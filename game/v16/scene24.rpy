# SCENE 24: Transition Mc walks home
# Locations: Street
# Characters: MC (Outfit: 5)
# Time: Tuesday night

label v16s24: # 24) MC goes home
    scene v16s24_1 # -MC walks along the street
    with dissolve

    pause 0.75

    if v14_amber_clean: 
        scene v16s24_2 # TPP Another shot of MC walking down the street
        with dissolve

        u "(Amber used to be really embarrassed to work there, but now she seems a lot more comfortable. It's nice to see her doing so well.)"


    else: # -if AmberDrugs
        scene v16s24_2
        with dissolve

        u "(I'm not sure how long it'll be before Amber ends up hitting one of those creeps... But I hope I'm there to see it when it happens!)"


    jump v16s25 # -Transition to Scene 25-