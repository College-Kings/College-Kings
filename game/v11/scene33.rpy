# SCENE 33: Chloe and Aubrey at the bar
# Location: Hotel bar, Hotel entrance, Sidewalk, In front of the car dealership
# Characters: MC (Outfit 0), Aubrey (Outfit 3), Chloe (Outfit 2), Bartender (Outfit 1), Charli (Outfit 1)
# Time: Day

label v11_bar_chloe_and_aubrey:
    scene v11caa1 # TPP. Show MC walking to the bar, mouth closed
    with fade
    play music "music/v11/Track Scene 11.mp3" fadein 2
    pause 0.75

    scene v11caa2 # FPP. MC spots chloe and aubrey sitting at the bar holding beer, mouth closed
    with dissolve

    play sound "sounds/swoosh.mp3"
    pause 0.75

    show screen fantasyOverlay

    scene v11caa2a # FPP. same as 2,MC is approaching chloe and aubrey but charli steps in the middle of the way, mouth opened
    with dissolve

    charli "It's almost fascinating just how narcissistic you are and how heavy you deflect."
    charli "First you thought I was being kind to the girls with a hidden agenda, but now that you know I'm gay you've lost the ability to connect those dots."
    charli "You can't comprehend being nice without an agenda, because you yourself aren't nice without an agenda."

    play sound "sounds/swoosh.mp3"

    pause 0.75
    hide screen fantasyOverlay

    scene v11caa3 # TPP. MC murmors with a mad face, mouth opened
    with dissolve


    u "(I am a nice guy... agenda my ass.)"

    scene v11caa4 # FPP. Looking at aubrey drinking a beer, mouth closed
    with dissolve

    u "Day drinking, huh?"

    scene v11caa4a # FPP. aubrey smiles, mouth opened
    with dissolve

    au "Hey, we're on vacation and taking advantage of being in a country where it's legal."

    scene v11caa4b # FPP. same as 4a, mouth closed
    with dissolve

    if CharacterService.is_mad(chloe):
        scene v11caa5 # FPP. Looking at chloe, she is starring away from mc, mouth closed
        with dissolve

        cl "..."

    else:
        scene v11caa6 # FPP. Looking at chloe smiling, mouth opened
        with dissolve

        cl "You should start taking advantage of it too. *Chuckles*"

        scene v11caa6a # FPP. Same as 6, mouth closed
        with dissolve

        u "Maybe I will."


    scene v11caa7 # TPP. MC takes a sit at the bar next to chloe and aubrey
    with dissolve

    pause 0.75

    scene v11caa8 # FPP. MC looks at bartender, mouth opened
    with dissolve

    bartender "What are you having today, love?"

    menu:
        "Something dark":
            scene v11caa8a # FPP. same as 8, mouth closed
            with dissolve

            u "Something dark."

            scene v11caa8b # FPP. looking at aubrey smiling, mouth opened
            with dissolve

            au "Now you're enjoying yourself. *Chuckles*"

        "Just water":
            scene v11caa8a
            with dissolve

            u "Just water please."

            scene v11caa8c # FPP. Looking at aubrey's slightly disgusted face, mouth opened
            with dissolve

            au "Um, lame! Get him something dark."

            scene v11caa8a
            with dissolve

            u "Seems I don't have a choice, something dark is fine."

    scene v11caa8
    with dissolve

    bartender "Coming up."

    scene v11caa9 # FPP. Looking at chloe and aubrey, mouth closed
    with dissolve

    u "Before I so rudely interrupted, what were you guys talking about?"

    scene v11caa9a # FPP. same as 9, aubrey's mouth opened
    with dissolve

    au "Mr. Lee being a total history nerd."

    scene v11caa9b # FPP. Same as 9, chloe looking at aubrey, chloe's mouth opened.
    with dissolve

    cl "He's not a nerd, Aubrey."

    scene v11caa9c # FPP. Same as 9a, aubrey looking at chloe, mouth opened.
    with dissolve

    au "Okay, I think he's a nerd when it comes to his history stuff."

    scene v11caa9
    with dissolve

    u "Maybe he's just really passionate."

    if CharacterService.is_mad(chloe):
        scene v11caa9b
        with dissolve

        cl "Yeah, what he said."

    else:
        scene v11caa9d # FPP. Chloe looking at MC with agree face, mouth opened
        with dissolve

        cl "That's exactly what I said."

    scene v11caa9a
    with dissolve

    au "Okay fine, he's not a nerd... just passionate. We'll run with that. *Chuckles*"

    scene v11caa9
    with dissolve

    u "Sounds like someone has it out for Mr. Lee."

    scene v11caa9a
    with dissolve

    au "Well, he failed me my first year. I was a terrible student, but I was so pissed when he failed me. He was doing the whole pass or no pass thing and I missed passing by one assignment."

    scene v11caa9
    with dissolve

    u "So you hold a grudge because he was fair? *Laughs*"

    scene v11caa9d
    with dissolve

    cl "That's kinda what it sounds like."

    play sound "sounds/call.mp3"

    scene v11caa10 # FPP. aubrey looks down at her pocket
    with dissolve

    pause 0.75

    scene v11caa11 # FPP. Aubrey looks at her phone smile on her face, mouth opened
    with dissolve

    au "Well, look at that! Someone needs me so I have to go... You two enjoy agreeing with each other. *Chuckles*"

    scene v11caa11a # FPP. looking at aubrey leaving, back turned to mc
    with dissolve

    stop sound

    u "Haha, later Aubrey."

    if CharacterService.is_mad(chloe):
        scene v11caa12 # FPP. Looking at chloe, mouth closed
        with dissolve

        u "Who do you think would win in a fight, a bear or gorilla?"

        scene v11caa12a # FPP. chloe looking confused, mouth opened
        with dissolve

        cl "What are you talking about?"

        scene v11caa12b # FPP. same as 12a, mouth closed
        with dissolve

        u "A fight between a bear and a gorilla, who wins?"

        scene v11caa12c # FPP. chloe looking uninterested, mouth opened
        with dissolve

        cl "*Sighs* I don't know, probably a gorilla. What's with the silly question?"

        scene v11caa12
        with dissolve

        u "Chloe, I'm just trying to get us back to being friends."

        scene v11caa12d # FPP. chloe looking at mc, mouth opened
        with dissolve

        cl "*Sighs* Round crackers or square crackers?"

        menu:
            "Round":
                scene v11caa12
                with dissolve

                u "Definitely going with the round ones."

            "Square":
                scene v11caa12
                with dissolve

                u "Definitely going with the square ones."

        scene v11caa12d
        with dissolve

        cl "I'm a round girl, myself."

        scene v11caa12
        with dissolve

        u "Look at us getting along... isn't this better than you walking around mad at me?"

        scene v11caa12d
        with dissolve

        cl "I'm not even really mad at you."

        scene v11caa12
        with dissolve

        u "Could've fooled me."

        scene v11caa12e # FPP. chloe has a slight smile, mouth opened
        with dissolve

        cl "Well, I mean sure... you pissed me off a while back, but I don't have it in me to hold a grudge or be upset forever over little things. I'm not Aubrey. *Chuckles*"

        scene v11caa12
        with dissolve

        u "Why have you been acting funny towards me, then?"

        scene v11caa12d
        with dissolve

        cl "Cause I didn't want to be the first one to apologize."

        scene v11caa12
        with dissolve

        u "That's kinda selfish."

        scene v11caa12d
        with dissolve

        cl "Well, blame my ego."

        scene v11caa13 # TPP. MC stands up and looks at chloe
        with dissolve

        pause 0.75

        scene v11caa14 # FPP. MC looking at chloe sitting down while he is standing up, mouth closed
        with dissolve

        u "Well look at us now, that wasn't so hard. You no longer have to walk around acting mad all the time."

        scene v11caa14a # FPP. Same, smile in cloes face, mouth opened
        with dissolve

        cl "Thanks, [name]."

        scene v11caa14b # FPP. same as 14a, mouth closed
        with dissolve

        u "No problem, grumpy."

        scene v11caa14a
        with dissolve

        cl "*Chuckles*"

        scene v11caa15 # TPP. MC leaving the bar
        with dissolve
        
        pause 0.75
        
        stop music fadeout 3

        if v11_riley_roomate:
            jump v11_riley_sex
        else:
            jump v11_chloe_hotel_room_amber_call

    else:
        scene v11caa16 # FPP. looking at chloe, still sitted, mouth opened
        with dissolve

        cl "Having an exciting day of vacation so far?"

        scene v11caa16a # FPP, same 16, mouth closed
        with dissolve

        u "It's been eventful. What are you getting into?"

        scene v11caa16
        with dissolve

        cl "You probably don't know this, but I actually really like cars. You know, like fast sports cars and stuff?"
        cl "There's a dealership right around the corner from here that Mr. Lee rented his car from, and they have a really cool car I'd love to drive."
        cl "I was thinking about going and test driving it, but I didn't want to go by myself and Aubrey said no because she had too much to drink..."

        scene v11caa16a
        with dissolve

        u "Well I haven't even touched my drink, so if you feel good enough I don't mind going with you."

        scene v11caa16b # FPP. real big smile in chloes face, mouth opened
        with dissolve

        cl "Really? Oh my god, thank you! I'll be right back."

        scene v11caa17 # TPP. Chloe standing up from the bar.
        with dissolve

        pause 0.75

        scene v11caa18 # TPP. Chloe running leaving the bar door
        with dissolve

        u "*Chuckles*"

        scene v11caa19 # FPP. looking at chloe leaving the bar door, has her back to the camera
        with dissolve

        bartender "Simping over the blonde... you and everyone else."

        scene v11caa19a # FPP. now looking at bartender, mouth closed
        with dissolve

        u "What? *Chuckles* Chloe's my friend."

        scene v11caa19b # FPP. same as 19a, mouth opened
        with dissolve

        bartender "Sure she is... A little advice? If you want a girl like her to stay, you might want to put a ring on it. That or give her a baby."

        scene v11caa19a
        with dissolve

        u "Okayyyy, that's enough bartender advice for today."

        scene v11caa20 # TPP. Chloe is running back to where MC is sitted,
        with dissolve

        pause 0.75

        scene v11caa21 # FPP. Chloe is standing up, with a slight smile on her face, mouth opened
        with dissolve

        cl "Okay, I'm ready."

        scene v11caa22a # FPP. MC is now standing up in front of chloe, mouth closed
        with dissolve

        u "Good, let's go."

        scene v11caa23 # TPP.MC and chloe exiting the bar
        with dissolve

        pause 0.75

        scene v11caa24 # TPP. MC and chloe exiting the hotel
        with dissolve

        pause 0.75

        scene v11caa25 # TPP. MC and chloe on the sidewalk
        with dissolve

        pause 0.75

        scene v11caa26 # TPP. MC and chloe in front of the car dealership
        with dissolve

        pause 0.75

        scene v11caa27 # TPP. MC and chloe waling into the dealership
        with dissolve
        stop music fadeout 3
        jump v11_cardealership