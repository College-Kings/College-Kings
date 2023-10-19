# SCENE 25: Hotel Bar
# Location: Hotel Bar
# Characters: MC (Outfit 1), Josh (Outfit 1)
# Time: Evening

label v11_hotel_bar:
    $ kiwii_post = KiwiiService.new_post(sebastian, "phone/kiwii/Posts/v11/v11_caleb.webp", _("Who's laughing now!"), number_likes=374)
    $ KiwiiService.new_comment(kiwii_post, chris, _("Someone's gonna be upset in the morning!"), number_likes=renpy.random.randint(100, 200))
    $ KiwiiService.new_comment(kiwii_post, nora, _("Sebastian that's cruel!!"), number_likes=renpy.random.randint(100, 200))

    $ kiwii_post = KiwiiService.new_post(imre, "phone/kiwii/Posts/v11/v11_imrebunny.webp", _("Say hello to our newest Wolf recruit"), number_likes=306)
    $ KiwiiService.new_comment(kiwii_post, aubrey, _("Awww cute!!"), number_likes=renpy.random.randint(100, 200))
    $ KiwiiService.new_comment(kiwii_post, nora, _("That thing stinks!"), number_likes=renpy.random.randint(100, 200))
    
    scene v11hob1 # TPP Show MC getting on to a stool at the hotel bar
    with dissolve
    play music music.ck1.v11.Track_Scene_5_6 fadein 2
    pause 0.75

    scene v11hob2 # FPP Show bartender, mouth open
    with dissolve

    bartender "What can I get you?"

    menu:
        "Beer":
            scene v11hob2a # FPP Same angle as v11hob2, show bartender, mouth closed
            with dissolve
            
            u "A beer."

            scene v11hob2
            with dissolve

            bartender "Alright, love."

            scene v11hob3 # FPP Show beer on the bar
            with dissolve

            pause 0.75

        "Something fruity":
            $ v11s25_beer = False

            scene v11hob2a
            with dissolve

            grant achievement("fruity", "Have a cocktail at the bar")
            u "Something fruity."

            scene v11hob2
            with dissolve

            bartender "Alright, love."

            scene v11hob3a # FPP Show fruity cocktail on the bar
            with dissolve

            pause 0.75

    if not josh_europe: # Josh mad, so didn't come to Europe
        if v11s25_beer:
            scene v11hob4 # TPP Show MC taking a drink of beer
            with dissolve

            u "*Gulp*"

            scene v11hob5 # FPP Show view of empty bar
            with dissolve

            u "(Surprised no one else is down here.)"

            scene v11hob4
            with dissolve

            u "*Gulp*"

        else:
            scene v11hob4a # TPP Same angle as v11hob4, MC taking a drink of fruity cocktail
            with dissolve

            u "*Gulp*"

            scene v11hob5
            with dissolve

            u "(Surprised no one else is down here.)"

            scene v11hob4a
            with dissolve

            u "*Gulp*"

    else: # Josh is in Europe
        if v11s25_beer:
            scene v11hob1a # TPP Same angle as v11hob1, Josh leaning against bar next to MC, smiling with mouth open, beer on the bar in front of MC
            with dissolve

            jo "Where have you been?"

        else:
            scene v11hob1b # TPP Same angle as v11hob1, Josh leaning against bar next to MC, smiling with mouth open, fruity cocktail on the bar in front of MC
            with dissolve

            jo "Where have you been?"

        scene v11hob6 # FPP Show Josh smiling with mouth closed
        with dissolve

        u "In Europe, what about you? *Laughs*"

        scene v11hob6a # FPP Same angle as v11hob6, Josh smiling with mouth open
        with dissolve

        jo "So you got jokes now? I thought we were gonna kick it on the trip, but I haven't even really seen you."

        scene v11hob6
        with dissolve

        u "Bro... you skipped both of the group events and been sleeping the whole time. This is the first time I've really seen you."

        scene v11hob6a
        with dissolve

        jo "I needed the sleep after the night I had at the bar last Thursday, haha."

        if v11_josh_nightclub:
            scene v11hob6
            with dissolve

            u "You ended up leaving with those two girls right?"

        else: # Didn't go to the bar with Josh
            scene v11hob6
            with dissolve

            u "What ended up happening?"

        scene v11hob6b # FPP Same angle as v11hob6, Josh holding up 2 fingers, smiling with mouth open
        with dissolve

        jo "Count it bro, one... two. We went back to my house and played some games, but we were drunk and started wrestling and damn... it was a good night."

        scene v11hob6
        with dissolve

        u "Enjoying the ladies, I see."

        scene v11hob6a
        with dissolve

        jo "You know it!"

        scene v11hob7 # FPP Show Josh looking out of the bar into the hotel lobby at a beautiful girl, Josh smiling with mouth open
        with dissolve

        jo "And don't get me started on the London girls. While you guys are at museums I've been learning about London directly from the source."

        scene v11hob7a # FPP Same angle as v11hob7, Josh still looking into lobby at girl, mouth closed
        with dissolve

        u "You can see girls back at home... Don't you wanna do some things you can't do back at home?"

        scene v11hob7
        with dissolve

        jo "I am doing things I can't do back at home... London girls."

        scene v11hob7a
        with dissolve

        u "*Chuckles* You're something else."

        scene v11hob7b # FPP Same angle as v11hob7, Josh still looking at girl with mouth open, girl is walking off
        with dissolve

        jo "Oh shit, gotta go man. I'll see ya around."

        scene v11hob7c # FPP Same angle as v11hob7, Josh walking away toward hotel lobby and the girl
        with dissolve

        u "(Damn, left so fast I couldn't even say bye.)"
    stop music fadeout 3
    jump v11_hotel_charlie_bar