# SCENE 27: Econ Class
# Location: Econ Class
# Characters: MC (Outfit 3), Lauren (outfit1), Riley(outfit1), Ryan(outfit1), Ms. Rose(outfit1), 
# Time: Tuesday Morning
    # -MC wakes up and hears his alarm going off-

label v10_econ_class:
    play music "music/v10/Track Scene 27.mp3" fadein 2
    if joinwolves:
        scene v10eco1 # TPP. Show MC in his room, Slight worried face, mouth closed (wolves)
        with fade
    else:
        scene v10eco9 # TPP. Show MC in his room, Slight worried face, mouth closed (apes)
        with fade
    u "(Oh shit I'm gonna be late for class if I don't hurry.)"

    scene v10eco2 # TPP. Show MC Walking into Econ Class, mouth closed
    with fade

    u "(Whew, made it.)"

    scene v10eco3 # FPP. Show Lauren and Riley Sat with a space beteen them, looking at camera (Mc is going to sit there)
    with dissolve


    if CharacterService.is_girlfriend(lauren):
        scene v10eco4 # FPP. Show Lauren, Slight smile, mouth open
        with dissolve

        la "Hey babe, I was starting to get a little worried. It's not like you to show up right on time."

    else:
        scene v10eco4
        with dissolve

        la "Someone's cutting it close."

    scene v10eco4a # FPP. Same Camera, mouth closed
    with dissolve

    u "Tell me about it, I slept through my alarm."

    scene v10eco5 # FPP. Show Riley, slight smile, mouth open
    with dissolve

    ri "Well after hanging all last night I bet you were tired."

    if joinwolves:
        scene v10eco6 # FPP. Show Ryan in seat on other side of room, mouth open
        with dissolve

        ry "What were you out doing?"

    else:
        scene v10eco6
        with dissolve

        ry "Wait, you were out having fun and didn't invite your main brother?"

    if CharacterService.is_girlfriend(lauren):
        scene v10eco4
        with dissolve

        la "I didn't know you were out last night. What were you up to?"

    else:
        scene v10eco4
        with dissolve

        la "Where was my invite?"

    scene v10eco5
    with dissolve

    ri "*Laughs* [name] was at the skatepark getting lessons and I saw him when I was leaving the library."
    ri "From what I saw he wouldn't have wanted anyone there. He did more falling than skating."

    scene v10eco6
    with dissolve

    ry "Sounds like [name]. *Chuckles*"

    scene v10eco4
    with dissolve

    la "I didn't even know you were wanting to learn how to skate. *Chuckles*"

    scene v10eco4a
    with dissolve

    u "Wanted to wait until I was good before I started showing off."

    scene v10eco6
    with dissolve

    ry "Probably a good idea."

    scene v10eco7 # FPP. Show Ms. Rose at the front of class, mouth open.
    with dissolve

    ro "*Smiling* Alright class! Today we're doing something a little different."

    scene v10eco7a # FPP. same 7, mouth closed
    with dissolve

    u "(She sure is in a good mood.)"

    scene v10eco7
    with dissolve

    ro "Today I'm gonna be teaching you all how to ensure your own independence."

    ro "In life you can't always depend on others, even those you think you can depend on."

    ro "So today, in Econ, we're gonna be learning financial independence."

    scene v10eco7a
    with dissolve

    u "(Okay, a little self reflecting.)"

    scene v10eco7
    with fade

    ro "Have your own bank account."

    scene v10eco7
    with fade

    ro "Make sure your credit is good as well."

    scene v10eco7
    with fade

    ro "Ask yourself if you've invested in your own wishes too."

    scene v10eco4
    with dissolve


    la "That was an... interesting class."

    scene v10eco5
    with dissolve

    ri "Yeah, I wonder why she switched class up like that."

    scene v10eco6
    with dissolve

    ry "Hey it works for me, I enjoyed it."

    scene v10eco4
    with dissolve

    la "You were asleep though. *Laughs*"

    scene v10eco6
    with dissolve

    ry "And that's why I enjoyed it. *Laughs*"

    scene v10eco7
    with dissolve

    ro "[name] do you mind if I speak to you for a moment?"

    scene v10eco6
    with dissolve

    ry "Someone's in trouble."

    scene v10eco6a # FPP. same 6, mouth closed
    with dissolve

    u "Oh shut up."

    scene v10eco7
    with dissolve

    u "Yeah?"

    scene v10eco8 # FPP. MC now stood infront of Ms rose at front of class, Show Ms. Rose, mouth open
    with dissolve

    if joinwolves:
        if CharacterService.is_kissed(ms_rose):
            ro "I just wanted to see how you were doing after... everything."
            
            scene v10eco8a # FPP. same 8, mouth closed.
            with dissolve

            u "Uhm, yeah I'm... fine. You?"

            scene v10eco8
            with dissolve

            ro "Yeah, uhm. I'm actually really happy."

        else:
            ro "I just wanted to see how you were doing after... everything."

            scene v10eco8a
            with dissolve

            u "Ha, I should be asking you that. Especially after that lesson."

            scene v10eco8
            with dissolve

            ro "That lesson was the happiest I've been while teaching."

            scene v10eco8a
            with dissolve

            u "You did sound pretty enthusiastic."

        menu:
            "Ask about Nora":
                scene v10eco8a
                with dissolve

                u "You know Ms. Rose, I was actually hoping to talk to you about the other night."

                scene v10eco8
                with dissolve

                ro "Please [name], when we're alone you can call me Lorraine."

                scene v10eco8a
                with dissolve

                u "Uhm... sure Lorraine. *Chuckles* The other night."
                
                u "when I was leaving, I happened to see Nora walking up and heard her say she had just got to her stepmom's house."

                scene v10eco8
                with dissolve

                ro "*Sighs* When she came in right after you left I wondered if you'd seen her."

                $ grant_achievement("family_secrets")

                ro "It's true, she's my stepdaughter. But since we both attend SVC we do our best to keep our relationship unknown."

                scene v10eco8a
                with dissolve

                u "I understand, that makes sense. Do you two have a good relationship?"

                scene v10eco8
                with dissolve

                ro "I've built a very good relationship with her since Lucious was gone all the time."

                ro "As Nora was growing up, most days it was just her and I."

                ro "Her biological mother passed away so I'm all she really has."

                ro "It's almost as if I'm her older sister honestly."

                scene v10eco8a
                with dissolve

                u "That's actually really nice. You just may have to tell me some good stories every once in a while."

                scene v10eco8
                with dissolve

                ro "I'm sure I could."

                scene v10eco8a
                with dissolve

                u "I'm glad to see you happy... Lorraine. *Chuckles*"

                scene v10eco8
                with dissolve

                ro "You helped a lot with that."

                scene v10eco8a
                with dissolve

                u "I'm glad I could."

                scene v10eco8
                with dissolve

                ro "Enjoy the rest of your day [name]."

                scene v10eco8a
                with dissolve

                u "You too."

            "Don't ask":
                scene v10eco8a
                with dissolve

                u "(It's obviously a private matter.)"

                u "I'm glad to see you happy Ms. Rose."

                scene v10eco8
                with dissolve

                ro "Please [name], when we're alone you can call me Lorraine."

                scene v10eco8a
                with dissolve

                u "I can manage that."

                scene v10eco8
                with dissolve

                ro "Enjoy the rest of your day [name]."

                scene v10eco8a
                with dissolve

                u "You too... Lorraine. *Chuckles*"

    else:

        scene v10eco8
        with dissolve

        ro "I'm just curious how you're feeling about this class."

        scene v10eco8a
        with dissolve

        u "I'm liking it."

        scene v10eco8
        with dissolve

        ro "Okay, well I noticed you seemed a little distracted and I wanted to make sure everything was good."

        scene v10eco8a
        with dissolve

        u "All is good."

        scene v10eco8
        with dissolve

        ro "Alright, come to me if you need anything."

        scene v10eco8a
        with dissolve

        u "Will do."
    stop music fadeout 3
    jump v10_talk_nora

    # -Transition to Scene 28-
