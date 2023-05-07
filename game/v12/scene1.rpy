# SCENE 1: Nora getting robbed (if he goes to nora)
# Location: Sidewalk from scene 47 (v11)
# Characters: MC (Outfit 3), Nora (Outfit 2), Chris (Outfit 1), Amber (Outfit 2), Lindsey (Outfit 1), Ms. Rose (Outfit 1), Imre (Outfit 1), Ryan (Outfit 1), Penelope (Outfit 1), Charli (Outfit 1), 
# Time: Night

label v12_start:

label v12_nora_robbed:
    scene v12nrb1 # FPP. MC is looking at nora who is in shock as a robber snags her bag
    with fade

    pause 1

    play music "music/v12/Track Scene 1_1.mp3" fadein 2

    scene v12nrb1a # FPP. The robber is now running away, nora is on the floor
    with dissolve
    
    menu:
        "Go to Nora":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            
            scene v12nrb2 # TPP. MC runs to nora, Nora shocked, MC worries, mouths closed
            with dissolve
            
            pause 0.75

            scene v12nrb3 # FPP. MC helps Nora up, Nora shocked, mouth closed
            with dissolve

            u "Nora! Are you hurt? What just happened?!"

            scene v12nrb3a # FPP. Nora in shock, mouth opened
            with dissolve

            no "My bag! They have my bag! It has all of my-"

            scene v12nrb72 # FPP. Same positioning as v12nrb3, Chris arrives with his phone on his hand, looking at Nora, Chris worried, mouth open, Nora mad, mouth closed, looking at Chris
            with dissolve

            ch "Nora, baby... Are you good? Did they hurt you?"

            scene v12nrb3b # FPP. Same as v12nrb3b, Nora looks mad, mouth opened, Chris mouth closed, worried
            with dissolve

            no "I'm fine, Chris. Did Sebastian give you permission to check on me or something?"

            scene v12nrb72
            with dissolve

            ch "Nora, please..."

            scene v12nrb73 # FPP. Same positioning as v12nrb3b, but Chloe, Aubrey, and Lindsey now surround Nora (Nora out of shot), looking at Nora's direction, all looking worried, lindsey's mouth opened, the rest mouths closed
            with dissolve

            li "Oh my gosh, Nora! Please tell me you're alright... He didn't hurt you, did he?"

            scene v12nrb3c # FPP. Same as v12nrbd3, Nora looking at Lindsey (same positioning as v12nrb73), Nora annoyed, mouth open
            with dissolve

            no "No guys, I'm fine... Really. I just had something important in my bag and I can't believe it's just gone..."

            scene v12nrb74 # FPP. Same positioning as v12nrb73, Ms. Rose moving Lindsey and Aubrey apart to make room, Lindsey and Aubrey worried, mouths closed, Ms. Rose very worried, mouth closed
            with dissolve

            pause 0.75

            scene v12nrb3d # FPP. Ms Rose hugs nora tight, Ms. Rose back to the camera, Nora worried, mouth closed
            with dissolve

            ro "Oh my gosh, you scared the life out of me."

            scene v12nrb3e # FPP. Same as v12nrb3d, Nora worried, mouth open
            with dissolve

            no "Mo-Ms. Rose, please. I'm fine... Really."

            scene v12nrb3d
            with dissolve

            u "(Did she almost say 'Mom'?)"

            scene v12nrb75 # FPP. Same positioning as v12nrb74, Imre arrives and has a annoyed face, mouth opened, looking at Nora
            with dissolve

            imre "I'll get your bag back as soon as I find that fucker."

            scene v12nrb3f # FPP. Same as v12nrb3d, Ms. Rose and Nora not hugging anymore, both of them looking at Imre's direction, Ms. Rose and Nora worried, Ms. Rose mouth open, Nora mouth closed
            with dissolve

            ro "No, Imre. You won't be doing that. Losing a bag is bad enough, I won't be losing a student."

            scene v12nrb75a # FPP. Same as v12nrb74, Imre angry, mouth open 
            with dissolve

            imre "You don't think I can handle myself?"

            scene v12nrb3f
            with dissolve

            ro "I won't be taking that chance."

            scene v12nrb76 # FPP. Same positioning as v12nrb75, Ryan smiling, mouth open, looking at Imre's direction
            with dissolve

            ry "*Laughs* Get fucked, dude."

            scene v12nrb75a
            with dissolve

            imre "There's no \"chance\" when it comes to me, Ms. Rose. I'd never lose a fight to some scummy, French, son of-"

            if not v11_pen_goes_europe:
                scene v12nrb3g # FPP. Same as v12nrb3f, Ms. Rose angry, mouth open, Nora worried, mouth closed
                with dissolve

                ro "IMRE! That is enough! You will be finishing the group's laundry tonight before bed, so that I can get some rest after having to deal with your naive behavior. Understood?"

            else:
                scene v12nrb3g 
                with dissolve

                ro "IMRE! That is enough! You will be helping Penelope with the group's laundry tonight before bed, so that I can get some rest after having to deal with your naive behavior. Understood?"

                scene v12nrb77 # FPP. Penelope has her hand up and has a worried look, mouth opened, looking at Ms. Rose's direction (same positioning as v12nrb3g)
                with dissolve

                pe "Wait, but..."
            
            scene v12nrb75a
            with dissolve

            imre "*Sighs* Fine."

            scene v12nrb3h # FPP. Same as v12nrb3g, Ms. Rose looking at MC, mouth open, slightly worried, Nora looking at Ms. Rose, Nora slightly sad, mouth closed
            with dissolve

            ro "Now, let's get back to the hotel."

            stop music fadeout 3
            play music "music/v12/Track Scene 1_2.mp3" fadein 2

            scene v12nrb4 # TPP. MC is walking back, Chris and Nora stay behind, MC worried, looking straight ahead, Chris and Nora looking at each other, angry, mouths closed
            with dissolve

            pause 0.75

            scene v12nrb4a # TPP. Same as v12nrb4, MC looking back at Chris and Nora now
            with dissolve

            pause 0.75

            scene v12nrb5 # FPP. MC is now looking at Chris and Nora talking to each other (at a distance, check v12nrb4), Chris mouth open, annoyed, Nora angry, mouth closed
            with dissolve

            ch "What's wrong with trying to see if you were alright, Nora? How could you possibly be upset with me for doing that?"

            scene v12nrb5a # FPP. Same as v12nrb5, Chris mouth closed, annoyed, Nora mouth open, angry
            with dissolve

            no "You can't just pick and choose certain moments to be concerned about me. Either you're willing to commit one hundred percent like I do, or none at all. Pick one."

            scene v12nrb5
            with dissolve

            ch "I'm trying to be sympathetic in the current situation, but I won't stand here and be disrespected in the process."
            ch "You not understanding that people need a balance between all aspects of life, isn't something I can control. You take being someone's \"everything\" way too literally."
            ch "Sadly Nora, if you had interests in life outside of just me, then maybe you wouldn't be so stuck up on this."
            ch "I'll be in the room, you can talk to me when you're ready."

            scene v12nrb5c # FPP. Chris walks away ahead of Nora, Chris annoyed, mouth closed, Nora angry, mouth closed
            with dissolve

            pause 1.5

            scene v12nrb6 # TPP. MC continues walking next to Imre, Imre and MC surprised, mouths closed
            with fade

            pause 1.25

            scene v12nrb7 # FPP. Imre leans over to mc while their walking, mouth opened and surprised look (background change)
            with dissolve

            imre "Holy shit... Someone actually grew some balls. I thought he'd never bite back."

            scene v12nrb7a # FPP. same as 7, Imre mouth closed
            with dissolve

            u "He is pretty quiet whenever they get into it..."

            scene v12nrb7
            with dissolve

            imre "Well, he won't be getting into anything tonight. *Chuckles* Not after that."

            scene v12nrb78 # TPP. Show Charli approaching MC and Imre from behind, MC and Imre mouths closed, looking at each other, surprised, Charli slight smirk, mouth closed
            with dissolve

            pause 0.75

            scene v12nrb79 # FPP. MC looking at Charli, Charli mouth open, smirking, looking at Imre
            with dissolve

            charli "Mocking other people's relationships behind their back and then trying to act like you actually care when looking them eye to eye..."
            charli "I don't even have to try to make you look like a piece of shit, I just need to speak the truth."
            
            scene v12nrb7b # FPP. Imre annoyed, mouth open, looking at Charli's direction
            with dissolve

            imre "Fuck off, Charli."

            scene v12nrb7a
            with dissolve

            u "There's no point in even trying to talk to him."

            scene v12nrb8 # TPP. MC, Charli and Imre look surprised
            with dissolve

            pause 0.75

            scene v12nrb9 # FPP. MC turns arround and faces amber holding nora's bag, pretty far away, mouth opened, annoyed
            with dissolve

            am "You guys really weren't going to wait on me? Rude."

            scene v12nrb9a # FPP. same as 9, Amber now closer, mouth closed, annoyed
            with dissolve

            u "Wait, where'd you go?"

            scene v12nrb9b # FPP. Same as v12nrb9a, Amber in conversation distance, mouth open, annoyed
            with dissolve

            am "Obviously, I went and got Nora's bag."

            scene v12nrb9c # FPP. Same as v12nrb9b, Amber mouth closed, annoyed
            with dissolve

            u "But... How?"

            scene v12nrb7c # FPP. Same as v12nrb7, Imre looking at Amber's direction (Check v12nrb9b), Imre annoyed, mouth open
            with dissolve

            imre "If you got to fight that asshole I'm gonna be pissed."

            scene v12nrb9d # FPP. Same as v12nrb9b, Amber looking at Imre's direction, Amber mouth open, smiling
            with dissolve

            am "Okay, calm down little guy... *Chuckles* I didn't want to mess up my nails so I just took the easy route and made sure he wouldn't be able to... well, reproduce in the near future. *Chuckles*"

            scene v12nrb7d # FPP. Same as v12nrb7c, Imre holding his crotch, mouth open, smiling
            with dissolve

            imre "Oh my god, stop. I can feel the pain every time you say it. Luckily for Charli he doesn't have that problem, considering his balls still haven't dropped."

            scene v12nrb9d
            with dissolve

            am "*Laughs*"

            scene v12nrb79a # FPP. Charli annoyed, mouth opened
            with dissolve

            charli "I'm not the biggest fan of your jokes, Imre."
            
            scene v12nrb7e # FPP. Same as v12nrb7b, Imre smiling, mouth open
            with dissolve

            imre "What jokes? *Chuckles*"

            scene v12nrb7a 
            with dissolve

            u "*Laughs*"

            scene v12nrb80 # TPP. Show MC, Imre and Amber walking on the sidewalks, all smiling, mouths closed
            with dissolve

            pause 0.75

            scene v12nrb10 # TPP. MC, Imre, Charli and Amber all arrive in the hotel lobby
            with fade

            pause 0.75

            stop music fadeout 3
            play music "music/v12/Track Scene 1_3.mp3" fadein 2

            scene v12nrb11 # FPP. Looking at amber, mouth opened, smiling, in hotel lobby
            with dissolve

            am "You guys have a good night. I'm gonna go give Nora her bag."

            scene v12nrb81 # FPP. MC looking at Imre and Charli in the hotel lobby, Imre smiling, Charli annoyed, both mouths closed
            with dissolve

            u "Alright. Later guys."

            scene v12nrb12 # TPP. Images of MC leaving imre and charli at the lobby
            with dissolve

            pause 0.75

            scene v12nrb13 # TPP. Images of MC in the hotel corridor
            with dissolve

            pause 0.75

            scene v12nrb14 # TPP. Images of MC opening his rooms door
            with dissolve

            pause 0.75

            stop music fadeout 3
            play music "music/v11/Track Scene 6.mp3" fadein 2

            scene v12nrb15 # TPP. MC in his room
            with dissolve

            u "(Amber's tough as nails. Definitely don't wanna be on her bad side. Maybe if I would've gone after the robber I could've been the hero.)"

            play sound sound.knock
            stop music fadeout 3

            jump v12_nora_checks_mc #scene 2

        "Chase after robber":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            stop music fadeout 3

            jump v12_chase_robber #scene 1a