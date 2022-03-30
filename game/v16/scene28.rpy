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

    if v15_lindsey_recording > 0:
        scene v16s28_3 # FPP. MC and Lindsey standing in front of the planning board, MC looking at Lindsey, Lindsey looking at MC, Lindsey worried expression, mouth open
        with dissolve

        li "Okay, so... Now that we're alone, I can speak more freely."

        scene v16s28_3a # FPP. Same as v16s28_3, Lindsey looking at the board, worried expression, mouth open
        with dissolve

        li "I don't know how the fuck Chloe got that recording. I mean..."

        scene v16s28_3
        with dissolve

        li "You were there that night, you know what happened."

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

    python:
        lindsey_board = PlanningBoard("images/v16/planning_boards/lindsey_background.webp", money=lindsey_board.money, style="lindsey_board") ### to be replaced with v16 board

        lindsey_board.add_approach("Newspaper",
            "Lindsey gets interviewed for the student newspaper",
            opinion="\"The student newspaper is going to be really popular, especially the first one. It'd be great to have an entire story in there dedicated to my campaign. We can tell whatever story we want, whether it's positively about me or negatively about my opponent.\"")

        lindsey_board.add_approach("Polly",
            "Get Polly to endorse Lindsey",
            opinion="\"A major pop star is in town, and ew have to take advantage of that. Can you imagine if Polly endorsed my campaign? Maybe we can even get her to perform! This would be insane.\"")

        v16s28_lindsey_elijah = lindsey_board.add_subtask("Newspaper",
            "Have Elijah interview Lindsey",
            opinion="\"Elijah is the head of the newspaper so it makes sense to ask him for an interview. Although... He's such a fucking prick. I wouldn't put it past him to agree to this idea simply because he'll want to twist my words into some gossipy blog. We have to be prepared when we meet with him.\"",
            people=[elijah])

        lindsey_board.add_subtask("Newspaper",
            "Have Riley interview Lindsey",
            opinion="\"Riley is new to the newspaper scene, plus she's one of the girls. I'd definitely be more comfortable having Riley interview me, but then again, we want to make sure the article comes across professional, so we'll need to prepare our topics.\"",
            people=[riley])

        lindsey_board.add_task("Newspaper",
            "Prepare Lindsey for interview",
            opinion="\"You're going to be my PR coach, okay? We're even going to have a list of mock interview questions, so we can really test how I do under pressure and you can give me tips on what might be best to say to our interviewer.\"",
            people=[lindsey,mc])

        lindsey_board.add_task("Newspaper",
            "Lindsey does the interview",
            opinion="\"I have to do this interview alone, because they'd definitely write that in there. \"She can't even do an interview on her own, how can she run a sorority?\", so... yeah. You can watch and listen from a distance or something. I can call you while I'm in the room maybe? Whatever it is, they have to think I've done this alone.\"",
            people=[lindsey])

        lindsey_board.add_task("Polly",
            "Find out where Polly is staying",
            opinion="\"The first step to this amazing idea is to find out where Polly is staying. I have a friend or two who might be able to help us track her down. It will take some effort to find her, but I promise you. I will find her.\"")

        v16s28_lindsey_roomservice = lindsey_board.add_subtask("Polly",
            "Pretend to be room service",
            opinion="\"Once we know where she's staying, we can get our hands on some matching employee uniforms, and go up to her room as Room Service. We just have to be smart about what we say, we don't want her to think we're crazy stalkers, you know?\"")

        lindsey_board.add_subtask("Polly",
            "Show up as yourselves",
            opinion="\"Once we know where she's staying, we take our chances by knocking on her door. Polly isn't a horrible person, so she won't turn down two really big fans, but we have to be careful not to freak her out.\"")

        lindsey_board.add_task("Polly",
            "Convince Polly to endorse Lindsey at her acoustic concert",
            opinion="\"Finally, we ask Polly to consider supporting my campaign. I have no idea if she'll perform, or post something, or what we can get her to do... But hopefully we can get something.\"",
            people=[lindsey,mc,polly])

    call screen planning_board(lindsey_board)
    
    if lindsey_board.approach is not None:
        $ v16_lindsey_newspaper = lindsey_board.approach.id == "Newspaper"

    if lindsey_board.selected_task is not None:
        $ v16_lindsey_elijah = lindsey_board.selected_task == v16s28_lindsey_elijah
        $ v16_lindsey_roomservice = lindsey_board.selected_task == v16s28_lindsey_roomservice

    # End planning board (screen disappears)

    scene v16s28_4 # TPP. Show MC pointing at something on the board (don't show the actual board, maybe just the back part of it where nothing is written), slight smile, Lindsey looking at where he's pointing with a curious expression, MC mouth open, Lindsey mouth closed
    with dissolve

    u "I think this idea is the strongest."

    if v16_lindsey_newspaper: # Interview 
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

            scene v16s28_3d
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

    if lindsey.relationship >= Relationship.FWB:
        scene v16s28_5 # TPP. Lindsey pulling MC by his shirt, Lindsey sexy smile, MC slightly surprised, both mouths closed
        with dissolve

        pause 1.5

        scene v16s28_5a # TPP. Lindsey kissing MC
        with dissolve
        play sound "sounds/kiss.mp3"
        pause 1.5

    else:
        scene v16s28_6 # TPP. Lindsey giving MC a hug
        with dissolve

        pause 1.25
    
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