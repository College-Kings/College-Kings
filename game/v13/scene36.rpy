# SCENE 36: walk to garden 
# Locations: sidewalk (location 1, 2 and 3) garden entrance
# Characters: MC (Outfit: 5), LINDSEY (Outfit: 1), IMRE (Outfit: 1), CHRIS (Outfit: 1), NORA (Outfit: 1)
# Time: evening 

label v13_walk_garden:
    scene v13s36_1 # TPP. MC and lindsey walking along the sidewalk
    with fade

    pause 0.75

    play music "music/v13/Track Scene 36.mp3" fadein 2

    #scene v13s36_2 # FPP. MC looking at lindsey who has a neutral expression, mouth closed (location 1)
    scene v13s36_3a
    with fade

    u "So, what exactly is going on?"

    #scene v13s36_2a # FPP same as 2, mouth opened
    scene v13s36_3
    with dissolve

    li "Chris is trying his best to win Nora over..."

    #scene v13s36_2b # FPP. same as 2, Lindsey now smiling, mouth opened
    scene v13s36_3b
    with dissolve

    li "He finished up with all of his frat planning with Sebastian and now for the last few days of our little vacay, he wants to be the perfect boyfriend. *Chuckles*"

    if CharacterService.is_fwb(nora):
        #scene v13s36_2 
        scene v13s36_3a
        with dissolve

        u "*Laughs* Right..."

    #scene v13s36_2
    scene v13s36_3a
    with dissolve

    u "Okay then, so what did he set up?"

    scene v13s36_3 # FPP. same as 2a (location 2)
    with dissolve

    li "It's really just gonna be a relaxing evening in the park; not much but it's something."

    li "Imre, myself, Nora, Chris and you are the only people that will be there. Nora is acting a little odd, but we'll see if it all goes well."

    scene v13s36_3a # FPP. Same as 2 (location 2)
    with dissolve

    u "Hmph, okay... I'm not really sure how I feel about this whole situation, guess I'll just have to see it through, ha."

    scene v13s36_3b # FPP. Same as 2b (location 2)
    with dissolve

    li "Well, here's your chance. *Chuckles*"

    scene v13s36_4 # TPP, MC and lindsey walk up to imre nora and chris(location 3)
    with fade

    pause 0.75

    scene v13s36_5 # FPP. Lindsey looking at the rest smiling, mouth opened (location 3)
    with dissolve

    li "Hey guys, hope you don't mind that I brought [name]?"

    scene v13s36_5a # FPP. Imre looking back at lidnsey smiling back, mouth opened (location 3)
    with dissolve

    imre "You know I don't."

    if CharacterService.is_mad(chris):
        scene v13s36_5c # FPP. Chris has a mad face on, looking at lindsey, mouth opened (location 3)
        with dissolve
        
        ch "Well, he's already here isn't he? Let's go."

        scene v13s36_5d # FPP. Lindsey looking back at chris with a uncomfortable look, mouth opened (location 3)
        with dissolve

        li "Okay..."

    else:
        scene v13s36_5b # FPP. Chris looking at lindsey, neutral expression, mouth opened (location 3)
        with dissolve
        
        ch "No, it's cool."

        scene v13s36_5
        with dissolve

        li "Good."

    scene v13s36_5e # FPP. Chris reaches for nora hand, nora's and chris's mouth closed (location 3)
    with dissolve

    pause 0.5

    scene v13s36_5f # FPP. Nora puts the same hand behind her ear as if uncomfortable, mouth opened (location 3)
    with dissolve

    no "Let's get to it, shall we guys?"

    scene v13s36_6 # TPP. Nora walks off ahead of everyone, everyone following behind
    with dissolve

    pause 0.75

    scene v13s36_7 # TPP. Everyone arriving at the garden
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v13s37