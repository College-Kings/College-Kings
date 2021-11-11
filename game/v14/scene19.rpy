# SCENE 19: Chloe shows you her campaign head quarter in the library
# Locations: Outside Library, Library, Chloe's HQ
# Characters: MC (Outfit: 9), CHLOE (Outfit: 2)
# Time: Morning

label v14s19:
    scene v14s19_1 # TPP. Show MC walking toward library, MC looking around for sign of Chloe, MC mouth closed.
    with dissolve

    pause 0.75

    scene v14s19_2 # TPP. Show MC in different location than v14s19_1, still looking for Chloe, MC mouth closed.
    with dissolve

    u "(Where the hell is she...?)"

    scene v14s19_3 # FPP. MC looking at a door that is cracked open.
    with dissolve

    u "(Gotta be in here.)"

    scene v14s19_3a # FPP. Same angle as v14s19_3, MC has opened the door, Chloe can be seen inside the room looking at a mirror, Chloe mouth closed
    with dissolve

    pause 0.75

    scene v14s19_4 # FPP. MC now inside room with Chloe, MC looking at Chloe, Chloe looking at mirror, Chloe mouth open
    with dissolve

    cl "Took you long enough! Ready to get started?"

    scene v14s19_4a # FPP. Same as v14s19_4, Chloe mouth closed
    with dissolve

    u "Damn, someone's eager..."
    
    if chloegf:
        scene v14s19_5 # TPP. Show MC leaning in to kiss Chloe, all mouths closed.
        with dissolve

        pause 0.75

        scene v14s19_5a # TPP. Same as v14s19_5, Show MC kissing Chloe's cheek, Chloe serious face, Chloe paying no attention to MC
        with dissolve

        pause 0.75

    scene v14s19_4a
    with dissolve

    u "Ha... No hi? No, how was class? Blah? Blah? Blah? Nothing?"

    scene v14s19_4
    with dissolve

    cl "I'm sorry [name], I'm just really focused and I'm anxious to get started considering the Lindsey parade that's been taking place all day."

    scene v14s19_4a
    with dissolve

    u "I can understand that... I guess I'll let you off the hook for being in such a haste."

    scene v14s19_4b # FPP. Same as v14s19_4, Chloe looking at MC, Chloe happy, Chloe mouth open
    with dissolve

    cl "Haha, thanks. Should we get started then?"

    scene v14s19_4c # FPP. Same as v14s19_4b, Chloe mouth closed.
    with dissolve

    u "Sure, let's get to it."

    scene v14s19_4b
    with dissolve

    cl "Okay, so here's my plan..."

    scene v14s19_4d # FPP. Same as v14s19_4, Chloe looking at MC, Chloe serious, Chloe mouth open
    with dissolve

    cl "The first phase of my campaign is to re-establish old loyalties. The first time I was elected, people loved me and I need to remind them why."

    cl "So, here's what I'm thinking for phase one."
label test:
    python:
        chloe_board.add_approach("Wolves", opinion="")
        chloe_board.add_approach("Apes", opinion="")

        chloe_board.add_task(0, "Talk to Chris about getting his full support in return for this.",
            opinion="Chris is basically like an open wound right now, and I don't want to rub salt on everything he's going through. If we use this vulnerable time to talk some sense into him, maybe we can get him to focus on himself, the Wolves, and most importantly, me as the President of the Chicks. Just make sure you don't say the wrong thing...",
            people=[mc, chloe, chris])
        chloe_board.add_subtask(0, "Announce it via Kiwii (photoshoot with a real wolf)",
            opinion="We can Rent-A-Wolf for an hour in exchange for a pretty penny. Can you imagine what people will say when they see that the Chicks have partnered with the Wolves, and I'm posing with a real wolf?!",
            people=[mc, chloe, wolf, trainer],
            cost=450)
        chloe_board.add_subtask(0, "Announce it via Kiwii (photoshoot with plush toy wolf)",
            opinion="I could easily grab a wolf plushy to pose with. It's a little less interesting than a real wolf, but definitely less expensive and of course, the safer option.",
            people=[mc, chloe],
            cost=50)

        chloe_board.add_task(1, "Host a small get together with Cameron, Grayson, Chloe, Aubrey and MC",
            opinion= "First thing's first: Get them all in a room, give them each a beer, and put on some good music. As soon as we've set the mood, we can get down to business.",
            people=[mc, chloe, aubrey, grayson, cameron])
        chloe_board.add_subtask(1, "Talk to Cameron about a strategic alliance",
            opinion="Cameron secretly has amazing leadership skills, and I know he plans to use them one day. If we tell Cameron exactly what he wants to hear in terms of the future of the Apes, he'll no reason to vote against me",
            people=[mc, chloe, cameron])
        chloe_board.add_subtask(1, "Seduce Grayson",
            opinion="Don't get me wrong, I know this sounds a little... manipulative, but you have to admit, I can easily get Grayson on our side with a pinch of flirting. And trust me, it won't have to be much, especially with a few drinks in him.",
            people=[mc, chloe, grayson])

    call screen planning_board(chloe_board)

label v14s19_continue:
    if chloe_board.approach.name == "Apes":
        $ v14_chloe_apes = True
        
        #if subtask B:
            #$ v14_chloe_grayson = True
    else:
        #if subtask A:
            #$ v14_realwolf = True            
        pass

    scene v14s19_99 # TPP. Show MC and Chloe standing infront of The Planning Board (a white board), both looking at the board, camera showing MC and Chloe, not the actual content of the board, MC and Chloe looking inquisitevely at the board, MC mouth open, Chloe mouth closed
    with dissolve

    u "From the options we have, these are the final decisions I'd go with."

    if v14_chloe_apes: # PLACEHOLDER
        cl "Getting the Apes to side with us could take a lot of convincing but..."
        cl "If we manage to pull it off, a Chicks and Apes alliance would make for an interesting future of the Chicks."

    else:
        cl "I know Chris trusts me, so I'm pretty sure we've already got the Wolves on our side. Guess we'll find out, though..."

    scene v14s19_99a # TPP. Same as v14s19_99, but Chloe mouth open, MC mouth closed
    with dissolve

    cl "Hmm, okay..."

    scene v14s19_6 # FPP. MC and Chloe looking at eachother, Chloe serious, Chloe mouth open.
    with dissolve

    cl "These are your choices, remember that. So, be sure you're there to help me when the time comes, okay?"

    scene v14s19_6a # FPP. Same as v14s19_6, Chloe mouth closed
    with dissolve

    u "Yes, Madame President..."

    scene v14s19_6b # FPP. Same as v14s19_6, Chloe looking at you judgementally, Chloe smiling, Chloe mouth open
    with dissolve

    cl "Ewww, that sounds so weird coming from you. *Chuckles*"

    scene v14s19_6c # FPP. Same as v14s19_6b, Chloe mouth closed
    with dissolve

    u "Hey, you asked for this."

    scene v14s19_6b
    with dissolve

    cl "Okay, okay, fine."

    scene v14s19_7 # FPP. MC looking at Chloe, Chloe halfway out the door, Chloe looking back at MC smiling, Chloe mouth closed.
    with dissolve

    pause 0.75

    scene v14s19_8 # TPP. Show MC and Chloe outside the room, walking together, both happy, both mouths closed.
    with dissolve

    pause 0.75

    jump v14s19a