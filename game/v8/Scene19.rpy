# Sun Evening in Room
# Location: MC Wolves Room, MC Apes Room
# Outfits: MC Outfit 2
# Time: Sunday Evening

init python:
    def v8s19_reply1():

        setattr(store, "text_with_an_s", True)
        grantAchievement("text_with_an_s")

        contact_Amber.newMessage(_("It's only fair, right? Make us even"))
        if config_censored:
            contact_Amber.addImgReply("gui/censoredPopup/censoredBackground.webp")

        elif joinwolves:
            contact_Amber.addImgReply("images/v8/Scene 19/w_dick_pic.webp")

        else:
            contact_Amber.addImgReply("images/v8/Scene 19/a_dick_pic.webp")

        contact_Amber.newMessage(_("Wow, better than I thought"))
        contact_Amber.addReply(_("So you thought about it?"))
        contact_Amber.newMessage(_("Maybe"))
        contact_Amber.addReply(_("Aw man you're driving me crazy"))
        contact_Amber.newMessage(_("So do something about it"))
        contact_Amber.addReply(_("Now? What about you?"))
        
        if config_censored:
            contact_Amber.newImgMessage("gui/censoredPopup/censoredBackground.webp")

        else:
            contact_Amber.newImgMessage("images/v8/Scene 19/amb_pussy_pic.webp")

        contact_Amber.addReply(_("Aw fuck"))
        contact_Amber.newMessage(_("You like?"))
        contact_Amber.addReply(_("I love! You're so hot!"))
        contact_Amber.newMessage(_("What would you do if you were here?"))
        contact_Amber.addReply(_("I would eat you until you couldn't take it anymore"))
        contact_Amber.newMessage(_("And then what?"))
        contact_Amber.addReply(_("I'd fuck you so good you'd scream my name"))
        contact_Amber.newMessage(_("I'm close. Will you finish with me?"))
        contact_Amber.addReply(_("Oh, God yes!"))
        contact_Amber.newMessage(_("NOW!"))
        contact_Amber.addReply(_("NOW!"))
        contact_Amber.newMessage("")
        contact_Amber.addReply(_("Holy shit, Amber! You're amazing!"))
        contact_Amber.newMessage(_("You weren't too bad yourself. Next time we need to do this in person"))
        contact_Amber.addReply(_("Give me 5 minutes ;)"))
        contact_Amber.newMessage(_("You're so cute! But it's time for bed. Dream about me ;)"))
        contact_Amber.addReply(_("With pleasure! Night!"))

    def v8s19_reply2():
        contact_Amber.newMessage(_("Good. Maybe someday we can think about things in the same room and see what happens"))
        contact_Amber.addReply(_("Please do"))
        contact_Amber.newMessage(_("I guess I better get back to studying. I keep getting distracted"))
        contact_Amber.addReply(_("I'm not gonna be able to think of anything else now. I'm done studying"))
        contact_Amber.newMessage(_("Well, sleep tight then ;)"))

    def v8s19_reply3():
        contact_Emily.newMessage(_("Great! See you there!"))

    def v8s19_reply4():
        contact_Emily.newMessage(_("You sure you're not mad?"))
        contact_Emily.addReply(_("No, not at all. Just beat. I'd love to go some other time"))
        contact_Emily.newMessage(_("Okay talk to you soon"))
        contact_Emily.addReply(_("Goodnight"))


label sun_eve_room:
    if joinwolves:
        scene v8sser1 # TPP. Show MC lying on his Wolves bed on his phone.
        with fade

        if not laurenrs:
            play sound "sounds/vibrate.mp3"
            $ contact_Amber.newMessage(_("Hey u up?"), queue=False)
            $ contact_Amber.addReply(_("Always for you ;)"))
            $ contact_Amber.newMessage(_("That's what I was hoping to hear"))
            $ contact_Amber.addReply(_("I can be even more up if you want..."))
            $ contact_Amber.newMessage(_("Really? Just like that?"))
            $ contact_Amber.addReply(_("What can I say? You're hot"))
            $ contact_Amber.newMessage(_("You're pretty hot yourself and I'm... thinking about things"))
            $ contact_Amber.addReply(_("What kind of things? Same things I'm thinking? ;)"))
            $ contact_Amber.newMessage(_("I think so"))
            $ contact_Amber.addReply(_("Wanna see what thinking about you has done to me?"), v8s19_reply1)
            $ contact_Amber.addReply(_("I look at your pic all the time...when I'm thinking about things"), v8s19_reply2)

        else:
            # -MC's phone buzzes-
            $ contact_Lauren.newMessage(_("Hey, Sweetie, what are you up to?"), queue=False)
            $ contact_Lauren.addReply(_("Nothing, just catching up on some homework. You having a good night?"))
            $ contact_Lauren.newMessage(_("It would be better if you were here..."))
            $ contact_Lauren.addReply(_("Really?"))
            $ contact_Lauren.newMessage(_("I could use some snuggles."))
            $ contact_Lauren.addReply(_("Aww, I'd love to get some snuggles. When can I see you again?"))
            $ contact_Lauren.newMessage(_("I have a big test coming up but after that? I miss you"))
            $ contact_Lauren.addReply(_("I miss you too. It's a date. Just let me know"))
            $ contact_Lauren.newMessage(_("Goodnight"))
            $ contact_Lauren.addReply(_("Goodnight"))

        call screen phone

        if forgiveemily:
            # -MC's phone buzzes-
            ### ERROR: (Aww, she couldn't get enough of me) [I figure this line works for either scenario but let me know if I should change it] ###
            $ contact_Emily.newMessage(_("Hey, I was thinking"), queue=False)
            $ contact_Emily.addReply(_("Uh oh that can't be good ;)"))
            $ contact_Emily.newMessage(_("Wanna meet up at the arcade?"))

            if hcGirl == "emily":
                $ contact_Emily.newMessage(_("I feel so bad about homecoming and want to make it up to you. My treat!"))
            $ contact_Emily.addReply(_("Sure! Sounds like fun. I can be there in a few minutes"), v8s19_reply3)
            $ contact_Emily.addReply(_("I would but it's getting late and I haven't even started Mr. Lee's project"), v8s19_reply4)

            label v8s19_phoneCheck1:
                if contact_Emily.replies:
                    call screen phone
                if contact_Emily.replies:
                    u "I should reply to Emily"
                    jump v8s19_phoneCheck1

            if contact_Emily.get_message("Great! See you there!"):
                jump emily_arcade

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
            $ contact_Amber.newMessage(_("Hey u up?"), queue=False)
            $ contact_Amber.addReply(_("Always for you ;)"))
            $ contact_Amber.newMessage(_("That's what I was hoping to hear"))
            $ contact_Amber.addReply(_("I can be even more up if you want..."))
            $ contact_Amber.newMessage(_("Really? Just like that?"))
            $ contact_Amber.addReply(_("What can I say? You're hot"))
            $ contact_Amber.newMessage(_("You're pretty hot yourself and I'm... thinking about things"))
            $ contact_Amber.addReply(_("What kind of things? Same things I'm thinking? ;)"))
            $ contact_Amber.newMessage(_("I think so"))
            $ contact_Amber.addReply(_("Wanna see what thinking about you has done to me?"), v8s19_reply1)
            $ contact_Amber.addReply(_("I look at your pic all the time...when I'm thinking about things"), v8s19_reply2)

        else:
            # -MC's phone buzzes-
            $ contact_Lauren.newMessage(_("Hey, Sweetie, what are you up to?"), queue=False)
            $ contact_Lauren.addReply(_("Nothing, just catching up on some homework. You having a good night?"))
            $ contact_Lauren.newMessage(_("It would be better if you were here..."))
            $ contact_Lauren.addReply(_("Really?"))
            $ contact_Lauren.newMessage(_("I could use some snuggles."))
            $ contact_Lauren.addReply(_("Aww, I'd love to get some snuggles. When can I see you again?"))
            $ contact_Lauren.newMessage(_("I have a big test coming up but after that? I miss you"))
            $ contact_Lauren.addReply(_("I miss you too. It's a date. Just let me know"))
            $ contact_Lauren.newMessage(_("Goodnight"))
            $ contact_Lauren.addReply(_("Goodnight"))

        call screen phone
            
        if forgiveemily:
            # -MC's phone buzzes-
            ### ERROR: (Aww, she couldn't get enough of me) [I figure this line works for either scenario but let me know if I should change it] ###
            $ contact_Emily.newMessage(_("Hey, I was thinking"), queue=False)
            $ contact_Emily.addReply(_("Uh oh that can't be good ;)"))
            $ contact_Emily.newMessage(_("Wanna meet up at the arcade?"))

            if hcGirl == "emily":
                $ contact_Emily.newMessage(_("I feel so bad about homecoming and want to make it up to you. My treat!"))
            $ contact_Emily.addReply(_("Sure! Sounds like fun. I can be there in a few minutes"), v8s19_reply3)
            $ contact_Emily.addReply(_("I would but it's getting late and I haven't even started Mr. Lee's project"), v8s19_reply4)

            label v8s19_phoneCheck2:
                if contact_Emily.replies:
                    call screen phone
                if contact_Emily.replies:
                    u "I should reply to Emily"
                    jump v8s19_phoneCheck2

            if contact_Emily.get_message("Great! See you there!"):
                jump emily_arcade

            scene v8sser4a # TPP. Same camera as v8sser4, show MC lying on his side as if to go to sleep.
            with dissolve

            u "(I think I'll get an early night)"

        else:
            scene v8sser4a
            with dissolve

            u "(I think I'll get an early night)"

        jump mon_morning_room