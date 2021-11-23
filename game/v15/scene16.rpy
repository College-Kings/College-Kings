# SCENE 16: MC leaves mad or not mad
# Locations: Outside Ms Rose's house on the way to Lauren's party
# Characters: MC (Outfit: 5)
# Time: Evening

label v15s16:
    if MadAtMsRose: #Placeholder for when scenes before are ready.
        scene v15s16_1 # TPP. Show MC walking out of Ms Rose's house, MC mad, mouth closed.
        with dissolve

        u "(I know she was trying, but- Seriously???"

        scene v15s16_2 # TPP. Show MC starting to walk down sidewalk towards Lauren's party, MC mad, mouth closed.
        with dissolve

        u "(She might have fucked up my life by giving me a drink that night.)"

        scene v15s16_3 # TPP. Show MC further down the sidewalk, MC mad, mouth closed.
        with dissolve

        u "(If they find any trace of that drug in my system, I'm done for...)"

        scene v15s16_4 # TPP. MC stopped in place with his eyes closed, MC neutral face, mouth closed.
        with dissolve

        u "*Sighs* (Now it's time for Lauren's party... Game face on, [name].)"

        scene v15s16_5 # TPP. MC starting to walk again, MC neutral face, mouth closed.
        with dissolve

        u "(Time for shopping.)"

    else:
        scene v15s16_1a # TPP. Same as v15s16_1, MC slight smile, mouth closed.
        with dissolve

        u "(Phew! She drives me absolutely wild... Haha.)"

        scene v15s16_2a # TPP. Same as v15s16_2, MC slight smile, mouth closed.
        with dissolve

        u "(Something about mature women and their cougar-ish ways...)"

        scene v15s16_3a # TPP. Same as v15s16_3, MC slight smile, mouth closed.
        with dissolve

        u "(Okay, snap out of it, [name]. We've got a party to get to!)"

        scene v15s16_4a # TPP. Same as v15s16_4, MC stopped in place with his eyes open, MC slight smile, mouth closed.
        with dissolve

        u "(And a costume to find...)"

        scene v15s16_5a # TPP. Same as v15s16_5, MC worried smile, mouth closed.
        with dissolve

        u "(And a gift to buy... Fuck.)"
    jump v15s17