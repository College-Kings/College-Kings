# SCENE 01: Threesome With Aubrey and Riley
# Locations: Hotel Room, Hotel Room Corridor
# Characters: MC (Outfit: 3), AUBREY (Outfit: 6), RILEY (Outfit: 6)
# Time: Night

label v14_start:
    if path_builder and not pb_name_set:
        $ name = renpy.input(_("What's your name?"), default=_("Alex")).strip() or _("Alex")
        $ pb_name_set = True
    
        if emily.relationship == Relationship.GIRLFRIEND:
            $ sceneList.add("v13_emily")

        if ms_rose.relationship == Relationship.GIRLFRIEND:
            $ sceneList.add("v12_rose")

        if lauren.relationship == Relationship.GIRLFRIEND:
            $ sceneList.add("v12_lauren")
            
        if nora.relationship == Relationship.GIRLFRIEND:
            $ sceneList.add("v12_nora")
            
        if chloe.relationship == Relationship.GIRLFRIEND:
            $ sceneList.add("v13_chloe")
            
        if lindsey.relationship == Relationship.GIRLFRIEND:
            $ sceneList.add("v12_lindsey")

        if lauren.relationship == Relationship.FRIEND:
            $ lauren.relationship = Relationship.KISS

    show screen phone_icon
    
    if emmy.simplr.pending_messages: #for compatibility with v12 players where emmy replies were not forced to be seen
        $ emmy.simplr.pending_messages = []
        $ emmy.simplr.sent_messages[-1].replies = []

    if aubrey.relationship >= Relationship.FWB and riley.relationship >= Relationship.FWB:
        $ v13_threesomeending = True
        jump v14s01

    else:
        jump v14s01a
    
label v14s01:
    play music "music/v12/Track Scene 23_2.mp3" fadein 2

    scene v14s01_1 # FPP. MC sitting on bed, looking at Riley and Aubrey making out, show some caressing between them
    with dissolve

    u "(Are they seriously trying to have a threesome...?)"

    call screen confirm("This act has voice acted sex scenes. Each girl has a unique voice and moans accordingly. Would you like to enable voice acting in the sex scenes?",
        yes_action=[SetVariable("voice_acted", True), Return()],
        no_action=[SetVariable("voice_acted", False), Return()])

    scene v14s01_1a # FPP. Same as v14s01_1, Riley and Aubrey removing their bras, they're looking at MC seductively, mouths closed
    with dissolve

    u "(Oh, shit. This is happening.)"

    if config_censored:
        call screen censoredPopup("v14s01_nsfwSkipLabel1")

    scene v14s01_1b # FPP. Same as v14s01_1a, Riley and Aubrey topless, looking at MC seductively, both mouths closed
    with dissolve

    menu:
        "We're doing this":
            $ add_point(KCT.TROUBLEMAKER)
            
            $ sceneList.add("v14_threesome")
            u "I'm gonna feel much better after this."

            scene v14s01_1c # FPP. Samer as v14s01_1b, but Aubrey mouth open, Riley mouth closed, Aubrey looking at Riley, Riley looking at Aubrey
            with dissolve

            au "*Chuckles* I knew he'd like the idea."

            scene v14s01_1d # FPP. Same as v14s01_1b, Aubrey and Riley looking at MC, Riley mouth open, Aubrey mouth closed
            with dissolve

            ri "Haha... You just relax, okay?"

            scene v14s01_1b
            with dissolve

            u "Yes, ma'am... That I can do."

            scene v14s01_2 # TPP. Show Riley helping MC remove his shirt while Aubrey is removing her panties
            with dissolve

            pause

            scene v14s01_3 # TPP. Show Aubrey helping MC remove his pants and boxers while Riley is removing her panties
            with dissolve

            pause

            scene v14s01_4 # TPP. Show Aubrey and Riley moving to suck MC's dick, all smiling, mouths closed
            with dissolve

            pause

            image v14auridbj = Movie(play="images/v14/Scene 1/v14auridbj.webm", loop=True, image="images/v14/Scene 1/v14auridbjStart.webp", start_image="images/v14/Scene 1/v14auridbjStart.webp") # double blowjob
            image v14auridbjf = Movie(play="images/v14/Scene 1/v14auridbjf.webm", loop=True, image="images/v14/Scene 1/v14auridbjStart.webp", start_image="images/v14/Scene 1/v14auridbjStart.webp") # double blowjob spedup
            image v14auridbj2 = Movie(play="images/v14/Scene 1/v14auridbj2.webm", loop=True, image="images/v14/Scene 1/v14auridbj2Start.webp", start_image="images/v14/Scene 1/v14auridbj2Start.webp") # double blowjob FPP
            image v14auridbj2f = Movie(play="images/v14/Scene 1/v14auridbj2f.webm", loop=True, image="images/v14/Scene 1/v14auridbj2Start.webp", start_image="images/v14/Scene 1/v14auridbj2Start.webp") # double blowjob FPP spedup

            scene v14auridbj # Ignore as animation
            with dissolve
            if voice_acted:
                $ renpy.sound.play("music/v14/va/Scene 1 - dbj_slow_2loops.mp3", loop=True)
            pause

            u "*Moans* Damn, ladies... That feels unbelievable."

            stop sound
            scene v14auridbjf # Ignore as animation
            with dissolve
            if voice_acted:
                $ renpy.sound.play("music/v14/va/Scene 1 - dbj_fast_2loops.mp3", loop=True)
            pause

            u "You two are so fucking beautiful."

            stop sound
            scene v14auridbj2 # Ignore as animation
            with dissolve
            if voice_acted:
                $ renpy.sound.play("music/v14/va/Scene 1 - dbj_slow_2loops.mp3", loop=True)
            pause

            u "Mmm, fuck! O-okay... Come here, now."

            stop sound
            scene v14auridbj2f # Ignore as animation
            with dissolve
            if voice_acted:
                $ renpy.sound.play("music/v14/va/Scene 1 - dbj_fast_2loops.mp3", loop=True)
            pause

            ri "Hehe... Yes, sir."

            stop sound
            scene v14s01_5 # TPP. Show Riley moving to climb on top of MC in reverse cowgirl and Aubrey moving to stay in front of Riley to kiss her
            with dissolve

            pause

            image v14aurircg = Movie(play="images/v14/Scene 1/v14aurircg.webm", loop=True, image="images/v14/Scene 1/v14aurircgStart.webp", start_image="images/v14/Scene 1/v14aurircgStart.webp") # Chloe Table top
            image v14aurircgf = Movie(play="images/v14/Scene 1/v14aurircgf.webm", loop=True, image="images/v14/Scene 1/v14aurircgStart.webp", start_image="images/v14/Scene 1/v14aurircgStart.webp") # Chloe Table top spedup
            image v14aurircg2 = Movie(play="images/v14/Scene 1/v14aurircg2.webm", loop=True, image="images/v14/Scene 1/v14aurircg2Start.webp", start_image="images/v14/Scene 1/v14aurircg2Start.webp") # Chloe Table top FPP
            image v14aurircg2f = Movie(play="images/v14/Scene 1/v14aurircg2f.webm", loop=True, image="images/v14/Scene 1/v14aurircg2Start.webp", start_image="images/v14/Scene 1/v14aurircg2Start.webp") # Chloe Table top FPP spedup

            scene v14aurircg # Ignore as animation
            with dissolve
            if voice_acted:
                $ renpy.sound.play("music/v14/va/Scene 1 - rcg_slow_4loops.mp3", loop=True)
            pause

            ri "*Moans* Oh yes! It gets better... every... time!"

            au "Mmm... *Chuckles*"

            stop sound
            scene v14aurircgf # Ignore as animation
            with dissolve
            if voice_acted:
                $ renpy.sound.play("music/v14/va/Scene 1 - rcg_fast_4loops.mp3", loop=True)
            pause

            au "Look at you, babe. You've definitely done this before."

            ri "Once or t-twice."

            stop sound
            scene v14aurircg2 # Ignore as animation
            with dissolve
            if voice_acted:
                $ renpy.sound.play("music/v14/va/Scene 1 - rcg_slow_4loops.mp3", loop=True)
            pause

            u "*Moans* She does a... damn good job, too."

            ri "*Panting* Ha!"

            stop sound
            scene v14aurircg2f # Ignore as animation
            with dissolve
            if voice_acted:
                $ renpy.sound.play("music/v14/va/Scene 1 - rcg_fast_4loops.mp3", loop=True)
            pause

            au "You know what? You haven't eaten in a long, long time, [name]."

            u "Ha... Wait. Huh?"

            stop sound
            scene v14s01_6 # TPP. Show Riley kissing Aubrey very passionately (Make sure position matches v14auricg animation)
            with dissolve

            pause

            scene v14s01_7 # TPP. Show Riley moving to sit on MC's face with one hand on the wall, Riley mouth open, sexy smirk
            with dissolve

            ri "I'll take care of that..."

            scene v14s01_8 # TPP. Show Riley sitting on MC's face and Aubrey getting on MC's dick in cowgirl
            with dissolve

            pause

            image v14auridcg = Movie(play="images/v14/Scene 1/v14auridcg.webm", loop=True, image="images/v14/Scene 1/v14auridcgStart.webp", start_image="images/v14/Scene 1/v14auridcgStart.webp") # Chloe Table top
            image v14auridcgf = Movie(play="images/v14/Scene 1/v14auridcgf.webm", loop=True, image="images/v14/Scene 1/v14auridcgStart.webp", start_image="images/v14/Scene 1/v14auridcgStart.webp") # Chloe Table top spedup
            image v14auridcg2 = Movie(play="images/v14/Scene 1/v14auridcg2.webm", loop=True, image="images/v14/Scene 1/v14auridcg2Start.webp", start_image="images/v14/Scene 1/v14auridcg2Start.webp") # Chloe Table top FPP
            image v14auridcg2f = Movie(play="images/v14/Scene 1/v14auridcg2f.webm", loop=True, image="images/v14/Scene 1/v14auridcg2Start.webp", start_image="images/v14/Scene 1/v14auridcg2Start.webp") # Chloe Table top FPP spedup

            scene v14auridcg # Ignore as animation
            with dissolve
            if voice_acted:
                $ renpy.sound.play("music/v14/va/Scene 1 - dcg_slow_4loops.mp3", loop=True)
            pause

            ri "Oh... F-f-fuuuuck... [name]!"

            au "*Moans* It's been way too long..."

            stop sound
            scene v14auridcgf # Ignore as animation
            with dissolve
            if voice_acted:
                $ renpy.sound.play("music/v14/va/Scene 1 - dcg_fast_4loops.mp3", loop=True)
            pause

            u "*Moans*"

            ri "This... is perfect... *Moans*"

            stop sound
            scene v14auridcg2 # Ignore as animation
            with dissolve
            if voice_acted:
                $ renpy.sound.play("music/v14/va/Scene 1 - dcg_slow_4loops.mp3", loop=True)
            pause

            au "Ha... Mmm... She's right. *Moans*"

            au "Are you feeling any better, [name]?"

            stop sound
            scene v14auridcg2f # Ignore as animation
            with dissolve
            if voice_acted:
                $ renpy.sound.play("music/v14/va/Scene 1 - dcg_fast_4loops.mp3", loop=True)
            pause

            u "*Mumbles*"

            ri "Ha! Mmm, that tickled... *Chuckles*"

            stop sound
            scene v14s01_9 # TPP. Close up of Aubrey, she's moving to suck his dick again, her mouth is open, looking at Riley
            with dissolve

            au "I'll take that as a yes. C'mon, Riley."

            scene v14s01_10 # TPP. Show Aubrey ready to suck MC's dick and Riley ready to suck on his balls
            with dissolve

            pause

            image v14aurido = Movie(play="images/v14/Scene 1/v14aurido.webm", loop=True, image="images/v14/Scene 1/v14auridoStart.webp", start_image="images/v14/Scene 1/v14auridoStart.webp") # Chloe Table top
            image v14auridof = Movie(play="images/v14/Scene 1/v14auridof.webm", loop=True, image="images/v14/Scene 1/v14auridoStart.webp", start_image="images/v14/Scene 1/v14auridoStart.webp") # Chloe Table top spedup
            image v14aurido2 = Movie(play="images/v14/Scene 1/v14aurido2.webm", loop=True, image="images/v14/Scene 1/v14aurido2Start.webp", start_image="images/v14/Scene 1/v14aurido2Start.webp") # Chloe Table top FPP
            image v14aurido2f = Movie(play="images/v14/Scene 1/v14aurido2f.webm", loop=True, image="images/v14/Scene 1/v14aurido2Start.webp", start_image="images/v14/Scene 1/v14aurido2Start.webp") # Chloe Table top FPP spedup

            scene v14aurido # Ignore as animation
            with dissolve
            if voice_acted:
                $ renpy.sound.play("music/v14/va/Scene 1 - doral_slow_2loops.mp3", loop=True)
            pause

            u "Wow, I... I have the best fucking life... *Moans*"

            stop sound
            scene v14auridof # Ignore as animation
            with dissolve
            if voice_acted:
                $ renpy.sound.play("music/v14/va/Scene 1 - doral_fast_4loops.mp3", loop=True)
            pause

            ri "*Chuckles*"

            stop sound
            scene v14aurido2 # Ignore as animation
            with dissolve
            if voice_acted:
                $ renpy.sound.play("music/v14/va/Scene 1 - doral_slow_2loops.mp3", loop=True)
            pause

            u "Sh-shit... Mmmm, I'm getting ready to... *Moans*"

            stop sound
            scene v14aurido2f # Ignore as animation
            with dissolve
            if voice_acted:
                $ renpy.sound.play("music/v14/va/Scene 1 - doral_fast_4loops.mp3", loop=True)
            pause
            au "Mmm! *Gags*"

            u "Fuck..."

            stop sound
            scene v14s01_11 # FPP. MC looking at Aubrey, Aubrey with his dick fully in her mouth, Riley sucking MC's balls
            with vpunch

            pause

            scene v14s01_11a # FPP. Aubrey licking her lips, seductive look, Riley stops sucking MC's balls, both looking at MC, mouths closed
            with dissolve

            pause 

            scene v14s01_11b # FPP. Same as v14s01_11a, Aubrey and Riley looking at each other, both sexy smiling, Aubrey mouth open, Riley mouth closed
            with dissolve

            au "Well, I have to admit..."

            scene v14s01_11c # FPP. Same as v14s01_11a, Aubrey mouth open, Riley mouth closed, both looking at MC, sexy smile
            with dissolve

            au "That was the best sex I've ever had, haha. How are you feeling over there, big guy?"

            scene v14s01_11d # FPP. Same as v14s01_11c, Aubrey and Riley mouths closed
            with dissolve

            $ grant_achievement("ready_player_three")

            u "*Chuckles* I feel absolutely amazing. Thank you ladies."

            scene v14s01_11e # FPP. Same as v14s01_11d, Riley mouth open, Aubrey mouth closed
            with dissolve

            ri "*Laughs* I call that a job well done."

            play sound "sounds/kiss.mp3"

            scene v14s01_11f # FPP. Same as v14s01_11d, Aubrey and Riley kissing
            with dissolve

            pause

            scene v14s01_11b
            with dissolve

            au "We may have to do this again, Riley."

            stop music fadeout 3
            play music "music/v12/Track Scene 35.mp3" fadein 2

            scene v14s01_11g # FPP. Same as v14s01_11b, Riley mouth open, Aubrey mouth closed
            with dissolve

            ri "Okay! I'm down. *Chuckles*"

            scene v14s01_11c
            with dissolve

            au "[name]?"

            scene v14s01_11d
            with dissolve

            u "Always! I mean, uh... Yeah, whenever."

            scene v14s01_11c
            with dissolve

            au "*Laughs* Good."

            scene v14s01_11b
            with dissolve

            au "Riley, let's go clean up."

            scene v14s01_11g
            with dissolve

            ri "Yeah, let's go."

            scene v14s01_11e
            with dissolve
            
            ri "Catch you later, [name]. Glad you're feeling better."

            scene v14s01_12 # TPP. Show Riley and Aubrey putting on their bras (Panties already on)
            with dissolve

            pause

            scene v14s01_13 # FPP. Show the girls leaving the room (in their underwear), focus on their asses
            with dissolve

            u "(Am I just a lucky bastard or did I do something to deserve that? They sure did act like I earned this... Whatever I did, I need to keep doing it.)"

            $ renpy.end_replay()

            scene v14s01_14 # TPP. Show MC getting out of his bed (he's naked), slight smile, mouth closed
            with dissolve

            pause 0.75

            scene v14s01_15 # TPP. Show MC putting on his shirt (pants already on)
            with dissolve

            pause 0.75

            scene v14s01_16 # TPP. Show MC leaving the hotel room, smiling, mouth closed
            with dissolve

            u "(Now that I'm awake I might as well go see what's going on.)"
            u "(My sleep schedule is gonna be all fucked now, though. Feeling energized at night isn't a good thing...) *Sighs*"

        "Stop them":
            $ add_point(KCT.BOYFRIEND)
            scene v14s01_1e # FPP. Same as v14s01_1b, Aubrey and Riley shocked, mouths closed
            with dissolve

            u "Aubrey, Riley, wait. I appreciate the concern, and I really appreciate what you're trying to do for me, but... Now isn't the best time."

            scene v14s01_1f # FPP. Same as v14s01_1e, but Riley mouth open, Aubrey mouth closed
            with dissolve

            ri "Oh..."

            scene v14s01_1g # FPP. Same as v14s01_1e, but Riley mouth closed, Aubrey mouth open
            with dissolve

            au "Wow, I was not expecting that."

            scene v14s01_1f
            with dissolve

            ri "We were hoping we could help the pain go away."

            scene v14s01_1g
            with dissolve

            au "You must've hit your head pretty hard... Now I really feel bad."

            scene v14s01_1e
            with dissolve

            u "Yeah, I'm not very aware right now. I do feel like getting up though I think."

            scene v14s01_1h # FPP. Same as v14s01_1f, but Riley and Aubrey looking at each other, both slight smiles
            with dissolve

            ri "Okay, well... In that case, Aubrey and I are gonna go hang out."

            scene v14s01_1i # FPP. Same as v14s01_1g, but Riley and Aubrey looking at each other, both slight smiles
            with dissolve

            au "*Chuckles* Sounds like a plan. Text us if you need us."

            scene v14s01_1j # FPP. Same as v14s01_1f, but both slight smiles
            with dissolve

            ri "Hope you feel better soon, [name]."

            scene v14s01_1k # FPP. Same as v14s01_1e, but both slight smiles
            with dissolve

            u "Thanks ladies."

            scene v14s01_13
            with dissolve

            u "(They really wanted to have a threesome... Those girls are fucking wild.)"

            label v14s01_nsfwSkipLabel1:

            scene v14s01_14a # TPP. Same as v14s01_14, but MC is fully clothed
            with dissolve

            pause 0.75

            scene v14s01_16
            with dissolve

            u "*Sighs* (My sleep schedule is gonna be fucked if I start waking up at night time. Oh well.)"


    scene v14s01_17
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v14s02