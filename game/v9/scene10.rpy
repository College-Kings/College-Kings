# SCENE 10: HISTORY CLASS
# Locations: College Hallways, History Class
# Characters: MC (Outfit 1), Imre (Outfit 2), Penelope (Outfit 1), Cameron (Outfit 2), Mr. Lee (Outfit 2), Random Classmate (Outfit 1)
# Time: Thursday Morning

label v9_history_class:
    scene v9hc1 # TPP. Show MC running down the college college hallway towards Mr. Lees class, camera from behind.
    with fade

    play music "music/v9/Track Scene 10.mp3" fadein 2

    pause 1

    scene v9hc2 # TPP. Show MC walking through the door into Mr. Lees class, MC looks out of breath.
    with dissolve

    pause 1

    scene v9hc3 # FPP. Show Mr. Lee stood at the front of the class looking at camera, Mr. Lee neutral expression, mouth open.
    with dissolve

    lee "[name], so nice of you to join us."

    if not joinwolves:
        scene v9hc4 # TPP. Show MC taking a seat next to Random Classmate, MC looks a bit embrassed.
        with dissolve

        pause 1

        jump v9_hc_cont1

    else:
        scene v9hc5 # TPP. Show MC taking a seat next to Imre, MC looks a bit embarrassed.
        with dissolve

        pause 0.5

        scene v9hc6 # FPP. Close up of Imre who is sat next to MC, Imre looking at camera, Imre slight smile, mouth open.
        with dissolve

        imre "You good, dude?"

        scene v9hc6a # FPP. Same camera as v9hc6, Imre mouth closed.
        with dissolve

        u "Yeah, just lost track of time."

        jump v9_hc_cont1

label v9_hc_cont1:
    scene v9hc7 # FPP. Show Mr. Lee pacing the front of the classroom, mouth open.
    with dissolve

    lee "I have an exciting class planned for you today."

    scene v9hc7a # FPP. Same camera as v9hc7, Mr. Lee, now stood somewhere else at the front of the class, mouth closed.
    with dissolve

    menu:
        "Heckle":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            jump v9_hc_heckle
        "Stay quiet":
            jump v9_hc_quiet

label v9_hc_heckle:
    u "Yeah, right! I can count on my naps in this class like clockwork."

    scene v9hc7b # FPP. Same camera as v9hc7, Mr. Lee looking at camera (MC), slight angry expression, mouth open.
    with dissolve

    lee "As reflected in your grades."

    jump v9_hc_cont2

label v9_hc_quiet:
    u "(Not likely.)"

    jump v9_hc_cont2

label v9_hc_cont2:
    scene v9hc8 # FPP. Show Mr. Lee stood at his desk picking up a large sword. Mr. Lee mouth open.
    with dissolve

    lee "You're going to perform short scenes based on life in a Viking village. This..."

    scene v9hc8a # FPP. Same camera as v9hc8, Mr. Lee looking at the class waving the sword around, mouth open.
    with dissolve

    lee "...is not a prop. It's from my personal collection, so no touching. But there will be other props for you to use."

    scene v9hc8b # FPP. Same camera as v9hc8, Mr. Lee placing the sword back on his desk, mouth open.
    with dissolve

    lee "Now, once I separate you into small groups, I want you to think about what life would have been like in a Viking village, and come up with a short scenario to act out."
    lee "There's a box of props in the corner at your disposal. Sorry, no real swords."

    scene v9hc8c # FPP. Same camera as v9hc8, Mr. Lee now stood next to his desk looking at the class, mouth closed.
    with dissolve

    u "(Awww, too bad.)"

    scene v9hc8d # FPP. Same camera as v9hc8, Mr. Lee now stood next to his desk looking at the class, gesturing someone to come up, mouth open.
    with dissolve

    lee "[name], Penelope, and Cameron, please come to the front."

    scene v9hc9 # FPP. Show Penelope getting up from her seat, smile, mouth open.
    with dissolve

    pe "This is gonna be so cool."

    scene v9hc10 # FPP. Show Cameron getting up from his seat, grumpy, mouth open.
    with dissolve

    ca "Whatever. I just wanna go back to bed."

    if not joinwolves:
        scene v9hc11 # TPP. Show MC getting up from his seat.
        with dissolve
    else:
        scene v9hc11a
        with dissolve

    pause 0.75

    scene v9hc12 # FPP. Show Cameron and Penelope at the front of the class looking inside a box of props with Mr. Lee. Camera as if MC is walking down the ailse towards the front of the class.
    with dissolve

    menu:
        "Grumble with Cameron":
            $ reputation.add_point(RepComponent.BRO)
            jump v9_hc_grumble
        "Be happy with Penelope":
            jump v9_hc_penelope

label v9_hc_grumble:
    u "Yeah we're gonna be screwed. Mr. Lee's already mad at me for being late."

    scene v9hc12a # FPP. Same camera as v9hc12, Cameron and Penelope now stood up. Cameron looking and pointing at camera, mouth open.
    with dissolve

    ca "See!"

    scene v9hc13 # TPP. Show MC now stood at the front of the class with Cameron, Penelope and Mr. Lee, Penelope looking at Cameron and MC, pen mouth open.
    with dissolve

    pe "Come on, guys. Let's make the most of it."

    jump v9_hc_cont3 

label v9_hc_penelope:
    u "Vikings! This'll be great! Wish we could have kept the sword, though."

    scene v9hc12a
    with dissolve

    ca "Now THAT would have been awesome!"

    scene v9hc13
    with dissolve

    pe "Ugh, boys."

    jump v9_hc_cont3

label v9_hc_cont3:
    scene v9hc14 # FPP. Show Penelope and Cameron, neutral expressions, mouths closed.
    with dissolve

    u "What props did we get?"

    scene v9hc15 # FPP. Show Cameron revealing a wig and placing it on his head, looking grumpy, mouth closed.
    with dissolve

    pause 1

    scene v9hc16 # FPP. Show Penelope revealing a long beard and placing it on her chin, laughing, mouth closed.
    with dissolve

    pause 1

    scene v9hc17 # TPP. Show MC going into the prop box and grabbing a fake sword.
    with dissolve

    pause 1

    scene v9hc18 # TPP. Show Cameron, Penelope and Mr. Lee looking at MC who is now holding the fake sword, Cameron grumpy, mouth open.
    with dissolve

    ca "No fair! I didn't see that!"

    scene v9hc19 # FPP. Close up Cameron looking grumpy, mouth closed.
    with dissolve

    u "You don't want to do your work anyway. And besides, you look cute."

    scene v9hc20 # TPP. Show Cameron punching MC on the arm, MC laughing.
    with dissolve

    pause 0.5

    scene v9hc21 # FPP. Show Penelope and Cameron, Penelope looking at Cameron, Penelope smile, Cameron grumpy. Pen mouth open.
    with dissolve

    pe "He's right, Cameron. You look beautiful."

    scene v9hc21a # FPP. Same camera as v9hc21, Penelope strokes her beard, giggle, mouth open.
    with dissolve

    pe "I'm so proud to call you my wife."

    scene v9hc21b # FPP. Same camera as v9hc21, Pen and cam both looking at camera, Pen smile, cam grumpy, mouths closed.
    with dissolve

    u "Perfect! You're the Viking King and Cameron's your lovely bride."

    scene v9hc21c # FPP. Same camera as v9hc21, both looking at camera, pen smile cam grumpy, cam mouth open.
    with dissolve

    ca "No the hell I'm not!"

    scene v9hc21d # FPP. Same camera as v9hc21, Pen looks at cam, pen giggle, mouths closed.
    with dissolve

    u "Now, what scene do we want to do?"

    scene v9hc22 # FPP. Close up Mr. Lee, mouth open.
    with dissolve

    lee "Alright class, that's enough prep time. Who wants to go first?"

    scene v9hc21e # FPP. Same camera as v9hc21, Pen raises arm, Cameron looks at her like wtf pen smile mouths closed.
    with dissolve

    menu:
        "Be scared":
            jump v9_hc_scared
        "Be ready":
            $ reputation.add_point(RepComponent.BRO)
            jump v9_hc_ready
        
label v9_hc_scared:
    u "We can't go first."

    scene v9hc21f # FPP. Same camera as v9hc21, both looking at camera, pen smile cam grumpy, pen mouth open.
    with dissolve

    pe "Relax, we got this."

    scene v9hc21c
    with dissolve

    ca "Let's just get it over with."

    jump v9_hc_cont4

label v9_hc_ready:
    u "We got this."

    scene v9hc21c
    with dissolve

    ca "You two are nuts."

    jump v9_hc_cont4

label v9_hc_cont4:
    scene v9hc22
    with dissolve

    lee "[name], Penelope, and Cameron. Show us what you came up with."

    stop music fadeout 3

    scene black
    with fade

    u "Imagine this... the year is 950, and your ship just landed at port. There's a bald burly guard waiting to take his dues off you. Behind him is your next target... a line of small wooden huts, ripe for plundering."

    jump v9_hc_demo
    
label v9_hc_return:
    scene v9hc23 # TPP. Show Pen cam MC with their props, Mr. Lee stood looking at them, lee mouth open.
    with fade

    play music "music/v9/Track Scene 10.mp3" fadein 2

    lee "Great job! I'm impressed. That's going to be hard to beat."

    scene v9hc24 # TPP. Show pen cam mc placing their props back into the prop box.
    with dissolve

    pause 1 

    scene v9hc25 # TPP. Show pen cam mc walking back to their desks.
    with dissolve

    pause 1

    if not joinwolves:
        scene v9hc26 # TPP. Show MC sitting back at his desk.
        with dissolve
    else:
        scene v9hc26a
        with dissolve

    stop music fadeout 3
    
    scene clocka
    with fade

    play sound sound.clock2

    pause (0.5)

    scene clockb
    with dissolve

    pause (0.5)

    scene clockc
    with dissolve

    pause (0.5)

    scene clockd
    with dissolve

    pause (0.5)

    stop sound

    scene clocke
    with dissolve
    
    jump v9_hallway
