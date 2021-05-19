# Sun Evening in Room
# Location: MC Wolves Room, MC Apes Room
# Outfits: MC Outfit 2
# Time: Sunday Evening

init python:
    def v8s19_reply1(): # s19_reply5
        contact_Amber.newMessage("It's only fair, right? Make us even")
        if joinwolves:
            contact_Amber.addImgReply("images/v8/Scene 19/w_dick_pic.webp")

        else:
            contact_Amber.addImgReply("images/v8/Scene 19/a_dick_pic.webp")

        contact_Amber.newMessage("Wow, better than I thought")
        contact_Amber.addReply("So you thought about it?")
        contact_Amber.newMessage("Maybe")
        contact_Amber.addReply("Aw man you're driving me crazy")
        contact_Amber.newMessage("So do something about it")
        contact_Amber.addReply("Now? What about you?")
        contact_Amber.newImgMessage("images/v8/Scene 19/amb_pussy_pic.webp")
        contact_Amber.addReply("Aw fuck", "s19_reply10")
        contact_Amber.newMessage("You like?")
        contact_Amber.addReply("I love! You're so hot!")
        contact_Amber.newMessage("What would you do if you were here?")
        contact_Amber.addReply("I would eat you until you couldn't take it anymore")
        contact_Amber.newMessage("And then what?")
        contact_Amber.addReply("I'd fuck you so good you'd scream my name")
        contact_Amber.newMessage("I'm close. Will you finish with me?")
        contact_Amber.addReply("Oh, God yes!")

    def v8s19_reply2():
        contact_Amber.newMessage("Good. Maybe someday we can think about things in the same room and see what happens")
        contact_Amber.addReply("Please do")
        contact_Amber.newMessage("I guess I better get back to studying. I keep getting distracted")
        contact_Amber.addReply("I'm not gonna be able to think of anything else now. I'm done studying")
        contact_Amber.newMessage("Well, sleep tight then ;)") 

    def v8s19_reply3():
        contact_Emily.newMessage("Great! See you there!")

    def v8s19_reply4():
        contact_Emily.newMessage("You sure you're not mad?")
        contact_Emily.addReply("No, not at all. Just beat. I'd love to go some other time")
        contact_Emily.newMessage("Okay talk to you soon")
        contact_Emily.addReply("Goodnight")


label sun_eve_room:
    if joinwolves:
        scene v8sser1 # TPP. Show MC lying on his Wolves bed on his phone.
        with fade

        if not laurenrs:
            play sound "sounds/vibrate.mp3"
            $ contact_Amber.newMessage("Hey u up?", queue=False)
            $ contact_Amber.addReply("Always for you ;)")
            $ contact_Amber.newMessage("That's what I was hoping to hear")
            $ contact_Amber.addReply("I can be even more up if you want...")
            $ contact_Amber.newMessage("Really? Just like that?")
            $ contact_Amber.addReply("What can I say? You're hot")
            $ contact_Amber.newMessage("You're pretty hot yourself and I'm... thinking about things")
            $ contact_Amber.addReply("What kind of things? Same things I'm thinking? ;)")
            $ contact_Amber.newMessage("I think so")
            $ contact_Amber.addReply("Wanna see what thinking about you has done to me?", v8s19_reply1)
            $ contact_Amber.addReply("I look at your pic all the time...when I'm thinking about things", v8s19_reply2)

        else:
            # -MC's phone buzzes-
            $ contact_Lauren.newMessage("Hey, Sweetie, what are you up to?", queue=False)
            $ contact_Lauren.addReply("Nothing, just catching up on some homework. You having a good night?")
            $ contact_Lauren.newMessage("It would be better if you were here...")
            $ contact_Lauren.addReply("Really?")
            $ contact_Lauren.newMessage("I could use some snuggles.")
            $ contact_Lauren.addReply("Aww, I'd love to get some snuggles. When can I see you again?")
            $ contact_Lauren.newMessage("I have a big test coming up but after that? I miss you")
            $ contact_Lauren.addReply("I miss you too. It's a date. Just let me know")
            $ contact_Lauren.newMessage("Goodnight")
            $ contact_Lauren.addReply("Goodnight")

        call screen phone

        if contact_Amber.getMessage("Wanna see what thinking about you has done to me?"):
            scene v8sser2
            with dissolve

            $ contact_Amber.newMessage("NOW!", queue=False)
            $ contact_Amber.addReply("NOW!")
            $ contact_Amber.addReply("Holy shit, Amber! You're amazing!")
            $ contact_Amber.newMessage("You weren't too bad yourself. Next time we need to do this in person")
            $ contact_Amber.addReply("Give me 5 minutes ;)")
            $ contact_Amber.newMessage("You're so cute! But it's time for bed. Dream about me ;)")
            $ contact_Amber.addReply("With pleasure! Night!")

            call screen phone

        ### ERROR: -Continue after choices- [MC still in bed] ###
        label s19_replyCont1:
            if forgiveemily:
                # -MC's phone buzzes-
                ### ERROR: (Aww, she couldn't get enough of me) [I figure this line works for either scenario but let me know if I should change it] ###
                $ contact_Emily.newMessage("Hey, I was thinking", queue=False)
                $ contact_Emily.addReply("Uh oh that can't be good ;)")
                $ contact_Emily.newMessage("Wanna meet up at the arcade?")

                if hcGirl == "emily":
                    $ contact_Emily.newMessage("I feel so bad about homecoming and want to make it up to you. My treat!")
                $ contact_Emily.addReply("Sure! Sounds like fun. I can be there in a few minutes", v8s19_reply3)
                $ contact_Emily.addReply("I would but it's getting late and I haven't even started Mr. Lee's project", v8s19_reply4)

                call screen phone

                scene v8sser1a # TPP. Same camera as v8sser1, show MC lying on his side as if to go to sleep.
                with dissolve

                u "(I think I'll get an early night)"

            else:
                scene v8sser1a
                with dissolve

                u "(I think I'll get an early night)"

            jump mon_morning_room

    else:
        scene v8sser4 # TPP. Show MC sat on his Apes bed on his phone.
        with fade

        if not laurenrs:
            play sound "sounds/vibrate.mp3"
            $ contact_Amber.newMessage("Hey u up?", queue=False)
            $ contact_Amber.addReply("Always for you ;)")
            $ contact_Amber.newMessage("That's what I was hoping to hear")
            $ contact_Amber.addReply("I can be even more up if you want...")
            $ contact_Amber.newMessage("Really? Just like that?")
            $ contact_Amber.addReply("What can I say? You're hot")
            $ contact_Amber.newMessage("You're pretty hot yourself and I'm... thinking about things")
            $ contact_Amber.addReply("What kind of things? Same things I'm thinking? ;)")
            $ contact_Amber.newMessage("I think so")
            $ contact_Amber.addReply("Wanna see what thinking about you has done to me?", v8s19_reply1)
            $ contact_Amber.addReply("I look at your pic all the time...when I'm thinking about things", v8s19_reply2)

        else:
            # -MC's phone buzzes-
            $ contact_Lauren.newMessage("Hey, Sweetie, what are you up to?", queue=False)
            $ contact_Lauren.addReply("Nothing, just catching up on some homework. You having a good night?")
            $ contact_Lauren.newMessage("It would be better if you were here...")
            $ contact_Lauren.addReply("Really?")
            $ contact_Lauren.newMessage("I could use some snuggles.")
            $ contact_Lauren.addReply("Aww, I'd love to get some snuggles. When can I see you again?")
            $ contact_Lauren.newMessage("I have a big test coming up but after that? I miss you")
            $ contact_Lauren.addReply("I miss you too. It's a date. Just let me know")
            $ contact_Lauren.newMessage("Goodnight")
            $ contact_Lauren.addReply("Goodnight")

        call screen phone

        label s19_replyCont2:
            ### ERROR: -Continue after choices- [MC still in bed] ###
            if forgiveemily:
                # -MC's phone buzzes-
                ### ERROR: (Aww, she couldn't get enough of me) [I figure this line works for either scenario but let me know if I should change it] ###
                $ contact_Emily.newMessage("Hey, I was thinking", queue=False)
                $ contact_Emily.addReply("Uh oh that can't be good ;)")
                $ contact_Emily.newMessage("Wanna meet up at the arcade?")

                if hcGirl == "emily":
                    $ contact_Emily.newMessage("I feel so bad about homecoming and want to make it up to you. My treat!")
                $ contact_Emily.addReply("Sure! Sounds like fun. I can be there in a few minutes", v8s19_reply3)
                $ contact_Emily.addReply("I would but it's getting late and I haven't even started Mr. Lee's project", v8s19_reply4)

                call screen phone

                scene v8sser4a # TPP. Same camera as v8sser4, show MC lying on his side as if to go to sleep.
                with dissolve

                u "(I think I'll get an early night)"

            else:
                scene v8sser4a
                with dissolve

                u "(I think I'll get an early night)"

            jump mon_morning_room