# SCENE 47: Transition Mc walks to the chicks house
# Locations: Chicks house
# Characters: CHLOE (Outfit: 3), MC (Outfit: 9), NORA (Outfit: 1)
# Time: Wednesday night

label v16s47: # 47) MC goes to the Chicks house
    play sound "sounds/knock.mp3"

    scene v16s47_1 # TPP Show MC knocking on the front door of the Chicks house
    with fade
    
    pause 0.75

    if v16s27_parent_chloe: # PLACEHOLDER VARIABLE # IF partnered with Chloe
        scene v16s47_2 # FPP Chloe (bored expression, mouth open) answering the door to the Chicks house
        with dissolve

        cl "Helloooo! Welcome to the house of enforced parenthood..."

        scene v16s47_2a # FPP Same angle as 2, Chloe (bored expression, mouth closed) at the door to the Chicks house
        with dissolve

        u "*Laughs* It's not that bad."

        scene v16s47_2
        with dissolve

        cl "We'll see."

        if chloe.relationship == Relationship.GIRLFRIEND: # TODO: Variable IF chloeGF
            scene v16s47_3 # TPP Show MC kissing Chloe on the cheek as he enters the Chicks house
            with dissolve

            pause 0.75

            scene v16s47_4 # TPP MC walking down the hall of the Chicks house, Chloe (smiling, mouth closed) visible behind him, looking at him walk away
            with dissolve
        
        else:
            scene v16s47_5 # TPP MC (slight smile, mouth closed) entering the Chicks house past Chloe (bored expression, mouth closed) as she closes the door
            with dissolve

        pause 0.75

        jump v16s48 # -if partner Chloe, transition to Scene 48-

    else: # IF partnered with Nora
        scene v16s47_6 # FPP Nora (smiling, mouth open) answering the door to the Chicks house. She is holding the baby doll like a real baby
        with dissolve

        no "Look who it is, [v16_baby]! It's your daddy!"

        scene v16s47_6a # FPP Same angle as 6. Nora (smiling, mouth closed) at the door to the chicks house, holding the baby doll
        with dissolve

        u "Oh dear, your mother has already gone insane and forgotten that you're made of plastic. *Laughs*"

        scene v16s47_6
        with dissolve

        no "*Chuckles* Screw you! It's fun to pretend for one night."

        if nora.relationship >= Relationship.FWB: # TODO: Variable VERIFY, SINCE RS NO LONGER MEANS ANYTHING ### ERROR: IF noraRS
            scene v16s47_3a # TPP Same angle as 3. Show MC kissing Nora on the cheek as he enters the Chicks house
            with dissolve

            pause 0.75

            scene v16s47_4a # TPP Same angle as 4. MC walking down the hall of the Chicks house, Nora (smiling, mouth closed) visible behind him, holding the baby doll, looking at him walk away
            with dissolve

        else:
            scene v16s47_5a # TPP Same angle as 5. MC (slight smile, mouth closed) entering the Chicks house past Nora (slight smile, mouth closed) as she holds the baby with one hand and closes the door with the other
            with dissolve

        pause 0.75

        jump v16s49 # -if partner Nora, transition to Scene 49-