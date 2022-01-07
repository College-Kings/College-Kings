# SCENE 43a: Walk to Mr. Lee's class with Penelope
# Locations: College, Mr. Lee Classroom
# Characters: MC (Outfit: 1), PENELOPE (Outfit: 1)
# Time: Morning

label v14s43a:
    scene v14s43a_1 # TPP. Show MC and Penelope walking together, both smiling, mouths closed (NOT holding hands). They are in the college
    with dissolve

    pause 0.75

    play music "music/v12/Track Scene 13.mp3" fadein 2

    if penelope.relationship.value >= Relationship.LOYAL.value:
        scene v14s43a_2 # TPP. Show MC and Penelope walking together, holding hands, smiling, mouths closed, different location to v14s43a_1
        with dissolve

        pause 0.75

    else:
        scene v14s43a_2a # TPP. Same as v14s43a_2, but Penelope and MC not holding hands
        with dissolve

        pause 0.75

    scene v14s43a_3 # FPP. MC and Penelope in the college hallway, standing next to each other, Penelope smiling, mouth closed
    with dissolve

    u "Oh, and just so you know... You snore super loudly. *Laughs* I'm sure you already knew that though."

    scene v14s43a_3a # FPP. Same as v14s43a_3, Penelope smiling, mouth open
    with dissolve

    pe "What?! I do not! Stop it, [name]."

    scene v14s43a_3
    with dissolve

    u "You were like..."

    u "*Loud snoring sounds*"

    scene v14s43a_3a
    with dissolve

    pe "Oh my- Stop! *Chuckles*"

    scene v14s43a_3b # FPP. Same as v14s43a_3a, Penelope slight smile, but also slightly serious, mouth open
    with dissolve

    pe "Please never bring that up again."

    scene v14s43a_3
    with dissolve

    u "Yeah, sure..."

    scene v14s43a_3a
    with dissolve

    pe "[name]!"

    scene v14s43a_3
    with dissolve

    u "Haha! You weren't actually snoring... Just kidding."

    scene v14s43a_3a
    with dissolve

    pe "You're not funny."

    scene v14s43a_3
    with dissolve

    u "I'll be funny once I tell everyone that you snore, though."

    scene v14s43a_3b
    with dissolve

    pe "You wouldn't do that."

    scene v14s43a_3
    with dissolve

    u "Wouldn't I?"

    scene v14s43a_3c # FPP. Same as v14s43a_3, Penelope rolling her eyes and laughing
    with dissolve

    pause 0.75

    if v14_emily_ily:
        play sound "sounds/vibrate.mp3"

        scene v14s43_3 # TPP. Show MC walking through the school, close to where he was in v14s43_2, grabbing his phone, slightly confused, mouth closed
        with dissolve

        u "(Hmm?)"

        scene v14s43_3a # TPP. Same as v14s43_3, MC looking down at his phone, slight smile, mouth closed
        with dissolve

        $ emily.messenger.newMessage("Hey you. How's your day going?", force_send=True)
        $ emily.messenger.addReply("It's barely started, haha. What about yours?")
        $ emily.messenger.newMessage("Not bad. Still in bed... Lol")
        $ emily.messenger.addReply("Oh yeah?")
        $ emily.messenger.newMessage("Haha...")
        $ emily.messenger.newImgMessage("images/v14/Scene 43/v14kw43.webp")
        $ emily.messenger.addReply("...Yes")
        $ emily.messenger.newMessage("Hahaha")
        $ emily.messenger.addReply("I mean, no. I might need some more evidence...")
        $ emily.messenger.newMessage("Hehe ;) Get to class, we'll talk soon, I miss you <3")
        $ emily.messenger.addReply("Fine... miss you more :)")

        label v14s43a_PhoneContinueEmily:
            if emily.messenger.replies:
                call screen phone
            if emily.messenger.replies:
                u "(I should check my phone.)"
                jump v14s43a_PhoneContinueEmily

        scene v14s43_3b # TPP. Same as v14s43_3a, MC putting his phone away
        with dissolve

        u "(Glad to see that Emily's still up to no good, haha.)"

        scene v14s43a_3b
        with dissolve
        
        pe "Good news? Bad news?"

        scene v14s43a_3
        with dissolve
        
        u "Uhh... no, nothing important..."
    
        u "(I need to be careful with my phone in public.)"

        if v7_emily_bowling:
            u "(Last time that Penelope learned about Emily she got upset.)"

        scene v14s43a_3a
        with dissolve
        
        pe "Let's go then."

    scene v14s43a_4 # TPP. Show MC and Penelope walking through the college, close to the classroom, both smiling, mouths closed (not holding hands)
    with dissolve

    pause 0.75

    scene v14s43a_5 # TPP. Show MC and Penelope entering the classroom, both smiling, mouths closed
    with fade

    pause 0.75

    scene v14s43a_6 # TPP. Show MC and Penelope taking their seats next to each other, both smiling, mouths closed
    with dissolve

    pause 0.75

    scene v14s43a_6a # TPP. Same as v14s43a_6, MC and Penelope now fully sitting down next to each other, smiling, mouths closed
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v14s43b