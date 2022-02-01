# SCENE 3: Dean comes to Apes about posted image
# Locations: Apes' House
# Characters: DEAN (Outfit: 1), MC (Outfit: 5), RYAN (Outfit: 1), CAMERON (Outfit: 2), GRAYSON (Outfit: 3)
# Time: Friday

label v15s3: # 3) Dean comes to Apes about posted image
    play music "music/v15/Track Scene 3.mp3" fadein 2

    scene v15s3_1 # TPP Show MC, now dressed, entering the main lounge of the Apes' House
    with fade

    pause 0.75
    
    scene v15s3_2 # FPP Show MCs view of Grayson, Cameron, and Ryan sitting on the couch in the lounge, looking awkward and uncomfortable
    with fade

    pause 0.75

    scene v15s3_3 # FPP MC sees the dean standing in front of the couch in the Apes' lounge. She looks angry, looking at MC, mouth open
    with dissolve

    de "Oh look, and here's another member of the Ape clan. Come and sit down, [name]."

    scene v15s3_2a # FPP Same angle as 2, Grayson, Cameron, and Ryan looking up at MC and making room for him on the couch
    with dissolve

    u "(Oh, shit... Too late to turn around and run, I guess.)"

    scene v15s3_4 # TPP Straight-on shot of MC sits on the couch next to Grayson, Cameron, and Ryan - they all look awkward, like this: https://i.pinimg.com/originals/a4/56/26/a45626af21728d79a410ea6f63c5acde.jpg
    with dissolve

    u "(I think I have an idea on what this is about.)"

    scene v15s3_5 # FPP Dean looking at MC, she has an angry expression, mouth open
    with dissolve

    de "I was just saying to Grayson here, that this fraternity is his responsibility."

    scene v15s3_5a # FPP Same angle as 5, Dean looking at Grayson and pointing her finger at him, mouth open
    with dissolve

    de "What happens under this roof is your responsibility."

    scene v15s3_5b # FPP Same angle as 5, Dean standing back and looking at the whole group, hands on her hips, mouth open
    with dissolve

    de "And posting indecent photos of female students, is certainly something that this whole house will be punished for."

    scene v15s3_6 # FPP Show Ryan, looking shocked and scared, looking at dean with mouth open
    with dissolve

    ry "What?!"

    scene v15s3_7 # FPP Show Cameron looking at Grayson, laughing with mouth open
    with dissolve

    ca "Ha, nice one, Gray..."

    scene v15s3_5a
    with dissolve

    de "If this type of behavior becomes a habit, Grayson, the Apes will be shut down completely. That's how serious you need to take this."

    scene v15s3_5b
    with dissolve

    de "I'm making a note on your permanent record. All of you, in fact."

    scene v15s3_8 # FPP Show Grayson looking up at Dean, worried/remorseful expression, mouth open
    with dissolve

    gr "I said I'm sorry, Mrs. Harrison. It was just a stupid prank-"

    scene v15s3_5a
    with dissolve

    de "No matter what your intention was, it's bullying."

    scene v15s3_8
    with dissolve

    gr "Again, I'm sorry. I- We obviously didn't think this through and sadly we made a bad decision as a group."

    scene v15s3_8a # FPP Same angle as 8, Grayson looking down, worried expression, mouth closed
    with dissolve

    u "(He's doing his best to sound sincere, and to spread the blame...)"

    scene v15s3_5b
    with dissolve

    de "An apology is just a start."

    de "What I need from you all right now, is to delete the posts and the photos from your phones."

    scene v15s3_4
    with dissolve

    pause 0.75

    scene v15s3_5c # FPP Same angle as 5, Dean with her hand on her hips shouting at the group
    with dissolve

    de "NOW!"

    scene v15s3_4a # TPP Same angle as 4. Grayson, Cameron, and Ryan all have their phones out, MC does not, is just sitting awkwardly
    with dissolve

    de "Oh, yes. I did hear that [name] was the only one smart enough to make the decision of not posting the photo."

    scene v15s3_5
    with dissolve

    de "At least there is one of you who has some integrity..."

    # -if MC tried to stand up for Chloe (remember variable for future dean scene with Chloe)
    if v14s41a_standup:
        scene v15s3_6a # FPP Same angle as 6, Ryan holding his phone but looking at MC, neutral expression, mouth open
        with dissolve

        ry "I knew we should've listened to you..."

    else: # -if MC did not stand up for Chloe
        scene v15s3_6a
        with dissolve

        ry "Way to be a team player..."

    # -regardless-
    scene v15s3_5
    with dissolve

    de "Well done, [name]. You're excused from the punishment."

    scene v15s3_8b # FPP Same angle as 8, Grayson looking at MC with an angry, "fuck you" expression
    with dissolve

    u "(Jeez, thanks for calling me out, Harrison!)"

    if v14_PenelopePartner:
        $ v14s43b_kiwiiPost3.remove_post()
    else:
        $ v14s43b_kiwiiPost6.remove_post()

    scene v15s3_7a # FPP Same angle as 7, Cameron looking up at dean, phone still in his hand, neutral expression, mouth open
    with dissolve

    ca "Done."

    if v14_PenelopePartner:
        $ v14s43b_kiwiiPost1.remove_post()
    else:
        $ v14s43b_kiwiiPost4.remove_post()

    scene v15s3_8
    with dissolve

    gr "Deleted."

    if v14_PenelopePartner:
        $ v14s43b_kiwiiPost2.remove_post()
    else:
        $ v14s43b_kiwiiPost5.remove_post()

    scene v15s3_6a
    with dissolve

    ry "Yeah, it's gone now."

    scene v15s3_5b
    with dissolve

    de "Very well. Make sure you message all the other Apes to do the same immediately."

    scene v15s3_6b # FPP Same angle as 6, Ryan looking at the Dean with a worried or scared expression, mouth open
    with dissolve

    ry "Y-yes, ma'am."

    scene v15s3_5b
    with dissolve

    de "I'm going to be watching you all very closely from now on..."

    scene v15s3_5a
    with dissolve

    de "The Apes' reputation is also the reputation of SVC. We want it to have a good reputation. Remember that."

    scene v15s3_9 # FPP Show dean walking out the front door of the Apes' house
    with dissolve

    pause 0.75

    scene v15s3_8c # FPP Same angle as 8, Grayson looking toward front door, laughing, mouth open
    with dissolve

    gr "Our reputation is exactly where it needs to be! *Laughs*"

    scene v15s3_6c # FPP Same angle as 6, Ryan looking down at his chest, worried expression, mouth open
    with dissolve

    ry "That sucked."

    scene v15s3_99
    with dissolve

    gr "It doesn't matter. The posts have already done the damage. We fucking did it, boys!"

    scene v15s3_6c
    with dissolve

    ry "What about the note on our permanent record?"

    scene v15s3_99
    with dissolve

    gr "That doesn't mean anything, man. Come on!"

    scene v15s3_7
    with dissolve

    ca "Yeah, it's not even worth thinking about."

    scene v15s3_10 # FPP Show Grayson and Cameron walking out of the room
    with dissolve

    u "This is what we get for joining the Apes. *Chuckles*"

    scene v15s3_6d # FPP Same as 6a, no phone
    with dissolve

    ry "You mean me? This is what I get for joining the Apes. You don't get shit."

    # -If MC tried to stop them from posting

    menu:
        "It's not my fault":
            scene v15s3_6e
            with dissolve

            u "Come on man, this isn't my fault."

            if v14s41a_standup:
                u "I tried to stop-"

            scene v15s3_6d
            with dissolve

            ry "Maybe not, but it sure doesn't matter now, does it?"

        "I'm sorry":
            scene v15s3_6e
            with dissolve

            u "Ryan, look, I'm sorry."

            if v14s41a_standup:
                u "I tried to stop-"

            scene v15s3_6d
            with dissolve

            ry "You know what, [name]? It doesn't fucking matter."

    scene v15s3_6e
    with dissolve

    u "*Sighs*"

    # -regardless-
    scene v15s3_4b # TPP Same angle as 4, Grayson and Cameron are gone, Ryan looks worried and is looking down, MC is getting up off the couch
    with dissolve

    pause 0.75

    scene v15s3_11 # TPP Show MC leaving out the front door of the Apes' house
    with dissolve

    u "(I'll just go check on Autumn at the shelter...)"

    stop music fadeout 3

    jump v15s4