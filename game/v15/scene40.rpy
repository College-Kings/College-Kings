# SCENE 40: Limo Ride Back Sebastian or Grayson
# Locations: Inside of the Limo
# Characters: AUTUMN (Outfit: 3), MC (Outfit: 10)
# Time: Night
# Render Count: 4 Unique 18 Total

label v15s40:
    scene v15s40_1 # FPP. Show just Autumn sitting beside Mc in the back of the Limo, Autumn has a slight smile, mouth open looking towards the front og the Limo at the other people, Don't show any other characters
    with dissolve

    aut "Haha, look at them all."

    scene v15s40_1a # FPP. same as v15s40_1 Show Autumn looking directly at Mc, still a slight smile, mouth is still closed.
    with dissolve

    u "I guess they're just not as hardcore as us."

    scene v15s40_1b # FPP. same as v15s40_1a Autumn's mouth is open, still looking at Mc, still a slight smile
    with dissolve

    aut "It's a curse really, haha."

    scene v15s40_2 # TPP. Show just Autumn and Mc sitting in the back of the Limo, looking at each other full smiles, mouths are closed
    with dissolve

    pause 0.75

    scene v15s40_1a
    with dissolve

    u "So... What you mentioned earlier, during the limo ride to the club..."

    scene v15s40_1b
    with dissolve

    aut "My sexuality?"

    scene v15s40_1a
    with dissolve

    u "Yeah. And sorry if you don't want to like-"

    u "I mean, it's okay if you don't want to talk about it, but they're all asleep now and it's only me."

    if autumn.relationship.value < Relationship.TRUST.value:
        scene v15s40_1b
        with dissolve

        aut "I think I've talked about it enough for today."

        scene v15s40_1a
        with dissolve

        u "Yeah, I get it. It's no problem at all."

        scene v15s40_1b
        with dissolve

        aut "I get that you have questions. I just need more time to process things, I guess."

        scene v15s40_1a
        with dissolve

        u "Absolutely. I understand."

        scene v15s40_1b
        with dissolve

        aut "Thanks."

        scene v15s40_1a
        with dissolve

        u "So, you had fun tonight at the club?"

        scene v15s40_1c # FPP. same as v15s40_1b Autumn increases to a full smile, still looking at Mc, mouth is still open
        with dissolve

        aut "Yeah! I've haven't danced like that in way too long..."

        aut "Solid company too. Aubrey and Lindsey are a lot of fun!"

        scene v15s40_1a
        with dissolve

        u "Yeah, they're great."

        if not v15_lindsey_inviteseb:
            scene v15s40_1c
            with dissolve

            aut "Grayson, not so much, haha."

            scene v15s40_1a
            with dissolve

            u "He's a bit... bittersweet, huh?"

            scene v15s40_1b
            with dissolve

            aut "That's a very polite way of putting it. *Giggles*"

        else:
            scene v15s40_1
            with dissolve

            aut "And Sebastian... He's such a nice guy."

            scene v15s40_1a
            with dissolve

            u "Yeah, he's one of those people that just seems to fit into any crowd."

            scene v15s40_1b
            with dissolve

            aut "Yeah, that's exactly it! It's a good skill to have too."

    else:
        scene v15s40_1b
        with dissolve

        aut "We can talk about it. It's been on my mind a lot, too."

        aut "And I was thinking about what Aubrey said."

        scene v15s40_1a
        with dissolve

        u "What's that?"

        scene v15s40_1d # FPP. same as v15s40_1b Autumn face is slightly turned away from mc looking away from mc, slightly embarrassed, mouth is still open
        with dissolve

        aut "About you being a good guy to lose my virginity to..."

        scene v15s40_1e # FPP. same as v15s40_1d Autumn is looking back at Mc, blushing even more, her face is still slightly turned away from Mc, mouth is still open
        with dissolve

        aut "I do like you, [name]. I like you a lot, actually..."

        scene v15s40_1f # FPP. same as v15s40_1e Autumn is now looking directly at Mc, mouth is closed, still slightly embarrased, still blushing
        with dissolve

        u "(Oh shit.)"

        scene v15s40_1g # FPP. same as v15s40_1f Autumn's mouth is open, no longer blushing, still slightly embarrsed, still looking at Mc
        with dissolve

        aut "And I think if I were to do it with anyone, I'd choose you."

        scene v15s40_1a
        with dissolve

        u "O-oh, that's..."

        scene v15s40_1b
        with dissolve

        aut "Ha, yeah? What do you think?"

        scene v15s40_1a
        with dissolve

        menu:
            "I'd like that":
                scene v15s40_1a
                with dissolve

                u "Yeah, I mean, I'd be happy to."

                if lauren.relationship.value >= Relationship.GIRLFRIEND.value:
                    $ autumn.relationship = Relationship.LOYAL

                    scene v15s40_1b
                    with dissolve

                    aut "Yeah. *Sighs* But you're dating my sister, so it's never going to happen."

                    scene v15s40_1a
                    with dissolve

                    u "Yeah, I'm flattered... I really am, but I'm with Lauren."

                    scene v15s40_1b
                    with dissolve

                    aut "And I love that my sister found such a great guy."

                    scene v15s40_1c
                    with dissolve

                    aut "Just wish I would have made my move the minute we met. Like finder's keepers. *Chuckles*"

                    scene v15s40_1a
                    with dissolve

                    u "Damn... Too bad you haven't built a time machine yet."

                    scene v15s40_1b
                    with dissolve

                    aut "Ha... Right."

                    scene v15s40_1a
                    with dissolve

                    u "Well, thank you, I appreciate it. I'm grateful that Lauren has such an amazing sister."

                    scene v15s40_1b
                    with dissolve

                    aut "Haha, thanks..."

                else:
                    $ autumn.relationship = Relationship.FWB

                    scene v15s40_1a
                    with dissolve

                    u "I'd really like that, Autumn."

                    scene v15s40_1h # FPP. same as v15s40_1b Autumn looks slightly shocked with excitement, still looking ta Mc, mouth is still open
                    with dissolve

                    aut "Wait, really?"

                    scene v15s40_1e
                    with dissolve

                    aut "Ha... That's such a relief. I was so nervous to ask, haha!"

                    scene v15s40_1f
                    with dissolve

                    u "What? I'd be crazy not to feel the same way. We get along so well."

                    scene v15s40_1b
                    with dissolve

                    aut "*Chuckles* Thank you..."

                    scene v15s40_1a
                    with dissolve

                    u "Of course, haha. Since the moment we met on the stairs, I pretty much knew we'd cross paths again eventually."

                    scene v15s40_2
                    with dissolve

                    pause 0.75

                    scene v15s40_2a # TPP. same as v15s40_2 Autumn puts a hand on Mc's chest and leans in to give Mc a slight kiss
                    with dissolve

                    pause 0.75

                    scene v15s40_2b # TPP. same as v15s40_2a Autumn pulls back and is now blushing head facing slightly down looking up at Mc slight smile mouth is closed, Mc has a hand on Autumns cheek looking at Autumn, slight smile, mouth is closed.
                    with dissolve

                    pause 0.75

                    scene v15s40_2c # TPP. same as v15s40_2b Mc pulls Autumn closer for a passionate kiss his hand gently carressing the back of her head pulling her closer, Autumns hand is carressing Mc's throat
                    with dissolve

                    pause 0.75

                    scene v15s40_1b
                    with dissolve

                    aut "Well, there's a start."

                    scene v15s40_1a
                    with dissolve

                    u "Of something new..."

                    scene v15s40_1c
                    with dissolve

                    aut "Hehe! You did not just reference that movie..."

                    scene v15s40_1a
                    with dissolve

                    u "So, what if I did? Huh?"

                    scene v15s40_2d # TPP. same as v15s40_2 Mc and Autumn laugh, still looking at each other
                    with dissolve

                    pause 0.75

            "It's not a good idea":
                scene v15s40_1a
                with dissolve

                u "I like you too, Autumn. But, as friends."

                scene v15s40_1b
                with dissolve

                aut "Yeah, of course."

                scene v15s40_1a
                with dissolve

                u "I think we have a lot of fun when we hang out together. And I don't want to ruin that."

                scene v15s40_1b
                with dissolve

                aut "You're right. We do have fun."

                scene v15s40_2
                with dissolve

                pause 0.75

                scene v15s40_1b
                with dissolve

                aut "Okay, we can keep it like this. Thanks for being honest, it means a lot"

                if lauren.relationship.value >= Relationship.GIRLFRIEND.value:
                    scene v15s40_1c
                    with dissolve

                    aut "You're going out with my sister anyway, ha! So yeah, nothing can happen."
            
        scene v15s40_1b
        with dissolve

        aut "Let's hang out again soon, okay?"

        scene v15s40_1a
        with dissolve

        u "Definitely. I'm already looking forward to it."

        scene v15s40_1c
        with dissolve

        aut "Haha, good."

    scene v15s40_1i # FPP. same as v15s40_1 Autumn turns her head to look out the Limo's window, slight smile, mouth is closed
    with dissolve

    pause 0.75

    scene v15s40_1b
    with dissolve

    aut "Oh, it looks like we're here. This is my stop."

    aut "Goodnight, [name]."

    scene v15s40_1a
    with dissolve

    u "Goodnight, Autumn."

    scene v15s40_3 # TPP. Show Autumn exiting the Limo, she is looking back and waving goodbye to Mc who is still sitting inside the Limo, both slight smiles, both mouths are closed
    with dissolve

    pause 0.75

    if autumn.relationship.value == Relationship.FWB.value:
        scene v15s40_4 # TPP. Autumn leans back into the limo to give Mc a kiss on the cheek, Mc slight smile mouth is closed
        with dissolve

        pause 0.75

    scene v15s40_3a # TPP. Autumn is walking away from the Limo slight smile mouth is closed, Mc is looking at Autumn slight smile mouth is closed
    with fade

    pause 0.75

    jump v15s41