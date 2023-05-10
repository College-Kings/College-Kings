# SCENE 06: MC gets breakfast
# Locations: hotel room, hotel corridor, hotel lobby
# Characters: MC (Outfit: 2), LUUK (Outfit: 1)
# Time: morning 

label v13s06:
    scene v13s06_1 # TPP. MC wakes up in the morning from his own bed, mouth closed
    with fade

    pause 0.75

    play music music.ck1.v13.Track_Scene_6 fadein 2

    scene v13s06_2 # TPP. MC sits up, slight smile on his face, mouth closed
    with dissolve

    u "(Waking up on my own, Amsterdam is starting out nice. *Chuckles*)"

    scene v13s06_3 # TPP. MC getting out of bed in his room
    with dissolve

    pause 0.75

    scene v13s06_4 # TPP. MC in the hotel corridor
    with dissolve

    pause 0.75

    scene v13s06_5 # TPP. MC in the hotel lobby
    with dissolve
    
    pause 0.75

    scene v13s06_6 # FPP. MC looking at the bartender, mouth closed
    with dissolve

    u "Hello."

    scene v13s06_6a # FPP. Same as 6, slight smile on the bartenders face, mouth opened
    with dissolve

    luuk "Sleepy field trip kid! Good morning."

    scene v13s06_6
    with dissolve

    u "Huh?"

    scene v13s06_6a
    with dissolve

    luuk "My name is Luuk, I saw you last night with the rest of the students and overheard your conversation."

    scene v13s06_6
    with dissolve

    u "Ahh, guess nothing gets past you, huh?"

    scene v13s06_6a
    with dissolve

    luuk "For a price, I can hear or not hear anything... So, whether you want to have some fun or stay out of trouble, I'm your guy."

    scene v13s06_6
    with dissolve

    u "That's a bold approach for someone you just met."

    scene v13s06_6a
    with dissolve

    luuk "I work at a hotel, everyone I talk to is someone I just met. *Chuckles*"

    scene v13s06_6
    with dissolve

    u "*Chuckles* Fair enough."

    scene v13s06_6b # FPP. same as 6, mouth opened
    with dissolve

    luuk "So, was there a reason you came over?"

    scene v13s06_6
    with dissolve

    u "Yeah, actually. We've been staying in Peace Hotels our entire trip, and I tried the breakfast in Paris and loved it. I was wondering if you guys had breakfast here in Amsterdam as well?"

    scene v13s06_6b
    with dissolve

    luuk "We normally do, but I'm sorry to say we don't this morning. There was a minor staffing situation so we had to cancel breakfast for today."

    scene v13s06_6
    with dissolve

    u "Oh, okay. Thanks for the info."

    scene v13s06_6a
    with dissolve

    luuk "Since you enjoyed the breakfast so much, come by again sometime before you leave and I'll personally make your meal."

    scene v13s06_6
    with dissolve

    u "So you're a confidence man and a chef?"

    scene v13s06_6b
    with dissolve

    luuk "It's good to possess many conflicting skills. No one expects a confidence man to be a good cook and no one expects the cook to be a confidence man."

    scene v13s06_6
    with dissolve

    u "Huh... You've really thought this through. *Chuckles*"

    scene v13s06_6a
    with dissolve

    luuk "Haha, let's just say I make more money scheming with the guests than I do checking them in."

    scene v13s06_6
    with dissolve

    u "Hmm. I may have to get in on that."

    scene v13s06_6a
    with dissolve

    luuk "You're not built for this kind of life, trust me. *Chuckles*"

    menu:
        "I am":
            scene v13s06_6
            with dissolve

            u "Of course I am."

            scene v13s06_7 # TPP. MC shows off his arm muscle, flexing face on, mouth closed
            with dissolve

            pause 0.75

            scene v13s06_6
            with dissolve

            u "Do you see this? I have all the muscle you need."

            scene v13s06_6a
            with dissolve

            luuk "Impressive. *Chuckles*"

        "Yeah, probably not":
            scene v13s06_6
            with dissolve

            u "Yeah, probably not. More of a straight and narrow kind of guy."

            scene v13s06_6a
            with dissolve

            luuk "Playing it safe always guarantees safety."

            scene v13s06_6
            with dissolve

            u "I was always told \"cowards live longer\"."

            scene v13s06_6a
            with dissolve

            luuk "That they do. *Chuckles*"

    scene v13s06_6a
    with dissolve

    luuk "Well... I'll see you soon for another breakfast. *Laughs* Also, remember what I said. I hear it all or don't hear anything."

    scene v13s06_6
    with dissolve

    u "I... heard... you."

    scene v13s06_6a
    with dissolve

    luuk "Clever."

    stop music fadeout 3

    jump v13_ticket_transfer