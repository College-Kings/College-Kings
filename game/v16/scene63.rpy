# SCENE 63: Chloe's Chicks Spa Day
# Locations: Chicks house/spa
# Characters: MC (Outfit: 2), JENNY (Outfit: teal towel), CHLOE (Outfit: pink towel), AUBREY (Outfit: dark red towel), NORA (Outfit: royal blue towel), LINDSEY (Outfit: purple towel)
# Time: Thursday Evening

label v16s63: # 63) Chloe's Spa Day
    play sound "sounds/knock.mp3"

    scene v16s63_1 # TPP Show MC knocking on the Chicks' front door
    with fade

    pause 0.75

    scene v16s63_2 # FPP Jenny (smile, mouth closed) answers, wearing nothing but a teal/turquoise colored towel wrapped around her, holding a candle-
    with dissolve

    u "Oh, hey, Jenny!"

    if jenny.relationship == Relationship.FWB: # -if JennyRS

        scene v16s63_2a # FPP Same angle as 2. Jenny (slight smile, mouth open) at the door in her towel
        with dissolve

        jen "Hello, handsome... Surprised to see me? *Giggles*"

    else: # -if not JennyRS
        scene v16s63_2a
        with dissolve

        jen "Haha, surprised to see me, [name]?"

    scene v16s63_2
    with dissolve

    u "A little bit. I thought this was a Chick's only thing."

    scene v16s63_2a
    with dissolve

    jen "Can't it also be a Chloe's friends thing?"

    scene v16s63_2
    with dissolve

    u "Ha, yeah, of course. I'm not complaining."

    u "What's with the candle?"

    scene v16s63_2b # FPP Same angle as 2. Jenny (annoyed, mouth open) at the door with her towel
    with dissolve

    jen "There's another power outage."

    scene v16s63_2c # FPP Same angle as 2. Jenny (annoyed, mouth closed) at the door with her towel
    with dissolve

    u "Damn, what's going on with that lately?"

    scene v16s63_2b
    with dissolve

    jen "I don't know, but it's really annoying! At least the candles fit in with the spa night vibes."

    scene v16s63_2c
    with dissolve

    u "*Laughs* Very true."

    scene v16s63_2a
    with dissolve

    jen "So, you're here to help?"

    scene v16s63_2
    with dissolve

    u "Hell yeah, I am!"

    scene v16s63_2a
    with dissolve

    jen "Get your ass in here then!"

    scene v16s63_3 # TPP Show MC following Jenny into the house
    with dissolve

    pause 0.75

    # -(There are candles throughout every room mentioned during Spa night.) Jenny leads MC into the living room. Jenny sits down on a chair.

    scene v16s63_4 # TPP Show MC following Jenny through the Chicks house toward the living room. The house is dark with a lot of candles set around for light
    with dissolve

    pause 0.75

    # Already in the room wearing different colored towels: Chloe wearing baby pink, Aubrey wearing dark red/burgundy, Nora wearing a dark/royal blue and Lindsey wearing purple/lilac. 
    # All are smiling, having a good time, drinking sparkling white wine in champagne flute glasses. Chloe, Aubrey and Nora are sat on the couch in that order. 
    # Lindsey is on a separate chair (keep Lindsey and Jenny far apart)-
    
    scene v16s63_5 # FPP Show living room of Chicks house, lit with candles. Chloe, Aubrey, Nora, Lindsey, and Jenny are in the room as described above
    with dissolve

    pause 0.75

    if v16s12_chloe_planboard_decide_mc_gives_massages or v16s61_chloe_pb_override_mc_gives_massages: # -if MC is Masseuse

        scene v16s63_5a # FPP Same angle as 5. Chloe (slight smile, mouth open) looking at MC
        with dissolve
        
        cl "Girls, our masseuse is here!"

    else: # -if MC is Standard help

        scene v16s63_5a
        with dissolve

        cl "Ooh, looks like our spa assistant has arrived... *Chuckles*"
    
    # -Regardless of MC's role-

    if chloe.relationship == Relationship.GIRLFRIEND: # -if ChloeGf

        scene v16s63_5b # FPP Same angle as 5. Chloe (slight smile, mouth open) looking over toward other girls
        with dissolve

        cl "The one night I'll share him with the rest of you... Haha."

        if aubrey.relationship == Relationship.TAMED: # -if AubreyTamed (Passed date night)

            # -Aubrey half smile, she isn't loving the fact that mc has a girlfriend or 2 or 3 or 4 or... ahem excuse me anyway or the fact that they're all in the same room together
            
            scene v16s63_6 # FPP Close up of Aubrey (neutral expression, mouth open) who is pointedly avoiding eye contact with Chloe
            with dissolve

            au "How kind of you..."

            scene v16s63_6a # FPP Same angle as 6. Aubrey (neutral expression, mouth closed) looking at MC
            with dissolve

            u "(This isn't awkward... Luckily Aubrey knows I'm in a relationship, but I don't think she's liking the idea of it.)"

        if nora.relationship == Relationship.FWB: # -if NoraRS

            scene v16s63_7 # FPP Close up of Nora (slight smile, eyebrow raised, mouth closed) looking at MC
            with dissolve

            no "Hmm..."

            u "(Nora seems excited about the sharing...)"

        scene v16s63_8 # FPP Close up of Jenny (smiling, mouth open) looking toward Chloe
        with dissolve

        jen "Share him? Haha, wait-"

        if jenny.relationship == Relationship.FWB: # -if JennyRS

            scene v16s63_8a # FPP Same angle as 8. Jenny (confused expression, slight smile, mouth open) looking at Chloe
            with dissolve
            
            jen "You're dating...?"

            scene v16s63_8b # FPP Same angle as 8, Jenny (confused expression, mouth closed) looking at MC
            with dissolve

            u "(Oh, did I forget to mention that part? Oops...)"

            scene v16s63_9 # FPP Close up on Chloe (smiling, mouth open) looking toward Jenny
            with dissolve

            cl "Yes... Ha."

        else: # -if not JennyRS
        
            scene v16s63_8c # FPP Same angle as 8, Jenny (laughing, mouth open) looking toward Chloe
            with dissolve

            jen "Oh, yeah! You're dating, holy shit! I just remembered. *Laughs* Sorry."

            scene v16s63_9
            with dissolve

            cl "Haha, it's okay."

    scene v16s63_6b # FPP Same angle as 6, Aubrey (slight smile, mouth open) looking at MC
    with dissolve

    au "Is he going to strip for us first?"

    scene v16s63_7a # FPP Same angle as 7, Nora (laughing, mouth open) looking toward Aubrey
    with dissolve

    no "*Laughs* Aubrey..."

    scene v16s63_8d # FPP Same angle as 8, Jenny (smiling, mouth open) looking at MC
    with dissolve

    jen "It would be rude of him not to, honestly."

    scene v16s63_5
    with dissolve

    menu:
        "Maybe later":
            u "Haha, damn, pouncing on me as soon as I'm through the door, ladies? Maybe later, if you're lucky."

            scene v16s63_8d
            with dissolve

            jen "Boooo!"

            scene v16s63_9
            with dissolve

            cl "Hah, okay, okay... Enough booing our volunteer!"

        "I'm expensive": 
            $ add_point(KCT.TROUBLEMAKER)

            scene v16s63_5
            #with dissolve

            u "I hate to break it to you ladies but, I'm expensive. I don't think you can afford this."

            scene v16s63_6b
            with dissolve

            au "We could pay you in other ways, I'm sure."

            scene v16s63_6c # FPP Same angle as 6, Aubrey (slight smile, mouth closed) looking at MC
            with dissolve

            u "Oh, really? Such as?"

            scene v16s63_7a
            with dissolve

            no "Food stamps. *Laughs*"

            scene v16s63_6d # FPP Same angle as 6, Aubrey (laughing, mouth open) throwing her head back, laughing
            with dissolve

            au "Haha!"

    # -Regardless of MC reaction-

    scene v16s63_10 # FPP Close up on Lindsay (slight smile, mouth open) looking at MC
    with dissolve

    li "Hope you're ready to work hard, we're needy. *Giggles*"

    scene v16s63_9a # FPP Same angle as 9, Chloe (slight smile, mouth open) looking toward other girls
    with dissolve

    cl "Um, he will. That's why he's here."

    scene v16s63_5c # FPP Same angle as 5. Chloe and Lindsay sharing an awkward glance, mouths closed
    with dissolve

    u "(Wow, looks like Chloe and Lindsey are being as fake-friendly as possible tonight. I wonder how long that'll last...)"

    scene v16s63_9a
    with dissolve

    cl "Anyway, everyone stop looking at [name] like a piece of meat and let's get on with the pampering!"

    scene v16s63_8
    with dissolve

    jen "We can do both, no? Tee-hee..."

    scene v16s63_5
    with dissolve

    u "(These girls are wild when they get together... Not that I'm complaining, haha.)"

    scene v16s63_9a
    with dissolve

    cl "Oh, also!"

    scene v16s63_9b # FPP Same angle as 9, Chloe (slight smile, mouth open) pointing toward the kitchen
    with dissolve

    cl "I put a suggestion box on the kitchen table. So please, throughout the night, add anything you want me to consider or discuss."

    scene v16s63_7a
    with dissolve

    no "Anything? *Scoffs*"

    scene v16s63_9a
    with dissolve

    cl "Yes... And it's anonymous, so don't hold back."

    scene v16s63_8
    with dissolve

    jen "That's a great idea."

    scene v16s63_6e # FPP Same angle as 6, Aubrey (slight smile, mouth open) looking toward Chloe
    with dissolve

    au "Yeah, I agree."

    scene v16s63_9a
    with dissolve

    cl "Thank you, ladies."

    scene v16s63_9c # FPP Same angle as 9, Chloe (slight smile, mouth closed) looking toward other girls
    with dissolve

    u "(I might have some fun with that later...)"

    scene v16s63_7b # FPP Same angle as 7, Nora (slight smile, mouth open) looking at MC
    with dissolve

    no "So, what's first on the agenda?"

    scene v16s63_7c # FPP Same angle as 7, Nora (slight smile, mouth closed) looking at MC
    with dissolve

    u "I think I'm giving you all a facial."

    scene v16s63_7a
    with dissolve

    no "Oh, my God... *Laughs*"

    scene v16s63_10
    with dissolve

    li "Haha! Are you?"

    scene v16s63_6b
    with dissolve

    au "*Giggles* Damn, at least take us out to dinner first."

    scene v16s63_9a
    with dissolve

    cl "Ha, ladies... Quit pestering!"

    scene v16s63_9b
    with dissolve

    cl "[name], the face masks are on the kitchen table."

    scene v16s63_9d # FPP Same angle as 9, Chloe (slight smile, mouth closed) looking at MC
    with dissolve

    u "Got it, I'll go fetch them."

    if chloe.relationship == Relationship.GIRLFRIEND: # -if chloeGF

        scene v16s63_9e # FPP Same angle as 9, Chloe (smiling, mouth open) looking at MC
        with dissolve

        cl "Thank you, baby."

        # -every time ChloeGF says something like this, NoraRS and AubreyRS have to pretend like it doesn't bother them, but it still does. 
        # Lots of straight faces, side-eye looks, and half-smiles during these moments. 
        # JennyRS is a bit more sad than the others during these moments bc she wasn't aware of MC's relationship with Chloe beforehand, she keeps her head down though, and stays positive for chloe.

        # -if mc also has a romantic relationship with Aubrey, Nora, or Jenny
        if nora.relationship == Relationship.FWB or aubrey.relationship == Relationship.TAMED or jenny.relationship == Relationship.FWB:
            
            scene v16s63_9d
            with dissolve

            u "(Yeah, Chloe. Just keep stabbing the same wound ... *Sighs* I feel like I'll need to have a few conversations after tonight.)"

            if nora.relationship >= Relationship.FWB:

                scene v16s63_7
                with dissolve

                pause 0.75

            if aubrey.relationship >= Relationship.TAMED:
                
                scene v16s63_6a
                with dissolve

                pause 0.75

            if jenny.relationship >= Relationship.FWB:
                
                scene v16s63_8e # FPP Same angle as 8, Jenny (slightly sad expression, mouth closed) looking down
                with dissolve

                pause 0.75

    scene v16s63_11 # TPP MC in the kitchen, the table visible in the shot. The facemasks are on the table, near the suggestion box and some pens with little squares of paper. MC looking at suggestion box
    with dissolve

    u "(Should I add a suggestion? It's anonymous so I can put anything I want.)"

    menu:
        "Compliment Chloe":
            
            $ add_point(KCT.BOYFRIEND)
            $ v16s63x_chloe_suggestion_set.add("v16s63_compliment")

            scene v16s63_12 # FPP View of suggestion box on the table
            with dissolve

            u "(I'll just tell Chloe she's doing a great job and to keep it up. She'll appreciate that.)"

        "Suggest a breast reduction":
            
            $ add_point(KCT.TROUBLEMAKER)
            $ v16s63x_chloe_suggestion_set.add("v16s63_breast_reduciton")

            scene v16s63_12
            with dissolve

            u "(I'm feeling mischievous... I'll say Chloe's boobs are too big and suggest a reduction. She'll be pissed and will probably think it was Nora or Lindsey.)"

        "Don't add a suggestion":
            
            scene v16s63_12
            with dissolve

            u "(Nah, I've got no reason to meddle any more than I already have, haha.)"

    # -Regardless of suggestion choice-

    if len(v16s63x_chloe_suggestion_set) > 0: # -if MC chose to write something

        scene v16s63_13 # TPP Show MC writing something on a piece of paper (what he's writing is not visible)
        with dissolve

        pause 0.75

        scene v16s63_12a # FPP Same angle as 12, MC placing a folder piece of paper into the suggestion box
        with dissolve

        pause 0.75

    scene v16s63_14 # TPP Show MC, holding the facemasks, walking away from the kitchen table
    with dissolve

    pause 0.75

    scene v16s63_5
    with dissolve

    u "Alright, who wants a facemask? And fair warning, I've never done this before..."

    scene v16s63_9e
    with dissolve

    cl "It's easy, you goofball. Just open the packet and spread it on our faces."

    scene v16s63_6d
    with dissolve

    au "*Laughs*"

    scene v16s63_9a
    with dissolve

    cl "What?"

    scene v16s63_7d # FPP Same angle as 7, Nora (smiling, mouth open) looking toward Chloe
    with dissolve

    no "No matter how you say it, it just sounds so dirty."

    scene v16s63_10a # FPP Same angle as 10, Lindsey (smiling, eyes closed, mouth open) with her hands in front of her face, miming spreading something on it
    with dissolve

    li "Yeah, [name]... *Fake moaning* Just spread it all over our faces. *Laughs*"

    scene v16s63_10b # FPP Same angle as 10, Lindsey (smiling, mouth closed) winking at MC
    with dissolve

    u "(*Gulps*)"

    scene v16s63_9f # FPP Same angle as 9, Chloe (rolling her eyes, mouth open) not looking at anyone
    with dissolve

    cl "*Sighs*"

    # -Some shots of MC opening the facemasks and spreading them on the face of each girl 
    # (It's a gentle green/blue color (or whatever we can get) They are gel masks that are spread on, avoiding eyes and lips, and after 15 minutes, they are peeled off)-
    # IN THE FOLLOWING SHOTS, IF GIRLS WHO ALREADY GOT A MASK ARE VISIBLE WHEN MC IS APPLYING IT TO ANOTHER, MAKE SURE THE MASK IS ON
    # HAVE FUN WITH THESE SHOTS. FEEL FREE TO MAKE THE GIRLS' EXPRESSION OR ACTIONS FUN, TO MATCH HER PERSONALITY

    scene v16s63_15 # TPP Show MC opening facemasks
    with dissolve

    pause 0.75

    scene v16s63_16 # TPP Show MC applying facemask to Jenny
    with dissolve

    pause 0.75

    scene v16s63_17 # TPP Show MC applying facemask to Chloe
    with dissolve

    pause 0.75

    scene v16s63_18 # TPP Show MC applying facemask to Aubrey
    with dissolve

    pause 0.75

    scene v16s63_19 # TPP Show MC applying facemask to Nora
    with dissolve

    pause 0.75

    scene v16s63_20 # TPP Show MC applying facemask to Lindsey
    with dissolve

    pause 0.75

    scene v16s63_5d # FPP Same angle as 5. All of the girls are sitting back, relaxing with the facemasks on
    with dissolve

    u "Okay, so, fifteen minutes and they're ready to take off?"

    scene v16s63_9g # FPP Same angle as 9, Chloe (facemask on, eyes closed, mouth open) leaning back, relaxing
    with dissolve

    cl "Yeah, that's right."

    scene v16s63_21 # TPP Show MC sitting down, his phone is out to keep track of, and kill, time
    with dissolve

    pause 0.75

    # -if MC bought the Expensive facemasks in Scene 35, or is not helping Chloe and was invited to help
    if "expensive_mask" in v16s63x_chloe_suggestion_set or not v14_help_chloe:

        scene v16s63_8f # FPP Same angle as 8, Jenny (facemask on, eyes closed, mouth open) leaning back, relaxing
        with dissolve

        jen "Mmm, they smell really nice..."

        scene v16s63_6f # FPP Same angle as 6, Aubrey (facemask on, eyes closed, mouth open) leaning back, relaxing
        with dissolve

        au "*Sniffs* Almost good enough to eat, haha."

        scene v16s63_10c # FPP Same angle as 10, Lindsey (facemask on, eyes closed, mouth open) leaning back, relaxing
        with dissolve

        li "I wouldn't go that far. *Giggles*"

        scene v16s63_6f
        with dissolve

        au "It's mainly cucumbers. Probably edible for the most part."

        scene v16s63_7e # FPP Same angle as 7, Nora (facemask on, eyes closed, mouth open) leaning back, relaxing
        with dissolve

        no "It does smell delicious..."

        scene v16s63_9g
        with dissolve

        cl "I think there's kiwi fruit and some avocado in some of them too."

        scene v16s63_6f
        with dissolve

        au "See? Perfectly edible!"

        scene v16s63_7e
        with dissolve

        no "Haha, Aubrey's going to be spreading it on her toast in the morning."

    else: # -if MC bought the Cheap facemasks in Scene 35
    
        $ set_presidency_percent(v14_lindsey_popularity + 2) # -LindseyPopularity +2

        scene v16s63_10c
        with dissolve

        li "They smell a bit..."

        scene v16s63_7e
        with dissolve

        no "Synthetic?"

        scene v16s63_6f
        with dissolve

        au "Yeah, like it's full of chemicals."

        scene v16s63_8f
        with dissolve

        jen "They're normally really fragrant, but I can't smell any fruit at all in these."

        scene v16s63_9g
        with dissolve

        cl "Is anyone else's face feeling a little...?"

        scene v16s63_9h # FPP Same angle as 9, Chloe (facemask on, eyes closed, mouth open) sitting up, hands up, feeling the facemask
        with dissolve

        cl "A little like..."

        scene v16s63_9i # FPP Same angle as 9, Chloe (facemask on, eyes open, mouth open) sitting straight up, she looks alarmed
        with dissolve

        cl "Burning?"

        scene v16s63_7e
        with dissolve

        no "Burning?! No, I'm fine."

        scene v16s63_10c
        with dissolve

        li "Is yours burning, Chloe?"

        scene v16s63_9i
        with dissolve

        cl "It fucking feels like it!"

        scene v16s63_22 # FPP Chloe (facemask on, mouth open) standing up, hands to her face, she looks alarmed
        with dissolve

        cl "And it's getting worse! Ow, shit!"

        scene v16s63_23 # FPP Show Chloe (facemask on, mouth open, if visible) running out of the room
        with dissolve

        cl "I'm taking it off, it hurts like hell!"

        scene v16s63_8g # FPP Same angle as 8, Jenny (facemask on, eyes open, mouth open) looking toward the door to the room
        with dissolve

        jen "Hurry before you get a chemical burn!"

        scene v16s63_24 # FPP Show Lindsay (facemask on, mouth open) standing up and walking toward the door to the room
        with dissolve

        li "Well, shit... I'm not going to take my chances."

        scene v16s63_25 # FPP Show Nora (facemask on, mouth open) standing up and feeling the facemask
        with dissolve

        no "Yeah, me neither. I'm getting this shit off."

        scene v16s63_8g
        with dissolve

        jen "Same, I don't want any burns!"

        scene v16s63_26 # FPP Show Lindsey, Nora, and Jenny walking out of the room
        with dissolve

        u "(Fuck,I should've picked up the expensive ones. I guess you get what you pay for...)"

        scene v16s63_6g # FPP Same angle as 6, Aubrey (facemask on, eyes closed, mouth closed) leaning back, relaxing
        with dissolve

        u "Aren't you going to wash yours off too?"

        scene v16s63_6f
        with dissolve

        au "No, it feels fine to me. They're overreacting, haha."

        scene v16s63_6g
        with dissolve

        u "You're so hardcore... *Laughs*"

        scene v16s63_6f
        with dissolve

        au "Haha, always have been, always will be."

    # -Regardless of which facemasks MC bought-

    scene v16s63_27 # TPP Show all of the girls back where they were sitting. Everyone has their facemask off except for Aubrey. MC is approaching her, mouth open
    with fade

    u "You ready to take yours off, Aubrey?"

    scene v16s63_6h # FPP Same angle as 6, Aubrey (facemask on, eyes open, mouth open) sitting up, looking at where facemasks are sitting
    with dissolve

    au "Yeah, but... I see there's a spare one. Why don't you give it a go?"

    scene v16s63_28 # FPP View of facemasks sitting on the table
    with dissolve

    menu:
        "Apply mask":
            $ v16s63_mc_wear_facial_mask = True

            u "Okay, why not?"

            scene v16s63_9e
            with dissolve

            cl "Because it made my skin feel like fire?! Why would you?"

            scene v16s63_6h
            with dissolve

            au "Oh, come on... I'm fine. You'll be fine."

            # -MC sits. A few shots of Aubrey applying his facemask. Then, with it applied, the girls looking at him, all smiling. 
            # MC sitting back, relaxing. The mask stays on until the end of the scene, mc cleans it off before he does the massages/when this scene ends
            
            scene v16s63_29 # TPP Show Aubrey (slight smile, mouth open)  applying facemask to MC
            with dissolve

            au "How does it feel?"

            scene v16s63_29a # TPP Same angle as 29, Aubrey (slight smile, mouth closed) applying facemask to MC (eyes closed, mouth open)
            with dissolve

            u "Healthier, I guess?"

            scene v16s63_29
            with dissolve

            au "Now I can say I've given you a facial, too. *Laughs*"

            scene v16s63_9a
            with dissolve

            cl "Ugh, Aubrey..."

        "Don't mask":
            scene v16s63_28
            #with dissolve
        
            u "No, I'm okay. Not a huge fan of chemical burns myself."

            scene v16s63_6h
            with dissolve

            au "Ha, fine! More for me."

    scene v16s63_9a
    with dissolve

    cl "I think it's about time we moved on to the massages."

    scene v16s63_6b
    with dissolve

    au "Oooh! That's a great idea. Why don't I go first? *Chuckles*"

    scene v16s63_9a
    with dissolve

    cl "Haha, okay. Off you go then."

    scene v16s63_7a
    with dissolve

    no "Aw, what? I wanted to go first."

    scene v16s63_6b
    with dissolve

    au "You snooze, you lose..."

    scene v16s63_7b
    with dissolve

    no "I'll go second then."

    scene v16s63_10
    with dissolve

    li "Third!"

    scene v16s63_8
    with dissolve

    jen "I'm happy just sitting here drinking with Chloe. I don't need any pampering."

    scene v16s63_9
    with dissolve

    cl "Aw, you're too cute, Jen."

    scene v16s63_30 # FPP Show Chloe and Jenny smiling at each other
    with dissolve

    pause 0.75

    scene v16s63_6b
    with dissolve

    au "Have fun, girls! Next time you see me I'll be a whole new woman."

    scene v16s63_31 # FPP Show Aubrey (slight smile, mouth closed) standing, looking back at the girls
    with dissolve

    pause 0.75

    if v16s12_chloe_planboard_decide_mc_gives_massages or v16s61_chloe_pb_override_mc_gives_massages: # -if MC is masseuse

        scene v16s63_32 # FPP View of all the girls, Aubrey standing, all with slight smiles, looking at MC
        with dissolve

        u "Try to behave yourselves while I'm gone, ladies."

        scene v16s63_8d
        with dissolve

        jen "Haha, we're making no promises."

        if v16s63_mc_wear_facial_mask: # -if applied a mask

            scene v16s63_33 # TPP Show MC (in facemask, mouth closed) feeling the facemask
            with dissolve

            u "(Should probably take this mask off first... Yeah, let's do that.)"

        scene v16s63_34 # TPP Show MC following Aubrey out of the room
        with dissolve

        pause 0.75

        jump v16s63a # -Transition to Scene 63a-

    else: # -if MC is not masseuse-
        
        if v16s63_mc_wear_facial_mask: # -if applied a mask

            scene v16s63_33a # TPP Same angle as 33. MC (in facemask, mouth open) feeling the facemask
            with dissolve

            u "I'm gonna take this mask off, be right back."

        jump v16s63b # -Transition to Scene 63b-