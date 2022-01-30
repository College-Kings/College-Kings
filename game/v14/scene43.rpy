# SCENE 43: Walk to Mr. Lee's class by yourself
# Locations: College, Mr. Lee Classroom
# Characters: MC (Outfit: 1), PENELOPE (Outfit: 1)
# Time: Morning
# Phone Images: YES
# v14kw43: Emily is laying flat on her back in her bed, one arm holding the phone for selfie, the other trying to cover her nipples but slightly failing, we see a bit of the panties she has on, she's making a kissy face

label v14s43:
    scene v14s43_1 # TPP. Show MC walking through the school, slight smile, mouth closed
    with fade

    pause 0.75

    play music "music/v12/Track Scene 13.mp3" fadein 2

    scene v14s43_2 # TPP. Show MC walking through the school (different location), slight smile, mouth closed
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

        label v14s43_PhoneContinueEmily:
            if emily.messenger.replies:
                call screen phone
            if emily.messenger.replies:
                u "(I should check my phone.)"
                jump v14s43_PhoneContinueEmily

        scene v14s43_3b # TPP. Same as v14s43_3a, MC putting his phone away
        with dissolve

        u "(Glad to see that Emily's still up to no good, haha.)"

    scene v14s43_4 # TPP. Show MC walking into class, slight smile, mouth closed
    with fade

    pause 0.75

    scene v14s43_5 # TPP. Show MC walking up to Penelope, she is sitting alone at the table, slightly smiling, mouth closed, MC slightly worried, mouth closed
    with dissolve

    pause 0.75

    scene v14s43_6 # FPP. MC standing next to the empty seat, looking at Penelope, she is sitting down, looking at him, slight smile, mouth closed
    with dissolve

    u "This seat taken?"

    scene v14s43_6a # FPP. Same as v14s43_6, Penelope slight smile, mouth open
    with dissolve

    if penelope.relationship >= Relationship.LIKES:
        pe "Saved, actually."

        scene v14s43_6
        with dissolve

        u "Oh?"

        scene v14s43_6a
        with dissolve

        pe "For this cute guy with brown fluffy hair and an amazing smile."

        scene v14s43_7 # TPP. Show MC smirking at Penelope, she is slightly embarassed, both mouths closed
        with dissolve

        pause 0.75

        scene v14s43_6a
        with dissolve

        pe "Sit down already, weirdo. *Chuckles*"

    else:
        pe "That depends..."

        scene v14s43_6
        with dissolve

        u "On what?"

        scene v14s43_6a
        with dissolve

        pe "Which type of bear is best?"

        scene v14s43_6
        with dissolve

        u "What? *Chuckles* What do you-"

        scene v14s43_6a
        with dissolve

        pe "False. Black bear."

        scene v14s43_6
        with dissolve

        u "Wait, how do you even-"

        scene v14s43_6a
        with dissolve

        pe "Sit down already, would you? People are starting to stare... *Laughs*"

    scene v14s43_8 # TPP. Show MC sitting down next to Penelope
    with dissolve
    
    pause 0.75

    scene v14s43_9 # FPP. MC sitting down next to Penelope, Penelope looking at him, slight smile, mouth closed
    with dissolve

    u "*Laughs* Good one."

    scene v14s43_9a # FPP. Same as v14s43_9, Penelope slight smile, mouth open
    with dissolve

    pe "Thank you."

    stop music fadeout 3

    jump v14s43b