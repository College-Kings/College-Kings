# SCENE 76: Transition Mc gets dressed up WOLVES OR APES
# Locations: MC WOLF DORM ROOM, MC APE DORM ROOM
# Characters: MC (Outfit: 6)
# Time: Friday night

label v16s76: # 76) MC dresses up for the opera
    
    if joinwolves: # if joinwolves:
        
        scene v16s76_1 # TPP Show MC getting into his homecoming suit [WOLF DORM ROOM ]
        with dissolve

        pause 0.75

        scene v16s76_2 # TPP MC (smiling, mouth closed) looks at himself in the mirror. He's wearing his homecoming suit, making last-minute adjustments [WOLF DORM ROOM ]
        with dissolve

        u "(Looking good, [name]. Real good... *Laughs*)"

        scene v16s76_3 # TPP Show MC (slight smile, mouth open) looking down at his phone in his hand to check the time [WOLF DORM ROOM ]
        with dissolve

        u "Time for the opera! Never thought I'd say that..."

        scene v16s76_4 # TPP Show MC walking out of his room [WOLF DORM ROOM ]
        with dissolve

        pause 0.75
    
    else: # joined apes 
        
        scene v16s76_5 # TPP Show MC getting into his homecoming suit [APE DORM ROOM ]
        with dissolve

        pause 0.75

        scene v16s76_6 # TPP MC (smiling, mouth closed) looks at himself in the mirror. He's wearing his homecoming suit, making last-minute adjustments [APE DORM ROOM ]
        with dissolve

        u "(Looking good, [name]. Real good... *Laughs*)"

        scene v16s76_7 # TPP Show MC (slight smile, mouth open) looking down at his phone in his hand to check the time [APE DORM ROOM ]
        with dissolve

        u "Time for the opera! Never thought I'd say that..."

        scene v16s76_8 # TPP Show MC walking out of his room [APE DORM ROOM ]
        with dissolve

        pause 0.75

    jump v16s77 # -Transition to Scene 77-