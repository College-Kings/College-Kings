# SCENE 18: Call With Lauren
# Locations: MC's Room (Wolves/Apes)
# Characters: MC (Outfit 1), Lauren (Outfit 3)
# Time:
label v10_call_with_lauren2:
    play music music.ck1.v10.Track_Scene_15 fadein 2

    if mc.frat == Frat.WOLVES: # MC is a wolf, is that the correct variable name?
        scene v10scwl1 # TPP. Show Lauren as though FPP, she's sitting on the train. Lauren on phone listening to MC, smiling, mouth closed.
        with fade

        u "Excited for the charity event?"

        scene v10scwl1a # TPP. Same camera as v10scwl1. Show Lauren as though FPP, she's sitting on the train. Lauren on phone listening to MC, smiling, mouth open.
        with dissolve

        la "Excited, nervous, all of the above."

        scene v10scwl1
        with dissolve

        u "Why are you nervous?"

        scene v10scwl1a
        with dissolve

        la "I just want everything to run smoothly. My sister would be pretty upset if things didn't go as planned."

        scene v10scwl2 # TPP. Show MC in his Wolves bedroom. MC is laying on his bed, phone to ear (talking to Lauren), smiling, mouth closed.
        with dissolve
        menu:
            "Joke":
                scene v10scwl1
                with dissolve

                u "Just make things go as planned then, sounds easy enough. Nothings ever gone wrong at a college student hosted event. *Chuckles*"

                scene v10scwl2
                with dissolve

                la "Very funny..."
            
            "Be serious":
                scene v10scwl1
                with dissolve

                u "I'm sure everything will go just fine, if there's anything that needs special attention I'm sure your sister is already on top of it."

                scene v10scwl2
                with dissolve

                la "Hopefully."

        scene v10scwl2
        with dissolve

        la "It's also like... what if no one comes to my thing? And I put all this work in and just no one ever comes by."

        scene v10scwl1
        with dissolve

        u "*Laughs* So the whole event is buzzing and every stand has a long queue, but just absolutely no one comes to you? That would be pretty funny to be fair."

        scene v10scwl1a
        with dissolve

        la "Well I'm glad my failure amuses you."

        scene v10scwl1
        with dissolve

        u "Okay, IMAGINARY failure. Obviously that's not gonna happen."

        scene v10scwl2
        with dissolve

        la "I don't know, this could be middle school all over again."

        scene v10scwl1
        with dissolve

        u "What happened in middle school?"

        scene v10scwl2
        with dissolve

        la "We had this school science fair, where everyone was supposed to show off the project they had been working on for the last few months-"

        scene v10scwl1
        with dissolve

        u "Let me guess, you didn't have a project."

        scene v10scwl2a # TPP. Same camera as v10scwl2. Show MC in his Wolves bedroom. MC is laying on his bed, phone to ear (talking to Lauren), thoughtful expression as he listens, mouth closed.
        with dissolve

        la "Oh no, I actually had an amazing project. I had worked on it non-stop for four months straight."
        
        la "It was a huge installation of the solar system that would look beautiful and glow in the dark. It had proper orbiting and everything."
        
        la "Since it would work best in the dark, I asked if I could have a room at the school instead of showing it off at a stand in the gym like everyone else."
        
        la "Well, once the science fair started, I waited 6 hours in that room. By myself. Not even the teacher that unlocked the room for me came by."
        
        la "Apparently he had forgotten to put up the sign that'd tell people about my installation."

        scene v10scwl1b # TPP. Same camera as v10scwl1. Show Lauren as though FPP, she's sitting on the train. Lauren on phone listening to MC, neutral/thoughtful expression, mouth closed.
        with dissolve

        u "Holy shit, that's so sad. I wish I could've seen the project. It sounds really cool."

        scene v10scwl1c # TPP. Same camera as v10scwl1. Show Lauren as though FPP, she's sitting on the train. Lauren on phone listening to MC, neutral/thoughtful expression, mouth open.
        with dissolve

        la "Yeah, it was. I guess no one will ever know."

        scene v10scwl1b
        with dissolve

        u "I assume you haven't forgiven your teacher to this day, huh?"

        scene v10scwl2b # TPP. Same camera as v10scwl2. Show MC in his Wolves bedroom. MC is laying on his bed, normal/content expression, mouth closed.
        with dissolve

        la "Well... no. But, in all fairness, most of my teachers weren't the nicest people anyways. I'm just glad that phase of my life is over."

        scene v10scwl1b
        with dissolve

        u "Sounds like you really didn't have a good time in middle school."

        scene v10scwl2b
        with dissolve

        la "It was a private school, so... no."

        scene v10scwl1b
        with dissolve

        u "Damn, you went to a private school?"

        scene v10scwl2b
        with dissolve

        la "Not just any private school... a very strict, religious one."

        scene v10scwl1b
        with dissolve

        u "Oh, I didn't even know you were super religious."

        scene v10scwl2b
        with dissolve

        la "I don't know what I am, but I know my parents are."

        scene v10scwl1b
        with dissolve

        u "So what's that like, growing up with very religious parents?"

        scene v10scwl2b
        with dissolve

        la "Uhm I don't know. I love my parents, but there were times when I really felt like I needed a break from them."
        
        la "My sister never really got along with them. Her whole \"fight the system\" mindset. She was always her own person and to be honest, I've always respected that a lot about her."

        scene v10scwl1b
        with dissolve

        u "Do you feel like you're not your own person?"

        scene v10scwl2a
        with dissolve

        la "Well, I just like making people happy. Sometimes to make others happy I have to do what I don't want to do. Maybe I just want to do me for once, you know?"

        scene v10scwl2a
        with dissolve
        menu:
            "Agree":
                scene v10scwl1b
                with dissolve
            
                u "Yeah, I get what you mean. I feel like we shouldn't ever sacrifice our own happiness just to make others happy. If we don't look out for ourselves then who will."

                scene v10scwl2
                with dissolve

                la "Never too late to start living for Lauren. *Chuckles*"

                scene v10scwl1
                with dissolve

                u "*Chuckles* Exactly."

            "Disagree":
                scene v10scwl1b
                with dissolve
                    
                u "I guess, but it's also nice to make other people happy. I don't know, your selflessness is one of the things I like most about you."

                scene v10scwl2b
                with dissolve

                la "Thanks, I guess. Yeah, you're probably right. I don't know. I think it's about finding a balance."

        scene v10scwl2
        with dissolve

        la "So uhm... rapid change of topics, do you want kids someday?"

        if CharacterService.is_girlfriend(lauren): # RCS - if MC is in a relationship with Lauren
            scene v10scwl1
            with dissolve

            u "Wait, is this like a trick question where I gotta make sure that my answer doesn't hurt your feelings or something?"

            scene v10scwl1a
            with dissolve

            la "*Laughs* No, I'm just interested in my boyfriend's thoughts."

            scene v10scwl1
            with dissolve

            u "Haha alright."

        scene v10scwl2a
        with dissolve
        menu:
            "Yes":
                scene v10scwl1
                with dissolve

                u "Someday I do, I consider myself somewhat of a family man. *Chuckles*"

                scene v10scwl2
                with dissolve

                la "I do too, well, family woman. The chance to create a person and then just be able to give that person the most amazing life possible just sounds too good to pass up on."

                if CharacterService.is_girlfriend(lauren): # RCS - MC is in a relationship with Lauren
                    scene v10scwl1a
                    with dissolve
                    
                    la "I think we'd make great parents, you know? And as long as you don't let your mother feed them, we may even have another childhood star in the family. *Laughs*"

                    scene v10scwl1
                    with dissolve

                    u "*Chuckles* Just not letting that one go, are you?"

                    scene v10scwl2
                    with dissolve

                    la "Not a chance."

                else: # RCS - MC is not in a relationship with Lauren
                    scene v10scwl1
                    with dissolve
                    
                    u "Someday I do, I consider myself somewhat of a family man. *Chuckles*"

                    scene v10scwl1a
                    with dissolve

                    la "Those poor kids, little do they know they're doomed to be fat babies."

                    scene v10scwl1
                    with dissolve

                    u "*Chuckles* Just not letting that one go, are you?"

                    scene v10scwl2
                    with dissolve

                    la "Not a chance."
        
            "No":
                scene v10scwl1b
                with dissolve

                u "I don't think so, kinda sounds expensive. I'm just not really a big family man."

                scene v10scwl2
                with dissolve

                la "Really? I definitely want kids. The chance to create a person and then just be able to give that person the most amazing life possible just sounds too good to pass up on."

                scene v10scwl1b
                with dissolve

                u "Yeah, I guess. I don't really know, it seems like a lot of responsibility."

                scene v10scwl1a
                with dissolve

                la "*Laughs* Having a kid? Yeah that's kind of the point."

        scene v10scwl1
        with dissolve

        u "You ever just have random questions pop up in your head, but then you're like... wait a minute, I don't even know what I'd do in that scenario?"

        scene v10scwl2
        with dissolve

        la "What? *Chuckles* Give me an example."

        scene v10scwl1
        with dissolve

        u "Okay, so right before I went to bed last night I thought about this. If you're a genie and someone says \"I wish you wouldn't grant me this wish\", what do you do?"

        scene v10scwl2
        with dissolve

        la "Uhm, not grant him the wish! *Laughs*"

        scene v10scwl1
        with dissolve

        u "You're making it too easy! If you're not granting him the wish then you would be granting him the wish, but that would mean you wouldn't grant him the wish and that-"

        scene v10scwl2
        with dissolve

        la "Okay, okay. I see what you're getting at. *Chuckles*"

        la "Anyways it looks like we're pulling up on the station, I really appreciate that we talked the whole time! Made time pass by a lot faster."

        scene v10scwl1
        with dissolve

        u "*Chuckles* Anytime."

        scene v10scwl2
        with dissolve

        la "Talk to you soon, bye."

        scene v10scwl1
        with dissolve

        u "Bye bye."

        scene v10scwl2
        with dissolve
        
        pause 0.5

        scene v10scwl2b
        with fade

        u "(Wow, that was quite a long call, but I feel like I really learned a lot about her... It's not that late, maybe I can go for a bit of a walk before going to bed.)"

        stop music fadeout 3

        jump v10_walk_jenny_text # -Transition to Scene 19-
    
    else: # MC is an ape
        scene v10scwl1
        with fade

        u "Excited for the charity event?"

        scene v10saow3 # IGNORE, RENDER FROM SCENE 15
        with dissolve

        la "Excited, nervous, all of the above."

        scene v10scwl1
        with dissolve

        u "Why are you nervous?"

        scene v10scwl1a
        with dissolve

        la "I just want everything to run smoothly. My sister would be pretty upset if things didn't go as planned."

        scene v10saow3 
        with dissolve
        menu:
            "Joke":
                scene v10scwl1
                with dissolve

                u "Just make things go as planned then, sounds easy enough. Nothings ever gone wrong at a college student hosted event. *Chuckles*"

                scene v10saow3 
                with dissolve

                la "Very funny..."
            
            "Be serious":
                scene v10scwl1
                with dissolve

                u "I'm sure everything will go just fine, if there's anything that needs special attention I'm sure your sister is already on top of it."

                scene v10saow3 
                with dissolve

                la "Hopefully."

        scene v10saow3 
        with dissolve

        la "It's also like... what if no one comes to my thing? And I put all this work in and just no one ever comes by."

        scene v10scwl1
        with dissolve

        u "*Laughs* So the whole event is buzzing and every stand has a long queue, but just absolutely no one comes to you? That would be pretty funny to be fair."

        scene v10saow3 
        with dissolve

        la "Well I'm glad my failure amuses you."

        scene v10scwl1
        with dissolve

        u "Okay, IMAGINARY failure. Obviously that's not gonna happen."

        scene v10scwl1a
        with dissolve

        la "I don't know, this could be middle school all over again."

        scene v10scwl1
        with dissolve

        u "What happened in middle school?"

        scene v10saow3 
        with dissolve

        la "We had this school science fair, where everyone was supposed to show off the project they had been working on for the last few months-"

        scene v10scwl1
        with dissolve

        u "Let me guess, you didn't have a project."

        scene v10saow3a # IGNORE, RENDER FROM SCENE 15
        with dissolve

        la "Oh no, I actually had an amazing project. I had worked on it non-stop for four months straight."
        
        la "It was a huge installation of the solar system that would look beautiful and glow in the dark. It had proper orbiting and everything."
        
        la "Since it would work best in the dark, I asked if I could have a room at the school instead of showing it off at a stand in the gym like everyone else."
        
        la "Well, once the science fair started, I waited 6 hours in that room. By myself. Not even the teacher that unlocked the room for me came by."
        
        la "Apparently he had forgotten to put up the sign that'd tell people about my installation."

        scene v10scwl1b # TPP. Same camera as v10scwl1. Show Lauren as though FPP, she's sitting on the train. Lauren on phone listening to MC, neutral/thoughtful expression, mouth closed.
        with dissolve

        u "Holy shit, that's so sad. I wish I could've seen the project. It sounds really cool."

        scene v10scwl1c # TPP. Same camera as v10scwl1. Show Lauren as though FPP, she's sitting on the train. Lauren on phone listening to MC, neutral/thoughtful expression, mouth open.
        with dissolve

        la "Yeah, it was. I guess no one will ever know."

        scene v10scwl1b
        with dissolve

        u "I assume you haven't forgiven your teacher to this day, huh?"

        scene v10saow3b # TPP. Same camera as v10saow3. Show MC in his Ape bedroom. MC is laying on his bed, normal/content expression, mouth closed.
        with dissolve

        la "Well... no. But, in all fairness, most of my teachers weren't the nicest people anyways. I'm just glad that phase of my life is over."

        scene v10scwl1b
        with dissolve

        u "Sounds like you really didn't have a good time in middle school."

        scene v10saow3b
        with dissolve

        la "It was a private school, so... no."

        scene v10scwl1b
        with dissolve

        u "Damn, you went to a private school?"

        scene v10scwl1c
        with dissolve

        la "Not just any private school... a very strict, religious one."

        scene v10saow3b
        with dissolve

        u "Oh, I didn't even know you were super religious."

        scene v10saow3a
        with dissolve

        la "I don't know what I am, but I know my parents are."

        scene v10scwl1b
        with dissolve

        u "So what's that like, growing up with very religious parents?"

        scene v10saow3a
        with dissolve

        la "Uhm I don't know. I love my parents, but there were times when I really felt like I needed a break from them."
        
        la "My sister never really got along with them. Her whole \"fight the system\" mindset. She was always her own person and to be honest, I've always respected that a lot about her."

        scene v10scwl1b
        with dissolve

        u "Do you feel like you're not your own person?"

        scene v10scwl1c
        with dissolve

        la "Well, I just like making people happy. Sometimes to make others happy I have to do what I don't want to do. Maybe I just want to do me for once, you know?"

        scene v10saow3a
        with dissolve
        menu:
            "Agree":
                scene v10scwl1b
                with dissolve
            
                u "Yeah, I get what you mean. I feel like we shouldn't ever sacrifice our own happiness just to make others happy. If we don't look out for ourselves then who will."

                scene v10saow3
                with dissolve

                la "Never too late to start living for Lauren. *Chuckles*"

                scene v10scwl1
                with dissolve

                u "*Chuckles* Exactly."

            "Disagree":
                scene v10scwl1b
                with dissolve
                    
                u "I guess, but it's also nice to make other people happy. I don't know, your selflessness is one of the things I like most about you."

                scene v10saow3
                with dissolve

                la "Thanks, I guess. Yeah, you're probably right. I don't know. I think it's about finding a balance."

        scene v10scwl1c
        with dissolve

        la "So uhm... rapid change of topics, do you want kids someday?"

        if CharacterService.is_girlfriend(lauren): # RCS - if MC is in a relationship with Lauren
            scene v10scwl1
            with dissolve

            u "Wait, is this like a trick question where I gotta make sure that my answer doesn't hurt your feelings or something?"

            scene v10saow3
            with dissolve

            la "*Laughs* No, I'm just interested in my boyfriend's thoughts."

            scene v10scwl1
            with dissolve

            u "Haha alright."

        scene v10saow3a
        with dissolve
        menu:
            "Yes":
                scene v10scwl1
                with dissolve

                u "Someday I do, I consider myself somewhat of a family man. *Chuckles*"

                scene v10saow3
                with dissolve

                la "I do too, well, family woman. The chance to create a person and then just be able to give that person the most amazing life possible just sounds too good to pass up on."

                if CharacterService.is_girlfriend(lauren): # RCS - MC is in a relationship with Lauren
                    scene v10scwl1a
                    with dissolve
                    
                    la "I think we'd make great parents, you know? And as long as you don't let your mother feed them, we may even have another childhood star in the family. *Laughs*"

                    scene v10scwl1
                    with dissolve

                    u "*Chuckles* Just not letting that one go, are you?"

                    scene v10saow3
                    with dissolve

                    la "Not a chance."

                else: # RCS - MC is not in a relationship with Lauren
                    scene v10scwl1
                    with dissolve
                    
                    u "Someday I do, I consider myself somewhat of a family man. *Chuckles*"

                    scene v10scwl1a
                    with dissolve

                    la "Those poor kids, little do they know they're doomed to be fat babies."

                    scene v10scwl1
                    with dissolve

                    u "*Chuckles* Just not letting that one go, are you?"

                    scene v10saow3
                    with dissolve

                    la "Not a chance."
        
            "No":
                scene v10scwl1b
                with dissolve

                u "I don't think so, kinda sounds expensive. I'm just not really a big family man."

                scene v10saow3
                with dissolve

                la "Really? I definitely want kids. The chance to create a person and then just be able to give that person the most amazing life possible just sounds too good to pass up on."

                scene v10scwl1b
                with dissolve

                u "Yeah, I guess. I don't really know, it seems like a lot of responsibility."

                scene v10saow3
                with dissolve

                la "*Laughs* Having a kid? Yeah that's kind of the point."

        scene v10scwl1
        with dissolve

        u "You ever just have random questions pop up in your head, but then you're like... wait a minute, I don't even know what I'd do in that scenario?"

        scene v10scwl1a
        with dissolve

        la "What? *Chuckles* Give me an example."

        scene v10scwl1
        with dissolve

        u "Okay, so right before I went to bed last night I thought about this. If you're a genie and someone says \"I wish you wouldn't grant me this wish\", what do you do?"

        scene v10saow3
        with dissolve

        la "Uhm, not grant him the wish! *Laughs*"

        scene v10scwl1
        with dissolve

        u "You're making it too easy! If you're not granting him the wish then you would be granting him the wish, but that would mean you wouldn't grant him the wish and that-"

        scene v10saow3
        with dissolve

        la "Okay, okay. I see what you're getting at. *Chuckles*"

        la "Anyways it looks like we're pulling up on the station, I really appreciate that we talked the whole time! Made time pass by a lot faster."

        scene v10scwl1
        with dissolve

        u "*Chuckles* Anytime."

        scene v10saow3
        with dissolve

        la "Talk to you soon, bye."

        scene v10scwl1
        with dissolve

        u "Bye bye."

        scene v10saow3
        with dissolve
        
        pause 0.5

        scene v10saow3b
        with fade

        u "(Wow, that was quite a long call, but I feel like I really learned a lot about her... It's not that late, maybe I can go for a bit of a walk before going to bed.)"

        stop music fadeout 3

        jump v10_walk_jenny_text # -Transition to Scene 19-