# SCENE 23: Simplr Event Walk
# Locations: Sidewalk, Simplr Bar Exterior
# Characters: MC (Outfit: 9), RYAN (Outfit: 1), IMRE (Outfit: 1)
# Time: Afternoon

label v13s23:
    scene v13s23_1 # TPP. Show MC, Ryan and Imre walking on the street towards the simplr bar, all slightly smiling, mouths closed
    with fade

    pause 0.75

    play music music.v13_Track_Scene_23 fadein 2

    scene v13s23_2 # TPP. Show MC, Ryan and Imre standing in front of the simplr bar, all slightly smiling, mouths closed
    with dissolve

    pause 0.75

    scene v13s23_3 # FPP. Same positioning as v13s23_2, MC looking at Ryan, Ryan looking at MC, Ryan slight smile, mouth closed
    with dissolve

    u "So, are you guys ready?"

    scene v13s23_3a # FPP. Same as v13s23_3, Ryan slight smile, mouth open
    with dissolve

    ry "I am... Imre's acting like he doesn't want me to come but, I'm on some \"fuck Imre\" vibes right now."

    #scene v13s23_4 # FPP. Same positioning as v13s23_2, MC looking at Imre, Imre looking at Ryan's direction, Imre slightly annoyed, mouth open
    scene v13s23_3b
    with dissolve

    imre "I don't want you to come, but two people isn't enough and Chris didn't wanna go out. So, here we are. It was either Chris or Mr. Lee, and he's a little occupied right now."

    if v13_charli_exposed:
        #scene v13s23_3b # FPP. Same as v13s23_3a, Ryan looking at Imre, Ryan slight smile, mouth open
        scene v13s23_2
        with dissolve

        ry "Oh yeah, what was all that yelling about? Did someone break one of his precious valuables or something?"

        scene v13s23_4a # FPP. Same as v13s23_4, Imre slight smile, mouth open
        with dissolve

        imre "*Laughs* When I got there, Mr. Lee had Charli pinned to the ground..."

        #scene v13s23_3
        scene v13s23_4c
        with dissolve

        u "Long story short, he won't be around anymore."
        u "In fact, I'm pretty sure he's banned from San Vallejo. *Chuckles*"

        #scene v13s23_3a
        #scene v13s23_2
        #with dissolve
        #ry "What do you mean?"
        #scene v13s23_3
        #with dissolve

        scene v13s23_4b # FPP. Same as v13s23_4, Imre looking at MC, Imre slight smile, mouth open
        with dissolve

        imre "Shit, dude... You really got rid of that rat?"

        scene v13s23_4c # FPP. Same as v13s23_4b, Imre slight smile, mouth closed
        with dissolve

        u "Hell yeah I did. He kind of did it to himself but, I just had to press the right button. *Chuckles*"

        #scene v13s23_3b
        scene v13s23_2
        with dissolve

        ry "Well, good. Now Imre can stop talking about how he's gonna kick his ass every day. *Chuckles*"

    scene v13s23_3
    with dissolve

    u "*Sighs* You guys really do go at it like a married couple, aren't you guys excited for this? I know I am!"

    #scene v13s23_3a
    scene v13s23_2
    with dissolve

    ry "Hell yeah, and Imre should be. Today he'll finally see a real girl."

    scene v13s23_4
    with dissolve

    imre "Shut the fuck up."

    #scene v13s23_3b
    scene v13s23_2
    with dissolve

    ry "*Laughs*"

    #scene v13s23_3
    #with dissolve

    u "Let's get over there."

    scene v13s23_5 # TPP. Show MC, Ryan and Imre walking into the bar, camera behind their backs
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v13s24