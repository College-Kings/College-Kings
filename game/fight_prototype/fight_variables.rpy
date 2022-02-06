default fight_reaction_time = 1
default fight_end_label = "fight_end"
default fight_game_state = FightGameState.ERROR

default player_fight_style = "Aggressive"


# Player Light Attacks
define PLAYER_JAB = Attack(AttackType.LIGHT, AttackType.JAB, 5, 2, Guard.SEMI_GUARD, {
    "start_image": "images/v2/jab2start.webp",
    "hit_image": "images/v2/jab2pic.webp",
    "block_image": "images/v2/jab1pic.webp"
})
define PLAYER_BODY_HOOK = Attack(AttackType.HEAVY, AttackType.BODY_HOOK, 10, 4, Guard.FULL_GUARD, {
    "start_image": "images/v2/hook2start.webp",
    "hit_image": "images/v2/hook2pic.webp",
    "block_image": "images/v2/hook1pic.webp"
})
define PLAYER_OVERHAND_PUNCH = Attack(AttackType.LIGHT, AttackType.OVERHAND_PUNCH, 5, 2, Guard.SEMI_GUARD, {
    "start_image": "images/v2/jab2start.webp",
    "hit_image": "images/v2/jab2pic.webp",
    "block_image": "images/v2/jab1pic.webp"
})

# Player Heavy Attacks
define PLAYER_HOOK = Attack(AttackType.HEAVY, AttackType.HOOK, 5, 2, Guard.FULL_GUARD, {
    "start_image": "images/v2/jab2start.webp",
    "hit_image": "images/v2/jab2pic.webp",
    "block_image": "images/v2/jab1pic.webp"
})
define PLAYER_UPPERCUT = Attack(AttackType.HEAVY, AttackType.UPPERCUT, 5, 2, Guard.FULL_GUARD, {
    "start_image": "images/v2/jab2start.webp",
    "hit_image": "images/v2/jab2pic.webp",
    "block_image": "images/v2/jab1pic.webp"
})
define PLAYER_KICK = Attack(AttackType.HEAVY, AttackType.KICK, 5, 2, Guard.FULL_GUARD, {
    "start_image": "images/v2/jab2start.webp",
    "hit_image": "images/v2/jab2pic.webp",
    "block_image": "images/v2/jab1pic.webp"
})

# Guards
define SEMI_GUARD = Defence(Guard.SEMI_GUARD, 2)
define FULL_GUARD = Defence(Guard.FULL_GUARD, 5)

# Opponent Light Attacks
define OPPONENT_JAB = Attack(AttackType.LIGHT, AttackType.JAB, 5, 2, Guard.SEMI_GUARD, {
    "start_image": "images/v2/tomjab.webp",
    "hit_image": "images/v2/tomjabhit.webp",
    "block_image": "images/v2/tomjabblock.webp"
})

# Opponent Heavy Attacks
define OPPONENT_KICK = Attack(AttackType.HEAVY, AttackType.KICK, 10, 4, Guard.FULL_GUARD, {
    "start_image": "images/v2/tomkick.webp",
    "hit_image": "images/v2/tomkickhit.webp",
    "block_image": "images/v2/tomkickblock.webp"
})