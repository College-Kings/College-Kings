# SCENE 49: Baby Night with Nora
# Locations: Chicks Sorority House/Living Room
# Characters: MC (Outfit: 9), NORA (Outfit: 1), WOMAN IN MOVIE (Outfit: 1), MAN IN MOVIE (Outfit: 1), [BABY] (Outfit: 1)
# Time: Night

label v16s49:
    scene v16s49_1 # TPP. MC (slight smile, mouths is closed, looking at Nora) follows Nora (slight smile, mouth is closed, looking at MC) carrying the baby into the living room.
    with dissolve

    pause 0.75

    scene v16s49_2 # TPP. MC (slight smile, mouths is closed, looking at Nora) and Nora (slight smile, mouth is closed, looking at MC) sit down on the couch. Nora keeps hold of the baby.
    with dissolve

    pause 0.75

    scene v16s49_3 # FPP. Nora (slight smile, mouth is closed, looking at MC) sitting on the couch, still holding the baby
    with dissolve

    u "Getting attached to [v16_baby] already, huh?"

    scene v16s49_3a # FPP. Nora (slight smile, mouth is open, looking at MC) sitting on the couch, still holding the baby
    with dissolve

    no "Yeah, I'm totally in mom mode right now, haha."

    scene v16s49_3
    with dissolve

    u "It's nice to see."

    scene v16s49_3b # FPP. Nora (half smile, mouth is closed, looking at MC) sitting on the couch, still holding the baby
    with dissolve

    pause 0.75

    scene v16s49_3a
    with dissolve

    no "Let's put a movie on, yeah?"

    scene v16s49_3
    with dissolve

    u "Okay, but not too loud. We don't want to wake the baby."

    scene v16s49_3a
    with dissolve

    no "*Chuckles* I'm expecting we'll need to use a key soon anyway."

    scene v16s49_3c # FPP. Nora (half smile, mouth is open, looking at MC) sitting on the couch, holds the baby face out towards MC to hold
    with dissolve

    no "Here, you hold [v16_baby]."

    scene v16s49_4 # TPP. Nora (slight smile, mouth is closed, looking at MC) hands MC (slight smile, mouths is closed, looking at Nora) the baby
    with dissolve

    pause 0.75

    scene v16s49_5 # TPP. Nora (slight smile, mouth is closed, looking back at MC) points the remote control at the TV in the Chicks Living Room, MC (slight smile, mouths is closed, looking at Nora) is holding the baby in his arms
    with dissolve

    pause 0.75

    scene v16s49_6 # TPP. Nora (slight smile, mouth is closed, looking at MC) and MC (slight smile, mouths is closed, looking at the baby) sitting close too each other on the couch while MC holds the baby in his arms 
    with fade

    pause 0.75

    scene v16s49_7 #  TPP Nora( slight smile, mouth closed, watching the TV) and MC (slight smile, mouth closed, watching the TV) sitting close to each other on the couch while MC holds the baby in his arms (TV is the ambient light that fills the dark room [CAMERA FROM THE TV POV]
    with dissolve

    wim "The car was in neutral. I don't know how it happened!"

    scene v16s49_7a # TPP Nora( slight smile, mouth closed, looking at MC) and MC (slight smile, mouth closed, watching the TV) sitting close to each other on the couch while MC holds the baby in his arms (TV is the ambient light that fills the dark room [CAMERA FROM THE TV POV]
    with dissolve

    mim "It doesn't matter what your excuse is, lady. You've crashed through my store window!"

    scene v16s49_7b # TPP Nora( slight smile, mouth closed, watching TV) and MC (slight smile, mouth closed, looking at Nora) sitting close to each other on the couch while MC holds the baby in his arms (TV is the ambient light that fills the dark room [CAMERA FROM THE TV POV]
    with dissolve

    wim "I'm sorry!"

    scene v16s49_7
    with dissolve

    mim "Sorry? I can't pay the bills with an-"
    
    mim "Wait... Veronica?"

    scene v16s49_7b
    with dissolve

    wim "...David? I thought you had perished in that Bar Mitzvah explosion all those years ago..."

    scene v16s49_7
    with dissolve

    mim "...And I thought YOU had died in quicksand!"

    scene v16s49_7a
    with dissolve

    wim "No, that was Maggie, my twin! I'm alive, I'm here!"

    scene v16s49_7
    with dissolve

    mim "Oh, Veronica! I thought I'd never get the chance to tell you my true feelings..."

    play sound "sounds/babycry.mp3"
    
    scene v16s49_8 # FPP. Close up shot of the baby doll in MC's Arms, Don't show the rest of MC
    with vpunch

    baby "*Crying*"

    scene v16s49_3d # FPP. Nora (slight smile, mouth is open, looking at MC) sitting on the couch, NOT holding the baby
    with dissolve

    no "And there it is..."

    scene v16s49_3e # FPP. Nora (slight smile, mouth is closed, looking at MC) sitting on the couch, NOT holding the baby
    with dissolve

    u "Dammit, it was just getting good! Bar Mitzvahs, quicksand... This movie is filled with drama!"

    scene v16s49_3d
    with dissolve

    no "Haha, parental duties come first."

    play sound "sounds/babycry.mp3"

    scene v16s49_8
    with dissolve

    baby "*Crying*"

    scene v16s49_3d
    with dissolve

    no "When I picked [v16_baby] up from campus, the teacher let it slip that it had just been burped."

    scene v16s49_3e
    with dissolve

    u "Oh, really?"

    scene v16s49_3d
    with dissolve

    no "Yeah, so I'm pretty confident it's time for a diaper change."

    scene v16s49_3f # FPP. Nora (slight smile, mouth is open, looking at MC) sitting on the couch, NOT holding the baby, handing MC the FOB Key
    with dissolve

    no "Here you go."

    scene v16s49_9 # FPP. Show just the green, orange, and blue FOB keys in MC's Hand
    with dissolve

    pause 0.75

    scene v16s49_3e
    with dissolve

    u "Oh, I see. So, I get the messy job, huh?"

    scene v16s49_3d
    with dissolve

    no "What's the matter? Too afraid to get your hands dirty? *Giggles*"

    play sound "sounds/babycry.mp3"

    scene v16s49_8
    with vpunch

    baby "*Crying*"

    scene v16s49_6a # TPP. Nora (slight smile, mouth is closed, looking at the TV) and MC (concerned expression, mouths is closed, looking at the baby) sitting close too each other on the couch while MC holds the baby on his lap with the FOB key in one of his hands in front of the baby
    with dissolve

    pause 0.75

    scene v16s49_9
    with dissolve

    $ v16_wrong_key = True

# -If MC chooses an incorrect key, the choice menu appears again for another attempt-
    while v16_wrong_key:
        menu:
            "Blue":
                scene v16s49_9a # FPP. Show just the BLUE Fob Key in MC's hand pressing it to the baby's lower back (Baby is in MCs lap)
                with dissolve

                pause 0.75

                play sound "sounds/babycry.mp3"

                scene v16s49_8
                with vpunch

                baby "*Crying*"
                
                u "(Nope! I think blue is for feeding.)"

                scene v16s49_9
                with dissolve
                    
            "Green":
                scene v16s49_9b # FPP. Show just the GREEN Fob Key in MC's hand pressing it to the baby's lower back (Baby is in MCs lap)
                with dissolve

                pause 0.75

                play sound "sounds/babycry.mp3"

                scene v16s49_8
                with vpunch

                baby "*Crying*"
                
                u "(Come on, [v16_baby]! Please stop...)"

            "Orange": # (CORRECT)
                $ v16_wrong_key = False

                play sound "sounds/babycoo.mp3"

                scene v16s49_9c # FPP. Show just the ORANGE Fob Key in MC's hand pressing it to the baby's lower back (Baby is in MCs lap)
                with dissolve

                u "Got it! Diaper successfully changed."

                scene v16s49_3d
                with dissolve

                no "Nice, good job!"

    scene v16s49_7
    with fade

    pause 0.75

    scene v16s49_3d
    with dissolve

    no "Here, I can take [v16_baby] back now."

    scene v16s49_3g # FPP. Nora (half smile, mouth is closed, looking at MC) sitting on the couch, MC is handing the baby to Nora baby's face is towards Nora and it's back is towards MC
    with dissolve

    u "Oh, okay. Damn... We really are sharing responsibilities evenly."

    scene v16s49_3a
    with dissolve

    no "I think all good parenting involves delegation."

    no "You deal with the dirty diapers, I'll deal with the feeding, and we can share the burping, haha."

    scene v16s49_3
    with dissolve

    u "I bet that's a sentence you never thought you'd say."

    scene v16s49_3a
    with dissolve

    no "*Chuckles* That's so true."

    no "I never thought a surprise college project like this would be so fun. I'm actually enjoying it."

    scene v16s49_3
    with dissolve

    u "I can tell. You've got a natural motherly instinct. *Laughs* I guarantee most people would just throw it to the side."

    scene v16s49_3a
    with dissolve

    no "Haha, yeah, or out the window."

    no "Luckily, I'm not like that."

    scene v16s49_3
    with dissolve

    u "Yeah, I definitely chose the right person to be the mother of my plastic baby."

    scene v16s49_3a
    with dissolve

    no "*Laughs*"

    scene v16s49_3b
    with dissolve

    pause 0.75

    scene v16s49_6c # TPP. Nora (slight smile, mouth is closed, looking at the TV) and MC (slight smile, mouths is closed, looking at the TV) sitting close too each other on the couch while Nora is holding the baby in her arms (TV is the ambient light that fills the dark room [CAMERA FROM THE TV POV]
    with dissolve

    pause 0.75

    scene v16s49_6d # TPP. Nora (yawns, mouth is open, eyes closed) and MC (slight smile, mouths is closed, looking at Nora) sitting close too each other on the couch while Nora hands the baby to MC (TV is the ambient light that fills the dark room [CAMERA FROM THE TV POV]
    with dissolve

    pause 0.75

    scene v16s49_6e # TPP. Nora (sleeping against MC shoulder, mouth is closed, eyes are closed) and MC (sleeping, head slightly forward, mouth is closed, eyes are closed) sitting close too each other on the couch while MC holds up the baby with one arm, Mc has his other arm wrapped around Nora, Nora's head is resting on MC's shoulder, and Mc is resting his head on Nora's head (TV is the ambient light that fills the dark room [CAMERA FROM THE TV POV]
    with fade

    pause 0.75

    play sound "sounds/babycry.mp3"

    scene v16s49_8
    with dissolve

    baby "*Crying*"

    pause 0.75

    play sound "sounds/babycry.mp3"

    scene v16s49_6f # TPP. Nora (shocked expression, mouth is open, eyes are wide open, head against MC's chest) and MC (shocked expression, mouth is open, eyes are wide open, arm around Nora, head resting on Nora's head) sitting close too each other on the couch. Mc struggles to hold onto the baby (TV is the ambient light that fills the dark room [CAMERA FROM THE TV POV]
    with vpunch

    baby "*Crying*"

    pause 0.75

    scene v16s49_3d
    with dissolve

    no "Oh, shit. That made me jump, haha."

    scene v16s49_3e
    with dissolve

    u "*Groans* That was such a good dream, too!"

    u "I was having ice cream at the beach, and I made friends with a giant seagull, and he flew me to Hawaii."

    scene v16s49_3d
    with dissolve

    no "You made friends with a giant seagull?"

    scene v16s49_3e
    with dissolve

    u "Yeah, his name was Florian."

    play sound "sounds/babycry.mp3"

    scene v16s49_8
    with dissolve

    baby "*Crying*"

    scene v16s49_3g
    with dissolve

    pause 0.75

    scene v16s49_10 # FPP. Nora (slight smile, mouth is open, looking at the baby) stands up with the baby, holding the baby with both arms, Camera angle is from MC's seated position from renders v16s49_3
    with dissolve

    no "Shh, shh, baby. It's okay..."

    no "Momma's here."

    play sound "sounds/babycry.mp3"

    scene v16s49_11 # FPP, Show just a close up shot of the baby's face
    with vpunch

    baby "*Crying*"

    scene v16s49_10a # FPP. Nora (slight smile, mouth is open, looking at MC) is standing up with the baby, holding the baby with both arms, Camera angle is from MC's seated position from renders v16s49_3
    with dissolve

    no "You need to calm your little head so mommy and daddy can get back to sleep."

    play sound "sounds/babycry.mp3"

    scene v16s49_11
    with vpunch

    baby "*Crying*"

    scene v16s49_10b # FPP. Nora (concerned expression, mouth is open, looking at the baby) is standing up with the baby, holding the baby with both arms, Camera angle is from MC's seated position from renders v16s49_3
    with dissolve

    no "Aw, are you hungry again? Is that what's wrong?"

    scene v16s49_10c # FPP. Nora (concerned expression, mouth is closed, looking at MC) is standing with the baby, holding the baby with both arms, Camera angle is from MC's seated position from renders v16s49_3
    with dissolve

    menu:
        "Grab the keys":
            scene v16s49_12 # FPP. Nora (concerned expression, mouth is closed, looking at MC) she is holding the baby, MC hands Nora the BLUE FOB key, camera angle is with both Mc and Nora standing
            with dissolve

            pause 0.75

            scene v16s49_12a # FPP. Nora (slight smile, mouth is closed, looking at MC) she is holding the BLUE FOB key and the baby, camera angle is with both Mc and Nora standing
            with dissolve

            u "I think you're gonna need these."

            scene v16s49_12b # FPP. Nora (slight smile, mouth is open, looking at MC) she is holding the BLUE FOB key and the baby, camera angle is with both Mc and Nora standing
            with dissolve

            no "Why, thank you, daddy."

            scene v16s49_12c # FPP. Nora (slight smirk, mouth is open, looking at MC) she is holding the BLUE FOB key and the baby, camera angle is with both Mc and Nora standing
            with dissolve

            u "(I can get used to that nickname.)"

            scene v16s49_12b
            with dissolve

            no "We make such a good team."

            scene v16s49_12a
            with dissolve

            u "We honestly do, I can't lie."

            play sound "sounds/babycry.mp3"

            scene v16s49_11
            with vpunch

            baby "*Crying*"

            play sound "sounds/babycoo.mp3"

            scene v16s49_12d # FPP. Nora (slight smile, mouth is open, looking at the baby) she is holding the FOB key to the babies mouth, camera angle is with both Mc and Nora standing
            with dissolve

            no "There. Isn't that yummy?"

            scene v16s49_6c
            with dissolve

            pause 0.75

            scene v16s49_3a
            with dissolve

            no "You know, I'm really glad we're partners."

            scene v16s49_3
            with dissolve

            u "Me too. This has been fun, spending time with you."

            scene v16s49_3a
            with dissolve

            no "I think you'll make a good father one day."

            scene v16s49_3
            with dissolve

            u "Do you really think so?"

            scene v16s49_3a
            with dissolve

            no "Of course! You're very attentive, and caring... Plus, you don't seem to mind the crying."

            scene v16s49_3
            with dissolve

            u "Oh, crying? Music to my ears, truly."

            scene v16s49_3a
            with dissolve

            no "And it's exactly that type of reply that makes you such a good partner, haha."

            if "v15_nora" in sceneList:
                scene v16s49_13 # TPP. Show MC (slight smile, mouths is closed, looking at Nora) and Nora (slight smile/blushing expression, mouth is closed, eyes are closed, facing MC) sitting on the couch, Nora is still holding the baby leaning in for a kiss from MC, they are not kissing yet (TV is the ambient light that fills the dark room [CAMERA FROM THE TV POV]
                with dissolve

                menu:
                    "Kiss her":
                        scene v16s49_13a # TPP. Show MC (kissing Nora eyes are closed) with one hand holding Nora's cheek and pulling her closer towards him and Nora (kissing Mc eyes are closed) she is still holding the baby, both of them still sitting on the couch
                        with dissolve

                        pause 0.75

                        scene v16s49_13b # TPP. Show MC (slight smile, mouths is closed, looking at the baby) with one hand still onto holding Nora's cheek, and the other placed behind the baby's head in a craddling fashion as Nora is still holding the baby, and Nora (with a lustful expression looking at MC) still holding the baby, both of them still sitting on the couch
                        with dissolve
                        
                        pause 0.75

                        scene v16s49_13c # TPP. Show MC (slight smile, mouths is closed, looking at Nora) with one hand still onto holding Nora's cheek, and the other placed behind the baby's head in a craddling fashion as Nora is still holding the baby, and Nora (slight smile, mouth is closed, looking at MC) still holding the baby, both of them still sitting on the couch
                        with dissolve

                        pause 0.75

                        scene v16s49_3a
                        with dissolve

                        no "Okay, back to sleep before the next round..."

                        scene v16s49_6j # TPP. Nora (full smile, mouth is closed, closing her eyes) lies her head on MC's lap with her feet up on the couch still holding the baby, MC (full smile, mouth is closed, looking at Nora) is still sitting on the couch
                        with dissolve

                        pause 0.75

                        scene v16s49_14 # TPP. Close up shot of MC closing his eyes with a tired expression
                        with dissolve

                        pause 0.75

                        scene v16s49_14a # TPP. Close up shot of MC with closed eyes mouth agape
                        with dissolve

                        pause 0.75

                        scene v16s49_14b # TPP. Close up shot of MC waking up holding his neck, slight pained expression
                        with dissolve

                        u "*Groans* (Ah, my neck. This really isn't comfortable.)"

                        scene v16s49_15 # FPP. Show a close up shot of Nora sleeping happily in his lap, still holding the baby
                        with dissolve

                        u "(Nora and [v16_baby] are still fast asleep. I think this i a good time for me to head home.)"

                        scene v16s49_16 # TPP. MC (slight smile, mouths is closed, looking at Nora) rests a pillow under Nora's head as he gets up from the couch, make sure MC and Nora's position matches v16s49_6j, Nora is still sleeping
                        with dissolve

                        pause 0.75

                        scene v16s49_17 # TPP. MC (slight smile, mouths is closed) is shown exiting the front door of the chicks sorority house
                        with dissolve

                        jump v16s49a # -Transition to Scene 49a-

                    "Keep it PG":
                        scene v16s49_13d # TPP. Show MC (no expression, mouths is open, looking at Nora) and Nora (slightly shocked expression, mouth is closed, looking at MC)  Nora is still holding the baby, sitting on the couch

                        u "Um... Sorry, it's just... It feels kind of weird to make out when there's a baby right there."

                        scene v16s49_13e # TPP. Show MC (no expression, mouth is closed, looking at Nora) and Nora (fake/dissapointed smile, mouth is open, looking at MC)  Nora is still holding the baby, sitting on the couch
                        with dissolve

                        no "Oh- Haha! I guess you're right, sorry."

                        no "Okay, back to sleep before the next round..."

                        scene v16s49_6i # TPP. Nora (slight smile, mouth is closed, closing her eyes) lies her head down on the couch arm opposite of MC, still holding the baby, with her feet up in MC's lap, MC (slight smile, mouth is closed, looking at Nora) is still sitting on the couch
                        with dissolve

                        pause 0.75

                        scene v16s49_14
                        with dissolve

                        pause 0.75

                        scene v16s49_14a 
                        with dissolve

                        pause 0.75

                        scene v16s49_14b 
                        with dissolve

                        u "*Groans* (Ah, my neck. This really isn't comfortable.)"

                        scene v16s49_18 # FPP. Show a close up shot of Nora sleeping with her head on the other side of the couch, feet on the couch still holding the baby
                        with dissolve

                        u "(Nora and [v16_baby] are still fast asleep. I think this i a good time for me to head home.)"

                        scene v16s49_19 # TPP. Show Nora (sleeping) still holding the baby and in the same position as v16s49_6i as MC (slight smile, mouths is closed, looking at Nora) gets up from the couch
                        with dissolve

                        jump v16s49a # -Transition to Scene 49a-

        "Cover your ears":
            scene v16s49_10c
            with dissolve

            u "Ugh, just feed the damn thing so we can go back to sleep already!"

            scene v16s49_10d # FPP. Nora (no expression, mouth is open, looking at MC) is standing with the baby, holding the baby with both arms, Camera angle is from MC's seated position from renders v16s49_3
            with dissolve

            no "Really? Is that what you'd say if there was a real baby here?"

            play sound "sounds/babycry.mp3"

            scene v16s49_11
            with vpunch

            baby "*Crying*"

            scene v16s49_10e # FPP. Nora (frustrated expression, mouth is closed, looking at MC) is standing with the baby, holding the baby with both arms, Camera angle is from MC's seated position from renders v16s49_3
            with dissolve

            u "I can't hear you over all the crying!"

            scene v16s49_10f # FPP. Nora (frustrated expression, mouth is open, looking at MC) is standing with the baby, holding the baby with both arms, Camera angle is from MC's seated position from renders v16s49_3
            with dissolve

            no "Take your hands off of your ears, grow up, and hand me the keys!"

            scene v16s49_10e
            with dissolve

            u "*Scoffs* I was only joking around."

            play sound "sounds/babycry.mp3"

            scene v16s49_11
            with vpunch

            baby "*Crying*"

            scene v16s49_10g # FPP. Nora (slightly angry expression, mouth is open, looking at MC) is standing up with the baby, holding the baby with both arms, Camera angle is from MC's seated position from renders v16s49_3
            with dissolve

            no "Come on, [name]. You know I want to take this seriously."

            scene v16s49_10e
            with dissolve

            u "Okay, okay."

            play sound "sounds/babycry.mp3"

            scene v16s49_11
            with vpunch

            baby "*Crying*"

            scene v16s49_12e # FPP. Nora (concerned expression, mouth is closed, looking at MC) she is holding the baby, MC hands Nora the BLUE, ORANGE, and GREEN FOB key, camera angle is with both Mc and Nora standing
            with dissolve

            pause 0.75

            scene v16s49_12f # FPP. Nora (concerned expression, mouth is closed, looking at the baby) she is holding the baby and places the blue FOB key to the baby's mouth, camera angle is with both Mc and Nora standing
            with dissolve

            pause 0.75

            play sound "sounds/babycoo.mp3"

            scene v16s49_12d
            with dissolve

            no "Phew... All better now?"

            scene v16s49_6g # TPP. Nora (slightly frustrated expression, mouth is closed, looking at MC) and MC (no expression, mouth is closed, looking at Nora) sitting close too each other on the couch while Nora is holding the baby in her arms
            with dissolve

            pause 0.75

            scene v16s49_13e
            with dissolve

            no "Okay, back to sleep before the next round..."

            scene v16s49_6h # TPP. Nora (no expression, mouth is closed, closing her eyes) lies her head down on the couch arm opposite of MC, still holding the baby, with her feet up on the couch between her and MC, MC (no expression, mouth is closed, looking at Nora) is still sitting on the couch
            with dissolve

            pause 0.75

            scene v16s49_14 
            with dissolve

            pause 0.75

            scene v16s49_14a 
            with dissolve

            pause 0.75

            scene v16s49_14b 
            with dissolve

            u "*Groans* (Ah, my neck. This really isn't comfortable.)"

            scene v16s49_18
            with dissolve

            u "(Nora and [v16_baby] are still fast asleep. I think this i a good time for me to head home.)"

            scene v16s49_19
            with dissolve

            jump v16s49a # -Transition to Scene 49a-