# SCENE 28: Mc & Lindsey in planning room
# Locations: Lindsey planning room
# Characters: LINDSEY (Outfit: 1), MC (Outfit: 9)
# Time: Morning

label v16s28:
    scene v16s28_1 # TPP. Lindsey and MC walking into her planning board room, both neutral, mouths closed
    with dissolve

    pause 0.75

    scene v16s28_2 # TPP. MC and Lindsey standing in front of the planning board, looking at the board (don't show what's written on the board), both neutral, mouths closed
    with dissolve

    pause 0.75

    if (v15_chloe_lindseysabotage and not v15_chloe_postkiwii) and v15_lindsey_recording > 0: ### TODO: Variable
        scene v16s28_3 # FPP. MC and Lindsey standing in front of the planning board, MC looking at Lindsey, Lindsey looking at MC, Lindsey worried expression, mouth open
        with dissolve

        li "Okay, so... Now that we're alone, I can speak more freely."

        scene v16s28_3a # FPP. Same as v16s28_3, Lindsey looking at the board, worried expression, mouth open
        with dissolve

        li "I don't know how the fuck Chloe got that recording. I mean..."

        scene v16s28_3
        with dissolve

        li "You were there that night; you know what happened."

        scene v16s28_3b # FPP. Same as v16s28_3, Lindsey worried, mouth closed
        with dissolve

        u "Yeah, I-"

        scene v16s28_3
        with dissolve

        li "I don't even want to think about it. I'm starting to get paranoid that every room I'm in is bugged or something."

        scene v16s28_3b
        with dissolve

        u "(Damn, if she ever found out it was me...)"

        scene v16s28_3a
        with dissolve

        li "But, with the damage already done, we're gonna have to smash this next phase."

    scene v16s28_3c # FPP. Same as v16s28_3, Lindsey neutral expression, mouth closed
    with dissolve

    u "Okay, so what are you thinking?"

    scene v16s28_3d # FPP. Same as v16s28_3, Lindsey slight smile, mouth open
    with dissolve

    li "I had some other ideas but I think these are the strongest, especially after hearing what Penelope said earlier."

    call screen planningboard # TODO: PLANNING BOARD CODE 

    scene v16s28_4 # TPP. Show MC pointing at something on the board (don't show the actual board, maybe just the back part of it where nothing is written), slight smile, Lindsey looking at where he's pointing with a curious expression, MC mouth open, Lindsey mouth closed
    with dissolve

    u "I think this idea is the strongest."

    if v16s28_lindsey_pb_intereview_polly_choicelindsey_interview: # Interview 
        scene v16s28_3e # FPP. Same as v16s28_3d, Lindsey slight smile, mouth closed
        with dissolve

        u "A lot of people are going to see the paper, so an interview would be great."

        scene v16s28_3d
        with dissolve

        li "Yeah, everyone is going to read that first edition. They're placing copies all over the school."

        scene v16s28_3e
        with dissolve

        u "I can help prepare you to the best of my ability, haha."

        scene v16s28_3d
        with dissolve

        li "I just hope there's no trick questions that can fuck up my campaign."

        scene v16s28_3e
        with dissolve

        u "We can practice, don't worry."
    
    else: # Get Polly to endorse Lindsey 
        scene v16s28_3e
        with dissolve

        u "If we could get Polly to endorse your campaign, I'd say you've basically got this presidency in the bag."

        scene v16s28_3d
        with dissolve

        li "Haha, I like your confidence. I sure hope so."

        scene v16s28_3e
        with dissolve

        u "There are quite a few hoops to jump through to get her on board, but it's totally do-able."

        scene v16s28_3d
        with dissolve

        li "Yeah, and she seems super friendly, especially for being a beautiful pop princess. *Laughs*"

        li "I just hope I don't fan-girl too much if we do get to talk to her."

    scene v16s28_3e
    with dissolve

    menu:
        "Stay positive":
            u "I can't wait to get started, I feel good about this one, it's going to be interesting."

            scene v16s28_3e
            with dissolve

            li "Yes! Phase three is a winner, no doubt."

        "Failing is a possibility":
            scene v16s28_3b
            with dissolve

            u "Let's be realistic, though. It could go wrong, so we should be prepared for that possibility."

            scene v16s28_3
            with dissolve

            li "Don't be so negative, [name]! We can do this, I know it."

            scene v16s28_3e
            with dissolve

            u "Haha, okay. I guess I could be a little more optimistic."

            scene v16s28_3d
            with dissolve

            li "Yes, you could."

    scene v16s28_3f # FPP. Same as v16s28_3d, Lindsey looking at the board, slight smile, mouth open
    with dissolve

    li "I'm feeling good about this one."

    scene v16s28_3d
    with dissolve

    li "And again, for the millionth time, thanks for your help."

    scene v16s28_3e
    with dissolve

    u "Haha, I wouldn't be here if I didn't want to be."

    scene v16s28_3g # FPP. Same as v16s28_3d, Lindsey looking down slightly embarassed, mouth open
    with dissolve

    li "I don't know if I say it often enough, but I appreciate it so much."

    scene v16s28_3d
    with dissolve

    li "Thanks for sticking to this with me."

    if lindsey.relationship == Relationship.FWB: # TODO: Variable
        scene v16s28_5 # TPP. Lindsey pulling MC by his shirt, Lindsey sexy smile, MC slightly surprised, both mouths closed
        with dissolve

        pause 0.75

        play sound "sounds/kiss.mp3"

        scene v16s28_5a # TPP. Lindsey kissing MC
        with dissolve

        pause 0.75

    else: ### if Lindsey Friend
        scene v16s28_6 # TPP. Lindsey giving MC a hug
        with dissolve

        pause 0.75
    
    scene v16s28_3e
    with dissolve

    u "We're in this together."

    scene v16s28_3d
    with dissolve

    li "Ugh, you're the best. Now go, I'll catch up with you later."

    scene v16s28_3e
    with dissolve

    u "Haha, ok. Have a good day."

    scene v16s28_7 # TPP. Show MC walking out of the door, Lindsey in the background, watching him leave, both smiling, mouths closed
    with dissolve

    pause 0.75

    jump v16s29