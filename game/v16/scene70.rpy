# SCENE 70: Transition Mc walks to Deans office
# Locations: School Hallway, Dean's Office Entrance
# Characters: PENELOPE (Outfit: 1), MC (Outfit: 5)
# Time: Friday Morning


label v16s70:

    if penelope.relationship == Relationship.LIKES and 0x20 & v16s27_mc_baby_duty_night != 0x20: # -if MC spent the night with Penelope From s68 -if PenelopeRS and MC is not on baby duty with partner, transition to Scene 69 -> 69a -> 70

        scene v16s70_2 # FPP. Show Penelope (slight smile, mouth is closed, looking at MC), Camera angle is from MC and Penelope walking side by side in the school hallway
        with dissolve

        u "I don't want to sound like a deadbeat dad, but it felt so good dropping off [v16_baby_name]."

        scene v16s70_2a # FPP. Show Penelope (slight smile, mouth is open, looking at MC), Camera angle is from MC and Penelope walking side by side in the school hallway
        with dissolve

        pe "*Laughs* Aw, that poor baby. It's been abandoned."

        scene v16s70_2
        with dissolve

        u "I'm sure it'll find a new father in about a day or two. *Laughs*"

        scene v16s70_1 # FPP. Show Penelope (slight smile, mouth is open, looking at MC) standing by the Dean's office door
        with dissolve

        pe "Well here we are"

    else: # -if MC did not spend the night with Penelope 

        scene v16s70_1
        with dissolve

        pe "Hey, thanks for coming. I wasn't too sure if I'd be able to handle this on my own."

        scene v16s70_1a # FPP. Show Penelope (slight smile, mouth is closed, looking at MC) standing by the Dean's office door
        with dissolve

        u "He's a chill dog. Like, a stoner almost."

        scene v16s70_1
        with dissolve

        pe "I know, but this is the Dean's dog. We can't fuck it up."

        scene v16s70_1a
        with dissolve

        u "Yeah, yeah, I get it. We can't kill the Dean's new dog. Noted."

        scene v16s70_1
        with dissolve

        pe "Great. I'm glad we're on the same page now. *Giggles*"

    # -Regardless of whether MC spent the night with Penelope-

    scene v16s70_1b # FPP. Show Penelope (slight smile, mouth is closed, looking at the door) knocking on the Dean's door
    with dissolve

    pause 0.75

    scene v16s70_1c # FPP. Show Penelope (slight smile, mouth is closed, looking at the door)
    with dissolve

    de "Yes, come in!"

    scene v16s70_3 # TPP. Penelope (slight smile, mouth is closed) and MC (slight smile, mouth is closed) enter the Dean's office
    with dissolve

    pause 0.75

    jump v16s71 # -Transition to Scene 71-