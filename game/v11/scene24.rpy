# SCENE 24: MC and Nora walk to Big Ben
# Location: London streets
# Characters: MC (Outfit 1), Nora (Outfit 1)
# Time: Evening

label v11_big_ben:
    scene v11bb1 # FPP Show Nora, neutral expression, mouth closed
    with dissolve
    play music "music/v11/Track Scene 5_5.mp3" fadein 2
    u "So, I know pretty much nothing about London..."

    scene v11bb1a # FPP Same angle as v11bb1, Nora with neutral expression, mouth open
    with dissolve

    no "When people say they know nothing that either means they truly know nothing or know hardly anything. Which one is it for you?"

    scene v11bb1
    with dissolve

    u "Absolutely nothing."

    scene v11bb1b # FPP Same angle as v11bb1, Nora smiling with mouth open
    with dissolve

    no "You didn't look up some stuff before the trip? *Chuckles*"

    scene v11bb1c # FPP Same angle as v11bb1, Nora smiling with mouth closed
    with dissolve

    u "Nope."

    scene v11bb1a
    with dissolve

    no "Haha, well allow me to inform you. The first thing you need to know is that London is under the rule of a Queen."

    scene v11bb1
    with dissolve

    u "Well, I know that."

    scene v11bb1b
    with dissolve

    no "See? You do know some stuff."

    scene v11bb1c
    with dissolve

    u "*Laughs*"

    scene v11bb1a
    with dissolve

    no "Let's see, what's something interesting... Oh! Did you know Big Ben isn't actually meant to be called that? It's called The Clock Tower. The Big Ben is actually the bell."

    scene v11bb1
    with dissolve

    u "When did you look this stuff up?"

    scene v11bb1d # FPP Same angle as v11bb1, Nora laughing
    with dissolve

    no "*Laughs* I didn't look it up, I learned it in school."

    scene v11bb1c
    with dissolve

    u "They didn't teach me that."

    scene v11bb1a
    with dissolve

    no "What about black cab drivers?"

    scene v11bb1
    with dissolve

    u "What about them?"

    scene v11bb1a
    with dissolve

    no "Black cab drivers have to take a test called \"The Knowledge\" which makes them memorize every single street in the capital."
    no "It takes years for some of them to pass."

    scene v11bb1
    with dissolve

    u "Uh that's..."

    scene v11bb1b
    with dissolve

    no "Black cabs, not black drivers."

    scene v11bb1c
    with dissolve

    u "Glad you explained that cause I was a little confused. *Chuckles*"

    scene v11bb1b
    with dissolve

    no "That would be terrible."
    
    scene v11bb1a
    with dissolve

    no "There's also over 170 museums in London. Mr. Lee just decided to take us to some amateur one."

    scene v11bb1
    with dissolve

    u "Don't hate on the amateurs. *Laughs*"

    scene v11bb1b
    with dissolve

    no "*Chuckles* I'm just saying."

    scene v11bb2 # Show London Black Cab (one of the range rovers we have will do, just play with the angles)
    with dissolve

    u "Is that one of those cabs?"

    scene v11bb2
    with dissolve

    no "Sure is, but they're way too expensive *Chuckles* Let's just use a rideshare app."

    scene v11bb3 # TPP Show MC and Nora climbing into the back of the Uber
    with dissolve

    pause 0.75

    scene v11bb4 # FPP Show Nora in back of Uber looking toward the driver, neutral expression, mouth open
    with dissolve

    no "To the clock tower please."

    scene v11bb4a # FPP Same angle as v11bb4, Nora mouth closed
    with dissolve

    driver "Perfect."

    scene v11bb5 # TPP Show MC and Nora in the back of the black cab, Big Ben in the background
    with dissolve

    pause 0.75

    scene v11bb4
    with dissolve

    no "There it is."

    scene v11bb4a
    with dissolve

    u "Where?"

    scene v11bb4b # FPP Same angle as v11bb4, Nora smiling with mouth open
    with dissolve

    no "The big clock right there. *Chuckles*"

    scene v11bb4c # FPP Same angle as v11bb4, Nora smiling with mouth closed
    with dissolve

    u "Oh! *Chuckles*"

    scene v11bb6 # TPP Show MC and Nora getting out of the Uber
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v11/Track Scene 7_2.mp3" fadein 2

    scene v11bb7 # FPP Show Nora looking up toward the clock tower, smiling with mouth open
    with dissolve

    no "It's a lot bigger than I thought it was."

    scene v11bb7a # FPP Same angle as v11bb7, Nora looking up at tower, smiling with mouth closed
    with dissolve

    u "*Whisper* That's what she said."

    scene v11bb7
    with dissolve

    no "Huh?"

    scene v11bb7a
    with dissolve

    u "Nothing."

    scene v11bb7
    with dissolve

    no "What time is it?"

    scene v11bb8 # FPP Show MC's phone, showing time as 6:58
    with dissolve

    u "It's 7."

    scene v11bb7b # FPP Same angle as v11bb7, Nora looking at MC, smiling with mouth open
    with dissolve

    no "What is the exact time? *Chuckles*"

    scene v11bb7c # FPP Same angle as v11bb7, Nora looking at MC, smiling with mouth closed
    with dissolve

    u "Oh, it's 6:58."

    scene v11bb7
    with dissolve

    no "Good, two more minutes."

    scene v11bb7a
    with dissolve

    u "What's happening at 7?"

    scene v11bb7
    with dissolve

    no "*Chuckles* You'll see."

    scene v11bb7c
    with dissolve

    u "What can we do for two minutes?"

    scene v11bb7b
    with dissolve

    no "*Whisper* Any girl... *Chuckles*"

    scene v11bb7c
    with dissolve

    u "What was that?"

    scene v11bb7b
    with dissolve

    no "Nothing."

    scene v11bb7a
    with dissolve

    u "I'm pretty sure you-"

    # Big Ben rings very loudly
    play sound "sounds/bells.mp3"
    scene v11bb9 # Show MC looking shocked, Nora looking at him, smiling with mouth closed
    with dissolve

    pause 3
    
    scene v11bb7c
    with dissolve

    u "What the fuck?"

    scene v11bb7b
    with dissolve

    no "*Laughs* It does that every hour on the dot. Haha, I can't believe how loud it is. That was beautiful."

    menu:
        "Agree":
            scene v11bb7c
            with dissolve

            u "Not gonna lie, it scared me a bit, but it was amazing. I'm glad I got to see this."

            scene v11bb9a # TPP Same angle as v11bb9, Nora giving MC a big hug, Nora smiling with mouth open
            with dissolve

            no "Thank you."

            scene v11bb7d # FPP Same angle as v11bb7, Nora leaning back after hugging MC, looking very happy with mouth open
            with dissolve

            no "Thank you for being a good person, for caring about this trip and for caring about me."
            no "I've felt pretty hopeless with all the shit that's been going on. The Chris drama, the stuff with Chloe, so much shit..."

            scene v11bb7
            with dissolve

            no "But this makes it all worth it."

            scene v11bb7c
            with dissolve

            u "I just felt like you deserved it, this was all your idea after all. I knew it meant a lot to you."

            scene v11bb7b
            with dissolve

            no "You're a good guy, [name]. Sorry for acting like a bitch so much... I just don't really like letting people in."
            no "Most people either don't actually care or have other motives for being nice."

            scene v11bb7c
            with dissolve

            u "Yeah I feel you. Well, that's not me."

            scene v11bb7e # FPP Same angle as v11bb7, Nora looking off into the distance, looking sad, mouth open
            with dissolve

            no "*Sighs*"

            scene v11bb7f # FPP Same angle as v11bb7, Nora looking off into the distance, looking sad, mouth closed
            with dissolve

            u "What's wrong?"

            scene v11bb7e
            with dissolve

            no "I just wish Chris was more like you is all."

            scene v11bb7f
            with dissolve

            u "What do you mean?"

            scene v11bb7g # FPP Same angle as v11bb7, Nora looking at MC, with a small, sad smile, mouth open
            with dissolve

            no "You're a frat member, a student, you make time for your friends and yet you still have time to give me a meaningful moment like this."

            scene v11bb7c
            with dissolve

            u "Haha, I'm glad you're enjoying yourself Nora."

            scene v11bb7b
            with dissolve

            no "C'mon, let's head on back before it gets too late."

            scene v11bb9b # TPP Same angle as v11bb9, Nora walking away pulling MC by the hand
            with dissolve

            pause 1

            scene v11bb10 # TPP MC and Nora climbing into a Uber, Nora holding MC's hand
            with dissolve

            pause 1

        "Make a move":
            $ v11_kiss_nora = True

            scene v11bb9c # TPP Same angle as v11bb9, MC grabbing Nora's hand and pulling her toward him, his other hand on her cheek
            with dissolve

            u "You're what's beautiful Nora."

            scene v11bb9d # TPP Same angle as v11bb9, MC trying to kiss Nora, Nora pushing him back, looking very angry with mouth open
            with dissolve

            no "WHAT THE FUCK ARE YOU DOING!?"

            scene v11bb7h # FPP Same angle as v11bb7, Nora looking at MC, angry with mouth closed
            with dissolve

            u "I thought-"

            scene v11bb7i # FPP Same angle as v11bb7, Nora looking at MC, angry with mouth open
            with dissolve

            no "You thought what?! That I wanted to cheat on my boyfriend? Ugh! Why couldn't you just be a good friend for a moment?"
            no "All guys are the same! You were just being nice because you thought you'd get some ass. Fuck you, [name]!"

            scene v11bb7j # FPP Same angle as v11bb7, Nora walking away from MC with her arms folded across her chest
            with dissolve

            u "Nora, wait!"

            scene v11bb11 # FPP Show MC grabbing Nora's hand to turn her around, Nora looking angry with her mouth closed
            with dissolve

            u "Wait."

            scene v11bb11a # FPP Same angle as v11bb11, Nora looking angry, pulling hand back, mouth open
            with dissolve

            no "Don't fucking touch me."

            scene v11bb11bb # FPP Same angle as v11bb11, Nora looking angry, arms folded across her chest, mouth closed
            with dissolve

            u "Nora I'm sorry, I didn't mean to cross the line. I just felt like we were having a moment."
            u "I know you and Chris are together, but you've been complaining about Chris and everything. I'm really sorry, I just got the wrong idea."

            scene v11bb11c # FPP Same angle as v11bb11, Nora looking down with neutral expression, mouth open
            with dissolve

            no "*Sighs* If I gave the wrong idea, that's my bad, but... really man? Fuck...?"

            scene v11bb11d # FPP Same angle as v11bb11, Nora looking down with neutral expression, mouth closed
            with dissolve

            u "I'm sorry."

            scene v11bb11c
            with dissolve

            no "Let's just go back."

            scene v11bb10a # TPP Same angle as v11bb10, MC and Nora getting into a black cab, Nora crossing her arms and looking upset
            with dissolve

            pause 1

    scene v11bb12 # TPP Back at hotel, Nora walking one direction, MC walking the other
    with dissolve

    pause 1
    stop music fadeout 3
    jump v11_hotel_bar