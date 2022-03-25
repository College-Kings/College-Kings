# SCENE 20: Amber Living Room Free Roam (Single Screen)
# Locations: Amber's Living Room
# Characters: MC (Outfit: 5)
# Time: Night
# Render Count: 17 Renders 4 Call Screens 1 clean background call screen with twazzlers present and 1 without. 1 dirty background call screen with twazzlers present and 1 without. 21 Total

label v16s20:
    if v14_amber_clean:
        jump v16s20_amber_clean

    else:
        jump v16s20_amber_dirty

label v16s20_amber_clean: # -if AmberSober, the room is fairly neat
    scene v16s20_1 # FPP. the room is fairly neat In the free roam, we can select Unpaid bills, which are on the coffee table. Open laptop, which is sat on the couch. Photos, which are on the wall. Twazzlers candy (same as we used in v14orv15), which is on the floor beside the couch. Phone charger, which is on the floor next to the plant pot. Selecting Phone charger will end the free roam- 
    with dissolve

    u "(Hmm, I could have a little look around first. Learn a little bit more about Amber. There's the phone charger though. She is in need after all...)"

    label v16s20_amber_living_room_twazzlers: # -if Twazzlers candy
        $ freeroam16.add("twazzlers")

        scene v16s20_2 # FPP. A close up shot of the Twazzlers in the location of the room from the call screen (REUSED: CANNOT INCLUDE TRASH).
        with dissolve

        u "(Mmm, Twazzlers. She might appreciate a snack...)"

        scene v16s20_2
        with dissolve

        menu:
            "Take the Twazzlers":
                $ v16s20_take_twazzlers = True

                scene v16s20_2
                with dissolve

                u "(I'm just the most thoughtful guy, aren't I?)"

                call screen v16s20_amber_living_room_twazzler_clean # same entire background as the clean scene, except this render is missing the twazzlers (REUSED: CANNOT INCLUDE TRASH).

            "Leave them":
                scene v16s20_2
                with dissolve

                u "(Nah, maybe she didn't bring them for a reason.)"

                call screen v16s20_amber_living_room # -Return to free roam-

    label v16s20_amber_living_room_unpaid_bills: # -if Unpaid Bills
        $ freeroam16.add("bills")

        scene v16s20_3 # FPP. Close up shot of bills. A big red stamp on the top one: "OVERDUE" (REUSED: CANNOT INCLUDE TRASH).
        with dissolve

        u "(Why does Amber have unpaid bills? I thought she was earning good money...)"

        if v16s20_take_twazzlers:
            call screen v16s20_amber_living_room_twazzler_clean

        else:
            call screen v16s20_amber_living_room

    label v16s20_amber_living_room_laptop: # -if Open Laptop
        $ freeroam16.add("laptop")

        scene v16s20_4 # FPP. Close up shot of just the laptop and the screen (REUSED: CANNOT INCLUDE TRASH).
        with dissolve

        pause 0.75

        scene v16s20_5 # FPP. Close up shot of Mc pressing the touchpad of the laptop with a finger (REUSED: CANNOT INCLUDE TRASH).
        with dissolve

        pause 0.75

        scene v16s20_6 # FPP. On the screen is the image of a man and woman wearing skimpy, tight, police uniforms, MC still has a finger on the touchpad
        with dissolve

        u "(No password? It's like she's begging me to snoop through her computer ...)"

        scene v16s20_7 # FPP. "Cop & Thief erotic fan fiction." is listed as a title in Bold Letters across the screen (REUSED: CANNOT INCLUDE TRASH).
        with dissolve

        u "(And I'm not disappointed, haha. Cop & Thief erotic fan fiction. Great title! What the hell is Amber reading?)"

        scene v16s20_8 # FPP. Show just MC's face and neck wide eyed and smiling.
        with dissolve

        u "(\"Eric removed Alicia's handcuffs and, much to her surprise, he pulled out his lengthy baton, asking her to grasp it. Then Eric began to gently spank her begging ass with it...)"

        scene v16s20_5
        with dissolve

        u "*Laughs* (I think I've read enough of that.)"

        if v16s20_take_twazzlers:
            call screen v16s20_amber_living_room_twazzler_clean

        else:
            call screen v16s20_amber_living_room

    label v16s20_amber_living_room_photos: # -if Photos
        $ freeroam16.add("photos")

        scene v16s20_9 # FPP. There are three photos: One with Amber, Kim & Josh. One with Amber and her young brother, Damian. One of young Amber playing violin shown from left to right.
        with dissolve

        pause 0.75

        scene v16s20_10 # FPP. Close-up shot of the photo of the One with Amber, Kim & Josh. 
        with dissolve

        u "(Well, I recognize Kim and Josh.)" 

        scene v16s20_11 # FPP. Close-up shot of the photo of the One with Amber and her young brother, Damian. 
        with dissolve

        u "(Not sure who the kid is with Amber in the other photo though.)"

        scene v16s20_12 # FPP. Close-up shot of the photo of the One of young Amber playing violin-
        with dissolve

        u "(And is that little Amber playing violin? Haha, maybe I should ask her to play for me sometime.)"

        scene v16s20_9
        with dissolve

        u "(I should do this more often. I feel like a detective, heh. .)"

        if v16s20_take_twazzlers:
            call screen v16s20_amber_living_room_twazzler_clean

        else:
            call screen v16s20_amber_living_room

    label v16s20_amber_living_room_phone_charger: # -if Phone charger (Ends Free Roam)
        $ freeroam16.add("charger")

        scene v16s20_13 # FPP. A close up shot of the phone charger in the location of the room from the call screen (REUSED: CANNOT INCLUDE TRASH).
        with dissolve

        u "(Here it is! I bet her phone's dead by now. She'll be so desperate for this!)"

        if v16s20_take_twazzlers:
            scene v16s20_14 # FPP. A close up shot of the phone charger in Mc's hand (REUSED: CANNOT INCLUDE TRASH).
            with dissolve

            u "Alright, that's everything. Let's head out!"

            call screen v16s20_end

        else:
            scene v16s20_14
            with dissolve

            u "Alright, I got what I came for."

            call screen v16s20_end

label v16s20_amber_dirty: # -if AmberDrugs, the room is messier with some beer bottles, pizza box, etc, but clickable items are in exactly the same places as AmberSober
    scene v16s20_1a # FPP. same as v16s20_1 the room is messier with some beer bottles, pizza box, etc, but clickable items are in exactly the same places as AmberSober
    with dissolve

    u "(Hmm, I could have a little look around first. Learn a little bit more about Amber. There's the phone charger though. She is in need after all...)"

    label v16s20_amber_living_room_twazzlers2: # -if Twazzlers candy
        $ freeroam16.add("twazzlers")

        scene v16s20_2
        with dissolve

        u "(Mmm, Twazzlers. She might appreciate a snack...)"

        scene v16s20_2
        with dissolve

        menu:
            "Take the Twazzlers":
                $ v16s20_take_twazzlers = True

                scene v16s20_2
                with dissolve

                u "(I'm just the most thoughtful guy, aren't I?)"

                call screen v16s20_amber_living_room_twazzler_dirty

            "Leave them":
                scene v16s20_2
                with dissolve

                u "(Nah, maybe she didn't bring them for a reason.)"

                call screen v16s20_amber_living_room

    label v16s20_amber_living_room_unpaid_bills2: # -if Unpaid Bills
        $ freeroam16.add("bills")

        scene v16s20_3
        with dissolve

        u "(Why does Amber have unpaid bills? I thought she was earning good money...)"

        if v16s20_take_twazzlers:
            call screen v16s20_amber_living_room_twazzler_dirty

        else:
            call screen v16s20_amber_living_room

    label v16s20_amber_living_room_laptop2: # -if Open Laptop
        $ freeroam16.add("laptop")

        scene v16s20_4
        with dissolve

        pause 0.75

        scene v16s20_5
        with dissolve

        pause 0.75

        scene v16s20_6
        with dissolve

        u "(No password? It's like she's begging me to snoop through her computer ...)"

        scene v16s20_7
        with dissolve

        u "(And I'm not disappointed, haha. Cop & Thief erotic fan fiction. Great title! What the hell is Amber reading?)"

        scene v16s20_8
        with dissolve

        u "(\"Eric removed Alicia's handcuffs and, much to her surprise, he pulled out his lengthy baton, asking her to grasp it. Then Eric began to gently spank her begging ass with it...)"

        scene v16s20_5
        with dissolve

        u "*Laughs* (I think I've read enough of that.)"

        if v16s20_take_twazzlers:
            call screen v16s20_amber_living_room_twazzler_dirty

        else:
            call screen v16s20_amber_living_room

    label v16s20_amber_living_room_photos2: # -if Photos
        $ freeroam16.add("photos")

        scene v16s20_9
        with dissolve

        pause 0.75

        scene v16s20_10
        with dissolve

        u "(Well, I recognize Kim and Josh.)" 

        scene v16s20_11
        with dissolve

        u "(Not sure who the kid is with Amber in the other photo though.)"

        scene v16s20_12
        with dissolve

        u "(And is that little Amber playing violin? Haha, maybe I should ask her to play for me sometime.)"

        scene v16s20_9
        with dissolve

        u "(I should do this more often. I feel like a detective, heh. .)"

        if v16s20_take_twazzlers:
            call screen v16s20_amber_living_room_twazzler_dirty

        else:
            call screen v16s20_amber_living_room # -Return to free roam-

    label v16s20_amber_living_room_phone_charger2: # -if Phone charger (Ends Free Roam)
        $ freeroam16.add("charger")

        scene v16s20_13
        with dissolve

        u "(Here it is! I bet her phone's dead by now. She'll be so desperate for this!)"

        if v16s20_take_twazzlers:
            scene v16s20_14
            with dissolve

            u "Alright, that's everything. Let's head out!"

            call screen v16s20_end

        else:
            scene v16s20_14
            with dissolve

            u "Alright got what I came for."

            call screen v16s20_end

label v16s20_end:
    scene v16s20_15 # FPP Show MC turning the lights off as he leaves the house, slight smile, mouth is closed
    with dissolve

    pause 0.75

    scene v16s20_16 # FPP. Show MC outside of the house placing the key back under the mat, slight smile, mouth is closed
    with dissolve

    pause 0.75

    scene v16s20_17 # FPP. Show MC walking away from Ambers House, slight smile, mouth is closed
    with dissolve

    pause 0.75

    jump v16s21