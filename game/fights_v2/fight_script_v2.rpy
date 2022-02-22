init python:
    class FightStance(SmartEnum):
        AGGRESSIVE = 5
        FORWARD = 10
        SOLID = 15
        DEFENSIVE = 20


    class BasePlayer:
        def __init__(self, guard, stamina=10, health=100, attack_multiplier=1):
            self.guard = guard
            self.max_stamina = stamina
            self.max_health = health
            self.attack_multiplier = attack_multiplier
            
            self._stamina = stamina
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
        def stance(self):
            stance = FightStance.AGGRESSIVE
            
            for s in FightStance:
                if s.value > self.guard:
                    return stance

                stance = s  

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
        def __init__(self, stance, stamina=10, health=100, attack_multiplier=1, stance_images=None):
            BasePlayer.__init__(self, stance, stamina, health, attack_multiplier)

            self.stance_images = stance_images

        @property
        def stance_image(self):
            return self.stance_images[self.stance]

    
    class Player(BasePlayer):
        pass


    def get_accuracy(move, target):
        if hasattr(move, "accuracy") and move.accuracy is not None:
            return move.accuracy + FightMove.ACCURACY_DICT[target.stance]
        else:
            return None


    def get_total_damage(move, attacker):
        if hasattr(move, "damage") and move.damage is not None:
            return move.damage + FightMove.DAMAGE_DICT[attacker.stance]
        else:
            return None


label hit_move(move, total_damage, target):
    scene expression move.images["hit_image"]
    with vpunch

    $ target.health -= total_damage

    show screen fight_popup("{} Hit".format(move.name))
    pause 1.0

    return


label missed_move(move):
    scene expression move.images["miss_image"]
    with vpunch

    show screen fight_popup("{} Miss".format(move.name))
    pause 1.0

    return


label player_attack_turn(player_move, player, opponent):
    $ renpy.set_return_stack([])
    $ fight_game_state = FightGameState.PLAYER_ATTACK

    if player_move == END_TURN:
        $ player.stamina = min(player.max_stamina + 3, player.stamina + 3)
        call fight_opponent_turn(player, opponent)

    elif player_move == TURTLE:
        $ player.guard = FightStance.DEFENSIVE.value

        # Stance Bonus
        if player.stance == FightStance.SOLID:
            $ player.guard += 10

        call fight_opponent_turn(player, opponent)

    $ accuracy_check = renpy.random.randint(0, 100)

    if hasattr(player_move, "images") and player_move.images is None:
        $ raise NotImplementedError("Player move is missing images.")

    $ player.stamina -= player_move.stamina_cost

    scene expression player_move.images["start_image"]
    pause 0.5

    # Player misses
    if get_accuracy(player_move, opponent) < accuracy_check:
        call missed_move(player_move)
    
    # Player hits attack
    else:
        call hit_move(player_move, get_total_damage(player_move, player), opponent)

    if opponent.health <= 0:
        jump expression fight_end_label

    # Set end stance
    if player_move.end_stance is not None:
        $ player.guard = player_move.end_stance.value

    if player.stamina > 0:
        call screen fight_player_turn(player, opponent)
    else:
        call fight_opponent_turn(player, opponent)


label fight_opponent_turn(player, opponent):
    $ renpy.set_return_stack([])
    $ fight_game_state = FightGameState.OPPONENT_ATTACK

    $ opponent_move = renpy.random.choice(opponent.base_attacks)

    if opponent.stamina < opponent_move.stamina_cost:
        call screen fight_player_turn(player, opponent)

    if opponent_move == END_TURN:
        $ opponent.stamina = min(opponent.max_stamina + 3, opponent.stamina + 3)
        call screen fight_player_turn(player, opponent)

    elif player_move == TURTLE:
        $ opponent.guard = FightStance.DEFENSIVE.value

        # Stance Bonus
        if opponent.stance == FightStance.SOLID:
            $ opponent.guard += 10

        call screen fight_player_turn(player, opponent)

    $ accuracy_check = renpy.random.randint(0, 100)

    if hasattr(opponent_move, "images") and opponent_move.images is None:
        $ raise NotImplementedError("Opponent move is missing images.")

    $ opponent.stamina -= opponent_move.stamina_cost

    scene expression opponent_move.images["start_image"]
    pause 0.5

    # Opponent misses
    if get_accuracy(opponent_move, player) < accuracy_check:
        call missed_move(opponent_move)
    
    # Opponent hits attack
    else:
        call hit_move(opponent_move, get_total_damage(opponent_move, opponent), player)

    if player.health <= 0:
        jump expression fight_end_label

    # Set end stance
    if opponent_move.end_stance is not None:
        $ opponent.guard = opponent_move.end_stance.value

    call fight_opponent_turn(player, opponent)


label fight_v2:
    python:
        player = Player(FightStance.FORWARD.value)
        opponent = Opponent(FightStance.FORWARD.value)

        player.turn_moves.append(END_TURN)
        player.turn_moves.append(TURTLE)

        # player.base_attacks.append(BODY_HOOK.copy(None))
        player.base_attacks.append(JAB.copy({
            "start_image": "fight_prototype/images/player_start_jab.webp",
            "hit_image": "fight_prototype/images/player_hit_jab.webp",
            "miss_image": "fight_prototype/images/player_jab_dodged.webp"
        }))
        player.base_attacks.append(HOOK.copy({
            "start_image": "fight_prototype/images/player_start_hook.webp",
            "hit_image": "fight_prototype/images/player_hit_hook.webp",
            "miss_image": "fight_prototype/images/player_hook_dodged.webp"
        }))
        # player.base_attacks.append(KICK.copy(None))

        # opponent.base_attacks.append(BODY_HOOK.copy(None))
        opponent.base_attacks.append(JAB.copy({
            "start_image": "fight_prototype/images/opponent_start_jab.webp",
            "hit_image": "fight_prototype/images/opponent_hit_jab.webp",
            "miss_image": "fight_prototype/images/opponent_jab_dodged.webp"
        }))
        # opponent.base_attacks.append(HOOK.copy(None))
        opponent.base_attacks.append(KICK.copy({
            "start_image": "fight_prototype/images/opponent_start_kick.webp",
            "hit_image": "fight_prototype/images/opponent_hit_kick.webp",
            "miss_image": "fight_prototype/images/opponent_kick_dodged.webp"
        }))

        opponent.stance_images = {
            FightStance.AGGRESSIVE: "images/v2/tomstancekick.webp",
            FightStance.FORWARD: "images/v2/tomstancehook.webp",
            FightStance.SOLID: "images/v2/tomstancejab.webp",
            FightStance.DEFENSIVE: "images/v2/tomstancejab.webp"
        }

        opponent.wins = 2

    show screen fight_debug(player, opponent)
    call screen fight_player_turn(player, opponent)
