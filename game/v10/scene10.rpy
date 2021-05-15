# SCENE 10: MC Wakes Up Room Scene
# Locations: MC Apes/Wolves Room
# Characters: MC (Underwear)
# Time: Sunday Morning

label v10_sun_morn:
    default v10s10_hangWLinds = False

    if joinwolves:
        scene v10sum1 # TPP. Show MC in his Wolves bed looking up at the ceiling, MC looks tired.
        with fade

        pause 0.75

        play sound "sounds/vibrate.mp3"

        scene v10sum2 # TPP. Show MC reaching for his phone.
        with dissolve

        pause 0.75

        scene v10sum2a # TPP. Same as sum2, MC now on his phone in bed.
        with dissolve

        $ phonexit = "v10s10_PhoneContinueRilW"
        $ showphone = True
        
        if v10_ryan_fight:
            if not v10_ryan_win:
                $ contact_Riley.newMessage("Hey [name], what you up to?")
                $ contact_Riley.addReply("Nothing much.", "v10s10_ReplyRilW1")
                call screen phone

                label v10s10_ReplyRilW1:
                    $ contact_Riley.newMessage("How are you feeling after the fight?")
                    $ contact_Riley.addReply("Fine.", "v10s10_ReplyRilW2")
                    call screen messager(contact_Riley)

                label v10s10_ReplyRilW2:
                    $ contact_Riley.newMessage("Look, I just wanted to say not to let it get to you.")
                    $ contact_Riley.addReply("You think it bothers me? Guy just got lucky, that's all.", "v10s10_ReplyRilW3")
                    call screen messager(contact_Riley)
                    
                label v10s10_ReplyRilW3:
                    $ contact_Riley.newMessage("Well I know it would bother me! Who likes to lose, right?")
                    $ contact_Riley.addReply("It's okay Riley, you really don't have to do this.", "v10s10_ReplyRilW4")
                    call screen messager(contact_Riley)

                label v10s10_ReplyRilW4:
                    $ contact_Riley.newMessage("Do what? I just wanted to let you know I'm here for you if you need me.")
                    $ contact_Riley.addReply("Appreciated.", "v10s10_ReplyRilW5")
                    call screen messager(contact_Riley)

                label v10s10_ReplyRilW5:
                    $ contact_Riley.newMessage("And I'll keep on trying to lure out that smile of yours.")
                    $ contact_Riley.addReply("Maybe some other time.", "v10s10_ReplyRilW6")
                    call screen messager(contact_Riley)

                label v10s10_ReplyRilW6:
                    $ contact_Riley.newMessage("OK, I understand. Until then! Bye")
                    $ contact_Riley.addReply("Bye", "v10s10_PhoneContinueRilW")
                    call screen messager(contact_Riley)

            else:
                $ contact_Riley.newMessage("Hey champion, you gave us an amazing show last night! :)")
                $ contact_Riley.addReply("Thanks, Riley.", "v10s10_ReplyRilW7")
                call screen phone
            
                label v10s10_ReplyRilW7:
                    $ contact_Riley.newMessage("I especially loved that last punch. I mean, I'm not into violence but, you know.")
                    $ contact_Riley.addReply("Haha I will pretend I do and say yes.", "v10s10_ReplyRilW8")
                    call screen messager(contact_Riley)

                label v10s10_ReplyRilW8:
                    $ contact_Riley.newMessage("Anyway just keep it up! You'll have your supporters around the corner. :)")
                    $ contact_Riley.addReply("What can I say but thanks again. This is just a beginning, I guess.", "v10s10_ReplyRilW9")
                    call screen messager(contact_Riley)

                label v10s10_ReplyRilW9:
                    $ contact_Riley.newMessage("Don't get hurt, though!")
                    $ contact_Riley.addReply("Hahah, I'll try not to.", "v10s10_ReplyRilW10")
                    call screen messager(contact_Riley)

                label v10s10_ReplyRilW10:
                    $ contact_Riley.newMessage("Promise?")
                    $ contact_Riley.addReply("Promise.", "v10s10_ReplyRilW11")
                    call screen messager(contact_Riley)

                label v10s10_ReplyRilW11:
                    $ contact_Riley.newMessage("Pinky one?")
                    $ contact_Riley.addReply("Bye, Riley. :)", "v10s10_PhoneContinueRilW")
                    call screen messager(contact_Riley)

            label v10s10_PhoneContinueRilW:
                if contact_Riley.messages[-1].replies:
                    u "(I should reply to Riley.)"
                    jump v10s10_PhoneContinueRilW

        else:
            play sound "sounds/vibrate.mp3"
            $ phoneexit = "v10s10_PhoneContinueJoshW1"

            $ contact_Josh.newMessage("Friends or not friends, dude wtf?! That was one good show wasted!")
            $ contact_Josh.newMessage("Just saying you missed out on impressing a lot of ladies today")
            $ contact_Josh.addReply("I know... But hey, maybe some appreciate the compassion?", "v10s10_ReplyJoshWa3")
            call screen phone

            label v10s10_ReplyJoshWa3:
                $ contact_Josh.newMessage("Haha, sure dude")
                $ contact_Josh.addReply("Whatever man.", "v10s10_PhoneContinueJoshW1")
                call screen messager(contact_Josh)

            label v10s10_PhoneContinueJoshW1:
                if contact_Josh.messages[-1].replies:
                    u "(I should reply to Josh.)"
                    jump v10s10_PhoneContinueJoshW1

        if v10_ryan_win:
            play sound "sounds/vibrate.mp3"
            $ phoneexit = "v10s10_PhoneContinueLinW"

            $ contact_Lindsey.newMessage("Hey, [name]... congrats on the win.")
            $ contact_Lindsey.newMessage("I know it's quite early, but")

        else:
            play sound "sounds/vibrate.mp3"
            $ phoneexit = "v10s10_PhoneContinueLinW"

            $ contact_Lindsey.newMessage("Hey, [name]... I know you have a lot on your mind right now with everything that happened yesterday...")
            
        $ contact_Lindsey.newMessage("I've just been dealing with some stuff...")
        $ contact_Lindsey.newMessage("and I need someone to talk to")
        $ contact_Lindsey.newMessage("Sorry, we don't even know each other that well")
        $ contact_Lindsey.newMessage("it's just, I feel like I can talk to you...")
        $ contact_Lindsey.newMessage("I don't know, I'm sorry I don't wanna bother you")
        $ contact_Lindsey.newMessage("Just forget what I said")
        $ contact_Lindsey.addReply("If you need someone to talk I'll come over right now!", "v10s10_ReplyLinW1")
        $ contact_Lindsey.addReply("Uhm okay. No worries, let me know if you need anything", "v10s10_PhoneContinueLinW")
        call screen phone

        label v10s10_ReplyLinW1:
            $ contact_Lindsey.newMessage("Really? Thank you xx")
            $ contact_Lindsey.addReply("On my way", "v10s10_PhoneContinueLinW")
            call screen messager(contact_Lindsey)

        label v10s10_PhoneContinueLinW:
            if contact_Lindsey.messages[-1].replies:
                u "(I should reply to Lindsey.)"
                jump v10s10_PhoneContinueLinW

        $ showphone = False

        scene v10sum3 # TPP. Show MC placing his phone back down and sitting on the edge of his bed.
        with dissolve

        u "(Let's make this day better than yesterday)"

        scene black
        with fade

        if v10s10_hangWLinds:
            jump v10_linds_room

        else:
            jump v10_wolves_redecorate

    else:
        scene v10sum4 # TPP. Show MC in his Apes bed looking up at the ceiling, MC looks tired.
        with fade

        pause 0.75

        play sound "sounds/vibrate.mp3"

        scene v10sum5 # TPP. Show MC reaching for his phone.
        with dissolve

        pause 0.75

        scene v10sum5a # TPP. Same as sum2, MC now on his phone in bed.
        with dissolve

        $ phonexit = "v10s10_PhoneContinueRilA"
        $ showphone = True
        
        if v10_imre_fight:
            if not v10_imre_win:
                $ contact_Riley.newMessage("Hey [name], what you up to?")
                $ contact_Riley.addReply("Nothing much.", "v10s10_ReplyRilA1")
                call screen phone

                label v10s10_ReplyRilA1:
                    $ contact_Riley.newMessage("How are you feeling after the fight?")
                    $ contact_Riley.addReply("Fine.", "v10s10_ReplyRilA2")
                    call screen messager(contact_Riley)

                label v10s10_ReplyRilA2:
                    $ contact_Riley.newMessage("Look, I just wanted to say not to let it get to you.")
                    $ contact_Riley.addReply("You think it bothers me? Guy just got lucky, that's all.", "v10s10_ReplyRilA3")
                    call screen messager(contact_Riley)
                    
                label v10s10_ReplyRilA3:
                    $ contact_Riley.newMessage("Well I know it would bother me! Who likes to lose, right?")
                    $ contact_Riley.addReply("It's okay Riley, you really don't have to do this.", "v10s10_ReplyRilA4")
                    call screen messager(contact_Riley)

                label v10s10_ReplyRilA4:
                    $ contact_Riley.newMessage("Do what? I just wanted to let you know I'm here for you if you need me.")
                    $ contact_Riley.addReply("Appreciated.", "v10s10_ReplyRilA5")
                    call screen messager(contact_Riley)

                label v10s10_ReplyRilA5:
                    $ contact_Riley.newMessage("And I'll keep on trying to lure out that smile of yours.")
                    $ contact_Riley.addReply("Maybe some other time.", "v10s10_ReplyRilA6")
                    call screen messager(contact_Riley)

                label v10s10_ReplyRilA6:
                    $ contact_Riley.newMessage("OK, I understand. Until then! Bye")
                    $ contact_Riley.addReply("Bye", "v10s10_PhoneContinueRilA")
                    call screen messager(contact_Riley)

            else:
                $ contact_Riley.newMessage("Hey champion, you gave us an amazing show last night! :)")
                $ contact_Riley.addReply("Thanks, Riley.", "v10s10_ReplyRilA7")
                $ showphone = True
                call screen phone
            
                label v10s10_ReplyRilA7:
                    $ contact_Riley.newMessage("I especially loved that last punch. I mean, I'm not into violence but, you know.")
                    $ contact_Riley.addReply("Haha I will pretend I do and say yes.", "v10s10_ReplyRilA8")
                    call screen messager(contact_Riley)

                label v10s10_ReplyRilA8:
                    $ contact_Riley.newMessage("Anyway just keep it up! You'll have your supporters around the corner. :)")
                    $ contact_Riley.addReply("What can I say but thanks again. This is just a beginning, I guess.", "v10s10_ReplyRilA9")
                    call screen messager(contact_Riley)

                label v10s10_ReplyRilA9:
                    $ contact_Riley.newMessage("Don't get hurt, though!")
                    $ contact_Riley.addReply("Hahah, I'll try not to.", "v10s10_ReplyRilA10")
                    call screen messager(contact_Riley)

                label v10s10_ReplyRilA10:
                    $ contact_Riley.newMessage("Promise?")
                    $ contact_Riley.addReply("Promise.", "v10s10_ReplyRilA11")
                    call screen messager(contact_Riley)

                label v10s10_ReplyRilA11:
                    $ contact_Riley.newMessage("Pinky one?")
                    $ contact_Riley.addReply("Bye, Riley. :)", "v10s10_PhoneContinueRilA")
                    call screen messager(contact_Riley)

            label v10s10_PhoneContinueRilA:
                if contact_Riley.messages[-1].replies:
                    u "(I should reply to Riley.)"
                    jump v10s10_PhoneContinueRilA

        else:
            $ contact_Josh.newMessage("Friends or not friends, dude wtf?! That was one good show wasted!")
            $ contact_Josh.newMessage("Just saying you missed out on impressing a lot of ladies today")
            $ contact_Josh.addReply("I know... But hey, maybe some appreciate the compassion?", "v10s10_ReplyJoshWa3")
            call screen phone

            label v10s10_ReplyJoshAa3:
                $ contact_Josh.newMessage("Haha, sure dude")
                $ contact_Josh.addReply("Whatever man.", "v10s10_PhoneContinueJoshA1")
                call screen messager(contact_Josh)

            label v10s10_PhoneContinueJoshA1:
                if contact_Josh.messages[-1].replies:
                    u "(I should reply to Josh.)"
                    jump v10s10_PhoneContinueJoshA1

        if v10_imre_win:
            play sound "sounds/vibrate.mp3"
            $ phoneexit = "v10s10_PhoneContinueLinA"

            $ contact_Lindsey.newMessage("Hey, [name]... congrats on the win.")
            $ contact_Lindsey.newMessage("I know it's quite early, but")

        else:
            play sound "sounds/vibrate.mp3"
            $ phoneexit = "v10s10_PhoneContinueLinA"

            $ contact_Lindsey.newMessage("Hey, [name]... I know you have a lot on your mind right now with everything that happened yesterday...")

        $ contact_Lindsey.newMessage("I've just been dealing with some stuff...")
        $ contact_Lindsey.newMessage("and I need someone to talk to")
        $ contact_Lindsey.newMessage("Sorry, we don't even know each other that well")
        $ contact_Lindsey.newMessage("it's just, I feel like I can talk to you...")
        $ contact_Lindsey.newMessage("I don't know, I'm sorry I don't wanna bother you")
        $ contact_Lindsey.newMessage("Just forget what I said")
        $ contact_Lindsey.addReply("If you need someone to talk I'll come over right now!", "v10s10_ReplyLinA1")
        $ contact_Lindsey.addReply("Uhm okay. No worries, let me know if you need anything", "v10s10_PhoneContinueLinA")
        call screen phone

        label v10s10_ReplyLinA1:
            $ contact_Lindsey.newMessage("Really? Thank you xx")
            $ contact_Lindsey.addReply("On my way", "v10s10_PhoneContinueLinA")
            call screen messager(contact_Lindsey)

        label v10s10_PhoneContinueLinA:
            if contact_Lindsey.messages[-1].replies:
                u "(I should reply to Lindsey.)"
                jump v10s10_PhoneContinueLinA

        $ showphone = False

        scene v10sum6 # TPP. Show MC placing his phone back down and sitting on the edge of his bed.
        with dissolve

        u "(Let's make this day better than yesterday)"

        scene black
        with fade

        if v10s10_hangWLinds:
            jump v10_linds_room

        else:
            jump v10_apes_sam