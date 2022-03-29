# SCENE 81: Transition Mc changes back into normal Clothes WOLVES OR APES
# Locations: MC's APE DORM ROOM, MC's WOLF DORM ROOM
# Characters: MC (Outfit: 5)
# Time: Friday evening


label v16s81: # 81) MC undresses/changes into normal clothes
    

    if not joinwolves:
        scene v16s81_1 # TPP Show MC entering his room in his fancy homecoming suit [APES DORM ROOM]
        with dissolve

        pause 0.75

        scene v16s81_2 # TPP Show MC taking off his fancy suit [APES DORM ROOM]
        with dissolve

        pause 0.75

        if v16s27_mc_baby_schedule["friday"] == BabyDuty.ALONE or v16s27_mc_baby_schedule["friday"] == BabyDuty.WITH_PARTNER: 
            
            scene v16s81_3 # TPP Show MC (slight frown, eyes closed, mouth closed) looking slightly up as if deeply sighing [APES DORM ROOM]
            with dissolve

            u "(Daddy duty begins...)"

            scene v16s81_2a # TPP Same angle as 2, MC getting into his normal clothes (in header) [APES DORM ROOM]
            with dissolve

            pause 0.75

            scene v16s81_4 # TPP Show MC leaving his room [APES DORM ROOM]
            with dissolve

            pause 0.75

            # if v16s27_mc_baby_duty_night == 4: # -if on baby duty alone, transition to Scene 45-
            if v16s27_mc_baby_schedule["friday"] == BabyDuty.ALONE:
                jump v16s45

            else: # -if sharing baby duty, transition to Scene 47-
                jump v16s47

        else: # -if partner is on baby duty
            
            scene v16s81_5 # FPP View of MC's bed [APES DORM ROOM]
            with dissolve

            u "(One peaceful night of sleep, coming up!)"

            scene v16s81_6 # TPP Show MC getting into bed [APES DORM ROOM]
            with dissolve

            pause 0.75

            scene v16s81_7 # TPP MC in bed, light's off, his eyes look heavy as he drifts off to sleep [APES DORM ROOM]
            with dissolve

            pause 0.75

            jump v16s50 # -Transition to Scene 50-
    
    else: # Wolf Dorm room 

        scene v16s81_8 # TPP Show MC entering his room in his fancy homecoming suit [WOLF DORM ROOM]
        with dissolve

        pause 0.75

        scene v16s81_9 # TPP Show MC taking off his fancy suit [WOLF DORM ROOM]
        with dissolve

        pause 0.75

        if v16s27_mc_baby_schedule["friday"] == BabyDuty.ALONE or v16s27_mc_baby_schedule["friday"] == BabyDuty.WITH_PARTNER: 
            
            scene v16s81_10 # TPP Show MC (slight frown, eyes closed, mouth closed) looking slightly up as if deeply sighing [WOLF DORM ROOM]
            with dissolve

            u "(Daddy duty begins...)"

            scene v16s81_9a # TPP Same angle as 2, MC getting into his normal clothes (in header) [WOLF DORM ROOM]
            with dissolve

            pause 0.75

            scene v16s81_11 # TPP Show MC leaving his room [WOLF DORM ROOM]
            with dissolve

            pause 0.75

            # if v16s27_mc_baby_duty_night == 4: # -if on baby duty alone, transition to Scene 45-
            if v16s27_mc_baby_schedule["friday"] == BabyDuty.ALONE:
                jump v16s45

            else: # -if sharing baby duty, transition to Scene 47-
                jump v16s47

        else: # -if partner is on baby duty
            
            scene v16s81_12 # FPP View of MC's bed [WOLF DORM ROOM]
            with dissolve

            u "(One peaceful night of sleep, coming up!)"

            scene v16s81_13 # TPP Show MC getting into bed [WOLF DORM ROOM]
            with dissolve

            pause 0.75

            scene v16s81_14 # TPP MC in bed, light's off, his eyes look heavy as he drifts off to sleep [WOLF DORM ROOM]
            with dissolve

            pause 0.75

            jump v16s50 # -Transition to Scene 50-