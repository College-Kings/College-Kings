# SCENE 18f: Sleeping over at Lauren's
# Locations: 
# Characters: 
# Time: 

label v15s18f:
    play music "music/v15/Track Scene 18f.mp3" fadein 2

    if v15s18_LaurensBed:
        scene v15s18f_1 # TPP. Show MC and Lauren in an affectionate cuddle, MC big spoon, Lauren little spoon, both have their eyes closed, both slight smile, mouth closed.
        with dissolve
        
        pause 2

    else: # Placeholder
        scene v15s18f_2 # TPP. Show Mc laying on the couch in the Deer's house, Party mess all around him, MC staring at the ceiling with a blanket on and his head on a pillow, neutral face mouth closed.
        with dissolve

        pause 0.75

        scene v15s18f_2a # TPP. MC laying on the couch in the Deer's house, Party mess all around him, MC laying on his side uncomfortable.
        with dissolve

        pause 0.75
        
        scene v15s18f_2 
        with dissolve

        pause 0.75

        scene v15s18f_2b # TPP. # TPP. Show Mc laying on the couch in the Deer's house, Party mess all around him, eyes closed with a blanket on and his head on a pillow, neutral face mouth closed.
        with dissolve

        pause 0.75

    jump v15s19