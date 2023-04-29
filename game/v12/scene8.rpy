# SCENE 8: Murder Mystery reveal
# Locations: Ferry
# Characters: MR. LEE (Outfit: 1) LINDSEY (Outfit: 1) CHARLI (Outfit: 1) RILEY (Outfit: 3) IMRE (Outfit: 2) MS. ROSE (Outfit: 1) MC (Outfit: 1) NORA (Outfit: 1) CHRIS (Outfit: 2)
# Time: Evening
# Phone Images: None

label v12_murder_mystery_reveal:
    hide screen murder_button_overlay

    scene v12mmr1 # FPP. Mr. Lee and Ms. Rose standing in front of the students, addressing them, only Mr. Lee in shot. Mr. Lee smiling, mouth open, looking at MC
    with dissolve

    if (joinwolves and len(v12s7_killList) == 15) or len(v12s7_killList) == 16:
        $ grant_achievement("mass_casualties")

    lee "Wow, that turned out a lot better than expected. I hope you all enjoyed yourselves. Was anyone surprised to learn [name] was my chosen murderer?"

    play music "music/v12/Track Scene 8.mp3" fadein 2

    scene v12mmr2 # FPP. Same positioning as v12mmr1, MC looking at Lindsey, Lindsey looking at Mr. Lee's direction, Lindsey smiling, mouth open
    with dissolve

    li "I was pretty surprised."

    scene v12mmr3 # FPP. Same positioning as v12mmr1, MC looking at Charli, Charli looking at Mr. Lee's direction, Charli slightly annoyed, mouth open
    with dissolve

    charli "I wasn't surprised at all."

    scene v12mmr1
    with dissolve

    lee "You may have noticed that the roles I chose for you all fit each of you in a significant way."

    scene v12mmr4 # FPP. Same positioning as v12mm1, MC looking at Riley, Riley looking at Mr. Lee's direction, Riley slight smile, mouth open
    with dissolve

    ri "You made me a rich woman. *Chuckles* How was that significant?"

    scene v12mmr1a # FPP. Same as v12mmr1, Mr. Lee looking at Riley's direction, Mr. Lee slight smile, mouth open
    with dissolve

    lee "How did it feel being a snotty rich woman?"

    scene v12mmr4a # FPP. Same as v12mmr4, Riley slightly sad, mouth open
    with dissolve

    ri "Uncomfortable, different, I don't know."

    scene v12mmr1a
    with dissolve

    lee "Spot on! Some of you got to experience being out of your comfort zone, others got to dig deep into how they normally behave, and then I threw in complete curveballs that I personally found quite amusing."

    scene v12mmr5 # FPP. Same positioning as v12mmr1, MC looking at Imre, Imre looking at Mr. Lee's direction, Imre slightly annoyed, mouth open
    with dissolve

    imre "Don't worry, soon I'm gonna do something for you that I find amusing."

    scene v12mmr1b # FPP. Same as v12mmr1, Mr. Lee looking at Imre's direction, Mr. Lee slight smirk, mouth open
    with dissolve

    lee "Good luck surprising me."

    scene v12mmr5
    with dissolve

    imre "Challenge accepted."

    scene v12mmr1
    with dissolve

    $ v12_murder_count = len(v12s7_killList)
    if len(v12s7_killList) >= 5:
    
        $ grant_achievement("killing_spree")

        lee "A total of [v12_murder_count] people were killed, so let's give our murderer a round of applause."

        scene v12mmr99 # TPP. Same positioning as v12mmr1, Show Riley, Lindsey and Imre applauding MC, all smiling, mouths closed
        with dissolve

        pause 0.75

        scene v12mmr6 # FPP. Same positioning as v12mmr1, MC looking at Ms. Rose, Ms. Rose looking at MC, Ms. Rose smiling, mouth open
        with dissolve

        ro "That's the only time we'll ever condone killing. *Chuckles*"

        scene v12mmr6a # FPP. Same as v12mmr6, Ms. Rose mouth closed, smiling
        with dissolve

        u "*Chuckles*"

        scene v12mmr1
        with dissolve

        lee "You were very stealthy out there and it was interesting to watch."

        scene v12mmr1c # FPP. Same as v12mmr1, Mr. Lee mouth closed, smiling
        with dissolve

        u "I'm a mastermind."

        scene v12mmr3a # FPP. Same as v12mmr3, Charli looking at MC, Charli annoyed, mouth open
        with dissolve

        charli "Never would've guessed you were so good at manipulation."

        scene v12mmr1d # FPP. Same as v12mmr1, Mr. Lee looking at Charli's direction, Mr. Lee smiling, mouth open
        with dissolve

        lee "You don't have to be good at manipulation if your target is naive or biased."

    else: # Killed less than 5 students

        lee "Well, our murderer got caught pretty fast. I was surprised how easily you got found out. The singling out strategy would've worked perfectly."

        scene v12mmr1c
        with dissolve

        u "My bad, I'm not a skilled killer."

        scene v12mmr1
        with dissolve

        lee "Haha, if you were, I'd be worried."

        scene v12mmr3a
        with dissolve

        charli "Can't be skilled at every bad guy thing."

    scene v12mmr5a # FPP. Same as v12mmr5, Imre looking at MC, Imre mouth open, neutral expression
    with dissolve

    imre "WAIT WAIT WAIT BRO! I just processed this, you let me walk around like that, you could've shut the game down from the jump."

    scene v12mmr1b
    with dissolve

    lee "Not intentionally, or else he would've been swimming."

    scene v12mmr5
    with dissolve

    imre "Well the game's over now so we're not worried about that."

    scene v12mmr1b
    with dissolve

    lee "There's still quite some time before we arrive, and I've tested the life jackets... they're working just fine."

    scene v12mmr5
    with dissolve

    imre "I'll be quiet."

    scene v12mmr1
    with dissolve

    lee "*Chuckles* Again, I hope everyone enjoyed themselves. Please try and relax before-"

    scene v12mmr7 # FPP. Same positioning as v12mmr1, MC looking at Nora, Nora looking at MC, her hand is on her stomach, she's about to vomit, mouth open (Nora is kind of far away)
    with dissolve

    no "Oh no."

    scene v12mmr7a # FPP. Same as v12mmr7, Nora mouth closed, same pose
    with dissolve

    u "What's wrong?"

    scene v12mmr7
    with dissolve

    no "Oof, my stomach is feeling really weird and I'm getting dizzy."

    scene v12mmr8 # FPP. Same positioning as v12mmr1, MC looking at Chris walking over to Nora, Chris worried, mouth closed
    with dissolve

    menu:
        "Let Chris help her":
            $ v12_help_chris += 1
            $ reputation.add_point(RepComponent.BRO)

            u "(It's his girl, he's got her.)"

            scene v12mmr7b # FPP. Same cam as v12mmr7, Chris and Nora looking at each other, Nora feeling sick, mouth closed, Chris worried, mouth open
            with dissolve

            ch "You need some water or something?"

            scene v12mmr7c # FPP. Same as v12mmr7b, Chris mouth closed, worried, Nora feeling sick, mouth open
            with dissolve

            no "Yes please, thank you."

            scene v12mmr7b
            with dissolve

            ch "No problem baby, I'll be right back."

            scene v12mmr8a # FPP. Same as v12mmr8, but show Chris walking the other direction, mouth closed, worried
            with dissolve

            pause 0.75

        "Hurry to help her":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            $ v8_nora_likes_mc = True
            
            scene v12mmr9 # TPP. Show MC rushing to Nora, MC worried, mouth closed, Nora feeling sick, mouth closed
            with dissolve
            
            pause 0.75

            scene v12mmr10 # FPP. MC and Nora standing next to each other, Nora feeling sick, mouth closed, show MC holding Nora up
            with dissolve

            u "You okay? Need some water or something?"

            scene v12mmr10a # FPP. Same as v12mmr10, Nora mouth open, feeling sick
            with dissolve

            no "I don't know, I feel weird all of a sudden. If you weren't holding me I don't know if I could stand."

            scene v12mmr10
            with dissolve

            u "Well don't worry I got you."

            pause 0.75

    scene v12mmr7
    with dissolve

    no "*Burp* Oh goodness."

    scene v12mmr7d # FPP. Show Nora running to the side of the ship, hand over her mouth
    with dissolve

    pause 0.75

    scene v12mmr11 # FPP. MC looks as Nora is throwing up over the edge of the ship
    with dissolve

    u "(Oh fuck.)"

    scene v12mmr1
    with dissolve

    lee "Casual sea sickness, the pleasures of the ferry. Enjoy the trip, students."

    scene v12mmr9b # FPP. Show MC running over to the edge of the ship where Nora is in v12mmr11, MC worried, mouth closed
    with dissolve

    pause 0.75

    scene v12mmr12 # FPP. MC and Nora standing next to each other at the edge of the ship (check v12mmr11), MC and Nora looking at each other, Nora holding her stomach, slightly sad expression, mouth closed
    with dissolve

    u "Are you okay?"

    scene v12mmr12a # FPP. Same as v12mmr12, Nora mouth closed, slightly sad
    with dissolve

    no "Honestly, I feel a lot better now. I'm gonna go sit down."

    scene v12mmr12
    with dissolve

    u "That's probably best."

    scene v12mmr12b # FPP. Same cam as v12mmr12, MC watches as Nora is walking out of frame, Nora still holding her stomach, mouth closed
    with dissolve

    u "(Let's wait out this long ass ride.)"

    scene v12mmr13 # TPP. Show MC walking towards a seat, mouth closed, bored expression
    with dissolve

    pause 0.75

    image ferry_arrival = Movie(play="images/v12/Scene 7/animations/Ferry B - To France.webm", loop=False)
    
    scene ferry_arrival
    with fade
    play sound "images/v12/Scene 7/animations/Track Scene - Ferry Ride (5 sec).mp3"

    pause 3.5

    scene v12mmr15 # TPP. Show MC sitting down, sleeping, mouth closed
    with fade

    pause 0.75

    scene v12mmr15a # TPP. Same as v12mmr15, Show MC waking up startled while sitting down, mouth closed
    with vpunch

    u "(Woah... we must be here.)"

    scene v12mmr14
    with dissolve

    pause 0.75

    scene v12mmr16 # TPP. Show MC walking towards the exit of the boat, neutral expression, mouth closed
    with dissolve

    pause 0.75

    scene v12mmr17 # TPP. Show MC going through the boat's exit, mouth closed, neutral expression
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v12_dock_arrival #scene 9