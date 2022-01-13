# SCENE 49: Tom confrontation in parking lot
# Locations: San Vallejo College parking lot.
# Characters: MC (Outfit: 1), RILEY (Outfit: 2), TOM (Outfit: 1)
# Time: Night

label v15s49:
    play music "music/v15/Track Scene 49.mp3" fadein 2

    scene v15s49_1 # TPP. MC looking out the window of the cab, its night time and raining outside, MC slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s49_2 # TPP. MC's head turned to face the cab driver, MC slight smile, mouth open.
    with dissolve

    u "Here's good. Thanks."

    scene v15s49_3 # TPP. Show MC getting out of the cab, the rain hitting his clothes, MC slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s49_4 # TPP. MC starting to walk towards his Frat house, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s49_4a # TPP. MC concerned, mouth closed
    with dissolve

    ri "What the fuck? Leave me alone!"

    u "(Huh? Is that Riley?)"

    scene v15s49_5 # FPP. MC turned to look at the parking lot, rain smashing down on the cars, Riley is facing Tom from the first fight, Tom is a little more buff now, Tom angry, mouth closed, Riley scared, mouth closed.
    with dissolve

    u "(What's going on? Is that- Tom?)"

    if wintom:
        u "(Haven't seen him since I kicked his ass.) *Scoffs*"
        
    elif fighttom:
        u "(Haven't seen him since he knocked me on my ass.)"

        u "(That's a memory I was hoping to forget...)"

    pause 0.75

    scene v15s49_6 # TPP. Show MC walking over to Tom and Riley, MC angry, mouth closed.
    with dissolve

    pause 0.75

    scene v15s49_7 # TPP. Close up of Tom, Tom looking at Riley, Tom angry, mouth open.
    with dissolve

    if v13_charli_exposed:
        tom "Listen here, you little bitch... I know you had something to do with why Charli got expelled!"
        
    else:
        tom "Listen here, you little bitch... I know you had something to do with Charli!"

    scene v15s49_8 # TPP. Close up of Riley, Riley looking at Tom, Riley confused, mouth open.
    with dissolve

    ri "W-what?"

    scene v15s49_7
    with dissolve

    tom "Charli was the reason I'm still in school, you fucking rat!"

    if v13_charli_exposed:
        tom "Now that he's gone, I have to find someone else to do all of my assignments."
    
    else:
        tom "But he's chickened out now, and I have to find someone else to do all of my assignments."

    scene v15s49_8
    with dissolve

    ri "That has nothing to do with me, you prick! It was only a matter of time before he got caught."

    scene v15s49_7
    with dissolve

    tom "Hah! Shut the hell up and listen to me."

    tom "Someone has to take his place. And that person is going to be you from now on, do you understand?"

    scene v15s49_8
    with dissolve

    ri "No, It's not... I'm not doing that-"

    scene v15s49_7
    with dissolve

    tom "You don't get to decide!"

    scene v15s49_9 # TPP. Show Tom grabbing Riley's arm, Riley angry, mouth open, Tom angry, mouth closed.
    with dissolve

    ri "Get... off of me! *Grunts*"

    scene v15s49_9a # TPP. Riley angry, mouth closed, Tom angry, mouth open.
    with dissolve

    tom "You'll do as you're told, or I'll make your life a living hell."

    scene v15s49_9
    with dissolve

    ri "*Grunts* Let... Go!"

    scene v15s49_9a
    with dissolve

    tom "Do you understand me?!"

    scene v15s49_10 # TPP. Tom shoving pushing Riley to the ground, Tom angry, mouth closed.
    with dissolve

    pause 0.75

    play sound "sounds/thud.mp3"
    scene v15s49_11 # TPP. Show Riley hitting the ground, angry, mouth closed.
    with dissolve

    menu:
        "Attack Tom":
            $ add_point(KCT.BRO)
            play sound "sounds/hs.mp3"

            scene v15s49_12 # TPP. Show MC charging into Tom and pushing him further from Riley.
            with dissolve

            pause 0.75

            scene v15s49_13 # FPP. MC standing between Tom and Riley, MC looking at Tom, Tom looking at MC, Tom angry, mouth closed.
            with dissolve

            u "What the fuck is your problem?!"

        "Check on Riley":
            $ add_point(KCT.BOYFRIEND)

            if riley.relationship >= Relationship.FWB:
                scene v15s49_14 # FPP. Show MC on his knee checking on Riley, MC looking at Riley, Riley looking at MC, Riley angry, mouth closed.
                with dissolve

                u "What the hell is going on?! Are you okay?"

                scene v15s49_14a # FPP. MC looking at Riley, Riley looking at MC, Riley upset, mouth open.
                with dissolve

                ri "[name]... *Sighs* Thank God you're here. *Sniffles*"
            else:
                scene v15s49_14
                with dissolve

                u "Riley! What the fuck- Are you okay?"

                scene v15s49_14a
                with dissolve

                ri "[name]? I'm... *Grunts* I'm fine."

                scene v15s49_15 # TPP. Show MC helping up Riley, both angry, mouth closed.
                with dissolve

                pause 0.75

                scene v15s49_16 # FPP. Both standing up now, MC looking at Riley, Riley looking at MC, Riley angry, mouth open.
                with dissolve

                ri "He just started screaming at me from across the street."

    scene v15s49_13a # FPP. MC standing between Tom and Riley, MC looking at Tom, Tom looking at MC, Tom angry, mouth open
    with dissolve

    tom "Oh, look! [name] shows up just when I'm looking to make someone bleed."

    scene v15s49_13
    with dissolve

    menu:
        "Stay calm":
            $ add_point(KCT.BRO)
            u "You know better than this, Tom. This is wrong."

            scene v15s49_13a
            with dissolve

            tom "Does it look like I give it fuck?! How about I drop your weak ass too?"

        "Get angry":
            $ add_point(KCT.TROUBLEMAKER)

            u "BACK THE FUCK OFF!"

            scene v15s49_13a
            with dissolve

            tom "MAKE ME, MOTHERFUCKER!"

    if wintom:
        scene v15s49_13
        with dissolve

        u "I'll gladly put your ass on the floor again, man."

        scene v15s49_13a
        with dissolve

        tom "*Scoffs* That was a long time ago, pal!"

        tom "I've been training almost every day since then."

    elif fighttom:
        scene v15s49_13a
        with dissolve

        tom "You really enjoy getting your ass handed to you, huh?"

        scene v15s49_13
        with dissolve

        u "Ha, right."

        scene v15s49_13a
        with dissolve

        tom "The only difference this time is that I train twice a week, so hopefully you don't wake up!"

    scene v15s49_13b # FPP. Tom walking closer to MC, Tom looking at Mc, MC looking at Tom, Tom angry, mouth closed.
    with dissolve

    u "Why are you doing this, Tom? Why Riley? Why me?"

    scene v15s49_13c # TPP. Tom standing closer to MC now, Tom looking at MC, MC looking at Tom, Tom angry, mouth open.
    with dissolve

    tom "Charli told me you two were behind his expulsion."

    scene v15s49_13d # TPP. Tom standning closer to MC, MC looking at Tom, Tom looking at MC, Tom angry, mouth closed.
    with dissolve

    u "Dude, like Riley said, it was only a matter of time before he got caught. There's no one to blame but himself."

    u "Why don't you go home now, huh? I think you've hurt enough people for today."

    scene v15s49_13c
    with dissolve

    tom "I'm not going anywhere, you little shithead. I'm not finished yet."

    scene v15s49_19 # TPP. Show Riley holding her arm as she is sitting against the hood of a car a little bit away from Tom and MC, Riley upset, mouth closed.
    with dissolve

    pause 0.75

    scene v15s49_13d
    with dissolve

    menu:
        "Antagonize Tom":
            $ add_point(KCT.TROUBLEMAKER)
            
            u "The more you talk, the bigger your forehead gets. Or should we just go ahead and start saying fivehead?"

            scene v15s49_13c
            with dissolve

            tom "Ha. Keep talking, fresh meat."

        "Try to calm Tom":
            $ add_point(KCT.BOYFRIEND)
            
            scene v15s49_13d
            #with dissolve

            u "We don't have to do this, you know. We can just forget about it and go home."

            scene v15s49_13c
            with dissolve

            tom "You won't be going home tonight, [name]. You'll be going to the nearest emergency room."

    scene v15s49_16a # TPP. Show Riley holding her arm as she is sitting against the hood of a car a little bit away from Tom and MC, Riley upset, mouth open.
    with dissolve

    ri "[name]."

    ri "We can walk away from this without a fight."

    menu:
        "Nobody's walking away":
            $ add_point(KCT.TROUBLEMAKER)

            scene v15s49_17 # TPP. Close up of MC's face looking at Tom, MC angry, mouth open.
            with dissolve

            u "Nobody's walking away, Riley."

            u "He's going to learn today."

        "I wish we could":
            $ add_point(KCT.BRO)
            u "I wish we could walk away, Riley."

            scene v15s49_17
            with dissolve

            u "But it looks like I have no choice."

    scene v15s49_13e # FPP. Show Tom in a fighting stance looking at MC, MC looking at Tom, Tom angry, mouth closed.
    with dissolve

    tom "You're about to die."

    scene v15s49_18 # TPP. A nice cinematic kind of shot of MC's fist clenched and the rain dripping off of it.
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump end15

label end15:
    if not renpy.loadable("v16/scene1.rpy"):
        scene savenow #nothing needed
        with Fade (1,0,1)
        " "

    if renpy.loadable("v16/scene1.rpy"):
        jump v16_start
    else:
        play music "music/vocal.mp3"
    
        call screen end_screen