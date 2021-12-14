# SCENE 50: Double Date
# Locations: Resturant 
# Characters: RYAN (Outfit: 1), MC (Outfit: 1), RILEY (Outfit: 4), EMILY (Outfit: 2)
# Time: Night

label v13s50:
    scene v13s50_1 # TPP. Show Ryan and MC at hotel lobby, Mc slight smile, mouth closed, Ryan, slight smile, mouth open
    with fade
    
    ry "I'm really nervous, haha."

    play music "music/v13/Track Scene 50_1.mp3" fadein 2

    scene v13s50_2 # FPP. Ryan looking at MC, slight smile, mouth closed
    with dissolve

    u "*Chuckles* Why?"

    scene v13s50_2a # FPP. Same as v13s50_2, mouth open
    with dissolve

    ry "Because this is real, dude! Like, it's an actual date."

    scene v13s50_2
    with dissolve

    u "*Laughs* Relax man, where are we going?"

    scene v13s50_2a
    with dissolve

    ry "The girls are already at the restaurant, we're just going to the one in the hotel here."

    scene v13s50_2
    with dissolve

    u "Alright cool, let's go."

    scene v13s50_2c # FPP. Same as v13s50_2, Ryan takes deep breath, mouth closed 
    with dissolve

    ry "*Deep breath*"

    scene v13s50_2
    with dissolve

    u "You're doing way too much right now..."

    scene v13s50_2a
    with dissolve

    ry "I'll relax, promise."

    scene v13s50_3 # TPP. Show MC and Ryan walking through hotel lobby, both slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v13s50_4 # TPP. Show MC and Ryan walking though hotel corridor, both neutral expression, mouth closed 
    with dissolve

    pause 0.75
   
    scene v13s50_5 # TPP. Show MC and Ryan walking into resturant, both neutral expression, mouth closed 
    with dissolve
    
    pause 0.75
    
    scene v13s50_6 # TPP. Show MC and Ryan sitting down at table, Ryan sits beside Emily, MC sits beside Riley, all slight smile, mouth closed
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v13/Track Scene 50_2.mp3" fadein 2

    scene v13s50_7 # FPP. Riley looking at MC, slight smile, mouth open
    with dissolve

    ri "There you guys are! We were starting to think you ditched us. *Laughs*"

    scene v13s50_7a # FPP. Same as v13s50_7, mouth closed
    with dissolve

    u "Oh no, never. *Chuckles*"

    scene v13s50_7
    with dissolve

    ri "Hope you both don't mind, but we ordered for the table already."

    scene v13s50_8 # FPP. Ryan looking across table in Riley's direction, slight smile, mouth open 
    with dissolve

    ry "Of course not."

    scene v13s50_9 # FPP. Emily looking at MC, slight smile, mouth open
    with dissolve

    em "I knew what [name] would've wanted."

    scene v13s50_8a # FPP. Same as v13s50_8, Ryan looking at MC
    with dissolve

    ry "Well, yeah... That makes sense. Ha."

    scene v13s50_9a # FPP. Same as v13s50_9, mouth closed  
    with dissolve

    u "(Oh my god.)"

    scene v13s50_7b # FPP. Same as v13s50_7, Riley looking across table in Emily's direction 
    with dissolve

    ri "So, how long have you guys been talking?"

    scene v13s50_9b # FPP. Same as v13s50_9, Emily looking at Riley 
    with dissolve

    em "A few weeks now."

    scene v13s50_7b
    with dissolve

    ri "Oooh okay, and look at you guys now. Having dates in other countries... *Chuckles*"

    scene v13s50_8
    with dissolve

    ry "Believe it or not, this is actually our first date."

    scene v13s50_7c # FPP. Same as v13s50_7, Riley looking at Ryan
    with dissolve

    ri "Aww, cute! Let's make it a good one. *Chuckles*"

    scene v13s50_9
    with dissolve

    em "*Whispers* We'll see."

    scene v13s50_7d # FPP. Same as v13s50_7b, different posture
    with dissolve

    ri "I've always liked the beginning, you know? The part where you're just getting to know each other and everything."

    scene v13s50_8b # FPP. Same as v13s50_8, Ryan looking at Emily
    with dissolve

    ry "As much as we've talked, I feel like I know everything there is to know about the beautiful Emily Barnes."

    scene v13s50_7c 
    with dissolve

    ri "Awww..."

    scene v13s50_9c # FPP. Same as v13s50_9, Emily looking at Ryan
    with dissolve

    em "There's still plenty to learn. *Chuckles* [name] still knows more about me than you do I think."

    scene v13s50_9
    with dissolve

    em "Isn't that right, [name]?"

    menu:
        "He knows more":
            $ add_point(KCT.BRO)
            scene v13s50_9a
            with dissolve

            u "You and I don't talk as often anymore, so he knows the new Emily way better than I do. I know the old Emily and well... Nevermind."

        "I know more":
            scene v13s50_8c # FPP. Same as v13s50_8a, mouth closed 
            with dissolve

            u "Yeah, you guys haven't talked long enough to make up for years of knowing each other, haha."

            scene v13s50_9
            with dissolve

            em "Very true."

    scene v13s50_7b
    with dissolve

    ri "Okayyy... So do you both live on campus?"

    scene v13s50_8
    with dissolve

    ry "We do."

    scene v13s50_8c
    with dissolve

    u "Ryan's into the frat life."

    scene v13s50_7d
    with dissolve

    ri "Oh yeah, have you seen him fight, Emily?"

    scene v13s50_9d # FPP. Same as v13s50_9c, slightly surprised expression
    with dissolve

    em "No, can you fight?"

    scene v13s50_8d # FPP. Same as v13s50_8b, different posture
    with dissolve

    ry "Can I? *Chuckles* I'm the best!"

    scene v13s50_9
    with dissolve

    em "Better than [name]? I've seen him fight and he's pretty fucking good."

    scene v13s50_8e # FPP. Same as v13s50_8b, Angry expression
    with dissolve

    ry "Who's your date, Emily? Me or [name]?"

    scene v13s50_8f # FPP. Same as v13s50_8e, different posture
    with dissolve

    ry "I'm starting to get confused since you keep giving him all the props."

    scene v13s50_7b
    with dissolve

    ri "Let's not make it awkward, guys. Ha..."

    scene v13s50_7a
    with dissolve

    u "Okay... I'm gonna go use the restroom."

    scene v13s50_10 # TPP. Show MC standing up from his seat, slight smile, mouth closed, Ryan, annoyed expression, mouth closed, Riley and Emily, slight smile, mouth closed
    with dissolve

    pause 0.75
    
    scene v13s50_11 # FPP. Emily looking at MC, slight smile, mouth open
    with dissolve

    em "I need to go too."

    scene v13s50_12 # FPP. Ryan looking to the side, slightly angry expression, mouth open
    with dissolve

    ry "*Whisper* Bullshit."

    scene v13s50_11a # FPP. Same as v13s50_11, mouth closed
    with dissolve

    u "I can wait for you to go."

    scene v13s50_11
    with dissolve

    em "Why? There's more than one bathroom."

    scene v13s50_11a
    with dissolve

    u "Okay, yeah... Guess we'll be right back."

    scene v13s50_12a # FPP. Same as v13s50_12, Ryan looking at Emily, slight smile, mouth open
    with dissolve

    ry "Hurry back, Em! A minute away from your beautiful face is a minute I regret."

    scene v13s50_11b # FPP. Same as v13s50_11, Emily looking at Ryan
    with dissolve

    em "Haha, okay handsome."
   
    scene v13s50_13 # TPP. Show MC and Emily walking off to the washroom, Emily further back from MC, MC neutral expression, mouth closed, Emily, slight smile, mouth open
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v13/Track Scene 50_3.mp3" fadein 2

    scene v13s50_14 # TPP. Show MC entering the washroom thinking to himself, slight smile, mouth closed 
    with dissolve

    pause 0.75

    u "(A little more awkward than I thought.)"

    scene v13s50_15 # TPP. Show Emily walking into washroom, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v13s50_16 # FPP. Emily looking at MC, slight smile, mouth closed 
    with dissolve

    u "Uhh, what the hell are you doing in here?"

    scene v13s50_16a # FPP. Same as v13s50_16, slightly irritated expression, mouth open
    with dissolve

    em "It's a unisex bathroom."

    scene v13s50_16
    with dissolve

    u "So? You know I'm in here."

    scene v13s50_16b # FPP. Same as v13s50_16, different posture
    with dissolve

    u "Why are you acting like this? You're on a date with Ryan, stop making it awkward."

    scene v13s50_16c # FPP. Same as v13s50_16, mouth open
    with dissolve

    em "You don't like it when I compliment you?"

    scene v13s50_16
    with dissolve

    u "Not when you're supposed to be on a date."

    scene v13s50_17 # TPP. Show Emily pushing MC against wall, Emily, slight smile, mouth open
    with dissolve

    em "So you do like it, just not publically."

    scene v13s50_18 # TPP. Show MC up against wall, MC, neutral expression, mouth closed, closeup, Emily has hands on MC, slight smile, mouth closed 
    with dissolve

    pause 0.75

    menu:
        "Kick her out":
            scene v13s50_19 # FPP. MC puts one hand on Emily's shoulder, pushing her back lightly, Emily, slightly surprised expression, mouth closed
            with dissolve

            pause 0.75

            stop music fadeout 3
            play music "music/v13/Track Scene 50_4.mp3" fadein 2

            scene v13s50_19a # FPP. Same as v13s50_19, MC hands down to his side
            with dissolve

            u "We're not doing this. Deadass, get the fuck out!"

            scene v13s50_19b # FPP. Same as v13s50_19a, slightly sad expression 
            with dissolve

            em "..."

            scene v13s50_19c # FPP. Same as v13s50_19b, angry expression
            with dissolve

            u "GO!"

            scene v13s50_19d # FPP. Same as v13s50_19c, mouth open
            with dissolve

            em "Fuck you!"

            scene v13s50_20 # FPP. Emily walks out of the washroom, back facing MC
            with dissolve

            pause 0.75

            scene v13s50_21 # FPP. MC looks at the washroom door that is closed, thinking to himself
            with dissolve
            
            u "(Damn, psycho. I thought no meant no!)"

            if v13s48_ryan_double_date:
                jump v13s50a_return_after_emily

            scene v13s50_21
            with dissolve

            u "(I'm taking my ass to bed.)"

        "Fuck her":
            scene v13s50_18a # TPP. Same as v13s50_18, MC, slight smile, mouth open
            with dissolve

            u "You know what?"

            stop music fadeout 3

            jump v13s50a

    scene v13s50_22 # TPP. Show MC leaving washroom, neutral expression, mouth closed
    with dissolve

    pause 0.75

    scene v13s50_23 # TPP. Show Mc walking through resturant, neutral expression, mouth closed 
    with dissolve

    pause 0.75

    scene v13s50_24 # TPP. Show MC walking into lobby, slight smile, mouth closed
    with dissolve

    pause 0.75

    stop music fadeout 3

    if chloe.relationship.value >= Relationship.GIRLFRIEND.value and not v11_riley_roomate:
        jump v13s52
    
    elif riley.relationship.value >= Relationship.FWB.value and v11_riley_roomate:
        jump v13s53
    
    else: 
        jump v13s54