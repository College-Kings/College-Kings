# SCENE 07: Hotel Lobby Trip Review and Going to The Airport
# Locations: Hotel Lobby
# Characters: MS. ROSE (Outfit: 1), CHRIS (Outfit: 1), AUBREY (Outfit: 1), RILEY (Outfit: 2), MC (Outfit: 5), IMRE (Outfit: 1), NORA (Outfit: 2)
# Time: Morning

label v14s07:
    play music "music/v12/Track Scene 27_1.mp3" fadein 2

    scene v14s07_1 # TPP. # MC arrives in the hotel lobby and he sees Aubrey and Riley together holding their bags, looking at each other with flirtatious expressions, mouths closed, Imre standing with Chris both of them with concerned expression looking over at Ms. Rose and Nora, Ms. Rose with a hand on Nora's soulder both of them looking at each other, slight frowns, mouths closed
    with dissolve

    pause 0.75

    scene v14s07_1a # TPP. same as v14s07_1 Ms. Rose walks away from nora to stand in front of and face the students, mc has walked closer to aubrey standing her right and riley is standing on aubreys left
    with dissolve

    pause 0.75

    scene v14s07_2 # FPP. show just Ms. Rose in hotel lobby, full smile, mouth open, one arm raised
    with dissolve

    ro "Students, thank you all for being quick and ready to head back home."

    scene v14s07_2a # FPP. same asv14s07_2 ms rose has put her hand down
    with dissolve

    ro "I've enjoyed this trip quite a bit, but I am very much ready to head home."

    scene v14s07_2b # FPP. same as v14s07_2a Ms. Rose looks to her left, mouth closed
    with dissolve

    ch "I couldn't agree more."

    scene v14s07_2a
    with dissolve

    ro "We all have a life to get back to in San Vallejo and the lives you have on campus, certainly need you all back."

    scene v14s07_2
    with dissolve

    ro "I'm aware that you all became very involved in this adventure..."

    scene v14s07_3 # FPP. Mc looks to his left and sees aubrey looking at riley with a flirtatious look, mouth open, and riley looking at aubrey with a shocked expression mouth open
    with dissolve

    au "*Whispers* Involved with each other..."

    scene v14s07_3b
    with dissolve
    
    pause 0.5

    scene v14s07_3a # FPP. same as v14s07_3 aubrey mouth closed
    with dissolve

    ri "*Whispers* Oh my god, Aubrey! Haha, shhh..."

    scene v14s07_3b # FPP. same as v14s07_3a riley half smile, mouth closed
    with dissolve

    u "(Look at them. All... lovey dovey.)"

    scene v14s07_2a
    with dissolve

    ro "There were memories made..."

    if mc.frat == Frat.WOLVES and ("v12_rose" in sceneList or "v11_rose" in sceneList):
        scene v14s07_2 # FPP. same as v14s07_2a Ms. Rose makes direct eye contact with mc
        with dissolve

        ro "Some of my most unforgettable experiences happened on this journey, as have yours."

        scene v14s07_2c
        with dissolve

        u "(Okay Rose, let's try to be a little less obvious here.)"

        scene v14s07_2a
        with dissolve

        ro "Maybe one day I'll come back here to create even more memories, but with someone special."

    scene v14s07_2
    with dissolve

    ro "You should all consider coming back to these beautiful countries some time, and enjoy it with your new found freedom and someone special by your side."

    scene v14s07_4 # FPP. show just imre looking at ms rose, full smile, mouth open
    with dissolve

    imre "*Laughs* Not anytime soon."

    scene v14s07_2d # FPP. same as v14s07_2b ms. rose looks to her right, mouth open
    with dissolve

    ro "Maybe not..."

    scene v14s07_4a # FPP. same as v14s07_4 Imre is blushing and smiling after Ms. Rose laughs and smiles at him
    with dissolve

    pause 0.75

    scene v14s07_2
    with dissolve

    ro "I now invite you all to the bus so that we can get on our way to the airport."

    scene v14s07_5 # TPP. show Ms. Rose walking towards the hotel lobby front door with mc walking behind her
    with dissolve
    
    pause 0.75

    stop music fadeout 3
    jump v14s08