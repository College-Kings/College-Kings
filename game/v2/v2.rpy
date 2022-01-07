init python:

    # Ryan messages
    def v2_reply1():
        add_point(KCT.BRO)
        ryan.messenger.newMessage(_("Look, I know what Grayson did was a dick move, but he was just being overprotective of Chloe"))
        ryan.messenger.addReply(_("Whatever"), v2_reply2)
        ryan.messenger.addReply(_("Don't you dare defend that guy"), v2_reply3)

    def v2_reply2():
        add_point(KCT.BRO)

    def v2_reply3():
        add_point(KCT.TROUBLEMAKER)
        ryan.messenger.newMessage(_("Sorry..."))

    def v2_reply4():
        add_point(KCT.TROUBLEMAKER)
        ryan.messenger.newMessage(_("Look, I know what Grayson did was a dick move, but he was just being overprotective of Chloe"))
        ryan.messenger.addReply(_("Whatever"), v2_reply2)
        ryan.messenger.addReply(_("Don't you dare defend that guy"), v2_reply3)

    # Lauren messages
    def v2_reply5():
        setattr(store, "meetlauren", True)
        add_point(KCT.BOYFRIEND)
        lauren.messenger.newMessage(_("Great, I'll see you then :)"))

    def v2_reply6():
        grant_achievement("mixed_feelings")

    # Josh messages
    def v2_reply7():
        add_point(KCT.BRO)
        josh.messenger.newMessage(_("It's fine, you go get her."))

    def v2_reply8():
        add_point(KCT.BOYFRIEND)
        josh.messenger.newMessage(_("Nah, you don't want a bitch like her."))
        josh.messenger.addReply(_("Yeah, I guess you're right."), v2_reply9)
        josh.messenger.addReply(_("Dude, what the fuck?!"), v2_reply10)

    def v2_reply9():
        add_point(KCT.BRO)
        josh.messenger.newMessage(_("Hahaha, I'm just kidding, yo."))
        josh.messenger.newMessage(_("Of course I gave her your number."))
        josh.messenger.addReply(_("Damn, you got me."))

    def v2_reply10():
        add_point(KCT.TROUBLEMAKER)
        josh.messenger.newMessage(_("Hahaha, I'm just kidding, yo."))
        josh.messenger.newMessage(_("Of course I gave her your number."))
        josh.messenger.addReply(_("Damn, you got me."))

    # Aubrey messages
    def v2_reply11():
        add_point(KCT.BRO)
        aubrey.messenger.newMessage(_("Yeah, I mean they had a thing a while ago but she broke it off 'cause he lied about some shit."))
        aubrey.messenger.newMessage(_("So... tomorrow?"))
        aubrey.messenger.addReply(_("My day tomorrow is quite full, but how about today?\n\nI need to buy a costume."), v2_reply12)

    def v2_reply12():
        add_point(KCT.BOYFRIEND)
        aubrey.messenger.newMessage(_("I've got dance practice tonight \n:("))
        aubrey.messenger.addReply(_("I'm not talking tonight, I can pick you up right now."))
        aubrey.messenger.newMessage(_("Oh wow, that's spontaneous, I like it haha.\n\nI guess come to the Chicks' house whenever you're ready and then we can go costume shopping."))
        aubrey.messenger.addReply(_("Cool, I'll be 20 mins."))

    def v2_reply13():
        setattr(store, "costumeaubrey", True)
        add_point(KCT.BOYFRIEND)
        aubrey.messenger.newMessage(_("Good :)"))

    def v2_reply14():
        setattr(store, "costumeaubrey", False)
        add_point(KCT.TROUBLEMAKER)
        aubrey.messenger.newMessage(_("Oh, okay. Guess we'll have to postpone the costume buying."))

label v2start:
    play music "music/muffledparty.mp3"
    scene black
    
    scene s121a
    with fade

    cl "*Muffled* Why did you do that?! We were just talking!"

    scene s121b
    with dissolve
    ry "*Muffled* [name]?! Are you okay??"

    stop music fadeout 3

    # you wake up in your room with Imre

    scene s123
    with Fade (3,0,3)

    imre "Hey man, did you have a good night?"

    play music "music/m9punk.mp3"
    scene s123a
    with dissolve

    u "What? How did I get here?"

    scene s123
    with dissolve

    imre "Some Ryan guy dropped you off, after you got yourself beaten up."

    scene s123a
    with dissolve

    u "Shit... my head hurts so much."

    scene s123
    with dissolve

    imre "I mean, have you seen your face?"

    imre "Here, I took a picture last night when you came home."

    scene s123b
    with fade ## holding phone with picture of you beaten up on it
    " "

    scene s123a
    with fade

    u "Man, Grayson is such an asshole. I didn't even do anything."

    scene s123c
    with dissolve

    imre "What did you expect? I told you the Apes are dogshit."

    imre "If you knew how to fight, maybe he wouldn't fuck with you."

    menu:
        "Hmm... maybe":
            $ add_point(KCT.BRO)

            scene s123d
            with dissolve
            u "Hmm... maybe."

            scene s123
            with dissolve
            imre "Just think about it, okay? I'll see you later."

        "I'm not fighting":
            $ add_point(KCT.BOYFRIEND)

            scene s123d
            with dissolve
            u "I'm not fighting. I'll just stay away from them."

            scene s123c
            with dissolve

            imre "Dude, you don't know what Grayson's like."

            imre "If he sees you looking at him wrong from now on, you'll end up in the hospital."

            menu:
                "I'll think about it":
                    $ add_point(KCT.BRO)

                    scene s123d
                    with dissolve
                    u "Look, I'll think about it. But don't get your hopes up."

                    scene s123
                    with dissolve
                    imre "That's all I'm asking for. I'll see you later."

                "I won't fight":
                    $ add_point(KCT.BOYFRIEND)

                    scene s123d
                    with dissolve
                    u "I'm not fighting. That's final."

                    scene s123c
                    with dissolve

                    imre "You're being stupid, man. Whatever, suit yourself."

    scene s96g
    with fade

    label bjj_bd: #for compatibility only
    play sound "sounds/vibrate.mp3"
    queue sound "sounds/vibrate.mp3"

    $ ryan.messenger.newMessage(_("You okay?"), force_send=True)
    $ ryan.messenger.addReply(_("I'm fine"), v2_reply1)
    $ ryan.messenger.addReply(_("No, wtf was that?! Fuck Grayson and fuck the Apes"), v2_reply4)

    $ add_point(KCT.TROUBLEMAKER)
    $ lauren.messenger.newMessage(_("Is everything okay?"))
    $ lauren.messenger.addReply(_("Yeah, I'm fine."))
    $ lauren.messenger.newMessage(_("Okay..."))

    if lauren.messenger.replies:
        $ lauren.messenger.newMessage(_("Hello?? Can we please talk today?"), force_send=True)
        $ lauren.messenger.addReply(_("Yeah, SV cafe in 20 mins?"), v2_reply5)
        $ lauren.messenger.addReply(_("Sorry, I can't"), v2_reply6)
    else:
        $ lauren.messenger.newMessage(_("Are we still on for today? :)"), force_send=True)
        $ lauren.messenger.addReply(_("Yeah, SV cafe in 20 mins?"), v2_reply5)
        $ lauren.messenger.addReply(_("Sorry, I can't"), v2_reply6)

    " "

    scene s96g
    with dissolve

    label repeatb:
        if lauren.messenger.replies:
            call screen phone
        if lauren.messenger.replies:
            u "(Damn, my phone's blowing up. I should probably check my messages.)"
            jump repeatb

    if meetlauren:
        u "(Well, time to head to the cafe to meet Lauren.)"

    else:
        u "(There's too much on my mind to be dealing with Lauren right now.)"

        u "(Maybe taking a walk will relax me.)"

    label walk1: #for compatibility only
    stop music fadeout 3
    scene s124
    with Fade (1,0,1)

    u "(I can't believe I got knocked out in front of everyone...)"

    play music "music/m4punk.mp3"

    u "(Especially in front of Chloe, that's so humiliating.)"

    scene s124a
    with dissolve

    u "(Is she dating Grayson? I really thought she was flirting with me.)"

    u "(But why would Grayson punch me otherwise?)"

    u "(Just thinking about all this shit makes me so mad.)"

    scene s125
    with dissolve

    tom "Eyy, Mr. steal-your-girl got beaten up. *laughs*"

    tom "That's what you get for being such a little bitch."

    menu:
        "Shout back":
            jump v1_tomShoutBack

        "Keep walking":
            scene s125a
            with dissolve

            tom "Yeah, you better keep walking, pussy."

            menu:
                "Shout back":
                    jump v1_tomShoutBack

                "Walk away":
                    jump v1_tomWalkAway

label bk_a: #for compatibility only
label v1_tomShoutBack:
    $ fighttom = True

    scene 126a # tom close up
    with dissolve

    u "The fuck did you just say to me?!"

    scene s126
    with dissolve

    tom "You heard me. You're a fucking bitch that tried to cockblock me."

    scene 126a
    with dissolve

    u "Dude, she wanted to talk to me. She was happy that you left. You bored her."
    scene push12

    scene tompush
    pause 0.7
    play sound "sounds/push.mp3"
    scene push12
    with vpunch

    tom "Fuck you!"

    stop music fadeout 3

# Tom Fight
label gb:

    scene sf1
    with dissolve
    " "

    scene tomstancekick
    with dissolve

    call screen confirm("Would you like to play the fighting tutorial?",
        yes_action=[SetVariable("fight_tutorial", True), Call("fight_tutorialLabel")],
        no_action=[SetVariable("fight_tutorial", False), Return()])

    if fight_tutorial:
        call screen tomtut1

        label tomtut1kick:
            scene kick2movie
            pause 0.7

            play sound "sounds/ks.mp3"
            
            scene kick2pic
            with hpunch

            tut "Great job! You've hit Tom and hurt him. He's now more likely to get tired, give up or even get knocked out."
            tut "Beware, since you've let your guard down to attack, he's going to try and abuse it with an attack of his own."

            scene tomhookmovie
            $ renpy.pause(0.7)

            scene tomhook
            show screen fight_tutorial(stance="defend")

            tut "Now it's time to block Tom's attack."

            show screen fight_tutorial(highlight="q", stance="defend")
            tut "{b}Q{/b} lets you block your head from heavy attacks such as hooks, which come from a slight angle."
            show screen fight_tutorial(highlight="w", stance="defend")
            tut "In order to protect yourself from attacks flying straight at your face, such as jabs, press {b}W{/b}."
            show screen fight_tutorial(highlight="r", stance="defend")
            tut "Lastly, you can protect your legs, from low kicks for example, by pressing {b}R{/b}."
            show screen fight_tutorial(highlight="q", stance="defend")
            tut "As of right now, there's a hook flying at your head, press {b}Q{/b} in the upcoming screen in order to block it."
            hide screen fight_tutorial

            call screen fight_defendTutorial


        label tomtut1hook:
            scene hook1movie
            $ renpy.pause(0.7)
            play sound "sounds/bs.mp3"
            scene hook1pic
            with hpunch

            tut "Yeah, why follow what the tutorial says?? It's not like it's trying to help you or anything."

            tut "Because you decided to attack Tom's guarded areas, he was able to block your attack easily."

            tut "He can now counter attack."
            $ stance = 2

            scene hookcountermovie
            $ renpy.pause(0.7)

            scene hookcounter

            show screen fight_tutorial(highlight="q", stance="defend")
            tut "{b}Q{/b} lets you block your head from heavy attacks such as hooks, which come from a slight angle."
            show screen fight_tutorial(highlight="w", stance="defend")
            tut "In order to protect yourself from attacks flying straight at your face, such as jabs, press {b}W{/b}."
            show screen fight_tutorial(highlight="r", stance="defend")
            tut "Lastly, you can protect your legs, from low kicks for example, by pressing {b}R{/b}."
            show screen fight_tutorial(highlight="w", stance="defend")
            tut "As of right now, there's a jab flying at your face, press {b}W{/b} in the upcoming screen in order to block it."
            hide screen fight_tutorial

            call screen fight_defendTutorial


        label tomtut1jab:
            scene jab1movie
            $ renpy.pause(0.7)
            play sound "sounds/bs.mp3"
            scene jab1pic
            with hpunch

            tut "Yeah, why follow what the tutorial says?? It's not like it's trying to help you or anything."

            tut "Because you decided to attack Tom's guarded areas, he was able to block your attack easily."

            tut "He can now counter attack."

            $ stance = 2

            scene jabcountermovie
            $ renpy.pause(0.7)

            scene jabcounter

            tut "Now it's time to block Tom's attack."

            show screen fight_tutorial(highlight="q", stance="defend")
            tut "{b}Q{/b} lets you block your head from heavy attacks such as hooks, which come from a slight angle."
            show screen fight_tutorial(highlight="w", stance="defend")
            tut "In order to protect yourself from attacks flying straight at your face, such as jabs, press {b}W{/b}."
            show screen fight_tutorial(highlight="r", stance="defend")
            tut "Lastly, you can protect your legs, from low kicks for example, by pressing {b}R{/b}."
            show screen fight_tutorial(highlight="w", stance="defend")
            tut "As of right now, there's a jab flying at your face, press {b}W{/b} in the upcoming screen in order to block it."
            hide screen fight_tutorial

            call screen fight_defendTutorial


        label tuthookblock:
            play sound "sounds/bs.mp3"
            scene tomhookblock
            with hpunch

            tut "Great job, you blocked Tom's hook."

            scene tomstancehook

            tut "This ends the tutorial. The real fight will test your reaction times."
            
            jump tomFightStart


        label tuthookhit:
            play sound "sounds/hs.mp3"
            scene tomhookhit
            with hpunch

            tut "You did not block your head by pressing {b}Q{/b} and got hit. Next time, try to block the correct part of your body."

            scene tomstancehook

            tut "This ends the tutorial. The real fight will test your reaction times."
            
            jump tomFightStart

########FIGHT SYSTEM
label tomFightStart:
    call screen fight_typeMenu

    if fight_type == "normal":
        $ simtomfight = False

        call screen fight_selectDifficulty

        call screen fight_keybindOptions
    
    elif fight_type == "simReal" or fight_type == "simWin":
        $ simtomfight = True
        
    $ stance = 1
    $ tomstance = renpy.random.choice([1, 2, 3, 4])
    $ tomattack = renpy.random.choice([1, 2, 3, 4])
    $ simtom = renpy.random.choice([1, 2, 3, 4, 5, 6])
    $ simyou = renpy.random.choice([1, 2, 3, 4, 5, 6])

    if fight_type == "simWin":
        $ youHealth = 100000
    else:
        $ youHealth = 3

    $ enemyhealth = 5
    $ youDamage = 0
    $ tomdmg = 0

    label tomkick1:
        if tomdmg >= enemyhealth:

            scene youfinishmovie
            $ renpy.pause(1)
            play sound "sounds/fall.mp3"
            $ stance = 0
            $ youDamage = 0
            scene youfinish
            with vpunch
            $ renpy.pause()

            jump youfinish

        else:
            $ tomdmg += 1
            scene kick2movie
            $ renpy.pause(0.7)
            play sound "sounds/ks.mp3"
            scene kick2pic
            with hpunch

            pause 0.5 #Variable here
            jump tomattack1




    label tomkick2:
        if youDamage >= youHealth:

            scene tomfinishmovie
            $ renpy.pause(1)
            play sound "sounds/fall.mp3"
            $ stance = 0
            $ youDamage = 0
            scene tomfinish
            with vpunch

            $ renpy.pause()


            jump tomfinish6
        else:


            scene hook1movie
            $ renpy.pause(0.7)
            play sound "sounds/bs.mp3"
            scene hook1pic
            with hpunch

            pause 0.5
            jump tomattack2



    label tomkick3:
        if youDamage >= youHealth:

            scene tomfinishmovie
            $ renpy.pause(1)
            play sound "sounds/fall.mp3"
            $ stance = 0
            $ youDamage = 0
            scene tomfinish
            with vpunch

            $ renpy.pause()

            jump tomfinish6
        else:

            scene jab1movie
            $ renpy.pause(0.7)
            play sound "sounds/bs.mp3"
            scene jab1pic
            with hpunch

            pause 0.5

            jump tomattack3


    label tomsimstart2:
    label tomsimstart:
    label tomhook1:
        if tomdmg >= enemyhealth:

            scene youfinishmovie
            $ renpy.pause(1)
            play sound "sounds/fall.mp3"
            $ stance = 0
            $ youDamage = 0
            scene youfinish
            with vpunch
            $ renpy.pause()

            jump youfinish


        else:

            scene hook2movie
            $ renpy.pause(0.7)
            play sound "sounds/hs.mp3"
            scene hook2pic
            with hpunch

            pause 0.5


            $ tomdmg += 1
            jump tomattack4

    label tomhook2:
        if youDamage >= youHealth:

            scene tomfinishmovie
            $ renpy.pause(1)
            play sound "sounds/fall.mp3"
            $ stance = 0
            $ youDamage = 0
            scene tomfinish
            with vpunch

            $ renpy.pause()

            jump tomfinish1
        else:


            scene jab1movie
            $ renpy.pause(0.7)
            play sound "sounds/bs.mp3"
            scene jab1pic
            with hpunch

            pause 0.5

            jump tomattack5

    label tomhook3:
        if youDamage >= youHealth:

            scene tomfinishmovie
            $ renpy.pause(1)
            play sound "sounds/fall.mp3"
            $ stance = 0
            $ youDamage = 0
            scene tomfinish
            with vpunch

            $ renpy.pause()

            jump tomfinish2
        else:


            scene kick1movie
            $ renpy.pause(0.7)
            play sound "sounds/ks.mp3"
            scene kick1pic
            with hpunch

            pause 0.5

            jump tomattack6


    label tomjab1:

        if tomdmg >= enemyhealth:

            scene youfinishmovie
            $ renpy.pause(1)
            play sound "sounds/fall.mp3"
            $ stance = 0
            $ youDamage = 0
            scene youfinish
            with vpunch
            $ renpy.pause()

            jump youfinish

        else:


            scene jab2movie
            $ renpy.pause(0.7)
            play sound "sounds/js.mp3"
            scene jab2pic
            with hpunch


            $ tomdmg += 1

            pause 0.5

            jump tomattack7


    label tomjab2:
        if youDamage >= youHealth:


            scene tomfinishmovie
            $ renpy.pause(1)
            play sound "sounds/fall.mp3"
            $ stance = 0
            $ youDamage = 0
            scene tomfinish
            with vpunch

            $ renpy.pause()

            jump tomfinish3
        else:
            scene hook1movie
            $ renpy.pause(0.7)
            play sound "sounds/bs.mp3"
            scene hook1pic
            with hpunch

            pause 0.5

            jump tomattack8


    label tomjab3:

        if youDamage >= youHealth:


            scene tomfinishmovie
            $ renpy.pause(1)

            play sound "sounds/fall.mp3"
            $ stance = 0
            $ youDamage = 0
            scene tomfinish
            with vpunch

            $ renpy.pause()

            jump tomfinish4
        else:


            scene kick1movie
            $ renpy.pause(0.7)
            play sound "sounds/ks.mp3"
            scene kick1pic
            with hpunch

            pause 0.5
            jump tomattack9


    label tomattack1:
    label tomattack2:
    label tomattack3:
    label tomattack4:
    label tomattack5:
    label tomattack6:
    label tomattack7:
    label tomattack8:
    label tomattack9:
    label timer1:
    label timer2:
    label timer3:
        $ stance = 2

        if tomattack == 1:


            scene tomhookmovie
            $ renpy.pause(0.4)

            scene tomhook
            $ tomstance = renpy.random.choice([1, 2, 3])
            $ simyou = renpy.random.choice([1, 2, 3, 4])

            if simtomfight:
                if simtom == 1:
                    jump tomhookhit2
                if simtom == 2:
                    jump tomhookhit
                if simtom == 3 or 4:
                    jump tomhookblocked

            else:
                call screen tomattack




        if tomattack == 2:




            scene tomjabmovie
            $ renpy.pause(0.4)

            scene tomjab
            $ tomstance = renpy.random.choice([1, 2, 3])
            $ simyou = renpy.random.choice([1, 2, 3, 4])

            if simtomfight:
                if simtom == 1:
                    jump tomjabhit2
                if simtom == 2:
                    jump tomjabhit
                if simtom == 3 or 4:
                    jump tomjabblocked

            else:
                call screen tomattack

        if tomattack == 3:



            scene tomkickmovie
            $ renpy.pause(0.4)

            scene tomkick
            $ tomstance = renpy.random.choice([1, 2, 3])
            $ simyou = renpy.random.choice([1, 2, 3, 4])


            if simtomfight:
                if simtom == 1:
                    jump tomkickhit
                if simtom == 2:
                    jump tomkickhit2
                if simtom == 3 or 4:
                    jump tomkickblocked
            else:
                call screen tomattack


    label tomhookhit:
    label tomhookhit2:
    label timer4:

        play sound "sounds/hs.mp3"
        $ youDamage += 1
        scene tomhookhit
        with hpunch

        pause 0.5
        $ stance = 1
        $ tomattack = renpy.random.choice([1, 2, 3])
        $ simtom = renpy.random.choice([1, 2, 3, 4])

        if simtomfight:
            if tomstance == 1:
                if simyou == 1:
                    jump tomkick2
                if simyou == 2:
                    jump tomkick3
                if simyou == 3 or 4:
                    jump tomkick1
            if tomstance == 2:
                if simyou == 1:
                    jump tomhook2
                if simyou == 2:
                    jump tomhook3
                if simyou == 3 or 4:
                    jump tomhook1
            if tomstance == 3:
                if simyou == 1:
                    jump tomjab2
                if simyou == 2:
                    jump tomjab3
                if simyou == 3 or 4:
                    jump tomjab1
        else:
            call screen youattack

    label tomhookblocked:

        play sound "sounds/bs.mp3"
        scene tomhookblock
        with hpunch

        pause 0.5
        $ stance = 1
        $ tomattack = renpy.random.choice([1, 2, 3])
        $ simtom = renpy.random.choice([1, 2, 3, 4])
        if simtomfight:
            if tomstance == 1:
                if simyou == 1:
                    jump tomkick2
                if simyou == 2:
                    jump tomkick3
                if simyou == 3 or 4:
                    jump tomkick1
            if tomstance == 2:
                if simyou == 1:
                    jump tomhook2
                if simyou == 2:
                    jump tomhook3
                if simyou == 3 or 4:
                    jump tomhook1
            if tomstance == 3:
                if simyou == 1:
                    jump tomjab2
                if simyou == 2:
                    jump tomjab3
                if simyou == 3 or 4:
                    jump tomjab1
        else:
            call screen youattack

    label tomjabhit:
    label tomjabhit2:
    label timer5:

        play sound "sounds/js.mp3"
        scene tomjabhit
        with hpunch

        pause 0.5
        $ youDamage += 1
        $ stance = 1
        $ tomattack = renpy.random.choice([1, 2, 3])
        $ simtom = renpy.random.choice([1, 2, 3, 4])
        if simtomfight:
            if tomstance == 1:
                if simyou == 1:
                    jump tomkick2
                if simyou == 2:
                    jump tomkick3
                if simyou == 3 or 4:
                    jump tomkick1
            if tomstance == 2:
                if simyou == 1:
                    jump tomhook2
                if simyou == 2:
                    jump tomhook3
                if simyou == 3 or 4:
                    jump tomhook1
            if tomstance == 3:
                if simyou == 1:
                    jump tomjab2
                if simyou == 2:
                    jump tomjab3
                if simyou == 3 or 4:
                    jump tomjab1
        else:
            call screen youattack

    label tomjabblocked:

        play sound "sounds/bs.mp3"
        scene tomjabblock
        with hpunch

        pause 0.5
        $ stance = 1
        $ tomattack = renpy.random.choice([1, 2, 3])
        $ simtom = renpy.random.choice([1, 2, 3, 4])
        if simtomfight:
            if tomstance == 1:
                if simyou == 1:
                    jump tomkick2
                if simyou == 2:
                    jump tomkick3
                if simyou == 3 or 4:
                    jump tomkick1
            if tomstance == 2:
                if simyou == 1:
                    jump tomhook2
                if simyou == 2:
                    jump tomhook3
                if simyou == 3 or 4:
                    jump tomhook1
            if tomstance == 3:
                if simyou == 1:
                    jump tomjab2
                if simyou == 2:
                    jump tomjab3
                if simyou == 3 or 4:
                    jump tomjab1
        else:
            call screen youattack

    label tomkickhit:
    label tomkickhit2:
    label timer6:
        play sound "sounds/ks.mp3"
        scene tomkickhit
        with hpunch

        pause 0.5
        $ youDamage += 1
        $ stance = 1
        $ tomattack = renpy.random.choice([1, 2, 3])
        $ simtom = renpy.random.choice([1, 2, 3, 4])
        if simtomfight:
            if tomstance == 1:
                if simyou == 1:
                    jump tomkick2
                if simyou == 2:
                    jump tomkick3
                if simyou == 3 or 4:
                    jump tomkick1
            if tomstance == 2:
                if simyou == 1:
                    jump tomhook2
                if simyou == 2:
                    jump tomhook3
                if simyou == 3 or 4:
                    jump tomhook1
            if tomstance == 3:
                if simyou == 1:
                    jump tomjab2
                if simyou == 2:
                    jump tomjab3
                if simyou == 3 or 4:
                    jump tomjab1
        else:
            call screen youattack

    label tomkickblocked:
        play sound "sounds/ks.mp3"
        scene tomkickblock
        with hpunch

        pause 0.5
        $ stance = 1
        $ tomattack = renpy.random.choice([1, 2, 3])
        $ simtom = renpy.random.choice([1, 2, 3, 4])
        if simtomfight:
            if tomstance == 1:
                if simyou == 1:
                    jump tomkick2
                if simyou == 2:
                    jump tomkick3
                if simyou == 3 or 4:
                    jump tomkick1
            if tomstance == 2:
                if simyou == 1:
                    jump tomhook2
                if simyou == 2:
                    jump tomhook3
                if simyou == 3 or 4:
                    jump tomhook1
            if tomstance == 3:
                if simyou == 1:
                    jump tomjab2
                if simyou == 2:
                    jump tomjab3
                if simyou == 3 or 4:
                    jump tomjab1
        else:
            call screen youattack


    label tomfinish1:
    label tomfinish2:
    label tomfinish3:
    label tomfinish4:
    label tomfinish5:
    label tomfinish6:

    scene tf

    " "

    jump v1_tomWalkAway

label youfinish:
    if reaction == 0.5:
        $ grant_achievement("the_notorious")
            
    $ wintom = True

    menu:
        "Kick him":
            $ add_point(KCT.TROUBLEMAKER)

            play sound "sounds/js.mp3"
            scene yf
            with vpunch

            u "Fuck you!"

        "Walk away":
            $ add_point(KCT.BRO)

    $ renpy.end_replay()

label tf2: #for compatibility only
label v1_tomWalkAway:
    $ firstfight = False

    if meetlauren:
        jump meet_lauren2

    else:
        scene s133
        with Fade (1,0,1) # in front of san vallejo
        if fighttom and not wintom:
            u "(Fuck, I feel like shit...)"

        elif fighttom:
            u "(Holy shit, I just knocked someone out...)"

        else:
            u "(What a douchebag...)"

        u "(Also, what am I gonna do about Lauren? I can't avoid her forever.)"

        jump history2

label meet_lauren2:
    play music "music/mlove2.mp3"

    if fighttom and not wintom:
        scene s128a #outside of cafe with bloody nose
        with Fade (1,0,1)
        u "(Fuck, I feel like shit...)"

        u "(Hopefully Lauren doesn't make a big deal out of my bruises.)"

    elif fighttom:
        scene s128 #outside of cafe
        with Fade (1,0,1)
        u "(Holy shit, I just knocked someone out...)"

        u "(Hopefully Lauren doesn't make a big deal out of my bruises.)"

    else:
        scene s128 #outside of cafe
        with Fade (1,0,1)
        u "(What a douchebag...)"

        u "(Hopefully Lauren doesn't make a big deal out of my bruises.)"

    scene s129 # seeing Lauren on a table in the cafe
    with fade

    la "Heyyy-"

    scene s129b
    with dissolve

    la "Oh my god! What happened to your face?!"

    scene s129c
    with dissolve

    u "Some asshole punched me in the face at the Apes' rush party last night."

    if fighttom and not wintom:
        u "(And also I just got beaten up by another guy on the way here...)"

    elif fighttom:
        u "(And also I just beat a guy up on the way here...)"

    scene s130 # lauren accross table # your hands are on the table
    with fade

    la "[name], fighting is so stupid. Please don't get sucked up into it. You're way too smart for that."

    scene s130a
    with dissolve

    u "No but... I didn't even do anything."

    scene s130 # lauren accross table # your hands are on the table
    with dissolve

    la "Ugh okay... I hope that's true. Anyway..."

    scene s130b
    with dissolve

    la "About yesterday in the park..."

    show screen tutorial([
        "When people make important decisions on how they feel about you, they consider what kind of a person you are.",
        "Your Key Character Trait (Loyal, Popular or Confident) has a strong influence on how other characters react to your behavior.",
        "Some people value a popular leader, some care more about loyalty than status and some are drawn to confidence.",
        "Your decisions matter and have long time effects, as you can only have one KCT at a time. So think about what kind of person you want to be."
    ])

    menu:
        "There was something there":
            $ add_point(KCT.BOYFRIEND)
            
            if lauren.relationship.value >= Relationship.KISS.value:
                    scene s130c
                    with dissolve
                    u "I know you stopped kissing me after about a second..."

                    u "But that second was amazing."

                    u "There was something real there and you know it."

            elif lauren.relationship.value >= Relationship.MOVE.value:
                scene s130c
                with dissolve

                u "I don't know why you pulled away when I tried to kiss you..."

                u "Maybe you were scared..."

                u "But there was something real there and you know it."

            else:
                scene s130c
                with dissolve

                u "We had this moment where I wanted to kiss you, but I didn't..."

                u "And I should have. There was something real there. Between us."

            if lauren.relationship.value >= Relationship.KISS.value or kct == "loyal":
                $ laawk = False

                if lauren.relationship.value < Relationship.KISS.value:
                    call screen kct_popup

                $ lauren.relationship = Relationship.GIRLFRIEND

                scene s131 ### Lauren grabbing your hand on the table
                with dissolve

                " "

                scene s130d # Lauren romancing at you holding your hand
                with dissolve

                $ grant_achievement("a_new_beginning")
                    
                la "Maybe you're right."

                scene s130e
                with dissolve

                u "Then let's go on a date. A real date."

                u "How about the movies? Tomorrow night."

                scene s130d
                with dissolve

                la "Okay yeah, let's do it."

                scene s130e
                with dissolve

                u "I'm really sorry, I'm late for class, but I'll see you tomorrow."

                scene s130d
                with dissolve

                la "Alright, see you tomorrow."

                if fighttom and not wintom:
                    scene s130e
                    with dissolve

                    u "(I should probably wash the blood off my face in the restroom before I go to class.)"

            else:
                scene s130f # lauren flustered
                with dissolve

                la "[name], I really like you..."

                la "... but I think we're just better as friends."

                la "I don't wanna jeopardize our friendship."

                menu:
                    "Give me a chance":
                        scene s130g
                        with dissolve

                        u "Lauren, please... give me a chance."

                        scene s130f
                        with dissolve

                        la "[name], I'm sorry. I just don't think we're right for each other."

                        la "Look, I gotta go to class. I'm really sorry."

                        scene s130g
                        with dissolve

                        u "Okay..."

                        if fighttom and not wintom:
                            scene s132 ## empty table, Lauren gone
                            with fade
                            u "(Shit, I forgot I have class right now.)"

                            u "(I should probably wash the blood off my face before I go.)"

                    "You're right":
                        scene s130g
                        with dissolve

                        u "Yeah, you're probably right. Let's just forget about it."

                        scene s130j ## lauren smile
                        with dissolve
                        u "I'm late for class, but I'll see you later, okay?"

                        scene s130h
                        with dissolve

                        la "Yeah, okay."

                        if fighttom and not wintom:
                            scene s130j
                            with dissolve

                            u "(I should probably wash the blood off my face in the restroom before I go to class.)"

        "Let's forget about it":
            $ add_point(KCT.BRO)
            $ laawk = False

            scene s130a
            with dissolve

            if lauren.relationship.value >= Relationship.MOVE.value:
                u "That was uhm... nothing."

                u "Let's just forget that ever happened."

            else:
                u "I mean nothing happened... Maybe it was awkward, but let's just forget about it."

            u "We just spent some nice time in the park together... as friends."

            scene s131
            with dissolve

            " "

            scene s130d
            with dissolve

            la "I'm really glad to have you as a friend, [name]."

            scene s130j
            with dissolve

            u "Yeah, I'm glad too."

            u "I have class right now, but I'll see you later, okay?"

            scene s130h
            with dissolve

            la "Yeah, sounds great."

            if fighttom and not wintom:
                scene s130j
                with dissolve

                u "(I should probably wash the blood off my face in the restroom before I go.)"

    hide screen tutorial
    
    scene s133
    with Fade (1,0,1)

    stop music fadeout 3

label historye: #for compatibility only
label history2:
    play sound "sounds/vibrate.mp3"

    $ josh.messenger.newMessage(_("Dude, I talked to this Aubrey chick the entire night and guess who's number she wanted..."), force_send=True)
    $ josh.messenger.newMessage(_("YOURS"), force_send=True)
    $ josh.messenger.newMessage(_("What a bitch..."), force_send=True)
    $ josh.messenger.addReply(_("Sorry, man. She doesn't know what she's missing."), v2_reply7)
    $ josh.messenger.addReply(_("Sooo, did you give it to her?"), v2_reply8)

    scene s133
    with dissolve

    u "(Time to sit through another boring ass lecture.)"

    play music "music/m16punk.mp3"
    scene s136 ## seeing Imre in lecture room looking apologetic
    with Fade (1,0,1)

    imre "Hey man, about earlier, I-"

    if fighttom and wintom:
        scene s136a
        with dissolve

        u "Imre, I just beat someone up."

        scene s136d #Imre excited
        with dissolve

        imre "Holy shit, was it Grayson?!"

        scene s136e
        with dissolve

        u "Nah, his name's Tom, I think."

        scene s136d
        with dissolve

        imre "What happened?"

        if meetlauren:
            scene s136e
            with dissolve
            u "I don't know, he walked by me on my way to meet with Lauren and just started to insult me."

        else:
            scene s136e
            with dissolve
            u "I don't know, he walked by me on my walk and just started to insult me."

        scene s136b
        with dissolve
        imre "So you just knocked him out?!"

        scene s136c
        with dissolve

        u "I mean no, I just confronted him about it, he pushed me and next thing I know, we're fighting."

        u "And then I just landed a couple good punches and suddenly he was laying on the floor bleeding."

        scene s136h # Imre holding his hands in front of mouth
        with dissolve

        imre "Holy shit, you're a natural, dude."

        scene s136d
        with dissolve

        imre "Train with me. Just once. Just to see if you like it. Please."

        scene s136e
        with dissolve

        u "Fine, I'll train with you. But just one time."

    elif fighttom:
        scene s136b
        with dissolve #Imre surprised

        imre "Dude, did you get beaten up again?! You look like shit!"

        scene s136f # Imre angry
        with dissolve

        imre "Was it another ape??? Tell me who, I'll fuck them up!"

        if meetlauren:
            scene s136g
            with dissolve
            u "Thanks... and I don't know if he was an Ape, but he was also at the party and he started insulting me on my way to meet with Lauren."
        else:
            scene s136g
            with dissolve
            u "Thanks... and I don't know if he was an Ape, but he was also at the party and he started insulting me on my walk."

        scene s136f
        with dissolve
        imre "What did you do?"

        scene s136g
        with dissolve

        u "I confronted him, then he pushed me and then we started fighting."

        scene s136c
        with dissolve

        u "And then he just landed a couple good punches and suddenly I was laying on the floor bleeding."

        scene s136b
        with dissolve
        imre "Shit, man..."

        scene s136c
        with dissolve

        u "Honestly, maybe you're right and I do need to learn to defend myself."

        scene s136b
        with dissolve

        imre "Look, I'm gonna train tomorrow. Why don't you train with me?"

        scene s136c
        with dissolve

        u "Yeah, okay. Thanks Imre."

    else:
        scene s136a
        with dissolve

        u "Imre, another guy tried to fight me today."

        scene s136b
        with dissolve

        imre "Oh shit, what happened? Another Ape?"

        if meetlauren:
            scene s136b
            with dissolve
            u "I don't know if he was an Ape, but he was also at the party and he started insulting me on my way to meet with Lauren."

        else:
            scene s136b
            with dissolve
            u "I don't know if he was an Ape, but he was also at the party and he started insulting me on my walk."

        scene s136b
        with dissolve
        imre "What did you do?"

        scene s136c
        with dissolve
        u "Well I didn't wanna get beaten up again, so I just walked away."

        scene s136b
        with dissolve

        imre "Dude, if you keep this up, you're gonna get treated like crap."

        imre "Look, I'm gonna train tomorrow. Why don't you train with me?"

        scene s136c
        with dissolve

        u "Okay... I guess I'll try it."

    label nextsceneo: #for compatibility only
    scene s134g  ### in lecture room, asian teacher Mr. Lee far away
    with fade

    lee "Welcome to History 101, I'm Mr. Lee."

    lee "I know that some of you have put this class off for multiple years, while others of you are taking it in their first year."

    scene s134 # closer
    with dissolve
    lee "Even though it is unfathomable to me how you could actively try to avoid the most exciting subject in the world..."

    lee "I guess there is something to be said about saving the best for last."

    scene s134a #walking to the side
    with dissolve

    lee "So what is history?"

    scene s134a2 #walking to the side
    with dissolve

    lee "Many people believe that history is about analyzing and understanding the past."

    scene s134b #finger pointing up
    with dissolve
    lee "But it's quite the contrary."

    scene s135 #lee face close up
    with dissolve
    lee "History is looking to the future... but backwards."

    scene s137
    with dissolve
    imre "*Whispers* What is he talking about??" ## Imre laughingly

    scene s137a
    with dissolve # you wispher back laughingly

    u "*Whispers* I don't know."

    scene s134
    with dissolve

    lee "Over the course of this year, you're not just going to learn about history."

    lee "You're going to live history, immerse yourself within it and understand what life was truly like in the past."

    scene s138 # Cameron shouts
    with dissolve

    ca "Yo teach, we get that you love the past, but don't you think the museum wants its shoes back?" ### item

    scene s139 # item closeup
    with dissolve

    "*Class laughing*"

    scene s134c #lee creepy smile
    with dissolve

    lee "What's your name, young man?"

    scene s138a # carmeron sarcasam
    with dissolve

    ca "It's Cameron, teach."

    scene s134c
    with dissolve

    lee "Mr. Cameron, if clothing is what gets you to pay attention in this class, then I suggest you dress up as a historical character for our next lesson."
    lee "As a matter of fact, I insist you do."

    scene s138a # cameron confident
    with dissolve

    ca "Sure, but I'll steal the show."

    scene s134d
    with dissolve

    lee "Perhaps you're right. Everyone should be wearing historically accurate costumes for the next lecture."

    "*Class confused*"

    lee "Come without costume and you've earned your first fail."

    lee "You've got Mr. Cameron to thank for that."

    stop music fadeout 3
    scene clocka
    with fade

    play sound "sounds/clock2.mp3"

    pause (0.5)

    scene clockb
    with dissolve

    pause (0.5)

    scene clockc
    with dissolve

    pause (0.5)

    scene clockd
    with dissolve

    pause (0.5)
    stop sound
    scene clocke
    with dissolve

    scene s140 # You and Imre in hallway
    with Fade (1,0,1)

    play music "music/m11punk.mp3"

    imre "I can't believe he's making us come in costume."

    scene s140a
    with dissolve

    u "Yeah, I don't even have anything I could wear. That's so annoying."

    u "Can we go to the mall later?"

    scene s140
    with dissolve

    imre "Sorry man, I heard the girls' volleyball team is playing and I'm not gonna miss that."

    scene s140a
    with dissolve

    u "I didn't know you were into volleyball."

    scene s140
    with dissolve

    imre "Oh, I'm not."

    scene s140a
    with dissolve

    u "Then why are you-"

    u "Oh..."

    scene s140b
    with dissolve

    imre "Hot girls in shorts getting sweaty? What more could I ask for?"

    scene s140c
    with dissolve

    u "Haha, you're impossible."

    scene s140b
    with dissolve

    imre "I got another class now, I'll see you later."

    scene s141 # Emily in corridor talking to nora
    with Fade (1,0,1)

    u "(Great... I guess it was only a matter of time 'til I saw Emily.)"

    scene s141a # Emily's head turns
    with dissolve

    em "[name]?"

    scene s142 # closeup
    with dissolve

    em "Oh my god, what happened to you?"

    scene s142b
    with dissolve

    no "Looks like he got beaten up."

    if nora.relationship.value >= Relationship.MOVE.value:
        scene s142a # both mouths shut
        with dissolve

        u "I didn't-"

        scene s142b # Nora
        with dissolve

        no "Wait, you're the same kid that hit on me a few days ago."

        scene s142c # emily
        with dissolve

        em "Charming."

        scene s142d

        u "First of all, I was just telling you that you're cute."

        u "Secondly, the guy who punched me came out of nowhere, it wasn't a fair fight."

    else:
        scene s142a # Nora
        with dissolve

        u "I- I didn't get beaten up, okay? A guy just punched me out of nowhere, it wasn't a fair fight."

    scene s142e # Emily empathy
    with dissolve

    em "You know, your eye looks pretty swollen. You really need to get that checked out."

    scene s142f
    with dissolve

    u "It's fine."

    scene s142e
    with dissolve

    em "I'll come with you if you want."

    scene s142f
    with dissolve

    u "Emily, we're not-"

    scene s142g # Nora with fingers pointing no looking at em
    with dissolve

    no "Look, I'm sensing some weird energy between you two, so I'ma leave."

    no "Bye Emily."

    scene s142j # no looking at you em looking at no
    with dissolve

    no "Bye weirdo."

    scene s142k # no walking away
    with dissolve

    u "What? I didn't even-"

    em "I'll see you later, Nora."

    scene s144 # only emily
    with fade

    em "Come on, let's-"

    scene s144a
    with dissolve

    u "Emily, we're not friends. You cheated on me."

    scene s144b
    with dissolve

    em "[name], I know I fucked up. I'm really sorry, okay?"

    em "We hit a rough patch and I was drunk and..."

    em "I just miss us. Even if it's just as friends."

    em "Can we please just hang out?"

    menu:
        "Okay, I guess":
            $ forgiveemily = True
            $ add_point(KCT.BOYFRIEND)

            scene s144c
            with dissolve

            u "Fine, let's go then."

            scene s144d #em happy
            with dissolve

            em "Really? Where do you wanna go?"

            scene s144e
            with dissolve

            u "I thought we're going to the doctor's office? Or are you gonna tell me that your concern was merely an attempt to hang out with me?"

            scene s144d
            with dissolve

            em "Right, of course not. Let's go."

            jump bo_ad

        "No, sorry":
            $ emilyandben = True
            $ forgiveemily = False
            $ add_point(KCT.TROUBLEMAKER)

            scene s144c
            with dissolve

            u "No Emily."

            scene s144c # em sad mouth close
            with dissolve

            u "I can't just forgive you like that. You don't know what you put me through."

            scene s144b
            with dissolve

            em "Oh..."

            em "I'll go then..."

            scene s144c
            with dissolve

            u "Goodbye, Emily."

            jump bo_bd

label bo_ad:

    play music "sounds/bus.mp3"

    scene carback

    show s145far # bus with emily, animation???? seeing obth bus sounds
    with Fade (1,0,1)

    pause 0.5

    hide s145far
    show s145
    with dissolve

    em "Sooo... did you text your new girlfriend that you're hanging out with your ex?"

    menu:
        "Yeah, of course. (joke)":
            $ add_point(KCT.TROUBLEMAKER)

            hide s145
            show s145a
            with dissolve

            u "Yeah, of course I did. I tell her everything."

            hide s145a
            show s145b
            with dissolve

            em "Oh... okay. That's- that's good. You should tell her stuff like this."

            hide s145b
            show s145bl
            with dissolve

            u "*Laughs* Emily, I'm kidding. I'm still single, I mean we only broke up a couple months ago."

            hide s145bl
            show s145c
            with dissolve

            em "[name], you gotta stop messing with me, haha."

            hide s145c
            show s145d
            with dissolve

            u "Oh come on, don't act like you didn't miss this."

            hide s145d
            show s145c
            with dissolve

            em "Maybe a little bit."

        "I'm still single":
            $ add_point(KCT.BOYFRIEND)

            hide s145
            show s145e
            with dissolve

            u "Believe it or not, I'm still single."

            hide s145e
            show s145d
            with dissolve

            u "I mean we only broke up a couple months ago."

            hide s145d
            show s145f
            with dissolve

            em "I guess you're right. I was just... you know, curious."

    hide s145c
    hide s145f
    show s145d
    with dissolve

    label bp_bd: #for compatibility only
    u "Hey, you remember the time you had your wisdom teeth pulled out and you looked like a hamster for 2 weeks straight?"

    hide s145d
    show s145c
    with dissolve

    em "Are you ever gonna stop bringing that up?"

    menu:
        "It was adorable":
            $ add_point(KCT.BOYFRIEND)

            hide s145c
            show s145d
            with dissolve #u looking romantic


            u "No way, you looked so adorable."

            hide s145d
            show s145f
            with dissolve
            em "What was adorable was how much you cared for me. I remember you bringing me a care package full of like a hundred different soups."

            em "It was so thoughtful."

        "It was so funny":
            $ add_point(KCT.BRO)

            hide s145c
            show s145d
            with dissolve

            u "It was sooo funny though."

            hide s145d
            show s145c
            with dissolve

            em "You're the one to talk, your face is literally swollen up right now."

            hide s145c
            show s145d
            with dissolve

            u "It's not my whole face, it's just my eye."

            u "Plus, it looks badass."

            hide s145d
            show s145c
            with dissolve

            em "Haha, I'm not sure who told you that."

    label bq_bd: #for compatibility only
    stop music
    play sound "sounds/busstop.mp3"

    hide s145c
    hide s145f
    show s145j
    with dissolve

    u "Shit, we gotta get off at this stop."

    stop sound

    scene s146far # doctors reception
    with Fade (1,0,1)

    play music "music/m16punk.mp3"

    u "Hey there, you accept walk-ins right?"

    u "I need someone to look at my eye."

    scene s146a # giving you forms
    with dissolve

    ben "Yeah, sure thing. Fill out these forms and then take a seat in the waiting room and I'll let you know when Dr. Ehrmantraut can slot you in."

    scene s147 #em pointing
    with dissolve

    em "Hey, I've seen you before, you went to school with my sister."

    em "Benjamin, right?"

    scene s146b
    with dissolve

    ben "Oh, I remember. You're Hannah's sister."

    scene s147a
    with dissolve

    em "Didn't you wanna become a lawyer?"

    scene s146c ## hands shrugigng to the side like IDK
    with dissolve

    ben "I mean yeah, but technically - I didn't get into law school."

    scene s146b
    with dissolve

    ben "But this is actually a really good job, you know."

    ben "It pays well. And I get benefits. Dental benefits."

    ben "So really, dream job."

    scene s147b # em smiling
    with dissolve

    em "Well, I'm glad you found something you like."

    scene s147c # em looking at you
    with dissolve

    em "Okay, I'm gonna go sit down in the waiting room while you fill out your forms."

    scene s147d
    with dissolve

    u "Cool, I'll be done in a second."

    # benjamin leaning over the counter while em goes to wait and you fill out forms

    scene s148
    with fade

    ben "So uhhh, are you hitting that, or can a bro make a move?"

    scene s148a # u lookiing up
    with dissolve

    ben "You know, even if you are hitting that... I'm totally fine with like a dual type of arrangement."

    scene s148b
    with dissolve

    u "Dude... aren't you like 30 or something?"

    scene s148a2
    with dissolve

    ben "What? I'm 24."

    menu:
        "Sure, knock yourself out":
            $ emilyandben = True
            $ add_point(KCT.BRO)

            scene s148b
            with dissolve

            $ grant_achievement("over_it")
                
            u "Sure, knock yourself out, man. We're not an item."

            scene s148d
            with dissolve

            ben "Thanks, bro! I'll think of you when I'm doing her."

            scene s148e
            with dissolve

            u "Please don't..."

        "Stay away from her":
            $ emilyandben = False
            $ add_point(KCT.BOYFRIEND)

            scene s148b
            with dissolve

            u "Just - just stay away from her, okay?"

            scene s148a
            with dissolve

            ben "Fine, bro. Sorry for asking."

    label br_bd: #for compatibility only
    scene s149 # emily in waiting room
    with fade

    em "All done with the forms?"

    menu:
        "Tell Emily about Benjamin":
            $ add_point(KCT.BOYFRIEND)
            $ add_point(KCT.TROUBLEMAKER)

            scene s149a
            with dissolve

            u "Yeah, but while I was doing it Benjamin asked me if he could make a move on you."

            scene s150 # em close up flirting
            with dissolve

            em "Oh really, are you my guardian now?"

            scene s150a # em curious
            with dissolve
            em "What did you say?"

            if not emilyandben:
                scene s150b
                with dissolve

                u "Uhm... I told him off."

                u "You know, just to protect you from having to deal with a creep."

                scene s150
                with dissolve

                em "Oh, so you're \"protecting\" me now, huh?"

                scene s150c # em flirting close
                with dissolve

                u "Oh shut up, if you wanna give him your phone number and have the worst date of your life, you're free to do so."

                scene s150d
                with dissolve

                em "Haha, I think I'm good."

            else:
                scene s150b
                with dissolve

                u "I told him he should."

                u "I mean there's no way you'd go for him anyways."

                scene s150d
                with dissolve
                em "Haha, he is kinda cute."

                em "Plus he has a job."

                scene s150e
                with dissolve

                u "As a receptionist."

        "Don't tell Emily":
            $ add_point(KCT.BRO)

            scene s149a
            with dissolve

            u "Yeah, I did. I guess now we gotta wait."

            u "What did you think of Benjamin by the way?"

            scene s150a
            with dissolve

            em "What do you mean?"

            scene s150b
            with dissolve

            u "You know, as a guy."

            scene s150d
            with dissolve

            em "I guess he's kinda cute, but also a bit weird."

            scene s150a
            with dissolve

            em "Why are you asking?"

            scene s150b
            with dissolve

            u "Just wondering."

    label bs_bd: #for compatibility only
    ### door opening benjamin coming in
    scene s151
    with dissolve

    ben "Dr. Ehrmantraut is now ready for you."

    scene s150d
    with dissolve

    em "I'll wait here, I saw a bunch of Vogues I wanna dig into."

    scene s152far ## doctors office
    with Fade (1,0,1)

    ehr "Okay, looking at you I'm gonna assume you're here because of your black eye?"

    scene s152far1
    with dissolve

    u "(Holy shit, I thought Dr. Ehrmantraut was a guy.)"

    scene s152far2
    with dissolve
    u "Uhh... yeah, my friend dragged me here in order to get it looked at."

    scene s152
    with dissolve

    ehr "Alright, let me have a closer look and see if there's anything unusual about it."

    scene s152b ## dr bending over to inspect your eye
    with dissolve

    ehr "Hmm..."

    ehr "It all looks fine to me."

    scene s152c
    with dissolve

    ehr "When did this happen?"

    scene s152d
    with dissolve

    u "Yesterday. I got punched in the face out of nowhere."

    scene s152c
    with dissolve

    ehr "Does it hurt a lot? I could prescribe you a week's worth of painkillers."

    scene s152d
    with dissolve

    u "(Why can't life be more like porn...? Sex with her would take any pain away.)"

    u "Uhm... no, that's fine. It doesn't hurt too badly."

    scene s152c
    with dissolve

    ehr "Well then, your face should be back to normal in a week. If it doesn't get better, please come see me again."

    scene s152d
    with dissolve

    u "Thanks, will do."

    u "(Now I really hope it doesn't get better...)"

    scene s153 ## em in waiting room reading vogue
    with Fade (1,0,1)

    u "Are you ready to go?"

    scene s153a
    with dissolve

    em "Yeah, let's leave."

label bo_bd:
    stop music fadeout 3

    scene s154 ## text from aubrey & you walking back alone
    with Fade (1,0,1)

    if forgiveemily:
        u "(Even though that just cost me almost a hundred dollars, it was kinda nice to spend time with Emily.)"

        u "(Still... I don't know if I can ever fully forgive her for what she did.)"

    # text from aubrey
    play sound "sounds/vibrate.mp3"

    $ aubrey.messenger.newMessage(_("Hey,\nJosh gave me your number\n\nI hope your face is feeling better after the shit that Grayson pulled..."), force_send=True)
    $ aubrey.messenger.newMessage(_("He's not even dating Chloe and you guys didn't even do anything so I don't know what he was thinking.\n\nAnyway, do you wanna like... hang out tomorrow?"), force_send=True)
    $ aubrey.messenger.addReply(_("Wait they're not dating?"), v2_reply11)
    $ aubrey.messenger.addReply(_("My day tomorrow is quite full, but how about today?\n\nI need to buy a costume."), v2_reply12)

    u "(Oh, I just got a message.)"

    label repeatc:
        if aubrey.messenger.replies:
            call screen phone
        if aubrey.messenger.replies:
            u "(I should check my messages.)"
            jump repeatc
    
    play music "music/mlove.mp3"

    scene s155
    with fade
    pe "Uhm... excuse me."

    pe "I- I know you-"

    scene s155a
    with dissolve

    u "Let me guess, you saw me get punched in the face at a party."

    scene s155
    with dissolve

    pe "Uhm, no, but that would explain your swollen eye."

    pe "You're in my History 101 class."

    scene s155a
    with dissolve

    u "With Mr. Lee?"

    scene s155b # pe smiling
    with dissolve

    pe "Yes. What other History 101 class is there?"

    scene s155c
    with dissolve

    u "Fair point. So... what's up? How can I help you?"

    scene s155
    with dissolve

    pe "Oh, well I saw you and I thought to myself \"Hey, I know this person and I should talk to him.\""

    scene s155a
    with dissolve
    u "Uhm, okay so-"

    scene s155
    with dissolve

    pe "And then I thought \"But what if I'm disturbing him?\" So I decided not to say anything."

    scene s155a
    with dissolve

    u "Well you're not-"

    scene s155
    with dissolve

    pe "But then I was like \"Penelope, you need to start talking to people at some point\" and then I approached you."

    scene s155a
    with dissolve

    u "Okay... I'm [name] and-"

    scene s155d #pe scared
    with dissolve

    pe "Oh god, is it weird? Did I make it weird?"

    pe "I should leave, this was a bad idea. Good bye."

    scene s155e # penelope turns around
    with dissolve

    pause 0.5

    scene s155f # you grab her arm
    with hpunch

    u "Wait."

    scene s155g # penelope turns head
    with dissolve

    u "There's no need to be nervous."

    u "So your name is Penelope right?"

    scene s155h
    with dissolve

    pe "Yes."

    scene s155g
    with dissolve

    u "So, what did you mean by \"you need to start talking to people at some point\"? Are you a freshman?"

    scene s155 # pe turns back around
    with dissolve

    pe "No, I'm a junior, but I just transferred to San Vallejo 'cause I got kicked out of my old college."

    pe "And my dad paid a lot of money so I could go to my old college and now he's super mad and he said I'll have to get a job 'cause he's gonna cut my money off."

    pe "And then I called my mom and said \"Mom, help! Dad is going crazy!\" But my mom was like \"You need to talk to him yourself.\""

    pe "I mean they don't really talk to each other since the divorce and it's like-"

    scene s155a
    with dissolve

    u "Okay, calm down. You-"

    scene s155d
    with dissolve

    pe "Oh god, am I oversharing again? I am, aren't I?"

    scene s155d2
    with dissolve

    u "It's all good. It's just... Why did you get kicked out of your old college?"

    scene s155
    with dissolve

    pe "Oh, I don't wanna say."

    scene s155a
    with dissolve

    u "Really? That's where you draw the line of not sharing?"

    scene s155
    with dissolve

    pe "Sorry but... it's bad, really bad."

    scene s155a
    with dissolve

    u "Come on, you can tell me."

    scene s155
    with dissolve

    pe "I'm really sorry, but I can't tell you. Please stop pressing me about it."

    scene s155a
    with dissolve

    u "Ugh... alright."

    play sound "sounds/vibrate.mp3"

    $ aubrey.messenger.newMessage(_("Hey, are you nearby?"), force_send=True)
    $ aubrey.messenger.addReply(_("Yeah, I'm just on my way, I'll be right there."), v2_reply13)
    $ aubrey.messenger.addReply(_("Sorry, something came up and I can't make it."), v2_reply14)

    u "(Fuck, I totally forgot about Aubrey. I guess it's time to make a decision.)"

    label repeatg:
        if aubrey.messenger.replies:
            call screen phone
        if aubrey.messenger.replies:
            u "(Aubrey's waiting for me, I need to let her know whether I'm coming or not.)"
            jump repeatg

    if costumeaubrey:
        u "Penelope, I'm really sorry, but I have to go and meet my friend. It was nice seeing you."

        scene s155
        with dissolve

        pe "Oh, I understand. I guess I'll see you around."

        scene s155a
        with dissolve

        u "Yeah, definitely. See you later."

        stop music fadeout 3

        jump csaub

    else:
        u "Sorry, I just had to reply to someone."

        u "Hey, do you also need a costume for Mr. Lee's class?"

        scene s155b
        with dissolve

        pe "Yeah, I was just on my way to buy one."

        scene s155c
        with dissolve

        u "Wanna go together? I need one as well."

        scene s155b
        with dissolve

        pe "I'd love that!"

        stop music fadeout 3

        jump cspe

label csaub:
    scene s156
    with Fade (1,0,1)
    play sound "sounds/knock.mp3"
    pause 1
    play sound "sounds/dooropen.mp3"

    scene s157
    with dissolve
    pause 0.75
    play music "music/m7punk.mp3"


    no "Oh, look who it is."

    scene s157a # nora shouting back
    with dissolve

    no "Aubrey, your lover boy is here."

    u "Thanks, for the kind introduction."

    scene s157 # fake smile
    with dissolve

    no "You're welcome."

    play sound "sounds/dooropen.mp3"

# door open sound
    scene s157d # aubrey appears
    with dissolve

    au "Hey."

    scene s157f
    with dissolve

    u "Hey, you ready to go?"

    scene s157e
    with dissolve

    au "Yeah, I would show you the house, but we don't have that much time 'cause I've got dance practice later."

    au "Plus there's a bunch of girls in their underwear in here right now. You wouldn't wanna see that."

    scene s157f
    with dissolve

    u "Yeah, that does sound horrible."

    scene s157e
    with dissolve

    au "Haha, I thought so. Let's go then."

    stop music fadeout 3

    scene s158 # at the clothing store # showing aubrey and u from behind
    with Fade (1,0,1)

    u "Didn't you say this was a costume shop?"

    play music "music/mindie1.mp3"

    queue music [ "music/mindie2.mp3", "music/mindie3.mp3" ]

    au "It was! At least the last time I was here."

    scene s159 # au talking to store ev
    with dissolve

    au "Excuse me, wasn't this a costume shop?"

    scene s159a
    with dissolve

    ev "Well, we were last year, but after Halloween was over sales plummeted."

    ev "So the owners had this crazy idea of Halloween in January, but the surprising increase of in-store injuries and following lawsuits quickly made it go bust."

    ev "We had to put in a new floor and change the branding, so now we just sell regular clothing in all months of the year."

    scene s159b
    with dissolve

    au "Damn, this was the only costume store nearby..."

    scene s159c
    with dissolve

    ev "I can check if we still have some costumes in the back, but it'll be a limited selection."

    scene s159d # aubrey smiloing
    with dissolve

    au "Yeah, that'd be amazing, thank you so much."

    scene s161 # in changing rooms room
    with Fade (1,0,1)

    pause 0.5

    scene s161a # ev comming with box
    with dissolve

    ev "So in this box are all the remaining costumes we have, I hope that's enough."

    scene s161b # puts box down
    with dissolve

    ev "Let me know if there's anything else you need."

    u "Thank you."

    scene s162a # looking at aubrey
    with dissolve

    u "Okay, let's have a look at some of these."

    scene s162
    with dissolve

    au "If there's any female ones in there, I'm trying them on."

    call screen costumes # choice between 3 costumes button try and button buy below, every time you try, Aubrey comes out in a different outfit, you can peek while changing

    # chnace to flirt with ev
    # chance to get caught when risky peeking

############ VIKING AUBREY
label try1: # viking
    if "viking" in costumetried:
        jump try1done

    else:
        $ costumetried.add("viking")
        jump try1new

label try1done:
    scene s163
    with Fade (1,0,1)

    u "(Yeah- still look the same as a viking as I did before.)"

    u "(I should really just choose a costume to buy.)"

    call screen costumes


label try1new:
    $ v2_outfits += 1

    scene s163 # in changing room
    with Fade (1,0,1)

    u "(Alright, rocking the Viking look.)"

    u "(I wonder what Aubrey is changing into.)"

    menu:
        "Peek":
            $ add_point(KCT.TROUBLEMAKER)

            scene s164 # Aubrey changing bad view
            with dissolve

            u "(Holy shit, if I could just stick my head through a bit further, I could get a way better view.)"

            menu:
                "Risk it":
                    if config_censored:
                        call screen censoredPopup("v2_nsfwSkipLabel1")

                    $ v2_caughtpeeking = renpy.random.choice([True, False])

                    if not v2_caughtpeeking:
                        scene s164a # Aubrey changing good view
                        with dissolve

                        u "(Oh my god, her ass is perfect.)"

                        u "(I should stop peeking now, or I'll get caught.)"

                    else:
                        jump caughta

                "Stop peeking":
                    pass

        "Don't peek":
            $ add_point(KCT.BOYFRIEND)

label v2_nsfwSkipLabel1:
    scene s163
    with dissolve

    u "(Let's see what Aubrey thinks of this costume.)"

    scene s165 # showing u and aubrey in costume
    with Fade (1,0,1)

    pause 0.5

    scene s166 # aubrey close up
    with dissolve

    au "Oh my god, you make an adorable Viking."

    scene s166a
    with dissolve

    u "Really? Adorable? How about hot?"

    scene s166b # flirty
    with dissolve

    au "Haha, what do you think of my outfit?"

    menu:
        "It's kinda hot":
            $ add_point(KCT.BOYFRIEND)

            scene s166c
            with dissolve

            u "I'm not gonna lie, it's kinda hot."

            u "You could be like my Viking queen."

            scene s166b
            with dissolve

            au "I think you've put me in the wrong time period, buddy."

            if v2_outfits < 3:
                scene s166
                with dissolve

                au "Let's try some of the other outfits."

            else:
                scene s166
                with dissolve

                au "Have you decided which one to buy yet?"

        "It's definitely something":
            $ add_point(KCT.BRO)

            scene s166c
            with dissolve

            u "I mean, it's definitely something."

            u "I'm not sure if you should replace your everyday clothes with it though."

            scene s166
            with dissolve

            if v2_outfits < 3:
                au "I'll guess I'll have to try some of the other outfits then."

            else:
                au "Have you decided which one to buy yet?"

    call screen costumes
######### VIKING AUBREY

############ KNIGHT AUBREY
label try2:
    if "knight" in costumetried:
        jump try2done
        
    else:
        $ costumetried.add("knight")
        jump try2new

label try2done:
    scene s167
    with Fade (1,0,1)

    u "(I mean looking at the Knight costume now, I notice that...)"

    u "(... it looks exactly the same as before.)"

    call screen costumes


label try2new:
    $ v2_outfits += 1

    scene s167 # in changing room
    with Fade (1,0,1)

    u "(I definitely do not fit into these shoulder pads.)"

    u "(Aubrey is changing right next to me...)"

    menu:
        "Peek":
            $ add_point(KCT.TROUBLEMAKER)

            scene s168 # Aubrey changing bad view
            with dissolve

            u "(Wow... if I could just stick my head through a bit further, I could get a way better view.)"

            menu:
                "Risk it":
                    if config_censored:
                        call screen censoredPopup("v2_nsfwSkipLabel2")

                    $ v2_caughtpeeking = renpy.random.choice([True, False])

                    if not v2_caughtpeeking:
                        scene s168a # Aubrey changing good view
                        with dissolve

                        u "(Damn, what I wouldn't give to touch her ass right now.)"

                        u "(I should stop peeking now, or I risk getting caught.)"

                    else:
                        jump caughtb

                "Stop peeking":
                    pass

        "Don't peek":
            $ add_point(KCT.BOYFRIEND)

label v2_nsfwSkipLabel2:
    scene s167
    with dissolve

    u "(Time to show this to Aubrey)"

    scene s169 # showing u and aubrey in costume
    with Fade (1,0,1)

    pause 0.5

    scene s170 # aubrey close up flirting
    with dissolve

    au "Damn, I like your outfit."

    scene s170a
    with dissolve

    u "Well thank you, milady."

    u "Yours is uhhh..."

    menu:
        "looking mighty fine":
            $ add_point(KCT.BOYFRIEND)

            u "...looking mighty fine as well."

            scene s170b # questioning
            with dissolve

            au "Is it weird that you talking like that kinda turns me on?"

            scene s170c
            with dissolve

            u "Wait really? Should I keep going?"


            scene s170d # aubrey laughing
            with dissolve

            au "Hahaha, no. I was just joking."

            if v2_outfits < 3:
                au "Let's switch outfits."

            else:
                au "Are you gonna buy this one?"

        "certainly practical":
            $ add_point(KCT.BRO)

            u "... certainly practical."

            scene s170d
            with dissolve

            au "That is the single greatest compliment I think I've ever received."

            scene s170e
            with dissolve

            u "I am kinda known for my charm."

            scene s170
            with dissolve

            au "Really? I thought it was for getting punched in the face."

            scene s170a
            with dissolve

            u "Wow, low blow."

            scene s170d

            if v2_outfits < 3:
                au "Let's switch outfits."

            else:
                au "So are you gonna buy this one?"

    call screen costumes
######### KNIGHT AUBREY

    ### aubrey third costume

    # okay this one is literally just a bra and panties. I'm not wearing that.
    # oh come on, I wanna see! # popularity check

############ COWBOY AUBREY
label try3:
    if "cowboy" in costumetried:
        jump try3done
        
    else:
        $ costumetried.add("cowboy")
        jump try3new

label try3done:
    scene s171
    with Fade (1,0,1)

    u "(The more I wear this, the more I feel like I would make a great cowboy.)"

    call screen costumes

label try3new:
    $ v2_outfits += 1

    scene s171 # in changing room
    with Fade (1,0,1)

    u "(Yeehaw!)"

    u "(I can hear Aubrey sliding her clothes off...)"

    menu:
        "Peek":
            $ add_point(KCT.TROUBLEMAKER)

            scene s172 # Aubrey changing bad view
            with dissolve

            u "(Fuck... if I could just stick my head through a bit further, I could get a way better view.)"

            menu:
                "Risk it":
                    if config_censored:
                        call screen censoredPopup("v2_nsfwSkipLabel3")

                    $ v2_caughtpeeking = renpy.random.choice([True, False])

                    if not v2_caughtpeeking:
                        scene s172a # Aubrey changing good view
                        with dissolve

                        u "(In all fairness, whenever I watch porn, the person getting caught spying gets to fuck the girl right afterwards.)"

                        u "(Still... I better stop peeking now, it's too risky.)"
                    else:
                        jump caughtc

                "Stop peeking":
                    pass

        "Don't peek":
            $ add_point(KCT.BOYFRIEND)

label v2_nsfwSkipLabel3:
    scene s171
    with dissolve

    u "Man she's gonna love this costume."

    scene s199 # showing u in front of closed stall with Aubrey
    with Fade (1,0,1)

    u "Aubrey? Are you coming out?"

    au "This costume is literally just historic lingerie."

    show screen tutorial([
        "When people make important decisions on how they feel about you, they consider what kind of a person you are.",
        "Your Key Character Trait (Loyal, Popular or Confident) has a strong influence on how other characters react to your behavior.",
        "Some people value a popular leader, some care more about loyalty than status and some are drawn to confidence.",
        "Your decisions matter and have long time effects, as you can only have one KCT at a time. So think about what kind of person you want to be."
    ])

    au "I'm not showing you this, haha."

    menu:
        "Oh come on":
            hide screen tutorial
            $ add_point(KCT.TROUBLEMAKER)

            u "Oh come on, Aubrey. I wanna see."

            if kct == "popular":
                call screen kct_popup
            else:
                au "Sorry but... I'm gonna get dressed again."

                u "Alright, fine."

                jump by_bd

            au "Okay, fine. Just for you."

            scene s175 # showing u in costume and aubrey in custome
            with Fade (1,0,1)

            pause 0.5

            scene s176a # aubrey like  I told you
            with dissolve

            u "Holy shit, you weren't exaggerating. That is revealing."

            scene s176
            with dissolve

            au "See what I mean now? Can I get dressed again?"

            scene s176a
            with dissolve

            u "You sure you don't wanna keep this on for the rest of the day?"

            scene s176b # aub laughing
            with dissolve

            au "Haha yes. I hope you got a good look, 'cause I'm changing back."

            au "Also, this cowboy outfit is probably the worst thing I've ever seen anyone wear."

            au "So let's get out of these outfits."

            call screen costumes

        "Fine":
            hide screen tutorial
            $ add_point(KCT.BOYFRIEND)

            u "Alright, fine."

            u "Then get dressed quickly, so that you can see my costume."

            au "Yeah, just give me a minute."

label by_bd:
    scene s173 # showing u in costume and aubrey in regular clothes
    with Fade (1,0,1)

    pause 0.5

    scene s174 # aubrey close up laughing
    with dissolve

    au "Oh god, that looks so bad on you."

    scene s174a
    with dissolve

    u "What?? I considered cowboy to be a serious career path for me after I saw myself in this outfit."

    scene s174
    with dissolve

    au "Oh no. Just whatever you do, do not buy this costume."

    au "I think you should get out of that as quickly as you can."

    call screen costumes

######################SHOPPING WITH PENELOPE shop2
label cspe:
    scene s158v2
    with Fade (1,0,1)

    u "I swear Google maps said this was a costume shop."

    play music "music/mindie1.mp3"

    queue music [ "music/mindie2.mp3", "music/mindie3.mp3" ]

    pe "Maybe we can ask the lady over there, she seems to work here."

    scene s159v2
    with dissolve

    pe "Excuse me, is this not a costume shop?"

    scene s159a
    with dissolve

    ev "Well, we were last year, but after Halloween was over sales plummeted."

    ev "So the owners had this crazy idea of Halloween in January, but the surprising increase of in-store injuries and following lawsuits quickly made it go bust."

    ev "We had to put in a new floor and change the branding, so now we just sell regular clothing in all months of the year."

    scene s159bv2
    with dissolve

    pe "Oh, wow, well that's very unfortunate. We were looking to buy some costumes."

    scene s159c
    with dissolve

    ev "If you want, I can check if we still have some in the back, but it'll be a limited selection."

    scene s159dv2
    with dissolve

    pe "Yes, that would be amazing. We'd really appreciate it, thank you."

    scene s161v2 # in changing rooms room
    with Fade (1,0,1)

    pause 0.5

    scene s161av2 # ev comming with box
    with dissolve

    ev "So in this box are all the remaining costumes we have, I hope that's enough."

    scene s161b # puts box down
    with dissolve

    ev "Let me know if there's anything else you need."

    u "Thank you."

    scene s162av2
    with dissolve

    u "Okay, let's have a look at some of these."

    scene s162v2
    with dissolve

    pe "I'm actually really excited to buy a costume."
    pe "At my old college we weren't even allowed to wear costumes on Halloween, because of the dress code."

    call screen costumes # choice between 3 costumes button try and button buy below, every time you try, Aubrey comes out in a different outfit, you can peek while changing

    # chnace to flirt with ev
    # chance to get caught when risky peeking

############ VIKING PENELOPE shop3
label try1p: # viking
    if "viking" in costumetried:
        jump try4done

    else:
        $ costumetried.add("viking")
        jump try4new

label try4done:
    scene s163
    with Fade (1,0,1)

    u "(Yeah- still look the same as a Viking as I did before.)"

    u "(I should really just choose a costume to buy.)"

    call screen costumes

label try4new:
    $ v2_outfits += 1

    scene s163 # in changing room
    with Fade (1,0,1)

    u "(Alright, rocking the Viking look.)"

    u "(I wonder what Penelope is changing in to.)"

    menu:
        "Peek":
            $ add_point(KCT.TROUBLEMAKER)

            scene s183 # penelope changing bad view
            with dissolve

            u "(Holy shit, if I could just stick my head through a bit further, I could get a way better view.)"

            menu:
                "Risk it":
                    if config_censored:
                        call screen censoredPopup("v2_nsfwSkipLabel4")

                    $ v2_caughtpeeking = renpy.random.choice([True, False])

                    if not v2_caughtpeeking:
                        scene s183a # pen changing good view
                        with dissolve

                        u "(Oh my god, her ass is so nice.)"

                        u "(I should stop peeking now, or I'll get caught.)"

                    else:
                        jump caughtd

                "Stop peeking":
                    pass

        "Don't peek":
            $ add_point(KCT.BOYFRIEND)

label v2_nsfwSkipLabel4:
    scene s163
    with dissolve

    u "(Let's see what Penelope thinks of this costume.)"

    scene s179far # showing u and pen in costume
    with Fade (1,0,1)

    pause 0.5

    scene s179 # pen close up
    with dissolve

    pe "Oh I don't think you should get that costume."

    scene s179a
    with dissolve

    u "Why? Do I look too dashing?"

    scene s179
    with dissolve

    pe "No, it's just that Vikings didn't actually have horns on their helmets."

    pe "And Mr. Lee said that the costumes should be historically accurate."

    scene s179a
    with dissolve

    u "Oh, right. Totally."

    scene s179
    with dissolve
    pe "So uhm... what do you think of my outfit?"

    menu:
        "You look beautiful":
            $ add_point(KCT.BOYFRIEND)

            scene s179a
            with dissolve

            u "You look beautiful. Do you like it?"

            scene s179b # romantic smile
            with dissolve

            pe "Awww, thank you."

            pe "Yeah, it's kinda cool."

            if v2_outfits < 3:
                pe "Should we try some other outfits?"

            else:
                pe "Are you ready to buy an outfit?"

        "I guess it's nice":
            $ add_point(KCT.BRO)

            scene s179a
            with dissolve

            u "I guess it's kinda nice. What do you think?"

            scene s179b # romantic smile
            with dissolve

            pe "I like it, but I'm not sure."

            if v2_outfits < 3:
                pe "Should we try some other outfits?"

            else:
                pe "Are you ready to buy an outfit?"

    call screen costumes

######### VIKING PEN

############ KNIGHT PEN shop4
label try2p:

    if "knight" in costumetried:
        jump try5done
        
    else:
        $ costumetried.add("knight")
        jump try5new

label try5done:
    scene s167
    with Fade (1,0,1)

    u "(I mean looking at the Knight costume now, I notice that...)"

    u "(... it looks exactly the same as before.)"

    call screen costumes

label try5new:
    $ v2_outfits += 1

    scene s167 # in changing room
    with Fade (1,0,1)

    u "(I definitely do not fit into these shoulder pads.)"

    u "(Penelope is changing right next to me...)"

    menu:
        "Peek":
            $ add_point(KCT.TROUBLEMAKER)

            scene s183 # pen changing bad view
            with dissolve

            u "(Wow... if I could just stick my head through a bit further, I could get a way better view.)"

            menu:
                "Risk it":
                    if config_censored:
                        call screen censoredPopup("v2_nsfwSkipLabel5")

                    $ v2_caughtpeeking = renpy.random.choice([True, False])

                    if not v2_caughtpeeking:
                        scene s183a
                        with dissolve

                        u "(Damn, what I wouldn't give to touch her ass right now.)"

                        u "(I should stop peeking now, or I risk getting caught.)"
                    else:
                        jump caughte

                "Stop peeking":
                    pass

        "Don't peek":
            $ add_point(KCT.BOYFRIEND)

label v2_nsfwSkipLabel5:
    scene s167
    with dissolve

    u "(Time to show this to Penelope)"

    scene s181 # showing u and penelope in costume
    with Fade (1,0,1)

    pause 0.5

    scene s182 # pen happy
    with dissolve

    pe "Oh, you're a knight!"

    scene s182a
    with dissolve

    u "Yeah and you're like a female with shoulder pads?"

    scene s182
    with dissolve

    pe "Sir, your perception skills are outstanding."

    scene s182a
    with dissolve

    u "Well thank you, milady."

    scene s182
    with dissolve

    pe "You know, our costumes fit quite well together."

    menu:
        "Flirt":
            $ add_point(KCT.BOYFRIEND)

            u "Yeah, maybe it's like the costume of two lovers, you know... historically speaking."

            scene s182
            with dissolve

            pe "Haha, I'm sure that's the case."

            if v2_outfits < 3:
                pe "Let's continue, I wanna try another outfit."

            else:
                pe "Are you ready to buy an outfit?"

        "Agree":
            $ add_point(KCT.BRO)

            u "Yeah, it would be a cool partner costume."

            scene s182
            with dissolve

            pe "That's a sweet idea. Maybe we can do something like that."

            if v2_outfits < 3:
                pe "But let's check out the other outfits first."

            else:
                pe "Would you be ready to buy an outfit?"

    call screen costumes

######### KNIGHT PEN

    ### aubrey third costume

    # okay this one is literally just a bra and panties. I'm not wearing that.
    # oh come on, I wanna see! # popularity check

############ COWBOY PEN shop5
label try3p:
    if "cowboy" in costumetried:
        jump try6done
        
    else:
        $ costumetried.add("cowboy")
        jump try6new

label try6done:
    scene s171
    with Fade (1,0,1)

    u "(The more I wear this, the more I feel like I would make a great cowboy.)"

    call screen costumes

label try6new:
    $ v2_outfits += 1

    scene s171 # in changing room
    with Fade (1,0,1)

    u "(Yeehaw!)"

    u "(I can hear Penelope sliding her clothes off...)"

    menu:
        "Peek":
            $ add_point(KCT.TROUBLEMAKER)

            scene s180 # pen changing bad view
            with dissolve

            u "(Fuck... if I could just stick my head through a bit further, I could get a way better view.)"

            menu:
                "Risk it":
                    if config_censored:
                        call screen censoredPopup("v2_nsfwSkipLabel6")

                    $ v2_caughtpeeking = renpy.random.choice([True, False])

                    if not v2_caughtpeeking:
                        scene s180a # pen changing good view
                        with dissolve

                        u "(In all fairness, whenever I watch porn, the person getting caught spying gets to fuck the girl right afterwards.)"

                        u "(Still... I better stop peeking now, it's too risky.)"
                    else:
                        jump caughtf

                "Stop peeking":
                    pass

        "Don't peek":
            $ add_point(KCT.BOYFRIEND)

label v2_nsfwSkipLabel6:
    scene s171
    with dissolve

    u "Man she's gonna love this costume."

    scene s199
    with Fade (1,0,1)

    u "Penelope? Are you coming out?"

    pe "Well I was trying on a costume, but after seeing I realize that it shows way too much skin to wear it to class."

    u "Can I see?"

    pe "No, haha. Sorry."


    menu:
        "Oh come on":
            $ add_point(KCT.TROUBLEMAKER)

            u "Oh come on, Penelope. I wanna see."


            pe "Sorry but... I'm gonna get dressed again."


            u "Alright, fine."

        "Fine":
            $ add_point(KCT.BOYFRIEND)

            u "Okay, fine."

            u "Then get dressed quickly, so that you can see my costume."

            pe "Yeah, just give me a minute."

    scene s184 # showing u in costume and aubrey in regular clothes
    with Fade (1,0,1)

    pause 0.5

    scene s185 # pe close up laughing
    with dissolve

    pe "Wow, I'm not sure how I feel about the cowboy look."

    scene s185a
    with dissolve

    u "What?? I considered cowboy to be a serious career path for me after I saw myself in this outfit."

    scene s185a
    with dissolve

    pe "Yeah... you should probably rethink that, haha."

    if v2_outfits < 3:
        pe "Let's check out something different."

    else:
        pe "Are you ready to buy an outfit?"

    call screen costumes

######### COWBOY PEN shop6


    ##### Aubrey caught peeking:

label caughta:
    scene s164a # Aubrey changing good view
    with dissolve

    u "(Oh my god, her ass is perfect.)"

    u "(I should stop peeking now, or I'll get caught.)"

    scene s163
    with dissolve

    jump v1_caughtContinue

label caughtb:
    scene s168a # Aubrey changing good view
    with dissolve

    u "(Damn, what I wouldn't give to touch her ass right now.)"

    u "(I should stop peeking now, or I risk getting caught.)"

    scene s167
    with dissolve

    jump v1_caughtContinue

label caughtc:
    scene s172a # Aubrey changing good view
    with dissolve

    u "(In all fairness, whenever I watch porn, the person getting caught spying gets to fuck the girl right afterwards.)"

    u "(Still... I better stop peeking now, it's too risky.)"

    scene s171
    with dissolve

    jump v1_caughtContinue

label v1_caughtContinue:
    au "[name], did I just see you pull your head out from underneath the dividers?"

    scene s177d # closeup aubrey outside in regular clothes angry
    with Fade (1,0,1)

    au "[name]? Did you just peek on me?"

    menu:
        "Apologize":
            $ add_point(KCT.BOYFRIEND)
            $ v2_caughtpeekingcounter = True

            scene s177e
            with dissolve

            u "Aubrey, I'm so sorry. It was just..."

            u "...so tempting."

            scene s177d # aubrey disappointed
            with dissolve

            au "Honestly, it's okay. It was just kinda surprising."

            au "How about we just buy a costume and get going?"

        "Deny it":
            $ add_point(KCT.TROUBLEMAKER)

            scene s177e
            with dissolve

            u "What are you talking about? You probably just saw my foot."

            if kct == "confident":
                call screen kct_popup

                $ v2_caughtpeekingcounter = True

                scene s177d # aub embarrassed
                with dissolve

                au "Wait really?"

                au "Ooops, I guess never mind, let's just buy a costume."

                scene s177e
                with dissolve

                u "Yeah, it's fine. I'll pick one."

            else:
                scene s177b # aubrey disappointed
                with dissolve

                au "Yeah, right."

                au "Honestly, I didn't even mind, but why would you lie about it, that's messed up."

                au "I'm gonna leave, I guess I'll see you around."

                scene s177c # empty
                with fade

                u "(Fuck, I shouldn't have lied to her.)"

                u "(And I still need to buy a costume...)"

    call screen costumes

    ##### Penelope caught peeking: shop7
label caughtd:
    scene s180a # pen changing good view
    with dissolve

    u "(Oh my god, her ass is so nice.)"

    u "(I should stop peeking now, or I'll get caught.)"

    scene s163
    with dissolve


    jump v1_caughtContinue_pen

label caughte:
    scene s183a
    with dissolve

    u "(Damn, what I wouldn't give to touch her ass right now.)"

    u "(I should stop peeking now, or I risk getting caught.)"

    scene s167
    with dissolve

    jump v1_caughtContinue_pen

label caughtf:
    scene s180a # pen changing good view
    with dissolve

    u "(In all fairness, whenever I watch porn, the person getting caught spying gets to fuck the girl right afterwards.)"

    u "(Still... I better stop peeking now, it's too risky.)"

    scene s171
    with dissolve

    jump v1_caughtContinue_pen

label v1_caughtContinue_pen:
    pe "Oh my god! [name], did I just see you pull your head out from underneath the dividers??"

    pe "Did you spy on me??"

    scene s186 # closeup pen outside in regular clothes upset
    with Fade (1,0,1)

    show screen tutorial([
        "When people make important decisions on how they feel about you, they consider what kind of a person you are.",
        "Your Key Character Trait (Loyal, Popular or Confident) has a strong influence on how other characters react to your behavior.",
        "Some people value a popular leader, some care more about loyalty than status and some are drawn to confidence.",
        "Your decisions matter and have long time effects, as you can only have one KCT at a time. So think about what kind of person you want to be."
    ])

    pe "[name]! What were you thinking?!"

    menu:
        "Apologize":
            hide screen tutorial
            $ add_point(KCT.BOYFRIEND)

            scene s186a
            with dissolve

            u "Penelope, I'm so sorry. It was just..."

            u "...so tempting."

            scene s186b # penelope sad
            with dissolve

            pe "I don't know how to deal with this right now."

            pe "I'm gonna leave, goodbye."

            scene s177c # empty
            with dissolve

            u "(Fuck, I shouldn't have risked it.)"

            u "(And I still need to buy a costume...)"

        "Deny it":
            hide screen tutorial
            $ add_point(KCT.TROUBLEMAKER)

            scene s186
            with dissolve

            u "What are you talking about? You probably just saw my foot."

            if kct == "confident":
                call screen kct_popup

                $ v2_caughtpeekingcounter = True

                scene s186d # pen embarrassed
                with dissolve

                pe "Wait really?"

                pe "I'm so sorry, I just... I just thought-"

                pe "Let's just both buy a costume and get out of here."

                scene s186e
                with dissolve

                u "Yeah, it's fine. I'll pick one."

            else:
                scene s186b
                with dissolve

                pe "[name], I know what I saw."

                pe "Why can't you just admit it?"

                pe "I don't know how to deal with this right now. Goodbye."

                scene s177c # empty
                with fade

                u "(Fuck, I shouldn't have risked it.)"

                u "(And I still need to buy a costume...)"

    call screen costumes

label v1_gocostumes:
    call screen costumes

# Purchase with Aubrey

label buy1:
    $ costume = 1
    jump buyCont
label buy2:
    $ costume = 2
    jump buyCont
label buy3:
    $ costume = 3
    jump buyCont

label buyCont:
    if v2_caughtpeeking:
        jump eve1

    else:
        scene s189  # at checkout with aubrey
        with Fade (1,0,1)

        u "I'll take this one, please."

        u "Pay by card."

        scene s188 # close up eve looking at cash register
        with dissolve

        ev "Well I'm glad you guys found something."

        scene s188a # close up eve head turn
        with dissolve

        u "Thanks again so much for helping us out."

        scene s188b
        with dissolve

        ev "Yeah, it's no worry."

        scene s188c #presents bag
        with dissolve

        ev "Alright, here you go."

        scene s188d
        with dissolve

        u "Thank you, have a nice day."

        scene s188b # eve smiling
        with dissolve

        ev "You too."

        scene s194 # walking home with aubrey
        with Fade (1,0,1)

        au "I had a really great time today."

        scene s195 # closeup
        with dissolve

        au "But I wouldn't mind doing something different than costume shopping next time."

        scene s195a
        with dissolve

        u "Haha, I'm sure we'll find something fun to do."

        u "I gotta go right here, so I'll see you later, okay?"

        scene s195
        with dissolve

        au "Yeah, goodbye [name]."

        jump v1_endShop

label buy1p:
    $ costume = 1
    jump v1_buyContinuePenelope
label buy2p:
    $ costume = 2
    jump v1_buyContinuePenelope
label buy3p:
    $ costume = 3
    jump v1_buyContinuePenelope

label v1_buyContinuePenelope:
    if v2_caughtpeeking:
        jump eve1

    else:
        scene s190 # at check out, pen looking at you
        with Fade (1,0,1)

        pe "Hey, sorry to ask this, but could you lend me the money for this? My dad just sent me a text that he froze my card."

        scene s190a
        with dissolve

        u "Oh shit. Yeah, of course."

        u "I'll take these two, please."

        u "Pay by card."

        scene s188 # close up eve looking at cash register
        with dissolve

        ev "Well I'm glad you guys found something."

        scene s188a # close up eve head turn
        with dissolve

        u "Thanks again so much for helping us out."

        scene s188b
        with dissolve

        ev "Yeah, it's no worry."

        scene s188c #presents bag
        with dissolve

        ev "Alright, here you go."

        scene s188d
        with dissolve

        u "Thank you, have a nice day."

        scene s188b # eve smiling
        with dissolve

        ev "You too."

        scene s192 # walking home with evelyn
        with Fade (1,0,1)

        pe "Thanks for paying for me."

        scene s193 # closeup
        with dissolve

        pe "If you give me your number, I can let you know as soon as I have the money to pay you back."

        scene s193a
        with dissolve

        u "Yeah sounds, good."

        u "I gotta go right here, so I'll see you later, okay?"

        scene s193
        with dissolve

        pe "Okay, bye [name]."

        jump v1_endShop

label eve1:
    scene s187  # you alone at checkout
    with Fade (1,0,1)

    u "I'll take this one, please."

    u "Pay by card."

    scene s188 # close up eve looking at cash register
    with dissolve

    ev "Well I'm glad you found something."

    scene s188a # close up eve head turn
    with dissolve

    ev "Even though you seem to have a lost a person on the way."

    scene s188b
    with dissolve

    u "Yeah, she had to get home."

    scene s188c #presents bag
    with dissolve

    ev "Alright, here you go."

    menu:
        "Make a move":
            $ evelyn.relationship = Relationship.MOVE
            $ add_point(KCT.BRO)

            scene s188d
            with dissolve

            u "Thanks."

            u "Hey, is there any chance I could get your number?"

            scene s188b
            with dissolve

            ev "I'm very flattered, but I'm 25 and you seem a bit too young for me."

            scene s188d
            with dissolve

            u "Give me one date to change your mind."

            u "Come on, it'll be fun."

            ev "Give me one good reason to give you a chance."

            scene s188g
            with dissolve

            menu:
                "Be smart":
                    $ evelynnumber = True

                    scene s188h
                    with dissolve

                    u "Look, I don't know and you don't know me. I'm [name] and I'm just looking for someone to have a good time with."

                    u "It's not gonna be the most exciting night of your life, and it's not gonna be a boring night at home playing jenga with the girls."

                    u "What this night will do, is serve as a benchmark for future dates with me."

                    u "What do you say?"

                    scene s188g
                    with dissolve

                    ev "Damn, that was convincing. Okay, I'm in."

                    ev "I'll give you my number, but you better bring your A-game."

                    scene s188h
                    with dissolve

                    u "Don't worry, you won't be disappointed."

                    scene s188b
                    with dissolve

                    ev "Well, I'm looking forward to it."

                    scene s188d
                    with dissolve

                    u "Great, I'll let you know."

                    u "(I'm getting really good at this flirting thing...)"

                "Be funny":
                    $ evelynnumber = False

                    scene s188h
                    with dissolve

                    u "How about I'll wear the costume I bought yesterday for our entire date?"

                    scene s188b
                    with dissolve

                    ev "Look, it's very cute that you'd do that for me, but I just don't think we'd be a great fit."

                    ev "I'm sure you'll find someone else."

                    scene s188d
                    with dissolve

                    u "Oh okay... I guess I'll see you around."

                    u "(Damn, that didn't go as planned...)"

        "Leave":
            $ add_point(KCT.BOYFRIEND)

            scene s188d
            with dissolve

            u "Thank you, have a nice day."

            scene s188b # eve smiling
            with dissolve

            ev "You too."

label endshopb: #for compatibility only
label v1_endShop:
    stop music fadeout 3

    scene s196
    with Fade (1,0,1)

    u "(The Wolves? What are they doing here?)"

    scene s197 # aaron pointing at you
    with dissolve

    aa "Hey, you're the guy that got punched by Grayson!"

    scene s197c
    with dissolve

    u "Really? Is that what I'm gonna be known for from now on?"

    scene s197b
    with dissolve

    ch "It doesn't have to be."

    ch "Look, Grayson's an asshole. If you wanna get back at him, you should pledge the Wolves."

    ch "If you're the right fit, you'll become one of us and trust me, next year a Wolf is gonna beat the shit out of Grayson and take the fucking crown."

    scene s197c
    with dissolve

    u "Uhm..."

    scene s197b
    with dissolve

    ch "Just think about it."

    scene s197d # walking away
    with dissolve

    u "(Hmmm...)"

    scene s198 # zoom on poster
    with dissolve

    u "(The Wolves... huh.)"

jump v3start