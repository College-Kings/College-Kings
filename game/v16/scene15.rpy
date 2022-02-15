# SCENE 15: Ideally single Scene Pier Free Roam with Penelope, Imre & Karen
# Locations: Carnival Park
# Characters: MC (Outfit: 5), PENELOPE (Outfit: 2), IMRE (Outfit: 1), KAREN (Outfit: 1), CARNIVAL WORKER (Outfit: 1), DYLAN (Outfit: 1), WHEEL ATTENDANT (Outfit: 1), HOTDOG VENDOR (Outfit: 1)
# Time: Evening
# Render Count: 63 Unique 169 Total

label v16s15:

    scene v16s15_1 # TPP. MC arrives at the pier entrance, now back in regular clothes. Penelope is already waiting for him, both of them slight smiles, mouths are closed, both looking at each other, MC is walking up to Penelope
    with dissolve

    if penelope.relationship.value >= Relationship.GIRLFRIEND.value: # -if PenelopeRS

        scene v16s15_2 # FPP MC gives Penelope a quick kiss
        with dissolve

        pause 0.75

        scene v16s15_3 # FPP. Penelope is looking at MC slight smile, mouth is closed
        with dissolve

        u "Well, hello there, young lady. Do you need some company?"

        scene v16s15_3a # FPP. Penelope is looking at MC slight smile, mouth is open
        with dissolve

        pe "Haha, why thank you, handsome stranger. Someone's finally here to rescue me!"

    elif penelope.relationship.value >= Relationship.FRIEND.value: # -if PenelopeFriend

        scene v16s15_3a
        with dissolve

        pe "Thanks for coming."

        scene v16s15_3
        with dissolve

        u "I'm never one to ignore a damsel in distress."

        scene v16s15_3a
        with dissolve

        pe "*Laughs* It's not that bad. It's just so awkward being the third wheel."

        pe "And I thought it'd be fun having you here with me."

    scene v16s15_3
    with dissolve

    u "So, where are the lovebirds?"

    scene v16s15_4 # TPP. Penelope points and MC looks over to see Imre and Karen standing next to each other talking to each other in the near distance, Penelope slight smile mouth open, Mc slight smile mouth is closed, Imre slight smile mouth is open, Karen slight smile mouth is closed, Imre and Karen are looking at each other
    with dissolve

    pe "They're just over there."

    scene v16s15_3
    with dissolve

    u "I need to experience this up close. Come on."

    scene v16s15_5 # TPP. MC and Penelope approach Imre and Karen slight everyone has slight smiles and mouths are closed except Imre who is waving MC and Penelope over slight smile mouth is open, Penelope is walking on MC's right
    with dissolve

    pause 0.75

    scene v16s15_6 # FPP. Show only Imre and Karen, slight smiles, Imre's mouth is open, Karen's mouth is closed, both of them looking at MC
    with dissolve

    imre "Oh, hey man! You're finally here."

    scene v16s15_6a # FPP. Show only Imre and Karen, slight smiles, Imre's mouth is closed, Karen's mouth is open, both of them looking at MC
    with dissolve

    karen "Hi, [name]."

    scene v16s15_6b # FPP. Show only Imre and Karen, slight smiles, both of their mouths are closed, both of them looking at MC
    with dissolve

    u "Hello, hello. So, how did this come about?"

    scene v16s15_6
    with dissolve

    imre "You remember that win-a-date stall that Karen was running at the Deer's event a while back? Well-"

    scene v16s15_6c # FPP. Karen hugs Imre still looking at MC half smile mouth is open, Imre is blushing mouth is closed is looking slightly away from Karen holding the back of his head with one hand and the other arm is around Karen's back.
    with dissolve

    karen "Imre won!"

    scene v16s15_6b
    with dissolve

    u "Haha, nice!"

    if v10lottery_ticket:

        scene v16s15_6b
        with dissolve

        u "All my hopes and dreams of winning have gone up in flames."

        scene v16s15_6d # FPP. Show only Imre and Karen, Imre slight smile mouth is closed, Karen is blushing slightly shocked expression, mouth is open, both of them looking at MC
        with dissolve

        karen "Really? Because we could-"

    scene v16s15_6e # FPP. Show only Imre and Karen, slight smiles, Imre's mouth is open, Karen's mouth is closed, Karen is looking at Imre, Imre is looking at MC
    with dissolve

    imre "So, yeah, anyway, it's just fun date."

    scene v16s15_6
    with dissolve

    imre "Are we going back in and hitting some rides or hanging out here like losers for the rest of the night?"

    scene v16s15_6a
    with dissolve

    karen "We'll go in, you can hang out here, haha."

    scene v16s15_6b
    with dissolve

    u "(Oh, shit.)"

    scene v16s15_7 # FPP. Show just Penelope looking at Imre, slight smile, mouth is open
    with dissolve

    pe "Haha! Yeah, Imre."

    scene v16s15_6f # FPP. Show only Imre and Karen, slight smiles, Imre's mouth is open, Karen's mouth is closed, both of them looking at Penelope
    with dissolve

    imre "Haha, yeah... Very funny."

    scene v16s15_6g # FPP. Show only Imre and Karen, slight smiles, Imre's mouth is closed, Karen's mouth is open, Karen and Imre are looking at each other
    with dissolve

    karen "Aw, isn't he cute when he gets embarrassed?"

    scene v16s15_6h # FPP. FPP. Show only Imre and Karen, slight smiles, Imre's mouth is open, Karen's mouth is closed, Karen and Imre are looking at each other
    with dissolve

    imre "I'm not embarrassed..."

    scene v16s15_6i # FPP Karen is pinching Imre's cheeks like a mother would to her child but Imre is blushing and not hating it, both of them slight smiles
    with dissolve

    u "(I think Imre has found his soulmate, haha.)"

    scene v16s15_6e
    with dissolve

    imre "Let's go!"

    scene v16s15_8 # TPP Keeping in pairs, they all walk through the entrance, Imre and Karen leading in front, MC and Penelope are walking together behind them, render can be made from back to avoid facial features, if not possible all slight smiles, mouths are closed, looking where they are walking
    with dissolve

    pause 0.75

    label v16s15_free_roam_pier_seen(backgroundImg, returnScreen, seenList):

        $ v16s15_seenList = seenList

        scene expression backgroundImg
        u "(We've already seen this attraction)"
        scene black
        $ renpy.call_screen(returnScreen)

    label v16s15pier_date

        scene v16s15_9 # -A single-screen free-roam with all four now stood inside the carnival. We can select the Carousel, the Wheel of chance, the Hot dog stand, and the Shooting range. Selecting the Shooting range will end the free roam, don't show any characters
        with dissolve

        v16s15pier_date_carousel: # -if Carousel
            $ freeroampier.add("carousel")
            $ v16s15_seenList = []

            scene v16s15_10 # TPP. The carousel has horses to sit on and also benches for more than one person. Imre and Karen sit on a bench. Imre puts his arm around Karen. She doesn't seem to notice, more interested in looking elsewhere. An older male carnival worker is standing nearby at the centre of the ride-
            with dissolve

            pause 0.75

            scene v16s15_11 # FPP. MC and Penelope are standing in front of the carousel ride, Penelope is looking at Mc slight smile, mouth is open
            with dissolve

            pe "I want one of the horses!  The bench seats are for babies. *Laughs*"

            scene v16s15_11a # FPP. MC and Penelope are standing in front of the carousel ride, Penelope is looking at Mc slight smile, mouth is closed
            with dissolve

            u "It's a carousel, Penelope. The whole thing is kind of for babies, haha."

            scene v16s15_11
            with dissolve

            pe "You know what I mean! I want to have a full carnival experience horses only!"

            scene v16s15_11b # FPP. Penelope crinkles her nose and raises her hands up to imitate having hooves like a horse, mouth is closed, slight smile, looking at MC
            with dissolve

            menu:

                "Sit alone":
                    $ add_point(KCT.BRO)
                    if penelope.relationship.value >= Relationship.GIRLFRIEND.value:
                        $ add_point(KCT.TROUBLEMAKER)

                    scene v16s15_11a
                    with dissolve

                    u "Haha, agreed. The horses are classic."

                    scene v16s15_12 # TPP. MC and Penelope sit on their own horses, next to each other, both of them looking at each other slight smiles, mouths are closed
                    with dissolve

                    pause 0.75

                    scene v16s15_13 # FPP. Show the carnival ride operator, standing behind ride controls, looking at MC and penelope, slight smile, mouth is open,
                    with dissolve

                    carni "Hold on tight, away we go!"

                    scene v16s15_14 # TPP. The ride begins. MC and Penelope are all smiles as they go around. They look across to each other. Quick shots in different poses
                    with dissolve

                    pause 0.75

                    scene v16s15_15 # TPP. The ride has gone through movement show a slightly different background, MC and Penelope are all smiles as they go around. They look across to each other. Quick shots in different poses
                    with dissolve

                    pause 0.75

                    scene v16s15_16 # TPP. The ride has gone through more movement show a slightly different background, MC and Penelope are all smiles as they go around. They look across to each other. Quick shots in different poses
                    with dissolve

                    pause 0.75

                    scene v16s15_17 # FPP. Show Penelope slight smile, mouth is closed, looking at MC 
                    with dissolve

                    u "It's so slow!"

                    scene v16s15_17a # FPP. Show Penelope slight smile, mouth is open, looking at MC 
                    with dissolve

                    pe "I know! Just pretend it's going super fast?"

                    scene v16s15_17b # FPP. Show Penelope slightly standing up in place like she's riding a rodeo horse, one hand in the air, and the other holding onto the horse, she is looking forward with an excited expression, mouth is open
                    with dissolve

                    pe "Wooooo! *Laughs*"

                    scene v16s15_12a # FPP. Show the carnival ride operator, standing behind ride controls, looking at MC and penelope, slight smile, mouth is closed
                    with dissolve

                    u "Come on, can't they make it go faster?"

                    scene v16s15_12
                    with dissolve

                    carni "Hey, I'll have you know I've set this ride at the perfect speed."

                    scene v16s15_12a
                    with dissolve

                    u "The perfect speed? I can walk faster than this!"

                    scene v16s15_12b # FPP. Show the carnival ride operator, standing behind ride controls, looking at MC and penelope, slightly annoyed, mouth is open
                    with dissolve

                    carni "Listen buddy, you think you know more about being a carousel operator than me? I'm protecting you."

                    carni "It used to go a lot faster, but an old lady broke her hip."

                    scene v16s15_12c # FPP. Show the carnival ride operator, standing behind ride controls, looking at MC and penelope, slightly annoyed, mouth is closed
                    with dissolve

                    menu:

                        "Laugh":
                            $ add_point(KCT.TROUBLEMAKER)

                            scene v16s15_12c
                            with dissolve

                            u "*Laughs*"

                            scene v16s15_12d # FPP. Show the carnival ride operator, standing behind ride controls, looking at MC and penelope, slightly angry, mouth is open
                            with dissolve

                            carni "Is that funny to you?!"

                            carni "If shitheads like you were in charge, it'd be cranked up to maximum speed and yourself and everyone else on this ride would be decapitated!"

                            scene v16s15_11c # TPP. MC and Penelope sit on their own horses, next to each other, both of them looking at each other with slightly serious expressions, Mc's mouth is open, Penelope's mouth is closed
                            with dissolve

                            pause 0.75

                            scene v16s15_12d
                            with dissolve

                            carni "So maybe you should be more respectful to the man currently holding your fucking life in the palm of his hands!"

                            scene v16s15_18 # TPP. Show two random terrified children on horses, one of them is crying. (IF YOU CAN'T MAKE THIS RENDER DUE TO AGE RESTRICTIONS OF CHARACTERS IN THIS GAME, THAN JUST JUST USE RENDER v16s15_11a IN THIS RENDERS PLACE)
                            with dissolve

                            u "(Holy shit, dude.... There are kids here.)"

                            scene v16s15_12d
                            with dissolve

                            carni "... Also, she sued us for a lot of money, so now we're not allowed to make it go any faster than this."

                        "Be polite":
                            $ add_point(KCT.BRO)

                            scene v16s15_12a
                            with dissolve

                            u "Oh, um... Alright, well. Thanks for letting us know."

                            scene v16s15_12
                            with dissolve

                            carni "You're welcome. We get a lot of complaints about how slow this ride is, but you have to understand I'm just trying to keep you safe!"

                            scene v16s15_12e # FPP. Show the carnival ride operator, standing behind ride controls, looking up at the sky, fist to his chest, with a very serious look on his face, mouth is open
                            with dissolve

                            carni "I won't let anyone get hurt... Not again."

                            u "(Wow, this guy is serious about his carousel. *Laughs*)"

                            ### ERROR: [End of Checkpoint 1.1. Continue to Checkpoint 2]

                "Sit with Penelope":
                    $ add_point(KCT.BOYFRIEND)

                    scene v16s15_11d # TPP. MC and Penelope are standing, next to a carousel horse both of them looking at each other slight smiles, Mc's mouth is open, Penelope's mouth is closed
                    with dissolve

                    u "Yeah, okay. Let's get on this one here."

                    scene v16s15_19 # FPP. Show just Penelope from the waist up, with the tops of carousel horses in the background, she is looking at Mc slight smile, mouth is open
                    with dissolve

                    pe "Together?"

                    scene v16s15_19a # FPP. Show just Penelope from the waist up, with the tops of carousel horses in the background, she is looking at Mc slight smile, mouth is closed
                    with dissolve

                    u "Sure. It'll be more fun."

                    scene v16s15_19
                    with dissolve

                    pe "Haha, okay! I hope there's enough room..."

                    scene v16s15_19a
                    with dissolve

                    u "Hey, what is that supposed to mean?"

                    scene v16s15_11e # TPP. penelope giggles and blushes, they get on the horse together, Penelope in front with MC behind, up close, no space between them, Mc slight smile, mouth is closed, both of them looking at each other
                    with dissolve

                    if penelope.relationship.value >= Relationship.GIRLFRIEND.value: # -if PenelopeRS

                        scene v16s15_20 # FPP. Show Penelope sitting in front of MC on the horse, looking over her shoulder back at MC, slight smile, mouth is open
                        with dissolve

                        pe "Um... *Giggles* I can feel something bulging..."

                        scene v16s15_20a # FPP. Show Penelope sitting in front of MC on the horse, looking over her shoulder back at MC, slight smile, mouth is closed
                        with dissolve

                        u "Haha, sorry, it's just my... phone."

                        scene v16s15_20
                        with dissolve

                        pe "Hmm, it doesn't feel like a phone..."

                        scene v16s15_20a
                        with dissolve

                        u "And what exactly does it feel like?"

                        scene v16s15_20
                        with dissolve

                        pe "Haha, [name], behave."

                    if v15s18cpen_oral: # -if MC also gave Penelope oral at Lauren's party

                        scene v16s15_20a
                        with dissolve

                        u "Oh, yeah? Like you behaved at Lauren's party?"

                        scene v16s15_20b # FPP. Show Penelope sitting in front of MC on the horse, looking over her shoulder back at MC, full smile, mouth is open 
                        with dissolve

                        pe "Oh, my God, [name]... Don't bring that up here, I'm gonna turn red!"

                        scene v16s15_20a
                        with dissolve

                        u "*Laughs* Why?"

                        scene v16s15_20
                        with dissolve

                        pe "*Sighs* That night was amazing. I still think about it a lot, ha."

                        scene v16s15_20a
                        with dissolve

                        u "Oh, yeah?"

                        scene v16s15_20
                        with dissolve

                        pe "Haha. Yeah, when I'm by myself."

                        scene v16s15_20a
                        with dissolve

                        u "Ah, sitting around and fantasizing about me? That's what you've been doing these days?"

                        scene v16s15_20c # FPP. Show Penelope sitting in front of MC on the horse, looking over her shoulder back at MC with puppy dog eyes, slight smile, mouth is open 
                        with dissolve

                        pe "I didn't say that was all I was doing..."

                        scene v16s15_20a
                        with dissolve

                        u "*Gasps* Are you talking dirty to me Penelope? *Chuckles*"

                        scene v16s15_20b
                        with dissolve

                        pe "Haha, not anymore. I think I better stop before your \"phone\" bursts through your jeans... *Laughs*"

                        scene v16s15_20a
                        with dissolve

                        u "(Oh, shit...) Yeah, it's a new model that... Um..."

                        u "It does that... When it's, uh... horny?"

                        scene v16s15_20b
                        with dissolve

                        pe "*Laughs*"

                        scene v16s15_20a
                        with dissolve

                        u "Sorry, I couldn't figure out where to take the innuendo from there, haha."

                        scene v16s15_20
                        with dissolve

                        pe "It's okay, you get an A for effort."

                    elif penelope.relationship.value >= Relationship.FRIEND.value: # -if PenelopeFriend

                        scene v16s15_20
                        with dissolve

                        pe "This is going to be an interesting ride!"

                        scene v16s15_20a
                        with dissolve

                        u "Haha, yeah. Be sure to check on me. I might fall off at any moment."

                        scene v16s15_20
                        with dissolve

                        pe "Right..."

                    scene v16s15_12
                    with dissolve

                    carni "Hold on tight! Away we g-"

                    scene v16s15_12b
                    with dissolve

                    carni "Actually, no. Hang on... You two! On the horse!"

                    scene v16s15_12c
                    with dissolve

                    u "(Us?)"

                    scene v16s15_12b
                    with dissolve

                    carni "You can't do that; you can't share one. We have weight limits for these horses."

                    scene v16s15_12c
                    with dissolve

                    u "Seriously? A weight limit?"

                    scene v16s15_12b
                    with dissolve

                    carni "Yes. Please get off and sit on one of the seats if you want to sit together."

                    scene v16s15_20c
                    with dissolve

                    pe "Boooo!"

                    scene v16s15_12c
                    with dissolve

                    karen "Yeah, boo!"

                    scene v16s15_12b
                    with dissolve

                    carni "We have safety regulations for a reason! Can't you see I'm trying to protect you?!"

                    scene v16s15_12f # FPP. Show the carnival ride operator, standing behind ride controls, he feels his head like he has a headache, rubs his temples, slightly annoyed expression, mouth is open, looking a MC and Penelope
                    with dissolve

                    carni "I am a carousel operator. I must enforce the safety regulations."

                    scene v16s15_12b
                    with dissolve

                    carni "I must keep you safe, no matter how much you spit on and boo and jeer me; For that is the oath I have taken."

                    scene v16s15_12e
                    with dissolve

                    carni "So, hate me if you must. But I WILL NOT let any harm fall upon you."

                    scene v16s15_12c
                    with dissolve

                    u "Whoa, okay... Hey man, we're getting off, see?"

                    scene v16s15_21 # TPP. MC and Penelope get down and go sit together in a seat, both no expressions, mouths are closed, looking at each other
                    with dissolve

                    pause 0.75

                    scene v16s15_12
                    with dissolve

                    carni "Okay, let's try this again. Everybody hold on tight... Away we go!"

                    scene v16s15_22 # FPP. Show Just Penelope from the shoulders up, just blue sky in the background, looking at Mc, slight smile, mouth is closed
                    with dissolve

                    u "Slowest ride ever... Haha!"

                    scene v16s15_22a # FPP. Show Just Penelope from the shoulders up, just blue sky in the background, looking at Mc, slight smile, mouth is open
                    with dissolve

                    pe "It really is, oh my... *Giggles*"

                    scene v16s15_22
                    with dissolve

                    u "Oh, I didn't ask yet. How did you get roped into coming with those guys?"

                    scene v16s15_22a
                    with dissolve

                    pe "Karen invited me. I only realized there was more to it once I had already gotten here."

                    scene v16s15_22
                    with dissolve

                    u "It's a bit weird that she invited you on her date, no?"

                    scene v16s15_22a
                    with dissolve

                    pe "Yeah, but I guess she's just shy and didn't want to meet Imre on her own?"

                    scene v16s15_22
                    with dissolve

                    u "Fair enough. One can only take so much of Imre at once."

                    scene v16s15_22a
                    with dissolve

                    pe "*Laughs* True."

                    ### ERROR: [End of Checkpoint 1.2. Continue to Checkpoint 2]

            ### ERROR: [Checkpoint 2 START]

            scene v16s15_23 # FPP. Show Imre and Karen sitting in their booth seat, Imre moves in for a kiss but Karen turns away
            with dissolve

            pause 0.75

            scene v16s15_23a # FPP. Show Imre and Karen sitting in their booth seat, Imre has a slightly sad expression, Karen has no expression, both of them looking at each other, mouths are closed
            with dissolve

            pause 0.75

            scene v16s15_23b # FPP. Show Imre and Karen sitting in their booth seat, Imre has a slightly sad expression mouth is open, Karen has no expression mouth is closed, both of them looking at each other 
            with dissolve

            imre "You don't want to kiss?"

            scene v16s15_23c # FPP. Show Imre and Karen sitting in their booth seat, Imre has a slightly sad expression mouth is closed, Karen has no expression mouth is open, both of them looking at each other 
            with dissolve

            karen "Not on a first date, Imre... You have to work harder for it."

            scene v16s15_23d # # FPP. Show Imre and Karen sitting in their booth seat, Imre is slightly upset mouth is closed, Karen is blushing mouth is closed, both of them looking at each other 
            with dissolve

            # -The ride ends-

            scene v16s15_12
            with dissolve

            carni "Please be careful as you dismount and exit the ride. If anyone has suffered any injuries, please go to the first-aid tent."

            scene v16s15_12e
            with dissolve

            carni "I refuse to let anyone die on my watch."

            scene v16s15_12a
            with dissolve

            u "We're good man, thanks."

            scene v16s15_12g # FPP. Show Penelope has walked up to the the carnival ride operator, smiling and giggling at the Ride operator, the ride operator is looking at Penelope with a slightly shocked expression
            with dissolve

            pe "*Giggles* Thank you! I felt so safe..."

            scene v16s15_12h # FPP Show Penelope has walked up to the the carnival ride operator, she has turned around and is now facing MC Penelope has a finger on her lip and an "I'm innocent" looking expression (like she is trying to act like she didn't make the ride operator blush on purpose), the ride operator is blushing looking at Penelope with a full smile, mouth is closed
            with dissolve

            pause 0.75

            scene v16s15_24 # TPP. MC and Penelope leave the carousel, both looking at each other, both of them laughing
            with dissolve

            pause 0.75

            scene v16s15_25 # TPP. Imre and Karen leave the carousel, both looking forward where they are walking, both of them slight smiles, mouths are closed
            with dissolve

            call screen v16s15pier_date        # -Return to free roam screen-

        v16s15pier_date_wheel: # -if Wheel of chance
            $ freeroampier.add("wheel")
            $ v16s15_seenList = []

            scene v16s15_26 # TPP Keeping in pairs the group approaches the Wheel of Chance, "Dylan" A short dude in a pink 'respect women' t-shirt is seen standing in front of the Wheel with an angry expression, mouth is open like he is yelling at the stall attendant, Imre and Karen leading in front, MC and Penelope are walking together behind them, render can be made from back to avoid facial features, if not possible all slight smiles, mouths are closed, looking where they are walking
            with dissolve

            pause 0.75

            scene v16s15_26a # TPP. "Dylan" A short dude in a pink 'respect women' t-shirt, turns away from the stall, upset. He passes and looks at the group he looks at the group and the group all looks at Dylan, Dylan has an angry expression mouth is open, everyone else has no expression, mouths are closed 
            with dissolve

            dy "Don't even bother with that thing! The wheel is completely rigged, bro!"

            scene v16s15_27 # FPP MC turns around, watching Dylan walk away, Dylan has an angry expression, mouth is closed
            with dissolve

            pause 0.75

            scene v16s15_28 # FPP. Show just Penelope, no expression, mouth is open, looking at MC
            with dissolve

            pe "He sounded upset..."

            scene v16s15_28a # FPP. Show just Penelope, no expression, mouth is closed, looking at MC
            with dissolve

            u "Yeah, he's probably right, but that's part of the carnival experience, right?"

            scene v16s15_28
            with dissolve

            pe "Getting scammed? Of course! *Laughs*"

            scene v16s15_29 # TPP. All four (Imre, Karen, Penelope, and MC) stand in front of the wheel of chance, all slight smiles, mouths are closed looking at the stall attendant. The stall attendant is an older woman running the game, long white hair like a witch, with a devious look in her eye
            with dissolve

            wa "Roll on up, you youngsters, have a spin! Everyone's a winner and it's only a dollar to enter!"

            scene v16s15_30 # FPP. Show just Imre and Karen, Imre handing money out towards the stall attendant, they both have slight smiles, Imre's mouth is open, Karen's mouth is closed
            with dissolve

            imre "Two spins, please. One for me and one for my date."

            scene v16s15_30a # FPP. Show just Imre and Karen, Imre has already handed the money to the attednant and is looking at Karen with a proud expression mouth is closed, Karen is looking at Imre with a full smile mouth is closed
            with dissolve

            pause 0.75

            scene v16s15_30b # FPP. Show just Imre and Karen, Imre and Karen are looking at each other, Imre's mouth is open, Karen's mouth is closed, both of them slgiht smiles
            with dissolve

            imre "I'm feeling lucky."

            scene v16s15_31 # FPP. Show just Imre and the stall attendant, Imre is looking at and spinning the wheel slight smile mouth is closed, The stall attendant has a devious look in her eye still looking at Imre mouth is closed
            with dissolve

            pause 0.75

            scene v16s15_32 # FPP. Show just the top portion of the wheel with a dial pointing at a red portion of the wheel with an image of an unwrapped candy on it
            with dissolve

            wa "We have a winner! Here's your candy."

            scene v16s15_31a # FPP. The attendant pulls a single piece of hard candy, unwrapped, out of her pants pocket, slight smile mouth is closed, Imre is looking at her smiling mouth is closed
            with dissolve

            pause 0.75

            scene v16s15_31b # FPP. The attendant hands Imre a single piece of hard candy, Imre takes it, both of them slight smiles, mouths are closed, both looking at each other
            with dissolve

            pause 0.75

            scene v16s15_31c # FPP. Imre immediately puts the candy in his mouth, he has chubby looking cheeks, looking at the attendant, the attendant is looking at Imre with a concerned expression, mouth is closed
            with dissolve

            pause 0.75

            scene v16s15_30c # FPP. Show just Imre and Karen, Imre and Karen are looking at each other, Imre's mouth is open with a piece of candy on his tongue slight smile, Karen is looking at Imre with a slightly disgusted expression, mouth is closed
            with dissolve

            imre "Nice!"

            scene v16s15_30d # FPP. Show just Imre and Karen, Imre and Karen are looking at each other, Imre's mouth is open with a piece of candy on his tongue slight smile, Karen is looking at Imre with a slightly disgusted expression, mouth is open
            with dissolve

            karen "Eww!"

            scene v16s15_30e # FPP. Show just Imre and Karen, Imre and Karen are looking at each other, Imre's mouth is open with a piece of candy on his tongue with a slightly concerned expression, Karen is looking at Imre with a slightly disgusted expression, mouth is closed
            with dissolve

            imre "What?"

            scene v16s15_30f # FPP. Show just Imre and Karen, Imre and Karen are looking at MC, Imre's mouth is open with a piece of candy on his tongue with a slightly concerned expression, Karen has a slightly disgusted expression, mouth is closed
            with dissolve

            u "Imre, that was just a random piece of candy..."

            scene v16s15_33 # FPP. Show just Penelope looking at the Stall attendant with a disgusted expression, mouth is open
            with dissolve

            pe "Out of your pocket? With no wrapper?"

            scene v16s15_34 # FPP. Show just the Stall attendant standing behind the "Wheel Game" with a devious expression and smile, mouth is open, looking at MC
            with dissolve

            wa "We didn't make any promises, ma'am."

            scene v16s15_30d
            with dissolve

            karen "That's so gross. Ugh..."

            scene v16s15_30e
            with dissolve

            imre "It's fine, guys. Germs can't attach to hard candy. It's science."

            scene v16s15_30d
            with dissolve

            karen "What? Who told you that?"

            scene v16s15_30e
            with dissolve

            imre "It's just common knowledge. Sugar kills germs. Back me up, [name]."

            scene v16s15_30f
            with dissolve

            u "It's literally the opposite, man..."

            imre "Well, what about the five second rule?"

            scene v16s15_33a # FPP. Show just Penelope looking at Imre with a disgusted expression, mouth is open
            with dissolve

            pe "I think it's been in her pocket longer than five seconds, Imre."

            scene v16s15_34
            with dissolve

            wa "All week so far!"

            scene v16s15_30f
            with dissolve

            imre "Uh, whatever... It's fine. Look-"

            scene v16s15_30g # FPP. Show just Imre and Karen, Imre's throws his head back and swallows the candy, Karen is looking at Imre with a very disgusted expression, mouth is closed
            with dissolve

            pause 0.75

            scene v16s15_30h # FPP. Show just Imre and Karen, Imre is looking at Karen with a proud expression mouth is closed, Karen is looking at Imre with a disgusted expression mouth is closed
            with dissolve

            imre "Finished."

            scene v16s15_33a
            with dissolve

            pe "You swallowed it whole?"

            scene v16s15_30i # FPP. Show just Imre and Karen, Imre and Karen are looking at MC, Imre has a slight smile mouth is open, Karen has no expression mouth is closed
            with dissolve

            imre "Well, I couldn't chew it up, ha! I'd break my teeth, dummy."

            scene v16s15_30j # FPP. Show just Imre and Karen, Imre and Karen are looking at MC, Imre has a slight smile mouth is closed, Karen has no expression mouth is closed
            with dissolve

            u "I worry about you sometimes, Imre."

            scene v16s15_30i
            with dissolve

            imre "Thanks, man. That's nice of you."

            scene v16s15_34
            with dissolve

            wa "And now for the lucky lady's turn."

            scene v16s15_30k # FPP. Show just Imre and Karen, Imre and Karen are looking at the stall attendant, Imre has a slight smile mouth is closed, Karen has no expression mouth is open
            with dissolve

            karen "Is every prize going to be garbage from your pocket?"

            scene v16s15_34
            with dissolve

            wa "You'll have to spin to find out!"

            scene v16s15_30k
            with dissolve

            karen "... *Sighs* Fine."

            scene v16s15_32a # FPP. Show just the top portion of the wheel with a dial pointing at a blue portion of the wheel with an image of a small piece of paper on it
            with dissolve

            pause 0.75

            scene v16s15_30k
            with dissolve

            karen "Wisdom? What does that mean?"

            scene v16s15_31d # FPP. The attendant hands Karen (Instead of Imre, Imre is not shown) a small piece of paper (like from a fortune cookie, but no cookie), Karen takes it no expression mouth is closed, the stall attendant has a slight smile mouth is closed
            with dissolve

            wa "Ooh, it's a special one. Here you go."

            scene v16s15_30l # FPP. Show just Imre and Karen, Imre and Karen are looking at each other, Imre's mouth is closed, Karen's mouth is open Karen looks at the piece of paper, reading whatever is written on it, Karen has no expression, Imre has a slight smile
            with dissolve

            karen "A great adventure awaits you today."

            scene v16s15_30m # FPP. Show just Imre and Karen, Imre and Karen are looking at the stall attendant, both of them no expressions, Imre's mouth is closed, Karen's mouth is open
            with dissolve

            karen "Is that it?"

            scene v16s15_33b # FPP. Show just Penelope looking at the Stall attendant with no expression, mouth is open
            with dissolve

            pe "It looks like it's from a fortune cookie."

            scene v16s15_30n # FPP. Show just Imre and Karen, Imre and Karen are looking at MC, both of them no expressions, Imre's mouth is open, Karen's mouth is closed
            with dissolve

            imre "I'm pretty sure that's what it is...."

            scene v16s15_30j
            with dissolve

            u "A dollar worth of wisdom! *Laughs*"

            scene v16s15_33c # FPP. Show just Penelope looking at MC with a slight smile, mouth is closed
            with dissolve

            u "Now it's our turn to be disappointed. Penelope?"

            scene v16s15_35 # TPP. Show just Mc and Penelope standing in front of the wheel, MC gestures Penelope to step forward, she happily does, both slight smiles, mouths are closed
            with dissolve

            pause 0.75

            scene v16s15_33d # FPP. Show just Penelope looking at MC with a slight smile, mouth is open
            with dissolve

            pe "[name]?"

            scene v16s15_36 # FPP. Show just MC and the stall attendant, MC is handing the stall attendant money he has a slight smile mouth is closed, The stall attendant has a devious look in her eye and a devious expression looking at MC
            with dissolve

            pause 0.75

            scene v16s15_33c
            with dissolve

            u "Ladies first."

            scene v16s15_33d
            with dissolve

            pe "Such a gentleman..."

            if penelope.relationship.value >= Relationship.GIRLFRIEND.value: # -penelopers kisses mc on the cheek-

                scene v16s15_37 # TPP. Show just Penelope Kissing Mc on the cheek, both slight smiles
                with dissolve

            scene v16s15_32
            with dissolve

            pause 0.75

            scene v16s15_33
            with dissolve

            pe "Candy again!"

            scene v16s15_34a # FPP. Show just the Stall attendant standing behind the "Wheel Game" holding out a piece of candy-with a devious expression and smile, mouth is open, looking at MC
            with dissolve

            wa "Here you a-"

            scene v16s15_33
            with dissolve

            pe "No, thanks. I'll pass."

            scene v16s15_34b # FPP. Show just the Stall attendant standing behind the "Wheel Game" with an annoyed expression, mouth is open, looking at MC
            with dissolve

            wa "Hmph. Suit yourself."

            scene v16s15_38 # FPP. Show just Imre looking at the stall attendant, slight smile, mouth is open
            with dissolve

            imre "I'll have it."

            scene v16s15_34b
            with dissolve

            wa "Sorry, no sharing allowed."

            scene v16s15_38
            with dissolve

            imre "Come on, man!"

            scene v16s15_40 # FPP. Show just Karen looking at MC, no expression, mouth is open
            with dissolve

            karen "*Whispers* Does this lady even work here?"

            scene v16s15_33e # FPP. Show just Penelope looking at Karen with a slight smile, mouth is open
            with dissolve

            pe "*Whispers* I'm not sure... But she looks like she lives here..."

            scene v16s15_39 # TPP. Show just Penenlope and Karen looking at each other and laughing. the girls giggle-
            with dissolve

            pause 0.75

            scene v16s15_33c
            with dissolve

            u "My turn! Let's win big..."

            scene v16s15_33c
            with dissolve

            menu:

                "Gentle spin":        # -MC spins. It lands on 'Hotdog'-
                    $ vs16s15hotdog_coupon = True
                    $ add_point(KCT.BRO)

                    scene v16s15_32b # FPP. Show just the top portion of the wheel with a dial pointing at a yellow portion of the wheel with an image of a coupoon with a hotdog on it
                    with dissolve

                    wa "Congratulations, young man! This is the best prize on the board if you ask me."

                    scene v16s15_34c # FPP. Show just the Stall attendant standing behind the "Wheel Game" with an annoyed expression, mouth is closed, looking at MC
                    with dissolve

                    u "Please don't pull an old hot dog out of your pocket..."

                    scene v16s15_33f # FPP. Show just Penelope looking at Mc with a full smile, mouth is open
                    with dissolve

                    pe "*Laughs*"

                    scene v16s15_38
                    with dissolve

                    imre "I'll eat it!"

                    scene v16s15_34d # FPP. Show just the Stall attendant standing behind the "Wheel Game" handing MC a 'free hotdog' coupon, with a slight smile, mouth is open, looking at MC 
                    with dissolve

                    wa "Here you go."

                    scene v16s15_34
                    with dissolve

                    wa "You can redeem it at the hotdog stand."

                    if v16s15_seenList = ["hotdog"]

                        scene v16s15_34e # FPP. Show just the Stall attendant standing behind the "Wheel Game" with a slight smile, mouth is closed, looking at MC 
                        with dissolve

                        u "Oh, we just left there, actually..."

                        scene v16s15_41 # FPP. Dylan comes out of nowhere, slight smile, mouth is open, looking at MC
                        with dissolve

                        dy "I'll take it!"

                        scene v16s15_41a # FPP. Dylan comes out of nowhere, slight smile, mouth is closed, looking at MC
                        with dissolve

                        u "Oh, sure. Here."

                        scene v16s15_42 # TPP. Show just MC and Dylan standing in front on the "Wheel Game" the attendant can be seen standing behind it looking at Mc and Dylan, MC hands Dylan the hotdog coupon, Mc has no expression mouth is closed, Dylan has a slight smile mouth is open, the Stall attendant has a slightly angry expression mouth is closed
                        with dissolve

                        pause 0.75

                        scene v16s15_42a # TPP. same as v16s15_42 Dylan is running away from MC and the attendant looking back at her and flipping her off full smile mouth is closed, the attendant is looking at Dylan with an angry expression mouth is open, Mc is looking at Dylan with a full smile mouth is open
                        with dissolve

                        wa "Hey, wait! No sharing!"

                        scene v16s15_42b # TPP. same as v16s15_42a Dylan has run further away and his mouth is open and the attendant's mouth is closed, everything else is the same.
                        with dissolve

                        dy "Fuck you, Linda!"

                        scene v16s15_38a # FPP. Show just Imre looking at MC, slight smile, mouth is open
                        with dissolve

                        imre "Haha! I love that guy!"

                        scene v16s15_34b
                        with dissolve

                        wa "You can all go now."

                        scene v16s15_38
                        with dissolve

                        imre "But I wanted to-"

                    else: # -if did not already go to hot dog stand

                        scene v16s15_34c
                        with dissolve

                        u "Phew, it's actually going to be edible. Nice!"

                        scene v16s15_33f
                        with dissolve

                        pe "Mmm! A hotdog does sound yummy..."

                        scene v16s15_33c
                        with dissolve

                        u "Hey, you turned down her pocket candy. This hot dog is mine!"

                    if penelope.relationship.value >= Relationship.GIRLFRIEND.value: # -if PenelopeRS

                        scene v16s15_33g # FPP. Penelope uses puppy dog eyes and flutters her lashes at MC, looking at MC, with a cute pouting expression, mouth is open
                        with dissolve

                        pe "But... But..."

                        scene v16s15_33h # FPP. Penelope looks slightly shocked, mouth is open, looking at MC
                        with dissolve

                        u "Those eye tricks don't work on me..."

                        scene v16s15_33i # FPP. Penelope pretends to cry, looking at Mc, mouth is closed
                        with dissolve

                        pe "*Sniffles*"

                        u "Okay, fine! Stop it with the tears! Jeez... *Sighs*"

                        scene v16s15_33j # FPP. Penelope acts cute, slight smile, mouth is open
                        with dissolve

                        pe "Hehe!"

                    else: # -if PenelopeFriend

                        scene v16s15_33k # FPP. Penelope frowns, and pouts her bottom lip, looking at Mc, mouth is open
                        with dissolve

                        pe "Meanie..."

                        scene v16s15_33c 
                        with dissolve

                        u "Oh, really? I'm a meanie?"

                        scene v16s15_33l # FPP. Penelope smirks, looks slightly away from MC, mouth is open
                        with dissolve

                        pe "No..."

                    scene v16s15_33c
                    with dissolve

                    u "Haha, alright. Everyone ready?"

                    scene v16s15_38a
                    with dissolve

                    imre "Yeah, let's blow this wheel scam."

                    scene v16s15_40a # FPP. Show just Karen, slight smile, mouth is open, looking at Mc
                    with dissolve

                    karen "Yes please!"

                "Strong spin":
                    $ add_point(KCT.TROUBLEMAKER)

                    scene v16s15_43 # TPP. Show just MC grabbing the wheel with both hands slight smile mouth is closed and the stall attendant standing behind the wheel with a devious smile, mouth is closed, looking at MC
                    with dissolve

                    pause 0.75

                    scene v16s15_44 # TPP. Show the wheel has broken, (either the wheel itself broke into pieces or just came off the axis, whatever is easier to render,) Both Mc and the stall attendant looking at the wheel with shocked expressions, mouths are open
                    with vpunch

                    imre "Oh, shit!"

                    pause 0.75

                    scene v16s15_45 # FPP. Show just the stall attendant standing over her broken wheel looking at MC with an angry expression, mouth is open, looking at MC
                    with dissolve

                    wa "You destroyed my wheel!"

                    scene v16s15_45a # FPP. Show just the stall attendant standing over her broken wheel looking at MC with an angry expression, mouth is closed, looking at MC
                    with dissolve

                    u "I'm sorry... I guess I just don't know my own strength, haha! That's crazy."

                    scene v16s15_45
                    with dissolve

                    wa "This wheel was a gift! How am I going to replace it?!"

                    scene v16s15_33b
                    with dissolve

                    pe "The wheel was a gift?"

                    scene v16s15_45a
                    with dissolve

                    u "What about my prize?"

                    scene v16s15_45
                    with dissolve

                    wa "Your prize? Your PRIZE?!"

                    wa "I won't call security. That's your prize for destroying my precious memory."

                    scene v16s15_45a
                    with dissolve

                    u "Damn, it's not like I did it on purpose."

                    scene v16s15_45
                    with dissolve

                    wa "Just go!"

        # -the group walks away, karen looks grossed out by smiling imre, and penelope and mc are either holding hands and smiling if RS or they are just smiling if they are just friends

        if penelope.relationship.value >= Relationship.GIRLFRIEND.value: # -if PenelopeRS

            scene v16s15_46 # TPP. The group walks away from the Wheel Stand, karen is walking next to Imre and looks grossed out by smiling imre both of their mouths are closed, Penelope and Mc are holding hands and smiling with mouths closed looking at each other as they are walking behind Imre and Karen
            with dissolve

        else: # -if PenelopeFriend

            scene v16s15_46a # TPP. The group walks away from the Wheel Stand, karen is walking next to Imre and looks grossed out by smiling imre both of their mouths are closed, Penelope and Mc are smiling with mouths closed looking at each other as they are walking behind Imre and Karen
            with dissolve

        call screen v16s15pier_date        # -Return to free roam screen-

        v16s15pier_date_carousel: # -if HotDog Stand
            $ freeroampier.add("hotdog")
            $ v16s15_seenList = []

            scene v16s15_47 # FPP. Imre puts money on the hotdog stand counter, Imre and Karen are looking at each other, with slight smiles, mouths are closed
            with dissolve

            pause 0.75

            scene v16s15_47a # FPP. Imre and Karen turn around to face MC and Penelope (Mc and Penelope are not shown,) Imre has a hotdog in one hand and a soda in the other slight smile mouth is closed looking at Mc, Karen doesn't have a hotdog, just a soda in one hand, slight smile, mouth is closed, looking at MC
            with dissolve

            pause 0.75

            scene v16s15_48 # FPP. Show just Penelope on MC's left looking at Karen, no expression, mouth is open
            with dissolve

            pe "Not hungry, Karen?"

            scene v16s15_49 # FPP. Show just Karen looking at Penelope on Mc's left, no expression, mouth is open
            with dissolve

            karen "I wouldn't mind a snack, but I'm vegan and they don't have any vegan options."

            scene v16s15_48
            with dissolve

            pe "What about popcorn?"

            scene v16s15_49
            with dissolve

            karen "I asked, it's all real butter though. The one thing this place doesn't cheap out on is the food, can you believe it? *Laughs*"

            scene v16s15_48
            with dissolve

            pe "Aw, it sucks they don't have anything."

            scene v16s15_49
            with dissolve

            karen "It's okay. I'm used to it."

            scene v16s15_50 # TPP. Show Karen and Imre walking past Penelope and MC, Imre is leaning in towards MC's ear to whisper to him he has a slight smile mouth is open, Mc has a slight smile mouth is closed, Penelope is slightly ahead of MC's direction with her back turned to MC and Imre, and Karen is slightly ahead of Imre's direction with her back turned to MC and Imre
            with dissolve

            imre "*Quietly* She might be vegan, but she'll be eating my meat later, haha."

            pause 0.75

            scene v16s15_51 # FPP. Show just full body image of Imre holding his hotdog around his pant's like it's his penis, with a cocky expression, mouth is open, looking at MC, Karen is seen walking away from Imre in the background with her back turned to the camera
            with dissolve

            u "With charm like that, man... How could she not?"

            scene v16s15_51a # FPP. Show Imre no longer posing with the hotdog, and has a slight smile, mouth is open, looking at Mc
            with dissolve

            imre "Ah, shut up."

            scene v16s15_52 # FPP. Show just the Hotdog Vendor, in the hotdog stall, looking up and away as if he's looking into a crowd, slight smile, mouth is open
            with dissolve

            hv "Next!"

            scene v16s15_52a # FPP. Show just the Hotdog Vendor, in the hotdog stall, looking directly at MC, slight smile, mouth is open
            with dissolve

            hv "Ah, hello there. I'm now going to amaze you with my psychic powers..."

            hv "You want a hotdog?"

            scene v16s15_53 # FPP. Show Just Penelope with part of the hotdog stand in the background, looking towards the Hotdog Vendor, slight smile, mouth is open
            with dissolve

            pe "You guessed it, haha. Yes, please. ."

            scene v16s15_52b # FPP. Show just the Hotdog Vendor, in the hotdog stall, looking at Penelope, slight smile, mouth is open
            with dissolve

            hv "My powers never fail! One hotdog coming right up!"

            if vs16s15hotdog_coupon: # -if MC already went to the Wheel of Chance and chose 'gentle spin' leading to a free hotdog coupon

                if penelope.relationship.value >= Relationship.GIRLFRIEND.value: # -if PenelopeRS

                    scene v16s15_53a # FPP. Show Just Penelope with part of the hotdog stand in the background, MC hands the hotdog coupon to Penelope, Penelope smiles, mouth is closed, looking at Mc
                    with dissolve

                    u "One free hot dog for the lady."

                    scene v16s15_53b # FPP. Show Just Penelope with part of the hotdog stand in the background, slight smile, mouth is open, looking at Mc
                    with dissolve

                    pe "Aw, you weren't kidding... You're so sweet."

                    scene v16s15_54 # TPP. Show Penelope holding and kissing MC in front of the hotdog stall, the Hotdog vendor is also shown looking at MC with a jealous/scowling expression
                    with dissolve

                else: # -if PenelopeFriend

                    scene v16s15_55 # FPP. Just show MC's hand with the hotdog coupon in it. 
                    with dissolve

                    u "(Penelope wants a hotdog, should I give her my coupon?)"

            scene v16s15_53b
            with dissolve

            menu:

                "Give her the coupon":
                    $ add_point(KCT.BOYFRIEND)

                    scene v16s15_53a
                    with dissolve

                    u "Here, you can use it."

                    scene v16s15_53b
                    with dissolve

                    pe "Woah, really?"

                    scene v16s15_53c # FPP. Show Just Penelope with part of the hotdog stand in the background, slight smile, mouth is closed, looking at Mc
                    with dissolve

                    u "Yeah, really."

                    scene v16s15_53b
                    with dissolve

                    pe "That's so sweet..."

                    scene v16s15_54a # TPP. same as v16s15_54 instead of kissing MC and Penelope are just hugging, the hotdog vendor still looks the same.
                    with dissolve

                    pause 0.75

                    scene v16s15_53c
                    with dissolve

                    pe "Thanks, [name]."

                "Keep the coupon":
                    $ add_point(KCT.BRO)
                    if penelope.relationship.value >= Relationship.GIRLFRIEND.value:
                        $ add_point(KCT.TROUBLEMAKER)

                    scene v16s15_55
                    with dissolve

                    u "(I could be nice... But I kinda want a hotdog.)"

                    u "(Sue me.)"

            scene v16s15_52c # FPP. The hotdog vendor hands Penelope her hotdog, both of them slight smiles, mouths are closed, looking at each other
            with dissolve

            pause 0.75

            scene v16s15_52a
            with dissolve

            hv "And now for you... I'm sensing a very powerful hunger for..."

            hv "A hotdog?"

            scene v16s15_52d # FPP. Show just the Hotdog Vendor, in the hotdog stall, looking at MC, slight smile, mouth is closed
            with dissolve

            u "Is there anything else on the menu? *Laughs*"

            scene v16s15_52a
            with dissolve

            hv "Nope!"

            scene v16s15_52d
            with dissolve

            u "One hotdog then, please!"

            scene v16s15_52e # FPP. Show the hotdog vendor handing MC a hotdog, slight smile, mouth is closed
            with dissolve

            pause 0.75

            scene v16s15_56 # FPP. Show MC walking back to and sitting down next to Penelope he has a slight smile mouth is closed looking at Penelope, Penelope is on MC's right as he sits down, Imre is directly across from MC, and Karen is diagonal from MC, everyone is looking at Mc slight smiles, mouths are closed, Imre has a hotdog and soda in front of him, Karen has just a soda in front of her, Penelope just has a hotdog in front of her, and Mc has just a hotdog in his hand
            with dissolve

            pause 0.75

            scene v16s15_57 # FPP. MC looks to his right and sees Penelope looking at Karen, slight smile mouth is open
            with dissolve

            pe "So, Karen, have you been a vegan all your life?"

            scene v16s15_58 # FPP. Mc looks diagonally and sees Karen looking at Penelope, slight smile, mouth is open
            with dissolve

            karen "Yeah, I was raised in a vegan household."

            scene v16s15_59 # FPP. MC looks directly ahead and sees Imre looking at Karen, slight smile, mouth is open
            with dissolve

            imre "A vegan household? Wait, do regular houses have meat in them?"

            scene v16s15_58a # FPP. Mc looks diagonally and sees Karen looking at Imre, slight smile, mouth is open
            with dissolve

            karen "No, Imre.... I mean that my parents were both vegan, so I was raised that way. Meat is just kind of disgusting to me."

            scene v16s15_59
            with dissolve

            imre "*Laughs* It was a joke by the way, I know what you meant."

            scene v16s15_57
            with dissolve

            pe "You don't even like the smell of meat?"

            scene v16s15_58
            with dissolve

            karen "Oh, God... Not at all. I can't even think past the fact it's a cooked animal."

            scene v16s15_58b # FPP. Mc looks diagonally and sees Karen looking at MC slight smile, mouth is closed
            with dissolve

            menu:

                "Respect veganism":
                    $ add_point(KCT.BRO)
                    $ add_point(KCT.BOYFRIEND)

                    scene v16s15_58b
                    with dissolve

                    u "I can understand why people choose not to eat meat. There are good health benefits as well."

                    u "Maybe I'll make this the last hotdog I ever eat, ha."

                    scene v16s15_58c # FPP. Mc looks diagonally and sees Karen looking at MC slight smile, mouth is open
                    with dissolve

                    karen "Haha, right... Good luck!"

                    scene v16s15_59a # FPP. MC looks directly ahead and sees Imre looking at MC, slight shocked, mouth is open
                    with dissolve

                    imre "Are you serious?"

                    scene v16s15_59b # FPP. MC looks directly ahead and sees Imre looking at MC, slight smile, mouth is closed
                    with dissolve

                    u "I'll let you know the next time I'm hungry for hotdogs, we'll see how I do. *Chuckles*"

                    scene v16s15_57a # FPP. MC looks to his right and sees Penelope looking at MC, slight smile mouth is open
                    with dissolve

                    pe "I've also heard that it's a lot healthier being vegan... Hmm."

                "Defend meat-eaters":
                    $ add_point(KCT.BRO)
                    $ add_point(KCT.TROUBLEMAKER)

                    scene v16s15_58d # FPP. Mc looks diagonally and sees Karen looking at MC slightly sad, mouth is closed
                    with dissolve

                    u "Animals eat each other all the time, though. The way I see it, eating meat is just letting nature run its course."

                    scene v16s15_57a
                    with dissolve

                    pe "The circle of life, right?"

                    scene v16s15_58d
                    with dissolve

                    u "Yeah, it's a constant cycle."

                    scene v16s15_58e # FPP. Mc looks diagonally and sees Karen looking at MC slightly sad, mouth is open
                    with dissolve

                    karen "You wouldn't be saying that if you knew anything about the meat industry, and how the animals are treated."

                    scene v16s15_58d
                    with dissolve

                    u "Maybe not but, eating beans and dip your whole life must be miserable."

                    scene v16s15_58c
                    with dissolve

                    karen "*Laughs* I love when people make that joke."

                    scene v16s15_59
                    with dissolve

                    imre "What do you mean?"

                    scene v16s15_57a
                    with dissolve

                    pe "There are millions of vegan recipes, just like normal food, haha."

                    scene v16s15_58a
                    with dissolve

                    karen "Yeah, especially these days, there are a lot of vegan restaurants opening. Some of them you wouldn't be able to tell are vegan."

                    scene v16s15_58b
                    with dissolve

                    u "Interesting."

            scene v16s15_59
            with dissolve

            imre "Karen, you don't know what you're missing out on."

            scene v16s15_58a
            with dissolve

            karen "You're right, I don't. It would probably make me sick, haha."

            scene v16s15_59
            with dissolve

            imre "Try some hotdog."

            scene v16s15_58a
            with dissolve

            karen "No, thanks."

            scene v16s15_60 # FPP. Show Imre and Karen sitting next to each other from where MC is sitting, Imre moves his hotdog towards Karen's face, Imre has a slight smile, mouth is open, Karen has no expression, mouth is closed, both of them are looking at each other
            with dissolve

            imre "Come on. Here. Try it."

            scene v16s15_60a # FPP. Show Imre and Karen sitting next to each other from where MC is sitting, Imre moves his hotdog closer towards Karen's face, Imre has a slight smile, mouth is closed, Karen has a slightly disgusted expression, mouth is open, both of them are looking at each other
            with dissolve

            karen "I said no, Imre."

            scene v16s15_60b # FPP. Show Imre and Karen sitting next to each other from where MC is sitting, Imre hotdog is now right up in Karen's face, Imre has a slight smile, mouth is closed, Karen has a greatly disgusted expression, mouth is closed, and she is trying to back her face away from the hotdog, both of them are looking at each other
            with dissolve

            imre "Just a small bite! Come on-"

            scene v16s15_60c # FPP. Show Imre and Karen sitting next to each other from where MC is sitting, Karen slaps the hotdog away from her face, Imre is extremely shocked mouth is open, Karen is extremely angry, mouth is open, , both of them are looking at each other
            with vpunch

            karen "No!"

            scene v16s15_60d # FPP. Show Imre and Karen sitting next to each other from where MC is sitting, Imre has no expression mouth is closed, Karen is extremely angry, mouth is open, both of them are looking at each other
            with dissolve

            karen "Fucking weirdo..."

            scene v16s15_60e # FPP. Show Imre and Karen sitting next to each other from where MC is sitting, Imre is looking down at the ground, Karen is looking at Imre, Imre has a slight sad expression mouth is open, Karen has a slightly angry expression looking at Imre
            with dissolve

            imre "Ah, man! My hotdog!"

            scene v16s15_57b # FPP. MC looks to his right and sees Penelope looking diagonally across at Imre, slight smile mouth is open
            with dissolve

            pe "Quick, Imre! Five second rule!"

            scene v16s15_59c # FPP. MC looks directly ahead and sees Imre looking diagonally across at Penelope, slight smile, mouth is open
            with dissolve

            imre "Oh, shit! Yeah!"

            scene v16s15_60d
            with dissolve

            karen "Imre, I swear to every God there is..."

            karen "If you eat that hotdog off the ground...!"

            scene v16s15_60f # FPP. Show Imre and Karen sitting next to each other from where MC is sitting, Imre has an anxious expression mouth is open, Karen is extremely angry, mouth is closed, both of them are looking at each other
            with dissolve

            imre "Um..."

            scene v16s15_60e
            with dissolve

            pause 0.75

            scene v16s15_60f
            with dissolve

            imre "I wasn't going to... Pfft."

            scene v16s15_60e
            with dissolve

            u "(Well, this is fucking awkward.)"

            scene v16s15_58f # FPP. Mc looks diagonally and sees Karen looking at Penelope with no expression, mouth is open
            with dissolve

            karen "Can we get back to the carnival games, please?"

            scene v16s15_57a
            with dissolve

            pe "Yeah, just as soon as I finish eating."

            scene v16s15_57c # FPP. MC looks to his right and sees Penelope looking at MC, slight smile mouth is open
            with dissolve

            u "I'll race you."

            scene v16s15_57a
            with dissolve

            pe "I'll have you know, I'm a two-time award-winning hotdog eating competitor."

            scene v16s15_57c
            with dissolve

            u "*Chuckles* ...Are you being serious right now?"

            scene v16s15_57a
            with dissolve

            pe "Mhmm."

            scene v16s15_57c
            with dissolve

            u "You have to tell me that story one day."

            scene v16s15_57a
            with dissolve

            pe "Deal, ha."

            scene v16s15_61 # TPP. Show just MC and Penelope sitting down from Imre and Karens viewpoint (Imre and Karen are not shown) MC bites half his hot dog while looking at Penelope, Penelope is looking at and smiling at MC but is acting like she's not impressed by MC
            with dissolve

            pause 0.75

            scene v16s15_61a # TPP. Show just MC and Penelope sitting down from Imre and Karens viewpoint (Imre and Karen are not shown) MC eats the other whole half of his hot dog, and his cheeks are puffed out from the food his mouth is open, Penelope is slightly shocked and laughing at MC, both of them are looking at each other
            with dissolve

            pause 0.75

            scene v16s15_61b # TPP. Show just MC and Penelope sitting down from Imre and Karens viewpoint (Imre and Karen are not shown) Mc still has puffy cheeks from the food his mouth is open, Penelope is smirking at Mc, mouth is open, both of them are looking at each other
            with dissolve

            pe "Wow, trying to show off?"

            u "*Muffled* Maybe."

            scene v16s15_61a
            with dissolve

            pause 0.75

            scene v16s15_62 # TPP. Show just Penelope and MC throwing away trash, Mc still has puffy cheeks, looking at Penelope, Penelope is laughing looking at MC
            with dissolve

            pause 0.75

            scene v16s15_63 # TPP. Show Penelope and Mc walking up to Imre and Karen, Mc still has puffy cheeks, Penelope is mimicking Mc his puffy cheeks looking at Imre and Karen, Imre and Karen are looking at Penelope and laughing, Mc is trying to hold his food in his mouth from laughing at Penelope
            with dissolve

            call screen v16s15pier_date            # -Return to free roam screen-

    v16s15pier_date_wheel: # -if Shooting range     # -Ends free roam-
        if not v16s15_seenList = ["wheel,""carousel,""hotdog"]

            u "(We should probably check out the other attractions first)"

        else: 

            jump v16s16