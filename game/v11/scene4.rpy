# SCENE 04: Emily at the Park
# Locations: MC's Bed (Wolves/Apes), The Park
# Characters: MC (smart outfit from scene 1), Emily (Outfit 2)
# Time: No clue bruv

init python:
    def v11s4_reply1():
        emily.messenger.newMessage("This is important, we need to talk now.")
        emily.messenger.addReply("What's up?")
        emily.messenger.newMessage("Meet me at the park.")
        emily.messenger.addReply("Okay.")

    def v11s4_reply2():
        emily.messenger.newMessage("Meet me at the park.")
        emily.messenger.addReply("Okay.")

label v11_emily_park:
    play music "music/v11/Track Scene 4_1.mp3" fadein 2
    if joinwolves: # MC is a Wolf
        scene v11seap1 # TPP. Show MC sitting down on his bed in WOLVES room and noticing that he got a text. Normal expression, mouth closed.
        with fade

        play sound "sounds/vibrate.mp3"
        u "(I should see who that is.)"

        scene v11seap1a # TPP. Same camera as v11seap1. Show MC sitting down on his bed in WOLVES room and looking at his phone, normal expression, mouth closed.
        with dissolve

        pause 0.75

    else: # MC is an Ape
        scene v11seap2 # TPP. Show MC sitting down on his bed in APES room and noticing that he got a text. Normal expression, mouth closed.
        with fade

        play sound "sounds/vibrate.mp3"
        u "(I should see who that is.)"

        scene v11seap2b # TPP. Same camera as v10seap2. Show MC sitting down on his bed in APES room and looking at his phone, normal expression, mouth closed.
        with dissolve

        pause 0.75

    $ emily.messenger.newMessage("Hey, we need to talk.", force_send=True)
    $ emily.messenger.addReply("I'm pretty busy right now.", v11s4_reply1)
    $ emily.messenger.addReply("What's up?", v11s4_reply2)

    label v11s4_PhoneContinueEmily1:
        if emily.messenger.replies:
            call screen phone
        if emily.messenger.replies:
            u "(I should check my phone.)"
            jump v11s4_PhoneContinueEmily1

    if joinwolves: # MC is a Wolf
        scene v11seap1b # TPP. Same camera as v11seap1. Show MC sitting on his bed in WOLVES room, putting his phone away. Normal expression, mouth closed.
        with dissolve

        u "(Let's go see what this is all about.)"

    else: # MC is an Ape
        scene v11seap2c # TPP. Same camer aas v10seap2. Show MC sitting on his bed in APES room, putting his phone away. Normal expression, mouth closed.
        with dissolve

        u "(Let's go see what this is all about.)"

    scene v11seap3 # TPP. Show MC walking around the park, like he's looking for someone. Normal expression, mouth closed.
    with fade

    pause 1.0

    scene v11seap3a # TPP. Same camera as v11seap3. Show MC starting to sit down on a park bench, normal expression, mouth closed.
    with dissolve

    pause 1.0

    scene v11seap4 # FPP. Show Emily walking towards MC, normal expression.
    with fade

    stop music fadeout 3

    play music "music/v11/Track Scene 4_2.mp3" fadein 2
    pause 1.0

    scene v11seap4a # FPP. Same camera as v10seap4. Show a closer shot of Emily standing in front of MC, normal expression, mouth closed.
    with dissolve

    u "You want to sit down?"

    scene v11seap4b # FPP. Same camera as v10seap4. Show a closer shot of Emily standing in front of MC, normal expression, mouth open.
    with dissolve

    em "I'm fine, this won't be long."

    scene v11seap4a
    with dissolve

    u "What's going on?"

    scene v11seap4b
    with dissolve

    em "I feel like the best thing to do is just come out and say it. We can't see each other anymore."

    if forgiveemily:
        scene v11seap4a
        with dissolve

        u "Where is this coming from?"

    else:
        scene v11seap4a
        with dissolve

        u "Uhm..."

    scene v11seap4c # FPP. Same camera as v10seap4. Show a closer shot of Emily standing in front of MC, slightly annoyed expression, mouth open.
    with dissolve

    em "I'm tired of seeing you with other girls. Call me jealous or whatever, but I can't be around anymore with you doing all that."

    scene v11seap4a
    with dissolve
    
    scene v11seap4c
    with dissolve

    em "I see the flirting, I see the way you look at them, I see, way too much. And I can't handle it."
    em "A friend of mine has been giving me a lot of good advice recently... and I think I need to start listening to him."

    scene v11seap4d # FPP. Same camera as v10seap4. Show a closer shot of Emily standing in front of MC, slightly annoyed expression, mouth closed.
    with dissolve
    menu:
        "That's fine":
            scene v11seap4d
            with dissolve

            u "That's fine."

            scene v11seap4c
            with dissolve

            em "What do you mean \"that's fine\"?"

            scene v11seap4d
            with dissolve

            u "I mean that's fine. If you don't wanna see each other anymore, that's your choice."

            scene v11seap4c
            with dissolve

            em "You're not even gonna try to change my mind?"

            scene v11seap4d
            with dissolve

            u "Ugh, obviously your mind is made up."
        
        "Be friends":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            scene v11seap4d
            with dissolve

            u "We don't have to see each other, but we can still be friends."

            scene v11seap4c
            with dissolve

            em "No we can't, to me we've never been just friends. We've been in a relationship or wanting to be since the moment we've met."
            
            em "Or, at least one of us was wanting to be. So I'm sorry. but it just won't work."

    if emily_europe: # mc invited emily to europe trip
        scene v11seap4c
        with dissolve

        em "I'm still going on the Europe trip, just... don't expect us to talk."

        scene v11seap4d
        with dissolve

        u "If that's what you want."

    else: # mc didn't invite emily to europe trip
        scene v11seap4c
        with dissolve

        em "And I know you're going on the Europe trip so don't expect me there."

        scene v11seap4d
        with dissolve

        u "Okay..."

    scene v11seap4b
    with dissolve

    em "That's all I wanted to say. Goodbye, [name]."

    scene v11seap4a
    with dissolve

    u "Bye."

    scene v11seap4e # FPP. Same camera as v10seap4. Show Emily walking away from MC.
    with dissolve

    u "(That was sudden.)"
    stop music fadeout 3
    jump v11_nightclub_with_josh