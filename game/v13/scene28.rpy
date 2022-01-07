# SCENE 28: Amber and MC Bus Stop 
# Locations: Bus stop
# Characters: AMBER (Outfit: 1), MC (Outfit: 9), SAMANTHA (Outfit: 1)
# Time: Evening

label v13s28:
    scene v13s28_1 # TPP. Show MC walking towards Amber at the bus station, slight smile, mouth closed
    with dissolve

    pause 0.75

    play music "music/v13/Track Scene 28.mp3" fadein 2

    scene v13s28_1a # TPP. Show MC standing at the bus station with Amber, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v13s28_2 # FPP. MC looking at Amber. Amber looking at MC, Amber slight smile, mouth open.
    with dissolve

    am "Jeez... Took you long enough. Did you have to do your nails real quick? *Laughs*"

    scene v13s28_2a # FPP. Same as v13s28_2. Amber slight smile, mouth closed.
    with dissolve

    u "Ha ha, funny. I wasn't that motivated to be here actually, since I have no idea where we're going."

    scene v13s28_2
    with dissolve

    am "I got us some tickets for a little bus tour thing..."

    scene v13s28_2a
    with dissolve

    u "A bus tour? Amber..."

    scene v13s28_2
    with dissolve

    am "A marijuana bus tour thing."

    scene v13s28_2a
    with dissolve

    u "You're piquing my interest..."

    scene v13s28_2b # FPP. Same as v13s28_2a, Amber different pose, slight smile, mouth open.
    with dissolve

    am "*Laughs* Interested or not, I already bought your ticket, so you're going."

    scene v13s28_2a
    with dissolve

    u "Damn, so it's like that?"

    scene v13s28_2
    with dissolve

    am "It's always been like that."

    scene v13s28_2a
    with dissolve

    u "What if I just don't wanna go?"

    scene v13s28_2b
    with dissolve

    am "Then I suggest you try to start wanting to go."

    scene v13s28_2a
    with dissolve

    u "Well, I already planned something else so... I can't."

    scene v13s28_2
    with dissolve

    am "Then you owe me some money."

    scene v13s28_2a
    with dissolve

    u "*Laughs* How do I owe you money? I didn't tell you to-"

    scene v13s28_3 # TPP. Amber grabbing MC's arm, Amber slight smile, mouth closed, MC confused expression, mouth closed.
    with dissolve

    pause 0.75

    scene v13s28_3a # TPP. Same as v13s28_3, Show Amber behind MC pulling his arm behind his back. Amber slight smile, mouth open, MC pain expression, mouth closed.
    with dissolve

    am "Money or tour, you pick."

    scene v13s28_3b # TPP. Same as v13s28_3a, MC pain expression, mouth open.
    with dissolve

    u "Ow, fuck! Okay... Fine, I'll go."

    scene v13s28_3c # TPP. Same as v13s28_3a. Amber letting go of MC's arm.
    with dissolve

    am "Wonderful."

    scene v13s28_2a
    with dissolve

    u "Damn, you're strong."

    scene v13s28_2
    with dissolve

    am "I know. *Chuckles*"

    scene v13s28_4 #TPP. Show MC and Amber starting to sit at bus stop, both slight smile, mouth closed 
    with dissolve

    pause 0.75

    scene v13s28_4a #TPP. Same as v13s28_4, Show MC and Amber sitting at bus stop.
    with dissolve

    pause 0.75

    if v11_invite_sam_europe: 
        scene v13s28_5 # FPP. Show Samantha walking towards bus stop
        with fade

        pause 0.75

        scene v13s28_5a # FPP. Same as v13s28_5. Show Samantha stopping and standing infront of MC and Amber, Slight smile mouth open.
        with dissolve

        sa "Hey guys! What are you up to?"

        scene v13s28_6 # FPP. MC looking at Amber while they sit down, Amber looking at Samantha, Amber slight smile, mouth open.
        with dissolve

        am "Going on a little weed tour. *Chuckles*"

        scene v13s28_7 # FPP. MC looking at Samantha, Samantha looking at Amber, Samantha slight smile, mouth open.
        with dissolve

        sa "Oooh! Can I come?"

        scene v13s28_6
        with dissolve

        am "You got money for a ticket? *Chuckles*"

        scene v13s28_7
        with dissolve

        sa "I don't have a dime on me..."

        scene v13s28_6
        with dissolve

        am "Well, there's your answer."

        scene v13s28_7a # Same as v13s28_7. Samantha different pose.
        with dissolve

        sa "Can't you guys spot me? Just this one time, Amber?"

        scene v13s28_6a # Same as v13s28_6. Amber different pose.
        with dissolve

        am "Not gonna happen, I'm officially broke. He may though."

        menu:
            "Not a good idea, Sam":
                $ add_point(KCT.BRO)
                scene v13s28_7b # FPP. Same as v13s28_7, Samantha looking at MC, Samantha slight smile, mouth closed.
                with dissolve

                u "I don't think you going on a marijuana tour is a good idea, Sam. You know, because of your... history."

                scene v13s28_7c # FPP. Same as v13s28_7b, Samantha angry expression, mouth open.
                with dissolve

                sa "I'm not some fucking fiend, [name]. And either way, I can do whatever the hell I want. It's shitty remarks like that which makes me wanna fuck around with drugs in the first place."

                scene v13s28_7d # FPP. Same as v13s28_7c, Samantha angry expression, mouth closed.
                with dissolve

                u "Sam, I'm just trying to do what's best for you."

                scene v13s28_7c
                with dissolve

                sa "Nah, you're trying to control what I do. Just like my obsessive brother. Fuck this and fuck you."

                scene v13s28_8 # TPP. Show Samantha storming away, angry, mouth closed
                with dissolve
               
                pause 0.75

                scene v13s28_6b # FPP. Same as v13s28_6, Amber looking at MC, Amber slight smile, mouth open.
                with dissolve

                am "Yikes. That was fun. *chuckles*"

                scene v13s28_6c # FPP. Same as v13s28_6, Amber slight smile, mouth closed.
                with dissolve

                u "*Sighs*"

            "Fine, I'll pay for you":
                $ v13_invite_samantha = True

                scene v13s28_7b
                with dissolve

                u "I mean it might be a little triggering but... Whatever, yeah. I'll pay for it."

                scene v13s28_7e # FPP. Same as v13s28_7b, Samantha slight smile, mouth open.
                with dissolve

                sa "Yayyy!"

                scene v13s28_9 # TPP. Show Samantha leaning over and hugging MC who is sitting down at the bus stop, all slight smile, all mouth closed.
                with dissolve

                pause 0.75

                scene v13s28_7b
                with dissolve

                u "I don't feel too good about this, Sam. Don't make me regret putting you in this kind of environment."

                scene v13s28_7e
                with dissolve

                sa "Don't worry, I'll be good. *Chuckles*"

                scene v13s28_7b
                with dissolve

                u "Alright. (I hope so.)"

                scene v13s28_10 # TPP. Show Samantha starting to sit next to MC and Amber, all slight smile, all mouths closed
                with dissolve

                pause 0.75

                scene v13s28_10a # TPP. Same as v13s28_10. Samantha sitting with MC and Amber.
                with dissolve

                pause 1.00

                scene v13s28_10b # TPP. Same as v13s28_10a, all different pose.
                with fade

                pause 0.75

        stop music fadeout 3

        jump v13s29
    
    else: 
        scene v13s28_11 # TPP. Show Amber and MC sitting at the bus stop.
        with dissolve

        pause 1.00

        scene v13s28_11a # TPP. Same as v13s28_11. MC and Amber different pose.
        with fade

        pause 0.75

        stop music fadeout 3

        jump v13s29