# SCENE 31: At Diner for Breakfast
# Locations: Cafe
# Characters: MC (Outfit 3), Nora (Outfit 1), Diner Waiter (Outfit 1), Random Girl
# Time: Saturday Morning

label v9_sat_cafe_w_nora:
    scene v9cwn1 # TPP. Show MC and Nora walking to a table in the cafe.
    with fade

    play music music.ck1.v9.Track_Scene_31 fadein 2

    pause 1

    scene v9cwn2 # TPP. Show Nora and MC taking a seat at the table.
    with dissolve

    pause 1

    scene v9cwn3 # FPP. Show Nora sat opposite MC at the table, Nora neutral, mouth open.
    with dissolve

    no "It feels good to have a nice meal once in awhile."

    scene v9cwn3a # FPP. Same camera as v9cwn3, neutral, mouth closed.
    with dissolve

    u "Do you and Chris not go on dates now and then?"

    scene v9cwn3
    with dissolve

    no "Do you really have to ask? We spent a lot of time together when we first started dating, but now it's like I'm second to the Wolves. And I know I shouldn't be jealous, but in a way I am. Like, if you have all this passion, love and attention to give, can some come my way?"

    scene v9cwn3a
    with dissolve

    u "I think you're right to see it the way you do. Your partner should come first regardless, and even though all of this seems important now, it's all temporary."

    scene v9cwn3b # FPP. Same camera as v9cwn3, smile, mouth open.
    with dissolve

    no "Wow, under that thick skull you're not as dull as the rest of those meat heads."

    scene v9cwn3c # FPP. Same camera as v9cwn3, smile, mouth closed.
    with dissolve

    u "Haha, surprise!"

    scene v9cwn4 # FPP. Show a Waiter stood by the table, looking at camera, smile, mouth open.
    with dissolve

    waiter "Good morning, what can I get for the couple?"

    scene v9cwn4a # FPP. Same camera as v9cwn4, smile, mouth closed.
    with dissolve

    menu:
        "Correct waiter" (bro=1.0):
            $ reputation.add_point(RepComponent.BRO)

            u "Actually, we're just friends."

            scene v9cwn4
            with dissolve

            waiter "Ahhh okay, what will you be having today?"

            scene v9cwn3c
            with fade

            u "Any good news about Europe?"

            scene v9cwn3b
            with dissolve

            if helpedNora:
                no "It's going great! We almost have everything we need. I'm thinking about seeing if we can get a bit more involvement from the houses. I mentioned it to Chris, but he only said \"we'll get to that later\". It means a lot to me that you've taken an interest."

            else:
                no "It's going pretty good. Checking something off the list everyday."

            scene v9cwn3c
            with dissolve

            u "Well I'm glad to hear it's all coming together."

            scene v9cwn3b
            with dissolve

            no "Thanks for asking."

            scene v9cwn5 # TPP. Show Nora and MC now stood outside the café, both smiling looking at eachother.
            with fade

            pause 1

            scene v9cwn6 # FPP. Show Nora, Nora smile, mouth open.
            with dissolve

            no "I had a really good time [name]. Wish I could do this more often."

            scene v9cwn6a # FPP. Same camera as v9cwn6, smile, mouth closed.
            with dissolve

            u "Maybe we can."

            scene v9cwn6
            with dissolve

            no "Maybe. See you around!"

            scene v9cwn6a
            with dissolve

            u "See ya!"

            scene v9cwn7 # FPP. Show MC and Nora walking away in opposite directions.
            with dissolve

        "Don't correct waiter" (boyfriend=1.0):
            $ reputation.add_point(RepComponent.BOYFRIEND)

            scene v9cwn3c
            with fade

            u "Any good news about Europe?"

            scene v9cwn3b
            with dissolve

            if helpedNora:
                no "It's going great! We almost have everything we need. I'm thinking about seeing if we can get a bit more involvement from the houses. I mentioned it to Chris, but he only said \"we'll get to that later\". It means a lot to me that you've taken an interest."

            else:
                no "It's going pretty good. Checking something off the list everyday."

            scene v9cwn3c
            with dissolve

            u "Well I'm glad to hear it's all coming together."

            scene v9cwn3b
            with dissolve

            no "Thanks for asking."

            scene v9cwn5
            with fade

            pause 1

            scene v9cwn6
            with dissolve

            no "I had a really good time [name]. Wish I could do this more often."

            scene v9cwn6a
            with dissolve

            u "Maybe we can."

            scene v9cwn6
            with dissolve

            no "Maybe. See you around!"

            scene v9cwn6a
            with dissolve

            u "See ya!"

            scene v9cwn7
            with dissolve

    jump v9_sat_gym

label v9_sat_cafe:
    scene v9cwn8 # TPP. Show MC sat at a table in the cafe on his own.
    with dissolve

    u "(I actually can't believe how hungry I am.)"

    scene v9cwn9 # FPP. Show a girl in the distance trying to take a sneak photo of MC.
    with dissolve

    u "(What the fuck!?)"

    scene v9cwn9a # FPP. Same camera as v9cwn9, Show the girl getting up and walking towards the camera.
    with dissolve

    if hl_punch:
        scene v9cwn10 # FPP. Show the girl, curious expression, mouth open.
        with dissolve

        unknown "Hey, sorry but you're the guy that punched that other guy on Kiwii right?"

        scene v9cwn10a # FPP. Same camera as v9cwn10, mouth closed.
        with dissolve

        u "Uh, yeah that's me."

        scene v9cwn10b # FPP. Same camera as v9cwn10, flustered expression, mouth open.
        with dissolve

        unknown "Wow, I can't believe it's you. Like you're actually here in front of me right now."

        scene v9cwn10c # FPP. Same camera as v9cwn10, flustered expression, mouth closed.
        with dissolve

        u "Thanks..."

        scene v9cwn10b
        with dissolve

        unknown "Can I sit with you or is that too much? No that's too much, or is it? OMG, you're so stupid. Not you, me. OMG!"

        scene v9cwn11 # FPP. Show the girl walking away, MC watching her, confused.
        with dissolve

        u "(Okay...)"

    else: 
        scene v9cwn10f
        with dissolve

        unknown "You're the guy that got his ass kicked on Kiwii right?"

        scene v9cwn10e # FPP. Same camera as v9cwn10, smirk, mouth closed.
        with dissolve

        u "Well I wouldn't say I got my ass kicked, but yeah."

        scene v9cwn10f # FPP. Same camera as v9cwn10, laugh, mouth open.
        with dissolve

        unknown "Well everyone else would call it getting your ass kicked, including me."

        scene v9cwn11
        with dissolve        

        u "(Okay... bitch.)"

    scene v9cwn7a # FPP. Same camera as v9cwn7, show MC walking away on his own.
    with fade

    u "(Well, let the crazy begin.)"

    stop music fadeout 3

    jump v9_sat_gym