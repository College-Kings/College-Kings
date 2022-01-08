# SCENE 41: MC gets woken up by text from Amber
# Locations: MC's room Wolves and Apes.
# Characters: MC (Outfit: Underwear)
# Time: Morning

label v15s41:
    scene black
    with dissolve
    
    pause 1

    scene sleep_transition_fast
    with fade

    pause 2.2

    if joinwolves:
        scene v15s41_1 # TPP. In wolves room, Camera close to MC's nightstand, his phone sitting on his nightstand turned off, MC sleeping on his side facing away from the camera.
        with dissolve

        pause 0.75

        $ amber.messenger.newMessage("Hey.")
        $ amber.messenger.newMessage("I need you to wake up...")
        play sound "sounds/vibrate.mp3"

        scene v15s41_1a # TPP. In wolves room, Camera close to MC's nightstand, his phone sitting on his nightstand his phone illuminating the dark room, MC sleeping on his side facing away from the camera.
        with dissolve

        pause 0.75

        $ amber.messenger.newMessage("Get your ass out of bed, [name]!")
        play sound "sounds/vibrate.mp3"

        scene v15s41_1a
        with dissolve

        pause 0.75

        $ amber.messenger.newMessage("We need to talk about Nora.")
        play sound "sounds/vibrate.mp3"

        scene v15s41_1a
        with dissolve

        pause 0.75

        $ amber.messenger.newMessage("Don't even waste time replying, okay?!")
        play sound "sounds/vibrate.mp3"

        scene v15s41_1b # TPP. In wolves room, Camera close to MC's nighstand, his phone sitting on his nightstand his phone illuminating the dark room, MC sitting up and looking up over at his phone, tired face, mouth closed.
        with dissolve

        u "(What the fuck? I didn't set an alarm... How many texts did I just get?)"

        $ amber.messenger.newMessage("Room 103 at SVC. Get here now! ASAP!")
        play sound "sounds/vibrate.mp3"

        scene v15s41_1c # TPP. In wolves room, Camera close to MC's nightstand, his phone sitting on his nightsand his phone illuminating the dark room, MC sitting up and grabbing his phone, tired face, mouth closed.
        with dissolve

        pause 0.75

        call screen phone

        pause 0.75

        scene v15s41_1d # TPP. In wolves room, Camera close to MC's nightstand, his phone sitting on his nightsand his phone illuminating the dark room, MC sitting up and looking at his phone., tired face, mouth closed.
        with dissolve
        
        pause 0.75

        scene v15s41_1e # TPP. In wolves room, Camera close to MC's nightstand, his phone sitting on his nightstand his phone turned off, MC putting his phone back on the night stand, tired face, mouth closed.
        with dissolve

        pause 0.75

        scene v15s41_2 # TPP. In wolves room, closer up of MC rubbing his eyes as he is waking up, tired face, mouth closed.
        with dissolve

        u "(Woah, what the hell? What does Amber know about Nora?)"

        scene v15s41_3 # TPP. In wolves room, MC getting out of of bed,neutral face, mouth closed.
        with dissolve

        u "(I need to get over there now.)"

        scene v15s41_4 # TPP. In wolves room, Show MC putting on his pants, neutral face, mouth closed.
        with dissolve

        pause 0.75

        scene v15s41_5 # TPP. In wolves room, Show MC putting on his shirt while he sort of sprints towards the door to leave, neutral face, mouth closed.
        with dissolve

        pause 0.75

        scene v15s41_5a # TPP. In wolves room, Show MC's shirt over his face, MC falling about to hit the ground.
        with dissolve

        pause 0.75

        play sound "sounds/thud.mp3"

        scene v15s41_5b # TPP. In wolves room, MC hitting the floor, his shirt over his face.
        with dissolve

        u "SON OF A BITCH!"
        
        pause 0.75

        scene v15s41_5c # TPP. In wolves room, MC getting up pulling his shirt fully on, MC neutral face, mouth closed.
        with dissolve

        pause 0.75

        play sound "sounds/dooropen.mp3"

        scene v15s41_6 # TPP. In wolves room, MC opening the door to his room and hurrying out, neutral face, mouth closed.
        with dissolve

        pause 0.75

        stop music fadeout 3

        jump v15s42

    else:
        scene v15s41_7 # TPP. In apes room, Camera close to MC's nightstand, his phone sitting on his nightstand turned off, MC sleeping on his side facing away from the camera.
        with dissolve

        pause 0.75

        $ amber.messenger.newMessage("Hey.")
        $ amber.messenger.newMessage("I need you to wake up...")
        play sound "sounds/vibrate.mp3"

        scene v15s41_7a # TPP. In apes room, Camera close to MC's nightstand, his phone sitting on his nightstand his phone illuminating the dark room, MC sleeping on his side facing away from the camera.
        with dissolve

        pause 0.75

        $ amber.messenger.newMessage("Get your ass out of bed, [name]!")
        play sound "sounds/vibrate.mp3"

        scene v15s41_7a
        with dissolve

        pause 0.75

        $ amber.messenger.newMessage("We need to talk about Nora.")
        play sound "sounds/vibrate.mp3"

        scene v15s41_7a
        with dissolve

        pause 0.75

        $ amber.messenger.newMessage("Don't even waste time replying, okay?!")
        play sound "sounds/vibrate.mp3"

        scene v15s41_7b # TPP. In apes room, Camera close to MC's nighstand, his phone sitting on his nightstand his phone illuminating the dark room, MC sitting up and looking up over at his phone, tired face, mouth closed.
        with dissolve

        u "(What the fuck? I didn't set an alarm... How many texts did I just get?)"

        $ amber.messenger.newMessage("Room 103 at SVC. Get here now! ASAP!")
        play sound "sounds/vibrate.mp3"

        scene v15s41_7c # TPP. In apes room, Camera close to MC's nightstand, his phone sitting on his nightsand his phone illuminating the dark room, MC sitting up and grabbing his phone, tired face, mouth closed.
        with dissolve

        pause 0.75

        scene v15s41_7d # TPP. In apes room, Camera close to MC's nightstand, his phone sitting on his nightsand his phone illuminating the dark room, MC sitting up and looking at his phone., tired face, mouth closed.
        with dissolve

        pause 0.75

        scene v15s41_7e # TPP. In apes room, Camera close to MC's nightstand, his phone sitting on his nightstand his phone turned off, MC putting his phone back on the night stand, tired face, mouth closed.
        with dissolve

        pause 0.75

        scene v15s41_8 # TPP. In apes room, closer up of MC rubbing his eyes as he is waking up, tired face, mouth closed.
        with dissolve

        u "(Woah, what the hell? What does Amber know about Nora?)"

        scene v15s41_9 # TPP. In apes room, MC getting out of of bed,neutral face, mouth closed.
        with dissolve

        u "(I need to get over there now.)"

        scene v15s41_10 # TPP. In apes room, Show MC putting on his pants, neutral face, mouth closed.
        with dissolve

        pause 0.75

        scene v15s41_11 # TPP. In apes room, Show MC putting on his shirt while he sort of sprints towards the door to leave, neutral face, mouth closed.
        with dissolve

        pause 0.75

        scene v15s41_11a # TPP. In apes room, Show MC's shirt over his face, MC falling about to hit the ground.
        with dissolve

        pause 0.75

        play sound "sounds/thud.mp3"

        scene v15s41_11b # TPP. In apes room, MC hitting the floor, his shirt over his face.
        with dissolve

        u "SON OF A BITCH!"
        
        pause 0.75

        scene v15s41_11c # TPP. In apes room, MC getting up pulling his shirt fully on, MC neutral face, mouth closed.
        with dissolve

        pause 0.75

        play sound "sounds/dooropen.mp3"

        scene v15s41_12 # TPP. In apes room, MC opening the door to his room and hurrying out, neutral face, mouth closed.
        with dissolve

        pause 0.75

        stop music fadeout 3

        jump v15s42