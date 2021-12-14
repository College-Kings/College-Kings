# SCENE 47: Lauren and MC dropping off the bikes
# Locations: Bike Drop off at the Beach
# Characters: MC (Outfit: 1), LAUREN (Outfit: 3), AUBREY (Outfit: 1)
# Time: Afternoon

label v13s47:
    scene v13s47_1 # TPP. show MC and lauren riding up to a bike drop off location at the beach, both slight smiles, mouths closed
    with dissolve

    pause 0.75

    play music "music/v13/Track Scene 47.mp3" fadein 2

    scene v13s47_2 # TPP. show MC and lauren get off their bikes and turn them into the bike clerk
    with dissolve

    pause 0.75

    scene v13s47_3 # FPP. show lauren looking at MC, slight smile, mouth closed
    with dissolve

    u "Did you have fun?"

    scene v13s47_3a # FPP. same as v13s47_3 lauren mouth open
    with dissolve

    la "I did, I'm kinda hungry now though. *Chuckles*"

    scene v13s47_3
    with dissolve

    u "Me too."

    scene v13s47_3a
    with dissolve

    la "Wanna get something to eat?"

    scene v13s47_3 
    with dissolve

    u "Sure, I could use a-"

    play sound "sounds/call.mp3"

    scene v13s47_3
    with dissolve

    u "One second."

    stop sound

    scene v13s47_4 # TPP. show MC answers Aubrey's call, don't show Aubrey, lauren standing next to mc, both slight smile, mc mouth open, lauren mouth closed, both of them looking at each other
    with dissolve

    u "Hello?"

    scene v13s47_4a # TPP. same as v13s47_4 show mc mouth closed
    with dissolve

    au "Hey, can you meet me at the beach?"

    scene v13s47_4
    with dissolve

    u "I'm already at the beach. *Chuckles*"

    scene v13s47_4
    with dissolve

    u "Lauren and I just dropped off our bikes at the bike drop off."

    scene v13s47_4a
    with dissolve

    au "Hmm... Oh! I see you. Look to your left. *Chuckles*"

    scene v13s47_5 # TPP. same as same as v13s47_4a camera pans to the left and MC turns and sees Aubrey waving, Aubrey is in a nice bikini, photoshoot ready, aubrey is smiling, mouth open
    with dissolve

    pause 0.75

    scene v13s47_5a # TPP. same as v13s47_5 mc mouth is open
    with dissolve

    u "Oh, hey! *Laughs*I see you."

    scene v13s47_5
    with dissolve

    au "So can you come hang or are you busy with Lauren?"

    scene v13s47_5a
    with dissolve

    u "We were actually getting ready to go get brunch."

    scene v13s47_3a
    with dissolve

    la "It's okay, don't worry about it."

    scene v13s47_3a
    with dissolve

    la "I'll eat with Amber, I needed to talk to her anyway."

    scene v13s47_3
    with dissolve

    u "Are you sure?"

    scene v13s47_3b # FPP. v13s47_3a lauren full smile
    with dissolve

    la "Yes, positive. *Chuckles*"

    scene v13s47_3
    with dissolve

    u "Okay. Well Aubrey, I guess I'm free."

    scene v13s47_5
    with dissolve

    au "Cool, see you in a few. Bye."

    scene v13s47_5a
    with dissolve

    u "Bye."

    scene v13s47_4b # TPP. same as v13s47_4, MC hangs up his phone
    with dissolve

    u "You sure you don't wanna go to brunch?"

    scene v13s47_3b
    with dissolve

    la "Yes, go catch up with Aubrey. I promise I will survive, haha."

    scene v13s47_3
    with dissolve

    u "Okay."

    if lauren.relationship.value >= Relationship.GIRLFRIEND.value:
        scene v13s47_3
        with dissolve

        u "Give me a kiss."

        scene v13s47_3c # FPP. same as v13s47_3b lauren mouth closed
        with dissolve

        pause 0.4

        play sound "sounds/kiss.mp3"
        scene v13s47_6 # TPP. show mc holding lauren behind her head kissing her
        with dissolve

        pause 1.5

        scene v13s47_3b
        with dissolve

        la "Bye, bye mister."

        scene v13s47_3c
        with dissolve

        u "Haha, bye."

        stop music fadeout 3
        jump v13s48

    else:
        scene v13s47_3a
        with dissolve

        la "Have fun!"

        scene v13s47_3
        with dissolve

        u "Bye, you too."

        stop music fadeout 3
        jump v13s48