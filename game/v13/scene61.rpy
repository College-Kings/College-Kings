# SCENE 61: MC injured back to hotel
# Locations: Hotel hallway, MC's Hotel Room.
# Characters: AUBREY (Outfit: 2), MC (Outfit: 3)
# Time: Afternoon

label v13s61:
    scene v13s61_1 # TPP. Show Aubrey helping MC walk to his room in the hotel hallway, MC pain expression, mouth closed, Aubrey worried expression, mouth closed.
    with dissolve

    pause 0.75

    play music "music/v13/Track Scene 61.mp3" fadein 2

    scene v13s61_2 # TPP. Show Aubrey helping MC into bed, MC pain expression, mouth closed, Aubrey worried expresion, mouth closed.
    with dissolve

    pause 0.75

    scene v13s61_3 # FPP. MC looking at Aubrey on the side of his bed with his blurry vision, Aubrey worried expression, mouth open.
    with dissolve

    au "Hey there... How are you feeling?"

    scene v13s61_3a # FPP. Same as v13s61_3, Aubrey worried expression, mouth closed.
    with dissolve

    u "I feel like I'm blacking out."

    scene black
    with dissolve
    
    pause 0.5

    scene v13s61_3
    with dissolve

    au "Just rest, okay? I'm so sorry I made you do that for a fucking picture..."

    scene v13s61_3b # FPP. Same as v13s61_3, Aubrey slight frown, mouth open.
    with dissolve

    au "I'm so sorry..."

    scene v13s61_3c # FPP. Same as v13s61_3b, Aubrey slight frown, mouth closed.
    with dissolve

    u "I... I'm gonna get some sleep."

    scene black
    with dissolve
    
    pause 0.5
    
    scene v13s61_3b
    with dissolve

    au "*Sighs* Okay, let me know if you need anything. Please."

    scene v13s61_3c
    with dissolve

    u "I will."

    scene v13s61_3b
    with dissolve

    au "Again, I'm so, so sorry."

    scene v13s61_3c
    with dissolve

    u "Don't worry about it, Aubrey. It's not your fault I can't climb. *Chuckles*"

    scene black
    with dissolve
    
    pause 0.5

    scene v13s61_3b
    with dissolve

    au "I'm glad you still have your sense of humor... Get some rest."

    scene v13s61_4 # FPP. Show Aubrey leaving the room, slight frown, mouth closed.
    with dissolve

    u "*Yawns*"

    scene v13s61_5 # TPP. Show MC sleeping on his back, tired face, mouth closed.
    with dissolve

    pause 0.75

    scene v13s61_5a # TPP. Same as v13s61_5, MC sleeping on his side.
    with fade

    pause 1

    scene v13s61_4a # FPP. Same as v13s61_4, MC looking at door to his room
    with fade

    play sound "sounds/knock.mp3"

    pause 1.5

    stop music fadeout 3

    if CharacterService.is_fwb(aubrey) and CharacterService.is_fwb(riley):
        jump v13s62

    else:
        jump v13s62a