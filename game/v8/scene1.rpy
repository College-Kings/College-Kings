### v8 beginning. Variable definitions here
label v8start:

    if lauren.relationship < Relationship.FRIEND: #reset lauren mad to friend
        $ CharacterService.set_relationship(lauren, Relationship.FRIEND, mc)
    
    if ending == "lauren":
        jump v8_la_start
    elif ending == "chloe":
        jump v8_cl_start
    elif ending == "riley" and (Moods.TEASED in riley.mood or CharacterService.is_fwb(riley)):
        jump v8_ri_start
    elif ending == "riley":
        jump v8_ri_start_fr
    else:
        jump hoco_amb_night

    ### SCENE 1: Lauren v7 ending continued
label v8_la_start:
    # Note to renderers: Make sure the clothes (they're in underwear) and any other props are the same as Lauren's ending in v7

    stop music fadeout 3

    scene sfr4la31a # Old render
    with dissolve
    u "I like the sound of that."

    play sound "sounds/switch.mp3"

    scene v8s1 # TPP. MC turning the light switch off in Lauren's room (lights are off in this render)
    with dissolve
    pause 0.5

    scene v8s2 # TPP. MC walking towards the bed close to it. Lauren curious, waiting for him with her head in her hand and elbow on pillow. Focus on Lauren
    with dissolve
    pause 0.5

    scene v8s3 # TPP (lateral shot, at least torsos should be fully visible). Lauren climbs on top of MC. Faces 1-2 feet apart, looking at each other. Both smiling, both of them mouths closed
    with dissolve
    pause

    scene v8s3a # Same as v8s3 but MC talking
    with dissolve
    u "God, you're beautiful."

    play sound "sounds/kiss.mp3"

    scene v8s4 # TPP (same angle as v8s3 but zoomed in to focus on faces and upper torsos). MC and Lauren making out passionately
    with dissolve
    pause 0.5

    scene v8s4a # Same as v8s4 but slightly different posture (like different lips locked and head tilt)
    with dissolve
    pause 0.5

    scene v8s3b # Same as v8s3 but Lauren talking
    with dissolve
    la "You're a great kisser, you know that?"

    scene v8s3a
    with dissolve
    u "Mhmm, and you aren't half bad yourself."

    scene v8s3b
    with dissolve
    la "Oh, reeaaally?"

    scene v8s4
    with dissolve
    pause 0.5

    scene v8s4a
    with dissolve
    pause 0.5

    scene v8s4
    with dissolve
    pause 0.5

    scene v8s4a
    with dissolve
    pause 0.5

    scene v8s4
    with dissolve
    pause 0.5

    scene v8s3b
    with dissolve
    la "...so you were saying?"

    scene v8s3a
    with dissolve
    u "Any chance I can take it back?"
    la "*Chuckles*"

    scene v8s5 # TPP. Lauren and MC cuddling facing each other with Lauren's head resting on MC's chest (just below MC's head). Lauren eyes closed, looking a bit tired but slightly smiling. Both of them mouths closed. MC's hand wrapped around Lauren and her hand resting on MC's chest
    with dissolve
    pause 0.5

    scene v8s5a # Same as v8s5 but Lauren talking
    with dissolve
    la "Wish we could do this all the time."

    scene v8s5b # Same as v8s5 but MC talking
    with dissolve
    u "Yeah, yeah me too."

    scene v8s5a
    with dissolve
    la "And maybe even something mo- *yaaawn*"

    scene v8s5b
    with dissolve
    u "You tired?"

    scene v8s5a
    with dissolve
    la "A bit."

    scene v8s5b
    with dissolve
    u "Why don't you get some rest then?"

    scene v8s5a
    with dissolve
    la "Have a good night, baby."

    scene v8s5b
    with dissolve
    u "You too."

    scene v8s5
    with dissolve
    pause 0.5

    scene v8s5c # Same as v8s5 but MC eyes closed
    with dissolve
    pause 0.8

    scene v8s6 # TPP (maybe from top). MC holding Lauren from back while spooning. It's morning and they're about to wake up.
    with Fade(1, 0.5, 1)
    pause 0.5

    scene v8s6a # Same as v8s6 but MC woke up (just eyes open)
    with Dissolve(1)
    pause 0.5

    play sound "sounds/kiss.mp3"

    scene v8s6b # MC kissing on Lauren's cheek (to wake her up)
    with dissolve
    u "Morning sleepy head."

    scene v8s6c # Lauren turns around to face MC (eyes open, smiling and looking cute), who is back on his pillow and just looking at her
    with dissolve
    pause 0.5

    scene v8s7 # FPP (v8s6c continued). Lauren looking cute and talking
    with dissolve
    la "Morning. Sleep well?"

    scene v8s7a # Same as v8s7 but Lauren mouth closed
    with dissolve
    u "Like a baby."

    scene v8s7
    with dissolve
    la "From the sound of your snoring, more like a hibernating bear."

    scene v8s7a
    with dissolve
    u "What??"

    scene v8s7b # Lauren laughing a little and talking
    with dissolve
    la "I'm kidding. Haha."

    scene v8s7
    with dissolve
    la "I'm just glad we finally got some cuddle time. I feel closer to you."

    scene v8s7a
    with dissolve
    u "Me too. Hopefully we can have more nights like this."

    scene v8s7
    with dissolve
    la "Of course. You are my boyfriend, after all."

    scene v8s8 # TPP (from top). Lauren and MC quick peck on the lips
    with dissolve
    play sound "sounds/kiss.mp3"
    pause 0.5

    scene v8s7a
    with dissolve
    u "You're the cutest, especially when you sleep."

    scene v8s7c # Lauren surprised a little but smiling and talking
    with dissolve
    la "You watched me?!"

    scene v8s7d # Same as v8s7c but Lauren mouth closed
    with dissolve
    u "You are my girlfriend, after all. Haha."

    scene v8s7c
    with dissolve
    la "Okaaaaay."

    scene v8s7d
    with dissolve
    u "What? Just saying you look like an angel when you sleep."

    scene v8s8
    with dissolve
    play sound "sounds/kiss.mp3"
    pause 0.5

    scene v8s7
    with dissolve
    la "Thanks babe... Ugh. I need to start getting ready."

    scene v8s7b
    with dissolve
    la "Although... on the other hand, laying here with you all day would be nice. Hah-"

    scene v8s7c
    with vpunch
    la "No! I have homework."

    scene v8s7d
    with dissolve
    u "As awesome as a day in bed sounds, I don't want to be the reason you flunk out."

    scene v8s8
    with dissolve
    play sound "sounds/kiss.mp3"
    pause 0.5

    scene v8s7a
    with dissolve
    u "Meet me back when you're done?"

    stop music fadeout 3

    scene v8s7
    with dissolve
    la "Okay babe. Byeee."

    scene black
    with Dissolve(1)
    pause 0.5

    jump aft_amb_night
