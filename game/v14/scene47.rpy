# SCENE 47: Take images of Lindsey car with/without Lindsey
# Locations: 
# Characters: LINDSEY (Outfit: 3), MC (Outfit: 1)
# Time: Evening
# OTHER IMAGES: YES
# SCREEN - Render just the car, make sure that the hood, trunk, passenger door and driver door are visible
# v14s47_lindsey_kiwii.webp - Lindsey in scene 47 outfit making a cute smile kind of shyly with no teeth wearing a Vote 4 Lindsey button on shirt

init python:
    def v14s47_kiwiiReply1():
        v14s47_kiwiiPost1.newComment(lindsey, "A new future for the Chicks, haha. :)", numberLikes=418)

    def v14s47_kiwiiReply2():
        v14s47_kiwiiPost1.newComment(lindsey, "Damn straight!", numberLikes=314)

    def v14s47_kiwiiReply3():
        v14s47_kiwiiPost1.newComment(lindsey, "You're a dork.", numberLikes=286)
    
    def v14s47_kiwiiReply4():
        v14s47_kiwiiPost1.newComment(lindsey, "Haha, I h8 you <3", numberLikes=266)

label v14s47:

    play music "music/v12/Track Scene 32_1.mp3" fadein 2
# -Peace and Cheex can help with this scene: MC walks up to Lindsey and they have a convo by the car with a few images of the car. When MC is ready to take pictures we will go to a free roam shot of the car. Highlight the passenger side, driver side, hood, and trunk. MC chooses in any order where to take pics. Once they've taken the pic, revert back to the freeroam screen where their previous choice is now greyed out, and the other choices remain while ALSO having a "Finish" button in the bottom right. MC has to take one photo, but can choose whether to take all 4, or leave after each one. Revert back to the freeroam screen after each photo is taken, the player makes their choices, and when all 4 have been taken or if they click "finish", -if finish dialogue.

# -MC approaches Lindsey who is standing next to a dirty (needs to be seen that it hasn't been washed b/c dialogue) old Volkswagen. They both smile when they see each other-

# -Lindsey mentioned that she would get dressed up for the photos if MC chose the option to have her in the photos on the planning board. So either way I need her in something new, something cute, sexy, but not lingerie. Heels probably, makeup maybe, MAKE SURE SHE HAS POCKETS for a lollipop, etc-

    scene v14s47_1 # TPP. Show MC arriving at the parking lot, back to camera, Lindsey leaning on the car, make sure car is dirty and old looking, slightly worried, not looking at MC, Lindsey and the car are far from MC
    with dissolve

    pause 0.75

    scene v14s47_1a # TPP. Same as v14s47_1, MC walking over to Lindsey, Lindsey looking at MC, smiling, mouth closed
    with dissolve

    pause 0.75

    scene v14s47_2 # FPP. MC now standing in front of Lindsey, Lindsey looking at MC, mouth open, smiling
    with dissolve

    li "There he is."

    scene v14s47_3 # TPP. Show MC looking confused, but smiling, to his right, mouth open, Lindsey laughing
    with dissolve

    u "Here who is?"

    if lindsey.relationship.value >= Relationship.FWB.value:
        scene v14s47_2
        with dissolve

        li "A handsome man... Who's ready to take some photos, I hope?"

        play sound "sounds/kiss.mp3"

        scene v14s47_4 # TPP. Close up of Lindsey kissing MC's cheek
        with dissolve

        pause

        scene v14s47_2a # FPP. Same as v14s47_2, Lindsey smiling, mouth closed
        with dissolve

        u "Haha, well thank you..."

        if v14_pics_with_linds: # PLACEHOLDER
            scene v14s47_5 # TPP. Close up of Lindsey and her outfit, Lindsey mouth closed, smiling
            with dissolve

            u "But holy hell..."

            scene v14s47_6 # TPP. Show MC twirling Lindsey around, Lindsey smiling, mouth open, MC smiling, mouth closed
            with dissolve

            li "I said I'd get dressed up nice."

            scene v14s47_2a
            with dissolve

            u "Yeah. *Chuckles* Really nice..."

        else:
            scene v14s47_5
            with dissolve

            u "But holy hell..."

            scene v14s47_6
            with dissolve

            li "Like what you see?"

            scene v14s47_2a
            with dissolve

            u "I like it a lot... *Laughs* Why are you all dressed up?"

            scene v14s47_2
            with dissolve

            li "Just finished taking a few presidential photos for Kiwii."

            scene v14s47_2a
            with dissolve

            u "Oooh..."

            scene v14s47_2
            with dissolve

            li "Be sure to comment exactly that on my post, haha."

            scene v14s47_2a
            with dissolve

            u "Oh, I will. You look great."

        scene v14s47_2
        with dissolve

        li "Thank you, [name]."

        scene v14s47_2b # FPP. Same as v14s47_2a, different pose, Lindsey excited and smiling, mouth open
        with dissolve

        li "Now, are you ready to capture all this beauty while I'm standing in front of the shittiest car you've ever seen?"

    else:
        scene v14s47_2b
        with dissolve

        li "My savior. My hero. My-"

        scene v14s47_2c # FPP. Same as v14s47_2b, Lindsey mouth closed
        with dissolve

        u "Uh, huh? Keep going... Please, I insist."

        scene v14s47_2
        with dissolve

        li "Okay, no. I think that's enough praise for today..."

        if v14_pics_with_linds:
            scene v14s47_2a
            with dissolve

            u "Not yet. I mean... You look great."

            scene v14s47_2
            with dissolve

            li "*Chuckles* Thank you, [name]. I told you I'd dress up nicely if it means that we make a bit extra cash."

            scene v14s47_2c
            with dissolve

            u "Haha... I think it'll work."

            scene v14s47_2b
            with dissolve

            li "Now, are you ready to capture all this beauty while I'm standing in front of the shittiest car you've ever seen?"
        
        else:
            scene v14s47_2a
            with dissolve

            u "You look nice by the way. Going out tonight?"

            scene v14s47_2
            with dissolve

            li "Haha, the opposite actually. I just finished taking a few presidential photos for Kiwii."

            scene v14s47_2c
            with dissolve

            u "Oh, gotcha. I can't wait to like, comment, subscribe, push the notification bell-"

            scene v14s47_2b
            with dissolve

            li "*Laughs* Alright, alright. Are you ready to capture all the beauty of the shittiest car you've ever seen?"

    scene v14s47_2c
    with dissolve

    u "*Laughs* As ready as I'll ever be. Is this it?"

    scene v14s47_7 # TPP. Showcase the car, make sure it looks like a bad car, Lindsey and MC standing by the car (both nervously smiling, mouths closed)
    with dissolve

    u "(Fucking hell...)"

    scene v14s47_8 # FPP. MC and Lindsey standing next to each other, close to the car, bodies facing the car, but looking at each other, Lindsey smiling, mouth open
    with dissolve

    li "Yep. This was my high school graduation present from my grandpa."

    scene v14s47_8a # FPP. Same as v14s47_8, Lindsey mouth closed
    with dissolve

    u "Oh, really? And you're selling it?"

    scene v14s47_8b # FPP. Same as v14s47_8, Lindsey looking down, smiling, mouth open
    with dissolve

    li "*Laughs* Okay, it's not like that..."

    scene v14s47_8a
    with dissolve

    u "I'm kidding."

    scene v14s47_8
    with dissolve

    li "I know but... Still, he gave it to me knowing that I would sell it. I just didn't need the extra money until now."

    scene v14s47_8a
    with dissolve

    u "Hm... Sounds like a nice Grandpa."

    scene v14s47_8b
    with dissolve

    li "Oh yeah. He's the best."

    scene v14s47_9 # TPP. Close up of MC's hand touching the dirt on the car
    with dissolve

    u "Didn't he mention that you should wash it first? *Laughs*"

    scene v14s47_8c # FPP. Same as v14s47_8, Lindsey looking at the car, smiling, mouth open
    with dissolve

    li "I haven't had time! This thing has been sitting around collecting dust for-"

    scene v14s47_8a
    with dissolve

    u "Decades? *Chuckles*"

    scene v14s47_8
    with dissolve

    li "[name]... *Laughs* Let's just take these photos already so we can sell it as quickly as we can. Please?"

    scene v14s47_8a
    with dissolve

    u "Alright, you're the boss."

    scene v14s47_10 # TPP. Show MC grabbing his phonem, getting ready to take pics, smiling, mouth closed
    with dissolve

    stop music fadeout 3

    play music "music/v12/Track Scene 32_2.mp3" fadein 2

    pause 0.75

    if v14_pics_with_linds:
        scene v14s47_8a
        with dissolve

        u "Ready to do some modelling for me?"

        scene v14s47_8
        with dissolve

        li "Hell yeah! I'm excited for this."

        scene v14s47_8a
        with dissolve

        u "Good to hear. The more pics you're in, the more dicks we can attract."

        scene v14s47_8b
        with dissolve

        li "*Laughs* That's so gross, yet so true..."

        scene v14s47_8a
        with dissolve

        u "There are a lot of pervs out there... I'm curious to see which one ends up buying this piece of junk. *Chuckles*"

        scene v14s47_8c
        with dissolve

        li "*Laughs* Interesting logic, [name]. They must be a perv if they decide to buy?"

        scene v14s47_8a
        with dissolve

        u "Either that or... Desperate for four wheels and a piece of metal."

        scene v14s47_8
        with dissolve

        li "*Laughs* Okay... Whatever they do with it, whyever they choose to buy; if they give us their money, I'm happy."

        scene v14s47_8a
        with dissolve

        u "Ha, true. Let's do it then."

        scene v14s47_8c
        with dissolve

        li "Okay. Where do you want me first?"

        scene v14s47_11 # FPP. MC looking at the car
        with dissolve

        u "Let's start with..."

    else:
        scene v14s47_8a
        with dissolve

        u "Well, I'm glad we decided on you not being in the photos, ha."

        scene v14s47_8
        with dissolve

        li "Yeah, me too. We've only got one shot at this, and I don't want to ruin it with any... unnecessary hotness. *Chuckles* You know?"

        scene v14s47_8a
        with dissolve

        u "Right... Some people can be so easily offended."

        u "I kind of meant because of how gross it is, though. *Laughs*"

        scene v14s47_8b
        with dissolve

        li "Oh my god, you're right... Good call, haha."

        scene v14s47_11
        with dissolve

        u "Alright, let's start with..."
    call screen v14s47_car

label v14s47_hood:
    if v14_pics_with_linds:
        $ v14s47_car_pics.append("v14s47_hood_2.webp")

        scene v14s47_hood_1 # TPP. MC walking over to the position he'll take Lindsey's picture, Lindsey moving towards the side of the hood

        pause 0.75

        scene v14s47_hood_2 # FPP. MC in position to take the picture, Lindsey in her picture pose (cleavage showing, resting her elbows on the hood), big smile, mouth closed
        with dissolve

        u "(Damn girl...)"

        scene v14s47_hood_3 # TPP. Close up of Lindsey's cleavage, Lindsey big smile, mouth closed
        with dissolve

        u "Just a little bit longer..."

        scene v14s47_hood_2a # FPP. Same as v14s47_hood_2, Lindsey mouth open
        with dissolve

        li "*Laughs* Just take the photo already, [name]!"

        scene v14s47_hood_2
        with dissolve

        u "*Chuckles* Sorry!"

        play sound "sounds/capture.mp3"

        scene v14s47_hood_4 # TPP. Show MC holding up his phone as if he were taking her pic (DO NOT SHOW LINDSEY/THE CAR; ONLY MC), smiling, mouth closed (Add a flash to the camera in PhotoShop)
        with flash

        pause 
        
        scene v14s47_hood_2
        with dissolve

        li "Nice. Now what?"
    
    else:
        $ v14s47_car_pics.append("v14s47_hood_2b.webp")

        scene v14s47_hood_1

        pause 0.75

        scene v14s47_hood_2b # FPP. Same as v14s47_hood_2, but no Lindsey in shot, she is standing off to side, but not in shot
        with dissolve

        u "Oh, shit! Was that a rat?!"

        scene v14s47_hood_5 # FPP. MC looking at Lindsey, Lindsey same positioning as v14s47_hood_2b, Lindsey freaking out, mouth open, looking at the ground
        with dissolve

        li "OH MY GOD! WHERE?!"

        scene v14s47_hood_5a # FPP. Same as v14s47_hood_5, Lindsey looking at MC, slight smile, mouth closed
        with dissolve

        u "*Chuckles*"

        scene v14s47_hood_5b # FPP. Same as v14s47_hood_5a, Lindsey mouth open
        with dissolve

        li "*Sighs* Hilarious."

        scene v14s47_hood_5a
        with dissolve

        u "Thank you."

        play sound "sounds/capture.mp3"

        scene v14s47_hood_4
        with flash

        pause

        scene v14s47_hood_5b
        with dissolve

        li "Nice. Now what?"

    call screen v14s47_car

label v14s47_trunk:
    if v14_pics_with_linds:
        $ v14s47_car_pics.append("v14s47_trunk_2b.webp")

        scene v14s47_trunk_1 # TPP. MC and Lindsey walking over to the trunk of the car, both smiling, mouths closed

        pause 0.75

        scene v14s47_trunk_2 # FPP. Lindsey's hand on the trunk, with her ass facing MC, as she looks back to MC, smiling, mouth open, MC is behind her (not right behind her, put him at a slight distance)
        with dissolve

        li "How's this look?"

        scene v14s47_trunk_2a # FPP. Same as v14s47_trunk_2, but Lindsey mouth closed
        with dissolve

        u "Can you get that ass any higher?"

        scene v14s47_trunk_2
        with dissolve

        li "I can try."

        scene v14s47_trunk_2b # FPP. Same as v14s47_trunk_2, Lindsey on the tip of her toes, to get her ass higher, Lindsey sexy smile, mouth closed
        with dissolve

        u "Ha, that's perfect."

        play sound "sounds/capture.mp3"

        scene v14s47_trunk_4 # TPP. Show MC holding up his phone as if he were taking her pic (DO NOT SHOW LINDSEY/THE CAR; ONLY MC), smiling, mouth closed (Add a flash to the camera in PhotoShop)
        with flash

        pause

        scene v14s47_trunk_2
        with dissolve

        li "Okay. What's next?"

    else:
        $ v14s47_car_pics.append("v14s47_trunk_2c.webp")

        scene v14s47_trunk_1

        pause 0.75

        scene v14s47_trunk_2c # FPP. Same as v14s47_trunk_2, but no Lindsey
        with dissolve

        u "It honestly kind of looks like a clown car from the circus."

        scene v14s47_trunk_3 # FPP. Lindsey standing next to MC, Lindsey looking at MC, smiling, mouth open
        with dissolve

        li "It does not! *Laughs*"

        scene v14s47_trunk_3a # FPP. Same as v14s47_trunk_3, Lindsey looking intensely at the car, kind of worried, mouth closed
        with dissolve

        li "..."

        scene v14s47_trunk_3b # FPP. Same as v14s47_trunk_3, Lindsey slightly worried, mouth open
        with dissolve

        li "Okay, it kinda does... Is it that bad?"

        scene v14s47_trunk_3c # FPP. Same as v14s47_trunk_3, Lindsey smirking, mouth closed
        with dissolve

        u "Not if you're a clown."

        scene v14s47_trunk_3d # FPP. Same as v14s47_trunk_3c, Lindsey smirking, mouth open
        with dissolve

        li "There's a few of those around here actually..."

        scene v14s47_trunk_3c
        with dissolve

        u "Oooooh! Shots fired."

        scene v14s47_trunk_3d
        with dissolve

        li "Haha."

        play sound "sounds/capture.mp3"

        scene v14s47_trunk_4 
        with flash

        pause

        scene v14s47_trunk_3
        with dissolve

        li "Okay. What's next?"

    call screen v14s47_car

label v14s47_driver:
    if v14_pics_with_linds:
        $ v14s47_car_pics.append("v14s47_driver_2c.webp")

        scene v14s47_driver_1 # TPP. Show MC and Lindsey walking over to the driver side of the car, both smiling, mouths closed

        pause 0.75

        scene v14s47_driver_2 # FPP. Lindsey standing by the driver door, MC in a place where he can take a pic of her and the car, Lindsey slightly excited, mouth open, showing her hand at MC (as if she were signalling for him to stop)
        with dissolve

        li "Wait! I just remembered..."

        scene v14s47_driver_2a # FPP. Same as v14s47_driver_2, Lindsey pulling out a lollipop out of her pocket, smiling, mouth open, wrapper on
        with dissolve

        li "I have a lollipop! Should I like... suck on it? *Laughs*"

        scene v14s47_driver_2b # FPP. Same as v14s47_driver_2, Lindsey looking at MC, unwrapping the lollipop, mouth closed, smiling
        with dissolve

        if lindsey.relationship.value >= Relationship.FWB.value:
            u "Is that even a question? *Chuckles*"

        else:
            u "Um... Yes. *Laughs*"

        scene v14s47_driver_2c # FPP. Same as v14s47_driver_2, Lindsey posing by the door, sucking on the lollipop, making a sexy face at MC, mouth closed
        with dissolve

        u "Holy shit, Linds... I wouldn't be able to turn down an offer like that either."

        scene v14s47_driver_2d # FPP. Same as v14s47_driver_2c, Lindsey mouth open
        with dissolve

        li "Ha! Feeling pervy?"

        scene v14s47_driver_2c
        with dissolve

        u "Eh... Please don't say that ever again."

        scene v14s47_driver_2d
        with dissolve

        li "Yeah... I definitely won't."

        scene v14s47_driver_2c
        with dissolve

        u "*Chuckles*"

        play sound "sounds/capture.mp3"

        scene v14s47_driver_3 # TPP. Show MC holding up his phone as if he were taking her pic (DO NOT SHOW LINDSEY/THE CAR; ONLY MC), smiling, mouth closed (Add a flash to the camera in PhotoShop)
        with flash

        pause

        scene v14s47_driver_2c
        with dissolve

        u "Beautiful. What's next?"
    
    else:
        $ v14s47_car_pics.append("v14s47_driver_2e.webp")

        scene v14s47_driver_1

        pause 0.75

        scene v14s47_driver_2e # FPP. Same as v14s47_driver_2, but Lindsey not in shot
        with dissolve

        u "And now the driver's side..."

        scene v14s47_driver_4 # FPP. Lindsey standing next to MC, Lindsey looking at MC, smiling, mouth closed
        with dissolve

        u "This is where the action happens."

        scene v14s47_driver_4a # FPP. Same as v14s47_driver_4, Lindsey mouth open
        with dissolve

        li "Ha, um... Pretty sure the action happens in the back seat."

        scene v14s47_driver_4
        with dissolve

        u "*Chuckles* Oh?"

        scene v14s47_driver_4a
        with dissolve

        li "What?"

        scene v14s47_driver_4
        with dissolve

        u "Sounds like you've got a story to tell...?"

        scene v14s47_driver_4a
        with dissolve

        li "*Laughs* No."

        scene v14s47_driver_4
        with dissolve

        u "But-"

        scene v14s47_driver_4a
        with dissolve

        li "N. O. No."

        scene v14s47_driver_4
        with dissolve

        u "Fine..."

        play sound "sounds/capture.mp3"

        scene v14s47_driver_3
        with flash

        pause

        scene v14s47_driver_4
        with dissolve

        u "Beautiful. What's next?"
    
    call screen v14s47_car

label v14s47_passenger:
    scene v14s47_passenger_1 # TPP. Show MC and Lindsey walking towards the passenger door

    pause 0.75

    if v14_pics_with_linds:
        scene v14s47_passenger_2 # FPP. Lindsey standing by the passenger door, MC looking at her (he's in a place where he can take her pic), Lindsey slightly confused, mouth open
        with dissolve

        li "Hmm..."

        li "I'm not sure what pose to do here."

        scene v14s47_passenger_2a # FPP. Same as v14s47_passenger_2, Lindsey mouth closed
        with dissolve

        menu:
            "Hand on hips":
                $ add_point(KCT.BOYFRIEND)
                $ v14s47_car_pics.append("v14s47_passenger_2b.webp")

                scene v14s47_passenger_2b # FPP. Same as v14s47_passenger_2, Lindsey mouth closed, smiling
                with dissolve

                u "Just give me a good smile with one hand on your hip and the other on the car."

                scene v14s47_passenger_2c # FPP. Same as v14s47_passenger_2b, Lindsey mouth open
                with dissolve

                li "Damn, okay Mr. Photography..."

                scene v14s47_passenger_2d # FPP. Same as v14s47_passenger_2b, Lindsey with one hand on her hip, another on the roof, smiling, mouth closed (a bit sexy, not too much)
                with dissolve

                pause

                play sound "sounds/capture.mp3"

                scene v14s47_passenger_3 # TPP. Show MC holding up his phone as if he were taking her pic (DO NOT SHOW LINDSEY/THE CAR; ONLY MC), smiling, mouth closed (Add a flash to the camera in PhotoShop)
                with flash

                pause

                scene v14s47_passenger_2c
                with dissolve

                li "Alrighty... Anymore?"

            "Stand there and look pretty":
                $ add_point(KCT.BRO)
                $ add_point(KCT.TROUBLEMAKER)
                $ v14s47_car_pics.append("v14s47_passenger_2e.webp")

                scene v14s47_passenger_2b
                with dissolve

                u "Just... Stand there and look pretty or something. *Laughs*"

                scene v14s47_passenger_2c
                with dissolve

                li "Wow! Great idea, [name]. So creative..."

                scene v14s47_passenger_2b
                with dissolve

                u "Haha, sorry. You look great no matter what, so it doesn't technically matter."

                scene v14s47_passenger_2c
                with dissolve

                li "Well, thank you, haha. I just hope the buyers think the same thing."

                scene v14s47_passenger_2e # FPP. Same as v14s47_passenger_2b, Lindsey on her knees, hands on her thighs, posing sexily with a mischievous smile, mouth closed
                with dissolve
                
                pause

                play sound "sounds/capture.mp3"

                scene v14s47_passenger_3 
                with flash

                pause 

                scene v14s47_passenger_2c
                with dissolve

                li "Alrighty... Anymore?"

        scene v14s47_passenger_3 
        with flash

        pause
    
    else:
        scene v14s47_passenger_2f # FPP. Same as v14s47_passenger_2, Lindsey not in shot, there is a bird on the roof, looking at the camera
        with dissolve

        u "Oh- We have a photo-bombing bird!"

        li "Ha, wow... He's looking right at the camera!"

        scene v14s47_passenger_4 # FPP. Lindsey standing next to MC, both looking at each other, Lindsey smiling, mouth closed
        with dissolve

        u "Do we want it in the shot?"

        scene v14s47_passenger_4a # FPP. Same as v14s47_passenger_4, but Lindsey mouth open
        with dissolve

        li "Hmm... Maybe the animal lovers will like it?"

        scene v14s47_passenger_4
        with dissolve

        menu:
            "Scare bird away":
                $ v14s47_car_pics.append("v14s47_passenger_2l.webp")
                
                u "Nah. Scare it away before it poops!"

                scene v14s47_passenger_2g # FPP. Same as v14s47_passenger_2f, Lindsey walking over to the brid, arms raised, mouth open, trying to scare it away (Lindsey was standing next to MC)
                with dissolve

                li "Go away, bird! This is a no-poop zone!"

                scene v14s47_passenger_2h # FPP. Same as v14s47_passenger_2g, Lindsey standing next to the bird, the bird is reacting, Lindsey mouth closed, Lindsey still trying to shoo it away, bird beak open
                with dissolve

                bird "Gawk!"

                scene v14s47_passenger_2i # FPP. Same as v14s47_passenger_2h, Lindsey mouth open, bird reacting, beak closed
                with dissolve

                li "Shoo! Why aren't you flying away?!"

                scene v14s47_passenger_2j # FPP. Same as v14s47_passenger_2i, Lindsey and bird kind of fighting, both mouths closed
                with dissolve

                u "*Laughs*"

                scene v14s47_passenger_2k # FPP. Same as v14s47_passenger_2j, Lindsey walking back to MC, bird flying away, Lindsey annoyed, mouth open
                with dissolve

                li "Finally! What the fuck was up with that thing?"

                scene v14s47_passenger_2l # FPP. Same as v14s47_passenger_2f, but no bird, just the car
                with dissolve

                pause

                play sound "sounds/capture.mp3"

                scene v14s47_passenger_3
                with flash

                pause

                scene v14s47_passenger_4a
                with dissolve

                li "Alrighty... Anymore?"

            "Take photo with bird":
                $ v14s47_car_pics.append("v14s47_passenger_2f.webp")

                u "Yeah, Linds. A crazy bird lady might buy the car simply because he's sitting on it. *Chuckles*"

                scene v14s47_passenger_4a
                with dissolve

                $ grant_achievement("say_chirp")
                li "He is a cute little bird!"

                play sound "sounds/capture.mp3"

                scene v14s47_passenger_3
                with flash

                pause

                scene v14s47_passenger_4a
                with dissolve

                li "Alrighty... Any more?"

    call screen v14s47_car

label v14s47_end:

    stop music fadeout 3

    play music "music/v12/Track Scene 32_4.mp3" fadein 2

    scene v14s47_end_1 # FPP. MC and Lindsey standing by the car, next to each other, Lindsey looking at MC, Lindsey smiling, mouth closed

    if len(v14s47_car_pics) < 4:
        u "Okay, I think that's enough."
    
    else:
        u "Alright. That's every angle of Grandpa's Wagen, I think."

    scene v14s47_end_1a # FPP. Same as v14s47_end_1, Lindsey mouth open
    with dissolve

    li "*Laughs* Great."

    if v14_pics_with_linds:
        scene v14s47_end_1b # FPP. Same as v14s47_end_1a, Lindsey different pose
        with dissolve

        li "I just really hope that the person who buys this thing doesn't actually expect me to come with it."

        scene v14s47_end_1c # FPP. Same as v14s47_end_1b, Lindsey mouth closed
        with dissolve

        u "We can let them think that all the way up until their money hits your bank account. Then we'll just ghost 'em. *Laughs*"

        scene v14s47_end_1a
        with dissolve

        li "[name]! *Chuckles*"

        scene v14s47_end_1
        with dissolve

        u "Aw, come on. Don't act like that isn't our plan..."

        scene v14s47_end_1a
        with dissolve

        li "Well, just... Don't say it out loud like that."

        scene v14s47_end_1c
        with dissolve

        u "Haha, okay."

    else:
        scene v14s47_end_1d # FPP. Same as v14s47_end_1c, Lindsey slightly worried
        with dissolve

        u "I hope we can find the perfect buyer for this thing."

        scene v14s47_end_1e # FPP. Same as v14s47_end_1d, Lindsey mouth open
        with dissolve

        li "*Sighs* Me too. Hopefully we can sell it to anyone at all, ha."

        scene v14s47_end_1c
        with dissolve

        u "I think we will. All depends on the ad now."

        scene v14s47_end_1b
        with dissolve

        li "Yeah, you're right."

    scene v14s47_end_1a
    with dissolve

    li "We need to create a listing on iBuy."

    scene v14s47_end_1
    with dissolve

    u "(I need a nap.)"

    scene v14s47_end_1b
    with dissolve

    li "Let's go get a coffee while we do that, yeah?"

    scene v14s47_end_1c
    with dissolve

    u "Are you reading my mind? "

    scene v14s47_end_1b
    with dissolve

    li "*Laughs* Not right now, no."

    scene v14s47_end_2 # TPP. Show Lindsey patting the car on the hood, MC waving at it as they walk towards the exit, both smiling, mouths closed
    with dissolve

    pause 0.75

    scene v14s47_end_3 # FPP. MC and Lindsey at the exit of the parking lot, looking at Lindsey, car in background, Lindsey smiling, mouth closed
    with dissolve

    u "Bye big chunk of metal! *Chuckles*"

    scene v14s47_end_3a # FPP. Same as v14s47_end_3, Lindsey mouth open
    with dissolve

    li "So mean..."

    scene v14s47_end_3
    with dissolve

    u "It's a car, Lindsey..."

    scene v14s47_end_3a
    with dissolve

    li "*Laughs*"

    scene v14s47_end_4 # TPP. Show MC and Lindsey walking along the street, both smiling, mouths closed
    with fade

    pause 0.75

    stop music fadeout 3


    $ v14s47_kiwiiPost1 = KiwiiPost(lindsey, "v14/v14s47_lindsey_kiwii.webp", "Making big moves ;)", numberLikes=720)
    $ v14s47_kiwiiPost1.newComment(nora, "Kick ass babe <3", force_send=True, numberLikes=259)
    $ v14s47_kiwiiPost1.newComment(aubrey, "Aww, look at your cute little button!", force_send=True, numberLikes=623)
    $ v14s47_kiwiiPost1.newComment(riley, "I have one too :) Hehe.", force_send=True, numberLikes=367)
    $ v14s47_kiwiiPost1.newComment(sebastian, "Looking all official now, Linds!", force_send=True, numberLikes=108)
    if v14_pics_with_linds:
        $ v14s47_kiwiiPost1.addReply("Damn, she's cute... What is she selling? ;)", v14s47_kiwiiReply1, numberLikes=351)
        $ v14s47_kiwiiPost1.addReply("#ThatsMyPresident", v14s47_kiwiiReply2, numberLikes=402)
    else:
        $ v14s47_kiwiiPost1.addReply("Liked, commenting, where do I subscribe", v14s47_kiwiiReply3, numberLikes=206)
        $ v14s47_kiwiiPost1.addReply("Oooh... ;)", v14s47_kiwiiReply4, numberLikes=151)

    jump v14s48