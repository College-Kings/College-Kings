# SCENE 30: MC and Chloe at the Gym
# Location: School gym
# Characters: MC (Outfit 3), Chloe (Outfit 5)
# Time: Afternoon

label v10_chloe_gym:
    play music music.ck1.v10.Track_Scene_30_1 fadein 2
    # MC and Chloe are in the gym which happens to be empty, the lights are on and the door is unlocked
    scene v10chg1 # TPP Show MC and Chloe at door to gym, light are on, MC is pulling open the door
    with fade

    pause 0.5

    scene v10chg2 # FPP Show Chloe in gym smiling, mouth closed
    with fade

    u "Well look at that, it must be our lucky day."

    scene v10chg2a # FPP Same angle as v10chg2, Chloe's eyebrow raised and mouth open
    with dissolve

    cl "Ready to lose?"

    scene v10chg2b # FPP Same angle and expression as v10chg2a, Chloe mouth closed
    with dissolve

    u "Lose?"

    scene v10chg2a
    with dissolve

    cl "It's been quite a minute since we played, I've been practicing, but I doubt you have. *Chuckles*"

    scene v10chg2
    with dissolve

    u "Pros don't need to practice! *Laughs*"

    scene v10chg2c # FPP Same angle and expression as v10chg2, Chloe mouth open
    with dissolve

    cl "Someone's in a... confident mood."

    scene v10chg2
    with dissolve

    u "What can I say? Life is like a video game and I'm the main character."

    scene v10chg2d # FPP Same angle as v10chg2, Chloe laughing with mouth open
    with dissolve

    cl "*Laughs* Let's go big shot!"

    scene v10chg2c
    with dissolve

    cl "Good luck!"

    scene v10chg2b
    with dissolve

    u "I'm not the one that needs it!"

    # MC and Chloe enter into a time passing montage as the play their game, 4 images with two per character and dialog lines in order

    scene v10chg3 # TPP Show MC playing volleyball, bump-setting ball
    with fade

    cl "Okay, stop cheating!"

    scene v10chg4 # TPP Show Chloe playing volleyball, returning the ball
    with fade

    u "Someone should've practiced a bit more. *Laughs*"

    scene v10chg3a # TPP Same angle as v10chg3, MC barely hitting the ball before it hits the ground
    with fade

    cl "I got you now!"

    scene v10chg4a # TPP Same angle as v10chg4, Show Chloe slamming the ball down over the net
    with fade

    pause 0.5

    scene v10chg3b # TPP Same angle as v10chg3, show MC blocking Chloe's shot
    with fade

    pause 0.5

    scene v10chg5 # FPP Show volleyball hitting the floor of the gym close up
    with fade

    pause 0.5

    scene v10chg2e # FPP Same angle as v10chg2, Chloe looking slightly disappointed, mouth closed
    with fade

    u "And that's the game!"

    scene v10chg2c
    with dissolve

    cl "Okay, when did you learn that? You weren't playing like that last time."

    scene v10chg2
    with dissolve

    u "I felt the need to dominate. *Laughs*"

    scene v10chg2a
    with dissolve

    cl "I noticed."

    scene v10chg2b
    with dissolve

    u "So what's my reward?"

    scene v10chg2c
    with dissolve

    cl "Is playing me not enough?"

    scene v10chg2
    with dissolve

    u "What's the point of a rematch if there's no reward?"

    scene v10chg2a
    with dissolve

    cl "What do you have in mind?"

    scene v10chg2b
    with dissolve

    u "I like to be surprised."

    scene v10chg2c
    with dissolve

    cl "Anything you don't like?"

    scene v10chg2
    with dissolve

    u "I have a whole list."

    scene v10chg2d
    with dissolve

    cl "Haha, great! Give me that so I know what my options are. *Laughs*"

    scene v10chg2
    with dissolve

    u "*Laughs*"

    scene v10chg6 # FPP Show Chloe bending over to pick up the volleyball off of the floor
    with dissolve

    u "(Damn...)"

    if CharacterService.is_fwb(chloe): # If in a relationship with Chloe
        # -Event1 Look closer-
        menu:
            "Look closer":
                label v10s30_galleryScene:
                $ sceneList.add("v10_chloe")
                scene v10chg6a # FPP Same angle as c10chg6a, Close up shot of Chloe's butt while she's bending over
                with dissolve

                pause 0.5
               
                scene v10chg6b # FPP Same angle as c10chg6b, Chloe now standing, giving MC a suspicious look with mouth open
                with dissolve

                cl "Were you just... you were trying to look up my shorts! You really are naughty! At least tell me you liked what you saw."

                scene v10chg2
                with dissolve

                u "I'd run that back on repeat."

                play sound sound.kiss

                scene v10chg7 # TPP In gym, show Chloe kissing MC
                with dissolve

                pause 0.5

                scene v10chg2c
                with dissolve

                cl "Good answer. You know, I just may have an idea for your little reward."

                # -Chloe grabs MC's hand and leads him to the locker room, same one she was in during hoco-
                scene v10chg8 # FPP Show Chloe holding MC's hand, pulling him toward the locker room
                with dissolve

                u "I like where this is going."
                
                scene v10chg9 # TPP MC and Chloe in locker room, both straddling a bench, facing each-other, both smiling with mouths closed
                with fade

                pause 0.5
                stop music fadeout 3
                play music music.ck1.v8.Track_Scene_30 fadein 2
                scene v10chg9a # TPP Same angle as v10chg8, Chloe looking seductive with mouth open
                with dissolve

                cl "Come here."

                image v10chgmo = Movie(play="images/v10/Scene 30/v10chgmo.webm", loop=True, image="images/v10/Scene 30/v10chgmoStart.webp", start_image="images/v10/Scene 30/v10chgmoStart.webp") # TPP MC and Chloe start making out on the locker room bench
                image v10chgmof = Movie(play="images/v10/Scene 30/v10chgmof.webm", loop=True, image="images/v10/Scene 30/v10chgmoStart.webp", start_image="images/v10/Scene 30/v10chgmoStart.webp")

                scene v10chgmo # MC and Chloe start making out on the locker room bench
                with dissolve
                pause

                scene v10chgmof
                with dissolve
                pause

                scene v10chg9b # TPP Same angle as v10chg9, MC pulling Chloe's thigh toward himself while pushing her shoulder back to lay her down on the bench
                with dissolve

                pause 0.5

                if is_censored:
                    call screen censored_popup("v10s30_nsfwSkipLabel1")

                scene v10chg10 # FPP Close up on Chloe, laying on her back on the bench, small smile and mouth closed, mc reaching to pull off her top.
                with dissolve

                u "Think you deserve a little reward too."

                # -Plenty of foreplay, MC kissing her body up and down after removing her shirt-
                image v10chgfp = Movie(play="images/v10/Scene 30/v10chgfp.webm", loop=True, image="images/v10/Scene 30/v10chgfpStart.webp", start_image="images/v10/Scene 30/v10chgfpStart.webp") # TPP MC removes Chloe's shirt while kissing up and down her body, Chloe closes her eyes and bites her lower lip
                image v10chgfpf = Movie(play="images/v10/Scene 30/v10chgfpf.webm", loop=True, image="images/v10/Scene 30/v10chgfpStart.webp", start_image="images/v10/Scene 30/v10chgfpStart.webp")

                scene v10chgfp # MC works some foreplay, kissing Chloe's body
                with dissolve

                cl "Oh, [name]!"

                scene v10chgfpf
                with dissolve
                
                cl "It feels so good!"

                scene v10chg10a # FPP Show Chloe laying on locker room bench, MC pulling off her shorts and panties
                with dissolve

                pause 0.5

                show screen v10s30_chloeSexOverlay

                image v10chgeo = Movie(play="images/v10/Scene 30/v10chgeo.webm", loop=True, image="images/v10/Scene 30/v10chgeoStart.webp", start_image="images/v10/Scene 30/v10chgeoStart.webp") # TPP Close up as MC is eating her out
                image v10chgeof = Movie(play="images/v10/Scene 30/v10chgeof.webm", loop=True, image="images/v10/Scene 30/v10chgeoStart.webp", start_image="images/v10/Scene 30/v10chgeoStart.webp")

                label v10s30_chloeLicking:
                    scene v10chgeo # MC eating Chloe out
                    with dissolve
                    
                    cl "I'm gonna cum!"

                    scene v10chgeof
                    with dissolve
                    
                    cl "Oh my god, I'm cumming!"

                    scene v10chg9c # TPP Same angle as v10chg9, MC's head between Chloe's legs while she grips the sides of the bench, back arched, face looking up, eyes closed
                    with dissolve

                    pause 0.5

                scene v10chg9d # TPP Same angle as v10chg9, Chloe sitting up and laying MC back on the bench just like he did with her, Chloe's mouth open
                with dissolve

                cl "Your turn."

                scene v10chg10b # FPP Looking down at Chloe, who is pulling down MC's jeans and exposing his penis
                with dissolve

                u "Oh God!"

                label v10s30_chloeBlowjob:
                    scene v10chg10c # FPP Same angle as v10chg10b, Chloe moving to give MC a blowjob
                    with dissolve

                    u "I need to win games more often."

                    image v10chgbj = Movie(play="images/v10/Scene 30/v10chgbj.webm", loop=True, image="images/v10/Scene 30/v10chgbjStart.webp", start_image="images/v10/Scene 30/v10chgbjStart.webp") # FPP Chloe giving MC a blowjob
                    image v10chgbjf = Movie(play="images/v10/Scene 30/v10chgbjf.webm", loop=True, image="images/v10/Scene 30/v10chgbjStart.webp", start_image="images/v10/Scene 30/v10chgbjStart.webp")

                    scene v10chgbj # Chloe giving MC a blowjob
                    with dissolve

                    u "This is... oh fuck."

                    scene v10chgbjf
                    with dissolve

                    u "I'm gonna cum."

                    scene v10chg10d # FPP Same angle as v10chg10b, MC holding Chloe's head with both hands while he cums in her mouth
                    with dissolve

                    u "Ahh fuck... I'm cumming!"

                    scene v10chg10e # FPP Same angle as v10chg10b, Chloe smiling, mouth open, cum in her mouth
                    with dissolve

                    cl "Mmm..."

                    scene v10chg10f # FPP Same angle as v10chg10b, Chloe smiling, mouth closed
                    with dissolve

                    cl "*gulp*"

                hide screen v10s30_chloeSexOverlay

                scene v10chg10g # FPP Same angle as v10chg10b, Chloe smiling, mouth open
                with dissolve

                cl "How was that for a reward?"

                scene v10chg10g
                with dissolve

                u "Couldn't have been better."

                scene v10chg11 # FPP Show Chloe, in locker room, standing and getting dressed
                with dissolve

                cl "As much as I would love to stay and chat, I need to go study. Hope you don't feel like I'm rushing off."

                scene v10chg11a # FPP Same angle as v10chg11, Chloe, now dressed, smiling with mouth closed
                with fade

                u "Nah you're good, I need to study too honestly."

                scene v10chg12 # TPP Show Chloe kissing MC in locker room
                with dissolve

                pause 0.5

                label v10s30_nsfwSkipLabel1:
                    scene v10chg11b # TPP Same angle and expression as v10chg11a, Chloe's mouth open
                    with dissolve

                    cl "Okay good, see you around."
                    $ renpy.end_replay()

            "Don't risk it":
                scene v10chg6
                with dissolve

                u "(Just here for a volleyball game.)"

                scene v10chg2d
                with fade

                cl "I'm glad you and I had a chance to settle that rematch, even though you must have done something tricky to win. *Laughs*"

                scene v10chg2b
                with dissolve

                u "Not saying I did or didn't have a trick up my sleeve, but even if I did a magician never reveals his secret. *Laughs*"

                scene v10chg2c
                with dissolve

                cl "Ha, well look I'm gonna run. I want to get some studying done before it's too late."

                scene v10chg2
                with dissolve

                u "Same here, I'll see you around."

                # Chloe kisses MC
                scene v10chg7
                with dissolve

                pause 0.5

    else: # If Chloe likes MC but no relationship
        menu:
            "Look closer":
                scene v10chg6a
                with dissolve

                pause 0.5

                scene v10chg6b
                with dissolve

                cl "Did I just catch you checking me out? Someone must be in a mood. *Chuckles*"

                scene v10chg2
                with dissolve

                u "What can I say, the view was nice."

                scene v10chg2c
                with dissolve

                cl "Ha, well too bad I can't entertain you more, I need to go study before it gets too late."

                scene v10chg2
                with dissolve

                u "Ha, me too."

                scene v10chg2c
                with dissolve

                cl "See you around [name]."

                scene v10chg2
                with dissolve

                u "See ya."

            "Don't risk it":
                scene v10chg6
                with dissolve

                u "(Just here for a volleyball game.)"

                scene v10chg2d
                with fade

                cl "I'm glad you and I had a chance to settle that rematch, even though you must have done something tricky to win. *Laughs*"

                scene v10chg2b
                with dissolve

                u "Not saying I did or didn't have a trick up my sleeve, but even if I did a magician never reveals his secret. *Laughs*"

                scene v10chg2c
                with dissolve

                cl "Ha, well look I'm gonna run. I want to get some studying in before it's too late."

                scene v10chg2
                with dissolve

                u "Same here, I'll see you around."

    stop music fadeout 3
# -Transition to Scene 31-
jump v10_late_alley