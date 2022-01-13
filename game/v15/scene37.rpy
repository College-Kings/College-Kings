# SCENE 37: MC walks back home
# Locations: The streets back to MC's frat house.
# Characters: MC (Outfit: 2)
# Time: Night

label v15s37:
    play music "music/v13/Track Scene 5.mp3" fadein 2

    scene v15s37_1 # TPP. Show MC walking down the street towards the frat houses, slight smile, mouth closed.
    with dissolve

    pause 0.75

    if v15_chloe_lindseysabotage:
        scene v15s37_2 # TPP. Close up of MC pulling out his phone, slight smile, mouth closed.
        with dissolve

        u "(I still need to send the recording to Chloe. I hope it's useful to her.)"

        scene v15s37_2a # TPP. Show MC on his phone his other hand pressing on part of the phone, slight smile, mouth closed.
        with dissolve
        
        pause 0.75

        scene v15s37_2b # TPP. Show MC pressing a different space on part of his phone, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s37_2c # TPP. Show MC putting his phone away, slight smile, mouth closed.
        with dissolve

        pause 0.75

    if not AutumnTrust:
        scene v15s37_3 # TPP. Show MC walking further down the street, slight smile, mouth closed
        with dissolve

        u "(That was a fun night, especially with Autumn there. I'm glad I'm getting to know her better.)"

    elif v15s36_not_good_idea and lauren.relationship >= Relationship.GIRLFRIEND: 
        scene v15s37_3
        with dissolve

        u "(I'm glad Autumn was okay with what I said back there.)"
        u "(I think she was forgetting for a moment that I'm dating her sister, ha... Or maybe she was testing me?)"

        u "(Anyway, even if I wanted to date two sisters...)"

        u "(That would be wrong on so many levels... Right?)"

    elif v15s36_not_good_idea:
        scene v15s37_3
        with dissolve

        u "(That was a nice surprise from Autumn. She's great and all but... it wouldn't feel right.)"

        u "(Not right now anyway.)"

    elif lauren.relationship >= Relationship.GIRLFRIEND:
        scene v15s37_3
        with dissolve

        u "(I'm glad we agreed that nothing can happen between us while I'm with Lauren.)"

        u "(I can't mess things up with Lauren, no matter how much I like her sister.)"

    else:
        scene v15s37_3
        with dissolve

        u "(What a fucking night... I never thought it would end with kissing Autumn!)"

        u "(You just never know what girls are really thinking, haha.)"

        u "(I'm so excited to spend more time with her.)"

    stop music fadeout 3

    jump v15s41