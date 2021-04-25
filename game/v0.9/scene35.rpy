# SCENE 35: Your Room Sat Afternoon
# Locations: MC Wolves/Apes room
# Characters: MC (Outfit 3)
# Time: Saturday Morning

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

        $ phoneexit = "s35_PhoneContinueW"

        $ contact_Chloe.newMessage("Hey [name], what you up to?")
        $ contact_Chloe.addReply("Nothing much. Just relaxing. I'm kind of tired.", "s35_ChloeReplyW1")
        $ showphone = True
        call screen phone

        label s35_ChloeReplyW1:
            $ contact_Chloe.newMessage("Awwww. Long day?")
            if chloers:
                $ contact_Chloe.addReply("Yeah haha, I feel wiped.", "s35_ChloeReplyWRs1")
                call screen messager(contact_Chloe)

            else:
                $ contact_Chloe.addReply("Yeah haha, I feel wiped.", "s35_ChloeReplyWNoRs1")
                call screen messager(contact_Chloe)

        label s35_ChloeReplyWRs1:
            $ contact_Chloe.newMessage("I was thinking about you and I kind of miss you.")
            $ contact_Chloe.addReply("Kinda? That's it? ;)", "s35_ChloeReplyWRs2")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyWRs2:
            $ contact_Chloe.newMessage("Maybe haha. Ok, yeah, I miss you.")
            $ contact_Chloe.addReply("I miss you too.", "s35_ChloeReplyWRs3")
            $ contact_Chloe.addReply("That's better haha", "s35_ChloeReplyWRs3a")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyWRs3:
            $ addPoint("bf", 1)
            call screen messager(contact_Chloe)
            jump s35_ChloeReplyWRs3a

        label s35_ChloeReplyWRs3a:
            $ contact_Chloe.newMessage("Wanna see what I'm doing now?")
            $ contact_Chloe.addReply("Yeah, of course", "s35_ChloeReplyWRs4a")
            $ contact_Chloe.addReply("You need to ask? :)", "s35_ChloeReplyWRs4")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyWRs4:
            $ addPoint("bro", 1)
            call screen messager(contact_Chloe)
            jump s35_ChloeReplyWRs4a

        label s35_ChloeReplyWRs4a:
            $ contact_Chloe.newImgMessage("images/v09/Scene 35/chloetxtimg.webp")
            $ contact_Chloe.addReply("OMG! I miss those!", "s35_ChloeReplyWRs5")
            $ contact_Chloe.addReply("OMG! You are magnificent!", "s35_ChloeReplyWRs5")
            call screen messager(contact_Chloe)
        
        label s35_ChloeReplyWRs5:
            $ contact_Chloe.newMessage("Thought you'd like that :)")
            $ contact_Chloe.addReply("Like? I love it! That just made my whole day better.", "s35_ChloeReplyWRs6")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyWRs6:
            $ contact_Chloe.newMessage("Awww, such a charmer haha. Your turn. Let me see yours.")
            $ contact_Chloe.addReply("Your wish is my command.", "s35_ChloeReplyWRs7")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyWRs7:
            $ contact_Chloe.addImgReply("images/v09/Scene 35/mcdickwolves.webp", "s35_ChloeReplyWRs8")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyWRs8:
            $ contact_Chloe.newMessage("God, I miss that cock. ")
            $ contact_Chloe.addReply("Can I come over? Haha.", "s35_ChloeReplyWRs9")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyWRs9:
            $ contact_Chloe.newMessage("I wish. I have a lot to do for tomorrow, but that would be nice.")
            $ contact_Chloe.addReply("Yeah, that would be great. Would like to see more of you.", "s35_ChloeReplyWRs10")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyWRs10:
            $ contact_Chloe.newMessage("No, that's all the pics I'm sending haha.")
            $ contact_Chloe.addReply("That's not what I meant, haha.", "s35_ChloeReplyWRs11")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyWRs11:
            $ contact_Chloe.newMessage("Haha, I know what you meant. I'd like that, too.")
            $ contact_Chloe.addReply("Well, let me know when you're free and I'll make time.", "s35_ChloeReplyWRs12")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyWRs12:
            $ contact_Chloe.newMessage("I definitely will. Goodnight [name]")
            $ contact_Chloe.addReply("Goodnight, gorgeous.", "s35_ChloeReplyWRs13")
            $ contact_Chloe.addReply("Goodnight, Chloe.", "s35_ChloeReplyWRs13a")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyWRs13:
            $ addPoint("bf", 1)
            call screen messager(contact_Chloe)

        label s35_ChloeReplyWRs13a:
            call screen messager(contact_Chloe) 

        label s35_ChloeReplyWNoRs1:
            $ contact_Chloe.newMessage("Ugh. I'm so tired of studying.")
            $ contact_Chloe.addReply("Haha, me too. Kinda want to throw my books out the window.", "s35_ChloeReplyWNoRs2")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyWNoRs2:
            $ contact_Chloe.newMessage("Haha. I wish I could just leave the house and not worry about it.")
            $ contact_Chloe.addReply("Me too. Wanna go for a walk together?", "s35_ChloeReplyWNoRs3")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyWNoRs3:
            $ contact_Chloe.newMessage("I wish. I have a lot to do for tomorrow, but that would be nice.")
            $ contact_Chloe.addReply("Yeah, it would be.", "s35_ChloeReplyWNoRs4")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyWNoRs4:
            $ contact_Chloe.newMessage("I think I'll soak in the tub for a bit.")
            $ contact_Chloe.addReply("Can I join you?", "s35_ChloeReplyWNoRs5")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyWNoRs5:
            $ contact_Chloe.newMessage("Haha! You wish :)")
            $ contact_Chloe.addReply("Hey, a guy can dream, right?", "s35_ChloeReplyWNoRs6")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyWNoRs6:
            $ contact_Chloe.newMessage("Yeah, but it's a dream.")
            $ contact_Chloe.addReply("For now haha.", "s35_ChloeReplyWNoRs7")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyWNoRs7:
            $ contact_Chloe.newMessage("Haha, yeah for now. Well, I'll let you go. Was great to talk to you [name].")
            $ contact_Chloe.addReply("Likewise. Don't be a stranger.", "s35_ChloeReplyWNoRs8")
            $ contact_Chloe.addReply("Yeah, it was nice to hear from you.", "s35_ChloeReplyWNoRs8")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyWNoRs8:
            $ contact_Chloe.newMessage("Goodnight [name]")
            $ contact_Chloe.addReply("Goodnight Chloe.", "s35_ChloeReplyWNoRs9")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyWNoRs9:
            call screen messager(contact_Chloe)

        label s35_PhoneContinueW:
            if contact_Chloe.messages[-1].replies:
                "(I should reply to Chloe.)"
                jump s35_PhoneContinueW

        $ showphone = False

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

        $ phoneexit = "s35_PhoneContinueA"

        $ contact_Chloe.newMessage("Hey [name], what you up to?")
        $ contact_Chloe.addReply("Nothing much. Just relaxing. I'm kind of tired.", "s35_ChloeReplyA1")
        $ showphone = True
        call screen phone

        label s35_ChloeReplyA1:
            $ contact_Chloe.newMessage("Awwww. Long day?")
            if chloers:
                $ contact_Chloe.addReply("Yeah haha, I feel wiped.", "s35_ChloeReplyARs1")
                call screen messager(contact_Chloe)

            else:
                $ contact_Chloe.addReply("Yeah haha, I feel wiped.", "s35_ChloeReplyANoRs1")
                call screen messager(contact_Chloe)

        label s35_ChloeReplyARs1:
            $ contact_Chloe.newMessage("I was thinking about you and I kind of miss you.")
            $ contact_Chloe.addReply("Kinda? That's it? ;)", "s35_ChloeReplyARs2")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyARs2:
            $ contact_Chloe.newMessage("Maybe haha. Ok, yeah, I miss you.")
            $ contact_Chloe.addReply("I miss you too.", "s35_ChloeReplyARs3")
            $ contact_Chloe.addReply("That's better haha", "s35_ChloeReplyARs3a")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyARs3:
            $ addPoint("bf", 1)
            call screen messager(contact_Chloe)
            jump s35_ChloeReplyARs3a

        label s35_ChloeReplyARs3a:
            $ contact_Chloe.newMessage("Wanna see what I'm doing now?")
            $ contact_Chloe.addReply("Yeah, of course", "s35_ChloeReplyARs4a")
            $ contact_Chloe.addReply("You need to ask? :)", "s35_ChloeReplyARs4")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyARs4:
            $ addPoint("bro", 1)
            call screen messager(contact_Chloe)
            jump s35_ChloeReplyARs4a

        label s35_ChloeReplyARs4a:
            $ contact_Chloe.newImgMessage("images/v09/Scene 35/chloetxtimg.webp")
            $ contact_Chloe.addReply("OMG! I miss those!", "s35_ChloeReplyARs5")
            $ contact_Chloe.addReply("OMG! You are magnificent!", "s35_ChloeReplyARs5")
            call screen messager(contact_Chloe)
        
        label s35_ChloeReplyARs5:
            $ contact_Chloe.newMessage("Thought you'd like that :)")
            $ contact_Chloe.addReply("Like? I love it! That just made my whole day better.", "s35_ChloeReplyARs6")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyARs6:
            $ contact_Chloe.newMessage("Awww, such a charmer haha. Your turn. Let me see yours.")
            $ contact_Chloe.addReply("Your wish is my command.", "s35_ChloeReplyARs7")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyARs7:
            $ contact_Chloe.addImgReply("images/v09/Scene 35/mcdickapes.webp", "s35_ChloeReplyARs8")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyARs8:
            $ contact_Chloe.newMessage("God, I miss that cock. ")
            $ contact_Chloe.addReply("Can I come over? Haha.", "s35_ChloeReplyARs9")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyARs9:
            $ contact_Chloe.newMessage("I wish. I have a lot to do for tomorrow, but that would be nice.")
            $ contact_Chloe.addReply("Yeah, that would be great. Would like to see more of you.", "s35_ChloeReplyARs10")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyARs10:
            $ contact_Chloe.newMessage("No, that's all the pics I'm sending haha.")
            $ contact_Chloe.addReply("That's not what I meant, haha.", "s35_ChloeReplyARs11")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyARs11:
            $ contact_Chloe.newMessage("Haha, I know what you meant. I'd like that, too.")
            $ contact_Chloe.addReply("Well, let me know when you're free and I'll make time.", "s35_ChloeReplyARs12")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyARs12:
            $ contact_Chloe.newMessage("I definitely will. Goodnight [name]")
            $ contact_Chloe.addReply("Goodnight, gorgeous.", "s35_ChloeReplyARs13")
            $ contact_Chloe.addReply("Goodnight, Chloe.", "s35_ChloeReplyARs13a")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyARs13:
            $ addPoint("bf", 1)
            call screen messager(contact_Chloe)

        label s35_ChloeReplyARs13a:
            call screen messager(contact_Chloe) 

        label s35_ChloeReplyANoRs1:
            $ contact_Chloe.newMessage("Ugh. I'm so tired of studying.")
            $ contact_Chloe.addReply("Haha, me too. Kinda want to throw my books out the window.", "s35_ChloeReplyANoRs2")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyANoRs2:
            $ contact_Chloe.newMessage("Haha. I wish I could just leave the house and not worry about it.")
            $ contact_Chloe.addReply("Me too. Wanna go for a walk together?", "s35_ChloeReplyANoRs3")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyANoRs3:
            $ contact_Chloe.newMessage("I wish. I have a lot to do for tomorrow, but that would be nice.")
            $ contact_Chloe.addReply("Yeah, it would be.", "s35_ChloeReplyANoRs4")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyANoRs4:
            $ contact_Chloe.newMessage("I think I'll soak in the tub for a bit.")
            $ contact_Chloe.addReply("Can I join you?", "s35_ChloeReplyANoRs5")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyANoRs5:
            $ contact_Chloe.newMessage("Haha! You wish :)")
            $ contact_Chloe.addReply("Hey, a guy can dream, right?", "s35_ChloeReplyANoRs6")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyANoRs6:
            $ contact_Chloe.newMessage("Yeah, but it's a dream.")
            $ contact_Chloe.addReply("For now haha.", "s35_ChloeReplyANoRs7")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyANoRs7:
            $ contact_Chloe.newMessage("Haha, yeah for now. Well, I'll let you go. Was great to talk to you [name].")
            $ contact_Chloe.addReply("Likewise. Don't be a stranger.", "s35_ChloeReplyANoRs8")
            $ contact_Chloe.addReply("Yeah, it was nice to hear from you.", "s35_ChloeReplyANoRs8")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyANoRs8:
            $ contact_Chloe.newMessage("Goodnight [name]")
            $ contact_Chloe.addReply("Goodnight Chloe.", "s35_ChloeReplyANoRs9")
            call screen messager(contact_Chloe)

        label s35_ChloeReplyANoRs9:
            call screen messager(contact_Chloe)

        label s35_PhoneContinueA:
            if contact_Chloe.messages[-1].replies:
                "(I should reply to Chloe.)"
                jump s35_PhoneContinueA

        $ showphone = False

        scene v9rsa7a # TPP. Same camera as v9rsa3, MC puts his phone down and yawns.
        with dissolve

        u "(Just a quick nap)"

        scene v9rsa8 # TPP. Show MC's Apes room door.
        with dissolve

        play sound "sounds/knock.mp3"

        u "Ugh!"

        jump v9_run_w_ryan     