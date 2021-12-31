# SCENE 36: MC walks Autumn back to Deers House
# Locations: Streets to Deer House
# Characters: AUTUMN (Outfit: 1), MC (Outfit: 2)
# Time: Night

label v15s36:
    scene v15s36_1 # TPP. Shot of MC and Autumn walking down the street, both slight smile, mouth closed.
    with fade

    pause 0.75

    scene v15s36_2 # FPP. MC and Autumn walking down the street, MC looking at Autumn, Autumn looking at MC, Autumn slight smile, mouth open.
    with dissolve

    aut "Tonight was so much fun!"

    scene v15s36_2a # FPP. MC and Autumn walking down the street, Houses in the background, MC looking at Autumn, Autumn looking at MC, Autumn slight smile, mouth closed.
    with dissolve

    u "Absolutely. The game, the drinks, and of course... The company. *Chuckles*"

    scene v15s36_2
    with dissolve

    aut "Haha, we make a good foursome."

    scene v15s36_2a
    with dissolve

    u "Oh-"

    scene v15s36_2
    with dissolve

    aut "And not in a sexual way! Before you say anything, haha."

    scene v15s36_3 # TPP. Closer up shot of MC and Autumn further down the street smiling at each other as they walk, both mouth closed.
    with dissolve

    pause 0.75

    scene v15s36_4 # FPP. MC and Autumn further down the street, new set of houses in the background, MC looking at Autumn, Autumn looking at MC, Autumn slight smile, mouth closed.
    with dissolve

    u "So... I don't know if it's up for conversation, but..."

    scene v15s36_4a # FPP. MC looking at Autumn, Autumn looking at MC, Autumn slight smile, mouth open.
    with dissolve

    aut "You're going to ask about my sexuality, aren't you?"

    scene v15s36_4
    with dissolve

    menu:
        "Oh no, I wasn't":
            $ add_point(KCT.BRO)
            u "Oh no, I wasn't. Actually I wanted to know what your favorite question from tonight was."

            jump v15s36_dontask

        "I'm really curious":
            $ add_point(KCT.BOYFRIEND)
            u "Well, I'm curious about getting to know the real Autumn, but I know it's a sensitive issue."

    u "Only if you're comfortable talking about it, of course."

    if autumn.relationship.value < Relationship.TRUST.value:
        scene v15s36_4a
        with dissolve

        aut "I get it, you've got questions, ha."

        aut "I'm just done talking about it for today."

        scene v15s36_4
        with dissolve

        u "Oh, okay. Sure. Sorry for-."

        scene v15s36_4a
        with dissolve

        aut "No, it's fine, really. I just need time to think about it all, you know. Maybe another time."

        scene v15s36_4
        with dissolve

        u "Yeah, I get that. No worries..."

        u "So, what was your favorite question from the game tonight?"

        label v15s36_dontask:

        scene v15s36_5 # FPP. MC and Autumn further down the street, new set of houses in the background, MC looking at Autumn, Autumn looking at MC, Autumn slight smile, mouth open.
        with dissolve

        aut "Oh! Umm, let me think... There were some really crazy ones, haha."

        scene v15s36_5a # FPP. MC looking at Autumn, Autumn looking at MC, Autumn slight smile, mouth closed.
        with dissolve

        u "*Laughs*"

        if v15_lindsey_mostlikelyto:
            scene v15s36_5
            with dissolve

            aut "The one about getting shit-face drunk and waking up on the other side of the country, haha."

            scene v15s36_5a
            with dissolve

            u "*Laughs* Because everyone said it would be me?"

            scene v15s36_5
            with dissolve

            aut "It's only a matter of time. *Giggles*"

            scene v15s36_5a
            with dissolve

            u "I can see you all taking bets on what state I'll wake up in."

            scene v15s36_5
            with dissolve

            aut "A drunken state... Haha!"

            scene v15s36_5a
            with dissolve

            u "Wow... Good one. Haha, I was going to say Missouri."

            scene v15s36_5
            with dissolve

            aut "Okay... That was way worse than my cheesy joke..."

            scene v15s36_6 # TPP. Show MC and Autumn laughing while looking at each other now further down the street.
            with dissolve

            pause 0.75

        else:
            scene v15s36_5
            with dissolve

            aut "It's gotta be the frogs, haha."

            aut "Little frog adventures? Sign me up!"

            scene v15s36_5a
            with dissolve

            u "Ha, what's so good about being a frog?"

            scene v15s36_5
            with dissolve

            aut "Everything! I wouldn't care if it rained..."

            scene v15s36_5a
            with dissolve

            u "And you could breathe underwater..."

            scene v15s36_5
            with dissolve

            aut "Mhmm... And jumping ability!"

            scene v15s36_5a
            with dissolve

            u "Okay, yeah. You're right. Frogs are kinda sick."

            scene v15s36_5
            with dissolve

            aut "Haha, exactly! Just don't let any of the actual frogs hearing you say that..."

            scene v15s36_5a
            with dissolve

            u "*Laughs* Good advice, thanks."

    else:
        scene v15s36_4a
        with dissolve

        aut "It's okay. We can talk about it."

        aut "To be honest, I've been thinking about it a lot."

        scene v15s36_4
        with dissolve

        u "Really? In what way?"

        scene v15s36_4a
        with dissolve

        aut "Well, it would be interesting to at least consider losing my virginity to someone. Then I'd know exactly how I feel."

        aut "I won't be left wondering, you know."

        scene v15s36_4
        with dissolve

        u "Yeah... I can understand that."

        scene v15s36_4a
        with dissolve

        aut "And if anybody ever asks, I can say... Yes! More sex please! Haha... Or just, meh... It's not for me."

        scene v15s36_4
        with dissolve

        u "*Laughs* I think that's a good way to go about it, but only if you're ready, you know?"

        scene v15s36_4a
        with dissolve

        aut "Yeah. Exactly. And I think..."

        aut "I think you'd be the right person to do it with."

        scene v15s36_4
        with dissolve

        u "(What?)"

        scene v15s36_4a
        with dissolve

        aut "We seem to get along really well, and I like your company."

        scene v15s36_4
        with dissolve

        u "(Is Autumn admitting that... She wants to have sex with me?!)"

        u "Yeah, I mean... I really like hanging out with you too."

        scene v15s36_4a
        with dissolve

        aut "So, what do you think about it?"

        scene v15s36_5a
        with dissolve

        menu:
            "I'd like that":
                u "Honestly, I'd really like that... I feel the same way."

                if lauren.relationship.value >= Relationship.GIRLFRIEND.value:
                    $ autumn.relationship = Relationship.LOYAL
                    scene v15s36_5
                    with dissolve

                    aut "Yeah, but... I know what you're going to say."

                    aut "You're dating Lauren, so obviously it's never going to happen. *Sighs*"

                    scene v15s36_5a
                    with dissolve

                    u "I'm flattered, truly. But, yeah... I'm dating your sister, ha."

                    scene v15s36_5
                    with dissolve

                    aut "Ha... Yeah."

                    aut "I'm really happy that she found such a great guy. It's just a shame that we can't clone you, haha."

                    scene v15s36_5a
                    with dissolve

                    u "Haha, thanks, Autumn. You're also an amazing person."

                    u "I'm sure you'll find someone as good as me one day... *Chuckles*"

                    scene v15s36_5
                    with dissolve

                    aut "Haha! Okay, mister... Don't push it."

                    scene v15s36_6
                    with dissolve

                    pause 0.75

                else:
                    $ autumn.relationship = Relationship.FWB

                    scene v15s36_5
                    with dissolve

                    aut "Wait, really? I was so nervous to ask... *Giggles*"

                    scene v15s36_5a
                    with dissolve

                    u "Haha, don't you remember? You were the very first person I met when I arrived at SVC."

                    scene v15s36_5
                    with dissolve

                    aut "Hehe, yeah. I was totally oblivious to your charm..."

                    scene v15s36_5a
                    with dissolve

                    u "My charm? Well, well, well..."

                    scene v15s36_5
                    with dissolve

                    aut "I just can't believe it took this long for me to catch up..."

                    scene v15s36_7 # TPP. Show Autumn and MC stopped on the side walk looking at each other both slight smile, mouth closed.
                    with dissolve

                    pause 0.75

                    scene v15s36_8 # FPP. MC and Autumn further down the street, new set of houses in the background, MC and Autumn standing still on the side walk, MC looking at Autumn, Autumn looking down at the ground, Autumn biting her lip. 
                    with dissolve

                    pause 0.75

                    scene v15s36_8a # FPP. MC looking at Autumn, Autumn looking at MC, Autumn nervous smile, mouth open.
                    with dissolve

                    aut "It all starts with a kiss, right?"

                    scene v15s36_8b # FPP. MC looking at Autumn, Autumn looking at MC, Autumn stepped closer to MC, Autumn flirty, mouth closed.
                    with dissolve

                    pause 0.75

                    play sound "sounds/kiss.mp3"

                    scene v15s36_8c # FPP. Autumn kissing MC 
                    with dissolve

                    pause 0.75

                    scene v15s36_8d # FPP. Autumn stepped back again, MC looking at Autumn, Autumn looking at Mc, Autumn biting her lip.
                    with dissolve

                    pause 0.75

                    scene v15s36_8b 
                    with dissolve

                    pause 0.75

                    play sound "sounds/kiss.mp3"

                    scene v15s36_9 # TPP. MC and Autumn kissing on the sidewalk, MC with his hands on Autumn's waist, Autumn's arms wrappped around MC's neck.
                    with dissolve

                    pause 0.75

                    scene v15s36_8e # FPP. Autumn stepped back, MC looking at Autumn, Autumn looking at MC, Autumn slight smile, mouth closed. 
                    with dissolve

                    u "And so it begins..."

                    scene v15s36_8f # FPP. Autumn stepped back, MC looking at Autumn, Autumn looking at MC, Autumn now blushing, Autumn slight smile, mouth closed. 
                    with dissolve

                    pause 0.75

            "It's not a good idea":
                $ v15s36_not_good_idea = True

                scene v15s36_5a
                with dissolve

                u "I do like you, Autumn... I just don't think we should be anything more than friends, you know."

                scene v15s36_5b # FPP. MC looking at Autumn, Autumn looking at MC, Autumn embarassed, Autumn slight frown, mouth closed. 
                with dissolve

                u "We have a lot of fun when we hang out, there's no expectations. I'd prefer to keep it like that."

                scene v15s36_5c # FPP, MC looking at Autumn, Autumn looking at MC, Autumn embarassed, Autumn slight frown, mouth open.
                with dissolve

                aut "Yeah, you're not wrong there. We do have a lot of fun. Why mess that up, right?"

                scene v15s36_5b
                with dissolve

                u "Right, yeah. I'm sorry if-"

                scene v15s36_5c
                with dissolve

                aut "No, no. There's nothing to apologize for. You're right, and thanks for being honest."

                if lauren.relationship.value >= Relationship.GIRLFRIEND.value:
                    scene v15s36_5
                    with dissolve

                    aut "You're literally dating my sister anyway, so... Nothing can happen between us, ha."

                    scene v15s36_5a
                    with dissolve

                    u "Exactly."

                scene v15s36_5
                with dissolve

                aut "Well, I'm going to see you again soon, yeah?"

                scene v15s36_5a
                with dissolve

                u "Definitely. I'm already looking forward to it."

                scene v15s36_5
                with dissolve

                aut "Haha, me too."

    scene v15s36_10 # TPP. Show MC and Autumn arriving at the Deer's house front.
    with fade 

    pause 0.75

    scene v15s36_11 # FPP. MC and Autumn at the front of the Deer's house, Autumn looking at MC, MC looking at Autumn, Autumn slight smile, mouth open.
    with dissolve

    aut "Here we are... Thanks for walking me home."

    scene v15s36_11a # FPP. MC and Autumn at the front of the Deer's house, Autumn looking at MC, MC looking at Autumn, Autumn slight smile, mouth open.
    with dissolve

    u "Anytime! Just call me."

    scene v15s36_11
    with dissolve

    aut "Hehe, goodnight, [name]."

    scene v15s36_11a
    with dissolve

    u "Goodnight, Autumn."

    scene v15s36_11b # FPP. Show Autumn walking away to the deer's house.
    with dissolve

    pause 0.75

    if autumn.relationship.value >= Relationship.FWB.value:
        scene v15s36_11c # FPP. Show Autumn stopping in place.
        with dissolve

        pause 0.75

        scene v15s36_11d # FPP. Show Autumn walking back towards MC, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s36_11a 
        with dissolve

        pause 0.75

        scene v15s36_11e # FPP. Autumn kissing MC on the cheek.
        with dissolve

        pause 0.75

        play sound "sounds/dooropen.mp3"

        scene v15s36_11f # FPP. Autumn opening the door to the Deer's house and walking in.
        with dissolve

        pause 0.75

        play sound "sounds/doorclose.mp3"

        scene v15s36_11g # FPP. The door closing behind Autumn as she enters.
        with dissolve

        pause 0.75

    jump v15s37
