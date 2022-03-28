# SCENE 78: Opera with Ms Rose
# Locations: Opera house
# Characters: MC (Outfit: Fancy), MS ROSE (Outfit: Nice dress), Old Woman, Tenor, Soprano
# Time: Friday night


default v16s78_probably_not = False

label v16s78: # 78) At the Opera with Ms Rose
    scene v16s78_1 # TPP Show MC entering the foyer of the Opera house
    with dissolve

    pause 0.75


    scene v16s78_2 # FPP Show Ms Rose (slight smile, mouth closed) to one side of the foyer. She is wearing a very nice dress and looking at MC
    with dissolve

    pause 0.75


    scene v16s78_3 # TPP As MC reaches Ms Rose, he takes her hand and they share a quick kiss
    with dissolve

    pause 0.75


    scene v16s78_4 # FPP Show Ms Rose (slight smile, mouth closed) close to MC, looking at him
    with dissolve

    menu:
        "Compliment her":
            $ addPoint("bf")

            u "You're looking absolutely stunning tonight."


            scene v16s78_4a # FPP Same angle as 4, Ms Rose (slight smile, mouth open) looking at MC
            with dissolve

            ro "Why, thank you... You look very handsome, yourself."


            scene v16s78_5 # TPP Show MC and Ms Rose kissing again, a proper kiss this time, she has her arms around his neck, and he has his arms around her back
            with dissolve

            pause 0.75


            scene v16s78_4
            with dissolve

            u "(That one's from Ryan, haha.)"


            scene v16s78_4a
            with dissolve

            ro "You clean up nice."


        "Mention the long ride":

            u "That was a longer ride than I had expected, haha."


            scene v16s78_4b # FPP Same angle as 4, Ms Rose (slight smile, mouth open) looking around at the opera house around them
            with dissolve

            ro "Yeah, they needed more land to build it this big, so they had to make it a little further out of town."


            scene v16s78_4a
            with dissolve

            ro "It's an incredible building."


            scene v16s78_4
            with dissolve

            u "Yeah, it's breathtaking."


            scene v16s78_4a
            with dissolve

            ro "Wait until you see the inside."


    ro "Let's go up to our private balcony."


    scene v16s78_4
    with dissolve

    u "Haha, I feel fancy when you say that."


    scene v16s78_4c # FPP Same angle as 4, Ms Rose (laughing, mouth open) looking at MC
    with dissolve

    ro "We are fancy! Well, for tonight at least *Laughs*"


    scene v16s78_6 # TPP MC and Ms Rose walking together toward the auditorium doors, smiling and holding hands
    with dissolve

    pause 0.75


    scene v16s78_7 # FPP Old woman (smiling, mouth open) looking at MC and Ms Rose
    with dissolve

    OLD WOMAN "Oh, that's lovely to see."


    scene v16s78_8 # FPP Ms Rose (slight smile, mouth open) looking at the old woman
    with dissolve

    ro "I'm sorry?"


    scene v16s78_7
    with dissolve

    OLD WOMAN "Taking your son out to the opera. My daughter and I used to come together, too."


    scene v16s78_7a # FPP Same angle as 7. Old woman (smiling, mouth closed) looking at MC and Ms Rose
    with dissolve

    u "(Oh... Fuck. She thinks Lorraine is my mother?!)"


    scene v16s78_8a # FPP Same angle as 8. Ms Rose (shocked expression, mouth open) looking at the old woman
    with dissolve

    ro "He's not my-"


    scene v16s78_8
    with dissolve

    OLD WOMAN "I wish I could get my son to come with me. You're very lucky."


    scene v16s78_9 # TPP Old woman (smiling, mouth open) waving to Ms Rose and MC and starting to walk away
    with dissolve

    OLD WOMAN "Have a nice evening!"


    scene v16s78_8a
    with dissolve

    ro "Mhmm, thanks. You too."


    scene v16s78_10 # TPP Ms Rose (neutral expression, mouth closed) and MC (mouth closed) walking again
    with dissolve

    u "(Well, this is awkward... Should I say something?)"


    menu:
        "Talk about it":
            scene v16s78_11 # FPP Ms Rose (neutral expression, mouth closed) looking ahead as she walks (not at MC)
            with dissolve

            u "She must need glasses... Ha."


            scene v16s78_11a # FPP Same angle as 11. Ms Rose (fake smile, sad expression, mouth open) still not looking at MC
            with dissolve

            ro "Yeah, maybe."


            scene v16s78_11
            with dissolve

            u "(Fuck off Grandma, you've upset my date!)"


            scene v16s78_12 # TPP Show MC (concerned, mouth open) putting  a hand on Ms Rose's (slight smile, mouth closed) waist as they walk, he is looking at her
            with dissolve

            u "Hey, all good?"


            scene v16s78_11b # FPP Same angle as 11. Ms Rose (small, real smile, mouth open) looking at MC
            with dissolve

            ro "I'm okay, yeah. It was just a bit of a shock, I guess. Hearing someone say that."


        "Say nothing":
            scene v16s78_11
            with dissolve

            u "(Sometimes, it's best to keep your mouth shut. Shame nobody told that old lady before she came here tonight...)"


    scene v16s78_13 # TPP Show MC and Ms Rose arriving at the private balcony
    with dissolve

    pause 0.75


    scene v16s78_14 # TPP Show Ms Rose sitting down in the private balcony, MC beginning to sit down next to her. It is clear he waited for her to sit before he sat
    with dissolve

    pause 0.75


    scene v16s78_15 # FPP View of the stage, lights dim and only the stage is illuminated
    with dissolve

    pause 0.75


    scene v16s78_15a # FPP Same angle as 15. Tenor is on stage, wearing a suit, with a big mustache. His mouth is open wide and his arm is out as he begins to sing
    with dissolve

    TENOR "*Singing in Italian*"


    menu:
        "What's he saying?":
            scene v16s78_16 # TPP MC (mouth open) leaning in close to Ms Rose to ask her a question in a whisper
            with dissolve

            u "What's he saying? What language is that?"


            scene v16s78_17 # FPP Ms Rose (smiling, mouth open) very close, whispering distance, she is still looking at the stage
            with dissolve

            ro "Italian. I can speak a little, but I have no clue what he's saying. *Laughs*"


            scene v16s78_17a # FPP Same angle as 17. Ms Rose (smiling, mouth closed) still looking toward the stage
            with dissolve

            u "I think I managed to pick up \"spaghetti\" and \"pizza\"."


            scene v16s78_17
            with dissolve

            ro "I'm not sure if he'd be singing about Italian cuisine... *Chuckles* But, then again, who knows."


            scene v16s78_17a
            with dissolve

            u "*Laughs* True."


            scene v16s78_17
            with dissolve

            ro "But, first lesson, the opera isn't about understanding what they're saying."


            scene v16s78_17b # FPP Same angle as 17. Ms Rose (smiling, mouth open) looking toward MC
            with dissolve

            ro "It's about enjoying it in the moment, with the beautiful architecture, and other open minds."


            scene v16s78_17
            with dissolve

            ro "Let his voice just... Completely wash over you."


            scene v16s78_17a
            with dissolve

            u "Hmm, okay... I can do that, I think."

            u "As long as you give me another kiss."


            scene v16s78_18 # TPP MC and Ms Rose, sitting in the private balcony, share a kiss
            with dissolve

            pause 0.75


            scene v16s78_17c # FPP Same angle as 17. Ms Rose (smiling, mouth closed) looking toward MC
            with dissolve

            u "I love how passionate you are about this."


            scene v16s78_17d # FPP Same angle as 17. Ms Rose (big smile, blushing, mouth open) looking down a bit in embarrassment
            with dissolve

            ro "Thank you."


            scene v16s78_15a
            with dissolve

            TENOR "*Singing in Italian*"

        
        "Don't ask":

            u "(It probably isn't good opera etiquette to begin a conversation while someone's singing.)"


    scene v16s78_15b # FPP Same angle as 15. Tenor is still on stage, mouth closed, Soprano is entering with a spotlight on her, mouth open to sing. She is wearing an elegant ball gown
    with dissolve

    SOPRANO "*Singing in Italian*"


    scene v16s78_15c # FPP Same angle as 15. Tenor and Soprano are close together in the center of the stage half facing each other, Tenor is singing, Soprano has her mouth closed
    with dissolve

    TENOR "*Singing in Italian*"


    scene v16s78_19 # FPP Show Ms Rose looking out into the audience
    with dissolve

    pause 0.75


    scene v16s78_20 # FPP Shot of the audience from the balcony. Have one or two attractive couples clearly visible, about Ms Rose's age
    with dissolve

    pause 0.75


    scene v16s78_21 # FPP Another shot of the audience, a little closer on a couple Ms. Rose's age, centered in the frame
    with dissolve

    ro "*Sighs*"


    scene v16s78_22 # FPP Ms Rose (sad expression, mouth open) looking out into the audience
    with dissolve

    ro "[name]..."


    scene v16s78_22a # FPP Same angle as 22. Ms Rose (sad expression, mouth closed) looking out into the audience
    with dissolve

    u "Yeah?"


    scene v16s78_22
    with dissolve

    ro "What that lady said earlier... It's true, isn't it?"


    scene v16s78_22a
    with dissolve

    u "What do you mean? You're definitely not my mother, haha."


    scene v16s78_22
    with dissolve

    ro "No, silly... About our age difference."


    scene v16s78_22b # FPP Same angle as 22. Ms Rose (sad expression, mouth open) looking toward MC, but down
    with dissolve

    ro "I guess that's just how we look to other people. I didn't realize I looked that old."


    scene v16s78_22a
    with dissolve

    u "Lorraine, stop it."


    scene v16s78_22
    with dissolve

    ro "You see all the other couples here... They don't have the age gap like we do."


    scene v16s78_22b
    with dissolve

    ro "And I'm your teacher..."


    scene v16s78_22
    with dissolve

    ro "Should we even be doing this?"


    scene v16s78_22a
    with dissolve

    menu:
        "If we want to":
            $ addPoint("tm")

            u "If we want to, then yes."

            u "Lorraine, look at me."


            scene v16s78_22c # FPP Same angle as 22. Ms Rose (sad expression, mouth closed) looking directly at MC
            with dissolve

            u "Forget what that lady said."

            u "Stop paying attention to other couples who are the same age. What the hell does that matter?"


            scene v16s78_20
            with dissolve

            u "We don't even know if they're happy or not."


            scene v16s78_22c
            with dissolve

            u "You just need to ask yourself if you're happy being with me. I know I'm happy being with you."


            scene v16s78_22d # FPP Same angle as 22. Ms Rose (more neutral expression, mouth closed) looking at MC, her head tilted a bit as if curious
            with dissolve

            u "If we enjoy our time together, then that's all that should matter."


            scene v16s78_22e # FPP Same angle as 22. Ms Rose (slight smile, mouth closed) looking at MC
            with dissolve

            pause 0.75


            scene v16s78_22f # FPP Same angle as 22. Ms Rose (slight smile, mouth open) looking at MC
            with dissolve

            ro "Somehow, you always know exactly what to say."


            scene v16s78_23 # TPP Ms Rose takes MC's chin into her hand and kisses him
            with dissolve

            pause 0.75


            scene v16s78_24 # TPP Front view of MC and Ms Rose, both looking forward and smiling slightly, Ms Rose holding MC's hand in her lap
            with dissolve

            pause 0.75


        "Probably not":
            $ v16s78_probably_not = True

            u "Honestly? Probably not. We're far from being an average couple, haha."

            u "But the only thing that matters is I like being with you."


            scene v16s78_22g # FPP Same angle as 22. Ms Rose (slightly angry, mouth closed) with her arms crossed over her chest, looking at the show
            with dissolve

            u "(Wha- How did I- What did I say?!)"

            u "Lorraine..."


            scene v16s78_22h # FPP Same angle as 22. Ms Rose (slightly angry, lips pursed to make a "shoosh" noise) with her arms crossed over her chest, looking at the show
            with dissolve

            ro "Shhh..."


            scene v16s78_22g
            with dissolve

            u "*Sighs*"


    scene v16s78_25 # TPP Show MC and Ms Rose returning to the foyer, moving to the side of the room (where they were at the beginning of the scene) to talk
    with fade

    pause 0.75


    if v16s78_probably_not: # -if Probably not
        scene v16s78_4d # FPP Same angle as 4. Ms Rose (neutral expression, mouth open) looking at MC
        with dissolve

        ro "Well, thanks for coming. I'm going to head home now."


        scene v16s78_4e # FPP Same angle as 4. Ms Rose (neutral expression, mouth closed) looking at MC
        with dissolve

        u "Oh, okay... You don't want me to come?"


        scene v16s78_4d
        with dissolve

        ro "Um, no, not tonight. I just want to be alone so I can think about things."


        scene v16s78_4e
        with dissolve

        u "Okay, is everything alright? I'm sorry if I said something off."


        scene v16s78_4d
        with dissolve

        ro "No, no, it's not about what you said."

        ro "It's just the first time I've ever really thought about our age difference, and I'm worried that this relationship isn't a good idea."


        scene v16s78_4e
        with dissolve

        u "Oh. Well, Lorraine, I like you. And I know you like being with me. What more do we need?"


        scene v16s78_4d
        with dissolve

        ro "I'm sorry, [name]. Just give me some time to think, okay? We'll talk again soon."


        scene v16s78_4e
        with dissolve

        u "*Scoffs* Yeah. Okay."

        u "(To be honest, this whole relationship has been nothing but fear and arguing... I'm not sure if it's a good idea anymore either. *Sighs*)"


        scene v16s78_26 # TPP Show Ms Rose (upset expression, mouth closed, if visible) walking away toward the exit of the Opera House.
        with dissolve

        pause 0.75

        
        jump v16s80 # -Transition to Scene 80-


    else: # -if MC chose If we want to
        scene v16s78_4a
        with dissolve

        ro "That was amazing! Their voices were incredible tonight, oh my..."


        scene v16s78_4
        with dissolve

        u "Honestly, that was a fun experience. I'm glad I lost my opera virginity with you tonight."


        scene v16s78_4c
        with dissolve

        ro "*Laughs* I'm honored to be your first."


        scene v16s78_4
        with dissolve

        u "So, what are we doing now?"


        scene v16s78_4a
        with dissolve

        ro "Um, I was thinking ice cream? There's a place nearby if you're up for a walk."


        if (v16s27_mc_baby_duty_night == 4 or v16s27_mc_baby_duty_night == 0x40) # -if MC is on baby duty alone or with partner
            scene v16s78_27 # TPP Show MC (neutral expression, mouth open) checking his phone
            with dissolve

            u "Ah, damn. I wish I could, but I have to get home. I have baby duty tonight."


            scene v16s78_4a
            with dissolve

            ro "Oh, you're doing the baby assignment this week! Are you enjoying it?"


            scene v16s78_4
            with dissolve

            u "Haha, I think I'll enjoy it more once it's over."


            scene v16s78_4a
            with dissolve

            ro "Ha, I was the same way. Hence why I have a stepdaughter, and not any biological. *Chuckles*"


            scene v16s78_4
            with dissolve

            u "You don't want any kids?"


            scene v16s78_4a
            with dissolve

            ro "Haha, why? Are you wanting some?"


            scene v16s78_4
            with dissolve

            u "Oh, I was just-"


            scene v16s78_4a
            with dissolve

            ro "*Giggles* I'm kidding. Another conversation for a different day."

            ro "You should get going. Thanks for tonight."


            scene v16s78_4
            with dissolve

            u "Of course. I had fun."


            scene v16s78_5
            with dissolve

            pause 0.75

        
            scene v16s78_28 # TPP Show MC (slight smile, if visible) walking away, Ms Rose (slight smile, mouth closed) watching him go
            with dissolve

            pause 0.75

            
            jump v16s80 # -Transition to Scene 80-

        
        else: # -if MC is not on baby duty
            scene v16s78_4
            with dissolve

            u "I'm up for ice cream, and if that includes a walk then... *Sighs* Let's go..."


            scene v16s78_4a
            with dissolve

            ro "Haha, so whiney..."


            scene v16s78_29 # TPP Show MC and Ms Rose leaving the Opera House, holding hands. Both smiling with mouths closed
            with dissolve

            
            jump v16s79 # -Transition to Scene 79-