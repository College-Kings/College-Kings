# SCENE 19: Riley's Revenge
# Locations: Hotel Lobby, Hotel Corridor
# Characters: RILEY (Outfit: 2), MC (Outfit: 9)
# Time: Morning

label v13s19:
    scene v13s19_1 # FPP. MC sitting down, looks at Riley, she is walking over to him, slight smile, mouth closed
    with dissolve

    pause 0.75

    play music "music/v13/Track Scene 19_1.mp3" fadein 2

    scene v13s19_1a # FPP. Same as v13s19_1, Riley now standing close to MC, mouth open, slight smile
    with dissolve

    ri "Hey... Are you ready to make this magic happen?"

    scene v13s19_1b # FPP. Same as v13s19_1a, Riley slight smile, mouth closed
    with dissolve

    u "*Chuckles* Talking about Charli?"

    scene v13s19_1a
    with dissolve

    ri "*Chuckles* You know it! C'mon."

    scene v13s19_2 # TPP. Show MC standing up, Riley same position as v13s19_1a, both slight smiles, mouths closed
    with dissolve

    pause 0.75

    scene v13s19_3 # FPP. MC now standing up, looking at Riley, Riley slight smile, mouth closed
    with dissolve

    u "Alright, let's go."

    scene v13s19_4 # TPP. Show MC and Riley walking in the hotel lobby, slight smiles, mouths closed
    with dissolve

    pause 0.75

    scene v13s19_5 # TPP. Show MC and Riley walking in the hotel corridor, slight smiles, mouths closed
    with fade

    pause 0.75

    stop music fadeout 3
    play music "music/v13/Track Scene 19_2.mp3" fadein 2

    scene v13s19_6 # TPP. Show Riley trying to open the door to Charli's room (it's locked) MC standing next to her, both slight smiles, mouths closed
    with dissolve

    pause 0.75

    scene v13s19_7 # FPP. Same positioning as v13s19_6, MC looking at Riley, Riley looking at MC, Riley slight smile, mouth closed
    with dissolve

    u "It's locked."

    scene v13s19_7a # FPP. Same as v13s19_7, Riley slight smile, mouth open
    with dissolve

    ri "Exactly. *Chuckles*"

    ri "That's what we want... Means he's not here."

    scene v13s19_6a # TPP. Same as v13s19_6, Riley now with the keycard in hand opening the door, both slight smiles, mouths closed
    with dissolve

    pause 0.75

    scene v13s19_7
    with dissolve

    u "What the hell? Where did you get that from?"

    if v11_pen_goes_europe:
        scene v13s19_7a
        with dissolve

        ri "Gotta give props to our favorite little hacker... *Chuckles*"

        scene v13s19_7
        with dissolve

        u "Haha! Penelope... (Gonna have to thank her for this.)"
    
    else:
        scene v13s19_7a
        with dissolve

        ri "Just a little gift from someone who wants this as much as we do..."

        scene v13s19_7
        with dissolve

        u "(Luuk?)"

    play sound "sounds/dooropen.mp3"
    scene v13s19_6b # TPP. Same as v13s19_6, Riley opening the door, both slight smiles, mouths closed
    with dissolve

    pause 0.75

    scene v13s19_7b # FPP. Same as v13s19_7a, but door open
    with dissolve

    ri "Bingo! We're in, baby!"

    ri "You just do your thing, okay? I texted Charli already to meet me somewhere else, so he must be headed there already."

    scene v13s19_7c # FPP. Same as v13s19_7, but door open
    with dissolve

    u "Wow, you got this all worked out, huh?"

    scene v13s19_7b
    with dissolve

    ri "He deserves a damn good show for what he's done to all of us."

    scene v13s19_7c
    with dissolve

    u "I'm gonna give him one."

    scene v13s19_7b
    with dissolve

    ri "*Chuckles* Thank you..."

    scene v13s19_8 # TPP. Show Riley kissing MC on the cheek
    with dissolve
    play sound sound.kiss
    
    pause 2

    scene v13s19_7b
    with dissolve

    ri "Good luck, and have fun!"

    scene v13s19_9 # TPP. Show Riley walking away, MC looking at her, both slight smiles, mouths closed
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v13s20