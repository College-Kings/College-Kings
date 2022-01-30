# SCENE 5: The next morning MC wakes up early
# Location: Hotel room, hotel lobby, hotel corridor, shuttle
# Characters: MC (Outfit 1), Amber (Outfit 1), Chloe (Outfit 3), Riley (Outfit 3), Lindsey (Outfit 1), Ms. Rose (Outfit 1)
# Time: Morning

label v12_morning_london:
    play music "music/v12/Track Scene 5.mp3" fadein 2

    if not v11_riley_roomate:
        if chloe.relationship >= Relationship.FWB:
            scene v12mol1 # TPP. Show MC waking up, Chloe sleeping next to him in MC's bed
            with fade

            pause 0.75

            scene v12mol1a # TPP. Show MC waking Chloe up, MC slight smile, mouth closed
            with dissolve

            pause 0.75

            scene v12mol3 # FPP. Same positioning as v12mol1, MC and Chloe looking at each other, Chloe slight smile, mouth closed
            with dissolve

            u "Wake up before we're late."

            scene v12mol3a # FPP. Same as v12mol3, Chloe slight smile, mouth open
            with dissolve

            cl "Is it really time to wake up? Pretty surprised that you woke up first. *Chuckles* No offense."

            scene v12mol3
            with dissolve

            u "Maybe you had more to drink last night than you thought."

            scene v12mol3a
            with dissolve

            cl "I like that excuse, we'll go with that."

            scene v12mol3b # FPP. Same as v12mol3, Chloe different pose
            with dissolve

            u "*Chuckles* Ready to get on the plane?"

            scene v12mol3c # FPP. Same as v12mol3b, Chloe slight smile, mouth open
            with dissolve

            cl "We're not getting on a plane remember?"

            scene v12mol3b
            with dissolve

            u "No... I don't remember. How are we getting to Paris?"

            scene v12mol3c
            with dissolve

            cl "We're taking a ferry."

            scene v12mol3
            with dissolve

            u "A what?"

            scene v12mol3a
            with dissolve

            cl "*Chuckles* You'll see."

        else:
            scene v12mol1b # TPP. Same as v12mol1, but MC alone in his bed
            with fade

            pause 0.75

            scene v12mol1c # TPP. Same as v12mol1b, show MC getting out of his bed
            with dissolve

            pause 0.75

            scene v12mol2 # TPP. Show MC waking Chloe up (Chloe in her bed), MC slight smile, mouth closed
            with dissolve

            pause 0.75

            scene v12mol4 # FPP. Same positioning as v12mol2, Chloe and MC looking at each other, Chloe slight smile, mouth closed
            with dissolve

            u "Wake up before we're late."

            scene v12mol4a # FPP. Same as v12mol4, Chloe slight smile, mouth open
            with dissolve

            cl "Is it really time to wake up? Pretty surprised that you woke up first. *Chuckles* No offense."

            scene v12mol4
            with dissolve

            u "Maybe you had more to drink last night than you thought."

            scene v12mol4a
            with dissolve

            cl "I like that excuse, we'll go with that."

            scene v12mol4b # FPP. Same as v12mol4, different pose
            with dissolve

            u "*Chuckles* Ready to get on the plane?"

            scene v12mol4c # FPP. Same as v12mol4b, Chloe slight smile, mouth open
            with dissolve

            cl "We're not getting on a plane remember?"

            scene v12mol4b
            with dissolve

            u "No... I don't remember. How are we getting to Paris?"

            scene v12mol4c
            with dissolve

            cl "We're taking a ferry."

            scene v12mol4
            with dissolve

            u "A what?"

            scene v12mol4a
            with dissolve

            cl "*Chuckles* You'll see."

    else:
        scene v12mol1b
        with fade

        pause 0.75

        scene v12mol1c
        with dissolve

        pause 0.75

        scene v12mol5 # FPP. MC standing next to his bed, looking at Riley sleeping in her bed
        with dissolve

        u "(I actually woke up first, time for a little payback.)"

        scene v12mol6 # TPP. Show MC grabbing his pillow, slight smile, mouth open
        with dissolve

        pause 1

        scene v12mol7 # TPP. Show MC sneaking up next to Riley, MC holding the pillow, ready to hit her, MC slight grin, mouth closed
        with dissolve

        pause 0.6

        scene v12mol7a # TPP. Same as v12mol7, Riley scaring MC, MC falling down to the floor, MC startled, mouth closed, Riley mouth open
        with dissolve

        ri "AHHHHH!!!!"

        scene v12mol7b # TPP. Show Riley smiling, mouth closed, sitting on her bed, watching MC get up from the floor, MC startled, mouth closed
        with dissolve

        pause 0.75

        scene v12mol8 # FPP. Same positioning as v12mol7b, MC standing now, MC and Riley looking at each other, Riley smile, mouth closed
        with dissolve

        u "Oh shit!"

        scene v12mol8a # FPP. Same as v12mol8, Riley smile, mouth open
        with dissolve

        ri "*Laughs* Yeah, you thought! You'll never wake up before me and you'll definitely never be able to sneak up on me."

        scene v12mol8
        with dissolve

        u "Haha, is that challenge or something?"

        scene v12mol8a
        with dissolve

        ri "Call it what you want, I call it the truth."

        scene v12mol8
        with dissolve

        u "Challenge accepted."

    scene v12mol9 # TPP. Show the door to the hallway
    with dissolve

    play sound "sounds/knock.mp3"

    pause 1.25
    
    scene v12mol10 # TPP. Show MC walking towards the door to the hallway, slight smile, mouth closed (Only MC in shot)
    with dissolve

    u "What's up?"

    if not v11_riley_roomate:
        scene v12mol99
        with dissolve

        pause 0.75

    scene v12mol11 # TPP. Show MC opening the door to the hallway, slight smile, mouth closed, Amber on the other side, mouth closed, slight smile
    with dissolve

    pause 1.25

    scene v12mol12 # FPP. MC and Amber looking at each other (MC in room, Amber in hallway), Amber slight smile, mouth open
    with dissolve

    am "Hey, it's time to go."

    scene v12mol12a # FPP. Same as v12mol12, Amber slight smile, mouth closed
    with dissolve

    u "Alright, cool."

    scene v12mol12
    with dissolve

    am "Hey, uh. Do you mind sitting by me on the plane? There's something I wanna talk to you about."

    if not v11_riley_roomate:
        scene v12mol12b # FPP. Same as v12mol12a, Amber slightly confused and smiling, mouth closed, different pose
        with dissolve

        u "We're taking a ferry, not a plane."

        scene v12mol12c # FPP. Same as v12mol12b, Amber mouth open, slightly confused and smiling
        with dissolve

        am "What's that?"

        scene v12mol12b
        with dissolve

        u "Apparently, we'll see."

        scene v12mol13 # FPP. Same positioning as v12mol12, MC looking at Chloe, Chloe sitting on her bed, looking at MC, laughing
        with dissolve

        cl "*Laughs*"

        scene v12mol12a
        with dissolve

        u "Let me just grab my bag."

        scene v12mol14 # TPP. Show MC grabbing his bag, slight smile, mouth closed (Only MC in shot)
        with dissolve

        pause 0.75

        if chloe.relationship >= Relationship.FWB:
            scene v12mol15 # TPP. Show MC giving Chloe a kiss, MC holding his bag
            with dissolve

            play sound "sounds/kiss.mp3"

            pause
        
        scene v12mol10a # FPP. Same as v12mol10, MC carrying his bag now
        with dissolve

        pause 0.75

    else:
        scene v12mol12a
        with dissolve

        u "Yeah sur-"

        scene v12mol12
        with dissolve

        am "Wait, it's actually a ferry we're taking. I keep forgetting, but yeah... Mind sitting by me?"

        scene v12mol12a
        with dissolve

        u "Sure, I don't mind."

        scene v12mol12
        with dissolve

        am "Thanks."

        scene v12mol14
        with dissolve

        pause 0.75

        scene v12mol10a
        with dissolve

        pause 0.75

        scene v12mol12a
        with dissolve

        u "Let's go, slowpoke. *Chuckles*"

    scene v12mol16 # TPP. Show MC and Amber walking in the hotel room corridor, both slightly smiling, mouths closed
    with dissolve

    pause 0.75

    scene v12mol17 # TPP. Show MC and Amber walking through the hotel lobby, Lindsey and Ms Rose in background talking to each other, all slight smiles, mouths closed
    with dissolve

    pause 0.75

    scene v12mol18 # TPP. Show MC getting on the shuttle with Amber, Riley in the background looking at them, MC and Amber slight smiles, mouths closed, Riley slightly confused, mouth closed
    with dissolve

    pause 0.75

    scene v12mol19 # TPP. Show the shuttle on the road
    with dissolve

    pause 1.25

    stop music fadeout 3

    jump v12_docks #scene 6