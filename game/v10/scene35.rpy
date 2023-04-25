label v10_chloe_vs_nora:

    scene v10cvn1 #First with Chloe grabbing Nora's shoulders and Nora making an aggressive face,
    with dissolve

    cl "*Grunts*"
    play music "music/v10/Track Scene 35.mp3" fadein 2

    scene v10cvn2 #second with Nora hitting Chloe's arms into the air off her shoulders
    with dissolve

    no "Oh my God, GET OFF!"

    scene v10cvn3 #Third and third and a half is Chloe slipping and Nora standing over her look down smiling
    with dissolve

    cl "*Screams* Ahh!"
    no "Who's smiling now?"

    scene v10cvn4 # fourth is Nora sitting on top of Chloe trying to pin her arms down as Chloe resist
    with dissolve

    no "C'mon Madame President."

    if is_censored:
        call screen censored_popup("v10s35_nsfwSkipLabel1")

    scene v10cvn5 # fifth is of Chloe lifting her waist throwing Nora up a little bit at which point her strap falls down on one side letting her breast slip out of her top and Nora gets extremely shocked,
    with dissolve

    cl "*Grunts*"
    no "*Screams* Ahh!"
    aa "This is getting more interesting by the second!"
    imre "Now you're making sense!"
    aut "Uhm..."

    scene v10cvn6 # sixth image is of Nora falling off of Chloe into the mud on her stomach,
    with dissolve

    no "Ugh!"

    scene v10cvn7 # seventh is of Chloe sitting on Nora pinning one arm behind her back while Nora is making a face of pain while covering her breast with the other arm
    with dissolve

    no "OKAY YOU WIN!"

label v10s35_nsfwSkipLabel1:
    scene v10cvn8 # FPP Nora is putting back on her bikini, Chloe is looking down at the mud on her body
    with dissolve

    aa "Looks like we have a winner, CHLOE!"

    scene v10cvn9 # FPP. Show chloe, still muddy, big smile on face, mouth closed.
    with dissolve

    aut "Congratulations, Chloe!"

    menu:
        "Talk to Chloe":
            scene v10cvn9a # fpp same 9, mouth open
            with dissolve

            u "Hey! Good job."

            if CharacterService.is_mad(chloe):
                scene v10cvn9a
                with dissolve
                
                cl "Uhm thanks, [name]."

                menu:
                    "Make a joke":
                        $ CharacterService.set_relationship(chloe, Relationship.FRIEND, mc)
                        $ CharacterService.remove_mood(chloe, Moods.MAD)

                        scene v10cvn9
                        with dissolve

                        u "I know you're a bit mad at me, but I just hope you never unleash your fury on me like that, haha."

                        scene v10cvn9a
                        with dissolve

                        cl "I'm not even really that mad at you anymore'"

                        scene v10cvn9
                        with dissolve

                        u "Haha, I'm glad. Anyway, I'll let you get back to celebrating."

                        scene v10cvn9a
                        with dissolve

                        cl "*Chuckles* Okay."

                    "Leave":
                        scene v10cvn9
                        with dissolve

                        u "I think I'll leave her to it."

            else:       
                scene v10cvn9b # fpp same 9,big smile, mouth open
                with dissolve

                cl "Wow, that felt good! I beat her ass!"

                scene v10cvn9c # fpp same 9,big smile, mouth closed
                with dissolve

                u "You did good. It was a nice match."

                if v10_cheerfornora:
                    # -if cheered for Nora-
                    scene v10cvn9a
                    with dissolve

                    cl "Also, did I hear you cheer for Nora?"

                    scene v10cvn9
                    with dissolve

                    u "Nope, no idea what you're talking about."

                    scene v10cvn9a
                    with dissolve

                    cl "Right..."

        "Talk to Nora":
            scene v10cvn10 # FPP. Show nora, mouth closed
            with dissolve

            u "Hey! You good?"

            scene v10cvn10a # FPP. Show nora, mouth open
            with dissolve

            no "I'm fine, if my stupid top wouldn't have messed up I would've won."

            scene v10cvn10
            with dissolve

            u "It did look like you were winning up until that point."

            scene v10cvn10a
            with dissolve

            no "*Sighs* The golden girl gets what she wants once again. It's fine, where's Chris?"

            scene v10cvn10
            with dissolve

            u "I saw him talking to someone earlier."

            scene v10cvn10a
            with dissolve

            no "So he didn't watch?"

            scene v10cvn10
            with dissolve

            u "Uhm, I'm not sure."

            scene v10cvn10a
            with dissolve

            no "*Sighs* Thanks [name]."

    scene v10cvn11 # FPP. Show autumn mouth open
    with dissolve

    aut "That was an... exciting start. Our next matchup is Emily and Aubrey."

    scene v10cvn12 # FPP. Show Emily and Aubrey entering the mud pool.
    with dissolve

    pause 1

    stop music fadeout 3
    jump v10_emily_vs_aubrey