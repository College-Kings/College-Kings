# SCENE 8: Chloe phase 2 convo
# Locations: Chloe's planning board room
# Characters: CHLOE (Outfit: 2), MC (Outfit: 5)
# Time: Morning

label v15s8:
    scene v15s8_1 # TPP. Show MC walking into the planning board room with Chloe, both slight smile, mouth closed.
    with fade

    pause 0.75

    scene v15s8_2 # TPP. Show MC and Chloe looking at each other standing infront of the planning board, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s8_3 # FPP. MC and Chloe standing infront of the planning board, MC looking at Chloe, Chloe looking at MC, Chloe slight smile, mouth open.
    with dissolve

    cl "So, for phase two, we're stepping things up."

    scene v15s8_3a # FPP. Same as v15s8_3, Chloe slight smile, mouth closed.
    with dissolve

    u "Sounds good. I'm up for anything... Besides murder."

    scene v15s8_3
    with dissolve

    cl "Haha! Okay, no murder... Got it."

    cl "Except for political murder. *Laughs* We're winning no matter what it takes."

    scene v15s8_3a
    with dissolve

    u "Yes, ma'am."

    if chloegf:
        scene v15s8_3b # FPP. Same as v15s8_3a, Chloe flirting expression, mouth open.
        with dissolve

        cl "Eww, no... I like it when you're in charge... *Chuckles*"

        scene v15s8_3c # FPP. Same as v15s8_3b, Chloe flirting expression, mouth closed.
        with dissolve

        u "*Laughs*"

        scene v15s8_3b
        with dissolve

        cl "Sir..."

        scene v15s8_3c
        with dissolve

        u "(Oh...) Ahem, right then. Show me."

    scene v15s8_3
    with dissolve

    cl "Our options are very different, but either one can be the perfect plan as long as we do it right."

    cl "It all depends on how we want to go about this..."

    scene v15s8_4 # TPP. Show MC upclose analyzing the planning board, MC in a generic standing thinking pose while he looks at the board, Chloe in the background, both slight smile, mouth closed.
    with dissolve

# -Insert Planning Board with the options for phase 2-
# -The planning board pops up and MC makes his choices from what's presented, close when finished-

    scene v15s8_4a # TPP. Same as v15s8_4, MC slight smile, mouth open, Chloe slight smile, mouth closed.
    with dissolve 

    u "I think that's the best way to go."

    if v15s8_chloe_pb_DamageLindseyRep:
        scene v15s8_3a
        with dissolve

        u "If you're willing to play dirty and put our feelings aside, this plan can turn tons of people against her and towards you."

        scene v15s8_3
        with dissolve

        cl "As long as you're in the right place at the right time, this is a solid idea."

        cl "And if by any chance there's alcohol present, every girl's inner bitch comes out to play when they're drunk."

        scene v15s8_3a
        with dissolve

        u "Haha, is that true?"

        scene v15s8_3
        with dissolve

        cl "For some it slips out quicker than other, but yeah. Eventually."

        scene v15s8_3a
        with dissolve

        u "That's what she said."

        scene v15s8_3d # FPP. Same as v15s8_3c, Chloe struggling to not laugh and hold a unamused face, mouth open.
        with dissolve

        cl "*Sighs*"

        scene v15s8_3
        with dissolve

    if v15_LessChickTuition:
        scene v15s8_3a
        with dissolve

        u "If you can lower tuition fees, people are really going to love you. They're going to think you have tons of power, you know?"

        scene v15s8_3
        with dissolve

        cl "Exactly, but this could also backfire. We need to do some serious planning before meeting with one of them."

        scene v15s8_3a
        with dissolve

        u "If we're going to succeed at this, we might need to do some research."

        scene v15s8_3
        with dissolve

        cl "Yeah, I'm all over it."

    cl "Okay. Yeah. I'm happy with this!"

    scene v15s8_3a
    with dissolve

    u "Good, me too."

    scene v15s8_3
    with dissolve

    cl "Then that's it for today I suppose thanks for helping me again."

    scene v15s8_3a
    with dissolve

    u "Happy to be of service. Want me to walk you out?"

    scene v15s8_3
    with dissolve

    cl "No, I uh- I need to make a few phone calls."

    if v14s51_take_diary or v14s51_take_money:
        cl "And I still have to report the robbery to the dean, so..."

        scene v15s8_3a
        with dissolve

        u "(Fuck! The dean? This is going a bit far...)"

        u "Okay, I'll leave you to it. I'm here for you if you need anything."

        scene v15s8_3
        with dissolve

        cl "I know. *Chuckles* You're the best."

    else:
        scene v15s8_3a
        with dissolve

        u "Presidential phone calls?"

        scene v15s8_3
        with dissolve

        cl "Of course, haha. I'm a VIP, [name]... A Very Important President, making very important phone calls."

        scene v15s8_3a
        with dissolve

        u "Right... Okay, whatever gets your juices flowing."

        if chloegf or chloers:
            scene v15s8_3b
            with dissolve

            cl "Usually, you get them flowing..."

            scene v15s8_3c
            with dissolve

            u "What was that?"

            scene v15s8_3b
            with dissolve

            cl "Nothing! *Chuckles* Bye now."

    scene v15s8_5 # TPP. Show MC winking at Chloe as she is holding her phone.
    with dissolve

    u "Bye, Chlo."

    if chloegf:
        scene v15s8_6 # FPP. Show Chloe getting close up and personal with MC, Chloe biting her lip, Flirting expression, mouth closed
        with dissolve

        pause 0.75

        play sound "sounds/kiss.mp3"

        scene v15s8_6a # FPP. Same as v15s8_6, Chloe kissing MC.
        with dissolve

        pause 0.75

    scene v15s8_7 # TPP. Show MC walking to leave the planning room, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s8_7a # TPP. Same as v15s8_7, MC starting to turn around.
    with dissolve

    pause 0.75

    if v14s51_take_diary or v14s51_take_money:
        scene v15s8_8 # FPP. MC some distance away from Chloe looking at her. Chloe stressed on the phone, mouth closed.
        with dissolve

    else:
        scene v15s8_8a # FPP. Same as v15s8_8, Chloe on the phone winking at MC, slight smile, mouth closed.
        with dissolve

    scene v15s8_7b # TPP. Same as v15s8_7, MC opening the door to the planning room to walk out.
    with dissolve

    pause 0.75

    scene v15s8_9 # TPP. Show MC leaving the library and entering into the hallway, MC slight smile, mouth closed.
    with fade

    jump v15s9