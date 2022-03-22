# SCENE 49a: MC leaves Chicks house
# Locations: Chicks Sorority House
# Characters: MC (Outfit: 9)
# Time: Wed Night

label v16s49a:
    scene v16s49a_1 # TPP. MC (slight smile, mouth closed) exits the chicks house front door
    with dissolve

    pause 0.75

    if v16s27_parent_chloe and v16s48_chloe_throws_baby: # -if parent with Chloe and she threw baby out the window
        scene v16s49a_2 # FPP. Show just the baby doll on the ground in the grass
        with dissolve

        u "(Sorry, [v16_baby_name]... Mommy didn't mean it... Well, she did kind of mean it, but- *Sighs*)"

        scene v16s49a_1a # TPP. MC has turned his back to the render and is inside of the doorway, holding the baby doll
        with dissolve

        pause 0.75

        scene v16s49a_2a # FPP. Show just the baby doll sitting on a small side table just inside the doorway, next to the door, from the entrances view
        with dissolve

        pause 0.75

    else: # -if partnered with Nora
        scene v16s49a_1b # TPP. MC (slight smile, mouth closed) walks away from the house, the chicks front door is closed
        with dissolve

        u "(Nora was a natural with the baby. She's going to be an awesome mom one day. No surprises there, to be honest. *Laughs*)"

    if v16s27_parent_chloe: # -if partnered with Chloe
        scene v16s49a_1
        with dissolve

        u "(Reminder to never let Chloe babysit!)"

        if "v16_chloe" in sceneList: # -if MC also had sex with Chloe         ####VARIABLE NEEDS TO BE ADDED TO SCENE 48 FOR CHLOE AND MC HAVING SEX!###
            scene v16s49a_1b
            with dissolve

            u "(But, I have to admit... the sex is amazing when she's angry. I've got to get her pissed off more often, haha!)"

    scene v16s49a_3 # TPP. Show MC (slight smile, mouth closed) walking away from the house on the sidewalk
    with dissolve

    pause 0.75

    # Set v16s50a_dotw to Thursday for s50a
    $ v16s50a_dotw = 5
    jump v16s50a