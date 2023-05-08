# SCENE 41: MC, Penelope Call walking Home
# Locations: Town & Streets, Penelope's Dorm
# Characters: MC (Outfit 9), Penelope (Outfit 1)
# Time: Wednesday Night

# -MC is walking back home-

label v10_mc_pen_call:
    scene v10spen1 # TPP. Show MC walking down the sidewalk.
    with fade

    u "(I love college, there's some down times, but plenty of good ones too.)"

    play music music.ck1.v10.Track_Scene_41_1 fadein 2

    scene v10spen2 # TPP. Show MC grabbing his pocket as if he's about to pull his phone out.
    with dissolve

    u "(Phones ringing.)"

    scene v10spen2a # TPP. Show MC on the phone as if he's making a phone call, mouth open.
    with dissolve

    u "Hello?"

    scene v10spen3 # TPP. Show Penelope sat in her dorm on the phone, looking slightly nervous, mouth open.
    with dissolve

    pe "Hey [name]... I just wanted to hear a friendly voice is all."

    scene v10spen2a
    with dissolve

    u "How are you feeling?"

    scene v10spen3
    with dissolve

    pe "Sick to my stomach. I can't even sleep. Tomorrow morning could ruin my entire life."

    scene v10spen2a
    with dissolve

    u "Or it couldn't."

    scene v10spen3
    with dissolve

    pe "Yeah, but-"

    scene v10spen2a
    with dissolve

    u "Look, yes it's true, all hell could break loose."
    u "But it's also true you could just get a little slap on the wrist. We just need to hope for the best and keep a positive attitude."

    scene v10spen3
    with dissolve

    pe "*Sighs* Do you practice these speeches?"

    scene v10spen2b # TPP. Same as 2a, MC smile, mouth open.
    with dissolve

    u "Maybe. For real though, you're an amazing student and the college benefits from you being here."
    u "All of us including myself will make it clear to them how good of a person you are. And who knows, we just may get a miracle."

    scene v10spen3a # TPP. Same as 3, neutral, mouth open.
    with dissolve

    pe "A miracle would be nice."

    scene v10spen2b
    with dissolve

    u "Don't worry. I will represent you in front of the committee and make sure that you'll have the best defense possible."
    u "I will argue the dean to the ground if needed."

    scene v10spen3b # TPP. Same as 3, smile, mouth open.
    with dissolve

    pe "Thank you [name]. I'm glad I called you, I feel a bit more relaxed now. Enough to get some sleep. I probably won't get much though,"

    scene v10spen2b
    with dissolve

    u "You're welcome Penelope, see you in the morning."

    scene v10spen3b
    with dissolve

    pe "See ya, bye."

    scene v10spen4 # TPP. Show MC hanging up the phone and continuing to walk on.
    with dissolve

    u "(I really hope tomorrow goes well.)"

    stop music fadeout 3
    play music music.ck1.v10.Track_Scene_41_2 fadein 2
    if joinwolves:

        scene v10spen5 # TPP. Show MC in his new wolves room, lying on his bed tired.
        with dissolve

        u "(That was a long day.)"

        scene black
        with dissolve

        pause 1

    else:

        scene v10spen6 # TPP. Show MC in his apes room, lying on his bed tired.
        with dissolve

        u "(That was a long day.)"

        scene black
        with dissolve

        pause 1
    stop music fadeout 3

    jump v10_waking_up_end

    # -Transition to Scene 41A-
