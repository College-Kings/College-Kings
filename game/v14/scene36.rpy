# SCENE 36: Jenny and mc in private lagoon pool
# Locations: The Lagoon
# Characters: JENNY (Outfit: Sexy Bikini/Denim Shorts), MC (Outfit: Swimming Trunks), LAUREN (Outfit: NUDE)
# Time: Evening/Night
# Render Count: 21 Unique, 88 Total

label v14s36:
    scene v14s36_1 # TPP. MC arrives at the lagoon and see's Jenny in the distant in a very sexy bikini standing next to the lagoon, looking at the water, not in the water yet, Jenny has denim shorts over the bikin bottom at this point, Jenny has a slight smile, mouth closed, Mc is wearing the same swimming trunks and shirt from the v14s35_5 render
    with dissolve

    pause 0.75

    play music "music/v13/Track Scene 41_3.mp3" fadein 2

    scene v14s36_2 # FPP. Mc walks up face to face to Jenny, Jenny see's MC and is now looking at him, full smile, mouth open
    with dissolve

    jen "Hey [name]! Such a nice spot, isn't it?"

    scene v14s36_2a # FPP. same as v14s36_2 Jenny's mouth is closed
    with dissolve

    u "Shit, Jenny... How'd you find this place?"

    scene v14s36_2
    with dissolve

    jen "I was literally just driving by and saw a sign for it. Apparently it's brand new so I wanted to enjoy it before it becomes the new hotspot."

    scene v14s36_2a
    with dissolve

    u "Well, I feel honored to be one of the first people to use it, haha."

    u "Are you planning on swimming?"

    scene v14s36_2
    with dissolve

    jen "Maybe. I thought I would but the water is a little colder than I expected. I will put my feet in though."

    scene v14s36_2a
    with dissolve

    u "That's a good idea. Let's start slow. *Laughs*"

    scene v14s36_3 # TPP. MC and Jenny are standing both put one foot into the water, no expressions, mouths closed
    with dissolve

    pause 0.75

    scene v14s36_3a # TPP. same as v14s36_3 MC and Jenny sit down and put both their feet in the water, slight smiles, mouths closed looking at each other
    with dissolve

    pause 0.75

    scene v14s36_4 # FPP. Mc is looking at Jenny, Jenny is looking at MC, Jenny, slight smile, mouth open
    with dissolve

    jen "Not too bad I guess."

    scene v14s36_4a # FPP. same as v14s36_4 Jenny's mouth is closed
    with dissolve

    u "So tell me, what made you wanna hang out tonight?"

    scene v14s36_4
    with dissolve

    jen "Honestly? I was just bored."

    scene v14s36_4a
    with dissolve

    menu:
        "Happy to help":
            $ add_point(KCT.BOYFRIEND)
            u "Oh, happy to help... Is Penelope busy today?"

        "Ouch, that hurts":
            $ add_point(KCT.TROUBLEMAKER)

            u "Ouch, can't believe I'm just a boredom reliever."

            scene v14s36_4
            with dissolve

            jen "Haha you're not. Well, just a bit maybe."

            scene v14s36_4a
            with dissolve

            u "So I assume Penelope's busy today?"

    scene v14s36_4
    with dissolve

    jen "Yeah, I tried texting her but she told me she was sleeping early."

    scene v14s36_4a
    with dissolve

    u "Oh, alright..."
    
    if penelope.relationship >= Relationship.LIKES and v11s23_penelope_date:
        u "(Maybe it's a good thing I didn't try calling her...)"

    scene v14s36_4b # FPP. same as v14s36_4 Jenny has a curious expression, mouth open
    with dissolve

    jen "Say, I've been noticing a lot of campaign stuff going on at SVC. I believe it's with the Chicks house?"

    scene v14s36_4c # FPP. same as v14s36_4b Jenny's mouth is closed
    with dissolve

    u "Yeah. Chloe, who is the current President, and Lindsey are running against each other for presidency."

    scene v14s36_4
    with dissolve

    jen "Hmm... I had a friend named Chloe when I was younger."

    scene v14s36_4a
    with dissolve

    u "Yeah?"

    scene v14s36_4
    with dissolve

    jen "Tall, blonde, and a true badass... We did pageants together when we were kids."

    scene v14s36_4a
    with dissolve

    u "Well, the Chloe I know is definitely a badass, or a bad bitch, depending on who you ask... *Laughs*."

    scene v14s36_4b
    with dissolve

    jen "Haha! Wait, no way... What's her last name?"

    scene v14s36_4c
    with dissolve

    u "Moralez?"

    scene v14s36_3b # TPP. same as v14s36_3a Jenny is shocked mouth open and grabs MC's leg as a reaction
    with dissolve

    pause 0.75

    scene v14s36_4d # FPP. same as v14s36_4 Jenny has a shocked expression, mouth open
    with dissolve

    jen "Get the fuck out of here! You're joking...?"

    scene v14s36_4a
    with dissolve

    u "Haha, nope. President of the Chicks, Homecoming Queen, and one of my close friends."

    scene v14s36_4
    with dissolve

    jen "This is crazy! Your Chloe is my Chloe..."

    scene v14s36_4a
    with dissolve

    u "*Laughs* Small world."

    scene v14s36_4
    with dissolve

    jen "I haven't seen her in years... What has she been up to?"

    scene v14s36_4a
    with dissolve

    u "Well, like I said, she's currently being challenged by a fellow Chick named Lindsey."

    scene v14s36_4e # FPP. same as v14s36_4 Jenny rolls her eyes, and laughs, mouth open
    with dissolve

    jen "Oh, pfft... *Laughs* There's no way she'll lose to some chick named Lindsey, haha."

    scene v14s36_4
    with dissolve

    jen "Chloe wins anything she puts her mind to. She's a do-whatever-you-gotta-do-to-win type of player."

    scene v14s36_4a
    with dissolve

    u "That definitely sounds like the Chloe I know, but Lindsey can't be taken too lightly. She's got a lot of supporters."

    scene v14s36_4f # FPP. same as v14s36_4 Jenny has a serious expression, mouth open, hand on her chin, looking slightly down and away from MC
    with dissolve

    jen "Chloe will focus on what's important and nothing else. I'm gonna have to see how I can get more involved in her campaign..."

    scene v14s36_4a
    with dissolve

    u "Haha, you and everyone else."

    scene v14s36_4g # FPP. same as v14s36_4 Jenny has a full smile, mouth open
    with dissolve

    jen "You're in a frat, aren't you?"

    scene v14s36_4h # FPP. same as v14s36_4a Jenny's mouth is closed
    with dissolve

    u "I am, yeah."

    scene v14s36_4g
    with dissolve

    jen "It's kinda weird but, I could never bring myself to join Greek life, but I always liked guys who did."

    scene v14s36_4h
    with dissolve

    u "Why's that?"

    scene v14s36_4
    with dissolve

    jen "Too many reasons to count, ha. But, I don't know... The frat boys always knew how to have fun."

    scene v14s36_4a
    with dissolve

    u "Some do."

    scene v14s36_4b
    with dissolve

    jen "Oh? Well, then what about you? Are you a fun one?"

    scene v14s36_4c
    with dissolve

    menu:
        "Yeah I am":
            $ v14_jennypoints += 1
            $ add_point(KCT.BRO)

            scene v14s36_4h
            with dissolve

            u "Yeah I am. I guess it depends on what you consider fun."

            scene v14s36_4g
            with dissolve

            jen "Well, I'm not some \"Chick\". *Chuckles*"

            jen "So what I consider fun is usually something wild and exhilarating. Like going to a strip club, spontaneous skinny dipping, stuff like that."

        "Not really":
            $ add_point(KCT.BOYFRIEND)

            scene v14s36_4a
            with dissolve

            u "Not really. I'm more of the reserved type I guess, because I like to focus on the serious stuff."

            scene v14s36_4i # FPP. same as v14s36_4 Jenny has a slightly upset expression, mouth open
            with dissolve

            jen "Oh, I see..."

            jen "Well, that's too bad."

    scene v14s36_4a
    with dissolve

    u "This is starting to make more and more sense..."

    scene v14s36_4
    with dissolve

    jen "What?"

    scene v14s36_4a
    with dissolve

    u "Your friendship with Penelope."

    u "You're the one that's secretly wild and leans on her for a bit of structure, and she's the structured one who leans on you for fun."

    scene v14s36_4g
    with dissolve

    jen "Haha..."

    jen "I've never taken the time to break down our friendship like that and look at it but, yeah. I guess you're right."

    scene v14s36_4h
    with dissolve

    u "Which is interesting, because I didn't get that vibe from you during the first impression."

    scene v14s36_4
    with dissolve

    jen "It's not something I show on first impression..."

    scene v14s36_4a
    with dissolve

    u "Haha, I see."

    u "I guess there's a lot you can get to know about a person if you see them more than a few times... Weird. *Laughs*"

    scene v14s36_4g
    with dissolve

    jen "*Laughs* How many times have we seen each other now?"

    scene v14s36_4h
    with dissolve

    u "Once."

    scene v14s36_4
    with dissolve

    jen "Well, it was more than once."

    scene v14s36_4a
    with dissolve

    u "I only remember the cafe... Oh! The meeting with the school board as well, I guess. We didn't meet up more than twice, right?"

    scene v14s36_4g
    with dissolve

    jen "I didn't ask how many times we've met up, I asked how many times we'd seen each other."

    scene v14s36_4h
    with dissolve

    u "(What is she talking about?)"

    scene v14s36_4
    with dissolve

    jen "And the answer to that question is three."

    scene v14s36_4a
    with dissolve

    u "Three...?"

    scene v14s36_4j # FPP. same as v14s36_4e Jenny has a slightly upset expression
    with dissolve

    jen "Oh, come on..."

    scene v14s36_4
    with dissolve

    jen "You don't remember that little picture I sent you while you were in Europe?"

    scene v14s36_4a
    with dissolve

    u "Oh... O-Oh! That's what you're talking about, haha. Well, that was an accident though, right?"

    scene v14s36_4k # FPP. same as v14s36_4f Jenny is slightly looking at Mc, with a shy expression, partially blushing
    with dissolve

    jen "True, yeah... But it wasn't a mistake."

    scene v14s36_4a
    with dissolve

    u "Huh?"

    scene v14s36_4
    with dissolve

    jen "Well, like..."

    jen "I'm not mad that it happened, and I don't regret it or anything. *Chuckles*"

    scene v14s36_4a
    with dissolve

    u "Wait... Why not?"

    scene v14s36_4g
    with dissolve

    jen "'Cause it's better that it was you rather than some creep, haha. At least it wasn't Imre or... What's his face..."

    scene v14s36_4h
    with dissolve

    u "Who's \"What's his face\"?"

    scene v14s36_4f
    with dissolve

    jen "Starts with an R, I think."

    scene v14s36_4a
    with dissolve

    u "Ryan?"

    scene v14s36_4g
    with dissolve

    jen "That's it! Yeah, at least It wasn't either of them."

    scene v14s36_4h
    with dissolve

    u "I mean, I don't blame you, but... Why don't you like them?"

    scene v14s36_4
    with dissolve

    jen "I wouldn't say I don't like them, but... I can just tell from what I do know about them, that they're not my kind of people."

    scene v14s36_4a
    with dissolve

    u "How do you know anything about them?"

    scene v14s36_4
    with dissolve

    jen "The same way I know things about you."

    scene v14s36_4a
    with dissolve

    u "And that is...?"

    scene v14s36_4g
    with dissolve

    jen "Penelope of course."

    scene v14s36_4h
    with dissolve

    u "Penelope isn't in a sorority and also chooses to miss out on a lot of those things. So I guess I don't see how she could know everyone so well, haha."

    scene v14s36_4g
    with dissolve

    jen "Penelope may be quiet but she has her ears to all the walls. She's very aware of the things around her."

    scene v14s36_4g
    with dissolve

    jen "And being the lover of gossip that I am, I'm always around to gather the tea."

    scene v14s36_4h
    with dissolve

    u "Haha, okay. Well, in that case..."

    scene v14s36_4a
    with dissolve

    u "I bet you've heard a lot from people other than Penelope."

    scene v14s36_4k
    with dissolve

    jen "I have. That's how I know that I can trust you and... You know, be myself."

    menu:
        "Not fair":
            $ v14_jennypoints += 1
            $ add_point(KCT.BOYFRIEND)

            scene v14s36_4a
            with dissolve

            u "Well, that's not fair."

            scene v14s36_4g
            with dissolve

            jen "Ha! What's not fair?"

            scene v14s36_4a
            with dissolve

            u "*Sighs* You know all this stuff about me and I know nothing about you."

            scene v14s36_4b
            with dissolve

            jen "So, you're saying that you want to get to know me?"

            scene v14s36_4c
            with dissolve

            u "That'd be nice, yeah. Of course."

        "You're a spy?":
            $ add_point(KCT.TROUBLEMAKER)

            scene v14s36_4a
            with dissolve

            u "What are you, a spy?"

            scene v14s36_4g
            with dissolve

            jen "What? No! I just hear things about everyone from everyone."

            scene v14s36_4h
            with dissolve

            u "Mhmm, good save."

            scene v14s36_4g
            with dissolve

            jen "*Chuckles* Whatever."

    scene v14s36_4
    with dissolve

    jen "Of course? Are you trying to make me feel special or something?"
    
    scene v14s36_4a
    with dissolve

    menu:
        "Yeah, or something...":
            $ v14_jennypoints += 1
            $ add_point(KCT.BOYFRIEND)

            scene v14s36_4h
            with dissolve

            u "Or something, yeah."

        "Just being a good friend":
            $ add_point(KCT.BRO)

            scene v14s36_4a
            with dissolve

            u "Haha, I'm just trying to be a good friend."

    if v14_jennypoints >= 3 or kct == "popular":
        if v14_jennypoints < 3:
            call screen kct_popup

        scene v14s36_3c # TPP same as v14s36_3a Jenny scoots closer to MC, looking down at his lap, slight smile mouth closed, Mc has a slightly concerned expression, mouth closed
        with dissolve

        u "(Huh?)"

        scene v14s36_3d # TPP. same as v14s36_3a Jenny has laid her head in MC's lap and is looking up at MC slight smile mouth closed, she has one foot in the water and one propped up on the side of the lagoon, one hand in the water and one laying across her stomach, Ms is looking down at Jenny slight smile mouth closed hands to his sides
        with dissolve

        pause 0.75

        scene v14s36_5 # FPP. Mc is looking down at his lap where Jenny has laid her head down in MC's lap, Mc's perspective can see her full head neck breasts and just below her navel/belly button, Jenny has one arm laying across her stomach and one dangling in the water below, Jenny is looking at MC slight smile mouth open
        with dissolve

        jen "I'm really happy you decided to come out tonight."

        jen "I'm kind of glad that Penelope turned me down, actually."

        scene v14s36_5a # FPP. same as v14s36_5 Jenny's mouth is closed
        with dissolve

        u "Ha. Why's that?"

        scene v14s36_5b # FPP. same as Jenny v14s36_5a reaches with her left hand and grabs Mc's right hand towards her chest
        with dissolve
        
        pause 0.75

        scene v14s36_5c # FPP. same as v14s36_5b Jenny places Mc's hand palm down between her breasts, and grazes the top of his hand with her fingers
        with dissolve

        jen "Well, honestly... I've been wanting to hang out with you like crazy."

        scene v14s36_5d # FPP. same as v14s36_5c Jenny looks slightly away from MC, and her fingers move to a slighlty different position but still on the top of MC's hand
        with dissolve

        jen "I didn't know you guys were going to be in Europe for that long, I thought it was gonna be like a weekend thing, so..."

        scene v14s36_5c
        with dissolve

        jen "I was excited to hang out with you after the Penelope stuff was settled and well, obviously it didn't happen till now."

        scene v14s36_5e # FPP. same as v14s36_5c Jenny's mouth is closed, and her fingers move to a slighlty different position but still on the top of MC's hand
        with dissolve

        u "Well, thank you. But also, why me?"

        scene v14s36_5d
        with dissolve

        jen "I still don't really know many people."

        scene v14s36_5e
        with dissolve

        u "You didn't go out and meet other people?"

        scene v14s36_5c
        with dissolve

        jen "I didn't really want to, haha. After meeting you and... You being so close with Penelope already... That's all I really need."

        scene v14s36_5d
        with dissolve

        jen "You're a loyal person that cares about your friends and you don't make stupid decisions that harm others."

        scene v14s36_5e
        with dissolve

        u "(Debatable...) Thank you Jenny but-"

        scene v14s36_5c
        with dissolve

        jen "On top of that, you dropped everything to come be with me in the middle of the night."

        scene v14s36_5d
        with dissolve

        jen "How could I want to be around anyone else?"

        menu:
            "Kiss her":
                $ jenny.relationship = Relationship.FWB
                $ sceneList.add("v14_jenny")
                
                if chloe.relationship >= Relationship.GIRLFRIEND or lauren.relationship >= Relationship.GIRLFRIEND or penelope.relationship >= Relationship.LIKES:
                    $ add_point(KCT.TROUBLEMAKER)
                else:
                    $ add_point(KCT.BOYFRIEND)

                label v14s36_sg:

                stop music fadeout 3
                play music "music/v14/Track Scene 25a_1.mp3" fadein 2

                scene v14s36_3h # TPP. same as v14s36_3d MC grabs Jenny's face and kisses her, both of their eyes are closed
                with dissolve

                pause 1.5

                play sound "sounds/kiss.mp3"
                scene v14s36_3i # TPP. same as v14s36_3h Jenny sits up and kisses MC some more
                with dissolve

                pause 1.5

                scene v14s36_3j # TPP. same as v14s36_3i MC is smiling while removing his shirt, Jenny watches mc take his shirt off with a smile on her face, happy expression
                with dissolve

                pause 1.5

                scene v14s36_4o # FPP. same as v14s36_4 Jenny blushes happily, increase to full smile, mouth open, looking at MC's chest
                with dissolve

                jen "Ha, wow..."

                scene v14s36_4p # FPP. same as v14s36_4o Jenny's mouth is closed
                with dissolve

                u "My bad, was I reading signals wrong?"

                scene v14s36_4g
                with dissolve

                jen "No! Not at all."

                scene v14s36_4
                with dissolve

                jen "I just..."

                scene v14s36_3k # TPP. same as v14s36_3j Jenny kisses MC's neck, close to his ear, Mc slight shocked expression mouth slightly open
                with dissolve

                jen "*Whispers* I didn't think you'd be down for this."

                u "(Oh fuuccckk...)"

                scene v14s36_3l # TPP. same as v14s36_3k Jenny kisses the other side of MC's neck, close to his jaw
                with dissolve

                jen "*Whispers* With us not really knowing each other that much..."

                u "Mhmm..."

                scene v14s36_3k
                with dissolve

                jen "*Whispers* But nonetheless, I'm really glad you are."

                scene v14s36_3l
                with dissolve

                u "*Moans*"

                scene v14s36_4q # FPP. same as v14s36_4 Jenny holds MC's face in her hands and looks at him smiling/flirty, mouth closed
                with dissolve

                u "Ha, I mean..."

                scene v14s36_4p
                with dissolve

                u "I feel like we've built a real connection tonight and along with everything we've already been through..."

                u "Something is there, I feel it. And I like it a lot."

                scene v14s36_3m # TPP. same as v14s36_3l Jenny and MC kiss passionately, mc has a hand around the small of her back, Jenny has a hand up on mc's cheek
                with dissolve

                jen "I'm usually the date first, dessert second, type of girl... but right now I'm feeling... Some type of way."

                scene v14s36_4p
                with dissolve

                u "*Laughs*"

                scene v14s36_4r # FPP. same as v14s36_4q Jenny's mouth is open
                with dissolve

                jen "Just promise me that this isn't the first and last time we'll get together, yeah?"

                scene v14s36_4p
                with dissolve

                u "I can easily promise that, 'cause I'm hoping for many nights like this in the future."

                scene v14s36_4s # FPP. Jenny backs up slightly and removes her denim shorts revealing a scar on her hip bone, Jenny slight smile mouth closed
                with dissolve

                pause

                scene v14s36_6 # FPP. Jenny has gotten into the water directly in front of mc looks at MC smiles and then removes her top, MC is looking at Jenny full smile, mouth closed
                with dissolve

                pause

                scene v14s36_6a # FPP. same as v14s36_6 Show Jenny in the water pulling MC's pants off, full smile, mouth open
                with dissolve

                jen "Don't worry about the suit. Come on."

                pause

                scene v14s36_7 # TPP. Mc gets into the water, Mc and Jenny are looking at each other, Full smiles, mouths closed, Jenny wraps her arms around the back of Mc's neck and head, Jenny also wraps her legs around mc's waist
                with dissolve

                pause

                image v14jenmo = Movie(play="images/v14/Scene 36/v14jenmo.webm", loop=True, image="images/v14/Scene 36/v14jenmoStart.webp", start_image="images/v14/Scene 36/v14jenmoStart.webp") # Jenny Makeout
                image v14jenmof = Movie(play="images/v14/Scene 36/v14jenmof.webm", loop=True, image="images/v14/Scene 36/v14jenmoStart.webp", start_image="images/v14/Scene 36/v14jenmoStart.webp") # Jenny Makeout spedup
                image v14jenmo2 = Movie(play="images/v14/Scene 36/v14jenmo2.webm", loop=True, image="images/v14/Scene 36/v14jenmo2Start.webp", start_image="images/v14/Scene 36/v14jenmo2Start.webp") # Jenny Makeout FPP
                image v14jenmo2f = Movie(play="images/v14/Scene 36/v14jenmo2f.webm", loop=True, image="images/v14/Scene 36/v14jenmo2Start.webp", start_image="images/v14/Scene 36/v14jenmo2Start.webp") # Jenny Makeout FPP spedup

                scene v14jenmo # Ignore as anim
                with dissolve
                if voice_acted:
                    $ renpy.sound.play("music/v14/va/Scene 36 - mo_slow_4loops.mp3", loop=True)
                pause

                u "We need to get these things off of you, don't we? Hmm..."

                stop sound
                scene v14jenmof # Ignore as anim
                with dissolve
                if voice_acted:
                    $ renpy.sound.play("music/v14/va/Scene 36 - mo_fast_4loops.mp3", loop=True)
                pause

                jen "*Chuckles* What are you-"

                stop sound
                scene v14jenmo2 # Ignore as anim
                with dissolve
                if voice_acted:
                    $ renpy.sound.play("music/v14/va/Scene 36 - mo_slow_4loops.mp3", loop=True)
                pause

                stop sound
                scene v14jenmo2f # Ignore as anim
                with dissolve
                if voice_acted:
                    $ renpy.sound.play("music/v14/va/Scene 36 - mo_fast_4loops.mp3", loop=True)
                pause

                stop sound
                scene v14s36_99
                with dissolve

                pause

                if config_censored:
                    call screen censoredPopup("v14s36_nsfwSkipLabel1")

                scene v14s36_lagsex_1 # TPP. MC starts to goes underwater, Jenny has a curious expression looking at Mc, mouth closed
                with dissolve

                pause

                scene v14s36_lagsex_1a # TPP. same as v14s36_lagsex_1 MC goes fully underwater, Jenny has a curious expression looking at the water, mouth open
                with dissolve

                pause

                scene v14s36_lagsex_1a
                with dissolve
                pause

                jen "Hello? What's happening..."

                scene v14s36_lagsex_1b # TPP. same as v14s36_lagsex_1 Jenny starts blushing, full smile, slightly jerks backwards, mouth open
                with dissolve
                pause

                jen "Hey! That tickles, haha! S-stop! What-"

                scene v14s36_lagsex_1c # TPP. same as v14s36_lagsex_1b Jenny has a shocked expression, mouth open
                with dissolve
                pause

                jen "*Gasps* Oh... My... GOD!"

                scene v14s36_lagsex_1d # TPP. same as v14s36_lagsex_1c MC comes up out of the water holding Jenny's bottoms in his mouth, one eybrow raised, looking at Jenny, Jenny holds both her hands to her cheeks, Jenny is blushing and has a shocked expression
                with dissolve

                pause

                scene v14s36_lagsex_1e # TPP. same as v14s36_lagsex_1d MC still has her bottoms in his mouth, Jenny has a finger seductively in her mouth, mouth open, full smile
                with dissolve
                pause
                
                jen "Well, well... That was a fancy little trick. *Laughs*"

                scene v14s36_lagsex_1f # TPP. same as v14s36_lagsex_1e Mc is holding her bottoms in the air in front of Jenny with one hand full smile mouth open, Jenny's mouth is closed biting her finger
                with dissolve
                pause

                u "Haha... Want 'em back?"

                scene v14s36_lagsex_1g # TPP. same as v14s36_lagsex_1f Jenny's mouth is open
                with dissolve
                pause

                jen "Nope, they belong to you now."

                scene v14s36_lagsex_1h # TPP. same as v14s36_lagsex_1g MC walks to Jenny, picks her up and places her on a rock near the edge, both full smiles mouths closed
                with dissolve

                pause

                scene v14s36_lagsex_2 # TPP. MC joins Jenny and sits next to her and they kiss a little while MC gets some boob action, Mc full smile mouth closed, Jenny full smile mouth slightly open
                with dissolve

                pause

                scene v14s36_lagsex_2a # TPP. same as v14s36_lagsex_2 MC leans back full smile mouth closed, Jenny grabs ahold of MC's cock, She playfully bites the tip of his cock while looking at MC
                with dissolve

                pause

                image v14jenbj = Movie(play="images/v14/Scene 36/v14jenbj.webm", loop=True, image="images/v14/Scene 36/v14jenbjStart.webp", start_image="images/v14/Scene 36/v14jenbjStart.webp") # Jenny Blowjob
                image v14jenbjf = Movie(play="images/v14/Scene 36/v14jenbjf.webm", loop=True, image="images/v14/Scene 36/v14jenbjStart.webp", start_image="images/v14/Scene 36/v14jenbjStart.webp") # Jenny Blowjob spedup
                image v14jenbj2 = Movie(play="images/v14/Scene 36/v14jenbj2.webm", loop=True, image="images/v14/Scene 36/v14jenbj2Start.webp", start_image="images/v14/Scene 36/v14jenbj2Start.webp") # Jenny Blowjob FPP
                image v14jenbj2f = Movie(play="images/v14/Scene 36/v14jenbj2f.webm", loop=True, image="images/v14/Scene 36/v14jenbj2Start.webp", start_image="images/v14/Scene 36/v14jenbj2Start.webp") # Jenny Blowjob FPP spedup

                scene v14jenbj # Ignore as anim
                with dissolve
                if voice_acted:
                    $ renpy.sound.play("music/v14/va/Scene 36 - bj_slow_4loops.mp3", loop=True)
                pause

                u "Jenny- Fffffuck, Jenny..."

                stop sound
                scene v14jenbjf # Ignore as anim
                with dissolve
                if voice_acted:
                    $ renpy.sound.play("music/v14/va/Scene 36 - bj_fast_4loops.mp3", loop=True)
                pause

                u "*Moans* Yes, holy shit..."

                stop sound
                scene v14jenbj2 # Ignore as anim
                with dissolve
                if voice_acted:
                    $ renpy.sound.play("music/v14/va/Scene 36 - bj_slow_4loops.mp3", loop=True)
                pause

                jen "*Gags*"

                stop sound
                scene v14jenbj2f # Ignore as anim
                with dissolve
                if voice_acted:
                    $ renpy.sound.play("music/v14/va/Scene 36 - bj_fast_4loops.mp3", loop=True)
                pause

                u "Ha... I... Shhhit..."

                u "You're so god damn sexy, Jenny... *Moans*"

                stop sound
                scene v14s36_lagsex_2b # TPP. same as v14s36_lagsex_2a Jenny stops, smiles, wipes her mouth, Mc full smile mouth closed
                with dissolve

                pause

                scene v14s36_lagsex_2c # TPP. same as v14s36_lagsex_2b Jenny gets on top of MC grabbing his cock and using her hand to guide mc's cock inside of her
                with dissolve

                pause

                scene v14s36_lagsex_2d # TPP. same as v14s36_lagsex_2c Jenny grabs mc's hands placing his hands around her waist, she rides him and they makeout
                with dissolve

                pause

                image v14jencg = Movie(play="images/v14/Scene 36/v14jencg.webm", loop=True, image="images/v14/Scene 36/v14jencgStart.webp", start_image="images/v14/Scene 36/v14jencgStart.webp") # Jenny Cowgirl
                image v14jencgf = Movie(play="images/v14/Scene 36/v14jencgf.webm", loop=True, image="images/v14/Scene 36/v14jencgStart.webp", start_image="images/v14/Scene 36/v14jencgStart.webp") # Jenny Cowgirl spedup
                image v14jencg2 = Movie(play="images/v14/Scene 36/v14jencg2.webm", loop=True, image="images/v14/Scene 36/v14jencg2Start.webp", start_image="images/v14/Scene 36/v14jencg2Start.webp") # Jenny Cowgirl FPP
                image v14jencg2f = Movie(play="images/v14/Scene 36/v14jencg2f.webm", loop=True, image="images/v14/Scene 36/v14jencg2Start.webp", start_image="images/v14/Scene 36/v14jencg2Start.webp") # Jenny Cowgirl FPP spedup

                scene v14jencg # Ignore as anim
                with dissolve
                if voice_acted:
                    $ renpy.sound.play("music/v14/va/Scene 36 - cg_slow_4loops.mp3", loop=True)
                pause

                jen "Fuck..."

                stop sound
                scene v14jencgf # Ignore as anim
                with dissolve
                if voice_acted:
                    $ renpy.sound.play("music/v14/va/Scene 36 - cg_fast_4loops.mp3", loop=True)
                pause

                u "Ha... You like that? *Moans*"

                stop sound
                scene v14jencg # Ignore as anim
                with dissolve
                if voice_acted:
                    $ renpy.sound.play("music/v14/va/Scene 36 - cg_slow_4loops.mp3", loop=True)
                pause

                jen "Yes... *Moans* Yes, [name]..."

                stop sound
                scene v14jencg2f # Ignore as anim
                with dissolve
                if voice_acted:
                    $ renpy.sound.play("music/v14/va/Scene 36 - cg_fast_4loops.mp3", loop=True)
                pause

                u "(These beautiful fucking tits...)"

                jen "*Gasps* Fuck, I'm- I'm cumming..."

                u "*Moans* Yes, baby..."

                jen "*Moans* Ohhh, fuck, [name]! *Panting* Fuck me, yes!"

                u "Mmm... Fuck, Jenny..."

                stop sound
                scene v14s36_lagsex_2e # TPP. same as v14s36_lagsex_2d Jenny stands up and offers MC a hand, both full smiles mouths open looking at each other
                with dissolve

                pause

                scene v14s36_lagsex_2f # TPP. same as v14s36_lagsex_2e Mc joins her and they kiss for a bit, butt squeezes, neck kissing
                with dissolve

                pause

                image v14jenjo = Movie(play="images/v14/Scene 36/v14jenjo.webm", loop=True, image="images/v14/Scene 36/v14jenjoStart.webp", start_image="images/v14/Scene 36/v14jenjoStart.webp") # Jenny Jerk Off
                image v14jenjof = Movie(play="images/v14/Scene 36/v14jenjof.webm", loop=True, image="images/v14/Scene 36/v14jenjoStart.webp", start_image="images/v14/Scene 36/v14jenjoStart.webp") # Jenny Jerk Off spedup
                image v14jenjo2 = Movie(play="images/v14/Scene 36/v14jenjo2.webm", loop=True, image="images/v14/Scene 36/v14jenjo2Start.webp", start_image="images/v14/Scene 36/v14jenjo2Start.webp") # Jenny Jerk Off FPP
                image v14jenjo2f = Movie(play="images/v14/Scene 36/v14jenjo2f.webm", loop=True, image="images/v14/Scene 36/v14jenjo2Start.webp", start_image="images/v14/Scene 36/v14jenjo2Start.webp") # Jenny Jerk Off FPP spedup

                scene v14jenjo # Ignore as anim
                with dissolve
                if voice_acted:
                    $ renpy.sound.play("music/v14/va/Scene 36 - jo_slow_2loops.mp3", loop=True)
                pause

                u "Ahh, fuck... Jenny! You're... You're gonna make me cum... *Moans*"

                stop sound
                scene v14jenjof # Ignore as anim
                with dissolve
                if voice_acted:
                    $ renpy.sound.play("music/v14/va/Scene 36 - jo_fast_2loops.mp3", loop=True)
                pause

                jen "Am I?"

                stop sound
                scene v14jenjo2 # Ignore as anim
                with dissolve
                if voice_acted:
                    $ renpy.sound.play("music/v14/va/Scene 36 - jo_slow_2loops.mp3", loop=True)
                pause

                u "Mmm- Yes! Yes, y-you are..."

                u "*Moans* Oh my fuck-"

                stop sound
                scene v14jenjo2f # Ignore as anim
                with dissolve
                if voice_acted:
                    $ renpy.sound.play("music/v14/va/Scene 36 - jo_fast_2loops.mp3", loop=True)
                pause

                jen "Do it then."

                u "Mmm! Jenny... *Moans* I'm cumming..."

                stop sound
                scene v14s36_lagsex_3 # FPP. MC cums and Jenny is there to catch it with her mouth open, tongue out, eyes open looking directly at mc
                with dissolve

                pause

                scene v14s36_lagsex_3a # FPP. same as v14s36_lagsex_3 Jenny closes her eyes and swallows Mc's cum
                with dissolve

                pause

                scene v14s36_lagsex_3b # FPP. same as v14s36_lagsex_3a Jenny is looking directly at Mc, full smile, biting a finger, motuh closed
                with dissolve
                pause

                jen "Mmm!"

                scene v14s36_lagsex_3c # FPP. same as v14s36_lagsex_3b Jenny has stopped biting her finger, mouth still closed
                with dissolve
                pause

                u "Ha... Damn, Jenny."

                scene v14s36_lagsex_3c
                with dissolve
                pause

                u "That was really nice, holy shit... *Panting*"

                scene v14s36_8 # TPP. Jenny kisses Mc on the cheek eyes closed while holding mc's hand, Mc full smile mouth closed
                with dissolve

                pause 0.75

                scene v14s36_8a # TPP. Jenny gets out of the water and is standing on the edge of the lagoon looking down at Mc still in the water, full smile mouth closed, mc is looking up at her full smile mouth closed
                with dissolve
                
                pause 0.75

                scene v14s36_9 # FPP. Mc looks up from where he is standing and see's a full body shot of Jenny, water glistening down her body, the scar on her hip bone from render v14s36_4s should be in the same place in this image, Jenny is looking down at Mc full smile mouth open
                with dissolve

                jen "We keep spending time together, who knows what we could get up to next."

                scene v14s36_9a # FPP. same as v14s36_9 Jenny's mouth is closed
                with dissolve

                u "I'm definitely looking forward to finding out."

                scene v14s36_9
                with dissolve

                jen "Good. Just stay loyal to your friends and stay loyal to me, and you'll be kept satisfied at all times. *Chuckles*"

                scene v14s36_9a
                with dissolve

                u "Haha... (I think) I can manage that."

                scene v14s36_9b # FPP. same as v14s36_9 Jenny uses her hands to cover her vagina and other arm to cover her breasts, mouth open, half smile, show her teeth possibly chattering 
                with dissolve

                jen "Okay, I'm freezing..."

                scene v14s36_9c # FPP. same as v14s36_9b Jenny's mouth is closed
                with dissolve

                u "Same. *Chuckles*"

                scene v14s36_10 # TPP. MC and Jenny put on their bottoms, use the clothes from render v14s36_1 slight smiles, mouths closed
                with dissolve

                pause 0.75

                label v14s36_nsfwSkipLabel1:

                scene v14s36_10a # TPP. same as v14s36_10 MC puts on his shirt and Jenny puts on her bikini top, use the clothes from render v14s36_1
                with dissolve

                pause 0.75

                stop music fadeout 3
                play music "music/v12/Track Scene 33_4.mp3" fadein 2

                scene v14s36_11 # FPP. Mc and Jenny are now both dressed, Jenny looking directly at mc, full smile, mouth open
                with dissolve

                jen "Thank you again for coming out with me tonight. After all of that, I have a lot on my mind that I need to process. *Chuckles*"

                scene v14s36_11
                with dissolve

                jen "I wasn't really expecting us to, you know... Do it, haha."

                scene v14s36_11a # FPP. same as v14s36_11 Jenny's mouth is closed
                with dissolve

                u "Ha, yeah... Me either."

                scene v14s36_11
                with dissolve

                jen "Have a good night, [name]."

                scene v14s36_11a
                with dissolve

                u "You too Jenny, I'll see you soon?"

                scene v14s36_11
                with dissolve

                jen "I hope so, yeah."

                scene v14s36_12 # FPP. Jenny walks away from mc looking back and waving goodbye, full smile, mouth closed
                with dissolve

                u "(My life is never dull, haha!)"

                $ renpy.end_replay()

            "Don't kiss her":
                $ jenny.relationship = Relationship.AWKWARD
                
                if chloe.relationship >= Relationship.GIRLFRIEND or lauren.relationship >= Relationship.GIRLFRIEND or penelope.relationship >= Relationship.LIKES:
                    $ add_point(KCT.BOYFRIEND)
                else:
                    $ add_point(KCT.TROUBLEMAKER)

                scene v14s36_5f # FPP same as v14s36_5c Jenny looks up at MC while her head is in his lap and cuffs her hand that was in the water around his cheek
                with dissolve

                u "Ha. um, sorry... it's kinda cold out here, don't you think?"

                scene v14s36_3e # TPP. same as v14s36_3a Jenny removes her hand and sits up, Jenny slightly embarrassed expression mouth closed looking away from MC, MC looking at Jenny no expression mouth closed
                with dissolve

                pause 0.75

                scene v14s36_4l # FPP. same as v14s36_4 Jenny is looking at mc, has an embarrassed expression, mouth open
                with dissolve

                jen "Umm, yeah. I, uh... I guess it is kinda cold."

                scene v14s36_4
                with dissolve

                jen "Maybe I should've brought more clothes, haha."

                scene v14s36_4a
                with dissolve

                u "Maybe we should-"

                scene v14s36_4
                with dissolve

                jen "I should probably get back anyway."

                scene v14s36_4a
                with dissolve

                u "Okay, yeah. I'll see you soon?"

                scene v14s36_4m # FPP. same as v14s36_4 Jenny has no expression, mouth open
                with dissolve

                jen "Right, yeah... For sure. Thanks again for coming."

                scene v14s36_4n # FPP. same as v14s36_4m Jenny's mouth is closed
                with dissolve

                u "Of course."

                scene v14s36_3f # TPP. same as v14s36_3 Jenny and mc have no feet in the water, are looking at each other, no expressions, mouths closed
                with dissolve

                pause 0.75

                scene v14s36_2b # FPP. same as v14s36_2 Jenny is looking at mc, no expression, mouth open
                with dissolve

                jen "Goodnight."

                pause 0.75

                scene v14s36_3g # TPP. same as v14s36_3f Jenny hugs MC awkwardly, trying not to fully hug him, Jenny and Mc no expressions mouths closed
                with dissolve

                pause 0.75

                scene v14s36_2c # FPP. same as v14s36_2b Jenny's mouth is closed
                with dissolve

                u "Goodnight."

    else:
        call screen kct_popup(required_kct="loyal")
        scene v14s36_4
        with dissolve

        jen "I'm so glad you came, [name]. This is a lot better than having to chill by myself, haha."

        scene v14s36_4a
        with dissolve

        u "Haha, I wouldn't want that. I appreciate the invite."

        scene v14s36_4g
        with dissolve

        jen "Good to know."

        scene v14s36_4
        with dissolve

        jen "It's starting to get a little cold... Maybe I should've brought more clothes. *Laughs*"

        scene v14s36_4a
        with dissolve

        u "If I had a jacket I'd help you out."

        scene v14s36_4g
        with dissolve

        jen "Haha, thanks. I should probably head on back anyway."

        scene v14s36_4a
        with dissolve

        u "Okay, yeah. It is a little late."

        scene v14s36_4
        with dissolve

        jen "A little, haha. Thanks for coming though."

        scene v14s36_4a
        with dissolve

        u "Of course."

        scene v14s36_3n # TPP. same as v14s36_3 Jenny gives MC a friendly, not romantic, hug slight smiles, mouths closed
        with dissolve

        pause 0.75

        scene v14s36_2
        with dissolve

        jen "Goodnight."

        scene v14s36_2a
        with dissolve

        u "Goodnight."

    scene v14s36_12a # FPP. same as v14s36_12 Jenny further walks away, her back is turned
    with dissolve

    pause 0.75

    if lauren.relationship >= Relationship.GIRLFRIEND:
        play sound "sounds/vibrate.mp3"

        scene v14s36_13 # FPP. MC looks at his phone and see's that Lauren is calling him
        with dissolve

        u "(Speaking of life never being dull...)"

        stop music fadeout 3
        play music "music/v12/Track Scene 33_3.mp3" fadein 2

        scene v14s36_14 # TPP. show Lauren in her bed naked sitting on her bed with her knees bent, one hand holding her phone, with the other hand on her clit, full smile mouth closed, looking between her legs, also show her laptop next to her
        with dissolve

        u "Hey babe, what's up?"

        scene v14s36_14a # TPP. same as v14s36_14 Lauren's mouth is open
        with dissolve

        la "My mind... is completely... and utterly... blown away right now."

        scene v14s36_14
        with dissolve

        u "Why's that?"

        scene v14s36_14a
        with dissolve

        la "Well, I've been watching porn all night long and I've seen some very... interesting things."

        scene v14s36_14b # TPP. same as v14s36_14 Lauren is now massaging one of her nipples, looking at the nipple she is massaging, mouth closed
        with dissolve

        menu:
            "What kind of things?":
                $ add_point(KCT.BOYFRIEND)

                u "Haha, what kind of things?"

                scene v14s36_14c # TPP same as v14s36_14b Laurens mouth is closed
                with dissolve

                la "Like, did you know that there's like hundreds of different sex positions and depending on the position, you can feel different things?"

            "You watching porn sounds hot":
                $ add_point(KCT.BRO)

                scene v14s36_14b
                #with dissolve
                
                u "You watching porn just sounds really hot."

                scene v14s36_14c # TPP same as v14s36_14b Laurens mouth is closed
                with dissolve

                la "I know... It kind of was. You should've been there."

                la "Did you know that there's like hundreds of different sex positions and depending on the position, you can feel different things?"


        scene v14s36_14b
        with dissolve

        u "What-"

        scene v14s36_14c
        with dissolve

        la "Some positions make it easier to get pregnant while others make it almost impossible!"

        scene v14s36_14d # TPP. same as v14s36_14b lauren grabs her throat gently, full smile mouth open
        with dissolve

        la "I wanna try so many things..."

        scene v14s36_14e # TPP. same as v14s36_14d Laurens mouth is closed
        with dissolve

        u "Really?"

        scene v14s36_14d
        with dissolve

        la "Really! So, I'm gonna need you to watch some stuff too and, you know..."

        la "Get some ideas of what you're comfortable with."

        scene v14s36_14e
        with dissolve

        u "Haha, okay. Alright."

        scene v14s36_14b
        with dissolve

        u "This is not at all like you, but I can't say I'm not enjoying it."

        scene v14s36_14c
        with dissolve

        la "Thank Amber for showing me this new world, but I think this is something that was hidden inside of me, deep down. I might be addicted to sex... *Laughs*"

        scene v14s36_14b
        with dissolve

        u "Well I really wanna come over now."

        scene v14s36_14c
        with dissolve

        la "Haha, I'm sure you do... But, I should've gone to bed a long time ago and here I am."

        scene v14s36_14
        with dissolve
        u "Watching porn."

        scene v14s36_14a
        with dissolve

        la "Exactly. So now I'm going to sleep."

        scene v14s36_14f # TPP. same as v14s36_14d Lauren licks her fingers
        with dissolve

        u "Fine, soon then."

        scene v14s36_14a
        with dissolve

        la "Very soon. Goodnight handsome."

        scene v14s36_14g # TPP. same as v14s36_14 Lauren puts her fingers inside of her pussy, her hand squeezing her phone, eye's closed, a look of ectasy comes over her face
        with dissolve

        u "Goodnight angel."

        scene v14s36_15 # TPP. Show MC putting his phone in his pocket, full smile, mouth open
        with dissolve

        u "Haha, wow. What a fucking night."

        scene v14s36_16 # TPP. Show mc leaving the lagoon entrance, full smile, mouth closed
        with dissolve

        pause 0.75

        scene v14s36_17 # TPP. Show mc walking on the sidewalk, full smile, mouth closed
        with dissolve

        pause 0.75

        scene v14s36_18 # TPP. Show MC seeing in the distance and waves at her, full smile, mouth open, Lindsey looks back and see's MC, slight smile, mouth closed
        with fade

        pause 0.75

        stop music fadeout 3

        jump v14s38

    else:
        scene v14s36_16
        with dissolve

        pause 0.75

        scene v14s36_17
        with dissolve

        pause 0.75

        scene v14s36_18
        with fade

        pause 0.75

        stop music fadeout 3

        jump v14s38