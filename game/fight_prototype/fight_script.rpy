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
                if move.defence_type == "semi_guard": # Player semi guard
                    self.guard = Guard.SEMI_GUARD

                    if attack.attack_type == AttackType.LIGHT: # Opponent light attack
                        opponent.guard = Guard.SEMI_GUARD
                        renpy.jump("opponent_light_block")

                    else: # Opponent Heavy attack
                        opponent.guard = Guard.LOW_GUARD
                        renpy.jump("opponent_heavy_hit")

                elif move.defence_type == "full_guard": # Player full guard
                    self.guard = Guard.FULL_GUARD
                    
                    if attack.attack_type == AttackType.LIGHT:
                        opponent.guard = Guard.SEMI_GUARD
                        renpy.jump("opponent_light_block")
                    else:
                        opponent.guard = Guard.LOW_GUARD
                        renpy.jump("opponent_heavy_block")

            else:
                raise TypeError("SOMETHING WENT WRONG!")



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


    call screen fight_neutral

label player_light:

    if (player.stamina >= 2 and player.guard < Guard.FULL_GUARD) or player.stamina >= 4:

        $ player.guard = Guard.SEMI_GUARD
        $ player.stamina -= 2

        scene jab2start

        pause 0.5

        if opponent.guard == Guard.LOW_GUARD: # opponent no guard

            scene jab2pic # Player hits
            with vpunch

            show screen fight_popup("Light Hit")

            pause 1

            $ opponent.health -= 5

            call screen fight_neutral

        elif opponent.guard == Guard.SEMI_GUARD: #opponent semi guard

            scene jab1pic # Opponent blocks hits
            with vpunch

            show screen fight_popup("Blocked")

            pause 1

            $ opponent.stamina += 5

            $ opponent_shielding_chance = renpy.random.value([0,1,2])

            if opponent_shielding_chance == 2: # opponent goes into full guard

                $ opponent.guard == Guard.FULL_GUARD 
                $ opponent_shielding_chance = 0

            call screen fight_neutral
            
        else: # opponent full guard
            
            scene jab1pic # Opponent blocks hits
            with vpunch

            show screen fight_popup("Blocked")

            pause 1

            $ opponent.stamina += 5

            call screen fight_neutral

    else:

        jump opponent_attacks

label player_heavy:

    if (player.stamina >= 5 and player.guard < Guard.FULL_GUARD) or player.stamina >= 7:

        $ player.guard = Guard.LOW_GUARD
        $ player.stamina -= 5

        scene hook2start

        pause 0.5

        if opponent.guard == Guard.LOW_GUARD: # opponent no guard

            scene hook2pic # Player hits
            with vpunch

            show screen fight_popup("Heavy Hit")

            pause 1

            $ opponent.health -= 10

            call screen fight_neutral

        elif opponent.guard == Guard.SEMI_GUARD: #opponent semi guard

            $ opponent_attack = renpy.random.choice([AttackType.LIGHT, AttackType.HEAVY])

            if opponent.stamina >= 2 and opponent_attack == AttackType.LIGHT: # opponent counters

                call screen fight_defense(opponent.attacks[opponent_attack])
                
            else: # player hits

                scene hook2pic # Player hits
                with vpunch

                show screen fight_popup("Heavy Hit")

                pause 1

                $ opponent.health -= 10
                $ opponent.guard = Guard.LOW_GUARD

                call screen fight_neutral
            
        else: # opponent full guard
            scene hook1pic # Opponent blocks hits
            with vpunch

            show screen fight_popup("Guard Shattered")

            $ opponent.health -= 2 #negated damage

            pause 1
            
            $ opponent.guard = Guard.LOW_GUARD
            $ opponent.stamina += 5

            call screen fight_neutral

    else:

        jump opponent_attacks

label player_semi_guard: #player changes to semi guard

    $ player.guard = Guard.SEMI_GUARD
    $ player.stamina += 5

    jump opponent_attacks

label player_full_guard: #player changes to full guard

    $ player.guard = Guard.FULL_GUARD
    $ player.stamina += 5

    jump opponent_attacks

label opponent_attacks:
    
    if (opponent.stamina >= 5 and opponent.guard < Guard.FULL_GUARD) or opponent.stamina >= 7: # opponent has enough stamina for heavy attack

        if player.guard == Guard.LOW_GUARD or player.guard == Guard.FULL_GUARD: # player low  or full guard

            call screen fight_defense(opponent.attacks[AttackType.HEAVY])

        else: # player has semi guard

            call screen fight_defense(opponent.attacks[renpy.random.choice([AttackType.LIGHT, AttackType.HEAVY])]) #opponent can attack light or heavy
 
    elif (opponent.stamina >= 2 and opponent.guard < Guard.FULL_GUARD) or opponent.stamina >= 4: # opponent has enough stamina for light attack

        call screen fight_defense(opponent.attacks[AttackType.LIGHT])
        
    else: # opponent doesn't have enough stamina to attack
        $ opponent.guard = Guard.SEMI_GUARD
        $ opponent.stamina += 5

        call screen fight_neutral

label opponent_light_hit:

        scene tomjabhit
        with vpunch

        $ player.health -= 5

        show screen fight_popup("LIGHT HIT")

        pause 1

        call screen fight_neutral

label opponent_light_block:

        scene tomjabblock
        with vpunch

        $ player.stamina += 5

        show screen fight_popup("BLOCKED")

        pause 1

        call screen fight_neutral


label opponent_heavy_hit:

        scene tomkickhit
        with vpunch

        $ player.health -= 10

        show screen fight_popup("HEAVY HIT")

        pause 1

        call screen fight_neutral

label opponent_heavy_block:

        scene tomkickblock
        with vpunch

        $ player.stamina += 5
        $ player.health -= 2 #Negated Damage
        $ player.guard = Guard.LOW_GUARD

        show screen fight_popup("GUARD SHATTERED")

        pause 1

        call screen fight_neutral


