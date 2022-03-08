# SCENE 42: Transition MC changes into normal clothes
# Locations: APE Bedroom, WOLF Bedroom 
# Characters: MC (Outfit: 9)
# Time: Wednesday

# THE INSTRUCTIONS FOR THIS SCENE WERE COMPLETELY INCOMPREHENSIBLE. I DID MY BEST TO FIGURE OUT WHAT THE WRITER WANTED

label v16s42: # 42) MC changes into normal clothes
    $ v16s42_kiwiiPost1 = KiwiiPost(Autumn, "Autumn holding Oscar the dog inside the dog shelter, you can see the re-opening decorations in the background, Oscar is making a funny face if possible", "Tomorrow is our biggest day of the year: Our grand re-opening! Stop by to drop off a small donation to support our non-profit and spend some time with our babies! *The animal shown is currently available for adoption* <3", numberLikes=842)
    $ v16s42_kiwiiPost1.new_comment(Lindsey, "OMG! I'm so upset that I can't make it... I probably would end up leaving with a pup!", numberLikes=98, force_send=True)
    $ v16s42_kiwiiPost1.new_comment(Chris, "Oh... my... I think the Wolves need a mascot!", numberLikes=154, force_send=True)
    $ v16s42_kiwiiPost1.new_comment(Sebastian, "You know damn well I'd be the one cleaning up after it... But hell yeah, let's do it!", numberLikes=115, force_send=True)
    $ v16s42_kiwiiPost1.new_comment(Lauren, "OMG, I think I know the perfect dog for you guys.", numberLikes=127, force_send=True)
    $ v16s42_kiwiiPost1.add_reply("I'll be there! Can't wait :)", numberLikes=54)
    $ v16s42_kiwiiPost1.new_comment(Autumn, "See you then! :)", numberLikes=124, force_send=True)
    $ v16s42_kiwiiPost1.add_reply("You're supporting this, Lauren?! Lol", mentions=Lauren, numberLikes=92)
    $ v16s42_kiwiiPost1.new_comment(Lauren, "Fully! <3", numberLikes=128, force_send=True)

    if v16s25a_date_with_aubrey: # TODO: Variable PLACEHOLDER VARIABLE # IF Transitioning from Scene 41 [Checkpoint 1.1]
        
        if not joinwolves:
            scene v16s42_1 # TPP Show MC entering his room in fancy clothes (DATE NIGHT CLOTHES s41) [APE ROOM]
            with dissolve

        else:
            scene v16s42_1a # TPP Show MC entering his room in fancy clothes (DATE NIGHT CLOTHES s41) [WOLF ROOM]
            with dissolve

        pause 0.75 
        
    else:
        if not joinwolves:
            scene v16s42_2 # TPP Show MC entering his room in normal clothes [APE ROOM]
            with dissolve
        else:
            scene v16s42_2a # TPP Show MC entering his room in normal clothes [WOLF ROOM]
            with dissolve

        pause 0.75

    if (1 & v16s27_mc_baby_duty_night == 1) or (0x10 & v16s27_mc_baby_duty_night = 0x10): # IF on baby duty alone or sharing baby duty 1 = alone_duty_on_Wed, 0x10 = shared_duty_on_Wed
        if v16s25a_date_with_aubrey: # PLACEHOLDER VARIABLE
            if not joinwolves:
                scene v16s42_1b # TPP Show MC Taking fancy clothes shirt off [APE ROOM]
                with dissolve

                pause 0.75

                scene v16s42_1c # TPP Show MC standing in boxers/underwear [APE ROOM]
                with dissolve

                pause 0.75

                scene v16s42_1d # TPP MC wearing pants from (outfit 9) [APE ROOM]
                with dissolve

                pause 0.75

                scene v16s42_1e # TPP MC wearing shirt and pants from (outfit 9) [APE ROOM]
                with dissolve

                pause 0.75

                scene v16s42_1f # TPP Show MC leaving his room in outfit 9 [APE ROOM]
                with dissolve

            else:
                scene v16s42_2b # TPP Show MC Taking fancy clothes shirt off [WOLF ROOM]
                with dissolve

                pause 0.75

                scene v16s42_2c # TPP Show MC standing in boxers/underwear [WOLF ROOM]
                with dissolve

                pause 0.75

                scene v16s42_2d # TPP MC wearing pants from (outfit 9) [WOLF ROOM]
                with dissolve

                pause 0.75

                scene v16s42_2e # TPP MC wearing shirt and pants from (outfit 9) [WOLF ROOM]
                with dissolve

                pause 0.75

                scene v16s42_2f # TPP Show MC leaving his room in outfit 9 [WOLF ROOM]
                with dissolve

            pause 0.75

        if 1 & v16s27_mc_baby_duty_night == 1: # PLACEHOLDER VARIABLE # IF on baby duty alone on Wed, transition to Scene 45-
        
            jump v16s45
        
        else: # IF sharing baby duty, transition to Scene 47-
            
            jump v16s47

    else: # IF partner is on baby duty alone
        if v16s25a_date_with_aubrey: # PLACEHOLDER VARIABLE
            if not joinwolves:
                scene v16s42_1b # TPP Show MC Taking fancy clothes shirt off [APE ROOM]
                with dissolve

                pause 0.75

                scene v16s42_1c # TPP Show MC standing in boxers/underwear [APE ROOM]
                with dissolve

            else:
                scene v16s42_2b # TPP Show MC Taking fancy clothes shirt off [WOLF ROOM]
                with dissolve

                pause 0.75

                scene v16s42_2c # TPP Show MC standing in boxers/underwear [WOLF ROOM]
                with dissolve

            pause 0.75

        else:
            if not joinwolves:
                scene v16s42_3 # TPP Show MC taking off shirt from outfit 9 (Exact same location as v16s42_1b so we can reuse v16s42_1c ) [APE ROOM]
                with dissolve

                scene v16s42_1c
                with dissolve

            else:
                scene v16s42_3a # TPP Show MC taking off shirt from outfit 9 (Exact same location as v16s42_2b so we can reuse v16s42_2c ) [WOLF ROOM]
                with dissolve

                scene v16s42_2c
                with dissolve
               
            pause 0.75

        if not joinwolves:
            scene v16s42_4 # TPP Show MC under the covers in his bed, phone on nightstand [APE ROOM]
            with dissolve
        else:
            scene v16s42_4a # TPP Show MC under the covers in his bed, phone on nightstand [WOLF ROOM]
            with dissolve
        
        pause 0.75

    jump v16s50 # -Transition to Scene 50