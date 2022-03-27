# SCENE 55: Prepare Lindsey for the Interview
# Locations: College library
# Characters: MC (Outfit: 2), Lindsey (Outfit: 3)
# Time: Thursday Morning

label v16s55: # 55) Prepare Lindsey for the interview
    scene v16s55_1 # TPP Show MC from behind walking into library. Ahead of him, Lindsey is sitting at a table in the corner of the library, looking at her phone
    with dissolve

    pause 0.75

    scene v16s55_2 # TPP Show MC (slight smile, mouth open) taking a seat at the table opposite Lindsey. Lindsey (slight smile, mouth closed) still looking at her phone
    with dissolve

    u "Hey, Linds."

    scene v16s55_3 # FPP MC's view of Lindsey (tired, mouth closed) across table. She is putting her phone away.
    with dissolve

    pause 0.75

    scene v16s55_3a # FPP Same angle as 3. Lindsey (eyes closed, mouth open) stretching and yawning dramatically
    with dissolve

    li "*yawns*"

    scene v16s55_3b # FPP Same angle as 3. Lindsey (neutral expression, mouth closed) looking at MC
    with dissolve

    u "Haha, sleepy?"

    scene v16s55_3c # FPP Same angle as 3. Lindsey (neutral expression, mouth open) looking at MC
    with dissolve

    li "I really need a nap. I could honestly fall asleep right here on this desk."

    scene v16s55_3b
    with dissolve

    u "Are you sure you're ready for our interview prep?"

    scene v16s55_3c
    with dissolve

    li "Yeah, I'll be okay. I'll get some extra strong coffee after this."

    scene v16s55_3d # FPP Same angle as 3. Lindsey (slight smile, mouth open) looking at MC
    with dissolve

    li "About a gallon should get me through the day."

    scene v16s55_3e # FPP Same angle as 3. Lindsey (slight smile, mouth closed) looking at MC
    with dissolve

    u "Haha, okay. If you're sure."

    scene v16s55_3d
    with dissolve

    li "Totally. Let's not overthink this. It should be pretty straight forward, so just ask me a couple of questions."

    # -We enter a UI showing three questions. The player can select two (drag and drop?). 
    # The three questions are: Can you say three positive things about your opponent? What is the most important quality of a good president? What was your last random act of kindness?-
    # I DON'T KNOW HOW TO CODE A DRAG-AND-DROP MENU. NEXT SCENE IS JUST MY IDEA FOR THE LAYOUT OF THE UI
    # scene v16s55_4 # FPP View of notebook on the table. Questions are on the left page, and place to drag them on the right
    # with dissolve

    # Implemented using the menu system 

    while len(v16s55_lindsey_question_set) < 2:
        menu:
            "Can you say three positive things about your opponent?" if "three_positives" not in v16s55_lindsey_question_set: 
                $ v16s55_lindsey_question_set.add("three_positives")

            "What is the most important quality of a good president?" if "important_quality" not in v16s55_lindsey_question_set:
                $ v16s55_lindsey_question_set.add("important_quality")

            "What was your last random act of kindness?" if "random_kindness" not in v16s55_lindsey_question_set:
                $ v16s55_lindsey_question_set.add("random_kindness")
                
    #-We exit the UI when the player has confirmed their selections-

    scene v16s55_3b
    with dissolve

    u "Okay, are you ready?"

    scene v16s55_3d
    with dissolve

    li "Fire away."

    # THE THREE 'IF' STATEMENTS USE PLACEHOLDER VARIABLES. THIS SECTION WILL LIKELY NEED TO BE CHANGED BASED ON IMPLIMENTATION OF DRAG-AND-DROP MENU
    if "three_positives" in v16s55_lindsey_question_set: # -if Can you say three positive things about your opponent? [Checkpoint 1.1]
        scene v16s55_3e
        with dissolve

        u "Tell me three positive things about your campaign opponent."

        scene v16s55_3c
        with dissolve

        li "Shit. Really?"

        scene v16s55_3b
        with dissolve

        u "Haha, yeah."

        scene v16s55_3d
        with dissolve

        li "Um... Well, she's blonde. And as we all know, blondes are awesome. *Chuckles*"

        scene v16s55_3f # FPP Same angle as 3. Lindsey (neutral expression, mouth open) looking up and to the side, like she's thinking
        with dissolve

        li "Um..."

        scene v16s55_3d
        with dissolve

        li "And I mean, it goes without saying really, but she really does have amazing boobs."

        scene v16s55_3e
        with dissolve

        menu:
            "Sounds great":
                $ v16s55_lindsey_followup_question_set.add("sounds_great")
                $ add_point(KCT.TROUBLEMAKER)

                scene v16s55_3e
                #with dissolve

                u "Can't argue with that. "

                scene v16s55_3b
                with dissolve

                u "Just one more."

                scene v16s55_3c
                with dissolve

                li "Um... Oh, and I hear she's good at volleyball too. That's three things."

                scene v16s55_3d ### check if 3d corresponds to mouth speaking
                with dissolve
                
                u "Great job."
            
            "Make a suggestion":
                $ v16s55_lindsey_followup_question_set.add("make_suggestion")

                scene v16s55_3e
                #with dissolve

                u "Haha, anything that isn't about her physical appearance?"

                scene v16s55_3b
                with dissolve

                li "..."

                scene v16s55_3c
                with dissolve

                li "I guess you could say she doesn't give up easily?"

                scene v16s55_3b
                with dissolve

                u "Go on."

                scene v16s55_3d
                with dissolve

                li "I mean, I'm destroying her campaign at the moment and yet she's still going, bless her."

                scene v16s55_3g # FPP Same angle as 3. Lindsey (wide, wicked grin, mouth closed) looking at MC
                with dissolve

                u "Haha, okay. Great compliment, but maybe leave out that second part. "

                scene v16s55_3e
                with dissolve

                u "You might sound a little arrogant saying you're 'destroying' her campaign..."

                scene v16s55_3d
                with dissolve

                li "Damn, do I really need to be that careful with my words?"

                scene v16s55_3e
                with dissolve

                u "Yeah, I think so. It needs to come across like a healthy rivalry between friends."

                u "If you need to, just pretend like she's your favorite person ever and make up good things about her."

                scene v16s55_3d
                with dissolve

                li "Ha... Like what?"

                scene v16s55_3e
                with dissolve

                u "Like, she's a great sorority sister. You can keep it vague like that."

                scene v16s55_3d
                with dissolve

                li "Okay, so pay her a vague compliment?"

                scene v16s55_3e
                with dissolve

                u "Yeah, and then move along quickly to the next one. That way you control the interview."

                scene v16s55_3d
                with dissolve

                li "Okay, got it. Easy enough."

    # [End of Checkpoint 1.1]

    elif "important_quality" in v16s55_lindsey_question_set: # -if What is the most important quality of a good president? [Checkpoint 1.2]
        scene v16s55_3e
        with dissolve

        u "What's the most important quality a president needs to have?"

        scene v16s55_3d
        with dissolve

        li "Ooh, that's a tricky question. Only one?"

        scene v16s55_3e
        with dissolve

        u "Just one. Choose wisely."

        scene v16s55_3f
        with dissolve

        li "Hmm..."

        scene v16s55_3c
        with dissolve

        li "I think a good president should be able to earn the loyalty of all of her sisters, you know, to keep everyone happy."

        scene v16s55_3b
        with dissolve

        menu:
            "That'll do":
                $ v16s55_lindsey_followup_question_set.add("thatll_do")

                u "Yeah, short but sweet. That'll do."

                scene v16s55_3c
                with dissolve

                li "Are you sure that's enough?"

                scene v16s55_3e
                with dissolve

                u "It was a good answer. Let's move on."

            "Expand on that":
                $ v16s55_lindsey_followup_question_set.add("expand")

                u "Okay, a little vague. What are you saying there? People skills?"

                scene v16s55_3d
                with dissolve

                li "Yeah, people skills. So, you can manipulate effectively, haha."

                scene v16s55_3e
                with dissolve

                u "Haha, okay, definitely don't want to use the word manipulate in the interview."

                scene v16s55_3d
                with dissolve

                li "No, of course not, duh. *Laughs*"

                scene v16s55_3e
                with dissolve

                u "You could also say an effective communicator."

                scene v16s55_3d
                with dissolve

                li "Ooh, I like that. Yeah, I'll use that one. Effective communicator."

    # [End of Checkpoint 1.2]
    
    if "random_kindness" in v16s55_lindsey_question_set: # -if What was your last random act of kindness? [Checkpoint 1.3]
        scene v16s55_3e
        with dissolve

        u "What was your last random act of kindness?"

        scene v16s55_3f
        with dissolve

        li "Um..."

        scene v16s55_3d
        with dissolve

        li "Oh! I donated money to the dog shelter!"

        # -if mc didn't go on a date with aubrey and gave a full donation to lindsey
        if not v16s25a_date_with_aubrey and v16s26_lindsey_donation_money == 50: # TODO: Variables 
            scene v16s55_3e
            with dissolve

            u "Which was really helpful, by the way. Autumn says thank you."

        # -if MC spent some of Lindsey's money
        elif v16s26_lindsey_donation_money > 0 and v16s26_lindsey_donation_money < 50: # TODO: Variable
            scene v16s55_3e
            with dissolve

            u "(Well, you donated a little less than you think...)"

        # -if MC spent all Lindsey's money and mc DID NOT post on Kiwii about the dog shelter
        elif v16s26_lindsey_donation_money == 0 and not v16s52_mc_dogshelter_kiwii_post: # TODO: PLACEHOLDER VARIABLE
            scene v16s55_3e
            with dissolve

            u "(Well, at least you think you did.)"

        # -if MC spent all Lindsey's money and MC DID post on Kiwii about the dog shelter
        elif v16s26_lindsey_donation_money == 0 and v16s52_mc_dogshelter_kiwii_post: # TODO: PLACEHOLDER VARIABLES
            scene v16s55_3c
            with dissolve 

            li "Or, I wanted to ask you about that. Autumn replied to my comment and asked about the donation...?"

            scene v16s55_3b
            with dissolve

            u "(Shit...)"

            u "Uh, yeah. It actually reminded me. I gave it to her once I saw your comment."

            scene v16s55_3d
            with dissolve

            li "Oh, haha. Good thing I reminded you then!"

            scene v16s55_3e
            with dissolve

            u "Yeah... (Phew.)"

        # -Regardless of MC spending her money-
        menu:
            "That's good to mention":
                $ v16s55_lindsey_followup_question_set.add("thats_good")
                $ add_point(KCT.BOYFRIEND)

                scene v16s55_3e
                with dissolve

                u "Nice. Who wouldn't like you after hearing that?"

                scene v16s55_3d
                with dissolve

                li "Haha, exactly! I've got this interview in the bag. Pfft."

                scene v16s55_3g
                with dissolve

                u "I'm loving that confidence, haha."

            "Ask her why":
                $ v16s55_lindsey_followup_question_set.add("ask_why")

                scene v16s55_3e
                with dissolve

                u "And why did you do that?"

                scene v16s55_3d
                with dissolve

                li "It's for a good cause. I donate to charity whenever I can."

                scene v16s55_3e
                with dissolve

                u "Perfect! Definitely say that."

                u "It makes you sound like an awesome person, someone who's really kind."

                scene v16s55_3d
                with dissolve

                li "I am an awesome person who's really kind!"

                scene v16s55_3e
                with dissolve

                u "Haha, I know, but... Hammer it home, hard, just don't sound too narcissistic."

                u "We need to spell it out for the slow ones in the back who haven't seen just how awesome you really are yet."

                scene v16s55_3d
                with dissolve

                li "*Laughs* Okay. I got it."

    # [End of Checkpoint 1.3] # -Regardless of all the question choices-
    scene v16s55_3c
    with dissolve

    li "Is that everything?"

    scene v16s55_3b
    with dissolve

    u "Yeah, you only asked for a couple, so we can stop there."

    scene v16s55_3a
    with dissolve

    li "Ugh, good. I'm exhausted. I think I did fine, no?"

    scene v16s55_3b
    with dissolve

    u "Yeah. We just need to talk about the person that's actually interviewing you now."

    scene v16s55_3c
    with dissolve

    li "Oh, okay, sure."

    # -if Lindsey is being interviewed by Elijah
    if v16_lindsey_elijah:
        scene v16s55_3b
        with dissolve

        u "The thing with Elijah is he might want to trip you up in order to get a controversial story, so be careful."

        scene v16s55_3h # FPP Same angle as 3. Lindsey (biting her lip in thought, mouth closed) leaning back in her seat, looking at MC
        with dissolve

        u "Just make sure you don't get pulled into ranting about Chloe or sounding like you have a big ego."

    # -if Lindsey is being interviewed by Riley
    elif v16_lindsey_newspaper:
        scene v16s55_3b
        with dissolve

        u "We know Riley much better than Elijah. So just be honest with her. Don't embellish the truth."

        scene v16s55_3h
        with dissolve

        u "And keep the discussion around yourself and how you'd be a strong president instead of criticizing Chloe."

    scene v16s55_3c
    with dissolve

    li "Right. I think I've got it all, it's just a lot at once."

    scene v16s55_3b
    with dissolve

    u "Well..."

    menu:
        "More advice": # -if More advice [Checkpoint 1.4]
            $ v16s55_lindsey_followup_question_set.add("more_advice")
            $ add_point(KCT.BOYFRIEND)

            u "The main thing is to keep control of your emotions. Don't just say the first thing that comes into your head. Think about it first."

            scene v16s55_3h
            with dissolve

            u "Don't worry if you want to think for a whole minute before answering. It's better than saying something you'll regret."

            if v16_lindsey_elijah: # -if being interviewed by Elijah
                u "And if all else fails, try flirting with him, but keep it subtle. Just give him a little bit of attention and he'll be putty in your hands."

            elif v16_lindsey_newspaper: # -if being interviewed by Riley
                u "I know Riley is treating her role seriously, so just make sure you're professional and it should go well. Even if she does crack a little joke, don't get over-friendly in the interview."

                u "Still, a few well-placed compliments will help too."

            scene v16s55_3d
            with dissolve

            li "Got it! That's great advice, [name]!"

        # [End of Checkpoint 1.4]
        
        "Let's finish up": # -if Let's finish up [Checkpoint 1.5]
            $ v16s55_lindsey_followup_question_set.add("finish_up")
            
            scene v16s55_3e
            with dissolve

            u "Other than that, I think we're good to go!"

            scene v16s55_3d
            with dissolve

            li "I hope the interview goes as smooth as this prep session, haha."

            scene v16s55_3e
            with dissolve

            u "Of course! You're going to do great."

    # [End of Checkpoint 1.5]
    scene v16s55_3e
    with dissolve

    u "That's everything I can think of."

    scene v16s55_3d
    with dissolve

    li "Okay, great. Thank you for prepping me!"

    scene v16s55_5 # TPP Lindsey leans across the table to give MC a hug
    with dissolve

    pause 0.75

    scene v16s55_3e
    with dissolve

    u "Of course. Do you feel ready for it?"

    scene v16s55_3d
    with dissolve

    li "As ready as I'll ever be, haha."

    scene v16s55_3e
    with dissolve

    u "I'll see you a bit later then for the main event."

    scene v16s55_6 # TPP MC and Lindsey both getting out of their seats to stand up
    with dissolve

    pause 0.75

    # -if LindseyRS
    if relationship.lindsey >= Relationship.FWB: 
        scene v16s55_7 # FPP Lindsey (sexy smile, mouth open), now standing, looking at MC
        with dissolve

        li "Okay... Wait! Can I have a kiss...?"

        scene v16s55_7a # Same angle as 3. FPP Lindsey (sexy smile, mouth closed), now standing, looking at MC
        with dissolve

        menu:
            "Absolutely":
                $ add_point(KCT.BOYFRIEND)

                play sound "sounds/kiss.mp3"

                u "Ha, absolutely. Come here."

                scene v16s55_8 # TPP MC pulling Lindsey in for a kiss
                with dissolve

                pause 0.75

                scene v16s55_7
                with dissolve

                li "Mmm... My favorite."

            "I have bad breath":
                $ add_point(KCT.TROUBLEMAKER)
                
                u "My breath smells pretty bad right now... *Chuckles* I'm sorry."

                scene v16s55_7b # Same angle as 3. FPP Lindsey (scrunching her nose in disgust but smiling, mouth open), now standing, looking at MC
                with dissolve

                li "Oh, ew! Ha, okay. Bye then."

    else: # -if not LindseyRS
        scene v16s55_7c # FPP Same angle as 3. Lindsey (small smile, mouth open), now standing, looking at MC
        with dissolve

        li "Okay, yeah. See you soon."

    scene v16s55_7d # FPP Same angle as 3. Lindsey (small smile, mouth closed), now standing, looking at MC
    with dissolve

    u "Later, Linds."

    scene v16s55_9 # TPP Show MC leaving the library
    with dissolve

    pause 0.75

    if joinwolves: # -if Wolves, transition to Scene 56-
        jump v16s56

    else: # -if Apes, transition to Scene 57-
        jump v16s57