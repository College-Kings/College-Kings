# SCENE 10: MC Wakes Up Room Scene
# Locations: MC Apes/Wolves Room
# Characters: MC (Underwear)
# Time: Sunday Morning

label v10_sun_morn:
    play music "music/v10/Track Scene 10.mp3" fadein 2
    if joinwolves:
        scene v10sum1 # TPP. Show MC in his Wolves bed looking up at the ceiling, MC looks tired.
        with fade
        play sound "sounds/vibrate.mp3"

        pause 1.25

        scene v10sum2 # TPP. Show MC reaching for his phone.
        with dissolve

        pause 0.75

        scene v10sum2a # TPP. Same as sum2, MC now on his phone in bed.
        with dissolve
        pause 0.75
    
        if v10_ryan_fight and not v10_ryan_win:
            $ MessengerService.new_message(riley, "Hey [name], what you up to?")
            $ MessengerService.add_reply(riley, "Nothing much.")
            $ MessengerService.new_message(riley, "How are you feeling after the fight?")
            $ MessengerService.add_reply(riley, "Fine.")
            $ MessengerService.new_message(riley, "Look, I just wanted to say not to let it get to you.")
            $ MessengerService.add_reply(riley, "You think it bothers me? Guy just got lucky, that's all.")
            $ MessengerService.new_message(riley, "Well I know it would bother me! Who likes to lose, right?")
            $ MessengerService.add_reply(riley, "It's okay Riley, you really don't have to do this.")
            $ MessengerService.new_message(riley, "Do what? I just wanted to let you know I'm here for you if you need me.")
            $ MessengerService.add_reply(riley, "Appreciated.")
            $ MessengerService.new_message(riley, "And I'll keep on trying to lure out that smile of yours.")
            $ MessengerService.add_reply(riley, "Maybe some other time.")
            $ MessengerService.new_message(riley, "OK, I understand. Until then! Bye")
            $ MessengerService.add_reply(riley, "Bye")

        elif v10_ryan_fight:
            $ MessengerService.new_message(riley, "Hey champion, you gave us an amazing show last night! :)")
            $ MessengerService.add_reply(riley, "Thanks, Riley.")
            $ MessengerService.new_message(riley, "I especially loved that last punch. I mean, I'm not into violence but, you know.")
            $ MessengerService.add_reply(riley, "Haha I will pretend I do and say yes.")
            $ MessengerService.new_message(riley, "Anyway just keep it up! You'll have your supporters around the corner. :)")
            $ MessengerService.add_reply(riley, "What can I say but thanks again. This is just a beginning, I guess.")
            $ MessengerService.new_message(riley, "Don't get hurt, though!")
            $ MessengerService.add_reply(riley, "Hahah, I'll try not to.")
            $ MessengerService.new_message(riley, "Promise?")
            $ MessengerService.add_reply(riley, "Promise.")
            $ MessengerService.new_message(riley, "Pinky one?")
            $ MessengerService.add_reply(riley, "Bye, Riley. :)")

        else:
            $ MessengerService.new_message(josh, "Friends or not friends, dude wtf?! That was one good show wasted!")
            $ MessengerService.new_message(josh, "Just saying you missed out on impressing a lot of ladies today")
            $ MessengerService.add_reply(josh, "I know... But hey, maybe some appreciate the compassion?")
            $ MessengerService.new_message(josh, "Haha, sure dude")
            $ MessengerService.add_reply(josh, "Whatever man.")

        while MessengerService.has_replies(josh) or MessengerService.has_replies(riley):
            call screen phone
            if MessengerService.has_replies(josh) or MessengerService.has_replies(riley):
                u "(I should check my phone.)"

        play sound "sounds/vibrate.mp3"

        python:
            v10s10_reply1 = MessageBuilder(lindsey)
            v10s10_reply1.set_variable("v10s10_hangWLinds", True)
            v10s10_reply1.new_message("Really? Thank you xx")
            v10s10_reply1.add_reply("On my way")

        if v10_ryan_win:
            $ MessengerService.new_message(lindsey, "Hey, [name]... congrats on the win.")
            $ MessengerService.new_message(lindsey, "I know it's quite early, but")
        else:
            $ MessengerService.new_message(lindsey, "Hey, [name]... I know you have a lot on your mind right now with everything that happened yesterday...")
        $ MessengerService.new_message(lindsey, "I've just been dealing with some stuff...")
        $ MessengerService.new_message(lindsey, "And I need someone to talk to")
        $ MessengerService.new_message(lindsey, "Sorry, we don't even know each other that well")
        $ MessengerService.new_message(lindsey, "It's just, I feel like I can talk to you...")
        $ MessengerService.new_message(lindsey, "I don't know, I'm sorry I don't wanna bother you")
        $ MessengerService.new_message(lindsey, "Just forget what I said")
        $ MessengerService.add_replies(lindsey,
            Reply("If you need someone to talk I'll come over right now!", v10s10_reply1),
            Reply("Uhm okay. No worries, let me know if you need anything")
        )

        while MessengerService.has_replies(lindsey):
            call screen phone
            if MessengerService.has_replies(lindsey):
                u "(I should reply to Lindsey.)"

        scene v10sum3 # TPP. Show MC placing his phone back down and sitting on the edge of his bed.
        with dissolve

        u "(Let's make this day better than yesterday)"

        scene black
        with fade

        stop music fadeout 3

        if v10s10_hangWLinds:
            jump v10_linds_room

        else:
            jump v10_mc_clock_trans

    else:
        scene v10sum4 # TPP. Show MC in his Apes bed looking up at the ceiling, MC looks tired.
        with fade
        play sound "sounds/vibrate.mp3"

        pause 1.25

        scene v10sum5a # TPP. Same as sum2, MC now on his phone in bed.
        with dissolve

        pause 0.75
        
        if v10_imre_fight and not v10_imre_win:
            $ MessengerService.new_message(riley, "Hey [name], what you up to?")
            $ MessengerService.add_reply(riley, "Nothing much.")
            $ MessengerService.new_message(riley, "How are you feeling after the fight?")
            $ MessengerService.add_reply(riley, "Fine.")
            $ MessengerService.new_message(riley, "Look, I just wanted to say not to let it get to you.")
            $ MessengerService.add_reply(riley, "You think it bothers me? Guy just got lucky, that's all.")
            $ MessengerService.new_message(riley, "Well I know it would bother me! Who likes to lose, right?")
            $ MessengerService.add_reply(riley, "It's okay Riley, you really don't have to do this.")
            $ MessengerService.new_message(riley, "Do what? I just wanted to let you know I'm here for you if you need me.")
            $ MessengerService.add_reply(riley, "Appreciated.")
            $ MessengerService.new_message(riley, "And I'll keep on trying to lure out that smile of yours.")
            $ MessengerService.add_reply(riley, "Maybe some other time.")
            $ MessengerService.new_message(riley, "OK, I understand. Until then! Bye")
            $ MessengerService.add_reply(riley, "Bye")

        elif v10_imre_fight:
            $ MessengerService.new_message(riley, "Hey champion, you gave us an amazing show last night! :)")
            $ MessengerService.add_reply(riley, "Thanks, Riley.")
            $ MessengerService.new_message(riley, "I especially loved that last punch. I mean, I'm not into violence but, you know.")
            $ MessengerService.add_reply(riley, "Haha I will pretend I do and say yes.")
            $ MessengerService.new_message(riley, "Anyway just keep it up! You'll have your supporters around the corner. :)")
            $ MessengerService.add_reply(riley, "What can I say but thanks again. This is just a beginning, I guess.")
            $ MessengerService.new_message(riley, "Don't get hurt, though!")
            $ MessengerService.add_reply(riley, "Hahah, I'll try not to.")
            $ MessengerService.new_message(riley, "Promise?")
            $ MessengerService.add_reply(riley, "Promise.")
            $ MessengerService.new_message(riley, "Pinky one?")
            $ MessengerService.add_reply(riley, "Bye, Riley. :)")

        else:
            $ MessengerService.new_message(josh, "Friends or not friends, dude wtf?! That was one good show wasted!")
            $ MessengerService.new_message(josh, "Just saying you missed out on impressing a lot of ladies today")
            $ MessengerService.add_reply(josh, "I know... But hey, maybe some appreciate the compassion?")
            $ MessengerService.new_message(josh, "Haha, sure dude")
            $ MessengerService.add_reply(josh, "Whatever man.")

        while MessengerService.has_replies(josh) or MessengerService.has_replies(riley):
            call screen phone
            if MessengerService.has_replies(josh) or MessengerService.has_replies(riley):
                u "(I should check my phone.)"

        play sound "sounds/vibrate.mp3"

        python:
            v10s10_reply1 = MessageBuilder(lindsey)
            v10s10_reply1.set_variable("v10s10_hangWLinds", True)
            v10s10_reply1.new_message("Really? Thank you xx")
            v10s10_reply1.add_reply("On my way")

        if v10_imre_win:
            $ MessengerService.new_message(lindsey, "Hey, [name]... congrats on the win.")
            $ MessengerService.new_message(lindsey, "I know it's quite early, but")
        else:
            $ MessengerService.new_message(lindsey, "Hey, [name]... I know you have a lot on your mind right now with everything that happened yesterday...", force_send=True)
        $ MessengerService.new_message(lindsey, "I've just been dealing with some stuff...")
        $ MessengerService.new_message(lindsey, "And I need someone to talk to")
        $ MessengerService.new_message(lindsey, "Sorry, we don't even know each other that well")
        $ MessengerService.new_message(lindsey, "It's just, I feel like I can talk to you...")
        $ MessengerService.new_message(lindsey, "I don't know, I'm sorry I don't wanna bother you")
        $ MessengerService.new_message(lindsey, "Just forget what I said")
        $ MessengerService.add_replies(lindsey,
            Reply("If you need someone to talk I'll come over right now!", v10s10_reply1),
            Reply("Uhm okay. No worries, let me know if you need anything")
        )

        while MessengerService.has_replies(lindsey):
            call screen phone
            if MessengerService.has_replies(lindsey):
                u "(I should reply to Lindsey.)"

        scene v10sum6 # TPP. Show MC placing his phone back down and sitting on the edge of his bed.
        with dissolve

        u "(Let's make this day better than yesterday)"

        scene black
        with fade

        stop music fadeout 3

        if v10s10_hangWLinds:
            jump v10_linds_room

        else:
            jump v10_mc_clock_trans