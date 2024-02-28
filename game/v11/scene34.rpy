# SCENE 34: Chloe and MC car dealership
# Location: Car dealership, streets of london 
# Characters: MC (Outfit 9), Chloe (Outfit 2), Salesman (Outfit ask lew), Mr Lee (Outfit 1)
# Time: Day

label v11_cardealership:
    $ v11_dealership = True

    scene v11cd1 # TPP. Shows MC and Chloe getting into the car dealership
    with fade
    play music music.ck1.v11.Track_Scene_3 fadein 2
    pause 0.75

    scene v11cd2 # TPP. MC is looking for a car salesman, spotting one, him looking back at them
    with dissolve

    pause 0.75
    
    scene v11cd3 # FPP. The car salesman comes in MCs and Chloe's direction, mouth opened 
    with dissolve

    csa "Hello there, how may I help you?"

    scene v11cd3a # FPP. looking at chloe and the car salesman, chloe's mouth is opened
    with dissolve

    cl "Oh hi, I'm in the market for a new sports car. Something worthy of being called an eye catcher."

    scene v11cd3b # FPP. same as 3a, chloe's mouth is closed and the car salesman is opened
    with dissolve

    csa "Ahh I see, anything particular such as the brand?"

    scene v11cd3a 
    with dissolve

    cl "Honey? Any particular brand?"

    scene v11cd4 # TPP. MC looking confused, mouth closed
    with dissolve

    u "(Honey?)"

    scene v11cd3c # FPP. Looking at chloe and the car salesman, mouth closed
    with dissolve

    u "Um, whatever you want, we'll get."

    scene v11cd3d # FPP. Same as 3b, smile on the carsalesman face, mouth opened. 
    with dissolve

    csa "Such a beautiful couple."
    
    scene v11cd3a 
    with dissolve

    cl "Thank you, I wouldn't mind looking at some of your German options."

    scene v11cd3b
    with dissolve

    csa "Well ma'am, it's your lucky day. We just had an import of the highest quality. A German model. You struck gold finding this man and now lady luck is shining on you once again."

    scene v11cd3e # FPP. chloe smiling, chloe's mouth opened 
    with dissolve

    cl "*Chuckles* We are blessed, that is true."

    scene v11cd3b
    with dissolve

    csa "How wonderful. Allow me to bring the vehicle around."

    scene v11cd5 # FPP. Carsalesman leaving the frame, back turned to camera
    with dissolve

    pause 0.75

    scene v11cd6 # FPP. MC looking at chloe, mouth closed
    with dissolve

    u "\"Honey\"? *Chuckles*"

    scene v11cd6a # FPP. Chloe smiling, mouth opened
    with dissolve

    cl "What? *Chuckles* I just thought we could have a little fun."

    if CharacterService.is_fwb(chloe) or CharacterService.is_girlfriend(chloe):
        scene v11cd7 # TPP. chloe whispers in MCs ear, MC looks surprised, MCs mouth closed chloe's mouth opened
        with dissolve
        
        cl "Plus who knows, I may get used to calling you that..."

    scene v11cd6
    with dissolve

    u "Guess I'll have to play along."

    scene v11cd6b # FPP. Chloe has a serious face, mouth opened
    with dissolve

    cl "Just a warning, I get very serious when I get into character."

    scene v11cd6
    with dissolve

    u "*Chuckles* We'll see about that."

    scene v11cd8 # TPP. Shows the car arriving at the front door
    with dissolve

    play sound sound.car_brake

    pause 1.75

    scene v11cd9 # FPP. Shows the sale rep coming in MCs and chloes direction, mouth opened
    with dissolve

    csa "The car is ready, however, I forgot there's a bit of information I must collect from you first."

    scene v11cd9a # FPP. Angle change, they are now standing in front of the main entrance doors, MC looking at chloe and the carsalesman, chloe's mouth opened
    with dissolve

    cl "Of course."

    scene v11cd9b # FPP. Same as 9a, chloe's mouth closed car salesman mouth opened
    with dissolve

    csa "Whose name will the vehicle's name be in?"

    scene v11cd9c # FPP. same as 9b, mouth closed
    with dissolve

    u "My wife's."

    scene v11cd10 # TPP. MC wraps his arms around Chloe's waist
    with dissolve

    pause 0.75

    scene v11cd11 # FPP. MCs arm around chloes waist still, looking at car saleswoman, mouth closed
    with dissolve

    u "Her car, her name."

    scene v11cd11a # FPP. same as 11, car salesman mouth opened
    with dissolve

    csa "Perfect. And your name?"

    scene v11cd11b # FPP. looking at chloe, mouth opened
    with dissolve

    cl "Chloe Moralez."

    scene v11cd11a
    with dissolve

    csa "Perfect, and I assume you are tourists?"

    scene v11cd11
    with dissolve

    u "Correct."

    scene v11cd12 # TPP. the salesman takes chloe and MC out of the store, mouth closed
    with dissolve

    pause 0.75

    scene v11cd13 # FPP. the salesman points to the direction they are supposed to take, salesman mouth opened
    with dissolve

    csa "Okay, so local streets around the dealership are the test driving route. Normally, there are a few more questions and details to run through, but I'm sure you two will be just fine. Here are the keys, sir."
    
    scene v11cd14 # FPP. MC looks at the salesman, mouth closed
    with dissolve

    u "Thank you."
    stop music fadeout 3
    play music music.ck1.v10.Track_Scene_13 fadein 2
    scene v11cd15 # TPP. MC and chloe getting into the car
    with dissolve

    pause 0.75

    if CharacterService.is_fwb(chloe) or CharacterService.is_girlfriend(chloe):
        scene v11cd16 #FPP. Inside of the car, mc looking at chloe in passenger sit, mouth closed
        with dissolve
        
        u "You ready, babe?"

        scene v11cd16a # FPP. same as 16, Chloe is smilling, mouth opened
        with dissolve

        cl "We're not in front of him anymore, we can stop acting like a couple. *Chuckles*"

        scene v11cd16
        with dissolve

        u "Who said I was acting?"

        scene v11cd17 # FPP. MC switches cars gear, mouth closed
        with dissolve

        pause 0.75

        scene v11cd18 # FPP. MC places his hand in Chloe's thigh
        with dissolve

        pause 0.75

    else:
        scene v11cd16
        with dissolve
        
        u "Calling a truce on who's the better actor?"

        scene v11cd16b # FPP. same as 16, mouth opened
        with dissolve

        cl "For now."

        scene v11cd16
        with dissolve

        u "Alright then."


    scene v11cd51 # FPP. MC looking at chloe in the passenger sit, smile on her face, mouth opened
    with dissolve

    pause 0.75

    play sound sound.revving

    scene v11cd52 # TPP. Show's the car pulling away from the front of the store
    with dissolve

    pause 2

    scene v11cd20 # TPP. MC and chloe inside the car, smiling, looking forwards in london steets location a (artist decides location)
    with dissolve

    play ambience ambience.driving

    pause 0.75
    
    scene v11cd19 # FPP. now on the road, looking at chloe, mouth opened, surprised look
    with dissolve

    cl "Oh wow, I didn't know you knew how to drive a car like this!"

    scene v11cd19a # FPP. same as 19, mouth closed
    with dissolve

    u "All cars are the same, it's the drivers you have to worry about."

    scene v11cd19
    with dissolve

    cl "Oh my god..."

    scene v11cd19a
    with dissolve

    u "What?"

    scene v11cd19
    with dissolve

    cl "My dad always says that, like verbatim. Word for word!"

    scene v11cd19a
    with dissolve

    u "He knows what he's talking about."

    scene v11cd21 # TPP. MC and chloe inside the car, smiling, looking forwards in london steets location b (artist chooses location)
    with dissolve

    pause 0.75

    scene v11cd22 # FPP. same camera angle as 19 background b, smiling, mouth opened
    with dissolve

    cl "Haha, [name], this is amazing."

    if CharacterService.is_fwb(chloe) or CharacterService.is_girlfriend(chloe):
        menu:
            "Talk about \"us\"": 
                scene v11cd22a # FPP. looking at chloe, mouth closed
                with dissolve

                u "You know Chloe, one day you and I really could be together driving around in a car like this."

                scene v11cd22b # FPP. Chloe looks at mc with a serious face, mouth opened
                with dissolve

                cl "What do you mean together?"

                scene v11cd22a
                with dissolve

                u "Like Mr. and Mrs. together."

                scene v11cd22 
                with dissolve

                cl "It wouldn't be the worst thing. *Chuckles* But really, that does sound nice."

                scene v11cd22a
                with dissolve

                u "I'm glad you think so."

            "Talk about cars":
                scene v11cd22a
                with dissolve
             
                u "I would've never thought to try and drive one of these."

                scene v11cd22
                with dissolve

                cl "I didn't know it'd be so easy to get! I thought we were going to have to scheme our way into it..."

                scene v11cd22a
                with dissolve

                u "You mean like fake being a couple? *Chuckles*"

                scene v11cd22
                with dissolve

                cl "*Chuckles* Yeah, something like that."
    else:
        scene v11cd22a
        with dissolve
        
        u "I would've never thought to try and drive one of these."

        scene v11cd22
        with dissolve

        cl "I didn't know it'd be so easy to get! I thought we were going to have to scheme our way into it..."

        scene v11cd22a
        with dissolve

        u "You mean like fake being a couple? *Chuckles*"

        scene v11cd22
        with dissolve

        cl "*Chuckles* Yeah, something like that."


    scene v11cd22b
    with dissolve
    
    cl "Isn't Chloe Moralez the one that's supposed to be driving?"

    scene v11cd22
    with dissolve

    u "I think I remember something like that, but it seems that my hands are glued to the wheel."

    scene v11cd23 # FPP. Chloe pinches MC's arm, mouth closed
    with dissolve

    u "Woah! Okay, okay. No pinching the driver... Let me pull over and we'll switch."

    scene v11cd24 # TPP. Show's the car parking in location c (artist chooses location)
    with dissolve

    stop ambience
    stop sound
    pause 0.75

    scene v11cd25 # FPP. looking at chloe, mouth opened
    with dissolve

    cl "What?"

    label v11s34_c1:

    if CharacterService.is_fwb(chloe) or CharacterService.is_girlfriend(chloe):
        menu:
            "Kiss her":
                scene v11cd30 # TPP. MC sits on the hood of the car, chloe is nearby
                with dissolve

                pause 0.75

                scene v11cd31 # FPP. MC pulls chloe into his lap, mouth closed
                with dissolve

                u "You are perfect."

                scene v11cd31a # FPP. Slight smile on chloe's face, mouth opened
                with dissolve

                cl "Ha, no I'm not. Nobody is."

                scene v11cd31b # FPP. Same as 31a, mouth closed
                with dissolve

                u "You're right. No one is perfect, but there are people that are perfect for each other and you, Chloe Moralez, are perfect for me."

                scene v11cd31c # FPP. Chloe looks surprised, mouth opened
                with dissolve

                cl "[name]-"

                scene v11cd32 # TPP. Mc kisses chloe romantically on the hood of the car
                with dissolve

                play sound sound.kiss

                pause 0.75

                scene v11cd33 # FPP. Chloe pulls away and is blushing, mouth opened
                with dissolve

                cl "I really like you, [name]."

                scene v11cd33a # FPP. same as 33, mouth closed
                with dissolve

                u "I like you too."

                scene v11cd33b # FPP. chloe looks away.
                with dissolve

                menu:
                    "Be my girlfriend":
                        scene v11cd33c # FPP. Chloe looks back at mc, mouth closed
                        with dissolve
                        stop music fadeout 3
                        play music music.ck1.v10.Track_Scene_11 fadein 2
                        u "Chloe, I've been captured by you since the moment I first saw you. Every day I think about you and hope that we can be together at all times."
                        u "I don't know what I'd do if one day you were just... gone. The truth is... I love you, Chloe, and I don't want to go another day without you being mine."
                        u "So with all that said, can we make it official? Will you be my girl?"

                        if CharacterService.is_girlfriend(chloe) or (meetchloe and hcGirl == "chloe" and ending == "chloe"): #chloe gf in case of seeing this scene via pathbuilder
                            $ CharacterService.set_relationship(chloe, Relationship.GIRLFRIEND)
                            
                            scene v11cd33d # FPP, sanme as 33c, chloe looking excited, mouth opened
                            with dissolve

                            cl "I... I love you too. Yes, yes I'll be your girl!"

                            scene v11cd34 # TPP. Chloe and MC get out of the hood of the car, mouth closed
                            with dissolve

                            pause 0.75

                            scene v11cd35 # TPP. MC picks up chloe with her legs wrapped arround him and kisses her romantically
                            with dissolve

                            play sound sound.kiss

                            if CharacterService.is_girlfriend(lauren) and not v11_lauren_caught_aubrey:
                                $ grant_achievement("two_timer")

                            pause 2.5

                            scene v11cd36 # FPP. MC sets chloe down, mouth closed
                            with dissolve

                            if CharacterService.is_girlfriend(lauren) and not v11_lauren_caught_aubrey:
                                u "(Damn, two girlfriends. This could get complicated fast.)"

                            u "Wow... c'mon, let's get this car back."

                            play ambience ambience.driving

                            scene v11cd28 # TPP. MC and chloe inside the car, smiling, looking forwards in london steets location d
                            with dissolve

                            pause 1

                            stop ambience
                                
                            scene v11cd29 # TPP. MC and chloe getting out of the car infront of the car dealership, mouth closed
                            with dissolve

                            pause 1

                        else:
                            scene v11cd37 # FPP. Chloe looks at mc, with a surprised face, mouth opened
                            with dissolve

                            cl "[name], I care about you a lot too, and I've enjoyed the time we've spent together, but we have so much more to explore about each other."
                            cl "You may like what you see now, but there's still so much we don't know about each other."
                            
                            scene v11cd37a
                            with dissolve
                            
                            scene v11cd37
                            with dissolve
                            
                            cl "I like where we're at, and I'm only focused on you, but we don't need to rush anything. I'm not going anywhere."

                            scene v11cd37a # FPP. Same as 37, mouth closed
                            with dissolve

                            u "I won't be going anywhere either."
                            
                            scene v11cd38 # FPP. Chloe kisses MC
                            with dissolve

                            play sound sound.kiss

                            pause 1.25

                            scene v11cd39 # FPP. chloe has a slight smile, mouth closed
                            with dissolve

                            u "C'mon, let's get this car back."

                            play ambience ambience.driving

                            scene v11cd28 # TPP. MC and chloe inside the car, smiling, looking forwards in london steets location d
                            with dissolve

                            pause 1

                            stop ambience
                                
                            scene v11cd29 # TPP. MC and chloe getting out of the car infront of the car dealership, mouth closed
                            with dissolve

                            pause 1

                    "Let's get the car back":
                        scene v11cd39
                        with dissolve

                        u "C'mon, let's get this car back."

                        play ambience ambience.driving

                        scene v11cd28 # TPP. MC and chloe inside the car, smiling, looking forwards in london steets location d
                        with dissolve

                        pause 0.75
                        
                        stop ambience

                        scene v11cd29 # TPP. MC and chloe getting out of the car infront of the car dealership, mouth closed
                        with dissolve

                        pause 1.25

            "Joke":
                scene v11cd25a # FPP. same as 25, mouth closed
                with dissolve
                u "I just never realized how..."

                scene v11cd25
                with dissolve

                cl "Just how what?"

                scene v11cd25a
                with dissolve

                u "..."

                scene v11cd25b # FPP. same as 25, chloe is looking impatient, mouth opened
                with dissolve

                cl "[name], what?"

                scene v11cd25a
                with dissolve

                u "Just how big your forehead is... *Laughs*"

                scene v11cd25c # FPP. same as 25, chloe laughs harder, mouth opened
                with dissolve

                cl "OH MY GOD, YOU'RE SUCH AN ASS! *Laughs* That's not funny."

                scene v11cd25d # FPP. chloe punches MC, mouth closed
                with dissolve

                u "*Laughs* Ouch!"

                scene v11cd25
                with dissolve

                cl "Get in before I start firing jokes back... You don't want me to hurt your feelings."

                scene v11cd25a
                with dissolve

                u "As you wish, your majesty."

                scene v11cd26 # FPP. Chloe gets in the car, mc is in the passanger door looking through glass, mouth opened
                with dissolve

                play sound sound.revving

                cl "If you don't hurry, I will leave you."

                scene v11cd26a # FPP. Same as 26, mouth closed
                with dissolve

                u "I'm coming!"

                scene v11cd27 # TPP. MC gets in the car
                with dissolve

                pause 0.75

                play ambience ambience.driving

                scene v11cd28 # TPP. MC and chloe inside the car, smiling, looking forwards in london steets location d
                with dissolve

                pause 0.75

                stop ambience
                
                scene v11cd29 # TPP. MC and chloe getting out of the car infront of the car dealership, mouth closed
                with dissolve
    
    else: 
        scene v11cd25a # FPP. same as 25, mouth closed
        with dissolve
        u "I just never realized how..."

        scene v11cd25
        with dissolve

        cl "Just how what?"

        scene v11cd25a
        with dissolve

        u "..."

        scene v11cd25b # FPP. same as 25, chloe is looking impatient, mouth opened
        with dissolve

        cl "[name], what?"

        scene v11cd25a
        with dissolve

        u "Just how big your forehead is... *Laughs*"

        scene v11cd25c # FPP. same as 25, chloe laughs harder, mouth opened
        with dissolve

        cl "OH MY GOD, YOU'RE SUCH AN ASS! *Laughs* That's not funny."

        scene v11cd25d # FPP. chloe punches MC, mouth closed
        with dissolve

        u "*Laughs* Ouch!"

        scene v11cd25
        with dissolve

        cl "Get in before I start firing jokes back... You don't want me to hurt your feelings."

        scene v11cd25a
        with dissolve

        u "As you wish, your majesty."

        scene v11cd26 # FPP. Chloe gets in the car, mc is in the passanger door looking through glass, mouth opened
        with dissolve

        play sound sound.revving

        cl "If you don't hurry, I will leave you."

        scene v11cd26a # FPP. Same as 26, mouth closed
        with dissolve

        u "I'm coming!"

        scene v11cd27 # TPP. MC gets in the car
        with dissolve

        pause 1

        play ambience ambience.driving

        scene v11cd28 # TPP. MC and chloe inside the car, smiling, looking forwards in london steets location d
        with dissolve

        pause 1

        stop ambience
        
        scene v11cd29 # TPP. MC and chloe getting out of the car infront of the car dealership, mouth closed
        with dissolve

        pause 1

    scene v11cd40 # FPP. now in front of the shop, looking at the car salesman, mouth opened
    with dissolve

    stop sound

    csa "Did you two enjoy the ride?"

    if CharacterService.is_girlfriend(chloe): 
        scene v11cd40a # FPP. same as 40, mouth closed
        with dissolve

        u "It changed our lives."

        scene v11cd40b # FPP. same as 40, smile on the carsalesman face, mouth opened
        with dissolve

        csa "You two have truly made my day."

    else: 
        scene v11cd40a
        with dissolve

        u "It was nice."

        scene v11cd40b 
        with dissolve

        csa "Wonderful!"

    scene v11cd40
    with dissolve

    csa "So, will you two be purchasing the car?"

    play sound sound.call

    scene v11cd41 # FPP. now looking at chloe, mouth opened
    with dissolve

    cl "So sorry, one second... My phone is ringing."

    scene v11cd41b # FPP. same as 41, chloe puts her phone to her ear, mouth opened
    with dissolve

    stop sound

    cl "Hello?"

    scene v11cd41b # FPP. same as 41a, chloe makes a shocked face, mouth opened.
    with dissolve

    cl "Oh my god, we're on our way right now!"

    scene v11cd41c # FPP. Chloe looks at MC with a worried face, mouth opened
    with dissolve

    cl "[name], we have to go right now. It's my sister."

    scene v11cd41d # FPP. Chloe looks at the salesman with a sorry face, mouth opened
    with dissolve

    cl "I am so sorry, we'll be back if possible."

    scene v11cd40a
    with dissolve

    u "I'm sorry."

    scene v11cd40
    with dissolve

    csa "No no, please go."

    scene v11cd41 
    with dissolve

    cl "C'mon, [name]!"

    scene v11cd42 # TPP. Chloe whispers in MC's ear, mouth opened
    with dissolve

    cl "*Whisper* Race ya."

    scene v11cd43 # FPP. MC whispers back in chloe's ear
    with dissolve

    u "*Whisper* Huh?"

    if not v11_riley_roomate: 
        scene v11cd44 # TPP. Shows image of chloe and mc running in the streets, smile on their faces
        with dissolve

        pause 0.75

        scene v11cd45 # TPP. Shows mc and chloe in the hotel entrance, still smiling and running
        with dissolve

        pause 0.75

        scene v11cd46 # TPP. shows chloe and mc arriving in their hotel room
        with dissolve

        pause 0.75

        scene v11cd47 # FPP. mc looking at chloe inside hotel room, smile on her face, mouth opened
        with dissolve

        cl "Damn, you're pretty fast."

        scene v11cd47a # FPP, Same as 47, mouth closed
        with dissolve

        u "Haha, you too."

        jump v11_chloe_hotel_room_amber_call

    else: 
        scene v11cd44 # TPP. Shows image of chloe and mc running in the streets, smile on their faces
        with dissolve

        pause 0.75

        scene v11cd45 # TPP. Shows mc and chloe in the hotel entrance, still smiling and running
        with dissolve

        pause 0.75

        scene v11cd46 # TPP. shows chloe and mc arriving in their hotel room
        with dissolve

        pause 0.75

        scene v11cd48 # FPP. Mrlee intercepts you at the door and has a serious face, mouth opened
        with dissolve

        lee "[name], I don't believe that's your room."

        scene v11cd48a # FPP. same as 47, mouth closed
        with dissolve

        u "(What a fucking cock-block.)"

        scene v11cd49 # FPP. Looking at chloe, mouth closed
        with dissolve

        u "I'll see you soon, Chloe."

        scene v11cd49a # FPP. same as 48, Chloe is making a kinky face, mouth opened
        with dissolve

        cl "You better."

        scene v11cd50 # TPP. Mc heads to his room, disapointed face, mouth closed
        with dissolve

        pause 0.75

        jump v11_riley_sex
