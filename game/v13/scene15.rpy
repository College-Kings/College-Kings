# SCENE 15: Lauren text rooming Chloe
# Locations: Hotel Room
# Characters: MC (Outfit: 2), CHLOE (Outfit: 6)
# Time: Night

init python:
    def v13s15_Reply1():
<<<<<<< Updated upstream
        setattr(store, "v13_cuddle_lauren", True)
=======
        v13_cuddle_lauren = True
>>>>>>> Stashed changes
        contact_Lauren.newMessage(_("Yayy :) "))

    def v13s15_Reply2():
        contact_Lauren.newMessage(_("Aww okay, it's cool "))
        contact_Lauren.addReply(_("Sorry babe, I'm just so tired. "))
<<<<<<< Updated upstream
        contact_Lauren.newMessage(_("It's okay, night. "))
=======
        ccontact_Lauren.newMessage(_("It's okay, night. "))
>>>>>>> Stashed changes

label v13s15:
    scene v13s15_1 # TPP. Show MC walking into the room, it's dark inside, MC neutral expression, mouth closed
    with dissolve

    pause 0.75

    scene v13s15_2 # TPP. Show MC standing in front of the door, in the room, MC neutral expression, mouth closed, room is dark
    with dissolve

    pause 0.75

    u "(Oh shit, she's probably asleep. Gonna have to tiptoe in the dark.)"

    scene v13s15_3 # TPP. Show MC walking tip toeing towards his bed, slightly scared, mouth closed
    with dissolve

    u "(I can't see a damn thing.)"

    scene v13s15_4 # TPP. Close up of MC's foot hitting his bed (no shows)
    with vpunch

    u "*Whisper* Fuck!"

    scene v13s15_5 # TPP. Chloe laying in her bed, turning on the light, she's confused, mouth closed
    with dissolve

    pause 0.75

    scene v13s15_6 # FPP. MC same positioning as v13s15_4, looking at Chloe, she's in her bed, under her covers, looking at MC, Chloe slightly worried, mouth closed
    with dissolve

    u "I'm sorry, Chloe."

    scene v13s15_6a # FPP. Same as v13s15_6, Chloe slightly worried, mouth open
    with dissolve

    cl "Did you hurt yourself?"

    scene v13s15_6b # FPP. Same as v13s15_6, Chloe slight smile, mouth closed
    with dissolve

    u "No, I just... I hit my foot on the bed."

    scene v13s15_6c # FPP. Same as v13s15_6b, Chloe slight smile, mouth open
    with dissolve

    cl "You should've turned on the light. *Chuckles*"

    scene v13s15_6b
    with dissolve

    u "I didn't wanna wake you."

    scene v13s15_6c
    with dissolve

    cl "Thanks for caring, but I would rather wake up in the middle of the night due to a light, than have to take a trip to the hospital."

    scene v13s15_6b
    with dissolve

    u "*Laughs* Thanks, but the pain is already gone."

    scene v13s15_6c
    with dissolve

    cl "You ready to go to sleep, then? I hope 'cause I'm so fucking tired..."

    scene v13s15_6b
    with dissolve

    u "You just take your little self to sleep."

    scene v13s15_6c
    with dissolve

    cl "Sounds like a plan."

    scene v13s15_6d # FPP. Same as v13s15_6, Chloe with her back turned to MC
    with dissolve

    pause 0.75

    if not laurenrs:
        scene v13s15_7 # TPP. Show MC removing his shirt, pants already off, in his boxers, slight smile, mouth closed
        with dissolve

        pause 0.75

        scene v13s15_8 # TPP. Show MC getting into his bed, slight smile, mouth closed
        with dissolve

        pause 0.75

        scene v13s15_9 # TPP. Show MC sleeping, room is dark
        with fade

        pause 0.75

        jump v13s17c
    else:
        play sound "sounds/vibrate.mp3"

        scene v13s15_10 # TPP. MC looking down at his phone, he is standing in same place as v13s15_6, slightly surprised, mouth closed
        with dissolve

        u "(Kinda late for a text.)"

        $ contact_Lauren.newMessage(_("You up? ", queue=False))
        $ contact_Lauren.addReply(_("Yeah, wassup? "))
        $ contact_Lauren.newMessage(_("Come cuddle with me? ;) "))
        $ contact_Lauren.addReply(_("You don't have to ask me twice, omw "), v13s15_Reply2)
        $ contact_Lauren.addReply(_("I'm already halfway asleep... "), v13s15_Reply1)

        scene v13s15_11 # FPP. MC looking down at his phone, he is standing in same place as v13s15_6
        with dissolve

        label v13s15_PhoneContinueLauren:
            if contact_Lauren.replies:
                call screen phone
            if contact_Lauren.replies:
                u "(I should check my phone.)"
                jump v13s15_PhoneContinueLauren
        
        if v13_cuddle_lauren:
            scene v13s15_12 # TPP. Show MC standing in same position as v13s15_6, slight smirk, mouth closed, looking at the door
            with dissolve

            u "(A night with the baby.)"

            if not chloegf:
                scene v13s15_13 # TPP. Show MC walking out of the room, slight smirk, mouth closed
                with dissolve

                pause 0.75

                jump v13s16

            else:
                scene v13s15_14 # TPP. Show MC walking towards the door, startled, mouth closed
                with vpunch

                cl "Hmm? [name]?"

                scene v13s15_15 # FPP. MC standing same place as v13s15_14, looking at Chloe, she is laying on her bed, looking at MC, suspicious, mouth open
                with dissolve

                cl "Where are you going?"

                scene v13s15_15a # FPP. Same as v13s15_15, Chloe suspicious, mouth closed
                with dissolve

                menu:
                    "Grabbing a snack":
                        $ chloeSus += 1

                        u "Oh, um... My stomach is feeling really empty, so I'm gonna go try to find something to snack on..."

                        scene v13s15_15
                        with dissolve

                        cl "But... It's the middle of the night... I don't know if-"

                        scene v13s15_15a
                        with dissolve

                        u "No worries, I saw a vending machine earlier."

                        scene v13s15_15
                        with dissolve

                        cl "Oh, I- Okay..."

                    "Imre needs me":
                        scene v13s15_15b # FPP. Same as v13s15_15a, Chloe slightly sad, mouth closed
                        with dissolve
                        
                        u "Oh, um... Imre needs me for something, so I'm gonna go see what's up."

                        scene v13s15_15c # FPP. Same as v13s15_15n, Chloe slightly sad, mouth open
                        with dissolve

                        cl "Don't be long, okay?"

                        scene v13s15_15b
                        with dissolve

                        u "I'll try not to, but who knows with Imre."

                        scene v13s15_15c
                        with dissolve

                        cl "*Sighs* Okay."

                scene v13s15_15d # FPP. Same as v13s15_15, Chloe rolling over, sleeping
                with dissolve

                u "(What she doesn't know won't hurt her.)"

                scene v13s15_13
                with dissolve

                pause 0.75

                jump v13s16

        else:
            scene v13s15_7 
            with dissolve

            pause 0.75

            scene v13s15_8 
            with dissolve

            pause 0.75

            scene v13s15_9
            with fade

            pause 0.75

            jump v13s17c