# SCENE 44a) Ms Rose and MC at the london underground
# Locations: london underground, streets, hotel lobby
# Characters: MC (Outfit 3), Ms Rose (Outfit 1), Riley (Outfit 2), Amber (Outfit 1),Nora (Outfit 2)
# Time: Afternoon
label v11_rose_underground:
    scene v11sub1 # TPP. Show MC sitting down next to ms. rose on subway
    with dissolve
    play music "music/v11/Track Scene 16.mp3" fadein 2
    pause 1

    scene v11sub2 # FPP. Show ms rose, mouth open
    with dissolve

    ro "Finally, a short moment to relax."

    scene v11sub2a # FPP. same 2, Show ms rose, mouth closed
    with dissolve

    u "Have you not had many chances to?"

    scene v11sub2
    with dissolve

    ro "I mean, I have, but technically I'm still on-the-clock even when I'm resting."

    scene v11sub2a
    with dissolve

    u "And I'm still in class."

    scene v11sub2
    with dissolve

    ro "So we'll enjoy the quiet moments."

    scene v11sub2a
    with dissolve

    u "Yeah. The quiet moments."

    if ms_rose.relationship.value >= Relationship.FWB.value and joinwolves: #sanitizing pathbuilder input
        scene v11sub2
        with dissolve

        ro "You've helped me enjoy this trip quite a bit, you know?"

        scene v11sub2a
        with dissolve

        # -Ms. Rose caresses MC's thigh-

        u "Have I, now?"

        scene v11sub2
        with dissolve

        ro "When we aren't so public... I just may have you help me a bit more. With a few private issues."

        scene v11sub2a
        with dissolve

        u "I'm sure I could help by doing one thing or another."

        scene v11sub2
        with dissolve

        ro "It looks like things are going to be a bit tight during the rest of our time here in London, but Paris is right around the corner."

        scene v11sub2a
        with dissolve

        u "Oh, big plans?"

        scene v11sub2b # FPP. Same 2, slight smile, change pose a little so not stale. mouth open
        with dissolve

        ro "Big plans for us."

        scene v11sub2c # FPP. Same 2a, slight smile, change pose a little so not stale. mouth closed
        with dissolve

        u "Shit, Paris here I come."

        scene v11sub2b
        with dissolve

        ro "I'll be sure to have your assigned room close to mine, because I plan on-"
        
    else:

        scene v11sub2c
        with dissolve

        u "What have you enjoyed most, so far?"

        scene v11sub2b
        with dissolve

        ro "Honestly? Just being away from home has been nice."

        scene v11sub2c
        with dissolve

        u "That sounds sort of sad."

        scene v11sub2b
        with dissolve

        ro "Not at all... I'm a free-spirited person and I often like to get out. Outside of just moving into a new house, I've stayed at home for so long."
        ro "No vacations, family visits or anything... It's just been work. This is work too, but obviously it feels slightly different."

        scene v11sub2c
        with dissolve

        u "I think students sometimes forget that teachers have lives outside of school."

        scene v11sub2b
        with dissolve

        ro "Professors."

        scene v11sub2a
        with dissolve

        u "Huh?"

        scene v11sub2
        with dissolve

        ro "I'm a professor. I worked hard to become a professor rather than a teacher."

        scene v11sub2a
        with dissolve

        u "Sorry, Professor. *Chuckles* I honestly don't think I've ever called you anything other than Ms. Rose. I think everyone just calls you that."

        scene v11sub2
        with dissolve

        ro "I never wanted to be that professor that was really harsh about things like titles, but I won't fall back to being called a teacher. *Chuckles*"
        ro "That's like calling the President \"mister\" and then their last name. It's just not their title you know?"

        scene v11sub2c
        with dissolve

        u "I get that."

        scene v11sub2b
        with dissolve

        ro "Oh, while I remember, when in Paris I'd like to-"

    scene black
    with vpunch

    ro "Okay, that can't be good."

    u "Pretty sure we stopped moving."

    ro "*Sighs* It never ends. I'll text Mr. Lee and let him know we're having a little trouble."

    scene v11sub3 # FPP. Ms. Rose pulls out her phone and the only light that can be seen is light from her phone
    with dissolve

    ro "*Sighs* Of course, there's no service down here. We'll just have to wait it out. Sometimes it really just feels like the universe is out to get me."

    menu:
        "Leave her be":
            scene v11sub3
            with dissolve
            
            u "(She has a lot on her plate right now, probably best to leave her alone.)"

            ro "We'll sit here for who knows how long. *Sighs*"

        "Comfort her":
            $ ms_rose.points += 1
            scene v11sub3
            with dissolve

            u "It's not. Like you said, enjoy the quiet moments. I'm not sure how long we'll be stuck here, but at least you can relax."

            ro "*Sighs* You're right, thank you."

            u "Always."
        

    scene v11sub4 # FPP. The light comes back on and MC looks over to Riley and Amber and sees them kissing,
    with dissolve

    pause 1

    scene v11sub4a # FPP. same 4, They quickly separate and blush while looking away from each to act like nothing happened
    with dissolve

    u "*Chuckles* Well, the lights are back."

    scene v11sub2
    with dissolve

    ro "Yes, but we still aren't moving."

    scene v11sub2a
    with dissolve

    u "True."

    scene v11sub2
    with dissolve

    ro "*Sighs*"

    scene v11sub2a
    with dissolve

    scene v11sub5 # Fpp. Show ms. rose looking bored
    with fade

    pause 2

    scene v11sub6 # FPP. Show Riley and Amber talking
    with fade

    pause 2

    scene v11sub7 # FPP. show nora sat on her own
    with fade

    pause 2

    scene v11sub2b
    with dissolve

    ro "And... we're finally moving! Just another few minutes now, students."

    scene v11sub8 # TPP. Show Mc walking off the train, Ms.rose, nora and Riley in background
    with fade

    pause 1

    scene v11sub9 # TPP. Show MC and characters from sub8, walking on sidewalk
    with fade

    pause 1

    scene v11sub10 # TPP. Show Mc and the previous characters entering the hotel
    with fade

    pause 1
    stop music fadeout 3
    jump v11_lobby_mrlee