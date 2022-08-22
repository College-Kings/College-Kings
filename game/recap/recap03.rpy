# Copyright 2022 CrimsonSky Ltd, All Rights Reserved 
#
#
#
#
#
#
#
#
#

label recap_end:
    
    hide screen phone_icon

    if not is_CK2:  # CK1 

        scene recap03_01 #v11amp7.webp
        with dissolve             
        
        u "In just a couple of days, we were flying out to Europe!"

        scene recap03_02 #v11bb5.webp
        with dissolve

        u "London was our first stop and I couldn't wait."

        scene recap03_03 #v11sas5.webp
        with dissolve

        u "It was time to make some more awesome memories!"

    else: # CK2 

        scene recap03_01 #v11amp7.webp
        with dissolve
        
        u "While we were in Europe..."

        scene recap03_04 #v11lip1.webp
        with dissolve

        pause 1.5
        
        scene recap03_04a #v11lip2.webp
        with dissolve

        u "it got out that Lindsey had decided to run against Chloe to be president of the Chicks sorority."

        scene recap03_05 #v12pwu16.webp
        with dissolve

        u "The tension was clearly building between her and Chloe."

        scene recap03_06 #v11chb9a.webp
        with dissolve

        pause 1.5

        scene recap03_06a #v13s41_17a.webp
        with dissolve

        u "Pretty soon, I was going to be expected to pick a side, or..."

        scene recap03_07 #v13s43_7.webp
        with dissolve

        u "I'd have to be really clever about how I decide to play this out."        

        scene recap03_08 #v13s12a_7.webp
        with dissolve
        
        u "There was also time to see the international superstar singer Polly in concert."

        scene recap03_09 #aub_pen_recap_screen.webp - split scene image of Aubrey on one side and Penelope on the other smiling 
        with dissolve

        menu: 

            "Take Aubrey":
                $ v0_penelope_concert = False
                $ v0_aubrey_concert = True
                
                scene recap03_10 #v13s12a_6o.webp
                with dissolve                
            
            "Take Penelope":
                $ v0_penelope_concert = True
                $ v0_aubrey_concert = False
                
                scene recap03_11 #v13s12b_8a.webp
                with dissolve

    pause 1.5

    scene recap03_12 #v14s07_1.webp
    with dissolve

    pause 1.5

    scene recap03_12a #v14s10_1.webp
    with dissolve

    pause 1.5
        
    scene recap03_12b #v14s10_5.webp
    with dissolve

    u "And then our Europe trip was over and it was time to fly home. It went by so fast but it's something I'll never forget!"

    if not is_CK2:
        jump v11_nora_chloe_hallway
    
    else:
        jump v1_start