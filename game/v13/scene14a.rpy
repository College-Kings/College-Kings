# SCENE 14a: Afterparty with Aubrey
# Locations: Club
# Characters: MC (Outfit: 2), AUBREY (Outfit: 1)
# Time: Night

label v13s14a:
    # -Upbeat club music is playing-

    scene v13s14a_1 # TPP Show MC, Aubrey, and Polly just inside the club entrance, looking around
    with dissolve

    pause 0.75

    play music "music/v13/Track Scene 14a_1.mp3" fadein 2

    #scene v13s14a_2 # FPP MC's view as he looks around the club
    scene v13s14a_1
    with dissolve

    u "Oh shit, this is a club, club!"

    scene v13s14a_3 # FPP Show Polly looking at MC, smiling with mouth open
    with dissolve

    polly "*Chuckles* What were you expecting?"

    #scene v13s14a_2
    scene v13s14a_1
    with dissolve

    u "I don't know, but I wasn't expecting this..."

    scene v13s14a_4 # FPP Show Aubrey looking at MC, smiling with mouth open
    with dissolve

    au "Haha, you look super shocked. This is the life you live when you're an icon..."

    scene v13s14a_3a # FPP Same as 3, Polly looking at Aubrey
    with dissolve

    polly "He'll never know what that's like. *Laughs*"

    scene v13s14a_4a # FPP Same as 4, Aubrey looking at Polly
    with dissolve

    au "True!"

    scene v13s14a_5 # FPP Show Polly and Aubrey, both looking at MC and smiling with mouths closed
    with dissolve

    u "Ganging up on me, huh?"

    scene v13s14a_3
    with dissolve

    polly "You'd like that, wouldn't you?"

    scene v13s14a_5
    with dissolve

    menu:
        "Plead the fifth": 
            $ add_point(KCT.TROUBLEMAKER)

            u "I plead the fifth. *Chuckles*"

            scene v13s14a_3
            with dissolve

            polly "I think I got my answer. *Laughs*"

        "I'm a one woman man":
            $ add_point(KCT.BOYFRIEND)

            u "I'm a one woman-man."

            scene v13s14a_4
            with dissolve

            au "Are you sure about that?"

            scene v13s14a_4b # FPP Same as 4, Aubrey looking at MC, mouth closed
            with dissolve

            u "*Chuckles* Positive."

            scene v13s14a_3
            with dissolve

            polly "Interesting... *Chuckles*"

    # -Regardless of choice scene continued
    scene v13s14a_3a
    with dissolve

    polly "Let's get some drinks!"

    scene v13s14a_4a
    with dissolve

    au "Yes!"

    scene v13s14a_3b # FPP Same angle as 3, Polly holding her hand to her mouth to yell at someone farther in the club
    with dissolve

    polly "Hey! Dickhead! Bring us some beers!"

    scene v13s14a_6 # FPP Show random guy from the concert walking over carrying a tray of beers, mouth open
    with dissolve

    random_guy "Here you go."

    scene v13s14a_6a # FPP Same angle as 6, random guy standing nearby with tray of beers, mouth closed
    with dissolve

    u "What the hell is this dick doing here?"

    scene v13s14a_3
    with dissolve

    polly "So, you don't like him either? Good."

    scene v13s14a_3c # FPP Same angle as 3, Polly looking at random guy, smiling with mouth open
    with dissolve

    polly "He was being an ass to my fans and went against concert rules, so rather than pressing charges he agreed to be my little helper for the night."

    scene v13s14a_7 # FPP Show Aubrey grabbing a drink from random guy's tray, Aubrey smiling with mouth open
    with dissolve

    au "Karma's a bitch, bitch. *Chuckles*"

    scene v13s14a_7a # FPP Same angle as 7, Aubrey holding beer, mouth closed, random guy's mouth open
    with dissolve

    random_guy "Don't talk to-"

    scene v13s14a_3a
    with dissolve

    polly "*Laughs* That's hilarious, I'm gonna have to steal that."

    scene v13s14a_8 # FPP Show random guy forcefully pushing a beer into MC's chest, MC smiling and taking the beer
    with dissolve

    pause 0.75

    scene v13s14a_6b # FPP Same angle as 6, random guy walking away, mouth open (if visible)
    with dissolve

    random_guy "Fuck off!"

    scene v13s14a_3b
    with dissolve

    polly "Aww... Poor baby, that's what you get when you wanna be an ass!"

    scene v13s14a_9 # FPP Show Aubrey tilting her drink way back, chugging it
    with dissolve

    pause 0.75

    scene v13s14a_9a # FPP Same angle as 9, Aubbrey holding a now empty drink, looking at MC, mouth open
    with dissolve

    au "Let's dance!"

    scene v13s14a_10 # TPP Show Aubrey holding MC's hand, dragging him onto the dance floor
    with dissolve

    polly "You two have fun! *Chuckles*"

    scene v13s14a_11 # FPP Show Aubrey, now on dance floor, smiling with mouth closed
    with dissolve

    u "I forgot how much you like to dance. *Laughs*"

    scene v13s14a_11a # FPP Same as 11, Aubrey's mouth open
    with dissolve

    au "Love, love, love to dance!"

    scene v13s14a_11
    with dissolve

    u "*Chuckles* Show me what you got."

    scene v13s14a_11a
    with dissolve

    au "I don't want to show you up... My skills would embarrass you. *Laughs*"

    scene v13s14a_11
    with dissolve

    u "Oh, you don't think I can keep up?"

    scene v13s14a_11a
    with dissolve

    au "Not with this."

    scene v13s14a_12 # FPP Show Aubrey beginning to dance, dance is skillful and sexy
    with dissolve

    pause 0.5

    scene v13s14a_12a # FPP Same angle as 12, more of Aubrey dancing, really getting into it
    with dissolve

    pause 0.5

    scene v13s14a_12b # FPP Same angle as 12, last view of Aubrey dancing, looking at MC
    with dissolve

    pause 0.5

    scene v13s14a_11
    with dissolve

    u "Please! That was nothing."

    scene v13s14a_13 # TPP Show MC with his elbows locked, beginning to do the robot
    with dissolve

    pause 0.5

    scene v13s14a_13a # TPP Same angle as 13, MC doing the robot, Aubrey watching, trying not to laugh
    with dissolve

    pause 0.5

    scene v13s14a_13b # TPP Same angle as 13, final image of MC dancing the robot, MC bending over like robot shutting down
    with dissolve

    pause 0.5

    scene v13s14a_11b # FPP Same angle as 11, Aubrey laughing, mouth open
    with dissolve
    
    au "I know you didn't just do the damn robot! *Laughs*"

    scene v13s14a_11
    with dissolve

    u "These are moves of the future, girl! Don't be a hater..."

    scene v13s14a_11a
    with dissolve

    au "Haha!"

    stop music fadeout 3
    play music "music/v13/Track Scene 14a_2.mp3" fadein 2

    # -The song changes to something slow and romantic-
    scene v13s14a_14 # TPP Show MC and Aubrey both looking up as if focussing on the song that just came on
    with dissolve

    pause 1

    scene v13s14a_11
    with dissolve

    u "Oh, that's a big music swing! *Chuckles*"

    scene v13s14a_11a
    with dissolve

    au "Uhh, yeah. Definitely a vibe change. *Chuckles*"

    scene v13s14a_11
    with dissolve

    menu:
        "Killed the vibe":
            u "More like a vibe killer..."

            scene v13s14a_11a
            with dissolve

            au "That's exactly what I was thinking, haha. Wanna get out of here before it gets worse?"

            scene v13s14a_11
            with dissolve
            u "Haha, yes please."

            scene v13s14a_11a
            with dissolve

            au "*Chuckles* Think we can walk back?"

            scene v13s14a_11
            with dissolve

            u "Yeah, it's not too far."

            stop music fadeout 3
            play music "music/v13/Track Scene 12a_2.mp3" fadein 2

            scene v13s14a_15 # TPP Show MC and Aubrey walking along the streets of Amsterdam late at night
            with dissolve

            pause 0.75

            scene v13s14a_16 # TPP Show MC and Aubrey entering the hotel lobby
            with dissolve

            pause 0.75

            stop music fadeout 3
            play music "music/v13/Track Scene 12a_1.mp3" fadein 2

            scene v13s14a_17 # FPP Show Aubrey, in hotel lobby, now speaking with MC, Aubrey smiling with mouth open
            with dissolve

            au "Tonight was definitely a night I will remember forever."

            scene v13s14a_17a # FPP Same as 17, Aubrey's mouth closed
            with dissolve

            u "How could you, Miss. \"soon-to-be Superstar\"?"

            scene v13s14a_17b # FPP Same angle as 17, Aubrey rolling her eyes and laughing slightly, mouth open
            with dissolve

            au "Haha, oh my god. Goodnight, [name]."

            scene v13s14a_17a
            with dissolve

            u "Haha, goodnight Aubrey."

            scene v13s14a_18 # TPP Show MC walking to his room
            with dissolve

            pause 0.75

            stop music fadeout 3

            if v11_riley_roomate:
                jump v13s15a

            else:
                jump v13s15

        "Dance with Aubrey":
            $ aubrey.points += 1

            scene v13s14a_19 # TPP Show MC taking Aubrey's hand and putting his hand on her waist
            with dissolve

            pause 0.5

            scene v13s14a_20 # TPP Show MC, with his hand around Aubrey's waist, pulling her within inches of his face to slow dance, Aubrey surprised with mouth open
            with dissolve

            au "Oh! Wow, I..."

            scene v13s14a_21 # FPP Show MC, with his hand around Aubrey's waist, pulling her within inches of his face to slow dance, Aubrey surprised with mouth open
            with dissolve

            u "What?"

            scene v13s14a_21a # FPP Same angle as 21, Aubrey smiling with mouth open
            with dissolve

            au "Ha, um... Nothing, nevermind."

            scene v13s14a_22 # TPP Show MC and Aubrey dancing romantically, both smiling
            with dissolve

            pause 0.5

            scene v13s14a_23 # TPP Another angle of MC and Aubrey dancing, Aubrey with her head on MC's shoulder, her eyes closed
            with dissolve

            pause 0.5

            scene v13s14a_22a # TPP Same angle as 22, final shot of MC and Aubrey dancing, Aubrey looking up into MC's eyes and smiling
            with dissolve

            scene v13s14a_21a
            with dissolve

            au "You wanna get out of here?"

            scene v13s14a_21b # FPP Same angle as 21, Aubrey smiling, mouth closed
            with dissolve

            u "I'd be happy too."

            scene v13s14a_21a
            with dissolve

            au "Think we can walk?"

            scene v13s14a_21b
            with dissolve

            u "Sure, c'mon..."

            stop music fadeout 3
            play music "music/v13/Track Scene 12a_2.mp3" fadein 2

            scene v13s14a_15
            with dissolve

            pause 0.75

            scene v13s14a_16
            with dissolve

            pause 0.75

            stop music fadeout 3
            play music "music/v13/Track Scene 12a_1.mp3" fadein 2

            scene v13s14a_17
            with dissolve

            au "Tonight was definitely a night I will remember forever."

            scene v13s14a_17a
            with dissolve

            u "How could you, Miss. \"soon-to-be Superstar\"?"

            scene v13s14a_17b
            with dissolve

            au "Haha, oh my god. Goodnight [name]."

            scene v13s14a_17a
            with dissolve

            u "Haha, goodnight Aubrey."

            scene v13s14a_24 # FPP Show Aubrey, in hotel lobby, walking away toward hallway to the rooms
            with dissolve

            pause 0.5

            scene v13s14a_24a # FPP Same angle as 24, Aubrey a few steps toward hallway, turning and looking at MC, neutral expression, mouth open
            with dissolve

            au "Oh. umm... [name]?"

            scene v13s14a_24b # FPP Same as 24a, Aubrey's mouth closed
            with dissolve

            u "Yeah?"

            scene v13s14a_24a
            with dissolve

            au "I just wanted to say that..."

            scene v13s14a_24c # FPP Same as 24a, Aubrey's smiling with mouth open
            with dissolve

            au "I've never danced with anyone like that before, and I really enjoyed it. Maybe we can go dancing again, sometime?"

            scene v13s14a_24d # FPP Same as 24c, Aubrey smiling with mouth closed
            with dissolve

            u "I'd like that."

            scene v13s14a_24c
            with dissolve

            au "Okay... Ha, good."

            au "Well, goodnight, for real this time. *Chuckles*"

            scene v13s14a_25 # TPP Show MC walking up to Aubrey
            with dissolve

            pause 0.5

            play sound "sounds/kiss.mp3"
            scene v13s14a_25a # TPP Same angle as 25, MC kissing Aubrey
            with dissolve

            pause 0.75

            scene v13s14a_26 # FPP Show Aubrey, very close to MC, smiling with mouth closed
            with dissolve

            u "*Chuckles* Goodnight."

            scene v13s14a_27 # FPP Show Aubrey walking away toward her room
            with dissolve

            pause 0.75

            scene v13s14a_18
            with dissolve

            pause 0.75

            stop music fadeout 3
            
            if v11_riley_roomate:
                jump v13s15a

            else:
                jump v13s15