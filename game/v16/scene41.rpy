# SCENE 41: Transition MC goes home dressed up
# Locations: Street
# Characters: MC (Outfit: DATE NIGHT OUTFIT)
# Time: Wednesday

label v16s41: # MC goes home dressed up    
    if v16s39_fr_aubrey_date_points >= 4 and aubrey.relationship < Relationship.TAMED: # TODO: Variable # IF failed the date & lost AubreyTamed
        scene v16s41_1 # TPP MC walking down the street looking sad and upset
        with dissolve

        u "(Well, that could've gone a whole lot better... I guess there's nothing I can do about it now. If only life had a replay button...)"

    else: # IF MC had a successful date
        scene v16s41_2 # TPP MC Walking down the street with a huge grin
        with dissolve

        u "(Aubrey is my girlfriend... Aubrey is my fucking girlfriend! Haha!)"

        # IF mc is dating chloe, lauren AND aubrey (all three GF variables)
        if (lauren.relationship >= Relationship.GIRLFRIEND and chloe.relationship >= Relationship.GIRLFRIEND) and aubrey.relationship >= Relationship.TAMED:
            scene v16s41_3 # TPP Another angle of walking down the street, MC looking happy, but a little nervous
            with dissolve

            u "(And then there were three... What am I doing out here? *Laughs* I need to start being extra careful around my ladies...)"

        # IF mc is dating chloe OR Lauren, and now also aubrey (not both chloe and lauren, only one of them, 2 GF variables total) 
        elif aubrey.relationship >= Relationship.TAMED and (lauren.relationship >= Relationship.GIRLFRIEND or chloe.relationship >= Relationship.GIRLFRIEND):
            scene v16s41_3
            with dissolve

            u "(Two girlfriends... Now I'm just asking for trouble, haha! *Sighs*)"

    jump v16s42 # -Transition to Scene 42-