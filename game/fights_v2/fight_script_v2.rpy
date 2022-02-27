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
        def __init__(self, stance, health=20, stamina=10, attack_multiplier=1):
            self.stance = stance
            self.stamina = stamina
            self.max_health = health
            self.attack_multiplier = attack_multiplier

            self.max_stamina = stamina
            self.guard = stance.value

            self._health = health

            self.wins = 0
            self.turn_moves = []
            self.base_attacks = []
            # self.attributes = []
            # self.passive_abilities = set()
            # self.special_abilities = set()
            # self.special_ability = None
            self.previous_attack = None
            
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
        def __init__(self, stance, health=20, stamina=10, attack_multiplier=1, stance_images=None):
            BasePlayer.__init__(self, stance, health, stamina, attack_multiplier)

            self.stance_images = stance_images

        @property
        def stance_image(self):
            return self.stance_images[self.stance]

    
    class Player(BasePlayer):
        pass


label hit_move(move, target):
    scene expression move.images["hit_image"]
    with vpunch

    if target.guard < move.damage:
        $ target.health -= (move.damage - target.guard)
        $ target.guard = 0

    else:
        $ target.guard -= move.damage

    show screen fight_popup("{} Hit".format(move.name))
    pause 1.0

    return


label blocked_move(move, target):
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

    call screen fight_player_turn(player, opponent)


label player_attack_turn(player_move, player, opponent):
    $ renpy.set_return_stack([])
    $ fight_game_state = FightGameState.PLAYER_ATTACK

    if player_move == END_TURN:
        $ player.stamina = player.max_stamina + min(player.stamina, 2)
        call fight_start_opponent_turn(player, opponent)

    elif player_move == TURTLE:
        $ player.guard = FightStance.DEFENSIVE.value

        # Stance Bonus
        if player.stance == FightStance.SOLID:
            $ player.guard += 2

        call fight_start_opponent_turn(player, opponent)

    if hasattr(player_move, "images") and player_move.images is None:
        $ raise NotImplementedError("Player move is missing images.")

    $ player.stamina -= player_move.stamina_cost

    scene expression player_move.images["start_image"]
    pause 1.0

    # Player hits attack
    if opponent.guard < player_move.damage:
        call hit_move(player_move, opponent)
    
    # Opponent blocks player attack
    else:
        call blocked_move(player_move, opponent)

    if opponent.health <= 0:
        jump expression fight_end_label

    # Set end stance
    if player_move.end_stance is not None:
        $ player.stance = player_move.end_stance

    if player.stamina > 0:
        call screen fight_player_turn(player, opponent)
    else:
        $ player.guard = player_move.end_stance.value
        $ player.stamina = player.max_stamina
        call fight_start_opponent_turn(player, opponent)


label fight_start_opponent_turn(player, opponent):
    scene black
    show text "Opponent's turn"
    pause 1.0
    show screen fight_opponent_turn

    call fight_opponent_turn(player, opponent)


label fight_opponent_turn(player, opponent):
    $ renpy.set_return_stack([])
    $ fight_game_state = FightGameState.OPPONENT_ATTACK

    $ opponent_move = renpy.random.choice(opponent.base_attacks)

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

    # Opponent hits attack
    if player.guard < opponent_move.damage:
        call hit_move(opponent_move, player)
    
    # Player blocks opponent attack
    else:
        call blocked_move(opponent_move, player)

    if player.health <= 0:
        jump expression fight_end_label

    # Set end stance
    if opponent_move.end_stance is not None:
        $ opponent.guard = opponent_move.end_stance.value

    call fight_opponent_turn(player, opponent)


label fight_v2:
    python:
        player = Player(FightStance.FORWARD)
        opponent = Opponent(FightStance.FORWARD)

        player.turn_moves.append(END_TURN)
        player.turn_moves.append(TURTLE)

        player.base_attacks.append(BODY_HOOK.copy({
            "start_image": "fight_prototype/images/player_start_hook.webp",
            "hit_image": "fight_prototype/images/player_hit_hook.webp",
            "blocked_image": "fight_prototype/images/player_hook_dodged.webp"
        }))
        player.base_attacks.append(JAB.copy({
            "start_image": "fight_prototype/images/player_start_jab.webp",
            "hit_image": "fight_prototype/images/player_hit_jab.webp",
            "blocked_image": "fight_prototype/images/player_jab_dodged.webp"
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
