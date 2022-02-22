# SCENE 42: Transition MC changes into normal clothes
# Locations: Bedroom
# Characters: MC (Outfit: 9)
# Time: Wednesday


# THE INSTRUCTIONS FOR THIS SCENE WERE COMPLETELY INCOMPREHENSIBLE. I DID MY BEST TO FIGURE OUT WHAT THE WRITER WANTED

label v16s42: # 42) MC changes into normal clothes

    $ v16s42_kiwiiPost1 = KiwiiPost(Autumn, "Autumn holding Oscar the dog inside the dog shelter, you can see the re-opening decorations in the background, Oscar is making a funny face if possible", _("Tomorrow is our biggest day of the year: Our grand re-opening! Stop by to drop off a small donation to support our non-profit and spend some time with our babies! *The animal shown is currently available for adoption* <3"), numberLikes=842)
    $ v16s42_kiwiiPost1.new_comment(Lindsey, "OMG! I'm so upset that I can't make it... I probably would end up leaving with a pup!", numberLikes=98)
    $ v16s42_kiwiiPost1.new_comment(Chris, "Oh... my... I think the Wolves need a mascot!", numberLikes=154)
    $ v16s42_kiwiiPost1.new_comment(Sebastian, "You know damn well I'd be the one cleaning up after it... But hell yeah, let's do it!", numberLikes=115)
    $ v16s42_kiwiiPost1.new_comment(Lauren, "OMG, I think I know the perfect dog for you guys.", numberLikes=127)
    $ v16s42_kiwiiPost1.add_reply("I'll be there! Can't wait :)", numberLikes=54)
    $ v16s42_kiwiiPost1.new_comment(Autumn, "See you then! :)", numberLikes=124)
    $ v16s42_kiwiiPost1.add_reply("You're supporting this, Lauren?! Lol", mentions=Lauren, numberLikes=92)
    $ v16s42_kiwiiPost1.new_comment(Lauren, "Fully! <3", numberLikes=128)


    if v16_aubrey_date: # PLACEHOLDER VARIABLE # IF Transitioning from Scene 41 [Checkpoint 1.1]
        scene v16s42_1 # TPP Show MC entering his room in fancy clothes (outfit 6)
        with dissolve

        pause 0.75
    

    else:
        scene v16s42_2 # TPP Show MC entering his room in normal clothes
        with dissolve

        pause 0.75


    if v16_baby_duty: # PLACEHOLDER VARIABLE # IF on baby duty alone or sharing baby duty
        if v16_aubrey_date: # PLACEHOLDER VARIABLE
            scene v16s42_3 # TPP MC changes into regular clothes (outfit 9) from fancy clothes (outfit 6)
            with dissolve

            pause 0.75


        scene v16s42_4 # TPP Show MC leaving his room
        with dissolve

        pause 0.75


        if v16_baby_duty_alone: # PLACEHOLDER VARIABLE # IF on baby duty alone, transition to Scene 45-
            jump v16s45
        
        else: # IF sharing baby duty, transition to Scene 47-
            jump v16s47


    else: # IF partner is on baby duty alone
        if v16_aubrey_date: # PLACEHOLDER VARIABLE
            scene v16s42_5 # TPP Show MC getting undressed for bed from fancy clothes (outfit 6)
            with dissolve

            pause 0.75

        else:
            scene v16s42_6 # TPP Show MC getting undressed for bed from normal clothes
            with dissolve

            pause 0.75


    jump v16s50 # -Transition to Scene 50