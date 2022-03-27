# SCENE 71: Penelope & Mc dog sitting
# Locations:  Dean's Office
# Characters: PENELOPE (Outfit: 1), MC (Outfit: 5), DEAN (Outfit: 1)
# Time: Friday Morning


label v16s71: ### ERROR: 71) Penelope dog sits for the dean

    # -Penelope enters first with MC following. The Dean is standing by her desk. Oscar is one side of the room, sitting on a dog bed/comfy blanket. Next to his bed is a bowl of water, and a food bowl (currently empty)-
    scene v16s71_1    # TPP Penelope(smile, mouth closed) walkining into the Dean's office with MC (smile, mouth closed) following behind her. 
    with dissolve

    pause 0.75

    scene v16s71_1a   # FPP Dean (smile, mouth closed) standing in front of her desk looking at the other side of the room (not at MC or Penelope).
    with dissolve

    pause 0.75 

    scene v16s71_1b   # FPP Oscar (the dog) on the other side of the room, sitting on his dog bed/blanket. Next to him is a bowl of water and an empty food bowl.
    with dissolve

    pause 0.75

    scene v16s71_2    # FPP Penelope (smiling, mouth open) looking at the Dean (smiling, mouth closed) who is looking at Penelope.
    with dissolve

    pe "Good morning, Dean Harrison."

    scene v16s71_2b   # FPP Penelope (smiling, mouth closed) looking at Dean (smiling. mouth closed) who is looking at MC.
    with dissolve

    u "Hi, Dean Harrison."

    scene v16s71_2a   # FPP Penelope(smiling, mouth closed) looking at Dean (smiling. mouth open) who is looking at Penelope.
    with dissolve

    de "Good morning. I appreciate you being on time."

    scene v16s71_2
    with dissolve

    pe "No problem."

    scene v16s71_2a
    with dissolve

    de "Everything you'll need is right here. I also bought some new toys for Oscar to play with."
    
    # -On the coffee table is a basket full of dog food and toys -
    scene v16s71_3    # TPP Close up of a basket full of various dog toys sitting somewhere in the Dean's office relatively close to Oscar.
    with dissolve    

    de "I need to leave for my meeting now, so."

    scene v16s71_2a
    with dissolve

    de "Thanks again for helping. I'll be back in an hour or so."

    scene v16s71_2
    with dissolve

    pe "Got it."

    scene v16s71_2a
    with dissolve

    de "Oh, and please feed him before I come back."

    de "If he doesn't eat once an hour, he'll take matters into his own hands... *Sighs*"

    scene v16s71_3
    with dissolve

    u "(Same.)"

    scene v16s71_2a
    with dissolve

    pe "Haha, okay. No worries."

    # -The Dean bends down to stroke Oscar; the dean only smiles when interacting with Oscar-

    scene v16s71_3a   # FPP Dean (smiling, mouth open) bends down and pets Oscar's head (still sitting on his bed/blanket). 
    with dissolve

    de "Okay, Oscar. Be a good boy for Penelope and I'll give you an extra sausage for dinner."

    u "(Haha, it's so weird seeing the Dean like this.)"

    # -The Dean exits-

    scene v16s71_4    # FPP The Dean exiting through her office door (back to camera). 
    with dissolve

    # -Penelope strokes Oscar-

    scene v16s71_3b   # FPP Penelope (smiling, mouth open) petting Oscar's head (still setting on his bed/blanket). 
    with dissolve

    pe "Hello, Oscar. Pleased to meet you."

    # -Penelope sits down in the Dean's chair-
    scene v16s71_5    # FPP Penelope (smiling, mouth closed) walking towards the Dean's desk. 
    with dissolve

    pause 0.75

    scene v16s71_5a   # FPP Penelope (smiling, mouth closed) walking around the desk toward the Dean's chair
    with dissolve

    pause 0.75

    scene v16s71_5b   # FPP Penelope (smiling, mouth closed) sitting in the Dean's chair looking at MC (OC is standing in front of the desk)
    with dissolve

    u "*Laughs* Comfortable?"

    scene v16s71_5c   # FPP Penelope (smiling, mouth open) sitting in the Dean's chair looking at Mc (OC is standing in front of the desk)
    with dissolve

    pe "Yeah, I could get used to this!"

    scene v16s71_5b
    with dissolve

    u "Dean Penelope at work."

    scene v16s71_5c
    with dissolve

    pe "*Laughs* Maybe one day I'll be running this place."

    scene v16s71_5b
    with dissolve

    u "You've been in that chair for two seconds and the power has already gone to your head."

    scene v16s71_5c
    with dissolve

    pe "Don't talk to your dean like that. Show me some respect!"

    scene v16s71_5b
    with dissolve

    u "*Laughs* Wow, you're worse than Harrison!"

    scene v16s71_5c
    with dissolve

    pe "*Laughs*"

    # -MC sits down on a chair, opposite side of desk to Penelope-
    
    scene v16s71_6    # TPP MC (smiling, mouth open) sitting in a chair in front of the Dean's desk looking at Penelope(smiling, mouth closed) sitting in the Dean's chair who looks at MC.
    with dissolve

    u "So, how did you get roped into this anyway?"

    scene v16s71_6a   # FPP Penelope (smiling, mouth open) sitting in the Dean's chair looking at MC (OC is sitting in front of the desk)
    with dissolve

    pe "Well, I ran into her when she was coming in one day, and she had Oscar."
    
    pe "She noticed that he didn't hate me, I guess, and asked if I could stop by sometimes to check on him."

    scene v16s71_6b   # FPP Penelope (smiling, mouth closed) sitting in the Dean's chair looking at MC (OC is standing in front of the desk)
    with dissolve

    u "And you said yes?"

    scene v16s71_6a
    with dissolve

    pe "I couldn't just say no! It's best to stay in her good books, isn't it?"

    scene v16s71_6b
    with dissolve

    u "Yeah, you're right. Happy Dean, happy life."
    
    # -if MC spent last night at Penelope's
    # This is the same condition used in s68 to branch to s69 (spend night with penelope) s68:206
    if penelope.relationship == Relationship.LOYAL and 0x20 & v16s27_mc_baby_duty_night != 0x20:

        scene v16s71_6a
        with dissolve

        pe "Haha, true. Although... What she doesn't know, won't hurt her."

        scene v16s71_6b
        with dissolve

        u "What do you mean?"

        scene v16s71_6a
        with dissolve

        pe "I mean, we didn't get the chance to do anything fun last night before we fell asleep..."

        scene v16s71_6b
        with dissolve

        u "Hmm, I suppose you're right."

        scene v16s71_6a
        with dissolve

        pe "So, let's do something here."

        scene v16s71_6b
        with dissolve

        u "In the Dean's office?"

        scene v16s71_6a
        with dissolve

        pe "Maybe even on her desk...?"

        scene v16s71_6b
        with dissolve

        u "With Oscar here?"

        scene v16s71_6a
        with dissolve

        pe "I don't care if you don't."

        scene v16s71_6b
        with dissolve

        u "Goodness me..."

        scene v16s71_6a
        with dissolve

        pe "Come give your dean a kiss, [name]."
        
        # -MC chooses event1 or event2
        # -event1 Kiss her
        # -event2 Don't kiss her
        menu: 
            "Kiss her": # -if Kiss her

                # -MC leans over the desk. Penelope leans over too. They meet in the middle, kissing-

                play sound "sounds/kiss.mp3"

                scene v16s71_7    # TPP MC (smiling, eyes closed) standing, leaning over the desk; Penelope (smiling, eyes closed) leaning over the desk kissing. 
                with dissolve

                # -Oscar gets up and walks around the room, restless-

                scene v16s71_8    # TPP Oscar, in front of his bed area, walking from the left to the right of the screen.
                with dissolve

                pause 0.75  

                scene v16s71_8a   # TPP Oscar, in front of his bed area, walking from the right to the left of hte screen.  
                with dissolve

                pause 0.75 

                scene v16s71_8
                with dissolve

                pause 0.75 

                scene v16s71_8a
                with dissolve

                pause 0.75

                scene v16s71_8b   # TPP Oscar( toungue out slightly), sitting IN FRONT of his bed looking off camera (in the direction of MC and Penelope)
                with dissolve

                pause 0.75

                # -mc looks at Oscar but Penelope is still kissing his neck
                scene v16s71_7a   # TPP MC (neutral, eyes open, mouth open) standing, leaning over the desk, head turned looking at Oscar (off camera); Penelope(smiling, eyes closed) leaning over, kissing MC's neck.
                with dissolve
                
                u "I think Oscar wants attention..."

                # -Penelope starts slipping her hands under MC's clothing

                scene v16s71_7b   # TPP MC (neutral, eyes open, mouth open) standing, leaning over the desk, head turned looking at Oscar (off camera); Penelope (smiling, eyes open, mouth closed) with her hands under MCs shirt looking at MC).
                with dissolve
                
                u "Should we play with him a little?"

                scene v16s71_7c   # TPP MC (neutral, eyes open, mouth closed) standing, leaning over the desk, head turned looking at Oscar (off camera); Penelope(smiling, horny, eyes open, mouth open) with her hands under MCs shirt looking at MC.
                with dissolve

                pe "*Panting* I think you should kiss me again."
                
                # -MC chooses event1 or event2
                # -event1 Kiss her
                # -event2 Look after Oscar
                menu:
                    "Kiss her": # -if Kiss her

                        scene v16s71_7d   # TPP MC (smiling, eyes open, mouth closed) standing, leaning over the desk, looking into Penelope's eyes; Penelope(smiling, horny, eyes open, mouth open) with her hands under MCs shirt, looking it MCs eyes.
                        with dissolve

                        u "I guess he can wait..."

                        # -MC walks around the desk to Penelope. They kiss passionately-
                        
                        scene v16s71_9    # TPP MC(smiling, mouth closed) walking around the Dean's desk to where Penelope (smiling, horny, "Fuck me" eyes, mouth closed) is looking at him.
                        with dissolve

                        pause 0.75

                        scene v16s71_9a   # TPP MC(eyes closed) standing, leaning down towards Penelope(eyes closed) looking upward toward MC, kissing passionately with a little bit of tongue showing.
                        with dissolve

                        # -Transition to Scene 71a-
                        jump v16s71a
                    
                    "Look after Oscar": # -if Look after Oscar

                        scene v16s71_7b
                        with dissolve

                        u "I want to, Penelope but-"

                        u "This seems risky."

                        u "Plus, I'm not sure how I feel about having a watcher..."

                        # -show Oscar staring at mc and penelope

                        scene v16s71_8b
                        with dissolve

                        pause 0.75

                        # -penelope stops kissing mc and get serious again
                        scene v16s71_7e   # TPP MC (neutral, eyes open, mouth closed) standing, leaning over the desk, head turned looking at Oscar (off camera); Penelope(disappointed, eyes open, mouth Open) with her hands back to herself.
                        with dissolve
                        
                        pe "*Sighs* You're right."

                        scene v16s71_3
                        with dissolve

                        u "Let's see what kind of toys he has, yeah?"

                        scene v16s71_6a
                        with dissolve

                        pe "Okay, yeah."

                        scene v16s71_6b
                        with dissolve

                        u "Besides, could you imagine if the Dean were to walk in on us in her office? On her desk? *Laughs*"

                        scene v16s71_6a
                        with dissolve

                        pe "Ha, yeah. I know..."                        

            "Don't kiss her": # -if Don't kiss her

                scene v16s71_6b
                with dissolve
                
                u "I don't think we should. What if she walks in on us?"

                scene v16s71_6a
                with dissolve

                pe "That's part of the f-"

                scene v16s71_6c   # FPP Penelope (disappointed, mouth open) sitting in the Dean's chair looking at MC (OC is sitting in front of the desk)
                with dissolve

                pe "*Sighs* Okay... I guess you're right."                

                pe "She'd murder us."

                scene v16s71_6d   # FPP Penelope (neutral, mouth closed) sitting in the Dean's chair looking at MC (OC is standing in front of the desk)
                with dissolve

                u "Instantly. And we'd both be expelled."

                scene v16s71_6a
                with dissolve

                pe "Alright, let's play with some toys instead."

                scene v16s71_
                with dissolve

    # -Regardless of if MC spent last night at Penelope's-

    # -MC and Penelope go to look in the basket of dog food and toys-
    scene v16s71_3
    with dissolve

    pe "Look at all the things she bought for him. He's spoiled already!"

    scene v16s71_3c   # TPP MC(smiling, mouth open) and Penelope(smiling, mouth closed) standing by the basket of toys, looking at Oscar(neutral) sitting in front of his bed. 
    with dissolve

    u "Hey, Oscar! Wanna play fetch?"

    scene v16s71_3d   # TPP MC(smiling, mouth closed) and Penelope(smiling, mouth closed) standing by the basket of toys, watching Oscar(excited, smiling) jump in the air in front of them.
    with dissolve

    pause 0.75

    scene v16s71_3e   # TPP MC(smiling, mouth closed) and Penelope(smiling, mouth closed) standing by the basket of toys, watching Oscar(excited, smiling) sit politely in front of them.
    with dissolve
    
    pause 0.75

    scene v16s71_3f   # FPP Penelope(smiling, mouth open) shoulders up looking at MC [location: standing by the basket of dog toys]
    with dissolve

    pe "I think that's a yes, haha."

    scene v16s71_3g
    with dissolve

    u "Alright, let's throw..."

    scene v16s71_3
    with dissolve

    # -MC chooses event1 or event2
    # -event1 Squeaky toy
    # -event2 Tennis ball
    menu:

        "Squeaky toy": # -if Squeaky toy

            # -MC throws a squeaky toy (an animal like a squirrel, if possible). Oscar pounces on it. He bites into it and throws it around, tearing the toy into pieces. MC and Penelope are a bit shocked-
            scene v16s71_10   # TPP MC and Penelope (smiling, mouth closed) stand by the basket of toys while MC throws a squeaky toy (Oscar is off camera).
            with dissolve
            
            pause 0.75

            scene v16s71_10a  # FPP Oscar running inside the Dean's office.
            with dissolve

            pause 0.75

            scene v16s71_10b  # FPP Oscar poucning on the squeaky took that sits on the floor.
            with dissolve

            pause 0.75

            scene v16s71_10c  # FPP Oscar laying down, chewing on the body of the sqeaky toy while the head and a (leg or arm) is dismembered on the floor a few centimeters away).
            with dissolve

            pause 0.75
            
            scene v16s71_10d  # TPP Close on MC and Penelope( shocked, mouth closed) waist up shot.
            with dissolve
            
            pause 0.75

            scene v16s71_3f
            with dissolve

            pe "Oh. I guess he wasn't a fan..."

            scene v16s71_3g
            with dissolve

            u "Depends on your perspective. Maybe he enjoyed it a little too much. *Laughs*"

            scene v16s71_3f
            with dissolve

            pe "Haha, that's true."
            
            pe "I better hide the evidence."

            scene v16s71_11   # FPP Penelope(smile, mouth closed) dropping the decapitated head of the squeaky toy into the Dean's trash can.
            with dissolve

            pause 0.75
            

        "Ball": # -if Tennis ball

            # -MC throws the tennis ball (can be any color). Oscar runs to it, then sits down with it, starts chewing the ball-
            scene v16s71_10e   # TPP MC and Penelope (smiling, mouth closed) stand by the basket of toys while MC throws a ball (Oscar is off camera).
            with dissolve

            pause 0.75

            scene v16s71_10a
            with dissolve

            pause 0.75

            scene v16s71_10f  # FPP Oscar laying down, chewing on the ball.
            with dissolve

            u "That's... Not how you play fetch, bud."

            scene v16s71_
            with dissolve

            # -MC retrieves the ball and throws it again. Oscar just goes to it again, sits down with it and chews at it-
            scene v16s71_10g  # TPP MC's hand reaching down and taking the ball away from Oscar who is laying down.
            with dissolve

            pause 0.75

            scene v16s71_10e
            with dissolve

            pause 0.75

            scene v16s71_10a
            with dissolve

            pause 0.75

            scene v16s71_10f
            with dissolve

            pause 0.75

            scene v16s71_3f
            with dissolve

            pe "Hmm, I don't think he knows how."

            scene v16s71_3g
            with dissolve

            u "Yeah, I guess nobody ever taught him."

            scene v16s71_3f
            with dissolve

            pe "Do you teach a dog to play fetch?"

            scene v16s71_3g
            with dissolve

            u "No idea. I just thought they did it automatically."

            scene v16s71_3f
            with dissolve

            pe "Ha. Apparently not."

            scene v16s71_3g
            with dissolve

            u "At least he seems to be enjoying himself."

            scene v16s71_3f
            with dissolve

            pe "Yeah, I guess that's enough exercise for now, haha."

    # -Regardless of dog toy-

    # -A few different shots for passage of time: MC, Penelope and Oscar in different positions around the room, stroking Oscar, sitting down with him on the couch, Penelope takes a selfie with MC and Oscar and posts it on Kiwii

    scene v16s71_12   # TPP MC and Penelope(smiling, mouths closed) sitting in the floor petting Oscar (tounge out, happy) laying down.
    with fase 

    pause 0.75

    scene v16s71_12a  # TPP Oscar sitting, licking Penelope's (eye closed, mouth closed, happy) cheek as she turns her head away from him. MC watching (smiling, mouth closed).
    with fade

    pause 0.75

    scene v16s71_12b  # TPP Penelope(smiling, mouth closed) pointing at MC(smiling, mouth closed) and Oscar (both in downward dog position, staring at each other)
    with fade

    pause 0.75

    scene v16s71_12c  # TPP Penelope(smiling, mouth closed) sitting on the couch with Oscar laying next to her, resting his head on her lap.
    with fade
    
    pause 0.75

    scene v16s71_12d  # TPP Penelope(smiling, mouth closed) sitting on the couch taking a selfie with Oscar sitting next to her.
    with fade

    pause 0.75

    #! v16s71_kiwii_post1 Description=Penelope selfie with mc and oscar  |  (PENELOPE KIWII POST? Autumn can comment)-

    $ v16s71_kiwii_post1 = KiwiiPost(penelope, "v16/v16s71_kiwii_post1.webp", "Having a fun morning with two stinky boys, hehe!", mentions=MC, numberLikes=213)
    $ kiwii_post.new_comment(autumn, "OMG! Oscar! He looks so happy <3", numberLikes=45, force_send=True)
    $ kiwii_post.new_comment(aubrey, "Where do I know that dog from???", numberLikes=24, force_send=True)
    $ kiwii_post.add_reply("From our visit to the lake! Remember that stoner guy?", numberLikes=56)
    $ kiwii_post.add_reply("What do you mean two?!", numberLikes=54)

    # -MC and Oscar are sitting on the couch. Penelope goes to the basket, looks in it-
    scene v16s71_3f
    with dissolve

    pe "I think it's time to feed him."

    scene v16s71_13   # FPP Penelope (smiling, mouth open) opens a can of dog food (with a cute dog on the label (if possible, it says beef stew flavor)-)
    with dissolve

    pe "And on today's menu, we have some delicious beef stew!"

    scene v16s71_13a  # FPP Penelope (smiling, mouth open) smelling the open can of dog food.
    with dissolve

    pe "Hmm. It smells pretty good, actually."

    scene v16s71_13b  # FPP Penelope (smiling, mouth closed) holding an open can of dog food.
    with dissolve

    u "Gonna have a taste?"

    scene v16s71_13c  # FPP Penelope (smiling, mouth open) holding an open can of dog food.
    with dissolve

    pe "Haha, no... But if I was starving and I had to eat dog food, I'd go with this brand."

    scene v16s71_13b
    with dissolve

    u "Wow, they should put that on the can. *Laughs*"

    scene v16s71_
    with dissolve

    # -Penelope smiles wider-

    scene v16s71_13d  # FPP Penelope (big Smile, mouth open) holding the open can of dog food in front of MC
    with dissolve
    
    pe "I dare you to taste it."

    scene v16s71_13e  # FPP Penelope (big Smile, mouth closed) holding the open can of dog food in front of MC
    with dissolve
    
    u "Damn, usually I never turn down a dare, but..."

    scene v16s71_13d
    with dissolve

    # -MC chooses event1 or event2
    # -event1 Taste it
    # -event2 Fuck no!
    menu:

        "Taste it": # -if Taste it

            scene v16s71_13e
            with dissolve

            u "Fine, fuck it."
            
            # -MC sticks his finger in the dog food and licks his finger-
            scene v16s71_13f  # TPP MC(neutral, mouth closed) sticks his finger in the open can of dog food that Penelope(smiling, mouth closed) holds.
            with dissolve

            pause 0.75

            scene v16s71_13g  # TPP MC(neutral, slight surprise) finger in his mouth while Penelope holds the open can of dog food.
            with dissolve

            pause 0.75

            scene v16s71_13g  # FPP Penelope (smiling, mouth open, nose crinkled as if saying "gross") holding an open can of dog food.
            with dissolve
            
            pe "Oh, ew! I can't believe you just did that! *Laughs*"

            scene v16s71_13b
            with dissolve

            u "You know what? It does taste like beef stew..."

            scene v16s71_13c
            with dissolve

            pe "You're so gross! Oh my God... *Giggles*"

            scene v16s71_13b
            with dissolve

            u "Better than the stuff they serve at the cafeteria, for damn sure."

            scene v16s71_13c
            with dissolve

            pe "*Laughs* Stop it."
            
            pe "I'd better give it to Oscar before you take another bite."

            scene v16s71_13b
            with dissolve

            u "Haha, what else is in the basket? I'll have any leftovers."

            scene v16s71_13c
            with dissolve

            pe "Ugh... I'm starting to regret letting you taste it."

            scene v16s71_13b
            with dissolve

            u "Letting me? You dared me!"

            scene v16s71_13c
            with dissolve

            pe "You could have said no!"

            scene v16s71_13b
            with dissolve

            u "Say no to a dare? I have too much honor for that."

            scene v16s71_
            with dissolve

        "Fuck no": # -if Fuck no!

            scene v16s71_13b
            with dissolve

            u "Fuck no!"

            scene v16s71_13c
            with dissolve

            pe "Aw, come on! Just a tiny bite. *Chuckles*"

            scene v16s71_13b
            with dissolve

            u "Never in a million years, thanks."

            scene v16s71_13c
            with dissolve

            pe "*Laughs* Fine, it's probably for the best."

            scene v16s71_13b
            with dissolve

            u "If you try it first, then maybe I'll consider it."

            scene v16s71_13c
            with dissolve

            pe "Yeah, right! I'm not falling for that one."

            scene v16s71_13b
            with dissolve

            u "Haha, worth a try."

    # -Regardless of tasting dog food or not-

    # -Penelope tips out the contents of the can into Oscar's food bowl. Oscar jumps off the couch, goes to the food and eats it up quick-
    scene v16s71_14   # FPP Penelope(neutral, mouth closed) squats by Oscar's food bowl holding the open can of dog food over the "empty" bowl.
    with dissolve

    pause 0.75

    scene v16s71_14a  # FPP Penelope(neutral, mouth closed) squats by Oscar's food bowl turns the open can of dog food upside down over the bowl. The dog bowl now has food in it. 
    with dissolve

    pause 0.75

    scene v16s71_14b  # FPP Penelope (neutral, mouth open) squats by Oscar's food bowl and watches Oscar eat his food (she no longer has the can of food)
    with dissolve

    pe "Wow, hungry boy!"

    scene v16s71_14c  # FPP Penelope(neutral, mouth closed) squats by Oscar's food bowl and watches Oscar eat his food. 
    with fade

    pause 0.75

    scene v16s71_14d  # FPP Penelope(neutral, mouth closed) squats by Oscar's empty food bowl [Oscar off camera])
    with dissolve

    pause 0.75

    # -After eating Oscar goes to his bed and settles down for a nap-
    scene v16s71_12d  # FPP Oscar curled up sleeping in middle of the couch.
    with dissolve

    u "And now it's time for a nap. *Sighs*I wish I could just play, eat, and sleep all day."

    scene v16s71_3f
    with dissolve

    pe "Haha, yeah. He's got it easy now that he's found a good owner."

    scene v16s71_3g
    with dissolve

    u "He deserves it."

    # -Penelope returns to MC, sitting next to him on the couch. They watch as Oscar's eyes gradually close as he falls asleep-
    scene v16s71_12e  # TPP MC(smiling, mouth closed) on one side of the couch, Oscar (sleeping) in the middle with his head on Penelope's (smiling, mouth closed) lap. MC and Penelope are watching Oscar sleep.
    with dissolve

    jump v16s71b

    # -Transition to Scene 71b-

