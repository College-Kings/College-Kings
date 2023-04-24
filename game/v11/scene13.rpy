# SCENE 13: Aubrey sex on a plane
# Location: Airplane/Bathroom
# Characters: MC(outfit 1) /Ryan(outfit 1) /Aubrey(outfit 1) /Lauren (outfit 1)
# Time: Afternoon

label v11_aubrey_plane_sex:
    scene v11aub1 # TPP. Show Aubrey walking down the plane aisle, she has a slight smile, mouth closed (MC can be seen sitting in his seat in the backrgound, make sure the rest of the seating matches scene12)
    with fade
    play music "music/v11/Track Scene 13_1.mp3" fadein 2
    pause 0.75

    if CharacterService.is_friend(aubrey):
        jump v11_nora_chris_plane

    else:
        scene v11aub2 # TPP. Show Aubrey's hand with a piece of paper slammed on to MC's chest (show MC being startled)
        with dissolve

        pause 0.75

        scene v11aub3 # FPP. MC is sitting in his seat, looking at Aubrey walking away, down the aisle, make sure she's going towards the back of the plane
        with dissolve

        pause 0.75

        scene v11aub4 # FPP. MC sitting in his seat, looking at the note, the note reads: I'm bored, meet me in the bathroom. XOXO
        with dissolve

        u "(I'm bored, meet me in the bathroom. XOXO)"

        menu:
            "Go after her":
                label v11_aubrey_plane_sex_sg:
                $ sceneList.add("v11_aubrey")
                if CharacterService.is_girlfriend(lauren):
                    $ CharacterService.set_mood(lauren, Moods.MAD)
                    $ v11_lauren_caught_aubrey = True

                scene v11aub4
                with dissolve

                u "(This'll be fun.)"

                scene v11aub6 # TPP. Show MC walking towards the bathroom, MC is smiling, mouth closed
                with dissolve

                pause 0.75
                
                scene v11aub7 # TPP. Show MC standing in front of the bathroom, looking back at the aisle, slight smile, mouth closed
                with dissolve

                pause 0.75

                if config_censored:
                    call screen censored_popup("v11s13_nsfwSkipLabel1")

                stop music fadeout 3
                play music "music/v11/Track Scene 13_2.mp3" fadein 2
                scene v11aub8 # FPP. MC walks in the bathroom and sees Aubrey, she is naked, smiling seducrtively at him, mouth closed (Make sure it's not the plane one, use the other bathroom)
                with dissolve

                u "Oh wow, someone's moving fast."

                scene v11aub8a # FPP. Same as v11aub8, but Aubrey mouth open
                with dissolve

                au "I don't see the reason for small talk. Pants off!"

                scene v11aub9 # TPP. Show Aubrey removing MC's pants, both mouths closed
                with dissolve

                pause 1.25

                scene v11aub10 # TPP. Show MC sitting on the toilet, Aubrey standing in front of him
                with dissolve
                
                pause 1.25

                scene v11aub11 # FPP. MC is now sitting on the toilet, pants off, Aubrey is kneeled between his legs, looking at his dick
                with dissolve

                pause 1.25

                image v11aubbj = Movie(play="images/v11/Scene 13/v11aubbj.webm", loop=True, image="images/v11/Scene 13/v11aubbjStart.webp", start_image="images/v11/Scene 13/v11aubbjStart.webp") # Aubrey giving mc head
                image v11aubbjf = Movie(play="images/v11/Scene 13/v11aubbjFPPf.webm", loop=True, image="images/v11/Scene 13/v11aubbjStart.webp", start_image="images/v11/Scene 13/v11aubbjStart.webp") # Aubrey giving mc head sped up
                image v11aubbjtpp = Movie(play="images/v11/Scene 13/v11aubbjtpp.webm", loop=True, image="images/v11/Scene 13/v11aubbjtppStart.webp", start_image="images/v11/Scene 13/v11aubbjtppStart.webp") # Aubrey giving mc head sped up
                image v11aubbjtppf = Movie(play="images/v11/Scene 13/v11aubbjtppf.webm", loop=True, image="images/v11/Scene 13/v11aubbjtppStart.webp", start_image="images/v11/Scene 13/v11aubbjtppStart.webp") # Aubrey giving mc head sped up

                image v11aubo = Movie(play="images/v11/Scene 13/v11auboTPP1.webm", loop=True, image="images/v11/Scene 13/v11auboTPP1Start.webp", start_image="images/v11/Scene 13/v11auboTPP1Start.webp") # Aubrey bent over the toilet fucking mc
                image v11aubof = Movie(play="images/v11/Scene 13/v11auboTPP1f.webm", loop=True, image="images/v11/Scene 13/v11auboTPP1Start.webp", start_image="images/v11/Scene 13/v11auboTPP1Start.webp") # Aubrey bent over the toilet fucking mc sped up 
                image v11aubo2 = Movie(play="images/v11/Scene 13/v11auboTPP2.webm", loop=True, image="images/v11/Scene 13/v11auboTPP2Start.webp", start_image="images/v11/Scene 13/v11auboTPP2Start.webp") # Aubrey bent over the toilet fucking mc
                image v11aubo2f = Movie(play="images/v11/Scene 13/v11auboTPP2f.webm", loop=True, image="images/v11/Scene 13/v11auboTPP2Start.webp", start_image="images/v11/Scene 13/v11auboTPP2Start.webp") # Aubrey bent over the toilet fucking mc sped up 

                image v11aubll = Movie(play="images/v11/Scene 13/v11aubllTPP.webm", loop=True, image="images/v11/Scene 13/v11aubllTPPStart.webp", start_image="images/v11/Scene 13/v11aubllTPPStart.webp") # Aubrey and MC standing sex
                image v11aubllf = Movie(play="images/v11/Scene 13/v11aubllTPPf.webm", loop=True, image="images/v11/Scene 13/v11aubllTPPStart.webp", start_image="images/v11/Scene 13/v11aubllTPPStart.webp") # Aubrey and MC standing sex sped up
                image v11aubll2 = Movie(play="images/v11/Scene 13/v11aubllTPP2.webm", loop=True, image="images/v11/Scene 13/v11aubllTPP2Start.webp", start_image="images/v11/Scene 13/v11aubllTPP2Start.webp") # Aubrey and MC standing sex
                image v11aubll2f = Movie(play="images/v11/Scene 13/v11aubllTPP2f.webm", loop=True, image="images/v11/Scene 13/v11aubllTPP2Start.webp", start_image="images/v11/Scene 13/v11aubllTPP2Start.webp") # Aubrey and MC standing sex sped up

                image v11auban = Movie(play="images/v11/Scene 13/v11auanTPP1.webm", loop=True, image="images/v11/Scene 13/v11auanTPP1Start.webp", start_image="images/v11/Scene 13/v11auanTPP1Start.webp") # Aubrey and MC anal doggy
                image v11aubanf = Movie(play="images/v11/Scene 13/v11auanTPP1f.webm", loop=True, image="images/v11/Scene 13/v11auanTPP1Start.webp", start_image="images/v11/Scene 13/v11auanTPP1Start.webp") # Aubrey and MC anal doggy sped up

                scene v11aubbj # Ignore as animation
                with dissolve
                pause

                u "Oh fuck!"

                scene v11aubbjf
                with dissolve
                pause

                u "Damn Aubrey!"

                scene v11aubbjtpp # Ignore as animation
                with dissolve
                pause

                u "You... Oh god."

                scene v11aubbjtppf 
                with dissolve
                pause

                u "Mhmmmm..."

                scene v11aub12 # FPP. Aubrey stops giving MC head, she is looking up at him, smiling, mouth closed
                with dissolve

                pause 1.25

                scene v11aub13 # TPP. Show MC removing his shirt, Aubrey is standing, helping him remove his shirt
                with dissolve

                pause 1.25

                scene v11aub13a # TPP. Same cam as v11aub13, MC turns Aubrey around, both smiling, mouth closed
                with dissolve

                pause 1.25

                scene v11aub13b # TPP. Same cam as v11aub13, MC is bending Aubrey over the toilet
                with dissolve

                pause 1.25

                scene v11aub14 # TPP. MC is now looking at Aubrey bent over with her hands on the toilet, camera to the side
                with dissolve

                pause 1.25

                scene v11aubo # Ignore as animation
                with dissolve
                pause 

                au "Damn [name]!"

                scene v11aubof # Ignore as animation
                with dissolve
                pause

                u "Are we being too loud?"

                scene v11aubo2
                with dissolve
                pause

                au "We're fine, don't stop."

                scene v11aubo2f
                with dissolve
                pause

                u "Damn, you feel so fucking good!"

                au "Fuuuuuuck!"

                # -Transition images of MC turning Aubrey around and doing standing missionary-
                scene v11aub15 # TPP. Show Aubrey standing up, with her back to MC (aubrey facing camera), both smiling, mouths closed
                with dissolve

                pause 1.25

                scene v11aub15a # TPP. Same cam as v11aub15, MC grabbing Aubrey's thigh and raising her leg, MC is also grabbing her waist, both smiling, mouths closed
                with dissolve

                pause 1.25
                
                scene v11aubll # Ignore as animation
                with dissolve
                pause

                au "*Moans*"

                au "Oh fuck!"

                play sound "sounds/knock.mp3"
                
                u "Oh shit..."

                scene v11aubllf # Ignore as animation
                with dissolve
                pause

                au "They can wait, I'm almost there."

                scene v11aubll2
                with dissolve
                pause

                au "*Moans*"

                scene v11aub16 # TPP. Show Lauren standing outside the bathroom, her ears are next to the door, mouth open, slightly worried (plane corridor)
                with dissolve

                la "Uhm... Are you okay in there?"

                scene v11aubll2f
                with dissolve
                pause

                u "This feels fucking amazing."

                scene v11aub26 # FPP. Show aubrey now standing infront of the toilet back to camera
                with dissolve

                pause 1

                scene v11aub26a # FPP. Show aubrey now bent over the toilet, mc's hand on her waist, aubrey's hands on the toilet.
                with dissolve

                pause 1
                
                scene v11auban
                with dissolve
                pause

                au "*Moans*"

                au "Oh fuck!"

                scene v11aubanf
                with dissolve
                pause

                au "Damn [name]!"
                
                if v11_lauren_caught_aubrey:
                    u "Oh fuck it's Lauren!"

                else:
                    u "Is that Lauren?"

                au "Oh God I'm cumming!"

                scene v11aub16
                with dissolve

                la "Did you say come in?"

                scene v11aub17 # FPP. MC is looking at the door, door slightly open, can not see Lauren yet (Make sure this render is using the plane bathroom instead of the other one)
                with dissolve

                play sound "sounds/cardooropen.mp3"

                pause 0.75
                stop music fadeout 3

                scene v11aub17c # FPP. Same as v11aub17a, but Lauren is surprised, mouth open
                with dissolve

                if v11_lauren_caught_aubrey:
                    pause 0.75
                    
                    scene v11aub17a # FPP. Same cam as v11aub17, door fully open, Lauren is very angry, mouth open
                    with dissolve

                    la "[name], what are you doing!?"

                    scene v11aub17b # FPP. Same as v11aub17a, Lauren is very angry, mouth closed
                    with dissolve
                    play music "music/v11/Track Scene 13_1.mp3" fadein 2
                    u "I'm just helping her with her uh..."

                    scene v11aub17a
                    with dissolve

                    la "How could you do this to me?! WHAT THE FUCK???"

                    scene v11aub17
                    with dissolve

                    play sound "sounds/doorclose.mp3"

                    pause 0.75
                    
                    scene v11aub18 # FPP. Aubrey is now standing in front of MC, in the same place as v11aub4, Aubrey mouth open, slight smile (This one is back to the bathroom location used prior)
                    with dissolve

                    au "Okay, I know she's pissed, but that was kind of exciting."

                else: # Lauren not dating MC
                    la "Oh... oh shit. Sorry."
                    play music "music/v11/Track Scene 13_1.mp3" fadein 2
                    scene v11aub17
                    with dissolve

                    play sound "sounds/doorclose.mp3"

                    pause 0.75

                    scene v11aub18
                    with dissolve

                    au "That was kind of exciting..."
                $ renpy.end_replay()

                menu:
                    "No, not really":
                        $ reputation.add_point(RepComponent.TROUBLEMAKER)
                        scene v11aub18a # FPP. Same as v11aub18, Aubrey mouth closed, slightly smiling
                        with dissolve

                        u "Uhm... I'm not sure I agree."
                        
                    "Kinda hot":
                        $ reputation.add_point(RepComponent.BOYFRIEND)
                        scene v11aub18a
                        with dissolve

                        u "*Chuckles* It was kinda hot."

                        if v11_lauren_caught_aubrey:
                            u "But now I'm gonna have to talk to her after the flight... fuck me."

                scene v11aub19 # TPP. Shot of MC putting his shirt on, Aubrey is pulling her shorts up, still no top
                with dissolve

                pause 1.25

                scene v11aub19a # TPP. Same cam as v11aub8, Aubrey is putting her top on (still showing her tits) and MC is zipping his pants
                with dissolve

                pause 1.25

                label v11s13_nsfwSkipLabel1:

                scene v11aub20 # FPP. Aubrey is poking her head through the bathroom door, MC is still inside (This render should use the plane bathroom)
                with dissolve

                pause 1.25

                scene v11aub20a # FPP. Same as v11aub20, Aubrey is now looking at MC, she is still at the door, Aubrey mouth open, seductive smile
                with dissolve

                au "Well, thanks for the... quick fix. *Chuckles*"

                scene v11aub17d # FPP. Same camera as v11aub6, Aubrey is leaving the door
                with dissolve

                pause 1

                scene v11aub17
                with dissolve

                pause 0.75

                scene v11aub21 # TPP. Show MC heading for the bathroom door (camera inside bathroom)
                with dissolve

                pause 0.75

                scene v11aub22 # FPP. MC is peeking through the bathroom door, he is looking down the aisle (make sure people are seated the same way as the other plane scenes)
                with dissolve
                
                pause 0.75

                scene v11aub23 # FPP. MC is now walking through the aisle, he is walking towards his seat
                with dissolve

                pause 0.75

                scene v11aub24 # FPP. MC is standing next to his seat, he is looking at Ryan, Ryan is looking through the window
                with dissolve

                pause 0.75

                scene v11aub25 # TPP. Show MC sitting in his seat, MC mouth closed, slight smile
                with dissolve

                pause 0.75

                scene v11aub5b
                with dissolve

                if v11_lauren_caught_aubrey:
                    ry "Lauren's pissed."

                    scene v11aub5a
                    with dissolve

                    u "I know."

                    scene v11aub5b
                    with dissolve

                    ry "Why?"

                else:
                    ry "What just happened?"

                scene v11aub5a
                with dissolve

                u "Long story."

                scene v11aub5b
                with dissolve

                ry "I doubt it's that long."

                scene v11aub5a
                with dissolve

                u "Why'd you say it like that?"

                scene v11aub5b
                with dissolve

                ry "Like what?"

                scene v11aub5a
                with dissolve

                u "Like how you said it."

                scene v11aub5d # FPP. Same as v11aub5, Ryan has a slight grin, mouth open
                with dissolve

                ry "Cause I bet you got a short story. *Chuckles*"

                scene v11aub5a
                with dissolve

                u "Emily didn't think it was short."

                scene v11aub5e # FPP. Same as v11aub5, Ryan looks at MC slightly pissed, mouth slightly open
                with dissolve

                ry "Pfff."

                scene v11aub5c
                with dissolve

                pause 0.75
                stop music fadeout 3
                jump v11_nora_chris_plane

            "Don't go after her":
                $ v11s13_rejected_aubrey = True
                scene v11aub4
                with dissolve

                u "(What? *Chuckles* She's crazy. Not on a fucking plane.)"

                scene v11aub5 # FPP. MC is sitting next to Ryan, Ryan and MC looking at each other, Ryan mouth slightly open, neutral look
                with dissolve

                ry "Hmph..."

                scene v11aub5a # FPP. Same as v11aub5, Ryan mouth closed, neutral look
                with dissolve

                u "What?"

                scene v11aub5b # FPP. Same as v11aub5, mouth normal open, neutral look
                with dissolve

                ry "Nothing."

                scene v11aub5c # FPP. Same as v11aub15, Ryan now looking at his windows
                with dissolve

                pause 0.75

                jump v11_nora_chris_plane