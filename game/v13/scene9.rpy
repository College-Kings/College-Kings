# SCENE 9: Chloe Pier
# Locations: Hotel hallway; Sidewalk, Pier, Hotel Room
# Characters: CHLOE (Outfit: 2), MC (Outfit: 2), RYAN (Outfit: 1)
# Time: Afternoon

label v13s9:
    scene v13s9_1 # TPP. Hotel hallway. MC walking down the hallway, back to camera, angled to where hotel room doors are visible on MC's right.
    with dissolve

    pause 0.75

    play music "music/v13/Track Scene 9_1.mp3" fadein 2

    scene v13s9_1a # TPP. Same as v13s9_1 but MC is halfway down the hall and he last room door at the end of the hall is halfway open. 
    with dissolve

    pause 0.75

    scene v13s9_1b # TPP. Same as v12s9_1a but MC is in arms length of the now open door that shows Chloe entering the hallway (from her room).
    with dissolve

    pause 0.75

    if chloe.relationship >= Relationship.GIRLFRIEND:
        scene v13s9_2 # FPP. Chloe full face smile, happy suprised, mouth open looking at MC.
        with dissolve

        cl "Oh! Hey there handsome. Guess I won't have to go around the hotel looking for you since you're right here. *Chuckles*"

        play sound "sounds/kiss.mp3"

        scene v13s9_3 # TPP. Chloe kisses MC on the lips.
        with dissolve

        pause 0.75

    else:
        scene v13s9_2a # FPP. Same as v13s9_2 excpet Chloe is just smiling (not fulll face or happy surpised; a "friend smile"), mouth open.
        with dissolve

        cl "Oh! Hey [name]. Guess I won't have to go around the hotel looking for you since you're right here. *Chuckles*"

    scene v13s9_2b # FPP. Same as v13s9_2a but Chloe happy with mouth closed. 
    with dissolve

    u "Need me for something?"

    scene v13s9_2c # FPP. Same as v13s9_2b but Chloe with mouth open. 
    with dissolve

    cl "If you're willing to join me, yeah. I've looked for hours on my phone trying to find some nice Amsterdam stuff to do..."

    scene v13s9_2d # FPP. Same as v13s9_2c but Chloe has a slight frown. 
    with dissolve

    cl "Sadly, I didn't find much that I'd actually be interested in..."
    
    scene v13s9_2a
    with dissolve
    
    cl "...but I did find a beach."

    scene v13s9_2b
    with dissolve

    u "There's a beach here?"

    scene v13s9_2a
    with dissolve

    cl "Yeah, it's called Scheveningen Beach... But instead of swimming, we can go to the pier. Do you wanna come with me?"

    scene v13s9_2b
    with dissolve

    u "Yeah, sure. I don't have anything else to do right now, haha."

    scene v13s9_2a
    with dissolve

    cl "Yay! Okay, great. Do you need to grab anything before we go or..."

    scene v13s9_2b
    with dissolve

    u "Nope, I'm ready now if you are."

    scene v13s9_2e # FPP, Same as v13s9_2a, but with Chloe winking at MC (smiling, mouth open). 
    with dissolve

    cl "Perfect, let's go then."

    scene v13s9_2b
    with dissolve

    u "Lead the way."

    scene v13s9_4 # TPP. MC walking with Chloe, slightly in front of him, down the hallway, both smiling, mouths closed.
    with fade

    pause 0.75
    
    scene v13s9_5 # TPP. MC walking with Chloe in the hotel lobby walking towards the exit, both smiling, mouths closed.
    with dissolve

    pause 0.75

    scene v13s9_6 # TPP. Outside, MC walking with Chloe exiting the hotel, both smiling, mouths closed
    with dissolve

    pause 0.75

    scene v13s9_7 # TPP. Outside, MC walking with Chloe down a side walk, smiling, mouths closed. 
    with dissolve

    pause 0.75 

    scene v13s9_8 # TPP. Outside, MC and Chloe, together, smiling, mouths closed arrive at the pier (optional a sign with the name of the Pier)
    with dissolve

    pause 0.75

    scene v13s9_9 # TPP. Outside, MC and Chloe walk together down a long dock the extends out above the water (pier), smiling, mouths closed.
    with dissolve

    pause 0.75 

    scene v13s9_10 # TPP. MC and Chloe, at the pier, leaning against the guard rail, looking out into the water, smiling, mouths closed.
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v13/Track Scene 9_2.mp3" fadein 2

    scene v13s9_11 # FPP. MC watching Chloe lean against the guard rail, slightly looking downward at the water, neutral expression, mouth open.
    with dissolve
    
    cl "I don't know how I feel about what I'm looking at..."

    scene v13s9_11a # FPP. Same as v13s9_11 but with Chloe's mouth closed.  
    with dissolve

    u "Haha, is the feeling leaning more towards being impressed or not interested?"

    scene v13s9_11b # FPP. Same as v13s9_11 but Chloe turns her head to face MC, slight smile, mouth open. 
    with dissolve

    cl "I'm really not sure... *Chuckles*"

    scene v13s9_11c # FPP. Same as v13s9_11b but Chloe thinking (head slightly tilted to left, eyes looking up and to the right, neutral expression, mouth open, index finger on her chin). 
    with dissolve

    cl "It's kinda like the first time I had coffee. I didn't know if I liked it or not, but I kept drinking."

    scene v13s9_11d # FPP. Same as v13s9_11b but Chloe mouth closed. 
    with dissolve

    u "That's how I was when I first joined the frat."

    scene v13s9_11e # FPP  Same as v13s9_11b but Chloe slightly frowning while showing the palm of her hand to MC (like a signal to stop). 
    with dissolve

    cl "Oh no, don't get me started on Greek life right now..."

    scene v13s9_11a
    with dissolve

    u "Ha, okay. My bad."

    scene v13s9_11
    with dissolve

    cl "You're fine... Sorry. Talking about it with you doesn't really bother me actually. I need to discuss it with someone; I need to discuss a lot of things on my mind."

    scene v13s9_11b
    with dissolve

    cl "Nora and Chris, Lindsey and this whole President thing..."

    if not v12_told_chloe and not v11_told_aubrey: # -If Chloe didn't know before (extra dialog)

        scene v13s9_11f # FPP. Same as v13s9_11b but Chloe leans in closer to MC, as if she was whispering to him. 
        with dissolve
    
        cl "I don't know if you know or not, but it's pretty much public info now that she's running to become the new President of the Chicks."

    scene v13s9_11a
    with dissolve
    
    u "You've spoken to Nora?"

    scene v13s9_11
    with dissolve

    cl "I haven't, no. I know we're all open and honest and everything, but I just don't feel that it's my place. Knowing her she'd say the same thing... *Chuckles*"

    scene v13s9_11a
    with dissolve

    u "So, you're not angry about the Lindsey situation?"

    scene v13s9_11b
    with dissolve

    cl "I was, but being angry doesn't solve anything. I just need to figure out how I'm gonna win this."

    scene v13s9_11d
    with dissolve

    u "I've heard that the President has never been challenged before."

    scene v13s9_12 # FPP. Chloe changing position, she is turning around, about to lean her butt/lower back against the gaurd rail, mouth closed.
    with dissolve

    pause 0.75

    scene v13s9_12a # FPP. Chloe, looking off screen/camera, with her butt/lowerback leaning against the guard rail one leg bent with her foot flat against the fencing, elbows resting on the guard rail, slightly sad, mouth closed
    with dissolve

    pause 0.75
    
    scene v13s9_12b # FPP. Same as v13s9_v12 but Chloe's head turned facing MC, but slightly downward avoiding eye contact, sad, mouth open.
    with dissolve

    cl "Not in the history of our sorority, so one of two things must be true. Either I'm the worst President ever, or Lindsey is the most egotistical member we've had."

    scene v13s9_12c # FPP. Same as v13s9_v12b but Chloe's mouth closed.
    with dissolve

    u "I don't know if it's that black and white..."

    scene v13s9_12b
    with dissolve

    cl "Well, I know what is black and white. If I don't remain President going into next semester, I'm going to lose my scholarship."

    scene v13s9_12c
    with dissolve

    u "*Sighs* Yeah, I heard about that..."

    scene v13s9_12d # FPP. Same as v13s9_12b but Chloe looking at MC, a little surprised/shocked, mouth open.
    with dissolve

    cl "Wait, what? How'd you find out?"

    scene v13s9_12e # FPP. Same as v13s9_12b but Chloe looking at MC, neutral expression, mouth closed.
    with dissolve

    u "Believe it or not, Nora mentioned it to me."

    scene v13s9_12f # FPP. Same as v13s9_12e but Chloe mouth open.
    with dissolve

    cl "Hmm, surprising. Maybe I'll actually get a pity vote out of it."
    
    u "(That's exactly what she said.)"
    
    scene v13s9_12e
    with dissolve

    u "So... You have to be the President in order to keep this scholarship?"

    scene v13s9_12b
    with dissolve

    cl "Yep, it's literally called The Greek Presidential Scholarship."

    scene v13s9_12c
    with dissolve

    u "Well, you can't misinterpret that."

    scene v13s9_12f
    with dissolve

    cl "I'm not too worried about losing it though, I have a pretty set in stone plan. Not only that, but I'll have your help as well. Or at least, I'd hope so."
    
    scene v13s9_12g # FPP. Same as v13s9_12b but Chloe has slighty sad expression (pouting), mouth closed, looking directly at MC (sad eyes, making it difficult for MC not to want help her).
    with dissolve

    menu:
        "Help Chloe":
            $ v13_help_chloe = True
            $ chloe.points += 1
            
            u "Of course I'll help. You obviously care about the girls, you've been running the sorority perfectly fine, and I'd hate for you to lose your scholarship."

            scene v13s9_12h # FPP. Chole facing MC (no longer leaning against rail) looking at MC, happy, mouth open.
            with dissolve

            cl "I knew I could count on you."

            if chloe.relationship >= Relationship.GIRLFRIEND: # -If Chloegirlfriend (extra dialog)
                $ add_point(KCT.BOYFRIEND)

                play sound "sounds/kiss.mp3"
                
                scene v13s9_13 # TPP: Chloe, facing MC (no longer leaning against rail) arms around MC, giving him a kiss.
                with dissolve

                pause 0.75

                scene v13s9_12h 
                with dissolve
                
                cl "You're honestly the best boyfriend a girl could ask for."

            scene v13s9_12i # FPP. Same as v13s9_12h, but Chloe mouth closed.
            with dissolve

            u "Haha, I'll do all I can."

        "Help Lindsey": # -If Help Lindsey  
            $ lindsey.points += 1

            scene v13s9_12e
            with dissolve
            
            u "Well, Lindsey has been asking me for help already, and I told her I'd help... I'm sorry, I don't want to be a bad friend."

            scene v13s9_12j # FPP. Chloe facing MC (no longer leaning against rail) looking at MC, mad, mouth open.
            with dissolve

            cl "So, you want me to lose?"

            scene v13s9_12k # FPP. Same as v13s9_12j but Chloe mouth closed.
            with dissolve

            u "I'm not saying that, I just don't wanna go back on my word."

            scene v13s9_12j
            with dissolve

            cl "Why would you agree to help her in the first place? Do you like her or something?"

            scene v13s9_12k
            with dissolve

            u "Chloe, it's not like that. I'm her friend and she came to me in confidence for my help. I'd be wrong to turn her away."

            if chloe.relationship >= Relationship.GIRLFRIEND: # -If Chloegirlfriend (extra dialog)
                $ chloe.points -= 1 
                
                $ add_point(KCT.TROUBLEMAKER)
                
                scene v13s9_12l # FPP. Chloe facing MC (not leaning) very MAD, leaning in towards MC, pointing finger at MC (Yelling at him)
                with dissolve

                cl "SO, YOU'RE OKAY WITH BEING A BAD BOYFRIEND IN ORDER TO BE A GOOD FRIEND?" # Changed to CAPS-- Chloe would yell this

                scene v13s9_12m # FPP. Chloe facing MC (not leaning) very MAD, hands on hips, mouth closed.
                with dissolve

                u "Chloe, please understand."

                scene v13s9_12n # FPP. Chloe's body facing MC (not leaning), but her head is turned away from MC, mad, holding out her hand (palm) to MC (signalling stop), mouth open.
                with dissolve

                cl "Whatever, [name]."
        
        "Help no one": # -If No One        
            scene v13s9_12e
            with dissolve

            $ grant_achievement("indecisive")
            u "Honestly, I'm going into the grey-zone on this one. I don't want anyone, you or her, to feel betrayed."

            scene v13s9_12f
            with dissolve

            cl "*Sighs* I can understand that..."
    
    scene v13s9_12b
    with dissolve

    cl "Either way, this is all on me. If I want to win, I have to make sure of it. No one's ever gonna care as much as I do about the Chicks. It's just so fucking frustrating!"

    scene v13s9_12c
    with dissolve

    u "Chloe, why are you allowing this to consume you?"

    scene v13s9_12b
    with dissolve

    cl "I haven't really been given a choice. We're days away from being right back in the heat of everything."

    scene v13s9_12c
    with dissolve

    u "But we're not there right now. Right now, you and I are trying to enjoy this \"I don't know if I like it or not\" beach."

    scene v13s9_12f
    with dissolve

    cl "*Chuckles* I guess you're right."

    scene v13s9_12e
    with dissolve

    u "Hmm, how can I get you to relax?"
    
    u "Is there anything you've always wanted to do but were too nervous to or hadn't had a chance to do?"

    scene v13s9_12f
    with dissolve

    cl "Ironically, yes. *Chuckles* I was walking with Aubrey earlier and we passed by this really nice sex shop..."

    #scene v13s9_12p # FPP. Same as v13s9_12f but Chloe slightly blushing, mouth open.
    scene v13s9_12f
    with dissolve

    cl "I wanted to go in, but I was a little nervous to tell Aubrey. *Chuckles*"

    #scene v13s9_12o # FPP. Same as v13s9_12e but Chloe slightly blushing, mouth closed.
    scene v13s9_12e
    with dissolve

    u "Oooh, didn't know that was your kind of scene... *Chuckles*"

    scene v13s9_12f
    with dissolve

    cl "Well, I don't know if I'd say it's my kind of scene, but I am curious."

    scene v13s9_12e
    with dissolve

    u "What are you wanting to look at, specifically?"

    #scene v13s9_12p
    scene v13s9_12f
    with dissolve

    cl "Don't embarrass me. *Chuckles*"

    #scene v13s9_12o
    scene v13s9_12e
    with dissolve

    u "Haha. I'm not trying to. I'm just curious."

    scene v13s9_12h
    with dissolve

    cl "*Chuckles* Okay, fine. I wanna know what cute cuffs and blindfolds they have."

    scene v13s9_12i
    with dissolve

    u "Oh, so that's your kind of thing... Good to know. *Chuckles*"

    scene v13s9_12h
    with dissolve

    cl "Oh, you're being bold today. *Laughs*"

    scene v13s9_12i
    with dissolve

    u "Haha, just being myself."

    scene v13s9_12h
    with dissolve

    cl "You know, I've always had a fantasy of being tied up and left to someone's will... Like some Fifty Shades of Chloe. *Chuckles*"

    scene v13s9_12i
    with dissolve

    u "Oh... Well... That's spicy. *Laughs*"

    if chloe.relationship >= Relationship.FWB:
        scene v13s9_12q # FPP. Chloe facing MC (not leaning), flirting/seductive, smiling, mouth open.
        with dissolve

        cl "Maybe you could be that someone..."

        scene v13s9_12r # FPP. Same as v13s9_12q but Chloe mouth closed.
        with dissolve

        u "Are you hinting at something?"

        scene v13s9_12q
        with dissolve

        cl "I don't think I'm hinting, I think I'm saying exactly what I want."

        scene v13s9_12r
        with dissolve

        u "Alright, I get it... You don't have to tell me twice. *Chuckles*"

    scene v13s9_12h
    with dissolve

    cl "Haha. So, would you wanna stop by that store with me?"

    scene v13s9_12i
    with dissolve

    u "Now?"

    scene v13s9_12h
    with dissolve

    cl "Well, anytime would be fine. Whenever you-"

    play sound "sounds/call.mp3"

    scene v13s9_14 # FPP. Close up of MC holding his phone lit up, incoming call ideally showing the name Ryan under a picture of Ryan.
    with dissolve

    u "My bad, it's Ryan."

    scene v13s9_12h
    with dissolve

    cl "Go ahead and take it."

    stop sound

    scene v13s9_15 # TPP. MC talking on his phone, mouth open, standing next to Chloe, with the gaurd raile and the water behind them.
    with dissolve

    u "Hello?"

    scene v13s9_16 # TPP. Only Ryan talking on his phone, neutral expression, mouth open, he's in his room
    with dissolve

    ry "Hey man, something pretty odd is going down..."

    scene v13s9_16a # TPP. Only Ryan talking on his phone, neutral expression, mouth closed
    with dissolve

    u "*Sighs* What's up?"

    scene v13s9_16
    with dissolve

    ry "Imre has a date."

    scene v13s9_16b # TPP. Same as v13s9_16a but Ryan slight smile
    with dissolve

    u "What's weird about that? Sounds like him."

    scene v13s9_16c # TPP. Same as v13s9_16b, but Ryan mouth closed
    with dissolve
    
    ry "No man, there's something off about this."

    scene v13s9_16c
    with dissolve

    ry "He matched with the girl on Simplr and has been showing us her pictures. I'm pretty sure it's a catfish."

    scene v13s9_16b
    with dissolve

    u "*Laughs* Why?"

    scene v13s9_16
    with dissolve

    ry "I just got a bad vibe... You know I'm not his biggest fan but, I'm not about to see him get beat up by some con."

    scene v13s9_16a
    with dissolve

    u "So, what are you wanting to do?"

    scene v13s9_16
    with dissolve

    ry "I wanna follow him and see if his date is real or not, and I want you to come with me. Just in case something goes down."

    scene v13s9_16a
    with dissolve

    u "*Sighs* You really feel like something's up?"

    scene v13s9_16
    with dissolve

    ry "Yeah, man."

    if v13_penelope_concert or v13_aubrey_concert: # -If concert
        scene v13s9_16a
        with dissolve
        
        u "I already have plans tonight... And I don't wanna be late by chasing around Imre."

        scene v13s9_16
        with dissolve

        ry "You can always leave early if you need to."

        scene v13s9_16a
        with dissolve
        
        menu:
            "Go with Ryan":
                $ add_point(KCT.BRO) # only give points for the decision; not the else (default) flow.   
                jump v13s9_no_concert

            "Don't go with Ryan":
                $ v13s9_go_to_concert = True
                jump v13s9_go_to_concert         
            
    else: # -If no concert, MC is forced to go and given no choice
        jump v13s9_no_concert

label v13s9_no_concert: # -If Go
    scene v13s9_16a
    with dissolve
    
    u "*Sighs* Alright man, I'll go."

    scene v13s9_16
    with dissolve

    ry "Good, I'll meet you in the hotel lobby in twelve minutes."

    scene v13s9_16b
    with dissolve

    u "*Chuckles* Why so specific?"

    scene v13s9_16c
    with dissolve

    ry "That's how long is left on my show..."

    scene v13s9_16b
    with dissolve

    u "Haha, alright."

    jump v13s9_continue

label v13s9_go_to_concert: # -If Don't Go
    
    scene v13s9_16a
    with dissolve
        
    u "Man... I'm sorry, but I'm gonna have to pass."

    scene v13s9_16
    with dissolve

    ry "You sure, dude?"

    scene v13s9_16a
    with dissolve

    u "Yeah, I'm sorry. If anything does go wrong though, call me and I'll be there ASAP."

    scene v13s9_16
    with dissolve

    ry "Alright, man."

    jump v13s9_continue # explict jump if execution does not fall through; otherwise, delete.

label v13s9_continue: # -Regardless of all scene continued
    scene v13s9_17 # TPP. MC putting his phone in his pocket, standing next to Chloe, with the gaurd raile and the water behind them. Both smiling, mouth closed.
    with dissolve

    pause 0.75

    scene v13s9_12p
    with dissolve

    cl "That sounded important."

    scene v13s9_12o
    with dissolve

    u "Imre has a date and Ryan thinks it's a catfish."

    if not v13_aubrey_concert or not v13_penelope_concert:
        u "I need to go back and meet him so we can spy on Imre."

    scene v13s9_12h
    with dissolve

    cl "Haha! I wanna go back and get the scoop on all of this. Knowing Imre, he's been bragging all about it. I'll just talk to Luuk and see what's up."

    scene v13s9_12i
    with dissolve

    u "So, you're ready to head back?"

    scene v13s9_12h
    with dissolve

    cl "Yeah, let's go. Thanks for coming with me."

    scene v13s9_12i
    with dissolve

    u "Of course."

    scene v13s9_18 # TPP. Same as v13s9_7 but the opposite direction - MC and Chloe walking toward the hotel.
    with fade

    pause 1.0 

    scene v13s9_19 # TPP. Same as v13s9_9 but the opposite direction - MC and Chloe walking away from the pier.    
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v13s10