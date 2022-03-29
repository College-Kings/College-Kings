# SCENE 38: Aubrey arrives at the restaurant
# Locations: Outside restaurant
# Characters: MC (Outfit: DATE NIGHT OUTFIT), AUBREY (Outfit: DATE NIGHT OUTFIT), DRIVER (Outfit: 1)
# Time: EVENING

label v16s38:
    scene v16s38_1 # TPP. MC arrives at the restaurant entrance and waits beside it (It's an Italian restaurant, but not a location we've been to before,) slight smile, mouth is closed
    with dissolve

    pause 0.75

    scene v16s38_2 # TPP. The cab arrives and the driver steps out, opening the door for Aubrey. Aubrey steps out, wearing date night outfit (already made) She doesn't look very cheerful as she's feeling insecure about her outfit. MC approaches her at the cab, slight smile, mouth is closed
    with dissolve

    pause 0.75

    scene v16s38_3 # FPP. Show just Aubrey from the waist up, slight smile, mouth is closed, looking at MC
    with dissolve

    u "Well, hello there, gorgeous... You look amazing, Aubrey."

    scene v16s38_4 # TPP. Show MC and Aubrey exchanging a quick hug.
    with dissolve

    pause 0.75

    scene v16s38_4a # TPP. Show MC and Aubrey exchanging a quick kiss.
    with dissolve
    play sound "sounds/kiss.mp3"
    pause 0.75

    scene v16s38_3a # FPP. Show just Aubrey from the waist up, no expression, mouth is open, looking at MC
    with dissolve

    au "Thanks, but... I don't feel it."

    scene v16s38_3b # FPP. Show just Aubrey from the waist up, no expression, mouth is closed, looking at MC
    with dissolve

    u "What, why? What's wrong?"

    scene v16s38_3c # FPP. Show just Aubrey from the waist up, no expression, mouth is closed, slightly looking away from MC
    with dissolve

    au "Am I showing too much skin?"

    scene v16s38_3b
    with dissolve

    u "I don't think so..."

    scene v16s38_3a
    with dissolve

    au "This place is so elegant, [name], I should've worn something longer."

    scene v16s38_3b
    with dissolve

    menu:
        "Reassure her":
            $ add_point(KCT.BOYFRIEND)
            $ add_point(KCT.BRO)

            scene v16s38_3b
            with dissolve

            u "Honestly, Aubrey..."

            scene v16s38_3d # FPP. Show just Aubrey (slighlty sad/embarrassed expression, mouth is closed) from the waist up, MC grabs both of Aubrey's hands (visible in render), looking at MC
            with dissolve

            u "You look absolutely perfect."

            scene v16s38_3e # FPP. Show just Aubrey from the waist up, MC is now only holding onto one of Aubrey's hands, Aubrey uses one of her hands and places it against her cheek/eye as to wipe away a tear, still a slighlty sad/embarrassed expression, mouth is open, head is pointing slightly down, and her eyes are looking up at MC
            with dissolve

            au "*Sighs* You sure?"

            scene v16s38_3d
            with dissolve

            u "Ha... I'm positive."

            scene v16s38_3f # FPP. Show just Aubrey from the waist up, Aubrey has let go of both of MC's hands, and tries to hide her smile, slighlt smile, mouth is closed, looking at MC
            with dissolve

            pause 0.75

        "Offer your jacket":
            $ add_point(KCT.BOYFRIEND)

            scene v16s38_3b
            with dissolve

            u "You can wear my jacket if you want?"

            scene v16s38_3g # FPP. Show just Aubrey from the waist up, slight shocked expression, mouth is open, looking at MC 
            with dissolve

            au "Oh, great. So, you agree?"

            scene v16s38_3b
            with dissolve

            u "What? I just want you to be comfortable."

            scene v16s38_3c
            with dissolve

            au "*Sighs*"

    scene v16s38_3a
    with dissolve

    au "Can we just hurry inside?"

    if v16_aubrey_date_cab >= 1:
        scene v16s38_3b
        with dissolve

        u "Of course, let me just pay your driver."

        scene v16s38_3a
        with dissolve

        au "Oh, right. I'll wait by the door."

        scene v16s38_5 # TPP. Show Aubrey walking away, going over to stand at the restaurant entrance. MC turns to the driver and hands him the money owed, Aubrey no expression mouth is closed, Mc slight smile mouth is closed looking at the driver, Driver slight smile mouth is closed looking at MC
        with dissolve

        pause 0.75

        scene v16s38_6 # FPP. Show just the driver from the waist up, slight smile, mouth is closed, accepting money that MC is handing him
        with dissolve

        u "Here you go."

        scene v16s38_6a # FPP. Show just the driver from the waist up, slight smile, mouth is open, the driver has put away the money
        with dissolve

        driver "Thanks, boss."

        scene v16s38_6b # FPP. Show just the driver from the waist up, slight smile, mouth is closed, the driver has put away the money
        with dissolve

        if v16_aubrey_date_cab == 2:
            u "(Ten bucks left for Lindsey's donation... Ha.)"

            u "(Should I just give him the rest as a tip?)"

        else:
            u "(This was supposed to be Lindsey's donation... Ha.)"

            u "(Should I give this guy a tip?)"

        scene v16s38_6b
        with dissolve

        menu:
            "Tip ten dollars":
                $ v16s38_tippped_driver = True
                $ v16_lindsey_donation -= 10
                $ add_point(KCT.BRO)

                scene v16s38_6b
                with dissolve

                u "(I'm already spending money meant for charity, I might as well get back a little good karma...)"

                scene v16s38_6
                with dissolve

                u "And here's your tip."

                scene v16s38_6a
                with dissolve

                driver "*Sarcastic* Oh, wow! Ten dollars?! I can put my kids through college with this."

                scene v16s38_6b
                with dissolve

                u "Seriously dude, I just gave you money that was meant for charity. How about a little gratitude?"

                scene v16s38_6a
                with dissolve

                driver "You what?"

                scene v16s38_6b
                with dissolve

                u "*Coughs* Nothing."

                scene v16s38_6a
                with dissolve

                driver "*Chuckles* It's okay, boss. I'm just joking with you."

                scene v16s38_6b
                with dissolve

                u "Oh- Yeah, haha. So was I."

                scene v16s38_6a
                with dissolve

                driver "Mmhmm, have a good night."

                scene v16s38_6b
                with dissolve

                u "Yeah, you too."

                scene v16s38_7 # TPP. Show Mc watching the the driver getting into the cab and driving away, Mc slight smile, mouth is closed, The driver slight smile, mouth is closed
                with dissolve

                pause 0.75

            "Save your money":
                $ add_point(KCT.TROUBLEMAKER)

                scene v16s38_6b
                with dissolve

                u "Thanks for dropping her off safely."

                scene v16s38_6a
                with dissolve

                driver "... Uh huh, that's my job."

                scene v16s38_6b
                with dissolve

                u "Well... Great work. Ha."

                scene v16s38_6c # FPP. The driver has a hand palm up slightly extended towards Mc, slight smile, mouth is slightly open
                with dissolve

                driver "..."

                scene v16s38_6d # FPP. The driver has a hand palm up slightly extended towards Mc, slight smile, mouth is closed
                with dissolve

                u "Take it easy!"

                scene v16s38_6e # FPP. The driver has a hand palm up slightly extended towards Mc, slight confused expression, mouth is slightly open
                with dissolve

                driver "..."

                scene v16s38_6f # FPP. The driver has a hand palm up slightly extended towards Mc, slight confused expression, mouth is closed
                with dissolve

                u "Alright, see ya!"

                scene v16s38_6e
                with dissolve

                pause 0.75

                scene v16s38_8 # TPP. MC walks away from the Driver, MC has a guilty expression mouth is closed, The Driver has a disgusted/angry expression, hand still extended out, looking at MC as he walks away
                with dissolve

                u "(Now I look like a dick because I didn't tip the man... But, fuck man, it's charity money!)"

                scene v16s38_9 # TPP. Show just a close up shot of MC's face, with a guilty expression, mouth is closed
                with dissolve

                u "(Then again... Maybe I am a dick.)"
            
    else: # IF did not order Aubrey a cab
        scene v16s38_3b
        with dissolve

        u "Yeah, of course. Let's go in."

    scene v16s38_10 # TPP. Show Mc and Aubrey walking arm in arm towards the Restaurant entrance, slight smiles, mouths are closed
    with dissolve

    pause 0.75

    if v16_aubrey_date_cab == 2: # IF MC ordered flowers with the cab
        scene v16s38_11 # FPP. Show just Aubrey from the shoulders up, looking over at MC from the side, slight smile, mouth is open
        with dissolve

        au "Oh, and thanks for the flowers. That was a fun surprise. *Laughs*"

        scene v16s38_11a # FPP. Show just Aubrey from the shoulders up, looking over at MC from the side, slight smile, mouth is closed
        with dissolve

        u "Of course, I want to make tonight special for you."

        scene v16s38_11
        with dissolve

        au "I was even more surprised when a bee came flying out of them..."

        scene v16s38_11a
        with dissolve

        u "Oh no! Are you all good?"

        scene v16s38_11
        with dissolve

        au "Eh, I'm kind of allergic to bee stings, so it was pretty horrific... *Laughs* I'm so anxious already..."

        scene v16s38_11a
        with dissolve

        u "I'm really sorry that happened."

        scene v16s38_11
        with dissolve

        au "Oh, it's not your fault. You didn't order a bee, haha."

        scene v16s38_11a
        with dissolve

        u "Ha, but why are you feeling anxious? It's just me."

        scene v16s38_11
        with dissolve

        au "Yeah, I know, know... It's just a different atmosphere, I guess?"

        scene v16s38_11a
        with dissolve

        u "Hmm, I get what you're saying. This is a bit more serious than our usual escapades."

        scene v16s38_11
        with dissolve

        au "*Laughs* Exactly."

        scene v16s38_11a
        with dissolve

        u "Let's just dive into this pit of fear together, yeah?"

        scene v16s38_11
        with dissolve

        au "Haha, yeah. Let's do it."

    else: ### ERROR: IF MC did not order flowers
        scene v16s38_11
        with dissolve

        au "All paid?"

    if v16s38_tippped_driver: # IF tipped the driver
        scene v16s38_11a
        with dissolve

        u "Paid, tipped, ready to go."

        scene v16s38_11b # FPP. Aubrey smiles proudly at mc, full smile, mouth is open, looking at MC
        with dissolve

        au "*Giggles* Perfect."

    else: ### ERROR: IF did not tip the driver
        scene v16s38_11a
        with dissolve

        u "Yup, ready to go."

        scene v16s38_11
        with dissolve

        au "Good."

        scene v16s38_10a # TPP. Show Mc and Aubrey walking arm in arm into the Restaurant, slight smiles, mouths are closed
        with dissolve

        pause 0.75

    jump v16s39 # -Transition to Scene 39-