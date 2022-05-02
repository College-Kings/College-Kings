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

label recap_start:
    
    hide screen phone_icon
    # r1
 
    scene recap01_01  # TPP Establishing shot of SVC campus exterior 
    with dissolve
    
    narrator "I still remember my first day at San Vallejo College."

    scene recap01_01a # new kid
    with dissolve

    narrator "Young and naive, I had no idea how my life was about to change."

    scene recap01_01b # TPP MC walking through the front doors of the college
    with dissolve

    narrator "All the girls..."

    scene recap01_01c
    with dissolve

    narrator "the parties... "
    
    scene recap01_01e 
    with dissolve
        
    narrator "the fights... " 
    
    scene recap01_01f
    with dissolve
    # r2 

    # input Ask the player for their name 
    $ name = renpy.input("What's your name?", default=("Alex").strip())
    $ name = name.strip()

    narrator "All of the sudden, I could be whoever I wanted to be..."

label test_rep_screen:    

    scene black
    with None        

    # set reputation using the screen 
    call screen recap_rep_selection_screen()

    # r3     

    scene recap01_03 # TPP or wide FPP Imre noraml clothes wolf jacekt
    with dissolve 

    u "In those early days, my dorm mate was Imre."

    scene recap01_03a # TPP image of Imre and MC hanging out or Imre chasing a girl or something, Or potential Imre chasing a girl with MC in present watching (lindsey gym scene)
    with dissolve

    u "He's an absolute sex hound, always trying to get laid..."

    scene recap01_03b # TPP or wide FPP image Some of the wolves frat members wearing frat jackets 
    with dissolve

    u "and obsessed with joining a frat called the Wolves."

    # r4

    scene recap01_04 # TPP or wide FPP image of Ryan
    with dissolve

    u "And I made friends with Ryan"

    scene recap01_04a # TPP image of MC and Ryan hanging out together
    with dissolve

    u "He's not as confident as Imre, but he's a solid wingman and a loyal friend."

    # r5 

    scene black
    with dissolve
    
    u "And there were the girls of course."

    scene recap01_05 # TPP or wide FPP image Lauren
    with dissolve

    u "Lauren..."
    
    scene recap01_5a #  Pic of riley
    with dissolve

    u "and Riley to start with."

    scene recap01_05b # TPP image 3-4 girls in a single frame image
    with dissolve 

    u "But that was soon going to change into lots more girls entering my life..."

    scene recap01_05c # TPP image different 3-4 girls in a single frame image
    with dissolve

    u "with so many choices about who I wanted to pursue a relationship with or just stay friends."

    scene black
    with dissolve

    u "That kinda leads me to the first huge decision I had to make that was going to shape my whole future."

    scene recap01_05d # TPP image Apes Frat guys on one side and Wolf frat guys on another side (maybe something from the fight scene) / frat jackets on to show distinction
    with dissolve

    u "Which frat did I want to join? The Wolves or the Apes?"

    # r6

    scene  recap01_06 # TPP Some of the girls skimpy outfits or should have some of main female chars but not all need to be main chars
    with dissolve

    u "Joining either frat would mean hooking up with the hottest girls..."

    scene recap01_06a # TPP image Party at the apes houses (2 images with a pause)
    with dissolve

    pause 1.25

    scene recap01_06b # TPP image Party at the apes houses (2 images with a pause)
    with dissolve

    pause 1.25

    scene recap01_06c # TPP image Party at the wolves houses (2 images with a pause)
    with dissolve

    u "going to awesome parties..."

    scene recap01_06d # TPP image MC in the fight tournament
    with dissolve

    u "and competing in fight tournaments."

    scene recap01_06e
    with dissolve

    pause 1.25 

    scene recap01_06f 
    with dissolve

    u "But both frats have a very different vibe."

    scene recap01_06g # TPP image Imre and MC doing Wolves Frat stuff or at the gym
    with dissolve

    u "Imre wanted me to join the Wolves."

    scene recap01_06h # TPP image Ryan and MC doing Ape stuff training in the basement
    with dissolve    

    u "Ryan wanted me to join the Apes"

label test_frat_selection:
        
    scene black
    with None
    
    call screen recap_frat_selection_screen()
        
    if _return == "apes":
        $ mc.frat = Frat.APES
    else:
        $ mc.frat = Frat.WOLVES

    # R7 

    if mc.frat == Frat.APES:
        
        scene recap01_07 # TPP image MC making his frat choice [APES]            
        with dissolve
    
        u "After making my choice..."

        scene recap01_07b # TPP MC during initiation [APES]
        with dissolve

        u "I passed my initiation by showing my loyaly to the frat and my new brothers..."

        pause 1.25
        
        scene recap01_07d # TPP image show MC wearing his APES jacket
        with dissolve

        pause 1.25
        
        scene recap01_07f # TPP image MC moving into his frat room [APES]
        with dissolve
            
        u "and moved into the frat house."
    
    else: 

        scene recap01_07a # TPP MC mkaing his frat choice [WOLVES]
        with dissolve
        
        u "After making my choice..."

        scene recap01_07c # TPP MC during intiiation [WOLVES] 
        
        u "I passed my initiation by showing my loyaly to the frat and my new brothers..."

        pause 1.25

        scene recap01_07e # TPP image show MC wearing his WOLVES jacket
        with dissolve

        pause 1.25

        scene recap01_07g # TPP MC moving into his frat room [WOLVES]
        with dissolve
        
        u "and moved into the frat house."


        # R8 

    scene recap01_08 #TPP image Girls from mud wrestling event
    with dissolve

    u "Back to the girls."

    scene recap01_08a # TPP of Emily kissing with MC or opening dream position of Emily
    with dissolve

    pause 1.25

    scene recap01_08b # TPP of Lauren's first kiss with MC 
    with dissolve

    pause 1.25
    
    scene recap01_08c # TPP of Riley's first kiss with MC
    with dissolve

    u "I could pursue multiple girls at the same time..." 

    scene recap01_09d # TPP of Aubrey's first kiss with MC/ or first sex encounter
    with dissolve

    pause 1.25

    scene recap01_09e # TPP MC's dream of Riley in the kitchen
    with dissolve

    u "but this became quite tricky as going for one girl..."
    
    scene recap01_09f: # TPP Scrolling view of Chloe after homecoming naked 
        subpixel True
        yalign 1.0
        linear 6.0 yalign 0.0             
    with fade

    pause 1.25

    u "sometimes meant I couldn't go for another because..."

    scene recap01_09g # TPP image TPP  Sex scene with Aubrey
    with fade

    pause 1.25

    scene recap01_09h # TPP  Chloe and Aubrey being chummy 
    with dissolve

    u "they were best friends..."

    scene recap01_09i # TPP of Autumn and Lauren warming up to MC 
    with dissolve

    u "or worse... sisters."

    scene black
    with dissolve

    u "I had to decide who to pursue."

    jump recap_02