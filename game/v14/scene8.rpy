# SCENE 08: Bus to Airport
# Locations: Outside Hotel
# Characters: MC (Outfit: 5), AMBER (Outfit: 1)
# Time: Morning

label v14s08:
    play music music.ck1.v11.Track_Scene_20_2 fadein 2

    scene v14s08_1 # TPP. mc sees the bus and walks towards it, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v14s08_2 # FPP. mc gets on the bus and sees amber already sitting down, amber is looking out of the window with her head turned away from mc, ambers face is not visible
    with dissolve

    pause 0.75

    scene v14s08_3 # FPP. same as v14s08_2 mc has walked up to and sat down next to amber, her face is still not visible
    with dissolve

    u "Hey, hey! I know you're probably ready to get back."

    scene v14s08_3c # FPP. same as v14s08_3 amber turns around and looks at mc, amber is crying, her make-up is running, and her mouth is closed
    with dissolve

    am "*Sniffs*"

    u "(Oh shit... Was she crying? Oh, fuck... What do I do here?)"

    u "(I mean, for normal girls I'd just ask what's wrong but, with Amber... I don't want to get stabbed today, you know?)"

    menu:
        "Ask her what's wrong" (boyfriend=1.0):
            $ reputation.add_point(RepComponent.BOYFRIEND)
            u "Hey, what's wrong?"

            scene v14s08_3d
            with dissolve

            am "I'm not in the mood to talk."

            scene v14s08_3e # FPP. same as v14s08_3d amber looks at her phone, mouth closed
            with dissolve

            u "*Sighs* (I knew I shouldn't have asked.)"

            scene v14s08_3
            with dissolve
            pause 0.75

            scene v14s08_3e
            with dissolve
            pause 0.75

            scene v14s08_3
            with dissolve
            pause 0.75

            scene v14s08_4 # FPP. show amber walking down the bus aisle, back turned, face not visible
            with dissolve
            pause 0.75

            scene v14s08_4a # FPP. same as v14s08_4 amber has walked further away
            with dissolve

            u "(She must be going through something pretty heavy.)"

            scene v14s08_5 # TPP. show MC getting off the bus, no expression, mouth closed
            with dissolve

            pause 0.75

        "Leave her alone" (bro=1.0):
            $ reputation.add_point(RepComponent.BRO)
            scene v14s08_3
            with dissolve

            u "(Not gonna open that can of worms... If she wanted to, she would.)"

            scene v14s08_3e
            with dissolve
            pause 0.75

            scene v14s08_3
            with dissolve
            pause 0.75

            scene v14s08_3e
            with dissolve
            pause 0.75

            scene v14s08_3d
            with dissolve

            am "*Deep breath*"

            scene v14s08_3e
            with dissolve
            pause 0.75

            scene v14s08_4
            with dissolve
            pause 0.75

            scene v14s08_4b # FPP. same as v14s08_4 amber turns around and looks at mc, no expression, mouth open
            with dissolve

            am "Uh, [name]..."

            am "Thanks for minding your own business."

            scene v14s08_4c # FPP. same as v14s08_4b amber slight smile, mouth closed
            with dissolve

            u "I respect your privacy, Amber. If you need to talk, you know I'm right here. If you'd rather sit in silence, I'm still here... *Laughs*"

            scene v14s08_4d # FPP. same as v14s08_4c amber half smile, mouth open
            with dissolve

            am "*Chuckles* For the first time ever, I think I see you as more than just a cute little fucktoy."

            scene v14s08_4c
            with dissolve

            u "Uhh, thanks. *Chuckles*"

            scene v14s08_4d
            with dissolve

            am "*Laughs*"

            scene v14s08_5a # TPP. same as v14s08_5 show amber with mc, both slight smiles, mouth closed
            with dissolve

            pause 0.75

    scene v14s08_6 # FPP. Amber has walked ahead of mc towards the airport main entrance, back turned, face not visible
    with dissolve

    pause 0.75

    scene v14s08_6a # FPP. Mc was walked further towards the door, Amber is no longer visible
    with dissolve

    pause 0.75

    scene v14s08_6b # FPP. Mc walks into the airport
    with dissolve

    pause 0.75

    stop music fadeout 3
    jump v14s09