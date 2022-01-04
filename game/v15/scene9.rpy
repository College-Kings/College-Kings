# SCENE 9: Wedding_announcement_and_Wheres_Nora
# Locations: School Hallway Near Library
# Characters: MC (Outfit: 5), AUBREY (Outfit: 1)
# Time: AfterNoon
# Render Count: 4 Unique, 31 Total

label v15s9:
    scene v15s9_1 # TPP. MC is now walking along the hallway near the library, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v15s9_2 # FPP. MC see's Aubrey is walking the other way from a slight distance, Aubrey waves at Mc, They smile at each other and stop to chat, Aubrey's mouth is slightly open
    with dissolve

    pause 0.75

    scene v15s9_3 # FPP. Aubrey is now face to face with MC, Aubrey slight smile, mouth closed
    with dissolve

    u "Hey!"

    scene v15s9_3a # FPP. same as v15s9_3 Aubrey increases to half smile, mouth open
    with dissolve

    au "Hi! You're just the guy I wanted to see, haha."

    scene v15s9_3b # FPP. same as v15s9_3a Aubrey's mouth is closed
    with dissolve

    u "Oh, really?"

    scene v15s9_3a
    with dissolve

    au "Yeah. I kind of have a weird favor to ask, but it should be fun... I hope. *Chuckles*"

    scene v15s9_3b
    with dissolve

    u "Okay... So far it doesn't sound very convincing, but I'll give you a chance"

    scene v15s9_3c # FPP. same as v15s9_3a Aubrey rolls her eyes
    with dissolve

    au "Haha, shut up! Just hear me out."

    scene v15s9_3a
    with dissolve

    au "My parents have decided to renew their wedding vows, so there's going to be a little ceremony."

    scene v15s9_3b
    with dissolve

    u "Oooh, fun... Haha."

    scene v15s9_3a
    with dissolve

    au "Yeah, I know, right? *Sighs*"

    au "Anyway, there will be food and drinks, so all we need to do is dress to impress."

    scene v15s9_3b
    with dissolve

    u "We?"

    scene v15s9_3d # FPP. same as v15s9_3a Aubrey's head is slightly tilted down, looking up at mc, playing with her hair
    with dissolve

    au "Yeah, so... I was kind of hoping you'd accompany me for the night, haha."

    scene v15s9_3b
    with dissolve

    u "You want me to come to your parent's vow renewal ceremony? *Laughs*"

    scene v15s9_3a
    with dissolve

    au "I know, it doesn't sound like a very fun night. But we can have fun together, we always do, yeah?"

    scene v15s9_3b
    with dissolve

    u "(There's no reason why I can't go with her, at least for moral support. But, I should make it clear if I want something more from her...)"

    u "Of course I'll come, yeah. But..."

    menu:
        "As friends":
            scene v15s9_3
            with dissolve

            u "It's just as friends, right? Or do I have to pretend to be your boyfriend? *Laughs*"

            # This removes AubreyTamed from the player and pushes them back into AubreyFriend, NOT FwB.-
            if v13s48_canoeing_as_date:
                $ aubrey.relationship = Relationship.FRIEND

                scene v15s9_3e # FPP. same as v15s9_3d Aubrey has a disapointed expression, looking away from MC
                with dissolve

                pause 0.75

                scene v15s9_3
                with dissolve

                au "Well, no... Ha, you don't have to pretend. If you want to go as friends that sounds fine."

                scene v15s9_3b
                with dissolve

                u "Haha, good. I'm not the best actor so that would've been a disaster. *Laughs*"

                scene v15s9_3d
                with dissolve

                au "Ha..."

            else:
                scene v15s9_3f # FPP. same as v15s9_3d Aubrey puts a hand to her chest in relief, head tilted slightly upward and looking away, facial expression is that of relief, slight smile, mouth open
                with dissolve

                pause 0.75

                scene v15s9_3a
                with dissolve

                au "Haha! No, no, no... No acting, just casual friends having a good time at an old couple's second wedding."

                scene v15s9_3b
                with dissolve

                u "Perfect. *Chuckles* That sounds like a plan."

                scene v15s9_4 # TPP. Show Aubrey and Mc standing next to each other, Aubrey gives MC a quick, friendly hug, both slight smiles, mouths closed
                with dissolve

                pause 0.75

                scene v15s9_3a
                with dissolve

                au "Thank you so much, [name]."

        "As your date":
            scene v15s9_3b
            with dissolve

            u "I'd like to come as your date if that's okay."

            if v13s48_canoeing_as_date:
                $ aubrey.relationship = Relationship.TAMED

                scene v15s9_3g # FPP. same as v15s9_3b Aubrey slightly blushes, head slightly tilted down, looking at mc, full smile, mouth closed
                with dissolve

                pause 0.75

                scene v15s9_3a
                with dissolve

                au "It's more than okay, actually... *Chuckles*"

                scene v15s9_3b
                with dissolve

                u "Really? You mean-"

                scene v15s9_3h # FPP. same as v15s9_3a Aubrey slightly pushes Mc with one hand, and covers her mouth from laughter with the other, Aubrey rolls her eyes
                with dissolve

                au "Okay, don't let it get to your head! Slow down, big guy... *Laughs*"

                scene v15s9_3b
                with dissolve

                u "Ha..."

                scene v15s9_3i # FPP. same as v15s9_3g Aubrey head is not tilted, looking straight at MC, slight smile, mouth open
                with dissolve

                au "But yeah, I'm starting to enjoy time with you as... you know..."

                scene v15s9_3b
                with dissolve

                u "A couple?"

                scene v15s9_3j # FPP. same as v15s9_3 Aubrey smirks
                with dissolve

                pause 0.75

                scene v15s9_3a
                with dissolve

                au "That's a strong word... *Chuckles*"

                scene v15s9_3b
                with dissolve

                u "Not really."

                scene v15s9_3k # FPP. same as MC v15s9_3a Aubrey increases to full smile, and touches Mc's face
                with dissolve

                au "Let's see how the night goes, okay?"

                scene v15s9_3b
                with dissolve

                u "Okay, I can do that."

                scene v15s9_3l # FPP. same as v15s9_3 Aubrey winks and a nice smile
                with dissolve

                pause 0.75

            else:
                scene v15s9_3m # FPP. same as v15s9_3f Aubreys head is tilted slightly to the side, looking at Mc like a lost puppy, slight smile mouth closed with a slightly curled bottom lip
                with dissolve

                pause 0.75

                scene v15s9_3i
                with dissolve

                au "[name]... I appreciate what you're trying to do, really..."

                au "But I really just need a friend right now."

                scene v15s9_3b
                with dissolve

                u "Ouch... I just got stabbed with the friendzone knife didn't I..."

                scene v15s9_3a
                with dissolve

                au "Eh, maybe. Probably just indigestion."

                scene v15s9_3b
                with dissolve

                u "Haha... *Sighs*"

                u "Okay. I got you, as a friend."

                scene v15s9_3a
                with dissolve

                au "Thank you. I can't imagine what it'd be like without having you there..."

                scene v15s9_4
                with dissolve

                pause 0.75

    scene v15s9_3a
    with dissolve

    au "So, my parents are sending a car to pick me up from the Chicks' house on Sunday morning."

    scene v15s9_3b
    with dissolve

    u "Sunday morning, got it."

    scene v15s9_3a
    with dissolve

    au "Yes, and don't be late!"

    scene v15s9_3b
    with dissolve

    u "No tardiness, noted..."

    scene v15s9_3a
    with dissolve

    au "And remember, dress to impress!"

    scene v15s9_3b
    with dissolve

    u "Fuck's sake okay..."

    scene v15s9_4a # TPP. same as v15s9_4 Aubrey is looking at mc with a confused/happy expression, slight smile, mouth closed, Mc is looking directly at Aubrey, with one hand extended outward as if he is holding a notebook in one hand palm up, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v15s9_4b # TPP. same as v15s9_4a Aubrey is now smirking at MC, Mc is now using his other hand to mimic holding a pencil
    with dissolve

    pause 0.75

    scene v15s9_4c # TPP. same as v15s9_4b Aubrey is now laughing and rolling her eyes, Mc is now looking at his hand pretending to write on his imaginarey notepad
    with dissolve

    u "Sunday... Don't be late... Dress nice..."

    scene v15s9_3a
    with dissolve

    au "Are you done? *Chuckles*"

    scene v15s9_3b
    with dissolve

    u "Mhmm, got it."

    scene v15s9_3n
    with dissolve

    au "Oh, one last thing..."


    au "Have you seen Nora? Nobody's heard from her since we landed at the airport. You know she broke up with Chris?"

    if joinwolves:
        scene v15s9_3o
        with dissolve

        u "Yeah, uh... Chris told us. It's kinda weird not seeing them together anymore. I was wondering where she was too."

        scene v15s9_3n
        with dissolve

        au "She's not answering her phone either, no matter who calls. It's all just so weird to me..."

        scene v15s9_3o
        with dissolve

        u "Agreed, I haven't seen her since the airport either. I actually sent her a text last night but nothing... I'll let you know if I hear anything."

    else:
        scene v15s9_3o # FPP. same as v15s9_3n Aubrey's mouth is closed
        with dissolve

        u "Well, shit... No, the last time I saw her was at the airport too. I hope she's okay."

        scene v15s9_3n
        with dissolve

        au "Me too. So, you don't know if anyone has heard from her?"

        scene v15s9_3o
        with dissolve

        u "I don't, but I'll keep an eye out and if I hear anything I'll call."

    scene v15s9_3n
    with dissolve

    au "Okay, thank you. It's been a few days now and some of us are starting to worry."

    au "I think I'm gonna pay Chris a visit and see what he has to say for himself."

    scene v15s9_3o
    with dissolve

    u "Ha, good luck with that."

    scene v15s9_3a
    with dissolve

    au "It's worth a try, right? I should get going though, thanks again for coming on Sunday."

    scene v15s9_3b
    with dissolve

    u "Seriously, no problem. See you soon, Aubs."

    scene v15s9_4d # same as v15s9_4 Aubrey is walking away from MC, waving goodbye, slight smile, mouth closed, MC is waving bye to Aubrey slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v15s9_1b # TPP. same as v15s9_1 show mc standing in the hallway, looking up and away holding his chin in thought, mouth closed
    with dissolve

    u "(Maybe I'll try Nora one more time... Let's see if she picks up the phone.)"

    scene v15s9_1c # TPP. same as v15s9_1b show a close up shot of Mc putting his phone to his ear, no expression, mouth closed
    with dissolve

    pause 0.75

    scene v15s9_1d # TPP. same as v15s9_1c MC has an excited/happy looking expression on his face, mouth open
    with dissolve

    no "Hey! This is Nora!"

    scene v15s9_1e # TPP. same as v15s9_1d Mc has a depressed look on his face, mouth closed
    with dissolve

    no "And I'm obviously doing something far more important than what you're calling about, so leave a message and-"

    scene v15s9_1f # TPP. same as v15s9_1b MC hangs up, and puts his phone away, no expression, mouth slightly open
    with dissolve

    u "*Sighs* (Straight to voicemail... Probably overloaded with messages from the girls anyway.)"

    scene v15s9_1g # TPP. MC continues walking along the hallway, no expression, mouth closed
    with dissolve

    pause 0.75

    $ v15s10_buyer_max_amount = 425

    if v14_pics_with_linds:
        $ v15s10_buyer_max_amount += 200

    $ v15s10_buyer_max_amount += (len(v14s47_car_pics) - 1) * 25

    if "v14s47_passenger_2b.webp" in v14s47_car_pics or "v14s47_passenger_2f.webp" in v14s47_car_pics:
        $ v15s10_buyer_max_amount += 50

    # Buyer's willingness to pay =
    #    425 by default
    #   +200 if Lindsey is in the pictures
    #   + 25 for every picture taken after the first one (can earn up to 3*25 = 75)
    #   + 50 if special picture taken (either Lindsey Hand on Hips, or Bird)
    
    # If the sum of the above is less than the listing price selected for the car in v14s48, the sale fails.
    
    # Other things that affect willingness to pay:
    #     penalty if you lie in the description (does not influence whether scene 10 appears, buyer only realizes it's a lie in scene 10)
    #     the exact amount of the penalty increases with the original sales price (up to $200)
    
    # Sale is for either the listed price, or buyer's willingness to pay by this point, whichever is lowest
    
    #   + 50 if you lie in the description and Lindsey is in the pictures (does not influence sale, it's a bonus that the male buyer pays afterwards)

    if v14_lindsey_sell:
        scene v15s9_1h # TPP. same as v15s9_1g Different Camera angle
        with dissolve

        pause 0.75

        play sound "sounds/vibrate.mp3"

        if v14s48_car_price <= v15s10_buyer_max_amount:
            $ v15_lindsey_sold = True
            
            $ lindsey.messenger.newMessage("Hey! Somebody wants to check out the car and they sound really interested!", force_send=True)
            $ lindsey.messenger.newMessage("I'm meeting them now. Can you come to where we took the photos?", force_send=True)

            if v14s48_car_description == CarDescription.LIE: # PLACEHOLDER - CHECK WITH OSCAR THE VARIABLE IN THE APP!
                $ lindsey.messenger.addReply("See? Lying works in mysterious ways, haha OMW", func=None)

            else:
                $ lindsey.messenger.addReply("Honesty is the best policy! Heading there now.", func=None)

            call screen phone

            scene v15s9_1f
            with dissolve

            pause 0.75

            scene v15s9_1h
            with dissolve

            pause 0.75

            jump v15s10

        else:
            $ lindsey.messenger.newMessage("24 hours is up! No interested buyers on the car... :(", force_send=True)
            $ lindsey.messenger.addReply("Ugh, that sucks! I'm sorry", func=None)
            $ lindsey.messenger.newMessage("It sucks big time! I think we messed up on the price...")
            $ lindsey.messenger.addReply("Can we change the price and list it again?", func=None)
            $ lindsey.messenger.newMessage("I thought about it, but it costs way too much. Let's just move on.")
            $ lindsey.messenger.addReply("Fuck, okay. What's next?", func=None)
            $ lindsey.messenger.newMessage("Are you on campus right now? We need to plan the next phase of the campaign.", force_send=True)
            $ lindsey.messenger.addReply("Yeah, I am. What's the plan?", func=None)
            $ lindsey.messenger.newMessage("Let's go to back to the janitor's closet and you'll find out ;)")
            $ lindsey.messenger.newMessage("Meet me at the end of the main hallway?")
            $ lindsey.messenger.addReply("Sure thing, be with you in a bit.", func=None)

            if lindsey.relationship.value >= Relationship.FWB.value:
                $ lindsey.messenger.addReply("Be there soon ;)", func=None)
            else:
                $ lindsey.messenger.addReply("OMW", func=None)

            call screen phone

            scene v15s9_1f
            with dissolve

            pause 0.75

            scene v15s9_1g
            with dissolve

            u "(Damn, I thought we did a decent job of pricing that thing... Hindsight's a bitch.)"

            scene v15s9_1h
            with dissolve

            pause 0.75

            jump v15s12

    elif v14_help_lindsey:
        scene v15s9_1h
        with dissolve

        pause 0.75

        play sound "sounds/vibrate.mp3"

        $ lindsey.messenger.newMessage("Hey! Are you on campus right now? We need to plan the next phase of the campaign.", force_send=True)
        $ lindsey.messenger.addReply("Yeah, I am. What's next?", func=None)
        $ lindsey.messenger.newMessage("Let's go to back to the janitor's closet and you'll find out ;)")
        $ lindsey.messenger.newMessage("Meet me at the end of the main hallway?")
        $ lindsey.messenger.addReply("Sure thing, be with you in a bit.", func=None)

        label v15s9_PhoneContinueLin:
            if lindsey.messenger.replies:
                call screen phone
            if lindsey.messenger.replies:
                u "(I should reply to Lindsey.)"
                jump v15s9_PhoneContinueLin

        jump v15s12        

    elif v15_mad_at_ms_rose:
        scene v15s9_1h
        with dissolve

        pause 0.75

        jump v15s14

    else:
        scene v15s9_1h
        with dissolve

        pause 0.75
        
        jump v15s13