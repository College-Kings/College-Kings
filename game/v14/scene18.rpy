# SCENE 18: Lindsey Ask For Help
# Locations: Classroom, College Hallway
# Characters: MC (Outfit: 9), LINDSEY (Outfit: 1)
# Time: Morning

label v14s18:
    play music "music/v11/Track Scene 16.mp3" fadein 2

    scene v14s18_1 # TPP. Show MC leaving the classroom, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v14s18_2 # FPP. MC standing in hallway, looking at Lindsey, Lindsey putting up a flyer on the wall, she has a pack of flyers in her other hand, Lindsey slight smile, mouth closed (MC is kind of far from Lindsey)
    with dissolve

    pause 0.75

    scene v14s18_3 # TPP. Show MC walking up to Lindsey, both slight smiles, mouths closed
    with dissolve

    pause 0.75

    scene v14s18_4 # FPP. MC standing in front of Lindsey, Lindsey looking at MC, Lindsey slight smile, mouth closed (Don't show the stack of flyers)
    with dissolve

    u "You don't have enough of those up already?"

    scene v14s18_4a # FPP. Same as v14s18_4, Lindsey mouth open
    with dissolve

    li "The more the merrier! Also, it's good you're here. Hold these?"

    scene v14s18_5 # TPP. Show Lindsey giving the stack of flyers to MC, both slight smiles, mouths closed
    with dissolve

    pause 0.75

    scene v14s18_4
    with dissolve

    u "Oh, sure..."

    scene v14s18_4a
    with dissolve

    li "The support for my campaign is beginning to really build up, so I'm trying to do last minute things. Anything to help in the end, you know?"

    scene v14s18_4b # FPP. Same as v14s18_4, Lindsey different pose
    with dissolve

    u "Seems like you have all the help you need... I don't see much of Chloe anywhere. *Chuckles*"

    scene v14s18_4c # FPP. Same as v14s18_4b, Lindsey mouth open
    with dissolve

    li "The race isn't won 'til the votes are counted, [name]! So until then, I'll be taking all the help I can get."

    scene v14s18_4
    with dissolve

    u "Ha, alright... Just don't work yourself too hard."

    scene v14s18_4a
    with dissolve

    li "I'll most likely be putting in extra work every day, haha. I have to make sure I've done everything I possibly can."

    scene v14s18_4b
    with dissolve

    u "You need to get a dream team to help you out, people you can trust."

    scene v14s18_4a
    with dissolve

    li "I could really use the help."

    scene v14s18_4c
    with dissolve

    li "I still have a shit ton of campaign planning to do and I can't exactly let just anyone in on that..."

    scene v14s18_4b
    with dissolve

    u "I get that."

    scene v14s18_4c
    with dissolve

    li "I mean, I know I've already asked you before, but..."

    scene v14s18_4a
    with dissolve

    li "Are you willing to help me?"

    scene v14s18_4
    with dissolve

    u "I-"

    scene v14s18_4a
    with dissolve

    li "Okay, wait... Before you answer, let me just say this."

    scene v14s18_4d # FPP. Same as v14s18_4a, Lindsey slightly worried, looking down, mouth open
    with dissolve

    li "Honestly, [name]... I need you, ha. I need your help."

    scene v14s18_4e # FPP. Same as v14s18_4d, Lindsey looking at MC now
    with dissolve

    li "I'm worried that without your help, I'll have a little if no chance of winning."

    scene v14s18_4i
    with dissolve

    u "You can win regardless of having me on your team, Linds. You have a really good chance, actually."

    scene v14s18_4d
    with dissolve

    li "We're friends... Right?"

    if "v12_lindsey" in sceneList and lindsey.relationship < Relationship.FWB: #to ensure compatibility flow with v12s17
        $ lindsey.relationship = Relationship.FWB

    if lindsey.relationship >= Relationship.FWB:
        scene v14s18_4a
        with dissolve

        li "Maybe even more than that?"

        scene v14s18_4d
        with dissolve
        
        li "Nevermind, that doesn't matter."

    if chloe.relationship >= Relationship.GIRLFRIEND:
        scene v14s18_4a
        with dissolve

        li "I know you're like... Dating her, or whatever you're calling it... *Chuckles*"

    scene v14s18_4c
    with dissolve

    li "I genuinely think that my only chance at beating Chloe starts with you joining my team."

    if lindsey.relationship >= Relationship.FWB:
        scene v14s18_4f # FPP. Lindsey very close to MC, she is whispering, mouth open, seductive smile
        with dissolve

        li "*Whispers* Maybe if we win you can have your way with the new President..."

        scene v14s18_4g # FPP. Same as v14s18_4f, Lindsey mouth closed
        with dissolve

        u "*Chuckles* That's an enticing proposal."

        scene v14s18_4f
        with dissolve

        li "*Laughs* I had a dream the other night, actually..."

        li "I was in the bathroom and I..."

        scene v14s18_4a
        with dissolve

        li "Ah, nevermind. You can find out the rest later."

        if not v13_threesomeending:
            scene v14s18_4
            with dissolve

            u "(A dream? In the bathroom...? Did we have the same dream?!)"

    scene v14s18_4c
    with dissolve

    li "So... what do you say, will you help me win this thing?"

    scene v14s18_4b
    with dissolve

    menu:
        "Help Lindsey":
            $ set_presidency_percent(v14_lindsey_popularity + 5)
            if chloe.relationship >= Relationship.GIRLFRIEND:
                $ add_point(KCT.TROUBLEMAKER)
            elif lindsey.relationship >= Relationship.FWB:
                $ add_point(KCT.BOYFRIEND)
            else:
                $ add_point(KCT.BRO)
            $ v14_help_lindsey = True

            if v14_help_chloe:
                $ grant_achievement("double_agent")
  
            u "From the very beginning I've been in support of your campaign, and I don't plan on stopping anytime soon."

            scene v14s18_6 # TPP. Show Lindsey hugging MC tightly, MC smiling, mouth closed, Lindsey smiling, mouth open
            with dissolve

            li "That's exactly what I expected..."

            if lindsey.relationship >= Relationship.FWB:
                scene v14s18_4h # FPP. Same as v14s18_4, show Lindsey looking around
                with dissolve

                pause 0.75

                play sound "sounds/kiss.mp3"

                scene v14s18_7 # TPP. Show Lindsey giving MC a kiss on the cheek
                with dissolve

                pause 1.5

            scene v14s18_4a
            with dissolve

            li "Well then, partner... Meet me at dawn in the janitor's closet, aka my presidential headquarters. *Chuckles*"

            scene v14s18_4
            with dissolve

            u "Haha, okay. Will do, boss lady."

            scene v14s18_5a # TPP. Same as v14s18_5, but MC is giving her the flyer back
            with dissolve

            if v14_help_chloe:
                u "(I have to make sure they don't find out I'm helping both of them... That might end badly.)"

            else:
                pause 0.75

        "Don't help Lindsey":
            if chloe.relationship >= Relationship.GIRLFRIEND:
                $ add_point(KCT.BOYFRIEND)
            elif lindsey.relationship >= Relationship.FWB:
                $ add_point(KCT.TROUBLEMAKER)
                
            scene v14s18_4i # FPP. Same as v14s18_4, Lindsey sad
            with dissolve

            u "I've been thinking about it, and now that we're actually back on campus I'm finally starting to get back into the swing of things. So, I don't think-"

            scene v14s18_4j # FPP. Same as v14s18_4i, Lindsey mouth open
            with dissolve

            li "I really don't need you to run through the list of reasons why you can't help me, ha."

            li "Honestly, I'm pretty shocked about it... But, I'm not gonna let it ruin my day."

            scene v14s18_4i
            with dissolve

            u "I'm sorry, but-"

            scene v14s18_4j
            with dissolve

            li "It's fine."

            scene v14s18_5b # TPP. Same as v14s18_5a, but Lindsey sad, MC slightly worried
            with dissolve

            pause 0.75

    scene v14s18_8 # FPP. Lindsey walking away, with her back turned to MC, holding her flyers (don't show her face)
    with dissolve

    pause 0.75

    if v14_help_chloe:
        
        scene v14s18_9 # TPP. Show MC standing in hallway, slight smile, mouth open
        with dissolve

        u "(Well, oddly enough, it's time to go help Chloe.)"

        scene v14s18_10 # TPP. Show MC leaving the college, going outside, slight smile, mouth closed
        with fade

        pause 0.75

        stop music fadeout 3
        jump v14s19 

    else:
        scene v14s18_11 # TPP. Show MC walking in the hallway
        with fade

        pause 0.75

        stop music fadeout 3
        jump v14s20