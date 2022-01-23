init python:
    class Guard(SmartEnum):
        NO_GUARD = 0
        LOW_GUARD = 1
        SEMI_GUARD = 2
        HIGH_GUARD = 3


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
                "light": None,
                "heavy": None
            }

        @property
        def stamina(self):
            return self._stamina

        @stamina.setter
        def stamina(self, value):
            self._stamina += value
            
        @property
        def health(self):
            return self._health

        @health.setter
        def health(self, value):
            self._health += value

        def change_health(self, value):
            current_health = self._health
            self._health += value

            renpy.show_screen("health_bar", current_health, self._health)


    class Opponent(BasePlayer):
        pass

    
    class Player(BasePlayer):
        def __init__(self, guard, stamina, health, attack_multiplier):
            BaseAttack.__init__(self, guard, stamina, health, attack_multiplier)
            
            self.moves = {
                "q": None, # light attack
                "w": None, # heavy attack
                "e": None, # semi guard
                "r": None # full guard
            }

        def turn(self, key, attack):
            move = self.moves[key]
            attack = opponent.attacks[attack]

            try: ## Attack Move
                if move.attack_type == "light": # Player light attack
                    self.guard = Guard.SEMI_GUARD

                    if attack.attack_type == "light": # Opponent light attack
                        opponent.guard = Guard.SEMI_GUARD
                        renpy.jump("opponent_light_hit")

                    else: # Opponent Heavy attack
                        opponent.guard = Guard.LOW_GUARD
                        renpy.jump("player_light")

                elif move.attack_type == "heavy":
                    self.guard = Guard.LOW_GUARD
                    
                    if attack.attack_type == "light":
                        opponent.guard = Guard.SEMI_GUARD
                    else:
                        opponent.guard = Guard.LOW_GUARD

                    renpy.jump("opponent_light_hit")

            except AttributeError: ## Defence Move
                if move.defence_type == "semi_guard": # Player semi guard
                    self.guard = Guard.SEMI_GUARD

                    if attack.attack_type == "light": # Opponent light attack
                        opponent.guard = Guard.SEMI_GUARD
                        renpy.jump("opponent_light_block")

                    else: # Opponent Heavy attack
                        opponent.guard = Guard.LOW_GUARD
                        renpy.jump("opponent_heavy_hit")

                elif move.attack_type == "full_guard": # Player full guard
                    self.guard = Guard.FULL_GUARD
                    
                    if attack.attack_type == "light":
                        opponent.guard = Guard.SEMI_GUARD
                    else:
                        opponent.guard = Guard.LOW_GUARD

                    renpy.jump("opponent_light_block")


label fight_test:
    show screen test_health
    show screen opponent_health_bar(100, 100)
    opponent = Opponent(Guard.LOW_GUARD)
    player = Player(Guard.LOW_GUARD)

    opponent.light = BaseAttack("images/v2/tomjab.webp")

    call screen fight_neutral

label player_light:

    if (player.stamina >= 2 and player_guard < 2) or player.stamina >= 4:

        $ player_guard = 1
        $ player.stamina -= 2

        scene jab2start

        pause 0.5

        if opponent_guard == 0: # opponent no guard

            scene jab2pic # Player hits
            with vpunch

            show screen fight_popup("Light Hit")

            pause 1

            $ opponent.health -= 5

            call screen fight_neutral

        elif oppponent_guard == 1: #opponent semi guard

            scene jab1pic # Opponent blocks hits
            with vpunch

            show screen fight_popup("Blocked")

            pause 1

            $ opponent_stamina += 5

            $ opponent_shielding_chance = renpy.random.value([0,1,2])

            if opponent_shielding_chance == 2: # opponent goes into full guard

                $ opponent_guard == 2 
                $ opponent_shielding_chance = 0

            call screen fight_neutral
            
        else: # opponent full guard
            
            scene jab1pic # Opponent blocks hits
            with vpunch

            show screen fight_popup("Blocked")

            pause 1

            $ opponent_stamina += 5

            call screen fight_neutral

    else:

        jump opponent_attacks

label player_heavy:

    if (player_stamina >= 5 and player_guard < 2) or player_stamina >= 7:

        $ player_guard = 0
        $ player_stamina -= 5

        scene hook2start

        pause 0.5

        if opponent_guard == 0: # opponent no guard

            scene hook2pic # Player hits
            with vpunch

            show screen fight_popup("Heavy Hit")

            pause 1

            $ opponent.health -= 10

            call screen fight_neutral

        elif oppponent_guard == 1: #opponent semi guard

            $ opponent_attack = renpy.random.choice([0, 1])

            if opponent_stamina >= 2 and opponent_attack == 0: # opponent counters

                call screen fight_defense
                
            else: # player hits

                scene hook2pic # Player hits
                with vpunch

                show screen fight_popup("Heavy Hit")

                pause 1

                $ opponent.health -= 10
                $ opponent_guard = 0 

                call screen fight_neutral
            
        else: # opponent full guard
            scene hook1pic # Opponent blocks hits
            with vpunch

            show screen fight_popup("Guard Shattered")

            $ opponent.health -= 2 #negated damage

            pause 1
            
            $ opponent_guard = 0
            $ opponent_stamina += 5

            call screen fight_neutral

    else:

        jump opponent_attacks

label player_semi_guard: #player changes to semi guard

    $ player_guard == 1:
    $ player_stamina += 5

    jump opponent_attacks

label player_full_guard: #player changes to full guard

    $ player_guard == 2:
    $ player_stamina += 5

    jump opponent_attacks

label opponent_attacks:
    
    if (opponent_stamina >= 5 and opponent_guard < 2) or opponent_stamina >= 7: # opponent has enough stamina for heavy attack

        if player_guard == 0 or playerguard == 2: # player low  or full guard

            $ opponent_attack = 1 # opponent does a heavy attack

        else: # player has semi guard

            $ opponent_attack = renpy.random.choice([0, 1]) #opponent can attack light or heavy

        call screen fight_defense

    elif (opponent_stamina >= 2 and opponent_guard < 2) or opponent_stamina >= 4: # opponent has enough stamina for light attack

        $ opponent_attack = 0 # opponent does a light attack

        call screen fight_defense
        
    else: # opponent doesn't have enough stamina to attack
        $ opponent_guard = 1
        $ opponent_stamina += 5

        call screen fight_neutral

label opponent_light_hit:

        scene tomjabhit
        with vpunch

        $ player_health -= 5

        show screen fight_popup("LIGHT HIT")

        pause 1

        call screen fight_neutral

label opponent_light_block:

        scene tomjabblock
        with vpunch

        $ player_stamina += 5

        show screen fight_popup("BLOCKED")

        pause 1

        call screen fight_neutral


label opponent_heavy_hit:

        scene tomhookhit
        with vpunch

        $ player_health -= 10

        show screen fight_popup("HEAVY HIT")

        pause 1

        call screen fight_neutral

label opponent_heavy_block:

        scene tomhookblock
        with vpunch

        $ player_stamina += 5
        $ player_health -= 2 #Negated Damage
        $ player_guard = 0

        show screen fight_popup("GUARD SHATTERED")

        pause 1

        call screen fight_neutral


