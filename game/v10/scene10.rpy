# SCENE 10: MC Wakes Up Room Scene
# Locations: MC Apes/Wolves Room
# Characters: MC (Underwear)
# Time: Sunday Morning

init python:
    def v10s10_reply1():
        setattr(store, "v10s10_hangWLinds", True)
        lindsey.messenger.newMessage("Really? Thank you xx")
        lindsey.messenger.addReply("On my way")

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
            $ riley.messenger.newMessage("Hey [name], what you up to?", force_send=True)
            $ riley.messenger.addReply("Nothing much.")
            $ riley.messenger.newMessage("How are you feeling after the fight?")
            $ riley.messenger.addReply("Fine.")
            $ riley.messenger.newMessage("Look, I just wanted to say not to let it get to you.")
            $ riley.messenger.addReply("You think it bothers me? Guy just got lucky, that's all.")
            $ riley.messenger.newMessage("Well I know it would bother me! Who likes to lose, right?")
            $ riley.messenger.addReply("It's okay Riley, you really don't have to do this.")
            $ riley.messenger.newMessage("Do what? I just wanted to let you know I'm here for you if you need me.")
            $ riley.messenger.addReply("Appreciated.")
            $ riley.messenger.newMessage("And I'll keep on trying to lure out that smile of yours.")
            $ riley.messenger.addReply("Maybe some other time.")
            $ riley.messenger.newMessage("OK, I understand. Until then! Bye")
            $ riley.messenger.addReply("Bye")

        elif v10_ryan_fight:
            $ riley.messenger.newMessage("Hey champion, you gave us an amazing show last night! :)", force_send=True)
            $ riley.messenger.addReply("Thanks, Riley.")
            $ riley.messenger.newMessage("I especially loved that last punch. I mean, I'm not into violence but, you know.")
            $ riley.messenger.addReply("Haha I will pretend I do and say yes.")
            $ riley.messenger.newMessage("Anyway just keep it up! You'll have your supporters around the corner. :)")
            $ riley.messenger.addReply("What can I say but thanks again. This is just a beginning, I guess.")
            $ riley.messenger.newMessage("Don't get hurt, though!")
            $ riley.messenger.addReply("Hahah, I'll try not to.")
            $ riley.messenger.newMessage("Promise?")
            $ riley.messenger.addReply("Promise.")
            $ riley.messenger.newMessage("Pinky one?")
            $ riley.messenger.addReply("Bye, Riley. :)")

        else:
            $ josh.messenger.newMessage("Friends or not friends, dude wtf?! That was one good show wasted!", force_send=True)
            $ josh.messenger.newMessage("Just saying you missed out on impressing a lot of ladies today", force_send=True)
            $ josh.messenger.addReply("I know... But hey, maybe some appreciate the compassion?")
            $ josh.messenger.newMessage("Haha, sure dude")
            $ josh.messenger.addReply("Whatever man.")

        label v10s10_PhoneContinueJoshW1:
            if josh.messenger.replies or riley.messenger.replies:
                call screen phone
            if josh.messenger.replies or riley.messenger.replies:
                u "(I should check my phone.)"
                jump v10s10_PhoneContinueJoshW1

        play sound "sounds/vibrate.mp3"

        if v10_ryan_win:
            $ lindsey.messenger.newMessage("Hey, [name]... congrats on the win.", force_send=True)
            $ lindsey.messenger.newMessage("I know it's quite early, but", force_send=True)

        else:
            $ lindsey.messenger.newMessage("Hey, [name]... I know you have a lot on your mind right now with everything that happened yesterday...", force_send=True)
            
        $ lindsey.messenger.newMessage("I've just been dealing with some stuff...", force_send=True)
        $ lindsey.messenger.newMessage("And I need someone to talk to", force_send=True)
        $ lindsey.messenger.newMessage("Sorry, we don't even know each other that well", force_send=True)
        $ lindsey.messenger.newMessage("It's just, I feel like I can talk to you...", force_send=True)
        $ lindsey.messenger.newMessage("I don't know, I'm sorry I don't wanna bother you", force_send=True)
        $ lindsey.messenger.newMessage("Just forget what I said", force_send=True)
        $ lindsey.messenger.addReply("If you need someone to talk I'll come over right now!", v10s10_reply1)
        $ lindsey.messenger.addReply("Uhm okay. No worries, let me know if you need anything")

        label v10s10_PhoneContinueLinW:
            if lindsey.messenger.replies:
                call screen phone
            if lindsey.messenger.replies:
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
        play sound "sounds/vibrate.mp3"

        pause 1.25

        scene v10sum5a # TPP. Same as sum2, MC now on his phone in bed.
        with dissolve

        pause 0.75
        
        if v10_imre_fight and not v10_imre_win:
            $ riley.messenger.newMessage("Hey [name], what you up to?", force_send=True)
            $ riley.messenger.addReply("Nothing much.")
            $ riley.messenger.newMessage("How are you feeling after the fight?")
            $ riley.messenger.addReply("Fine.")
            $ riley.messenger.newMessage("Look, I just wanted to say not to let it get to you.")
            $ riley.messenger.addReply("You think it bothers me? Guy just got lucky, that's all.")
            $ riley.messenger.newMessage("Well I know it would bother me! Who likes to lose, right?")
            $ riley.messenger.addReply("It's okay Riley, you really don't have to do this.")
            $ riley.messenger.newMessage("Do what? I just wanted to let you know I'm here for you if you need me.")
            $ riley.messenger.addReply("Appreciated.")
            $ riley.messenger.newMessage("And I'll keep on trying to lure out that smile of yours.")
            $ riley.messenger.addReply("Maybe some other time.")
            $ riley.messenger.newMessage("OK, I understand. Until then! Bye")
            $ riley.messenger.addReply("Bye")

        elif v10_imre_fight:
            $ riley.messenger.newMessage("Hey champion, you gave us an amazing show last night! :)", force_send=True)
            $ riley.messenger.addReply("Thanks, Riley.")
            $ riley.messenger.newMessage("I especially loved that last punch. I mean, I'm not into violence but, you know.")
            $ riley.messenger.addReply("Haha I will pretend I do and say yes.")
            $ riley.messenger.newMessage("Anyway just keep it up! You'll have your supporters around the corner. :)")
            $ riley.messenger.addReply("What can I say but thanks again. This is just a beginning, I guess.")
            $ riley.messenger.newMessage("Don't get hurt, though!")
            $ riley.messenger.addReply("Hahah, I'll try not to.")
            $ riley.messenger.newMessage("Promise?")
            $ riley.messenger.addReply("Promise.")
            $ riley.messenger.newMessage("Pinky one?")
            $ riley.messenger.addReply("Bye, Riley. :)")

        else:
            $ josh.messenger.newMessage("Friends or not friends, dude wtf?! That was one good show wasted!", force_send=True)
            $ josh.messenger.newMessage("Just saying you missed out on impressing a lot of ladies today", force_send=True)
            $ josh.messenger.addReply("I know... But hey, maybe some appreciate the compassion?")
            $ josh.messenger.newMessage("Haha, sure dude")
            $ josh.messenger.addReply("Whatever man.")

        label v10s10_PhoneContinueJoshW2:
            if josh.messenger.replies or riley.messenger.replies:
                call screen phone
            if josh.messenger.replies or riley.messenger.replies:
                u "(I should check my phone.)"
                jump v10s10_PhoneContinueJoshW2

        play sound "sounds/vibrate.mp3"

        if v10_imre_win:
            $ lindsey.messenger.newMessage("Hey, [name]... congrats on the win.", force_send=True)
            $ lindsey.messenger.newMessage("I know it's quite early, but", force_send=True)

        else:
            $ lindsey.messenger.newMessage("Hey, [name]... I know you have a lot on your mind right now with everything that happened yesterday...", force_send=True)
            
        $ lindsey.messenger.newMessage("I've just been dealing with some stuff...", force_send=True)
        $ lindsey.messenger.newMessage("And I need someone to talk to", force_send=True)
        $ lindsey.messenger.newMessage("Sorry, we don't even know each other that well", force_send=True)
        $ lindsey.messenger.newMessage("It's just, I feel like I can talk to you...", force_send=True)
        $ lindsey.messenger.newMessage("I don't know, I'm sorry I don't wanna bother you", force_send=True)
        $ lindsey.messenger.newMessage("Just forget what I said", force_send=True)
        $ lindsey.messenger.addReply("If you need someone to talk I'll come over right now!", v10s10_reply1)
        $ lindsey.messenger.addReply("Uhm okay. No worries, let me know if you need anything")

        label v10s10_PhoneContinueLinA:
            if lindsey.messenger.replies:
                call screen phone
            if lindsey.messenger.replies:
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