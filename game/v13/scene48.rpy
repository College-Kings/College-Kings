# SCENE 48: Aubrey and MC at the Beach
# Locations: The Beach
# Characters: MC (Outfit: 1), AUBREY (Outfit: 4), RYAN (Outfit: 1)
# Time: Evening

label v13s48:
    scene v13s48_1 # TPP. Show MC walking up to Aubrey on the beach, Both slight smile, mouth closed.
    with dissolve

    pause 0.75

    play music "music/v13/Track Scene 48.mp3" fadein 2

    scene v13s48_2 # FPP. MC looking at Aubrey, Aubrey looking at MC, Slight smile, mouth closed.
    with dissolve

    u "Hey there. You look awfully nice."

    scene v13s48_2a # FPP. Same as v13s48_2a, Aubrey slight smile, mouth open.
    with dissolve

    au "Haha, thank you."

    scene v13s48_2
    with dissolve

    u "I couldn't really tell if you needed my help with something or if you were just wanting to hang."

    scene v13s48_2a
    with dissolve

    au "A little bit of both. *Chuckles* I was wondering if you'd take pictures of me for my Kiwii?"

    scene v13s48_2
    with dissolve

    u "Yeah, I can do that."

    scene v13s48_2a
    with dissolve

    au "Great! Thank you..."

    if s12v32_get_aubrey_flowers:
        scene v13s48_3 # FPP. Show Aubrey turning her back to the MC and walking towards the water, slight smile, mouth closed.
        with dissolve

        u "(Aubrey and I obviously have a romantic connection... Only time will tell if she'll ever wanna be more than friends.)"
    else:
        scene v13s48_3 
        with dissolve

        pause 0.75

    scene v13s48_4 # FPP. MC and Aubrey standing close to the water, Aubrey slight smile, mouth open.
    with dissolve

    au "You think this is a good spot?"

    scene v13s48_4a # FPP. Same as v13s48_4, Aubrey slight smile, mouth closed.
    with dissolve

    u "*Laughs* You're the expert, not me."

    scene v13s48_4 
    with dissolve

    au "Haha, very true... We'll go with this then."

    scene v13s48_4b # FPP. Same as v13s48_4a, Show Aubrey handing MC her phone.
    with dissolve

    pause 0.75

    scene v13s48_4c # FPP. Same as v13s48_4b, Show MC taking Aubrey's phone, Aubrey slight smile, mouth open.
    with dissolve

    au "Are you sure you know what you're doing?"

    scene v13s48_4a
    with dissolve

    u "I'm sure it's not that hard, I think I can press a button or two. *Chuckles*"

    scene v13s48_4
    with dissolve

    au "When taking the pictures, just imagine the angles and poses you'd like to see me in and take a picture of that."

    scene v13s48_4a
    with dissolve

    u "That's easy enough."

    scene v13s48_4
    with dissolve

    au "And that's why men are the best photographers."

    scene v13s48_4a
    with dissolve

    u "*Chuckles*"

    scene v13s48_4
    with dissolve

    au "Are you ready?"

    scene v13s48_4a
    with dissolve

    u "Pfft. Are you ready?"

    scene v13s48_4
    with dissolve

    au "Haha, let's do this."

    scene v13s48_5 # TPP. Show MC holding up Aubrey's phone.
    with dissolve

    pause 0.75

    scene v13s48_6 # TPP. Camera angle only showing Aubrey in a seductive pose, Aubrey looking at MC holding the phone (off camera), flirty expression, mouth closed.
    with dissolve

    pause 0.7

    scene v13s48_6
    with flash

    pause 0.75
    
    menu:
        "Stay quiet":
            $ add_point(KCT.BRO)
            scene v13s48_6
            with dissolve

            u "(I'll let her work.)"

        "DAMNNN...!":
            $ add_point(KCT.BOYFRIEND)
            scene v13s48_6
            with dissolve
            
            u "Damnnn! You look good!"

            scene v13s48_6a # TPP. Same as v13s48_6, Aubrey slight smile, mouth open.
            with dissolve

            au "Stop before you make me blush! *Chuckles*"

            scene v13s48_6b # TPP. Same as v13s48_6a, Aubrey slight smile, mouth closed.
            with dissolve

            u "Sorry not sorry. It needed to be said."

            scene v13s48_6a
            with dissolve

            au "Haha, thank you."

    scene v13s48_6c # TPP. Same as v13s48_6, Aubrey different pose.
    with dissolve

    pause 0.7

    scene v13s48_6c
    with flash

    pause 0.7

    scene v13s48_6d # TPP. Same as v13s48_6c, Aubrey new pose.
    with dissolve

    pause 0.7

    scene v13s48_6d
    with flash

    pause 0.75

    scene v13s48_4
    with dissolve

    au "So... How do they look?"

    scene v13s48_4a
    with dissolve

    u "They look amazing so far. You're stunning!"

    scene v13s48_4
    with dissolve

    au "Aww... Can I see?"

    scene v13s48_4a
    with dissolve

    u "Yeah."

    scene v13s48_4d # FPP. Same as v13s48_4, Aubrey looking at her phone, slight smile, mouth open.
    with dissolve

    au "Oh, wow... I might have you do this for me more often."

    scene v13s48_4e # FPP. Same as v13s48_4d, Aubrey putting her phone down so she isn't looking at it anymore, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v13s48_4a
    with dissolve

    u "No problem. *Chuckles* My regular rate is one fifty a shoot but for you, I'll do seventy-five."

    scene v13s48_4
    with dissolve

    au "How generous... *Chuckles*"

    scene v13s48_4a
    with dissolve

    u "So, is that it?"

    scene v13s48_4
    with dissolve

    au "Well, that was the \"need you to do something\" part, but now it's time for the \"hang out with you\" part. *Laughs*"

    scene v13s48_4a
    with dissolve

    u "Haha, great. What'd you have in mind?"

    scene v13s48_4
    with dissolve

    au "Get in my bikini and tell you to meet me at the beach."

    au "That's about it. *Chuckles*"

    scene v13s48_4a
    with dissolve

    u "I like that plan so far. *Chuckles* How about we walk along the beach?"

    scene v13s48_4
    with dissolve

    au "Yes! I'm down."

    scene v13s48_7 # TPP. Show MC and Aubrey walking together down the beach, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v13s48_8 # FPP. Aubrey beside MC on the side showing the ocean, Aubrey looking at MC, MC looking at Aubrey, Aubrey slight smile, mouth closed.
    with dissolve

    u "Can I ask you something?"

    scene v13s48_8a # FPP. Same as v13s48_8, Aubrey slight smile, mouth open.
    with dissolve

    au "Go ahead."

    scene v13s48_8
    with dissolve

    u "How come you don't talk about yourself very often? Like, how you grew up... How you feel about all the drama going on in the sorority that you're the VP of... Etc."

    scene v13s48_8a
    with dissolve

    au "Ha... Well, to be honest..."

    scene v13s48_8a
    with dissolve

    au "My childhood was very basic and I'm trying my best to avoid the sister drama for as long as I can."

    scene v13s48_8
    with dissolve

    u "Gotcha, but now it'd be nice to actually get to know you a bit better."

    scene v13s48_8a
    with dissolve

    au "*Chuckles* Why do you wanna know me better?"

    scene v13s48_8
    with dissolve

    menu:
        "Because we're friends":
            $ add_point(KCT.BRO)
            u "Because we're friends and it'd be nice to know you a bit better. *Chuckles*"

        "Because I like you":
            $ add_point(KCT.BOYFRIEND)
            u "Because I like you, and it'd be nice to add more reasons why I like you to my list. *Chuckles*"

    scene v13s48_8a
    with dissolve

    au "What if you don't like the stuff I tell you? *Chuckles*"

    scene v13s48_8
    with dissolve

    u "Then I guess I'll have to fall back on the things I do like."

    scene v13s48_8a
    with dissolve

    au "*Chuckles* Well..."

    scene v13s48_8a
    with dissolve

    au "Like I said, my childhood was pretty basic. I had both parents, a suburban home, an older sister, I did cheerleading... Super basic stuff."

    scene v13s48_8a
    with dissolve

    au "My sister started modeling when she turned eighteen and it always sparked my interest, but I was worried it'd seem like I was just copying her."

    scene v13s48_8
    with dissolve

    u "That's a reasonable insecurity, but look at you now. You literally got offered a job while she was in the middle of a photoshoot."

    scene v13s48_8a
    with dissolve

    au "Yeah... You're right. *Chuckles*"

    scene v13s48_8
    with dissolve

    u "What subjects were you good at?"

    scene v13s48_8b # FPP. Same as v13s48_8, Aubrey different pose (Arm pose since they are walking), Aubrey slight smile, open.
    with dissolve

    au "You mean like, while I was in school?"

    scene v13s48_8c # FPP. Same as v13s48_8b, Aubrey slight smile, mouth closed.
    with dissolve

    u "Yeah."

    scene v13s48_8a
    with dissolve

    au "None. *Chuckles*"

    scene v13s48_8
    with dissolve

    u "Damn! Really? *Chuckles*"

    scene v13s48_8a
    with dissolve

    au "No wait, wait... I was good at PE."

    scene v13s48_8
    with dissolve

    u "Shit Aubs..."

    scene v13s48_8b
    with dissolve

    au "What? *Chuckles*"

    scene v13s48_8c
    with dissolve

    u "Is PE even considered a subject?"

    scene v13s48_8a
    with dissolve

    au "Haha! It was at my school."

    scene v13s48_8
    with dissolve

    u "*Chuckles* You don't even know what PE stands for, do you?"

    scene v13s48_8a
    with dissolve

    au "Yes I do..."

    scene v13s48_8
    with dissolve

    u "What?"

    scene v13s48_8a
    with dissolve

    au "It stands for..."

    scene v13s48_8
    with dissolve

    u "Phy-"

    scene v13s48_8a
    with dissolve

    au "I don't need any hints, [name]."

    scene v13s48_8
    with dissolve

    u "My bad, go on. *Chuckles*"

    scene v13s48_8a
    with dissolve

    au "..."

    scene v13s48_8
    with dissolve

    u "*Whistling*"

    scene v13s48_8b
    with dissolve

    au "Alright, fine! Fuck you. *Laughs* What does it stand for?"

    scene v13s48_8c
    with dissolve

    u "Physical education..."

    scene v13s48_8a
    with dissolve

    au "Pfft... I knew that."

    scene v13s48_8
    with dissolve

    u "Haha, right... So were you the cute cheerleader that wasn't all that smart? Or..."

    scene v13s48_8a
    with dissolve

    au "Just like any movie! I told you I was basic. *Chuckles*"

    scene v13s48_8
    with dissolve

    u "Basic is better than tragic."

    scene v13s48_8a
    with dissolve

    au "That's true. *Chuckles*"

    au "People like Nora didn't even have that. I'm not gonna spill her tea, but yeah."

    scene v13s48_8
    with dissolve

    u "You can spill some tea about the Chicks, though. *Chuckles*"

    u "What's the sway of things? Does it look like Lindsey has a chance?"

    scene v13s48_8a
    with dissolve

    au "A chance would be an understatement. Honestly, I'm thinking she'll win."

    scene v13s48_8
    with dissolve

    u "What makes you say that?"

    scene v13s48_8a
    with dissolve

    au "All of the girls support her. Even the ones that have promised to vote for Chloe, still deep down want Lindsey to win."

    au "Chloe is getting a shit ton of votes based on pity and loyalty, but not faith in her leadership. People actually believe in Lindsey."

    scene v13s48_8
    with dissolve

    u "That's kinda surprising with her being so new compared to Chloe, right?"

    scene v13s48_8a
    with dissolve

    au "Well with her being a legacy, it helps a lot and with her mother passing away, she's getting a few pity votes as well."

    scene v13s48_8
    with dissolve

    u "Sheeeeesh. Guess we're gonna be biting our nails on this one?"

    scene v13s48_8a
    with dissolve

    au "And this is why I don't talk about it. *Chuckles* Too much drama."

    scene v13s48_8
    with dissolve

    u "It is a lot to take in."

    scene v13s48_8a
    with dissolve

    au "Yeah..."

    scene v13s48_8
    with dissolve

    menu :
        "Get her chocolates":
            $ aubrey.points += 1
            $ add_point(KCT.BOYFRIEND)
            $ v13s48_get_aubrey_chocolate = True

            u "Wait right here okay?"

            scene v13s48_8d # FPP. Same as v13s48_8, Aubrey confused expression, mouth open.
            with dissolve

            au "Oka-"

            scene v13s48_9 # TPP. Show MC walking towards the chocolate stand
            with dissolve

            pause 0.75

            scene v13s48_10 # FPP. MC looking at the chocolate stand with no one behind the counter.
            with dissolve

            u "(There's nobody here. Guess it's an honor system.)"

            scene v13s48_10a # FPP. Same as v13s48_10, MC puts some money down.
            with dissolve

            pause 0.75

            scene v13s48_10b # FPP. Same as v13s48_10a, MC taking the chocolates.
            with dissolve

            pause 0.75

            scene v13s48_9a # TPP. Same as v13s48_9, MC walking away from the chocolate stand
            with dissolve

            pause 0.75

            scene v13s48_11 # TPP. MC handing the chocolates to Aubrey, Aubrey slight smile, mouth closed, MC slight smile, mouth open.
            with dissolve

            u "Here you go..."

            scene v13s48_8e # FPP. Same as v13s48_8a, Aubrey looking down at the Chocolates (Chocolates in her hands off camera), Aubrey slight smile, mouth open.
            with dissolve

            au "What's this for?"

            scene v13s48_8f # FPP. Same as v13s48_8e, Aubrey slight smile, mouth closed.
            with dissolve

            u "Just getting a snack for a snacc."

            scene v13s48_8a
            with dissolve

            au "*Laughs* That was actually funny... Nice job."

            scene v13s48_8
            with dissolve

            u "I was going for something more romantic, but funny works too. *Chuckles*"

            scene v13s48_8a
            with dissolve

            au "*Chuckles* It was both."

            scene v13s48_8
            with dissolve

            u "So you're starting to warm up to me, huh?"

            scene v13s48_8b 
            with dissolve

            au "Don't push it, mister."

            scene v13s48_8c
            with dissolve

            u "*Chuckles* Yes ma'am."

        "(That's too much...)":
            u "(I'm not getting her chocolates. *Chuckles* That's doing too much.)"

    u "You know what would be really cool to do in Amsterdam?"

    scene v13s48_8b
    with dissolve

    au "What?"

    scene v13s48_8c
    with dissolve

    u "Canoeing, and then maybe a little picnic."

    scene v13s48_8a
    with dissolve

    au "Sounds kinda romantic don't you think?"

    if aubrey.relationship.value >= Relationship.FWB.value:
        au "I know we're fucking, but..."

        scene v13s48_8
        with dissolve
        
        menu:
            "I meant as friends":
                $ add_point(KCT.BRO)

                u "I meant it as friends."

                scene v13s48_8a
                with dissolve

                au "Mhmm, okay. *Chuckles* When are you thinking about going?"

            "I meant as a date":
                $ add_point(KCT.BOYFRIEND)

                scene v13s48_8
                #with dissolve

                u "I meant it as a date."

                if s12v32_get_aubrey_flowers and v13s48_get_aubrey_chocolate:
                    $ v13s48_canoeing_as_date = True

                    scene v13s48_8a
                    with dissolve
                    
                    au "You've been working overtime trying to \"woo\" me, huh?"

                    scene v13s48_8
                    with dissolve

                    u "How am I doing? Feeling \"woo'd\" yet?"

                    scene v13s48_8a
                    with dissolve

                    au "*Chuckles* When are you wanting to have this... date?"

                else:
                    scene v13s48_8a
                    with dissolve

                    au "We can go as friends. When are you thinking about going?"

    scene v13s48_8
    with dissolve

    u "Tomorrow maybe?"

    scene v13s48_8a
    with dissolve

    au "That works, sure."

    scene v13s48_8
    with dissolve

    u "Oooh, now I'm excited. *Chuckles*"

    if v10s33_ryan_flirt_emily and emily_europe:
        play sound "sounds/vibrate.mp3"

        scene v13s48_8
        with dissolve

        u "One second, I'm popular today. *Chuckles*"

        scene v13s48_12 # TPP. Show Ryan at Hotel holding phone to his ear, slight smile, mouth closed.
        with dissolve

        u "Hello?"

        scene v13s48_12a # TPP. Same as v13s48_12, Ryan slight smile, mouth open.
        with dissolve

        ry "Hey man, just wanna make sure you're still sure about your decision regarding our date?"

        ry "I thought I'd ask again 'cause I really do want you there, but I wanna be sure you're comfortable first."

        menu :
            "Go on the date":
                $ add_point(KCT.BRO)
                $ v13s48_ryan_double_date = True

                scene v13s48_12
                with dissolve
                
                u "Yes Ryan, I'll go. Did you already invite Riley?"

                scene v13s48_12a
                with dissolve

                ry "I did, I have her on hold waiting for your answer... So, I'll see you soon."

                scene v13s48_12
                with dissolve

                u "Alright, sounds good."

            "Don't go on the date":
                $ add_point(KCT.BOYFRIEND)

                scene v13s48_12
                with dissolve
                
                u "Yeah man, I'm not feeling too comfortable about it."

                scene v13s48_12a
                with dissolve

                ry "I understand, this is why I wanted to ask again."

                scene v13s48_12
                with dissolve

                u "Thanks man."

                scene v13s48_12a
                with dissolve

                ry "No worries."

    scene v13s48_8
    with dissolve

    u "Are you ready to go?"

    scene v13s48_8a
    with dissolve

    au "I am, yeah. I'm kinda starting to get cold. *Chuckles*"

    scene v13s48_8
    with dissolve

    u "Well, let's get you back before you freeze. *Chuckles* I wish I had some sort of jacket."

    scene v13s48_7
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v13s49