# SCENE 14b: Afterparty with Penelope
# Locations: Club, Hotel Lobby
# Characters: MC (Outfit: 2), PENELOPE (Outfit: 3)
# Time: Wednesday night

label v13s14b:
    # -Upbeat club music is playing-

    scene v13s14b_1 # TPP Show MC, Penelope, and Polly just inside the club entrance, looking around
    with dissolve

    pause 0.75

    play music music.v13_Track_Scene_14a_1 fadein 2

    #scene v13s14b_2 # FPP MC's view as he looks around the club
    scene v13s14b_1
    with dissolve
    
    u "Oh shit, this is a club, club!"

    scene v13s14b_3 # FPP Show Polly looking at MC, smiling with mouth open
    with dissolve

    polly "*Chuckles* What were you expecting?"

    #scene v13s14b_2
    scene v13s14b_1
    with dissolve

    u "I don't know, but I wasn't expecting this..."

    scene v13s14b_4 # FPP Show Penelope looking around club, smiling with mouth open
    with dissolve

    pe "Holy... I love this! I've only seen clubs like this on TV. *Chuckles*"

    scene v13s14b_3a # FPP Same as 3, Polly looking at Penelope
    with dissolve

    polly "So you do have a fun side? *Chuckles* I was hoping you'd like this type of scene. Do you drink?"

    scene v13s14b_4a # FPP Same as 4, Penelope looking at Polly, neutral expression, mouth open
    with dissolve

    pe "Oh, no. I'm not a really big drinker."

    scene v13s14b_3a
    with dissolve

    polly "Oh, c'mon... You can have one drink."

    scene v13s14b_4b # FPP Same as 4, Penelope looking at MC, worried expression, mouth closed
    with dissolve

    u "One shouldn't hurt."

    scene v13s14b_4a
    with dissolve

    pe "Alright, just something simple though..."

    scene v13s14b_3b # FPP Same angle as 3, Polly holding her hand to her mouth to yell at someone farther in the club
    with dissolve

    polly "I can make that work. Hey! Dickhead! Bring us some beers!"

    scene v13s14b_5 # FPP Show random guy from the concert walking over carrying a tray of beers, mouth open
    with dissolve

    random_guy "Here you go."

    scene v13s14b_5a # FPP Same angle as 5, random guy standing nearby with tray of beers, mouth closed
    with dissolve

    u "What the hell is this dick doing here?"

    scene v13s14b_3
    with dissolve

    polly "So you don't like him either, good. He was being an ass to my fans and went against concert rules, so rather than pressing charges he agreed to be my little helper for the night."

    scene v13s14b_5b # FPP Same angle as 5, random guy looking at Penelope and laughing, mouth open
    with dissolve

    random_guy "You guys aren't having this softie here, drink are you? *Scoffs*"
    random_guy "Don't look at me when she's sitting on her ass. *Laughs*"

    scene v13s14b_3c # FPP Same angle as 3, Polly looking at random guy, angry with mouth open
    with dissolve

    polly "Don't talk to my sis like that you fucking dickbag!"

    scene v13s14b_6 # FPP Show Polly angrily grabbing a beer from the tray that random guy is holding
    with dissolve

    pause 0.5

    scene v13s14b_7 # FPP Show Polly handing beer to Penelope, Polly smiling with mouth open, Penelope looking worried
    with dissolve

    polly "Chug it!"

    scene v13s14b_4b
    with dissolve

    u "*Chuckles* Don't look at me."

    scene v13s14b_4c # FPP Same angle as 4, Penelope looking at her beer with a neutral expression, mouth open
    with dissolve

    pe "*Sighs* Bottoms up..."

    scene v13s14b_8 # FPP Show Penelope tilting her drink way back, chugging it
    with dissolve

    pause 0.75

    scene v13s14b_4d # FPP Same angle as 4, Penelope holding her empty beer, she has a disgusted expression, mouth open
    with dissolve

    pe "Ugh! That's so gross..."

    scene v13s14b_3a
    with dissolve

    polly "The taste doesn't matter, sister! It's the vibe you get from the chug that counts. *Chuckles*"

    scene v13s14b_4d
    with dissolve

    pe "Hopefully it's a good vibe."

    scene v13s14b_3a
    with dissolve

    polly "If you're anything like me, you'll think it's good."

    scene v13s14b_4e # FPP Same angle as 4, Penelope looking at Polly, smiling with mouth open
    with dissolve

    pe "*Chuckles* I'm a lot like you so far."

    scene v13s14b_3a
    with dissolve

    polly "See? You're loosening up already!"

    scene v13s14b_4f # FPP Same angle as 4, Penelope smiling at MC, mouth closed
    with dissolve

    u "Are you planning on getting out of your shell tonight?"

    scene v13s14b_4g # FPP Same as 4f, Penelope smiling with mouth open
    with dissolve

    pe "It's the only night of freedom I'll have for a while so... Yeah, I guess kinda."

    scene v13s14b_9 # FPP Show Penelope taking a beer out of Polly's hand
    with dissolve

    pause 0.5

    scene v13s14b_8
    with dissolve

    polly "Yes ma'am! Two down!"

    scene v13s14b_4e
    with dissolve

    pe "Woah, I can definitely feel it working its magic. *Chuckles*"

    scene v13s14b_4f
    with dissolve

    menu:
        "Impressive":
            u "This is low-key impressive. *Laughs*"

            scene v13s14b_10 # FPP Show Penelope cheering with her hand in the air, big smile, mouth open
            with dissolve

            pe "*Tipsy* Round of applause for Penelope!"

            scene v13s14b_11 # TPP Show MC, Polly, and Penelope clapping and laughing, everyone looking at Penelope, Polly's mouth open
            with dissolve

            polly "Which one? *Laughs*"

        "You should stop":
            u "You should slow down a bit."

            scene v13s14b_3a
            with dissolve

            polly "Buzz kill! You need to drink more!"

            scene v13s14b_4h # FPP Same angle as 4, Penelope looking at Polly with a big, drunk smile, mouth closed
            with dissolve

            u "Oh, god..."

    # -Regardless of choice scene continued

    scene v13s14b_4g
    with dissolve
    
    pe "*Tipsy* C'mon, [name]! I wanna dance."

    scene v13s14b_3a
    with dissolve

    polly "Take him to the floor, sis."

    scene v13s14b_12 # TPP Show Penelope holding MC's hand, dragging him to the dance floor
    with dissolve

    pause 0.5

    scene v13s14b_13 # TPP Show Penelope dancing with MC, her dancing on him with her back to him
    with dissolve

    pause 0.5

    scene v13s14b_13a # TPP Same angle as 13, Penelope really getting into the dance, MC starting to dance with her
    with dissolve

    pause 0.5

    scene v13s14b_13b # TPP Same angle as 13, Penelope now turned around and dancing very close to MC, face to face
    with dissolve

    pause 0.5

    scene v13s14b_14 # FPP Show Penelope, close to MC, dancing and looking at him, smiling with mouth closed
    with dissolve

    u "You're turned all the way up right now. *Chuckles*"

    scene v13s14b_14a # FPP Same as 14, Penelope's mouth open
    with dissolve

    pe "*Drunk* Haha, I'm so happy!"

    scene v13s14b_15 # TPP Show Penelope with her hands on MC's cheeks, whispering into his ear
    with dissolve

    pe "*Drunk* You're so handsome, I just wanna eat you up..."

    scene v13s14b_16 # FPP Show Penelope, with her hands out on MC's shoulders, smiling with her mouth closed
    with dissolve

    menu:
        "Be a gentleman":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            u "Penelope, you're pretty drunk. *Chuckles* I should get you back so you can get a good night's worth of sleep."

            scene v13s14b_16a # FPP Same angle as 16, Penelope dissapointed but still smiling, mouth open
            with dissolve

            pe "*Drunk* Aww..."

            scene v13s14b_16b # FPP Same angle as 16, Penelope smiling at MC, mouth open
            with dissolve

            pe "Okay, handsome boy. If we have too."

            scene v13s14b_17 # FPP Show Polly walking toward MC and Penelope on the dance floor
            with dissolve

            pause 0.75

            scene v13s14b_18 # FPP Polly on the dance floor, looking at MC, smiling with mouth closed
            with dissolve

            u "Hey Polly, I'm gonna get her home."

            scene v13s14b_18a # FPP Same angle as 17, Polly looking at Penelope, mouth open
            with dissolve

            polly "She kicked over the can, huh? *Chuckles*"

            scene v13s14b_18
            with dissolve

            u "You could say that. *Chuckles*"

        "Have fun":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            u "I may just let you..."

            play sound sound.kiss
            scene v13s14b_15a # TPP Same angle as 15, Penelope kissing and nibbling MC's neck
            with dissolve

            pause 0.75

            scene v13s14b_16c # FPP Same angle as 16, only part of Penelope's head visible, as she is kissing MC's neck
            with dissolve

            u "Mmm..."
            u "Wait... Are you trying to give me a hickey?"

            scene v13s14b_16b
            with dissolve

            pe "*Drunk* We have to remember our night together... *Chuckles*"

            scene v13s14b_15b # TPP Same angle as 15, Penelope has her arms around MC, her head against his chest, and her eyes closed
            with dissolve

            pause 0.75

            scene v13s14b_19 # FPP MC looking down at Penelope, who is hugging him with her head against his chest
            with dissolve

            u "Penelope, are you okay?"

            scene v13s14b_19a # FPP Same angle as 19, Penelope looking up slightly at MC, mouth open
            with dissolve

            pe "*Drunk* I'm a little dizzy..."

            scene v13s14b_19
            with dissolve

            u "Are you-"

            scene v13s14b_20 # TPP Show Penelope sitting roughly on the ground, holding on to MC's leg
            with dissolve

            pause 0.75

            scene v13s14b_21 # FPP MC looking down at Penelope, who is sitting on the floor holding MC's leg, looking up at him, smiling with mouth closed
            with dissolve

            u "(Oh, fuck.)"

            scene v13s14b_21a # FPP Same as 21, Penelope's mouth open
            with dissolve

            pe "*Drunk* This is a funny night... *Laughs*"

            scene v13s14b_17
            with dissolve

            pause 0.75

            scene v13s14b_18b # FPP Show Polly looking down at Penelope, surprised expression, mouth open
            with dissolve

            polly "Oh, wow... Someone's off the rocker. *Chuckles*"

            scene v13s14b_21b # FPP Same angle as 21, Penelope has her eyes closed
            with dissolve

            u "Yeah, I probably should've paid closer attention to her before it got this bad..."

            scene v13s14b_18c # FPP Same angle as 18, Polly smiling down at Penelope, mouth open
            with dissolve

            polly "She'll be fine. Let me get you a ride."

    # -Regardless of choice scene continued

    scene v13s14b_18d # FPP Same angle as 18, Polly shouting off into the distance
    with dissolve

    polly "Hey dickhead, get the chauffeur ready!"

    scene v13s14b_18
    with dissolve

    u "Haha, thanks."

    scene v13s14b_18e # FPP Same angle as 18, Polly smiling at MC, mouth open
    with dissolve

    polly "No problem. I'll be looking forward to seeing you guys when I'm in America. I'll even come perform, wherever you guys want."

    scene v13s14b_18
    with dissolve

    u "Sounds great. Really, this has been awesome. Thanks."

    scene v13s14b_18e
    with dissolve

    polly "Go ahead and meet them out in the front."

    scene v13s14b_18
    with dissolve

    u "Cool, later Polly."

    scene v13s14b_18e
    with dissolve

    polly "Later, take care of my sis!"

    scene v13s14b_18
    with dissolve

    u "I will."

    scene v13s14b_22 # TPP Show MC bending down to pick up Penelope, who is limp with her eyes closed
    with dissolve

    pause 0.75

    scene v13s14b_23 # TPP Show MC carrying Penelope. Penelope still has her eyes closed, smiling with her mouth open
    with dissolve

    pe "*Drunk* I'm flying!!!"

    scene v13s14b_24 # FPP MC's view as he carries Penelope toward the door to the club
    with dissolve

    grant Achievement("funny_night", "Yes Penelope, you're flying")
    u "Haha... Yes Penelope, you're flying."

    stop music fadeout 3
    play music music.ck1.v13.Track_Scene_12a_2 fadein 2

    scene v13s14b_25 # TPP Show MC helping Penelope into the car. Penelope's eyes still closed
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music music.ck1.v13.Track_Scene_14b fadein 2

    scene v13s14b_26 # TPP Show MC carrying Penelope through the hotel lobby
    with dissolve

    pause 0.75

    scene v13s14b_27 # TPP Show MC placing Penelope, who is asleep, into her bed
    with dissolve

    pause 0.75

    scene v13s14b_28 # TPP Show MC walking back to his room
    with dissolve

    pause 0.75

    stop music fadeout 3

    if v11_riley_roomate:
        jump v13s15a

    else:
        jump v13s15