init python:
    class FightGameState(Enum):
        PLAYER_ATTACK = 0
        PLAYER_DEFENCE = 1
        OPPONENT_ATTACK = 2
        OPPONENT_DEFENCE = 3
        ERROR = 99


    class FightStance(SmartEnum):
        AGGRESSIVE = 1
        FORWARD = 2
        SOLID = 3
        DEFENSIVE = 4


    class BasePlayer:
        MAX_GUARD = FightStance.DEFENSIVE.value + 1 # Turtle stance bonus

        def __init__(self, name, stance, health=20, stamina=8, attack_multiplier=1):
            self.name = name
            self.stance = stance
            self.stamina = stamina
            self.max_health = health
            self.attack_multiplier = attack_multiplier

            self.max_stamina = stamina
            self.stance_bonus = None
            self.guard_broken = 0

            self._health = health
            self._guard = stance.value

            self.wins = 0
            self.turn_moves = []
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

        def add_previous_move(self, move):
            self.previous_moves.append(move.name)

        def reset_previous_moves(self):
            self.previous_moves = []

        def set_stance_bonus(self, move):
            if self.stance == move.ideal_stance:
                self.stance_bonus = move.name
            else:
                self.stance_bonus = None


    class Opponent(BasePlayer):
        def __init__(self, name, stance, health=20, stamina=8, attack_multiplier=1, stance_images=None):
            BasePlayer.__init__(self, name, stance, health, stamina, attack_multiplier)

            self.stance_images = stance_images

        @property
        def stance_image(self):
            return self.stance_images[self.stance]

    
    class Player(BasePlayer):
        pass


default fight_previous_moves = []


label move_attack(target, move, move_damage, ignore_guard=False):
    if move_damage > target.guard and target.guard <= 0:
        $ target.guard_broken += 1

    if target.guard < move_damage or ignore_guard:
        scene expression move.images["hit_image"]
        with vpunch

        $ target.health -= (damage - target.guard)
        $ target.guard = 0

        show screen fight_popup("{} Hit".format(move.name))

    else:
        scene expression move.images["blocked_image"]
        with vpunch

        $ target.guard -= move.damage

        show screen fight_popup("{} Blocked".format(move.name))

    pause 1.0

    return


label fight_start_player_turn(player, opponent):
    hide screen fight_opponent_turn
    scene black
    show text "Your Turn"
    pause 1.0

    $ player.guard = player.stance.value
    $ fight_previous_moves.append({opponent.name: opponent.previous_moves.copy()})
    $ opponent.reset_previous_moves()

    call screen fight_player_turn(player, opponent)


label player_attack_turn(player_move, player, opponent):
    $ renpy.set_return_stack([])
    $ fight_game_state = FightGameState.PLAYER_ATTACK
    $ player.add_previous_move(player_move)

    if player_move == END_TURN:
        $ player.stamina = player.max_stamina + min(player.stamina, 2)
        $ player.guard = player.stance.value
        call fight_start_opponent_turn(player, opponent)

    elif player_move == TURTLE:
        $ player.guard = FightStance.DEFENSIVE.value

        # Stance Bonus
        if player.stance == FightStance.SOLID:
            $ player.guard += 1

        call fight_start_opponent_turn(player, opponent)

    if hasattr(player_move, "images") and player_move.images is None:
        $ raise NotImplementedError("Player move is missing images.")

    $ player.stamina -= player_move.stamina_cost

    scene expression player_move.images["start_image"]
    pause 1.0

    # Player attacks
    # Opponent Approachs
    # Primed
    $ primed_multiplier = 1.0

    if len(fight_previous_moves) >= 2 and fight_previous_moves[-2][name].count(player_move.name) == 2:
        if opponent.health / opponent.max_health <= 0.25:
            $ primed_multiplier = 0.7
        elif 0.25 < opponent.health / opponent.max_health <= 0.5:
            $ primed_multiplier = 0.4
        else:
            $ primed_multiplier = 0.1

    # Reckless
    $ reckless_multiplier = 1.0

    if len(fight_previous_moves) >= 4 and fight_previous_moves[-2][name][-1] == "Turtle" and fight_previous_moves[-4][name][-1] == "Turtle":
        if opponent.health / opponent.max_health <= 0.25:
            $ reckless_multiplier = 1.9
        elif 0.25 < opponent.health / opponent.max_health <= 0.5:
            $ reckless_multiplier = 1.6
        else:
            $ reckless_multiplier = 1.3

    # Calculating
    if len(fight_previous_moves) >= 4 and fight_previous_moves[-4][name] == fight_previous_moves[-2][name]:
        if opponent.health / opponent.max_health <= 0.25:
            $ player.health -= round(player_move.damage * 0.9)
        elif 0.25 < opponent.health / opponent.max_health <= 0.5:
            $ player.health -= round(player_move.damage * 0.6)
        else:
            $ player.health -= round(player_move.damage * 0.3)

    # Stance Bonus
    $ stance_multiplier = 1.0
    
    # Body Hook Stamina Bonus
    if player.stance_bonus == BODY_HOOK.name:
        $ stance_multiplier = 1.2

    if player.stance_bonus == KICK.name and player.stamina == 6:
        $ stance_multiplier = 1.2

    $ damage = round(player_move.damage * primed_multiplier * reckless_multiplier * stance_multiplier)
    call move_attack(opponent, player_move, damage, ignore_guard=(player.stance_bonus==JAB.name))

    if opponent.health <= 0:
        jump expression fight_end_label

    # Set end stance
    if player_move.end_stance is not None:
        $ player.stance = player_move.end_stance

    if player.stamina > 0:
        call screen fight_player_turn(player, opponent)
    else:
        $ player.guard = player.stance.value
        $ player.stamina = player.max_stamina
        call fight_start_opponent_turn(player, opponent)


label fight_start_opponent_turn(player, opponent):
    scene black
    show text "Opponent's turn"
    pause 1.0
    show screen fight_opponent_turn

    # Overwhelmed
    if len(player.previous_moves) >= 4:
        if opponent.health / opponent.max_health <= 0.25:
            $ overwhelmed_multiplier = 1.9
        elif 0.25 < opponent.health / opponent.max_health <= 0.5:
            $ overwhelmed_multiplier = 1.6
        else:
            $ overwhelmed_multiplier = 1.3
    else:
        $ overwhelmed_multiplier = 1

    $ opponent.guard = round(opponent.stance.value * overwhelmed_multiplier)

    # Hook stance bonus
    if player.stance_bonus == HOOK.name:
        $ opponent.stance -= 2

    $ fight_previous_moves.append({player.name: player.previous_moves.copy()})
    $ player.reset_previous_moves()

    call fight_opponent_turn(player, opponent)


label fight_opponent_turn(player, opponent):
    $ renpy.set_return_stack([])
    $ fight_game_state = FightGameState.OPPONENT_ATTACK

    $ opponent_move = renpy.random.choice(opponent.base_attacks)
    $ player.add_previous_move(opponent_move)

    if opponent.stamina < opponent_move.stamina_cost:
        $ opponent.stamina = opponent.max_stamina
        call fight_start_player_turn(player, opponent)

    if opponent_move == END_TURN:
        $ opponent.stamina = opponent.max_stamina + min(opponent.stamina, 2)
        call fight_start_player_turn(player, opponent)

    elif opponent_move == TURTLE:
        $ opponent.guard = FightStance.DEFENSIVE.value

        # Stance Bonus
        if opponent.stance == FightStance.SOLID:
            $ opponent.guard += 10

        call fight_start_player_turn(player, opponent)

    $ accuracy_check = renpy.random.randint(0, 100)

    if hasattr(opponent_move, "images") and opponent_move.images is None:
        $ raise NotImplementedError("Opponent move is missing images.")

    $ opponent.stamina -= opponent_move.stamina_cost

    scene expression opponent_move.images["start_image"]
    pause 1.0

    # Opponent attacks
    # Reckless
    $ reckless_multiplier = 1.0

    if len(fight_previous_moves) >= 3 and fight_previous_moves[-1][name][-1] == "Turtle" and fight_previous_moves[-3][name][-1] == "Turtle":
        if opponent.health / opponent.max_health <= 0.25:
            $ reckless_multiplier = 1.45
        elif 0.25 < opponent.health / opponent.max_health <= 0.5:
            $ reckless_multiplier = 1.3
        else:
            $ reckless_multiplier = 1.15

    $ damage = round(opponent_move.damage * reckless_multiplier)

    call move_attack(player, opponent_move, damage)

    if player.health <= 0:
        jump expression fight_end_label

    # Set end stance
    if opponent_move.end_stance is not None:
        $ opponent.stance = opponent_move.end_stance

    call fight_opponent_turn(player, opponent)


label fight_v2:
    python:
        player = Player(name, FightStance.FORWARD)
        opponent = Opponent("Tom", FightStance.FORWARD)

        player.base_attacks.append(JAB.copy({
            "start_image": "fight_prototype/images/player_start_jab.webp",
            "hit_image": "fight_prototype/images/player_hit_jab.webp",
            "blocked_image": "fight_prototype/images/player_jab_dodged.webp"
        }))
        player.base_attacks.append(BODY_HOOK.copy({
            "start_image": "fight_prototype/images/player_start_hook.webp",
            "hit_image": "fight_prototype/images/player_hit_hook.webp",
            "blocked_image": "fight_prototype/images/player_hook_dodged.webp"
        }))
        player.base_attacks.append(HOOK.copy({
            "start_image": "fight_prototype/images/player_start_hook.webp",
            "hit_image": "fight_prototype/images/player_hit_hook.webp",
            "blocked_image": "fight_prototype/images/player_hook_dodged.webp"
        }))
        player.base_attacks.append(KICK.copy({
            "start_image": "images/v2/kick1start.webp",
            "hit_image": "images/v2/kick2pic.webp",
            "blocked_image":  "images/v2/kick1pic.webp"
        }))

        player.special_attack = HEADBUTT.copy({})

        player.turn_moves.append(TURTLE)
        player.turn_moves.append(END_TURN)


        # opponent.base_attacks.append(BODY_HOOK.copy(None))
        opponent.base_attacks.append(JAB.copy({
            "start_image": "fight_prototype/images/opponent_start_jab.webp",
            "hit_image": "fight_prototype/images/opponent_hit_jab.webp",
            "blocked_image": "fight_prototype/images/opponent_jab_dodged.webp"
        }))
        # opponent.base_attacks.append(HOOK.copy(None))
        opponent.base_attacks.append(KICK.copy({
            "start_image": "fight_prototype/images/opponent_start_kick.webp",
            "hit_image": "fight_prototype/images/opponent_hit_kick.webp",
            "blocked_image": "fight_prototype/images/opponent_kick_dodged.webp"
        }))

        opponent.stance_images = {
            FightStance.AGGRESSIVE: "images/v2/tomstancekick.webp",
            FightStance.FORWARD: "images/v2/tomstancehook.webp",
            FightStance.SOLID: "images/v2/tomstancejab.webp",
            FightStance.DEFENSIVE: "images/v2/tomstancejab.webp"
        }

        opponent.wins = 2

    show screen fight_debug(player, opponent)
    show screen health_bars(player, opponent)
    call fight_start_player_turn(player, opponent)
