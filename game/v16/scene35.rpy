# SCENE 35: Buying spa items for Chloe
# Locations: Store with spa items
# Characters: MC (Outfit: 9), Cashier (Outfit: 1)
# Time: Morning


label v16s35:
    play sound "sounds/dooropen.mp3"

    scene v16s35_1 # TPP. Show MC walking into the store with all the spa items, MC slight smile, mouth closed.
    with fade (1,0,1)

    u "(Okay, spa supplies...)"

    play sound "sound/doorclose.mp3"

    scene v16s35_2 # TPP. Show MC walking through the store, MC slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v16s35_3 # FPP. MC looking at the part of the store with massage oil and face mask.
    with dissolve

    u "(I'm going to need some massage oil and face masks.)"

    # - TODO: SPA FREEROAM - A UI pops up showing MC his choices. He can purchase one type of massage oil: Tingling Mint or Calming Citrus. And one type of face mask: Expensive brand or Cheap brand-
    # TODO: Use $ v16s35_mc_spa_shopping.add() to add items MC purchases in the freeroam 

    # -Exit UI when choices have been made-

    if "Tingling mint massage oil" in v16s35_mc_spa_shopping: # TODO: Variable #Placeholder
        
        scene v16s35_4 # FPP. MC focused on the massaging oils.
        with dissolve

        u "(Tingling mint. That sounds refreshing, right?)"

    else:
        scene v16s35_4
        with dissolve

        u "(Calming citrus. Can't go wrong with a name like that, haha.)"

    if "Expensive face mask" in v16s35_mc_spa_shopping: # TODO: Variable #Placeholder
        
        scene v16s35_5 # FPP. MC focused on the face mask.
        with dissolve

        u "(Let's go with the high-end masks. Only the best for the Chicks' skin!)"

    else:
        
        scene v16s35_5
        with dissolve
        
        u "(Face masks don't really matter... They all do the same thing anyway, right?)"

    scene v16s35_3
    with dissolve

    u "(Nice. The girls are gonna love this stuff, I'm sure.)"

    u "(Now to pay for it...)"

    scene v16s35_6 # TPP. Show MC approaching the cashier with the items, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v16s35_7 # TPP. Close up of MC's hand putting the money on the counter
    with dissolve 

    pause 0.75

    scene v16s35_7a # TPP. Close up of the Cashier handing MC the bag and MC grabbing it.
    with dissolve

    u "Thanks."

    play sound "sounds/dooropen.mp3"

    scene v16s35_8 # TPP. MC walking out of the store with a shopping bag in his hand, the cashier in the back smiling and waving him goodbye.
    with dissolve

    u "(I'll drop these off at the Chicks house first, then I need to head back home.)"

    play sound "sounds/doorclose.mp3"

    scene v16s35_9 # TPP. MC walking down the street with a shopping bag in his hand, MC slight smile, mouth closed.
    with dissolve
    
    if joinwolves:

        scene v16s35_9
        with dissolve

        u "(And hopefully there's no Chris and Imre drama waiting for me this time...)"
    else:
        scene v16s35_9
        with dissolve
        
        u "(And hopefully there's no Grayson and Sam drama waiting for me this time...)"

    jump v16s33