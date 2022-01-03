# SCENE 20: Mon Night in Room (Simplr)
# Locations: MC NEW Wolves/Apes Room
# Characters: MC (Outfit 1)
# Time: Monday Night

init python:
    def v10s20_reply1():
        setattr(store, "v10_simplr_known", True)
        josh.messenger.newMessage("Then why are you acting clueless? Any good matches?")
        josh.messenger.addReply("I haven't used it yet.", v10s20_reply2)

    def v10s20_reply2():
        josh.messenger.newMessage("WHAT! I've been talking to so many hot chicks. What are you waiting for?")
        josh.messenger.newMessage("Hop on it.")
        josh.messenger.newMessage("You been under a rock? Get it and check it out. You probably won't get as many girls as me, but tell me how it goes.")
        josh.messenger.addReply("Haha, okay.")

label v10_room_mon_night:
    play music "music/v10/Track Scene 20.mp3" fadein 2
    if joinwolves:
        scene v10smnr1 # TPP. Show mc in his new Wolves room chilling on his bed on his phone.
        with Fade(1, 0, 1)

        pause 0.75

        play sound "sounds/vibrate.mp3"

        $ josh.messenger.newMessage("So what do think!? Any good ones for you?", force_send=True)
        $ josh.messenger.addReply("What are you talking about?")
        $ josh.messenger.newMessage("Wait, you don't know what I'm talking about? Everybody on campus knows about it. Except for you I guess.")
        $ josh.messenger.addReply("What does everyone know about?")
        $ josh.messenger.newMessage("The new dating app Simplr, they literally just launched.")
        $ josh.messenger.newMessage("You really haven't heard about it?")
        $ josh.messenger.addReply("Oh yeah, I heard.", v10s20_reply1)
        $ josh.messenger.addReply("I have no idea what you're talking about.", v10s20_reply2)

        label v10s20_PhoneContinueW:
            if josh.messenger.replies:
                call screen phone
            if josh.messenger.replies:
                u "(I should reply to Josh.)"
                jump v10s20_PhoneContinueW

        if v10_simplr_known:
            u "(Okay let's check this out.)"

        else:
            scene v10smnr1a # TPP. Same as 1, MC smiling.
            with dissolve

            u "(I'm not surprised Josh is so excited about this. Too bad the girls have to meet him in person too.)"

            scene v10smnr1
            with dissolve

        $ simplr_app.unlock()

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

        play sound "sounds/vibrate.mp3"

        $ josh.messenger.newMessage("So what do think!? Any good ones for you?", force_send=True)
        $ josh.messenger.addReply("What are you talking about?")
        $ josh.messenger.newMessage("Wait, you don't know what I'm talking about? Everybody on campus knows about it. Except for you I guess.")
        $ josh.messenger.addReply("What does everyone know about?")
        $ josh.messenger.newMessage("The new dating app Simplr, they literally just launched.")
        $ josh.messenger.newMessage("You really haven't heard about it?")
        $ josh.messenger.addReply("Oh yeah, I heard.", v10s20_reply1)
        $ josh.messenger.addReply("I have no idea what you're talking about.", v10s20_reply2)

        label v10s20_PhoneContinue2:
            if josh.messenger.replies:
                call screen phone
            if josh.messenger.replies:
                u "(I should reply to Josh.)"
                jump v10s20_PhoneContinue2

        if v10_simplr_known:
            u "(Okay let's check this out.)"

        else:
            scene v10smnr3a # TPP. Same as 3, MC smiling.
            with dissolve

            u "(I'm not surprised Josh is so excited about this. Too bad the girls have to meet him in person too.)"

            scene v10smnr3
            with dissolve

        $ simplr_app.unlock()

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