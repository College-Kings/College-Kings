### SCENE 4: v07 Riley friends ending continued
label v08_ri_start_fr:
    # Note to renderers: Make sure the MC is in his suit and Riley is in her HoCo dress. Any other props are the same as Riley's friendship ending in v07

    scene v8s40
    with dissolve
    ri "I'm bisexual."

    scene v8s40a
    with dissolve
    u "Really!?"

    scene v8s40
    with dissolve
    ri "Yeah, and I haven't told anyone except you."

    scene v8s40a
    with dissolve
    u "So why now? Why me?"

    scene v8s40
    with dissolve
    ri "I think I want to experiment with other girls."

    if upstairs == "aubrey":
        scene v8s40a
        with dissolve
        u "Did you know Aubrey is bisexual?"

        scene v8s40 # sfr4ri56 from v07 continued, so keep the setting same. Riley surprised/intrigued a little and talking
        with dissolve
        ri "Wait, really?"

        scene v8s40a # Same as v8s40 but Riley mouth closed
        with dissolve
        u "Yeah. She told me herself."

        scene v8s40
        with dissolve
        ri "I'm intrigued."

        scene v8s40a
        with dissolve
        u "You guys should get together."

        scene v8s40b # Riley a flirty and talking
        with dissolve
        ri "Maybe."

        scene v8s40c # Same as v8s40b but Riley mouth closed
        with dissolve
        u "Then you can invite me."

        scene v8s41 # FPP. Riley playfully pushes MC. Same as s40's camera but move it back a little (as if the MC tilted back) and show her hand to give the feel that she hit him, mouth half open
        with vpunch
        ri "Also a maybe!"

        scene v8s40b
        with dissolve
        ri "I don't know if you can handle two girls."

        scene v8s40c
        with dissolve
        u "Aw come on."

        scene v8s40d # Riley laughing a little, cute and talking
        with dissolve
        ri "Haha just teasing, but we'll see."

        scene v8s40e # Same as v8s40d but Riley mouth closed
        with dissolve
        u "You know, that's actually pretty hot."

    else:
        scene v8s40a
        with dissolve
        u "That's pretty hot."

    scene v8s40d
    with dissolve
    ri "It's not meant to be a guy's sexual fantasy."

    scene v8s40f # Riley shrugging with her shoulders raised and talking
    with dissolve
    ri "I'm just being honest. I'm genuinely attracted to girls."

    scene v8s40e
    with dissolve
    u "And I'm just saying it's pretty hot to imagine two hot girls going down on each other."

    scene v8s41
    with vpunch
    pause 0.5

    scene v8s40c
    with dissolve
    u "What? I'm just being honest too."

    scene v8s40b
    with dissolve
    ri "Yeah, yeah."

    scene v8s40a
    with dissolve
    u "So you hooked up with other girls before?"

    scene v8s40
    with dissolve
    ri "Never. I mean... not like that. Just made out."

    scene v8s40b
    with dissolve
    ri "But I like watching lesbian porn. A lot."

    scene v8s40c
    with dissolve
    u "Don't we all?"

    scene v8s40g # Riley rolling eyes, cute and smiling, mouth closed
    with dissolve
    ri "..."

    scene v8s40a
    with dissolve
    u "So, I'm just saying, if you're ever nervous, you know for your first full on female hook up, just call me."

    scene v8s40b
    with dissolve
    ri "Haha. Okay! I'll think about it."

    scene v8s40c
    with dissolve
    u "You know, makes sense. You'll be comfortable. I sure as hell will be too."

    scene v8s40d
    with dissolve
    ri "Okay, okay. I get it. But yeah, thanks for being an ear for me."

    scene v8s40e
    with dissolve
    u "Anytime."

    scene v8s40h # Riley yawns
    with dissolve
    pause 1

    scene v8s40a
    with dissolve
    u "Tired?"

    scene v8s40
    with dissolve
    ri "Yeah."

    scene clock2a # Old render
    with dissolve
    pause 1

    scene v8s40
    with dissolve
    ri "It's pretty late."

    scene v8s40a
    with dissolve
    u "Yeah, I'm gonna head home."

    scene v8s40
    with dissolve
    ri "Okay. Talk soon?"

    scene v8s40a
    with dissolve
    u "Sure, bye."

    scene v8s40d
    with dissolve
    ri "Byeee."

    scene black
    with Dissolve(1)
    pause 0.5

    jump aft_amb_night
