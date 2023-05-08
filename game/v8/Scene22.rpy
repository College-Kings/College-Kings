# Talking To The Dean
# Location: MC Apes Room, MC Wolves Room
# Outfits: MC Outfit 3
# Time: Monday Morning

label s22:
    if mc.frat == Frat.WOLVES:
        scene v8spc1 # TPP. Show MC sat on the edge of his bed in Wolves room.
        with Fade(0.75, 0.25, 0.75)

        u "(Hope she answers.)"

        scene v8spc1a # TPP. Same camera as v8spc1, Show MC now with phone to ear.
        with dissolve

        pe "Hello?"

        scene v8spc2 # TPP. Camera from infront of MC, show him on the phone, neutral expression, mouth open.
        with dissolve

        u "Penelope? Its [name]."

        scene v8spc2a # TPP. Same camera as vaspc2, MC mouth closed.
        with dissolve

        pe "Hi! How's it going?"

        scene v8spc2
        with dissolve

        u "Pretty good so far. I wanted to call you and let you know I talked to the dean."

        scene v8spc2a
        with dissolve

        pe "Oh? How did it go?"

        scene v8spc2
        with dissolve

        u "As far as I can tell, it went okay, I guess. She said she would take what I said under advisement."

        scene v8spc2b # TPP. Same camera as vaspc2, MC slight smile, mouth closed.
        with dissolve

        pe "Oh. Well, at least you tried, which is more than anyone else did. Thank you for this."

        scene v8spc2c # TPP. Same camera as vaspc2, MC slight smile, mouth open.
        with dissolve

        u "Hey, it's not over yet. She asked me to tell you not to think about doing anything like this again. Might be some hope."

        scene v8spc2b
        with dissolve

        pe "Yeah, maybe. At least I hope so. Thanks again [name], I appreciate it."

        scene v8spc2c
        with dissolve

        u "No worries. Wanna hang out today?"

        scene v8spc2b
        with dissolve

        pe "I'd love to, but I need to study and I made plans with Jenny later. I'm sorry."

        scene v8spc2c
        with dissolve

        u "Oh, it's okay. Have fun and stay away from computers, hahaha."

        scene v8spc2b
        with dissolve

        pe "Hahaha! You don't need to tell me! I learned my lesson! Bye [name]."

        scene v8spc2
        with dissolve

        u "Bye."

        scene v8spc1b # TPP. Same camera as v8spc1, Show MC hanging up the call.
        with dissolve

        u "(Well, nothing else to do besides wait and hope for the best)"

        scene v8spc1
        with dissolve

    else:
        scene v8spc3 # TPP. Show MC sat on the edge of his bed in Apes room.
        with Fade(0.75, 0.25, 0.75)

        u "(Hope she answers.)"

        scene v8spc3a # TPP. Same camera as v8spc3, Show MC now with phone to ear.
        with dissolve

        pe "Hello?"

        scene v8spc4 # TPP. Camera from infront of MC, show him on the phone, neutral expression, mouth open.
        with dissolve

        u "Penelope? Its [name]."

        scene v8spc4a # TPP. Same camera as vaspc4, MC mouth closed.
        with dissolve

        pe "Hi! How's it going?"

        scene v8spc4
        with dissolve

        u "Pretty good so far. I wanted to call you and let you know I talked to the dean."

        scene v8spc4a
        with dissolve

        pe "Oh? How did it go?"

        scene v8spc4
        with dissolve

        u "As far as I can tell, it went okay, I guess. She said she would take what I said under advisement."

        scene v8spc4b # TPP. Same camera as vaspc4, MC slight smile, mouth closed.
        with dissolve

        pe "Oh. Well, at least you tried, which is more than anyone else did. Thank you for this."

        scene v8spc4c # TPP. Same camera as vaspc4, MC slight smile, mouth open.
        with dissolve

        u "Hey, it's not over yet. She asked me to tell you not to think about doing anything like this again. Might be some hope."

        scene v8spc4b
        with dissolve

        pe "Yeah, maybe. At least I hope so. Thanks again [name], I appreciate it."

        scene v8spc4c
        with dissolve

        u "No worries. Wanna hang out today?"

        scene v8spc4b
        with dissolve

        pe "I'd love to, but I need to study and I made plans with Jenny later. I'm sorry."

        scene v8spc4c
        with dissolve

        u "Oh, it's okay. Have fun and stay away from computers, hahaha."

        scene v8spc4b
        with dissolve

        pe "Hahaha! You don't need to tell me! I learned my lesson! Bye [name]."

        scene v8spc4
        with dissolve

        u "Bye."

        scene v8spc3b # TPP. Same camera as v8spc3, Show MC hanging up the call.
        with dissolve

        u "(Well, nothing else to do besides wait and hope for the best.)"

        scene v8spc3
        with dissolve

    jump josh_calls_you
