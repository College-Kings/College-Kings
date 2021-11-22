# SCENE 6: School hallway towards library
# Locations: School hallway
# Characters: MC (Outfit: 5), Chloe (Outfit: 2)
# Time: Friday


label v15s6:
    scene v15s6_1 # TPP Show MC walking in school hallway toward library
    with dissolve

    pause 1

    if (v14s51_take_diary or v14s51_take_money): # -if MC stole any of Chloe's money and/or her diary from her room

        scene v15s6_2 # FPP Show Chloe exiting library, she is crying, using her hand to try and mask the tears
        with dissolve

        u "(There's Chloe. Oh shit- Is she crying?)"
        u "(What happened this time... *Sighs*)"


    else: # -if MC stole nothing from Chloe's room or never went to Chloe's room

        scene v15s6_2a # FPP Show Chloe near library door, smiling and chatting with two random students
        with dissolve

        u "(Oh, there's Chloe. Putting on the charm for votes no doubt, haha.)"

    # -Regardless-
    jump v15s7 # -Transition to Scene 7-
