# SCENE 46: Solo Baby Night WOLVES OR APES (both)
# Locations: MC's room (either frat house)
# Characters: MC (Outfit: 9), [V16_BABY] (Outfit: x), SAMANTHA (unseen), CAMERON (unseen), GRAYSON (unseen)
# Time: Wed Night

label v16s46: # 46) Baby night, MC only
    # -Scene is the same for Wolves and Apes unless specified.
    # ALL RENDERS SHOW ONLY THE INSIDE OF MC'S ROOM

    if joinwolves:
        scene v16s46_31 # TPP Show MC (tired, mouth closed), holding baby doll, entering his room [WOLF ROOM]
    else:
        scene v16s46_1 # TPP Show MC (tired, mouth closed), holding baby doll, entering his room [APE ROOM]
    with dissolve

    pause 0.75

    if joinwolves:
        scene v16s46_32 # TPP Show the baby doll on MC's bed, MC pulling a chair next to the bed [WOLF ROOM]
    else:
        scene v16s46_2 # TPP Show the baby doll on MC's bed, MC pulling a chair next to the bed [APE ROOM]
    with dissolve
        
    pause 0.75
        
    if joinwolves:
        scene v16s46_33 # FPP Show MC placing the baby on the chair [WOLF ROOM]
    else:
        scene v16s46_3 # FPP Show MC placing the baby on the chair [APE ROOM]
    with dissolve
        
    pause 0.75
        
    if joinwolves:
        scene v16s46_34 # TPP Show MC taking off his shirt [WOLF ROOM]
    else:
        scene v16s46_4 # TPP Show MC taking off his shirt [APE ROOM]
    with dissolve
        
    pause 0.75

    if joinwolves:
        scene v16s46_34a # TPP Show MC taking in his boxers/underwear [WOLF ROOM]
    else:
        scene v16s46_4a # TPP Show MC taking in his boxers/underwear [APE ROOM]
    with dissolve
        
    pause 0.75
        
    if joinwolves:
        scene v16s46_35 # TPP Show MC laying in bed, reaching for the light [WOLF ROOM]
    else:
        scene v16s46_5 # TPP Show MC laying in bed, reaching for the light [APE ROOM]
    with dissolve

    u "(Let's see how long this lasts before I get woken up...)"

    if joinwolves:
        scene v16s46_36 # FPP Show MCs glowing phone with the time of 1:17am [WOLF ROOM]
    else:
        scene v16s46_6 # FPP Show MCs glowing phone with the time of 1:17am [APE ROOM]
    with fade

    u "*Snoring*"

    play sound "sounds/babycry.mp3"

    if joinwolves:
        scene v16s46_37a # FPP Same angle as 6, MCs glowing phone with a time of 1:47am [WOLF ROOM]
    else:
        scene v16s46_7a # FPP Same angle as 6, MCs glowing phone with a time of 1:47am [APE ROOM]
    with fade

    baby "*Crying*"
    
    u "Hmm?"

    if joinwolves:
        scene v16s46_35a # TPP Same angle as 5, MC (sleepy, mouth open) opens his eyes part way, confused [WOLF ROOM]
    else:
        scene v16s46_5a # TPP Same angle as 5, MC (sleepy, mouth open) opens his eyes part way, confused [APE ROOM]
    with dissolve

    u "Ahh, fuck..."

    play sound "sounds/babycry.mp3"

    if joinwolves:
        scene v16s46_37 # TPP MC sitting on the edge of the bed, turning on the light, sleepy eyes half-open [WOLF ROOM]
    else:
        scene v16s46_7 # TPP MC sitting on the edge of the bed, turning on the light, sleepy eyes half-open [APE ROOM]
    with dissolve

    baby "*Cries louder*"

    if joinwolves:
        scene v16s46_38 # FPP Looking at the baby doll, sitting on chair [WOLF ROOM]
    else:
        scene v16s46_8 # FPP Looking at the baby doll, sitting on chair [APE ROOM]
    with dissolve

    u "(Let's see if we can shut this thing up quickly...)"

    if joinwolves:
        scene v16s46_39 # TPP MC (tired expression, mouth open) looking around on his desk [WOLF ROOM]
    else:
        scene v16s46_9 # TPP MC (tired expression, mouth open) looking around on his desk [APE ROOM]
    with dissolve

    u "What did I-"

    play sound "sounds/babycry.mp3"

    if joinwolves:
        scene v16s46_38
    else:
        scene v16s46_8
    with dissolve

    baby "*Crying*"

    u "(Where did I put the damn keys?)"

    if joinwolves:
        scene v16s46_40 # TPP Show MC (mouth closed) looking on his bed, pulling down the covers [WOLF ROOM]
    else:
        scene v16s46_10 # TPP Show MC (mouth closed) looking on his bed, pulling down the covers [APE ROOM]
    with dissolve

    u "(Not here...)"

    play sound "sounds/babycry.mp3"

    if joinwolves:
        scene v16s46_38
    else:
        scene v16s46_8
    with dissolve

    baby "*Cries*"

    if joinwolves:
        scene v16s46_41 # TPP MC (mouth open) holding his hands out to the baby doll, as if soothing a real baby [WOLF ROOM]
    else:
        scene v16s46_11 # TPP MC (mouth open) holding his hands out to the baby doll, as if soothing a real baby [APE ROOM]
    with dissolve

    u "I'm sorry, [v16_baby_name]..."

    if joinwolves:
        scene v16s46_42 # TPP MC (mouth closed) searching under his bed [WOLF ROOM]
    else:
        scene v16s46_12 # TPP MC (mouth closed) searching under his bed [APE ROOM]
    with dissolve

    u "(Shit...)"

    play sound "sounds/babyscream.mp3"

    if joinwolves:
        scene v16s46_38
    else:
        scene v16s46_8
    with dissolve

    baby "*Screaming cry*"

    if joinwolves:
        scene v16s46_43 # TPP MC (mouth open) searching in the bedside table [WOLF ROOM]
    else:
        scene v16s46_13 # TPP MC (mouth open) searching in the bedside table [APE ROOM]
    with dissolve

    u "(Fuck!) Where are the fucking keys?!"


    if not joinwolves:
        # -Only the closed door is shown. The door never opens, and the voices are just coming from the other side-

        scene v16s46_14 # FPP Show the closed door to MC's room
        with dissolve

        play sound "sounds/bangdoor.mp3"

        sa "[name]! Shut that thing up, now!"

        scene v16s46_8
        with dissolve

        play sound "sounds/babycry.mp3"
        
        baby "*Cries*"

        scene v16s46_15 # TPP MC (mouth closed) on his hands and knees scanning the floor [APE ROOM]
        with dissolve

        menu:
            "I'm sorry!":
                $ add_point(KCT.BRO)

                scene v16s46_15
                with dissolve

                u "Yeah, I'm trying! Sorry!"

                scene v16s46_14
                with dissolve

                sa "Well, try harder!"

            "Don't you think I'm trying?!":
                $ add_point(KCT.TROUBLEMAKER)

                scene v16s46_14
                with dissolve

                u "Don't you think I'm trying?!"

                sa "It's waking everyone up, [name]."

                scene v16s46_16 # TPP MC (mouth open) searching his closet [APE ROOM]
                with dissolve

                u "Thank you for the information, Sam!"

                scene v16s46_14
                with dissolve

                sa "Ugh!"

                scene v16s46_16
                with dissolve

                u "*Whispers* No shit it's waking everyone up... I got woken up too, but-"

        scene v16s46_14
        with dissolve

        ca "What the hell is going on?"

        play sound "sounds/babycry.mp3"

        scene v16s46_8
        with dissolve

        baby "*Crying*"

        scene v16s46_14
        with dissolve

        sa "[name] has one of those stupid fucking baby dolls."

        ca "*Sighs*"

        ca "It's pretty simple, dingus! Just use the keys and it stops crying."

        play sound "sounds/babycry.mp3"

        scene v16s46_8
        with dissolve

        baby "*Crying*"

        scene v16s46_11
        with dissolve

        u "Yeah, I know that!"

        scene v16s46_14
        with dissolve

        ca "Sounds like it needs a diaper change. That's the brown key."

        u "There isn't a brown key, asshole!"

        ca "*Laughs* Okay, it's the orange key."

        scene v16s46_13
        with dissolve

        u "How can you even tell what it wants by the sound of its crying?!?"

        scene v16s46_14
        with dissolve

        ca "I have a very strong paternal instinct! Just, shut it up!"

        play sound "sounds/babyscream.mp3"

        scene v16s46_8
        with dissolve

        baby "*Screaming cries*"

        scene v16s46_9
        with dissolve

        u "Well, I would if I could find the keys!"

        scene v16s46_14
        with dissolve

        ca "Are you serious? How did you lose the keys already?"

        u "I don't know, Cameron. Why would you ask me that?"

        ca "Haha, fail!"

        play sound "sounds/babycry.mp3"

        scene v16s46_8
        with dissolve

        baby "*Crying*"

        scene v16s46_11
        with dissolve

        u "I'm about to start fucking crying, too."

        scene v16s46_14
        with dissolve

        gr "Hello? Why are we all awake and standing at [name]'s door?"

        u "Great question."

        ca "Divorced father issues."

        scene v16s46_17 # TPP MC (mouth closed) searching behind his bed [APE ROOM]
        with dissolve

        gr "Who's this time?"

        sa "[name] is playing daddy tonight."

        play sound "sounds/babycry.mp3"

        scene v16s46_8
        with dissolve

        baby "*Cries*"

        scene v16s46_14
        with dissolve

        gr "Why do-"

        scene v16s46_12
        with dissolve

        gr "No. You know what? I don't care."

        scene v16s46_14
        with dissolve
        
        play sound "sounds/bangdoor.mp3"

        gr "Shut that fucking thing up before I rip this door down!"

        scene v16s46_11
        with dissolve

        u "I'm going to!"

        u "Somehow..."

        play sound "sounds/babycry.mp3"

        scene v16s46_8
        with dissolve

        baby "*Crying*"

    # -Regardless of Apes-
    if joinwolves:
        scene v16s46_48 # TPP MC (mouth closed) picking up the baby and looking underneath - he see's the keys [WOLF ROOM]
    else:
        scene v16s46_18 # TPP MC (mouth closed) picking up the baby and looking underneath - he see's the keys [APE ROOM]
    with dissolve

    u "(Fuck my life, dude!)"

    if joinwolves:
        scene v16s46_49 # FPP Closeup of the keys in MC's hand, all three clearly visible [WOLF ROOM]
    else:
        scene v16s46_19 # FPP Closeup of the keys in MC's hand, all three clearly visible [APE ROOM]
    with dissolve

    u "(Okay, it's time for a diaper change. Which key was it?)"

    # -If MC chooses an incorrect key, the choice menu appears again for another attempt-

    menu v16_wrong_key_1:
        "Blue":
            play sound "sounds/babycry.mp3" 

            if joinwolves:
                scene v16s46_50 # TPP MC (frustrated expression, mouth closed) using the blue key on the baby doll [WOLF ROOM]
            else:
                scene v16s46_20 # TPP MC (frustrated expression, mouth closed) using the blue key on the baby doll [APE ROOM]
            with dissolve

            baby "*Cries*"

            if joinwolves:
                scene v16s46_49
            else:
                scene v16s46_19
            with dissolve

            u "(Dammit... Not blue.)"

            jump v16_wrong_key_1

        "Green":
            play sound "sounds/babyscream.mp3"

            if joinwolves:
                scene v16s46_50a # TPP Same angle as 20, MC (frustrated expression, mouth closed) using the green key on the baby doll [WOLF ROOM]
            else:
                scene v16s46_20a # TPP Same angle as 20, MC (frustrated expression, mouth closed) using the green key on the baby doll [APE ROOM]
            with dissolve

            baby "*Scream crying*"

            if joinwolves:
                scene v16s46_49
            else:
                scene v16s46_19
            with dissolve

            u "(Ah, for fuck's sake...) Okay, okay! Wrong one, got it. Shhhh..."

            jump v16_wrong_key_1

        "Orange":
            play sound "sounds/babycoo.mp3"

            if joinwolves:
                scene v16s46_50b # TPP Same angle as 20, MC (relieved expression, mouth closed) using the orange key on the baby doll [WOLF ROOM]
            else:
                scene v16s46_20b # TPP Same angle as 20, MC (relieved expression, mouth closed) using the orange key on the baby doll [APE ROOM]
            with dissolve

            baby "*Cooing*"

            if joinwolves:
                scene v16s46_51 # FPP MC holding baby doll up in front of him in both hands [WOLF ROOM]
            else:
                scene v16s46_21 # FPP MC holding baby doll up in front of him in both hands [APE ROOM]
            with dissolve

            u "*Sighs* Finally..."

    if joinwolves:
        scene v16s46_52 # TPP MC (relieved, mouth closed) placing the baby doll on the chair with the keys next to it [WOLF ROOM]
    else:
        scene v16s46_22 # TPP MC (relieved, mouth closed) placing the baby doll on the chair with the keys next to it [APE ROOM]
    with dissolve

    pause 0.75

    if not joinwolves:
        ca "Well done, dad!"

        scene v16s46_14
        with dissolve

        sa "If I wake up because of that kid one more time tonight, I'm calling child protective services."

        gr "Wait, does [name] actually have a baby?"

        sa "I'll explain tomorrow."

        scene v16s46_23 # TPP MC (exhausted, mouth closed) sitting on the edge of the bed with his head in his hands [APE ROOM]
        with dissolve

        gr "Wha- Cam?"

        ca "Back to bed, kids."

        scene v16s46_14
        with dissolve

        gr "What the hell is happening around here?"

    if joinwolves:
        scene v16s46_54 # FPP MC shutting off the light [WOLF ROOM]
    else:
        scene v16s46_24 # FPP MC shutting off the light [APE ROOM]
    with dissolve

    pause 0.75

    if joinwolves:
        scene v16s46_55 # TPP MC (eyes closed, mouth open) lays in bed with his arm across his face [WOLF ROOM]
    else:
        scene v16s46_25 # TPP MC (eyes closed, mouth open) lays in bed with his arm across his face [APE ROOM]
    with dissolve

    u "Okay, I don't want any more of that, [v16_baby_name]... Please, let's get some sleep now."
    
    jump v16s50a # -Transition to Scene 50a-