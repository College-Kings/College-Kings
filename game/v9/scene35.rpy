# SCENE 35: Your Room Sat Afternoon
# Locations: MC Wolves/Apes room
# Characters: MC (Outfit 3)
# Time: Saturday Morning

init python:
    def v9s35_reply1():
        contact_Chloe.newMessage(_("I was thinking about you and I kind of miss you."))
        contact_Chloe.addReply(_("Kinda? That's it? ;)"))
        contact_Chloe.newMessage(_("Maybe haha. Ok, yeah, I miss you."))
        contact_Chloe.addReply(_("I miss you too."), v9s35_reply2)
        contact_Chloe.addReply(_("That's better haha"), v9s35_reply3)

    def v9s35_reply2():
        addPoint("bf")
        v9s35_reply3()

    def v9s35_reply3():
        contact_Chloe.newMessage(_("Wanna see what I'm doing now?"))
        contact_Chloe.addReply(_("Yeah, of course"), v9s35_reply4)
        contact_Chloe.addReply(_("You need to ask? :)"), v9s35_reply5)

    def v9s35_reply4():
        addPoint("bf")
        v9s35_reply5()

    def v9s35_reply5():
        contact_Chloe.newImgMessage(_("images/v9/Scene 35/chloetxtimg.webp"))
        contact_Chloe.addReply(_("OMG! I miss those!"), v9s35_reply6)
        contact_Chloe.addReply(_("OMG! You are magnificent!"), "s35_ChloeReplyWRs5")
    
    def v9s35_reply6():
        contact_Chloe.newMessage(_("Thought you'd like that :)"))
        contact_Chloe.addReply(_("Like? I love it! That just made my whole day better."))
        contact_Chloe.newMessage(_("Awww, such a charmer haha. Your turn. Let me see yours."))
        contact_Chloe.addReply(_("Your wish is my command."))
        contact_Chloe.addImgReply(_("images/v9/Scene 35/mcdickwolves.webp"))
        contact_Chloe.newMessage(_("God, I miss that cock. "))
        contact_Chloe.addReply(_("Can I come over? Haha."))
        contact_Chloe.newMessage(_("I wish. I have a lot to do for tomorrow, but that would be nice."))
        contact_Chloe.addReply(_("Yeah, that would be great. Would like to see more of you."))
        contact_Chloe.newMessage(_("No, that's all the pics I'm sending haha."))
        contact_Chloe.addReply(_("That's not what I meant, haha."))
        contact_Chloe.newMessage(_("Haha, I know what you meant. I'd like that, too."))
        contact_Chloe.addReply(_("Well, let me know when you're free and I'll make time."))
        contact_Chloe.newMessage(_("I definitely will. Goodnight [name]"))
        contact_Chloe.addReply(_("Goodnight, gorgeous."), v9s35_reply7)
        contact_Chloe.addReply(_("Goodnight, Chloe."))

    def v9s35_reply7():
        addPoint("bf")

    def v9s35_reply8():
        contact_Chloe.newMessage(_("Ugh. I'm so tired of studying."))
        contact_Chloe.addReply(_("Haha, me too. Kinda want to throw my books out the window."))
        contact_Chloe.newMessage(_("Haha. I wish I could just leave the house and not worry about it."))
        contact_Chloe.addReply(_("Me too. Wanna go for a walk together?"))
        contact_Chloe.newMessage(_("I wish. I have a lot to do for tomorrow, but that would be nice."))
        contact_Chloe.addReply(_("Yeah, it would be."))
        contact_Chloe.newMessage(_("I think I'll soak in the tub for a bit."))
        contact_Chloe.addReply(_("Can I join you?"))
        contact_Chloe.newMessage(_("Haha! You wish :)"))
        contact_Chloe.addReply(_("Hey, a guy can dream, right?"))
        contact_Chloe.newMessage(_("Yeah, but it's a dream."))
        contact_Chloe.addReply(_("For now haha."))
        contact_Chloe.newMessage(_("Haha, yeah for now. Well, I'll let you go. Was great to talk to you [name]."))
        contact_Chloe.addReply(_("Likewise. Don't be a stranger."))
        contact_Chloe.addReply(_("Yeah, it was nice to hear from you."))
        contact_Chloe.newMessage(_("Goodnight [name]"))
        contact_Chloe.addReply(_("Goodnight Chloe."))

label v9_room_sat_aft:
    if joinwolves:
        scene v9rsa1 # TPP. Show MC stood in his Wolves room near his bed.
        with fade

        pause 1

        scene v9rsa2 # TPP. Show MC flopped facedown on his bed.
        with dissolve

        u "(How much longer do I have?)"

        scene v9rsa3 # TPP. Show MC now on his back on his bed, looking at his phone (don't show phone screen)
        with dissolve
        
        play sound "sounds/vibrate.mp3"

        u "(I wonder who this is)"

        $ contact_Chloe.newMessage(_("Hey [name], what you up to?"), queue=False)
        $ contact_Chloe.addReply(_("Nothing much. Just relaxing. I'm kind of tired."))
        $ contact_Chloe.newMessage(_("Awwww. Long day?"))
        if chloers:
            $ contact_Chloe.addReply(_("Yeah haha, I feel wiped."), v9s35_reply1)
        else:
            $ contact_Chloe.addReply(_("Yeah haha, I feel wiped."), v9s35_reply8)

        label s35_PhoneContinueW:
            if contact_Chloe.getReplies():
                call screen phone
            if contact_Chloe.getReplies():
                "(I should reply to Chloe.)"
                jump s35_PhoneContinueW

        scene v9rsa3a # TPP. Same camera as v9rsa3, MC puts his phone down and yawns.
        with dissolve

        u "(Just a quick nap)"

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

        scene v9rsa7 # TPP. Show MC now on his back on his bed, looking at his phone (don't show phone screen)
        with dissolve
        
        play sound "sounds/vibrate.mp3"

        u "(I wonder who this is)"

        $ contact_Chloe.newMessage(_("Hey [name], what you up to?"), queue=False)
        $ contact_Chloe.addReply(_("Nothing much. Just relaxing. I'm kind of tired."))
        $ contact_Chloe.newMessage(_("Awwww. Long day?"))
        if chloers:
            $ contact_Chloe.addReply(_("Yeah haha, I feel wiped."), v9s35_reply1)
        else:
            $ contact_Chloe.addReply(_("Yeah haha, I feel wiped."), v9s35_reply8)

        label s35_PhoneContinueA:
            if contact_Chloe.getReplies():
                call screen phone
            if contact_Chloe.getReplies():
                "(I should reply to Chloe.)"
                jump s35_PhoneContinueA

        scene v9rsa7a # TPP. Same camera as v9rsa3, MC puts his phone down and yawns.
        with dissolve

        u "(Just a quick nap)"

        scene v9rsa8 # TPP. Show MC's Apes room door.
        with dissolve

        play sound "sounds/knock.mp3"

        u "Ugh!"

        jump v9_run_w_ryan