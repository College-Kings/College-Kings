# SCENE 7: MC vs Imre (Apes)
# Locations: Warehouse
# Characters: MC (Outfit 7),Josh (Outfit 2),Ryan (Outfit 2),Imre (Outfit 4),Grayson (Outfit 3)
# Time: Saturday Night
label v10_mc_vs_imre_fight:
    scene v10mvi1 # FPP. Show ryan and grayson near ring, Ryan Mouth open Grayson mouth closed
    with dissolve
    ry "Hey man real quick. I'm not saying I think you would, but I know you and Imre are friends and have been close since you started college..."

    ry "Just don't let that get in the middle of this fight."

    scene v10mvi1a # FPP. Same camera as v10mvi1, Show Ryan and Grayson near ring,ryan mouth closed Grayson mouth closed
    with dissolve

    u "Just beacuse we're-"

    scene v10mvi1b # FPP. Same camera as v10mvr1, Show ryan and Grayson near ring, ryan mouth closed Grayson mouth open
    with dissolve

    gr "Don't even start with all the sappy shit! You better destroy his ass!"

    scene v10mvr2 # Ignore this render, reused from scene 6
    with dissolve

    jo "*Loud whipser* Hey, I got some plans tonight. How much longer is-"

    scene v10mvi1b
    with dissolve

    gr "Bro chill the fuck out, we're ready!"

    scene v10mvi1
    with dissolve

    ry "Do it for the Apes man."

    scene v10mvi1a
    with dissolve

    u "You got it."

    scene v10mvr3 #Ignore this render, reused from scene 6
    with dissolve

    jo "Looks like our fighters are ready!"

    scene v10mvi2 # TPP. Show josh in the centre of the ring MC and Imre next to josh either side, Josh mouth closed, mc mouth closed, imre mouth open
    with dissolve

    imre "Ready to get your ass kicked?"

    menu:
        "Fight Imre":
            scene v10mvi3 # FPP. Show Imre infront of camera in ring, mouth closed, hands raised ready to fight.
            with dissolve

            u "You're going down tonight."

            jo "Same rules as before, just get it guys!"

            # -Manual Fight-

        "Don't Fight":
            scene v10mvi3 # FPP. Show Imre infront of camera in ring, mouth closed, hands raised ready to fight.
            with dissolve

            u "I don't think I can do this. I- I... I'm sorry guys."

            scene v10mvi4 # FPP. Show Close up from ring of Ryan and grayson stood watching, Ryan mouth open, Grayson mouth closed
            with dissolve
            ry "What the fuck did I just say?! I literally just-"

            scene v10mvi4a # FPP. Show Close up from ring of Ryan and grayson stood watching, Ryan mouth closed, Grayson mouth open
            with dissolve

            gr "Fucking pussy, go fight that bitch or you're sleeping outside tonight!"

            scene v10mvi3a # FPP. Same Camera as v10mvi3, Show Imre infront of camera in ring, mouth open, hands raised ready to fight.
            with dissolve

            imre "Hahaha, pussy."

            scene v10mvi3
            with dissolve

            u "I can't, I just can't."

            jump v10_avoid_fight

    # -Transition to Scene 8-
