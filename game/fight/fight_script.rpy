init python:
    class FightStance(SmartEnum):
        AGGRESSIVE = 1
        FORWARD = 2
        SOLID = 3
        DEFENSIVE = 4


    class BasePlayer:
        MAX_GUARD = FightStance.DEFENSIVE.value + 1 # Turtle stance bonus

        def __init__(self, name, stance, health=20, stamina=8, attack_multiplier=1, quirk=None):
            self.name = name
            self.stance = stance
            self.stamina = stamina
            self.max_health = health
            self.attack_multiplier = attack_multiplier
            self.quirk = quirk

            self.max_stamina = stamina
            self.stance_bonus = None

            self._health = health
            self._guard = stance.value

            self.wins = 0
            self.turn_moves = [Turtle(), EndTurn()]
            self.base_attacks = []
            self.special_attack = None
            self.previous_moves = []
            
        @property
        def health(self):
            return int(self._health)

        @health.setter
        def health(self, value):
            self._health = max(value, 0)

        @property
        def guard(self):
            return int(self._guard)

        @guard.setter
        def guard(self, value):
            self._guard = max(value, 0)

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

        def set_stance_bonus(self, move):
            if self.stance == move.ideal_stance:
                self.stance_bonus = move.name
            else:
                self.stance_bonus = None

        def get_primed_muliplier(self, fight, move):
            if isinstance(self, Player):
                return 1.0
            
            try:
                if fight.move_list[-1][fight.player.name].count(move.name) != 2:
                    return 1.0

                if self.health / float(self.max_health) <= 0.25: ### decimals!
                    return 0.7
                elif 0.25 < self.health / float(self.max_health) <= 0.5:
                    return 0.4
                else:
                    return 0.1
            
            except IndexError:
                return 1.0

        def get_reckless_multiplier(self, fight):
            if isinstance(self, Player):
                return 1.0

            try:
                if not isinstance(fight.move_list[-5][fight.player.name][-1], Turtle) and not isinstance(fight.move_list[-3][fight.player.name][-1], Turtle):
                    return 1.0

                if self.health / float(self.max_health) <= 0.25:
                    return 1.9
                elif 0.25 < self.health / float(self.max_health) <= 0.5:
                    return 1.6
                else:
                    return 1.3

            except IndexError:
                return 1.0

        def get_calculating_muliplier(self, fight):
            if isinstance(self, Player):
                return 0

            try:
                if fight.move_list[-4][self.name] != fight.move_list[-2][self.name]:
                    return 0

                if fight.opponent.fighter.health / float(fight.opponent.fighter.max_health) <= 0.25:
                    return 0.9
                elif 0.25 < fight.opponent.fighter.health / float(fight.opponent.fighter.max_health) <= 0.5:
                    return 0.6
                else:
                    return 0.3
            
            except IndexError:
                return 0

        def get_stance_multiplier(self, fight):
            if self.stance_bonus == "Body Hook":
                return 1.2

            # Stance Bonus: Kick
            if self.stance_bonus == "Kick" and self.stamina == 5:
                return 1.2

            return 1.0


    class Opponent(BasePlayer):
        def __init__(self, name, stance, health=20, stamina=8, attack_multiplier=1):
            BasePlayer.__init__(self, name, stance, health, stamina, attack_multiplier)

            self.stance_images = None

        @property
        def stance_image(self):
            return self.stance_images[self.stance]


    class Player(BasePlayer):
        pass


label move_attack(fight, target, attacker, move, move_damage):
    $ fight.stats[attacker.name]["damage_dealt"] += move_damage
    $ fight.stats[target.name]["damage_blocked"] += max(move_damage - target.guard, 0)

    if move_damage > target.guard and target.guard <= 0 and not attacker.stance_bonus == "Jab":
        $ fight.stats[attacker.name]["guards_broken"] += 1

        # Quirk: Backlash
        if isinstance(target.quirk, Backlash) or isinstance(attacker.quirk, Backlash):
            $ attacker.health -= 15

    if target.guard < move_damage or attacker.stance_bonus == "Jab":
        scene expression move.images["hit_image"]
        with vpunch

        $ target.health -= (damage - target.guard)
        $ target.guard = 0

    else:
        scene expression move.images["blocked_image"]
        with vpunch

        $ target.guard -= move.damage

    pause 1.0

    return


label fight_start_turn(fight, target, attacker):
    hide screen phone_icon

    scene black

    if attacker == fight.player.fighter:
        show text "Your Turn"
    else:
        show text "Opponent's turn"

    pause 1.0

    $ overwhelmed_multiplier = 1

    if attacker == fight.opponent.fighter:
        # Overwhelmed
        if len(fight.move_list[-1][target.name]) >= 4:
            if attacker.health / float(attacker.max_health) <= 0.25:
                $ overwhelmed_multiplier = 1.9
            elif 0.25 < attacker.health / float(attacker.max_health) <= 0.5:
                $ overwhelmed_multiplier = 1.6
            else:
                $ overwhelmed_multiplier = 1.3

    $ attacker.guard = round(attacker.stance.value * overwhelmed_multiplier)

    if isinstance(target.stance_bonus, Hook):
        $ attacker.stamina -= 2

    $ fight.move_list.append({attacker.name: []})

    if attacker == fight.player.fighter:
        call screen fight_player_turn(fight, attacker, target)
    else:
        call fight_attack_turn(fight, target, attacker) from _call_fight_attack_turn


label fight_attack_turn(fight, target, attacker, move=None):
    $ renpy.set_return_stack([])

    if move is None:
        if attacker.special_attack is not None and attacker.special_attack.is_sensitive(fight, target, attacker) and attacker.stamina >= attacker.special_attack.stamina_cost:
            $ move = attacker.special_attack
        elif filter(lambda move: move.ideal_stance == attacker.stance and move.stamina_cost <= attacker.stamina, attacker.base_attacks):
            $ move = renpy.random.choice(filter(lambda move: move.ideal_stance == attacker.stance, attacker.base_attacks))
        elif filter(lambda move: move.stamina_cost <= attacker.stamina, attacker.base_attacks + attacker.turn_moves):
            $ move = renpy.random.choice(filter(lambda move: move.stamina_cost <= attacker.stamina, attacker.base_attacks + attacker.turn_moves))

    $ fight.move_list[-1][attacker.name].append(move)

    if isinstance(move, EndTurn):
        $ attacker.stamina = attacker.max_stamina + min(attacker.stamina, 2)
        $ attacker.guard = attacker.stance.value
        call fight_start_turn(fight, attacker, target) from _call_fight_start_turn

    elif isinstance(move, Turtle):
        $ attacker.guard = FightStance.DEFENSIVE.value

        # Stance Bonus
        if attacker.stance == FightStance.SOLID:
            $ attacker.guard += 1

        call fight_start_turn(fight, attacker, target) from _call_fight_start_turn_1

    if hasattr(move, "images") and not move.images:
        $ raise NotImplementedError("Move {} is missing images.".format(move.name))

    $ attacker.stamina -= move.stamina_cost

    scene expression move.images["start_image"]
    pause 1.0

        # Player attacks
        # Opponent Approachs
    $ primed_multiplier = target.get_primed_muliplier(fight, move) 

    $ reckless_multiplier = target.get_reckless_multiplier(fight)

    if attacker == fight.player.fighter: 
        # Calculating
        $ attacker.health -= round(move.damage * target.get_calculating_muliplier(fight))

    # Stance Bonus
    $ stance_multiplier = target.get_stance_multiplier(fight)

    # Quirk: The Great Equalizer
    $ the_great_equalizer_multiplier = attacker.quirk.effect(target, attacker) if isinstance(attacker.quirk, TheGreatEqualizer) else 1.0

    # Quirk: In The Zone
    $ in_the_zone_multiplier = attacker.quirk.effect(attacker, move) if isinstance(attacker.quirk, InTheZone) else 1.0

    # Quirk: Double Time
    $ double_time_multiplier = 2.0 if isinstance(attacker.quirk, DoubleTime) or isinstance(target.quirk, DoubleTime) else 1.0

    # Quirk: All In
    $ all_in_multiplier = 2.0 if isinstance(attacker.quirk, DoubleTime) or isinstance(target.quirk, DoubleTime) else 1.0

    $ damage = round(move.damage * primed_multiplier * reckless_multiplier * stance_multiplier * the_great_equalizer_multiplier * in_the_zone_multiplier * double_time_multiplier * all_in_multiplier)

    # Seeing Red quirk
    if isinstance(attacker.quirk, SeeingRed) and not fight.moves_list[-1][attacker.name]:
        $ damage *= 2

    call move_attack(fight, target, attacker, move, damage) from _call_move_attack

    if target.health <= 0:
        show screen phone_icon
        jump expression fight.end_label

    # Set end stance
    if move.end_stance is not None:
        $ attacker.stance = move.end_stance

    if attacker.stamina > 0:
        if attacker == fight.player.fighter:
            call screen fight_player_turn(fight, fight.player.fighter, fight.opponent.fighter)
        else:
            call fight_attack_turn(fight, target, attacker) from _call_fight_attack_turn_1

    else:
        # Seeing Red quirk
        if isinstance(attacker.quirk, SeeingRed) and attacker.stance == FightStance.AGGRESSIVE:
            $ attacker.guard = 0
        else:
            $ attacker.guard = attacker.stance.value
        $ attacker.stamina = attacker.max_stamina
        call fight_start_turn(fight, attacker, target) from _call_fight_start_turn_2
