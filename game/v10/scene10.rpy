# SCENE 10: MC Wakes Up Room Scene
# Locations: MC Apes/Wolves Room
# Characters: MC (Underwear)
# Time: Sunday Morning

init python:
    def v10s10_reply1():
        setattr(store, "v10s10_hangWLinds", True)
        contact_Lindsey.newMessage("Really? Thank you xx")
        contact_Lindsey.addReply("On my way")

label v10_sun_morn:
    default v10s10_hangWLinds = False
    play music "music/v10/Scene 10/Track Scene 10.mp3" fadein 3
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
        
        if v10_ryan_fight and not v10_ryan_win:
            $ contact_Riley.newMessage("Hey [name], what you up to?", queue=False)
            $ contact_Riley.addReply("Nothing much.")
            $ contact_Riley.newMessage("How are you feeling after the fight?")
            $ contact_Riley.addReply("Fine.")
            $ contact_Riley.newMessage("Look, I just wanted to say not to let it get to you.")
            $ contact_Riley.addReply("You think it bothers me? Guy just got lucky, that's all.")
            $ contact_Riley.newMessage("Well I know it would bother me! Who likes to lose, right?")
            $ contact_Riley.addReply("It's okay Riley, you really don't have to do this.")
            $ contact_Riley.newMessage("Do what? I just wanted to let you know I'm here for you if you need me.")
            $ contact_Riley.addReply("Appreciated.")
            $ contact_Riley.newMessage("And I'll keep on trying to lure out that smile of yours.")
            $ contact_Riley.addReply("Maybe some other time.")
            $ contact_Riley.newMessage("OK, I understand. Until then! Bye")
            $ contact_Riley.addReply("Bye")

        elif v10_ryan_fight:
            $ contact_Riley.newMessage("Hey champion, you gave us an amazing show last night! :)", queue=False)
            $ contact_Riley.addReply("Thanks, Riley.")
            $ contact_Riley.newMessage("I especially loved that last punch. I mean, I'm not into violence but, you know.")
            $ contact_Riley.addReply("Haha I will pretend I do and say yes.")
            $ contact_Riley.newMessage("Anyway just keep it up! You'll have your supporters around the corner. :)")
            $ contact_Riley.addReply("What can I say but thanks again. This is just a beginning, I guess.")
            $ contact_Riley.newMessage("Don't get hurt, though!")
            $ contact_Riley.addReply("Hahah, I'll try not to.")
            $ contact_Riley.newMessage("Promise?")
            $ contact_Riley.addReply("Promise.")
            $ contact_Riley.newMessage("Pinky one?")
            $ contact_Riley.addReply("Bye, Riley. :)")

        else:
            play sound "sounds/vibrate.mp3"

            $ contact_Josh.newMessage("Friends or not friends, dude wtf?! That was one good show wasted!", queue=False)
            $ contact_Josh.newMessage("Just saying you missed out on impressing a lot of ladies today", queue=False)
            $ contact_Josh.addReply("I know... But hey, maybe some appreciate the compassion?")
            $ contact_Josh.newMessage("Haha, sure dude")
            $ contact_Josh.addReply("Whatever man.")

        label v10s10_PhoneContinueJoshW1:
            if contact_Josh.getReplies() or contact_Riley.getReplies():
                call screen phone
            if contact_Josh.getReplies() or contact_Riley.getReplies():
                u "(I should check my phone.)"
                jump v10s10_PhoneContinueJoshW1

        if v10_ryan_win:
            play sound "sounds/vibrate.mp3"

            $ contact_Lindsey.newMessage("Hey, [name]... congrats on the win.", queue=False)
            $ contact_Lindsey.newMessage("I know it's quite early, but", queue=False)

        else:
            play sound "sounds/vibrate.mp3"

            $ contact_Lindsey.newMessage("Hey, [name]... I know you have a lot on your mind right now with everything that happened yesterday...", queue=False)
            
        $ contact_Lindsey.newMessage("I've just been dealing with some stuff...", queue=False)
        $ contact_Lindsey.newMessage("And I need someone to talk to", queue=False)
        $ contact_Lindsey.newMessage("Sorry, we don't even know each other that well", queue=False)
        $ contact_Lindsey.newMessage("It's just, I feel like I can talk to you...", queue=False)
        $ contact_Lindsey.newMessage("I don't know, I'm sorry I don't wanna bother you", queue=False)
        $ contact_Lindsey.newMessage("Just forget what I said", queue=False)
        $ contact_Lindsey.addReply("If you need someone to talk I'll come over right now!", v10s10_reply1)
        $ contact_Lindsey.addReply("Uhm okay. No worries, let me know if you need anything")

        label v10s10_PhoneContinueLinW:
            if contact_Lindsey.getReplies():
                call screen phone
            if contact_Lindsey.getReplies():
                u "(I should reply to Lindsey.)"
                jump v10s10_PhoneContinueLinW

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

        pause 0.75

        play sound "sounds/vibrate.mp3"

        scene v10sum5a # TPP. Same as sum2, MC now on his phone in bed.
        with dissolve
        
        if v10_imre_fight and not v10_imre_win:
            $ contact_Riley.newMessage("Hey [name], what you up to?", queue=False)
            $ contact_Riley.addReply("Nothing much.")
            $ contact_Riley.newMessage("How are you feeling after the fight?")
            $ contact_Riley.addReply("Fine.")
            $ contact_Riley.newMessage("Look, I just wanted to say not to let it get to you.")
            $ contact_Riley.addReply("You think it bothers me? Guy just got lucky, that's all.")
            $ contact_Riley.newMessage("Well I know it would bother me! Who likes to lose, right?")
            $ contact_Riley.addReply("It's okay Riley, you really don't have to do this.")
            $ contact_Riley.newMessage("Do what? I just wanted to let you know I'm here for you if you need me.")
            $ contact_Riley.addReply("Appreciated.")
            $ contact_Riley.newMessage("And I'll keep on trying to lure out that smile of yours.")
            $ contact_Riley.addReply("Maybe some other time.")
            $ contact_Riley.newMessage("OK, I understand. Until then! Bye")
            $ contact_Riley.addReply("Bye")

        elif v10_imre_fight:
            $ contact_Riley.newMessage("Hey champion, you gave us an amazing show last night! :)", queue=False)
            $ contact_Riley.addReply("Thanks, Riley.")
            $ contact_Riley.newMessage("I especially loved that last punch. I mean, I'm not into violence but, you know.")
            $ contact_Riley.addReply("Haha I will pretend I do and say yes.")
            $ contact_Riley.newMessage("Anyway just keep it up! You'll have your supporters around the corner. :)")
            $ contact_Riley.addReply("What can I say but thanks again. This is just a beginning, I guess.")
            $ contact_Riley.newMessage("Don't get hurt, though!")
            $ contact_Riley.addReply("Hahah, I'll try not to.")
            $ contact_Riley.newMessage("Promise?")
            $ contact_Riley.addReply("Promise.")
            $ contact_Riley.newMessage("Pinky one?")
            $ contact_Riley.addReply("Bye, Riley. :)")

        else:
            play sound "sounds/vibrate.mp3"

            $ contact_Josh.newMessage("Friends or not friends, dude wtf?! That was one good show wasted!", queue=False)
            $ contact_Josh.newMessage("Just saying you missed out on impressing a lot of ladies today", queue=False)
            $ contact_Josh.addReply("I know... But hey, maybe some appreciate the compassion?", "v10s10_ReplyJoshWa3")
            $ contact_Josh.newMessage("Haha, sure dude")
            $ contact_Josh.addReply("Whatever man.")

        label v10s10_PhoneContinueJoshW2:
            if contact_Josh.getReplies() or contact_Riley.getReplies():
                call screen phone
            if contact_Josh.getReplies() or contact_Riley.getReplies():
                u "(I should check my phone.)"
                jump v10s10_PhoneContinueJoshW2

        if v10_imre_win:
            play sound "sounds/vibrate.mp3"

            $ contact_Lindsey.newMessage("Hey, [name]... congrats on the win.", queue=False)
            $ contact_Lindsey.newMessage("I know it's quite early, but", queue=False)

        else:
            play sound "sounds/vibrate.mp3"

            $ contact_Lindsey.newMessage("Hey, [name]... I know you have a lot on your mind right now with everything that happened yesterday...", queue=False)
            
        $ contact_Lindsey.newMessage("I've just been dealing with some stuff...", queue=False)
        $ contact_Lindsey.newMessage("And I need someone to talk to", queue=False)
        $ contact_Lindsey.newMessage("Sorry, we don't even know each other that well", queue=False)
        $ contact_Lindsey.newMessage("It's just, I feel like I can talk to you...", queue=False)
        $ contact_Lindsey.newMessage("I don't know, I'm sorry I don't wanna bother you", queue=False)
        $ contact_Lindsey.newMessage("Just forget what I said", queue=False)
        $ contact_Lindsey.addReply("If you need someone to talk I'll come over right now!", v10s10_reply1)
        $ contact_Lindsey.addReply("Uhm okay. No worries, let me know if you need anything")

        label v10s10_PhoneContinueLinA:
            if contact_Lindsey.getReplies():
                call screen phone
            if contact_Lindsey.getReplies():
                u "(I should reply to Lindsey.)"
                jump v10s10_PhoneContinueLinA

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