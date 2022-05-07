# SCENE 6: MC vs Ryan (Wolves)
# Locations: Warehouse
# Characters:
# Time: Saturday Night

label v10_mc_vs_ryan_fight:
    play music "music/v10/Track Scene 6.mp3" fadein 2
    
    if False:
        scene v10mvr1 # FPP. Show imre and chris near ring, imre excited look, mouth open chris mouth closed
        with dissolve

        imre "Holy shit man, did you see that shit!? I was planning on doing that one-two thing Sebastian showed me but I guess the one was enough!"

        scene v10mvr1a # FPP. Same camera as v10mvr1, Show imre and chris near ring, imre excited look, mouth closed chris mouth closed
        with dissolve

        u "*Laughs* Yeah man, that was fucking sick!"

        scene v10mvr1
        with dissolve
        # -Imre starts dancing-
        imre "*Sings* I'm getting me some pussy after that! I'm getting me some pussy! I'm getting me some pussy!"

        scene v10mvr1b # FPP. Same camera as v10mvr1, Show imre and chris near ring, excited look, imre mouth closed Chris mouth open
        with dissolve

        ch "Imre did good out there, but don't let his win distract you."

    scene v10mvr2 # FPP. Show Jost leant against the edge of the ring, slight smile, mouth open
    with dissolve

    jo "*Loud whisper* Hey, I got some plans tonight. How much longer is..."

    scene v10mvr1b
    with dissolve

    ch "We're ready Josh! *Laughs*"

    scene v10mvr1
    with dissolve

    imre "Go take him apart!"

    scene v10mvr1a
    with dissolve

    u "You got it man."

    scene v10mvr3 # TPP. Show Josh in the ring, mc walking towards him from behind mc.
    with dissolve

    pause 0.5

    scene v10mvr4 # TPP. Show josh in the centre of the ring and ryan and MC in opposite corners, Josh mouth open, mc and ryan mouth closed
    with dissolve
    jo "Looks like our fighters are ready!"

    scene v10mvr5 # TPP. Show josh in the centre of the ring and ryan next to josh either side, Josh mouth closed, mc mouth closed, ryan mouth open
    with dissolve

    ry "You ready to do this?"

    # TODO: Update ryan fight
    menu:
        "Fight Ryan":
            $ v10_ryan_fight = True
            scene v10mvr6a # FPP. Show Ryan infront of camera in ring, mouth open, hands raised ready to fight.
            with dissolve
            u "Question is, are you ready?"

            jo "Same rules as before, just get it guys!"

            # Ryan Fight
            call screen confirm("Would you like to play the fighting tutorial?",
                yes_action=[SetVariable("fight_tutorial", True), Call("fight_tutorialLabel")],
                no_action=[SetVariable("fight_tutorial", False), Return()])

            scene v10mvr6a

            call screen fight_typeMenu

            if fight_type == "normal":
                $ simRyanFight = False
                $ ryanStance = renpy.random.choice([1, 2, 3, 4])
                $ ryanAttack = renpy.random.choice([1, 2, 3, 4])

                call screen fight_selectDifficulty

                call screen fight_keybindOptions

            elif fight_type == "simReal" or fight_type == "simWin":
                $ simRyanFight = True
                $ stance = 1

                $ ryanStance = renpy.random.choice([1, 2, 3, 4])
                $ ryanAttack = renpy.random.choice([1, 2, 3, 4])
                $ ryanSimulation = renpy.random.choice([1, 2, 3, 4, 5, 6])

            if fight_type == "simWin":
                $ youHealth = 100000
            else:
                $ youHealth = 3

            $ enemyhealth = 6
            $ youDamage = 0
            $ ryanDamage = 0

            # Ryan attacks MC
            label ryan_McAttack:
                $ stance = 2 # Defence

                show screen fight_overlay(stance="defend") # TODO: Update fight code

                # Ryan hook
                if ryanAttack == 1:

                    scene ryanhook
                    pause 0.6 # Trial Error

                    scene ryanhookend
                    $ ryanStance = renpy.random.choice([1, 2, 3, 4]) # Ryan next defensive stance
                    $ simyou = renpy.random.choice([1, 2, 3, 4, 5, 6]) # What attack you're gonna pick next

                    if simRyanFight:
                        if ryanSimulation in [1, 2, 3]: # simryan is ryan random attack
                            jump ryan_McKickHit # REMEMBER switch attacks!
                        else:
                            jump ryan_McKickBlock

                    else:
                        call screen ryanFight_MCDefend(attack="Hook")

                # Ryan jab
                if ryanAttack == 2:

                    scene ryanjab
                    $ renpy.pause(0.5)

                    scene ryanjabend
                    $ ryanStance = renpy.random.choice([1, 2, 3, 4])
                    $ simyou = renpy.random.choice([1, 2, 3, 4, 5, 6])

                    if simRyanFight:
                        if ryanSimulation in [1, 2, 3]:
                            jump ryan_McJabHit
                        else:
                            jump ryan_McJabBlock

                    else:
                        call screen ryanFight_MCDefend(attack="Jab")

                # Ryan body hook
                if ryanAttack == 3:

                    scene ryanbody
                    $ renpy.pause(0.7)

                    scene ryanbodyend
                    $ ryanStance = renpy.random.choice([1, 2, 3, 4])
                    $ simyou = renpy.random.choice([1, 2, 3, 4, 5, 6])

                    if simRyanFight:
                        if ryanSimulation in [1, 2, 3]:
                            jump ryan_McHookHit
                        else:
                            jump ryan_McHookBlock

                    else:
                        call screen ryanFight_MCDefend(attack="BodyHook")

                # Ryan kick
                if ryanAttack == 4:

                    scene ryankick
                    $ renpy.pause(0.6)

                    scene ryankickend
                    $ ryanStance = renpy.random.choice([1, 2, 3, 4])
                    $ simyou = renpy.random.choice([1, 2, 3, 4, 5, 6])

                    if simRyanFight:
                        if ryanSimulation in [1, 2, 3]:
                            jump ryan_McBodyhookHit
                        else:
                            jump ryan_McBodyhookBlock

                    else:
                        call screen ryanFight_MCDefend(attack="Kick")


            # label Attacker_TargetAction
            label mc_ryanKickHit: # MC Kicks Ryan (Hits/No Block)
                $ ryanDamage += 1

                scene mc_ryan_Kick_hit
                pause 1 # Trial/Error
                
                if ryanDamage >= enemyhealth:
                    jump mc_ryanFightEnd
                jump ryan_McAttack

            label mc_ryanKickBlock: # MC Kicks Ryan (Blocks)
                scene mc_ryan_Kick_block
                pause 0.7 # Trial/Error

                jump ryan_McAttack


            label mc_ryanJabsHit: # MC Jabs Ryan (Hits/No Block)
                $ ryanDamage += 1

                scene mc_ryan_Jab_hit
                pause 1 # Trial/Error

                if ryanDamage >= enemyhealth:
                    jump mc_ryanFightEnd
                jump ryan_McAttack

            label mc_ryanJabsBlock: # MC Jabs Ryan (Blocks)
                scene mc_ryan_Jab_block
                pause 1 # Trial/Error

                jump ryan_McAttack

            label mc_ryanHooksHit: # MC Hooks Ryan (Hits/No Block)
                $ ryanDamage += 1

                scene mc_ryan_Hook_hit
                pause 1 # Trial/Error

                if ryanDamage >= enemyhealth:
                    jump mc_ryanFightEnd
                jump ryan_McAttack

            label mc_ryanHooksBlock: # MC Hooks Ryan (Blocks)
                scene mc_ryan_Hook_block
                pause 1 # Trial/Error

                jump ryan_McAttack

            label mc_ryanBodyhookHit: # MC Body Hooks Ryan (Hits/No Block)
                $ ryanDamage += 1

                scene mc_ryan_BodyJab_hit
                pause 1 # Trial/Error

                if ryanDamage >= enemyhealth:
                    jump mc_ryanFightEnd
                jump ryan_McAttack

            label mc_ryanBodyhookBlock: # MC Body Hooks Ryan (Blocks)
                scene mc_ryan_BodyJab_block
                pause 1 # Trial/Error

                jump ryan_McAttack


            label ryan_McKickHit: # Ryan Kicks MC (Hits/No Block)

                play sound "sounds/ks.mp3"
                $ youDamage += 1
                scene Ryan_Kick_hit
                with hpunch

                pause 0.5
                $ stance = 1
                $ ryanAttack = renpy.random.choice([1, 2, 3, 4])
                $ ryanSimulation = renpy.random.choice([1, 2, 3, 4, 5, 6])
                jump mc_ryanAttack

            label ryan_McKickBlock: # Ryan Kicks MC (Blocked)

                play sound "sounds/ks.mp3"
                scene Ryan_Kick_block
                with hpunch

                pause 0.5
                $ stance = 1
                $ ryanAttack = renpy.random.choice([1, 2, 3, 4])
                $ ryanSimulation = renpy.random.choice([1, 2, 3, 4])
                jump mc_ryanAttack

            label ryan_McJabHit: # Ryan Kicks MC (Hits/No Block)

                play sound "sounds/js.mp3"
                $ youDamage += 1
                scene Ryan_Jab_hit
                with hpunch

                pause 0.5
                $ stance = 1
                $ ryanAttack = renpy.random.choice([1, 2, 3, 4])
                $ ryanSimulation = renpy.random.choice([1, 2, 3, 4])
                if youDamage >= youHealth:
                        jump ryan_McFightEnd
                jump mc_ryanAttack

            label ryan_McJabBlock: # Ryan Kicks MC (Hits/No Block)

                play sound "sounds/bs.mp3"
                scene Ryan_Hook_block
                with hpunch

                pause 0.5
                $ stance = 1
                $ ryanAttack = renpy.random.choice([1, 2, 3, 4])
                $ ryanSimulation = renpy.random.choice([1, 2, 3, 4])
                jump mc_ryanAttack

            label ryan_McHookHit: # Ryan Kicks MC (Hits/No Block)

                play sound "sounds/hs.mp3"
                $ youDamage += 1
                scene Ryan_Hook_hit
                with hpunch

                pause 0.5
                $ stance = 1
                $ ryanAttack = renpy.random.choice([1, 2, 3, 4])
                $ ryanSimulation = renpy.random.choice([1, 2, 3, 4])
                if youDamage >= youHealth:
                        jump ryan_McFightEnd
                jump mc_ryanAttack

            label ryan_McHookBlock: # Ryan Kicks MC (Hits/No Block)

                play sound "sounds/bs.mp3"
                scene Ryan_Hook_block
                with hpunch

                pause 0.5
                $ stance = 1
                $ ryanAttack = renpy.random.choice([1, 2, 3, 4])
                $ ryanSimulation = renpy.random.choice([1, 2, 3, 4])
                jump mc_ryanAttack

            label ryan_McBodyhookHit: # Ryan Kicks MC (Hits/No Block)

                play sound "sounds/hs.mp3"
                $ youDamage += 1
                scene Ryan_BodyJab_hit
                with hpunch

                pause 0.5
                $ stance = 1
                $ ryanAttack = renpy.random.choice([1, 2, 3, 4])
                $ ryanSimulation = renpy.random.choice([1, 2, 3, 4])
                jump mc_ryanAttack

            label ryan_McBodyhookBlock: # Ryan Kicks MC (Hits/No Block)

                play sound "sounds/bs.mp3"
                scene Ryan_BodyJab_block
                with hpunch

                pause 0.5
                $ stance = 1
                $ ryanAttack = renpy.random.choice([1, 2, 3, 4])
                $ ryanSimulation = renpy.random.choice([1, 2, 3, 4])
                jump mc_ryanAttack


            label mc_ryanAttack:
                if simRyanFight:
                    if ryanStance == 1: # Jab Weakness
                        if simyou == 1:
                            jump mc_ryanBodyhookBlock
                        if simyou == 2:
                            jump mc_ryanHooksBlock
                        if simyou == 3:
                            jump mc_ryanKickBlock
                        if simyou == 4 or simyou == 5 or simyou == 6:
                            jump mc_ryanJabsHit
                    if ryanStance == 2: # Hook Weakness
                        if simyou == 1:
                            jump mc_ryanHooksBlock
                        if simyou == 2:
                            jump mc_ryanJabsBlock
                        if simyou == 3:
                            jump mc_ryanKickBlock
                        if simyou == 4 or simyou == 5 or simyou == 6:
                            jump mc_ryanBodyhookHit
                    if ryanStance == 3: # Body Hook Weakness
                        if simyou == 1:
                            jump mc_ryanJabsBlock
                        if simyou == 2:
                            jump mc_ryanHooksBlock
                        if simyou == 3:
                            jump mc_ryanKickBlock
                        if simyou == 4 or simyou == 5 or simyou == 6:
                            jump mc_ryanBodyhookBlock
                    if ryanStance == 4: # Kick Weakness
                        if simyou == 1:
                            jump mc_ryanBodyhookBlock
                        if simyou == 2:
                            jump mc_ryanHooksBlock
                        if simyou == 3:
                            jump mc_ryanJabsBlock
                        if simyou == 4 or simyou == 5 or simyou == 6:
                            jump mc_ryanKickHit
                else:
                    call screen ryanFight_MCAttack


            label mc_ryanFightEnd: # MC wins fight against Ryan
                $ v10_ryan_win = True

                jump ryan_fightEnd

            label ryan_McFightEnd: # MC loses fight against Ryan
                $ v10_ryan_win = False
                jump ryan_fightEnd

            label ryan_fightEnd:
                hide screen ryanFight_MCAttack
                hide screen ryanFight_MCDefend
                hide screen fight_overlay # TODO: Update fight code
                $ youDamage = 0
                $ stance = 0
                stop music fadeout 3
            jump v10_fight_result

        "Don't fight":
            scene v10mvr6a
            with dissolve

            $ grant_achievement("fright_club")
            
            u "I don't think I can do this. Sorry guys."

            scene v10mvr7 # FPP. Show Close up from ring of Chris and imre stood watching, Imre mouth open, chris mouth closed
            with dissolve
            imre "Dude, you better not quit right now!"

            scene v10mvr7a # FPP. Show Close up from ring of Chris and imre stood watching, Imre mouth closed, chris mouth open
            with dissolve

            ch "Come on, man. You got this!"

            scene v10mvr6  #Ryan mouth open
            with dissolve

            ry "Man, what are you doing?! We have to do this."

            scene v10mvr6a
            with dissolve

            u "I can't, I just can't."
            
            stop music fadeout 3
            
            jump v10_avoid_fight