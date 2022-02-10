define fight_full_guard_stamina_penalty = 2

default fight_reaction_time = 1
default fight_end_label = "fight_end"
default fight_game_state = FightGameState.ERROR

default player_fight_style = "Aggressive"


# Light Attacks
define JAB = Attack(AttackType.LIGHT, AttackType.JAB, 5, 2)
define HOOK = Attack(AttackType.HEAVY, AttackType.BODY_HOOK, 10, 4)
define PUNCH = Attack(AttackType.LIGHT, AttackType.OVERHAND_PUNCH, 5, 2)

# Heavy Attacks
define HOOK = Attack(AttackType.HEAVY, AttackType.HOOK, 10, 6)
define UPPERCUT = Attack(AttackType.HEAVY, AttackType.UPPERCUT, 10, 6)
define KICK = Attack(AttackType.HEAVY, AttackType.KICK, 10, 6)

# Defensive Moves
define BLOCK = Defence(DefensiveMove.BLOCK, 2)
define DODGE = Defence(DefensiveMove.DODGE, 3)
