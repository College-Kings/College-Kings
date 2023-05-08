# SCENE 12: Seating/Ryan Conversation
# Location: Plane
# Characters: MC (Outfit 1), Ryan (Outfit X), Ms. Rose (Outfit 1), Chloe (outfit 5), Riley (outfit 2), Chris(outfit 1), Nora (outfit 1) # Added a couple extra characters and outfits encase need to pad out with non speaking characters in the looking down isle shot.
# Time: Saturday morning

label v11_sit_ryan_convo:
    scene v11src1 # FPP View down the aisle from front of the plane, some people sitting, some standing, Ms. Rose standing with mouth open
    with dissolve
    play music music.ck1.v11.Track_Scene_12 fadein 2
    ro "Alright, you know your seats. [name], you're sitting next to Ryan."

    scene v11src1a # FPP Same angle and characters as v11src1, Ms. Rose mouth closed
    with dissolve

    u "Oh, okay."

    scene v11src2 # TPP MC moving down aisle of plane to his seat
    with dissolve

    pause 0.75

    scene v11src3 # TPP MC sitting next to Ryan. MC in aisle seat of row
    with dissolve

    pause 0.75

    if v10s33_ryan_flirt_emily: # Talked to Ryan at Charity event and gave him your blessing
        scene v11src4 # FPP Show Ryan, sitting in seat next to window, neutral expression, mouth open
        with dissolve

        ry "This is gonna be a long flight."

        scene v11src4a # FPP Same angle as v11src4, Ryan mouth closed
        with dissolve

        u "Sure is, I'm gonna have to do some sleeping to pass the time."

        scene v11src4
        with dissolve

        ry "Or we can talk."

        scene v11src4a
        with dissolve

        u "About?"

        scene v11src4b # FPP Same angle as v11src4, Ryan with curious expression, mouth open
        with dissolve

        ry "I don't know, what's new?"

        scene v11src4a
        with dissolve

        u "Hmm... got some new clothes, had a hearing with the dean, and well, Emily said she no longer wants to talk to me."

        scene v11src4c # FPP. Same angle as v11src4, Ryan looking surprised, mouth open
        with dissolve

        ry "Oh damn, why?"

        scene v11src4a
        with dissolve

        u "I don't even remember."

        scene v11src4
        with dissolve

        ry "She actually said hey to me in the hall yesterday. Invited me to do some first responders class."

        scene v11src4a
        with dissolve

        u "I'm pretty sure she wants to be a nurse or something so I'm not surprised."

        scene v11src4b
        with dissolve

        ry "Since you know her so well... Do you think you could tell me some things about her?"

        menu:
            "No thanks":
                scene v11src4a
                with dissolve

                u "Uhm, I'm pretty tired, so I think I'm going to sleep."
            
            "Like what?":
                $ reputation.add_point(RepComponent.BRO)

                scene v11src4j # FPP Same angle as v11src4, Ryan smiling slightly, mouth closed
                with dissolve

                u "Like what?"

                scene v11src4b
                with dissolve

                ry "Like her favorite things, what pisses her off, stuff like that."

                scene v11src4a
                with dissolve

                u "She's very intense. I don't know... When she gets attached, she's attached. But that doesn't necessarily have to mean loyal as I found out..."

                scene v11src4c
                with dissolve

                ry "Damn. What else?"

                scene v11src4a
                with dissolve

                u "She's talked about being a doctor before. She's into a lot of medical stuff."

                scene v11src4e # FPP. Same angle as v11src4, Ryan smiling, mouth open
                with dissolve

                ry "Okay, so lots of student loan debt, but a good long term paycheck. Very promising."

                scene v11src4d # FPP. Same angle as v11src4, Ryan smiling slightly, mouth closed
                with dissolve

                u "Bro, you've talked to other girls, why Emily?"

                scene v11src4e
                with dissolve

                ry "I don't know bro, I'm just really into her. She's fire."

                scene v11src4d
                with dissolve

                u "What do you even like about her though?"

                scene v11src4b
                with dissolve

                ry "I just have that feeling man. Sure there's other girls I find attractive, but it's not all about that with her. I feel something else."

                scene v11src4d
                with dissolve

                u "You're just tryna smash."

                scene v11src4f # FPP Same angle as v11src4, Ryan with serious expression, mouth open
                with dissolve

                ry "Nah man... I'm serious."

                scene v11src4a
                with dissolve

                u "Look, I can't tell you everything, that'd just be weird. You'll find more value in getting to know her yourself and her opening up to you."

                scene v11src4
                with dissolve

                ry "True, plus I wouldn't know what to talk about if I knew everything about her."

                scene v11src4d
                with dissolve

                u "See? You got it all figured out. Now let me get some sleep."

    elif not "ryan" in freeroam6: # If didn't talk to Ryan at charity event
        scene v11src4
        with dissolve

        ry "This is gonna be a long flight."

        scene v11src4a
        with dissolve

        u "Sure is, I'm gonna have to do some sleeping to pass the time."

        scene v11src4
        with dissolve

        ry "Or we can talk."

        scene v11src4a
        with dissolve

        u "About?"

        scene v11src4b
        with dissolve

        ry "I don't know, what's new?"

        scene v11src4a
        with dissolve

        u "Hmm... got some new clothes, had a hearing with the dean, and well, Emily said she no longer wants to talk to me."

        scene v11src4d
        with dissolve

        ry "Oh damn, why?"

        scene v11src4a
        with dissolve

        u "I don't even remember."

        scene v11src4
        with dissolve

        ry "She actually said hey to me in the hall yesterday. Invited me to do some first responders class."

        scene v11src4a
        with dissolve

        u "I'm pretty sure she wants to be a nurse or something so I'm not surprised."

        scene v11src4b
        with dissolve

        ry "Since you know her so well... Do you think you could tell me some things about her?"

        menu:
            "Give blessing":
                $ reputation.add_point(RepComponent.BRO)
                scene v11src4d
                with dissolve

                u "Haha, sounds like you like her."

                scene v11src4b
                with dissolve

                ry "Oh yeah, uhm, that doesn't bother you does it?"

                scene v11src4d
                with dissolve

                u "I'm honestly over her man, you can do whatever you want."

                scene v11src4e
                with dissolve

                ry "Alright, I was hoping it wasn't an issue."

                scene v11src4d
                with dissolve

                u "It's cool, man."

                scene v11src4b
                with dissolve

                ry "So uh... about my question."

                scene v11src4a
                with dissolve

                u "She's very intense. I don't know... When she gets attached, she's attached. But that doesn't necessarily have to mean loyal as I found out..."

                scene v11src4c
                with dissolve

                ry "Damn. What else?"

                scene v11src4a
                with dissolve

                u "She's talked about being a doctor before. She's into a lot of medical stuff."

                scene v11src4e
                with dissolve

                ry "Okay, so lots of student loan debt, but a good long term paycheck. Very promising."

                scene v11src4d
                with dissolve

                u "Bro, you've talked to other girls, why Emily?"

                scene v11src4e
                with dissolve

                ry "I don't know bro, I'm just really into her. She's fire."

                scene v11src4d
                with dissolve

                u "What do you even like about her though?"

                scene v11src4b
                with dissolve

                ry "I just have that feeling man. Sure there's other girls I find attractive, but it's not all about that with her. I feel something else."

                scene v11src4d
                with dissolve

                u "You're just tryna smash."

                scene v11src4f
                with dissolve

                ry "Nah man... I'm serious."

                scene v11src4a
                with dissolve

                u "Look, I can't tell you everything, that'd just be weird. You'll find more value in getting to know her yourself and her opening up to you."

                scene v11src4
                with dissolve

                ry "True, plus I wouldn't know what to talk about if I knew everything about her."

                scene v11src4d
                with dissolve

                u "See? You got it all figured out. Now let me get some sleep."

            "Don't give blessing":
                scene v11src4a
                with dissolve

                u "Why? You're not trying to talk to my ex are you?"

                scene v11src4f
                with dissolve

                ry "Well I know she's your ex, but I thought since-"

                scene v11src4a
                with dissolve

                u "I don't know what you were thinking, but it needs to be anything except talking to my ex. You should know that's not cool."

                scene v11src4
                with dissolve

                ry "So you're gonna try and get back with her?"

                scene v11src4a
                with dissolve

                u "What? Bro, just leave her alone alright."

                scene v11src4f
                with dissolve

                ry "*Sighs* Fine."

                scene v11src4g # FPP Same angle as v11src4, Ryan looks away from MC, out of the window of the plane
                with dissolve

                pause 0.75

    else: # Talked to Ryan at charity event, but did not give blessing
        scene v11src5 # Show MC's arm resting on arm rest, Ryan's arm next to it beside arm rest
        with dissolve

        u "*Sighs*"

        scene v11src4
        with dissolve

        ry "Aye man, do you mind if I use the armrest?"

        menu:
            "Be a dick":
                $ reputation.add_point(RepComponent.TROUBLEMAKER)
                scene v11src4a
                with dissolve

                u "Oh sure, go ahead and try to get something else I already had."

                scene v11src4h # FPP Same angle as v11src4, Ryan with angry expression, mouth open
                with dissolve

                ry "You don't have to be a dick. At least I came to you about her instead of going behind your back. I showed some respect, too bad you can't return the favor."

                scene v11src4i # FPP Same angle as v11src4, Ryan with angry expression, mouth closed
                with dissolve

                u "She's not even gonna go for you. You're causing a drift between us and wasting your time with her. She's obsessed with me."

                scene v11src4h
                with dissolve

                ry "No she's not, she's told me she cut you off."

                scene v11src4i
                with dissolve

                u "Did she tell you her reason? Doubt it."

                scene v11src4
                with dissolve

                ry "She wanted to focus on herself."

                scene v11src4i
                with dissolve

                u "Keep telling yourself that man, I'm going to sleep."

            "Let him":
                $ reputation.add_point(RepComponent.BRO)
                scene v11src4a
                with dissolve

                u "Yeah man, go ahead."

                scene v11src4
                with dissolve

                ry "This is gonna be a long flight."

                scene v11src4a
                with dissolve

                u "Sure is, I'm gonna have to do some sleeping to pass the time."

                scene v11src4g
                with dissolve

                ry "Yeah, for sure."

    scene v11src6 # TPP Show MC slouching in aisle seat, arms folded across his chest, eyes closed (asleep)
    with dissolve

    pause 0.75
    stop music fadeout 3
    # -Fades to Scene 13-
    jump v11_aubrey_plane_sex