# SCENE 28: Call With Lindsey
# Locations: MC Wolves/Apes Room, Lindsey's Room
# Characters: MC (Outfit 3), Lindsey (Outfit 1)
# Time: Friday Night

label v9_call_w_lindsey:
    if joinwolves:
        scene v9cwl3 # TPP. Show MC on his bed in his Wolves room, phone in hand, looking tired.
        with fade

        play music "music/v9/Track Scene 3.mp3" fadein 2

        u "(What a jam-packed day. And this wasn't even the real deal. Tomorrow is showtime.)"
        u "(I didn't see myself going down this road when I started college, but I'm in too deep now. There's no way I'll lose, no way in hell.)"

        play sound "sounds/calling.mp3"
        pause 1

        stop sound

        scene v9cwl3a # TPP. Same camera as v9cwl1, MC looking at his phone.
        with dissolve

        u "(I wonder who's calling this late. Oh, it's Lindsey.)"

        scene v9cwl3b # TPP. Show MC on the phone, smile, mouth open.
        with dissolve

        u "Hey Linds!"

        scene v9cwl2 # TPP. Show Lindsey on the phone, smile, mouth open (Now in Lindsey's room).
        with dissolve

        li "\"Linds\", so we're on a nickname basis now huh?"

        scene v9cwl3c # TPP. Same camera as v9cwl1, MC neutral expression, mouth open.
        with dissolve

        u "I'd say we are."

        scene v9cwl2
        with dissolve

        li "So freshmeat..."

        scene v9cwl3b
        with dissolve

        u "\"Freshmeat\", please say that's something you just came up with and not something people are calling me."

        scene v9cwl2
        with dissolve

        li "Ha, guess you'll never know. Anyway though, I called to ask how you're feeling about the fight tomorrow?"

        li "This fight could be major for you. Think you'll come out on top?"

        scene v9cwl3b
        with dissolve

        if kct == "confident":
            u "Does a fish need water? Of course I'll come out on top. When I set my mind to something that's it, mission accomplished."

        elif kct == "popular":
            u "I know there's a lot of focus on me, but I'm just really focused on bringing this home for the boys. They deserve this and I wanna make 'em proud."

        else:
            u "I've been training hard. For someone that had never fought before, I feel I'm doing pretty well. So I feel pretty good about my chances."

        scene v9cwl2a # TPP. Same camera as v9cwl2, Lindsey neutral expression
        with dissolve

        li "I like where your head is at. Just don't go acting a fool and getting yourself hurt."

        scene v9cwl3b
        with dissolve

        u "Awww, school magazine front page, Linds cares deeply for [name]'s safety."

        scene v9cwl2
        with dissolve

        li "Keep calling me by that little nickname and I may care a little less."

        scene v9cwl3d # TPP. Same camera as v9cwl1, MC laugh, mouth open.
        with dissolve

        u "So are you calling all the fighters tonight or just me?"

        scene v9cwl2
        with dissolve

        li "Someone's looking to feel special before his big day I see."
        li "If you must know, some of my girlfriends were talking about some of this year's new fighters and your name came up so I thought I'd see how you were feeling."

        scene v9cwl3b
        with dissolve

        u "Haha, that's sweet of you."

        scene v9cwl2
        with dissolve

        li "I know. I could be even sweeter."

        scene v9cwl3b
        with dissolve

        u "Yeah? You could, huh?"

        scene v9cwl2
        with dissolve

        li "Maybe. Wishing you well tomorrow, goodnight."

        scene v9cwl3c
        with dissolve

        u "Goodnight."

        play sound "sounds/rejectcall.mp3"

        scene v9cwl3
        with dissolve

        u "(Was she hinting at something? \"I could be even sweeter\", what does that mean? Oh well, time to get some rest. I got a big day tomorrow.)"

        scene v9cwl3e # TPP. Same camera as v9cwl1, Show MC no longer on the phone, lying on his side to go to sleep.
        with dissolve

        scene black
        with dissolve

        pause 1

        jump v9_your_room_satmorn

    else:
        scene v9cwl1 # TPP. Show MC on his bed in his Apes room, phone in hand, looking tired.
        with fade

        u "(What a jam-packed day. And this wasn't even the real deal. Tomorrow is showtime.)"
        u "(I didn't see myself going down this road when I started college, but I'm in too deep now. There's no way I'll lose, no way in hell.)"

        play sound "sounds/calling.mp3"
        pause 1

        stop sound

        scene v9cwl1a # TPP. Same camera as v9cwl1, MC looking at his phone.
        with dissolve

        u "(I wonder who's calling this late. Oh, it's Lindsey.)"

        scene v9cwl1b # TPP. Show MC on the phone, smile, mouth open.
        with dissolve

        u "Hey Linds!"

        scene v9cwl2 # TPP. Show Lindsey on the phone, smile, mouth open (Now in Lindsey's room).
        with dissolve

        li "\"Linds\", so we're on a nickname basis now huh?"

        scene v9cwl1c # TPP. Same camera as v9cwl1, MC neutral expression, mouth open.
        with dissolve

        u "I'd say we are."

        scene v9cwl2
        with dissolve

        li "So freshmeat..."

        scene v9cwl1b
        with dissolve

        u "\"Freshmeat\", please say that's something you just came up with and not something people are calling me."

        scene v9cwl2
        with dissolve

        li "Ha, guess you'll never know. Anyway though, I called to ask how you're feeling about the fight tomorrow. This could be major for you. Think you'll come out on top?"

        scene v9cwl1b
        with dissolve

        if kct == "confident":
            u "Does a fish need water? Of course I'll come out on top. When I set my mind to something that's it, mission accomplished."

        elif kct == "popular":
            u "I know there's a lot of focus on me, but I'm just really focused on bringing this home for the boys. They deserve this and I wanna make 'em proud."

        else:
            u "I've been training hard. For someone that had never fought before, I feel I'm doing pretty well. So I feel pretty good about my chances."

        scene v9cwl2a # TPP. Same camera as v9cwl2, Lindsey neutral expression
        with dissolve

        li "I like where your head is at. Just don't go acting a fool and getting yourself hurt."

        scene v9cwl1b
        with dissolve

        u "Awww, school magazine front page, Linds cares deeply for [name]'s safety."

        scene v9cwl2
        with dissolve

        li "Keep calling me by that little nickname and I may care a little less."

        scene v9cwl1d # TPP. Same camera as v9cwl1, MC laugh, mouth open.
        with dissolve

        u "So are you calling all the fighters tonight or just me?"

        scene v9cwl2
        with dissolve

        li "Someone's looking to feel special before his big day I see."
        li "If you must know, some of my girlfriends were talking about some of this year's new fighters and your name came up so I thought I'd see how you were feeling."

        scene v9cwl1b
        with dissolve

        u "Haha, that's sweet of you."

        scene v9cwl2
        with dissolve

        li "I know. I could be even sweeter."

        scene v9cwl1b
        with dissolve

        u "Yeah? You could, huh?"

        scene v9cwl2
        with dissolve

        li "Maybe. Wishing you well tomorrow, goodnight."

        scene v9cwl1c
        with dissolve

        u "Goodnight."

        play sound "sounds/rejectcall.mp3"

        scene v9cwl1
        with dissolve

        u "(Was she hinting at something? \"I could be even sweeter\", what does that mean? Oh well, time to get some rest. I got a big day tomorrow.)"

        scene v9cwl1e # TPP. Same camera as v9cwl1, Show MC no longer on the phone, lying on his side to go to sleep.
        with dissolve

        scene black
        with dissolve

        stop music fadeout 3

        pause 1

        jump v9_your_room_satmorn
