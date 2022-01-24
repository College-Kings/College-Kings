init python:
    class AttackType:
        LIGHT = 0
        HEAVY = 1


    class Guard(SmartEnum):
        NO_GUARD = 0
        LOW_GUARD = 1
        SEMI_GUARD = 2
        FULL_GUARD = 3


    class Attack:
        def __init__(self, attack_type, counter_guard, image):
            self.attack_type = attack_type
            self.counter_guard = counter_guard
            self.image = image
            

    class Defence:
        def __init__(self, defence_type, image):
            self.defence_type = defence_type
            self.image = image


    class BasePlayer:
        def __init__(self, guard=None, stamina=10, health=100, attack_multiplier=1):
            self.guard = guard
            self.max_stamina = stamina
            self.max_health = health
            self.attack_multiplier = attack_multiplier
            
            self._stamina = stamina
            self._health = health

            self.attacks = {
                AttackType.LIGHT: None,
                AttackType.HEAVY: None
            }

        @property
        def stamina(self):
            return self._stamina

        @stamina.setter
        def stamina(self, value):
            self._stamina = value
            self._stamina = min(max(self._stamina, 0), self.max_stamina)
            
        @property
        def health(self):
            return self._health

        @health.setter
        def health(self, value):
            self._health = value
            self._health = max(self._health, 0)

        def change_health(self, value):
            current_health = self._health
            self._health += value

            renpy.show_screen("health_bar", current_health, self._health)


    class Opponent(BasePlayer):
        pass

    
    class Player(BasePlayer):
        def __init__(self, guard=None, stamina=10, health=100, attack_multiplier=1):
            BasePlayer.__init__(self, guard, stamina, health, attack_multiplier)
            
            self.moves = {
                "q": None, # light attack
                "w": None, # heavy attack
                "e": None, # semi guard
                "r": None # full guard
            }

        def turn(self, key, attack):
            move = self.moves[key]

            if isinstance(move, Attack): ## Attack Move
                if move.attack_type == AttackType.LIGHT: # Player light attack
                    self.guard = Guard.SEMI_GUARD

                    if attack.attack_type == AttackType.LIGHT: # Opponent light attack
                        opponent.guard = Guard.SEMI_GUARD
                        renpy.jump("opponent_light_hit")

                    else: # Opponent Heavy attack
                        opponent.guard = Guard.LOW_GUARD
                        opponent.stamina -= heavy_attack_stamina_cost # test
                        renpy.jump("player_light")

                elif move.attack_type == AttackType.HEAVY:
                    self.guard = Guard.LOW_GUARD
                    
                    if attack.attack_type == AttackType.LIGHT:
                        opponent.guard = Guard.SEMI_GUARD
                        renpy.jump("opponent_light_hit")
                    else:
                        opponent.guard = Guard.LOW_GUARD
                        renpy.jump("opponent_heavy_hit")

            elif isinstance(move, Defence): ## Defence Move
                if move.defence_type == Guard.SEMI_GUARD: # Player semi guard
                    self.guard = Guard.SEMI_GUARD

                    if attack.attack_type == AttackType.LIGHT: # Opponent light attack
                        opponent.guard = Guard.SEMI_GUARD
                        renpy.jump("opponent_light_block")

                    else: # Opponent Heavy attack
                        opponent.guard = Guard.LOW_GUARD
                        renpy.jump("opponent_heavy_hit")

                elif move.defence_type == Guard.FULL_GUARD: # Player full guard
                    self.guard = Guard.FULL_GUARD
                    
                    if attack.attack_type == AttackType.LIGHT:
                        opponent.guard = Guard.SEMI_GUARD
                        renpy.jump("opponent_light_block")
                    else:
                        opponent.guard = Guard.LOW_GUARD
                        renpy.jump("opponent_heavy_block")

    config.keymap["launch_editor"].remove('E')
    config.keymap["reload_game"].remove('R')
    renpy.clear_keymap_cache()

label fight_test:
    show screen test_health
    show screen health_bar(100, 100)

    python:
        opponent.attacks[AttackType.LIGHT] = Attack(AttackType.LIGHT, Guard.SEMI_GUARD, "images/v2/tomjab.webp")
        opponent.attacks[AttackType.HEAVY] = Attack(AttackType.HEAVY, Guard.FULL_GUARD, "images/v2/tomkick.webp")

        player.moves["q"] = Attack(AttackType.LIGHT, Guard.SEMI_GUARD, "images/v2/jab2start.webp")
        player.moves["w"] = Attack(AttackType.HEAVY, Guard.FULL_GUARD, "images/v2/hook2start.webp")
        player.moves["e"] = Defence(Guard.SEMI_GUARD, "images/v2/tomjab.webp")
        player.moves["r"] = Defence(Guard.FULL_GUARD, "images/v2/tomjab.webp")

    menu:

        "Easy":
            $ fight_reaction_time = 1.5

        "Medium":
            $ fight_reaction_time = 1

        "Hard":
            $ fight_reaction_time = 0.75

        "Impossible":
            $ fight_reaction_time = 0.5



    call screen fight_neutral

label player_light:

    if (player.stamina >= light_attack_stamina_cost and player.guard < Guard.FULL_GUARD) or player.stamina >= (light_attack_stamina_cost + full_guard_stamina_cost):

        $ player.guard = Guard.SEMI_GUARD
        $ player.stamina -= light_attack_stamina_cost

        scene jab2start

        pause 0.5

        if opponent.guard == Guard.LOW_GUARD: # opponent no guard

            scene jab2pic # Player hits
            with vpunch

            show screen fight_popup("Light Hit")

            pause 1

            $ opponent.health -= player_light_attack_damage

            call screen fight_neutral

        elif opponent.guard == Guard.SEMI_GUARD: #opponent semi guard

            scene jab1pic # Opponent blocks hits
            with vpunch

            show screen fight_popup("Blocked")

            pause 1

            $ opponent.stamina += light_block_stamina_gain
            $ player_fury += 1

            if player_fury == 2: # opponent goes into full guard

                $ opponent.guard = Guard.FULL_GUARD 
                $ player_fury = 0

            call screen fight_neutral
            
        else: # opponent full guard
            
            scene jab1pic # Opponent blocks hits
            with vpunch

            show screen fight_popup("Blocked")

            pause 1

            call screen fight_neutral

    else:

        jump opponent_attacks

label player_heavy:

    if (player.stamina >= heavy_attack_stamina_cost and player.guard < Guard.FULL_GUARD) or player.stamina >= (heavy_attack_stamina_cost + full_guard_stamina_cost):

        $ player.guard = Guard.LOW_GUARD
        $ player.stamina -= heavy_attack_stamina_cost

        scene hook2start

        pause 0.5

        if opponent.guard == Guard.LOW_GUARD: # opponent no guard

            scene hook2pic # Player hits
            with vpunch

            show screen fight_popup("Heavy Hit")

            pause 1

            $ opponent.health -= player_heavy_attack_damage

            call screen fight_neutral

        elif opponent.guard == Guard.SEMI_GUARD: #opponent semi guard

            $ opponent_attack = renpy.random.choice([AttackType.LIGHT, AttackType.HEAVY])

            if opponent.stamina >= light_attack_stamina_cost and opponent_attack == AttackType.LIGHT: # opponent counters

                call screen fight_defense(opponent.attacks[opponent_attack])
                
            else: # player hits

                scene hook2pic # Player hits
                with vpunch

                show screen fight_popup("Heavy Hit")

                pause 1

                $ opponent.health -= player_heavy_attack_damage
                $ opponent.guard = Guard.LOW_GUARD

                call screen fight_neutral
            
        else: # opponent full guard
            scene hook1pic # Opponent blocks hits
            with vpunch

            show screen fight_popup("Guard Shattered")

            $ opponent.health -= player_heavy_attack_negated_damage #negated damage

            pause 1
            
            $ opponent.guard = Guard.LOW_GUARD

            call screen fight_neutral

    else:

        jump opponent_attacks

label player_semi_guard: #player changes to semi guard

    $ player.guard = Guard.SEMI_GUARD

    jump opponent_attacks

label player_full_guard: #player changes to full guard

    $ player.guard = Guard.FULL_GUARD

    jump opponent_attacks

label opponent_attacks:
    
    if (opponent.stamina >= heavy_attack_stamina_cost and opponent.guard < Guard.FULL_GUARD) or opponent.stamina >= (heavy_attack_stamina_cost + full_guard_stamina_cost): # opponent has enough stamina for heavy attack

        if player.guard == Guard.LOW_GUARD: # player low  or full guard

            call screen fight_defense(opponent.attacks[renpy.random.choice([AttackType.LIGHT, AttackType.HEAVY])]) #opponent can attack light or heavy

        elif player.guard == Guard.FULL_GUARD:

            call screen fight_defense(opponent.attacks[AttackType.HEAVY])

        else: # player has semi guard

            call screen fight_defense(opponent.attacks[renpy.random.choice([AttackType.LIGHT, AttackType.HEAVY])]) #opponent can attack light or heavy
 
    elif (opponent.stamina >= light_attack_stamina_cost and opponent.guard < Guard.FULL_GUARD) or opponent.stamina >= (light_attack_stamina_cost + full_guard_stamina_cost): # opponent has enough stamina for light attack

        call screen fight_defense(opponent.attacks[AttackType.LIGHT])
        
    else: # opponent doesn't have enough stamina to attack
        $ opponent.guard = Guard.SEMI_GUARD

        $ opponent.stamina += 4

        $ player.stamina += 4

        call screen fight_neutral

label opponent_light_hit:

        $ opponent.stamina -= light_attack_stamina_cost

        scene tomjabhit
        with vpunch

        $ player.health -= opponent_light_attack_damage

        show screen fight_popup("LIGHT HIT")

        pause 1

        call screen fight_neutral

label opponent_light_block:

        $ opponent.stamina -= light_attack_stamina_cost

        scene tomjabblock
        with vpunch

        if player.guard == Guard.SEMI_GUARD:
            $ player.stamina += light_block_stamina_gain

        show screen fight_popup("BLOCKED")

        pause 1

        call screen fight_neutral


label opponent_heavy_hit:

        $ opponent.stamina -= heavy_attack_stamina_cost

        scene tomkickhit
        with vpunch

        $ player.health -= opponent_heavy_attack_damage

        show screen fight_popup("HEAVY HIT")

        pause 1

        call screen fight_neutral

label opponent_heavy_block:

        $ opponent.stamina -= heavy_attack_stamina_cost

        scene tomkickblock
        with vpunch

        $ player.health -= opponent_heavy_attack_negated_damage #Negated Damage
        $ player.guard = Guard.LOW_GUARD

        show screen fight_popup("GUARD SHATTERED")

        pause 1

        call screen fight_neutral


