# SCENE 14: If MC got mad at Ms. Rose, she wants to make him dinner
# Locations: Out front of College Building
# Characters: MC (Outfit: 5), Ms. Rose (Outfit: 1)
# Time: Afternoon

label v15s14:
    scene v15s14_1 # TPP. Show MC walking out of the College building, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v15s14_2 # TPP. Show Ms. Rose standing by her car waving at MC, Slight smile, mouth open.
    with vpunch

    ro "Hey, [name]!"

    scene v15s14_3 # FPP. MC standing at the bottom of the stars looking at Ms. Rose in the distance hand on her hip by her car, slight smile, mouth closed.
    with dissolve

    u "*Sighs* (What does she want now?)"

    scene v15s14_4 # TPP. Shot from behind MC walking towards Ms. Rose who is stood by her car, Ms. Rose slight smile, mouth closed, MC's face not shown.
    with dissolve

    pause 0.75

    scene v15s14_5 # FPP. MC standing infront of Ms. Rose at her car, Ms. Rose, slight smile, mouth closed.
    with dissolve

    menu:
        "Say nothing":
            $ add_point(KCT.BRO)
            
            u "..."

            scene v15s14_5a # FPp. Same as v15s14_5, Ms. Rose, Apologetic expression, mouth open
            with dissolve

            ro "Oh, is this the silent treatment?"

        "I'm not happy":
            $ add_point(KCT.BOYFRIEND)
            
            scene v15s14_5b # FPP. Same as v15s15_5a, Ms. Rose, Apologetic expression, mouth closed.
            with dissolve

            u "I'm still far from happy about our conversation earlier."

    scene v15s14_5a
    with dissolve

    ro "Okay, you have every right to be angry, but let me at least try to make it up to you."

    scene v15s14_5b
    with dissolve

    u "How are you going to make it up to me?"

    scene v15s14_5c # FPP. Same as v15s5_5, Ms. Rose, slight smile, mouth open.
    with dissolve

    ro "I can start by making you dinner, come on."

    ro "I'll take you to my place, you can sit back, relax, and just have a home-cooked meal."

    ro "When was the last time you had a decent home-cooked meal?"

    scene v15s14_5
    with dissolve

    u "It's been a while, I guess."

    menu:
        "Don't drug me":
            $ add_point(KCT.BOYFRIEND)
            
            scene v15s14_5b
            with dissolve
            
            u "Just don't slip me anymore fucking drugs, okay?"

            scene v15s14_5d # FPP. Same as v15s5_5b, Ms. Rose turned on by his anger, Ms. Rose giving a flirty pout, mouth open.
            with dissolve

            ro "Ooh, okay... Understood, [name]. I'll do whatever you say."

            scene v15s14_5e # FPP. Same as v15s5_5d, Ms. Rose biting her lip.
            with dissolve

            u "*Sighs*"

            scene v15s14_5c
            with dissolve

            ro "Hop in!"

            scene v15s14_6 # TPP. Show MC and Ms. Rose getting into her car, MC neutral face, mouth closed, Ms. Rose, slight smile, mouth closed.
            with dissolve

            pause 0.75

            scene v15s14_7 # TPP. Close up of MC buckling his seatbelt in the passenger seat, neutral face, mouth closed.
            with dissolve

            pause 1

            scene v15s14_8 # TPP. Nice aerial shot of the car leaving campus
            with fade

            pause 1

        "Let's go":
            $ add_point(KCT.TROUBLEMAKER)
             
            u "Okay, let's go."

            scene v15s14_5c
            with dissolve

            ro "Hop in!"

            scene v15s14_6 # TPP. Show MC and Ms. Rose getting into her car, MC neutral face, mouth closed, Ms. Rose, slight smile, mouth closed.
            with dissolve

            pause 0.75

            scene v15s14_7 # TPP. Close up of MC buckling his seatbelt in the passenger seat, neutral face, mouth closed.
            with dissolve

            pause 1

            scene v15s14_8 # TPP. Nice aerial shot of the car leaving campus
            with fade

            pause 1

            scene v15s14_9 # FPP. Show Ms. Rose's hand on MC's thigh near his crotch while she drives.
            with dissolve

            pause 1

    scene v15s14_10 # TPP. Show the car on a road near Ms. Rose's house
    with fade

    pause 1

    scene v15s14_11 # TPP. Shot of the car pulling into Ms. Rose's drive way.
    with dissolve

    pause 1

    stop music fadeout 3

    jump v15s15