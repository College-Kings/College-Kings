# SCENE 4: Ryan vs Perry
# Locations: Abandoned Warehouse
# Characters: Ryan (Outfit 2), Perry (Outfit ), Josh (Outfit 2), 
# Time: Saturday Night
label v9_ryan_v_perry_fight:
    play music music.ck1.v10.Track_Scene_4 fadein 2
    scene v10rpf1 # FPP. Show josh, in ring, excited look, mouth open
    with fade
    jo "Well, the show must go on."
    
    jo "After this small delay, we're now finally ready for the first fight of the night."
    
    jo "Ryan versus Perry!"

    scene v10rpf2 # FPP. Show Ryan and Perry entering the ring, mouths closed
    with dissolve

    pause 0.75

    scene v10rpf3 # FPP. Show close up of josh, excited look, mouth open
    with dissolve
    jo "Don't kill each other, stay in the ring, yada, yada, yada. Have fun!"

    scene v10rpf4 # FPP. Show close up of josh exiting the ring, mouth closed
    with dissolve

    pause 0.75

    scene v10rpf2a # FPP. Same camera as v10rpf2, Show Ryan and Perry now in the ring, mouths closed
    with dissolve

    pause 0.75

    scene v10rpf5 # FPP. Show close up of perry, hand up gaurding face, mouth open
    with dissolve
    guyd "Let's dance, Ape."

    scene v10rpf6 # FPP. Show close up of Ryan, hand up gaurding his CHEST, mouth open
    with dissolve
    ry "Apes don't dance, bitch. We fight!"

    scene v10rpf7 # TPP. Show Perry and ryan squaring up to each other in the ring, mouths closed
    with dissolve

    pause 0.75

    scene v10rpf7a # TPP. Same camera as v10rpf7, show perry throwing a punch towards ryan (Not connected yet), mouths closed
    with dissolve

    pause 0.5

    scene v10rpf7b # TPP. Same camera as v10rpf7, Ryan ducking under perrys punch, mouths closed
    with dissolve

    pause 0.5

    scene v10rpf7c # TPP. Same camera as v10rpf7, Ryan gives perry an upper cut to the chin, mouths closed
    with dissolve

    pause 0.5

    scene v10rpf4a # FPP. Show close up of josh entering the ring, mouth closed
    with dissolve

    pause 0.5

    scene v10rpf8 # FPP. Show Josh, mouth open in ring, show perry on floor unconcious, show ryan holding hands in the air, mouth closed
    with dissolve
    jo "Doesn't look like he's getting up anytime soon! Not sure any of us expected this to happen so quickly... Is he alive?"

    jo "Ah, who cares, this is fight night."
    
    jo "Anyways, looks like we have a winner everyone! Most likely in record time!"

    jo "Any words to the crowd after that amazing performance?"

    scene v10rpf9 # FPP. Show close up of ryan in the ring, mouth open, happy look
    with dissolve

    ry "I'm just warming up."

    scene v10rpf3
    with dissolve

    jo "You've heard it here first, Ryan came to fight!"
    stop music fadeout 3
    jump v10_mc_vs_ryan_fight

    # -Transition to Scene 6-