# SCENE 81: Transition Mc changes back into normal Clothes WOLVES OR APES
# Locations: MC's room
# Characters: MC (Outfit: 5)
# Time: Friday night


label v16s81: # 81) MC undresses/changes into normal clothes
    # -MC enters his room (Wolves only). He gets undressed, out of his homecoming suit-
    # LEAVING THIS WRITER'S DESCRIPTION TO EXPRESS MY CONFUSION. NOT SURE WHY "WOLVES ONLY" FOR THIS DESCRIPTION. UNCOMMENT LINE 11 AND INDENT AS NEEDED

    # if joinwolves:
    scene v16s81_1 # TPP Show MC entering his room in his fancy homecoming suit
    with dissolve

    pause 0.75


    scene v16s81_2 # TPP Show MC taking off his fancy suit
    with dissolve

    pause 0.75


    if (v16s27_mc_baby_duty_night == 4 or v16s27_mc_baby_duty_night == 0x40): # -if on baby duty alone or sharing baby duty
        scene v16s81_3 # TPP Show MC (slight frown, eyes closed, mouth closed) looking slightly up as if deeply sighing
        with dissolve

        u "(Daddy duty begins...)"


        scene v16s81_2a # TPP Same angle as 2, MC getting into his normal clothes (in header)
        with dissolve

        pause 0.75


        scene v16s81_4 # TPP Show MC leaving his room
        with dissolve

        pause 0.75


        if v16s27_mc_baby_duty_night == 4: # -if on baby duty alone, transition to Scene 45-
            jump v16s45


        else: # -if sharing baby duty, transition to Scene 47-
            jump v16s47


    else: # -if partner is on baby duty
        scene v16s81_5 # FPP View of MC's bed
        with dissolve

        u "(One peaceful night of sleep, coming up!)"


        scene v16s81_6 # TPP Show MC getting into bed
        with dissolve

        pause 0.75


        scene v16s81_7 # TPP MC in bed, light's off, his eyes look heavy as he drifts off to sleep
        with dissolve

        pause 0.75


        # REVIEWER - I DON'T THINK THIS JUMP IS CORRECT WITH THE RESTRUCTURING - SEEMS LIKE IT WOULD BE A JUMP TO 83 OR 84 DEPENDING ON FRAT
        jump v16s50 # -Transition to Scene 50-