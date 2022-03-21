# SCENE 62: Transition Mc walks to chicks house
# Locations: The sidewalk towards the Chicks house.
# Characters: MC (outfit: 2)
# Time: Thursday Evening

label v16s62:

    scene v16s62_1 # TPP. Show MC(slight smile, mouth closed) walking down the sidewalk towards the Chicks house.
    with fade
    
    pause 0.75
    
    if v14_help_chloe and not v16s12_chloe_planboard_decide_newspaper_cover:
        jump v16s63

    else:
        jump v16s65