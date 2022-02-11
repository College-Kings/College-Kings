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


    class FightingStance(Enum):
        NEUTRAL = 0
        LOST_FOOTING = 1


    class AttackType(Enum):
        LIGHT = 0
        HEAVY = 1

        JAB = 2             # Breaks semi guard
        BODY_HOOK = 3       # Opponent doesn't gain stamina if blocked
        OVERHAND_PUNCH = 4  # Countering a heavy attack doesn't cost stamina

        HOOK = 5            # If hit, opponent loses all stamina
        UPPERCUT = 6        # Can't be countered
        KICK = 7            # If guard breaking deal more reduced damage


    class DefensiveMove(Enum):
        DODGE = 0
        BLOCK = 1


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
        def __init__(self, move_type, name, damage, stamina_cost, images=None):
            self.move_type = move_type
            self.name = name
            self.damage = damage
            self.stamina_cost = stamina_cost
            self.images = images

        def copy(self, images=None):
            return self.__class__(self.move_type, self.name, self.damage, self.stamina_cost, images)       


    class Defence:
        def __init__(self, name, stamina_cost, image=None):
            self.name = name
            self.stamina_cost = stamina_cost
            self.image = image

        def copy(self, image=None):
            return self.__class__(self.name, self.stamina_cost, image)       
    

    class Attribute:
        def __init__(self, type, name, value, description, passive_ability, active_ability):
            self.type = type
            self.name = name
            self.value = value
            self.description = description
            self.passive_ability = passive_ability
            self.active_ability = active_ability


    class BasePlayer:
        def __init__(self, fighting_style, stance, stamina=10, health=100, attack_multiplier=1, images=None):
            self.fighting_style = fighting_style
            self.stance = stance
            self.max_stamina = stamina
            self.max_health = health
            self.attack_multiplier = attack_multiplier
            self.images = images

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

        @property
        def stance_image(self):
            return self.images[self.stance]

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
        def set_specials(self):
            for attr in self.attributes:
                if attr.value >= 5:
                    self.passive_abilities.add(attr.passive_ability)

    
    class Player(BasePlayer):
        def __init__(self, fighting_style, stance, stamina=10, health=100, attack_multiplier=1, images=None):
            BasePlayer.__init__(self, fighting_style, stance, stamina, health, attack_multiplier, images)
            
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
    
    if isinstance(player_move, Defence):
        if player.stamina >= player_move.stamina_cost:
            $ player.stamina -= player_move.stamina_cost
            scene expression player_move.image
            pause 0.5

        call opponent_attack_turn(player, opponent)

    if player.stamina < player_move.stamina_cost:
        call opponent_attack_turn(player, opponent)

    $ player.stamina -= player_move.stamina_cost

    # Player attacks
    scene expression player_move.images["start_image"]
    pause 0.5

    $ opponent_move = renpy.random.choice((BLOCK, DODGE, None))

    if opponent_move is not None:
        if opponent.stamina < opponent_move.stamina_cost:
            $ opponent_move = None
        else:
            $ opponent.stamina -= opponent_move.stamina_cost

    # Player attack hits opponent
    if opponent_move is None:
        scene expression player_move.images["hit_image"]
        with vpunch

        $ opponent.health -= player_move.damage

        show screen fight_popup("{} Hit".format(player_move.move_type.name))

    # Opponent blocked player's attack
    elif opponent_move == BLOCK:
        scene expression player_move.images["block_image"]
        with vpunch

    # Opponent dodged player's attack
    elif opponent_move == DODGE:
        scene expression player_move.images["dodge_image"]
        with vpunch

    pause 1.0

    if opponent.health <= 0:
        jump expression fight_end_label

    call screen fight_attack(player, opponent)


label player_defence_turn(timing_var, player_move, player, opponent_attack, opponent):
    $ renpy.set_return_stack([])
    $ fight_game_state = FightGameState.PLAYER_DEFENCE

    # Set player move to None if no stamina and not overhand special effect 
    if player_move is not None and player.stamina < player_move.stamina_cost:
        $ player_move = None

    if player_move is None or isinstance(player_move, Attack):
        call opponent_attack_hit(opponent_attack, player, opponent)

    else:
        if opponent_attack.move_type == AttackType.LIGHT:
            if player_move.name == DefensiveMove.BLOCK:
                if timing_var > 65: # Late
                    call opponent_attack_hit(opponent_attack, player, opponent)

                elif timing_var < 35: # Early
                    call opponent_attack_blocked(opponent_attack, player, opponent)

                else: # Perfect
                    call opponent_lost_footing(player, opponent)

            elif player_move.name == DefensiveMove.DODGE:
                if 35 < timing_var < 65: # Perfect
                    call opponent_attack_dodged(opponent_attack)

                else: # Late / Early
                    call opponent_attack_hit(opponent_attack, player, opponent)

        elif opponent_attack.move_type == AttackType.HEAVY:
            if player_move.name == DefensiveMove.BLOCK:
                if timing_var > 65: # Late
                    call opponent_attack_hit(opponent_attack, player, opponent)

                else: # Perfect
                    call player_lost_footing(player, opponent)

            elif player_move.name == DefensiveMove.DODGE:
                if 35 < timing_var < 65: # Perfect
                    call opponent_attack_dodged(opponent_attack)

                else: # Late / Early
                    call opponent_attack_hit(opponent_attack, player, opponent)

    pause 1

    if player.health <= 0:
        jump expression fight_end_label

    call screen fight_attack


label opponent_attack_hit(opponent_attack, player, opponent):
    scene expression opponent_attack.images["hit_image"]
    with vpunch

    $ player.health -= opponent_attack.damage * opponent.attack_multiplier

    show screen fight_popup("{} HIT".format(opponent_attack.move_type.name))
    
    return


label opponent_attack_blocked(opponent_attack, player, opponent):
    scene expression opponent_attack.images["block_image"]
    with vpunch

    if opponent_attack.move_type == AttackType.HEAVY:
        call player_lost_footing(player, opponent)
    else:
        show screen fight_popup("BLOCKED")

    return


label opponent_attack_dodged(opponent_attack):
    scene expression opponent_attack.images["dodge_image"]
    with vpunch

    show screen fight_popup("DODGED")

    return


label opponent_lost_footing(player, opponent):
    scene expression opponent.images[FightingStance.LOST_FOOTING]
    with vpunch

    $ opponent.stance = FightingStance.LOST_FOOTING

    show screen fight_popup("LOST FOOTING")
    call screen fight_attack(player, opponent)

    return


label player_lost_footing(player, opponent):
    scene expression player.images[FightingStance.LOST_FOOTING]
    with vpunch

    $ player.stance = FightingStance.LOST_FOOTING

    show screen fight_popup("LOST FOOTING")
    call screen opponent_attack_turn(player, opponent)

    return


label opponent_attack_turn(player, opponent):
    $ renpy.set_return_stack([])
    $ fight_game_state = FightGameState.OPPONENT_ATTACK

    $ p = (0.5, 0.5)

    $ opponent_move_type = weighted_choice((AttackType.LIGHT, AttackType.HEAVY), probability=p)
    $ opponent_move = opponent.attacks[opponent_move_type]

    if opponent_move.stamina_cost < opponent.stamina:
        $ opponent.stamina -= opponent_move.stamina_cost

        call screen fight_defense(opponent_move)

    else: # TODO: Check if stack
        call screen fight_attack


label fight_test:
    $ fight_game_state = FightGameState.ERROR

    python:
        player = Player(FightingStyle.STYLE_TWO, FightingStance.NEUTRAL, images={
            FightingStance.NEUTRAL: "fight_prototype/images/player_neutral_stance.png",
            FightingStance.LOST_FOOTING: "fight_prototype/images/player_lost_footing.png",
        })
        opponent = Opponent(FightingStyle.STYLE_ONE, FightingStance.NEUTRAL, images={
            FightingStance.NEUTRAL: "fight_prototype/images/opponent_neutral_stance.png",
            FightingStance.LOST_FOOTING: "fight_prototype/images/opponent_lost_footing.png"
        })

        player.moves["q"] = JAB.copy({
            "start_image": "fight_prototype/images/player_start_jab.webp",
            "hit_image": "fight_prototype/images/player_hit_jab.webp",
            "block_image": "fight_prototype/images/player_jab_blocked.webp",
            "dodge_image": "fight_prototype/images/player_jab_dodged.png"
        })
        player.moves["w"] = HOOK.copy({
            "start_image": "fight_prototype/images/player_start_hook.webp",
            "hit_image": "fight_prototype/images/player_hit_hook.webp",
            "block_image": "fight_prototype/images/player_hook_blocked.webp",
            "dodge_image": "fight_prototype/images/player_hook_dodged.png"
        })
        player.moves["e"] = BLOCK.copy("fight_prototype/images/player_block.webp")
        player.moves["r"] = DODGE.copy("fight_prototype/images/player_dodge.png")

        opponent.attacks[AttackType.LIGHT] = JAB.copy({
            "start_image": "fight_prototype/images/opponent_start_jab.webp",
            "hit_image": "fight_prototype/images/opponent_hit_jab.webp",
            "block_image": "fight_prototype/images/opponent_jab_blocked.webp",
            "dodge_image": "fight_prototype/images/opponent_jab_dodged.png"
        })
        opponent.attacks[AttackType.HEAVY] = KICK.copy({
            "start_image": "fight_prototype/images/opponent_start_kick.webp",
            "hit_image": "fight_prototype/images/opponent_hit_kick.webp",
            "block_image": "fight_prototype/images/opponent_kick_blocked.webp",
            "dodge_image": "fight_prototype/images/opponent_kick_dodged.png"
        })

        opponent.wins = 2

    call screen fight_menu([
        JAB,
        HOOK,
        PUNCH,
        HOOK,
        UPPERCUT,
        KICK
    ], "First Fight")

    label fight_start:

    show screen test_health
    show screen new_fight_overlay(player, opponent)

    call opponent_attack_turn(player, opponent)
