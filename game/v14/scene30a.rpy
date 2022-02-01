# SCENE 30a: Photoshoot with Chloe REAL WOLF
# Locations: The woods same as photoshoot with plush wolf
# Characters: CHLOE (Outfit: 1), MC (Outfit: 2), WOLF TRAINER (Outfit: 1)
# Time: Afternoon

label v14s30a:
# -Mc arrives at the woods and sees Chloe petting the wolf while trainer stands next to it with a leash
    scene v14s30a_1 # TPP. Show MC walking in the woods towards the photoshoot location, Slight smile, mouth closed. (Can reuse the one from v14s30)
    with dissolve

    pause 0.5

    play music "music/v13/Track Scene 59_1.mp3" fadein 2

    scene v14s30a_2 # TPP. MC finds Chloe in the woods with the Wolf Trainer at the photoshoot set, Chloe petting the wolf, All slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v14s30a_3 # FPP. MC looking at Chloe petting the wolf and the Wolf trainer pointing over at MC, Chloe and Wolf Trainer slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v14s30a_3a # FPP. Same as v14s30a_3, Chloe turns to see MC, Wolf Trainer no longer pointing, Wolf Trainer, slight smile, mouth closed, Chloe slight smile, mouth open.
    with dissolve

    cl "[name], there you are!"

    scene v14s30a_4 # FPP. MC walking over to Chloe and the wolf trainer, Chloe and Wolf trainer, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v14s30a_5 # FPP. MC standing with Chloe and the Wolf Trainer, MC looking at Chloe, Chloe and Wolf Trainer looking at MC, Both slight smile, mouth closed.
    with dissolve

    u "Hey, I see this is a real fucking wolf..."

    scene v14s30a_5a # FPP. Same as v14s30a_5, Wolf trainer looking at Chloe, Chloe slight smile, mouth open, Wolf Trainer slight smile, mouth closed.
    with dissolve

    cl "Yes! He's so cute!"

    scene v14s30a_5
    with dissolve

    u "Haha, don't think cute is the word I'd use to describe him."

    scene v14s30a_6 # FPP. MC looking at the Wolf Trainer, Chloe looking at Wolf trainer, Wolf trainer slight smile, mouth open.
    with dissolve

    wtrain "Aye mate, he's a lover. Trust me."

    scene v14s30a_6a # FPP. Same as v14s30a_6, Wolf Trainer slight smile, mouth closed.
    with dissolve

    u "Trust you, huh? I don't even know your name."

    scene v14s30a_6
    with dissolve

    wtrain "Well, that's unimportant. Just know, your life lies safely in my hands."

    scene v14s30a_6a
    with dissolve

    u "Ah, nice..."

    scene v14s30a_5a
    with dissolve

    cl "*Laughs*"

    scene v14s30a_6a
    with dissolve

    u "So, Australian?"

    scene v14s30a_6
    with dissolve

    wtrain "Right on, mate..."

    scene v14s30a_5a
    with dissolve

    cl "He used to date one of my close friends, until the accident..."

    scene v14s30a_5
    with dissolve

    u "The accident?!"

    scene v14s30a_6b # FPP. Same as v14s30a_6a, MC looking at Wolf Trainer, Wolf Trainer looking at Chloe, Chloe slight smile, mouth closed, Wolf trainer slight smile, mouth open.
    with dissolve

    wtrain "Oh, pfft..."

    wtrain "Come on, Chloe... It was just a scratch."

    scene v14s30a_5b # FPP. Same as v14s30a_5a, Chloe looking at Wolf Trainer, MC looking at Chloe, Wolf Trainer looking at Chloe, Chloe slight smile, mouth open, Wolf Trainer, slight smile, mouth closed.
    with dissolve

    cl "Right... That's what you kept telling Jenny, right?"

    scene v14s30a_5c # FPP. Same as v14s30a_5b, Chloe looking at Wolf Trainer, MC looking at Chloe, Wolf Trainer looking at Chloe, Both slight smile, mouth closed.
    with dissolve

    u "(Jenny?)"

    scene v14s30a_6a
    with dissolve

    u "Should I be worried or not?"

    scene v14s30a_6
    with dissolve

    wtrain "No mate, this is a completely different wolf..."

    scene v14s30a_6a
    with dissolve

    u "Ha..."

    scene v14s30a_5a
    with dissolve

    cl "Right, so..."

    scene v14s30a_6
    with dissolve

    wtrain "So... Bet you're wondering what an Australian is doing with a wolf, huh?"

    scene v14s30a_6a
    with dissolve

    u "I wasn't really-"

    scene v14s30a_5a
    with dissolve

    cl "Okay, let's get this party started shall we?"

    scene v14s30a_5
    with dissolve

    u "Am I taking the pictures?"

    scene v14s30a_6
    with dissolve

    wtrain "Would you rather hold onto the wolf?"

    scene v14s30a_6a
    with dissolve

    u "Ready when you are!"

    scene v14s30a_5a
    with dissolve

    cl "Make us look good."

    if chloe.relationship >= Relationship.GIRLFRIEND:
        scene v14s30a_5
        with dissolve

        u "It'd be impossible to make you look bad."

        scene v14s30a_7 # TPP. Chloe kissing MC on the cheek.
        with dissolve
        
        pause 0.75

    scene v14s30a_8 # TPP. Camera positioned infront of Photoshoot Camera to just show Chloe, the wolf, and the wolf trainer, Both slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v14s30a_9 # FPP. MC behind the Camera the equipment visible, The wolf running towards MC, Chloe and Wolf Trainer slight smile, mouths closed.
    with dissolve

    u "Woah, woah, woa- Oh... Umm, excuse me?"

    scene v14s30a_9a # FPP. Same as v14s30a_9, The wolf walking up to MC, Wolf trainer slight smile, mouth open, Chloe slight smile, mouth closed.
    with dissolve

    wtrain "Oh, uh, don't worry! Just stay calm, and so will he. *Nervous chuckling*"

    scene v14s30a_9b # FPP. Same as v14s30a_9a, The wolf sniffing MC, Chloe slight smile, mouth open, Wolf trainer slight smile, mouth closed.
    with dissolve

    cl "[name]?!"

    scene v14s30a_10 # TPP. Show the Wolf tugging at MC's pants, the wolfs tail wagging to the left.
    with vpunch

    u "(This is it... This is how I die...)"

    scene v14s30a_10a # TPP. Same as v14s30a_10, Wolf tugging a little harder on MC's pants, wolfs tail now wagging to the right.
    with dissolve

    menu:
        "Run":
            $ add_point(KCT.BOYFRIEND)
            scene v14s30a_11 # TPP. MC walking backwards getting prepared to run, MC worried face, mouth open.
            with dissolve

            u "AH! Oh! Stop it! No, ugh!"

            scene v14s30a_12 # TPP. Mc falls backwards onto his butt, worried face, mouth closed.
            with dissolve

            pause 0.75

            scene v14s30a_12a # TPP. Same as v14s30a_12, The wolf walks up to MC and sniffs his crotch, MC worried face, mouth closed.
            with dissolve

            pause 0.75

            scene v14s30a_12b # TPP. Same as v14s30a_12a, The wolf licks MC's face, MC worried face, mouth closed.
            with dissolve

            pause 0.75

            scene v14s30a_13 # TPP. Close up of Chloe and the Wolf Trainer standing next to each other, Chloe slight smile, mouth closed, Wolf trainer slight smile, mouth open.
            with dissolve

            wtrain "Fuck me dead, mate!"

            scene v14s30a_13a # TPP. Same as v14s30a_13, Chloe looking at the Wolf trainer, Chloe slight smile, mouth open, Wolf trainer slight smile, mouth closed.
            with dissolve

            cl "Huh?"

            scene v14s30a_13
            with dissolve

            wtrain "Australian thing... You must have some good meat."

            scene v14s30a_13b # TPP. Same as v14s30a_13, Chloe and Wolf Trainer looking towards MC, Wolf Trainer and Chloe slight smile, mouth closed.
            with dissolve

            u "Can you get him? *Grunts* Please?"

            scene v14s30a_13
            with dissolve

            wtrain "Back! Back, Niko!"

            scene v14s30a_13c # TPP. Same as v14s30a_13b, The Wolf goes back to sitting next to Chloe, Both slight smile, mouth closed.
            with dissolve

        "Stay still":
            $ add_point(KCT.BRO)
            scene v14s30a_10
            with dissolve

            u "(Fuck, fuck, fuck!)"

            scene v14s30a_13
            with dissolve

            wtrain "Blimey!"

            scene v14s30a_13b
            with dissolve

            u "What should I do?!"

            scene v14s30a_13
            with dissolve

            wtrain "Exactly what you're doing now, mate. Seems as though he just likes your meat!"

            scene v14s30a_13d # TPP. Same as v14s30a_13, Chloe slight smile, mouth open, Wolf Trainer slight smile, mouth closed.
            with dissolve

            cl "*Laughs*"

            scene v14s30a_10a
            with dissolve

            u "Funny guys, really. Can we make this stop now?"

            scene v14s30a_13
            with dissolve

            wtrain "Niko, heel."

            scene v14s30a_13c
            with dissolve

    pause 0.75

    scene v14s30a_8
    with dissolve

    u "He's good now, right?"

    scene v14s30a_8a # TPP. Same as v14s30a_8, Chloe slight smile, mouth open, Wolf trainer slight smile, mouth closed.
    with dissolve

    cl "Just c'mon already, meat man. *Chuckles*"

    scene v14s30a_8
    with dissolve

    u "Fuck's sake... Never living that one down."

    menu:
        "Take Picture":
            scene v14s30a_8b # TPP. Same as v14s30a_8a, Chloe posing with one hand on her hip and one hand on the wolf's head, Chloe smiling proudly, Mouth closed.
            with flash

    menu:
        "Take Picture":
            scene v14s30a_8c # TPP. Same as v14s30a_8b, Chloe giving the wolf a high five, Chloe slight smile, mouth closed.
            with flash

    menu:
        "Take Picture":
            scene v14s30a_8d # TPP. Same as v14s30a_8c, Chloe with her hands in the shape of Wolf's claws acting scary for the camera, The wolf growling towards the camera, Chloe Intimidating face, mouth closed.
            with flash

    menu:
        "Take Picture":
            scene v14s30a_8
            with flash

    u "Alright."

    scene v14s30a_8a
    with dissolve

    cl "Yay! Let's see..."

    scene v14s30a_9c # FPP. Same as v14s30_9b, Chloe running towards MC, The wolf and the wolf trainer in the background, Chloe slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v14s30a_14 # FPP(Keep wolf and wolf trainer out of shot to make it easier). Chloe looking at the camera, slight smile, mouth open.
    with dissolve

    cl "These are great! Come look."

    scene v14s30a_14a # FPP. Same as v14s30a_14, Chloe looking at MC, Slight smile, mouth closed.
    with dissolve

    u "I've already seen them all, Chloe. *Laughs* Pick your favorites and maybe I can help you choose."

    scene v14s30a_14b # FPP. Same as v14s30a_14a, Chloe looking at MC, slight smile, mouth open. 
    with dissolve

    cl "Yeah okay, haha. Thank you again."

    scene v14s30a_14a 
    with dissolve

    u "Of course."

    scene v14s30a_15 # TPP. Close up of the wolf trainer and the wolf, Wolf trainer slight smile, mouth open.
    with dissolve

    wtrain "Will there be any other pictures taken?"

    scene v14s30a_15a # TPP. Same as v14s30a_15, Wolf trainer slight smile, mouth closed.
    with dissolve

    cl "Nope, we're all finished."

    scene v14s30a_15
    with dissolve

    wtrain "Good deal mate, I'll be packing up then."

    scene v14s30a_15a
    with dissolve

    u "Thanks for coming out here, bye Niko!"

    scene v14s30a_16 # TPP. Close up of just the Wolf winking at MC.
    with dissolve

    u "(What the fuck?!)"

    scene v14s30a_14b
    with dissolve

    cl "C'mon [name], let's head back and pick out the winner."

    scene v14s30a_17 # TPP. Show MC and Chloe walking together out of the woods, both slight smile, mouth closed. (Can reuse v14s30_8)
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v14s30b