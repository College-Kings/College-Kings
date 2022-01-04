# Drug Deal With Josh
# Location: Urban Alley
# Outfits: MC Outfit 2, Josh Outfit 1, Lars Outfit 1, Joe Outfit 1
# Time: Monday Evening bordering on Night
# Please save each scene as some scenes continue from previous scenes as I had to move things around. This is my bad - I have noted when you need to go back in render descriptions.
# It's probably best to look at the rpy file to get a better understand of the timeline of the renders.

label drug_deal_w_josh:
    stop music fadeout 3
    scene v8sdd1 # TPP. Show a long shot of the alley, Josh and MC, next to eachother walking down the alley cautiosly. Camera from behind Josh and MC.
    with fade

    pause 0.5

    scene v8sdd2 # FPP. Show Josh turning his head to his side to look at MC (Camera). Josh slightly concerned expression, mouth open.
    with dissolve

    jo "(Quietly) Looks like we're a little early. Keep your eyes open and don't say anything, okay?"

    scene v8sdd2a # FPP. Same camera as v8sdd2, Josh looking forward again, concerned expression, mouth closed.
    with dissolve

    u "(Quietly) Fuck, it stinks here."

    scene v8sdd2
    with dissolve

    jo "(Quietly) Yeah. You ready for this?"

    scene v8sdd2a
    with dissolve

    u "(Quietly) Yeah, okay. What do I do if..."

    scene v8sdd3 # TPP. Show Joe and Lars approaching MC and Josh from the door to their left (sabBuilding01Door), walking to their final position which should be infront of sabBuilding02. Josh and MC turn to look at them, Joe and Lars with thuggish/hard expressions, MC slight concerned expression, Josh neutral expression. Joe carrying metal pipe.
    with dissolve

    pause 0.5

    scene v8sdd4 # FPP. Show Joe and Lars stood next to eachother opposite Josh and MC, Joe holding pipe across him infront of his stomach in both hands, both menacing expressions, Joe mouth open.
    with dissolve

    je "'Sup."

    scene v8sdd5 # TPP. Show Josh nodding his head slightly, Josh mouth open. Everyone else mouth closed.
    with dissolve

    jo "'Sup."

    scene v8sdd4a # FPP. Same camera as v8sdd4, show Lars looking around menacingly, Joe looking at camera, Joe mouth open.
    with dissolve

    je "You got the shit?"

    scene v8sdd5a # FPP. Same camera as v8sdd5, Josh looking at Joe and Lars with a slight stern expression, Josh mouth open, everyone else mouth closed.
    with dissolve

    jo "Yeah. You got the cash?"

    scene v8sdd4a
    with dissolve

    je "Yeah. Let me see the stuff."

    scene v8sdd5a
    with dissolve

    jo "Let me see the cash."

    scene v8sdd4b # FPP. Same camera as v8sdd4, Joe looking down slightly with a chuckle, Lars menacing smile, mouths closed.
    with dissolve

    pause 0.5

    play music "music/m3punk.mp3"

    scene v8sdd4c # FPP. Same camera as v8sdd4, Joe and Lars looking at the camera, angry expression, Joe now holding the pipe in one hand only. Joe mouth open.
    with dissolve

    je "See, this is where you're under the wrong impression you're in control of this situation. My buddy here, Lars, has a quick temper and fists like rock. Pretty sure I don't gotta spell shit out for ya, do I?"

    scene v8sdd5b # TPP. Same camera as v8sdd5, Josh looking nervous but trying to hide it, Joe and Lars angry expression, MC looking nervous, everyone else mouth closed, Josh mouth open,
    with dissolve

    jo "Spell out what? You've got the cash, I've got the shit, what's the problem?"

    scene v8sdd4c
    with dissolve

    je "Well gee, looks like you aren't too bright. Lars, enlighten the man, will ya?"

    scene v8sdd6 # FPP. Show Lars stepping towards the camera, Lars menacing grin, fist in hand.
    with dissolve

    pause 0.5

    scene v8sdd6a # FPP.Same camera as v8sdd6, Joe and Lars are now stood close to camera (Josh & MC), Joe menacing smile, Lars looking slightly angry, Joe mouth open.
    with dissolve

    je "If I were you, I'd just hand over the shit now before you end up with a nice, shiny dent in your skull. Save Lars the effort. You dig?"

    menu:
        "Intervene":
            $ add_point(KCT.BRO)
            jump int_deal_w_josh
        "Don't intervene":
            jump no_int_deal_w_josh

label int_deal_w_josh:
    scene v8sdd7 # TPP. Show Josh taking out the cocaine from his pocket about to hand it to Lars, Lars has his hand out waiting in anticipation, Joe and Lars menacing smile, Josh nervous.
    with dissolve

    pause 0.5

    scene v8sdd8 # TPP. Show MC stepping between Lars and Josh, MC slight angry expression, Lars & Joe angry, Josh shocked, MC mouth open.
    with dissolve

    u "Hey, back off."

    scene v8sdd9 # FPP. Show Joe and Lars both looking at camera, Joe chuckling, Lars angry, Joe mouth open.
    with dissolve

    je "Well, lookie here, a real hero. Lars, show him what happens to heroes."

    scene v8sdd10 # TPP. Show Joe running at Josh with the Pipe looking angry, Lars readying for a fight with MC.
    with dissolve

    # Lars Fight
    call screen confirm("Would you like to play the fighting tutorial?",
        yes_action=[SetVariable("fight_tutorial", True), Call("fight_tutorialLabel")],
        no_action=[SetVariable("fight_tutorial", False), Return()])
        
    scene v8sdd10

    call screen fight_typeMenu

    if fight_type == "normal":
        $ simLarsFight = False

        call screen fight_selectDifficulty

        call screen fight_keybindOptions
    
    elif fight_type == "simReal" or fight_type == "simWin":
        $ simLarsFight = True
        
    $ stance = 1
    $ larsStance = renpy.random.choice([1, 2, 3, 4])
    $ larsAttack = renpy.random.choice([1, 2, 3, 4])
    $ larsSimulation = renpy.random.choice([1, 2, 3, 4, 5, 6])
    $ simyou = renpy.random.choice([1, 2, 3, 4, 5, 6])

    if fight_type == "simWin":
        $ youHealth = 100000
    else:
        $ youHealth = 3

    $ enemyhealth = 6
    $ youDamage = 0
    $ larsdmg = 0

# Lars attacks MC
label lars_McAttack:
    $ stance = 2

    show screen fight_overlay(stance="defend")
    
    # Lars hook
    if larsAttack == 1:

        scene larshook
        pause 0.6 # Trial Error

        scene larshookend
        $ larsStance = renpy.random.choice([1, 2, 3, 4]) # Lars next defensive stance
        $ simyou = renpy.random.choice([1, 2, 3, 4, 5, 6]) # What attack you're gonna pick next

        if simLarsFight:
            if larsSimulation in [1, 2, 3]: # simlars is lars random attack
                jump lars_McKickHit # REMEMBER switch attacks!
            else:
                jump lars_McKickBlock

        else:
            call screen larsFight_MCDefend(attack="Hook")

    # Lars jab
    if larsAttack == 2:

        scene larsjab
        $ renpy.pause(0.5)

        scene larsjabend
        $ larsStance = renpy.random.choice([1, 2, 3, 4])
        $ simyou = renpy.random.choice([1, 2, 3, 4, 5, 6])

        if simLarsFight:
            if larsSimulation in [1, 2, 3]:
                jump lars_McJabHit
            else:
                jump lars_McJabBlock

        else:
            call screen larsFight_MCDefend(attack="Jab")

    # Lars body hook
    if larsAttack == 3:

        scene larsbody
        $ renpy.pause(0.7)

        scene larsbodyend
        $ larsStance = renpy.random.choice([1, 2, 3, 4])
        $ simyou = renpy.random.choice([1, 2, 3, 4, 5, 6])

        if simLarsFight:
            if larsSimulation in [1, 2, 3]:
                jump lars_McHookHit
            else:
                jump lars_McHookBlock

        else:
            call screen larsFight_MCDefend(attack="BodyHook")

    # Lars kick
    if larsAttack == 4:

        scene larskick
        $ renpy.pause(0.6)

        scene larskickend
        $ larsStance = renpy.random.choice([1, 2, 3, 4])
        $ simyou = renpy.random.choice([1, 2, 3, 4, 5, 6])

        if simLarsFight:
            if larsSimulation in [1, 2, 3]:
                jump lars_McBodyhookHit
            else:
                jump lars_McBodyhookBlock

        else:
            call screen larsFight_MCDefend(attack="Kick")


# label Attacker_TargetAction
label mc_LarsKickHit: # MC Kicks Lars (Hits/No Block)

    $ larsdmg += 1
    scene MC_Lars_Kick_hit 
    pause 1 # Trial/Error
    if larsdmg >= enemyhealth:
        jump mc_larsFightEnd
    jump lars_McAttack

label mc_LarsKickBlock: # MC Kicks Lars (Blocks)

        scene MC_Lars_Kick_block 
        pause 0.7 # Trial/Error
        jump lars_McAttack


label mc_LarsJabsHit: # MC Jabs Lars (Hits/No Block)

    $ larsdmg += 1
    scene MC_Lars_Jab_hit
    pause 0.7 # Trial/Error
    if larsdmg >= enemyhealth:
        jump mc_larsFightEnd
    jump lars_McAttack

label mc_LarsJabsBlock: # MC Jabs Lars (Blocks)

        scene MC_Lars_Jab_block
        pause 0.7 # Trial/Error
        jump lars_McAttack


label mc_LarsHooksHit: # MC Hooks Lars (Hits/No Block)

    $ larsdmg += 1
    scene MC_Lars_Hook_hit
    pause 0.7 # Trial/Error
    if larsdmg >= enemyhealth:
        jump mc_larsFightEnd
    jump lars_McAttack

label mc_LarsHooksBlock: # MC Hooks Lars (Blocks)

        scene MC_Lars_Hook_block 
        pause 0.7 # Trial/Error
        jump lars_McAttack


label mc_LarsBodyhookHit: # MC Body Hooks Lars (Hits/No Block)


    $ larsdmg += 1
    scene MC_Lars_BodyJab_hit
    pause 0.7 # Trial/Error
    if larsdmg >= enemyhealth:
        jump mc_larsFightEnd
    jump lars_McAttack

label mc_LarsBodyhookBlock: # MC Body Hooks Lars (Blocks)

        scene MC_Lars_BodyJab_block 
        pause 0.7 # Trial/Error
        jump lars_McAttack


label lars_McKickHit: # Lars Kicks MC (Hits/No Block)

    play sound "sounds/ks.mp3"
    $ youDamage += 1
    scene Lars_Kick_hit
    with hpunch

    pause 0.5
    $ stance = 1
    $ larsAttack = renpy.random.choice([1, 2, 3, 4])
    $ larsSimulation = renpy.random.choice([1, 2, 3, 4, 5, 6])
    jump mc_larsAttack

label lars_McKickBlock: # Lars Kicks MC (Blocked)

    play sound "sounds/ks.mp3"
    scene Lars_Kick_block
    with hpunch

    pause 0.5
    $ stance = 1
    $ larsAttack = renpy.random.choice([1, 2, 3, 4])
    $ larsSimulation = renpy.random.choice([1, 2, 3, 4])
    jump mc_larsAttack

label lars_McJabHit: # Lars Kicks MC (Hits/No Block)

    play sound "sounds/js.mp3"
    $ youDamage += 1
    scene Lars_Jab_hit
    with hpunch

    pause 0.5
    $ stance = 1
    $ larsAttack = renpy.random.choice([1, 2, 3, 4])
    $ larsSimulation = renpy.random.choice([1, 2, 3, 4])
    if youDamage >= youHealth:
            jump lars_McFightEnd
    jump mc_larsAttack

label lars_McJabBlock: # Lars Kicks MC (Hits/No Block)

    play sound "sounds/bs.mp3"
    scene Lars_Hook_block
    with hpunch

    pause 0.5
    $ stance = 1
    $ larsAttack = renpy.random.choice([1, 2, 3, 4])
    $ larsSimulation = renpy.random.choice([1, 2, 3, 4])
    jump mc_larsAttack

label lars_McHookHit: # Lars Kicks MC (Hits/No Block)

    play sound "sounds/hs.mp3"
    $ youDamage += 1
    scene Lars_Hook_hit
    with hpunch

    pause 0.5
    $ stance = 1
    $ larsAttack = renpy.random.choice([1, 2, 3, 4])
    $ larsSimulation = renpy.random.choice([1, 2, 3, 4])
    if youDamage >= youHealth:
            jump lars_McFightEnd
    jump mc_larsAttack

label lars_McHookBlock: # Lars Kicks MC (Hits/No Block)

    play sound "sounds/bs.mp3"
    scene Lars_Hook_block
    with hpunch

    pause 0.5
    $ stance = 1
    $ larsAttack = renpy.random.choice([1, 2, 3, 4])
    $ larsSimulation = renpy.random.choice([1, 2, 3, 4])
    jump mc_larsAttack

label lars_McBodyhookHit: # Lars Kicks MC (Hits/No Block)

    play sound "sounds/hs.mp3"
    $ youDamage += 1
    scene Lars_BodyJab_hit
    with hpunch

    pause 0.5
    $ stance = 1
    $ larsAttack = renpy.random.choice([1, 2, 3, 4])
    $ larsSimulation = renpy.random.choice([1, 2, 3, 4])
    jump mc_larsAttack

label lars_McBodyhookBlock: # Lars Kicks MC (Hits/No Block)

    play sound "sounds/bs.mp3"
    scene Lars_BodyJab_block
    with hpunch

    pause 0.5
    $ stance = 1
    $ larsAttack = renpy.random.choice([1, 2, 3, 4])
    $ larsSimulation = renpy.random.choice([1, 2, 3, 4])
    jump mc_larsAttack


label mc_larsAttack:
    if simLarsFight:
        if larsStance == 1: # Jab Weakness
            if simyou == 1:
                jump mc_LarsBodyhookBlock
            if simyou == 2:
                jump mc_LarsHooksBlock
            if simyou == 3:
                jump mc_LarsKickBlock
            if simyou == 4 or simyou == 5 or simyou == 6:
                jump mc_LarsJabsHit
        if larsStance == 2: # Hook Weakness
            if simyou == 1:
                jump mc_LarsHooksBlock
            if simyou == 2:
                jump mc_LarsJabsBlock
            if simyou == 3:
                jump mc_LarsKickBlock
            if simyou == 4 or simyou == 5 or simyou == 6:
                jump mc_LarsBodyhookHit
        if larsStance == 3: # Body Hook Weakness
            if simyou == 1:
                jump mc_LarsJabsBlock
            if simyou == 2:
                jump mc_LarsHooksBlock
            if simyou == 3:
                jump mc_LarsKickBlock
            if simyou == 4 or simyou == 5 or simyou == 6:
                jump mc_LarsBodyhookBlock
        if larsStance == 4: # Kick Weakness
            if simyou == 1:
                jump mc_LarsBodyhookBlock
            if simyou == 2:
                jump mc_LarsHooksBlock
            if simyou == 3:
                jump mc_LarsJabsBlock
            if simyou == 4 or simyou == 5 or simyou == 6:
                jump mc_LarsKickHit
    else:
        call screen larsFight_MCAttack


label mc_larsFightEnd: # MC wins fight against Lars
    hide screen s28_larsMcAttack
    hide screen s28_mcLarsAttack
    hide screen fight_overlay
    $ youDamage = 0
    $ stance = 0
    $ s28_fightWinner = "MC"

    jump beat_lars

label lars_McFightEnd: # MC loses fight against Lars
    hide screen s28_larsMcAttack
    hide screen s28_mcLarsAttack
    hide screen fight_overlay
    $ youDamage = 0
    $ stance = 0
    $ s28_fightWinner = "Lars"
    
    jump beat_by_lars

label beat_lars:
    scene v8sdd11 # TPP. Show Josh and Joe fighting, Joe is swinging the pipe he has to hit Josh over the head, Josh looking concerned, Joe looking angry.
    with dissolve

    pause 0.5

    scene v8sdd11a # TPP. Same camera as v8sdd11, Joe now hits Josh on the head with the pipe, Josh wincing in pain, Joe angry.
    with vpunch

    pause 0.5

    scene v8sdd11b # TPP. Same camera as v8sdd11, Josh is now on the ground dazed, Joe turns around to face MC looking angry.
    with dissolve

    u "(Oh shit)"

    scene v8sdd12 # FPP. Show Joe charging at MC about to swing the pipe over MC's head, Joe looking angry.
    with dissolve

    menu (fail_label="hit_with_pipe"):
        "Duck":
            jump dodged_pipe
        "...":
            jump hit_with_pipe

label no_int_deal_w_josh:
    scene v8sdd24 # TPP. !RETURN CHARACTERS TO SAME POSITIONS AS v8sdd6a! Show Josh looking at Joe and Lars, angry expression, mouth open.
    with dissolve

    jo "No. Fuck you! I'm not giving you shit! You want it, you pay me."

    scene v8sdd25 # FPP. Show Joe and Lars staring at Josh, Joe chuckling sardonically, Joe looking angry. Joe mouth open.
    with dissolve

    je "No, no, no... fuck YOU."

    scene v8sdd26 # FPP. Show Joe stepping forward and jabbing Josh in the stomach with the pipe he's holding. Josh winces in pain.
    with dissolve

    pause 0.5

    scene v8sdd27 # FPP. Show Joe swinging the pipe and hitting Josh over the head with it, Josh begins to fall to the ground.
    with dissolve

    pause 0.5

    scene v8sdd28 # FPP. Joe and Lars both turn and look at camera (MC). Joe pointing at camera, annoyed expression, Lars slightly annoyed expression, Joe mouth open.
    with dissolve

    je "You call the cops, I'll find you and pull your tongue down and tie it to your dick, got it?"

    scene v8sdd29 # FPP. Show either Joe or Lars picking up the drugs the other is walking away. Josh on the ground in pain. Josh looking injured and bruised.
    with dissolve

    pause 0.5

    jump check_on_josh

label dodged_pipe:
    $ v8_dodged_pipe = True
    scene v8sdd13 # TPP. Show MC ducking as Joe swings the pipe over his head, Lars stood directly behind MC.
    with dissolve

    pause 0.5

    scene v8sdd13a # TPP. Same camera as v8sdd13, Joe now hits Lars on the head with the pipe, Lars winces with pain and begins to fall to the ground.
    with vpunch

    $ renpy.end_replay()

    pause 0.5

    scene v8sdd14 # TPP. Show MC looking up at Joe who is in shock, MC starts to stand up in preparation to plant a huge uppercut on Joe's chin. Lars on the ground. MC focused expression, MC mouth open.
    with dissolve

    $ grant_achievement("ip_man")

    u "Fuck you!"

    scene v8sdd15 # TPP. Show MC uppercuting Joe, camera from the side, MC looks focused, Joe winces in pain as he takes the uppercut square to the chin.
    with vpunch

    pause 0.5

    scene v8sdd16 # FPP. Show Joe knocked out on the ground, Camera looking down on Joe as if MC is stood over him.
    with dissolve

    u "Fucking piece of shit!"

    scene v8sdd17 # FPP. Show MC picking up the cash that Joe dropped.
    with dissolve

    pause 0.5

    scene v8sdd18 # FPP. Show Joe lying on the floor, MC looking over him but from Joe's side.
    with dissolve

    menu:
        "Kick Joe":
            $ add_point(KCT.TROUBLEMAKER)
            jump volley_joe

        "Walk away":
            jump check_on_josh

label hit_with_pipe:
    scene v8sdd31 # TPP. !RETURN CHARACTERS TO SAME POSITIONS AS v8sdd12! Show MC getting hit on the head with the pipe Joe is holding, MC winces in pain.
    with vpunch

    pause 0.5

    scene v8sdd32 # TPP. Show MC on the ground in pain, Joe standing over him menacingly, Joe mouth open.
    with dissolve

    $ renpy.end_replay()

    je "Hahaha, see ya, \"hero\"."

    scene v8sdd33 # TPP. Show Joe and Lars leaving the scene, one of them is grabbing the drugs from Josh.
    with dissolve

    pause 0.5

    scene v8sdd33a # TPP. Same camera as v8sdd33, show Joe and Lars leaving the scene, MC and Josh on the floor, Josh looking injured and bruised, MC looking dazed.
    with dissolve

    pause 0.5

    scene v8sdd34 # TPP. Show MC getting up from the ground, pain expression.
    with dissolve

    pause 0.5

    jump check_on_josh

label beat_by_lars:
    scene v8sdd35 # TPP. Show MC falling to the ground after taking a punch from Lars.
    with vpunch

    pause 0.75

    scene v8sdd11a # TPP. Show Josh getting hit over the head by Joe with his metal pipe, MC lay on the ground, Lars looking down at MC with a smile, Josh wincing in pain falling to the ground.
    with dissolve

    pause 0.75

    scene v8sdd37 # FPP. Show Joe & Lars standing over MC with sinister smirk, Joe mouth open, both looking at camera.
    with dissolve

    je "A valiant effort, hero, but not good enough. Let's go, Lars."
    $ renpy.end_replay()

    scene v8sdd33 # TPP. Show Joe and Lars leaving the scene, one of them is grabbing the drugs from Josh.
    with dissolve

    pause 0.75

    scene v8sdd33a # TPP. Same camera as v8sdd38, Joe and Lars leaving the alley.
    with dissolve

    pause 0.75

    scene v8sdd34a # TPP. Show MC getting up from the ground, pain expression.
    with dissolve

    jump check_on_josh

label volley_joe:
    scene v8sdd19 # TPP. Show MC kicking Joe in the ribs as he is lying on the ground, MC angry, mouth open.
    with dissolve

    u "Cocksucker..."

    jump check_on_josh

label check_on_josh:
    scene v8sdd20 # TPP. Show MC walking over to Josh who is laying on the floor, Josh looking injured and bruised. From this point onwards Josh should have a bruised face and appear weak/injured.
    with dissolve

    pause 0.75

    scene v8sdd21 # FPP. Show Josh lay on the ground, Josh looking up at camera, Josh pain expression, mouth closed.
    with dissolve

    u "Hey Josh, you alright? Can you move?"

    scene v8sdd21a # FPP. Same camera as v8sdd21, Josh groans, mouth open.
    with dissolve

    jo "Fuck man, this wasn't supposed to happen..."

    scene v8sdd21
    with dissolve

    u "We don't have time for this. We gotta go. C'mon, let's get you home."

    if s28_fightWinner == "MC":

        scene v8sdd22 # TPP. Show MC helping Josh stand up, Josh really acting very injured.
        with dissolve

        pause 0.75

        scene v8sdd23 # TPP. Show MC and Josh leaving the alley, Josh's arm draped over MC's shoulder, MC's arm around Josh's side.
        with dissolve

        pause 0.75

    # -Transition to Scene 29-
    jump after_drugs
