# SCENE 16: Shooting Range
# Locations: Shooting Range at the Pier, Pier Bathroom (External)
# Characters: KAREN (Outfit: 1), PENELOPE (Outfit: 2), IMRE (Outfit: 1), MC (Outfit: 5), THE BULLSEYE (Outfit: 1), DYLAN (Outfit: 1), HOTDOG VENDOR
# Time: Evening

label v16s16:
    scene v16s16_1 # TPP. Show Penelope and MC walking together then Imre and Karen walking together besides them infront of the SHOOTING RANGE/GALLERY, Imre awkward smile, mouth closed, Penelope, MC, and Karen slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v16s16_2 # FPP. Karen and Imre across from MC and Penelope as they all stand in front of the SHOOTING RANE, MC looking at Karen, Karen looking at Penelope (Out of MC's view), Karen neutral face, mouth open, Imre awkward smile, mouth closed.
    with dissolve

    dg3 "Oh, that soda's gone straight through me... I'm gonna go find the bathroom, okay guys?"

    scene v16s16_3 # FPP. Karen and Imre across from MC and Penelope as they all stand outside the SHOOTING RANGE, MC looking at Penelope, Penelope looking at Karen, Penelope slight smile, mouth closed.
    with dissolve

    pe "Do you want me to come with you?"

    scene v16s16_2
    with dissolve

    dg3 "No, it's okay. I saw it earlier. Thank you though."

    scene v16s16_4 # TPP. Show Karen walking away from the group towards the bathroom. Imre, Penelope, and MC watching Karen walk away, Karen neutral face, mouth closed, Imre awkward smile, mouth closed, Mc and Penelope slight smile, mouth closed. 
    with dissolve

    pause 0.75

    scene v16s16_5 # FPP. MC looking at Imre, Imre looking at MC, Imre neutral face, mouth open.
    with dissolve

    imre "*Sighs* Man..."

    scene v16s16_5a # FPP. MC looking at Imre, Imre looking at MC, Imre neutral face, mouth closed.
    with dissolve

    u "What?"

    scene v16s16_5
    with dissolve

    imre "Do you think she's angry about the hotdog thing?"

    scene v16s16_5a
    with dissolve

    menu:
        "Nah, it's fine":
            $ add_point(KCT.BRO)

            scene v16s16_5a
            with dissolve

            u "Haha, honestly? I think it's fine."

            scene v16s16_5
            with dissolve

            imre "Really?"

            scene v16s16_3a # FPP. MC looking at Penelope, Penelope looking at MC, Penelope confused, mouth open.
            with dissolve

            pe "Yeah, really?"

            scene v16s16_3b # FPP. MC and Penelope next to each other. Only Imre across from them, Karen gone. MC looking at Penelope, Penelope looking at MC, Penelope confused, mouth closed.
            with dissolve

            u "Yeah, seriously. If anything, she was just a little embarrassed that she knocked your food on the floor."

            scene v16s16_3c # FPP. MC and Penelope next to each other. Only Imre across from them, Karen gone. MC looking at Penelope, Penelope looking at MC, Penelope neutral face, mouth open.
            with dissolve

            pe "Yeah. That's probably what happened."

            scene v16s16_5
            with dissolve

            imre "Hmm, I guess."

            imre "I still would've eaten it though, haha!"

            scene v16s16_5a
            with dissolve

            u "I know, buddy... I know."

        "Definitely":
            $ add_point(KCT.TROUBLEMAKER)

            scene v16s16_5a
            with dissolve

            u "*Laughs* Definitely."

            scene v16s16_5
            with dissolve

            imre "Dude. Really?"

            scene v16s16_3d # FPP. MC looking at Penelope, Penelope looking at Imre, Penelope neutral face, mouth open.
            with dissolve

            pe "Imre... You tried to shove a piece of meat into her mouth."

            scene v16s16_5b # FPP. MC looking at Imre, Imre looking at Penelope, Imre neutral face, mouth closed.
            with dissolve

            imre "It was just a joke! I was trying to flirt..."

            scene v16s16_5a
            with dissolve

            u "Well, your idea of flirting is somehow forcing a vegan to taste a hot dog."

            scene v16s16_5
            with dissolve

            imre "*Sighs* I really screwed up, huh?"

            scene v16s16_5a
            with dissolve

            menu:
                "It's not over yet":
                    $ add_point(KCT.BRO)
                    scene v16s16_5a
                    with dissolve

                    u "I mean, yeah, you did. But that doesn't mean it's over."

                    scene v16s16_5
                    with dissolve

                    imre "How?"

                    scene v16s16_3d
                    with dissolve

                    pe "Imre, do you like the girl?"

                    scene v16s16_5b
                    with dissolve

                    imre "Yeah, of course."

                    scene v16s16_3d
                    with dissolve

                    pe "And is she worth the trouble of apologizing, and attempting to fix your mistakes?"

                    scene v16s16_5b
                    with dissolve

                    imre "Well, I thought so... But-"

                    scene v16s16_5a
                    with dissolve

                    u "She is or she isn't."

                    u "Don't let anything, or anyone for that matter, ever make you feel like you don't deserve the things you want in life."

                    scene v16s16_6 # TPP. Close up of Penelope's face as she looks at MC, Penelope with a nice bright smile as she blushes looking at MC, Penelope subtly biting her lip.
                    with dissolve

                    pause 0.75

                    if penelope.relationship >= Relationship.LIKES: ### TODO: Variable
                        scene v16s16_7 # TPP. Cute shot of just MC and Penelope, Penelope holding hands with MC and leaning into him, Penelope slight smile, blushing, MC slight smile, mouth closed.
                        with dissolve

                        pause 0.75

                    scene v16s16_5
                    with dissolve

                    imre "Ha. Yeah, you're right. I can make anything happen as long as I try."

                    scene v16s16_3e # FPP. MC looking at Penelope, Penelope looking at Imre, Penelope slight smile, mouth open.
                    with dissolve

                    pe "Yes! That's the smartest thing I've ever heard you say. *Laughs*"

                    scene v16s16_5c # FPP. Mc looking at Imre, Imre looking at MC, slight smile, mouth open.
                    with dissolve

                    imre "Thanks, [name]."

                "Yeah, it's over":
                    $ add_point(KCT.TROUBLEMAKER)
                    scene v16s16_5a
                    with dissolve

                    u "Big time, yeah. I think it's over."

                    scene v16s16_5
                    with dissolve

                    imre "But guys, I was just trying to be nice."

                    scene v16s16_3d
                    with dissolve

                    pe "Oh?"

                    scene v16s16_5b
                    with dissolve

                    imre "It takes a lot for me to want to share my food with someone."

                    scene v16s16_5a
                    with dissolve

                    u "Yeah, I can see that."

                    scene v16s16_3d
                    with dissolve

                    pe "Well, if you like her as much as you say you do... Maybe you should try a different way of communicating that to her."

                    scene v16s16_5c
                    with dissolve

                    imre "Hmm... You're right!"

                    if penelope.relationship >= Relationship.LIKES: ### TODO: Variable
                        scene v16s16_5d # FPP. Imre (slight smile, mouth open) leaning closer to MC and whispering in his ear.
                        with dissolve

                        imre "*Whispers* I like this one."

                        scene v16s16_5e # FPP. Imre (slight smile, mouth closed) leaning closer to MC and whispering in his ear
                        with dissolve

                        u "*Whispers* Ha. Me too."

                        scene v16s16_6a # TPP. Close up of Penelope's face (curious but with a smile, mouth closed) looking at Imre and MC 
                        with dissolve
                        
                        pause 0.75

                        scene v16s16_5d
                        with dissolve

                        imre "*Whispers* She might be a keeper..."

                        scene v16s16_5e
                        with dissolve

                        u "*Whispers* Hm, you think so?"

                        scene v16s16_5d
                        with dissolve

                        imre "*Whispers* Maybe, I don't know for-"

                        scene v16s16_3e
                        with dissolve

                        pe "Excuse me ladies, can we stop with gossip? I'm right here."

                        scene v16s16_5c
                        with dissolve

                        imre "*Coughs* So, yeah... Underwear. Red. You know?"

                        scene v16s16_5f # FPP. Mc looking at Imre, Imre (slight smile, mouth closed) looking at MC, 
                        with dissolve

                        u "... What?"

                        scene v16s16_3f # FPP. MC looking at Penelope, Penelope (flirty, mouth closed) looking at MC
                        with dissolve

                        pause 0.75

                        scene v16s16_5c
                        with dissolve

                        imre "So, anyway..."

    imre "I need to win her something, I think. Here at the shooting gallery, to get things back on track."

    scene v16s16_5f
    with dissolve

    u "Get things back on track? So, you're wanting to make it work?"

    scene v16s16_5c
    with dissolve

    imre "Uh... Pfft... Who knows?"

    scene v16s16_5f
    with dissolve

    u "..."

    scene v16s16_5c
    with dissolve

    imre "I don't know, dude. It would just be nice to win her something, I guess."

    imre "Maybe it'll make her feel better about the hotdog thing? And hopefully set things up nicely for a second date."

    scene v16s16_5f
    with dissolve

    u "(Wow... Imre's already thinking about a second date? And he hasn't even seen her naked yet??? True love does exist...)"

    scene v16s16_3e
    with dissolve

    pe "Go for it! Whatever you want to do, we support it."

    scene v16s16_8 # FPP. [Standing in front of the SHOOTING RANGE, MC looking at the vendor/The Bullseye on the RIGHT SIDE of the SHOOTING RANGE (man in the cowboy costume with a cowboy hat, if possible some nice old west facial hair, he has the rifle for the range)] BULLSEYE (slight smile, mouth open) looks at the MC. GUN is interchangable with PISTOL or RILFE depending on the prp chosen for the scene.
    with dissolve
    # -The shooting range vendor is wearing a cowboy costume (or normal clothes with cowboy hat), the "gun" is described as a rifle, if renders cannot match that description, please change it accordingly, cheex can help if needed-
    tb "Howdy partners! Welcome to the gallery made for shooting."

    tb "You can call me The Bullseye. Step right up to test y'all's rootin' tootin' shootin' skills and maybe you'll win yourself a prize!"

    scene v16s16_9 # FPP. [OC Penelope and MC stand between BULLSEYE and IMRE at the RANGE] MC Imre (Imre slight smile, mouth open) stepping up to BULLSEYE.
    with dissolve

    imre "Alright, give me a gun, bucko. I'm gonna win that huge teddy, fair and square!"

    scene v16s16_8
    with dissolve

    tb "It's not impossible to get on your first try, just believe in yourself."

    scene v16s16_8a # FPP. Show the BULLSEYE putting the gun on some table at the gallery to pick up (LEFT SIDE FACING GALLERY), BULLSEYE (slight smile, mouth closed).
    with dissolve

    pause 0.75

    scene v16s16_9a # FPP. Imre standing at the gallery, Imre's eyes closed, neutral face, mouth open.
    with dissolve

    imre "*Whispers* I believe..."

    scene v16s16_10 # TPP. Close up of Imre aiming with the gun, Imre neutral face, mouth closed.
    with dissolve

    pause 0.75

    play sound "sounds/gun.mp3"

    scene v16s16_11 # TPP. Shot of the targets, the first one getting hit.
    with dissolve

    pause 0.75

    scene v16s16_10
    with dissolve

    pause 0.75
    
    play sound "sounds/gun.mp3"

    scene v16s16_11a # TPP. Shot of the targets, the second one getting hit.
    with dissolve

    pause 0.75

    scene v16s16_10
    with dissolve

    pause 0.75

    play sound "sounds/gun.mp3"

    scene v16s16_11b # TPP. Shot of the tragets, the third one getting hit.
    with dissolve

    pause 0.75

    scene v16s16_9b # FPP. Show Imre cheering with the gun in one hand, slight smile, mouth open.
    with dissolve

    imre "Haha! Fuck yeah! Did you see that shit?"

    scene v16s16_12 # TPP. Show Imre and MC standing at the shooting gallery high fiving, Imre with the gun in the hand he isn't using to high five, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v16s16_8
    with dissolve

    tb "Easy on the cussin' there, sailor! And put down that rifle for me before you hurt yourself."

    scene v16s16_1a # TPP. Show MC and Penelope standing together by the shooting range Imre standing across from them and holding a huge teddy bear, Karen gone. All slight smile, mouth close.
    with fade

    pause 0.75

    scene v16s16_3e
    with dissolve

    pe "I can't believe you won it! I can't wait to see Karen's face, haha."

    scene v16s16_8
    with dissolve

    tb "Just goes to show what you can do once you set your mind to something."

    scene v16s16_5g # FPP. Mc looking at Imre (slight smile, mouth open), looking over at Bullseye.
    with dissolve

    imre "Haha! Cowboys are too fucking cool, man. Thanks Bullseye."

    scene v16s16_8
    with dissolve

    tb "Of course! Anyone else want to pull my trigger?"

    scene v16s16_3g # FPP. MC looking at Penelope (slight smile, mouth open) looking at MC
    with dissolve

    pe "Um... *Giggles*"

    scene v16s16_8b # FPP. MC looking at the Bullseye ( slight smile, mouth closed) looking at the MC and his friends
    with dissolve

    u "I don't know if I want to pull your trigger, but..."

    if penelope.relationship >= Relationship.LIKES: ###TODO: Variable
        scene v16s16_9c # FPP. MC looking at Penelope (winking, slight smile, mouth open) standing up to the shooting range who is looking at MC
        with dissolve

        pe "But... you're going to win me something, right?"

        scene v16s16_9d # FPP. MC looking at Penelope (Penelope slight smile, mouth closed) standing at the shooting range who is looking at MC
        with dissolve

        u "Pfft... Of course."

        scene v16s16_9e # FPP. MC looking at Penelope (Penelope slight smile, mouth open) standing at the shooting range who is looking at MC
        with dissolve

        pe "Haha, I'm kidding, you don't have to."

    scene v16s16_8
    with dissolve

    tb "Ah, come on! You've got to win a lady as pretty as she, a wonderful prize in order to make her happy."

    scene v16s16_8b
    with dissolve

    u "(Is this man a cowboy or a poet...?)"

    scene v16s16_9e
    with dissolve

    pe "At least give it a try, no pressure. We're getting the full experience today, remember? *Laughs*"

    scene v16s16_9d
    with dissolve

    u "Ha. Sure, okay. If I win, it's yours."

    scene v16s16_9e
    with dissolve

    pe "Yes! I mean... Deal. *Chuckles*"

    scene v16s16_8
    with dissolve

    tb "Our next gunslinger approaches! Let's see what he's got!"

    scene v16s16_5c
    with dissolve

    imre "Woohoo! You got this, [name], easily!"

    scene v16s16_9e
    with dissolve

    pe "Yeah, you got this."

    scene v16s16_8
    with dissolve

    tb "Remember, just believe..."

    scene v16s16_8a
    with dissolve

    pause 0.75

    scene v16s16_13 # FPP. MC aiming down the range at the targets with the gun (This is FPP-- do down the lenght of the gun using the sighting marks with the target)
    with dissolve

    pause 0.75

    if v16_win_range: ### TODO: Variable
        scene v16s16_9e
        with dissolve

        pe "Ahh! You actually did it!"

        scene v16s16_9d
        with dissolve

        u "You weren't expecting me too? *Laughs*"

        if penelope.relationship >= Relationship.LIKES: ### TODO: Variable
            scene v16s16_7a
            with dissolve

            pe "*Sighs* You know what I mean. You're amazing with a gun!"

            play sound "sounds/kiss.mp3"
            
            scene v16s16_7b # TPP. Show MC and Penelope kissing.
            with dissolve

            pause 0.75
            
            scene v16s16_9d
            with dissolve

            u "(Hmm, I guess I have done pretty well in the past with shooting.)"

        else:
            scene v16s16_7a # TPP. MC and Penelope hugging, Both slight smile, Penelope mouth open, MC mouth closed.
            with dissolve

            pe "*Sighs* You know what I mean. You're amazing with a gun!"

            scene v16s16_9d
            with dissolve

            u "(Hmm, I guess I have done pretty well in the past with shooting.)"
            
        scene v16s16_8
        with dissolve

        tb "Congratulations, partner! You're a regular Annie Oakley!"

        scene v16s16_8b
        with dissolve

        u "I'd say I'm a little more masculine than her, but I'll take the compliment, haha."

        scene v16s16_8
        with dissolve

        tb "Um, tough news though... I've kinda run out of the top prizes. Would you accept some candy?"

        scene v16s16_8b
        with dissolve

        u "It's not currently melting in your pocket, is it?"

        scene v16s16_8
        with dissolve

        tb "Um, no Sir. What a strange question..."

        scene v16s16_8b
        with dissolve

        u "It's been a strange day."

        scene v16s16_8
        with dissolve

        tb "Well, nothing strange here..."

        scene v16s16_8b
        with dissolve
        
        u "(Eh, that's debatable.)"

        scene v16s16_8d # FPP.MC at the SHOOTING RANGE looking at the Bullseye (slight smile, mouth open) looking at MC while placing a heart candy on the table
        with dissolve

        tb "And here's what I have left. It's a love heart!"

        scene v16s16_14 # FPP. MC looking down at the table with candy is on, Penelope grabbing the candy slight smile, mouth closed.
        with dissolve
        
        pause 0.75

        scene v16s16_9e
        with dissolve

        pe "Oh, yay! It has a wrapper on it!"

        scene v16s16_9d
        with dissolve

        u "Haha, thank God."

        scene v16s16_8
        with dissolve

        tb "Why wouldn't it have a wrap-"

        if penelope.relationship >= Relationship.LIKES: ### TODO: Variable, if Penelope RS
            scene v16s16_9e
            with dissolve

            pe "And it's s a cute little heart..."

            scene v16s16_9d
            with dissolve

            u "Almost like it was meant to be, huh?"

            scene v16s16_9e
            with dissolve

            pe "*Laughs* Yes. Me and this yummy heart. It was meant to be."

        scene v16s16_9f # FPP. Penelope (smiling, mouth closed) standing at the SHOOTING RANGE eating the candy.
        with dissolve

        pause 0.75

        scene v16s16_9e
        with dissolve

        pe "Mmm, it tastes like sour apples."

    else:
        scene v16s16_8b
        with dissolve

        u "Fuck..."

        scene v16s16_8
        with dissolve

        tb "Watch your profan-"

        scene v16s16_9d
        with dissolve

        u "I'm sorry, Pe."

        scene v16s16_9e
        with dissolve

        pe "Haha, it's okay! It wasn't about the prize anyway. I had a lot of fun."

        scene v16s16_9d
        with dissolve

        u "(The world doesn't deserve this girl... She's way too sweet!)"

        scene v16s16_8
        with dissolve

        tb "Yeah, there's no shame in losing, pal!"

        tb "Although, I'd hold off on applying for the police department for right now. *Laughs*"

        scene v16s16_5g
        with dissolve

        imre "Haha! Nice once."

        scene v16s16_8
        with dissolve

        tb "Get yourself a job serving drinks, you've got the looks for it."

        tb "And if you didn't, there's always work in re-shoeing horses."

        scene v16s16_8b
        with dissolve

        u "Yeah... Thanks. That's great advice."

    scene v16s16_5c
    with dissolve

    imre "Hey, guys. Karen's been gone a while now, should we go check on her?"

    scene v16s16_3e
    with dissolve

    pe "Oh, shit... You're right."

    scene v16s16_5f
    with dissolve

    u "Let's go find her."

    scene v16s16_3h # FPP. MC Looking at Penelope( slight smile, mouth open) pointing off somewhere.
    with dissolve

    pe "I think she went to the bathroom over here..."

    scene v16s16_15 # TPP. MC and Penelope walking to the bathroom, Imre beside them (holding the prize teddy bear he won), slight smile, mouth closed.
    with fade

    pause 0.75

    scene v16s16_16 # FPP. Penelope, MC and Imre by the bathrooms, Show Penelope (shocked, mouth open) pointing and looking ahead to something off camera
    with dissolve

    pe "*Gasps* Is that-"

    scene v16s16_17 # TPP. Upclose shot of Karen making out with a HOTDOG VENDOR. 
    with dissolve

    u "(Oh... Fuck.)"

    scene v16s16_18 # TPP. Close up of Imre's face, Imre's jaw dropped.
    with dissolve

    pause 0.75

    scene v16s16_18a # TPP. Close up of Imre's face, Imre sad, mouth closed.
    with dissolve

    pause 0.75

    scene v16s16_18b # TPP .Close up of Imre's face, Imre angry, mouth open.
    with dissolve

    imre "What the fuck?!"

    scene v16s16_19 # FPP. At the bathrooms Imre taking a step towards Karen's direction, Mc looking at Imre, Imre angry, mouth closed.
    with dissolve

    pause 0.75

    scene v16s16_19a # FPP. At the bathrooms, MC grabbing Imre's arm as he walks towards Karen's direction, Imre angry, mouth closed.
    with dissolve

    u "Imre, wait-"

    play sound "sounds/thud.mp3"

    scene v16s16_19b # FPP. At the bathrooms, Imre ripping his arm out of MC's grasp, Imre angry, mouth open.
    with vpunch

    imre "No! Wait for what?!"

    scene v16s16_16a # FPP. MC, Penelope, and Imre standing together at the bathrooms, MC looking at Penelope (neutral face, mouth closed) looking at Imre (off Camera).
    with dissolve

    pe "Imre-"

    scene v16s16_19c # FPP. At the bathrooms, MC looking at Imre, Imre looking (Imre shocked, mouth open) at Penelope (off camera)
    with dissolve

    imre "Are you not seeing this?! Are you not-"

    scene v16s16_19d # FPP. At the bathrooms, MC looking at Imre, Imre with his head in his hands, Imre stressed, mouth open.
    with dissolve

    imre "Are you not fucking seeing this?"

    scene v16s16_19e # FPP. At the bathrooms Imre standing infront of MC, MC looking at Imre, Imre looking at MC, Imre angry, mouth closed.
    with dissolve

    u "I am, I see it, Imre."

    scene v16s16_19f # FPP. At the bathrooms Imre standing infront of MC, MC looking at Imre, Imre looking at MC, Imre angry, mouth open. 
    with dissolve

    imre "What do I-"

    imre "I'm going to fucking kill that guy."

    scene v16s16_19f
    with dissolve

    menu:
        "Try to calm Imre":
            $ add_point(KCT.BRO)
            scene v16s16_19e
            with dissolve

            u "I know you're feeling a lot right now. You have every right to be pissed, but let's go be pissed somewhere else."

            scene v16s16_19f
            with dissolve

            imre "Ha! And let them continue?!"

            scene v16s16_16a
            with dissolve

            pe "If that's what she wants, Imre... Let her do it. Let her learn from this mistake. You deserve better than that."

        "Blame Karen, not him":
            $ add_point(KCT.TROUBLEMAKER)
            scene v16s16_19e
            with dissolve

            u "Well... I wouldn't blame the guy. I think he was just in the right place at the right time."

            scene v16s16_19f
            with dissolve

            imre "For real? The right place? The hot dog stand?"

            scene v16s16_16a
            with dissolve

            pe "Yeah... Why was she even- Nevermind..."

            scene v16s16_19e
            with dissolve

            u "I'm just saying, let's not get involved with this hot dog dude. Let's leave her here, and she can figure her own ride out."

    scene v16s16_19f
    with dissolve

    imre "This is bullshit!"

    scene v16s16_20 # TPP. Imre storming away from MC and Penelope (towards the PIER ENTRANCE), Imre angry, mouth closed, MC and Penelope, both neutral face, mouth closed.
    with dissolve

    pause 0.75

    scene v16s16_21 # TPP. Show Imre dunking the bear he won head first into the trash can, Imre angry, mouth closed.
    with dissolve

    pause 0.75

    scene v16s16_16b # FPP. Standing at the bathrooms, MC looking at Penelope, Penelope looking at MC, Penelope neutral face, mouth open.
    with dissolve

    pe "Oh, shit... This is bad, [name]."

    scene v16s16_16c # FPP. Standing at the bathrooms, MC looking at Penelope, Penelope looking at MC, Penelope neutral face, mouth closed.
    with dissolve

    u "(Yeah, it is.)"

    scene v16s16_16b
    with dissolve

    pe "You better go after him. I'll talk to Karen."

    scene v16s16_16c
    with dissolve

    u "Are you sure?"

    scene v16s16_16b
    with dissolve

    pe "Yeah, I just want to make sure she's being safe. Just do your best to calm him down."

    scene v16s16_16c
    with dissolve

    u "Okay, I'll try."

    scene v16s16_22 # FPP. MC turned around facing towards the PIER ENTRANCE.
    with vpunch

    pe "Hey!"

    scene v16s16_16c
    with dissolve

    u "Yeah?"

    if penelope.relationship >= Relationship.LIKES: ### TODO: Variable, if penelope rs
        scene v16s16_16d # FPP. Penelope and MC at the bathrooms, MC looking at Penelope, Penelope looking at MC, penelope slight smile, mouth open.
        with dissolve

        pe "Thanks for coming today."

        play sound "sounds/kiss.mp3"

        scene v16s16_16e # TPP. Penelope leaned forward kissing MC.
        with dissolve
        
        pause 0.75
        
    else:
        scene v16s16_16d
        with dissolve

        pe "Thank you for showing up."

    scene v16s16_16f # FPP. Penelope and MC at the bathrooms, MC looking at Penelope, Penelope looking at MC, Penelope slight smile, mouth closed.
    with dissolve

    u "Of course. I'm glad I did, haha."

    scene v16s16_16d
    with dissolve

    pe "*Sighs* Me too."

    pe "Okay, see you soon. Good luck."

    scene v16s16_16f
    with dissolve

    u "You too."

    scene v16s16_21a # TPP. Dylan taking the teddy bear out of the trashcan, Dylan full smile, mouth open.
    with dissolve

    dy "Together at last..."

    scene v16s16_21b # TPP. Dylan walking off with the beat, Dylan full smile, mouth closed.
    with dissolve

    pause 0.75

    jump v16s17