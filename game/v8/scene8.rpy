# Protest with Autumn
# Location: Protest Street
# Outfits: MC outfit 3, Autumn outfit 1, Evelyn outfit 3
# Time: Saturday Afternoon

label prot_w_au:
    scene v8sprot1 # FPP. Sweeping shot of the protest, lots of people holding signs, Autumn also in the protest holding a sign.
    with Fade(0.75, 0.25, 0.75)

    pause 1.5

    scene v8sprot2 # FPP. Camera now closer to the proest, Autumn turns around and looks at camera, waving her arms, Autumn smile.
    with dissolve

    pause 0.5

    play music "music/mindie5.mp3" fadein 2
    queue music "music/mfunk.mp3"

    scene v8sprot3 # FPP. Close up of Autumn, Autumn smile, mouth open.
    with dissolve

    aut "Hey, hey! You showed."

    scene v8sprot3a # FPP. Same camera as v8sprot3, Autumn smile, mouth closed.
    with dissolve

    u "Said I'd be here."

    scene v8sprot3
    with dissolve

    aut "You did!"

    scene v8sprot3a
    with dissolve

    u "You got my sign?"

    scene v8sprot4 # TPP. Show MC stood opposite Autumn, Autumn hands MC the sign he made previously with Autumn, both smiling, mouths closed.
    with dissolve

    pause 0.5

    scene v8sprot3
    with dissolve

    aut "Yup."

    scene v8sprot5 # FPP. Show MC taking a closer look at the sign in his hands.
    with dissolve

    u "Yeah, looks better than I remembered. Haha."

    scene v8sprot3
    with dissolve
    aut "Well, it's more about the message anyway."

    scene v8sprot3a
    with dissolve
    u "Yeah that's true."

    scene v8sprot6 # TPP. Show MC taking a look around at all the people at the protest, MC looks slightly nervous, mouth closed.
    with dissolve
    pause 1

    scene v8sprot3
    with dissolve
    aut "Ready?"

    scene v8sprot3a
    with dissolve

    menu:
        "Pretend you know what you're doing":
            $ add_point(KCT.TROUBLEMAKER)
            jump prot_w_au_wing

        "Ask what you need to do":
            $ add_point(KCT.BOYFRIEND)
            jump prot_w_au_no_wing

label prot_w_au_wing:

    u "Yeah, of course."

    scene v8sprot7 # TPP. Show MC waving his sign around in the air, mouth closed, Autumn looking at MC, impressed, mouth closed.
    with dissolve

    pause 0.5

    scene v8sprot7a # TPP. Same camera as v8sprot7, mouth open as if shouting, Autumn looking at MC, impressed, mouth closed.
    with dissolve

    u "We won't stop, until it's fair. We won't stop until it's fair."

    scene v8sprot3b # FPP. Same camera as v8sprot3, Autumn looking impressed, mouth open.
    with dissolve

    aut "So you have done this before?"

    scene v8sprot3c # FPP. Same camera as v8sprot3, Autumn looking impressed, mouth closed.
    with dissolve

    u "Yeah, of course. That's how you get the word out."

    scene v8sprot3b
    with dissolve

    aut "Do you protest a lot?"

    scene v8sprot3c
    with dissolve

    u "When I can. As much as I can I mean."

    scene v8sprot3
    with dissolve

    aut "That's good. It's nice to know people who are knowledgeable in politics and the issues we still face in society everyday."

    scene v8sprot3a
    with dissolve

    u "Like I said, we won't stop until it's fair."

    jump prot_w_au_1

label prot_w_au_no_wing:

    u "Uhh... so it's been a while for me. How does this work again?"

    scene v8sprot3
    with dissolve

    aut "Haha that's okay. Is this your first time?"

    scene v8sprot3a
    with dissolve

    u "No, no I--"

    scene v8sprot3
    with dissolve

    aut "It's okay. We're just here to make our voices heard, that's all."

    scene v8sprot8 # FPP. Show Autumn holding up her sign facing the camera, mouth closed.
    with dissolve

    ###CHECK - removed because of missing image
    # pause 0.5
    #
    # scene v8sprot8a # FPP. Same camera as v8sprot8, but Autumn mouth open
    # with dissolve

    aut "And really you just say whatever you like, as long as it has a purpose. Haha. Watch. We won't stop until we're heard!"

    scene v8sprot3
    with dissolve

    aut "See? Really not much to it."

    scene v8sprot3a
    with dissolve

    u "Yeah. Haha. I should've known."

    scene v8sprot3
    with dissolve

    aut "It can be a bit overwhelming at first, but always remember why we're here."

    scene v8sprot3a
    with dissolve

    u "Thanks."

    jump prot_w_au_1

label prot_w_au_1:

    scene v8sprot3d # FPP. Same camera as v8sprot3, Autumn looking serious, mouth open.
    with dissolve

    aut "Have you heard about the new legislation being proposed on abortions?"

    scene v8sprot3e # FPP. Same camera as v8sprot3, Autumn looking serious, mouth closed.
    with dissolve

    menu:
        "Pretend you know about it":
            $ add_point(KCT.TROUBLEMAKER)
            jump prot_w_au_leg
        "Admit you don't know":
            jump prot_w_au_no_leg

label prot_w_au_leg:

    u "Yeah, pretty insane if you ask me. Abortion, such a horrible thing."

    scene v8sprot3f # FPP. Same camera as v8sprot3, Autumn looking shocked, mouth open.
    with dissolve

    aut "You're against abortion?"

    scene v8sprot9 # FPP. Close up MC, looking confused, mouth open.
    with dissolve

    u "Uhh-- I mean--"

    scene v8sprot3d
    with dissolve

    aut "You mean you meant you're against the anti-abortion legislation."

    scene v8sprot3e
    with dissolve

    u "Yeah, that's what I meant."

    scene v8sprot3d
    with dissolve

    aut "It's crazy that government officials, especially considering that they're all mostly men, think they can have a say in what a woman does with their body."

    scene v8sprot3e
    with dissolve

    u "Fucked up."

    ###CHECK - removed because of missing image
    # scene v8sprot10 # TPP. Show shot of protestors protesting.
    # with dissolve

    scene v8sprot8
    with dissolve

    aut "And that's why we're here right? To tell them that our bodies are our choice. We can't keep letting men think they have the say over everything."

    scene v8sprot3a
    with dissolve

    u "Yeah. It's all about equality. You're right. Woman weren't made to serve men. We're all our own people."

    scene v8sprot3
    with dissolve

    aut "Exactly! Glad you understand. Like I said before, really nice knowing guys who have a say in the woman's rights movement. It's not often you find guys who are willing to stand by woman and fight with them."

    scene v8sprot3a
    with dissolve

    u "And that's how you create a movement. One by one until everyone's on board."

    scene v8sprot3
    with dissolve

    aut "Yeah."

    jump prot_w_au_2

label prot_w_au_no_leg:
    u "Honestly, I have no idea."

    scene v8sprot3f
    with dissolve

    aut "Oh, so you haven't heard?"

    scene v8sprot9
    with dissolve

    u "Yeah I guess I just had a lot going on lately. I wasn't able to keep up with the news as much."

    scene v8sprot3d
    with dissolve

    aut "Well I can fill you in... It's disgusting. A bunch of misogynistic men and political officials introduced legislation to try and make abortions illegal."

    scene v8sprot3e
    with dissolve

    u "They can do that?"

    scene v8sprot3d
    with dissolve

    aut "Not if we have a say. The issue is in the conservative states. They're typically religious and lean towards things like that. But I say, a man should never have a say over a woman's body."

    scene v8sprot3e
    with dissolve

    u "You're right, they shouldn't. Can't even believe they're doing that."

    scene v8sprot3d
    with dissolve

    aut "It's sickening, if you ask me. A man has no business telling a woman what she can and cannot do with her body, and neither does the government. Abortions are legal for a multitude of reasons."

    aut "I mean if someone wants to bring a child in the world, they need to be prepared. That's how so many kids end up in foster care."

    scene v8sprot3e
    with dissolve

    u "It's a really sad, unfortunate world we live in... But you know, one step at a time!"

    scene v8sprot3
    with dissolve

    aut "Yes! And thanks for joining, this movement needs more men."

    scene v8sprot3a
    with dissolve

    u "Of course. This is a real world issue. Gotta stand by the woman."

    scene v8sprot11 # TPP. Show Autumn smiling at MC, protestors stood behind Autumn protesting, camera from behind MC, both mouths closed.
    with dissolve

    pause 1

    jump prot_w_au_2

label prot_w_au_2:

    scene v8sprot12 # TPP. Show MC and Autumn stood slightly away from the protestors, Autumn mouth open, smile, MC neutral expression, mouth closed.
    with dissolve

    aut "You think you'll be up to do this again soon?"

    scene v8sprot12a # TPP. Same camera as v8sprot12, MC smile, mouth open, Autumn smile, mouth closed.
    with dissolve

    u "Yeah, anytime."

    if evelyn.relationship >= Relationship.LIKES:
        scene v8sprot13 # TPP. Show Evelyn walking past MC, MC turns to look at Evenlyn walking past.
        with dissolve

        pause 1

        scene v8sprot12a
        with dissolve

        u "Hey, I'll be right back. I've just spotted a friend."

        scene v8sprot12
        with dissolve

        aut "Sure thing."

        scene v8sprot14 # FPP. Show Evelyn walking down the street.
        with dissolve

        pause 0.5

        scene v8sprot15 # FPP. Same as v8sprot14 but now closer to Evelyn.
        with dissolve

        u "Hey Evelyn."

        scene v8sprot15a # FPP. Same camera as v8sprot15, Evelyn now turns around and looks at the camera, Evelyn looks pleasantly surprised.
        with dissolve

        scene v8sprot16 # FPP. Close up of Evelyn, surprised expression, mouth open.
        with dissolve

        ev "[name]! What are you doing here?"

        scene v8sprot16a # FPP. Same camera as v8sprot16, Evelyn smile, mouth closed.
        with dissolve

        u "Protesting of course."

        scene v8sprot16
        with dissolve

        ev "Wow, you never mentioned you were into this kind of stuff. I didn't take you as a political person."

        scene v8sprot16a
        with dissolve

        u "Well it's an important issue. So I thought I'd come join the protest today."

        scene v8sprot16b # FPP. Same camera as v8sprot16, Evelyn smile, mouth open.
        with dissolve

        ev "That's amazing. Wish you told me before."

        scene v8sprot16a
        with dissolve

        u "Would it have changed anything?"

        scene v8sprot16c # FPP. Same camera as v8sprot16, Evelyn laugh, mouth open.
        with dissolve

        ev "Haha. Well, no. I had a great time. But honestly, it's a turn on. A guy coming out to a woman's protest for women's rights. That's what I think a real man should be about."

        scene v8sprot16a
        with dissolve

        u "I guess I will take that as a compliment then."

        scene v8sprot16b
        with dissolve

        ev "Definitely a compliment."

        scene v8sprot16a
        with dissolve

        u "So what's up? How have you been? "

        scene v8sprot16d # FPP. Same camera as v8sprot16d, Evelyn neutral expression, mouth open.
        with dissolve

        ev "I'm great actually since I last saw you. I started looking into medical programs, you know, so I can really start to work towards my career."

        scene v8sprot17 # TPP. Show MC and Evelyn stood together, MC slight wink, smile, mouth open, Evelyn mouth closed, neutral expression.
        with dissolve

        u "That's awesome. Glad to see you're pursuing your dreams... That's such a turn on."

        scene v8sprot16c
        with dissolve

        ev "Haha. Yeah, it feels good to be a bit closer to it, you know. But enough about me, how have you been?"

        scene v8sprot16a
        with dissolve

        u "Good. Same. Homework and studying. Gotta keep the grades up. No complaints."

        scene v8sprot16b
        with dissolve

        ev "That's great... Well, I think we should definitely hang out again soon. Don't you think?"

        scene v8sprot16a
        with dissolve

        u "Yeah, yeah. I'd love that."

        scene v8sprot16d
        with dissolve

        ev "Cool."

        scene v8sprot16e # FPP. Same camera as v8sprot16, Evelyn neutral expression, mouth closed.
        with dissolve

        u "Well, I'm gonna get back to my friend."

        scene v8sprot16d
        with dissolve

        ev "Who'd you come with?"

        scene v8sprot16e
        with dissolve

        u "Autumn invited me."

        scene v8sprot16b
        with dissolve

        ev "Oh I love Autumn! She comes to every one of these things. She's a strong woman. And very intelligent."

        scene v8sprot16a
        with dissolve

        u "Yeah. She's cool."

        scene v8sprot16b
        with dissolve

        ev "Well I won't keep you! See you around [name]."

        scene v8sprot16f # FPP. Same camera as v8sprot16, Evelyn smile, mouth open, waving.
        with dissolve

        pause 0.5

        scene v8sprot18 # TPP. Show Evelyn walking away from MC, MC neutral expression mouth open.
        with dissolve

        u "Okay."

        scene v8sprot19 # TPP. Show MC walking back towards Autumn who is stood with protestors.
        with dissolve

        pause 0.5

        scene v8sprot20 # FPP. Close up of Autumn with some protestors in the background, Autumn smile, mouth open.
        with dissolve

        aut "Find your friend?"

        scene v8sprot20a # FPP. Same camera as v8sprot20, Autumn smile, mouth closed.
        with dissolve

        u "Yup."

    jump prot_w_au_end

label prot_w_au_end:

    scene v8sprot20b # FPP. Same camera as v8sprot20, protestors in the background are now leaving, Autumn smile, mouth open.
    with dissolve

    aut "It's just about wrapping up here, in case you wanted to head out. You don't have to stay for clean up or anything."

    scene v8sprot20c # FPP. Same camera as v8sprot20, protestors in the background are now leaving, Autumn smile, mouth closed.
    with dissolve

    u "Yeah, well, I'm feeling pretty tired. Think I'll head back."

    scene v8sprot20b
    with dissolve

    aut "Yeah of course! And again thanks for coming."

    scene v8sprot20c
    with dissolve

    u "Anytime."

    scene v8sprot20d # FPP. Same camera as v8sprot20, protestors in the background are now gone, Autumn smile, mouth open.
    with dissolve

    aut "I'll let you know when there's another protest."

    scene v8sprot20e # FPP. Same camera as v8sprot20, protestors in the background are now gone, Autumn smile, mouth closed.
    with dissolve

    u "Sounds good."

    stop music fadeout 3

    scene v8sprot21 # FPP. Show MC walking away.
    with dissolve
    pause 0.75

    scene black
    with Dissolve(1)
    pause 0.5

    if joinwolves:
        jump after_prot_wolves

    else:
        jump after_prot_dorm
