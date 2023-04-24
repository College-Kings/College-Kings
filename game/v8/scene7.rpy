# Scene 7 - Cafe With Aubrey
# Note to renderers, MC wearing outfit 3, Aubrey wearing outfit 1.
label caf_w_aub:
    scene scaf5 # FPP. Sweeping shot of inside the cafe, show Aubrey sat at a table on her own.
    with fade

    pause 0.75

    scene scaf6 # FPP. Closer to where Aubrey is sat in the Cafe.
    with dissolve

    u "Can I join you?"

    scene scaf6a # FPP. Same camera as scaf6, but Aubrey turns to look at the camera, Aubrey smile.
    with dissolve

    pause 0.75

    scene scaf6b # FPP. Same camera as scaf6, but Aubrey turns to look at the camera, Aubrey smile, mouth open.
    with dissolve

    au "Hey! Yeah, join me."

    scene scaf7 # TPP. Show MC sitting at table with Aubrey, MC should be sitting directly opposite Aubrey.
    with dissolve

    pause 0.75

    scene scaf8 # FPP. Close up of Aubrey sat at cafe table, Aubrey slight smile.
    with dissolve

    if CharacterService.is_fwb(aubrey):
        u "How you doin?"

        scene scaf8a # FPP. Same camera as scaf8, Aubrey slight smile, mouth open.
        with dissolve

        au "Good. Can't complain."

        scene scaf8
        with dissolve

        u "You look good today."

        scene scaf8b # FPP. Same camera as scaf8, Aubrey laugh, one brow raised, mouth open.
        with dissolve

        au "I just woke up."

        scene scaf8
        with dissolve

        u "Should've woken up next to me."

        scene scaf8c # FPP. Same camera as scaf8, Aubrey laugh, mouth open.
        with dissolve

        au "Haha! Someone's horny."

        scene scaf8
        with dissolve

        u "Maybe."

        scene scaf8d # FPP. Same camera as scaf8, Aubrey leaning forward out of chair a bit over table towards camera, Aubrey smirk, mouth open.
        with dissolve

        au "Maybe I am too."

        scene scaf8
        with dissolve

        pause 0.75

        scene scaf8a
        with dissolve

        au "So, you have a good night?"

        scene scaf8
        with dissolve

        u "Yeah, yeah. You?"

        scene scaf8a
        with dissolve

        au "Yeah I actually did."

        if ending != "amber":
            scene scaf8
            with dissolve

            u "Your dress was sexy as fuck."

            scene scaf8a
            with dissolve

            au "You didn't think I'd show up in something ugly?"

            scene scaf8
            with dissolve

            u "Just saying, it looked good."

        scene scaf8e # FPP. Same camera as scaf8, Aubrey neutral expression, mouth open.
        with dissolve
        au "You have a lot going on today?"

        if protest:
            play sound "sounds/call.mp3"

            scene scaf9 # TPP. Show MC and Aubrey, MC has his phone in hand as Autumn is calling him. Aubrey neutral expression, MC neutral expression mouth open.
            with dissolve

            u "Hold on, let me get this."

            scene scaf9a # TPP. Same camera as scaf9a, Show MC walking away from the table now on the phone, MC mouth closed. Aubrey neutral expression mouth open.
            with dissolve
            stop sound
            play sound "sounds/answercall.mp3"
            au "Okay."

            jump au_prot_call

        else:
            jump cafe_no_call

    else:
        u "Eating alone?"

        scene scaf8a
        with dissolve

        au "Well it is just breakfast. Do I always have to be with someone?"

        scene scaf8
        with dissolve

        u "No, just figured you know last night, homecoming. Everyone seemed to be with someone."

        scene scaf8d
        with dissolve

        au "Well I guess, even if I was with someone, I don't need them following me around the next day."

        scene scaf8
        with dissolve

        u "True. I feel you on that one."

        scene scaf8a
        with dissolve

        au "So, you enjoy your night?"

        scene scaf8
        with dissolve

        u "Yeah. It was cool. Yours?"

        scene scaf8a
        with dissolve

        au "I actually had a lot of fun at the dance."

        if ending != "amber":
            scene scaf8
            with dissolve

            u "That's good. Your dress looked great."

            scene scaf8a
            with dissolve

            au "Thanks. Not so much of an evening gown girl, but I liked the dress I found."

            scene scaf8
            with dissolve

            u "Yeah, good pick."

        scene scaf8e
        with dissolve
        au "So you got a lot going on today?"

        if protest:
            play sound "sounds/call.mp3"

            scene scaf9
            with dissolve

            u "Hold on, I'm gonna take this."

            scene scaf9a # TPP. Same camera as scaf9a, Show MC walking away from the table now on the phone, MC mouth closed. Aubrey neutral expression mouth open.
            with dissolve
            
            stop sound
            play sound "sounds/answercall.mp3"
            au "Okay."

            jump au_prot_call

        else:
            jump cafe_no_call

label cafe_no_call:
    scene scaf8
    with dissolve

    if joinwolves:
        u "Nothing in particular except for some of the Wolves' stuff."

    else:
        u "Apes joining ceremony is tonight, so there's that."

    u "What about you?"

    scene scaf8a
    with dissolve
    au "Same old, same old."

    scene scaf8
    with dissolve
    u "Mhm. Can I have a bite? I'm starving."

    stop music fadeout 3

    scene black
    with Dissolve(1)
    pause 0.75

    if joinwolves:
        jump after_prot_wolves

    else:
        jump after_prot_dorm

label au_prot_call:
    scene scaf10 # TPP. Show MC stood in a corner of the café on the phone to Autumn, neutral expression, mouth open.
    with dissolve
    u "Hello?"

    scene scaf10a # TPP. Same camera as scaf10, neutral expression, mouth closed.
    with dissolve

    aut "Hey, you still coming to the protest?"

    scene scaf10a
    with dissolve

    menu:
        "Go to the protest":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            jump caf_prot_au

        "Don't go to the protest":
            jump caf_no_prot_au

label caf_prot_au:
    scene scaf10
    with dissolve

    u "Oh yeah, the protest."

    scene scaf10a
    with dissolve

    aut "Haha did you forget?"

    scene scaf10
    with dissolve

    u "No, no. Not at all. I'm coming right now."

    scene scaf10a
    with dissolve

    aut "Okay. See you soon!"

    scene scaf10b
    with dissolve

    pause 0.75

    scene scaf12 # TPP. Show Aubrey sat at table, with MC stood opposite her, Aubrey neutral expression looking up at MC, mouth closed, MC neutral expression, mouth open.
    with dissolve

    u "Hey, I totally forgot, I did have something going on today."

    scene scaf13 # FPP. Show Aubrey looking into camera, nautral expression, mouth open.
    with dissolve

    au "Yeah, it's cool."

    scene scaf13a # FPP. Same camera as scaf13, Aubrey neutral expression, mouth closed.
    with dissolve

    u "See you around?"

    scene scaf13b # FPP. Same camera as scaf13, Aubrey smile, mouth open.
    with dissolve

    au "Yeah."

    stop music fadeout 3

    scene scaf14 # TPP. Show MC walking towards the cafe door, leaving the cafe, Camera from behind MC.
    with dissolve

    pause 0.75

    jump prot_w_au

label caf_no_prot_au:
    scene scaf10
    with dissolve

    u "Hey, sorry. Meant to call you earlier. Woke up and I'm feeling really under the weather today."

    scene scaf10a
    with dissolve

    aut "Oh... yeah, it's cool!"

    scene scaf10
    with dissolve

    u "Yeah, so sorry. I'll definitely try and catch the next one."

    scene scaf10a
    with dissolve

    aut "Yeah okay. Feel better."

    scene scaf10
    with dissolve

    u "Thanks."

    scene scaf10b # TPP. Same camera as scaf10, show MC walking out of view, no longer on the phone, neutral expression, mouth closed.
    with dissolve

    pause 0.75

    scene scaf12a # TPP. Same camera as scaf12, Aubrey neutral expression looking up at MC, mouth open, MC neutral expression, mouth closed.
    with dissolve

    au "Who was that?"

    scene scaf15 # TPP. Show MC sitting back down at the table with Aubrey, sat opposite as in scaf7. MC mouth open, Aubrey mouth closed.
    with dissolve

    u "Just a friend."

    scene scaf8a
    with dissolve

    au "Oh okay. Sounded like you had to be somewhere."

    scene scaf8
    with dissolve

    u "I probably should be heading off actually."

    scene scaf8a
    with dissolve

    au "Well don't let me keep you."

    scene scaf8
    with dissolve

    u "See you later Aubrey."

    scene scaf8a
    with dissolve
    au "Bye [name]."

    scene scaf16 # TPP MC getting out of his chair leaving Aubrey sittin there, both smiling.
    with dissolve
    pause 0.75

    scene scaf17 # TPP MC heading to the door, aubs still sitting there watching him go.
    with dissolve
    pause 0.75

    scene scaf18 # TPP MC walking down the street going home.
    with dissolve
    pause 0.75
    
    stop music fadeout 3

    scene black
    with Dissolve(1)
    pause 0.75

    if joinwolves:
        jump after_prot_wolves

    else:
        jump after_prot_dorm