# SCENE 35: Your Room Sat Afternoon
# Locations: MC Wolves/Apes room
# Characters: MC (Outfit 3)
# Time: Saturday Morning

label v9_room_sat_aft:

    python:
        v9s35_reply8 = MessageBuilder(chloe)
        v9s35_reply8.new_message(_("Ugh. I'm so tired of studying."))
        v9s35_reply8.add_reply(_("Haha, me too. Kinda want to throw my books out the window."))
        v9s35_reply8.new_message(_("Haha. I wish I could just leave the house and not worry about it."))
        v9s35_reply8.add_reply(_("Me too. Wanna go for a walk together?"))
        v9s35_reply8.new_message(_("I wish. I have a lot to do for tomorrow, but that would be nice."))
        v9s35_reply8.add_reply(_("Yeah, it would be."))
        v9s35_reply8.new_message(_("I think I'll soak in the tub for a bit."))
        v9s35_reply8.add_reply(_("Can I join you?"))
        v9s35_reply8.new_message(_("Haha! You wish :)"))
        v9s35_reply8.add_reply(_("Hey, a guy can dream, right?"))
        v9s35_reply8.new_message(_("Yeah, but it's a dream."))
        v9s35_reply8.add_reply(_("For now haha."))
        v9s35_reply8.new_message(_("Haha, yeah for now. Well, I'll let you go. Was great to talk to you [name]."))
        v9s35_reply8.add_replies(
            Reply(_("Likewise. Don't be a stranger.")),
            Reply(_("Yeah, it was nice to hear from you."))
        )
        v9s35_reply8.new_message(_("Goodnight [name]"))
        v9s35_reply8.add_reply(_("Goodnight Chloe."))

        v9s35_reply7 = MessageBuilder(chloe)
        v9s35_reply7.add_function(reputation.add_point, RepComponent.BOYFRIEND)

        v9s35_reply5a = MessageBuilder(chloe)
        v9s35_reply5a.new_message(_("Thought you'd like that :)"))
        v9s35_reply5a.add_reply(_("Like? I love it! That just made my whole day better."))
        v9s35_reply5a.new_message(_("Awww, such a charmer haha. Your turn. Let me see yours."))
        v9s35_reply5a.add_reply(_("Your wish is my command."))
        v9s35_reply5a.add_reply("images/v9/Scene 35/mcdickwolves.webp")
        v9s35_reply5a.new_message(_("God, I miss that cock."))
        v9s35_reply5a.add_reply(_("Can I come over? Haha."))
        v9s35_reply5a.new_message(_("I wish. I have a lot to do for tomorrow, but that would be nice."))
        v9s35_reply5a.add_reply(_("Yeah, that would be great. Would like to see more of you."))
        v9s35_reply5a.new_message(_("No, that's all the pics I'm sending haha."))
        v9s35_reply5a.add_reply(_("That's not what I meant, haha."))
        v9s35_reply5a.new_message(_("Haha, I know what you meant. I'd like that, too."))
        v9s35_reply5a.add_reply(_("Well, let me know when you're free and I'll make time."))
        v9s35_reply5a.new_message(_("I definitely will. Goodnight [name]"))
        v9s35_reply5a.add_replies(
            Reply(_("Goodnight, gorgeous."), v9s35_reply7),
            Reply(_("Goodnight, Chloe."))
        )

        v9s35_reply4 = MessageBuilder(chloe)
        v9s35_reply4.add_function(reputation.add_point, RepComponent.BOYFRIEND)
        v9s35_reply4.new_message("images/v9/Scene 35/chloetxtimg.webp")
        v9s35_reply4.add_replies(
            Reply(_("OMG! I miss those!"), v9s35_reply5a),
            Reply(_("OMG! You are magnificent!"), v9s35_reply5a)
        )

        v9s35_reply5 = MessageBuilder(chloe)
        v9s35_reply5.new_message("images/v9/Scene 35/chloetxtimg.webp")
        v9s35_reply5.add_replies(
            Reply(_("OMG! I miss those!"), v9s35_reply5a),
            Reply(_("OMG! You are magnificent!"), v9s35_reply5a)
        )

        v9s35_reply2 = MessageBuilder(chloe)
        v9s35_reply2.add_function(reputation.add_point, RepComponent.BOYFRIEND)
        v9s35_reply2.new_message(_("Wanna see what I'm doing now?"))
        v9s35_reply2.add_replies(
            Reply(_("Yeah, of course"), v9s35_reply4),
            Reply(_("You need to ask? :)"), v9s35_reply5)
        )

        v9s35_reply3 = MessageBuilder(chloe)
        v9s35_reply3.new_message(_("Wanna see what I'm doing now?"))
        v9s35_reply3.add_replies(
            Reply(_("Yeah, of course"), v9s35_reply4),
            Reply(_("You need to ask? :)"), v9s35_reply5)
        )

        v9s35_reply1 = MessageBuilder(chloe)
        v9s35_reply1.new_message(_("I was thinking about you and I kind of miss you."))
        v9s35_reply1.add_reply(_("Kinda? That's it? ;)"))
        v9s35_reply1.new_message(_("Maybe haha. Ok, yeah, I miss you."))
        v9s35_reply1.add_replies(
            Reply(_("I miss you too."), v9s35_reply2),
            Reply(_("That's better haha"), v9s35_reply3)
        )

    if joinwolves:
        scene v9rsa1 # TPP. Show MC stood in his Wolves room near his bed.
        with fade

        pause 1

        scene v9rsa2 # TPP. Show MC flopped facedown on his bed.
        with dissolve

        u "(How much longer do I have?)"

        if not CharacterService.is_mad(chloe):
            scene v9rsa3 # TPP. Show MC now on his back on his bed, looking at his phone (don't show phone screen)
            with dissolve
            
            $ MessengerService.new_message(chloe, _("Hey [name], what you up to?"))
            $ MessengerService.add_reply(chloe, _("Nothing much. Just relaxing. I'm kind of tired."))
            $ MessengerService.new_message(chloe, _("Awwww. Long day?"))
            if CharacterService.is_fwb(chloe):
                $ MessengerService.add_replies(chloe, Reply(_("Yeah haha, I feel wiped."), v9s35_reply1))
            else:
                $ MessengerService.add_replies(chloe, Reply(_("Yeah haha, I feel wiped."), v9s35_reply8))
        
            play sound sound.vibrate

            u "(I wonder who this is.)"

            while MessengerService.has_replies(chloe):
                call screen phone
                if MessengerService.has_replies(chloe):
                    u "(I should reply to Chloe.)"

            scene v9rsa3a # TPP. Same camera as v9rsa3, MC puts his phone down and yawns.
            with dissolve

        u "(Just a quick nap.)"

        scene v9rsa4 # TPP. Show MC's Wolves room door.
        with dissolve

        play sound sound.knock

        u "Ugh!"

        jump v9_run_w_imre

    else:
        scene v9rsa5 # TPP. Show MC stood in his Apes room near his bed.
        with fade

        pause 1

        scene v9rsa6 # TPP. Show MC flopped facedown on his bed.
        with dissolve

        u "(How much longer do I have?)"

        if not CharacterService.is_mad(chloe):
            scene v9rsa7 # TPP. Show MC now on his back on his bed, looking at his phone (don't show phone screen)
            with dissolve
            
            play sound sound.vibrate

            u "(I wonder who this is.)"

            $ MessengerService.new_message(chloe, _("Hey [name], what you up to?"))
            $ MessengerService.add_reply(chloe, _("Nothing much. Just relaxing. I'm kind of tired."))
            $ MessengerService.new_message(chloe, _("Awwww. Long day?"))
            if CharacterService.is_fwb(chloe):
                $ MessengerService.add_replies(chloe, Reply(_("Yeah haha, I feel wiped."), v9s35_reply1))
            else:
                $ MessengerService.add_replies(chloe, Reply(_("Yeah haha, I feel wiped."), v9s35_reply8))
        
            play sound sound.vibrate

            u "(I wonder who this is.)"

            while MessengerService.has_replies(chloe):
                call screen phone
                if MessengerService.has_replies(chloe):
                    u "(I should reply to Chloe.)"

            scene v9rsa7a # TPP. Same camera as v9rsa3, MC puts his phone down and yawns.
            with dissolve

        u "(Just a quick nap.)"

        scene v9rsa8 # TPP. Show MC's Apes room door.
        with dissolve

        play sound sound.knock

        u "Ugh!"

        jump v9_run_w_ryan