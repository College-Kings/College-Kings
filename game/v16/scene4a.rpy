# SCENE 4a_MC_wakes_up: 
# Locations: MC's Wolves/Apes room.
# Characters: MC (Outfit: 5)
# Time: Morning

label v16s4a:

    # -Transition from night to day-
    scene sleep_transition_fast # Ignore Animation
    with fade

    pause 2.2

    scene black
    with dissolve
    
    pause 1

# -MC wakes up, stretching and yawning-
    if joinwolves:
        scene v16s4a_1 # TPP. In wolves room, Show MC laying in bed with his eyes closed, neutral face, mouth closed.
        with dissolve

        pause 0.75

        scene v16s4a_1a # TPP. In wolves room, Show MC laying in bed slightly opening his eyes, neutral face, mouth closed.
        with dissolve

        pause 0.75

        scene v16s4a_2 # TPP. In wolves room, Show MC sitting up in bed and stretching, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v16s4a_3 # TPP. In wolves room, Show MC getting out of bed, slight smile, mouth closed.
        with dissolve

        u "(Another day full of endless possibilities... Gotta love college.)"

        scene v16s4a_4 # TPP. In wolves room, Show MC in the middle of his room putting on his pants, slight smile, mouth closed.
        with dissolve

        pause 0.75 

        scene v16s4a_4a # TPP. In wolves room, Show MC in the middle of his room putting on his shirt, his face obscurred.
        with dissolve

        pause 0.75 

        scene v16s4a_5 # FPP. In wolves room, MC looking at himself in the mirror pointing finger guns, MC smirking, mouth closed.
        with dissolve

        pause 0.75 

        play sound "sounds/dooropen.mp3"

        scene v16s4a_6 # TPP. In wolves room, Shot from behind MC of him opening the door to his room and leaving
        with dissolve

        pause 0.75 

        play sound "sounds/doorclose.mp3"

        scene v16s4a_6a # TPP. In wolves room, Shot of just the room door closed.
        with dissolve

        pause 0.75

    else:
        scene v16s4a_7 # TPP. In apes room, Show MC laying in bed with his eyes closed, neutral face, mouth closed.
        with dissolve

        pause 0.75

        scene v16s4a_7a # TPP. In apes room, Show MC laying in bed slightly opening his eyes, neutral face, mouth closed.
        with dissolve

        pause 0.75

        scene v16s4a_8 # TPP. In apes room, Show MC sitting up in bed and stretching, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v16s4a_9 # TPP. In apes room, Show MC getting out of bed, slight smile, mouth closed.
        with dissolve

        u "(Another day full of endless possibilities... Gotta love college.)"

        scene v16s4a_10 # TPP. In apes room, Show MC in the middle of his room putting on his pants, slight smile, mouth closed.
        with dissolve

        pause 0.75 

        scene v16s4a_10a # TPP. In apes room, Show MC in the middle of his room putting on his shirt, his face obscurred.
        with dissolve

        pause 0.75 

        scene v16s4a_11 # FPP. In apes room, MC looking at himself in the mirror pointing finger guns, MC smirking, mouth closed.
        with dissolve

        pause 0.75 

        play sound "sounds/dooropen.mp3"

        scene v16s4a_12 # TPP. In apes room, Shot from behind MC of him opening the door to his room and leaving
        with dissolve

        pause 0.75 

        play sound "sounds/doorclose.mp3"

        scene v16s4a_12a # TPP. In apes room, Shot of just the room door closed.
        with dissolve

        pause 0.75

jump v16s6