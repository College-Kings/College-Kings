# SCENE 41a: MC waking up in his room cliffhanger
# Locations: MC NEW Wolves/Apes Room
# Characters: MC (Underwear)
# Time: Thursday Morning

label v10_waking_up_end:
    play music "music/v10/Scene 41a/Track Scene 41a_1.mp3" fadein 3
    if joinwolves:
        scene v10end1 # TPP. Show MC waking up drowsy in his new Wolves room.
        with fade

        u "(OH FUCK WHAT TIME IS IT?)"

        scene v10end2 # TPP. Show MC on his bed, shocked expression.
        with dissolve

        pause 0.75

        scene v10end2a # TPP. Same as 2, MC grabs his phone, panicked expression.
        with dissolve

        u "(Oh shit, Penelope has been blowing me up.)"
        stop music fadeout 3
        play music "music/v10/Scene 41a/Track Scene 41a_2.mp3" fadein 3
        python:
            contact_Penelope.newMessage("Hey, do you mind coming by before the hearing starts?", queue=False)
            contact_Penelope.newMessage("Hey! Where are you, the hearing is in two hours.", queue=False)
            contact_Penelope.newMessage("WHERE ARE YOU THE HEARING IS IN 15 MINUTES!?", queue=False)
            contact_Penelope.newMessage("OMG, WE'RE STARTING! WHERE ARE YOU?", queue=False)

        call screen phone

        label v10s41a_phoneCheckW:
            if contact_Penelope.getReplies():
                call screen phone

                u "(I should check my phone)"

                jump v10s41a_phoneCheckW

        scene v10end3 # TPP. Show MC, now wearing outfit 2, rushing out of his room.
        with dissolve

        pause 0.75

        scene black
        with fade

        pause 1
        stop music fadeout 3
        jump end10

    else:
        scene v10end4 # TPP. Show MC waking up drowsy in his Apes room.
        with fade

        u "(OH FUCK WHAT TIME IS IT?)"

        scene v10end5 # TPP. Show MC on his bed, shocked expression.
        with dissolve

        pause 0.75

        scene v10end5a # TPP. Same as 2, MC grabs his phone, panicked expression.
        with dissolve

        u "(Oh shit, Penelope has been blowing me up.)"
        stop music fadeout 3
        play music "music/v10/Scene 41a/Track Scene 41a_2.mp3" fadein 3
        python:
            contact_Penelope.newMessage("Hey, do you mind coming by before the hearing starts?", queue=False)
            contact_Penelope.newMessage("Hey! Where are you, the hearing is in two hours.", queue=False)
            contact_Penelope.newMessage("WHERE ARE YOU THE HEARING IS IN 15 MINUTES!?", queue=False)
            contact_Penelope.newMessage("OMG, WE'RE STARTING! WHERE ARE YOU?", queue=False)

        call screen phone

        label v10s41a_phoneCheckA:
            if contact_Penelope.getReplies():
                call screen phone

                u "(I should check my phone)"

                jump v10s41a_phoneCheckA

        scene v10end6 # TPP. Show MC, now wearing outfit 2, rushing out of his room.
        with dissolve

        pause 0.75

        scene black
        with fade

        pause 1
        stop music fadeout 3
        jump end10

label end10:
    if persistent.ep < 11:
        scene savenow
        with Fade (1,0,1)
        " "

    if persistent.ep < 11:
        jump end_credits
    else:
        jump v11start
