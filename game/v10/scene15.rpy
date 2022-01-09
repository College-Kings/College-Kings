# SCENE 15: Call With Lauren, Aubrey Outside Window
# Locations: MC's Room (Wolves/Apes)
# Characters: MC (Outfit 1), Lauren (Outfit 3), Aubrey (Outfit 3)
# Time:
label v10_call_with_lauren1:
    play music "music/v10/Track Scene 15.mp3" fadein 2
    if joinwolves: # MC is a wolf, is that the correct variable name?
        scene v10saow1 # TPP. Show MC in his Wolves bedroom, laying in his bed relaxing. He notices his phone buzzing. Curious/thoughtful expression, mouth closed.
        with fade

        play sound "sounds/call.mp3"
        
        pause 1

        u "(Guess I should get that.)"

        scene v10saow1a # TPP. Same camera as v10saow1. Show MC in his Wolves bedroom, laying in his bed relaxing. He checks his phone to see who's calling. Curious/thoughtful expression, mouth closed.
        with dissolve

        u "(Oh, it's Lauren.)"

        scene v10scwl1 # IGNORE, RENDER FROM SCENE 18.
        with dissolve
        stop sound
        play sound "sounds/answercall.mp3"

        u "Hello?"

        if lauren.relationship.value >= Relationship.GIRLFRIEND.value: # RCS - MC is a relationship with Lauren
            scene v10scwl1a # IGNORE, RENDER FROM SCENE 18
            with dissolve
            
            la "Heyyy, cutie, are you free right now?"

            scene v10scwl1
            with dissolve

            u "Sure, I'm just chilling in my room, what's up? Also, since when do you call me cutie?"
        
        else: # RCS - MC is not in a relationship with Lauren
            scene v10scwl1a
            with dissolve

            la "Heyyy, are you free right now?"

            scene v10scwl1
            with dissolve

            u "Sure, I'm just chilling in my room. What's up?"

        scene v10scwl2 # Ignore Render
        with dissolve

        la "Well... I'm stuck on a train for another 40 minutes and after spending the last 20 minutes looking through Kiwii, now I'm kinda bored."

        scene v10scwl1
        with dissolve

        u "Oh, where are you going?"

        scene v10scwl2
        with dissolve

        la "Actually, it was my mom's birthday, so yesterday I kinda just spontaneously decided to visit her and now I'm on my way back."

        scene v10scwl1
        with dissolve

        u "Aww that's cute, haha. What'd you get her?"

        scene v10scwl2
        with dissolve

        la "A necklace, she really loves jewelry. So uhm..."

        scene v10scwl1
        with dissolve

        u "What?"

        scene v10scwl2
        with dissolve

        la "Well I didn't really know what I wanted to talk about, I just wanted to talk. *Laughs*"

        scene v10scwl1
        with dissolve

        u "Guess that means you're leaving the conversation planning to me? *Laughs*"

        scene v10scwl2
        with dissolve

        la "That would be correct."

        scene v10scwl1
        with dissolve

        u "How about we play a game?"

        scene v10scwl1a
        with dissolve

        la "I mean at this point I'm happy with anything, what game did you have in mind?"

        scene v10scwl2
        with dissolve

        menu:
            "Two truths one lie":
                scene v10scwl2c # TPP. Same camera as v10scwl2. Show MC in his Wolves bedroom. MC is laying on his bed, normal/content expression, mouth open
                with dissolve

                u "How about we play two truths and a lie?"

                scene v10scwl2
                with dissolve

                la "Alright, but you start. I'm always bad at these things."

                scene v10scwl1
                with dissolve

                u "Okay let's see. I got chased by a pack of dogs after school and hid in a porta potty for hours as a kid..."
                
                u "I was the star in a children's show as an infant, and I'm a pretty good harmonica player."

                scene v10scwl2
                with dissolve

                la "So you just jump to the hardest difficulty huh? *Laughs*"

                scene v10scwl1
                with dissolve

                u "I don't want to brag or anything, but I am sort of a professional at this game. The trick is to live a life that's utterly ridiculous."

                scene v10scwl2
                with dissolve

                la "Honestly, I have no idea, haha. But I really want the harmonica and children's show stuff to be true, so I'm gonna say you did not get chased by a pack of dogs. Am I right?"

                scene v10scwl1
                with dissolve

                u "Are you?"

                scene v10scwl2
                with dissolve

                la "Oh no, don't tell me you're one of those people that changes the \"right\" answer so no one can ever guess correctly." 
                
                la "My dad always changed his answer when we played games. He'd put his fingers behind his back and tell me to guess how many fingers he was holding up."
                
                la "No matter what I guessed I'd always be wrong because come to find out he would change it if I got it right."

                scene v10scwl1
                with dissolve

                u "*Smiles* That's actually hilarious. But I won't do you like that. You actually were right."

                scene v10scwl1a
                with dissolve

                la "*Laughs* Really?"

                scene v10scwl1
                with dissolve

                u "Yeah, I'd rather get chewed up by dogs then suffer the smell of a porta potty for hours."

                scene v10scwl2
                with dissolve

                la "I was gonna say it would've been impressive if you could stand the smell that long. In that case, we have to pause the game and talk about these truths."

                scene v10scwl1
                with dissolve

                u "Yeah to be fair, I kinda knew you were gonna follow up on them when I said them out loud. *Chuckles*"

                scene v10scwl2
                with dissolve

                la "Sooo, you were an infant TV sensation? And you've never told me about it?"

                scene v10scwl1
                with dissolve

                u "*Laughs* First of all, sensation may be pushing it a bit. Second of all, I don't really tell anyone about it."
                
                u "I mean it was all my grandmother's idea really."
                
                u "She was obsessed at how cute I was so she found me an agent, my agent got me on the show, and after one short season the show got cancelled."
                
                u "The rest is history."

                scene v10scwl2
                with dissolve

                la "Wait, why did the show get cancelled?"

                scene v10scwl1
                with dissolve

                u "Do I really have to say?"

                scene v10scwl1a
                with dissolve

                la "*Laughs* Now you do!"

                scene v10scwl1
                with dissolve

                u "It's because I gained a whole lot of baby weight and the producers said a \"fat\" baby wasn't good for the camera."

                scene v10scwl2
                with dissolve

                la "Awww, why is that both funny and sad? Okay, now explain the second one."

                scene v10scwl1
                with dissolve

                u "What was the second one again? Only thing I can think about right now are my fat baby rolls."

                scene v10scwl2
                with dissolve

                la "Haha, you said you played the harmonica..."

                scene v10scwl1
                with dissolve

                u "Oh yeah, I played a lot growing up. I used to love those old western movies and all the cool cowboys played the harmonica so I picked it up."
                
                u "After a few years of dabbling, I got really good."

                scene v10scwl2
                with dissolve

                la "Can you still play?"

                scene v10scwl1
                with dissolve

                u "I haven't played in a long time, but sure. I could definitely pick it up anytime."

                scene v10scwl1a
                with dissolve

                la "I'm gonna need proof of a claim that bold."

                scene v10scwl2
                with dissolve

                menu:
                    "I could play":      
                        scene v10scwl2c
                        with dissolve

                        u "I guess it wouldn't hurt to give a little performance sometime."

                        if lauren.relationship.value >= Relationship.GIRLFRIEND.value: # MC is in a relationship with Lauren
                            scene v10scwl1a
                            with dissolve
                            
                            la "Maybe on our next date?"

                            scene v10scwl1
                            with dissolve

                            u "Sure, that sounds good."

                            scene v10scwl1a
                            with dissolve

                            la "Can't wait. You don't hear of a lot of people playing the harmonica, almost as rare as hearing someone be able to play the harp."

                            scene v10scwl1
                            with dissolve

                            u "What can I say, I'm a unique guy."
                    
                    "Joke around":
                        scene v10scwl2c 
                        with dissolve
                        
                        u "Well there's certainly ways to prove my mouth agility to you."

                        scene v10scwl1a
                        with dissolve

                        la "What do you mean?"

                        scene v10scwl1
                        with dissolve

                        u "You know, playing the harmonica requires quite a lot of tongue coordination, usually girls like that."

                        if lauren.relationship.value >= Relationship.KISS.value: # maybe another variable for having madeout with lauren?
                            scene v10scwl2
                            with dissolve

                            la "*Laughs* Ewww, [name] stop it!"

                            scene v10scwl1
                            with dissolve

                            u "*Laughs* What? I'm just saying!"

                            scene v10scwl2
                            with dissolve

                            la "You're unbelievable, I just wanted to hear you play!"

                            scene v10scwl1
                            with dissolve

                            u "*Chuckles* Fine, we can do that too."

                        else: # RCS - MC is not in a relationship with Lauren, and didn't makeout with her
                            scene v10scwl2
                            with dissolve
                            
                            la "Uhm, I think I'll pass."

                            scene v10scwl1
                            with dissolve

                            u "Alright, offer stands."

                            scene v10scwl2
                            with dissolve

                            la "I just wanted to hear you play."

                            scene v10scwl1
                            with dissolve

                            u "Fine, I can do that too."

                            scene v10scwl2
                            with dissolve

                            la "Good."
        
            "Favorites":
                scene v10scwl2c 
                with dissolve
                
                u "Let's play favorites!"

                scene v10scwl2
                with dissolve

                la "Favorites? I don't know if I know what that is."

                scene v10scwl1
                with dissolve

                u "Honestly, I'm not sure if I made it up or learned about it from someone else. It's a pretty simple game."
                
                u "I just name a topic, say my favorite thing in that topic and then you answer your favorite. Then the game continues, but switched."

                if lauren.relationship.value >= Relationship.GIRLFRIEND.value: # RCS - MC is in a relationship with Lauren
                    scene v10scwl2
                    with dissolve

                    la "Uhm, I mean sure. Anything's better than doing nothing on this train."

                    scene v10scwl1
                    with dissolve

                    u "Okay, I feel like considering you get to talk to your boyfriend and hear about all his favorite things, you're getting a pretty good deal here."

                    scene v10scwl2
                    with dissolve

                    la "*Chuckles* My bad, you're right. I'm excited to hear all of your favorites and I'm sure this game will be an essential pillar to the strengthening of our relationship."

                    scene v10scwl1
                    with dissolve

                    u "See, that wasn't so hard, was it?"

                    scene v10scwl1a
                    with dissolve

                    la "Yeah, yeah, yeah. *Laughs* Can we start already?"

                else:
                    scene v10scwl2
                    with dissolve
                    
                    la "Seems easy enough. Let's do it."

                scene v10scwl1
                with dissolve
                
                u "Alright let's go."

                scene v10scwl2
                with dissolve

                menu:
                    "Orange":
                        scene v10scwl2c 
                        with dissolve
                        
                        u "Color, orange."

                    "Blue":
                        scene v10scwl2c 
                        with dissolve

                        u "Color, blue."

                scene v10scwl1a
                with dissolve

                la "Green. Animal, lemur monkey."

                scene v10scwl1
                with dissolve

                u "Cute."

                scene v10scwl2
                with dissolve

                menu:
                    "Gecko":
                        scene v10scwl2c 
                        with dissolve
                        
                        u "Gecko."
                    
                    "Lion":
                        scene v10scwl2c 
                        with dissolve
                        
                        $ grant_achievement("rawr_im_a_lion")
                        u "Lion."

                scene v10scwl2
                with dissolve

                menu:
                    "Spring":
                        scene v10scwl2c 
                        with dissolve
                        
                        u "Hmm, season... Spring."

                    "Fall":
                        scene v10scwl2c 
                        with dissolve

                        u "Hmm, season... Fall."
            
                scene v10scwl1a
                with dissolve

                la "Fall. Holiday, my birthday."

                scene v10scwl1
                with dissolve

                u "Wait, what? Your birthday doesn't count as a holiday... well unless your birthday is on a holiday. *Laughs*"

                scene v10scwl2
                with dissolve

                la "My birthday actually is a holiday, can you guess which one."

                scene v10scwl1
                with dissolve

                u "Hmmm, can I get a hint?"

                scene v10scwl2
                with dissolve

                la "I feel like a hint is hard to give without giving it away. Let's see, well... it's one of the major holidays."

                scene v10scwl1
                with dissolve

                u "Kinda surprised I don't know your birthday already, but let's see, are you a Christmas baby?"

                scene v10scwl2
                with dissolve

                la "Nope! Wanna keep guessing?"

                scene v10scwl1
                with dissolve

                u "New Years Baby?"

                scene v10scwl2
                with dissolve

                la "Nope! I'll just tell you, my birthday is Halloween."

                scene v10scwl1
                with dissolve

                u "Wait, is Halloween a holiday?"

                scene v10scwl2
                with dissolve

                la "Yeah, of course. You ever had school on Halloween? *Chuckles* What did you think it was?"

                scene v10scwl1
                with dissolve

                u "I don't know, like a day were people celebrate scary stuff and don't have to go to school because of it."

                scene v10scwl2
                with dissolve

                la "Celebrating and time off, and that does not sound like a holiday to you why? *Laughs*"

                scene v10scwl1
                with dissolve

                u "*Chuckles* Huh, I guess you're right."

                scene v10scwl1
                with dissolve

                u "So Halloween. You must like horror movies and stuff."

                scene v10scwl2
                with dissolve

                la "Honestly, I can't stand anything scary related and most people are surprised when they know Halloween is my birthday."

                scene v10scwl1
                with dissolve

                u "I have to admit it is a bad coincidence."

                scene v10scwl2
                with dissolve

                la "Are you a big Halloween fan?"

                scene v10scwl1
                with dissolve

                u "I actually love Halloween, but I-"

        play sound "sounds/twig.mp3"

        scene v10saow1b # TPP. Same camera as v10saow1. MC laying in his bed relaxing. He has the phone up to his ear, talking with Lauren. He looks over towards his window. Curious/thoughtful expression, mouth closed.
        with dissolve
        
        pause 1

        scene v10saow1c # TPP. Same camera as v10saow1. Show MC in his Wolves bedroom, laying in his bed relaxing. He puts the phone aside and gets up from his bed. Curious expression, mouth closed.
        with dissolve
        
        pause 0.75
        
        scene v10saow1e # TPP. Same camera as v10saow1. Show MC in his Wolves bedroom, standing by his bed with his phone up to his ear (talking with Lauren). Normal expression, mouth open.
        with dissolve

        u "Hey Lauren, mind giving me just a sec?"

        scene v10saow1d # TPP. Same camera as v10saow1. Show MC in his Wolves bedroom, standing by his bed with his phone up to his ear (talking with Lauren). Normal expression, mouth closed.
        with dissolve

        la "Yeah sure!"

        scene v10saow5 # FPP. MC is looking out the window. Show Aubrey outside in gym clothes, smiling, mouth closed.
        with fade

        u "Hey, what's up? Also, did you just throw a pebble at my window? *Chuckles*"

        scene v10saow5a # FPP. Same camera as v10saow5. MC is looking out the window. Show Aubrey, smiling, mouth open.
        with dissolve

        au "That must have been the wind. I'm just on my way home from the gym."

        if aubrey.relationship.value >= Relationship.FWB.value: # RCS - MC is in a relationship with Aubrey
            scene v10saow5a
            with dissolve

            au "I'm gonna have the house all to myself since none of the girls are home. You wanna come over?"

            scene v10saow5
            with dissolve

            menu:
                "Walk her home":
                    scene v10saow5
                    with dissolve

                    u "Hell yeah, I'll be down in a second."

                    scene v10saow1d
                    with dissolve
                    
                    pause 0.5

                    scene v10scwl1b # Ignore Render
                    with fade

                    u "Hey Lauren..."

                    scene v10scwl1c # Ignore Render
                    with dissolve

                    la "There you are, something wrong?"

                    scene v10scwl1b
                    with dissolve

                    u "No, nothing's wrong, but I have to go. Apparently there's some frat thing coming up they wanna prep us for."

                    scene v10scwl1c
                    with dissolve

                    la "Oh okay... no problem, I'll talk to you soon."

                    scene v10scwl1b
                    with dissolve

                    u "Bye bye."

                    jump v10_aubrey_house
                
                "Don't walk her home": # RCS - there was nothing for this so I just used the stuff from no relationship w/ Aubrey branch
                    scene v10saow5
                    with dissolve

                    u "I'd love to, but I'm busy right now, sorry."

                    scene v10saow5a
                    with dissolve

                    au "Oh okay, guess I'll see you around then."

                    scene v10saow5
                    with dissolve

                    u "See ya!"

                    scene v10saow1d
                    with dissolve
                    
                    pause 0.5

                    scene v10scwl1
                    with fade

                    u "Hey Lauren!"

                    scene v10scwl2 
                    with dissolve

                    la "There you are? Everything okay?"

                    scene v10scwl1
                    with dissolve

                    u "Yeah everything's fine, had a bird at my window. *Laughs*"

                    scene v10scwl2 
                    with dissolve

                    la "A bird took you that long? What'd you do, sing to it? *Laughs*"

                    scene v10scwl1
                    with dissolve

                    u "Something like that."

        else: # RCS - MC is not in a relationship with Aubrey
            scene v10saow5a
            with dissolve

            au "It's kind of a long walk, wanna go with me and hang out?"

            scene v10saow5
            with dissolve

            menu:
                "Walk her home":
                    scene v10saow5
                    with dissolve

                    u "Yeah sure, I'll be right down."

                    scene v10saow1d
                    with dissolve

                    pause 0.5
                    
                    scene v10scwl1b
                    with fade

                    u "Hey Lauren..."

                    scene v10scwl1c
                    with dissolve

                    la "There you are, something wrong?"

                    scene v10scwl1b
                    with dissolve

                    u "No nothing's wrong, but I have to go. Something came up."

                    scene v10scwl1c
                    with dissolve

                    la "Oh okay... no problem, I'll talk to you soon."

                    scene v10scwl1b
                    with dissolve

                    u "Later."

                    jump v10_aubrey_house
            
                "Don't walk her home":
                    scene v10saow5
                    with dissolve

                    u "I'd love to, but I'm busy right now, sorry."

                    scene v10saow5a
                    with dissolve

                    au "Oh okay, guess I'll see you around then."

                    scene v10saow5
                    with dissolve

                    u "See ya!"

                    scene v10saow1d
                    with dissolve

                    pause 0.5

                    scene v10scwl1
                    with fade

                    u "Hey Lauren!"

                    scene v10scwl2 
                    with dissolve

                    la "There you are? Everything okay?"

                    scene v10scwl2 
                    with dissolve

                    u "Yeah everything's fine, had a bird at my window. *Laughs*"

                    scene v10scwl1a
                    with dissolve

                    la "A bird took you that long? What'd you do, sing to it? *Laughs*"

                    scene v10scwl2 
                    with dissolve

                    u "Something like that."
    
    else: # mc is an ape
        scene v10saow4 # TPP. Show MC in his Ape bedroom, laying in his bed relaxing. He notices his phone buzzing. Curious/thoughtful expression, mouth closed.
        with fade

        u "(Guess I should get that.)"

        scene v10saow4a # TPP. Same camera as v10saow1. Show MC in his Ape bedroom, laying in his bed relaxing. He checks his phone to see who's calling. Curious/thoughtful expression, mouth closed.
        with dissolve

        u "(Oh it's Lauren.)"

        scene v10scwl1 # IGNORE, RENDER FROM SCENE 18.
        with dissolve

        u "Hello?"

        if lauren.relationship.value >= Relationship.GIRLFRIEND.value: # RCS - MC is a relationship with Lauren
            scene v10scwl1a # IGNORE, RENDER FROM SCENE 18
            with dissolve
            
            la "Heyyy, cutie, are you free right now?"

            scene v10scwl1
            with dissolve

            u "Sure, I'm just chilling in my room, what's up? Also, since when do you call me cutie?"
        
        else: # RCS - MC is not in a relationship with Lauren
            scene v10scwl1a
            with dissolve

            la "Heyyy, are you free right now?"

            scene v10scwl1
            with dissolve

            u "Sure, I'm just chilling in my room. What's up?"

        scene v10saow3 # TPP. Show MC in his Ape bedroom. MC is laying on his bed, phone to ear (talking to Lauren), smiling, mouth closed.
        with dissolve

        la "Well... I'm stuck on a train for another 40 minutes and after spending the last 20 minutes looking through Kiwii, now I'm kinda bored."

        scene v10scwl1
        with dissolve

        u "Oh, where are you going?"

        scene v10saow3
        with dissolve

        la "Actually, it was my mom's birthday, so yesterday I kinda just spontaneously decided to visit her and now I'm on my way back."

        scene v10scwl1
        with dissolve

        u "Aww that's cute, haha. What'd you get her?"

        scene v10saow3
        with dissolve

        la "A necklace, she really loves jewelry. So uhm..."

        scene v10scwl1
        with dissolve

        u "What?"

        scene v10saow3
        with dissolve

        la "Well I didn't really know what I wanted to talk about, I just wanted to talk. *Laughs*"

        scene v10scwl1
        with dissolve

        u "Guess that means you're leaving the conversation planning to me? *Laughs*"

        scene v10saow3
        with dissolve

        la "That would be correct."

        scene v10scwl1
        with dissolve

        u "How about we play a game?"

        scene v10scwl1a
        with dissolve

        la "I mean at this point I'm happy with anything, what game did you have in mind?"

        scene v10saow3 
        with dissolve

        menu:
            "Two truths one lie":
                scene v10saow3c # TPP. Same camera as v10scwl2. Show MC in his Ape bedroom. MC is laying on his bed, normal/content expression, mouth open
                with dissolve

                u "How about we play two truths and a lie?"

                scene v10scwl1a
                with dissolve

                la "Alright, but you start. I'm always bad at these things."

                scene v10scwl1
                with dissolve

                u "Okay let's see. I got chased by a pack of dogs after school and hid in a porta potty for hours as a kid..."
                
                u "I was the star in a children's show as an infant, and I'm a pretty good harmonica player."

                scene v10saow3
                with dissolve

                la "So you just jump to the hardest difficulty huh? *Laughs*"

                scene v10scwl1
                with dissolve

                u "I don't want to brag or anything, but I am sort of a professional at this game. The trick is to live a life that's utterly ridiculous."

                scene v10saow3
                with dissolve

                la "Honestly, I have no idea, haha. But I really want the harmonica and children's show stuff to be true, so I'm gonna say you did not get chased by a pack of dogs. Am I right?"

                scene v10scwl1
                with dissolve

                u "Are you?"

                scene v10saow3
                with dissolve

                la "Oh no, don't tell me you're one of those people that changes the \"right\" answer so no one can ever guess correctly." 
                
                la "My dad always changed his answer when we played games. He'd put his fingers behind his back and tell me to guess how many fingers he was holding up."
                
                la "No matter what I guessed I'd always be wrong because come to find out he would change it if I got it right."

                scene v10scwl1
                with dissolve

                u "*Smiles* That's actually hilarious. But I won't do you like that. You actually were right."

                scene v10scwl1a
                with dissolve

                la "*Laughs* Really?"

                scene v10scwl1
                with dissolve

                u "Yeah, I'd rather get chewed up by dogs then suffer the smell of a porta potty for hours."

                scene v10saow3
                with dissolve

                la "I was gonna say it would've been impressive if you could stand the smell that long. In that case, we have to pause the game and talk about these truths."

                scene v10scwl1
                with dissolve

                u "Yeah to be fair, I kinda knew you were gonna follow up on them when I said them out loud. *Chuckles*"

                scene v10saow3
                with dissolve

                la "Sooo, you were an infant TV sensation? And you've never told me about it?"

                scene v10scwl1
                with dissolve

                u "*Laughs* First of all, sensation may be pushing it a bit. Second of all, I don't really tell anyone about it."
                
                u "I mean it was all my grandmother's idea really."
                
                u "She was obsessed at how cute I was so she found me an agent, my agent got me on the show, and after one short season the show got cancelled."
                
                u "The rest is history."

                scene v10saow3
                with dissolve

                la "Wait, why did the show get cancelled?"

                scene v10scwl1
                with dissolve

                u "Do I really have to say?"

                scene v10saow3
                with dissolve

                la "*Laughs* Now you do!"

                scene v10scwl1
                with dissolve

                u "It's because I gained a whole lot of baby weight and the producers said a \"fat\" baby wasn't good for the camera."

                scene v10saow3
                with dissolve

                la "Awww, why is that both funny and sad? Okay, now explain the second one."

                scene v10scwl1
                with dissolve

                u "What was the second one again? Only thing I can think about right now are my fat baby rolls."

                scene v10saow3
                with dissolve

                la "Haha, you said you played the harmonica..."

                scene v10scwl1
                with dissolve

                u "Oh yeah, I played a lot growing up. I used to love those old western movies and all the cool cowboys played the harmonica so I picked it up."
                
                u "After a few years of dabbling, I got really good."

                scene v10saow3
                with dissolve

                la "Can you still play?"

                scene v10scwl1
                with dissolve

                u "I haven't played in a long time, but sure. I could definitely pick it up anytime."

                scene v10scwl1a
                with dissolve

                la "I'm gonna need proof of a claim that bold."

                scene v10saow3
                with dissolve

                menu:
                    "I could play":      
                        scene v10saow3c
                        with dissolve

                        u "I guess it wouldn't hurt to give a little performance sometime."

                        if lauren.relationship.value >= Relationship.GIRLFRIEND.value: # MC is in a relationship with Lauren
                            scene v10scwl1a
                            with dissolve
                            
                            la "Maybe on our next date?"

                            scene v10scwl1
                            with dissolve

                            u "Sure, that sounds good."

                            scene v10saow3
                            with dissolve

                            la "Can't wait. You don't hear of a lot of people playing the harmonica, almost as rare as hearing someone be able to play the harp."

                            scene v10scwl1
                            with dissolve

                            u "What can I say, I'm a unique guy."
                    
                    "Joke around":
                        scene v10saow3c
                        with dissolve
                        
                        u "Well there's certainly ways to prove my mouth agility to you."

                        scene v10saow3
                        with dissolve

                        la "What do you mean?"

                        scene v10scwl1
                        with dissolve

                        u "You know, playing the harmonica requires quite a lot of tongue coordination, usually girls like that."

                        if lauren.relationship.value >= Relationship.KISS.value: # maybe another variable for having madeout with lauren?
                            scene v10scwl1a
                            with dissolve

                            la "*Laughs* Ewww, [name] stop it!"

                            scene v10scwl1
                            with dissolve

                            u "*Laughs* What? I'm just saying!"

                            scene v10saow3
                            with dissolve

                            la "You're unbelievable, I just wanted to hear you play!"

                            scene v10scwl1
                            with dissolve

                            u "*Chuckles* Fine, we can do that too."

                        else: # RCS - MC is not in a relationship with Lauren, and didn't makeout with her
                            scene v10scwl1a
                            with dissolve
                            
                            la "Uhm, I think I'll pass."

                            scene v10scwl1
                            with dissolve

                            u "Alright, offer stands."

                            scene v10saow3
                            with dissolve

                            la "I just wanted to hear you play."

                            scene v10scwl1
                            with dissolve

                            u "Fine, I can do that too."

                            scene v10saow3
                            with dissolve

                            la "Good."
        
            "Favorites":
                scene v10saow3c
                with dissolve
                
                u "Let's play favorites!"

                scene v10scwl1a
                with dissolve

                la "Favorites? I don't know if I know what that is."

                scene v10scwl1
                with dissolve

                u "Honestly, I'm not sure if I made it up or learned about it from someone else. It's a pretty simple game."
                
                u "I just name a topic, say my favorite thing in that topic and then you answer your favorite. Then the game continues, but switched."

                if lauren.relationship.value >= Relationship.GIRLFRIEND.value: # RCS - MC is in a relationship with Lauren
                    scene v10saow3
                    with dissolve

                    la "Uhm, I mean sure. Anything's better than doing nothing on this train."

                    scene v10scwl1
                    with dissolve

                    u "Okay, I feel like considering you get to talk to your boyfriend and hear about all his favorite things, you're getting a pretty good deal here."

                    scene v10saow3
                    with dissolve

                    la "*Chuckles* My bad, you're right. I'm excited to hear all of your favorites and I'm sure this game will be an essential pillar to the strengthening of our relationship."

                    scene v10scwl1
                    with dissolve

                    u "See, that wasn't so hard, was it?"

                    scene v10saow3
                    with dissolve

                    la "Yeah, yeah, yeah. *Laughs* Can we start already?"

                else:
                    scene v10saow3
                    with dissolve
                    
                    la "Seems easy enough. Let's do it."

                scene v10scwl1
                with dissolve
                
                u "Alright let's go."

                scene v10saow3
                with dissolve

                menu:
                    "Orange":
                        scene v10saow3c
                        with dissolve
                        
                        u "Color, orange."

                    "Blue":
                        scene v10saow3c
                        with dissolve

                        u "Color, blue."

                scene v10scwl1a
                with dissolve

                la "Green. Animal, lemur monkey."

                scene v10scwl1
                with dissolve

                u "Cute."

                scene v10saow3
                with dissolve

                menu:
                    "Gecko":
                        scene v10saow3c
                        with dissolve
                        
                        u "Gecko."
                    
                    "Lion":
                        scene v10saow3c
                        with dissolve

                        $ grant_achievement("rawr_im_a_lion")
                        u "Lion."

                scene v10saow3
                with dissolve

                menu:
                    "Spring":
                        scene v10saow3c
                        with dissolve
                        
                        u "Hmm, season... Spring."

                    "Fall":
                        scene v10saow3c
                        with dissolve

                        u "Hmm, season... Fall."
            
                scene v10scwl1a
                with dissolve

                la "Fall. Holiday, my birthday."

                scene v10scwl1
                with dissolve

                u "Wait, what? Your birthday doesn't count as a holiday... well unless your birthday is on a holiday. *Laughs*"

                scene v10saow3
                with dissolve

                la "My birthday actually is a holiday, can you guess which one."

                scene v10scwl1
                with dissolve

                u "Hmmm, can I get a hint?"

                scene v10saow3
                with dissolve

                la "I feel like a hint is hard to give without giving it away. Let's see, well... it's one of the major holidays."

                scene v10scwl1
                with dissolve

                u "Kinda surprised I don't know your birthday already, but let's see, are you a Christmas baby?"

                scene v10saow3
                with dissolve

                la "Nope! Wanna keep guessing?"

                scene v10scwl1
                with dissolve

                u "New Years Baby?"

                scene v10saow3
                with dissolve

                la "Nope! I'll just tell you, my birthday is Halloween."

                scene v10scwl1
                with dissolve

                u "Wait, is Halloween a holiday?"

                scene v10saow3
                with dissolve

                la "Yeah, of course. You ever had school on Halloween? *Chuckles* What did you think it was?"

                scene v10scwl1
                with dissolve

                u "I don't know, like a day were people celebrate scary stuff and don't have to go to school because of it."

                scene v10saow3
                with dissolve

                la "Celebrating and time off, and that does not sound like a holiday to you why? *Laughs*"

                scene v10scwl1
                with dissolve

                u "*Chuckles* Huh, I guess you're right."

                scene v10scwl1
                with dissolve

                u "So Halloween. You must like horror movies and stuff."

                scene v10saow3
                with dissolve

                la "Honestly, I can't stand anything scary related and most people are surprised when they know Halloween is my birthday."

                scene v10scwl1
                with dissolve

                u "I have to admit it is a bad coincidence."

                scene v10saow3
                with dissolve

                la "Are you a big Halloween fan?"

                scene v10scwl1
                with dissolve

                u "I actually love Halloween, but I-"

        scene v10saow4b # TPP. Same camera as v10saow4. Show MC in his Ape bedroom, laying in his bed relaxing. He has the phone up to his ear, talking w' Lauren. Curious/thoughtful expression, mouth closed.
        with dissolve
        
        pause 0.75

        scene v10saow4c # TPP. Same camera as v10saow4. Show MC in his Ape bedroom, laying in his bed relaxing. He puts the phone aside and gets up from his bed. Curious expression, mouth closed.
        with dissolve
        
        pause 0.75

        scene v10saow4e # TPP. Same camera as v10saow1. Show MC in his Ape bedroom, standing by his bed with his phone up to his ear (talking with Lauren). Normal expression, mouth open.
        with dissolve

        u "Hey Lauren, mind giving me just a sec?"

        scene v10saow4d # TPP. Same camera as v10saow4. Show MC in his Ape bedroom, standing by his bed with his phone up to his ear (talking with Lauren). Normal expression, mouth closed.
        with dissolve

        la "Yeah sure!"

        scene v10saow5 # FPP. MC is looking out the window. Show Aubrey outside, smiling, mouth closed.(apes)
        with dissolve

        u "Hey What's up? Also, did you just throw a pebble at my window? *Chuckles*"

        scene v10saow5a # FPP. Same camera as v10saow5. MC is looking out the window. Show Aubrey outside in gym clothes, smiling, mouth open.(apes)
        with dissolve

        au "That must have been the wind. I'm just on my way home from the gym."

        if aubrey.relationship.value >= Relationship.FWB.value: # RCS - MC is in a relationship with Aubrey
            scene v10saow5a
            with dissolve

            au "I'm gonna have the house all to myself since none of the girls are home. You wanna come over?"

            scene v10saow5
            with dissolve

            menu:
                "Walk her home":
                    scene v10saow5
                    with dissolve

                    u "Hell yeah, I'll be down in a second."

                    scene v10scwl1b
                    with fade

                    u "Hey Lauren..."

                    scene v10scwl1c
                    with dissolve

                    la "There you are, something wrong?"

                    scene v10scwl1b
                    with dissolve

                    u "No nothing's wrong, but I have to go. Apparently there's some frat thing coming up they wanna prep us for."

                    scene v10scwl1c
                    with dissolve

                    la "Oh okay... no problem, I'll talk to you soon."

                    scene v10scwl1b
                    with dissolve

                    u "Bye Bye."

                    jump v10_aubrey_house
                
                "Don't walk her home": # RCS - there was nothing for this so I just used the stuff from no relationship w/ Aubrey branch
                    scene v10saow5
                    with dissolve

                    u "I'd love to, but I'm busy right now, sorry."

                    scene v10saow5a
                    with dissolve

                    au "Oh okay, guess I'll see you around then."

                    scene v10saow5
                    with dissolve

                    u "See ya!"

                    scene v10scwl1
                    with fade

                    u "Hey Lauren!"

                    scene v10saow3
                    with dissolve

                    la "There you are? Everything okay?"

                    scene v10scwl1
                    with dissolve

                    u "Yeah everything's fine, had a bird at my window. *Laughs*"

                    scene v10saow3
                    with dissolve

                    la "A bird took you that long? What'd you do, sing to it? *Laughs*"

                    scene v10scwl1
                    with dissolve

                    u "Something like that."

        else: # RCS - MC is not in a relationship with Aubrey
            scene v10saow5a
            with dissolve

            au "It's kind of a long walk, wanna go with me and hang out?"

            menu:
                "Walk her home":
                    scene v10saow5
                    with dissolve

                    u "Yeah sure, I'll be right down."

                    scene v10saow4d
                    with dissolve

                    pause 0.5
                    
                    scene v10scwl1b
                    with fade

                    u "Hey Lauren..."

                    scene v10scwl1c
                    with dissolve

                    la "There you are, something wrong?"

                    scene v10scwl1b
                    with dissolve

                    u "No nothing's wrong, but I have to go. Something came up."

                    scene v10scwl1c
                    with dissolve

                    la "Oh okay... no problem, I'll talk to you soon."

                    scene v10scwl1b
                    with dissolve

                    u "Later."

                    jump v10_aubrey_house
            
                "Don't walk her home":
                    scene v10saow5
                    with dissolve

                    u "I'd love to, but I'm busy right now, sorry."

                    scene v10saow5a
                    with dissolve

                    au "Oh okay, guess I'll see you around then."

                    scene v10saow5
                    with dissolve

                    u "See ya!"

                    scene v10scwl1
                    with fade

                    u "Hey Lauren!"

                    scene v10saow3
                    with dissolve

                    la "There you are? Everything okay?"

                    scene v10scwl1
                    with dissolve

                    u "Yeah everything's fine, had a bird at my window. *Laughs*"

                    scene v10saow3
                    with dissolve

                    la "A bird took you that long? What'd you do, sing to it? *Laughs*"

                    scene v10scwl1
                    with dissolve

                    u "Something like that."

    stop music fadeout 3

    jump v10_call_with_lauren2 # scene 18 for mc who didn't leave with aubrey