# SCENE 4: Arrival at Amsterdam Hotel
# Locations: Hotel Lobby
# Characters: MS. ROSE (Outfit: 1), MC (Outfit: 1), RILEY (Outfit: 2), CHLOE (Outfit: 3)
# Time: Night

label v13s4:
    if v11_riley_roomate:
        scene v13s4_1 # TPP. Show MC and Riley getting off the bus, both slightly smiling, mouths closed
        with dissolve

        pause 0.75

        play music "music/v13/Track Scene 4.mp3" fadein 2

        scene v13s4_2 # TPP. Show MC and Riley walking in to the hotel, Ms. Rose in front of them, all slightly smiling, mouths closed, all carrying their luggage
        with dissolve

        pause 0.75

    else:
        scene v13s4_1a # TPP. Same as v13s4_1, but Chloe instead of Riley, Chloe frowning, tired, mouth closed
        with dissolve

        pause 0.75

        play music "music/v13/Track Scene 4.mp3" fadein 2

        scene v13s4_2a # TPP. Same as v13s4_2, but Chloe instead of Riley, Chloe frowning, tired, mouth closed
        with dissolve

        pause 0.75

    scene v13s4_3 # FPP. MC looking at Ms. Rose in hotel lobby, Ms. Rose slight smile, mouth open, looking at MC
    with dissolve

    ro "*Yawn* Alright students, by now you all know how this check-in process works so... Please get yourselves situated."

    if v11_riley_roomate:
        scene v13s4_4 # FPP. MC looking at Riley who is standing next to him, Riley slight smile, mouth closed
        with dissolve

        u "Ready to get some sleep?"

        scene v13s4_4a # FPP. Same as v13s4_4, Riley slight smile, mouth open
        with dissolve

        ri "You don't even have to ask... *Chuckles*"

        scene v13s4_5 # TPP. Show MC and Riley walking in hotel lobby stowards the corridor, carrying their luggage, slight smiles, mouths closed
        with dissolve

        u "(I may have been sleeping that entire ride, but it wasn't very relaxing.)"

        stop music fadeout 3

        jump v13s5a

    else:
        scene v13s4_6 # FPP. MC looking at Chloe who is standing next to MC, Chloe eyes closed, neutral expression, mouth closed
        with dissolve

        u "Ready to get some sleep?"

        u "Chloe?"

        scene v13s4_6a # FPP. Same as v13s4_6a, Chloe startled, mouth closed, eyes open
        with vpunch

        u "CHLOE!"

        scene v13s4_6b # FPP. Same as v13s4_6a, Chloe slightly annoyed, mouth open
        with dissolve

        cl "Huh? Yeah?"

        scene v13s4_6c # FPP. Same as v13s4_6b, Chloe slightly annoyed, mouth closed
        with dissolve

        u "Were you just standing there asleep? *Chuckles*"

        scene v13s4_6b
        with dissolve

        cl "I'm so tired, [name]. I woke up way too early this morning and that bus ride was making me sick so I couldn't sleep."

        scene v13s4_6d # FPP. Same as v13s4_6c, Chloe frowning, mouth closed
        with dissolve

        u "Aww, poor baby. *Chuckles*"

        scene v13s4_6e # FPP. Same as v13s4_6d, Chloe frowning, mouth open
        with dissolve

        cl "Uh-huh, I'm going to bed."

        scene v13s4_6d
        with dissolve

        u "*Chuckles* Right behind you."

        if CharacterService.is_girlfriend(chloe, Relationship.GIRLFRIEND):
            scene v13s4_5b # TPP. Same as v13s4_5a, but MC carrying Chloe's luggage as well
            with dissolve

            pause 1

        else:
            scene v13s4_5a # TPP. Same as v13s4_5, but instead of Riley, it's Chloe, Chloe frowning, mouth closed, carrying her luggage
            with dissolve

            pause 1

        stop music fadeout 3
                
        jump v13s5