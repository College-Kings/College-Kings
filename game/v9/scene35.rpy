# SCENE 35: Your Room Sat Afternoon
# Locations: MC Wolves/Apes room
# Characters: MC (Outfit 3)
# Time: Saturday Morning

init python:
    def v9s35_reply1():
        chloe.messenger.newMessage(_("I was thinking about you and I kind of miss you."))
        chloe.messenger.addReply(_("Kinda? That's it? ;)"))
        chloe.messenger.newMessage(_("Maybe haha. Ok, yeah, I miss you."))
        chloe.messenger.addReply(_("I miss you too."), v9s35_reply2)
        chloe.messenger.addReply(_("That's better haha"), v9s35_reply3)

    def v9s35_reply2():
        add_point(Reputations.BOYFRIEND)
        v9s35_reply3()

    def v9s35_reply3():
        chloe.messenger.newMessage(_("Wanna see what I'm doing now?"))
        chloe.messenger.addReply(_("Yeah, of course"), v9s35_reply4)
        chloe.messenger.addReply(_("You need to ask? :)"), v9s35_reply5)

    def v9s35_reply4():
        add_point(Reputations.BOYFRIEND)
        v9s35_reply5()

    def v9s35_reply5():
        chloe.messenger.newImgMessage("images/v9/Scene 35/chloetxtimg.webp")
        chloe.messenger.addReply(_("OMG! I miss those!"), v9s35_reply5a)
        chloe.messenger.addReply(_("OMG! You are magnificent!"), v9s35_reply5a)

    def v9s35_reply5a():
        chloe.messenger.newMessage(_("Thought you'd like that :)"))
        chloe.messenger.addReply(_("Like? I love it! That just made my whole day better."))
        chloe.messenger.newMessage(_("Awww, such a charmer haha. Your turn. Let me see yours."))
        chloe.messenger.addReply(_("Your wish is my command."))
        chloe.messenger.addImgReply("images/v9/Scene 35/mcdickwolves.webp", newMessage=True)
        chloe.messenger.newMessage(_("God, I miss that cock."))
        chloe.messenger.addReply(_("Can I come over? Haha."))
        chloe.messenger.newMessage(_("I wish. I have a lot to do for tomorrow, but that would be nice."))
        chloe.messenger.addReply(_("Yeah, that would be great. Would like to see more of you."))
        chloe.messenger.newMessage(_("No, that's all the pics I'm sending haha."))
        chloe.messenger.addReply(_("That's not what I meant, haha."))
        chloe.messenger.newMessage(_("Haha, I know what you meant. I'd like that, too."))
        chloe.messenger.addReply(_("Well, let me know when you're free and I'll make time."))
        chloe.messenger.newMessage(_("I definitely will. Goodnight [name]"))
        chloe.messenger.addReply(_("Goodnight, gorgeous."), v9s35_reply7)
        chloe.messenger.addReply(_("Goodnight, Chloe."))

    def v9s35_reply7():
        add_point(Reputations.BOYFRIEND)

    def v9s35_reply8():
        chloe.messenger.newMessage(_("Ugh. I'm so tired of studying."))
        chloe.messenger.addReply(_("Haha, me too. Kinda want to throw my books out the window."))
        chloe.messenger.newMessage(_("Haha. I wish I could just leave the house and not worry about it."))
        chloe.messenger.addReply(_("Me too. Wanna go for a walk together?"))
        chloe.messenger.newMessage(_("I wish. I have a lot to do for tomorrow, but that would be nice."))
        chloe.messenger.addReply(_("Yeah, it would be."))
        chloe.messenger.newMessage(_("I think I'll soak in the tub for a bit."))
        chloe.messenger.addReply(_("Can I join you?"))
        chloe.messenger.newMessage(_("Haha! You wish :)"))
        chloe.messenger.addReply(_("Hey, a guy can dream, right?"))
        chloe.messenger.newMessage(_("Yeah, but it's a dream."))
        chloe.messenger.addReply(_("For now haha."))
        chloe.messenger.newMessage(_("Haha, yeah for now. Well, I'll let you go. Was great to talk to you [name]."))
        chloe.messenger.addReply(_("Likewise. Don't be a stranger."))
        chloe.messenger.addReply(_("Yeah, it was nice to hear from you."))
        chloe.messenger.newMessage(_("Goodnight [name]"))
        chloe.messenger.addReply(_("Goodnight Chloe."))

label v9_room_sat_aft:
    if joinwolves:
        scene v9rsa1 # TPP. Show MC stood in his Wolves room near his bed.
        with fade

        pause 1

        scene v9rsa2 # TPP. Show MC flopped facedown on his bed.
        with dissolve

        u "(How much longer do I have?)"

        if chloe.relationship > Relationship.MAD:
            scene v9rsa3 # TPP. Show MC now on his back on his bed, looking at his phone (don't show phone screen)
            with dissolve
            
            $ chloe.messenger.newMessage(_("Hey [name], what you up to?"), force_send=True)
            $ chloe.messenger.addReply(_("Nothing much. Just relaxing. I'm kind of tired."))
            $ chloe.messenger.newMessage(_("Awwww. Long day?"))
            if chloe.relationship >= Relationship.FWB:
                $ chloe.messenger.addReply(_("Yeah haha, I feel wiped."), v9s35_reply1)
            else:
                $ chloe.messenger.addReply(_("Yeah haha, I feel wiped."), v9s35_reply8)
        
            play sound "sounds/vibrate.mp3"

            u "(I wonder who this is.)"

            label s35_PhoneContinueW:
                if chloe.messenger.replies:
                    call screen phone
                if chloe.messenger.replies:
                    u "(I should reply to Chloe.)"
                    jump s35_PhoneContinueW

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

        if chloe.relationship > Relationship.MAD:
            scene v9rsa7 # TPP. Show MC now on his back on his bed, looking at his phone (don't show phone screen)
            with dissolve
            
            play sound "sounds/vibrate.mp3"

            u "(I wonder who this is.)"

            $ chloe.messenger.newMessage(_("Hey [name], what you up to?"), force_send=True)
            $ chloe.messenger.addReply(_("Nothing much. Just relaxing. I'm kind of tired."))
            $ chloe.messenger.newMessage(_("Awwww. Long day?"))
            if chloe.relationship >= Relationship.FWB:
                $ chloe.messenger.addReply(_("Yeah haha, I feel wiped."), v9s35_reply1)
            else:
                $ chloe.messenger.addReply(_("Yeah haha, I feel wiped."), v9s35_reply8)

            label s35_PhoneContinueA:
                if chloe.messenger.replies:
                    call screen phone
                if chloe.messenger.replies:
                    u "(I should reply to Chloe.)"
                    jump s35_PhoneContinueA

            scene v9rsa7a # TPP. Same camera as v9rsa3, MC puts his phone down and yawns.
            with dissolve

        u "(Just a quick nap.)"

        scene v9rsa8 # TPP. Show MC's Apes room door.
        with dissolve

        play sound "sounds/knock.mp3"

        u "Ugh!"

        jump v9_run_w_ryan