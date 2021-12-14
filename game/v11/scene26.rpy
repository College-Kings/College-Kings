# SCENE 26: Hotel Bar with Ms. Rose and Samantha
# Location: Hotel Bar
# Characters: MC (Outfit 1), Ms. Rose (Outfit 1), Samantha (Outfit 1)
# Time: Evening

label v11_hotel_bar_wolves: #can only get here if joinwolves
    play music "music/v11/Track Scene 5_6.mp3" fadein 2
    if v11s25_beer:
        scene v11hrs1 # TPP Show MC taking a drink of his beer
        with dissolve

        u "*Gulp*"

        scene v11hrs2 # FPP MC looking down at his phone
        with dissolve

        u "*Sighs*"

        scene v11hrs1
        with dissolve

        u "*Gulp*"

        # MC looking down at the bar when he hears Ms. Rose behind him
        scene v11hrs3 # FPP Show bar with a half-empty beer
        with dissolve

        ro "Mmhmm..."

    else:
        scene v11hrs1a # TPP Same angle as v11hrs1, show MC taking a drink of a fruity cocktail
        with dissolve

        u "*Gulp*"

        scene v11hrs2
        with dissolve

        u "*Sighs*"

        scene v11hrs1a
        with dissolve

        u "*Gulp*"

        # MC looking down at the bar when he hears Ms. Rose behind him
        scene v11hrs3a # TPP Same angle as v11hrs3, show bar with a half-empty fruity cocktail
        with dissolve

        ro "Mmhmm..."

    scene v11hrs4 # FPP Show Ms Rose, standing behind where MC is sitting, smiling with mouth open
    with dissolve

    ro "Should you be drinking that?"

    scene v11hrs4a # FPP Same angle as v11hrs4, Ms. Rose smiling with mouth closed
    with dissolve

    u "Well, it's legal here. And... What happens in London stays in London."

    scene v11hrs5 # TPP Show Ms. Rose taking a seat at the bar next to MC, Ms. Rose smiling with mouth open
    with dissolve

    ro "*Chuckles* Glad to see you students taking in the full Europe experience."

    scene v11hrs6 # FPP Show Ms. Rose, sitting next to MC, smiling with mouth closed
    with dissolve

    u "Some of us are, others are sleeping all day or skipping out."

    scene v11hrs6a # FPP Same angle as v11hrs6, Ms. Rose smiling with mouth open
    with dissolve

    ro "Reminds me of when I was in school. I went on a trip to Mexico and spent a bunch of time with the salsa dancers, missed out on everything else. *Chuckles*"

    scene v11hrs6
    with dissolve

    u "Haha, I didn't know you liked dancing?"

    scene v11hrs6a
    with dissolve

    ro "There's a lot that students don't know about their teachers..."

    scene v11hrs6
    with dissolve

    u "Haha, true. But, if you want to know something about Mr. Lee all you have to do is ask. That man's an open book."

    scene v11hrs6b # FPP Same angle as v11hrs6, Ms. Rose smiling, eyebrow raised, mouth open
    with dissolve

    ro "And I'm not?"

    scene v11hrs6
    with dissolve

    u "Guess I wouldn't know."

    scene v11hrs7 # FPP Show bartender behind bar, mouth open
    with dissolve

    bartender "Anything for you ma'am?"

    scene v11hrs6a
    with dissolve

    ro "No thank you, not for me. I was just heading up to my room."

    scene v11hrs6
    with dissolve

    if ms_rose.relationship.value >= Relationship.FWB.value:
        pause 0.5

        scene v11hrs8 # TPP Close up of Ms. Rose whispering in MC's ear, Ms. Rose smiling with mouth open
        with dissolve

        ro "*Whisper* Speaking of what happens in London stays in London... Room 404, 10 minutes. Don't be late."

        #play sound "sounds/kiss.mp3"

        scene v11hrs4b # FPP Same angle as v11hrs4, Ms. Rose walking away, looking back at MC and blowing a kiss
        with dissolve

        u "(Did she just say what I think she said?)"

    else:
        scene v11hrs6a
        with dissolve

        ro "Have a good night, [name]."

        scene v11hrs6
        with dissolve

        u "You too."

    scene v11hrs7
    with dissolve

    bartender "She's a very pretty lady."

    scene v11hrs7a # FPP Same angle as v11hrs7, bartender's mouth closed
    with dissolve

    u "She's my teacher."

    scene v11hrs7
    with dissolve

    bartender "And? Doesn't change how beautiful she is."

    scene v11hrs7a
    with dissolve

    u "*Chuckles* True."

    scene v11hrs7
    with dissolve

    bartender "You know, this hotel gets a lot of tourists and I've seen all types of groups. Pretty rare for students to drink, even rarer for them to drink alone."

    scene v11hrs7a
    with dissolve

    u "I won't be down here long. Someone will either come down and join me or they'll blow up my phone."
    u "This is probably the first time I've had a few minutes to myself besides being asleep."

    scene v11hrs2
    with dissolve

    bartender "Someone hit you up?"

    scene v11hrs7a
    with dissolve

    u "Not yet."

    if v11s25_beer:
        scene v11hrs1
        with dissolve

        u "*Gulp*"

        scene v11hrs9 # FPP View of the empty bar
        with dissolve

        u "*Sighs*"

        scene v11hrs1b # TPP Same angle as v11hrs1, show MC finishing off his beer
        with dissolve

        u "*Gulp*"

    else:
        scene v11hrs1a
        with dissolve

        u "*Gulp*"

        scene v11hrs9
        with dissolve

        u "*Sighs*"

        scene v11hrs1c # TPP. Same angle as v11hrs1, show MC finishing off his fruity cocktail
        with dissolve

        u "*Gulp*"

    if ms_rose.relationship.value >= Relationship.FWB.value:
        scene v11hrs2
        with dissolve

        u "(10 minutes.)"

        menu:
            "Go to her room":
                $ add_point(KCT.TROUBLEMAKER)

                scene v11hrs5a # TPP Same angle as v11hrs5, MC alone at bar, getting off of bar stool to leave
                with dissolve

                pause 0.75

                scene v11hrs10 # FPP View of bartender from entrance to bar, bartender still behind the bar, smiling with mouth open
                with dissolve

                bartender "Tell her I said hi."

                scene v11hrs11 # TPP Show MC exiting the bar into the hotel lobby
                with dissolve

                u "(Haha.)"

                jump v11_ms_rose_sex

            "Don't go":
                scene v11hrs2
                with dissolve

                u "(*Sighs* This isn't right.)"
    jump v11_bartender_hotel_chat

label v11_hotel_bar_apes:
    if v11s25_beer:
        scene v11hrs1
        with dissolve

        u "*Gulp*"

        scene v11hrs2
        with dissolve

        u "*Sighs*"

        scene v11hrs1
        with dissolve

    else:
        scene v11hrs1a
        with dissolve

        u "*Gulp*"

        scene v11hrs2
        with dissolve

        u "*Sighs*"

        scene v11hrs1a
        with dissolve

        u "*Gulp*"

    if v11_invite_sam_europe:
        # -MC is looking at the bar when he hears Samantha behind him-
        if v11s25_beer:
            scene v11hrs3
            with dissolve

            sa "I get away from one Ape and bump into another."

        else:
            scene v11hrs3a
            with dissolve

            sa "I get away from one Ape and bump into another."

        scene v11hrs4c # FPP Same angle as v11hrs4, show Samantha standing behind where MC is sitting, annoyed expression, mouth closed
        with dissolve

        u "*Chuckles* Hey Sam."

        scene v11hrs4d # FPP Same angle as v11hrs4, Samantha looking annoyed with mouth open
        with dissolve

        sa "Hey."

        scene v11hrs5b # TPP Same angle as v11hrs5, show Samantha taking a seat at the bar next to MC, annoyed expression, mouth open
        with dissolve

        sa "You know, I thought when I came on this trip I'd be getting away from Cameron. I didn't think he'd be stalking the shit out of me all the way to Europe."

        scene v11hrs6c # FPP Same angle as v11hrs6, Samantha sitting next to MC, looking annoyed with mouth open
        with dissolve

        sa "You know he isn't even with the group? He booked his own flight and is following our Europe tour."

        scene v11hrs6d # FPP Same angle as v11hrs6, Samantha sitting next to MC, looking annoyed with mouth closed
        with dissolve

        u "*Laughs* I really needed a laugh, Sam. Thanks, haha."

        scene v11hrs6c
        with dissolve

        sa "It isn't funny, he's fucking crazy."

        scene v11hrs7
        with dissolve

        bartender "On that note, I assume you'll be wanting a drink?"

        scene v11hrs6d
        with dissolve

        u "You want a beer?"

        scene v11hrs6c
        with dissolve

        sa "It's probably not a good idea for me to drink. And believe it or not, that's not what I came down here for."

        scene v11hrs6d
        with dissolve

        u "What did you come down here for?"

        scene v11hrs6c
        with dissolve

        sa "I came down here for the spa."

        scene v11hrs6d
        with dissolve

        u "But you're at the bar, you see how that could be misleading?"

        scene v11hrs6c
        with dissolve

        sa "The spa is closed."

        scene v11hrs6d
        with dissolve

        u "Ahh."

        scene v11hrs7
        with dissolve

        bartender "Yes, I'm sorry love, but it'll be open come morning."

        scene v11hrs12 # FPP Show bartender walking from behind the bar to the back room
        with dissolve

        pause 0.5
        
        scene v11hrs13 # FPP Show Samantha leaning on the bar, watching the bartender walk away, Samantha's eyebrow raised, mouth closed
        with dissolve

        pause 0.5

        scene v11hrs13a # FPP Same angle as v11hrs13, Samantha now smiling as she leans over the bar and grabs a set of keys
        with dissolve

        u "*Whisper* What are you doing? *Chuckles*"

        scene v11hrs6e # FPP Same angle as v11hrs6, Samantha holding a set of keys, she has a mischievous smile, mouth open
        with dissolve

        sa "*Whisper* What I came over here for. I said I was going to the spa."

        menu:
            "Put them back":
                scene v11hrs6f # FPP Same angle as v11hrs6, Samantha holding the keys with a mischievous smile, mouth closed
                with dissolve

                u "*Whisper* What? No, put them back. You can't just take her keys. What are you thinking?"

                scene v11hrs6c
                with dissolve

                sa "Oh my God, I swear I can't do anything I wanna do..."

                scene v11hrs13b # FPP Same angle as v11hrs13b, Samantha looking annoyed as she throws the keys back to where she got them
                with dissolve

                pause 0.5

                scene v11hrs4e # FPP Same angle as v11hrs4, show Samantha walking away angry, arms folded across her chest
                with dissolve

                u "*Sighs*"

                scene v11hrs7
                with dissolve

                bartender "Quite the friends you have. *Chuckles*"

                scene v11hrs7a
                with dissolve

                u "Tell me about it."

            "Now what?":
                scene v11hrs6f
                with dissolve

                u "Okay klepto, now what?"

                scene v11hrs6e
                with dissolve

                sa "Now I go to the spa. C'mon, you're coming too."

                scene v11hrs6f
                with dissolve

                u "So I can get wrapped up in your little scheme? *Chuckles*"

                scene v11hrs5c # TPP Same angle as v11hrs5, Samantha smiling with mouth open, holding keys in one hand, other hand holding MC's, pulling him off of his bar stool
                with dissolve

                sa "Less talking, more walking!"

                scene v11hrs11a # TPP Same angle as v11hrs11, show Samantha pulling MC out of the bar into the hotel lobby
                with dissolve

                pause 0.5

                jump v11_sam_spa
    stop music fadeout 3
    jump v11_bartender_hotel_chat