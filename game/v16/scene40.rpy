# SCENE 40: Aubrey & Mc outside the restaurant
# Locations: Outside of the Aubrey Date Night Restauraunt
# Characters: AUBREY (Outfit: DATE NIGHT OUTFIT), MC (Outfit: DATE NIGHT OUTFIT)
# Time: Evening


label v16s40:

    scene v16s40_1 # TPP. MC and Aubrey exit the front door of the restaurant both of them slight smiles, mouths are closed, looking at each other
    with dissolve

    pause 0.75

    scene v16s40_2 # TPP. MC and Aubrey stop turn and face each other a few feet away from the entrance of the restaurant, both of them slight smiles, mouths are closed
    with dissolve

    if v16s39aubrey_date_points >= 10: ### ERROR: IF MC scored maximum 10 points

        scene v16s40_3 # FPP. Show just Aubrey from the waist up, slight smile, mouth is open, looking at MC, show Aubrey holding both of Mc's hand 
        with dissolve

        au "You know, I started out kind of anxious, but that was an amazing first official date, [name]."

        au "Thank you."

        scene v16s40_4 # TPP. Aubrey kisses MC passionately, and holds MC's hand, both of their eyes are closed during the kiss, Mc wraps his arm around Aubreys back as she kisses him.
        with dissolve

    if v16s39aubrey_date_points == 8 or v16s39aubrey_date_points == 9: ### ERROR: IF MC scored 8-9 points

        scene v16s40_3a # FPP. Show just Aubrey from the waist up, slight smile, mouth is open, looking at MC, show Aubrey holding one of Mc's hand 
        with dissolve

        au "Thanks, [name]. Overall, I had a great time tonight."

        scene v16s40_3b # FPP. Show just Aubrey from the waist up, slight smile, mouth is closed, looking at MC, show Aubrey holding one of Mc's hand 
        with dissolve

        u "Haha, sounds like you were keeping score or something."

        scene v16s40_3a
        with dissolve

        au "Something like that, hehe."

    if v16s39aubrey_date_points >= 4 and v16s39aubrey_date_points <= 7: ### ERROR: IF MC scored 4-7 points

        scene v16s40_3a
        with dissolve

        au "Well, it wasn't a perfect evening, but you did okay... just about."

        scene v16s40_3b
        with dissolve

        u "Ha, I guess I'll have to step it up next time?"

        scene v16s40_3a
        with dissolve

        au "Mmm, yeah you probably should, haha."

    ### ERROR: END IF

    if v16s39aubrey_date_points >= 4: ### ERROR: IF MC scored 4-10 points (passed the date)
        $ aubrey.relationship.value == Relationship.GIRLFRIEND.value

        scene v16s40_3c # FPP. Show just Aubrey from the waist up, slight smile, mouth is closed, looking at MC
        with dissolve

        u "I'm glad you had a good time. I did too."

        u "I guess this makes us a proper couple now?"

        scene v16s40_3d # FPP. Show just Aubrey from the waist up, slight smile, mouth is closed, turning her head slightly away from MC but still looking at MC, slightly blushing
        with dissolve

        pause 0.75

        scene v16s40_3e # FPP. Show just Aubrey from the waist up, slight smile, mouth is open, slightly blushing, looking at MC 
        with dissolve

        au "Yeah... It does. As weird as it sounds, it feels right."

        scene v16s40_3f # FPP. Show just Aubrey from the waist up, slight smile, mouth is closed, slightly blushing, looking at MC 
        with dissolve

        u "You being by my side has always felt right, now I can just call you my girlfriend."

        scene v16s40_3e
        with dissolve

        au "Haha. Exactly... Boyfriend."

        scene v16s40_3d
        with dissolve

        pause 0.75

        scene v16s40_4a # TPP. Aubrey and MC embrace each other and kiss, Aubrey hands are up and MC's shoulders, MC's hands are around the small of Aubrey's back just above her butt
        with dissolve

        pause 0.75

        scene v16s40_3c
        with dissolve

        u "Do you wanna walk back to your place?"

        scene v16s40_3g # FPP. Show just Aubrey from the waist up, slight smile, mouth is open, looking at MC
        with dissolve

        au "Um... Actually, I don't think we should."

        scene v16s40_3c
        with dissolve

        u "Oh. How come?"

        scene v16s40_3c
        with dissolve

        au "Tonight was like our first real date, so I want to do this right."

        scene v16s40_3g
        with dissolve

        u "Okay... And?"

        scene v16s40_3c
        with dissolve

        au "So, let's end the night here? Separately? Like adults?"

        scene v16s40_3g
        with dissolve

        u "Haha, wow. Are you sure?"

        scene v16s40_3c
        with dissolve

        au "Yeah, and trust me. When we see each other again, it's going to be extra special."

        scene v16s40_4b # TPP. Aubrey leans close to whisper into MC's ear slight smile mouth is open, using one hand to funnel the sound into his ear, and the other hand is on his chest, she is looking at and winking at MC, MC's hands are to the sides not touching Aubrey, looking at Aubrey, slight smile, mouth is closed
        with dissolve

        au "I'll make sure of it..."

        scene v16s40_3c
        with dissolve

        u "Well, shit. Sign me up."

        scene v16s40_3
        with dissolve

        au "Haha, you're too cute."

        scene v16s40_4c # TPP. Aubrey leans in and gives MC's a quick kiss on the cheek, Mc also kisses Aubrey on the cheek, both of them slight smiles
        with dissolve

    ### ERROR: IF MC has baby duties tonight 
    ### TRANSCRIBER NOTE!!! ### THERE IS NO ALTERNATIVE SCENE TO TRAVEL TOO, REGARDLESS OF "BABY DUTIES" MC FIRST HAS TO GO HOME TO CHANGE BEFORE EITHER "BABY DUTY" SCENE HAPPENS MAKING THIS "IF STATEMENT" UNNECESSARY, IF IT IS SCENE DEPENDENT DIALOGUE THEN IT REQUIRES CLARIFICATION AS TO WHICH "BABY DUTY" SCENE THIS DIALOGUE REFERS TOO ### ATTENTION!!! ###

    scene v16s40_3c
    with dissolve

    u "That's probably for the best, anyway. I just remembered I'm on baby duty tonight."

    scene v16s40_3g
    with dissolve

    au "Oh, yeah... Been there and done that, no thank you! *Laughs*"

    scene v16s40_3c
    with dissolve

    u "Well, think of me when you're enjoying a quiet, relaxing slumber..."

    scene v16s40_3g
    with dissolve

    au "Haha, I will. Good luck!"

    scene v16s40_3c
    with dissolve

    u "Thanks, ha."

    ### ERROR: END IF

    scene v16s40_3c
    with dissolve

    u "Alright then, goodnight beautiful."

    scene v16s40_3
    with dissolve

    au "Night, [name]."

    scene v16s40_2a # TPP. MC (slight smile, mouth is closed) is still in the same position from render v16s40_2 looking at Aubrey walking away, Aubrey (slight smile, mouth is closed) is looking at and waving to MC as she walks away
    with dissolve

    jump v16s41 # -Transition to Scene 41-

    ### ERROR: END IF

    if v16s39aubrey_date_points <= 3: ### ERROR: IF MC scored 0-3 points (DATE FAIL = Loses AubreyTamed)
        $ AubreyTamed = False

        scene v16s40_3h # FPP. Show just Aubrey from the waist up, no expression, mouth is closed, looking at MC
        with dissolve

        u "So, did you have a good time?"

        scene v16s40_3i # FPP. Show just Aubrey from the waist up, no expression, mouth is open, looking at MC
        with dissolve

        au "Um... It could have gone better, I think..."

        scene v16s40_3h
        with dissolve

        u "What do you mean?"

        scene v16s40_3i
        with dissolve

        au "I just don't think this is going to work, [name]."

        scene v16s40_3h
        with dissolve

        u "What?"

        scene v16s40_3i
        with dissolve

        au "Like, it still just feels so unnatural for me. I'm sorry."

        au "I think our perfect relationship is being close friends, if I'm being honest."

        scene v16s40_3h
        with dissolve

        u "Oh... I guess so."

        scene v16s40_3i
        with dissolve

        au "I'm sorry, [name]. I still care about you, and love being around you. Just didn't feel the sparks tonight."

        scene v16s40_3h
        with dissolve

        u "I get it, thanks for being honest. I'm sorry it didn't go as well as we both wanted it to."

        scene v16s40_3i
        with dissolve

        au "Don't apologize, you were being yourself and that's the most important thing."

        scene v16s40_3h
        with dissolve

        u "*Sighs* Yeah, okay."

        ### ERROR: IF MC has baby duties tonight
        ### TRANSCRIBER NOTE!!! ### THERE IS NO ALTERNATIVE SCENE TO TRAVEL TOO, REGARDLESS OF "BABY DUTIES" MC FIRST HAS TO GO HOME TO CHANGE BEFORE EITHER "BABY DUTY" SCENE HAPPENS MAKING THIS "IF STATEMENT" UNNECESSARY, IF IT IS SCENE DEPENDENT DIALOGUE THEN IT REQUIRES CLARIFICATION AS TO WHICH "BABY DUTY" SCENE THIS DIALOGUE REFERS TOO ### ATTENTION!!! ###

        scene v16s40_3c
        with dissolve

        u "I should uh, head back now. I'm on baby duty tonight."

        scene v16s40_3g
        with dissolve

        au "Oh, yeah. Good luck with that, haha. I hope it doesn't cry too much."

        scene v16s40_3c
        with dissolve

        u "Haha, I hope so too, thanks."

        ### ERROR: END IF

        scene v16s40_3g
        with dissolve

        au "And it's time for me to go home and put on something more comfortable!"

        scene v16s40_3c
        with dissolve

        au "Night, [name]."

        scene v16s40_3g
        with dissolve

        u "Night, Aubrey."

        scene v16s40_4d # TPP. MC and Aubrey share a quick hug, slight smiles, mouths are closed
        with dissolve

        ### ERROR: END IF

        scene v16s40_2a
        with dissolve

        jump v16s41# -Transition to Scene 41-

    # EDITOR NOTE!!! # (Can you please double check that this makes sense according to miro, and it all adds up? From my pov I think it's good but want to make sure everything is covered and lines up evenly. DM with any questions -cheexi)