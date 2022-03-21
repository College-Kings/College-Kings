# SCENE 64: Chicks Garden Bonfire
# Locations: Chicks backyard of Sorority House
# Characters: CHLOE (Outfit: 1), LINDSEY (Outfit: 3), MC (Outfit: 2), AUBREY (Outfit: 1), NORA (Outfit: 2), JENNY (Outfit: 1)
# Time: Evening


label v16s64:

    scene v16s64_1 # TPP. In the backyard, Chloe (slight smile, mouth open, looking at Jenny), and Jenny (slight smile, mouth closed, looking at Chloe) are sitting next to each other, Nora (slight smile, mouth open, looking at Aubrey) is sitting between Jenny and Aubrey, and Aubrey (slight smile, mouth closed, looking at Nora) is sitting next to Nora, everyone is sat around a small campfire with a neat stone circle around it, two open spots around the campfire are for MC (slight smile, mouth closed, looking at Lindsey) who will sit next to Chloe and Lindsey (slight smile, mouth open, looking at MC) who will sit next to Aubreywalking towards the campfire circle MC is holding the suggestion box from v16s63b
    with dissolve

    pause 0.75

    if v16s63kissing_convo: # -if Transitioning from Scene 63b-  !!!###PLACEHOLDER VARIABLE###!!!

        scene v16s64_2 # FPP. Show just Chloe already sitting (slight smile, mouth open, looking at Lindsey)
        with dissolve

        cl "How was the massage, Lindsey?"

        scene v16s64_3 # FPP. Show just Lindsey already sitting (slight smile, mouth open, looking at Chloe )
        with dissolve

        li "Amazing. A little rough at points but hey, I like it hard sometimes, haha."

    else: # -if Transitioning from Scene 63a or 63c-

        scene v16s64_2
        with dissolve

        cl "Oh, here they are."

        scene v16s64_3
        with dissolve

        li "Yeah, it took us a moment to find you, haha."

        scene v16s64_2a # FPP. Show just Chloe (slight smile, mouth closed, looking at MC)
        with dissolve

        u "Here, I picked this up on the way."

        scene v16s64_2b # FPP. Show just Chloe (slight smile, mouth open, looking at MC)
        with dissolve

        cl "Thanks. I wanted to look through it now actually."

    # -Regardless of what scene we're transitioning from-

    scene v16s64_2c # FPP. MC hands (Only MC hands are shown) Chloe (slight smile, mouth closed, looking at MC) the suggestion box and Chloe takes the suggestion box from MC
    with dissolve

    pause 0.75

    scene v16s64_2b
    with dissolve

    cl "Break out the marshmallows. I've got everything we need for making s'mores."

    scene v16s64_4 # FPP. Show just Aubrey already sitting (slight smile, mouth open, looking at Chloe)
    with dissolve

    au "Oh, my God. I love s'mores."

    scene v16s64_5 # TPP. Aubrey (slight smile, mouth closed, looking at MC) hands MC (slight smile, mouth is closed, looking at Aubrey) a little stick with a marshmallow on it, and Nora (slight smile, mouth is closed, looking at Jenny) hands Jenny (slight smile, mouth is closed, looking at Nora) a little stick with a marshmallow on it, Chloe (slight smile, mouth is closed, looking at the suggestion box) is opening the suggestion box and has a small piece of paper in her hand. Lindsey (slight smile, mouth is closed, looking at the campfire) already holding a little stick with a marshmallow on it.
    with dissolve

    menu:

        "Take one":
            $ add_point(KCT.BRO)

            scene v16s64_4a # FPP. Show just Aubrey (slight smile, mouth closed, looking at MC) holding out a little stick with a marshmallow on it to MC
            with dissolve

            u "Thanks! I love marshmallows."

            scene v16s64_4b # FPP. Show just Aubrey (slight smile, mouth open, looking at MC)
            with dissolve

            au "*Laughs* Me too!"

        "I'm not hungry":
            $ add_point(KCT.TROUBLEMAKER)

            scene v16s64_4a
            with dissolve

            u "No, thanks. I'm not in the mood."

            scene v16s64_4c # FPP. Show just Aubrey (inquisitive expression, mouth open, looking at MC) holding out a little stick with a marshmallow on it to MC
            with dissolve

            au "Not in the mood for marshmallows by the campfire? Are you insane?"

            scene v16s64_4d # FPP. Show just Aubrey (inquisitive expression, mouth open, looking at MC) the stick with the marshmallow on it is still in her hand, but she is no longer holding it out towards MC
            with dissolve

            u "No, just a little full, but thanks for your concern. *Chuckles*"

            scene v16s64_4e # FPP. Show just Aubrey (slight smile, mouth open, looking at MC) holds the stick with the marshmallow on it towards her mouth
            with dissolve

            au "I'll eat yours then."

            scene v16s64_4f # FPP. Aubrey (eating, mouth open, looking at MC) pulls the marshmallow off the stick and shoves the whole marshmallow in her mouth
            with dissolve

            pause 0.75

            scene v16s64_4g # FPP. Aubrey (slight smile, mouth is closed, looking at MC) has puffed out cheeks because the hwole marshmallow is in her mouth
            with dissolve

            u "*Laughs* Wow, how many do you think we can fit in there?"

            scene v16s64_4h # FPP. Aubrey (slight smile, mouth is open, looking at MC) has puffed out cheeks because the hwole marshmallow is in her mouth, the marshmallow can be slightly seen in her mouth
            with dissolve

            au "*Muffled* Wanna find out?"

            scene v16s64_6 # TPP. Show MC and Lindsey (both laughing looking at Aubrey), Aubrey (laughing, mouth open, looking at MC) still has puffed out cheeks, and the marshmallow can be slightly seen in her mouth
            with dissolve

    if v16s63breast_reduction and v16s63bbreath_mint: ###!!!PLACEHOLDER VARIABLE!!!### # -if MC chose insults in both 16.63 and 16.63b
        $ v16s64insulted_chloe = True ###!!!VARIABLE MUST BE ADDED FOR POSSIBLE CHLOE BREAK-UP!!!###

        scene v16s64_2d # FPP. Show just Chloe (angry expression, mouth open, looking at MC)
        with dissolve

        cl "I don't have bad breath or saggy tits, you fucking asshole!"

    elif v16s63breast_reduction and v16s63bcompliment or v16s63bbreath_mint and v16s63compliment: ###!!!PLACEHOLDER VARIABLES!!!### # -if MC chose Suggest a breast reduction in 16.63 and/or Suggest a breath mint in 16.63b (if MC chose one of these, but also picked a compliment, the positive note is not acknowledged because a bad one was written. This means that if MC chose at least one insult, any positive messages are ignored.)
        $ v16s64insulted_chloe = True ###!!!VARIABLE MUST BE ADDED FOR POSSIBLE CHLOE BREAK-UP!!!###

        scene v16s64_2d
        with dissolve

        cl "What the fuck is this?"

        cl "[name], is this funny to you?!"

        scene v16s64_2e # FPP. Show just Chloe (angry expression, mouth closed, looking at MC)
        with dissolve

        u "Huh?"

    elif v16s63bbreath_mint: ###!!!PLACEHOLDER VARIABLE!!!### # -if MC chose Suggest a breath mint in 16.63b
        $ v16s64insulted_chloe = True ###!!!VARIABLE MUST BE ADDED FOR POSSIBLE CHLOE BREAK-UP!!!###

        scene v16s64_2f # FPP. Show just Chloe (slightly angry expression, mouth open, looking at MC)
        with dissolve

        cl "You suggest I use a breath mint?"


    elif v16s63breast_reduction: ###!!!PLACEHOLDER VARIABLE!!!### # -if MC chose Suggest a breast reduction in 16.63
        $ v16s64insulted_chloe = True ###!!!VARIABLE MUST BE ADDED FOR POSSIBLE CHLOE BREAK-UP!!!###

        scene v16s64_2d
        with dissolve

        cl "A breast reduction? That's your fucking suggestion?"

    # -regardless

    if v16s64insulted_chloe: # -if insulted Chloe

        # -chloe is pissed and the others girls can't believe it, but Lindsey and Nora are laughing about it, nora trying to hide her smile

        scene v16s64_4i # FPP. Show just Aubrey (concerned expression, mouth is open, looking at MC)
        with dissolve

        au "Wait... What?"

        scene v16s64_7 # FPP. Show just Nora (slight smile, mouth slightly open, slightly laughing, looking at MC) trying to hide her laughter with her hand
        with dissolve

        no "*Snickers*"

        scene v16s64_2e
        with dissolve

        u "(Oh, fuck! How does she know it was me...?)"

        scene v16s64_8 # FPP. Show just Jenny (dissapointed expression, mouth is open, looking at MC)
        with dissolve

        jen "[name]? Did you seriously write that?"

        scene v16s64_2e
        with dissolve

        menu:

            "Tell the truth":
                $ v16s64confessed_insult = True # -try to keep this variable as it will possibly avoid a breakup i assume, thank you
                $ add_point(KCT.BRO)
                if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                    $ add_point(KCT.BOYFRIEND)

                scene v16s64_2e
                with dissolve

                u "Yeah, I... I'm sorry, Chloe."

                scene v16s64_2d
                with dissolve

                cl "*Scoffs* Sorry? Why the fuck did you write it then?"

                scene v16s64_2e
                with dissolve

                u "Honestly, I just thought it'd get a few laughs and lighten the mood, I guess? I really am sorry-"

            "Deny it":
                $ v16s64denied_insult = True # -try to keep this variable as it will impact a breakup i assume, thank you
                $ add_point(KCT.TROUBLEMAKER)
                if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                    $ add_point(KCT.TROUBLEMAKER)

                scene v16s64_2e
                with dissolve

                u "What? I didn't write anything like th-"

                scene v16s64_2g # FPP. Show just Chloe (extremely angry expression, mouth open, looking at MC)
                with dissolve

                cl "*Scoffs* Are you seriously trying to deny it?"

                scene v16s64_2h # FPP. Show just Chloe (extremely angry expression, mouth closed, looking at MC)
                with dissolve

                u "I didn't-"

                scene v16s64_2g
                with dissolve

                cl "I recognize your non-feminine handwriting, [name]."

                scene v16s64_2h
                with dissolve

                u "(Shit.)"

                u "Look, I'm sorry."

                scene v16s64_2g
                with dissolve

                cl "Ha! He's sorry."

                scene v16s64_2h
                with dissolve

                u "I just thought it would be funny, honestly, I didn't mean any harm."

        scene v16s64_2g
        with dissolve

        cl "Well, it's not funny! It's obviously not fucking funny at all."

        scene v16s64_2h
        with dissolve

        u "I'm sorry, seriously! It was just a little prank... I swear."

        scene v16s64_2i # FPP. Show just Chloe (no expression, mouth open, looking at MC)
        with dissolve

        cl "*Sighs* I don't know about you sometimes, [name]. You have a strange sense of humor."

        if chloe.relationship.value >= Relationship.GIRLFRIEND.value: # -if also ChloeGF

            scene v16s64_2j # FPP. Show just Chloe (slighty sad expression, mouth open, looking at MC)
            with dissolve

            cl "If you think I'd find anonymous insults funny, then maybe I should rethink things between us..."

            scene v16s64_2k # FPP. Show just Chloe (sad expression, mouth closed, looking at MC)
            with dissolve

            u "Chloe..."

        scene v16s64_2k
        with dissolve

        u "(Well, I fucked up.) I apologize, Chloe. It was a stupid idea, and you have every right to be upset with me, but I hope you can forgive me soon."

        scene v16s64_7a # FPP. Show just Nora (slight smile, mouth open, looking at Chloe) 
        with dissolve

        no "Ahem! Well, if you ask me..."

        scene v16s64_8a # FPP. Show just Jenny (slight smile, mouth open, looking at Nora) 
        with dissolve

        jen "Pretty sure no one did..."

        scene v16s64_9 # TPP. Jenny (sarcastic smile, mouth closed, looking at Nora intimidatingly) and Nora (classic Nora Bitch face, mouth closed, looking at Jenny intimidatingly) Try and make it look similar to a UFC/Boxing matchup Poster, but they are still sitting
        with dissolve

        pause 0.75

        scene v16s64_7b # FPP. Show just Nora (condescending expression, mouth open, looking at MC) 
        with dissolve

        no "That was pretty shitty of you, [name]. Hilarious, but wrong. You don't say that shit about a girl, it sticks with us a lot longer than you'd think."

        scene v16s64_7c # FPP. Show just Nora (condescending expression, mouth closed, looking at MC) 
        with dissolve

        u "*Sighs* I understand."

        scene v16s64_7d # FPP. Show just Nora (no expression, mouth open, looking at Chloe) 
        with dissolve

        no "With that being said... Come on, Chloe. You know he didn't mean to hurt you."

        scene v16s64_4j # FPP. Show just Aubrey (no expression, mouth open, looking at Chloe) 
        with dissolve

        au "Listen, babe. Everyone here knows that your body is impeccable."

        if # -if chloeGF (extra dialogue)

            scene v16s64_4k # FPP. Show just Aubrey (slightly angry, mouth open, looking at MC) 
            with dissolve

            au "[name] knows it damn well."

            scene v16s64_4l # FPP. Show just Aubrey (slightly angry, mouth closed, looking at MC) 
            with dissolve

            u "I do. *Chuckles*"

            if chloe.relationship.value >= Relationship.GIRLFRIEND.value and AubreyTamed: ###!!!Check for proper AubreyTamed Variable!!!###
            
                scene v16s64_4m # FPP. Show just Aubrey (sad smile, mouth closed, trying not to look at MC) 
                with dissolve

            else:

                scene v16s64_4n # FPP. Show just Aubrey (slight smile, mouth closed, looking at MC) 

        scene v16s64_8b # FPP. Show just Jenny (full smile, mouth closed, looking at Chloe)
        with dissolve

        jen "It is! We all wouldn't have made out with you for the past hour if you weren't a total smoke show."

        scene v16s64_2l # FPP. Show just Chloe (sad smile, mouth open, looking at Jenny), slightly tearing up
        with dissolve

        cl "*Laughs* Thanks. That does make me feel a little better about it."

        scene v16s64_2j
        with dissolve

        cl "*Sighs* [name]..."

        scene v16s64_2k
        with dissolve

        u "Yeah?"

        scene v16s64_2j
        with dissolve

        cl "Don't ever pull that shit on me again."

        scene v16s64_2m # FPP. Show just Chloe (sad smile, mouth closed, looking at MC), slightly tearing up
        with dissolve

        u "Message received. (Not making any promises though, hehee...)"

    if v16s63compliment or v16s63bcompliment and not v16s63breast_reduction and not v16s63bbreath_mint: # if MC chose to compliment chloe in 16.36 and/or 16.63b (both times or just once with NO insults)

        scene v16s64_2b
        with dissolve

        cl "Aw! [name]... Thanks. You're sweet for adding something cute."

        scene v16s64_2a
        with dissolve

        u "Wait! How'd you know it was me?!"

        scene v16s64_2b
        with dissolve

        cl "Umm, don't take this the wrong way, but... Your handwriting looks like chicken scratches. *Giggles*"

        scene v16s64_4o # FPP. Show just Aubrey (slight smile, mouth open, looking at Chloe)
        with dissolve

        au "Haha, hey! It could be mine."

        scene v16s64_2n # FPP. Show just Chloe (slight smile, mouth open, looking at Aubrey)
        with dissolve

        cl "No, no... [name]'s is much, much worse. *Laughs*"

        scene v16s64_2a
        with dissolve

        u "(Dammit...)"

    elif not v16s63compliment or v16s63bcompliment or v16s63breast_reduction or v16s63bbreath_mint  # -if MC chose to not write anything at all

        scene v16s64_2
        with dissolve

        cl "Aw, thanks for the suggestions, everyone. These are actually helpful! Well, some of them..."

        scene v16s64_2n
        with dissolve

        cl "*Laughs* Communal vibrators? Thanks for a laugh, Aubrey!"

        scene v16s64_4o
        with dissolve

        au "Wha- It's a serious suggestion!"

        scene v16s64_2n
        with dissolve

        cl "Hmm... I'll take it into consideration."

    # -end if-

    scene v16s64_2a
    with dissolve

    u "I'm thinking this a good time for me to go and let the real party begin, haha."

    scene v16s64_3a # FPP. Show just Lindsey (slight smile, mouth open, looking at, MC)
    with dissolve

    li "Finally! No boys, no boys, no boys!"

    if # -if lindseyrs she winks at him-

        scene v16s64_3b # FPP. Show just Lindsey (slight smile, mouth closed, winking at MC)
        with dissolve

    scene v16s64_2a
    with dissolve

    u "Damn... Are you guys sure you don't need a big, strong, handsome man to stay here with you all night?"

    scene v16s64_7e # FPP. Show just Nora (slight smile, mouth closed, rolling her eyes)
    with dissolve

    no "Oh, for the love of God..."

    scene v16s64_2b
    with dissolve

    cl "Yeah, we'll live. *Giggles* I promise."

    scene v16s64_8b
    with dissolve

    jen "Things are about to get WILD!"

    scene v16s64_4o
    with dissolve

    au "Yessssss!"

    scene v16s64_4n
    with dissolve

    u "(I wanna get wild...)"

    scene v16s64_3
    with dissolve

    li "Oh, Polly is performing on campus, actually. So, I need to go for a tiny bit, but I'll be back for movies."

    scene v16s64_2a
    with dissolve

    u "That's where I'm headed, too."

    scene v16s64_3
    with dissolve

    li "Thanks for the spa night, Chloe. I genuinely had fun, surprisingly. *Chuckles*"

    scene v16s64_2
    with dissolve

    cl "Ha, no problem. Don't be late, we're starting with or without you!"

    scene v16s64_3
    with dissolve

    li "I know, I know! I'm just too much of a Polly fan to miss this."

    scene v16s64_2a
    with dissolve

    u "Have a great night, ladies! You know how to get ahold of me in case of an emergency."

    scene v16s64_8c # FPP. Show just Jenny (slight smile, mouth open, looking at MC)
    with dissolve

    jen "Leave already so we can talk about you!"

    scene v16s64_1a # TPP. same as v16s64_1 Everyone is now sitting, Mc (slight smile, mouth is open, looking at the girls) is putting his hands up like "I give up," Chloe, Jenny, Nora, Aubrey, and Lindsey (all laughing, all mouths open, all looking at MC)
    with dissolve

    u "Fine."

    scene v16s64_1b # TPP. same as v16s64_1a MC (pretends to be angry and offended, mouth closed, walking away from the girls), Lindsey (slight smile, mouth is open, looking at MC) waves at MC and stands up from her seat, Chloe, Jenny, Nora, and Aubrey still sitting (all slight smiles, all mouths closed, all looking at MC)
    with dissolve

    li "Wait one sec, [name]. Let me change first, wait here!"

    scene v16s64_10 # TPP. Show just MC (slight smile, mouth is closed, looking wherever) standing in the front yard on the Chicks sorority house
    with dissolve

    pause 0.75

    scene v16s64_10a # TPP. Show just MC (slight smile, mouth is closed, looking at Lindsey) and Lindsey (slight smile, mouth is closed, looking at MC) exiting the Chicks sorority front door.
    with dissolve

    pause 0.75

    jump v16s66 # -Transition to Scene 66-