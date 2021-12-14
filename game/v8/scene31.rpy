# Economics Class
# Location: Economics Class
# Outfits: MC Outfit 2, Ryan Outfit 1, Lauren Outfit 3, Ms. Rose Outfit 1, Riley Outfit 4 (Make sure to use .duf where Riley is wearing glasses)
# Time: Tuesday Morning

label v8_tues_eco_class:
    scene v8stec1 # FPP. Sweeping shot of the economics class, show Riley, Lauren and Ryan all sat on the back row.
    with Fade(0.75, 2, 0.75)

    pause 0.5

    scene v8stec2 # TPP. Show MC sitting down inbetween Riley and Lauren, Riley & Lauren looking at MC.
    with dissolve

    pause 0.5

    play music "music/m16punk.mp3"

    scene v8stec3 # FPP. Show Ms Rose stood at the front of the class, mouth open looking around at class, mouth open.
    with dissolve

    ro "Good morning, class. Let's get right to it. We've got a lot to cover."

    scene v8stec3a # FPP. Same camera as v8stec3, Ms. Rose pacing side to side at the front of the class, questioning gesture, mouth open.
    with dissolve

    ro "Now, let's discuss the difference between Macroeconomics and Microeconomics. Who wants to tell me what Macroeconomics means?"

    scene v8stec4 # TPP. Show MC in his seat yawning, looking tired, mouth closed.
    with dissolve

    u "(It's too early for this stuff.)"

    scene v8stec5 # FPP. Close up Riley, Riley turns to the side in her seat to look at camera (MC). Riley smile, mouth closed.
    with dissolve

    u "They look great!"

    scene v8stec5a # FPP. Same camera as v8stec5, Riley smile, mouth open.
    with dissolve

    ri "Thanks!"

    scene v8stec5
    with dissolve

    u "Can you see better?"

    scene v8stec5a
    with dissolve

    ri "Yes! Not sure how I managed before now."

    scene v8stec5
    with dissolve

    if riley.relationship.value >= Relationship.FWB.value:
        u "It's too bad, though."

        scene v8stec5b # FPP. Same camera as v8stec5, Riley confused, mouth open.
        with dissolve

        ri "Why?"

        scene v8stec5c # FPP. Same camera as v8stec5, Riley confused, mouth closed.
        with dissolve

        u "You made such a cute face squinting to see the board."

        scene v8stec5
        with dissolve

        ri "Awww thanks [name]!"

    else:
        u "I bet!"

    scene v8stec3b # FPP. Same camera as v8stec3, Ms. Rose stood somewhere else at the front of the class, explanation gesture, looking at class, mouth open.
    with dissolve

    ro "Microeconomics, on the other hand, is all about how each individual interacts with the economy."

    scene v8stec6 # FPP. Show Ryan, Ryan turns head to face camera, Ryan neutral expression, mouth closed.
    with dissolve

    u "Hey."

    if joinwolves:
        scene v8stec6a # FPP. Same camera as v8stec6, Ryan neutral expression, mouth open
        with dissolve

        ry "Sup?"

        scene v8stec6
        with dissolve

        u "Tired."

        scene v8stec6a
        with dissolve

        ry "Yeah, this ain't helping."

        scene v8stec6
        with dissolve

        u "For sure!"

        scene v8stec6b # FPP. Same camera as v8stec6, Ryan smile, mouth open.
        with dissolve

        ry "If I start snoring, just nudge me."

        scene v8stec6c # FPP. Same camera as v8stec6, Ryan smile, mouth closed.
        with dissolve

        u "Only if you do the same for me."

        jump tec_cont

    else:
        scene v8stec6b
        with dissolve

        ry "Bro! How's your new room?"

        scene v8stec6c
        with dissolve

        u "It's good."

        scene v8stec6a
        with dissolve

        ry "Surprised you can sleep at all with the noise."

        scene v8stec6
        with dissolve

        menu:
            "Confide in Ryan":
                $ add_point(KCT.BRO)
                jump tec_conf_ryan
            "Play it cool":
                jump tec_cool_ryan

label tec_conf_ryan:
    u "Yeah it wasn't easy, but luckily I'd do anything to stop studying."

    scene v8stec6b
    with dissolve

    ry "I had trouble my first couple nights, too. But you get used to it. And Grayson will make sure you're drunk enough to pass out every night if you let him."

    jump tec_cont

label tec_cool_ryan:
    u "Nah, one page of my Econ book and I'm out! Might come back to haunt me today, though."

    scene v8stec6d # FPP. Same camera as v8stec6, Ryan laugh, mouth open.
    with dissolve

    ry "Mine's history. I'm surprised I haven't flunked out."

    scene v8stec6c
    with dissolve

    u "Julia would kill me if I did."

    scene v8stec6d
    with dissolve

    ry "Shit, my parents, too!"

    jump tec_cont

label tec_cont:
    scene v8stec3c # FPP. Same camera as v8stec3, Ms. Rose stood near her desk, looking at the class, mouth open.
    with dissolve

    ro "Some of the terms you may already know from daily life would be inflation and capital. We're gonna spend this hour digging into the meat of..."

    scene v8stec7 # TPP. Show MC yawning in his chair.
    with dissolve

    pause 0.5

    if lauren.relationship.value >= Relationship.GIRLFRIEND.value:
        scene v8stec8 # FPP. Show Lauren, Lauren looking at camera, Lauren smile, mouth open.
        with dissolve

        la "Babe, you're gonna get me started."

        scene v8stec8a # FPP. Same camera as v8stec8, Lauren smile, mouth closed.
        with dissolve

        u "Sorry, I just can't focus."

        menu:
            "Flirt with Lauren":
                $ add_point(KCT.BOYFRIEND)
                jump fl_w_lau

            "Don't flirt with Lauren":
                jump no_fl_w_lau

    else:
        jump tec_end_time

label fl_w_lau:
    u "You're too beautiful. It's distracting."

    scene v8stec8b # FPP. Same camera as v8stec8, Lauren looking flattered, mouth open.
    with dissolve

    la "Awww, you're so sweet. What would I do without you?"

    scene v8stec8a
    with dissolve

    u "I don't want to ever find out."

    scene v8stec9 # TPP. Show MC kissing Lauren on the cheek, Lauren looking a little shocked, mouth closed.
    with dissolve

    pause 0.5

    scene v8stec8b
    with dissolve

    la "Now pay attention before we get in trouble."

    scene v8stec8a
    with dissolve

    u "Yes, ma'am."

    jump tec_end_time

label no_fl_w_lau:
    u "I don't know who thought a 9 a.m. Econ class was a good idea."

    scene v8stec8
    with dissolve

    la "Probably the person who picked your schedule... oh wait, that's you."

    scene v8stec8a
    with dissolve

    u "Remind me to have a talk with myself after my nap."

    scene v8stec8
    with dissolve

    la "You're impossible."

    scene v8stec8a
    with dissolve

    u "But you love it."

    scene v8stec8c # FPP. Same camera as v8stec8, Lauren looks a little shocked, mouth closed.
    with dissolve

    u "(Shit!)"

    menu:
        "Play it off":
            jump tec_lau_off
        "Go with it":
            jump tec_lau_roll

label tec_lau_off:
    u "Like! You like it."

    scene v8stec8
    with dissolve

    la "I like it a lot."

    scene v8stec8a
    with dissolve

    u "(Whew!)"

    jump tec_end_time

label tec_lau_roll:
    scene v8stec10 # TPP. Show MC winking at Lauren, Lauren giggling, mouths closed.
    with dissolve

    pause 0.5

    jump tec_end_time

label tec_end_time:
    scene v8stec11 # FPP. Show Ms Rose stood behind her desk, adressing class, mouth open.
    with dissolve

    ro "Who wants to tell the class what they know about the free market?"

    stop music fadeout 3

    play sound "sounds/clock2.mp3"
    scene clocka
    with fade
    pause 0.5

    scene clockb
    with dissolve
    pause 0.5

    scene clockc
    with dissolve
    pause 0.5

    scene clockd
    with dissolve
    pause 0.5

    scene clocke
    with dissolve
    pause 0.5

    jump mr_aft_class
