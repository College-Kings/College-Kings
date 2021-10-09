# SCENE 30: Photoshoot with Chloe PLUSH WOLF
# Locations: Wolves House
# Characters: CHLOE (Outfit: 1), MC (Outfit: 2), IMRE (Outfit: 1)
# Time: Afternoon

label v14s30:
    scene v14s30_1 # TPP. Show MC walking towards the steps of the Wolves House.
    with fade

    pause .25
    
    play sound "sounds/dooropen.mp3"

    pause .25

    play sound "sounds/doorclose.mp3"

    pause .25

    scene v14s30_2 # FPP. MC inside wolves house Chloe walking up to MC, slight smile, mouth closed
    with dissolve

    pause .25

    scene v14s30_2a # FPP. Same as v14s30_2, Chloe standing infront of MC, slight smile, mouth open.
    with dissolve

    cl "[Name], there you are!"

    scene v14s30_2b # FPP. Same as v14s30_2a, Chloe slight smile, mouth closed.
    with dissolve

    u "Hey, how's it going?"

    scene v14s30_2a
    with dissolve

    cl "Not very good."

    scene v14s30_2b
    with dissolve

    u "Why not?"

    scene v14s30_2a
    with dissolve

    cl "Since the Wolves couldn't help much with the cost of our shoot, I had to go ahead and pay for everything."

    cl "So the campaign fund took a little bit of a hit."

    scene v14s30_2b
    with dissolve

    u "Okay... How bad are we talking?"

    scene v14s30_2a
    with dissolve

    cl "Remember planning things out and thinking about the cost of our two options?"

    scene v14s30_2b
    with dissolve

    u "I remember, yes."

    scene v14s30_2a
    with dissolve

    cl "Well, since it's not the real wolf it's cheaper, that’s true."

    cl "Obviously it's a toy, but Chris said it had to be a specific one and that specific one was super expensive."

    scene v14s30_2b
    with dissolve

    u "Damn… So, we’re broke now or what?"

    scene v14s30_2a
    with dissolve

    cl "Not broke, still less than the real wolf would have been, but…"

    cl "I had to get in an auction for it and since I had no choice but to walk away with it, I had to have the highest bid."

    if v14_pw_half_chris_support:

        cl "Chris helped a bit though, so that was nice."

    scene v14s30_2b
    with dissolve

    u "This better be a nice ass toy…"

    scene v14s30_2a
    with dissolve

    cl "Haha, it is pretty nice!"

    scene v14s30_2b
    with dissolve

    u "Who's all in the picture?"

    scene v14s30_2a
    with dissolve

    if joinwolves:

        cl "Me and you."

        scene v14s30_2b
        with dissolve

        u "That's what I thought. *Chuckles*"

        scene v14s30_2a
        with dissolve

    if joinapes:

        cl "Imre and I."

        scene v14s30_2b
        with dissolve

        u "I knew it. *Chuckles*"

        scene v14s30_2a
        with dissolve

        cl "*Chuckles*"

    cl "Imre is the only one who was free to help."

    scene v14s30_2b
    with dissolve

    u "Take what you can get, I guess."

    scene v14s30_2a
    with dissolve

    cl "As long as they are supporting me I'm happy."

    scene v14s30_2b
    with dissolve

    u "Can’t go wrong with that."

    if joinapes:
        scene v14s30_2a
        with dissolve

        cl "Too bad you aren't a Wolf, then you could just be in the photos with me. *Laughs*"

        scene v14s30_2b
        with dissolve

        u "True. I'm surprised they even let me in here, actually."

        scene v14s30_2a
        with dissolve

        cl "Honestly, they probably haven't even noticed."

        scene v14s30_2c # FPP. Same as v14s30_2b, Imre behind Chloe walking up to MC and Chloe, Imre slight smile, mouth closed.
        with dissolve

        pause .25

        scene v14s30_3 # FPP. Imre standing with MC and Chloe, Chloe looking at Imre, MC looking at Imre, Imre looking at MC, neutral expression, mouth open.

        imre "No, no, no… You may be cool, but you're not a Wolf, Wolf prospect, or a fine ass girl. You gotta go, [name]."

        scene v14s30_3a # FPP. Same as v14s30_3, Imre neutral expression, mouth closed.
        with dissolve

        u "That didn't last long. *Chuckles*"

        scene v14s30_2d # FPP. Same as v14s30_2c, Imre off to the side of Chloe, MC looking at Chloe, Chloe looking at MC, Chloe slight smile, mouth open.
        with dissolve

        cl "Sorry [name]."

        scene v14s30_2e # FPP. Same as v14s30_2d, Chloe slight smile, mouth closed.
        with dissolve

        u "It's fine, I get it , *Chuckles* I'll sit outside."

        u "Come show me the pictures when you're done?"

        scene v14s30_2d
        with dissolve

        cl "I will. Thanks again."

        scene v14s30_2e
        with dissolve

        u "Of course."

        scene v14s30_4 # TPP. Show MC walking away from Chloe and Imre
        with dissolve

        pause .25

        play sound "sounds/dooropen.mp3"

        pause .25

        play sound "sounds/doorclose.mp3"

        pause .25

        scene v14s30_5 # TPP. Show MC sitting alone on the Wolves porch, neutral expression, mouth closed.
        with dissolve

        pause .5

        scene v14s30_5a # TPP. Same as v14s30_5, MC with his head in his hands bored while waiting, neutral expression, mouth closed.
        with fade

        pause .25

        play sound "sounds/dooropen.mp3"

        pause .25

        play sound "sound/doorclose.mp3"

        scene v14s30_5b # TPP. Show Chloe walking towards MC after leaving the Wolves house.
        with dissolve

        pause .25

        scene v14s30_6 # FPP. Chloe and MC sitting on the Wolves porch, Chloe looking at MC, MC looking at Chloe, Chloe slight smile, mouth closed.
        with dissolve

        u "Hey, hey."

        scene v14s30_6
        with dissolve

        jump v14s30b

    if joinwolves
        scene v14s30_2a
        with dissolve

        cl "Let's go ahead and get started before Chris wakes up and takes down all of our props and decorations. *Laughs*"

        scene v14s30_2b
        with dissolve

        u "Roger that."

        scene v14s30_2c
        with dissolve

        pause .25

        scene v14s30_2f # FPP. Same as v14s30_2e, Imre Standing with MC and Chloe, Chloe looking at Imre, MC looking at Chloe, Chloe slight smile, mouth open, Imre slight smile, mouth closed.
        with dissolve

        cl "Hey, Imre!"

        scene v14s30_3b # FPP. Same as v14s30_3a, Imre looking at Chloe, MC looking at Imre, Chloe looking at Imre, Imre slight smile, mouth open, Chloe slight smile, mouth closed.
        with dissolve

        imre "Yeah?"

        scene v14s30_2f
        with dissolve

        cl "Mind showing [name] the setup? I'll be there in a second."

        scene v14s30_3b
        with dissolve

        imre "Sure thing, boss lady! C'mon, man."

        scene v14s30_7 # TPP. Show Imre and MC walking to a different room.
        with dissolve

        pause .25

        scene v14s30_8 # FPP. MC and Imre in room of wolves house with white backdrop and setup for the photoshoot, MC looking at Imre, Imre looking at MC, Imre slight smile, mouth closed.
        with dissolve

        u "So, every other Wolf says no, but you're still down to do the shoot. Why's that?"

        scene v14s30_8a # FPP. Same as v14s30_8, Imre slight smile, mouth open.
        with dissolve

        imre "You and I both know why we’re here, so let's get busy."

        if chloegf:
            scene v14s30_8
            with dissolve

            u "It's kinda strange of you to talk about Chloe like that, when you know she's my girl."

            scene v14s30_8a
            with dissolve

            imre "Your girl is the finest dime at SVC, you and I both know that, yeah? So, take it as a compliment and let's get to work."

        scene v14s30_9 # TPP. Close up of Chloe walking into the room with the Plush Wolf.
        with dissolve

        pause .25

        scene v14s30_10 # FPP. Chloe looking at MC, MC looking at Chloe, Imre looking at Chloe, Chloe standing with MC and Imre, Chloe holding the plush wolf,slight smile, mouth closed.

        u "Damn, that's a pretty sick toy."

        scene v14s30_10a # FPP. Same as v14s30_10, Chloe slight smile, mouth open.
        with dissolve

        cl "Sick and expensive, haha."

        cl "Let's get through these so I can get to the next thing I gotta do."

        scene v14s30_8b # FPP. Same as v14s30_8a, Imre looking at Chloe with the plush wolf standing next to him and MC , Chloe looking at Imre, MC looking at Chloe, Imre slight smile, mouth open.
        with dissolve

        imre "Ma'am, yes ma'am!"

        scene v14s30_10b # FPP. Same as v14s30_10a, Chloe looking at Imre, Imre looking at Chloe, Chloe slight smile, mouth open.
        with dissolve

        cl "You got the camera?"

        scene v14s30_10c # FPP. Same as v14s30_10b, Chloe slight smile, mouth closed.
        with dissolve

        u "Me?"

        scene v14s30_8c # FPP. Same as v14s30_8b, Imre looking at MC, Chloe looking at Imre, Imre slight smile, mouth open.
        with dissolve

        imre "She's not talking to you, bro."

        scene v14s30_8b
        with dissolve

        imre "Of course I got it, Chlo. I'm just gonna use my phone."

        if chloegf:
       
            scene v14s30_8d # FPP. Same as v14s30_8b, Imre slight smile, mouth closed.
            with dissolve

            u "(He’s calling her “Chlo” now…)"

        scene v14s30_10b
        with dissolve

        cl "We need really good pictures, Imre… You can't just use your phone."

        scene v14s30_8b
        with dissolve

        imre "Do you know what kind of phone I’ve got? *Scoffs*"

        imre "My phone is better than most of those “nice cameras” you’re referring to."

        imre "You guys just make sure you’re looking good and happy…"

        imre "One of you has nothing to worry about. *Chuckles*"

        if chloegf:
            scene v14s30_8e # FPP. Same as v14s30_8c, Imre slight smile, mouth closed.
            with dissolve

            u "Really, man?"

            scene v14s30_8c
            with dissolve

            imre "*Laughs* C’mon bro…"
        elif chloers and not chloegf
            scene v14s30_8e
            with dissolve
    
            u "(He’s all over Chloe today, isn’t he? Ha…)"
        elif not chloers or not chloegf:
            scene v14s30_8e
            with dissolve

            u "Wow, thanks man."

        scene v14s30_10a
        with dissolve

        cl "Oh my gosh, okay… *Chuckles*"

        cl "Let's get these pictures taken."

        scene v14s30_11 # TPP. MC and Chloe walking to the photoshoot spot to take photos, Chloe carrying the plush wolf, both slight smile, mouth closed.
        with dissolve

        pause .25

        scene v14s30_12 # TPP. Camera only showing MC and Chloe standing in position for the photoshoot the plush wolf on the ground, Chloe slight smile, mouth open, MC slight smile, mouth closed.
        with dissolve

        cl "Ready?"

        scene v14s30_12a # TPP. Same as v14s30_12, Both slight smile, mouth closed.
        with dissolve

        imre "Ready."

        scene v14s30_12b # TPP. Same as v14s30_12a, MC and Chloe posing tough with the wolf
        with flash

        pause .25

        scene v14s30_12c # TPP. Same as v14s30_12b, Different pose.
        with flash

        pause .25

        scene v14s30_12d # TPP. Same as v14s30_12c, Yet another new pose.
        with flash

        pause .25

        scene v14s30_11a # TPP. Same as v14s30_11, MC and Chloe walking off the photoset, Chloe leaving the wolf behind, both slight smile, mouth closed. 
        with dissolve

        pause .25

        scene v14s30_13 # FPP. Imre standing infront of MC and Chloe, Chloe to the side of MC (Off Camera), Imre looking at MC, slight smile, mouth open.
        with dissolve

        imre "These are actually halfway decent."

        scene v14s30_13a # FPP. Same as v14s30_13, Imre slight smile, mouth closed
        with dissolve

        u "Are you all done with the jokes?"

        scene v14s30_13
        with dissolve

        imre "Not even close."

        scene v14s30_14 # FPP. MC looking at Chloe, Chloe looking at Imre(Imre off camera infront of MC and Chloe), Chloe slight smile, mouth open.
        with dissolve

        cl "*Chuckles* Can you send those to me?"

        scene v14s30_13b # FPP. Imre looking at Chloe(Chloe off camera), Imre slight smile, mouth open.
        with dissolve

        imre "Sure can! Just give me those digits…"

        scene v14s30_14
        with dissolve

        cl "Stop acting like that, haha. You have my number,"

        scene v14s30_13b
        with dissolve

        imre "Yeah, I know. *Chuckles*"

        scene v14s30_14
        with dissolve

        cl "I don't know why you're trying to start something."

        scene v14s30_13b
        with dissolve

        imre "*Laughs* Nah… I'm not trying to start anything."

        scene v14s30_13a
        with dissolve

        u "(Is he trying to rile me up or something? *Chuckles* It's definitely not working.)"

        scene v14s30_13c # FPP. Same as v14s30_13b, Imre looking at his phone, slight smile, mouth open.
        with dissolve

        imre "You get 'em?"

        scene v14s30_14a # FPP. Chloe looking at her phone, slight smile, mouth open.
        with dissolve

        cl "Got 'em. [name], let's go look at these closely and pick a good one."

        scene v14s30_15 # TPP. MC and Chloe walking away from Imre, all slight smile, mouth closed.
        with dissolve

        pause .5

        play sound "sounds/dooropen.mp3"

        pause .25

        play sound "sounds/doorclose.mp3"

        scene .25

        scene v14s30_6
        with fade

        pause .25

        jump v14s30b
