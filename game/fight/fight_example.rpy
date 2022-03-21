label fight_example:
    python:
        player = Player(name, FightStance.FORWARD)
        opponent = Opponent("Tom", FightStance.AGGRESSIVE)

        # Player base attacks
        player.base_attacks.append(BodyHook({
            "start_image": "",
            "hit_image": "",
            "blocked_image": ""
        }))
        player.base_attacks.append(Jab({
            "start_image": "",
            "hit_image": "",
            "blocked_image": ""
        }))
        player.base_attacks.append(Hook({
            "start_image": "",
            "hit_image": "",
            "blocked_image": ""
        }))
        player.base_attacks.append(Kick({
            "start_image": "",
            "hit_image": "",
            "blocked_image": ""
        }))

        # Player special attacks
        player.special_attack = Headbutt({
            "start_image": "",
            "hit_image": "",
            "blocked_image": ""
        })

        opponent.stance_images = {
            FightStance.AGGRESSIVE: "",
            FightStance.DEFENSIVE: "",
            FightStance.FORWARD: "",
            FightStance.SOLID: ""
        }

        opponent.base_attacks.append(BodyHook({
            "start_image": "",
            "hit_image": "",
            "blocked_image": ""
        }))
        opponent.base_attacks.append(Jab({
            "start_image": "",
            "hit_image": "",
            "blocked_image": ""
        }))
        opponent.base_attacks.append(Hook({
            "start_image": "",
            "hit_image": "",
            "blocked_image": ""
        }))
        opponent.base_attacks.append(Kick({
            "start_image": "",
            "hit_image": "",
            "blocked_image": ""
        }))
        
        opponent.special_attack = Headbutt({
            "start_image": "",
            "hit_image": "",
            "blocked_image": ""
        })