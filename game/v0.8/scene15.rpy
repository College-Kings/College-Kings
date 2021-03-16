# Penelo
# Location: MC's Apes Room OR MC Wolves Room
# Outfits: MC Outfit 2
# Time: Sunday Morning

label penelope_dorm_hack:
    scene v8spen1 # FPP. Long shot of the hallway leading up to Penelope's dorm.
    with fade

    pause 0.5

    scene v8spen2 # TPP. Show MC knocking on Penelope's dorm door.
    with dissolve

    pause 0.5

    scene v8spen2a # TPP. Same camera as v8spen2, MC now stood infront of the door, no longer knocking.
    with dissolve

    pe "It's open!"

    scene v8spen3 # FPP. Now inside Penelope's dorm, show Penelope sitting on her bed, crying.
    with dissolve

    u "Penelope?"

    scene v8spen3a # FPP. Same camera as v8spen3, show Penelope quickly standing up walking towards MC with pace. Penelope still upset.
    with dissolve

    pause 0.5

    scene v8spen4 # TPP. Show Penelope hugging MC. Penelope still upset. MC mouth open.
    with dissolve

    u "Hey, hey, hey. It's okay. I've got you."

    scene v8spen5 # FPP. Close up Penelope, Penelope crying, mouth closed.
    with dissolve

    u "Talk to me. Tell me everything, okay?"

    scene v8spen5a # FPP. Same camera as v8spen5, Penelope trying to compose herself, mouth open.
    with dissolve

    pe "*Sniffles* O-okay, remember when you saw me in the hall at Hoco? And I was on the phone?"

    scene v8spen5b # FPP. Same camera as v8spen5, Penelope trying to compose herself, mouth closed.
    with dissolve

    u "Yeah, I remember. You seemed really upset on the phone."

    scene v8spen5a
    with dissolve

    pe "Well I was talking to my friend who got kicked out of her college, Jenny, and she couldn't get into any s-school because of what happened at her..."

    scene v8spen5c # FPP. Same camera as v8spen5, Penelope looking away from the camera (to her side). Mouth open.
    with dissolve

    pe "Last school, so I hacked into San Vallejo's registry and enrolled her here, only I-I got caught somehow."

    scene v8spen5a
    with dissolve

    pe "I was really careful and I covered my tracks and..."

    scene v8spen5d # FPP. Same camera as v8spen5, Penelope looking back at the camera, looking angry and upset, mouth open.
    with dissolve

    pe "I still got caught. What am I gonna do? I can't go to jail and I don't have $15 thousand lying around! My life is fucked!"

    scene v8spen6 # FPP. Show Penelope walking off to sit back on the edge of her bed again, still upset.
    with dissolve

    pause 0.5

    scene v8spen7 # TPP. Show MC sat on the edge of the bed next to Penelope, both looking at eachother Penelope mouth open, still upset.
    with dissolve

    pe "I'm sorry. I'm just so scared!"

    scene v8spen8 # FPP. Close up Penelope (sat on edge of bed), Penelope upset, mouth closed.
    with dissolve

    menu:
        "Offer to help Penelope":
            $ addPoint ("bf", 1)
            jump help_pen

        "Offer to support Penelope":
            jump no_help_pen

label help_pen:

    u "If you want, I can talk to the Dean on Monday on your behalf. I'm sure we could work something out if we tried and be smart about it."

    scene v8spen8a # FPP. Same camera as v8spen8, Penelope upset, mouth open.
    with dissolve

    pe "I don't know. Why would he listen to you or me?"

    scene v8spen8
    with dissolve

    u "Well, it can't hurt to try. We gotta do something, right?"

    scene v8spen8b # FPP. Same camera as v8spen8, Penelope still upset but also slightly smiling, mouth open.
    with dissolve

    pe "Okay. I guess we can do that."

    scene v8spen8c # FPP. Same camera as v8spen8, Penelope still upset but also slightly smiling, mouth closed.
    with dissolve

    u "Yeah? We got this. First thing Monday morning, I'll go see the Dean, okay?"

    scene v8spen9 # FPP. Show Penelope hugging MC. Penelope smiling.
    with dissolve

    pause 0.5

    scene v9spen8d # FPP. Same camera as v8spen8, Penelope dries her eyes and regains some composure. Penelope mouth open.
    with dissolve

    pe "Thanks, [name]. This means the world to me. Really."

    scene v8spen9 # TPP. Show Penelope hugging MC. Both smiling. MC mouth open.
    with dissolve

    u "That's what friends are for."

    scene v8spen10 # TPP. Show MC leaving Penelope's dorm, Penelope still sat on edge of bed looking cheered up, looking at MC, MC neutral expression.
    with dissolve

    # SCENE 16 #

label no_help_pen:

    u "If you need me for anything, you know where to find me, okay? I have to get home and study, but text me any time."

    scene v8spen8b
    with dissolve
    pe "Thanks, [name], I will, and thank you for being here for me."

    scene v8spen8c
    with dissolve

    u "It's not a problem. You hang in there, okay?"

    scene v8spen8e # FPP. Same camera as v8spen8, Penelope nodding her head and smiling softly.
    with dissolve

    pause 0.5

    scene v8spen11 # TPP. Show MC leaving Penelope's dorm, MC neutral expression, Penelope still looks a bit sad but slightly smiling.
    with dissolve

    u "(Damn, I hope she'll be okay)"

    # SCENE 16 #
