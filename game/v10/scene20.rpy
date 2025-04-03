# SCENE 20: Mon Night in Room (Simplr)
# Locations: MC NEW Wolves/Apes Room
# Characters: MC (Outfit 1)
# Time: Monday Night

label v10_room_mon_night:
    play music music.ck1.v10.Track_Scene_20 fadein 2
    if mc.frat == Frat.WOLVES:
        scene v10smnr1 # TPP. Show mc in his new Wolves room chilling on his bed on his phone.
        with Fade(1, 0, 1)

        pause 0.75

        play sound sound.vibrate

        python:
            v10s20_reply1 = MessageBuilder(josh)
            v10s20_reply1.set_variable("v10_simplr_known", True)
            v10s20_reply1.new_message("Then why are you acting clueless? Any good matches?")
            v10s20_reply1.add_reply("I haven't used it yet.", v10s20_reply2)

            v10s20_reply2 = MessageBuilder(josh)
            v10s20_reply2.new_message("WHAT! I've been talking to so many hot chicks. What are you waiting for?")
            v10s20_reply2.new_message("Hop on it.")
            v10s20_reply2.new_message("You been under a rock? Get it and check it out. You probably won't get as many girls as me, but tell me how it goes.")
            v10s20_reply2.add_reply("Haha, okay.")
        
        $ MessengerService.new_message(josh, "So what do think!? Any good ones for you?")
        $ MessengerService.add_reply(josh, "What are you talking about?")
        $ MessengerService.new_message(josh, "Wait, you don't know what I'm talking about? Everybody on campus knows about it. Except for you I guess.")
        $ MessengerService.add_reply(josh, "What does everyone know about?")
        $ MessengerService.new_message(josh, "The new dating app Simplr, they literally just launched.")
        $ MessengerService.new_message(josh, "You really haven't heard about it?")
        $ MessengerService.add_replies(josh,
            Reply("Oh yeah, I heard.", v10s20_reply1),
            Reply("I have no idea what you're talking about.", v10s20_reply2)
        )

        while MessengerService.has_replies(josh):
            call screen phone
            if MessengerService.has_replies(josh):
                u "(I should reply to Josh.)"

        if simplr_app not in phone.applications:
            $ phone.applications.append(simplr_app)
        
        if v10_simplr_known:
            u "(Okay let's check this out.)"

        else:
            scene v10smnr1a # TPP. Same as 1, MC smiling.
            with dissolve

            u "(I'm not surprised Josh is so excited about this. Too bad the girls have to meet him in person too.)"

            scene v10smnr1
            with dissolve

        u "(Hmm, I can see why so many people are talking about it.)"
        u "(It would be kinda weird though if I saw someone I knew.)"
        u "(Do you try to match with friends you see on there, or is that weird?)"
        u "(I guess I'll figure that out if it ever comes to it. It's about time I go to bed.)"

        scene v10smnr2 # TPP. Show MC putting down his phone and going to sleep.
        with dissolve

        pause 0.75

        scene black
        with Fade(2, 0, 2)

        pause 1

        stop music fadeout 3

        jump v10_cafe_w_jenny

    else:
        scene v10smnr3 # TPP. Show mc in his Apes room chilling on his bed on his phone.
        with Fade(1, 0, 1)

        pause 0.75

        play sound sound.vibrate

        python:
            v10s20_reply1 = MessageBuilder(josh)
            v10s20_reply1.set_variable("v10_simplr_known", True)
            v10s20_reply1.new_message("Then why are you acting clueless? Any good matches?")
            v10s20_reply1.add_reply("I haven't used it yet.", v10s20_reply2)

            v10s20_reply2 = MessageBuilder(josh)
            v10s20_reply2.new_message("WHAT! I've been talking to so many hot chicks. What are you waiting for?")
            v10s20_reply2.new_message("Hop on it.")
            v10s20_reply2.new_message("You been under a rock? Get it and check it out. You probably won't get as many girls as me, but tell me how it goes.")
            v10s20_reply2.add_reply("Haha, okay.")

        $ MessengerService.new_message(josh, "So what do think!? Any good ones for you?")
        $ MessengerService.add_reply(josh, "What are you talking about?")
        $ MessengerService.new_message(josh, "Wait, you don't know what I'm talking about? Everybody on campus knows about it. Except for you I guess.")
        $ MessengerService.add_reply(josh, "What does everyone know about?")
        $ MessengerService.new_message(josh, "The new dating app Simplr, they literally just launched.")
        $ MessengerService.new_message(josh, "You really haven't heard about it?")
        $ MessengerService.add_replies(josh,
            Reply("Oh yeah, I heard.", v10s20_reply1),
            Reply("I have no idea what you're talking about.", v10s20_reply2)
        )
        while MessengerService.has_replies(josh):
            call screen phone
            if MessengerService.has_replies(josh):
                u "(I should reply to Josh.)"

        if v10_simplr_known:
            u "(Okay let's check this out.)"

        else:
            scene v10smnr3a # TPP. Same as 3, MC smiling.
            with dissolve

            u "(I'm not surprised Josh is so excited about this. Too bad the girls have to meet him in person too.)"

            scene v10smnr3
            with dissolve

        u "(Hmm, I can see why so many people are talking about it.)"
        u "(It would be kinda weird though if I saw someone I knew.)"
        u "(Do you try to match with friends you see on there, or is that weird?)"
        u "(I guess I'll figure that out if it ever comes to it. It's about time I go to bed.)"

        scene v10smnr4 # TPP. Show MC putting down his phone and going to sleep.
        with dissolve

        pause 0.75

        scene black
        with Fade(2, 0, 2)

        pause 1
        stop music fadeout 3
        jump v10_cafe_w_jenny
