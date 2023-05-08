# SCENE 9: Arrival to France
# Locations: Dock
# Characters: IMRE (Outfit: 2), MC (Outfit: 1), MR. LEE (Outfit: 1), RYAN (Outfit: 1), AMBER (Outfit: 1), RILEY (OUTFIT: 3)
# Time: Evening
# Phone Images: None

label v12_dock_arrival:
    scene v12doa1 # TPP. Show MC walking on the dock, neutral expression, mouth closed
    with dissolve

    pause 1

    play music music.ck1.v12.Track_Scene_9 fadein 2

    scene v12doa2 # TPP. Show Imre running past MC, MC slightly surprised, mouth closed, Imre happy, mouth closed
    with dissolve

    pause 1

    scene v12doa3 # FPP. Imre ahead of MC, Imre smiling, looking at the sky, mouth open as he is screaming, Imre's arms are raised, pointing to the sky
    with dissolve

    imre "I'M IN PARIS BABYYYYYYYYY!!"

    scene v12doa3a # FPP. Same as v12doa3, Imre mouth closed, same pose as v12doa3
    with dissolve

    u "*Laughs*"

    scene v12doa4 # FPP. Mr. Lee standing next to MC, Mr. Lee looking at Imre's direction (same positioning as v12doa3), Mr. Lee slightly annoyed, mouth open
    with dissolve

    lee "We only crossed the border, we're not in Paris yet."

    scene v12doa4a # FPP. Same as v12doa4, Mr. Lee looking at MC, Mr. Lee neutral expression, mouth open
    with dissolve
    
    lee "Students, grab your luggage and get on the bus so we can get to the hotel."

    scene v12doa5 # TPP. Show Ryan walking up to Imre (Same positioning as v12doa3, Imre not in shot), Ryan slight smirk, mouth closed
    with dissolve

    pause 0.75

    scene v12doa3b # FPP. Same as v12doa3, Ryan standing next to Imre, Imre and Ryan looking at each other, Imre slightly annoyed, mouth closed, Ryan slight smirk, mouth open (Imre no longer doing the pose)
    with dissolve

    ry "Hey ho, I'll take ya to the hotel if ya hoes don't tell."

    scene v12doa4b # FPP. Same as v12doa4, Mr. Lee looking at Ryan's direction (same positioning as v12doa3b), Mr. Lee slightly annoyed, mouth open
    with dissolve

    lee "Ryan, you know, they have open fields here in France as well."

    scene v12doa3c # FPP. Same as v12doa3b, Ryan looking at Mr. Lee, Imre looking at Ryan, Ryan slightly sad, mouth open, Imre slight grin, mouth closed
    with dissolve

    ry "Sorry."

    scene v12doa6 # TPP. Show MC and Amber walking towards the bus, mouths closed, slight smile
    with dissolve

    pause 0.75

    scene v12doa7 # FPP. MC is outside the bus, he watches as Riley board the bus (her back is to the camera)
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v12_amber_bus #scene 10