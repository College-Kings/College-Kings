# SCENE 27: Sex Ed Event
# Locations: Amphitheatre
# Characters: MR LEE (Outfit: 1), PENELOPE (Outfit: 3), MC (Outfit: 9), CHLOE (Outfit: 3), NORA (Outfit: 1), SEX ED TEACHER (Outfit: 1), CAMERON (Outfit: 3), LINDSEY (Outfit: 1)
# Time: Morning

label v16s27:
    scene v16s27_1 # TPP. MC (slight smile, mouth is closed,) Penelope (slight smile, mouth is closed,) and Lindsey (slight smile, mouth is closed,) enter the amphitheatre.
    with dissolve

    pause 0.75

    scene v16s27_2 # TPP. Penelope (slight smile, mouth is closed,) and Lindsey (slight smile, mouth is closed,) sit down next to each other. MC (slight smile, mouth is closed,) sits in a spare chair further away, next to a random female character (slight smile, mouth is closed,)
    with dissolve

    pause 0.75

    scene v16s27_3 # TPP. Mr Lee (slight smile, mouth is closed,) is standing at the front of the room. A Sex Ed teacher (slight smile, mouth is closed,) is sat at a desk at the front of the room
    with dissolve

    pause 0.75

    scene v16s27_4 # FPP. Show just Mr. Lee (slight smile, mouth is open, looking at MC) full body view standing at the front of the class
    with dissolve

    lee "Okay, students. Settle down please."

    lee "Instead of your regular classes, you have a very special class today, and I'm expecting you all to perform to the highest standard."

    lee "No, it's not a ten-hour lecture. I know you can't handle that much excitement."

    lee "Instead, you're all going to be learning about how to take care of a baby!"

    scene v16s27_5 # FPP. Show just Penelope (slight smile, mouth is open, looking at Mr. Lee) raising her hand
    with dissolve

    pe "Mr. Lee? I don't mean to be rude, but what does this have to do with history?"

    scene v16s27_4a # FPP. Show just Mr. Lee (slight smile, mouth is open, looking at Penelope) full body view standing at the front of the class
    with dissolve

    lee "That's a great question, Penelope!"

    lee "The first thing you need to do before you can become a parent is settle on a partner. A decision not to be taken lightly."

    scene v16s27_4b # FPP. Show just Mr. Lee (slight smile, mouth is closed, looking at MC) full body view standing at the front of the class
    with dissolve

    u "(So, he's just not going to tell us or...?)"

    scene v16s27_4c # FPP. Show just Mr. Lee (slight smile, mouth is open, looking at MC) pointing a finger at the his head in a "use your mind manner," full body view standing at the front of the class
    with dissolve

    lee "Choose wisely!"

    scene v16s27_6 # TPP. Show 4 random characters (2 male and 2 female) 2 pairs, each pair has (1 male and 1 female,) all slight smiles, mouths are closed, looking at their paired partner
    with dissolve

    pause 0.75

    scene v16s27_7 # TPP. Show Nora (slight smile, mouth is closed, looking at MC) sitting in her seat with a bunch of seats between her and Chloe, and Chloe (slight smile, mouth is closed, looking at her phone) sitting in her seat with her phone in her hands.
    with dissolve

    u "(Looks like most people have chosen their partner already! I need to be quick before everyone else is taken!)"

    scene v16s27_7
    with dissolve

    menu (fail_label="v16s27_default_chloe_parent"): # 3 second timer default
        "Parent with Chloe":
            $ v16s27_parent_chloe = True

            jump v16s27_choose_chloe_parent
        
        "Parent with Nora":
            $ v16s27_parent_chloe = False

            scene v16s27_9 # FPP. Show just Nora (slight smile, mouth is closed, looking at MC) sitting in her seat, camera angle is from a seated positon
            with dissolve

            u "Nora?"

            scene v16s27_9a # FPP. Show just Nora (slight smile, mouth is open, looking at MC) sitting in her seat, camera angle is from a seated positon
            with dissolve

            no "Yes. I'll be your wife for the class, haha."

            scene v16s27_9
            with dissolve

            u "Haha, perfect."

            scene v16s27_9a
            with dissolve

            no "But no jerking around. I really want to learn how to be a good parent."

            scene v16s27_9
            with dissolve

            u "Okay, it's a deal."

            u "(Nice. I figured she'd be totally into this.)"
            
            jump v16s27_continue_after_parent_choice
        
    label v16s27_default_chloe_parent:
        $ v16s27_parent_chloe = True

        scene v16s27_8 # FPP. Show just Chloe (no expression, mouth is closed, looking at her phone) sitting in her seat with her phone in her hands, camera angle is from a seated positon
        with dissolve

        u "(Chloe's sitting closest to me. I'll just go with her.)"
    
    label v16s27_choose_chloe_parent:
        scene v16s27_8 
        with dissolve

        u "Hey, Chloe. Want to partner up for this?"

        scene v16s27_8a # FPP. Show just Chloe (no expression, mouth is closed, looking at MC) sitting in her seat with her phone in her hands, camera angle is from a seated positon
        with dissolve

        pause 0.75

        scene v16s27_8b # FPP. Show just Chloe (no expression, mouth is open, looking at her phone) sitting in her seat with her phone in her hands, camera angle is from a seated positon
        with dissolve

        cl "Oh, yeah, sure."

        scene v16s27_8a
        with dissolve

        u "You don't sound too interested."

        scene v16s27_8c # FPP. Show just Chloe (no expression, mouth is open, looking at MC) sitting in her seat with her phone in her hands, camera angle is from a seated positon
        with dissolve

        cl "Well, we have to play with baby dolls. *Scoffs*"

        scene v16s27_8b
        with dissolve

        cl "It's got nothing to do with history so it's probably not going to be on the final. Plus, this is just..."

        scene v16s27_8c
        with dissolve

        cl "Well, it's kinda lame, isn't it?"

        scene v16s27_8
        with dissolve

        u "Depends on your perspective."

        scene v16s27_8c
        with dissolve

        cl "Well, my perspective is that it's lame."

        scene v16s27_8a
        with dissolve

        u "Fair enough. Maybe you'll change your mind one day?"

        scene v16s27_8b
        with dissolve

        cl "It's possible, but that's a concern for me in the future me."

        scene v16s27_8
        with dissolve

        u "(Perhaps she'll show more interest once we know exactly what we've got to do.)"

    label v16s27_continue_after_parent_choice:# -Regardless of parent choice-

        scene v16s27_4
        with dissolve

        lee "Now that we have that out of the way, I'll leave you in the capable hands of your sex ed teacher."

        scene v16s27_3a # TPP. Mr Lee (slight smile, mouth is closed, looking at the Sex Ed Teacher,) with an extended arm outstrecthed towards her in a "presenting" manner, The Sex Ed Teacher (slight smile, mouth is closed, looking at Mr. Lee,) holding a baby doll stands up from the desk and walks towards Mr. Lee
        with dissolve

        pause 0.75

        scene v16s27_10 # TPP. Show Mr. Lee's back turned to the render, leaving the Amphitheatre
        with dissolve

        pause 0.75

        scene v16s27_11 # FPP. Show just Sex Ed Teacher (SET) (slight smile, mouth is open, looking at MC) holding up the baby doll with both hands
        with dissolve

        sexed "Hello, class. I'd like everyone to look at this baby."

        if not v16s27_parent_chloe: # Parent with Nora 

            scene v16s27_9b # FPP. Show just Nora (slight smile, mouth is open, looking at the (SET)) sitting in her seat, camera angle is from a seated positon
            with dissolve

            no "Awww!"

        else:

            scene v16s27_9c # FPP. Show just Nora (slight smile, mouth is open, looking at the (SET)) sitting in her seat, camera angle is from a seated positon, with multiple seats between MC and Nora (MC is not shown)
            with dissolve

            no "Awww!"

        scene v16s27_11a # FPP. Show just Sex Ed Teacher (SET) (slight smile, mouth is open, looking at Nora) cradling the baby doll
        with dissolve

        sexed "No need to be jealous. *Chuckles* You're all going to be getting one of these to look after."

        scene v16s27_11b # FPP. Show just Sex Ed Teacher (SET) (slight smile, mouth is closed, looking at MC) cradling the baby doll
        with dissolve

        u "(How are we supposed to look after a doll?)"

        scene v16s27_11c # FPP. Show just Sex Ed Teacher (SET) (slight smile, mouth is open, looking at MC) cradling the baby doll
        with dissolve

        sexed "Now, let's go through the rules."

        sexed "What do these babies need? They need feeding, they need burping, they need their diapers changed."

        scene v16s27_12 # FPP. Show just Cameron (slight smile, mouth is open, looking at the (SET,))
        with dissolve

        ca "Just like the Wolves, haha!"

        scene v16s27_11c
        with dissolve

        sexed "If your baby is upset for any reason, it'll cry. But lucky for you, each baby comes with a set of keys."

        scene v16s27_11d # FPP. Show just Sex Ed Teacher (SET) (slight smile, mouth is open, looking at MC) cradling the baby doll with one arm, and now holding up three FOB keys
        with dissolve

        sexed "Use the correct key and the crying will stop. The blue one is for feeding. The green one is for burping. The orange one is for changing its diaper."

        scene v16s27_11e # FPP Show just Sex Ed Teacher (SET) (slight smile, mouth is open, looking at MC) cradling the baby doll with one arm, and now only holding one FOB key and touching the key to the baby's lips, make a small green light appear on the FOB key
        with dissolve

        sexed "Simply touch the correct key on the baby's mouth for feeding or burping." 

        scene v16s27_11f # FPP Show just Sex Ed Teacher (SET) (slight smile, mouth is open, looking at MC) cradling the baby doll with one arm, and now only holding one FOB key and touching the key to the babys lower back, make a small green light appear on the FOB key
        with dissolve

        sexed "Or to change the diaper, touch the correct key on the baby's lower back."

        scene v16s27_11g # FPP Show just Sex Ed Teacher (SET) (slight smile, mouth is open, looking at MC) cradling the baby doll with one arm, and now only holding one FOB key and touching the key to the baby's lips, make a small red light appear on the FOB key
        with dissolve

        sexed "The sensor inside will detect whether you've used the correct one or not."

        if v16s27_parent_chloe: # -if MC is parenting with Chloe
            scene v16s27_8
            with dissolve

            u "(Is she paying attention to any of this?)"

            scene v16s27_8
            with dissolve

            menu:
                "Say something":
                    $ add_point(KCT.TROUBLEMAKER)

                    scene v16s27_8a
                    with dissolve

                    u "Are you remembering any of this?"

                    scene v16s27_8b
                    with dissolve

                    cl "Yeah, yeah. Tap the key on it to stop it crying. It's not rocket science, [name]."

                    scene v16s27_8
                    with dissolve

                    u "You should probably take some notes though?"

                    scene v16s27_8d # FPP. Show just Chloe (slightly annoyed expression, mouth is open, looking at MC) sitting in her seat with her phone in her hands, camera angle is from a seated positon
                    with dissolve

                    cl "*Scoffs* Don't be so serious. There's nothing to worry about. It's easy!"

                "Keep quiet":
                    $ add_point(KCT.BRO)

                    scene v16s27_8
                    with dissolve

                    u "(She's obviously not, and I don't feel like starting an argument.)"

        else:# -if MC is parenting with Nora
            scene v16s27_9d # FPP. Show just Nora (slight smile, mouth is closed, looking at the (SET)) sitting in her seat, camera angle is from a seated positon
            with dissolve

            u "(Should I check that Nora's getting all this?)"

            scene v16s27_9d
            with dissolve

            menu:
                "Talk to her":
                    $ add_point(KCT.TROUBLEMAKER)

                    scene v16s27_9
                    with dissolve

                    u "Are you remembering all of this?"

                    scene v16s27_9e # FPP. Show just Nora (slight annoyed expression, mouth is open, looking at MC) sitting in her seat, camera angle is from a seated positon
                    with dissolve

                    no "Shhh!"

                    scene v16s27_9d
                    with dissolve

                    u "(I guess that answers my question...)"

                "Say nothing":
                    $ add_point(KCT.BRO)

                    scene v16s27_9
                    with dissolve

                    u "(Nah, she looks like she's absorbing all the info. She'll make a great fake-baby mom, ha.)"
            
        # -Regardless of partner choice-

        scene v16s27_11c
        with dissolve

        sexed "It's all pretty straight forward. Once you've spent some time with your baby, you will start to understand it's needs."

        sexed "Just like in real life, the babies will cry when you're trying to sleep."

        sexed "Therefore, these night babies, as they're called, will activate from ten at night until ten in the morning."

        scene v16s27_11b
        with dissolve

        u "(Seriously? Goodbye sleep! *Sighs*)"

        scene v16s27_11c
        with dissolve

        sexed "You and your partner will be caring for the baby for three nights in total and return your baby on Saturday where I will evaluate your performance."

        sexed "As partners, each of you will spend one night alone with the baby as well as one night together. So, all that's left for you and your partner is to agree on a schedule."

        scene v16s27_11b
        with dissolve

        u "(Okay, let's see what's best...)"

        # TODO: UI SCREEN #!#!#!#!# -The UI pops up, showing the three nights, and MC can choose the baby-duty schedule- #!#!#!#!#

        scene v16s27_11b
        with dissolve

        u "(I'm sure that'll work out okay.)"

        scene v16s27_11c
        with dissolve

        sexed "Oh, and one final thing. Feel free to name your baby whatever you want."

        scene v16s27_11b
        with dissolve

        u "(I guess we'd better name it something...)"

        if v16s27_parent_chloe: # -if chloe partner
            scene v16s27_8a
            with dissolve

            u "Any suggestions for a name?"

            scene v16s27_8e # FPP. Show just Chloe (slight smile, mouth is open, looking at MC) sitting in her seat with her phone in her hands, camera angle is from a seated positon
            with dissolve

            cl "Plastic? *Laughs*"

            scene v16s27_8f # FPP. Show just Chloe (slight smile, mouth is closed, looking at MC) sitting in her seat with her phone in her hands, camera angle is from a seated positon
            with dissolve

            u "Ha, seriously?"

            scene v16s27_8e
            with dissolve

            cl "I honestly don't care, [name]. Just pick something."

            scene v16s27_8
            with dissolve

            menu:
                "Plastic, it is":
                    $ add_point(KCT.BRO)

                    $ baby.username = "Plastic"

                    scene v16s27_8a
                    with dissolve

                    u "Alright, baby Plastic. I hope you like your new name."

                    scene v16s27_8c
                    with dissolve

                    cl "*Sighs* I don't think it has much of an opinion."

                "A different name":
                    # -Player gets to type baby name-

                    # $ BABY_NAME = name = renpy.input(_("What's your baby's name?"), default=_("Baby")).strip() or _("Baby")
                    $ baby.username = v16_baby = renpy.input("What's your baby's name?", default=("Plastic").strip())

                    scene v16s27_8c
                    with dissolve

                    cl "[v16_baby], huh?"

                    scene v16s27_8a
                    with dissolve

                    u "Yeah, it's perfect."

                    scene v16s27_8c
                    with dissolve

                    cl "Okay, whatever you say."

        else: # -if nora partner
            scene v16s27_9
            with dissolve

            u "What are you thinking? Nora junior? *Laughs*"

            scene v16s27_9a
            with dissolve

            no "Haha, no! Come on, let's do something cute like... Henry or..."

            scene v16s27_9
            with dissolve

            no "Scarlet?"

            scene v16s27_9a
            with dissolve

            u "Hmm, well, have we got a boy or a girl?"

            scene v16s27_9
            with dissolve

            no "Umm, that doesn't really matter I don't think."

            scene v16s27_9a
            with dissolve

            u "Ha, okay... (Let her pick, or suggest something else?)"

            scene v16s27_9
            with dissolve

            menu:
                "Scarlet or Henry?":
                    $ add_point(KCT.BOYFRIEND)
                    $ v16_baby = "Henry"

                    scene v16s27_9
                    with dissolve

                    u "So which one?"

                    scene v16s27_9a
                    with dissolve

                    no "You don't care?"

                    scene v16s27_9
                    with dissolve

                    u "No, I mean- I do care, I just like both of them. You can pick."

                    scene v16s27_9f # FPP. Show just Nora (half smile, mouth is closed, looking at MC) sitting in her seat, camera angle is from a seated positon
                    with dissolve

                    pause 0.75

                    scene v16s27_9a
                    with dissolve

                    no "Okay. Baby Henry, then?"

                    scene v16s27_9
                    with dissolve

                    u "Sounds good, yeah."

                "Something else":
                    # -Player gets to type baby name-

                    $ baby.username = v16_baby = renpy.input("What's your baby's name?", default=("Henry").strip())

                    scene v16s27_9g # FPP. Show just Nora (slight smile, mouth is closed, looking in the air) in a thinking pose sitting in her seat, camera angle is from a seated positon
                    with dissolve

                    no "Hmm..."

                    u "Is that okay?"

                    scene v16s27_9a
                    with dissolve

                    no "Ha, sure. [v16_baby] it is."
                
        # -Regardless of baby name-

        scene v16s27_11c
        with dissolve

        sexed "And that's everything!"

        sexed "Congratulations, and welcome to parenthood! Your babies will be available for collection this evening so please stop by later to pick them up."

        sexed "And I'll see you all in three days at the Nurse's office for your reviews. Have a good day, parents!"

        if v16s27_parent_chloe: # -if MC is parenting with Chloe
            scene v16s27_8e
            with dissolve

            cl "*Sighs* Thank God that's over with. Now we can get on with our lives."

            scene v16s27_8f
            with dissolve

            u "Look, I can tell you're not too excited about this. But can we at least try? I don't exactly want to fail this thing."

            scene v16s27_8b
            with dissolve

            cl "Yeah, I know. There are just more important things for me to do right now."

            scene v16s27_8a
            with dissolve

            u "Chloe, this is a project for a class. We're here for an education at the end of the day. Can we prioritize that for a second?"

            scene v16s27_8d
            with dissolve

            cl "Like I said, it's not for a grade, [name]. It's just a stupid baby doll that they want us to get sleep deprived over."

            scene v16s27_8a
            with dissolve

            u "Well then let's get sleep deprived! This is supposed to be an experience, and I chose you as my partner because I thought it'd be fun."

            scene v16s27_8c
            with dissolve

            cl "Okay, well I'm not going to pretend that I actually gave birth to this thing."

            scene v16s27_8d
            with dissolve

            cl "If you wanted someone who was going to act like a \"mommy\", you should've partnered with Nora."

            scene v16s27_8b
            with dissolve

            cl "I bet she'd happily wake up at 3am to burp the stupid thing."

            scene v16s27_8a
            with dissolve

            u "Okay, I'm not asking you to play house with me, Chloe. Let's just try to get through it."

            scene v16s27_8c
            with dissolve

            cl "Okay, fine."

            scene v16s27_8
            with dissolve

            u "(I already feel like a single dad over here.)"

        else: # -if MC is parenting with Nora
            scene v16s27_9a
            with dissolve

            no "Yay! I actually can't wait to get started on this, haha."

            scene v16s27_9
            with dissolve

            u "It's gonna be a real test to confirm if you'd want kids in the future or not."

            scene v16s27_9a
            with dissolve

            no "Oh, I already know I want kids. Not sure how many though."

            no "No matter how this project goes, I'll still want to be a mom one day."

            scene v16s27_9
            with dissolve

            u "You're one of those people who has everything in life mentally planned out, huh? *Chuckles*"

            scene v16s27_9a
            with dissolve

            no "Haha, quite a lot of it, actually."

            no "Can you blame me, though? I've been doing nothing but reflecting, accepting, and improving these past few weeks. Figured a lot of things out."

            scene v16s27_9
            with dissolve

            u "That sounds great, and I'm happy for you... But let's see how you do at 4am when [v16_baby] needs a diaper change. *Laughs*"

            scene v16s27_9h # FPP. Show just Nora (half smile, mouth is open, looking at MC) sitting in her seat, camera angle is from a seated positon
            with dissolve

            no "Haha, I'll do it with a smile! I guarantee Chloe will be ripping her hair out across the hall, but I'm excited."

            scene v16s27_9
            with dissolve

            u "(Well, now I'm convinced. We should pass this easily.)"

        # -Regardless of partner choice-

        scene v16s27_13 # TPP. Show the random students (slight smiles, mouths are closed,) from render v16s27_5 walking out of the Amphitheatre
        with dissolve

        pause 0.75

        scene v16s27_14 # TPP. Show just MC (slight smile, mouth is closed,) standing at the exit to the Amphitheatre.
        with dissolve

        pause 0.75

        if v14_help_lindsey: # -if MC is helping Lindsey
            scene v16s27_14a # TPP. Show MC (slight smile, mouth is closed, looking at Lindsey) standing at the exit to the Amphitheatre, and Lindsey (slight smile, mouth is closed, looking at MC) approaching MC
            with dissolve

            pause 0.75

            scene v16s27_15 # FPP. Show just Lindsey (slight smile, mouth is open, looking at MC) with the Amphitheatre exit in the background
            with dissolve

            li "Hey, don't think you're escaping just yet! Haha, we need to go plan for phase three of my campaign!"

            scene v16s27_15a # FPP. Show just Lindsey (slight smile, mouth is closed, looking at MC) with the Amphitheatre exit in the background
            with dissolve

            u "Whoa, back to work already without paternity leave? That's harsh..."

            scene v16s27_15b # FPP. Show just Lindsey (no expression, mouth is open, looking at MC) with the Amphitheatre exit in the background
            with dissolve

            li "*Sighs* Really?"

            scene v16s27_14b # TPP. Show MC (slight smile, mouth is open, looking at Lindsey) with his hands in the air like he surrenders, and Lindsey (slight smile, mouth is closed, looking at MC) standing at the exit to the Amphitheatre
            with dissolve

            u "Hey, you're the boss."

            scene v16s27_14c # TPP. Show MC (slight smile, mouth is closed, looking at Lindsey) with his hands in the air like he surrenders with his back turned to Lindsey and looking over his shoulder at Lindsey, while Lindsey (laughing, mouth is open, looking at MC) and playfully pushing MC out of the Amphitheatre exit
            with dissolve

            jump v16s28 # -Transition to Scene 28-

        else: # -if MC is not helping Lindsey
            jump v16s29 # -Transition to Scene 29-