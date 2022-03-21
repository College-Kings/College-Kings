# SCENE 24: Simplr Event
# Locations: Simplr Bar
# Characters: BAR HOST (Outfit: 1), MC (Outfit: 9), IMRE (Outfit: 1), RYAN (Outfit: 1), EMMY (Outfit: 1), KOURTNEY (Outfit: 1), ARYSSA (Outfit: 1)
# Time: Afternoon

label v13s24:
    scene v13s24_1 # TPP. show MC, imre and ryan, walking into Simplr bar up to the barhost standing at a mobile podium, all slight smiles, all mouths closed
    with dissolve

    pause 0.75

    play music "music/v13/Track Scene 24_1.mp3" fadein 2

    scene v13s24_2 # TPP. show imre and ryan standing next to each other on MC's left and barhost on MC's right, imre slight anger mouth open, ryan slight smile mouth closed, barhost slight smile mouth open
    with dissolve

    pause 0.75

    scene v13s24_3 # FPP. show just barhost, slight smile, mouth open
    with dissolve

    barh "Well, well, well... If it isn't the guy who got catfished and his two stalker friends. *Laughs*"

    scene v13s24_3a # FPP. same as v13s24_3, barhost mouth closed
    with dissolve

    u "Haha, what was your name again?"

    scene v13s24_3
    with dissolve

    barh "The host has no name."

    scene v13s24_3a
    with dissolve

    u "(Huh?)"

    scene v13s24_3
    with dissolve

    barh "I'm actually really glad I invited you guys and I'm even more happy that you decided to come."

    scene v13s24_3a
    with dissolve

    u "Why is that?"

    scene v13s24_3
    with dissolve

    barh "Well, you're the only guys that came. *Chuckles*"

    scene v13s24_3
    with dissolve

    barh "There's three other singles, but they're all girls. One for each of you maybe? *Laughs*"

    menu:
        "I already have a girl":
            $ add_point(KCT.BOYFRIEND)

            scene v13s24_3a
            with dissolve

            u "I actually already have a girl... Ha."

            scene v13s24_3
            with dissolve

            barh "Well, guess you won't be having too much fun tonight then."

            scene v13s24_4 # FPP. show just imre slight smile, mouth open
            with dissolve

            imre "Sucks for him! *Laughs*"

            scene v13s24_5 # FPP show just ryan slight smile, mouth open
            with dissolve

            ry "*Laughs*"
  
            scene v13s24_6 # FPP. show ryan and imre looking at eachother, both laughing, both full smiles, both mouths open, barhost mouth closed
            with dissolve

            pause 0.75

            scene v13s24_6a # FPP. ryan and imre realize they're both laughing at imre's joke, look away from each other, stop laughing and get serious/awkward, mouths closed
            with dissolve

            pause 0.75

            scene v13s24_3
            with dissolve

            barh "Awkward..."

        "Fuck yeah, let's mingle":
            $ add_point(KCT.BRO)
            if chloe.relationship >= Relationship.GIRLFRIEND or lauren.relationship >= Relationship.GIRLFRIEND:
                $ add_point(KCT.TROUBLEMAKER)

            scene v13s24_3a
            with dissolve

            u "Fuck yeah, let's mingle boys! *Chuckles*"

            scene v13s24_2a # TPP. same as v13s24_2 imre slight smile mouth closed, barhost mouth closed
            with dissolve

            u "One for all and all for... Well, when you guys are finished it can be all for one. *Chuckles*"

            scene v13s24_3
            with dissolve

            barh "*Laughs* I like this guy!"

    scene v13s24_3
    with dissolve

    barh "So, I've prepared a table for you guys and the ladies are already waiting..."

    scene v13s24_3
    with dissolve

    barh "If you will please take a seat, I'll bring them in one by one."

    scene v13s24_3
    with dissolve

    barh "They'll ask each of you a question or two and then they'll leave."
            
    scene v13s24_4
    with dissolve

    imre "No feedback?! How do I know if they're down to pound?"

    scene v13s24_3
    with dissolve

    barh "*Chuckles* Don't worry, pal."

    scene v13s24_3
    with dissolve

    barh "After the speed dates, depending on your answers, the ladies will give a little report on what they think of you."

    scene v13s24_5
    with dissolve

    ry "Ooooh! *Laughs*"

    scene v13s24_5
    with dissolve

    ry "Sounds all good to me... Let's do this thing, boys."

    scene v13s24_7 # TPP. MC, ryan, and imre walk towards a table, barhost rolls his mobile behind the table, all slight smiles, all mouths closed
    with dissolve

    pause 0.75

    scene v13s24_8 # TPP. MC, ryan, and imre sit down at a square table, with seating for 4 people, ryan sits to right of MC, imre sits to the left of MC, leaving the chair ooposite of MC free, imre and ryan both looking at MC, barhost rolls mobile podium just behind imre's left shouder, everyone has slight smiles and mouths closed
    with dissolve

    pause 0.75

    scene v13s24_9 # FPP. show imre on MC's left and ryan on MC's right, the chair in front of MC is empty, imre and ryan are both looking at MC with slight smiles and mouths closed
    with dissolve

    pause 0.75

    scene v13s24_10 # FPP. MC looks to his left, show just imre, imre looking at MC, slight smile, mouth open
    with dissolve

    imre "Just so you know, you guys are gonna miss out on all the ladies..."

    scene v13s24_11 # FPP. MC looks to his right, show just ryan, ryan looking at MC, slight smile, mouth open
    with dissolve

    ry "*Chuckles* Here we go..."

    scene v13s24_10
    with dissolve

    imre "I'm just saying, with the way I play... It's game over for you boys."

    scene v13s24_10a # FPP. same as v13s24_10 imre mouth closed
    with dissolve

    u "*Laughs* Okay, cornball catfish."

    scene v13s24_10b # FPP. same as v13s24_10a imre slight angry, mouth open
    with dissolve

    imre "Hey! That was one time, and it was definitely not my fault."

    scene v13s24_10c # FPP. same as v13s24_10b imre mouth closed
    with dissolve

    u "What does that change? *Laughs*"

    scene v13s24_11
    with dissolve

    ry "*Chuckles* You guys think the questions will be really deep or just like, surface level?"

    scene v13s24_11a # FPP. same as v13s24_11 ryan mouth closed
    with dissolve

    u "Considering they came to an event like this, the girls are probably gonna take it pretty seriously."

    scene v13s24_11
    with dissolve

    ry "Hmm... We'll see I guess..."

    scene v13s24_11a
    with dissolve

    u "What's wrong? Getting nervous about that new hairdo all of a sudden? *Laughs*"

    scene v13s24_11
    with dissolve

    ry "Maaann... Why would you even say that? I finally stopped thinking about it."

    scene v13s24_10
    with dissolve

    imre "*Laughs* Either way, I'm dicking someone down after this, boys."

    scene v13s24_11b # FPP. same as v13s24_11 ryan looking at imre
    with dissolve

    ry "What the hell are you on about? As soon as they see that cupcake on your boob they'll be long gone. *Laughs*"

    scene v13s24_11a
    with dissolve

    u "Haha! That was pretty fucking good Ryan."

    scene v13s24_11b
    with dissolve

    ry "Imre! The cake is a lie!"

    scene v13s24_10d # FPP. same as v13s24_10b imre looking at ryan
    with dissolve

    imre "Man, you guys are a bunch a d-"

    scene v13s24_12 # FPP. barhost standing at the podium, one hand palm up and open outstretched, half smile, mouth open
    with dissolve

    barh "The first woman is coming in, stand tall gentlemen! For Emmy has arrived!"

    stop music fadeout 3
    play music "music/v13/Track Scene 24_2.mp3" fadein 2

    scene v13s24_13 # FPP. emmy walks in, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v13s24_14 # FPP. emmy pulls chair out to sit down in the free seat opposite of MC, show imre to the MC's left (still sitting,) show ryan to MC's right (still sitting,) both imre and ryan are looking at emmy, all slight smiles, all mouths closed
    with dissolve

    pause 0.75

    scene v13s24_15 # FPP. imre and ryan are still in frame, emmy has sat down, emmy looks at MC, ryan and imre looking at emmy, all slight smiles, all mouths closed
    with dissolve

    pause 0.75

    scene v13s24_16 # FPP. show just emmy looking at mc, slight smile, mouth open
    with dissolve

    emmy "Hello boys! *Chuckles* It's nice to meet you all."

    if emmy.simplr in simplr_app.contacts: #for v12-v13 compatibility
        $ v12s24_emmymatch = True

    if v12s24_emmymatch:
        scene v13s24_17 # FPP. emmy recognizes MC, eyebrow raised, slight smile, mouth closed
        with dissolve

        pause 0.75

        scene v13s24_18 # FPP. show emmy, imre, and ryan, emmy leans towards and whispers to MC, slight smile, mouth closed, show imre looking at emmy's ass, slight smile, mouth closed, and ryan looking at emmy's boobs, slight smile, mouth closed
        with dissolve

        pause 0.75

        scene v13s24_18a # FPP. same as v13s24_18 emmy's'mouth open, show imre looking at emmy's ass, full smile, mouth open, and ryan looking at emmy's boobs, full smile, mouth open
        with dissolve

        pause 0.75

        scene v13s24_18b # FPP. same as v13s24_18a show imre and ryan looking at each other
        with dissolve

        emmy "*Whispers* Is that you [name]?"

        scene v13s24_18c # FPP. same as v13s24_18b show ryan and imre looking away from each other, both mouths closed, both slight frowns
        with dissolve

        u "*Whispers* In the flesh."

        scene v13s24_18d # FPP. same as v13s24_18c ryan and imre now looking at MC, both no expression, imre mouth open, ryan mouth closed
        with dissolve

        imre "Umm, hello?"

        scene v13s24_18e # FPP. same as v13s24_18d emmy mouth open looking back at imre, imre mouth closed looking at emmy, ryan looks at emmy's boobs one last time
        with dissolve

        emmy "Oh! Haha, I'm sorry."

    scene v13s24_11c # FPP. same as v13s24_11 ryan looking at emmy
    with dissolve

    ry "It's nice to meet you too. I'm looking forward to answering your questions."

    scene v13s24_16a # FPP. same as v13s24_16 emmy looking at ryan
    with dissolve

    emmy "How sweet of you! *Chuckles* Guess I should just hop right into it, huh?"

    scene v13s24_16b # FPP. same as v13s24_16 emmy mouth closed
    with dissolve

    u "I'm ready when you are. *Chuckles*"

    scene v13s24_12a # FPP. same as v13s24_12 Both hands on podium.
    with dissolve

    barh "Just bypass the host, huh guys?"

    scene v13s24_12b # FPP. same as v13s24_12a barhost mouth closed
    with dissolve

    u "Oh, right... *Laughs* Sorry."

    scene v13s24_12a
    with dissolve

    barh "No, no, no. I'm only teasing... Go right ahead."

    scene v13s24_16c # FPP. same as v13s24_16 emmy looking at barhost
    with dissolve

    emmy "Ha, alright..."

    scene v13s24_16
    with dissolve

    emmy "First question... How do you feel about kids?"

    scene v13s24_10e # FPP. same v13s24_10 imre looking at emmy
    with dissolve

    imre "Man, fuck them kids! *Laughs* I'm not trying to get you pregnant."

    scene v13s24_10e
    with dissolve

    imre "We can have fun and all but, no kids... Not right now at least."

    scene v13s24_11c
    with dissolve

    ry "Well, I'll be honest. I'm not interested in having kids at this very moment, but I do want children in the future... And many of them. *Chuckles*"

    menu:
        "No kids for me":
            $ add_point(KCT.BRO)
            $ v13_emmy_points += 1
            
            scene v13s24_11a
            #with dissolve

            u "Yeah, I'm on the no kids vibe at the moment too. Guess it's just not something I think about."

            scene v13s24_16d # FPP. same as v13s24_16b emmy head tilted, playing with her hair, happy smile
            with dissolve

            pause 0.75

        "I'm a family man":
            $ add_point(KCT.BOYFRIEND)
            
            scene v13s24_11a
            #with dissolve
            
            u "I'm a family man of course, a little bit of me continued through our generations. That's really what I'm all about."

            scene v13s24_16e # FPP. same as v13s24_16b emmy flirty smirk, squinting a little like she's trying to figure him out
            with dissolve

            pause 0.75

    scene v13s24_16
    with dissolve

    emmy "Okay... Interesting answers so far. *Chuckles*"

    scene v13s24_16
    with dissolve

    emmy "Next question, would you rather live in the rurals or in the city?"

    scene v13s24_10e
    with dissolve

    imre "City."

    scene v13s24_11c
    with dissolve

    ry "City."

    menu:
        "City":
            $ v13_emmy_points += 2
            
            if v13_emmy_points == 3:
                $ emmy.relationship = Relationship.LIKES
            
            scene v13s24_16b
            with dissolve

            u "City."

            scene v13s24_16
            with dissolve

            emmy "Haha! Interesting..."
            
        "Rural":
            scene v13s24_16b
            with dissolve

            u "Rural."

            scene v13s24_16
            with dissolve

            emmy "Oh... Interesting. *Chuckles*"

    scene v13s24_16
    with dissolve

    emmy "Well, that's all that's all I needed to hear!"

    scene v13s24_10e
    with dissolve

    imre "You sure?"

    scene v13s24_16f # FPP. same as v13s24_16 emmy looking at imre 
    with dissolve

    emmy "Very sure. *Chuckles*"

    scene v13s24_12a
    with dissolve

    barh "Alright then, Emmy. Will you send in Kourtney for us, please?"

    scene v13s24_16
    with dissolve

    emmy "Sure. See you soon guys..."

    scene v13s24_14
    with dissolve

    pause 0.75

    scene v13s24_13a # FPP. same as v13s24_13 emmy's back is turned.
    with dissolve

    pause 0.75

    scene v13s24_10
    with dissolve

    imre "*Chuckles* She was definitely into me."

    scene v13s24_11b
    with dissolve

    ry "You are far from being her type, Imre. *Laughs* No woman brings up the idea of having kids if she doesn't want any."

    scene v13s24_10d
    with dissolve

    imre "That's not true."

    scene v13s24_11b
    with dissolve

    ry "You'll find out soon."

    scene v13s24_13b # FPP. same as v13s24_13 kourtney instead of emmy
    with dissolve

    pause 0.75

    scene v13s24_14a # FPP. same as v13s24_14 kourtney instead of emmy
    with dissolve

    pause 0.75

    scene v13s24_15a # FPP. same as v13s24_15 kourtney instead of emmy
    with dissolve

    u "Good luck guys."

    scene v13s24_16g # FPP. same as v13s24_16 kourtney instead of emmy
    with dissolve

    kourt "Gentlemen."

    scene v13s24_16h # FPP. same as v13s24_16g kourtney looks at MC, one hand over her heart, slight smile, mouth closed
    with dissolve

    u "Our lady."

    scene v13s24_10
    with dissolve

    imre "*Whisper* Simp."

    scene v13s24_16h
    with dissolve

    u "*Chuckles*"

    scene v13s24_16g
    with dissolve

    kourt "Alright, so I only have one question."

    scene v13s24_11c
    with dissolve

    ry "I like that. One will answer them all. *Chuckles* Go ahead."

    scene v13s24_16g
    with dissolve

    kourt "Haha, alright... Are you the type of man to open the door for me every day and get me flowers every special occasion?"

    scene v13s24_10e
    with dissolve

    imre "Sorry babe, that's not for me. *Laughs*"

    scene v13s24_11c
    with dissolve

    ry "I do like to spoil my girl, so maybe."

    menu:
        "Yes, I'm a romantic":
            $ add_point(KCT.BOYFRIEND)
            $ kourtney.relationship = Relationship.LIKES
            
            scene v13s24_16h
            with dissolve

            u "I feel like I'm a romantic, so of course."

        "No, that's too old school":
            $ add_point(KCT.TROUBLEMAKER)

            scene v13s24_16i # FPP. same as v13s24_16h kourtney slight frown
            with dissolve

            u "That sounds like a lot for our generation, but even if it isn't... I just don't see myself doing that."

    scene v13s24_16g
    with dissolve

    kourt "Well, I can easily see who is and isn't a real man. *Chuckles*"

    scene v13s24_12a
    with dissolve

    barh "Thank you Kourtney. Please send in Aryssa."

    scene v13s24_14a
    with dissolve

    pause 0.75

    scene v13s24_13c # FPP. same as v13s24_13b kourtney's back is turned
    with dissolve

    pause 0.75

    scene v13s24_10
    with dissolve

    imre "She was a weird ass chick..."

    scene v13s24_11b
    with dissolve

    ry "What was weird about her?"

    scene v13s24_11a
    with dissolve

    u "He's just talking shit, can't get Ashton off his mind."

    scene v13s24_10
    with dissolve

    imre "Who's Ashton?"

    scene v13s24_12a
    with dissolve

    barh "Haha, I see he's trying hard to forget..."

    scene v13s24_10f # FPP. same as v13s24_10c imre flips off MC
    with dissolve

    pause 0.75

    scene v13s24_13d # FPP. same as v13s24_13 aryssa instead of emmy
    with dissolve

    pause 0.75

    scene v13s24_10g # FPP. same as v13s24_10c imre looks at and flips off barhost
    with dissolve

    pause 0.75

    scene v13s24_14b # FPP. same as v13s24_14 aryssa instead of emmy
    with dissolve

    pause 0.75

    scene v13s24_15b # FPP. same as v13s24_15 aryssa instead of emmy
    with dissolve

    pause 0.75

    scene v13s24_16j # FPP. same as v13s24_16f aryssa instead of emmy
    with dissolve

    ary "Flipping two people off already? Not an impressive sight."

    scene v13s24_10h # FPP. same as v13s24_10e imre slightly shocked
    with dissolve

    imre "*Shocked* I was just... They brought up the- Nevermind. *Sighs*"

    scene v13s24_16k # FPP. same as v13s24_16 aryssa instead of emmy
    with dissolve

    ary "*Chuckles* Okay so, I also just have one question."

    scene v13s24_16l # FPP. same as v13s24_16b aryssa instead of emmy
    with dissolve

    u "Shoot."

    scene v13s24_16k
    with dissolve

    ary "If you were beyond wealthy, would you still work?"

    scene v13s24_10e
    with dissolve

    imre "Hell no."

    scene v13s24_11c
    with dissolve

    ry "Well, I wouldn't wanna be doing nothing. So, probably."

    menu:
        "Work":
            $ add_point(KCT.BOYFRIEND)
            $ aryssa.relationship = Relationship.LIKES
            
            scene v13s24_16l
            with dissolve

            u "I'd still be working in some way, shape or form. Don't have time for boredom."

        "Retired life":
            $ add_point(KCT.BRO)
            $ add_point(KCT.TROUBLEMAKER)

            scene v13s24_16m # FPP. same as v13s24_16l aryssa slight frown
            with dissolve

            u "Why work if you're rich? Isn't that the point in getting rich? So that you don't have to work? *Chuckles*"

            scene v13s24_10
            with dissolve

            imre "*Laughs*"

    scene v13s24_16k
    with dissolve

    ary "Well... You guys have pretty definitive personalities."

    scene v13s24_16l
    with dissolve

    u "We try to be different. *Chuckles*"

    scene v13s24_16k
    with dissolve

    ary "Haha, I like that."

    scene v13s24_12a
    with dissolve

    barh "It's now time to get to the results! Emmy? Kourtney? You can come on out."

    scene v13s24_13e # TPP. same as v13s24_13 emmy and kourtney walking in, both slight smiles, both mouths closed
    with dissolve

    pause 0.75

    scene v13s24_19 # FPP. show barhost dragging a large bench for three people in front of the table (where the chair was) for the ladies, barhost visibly struggling, mouth closed
    with dissolve

    pause 0.75

    scene v13s24_20 # FPP. show emmy kourtney and aryssa sitting on the bench, all slight smiles, mouths closed
    with dissolve

    pause 0.75

    scene v13s24_10 
    with dissolve

    imre "This is going pretty fast..."

    scene v13s24_12a
    with dissolve

    barh "That's what she said. *Laughs*"

    scene v13s24_12a
    with dissolve

    barh "Right then... Ladies, go ahead and decide on your man. If you would be willing to go on a date with [name], please raise your hand."

    if not emmy.relationship >= Relationship.LIKES and not kourtney.relationship >= Relationship.LIKES and not aryssa.relationship >= Relationship.LIKES:
        scene v13s24_20a # FPP. same as v13s24_20 emmy kourtney and aryssa looking in different directions, no expressions, hands MUST be at sides or in laps NOT raised, mouths closed
        with dissolve

        pause 2

        scene v13s24_21 # TPP. FPP from the ladies perspective, MC slightly shocked, palms of hands up raised to chest level, imre and ryan pointing and laughing at MC, all mouths open
        with dissolve

        pause 1

    elif emmy.relationship >= Relationship.LIKES and kourtney.relationship >= Relationship.LIKES and aryssa.relationship >= Relationship.LIKES:
        scene v13s24_20b # FPP. same as v13s24_20 emmy kourtney and aryssa looking at MC, all with one hand raised, all fully smiling, all mouths closed
        with dissolve

        pause 2

        scene v13s24_10i # FPP. same as v13s24_10a imre rolls his eyes
        with dissolve

        pause 1

        scene v13s24_11d # FPP. same as v13s24_11a ryan rolls his eyes
        with dissolve

        pause 1

    elif emmy.relationship >= Relationship.LIKES and kourtney.relationship >= Relationship.LIKES:
        scene v13s24_20c # FPP. same as v13s24_20b aryssa no expression and doesn't raise her hand
        with dissolve

        pause 2

    elif emmy.relationship >= Relationship.LIKES and aryssa.relationship >= Relationship.LIKES:
        scene v13s24_20d # FPP. same as v13s24_20b kourtney no expression and doesn't raise her hand
        with dissolve

        pause 2

    elif kourtney.relationship >= Relationship.LIKES and aryssa.relationship >= Relationship.LIKES:
        scene v13s24_20e # FPP. same as v13s24_20b emmy no expression and doesn't raise her hand
        with dissolve

        pause 2

    elif emmy.relationship >= Relationship.LIKES:
        scene v13s24_20f # FPP. same as v13s24_20b show just emmy raising her hand, full smile, mouth closed, 
        with dissolve

        pause 2

    elif kourtney.relationship >= Relationship.LIKES:
        scene v13s24_20g # FPP. same as v13s24_20b show just kourtney raising her hand, full smile, mouth closed, 
        with dissolve

        pause 2

    elif aryssa.relationship >= Relationship.LIKES:
        scene v13s24_20h # FPP. same as v13s24_20b show just aryssa raising her hand, full smile, mouth closed, 
        with dissolve

        pause 2

    scene v13s24_12a
    with dissolve

    barh "Alright... If you'd be willing to go out with Ryan, please raise your hand."

    scene v13s24_20e
    with dissolve

    pause 1.25

    scene v13s24_12a
    with dissolve

    barh "Very well... Lastly, catfish-I mean, Imre. *Chuckles* If you'd be willing to go out with Imre, please raise your hand."

    scene v13s24_20f
    with dissolve

    pause 1.25

    scene v13s24_10e
    with dissolve

    imre "I'm all yours baby!"

    scene v13s24_20i # FPP. same as v13s24_20f kourtney and aryssa roll their eyes, emmy has put down here hand
    with dissolve

    emmy "*Chuckles*"

    scene v13s24_12a
    with dissolve

    barh "Alright then, now it is time for my favorite part of the evening... The dates!"

    scene v13s24_12a
    with dissolve

    if not emmy.relationship >= Relationship.LIKES and not kourtney.relationship >= Relationship.LIKES and not aryssa.relationship >= Relationship.LIKES:
        scene v13s24_12a
        with dissolve

        barh "Sorry, [name]. You didn't find your match today, but it was nice meeting you."

        scene v13s24_12b # FPP. same as v13s24_12a barhost mouth closed
        with dissolve

        u "Ah, well... That's alright I guess. *Chuckles* You guys have fun."

        scene v13s24_10j # FPP. same as v13s24_10 imre slight frown
        with dissolve

        imre "Sorry man... We will though."

        scene v13s24_11
        with dissolve

        ry "Yeah, haha. We will."

        scene v13s24_22 # FPP. MC is still sitting at the table, show imre walking next to emmy, show ryan walking between kourtney and aryssa, all of their backs turned
        with dissolve

        pause 0.75

        scene v13s24_22a # FPP. same as v13s24_22 show aryssa walking away from the group, imre and emmy go in one direction, ryan and kourtney go in another direction
        with dissolve

        pause 0.75

        scene v13s24_23 # TPP. MC stands up and walks to the bench
        with dissolve

        pause 0.75
        
        scene v13s24_24 # TPP. MC lays on his back on the bench
        with dissolve

        pause 0.75

        scene v13s24_24a # TPP. same as v13s24_24 MC looks up at his phone, slight smile, mouth closed
        with dissolve

        jump v13s27

    else:

        barh "We'll give you the choice based on the ladies interested in you, and you'll have a chance to talk one-on-one."
        scene black

        call screen v13s24_girl

label v13s24_emmy_date:
            
    scene v13s24_26 # FPP show mc reaching out with his hand to emmy, emmy still sitting on the bench placing her hand into mc's hand, looking up at mc, slight smile, mouth closed
    with dissolve

    u "Let's go, Emmy."

    scene v13s24_27 # TPP show mc looking imre and ryan sitting at the table, imre mouth open, slight anger, mouth open, ryan slight smile, mouth open.
    with dissolve

    imre "What about me?"

    scene v13s24_27a # TPP same as v13s24_27 imre mouth closed, sad expression, ryan laughing, mouth open
    with dissolve

    u "Sorry man. *Chuckles*"

    scene v13s24_28 # TPP. MC grabs emmy's hand and leads her toward a more private seating area, MC slight smile mouth open, emmy slight smile mouth closed
    with fade

    pause 0.75

    jump v13s25

label v13s24_kourtney_date:

    scene v13s24_26a # FPP same as v13s24_26 kourtney instead of emmy
    with dissolve

    $ grant_achievement("romantic_heart")
    u "Let's go, Kourtney."

    scene v13s24_28a # TPP. same as v13s24_28 kourtney instead of emmy
    with fade

    pause 0.75
    
    jump v13s25a

label v13s24_aryssa_date:

    scene v13s24_26b # FPP same as v13s24_26 aryssa instead of emmy
    with dissolve

    u "Let's go, Aryssa."
    
    scene v13s24_28b # TPP. same as v13s24_28 aryssa instead of emmy
    with fade

    pause 0.75

    jump v13s25b

label v13s24_no_simplr_date:

    scene v13s24_11a
    with dissolve

    u "Yeah, I don't know actually. You guys go ahead and enjoy yourselves, I'm just gonna chill."

    scene v13s24_11e # FPP. same as v13s24_11 ryan slight frown
    with dissolve

    ry "Huh? You sure?"

    scene v13s24_11a
    with dissolve

    u "Yeah, I'm sure."

    scene v13s24_10
    with dissolve

    imre "Well, we will enjoy ourselves. *Chuckles*"

    scene v13s24_22
    with dissolve

    pause 0.75

    scene v13s24_22a
    with dissolve

    pause 0.75

    scene v13s24_23
    with dissolve

    pause 0.75
    
    #scene v13s24_24
    #with dissolve

    #pause 0.75

    #scene v13s24_24a
    #with fade

    #pause 0.75

    jump v13s27