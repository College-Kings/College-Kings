# SCENE 31: Apes 1
# Locations: Apes Frat House
# Characters: GRAYSON (Outfit: 3), SAMANTHA (Outfit: 1), MC (Outfit: 9)
# Time: Afternoon

label v16s31:
    scene v16s31_1 # TPP. MC enters the house, seeing Grayson and Samantha in the kitchen. Grayson is looking in the refrigerator, the refrigerator light is off, Grayson has a slightly annoyed expression, mouth is closed. Samantha sat on a stool at the countertop looking at MC slight smile mouth is closed. MC joins them slight smile mouth is closed
    with dissolve

    pause 0.75

    scene v16s31_2 # FPP. Show just Grayson leaning and looking into the fridge, slightly annoyed, mouth is open
    with dissolve

    gr "It's definitely switched off."

    scene v16s31_3 # FPP. Show Just Samanthan sitting on a stool, no expression, mouth is open, looking towards Grayson
    with dissolve

    sa "Have you checked the plug?"

    scene v16s31_2a # FPP. Show Grayson leaning into the fridge but is looking back over his shoulder at Samantha, slightly annoyed expression, mouth is open
    with dissolve

    gr "*Sighs* Of course I've checked the fucking plug."

    scene v16s31_2b # FPP. Show just Grayson has closed the fridge, slightly annoyed expression, mouth is closed, looking at MC
    with dissolve

    u "What's going on in here?"

    scene v16s31_3a # FPP. Show Just Samanthan sitting on a stool, no expression, mouth is open, looking at MC
    with dissolve

    sa "Grayson forgot to pay the electricity bill."

    scene v16s31_2c # FPP. Show just Grayson has closed the fridge, slightly annoyed expression, mouth is open, looking at Samantha
    with dissolve

    gr "No, I haven't! Stop saying that, Sam. The power just went out, I think."

    scene v16s31_2b
    with dissolve

    u "Oh yeah, Aubrey told me there's been a lot of blackouts lately."

    scene v16s31_3a
    with dissolve

    sa "Well, hopefully it won't take too long to come back on."

    scene v16s31_3b # FPP. Show Just Samantha sitting on a stool, slight smile, mouth is open, looking at Grayson
    with dissolve

    sa "'Cause Grayson can't sleep without his nightlight. *Laughs*"

    scene v16s31_2c
    with dissolve

    gr "How did you know about my- *Sighs*"

    gr "You're really starting to piss me off, Sam!"

    scene v16s31_3b
    with dissolve

    sa "Oh, calm down, Grayson. You know I'm just messing with you."

    scene v16s31_2c
    with dissolve

    gr "You know what? This little arrangement with you living here? It needs to end."

    gr "You're not an Ape. You shouldn't be here."

    scene v16s31_3c # FPP. Show Just Samantha sitting on a stool, slightly annoyed expression, mouth is open, looking at Grayson
    with dissolve

    sa "Tell that to my brother, meathead. I don't want to be here any longer than I have to!"

    if v14_SamanthaDrugs: # -if SamanthaDrugs
        scene v16s31_2c
        with dissolve

        gr "Yeah, well maybe have some self-control with the drugs, then Cameron wouldn't have to babysit you."

        scene v16s31_3c
        with dissolve

        sa "Oh, fuck off, Grayson."

        scene v16s31_2c
        with dissolve

        gr "Don't talk to me like that. I'm serious."

        scene v16s31_3b
        with dissolve

        sa "*Laughs* Whatever."

    else: # -if SamanthaSober
        scene v16s31_3
        with dissolve

        sa "I've been good lately, no drugs or alcohol. I'm hoping to be gone soon."

        scene v16s31_2c
        with dissolve

        gr "Good! I'm sick of seeing you here."

        scene v16s31_2b
        with dissolve

        u "Grayson, come on."

        scene v16s31_2d # FPP. Show just Grayson has closed the fridge, slightly annoyed expression, mouth is open, looking at MC
        with dissolve

        gr "This is a fucking frat! Not a halfway house, [name]."

    menu:
        "Agree with Grayson":
            scene v16s31_2b
            with dissolve

            u "I do see where Grayson is coming from, Sam. Not many frats have girls living on their couches."

            if v14_SamanthaDrugs: # -if SamanthaDrugs
                scene v16s31_3e # FPP. Show Just Samantha sitting on a stool, slightly annoyed expression, mouth is closeed, looking at MC
                with dissolve

                sa "Well, fuck you too, then."

                scene v16s31_2c
                with dissolve

                gr "*Scoffs* Do you see what I have to deal with?"

                scene v16s31_2b
                with dissolve

                u "*Sighs* Sam-"

                scene v16s31_3e
                with dissolve

                sa "Like I said, talk to Cameron about it!"

            else: # -if SamanthaSober
                scene v16s31_3a
                with dissolve

                sa "You know why I'm here, though. This isn't exactly what I want either, remember?"

        "Defend Samantha":
            scene v16s31_2b
            with dissolve

            u "Grayson, go easy on her."

            scene v16s31_2d
            with dissolve

            gr "Here we fucking go..."

            scene v16s31_3e # FPP. Show Just Samantha sitting on a stool, slight smile, mouth is closeed, looking at MC
            with dissolve

            sa "*Giggles*"

            scene v16s31_2b
            with dissolve

            u "I know it's frustrating, I get it. But this is Cameron's sister. By helping Sam, we're helping one of the Apes."

            scene v16s31_2d
            with dissolve

            gr "You sound like you've been watching too many daytime talk shows, [name]."

            scene v16s31_2b
            with dissolve

            u "(What...?)"

            scene v16s31_2e # FPP. Show just Grayson has closed the fridge, slightly angry expression, mouth is open, looking at MC
            with dissolve

            gr "I don't care what it looks like or how it makes people feel. This is the Apes Fraternity house, I am the president of the Apes, and I want her out of here!"

            if v14_SamanthaDrugs: # -if SamanthaDrugs
                scene v16s31_3c
                with dissolve

                sa "*Whispers* I think he's angry because he wants to bang me. That's what this is."

                scene v16s31_2f # FPP. Show just Grayson has closed the fridge, slightly angry expression, mouth is open, looking at Samantha
                with dissolve

                gr "I wouldn't even touch you with someone else's dick!"

            else: # -if SamanthaSober
                scene v16s31_3c
                with dissolve

                sa "Okay, message received. Thanks for putting it so delicately! Dickhead..."

                scene v16s31_2g # FPP. Show just Grayson has closed the fridge, slight smile, mouth is open, looking at Samantha
                with dissolve

                gr "Haha, great! It's finally sinking into that ugly little head of yours!"

    scene v16s31_2h # FPP. Grayson throws up his hands with a frustrated expression, mouth is open, looking at Mc
    with dissolve

    gr "Now, I'm done with this conversation."

    scene v16s31_4 # TPP. Grayson starts walking out the room, Grayson looks at Mc as he walks by no expression mouth is open, MC looks at Grayson no expression mouth is closed, Samantha is still sitting on the stool looking at Grayson no expression, mouth is closed
    with dissolve

    gr "I'm going to go buy some candles in case this power outage happens again."

    scene v16s31_4a # TPP. Grayson walks further away from Mc and Sam no expression mouth is closed, Mc is looking at Samantha slight smile mouth is closed, Samantha has a hand to the side of her mouth trying to sound louder slight smile mouth is open
    with dissolve

    sa "You know, a lot of kids grow out of their fear of the dark at a young age!"

    scene v16s31_4b # TPP. Grayson doesn't turn when he replies, just keeps walking, flips sam off, Mc is looking at Grayson slight smile mouth is closed, Samantha is looking at Grayson slight smile mouth is closed
    with dissolve

    gr "Fuck off, Sam!"

    scene v16s31_3f # FPP. Show Just Samantha sitting on a stool, slight smile, mouth is open, looking at MC
    with dissolve

    sa "He's such an asshole sometimes."

    sa "Actually, no... He's an asshole all the time."

    scene v16s31_3d
    with dissolve

    u "Haha, yeah. He definitely lets you know when he's pissed off."

    u "...And he is pissed off a LOT."

    scene v16s31_3f
    with dissolve

    sa "Ha, a true Ape. Always angry and ready for a fight."

    scene v16s31_3g # FPP. Show Just Samantha sitting on a stool, Samantha yawns and stretches, slight smile, mouth is open, looking at MC
    with dissolve

    sa "*Sighs* Power outages are so boring! There's nothing to do."

    scene v16s31_3d
    with dissolve

    u "Maybe do some studying?"

    scene v16s31_3f
    with dissolve

    sa "Haha! Good one you weirdo."

    sa "I'm gonna head out and see what people are up to. Catch you later, [name]."

    scene v16s31_3d
    with dissolve

    u "Yeah, okay. Later, Sam."

    scene v16s31_5 # TPP. Show just Samantha gets up to walk out and Mc standing a few feet away from her, both looking at each other slight smiles, mouths are closed
    with dissolve

    pause 0.75

    if v14_SamanthaDrugs: # TODO: Variable # -if SamanthaDrugs and MC had sex
        scene v16s31_5a # TPP. As Sam passes MC, she stops for a moment and leans in towards Mc's ear, both slight smiles, Samantha's mouth is open, Mc's mouth is closed
        with dissolve

        sa "Oh, and my memory of us fucking... it's kinda fading. So, let's refresh that soon."

        scene v16s31_5b # TPP. Close up shot from the head down to MC's dick, Samantha rubs her hand over MC's dick, Samantha bites her lip, MC is slightly shocked but also pleasantly surprised by the action
        with dissolve

        pause 0.75

        scene v16s31_5c # TPP. Sam walks out the room with a sly smile. MC watches her go
        with dissolve

        u "(Deal...)"

    scene v16s31_6 # TPP. Close up shot of MC holding his chin and appearing to be in thought, slight smile, mouth is closed.
    with dissolve

    u "(I guess I'll go to my room...)"

    jump v16s32