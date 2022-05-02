# Copyright 2022 CrimsonSky Ltd, All Rights Reserved 
#
#
#
#
#
#
#
#
#

# This scene proces the first run pass of the girls and their questions
# Each girl is called sequentially in the following order
#
# Emily
# Aubrey
# Lauren   
# Autumn
# Riley
# Nora
# Ms Rose
# Chloe
# Penelope 
# Amber
# Samantha
# Lindsey
# Jenny
#
# Jenny sets the recap_first_run variable to false and then calls the recap_girl_overview screen
# where the player can then see a summary of the girls and click on them to change their answers to the questions.
#

label recap_02: 

label recap_emily_questions:

    hide screen phone_icon

    scene black
    with None

    call screen recap_girl_summary("emily")

    if _return == "Forgive her":
        # Set variables here 

        scene recap02_01 # v5 s411a
        with dissolve

        u "After forgiving her, she was really clingy and just wouldn't leave me alone."

        scene recap02_01a # v8s20 v8arcade7 
        with dissolve

        u "I needed to have a serious think about how far I wanted to take things with her."

        scene recap02_01b # v8s20 v8arcade12a
        with dissolve

        menu:

            "Stay friends":
                # Set variables for this decision here 
                # Emily Friend here 

                hide screen phone_icon

                scene recap02_01c # v8s20 v8arcade4h
                with dissolve

                u "I decided it would be best to just keep her firmly in the friend zone. Much less drama that way!"

                if not recap_first_run:
                    jump recap_girl_overview
                    
                else:
                    jump recap_aubrey_questions

            "Start having sex again":
                # Set variables for this decision here
                # Emily RS here
                $ emily.relationship = Relationship.FWB                

                hide screen phone_icon

                scene recap02_01d   # v6 em10a
                with dissolve

                u "I guess I still had feelings for her, and the sex was always great, so why not?"
                
                if not is_CK2:

                    if not recap_first_run:
                        jump recap_girl_overview                        
                    
                    else:
                        jump recap_aubrey_questions
                
                scene recap02_01e  # v6 s538s
                with dissolve

                u "Things with Emily were very on and off. She was jealous of the attention I was getting from other girls and she wanted to stop seeing me."

                scene recap02_01f  # v13s50_19d
                with dissolve

                u "Then when we were in Europe, all that built-up tension boiled over into potentially having some angry sex."                

                scene recap02_01g  # v13s51_9 
                with dissolve

                menu:
                    "Have sex":
                        # Set variables for this decision here
                        # EmilyRS here
                        $ viewed_scenes.add("v13_emily") 

                        hide screen phone_icon

                        scene recap02_01h  # v13s50a_4
                        with dissolve

                        pause 1.25

                        scene recap02_01i  # v13s50a_5
                        with dissolve

                        pause 1.25

                        scene recap02_01j  # v13s50av4Start
                        with dissolve

                        pause 1.25

                        scene recap02_01k  # v13s50av2Start
                        with dissolve

                        pause 1.25

                        scene recap02_01l  # v13s50av4bStart
                        with dissolve

                        pause 1.25

                        scene recap02_01m  # v13s50a_9
                        with dissolve

                        u "Well, it happened. I gave her what she wanted but I don't regret it. That was some hot angry sex!"

                    "Don't have sex":
                        # Set variables for this decision here
                        # Emily Friend here 

                        hide screen phone_icon

                        scene recap02_01n   # v13s51_11a
                        with dissolve

                        pause 1.25

                        scene recap02_01o   # v13s51_12b
                        with dissolve

                        pause 1.25

                        scene recap02_01p   # v13s51_12c
                        with dissolve

                        pause 1.25

                        scene recap02_01q   # v13s51_12d
                        with dissolve

                        pause 1.25

                        scene recap02_01r   # v13s51_13a
                        with dissolve                        

                if not recap_first_run:
                    jump recap_girl_overview
                    
    else: # Don't forgive her
        # Set variables here
        # Emily friend here
        hide screen phone_icon    

    if not recap_first_run:
        jump recap_girl_overview

label recap_aubrey_questions:
    
    hide screen phone_icon

    scene black
    with None
    
    call screen recap_girl_summary("aubrey")

    if _return == "Be friends":
        # set variables here
        # Aubrey friend here
        
        scene recap02_09    # v6 s571a
        with dissolve

        u "I wasn't so sure the friends-with-benefits thing was right for me and Aubrey."

        scene recap02_09a    # v6 sufr3au2a
        with dissolve
        
        u "I honestly preferred being friends without the benefits, at least for now."

        if not recap_first_run:
            jump recap_girl_overview
        else:
            jump recap_lauren_questions

    else: # Have Sex
        # set variables here
        $ viewed_scenes.add("v11_aubrey")
        $ aubrey.relationship = Relationship.FWB

        scene recap02_09b    # v3 anew8
        with dissolve        
        
        u "That's the point of college, isn't it?"
        
        scene recap02_09c    # v6 naub16a
        with dissolve

        pause 1.25

        scene recap02_09d    # naub11start
        with dissolve

        pause 1.25

        scene recap02_09e    # v11aub8a
        with dissolve

        pause 1.25

        scene recap02_09f    #  v11aubllTPP2Start
        with dissolve

        pause 1.25

        scene recap02_09g    # v11auanTPP1Start
        with dissolve
        
        u "Having sex with hot chicks? And Aubrey was definitely hot."
    
        scene recap02_09y
        with dissolve

        pause 1.25
        
        scene recap02_09x
        with dissolve
        
        pause 1.25
        
        scene recap02_09w
        with dissolve
    
        u "Aubrey never thought of herself as the relationship type."
    
        u "I thought I saw a romantic side in her but I didn't know if it would end well if I tried to push her in that direction."
    
        menu:
            "Try being romantic":
                $ v0s48_canoeing_as_date = True

                hide screen phone_icon

                scene recap02_09u
                with dissolve
                
                u "She didn't take it seriously at first."

                scene recap02_09z
                with dissolve
                
                u "Though as we became closer, she began to come around to the idea."

                scene recap02_09t
                with dissolve

                u "But this is still new territory for us to explore."

            "Stay FWB":
                hide screen phone_icon

                scene recap02_09v
                with dissolve
                
                u "In the end, I didn't go for it. Our relationship wasn't very deep, but I liked what I had."

    
    if not recap_first_run:
        jump recap_girl_overview

label recap_lauren_questions:
    
    hide screen phone_icon
    
    scene black
    with None
    
    call screen recap_girl_summary("lauren")

    if _return == "Be friends":
        # set variables here
        # lauren friends
        pass

    else: #  Pursue a relationship
        $ lauren.relationship = Relationship.GIRLFRIEND

        scene recap02_04  # s87c
        with dissolve
        
        u "The next day, I met up with her..."

        scene recap02_04a   # s88
        with dissolve

        u "and we got to talking about the dating game."

        scene recap02_04b    # s89j
        with dissolve

        u "That's when she kinda revealed she was still a virgin."

        scene recap02_04c    # v3 s286
        with dissolve

        u "We later went on a date to see a movie."

        scene recap02_04d    # laurenkiss2
        with dissolve

        u "We kissed and things seemed to be going really well."

        scene recap03_04e   #  v3 s291a
        with dissolve

        menu:

            "Push for more":
                # set variables here
                # laruen friend here
                $ v0_lauren_too_far = True
                $ lauren.relationship = Relationship.FRIEND

                scene recap02_04f  # v3 s291b
                with dissolve

                pause 1.25

                scene recap02_04g  # v3 s291c
                with dissolve

                pause 1.258

                scene  recap02_4h  # v3 s289f
                with dissolve

                u "And that's when she broke things off with me right there and then for going too far."

                scene recap02_04i  # v3 s289g
                with dissolve

                u "Maybe I'll have another chance in the future, but we'd have to stay friends for a while."

                if not is_CK2:
                    if not recap_first_run:
                        jump recap_girl_overview
                    else:
                        jump recap_autumn_questions

            "Don't push it":
                # set variables here 
                # laruen gf here 

                scene recap02_04j # v3 s289
                with dissolve

                u "I didn't want to push things too far too soon. We continued watching the movie and had a really nice time together."

                scene recap02_04c
                with dissolve

                u "I knew she was the right girl for me."
        
        if aubrey.relationship == Relationship.FWB:
            scene recap02_04k  # v11aub25
            with dissolve

            u "We were on the airplane to London for the start of our European vacation..."

            scene recap02_04l  # v11aub2 
            with dissolve

            pause 1.25

            scene recap02_04m  # v11aub4
            with dissolve

            u "and Aubrey wanted me to join her in the bathroom..."
            
            scene recap02_04n  # v11aub8a
            with dissolve

            u "for some mile-high action."

            menu:
                "Sex with Aubrey":
                    # Set variables here                   
                    $ viewed_scenes.add("v11_aubrey")
                    $ v0_lauren_caught_aubrey = True
                    $ lauren.relationship = Relationship.FRIEND

                    scene recap02_04o  # v11aub9
                    with dissolve

                    pause 1.25

                    scene recap02_04p  # v11aub10
                    with dissolve

                    pause 1.25

                    scene recap02_04q  # v11aublltpp2start
                    with dissolve

                    pause 1.25

                    scene recap02_04r   # v11aub17c
                    with dissolve
                    
                    pause 1.25

                    scene recap02_04s   # v11aub17a
                    with dissolve

                    u "And of course Lauren walked in on us! So that was the end of that relationship!"

                    if not recap_first_run:
                        jump recap_girl_overview
                    else:
                        jump recap_autumn_questions
                
                "Don't have sex":
                    $ v0s13_rejected_aubrey = True

                    scene recap02_04t  # v11noch1
                    with dissolve

                    u "I didn't take her up on her offer. I'm not going to cheat on Lauren just like that!"
        
        scene recap02_04u  # v12las15
        with dissolve

        u "A little later into the vacation..."

        scene recap02_04v  # v12las20
        with dissolve

        pause 1.25

        scene recap02_04w  # v12las21
        with dissolve        
        
        u "I had a really nice date with Lauren..."
        
        scene recap02_04x  # v12las53
        with dissolve

        u "and she seemed ready to have sex for the first time."

        menu:

            "Extra effort":
                # set variables here
                # lauren GF here
                $ viewed_scenes.add("v12_lauren")

                scene recap02_04y  # v12las53a
                with dissolve

                u  "I put on some extra charm..."

                scene recap02_04z  # v12las53b
                with dissolve

                u  "and was proved right."
                
                scene recap02_05  #  v12Laucgstart
                with dissolve

                u "It was slow and sensual..." 
                
                scene recap02_05a  # v12las65
                with dissolve

                u "and it felt great to be the one she chose for her first time."

            "Take it easy":
                # set variables here
                # laren GF here

                scene recap02_05b  # v12las73
                with dissolve

                u "Maybe I played it wrong, but we ended up not having sex that night."

                scene recap02_05c  # v12las34
                with dissolve

                u "When it does eventually happen, I'll make sure it's amazing."        

        if not recap_first_run:
            jump recap_girl_overview

label recap_autumn_questions:

    hide screen phone_icon

    scene black
    with None

    call screen recap_girl_summary("autumn")

    if _return == "Spend time with her":
        # Set variables here
        # AutumnFriend
        $ v0_visited_shelter = True
        $ v0_signs = True
        $ v0_protest = True
        
        scene recap02_02  # v7 s722 
        with dissolve

        pause 1.25

        scene recap02_02a  # v7 s725
        with dissolve

        u "It wasn't going to hurt anything by hanging out with her..."
        
        scene recap02_02b # v7 sas12a 
        with dissolve
        
        u "and it was actually quite fun getting to know her better and learning that she's into things like political activism."

    else: # Dont spend time with Autumn
        scene recap02_02c  # v4 s334
        with dissolve

        u "Who's got time to waste on girls that require this much effort? I'll move on quickly, thanks!"
    
    scene black
    with None

    if not recap_first_run:
        jump recap_girl_overview

label recap_riley_questions:
    
    hide screen phone_icon

    scene black
    with None

    call screen recap_girl_summary("riley")

    if _return == "Be friends":
        # set variables where
        # riley friend here 

        if not recap_first_run:
            jump recap_girl_overview

    else: # Pursue a relationship

        scene recap02_06    # v7 s710
        with dissolve
        
        u  "We started hooking up..." 
        
        scene recap02_06b    # v7 rivid8052
        with dissolve

        u "and the sex was great..." 
        
        scene recap02_06c    # v8sopt25
        with dissolve        

        u "then later I found out that she's actually bisexual..."
        
        scene recap02_06d    # v8sopt27b
        with dissolve

        pause 1.25

        scene recap02_06e    # v11sub4
        with dissolve
         
        u "She seemed to be hinting that she'd like some sexual experiences with other girls." 
        
        scene recap02_06f    # v11ras3
        with dissolve

        u "I guess, as a guy, you're either into that or you're not."

        menu:
            "Let be friends":
                # set variables here 
                $ riley.relationship = Relationship.FRIEND

                scene recap02_06g    # v11ras6
                with dissolve

                u "I'm just not into that, so it's probably for the best we stay friends."

                if not recap_first_run:
                    jump recap_girl_overview
                else:
                    jump recap_nora_questions

            "Contnue relationship":
                # set variables here
                $ riley.relationship = Relationship.FWB 

                scene recap02_06f
                #with dissolve

                u "Maybe I could angle for a threesome at some point! That would be incredible!"

                if not is_CK2 or (is_CK2 and recap_choose_threesome):
                    if not recap_first_run:
                        jump recap_girl_overview
                    else:
                        jump recap_nora_questions                                
    
        if aubrey.relationship == Relationship.FWB:
            # Three some question
            
            scene recap02_06h    # v13s33_8
            with dissolve

            u "Fast forward to right near the end of our Europe trip, while we were in Amsterdam..."

            scene recap02_06i   # v13s62_2g
            with dissolve

            pause 1.25        

            scene recap02_06j    # v13s62_2i
            with dissolve

            u "the threesome thing became a real option!"

            scene recap02_06k    # v13s62_3a
            with dissolve
            
            menu:
                "Have threesome":
                    # set variables here
                    # riley rs here
                    $ recap_choose_threesome = True
                    $ viewed_scenes.add("v14_threesome")
                    $ v0_threesomeending = True 

                    scene recap02_06l    # v14auridoStart
                    with dissolve

                    pause 1.25

                    scene recap02_06m    # v14aurircgStart
                    with dissolve

                    pause 1.25

                    scene recap02_06n    # v14s01_8
                    with dissolve

                    u "Wow! I won't be forgetting that in a hurry!"

                "Don't have threesome":
                    # set variables here

                    scene recap02_06o    # v13s62_1
                    with dissolve

                    u "I just wasn't sure that was the right move for me with either of the girls."    

    if not recap_first_run:
        jump recap_girl_overview

label recap_nora_questions:
    
    hide screen phone_icon

    scene black
    with None

    call screen recap_girl_summary("nora")

    if _return == "Don't flirt with her":
        # set variables here        
        
        scene recap02_07    # v1  s55ch3
        with dissolve

        u "Yeah, actually, even if I am interested, there's no way I'm putting moves on a girl who already has a boyfriend."
        
        scene recap02_07a    # v6 s520h
        with dissolve

        u "Best to stay friends without all the flirting. Plus she might tell Chris!"

    else: # Flirt with her
        # set variables here

        scene recap02_07b    # v7 s702a
        with dissolve
        
        u "It's just a harmless bit of flirting..."
        
        scene recap02_07c    # v7 s702f
        with dissolve
        
        u "and every girl appreciates it when a guy lets them know in the most subtle of ways that they're hot."

    # second question

    scene recap02_07d    #  v8 v8shal2
    with dissolve

    u "I also had the chance to help her out with signing people up for the big summer trip to Europe."

    scene recap02_07e    # v8 v8shal4
    with dissolve

    menu:

        "Help Nora":
            # set variables here
            # Nora friend here
            $ v0_help_nora_freeroam = True
            $ v0_chase_robber = True
            $ v0_fight_win = True
            $ v0_followed_nora = True 

            scene recap02_07f    # v8 v8shal8
            with dissolve

            u "It'd be interesting to take part, but more than that, it would get Nora to like me more!"


        "Don't help Nora":
            # set variables here
            # Nora friend here 

            scene recap02_07g    #  v8 v8shal3e
            with dissolve
            
            u "In all honesty, I wasn't that bothered when it came down to it."
            
            scene recap02_07h    #  v8 v8shal6
            with dissolve
            
            u  "I'll just let nature take its course. What will be will be!"

    if not is_CK2:
        if not recap_first_run:
            jump recap_girl_overview
        else:
            jump recap_ms_rose_questions
    
    # question 3

    scene recap02_07i    # v14s10_1
    with dissolve

    pause 1.25

    scene recap02_07j    # v12ncf4e
    with dissolve

    u "Once we were in Europe, things between Nora and Chris were getting worse." 
    
    scene recap02_07k    # v11bb3
    with dissolve

    pause 1.25

    scene recap02_07l    # v11bb7a
    with dissolve

    u "I had some alone time sightseeing with her..."

    scene recap02_07m    # v11bb5
    with dissolve

    pause 1.25
    
    scene recap02_07n    # v11bb9b
    with dissolve

    pause 1.25

    scene recap02_07o    # v11bb9c
    with dissolve
    
    u "and there was the opportunity to move in for a kiss if I was interested in her, even though there was a huge risk involved and it might backfire."

    menu:

        "Kiss Nora":
            # set variables here
            # Nora friend here 
            $ v0s16_kissnora = True
            $ v0_imre_disloyal = True
            $ v0_freeroam11.add("nora") 

            scene recap02_07p    # v11bb9d
            with dissolve

            u "Well that messed everything up!"
            
            scene recap02_07q    # v11bb11a
            with dissolve

            u "She was angry with me for pulling a move like that and it's going to take a while to win back those trust points."

            if not recap_first_run:
                jump recap_girl_overview
            else:
                jump recap_ms_rose_questions

        "Don't kiss Nora":
            # set variables here
            $ v0s16_kissnora = False
            $ v0_imre_disloyal = False

            scene recap02_07r # v11bb9a
            with dissolve

            u "That was the right thing to do. No need to spoil a good thing!"

    # Question 4 

    scene recap02_07s    # v12nos1a
    with dissolve

    u "The decision not to kiss her meant I could get even closer to her. Later, we were talking in her hotel room."

    scene recap02_07t    # v12nos7
    with dissolve

    menu:
        "Stay friends":
            # set variables here
            # Nora friend here

            scene recap02_07u    # v12nos8
            with dissolve

            u "We talked about the problems she was going through with Chris..."
            
            scene recap02_07v    # v12nos4
            with dissolve
            
            u "and she seemed to really appreciate being able to talk it all through with me."

            scene recap02_07w    # v12nos10
            with dissolve

            pause 1.25            

        "Kiss her":
            # set variables here
            # Nora rs here
            $ nora.relationship = Relationship.FWB

            scene recap02_07x    # v12nos2
            with dissolve

            pause 1.25
            
            scene recap02_07y    # v12nos5
            with dissolve

            u "She really seemed to enjoy the way I was focusing on her and showing her attention."

            scene recap02_07z    # # v12nos15a
            with dissolve

            u "I went in for the kiss and it didn't stop there."

            scene recap02_08    # v12nos18
            with dissolve

            pause 1.25

            scene recap02_08a    # v12nos19
            with dissolve

            pause 1.25

            scene recap02_08b    # v12norst2Start
            with dissolve

            pause 1.25

            scene recap02_08c    # v12norsbStart
            with dissolve

            pause 1.25

            scene recap02_08d    # v12nos27
            with dissolve
            
            u "We ended up having some incredible sex! Sorry, Chris!"


    if not recap_first_run:
        jump recap_girl_overview

label recap_ms_rose_questions:
    
    hide screen phone_icon

    scene black
    with None

    call screen recap_girl_summary("ms_rose")

    # MsRose can have three return values 
    #
    # "continue"
    # "Pursue a relationship"
    # "Be friends"

    if _return == "continue": # MC is on the ape Path
        # set variables here
        # ms rose friend here 
        if not recap_first_run:
            jump recap_girl_overview
        else:
            jump recap_chloe_questions

    elif _return == "Be friends":
        # set variables here
        # msrose friend here
        
        scene recap02_03  # v1 s84
        with dissolve

        u "She's my teacher, so no way is anything happening there. It would only lead to trouble anyway!"


    else: # Pursue a relationship
        # Set varibles here
        scene recap02_03a  # v7 shr5e
        with dissolve

        u "Who doesn't want to bang the hottest teacher at SVC? You just have to believe it's possible."

        scene recap02_03b  # v10msf5 
        with dissolve

        u "I had the chance to kiss her, but it was a big play with a lot of risk."

        scene recap02_03c  # v10msf5b 
        with dissolve

        menu:
            "Kiss her":
                # Set variables here
                # msroseRS here

                if not is_CK2:
                    if not recap_first_run:
                        jump recap_girl_overview
                    else:
                        jump recap_chloe_questions

                scene recap02_03d  # v10msf6 
                with dissolve

                pause 1.25

                scene recap02_03e # v11src1a 

                u "On our Europe trip, the chance came up again."
                
                scene recap02_03f  # v11ros2g  
                with dissolve

                u "She wanted to speak alone with me, and I could feel the sexual tension."

                scene recap02_03g # v11roc2 
                with dissolve

                menu:
                    
                    "Kiss her again":
                        # set variables here
                        $ ms_rose.relationship = Relationship.FWB
                        $ viewed_scenes.add("v12_rose")

                        scene recap02_03h # v11roc6  Ms Rose and MC kissing in hallway with tongue
                        with dissolve

                        u "I wasn't wrong about the sexual tension..."

                        scene recap02_03i # v11ros6a
                        with dissolve

                        u "and that kiss sealed the deal for a couple of amazing sex sessions!"

                        scene recap02_03j # v11ros9 
                        with dissolve

                        pause 1.25

                        scene recap02_03k # v12rossdStart 
                        with dissolve

                        pause 1.25

                        scene recap02_03l #  v11roc8 
                        with dissolve

                        u "What happens in Europe stays in Europe!"

                    "Don't kiss her":
                        # set variables here 
                        # msrose friend here 

                        scene recap02_03m # v11arrh3c 
                        with dissolve

                        u "Okay, maybe I didn't feel so confident about that sexual tension after all."

            "Don't kiss her":
                # Set variables here
                # ms rose friend here

                scene recap02_03d  # v11s43 v11bank28a 
                with dissolve

                u "Yeah, on second thoughts, I figured it would be best to stay out of that one."
    
    if not recap_first_run:
        jump recap_girl_overview

label recap_chloe_questions:
    
    hide screen phone_icon

    scene black
    with dissolve

    call screen recap_girl_summary("chloe")

    if _return == "Be friends":
        # set variables here
        # chloe friend here 

        scene recap02_10    # v1 s114b
        with dissolve

        u " It was more of a friend vibe for me really..."
        
        scene recap02_10a    # v7 sfr4cl18
        with dissolve
        
        u "and to be honest, I found at least one other girl more interesting and worthy of my time."

        
        if not recap_first_run:
            jump recap_girl_overview
        else:
            jump recap_penelope_questions
    
    
    else: # Pursue a relationship
        # set variables here
        $ v0_hc_girl = "chloe"
        $ chloe.relationship = Relationship.FWB        
        
        scene recap02_10b    # v3 s204
        with dissolve

        pause 1.25

        scene recap02_10c    # v6 sfr3cl1a
        with dissolve
        
        pause 1.25

        scene recap02_10d    # v4 s370d
        with dissolve
        
        u "I was expecting this to be hard work..."
        
        scene recap02_10e    # v7 sfr4cl8
        with dissolve

        pause 1.25

        scene recap02_10f    # v7 sfr4cl30
        with dissolve

        pause 1.25

        scene recap02_10g    # v8 v8s13
        with dissolve

        pause 1.25

        scene recap02_10h    # v11chcgStart
        with dissolve
        
        u "but I figured the rewards would be more than worth it!"

    # second question

    scene recap02_10i    # v11clhall1c
    with dissolve

    pause 1.25

    scene recap02_10j    # v11chb7
    with dissolve

    u "I didn't realize I'd be appeasing her ego so much though with all the in-fighting at her sorority." 

    scene recap02_10k    # v10such3b
    with dissolve

    pause 1.25
    
    scene recap02_10l    # v11car9a
    with dissolve

    pause 1.25

    scene recap02_10m    # v11car18a
    with dissolve

    u "Chloe was the president of the Chicks, and it seems other girls in the sorority didn't want her to be."

    menu:
        "Take Chloe's side":
            # set variables here
            # chloe rs here
            $ v0_help_chloe_pier = True

            scene recap02_10n    # v10such4c
            with dissolve

            u "It was best not to get involved too much."

            scene recap02_10o    # v10chg10a
            with dissolve 
            
            u "I've decided Chloe is the one for me, so I'm not going to let any sorority drama get in the way of that."

            if not is_CK2:
                if not recap_first_run:
                    jump recap_girl_overview
                else:
                    jump recap_penelope_questions

        "Try to reason":
            # set variables here
            $ v0_cheer_for_nora = True
            $ v0_help_chloe_pier = False

            scene recap02_10p    # v6 s472
            with dissolve

            u "Well, I tried to get her to see the other side of things, but that only made her angry."

            # KCT Check 
            if reputation() == Reputations.POPULAR:
                # set variables here
                # chloe rs here 

                scene recap02_10q    # v6 sfr3cl4a
                with dissolve
                
                u "Luckily, she came around and didn't stay angry for long." 

                scene recap02_10r    # v8steak20
                with dissolve
                
                u "We're all good now, and I've learnt to be more careful in future..." 

                scene recap02_10s    # v12ncf9
                with dissolve
                
                u "because Chloe really does have a bad temper when she's pissed!"                                

            else: # not popular       
                # Set variables here
                $ chloe.relationship = Relationship.FRIEND 

                scene recap02_10t    # v10such4d
                with dissolve

                u "I'm not sure if I'm ever going to recover from that." 
                
                scene recap02_10u    # s204a
                with dissolve

                u "She seemed to be considering my reputation all the time, whether I'm popular enough..." 
                
                scene recap02_10v    # v1 s112g
                with dissolve
                
                u "And I think I've been relegated to the friend zone."

                if not recap_first_run:
                    jump recap_girl_overview
                else:
                    jump recap_penelope_questions

    # third question

    scene recap02_10w    # v11cd20
    with dissolve
    
    u "In Europe, I had the chance to take things a step further."

    scene recap02_10x    # v11cd31
    with dissolve

    menu:
        "Ask to be girlfriend":
            # set variables here
            # Chloe gf here
            $ chloe.relationship = Relationship.GIRLFRIEND

            scene recap02_10y    # v11cd31c
            with dissolve

            u "Timing is everything and I managed to play things just right." 

            scene recap02_10z    # v11cd31b
            with dissolve

            pause 1.25

            scene recap02_11    # v11cd35
            with dissolve

            pause 1.25

            scene recap02_11a    # v11cd32
            with dissolve

            pause 1.25

            scene recap02_11b    # v11cd45
            with dissolve
            
            u "I was now going out with the hottest girl on campus!"

        "Don't ask":
            # set variables here
 
            scene recap02_11c    # v11cd30
            with dissolve

            u "It suited me much better to keep things the way they were." 

            scene recap02_11d    # v11cd46
            with dissolve
            
            u "I didn't want to get tied into a proper full-on relationship with Chloe and that temper of hers!"

    if not recap_first_run:
        jump recap_girl_overview

label recap_penelope_questions:
    
    hide screen phone_icon

    scene black
    with None

    call screen recap_girl_summary("penelope")

    if _return == "Be friends":
        # set variables here

        if not recap_first_run:
            jump recap_girl_overview
        else:
            jump recap_amber_questions

    # Pursue a relationship    

    # second question

    scene recap02_12   # v4  s342
    with dissolve

    u "Later, I needed a caffeine fix so went to the local café." 

    scene recap02_12a   # v4 s345
    with dissolve

    pause 1.25

    scene recap02_12b   # v4 s345a
    with dissolve

    pause 1.25

    scene recap02_12c   # v4 s345f
    with dissolve
    
    u "I bumped into her there and we started chatting." 

    scene recap02_12d   # v4 s350
    with dissolve
    
    u "She's got such a beautiful smile."

    menu:

        "Kiss her":
            # set variables here
            # Penelope friend here

            scene recap02_12e   # s348b
            with dissolve
            
            u "I pushed things too far too soon, and she left the café." 
            
            scene recap02_12f   # s351
            with dissolve
            
            u "Dammit! She seems like the forgiving type, but it looks like I'm friend zoned for now."

            if not is_CK2:
                if not recap_first_run:
                    jump recap_girl_overview
                else:
                    jump recap_amber_questions

        "Ask her out":
            # set variables here
            # Penelope rs here 
            
            scene recap02_12g   # s349b
            with dissolve

            pause 1.25

            scene recap02_12h   # s634a
            with dissolve

            u "We went bowling for our first date."

            scene recap02_12i   # s642
            with dissolve
            
            pause 1.25

            scene recap02_12j   # s650
            with dissolve

            pause 1.25

            scene recap02_12k   # s651
            with dissolve
            
            u "Note to self: Don't go bowling with her again as she has the skills of a pro player..."

            scene recap02_12l   # s653
            with dissolve
            
            u "and I'll lose every time!"
            
            scene recap02_12m   # s658l
            with dissolve
            
            u "We ended the date with a kiss and I was flying high!"

            if not is_CK2:
                if not recap_first_run:
                    jump recap_girl_overview
                else:
                    jump recap_amber_questions

    # third question

    scene recap02_12n   # v11coc11a
    with dissolve

    pause 1.25

    scene recap02_12o   # v11coc11b
    with dissolve

    u "I helped Penelope with her school hearing after she got caught hacking the college system." 

    scene recap02_12p   # v11coc16b
    with dissolve
    
    u "I didn't really have any idea what I was doing..."

    scene recap02_12q   # v11coc16c
    with dissolve
    
    u "and I suddenly had to figure out how to behave like a professional lawyer type person."

    menu:
        "Tell the truth about Penelope":
            # set variables here
            # Penelope rs here 
            $ v0_pen_goes_europe = True
            $ v0s23_penelope_date = True
            $ penelope.relationship = Relationship.LIKES

            scene recap02_12q   
            with dissolve
            
            u "I defended Penelope's actions and told the truth.."
            
            scene recap02_12r   # v11coc18
            with dissolve
            
            u "but also used the lack of concrete facts to poke holes in their accusations against her."

            scene recap02_12s   # v11coc25a
            with dissolve

            pause 1.25

            scene recap02_12t   # v11coc25b
            with dissolve

            u "And we won!"

            scene recap02_12u   # v11coc27
            with dissolve
            
            u "I guess I'd make a pretty good lawyer type person after all!"

            scene recap02_12v   # v11amp9b
            with dissolve
            
            u "Another bonus was the Penelope could come on the Europe trip!"

        "Lie and use diversion tatics":
            # set variables here
            # Don't set here (rs depedns on answer to question 2 )

            scene recap02_12q   
            with dissolve

            pause 1.25

            scene recap02_12w   # v11coc24f
            with dissolve
            
            u "I did my best to get them to drop the charge, but they found her guilty!"
            
            scene recap02_12x   # v11coc24a
            with dissolve

            pause 1.25

            scene recap02_12y   # v11coc24b
            with dissolve

            u "Penelope had a huge fine to pay and it also meant that she wasn't allowed to come on the Europe trip, which sucked big time."

    if not recap_first_run:
        jump recap_girl_overview

label recap_amber_questions:
    
    hide screen phone_icon

    scene black
    with None

    call screen recap_girl_summary("amber")

    if _return == "Be friends":
        # set variables here
        # Amber friend here

        if not recap_first_run:
            jump recap_girl_overview
        else:
            jump recap_samantha_questions

    # KCT check 

    if reputation() == Reputations.POPULAR:
        # set variables here
        # amber RS here
        $ amber.relationship = Relationship.FWB 

        scene recap02_13   # jomon4
        with dissolve

        u "I was popular enough for Amber to be interested."

        scene recap02_13a   # jomon14c
        with dissolve

        pause 1.25

        scene recap02_13b   # jomon15a
        with dissolve

        pause 1.25

        scene recap02_13c   # jomon15b
        with dissolve

        pause 1.25
        
        scene recap02_13d   # sfr4am3a
        with dissolve

        pause 1.25

        scene recap02_13e   # v9jka2
        with dissolve
        
        u "That's how she works and I've got no problem with that."
        
        scene recap02_13f   # v8 cgt_00
        with dissolve

        pause 1.25

        scene recap02_13g   # v8 cgt_119
        with dissolve

        pause 1.25

        scene recap02_13h   # v10ambcgStart
        with dissolve

        pause 1.25

        scene recap02_13i   # v8samb13
        with dissolve
        
        u "Though it was just going to be a friends-with-benefits type deal for the foreseeable future."

    else: # not popular
        # set variables here
        # amber friend here 

        scene recap02_13j   # s919g
        with dissolve

        pause 1.25

        scene recap02_13k   # s919h
        with dissolve

        u "The only way to get with Amber was by being popular." 
        
        scene recap02_13l   # v2 sf1
        with dissolve        

        pause 1.25

        scene recap02_13m   # v2 tf
        with dissolve

        u "My reputation needed more work in order for that to happen." 
        
        scene recap02_13n   # v10rva7
        with dissolve

        pause 1.25

        scene recap02_13o   # v10rva10a
        with dissolve
        
        u "She's a fun friend to have around anyway, and maybe I'll get another chance for something more in the future."

    if not recap_first_run:
        jump recap_girl_overview

label recap_samantha_questions:
    
    hide screen phone_icon

    scene black
    with None

    call screen recap_girl_summary("samantha")

    if _return == "continue":
        # set variables here

        if not recap_first_run:
            jump recap_girl_overview
        else:
            jump recap_lindsey_questions

    elif _return == "Keep my distance":
        # set variables here

        scene recap02_14     # v8s18 v9rwsa6e
        with dissolve

        u "Yeah, I wasn't going anywhere near Cameron's sister."
        
        scene recap02_14a     # v10s25 v10skt8a
        with dissolve
        
        u "He'd tear my arms off!"  

        if not recap_first_run:
            jump recap_girl_overview
        else:
            jump recap_lindsey_questions

    # Get Closer
    # set variables here 
    
    scene recap02_14b     # v10s9 v10sraf7b
    with dissolve
    
    u "I was totally playing with fire..."
    
    scene recap02_14c     #  v11s28 v11sas20
    with dissolve
    
    u "But she was hot!"

    # third question

    scene recap02_14k     #  v11s3 v11samp2c
    with dissolve

    u "I had the chance to decide whether I wanted to invite her on the Europe trip or not."

    menu:
        "Invite Samantha to Europe":
            # set variables here
            $ v0_invite_sam_europe = True 

            scene recap02_14l     # v11s3 v11samp2f
            with dissolve

            pause 1.25

        "Don't invite":
            # set variables here

            scene recap02_14m     # v11s3  v11samp2i
            with dissolve

            pause 1.25

            if not recap_first_run:
                jump recap_girl_overview
            else:
                jump recap_lindsey_questions    

    # second question 

    scene recap02_14d     # v10s25a v10skt4b
    with dissolve

    u "We got to drinking one time and I saw first-hand how much of a lightweight she is with alcohol." 
    
    scene recap02_14e     # v10s25a v10skt8a
    with dissolve
    
    u "Cameron got really angry with me." 
    
    scene recap02_14f     # v10s25a v10skt8c
    with dissolve

    u "I think he could get a lot angrier and I had to think about whether Samantha was worth all this potential drama."

    menu: 
        "Be friends":
            # set variables here

            scene recap02_14g     # v9s22 v9rwsa6e
            with dissolve
            
            u "Probably not worth it." 
            
            scene recap02_14h     #  v9rwsa4
            with dissolve

            u "I decided to back off and just keep her and her psycho brother at a safe distance, as best I could anyway."

            if not is_CK2:
                if not recap_first_run:
                    jump recap_girl_overview
                else:
                    jump recap_lindsey_questions
        
        "Pursue a relationship":
            # set variables here
            $ samantha.relationship = Relationship.MOVE 

            scene recap02_14i     # v9s24 v9wws3
            with dissolve
            
            u "There was a connection between us and I don't care what Cameron thinks about that." 
            
            scene recap02_14j     # v11 s28a v11sas21
            with dissolve

            u "I want to see how far I can take things with her as our relationship builds."

            if not is_CK2:
                if not recap_first_run:
                    jump recap_girl_overview
                else:
                    jump recap_lindsey_questions


    # fourth question:

    scene recap02_14n     #  v13s29_18a
    with dissolve

    u "While we were in Amsterdam, there was obviously the opportunity to partake in some drug-taking."     

    scene recap02_14o     # v12s23a v12mor7
    with dissolve

    u "But Samantha's lack of self-control was in danger of becoming a problem."

    menu:
        "Invite on Weed Bus tour":
            # set variable here
            # Samantha rs/friend depends on previous setting; not set here
            $ v0_invite_samantha = True

            scene recap02_14p     # v13s29_18
            with dissolve

            pause 1.25

            scene recap02_14q     # v13s29_16
            with dissolve

            pause 1.25

            scene recap02_14r     # v13s29_21
            with dissolve

            u "We had a good time, but Cameron would surely be coming after me if he ever found out I was encouraging her drug habit."


        "Don't invite":
            # set variable here
            # Samantha rs/friend depends on previous setting; not set here

            scene recap02_14s     # v13s31_16
            with dissolve
            
            u "But then I found out she ended up in hospital after going off on her own and taking drugs with random people!" 
            
            scene recap02_14t     # v13s31_100
            with dissolve

            u "Cameron came to find me and looked like he was going to rip my head off..." 
            
            scene recap02_14u     # v13s31_14
            with dissolve
            
            u "but then he realized I had tried to help her and he really appreciated it."

    if not recap_first_run:
        jump recap_girl_overview

label recap_lindsey_questions:
    
    hide screen phone_icon

    scene black
    with None

    call screen recap_girl_summary("lindsey")

    if _return == "Don't go see her":
        # set variables here
        # lindsey friends here

        if not recap_first_run:
            jump recap_girl_overview
        else:
            jump recap_jenny_questions
    
    # Go see her

    # second question

    scene recap02_15    # v9s39 v9hwl6
    with dissolve

    u "We were having a nice chat and she was dropping signs that she was clearly interested in me."

    scene recap02_15a    #v9s39 v9hwl7a
    with dissolve

    menu:

        "Kiss her":
            # set variables here
            $ lindsey.relationship = Relationship.KISS

            scene recap02_15b    # v9s39 v9linksStart
            with dissolve
            
            u "She's hot, so of course I wanted to seal the deal before heading off to the tournament." 
            
            scene recap02_15c    # v9s39 v9hwl7
            with dissolve

            pause 1.25

            scene recap02_15d    # v9s39 v9hwl13
            with dissolve

            u "Hopefully it won't be too long before we move things beyond that kiss."

            if not is_CK2:
                if not recap_first_run:
                    jump recap_girl_overview

        "Pull away":
            # set variables here 
            # lindsey friend here 

            scene recap02_15e    # v9s39 v9hwl7b
            with dissolve
            
            u "I came to talk to her as friends, and that's how I wanted to leave it, at least for now."
            
            scene recap02_15f    # v9s39 v9hwl14
            with dissolve

            u "Plus there was a fight tournament to concentrate on, and she was proving to be a bit of a distraction."

            if not recap_first_run:
                jump recap_girl_overview
            else:
                jump recap_jenny_questions

    # third question

    scene recap02_15g    # v12s17   v12esr26
    with dissolve
    
    u "That time finally came when we went to Europe."

    scene recap02_15h    # v12s17 v12esr30
    with dissolve

    u "It was on Lindsey's birthday, and all lights were green for me to give her a special birthday treat."

    menu:
        "Take things further":
            # set variables here
            # lindsey rs here
            $ lindsey.relationship = Relationship.FWB

            scene recap02_15i    # v12esr35
            with dissolve

            pause 1.25

            scene recap02_15j    # v12esr43
            with dissolve

            pause 1.25

            scene recap02_15k    #  v12esr42
            with dissolve

            pause 1.25

            scene recap02_15l    # v12esr41c
            with dissolve

            pause 1.25

            scene recap02_15m    # v12esr40
            with dissolve

            pause 1.25

            scene recap02_15n    # v12esr47
            with dissolve
            
            u "Well, we both got a treat that day!"


        "Don't take things further":
            # set variables here
            # lindsey rs here 

            scene recap02_15o    # v12esr26b
            with dissolve

            u "She understood that it probably wasn't the best idea to do anything in such a public place."

    if not recap_first_run:
        jump recap_girl_overview

label recap_jenny_questions:
    
    hide screen phone_icon

    scene black
    with None

    call screen recap_girl_summary("jenny")

    # Jenny only returns continue so nothing to process here
    # Jenny friend

    # this is the end of the first run so turn it off
    if recap_first_run:
        $ recap_first_run = False
        

label recap_girl_overview:
    
    hide screen phone_icon

    scene black
    with None
    
    call screen recap_girl_overview_screen()
    
