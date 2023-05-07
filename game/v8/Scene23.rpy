# Josh Calls You
# Location: MC Apes Room, MC Wolves Room
# Outfits: MC Outfit 3
# Time: Monday Morning

label josh_calls_you:
    if joinwolves:
        scene v8sjc1 # TPP. Show MC sat at his desk in his Wolves room chilling.
        with dissolve

        pause 0.5

        play sound sound.call

        scene v8sjc2 # TPP. Show MC's phone ringing on his bed, it's Josh on the caller ID.
        with dissolve

        u "(Wonder who's calling.)"

        scene v8sjc3 # TPP. Show MC walking over to his phone on his bed to pick it up.
        with dissolve

        pause 0.5

        stop sound
        play sound sound.answer_call

        scene v8sjc4 # TPP. Show MC stood up in his room on the phone to Josh, MC slightly confused expression, mouth open.
        with dissolve

        u "Hello?"

        scene v8sjc4a # TPP. Same camera as v8sjc4, MC slightly confused expression, mouth closed.
        with dissolve

        jo "Hey yo, its Josh, what's up man?"

        scene v8sjc4b # TPP. Same camera as v8sjc4, MC slight smile, mouth open.
        with dissolve

        u "Not much. Just chilling in my room. What's up?"

        scene v8sjc4c # TPP. Same camera as v8sjc4, MC slight smile, mouth closed.
        with dissolve

        jo "Well, look, I got something to talk to you about, so would you mind swinging by?"

        scene v8sjc4
        with dissolve

        u "Why? Is something wrong?"

        scene v8sjc4a
        with dissolve

        jo "No, no, nothing wrong, just don't wanna say it over the phone, you get me?"

        scene v8sjc4d # TPP. Same camera as v8sjc4, MC neutral expression, mouth open.
        with dissolve

        u "Yeah I got you. I'll be right over."

        scene v8sjc4e # TPP. Same camera as v8sjc4, MC neutral expression, mouth closed.
        with dissolve

        jo "Awesome! See you then bro!"

        play sound sound.reject_call
        stop music fadeout 3

        scene v8sjc5 # TPP. Show MC hanging up the phone.
        with dissolve

        u "(Well, I guess I'll head over there then.)"

        scene v8sjc6 # TPP. Show MC leaving his Wolves room.
        with dissolve

        pause 0.75

    else:
        scene v8sjc7 # TPP. Show MC sat at his desk in his Apes room chilling.
        with dissolve

        pause 0.5

        play sound sound.call

        scene v8sjc8 # TPP. Show MC's phone ringing on his bed, it's Josh on the caller ID.
        with dissolve

        u "(Wonder who's calling.)"

        scene v8sjc9 # TPP. Show MC walking over to his phone on his bed to pick it up.
        with dissolve

        pause 0.5

        stop sound
        play sound sound.answer_call

        scene v8sjc10 # TPP. Show MC stood up in his room on the phone to Josh, MC slightly confused expression, mouth open.
        with dissolve

        u "Hello?"

        scene v8sjc10a # TPP. Same camera as v8sjc10, MC slightly confused expression, mouth closed.
        with dissolve

        jo "Hey yo, its Josh, what's up man?"

        scene v8sjc10b # TPP. Same camera as v8sjc10, MC slight smile, mouth open.
        with dissolve

        u "Not much. Just chilling in my room. What's up?"

        scene v8sjc10c # TPP. Same camera as v8sjc10, MC slight smile, mouth closed.
        with dissolve

        jo "Well, look, I got something to talk to you about, so would you mind swinging by?"

        scene v8sjc10
        with dissolve

        u "Why? Is something wrong?"

        scene v8sjc10a
        with dissolve

        jo "No, no, nothing wrong, just don't wanna say it over the phone, you get me?"

        scene v8sjc10d # TPP. Same camera as v8sjc10, MC neutral expression, mouth open.
        with dissolve

        u "Yeah I got you. I'll be right over."

        scene v8sjc10e # TPP. Same camera as v8sjc10, MC neutral expression, mouth closed.
        with dissolve

        jo "Awesome! See you then bro!"

        play sound sound.reject_call

        # -Josh hangs up-
        stop music fadeout 3

        scene v8sjc11 # TPP. Show MC hanging up the phone.
        with dissolve

        u "(Well, I guess I'll head over there then.)"

        scene v8sjc12 # TPP. Show MC leaving his Apes room.
        with dissolve

        pause 0.75

    jump josh_room