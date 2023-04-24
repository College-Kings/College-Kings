# SCENE 30: Amber and the Canals 
# Locations: The Canal, Hotel Lobby, Hospital Exterior
# Characters: MC (Outfit: 9), AMBER (Outfit: 1), SAMANTHA (Outfit: 1), LAUREN (Outfit: 3)
# Time: Night

label v13s30:
    scene v13s30_1 # TPP. Show MC and Amber down in the canals, Both slight smile, MC Mouth open.
    with dissolve

    u "Wait a minute, are these not the canals you were talking about?"

    play music "music/v13/Track Scene 30_1.mp3" fadein 2

    scene v13s30_2 # FPP. MC looking at Amber, Amber looking at MC, Amber slight smile, mouth open. 
    with dissolve

    am "Oh shit, they are."

    am "And we got some weed!!! You know what that means..."

    scene v13s30_2a # FPP. Same as v13s30_2, Amber slight smile, mouth closed.
    with dissolve

    u "What?"

    scene v13s30_2
    with dissolve

    am "Time to see if the water dances."

    if v13_invite_samantha: 
        scene v13s30_3 # FPP. MC looking at Samantha, Samantha looking at Amber, Samantha worried smile, mouth open
        with dissolve
    
        sa "Oh umm, I'm cool with hanging out a bit but, I think if you're gonna smoke I should go."

        scene v13s30_2j # FPP. MC Looking at Amber, Amber looking at Samantha, slight smile, mouth open.
        with dissolve

        am "You don't want some?"

        scene v13s30_3
        with dissolve

        sa "I'm trying to cut back."

        scene v13s30_2j
        with dissolve

        am "Your call."

        scene v13s30_3a # FPP. Same as v13s30_3, Samantha looking at MC, Samantha slight smile, mouth open
        with dissolve

        sa "Yeah. Thanks anyway. Later guys."

        scene v13s30_3b # FPP. Same as v13s30_3a, Samantha slight smile, mouth closed
        with dissolve

        u "Bye Sam."

        scene v13s30_3a
        with dissolve

        sa "See ya, have fun! And thanks for letting me come."

        scene v13s30_4 # TPP. Samantha hugging MC, Samantha slight smile, mouth closed
        with dissolve

        pause 0.75

        scene v13s30_3c # FPP. Same as v13s30_3b, Samantha walking away from MC. 
        with dissolve

        pause 0.75

        scene v13s30_2
        with dissolve

        am "Somebody's got a thing for you."

        scene v13s30_2a
        with dissolve

        u "I don't know about all that. *Chuckles*"

        scene v13s30_2
        with dissolve

        am "Well, she didn't give me a hug... *Chuckles*"

        scene v13s30_2a
        with dissolve

        u "*Chuckles* Fair enough."

    scene v13s30_2a
    with dissolve

    u "If the water's gonna dance, does that mean we're going to be dizzy?"

    if not v11_smoke_amber_amsterdam: #placeholder
        scene v13s30_2
        with dissolve

        am "You said you didn't wanna come with me back when we were in London, but you are here now..."

        am "So, if you get fucked up I'll try to feel bad. *Chuckles*"

    else:
        scene v13s30_2
        with dissolve

        am "You said you wanted to come back when we were in London. So if you get fucked up, that's on you. *Chuckles*"

    scene v13s30_2a
    with dissolve

    u "I appreciate that. *Chuckles*"

    scene v13s30_2
    with dissolve

    am "You know what?"

    scene v13s30_2b # FPP. Same as v13s30_2a, Amber pulling out her phone, slight smile, mouth closed.
    with dissolve

    pause 0.75

    play sound "sounds/rejectcall.mp3"
    scene v13s30_2c # FPP. Same as v13s30_2b, Amber with phone to her ear, slight smile, mouth open.
    with dissolve

    am "Hey, what are you doing right now?"

    scene v13s30_2k # FPP. Same as v13s30_2c, Amber mouth closed, slight smile
    with dissolve

    pause 0.75

    scene v13s30_2c
    with dissolve

    am "Alright, come by the canals?"

    scene v13s30_2k
    with dissolve

    pause 0.75

    scene v13s30_2c
    with dissolve

    am "Yes, right now."

    scene v13s30_2k
    with dissolve

    pause 0.75

    scene v13s30_2c
    with dissolve

    am "Haha, that's my girl. Bye!"

    scene v13s30_2d # FPP. Same as v13s30_2a, Amber putting her phone away, slight smile, mouth closed.
    with dissolve

    u "Who did you invite?"

    scene v13s30_2
    with dissolve

    am "You'll see when she gets here."

    scene v13s30_2a
    with dissolve

    u "Always with the games. Tsk tsk..."

    scene v13s30_2
    with dissolve

    am "You know it... *Chuckles* Let's get started."

    scene v13s30_2a
    with dissolve

    u "Better not have grabbed that HardOn stuff..."

    scene v13s30_2
    with dissolve

    am "Guess you'll find out, haha. Are you gonna smoke?"

    menu:
        "I'm good":
            scene v13s30_2a
            with dissolve

            u "I'm good, not trying to get fucked up, fucked up. *Laughs*"

            scene v13s30_2e # FPP. Same as v13s30_2, Amber confused smile, mouth open
            with dissolve

            am "Wack ass."

            scene v13s30_2a
            with dissolve

            u "*Laughs*"

        "Why not!?":
            $ v13_smoke_weed = True

            scene v13s30_2a
            with dissolve
            
            u "I've never passed up on an opportunity to have a good time."

            scene v13s30_2
            with dissolve

            am "That was a wack way to put it, but let's roll up. *Laughs*"

    scene v13s30_2f # FPP. Same as v13s30_2, MC Looking at Amber, Amber looking away from MC, Amber slight smile, mouth open.
    with dissolve

    am "Speaking of wack, look who it is!"

    scene v13s30_5 # TPP. Lauren walking up to MC and Amber, Slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v13s30_5a # TPP. Same as v13s30_5, Lauren standing with MC and Amber, Slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v13s30_6 # FPP. MC looking at Lauren, Lauren looking at Amber, Lauren slight smile, mouth open.
    with dissolve

    la "Uhh rude... Why'd you ask me to come?"

    scene v13s30_2g # FPP. Same as v13s30_2f, Amber looking at Lauren, Amber Slight smile, mouth open.
    with dissolve

    am "*Chuckles* Come roll up with us."

    if v11_lauren_caught_aubrey: 
        scene v13s30_2a
        with dissolve

        u "*Whisper* Amber, really?"

        scene v13s30_2
        with dissolve

        am "What? Weed solves everything... She won't be mad at you after a good session on the Cheex. *Chuckles*"

        scene v13s30_6a # FPP. Same as v13s30_6, Lauren looking back at MC, slight frown, mouth open
        with dissolve

        la "*Sighs* I've been thinking about this anyway, and I'm not gonna walk around all the time with an angry face just because of you."

        scene v13s30_6e # FPP. Same as v13s30_6a, Lauren different pose
        with dissolve

        la "It isn't doing anything but keeping me in a bad mood so, we can be civil."

        scene v13s30_6a
        with dissolve

        la "You obviously aren't ready for commitment and taught me that some people are still trying to do as they please, so I will too."

        scene v13s30_6b # FPP. Same as v13s30_6a, Lauren slight frown, mouth closed
        with dissolve

        u "Lauren, I'm sorry. For real."

        scene v13s30_6a
        with dissolve

        la "No need to apologize anymore, it's done. Forgive and forget."

        scene v13s30_2
        with dissolve

        am "See? No hard feelings. Time to light up."

        scene v13s30_7 # TPP. MC, Amber, and Lauren starting to sit down in the Canal, all slight smile, mouths closed
        with dissolve

        pause 0.75

        scene v13s30_7a # TPP. Same as v13s30_7 MC, Amber and Lauren sitting down in the Canal, all slight smile, all mouths closed
        with dissolve

        pause 0.75
   
    elif CharacterService.is_girlfriend(lauren):
        scene v13s30_6c # FPP. Same as v13s30_6a, Lauren slight smile, mouth open.
        with dissolve

        la "[name], I didn't know you'd be here..."

        scene v13s30_6d # FPP. Same as v13s30_6c, Lauren slight smile, mouth closed.
        with dissolve

        u "Amber dragged me here."

        scene v13s30_2
        with dissolve

        am "Because you guys are both uptight and need to relax."

        scene v13s30_7 
        with dissolve

        pause 0.75

        scene v13s30_7b # TPP. Same as v13s30_7a, all slight smile, Lauren and MC mouth closed, Amber mouth open.
        with dissolve

        am "Keep the lovey dovey shit to a minimum."

        scene v13s30_8 # FPP. MC and Lauren sitting down. Mc looking at Lauren, Lauren looking at MC, Lauren slight smile, mouth open.
        with dissolve

        la "*Chuckles*"

        scene v13s30_9 # TPP. MC and Lauren sitting down, Lauren grabbing MC's chin gently, both slight smile, mouths closed
        with dissolve

        pause 0.75

        play sound "sounds/kiss.mp3"
        scene v13s30_9a # TPP. Same as v13s30_9. Lauren kissing MC while grabbing his chin.
        with dissolve

        pause 0.75

        scene v13s30_9
        with dissolve

        pause 0.75

        scene v13s30_9a 
        with dissolve

        pause 0.75

        scene v13s30_8
        with dissolve

        la "That's the minimum."

        scene v13s30_10 # FPP. MC, Lauren, and Amber sitting down, MC looking at Amber. Amber looking at Lauren, Amber slight smile, mouth open.
        with dissolve

        am "I hate you. *Laughs*"

        scene v13s30_8
        with dissolve

        la "*Laughs*"

    else:
        scene v13s30_6c
        with dissolve

        la "[name], I didn't know you'd be here."

        scene v13s30_6d
        with dissolve

        u "Amber dragged me here."

        scene v13s30_2
        with dissolve

        am "Because you guys are both uptight and need to relax."

        scene v13s30_7 
        with dissolve

        pause 0.75

        scene v13s30_7a
        with dissolve

        pause 0.75

        scene v13s30_8
        with dissolve

        la "Haha, what?"

    scene v13s30_8a # FPP. Same as v13s30_8, Lauren looking at Amber, slight smile, mouth open.
    with dissolve

    la "Amber, you know I've never smoked before."

    scene v13s30_10
    with dissolve

    am "There's a first time for everything."

    scene v13s30_8a
    with dissolve

    la "Not everything. I'm not so sure about smoking."

    menu:
        "It's relaxing":
            scene v13s30_8e # FPP. Same as v13s30_8, Lauren slight smile, mouth closed
            with dissolve

            u "It is relaxing, always helps me blow off a bit of steam."

        "It's up to you":
            $ v13_lauren_smoke = True
            
            scene v13s30_8e
            with dissolve

            u "It's up to you, some people love it and others can do without."

    scene v13s30_10
    with dissolve

    am "Just take a few hits, you can take your time with it."

    scene v13s30_8b # FPP. Same as v13s30_8a. Lauren worried smile, mouth open.
    with dissolve

    la "Is it going to make me feel sick?"

    scene v13s30_10
    with dissolve

    am "As long as you don't do too much you'll be fine."

    if v13_lauren_smoke or (reputation() == Reputations.LOYAL and not "v11_aubrey" in sceneList):
        if not v13_lauren_smoke:
            $ v13_lauren_smoke = True
            call screen reputation_popup

        scene v13s30_8a
        with dissolve

        la "You know what? Fuck it. We're in Amsterdam! I'll do it."

        scene v13s30_10
        with dissolve

        am "Oh wow, was that a cuss word... Someone's feeling feisty tonight! Just risk it all, huh?"

        scene v13s30_8a
        with dissolve

        la "I'm just trying to have fun. We don't have many days left before we're back on campus."

        scene v13s30_10
        with dissolve

        am "Hell yeah. That's the spirit."

        am "Oh yeah, that's a damn good strain right there."

        scene v13s30_11 # TPP. Amber and Lauren sitting down with MC, Amber starting to pass the blunt to Lauren, Lauren starting to reach for the blunt, both slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v13s30_11a # TPP. Same as v13s30_11, Lauren taking the blunt from Amber, both slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v13s30_8c # FPP. Same as v13s30_8, MC looking at Lauren, Lauren looking away as she takes a hit from the blunt.
        with dissolve

        pause 0.75

        scene v13s30_8d # FPP. Same as v13s30_8c, blunt away from Lauren's face, Lauren's hand at her mouth as she coughs.
        with dissolve

        la "*Cough* *Cough* *Cough* *Cough*"

        scene v13s30_10
        with dissolve

        am "Haha, definitely a newbie."

        scene v13s30_10a # FPP. Same as v13s30_10, Amber slight smile, mouth closed.
        with dissolve

        u "*Chuckles*"

        scene v13s30_8
        with dissolve

        la "*Coughs* Don't laugh just because I'm not a pothead like you guys."

        if not v13_smoke_weed:
            scene v13s30_8e
            with dissolve

            u "I'm not smoking at all, so..."

        else:
            scene v13s30_8e
            with dissolve

            u "I don't smoke that much, just have a few times."

        scene v13s30_10
        with dissolve

        am "Don't take such a big hit."

        if v13_smoke_weed:
            scene v13s30_12 # TPP. MC, Amber, and Lauren sitting in canal, show Lauren starting to hand the blunt to MC, Lauren nervous smile, mouth closed, MC slight smile, mouth closed.
            with dissolve

            pause 0.75

            scene v13s30_12a # TPP. Same as v13s30_12, MC taking blunt from Lauren.
            with dissolve

            pause 0.75

            scene v13s30_12b # TPP. Same as v13s30_12a, MC taking a hit from the blunt
            with dissolve

            pause 0.75 

            scene v13s30_12c # TPP. Same as v13s30_12b, MC moved blunt away from face
            with dissolve

            pause 0.75

            scene v13s30_12d # TPP. Same as v13s30_12c, MC starting to pass blunt to Amber, Amber reaching for the blunt, Both slight smile, mouths closed.
            with dissolve

            pause 0.75

            scene v13s30_12e # TPP. Same as v13s30_12d, Amber taking blunt from MC.
            with dissolve

            pause 0.75
        
        scene v13s30_8f # FPP. Same as v13s30_8, Lauren worried expression, Mouth open.
        with dissolve

        la "I can definitely feel something..."

        scene v13s30_10
        with dissolve

        am "It's a little quick for a reaction, you sure you're not just faking it? *Chuckles*"

        scene v13s30_8f
        with dissolve

        la "I'm definitely... Not faking."

        scene v13s30_8g # FPP. Same as v13s30_8f, Lauren looking at MC, Lauren worried expression, mouth closed
        with dissolve

        u "It was one hit, though."

        scene v13s30_8f
        with dissolve

        la "Guys, I'm not playing. It... It looks like the water is... Dancing?"

        scene v13s30_10
        with dissolve

        am "Ayeeee, it's working! *Laughs*"

        scene v13s30_8g
        with dissolve

        u "Amber was told that if you get high at the canals, it looks like the water is dancing. So, you're definitely high. *Laughs*"

        scene v13s30_8f
        with dissolve

        la "I'm a little more than high..."

        scene v13s30_13 # TPP. Show Lauren getting up, worried expression, mouth closed.
        with dissolve

        pause 0.75 

        scene v13s30_13a # TPP. Same as v13s30_13, Show Lauren standing up.
        with dissolve

        pause 0.75 

        scene v13s30_13b # TPP. Same as v13s30_13a, Show MC getting up, MC worried expression, mouth closed.
        with dissolve

        pause 0.75

        scene v13s30_13c # TPP. Same as v13s30_13b, MC standing up, MC worried expression, Mouth open.
        with dissolve

        u "Hey, uh, you should sit down."

        scene v13s30_14 # FPP. MC looking at Lauren, Lauren looking at MC, Lauren nervous expression, mouth open.
        with dissolve

        la "I'm fine."

        scene v13s30_15 # TPP. Show Lauren starting to lose balance.
        with dissolve

        pause 0.75

        scene v13s30_15a # TPP. Same as v13s30_15, Show MC catching Lauren in his arms, MC worried expression, Mouth open
        with dissolve

        u "She's shaking, Amber..."

        stop music fadeout 3
        play music "music/v13/Track Scene 30_2.mp3" fadein 2

        scene v13s30_15b # TPP. Same as v13s30_15a, Show MC looking down towards where Amber is sitting, MC worried expression, mouth closed, amber worried expression, Mouth open.
        with dissolve

        am "Ahh fuck!"

        scene v13s30_16 # TPP. Show Amber getting up off the ground, Amber worried expression, mouth closed.
        with dissolve

        pause 0.5

        scene v13s30_16a # TPP. Show Amber standing, Amber worried expression, mouth open.
        with dissolve

        am "Let's get to the hospital now. Can you carry her? It's not too far?"

        scene v13s30_17 # TPP. Show MC starting to pick up Lauren, MC worried expression, mouth open.
        with dissolve

        u "I got her."

        scene v13s30_17a # TPP. Same as v13s30_17, MC princess/bridal carrying Lauren, MC worried expression, mouth closed, Lauren unconscious expression, mouth open. 
        with dissolve

        la "*Mumble*"

        scene v13s30_18 # FPP. MC looking at Lauren passed out in his arms, Lauren unconscious expression, mouth closed.
        with dissolve

        u "Just relax Lauren, I got you."

        scene v13s30_19 # TPP. MC walking with Amber out of the canal while holding Lauren
        with dissolve

        pause 0.25

        scene v13s30_19a # TPP. Same as v13s30_19. All further away from the camera.
        with dissolve

        pause 1.00

        scene v13s30_20 # TPP. MC carrying Lauren while outside of the hospital with Amber next to him.
        with Fade(1,1,1)

        stop music fadeout 3

        jump v13s31 

    else:
        if not "v11_aubrey" in sceneList:
            call screen reputation_popup(required_reputation="loyal")
    
        scene v13s30_21 # FPP. Amber the only one sitting. MC looking at Lauren, Lauren looking at Amber where she is sitting, Lauren slight frown, mouth open, Amber slight frown, mouth closed.
        with dissolve

        la "Maybe another time... I'm not feeling very risky tonight."

        scene v13s30_21a # FPP. Same as v13s30_21, Lauren slight frown mouth closed, Amber slight frown, mouth open.
        with dissolve

        am "Don't kill the vibe, please? I wanted to do this with you."

        scene v13s30_21
        with dissolve

        la "*Sighs* Please don't make me feel bad. Maybe another time, okay?"

        scene v13s30_21a
        with dissolve

        am "*Sighs* Fine."

        scene v13s30_22 # TPP. Show Amber starting to stand up
        with dissolve

        pause 0.75

        scene v13s30_22a # TPP. Show Amber standing, slight frown, mouth open.
        with dissolve

        am "Let's just head on back."

        scene v13s30_2h # FPP. Same as v13s30_2. Amber slight frown, mouth closed.
        with dissolve

        u "You sure?"

        scene v13s30_2i # FPP. Same as v13s30_2h. Amber slight frown, mouth open.
        with dissolve

        am "Yeah, let's go."

        scene v13s30_2h
        with dissolve

        la "I'm sorry, Amber."

        scene v13s30_2g
        with dissolve

        am "Oh, don't worry. You'll make it up to me. *Chuckles*"

        scene v13s30_6
        with dissolve

        la "Haha, if you say so."

        scene v13s30_23 # TPP. Show MC, Lauren, and Amber walking out of canal.
        with dissolve

        pause 0.75

        scene v13s30_24 # TPP. Show MC, Lauren, and Amber inside hotel lobby
        with Fade(1,1,1)

        pause 0.75

        stop music fadeout 3

        jump v13s32