# SCENE 7: Mc talks to Autumn in Hallway
# Locations: School Hallway
# Characters: MC (Outfit: 5), AUTUMN (Outfit: 2)
# Time: Morning
# Render Count: 8 Unique Renders 23 Total Renders

label v16s7:
    scene v16s7_1 # TPP. Show MC walking through a school hallway, slight smile, mouth is closed, Show a PA system on the wall somewhere behind MC
    with dissolve

    pause 0.75

    if v15_chloe_lindseysabotage and not v15_chloe_postkiwii: # -if MC chose Embarrass Lindsey, PA system announcement
        scene v16s7_2 # TPP. MC and a few other random characters show up in frame, NO MAIN CHARACTERS, all of them stop walking and look up at the PA system speaker on the wall. All of them no expressions, mouths are closed
        with dissolve

        pause 0.75

        if v15_lindsey_gamenight: # Game Night
            if v15_lindsey_alcohol and v15bring_up_chloe:
                scene v16s7_3 # FPP. Close up view of the PA system speaker on the wall
                with dissolve

                pa "*Drunk* What I don't like about Chloe?"

                pa "*Drunk* *Giggles* do you want a list? I mean, where do I start?"

                scene v16s7_2a # TPP MC has a slight smile, mouth is closed still looking at the PA system speaker on the wall. The other Random Characters are looking at each other and the PA system with excitement
                with dissolve

                u "(Oh, my fucking god, it's happening.)"

                scene v16s7_3
                with dissolve

                pa "*Drunk* Her plastic boobs?"

                pa "*Drunk* Or her plastic nose?"

                if v15say_nothing: # -if MC also chose Say nothing on Games Night
                    scene v16s7_2b # TPP. MC has a slight smile, mouth is closed, looking at the Random Characters, The Random Characters are now laughing, and looking at each other
                    with dissolve

                    u "(Oh... This is it!)"

                    scene v16s7_3
                    with dissolve

                    pa "*Drunk* That's why she's doing everything she can to not lose her scholarship."

                    pa "*Drunk* She'd have to sell a good chunk of her body back to the surgeons in order to pay for school, ha!"

                    scene v16s7_2c # TPP. MC has a slight smile, mouth is closed, looking at the Random Characters, One of the Random Characters is laughing so hard another Random Character has to hold him/her up to keep him/her from falling down.
                    with dissolve

                    u "(Oh shit!)"

            elif v15game_night_kct_check: # Lindsey was not drunk, but MC passed a KCT Check
                scene v16s7_3
                with dissolve

                pa "...She's my campaign rival..."

                pa "What do you want me to say? That her boobs are obviously fake? Everyone knows that..."

                scene v16s7_2b
                with dissolve

                u "(Oh, shit...)"

        elif not v15_lindsey_gamenight: # VIP Night
            if v15_lindsey_alcohol and v15_stay_on_topic:
                scene v16s7_3
                with dissolve

                pa "*Tipsy* What I don't like about Chloe?"

                pa "*Tipsy* What doesn't annoy me? Everything about her is annoying."

                scene v16s7_2a
                with dissolve

                u "(Oh, my fucking god, it's happening.)"

                scene v16s7_3
                with dissolve

                pa "*Tipsy* She gets everything handed to her, even her fucking boobs!"

                pa "*Drunk* I mean no wonder she's such a bitch all the time..."

                if v15say_nothing: # -if MC also chose Say nothing on VIP night
                    scene v16s7_2b
                    with dissolve

                    u "(Oh... This is it!)"

                    scene v16s7_3
                    with dissolve

                    pa "*Drunk* She's constantly worried about losing her free ride to a degree."

                    pa "*Drunk* Without the President's scholarship, she'd have to sell all of that plastic back to the surgeons... *Laughs*"

                    scene v16s7_2c
                    with dissolve

                    u "(Oh shit!)"

            elif v15_lindsey_recording == 1: # Lindsey was not drunk, but MC passed a KCT Check
                pa "What do you want me to say? That she gets everything handed to her?"

                pa "Or that the only reason she wants to be President is because she can't afford tuition?"

                scene v16s7_2b
                with dissolve

                u "(Oh, shit...)"

        scene v16s7_2d # TPP. MC is just looking at the random characters excitement, MC slight smile, mouth is closed, the random characters have different poses and are still all laughing, Show Autumn walking towards MC, concerned expression, mouth is closed
        with dissolve

        u "(Shit is about to hit the fan!)"

        scene v16s7_2e # TPP. The Random Characters are walking away smiling and now MC and Autumn are face to face looking at each other. Mc has no expression mouth is closed, Autumn has a concerned expression mouth is closed
        with dissolve

        pause 0.75

    elif v15_chloe_lindseysabotage and v15s8_chloe_kiwii == chloe_board.add_subtask("Sabotage") and v15_chloe_postkiwii = chloe_board.selected_task == v15s8_chloe_kiwii: # -if MC chose Embarrass Lindsey, Kiwii post announcement
        scene v16s7_1a # TPP. MC is still in the school hallway as v16s7_1 MC's phone vibrates and he pulls his phone from his pocket and looks at it
        with dissolve

        pause 0.75

        $ chloe.messenger.newMessage("Check out SVC's Kiwii page and play the audio ;)")
            
        ### force open kiwii and/or check for Chloe message
        # -MC opens his Kiwii app to view the SVC Kiwii page. The most recent post is an audio file posted by an anonymous user with an empty avatar. The audio autoplays-

        if v15_lindsey_gamenight:
            if v15_lindsey_alcohol and v15bring_up_chloe:
                scene v16s7_4 # FPP. Close up shot of MC's phone, show something like "KIWI AUDIO" with the KIWI logo on the screen
                with dissolve

                pha "*Drunk* What I don't like about Chloe?"

                pha "*Drunk* *Giggles* do you want a list? I mean, where do I start?"

                scene v16s7_5 # TPP. close up shot of MC's face, slight smile, mouth is slightly open.
                with dissolve

                u "(Oh, my fucking god, it's happening.)"

                scene v16s7_4
                with dissolve

                pha "*Drunk* Her plastic boobs?"

                pha "*Drunk* Or her plastic nose?"

                if v15say_nothing: # -if MC also chose Say nothing on Games Night
                    scene v16s7_5a # TPP. close up shot of MC's Face, he has an excited expression, mouth is open
                    with dissolve

                    u "(Oh... This is it!)"

                    scene v16s7_4
                    with dissolve

                    pha "*Drunk* That's why she's doing everything she can to not lose her scholarship."

                    pha "*Drunk* She'd have to sell a good chunk of her body back to the surgeons in order to pay for school, ha!"

                    scene v16s7_5
                    with dissolve

                    u "(Oh shit!)"

            elif v15game_night_kct_check: # Lindsey was not drunk, but MC passed a KCT Check
                scene v16s7_4
                with dissolve

                pha "...She's my campaign rival..."

                pha "What do you want me to say? That her boobs are obviously fake? Everyone knows that..."

                scene v16s7_5
                with dissolve

                u "(Oh, shit...)"

        elif not v15_lindsey_gamenight: # VIP Night
            if v15_lindsey_alcohol and v15_stay_on_topic:
                scene v16s7_4
                with dissolve

                pha "*Tipsy* What I don't like about Chloe?"

                pha "*Tipsy* What doesn't annoy me? Everything about her is annoying."

                scene v16s7_5
                with dissolve

                u "(Oh, my fucking god, it's happening.)"

                scene v16s7_4
                with dissolve

                pha "*Tipsy* She gets everything handed to her, even her fucking boobs!"

                pha "*Drunk* I mean no wonder she's such a bitch all the time..."

                if v15say_nothing: # -if MC also chose Say nothing on VIP night
                    scene v16s7_5a
                    with dissolve

                    u "(Oh... This is it!)"

                    scene v16s7_4
                    with dissolve

                    pha "*Drunk* She's constantly worried about losing her free ride to a degree."

                    pha "*Drunk* Without the President's scholarship, she'd have to sell all of that plastic back to the surgeons... *Laughs*"

                    scene v16s7_5
                    with dissolve

                    u "(Oh shit!)"

            elif v15_lindsey_recording == 1: # Lindsey was not drunk, but MC passed a KCT Check
                scene v16s7_4
                with dissolve

                pha "What do you want me to say? That she gets everything handed to her?"

                pha "Or that the only reason she wants to be President is because she can't afford tuition?"

                scene v16s7_5
                with dissolve

                u "(Oh, shit...)"

        scene v16s7_2d
        with dissolve

        u "(Shit is about to hit the fan!)"

        scene v16s7_2e
        with dissolve
        
        pause 0.75

    else: # -if MC not helping Chloe and/or did not get Lindsey drunk at Games night or VIP night
        jump v16s7_did_not_sabotage_lindsey

    scene v16s7_6 # FPP. Show Autumn with a concerned expression, mouth is open, looking at MC
    with dissolve

    aut "What the hell did I just hear?"

    scene v16s7_6a # FPP. Show Autumn with a concerned expression, mouth is closed, looking at MC
    with dissolve

    u "The same thing everyone else just heard. Lindsey talking shit about Chloe."

    scene v16s7_6
    with dissolve

    aut "Yeah, I remember that night, but there was no ill-intent behind it. Lindsey was drunk."

    scene v16s7_6a
    with dissolve

    u "I know."

    scene v16s7_6
    with dissolve

    aut "I'm guessing Chloe is behind this? How the hell did she even get a recording of it, though?"

    menu:
        "Defend Lindsey":
            scene v16s7_6a
            with dissolve

            u "No idea. You're right about Lindsey though, she didn't actually mean any of it. Chloe's playing dirty here."

        "Defend Chloe":
            scene v16s7_6a
            with dissolve

            u "No idea. But there's no denying that Lindsey said those things about Chloe."

            scene v16s7_6
            with dissolve

            aut "But she was drunk, [name]. She didn't mean any of it."

            scene v16s7_6a
            with dissolve

            u "I don't know. People are more honest when they're drunk. Drunk words are sober thoughts, you know?"

            scene v16s7_6
            with dissolve

            aut "Yeah, yeah... Still, I feel sorry for her."

            scene v16s7_6a
            with dissolve

            u "I feel sorry for Chloe. Lindsey just roasted her, and the entire school heard it. Lindsey isn't really the victim here."

    scene v16s7_6b # FPP. Autumn looks away from MC in the direction of someone shouting, still a concerned expression, mouth is still closed
    with dissolve

    rg1 "Yo! Chloe's out there, look!"

    scene v16s7_6c # FPP. same as v16s7_6b Autumn looks in another direction
    with dissolve

    rg2 "I think she's crying, bro. Let's go make sure she's okay."

    scene v16s7_6a
    with dissolve

    u "Should we go check on her?"

    scene v16s7_6
    with dissolve

    aut "No, I'm not getting involved in all the drama."

    scene v16s7_7 # TPP. Show just the top halves of MC and Autumn, no one else in the background, MC looks towards where the guys were shouting, autumn is looking at MC, Autumn and MC both have no expressions, mouths are closed
    with dissolve

    pause 0.75

    scene v16s7_7a # TPP. same as v16s7_7 Autumn grabs MC's face and turns his head facing back towards facing her, Autumn and MC both have no expressions, mouths are closed
    with dissolve

    pause 0.75

    scene v16s7_6
    with dissolve

    aut "And you shouldn't either. It's not worth the energy, [name]. This isn't your fight."

    scene v16s7_6a
    with dissolve

    u "You're probably right, but-"

    u "I need to see what's going on."

    scene v16s7_6
    with dissolve

    aut "Alright, but don't say I didn't warn you."

    scene v16s7_6a
    with dissolve

    u "Don't worry, I'll come crying when I regret this decision."

    if autumn.relationship >= Relationship.KISS: # -if autumnrs (they kissed in v15)
        scene v16s7_6d # FPP. Autumn has a slight smile, mouth is open, looking at MC
        with dissolve

        aut "*Sighs* I look forward to it, actually."

        scene v16s7_6e # FPP. Autumn has a slight smile, mouth is closed, looking at MC
        with dissolve

        pause 0.75

    else:
        scene v16s7_6f # FPP. Autumn rolls her eyes, no expression, mouth is slightly open
        with dissolve

        aut "*Sighs*"

        scene v16s7_6e
        with dissolve

        pause 0.75

    scene v16s7_8 # TPP. Autumn walks away from MC, waving goodbye, slight smile mouth is closed, looking at MC, MC has a slight smile, mouth is closed, looking at Autumn
    with dissolve

    pause 0.75

    jump v16s8 # -If PA system or Kiwii post Announcement, transition to v16s8-

    label v16s7_did_not_sabotage_lindsey:
        scene v16s7_1b # TPP. Show MC walking along the hallway. Autumn is walking the other way. They share a smile, stopping to chat
        with dissolve

        pause 0.75

        scene v16s7_6d
        with dissolve

        aut "Hey, [name]."

        scene v16s7_6e
        with dissolve

        u "Fancy seeing you here."

        scene v16s7_6d
        with dissolve

        aut "At the school we both go to? Yeah... What are the odds? *Giggles*"

        aut "I'm glad I bumped into you, actually."

        scene v16s7_6e
        with dissolve

        u "Oh, the pleasure is all mine."

        scene v16s7_6d
        with dissolve

        aut "*Laughs* I wanted to let you know that I expect to see you at the reopening of the dog shelter on Thursday."

        scene v16s7_6e
        with dissolve

        u "Oh, of course. I wouldn't miss it for the world."

        scene v16s7_6d
        with dissolve

        aut "Ha, thanks."

        aut "Hopefully we can get some of the dogs adopted too."

        scene v16s7_6e
        with dissolve

        u "That would be nice, yeah."

        scene v16s7_6e
        with dissolve

        menu:
            "Ask about [dog_name]":
                scene v16s7_6e
                with dissolve

                u "How's [dog_name]? Still happy with the awesome name I gave him?"

                scene v16s7_6d
                with dissolve

                aut "Oh, of course! *Chuckles* He's still with us."

                aut "There's been some interest in him though. There's a couple coming back to see him tomorrow."

                scene v16s7_6e
                with dissolve

                u "Fingers crossed then."

                scene v16s7_6d
                with dissolve

                aut "Yeah, he's such a cutie. I really hope they take him."

                scene v16s7_6e
                with dissolve

                u "I'm sure [dog_name] will be able to charm them."

                scene v16s7_6e
                with dissolve

                pause 0.75

                scene v16s7_6d
                with dissolve

                aut "Yeah, me too."

            "Get to class":
                scene v16s7_6e
                with dissolve

                u "Anyway, I should get to economics class now."

                scene v16s7_6d
                with dissolve

                aut "Ooh, economics! Fun times... *Chortles*"

                scene v16s7_6e
                with dissolve

                u "Yeah, not in the mood to get yelled at for being late today. *Laughs*"

                scene v16s7_6d
                with dissolve

                aut "Haha, me too."

        scene v16s7_6d
        with dissolve

        aut "I've got a lot to do today and not enough time to do it. See you later!"

        scene v16s7_6e
        with dissolve

        u "Never a dull moment for you presidents, huh? Bye, Autumn."

        scene v16s7_8
        with dissolve

        pause 0.75

        scene v16s7_8a # FPP. Mc is shown walking alone and away from Autumns direction in v16s7_8, slight smile, mouth is closed
        with dissolve

        pause 0.75

        jump v16s9 # -If not on Announcement path, transition to v16s9-