# SCENE 07: 7) Shopping at Lew's with Aubrey/Catching Amber working
# Locations: MC bedroom, sidewalk, lew's clothing store
# Characters: MC (outfit 9), Aubrey (Outfit 1), Amber (smart button up shits and trousers(may need new outfit from lew))
# Time: Friday Morning

label v11_room_aubrey_shopping:
    play music "music/v11/Track Scene 7_1.mp3" fadein 2
    if joinwolves:
        scene v11auw1 # TPP. Show MC sitting on his bed, as if he had just woken up, he's tired and yawning (New Wolves room)
        with fade

        pause 0.75

        play sound "sounds/twig.mp3"

        scene v11auw2 # TPP. Show a pebble hitting the room's window
        with dissolve

        u "(What is that?)"

        stop sound

        scene v11auw1a # TPP. Same cam as v11auw1, Show MC standing up next to his bed, looking at the window, he is walking, has a startled expression (New Wolves room)
        with dissolve

        pause 1

    else:
        scene v11auw3 # TPP. Show MC sitting on his bed, as if he had just woken up, he's tired and yawning (Apes room)
        with fade

        pause 0.75

        play sound "sounds/twig.mp3"

        scene v11auw2 # TPP. Show a pebble hitting the room's window
        with dissolve

        u "(What is that?)"

        stop sound

        scene v11auw3a # TPP. Same cam as v11auw3, Show MC standing up next to his bed, looking at the window, he is walking, has a startled expression (Apes room)
        with dissolve

        pause 1

    scene v11auw4 # FPP. MC is looking out of his window to Aubrey, who is looking back at him, she is smiling, mouth closed
    with dissolve

    u "*Laughs* Why don't you just knock like a normal person? You're gonna break my window one of these days."

    scene v11auw4a # FPP. Same as v11auw4, Aubrey is smiling, mouth open
    with dissolve

    au "Because I'm not normal."

    scene v11auw4
    with dissolve

    u "Clearly. What's up?"

    scene v11auw4a
    with dissolve

    au "I need to go shopping, I wanna get some cute clothes for Europe."

    scene v11auw4
    with dissolve

    u "And let me guess, you need someone to carry your bags."

    scene v11auw4a
    with dissolve

    au "*Laughs* You said it, not me! But I was more so thinking you may want to get some clothes too..."

    scene v11auw4
    with dissolve

    u "I already have clothes."

    scene v11auw4a
    with dissolve

    au "There's always room for improvement. *Laughs*"

    scene v11auw4
    with dissolve

    u "Funny. Give me two secs and I'll be down."

    scene v11auw4a
    with dissolve

    au "Hurry, it's windy out here."
    stop music fadeout 3
    play music "music/v11/Track Scene 7_2.mp3" fadein 2
    scene v11auw5 # TPP. Show MC and Aubrey walking on the sidewalk (around the city, near where Lew's will be) both of them mouth closed, happy expression
    with fade

    pause 0.75

    scene v11auw6 # FPP. MC and Aubrey are walking, looking at each other, Aubrey mouth closed, smiling
    with dissolve

    u "What store are we going to?"

    scene v11auw6a # FPP. Same as v11auw6, Aubrey mouth open, smiling
    with dissolve

    au "The only store worth going to, Lew's."

    scene v11auw6
    with dissolve

    u "Now I know I'm not getting anything. Nothing there is less than $45. I probably can't even afford a sock from Lew's. *Laughs*"

    scene v11auw6a
    with dissolve

    au "*Chuckles* It's not that bad, I'm sure we can find you something."

    scene v11auw6
    with dissolve

    u "Whenever I glance at that place all the customers look rich. Pretty sure one guy walked in with a security guard. You know how rich you gotta be to have your own security guard?"

    scene v11auw6a
    with dissolve

    au "*Chuckles* Just look around a bit at least, and if you end up not getting anything, you can still help me carry my bags."

    scene v11auw6
    with dissolve

    u "And finally we've gotten to the real reason I'm here."

    scene v11auw6a
    with dissolve

    au "Again, you said it, not me. *Laughs*"

    stop music fadeout 3
    play music "music/v11/Track Scene 7_3.mp3" fadein 2

    scene v11auw7 # TPP. Show MC and Aubrey walking through the door of Lew's shop. They're both smiling, mouths closed
    with dissolve

    pause 1.25

    scene v11auw8 # FPP. MC is standing next to Aubrey who is looking through a clothe rack, mouth closed, smiling
    with dissolve

    u "Make sure you get something really nice, maybe that can help take everyone's mind off of you getting your ass kicked during mud wrestling."

    scene v11auw8a # FPP. Same cam as v11auw8, Aubrey is now looking at MC, smiling, mouth open
    with dissolve

    au "*Laughs* Hey... Emily is stronger than she looks. That was not a fair matchup."

    scene v11auw8b # FPP. Same cam as v11auw8, Aubrey is now looking at MC, smiling, mouth closed
    with dissolve

    u "You chose to fight her though."

    scene v11auw8a
    with dissolve

    au "That was before I knew she was Hulk Jr."

    scene v11auw8b
    with dissolve

    u "Excuses. *Chuckles*"

    scene v11auw8a
    with dissolve

    au "Hey, at least our fight was civilized. Unlike Nora and Chloe's..."

    scene v11auw8b
    with dissolve

    u "It did get pretty intense."

    scene v11auw8a
    with dissolve

    au "Those two have been at each other's throats for too long now."

    scene v11auw8b
    with dissolve

    u "What do you mean?"

    scene v11auw8a
    with dissolve

    au "All they do is fight."

    scene v11auw8b
    with dissolve

    u "Does it affect the sorority?"

    scene v11auw8a
    with dissolve

    au "Of course it does. We can't do anything without them throwing sly comments at each other."

    scene v11auw8b
    with dissolve

    u "So, what's the solution? You guys could fight it out like we do. *Laughs*"

    scene v11auw8a
    with dissolve

    au "That wouldn't be good. It sucks cause I feel like I'm right in the middle of it all. I'm friends with Chloe, and I'm VP, but I'm cool with Nora too. It's just hard."

    au "I think we need to make some changes. I don't know what, but something has to change."

    scene v11auw8b
    with dissolve

    u "Sounds like they need to figure their shit out."

    scene v11auw8a
    with dissolve

    au "Yeah..."

    scene v11auw8
    with dissolve

    pause 0.75

    scene v11auw8c # FPP. Same cam as v11auw8, Aubrey is now holding one outfit in either hand, she is showing them to MC, she is smiling, mouth opened
    with dissolve

    au "Here, look. Which one do you think is better?"

    scene v11auw8d # FPP. Same cam as v11auw8, Aubrey is now holding one outfit in either hand, she is showing them to MC, she is smiling, mouth closed
    with dissolve

    menu:
        "The white one":
            u "The white one."

        "The blue one":
            u "The blue one."
        
    scene v11auw8e # FPP. Same cam as v11auw8, Aubrey is now holding the outfits by her side, she is smiling, mouth open
    with dissolve

    au "Good, if we do anything in Europe together I'll wear this one, but I'm getting both. *Chuckles*"

    scene v11auw8f # FPP. Same cam as v11auw8, Aubrey is now holding the outfits by her side, she is smiling, mouth closed
    with dissolve

    u "Haha."

    scene v11auw8e
    with dissolve

    au "Are you getting anything?"

    scene v11auw8f
    with dissolve

    menu:
        "Get something":
            scene v11auw8f
            with dissolve

            u "Yeah, I'll get a new shirt. Let me see how much money I-"

            scene v11auw8e
            with dissolve

            au "What?"

            scene v11auw8f
            with dissolve

            u "I forgot to grab my wallet."

            scene v11auw8e
            with dissolve

            au "This is why you should never rush. *Chuckles*"

            scene v11auw8f
            with dissolve

            u "I was rushing because someone was crying about the wind."

            scene v11auw8e
            with dissolve

            au "*Chuckles* Okay, good point. I'll get it for you."

            scene v11auw8f
            with dissolve

            u "You don't need to do that."

            scene v11auw8e
            with dissolve

            au "Based on what you're wearing now... yes I do."

        "Don't get anything":
            scene v11auw8f
            with dissolve

            u "I'm good."

            scene v11auw8e
            with dissolve

            au "No you're not."

            scene v11auw8f
            with dissolve

            u "What's wrong with what I'm wearing?"

            scene v11auw8e
            with dissolve

            au "Haha, well to start... everything. *Laughs*"

            scene v11auw8f
            with dissolve

            u "Okay fine, what should I get?"

            scene v11auw8e
            with dissolve

            au "Here, you can get this."
    
    # -A pop up of the new outfit is shown-

    scene v11auw8g # FPP. Same cam as v11auw8, MC is holding up his new outfit in front of him and he's looking at it, Aubrey is hidden behidn the new shirt
    with dissolve

    pause 1.25

    scene v11auw8e
    with dissolve

    u "Alright, I can rock this."

    scene v11auw8f
    with dissolve

    au "Let's go ring all this stuff up."

    scene v11auw9 # FPP. MC is walking up to the register, Amber looks at MC, she has a shocked face (MC is not too close to the register)
    with dissolve

    pause 0.75

    scene v11auw10 # FPP. MC is now at the register, Amber ducked down below the register, she is looking at the manager, mouth closed, worried expression. The manager is off to her side, looking at her, mouth open, slightly angry
    with dissolve

    mana "What are you doing?"

    scene v11auw10a # TPP. Same cam as v11auw10, Amber mouth open, looking at manager, worried expression, Manager slightly angry, looking at her, mouth closed
    with dissolve

    am "Sorry, I ugh... I dropped my contact."

    scene v11auw11 # FPP. Amber is now standing at the register, looking at MC, her mouth is open, worried expression, Manager has left
    with dissolve

    am "What are you guys doing here?"

    scene v11auw11a # FPP. Same cam as v11auw11, Amber mouth closed, worried expression
    with dissolve

    u "Shopping, obviously. *Laughs*"

    u "The real question is, what are you doing here?"

    scene v11auw11
    with dissolve

    am "Working, \"obviously\"."

    scene v11auw11a
    with dissolve

    u "At Lew's? *Chuckles* How'd you even get a job at a place like this?"

    scene v11auw11
    with dissolve

    am "I worked hard to get this job just so I didn't have to run into people that I know, plus the pay is good. So, can you guys try to keep this to yourselves?"

    am "I really don't want everyone knowing where I work."

    scene v11auw11a
    with dissolve

    menu:
        "Of course":
            $ amber.points += 1
            $ reputation.add_point(RepComponent.BOYFRIEND)

            scene v11auw11b # FPP. Same cam as v11auw11, Amber mouth closed, slight smile
            with dissolve

            u "Of course, I won't say anything. I wouldn't wanna ruin that badass reputation of yours."

            scene v11auw11c # FPP. Same cam as v11auw11, Amber mouth open, slight smile
            with dissolve

            am "*Laughs* Thanks."

            scene v11auw12 # FPP. MC is looking at Aubrey, Aubrey is looking at Amber, Aubrey has mouth open, slight smile (MC is next to Aubrey, Amber is at the cash register, same positioning as v11auw11)
            with dissolve

            au "For sure, no worries."

            scene v11auw11d # FPP. Same cam as v11auw11, MC looking at Amber, Amber looking at Aubrey, mouth open, slight smile (Aubrey is next to MC, Aubrey out of shot)
            with dissolve

            am "Thanks, Aubrey."

        "Tease":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            $ amber.points -= 1
            $ v11_tease_amber += 1

            scene v11auw11a
            with dissolve

            u "I might be able to keep quiet, but who knows. What's in it for me?"

            scene v11auw11
            with dissolve

            am "[name], please just shut up about it."

            scene v11auw11a
            with dissolve

            u "Okay okay."

            scene v11auw12
            with dissolve

            au "For sure, no worries."

            scene v11auw11d
            with dissolve

            am "Thanks, Aubrey."

    scene v11auw11e # FPP. Same cam as v11auw11, manager is now in shot, next to Amber, Amber mouth open, slight smile
    with dissolve

    am "Anything else I can get you ma'am? Sir?"

    scene v11auw11f # FPP. Same cam as v11auw11, manager is now in shot, next to Amber, Amber mouth closed, slight smile
    with dissolve

    u "*Laughs* Nope, have a nice day."

    scene v11auw11e
    with dissolve

    am "You too, come back and see us soon."

    scene v11auw7a # TPP. Same cam as v11auw7, but MC and Aubrey are now walking out of the store
    with dissolve

    pause 0.75
    
    scene v11auw13 # FPP. MC and Aubrey are walking looking at each other, Aubrey mouth open, smiling (different sidewalk than v11auw6), Aubrey is carrying the bags from her purchase
    with dissolve

    au "She's going to Europe, right?"

    scene v11auw13a # FPP. Same cas v11auw3, Aubrey mouth closed, smiling
    with dissolve

    u "Hmmm, I think so."

    scene v11auw13
    with dissolve

    au "This trip just got way more interesting. *Chuckles*"

    scene v11auw13a
    with dissolve

    menu:
        "Agree":
            scene v11auw13a
            with dissolve

            u "Haha, it sure did. Amber's in for one."

        "Disagree":
            scene v11auw13a
            with dissolve

            u "Haha, maybe we should just keep it to ourselves. It is pretty funny though."
        
    scene v11auw13
    with dissolve

    au "Alright, I know I was joking at first, but could you actually help me get this stuff to the house?"

    scene v11auw13a
    with dissolve

    u "*Sighs* If I have to. *Chuckles*"

    scene v11auw13
    with dissolve

    au "Much appreciated. *Laughs*"

    scene v11auw14 # TPP. Show MC and Aubrey walking on the sidewalk, they're each holding a bag from their purchase at Lew's, they're both smiling, mouths closed
    with dissolve

    pause 0.75

    jump v11_chicks_house
# -Transition to Scene 8-