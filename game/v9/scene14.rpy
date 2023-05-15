# SCENE 14: Your Room Seb & Marcus
# Locations: MC Wolves Room
# Characters: MC (Outfit 1), Sebastian (Outfit 1), Marcus (Outfit 1)
# Time: Thursday Evening

label v9_thur_room_w_seb:
    # -suddenly there's a loud knock on MC's door so he quickly turns around surprised, then jumps off the chair to open the door-
    scene v9trs1 # TPP. Show MC's Wolves room door.
    with dissolve

    play sound sound.knock

    "*Knock* *knock* *knock*"

    scene v9trs2 # TPP. Show MC getting up from his chair towards the door to open it.
    with dissolve

    play music music.ck1.v9.Track_Scene_14 fadein 2

    "Fuck dude, open up!"

    if hl_punch:
        scene v9trs3 # FPP. Show Sebastian and Marcus stood outside MC's door, both smiling, mouths closed.
        with dissolve

        pause 0.5

        jump v9_thur_w_punch
    else:
        scene v9trs3a # FPP. Same camera as v9trs3, both surprised, mouths closed.
        with dissolve

        pause 0.5

        jump v9_thur_w_no_punch

label v9_thur_w_punch:
    scene v9trs3b # FPP. Same camera as v9trs3, both smiling, Sebastian mouth open.
    with dissolve

    se "Well well well! Can you believe this, Marcus?"

    scene v9trs3c # FPP. Same camera as v9trs3, both smiling, Sebastian mouth closed, Marcus mouth open.
    with dissolve

    guyc "Of course I can, haha! Our boy is a fucking star!"

    scene v9trs3b
    with dissolve

    se "Our cub is a famous Wolf!"

    scene v9trs3
    with dissolve

    u "Huh? What the hell are you guys talking about?"

    scene v9trs3d # FPP. Same camera as v9trs3, both shocked, Marcus mouth open.
    with dissolve

    guyc "Holy shit, he doesn't know?!"

    scene v9trs3e # FPP. Same camera as v9trs3, both shocked, Sebastian mouth open.
    with dissolve

    se "Are you fucking kidding me, [name]?"

    scene v9trs3a
    with dissolve

    u "What is going on?!"

    scene v9trs3c
    with dissolve

    guyc "Did you check Kiwii out, man?"

    scene v9trs3b
    with dissolve

    se "It looks like he doesn't know for real!"

    scene v9trs3
    with dissolve

    u "Know what?!"

    scene v9trs4 # TPP. Show MC rushing back to his desk to pick up his phone slight concerned expression, Sebastian and Marcus walk into MC's room behind him.
    with dissolve

    pause 0.8

    scene v9trs5 # FPP. Show Marcus and Chris, now stood in MC's room, both smiling, Sebastian mouth open.
    with dissolve

    se "It's fucking awesome, dude."

    scene v9trs5a # FPP. Same camera as v9trs5, both smiling, Marcus mouth open.
    with dissolve

    guyc "Made us proud, bro."

    $ kiwii_post = KiwiiService.new_post(chris, "v9/Scene 12/v9hlw8c.webp", "That's my boy! Go [name]! Fuck yeah!", number_likes=renpy.random.randint(100, 200))
    $ KiwiiService.new_comment(kiwii_post, sebastian, "Fuckin' A!", number_likes=renpy.random.randint(15, 35))
    $ KiwiiService.new_comment(kiwii_post, aubrey, "Knew he had it in him!", number_likes=renpy.random.randint(15, 35))

    scene v9trs4a # TPP. Same camera as v9trs4, Show MC looking at his phone in hand.
    with dissolve
    
    pause 1

    call screen phone

    scene v9trs5
    with dissolve

    se "That punch, man."

    scene v9trs5a
    with dissolve

    guyc "Fuck yeah! Seems the training did you well. Just like it should!"

    if reputation() == Reputations.LOYAL:
        scene v9trs5b # FPP. Same camera as v9trs5, both smiling, mouths closed.
        with dissolve

        u "Holy fuck, I didn't know someone was filming. I mean, it's cool and all, but what if I get in trouble with this?"

        scene v9trs5
        with dissolve

        se "Relax, we got your back."

        scene v9trs5b
        with dissolve

        u "I'm not talking about revenge, that guy attacked me first. I'm talking about fighting in the hallways!"

        scene v9trs5c # FPP. Same camera as v9trs5, both neutral, Marcus mouth open.
        with dissolve

        guyc "Well if he attacked first, people can vouch for you."

        scene v9trs5d # FPP. Same camera as v9trs5, both neutral, Sebastian mouth open.
        with dissolve

        se "Hell, WE can vouch for you. It was self-defense."

        scene v9trs5a
        with dissolve

        guyc "A pretty badass self-defense, haha."

        scene v9trs5b
        with dissolve

        u "But you weren't there."

        scene v9trs5a
        with dissolve

        guyc "We're always there."

        scene v9trs5
        with dissolve

        se "With mind and soul, brother Wolf."

        jump v9_thur_room_w_seb_cont1
        
    else:
        scene v9trs5b
        with dissolve

        u "Well would you look at that. When one feels no need to brag, they just throw pictures of him around, haha."

        scene v9trs5
        with dissolve

        se "Wow, both strong and a cool player, this [name], haha. Well I can tell you, that was one hell of a knockout."

        scene v9trs5a
        with dissolve

        guyc "I can almost feel it, as if I was there watching."

        scene v9trs5b
        with dissolve

        u "But you weren't. It was just a lone Wolf there, fighting his battles, tsk tsk tsk."

        scene v9trs5c
        with dissolve

        guyc "Oh no, no! We are always there."

        scene v9trs5
        with dissolve

        se "If not in body, then with mind and soul, brother Wolf!"

        jump v9_thur_room_w_seb_cont1

label v9_thur_room_w_seb_cont1:
    scene v9trs5b
    with dissolve

    u "Haha, you guys are idiots."

    scene v9trs5a
    with dissolve

    guyc "I'll let that slide, Mr. Showoff."

    scene v9trs5
    with dissolve

    se "Today is a good day, aaaah-ooooooh!"

    scene v9trs6 # TPP. Show Marcus lifting up a pack of beers, everyone smiling, Marcus mouth open.
    with dissolve

    guyc "And here's to that, aaaah-ooooooh!!"

    scene v9trs7 # TPP. Show everyone grabbing a beer and making a toast.
    with dissolve

    pause 1

    scene v9trs7a # TPP. Show everyone chugging the beers.
    with dissolve

    pause 1

    scene v9trs8 # FPP. Show Sebastian and Marcus, Sebastian holding his beer in the air, both smiling, Sebastian mouth open.
    with dissolve

    se "For an ex cub!"

    scene v9trs8a # FPP. Same camera as v9trs8, Marcus now with beer in the air, both smiling, Marcus mouth open.   
    with dissolve

    guyc "For [name]!"

    scene v9trs8b # FPP. Same camera as v9trs8, both beers in the air, both smiling, mouths closed.
    with dissolve

    u "For the Wolves!"

    scene v9trs7a
    with dissolve
    # -they chug down on beers and laugh it off-

    pause 1

    scene v9trs5a
    with dissolve

    guyc "Two days left before the Freshman Brawl."

    scene v9trs5
    with dissolve

    se "And our boy looks ready as fuck."

    scene v9trs5b
    with dissolve

    u "I wouldn't say I'm THAT ready. But hearing you guys say it, surely makes me feel like I am."

    scene v9trs5a
    with dissolve

    guyc "Trust me, [name]. I can see it in you."

    scene v9trs5
    with dissolve

    se "You got this more than anyone ever could."

    scene v9trs5a
    with dissolve

    guyc "You will see."

    scene v9trs5b
    with dissolve

    u "Talk about pressure, haha. Just kidding. Thanks you guys."

    scene v9trs5
    with dissolve

    se "Less thanking!"

    scene v9trs5a
    with dissolve

    guyc "More beer!"

    scene v9trs5b
    with dissolve

    u "Haha, cheers!"

    scene v9trs7a
    with dissolve

    pause 1

    jump v9_room_thur_night

label v9_thur_w_no_punch:
    scene v9trs3e
    with dissolve

    se "Fucking shit, are you okay man?"

    scene v9trs3f # FPP. Same camera as v9trs3, both concerned, mouths closed.
    with dissolve

    u "So you heard?"

    scene v9trs3d
    with dissolve

    guyc "Heard? Fucking saw it, dude."

    scene v9trs3f
    with dissolve

    u "What? Where?"

    scene v9trs3e
    with dissolve

    se "Check Kiwii, for fucks sake."

    scene v9trs4
    with dissolve

    pause 1

    scene v9trs4a
    with dissolve

    # kiwiiPost
    # -MC rushes back to pick up his phone from the table then checks out Kiwii to find a picture of the guy knocking him out in the hallway-

    u "Fucking bastard."

    scene v9trs5c
    with dissolve

    guyc "Shit [name], what was that all about?"

    scene v9trs5e # FPP. Same camera as v9trs5, both neutral, mouths closed.
    with dissolve

    u "Just some random prick. I bumped into him in the hallway, and he did not wanna listen to reason."

    scene v9trs5d
    with dissolve

    se "And he punched you just like that?"

    scene v9trs5e
    with dissolve

    u "It was all out of nowhere, Seb. Caught me by surprise, I didn't see it coming."

    scene v9trs5c
    with dissolve

    guyc "Did seem pretty dirty to me, yeah."

    scene v9trs5e
    with dissolve

    u "I was just looking down and he punched me in the face!"

    scene v9trs5d
    with dissolve

    se "Shit dude, are you insane? What were you looking down for? Dropped something? Your brain perhaps?"

    scene v9trs5e
    with dissolve

    u "I didn't expect the asshole to just attack me like that, okay? I was trying to be reasonable with him."

    scene v9trs5c
    with dissolve

    guyc "I think you should see a lesson here."

    scene v9trs5e
    with dissolve

    u "A lesson? To fucking strike first and ask questions later, every time, all the time?"

    scene v9trs9 # TPP. Show Sebastian placing his hand on MC's shoulder, neutral expression, mouth open, Marcus mouth closed.
    with dissolve

    pause 1

    scene v9trs5d
    with dissolve

    se "Looks to me you are still suffering from that blow. Look man, it's not about attacking first. It's about never dropping your guard."

    scene v9trs5e
    with dissolve

    u "I know. It just fucking..."

    scene v9trs5d
    with dissolve

    se "It just fucking what? If you are a Wolf, there is no excuse. How do Wolves walk?"

    scene v9trs5e
    with dissolve

    u "With their heads held up?"

    scene v9trs5c
    with dissolve

    guyc "Damn right. Upwards and proud."

    scene v9trs5d
    with dissolve

    se "And ready for anything. And you just were not ready."

    scene v9trs5e
    with dissolve

    u "There was this chick though."

    scene v9trs5d
    with dissolve

    se "Pussy aside, there is a time and place for everything. And that was your time to get punched."

    scene v9trs5c
    with dissolve

    guyc "And now is your time to learn your lesson."

    scene v9trs5e
    with dissolve

    u "Fuck it guys, did you have this rehearsed or what?"

    scene v9trs5d
    with dissolve

    se "It's called common sense, nosebleeder."

    scene v9trs10 # TPP. Show MC checking his nose thinking it's still bleeding but there is no blood.
    with dissolve

    pause 1

    scene v9trs5e
    with dissolve

    u "I guess you are right. I did decide on it anyway. I will not get surprised like that again."

    scene v9trs11 # TPP. Show Sebastian sarastically punching MC on the shoulder, Sebastian smiling.
    with dissolve

    pause 1

    scene v9trs5d
    with dissolve

    se "In that case, you will not. Alright, now that we got that out of the way, Marcus?"

    scene v9trs6
    with dissolve

    pause 1

    scene v9trs5a
    with dissolve

    guyc "We toast!"

    scene v9trs5b
    with dissolve

    u "Haha, what for?"

    scene v9trs8
    with dissolve

    se "For a good lesson."

    scene v9trs8a
    with dissolve

    guyc "For the nosebleeder [name], haha!"

    scene v9trs8b
    with dissolve

    u "Haha, okay, for the Wolves!"

    scene v9trs7a
    with dissolve

    pause 1

    scene v9trs5
    with dissolve

    se "That hits the spot."

    scene v9trs5b
    with dissolve

    u "You can say that again. But you haven't seen everything in the picture, anyway."

    scene v9trs5a
    with dissolve

    guyc "Yeah?"

    scene v9trs5b
    with dissolve

    u "When a warrior gets punched in the face with a cowardly blow, there's always gonna be some hot chick tending his wounds, hehe."

    scene v9trs5
    with dissolve

    se "Oh is that so, haha? Do tell!"

    scene v9trs5b
    with dissolve

    u "So I open my eyes, flat on my back, when..."

    scene black
    with dissolve

    stop music fadeout 3

    pause 1

    jump v9_room_thur_night
