init python:
    class FightGameState(Enum):
        PLAYER_ATTACK = 0
        PLAYER_DEFENCE = 1
        OPPONENT_ATTACK = 2
        OPPONENT_DEFENCE = 3
        ERROR = 99


    class FightRank(Enum):
        UNDERDOG = {
            "win_requirement": 0,
            "bonus_attribute_points": 3
        }
        BRAWLER = {
            "win_requirement": 1,
            "bonus_attribute_points": 3
        }
        COMPETITOR = {
            "win_requirement": 3,
            "bonus_attribute_points": 4
        }
        GLADIATOR = {
            "win_requirement": 6,
            "bonus_attribute_points": 4
        }
        SAVAGE = {
            "win_requirement": 10,
            "bonus_attribute_points": 5
        }
        OVERDOG = {
            "win_requirement": 15,
            "bonus_attribute_points": 5
        }

        @staticmethod
        def next_rank(number_wins):
            return min(rank.value["win_requirement"] for rank in FightRank if rank.value["win_requirement"] > number_wins)


    class FightingStyle(Enum):
        STYLE_ONE = 1
        STYLE_TWO = 2
        STYLE_THREE = 3


    class AttackType(Enum):
        LIGHT = 0
        HEAVY = 1

        JAB = 2             # Breaks semi guard
        BODY_HOOK = 3       # Opponent doesn't gain stamina if blocked
        OVERHAND_PUNCH = 4  # Countering a heavy attack doesn't cost stamina

        HOOK = 5            # If hit, opponent loses all stamina
        UPPERCUT = 6        # Can't be countered
        KICK = 7            # If guard breaking deal more reduced damage


    class Guard(SmartEnum):
        LOW_GUARD = 0
        SEMI_GUARD = 1
        FULL_GUARD = 2


    class AttributeType(Enum):
        HEALTH = 0
        STAMINA = 1
        LIGHT_ATTACK_DAMAGE = 2
        HEAVY_ATTACK_DAMAGE = 3


    class SpecialAbilityType(Enum):
        PASSIVE = 0
        ACTIVE = 1

    
    class SpecialPassives(Enum):
        BERSERK = 0
        FULLY_CHARGED = 1
        COMBO = 2
        BRUISER = 3

    
    class SpecialActives(Enum):
        SECOND_WIND = 0
        RESET = 1
        FURY = 2
        DEVASTATING_FORCE = 3


    class Attack:
        def __init__(self, move_type, name, damage, stamina_cost, blocking_guard, images):
            self.move_type = move_type
            self.name = name
            self.damage = damage
            self.stamina_cost = stamina_cost
            self.blocking_guard = blocking_guard
            self.images = images
            

    class Defence:
        def __init__(self, move_type, stamina_cost):
            self.move_type = move_type
            self.stamina_cost = stamina_cost

    
    class Attribute:
        def __init__(self, type, name, value, description, passive_ability, active_ability):
            self.type = type
            self.name = name
            self.value = value
            self.description = description
            self.passive_ability = passive_ability
            self.active_ability = active_ability


    class BasePlayer:
        def __init__(self, fighting_style, guard=None, stamina=10, health=100, attack_multiplier=1):
            self.fighting_style = fighting_style
            self.guard = guard
            self.max_stamina = stamina
            self.max_health = health
            self.attack_multiplier = attack_multiplier
            
            self._stamina = stamina
            self._health = health

            self.wins = 0
            self.attacks = {
                AttackType.LIGHT: None,
                AttackType.HEAVY: None
            }
            self.attributes = []
            self.passive_abilities = set()
            self.special_abilities = set()
            self.special_ability = None
            self.previous_attack = None # Only successful attack

        @property
        def stamina(self):
            return self._stamina

        @stamina.setter
        def stamina(self, value):
            self._stamina = value
            self._stamina = min(self._stamina, self.max_stamina)
            
        @property
        def health(self):
            return self._health

        @health.setter
        def health(self, value):
            self._health = value
            self._health = max(self._health, 0)

        @property
        def rank(self):
            rv = FightRank.UNDERDOG
            for rank in FightRank:
                if rank.value["win_requirement"] > self.wins:
                    break
                rv = rank
            return rv

        def set_specials(self):
            for attr in self.attributes:
                if attr.value == 10:
                    self.special_abilities.add(attr.active_ability)
                    self.passive_abilities.add(attr.passive_ability)
                elif attr.value >= 5:
                    self.passive_abilities.add(attr.passive_ability)


    class Opponent(BasePlayer):
        def __init__(self, fighting_style, guard=None, stamina=10, health=100, attack_multiplier=1, guard_images=None):
            BasePlayer.__init__(self, fighting_style, guard, stamina, health, attack_multiplier)

            self.guard_images = guard_images

        @property
        def guard_image(self):
            return self.guard_images[self.guard]

        def set_specials(self):
            for attr in self.attributes:
                if attr.value >= 5:
                    self.passive_abilities.add(attr.passive_ability)

    
    class Player(BasePlayer):
        def __init__(self, fighting_style, guard=None, stamina=10, health=100, attack_multiplier=1):
            BasePlayer.__init__(self, fighting_style, guard, stamina, health, attack_multiplier)
            
            self.moves = {
                "q": None, # light attack
                "w": None, # heavy attack
                "e": None, # semi guard
                "r": None, # full guard
                "K_SPACE": None # Active ability
            }


label player_attack_turn(player_move, player, opponent):
    $ renpy.set_return_stack([])
    $ fight_game_state = FightGameState.PLAYER_ATTACK
    
    # If Guard.FULL_GUARD lose stamina
    if player.guard == Guard.FULL_GUARD:
        if player.stamina >= fight_full_guard_stamina_penalty:
            $ player.stamina -= fight_full_guard_stamina_penalty ## TODO: Fine tune stamina loss
        else:
            call opponent_attack_turn(player, opponent)

    if player.stamina < player_move.stamina_cost:
        call opponent_attack_turn(player, opponent)

    $ player.stamina -= player_move.stamina_cost

    # Player sets guard
    if isinstance(player_move.move_type, Guard):
        $ player.guard = player_move.move_type

        call opponent_attack_turn(player, opponent)

    # Player attacks
    else:
        scene expression player_move.images["start_image"]
        pause 0.5

        # Set player passive guard
        if player_move.move_type == AttackType.LIGHT:
            $ player.guard = Guard.SEMI_GUARD
            
        elif player_move.move_type == AttackType.HEAVY:
            $ player.guard = Guard.LOW_GUARD

        # Player attack hit        
        if opponent.guard < player_move.blocking_guard:

            # Opponent chance to counter
            if opponent.guard == Guard.SEMI_GUARD and opponent.stamina >= opponent.attacks[AttackType.LIGHT].stamina_cost:
                ## TODO: Add chance for counter
                call player_defence_turn(None, player, opponent.attacks[AttackType.LIGHT], opponent)

            scene expression player_move.images["hit_image"]
            with vpunch

            $ opponent.health -= player_move.damage

            show screen fight_popup("{} Hit".format(player_move.move_type.name))

        # Opponent blocked player's attack
        else:
            scene expression player_move.images["block_image"]
            with vpunch

            # Light attack blocked
            if player_move.move_type == AttackType.LIGHT:
                ## TODO: Clarify "Set to high guard after 2nd block"
                $ player.stamina += 3 ## TODO: Fine tune stamina gain
                show screen fight_popup("Blocked")

            # Heavy attack blocked
            else:
                $ opponent.health -= int(player_move.damage * 0.3) # Reduced damage

        if player_move.move_type == AttackType.HEAVY:
            $ opponent.guard = Guard.LOW_GUARD
            show screen fight_popup("Guard Shattered") 

        pause 1.0

        if opponent.health <= 0:
            jump expression fight_end_label

    call screen fight_attack


label player_defence_turn(player_move, player, opponent_attack, opponent):
    $ renpy.set_return_stack([])
    $ fight_game_state = FightGameState.PLAYER_DEFENCE

    # Set player move to None if no stamina and not overhand special effect 
    if player_move is not None and player.stamina < player_move.stamina_cost:
        $ player_move = None

    if player_move is not None:
        $ player.stamina -= player_move.stamina_cost

        ## Player Attack Moves
        if player_move.move_type == AttackType.LIGHT:
            $ player.guard = Guard.SEMI_GUARD

            # Player Counter Attack
            if opponent_attack.move_type == AttackType.HEAVY:
                call player_attack_turn(player_move, player, opponent)
        
        elif player_move.move_type == AttackType.HEAVY:
            $ player.guard = Guard.LOW_GUARD

        ## Defence Moves
        if player_move.move_type in Guard:
            $ player.guard = player_move.move_type

    # Opponent's attack hits
    if player.guard < opponent_attack.blocking_guard or player_move.move_type == AttackType.LIGHT:
        scene expression opponent_attack.images["hit_image"]
        with vpunch

        $ player.health -= opponent_attack.damage * opponent.attack_multiplier

        show screen fight_popup("{} HIT".format(opponent_attack.move_type.name))

    # Opponent's attack blocked
    else:
        scene expression opponent_attack.images["block_image"]
        with vpunch

        if opponent_attack.move_type == AttackType.HEAVY:
            $ player.health -= int(opponent_attack.damage * 0.3) # Reduced damage
            $ player.guard = Guard.LOW_GUARD
            show screen fight_popup("GUARD SHATTERED")
        else:
            show screen fight_popup("BLOCKED")

    pause 1

    if player.health <= 0:
        jump expression fight_end_label

    call screen fight_attack


label opponent_attack_turn(player, opponent):
    $ renpy.set_return_stack([])
    $ fight_game_state = FightGameState.OPPONENT_ATTACK

    if player.guard == Guard.FULL_GUARD: # Heavily favour heavy attack 
        $ p = (0.1, 0.9)
    elif opponent.attacks[AttackType.LIGHT].stamina_cost < opponent.stamina < opponent.attacks[AttackType.HEAVY].stamina_cost: # Heavily favour light attack
        $ p = (0.9, 0.1)
    else:
        $ p = (0.5, 0.5)

    $ opponent_move_type = weighted_choice((AttackType.LIGHT, AttackType.HEAVY), probability=p)
    $ opponent_move = opponent.attacks[opponent_move_type]

    # If Guard.FULL_GUARD lose stamina
    if opponent.guard == Guard.FULL_GUARD:
        if opponent.stamina >= fight_full_guard_stamina_penalty:
            $ opponent.stamina -= fight_full_guard_stamina_penalty ## TODO: Fine tune stamina loss
        else:
            call screen fight_attack

    if opponent_move.stamina_cost < opponent.stamina:
        $ opponent.stamina -= opponent_move.stamina_cost
        
        # Set opponent passive guard
        if opponent_move_type == AttackType.LIGHT:
            $ opponent.guard = Guard.SEMI_GUARD
        elif opponent_move_type == AttackType.HEAVY:
            $ opponent.guard = Guard.LOW_GUARD

        call screen fight_defense(opponent_move)

    else:
        $ opponent.guard = Guard.SEMI_GUARD
        call screen fight_attack


label fight_test:
    $ fight_game_state = FightGameState.ERROR
    python:
        opponent = Opponent(FightingStyle.STYLE_ONE, Guard.LOW_GUARD)
        player = Player(FightingStyle.STYLE_TWO, Guard.LOW_GUARD)

        opponent.attacks[AttackType.LIGHT] = OPPONENT_JAB
        opponent.attacks[AttackType.HEAVY] = OPPONENT_KICK

        opponent.guard_images = {
            Guard.FULL_GUARD: "images/v2/tomstancekick.webp",
            Guard.SEMI_GUARD: "images/v2/tomstancehook.webp",
            Guard.LOW_GUARD: "images/v2/tomstancejab.webp"
        }

        player.moves["q"] = PLAYER_JAB
        player.moves["w"] = PLAYER_HOOK
        player.moves["e"] = SEMI_GUARD
        player.moves["r"] = FULL_GUARD

        player.attributes.append(Attribute(AttributeType.HEALTH, "Health", 1, "", SpecialPassives.BERSERK, SpecialActives.SECOND_WIND))
        player.attributes.append(Attribute(AttributeType.STAMINA, "Stamina", 1, "", SpecialPassives.FULLY_CHARGED, SpecialActives.RESET))
        player.attributes.append(Attribute(AttributeType.LIGHT_ATTACK_DAMAGE, "Light Attack Damage", 1, "", SpecialPassives.COMBO, SpecialActives.FURY))
        player.attributes.append(Attribute(AttributeType.HEAVY_ATTACK_DAMAGE, "Heavy Attack Damage", 1, "", SpecialPassives.BRUISER, SpecialActives.DEVASTATING_FORCE))

        opponent.attributes.append(Attribute(AttributeType.HEALTH, "Health", 10, "", SpecialPassives.BERSERK, SpecialActives.SECOND_WIND))
        opponent.attributes.append(Attribute(AttributeType.STAMINA, "Stamina", 10, "", SpecialPassives.FULLY_CHARGED, SpecialActives.RESET))
        opponent.attributes.append(Attribute(AttributeType.LIGHT_ATTACK_DAMAGE, "Light Attack Damage", 10, "", SpecialPassives.COMBO, SpecialActives.FURY))
        opponent.attributes.append(Attribute(AttributeType.HEAVY_ATTACK_DAMAGE, "Heavy Attack Damage", 10, "", SpecialPassives.BRUISER, SpecialActives.DEVASTATING_FORCE))
        opponent.set_specials()

        opponent.wins = 2

    call screen fight_menu([
        PLAYER_JAB,
        PLAYER_BODY_HOOK,
        PLAYER_OVERHAND_PUNCH,
        PLAYER_HOOK,
        PLAYER_UPPERCUT,
        PLAYER_KICK
    ], "First Fight")

    label fight_start:

    show screen test_health
    show screen new_fight_overlay(player, opponent)

    call screen fight_attack
