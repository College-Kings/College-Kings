# SCENE 46: Solo Baby Night WOLVES OR APES (both)
# Locations: MC's room (either frat house)
# Characters: MC (Outfit: 9), [BABY_NAME] (Outfit: x), SAMANTHA (unseen), CAMERON (unseen), GRAYSON (unseen)
# Time: Wednesday evening

label v16s46: # 46) Baby night, MC only
    # -Scene is the same for Wolves and Apes unless specified.
    # ALL RENDERS SHOW ONLY THE INSIDE OF MC'S ROOM
    
    scene v16s46_1 # TPP Show MC (tired, mouth closed), holding baby doll, entering his room
    with dissolve

    pause 0.75

    scene v16s46_2 # TPP Show the baby doll on MC's bed, MC pulling a chair next to the bed
    with dissolve
    
    pause 0.75
    
    scene v16s46_3 # FPP Show MC placing the baby on the chair
    with dissolve
    
    pause 0.75
    
    scene v16s46_4 # TPP Show MC getting undressed
    with dissolve
    
    pause 0.75
    
    scene v16s46_5 # TPP Show MC laying in bed, reaching for the light
    with dissolve

    u "(Let's see how long this lasts before I get woken up...)"

    scene v16s46_6 # FPP Show glowing digital clock with a late-night time
    with dissolve

    u "*Snoring*"

    scene v16s46_7a # FPP Same angle as 6, glowing digital clock reads 30 minutes later
    with fade

    baby "*Crying*"

    scene v16s46_6
    with dissolve

    u "Hmm?"

    scene v16s46_5a # TPP Same angle as 5, MC opens his eyes part way, confused
    with dissolve

    u "Ahh, fuck..."

    scene v16s46_7 # TPP MC sitting on the edge of the bed, turning on the ligh, sleepy eyes half-open
    with dissolve

    baby "*Cries louder*"

    scene v16s46_8 # FPP Looking at the baby doll, sitting on chair
    with dissolve

    u "(Let's see if we can shut this thing up quickly...)"

    scene v16s46_9 # TPP MC (tired expression, mouth open) looking around on his desk
    with dissolve

    u "What did I-"

    scene v16s46_8
    with dissolve

    baby "*Crying*"

    u "(Where did I put the damn keys?)"

    scene v16s46_10 # TPP Show MC (mouth closed) looking on his bed, pulling down the covers
    with dissolve

    u "(Not here...)"

    scene v16s46_8
    with dissolve

    baby "*Cries*"

    scene v16s46_11 # TPP MC (mouth open) holding his hands out to the baby doll, as if soothing a real baby
    with dissolve

    u "I'm sorry, [BABY_NAME]..."

    scene v16s46_12 # TPP MC (mouth closed) searching under his bed
    with dissolve

    u "(Shit...)"

    scene v16s46_8
    with dissolve

    baby "*Screaming cry*"

    scene v16s46_13 # TPP MC (mouth open) searching in the bedside table
    with dissolve

    u "(Fuck!) Where are the fucking keys?!"

    if not joinwolves: # -if Apes
        # -Only the closed door is shown. The door never opens, and the voices are just coming from the other side-
        scene v16s46_14 # FPP Show the closed door to MC's room
        with dissolve

        *Banging on door* ### NOT SURE HOW TO CODE A NOISE

        sa "[name]! Shut that thing up, now!"

        scene v16s46_8
        with dissolve

        baby "*Cries*"

        scene v16s46_15 # TPP MC (mouth closed) on his hands and knees scanning the floor
        with dissolve

        menu:
            "Be sorry":
                 $ add_point(KCT.BRO)

                scene v16s46_14
                with dissolve

                u "Yeah, I'm trying! Sorry!"

                scene v16s46_15
                with dissolve

                sa "Well, try harder!"

            "Be agitated":
                 $ add_point(KCT.TROUBLEMAKER)

                scene v16s46_14
                with dissolve

                u "Don't you think I'm trying?!"

                sa "It's waking everyone up, [name]."

                scene v16s46_16 # TPP MC (mouth open) searching his closet
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

        scene v16s46_8
        with dissolve

        baby "*Crying*"

        scene v16s46_14
        with dissolve

        sa "[name] has one of those stupid fucking baby dolls."

        ca "*Sighs*"

        ca "It's pretty simple, dingus! Just use the keys and it stops crying."

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

        scene v16s46_15
        with dissolve

        ca "I have a very strong paternal instinct! Just, shut it up!"

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

        scene v16s46_17 # TPP MC (mouth closed) searching behind his bed
        with dissolve

        gr "Who's this time?"

        sa "[name] is playing daddy tonight."

        scene v16s46_8
        with dissolve

        baby "*Cries*"

        scene v16s46_
        with dissolve

        gr "Why do-"

        scene v16s46_12
        with dissolve

        gr "No. You know what? I don't care."

        scene v16s46_14
        with dissolve

        *Banging on door* # NOT SURE HOW TO CODE NOISE

        gr "Shut that fucking thing up before I rip this door down!"

        scene v16s46_11
        with dissolve

        u "I'm going to!"

        u "Somehow..."

        scene v16s46_8
        with dissolve

        baby "*Crying*"

    # -Regardless of Apes-
    scene v16s46_18 # TPP MC (mouth closed) picking up the baby and looking underneath - he see's the keys
    with dissolve

    u "(Fuck my life, dude!)"

    scene v16s46_19 # FPP Closeup of the keys in MC's hand, all three clearly visible
    with dissolve

    u "(Okay, it's time for a diaper change. Which key was it?)"

    # -If MC chooses an incorrect key, the choice menu appears again for another attempt-
    while v16s46_wrong_key: # NOT SURE IF THIS IS THE BEST WAY TO IMPLIMENT THIS
        menu:
            "Blue":
                scene v16s46_20 # TPP MC (frustrated expression, mouth closed) using  the blue key on the baby doll
                with dissolve

                baby "*Cries*"

                scene v16s46_19
                with dissolve

                u "(Dammit... Not blue.)"

            "Green":
                scene v16s46_20a # TPP Same angle as 20, MC (frustrated expression, mouth closed) using the green key on the baby doll
                with dissolve

                baby "*Scream crying*"

                scene v16s46_19
                with dissolve

                u "(Ah, for fuck's sake...) Okay, okay! Wrong one, got it. Shhhh..."

            "Orange":
                $ v16_wrong_key = False

                scene v16s46_20b # TPP Same angle as 20, MC (relieved expression, mouth closed) using the orange key on the baby doll
                with dissolve

                baby "*Cooing*"

                scene v16s46_21 # FPP MC holding baby doll up in front of him in both hands
                with dissolve

                u "*Sighs* Finally..."

    scene v16s46_22 # TPP MC (relieved, mouth closed) placing the baby doll on the chair with the keys next to it
    with dissolve

    pause 0.75

    if not joinwolves: # -if Apes
        ca "Well done, dad!"

        scene v16s46_14
        with dissolve

        sa "If I wake up because of that kid one more time tonight, I'm calling child protective services."

        gr "Wait, does [name] actually have a baby?"

        sa "I'll explain tomorrow."

        scene v16s46_23 # TPP MC (exhausted, mouth closed) sitting on the edge of the bed with his head in his hands
        with dissolve

        gr "Wha- Cam?"

        ca "Back to bed, kids."

        scene v16s46_14
        with dissolve

        gr "What the hell is happening around here?"

    scene v16s46_24 # FPP MC shutting off the light
    with dissolve

    pause 0.75

    scene v16s46_25 # TPP MC (eyes closed, mouth open) lays in bed with his arm across his face
    with dissolve

    u "Okay, I don't want any more of that, [baby_name]... Please, let's get some sleep now."

    jump v16s50a # -Transition to Scene 50a-