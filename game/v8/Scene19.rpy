# Sun Evening in Room
# Location: MC Wolves Room, MC Apes Room
# Outfits: MC Outfit 2
# Time: Sunday Evening
label sun_eve_room:
    python:
        v8s19_reply1 = MessageBuilder(amber)
        v8s19_reply1.add_function(text_with_an_s.grant)
        v8s19_reply1.new_message(_("It's only fair, right? Make us even"))

        if is_censored:
            v8s19_reply1.add_reply("gui/censoredPopup/censoredBackground.webp")
        elif mc.frat == Frat.WOLVES:
            v8s19_reply1.add_reply("images/v8/Scene 19/w_dick_pic.webp")
        else:
            v8s19_reply1.add_reply("images/v8/Scene 19/a_dick_pic.webp")

        v8s19_reply1.new_message(_("Wow, better than I thought"))
        v8s19_reply1.add_reply(_("So you thought about it?"))
        v8s19_reply1.new_message(_("Maybe"))
        v8s19_reply1.add_reply(_("Aw man you're driving me crazy"))
        v8s19_reply1.new_message(_("So do something about it"))
        v8s19_reply1.add_reply(_("Now? What about you?"))

        if is_censored:
            v8s19_reply1.new_message("gui/censoredPopup/censoredBackground.webp")
        else:
            v8s19_reply1.new_message("images/v8/Scene 19/amb_pussy_pic.webp")

        v8s19_reply1.add_reply(_("Aw fuck"))
        v8s19_reply1.new_message(_("You like?"))
        v8s19_reply1.add_reply(_("I love! You're so hot!"))
        v8s19_reply1.new_message(_("What would you do if you were here?"))
        v8s19_reply1.add_reply(_("I would eat you until you couldn't take it anymore"))
        v8s19_reply1.new_message(_("And then what?"))
        v8s19_reply1.add_reply(_("I'd fuck you so good you'd scream my name"))
        v8s19_reply1.new_message(_("I'm close. Will you finish with me?"))
        v8s19_reply1.add_reply(_("Oh, God yes!"))
        v8s19_reply1.new_message(_("NOW!"))
        v8s19_reply1.add_reply(_("NOW!"))
        v8s19_reply1.add_reply(_("Holy shit, Amber! You're amazing!"))
        v8s19_reply1.new_message(_("You weren't too bad yourself. Next time we need to do this in person"))
        v8s19_reply1.add_reply(_("Give me 5 minutes ;)"))
        v8s19_reply1.new_message(_("You're so cute! But it's time for bed. Dream about me ;)"))
        v8s19_reply1.add_reply(_("With pleasure! Night!"))

        v8s19_reply2 = MessageBuilder(amber)
        v8s19_reply2.new_message(_("Good. Maybe someday we can think about things in the same room and see what happens"))
        v8s19_reply2.add_reply(_("Please do"))
        v8s19_reply2.new_message(_("I guess I better get back to studying. I keep getting distracted"))
        v8s19_reply2.add_reply(_("I'm not gonna be able to think of anything else now. I'm done studying"))
        v8s19_reply2.new_message(_("Well, sleep tight then ;)"))

        v8s19_reply3 = MessageBuilder(emily)
        v8s19_reply3.new_message(_("Great! See you there!"))

        v8s19_reply4 = MessageBuilder(emily)
        v8s19_reply4.new_message(_("You sure you're not mad?"))
        v8s19_reply4.add_reply(_("No, not at all. Just beat. I'd love to go some other time"))
        v8s19_reply4.new_message(_("Okay talk to you soon"))
        v8s19_reply4.add_reply(_("Goodnight"))

    if mc.frat == Frat.WOLVES:
        scene v8sser1 # TPP. Show MC lying on his Wolves bed on his phone.
        with fade

        if CharacterService.is_girlfriend(lauren):
            # -MC's phone buzzes-
            $ MessengerService.new_message(lauren, _("Hey, Sweetie, what are you up to?"))
            $ MessengerService.add_reply(lauren, _("Nothing, just catching up on some homework. You having a good night?"))
            $ MessengerService.new_message(lauren, _("It would be better if you were here..."))
            $ MessengerService.add_reply(lauren, _("Really?"))
            $ MessengerService.new_message(lauren, _("I could use some snuggles."))
            $ MessengerService.add_reply(lauren, _("Aww, I'd love to get some snuggles. When can I see you again?"))
            $ MessengerService.new_message(lauren, _("I have a big test coming up but after that? I miss you"))
            $ MessengerService.add_reply(lauren, _("I miss you too. It's a date. Just let me know"))
            $ MessengerService.new_message(lauren, _("Goodnight"))
            $ MessengerService.add_reply(lauren, _("Goodnight"))

        elif CharacterService.is_fwb(amber):
            play sound sound.vibrate

            python:
                MessengerService.new_message(amber, _("Hey u up?"))
                MessengerService.add_reply(amber, _("Always for you ;)"))
                MessengerService.new_message(amber, _("That's what I was hoping to hear"))
                MessengerService.add_reply(amber, _("I can be even more up if you want..."))
                MessengerService.new_message(amber, _("Really? Just like that?"))
                MessengerService.add_reply(amber, _("What can I say? You're hot"))
                MessengerService.new_message(amber, _("You're pretty hot yourself and I'm... thinking about things"))
                MessengerService.add_reply(amber, _("What kind of things? Same things I'm thinking? ;)"))
                MessengerService.new_message(amber, _("I think so"))
                MessengerService.add_replies(amber,
                    Reply(_("Wanna see what thinking about you has done to me?"), v8s19_reply1),
                    Reply(_("I look at your pic all the time...when I'm thinking about things"), v8s19_reply2)
                )

        if forgiveemily:
            # -MC's phone buzzes-
            ### ERROR: (Aww, she couldn't get enough of me) [I figure this line works for either scenario but let me know if I should change it] ###
            $ MessengerService.new_message(emily, _("Hey, I was thinking"))
            $ MessengerService.add_reply(emily, _("Uh oh that can't be good ;)"))
            $ MessengerService.new_message(emily, _("Wanna meet up at the arcade?"))

            if hcGirl == "emily":
                $ MessengerService.new_message(emily, _("I feel so bad about homecoming and want to make it up to you. My treat!"))
            $ MessengerService.add_replies(emily,
                Reply(_("Sure! Sounds like fun. I can be there in a few minutes"), v8s19_reply3),
                Reply(_("I would but it's getting late and I haven't even started Mr. Lee's project"), v8s19_reply4)
            )

            while MessengerService.has_replies(emily):
                call screen phone
                if MessengerService.has_replies(emily):
                    u "I should reply to Emily"

            if MessengerService.find_message(emily, "Great! See you there!"):
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

        if CharacterService.is_girlfriend(lauren):
            # -MC's phone buzzes-
            $ MessengerService.new_message(lauren, _("Hey, Sweetie, what are you up to?"))
            $ MessengerService.add_reply(lauren, _("Nothing, just catching up on some homework. You having a good night?"))
            $ MessengerService.new_message(lauren, _("It would be better if you were here..."))
            $ MessengerService.add_reply(lauren, _("Really?"))
            $ MessengerService.new_message(lauren, _("I could use some snuggles."))
            $ MessengerService.add_reply(lauren, _("Aww, I'd love to get some snuggles. When can I see you again?"))
            $ MessengerService.new_message(lauren, _("I have a big test coming up but after that? I miss you"))
            $ MessengerService.add_reply(lauren, _("I miss you too. It's a date. Just let me know"))
            $ MessengerService.new_message(lauren, _("Goodnight"))
            $ MessengerService.add_reply(lauren, _("Goodnight"))

        elif CharacterService.is_fwb(amber):
            play sound sound.vibrate

            python:
                MessengerService.new_message(amber, _("Hey u up?"))
                MessengerService.add_reply(amber, _("Always for you ;)"))
                MessengerService.new_message(amber, _("That's what I was hoping to hear"))
                MessengerService.add_reply(amber, _("I can be even more up if you want..."))
                MessengerService.new_message(amber, _("Really? Just like that?"))
                MessengerService.add_reply(amber, _("What can I say? You're hot"))
                MessengerService.new_message(amber, _("You're pretty hot yourself and I'm... thinking about things"))
                MessengerService.add_reply(amber, _("What kind of things? Same things I'm thinking? ;)"))
                MessengerService.new_message(amber, _("I think so"))
                MessengerService.add_replies(amber,
                    Reply(_("Wanna see what thinking about you has done to me?"), v8s19_reply1),
                    Reply(_("I look at your pic all the time...when I'm thinking about things"), v8s19_reply2)
                )
                
        if forgiveemily:
            # -MC's phone buzzes-
            ### ERROR: (Aww, she couldn't get enough of me) [I figure this line works for either scenario but let me know if I should change it] ###
            $ MessengerService.new_message(emily, _("Hey, I was thinking"))
            $ MessengerService.add_reply(emily, _("Uh oh that can't be good ;)"))
            $ MessengerService.new_message(emily, _("Wanna meet up at the arcade?"))

            if hcGirl == "emily":
                $ MessengerService.new_message(emily, _("I feel so bad about homecoming and want to make it up to you. My treat!"))
            $ MessengerService.add_replies(emily,
                Reply(_("Sure! Sounds like fun. I can be there in a few minutes"), v8s19_reply3),
                Reply(_("I would but it's getting late and I haven't even started Mr. Lee's project"), v8s19_reply4)
            )

            while MessengerService.has_replies(emily):
                call screen phone
                if MessengerService.has_replies(emily):
                    u "I should reply to Emily"

            if MessengerService.find_message(emily, "Great! See you there!"):
                jump emily_arcade

            scene v8sser4a # TPP. Same camera as v8sser4, show MC lying on his side as if to go to sleep.
            with dissolve

            u "(I think I'll get an early night)"

        else:
            scene v8sser4a
            with dissolve

            u "(I think I'll get an early night)"

        jump mon_morning_room
