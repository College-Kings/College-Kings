# SCENE 35: Your Room Sat Afternoon
# Locations: MC Wolves/Apes room
# Characters: MC (Outfit 3)
# Time: Saturday Morning

label v9_room_sat_aft:
    $ v9s35_reply_boyfriend = MessageBuilder(chloe).add_function(reputation.add_point, RepComponent.BOYFRIEND)
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
                $ MessengerService.add_reply(chloe, _("Yeah haha, I feel wiped."))
                $ MessengerService.new_message(chloe, _("I was thinking about you and I kind of miss you."))
                $ MessengerService.add_reply(chloe, _("Kinda? That's it? ;)"))
                $ MessengerService.new_message(chloe, _("Maybe haha. Ok, yeah, I miss you."))
                $ MessengerService.add_replies(chloe,
                    Reply(_("I miss you too."), v9s35_reply_boyfriend),
                    Reply(_("That's better haha"))
                )
                $ MessengerService.new_message(chloe, _("Wanna see what I'm doing now?"))
                $ MessengerService.add_replies(chloe,
                    Reply(_("Yeah, of course"), v9s35_reply_boyfriend),
                    Reply(_("You need to ask? :)"))
                )
                $ MessengerService.new_message(chloe, "images/v9/Scene 35/chloetxtimg.webp")
                $ MessengerService.add_replies(chloe,
                    Reply(_("OMG! I miss those!")),
                    Reply(_("OMG! You are magnificent!"))
                )
                $ MessengerService.new_message(chloe, _("Thought you'd like that :)"))
                $ MessengerService.add_reply(chloe, _("Like? I love it! That just made my whole day better."))
                $ MessengerService.new_message(chloe, _("Awww, such a charmer haha. Your turn. Let me see yours."))
                $ MessengerService.add_reply(chloe, _("Your wish is my command."))
                $ MessengerService.add_reply(chloe, "images/v9/Scene 35/mcdickwolves.webp")
                $ MessengerService.new_message(chloe, _("God, I miss that cock."))
                $ MessengerService.add_reply(chloe, _("Can I come over? Haha."))
                $ MessengerService.new_message(chloe, _("I wish. I have a lot to do for tomorrow, but that would be nice."))
                $ MessengerService.add_reply(chloe, _("Yeah, that would be great. Would like to see more of you."))
                $ MessengerService.new_message(chloe, _("No, that's all the pics I'm sending haha."))
                $ MessengerService.add_reply(chloe, _("That's not what I meant, haha."))
                $ MessengerService.new_message(chloe, _("Haha, I know what you meant. I'd like that, too."))
                $ MessengerService.add_reply(chloe, _("Well, let me know when you're free and I'll make time."))
                $ MessengerService.new_message(chloe, _("I definitely will. Goodnight [name]"))
                $ MessengerService.add_replies(chloe,
                    Reply(_("Goodnight, gorgeous."), v9s35_reply_boyfriend),
                    Reply(_("Goodnight, Chloe."))
                )

            else:
                $ MessengerService.add_reply(chloe, _("Yeah haha, I feel wiped."))
                $ MessengerService.new_message(chloe, _("Ugh. I'm so tired of studying."))
                $ MessengerService.add_reply(chloe, _("Haha, me too. Kinda want to throw my books out the window."))
                $ MessengerService.new_message(chloe, _("Haha. I wish I could just leave the house and not worry about it."))
                $ MessengerService.add_reply(chloe, _("Me too. Wanna go for a walk together?"))
                $ MessengerService.new_message(chloe, _("I wish. I have a lot to do for tomorrow, but that would be nice."))
                $ MessengerService.add_reply(chloe, _("Yeah, it would be."))
                $ MessengerService.new_message(chloe, _("I think I'll soak in the tub for a bit."))
                $ MessengerService.add_reply(chloe, _("Can I join you?"))
                $ MessengerService.new_message(chloe, _("Haha! You wish :)"))
                $ MessengerService.add_reply(chloe, _("Hey, a guy can dream, right?"))
                $ MessengerService.new_message(chloe, _("Yeah, but it's a dream."))
                $ MessengerService.add_reply(chloe, _("For now haha."))
                $ MessengerService.new_message(chloe, _("Haha, yeah for now. Well, I'll let you go. Was great to talk to you [name]."))
                $ MessengerService.add_replies(chloe,
                    Reply(_("Likewise. Don't be a stranger.")),
                    Reply(_("Yeah, it was nice to hear from you."))
                )
                $ MessengerService.new_message(chloe, _("Goodnight [name]"))
                $ MessengerService.add_reply(chloe, _("Goodnight Chloe."))
        
            play sound "sounds/vibrate.mp3"

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

        play sound "sounds/knock.mp3"

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
            
            play sound "sounds/vibrate.mp3"

            u "(I wonder who this is.)"

            $ MessengerService.new_message(chloe, _("Hey [name], what you up to?"))
            $ MessengerService.add_reply(chloe, _("Nothing much. Just relaxing. I'm kind of tired."))
            $ MessengerService.new_message(chloe, _("Awwww. Long day?"))

            if CharacterService.is_fwb(chloe):
                $ MessengerService.add_reply(chloe, _("Yeah haha, I feel wiped."))
                $ MessengerService.new_message(chloe, _("I was thinking about you and I kind of miss you."))
                $ MessengerService.add_reply(chloe, _("Kinda? That's it? ;)"))
                $ MessengerService.new_message(chloe, _("Maybe haha. Ok, yeah, I miss you."))
                $ MessengerService.add_replies(chloe,
                    Reply(_("I miss you too."), v9s35_reply_boyfriend),
                    Reply(_("That's better haha"))
                )
                $ MessengerService.new_message(chloe, _("Wanna see what I'm doing now?"))
                $ MessengerService.add_replies(chloe,
                    Reply(_("Yeah, of course"), v9s35_reply_boyfriend),
                    Reply(_("You need to ask? :)"))
                )
                $ MessengerService.new_message(chloe, "images/v9/Scene 35/chloetxtimg.webp")
                $ MessengerService.add_replies(chloe,
                    Reply(_("OMG! I miss those!")),
                    Reply(_("OMG! You are magnificent!"))
                )
                $ MessengerService.new_message(chloe, _("Thought you'd like that :)"))
                $ MessengerService.add_reply(chloe, _("Like? I love it! That just made my whole day better."))
                $ MessengerService.new_message(chloe, _("Awww, such a charmer haha. Your turn. Let me see yours."))
                $ MessengerService.add_reply(chloe, _("Your wish is my command."))
                $ MessengerService.add_reply(chloe, "images/v9/Scene 35/mcdickwolves.webp")
                $ MessengerService.new_message(chloe, _("God, I miss that cock."))
                $ MessengerService.add_reply(chloe, _("Can I come over? Haha."))
                $ MessengerService.new_message(chloe, _("I wish. I have a lot to do for tomorrow, but that would be nice."))
                $ MessengerService.add_reply(chloe, _("Yeah, that would be great. Would like to see more of you."))
                $ MessengerService.new_message(chloe, _("No, that's all the pics I'm sending haha."))
                $ MessengerService.add_reply(chloe, _("That's not what I meant, haha."))
                $ MessengerService.new_message(chloe, _("Haha, I know what you meant. I'd like that, too."))
                $ MessengerService.add_reply(chloe, _("Well, let me know when you're free and I'll make time."))
                $ MessengerService.new_message(chloe, _("I definitely will. Goodnight [name]"))
                $ MessengerService.add_replies(chloe,
                    Reply(_("Goodnight, gorgeous."), v9s35_reply_boyfriend),
                    Reply(_("Goodnight, Chloe."))
                )
                
            else:
                $ MessengerService.add_reply(chloe, _("Yeah haha, I feel wiped."))
                $ MessengerService.new_message(chloe, _("Ugh. I'm so tired of studying."))
                $ MessengerService.add_reply(chloe, _("Haha, me too. Kinda want to throw my books out the window."))
                $ MessengerService.new_message(chloe, _("Haha. I wish I could just leave the house and not worry about it."))
                $ MessengerService.add_reply(chloe, _("Me too. Wanna go for a walk together?"))
                $ MessengerService.new_message(chloe, _("I wish. I have a lot to do for tomorrow, but that would be nice."))
                $ MessengerService.add_reply(chloe, _("Yeah, it would be."))
                $ MessengerService.new_message(chloe, _("I think I'll soak in the tub for a bit."))
                $ MessengerService.add_reply(chloe, _("Can I join you?"))
                $ MessengerService.new_message(chloe, _("Haha! You wish :)"))
                $ MessengerService.add_reply(chloe, _("Hey, a guy can dream, right?"))
                $ MessengerService.new_message(chloe, _("Yeah, but it's a dream."))
                $ MessengerService.add_reply(chloe, _("For now haha."))
                $ MessengerService.new_message(chloe, _("Haha, yeah for now. Well, I'll let you go. Was great to talk to you [name]."))
                $ MessengerService.add_replies(chloe,
                    Reply(_("Likewise. Don't be a stranger.")),
                    Reply(_("Yeah, it was nice to hear from you."))
                )
                $ MessengerService.new_message(chloe, _("Goodnight [name]"))
                $ MessengerService.add_reply(chloe, _("Goodnight Chloe."))

            while MessengerService.has_replies(chloe):
                call screen phone
                if MessengerService.has_replies(chloe):
                    u "(I should reply to Chloe.)"

            scene v9rsa7a # TPP. Same camera as v9rsa3, MC puts his phone down and yawns.
            with dissolve

        u "(Just a quick nap.)"

        scene v9rsa8 # TPP. Show MC's Apes room door.
        with dissolve

        play sound "sounds/knock.mp3"

        u "Ugh!"

        jump v9_run_w_ryan