# SCENE 7: Free Roam Lake
# Locations: Lake
# Characters: MC - Outfit 1, Aubrey - Outfit 4, Riley - Outfit 4, Ryan - Outfit 1
# Time: Wednesday morning
# -Ryan, Aubrey, Riley and MC are at the lake-
# -Ryan is sitting on a picnic blanket, one leg bent in knee, supporting himself with one arm, looking at Riley and Aubrey-
# -Riley is sitting on the pier, with her legs hanging over the ledge-
# -Aubrey is in her pink bikini, swimming on the left side of the lake-
# -On the right side of the lake there is a guy who took his dog for a walk, petting him-
# -On the far left, there's a guy sleeping under a tree wearing a cool looking cowboy hat over his face-

# -You get to choose who to approach, in any order you like. If you click on either Aubrey or Riley, camera zooms in on the two-

########################## FREEROAM 5: LAKE

# FREEROAM SCREENS

label v9_before_lake_fr:
    scene fr5lakefull
    with dissolve

    play music "music/v9/Track Scene 7.mp3" fadein 2

    scene fr5lakefull

    call screen v9s7_lakeFull

label fr5ryan1:
    $ freeroam5.add("ryan")

    if joinwolves:
        scene v9slake1 #FPP closeup ryan sitting on a picnic blanket, mouth closed, Ryan grinning looking at the girls (you can't see the girls)

        u "Enjoying the view?"

        scene v9slake1b #same as 1, Ryan turns his head towards you, mouth open, smiling
        with dissolve

        ry "That obvious, huh?"

        scene v9slake1c # same as 1b, mouth closed
        with dissolve

        u "It's that grin that gives it away, hah."

        scene v9slake1b
        with dissolve

        ry "Can't help it, man. College life, I mean. It's like burning of hotness!"

        scene v9slake1c
        with dissolve

        u "Yes, I've noticed."

        scene v9slake1b
        with dissolve

        ry "Ever since it started, it's been kinda hard to grasp it all, but how could one not?"
        ry "Throw all the pussy you can my way, and I'll handle it no problem, haha."
        ry "Being in a frat surely does not make it any harder!"

        scene v9slake1c
        with dissolve

        menu:
            "Mention the Wolves":
                u "And to me, getting into Wolves really feels like a pretty good choice."

                scene v9slake1d # same as 1b, ryan a bit annoyed mouth open
                with dissolve

                ry "Oh, here we go, boy. Apes are the way to go, and never look back."

                scene v9slake1b
                with dissolve

                ry "But at least you did get a piece of my philosophy. Frat guys always have better chances with the ladies."

                scene v9slake1c
                with dissolve

                u "I guess you are right. But there's also something else I've learned."

                scene v9slake1b
                with dissolve

                ry "And what is that?"

                scene v9slake1c
                with dissolve

                u "Frat choice does not matter when it comes to being friends, ape boy."

                scene v9slake1b
                with dissolve

                ry "Oh is that so, little puppy?"

                ry "Still, a poor choice by you, I can tell you that, ha."

                scene v9slake1c
                with dissolve

                u "I don't really see you dripping in pussy, haha."

                scene v9slake1b
                with dissolve

                ry "Shut up!"

            "Play it cool":
                u "Frat or not, it all comes down to the looks. And one could not deny your boy's handsome as fuck, haha."

                scene v9slake1f # same as 1b, ryan eyebrow raised, teasing mc, mouth open
                with dissolve

                ry "Now that you mention it, that first day I met you, I almost mistook you for a babe."

                scene v9slake1g # same as 1f, mouth closed
                with dissolve

                u "Ha!"

                scene v9slake1b
                with dissolve

                ry "No to be fair, who could ever mistake you for a girl with an ass pointy as that?! Haha."

                scene v9slake1c
                with dissolve

                u "OK now that's too far, asshole!"

                scene v9slake1b
                with dissolve

        ry "Anyway, I don't mind a day such as this sometimes. A cool breeze and a hot view, hehe."

        scene v9slake1c
        with dissolve

        u "I guess I should leave you at it, then. Let me check around for a bit."

        scene v9slake1b
        with dissolve

        ry "You do that, man."

    else:
        scene v9slake1

        u "Yo, how's my bro doing?"

        scene v9slake1b
        with dissolve

        ry "Just into some important scientific business."

        scene v9slake1c
        with dissolve

        u "By staring at the girls, right?"

        scene v9slake1b
        with dissolve

        ry "You make it sound like I'm monkeying around, but it's pretty important!"

        scene v9slake1c
        with dissolve

        u "Haha, how's that?"

        scene v9slake1f
        with dissolve

        ry "There may be enough pussy to go around, but a man should properly evaluate first, you know?"

        scene v9slake1g
        with dissolve

        u "And you are evaluating Riley and Aubrey?"

        scene v9slake1f
        with dissolve

        ry "It's just a way of sharpening up senses and expectations!"

        scene v9slake1g
        with dissolve

        u "So how's that working for you?"

        scene v9slake1f
        with dissolve

        ry "Good, good. For instance, I can tell you that Aubrey maybe looks like it, but I can sense she's not very experienced."

        scene v9slake1g
        with dissolve

        u "Oh, haha dude, I think you got it all wrong."

        scene v9slake1f
        with dissolve

        ry "Or maybe I'm just not into giving away secrets!"

        scene v9slake1g
        with dissolve

        u "Yeah yeah, or that."

        scene v9slake1b
        with dissolve

        ry "So what's up with you? You're looking more cheerful than usual today."

        scene v9slake1c
        with dissolve

        menu:
            "Talk about your dream":
                $ add_point(KCT.BOYFRIEND)

                u "I'm not so sure about that. Last night I had a fucked up dream."

                scene v9slake1h # same as 1f, ryan curious, mouth open
                with dissolve

                ry "A dream, huh. What was it about?"

                scene v9slake1j #same as 1j, mouth closed
                with dissolve

                u "There was this dark void all around me and then a boxing ring and then a fight."

                scene v9slake1h
                with dissolve

                ry "You were fighting someone? In a dark void?"

                scene v9slake1j
                with dissolve

                u "Yeah, I wanted to fight the Wolves. But no matter how hard I tried to hit, I did nothing."

                scene v9slake1f
                with dissolve

                ry "Seems like you're worried about the Brawl, [name]."

                scene v9slake1g
                with dissolve

                u "Not about the Brawl but, there was more."

                scene v9slake1h
                with dissolve

                ry "Yeah?"

                scene v9slake1j
                with dissolve

                u "No matter how hard I tried, everyone was disappointed in me."

                u "It felt like fucking up everything."
                u "Like losing there meant losing everything."

                scene v9slake1h
                with dissolve

                ry "I get it. But it was all just a dream, right?"

                scene v9slake1j
                with dissolve

                u "I... I guess, so."

                scene v9slake1h
                with dissolve

                ry "Look, man. You got this, and I'm not just saying it."

                scene v9slake1j
                with dissolve

                u "Doesn't feel like that to me."

                scene v9slake1h
                with dissolve

                ry "I know, but that's how things always are from your own perspective."

                scene v9slake1j
                with dissolve

                u "Sounds pretty wise, for words coming out of Ryan's mouth."

                scene v9slake1h
                with dissolve

                ry "I had moments like that too. You know, doubting yourself and all."

                scene v9slake1b
                with dissolve
                
                ry "But seeing you, [name]. You are the kind of guy who makes the right choices."
                ry "And the kind of guy who can do this. Someone to show how great Apes are. And how hard they can punch."

                scene v9slake1c
                with dissolve

                u "Thanks, Ryan. I didn't even know I needed this. But it seems I sure as fuck have."

                scene v9slake1b
                with dissolve

                ry "No problem, that's what bros are for, am I right?"

                scene v9slake1c
                with dissolve

                u "Right as fuck, my man."

            "Talk about the brawl":
                $ add_point(KCT.BRO)

                # -if MC chooses to tell Ryan how excited he is about the Brawl-

                u "I guess I am just excited."

                scene v9slake1b
                with dissolve

                ry "About what?"

                scene v9slake1c
                with dissolve

                u "The Freshmen Brawl."

                scene v9slake1h
                with dissolve

                ry "You got this, right?"

                scene v9slake1j
                with dissolve

                u "I was not sure at first. You know, it was all so sudden."

                scene v9slake1h
                with dissolve

                ry "But that's how best things work, right?"

                scene v9slake1j
                with dissolve

                u "I guess so. I've been training for this, and there's no way in Hell I'm gonna lose."

                scene v9slake1b
                with dissolve

                ry "Fuck yeah!"

                scene v9slake1c
                with dissolve

                u "No Wolf or man can stand in my way!"

                scene v9slake1b
                with dissolve

                ry "Fuck yeah!"

                scene v9slake1c
                with dissolve

                u "And no stupid fucking dreams can stop me!"

                scene v9slake1h
                with dissolve

                ry "Fuck- Errr, what?"

                scene v9slake1j
                with dissolve

                u "I got this, man!"

                scene v9slake1h
                with dissolve

                ry "What dreams?"

                scene v9slake1j
                with dissolve

                u "Oh man, I feel so great!"

                scene v9slake1d
                with dissolve

                ry "Right."

                scene v9slake1b
                with dissolve

        ry "Anyway, it's great to see you are doing well. And I surely don't mind a day such as this sometimes. A cool breeze and a hot view, hehe."

        scene v9slake1c
        with dissolve

        u "I guess I should leave you at it, then. Let me check around for a bit."

        scene v9slake1b
        with dissolve

        ry "You do that, man."

    call screen v9s7_lakeFull

label fr5riley1:
    $ freeroam5.add("riley")

    scene v9slake2 #FPP Close up as if sitting next to Riley, you look at her from the side, Riley is sitting on the pier, with her legs hanging over the ledge, Riley looking at the lake. -

    if riley.relationship >= Relationship.FWB:
        u "What's a pretty lady doing all by herself?"

        scene v9slake2b #same as 2, but Riley now looking at you, flirting, mouth open
        with dissolve

        ri "Maybe she's waiting for a hot guy to ask her that exact question, hehe."

        scene v9slake2c #same as 2b, but mouth closed
        with dissolve

        u "Well what do you know. Here he comes, hah."

        scene v9slake2b
        with dissolve

        ri "Where? Can't see. Come closer, mister."

        scene v9slake2c
        with dissolve

        menu:
            "Kiss her":
                $ add_point(KCT.TROUBLEMAKER)

                play sound "sounds/kiss.mp3"

                scene v9slake3 #TPP showing mc and riley kissing
                with dissolve
                
                pause 1.0

                scene v9slake2c
                with dissolve

                u "Did that fix your eyesight, lady?"

                scene v9slake2b
                with dissolve

                ri "No, but I wouldn't mind trying again, hehe."

                scene v9slake2c
                with dissolve

                u "Pretty and clever, what a combination."

                scene v9slake2b
                with dissolve

                ri "And what a sweet talker, hah."

                scene v9slake2c
                with dissolve

                u "You know it."

            "Blow air at her":
                scene v9slake3b #same camera as 3, but mc blowing air in rileys face
                with dissolve

                u "*Blows air*"

                scene v9slake2d #same as 2b but Riley laughing
                with dissolve

                ri "What the fuck was that?! Haha!"

                scene v9slake2e # same as 2b but riley mouth closed
                with dissolve

                u "It's a family recipe, don't even try to ask."

                scene v9slake2b
                with dissolve

                ri "Why would I? It sucks, haha."

                scene v9slake2c
                with dissolve

                u "First of all, it does not suck, it blows! And second of all, it's not an instant remedy, you know."

        scene v9slake2b
        with dissolve

        ri "And here was I relaxing. Then HE had to drop by and make me all excited and what not."

        scene v9slake2c
        with dissolve

        u "I was just checking on you. Having a nice time?"

        scene v9slake2f # same as 2b but riley smiling mouth open
        with dissolve

        ri "Yeah. I really need this sometimes. Just looking at water is so relaxing. Don't you think so?"

        scene v9slake2g # same as 2f but riley mouth closed
        with dissolve

        u "I guess so. Sorry for interrupting."

        scene v9slake2f
        with dissolve

        ri "Not at all."

        scene v9slake2g
        with dissolve

        u "Hehe, OK I'm gonna go check on others."

        scene v9slake2f
        with dissolve

        ri "Okay."

    if riley.relationship < Relationship.FWB:
        u "And I thought I was gonna find you close to the water. Wanna take a dip?"

        scene v9slake2f
        with dissolve

        ri "No, not in the mood for that. I just like being close, watching it, that's all."

        scene v9slake2g
        with dissolve

        u "Sounds like fun, hah."

        scene v9slake2f
        with dissolve

        ri "You'd be surprised, actually. Fun is not always about getting excited."
        
        ri "Sometimes it's just about..."

        scene v9slake2b
        with dissolve
        ri "Relaxing yourself."

        scene v9slake2g
        with dissolve

        u "Let me leave you to your relaxation a bit more. Weirdo."

        scene v9slake2d
        with dissolve

        ri "Weirdo!"

    call screen v9s7_lakeZoomIn

label fr5riley2:
    scene fr5lakezoomin

    u "(I've already talked to her.)"

    call screen v9s7_lakeZoomIn

# -if you click on Aubrey-
label fr5aubrey1:
    $ freeroam5.add("aubrey")

    scene v9slake4a # FPP close up aubrey swimming in the lake, very close to you, looking at you still on land. You're standing so she's looking up smiling, mouth closed.

    u "How's the water?"

    scene v9slake4 #same as 4a, mouth open
    with dissolve

    au "Nice and cool, just the way I like it."

    scene v9slake4a
    with dissolve

    u "Doesn't sound too nice, hm."

    scene v9slake4b # same as 4b aubrey flirting/teasing mouth open
    with dissolve

    au "Oh what, don't tell me that [name] is afraid of a bit of cold water?"

    scene v9slake4c # same as 4b mouth closed
    with dissolve

    u "What? Of course not!"

    scene v9slake4b
    with dissolve

    au "Boo-hoo, water is so cold, it would make his nipples sharp as a razor, boo-hoo."

    scene v9slake4c
    with dissolve

    u "Freeze the lake if you want, I'm not afraid of the water no matter how cold it is."

    scene v9slake4b
    with dissolve

    au "Prove it! Come and join me."

    scene v9slake4c
    with dissolve

    u "Oh yeah?"

    scene v9slake4b
    with dissolve

    au "Yeah."

    scene v9slake4c
    with dissolve

    menu: 
        "Don't join her":
            $ add_point(KCT.TROUBLEMAKER)

            u "That was a nice try, miss. But you must be mistaking me for a child, if you thought that would work."

            scene v9slake4d #same as 4b but aubrey booing mc (hands around her mouth, she's dissapointed)
            with dissolve

            au "Boo! Boo!"

            scene v9slake4e #same as 4d but mouth closed
            with dissolve

            u "Maybe some other time. I didn't bring my shorts, anyway."

            scene v9slake4b
            with dissolve

            au "You are such a party-pooper, [name]. I'll forgive you, though. But don't forget, you owe me one now."

            scene v9slake4c
            with dissolve

            u "Is that so? Owe you what?"

            scene v9slake4b
            with dissolve

            au "We'll see."

            scene v9slake4c
            with dissolve

            u "Sounds interesting. I guess we will see."

        "Join her":
            $ add_point(KCT.BOYFRIEND)

            u "Fine, let me just take my clothes off."

            scene v9slake4b
            with dissolve

            au "That's what I like to hear."

            scene v9slake5 #TPP showing mc and Aubrey floating in the water next to each other
            with fade

            pause 0.5

            scene v9slake6 #FPP close up Aubrey in the water, you're also in the water with her so the it should be quite close and same height, aubrey flirting, mouth open
            with dissolve

            au "So, how's the water?"

            scene v9slake6a #same as 6, mouth closed
            with dissolve

            u "Just like it was promised. Almost as cool as me."

            scene v9slake6
            with dissolve

            au "Oh, is that so? Well, I'm glad you like it."

            scene v9slake6a
            with dissolve

            u "If it's good to you, why would I be any different? So, why did you invite me here?"

            scene v9slake6b #same as 6, aubrey smiling, mouth open
            with dissolve

            au "I just thought it could be fun, you know. I was getting a bit lonely."

            scene v9slake6c #same as 6b, mouth closed
            with dissolve

            u "Well that can't be a good thing, especially if it's someone like you."

            scene v9slake6b
            with dissolve

            au "What do you mean \"like me\"? What am I like?"

            scene v9slake6c
            with dissolve

            u "Ever since I've met you, one thing was the same. Nothing was ever the same, when it comes to you."

            scene v9slake6b
            with dissolve

            au "Oh, getting philosophical?"

            scene v9slake6c
            with dissolve

            u "I just don't think a girl like you would want the world to stop. If anything, I'd say you'd want to spin it faster."

            scene v9slake6b
            with dissolve

            au "Then I guess you know me a bit better than I would expect."

            scene v9slake6c
            with dissolve

            u "For one living in the moment, I wouldn't say you expect much at all. Well, maybe you don't expect much, but you surely know how to seize the moment."

            if aubrey.relationship >= Relationship.FWB:
                label v9_aubrey_scene_lake:
                    $ sceneList.add("v9_aubrey")

                    scene v9slake6
                    with dissolve

                    au "Wow, you keep on surprising me, [name]. And you are right, I did think of something fun just now."

                    scene v9slake6a
                    with dissolve

                    u "What could that be?"

                    scene v9slake6b
                    with dissolve

                    au "It can't be told. It has to be shown. Come with me."

                    scene v9slake7 # They swim for a bit into a location between some rocks on the shore, where it's hard for anyone to see them, but they stay in water 
                    with Dissolve(1)

                    pause 0.5

                    scene v9slake8a # FPP close up, same as 6 from angle and closeness, just in new, more remote location. aubrey flirty mouth closed
                    with dissolve

                    u "What is this?"

                    if config_censored:
                        call screen censored_popup("v9s7_nsfwSkipLabel1")

                    scene v9slake8 # same as 8a, mouth open
                    with dissolve

                    au "It's my secret place. Do you like it?"

                    scene v9slake9 # Showing closeup only Aubrey's hand grabbing mc's crotch underwater
                    with vpunch

                    u "Oh I like THAT."
                
                    scene v9slake8
                    with dissolve

                    au "Come. Follow me."

                    scene v9slake16 #TPP mc and aubrey are lying next to each other on a large rock in the middle of the lake, mc's underpants need to be wet
                    with fade
                    
                    au "Now, where were we?"

                    image v9slake17vid = Movie (play="images/v9/scene 7/v9slake17vid.webm", loop = True, image = "images/v9/scene 7/v9slake17vidend.webp", start_image = "images/v9/scene 7/v9slake17vidstart.webp")
                    image v9slake18vid = Movie (play="images/v9/scene 7/v9slake18vid.webm", loop = True, image = "images/v9/scene 7/v9slake18vidend.webp", start_image = "images/v9/scene 7/v9slake18vidstart.webp")
                    image v9slake18vidfast = Movie (play="images/v9/scene 7/v9slake18vidf.webm", loop = True, image = "images/v9/scene 7/v9slake18vidend.webp", start_image = "images/v9/scene 7/v9slake18vidstart.webp")
                    image v9slake19vid = Movie (play="images/v9/scene 7/v9slake19vid.webm", loop = True, image = "images/v9/scene 7/v9slake19vidend.webp", start_image = "images/v9/scene 7/v9slake19vidstart.webp")
                    image v9slake19vidfast = Movie (play="images/v9/scene 7/v9slake19vidf.webm", loop = True, image = "images/v9/scene 7/v9slake19vidend.webp", start_image = "images/v9/scene 7/v9slake19vidstart.webp")

                    scene v9slake17vid # mc and aubrey make out animation
                    with dissolve
                    
                    $ grant_achievement("relaxing_day")

                    " "

                    scene v9slake18 # aubreys hand on mc's dick over wet underpants
                    with dissolve

                    au "Let's see what we got here."

                    scene v9slake18vid # aubrey handjob slow, TPP
                    with fade

                    u "Damn..."

                    " "

                    scene v9slake19vid # aubrey handjob slow, FPP
                    with dissolve

                    au "You like this?"

                    " "

                    scene v9slake18vidfast # aubrey handjob fast, TPP (Not rendered again)
                    with dissolve

                    u "Fuck, yeah. It feels soo good!"

                    " "

                    scene v9slake19vidfast # aubrey handjob fast, FPP
                    with dissolve

                    au "You like this?"

                    " "

                    scene v9slake20 # close up mc cumshot
                    with flash

                    pause 0.5

                    scene v9slake20a # same as 20, cum over aubrey's hand
                    with flash

                    pause 1.0

                    scene v9slake21a # FPP close up Aubrey looking at you, mouth closed flirty curious smile looking at mc
                    with dissolve

                    u "Wow..."

                    scene v9slake21 # same as 21a, mouth open
                    with dissolve

                    au "Haha, I knew you'd like it."

                    au "We should probably swim back before the others notice we're missing though."

                    scene v9slake21a
                    with dissolve

                    u "You sure you don't want me to do you?"

                    scene v9slake21 
                    with dissolve

                    au "Haha, don't worry. We'll just spend more time on me next time."

                    scene v9slake21a
                    with dissolve

                    u "That does sound fair, haha."

                label v9s7_nsfwSkipLabel1:
                    scene black
                    with dissolve

                    pause 0.3
                    $ renpy.end_replay()

            else:
                scene v9slake6b
                with dissolve

                au "Wow, you keep on surprising me, [name]."

                scene v9slake6c
                with dissolve

                u "One could say I'm full of surprises. But I think I just know how to figure out people I care about."

                scene v9slake6b
                with dissolve

                au "Oh, so you care about me?"

                scene v9slake6c
                with dissolve

                u "Oh, so I figured you out?"

                scene v9slake6b
                with dissolve

                au "I guess that is a double edged sword, ha."

                scene v9slake6c
                with dissolve

                u "That's life. Like, do you think Ryan ever thought I would ruin his view by jumping in here?"

                scene v9slake6d #same as 6b, aubrey curious, mouth open
                with dissolve

                au "What do you mean?"

                scene v9slake6e #same as 6d, mouth closed
                with dissolve

                u "He's been staring at you ever since we came here."

                scene v9slake6
                with dissolve

                au "Well who could blame him?"

                scene v9slake6a
                with dissolve

                u "True."

                scene v9slake6b
                with dissolve

                au "Ha, are you saying I'm hot?"

                scene v9slake6c
                with dissolve

                u "I'm not saying anything. But saying otherwise could be one lie over my weekly quota."

                scene v9slake6
                with dissolve

                au "Funny. Or should I say clever."

                scene v9slake6a
                with dissolve

                u "Some would say both."

                scene v9slake6b
                with dissolve

                au "Maybe, haha."

                scene v9slake6c
                with dissolve

                u "Well, I guess I should probably get out now. Explore the place a bit more, you know?"

                scene v9slake6b
                with dissolve

                au "Alright, see you later."

    call screen v9s7_lakeZoomIn

label fr5aubrey2:
    scene fr5lakezoomin

    # -if you click on Aubrey again, MC thinks to himself-
    u "(I should look around a bit more.)"

    call screen v9s7_lakeZoomIn

    # -if you click on the guy sleeping under the tree-

label fr5treeguy1:
    $ freeroam5.add("treeguy")

    scene v9slake10 # FPP close up of guy under the tree sleeping sitting leaned to the tree

    u "Hmm. Hello?"

    " "

    u "Should you be sleeping there?"

    scene v9slake10b # same as 10, guy looks up at you, mouth open, reluctant, annoyed
    with dissolve

    unknown "Worried about my health, son?"

    # -MC looks surprised that he even got an answer-

    scene v9slake10c # same as 10b, mouth closed
    with dissolve

    u "Well, yeah. That, and getting robbed, for instance."

    scene v9slake10b 
    with dissolve

    unknown "Nobody steals from me."

    scene v9slake10c
    with dissolve

    u "How can you be so sure?"

    scene v9slake10b
    with dissolve

    unknown "This is my neighborhood. If not for me, this place would not be the same."

    scene v9slake10c
    with dissolve

    u "What do you mean, the same?"

    scene v9slake10b
    with dissolve

    unknown "A few years back, this place was not so fine and dandy. To be honest, nobody wanted to live here."

    scene v9slake10c
    with dissolve

    u "How so?"

    scene v9slake10b
    with dissolve

    unknown "People wanna move to city, they don't see the beauty of the countryside no more."

    scene v9slake10c
    with dissolve

    u "Kind of make sense."

    scene v9slake10d # same as 10b, guy holds up his hands to mc, mouth open, determind look (please look at script)
    with dissolve

    unknown "You see these two hands, son? If you want something, you gotta grab it with these."

    scene v9slake10e #same as 10d, mouth closed
    with dissolve

    u "You've grabbed people?"

    scene v9slake10f # same as 10d, guy moves his hands down but determined look, slight smile, mouth open
    with dissolve

    unknown "Hah! No, son. You grab a rake. A shovel. A plow! Make the land beautiful and rich. Then land grabs the people for you."

    scene v9slake10g # same as 10f, mouth closed
    with dissolve

    u "Is that how you did it?"

    scene v9slake10f
    with dissolve

    unknown "I live at a farm down the road. Was the only farm left around here, but now it's just one of many."

    scene v9slake10g
    with dissolve

    u "I gotta say, that does sound pretty cool."

    scene v9slake10f
    with dissolve

    unknown "If the way ever takes you down that road, just a few miles from here, feel free to drop by. I will show you how to grab the people. And some ladies, hah."

    scene v9slake10g
    with dissolve

    u "Haha, alright."

    scene v9slake10f
    with dissolve

    unknown "Now if you don't mind, son. Wednesday is a rest day for me."

    scene v9slake10g
    with dissolve

    u "Sure. See ya around."

    call screen v9s7_lakeFull

# -if you click on the guy again, MC thinks to himself-
label fr5treeguy2:
    scene fr5lakefull

    u "(I should leave him alone.)"

    call screen v9s7_lakeFull

    # -if you click on the guy petting a dog-

label fr5dogwalker1:
    $ freeroam5.add("dogwalker")

    scene v9slake11a #FPP close up of dogwalker petting his dog excited, looking at the dog, mouth closed

    if v7_visited_shelter:
        u "Wait a second. Is that Oscar?!"

        scene v9slake11b # same as 11, dogwalker looks at you smiling, mouth open
        with dissolve

        unknown "Oh! You know my boy here?"

        scene v9slake11c #same as 11b, mouth closed
        with dissolve

        u "Who could forget that ugl- I mean, yeah. I've seen him at the shelter the other day."

        scene v9slake11b
        with dissolve

        unknown "What a coincidence. Well that's exactly where I've met Oscar as well!"

        scene v9slake11c
        with dissolve

        u "Right. So, you adopted him?"

        scene v9slake11b
        with dissolve

        unknown "I just could not resist. You see, people don't usually come running to me."

        scene v9slake11c
        with dissolve

        u "Uh-huh."

        scene v9slake11b
        with dissolve

        unknown "Or animals."

        scene v9slake11c
        with dissolve

        u "I see."

        scene v9slake11b
        with dissolve

        unknown "Or anyone. They most of the time avoid me."

        scene v9slake11c
        with dissolve

        u "Right..."

        scene v9slake11 # same as 11a, mouth open
        with dissolve

        unknown "But not Oscar, oh no! When he saw his daddy, he came running straight to me. Didn't you, Oscar, didn't you?!"

        scene v9slake11a
        with dissolve

        u "Who would have though. You do kind of look alike."

        scene v9slake11b
        with dissolve

        unknown "It was just like magic. I knew right away he was gonna be mine."

        scene v9slake11c
        with dissolve

        u "(I would say it goes the other way around.)"

        u "That's cute! Nice talking to you!"

    else:
        u "What a cute dog!" 

        scene v9slake11b
        with dissolve

        unknown "Thanks! I got him from the shelter just a few days ago!"

        scene v9slake11c
        with dissolve

        u "Oh, so you adopted him?"

        scene v9slake11b
        with dissolve

        unknown "I just could not resist. You see, people don't usually come running to me."

        scene v9slake11c
        with dissolve

        u "Uh-huh."

        scene v9slake11b
        with dissolve

        unknown "Or animals."

        scene v9slake11c
        with dissolve

        u "I see."

        scene v9slake11b
        with dissolve

        unknown "Or anyone. They most of the time avoid me."

        scene v9slake11c
        with dissolve

        u "Right..."

        scene v9slake11 # same as 11a, mouth open
        with dissolve

        unknown "But not Oscar, oh no! When he saw his daddy, he came running straight to me. Didn't you, Oscar, didn't you?!"

        scene v9slake11a
        with dissolve

        u "Who would have though. You do kind of look alike."

        scene v9slake11b
        with dissolve

        unknown "It was just like magic. I knew right away he was gonna be mine."

        scene v9slake11c
        with dissolve

        u "(I would say it goes the other way around.)"

        u "That's cute! Nice talking to you!"

        # what if you don't know oscar
    call screen v9s7_lakeFull

    # -back to free roam-

# -if you click on the guy again, MC thinks to himself-
label fr5dogwalker2:
    scene fr5lakefull

    u "(I'm not going near that dog again.)"

    call screen v9s7_lakeFull

# -doing all the conversations ends the free roam-
# -animation of time passing by for about 4 hours-
# -MC is sitting with Ryan on the picnic blanket, and Aubrey and Riley come and join you. It's starting to get darker.-

label fr5ryan3:

    scene v9slake12 #TPP showing aubrey, ryan, mc  and riley sitting on the picnic matt, it's evening now.
    with fade

    pause 0.5

    scene v9slake13 #FPP close up Ryan (only ryan) toasting with a beer, mouth open, smiling
    with dissolve

    ry "Here's to a great day!"

    scene v9slake14 #FPP close up Aubrey,(only aubrey) looking at her soda can dissapointed, mouth open
    with dissolve

    au "Why'd you give me soda?"

    scene v9slake13b #same as 13, Ryan looking at Aubrey, cheeky, mouth open
    with dissolve

    ry "It's the driver's juice."

    scene v9slake14b # same as 14, aubrey looking at Ryan funnily annoyed, mouth open
    with dissolve

    au "I don't have to drive, any of you could!"

    scene v9slake13b
    with dissolve

    # -Ryan is already chugging down his beer-

    ry "Boo Beeb (too late)."

    scene v9slake15 # FPP close up Riley (only riley) with beer in her hand, smiling mouth open talking to the group
    with dissolve

    ri "Today was certainly relaxing..."

    if "v9_aubrey" in sceneList:
        scene v9slake14d #same as 14b, now aubrey looking at you slight smile mouth open
        with dissolve

        au "And exciting."

        scene v9slake14e # same as 14d, mouth closed
        with dissolve

    else:
        scene v9slake15a # same as 15, mouth closed
        with dissolve

    u "Most of all, fun. Thanks for inviting me, you guys. I needed this."

    scene v9slake15b #same as 15, looks at mc (this is in first person), cheeky smile, mouth open
    with dissolve

    ri "Well, now you will know for the next time, always to say yes to all of my awesome proposals."

    scene v9slake15c # same as 15b, mouth closed
    with dissolve

    u "I'll have to think about it."

    scene v9slake14d
    with fade

    au "It's starting to get dark and chilly. What do you say we head back?"

    scene v9slake14e
    with dissolve

    u "Sure."

    scene v9slake15
    with dissolve

    ri "Let me grab our stuff."

    stop music fadeout 3

    jump v9_driving_home_lake
# -the scene continues in scene 8-