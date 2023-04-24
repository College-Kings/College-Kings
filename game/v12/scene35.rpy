# SCENE 35: MC back at his room
# Locations: Hotel Room, Hotel Room Corridor
# Characters: MC (Outfit: 2), NORA (Outfit: 1), CHRIS (Outfit: 1)
# Time: Night
# Phone Images: None

label v12_chris_nora_room:
    scene v12cnr1 # TPP. Show MC walking in the hotel corridor, neutral expression, mouth closed
    with dissolve

    pause 0.75

    play music "music/v12/Track Scene 35.mp3" fadein 2

    scene v12cnr2 # TPP. Show MC walking into his room, mouth closed, neutral expression
    with dissolve

    pause 0.75

    scene v12cnr3 # TPP. Show MC trying to open the bathroom door, neutral expression, mouth closed (door is locked)
    with dissolve

    u "(Locked, she must be in the shower.)"

    scene v12cnr4 # TPP. Show MC walking towards his bed, neutral expression, mouth closed
    with dissolve

    pause 0.75

    scene v12cnr5 # TPP. Show MC lying on his bed, looking at the ceiling, mouth closed, neutral expression
    with dissolve

    u "*Sighs*"

    scene v12cnr5a # TPP. Same as v12cnr5, Show MC looking at the wall, confused, mouth closed
    with dissolve

    no "*Inaudible*"

    scene v12cnr6 # TPP. Show MC walking towards the wall, confused, mouth closed
    with dissolve

    ch "*Inaudible*"

    scene v12cnr7 # TPP. Show MC putting his ear to the wall, mouth closed, confused
    with dissolve

    u "(Are they fighting again?)"

    scene v12cnr8 # TPP. Chris and Nora in another room arguing. Show Nora looking at Chris, Nora pointing at the door to the hallway, Nora very angry, mouth open (Only Nora in shot)
    with dissolve

    no "Just get the fuck out! If you don't wanna be around me, don't be around me."

    scene v12cnr9 # TPP. Same positioning as v12cnr8, Show Chris looking at Nora, Chris very angry, mouth open (Only Chris in shot)
    with dissolve

    ch "I'm not gonna keep feeling bad all the time like all this shit is my fault. Enjoy your fucking night. I'll go sleep somewhere else!"

    play sound "sounds/slam.mp3"

    scene v12cnr7a # TPP. Same as v12cnr7, MC startled, mouth closed
    with dissolve

    u "(Oh shit!)"

    scene v12cnr4
    with dissolve

    u "(It really seems like those two are coming to a crossroads. I'm sure she's pretty heated right now, I wonder if I should go talk to her.)"

    menu:
        "Go to Nora":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            scene v12cnr10 # TPP. Show MC walking towards his hotel room door to the hallway, neutral expression, mouth closed
            with dissolve

            u "(I'm going.)"

            scene v12cnr11 # TPP. Show MC walking towards Nora's room (he is in the hallway), MC slightly worried expression, mouth closed
            with dissolve

            pause 0.75

            scene v12cnr12 # TPP. Show MC knocking on Nora's door, MC slightly worried, mouth open
            with dissolve
            play sound "sounds/knock.mp3"

            u "Nora, I... Are you alright?"

            scene v12cnr13 # TPP. Show Nora sitting on her bed, Nora is crying, mouth open, looking at the hotel room door
            with dissolve

            no "I just wanna be alone right now, [name]."

            scene v12cnr13a # TPP. Same as v12cnr13, Nora crying, mouth closed
            with dissolve

            u "Nora..."

            if v8_nora_likes_mc or v11_kiss_nora: # if Nora likes she lets him in after a bit. If not Nora likes he has to convince her and can fail. If mc made a move on Nora before, she is not letting him in.
                scene v12cnr13
                with dissolve

                no "Please, just... Leave me alone."

                scene v12cnr13a
                with dissolve

                u "*Sighs* Alright."

                scene v12cnr11a # TPP. Same as v12cnr11, MC walking back to his room, slightly worried, mouth closed
                with dissolve

                pause 0.75

                scene v12cnr2
                with dissolve

                pause 0.75

                play sound "sounds/doorclose.mp3"
                scene v12cnr4
                with dissolve

                pause 0.75

                scene v12cnr5
                with dissolve

                u "(Guess I should've just left her alone.)"

                jump v12_game_roommate

            else:
                play sound "sounds/dooropen.mp3"
                scene v12cnr12a # TPP. Same as v12cnr12, Door open, Nora inside the room, looking at MC who is outside, Nora crying, mouth closed, MC worried, mouth closed
                with dissolve

                pause 1.25

                scene v12cnr14 # TPP. Show Nora walking towards her bed, MC slightly behind her, Nora crying, mouth closed, MC worried, mouth closed
                with dissolve

                pause 1

                scene v12cnr15 # TPP. Show Nora and MC sitting next to each other on the bed, Nora crying, mouth closed, MC worried, mouth open, Nora looking down, MC looking at Nora
                with dissolve

                pause 0.75

                stop music fadeout 3

                jump v12_nora_room #scene 35a

        "Leave her alone":
            $ reputation.add_point(RepComponent.BRO)
            scene v12cnr5
            with dissolve

            u "(It's not my place to get involved.)"

            stop music fadeout 3

            jump v12_game_roommate #scene 35b