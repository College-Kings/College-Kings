# Economics Class
# Location: Economics Class
# Outfits: MC Outfit 2, Ryan Outfit 1, Lauren Outfit 3, Ms. Rose Outfit 1, Riley Outfit 4 (Make sure to use .duf where Riley is wearing glasses)
# Time: Tuesday Morning

label mr_aft_class:
    if joinwolves:
        scene v8saec1 # TPP. Show everyone in the class standing up from their seats in preparation to leave the class.
        with dissolve
        pause 0.5

        play music "music/mindie3.mp3"

        scene v8saec2 # FPP. Show Ms. Rose looking at MC (Camera), gesturing to come over, neutral expression, mouth open.
        with dissolve

        ro "[name], can I speak with you for a moment?"

        scene v8saec3 # FPP. Show Ryan who is stood up looking at camera, Ryan slight confused expression, mouth open.
        with dissolve

        ry "Dude, what did you do?"

        scene v8saec4 # TPP. Show MC looking at Ryan, MC shrugging, unsure expression, Ryan confused expression, mouth closed.
        with dissolve

        u "(I'm sure Ms. Rose doesn't want anyone knowing her business.)"

        scene v8saec5 # TPP. Show MC walking to the front of the class, everyone else leaving through the door.
        with dissolve

        pause 0.5

        scene v8saec6 # FPP. MC now at the front of the class infront of Ms. Rose. Show Ms. Rose, neutral expression, mouth open.
        with dissolve

        ro "I just wanted to thank you for all your help this weekend."

        scene v8saec6a # FPP. Same camera as v8saec6, mouth closed.
        with dissolve

        u "Don't mention it. I'm glad we could get you out of there."

        scene v8saec6b # FPP. Same camera as v8saec6, Ms. Rose looking a little bit sad, mouth open.
        with dissolve

        ro "I'm sorry I was so emotional. It's not like me."

        scene v8saec6c # FPP. Same camera as v8saec6, Ms. Rose looking a little bit sad, mouth closed.
        with dissolve

        u "Hey, don't worry about it. You have every right to feel whatever you're feeling. I'm sure it couldn't have been easy."

        scene v8saec6d # FPP. Same camera as v8saec6, Ms. Rose looks down slightly, looking sad, mouth open.
        with dissolve

        ro "No, it wasn't. Mr. Rose and I... we spent so many happy years together. I tried so hard to wait for him to get better, but I don't think that's possible now."

        scene v8saec6
        with dissolve

        menu:
            "Ask more questions":
                $ reputation.add_point(RepComponent.BOYFRIEND)
                jump ask_rose_more_q
            "Leave":
                jump no_ask_rose_more_q

    else:
        jump hallway_w_nora

label ask_rose_more_q:
    u "I know it's none of my business, but are you alright? Is he still bothering you? Do you feel safe?"

    scene v8saec6d
    with dissolve

    ro "He... he's not taking it well. But he doesn't know where I moved to. So he can't find me. I think it's for the best."

    scene v8saec6
    with dissolve

    u "Me too. We have to keep you safe!"

    jump aec_rose_end

label no_ask_rose_more_q:
    u "(I'm sure she doesn't want to think about this stuff at school.)"

    jump aec_rose_end

label aec_rose_end:
    u "You let me know if you need anything else. We're here for you. I gotta get going before I'm late to my next class."

    scene v8saec6e # FPP. Same camera as v8saec6, Ms. Rose cracks a little smile, mouth open.
    with dissolve

    ro "Of course. Tell Chris and the other boys how thankful I am to have you guys around."

    scene v8saec6f # FPP. Same camera as v8saec6, Ms. Rose cracks a little smile, mouth closed.
    with dissolve

    u "I will."

    scene v8saec7 # FPP. Show MC walking towards the exit of Economics Class Room, Ms. Rose slight smile, mouth closed.
    with dissolve

    pause 0.5

    stop music fadeout 3

    scene v8saec8 # TPP. Show MC now wear the exit of the class room, MC smile waving to Ms. Rose, Ms. Rose smile waving back.
    with dissolve
    pause 0.5

    jump hallway_w_nora