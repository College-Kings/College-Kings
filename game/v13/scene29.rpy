# SCENE 29: Weed Bus Tour
# Locations: Street, Weed Bus, Bus stop
# Characters: GARY (Outfit: 1), AMBER (Outfit: 1), MC (Outfit: 9), SAMANTHA (Outfit: 1)
# Time: Evening

label v13s29:
    play music "music/v13/Track Scene 29_1.mp3" fadein 2

    if not v13_invite_samantha:
        scene v13s29_1: # TPP. Show Amber and MC on sidewalk in front of The AmsterDamn, all smiling, all mouths closed (Weed Bus)
        with dissolve

        pause 0.75

        scene v13s29_2 # TPP. MC and Amber walking into bus, slight smiles, all mouths closed
        with dissolve

        pause 0.75

        scene v13s29_3 # TPP. Show Amber sitting next to MC inside the Amsterdamn, show Gary at the front of the bus, all smiling, all mouths closed
        with dissolve

        pause 0.75

        scene v13s29_4 # FPP. MC looking at Gary, Gary happy, arms spread apart, mouth open
        with dissolve

        gary "My friends, my wonderful friends. Welcome to the bus of weed, or as I like to call it, The AmsterDamn."

        scene v13s29_5 # FPP. MC looking at Amber sitting next to him, Amber looking at MC, leaning in close to MC, slight smile, mouth open
        with dissolve

        am "*Whisper* Weirdo."

        scene v13s29_5a # FPP. Same as v13s29_5, Amber smiling at MC, mouth closed
        with dissolve

        u "*Chuckles*"

        scene v13s29_4a # FPP. Same angle as v13s29_4, Gary hands on hips, unhappy face, mouth open
        with dissolve

        gary "First, I gotta deal with the boring stuff. Who bought their tickets?"

        scene v13s29_3a # TPP. Same angle as v13s29_3, Amber and MC raising their hands, looking at eachother smiling, mouths closed
        with dissolve

        pause 0.75
        
        #scene v13s29_6 # FPP. MC looking at Gary, Gary has moved closer to MC, MC extending arm toward Gary with currency in hand, Gary smiling, mouth closed
        #with dissolve

        #pause 0.75

    else:
        scene v13s29_1a: # TPP. Show Samantha, Amber and MC on sidewalk in front of The AmsterDamn, all smiling, all mouths closed (AmsterDamn = Weed Bus)
        with dissolve

        pause 0.75

        scene v13s29_2a # TPP. Same angle as v13s29_2, Samantha, Amber, and MC walking up bus steps, all mouths closed
        with dissolve

        pause 0.75

        scene v13s29_99 # TPP. Show MC sitting inbetween Amber and Samantha inside the Amsterdamn, show Gary at the front of the bus, all smiling, all mouths closed
        with dissolve

        pause 0.75

        scene v13s29_4
        with dissolve

        gary "My friends, my wonderful friends. Welcome to the bus of weed, or as I like to call it, The AmsterDamn."

        scene v13s29_5
        with dissolve

        am "*Whisper* Weirdo."

        scene v13s29_5a
        with dissolve

        u "*Chuckles*"

        scene v13s29_4a
        with dissolve

        gary "First, I gotta deal with the boring stuff. Who bought their tickets?"

        scene v13s29_3b # TPP. Same angle as v13s29_3a, Amber raising her hand looking at Gary, MC raising his hand looking at Gary, Samantha looking at MC, all mouths closed
        with dissolve

        pause 0.75

        scene v13s29_6a # FPP. Same angle as v13s29_6, Gary confused, mouth closed
        with dissolve

        u "She doesn't have hers, but here."

        scene v13s29_6b # FPP. Same angle as v13s29_6, Gary mouth open
        with dissolve

        gary "Very good!"

    scene v13s29_4
    with dissolve

    gary "Now I should introduce myself, my name is Gary Ganja, King of Weeds, etc."

    scene v13s29_4b # FPP. Same angle as v13s29_4, same positioning, arms still stretched out, Gary looking at MC annoyed, Gary mouth closed
    with dissolve

    u "So, what did we spend our money on...?"

    scene v13s29_4c # FPP. Same angle as v13s29_4b, Gary mouth open
    with dissolve

    gary "Well young friend, you paid for a ticket, but you're getting an experience."

    scene v13s29_7 # FPP. MC looking at Amber, Amber looking at Gary, Amber annoyed, Amber mouth open
    with dissolve

    am "I paid to find out what's the best weed so let's get on with it."

    scene v13s29_8 # FPP. MC looking at Gary, Gary's hands up, palms facing Amber and MC, Gary smiling, slightly shocked, Gary mouth open
    with dissolve

    gary "Chillax my brothers and sisters, the time has come for your eyes to be opened..."

    scene v13s29_9 # FPP. MC looking at Gary, Gary bowing down, one arm over his stomach, the other stretched out, Gary mouth open
    with dissolve

    gary "Follow me."

    if not v13_invite_samantha:
        scene v13s29_10 # FPP. MC looking at Gary, Gary standing next to a weed plant, [Weed plant has bong next to it], Gary's palms open, Gary gesturing toward the weed plant, Gary eyes closed, Gary very happy, Gary mouth open
        with dissolve

        gary "Can either of you tell me what this is?"

    else:
        scene v13s29_10
        with dissolve

        gary "Can anyone tell me what this is?"

    scene v13s29_11 # FPP. MC looking at Amber, Amber looking at weed plant, Amber bored and unimpressed, Amber arms crossed, Amber mouth open
    with dissolve

    am "Pot."

    scene v13s29_10a # FPP. Same angle as v13s29_10, Gary has new pose, Gary mouth open
    with dissolve

    gary "More specifically?"

    scene v13s29_11a # FPP. Same angle as v13s29_11, Amber slight smile, mouth open
    with dissolve

    am "Good pot. *Chuckles*"

    scene v13s29_10b # FPP. Same angle as v13s29_10, Gary looking at Amber, mouth open
    with dissolve

    gary "My sister, this is called the Cheex."

    scene v13s29_10c # FPP. Same angle as v13s29_10b, Gary looking at MC, mouth closed
    with dissolve

    u "Why is it called that?"

    scene v13s29_12 # FPP. Close up of weed plant
    with dissolve

    gary "Because your cheeks is what you'll be on after a good hit of this beautiful creation of god."

    scene v13s29_11b # FPP. Same angle as v13s29_11a, Amber looking at Gary, mouth open
    with dissolve

    am "You gonna let us hit it?"

    scene v13s29_13 # FPP. MC looking at Gary, Gary hand on back of neck, Gary asking an embarrasing question, mouth open
    with dissolve

    gary "How old are you?"

    scene v13s29_11c # FPP. Same angle as v13s29_11b, Amber looking at Gary, Amber angry, Amber mouth open
    with dissolve

    am "Really? You take my money and show me everything, but now you wanna ask our ages? Don't be like that!"

    scene v13s29_10d # FPP. Same angle as v13s29_10a, Gary crossing his arms, Gary looking at amber, Gary flirty, Gary mouth open
    with dissolve

    gary "So be it, but I wasn't asking you your age because the weed."

    scene v13s29_10e # FPP. Same angle as v13s29_10d, Gary mouth closed
    with dissolve

    u "(Here we go again, another dude flirting with Amber.)"

    scene v13s29_11d # FPP. Same angle as v13s29_11c, Amber looking at Gary, Amber slightly disgusted and shocked, Amber blushing, Amber mouth open
    with dissolve

    am "Ohhh..."

    scene v13s29_10f # FPP. Same angle as v13s29_10d, Gary reaching for bong next to weed plant, Gary looking at Amber, Gary mouth open
    with dissolve

    gary "Don't be shy."

    scene v13s29_10g # FPP. Same angle as v13s29_10f, Gary is offering the bong to Amber, Gary mouth open
    with dissolve

    gary "Take a hit."

    scene v13s29_14 # FPP. MC looking at Amber, Amber holding bong, Amber lips on bong, Gary lighting the bowl for Amber, Bong filling up with smoke, Amber looking down at bong
    with dissolve

    pause 2.5

    scene v13s29_14a # FPP. Same angle as v13s29_14, Gary removed bowl from bong, bong cleared of smoke, Amber looking at ceiling head tilted back, Amber holding breath
    with dissolve

    pause 1.5

    scene v13s29_14b # FPP. Same angle as v13s29_14a, Amber exhaling a lot of smoke, Amber eyes slightly droopy, Amber slightly smiling, Amber mouth open
    with dissolve

    am "Oh wow!"

    scene v13s29_10d 
    with dissolve

    gary "Wow indeed."

    scene v13s29_15 # FPP. Same angle as v13s29_10, Gary is holding a new weed plant, Gary happy, Gary looking at MC, Gary mouth open
    with dissolve

    gary "This here is a HardOn!"

    scene v13s29_15a # FPP. Same angle as v13s29_15, Gary mouth closed
    with dissolve

    u "A WHAT?"

    scene v13s29_15
    with dissolve

    gary "You heard me right, it's a HardOn."

    if v13_invite_samantha:
        scene v13s29_16 # FPP. MC looking at Samantha, Samantha looking at weed plant, Samantha flirty slight smile, Samantha mouth open
        with dissolve

        sa "I can guess why she's called that."

    scene v13s29_17 # FPP. MC and Gary looking at eachother, Gary close to MC, Gary more happy, Gary offering the bong to MC, Gary mouth open
    with dissolve

    gary "Take a hit my brother."

    scene v13s29_17 
    with dissolve

    menu:
        "Nope":
            scene v13s29_17a # FPP. Same angle as v13s29_17, MC hand up, refusing bong, Gary very sad, lowering bong, frowning, mouth closed
            with dissolve

            u "That's not for me."

            scene v13s29_17b # FPP. Same angle as v13s29_17a, Gary mouth open
            with dissolve

            gary "A weed hater on a weed tour, your a weird dude friend."

            scene v13s29_17a
            with dissolve

            u "It wasn't my choice to come."
            
        "Okay":
            $ reputation.add_point(RepComponent.BRO)
            $ v13_smoke_weed = True
            u "Okay, sure."

            scene v13s29_18 # TPP. Show MC hitting bong, bong full of smoke
            with dissolve

            pause 2

            scene v13s29_18a # TPP. Same as v13s29_18, MC breathing out smoke, eyes drooping
            with dissolve

            gary "Okayyyy!"

            scene v13s29_18b # TPP. Same as v13s29_18a, MC looking down at crotch.
            with dissolve

            u "I don't have a hard-"

            scene v13s29_19 # TPP. Close up of MC's bulging erection
            with dissolve

            am "Oh lord..."

            scene v13s29_17c # FPP. Same as v13s29_17, Gary not holding bong, Gary mouth open
            with dissolve

            gary "It's like magic... I use them all the time. And trust me, I know how to use it."

            scene v13s29_17d # FPP. Same as v13s29_17c, Gary mouth closed
            with dissolve

            u "When is this gonna go down?"

            scene v13s29_17c
            with dissolve

            gary "Who know, just think about your grandmother... It works for me."

            scene v13s29_17d
            with dissolve

            u "*Whisper* What the fuck."

    scene v13s29_20 # FPP. MC looking at Gary, Gary facing and looking at Amber, Gary serious, Gary mouth open
    with dissolve

    gary "Alright, time for the lesson. Who here supports the legalization of marijuana all over the world?"

    if v13_invite_samantha:
        scene v13s29_21 # FPP. MC looking at Amber and Sam, both smiling and raising their hands, both looking at Gary, both mouths closed
        with dissolve

        pause 0.75

    else:
        scene v13s29_21a # FPP. Same angle as v13s29_21, Samantha absent
        with dissolve

        pause 0.75


    scene v13s29_20a # FPP. Same as v13s29_20, Gary facing and looking at MC, mouth closed
    with dissolve

    menu:
        "Yes":
            u "Of course."

        "No":
            u "Yeah, I'm not on board with that... Sorry."

    scene v13s29_20b # FPP. Same as v13s29_20, Gary very happy, Gary mouth open
    with dissolve

    gary "Those who don't support legalization aren't crazy and have a very fair point. Even though I LOVE WEED, I don't even support its legalization."

    scene v13s29_11c
    with dissolve

    am "How the fuck does that work? *Chuckles*"

    scene v13s29_20c # FPP. Same angle as v13s29_20b, Gary face neutral, Gary looking at Amber, Gary mouth open
    with dissolve

    gary "Again, I love the shit, but we don't know its affects on every demographic. Young and old, healthy and sick, direct or secondhand high, etc."
    gary "Without a full study I wouldn't feel comfortable with this being as obtainable as a cigarette. It'd be in every school around."

    scene v13s29_20d # FPP. Same angle as v13s29_20c, Gary looking at MC, Gary mouth closed
    with dissolve

    u "It is already."

    scene v13s29_20e # FPP. Same angle as v13s29_20d, Gary looking at Mc, Gary mouth open
    with dissolve

    gary "Not at the level it could be."

    scene v13s29_20d
    with dissolve

    u "For a pothead you seem really concerned about... opposing pot."

    scene v13s29_20e
    with dissolve

    gary "I don't like the term pothead, I'm a Ganja Specialist."

    scene v13s29_22 # FPP. MC looking at Amber, Amber whispering to MC, Amber laughing, Amber mouth open
    with dissolve

    am "*Whisper* Oh my god. *Chuckles*"

    scene v13s29_20f # FPP. Same angle as v13s29_20c Gary annoyed, Gary looking at Amber, Gary mouth open
    with dissolve

    gary "Are you not enjoying the bus tour?"

    scene v13s29_11c
    with dissolve

    am "It's just not what I expected. I thought we'd get high and shit."

    scene v13s29_23 # FPP. MC looking at Gary and Amber, Gary close to Amber, Gary flirting with Amber, Amber looking at Gary nervous, Gary mouth open, Amber mouth closed
    with dissolve

    gary "Come back to my place and chill with me and you can have all the weed you want."

    scene v13s29_23a # FPP. Same angle as v13s29_23, Amber arm wrapped around Gary's shoulder, Amber flirting back with Gary, Amber mouth open, Gary mouth closed
    with dissolve

    am "You like me that much huh?"

    scene v13s29_23b # FPP. Same angle as v13s29_23a, Gary moving in for a kiss, make Gary look stupid, Amber scared of Gary, Amber mouth closed, Gary trying to kiss
    with dissolve

    gary "You know I do."

    play sound "sounds/js.mp3"
    scene v13s29_24 # TPP. Show Amber angry, kneeing Gary in the nuts, Gary in pain, both mouths open
    with vpunch

    pause 0.75

    stop music fadeout 3
    play music "music/v13/Track Scene 29_2.mp3" fadein 2

    scene v13s29_25 # TPP. Show Amber grabbing bags of weed from the bus, preparing to escape, Amber mouth open
    with dissolve

    am "Go, go, go!"

    if v13_invite_samantha:
        scene v13s29_26 # TPP. Show Amber, MC, and Samantha escaping from the Amsterdamn, all mouths open
        with dissolve

        pause 0.75

    else: 
        scene v13s29_26a # TPP. Same angle as v13s29_26, Samantha absent.
        with dissolve

        pause 0.75

    scene v13s29_27 # FPP. MC looking at Amber running, MC directly behind Amber, MC far behind Amber, Amber running towards canals
    with dissolve

    u "Slow down!"

    scene v13s29_27a # FPP. Same angle as v13s29_27, MC slightly closer, Amber standing still, Amber slightly turned around looking at MC, Amber mouth closed.
    with dissolve

    pause 0.75

    scene v13s29_28 # FPP. MC looking at Amber, Amber standing in front of MC, Amber laughing, Amber mouth open
    with dissolve

    am "Did you not just see what I did, I don't know the laws out here. *Chuckles* We gotta go."

    scene v13s29_28a # FPP. Same angle as v13s29_28, Amber mouth open
    with dissolve

    u "Always getting hit on by some weirdo!"

    scene v13s29_28
    with dissolve

    am "The story of my life! *Laughs*"

    if v13_invite_samantha:
        scene v13s29_29 # TPP. Show MC, Amber, and Sam running together
        with fade

        pause 0.75

        scene v13s29_30 # TPP. Show MC, Amber, and Sam running together, now in new location
        with fade

        pause 0.75

        scene v13s29_31 # TPP. Show MC, Amber and Sam arriving at the pier
        with dissolve

        pause 0.75

    else: 
        scene v13s29_29a # TPP. Same as v13s29_29, Sam absent
        with dissolve

        pause 0.75

        scene v13s29_30a # TPP. Same as v13s29_30, Sam absent
        with dissolve

        pause 0.75

        scene v13s29_31a # TPP. Same as v13s29_31, Sam absent
        with dissolve

        pause 0.75

    scene v13s29_32 # FPP. MC looking at Amber, Amber sweaty, Amber tired, Amber looking and facing away from MC, Amber mouth open heavily breathing
    with dissolve

    stop music fadeout 3
    play music "music/v13/Track Scene 29_3.mp3" fadein 2

    u "*Heavy breathing* Fuck!"

    scene v13s29_32a # FPP. Same as v13s29_32, Amber facing and looking at MC, Amber mouth open speaking
    with dissolve

    am "*Heavy breathing* You're out of shape."

    scene v13s29_32b # FPP. Same as v13s29_32a, Amber slight smirk, Amber mouth open heavily breathing
    with dissolve

    u "Because what, I'm breathing? You're breathing heavy too."

    scene v13s29_32a
    with dissolve

    am "*Heavy breathing* I could run another mile, I noticed you slowing down."

    scene v13s29_32b
    with dissolve

    u "*Heavy breathing* Whatever."

    if v13_invite_samantha:
        scene v13s29_33 # FPP. MC looking at Sam, Sam completely energized and not tired at all, Sam looking at Amber, Sam mouth open
        with dissolve

        sa "I don't get why either of you are breathing so heavy, it wasn't that far."

        scene v13s29_32c # FPP. Same as v13s29_32a, Amber looking at Sam, Amber slight smirk, Amber mouth open
        with dissolve

        am "*Heavy breathing* When you get some meat on your bones come talk to me."

        scene v13s29_33a # FPP. Same as v13s29_33, Sam angry, Sam mouth open
        with dissolve

        sa "You calling me a stick?"

        scene v13s29_32c
        with dissolve

        am "You said it, not me."

        scene v13s29_33b # FPP. Same as v13s29_33a, Sam sad, Sam mouth open
        with dissolve

        sa "I'm not that skinny, am I?"

        scene v13s29_32c
        with dissolve

        am "You could use a few more pounds."

        scene v13s29_33c # FPP. Same as v13s29_33b, Sam slightly depressed, Sam looking down, Sam mouth open
        with dissolve

        sa "Well damn, okay."

    scene v13s29_34 # TPP. Show MC and Amber walking down the street, neutral expression, mouth closed
    with Fade(1, 0.5, 1)

    pause 0.75

    if v13_invite_samantha:
        scene v13s29_35 # TPP. Show MC, Amber and Samantha walking down the street, arriving at the canal, neutral expressions, mouths closed
        with fade

        pause 0.75
    
    else:
        scene v13s29_35a # TPP. Same as v13s29_35, no Samantha
        with fade

        pause 0.75

    stop music fadeout 3

    jump v13s30