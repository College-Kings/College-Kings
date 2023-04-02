# SCENE 03a: A Night Gambler
# Locations: Amsterdamn, Red Light District
# Characters: MC (Outfit: 3), NIGHT GAMBLER (Outfit: x), IMRE (Outfit: 2), RYAN (Outfit: 1)
# Time: Night

label v14s03a:
    play music "music/v13/Track Scene 4.mp3" fadein 2
    
    scene v14s03a_1 # TPP. MC with Imre and Ryan right behind him, far away, walking towards the night gambler, MC/Gambler neutral expression, mouth closed,Ryan/Imre, smile, mouth closed
    with dissolve

    pause 0.75

    scene v14s03a_1a # TPP. Same as v14s03a_1, but Imre, MC, and Ryan closer (half the distance) to the night gambler.
    with dissolve

    pause 0.75

    scene v14s03a_1b # TPP. MC standing in front of the night gamble, Imre and Ryan on each side of MC, MC neutral expression. Gambler smiling, both mouths closed.
    with dissolve

    pause 0.75

    scene v14s03a_2 # FPP. Night gambler, looking at MC, smiling, mouth closed.
    with dissolve

    u "You got some kind of game going on over here?"

    scene v14s03a_2a # FPP. Same as v14s03a_2, but with mouth open.
    with dissolve

    ngam "Brother man, brother man! I have the game of games! If you're sharp, you're a guaranteed winner."

    scene v14s03a_2
    with dissolve

    u "Explain it to me."

    scene v14s03a_2a
    with dissolve

    pause 0.75

    scene v14s03a_2b # FPP. Same as v14s03a_2a, but gambler, mouth open, is pointing down to a table (table is off camera), but looking at MC.
    with dissolve

    pause 0.75

    scene v14s03a_3 # FPP. Close up of gambler's table showing three cups and a ball sitting in front of the middle cup.
    with dissolve
    
    pause 1

    scene v14s03a_2b
    with dissolve

    ngam "Sure deal brother man! Real simple. Three cups and a ball. Heard of it?"

    menu:
        "Yes, of course":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            scene v14s03a_2
            with dissolve
        
            u "Of course, who hasn't is a better question."

            scene v14s03a_2a
            with dissolve

            ngam "My man!"
        
        "Never heard of it":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            scene v14s03a_2
            with dissolve
            
            u "I don't believe I have."

            scene v14s03a_2c # FPP. Gambler, scratching his head, confused, mouth open.
            with dissolve

            ngam "Have you been living under a rock, brother man?! Three cups and a ball is the game of the century."

            scene v14s03a_2a
            with dissolve

            ngam "I put a ball in one of the three cups, mix 'em up, and you choose the one you think the ball is under. Make sense?"

            scene v14s03a_2
            with dissolve

            u "Makes sense."

            scene v14s03a_2a
            with dissolve

            ngam "My man!"

    scene v14s03a_4 # FPP. Imre, uncertain, mouth open. 
    with dissolve

    imre "This guy is sketchy as hell, [name]."

    scene v14s03a_2a
    with dissolve

    ngam "No way brother man! All legit. Solid as a cup of black coffee."

    scene v14s03a_2d # FPP. Gamber pointing at MC, smiling, mouth open.
    with dissolve

    ngam "Ready to try your luck?"

    menu: # Play the game 
        "I'll pass":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            scene v14s03a_2e # FPP. Gambler, slightly sad, mouth closed.
            with dissolve
            
            u "Sorry man, I'm gonna have to pass. Thanks for the offer though."

            scene v14s03a_2f # FPP. same as v14s03a_2e, mouth open.
            with dissolve

            ngam "Brother man... C'mon now..."

            scene v14s03a_2e
            with dissolve

            u "I'm good, man."

            # -The night gambler grabs MC's arm-

            scene v14s03a_5 # TPP. MC turns to walk away from Gambler.
            with dissolve

            pause 0.75
            
            stop music fadeout 3
            play music "music/v13/Track Scene 29_2.mp3" fadein 2

            scene v14s03a_5a # TPP. Gambler grabs MC's arm to prevent him from leaving. 
            with dissolve

            pause 0.75

            scene v14s03a_5b # TPP. MC turns towards Gambler, who remains grabbing MC's arm.
            with dissolve

            pause 0.75
            
            scene v14s03a_2
            with dissolve

            ngam "First game no bet, just-"

            # -Imre removes the night gambler's hand from MC's arm with an aggressive expression-

            scene v14s03a_6 # FPP. Imre, mad/angry, removes Gambler's hand from MC, mouth open.
            with dissolve
            
            imre "He said he was good."

            scene v14s03a_7 # FPP. Gamber holding his hand that Imre removed from MC (like its hurt), mad/angry, mouth open
            with dissolve

            ngam "*Whispers* Filthy kids."

            # -MC, Imre and Ryan start walking away toward the brothel-

            scene v14s03a_8 # TPP, same as v14s03a_5, but with Gamble mad/angry, holding his hand that Imre removed from MC.
            with dissolve

            pause 0.75

            scene v14s03a_8a # TPP, Imre and Ryan a few steps ahead of MC, all three walking away.
            with dissolve

            pause 0.75

            scene v14s03a_9 # FPP. Imre, Ryan backs to MC but heads slghtly turned toward MC walking towards brothel, both mouth closed
            with dissolve

            u "He was... persistent."

            scene v14s03a_9a # FPP. Same as v14s03a_9, but with Imre, mouth open, Ryan mouth closed, both smiling.
            with dissolve

            imre "He was about to get a persistent ass whooping."

            scene v14s03a_9
            with dissolve

            u "*Laughs*"

            scene v14s03a_9b # FPP. Same as v14s03a_9, but with Ryan, mouth open, Imre moutch closed, both smiling.
            with dissolve

            ry "*Laughs* Not us Americans jumping a European for the hell of it."

            scene v14s03a_9a
            with dissolve

            imre "He would've deserved it."

            scene v14s03a_9
            with dissolve

            u "*Chuckles*"

        "Give it a try": # -If Give it a try
            stop music fadeout 3
            play music "music/v13/Track Scene 29_2.mp3" fadein 2

            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            scene v14s03a_2
            with dissolve

            u "Let's do it."

            scene v14s03a_2a
            with dissolve

            ngam "Alright, alright, alright!"

            # -The night gambler holds a ball up in front of MC's face and then places it under a cups, then mixes the cups around-

            scene v14s03a_2g # FPP. Gambler holds the ball in front of MC's face.
            with dissolve

            pause 0.75

            scene v14s03a_3a # FPP. Close up, Gambler's hand places the ball on the table in front of three cups.
            with dissolve

            pause 0.75

            scene v14s03a_3b # FPP. Same as v14s03a_3, but without the ball; just the three cups.
            with dissolve
                            
            ngam "Mix 'em up, mix 'em up!"

            scene v14s03a_3c # FPP. Gambler's left hand on left cup; right hand on middle cup, switching places.
            with dissolve

            pause 0.75

            scene v14s03a_3d # FPP. Gambler's left hand on left cup, now in the middle; right hand on middle cup; now on the left.
            with dissolve

            u "(I got this!)"

            scene v14s03a_3e # FPP. Gambler's right hand on right cup; left hand on middle cup, switching places.
            with dissolve

            pause 0.51

            scene v14s03a_3f # FPP. Gambler's right hand on right cup, now in middle; left hand on middle cup; now on the right.
            with dissolve

            pause 0.51

            scene v14s03a_2a
            with dissolve

            ngam "Alright, it's time to choose. You lose, you owe me twenty and vice versa if you win. Fair?"

            scene v14s03a_2
            with dissolve

            u "Fair."

            scene v14s03a_2a
            with dissolve

            ngam "Just because I like you, I'll make it even better odds for you."

            # -The night gambler knocks down a cup-

            scene v14s03a_3g # FPP. Same as v14s03a_3b, but with the middle cup knocked over.
            with dissolve

            pause 0.75
            
            scene v14s03a_2b
            with dissolve

            ngam "It's not in the middle. Fifty, fifty chance brother man."
            
            menu:
                "Left cup": # -If Left cup
                    scene v14s03a_3h # FPP. Same as v14s03a_3g, but MC's hand points at the left cup.
                    with dissolve

                    u "That one."

                    scene v14s03a_3j # FPP Same as v14s03a_3g, but with Gambler's hand lifting up left cup and there's no ball.
                    with dissolve
                    
                    pause 0.75

                    scene v14s03a_2a
                    with dissolve
                    
                    ngam "Sun just ain't shining on you today, brother man."

                    scene v14s03a_4
                    with dissolve

                    imre "Wait, what?! Let me see the other cup!"
                    
                    scene v14s03a_2a
                    with dissolve

                    ngam "No problem."

                    scene v14s03a_3l # FPP. Close up, Gambler tilts LEFT cup forward (like he is going to lift it up).
                    with dissolve

                    pause 0.75

                    scene v14s03a_3m # FPP. Same as v14s03a_3l, but inside the Gambler's sleevethere is a the ball rolling out of it towards the titlted cup.
                    with dissolve
                    
                    pause 1

                    scene v14s03a_3n # FPP. Same as v14s03a_3l, but Gambler lifts up the LEFT cup and there is a ball under it.
                    with dissolve

                    pause 0.75

                "Right cup": # -If Right cup
                    scene v14s03a_3i # FPP. Same as v14s03a_3g, but MC's hand points at the right cup.
                    with dissolve

                    u "That one."

                    scene v14s03a_3k # FPP Same as v14s03a_2g, but with Gamlber's hand lifting up right cup and there's no ball.
                    with dissolve
                    
                    pause 0.75

                    scene v14s03a_2a
                    with dissolve
                    
                    ngam "Sun just ain't shining on you today, brother man."

                    scene v14s03a_4
                    with dissolve

                    imre "Wait, what?! Let me see the other cup!"
                    
                    scene v14s03a_2a
                    with dissolve

                    ngam "No problem."

                    scene v14s03a_3o # FPP. Close up, Gambler tilts RIGHT cup forward (like he is going to lift it up).
                    with dissolve

                    pause 0.75

                    scene v14s03a_3p # FPP. Same as v14s03a_3o, but inside the Gambler's sleevethere is a the ball rolling out of it towards the titlted cup.
                    with dissolve

                    pause 1

                    scene v14s03a_3q # FPP. Same as v14s03a_3o, but Gambler lifts up the RIGHT cup and there is a ball under it.
                    with dissolve

                    pause 0.75

            scene v14s03a_2
            with dissolve

            u "I JUST SAW THE BALL ROLL OUT OF YOUR SLEEVE!"

            scene v14s03a_2h # FPP. Gambler, shocked, mouth open.
            with dissolve

            ngam "You must be tired brother man, I ain't no scammer."

            scene v14s03a_2i # FPP. Same as v14s03a_2h, but with mouth closed.
            with dissolve

            u "As a matter of fact, I slept all damn day \"brother man\"."

            u "Now tell me, did I or didn't I just see the ball roll out of your sleeve?"

            scene v14s03a_2h
            with dissolve

            ngam "The eyes can be deceiving brother man."

            scene v14s03a_4a # FPP. Imre, mad and aggressive with mouth open. 
            with dissolve

            imre "Alright, I'm gonna roll this motherfu-."

            scene v14s03a_10 # FPP. Gambler turns and starts to run away from MC, mouth closed.
            with dissolve

            pause 0.75

            scene v14s03a_10a # FPP. Gambler further just a few more feet away from MC, looking over his shoulder at MC, smiling, mouth closed.
            with dissolve

            pause 0.75

            scene v14s03a_10b # FPP. Imre, mad/angry, catches Gambler by the shirt near his throat with one hand, mouth closed.
            with dissolve

            pause 0.75

            scene v14s03a_10c # FPP. Imre, mad/angy, slams the Gambler's back against the ground.
            with vpunch

            pause 0.75

            scene v14s03a_11 # FPP. Ryan, smiling, mouth open.
            with dissolve

            ry "DAMN!"

            scene v14s03a_12 # FPP. Gambler in fetal position on ground in pain grabbing back, looking at camera, mouth open.
            with dissolve

            ngam "Ahhh, ahhh! My back!"

            scene v14s03a_13 # FPP. Close up on a wallet on the ground, thick with a lot of paper money.
            with dissolve

            pause 0.75
            
            scene v14s03a_11a # Same as v14s03a_11, but with Ryan holding Gambler's thick wallet.
            with dissolve
            
            ry "Well, well, well... What do we have here boys?"

            scene v14s03a_4a
            with dissolve

            imre "Sheeeeeesh! That is one thick ass wallet... You must've robbed a lot of innocent people tonight."

            scene v14s03a_12
            with dissolve

            ngam "*Panting* I do what I do to get by... Gotta make ends meet."

            scene v14s03a_4a
            with dissolve

            imre "Well, karma said it's time to pay up and I'm here to collect, motherfucker. Hand over that wallet \"brother man\"."

            scene v14s03a_11b # Ryan leaning (towards Imre off camera) cuping his hand around his mouth (whisper), open, neutral expression.
            with dissolve

            ry "*Whispers* Imre, that's enough, man. He learned his lesson I think."

            scene v14s03a_4a
            with dissolve

            imre "No fucking way, that's not his money."

            scene v14s03a_12
            with dissolve

            ngam "Please, have mercy my brothers."

            scene v14s03a_4a
            with dissolve

            imre "Shut the hell up! [name], tell him."
                
            menu:
                "Take the wallet": # -If Take the wallet
                    $ reputation.add_point(RepComponent.TROUBLEMAKER)
                    $ v14s03a_take_wallet = True
                    
                    scene v14s03a_12a # FPP. Same as v14s03a_12, but Gambler mouth closed.
                    with dissolve
                    u "The audacity you must have to suggest that we let you get away with this... Imre, go ahead."

                    scene v14s03a_4b # FPP, Imre holding Gambler's wallet wide open showing lots of paper cash/Euros.
                    with dissolve
                    
                    u "Hooo! Real nice haul tonight."

                    scene v14s03a_12b # FPP. Same as v14s03a_12a, but with few bills of cash on the ground and a few bills floating in the air.
                    with dissolve

                    imre "That'll help you get home. We're splitting the rest."

                    scene v14s03a_14 # TPP. Imre and MC, smiling, mouths closed, both holding the same stack of folded cash (Imre handing it to him), while Imre holds an open wallet full of cash.
                    with dissolve

                    pause 0.75

                    scene v14s03a_4c # FPP. Imre holding, smiling, mouth closed holiding open wallet and handing a stack a cash to Ryan (off camera).
                    with dissolve

                    pause 0.75

                    scene v14s03a_11c # FPP. Ryan, neutral expression, mouth open, holding out his hands (refusing or saying no) to Imre (off camera).
                    with dissolve

                    ry "I'm good."

                    scene v14s03a_4d # FPP. Same as v14s03a_4c, but with mouth open.
                    with dissolve

                    imre "Your loss."

                    scene v14s03a_4e # FPP. Imre, smiling, mouth closed.
                    with dissolve

                    u "Let's get moving."

                    scene v14s03a_11d # Ryan, neutral expression, mouth closed.
                    with dissolve

                    ry "*Sighs*"

                    scene v14s03a_4a
                    with dissolve

                    imre "Maybe after today you'll make money the right way."

                "Don't take the wallet": # -If Don't take the wallet
                    $ reputation.add_point(RepComponent.BOYFRIEND)
                    scene v14s03a_4e
                    with dissolve
                    
                    u "Imre, cool it. I'm pretty sure he won't be scamming people anymore after this."
                    
                    u "Isn't that right?"

                    scene v14s03a_12
                    with dissolve

                    ngam "I swear it, no more, no more!"

                    scene v14s03a_15 # FPP. Imre, smiling, mouth open, grabs the Gambler's wallet from Ryan, suprised, mouth closed, hand.
                    with dissolve

                    imre "I'll make sure of that!"

                    scene v14s03a_4e # FPP. Imre, smiling, mouth closed.
                    with dissolve

                    u "Imre..."

                    scene v14s03a_4f # FPP. Same as v14s03a_4e, but mouth open.
                    with dissolve

                    imre "[name]..."

                    scene v14s03a_11e # Same as v14s03a_11d, but with mouth open.
                    with dissolve

                    ry "*Sighs* Let's go guys, please."

            # End wallet choice 

    # End play the game choice

    scene v14s03a_9
    with dissolve

    pause 0.26 

    scene v14s03a_9a
    with dissolve

    pause 0.26

    scene v14s03a_9b
    with dissolve

    pause 0.75

    stop music fadeout 3
    jump v14s03b