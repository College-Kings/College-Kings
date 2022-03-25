# SCENE 61: Transition Mc studies
# Locations: Apes Dorm Room, Wolf Dorm Room
# Characters: MC (Outfit: 2), CHLOE (Outfit: 1), [BABY_NAME] (Outfit: 1)
# Time: Thursday Afternoon

label v16s61:
    if joinwolves:
        play sound "sounds/dooropen.mp3"
        
        scene v16s61_1 # TPP. Show MC (slight smile, mouth closed) walking into his wolves room.
        with fade

        pause 0.75

        play sound "sounds/doorclose.mp3"

        scene v16s61_2 # TPP. In wolves room. Show MC (slight smile, mouth closed) sitting on his bed.
        with dissolve

        pause 0.75

        # -if Transitioning directly from Scene 56 (Wolves 2)
        if not v14_help_lindsey:
            scene v16s61_2
            with dissolve 

            u "*Sighs* (What are we going to do about Chris and Imre? I feel like this whole house could use some anger management training.)"
        
        # -if Succeeded with Polly at hotel
        if v16s59_polly_endorse_lindsey: #placeholder
            scene v16s61_2
            with dissolve

            u "(I can't believe we managed to get Polly on board with our crazy idea! Lindsey loves her more than ever now, haha.)"

        else: 
            scene v16s61_2
            with dissolve

            u "(Well, that was embarrassing...)"

            # -if also wore room service uniforms
            if v16s28_lindsey_pb_pretend_roomservice: # placeholder
                play sound "sounds/vibrate.mp3"
                
                scene v16s61_2a # TPP. In wolves room. Show MC (slight smile, mouth closed) sitting on his bed pulling out his phone from his pocket
                with dissolve 

                pause 0.75 
                
                scene v16s61_2b # TPP In wolves room. Show MC (slight smile, mouth closed) sitting on his bed looking at his phone.
                with dissolve 

                u "(It was nice of the bodyguard to let us change out of those uniforms first, but did he really have to pick Lindsey up again? I swear he did it just for the photos! What a prick.)"

                #! v16s61kw_1 MC and Lindsey (both regular clothes) with Polly's bodyguard at the exit of the hotel, Lindsey being carried out over his shoulder

                ###check force send
                $ v16s61_kiwiiPost1 = KiwiiPost(chloe, "v16/v16s61_chlpost1.webp", "Umm... Is this you, Lindsey? LOL #FuturePresident?", mentions=lindsey, numberLikes=645)
                $ v16s61_kiwiiPost1.newComment(aubrey, "Wait, what the hell? And [name]?", numberLikes=51, force_send=True)
                $ v16s61_kiwiiPost1.newComment(penelope, "Wait... Is that Polly's security guard?! What happened???", numberLikes=95, force_send=True)
                $ v16s61_kiwiiPost1.addReply("Just fooling around! Ha...", numberLikes=42)
                $ v16s61_kiwiiPost1.addReply("Uh, Lindsey will tell you. Right, Linds?", mentions=lindsey, numberLikes=46)
                $ v16s61_kiwiiPost1.newComment(lindsey, "Oh! I can't believe there was paparazzi! We were just having some fun :)", numberLikes=54, force_send=True)
                $ v16s61_kiwiiPost1.newComment(ryan, "He doesn't look very excited...", numberLikes=78, force_send=True)
               
                if False:
                    scene v16s61_chlpost1
                    with dissolve
               
                $ set_presidency_percent(v14_lindsey_popularity - 3)
                
                scene v16s61_2b
                with dissolve 

                u "(Paparazzi?! What the fuck...)"
        
        # -if helping Chloe with Spa evening
        if not v16s12_chloe_planboard_decide_newspaper_cover:
            scene v16s61_2 
            with dissolve

            u "(I've still got some time before I need to help Chloe with this spa thing. Definitely excited for that!)"
            
            # -if chose to be the masseuse on planning board
            if v16s12_chloe_planboard_decide_mc_gives_massages:
                scene v16s61_2
                with dissolve

                u "(Especially the massages...)"

        scene v16s61_2
        with dissolve

        u "(Hmm, what should I do with my free time?)"

        u "(I guess I should take the opportunity to study a little. I am here to learn after all... Ugh.)"

        scene v16s61_3 # TPP. In wolves room. Close up of MC(slight smile, mouth closed) sitting at his study desk
        with dissolve

        pause 0.75

        scene v16s61_4 # TPP. In wolves room. Close up of MC(slight smile, mouth closed) reading a book at his study desk
        with dissolve

        pause 0.75

        scene v16s61_5 # TPP. In wolves room. Close up of MC(bored, mouth closed) writing in a notepad.
        with dissolve

        pause 0.75

        scene v16s61_4
        with dissolve

        pause 0.75
        
        scene v16s61_6 # TPP. In wolves room. Close up of MC(bored, mouth closed) looking like he is falling asleep at his desk.
        with dissolve

        pause 0.75

        if v14_help_chloe and not v16s12_chloe_planboard_decide_newspaper_cover:
            scene v16s61_6
            with dissolve

            u "(I can't take this anymore... What time is it?)"

            scene v16s61_7 # TPP. In wolves room. Close up of MC (slight smile, mouth closed.) looking at his phone while he sits at the study desk.
            with dissolve

            u "(Nice! Time to go hang out with some half-naked ladies. Woohoo!)"

            jump v16s62

        elif not v14_help_chloe: # -if not helping Chloe with her campaign
            play sound "sounds/vibrate.mp3"

            scene v16s61_7
            with dissolve

            pause 0.75

            scene v16s61_8 # TPP. In wolves room. MC (slight smile, mouth open) standing up from his chair and holding his phone to his ear.
            with dissolve

            u "Hello, my Chlo. *Chuckles* How are you?"

            # -You can show a couple of images, 2-3 max, of Chloe during this convo. I suggest that she's preparing the house and party supplies during the call (These images are not a priority and can be cut if needed, otherwise mc is just shown pacing his room during the call.)
            # -if ChloeGf 
            if chloe.relationship >= Relationship.GIRLFRIEND:
                scene v16s61_9 # TPP. Shot of Chloe(slight smile, mouth open) at the chicks house holding her phone to her ear. The house looks almost ready for the party
                with dissolve 

                cl "Hey you! I need some help."
            
            else:
                scene v16s61_9
                with dissolve

                cl "Hey, [name]! I'm fine, thanks I need some help, though."

            scene v16s61_9a # TPP. Shot of Chloe(slight smile, mouth closed.) at the chicks house holding her phone to her ear. The house looks almost ready for the party
            with dissolve

            u "Don't we all? *Laughs*"

            scene v16s61_9
            with dissolve

            cl "Ha. To be honest I don't know why I'm even asking, I think I already know what your answer is going to be."

            scene v16s61_9a
            with dissolve

            u "Oh yeah? Test me, what's up?"

            scene v16s61_9
            with dissolve

            cl "I'm doing a spa night at the house for a few of the girls. Trying to raise morale I guess you could say."

            scene v16s61_9a
            with dissolve

            u "Mmmkay... Continue..."

            scene v16s61_9
            with dissolve

            cl "I've still got time to book a masseuse, but I thought I'd check to see if you would volunteer first. I'd be saving a lot of money, too."

            scene v16s61_9a
            with dissolve

            u "You're asking me to be a masseuse for the evening? Without pay?"

            scene v16s61_9
            with dissolve

            cl "Yes... Please? You're invited regardless, because we might need some help with face masks and stuff, but..."

            cl "Would you please, please, please be our masseuse for the night?"

            scene v16s61_9a
            with dissolve

            u "Hm... Well, I have no plans so I can come."

            scene v16s61_9
            with dissolve

            cl "Great!"

            scene v16s61_9a
            with dissolve

            u "(But do I want to massage a few girls, or help with normal stuff all night?)"

            scene v16s61_8
            with dissolve

            menu:
                "Be the masseuse":
                    $ v16s61_chloe_pb_override_mc_gives_massages = True
                    $ add_Point(KCT.TROUBLEMAKER)

                    scene v16s61_9a
                    with dissolve

                    u "And honestly, it sounds like a job I was born for."

                    scene v16s61_9
                    with dissolve

                    cl "Haha, thank you!"

                    scene v16s61_9a
                    with dissolve

                    u "When is it?"

                    scene v16s61_9
                    with dissolve

                    cl "Just come to the Chicks house now if you can."

                    scene v16s61_9a
                    with dissolve

                    u "Haha, okay. I'm warming my hands up as we speak!"

                    scene v16s61_9
                    with dissolve

                    cl "*Laughs* Terrific."

                "Be a helper":
                    $ add_Point(KCT.BRO)

                    scene v16s61_9a
                    with dissolve

                    u "I don't really have much experience in massaging, so maybe you should hire a professional. *Laughs*"

                    scene v16s61_9
                    with dissolve

                    cl "Okay, yeah. That would probably be best. Then you can just hangout and assist with other things."

                    scene v16s61_9a
                    with dissolve

                    u "Okay, like what?"

                    scene v16s61_9
                    with dissolve

                    cl "Oh, I'll just tell you when you get here."

                    scene v16s61_9a
                    with dissolve

                    u "When am I coming?"

                    scene v16s61_9
                    with dissolve

                    cl "Now?"

                    scene v16s61_9a
                    with dissolve

                    u "Oh. Right. Coming!"

            scene v16s61_9 
            with dissolve

            cl "See you when you get here!"

            play sound "sounds/rejectcall.mp3"

            scene v16s61_8
            with dissolve

            pause 0.75 

            play sound "sounds/dooropen.mp3"

            scene v16s61_10 # TPP. Show MC(slight smile,mouth closed) leaving his wolves room.
            with dissolve 

            pause 0.75

            jump v16s62

        else:             
            play sound "sounds/thud.mp3"

            scene v16s61_6a # TPP. Show MC fallen asleep his head hitting the book on his desk.
            with vpunch 

            pause 0.75

            scene black
            with dissolve

            pause 0.75

            # -Fade to a nightmare. A black void all around MC. He looks confused for a moment. He turns to see a huge baby, standing up, towering over him (like the big baby from Spirited Away). It's five times the size of MC-

            scene v16s61_11 # TPP. Show MC(confused,mouth closed) standing in a black void nightmare and looking around.
            with fade 

            pause 0.75 

            scene v16s61_11a # TPP. Show MC(Jaw dropped) looking behind him we don't see whats behind him yet.
            with dissolve 
            
            pause 0.75 

            scene v16s61_12 # TPP. Shot from a bit behind MC of him looking up at a gigantic baby(Angry, mouth closed.) that is towering over him. The Babys eyes locked onto MC
            with dissolve

            u "(Oh, fuck. That's a big ass baby!)"

            scene v16s61_12a # TPP. Shot from a bit behind MC of him looking up at a gigantic baby(Angry, mouth open) that is towering over him. The babys eyes locked onto MC.
            with dissolve 

            baby "ME... HUNGRY..."
            
            scene v16s61_12b # TPP. Shot from a bit behind MC of him looking up at the gigantic baby(angry, mouth closed) reaching to grab MC.
            with dissolve

            u "(Huh? What the hell is happening?)"

            scene v16s61_12c # TPP. Shot from a bit behind MC of him looking up at the gigantic baby(angry, mouth open) reaching to grab MC.
            with dissolve

            baby "ME... KILL..."

            scene v16s61_12b
            with dissolve

            u "(You what?! Hell no!)"

            scene v16s61_13 # TPP. Shot from infront of MC(worried, mouth closed.) MC running towards the Camera as the baby(Angry, mouth open) is chasing him.
            with vpunch

            baby "ME... EAT..."

            scene v16s61_13a # TPP. Shot from infront of MC(worried, mouth closed.) MC running towards the Camera as the baby(Angry, mouth closed) is chasing him.
            with dissolve

            u "(No! Leave me alone!)"

            scene v16s61_13
            with dissolve

            baby "GET... IN... TUM TUM!!!"

            scene v16s61_13a
            with dissolve

            u "(Noooooooooooo! AGHHHH-)"

            scene v16s61_6b # TPP. Show MC with his head on the book opening his eyes.
            with vpunch

            u "(Huh? Whoa, what the actual fuck? Why is [v16_baby_name] invading my dreams? I need to get my head straight...)"

            scene v16s61_7
            with dissolve

            u "(Oh, shit. I better hurry before I miss Polly's performance!)"

            play sound "sounds/dooropen.mp3"

            scene v16s61_10
            with dissolve

            pause 0.75

            jump v16s66 
    else:
        play sound "sounds/dooropen.mp3"
        
        scene v16s61_14 # TPP. Show MC (slight smile, mouth closed) walking into his apes room.
        with fade

        pause 0.75

        play sound "sounds/doorclose.mp3"

        scene v16s61_15 # TPP. In apes room. Show MC (slight smile, mouth closed) sitting on his bed.
        with dissolve

        pause 0.75

        # -if Transitioning directly from Scene 57 (Apes 2)
        if not v14_help_lindsey:
            scene v16s61_15
            with dissolve

            u "*Sighs* (This whole Sam thing is forcing everyone to choose sides. Whichever way you slice it, it's not good for the frat.)"
        
        else:
            # -if Succeeded with Polly at hotel
            if v16s59_polly_endorse_lindsey:
                scene v16s61_15
                with dissolve

                u "(I can't believe we managed to get Polly on board with our crazy idea! Lindsey loves her more than ever now, haha.)"

            else: 
                scene v16s61_15
                with dissolve

                u "(Well, that was embarrassing...)"

                # -if also wore room service uniforms
                if v16s28_lindsey_pb_pretend_roomservice:
                    play sound "sounds/vibrate.mp3"
                    
                    scene v16s61_15a # TPP. In apes room. Show MC (slight smile, mouth closed) sitting on his bed pulling out his phone from his pocket
                    with dissolve 

                    pause 0.75 
                    
                    scene v16s61_15b # TPP In apes room. Show MC (slight smile, mouth closed) sitting on his bed looking at his phone.
                    with dissolve 

                    u "(It was nice of the bodyguard to let us change out of those uniforms first, but did he really have to pick Lindsey up again? I swear he did it just for the photos! What a prick.)"
                    
                    $ v16s61_kiwiiPost2 = KiwiiPost(chloe, "v16/v16s61_chlpost2.webp", "Umm... Is this you, Lindsey? LOL #FuturePresident?", mentions=lindsey, numberLikes=645)
                    $ v16s61_kiwiiPost2.newComment(aubrey, "Wait, what the hell? And [name]?", numberLikes=51, force_send=True)
                    $ v16s61_kiwiiPost2.newComment(penelope, "Wait... Is that Polly's security guard?! What happened???", numberLikes=95, force_send=True)
                    $ v16s61_kiwiiPost2.addReply("Just fooling around! Ha...", numberLikes=42)
                    $ v16s61_kiwiiPost2.addReply("Uh, Lindsey will tell you. Right, Linds?", mentions=lindsey, numberLikes=46)
                    $ v16s61_kiwiiPost2.newComment(lindsey, "Oh! I can't believe there was paparazzi! We were just having some fun :)", force_send=True)
                    $ v16s61_kiwiiPost2.newComment(ryan, "He doesn't look very excited...", numberLikes=78, force_send=True)
                
                    if False: #For Lint
                        scene v16s61_chlpost2
                        with dissolve
                
                    $ set_presidency_percent(v14_lindsey_popularity - 3)
                    
                    scene v16s61_15b
                    with dissolve 

                    u "(Paparazzi?! What the fuck...)"
        
        # -if helping Chloe with Spa evening
        if not v16s12_chloe_planboard_decide_newspaper_cover:
            scene v16s61_15 
            with dissolve

            u "(I've still got some time before I need to help Chloe with this spa thing. Definitely excited for that!)"
            
            # -if chose to be the masseuse on planning board
            if v16s12_chloe_planboard_decide_mc_gives_massages:
                scene v16s61_15
                with dissolve

                u "(Especially the massages...)"

        scene v16s61_15
        with dissolve

        u "(Hmm, what should I do with my free time?)"

        u "(I guess I should take the opportunity to study a little. I am here to learn after all... Ugh.)"

        scene v16s61_16 # TPP. In apes room. Close up of MC(slight smile, mouth closed) sitting at his study desk
        with dissolve

        pause 0.75

        scene v16s61_17 # TPP. In apes room. Close up of MC(slight smile, mouth closed) reading a book at his study desk
        with dissolve

        pause 0.75

        scene v16s61_18 # TPP. In apes room. Close up of MC(bored, mouth closed) writing in a notepad.
        with dissolve

        pause 0.75

        scene v16s61_17
        with dissolve

        pause 0.75
        
        scene v16s61_19 # TPP. In apes room. Close up of MC(bored, mouth closed) looking like he is falling asleep at his desk.
        with dissolve

        pause 0.75

        if v14_help_chloe and not v16s12_chloe_planboard_decide_newspaper_cover:
            scene v16s61_19
            with dissolve

            u "(I can't take this anymore... What time is it?)"

            scene v16s61_20 # TPP. In apes room. Close up of MC (slight smile, mouth closed.) looking at his phone while he sits at the study desk.
            with dissolve

            u "(Nice! Time to go hang out with some half-naked ladies. Woohoo!)"

            jump v16s62
        
        elif not v14_help_chloe: # -if not helping Chloe with her campaign
            play sound "sounds/vibrate.mp3"

            scene v16s61_20
            with dissolve

            pause 0.75

            scene v16s61_21 # TPP. In apes room. MC (slight smile, mouth open) standing up from his chair and holding his phone to his ear.
            with dissolve

            u "Hello, my Chlo. *Chuckles* How are you?"

            # -You can show a couple of images, 2-3 max, of Chloe during this convo. I suggest that she's preparing the house and party supplies during the call (These images are not a priority and can be cut if needed, otherwise mc is just shown pacing his room during the call.)
            # -if ChloeGf 
            if chloe.relationship >= Relationship.GIRLFRIEND: 
                scene v16s61_9 
                with dissolve 

                cl "Hey you! I need some help."

            else:
                scene v16s61_9
                with dissolve

                cl "Hey, [name]! I'm fine, thanks I need some help, though."

            scene v16s61_9a 
            with dissolve

            u "Don't we all? *Laughs*"

            scene v16s61_9
            with dissolve

            cl "Ha. To be honest I don't know why I'm even asking, I think I already know what your answer is going to be."

            scene v16s61_9a
            with dissolve

            u "Oh yeah? Test me, what's up?"

            scene v16s61_9
            with dissolve

            cl "I'm doing a spa night at the house for a few of the girls. Trying to raise morale I guess you could say."

            scene v16s61_9a
            with dissolve

            u "Mmmkay... Continue..."

            scene v16s61_9
            with dissolve

            cl "I've still got time to book a masseuse, but I thought I'd check to see if you would volunteer first. I'd be saving a lot of money, too."

            scene v16s61_9a
            with dissolve

            u "You're asking me to be a masseuse for the evening? Without pay?"

            scene v16s61_9
            with dissolve

            cl "Yes... Please? You're invited regardless, because we might need some help with face masks and stuff, but..."

            cl "Would you please, please, please be our masseuse for the night?"

            scene v16s61_9a
            with dissolve

            u "Hm... Well, I have no plans so I can come."

            scene v16s61_9
            with dissolve

            cl "Great!"

            scene v16s61_9a
            with dissolve

            u "(But do I want to massage a few girls, or help with normal stuff all night?)"

            scene v16s61_21
            with dissolve

            menu:
                "Be the masseuse":
                    $ v16s61_chloe_pb_override_mc_gives_massages = True
                    $ add_Point(KCT.TROUBLEMAKER)

                    scene v16s61_9a
                    with dissolve

                    u "And honestly, it sounds like a job I was born for."

                    scene v16s61_9
                    with dissolve

                    cl "Haha, thank you!"

                    scene v16s61_9a
                    with dissolve

                    u "When is it?"

                    scene v16s61_9
                    with dissolve

                    cl "Just come to the Chicks house now if you can."

                    scene v16s61_9a
                    with dissolve

                    u "Haha, okay. I'm warming my hands up as we speak!"

                    scene v16s61_9
                    with dissolve

                    cl "*Laughs* Terrific."

                "Be a helper":
                    $ add_Point(KCT.BRO)

                    scene v16s61_9a
                    with dissolve

                    u "I don't really have much experience in massaging, so maybe you should hire a professional. *Laughs*"

                    scene v16s61_9
                    with dissolve

                    cl "Okay, yeah. That would probably be best. Then you can just hangout and assist with other things."

                    scene v16s61_9a
                    with dissolve

                    u "Okay, like what?"

                    scene v16s61_9
                    with dissolve

                    cl "Oh, I'll just tell you when you get here."

                    scene v16s61_9a
                    with dissolve

                    u "When am I coming?"

                    scene v16s61_9
                    with dissolve

                    cl "Now?"

                    scene v16s61_9a
                    with dissolve

                    u "Oh. Right. Coming!"

            scene v16s61_9 
            with dissolve

            cl "See you when you get here!"

            play sound "sounds/rejectcall.mp3"

            scene v16s61_21
            with dissolve

            pause 0.75 

            play sound "sounds/dooropen.mp3"

            scene v16s61_22 # TPP. Show MC(slight smile,mouth closed) leaving his apes room.
            with dissolve 

            pause 0.75

            jump v16s62

        else: 
            play sound "sounds/thud.mp3"

            scene v16s61_19a # TPP. Show MC fallen asleep his head hitting the book on his desk.
            with vpunch 

            pause 0.75 

            scene black
            with dissolve

            pause 0.75

            # -Fade to a nightmare. A black void all around MC. He looks confused for a moment. He turns to see a huge baby, standing up, towering over him (like the big baby from Spirited Away). It's five times the size of MC-

            scene v16s61_11 # TPP. Show MC(confused,mouth closed) standing in a black void nightmare and looking around.
            with fade

            pause 0.75 

            scene v16s61_11a # TPP. Show MC(Jaw dropped) looking behind him we don't see whats behind him yet.
            with dissolve 
            
            pause 0.75 

            scene v16s61_12 # TPP. Shot from a bit behind MC of him looking up at a gigantic baby(Angry, mouth closed.) that is towering over him. The Babys eyes locked onto MC
            with dissolve

            u "(Oh, fuck. That's a big ass baby!)"

            scene v16s61_12a # TPP. Shot from a bit behind MC of him looking up at a gigantic baby(Angry, mouth open) that is towering over him. The babys eyes locked onto MC.
            with dissolve 

            baby "ME... HUNGRY..."
            
            scene v16s61_12b # TPP. Shot from a bit behind MC of him looking up at the gigantic baby(angry, mouth closed) reaching to grab MC.
            with dissolve

            u "(Huh? What the hell is happening?)"

            scene v16s61_12c # TPP. Shot from a bit behind MC of him looking up at the gigantic baby(angry, mouth open) reaching to grab MC.
            with dissolve

            baby "ME... KILL..."

            scene v16s61_12b
            with dissolve

            u "(You what?! Hell no!)"

            scene v16s61_13 # TPP. Shot from infront of MC(worried, mouth closed.) MC running towards the Camera as the baby(Angry, mouth open) is chasing him.
            with vpunch

            baby "ME... EAT..."

            scene v16s61_13a # TPP. Shot from infront of MC(worried, mouth closed.) MC running towards the Camera as the baby(Angry, mouth closed) is chasing him.
            with dissolve

            u "(No! Leave me alone!)"

            scene v16s61_13
            with dissolve

            baby "GET... IN... TUM TUM!!!"

            scene v16s61_13a
            with dissolve

            u "(Noooooooooooo! AGHHHH-)"

            scene v16s61_19b # TPP. Show MC with his head on the book opening his eyes.
            with vpunch

            u "(Huh? Whoa, what the actual fuck? Why is [v16_baby_name] invading my dreams? I need to get my head straight...)"

            scene v16s61_20
            with dissolve

            u "(Oh, shit. I better hurry before I miss Polly's performance!)"

            play sound "sounds/dooropen.mp3"

            scene v16s61_22
            with dissolve

            pause 0.75

            jump v16s66