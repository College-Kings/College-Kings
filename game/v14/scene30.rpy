# SCENE 30: Photoshoot with Chloe PLUSH WOLF
# Locations: The woods
# Characters: CHLOE (Outfit: 1), MC (Outfit: 2)
# Time: Afternoon

label v14s30:
    scene v14s30_1 # TPP. Show MC walking in the woods towards the photoshoot location, Slight smile, mouth closed.
    with dissolve

    pause 0.5

    play music "music/v13/Track Scene 59_1.mp3" fadein 2

    scene v14s30_2 # TPP. Show MC finding Chloe in the woods pressing button on the camera, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v14s30_3 # FPP. MC looking at Chloe play with the camera, Chloe not realizing MC is there yet, Chloe slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v14s30_3a # FPP. Same as v14s30_3, Chloe turns to see MC, slight smile, mouth open.
    with dissolve

    cl "[name], there you are!"

    scene v14s30_3b # FPP. Same as v14s30_3a, Chloe walking towards MC, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v14s30_3c # FPP. Same as v14s30_3b, Chloe standing infront of MC, Looking at MC, Chloe slight smile, mouth closed.
    with dissolve

    u "Hey, how's it going?"

    scene v14s30_3d # FPP. SAme as v14s30_3c, Chloe slight smile, mouth open.
    with dissolve

    cl "Not too bad... Although, this thing was definitely NOT cheap."

    scene v14s30_3c
    with dissolve

    u "How bad was it?"

    scene v14s30_3d
    with dissolve

    cl "Well, for it being the only one left at the auction, let's just say it was right under our budget."

    scene v14s30_3c
    with dissolve

    u "Damn."

    if v14_chrissupport >= 2:
        scene v14s30_3d
        with dissolve

        cl "Chris helped a bit though, so that was nice."

    scene v14s30_3c
    with dissolve

    u "This better be a nice ass toy..."

    scene v14s30_3d
    with dissolve

    cl "Haha, it is pretty fancy!"

    cl "As soon as we're all set up, I'm just gonna take a few shots and then we can pick our favorites."

    scene v14s30_3c
    with dissolve

    u "So, it's just you and the wolf?"

    scene v14s30_3d
    with dissolve

    cl "Yeah, I kinda felt like it was too much to ask individual people to get involved, you know?"

    scene v14s30_3c
    with dissolve

    u "Or did Chris tell you that... *Chuckles*"

    scene v14s30_3d
    with dissolve

    cl "Okay, yes..."

    cl "As long as they are supporting me I'm happy."

    scene v14s30_3c
    with dissolve

    u "Can't go wrong with that."

    scene v14s30_3d
    with dissolve

    cl "Okay so..."

    scene v14s30_4 # TPP. Close up of only Chloe. Show Chloe walking over to the front of the Camera, Slight Smile, mouth closed.
    with dissolve

    pause 0.75

    scene v14s30_4a # TPP. Same as v14s30_4, Chloe infront of the camera in position for the pictures, slight smile, mouth closed.
    with dissolve

    u "You want me to take them?"

    scene v14s30_4b # TPP. Same as v14s30_4a, Chloe slight smile, mouth open.
    with dissolve

    cl "Yes... Please. *Laughs*"

    scene v14s30_5 # TPP. Close up Camera view infront of the photoshoot camera, looking at Chloe and the plush wolf, Chloe slight smile, mouth closed.
    with dissolve

    u "Okay, ready when you are."

    menu:
        "Take Picture":
            scene v14s30_5a # TPP. Same as v14s30_5, Chloe posing with her hand on her hip, Chloe proud smile, mouth closed
            with flash

    menu:
        "Take Picture":
            scene v14s30_5b # TPP. Same as v14s30_5a, Chloe holding the plush wolf with one arm and her other hand in the air like she is cheering, slight smile, mouth closed.
            with flash

    menu:
        "Take Picture":
            scene v14s30_5c # TPP. Same as v14s30_5b, Chloe in a new pose, slight smile, mouth closed.
            with flash

    menu:
        "Take Picture":
            scene v14s30_5d # TPP. Chloe standing normally infront of the camera, slight smile, mouth closed.
            with flash

    u "Okay, I think I've got a pretty good selection to choose from."

    scene v14s30_6 # FPP. Chloe walking over to MC off the photoshoot spot, Chloe slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v14s30_6a # FPP. Chloe standing infront of MC, slight smile, mouth open.
    with dissolve

    cl "How do they look? Too cheesy?"

    scene v14s30_6b # FPP. Same as v14s30_6a, Chloe slight smile, mouth closed.
    with dissolve

    u "Haha, no. You look great as always."

    if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
        scene v14s30_7 # TPP. Show Chloe kissing MC passionately.
        with dissolve

        pause 0.75

        scene v14s30_7a # TPP. Same as v14s30_7, Chloe and MC kissing put a different position.
        with dissolve

        pause 0.75

        scene v14s30_6a
        with dissolve

        cl "Thank you."

        scene v14s30_6b
        with dissolve

        u "Of course."

    scene v14s30_6a
    with dissolve

    cl "Okay, we can leave the stuff here because I think some of The Wolves wanted to... play with it. *Laughs*"

    scene v14s30_6b
    with dissolve

    u "Haha, what?"

    scene v14s30_6a
    with dissolve

    cl "I try not to ask too many questions, you know?"

    cl "Alright, let's head back and look at these closely so we can pick a good one."

    scene v14s30_8 # TPP. Show MC and Chloe walking together out of the woods, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v14s30b