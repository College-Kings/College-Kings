# Wolves Gym Intro
# Location: Wolves Gym
# Outfits: MC Outfit 3, Sebastian Outfit 1
# Time: Saturday Evening

label wolves_gym_intro:
    play music music.ck1.m11punk fadein 2

    scene v8swgym1 # FPP. Shot of the Wolves gym, Sebastian in view, mouth open, arms out as if introducing someone to a location.
    with Fade(0.75, 0.25, 0.75)

    se "Our pack house."

    scene v8swgym2 # TPP. Show MC looking around Wolves gym, MC smile, mouth open.
    with dissolve

    u "Nice. Reminds me of the setup I had back home."

    pause 0.5

    scene v8swgym3 # FPP. Show Sebastian looking at camera with a confused expression, mouth closed.
    with dissolve

    u "I had it... Doesn't mean I used it."

    scene v8swgym3a # FPP. Same camera as v8swgym3, Sebastian smile, mouth open.
    with dissolve
    
    se "Well, we'll get you in fighting shape, don't worry."

    jump work_with_seb
