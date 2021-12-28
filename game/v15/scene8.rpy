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

    if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
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

    pause 0.75

# -Insert Planning Board with the options for phase 2-
# -The planning board pops up and MC makes his choices from what's presented, close when finished-
    python:
        chloe_board = PlanningBoard("images/v15/planning_boards/chloe_background.webp", money=chloe_board.money)

        chloe_board.add_approach("Sabotage",
            "Damage Lindsey's reputation",
            opinion="\"This idea isn't for the faint of heart, but I've got to play the game if I want to win it... We sabotage her campaign with a not-so-tiny bit of embarrassment.\"")
        
        chloe_board.add_approach("Tuition",
            "Less tuition for all Chicks",
            opinion="\"The one thing I have always dreamed of being able to do as the President of the Chicks is to get all members free tuition. If we make a good enough case, I might be able to convince the Dean into making this happen.\"")

        chloe_board.add_task("Sabotage",
            "Secretly record Lindsey",
            opinion="\"After we get a few bottles of booze, you and Imre will do your best to get Lindsey wasted. I'm not sure what type of mood she'll be in, but maybe you should tell her she needs to relax for a bit. After all, she's probably stressed that she has nothing and I have everything...\"")

        chloe_board.add_task("Sabotage",
            "Provoke Lindsey to say something that might damage her reputation",
            opinion="\"OPINION\"")

        v15s8_chloe_kiwii = chloe_board.add_subtask("Sabotage",
            "Chloe posts the recording on Kiwii",
            opinion="\"OPINION\"")

        chloe_board.add_subtask("Sabotage",
            "Share the recording through the Dean's announcement system",
            opinion="\"OPINION\"")

        v15s8_chloe_lee = chloe_board.add_subtask("Tuition",
            "Try and convince Mr. Lee to support you in front of the Dean on this",
            opinion="\"Before we throw this crazy idea out in front of the Dean, we need support from some of the lecturers. I think Mr. Lee is our best bet, he's smart and very well respected. Although he can be hard to read.\"")

        chloe_board.add_subtask("Tuition",
            "Try and convince Ms. Rose to support you in front of the Dean on this",
            opinion="\"Before we throw this crazy idea out in front of the Dean, we need support from some of the lecturers. Ms. Rose could be worth a try. She's very empathetic, I just don't know how much she likes me...\"")
            
        chloe_board.add_task("Tuition",
            "Talk to the Dean with Mr. Lee or Ms. Rose's support",
            opinion="\"Finally, we have a meeting with the Dean. If we can show that a lecturer supports our idea, we should be able to get her approval. \"")

    call screen planning_board(chloe_board)

    if chloe_board.approach is not None:
        $ v15_chloe_lindseysabotage = chloe_board.approach.id == "Sabotage"

    if chloe_board.selected_task is not None:
        $ v15_chloe_postkiwii = chloe_board.selected_task == v15s8_chloe_kiwii
        $ v15_chloe_mrleesupport = chloe_board.selected_task == v15s8_chloe_lee

    # End planning board (screen disappears)

    scene v15s8_4a # TPP. Same as v15s8_4, MC slight smile, mouth open, Chloe slight smile, mouth closed.
    with dissolve

    u "I think that's the best way to go."

    if v15_chloe_lindseysabotage:
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

        cl "For some it slips out quicker than others, but yeah. Eventually."

        scene v15s8_3a
        with dissolve

        u "That's what she said."

        scene v15s8_3d # FPP. Same as v15s8_3c, Chloe struggling to not laugh and hold a unamused face, mouth open.
        with dissolve

        cl "*Sighs*"

        scene v15s8_3
        with dissolve

        pause 0.75

    elif v14_help_chloe:
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

    cl "Then that's it for today I suppose. Thanks for helping me again."

    scene v15s8_3a
    with dissolve

    u "Happy to be of service. Want me to walk you out?"

    scene v15s8_3
    with dissolve

    cl "No, I uh- I need to make a few phone calls."

    if "diary" in freeroam12stolen or "cash_large" in freeroam12stolen or "cash_small" in freeroam12stolen:
        cl "And I still have to report the robbery to the Dean, so..."

        scene v15s8_3a
        with dissolve

        u "(Fuck! The Dean? This is going a bit far...)"

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

        if chloe.relationship.value >= Relationship.FWB.value:
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

    u "Bye, Chloe."

    if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
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

    if "diary" in freeroam12stolen or "cash_large" in freeroam12stolen or "cash_small" in freeroam12stolen:
        scene v15s8_8 # FPP. MC some distance away from Chloe looking at her. Chloe stressed on the phone, mouth closed.
        with dissolve

        pause 0.75

    else:
        scene v15s8_8a # FPP. Same as v15s8_8, Chloe on the phone winking at MC, slight smile, mouth closed.
        with dissolve

        pause 0.75

    scene v15s8_7b # TPP. Same as v15s8_7, MC opening the door to the planning room to walk out.
    with dissolve

    pause 0.75

    scene v15s8_9 # TPP. Show MC leaving the library and entering into the hallway, MC slight smile, mouth closed.
    with fade
    
    pause 0.75

    jump v15s9