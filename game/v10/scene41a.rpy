# SCENE 41a: MC waking up in his room cliffhanger
# Locations: MC NEW Wolves/Apes Room
# Characters: MC (Underwear)
# Time: Thursday Morning

label v10_waking_up_end:
    play music music.ck1.v10.Track_Scene_22_1 fadein 2

    if mc.frat == Frat.WOLVES:
        scene v10end1 # TPP. Show MC waking up drowsy in his new Wolves room.
        with fade

        u "(OH FUCK WHAT TIME IS IT?)"

        scene v10end2 # TPP. Show MC on his bed, shocked expression.
        with dissolve

        pause 0.75

        scene v10end2a # TPP. Same as 2, MC grabs his phone, panicked expression.
        with dissolve

        $ MessengerService.new_message(penelope, "Hey, do you mind coming by before the hearing starts?")
        $ MessengerService.new_message(penelope, "Hey! Where are you, the hearing is in two hours.")
        $ MessengerService.new_message(penelope, "WHERE ARE YOU THE HEARING IS IN 15 MINUTES!?")
        $ MessengerService.new_message(penelope, "OMG, WE'RE STARTING! WHERE ARE YOU?")

        u "(Oh shit, Penelope has been blowing me up.)"
        
        call screen messenger(penelope)

        stop music fadeout 3
        play music music.ck1.v10.Track_Scene_41a_2 fadein 2
        
        scene v10end3 # TPP. Show MC, now wearing outfit 2, rushing out of his room.
        with dissolve

        pause 0.75

        scene black
        with fade

        pause 1
        stop music fadeout 3

    else:
        scene v10end4 # TPP. Show MC waking up drowsy in his Apes room.
        with fade

        u "(OH FUCK WHAT TIME IS IT?)"

        scene v10end5 # TPP. Show MC on his bed, shocked expression.
        with dissolve

        pause 0.75

        scene v10end5a # TPP. Same as 2, MC grabs his phone, panicked expression.
        with dissolve

        $ MessengerService.new_message(penelope, "Hey, do you mind coming by before the hearing starts?")
        $ MessengerService.new_message(penelope, "Hey! Where are you, the hearing is in two hours.")
        $ MessengerService.new_message(penelope, "WHERE ARE YOU THE HEARING IS IN 15 MINUTES!?")
        $ MessengerService.new_message(penelope, "OMG, WE'RE STARTING! WHERE ARE YOU?")

        u "(Oh shit, Penelope has been blowing me up.)"

        call screen messenger(penelope)

        stop music fadeout 3
        play music music.ck1.v10.Track_Scene_41a_2 fadein 2

        scene v10end6 # TPP. Show MC, now wearing outfit 2, rushing out of his room.
        with dissolve

        pause 0.75

        scene black
        with fade

        pause 1
        stop music fadeout 3

    jump v11_start
