# SCENE 27: MC gets a call from Jenny
# Locations: Front of chics house (outside), Underground bar
# Characters: MC (Outfit: 9, JENNY (Outfit: 4), PENELOPE (Outfit: 7), SAMANTHA (Outfit: 1)
# Time: Evening

label v15s27: # -MC walks out of the Chicks house-
    scene v15s27_1 # TPP. Camera facing Chicks' front door with MC opening the door; MC neutral expression mouth closed.
    with dissolve

    pause 0.75

    scene v15s27_1a # TPP. Camera facing Chicks' front door with MC exiting through the door; MC neutral expression mouth closed.
    with dissolve

    pause 0.75

    scene v15s27_1b # TPP. Camera facing Chicks' front door with MC closing the door behind him; MC neutral expressoin mouth closed.
    with dissolve

    pause 0.75

    if "v14_threesome" in sceneList: # -if had threesome
        scene v15s27_2 # TPP. MC standings in front of the door neutral expression mouth closed.
        with dissolve
        
        u "(Well, that turned into quite a dramatic conversation...)"

        scene v15s27_2a # TPP. MC few steps further from v15s27_2; MC neutral expression mouth closed.
        with dissolve
        
        u "*Sighs* (It's impossible to make everyone happy all the time.)"

        scene v15s27_2b # TPP. MC a few steps further from v15s27_2a; MC concerned mouth closed.
        with dissolve

        u "(I just hope Riley and Aubrey can still be good friends with each other.)"

    else: # -if did not have threesome
        scene v15s27_2
        with dissolve
        
        u "(Well, that was an interesting conversation...) *Chuckles*"

    if v15_RileyUpset: # -if RileyUpset potentially set in scene26
        scene v15s27_2b
        with dissolve

        u "(Riley didn't seem too pleased about the whole situation. Hopefully she's over it before I see her next.)"
    # -Regardless-

    scene v15s27_3 # TPP. MC a few steps further from v15s27_2a with the Chicks' house behind him; neutral expreession mouth closed.
    with dissolve

    pause 0.75

    play sound "sounds/vibrate.mp3"

    scene v15s27_3a # TPP. MC slightly surprised mouth closed, reaching for phone in his pocket.
    with dissolve

    pause 0.75
    
    # -MC's phone vibrates, he answers a call from Jenny-
    # -If you want to make it more interesting, show Jenny and Penelope on the other line, they've been drinking so they're smiley and dancy-
    scene v15s27_3b # TPP. MC holding his phone to his ear, smiling mouth open.
    with dissolve

    u "Hello?"

    scene v15s27_4 # TPP. Jenny sitting at the bar with a booths behind her (Samantha is sitting in the booth behind her but Samantha's face is blocked by Jenny), holding her phonein her right hand, smiling, buzzed from drinking, mouth open [Underground Bar]. There is a drink on the bar in front of her left hand.
    with dissolve

    jen "Hey, [name]! What are you up to right now?"

    scene v15s27_3b
    with dissolve

    u "I was just about to head home. Thinking about having a relaxed evening for once, haha."

    scene v15s27_4
    with dissolve

    jen "Wrong! You're coming out with us!"

    scene v15s27_3c # TPP. MC holding his phone to his ear, slightly surprised, smiling mouth open.
    with dissolve

    u "Us?"

    scene v15s27_4a # TPP. Jenny sitting at the bar blocking Samantha in the booth, phone to her ear (right hand), holding a drink (left hand), smiling mouth open [Underground Bar].
    with dissolve

    jen "Me and Penelope! Your two favorite girls?!"

    menu:
        "You are my favorite girls...":
            $ add_point(KCT.BOYFRIEND)
            
            scene v15s27_3d # TPP. MC holding his phone to his ear, laughing, smiling, mouth open.
            with dissolve

            u "*Laughs* Well, you are my two favorite girls, that's true..."

            if lauren.relationship.value >= Relationship.GIRLFRIEND.value or chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                $ add_point(KCT.TROUBLEMAKER)
                
                u "(Well, maybe in the top three...)"
            
            if lauren.relationship.value >= Relationship.GIRLFRIEND.value and chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                u "(Or four... Wait, how many girlfriends do I have?)"

            scene v15s27_4a
            with dissolve

            jen "Mhmm..."

        "Favorite? I'm not so sure.":
            $ add_point(KCT.TROUBLEMAKER)

            scene v15s27_3d # TPP. MC holding his phone to his ear, laughing, smiling, mouth open.
            with dissolve

            u "*Laughs* Favorite? I'm not so sure."

            u "There's a lot of pretty girls out there, you know?"

            scene v15s27_4a
            with dissolve

            jen "Yeah, but none of them are as fun as we are."

            scene v15s27_3d # TPP. MC holding his phone to his ear, laughing, smiling, mouth open.
            with dissolve

            u "Maybe."

    scene v15s27_3b
    with dissolve

    u "But seriously, I think I'm just going to get into bed early tonight."

    scene v15s27_4b # TPP. Jenny sitting at the bar blocking Samantha in the booth behind her, phone to her ear (right hand), her hand around her drink (left hand) that is on the bar, smiling mouth open [Underground bar].
    with dissolve

    jen "Oh, come on Grandpa! There's a new underground bar that just opened up, and they're not checking IDs!"

    if v15s24_nancy_dick:
        u "(Good, I wouldn't want a repeat of that Nancy Dick fiasco...)"
    elif v15_lindsey_gamenight:
        u "(Good, I wouldn't want a repeat of that Andrew King fiasco...)"
    elif v11_josh_nightclub:
        u "(Good, my last one from Josh expired like a day after I got it, haha.)"
        u "(Speaking of Josh... Where the hell is he?)"

    scene v15s27_4a
    with dissolve

    jen "Let's get our drink on!"

    scene v15s27_4c # TPP. Jenny switches the phone to her other hand (left hand) and ear, her headed turned toward the right off screen, smiling mouth open. Drink is on the bar [Underground Bar]. 
    with dissolve

    pause 0.75

    scene v15s27_4d # TPP. Jenny gestures for someone to come toward her, smiling mouth opened. Drink is on the bar [Underground Bar]
    with dissolve

    pause 0.75

    scene v15s27_4e # TPP. Penelope enter the scene from player's left (Jenny's right), Penelope is buzzed from drinking and smiling mouth closed. Jenny smiling, holding her phone (left hand), mouth closed, drink on the bar. [Underground Bar].
    with dissolve

    pause 0.75

    scene v15s27_4f # TPP. Penelope smiling, mouth closd, grabbing for Jenny's phone (left hand) while Jenny pulls away from her revealing Samantha sitting in the booth behind them. Penelope and Jenny smiling mouths closed. Jenny's drink is on the bar [Underground Bar].
    with dissolve

    pause 0.75

    scene v15s27_4g # TPP. Jenny switches her phone to her right hand (closest to Penelope) as Penelope continues to pull Jenny's hand with the phone closer to her. Samantha is blocked from view for the remainder of the scene. Both girls are smiling mouths closed [Underground Bar].
    with dissolve

    pause 0.75
    
    scene v15s27_4h # TPP. Penelope leaning in towards Jenny's phone (Jenny's right hand), smiling mouth open, talking into the phone. Jenny's holding her drink in her left hand smiling, mouth closed [Underground Bar].
    with dissolve

    pe "Yeah, [name]! Don't be a boring old man for once! You can go slipper shopping tomorrow. *Laughs*"

    scene v15s27_4i # TPP. Penelope leaning in towards Jenny's phone (Jenny's right hand), smiling mouth closed. Jenny's holding her drink in her left hand smiling, mouth open, leaning toward her phone [Underground Bar].
    with dissolve

    jen "*Laughs* Good one."

    scene v15s27_4h
    with dissolve

    pe "You're coming out drinking with us! That's final!"

    scene v15s27_3d
    with dissolve

    u "Haha, okay, okay. I guess I am!"

    u "(I can always rest later.)"

    scene v15s27_4h
    with dissolve

    pe "We'll text you the details."

    scene v15s27_4i
    with dissolve

    jen "Yes!"

    scene v15s27_3d
    with dissolve

    u "Okay, crazies. I'll see you there. *Laughs*"

    scene v15s27_3e # TPP. MC putting his phone in his pocket, smiling, mouth closed. # -MC smiles as he hangs up, puts his phone away, and continues walking-
    with dissolve

    u "(This should be fun.)"

    scene v15s27_3f # TPP. Camera wide showing MC leaving the front yard of the Chicks' house.
    with dissolve
    
    pause 0.75

jump v15s28 # -Transition to Scene 28-