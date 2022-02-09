label backup:
    # Player attack counter
    if opponent.guard == Guard.SEMI_GUARD and player_move.name != AttackType.UPPERCUT:
        $ counter_attack = renpy.random.choice(opponent.attacks)

        if opponent.stamina >= counter_attack.stamina_cost:
            call screen fight_defense(counter_attack)


    # Passive Abilities
    $ damage = player_move.damage

    # Passive Ability: Health
    if (SpecialPassives.BERSERK in player.passive_abilities) and (player.health <= player.max_health * 0.2):
        $ damage *= 1.5

    # Passive Ability: Stamina
    if (SpecialPassives.FULLY_CHARGED in player.passive_abilities) and (player.stamina >= player.max_stamina * 0.75):
        $ damage *= 1.25

    # Passive Ability: Light Attack Damage
    if (SpecialPassives.COMBO in player.passive_abilities) and (player_move.type == AttackType.LIGHT and player.previous_attack == AttackType.LIGHT):
        $ damage *= 1.25

    # Special Effect: Hook
    if player_move.name == AttackType.HOOK:
        $ opponent.stamina = 0

    # Passive Ability: Heavy Attack Damage
    if SpecialPassives.BRUISER in player.passive_abilities:
        $ damage = int(damage * 1.25)

    # Special Effect: Kick
    if player_move.name == AttackType.KICK:
        $ damage = int(damage * 1.25)

    # Jab special effect
    if player_move.name == AttackType.JAB:
        $ opponent.guard = Guard.LOW_GUARD

    # Body hook special effect
    # if player_move.name == AttackType.BODY_HOOK:
    #     $ opponent.stamina -= 3 # No stamina gain

    $ player.previous_attack = player_move

    # or (player.previous_attack is not None and player.previous_attack.name == AttackType.OVERHAND_PUNCH):