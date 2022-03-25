label fight_example:
    python:
        mc.fighter = Player(name, FightStance.FORWARD)

        # Player base attacks
        mc.fighter.base_attacks.append(BodyHook({
            "start_image": "",
            "hit_image": "",
            "blocked_image": ""
        }))
        mc.fighter.base_attacks.append(Jab({
            "start_image": "",
            "hit_image": "",
            "blocked_image": ""
        }))
        mc.fighter.base_attacks.append(Hook({
            "start_image": "",
            "hit_image": "",
            "blocked_image": ""
        }))
        mc.fighter.base_attacks.append(Kick({
            "start_image": "",
            "hit_image": "",
            "blocked_image": ""
        }))

        tom.fighter = Opponent("Tom", FightStance.AGGRESSIVE)

        tom.fighter.stance_images = {
            FightStance.AGGRESSIVE: "",
            FightStance.DEFENSIVE: "",
            FightStance.FORWARD: "",
            FightStance.SOLID: ""
        }

        tom.fighter.base_attacks.append(BodyHook({
            "start_image": "",
            "hit_image": "",
            "blocked_image": ""
        }))
        tom.fighter.base_attacks.append(Jab({
            "start_image": "",
            "hit_image": "",
            "blocked_image": ""
        }))
        tom.fighter.base_attacks.append(Hook({
            "start_image": "",
            "hit_image": "",
            "blocked_image": ""
        }))
        tom.fighter.base_attacks.append(Kick({
            "start_image": "",
            "hit_image": "",
            "blocked_image": ""
        }))
        
        tom.fighter.special_attack = Headbutt({
            "start_image": "",
            "hit_image": "",
            "blocked_image": ""
        })

        tom.fighter.quirk = seeing_red

        fight = Fight(mc, tom, "v1_start")

    call screen fight_overview(fight, "First Fight")