# SCENE20: ARCADE WITH EMILY
# Locations: Slot Machine Arcade, Emily's dorm
# Characters: MC (outfit 2), Emily (outfit 3 or better put together something more skimpier), arcade room employee, two random extras
# Time: Sunday evening

### Extra audio files needed (coded but commented out for now) ###
# arcade_amb.mp3 - Arcade room ambience, arcade_win.mp3 - A short arcade game winning sound, arcade_lose.mp3 - A short arcade game losing sound

init python:
    renpy.music.register_channel("ambience", mixer="sfx", loop=True)

label emily_arcade:
    
    $ renpy.music.set_volume(1, channel="ambience")

    scene v8arcade1 # TPP. MC walking into the arcade building, Emily can be seen waiting for him inside
    with Fade(0.75, 0.25, 0.75)
    play ambience "sounds/arcade_amb.mp3" fadein 2
    pause 1

    if emily.relationship >= Relationship.FWB:
        scene v8arcade2 # FPP. (after MC walks up to Emily). Emily cheerful, mouth open
        with dissolve
        em "Hey, sexy!"

        scene v8arcade2a # Same as v8arcade2 but Emily mouth closed
        with dissolve
        u "You're the sexy one! You look amazing!"

        scene v8arcade2
        with dissolve
        em "Thank you. I was hoping you'd like it."

        scene v8arcade2a
        with dissolve
        u "Love it! Although..."

        scene v8arcade3 # FPP. Same camera position as v8arcade2 but tilt the camera downwards to show Emily's body
        with dissolve
        u "This your way of distracting me so you win?"

        scene v8arcade2b # Emily slightly flirty, brow raised, mouth open
        with dissolve
        em "Maybe."

        scene v8arcade2c # Emily walking away towards Six shooter game. (Smiling and mouth open if face is visible)
        with dissolve
        em "Follow me."

        scene v8arcade4 # FPP. (Emily and MC standing in front of Six shooter game. Emily is standing slightly closer to it to the arcade machine is visible in frame). Emily looking at MC, cheerful and talking. Use different arcade screens for different renders that start with arcade4 so it looks lively. Pick a random screen unless mentioned
        with dissolve
        em "You know how to shoot?"

        scene v8arcade4a # Same as v8arcade4 but Emily mouth closed
        with dissolve
        u "Absolutely not, but I'll give it a... {i}shot!{/i}"

        scene v8arcade4b # Emily places her hand on MC's chest, laughing with her hand covering her mouth, eyes closed and mouth open
        with dissolve
        em "You're lucky it's a slot game. If your aim was as bad as that joke..."
        u "Hey! That was a great joke!"

        scene v8arcade4
        with dissolve
        em "Sure it was. Loser pays for the next game?"

        scene v8arcade4a
        with dissolve

        menu:
            "Take the bet":
                $ add_point(KCT.BOYFRIEND)
                $ emilyArcade = 1

                jump em_arcade_1

            "Make it more interesting":
                $ add_point(KCT.TROUBLEMAKER)
                $ emilyArcade = 2

                jump em_arcade_2

    else:
        scene v8arcade2
        with dissolve
        em "Hey, [name]!"

        scene v8arcade2a
        with dissolve
        u "Hey! Thanks for inviting me."

        scene v8arcade2
        with dissolve
        em "No problem. Figured we could chill and I could kick your ass at some games."

        scene v8arcade2a
        with dissolve
        u "Don't be so sure! You know I lived in the arcade back home!"

        scene v8arcade2
        with dissolve
        em "Yeah, but I was right there by your side. I'm sure I picked up a few tips."

        scene v8arcade2c
        with dissolve
        em "Follow me."

        scene v8arcade4
        with dissolve
        em "You know how to shoot?"

        scene v8arcade4a
        with dissolve
        u "Absolutely not, but I'll give it a... {i}shot!{/i}"

        scene v8arcade4f # Emily rolling eyes, but smiling
        with dissolve
        em "*Groans*"

        scene v8arcade4
        with dissolve
        em "So, loser pays for the next game?"

        scene v8arcade4a
        with dissolve

        menu:
            "Take the bet":
                $ add_point(KCT.BRO)
                $ emilyArcade = 3

                jump em_arcade_3

            "Make it more fun":
                $ add_point(KCT.TROUBLEMAKER)
                $ emilyArcade = 4

                jump em_arcade_4

label em_arcade_2:
    scene v8arcade4a
    with dissolve
    u "If we're betting, let's make it interesting. I'll pay for all the games."

    scene v8arcade4
    with dissolve
    em "What you got in mind?"

    scene v8arcade4a
    with dissolve
    u "Winner gets a kiss, loser chooses where..."

    scene v8arcade4c # Emily flirty and mouth open
    with dissolve
    em "Ooh, I like it. Pucker up buddy!"

    scene v8arcade4d # Emily flirty, mouth closed
    with dissolve
    u "Not so fast. I know those lips well. I'm making sure I get to feel 'em!"

    scene v8arcade4c
    with dissolve
    em "Put your tokens where your mouth is, then!"

    scene v8arcade4a
    with dissolve
    u "Yes, ma'am. Let me get some change."

    scene v8arcade1y # TPP. MC drawing tokens from the token machine, or the employee if there's no machine
    with dissolve
    empl "Have fun, sir!"

    scene v8arcade4e # MC giving Emily a token. Emily smiling and taking it, mouth closed
    with fade
    u "Ladies first."

    scene v8arcade4
    with dissolve
    em "Highest payout wins?"

    scene v8arcade4a
    with dissolve
    u "Yep."

    scene v8arcade5 # TPP. Emily playing the six shooter game. MC is standing somewhere near her but need not be visible in frame
    with dissolve
    pause 1

    scene v8arcade5a # Different shot of Emily playing the six shooter game, "You win" screen on the arcade machine (show a high score if it can be done)
    with dissolve
    pause 1

    play sound "sounds/arcade_win.mp3"

    scene v8arcade5b # Emily celebrating victory, same arcade screen as v8arcade5a
    with dissolve
    pause 1

    scene v8arcade6 # FPP. (Emily turns to face the MC) Emily looking into the camera, happy, with a smirk, mouth open. If arcade machine is visible, same arcade screen as v8arcade5a
    with dissolve
    em "Beat that!"

    scene v8arcade6a # Same as v8arcade6 but Emily mouth closed
    with dissolve
    u "Not gonna make it easy for me, are you?"

    scene v8arcade7 # TPP. MC playing the six shooter game. Emily standing near him looking at the arcade machine, neutral expression, mouth closed
    with dissolve
    pause 1

    play sound "sounds/arcade_lose.mp3"

    scene v8arcade7a # Different shot of MC playing the six shooter game, "You lose" screen on the arcade machine (show a low score if it can be done). Emily looking at the arcade machine, neutral expression, mouth closed
    with dissolve
    pause 1
    u "No way I coulda won that one."

    scene v8arcade8 # FPP. (MC and Emily close up) Emily tapping her cheek (as if asking for a kiss), flirty expression, mouth open. Same arcade screen as in v8arcade7a if the machine is visible
    with dissolve
    em "Pay up!"

    scene v8arcade9 # TPP. MC kissing on Emily's cheek. Emily looking happy, mouth closed
    with dissolve
    play sound "sounds/kiss.mp3"
    pause 1

    scene v8arcade8a # Emily looking happy, mouth closed
    with dissolve
    u "Don't get used to it. I got the next one for sure."

    scene v8arcade10 # FPP. Emily standing in front of "Chase the wheel" game, pointing towards it, smiling and mouth open
    with dissolve
    em "Maybe you'll have better luck if you go first next."

    scene v8arcade10a # Same as v8arcade10 but Emily mouth closed
    with dissolve
    u "Good thinking."

    scene v8arcade11 # TPP. Show MC playing "chase the wheel" game. Emily standing near him, neutral expression, mouth closed
    with dissolve
    pause 1

    play sound "sounds/arcade_lose.mp3"

    scene v8arcade11a # Different shot of MC playing "chase the wheel" game, "You lose" screen on the arcade machine. Emily laughing a little, mouth closed
    with dissolve
    pause 1

    scene v8arcade12 # FPP. (MC and Emily close up near chase the wheel machine). Emily smirky, mouth open
    with dissolve
    em "Or not. If I didn't know any better, I'd think you were letting me win."

    scene v8arcade12a # Same as v8arcade12 but Emily mouth closed
    with dissolve
    u "How? Haha!"

    scene v8arcade12
    with dissolve
    em "Step aside. Let me show you how it's done."

    scene v8arcade13 # FPP. Show Emily playing "chase the wheel" game. MC standing near her. Make sure the arcade machine screen is visible
    with dissolve
    pause 1

    play sound "sounds/arcade_win.mp3"

    scene v8arcade13a # Different shot of Emily playing "chase the wheel" game, "You win" screen on the arcade machine
    with dissolve
    pause 1

    scene v8arcade13b # Emily turns to look at the MC. Laughing, smirky and mouth open. Same arcade screen as in v8arcade13a
    with dissolve
    em "I'm so glad I invited you out!"

    scene v8arcade13c # Same as v8arcade13b but Emily mouth closed
    with dissolve
    u "Well, where would you like it, ma'am?"

    scene v8arcade13b
    with dissolve
    em "How about..."

    scene v8arcade13d # Emily pointing between her boobs, smiling, one brow raised, mouth closed
    with dissolve
    pause 1
    u "My pleasure!"

    scene v8arcade14 # TPP. Close up of MC shoving his face between Emily's boobs while holding them.
    with dissolve
    play sound "sounds/kiss.mp3"
    pause 1

    scene v8arcade12a
    with dissolve
    u "I'm starting to think losing isn't so bad."

    scene v8arcade15 # FPP. Emily walking up to the coin drop game. MC is behind her
    with fade
    pause 0.5

    scene v8arcade15a # Emily turns back, smiling, mouth open
    with dissolve
    em "First person to get a payout wins-"

    scene v8arcade15b # Same as v8arcade15a but Emily mouth closed
    with dissolve
    u "Oh, you're going down now. I have the magic touch with this game!"

    scene v8arcade15c # Emily flirty, mouth open
    with dissolve
    em "Not just this game."

    scene v8arcade16 # TPP. MC leaning in to kiss Emily but she is leaning back to dodge it, smiling, one brow raised, mouth open
    with dissolve
    em "Hey... wait 'til you lose again!"


    scene v8arcade17 # TPP. MC putting a token in the machine or pressing the start button, however that is activated. Emily just standing, neutral expression, mouth closed
    with dissolve
    u "You're underestimating me ma'am. Watch me."

    play sound "sounds/arcade_coin.mp3"
    pause

    scene v8arcade17a # TPP. MC putting a token in the machine or pressing the start button, however that is activated. Emily just standing, neutral expression, mouth closed
    with dissolve
    em "My turn now."

    play sound "sounds/arcade_coin.mp3"
    pause

    scene v8arcade17b # MC wins (Not sure how you would show it in this case. Maybe green lights?) Emily surprised but smiling, mouth open. MC happy, mouth open
    with dissolve
    u "Wooo! I win!"
    em "Guess I gotta pay up."
    em "Where do you want it?"
    u "I think you know where."

    scene v8arcade15d # Emily shocked/embarrassed, mouth open
    with dissolve
    em "In public!?"

    scene v8arcade15e # Same as v8arcade15d but Emily mouth closed
    with dissolve
    u "I meant that spot on my neck you naughty girl *laugh*"

    scene v8arcade15d
    with dissolve
    em "Oh.."

    scene v8arcade18 # TPP. Emily kissing MC's neck. MC smiling like an idiot, mouth closed
    with dissolve
    play sound "sounds/kiss.mp3"
    pause 1

    scene v8arcade18a # Same as v8arcade18 but MC mouth open
    with dissolve
    u "Oh, God. I changed my mind. I choose the other spot."

    scene v8arcade15f # Emily looking down at MC's dick, flirty, mouth open
    with dissolve
    pause

    scene v8arcade15c
    with dissolve
    em "How about we make this more interesting?"
    u "Yeah?"

    scene v8arcade19 # FPP. Emily walking up to the claw machine game. MC is behind her
    with fade
    pause 1

    scene v8arcade19a # Emily turns back, smiling with a little smirk, mouth open
    with dissolve
    em "First person to get a stuffed animal is the ultimate winner."

    scene v8arcade19b # Same as v8arcade19a but Emily mouth closed
    with dissolve
    u "And?"

    scene v8arcade19a
    with dissolve
    em "And loser has to eat her out."

    scene v8arcade19b
    with dissolve
    u "Or blow him."

    scene v8arcade19c # Emily laughing, mouth open
    with dissolve
    em "Not the way you've been playing!"
    u "Seems like I win either way, so I'll even let you go first."
    em "Such a gentleman."

    scene v8arcade20 # TPP. Emily trying out the claw game. MC not in the frame
    with dissolve
    em "Get ready to lose."

    play sound "sounds/arcade_lose.mp3"

    scene v8arcade20a # Show Emily losing (Not sure how you would show it. Maybe red lights?). MC not in the frame
    with hpunch
    em "Damn it."

    scene v8arcade20b # MC trying out the claw game. Emily not in the frame
    with dissolve
    u "Let me show you how it's done."

    play sound "sounds/arcade_lose.mp3"

    scene v8arcade20c # Show MC losing. Emily not in the frame
    with hpunch
    u "So close."
    em "Good show. My turn now."

    scene v8arcade20
    with dissolve
    pause 1

    play sound "sounds/arcade_lose.mp3"

    scene v8arcade20a
    with hpunch
    pause 1

    scene v8arcade20b
    with dissolve
    pause 1

    play sound "sounds/arcade_lose.mp3"

    scene v8arcade20c
    with hpunch
    pause 1

    scene v8arcade20
    with dissolve
    pause 1

    play sound "sounds/arcade_lose.mp3"

    scene v8arcade20a
    with hpunch
    pause 1

    scene v8arcade20b
    with dissolve
    pause 1

    play sound "sounds/arcade_win.mp3"

    scene v8arcade20d # Show MC winning (green lights?) and celebrating, mouth open
    with hpunch
    u "Finally!"
    em "HOW?"

    scene v8arcade21 # FPP. (MC and Emily close up near claw machine). Emily surprised, mouth closed
    with dissolve
    u "Don't care. Get ready to-"

    scene v8arcade21a # Emily looks to the side as if someone caught her attention, mouth closed
    with dissolve
    ann "Attention! We're closing in five minutes. Everyone is requested to leave the arcade zone immediately. Thank you for visiting."

    scene v8arcade21b # Emily looks back at the MC, laughing, mouth open
    with dissolve
    em "Awww, too bad. Time to go home."

    scene v8arcade21c # Same as v8arcade21b but Emily mouth closed
    with dissolve
    u "But I was winning! I had it!"

    scene v8arcade21b
    with dissolve
    em "Sure you did. Come on. Walk me home."

    scene v8arcade21c
    with dissolve
    u "Don't you think I'll forget about it."

    stop ambience fadeout 3

    scene v8arcade22 # TPP. MC and Emily walking in the hallway walking towards her dorm door
    with Fade(0.75, 0.25, 0.75)
    pause 0.5

    scene v8arcade23 # FPP. Emily standing near her door. Looking very happy and mouth open
    with dissolve
    em "Thank you for the lovely evening."

    scene v8arcade24 # TPP. MC and Emily passionate kiss
    with dissolve
    play sound "sounds/kiss.mp3"
    pause 1

    scene v8arcade23a # Same as v8arcade23 but Emily mouth closed
    with dissolve
    u "And thanks for asking me to come out. This sure beat studying."

    scene v8arcade23
    with dissolve
    em "Maybe we can do it again sometime."

    scene v8arcade23a
    with dissolve
    u "Hope so."

    scene v8arcade23
    with dissolve
    em "Goodnight, [name]."

    play sound "sounds/dooropen.mp3"

    scene v8arcade23b # Emily opened the door and is walking in while looking back at the MC, smiling, mouth closed
    with dissolve
    u "Night."

    scene v8arcade23c # Emily went inside, so just the door closed
    with dissolve
    play sound "sounds/doorclose.mp3"
    pause 0.5

    scene v8arcade28 # TPP. continuation of v8arcade23. MC starts walking away, smiling, mouth closed
    with dissolve
    pause 0.5

    jump mon_morning_room

label em_arcade_1:
    scene v8arcade4a
    with dissolve
    u "You're on. Let me get some change."

    scene v8arcade1y
    with dissolve
    empl "Have fun, sir!"

    scene v8arcade4e
    with fade
    u "Ladies first."

    scene v8arcade4
    with dissolve
    em "Highest payout wins?"

    scene v8arcade4a
    with dissolve
    u "Yep."

    scene v8arcade5
    with dissolve
    pause 1

    scene v8arcade5a
    with dissolve
    pause 1

    play sound "sounds/arcade_win.mp3"

    scene v8arcade5b
    with dissolve
    pause 1

    scene v8arcade6
    with dissolve
    em "Beat that!"

    scene v8arcade6a
    with dissolve
    u "Not gonna make it easy for me, are you?"

    scene v8arcade7
    with dissolve
    pause 0.5

    play sound "sounds/arcade_lose.mp3"

    scene v8arcade7a
    with dissolve
    pause 1
    u "No way I coulda won that one."

    scene v8arcade8b # Emily holding her hand out as if asking for something, smirky, mouth open
    with dissolve
    em "Pay up!"

    scene v8arcade8c # MC handing Emily a token. Emily same as in v8arcade8b but mouth closed
    with dissolve
    u "That was just luck. I got the next one."

    scene v8arcade10
    with dissolve
    em "Maybe you'll have better luck if you go first next."

    scene v8arcade10a
    with dissolve
    u "Good thinking."

    scene v8arcade11
    with dissolve
    pause 0.5

    play sound "sounds/arcade_lose.mp3"

    scene v8arcade11a
    with dissolve
    pause 1

    scene v8arcade12
    with dissolve
    em "Or not. If I didn't know any better, I'd think you were letting me win."

    scene v8arcade12a
    with dissolve
    u "How? Haha!"

    scene v8arcade12
    with dissolve
    em "Step aside. Let me show you how it's done."

    scene v8arcade13
    with dissolve
    pause 0.5

    play sound "sounds/arcade_win.mp3"

    scene v8arcade13a
    with dissolve
    pause 1

    scene v8arcade13b # Emily turns to look at the MC. Laughing, smirky and mouth open. Same arcade screen as in v8arcade13a
    with dissolve
    em "I'm so glad I invited you out!"

    scene v8arcade13c # Same as v8arcade13b but Emily mouth closed
    with dissolve
    u "More tokens?"

    scene v8arcade13b
    with dissolve
    em "That was the bet."

    scene v8arcade15
    with fade
    pause 0.5

    scene v8arcade15a
    with dissolve
    em "First person to get a payout wins-"

    scene v8arcade15b
    with dissolve
    u "Oh, you're going down now. I have the magic touch with this game!"

    scene v8arcade15g # Emily rolling her eyes, smirky, mouth open
    with dissolve
    em "I'm sure you do."

    scene v8arcade17
    with dissolve
    u "You're underestimating me ma'am. Watch me."

    play sound "sounds/arcade_coin.mp3"
    pause

    scene v8arcade17a # TPP. MC putting a token in the machine or pressing the start button, however that is activated. Emily just standing, neutral expression, mouth closed
    with dissolve
    em "My turn now."

    play sound "sounds/arcade_coin.mp3"
    pause

    scene v8arcade17b
    with dissolve
    u "Wooo! I win!"
    em "Pure luck."

    scene v8arcade15h # Emily handing MC a token, mouth open, neutral expression
    with dissolve
    em "Here."

    scene v8arcade15c
    with dissolve
    em "How about we make this more interesting?"
    u "Yeah?"

    scene v8arcade19
    with fade
    pause 1

    scene v8arcade19a
    with dissolve
    em "First person to get a stuffed animal is the ultimate winner."

    scene v8arcade19b
    with dissolve
    u "What do they win?"

    scene v8arcade19a
    with dissolve
    em "A kiss."

    scene v8arcade19b
    with dissolve
    u "Seems like I win either way, so I'll even let you go first."

    scene v8arcade19c
    with dissolve
    em "Such a gentleman."

    scene v8arcade20
    with dissolve
    em "Get ready to lose."

    play sound "sounds/arcade_lose.mp3"

    scene v8arcade20a
    with hpunch
    em "Damn it."

    scene v8arcade20b
    with dissolve
    u "Let me show you how it's done."

    play sound "sounds/arcade_lose.mp3"

    scene v8arcade20c
    with hpunch
    u "So close!"
    em "Good show. My turn now."

    scene v8arcade20
    with dissolve
    pause 1

    play sound "sounds/arcade_lose.mp3"

    scene v8arcade20a
    with hpunch
    pause 1

    scene v8arcade20b
    with dissolve
    pause 1

    play sound "sounds/arcade_lose.mp3"

    scene v8arcade20c
    with hpunch
    pause 1

    scene v8arcade20
    with dissolve
    pause 1

    play sound "sounds/arcade_lose.mp3"

    scene v8arcade20a
    with hpunch
    pause 1

    scene v8arcade20b
    with dissolve
    pause 1

    play sound "sounds/arcade_win.mp3"

    scene v8arcade20d
    with hpunch
    u "Finally!"
    em "HOW?"

    scene v8arcade21
    with dissolve
    u "It's called talen-"

    scene v8arcade21a
    with dissolve
    ann "Attention! We're closing in five minutes. Everyone is requested to leave the arcade zone immediately. Thank you for visiting."

    scene v8arcade21b
    with dissolve
    em "Awww, too bad. Time to go home."

    scene v8arcade21c
    with dissolve
    u "But I was winning! I had it!"

    scene v8arcade21b
    with dissolve
    em "Sure you did. Come on. Walk me home."

    stop ambience fadeout 3

    scene v8arcade22
    with Fade(0.75, 0.25, 0.75)
    pause 0.5

    scene v8arcade23a
    with dissolve

    menu:
        "Kiss her":
            if lauren.relationship >= Relationship.GIRLFRIEND:
                $ add_point(KCT.TROUBLEMAKER)

            else:
                $ add_point(KCT.BOYFRIEND)

            scene v8arcade24
            with dissolve
            play sound "sounds/kiss.mp3"
            pause 1

            scene v8arcade23
            with dissolve
            em "Thank you for the lovely evening."

            scene v8arcade23a
            with dissolve
            u "And thanks for asking me to come out. This sure beat studying."

            scene v8arcade23
            with dissolve
            em "Maybe we can do it again sometime."

            scene v8arcade23a
            with dissolve
            u "Hope so."

            scene v8arcade23
            with dissolve
            em "Goodnight, [name]."

            play sound "sounds/dooropen.mp3"

            scene v8arcade23b
            with dissolve
            u "Night."

            play sound "sounds/doorclose.mp3"

            scene v8arcade23c
            with dissolve
            pause 0.5

            scene v8arcade28
            with dissolve
            pause 0.5

            jump mon_morning_room

        "Good night":
            if lauren.relationship >= Relationship.GIRLFRIEND:
                $ add_point(KCT.BOYFRIEND)

            scene v8arcade23a
            with dissolve
            u "I had fun."

            scene v8arcade23
            with dissolve
            em "Me too, goodnight."

            play sound "sounds/dooropen.mp3"

            scene v8arcade23b
            with dissolve
            u "Night."

            play sound "sounds/doorclose.mp3"

            scene v8arcade23c
            with dissolve
            pause 0.5

            scene v8arcade28
            with dissolve
            pause 0.5

            jump mon_morning_room

label em_arcade_4:
    scene v8arcade4a
    with dissolve
    u "If we're betting, let's make it more fun. I'll pay for all the games."

    scene v8arcade4
    with dissolve
    em "What you got in mind?"

    scene v8arcade4a
    with dissolve
    u "How about loser does a dare?"

    scene v8arcade4g # Emily looking at MC suspiciously
    with dissolve
    pause
    u "Calm down, nothing too bad. Just some fun."

    scene v8arcade4h # Same as v8arcade4g but Emily mouth open
    with dissolve
    em "Okay, but I'm watching you [name]."

    scene v8arcade4a
    with dissolve
    u "Don't worry. Let me get some change."

    scene v8arcade1y
    with dissolve
    empl "Have fun, sir!"

    scene v8arcade4e
    with fade
    u "Ladies first."

    scene v8arcade4
    with dissolve
    em "Highest payout wins?"

    scene v8arcade4a
    with dissolve
    u "Yep."

    scene v8arcade5
    with dissolve
    pause 1

    scene v8arcade5a
    with dissolve
    pause 1

    play sound "sounds/arcade_win.mp3"

    scene v8arcade5b
    with dissolve
    pause 1

    scene v8arcade6
    with dissolve
    em "Beat that!"

    scene v8arcade6a
    with dissolve
    u "Not gonna make it easy for me, are you?"

    scene v8arcade7
    with dissolve
    pause 0.5

    play sound "sounds/arcade_lose.mp3"

    scene v8arcade7a
    with dissolve
    pause 1
    u "No way I coulda won that one."

    scene v8arcade6
    with dissolve
    em "Pay up!"

    scene v8arcade6a
    with dissolve
    u "What do you want me to do?"
    em "Hmmm..."

    scene v8arcade6
    with dissolve
    em "Go flash the camera."

    scene v8arcade6a
    with dissolve
    u "Do what?"

    scene v8arcade6
    with dissolve
    em "You heard me."

    scene v8arcade6a
    with dissolve
    u "I'll get you for this."

    scene v8arcade25 # TPP. (This is continuation of v8arcade8). MC walks in front of the security camera and strips his shirt in front of it (show him holding the shirt). Emily just watching while laughing, mouth open
    with dissolve
    em "The security guy is gonna love this."

    scene v8arcade10
    with fade
    em "Maybe you'll have better luck if you go first next."

    scene v8arcade10a
    with dissolve
    u "Good thinking."

    scene v8arcade11
    with dissolve
    pause 0.5

    play sound "sounds/arcade_lose.mp3"

    scene v8arcade11a
    with dissolve
    pause 1

    scene v8arcade12
    with dissolve
    em "Or not. If I didn't know any better, I'd think you were letting me win."

    scene v8arcade12a
    with dissolve
    u "How? Haha!"

    scene v8arcade12
    with dissolve
    em "Step aside. Let me show you how it's done."

    scene v8arcade13
    with dissolve
    pause 0.5

    play sound "sounds/arcade_win.mp3"

    scene v8arcade13a
    with dissolve
    pause 1

    scene v8arcade13b
    with dissolve
    em "I'm so glad I invited you out!"

    scene v8arcade13c
    with dissolve
    u "Now what?"

    scene v8arcade13b
    with dissolve
    em "How about..."

    scene v8arcade26 # TPP. Showing a couple of random extras playing by a different arcade
    with dissolve
    em "Oh! Go over by those people and pick your nose where everyone can see you."

    scene v8arcade13c
    with dissolve
    u "You're kidding!"

    scene v8arcade13b
    with dissolve
    em "Nope."

    scene v8arcade13c
    with dissolve
    u "UGH!"

    scene v8arcade26a # MC walks in and starts picking his nose in front of them. They're grossed out and looking weirdly at the MC, mouths closed
    with dissolve
    pause
    em "*Laughs out loud*"

    scene v8arcade13c
    with dissolve
    u "I'm starting to regret this idea to make it interesting."

    scene v8arcade13b
    with dissolve
    em "Just you wait 'til your defeat."

    scene v8arcade15
    with fade
    pause 0.5

    scene v8arcade15a
    with dissolve
    em "First person to get a payout wins-"

    scene v8arcade15b
    with dissolve
    u "Oh, you're going down now. I have the magic touch with this game!"

    scene v8arcade15g
    with dissolve
    em "I'm sure you do."

    scene v8arcade17
    with dissolve
    u "You're underestimating me ma'am. Watch me."

    play sound "sounds/arcade_coin.mp3"
    pause

    scene v8arcade17a
    with dissolve
    em "My turn now."

    play sound "sounds/arcade_coin.mp3"
    pause

    scene v8arcade17b
    with dissolve
    u "Wooo! I win!"
    em "Guess I gotta pay up."

    scene v8arcade15e
    with dissolve
    u "(Shit, here's my chance.)"
    u "I had to flash the camera..."
    u "...so it's only fair..."

    scene v8arcade27 # FPP. (This is continuation of v8arcade15, so same camera coordinates but camera turned sideways a little). Emily starts walking away from the camera looking disappointed
    with dissolve
    em "Wow."
    u "NO!"

    scene v8arcade27a # Emily turns back and is looking at MC, disappointed, mouth open
    with dissolve
    u "For my eyes only."

    scene v8arcade27b # Emily comes very close to MC and starts pulling her top up, smiling but kinda seductive look, mouth closed
    with dissolve
    pause 0.5

    if config_censored:
        call screen censoredPopup("v8s20_nsfwSkipLabel1")

    scene v8arcade27c # Same as v8arcade27b but she pulled her top up completely
    with dissolve

    $ grant_achievement("lucky_7")

    u "Oh, God, I miss them."

label v8s20_nsfwSkipLabel1:
    scene v8arcade27b
    with dissolve
    pause 0.5

    scene v8arcade15c
    with dissolve
    em "How about we make this more interesting?"
    u "More interesting than that?"

    scene v8arcade19
    with fade
    pause 1

    scene v8arcade19a
    with dissolve
    em "First person to get a stuffed animal is the ultimate winner."

    scene v8arcade19b
    with dissolve
    u "And?"

    scene v8arcade19a
    with dissolve
    em "Winner gets a kiss."

    scene v8arcade19b
    with dissolve
    u "Seems like I win either way, so I'll even let you go first."

    scene v8arcade19c
    with dissolve
    em "Such a gentleman."

    scene v8arcade20
    with dissolve
    em "Get ready to lose."

    play sound "sounds/arcade_lose.mp3"

    scene v8arcade20a
    with hpunch
    em "Damn it."

    scene v8arcade20b
    with dissolve
    u "Let me show you how it's done."

    play sound "sounds/arcade_lose.mp3"

    scene v8arcade20c
    with hpunch
    u "So close!"
    em "Good show. My turn now."

    scene v8arcade20
    with dissolve
    pause 1

    play sound "sounds/arcade_lose.mp3"

    scene v8arcade20a
    with hpunch
    pause 1

    scene v8arcade20b
    with dissolve
    pause 1

    play sound "sounds/arcade_lose.mp3"

    scene v8arcade20c
    with hpunch
    pause 1

    scene v8arcade20
    with dissolve
    pause 1

    play sound "sounds/arcade_lose.mp3"

    scene v8arcade20a
    with hpunch
    pause 1

    scene v8arcade20b
    with dissolve
    pause 1

    play sound "sounds/arcade_win.mp3"

    scene v8arcade20d
    with hpunch
    u "Finally!"
    em "HOW?"

    scene v8arcade21
    with dissolve
    u "It's called talen-"

    scene v8arcade21a
    with dissolve
    ann "Attention! We're closing in five minutes. Everyone is requested to leave the arcade zone immediately. Thank you for visiting."

    scene v8arcade21b
    with dissolve
    em "Awww, too bad. Time to go home."

    scene v8arcade21c
    with dissolve
    u "But I was winning! I had it!"

    scene v8arcade21b
    with dissolve
    em "Sure you did. Come on. Walk me home."

    stop ambience fadeout 3

    scene v8arcade22
    with Fade(0.75, 0.25, 0.75)
    pause 0.5

    scene v8arcade23a
    with dissolve

    menu:
        "Kiss her":
            if lauren.relationship >= Relationship.GIRLFRIEND:
                $ add_point(KCT.TROUBLEMAKER)
            else:
                $ add_point(KCT.BOYFRIEND)

            scene v8arcade24
            with dissolve
            play sound "sounds/kiss.mp3"
            pause 1

            scene v8arcade23
            with dissolve
            em "Thank you for the lovely evening."

            scene v8arcade23a
            with dissolve
            u "And thanks for asking me to come out. This sure beat studying."

            scene v8arcade23
            with dissolve
            em "Maybe we can do it again sometime."

            scene v8arcade23a
            with dissolve
            u "Hope so."

            scene v8arcade23
            with dissolve
            em "Goodnight, [name]."

            play sound "sounds/dooropen.mp3"

            scene v8arcade23b
            with dissolve
            u "Night."

            play sound "sounds/doorclose.mp3"

            scene v8arcade23c
            with dissolve
            pause 0.5

            scene v8arcade28
            with dissolve
            pause 0.5

            jump mon_morning_room

        "Good night":
            if lauren.relationship >= Relationship.GIRLFRIEND:
                $ add_point(KCT.BOYFRIEND)

            scene v8arcade23a
            with dissolve
            u "I had fun."

            scene v8arcade23
            with dissolve
            em "Me too, thanks for coming. Goodnight."

            play sound "sounds/dooropen.mp3"

            scene v8arcade23b
            with dissolve
            u "Night."

            play sound "sounds/doorclose.mp3"

            scene v8arcade23c
            with dissolve
            pause 0.5

            scene v8arcade28
            with dissolve
            pause 0.5

            jump mon_morning_room

label em_arcade_3:
    scene v8arcade4a
    with dissolve
    u "You're on. Let me get some change."

    scene v8arcade1y
    with dissolve
    empl "Have fun, sir!"

    scene v8arcade4e
    with fade
    u "Ladies first."

    scene v8arcade4
    with dissolve
    em "Highest payout wins?"

    scene v8arcade4a
    with dissolve
    u "Yep."

    scene v8arcade5
    with dissolve
    pause 1

    scene v8arcade5a
    with dissolve
    pause 1

    play sound "sounds/arcade_win.mp3"

    scene v8arcade5b
    with dissolve
    pause 1

    scene v8arcade6
    with dissolve
    em "Beat that!"

    scene v8arcade6a
    with dissolve
    u "Not gonna make it easy for me, are you?"

    scene v8arcade7
    with dissolve
    pause 0.5

    play sound "sounds/arcade_lose.mp3"

    scene v8arcade7a
    with dissolve
    pause 1
    u "No way I coulda won that one."

    scene v8arcade8b
    with dissolve
    em "Pay up!"

    scene v8arcade8c
    with dissolve
    u "That was just luck. I got the next one."

    scene v8arcade10
    with dissolve
    em "Maybe you'll have better luck if you go first next."

    scene v8arcade10a
    with dissolve
    u "Good thinking."

    scene v8arcade11
    with dissolve
    pause 0.5

    play sound "sounds/arcade_lose.mp3"

    scene v8arcade11a
    with dissolve
    pause 1

    scene v8arcade12
    with dissolve
    em "Or not. If I didn't know any better, I'd think you were letting me win."

    scene v8arcade12a
    with dissolve
    u "How? Haha!"

    scene v8arcade12
    with dissolve
    em "Step aside. Let me show you how it's done."

    scene v8arcade13
    with dissolve
    pause 0.5

    play sound "sounds/arcade_win.mp3"

    scene v8arcade13a
    with dissolve
    pause 1

    scene v8arcade13b
    with dissolve
    em "I'm so glad I invited you out!"

    scene v8arcade13c
    with dissolve
    u "More tokens?"

    scene v8arcade13b
    with dissolve
    em "That was the bet."

    scene v8arcade15
    with fade
    pause 0.5

    scene v8arcade15a
    with dissolve
    em "First person to get a payout wins-"

    scene v8arcade15b
    with dissolve
    u "Oh, you're going down now. I have the magic touch with this game!"

    scene v8arcade15g
    with dissolve
    em "I'm sure you do."

    scene v8arcade17
    with dissolve
    u "You're underestimating me ma'am. Watch me."

    play sound "sounds/arcade_coin.mp3"
    pause

    scene v8arcade17a
    with dissolve
    em "My turn now."

    play sound "sounds/arcade_coin.mp3"
    pause

    scene v8arcade17b
    with dissolve
    u "Wooo! I win!"
    em "Pure luck."

    scene v8arcade15h
    with dissolve
    em "Here."

    scene v8arcade15c
    with dissolve
    em "How about we increase the stakes?"
    u "How exactly?"

    scene v8arcade19
    with fade
    pause 1

    scene v8arcade19a
    with dissolve
    em "First person to get a stuffed animal is the ultimate winner."

    scene v8arcade19b
    with dissolve
    u "And?"

    scene v8arcade19a
    with dissolve
    em "Winner gets all the tokens."

    scene v8arcade19b
    with dissolve
    u "One of us will be walking around naked this week."

    scene v8arcade19c
    with dissolve
    em "Won't be me. Not the way you've been playing!"

    scene v8arcade20
    with dissolve
    em "Get ready to lose."

    play sound "sounds/arcade_lose.mp3"

    scene v8arcade20a
    with hpunch
    em "Damn it."

    scene v8arcade20b
    with dissolve
    u "Let me show you how it's done."

    play sound "sounds/arcade_lose.mp3"

    scene v8arcade20c
    with hpunch
    u "So close!"
    em "Good show. My turn now."

    scene v8arcade20
    with dissolve
    pause 1

    play sound "sounds/arcade_lose.mp3"

    scene v8arcade20a
    with hpunch
    pause 1

    scene v8arcade20b
    with dissolve
    pause 1

    play sound "sounds/arcade_lose.mp3"

    scene v8arcade20c
    with hpunch
    pause 1

    scene v8arcade20
    with dissolve
    pause 1

    play sound "sounds/arcade_lose.mp3"

    scene v8arcade20a
    with hpunch
    pause 1

    scene v8arcade20b
    with dissolve
    pause 1

    play sound "sounds/arcade_win.mp3"

    scene v8arcade20d
    with hpunch
    u "Finally!"
    em "HOW?"

    scene v8arcade21
    with dissolve
    u "It's called talen-"

    scene v8arcade21a
    with dissolve
    ann "Attention! We're closing in five minutes. Everyone is requested to leave the arcade area immediately. Thank you for visiting."

    scene v8arcade21b
    with dissolve
    em "Awww, too bad. Time to go home."

    scene v8arcade21c
    with dissolve
    u "But I was winning! I had it!"

    scene v8arcade21b
    with dissolve
    em "Sure you did. Come on. Walk me home."

    stop ambience fadeout 3

    scene v8arcade22
    with Fade(0.75, 0.25, 0.75)
    pause 0.5

    scene v8arcade23a
    with dissolve
    u "I had fun."

    scene v8arcade23
    with dissolve
    em "Me too, thanks for coming. Goodnight."

    play sound "sounds/dooropen.mp3"

    scene v8arcade23b
    with dissolve
    u "Night."

    play sound "sounds/doorclose.mp3"

    scene v8arcade23c
    with dissolve
    pause 0.5

    scene v8arcade28
    with dissolve
    pause 0.5

    jump mon_morning_room
