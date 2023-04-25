# SCENE 5: Text from Josh/Sex with Candy
# Location: At the park still from scene 4
# Characters: MC smart outfit from scene 1, Josh (Outfit 1)
# Time: Night time

label v11_nightclub_with_josh:
    #scene v11seap4e # FPP. Show the Park, Show Emily just leaving
    #with fade

    scene v11swc31
    with dissolve

    play music "music/v11/Track Scene 4_1.mp3" fadein 2
    play sound "sounds/vibrate.mp3"

    u "(Let's see who this is.)"

    python:
        v11s5_reply1 = MessageBuilder(josh)
        v11s5_reply1.new_message("Really bro, that's lame.")
        v11s5_reply1.add_reply("No for real, I have to pack for the trip.")
        if josh_europe:
            v11s5_reply1.new_message("Fuck, me too.")
        else:
            v11s5_reply1.new_message("Whatever man!")

        v11s5_reply2 = MessageBuilder(josh)
        v11s5_reply2.set_variable("v11_josh_nightclub", True)
        v11s5_reply2.new_message("Let's party!")

    $ MessengerService.new_message(josh, "WE GETTIN FUCKED UP TONIGHT!")
    $ MessengerService.add_reply(josh, "Who?")
    $ MessengerService.new_message(josh, "You and me, meet me at the bar on Stevenson.")
    $ MessengerService.add_reply(josh, "There's a lot of bars on Stevenson.")
    $ MessengerService.new_message(josh, "The Hive duh!")
    $ MessengerService.add_reply(josh, "Josh, we can't even get in.")
    $ MessengerService.new_message(josh, "With these fake IDs we can...")
    $ MessengerService.add_replies(josh,
        Reply("I can't be staying up anyway, I still have a ton of stuff to do tonight.", v11s5_reply1)
        Reply("LET'S FUCKING GOOOOO! OMW NOW!", v11s5_reply2)
    )

    while MessengerService.has_replies(josh):
        call screen phone
        if MessengerService.has_replies(josh):
            u "(I should check my phone.)"

    if not v11_josh_nightclub:

        u "(I'm going home and straight to bed.)"

        scene v11swc32 # TPP. Show MC walking down the side walk (further down the street)
        with dissolve

        pause 0.75

        scene v11swc33 # TPP. Show MC walking down the side walk (even further down the street)
        with dissolve

        pause 0.75

        jump v11_thurs_night_room

    else:
        u "(This is gonna be a fun ass night.)"

    scene v11swc32 # TPP. Show MC walking down the side walk (further down the street)
    with dissolve

    pause 1 

    scene v11swc33 # TPP. Show MC walking down the side walk (even further down the street)
    with dissolve

    pause 1 

    scene v11swc2 # TPP Show MC giving Josh a high 5 outside of a bar
    with fade

    stop music fadeout 3
    play music "music/v11/Track Scene 5_2.mp3" fadein 2

    jo "There he is. Ready to get fucked up?"

    scene v11swc3 # FPP Outside of bar, show Josh smiling, mouth closed
    with dissolve

    u "Sure am!"

    scene v11swc3a # FPP Same angle as v11swc3, Josh handing MC an ID card, mouth open
    with dissolve

    jo "Alright! Let's go inside Mr. John Smith."

    scene v11swc3
    with dissolve

    u "Wait what?"

    scene v11swc3b # FPP Same angle as v11swc3, Josh with big smile, mouth open
    with dissolve

    jo "Yeah, that's the name I put on your ID. Cool right?"

    menu:
        "Cool":
            $ reputation.add_point(RepComponent.BRO)

            scene v11swc3
            with dissolve

            u "Hell yeah! Hi, I'm John Smith. My stock dividends have treated me well, and I'm here to have a good time."

        "Basic":
            scene v11swc3
            with dissolve

            u "That's the most basic name ever. Should've just used my real name."

            scene v11swc3b
            with dissolve

            jo "Pfft, no dude. You're supposed to enjoy this, just have fun with it."

            scene v11swc3
            with dissolve

            u "Fine. Hi, I'm John Smith. My stock dividends have treated me well, and I'm here to have a good time."

    stop music fadeout 3
    play music "music/v11/Track Scene 5_3.mp3" fadein 2

    scene v11swc3b
    with dissolve

    jo "That was good, but watch this. Hey ladies, the name's Bruce Wayne. Anyone tryna have a good time tonight?"

    scene v11swc3
    with dissolve

    u "Did you say Bruce Wayne?"

    scene v11swc3b
    with dissolve

    jo "Sure did."

    scene v11swc3
    with dissolve

    u "Bro... that's Batman. No way you get away with that. *Chuckles*"

    scene v11swc3b
    with dissolve

    jo "Of course I will, We pretty much look alike... Let's do this."

    scene v11swc3
    with dissolve

    if not josh_europe:
        menu:
            "Invite to Europe":
                $ reputation.add_point(RepComponent.BRO)
                $ josh_europe = True

                scene v11swc3
                with dissolve

                u "While I still remember, I didn't see your name on the list of people going to Europe. Are you not coming?"

                scene v11swc3c # FPP Same angle as v11swc3, Josh with neutral expression, mouth open
                with dissolve

                jo "Are you?"

                scene v11swc3d # FPP Same angle and expression as v11swc3, Josh mouth closed
                with dissolve

                u "Of course, all the girls are going so why not? *Chuckles*"

                scene v11swc3c
                with dissolve

                jo "*All* of the girls? Do I need to do anything to go?"

                scene v11swc3d
                with dissolve

                u "Just talk to Ms. Rose or Mr. Lee tomorrow and get on the list. But do it early because we leave Saturday morning."

                scene v11swc3b
                with dissolve

                jo "If I'm not too fucked up after tonight, I'll do it first thing tomorrow. Now c'mon."

            "Don't invite":
                scene v11swc3
                with dissolve

                u "(Nah.)"

    scene v11swc4 # TPP Inside of bar, show MC and Josh talking to Security Guard, Security Guard with serious expression, hand up, mouth open
    with fade

    sec "Hold up. IDs please."

    scene v11swc4a # TPP Same angle as v11swc4, Security Guard mouth closed, Josh and MC holding up IDs
    with dissolve

    pause 0.75

    scene v11swc4b # TPP Same angle as v11swc4, Security Guard hand down, neutral expression, mouth open
    with dissolve

    sec "Alright, looks good to me. Enjoy yourselves."

    scene v11swc4c # TPP Same angle and expression as v11swc4b, Josh mouth open, Security Guard mouth closed
    with dissolve

    jo "Thanks."

    scene v11swc5 # TPP Show Josh and MC at bar
    with dissolve

    pause 0.75

    scene v11swc6 # FPP At bar, show Josh smiling, mouth closed
    with dissolve

    u "*Whisper* How did that just happen?"

    scene v11swc6a # FPP Same angle and expression as v11swc6, Josh mouth open
    with dissolve

    jo "I told you it'd work, now let's get drunk!"

    scene v11swc5a # TPP Same angle as v11swc5, Josh and MC at bar, Bartender behind bar, mouth open
    with dissolve

    bartender "What can I get you?"

    scene v11swc5b # TPP Same angle and characters as v11swc5a, Bartender mouth closed, Josh holding up three fingers
    with dissolve

    jo "Three shots of Henny."

    scene v11swc6b # FPP Show Bartender behind bar, mouth open
    with dissolve

    bartender "And for you?"

    menu:
        "Henny":
            $ reputation.add_point(RepComponent.BRO)

            scene v11swc6c # FPP Same angle as v11swc6b, Bartender mouth closed
            with dissolve

            u "I'll take the same."

            scene v11swc6d # FPP Show three shots of amber liquor on the bar
            with dissolve

            pause 0.75

        "Vodka":
            scene v11swc6c
            with dissolve

            u "Three shots of Vodka for me."

            scene v11swc6e # FPP Show three shots of clear liquor on the bar
            with dissolve

            pause 0.75

    scene v11swc6a
    with dissolve

    jo "Nice choice!"

    scene v11swc6f # FPP Show Josh, smiling with mouth open, looking away toward the crowd in the bar
    with dissolve

    jo "Alright let's see, who's going home with me tonight?"

    scene v11swc6g # FPP Same angle and expression as v11swc6f, Josh mouth closed
    with dissolve

    u "That's how we're starting the night off? *Chuckles*"

    scene v11swc6f
    with dissolve

    jo "That's how I start every night, and you should too. Look at all these fine ass chicks."

    scene v11swc7 # FPP Show cute girl talking to her friend
    with dissolve

    pause 1.25

    scene v11swc8 # FPP Show another cute girl taking a drink
    with dissolve

    pause 1.25

    scene v11swc9 # FPP Show Ericka, Candy, and Jane at their table, talking to each other
    with dissolve

    u "If you say so."

    scene v11swc6h # FPP Same angle as v11swc6, Foxy talking to Josh, Foxy mouth open, Josh looking confused, mouth closed
    with dissolve

    foxy "Hey handsome, don't think I've seen you around here."

    scene v11swc6i # FPP Same angle and characters as v11swc6h, Foxy mouth closed, Josh mouth open
    with dissolve

    jo "I don't come here often, bro."

    scene v11swc6h
    with dissolve

    foxy "Oh please, save the bro stuff for your friend over there. I'm a queen, call me Foxy. Are you drunk yet?"

    scene v11swc6i
    with dissolve

    jo "Definitely not."

    scene v11swc6h
    with dissolve

    foxy "Find me when you are."

    scene v11swc10 # FPP Show Foxy walking away
    with dissolve

    jo "Definitely won't."

    scene v11swc6j # FPP Same angle as v11swc6f, Josh taking a shot of amber liquor
    with dissolve

    u "Trying to get drunk for your new girlfriend? *Chuckles*"

    scene v11swc6f
    with dissolve

    jo "Getting drunk to forget that happened. Look man, those girls over there keep looking at us."

    scene v11swc9a # FPP Same angle and characters as v11swc9, Ericka and Jane looking at MC and smiling, Candy looking bored
    with dissolve

    jo "Let's talk to them."

    scene v11swc11 # TPP Josh walking to Ericka, Candy, and Jane's table, MC following
    with dissolve

    pause 0.75
    
    scene v11swc9b # FPP Same angle and characters v11swc9, Ericka smiling mouth open, Jane smiling mouth closed, Candy still looking bored
    with dissolve

    ericka "We were wondering when you two would come say hi to us! What're your names?"

    scene v11swc9c # FPP Same angle, characters, and expressions as v11swc9b, Ericka mouth closed
    with dissolve

    u "Uhm, John."

    scene v11swc9b
    with dissolve

    ericka "Nice to meet \"Uhm John\". *Chuckles* And you?"

    scene v11swc9c
    with dissolve

    jo "Bruce."

    scene v11swc9b
    with dissolve

    ericka "My name's Ericka, this is Candy, and this is Jane."

    scene v11swc9c
    with dissolve

    u "Nice to meet you guys."

    scene v11swc9b
    with dissolve

    jane "We get that a lot. *Chuckles*"

    scene v11swc9d # FPP Same angle and characters as v11swc9b, Candy looking annoyed with mouth open
    with dissolve

    candy "Oh my god... I came here to drink. Unless one of these guys is gonna buy me a drink, I don't see why we're talking to them."

    scene v11swc9c
    with dissolve

    u "I'll get you a drink."

    scene v11swc9e # FPP Same angle and characters as v11swc9b, Candy smiling with mouth open
    with dissolve

    candy "Finally, a gentleman."

    scene v11swc12 # FPP Show Candy walking up to bar
    with dissolve

    pause 0.75

    scene v11swc13 # FPP Show Josh, grinning, mouth open
    with dissolve

    jo "Good luck."

    scene v11swc14 # FPP Show Josh walking away with Ericka and Jane, Josh has an arm around each girl
    with dissolve

    pause 0.75

    scene v11swc5c # TPP Same angle as v11swc5, MC and Candy at bar, Candy with mouth open and her hand up, getting Bartender's attention
    with dissolve

    candy "Excuse me?"

    scene v11swc6b
    with dissolve

    bartender "Yes ma'am, what can I get you?"

    scene v11swc6k # FPP Same angle as v11swc6f, show Candy looking at MC with a curious expression, mouth closed
    with dissolve

    menu:
        "Whatever you want":
            $ candyLike += 1

            scene v11swc6k
            with dissolve

            u "Whatever you want."

            scene v11swc6l # FPP Same as v11swc6k, Candy smiling with mouth open
            with dissolve

            candy "Surprise me."

        "Something cheap":
            scene v11swc6k
            with dissolve

            u "Something cheap."

            scene v11swc6m # FPP Same as v11swc6k, Candy looking annoyed, mouth open
            with dissolve

            candy "I'll just have a beer."

    scene v11swc6n # FPP Same as v11swc6k, Candy with neutral expression, mouth closed
    with dissolve

    u "You seem down, wanna talk about it?"

    scene v11swc6m
    with dissolve

    candy "*Sighs* You mean there's a guy in this world that actually cares to hear what I have to say?"

    menu:
        "Not really":
            scene v11swc6n
            with dissolve

            u "Not really what I came out to do, but I'm here now."

            scene v11swc6m
            with dissolve

            candy "Yeah, no one would actually choose to listen to my crappy life..."

        "Sure":
            $ candyLike += 1

            scene v11swc6n
            with dissolve

            u "Yeah, I'm always down for a good conversation."

            scene v11swc6l
            with dissolve

            candy "That's sweet."

    scene v11swc6m
    with dissolve

    candy "My boyfriend never listens to me and I swear he's fucking psycho. He's always trying to know where I am and shit. Like, I'm not your property. You know what I mean?"

    scene v11swc6n
    with dissolve

    u "Yeah, you definitely deserve a drink. Sounds like a stalker to me. *Chuckles*"

    scene v11swc6o # FPP Same as v11swc6k, Candy with neutral expression, mouth open
    with dissolve

    candy "Well, I mean, I don't know. Anyways, you have someone you're talking to?"

    menu:
        "Yes":
            scene v11swc6n
            with dissolve

            u "Yeah I do."

            scene v11swc6o
            with dissolve

            candy "Why are you here instead of with her?"

        "No":
            $ candyLike += 1

            scene v11swc6n
            with dissolve

            u "No I don't."

            scene v11swc6l
            with dissolve

            candy "I guess that's good news."

            scene v11swc6p # FPP Same as v11swc6k, Candy smiling with mouth closed
            with dissolve

            u "Why is that good news?"

            scene v11swc6l
            with dissolve

            candy "Cause that means I don't have to feel bad for talking to you. What made you come out tonight, single guy?"

    scene v11swc6n
    with dissolve

    u "Tonight I'm just chilling with my friend. He thought getting fucked up would be a good idea, but I'm not even sure where he ran off to."

    scene v11swc6o
    with dissolve
    
    candy "Sounds like your friend is smart. I'm sorry, what'd you say your name was again?"

    scene v11swc6k
    with dissolve

    u "It's [name]."

    scene v11swc6o
    with dissolve

    candy "I thought you said it was John or something..."

    scene v11swc6n
    with dissolve

    u "Oh uhm..."

    scene v11swc6l
    with dissolve

    candy "No worries. Candy isn't my real name either, but it's what I like to go by when I wanna go out and have fun."

    scene v11swc6p
    with dissolve

    u "That's smart, actually. Probably makes it harder for the creeps at the bar to stalk you on Kiwii."

    if candyLike != 3 and not reputation() == Reputations.POPULAR:
        if not reputation() == Reputations.POPULAR:
            call screen reputation_popup(required_reputation="popular")
    
        scene v11swc6o
        with dissolve

        candy "Yeah so, look - you're a really sweet guy and I'd love getting to hang out with you more, but I'm sure my boyfriend is looking for me. Maybe I'll see you another time."

        scene v11swc6n
        with dissolve

        u "Hopefully."

        scene v11swc15 # FPP Show Candy walking away
        with dissolve

        pause 0.75

        scene v11swc5e # TPP Same angle as v11swc5, show MC at bar, alone, looking around
        with dissolve

        pause 0.75

        scene v11swc15a # TPP Same angle as v11swc15, show crowd in the bar, Josh is nowhere to be seen
        with dissolve

        u "(Where's Josh?)"

        scene v11swc6b
        with dissolve

        bartender "Your buddy left with those two girls."

        scene v11swc15a
        with dissolve

        u "Should've known..."

        scene v11swc15a
        with dissolve

        u "(I should just go home and sleep.)"

        jump v11_thurs_night_room

    if candyLike != 3:
        call screen reputation_popup

    scene v11swc6l
    with dissolve

    candy "Yeah, so, you seem like a really caring guy..."

    scene v11swc5f # FPP Same angle as v11swc5, show Candy placing her hand on MCs, Candy smiling with mouth open
    with dissolve

    candy "Wanna head back to my place?"

    menu:
        "No":
            scene v11swc6p
            with dissolve

            u "I'm sorry, I'd love to, but I wouldn't want to get in between you and your man."

            scene v11swc6l
            with dissolve

            candy "Too bad I'm not single huh? See you around."

            scene v11swc15
            with dissolve

            pause 0.75

            scene v11swc5e
            with dissolve

            pause 0.75

            scene v11swc15a
            with dissolve

            u "(Where's Josh?)"

            scene v11swc6b
            with dissolve

            bartender "Your buddy left with those two girls."

            scene v11swc15a
            with dissolve

            u "Should've known..."

            scene v11swc15a
            with dissolve

            u "(I should just go home and sleep.)"

            jump v11_thurs_night_room

        "Yes":
            scene v11swc6p
            with dissolve

            u "That sounds nice."

    scene v11swc11a # TPP Same angle as v11swc11, Candy holding MC's hand, leading him away from bar
    with dissolve

    pause 0.75
    stop music fadeout 3
    play music "music/v11/Track Scene 5_4.mp3" fadein 2
    scene v11swc16 # TPP Outside of bar, Dannis walking up to MC and Candy, Dennis looks angry with mouth open
    with dissolve

    dennis "WHO THE FUCK IS THIS?"

    scene v11swc3e # FPP Outside of bar, show Candy looking worried, mouth open
    with dissolve

    candy "Dennis, uhm... he's my friend."

    scene v11swc3f # FPP Show Dennis looking angry, mouth open
    with dissolve

    dennis "Holding hands with a friend?"

    menu:
        "Yell back":
            scene v11swc3g # FPP Same angle as v11swc3f, Dennis looking angry with mouth closed
            with dissolve

            u "Yo, chill dude! Who even are you?"

            scene v11swc3f
            with dissolve

            dennis "THE FUCK?"

            scene v11swc16a # TPP Same angle as v11swc16, Show Dennis punching MC
            with dissolve
            play sound "sounds/facepunch1.mp3"

            pause 0.75
            
            scene v11swc16b # TPP Same angle as v11swc16, Dennis pulling Candy away by her hand, MC not in the frame
            with dissolve

            u "(I should've never come out tonight.)"

            scene v11swc17 # TPP Show MC laying on the ground
            with dissolve

            foxy "Oh poor baby, are you okay? Let me help you."

            scene v11swc16c # TPP Same angle as v11swc16, Foxy helping MC up, Foxy looks concerned, mouth open
            with dissolve

            foxy "Do you need a ride home, honey?"

            scene v11swc3h # FPP Show Foxy looking concerned, mouth closed
            with dissolve

            u "I'll be fine, thanks."

            scene v11swc16d # TPP Show MC walking away from bar, Foxy smacking him on the ass, Foxy's mouth open
            with dissolve

            foxy "Come back and see me sometime."

            scene v11swc18 # FPP View outside, night, on empty sidewalk
            with dissolve

            u "(What the actual fuck?)"

            jump v11_thurs_night_room

        "Act like family":
            $ sceneList.add("v11_candy")
            $ CharacterService.set_relationship(candy, Relationship.FWB, mc)

            scene v11swc16e # TPP Same angle and characters as v11swc16, MC puts one hand on his waist, stands in a faminine way, and holds his other hand up, wrist limp
            with dissolve
            
            u "She's my cousin, dude."

    scene v11swc3i # FPP Show Dennis looking confused, mouth closed
    with dissolve
    pause 0.75

    scene v11swc3j # FPP Show Candy, laughing, mouth open
    with dissolve

    candy "Oh my god. *Laughs*"

    scene v11swc3k # FPP Same angle as v11swc3i, Dennis looking confused with mouth open
    with dissolve
    
    dennis "Oh... uh... I've been blowing up your phone and I even drove by your place!"

    scene v11swc3j
    with dissolve

    candy "Obviously I've been with my cousin. I'll call you tomorrow."

    scene v11swc3i
    with dissolve

    u "See ya."

    scene v11swc16f # TPP Same angle and characters as v11swc16, Dennis walking away from MC and Candy
    with dissolve

    pause 1

    scene v11swc3j
    with dissolve

    candy "*Laughs* Nice save."

    scene v11swc19 # TPP Show MC and Candy walking through a neighborhood to her house
    with fade

    pause 1

label v11s5_galleryScene:

    scene v11swc20 # FPP At Candy's house, show Candy smiling, mouth closed
    with fade
    stop music fadeout 3
    play music "music/v11/Track Scene 5_5.mp3" fadein 2
    u "This is a nice place, you live here by yourself?"

    scene v11swc20a # FPP Same angle as v11swc20, Candy smiling with mouth open
    with dissolve

    candy "Yeah. I had a roommate but she just moved out last week, so the place is all mine until they stick me with a new one."

    scene v11swc20
    with dissolve

    u "Nice."

    scene v11swc20b # FPP Same angle as v11swc20, Candy facing away from MC, holding his hand, leading him toward the bedroom
    with dissolve

    candy "C'mon."

    scene v11swc21 # TPP Candy pushing MC back onto her bed, Candy smiling, mouth open
    with dissolve

    candy "My real name is Angelina by the way, but I do prefer Candy."

    scene v11swc22 # FPP Show Candy standing above MC, Candy smiling with mouth closed
    with dissolve

    $ grant_achievement("candy_crusher")
    u "Candy it is."

    if is_censored:
        call screen censored_popup("v11s5_nsfwSkipLabel1")

    scene v11swc21a # TPP Same angle as v11swc21, Candy removing her clothing
    with dissolve

    pause 1.25

    scene v11swc21b # TPP Same angle as v11swc21, Candy, now naked, undressing MC
    with fade

    stop music fadeout 3
    play music "music/v11/Track Scene 5_6.mp3" fadein 2
    pause 1.25

    image v11cbj = Movie(play="images/v11/Scene 5/v11canbj.webm", loop=True, image="images/v11/Scene 5/v11canbjStart.webp", start_image="images/v11/Scene 5/v11canbjStart.webp") # FPP Candy giving MC a blowjob
    image v11cbjf = Movie(play="images/v11/Scene 5/v11canbjf.webm", loop=True, image="images/v11/Scene 5/v11canbjStart.webp", start_image="images/v11/Scene 5/v11canbjStart.webp")
    image v11cbj2 = Movie(play="images/v11/Scene 5/v11canbjTPP.webm", loop=True, image="images/v11/Scene 5/v11canbjTPPStart.webp", start_image="images/v11/Scene 5/v11canbjTPPStart.webp") # FPP Candy giving MC a blowjob
    image v11cbj2f = Movie(play="images/v11/Scene 5/v11canbjTPPf.webm", loop=True, image="images/v11/Scene 5/v11canbjTPPStart.webp", start_image="images/v11/Scene 5/v11canbjTPPStart.webp")
    
    scene v11cbj # Candy giving MC a blowjob
    with fade

    u "Oh fuck."

    scene v11cbjf
    with dissolve
    
    u "This feels so fucking good."

    scene v11cbj2
    with dissolve

    u "*Grunts*"

    scene v11cbj2f
    with dissolve

    u "Oh my god, come here."

    scene v11swc22a # FPP. candy getting on top of MC ready to ride MC
    with dissolve

    pause 1

    scene v11swc22b # FPP. Close up of Candy, who is naked and riding MC. Candy smiling, with mouth closed
    with fade

    u "I'm glad I went out tonight."

    image v11ccg = Movie(play="images/v11/Scene 5/v11cancg.webm", loop=True, image="images/v11/Scene 5/v11cancgStart.webp", start_image="images/v11/Scene 5/v11cancgStart.webp") # TPP Candy riding MC, their faces near each other
    image v11ccgf = Movie(play="images/v11/Scene 5/v11cancgf.webm", loop=True, image="images/v11/Scene 5/v11cancgStart.webp", start_image="images/v11/Scene 5/v11cancgStart.webp")
    image v11ccg2 = Movie(play="images/v11/Scene 5/v11cancgFPP.webm", loop=True, image="images/v11/Scene 5/v11cancgFPPStart.webp", start_image="images/v11/Scene 5/v11cancgFPPStart.webp") # TPP Candy riding MC, their faces near each other
    image v11ccg2f = Movie(play="images/v11/Scene 5/v11cancgFPPf.webm", loop=True, image="images/v11/Scene 5/v11cancgFPPStart.webp", start_image="images/v11/Scene 5/v11cancgFPPStart.webp")

    candy "I am too."

    scene v11ccg # Candy riding MC, their faces close to each other
    with dissolve
    pause

    candy "Oh God."

    scene v11ccgf
    with dissolve

    candy "Oh yes!"

    scene v11ccg2
    with dissolve

    u "Fuck... You're amazing."

    scene v11ccg2f
    with dissolve

    candy "*Moans*"

    image v11cmi = Movie(play="images/v11/Scene 5/v11cmi.webm", loop=True, image="images/v11/Scene 5/v11cmiStart.webp", start_image="images/v11/Scene 5/v11cmiStart.webp") # TPP MC and Candy having sex in missionary position
    image v11cmif = Movie(play="images/v11/Scene 5/v11cmif.webm", loop=True, image="images/v11/Scene 5/v11cmiStart.webp", start_image="images/v11/Scene 5/v11cmiStart.webp")

    scene v11scw34 # FPP. Show candy now closer to MC's face like in the v10cmi animation.
    with dissolve

    scene v11cmi # MC and Candy in missionary position
    with dissolve

    candy "YESSSSS!"

    scene v11cmif
    with dissolve

    candy "FUCK ME!"

    image v11cdg = Movie(play="images/v11/Scene 5/v11cdg.webm", loop=True, image="images/v11/Scene 5/v11cdgStart.webp", start_image="images/v11/Scene 5/v11cdgStart.webp") # TPP MC rolls Candy over onto her knees and performs doggystyle while holding her arms back-
    image v11cdgf = Movie(play="images/v11/Scene 5/v11cdgf.webm", loop=True, image="images/v11/Scene 5/v11cdgStart.webp", start_image="images/v11/Scene 5/v11cdgStart.webp")

    scene v11scw35 # FPP. Show Candy on her hands and knee's ready for doggy style like in the v10cdg animation
    with dissolve

    u "Turn around for me."

    scene v11cdg # MC and Candy having sex doggy style
    with dissolve

    candy "I needed this so bad!"

    scene v11cdgf
    with dissolve

    candy "I'm gonna cum."

    scene v11swc23 # FPP Show Candy from behind while having sex doggy style
    with dissolve

    u "Me too."

    scene v11swc23
    with dissolve

    candy "Don't pull out, it's fine."

    scene v11swc21c # TPP Same angle as v11swc21, MC and Candy finishing in doggy style
    with flash

    pause 0.75

    scene v11swc36 # FPP. Show Candy with cum dripping out her pussy, same position as v10cdg animation
    with dissolve

    pause 0.75

    scene v11swc24 # TPP MC and Candy laying beside each other in bed, both with small smiles, Candy's mouth open
    with dissolve

    candy "That was exactly what I needed."

    label v11s5_nsfwSkipLabel1:

    scene v11swc25 # FPP Show Candy, laying in bed, smiling with mouth closed
    with dissolve

    u "Glad I could help."

    scene v11swc25a # FPP Same angle as v11swc25, Candy looking scared
    with dissolve

    dennis "ANGELINA! WHO THE FUCK IS THAT IN THERE WITH YOU? I HEAR YOU IN THERE FUCKING!"

    scene v11swc21d # TPP Same angle as v11swc21, MC frantically putting his clothes on
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v11/Track Scene 5_7.mp3" fadein 2

    scene v11swc26 # FPP View of the bedroom door
    with dissolve

    u "Oh fuck!"

    play sound "sounds/slam.mp3"

    scene v11swc26a # FPP Same angle as v11swc26, Dennis kicking in bedroom door, looking angry with mouth open
    with dissolve

    dennis "You motherfucker!"

    scene v11swc26b # FPP Same angle as v11swc26, Dennis rushing toward MC with his fists clenched
    with dissolve

    menu:
        "Dodge":
            scene v11swc27 # TPP Dennis throwing a punch at MC, MC dodging
            with dissolve

            pause 0.75

            scene v11swc27a # TPP MC rushing out of the door to Candy's bedroom
            with dissolve
            
            pause 0.75

            scene v11swc28 # FPP Show Dennis looking very angry, mouth closed
            with dissolve

            u "FUCK YOU DENNIS!"

        "Run":
            scene v11swc27b # TPP MC tripping as he tries to run away from Dennis
            with dissolve

            pause 0.75

            scene v11swc27c # TPP Dennis stomping on MC's back
            with dissolve

            pause 0.75

            if not is_censored:
                scene v11swc29 # FPP MC's view while on the bedroom floor
                with dissolve
    
            u "FUCK!"

            scene v11swc27d # TPP MC getting up and running out the door
            with dissolve

            pause 0.75

            scene v11swc28
            with dissolve

            u "FUCK YOU DENNIS!"

    scene v11swc30 # TPP MC outside, walking home
    with fade

    pause 0.75

    scene v11swc18
    with dissolve
    
    u "Pheww."

    stop music fadeout 3

    $ renpy.end_replay()

jump v11_thurs_night_room