# SCENE 2: Transition
# Locations: San Vallejo parking lot after the fight with Tom
# Characters: MC (Outfit: 1), Riley (Outfit: 2)
# Time: Night

label v16s2:
    if v16s2_walkalone: #Placeholder variable
        scene v16s2_1 # TPP. Shot of MC walking along the street onto campus, neutral face, mouth closed
        with dissolve

        pause .4

        scene v16s2_2 # TPP. MC further down the street walking on campus, neutral face, mouth closed.
        with dissolve 

        jump v16s4
    else:
        scene v16s2_1a # TPP. Shot of MC and Riley walking along the street onto campus, both neutral face, mouth closed.
        with dissolve 

        pause .4 

        scene v16s2_2a # TPP. MC and Riley further down the stree walking on campus, both neutral face, mouth closed.
        with dissolve

        jump v16s3