# SCENE 32: Running into Emily
# Location: Sidewalk, Hotel Lobby
# Characters: MC (Outfit 9), Emily (Outfit 1)
# Time: Day

label v11_emily_sidewalk:
    scene v11ems1a # FPP. Show MC and Emily in talking distance (check positioning in v11lip9), Emily slightly annoyed, looking at MC
    with dissolve
    play music music.ck1.v10.Track_Scene_39 fadein 2
    u "Hey Emily, haven't seen you the whole time we've been here."

    scene v11ems1 # FPP. Same as v11ems1, Emily slightly annoyed, mouth closed
    with dissolve

    em "That's the point. Do you not remember our talk?"

    scene v11ems1a
    with dissolve

    u "Yeah I remember, but-"

    scene v11ems1
    with dissolve

    em "Then you know why we haven't seen each other."

    scene v11ems1b # FPP. Same as v11ems1, Emily walking past MC, she is slightly annoyed, mouth closed
    with dissolve

    pause 0.75

    scene v11ems2 # FPP. MC looking as Emily walks away, he's looking at her from behind
    with dissolve

    u "(She really doesn't want to talk to me. Oh, well.)"

    scene v11ems3 # TPP. Show MC walking into the hotel lobby, mouth closed, slight smile
    with fade

    pause 0.75

    scene v11ems4 # TPP. Show MC walking through the hotel lobby, mouth closed, slight smile
    with dissolve

    pause 0.75
    stop music fadeout 3
    jump v11_bar_chloe_and_aubrey