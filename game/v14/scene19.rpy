# SCENE 19: Chloe shows you her campaign head quarter in the library
# Locations: Outside Library, Library, Chloe's HQ
# Characters: MC (Outfit: 9), CHLOE (Outfit: 2)
# Time: Morning

label v14s19:
    play music "music/v14/Track Scene 19.mp3" fadein 2

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
    
    if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
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

    python:
        chloe_board.add_approach("Wolves", "Announce the Wolves as official brotherhood of the chicks", opinion="\"The Wolves and The Chicks already have a special bond, but we can convince Chris to make the Wolves our official brotherhood frat. This means a lifetime of loyalty and support, which is  exactly what I need right now.\" - Chloe")
        chloe_board.add_approach("Apes", "\"Get the Apes on our side", opinion="Chris is basically like an open wound right now, and I don't want to rub salt on everything he's going through. If we use this vulnerable time to talk some sense into him, maybe we can get him to focus on himself, the Wolves, and most importantly, me as the President of the Chicks. Just make sure you don't say the wrong thing...\" - Chloe")

        chloe_board.add_task("Wolves", "Talk to Chris for his full support",
            opinion="\"Chris is basically like an open wound right now, and I don't want to rub salt on everything he's going through. If we use this vulnerable time to talk some sense into him, maybe we can get him to focus on what's truly important\" - Chloe",
            people=[mc, chloe, chris])
        v14s19_real_wolf = chloe_board.add_subtask("Wolves", "Photoshoot with a real wolf",
            opinion="\"We can Rent-A-Wolf for an hour in exchange for a pretty penny. Can you imagine what people will say when they see that the Chicks have partnered with the Wolves, and I'm posing with a real wolf?!\" - Chloe",
            people=[mc, chloe, wolf, trainer],
            cost=450)
        v14s19_plush_wolf = chloe_board.add_subtask("Wolves", "Photoshoot with plush toy wolf",
            opinion="\"I could easily grab a wolf plushie to pose with. It's a little less interesting than a real wolf, but definitely less expensive and of course, the safer option.\" - Chloe",
            people=[mc, chloe],
            cost=50)
        chloe_board.add_task("Wolves", "Post the photo on Kiwii",
            opinion="\"The last step is to post the photo with a good caption and hope for the best.\" - Chloe",
            people=[mc, chloe])

        chloe_board.add_task("Apes", "Host a small get together with Cameron, Grayson, Chloe, Aubrey and you",
            opinion= "\"First things first: Get them all in a room, give them each a beer, and put on some good music. As soon as we've set the mood, we can get down to business.\" - Chloe",
            people=[mc, chloe, aubrey, grayson, cameron])
        v14s19_talk_cameron = chloe_board.add_subtask("Apes", "Talk to Cameron about a strategic alliance",
            opinion="\"Cameron secretly has amazing leadership skills, and I know he plans to use them one day. If we tell Cameron exactly what he wants to hear in terms of the future of the Apes, he'll have no reason to vote against me\" - Chloe",
            people=[mc, chloe, cameron])
        v14s19_seduce_grayson = chloe_board.add_subtask("Apes", "Seduce Grayson",
            opinion="\"Don't get me wrong, I know this sounds a little... manipulative, but you have to admit, I can easily get Grayson on our side with a pinch of flirting. And trust me, it won't have to be much, especially with a few drinks in him.\" - Chloe",
            people=[mc, chloe, grayson])

    call screen planning_board(chloe_board)

label v14s19_continue:
    $ v14_chloe_wolves = chloe_board.approach.id == "Wolves"
    $ v14_realwolf = chloe_board.selected_task == v14s19_real_wolf
    $ v14_chloe_cameron = chloe_board.selected_task == v14s19_talk_cameron

    scene v14s19_99 # TPP. Show MC and Chloe standing infront of The Planning Board (a white board), both looking at the board, camera showing MC and Chloe, not the actual content of the board, MC and Chloe looking inquisitevely at the board, MC mouth open, Chloe mouth closed
    with dissolve

    u "From the options we have, these are the final decisions I'd go with."

    scene v14s19_99a # TPP. Same as v14s19_99, but Chloe mouth open, MC mouth closed
    with dissolve

    if (v14_help_chloe and not v14_chloe_wolves):
        cl "Getting the Apes to side with us could take a lot of convincing but..."
        cl "If we manage to pull it off, a Chicks and Apes alliance would make for an interesting future of the Chicks."

    else:
        cl "I know Chris trusts me, so I'm pretty sure we've already got the Wolves on our side. Guess we'll find out, though..."

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

    stop music fadeout 3
    jump v14s19a