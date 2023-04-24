# SCENE 15a: Lauren text rooming Riley
# Locations: Hotel Room
# Characters: MC (Outfit: 2), RILEY (Outfit: NAKED)
# Time: Night

init python:
    def v13s15a_Reply1():
        setattr(store, "v13_cuddle_lauren_text", True)
        lauren.messenger.newMessage("Yayy :)")

    def v13s15a_Reply2():
        lauren.messenger.newMessage("Aww okay, it's cool")
        lauren.messenger.addReply("Sorry babe, I'm just so tired.")
        lauren.messenger.newMessage("It's okay.")

label v13s15a:
    scene v13s15a_1 # TPP. Show MC walking into the room, it's dark inside, MC neutral expression, mouth closed
    with dissolve

    pause 0.75

    play music "music/v13/Track Scene 15.mp3" fadein 2

    scene v13s15a_2 # TPP. Show MC standing in front of the door, in the room, MC neutral expression, mouth closed, room is dark
    with dissolve

    pause 0.75

    u "(Oh shit, she's probably asleep. Gonna have to tiptoe in the dark.)"

    scene v13s15a_3 # TPP. Show MC walking tip toeing towards his bed, slightly scared, mouth closed
    with dissolve

    u "(I can't see a damn thing.)"

    scene v13s15a_4 # TPP. Close up of MC's foot hitting his bed (no shows)
    with vpunch

    u "*Whisper* Fuck!"

    scene v13s15a_5 # TPP. Riley laying in her bed, turning on the light, she's confused, mouth closed
    with dissolve

    pause 0.75

    scene v13s15a_6 # FPP. MC same positioning as v13s15a_4, looking at Riley, she's in her bed, under her covers, looking at MC, Riley slightly angry, mouth closed
    with dissolve

    u "I'm so sorry, Riley..."

    scene v13s15a_6a # FPP. Same as v13s15a_6, Riley slight smile, mouth open
    with dissolve

    ri "Don't be sorry, do better. I'm trying to sleep. *Chuckles*"

    scene v13s15a_6b # FPP. Same as v13s15a_6, Riley slight smile, mouth closed
    with dissolve

    u "You couldn't even say that with a straight face..."

    scene v13s15a_6c # FPP. Same as v13s15a_6, Riley slightly sad, mouth open
    with dissolve

    ri "It's hard to be mean to you when I've been... You know?"

    scene v13s15a_6d # FPP. Same as v13s15a_6c, Riley slightly sad, mouth closed
    with dissolve

    u "I told you, I'm not upset. I honestly forget about it all the time until you bring it up."

    scene v13s15a_6c
    with dissolve

    ri "It's because I still don't sit right with it..."

    ri "I wanna make sure I balance the scale, you know?"

    scene v13s15a_6d
    with dissolve

    u "I hear you."

    if CharacterService.is_girlfriend(lauren, Relationship.GIRLFRIEND) and not v11_lauren_caught_aubrey: #if healthy lauren relationship
        play sound "sounds/vibrate.mp3"

        scene v13s15a_7 # TPP. MC looking down at his phone, he is standing in same place as v13s15a_6, slightly surprised, mouth closed
        with dissolve

        u "(Kinda late for a text.)"

        $ lauren.messenger.newMessage("You up?", force_send=True)
        $ lauren.messenger.addReply("Yeah, wassup?")
        $ lauren.messenger.newMessage("Come cuddle with me? ;)")
        $ lauren.messenger.addReply("You don't have to ask me twice, omw", v13s15a_Reply1)
        $ lauren.messenger.addReply("I'm already asleep...", v13s15a_Reply2)

        scene v13s15a_8 # FPP. MC looking down at his phone, he is standing in same place as v13s15a_6
        with dissolve

        pause 0.75

        label v13s15a_PhoneContinueLauren:
            if lauren.messenger.replies:
                call screen phone
            if lauren.messenger.replies:
                u "(I should check my phone.)"
                jump v13s15a_PhoneContinueLauren

    if v13_cuddle_lauren_text:
        scene v13s15a_6b
        with dissolve

        u "Something just came up, I gotta dip. Later."

        scene v13s15a_6e # FPP. Same as v13s15a_6, Riley startled, mouth open
        with dissolve

        ri "Wait! [name]!"

        scene v13s15a_6f # FPP. Same as v13s15a_6, Riley sexy look, mouth closed
        with dissolve

        u "Yeah?"

        if config_censored:
            call screen censored_popup("v13s15a_nsfwSkipLabel1")

        scene v13s15a_6g # FPP. Same as v13s15a_6f, Riley sexy look, mouth open
        with dissolve

        ri "I know this is gonna be... blunt..."

        scene v13s15a_6h # FPP. Same as v13s15a_6g, Riley's blanket slightly showing a bit of her boob
        with dissolve

        ri "But, I was hoping I could pay you back tonight..."

        scene v13s15a_6i # FPP. Same as v13s15a_6h, Riley sexy looks, mouth closed
        with dissolve

        u "How so?"

        scene v13s15a_6h
        with dissolve

        ri "I was hoping you'd come over here..."

        scene v13s15a_6j # FPP. Same as v13s15a_6h, Riley in the motion of removing the blanket completely, sexy look, mouth open
        with dissolve

        ri "Find out."

        scene v13s15a_6k # FPP. Same as v13s15a_6j, Riley sexy look, mouth closed, blanket off, normal pose
        with dissolve

        u "Oh..."

        scene v13s15a_6l # FPP. Same as v13s15a_6k, Riley sexy look, mouth open
        with dissolve

        ri "So, gonna let me make it up to you?"

        scene v13s15a_6k
        with dissolve

        menu:
            "Stay with Riley":
                $ grant_achievement("gentlemen_prefer_gingers")
                u "Is that even a question?"

                scene v13s15a_9 # TPP. Show MC removing his pants, shirt already off, smiling, mouth closed
                with dissolve

                pause 0.75

                scene v13s15a_10 # TPP. Show MC getting on top of Riley, both smiling, mouths closed
                with dissolve

                pause 0.75

                scene v13s15a_11 # TPP. Show MC and Riley making out, MC on top of her, he's grabbing her boob
                with dissolve

                pause 0.75

                stop music fadeout 3

                jump v13s16a

            "Cuddle with Lauren":
                $ v13_cuddle_lauren = True

                scene v13s15a_6m # FPP. Same as v13s15a_6k, Riley slightly surprised, mouth closed
                with dissolve

                u "Very flattering, Riley. I mean... Very... Very flattering..."

                scene v13s15a_6n # FPP. Same as v13s15a_6m, Riley slight smile, mouth closed
                with dissolve

                u "But, I really do need to run... And as I said before, no need to pay me back. All is forgiven."

                scene v13s15a_6a
                with dissolve

                ri "Alrighty, then... I'll stop feeling guilty."

                scene v13s15a_6b
                with dissolve

                u "Good, have a good night, Riley."

                scene v13s15a_6a
                with dissolve

                ri "You too."

                scene v13s15a_12 # TPP. Show MC walking out of his room, slight smile, mouth closed
                with dissolve

                pause 0.75

                stop music fadeout 3

                jump v13s16

    else:
        scene v13s15a_6g
        with dissolve

        ri "[name]?"

        scene v13s15a_6f
        with dissolve

        u "Yeah?"

        scene v13s15a_6h
        with dissolve

        ri "I know this is gonna be blunt, but I was hoping I could pay you back tonight."

        scene v13s15a_6i
        with dissolve

        u "How so?"

        if config_censored:
            call screen censored_popup("v13s15a_nsfwSkipLabel1")

        scene v13s15a_6j
        with dissolve

        ri "I was hoping you'd come over here and fuck me."

        scene v13s15a_6k
        with dissolve

        u "Oh..."

        scene v13s15a_6l
        with dissolve

        ri "So, gonna let me make it up to you?"

        scene v13s15a_6k
        with dissolve

        menu:
            "Let Riley do it":
                u "Is that even a question?"

                scene v13s15a_9 
                with dissolve

                pause 0.75

                scene v13s15a_10 
                with dissolve

                pause 0.75

                scene v13s15a_11
                with dissolve

                pause 0.75

                stop music fadeout 3

                jump v13s16a

            "Go to sleep":
                scene v13s15a_6m
                with dissolve

                u "Very flattering, I mean very very flattering. But as I said before, no need to pay me back. All is forgiven and I don't want you doing that as a payback."

                scene v13s15a_6a
                with dissolve

                ri "Alrighty, I'll stop feeling guilty."

                scene v13s15a_6b
                with dissolve

                u "Good, have a good night, Riley."

                scene v13s15a_6a
                with dissolve

                ri "You too."

                scene v13s15a_13 # TPP. Show MC removing his shirt, pants already off, in his boxers, slight smile, mouth closed
                with dissolve

                pause 0.75

                scene v13s15a_14 # TPP. Show MC getting into his bed, slight smile, mouth closed
                with dissolve

                pause 0.75

                scene v13s15a_15 # TPP. Show MC sleeping, room is dark
                with dissolve

                pause 0.75

                stop music fadeout 3

                jump v13s17c