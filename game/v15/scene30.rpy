# SCENE 30: Go to bed, Apes
# Locations: Mc's Apes Bedroom
# Characters: MC (Outfit: 9)
# Time: Night
# Render Count: 5 Unique, 14 total

label v15s30:
    play music "music/v13/Track Scene 15.mp3" fadein 2

    scene v15s30_1 # TPP. MC walks into his Ape's bedroom, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v15s30_2 # TPP. MC changes into boxers, gets into bed, slight smile, mouth closed
    with dissolve

    u "(Jenny and Penelope are a real handful when they get together! Haha...)"

    scene v15s30_3 # TPP. MC is laying in his Ape's bed, slight smile, mouth closed
    with dissolve

    u "(A lot of fun though, that's for sure.)"

    u "(And it was a nice surprise seeing Samantha at the bar...)"

    scene v15s30_3
    with dissolve

    pause 0.75

    if v14_Samantha_clean:
        scene v15s30_3
        with dissolve

        u "(And she was drinking non-alcoholic beer? It's good to see her doing better.)"

    else:
        scene v15s30_3
        with dissolve

        u "(She's a wild one... I just hope things between Cameron and I stay cool.)"

    scene v15s30_3a # TPP. same as v15s30_3 MC Yawns
    with dissolve

    u "(Tomorrow is a big day with Aubrey. I'd better get a good night's sleep.)"

    scene v15s30_3
    with dissolve

    pause 0.75

    if v14_emily_ily:
        play sound "sounds/vibrate.mp3"

        scene v15s30_3b # TPP. Mc looks at his phone on the nightstand, slight smile, mouth closed
        with dissolve

        pause 0.75

        scene v15s30_4 # FPP. MC picks up his phone and checks his texts and sees a message from Emily, From MC's chest and entire lower body is visible from the angle of him laying on the bed
        with dissolve

        pause 1.5

        $ emily.messenger.newImgMessage("images/v15/Scene 29/v15s29_emily_lingerie.webp", force_send=True) #Standing next to a full bathtub, in sexy *new* lingerie
        $ emily.messenger.newMessage("About to have a late night bath, thinking of you.", force_send=True)
        $ emily.messenger.addReply("Oh, yeah?", func=None)
        $ emily.messenger.addReply("Let me see? ;)", func=None)

        if config_censored:
            $ emily.messenger.newImgMessage("gui/censoredPopup/censoredBackground.webp", force_send=True)
        else:
            $ emily.messenger.newImgMessage("images/v15/Scene 29/emilynude1.webp", force_send=True) # Emily sat on the edge of the bath, now naked, legs crossed

        $ emily.messenger.newMessage("What would we be doing right now if you were here with me? ;)", force_send=True)
        $ emily.messenger.addReply("We'd be getting very wet and extremely warm...", func=None)
        $ emily.messenger.newMessage("Mmm... Send me a pic? ;)", force_send=True)

        label v15s30_PhoneContinue:
            if emily.messenger.replies:
                call screen phone
            if emily.messenger.replies:
                u "(I should check out what Emily wants.)"
                jump v15s30_PhoneContinue

        scene v15s30_4
        with dissolve

        menu:
            "Sext Emily":
                $ add_point(KCT.TROUBLEMAKER)
                $ add_point(KCT.BRO)
                $ v15_emily_sext = True
                
                scene v15s30_4
                with dissolve

                pause 0.75

                scene v15s30_4a # FPP. same as v15s30_4 MC has pulled out his dick and started stroking it
                with dissolve
                
                pause 0.75

                if config_censored:
                    $ emily.messenger.newImgMessage("gui/censoredPopup/censoredBackground.webp", force_send=True)
                else:
                    $ emily.messenger.newImgMessage("images/v15/Scene 29/emilynude_MC_DicPic1.webp", force_send=True) # Ignore as Reused from scene 29

                $ emily.messenger.newMessage("Omg, you're so hard for me... Are you touching yourself?", force_send=True)
                $ emily.messenger.addReply("I am now. Thinking about you in that bath ;)", func=None)
                $ emily.messenger.newMessage("Hehe, I'm thinking about you slipping of inside me...", force_send=True)
                $ emily.messenger.newMessage("I do miss you... Both of you, haha.", force_send=True)
                $ emily.messenger.addReply("I'm sure you'll see us again soon.", func=None)
                $ emily.messenger.newMessage("How soon? I need you so bad...", force_send=True)
                $ emily.messenger.addReply("We'll see... If you're a good girl then maybe soon rather than later ;)")

                if config_censored:
                    $ emily.messenger.newImgMessage("gui/censoredPopup/censoredBackground.webp", force_send=True)
                else:
                    $ emily.messenger.newImgMessage("images/v15/Scene 29/emilynude2.webp", force_send=True) # Ignore as reused from Scene 29

                $ emily.messenger.newMessage("I want you here. Now.", force_send=True)
                $ emily.messenger.addReply("Fuck, that's so hot...", func=None)
                $ emily.messenger.addReply("You have to earn it...", func=None)
                $ emily.messenger.newMessage("I'm going to cum for you...", force_send=True)
                $ emily.messenger.addReply("Good.", func=None)
                $ emily.messenger.newMessage("Send me a pic when you're finished? ;)", force_send=True)

                label v15s30_PhoneContinue2:
                    if emily.messenger.replies:
                        call screen phone
                    if emily.messenger.replies:
                        u "(I should reply to Emily.)"
                        jump v15s30_PhoneContinue2

                scene v15s30_4a
                with dissolve

                pause 0.75

                scene v15s30_4b # FPP. same as v15s30_4a Mc's hand is stroking the bottom part of the shaft of his dick
                with dissolve

                pause 0.75

                scene v15s30_4c # FPP. same as v15s30_4b Mc's hand is stroking the top part of the the shaft of his dick
                with dissolve

                pause 0.75

                scene v15s30_4d # FPP. same as v15s30_4c Mc blows a huge load all over his hand
                with dissolve

                u "*Moans*"

                scene v15s30_4e # FPP. same as v15s30_4d MC takes a picture of the cum on his hand and send's it to Emily
                with dissolve

                pause 0.75

                if config_censored:
                    $ emily.messenger.newImgMessage("gui/censoredPopup/censoredBackground.webp", force_send=True)
                else: 
                    $ emily.messenger.addImgReply("images/v15/Scene 29/emilynude_MC_DicPic2.webp", func=None) # Ignore as reused from scene 29

                $ emily.messenger.newMessage("God, I wish I was there to help clean that off you...", force_send=True)
                $ emily.messenger.addReply("You're such a dirty girl, Emily.", func=None)
                $ emily.messenger.addReply("Haha, my dirty girl...", func=None)
                $ emily.messenger.newMessage("You know it ;)", force_send=True)
                $ emily.messenger.newMessage("Night, [name]. Thanks for the show :)", force_send=True)
                $ emily.messenger.addReply("You too. <3 Night.", func=None)

                scene v15s30_4f # same as v15s30_4d FPP. MC wipes his dick clean of cum
                with dissolve

                pause 0.75

                scene v15s30_3
                with dissolve

                u "(Okay, now I'm super relaxed... Haha. Time for sleep.)"

            "Don't sext her":
                $ add_point(KCT.BOYFRIEND)
                
                $ emily.messenger.addReply("Not really in the mood... I'm sorry", func=None)
                $ emily.messenger.newMessage("Oh, okay. No worries. I'll talk to you soon, I miss you <3", force_send=True)
                $ emily.messenger.addReply("You too, night :)", func=None)

                label v15s30_PhoneContinue3:
                    if emily.messenger.replies:
                        call screen phone
                    if emily.messenger.replies:
                        u "(I should reply to Emily.)"
                        jump v15s30_PhoneContinue3

                scene v15s30_4
                with dissolve

                pause 0.75

                scene v15s30_3
                with dissolve

                u "(Okay, time for sleep now.)"

    scene v15s30_5 # TPP. lights are out, and MC has laid down to go to sleep, no expression, eyes closed
    with fade

    pause 0.75

    stop music fadeout 3

    scene black
    with fade
    
    pause 2

    jump v15s31