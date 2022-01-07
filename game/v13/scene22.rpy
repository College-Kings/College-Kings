# SCENE 22: Charli talk outside - test
# Locations: Outside hotel
# Characters: AUBREY (Outfit: 3), MC (Outfit: 9), RILEY (Outfit: 2), IMRE (Outfit: 1), RYAN (Outfit: 1)
# Time: Afternoon

label v13s22:
    scene v13s22_1 # TPP. MC, Riley, and Aubrey in that order. Sitting next to MC on curb outside hotel door, MC looking at Riley and Aubrey, Aubrey and Riley looking at MC, Aubrey confused expression, Mouth open, Riley neutral expression. Mouth Closed.
    with dissolve

    au "Please fill me in... 'Cause that shit was odd."

    play music "music/v13/Track Scene 22.mp3" fadein 2

    scene v13s22_2 # FPP. MC looking at Aubrey, Aubrey looking at MC, Aubrey confused expression, mouth closed.
    with dissolve

    u "So, I assume you know about the shit he pulled with framing me for exposing Riley's picture?"

    scene v13s22_2a # FPP. MC looking at Aubrey, Aubrey looking at MC, Aubrey slightly annoyed, mouth open
    with dissolve

    au "Yeah, that was completely fucked up..."

    scene v13s22_2b # FPP. Same as v13s22_2a, Aubrey slightly annoyed, mouth closed.
    with dissolve

    u "Well, after a heart to heart... Riley and I decided to get him back by doing a little prank."

    scene v13s22_2a
    with dissolve

    au "Okay, go on..."

    scene v13s22_2b
    with dissolve

    u "While I was working my magic, I saw that his computer was open and did a little investigation."

    scene v13s22_2a
    with dissolve

    au "And you found...?"

    scene v13s22_2b
    with dissolve

    u "Charli has been writing finals and taking exams for students in Mr. Lee's class, and making bank while at it."

    scene v13s22_3 # FPP. MC looking at Riley, Riley looking at MC, Riley surprised expression, mouth open.
    with dissolve

    ri "How much are we talking?"

    scene v13s22_3a # FPP. Same as v13s22_3, Riley surprised expression, mouth closed.
    with dissolve

    u "This man basically has a whole company."

    scene v13s22_2c # FPP. Same as v13s22_2a, Aubrey surprised expression, mouth open
    with dissolve

    au "So, you ratted him out?"

    if v13_charli_exposed:
        scene v13s22_2d # FPP. Same as v13s22_2c, Aubrey surprised expression, mouth closed.
        with dissolve
        
        u "I sure the fuck did! It's about time he got a taste of his own medicine. He made it worse by trying Mr. Lee like that."

        scene v13s22_3b # FPP. Same as v13s22_3a, Riley slightly annoyed, mouth open.
        with dissolve

        ri "That's gonna make it way worse!"

        scene v13s22_2e # FPP. Same as v13s22_2d, Aubrey slight smile, mouth open
        with dissolve

        au "You ratted him out... I would've made him give me a cut to keep my mouth shut. *Chuckles*"

        scene v13s22_3c # FPP. Same as v13s22_3b, Riley looking at Aubrey, Riley slight smile, mouth open.
        with dissolve

        ri "Not a bad idea... *Chuckles*"

    else:
        scene v13s22_2d
        with dissolve
        
        u "I could've, but I confronted him instead."

        scene v13s22_2c
        with dissolve

        au "How'd he react?"

        scene v13s22_2f # FPP. Same as v13s22_2e, Aubrey slight smile, mouth closed 
        with dissolve

        u "He tried to deny it, then tried threatening me for breaking into his room."

        u "Eventually, he realized he has no choice but to give in and said when we get back he's gonna stay away from me."

        u "From all of us."

        scene v13s22_3d # FPP. Riley reaching for MC's hand, Riley leaning closer to MC, Riley smiling, mouth closed. 
        with dissolve

        pause 0.75

        scene v13s22_4 # FPP. MC looking down at Riley's hand holding his. 
        with dissolve

        au "So, you just let him go? Didn't even make him pay you to stay quiet?"

        scene v13s22_3e # FPP. Same as v13s22_3d. Riley smiling, mouth open.
        with dissolve

        ri "Yeah, that actually would've been a good idea... *Chuckles*"

        scene v13s22_3f # FPP. Same as v13s22_3e. Riley smiling, mouth closed.
        with dissolve

        u "I just let him go, I'd rather not see him again. Dealing with his bullshit isn't worth some dollars."

        scene v13s22_2e
        with dissolve

        au "To you. *Laughs*"

    scene v13s22_3e
    with dissolve

    ri "Charli is done for, guys."

    scene v13s22_2e
    with dissolve

    au "Haha, well... It was nice knowing him."

    scene v13s22_2f
    with dissolve

    u "For who?"

    scene v13s22_3e
    with dissolve

    ri "Outside of hating you for no reason and doing mean shit, he was kind of cool... *Chuckles*"

    scene v13s22_3f
    with dissolve

    u "Wow, thanks..."

    scene v13s22_2g # FPP. Same as v13s22_2a. Aubrey looking at Riley, Aubrey slight smile, mouth open. 
    with dissolve

    au "The picture thing was the last straw for me."

    scene v13s22_3c
    with dissolve

    ri "First and last straw, for me too. That picture was not something I wanted to share with everyone."

    scene v13s22_2g
    with dissolve

    au "Oh my god, Riley... That picture was nothing. We all have a silly childhood picture. *Chuckles*"

    au "I have some crazy pictures and when we go inside, I'll show you. Maybe then you'll stop being so insecure."

    scene v13s22_3c
    with dissolve

    ri "I probably shouldn't have been so serious about the picture, but I think I just felt more disrespected than embarrassed."

    scene v13s22_2g
    with dissolve

    au "Well, the one that disrespected you won't be a problem anymore."

    scene v13s22_3c
    with dissolve

    ri "I was probably being dramatic..."

    scene v13s22_3f
    with dissolve

    u "Probably? *Chuckles*"

    scene v13s22_3e
    with dissolve

    ri "Okay, I definitely was. *Laughs*"

    scene v13s22_6 # FPP. MC looking up at the hotel door, Imre and Ryan walking out of hotel, both slight smile, mouth closed.
    with dissolve

    pause 0.75 

    scene v13s22_7 # FPP. MC looking at Imre, Imre standing on sidewalk infront of door, Imre looking at Aubrey, slight smile, mouth open.
    with dissolve

    imre "What's up ladies? And Aubrey. *Chuckles*"

    scene v13s22_2h # FPP. Aubrey looking at Imre, slight smile, mouth open.
    with dissolve

    au "Eat a dick, Imre. *Chuckles*"

    scene v13s22_7a # FPP. Same as v13s22_7. Imre looking back at the MC, slight smile, mouth open.
    with dissolve

    imre "Haha, alright, don't chew me out just yet... We're kidnapping [name]."

    scene v13s22_7b # FPP. Same as v13s22_7a. Imre slight smile, mouth closed.
    with dissolve

    u "For?"

    scene v13s22_8 # FPP. MC looking at Ryan. Ryan slight smile, mouth open.
    with dissolve

    ry "Remember the event we were supposed to go to?"

    scene v13s22_8a # FPP. Ryan slight smile, mouth closed.
    with dissolve

    u "(Event? What is he... Oh, he's talking about the Simplr thing.)"

    u "Oh, yeah!"

    scene v13s22_9 # TPP. MC starting to get up off the ground
    with dissolve

    pause 0.75

    scene v13s22_10 # FPP. MC standing up looking down at Riley and Aubrey. Both slight smile, mouth closed
    with dissolve

    u "You all good, guys?"

    scene v13s22_10a # FPP. Aubrey and Riley looking at each other, Aubrey grabbing Riley's hand, Aubrey slight smile, mouth open, Riley slight smile, mouth closed.
    with dissolve

    au "We are. C'mon Riley! Let me go show off these baby bloopers. *Laughs*"

    scene v13s22_10b # FPP. Same as v13s22_10, Aubrey and Riley getting up off the ground, both slightly smiling, mouths closed 
    with dissolve

    pause 0.75

    scene v13s22_11 # FPP. MC looking at Aubrey and Riley heading towards the hotel door
    with dissolve

    pause 0.75

    scene v13s22_11a # TPP. Same as v13s22_11, Aubrey and Riley walking inside the hotel
    with dissolve

    pause 0.75

    scene v13s22_12 # TPP. Imre and Ryan standing infront of MC, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v13s23