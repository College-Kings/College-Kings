# SCENE 20: Mon Night in Room (Simplr)
# Locations: MC NEW Wolves/Apes Room
# Characters: MC (Outfit 1)
# Time: Monday Night

init python:
    def v10s20_reply1():
        setattr(store, "v10_simplr_known", True)
        contact_Josh.newMessage("Then why are you acting clueless? Any good matches?")
        contact_Josh.addReply("I haven't used it yet.", v10s20_reply2)

    def v10s20_reply2():
        contact_Josh.newMessage("WHAT! I've been talking to so many hot chicks. What are you waiting for?")
        contact_Josh.newMessage("Hop on it.")
        contact_Josh.newMessage("You been under a rock? Get it and check it out. You probably won't get as many girls as me, but tell me how it goes.")
        contact_Josh.addReply("Haha, okay.")

label v10_room_mon_night:
    if joinwolves:
        scene v10smnr1 # TPP. Show mc in his new Wolves room chilling on his bed on his phone.
        with Fade(1, 0, 1)

        pause 0.75

        play sound "sounds/vibrate.mp3"

        $ contact_Josh.newMessage("So what do think!? Any good ones for you?", queue=False)
        $ contact_Josh.addReply("What are you talking about?")
        $ contact_Josh.newMessage("Wait, you don't know what I'm talking about? Everybody on campus knows about it. Except for you I guess.")
        $ contact_Josh.addReply("What does everyone know about?")
        $ contact_Josh.newMessage("The new dating app Simplr, they literally just launched.")
        $ contact_Josh.newMessage("You really haven't heard about it?")
        $ contact_Josh.addReply("Oh yeah, I heard.", v10s20_reply1)
        $ contact_Josh.addReply("I have no idea what you're talking about.", v10s20_reply2)

        label v10s20_PhoneContinueW:
            if contact_Josh.getReplies():
                call screen phone
            if contact_Josh.getReplies():
                "(I should reply to Josh.)"
                jump v10s20_PhoneContinueW

        if v10_simplr_known:
            u "(Okay let's check this out.)"

        else:
            scene v10smnr1a # TPP. Same as 1, MC smiling.
            with dissolve

            u "(I'm not surprised Josh is so excited about this. Too bad the girls have to meet him in person too.)"

            scene v10smnr1
            with dissolve

        # -MC unlocks Simplr-
        # -MC opens the Simplr app-
        # -MC uses the Simplr app-

        u "(Hmm, I can see why so many people are talking about it.)"
        u "(It would be kinda weird though if I saw someone I knew.)"
        u "(Do you try to match with friends you see on there, or is that weird?)"
        u "(I guess I’ll figure that out if it ever comes to it. It's about time I go to bed.)"

        scene v10smnr2 # TPP. Show MC putting down his phone and going to sleep.
        with dissolve

        pause 0.75

        scene black
        with Fade(2, 0, 2)

        pause 1

        jump v10_cafe_w_jenny

    else:
        scene v10smnr3 # TPP. Show mc in his Apes room chilling on his bed  on his phone.
        with Fade(1, 0, 1)

        pause 0.75

        play sound "sounds/vibrate.mp3"

        $ contact_Josh.newMessage("So what do think!? Any good ones for you?", queue=False)
        $ contact_Josh.addReply("What are you talking about?")
        $ contact_Josh.newMessage("Wait, you don't know what I'm talking about? Everybody on campus knows about it. Except for you I guess.")
        $ contact_Josh.addReply("What does everyone know about?")
        $ contact_Josh.newMessage("The new dating app Simplr, they literally just launched.")
        $ contact_Josh.newMessage("You really haven't heard about it?")
        $ contact_Josh.addReply("Oh yeah, I heard.", v10s20_reply1)
        $ contact_Josh.addReply("I have no idea what you're talking about.", v10s20_reply2)

        label v10s20_PhoneContinue2:
            if contact_Josh.getReplies():
                call screen phone
            if contact_Josh.getReplies():
                "(I should reply to Josh.)"
                jump v10s20_PhoneContinue2

        if v10_simplr_known:
            u "(Okay let's check this out.)"

        else:
            scene v10smnr3a # TPP. Same as 3, MC smiling.
            with dissolve

            u "(I'm not surprised Josh is so excited about this. Too bad the girls have to meet him in person too.)"

            scene v10smnr3
            with dissolve

        # -MC unlocks Simplr-
        # -MC opens the Simplr app-
        # -MC uses the Simplr app-

        u "(Hmm, I can see why so many people are talking about it.)"
        u "(It would be kinda weird though if I saw someone I knew.)"
        u "(Do you try to match with friends you see on there, or is that weird?)"
        u "(I guess I’ll figure that out if it ever comes to it. It's about time I go to bed.)"

        scene v10smnr4 # TPP. Show MC putting down his phone and going to sleep.
        with dissolve

        pause 0.75

        scene black
        with Fade(2, 0, 2)

        pause 1

        jump v10_cafe_w_jenny        
