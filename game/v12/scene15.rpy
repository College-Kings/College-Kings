# SCENE 15: 2nd riddle with Riley
# Locations: Catacomb entrance, inside the catacomb, sidewalk, in front of hotel, hotel lobby 
# Characters: MC (Outfit: 5), RILEY (Outfit: 2)
# Time: afternoon

label v12_riddle_riley:
    scene v12rrl1 # TPP. MC and riley standing outside the catacombs
    with fade

    pause 1.25

    play music music.ck1.v12.Track_Scene_15_1 fadein 2

    scene v12rrl2 # FPP. MC looking at riley, mouth closed
    with dissolve

    u "Where the fuck are we?"

    scene v12rrl2a # FPP. Riley smiling slightly, mouth opened
    with dissolve

    ri "The catacombs. *Chuckles* This is the spot of the next clue."

    scene v12rrl2
    with dissolve

    u "I really doubt that, but... Then again, I don't know the riddle."

    scene v12rrl2b # FPP. Same as 2, mouth opened
    with dissolve

    ri "Don't doubt my skills, [name]. But if you must know, listen. \"In the city of love, where sleeping hearts lie, not down in the river but where the ancestors lie.\""

    scene v12rrl2
    with dissolve

    u "So, why here? \"Where ancestors lie\" could be any cemetery. Hell, it could be a pyramid or a museum."

    scene v12rrl2b
    with dissolve

    ri "First of all, there are no pyramids in Paris. Second, I saw a picture of the catacombs at Duncan's. And third, there's nothing special about a regular cemetery."

    scene v12rrl2
    with dissolve

    u "Riley! Don't say things like that, especially about a burial ground. *Chuckles*"

    scene v12rrl2b
    with dissolve

    ri "What? I didn't mean it in a bad way... I'm just saying in regard to the treasure hunt, it's more likely to be here."

    scene v12rrl2
    with dissolve

    u "Hating on the dead is never a good thing. When the zombies, ghosts or whatever comes, I won't be there to help you. But at least you'll have your super power and you can tell them if they're hungry. *Laughs*"

    scene v12rrl2a
    with dissolve

    ri "Oh my gosh, c'mon already."

    scene v12rrl3 # TPP. MC and riley enter the catacombs, back to the camera
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music music.v12_Track_Scene_15_2 fadein 2

    scene v12rrl4 # FPP. MC looking at riley, mouth closed
    with dissolve

    u "This is confusing, how are we supposed to know where to go or what to do?"

    scene v12rrl4a # FPP. Same as 4, mouth opened
    with dissolve

    ri "Don't be a party pooper, just follow me."

    scene v12rrl5 # TPP. Riley leading MC arround the catacombs
    with dissolve

    pause 0.75

    scene v12rrl6 # TPP. Riley leading MC arround the catacombs
    with dissolve

    pause 0.75

    scene v12rrl7 # FPP. MC looking at riley, mouth opened
    with dissolve

    ri "I'm pretty sure this is where the bodies are put."

    scene v12rrl7a # FPP. Same as 7, mouth closed
    with dissolve

    u "I feel like we're not supposed to be down here."

    scene v12rrl7
    with dissolve

    ri "Maybe we are, maybe we aren't. Start looking around for the next clue... I'm positive it's here somewhere."

    scene v12rrl8 # TPP. MC and riley looking arround trying to find the clue
    with dissolve

    pause 0.6
    
    scene v12rrl9 # TPP. MC and riley looking arround trying to find the clue
    with dissolve

    menu:
        "Keep looking" (boyfriend=1.0):
            $ reputation.add_point(RepComponent.BOYFRIEND)
            scene v12rrl10 # FPP. MC still searching looking at riley who is also still searching, mouth closed
            with dissolve

            u "Did you find anything?"

            scene v12rrl10a # FPP. Same as 10, mouth opened
            with dissolve

            ri "Not yet, you?"

            scene v12rrl10 
            with dissolve

            u "Nope, still looking. I'm telling you Riley, there's nothing down h-"

        "Give up" (bro=1.0):
            $ reputation.add_point(RepComponent.BRO)
            scene v12rrl11 # TPP. MC sits down
            with dissolve

            pause 0.75

            scene v12rrl12 # FPP. MC sitting down, looking at riley, mouth closed
            with dissolve
            
            u "*Sighs*"

            scene v12rrl12a # FPP. Same as 12, Riley looking confused, mouth opened
            with dissolve

            ri "Why are you sitting?"

            scene v12rrl12
            with dissolve

            u "I give up, I can't find it. I'm telling you there's nothing down here."

            scene v12rrl12b # FPP. Riley with her hands in her hand as if she is asking for help
            with dissolve

            ri "C'mon, please? I can't find it myself."

            scene v12rrl12
            with dissolve

            u "Oh, I'm sure you can."

            scene v12rrl12c # FPP. Riley searching, looking back at MC, mouth opened
            with dissolve

            ri "[name]..."

            scene v12rrl13 # TPP. MC stands up
            with dissolve

            pause 0.75

    scene v12rrl69420 # FPP. MC standing a little away from riley, mouth opened
    with dissolve

    ri "Oh, wait! I just found something."

    scene v12rrl14 # TPP. MC walks over to riley
    with dissolve

    pause 1.25

    scene v12rrl15 # FPP. MC looking at riley, mouth closed
    with dissolve

    u "I stand corrected... *Chuckles* What is it?"

    scene v12rrl16 # TPP. MC and riley looking at a piece of paper in the wall
    with dissolve

    pause 1.25

    scene v12rrl15a # FPP. Same as 15, mouth opened
    with dissolve

    ri "This has to be the clue."

    scene v12rrl15
    with dissolve

    u "Pull it out."

    scene v12rrl15
    with dissolve

    ri "..."

    scene v12rrl15
    with dissolve

    u "What?"

    scene v12rrl15b # FPP. Riley looking uneasy, mouth opened
    with dissolve

    ri "I'm kind of nervous."

    scene v12rrl15
    with dissolve

    u "Why? It's just a piece of paper. *Chuckles*"

    scene v12rrl15b
    with dissolve

    ri "All we had to do was look around for it... This almost feels too easy."

    scene v12rrl15
    with dissolve

    u "*Sighs* Fine. I'll do it."

    scene v12rrl17 # TPP. MC pulls the piece of paper out of the wall
    with dissolve

    pause 0.75

    scene v12rrl15c # FPP. MC now holding the piece of paper looking at riley, mouth closed
    with dissolve

    u "See, nothing went wrong."

    scene v12rrl15d # FPP. MC hands riley the piece of paper 
    with dissolve

    pause 0.6

    scene v12rrl15e # FPP. Riley now holding the peace of paper, still looking ueasy, mouth opened
    with dissolve

    ri "You're not suspicious or anything?"

    scene v12rrl15f # FPP. Same as 15e, mouth closed
    with dissolve

    u "Why? Should I be?"

    scene v12rrl15e
    with dissolve

    ri "Well, you know-"

    scene v12rrl15g # FPP. The lights go out, looking at riley, mouth closed
    with dissolve

    u "What the fuck?"

    scene v12rrl15h # FPP. Riley looking back, mouth opened
    with dissolve

    ri "And... Now we're in the dark."

    scene v12rrl15g
    with dissolve

    u "*Sighs* I'm starting to really hate these shitty riddles."

    scene v12rrl15i # FPP. Riley smling
    with dissolve

    ri "*Chuckles*"

    scene v12rrl15e
    with dissolve

    ri "Oh nice, we're good I guess. Let's get back and..."

    scene v12rrl15f
    with dissolve

    u "And... what?"

    scene v12rrl15e
    with dissolve

    ri "I actually don't know how to get back, do you?"

    scene v12rrl15f
    with dissolve

    u "I was just following you."

    scene v12rrl15h
    with dissolve

    ri "Okay, what is going on?"

    scene v12rrl15g
    with dissolve

    u "I have no fucking clue..."

    scene v12rrl18 # TPP. Lights flickering on as time passes
    with dissolve

    pause 0.75

    scene v12rrl19 # TPP. Lights flickering off as time passes
    with dissolve

    pause 0.75

    scene v12rrl20 # FPP. Lights flickering on, riley looking spooked, mouth opened
    with dissolve

    ri "Let's get the fuck out of here, now. Please hold my hand so we don't get lost."

    scene v12rrl20
    with dissolve

    ri "You pick! Which way should we go?"

    menu:
        "Left":
            scene v12rrl21 # FPP. Looking at a tunnel that has a left and right exit
            with dissolve

            u "Pretty sure it's this way."

            scene v12rrl22 # TPP. MC and riley going left
            with dissolve

            pause 0.75

        "Right":
            scene v12rrl21
            with dissolve
            
            u "Let's try this way."

            scene v12rrl23 # TPP. MC and riley going right
            with dissolve

            pause 0.75
    
    scene v12rrl24 # TPP. Time passing montage #1
    with dissolve

    pause 1

    scene v12rrl25 # TPP. Time passing montage #2
    with dissolve

    pause 1

    scene v12rrl26 # TPP. Time passing montage #3
    with dissolve

    pause 1

    scene v12rrl27 # FPP. pointing at the exit
    with dissolve

    u "Look, that's the exit! C'mon."

    scene v12rrl28 # FPP. Looking at riley, slight smile, mouth opened
    with dissolve

    ri "Finally..."

    scene v12rrl29 # TPP. MC and riley walking out
    with dissolve

    pause 0.75

    scene v12rrl30 # TPP. Riley trips
    with dissolve

    pause 0.6

    stop music fadeout 3
    play music music.ck1.v12.Track_Scene_15_3 fadein 2

    play sound sound.hit
    scene v12rrl31 # FPP. Riley on the ground, looking hurt, hand on her leg, mouth opened
    with dissolve

    ri "OW OW OW OW OW! Fuck!"

    scene v12rrl31a # FPP. Same as 31, mouth closed
    with dissolve

    u "Oh shit, are you okay?"

    scene v12rrl31 
    with dissolve

    ri "Not exactly. I think I fucked up my ankle..."

    scene v12rrl31a
    with dissolve

    u "Can you walk?"

    scene v12rrl31 
    with dissolve

    ri "Not comfortably... I'm sorry."

    menu:
        "Help her walk" (bro=1.0):
            $ reputation.add_point(RepComponent.BRO)
            scene v12rrl32 # TPP. MC helps riley stand up
            with dissolve

            pause 0.75

            scene v12rrl33 # TPP. Riley arround mc's shoulder as they walk together
            with dissolve

            pause 0.75

            scene v12rrl34 # FPP. Riley arround MC's shoulder, looking at riley, mouth closed
            with dissolve

            u "It's fine, c'mon."

            scene v12rrl34a # FPP. Same as 34, mouth opened
            with dissolve

            ri "Thanks. It's probably not that bad. *Chuckles* It'll likely be fine in a few minutes, it surprised me more than it hurt."

            scene v12rrl34
            with dissolve

            u "Don't worry, I got you. But, everything that's happened so far has just given me more of a reason to not like this stupid hunt."

            scene v12rrl34a
            with dissolve

            ri "We are running into every problem possible aren't we? *Chuckles*"

            scene v12rrl34
            with dissolve

            u "*Laughs* Let's get you back..."

            scene v12rrl34a
            with dissolve

            ri "Oh yeah, Mr. Lee has an event planned for when we get back."

            scene v12rrl34
            with dissolve

            u "*Sighs* Yay... More Mr. Lee stuff."

            scene v12rrl35 # TPP. MC and Riley heading on the sidewalk in front of the catacombs, riley still arround MC's shoulder
            with dissolve

            pause 1

            scene v12rrl36 # TPP. MC and riley in front of the hotel, riley still arround MC's shoulder
            with dissolve

            pause 1

            scene v12rrl37 # TPP. MC and Riley going into the lobby, riley still arround MC's shoulder
            with dissolve

            pause 1

        "Carry her" (boyfriend=1.0):
            $ reputation.add_point(RepComponent.BOYFRIEND)
            scene v12rrl38 # TPP. MC Picks up riley
            with dissolve

            pause 1.25

            scene v12rrl39 # FPP. Riley on MC's arm, smiling, mouth closed
            with dissolve

            u "No worries. This okay?"

            scene v12rrl39a # FPP. Same as 39, mouth opened
            with dissolve

            ri "Woah, haha! This feels like a scene in a movie and I'm the princess."

            scene v12rrl39 
            with dissolve

            u "Guess that makes me a prince."

            scene v12rrl40 # TPP. Riley carreses MC's cheek
            with dissolve

            pause 0.75

            scene v12rrl39b # FPP. Riley making a seducing face, mouth opened
            with dissolve

            ri "I guess it does."

            menu:
                "Kiss her" (boyfriend=1.0):
                    $ reputation.add_point(RepComponent.BOYFRIEND)

                    scene v12rrl41 # TPP MC kisses Riley
                    with dissolve

                    play sound sound.kiss

                    pause 1

                    scene v12rrl39b
                    with dissolve

                    ri "I'm definitely into the more hot and sexy vibes, but this was probably the most romantic thing I've ever experienced."

                "Don't kiss her":
                    pass 
    
            scene v12rrl39a 
            with dissolve

            ri "*Chuckles* You're so sweet, [name]."

            scene v12rrl39
            with dissolve

            u "Thanks... You give me many reasons to be. Now, let's get you back."

            scene v12rrl39a
            with dissolve

            ri "Actually, I think I'm feeling fine enough to walk."

            scene v12rrl39
            with dissolve

            u "You sure?"

            scene v12rrl39a
            with dissolve

            ri "Yeah, I'm sure."

            scene v12rrl42 # TPP. MC places riley down 
            with dissolve

            pause 0.75

            scene v12rrl43 # TPP. MC and riley start walking, in front of the catacombs
            with dissolve

            pause 0.75

            scene v12rrl44 # FPP. Now walking with riley, mouth opened
            with dissolve

            ri "Also, I'm pretty sure Mr. Lee has something planned for us once we get back."

            scene v12rrl44a # FPP. Same as 44, mouth closed
            with dissolve

            u "*Sighs* Yayyyyyy."

            scene v12rrl44b # FPP. Riley smiling, mouth opened
            with dissolve

            ri "*Chuckles*"

            scene v12rrl44c # FPP. Riley reaches for mc's hand
            with dissolve

            menu:
                "Hold her hand" (boyfriend=1.0):
                    $ reputation.add_point(RepComponent.BOYFRIEND)
                    scene v12rrl45 # TPP. MC and riley hold hands 
                    with dissolve

                    pause 0.75

                    scene v12rrl46 # TPP. MC and riley and MC holding hands in front of the hotel
                    with dissolve

                    pause 0.75

                    scene v12rrl47 # TPP. MC and Riley in the hotel lobby still holding hands
                    with dissolve

                "Scratch your face" (bro=1.0):
                    $ reputation.add_point(RepComponent.BRO)
                    scene v12rrl48 # TPP. MC scratches his face
                    with dissolve

                    pause 1

                    scene v12rrl49 # TPP. MC and riley walking back, in front of the hotel
                    with dissolve

                    pause 1

                    scene v12rrl50 # TPP. MC and riley in the hotel lobby
                    with dissolve

                    pause 1
    
    stop music fadeout 3

    jump v12_valentine #scene 16