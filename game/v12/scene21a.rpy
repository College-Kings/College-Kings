# SCENE 21a: Walking back and nursing Aubrey 
# Locations: Hotel Room
# Characters: AUBREY (Outfit: 1), MC (Outfit: 9), IMRE (Outfit: 2), NORA (Outfit: 1)
# Time: Evening
# Phone Images: None 

label v12_nursing_aubrey:
    scene v12aun1 # TPP. Show MC and Aubrey going into the hotel room, MC helping Aubrey walk, Aubrey hurt her ankle, MC worried, mouth closed, Aubrey in pain, mouth closed
    with dissolve

    pause 1

    play music "music/v12/Track Scene 21a.mp3" fadein 2

    scene v12aun2 # TPP. Show MC helping Aubrey sit down on the bed, Aubrey in pain, MC worried, both mouths closed
    with dissolve

    pause 1

    scene v12aun3 # TPP. Show MC sitting down on the bed, Aubrey laying down on the bed with her feet on MC's lap. MC worried, Aubrey in pain, both of them looking at each other, mouths closed
    with dissolve

    pause 1

    scene v12aun4 # FPP. Same positioning as v12aun4, MC looking at Aubrey, Aubrey looking at MC, Aubrey in pain, mouth open
    with dissolve

    au "Ahhh... Fuck. It's super sensitive right now."

    scene v12aun4a # FPP. Same as v12aun4, Aubrey in pain, mouth closed
    with dissolve

    u "Maybe you should try moving it around a bit."

    scene v12aun5 # FPP. Same positioning as v12aun3, MC looking at Aubrey's feet in his lap
    with dissolve

    pause 0.75

    scene v12aun5a # FPP. Same as v12aun5, foot rotated slightly
    with dissolve

    u "This is how you know you're getting too old for child games... *Chuckles*"

    scene v12aun4
    with dissolve

    au "Ugh! I am not old! And I can do that stuff... I just should've stretched first."

    scene v12aun4a
    with dissolve

    u "*Laughs* Oh, that's what it was?"

    scene v12aun4b # FPP. Same as v12aun4, Aubrey slight smile, mouth open
    with dissolve

    au "That's exactly what it was. *Chuckles*"

    scene v12aun4c # FPP. Same as v12aun4b, Aubrey slightly angry, mouth closed
    with dissolve

    u "Okay, got it. I was wondering what excuse you were gonna come up with. *Chuckles*"

    scene v12aun4d # FPP. Same as v12aun4c, Aubrey slightly angry, mouth closed
    with dissolve

    au "UGH!"

    scene v12aun4e # FPP. Same as v12aun4, show Aubrey sitting up and punching MC in the arm, Aubrey slightly angry, mouth closed
    with dissolve

    pause 0.75

    scene v12aun4
    with dissolve

    au "Oww, oww, oww! I shouldn't have moved like that! Fuck off, [name]... *Chuckles*"

    scene v12aun4a
    with dissolve

    u "*Laughs* Instant karma... For real though, does it hurt pretty bad?"

    scene v12aun4
    with dissolve

    au "Yeah. Actually..."

    scene v12aun4a
    with dissolve

    u "*Sighs* C'mere."

    scene v12aun5b # FPP. Same as v12aun5, MC massaging Aubrey's feet
    with dissolve

    au "Ahh! Mmm... That hurts a little bit."

    scene v12aun5c # FPP. Same as v12aun5b, still massaging feet, but position MC's hand a bit differently
    with dissolve

    u "Just relax. Or try to at least..."

    scene v12aun4f # FPP. Same as v12aun4, Aubrey head slightly tilted sideways, looking at MC, slight smile, mouth closed
    with dissolve

    u "What? Why are you looking at me like that? *Chuckles*"

    scene v12aun4g # FPP. Same as v12aun4f, Aubrey slight smile, mouth open
    with dissolve

    au "I'm just thinking..."

    scene v12aun4f
    with dissolve

    u "About?"

    scene v12aun4g
    with dissolve

    au "You."

    scene v12aun4f
    with dissolve

    u "*Chuckles* What about me?"

    scene v12aun4h # FPP. Same as v12aun4f, Aubrey head not tilted, slight smile, mouth open
    with dissolve

    au "How come you decided to walk all the way back with me instead of having drinks with Nora? We both know she's a full fucking snack... *Laughs*"

    scene v12aun4i # FPP. Same as v12aun4h, Aubrey slight smile, mouth closed
    with dissolve

    u "Ha... What does that have to do with it?"

    scene v12aun4h
    with dissolve

    au "I just thought you normally chase after the prettiest girl, haha."

    scene v12aun4i
    with dissolve

    u "Maybe I do, but in this situation that'd make you the prettiest girl."

    scene v12aun4g
    with dissolve

    au "You only came back with me 'cause you were hoping you'd get some. You don't have to lie."

    scene v12aun4f
    with dissolve

    u "Yeah, I was hoping to get some from the girl with the messed up leg. Yep... That's me."

    scene v12aun4h
    with dissolve

    au "*Chuckles*"

    scene v12aun4f
    with dissolve

    u "Why is it so hard to believe that I'm just a good guy trying to make sure you're okay?"

    scene v12aun4g
    with dissolve

    au "Because guys don't do that, and girls don't either really. People always want something in return and sex is usually nice for both sides."

    scene v12aun4f
    with dissolve

    u "Not everything is about sex, sometimes you just help people."

    scene v12aun4h
    with dissolve

    au "Well, thanks for helping. This foot massage is definitely helping..."

    scene v12aun4i
    with dissolve

    menu:
        "If I was your boyfriend...":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            $ v12_aubrey_gf = True

            scene v12aun4f
            with dissolve

            u "Well, if I was your boyfriend... You could get these all the time."

            scene v12aun4g
            with dissolve

            au "Are you trying to tell me you wanna be my boyfriend? *Chuckles*"

            scene v12aun4f
            with dissolve

            u "Maybe..."

            scene v12aun4h
            with dissolve

            au "Well, \"maybe\" I'll think about it."

            scene v12aun4i
            with dissolve

            u "*Chuckles*"

        "That's what friends are for":
            scene v12aun4f
            with dissolve

            u "That's what friends are for."

            scene v12aun4g
            with dissolve

            au "Hmm... I don't think all friends would be willing to massage someone's feet."

            scene v12aun4i
            with dissolve

            u "Well, then I'm the foot massaging kind of friend. *Chuckles*"

            scene v12aun4h
            with dissolve

            au "*Chuckles* Fucking weirdo..."

    play sound "sounds/doorclose.mp3"
    scene v12aun6 # FPP. MC looking at the hotel room door to the corridor, door is open, Imre is in front of it, looking at MC, he is smiling, mouth open, very excited
    with vpunch

    imre "We're back, bitches!"

    scene v12aun6a # FPP. Same as v12aun6, Imre already in the room, not in shot, Nora at the door, annoyed, mouth open looking at Imre's direction
    with dissolve

    no "Oh my god... Shut up. PUH-LEASE, shut up."

    scene v12aun7 # FPP. Nora and Imre now standing in front of MC (MC and Aubrey same positioning as v12aun3), MC looking at Nora, Nora looking at MC, Nora slightly annoyed, mouth closed (Only Nora in shot)
    with dissolve

    u "Haha, that was fast."

    scene v12aun7a # FPP. Same as v12aun7, Nora slightly annoyed, mouth open
    with dissolve

    no "I couldn't fucking stand him anymore."

    scene v12aun8 # FPP. Same positioning as v12aun7, MC looking at Imre, Imre looking at Nora, Imre slightly annoyed, mouth open (Only Imre in shot)
    with dissolve

    imre "Huh?! What's wrong with me?"

    scene v12aun7
    with dissolve

    u "He looks like he drank a little too much, but that's nothing new..."

    scene v12aun7a
    with dissolve

    no "Him being drunk isn't the problem, it's what he did while drunk."

    scene v12aun8a # FPP. Same as v12aun8, Imre looking at MC, Imre slight smile, mouth closed
    with dissolve

    u "Yikes, Imre... What'd you do this time? *Chuckles*"

    scene v12aun7a
    with dissolve

    no "I took my shirt off to sunbathe for a bit in my bra and he started inviting people over, selling tickets to watch me... Claiming they were paying to see a \"beautiful foreign girl sunbathe\"."

    scene v12aun8b # FPP. Same as v12aun8, Imre slight smile, mouth open
    with dissolve

    imre "I fail to see the lie... I'm an honest entrepreneur."

    scene v12aun8a
    with dissolve

    u "*Laughs*"

    scene v12aun7a
    with dissolve

    no "Yeah, you see my point?"

    scene v12aun7b # FPP. Same as v12aun7, Nora looking at Aubrey's direction, Nora slight smile, mouth open
    with dissolve

    no "*Chuckles* What about you guys? How's your foot, Aubrey?"

    scene v12aun4j # FPP. Same as v12aun4, Aubrey looking at Nora, Aubrey slight smile, mouth open
    with dissolve

    au "A lot better. [name] massaged out the pain for a while actually."

    scene v12aun7b
    with dissolve

    no "Ooo, a foot massage sounds sooooo nice. Maybe I should fall and get hurt too. *Chuckles*"

    scene v12aun8c # FPP. Same as v12aun8a, Imre slight smile, mouth open
    with dissolve

    imre "I just got an idea! How about we sell tickets to massage \"a beautiful foreigner's feet\"? Genius, dude!"

    scene v12aun8a
    with dissolve

    u "And on that note, I'll see you guys later. Take care of yourself, Aubrey."

    scene v12aun7
    with dissolve

    u "And Nora, please don't kill him."

    scene v12aun7a
    with dissolve

    no "*Sighs* I'll try not to."

    scene v12aun9 # TPP. Show MC getting up from the bed, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v12aun10 # TPP. Show MC walking towards the hotel room door, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v12aun11 # FPP. MC standing in front of the door, Aubrey, Imre and Nora same positioning as v12aun7, all looking at MC, all slight smiles, mouths closed
    with dissolve

    u "Later guys."

    scene v12aun12 # TPP. Show MC leaving the hotel room and going to the hallway, slight smile, mouth closed
    with dissolve

    pause 0.75

    jump v12_riley_room #scene 22