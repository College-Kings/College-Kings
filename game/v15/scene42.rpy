# SCENE 42: Finding Nora, Case discussion with Amber
# Locations: SVC Meeting room
# Characters: AMBER (Outfit: Detective costume), MC (Outfit: 1)
# Time: Morning

label v15s42:
# -MC enters the SVC meeting room. It's quite dated with beige/grey walls, like an old room at the FBI, a large wooden desk with a coffee machine and croissants on it., filing cabinets, blinds drawn and sparse lighting. Amber is standing next to a pinboard on the wall. We don't see the details of it just yet. Amber is wearing a stylish, Sam Spade detective-style fedora hat-
    play sound "sounds/dooropen.mp3"

    scene v15s42_1 # TPP. Show MC walking into the SVC meeting room, Description of room: Dated grey/beige walls, a large wooden desk, filing cabinets, blinds drawn with sparse lighting in the room, MC slightly confused, mouth closed.
    with fade

    pause 0.75

    play sound "sounds/dooropen.mp3"

    scene v15s42_2 # TPP. Show MC entering the room and closing the door behind him, slightly confused, mouth closed.
    with dissolve

    pause 0.75

    scene v15s42_3 # FPP. View of the room, Amber is leaning against the wall on the side of her pinboard, Amber is looking at the floor, smug face, mouth closed.
    with dissolve

    pause 0.75

    scene v15s42_3a # FPP. Amber leans against the wall and looks at MC, Amber with a smirk, mouth open.
    with dissolve

    am "[name], finally! Where have you been?"

    scene v15s42_3b # FPP. Amber walking towards MC, Amber smirking face, mouth closed.
    with dissolve

    u "Asleep?"

    scene v15s42_3c # FPP. Amber standing infront of MC, Amber smirking, mouth open.
    with dissolve

    am "Grab a coffee, we've got a lot of work to do."

    scene v15s42_4 # FPP. show Amber pouring a cup of coffee from the coffee machine, slight smile, mouth closed.
    with dissolve

    u "What is this place? *Chuckles*"

    scene v15s42_5 # FPP. MC walks up to the table and looks at the coffee station and croissants as Amber pours her cup, Amber slight smile, mouth open.
    with dissolve

    am "We really don't have time for questions, [name]."

    scene v15s42_6 # TPP. MC now with the coffee beaker pouring himself a cup of coffee, slight smile, mouth closed.
    with dissolve

    u "(Holy fuck, I needed this.)"

    scene v15s42_7 # FPP. Amber standing infront of MC, holding her cup of coffee, slight smile, mouth open.
    with dissolve

    am "We need to get busy, there's a lot of ground to cover."

    scene v15s42_8 # TPP. Wide view showing MC and Amber looking at each other both sipping their coffee.
    with dissolve

    menu:
        "Ask about the room":
            $ add_point(KCT.TROUBLEMAKER)
            
            scene v15s42_7a # FPP. Amber standing infront of MC, holding her cup of coffee, slight smile, mouth closed.
            with dissolve

            u "I wanna know where I am first, Amber. *Chuckles*"

            scene v15s42_7
            with dissolve

            am "You're in an old meeting room that the faculty doesn't... use anymore."

            scene v15s42_7a
            with dissolve

            u "What do you mean they don't use it anymore? Why?"

            scene v15s42_7
            with dissolve

            am "They don't have access anymore."

            scene v15s42_7a
            with dissolve

            u "How do you have access but the-"

            scene v15s42_7b # FPP. Amber standing infront of MC, holding her cup of coffee, Amber guilty, mouth open.
            with dissolve

            am "I have the only key, they think the door is busted, and they don't care about fixing it. Any other questions?"

            scene v15s42_7c # FPP. Amber standing infront of MC, holding her cup of coffee, Amber guilty, mouth close.
            with dissolve

            u "Haha..."

            scene v15s42_7b
            with dissolve

            am "What? Why are you laughing?"

            scene v15s42_7c
            with dissolve

            u "You're just a badass. It's hilarious sometimes."

            scene v15s42_7
            with dissolve

            am "Welcome to my office, then."

            scene v15s42_7a
            with dissolve

            u "*Laughs* Thank you. So, why are we here?"

        "Let it go":
            $ add_point(KCT.BOYFRIEND)
            
            scene v15s42_7a
            with dissolve

            u "Okay, forget it. What's happening?"

    scene v15s42_7
    with dissolve

    am "We've got a missing person case to solve."

    scene v15s42_7a
    with dissolve

    u "Nora."

    scene v15s42_7
    with dissolve

    am "Yes."

    scene v15s42_7i # FPP. Amber infront of MC, Amber holding up and looking at her pad with notes on it, Amber slight smile, mouth open.
    with dissolve

    am "She's been gone since Tuesday. Last seen at the airport."

    scene v15s42_7h # FPP. Amber infront of MC, Amber holding up and looking at her pad with notes on it, Amber slight smile, mouth closed.
    with dissolve

    u "(Since Tuesday?)"

    if joinwolves:
        u "(Chris said he saw her recently, so that can't be true.)"

    scene v15s42_7b
    with dissolve

    am "The trail has gone completely cold, but there's still way more to the story."

    scene v15s42_7c
    with dissolve

    u "I agree. So, we've got some investigating to do, right?"

    scene v15s42_7
    with dissolve

    am "Damn straight, son!"

    scene v15s42_7a
    with dissolve

    u "*Laughs* What?"

    scene v15s42_7
    with dissolve

    am "Oh, ha. Sorry... *Chuckles*"

    am "I've just been binge-watching a lot of crime shows lately, you know. To get in the right mindset."

    if v14_amber_clean: 
        scene v15s42_7a
        with dissolve

        u "How are you finding time to do all these things and have a great job?"

        scene v15s42_7
        with dissolve

        am "Haha! It's kind of amazing what you're capable of when you're not trying to get high all time..."

        scene v15s42_7a
        with dissolve

        u "Wow. Who would've thought?"

        scene v15s42_9 # TPP. Show both MC and Amber laughing.
        with dissolve

        pause 0.75

        scene v15s42_7a
        with dissolve

        u "(Amber seems to be in a really good place right now, if I wanted to make things more serious between us..."
        u "(Maybe now's the time to start?)"

        menu:
            "Flirt":
                $ add_point(KCT.BOYFRIEND)
                $ v15s42_flirt = True
                
                u "Sobriety looks great on you."

                u "But then again, everything looks great on you so..."

                scene v15s42_7d # FPP. MC looking at Amber, Amber looking at MC, Amber's eyes light up, Amber blushing, Amber full smile, mouth open.
                with dissolve

                am "Even being obsessed with crime shows?"

                scene v15s42_7a
                with dissolve

                u "Well, just don't murder me and we'll be alright."

                scene v15s42_7
                with dissolve

                am "*Giggles* Okay, I can manage that I think."

            "Friendly compliment":
                $ add_point(KCT.BRO)

                scene v15s42_7a
                #with dissolve

                u "Sobriety looks great on you, not gonna lie."

                scene v15s42_7
                with dissolve

                am "Thanks, [name]."

    else:
        scene v15s42_7a
        with dissolve

        u "Aren't you tired from dancing until three in the morning? How do you do so much all the time?"

        scene v15s42_7
        with dissolve

        am "Oh, pfft. I don't really get tired anymore, haha."

        am "The excitement from work, stress from school, and high from the drugs all really just keeps my eyes glued open."

        scene v15s42_7a
        with dissolve

        u "Oh, that sounds... Good."

    scene v15s42_7
    with dissolve

    am "Last night, I started watching this classic noir movie, like the old black and white ones? I'm learning a lot!"

    scene v15s42_7a
    with dissolve

    u "I mean, that's great! Haha, it explains the hat."

    scene v15s42_7
    with dissolve

    am "The hat is a very important part of any detective's process."

    scene v15s42_7a
    with dissolve

    u "Hmm, is that true?"

    scene v15s42_7
    with dissolve

    am "Yes, it's true! A dependable outfit is one thing, your hat has to fit your attitude."
    am "But the main thing we need to decide on before we can start investigating is..."

    scene v15s42_7e # FPP. MC looking at Amber, Amber looking at MC, Amber holding her coffee cup with both hands studying MC, Amber suspicious, mouth open.
    with dissolve

    am "What type of detective you are."

    scene v15s42_7a
    with dissolve

    u "What type of detective am I? I thought you were the lead investigator"

    scene v15s42_7
    with dissolve

    am "Well, yeah, I am. But you have to really like... Feel the role."

    scene v15s42_7a
    with dissolve

    u "Amber."

    scene v15s42_7
    with dissolve

    am "Oh, come on! Just play along, would you?"

    scene v15s42_7a
    with dissolve

    u "Hmm, okay. Fine."

    scene v15s42_7
    with dissolve

    am "So, take a look and see what speaks to you..."

    scene v15s42_7a
    with dissolve

    pause 0.75

    menu:
        "Select detective type"
        "Professional":
            $ mc.detective = Detective.PROFESSIONAL
        "Psychologist":
            $ mc.detective = Detective.PSYCHOLOGIST
        "Loose Cannon":
            $ mc.detective = Detective.LOOSE_CANNON

    # -A UI pops up to show the three detective archetypes that MC can choose from (Professional, Psychologist, Loose Cannon). MC makes his choice and the UI disappears again-

    if mc.detective = Detective.PROFESSIONAL:
        scene v15s42_7a
        with dissolve

        u "A professional."

        scene v15s42_7
        with dissolve

        am "Yeah?"

        scene v15s42_7a
        with dissolve

        u "Yeah, I think logically. The facts never lie, two plus two equals four..."

        scene v15s42_7
        with dissolve

        am "Haha, okay fair. Yeah! I can see this."

    elif mc.detective = Detective.PSYCHOLOGIST:
        scene v15s42_7a
        with dissolve

        u "A psychologist."

        scene v15s42_7
        with dissolve

        am "You think?"

        scene v15s42_7a
        with dissolve

        u "Oh yeah. I want to get into the minds of people and figure out what they're thinking and what they know."

        scene v15s42_7
        with dissolve

        am "Okay, cool! So, you'll be good at analyzing every word and figuring out if they're lying or telling us the truth."

    elif mc.detective = Detective.LOOSE_CANNON:
        scene v15s42_7a
        with dissolve

        u "A loose cannon."

        scene v15s42_7f # FPP. MC looking at Amber, Amber looking at MC, Amber confused, mouth open.
        with dissolve

        am "For sure?"

        scene v15s42_7a
        with dissolve

        u "For damn sure. I'll slam someone's head through a wall if it helps us find Nora."

        scene v15s42_7
        with dissolve

        am "Ooh..."

        if v15s42_flirt:
            scene v15s42_7g # FPP. MC looking at Amber, Amber looking at MC, Amber smirking, mouth closed.
            with dissolve
            
            pause 0.75
            
        scene v15s42_7
        with dissolve

        am "Let's try not to kill anyone, though, okay? *Laughs*"

        scene v15s42_7a
        with dissolve

        u "*Sighs* Fine."

    scene v15s42_7a
    with dissolve

    u "Okay so, what's the first step, detective?"

    scene v15s42_10 # Close up of just Amber pointing at the pinboard she was working on, Amber slight smile, mouth open.
    with dissolve

    am "Well, I made this so we can gather all of our findings in one place..."

    am "There's a shit ton of clues, we just have to find them."

    scene v15s42_11 # FPP. MC standing closer looking at the board as Amber is looking at the board and pointing at it, Amber slight smile, mouth closed.
    with dissolve

    pause 0.75

# -The UI pops up to show MC the headings Clues and Possible Locations, they currently have question marks over the unlockable items. MC exits the UI whenever-

    scene v15s42_12 # FPP. MC standing by the board, MC looking at Amber, Amber looking at Mc, Amber slight smile, mouth closed.
    with dissolve

    u "Okay, nice. So, where do you think we'll find clues?"

    scene v15s42_12a # FPP. MC standing by the board, MC looking at Amber, Amber looking at Mc, Amber slight smile, mouth open.
    with dissolve

    am "Our first line of duty is to interrogate the prime suspect."

    scene v15s42_12
    with dissolve

    u "Chris?"

    scene v15s42_12a
    with dissolve

    am "Ha. Glad we agree on that."

    scene v15s42_12
    with dissolve

    u "Okay, let's head out. I want to get to the bottom of this."

    scene v15s42_12a
    with dissolve

    am "Me and you both!"

    am "Oh wait, did you want to bring a snack with you? You should eat."

    scene v15s42_12
    with dissolve

    pause 0.75

    menu:
        "Grab breakfast":
            $ add_point(KCT.BOYFRIEND)
            $ v15s42_grab_breakfast = True
            
            scene v15s42_13 # TPP. Show MC grabbing a croissant, slight smile, mouth open.
            with dissolve

            u "I guess you're right. Most important meal of the day, huh?"

            scene v15s42_13a # TPP. MC takes a bite from the croissant.
            with dissolve

            pause 0.75

        "Not hungry":
            $ add_point(KCT.BRO)
            
            scene v15s42_12
            with dissolve

            u "I'm not that hungry right now. Kind of just want to get to work."

            scene v15s42_12a
            with dissolve

            am "You're not having breakfast?"

            scene v15s42_12
            with dissolve

            u "No. Is that okay?"

            scene v15s42_12a
            with dissolve

            am "I mean, you'll probably regret it."

    scene v15s42_12a
    with dissolve

    am "A smart detective works on a full stomach, and that coffee helps you stay alert."

    scene v15s42_12
    with dissolve

    u "Damn, you're really into this whole thing, Amber. Maybe you should do this for a living?"

    scene v15s42_12a
    with dissolve

    am "Be a cop? Hell no."

    scene v15s42_12
    with dissolve

    u "Haha, no, of course not. But, maybe like a private investigator."

    scene v15s42_12a
    with dissolve

    am "Hmm, maybe. Let's see how we do today, and I might think about it."

    scene v15s42_12
    with dissolve

    u "Sounds good to me."

    if v15s42_grab_breakfast:
        play sound "sounds/dooropen.mp3"

        scene v15s42_14 # TPP. Show Amber and MC leaving the meeting room, Amber slight smile, mouth closed, MC eating the last of his croissant as they leave the room.
        with dissolve

        pause 0.75

    else:
        play sound "sounds/dooropen.mp3"

        scene v15s42_14a # TPP. Show Amber and MC leaving the meeting room, Amber slight smile, mouth closed, MC slight smile, mouth closed.
        with dissolve

    pause 0.75

    play sound "sounds/doorclose.mp3"

    scene v15s42_14b # TPP. Amber and MC gone the door to the meeting room closed.
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v15s43