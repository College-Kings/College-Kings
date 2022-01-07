# SCENE 38: walk back with imre
# Locations: sidewalk (1,2,3) and hotel lobby
# Characters: IMRE (Outfit: 1), MC (Outfit: 5)
# Time: evening 

label v13_walk_imre:
    scene v13s38_1 # TPP. MC and imre walking in the sidewalk (location 1)
    with fade

    play music "music/v13/Track Scene 38.mp3" fadein 2

    if v13_imre_disloyal:
        scene v13s38_2 # FPP. MC looking at imre who looks dissapointed, mouth opened (location 1)
        with dissolve

        imre "I never expected you to be like that."

        scene v13s38_2a # FPP. Same as 2, mouth closed
        with dissolve

        u "I'm not a fuckboy, Imre."

        scene v13s38_2b # FPP. Same as 2, imre looking confused, mouth opened
        with dissolve

        imre "How can you say that? Especially when I just saw you swapping spit with the homie's girl?"

        scene v13s38_2c # FPP. Same as 2b, mouth closed
        with dissolve

        u "We've gotten really close these past few weeks, man, and shit just... happened."

        scene v13s38_2a
        with dissolve

        u "I do know it's wrong and I'll keep it under control until she and Chris figure out what they're gonna do."

        scene v13s38_2
        with dissolve

        imre "Oh, that's already decided. They're breaking up."

        scene v13s38_2c
        with dissolve

        u "How do you know that?"

        scene v13s38_3 # FPP. Imre looking determined, mouth opened (location 2)
        with dissolve

        imre "Because I'm gonna make it happen if it's the last thing I do. She obviously isn't good for him."

        imre "You may have broken bro code, but she actually cheated. So, she's gotta go."

    else:
        scene v13s38_2b
        with dissolve
        
        imre "I'm not liking this vibe she's giving off."

        scene v13s38_2c
        with dissolve

        u "Who?"

        scene v13s38_2b
        with dissolve

        imre "Nora, duh. You don't see all the hand moving and fake smiling she's doing?"

        imre "Chris is out here actually trying and she's not doing a damn thing to help the situation."

    scene v13s38_3a # FPP. same as 3, Imre with a neutral expression, mouth closed
    with dissolve

    u "I feel as if there's a deeper reason for you having beef with Nora."

    scene v13s38_3b # FPP. Same as 3a, mouth open
    with dissolve

    imre "There is..."

    scene v13s38_3a
    with dissolve

    u "And that reason is...?"

    scene v13s38_3c # FPP. Same as 4, imre sighing, mouth opened
    with dissolve

    imre "*Sighs* You know how my brother was a Wolf?"

    scene v13s38_3a
    with dissolve

    u "Yeah."

    scene v13s38_3b
    with dissolve

    imre "Well, my brother had the hots for Nora and because she was with Chris, she turned him away."

    imre "I respected it a lot, and when I joined the Wolves I expected to see a strong bond between the two of them."

    scene v13s38_3a
    with dissolve

    u "Well, you must've been disappointed."

    scene v13s38_4 # FPP. same as 3b (location 3)
    with dissolve

    imre "Very much so. If Chris was such a good guy that she rejected my brother, then why all of the sudden is he not good enough for her to reject you? Chris hasn't changed."

    scene v13s38_4a # FPP. same as 3a (location 3)
    with dissolve

    u "I get that you know a lot about them Imre, but you can't know every aspect of their relationship."

    u "How do you know deep within that he hasn't changed?"

    scene v13s38_4
    with dissolve

    imre "I just don't believe it. He's a loyal and dependable guy."

    scene v13s38_4b # FPP. Same as 4, imre slight smile, mouth opened
    with dissolve

    imre "It didn't bother me when she rejected my brother because hell... if I'm being honest, she rejected him for a better man."

    scene v13s38_4c # FPP. same as 4b, mouth closed
    with dissolve

    u "You're kind of dick riding Chris a little bit, don't you think so?"

    scene v13s38_4b
    with dissolve

    imre "You must not know the Chris that I know, and that's not me throwing shade... It's just a factual statement."

    scene v13s38_4c
    with dissolve

    u "I won't debate you on that."

    scene v13s38_5 # TPP. MC and imre arrive in front of the hotel
    with dissolve

    pause 0.75

    scene v13s38_6 # TPP. Imre and MC entering the hotel lobby
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v13_hotel_imre