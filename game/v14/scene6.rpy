# SCENE 06: Wake up Next Morning
# Locations: Hotel Room, Hotel Corridor
# Characters: MC (Outfit: 5), IMRE (Outfit: 1)
# Time: Morning

label v14s06:
    play music music.v13_Track_Scene_46_1 fadein 2

    scene black
    with fade
    
    pause 2

    scene v14s06_1 # TPP. Show MC waking up in his bed
    with dissolve

    pause 0.75

    scene v14s06_2 # TPP. Show MC sitting up on his bed, holding a fist in one of his hands, he is excited, mouth closed
    with dissolve

    u "(Damn, I feel energized this morning.)"

    scene v14s06_3 # TPP. Show MC getting out of bed, smiling, mouth closed
    with dissolve

    pause 0.75

    scene v14s06_4 # TPP. Show MC putting his shirt on (pants already on), smiling, mouth closed
    with dissolve

    u "(I feel like I never even hit my head.)"

    play sound sound.knock

    scene v14s06_5 # FPP. MC standing same place as v14s06_4, looking at the hotel door (door closed)
    with dissolve

    pause 0.75

    scene v14s06_6 # TPP. Show MC walking towards the door
    with dissolve

    pause 0.75

    scene v14s06_7 # FPP. MC standing in front of door, door open, Imre on the other side, looking at MC, smiling, mouth closed
    with dissolve

    u "Hey, man."

    scene v14s06_7a # FPP. Same as v14s06_7, but Imre mouth open
    with dissolve

    imre "Hey. It's finally time to leave this continent and head back home. You ready?"

    scene v14s06_7
    with dissolve

    u "Yeah, I can finish packing real quick."

    if v14s03a_take_wallet:
        scene v14s06_7a
        with dissolve

        imre "By the way, Luuk has some American dollars, if you wanted to exchange any money."

        scene v14s06_7
        with dissolve
        
        u "Oh shit, good idea!"

    u "Tell me, are we riding the bus or...?"

    scene v14s06_7a
    with dissolve

    imre "Yeah, we're riding the bus to the airport. Hurry up, bitch!"

    if v14s4_tell_imre:

        scene v14s06_7b # FPP. Same as v14s06_7, Imre turning around to walk away
        with dissolve

        u "Imre, wait!"

        scene v14s06_7a
        with dissolve

        imre "Yeah?"

        scene v14s06_7c # FPP. Same as v14s06_7, but Imre slightly annoyed
        with dissolve

        u "Look... I'm really sorry for last night. I know you were trying with Ryan and-"

        scene v14s06_7d # FPP. Same as v14s06_7c, but Imre mouth open
        with dissolve

        imre "[name], Ryan and I are done!"

        imre "I'm trying to stay reserved, but in truth, I want to beat his ass. I'm just not sure if that'll give me the hint of justification I'm looking for."

        scene v14s06_7c
        with dissolve

        u "Are you gonna-"

        scene v14s06_7d
        with dissolve

        imre "He's gonna get what's coming to him, yeah."

        scene v14s06_7b
        with dissolve

        u "*Sighs*"

        scene v14s06_8 # TPP. Show MC grabbing his bag, slightly worried, mouth closed
        with dissolve

        u "(Hopefully things are gonna start getting back to normal.)"

    scene v14s06_9 # TPP. Show MC leaving the room with his bag, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v14s06_10 # TPP. Show MC walking through hotel lobby with his bag, slight smile, mouth closed
    with dissolve

    pause 0.75

    if v14s03a_take_wallet:
        scene v13s18_2
        with fade
       
        luuk "My man [name]!"

        scene v13s06_6a
        with dissolve
        
        luuk "Need some American money, I assume?"

        scene v13s06_6
        with dissolve
        
        u "(This guy is on top of everything...)"
        
        scene v13s21_3
        with fade
        
        pause 0.5
        
        scene v13s06_6
        with fade
        
        u "Perfect. Thanks for everything, Luuk!"

    stop music fadeout 3
    jump v14s07