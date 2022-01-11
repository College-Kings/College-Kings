# Sun Evening in Room
# Location: MC Wolves Room, MC Apes Room
# Outfits: MC Outfit 2
# Time: Sunday Evening

init python:
    def v8s19_reply1():

        grant_achievement("text_with_an_s")

        amber.messenger.newMessage(_("It's only fair, right? Make us even"))
        if config_censored:
            amber.messenger.addImgReply("gui/censoredPopup/censoredBackground.webp")

        elif joinwolves:
            amber.messenger.addImgReply("images/v8/Scene 19/w_dick_pic.webp")

        else:
            amber.messenger.addImgReply("images/v8/Scene 19/a_dick_pic.webp")

        amber.messenger.newMessage(_("Wow, better than I thought"))
        amber.messenger.addReply(_("So you thought about it?"))
        amber.messenger.newMessage(_("Maybe"))
        amber.messenger.addReply(_("Aw man you're driving me crazy"))
        amber.messenger.newMessage(_("So do something about it"))
        amber.messenger.addReply(_("Now? What about you?"))
        
        if config_censored:
            amber.messenger.newImgMessage("gui/censoredPopup/censoredBackground.webp")

        else:
            amber.messenger.newImgMessage("images/v8/Scene 19/amb_pussy_pic.webp")

        amber.messenger.addReply(_("Aw fuck"))
        amber.messenger.newMessage(_("You like?"))
        amber.messenger.addReply(_("I love! You're so hot!"))
        amber.messenger.newMessage(_("What would you do if you were here?"))
        amber.messenger.addReply(_("I would eat you until you couldn't take it anymore"))
        amber.messenger.newMessage(_("And then what?"))
        amber.messenger.addReply(_("I'd fuck you so good you'd scream my name"))
        amber.messenger.newMessage(_("I'm close. Will you finish with me?"))
        amber.messenger.addReply(_("Oh, God yes!"))
        amber.messenger.newMessage(_("NOW!"))
        amber.messenger.addReply(_("NOW!"))
        amber.messenger.newMessage("")
        amber.messenger.addReply(_("Holy shit, Amber! You're amazing!"))
        amber.messenger.newMessage(_("You weren't too bad yourself. Next time we need to do this in person"))
        amber.messenger.addReply(_("Give me 5 minutes ;)"))
        amber.messenger.newMessage(_("You're so cute! But it's time for bed. Dream about me ;)"))
        amber.messenger.addReply(_("With pleasure! Night!"))

    def v8s19_reply2():
        amber.messenger.newMessage(_("Good. Maybe someday we can think about things in the same room and see what happens"))
        amber.messenger.addReply(_("Please do"))
        amber.messenger.newMessage(_("I guess I better get back to studying. I keep getting distracted"))
        amber.messenger.addReply(_("I'm not gonna be able to think of anything else now. I'm done studying"))
        amber.messenger.newMessage(_("Well, sleep tight then ;)"))

    def v8s19_reply3():
        emily.messenger.newMessage(_("Great! See you there!"))

    def v8s19_reply4():
        emily.messenger.newMessage(_("You sure you're not mad?"))
        emily.messenger.addReply(_("No, not at all. Just beat. I'd love to go some other time"))
        emily.messenger.newMessage(_("Okay talk to you soon"))
        emily.messenger.addReply(_("Goodnight"))


label sun_eve_room:
    if joinwolves:
        scene v8sser1 # TPP. Show MC lying on his Wolves bed on his phone.
        with fade

        if lauren.relationship >= Relationship.GIRLFRIEND:
            # -MC's phone buzzes-
            $ lauren.messenger.newMessage(_("Hey, Sweetie, what are you up to?"), force_send=True)
            $ lauren.messenger.addReply(_("Nothing, just catching up on some homework. You having a good night?"))
            $ lauren.messenger.newMessage(_("It would be better if you were here..."))
            $ lauren.messenger.addReply(_("Really?"))
            $ lauren.messenger.newMessage(_("I could use some snuggles."))
            $ lauren.messenger.addReply(_("Aww, I'd love to get some snuggles. When can I see you again?"))
            $ lauren.messenger.newMessage(_("I have a big test coming up but after that? I miss you"))
            $ lauren.messenger.addReply(_("I miss you too. It's a date. Just let me know"))
            $ lauren.messenger.newMessage(_("Goodnight"))
            $ lauren.messenger.addReply(_("Goodnight"))

        else:
            play sound "sounds/vibrate.mp3"
            $ amber.messenger.newMessage(_("Hey u up?"), force_send=True)
            $ amber.messenger.addReply(_("Always for you ;)"))
            $ amber.messenger.newMessage(_("That's what I was hoping to hear"))
            $ amber.messenger.addReply(_("I can be even more up if you want..."))
            $ amber.messenger.newMessage(_("Really? Just like that?"))
            $ amber.messenger.addReply(_("What can I say? You're hot"))
            $ amber.messenger.newMessage(_("You're pretty hot yourself and I'm... thinking about things"))
            $ amber.messenger.addReply(_("What kind of things? Same things I'm thinking? ;)"))
            $ amber.messenger.newMessage(_("I think so"))
            $ amber.messenger.addReply(_("Wanna see what thinking about you has done to me?"), v8s19_reply1)
            $ amber.messenger.addReply(_("I look at your pic all the time...when I'm thinking about things"), v8s19_reply2)

        call screen phone

        if forgiveemily:
            # -MC's phone buzzes-
            ### ERROR: (Aww, she couldn't get enough of me) [I figure this line works for either scenario but let me know if I should change it] ###
            $ emily.messenger.newMessage(_("Hey, I was thinking"), force_send=True)
            $ emily.messenger.addReply(_("Uh oh that can't be good ;)"))
            $ emily.messenger.newMessage(_("Wanna meet up at the arcade?"))

            if hcGirl == "emily":
                $ emily.messenger.newMessage(_("I feel so bad about homecoming and want to make it up to you. My treat!"))
            $ emily.messenger.addReply(_("Sure! Sounds like fun. I can be there in a few minutes"), v8s19_reply3)
            $ emily.messenger.addReply(_("I would but it's getting late and I haven't even started Mr. Lee's project"), v8s19_reply4)

            label v8s19_phoneCheck1:
                if emily.messenger.replies:
                    call screen phone
                if emily.messenger.replies:
                    u "I should reply to Emily"
                    jump v8s19_phoneCheck1

            if emily.messenger.find_message("Great! See you there!"):
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

        if lauren.relationship >= Relationship.GIRLFRIEND:
            # -MC's phone buzzes-
            $ lauren.messenger.newMessage(_("Hey, Sweetie, what are you up to?"), force_send=True)
            $ lauren.messenger.addReply(_("Nothing, just catching up on some homework. You having a good night?"))
            $ lauren.messenger.newMessage(_("It would be better if you were here..."))
            $ lauren.messenger.addReply(_("Really?"))
            $ lauren.messenger.newMessage(_("I could use some snuggles."))
            $ lauren.messenger.addReply(_("Aww, I'd love to get some snuggles. When can I see you again?"))
            $ lauren.messenger.newMessage(_("I have a big test coming up but after that? I miss you"))
            $ lauren.messenger.addReply(_("I miss you too. It's a date. Just let me know"))
            $ lauren.messenger.newMessage(_("Goodnight"))
            $ lauren.messenger.addReply(_("Goodnight"))

        else:
            play sound "sounds/vibrate.mp3"
            $ amber.messenger.newMessage(_("Hey u up?"), force_send=True)
            $ amber.messenger.addReply(_("Always for you ;)"))
            $ amber.messenger.newMessage(_("That's what I was hoping to hear"))
            $ amber.messenger.addReply(_("I can be even more up if you want..."))
            $ amber.messenger.newMessage(_("Really? Just like that?"))
            $ amber.messenger.addReply(_("What can I say? You're hot"))
            $ amber.messenger.newMessage(_("You're pretty hot yourself and I'm... thinking about things"))
            $ amber.messenger.addReply(_("What kind of things? Same things I'm thinking? ;)"))
            $ amber.messenger.newMessage(_("I think so"))
            $ amber.messenger.addReply(_("Wanna see what thinking about you has done to me?"), v8s19_reply1)
            $ amber.messenger.addReply(_("I look at your pic all the time...when I'm thinking about things"), v8s19_reply2)

        call screen phone
            
        if forgiveemily:
            # -MC's phone buzzes-
            ### ERROR: (Aww, she couldn't get enough of me) [I figure this line works for either scenario but let me know if I should change it] ###
            $ emily.messenger.newMessage(_("Hey, I was thinking"), force_send=True)
            $ emily.messenger.addReply(_("Uh oh that can't be good ;)"))
            $ emily.messenger.newMessage(_("Wanna meet up at the arcade?"))

            if hcGirl == "emily":
                $ emily.messenger.newMessage(_("I feel so bad about homecoming and want to make it up to you. My treat!"))
            $ emily.messenger.addReply(_("Sure! Sounds like fun. I can be there in a few minutes"), v8s19_reply3)
            $ emily.messenger.addReply(_("I would but it's getting late and I haven't even started Mr. Lee's project"), v8s19_reply4)

            label v8s19_phoneCheck2:
                if emily.messenger.replies:
                    call screen phone
                if emily.messenger.replies:
                    u "I should reply to Emily"
                    jump v8s19_phoneCheck2

            if emily.messenger.find_message("Great! See you there!"):
                jump emily_arcade

            scene v8sser4a # TPP. Same camera as v8sser4, show MC lying on his side as if to go to sleep.
            with dissolve

            u "(I think I'll get an early night)"

        else:
            scene v8sser4a
            with dissolve

            u "(I think I'll get an early night)"

        jump mon_morning_room