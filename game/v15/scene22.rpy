# SCENE 22: Chloe vs Dean
# Locations: School Hallway/Deans Office
# Characters: CHLOE (Outfit: 3), MC (Outfit: 9), DEAN (Outfit: 1)
# Time: Morning
# Render Count: 8 Unique 71 Total

label v15s22:
    $ v15s22_kiwiiPost1= KiwiiPost(chloe, "v15s22Kiwii1", "Making changes for my girls!", numberLikes=515)
    $ v15s22_kiwiiPost1.newComment(aubrey, "Ooooh, what are you up to?", numberLikes=renpy.random.randint(160, 460))
    $ v15s22_kiwiiPost1.newComment(grayson, "Hanging out with the Dean now? That's one way to get votes I guess...", numberLikes=renpy.random.randint(160, 460))
    $ v15s22_kiwiiPost1.newComment(chris, "Looks like the President of the Chicks is making some big moves, huh?", numberLikes=renpy.random.randint(160, 460))
    $ v15s22_kiwiiPost1.newComment(chloe, "Trying to! Also, fuck off Gray :)", numberLikes=renpy.random.randint(160, 460))

    if False: # for Lint
        scene v15s22Kiwii1 # smile next the dean's office door

    scene v15s22_1 # TPP. Chloe and MC are walking in the school hallway, slight smiles, mouths are closed, looking forward
    with dissolve

    pause 0.75

    if v15s21_meeting_points >= 1:
        if v15_chloe_mrleesupport:
            scene v15s22_2 # FPP. Show only Chloe looking at mc, no expression, mouth is open, just show a hallway wall in the background no decorations, windows, or doors if possible
            with dissolve

            cl "*Sighs* It wasn't perfect but at least we have Mr. Lee's signature."

            scene v15s22_2a # FPP. same as v15s22_2 Chloe's mouth is closed, still looking at Mc, still no expression
            with dissolve

            u "We knew he would be a hard guy to impress."

            scene v15s22_2
            with dissolve

            cl "Yeah, I'm so glad he's on our side."

            cl "But giving up my scholarship is going to make things really stressful."

            scene v15s22_2a
            with dissolve

            menu:
                "Be supportive":
                    $ add_point(KCT.BRO)
                    
                    if chloe.relationship.value >= Relationship.FWB.value:
                        $ add_point(KCT.BOYFRIEND)

                    scene v15s22_2a
                    with dissolve

                    u "It'll be okay. I'm sure everything will work out for the best."

                    scene v15s22_2
                    with dissolve

                    cl "I really hope so."

                "Be brutally honest":
                    $ add_point(KCT.TROUBLEMAKER)
                    
                    if chloe.relationship.value >= Relationship.FWB.value:
                        $ add_point(KCT.BRO)

                    scene v15s22_2a
                    with dissolve

                    u "You'll just have to get a part-time job or something."

                    scene v15s22_2
                    with dissolve

                    cl "*Sighs* Yeah, I guess so."

        elif v15_seduce_ms_rose or v15_threaten_ms_rose:
            scene v15s22_2b # FPP. same as v15s22_2 Chloe has a full smile, mouth is still open, still looking at mc
            with dissolve

            cl "Wow! Ms. Rose is supporting the whole thing, so I get to keep my scholarship as well!"

            scene v15s22_2c # FPP. same as v15s22_2b Chloe has a slight smile, mouth is still open, still looking at mc
            with dissolve

            cl "Whatever you said to her, it worked!"

            scene v15s22_2d # FPP. same as v15s22_2c Chloe's mouth is closed, still a slight smile, still looking at mc
            with dissolve

            menu:
                "Change the subject":
                    $ add_point(KCT.BRO)
                    
                    if chloe.relationship.value >= Relationship.FWB.value:
                        $ add_point(KCT.BOYFRIEND)

                    scene v15s22_2d
                    with dissolve

                    u "It's not over yet. We still need to impress the Dean."

                    scene v15s22_2b
                    with dissolve

                    cl "Yeah, you're right, we have to stay focused."

                    scene v15s22_2c
                    with dissolve

                    cl "Let's hope she's in a good mood."

                "Lie":
                    $ add_point(KCT.BRO)
                    
                    if chloe.relationship.value >= Relationship.FWB.value:
                        $ add_point(KCT.TROUBLEMAKER)

                    scene v15s22_2d
                    with dissolve

                    u "I just figured the Nora thing was playing on her mind. Thought it was best you left the room."

                    scene v15s22_2c
                    with dissolve

                    cl "Ah, okay. That makes sense."

        else:
            scene v15s22_2
            with dissolve

            cl "*Sighs* I thought Ms. Rose would want to help me keep my scholarship. I don't know what I'm going to do if I lose that."

            scene v15s22_2a
            with dissolve

            u "We have her support for the reduced fees. That's something."

            scene v15s22_2
            with dissolve

            cl "Yeah, it's just stressful, you know?"

            scene v15s22_2a
            with dissolve

            menu:
                "Be supportive":
                    $ add_point(KCT.BRO)
                    
                    if chloe.relationship.value >= Relationship.FWB.value:
                        $ add_point(KCT.BOYFRIEND)

                    scene v15s22_2a
                    with dissolve

                    u "It'll be okay. I'm sure everything will work out for the best."

                    scene v15s22_2
                    with dissolve

                    cl "I really hope so."

                "Be brutally honest":
                    $ add_point(KCT.TROUBLEMAKER)
                    
                    if chloe.relationship.value >= Relationship.FWB.value:
                        $ add_point(KCT.BRO)

                    scene v15s22_2a
                    with dissolve

                    u "You'll just have to get a part-time job or something."

                    scene v15s22_2
                    with dissolve

                    cl "*Sighs* Yeah, I guess so."
            
    else:
        scene v15s22_2
        with dissolve

        cl "I can't believe we're going to the Dean without a signature. I thought we had a good case."

        scene v15s22_2a
        with dissolve

        menu:
            "Be supportive":
                $ add_point(KCT.BRO)
                
                if chloe.relationship.value >= Relationship.FWB.value:
                    $ add_point(KCT.BOYFRIEND)

                scene v15s22_2a
                with dissolve

                u "You can't win them all, Chloe."

                scene v15s22_2
                with dissolve

                cl "We really needed a signature."

                scene v15s22_2a
                with dissolve

                u "I know, but you have to stay positive. We still have a chance."

            "Be brutally honest":
                $ add_point(KCT.TROUBLEMAKER)
                
                if chloe.relationship.value >= Relationship.FWB.value:
                    $ add_point(KCT.BRO)

                scene v15s22_2a
                with dissolve

                u "We were awful in there. I'm not surprised."

                scene v15s22_2
                with dissolve

                cl "Still, they could have signed. They don't have anything to lose. I could lose everything."

                scene v15s22_2a
                with dissolve

                u "They could have signed, but they didn't, and that's that."
        
    scene v15s22_2a
    with dissolve

    u "Look, we're almost at the Dean's office now."

    scene v15s22_3 # TPP. Show Chloe and MC standing beside the Dean's office door, slight smiles, mouths are closed, Chloe looking at the door, Mc looking at Chloe
    with dissolve

    pause 0.75

    scene v15s22_2e # FPP. same as v15s22_2 Show Chloe in front of the Deans office door, still no expression, still looking at Mc, mouth is still open
    with dissolve

    cl "Okay, so before we go in, we need to think about how we're going to approach the Dean."

    scene v15s22_2f # FPP. same as v15s22_2e Chloe's mouth is closed, still looking at mc, still no expression
    with dissolve

    u "She's basically a combination of Mr. Lee and Ms. Rose, isn't she?"

    scene v15s22_2e
    with dissolve

    cl "Well, yes and no. Here, take a look at my notes."

    # -The UI pops up showing Dean Harrison's character brief. MC exits whenever-
    show screen v15_teacher_brief("dean")

    scene v15s22_2f 
    with dissolve

    pause 0.75

    scene v15s22_2e
    with dissolve

    cl "We need to convince her that our proposal benefits SVC."

    cl "SVC is always her priority. It's like she's married to this place."

    cl "But above all we need to show her respect. After all, what she says, goes."

    scene v15s22_2f
    with dissolve

    u "Understood."

    scene v15s22_2e
    with dissolve

    cl "And we aren't taking these notes with us. I don't want us to be distracted, and I don't want to risk pissing her off, so..."

    scene v15s22_2f
    with dissolve

    u "I'm ready."

    scene v15s22_2e
    with dissolve

    cl "Good."

    cl "*Deep breath* Okay, let's go."

    play sound "sounds/knock.mp3"

    scene v15s22_2g # FPP. same as v15s22_2f Chloe turns away from Mc and knocks on the Dean's door, still no expression, mouth is still closed
    with dissolve

    pause 0.75

    scene v15s22_2h # FPP. same as v15s22_2g Chloe is no longer knocking on the door, still no expression, mouth is still closed
    with dissolve

    de "Come in."

    pause 0.75

    scene v15s22_4 # TPP. MC and Chloe are standing in front of the Dean's desk, Chloe has a slight smile, mouth is closed, Mc has a slight smile mouth is closed, The Dean is sat behind her desk, writing on a piece of paper, she is looking at her paperwork and not Chloe or Mc, no expression, mouth is closed, try to get the image as close as possible to avoid showing an excess amount of the office
    with dissolve

    pause 0.75

    if kct == "popular":
        $ v15s22_meeting_points += 1

    $ animated_value_percent = v15s21_meeting_points+5

    scene v15s22_4a # TPP. same as v15s22_4 The only difference is that Chloe's mouth is open, The dean does not look up at Chloe or Mc
    with dissolve

    cl "Hello, Dean Harrison. We're here for my meeting. Thank you for-"

    scene v15s22_4b # TPP. same as v15s22_4 The only difference is the Dean's mouth is open, she does not look up at Chloe or Mc
    with dissolve

    de "Just take a seat. I'll be with you in a moment."

    scene v15s22_4a
    with dissolve

    cl "Oh, okay."

    scene v15s22_4
    with dissolve

    menu:
        "Say hello to the Dean":
            #$ add_point(KCT.TROUBLEMAKER)

            scene v15s22_4c # TPP. same as v15s22_4 The only difference is Mc's mouth is open, The dean does not look up at Chloe or Mc
            with dissolve

            u "Hi, Dean Harrison."

            $ v15s22_meeting_points -= 1
            show screen teacher_conviction_bar((v15s22_meeting_points+5) * 100 / 13, "CONVINCE DEAN", "DEAN", "images/v15/conviction_bars/dean_background.webp")

            scene v15s22_4b
            with dissolve

            de "I said I'll be with you in a moment, [name]."

        "Just sit down": # (CORRECT CHOICE - ONE POINT)
            $ v15s22_meeting_points += 0
            show screen teacher_conviction_bar((v15s22_meeting_points+5) * 100 / 13, "CONVINCE DEAN", "DEAN", "images/v15/conviction_bars/dean_background.webp")

            #$ add_point(KCT.BRO)

            scene v15s22_4
            with dissolve

            u "(Better just do as she says. Don't want to disturb her while she's busy.)"

    scene v15s22_5 # TPP. MC and Chloe sit down on a couch, Mc sits on the left and Chloe sits on the right, slight smiles mouths are closed they are looking at each other, there is a comfortable looking chair sitting directly across from the couch where Mc and Chloe are sitting, a small end table is next to the comfortable chair, zoom in as much as possible to avoid having to show the dean or her desk in the render
    with dissolve

    pause 0.75

    scene v15s22_4d # TPP. same as v15s22_4 Chloe and Mc are no longer in this render, The dean has put down her pen and is looking in the direction of where Chloe and Mc are sitting on the couch, no expression, mouth is closed
    with dissolve

    pause 0.75

    scene v15s22_5a # TPP. same as v15s22_5 Mc and Chloe are now looking at the Dean still slight smiles mouths are still closed, The Dean is sitting down in the chair across from Chloe and Mc no expression mouth is closed looking at Mc and Chloe
    with dissolve

    pause 0.75

    scene v15s22_6 # FPP. Show only the Dean sitting on the Chair from render v15s22_5 no expression, all v15s22_6 renders The Dean will be sitting in this chair unless otherwise stated, looking at Chloe on the Deans left, mouth is open, make the angle hide the end table sitting next to her
    with dissolve

    de "Okay, so how can I help you both today?"

    scene v15s22_7 # FPP. Show only Chloe sitting on the couch from render v15s22_5, Mc is looking to his right at Chloe, Chloe has a slight smile, mouth is open
    with dissolve

    cl "It's about my proposal to reduce tuition fees for the Chicks."

    scene v15s22_7a # FPP. same as v15s22_7 Chloe holds out a piece of paper towards the Dean, still a slight smile, mouth is closed
    with dissolve
    
    pause 0.75

    if v15s21_meeting_points >= 1:
        if v15_chloe_mrleesupport:
            scene v15s22_7
            with dissolve

            cl "We have signed support from Mr. Lee."

            scene v15s22_6a # FPP. same as v15s22_6 The Dean is holding the paper Chloe handed her from render v15s22_7a slightly in front of her, still no expression, still looking at Chloe, mouth is still open
            with dissolve

            $ v15s22_meeting_points += 1
            show screen teacher_conviction_bar((v15s22_meeting_points+5) * 100 / 13, "CONVINCE DEAN", "DEAN", "images/v15/conviction_bars/mr_lee_background.webp")

            de "Mr. Lee? You must have been very convincing."

            de "I can't imagine Mr. Lee wanting to support something like this."

            scene v15s22_5b # TPP. same as v15s22_5a The Dean is sitting in the chair and looking at and placing a piece of paper on the end table next to her chair, still no expression, mouth is closed, Mc and Chloe are still sitting down on the couch looking at The Dean slight smiles mouths are closed
            with dissolve

            menu:
                "Explain why Mr. Lee signed": # (CORRECT CHOICE - ONE POINT)
                    #$ add_point(KCT.BRO)

                    scene v15s22_6b # FPP. same as v15s22_6 The Dean is looking at Mc, mouth is closed, still no expression
                    with dissolve

                    u "Mr. Lee felt that we have good intentions with this proposal and believed it would benefit SVC."

                    scene v15s22_6c # FPP. same as v15s22_6b The Dean has a slight smile, still looking at Mc, mouth is still open
                    with dissolve

                    $ v15s22_meeting_points += 1
                    show screen teacher_conviction_bar((v15s22_meeting_points+5) * 100 / 13, "CONVINCE DEAN", "DEAN", "images/v15/conviction_bars/dean_background.webp")

                    de "Well, I look forward to hearing from him how he came to that conclusion."

                    de "So now you're here to convince me."

                "Make a joke":
                    #$ add_point(KCT.TROUBLEMAKER)

                    scene v15s22_6b
                    with dissolve

                    u "He didn't. We faked his signature."

                    scene v15s22_7b # FPP. same as v15s22_7 Chloe has a shocked expression, looking at Mc, mouth is still open
                    with dissolve

                    cl "[name]!"

                    scene v15s22_7c # FPP. same as v15s22_7 Chloe has a worried expression, still looking at the Dean, mouth is still open
                    with dissolve

                    cl "I'm sorry, Dean Harrison."

                    scene v15s22_7d # FPP. same as v15s22_7c Chloe is looking at Mc, mouth is closed, still a worried expression
                    with dissolve

                    u "I'm only joking. Just thought I'd lighten the mood in here..."

                    scene v15s22_6b
                    with dissolve

                    u "He signed it, I promise."

                    scene v15s22_6c
                    with dissolve

                    de "You're quite the comedian, aren't you, [name]?"

                    scene v15s22_6d # FPP. same as v15s22_6c The Dean's mouth is closed, still looking at Mc, still a slight smile
                    with dissolve

                    u "Well-"

                    scene v15s22_6e # FPP. same as v15s22_6c The Dean has an annoyed expression, still looking at Mc, mouth is still open
                    with dissolve

                    $ v15s22_meeting_points -= 1
                    show screen teacher_conviction_bar((v15s22_meeting_points+5) * 100 / 13, "CONVINCE DEAN", "DEAN", "images/v15/conviction_bars/dean_background.webp")

                    de "I can assure you, nobody finds you funny."

                    scene v15s22_6f # FPP. same as v15s22_6e The Dean's mouth is closed, still looking at Mc, still an annoyed expression
                    with dissolve

                    u "...Sorry."

                    scene v15s22_6g # FPP. same as v15s22_6b The Dean's mouth is open, still no expression, still looking at Mc
                    with dissolve

                    de "All jokes aside, you must have impressed him."

                    de "So now you're here to convince me."

        else:
            scene v15s22_7
            with dissolve

            cl "We have signed support from Ms. Rose."

            scene v15s22_6h # FPP. same as v15s22_6 The Dean has a slight smile, still looking at Chloe, mouth is still open
            with dissolve

            $ v15s22_meeting_points += 1
            show screen teacher_conviction_bar((v15s22_meeting_points+5) * 100 / 13, "CONVINCE DEAN", "DEAN", "images/v15/conviction_bars/dean_background.webp")

            de "Oh, good. You've already convinced Ms. Rose."

            de "She only supports worthy causes, so that bodes well."

            scene v15s22_6i # FPP. same as v15s22_6h The Dean's mouth is closed, still looking at Chloe, still a slight smile
            with dissolve

            menu:
                "Explain why Ms. Rose signed": # (CORRECT CHOICE - ONE POINT)
                    #$ add_point(KCT.BRO)

                    scene v15s22_6d
                    with dissolve

                    u "Ms. Rose felt that not only was this a great proposal for the Chicks, but that it would benefit SVC overall."

                    scene v15s22_6c
                    with dissolve

                    $ v15s22_meeting_points += 1
                    show screen teacher_conviction_bar((v15s22_meeting_points+5) * 100 / 13, "CONVINCE DEAN", "DEAN", "images/v15/conviction_bars/dean_background.webp")

                    de "Did she? I'll be interested to hear from her how she arrived at that conclusion."

                    de "So now you're here to convince me."

                "Be funny":
                    #$ add_point(KCT.TROUBLEMAKER)

                    scene v15s22_6d
                    with dissolve

                    u "Yeah, she was very supportive after we slipped her some cash."

                    scene v15s22_6j # FPP. same as v15s22_6d The Dean sighs and rolls her eyes, still an annoyed expression
                    with dissolve

                    pause 0.75

                    scene v15s22_7b
                    with dissolve

                    cl "[name]!"

                    scene v15s22_7c
                    with dissolve

                    cl "I'm sorry, Dean Harrison..."

                    scene v15s22_7d
                    with dissolve

                    u "It's only a joke!"

                    scene v15s22_6k # FPP. same as v15s22_6f The Dean gives mc a stern look, not impressed expression, mouth is still closed
                    with dissolve

                    pause 0.75

                    scene v15s22_6f
                    with dissolve

                    u "There was no bribe, honest."

                    scene v15s22_6e
                    with dissolve

                    de "Timing is everything, [name]. And this certainly isn't the time."

                    $ v15s22_meeting_points -= 1
                    show screen teacher_conviction_bar((v15s22_meeting_points+5) * 100 / 13, "CONVINCE DEAN", "DEAN", "images/v15/conviction_bars/dean_background.webp")
                    de "The next time you speak, make sure it's something sensible."

                    scene v15s22_6f
                    with dissolve

                    u "Sorry."

                    scene v15s22_7e # FPP. same as v15s22_7b Chloe is slightly angry, mouth is closed, still looking at Mc
                    with dissolve

                    pause 0.75

                    scene v15s22_6g
                    with dissolve

                    de "So now you're here to convince me."

    else:
        scene v15s22_6
        with dissolve

        $ v15s22_meeting_points -= 1
        show screen teacher_conviction_bar((v15s22_meeting_points+5) * 100 / 13, "CONVINCE DEAN", "DEAN", "images/v15/conviction_bars/dean_background.webp")

        de "It doesn't look like you managed to secure any support from a teacher. There's no signature on here."

        scene v15s22_7c
        with dissolve

        cl "Well... We had a meeting, but unfortunately, we didn't win their support."

        scene v15s22_7d
        with dissolve

        menu:
            "The teacher was unfair":
                #$ add_point(KCT.TROUBLEMAKER)

                scene v15s22_6b
                with dissolve

                u "Yeah, I don't want to name names, but..."

                u "They really didn't listen to us."

                scene v15s22_7f # FPP. same as v15s22_7d Chloe has a confused expression, still looking at Mc, mouth is still open
                with dissolve

                pause 0.75

                scene v15s22_6b
                with dissolve

                u "We spent so much time preparing and they basically ignored everything we had to say."

                scene v15s22_6g
                with dissolve

                de "I can't imagine you're talking about any of my teachers here at SVC, [name]."

                scene v15s22_6e
                with dissolve

                $ v15s22_meeting_points -= 1
                show screen teacher_conviction_bar((v15s22_meeting_points+5) * 100 / 13, "CONVINCE DEAN", "DEAN", "images/v15/conviction_bars/dean_background.webp")

                de "I'm sure whoever you met with, you obviously didn't do a very good job of convincing them."

                scene v15s22_7c
                with dissolve

                cl "Probably, yes."

                scene v15s22_6f
                with dissolve

                u "That may be so, but I still feel we weren't given a fair shot."

                scene v15s22_7g # FPP. same as v15s22_7f chloe gives mc a stern look as if she's telling him to shut tp with her eyes, still looking at Mc, mouth is still closed
                with dissolve

                pause 0.75

                scene v15s22_6g
                with dissolve

                de "So now you're here to convince me."

            "We could've done better": # (CORRECT CHOICE - ONE POINT)
                #$ add_point(KCT.BRO)

                scene v15s22_6b
                with dissolve

                $ v15s22_meeting_points += 1
                show screen teacher_conviction_bar((v15s22_meeting_points+5) * 100 / 13, "CONVINCE DEAN", "DEAN", "images/v15/conviction_bars/dean_background.webp")

                u "In all honesty, we could've done better. We've reflected on it and learned a lot from the experience."

                scene v15s22_6d
                with dissolve

                pause 0.75

                scene v15s22_6c
                with dissolve

                de "So now you're here to convince me."

    scene v15s22_6b
    with dissolve

    u "Yes."
    
    if v11_pen_goes_europe:
        scene v15s22_6c
        with dissolve
        
        $ v15s22_meeting_points += 1
        show screen teacher_conviction_bar((v15s22_meeting_points+5) * 100 / 13, "CONVINCE DEAN", "DEAN", "images/v15/conviction_bars/dean_background.webp") 

        de "You did a fine job defending your friend when we met last time, [name]."
        
        de "I expect nothing but a solid presentation of your arguments today."
        
    else:
        scene v15s22_6c
        with dissolve
        
        de "For the sake of both of you I hope you do a better job than when we met last time, [name]."

    scene v15s22_6
    with dissolve

    de "I need to be sure that this proposal is a good idea for everyone, Chloe. Not just for the Chicks."

    scene v15s22_7
    with dissolve

    cl "Oh, absolutely."

    scene v15s22_6
    with dissolve

    de "Okay, so..."

    scene v15s22_6h
    with dissolve

    de "Convince me."

    scene v15s22_6d
    with dissolve

    menu:
        "I'll take my time":
            #$ add_point(KCT.TROUBLEMAKER)

            scene v15s22_6b
            with dissolve

            u "I'll take my time if that's alright. I don't want to leave out any major details."

            scene v15s22_6c
            with dissolve

            $ v15s22_meeting_points -= 1
            show screen teacher_conviction_bar((v15s22_meeting_points+5) * 100 / 13, "CONVINCE DEAN", "DEAN", "images/v15/conviction_bars/dean_background.webp")

            de "That's not necessary. I know what you're asking for, I need you to convince me."

        "Your time is important": # (CORRECT CHOICE - ONE POINT)
            #$ add_point(KCT.BRO)

            scene v15s22_6d
            with dissolve

            u "Your time is important, so I'll be as brief as possible."

            scene v15s22_6c
            with dissolve

            $ v15s22_meeting_points += 1
            show screen teacher_conviction_bar((v15s22_meeting_points+5) * 100 / 13, "CONVINCE DEAN", "DEAN", "images/v15/conviction_bars/dean_background.webp")

            de "Thank you. I'm glad you understand."

    if v15s21_meeting_points >= 1:
        menu:
            "Summarize the plan": # (CORRECT CHOICE - ONE POINT)
                #$ add_point(KCT.BRO)

                scene v15s22_6d
                with dissolve

                u "I'll try to summarize as best I can."

                scene v15s22_6c
                with dissolve

                $ v15s22_meeting_points += 1
                show screen teacher_conviction_bar((v15s22_meeting_points+5) * 100 / 13, "CONVINCE DEAN", "DEAN", "images/v15/conviction_bars/dean_background.webp")

                de "That would be appreciated."

                scene v15s22_6d
                with dissolve
                
            "Stress the teacher's support":
                #$ add_point(KCT.TROUBLEMAKER)

                scene v15s22_6b
                with dissolve

                u "I feel like it should be enough that we secured support from a teacher. Let's not pretend that's an easy thing to do."

                scene v15s22_7d
                with dissolve

                cl "Well, we can still try to summarize our goal for the Dean, [name]."

                scene v15s22_6h
                with dissolve

                $ v15s22_meeting_points -= 1
                show screen teacher_conviction_bar((v15s22_meeting_points+5) * 100 / 13, "CONVINCE DEAN", "DEAN", "images/v15/conviction_bars/dean_background.webp")

                de "That would be advisable, yes."

                scene v15s22_6f
                with dissolve

                menu:
                    "Agree": # (CORRECT CHOICE - ONE POINT)
                        #$ add_point(KCT.BRO)

                        scene v15s22_6b
                        with dissolve

                        $ v15s22_meeting_points += 1
                        show screen teacher_conviction_bar((v15s22_meeting_points+5) * 100 / 13, "CONVINCE DEAN", "DEAN", "images/v15/conviction_bars/dean_background.webp")

                        u "Okay, sure. Let's do that then."

                    "Be reluctant":
                        #$ add_point(KCT.TROUBLEMAKER)

                        scene v15s22_6k
                        with dissolve

                        $ v15s22_meeting_points -= 1
                        show screen teacher_conviction_bar((v15s22_meeting_points+5) * 100 / 13, "CONVINCE DEAN", "DEAN", "images/v15/conviction_bars/dean_background.webp")

                        u "We've worked very hard all day to prepare that signature for you, but sure. You're the boss."

                        pause 0.75

                        scene v15s22_7g
                        with dissolve
                        
                        pause 0.75

    scene v15s22_6g
    with dissolve

    de "Quickly, please. I have another meeting soon."

    scene v15s22_6b
    with dissolve

    u "(This woman is so difficult.)"

    scene v15s22_6b
    with dissolve

    menu:
        "Quick version":
            #$ add_point(KCT.TROUBLEMAKER)

            scene v15s22_6b
            with dissolve

            u "Well, if we're pushed for time..."

            scene v15s22_6b
            with dissolve

            u "Basically, we think you should agree to this proposal because in the long term it will attract a lot more students to SVC."

            scene v15s22_6l # FPP. same as v15s22_6k The Dean has a slightly confused expression, still looking at Mc, mouth is still closed
            with dissolve

            u "And it will encourage other sororities and fraternities to want the same treatment as the Chicks."

            scene v15s22_6m # FPP. same as v15s22_6l The Dean's mouth is open, still a slightly confused expression, still looking at Mc
            with dissolve

            u "And this should help improve enrollment numbers if we're offering reduced tuition fees."

            scene v15s22_6l
            with dissolve

            de "..."

            scene v15s22_6m
            with dissolve

            de "Oh, have you finished? That's it?"

            scene v15s22_6l
            with dissolve

            u "You wanted a quick version."

            scene v15s22_6m
            with dissolve

            $ v15s22_meeting_points -= 1
            show screen teacher_conviction_bar((v15s22_meeting_points+5) * 100 / 13, "CONVINCE DEAN", "DEAN", "images/v15/conviction_bars/dean_background.webp")

            de "That was... very quick."

            scene v15s22_7c
            with dissolve

            cl "It's obviously not as simple as that, but, yeah. That was a little quick..."

            scene v15s22_7f
            with dissolve

            pause 0.75

        "Main points": # (CORRECT CHOICE - ONE POINT)
            #$ add_point(KCT.BRO)

            scene v15s22_6b
            with dissolve

            u "First, think about all the students that would enroll here because of the possibility of reduced tuition."

            scene v15s22_6n # FPP. same as v15s22_6g The Dean has an intrigued expression, still looking at Mc, mouth is still closed
            with dissolve

            u "It also encourages less-privileged people to apply. With reduced tuition fees, they might feel they can afford a college education."

            scene v15s22_6g
            with dissolve

            $ v15s22_meeting_points += 1
            show screen teacher_conviction_bar((v15s22_meeting_points+5) * 100 / 13, "CONVINCE DEAN", "DEAN", "images/v15/conviction_bars/dean_background.webp")

            de "Okay, that's a valid first point."

            scene v15s22_7
            with dissolve

            cl "Yeah, we think it has the potential to open things up and provide opportunities for others."

            scene v15s22_6b
            with dissolve

            u "And in terms of fairness with the other sororities and fraternities, when they see the Chicks leading the way, they will want the same treatment."

            scene v15s22_6n
            with dissolve

            u "This will make them up their game and work harder as leaders and as students."

            scene v15s22_7
            with dissolve

            cl "And with lower fees across the board, it will help with our first point about encouraging more people to enroll."

            scene v15s22_6g
            with dissolve

            de "I see... Good."

            scene v15s22_6h
            with dissolve

            de "I was wondering how you would justify that, but it makes sense that they would need to work a bit harder."

            scene v15s22_6c
            with dissolve

            de "They'd have to ask for a meeting with me too if they want the same treatment."

            scene v15s22_7
            with dissolve

            cl "Exactly."
        
    if not v15_seduce_ms_rose and not v15_threaten_ms_rose:
        scene v15s22_6b
        with dissolve

        u "And you should also know that Chloe has agreed to give up her scholarship as part of the proposal."

        scene v15s22_6o # FPP. same as v15s22_6b The Dean is slightly shocked, mouth is still closed, still looking at Mc
        with dissolve

        de "Oh- Wow..."

        scene v15s22_6h
        with dissolve

        $ v15s22_meeting_points += 1
        show screen teacher_conviction_bar((v15s22_meeting_points+5) * 100 / 13, "CONVINCE DEAN", "DEAN", "images/v15/conviction_bars/dean_background.webp")
        
        de "That is a surprise. I was opposed to the scholarship from the beginning, so that's a major bonus point, Chloe."

        scene v15s22_7
        with dissolve

        cl "We're thinking that the money from the scholarship can be put towards reducing the tuition fees."

        scene v15s22_6h
        with dissolve

        de "That's an excellent idea."

    scene v15s22_6
    with dissolve

    de "Well, I think I've heard enough to make my decision."

    scene v15s22_5b
    with dissolve

    pause 0.75

    scene v15s22_6p # FPP. same as v15s22_6a The Dean is looking at the piece of paper, reading it again for a moment, mouth is closed, still no expression
    with dissolve
    
    pause 0.75

    scene v15s22_7d
    with dissolve

    pause 0.75

    scene v15s22_6a
    with dissolve

    de "Hmm."

    scene v15s22_5b
    with dissolve

    pause 0.75

    if v15s21_meeting_points >= 1:
        if v15s22_meeting_points >= 5: # -if won signature and max dean support

            scene v15s22_6q # FPP. same as v15s22_6h The Dean has a full smile, still looking at Chloe, mouth is still open
            with dissolve

            de "You've done very well with this proposal. I'm impressed."

            jump v15dean_successful

        elif v15s22_meeting_points == 1 and kct == "popular": # if won signature and low dean support with kct popular
            call screen kct_popup

            scene v15s22_6
            with dissolve

            de "I have to be honest. You didn't do very well at all."

            scene v15s22_6g
            with dissolve

            de "However, I'm aware that you're both very popular students here at SVC, and that always adds a certain momentum to a cause."

            jump v15dean_successful

        elif v15s22_meeting_points >= 1: # -if won signature and medium dean support
            scene v15s22_6h
            with dissolve

            de "The meeting didn't go perfectly, but you did a good job of convincing me."

            jump v15dean_successful

        else: # -if won signature and no dean support
            scene v15s22_6g
            with dissolve

            de "When I consider everything that you've said today, it wasn't good enough. I think you could have done a lot better."

            scene v15s22_7b
            with dissolve

            u "(Fuck...)"

            scene v15s22_6g
            with dissolve

            de "And based on that performance, I'm not sure how you even managed to secure a teacher's signature..."

            scene v15s22_7c
            with dissolve

            cl "Can we please just try again?"

            scene v15s22_6
            with dissolve

            de "There are no do-overs, Chloe."

            de "I'm sorry. My answer is no. Good luck with the rest of your campaign."

            scene v15s22_7h # FPP. same as v15s22_7d Chloe has a very sad expression, mouth is open, still looking at Mc
            with dissolve

            pause 0.75

            scene v15s22_7i # FPP. same as v15s22_7h Chloe is looking at The Dean, still a very sad expression, mouth is still open
            with dissolve

            cl "Okay. Thanks."

            jump v15dean_unsuccessful

    elif v15s22_meeting_points >= 5: # -if no signature, but high dean support
        scene v15s22_6q # FPP. same as v15s22_6h The Dean has a full smile, still looking at Chloe, mouth is still open
        with dissolve

        de "You've done very well with this proposal. I'm impressed."

        scene v15s22_6
        with dissolve

        de "But you need to give up your scholarship. Only then we can proceed with this."

        scene v15s22_7j # FPP. same as v15s22_7b Chloe is looking at The Dean, still a shocked expression, mouth is still open
        with dissolve

        cl "What?!"

        scene v15s22_6
        with dissolve

        de "It's the only way I can make this feasible."

        scene v15s22_7d
        with dissolve

        pause 0.75

        scene v15s22_7c
        with dissolve

        cl "Well... if it's the only way..."

        cl "I guess we should do it."

        scene v15s22_7d
        with dissolve

        u "*Whispers* Are you sure?"

        scene v15s22_7k # FPP. same as v15s22_7d Chloe's mouth is open, still a worried expression, still looking at Mc
        with dissolve

        cl "Yeah. I have to do whatever it takes."

        scene v15s22_6h
        with dissolve

        de "That's a very mature decision, Chloe. Well done."

        scene v15s22_7l # FPP. same as v15s22_7 Chloe has no expression, still looking at The Dean, mouth is still open
        with dissolve

        cl "Thank you."

        scene v15s22_6h
        with dissolve

        de "Now you just need to win your campaign and we make this a reality."

        scene v15s22_7l
        with dissolve

        cl "I'll do my best, ha."

        jump v15dean_successful

    elif v15s22_meeting_points >= 1: # -if no signature, and medium/low dean support
        if kct == "popular":
        
            if v15s22_meeting_points == 1:
                call screen kct_popup
        
            scene v15s22_6g
            with dissolve

            de "You're both very popular students, which I think helps your position on this proposal. But..."

        scene v15s22_6
        with dissolve

        de "Chloe, you're going to have to give up your scholarship for this to work."

        scene v15s22_7c
        with dissolve

        cl "Oh... Do I really need to? I-"

        scene v15s22_6
        with dissolve

        de "Yes. It's the only way I can afford to make this idea work."

        scene v15s22_7d
        with dissolve

        pause 0.75

        scene v15s22_7k
        with dissolve

        cl "Well..."

        scene v15s22_7c
        with dissolve

        cl "If that's what it takes, I guess we should do it."

        scene v15s22_7d
        with dissolve

        u "*Whispers* Are you sure?"

        scene v15s22_7k
        with dissolve

        cl "Yeah. I have to do whatever it takes."

        scene v15s22_6h
        with dissolve

        de "You've made a wise decision, Chloe. Well done."

        scene v15s22_7l
        with dissolve

        cl "Thank you."

        scene v15s22_6h
        with dissolve

        de "Now go and win your campaign and we can make this a reality."

        scene v15s22_7l
        with dissolve

        cl "I really hope I can. I'll keep working hard."

        scene v15s22_6h
        with dissolve

        de "Good for you."

        jump v15dean_successful

    else: # -if no signature and MC scored 2 points or less
        scene v15s22_6
        with dissolve

        de "You arrived already in a weak position, having failed to secure support from any teachers."

        scene v15s22_6e
        with dissolve

        de "And your performance here today was lacking." 
        
        scene v15s22_6
        with dissolve

        de "I commend you for your efforts, but I have to reject your proposal."

        de "Good luck with the rest of your campaign, Chloe."

        scene v15s22_7h
        with dissolve

        pause 0.75

        scene v15s22_7i
        with dissolve

        cl "Oh, okay then... Thanks."

        jump v15dean_unsuccessful

    label v15dean_successful:
        scene v15s22_6h
        with dissolve

        $ set_presidency_percent(v14_lindsey_popularity - 3)

        de "I'm happy to proceed with reducing tuition fees for the Chicks. We can use your sorority as a case study and see how it goes."

        scene v15s22_7j
        with dissolve

        cl "*Gasps* Oh my-"

        scene v15s22_7m # FPP. same as v15s22_7b Chloe has an excited expression, mouth is still open, still looking at Mc
        with dissolve

        pause 0.75

        scene v15s22_7n # FPP. same as v15s22_7m Chloe is looking at The Dean, still an excited expression, mouth is still open
        with dissolve

        cl "That's amazing! Thank you so much!"

        scene v15s22_6d
        with dissolve

        u "Seriously, this is great. Thank you."

        scene v15s22_6h
        with dissolve

        de "Now you just need to complete the simple task of winning your campaign."

        scene v15s22_6q
        with dissolve

        de "Then this whole plan can become official."

        scene v15s22_7
        with dissolve

        cl "Yeah, no pressure there! *Nervous chuckles*"

        scene v15s22_6h
        with dissolve

        de "I'm sure you can do it. You've come this far."

        scene v15s22_5c # TPP. same as v15s22_5b The Dean, Chloe, and Mc are all now standing, The Dean is shaking Chloe's hand both of them have slight smiles, mouths are closed, Mc is watching Chloe slight smile mouth is closed
        with dissolve

        pause 0.75

        scene v15s22_3a # TPP. same as v15s22_3 MC and Chloe are walking out of The Dean's office, both of them are smiling and looking at each other
        with dissolve

        pause 0.75

        scene v15s22_1a # TPP same as v15s22_1 Chloe and Mc are walking the other direction, still slight smiles, Chloe's mouth is open, Mc's mouth is closed, they are looking at each other
        with dissolve

        pause 0.75

        scene v15s22_2b
        with dissolve

        cl "We did it! *Laughs*"

        scene v15s22_2d
        with dissolve

        u "Haha, we did! I can't believe we actually just pulled that off."

        scene v15s22_2c
        with dissolve

        cl "Thank you so much for your help in there, [name]."

        scene v15s22_2d
        with dissolve

        u "Of course."

        if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
            play sound "sounds/kiss.mp3"
        
            scene v15s22_1d # TPP. same as v15s22_1b Chloe gives Mc a romantic hug and kiss, both of them have their eyes closed
            with dissolve

            pause 0.75

            play sound "sounds/vibrate.mp3"

            scene v15s22_1c
            with dissolve

            pause 0.75

            scene v15s22_8
            with dissolve

            pause 0.75

        elif chloe.relationship.value < Relationship.FWB.value: 
            scene v15s22_1b # TPP. same as v15s22_1a Mc and Chloe stop walking and Chloe gives Mc and friendly hug, both slight smiles, both mouths are closed
            with dissolve

            pause 0.75

            play sound "sounds/vibrate.mp3"

            scene v15s22_1c # TPP. same as v15s22_1 Mc and Chloe stop hugging and Mc pulls his phone out of his pocket, Mc and Chloe are looking down at his phone, slight smiles, mouths are closed
            with dissolve

            pause 0.75

            scene v15s22_8 # FPP. Closed up shot of Mc's phone, show only his phone in his hand, the phone screen says, new messages
            with dissolve

            pause 0.75
        
        jump v15s22_afterchloe

    label v15dean_unsuccessful:
        scene v15s22_5d # TPP. same as v15s22_5c The Dean is walking away from Mc and Chloe not shaking Chloe's hand no expression mouth is closed, Mc and Chloe are both still standing, Chloe has a sad expressions looking at Mc mouth is closed, Mc has no expression looking at Chloe mouth is closed
        with dissolve

        pause 0.75

        scene v15s22_3b # TPP. same as v15s22_3b MC has no expression mouth is closed looking at Chloe, Chloe has a sad expression mouth is closed looking at Mc
        with dissolve

        pause 0.75

        scene v15s22_1e # TPP. same as v15s22_1a Chloe has a sad expression mouth is closed looking forward, Mc has no expression, mouth is closed, looking at Chloe
        with dissolve

        pause 0.75

        scene v15s22_2i # FPP. same as v15s22_2 Chloe has a very sad expression, mouth is still open, still looking at Mc
        with dissolve

        cl "I can't believe it... I worked so hard for this..."

        if v15s21_meeting_points >= 1:
            if v15_chloe_mrleesupport:
                cl "We even got Mr. Lee's support. All that hard work... for nothing."
                
            else:
                cl "We even got Ms. Rose's support. All that hard work... for nothing."

        scene v15s22_2j # FPP. same as v15s22_2i Chloe's mouth is closed, still looking at Mc, still a very sad expression
        with dissolve

        u "I'm sorry, Chloe I-"

        scene v15s22_2i
        with dissolve

        cl "I need to be alone for a little while."

        scene v15s22_1f # TPP. Chloe walks away from MC, her back is turned to Mc, still a sad expression, still looking forward, mouth is still closed, Mc has no expression watching Chloe Leave, mouth is open
        with dissolve

        menu:
            "Call after her":
                $ add_point(KCT.BRO)
                
                if chloe.relationship.value >= Relationship.FWB.value:
                    $ add_point(KCT.TROUBLEMAKER)

                scene v15s22_1f
                with dissolve

                u "Chloe!"

                u "Come on, let's talk about it!"

                scene v15s22_1g # TPP. same as v15s22_1f Chloe completely ignores MC and walks further away, Chloe's face can't be seen now, Mc is still watching Chloe leave, Mc has a sad expression, mouth is closed
                with dissolve

                pause 0.75

                play sound "sounds/vibrate.mp3"

                scene v15s22_1h # TPP. same as v15s22_1g Chloe is no longer visible in the render, Mc is looking down at his pocket pulling out his phone, no expression, mouth is closed
                with dissolve

                pause 0.75

                scene v15s22_8
                with dissolve

                pause 0.75

            "Say nothing":
                $ add_point(KCT.BRO)
                
                if chloe.relationship.value >= Relationship.FWB.value:
                    $ add_point(KCT.BOYFRIEND)

                scene v15s22_1g
                with dissolve

                u "(I think it's best I give her some space.)"
            
                play sound "sounds/vibrate.mp3"

                scene v15s22_1h
                with dissolve

                pause 0.75

                scene v15s22_8
                with dissolve

                pause 0.75

    label v15s22_afterchloe:

    if v15_lindsey_gamenight: # -if helping Lindsey with Games night
        $ lindsey.messenger.newMessage("Hey, can you come meet me now to buy the alcohol for our game night? I have a plan! I'll send the details of which store to come to.", force_send=True)
        $ lindsey.messenger.addReply("Okay, I'll be there soon!", func=None)

    elif v14_help_lindsey:
        $ lindsey.messenger.newMessage("Hey, can you call the club and book the VIP party package now please? See what you can do in terms of them serving us alcohol and negotiating the price!", force_send=True)
        $ lindsey.messenger.addReply("Okay, I'll try to charm them. I'll let you know how it goes!", func=None)

    else:
        $ aubrey.messenger.newMessage("Come to the Chicks house. I have an extra special surprise for you ;) I think you've earned it.", force_send=True)

        if aubrey.relationship.value >= Relationship.FWB.value: # -if AubreyRs
            $ aubrey.messenger.addReply("A naked surprise? ;)", func=None)
            $ aubrey.messenger.newMessage("Guess you'll find out soon enough!", force_send=True)

        else: # -if AubreyFriend
            $ aubrey.messenger.addReply("Haha, okay see you there.", func=None)

    label v15s22_PhoneContinueLin:
        if lindsey.messenger.replies:
            call screen phone
        if lindsey.messenger.replies:
            u "(I should reply to Lindsey.)"
            jump v15s22_PhoneContinueLin

    label v15s22_PhoneContinueAub:
        if aubrey.messenger.replies:
            call screen phone
        if aubrey.messenger.replies:
            u "(I should reply to Aubrey.)"
            jump v15s22_PhoneContinueAub


    scene v15s22_8a # FPP. same as v15s22_8 The phone is now just has a blank black screen
    with dissolve

    pause 0.75

    if v15s22_meeting_points >= 1:
        scene v15s22_2d
        with dissolve

        u "Looks like I need to go."

        scene v15s22_2c
        with dissolve

        cl "That's okay. I'm done with you for now, haha."

        scene v15s22_2d
        with dissolve

        u "Haha, okay. Well, glad I could be of service."

        scene v15s22_2c
        with dissolve

        cl "Thanks again, [name]. You're the best."

        scene v15s22_2d
        with dissolve

        u "No problem at all!"

        scene v15s22_1i # TPP. same as v15s22_1a Mc is walking away from Chloe looking back at her and waving, Chloe is waving back at Mc, both of them slight smiles aand mouths closed
        with dissolve

        pause 0.75

    else:
        scene v15s22_1j # TPP. same as v15s22_1h Mc has a full smile, looking at his phone in his hand, mouth is closed, Chloe is still not in the render
        with dissolve

        u "(I need a pick me up... Please Aubrey, give me a good time. *Sighs*)"

        scene v15s22_1k # TPP. same as v15s22_1j Mc has put his phone away in his pocket and is now walking down the hallway, slight smile, mouth is closed, Chloe is still not in the render
        with dissolve

        pause 0.75

    if v15_lindsey_gamenight:
        jump v15s24

    elif v14_help_lindsey:
        jump v15s25

    else:
        jump v15s26