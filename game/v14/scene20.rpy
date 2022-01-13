# SCENE 20: AUTUMN PROMOTING THE GRAND RE-OPENING OF DOG SHELTER
# Locations: School hallways
# Characters: AUTUMN (Outfit: 1), MC (Outfit: 1)
# Time: Tuesday

label v14s20:
    play music "music/v13/Track Scene 21.mp3" fadein 2

    scene v14s20_1 # FPP Show Autumn, in school hallway, handing out candy to people walking by, smiling with mouth open
    with dissolve

    aut "Please come out and support!"

    scene v14s20_1a # FPP Same angle as 1, someone taking candy and saying something to Autumn, Autumn responding, smiling with mouth open
    with dissolve

    aut "Thank you so much!"

    scene v14s20_2 # FPP Autumn seeing MC and jogging up to him, with a big smile
    with dissolve

    pause 0.75

    scene v14s20_3 # FPP Autumn standing near MC, smiling with mouth open
    with dissolve

    aut "Hey, [name]! Want some candy?"

    scene v14s20_3a # FPP Same as 3, Autumn smiling with mouth closed
    with dissolve

    u "That was a very \"get in my van\" type of thing to say..."

    scene v14s20_3b # FPP Same angle as 3, Autumn looks shocked and horrified, mouth open
    with dissolve

    aut "Oh my god, NO!"
    
    scene v14s20_3c # FPP Same angle as 3, Autumn looks embarrassed, mouth open
    with dissolve
    
    aut "I'm not kidnapping you, haha."

    scene v14s20_3a
    with dissolve

    u "*Chuckles* That's what a kidnapper would say."

    scene v14s20_3
    with dissolve

    aut "*Laughs* Not a very good one."

    scene v14s20_3a
    with dissolve

    u "Haha. So, what are you handing out candy for?"

    scene v14s20_3
    with dissolve

    aut "Oh, you remember the dog shelter I'm working for?"

    scene v14s20_3a
    with dissolve

    u "Yeah, of course."

    scene v14s20_3
    with dissolve

    aut "We're having a grand re-opening."

    scene v14s20_3a
    with dissolve

    u "When did you guys shut down?"

    scene v14s20_3
    with dissolve

    aut "We didn't really. We just had some major exterior renovations and they also renamed the place."
    aut "It took a few weeks and we wanted to have a little celebration day for the community."

    scene v14s20_3a
    with dissolve

    u "Ah, that makes sense. Sounds like a cool idea."

    scene v14s20_3
    with dissolve

    aut "Yeah, it should be fun."

    scene v14s20_3d # FPP Same angle as 3, Autumn looks excited, mouth open
    with dissolve

    aut "Oh, wow, I can't believe I didn't ask! How was the trip? *Laughs*"

    scene v14s20_3a
    with dissolve

    menu:

        "It was great":
            $ add_point(KCT.BRO)

            u "The trip was great."

            scene v14s20_3e # FPP Same angle as 3, Autumn's eyebrow raised, mouth closed
            with dissolve

            u "Drama, fun and excitement. A little dose of everything."

        "It was alright":
            $ add_point(KCT.TROUBLEMAKER)

            u "Yeah it was alright."

            scene v14s20_3e # FPP Same angle as 3, Autumn's eyebrow raised, mouth closed
            with dissolve

            u "A lot of drama, but otherwise quite fun."
    
    scene v14s20_3f # FPP Same as 3e, Autumn's mouth open
    with dissolve

    aut "*Chuckles* Lauren definitely enjoyed it. She told me about some of the things she did with Amber, and... I can tell she had a big influence on her."

    scene v14s20_3e
    with dissolve

    u "Oh yeah? How can you tell that?"

    scene v14s20_3f
    with dissolve

    aut "I know my sister as the \"risk free, never do a bad thing, sweetheart.\""
    aut "She's definitely loosened up since you guys returned and I'm sure Amber had much to do with that. *Laughs*"

    scene v14s20_3a
    with dissolve

    u "Yeah, they seem to get along surprisingly well, haha."

    if v11_lauren_caught_aubrey:
        scene v14s20_3g # FPP Same angle as 3, Autumn with neutral expression, mouth open
        with dissolve

        aut "The whole break up between you guys seemed to get her to open up."

        scene v14s20_3
        with dissolve

        aut "She didn't go into detail about what happened, but she said you guys are still friends so I'm not that concerned."

        scene v14s20_3a
        with dissolve

        u "It definitely wasn't a good day. Not proud of some of the decisions I made but, we're still there for each other."

        scene v14s20_3
        with dissolve

        aut "I'm glad to hear that. My sister's first real boyfriend wasn't a complete dickhead... Phew! *Laughs*"

        scene v14s20_3a
        with dissolve

        u "Not completely..."

    elif lauren.relationship >= Relationship.GIRLFRIEND:
        scene v14s20_3f
        with dissolve

        aut "You probably had something to do with it as well. She has been talking a bit more... especially since you guys returned."

        scene v14s20_3
        with dissolve

        aut "You guys have been together for a while now, right? How are you feeling about the relationship so far?"

        scene v14s20_3a
        with dissolve

        menu:
            "I love her":
                $ add_point(KCT.BOYFRIEND)

                u "I love your sister, Autumn. I honestly couldn't imagine being with anyone other than Lauren."

                scene v14s20_3
                with dissolve

                aut "And to think I bumped into you first on day one... Guess I found my sister's boyfriend for her."

                scene v14s20_3a
                with dissolve

                u "Haha, yeah. I guess you did."

                scene v14s20_3d
                with dissolve

                aut "Anyways, I'm really glad to hear that. This is good for her."

                scene v14s20_3
                with dissolve

                aut "You're good for her."

                scene v14s20_3a
                with dissolve

                u "Thanks, I appreciate it."

                scene v14s20_3
                with dissolve

                aut "Of course."

            "It's going great":
                $ autumn.points += 1
                $ AutumnTrust = True

                scene v14s20_3a
                #with dissolve
                
                u "It's going great so far."

                scene v14s20_3
                with dissolve

                aut "That's good to hear. The way she talks about you tells me that you're a pretty trustworthy person."

                scene v14s20_3a
                with dissolve

                u "Of course. I try to be."

                scene v14s20_3
                with dissolve

                aut "*Chuckles*"

    else: # -If LaurenFriend
        scene v14s20_3a
        with dissolve

        u "Amber is a wild card, we all definitely have fun with her. There's no doubt about that, haha."

        scene v14s20_3e
        with dissolve

        u "That girl can give anyone a good time, but she's very influential. She knows how to..."

        u "...lure other people to the dark side. If you know what I mean."

        scene v14s20_3f
        with dissolve

        aut "I definitely get what you're saying. *Chuckles*"

        scene v14s20_3a
        with dissolve

        u "Lauren's great at handling peer pressure, though."

        scene v14s20_3
        with dissolve

        aut "I'm glad to hear that. But, I don't worry much about her anymore. She's become very independent since the start of the semester."

        scene v14s20_3a
        with dissolve

        u "Yeah, she has."

    # -Continue regardless of everything
    scene v14s20_3
    with dissolve

    aut "So... The re-opening is on Saturday, don't forget!"

    scene v14s20_3a
    with dissolve

    u "Was that an invitation?"

    scene v14s20_3
    with dissolve

    aut "It is now... *Laughs*"

    scene v14s20_3a
    with dissolve

    u "You two are nothing alike."

    scene v14s20_3d
    with dissolve

    aut "We are too!"

    scene v14s20_3a
    with dissolve

    u "Haha, how? You look nothing alike and your personalities are black and white."

    scene v14s20_3f
    with dissolve

    aut "Well... maybe one of us is adopted? That would be the shock of the century."

    scene v14s20_3e
    with dissolve

    u "Indeed it would. Your parents would have some explaining to do..."

    scene v14s20_3
    with dissolve

    aut "*Laughs* It's so weird but, you remind me of my childhood friend, Hero."

    scene v14s20_3a
    with dissolve

    u "Hero? His name was Hero?"

    scene v14s20_3
    with dissolve

    aut "Yes! Even we thought it was a really unique name at first, haha. Cool, huh?"

    scene v14s20_3a
    with dissolve

    u "Hell yeah it's cool. No one else is named that. *Laughs*"

    scene v14s20_3
    with dissolve

    aut "His parents used to say they knew he'd never be mistaken for someone else and that's why they liked the name at first. *Chuckles*"

    scene v14s20_3g
    with dissolve

    aut "Plus, before Hero was born, his parents were told that they were infertile, and couldn't have kids."

    scene v14s20_3
    with dissolve

    aut "Which obviously crushed their spirits. But magically, one day his mother was pregnant and nine months later came their hero. *Chuckles*"

    scene v14s20_3a
    with dissolve

    u "Holy shit... That's such a good story."

    scene v14s20_3
    with dissolve

    aut "I only tell good stories."

    scene v14s20_3a
    with dissolve

    u "*Laughs* You know, I don't think I've ever seen you hang out with anyone."

    scene v14s20_3c
    with dissolve

    aut "Oh, please... I have."

    scene v14s20_3a
    with dissolve

    u "I've literally never seen you with anyone. Besides Lauren. Maybe."

    scene v14s20_3g
    with dissolve

    aut "I really don't have many friends, and it's mostly by choice."

    scene v14s20_3h # FPP Same as 3g, Autumn's mouth closed
    with dissolve

    u "How come?"

    scene v14s20_3g
    with dissolve

    aut "Well, I had a friend. The one I just told you about- Hero."

    scene v14s20_3h
    with dissolve

    u "Do you still hang out together?"

    scene v14s20_3
    with dissolve

    aut "Oh, fuck no. Excuse my language, haha. But, he and I had a pretty bad falling out."

    scene v14s20_3a
    with dissolve

    u "Over what? Wait, sorry if you weren't wanting to talk about this."

    scene v14s20_3c
    with dissolve

    aut "Ha, it's okay. I'd rather not, though."

    scene v14s20_3h
    with dissolve

    u "I understand, completely."

    scene v14s20_3
    with dissolve

    aut "Thanks."

    scene v14s20_3f
    with dissolve

    aut "You know, it's kinda odd that you and I haven't gotten to know each other very well yet."

    scene v14s20_3e
    with dissolve

    u "With me being close as I am to Lauren, yeah. It is a bit odd, isn't it?"

    scene v14s20_3f
    with dissolve

    aut "Ha, yeah... Well, umm-"

    scene v14s20_3e
    with dissolve

    menu:
        "We should hang out more":
            $ add_point(KCT.TROUBLEMAKER)
            u "We should just hang out more. *Chuckles*"

            scene v14s20_3
            with dissolve

            aut "You think so?"

            scene v14s20_3a
            with dissolve

            u "Yeah, I do."

            scene v14s20_4 # TPP Autumn makes eye contact with MC, Autumn's mouth closed
            with dissolve

            pause 0.75

            scene v14s20_4a # TPP Same angle as 4, Autumn looking away from MC, she looks embarrased, mouth open
            with dissolve

            aut "Me too."

            scene v14s20_3
            with dissolve

            aut "So, I might shoot you a text on Friday and see if you're free? For the event on Saturday?"

            scene v14s20_3a
            with dissolve

            u "I'll be waiting by the phone."

            scene v14s20_3
            with dissolve

            aut "Haha, sounds like you need some more friends too."

            scene v14s20_3a
            with dissolve

            u "Nope, I've got plenty... Just don't have you."

            scene v14s20_3i # FPP Same angle as 3, Autumn blushes and looks embarrassed, looks down, smiles and bites her lower lip
            with dissolve

            pause 0.75

            scene v14s20_3a
            with dissolve

            u "Yeah, see ya."

        "It was nice catching up":
            $ add_point(KCT.BOYFRIEND)
            u "It was really nice catching up with you, but I actually need to hurry. I've got this thing..."

            scene v14s20_3
            with dissolve

            aut "Oh, right, yeah! Don't let me make you late, go ahead."

            scene v14s20_3a
            with dissolve

            u "*Chuckles* Thanks."

            u "Yeah, see ya."

    # -Regardless of everything scene continued

    scene v14s20_5 # FPP Show Autumn walking off down the hall toward more people
    with dissolve

    u "(She was extremely upbeat. She's either happy about this grand re-opening or happy about something else... Or maybe even someone else, hehe.)"

    scene v14s20_6 # TPP Show MC walking out of the school
    with dissolve

    pause 0.75

    stop music fadeout 3
    if chloe.relationship >= Relationship.FWB and v14_talk_to_chris:
        jump v14s21

    else:
        jump v14s21b