# SCENE 11: At the hotel in Paris
# Locations: Hotel lobby, lobby private area, hotel corridor and in front of room
# Characters: IMRE (Outfit: 2), MS. ROSE (Outfit: 1), CHRIS (Outfit: 2), AMBER (Outfit: 1), LAUREN (Outfit: 3), MC (Outfit: 1), NORA (Outfit: 1)
# Time: Night

label v12_paris_hotel:
    scene v12pht1 # TPP. All students are gathered in the lobby
    with fade
    
    pause 0.75

    play music "music/v12/Track Scene 11.mp3" fadein 2

    scene v12pht2 # FPP. Looking at imre, mouth opened
    with dissolve

    imre "How do we travel for hours and end up right back at the same hotel?"

    scene v12pht2a # FPP. Looking at ms rose, mouth opened
    with dissolve

    ro "It's a chain hotel. Peace Hotels isn't just one hotel, there's hundreds of them all over the world."

    scene v12pht2
    with dissolve

    imre "Ohhhh."

    scene v12pht2b # FPP. Now looking at chris, mouth opened
    with dissolve

    ch "You know I love ya man, but you lose your marbles sometimes."

    scene v12pht2
    with dissolve

    imre "I blame it on being a good fighter, can't focus on much else."

    scene v12pht2c # FPP. Same as 2b, chris smiling
    with dissolve

    ch "Haha, good shit."

    scene v12pht3 # FPP. Chris and Imre high five
    with dissolve

    play sound "sounds/ks.mp3"

    pause 0.75

    scene v12pht2a
    with dissolve

    ro "Alright, well. It's very late and regardless of whether or not you slept on the way here, I imagine you're all very tired."
    ro "So let me get through this as smoothly as possible. Your sleeping arrangements will be the same as last time."

    scene v12pht2d # FPP. Amber looking worried, mouth opened
    with dissolve

    am "Wait, I have to be with Lauren again?"

    scene v12pht2e # FPP. Lauren looking shocked, mouth opened
    with dissolve

    la "*Shocked* Was I that bad?"

    scene v12pht2f # FPP. Same as 2d, amber smiling
    with dissolve

    am "Haha, no I'm just teasing."

    scene v12pht2e
    with dissolve

    la "Don't say things like that! I started getting self-conscious..."

    scene v12pht2a
    with dissolve

    ro "Please grab your keys from the counter and get checked in."

    if not v11_riley_roomate:
        scene v12pht4 # TPP. MC grabs the key from the counter
        with dissolve

        u "(Me and Chloe again.)"

    else:
        scene v12pht4 
        with dissolve

        u "(Me and Riley again.)"

    scene v12pht5 # TPP. MC at the counter, nora taps him on the shoulder
    with dissolve

    pause 0.75

    scene v12pht6 # TPP. MC turns arround and looks at nora
    with dissolve

    pause 1.25

    scene v12pht7 # FPP. Looking at nora, mouth closed
    with dissolve

    u "Yeah?"

    scene v12pht7a # FPP. Same as 7, nora looking uneasy, mouth opened
    with dissolve

    no "I know it's not a secret that Chris and I aren't in the best place, but it's not cool for you to be talking about it to other people."

    scene v12pht7
    with dissolve

    u "What are you talking about?"

    scene v12pht7a
    with dissolve

    no "Charli told me you've been telling him stuff about me and Chris."

    scene v12pht7
    with dissolve

    u "*Laughs*"

    scene v12pht7b # FPP. Same as 7a, nora looking mad, mouth opened
    with dissolve

    no "I don't see what's so funny."

    scene v12pht7 
    with dissolve

    u "I don't even fuck with Charli enough to say hi to him. What makes you think I'd bother to have a full on conversation with him about one of my friends?"

    if v11_kiss_nora:
        scene v12pht7b
        with dissolve

        no "Mhmm, you sure you're just a friend? We don't try to kiss our friends, remember?"

        scene v12pht7
        with dissolve

        u "*Sighs* I really thought we were past that, Nora. I wasn't trying to disrespect you."

        scene v12pht7c # FPP. Nora slight smile, mouth opened
        with dissolve

        no "*Chuckles* If you say so..."

    scene v12pht7a
    with dissolve

    no "Hmm... I will admit, it did seem odd to me that you would be talking to Charli."

    scene v12pht7
    with dissolve

    u "Yeah, very odd. Thanks for introducing me to that guy, by the way."

    scene v12pht7c
    with dissolve

    no "Haha, you're welcome."

    scene v12pht7
    with dissolve

    u "*Chuckles*"

    scene v12pht7a
    with dissolve

    no "Sorry for jumping to conclusions. My mind hasn't been all there lately. Charli was just trying to stir shit up I guess."

    scene v12pht7
    with dissolve

    u "Or trying to cause more issues between you and Chris."

    scene v12pht7a
    with dissolve

    no "There aren't many more issues we could have."

    scene v12pht7 
    with dissolve

    u "What do you mean?"

    scene v12pht7d # FPP. Nora looks arround
    with dissolve

    pause 0.75

    scene v12pht7e # FPP. Nora signals for MC to follow her, mouth opened
    with dissolve

    no "C'mon."

    scene v12pht8 # TPP. MC and nora go to a private area in the lobby
    with dissolve

    pause 0.75

    scene v12pht9 # FPP. Nora looking uneasy, mouth opened
    with dissolve

    no "I don't know how to say it, so... I'm just gonna do it."

    scene v12pht9
    with dissolve

    no "Chris and I have been dating for years now, right? It feels like we've always just been together, to the point that neither of us lived our own lives."
    no "And I'm not saying I want to break up with Chris or anything like that..."

    scene v12pht9a
    with dissolve

    scene v12pht9
    with dissolve

    no "I'm just sort of losing confidence in our relationship as it is. I feel we could've done better by getting to know ourselves before we got together."
    no "That way we actually knew the person we were getting with instead of figuring that out along the way."

    scene v12pht9a # FPP. Same as 9, mouth closed
    with dissolve

    u "Is Chris really not the same person he was when you guys first got together?"

    scene v12pht9
    with dissolve

    no "God no, he's changed a lot. He's way more confident, for one. There's been a lot of positive changes, but there's also been... other changes too."

    scene v12pht9a
    with dissolve

    u "Bad changes?"

    scene v12pht9
    with dissolve

    no "See, I wouldn't say they're bad, but just not good for me. People can call me what they want, but I like spending a lot of time with my partner, and Chris and I used to spend time together all the time."
    no "So it's not like I'm expecting anything new."

    scene v12pht9a
    with dissolve

    scene v12pht9
    with dissolve

    no "He basically just stopped giving me the amount of attention that he used to give me. If he acted the way he does now, back then, I'm not saying we wouldn't have dated..."
    no "But I wouldn't be expecting as much as I am from him. I just wish he wouldn't have changed."

    scene v12pht9a
    with dissolve

    u "Feel kinda swindled?"

    scene v12pht9
    with dissolve

    no "Something like that? But, I'm not just gonna back out you know, I do love him. I've spent most of my life with that man and I have a lot of good memories with him."

    scene v12pht9a
    with dissolve

    u "That's very loyal of you. I can only imagine how much you've been through together."

    scene v12pht9b # FPP. Nora slight smile, mouth opened
    with dissolve

    no "Haha, Chris used to be so corny."

    scene v12pht9a
    with dissolve

    u "Ha, really? That's hard to imagine."

    scene v12pht9
    with dissolve

    no "Believe it. I'm telling you, he's changed a lot as we've gotten older. He just..."

    scene v12pht9c # FPP. Nora puts her head down and wipes her eyes as if tearing up
    with dissolve

    pause 1.25

    scene v12pht9d # FPP. nora looking at mc, tear in her eyes, mouth closed
    with dissolve

    u "You okay?"

    scene v12pht9e # FPP. Same as 9d, mouth opened
    with dissolve

    no "Yeah, it's just a lot, you know? Never thought I'd be in a situation like this."

    menu:
        "Support her choice":
            $ reputation.add_point(Reputations.BOYFRIEND)
            scene v12pht9d
            with dissolve

            u "I'm not going to pick sides or try to sway you one way or the other, I don't feel like that's my place."
            u "I'm friends with both of you so, as your friend, I'm going to support any decision you make. No matter what it is."

            scene v12pht9e
            with dissolve

            no "I really appreciate that. Like for real. Thanks, [name]!"

            scene v12pht9d
            with dissolve

            u "That's what FRIENDS are for. *Chuckles*"

        "Help Chris":
            $ v12_help_chris += 1
            $ reputation.add_point(Reputations.BRO)
            scene v12pht9d
            with dissolve

            u "You know, I'm sure deep down Chris is still the exact same person you fell in love with. He's just in situations now that divide his time up in a way that they didn't before."
            u "I bet if all the other distractions weren't a factor, you'd be the only thing on his mind."

            scene v12pht9f # FPP. Same as 9e, still crying, slight smile, mouth opened
            with dissolve

            no "I'd like to believe that is true."

            scene v12pht9d
            with dissolve

            u "I'm really sure it is."

    scene v12pht9g # FPP. Nora wiping the tear off her face
    with dissolve

    pause 0.75

    scene v12pht9b 
    with dissolve

    no "Charli chose the wrong person to try and make me mad at, huh?"

    scene v12pht9h # FPP. Same as 9b, mouth closed
    with dissolve

    u "Definitely."

    scene v12pht9b 
    with dissolve

    no "Should I turn the tables and have a little \"mind your own business\" talk with him?"

    menu:
        "Yes":
            $ reputation.add_point(Reputations.TROUBLEMAKER)
            scene v12pht9h
            with dissolve

            u "You know I'd love to see that."

            scene v12pht9b
            with dissolve

            no "Haha, I'll think about it."

        "No":
            $ reputation.add_point(Reputations.BOYFRIEND)
            scene v12pht9h 
            with dissolve

            u "Haha, no. Let's just leave it alone. He technically isn't hurting anyone but himself."

            scene v12pht9b 
            with dissolve

            no "True, very true."

    scene v12pht9b
    with dissolve

    no "Well, thanks for talking to me. I'll let you get to your room, don't want your roommate freaking out."

    scene v12pht9h
    with dissolve

    u "Haha, sounds good. You know where to find me if you need me."

    scene v12pht9i # FPP. Nora leaving back turned to the camera
    with dissolve

    pause 0.75

    scene v12pht10 # TPP. MC walking off the lobby
    with dissolve

    pause 0.75

    scene v12crm1 # TPP. MC in the hotel corridor heading to his room
    with dissolve

    pause 0.75

    scene v12pht12 # TPP. MC at his hotel door
    with dissolve
    play sound "sounds/dooropen.mp3"

    pause 0.75
    stop music fadeout 3

    jump v12_room_chloe_riley #scene 12