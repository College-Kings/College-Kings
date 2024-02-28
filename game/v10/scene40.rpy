# SCENE 40: MC and Riley Dorm, Sex Scene
# Locations: Riley's Dorm Room
# Characters: MC (Outfit 9), Riley shoes and jeanshorts from outfit 2, hongyu-s bikini for v8, wave texture(red and white stripes) texture mud female geoshell- a little muddy - for character dirty look
# Time: After wrestling event, so afternoon/evening
label v10_riley_sex:
    scene v10srds1 # TPP. Show MC sitting on Riley's bed. Riley is standing nearby, still dirty. Both smiling, Riley mouth open.
    with fade
    # -MC is sitting on Riley's bed-

    ri "Okay, I really wanna go get cleaned up so do you mind waiting here?"

    play music music.ck1.v10.Track_Scene_40_1 fadein 2

    scene v10srds2 # FPP. Show Riley, smiling, mouth closed. She's still dirty.
    with dissolve

    u "I don't mind."

    scene v10srds2a # FPP. Same camera as v10srds2. Show Riley, smiling, mouth open. She's still dirty.
    with dissolve

    ri "Okay good, I'll be back soon."

    scene v10srds1a # TPP. Same camera as v10srds1. Show MC sitting on Riley's bed. Riley is walking out of the shot, still dirty.
    with dissolve

    pause 0.75

    scene v10srds1b # TPP. Same camera as v10srds1. Show MC sitting on Riley's bed, waiting. MC has a normal/bored expression.
    with dissolve

    u "(What to do, what to do?)"

    scene v10srds1c # TPP. Same camera as v10srds1. Show MC sitting on Riley's bed, waiting. He's looking at his phone, with a normal/bored expression.
    with fade

    u "(That was a long three minutes.)"

    scene v10srds1d # TPP. Same camera as v10srds1. Show MC sitting on Riley's bed, waiting. He's slumped over, looking bored/tired.
    with dissolve

    u "(Shit, am I getting tired?)"

    scene v10srds1e # TPP. Same camera as v10srds1. Show MC sitting on Riley's bed, waiting. He's running a hand through his hand/rubbing his face, with a bored/tired expression.
    with dissolve

    u "(Okay, she should be coming out soon.)"

    if CharacterService.is_fwb(riley)or reputation() == Reputations.CONFIDENT:
        label v10s40_galleryScene:
            if _in_replay:
                $ CharacterService.set_relationship(riley, Relationship.FWB)

    scene v10srds3 # FPP. Show Riley walking into her dorm room, wrapped in a towel, her hair down and still wet. She has a little smile, mouth open.
    with fade

    ri "I'm back."

    scene v10srds3a # FPP. Same camera as v10srds3, but focused more on Riley's towel/body. Show Riley wrapped in a towel, her hair down and still wet. She has a little smile, mouth closed.
    with dissolve

    u "You look uhm-"

    scene v10srds3b # FPP. Same camera as v10srds3. Show Riley wrapped in a towel, her hair down and still wet. She has a little smile, mouth open.
    with dissolve

    ri "*Chuckles* I forgot a change of clothes."

    if CharacterService.is_fwb(riley): # mc in a relationship with riley
        scene v10srds1f # TPP. Same camera as v10srds1. Show MC standing up from Riley's bed, smiling, mouth closed.
        with fade

        pause 0.50

        scene v10srds4 # TPP. MC and Riley standing face-to-face from the side. Both smiling, mouths closed. Riley is wrapped in a towel, her hair down and still wet.
        with dissolve

        menu:
            "Offer to turn around":
                scene v10srds3a
                with dissolve

                u "Go ahead and get dressed, I'll turn around."

                scene v10srds8 # FPP. MC turns around and looks at the wall.
                with dissolve

                ri "Awww, not even a little peek?"

                scene v10srds8
                with dissolve
                menu:
                    "Don't peek":
                        scene v10srds8
                        with dissolve

                        u "No ma'am."

                        scene v10srds8
                        with dissolve

                        ri "Such a gentleman."

                        scene v10srds6b # TPP. Same camera as v10srds6. Show MC and Riley laying next to each other in bed, dressed. Both smiling, Riley mouth open.
                        with fade

                        ri "Hey, can I ask you something?"

                        scene v10srds7b # FPP. Same camera as v10srds7. Show Riley next to MC, dressed in bed, face-to-face. Riley is smiling, mouth closed.
                        with dissolve

                        u "Sure, what's up?"

                        scene v10srds7c # FPP. Same camera as v10srds7. Show Riley next to MC, dressed in bed, face-to-face. Riley is smiling, mouth open.
                        with dissolve

                        ri "What would you do if you had a million dollars and you could either only spend it on yourself or only spend it on others?"

                        scene v10srds7b
                        with dissolve

                        u "Uhhh... I'm not sure."

                        scene v10srds7c
                        with dissolve

                        ri "Come on, you gotta choose one."

                        scene v10srds7b
                        with dissolve
                        menu:
                            "Myself":
                                scene v10srds7b
                                with dissolve

                                u "I'd spend it all on myself and then give away the stuff that I wanted to give."

                                scene v10srds7c
                                with dissolve

                                ri "What, no. *Laughs* You can't give away anything, quit trying to find loopholes. It's supposed to be a hard choice."

                                scene v10srds7b
                                with dissolve

                                u "Look at it as if I'm buying happiness."
                                
                                u "I get happy when I do things for others so if I buy others something or give something away that they want. then I'm also buying happiness for myself."

                                scene v10srds7c
                                with dissolve

                                ri "Haven't you ever heard you can't buy happiness? *Chuckles*"

                                scene v10srds7b
                                with dissolve

                                u "Well I just found a way."

                                scene v10srds7c
                                with dissolve

                                ri "You're crazy. *Laughs*"
                            
                            "Others":
                                scene v10srds7b
                                with dissolve

                                u "Easy, I'd give it all to one person and sign a contract with him saying he had to give half of it back to me."
                                
                                u "A quarter of it he had to spend on my family and friends, and the rest he could keep."

                                scene v10srds7c
                                with dissolve

                                ri "What, no. *Laughs* You can't make deals like that, quit trying to find loopholes. It's supposed to be a hard choice." 
                                
                                ri "Plus, why would you just have him also give you what you wanted to give away to your family and friends so you could do?"

                                scene v10srds7b
                                with dissolve

                                u "*Chuckles* That would make more sense."

                                scene v10srds7c
                                with dissolve

                                ri "Didn't think that one through. *Laughs*"

                        scene v10srds6b
                        with dissolve

                        ri "You have to get up early?"

                        scene v10srds7b
                        with dissolve

                        u "Yeah, I have something pretty major in the morning."

                        scene v10srds7c
                        with dissolve

                        ri "Don't you think you should go then?"

                        scene v10srds7b
                        with dissolve

                        u "Oh so you're kicking me out?"

                        scene v10srds7c
                        with dissolve

                        ri "Haha, no! I just don't want you to be super tired."

                        scene v10srds7b
                        with dissolve

                        u "Haha, yeah you're right. I should get out of here. I'll see you soon."

                        scene v10srds7c
                        with dissolve

                        ri "See ya."

                        $ renpy.end_replay()

                        jump v10_mc_pen_call # -Transition to Scene 41-

                    "Peek":
                        $ CharacterService.set_relationship(riley, Relationship.FWB)
                        $ sceneList.add("v10_riley")

                        scene v10srds1f
                        with dissolve

                        pause 0.50

                        scene v10srds4
                        with dissolve

                        pause 0.75

                        scene v10srds4a
                        with dissolve

                        pause 0.75

                        if is_censored:
                            call screen censored_popup("v10_mc_pen_call")

                        scene v10srds5
                        with dissolve

                        pause 0.75

                        scene v10srds5a
                        with dissolve

                        ri "Someone's confident."

                        scene v10srds5b
                        with dissolve

                        u "Come here."

                        lovense vibrate 2
                        lovense rotate 1
                        lovense suction 1
                        lovense thrust 1

                        scene v10srds5c
                        with dissolve

                        u "Lie down."

                        label v10s40_rileyReverse:
                            scene v10rircg
                            with dissolve
                            pause
                            u "You're so sexy."

                            ri "Squeeze my thighs."

                            lovense vibrate 4
                            lovense rotate 2
                            lovense suction 2
                            lovense thrust 2

                            scene v10rircgf
                            with dissolve
                            pause
                            ri "Oh god!"

                        scene v10riam
                        with dissolve
                        pause
                        ri "Oh fuck!"

                        scene v10riamf
                        with dissolve
                        pause
                        ri "[name]!"

                        ri "My turn."

                        label v10s40_rileyCowgirl:
                            lovense vibrate 5
                            lovense rotate 3
                            lovense suction 3
                            lovense thrust 3

                            scene v10riot
                            with dissolve
                            pause
                            u "Fuck that feels good."

                            ri "You like it huh?"

                            lovense vibrate 7
                            lovense rotate 4
                            lovense suction 3
                            lovense thrust 3

                            scene v10riotf
                            with dissolve
                            pause
                            u "Oh fuck, YESSS!"

                            u "I'm gonna cum."

                            ri "Go ahead."

                            scene v10riotf
                            with flash
                            pause

                        scene v10srds6
                        with fade

                        pause 0.75

                        hide screen v10s40_rileySexOverlay

                        lovense stop

                        scene v10srds6a
                        with dissolve

                        ri "That was nice."

                        scene v10srds7
                        with dissolve

                        u "It was."
            "Make a move":
                $ CharacterService.set_relationship(riley, Relationship.FWB)
                $ sceneList.add("v10_riley")

                scene v10srds4a # TPP. Same camera as v10srds4. Show MC and Riley. Both smiling, mouths closed. MC puts his hand on Riley's towel and drops it to the floor.
                with dissolve

                pause 0.75

                if is_censored:
                    call screen censored_popup("v10_mc_pen_call")

                scene v10srds5 # FPP. Show Riley naked, towel at her feet, smiling, mouth closed.
                with dissolve

                pause 0.75

                scene v10srds5a # FPP. Same camera as v10srds5. Show Riley naked, stepping forward and wrapping her arms around MC. Smiling, mouth open.
                with dissolve

                ri "I like where this is going."

                lovense vibrate 2
                lovense rotate 1
                lovense suction 1
                lovense thrust 1

                scene v10srds5b # FPP. Same camera as v10srds5. Show Riley naked, standing close with her arms wrapped around MC. Smiling, mouth closed.
                with dissolve

                u "Come here."

                scene v10srds5c # FPP. Same camera as v10srds5. Show Riley naked, smiling, mouth closed, stepping forward as though MC is leading her to the bed.
                with dissolve

                stop music fadeout 3
                play music music.ck1.v10.Track_Scene_40_2 fadein 2

                u "Lie down."
                
                image v10rircg = Movie(play="images/v10/Scene 40/v10rircg.webm", loop=True, image="images/v10/Scene 40/v10rircgStart.webp", start_image="images/v10/Scene 40/v10rircgStart.webp") 
                image v10rircgf = Movie(play="images/v10/Scene 40/v10rircgf.webm", loop=True, image="images/v10/Scene 40/v10rircgStart.webp", start_image="images/v10/Scene 40/v10rircgStart.webp")

                # -Move to position 2 (refer to Miro)-

                lovense vibrate 3
                lovense rotate 2
                lovense suction 2
                lovense thrust 2

                scene v10rircg
                with dissolve
                pause
                u "You're so sexy."

                ri "Squeeze my thighs."

                scene v10rircgf
                with dissolve
                pause
                ri "Oh god!"

                image v10riam = Movie(play="images/v10/Scene 40/v10riam.webm", loop=True, image="images/v10/Scene 40/v10riamStart.webp", start_image="images/v10/Scene 40/v10riamStart.webp")
                image v10riamf = Movie(play="images/v10/Scene 40/v10riamf.webm", loop=True, image="images/v10/Scene 40/v10riamStart.webp", start_image="images/v10/Scene 40/v10riamStart.webp")


                scene v10riam
                with dissolve
                pause
                ri "Oh fuck!"

                scene v10riamf
                with dissolve
                pause
                ri "[name]!"

                ri "My turn."

                image v10riot = Movie(play="images/v10/Scene 40/v10riot.webm", loop=True, image="images/v10/Scene 40/v10riotStart.webp", start_image="images/v10/Scene 40/v10riotStart.webp")
                image v10riotf = Movie(play="images/v10/Scene 40/v10riot.webm", loop=True, image="images/v10/Scene 40/v10riotStart.webp", start_image="images/v10/Scene 40/v10riotStart.webp")

                lovense vibrate 5
                lovense rotate 3
                lovense suction 3
                lovense thrust 3

                scene v10riot
                with dissolve
                pause
                u "Fuck that feels good."

                ri "You like it huh?"

                scene v10riotf
                with dissolve
                pause
                u "Oh fuck, YESSS!"

                u "I'm gonna cum."

                ri "Go ahead."

                scene v10riotf
                with flash
                pause

                scene v10srds6 # TPP. Show MC and Riley laying naked in bed together after sex. Both smiling, mouths closed.
                with fade

                pause 0.75

                lovense stop

                stop music fadeout 3
                play music music.ck1.v10.Track_Scene_40_3 fadein 2
                scene v10srds6a # TPP. Same camera as v10srds6. Show MC and Riley laying naked in bed together after sex. Both smiling, Riley mouth open.
                with dissolve

                ri "That was nice."

                scene v10srds7 # FPP. Show Riley next to MC, naked in bed, face-to-face. Riley is smiling, mouth closed.
                with dissolve

                u "It was."

                scene v10srds7a # FPP. Same camera as v10srds7. Show Riley next to MC, naked in bed, face-to-face. Riley is smiling, mouth open.
                with dissolve

                ri "Hey, can I ask you something?"

                scene v10srds7
                with dissolve

                u "Sure, what's up?"

                scene v10srds7a
                with dissolve

                ri "What would you do if you had a million dollars and you could either only spend it on yourself or only spend it on others?"

                scene v10srds7
                with dissolve

                u "Uhhh... I'm not sure."

                scene v10srds7a
                with dissolve

                ri "Come on, you gotta choose one."

                scene v10srds7
                with dissolve
                menu:
                    "Myself":
                        scene v10srds7
                        with dissolve

                        u "I'd spend it all on myself and then give away the stuff that I wanted to give."

                        scene v10srds7a
                        with dissolve

                        ri "What, no. *Laughs* You can't give away anything, quit trying to find loopholes. It's supposed to be a hard choice."

                        scene v10srds7
                        with dissolve

                        u "Look at it as if I'm buying happiness."
                            
                        u "I get happy when I do things for others so if I buy others something or give something away that they want, then I'm also buying happiness for myself."

                        scene v10srds7a
                        with dissolve

                        ri "Haven't you ever heard you can't buy happiness? *Chuckles*"

                        scene v10srds7
                        with dissolve

                        u "Well I just found a way."

                        scene v10srds7a
                        with dissolve

                        ri "You're crazy. *Laughs*"
                        
                    "Others":
                        scene v10srds7
                        with dissolve

                        u "Easy, I'd give it all to one person and sign a contract with him saying he had to give half of it back to me."
                            
                        u "A quarter of it he had to spend on my family and friends, and the rest he could keep."

                        scene v10srds7a
                        with dissolve

                        ri "What, no. *Laughs* You can't make deals like that, quit trying to find loopholes. It's supposed to be a hard choice."
                            
                        ri "Plus, why would you just have him also give you what you wanted to give away to your family and friends so you could do?"

                        scene v10srds7
                        with dissolve

                        u "*Chuckles* That would make more sense."

                        scene v10srds7a
                        with dissolve

                        ri "Didn't think that one through. *Laughs*"

        scene v10srds6a
        with dissolve

        ri "Don't you have to get up early tomorrow?"

        scene v10srds7
        with dissolve

        u "Yeah, I have something pretty major in the morning."

        scene v10srds7a
        with dissolve

        ri "Don't you think you should go then?"

        scene v10srds7
        with dissolve

        u "Oh so you're kicking me out?"

        scene v10srds7a
        with dissolve

        ri "Haha, no! I just don't want you to be super tired."

        scene v10srds7
        with dissolve

        u "Haha, yeah you're right. I should get out of here. I'll see you soon."

        scene v10srds7a
        with dissolve

        ri "See ya."
        $ renpy.end_replay()

        jump v10_mc_pen_call # -Transition to Scene 41-

    elif reputation() == Reputations.CONFIDENT: # -If not riley rs with KCT Confident #
        call screen reputation_popup

        scene v10srds3a
        with dissolve
        menu:
            "Make a move":
                $ CharacterService.set_relationship(riley, Relationship.FWB)
                $ sceneList.add("v10_riley")

                scene v10srds1f
                with dissolve

                pause 0.50

                scene v10srds4
                with dissolve

                pause 0.75

                scene v10srds4a
                with dissolve

                pause 0.75

                if is_censored:
                    call screen censored_popup("v10_mc_pen_call")

                scene v10srds5
                with dissolve

                pause 0.75

                scene v10srds5a
                with dissolve

                ri "Someone's confident."

                lovense vibrate 2
                lovense rotate 1
                lovense suction 1
                lovense thrust 1 

                scene v10srds5b
                with dissolve

                u "Come here."

                scene v10srds5c
                with dissolve

                stop music fadeout 3
                play music music.ck1.v10.Track_Scene_40_2 fadein 2

                u "Lie down."

                scene v10rircg
                with dissolve
                pause
                u "You're so sexy."

                ri "Squeeze my thighs."

                lovense vibrate 4
                lovense rotate 2
                lovense suction 2
                lovense thrust 2

                scene v10rircgf
                with dissolve
                pause
                ri "Oh god!"

                scene v10riam
                with dissolve
                pause
                ri "Oh fuck!"

                scene v10riamf
                with dissolve
                pause
                ri "[name]!"

                ri "My turn."

                scene v10riot
                with dissolve
                pause
                u "Fuck that feels good."

                ri "You like it huh?"

                lovense vibrate 6
                lovense rotate 4
                lovense suction 4
                lovense thrust 4

                scene v10riotf
                with dissolve
                pause
                u "Oh fuck, YESSS!"

                u "I'm gonna cum."

                ri "Go ahead."

                scene v10riotf
                with flash
                pause

                scene v10srds6a
                with dissolve

                ri "That was nice."
                
                lovense stop

                stop music fadeout 3
                play music music.ck1.v10.Track_Scene_40_3 fadein 2
                scene v10srds7
                with dissolve

                u "It was."

            "Offer to turn around":
                scene v10srds3a
                with dissolve

                u "Go ahead and get dressed, I'll turn around."

                scene v10srds8 # FPP. MC turns around and looks at the wall.
                with dissolve

                ri "Awww, not even a little peek?"

                scene v10srds8
                with dissolve
                menu:
                    "Don't peek":
                        scene v10srds8
                        with dissolve

                        u "No ma'am."

                        scene v10srds8
                        with dissolve

                        ri "Such a gentleman."

                        scene v10srds6b # TPP. Same camera as v10srds6. Show MC and Riley laying next to each other in bed, dressed. Both smiling, Riley mouth open.
                        with fade

                        ri "Hey, can I ask you something?"

                        scene v10srds7b # FPP. Same camera as v10srds7. Show Riley next to MC, dressed in bed, face-to-face. Riley is smiling, mouth closed.
                        with dissolve

                        u "Sure, what's up?"

                        scene v10srds7c # FPP. Same camera as v10srds7. Show Riley next to MC, dressed in bed, face-to-face. Riley is smiling, mouth open.
                        with dissolve

                        ri "What would you do if you had a million dollars and you could either only spend it on yourself or only spend it on others?"

                        scene v10srds7b
                        with dissolve

                        u "Uhhh... I'm not sure."

                        scene v10srds7c
                        with dissolve

                        ri "Come on, you gotta choose one."

                        scene v10srds7b
                        with dissolve
                        menu:
                            "Myself":
                                scene v10srds7b
                                with dissolve

                                u "I'd spend it all on myself and then give away the stuff that I wanted to give."

                                scene v10srds7c
                                with dissolve

                                ri "What, no. *Laughs* You can't give away anything, quit trying to find loopholes. It's supposed to be a hard choice."

                                scene v10srds7b
                                with dissolve

                                u "Look at it as if I'm buying happiness."
                                
                                u "I get happy when I do things for others so if I buy others something or give something away that they want. then I'm also buying happiness for myself."

                                scene v10srds7c
                                with dissolve

                                ri "Haven't you ever heard you can't buy happiness? *Chuckles*"

                                scene v10srds7b
                                with dissolve

                                u "Well I just found a way."

                                scene v10srds7c
                                with dissolve

                                ri "You're crazy. *Laughs*"
                            
                            "Others":
                                scene v10srds7b
                                with dissolve

                                u "Easy, I'd give it all to one person and sign a contract with him saying he had to give half of it back to me."
                                
                                u "A quarter of it he had to spend on my family and friends, and the rest he could keep."

                                scene v10srds7c
                                with dissolve

                                ri "What, no. *Laughs* You can't make deals like that, quit trying to find loopholes. It's supposed to be a hard choice." 
                                
                                ri "Plus, why would you just have him also give you what you wanted to give away to your family and friends so you could do?"

                                scene v10srds7b
                                with dissolve

                                u "*Chuckles* That would make more sense."

                                scene v10srds7c
                                with dissolve

                                ri "Didn't think that one through. *Laughs*"

                        scene v10srds6b
                        with dissolve

                        ri "You have to get up early?"

                        scene v10srds7b
                        with dissolve

                        u "Yeah, I have something pretty major in the morning."

                        scene v10srds7c
                        with dissolve

                        ri "Don't you think you should go then?"

                        scene v10srds7b
                        with dissolve

                        u "Oh so you're kicking me out?"

                        scene v10srds7c
                        with dissolve

                        ri "Haha, no! I just don't want you to be super tired."

                        scene v10srds7b
                        with dissolve

                        u "Haha, yeah you're right. I should get out of here. I'll see you soon."

                        scene v10srds7c
                        with dissolve

                        ri "See ya."

                        $ renpy.end_replay()

                        jump v10_mc_pen_call # -Transition to Scene 41-
                    
                    "Peek":
                        $ CharacterService.set_relationship(riley, Relationship.FWB)
                        $ sceneList.add("v10_riley")

                        scene v10srds1f
                        with dissolve

                        pause 0.50

                        scene v10srds4
                        with dissolve

                        pause 0.75

                        scene v10srds4a
                        with dissolve

                        pause 0.75

                        if is_censored:
                            call screen censored_popup("v10_mc_pen_call")

                        scene v10srds5
                        with dissolve

                        pause 0.75

                        scene v10srds5a
                        with dissolve

                        ri "Someone's confident."

                        lovense vibrate 2
                        lovense rotate 1
                        lovense suction 1
                        lovense thrust 1

                        scene v10srds5b
                        with dissolve

                        u "Come here."

                        scene v10srds5c
                        with dissolve

                        u "Lie down."

                        scene v10rircg
                        with dissolve
                        pause
                        u "You're so sexy."

                        ri "Squeeze my thighs."

                        lovense vibrate 4
                        lovense rotate 3
                        lovense suction 3
                        lovense thrust 3

                        scene v10rircgf
                        with dissolve
                        pause
                        ri "Oh god!"

                        scene v10riam
                        with dissolve
                        pause
                        ri "Oh fuck!"

                        scene v10riamf
                        with dissolve
                        pause
                        ri "[name]!"

                        ri "My turn."

                        scene v10riot
                        with dissolve
                        pause
                        u "Fuck that feels good."

                        ri "You like it huh?"
                        
                        lovense vibrate 7
                        lovense rotate 4
                        lovense suction 4
                        lovense thrust 4

                        scene v10riotf
                        with dissolve
                        pause
                        u "Oh fuck, YESSS!"

                        u "I'm gonna cum."

                        ri "Go ahead."

                        scene v10riotf
                        with flash
                        pause

                        scene v10srds6
                        with fade

                        pause 0.75

                        lovense stop
                        
                        scene v10srds6a
                        with dissolve

                        ri "That was nice."

                        scene v10srds7
                        with dissolve

                        u "It was."

        scene v10srds7a
        with dissolve

        ri "Hey, can I ask you something?"

        scene v10srds7
        with dissolve

        u "Sure, what's up?"

        scene v10srds7a
        with dissolve

        ri "What would you do if you had a million dollars and you could either only spend it on yourself or only spend it on others?"

        scene v10srds7
        with dissolve

        u "Uhhh... I'm not sure."

        scene v10srds7a
        with dissolve

        ri "Come on, you gotta choose one."

        scene v10srds7
        with dissolve
        menu:
            "Myself":
                scene v10srds7
                with dissolve

                u "I'd spend it all on myself and then give away the stuff that I wanted to give."

                scene v10srds7a
                with dissolve

                ri "What, no. *Laughs* You can't give away anything, quit trying to find loopholes. It's supposed to be a hard choice."

                scene v10srds7
                with dissolve

                u "Look at it as if I'm buying happiness."
                            
                u "I get happy when I do things for others so if I buy others something or give something away that they want, then I'm also buying happiness for myself."

                scene v10srds7a
                with dissolve

                ri "Haven't you ever heard you can't buy happiness? *Chuckles*"

                scene v10srds7
                with dissolve

                u "Well I just found a way."

                scene v10srds7a
                with dissolve

                ri "You're crazy. *Laughs*"

            "Others":
                scene v10srds7
                with dissolve

                u "Easy, I'd give it all to one person and sign a contract with him saying he had to give half of it back to me."
                            
                u "A quarter of it he had to spend on my family and friends, and the rest he could keep."

                scene v10srds7a
                with dissolve

                ri "What, no. *Laughs* You can't make deals like that, quit trying to find loopholes. It's supposed to be a hard choice."
                            
                ri "Plus, why would you just have him also give you what you wanted to give away to your family and friends so you could do?"

                scene v10srds7
                with dissolve

                u "*Chuckles* That would make more sense."

                scene v10srds7a
                with dissolve

                ri "Didn't think that one through. *Laughs*"

        scene v10srds6a
        with dissolve

        ri "You have to get up early?"

        scene v10srds7
        with dissolve

        u "Yeah, I have something pretty major in the morning."

        scene v10srds7a
        with dissolve

        ri "Don't you think you should go then?"

        scene v10srds7
        with dissolve

        u "Oh so you're kicking me out?"

        scene v10srds7a
        with dissolve

        ri "Haha, no! I just don't want you to be super tired."

        scene v10srds7
        with dissolve

        u "Haha, yeah you're right. I should get out of here. I'll see you soon."

        scene v10srds7a
        with dissolve

        ri "See ya."

        $ renpy.end_replay()

        jump v10_mc_pen_call # -Transition to Scene 41-

    else: # -If not riley rs without KCT Confident
        scene v10srds3a
        with dissolve
        menu:
            "Make a move":
                scene v10srds1f
                with dissolve

                pause 0.50

                scene v10srds4
                with dissolve

                pause 0.75

                scene v10srds4a
                with dissolve

                pause 0.75

                scene v10srds5d # FPP. Same camera as v10srds5. Show Riley naked, towel at her feet, with a surprised/shocked expression, mouth open. She's trying to cover her nakedness.
                with dissolve

                ri "WHOA, I didn't expect this from you!"

                scene v10srds5e # FPP. Same camera as v10srds5. Show Riley naked, towel at her feet, with a surprised/shocked expression, mouth closed. She's trying to cover her nakedness.
                with dissolve

                u "Was I reading things wrong?"

                scene v10srds5f # FPP. Same camera as v10srds5. Show Riley naked, towel at her feet, with a little frown/slight annoyed expression, mouth open. She's trying to cover her nakedness.
                with dissolve

                ri "I don't know, this just doesn't feel like the right time, maybe you should go."

                scene v10srds5g # FPP. Same camera as v10srds5. Show Riley naked, towel at her feet, with a little frown/slight annoyed expression, mouth closed. She's trying to cover her nakedness.
                with dissolve

                u "Uhm yeah, my bad. Bye. Sorry."

                scene v10srds3c # TPP. Same camera as v10srs3. Show MC leaving the dorm.
                with dissolve

                pause 0.50

                jump v10_mc_pen_call # -Transition to scene 41-
            
            "Offer to turn around":
                scene v10srds3a
                with dissolve

                u "Go ahead and get dressed, I'll turn around."

                scene v10srds8
                with dissolve

                ri "Alrighty."

                scene v10srds6b
                with fade

                ri "Hey, can I ask you something?"

                scene v10srds7b
                with dissolve

                u "Sure, what's up?"

                scene v10srds7c
                with dissolve

                ri "What would you do if you had a million dollars and you could either only spend it on yourself or only spend it on others?"

                scene v10srds7b
                with dissolve

                u "Uhhh... I'm not sure."

                scene v10srds7c
                with dissolve

                ri "Come on, you gotta choose one."

                scene v10srds7b
                with dissolve
                menu:
                    "Myself":
                        scene v10srds7b
                        with dissolve

                        u "I'd spend it all on myself and then give away the stuff that I wanted to give."

                        scene v10srds7c
                        with dissolve

                        ri "What, no. *Laughs* You can't give away anything, quit trying to find loopholes. It's supposed to be a hard choice."

                        scene v10srds7b
                        with dissolve

                        u "Look at it as if I'm buying happiness."
                        
                        u "I get happy when I do things for others so if I buy others something or give something away that they want, then I'm also buying happiness for myself."

                        scene v10srds7c
                        with dissolve

                        ri "Haven't you ever heard you can't buy happiness? *Chuckles*"

                        scene v10srds7b
                        with dissolve

                        u "Well I just found a way."

                        scene v10srds7c
                        with dissolve

                        ri "You're crazy. *Laughs*"
                    
                    "Others":
                        scene v10srds7b
                        with dissolve

                        u "Easy, I'd give it all to one person and sign a contract with him saying he had to give half of it back to me."
                        
                        u "A quarter of it he had to spend on my family and friends, and the rest he could keep."

                        scene v10srds7c
                        with dissolve

                        ri "What, no. *Laughs* You can't make deals like that, quit trying to find loopholes. It's supposed to be a hard choice."
                        
                        ri "Plus, why would you just have him also give you what you wanted to give away to your family and friends so you could do?"

                        scene v10srds7b
                        with dissolve

                        u "*Chuckles* That would make more sense."

                        scene v10srds7c
                        with dissolve

                        ri "Didn't think that one through. *Laughs*"

                scene v10srds6b
                with dissolve

                ri "Don't you have to get up early tomorrow?"

                scene v10srds7b
                with dissolve

                u "Yeah, I have something pretty major in the morning."

                scene v10srds7c
                with dissolve

                ri "Don't you think you should go then?"

                scene v10srds7b
                with dissolve

                u "Oh so you're kicking me out?"

                scene v10srds7c
                with dissolve

                ri "Haha, no! I just don't want you to be super tired."

                scene v10srds7b
                with dissolve

                u "Haha, yeah you're right. I should get out of here. I'll see you soon."

                scene v10srds7c
                with dissolve

                ri "See ya."
                stop music fadeout 3

                jump v10_mc_pen_call # -Transition to Scene 41-