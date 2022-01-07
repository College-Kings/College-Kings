# SCENE 57: Giving Ms Rose her present
# Locations: Hotel Lobby
# Characters: MC (Outfit: 3), NORA (Outfit: 1), MS. ROSE (Outfit: 1)
# Time: Afternoon

label v13s57:
    scene v13s57_1 # FPP. MC looking at Nora, Nora slight smile, Nora looking at MC, Nora mouth closed
    with dissolve

    u "You wanna call her down here?"

    play music "music/v13/Track Scene 57.mp3" fadein 2

    scene v13s57_1a # FPP. Same angle v13s57_1, Nora looking down at phone, Nora mouth open
    with dissolve

    no "Yeah, I'll call her."

    scene v13s57_1b # FPP. Same angle as v13s57_1, Nora on phone, Nora looking at MC, Nora smile, Nora mouth open
    with dissolve

    no "Hey, do you mind coming down to the lobby?"

    scene v13s57_1c # FPP. Same as v13s57_1b, Nora mouth closed.
    with dissolve

    pause 0.75

    scene v13s57_1b
    with dissolve

    no "No, nothing's wrong. [name] and I just have something we'd like to show you."

    scene v13s57_1c
    with dissolve

    pause 0.75

    scene v13s57_1b
    with dissolve

    no "Sounds good, see you soon."

    #scene v13s57_1d # FPP. Same as v13s57_1a, Nora mouth closed
    scene v13s57a_2b
    with dissolve

    play sound "sounds/rejectcall.mp3"

    u "Is she on the way?"

    scene v13s57_1a
    with dissolve

    no "Yep."

    scene v13s57_2 # FPP. MC looking at Rose walking toward Nora and MC, rose mouth closed.
    with fade

    pause 0.75

    scene v13s57_3 # FPP. Rose close to MC, MC looking at Rose, Rose looking at Nora, Rose mouth open
    with dissolve

    ro "Hey you two, what do you need to show me?"

    scene v13s57_4 # FPP. MC looking at Nora, Nora looking at Rose, Nora happy, Nora mouth open
    with dissolve

    no "Well, now that the trip is coming to an end and it wouldn't have been possible without you, [name] and I wanted to take the time to get you something as a little \"thank you\"."

    scene v13s57_5 # TPP. Nora out of frame, Noras hands in frame, Noras hands presenting perfume, Show Rose reacting behind Noras hands, Rose shocked mouth open
    with dissolve

    ro "Oh, wow... You guys didn't have to do this! But thank you..."

    scene v13s57_3a # FPP. Same as v13s57_3, Rose very happy, Rose mouth open
    with dissolve

    ro "I really appreciate it. This is truly special. *Chuckles*"

    scene v13s57_3b # FPP. Same as v13s57_3a, Rose looking at MC, Rose mouth closed
    with dissolve

    u "Of course, haha. You deserve it."

    scene v13s57_4
    with dissolve

    no "I'm out of money, so [name] was actually the one who paid for it."

    if ms_rose.relationship.value >= Relationship.FWB.value and joinwolves: #sanitizing pathbuilder input
        scene v13s57_6 # TPP. Show Ms Rose sincerely hugging MC, Rose very grateful, Rose mouth open
        with dissolve

        ro "That was very kind of you [name], I won't forget this."

        scene v13s57_3b
        with dissolve

        u "You're more than welcome, really."

    else:
        scene v13s57_3c # FPP. Same as v13s57_3b, Rose looking at MC happy, Rose mouth open
        with dissolve

        ro "I guess it won't be biased if I say I have a favorite student this year then, huh?"

        scene v13s57_3b
        with dissolve

        u "I guess not. *Chuckles*"

    scene v13s57_3c
    with dissolve

    ro "I'm gonna go try this one right now... *Chuckles* Thank you both again."

    scene v13s57_4
    with dissolve

    no "No worries, you really do deserve it."

    scene v13s57_7 # FPP. MC looking at Nora, Nora very happy, Nora hands on hips, Nora looking at MC, Nora mouth open
    with dissolve

    no "That went well I think!"

    scene v13s57_7a # FPP. Same as v13s57_7, Nora smile, Nora mouth closed.
    with dissolve

    u "It did. A few more gifts and we'll get A's all semester. *Laughs*"

    scene v13s57_7
    with dissolve

    no "Haha, that's the plan, right? I'm going to go and take a shower."

    scene v13s57_7a
    with dissolve

    u "Sounds good, I gotta get ready anyway. I'm going out."

    scene v13s57_7b # FPP. Same angle as v13s57_7, Nora flirty, Nora mouth open
    with dissolve

    no "Anywhere special?"

    scene v13s57_7c # FPP. Same as v13s57_7b, Nora mouth closed
    with dissolve

    u "Aubrey and I are just gonna go looking at boats or something like that."

    scene v13s57_7b
    with dissolve

    no "Oh, okay. Well... Have fun."

    scene v13s57_7c
    with dissolve

    u "Thanks. You too, haha."

    scene v13s57_8 # FPP. MC looking at Nora, Nora walking back to her room.
    with dissolve

    pause 0.75

    scene v13s57_9 # TPP. MC walking over to one of the seats in the hotel lobby, slight smile, mouth closed
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v13s58