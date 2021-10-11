# SCENE 18: Lindsey Ask For Help
# Locations: Classroom, College Hallway
# Characters: MC (Outfit: 9), LINDSEY (Outfit: 1)
# Time: Morning

default help_Lindsey = False
default help_Chloe = False

label v14s18:
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

    u "You don't have enough of those up already? *Chuckles*"

    scene v14s18_4a # FPP. Same as v14s18_4, Lindsey mouth open
    with dissolve

    li "The more they merrier! Also, it's good you're here, hold these?"

    scene v14s18_5 # TPP. Show Lindsey giving the stack of flyers to MC, both slight smiles, mouths closed
    with dissolve

    pause 0.75

    scene v14s18_4
    with dissolve

    u "Oh, sure..."

    scene v14s18_4a
    with dissolve

    li "The support for my campaign is beginning to ramp up."

    scene v14s18_4b # FPP. Same as v14s18_4, Lindsey different pose
    with dissolve

    u "Seems like you have all the help you need... I don't see much of Chloe anywhere. *Chuckles*"

    scene v14s18_4c # FPP. Same as v14s18_4b, Lindsey mouth open
    with dissolve

    li "The race isn't won 'til the votes are counted, so I'll be taking all the help I can get until then."

    scene v14s18_4a
    with dissolve

    li "And if I can't get any help then I'll just be putting in the extra work every day. To make sure I've done everything I possibly can."

    scene v14s18_4
    with dissolve

    u "You definitely know how to put in some work... Look at these halls!"

    scene v14s18_4a
    with dissolve

    li "Despite what it may seem, I do actually want the help."

    scene v14s18_4c
    with dissolve

    li "I still have a shit ton of campaign planning to do and I can't exactly let just anyone in on that... but I would enjoy your advice."

    scene v14s18_4b
    with dissolve

    u "Lindsey..."

    scene v14s18_4c
    with dissolve

    li "I know I've already asked before, but this my final choice, are you willing to help me with my campaign?"

    scene v14s18_4
    with dissolve

    u "I-"

    scene v14s18_4a
    with dissolve

    li "Wait! Before you answer, let me just say this..."

    scene v14s18_4d # FPP. Same as v14s18_4a, Lindsey slightly worried, looking down, mouth open
    with dissolve

    li "Honestly [Name]... I need you. I need your help."

    scene v14s18_4e # FPP. Same as v14s18_4d, Lindsey looking at MC now
    with dissolve

    li "I'm worried that without your help, I'm a lost cause. I mean, we're friends... Right?"

    if lindseyrs:
        scene v14s18_4a
        with dissolve

        li "Maybe even more than that?"

        scene v14s18_4d
        with dissolve
        
        li "Nevermind, It doesn't matter."

    if chloegf:
        scene v14s18_4a
        with dissolve

        li "I know you're like, dating her, or whatever you're calling it... *Chuckles* But genuinely, my only chance at beating Chloe starts with you joining my team."

    if lindseyrs:
        scene v14s18_4f # FPP. Lindsey very close to MC, she is whispering, mouth open, seductive smile
        with dissolve

        li "*Whispers* Maybe if we win you can have your way with the new president..."

        scene v14s18_4g # FPP. Same as v14s18_4f, Lindsey mouth closed
        with dissolve

        u "*Chuckles* That's an enticing proposal."

        scene v14s18_4f
        with dissolve

        li "*Laughs* I had a dream the other night, actually..."

        scene v14s18_4g
        with dissolve

        li "I was in the bathroom and I was..."

        scene v14s18_4a
        with dissolve

        li "Ah, nevermind. You can find out the rest later. *Chuckles*"

        if not aubreyrs and not rileyrs:
            scene v14s18_4
            with dissolve

            u "(A dream? In the bathroom...? Did we have the same dream?!)"

    scene v14s18_4c
    with dissolve

    li "So... What do you say, will you help me win this thing?"

    scene v14s18_4b
    with dissolve

    menu:
        "Help Lindsey":
            $ help_Lindsey = True
  
            u "From the very beginning I've been in support of your campaign, and I don't plan on stopping anytime soon."

            scene v14s18_6 # TPP. Show Lindsey hugging MC tightly, MC smiling, mouth closed, Lindsey smiling, mouth open
            with dissolve

            li "That's exactly what I expected..."

            if lindseyrs:
                scene v14s18_4h # FPP. Same as v14s18_4, show Lindsey looking around
                with dissolve

                pause 0.75

                play sound "sounds/kiss.mp3"

                scene v14s18_7 # TPP. Show Lindsey giving MC a kiss on the cheek
                with dissolve

                pause

            scene v14s18_4a
            with dissolve

            li "Meet me at dawn in the janitor's closet, aka my presidential headquarters. *Chuckles*"

            scene v14s18_4
            with dissolve

            u "Haha, okay. Will do, boss lady."

            scene v14s18_5a # TPP. Same as v14s18_5, but MC is giving her the flyer back
            with dissolve

            pause 0.75

        "Don't help Lindsey":
            scene v14s18_4i # FPP. Same as v14s18_4, Lindsey sad
            with dissolve

            u "Look, I've been thinking about it and now that we're actually back on campus I'm finally starting to get back into the swing of things. So, I don't think-"

            scene v14s18_4j # FPP. Same as v14s18_4i, Lindsey mouth open
            with dissolve

            li "I really don't need you to run through the list of reasons why you can't help me, ha."

            li "Honestly, I'm majorly surprised that you decided not to... But, I'm not gonna harp on it."

            scene v14s18_4i
            with dissolve

            u "I'm sorry Lindsey, but-"

            scene v14s18_4
            with dissolve

            li "It's fine."

            scene v14s18_5b # TPP. Same as v14s18_5a, but Lindsey sad, MC slightly worried
            with dissolve

            pause 0.75

    scene v14s18_8 # FPP. Lindsey walking away, with her back turned to MC, holding her flyers (don't show her face)
    with dissolve

    pause 0.75

    if help_Chloe:
        scene v14s18_9 # TPP. Show MC standing in hallway, slight smile, mouth open
        with dissolve

        u "Well, oddly enough, it's  time to go help Chloe."

        scene v14s18_10 # TPP. Show MC leaving the college, going outside, slight smile, mouth closed
        with fade

        pause 0.75

        jump v14s19 

    else:
        scene v14s18_11 # TPP. Show MC walking in the hallway
        with fade

        pause 0.75

        jump v14s20