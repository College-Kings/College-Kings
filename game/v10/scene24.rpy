# SCENE 24: Lauren's Room
# Location: Lauren Bedroom
# Characters: MC (Outfit X), Lauren, (Outift X), Samantha (Outfit X), Ms. Rose (Outfit X)
# Time: Tuesday Evening

label v10_lauren_room:
    scene v10lar1 # TPP Show MC knocking on Lauren's door.
    with fade
    play music "music/v10/Track Scene 24_1.mp3" fadein 2
    play sound "sounds/knock.mp3"
    
    pause 0.75
    
    scene v10lar2 # FPP Show Lauren answering the door smiling, mouth open
    with dissolve

    la "Heyyyy."

    if lauren.relationship >= Relationship.GIRLFRIEND: # If in a relationship with Lauren
        scene v10lar1a # TPP Same angle as v10lar1: MC and Lauren kiss at her door
        with dissolve

        play sound "sounds/kiss.mp3"

        pause 0.75

    scene v10lar2a # FPP Same angle and expression as v10lar2, Lauren mouth closed
    with dissolve

    u "Hey Lauren."

    scene v10lar3 # FPP MC and Lauren sitting on her bed. Show Lauren in her room, Lauren looking slightly embarrassed, mouth open
    with fade

    la "Okay I'm gonna confess, I had a little bit of a motive in having you come over."

    scene v10lar3a # FPP Same angle and expression as v10lar3, Lauren mouth closed
    with dissolve

    u "Oh really? What's up?"

    scene v10lar3
    with dissolve

    la "Well, I looked into both the living statue and the bake sale for the charity event."
    la "I even spoke to my sister about it. I decided I'm just going to go ahead and do the bake sale."

    la "It's the least nerve wrecking thing of the two. Plus, it'll raise more money."

    scene v10lar3a
    with dissolve

    menu:
        "Agree":
            $ v10s33_laurenBakeSale = True

            $ reputation.add_point(Reputations.BOYFRIEND)
            scene v10lar3a
            with dissolve

            u "That seems like a good idea."

            scene v10lar3b # FPP Same angle as v10lar3, Lauren smiling with mouth open
            with dissolve

            la "Glad you think so too."

        "Push back":
            scene v10lar3a
            with dissolve
                
            u "Wait really?"

            scene v10lar3
            with dissolve

            la "I don't know, I'm just nervous about being eyeballed by so many people."

            scene v10lar3a
            with dissolve

            u "Don't even think about them. Think about the event."

            scene v10lar3
            with dissolve

            la "You really think it's a good idea?"

            scene v10lar3a
            with dissolve

            u "I really do."

            if lauren.relationship >= Relationship.GIRLFRIEND or kct == "loyal":
                if lauren.relationship < Relationship.GIRLFRIEND:
                    call screen reputation_popup
                $ v10s33_laurenBakeSale = False

                scene v10lar3b
                with dissolve
                
                la "Okay, I'll trust you on this one."

                scene v10lar3c # FPP Same angle and expression as v10lar3b, Lauren mouth closed
                with dissolve

                u "I'm sure it'll be fun."

            else: # KCT not Loyal
                $ v10s33_laurenBakeSale = True

                scene v10lar3d #FPP Same angle as v10lar3, Lauren looking down, sad expression, mouth open
                with dissolve

                la "Hmm, I don't know. I think I'm just gonna go with the bake sale."

                scene v10lar3a
                with dissolve

                u "*Sighs* Alright."

    # Continue after choice
    scene v10lar3
    with dissolve

    la "I'm hoping this event will let me connect more with my sister."
    la "We're close, but since college started I've noticed we've had very little time for each other."

    la "It's one of the reasons I wanted to join the Deers."

    scene v10lar3a
    with dissolve

    u "Do you ever get a chance to hang out with her?"

    scene v10lar3
    with dissolve

    la "Not really. She's either in the library busy, at a protest, doing Deer stuff or in class."
    la "I thought if I get involved in some of the things she's involved in we'd have more time for each other."

    scene v10lar3c
    with dissolve

    u "Not a bad idea haha."

    scene v10lar3b
    with dissolve

    la "Let's hope it actually works out."

    scene v10lar3c
    with dissolve

    u "The mud wrestling is Autumn's event right? So that'd probably be a good way for you to get closer with her. *Chuckles*"

    scene v10lar3
    with dissolve

    la "Oh uhm, I wasn't even considering that to be honest."

    scene v10lar3a
    with dissolve

    u "Why not? *Laughs*"

    scene v10lar3d
    with dissolve

    la "Just not really my thing you know..."

    menu:
        "Encourage her":
            $ reputation.add_point(Reputations.TROUBLEMAKER)
            scene v10lar3c
            with dissolve

            u "I think you should."

        "Let her decide":
            scene v10lar3c
            with dissolve

            u "Hey, do what makes you happy."

    # Continue after choice
    scene v10lar3f # FPP Same angle as v10lar3, Lauren laughing and rolling her eyes, mouth open
    with dissolve

    la "Could you really imagine it? Me? In a mud wrestling contest?"

    scene v10lar3c
    with dissolve

    u "I bet you'd be really good. *Laughs*"

    scene v10lar3b
    with dissolve

    la "I don't even know how to wrestle, how could I be good?"

    scene v10lar3c
    with dissolve

    u "You never know until you try."

    if lauren.relationship >= Relationship.KISS:
        label v10_lauren_room_sg:
            if _in_replay:
                $ lauren.relationship = Relationship.GIRLFRIEND

    if lauren.relationship >= Relationship.KISS: # If dating or have made out        
        scene v10lar3g # FPP Same angle as v10lar3, Lauren looking seductive, mouth open
        with dissolve

        la "*Mischievously* You know what? You're right."

        scene v10lar4 # TPP Show Lauren tackling MC, both smiling, Lauren climbing on top
        with dissolve

        pause 0.75

        scene v10lar4a # TPP Same angle as v10lar4, Lauren and MC wrestling in a sexy way on the floor, Lauren mouth open
        with dissolve
    
        la "*Mischievous* Guess I should practice."

        scene v10lar5 # FPP Show Lauren laying on the ground, close up on face from above, Lauren smiling, mouth closed
        with dissolve

        u "Aww, should I go easy on you?"

        scene v10lar4a
        with dissolve

        la "No need to."

        scene v10lar6 # FPP Show Lauren's face close up from below, as if pinned underneath her, Lauren with a big smile, mouth closed
        with dissolve 

        u "Oh no, you're too strong, I give up. *Laughs*"

        scene v10lar6a # FPP Same angle and expression as v10lar6, Lauren mouth open
        with dissolve

        la "*Laughs*"

        scene v10lar6b # FPP Same angle as v10lar6, Lauren with a seductive look, mouth closed
        with dissolve

        u "Lauren are we-"

        scene v10lar4b # TPP Same angle as v10lar4, Lauren and MC making out on the floor
        with dissolve

        u "(Oh wow!)"

        if config_censored:
            call screen censored_popup("v10s24_nsfwSkipLabel1")

        scene v10lar7 # TPP Show Lauren on MC's lap facing him, MC arms around her waist, Lauren eyes closed and mouth open
        with dissolve

        la "*Moans*"

        scene v10lar7a # TPP Same angle as v10lar7, Lauren with her arms up while MC removes her shirt while they kiss
        with dissolve

        u "(Let's get rid of this.)"

        scene v10lar7b # TPP Same angle as v10lar7, MC leaning back slightly and removing Lauren's bra, Lauren smiling, mouth open
        with dissolve

        la "Someone's excited."

        scene v10lar7c # TPP Same angle as v10lar7, Lauren now topless, eyes closed and mouth open, MC gently cupping her breast
        with dissolve

        la "Oh [name]! *Moans*"
        stop music fadeout 3
        play music "music/v10/Track Scene 24_2.mp3" fadein 2
        menu:
            "Suck on her tits":
                $ sceneList.add("v10_lauren")

                # MC starts kissing around her boobs and nipples. Ensure this scene is detailed and long, kissing all over her upper body
                image v10lautk = Movie(play="images/v10/Scene 24/v10lautk.webm", loop=True, image="images/v10/Scene 24/v10lautkStart.webp", start_image="images/v10/Scene 24/v10lautkStart.webp") # TPP MC tenderly kissing Lauren on upper chest, holding her breast and playing with her nipple
                image v10lautkf = Movie(play="images/v10/Scene 24/v10lautkf.webm", loop=True, image="images/v10/Scene 24/v10lautkStart.webp", start_image="images/v10/Scene 24/v10lautkStart.webp")

                scene v10lautk # MC starts kissing Lauren's upper chest while teasing her breast
                with dissolve
                pause

                scene v10lautkf
                with dissolve
                pause

                if lauren.relationship >= Relationship.GIRLFRIEND or (lauren.relationship >= Relationship.KISS and kct == "loyal"):
                    if lauren.relationship < Relationship.GIRLFRIEND:
                        $ lauren.relationship = Relationship.GIRLFRIEND
                        call screen reputation_popup
                        
                    image v10lauts = Movie(play="images/v10/Scene 24/v10lauts.webm", loop=True, image="images/v10/Scene 24/v10lautsStart.webp", start_image="images/v10/Scene 24/v10lautsStart.webp") # TPP MC's arms around Lauren's waist while he sucks on her nipple, Lauren eyes rolled back in pleasure
                    image v10lautsf = Movie(play="images/v10/Scene 24/v10lautsf.webm", loop=True, image="images/v10/Scene 24/v10lautsStart.webp", start_image="images/v10/Scene 24/v10lautsStart.webp")

                    scene v10lauts # MC sucks on Lauren's nipple, arms around her waist, while her eyes roll with pleasure
                    with dissolve
                    pause

                    scene v10lautsf
                    with dissolve
                    pause

                    scene v10lar7d # TPP Same angle as v10lar7d, Lauren topless, MC and Lauren kissing with eyes closed
                    with dissolve

                    pause 0.75

                    scene v10lar7e # TPP Same angle as v10lar7, MC smiling, Lauren looks shy but happy, mouth open
                    with dissolve

                    la "That was... fun."

                    scene v10lar8 # FPP Show Lauren, up close, topless, smiling with mouth closed
                    with dissolve

                    u "*Smiles* Yeah."

                    scene v10lar9 # FPP Show Lauren standing up and beginning to put her bra and shirt back on, Lauren smiling
                    with dissolve

                    pause 0.75

                    # Back sitting on the bed
                    scene v10lar3b
                    with fade

                    la "I always enjoy spending time with you. With you I'm just... comfortable."

                    scene v10lar3c
                    with dissolve

                    u "I feel the same way."

                    scene v10lar3b
                    with dissolve

                    la "It'd be nice if-"

                else: # If Suck her tits with anything else
                    scene v10lar8a # FPP Same angle as v10lar8, Lauren looking uncomfortable, mouth open
                    with dissolve

                    stop music fadeout 3

                    play music "music/v10/Track Scene 24_3.mp3" fadein 2
                    
                    la "[name], I... I don't think I'm ready. Sorry I just..."

                    scene v10lar9a # FPP Same angle as v10lar9, Lauren getting dressed, looking uncomfortable, mouth closed
                    with dissolve

                    u "Sorry if I, you know..."

                    # Back on bed
                    scene v10lar3
                    with dissolve

                    la "It's fine, I'd just rather move... slower."

                    scene v10lar3a
                    with dissolve

                    u "I understand."

                    scene v10lar3
                    with dissolve

                    la "All of my friends were a bit more... experienced before coming to SVC. Kinda wish I would've been too."

                    scene v10lar3c
                    with dissolve

                    u "We'll go as fast as you're comfortable with. Don't worry about me."

                    scene v10lar3b
                    with dissolve

                    la "Thanks for understanding. Maybe we could uhm-"

            "Kiss her":
                # Lauren and MC contine making out
                scene v10lar7d
                with dissolve

                pause 0.75

                # -Lauren eventually pulls back and appears slightly shy but happy-
                scene v10lar7e
                with dissolve

                la "That was... fun."

                scene v10lar8
                with dissolve

                u "*Smiles* Yeah."

                # Lauren gets up and gets her bra and shirt back on
                scene v10lar9
                with dissolve

                pause 0.75
                label v10s24_nsfwSkipLabel1:
                    # Back sitting on the bed
                    scene v10lar3b
                    with fade

                    la "I always enjoy spending time with you. With you I'm just... comfortable."

                    scene v10lar3c
                    with dissolve

                    u "I feel the same way."

                    scene v10lar3b
                    with dissolve

                    la "It'd be nice if-"

    else: # Just friends with Lauren
        scene v10lar3f
        with dissolve

        la "You think I'd be good, haha. You probably just wanna see me in a bikini."

        scene v10lar3c
        with dissolve

        u "That wouldn't be the worst thing in the world, haha."

        scene v10lar3
        with dissolve

        la "Honestly, that'd be one of the things I'd be most nervous about. Not necessarily the wrestling."
        la "I actually think I'd do good, but I'm sort of nervous about everyone watching me."

        scene v10lar3c
        with dissolve

        u "Hey, I could always host the mud wrestling privately in my room. To make you feel more... comfortable. *Laughs*"

        scene v10lar3f
        with dissolve

        la "Haha, yeah I'll think about it."

        if v10s33_laurenBakeSale: # If Lauren is doing bake sale
            scene v10lar3b
            with dissolve

            la "Oh, something funny actually happened the other day."
            la "I was at the banner place letting them know what I needed my bake sale sign to say."
            
            la "I told them 'Lauren's Choice Muffins'; tell me why I go to pick up the banner and it says 'Lauren's Moist Muffins'?"

            scene v10lar3c
            with dissolve

            u "That's actually pretty funny, were you able to get a new sign made in time?"

            scene v10lar3b
            with dissolve

            la "I could have, but some of the other Deers were with me and they loved the play on words."
            la "Though somewhat embarrassing, I just went with it."

            scene v10lar3c
            with dissolve

            u "Hey, maybe it'll draw more customers. Imre probably wouldn't go to a bake sale."
            u "But I'm sure he'd be in line for some \"moist muffins.\" *Laughs*"

            scene v10lar3f
            with dissolve

            la "I may just have to spice the name up a bit then. *Laughs*"

            scene v10lar3c
            with dissolve

            u "So what are some of the other girls doing?"

        else: # Lauren not doing bake sale
            scene v10lar3c
            with dissolve

            u "So you're doing the living statue, What are some of the other girls doing?"

        scene v10lar3b
        with dissolve

        la "I know someone's doing a thrift sale, there's \"win a date\" and someone's even doing body painting."

        scene v10lar3c
        with dissolve

        u "Body painting?"

        scene v10lar3g
        with dissolve

        la "Yeah, body painting. I'm starting to think you have other interests in attending the event than just supporting me. *Chuckles*"

        scene v10lar3c
        with dissolve

        u "Why not kill two birds with one stone? *Chuckles*"

        scene v10lar3b
        with dissolve

        la "Guess that's how boys are. Would you be willing to-"

    # Regardless of friends dating or made out scene continued
    scene v10lar3a
    with dissolve

    u "Uhm, hold on."

    if joinwolves:
        scene v10lar11 # FPP Show Ms. Rose on phone, worried expression, mouth closed, plain black background
        with dissolve

        u "Hello?"

        scene v10lar10 # TPP Show MC sitting on Lauren's bed, holding phone to his ear, neutral expression, mouth closed
        with dissolve

        ro "Hey [name], it's Ms. Rose, I'm sorry for calling out of the blue."
        ro "But I don't really know who else to turn to. My husband is outside parked in his car and just won't leave."
        
        ro "I'm starting to feel a little unsafe."

        scene v10lar11
        with dissolve

        u "That sounds super creepy. I'll come by and make sure you're okay."

        scene v10lar10a # TPP Same as v10lar10, MC expression is concerned
        with dissolve

        ro "That's not-"

        scene v10lar11
        with dissolve

        u "It doesn't bother me, I'm on my way."

        scene v10lar10a
        with dissolve

        ro "Thank you."
    
    else: # If not Wolves, then Apes
        scene v10lar12 # FPP Show Samantha on phone, worried expression, mouth closed, plain black background
        with dissolve

        u "Hello?"

        scene v10lar10a
        with dissolve
        
        sa "Hey, can you come home? It's pretty important, but I can't go into detail. I just need you to come home now!"

        scene v10lar12
        with dissolve

        u "Oh shit, of course. I'm on my way right now."

    scene v10lar3h # FPP Same angle as v10lar3, Lauren looking concerned, mouth open
    with dissolve

    la "Everything okay?"

    scene v10lar3i # FPP Same as v10lar3h, Lauren mouth closed
    with dissolve

    u "Yeah, I gotta go though. Just something I need to take care of."

    scene v10lar3h
    with dissolve

    la "Oh okay, I guess I'll see you at the event."

    scene v10lar3i
    with dissolve

    u "Of course."

    if lauren.relationship >= Relationship.GIRLFRIEND: # lauren and mc kiss goodbye at her door
        scene v10lar1a
        with fade

        play sound "sounds/kiss.mp3"
        
        pause 1

    $ renpy.end_replay()
    if joinwolves:
        jump v10_ms_rose_fight
    else:
        jump v10_sam_kitchen