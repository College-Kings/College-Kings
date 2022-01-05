# SCENE 21: Meeting with Ms. Rose
# Locations: A Private room located in the Library
# Characters: CHLOE (Outfit: 3), MC (Outfit: 9), Ms. Rose (Outfit: 1), Mr. LEE (Outfit: 1)
# Time: AfterNoon
# Render Count: 17 unique 148 total

label v15s21:
    if v15_chloe_mrleesupport:
        if kct == "loyal":
            $ v15s21_meeting_points += 1

        $ animated_value_percent = (v15s21_meeting_points + 4) * 10

        scene v15s21_1 # FPP. Mr . Lee enters the library, slight smile, mouth closed
        with dissolve

        pause 0.75

        scene v15s21_2 # FPP. Chloe and Mc are still sitting down in the library from renders created in v15s20, Chloe looks away from MC towards Mr. Lee walking into the library, Chloe slight smile, mouth open
        with dissolve

        cl "Here he is."

        $ opened_count = 0 # reset counter
        scene v15s21_3 # FPP. Mr. Lee approaches them slight smile mouth open, Chloe and MC stand up, Chloe slight smile, mouth closed
        with dissolve

        lee "Good morning, Chloe and [name]."

        scene v15s21_3a # FPP. Mr. Lee is now in front of Chloe and MC, Mr. Lee slight smile mouth closed, Chloe slight smile mouth open looking at Mr. Lee
        with dissolve

        cl "Good morning, Mr. Lee."

        scene v15s21_3b # FPP. same as v15s21_3a Mr. Lee and Chloe, slight smiles, mouths closed
        with dissolve

        u "Hello."

        scene v15s21_3c #FPP. same as v15s21_3a Mr. Lee's mouth is open
        with dissolve

        lee "I'm glad to see you're both on time. That shows not only intelligence, but great respect for your guest."

        scene v15s21_3b
        with dissolve

        u "(Straight in with the life lessons, haha.)"

        u "Of course, your time is very valuable, as is ours."

        scene v15s21_3a
        with dissolve

        cl "Yes, thank you for agreeing to this, Mr. Lee."

        cl "If you would like to follow me, I've booked a room for us to meet."

        scene v15s21_3c
        with dissolve

        lee "Punctual and organized. Very good."

        scene v15s21_3d # FPP. same as v15s21_3b Chloe looks at MC giving him a happy look to MC
        with dissolve

        u "(I think we're scoring points already.)"

        scene v15s21_4 # TPP. Show Chloe opening the door to a private room in the library, Mr. Lee walks into the room first followed by mc, all slight smiles, mouths closed
        with dissolve

        pause 0.75

        scene v15s21_5 # TPP. Show a table with at least 3 seats, Chloe sits on one side with an empty to her right for MC, Mr, Lee sits at a chair located on the other side of the table, slight smiles, mouths closed, Mr. Lee and Chloe are looking at each other.
        with dissolve

        pause 0.75

        scene v15s21_6 # FPP. Mc has sat down across from Mr. Lee and next to Chloe, Show only Mr. Lee, looking at Chloe, slight smile, mouth open
        with dissolve

        lee "So, I understand you have a proposal that you would like my support on?"

        #!!!RENDERER!!! DO NOT SHOW MR.LEE OR MS.ROSE ON ANY OF THE RENDERS LISTED AS v15s21_7... THIS IS NECESSARY TO REDUCE RENDER COUNT AND HOLD CONSISTENCY!

        scene v15s21_7 # FPP. MC looks to his left and see's only Chloe looking at the teacher's position, slight smile, mouth open
        with dissolve

        cl "Yeah, it's part of my election campaign. I'm being challenged for the presidency of the Chicks."

        scene v15s21_6
        with dissolve

        lee "We've all seen the posters, they're everywhere. Lindsey is shaping up to be quite a formidable rival."

        scene v15s21_6a # same as v15s21_6 FPP. Mr. Lee is still looking at Chloe, slight smile, mnouth closed
        with dissolve
        show screen teacher_conviction_bar((v15s21_meeting_points + 4) * 10, "MR. LEE")

        menu:
            "Lindsey's wasting paper":
                $ add_point(KCT.TROUBLEMAKER)
                $ v15s21_meeting_points -= 1

                show screen teacher_conviction_bar((v15s21_meeting_points + 4) * 10, "MR. LEE")

                scene v15s21_6b # FPP same as v15s21_6 Mr. Lee is now looking at mc, no expression, mouth closed.
                with dissolve

                u "I think it's irresponsible to waste so much paper, does she not care about the environment?"

                scene v15s21_7a # FPP. same as v15s21_7 Chloe is looking at Mc, no expression, mouth open
                with dissolve

                cl "*Whispers* [name]..."

                scene v15s21_6b
                with dissolve

                u "They should all be taken down as punishment in my opinion."

                scene v15s21_6c # FPP. same as v15s21_6b Mr. Lee's mouth is open, is still looking at Mc, still no epxpression
                with dissolve

                lee "I agree with your global deforestation concerns, but punishing Lindsey for simply putting up posters would be a bit too far, don't you think?"

                scene v15s21_6a
                with dissolve

                cl "Of course, we don't want that. *Nervous chuckles*"

                scene v15s21_6b
                with dissolve

                u "(*Sighs*)"

                scene v15s21_6c
                with dissolve

                lee "There is honor in fighting fair, [name], and Lindsey is doing nothing wrong."

                scene v15s21_6b
                with dissolve

                u "Yeah. You're right, I'm sorry."

            "Stay quiet":
                $ v15s21_meeting_points += 0
                $ add_point(KCT.BRO)

                show screen teacher_conviction_bar((v15s21_meeting_points + 4) * 10, "MR. LEE")

                scene v15s21_6d #FPP. same as v15s21_6b Mr. Lee is still looking at MC, mouth closed, slight smile
                with dissolve

                u "(It's best to keep my mouth shut... Don't want to risk pissing him off.)"

                scene v15s21_7
                with dissolve

                cl "I have to agree, she is. Which is why I'm doing whatever it takes to prove to my peers that I'm a better fit for President."

                scene v15s21_6
                with dissolve

                lee "Excellent. Then, let's begin."

        scene v15s21_7
        with dissolve

        cl "So, the reason I've asked you to meet with us today is to hopefully gain your support for my proposal."

        scene v15s21_7b # FPP. same as v15s21_7 Chloe holds out a paper, slight smile, mouth closed
        with dissolve

        pause 0.75

        scene v15s21_6e # FPP. same as v15s21_6 Mr. Lee is looking at the paper Chloe handed him from v15s21_7b, serious expression, mouth closed
        with dissolve

        pause 0.75

        scene v15s21_7 
        with dissolve

        cl "If I'm successful, I can then take our approved idea to the Dean and get it implemented."

        scene v15s21_6f # FPP. same as v15s21_6e Mr. Lee looks up from the paper at Chloe with a raised eyebrow, slight smile, mouth is still closed, still holding the paper
        with dissolve

        lee "Hmm."

        scene v15s21_7c # FPP. same as v15s21_7a Chloe is still looking at Mc, sliight smile, mouth closed
        with dissolve

        u "(Who is this smart person and what did she do with Chloe?)"

        scene v15s21_6e
        with dissolve

        pause 0.75

        scene v15s21_7d # FPP. same as v15s21_7a Chloe looks at Mc with a nervous expression, mouth is still closed
        with dissolve

        pause 0.75

        scene v15s21_6g # FPP. same as v15s21_6f Mr. Lee's mouth is open, still has a raised eyebrow, still looking up from the paper at Chloe, still holding the paper
        with dissolve

        lee "That's a bold proposal. You'll certainly gain a majority of votes if you succeed."

        scene v15s21_7
        with dissolve

        cl "Thank you."

        scene v15s21_5a # TPP. same as v15s21_5 Mc, is now sitting next to chloe, Show Mr. Lee putting the paper into the center of the table between himself and Mc and Chloe, all of them no expressions, mouths closed
        with dissolve

        pause 0.75

        scene v15s21_6
        with dissolve

        lee "Now, I have a few questions..."

        scene v15s21_6a
        with dissolve

        u "Here we go..."

        if v15_took_notes:
            scene v15s21_6a
            with dissolve

            u "(At least we brought the notes with us. We can refer to them whenever.)"

        else: # -they have no journal icon, no access to notes-
            scene v15s21_6a
            with dissolve

            u "(I hope I don't regret not bringing those notes.)"

        scene v15s21_6h # FPP. same as v15s21_6 Mr. Lee has no expression, is still looking at Chloe, mouth is still open
        with dissolve

        lee "Naturally, my initial feelings are to fight strongly against this."

        lee "How can you justify one group having lower tuition fees and not the others?"

        lee "What will your fellow students think when they see the Chicks being favored over the other frats and sororities?"

        scene v15s21_6b
        with dissolve

        menu:
            "They just have to ask":
                $ v15s21_meeting_points += 1
                $ add_point(KCT.BRO)

                show screen teacher_conviction_bar((v15s21_meeting_points + 4) * 10, "MR. LEE")


                scene v15s21_6b
                with dissolve

                u "In all fairness, they have every right to walk in here and ask for lower tuition fees. They just have to ask. This isn't favoritism."

                scene v15s21_6d
                with dissolve

                u "Chloe might just be the first person who's brave enough to make it happen."

                scene v15s21_7
                with dissolve

                cl "It's true. If they want the same treatment, they just have to try."

                scene v15s21_6i # FPP. same as v15s21_6d Mr. lee smirks, mouth is open, still looking at MC, still slight smile
                with dissolve

                lee "Yes, that is true. I'm all for students taking the initiative and owning responsibility."

                lee "They are indeed free to ask for the same treatment if they want it."
                lee "And I'm certain they will if your plan goes through. So we should consider the implications of that carefully."

            "This is Chloe's idea":
                $ add_point(KCT.BOYFRIEND)
                $ add_point(KCT.TROUBLEMAKER)

                $ v15s21_meeting_points -= 1

                show screen teacher_conviction_bar((v15s21_meeting_points + 4) * 10, "MR. LEE")


                scene v15s21_6b
                with dissolve

                u "Chloe came up with this idea, that's not her fault."

                scene v15s21_6j # FPP. same as v15s21_6b Mr. Lee raises an eyebrow, is still looking at mc, still no expression, mouth is still closed
                with dissolve

                u "Why should the future of the Chicks have to suffer because others are sad that they didn't think of it first?"

                scene v15s21_7a
                with dissolve

                cl "Yeah, that's true..."

                scene v15s21_6c
                with dissolve

                lee "It is not that they didn't think of it, it may just seem out of order for an entire sorority to receive tuition benefits, and not the others."

                scene v15s21_6b
                with dissolve

                u "Chloe's the one putting in all the hard work to make a change. If it's awarded, then the Chicks deserve it, plain and simple."

                scene v15s21_6c
                with dissolve

                lee "Hard work does not mean others should lose out, nor does it make them any less smart."

        scene v15s21_7
        with dissolve

        cl "Whether it's just the Chicks or all the other frats and sororities too that benefit, reduced tuition equals more students coming to SVC."

        scene v15s21_6
        with dissolve

        lee "Please explain."

        scene v15s21_7
        with dissolve

        cl "Well, it's obvious more students would come here for that. Everyone would love lower tuition fees, wouldn't they?"

        scene v15s21_6k # FPP. same as v15s21_6 Mr. Lee is still looking at Chloe, rolls his eyes, no expression, mouth is still open
        with dissolve

        lee "*Sighs* Yes, money attracts."

        scene v15s21_6b
        with dissolve

        u "(I should jump in here and expand on that.)"

        u "I think what's most important about Chloe's proposal is that this will..."

        scene v15s21_6b
        with dissolve

        menu:
            "Make SVC more money":
                $ add_point(KCT.TROUBLEMAKER)

                $ v15s21_meeting_points -= 1

                show screen teacher_conviction_bar((v15s21_meeting_points + 4) * 10, "MR. LEE")


                scene v15s21_6b
                with dissolve

                u "Overall, increase SVC's annual income."

                scene v15s21_6l # FPP. same as v15s21_6b Mr. Lee has a judgemnetal expression, still looking at Mc, mouth is still closed
                with dissolve

                u "With lower fees you can have a lot more students applying each year, so in the end it pays off for the school."

                scene v15s21_6b
                with dissolve

                u "You might even get a pay raise from all that sweet money coming in. In the long run, it's all about profit."

                scene v15s21_6m # FPP. same as v15s21_6l Mr. Lee has an offended expression, still lookimng at Mc, mouth is open
                with dissolve

                lee "*Scoffs*"

                lee "I have to disagree with you there, [name]. Education should never be valued solely on its ability to generate profit."

                lee "And I do thank you for your concern, but I'm very happy with my current salary... If you must know."

                scene v15s21_6n # FPP. same as v15s21_6m Mr. Lee's mouth is closed, still has an offended expression, still looking at mc
                with dissolve

                u "Of course, s-sorry."

            "Improve students' livelihood":
                $ v15s21_meeting_points += 1
                $ add_point(KCT.BRO)

                show screen teacher_conviction_bar((v15s21_meeting_points + 4) * 10, "MR. LEE")


                scene v15s21_6b
                with dissolve

                u "Improve the livelihood of your students. Mentally and physically."

                scene v15s21_6o # FPP. same as v15s21_6d Mr. Lee. places a hand under his chin and listens intently, furrows his eyebrows, still a slight smile, mouth is still closed
                with dissolve

                u "College is a huge financial burden, Mr. Lee."
                u "With lower fees, students may be more free to enjoy extracurricular activities around campus, rather than working in between classes."

                scene v15s21_7
                with dissolve

                cl "Not having to work would be amazing..."

                scene v15s21_6p # FPP. same as v15s21_6l Mr. Lee looks at Chloe, still has a judgemental expression, mouth is still closed
                with dissolve

                pause 0.75

                scene v15s21_7e # FPP. same as v15s21_7a Chloe has no expression, eyes widen, still looking at Mr. Lee, mouth is still open
                with dissolve

                cl "I mean, for everyone..."

                scene v15s21_6b
                with dissolve

                u "Right."

                scene v15s21_7e
                with dissolve

                cl "I can't keep count of how many times my friends were so stressed about affording tuition, that they started failing their classes..."

                scene v15s21_7f # FPP. same as v15s21_7a Chloe's mouth is closed, still no expression, still looking at mc
                with dissolve

                u "(Nice save... *Chuckles*)"

                scene v15s21_6b
                with dissolve

                u "And let's not forget about those who can't even afford college in the first place."

                scene v15s21_6d
                with dissolve

                u "If SVC subsidized their fees, even by a little, it would encourage many people from low-income households to invest in their education."

                scene v15s21_6i
                with dissolve

                lee "Hmph... Yes, those are some very valid points, [name]."

                lee "Finding ways to help the less privileged should always be a priority."

                lee "And it would be a shame for anyone to miss out on the opportunity to have a college education here at SVC."

                scene v15s21_7
                with dissolve

                cl "Absolutely it would."

                scene v15s21_7c
                with dissolve

                pause 0.75

        scene v15s21_6
        with dissolve

        lee "But let's not forget, Chloe..."

        scene v15s21_7g # FPP. same as v15s21_7d Chloe is looking at the teacher, still nervous expression, mouth is still closed
        with dissolve

        pause 0.75

        scene v15s21_6h
        with dissolve

        lee "That the Chicks already have a scholarship in place where their President pays absolutely nothing for tuition."

        scene v15s21_7h # FPP. same as v15s21_7g Chloe's mouth is open, still looking at the teacher, still nervous expression
        with dissolve

        cl "Um, y-yes... That started the year I became President."

        scene v15s21_6h
        with dissolve

        lee "I'm aware."
        
        lee "This is something I was against at the time, but nevertheless..."

        lee "It was approved by the Dean."

        scene v15s21_7h
        with dissolve

        cl "Well, surely the Dean approved it for a good reason."

        scene v15s21_6h
        with dissolve

        lee "It's quite a grey area still... Though, I understand I may be in the minority with my opinion on that."

        lee "I'm sure that being President requires a good amount of hard work."
        lee "But I still feel that it's unfair to give a free ride to someone just because they won a popularity contest."

        scene v15s21_7i # FPP. same as v15s21_7h Chloe places a hand on her chest and extends the other hand palm up to the teacher, still looking at the teacher, still a nervous epxression, mouth is still closed
        with dissolve

        cl "But that's not my fault."

        scene v15s21_6h
        with dissolve

        lee "Nobody is saying it's your fault, Chloe."

        scene v15s21_6b
        with dissolve

        menu:
            "Defend the Dean's decision":
                $ add_point(KCT.BOYFRIEND)

                $ v15s21_meeting_points -= 1
                
                show screen teacher_conviction_bar((v15s21_meeting_points + 4) * 10, "MR. LEE")


                scene v15s21_6b
                with dissolve

                u "I think the Dean made a wise decision with the scholarship."

                scene v15s21_6l
                with dissolve

                u "Since she is the Dean, her decisions are probably what's most beneficial for the school."

                scene v15s21_7a
                with dissolve

                cl "Yes, that's what she said."

                scene v15s21_6l
                with dissolve

                u "So, I don't see how Chloe could be undeserving of the benefits."

                scene v15s21_6q # FPP. same as v15s21_6l Mr. lees mouth is open, still a judgemental expression, still looking at MC
                with dissolve

                lee "It would require you to see things from another perspective, [name]. A skill that you're clearly struggling to demonstrate at the moment."

            "Defend Mr. Lee's opinion":
                $ v15s21_meeting_points += 1
                $ add_point(KCT.BRO)

                show screen teacher_conviction_bar((v15s21_meeting_points + 4) * 10, "MR. LEE")


                scene v15s21_6b
                with dissolve

                u "I can see your point of view. It may seem unbalanced."

                scene v15s21_7j # FPP. same as v15s21_7h Chloe has a confused expression, still looking at Mc, mouth is still closed.
                with dissolve

                u "To others."

                scene v15s21_6i
                with dissolve

                lee "Exactly, I'm glad one of you can at least see that this might upset a few people."

                scene v15s21_7h
                with dissolve

                cl "Okay, and...?"

                scene v15s21_6a
                with dissolve

                u "Do you have any suggestions for us?"

                scene v15s21_6r # FPP. same as v15s21_6d Mr. Lee has a full smile, mouth is open, still looking at Mc
                with dissolve

                lee "I'm glad you asked, [name]. I do have a suggestion, and I believe it'd work."
                lee "But I'll keep it to myself until I've decided if I'm going to support this idea."

        scene v15s21_6d
        with dissolve

        u "*Sighs* Okay, is there anything else?"

        if v15_took_notes and opened_count >= 5: # -if TookNotes and clicks on the journal five times- #
            scene v15s21_6c
            with dissolve

            $ grant_achievement("too_much_information")
            lee "[name], I appreciate that you came prepared and did your research..."

            scene v15s21_6b
            with dissolve

            u "(Shit...) I-"

            scene v15s21_6c
            with dissolve

            lee "Please, just take this as an important life lesson. Keep your eyes in the meeting as well as your head."

            scene v15s21_6b
            with dissolve

            u "Yeah, of course. Sorry."

            scene v15s21_6b
            with dissolve

            lee "Mmhmm..."

        scene v15s21_6
        with dissolve

        lee "Is that everything that you guys wanted to discuss?"

        if not v13_perfume: # -if MC gave Mr. Lee the bonsai tree gift in Amsterdam (had scene 13.57a instead of 13.57) = (bonus correct_points +1)
            $ v15s21_meeting_points += 1

            scene v15s21_7c
            with dissolve

            u "I believe so... Chloe?"

            scene v15s21_7k # FPP. same as v15s21_7c Chloe's mouth is open, still a slight smile, still looking at MC
            with dissolve

            cl "I'm finished as well."

            scene v15s21_6
            with dissolve

            lee "Very well, I-"

            scene v15s21_6r
            with dissolve

            lee "Oh! I almost forgot to mention!"

            show screen teacher_conviction_bar((v15s21_meeting_points + 4) * 10, "MR. LEE")

            lee "The bonsai tree you gifted to me is absolutely thriving alongside the others in my office."

            lee "If you're ever interested, swing by sometime and I'll teach you how to look after them."

            scene v15s21_6s # FPP. same as v15s21_6r Mr. Lee's mouth is closed, still a full smile, still looking at Mc
            with dissolve

            u "Oh, that's... a very kind offer. Thanks, haha."

            scene v15s21_7
            with dissolve

            cl "Are they difficult to care for?"

            scene v15s21_6
            with dissolve

            lee "Indeed. Their temperaments require endless patience and care from their owner, qualities that we should all practice."

            scene v15s21_7k
            with dissolve

            cl "Huh..."

            scene v15s21_6d
            with dissolve

            u "Ha, yeah. Well..."

        if v11_ride_with_mrlee: # -if MC took car journey with Mr. Lee in Europe (had scene 11.37a instead of 11.37b, didn't walk with Imre and Ryan) = (bonus correct_points +1)
            $ v15s21_meeting_points += 1

            scene v15s21_6d
            with dissolve

            u "Yeah, I think so. But, also..."

            show screen teacher_conviction_bar((v15s21_meeting_points + 4) * 10, "MR. LEE")

            u "I just wanted to say that, a wise man once taught me about the importance of personal responsibility."

            scene v15s21_6s
            with dissolve

            u "And, I think Chloe is taking huge responsibility in her Presidency role by using her influence to benefit others."

            scene v15s21_7k
            with dissolve

            cl "*Chuckles* Thank you, [name]."

            scene v15s21_6r
            with dissolve

            lee "Haha, very good, [name]."

            scene v15s21_6s
            with dissolve

            lee "I might be inclined to question the motives of your flattery, but I can see in your eyes that you're being sincere."

            scene v15s21_6r
            with dissolve

            u "*Laughs*"

            scene v15s21_6s
            with dissolve

            lee "You're a good student when you want to be."

            scene v15s21_6r
            with dissolve

            u "Honestly, the conversation we had in London has stuck with me. I appreciate it."

            scene v15s21_6s
            with dissolve

            lee "I'm happy to hear it."

            scene v15s21_7k
            with dissolve

            cl "*Whispers* I don't know what you guys are talking about..."

            scene v15s21_7c
            with dissolve

            u "Haha, it's nothing."

        scene v15s21_6d
        with dissolve

        u "I think we're all finished, then."

        scene v15s21_7
        with dissolve

        cl "Yeah. We've covered all the main points that we wanted to discuss."

        scene v15s21_7c
        with dissolve

        cl "I just have a paper here for you to sign, if you're willing to support our plans."

        scene v15s21_6e
        with dissolve

        pause 0.75

        scene v15s21_7
        with dissolve

        cl "Then I can just present it to the Dean when we meet with her."

        scene v15s21_5a
        with dissolve

        pause 0.75

        hide screen teacher_conviction_bar with dissolve

        hide screen v15_teacher_brief_icon

        if v15s21_meeting_points >= 5: #TBD optimal difficulty level
            if v15s21_meeting_points == 5 and kct == "loyal":
                call screen kct_popup
                
            scene v15s21_6
            with dissolve

            lee "Well..."

            scene v15s21_6r
            with dissolve

            lee "You're clearly passionate about this, and I'm convinced that both of your intentions are honest."

            scene v15s21_7
            with dissolve

            cl "Wait, so-"

            scene v15s21_7c
            with dissolve

            u "(We did it?!)"

            scene v15s21_6r
            with dissolve

            lee "You should be very proud. This was an excellent proposal."

            scene v15s21_5c # TPP. same as v15s21_5 MC is now sitting next to Chloe, Chloe and Mc look at each other and high five, both full smiles, both mouths open, Mr. Lee is still sitting down looking at Chloe, Still a slight smile, mouth is still closed
            with dissolve

            pause 0.75

        elif v15s21_meeting_points >= 3:
            scene v15s21_6
            with dissolve

            lee "Well, I'll be honest..."

            scene v15s21_6h
            with dissolve

            lee "You weren't 100% convincing throughout the meeting..."

            scene v15s21_7g
            with dissolve

            u "(Oh no...)"

            scene v15s21_6
            with dissolve

            lee "But you still did a very nice job."

            scene v15s21_7
            with dissolve

            cl "Really?!"

            scene v15s21_6
            with dissolve

            lee "Of course. You were both responsible individuals, who didn't waste my time, and made valid arguments."

            lee "You've earned my support."

            scene v15s21_5c
            with dissolve

            pause 0.75

        elif v15s21_meeting_points >= 1:
            if v15s21_meeting_points == 1 and kct == "loyal":
                call screen kct_popup
            
            scene v15s21_6h
            with dissolve

            lee "I can't say that I'm completely convinced..."

            scene v15s21_6c
            with dissolve

            lee "But I do believe that the two of you have good intentions, although you've chosen to communicate poorly today."

            scene v15s21_6b
            with dissolve

            u "I'm sorry, so..."

            scene v15s21_7a
            with dissolve

            cl "You'll sign?"

        else:
            scene v15s21_6h
            with dissolve

            lee "Oh, alright. Well..."

            lee "To be honest, I'm not fully satisfied. I can't tell your intentions are pure."

            scene v15s21_6b
            with dissolve

            u "(What?)"

            scene v15s21_6c
            with dissolve

            lee "I almost get the sense that you both need to do work on realigning your moral compasses."

            scene v15s21_6b
            with dissolve

            u "I'm sorry?"

            scene v15s21_7h
            with dissolve

            cl "So, you're not going to sign?"

            scene v15s21_6h
            with dissolve

            lee "On this occasion, no. I'm sorry to say I must decline."

            scene v15s21_6h
            with dissolve

            lee "But thank you for the meeting. It has been enlightening at the very least."

            scene v15s21_6t # FPP. same as v15s21_6h Mr. Lee stands up from his seat, still no expression, mouth is still open
            with dissolve

            lee "And I wish you good luck for your meeting with the Dean."

            scene v15s21_7g
            with dissolve

            cl "..."

            scene v15s21_6u # FPP. same as v15s21_6t Mr. Lee's mouth is closed, still standing up from his seat, still no expression
            with dissolve

            u "Thanks..."

            scene v15s21_5b # same as v15s21_5 Mr. Lee is walking away from the table, no expression, mouth is closed, Mc and Chloe are sitting at the table, looking at each other with confused expressions, both mouths are closed
            with fade

            pause 0.75

            jump v15s22 # -Transition to Scene 22-

        scene v15s21_6
        with dissolve

        lee "I'll sign the paper and all, but on one condition."

        scene v15s21_7l # FPP. same as v15s21_7a Chloe is looking at the teacher, still no expression, mouth is still open
        with dissolve

        cl "Umm, okay. What is it?"

        scene v15s21_6a
        with dissolve

        lee "I advise that you adjust your proposal, offering to dissolve the President's scholarship."

        scene v15s21_7h
        with dissolve

        cl "What-"

        scene v15s21_6
        with dissolve

        lee "The money used to cover your tuition, can go towards reducing the tuition fees for all Chicks."

        scene v15s21_6
        with dissolve

        lee "And the President, which is you in this circumstance..."

        scene v15s21_7h
        with dissolve

        cl "Yes..."

        scene v15s21_6
        with dissolve

        lee "From then on, you'll pay the same amount for tuition as all the other Chicks do."

        scene v15s21_7g
        with dissolve

        u "(Oh...)"

        scene v15s21_7h
        with dissolve

        cl "You're suggesting that I... give up my scholarship?"

        scene v15s21_6v # FPP. same as v15s21_6h Mr. Lee extends a hand out, palm up in an explainatory manner, still no expression, still looking at Chloe, mouth is still open
        with dissolve

        lee "You can't expect to have the best of both worlds, Chloe. The school is not made of money, we have to be smart about this financially."

        lee "Are you willing to give up your special privileges for the greater good of your peers?"

        scene v15s21_7h
        with dissolve

        cl "I mean... It's just-"

        scene v15s21_7m # FPP. same as v15s21_7a Chloe has a stressed expression, still looking at Mc, mouth is still closed
        with dissolve

        u "It's your decision, Chloe."

        scene v15s21_7n # FPP. same as v15s21_7m Chloe has a conflicted expression, looking away from mc and the teacher, mouth is still closed
        with dissolve

        cl "..."

        scene v15s21_7n
        with dissolve

        u "(Can she even afford to pay for tuition...?)"

        scene v15s21_7l
        with dissolve

        cl "Let's do it."

        scene v15s21_7f
        with dissolve

        u "You-"

        scene v15s21_6w # FPP. same as v15s21_6r Mr. Lee is looking at Chloe, still a full smile, mouth is still open
        with dissolve

        lee "Wonderful! What a bold decision, Chloe. I admire your bravery today."

        scene v15s21_7l
        with dissolve

        cl "Thank you, Mr. Lee."

        scene v15s21_7o # FPP. same as v15s21_7 Chloe mouth is open still has no expression, still looking at the teacher
        with dissolve

        u "..."

        scene v15s21_7p # FPP. same as v15s21_7b Chloe holds out a pen instead of the paper, no expression, mouth is still closed
        with dissolve

        pause 0.75

        scene v15s21_6x # FPP. same as v15s21_6e Mr. Lee is signing a paper from the paper Chloe gave him, looking at the paperwork, slight smile, mouth is open
        with dissolve

        lee "I shall make a note here of the conditions of my support..."

        lee "And lastly, my autograph! Haha."

        scene v15s21_7o
        with dissolve

        cl "Ha..."

        scene v15s21_7d
        with dissolve

        u "You okay?"

        scene v15s21_7q # FPP. same as v15s21_7d Chloe's mouth is open, still looking at mc with a nervous expression
        with dissolve

        cl "Umm... I-"

        scene v15s21_6y # FPP. same as v15s21_6x Mr. Lee hands the paper and pen back to Chloe, looking at Chloe, Full smile, mouth is open
        with dissolve

        lee "Here we are!"

        scene v15s21_7
        with dissolve

        cl "Thank you so much. I really appreciate your time today."

        scene v15s21_6s
        with dissolve

        u "Yeah, thanks for meeting with us Mr. Lee."

        scene v15s21_6z # FPP. same as v15s21_6t Mr. Lee has a full smile, still standing up from his seat, still looking at Mc
        with dissolve

        lee "You're both very welcome."

        lee "And I wish you the best of luck!"

        scene v15s21_5d # TPP. same as v15s21_5b Mr. Lee is looking at and waving goodbye to Chloe and Mc as he leaves, Mc and Chloe are looking at Mr. Lee, Everyone has a slight smile, and all mouths are closed
        with fade

        pause 0.75

        jump v15s22 # -Transition to Scene 22-

    else: # -if meeting Ms. Rose
        if kct == "confident":
            $ v15s21_meeting_points += 1

        $ animated_value_percent = (v15s21_meeting_points+4) * 100 / 11

        scene v15s21_8 # FPP. Ms. Rose enters the library, slight smile, mouth closed
        with dissolve

        pause 0.75

        scene v15s21_9 # FPP. Chloe and Mc are still sitting down in the library from renders created in v15s20, Chloe looks away from MC towards Ms. Rose walking into the library, Chloe slight smile, mouth open
        with dissolve

        cl "Here she comes, look alive."

        scene v15s21_10 # FPP. Ms. Rose approaches them slight smile mouth closed, Chloe and MC stand up, Chloe slight smile, mouth closed, Chloe looking at Ms. Rose
        with dissolve

        pause 0.75

        if v15_mad_at_ms_rose and not "v15_rose" in sceneList:
            scene v15s21_10a # FPP. same as v15s21_10 Ms. Rose and Chloe look at Mc, slight smiles, mouths closed
            with dissolve

            u "(I have to put my emotions to the side during this meeting, I can't let my anger get in the way.)"

        elif "v15_rose" in sceneList: # -if MC had kitchen sex with Ms. Rose
            scene v15s21_10a
            with dissolve

            u "(Don't think about sex, don't think about sex, don't think abou-)"

        $ opened_count = 0 # reset counter
        scene v15s21_10b # FPP. same as v15s21_10a Ms. Rose looking at Chloe slight smile mouth open, Chloe looking at Ms. Rose slight smile mouth closed
        with dissolve

        ro "Hi, Chloe. Hello [name]. It's nice to see you both."

        scene v15s21_10a
        with dissolve

        u "Hi, Ms. Rose."

        scene v15s21_10c # FPP. same as v15s21_10b Chloe's mouth is open, Ms. Rose's mouth is closed, both of them are still looking at each other with slight smiles
        with dissolve

        cl "Yes, hello! Thank you so much for agreeing to see me..."

        cl "If you'd like to follow me, I've set up a meeting room for us."

        scene v15s21_10b
        with dissolve

        ro "Oh! Very organized... Impressive."

        if ms_rose.relationship.value >= Relationship.FWB.value:
        
            scene v15s21_10d # FPP. Chloe is walking away with her back turned and can't see Mc or Ms. Rose, Ms. Rose is giving Mc a wink, slight smile, mouth closed
            with dissolve
            
            pause 0.75

        scene v15s21_11 # TPP. Show Chloe opening the door to a private room in the library, Ms. Rose walks into the room first followed by mc, all slight smiles, mouths closed
        with dissolve

        pause 0.75

        scene v15s21_12 # TPP. Show a table with at least 3 seats, Chloe sits on one side with an empty to her right for MC, Mr, Lee sits at a chair located on the other side of the table, slight smiles, mouths closed, Ms, Rose and Chloe are looking at each other.
        with dissolve

        pause 0.75

        show screen teacher_conviction_bar((v15s21_meeting_points + 4) * 100 / 11, "MS. ROSE")

        if ms_rose.relationship.value >= Relationship.FWB.value:
            $ v15s21_meeting_points += 2

            show screen teacher_conviction_bar((v15s21_meeting_points + 4) * 100 / 11, "MS. ROSE")

        scene v15s21_13 # FPP. Show Ms. Rose only looking at Chloe, slight smile, mouth open
        with dissolve

        ro "So, how can I help you two out today?"

        scene v15s21_7l
        with dissolve

        cl "As I'm sure you know, I'm being challenged for the presidency of the Chicks."

        scene v15s21_13a # FPP. same as v15s21_13 Ms. Rose has no expression, still looking at Chloe, mouth is still open
        with dissolve

        ro "Yes, I've heard it's been... quite a stormy time in the Chicks house lately."

        scene v15s21_13b # FPP. same as v15s21_13a Ms. Rose is looking at Mc, mouth is closed, still no expression
        with dissolve

        u "(That's one way to put it)"

        scene v15s21_7l 
        with dissolve

        cl "Right, and I want it all to be over. As soon as possible."

        scene v15s21_13a
        with dissolve

        ro "Very well."

        scene v15s21_7l
        with dissolve

        cl "So, I've thought of a proposal that I'd love to have your support on."

        scene v15s21_13b
        with dissolve

        menu:
            "Mention Nora":
                $ add_point(KCT.TROUBLEMAKER)
                $ v15s21_meeting_points -= 1

                scene v15s21_13a
                with dissolve

                u "I'm sure you're aware of the issues between Chloe and Nora at the moment, but-"

                scene v15s21_7f
                with dissolve

                cl "*Sighs*"

                scene v15s21_7r # FPP. v15s21_7f Chloe puts her head down in embarrassment, and covers her face with her hand, Chloe is still facing Mc
                with dissolve

                pause 0.75

                scene v15s21_13c # FPP. same as v15s21_13a Ms. Rose is looking at Mc, still no expression, mouth is still open
                with dissolve

                pause 0.75

                show screen teacher_conviction_bar((v15s21_meeting_points + 4) * 100 / 11, "MS. ROSE")

                ro "Personally, I think Nora has already made up her mind about Chloe's ability to lead."
                ro "And I'm not here to discuss that or take any part in the ongoing feud."

                scene v15s21_7l
                with dissolve

                cl "No, of course not. We can move on."

                scene v15s21_7s # FPP. same as v15s21_7a Chloe looks at Mc slightly angry, mouth is still closed
                with dissolve

                u "(Not off to a great start... Should've kept my mouth shut, fuck.)"

            "Stay quiet":
                $ add_point(KCT.BOYFRIEND)

                show screen teacher_conviction_bar((v15s21_meeting_points + 4) * 100 / 11, "MS. ROSE")

                scene v15s21_13b
                with dissolve

                u "(I'll keep quiet for now. It's best to not start out on the wrong foot.)"

        scene v15s21_13a
        with dissolve

        ro "Alright, you have my attention."

        scene v15s21_7
        with dissolve

        cl "You know how much I care about the Chicks, and I think with your support we could become bigger and better than ever before."

        scene v15s21_13
        with dissolve

        ro "Hmm... Well, I'm intrigued. What is your proposal?"

        scene v15s21_13d # FPP. same as v15s21_13 Ms. Rose has a very serious face, she's focused on Chloe, mouth is closed
        with dissolve

        u "(She is just... impossible to read.)"

        scene v15s21_7
        with dissolve

        cl "I would like to lower the cost of tuition for all Chicks, and with your signature I can take my proposal to the Dean."

        scene v15s21_13a
        with dissolve

        ro "Ha..."

        scene v15s21_13
        with dissolve

        ro "Well, that's certainly one way of bringing the peace back to the Chicks house."

        scene v15s21_7
        with dissolve

        cl "Yes, I... I hope so."

        scene v15s21_7
        with dissolve

        pause 0.75

        if v15_took_notes: # -a little journal icon appears, they can click on it AT ANY TIME during this scene and see the notes that they created in scene 20 with Chloe-
            scene v15s21_13f # FPP. v15s21_13 Ms, Rose looks at Mc, mouth is closed, still a slight smile
            with dissolve

            u "(Don't forget, I brought notes! We can refer to them whenever.)"

        else: # -they have no journal icon, no access to notes-
            scene v15s21_13f
            with dissolve

            u "(I hope I don't regret not bringing those notes.)"

        scene v15s21_13
        with dissolve

        ro "So I guess now all I'm wondering is, why do you want my support on this?"

        scene v15s21_13g # FPP. same as v15s21_13 Ms. Rose raises an eyebrow, still looking at Chloe, still a slight smile, mouth is still closed
        with dissolve

        ro "Why come to me, instead of someone like Mr. Lee?"

        scene v15s21_13f
        with dissolve

        u "(Oof, straight to the truth... Okay.)"

        scene v15s21_13c
        with dissolve

        ro "Did you both think that I'd be easier to persuade?"

        scene v15s21_7t # FPP. same as v15s21_7 Chloe is slightly scared, still looking at Ms. Rose, mouth is still open
        with dissolve

        cl "No, of course not! I mean, yes... I-"

        scene v15s21_7f
        with dissolve

        menu:
            "You understand sorority life":
                $ v15s21_meeting_points += 1
                $ add_point(KCT.BOYFRIEND)

                show screen teacher_conviction_bar((v15s21_meeting_points + 4) * 100 / 11, "MS. ROSE")

                scene v15s21_13b
                with dissolve

                u "We need the opinion of someone who understands the inner workings of sorority life."

                scene v15s21_13h # FPP. same as v15s21_13b Ms. Rose has a confused expression, still looking at Mc, mouth is still closed
                with dissolve

                u "Mr. Lee doesn't know what college is like for girls, or how it can be improved... Neither do I."

                u "Who better to ask than one of our female role models?"

                scene v15s21_7
                with dissolve

                cl "You're more sympathetic to our needs too, and basically just... awesome at supporting women, y'know?"

                scene v15s21_13i # FPP. same as v15s21_13 Ms. Rose has a full smile, still looking at Chloe, mouth is still open
                with dissolve

                ro "Haha... Well, I'm glad that you both feel that way. Thank you."

            "Mr. Lee doesn't listen":
                $ add_point(KCT.TROUBLEMAKER)
                $ v15s21_meeting_points -= 1

                show screen teacher_conviction_bar((v15s21_meeting_points + 4) * 100 / 11, "MS. ROSE")

                scene v15s21_13b
                with dissolve

                u "Mr. Lee only listens to what Mr. Lee wants to hear, he doesn't listen to opposing views."

                scene v15s21_13j # FPP. same as v15s21_13b Ms. Rose has a dissaproving expression, still looking at Mc, mouth is still closed
                with dissolve

                pause 0.75

                scene v15s21_7l
                with dissolve

                cl "We wanted to gain a female perspective."

                scene v15s21_13j
                with dissolve

                u "Right. Besides, he can be a bit harsh sometimes."

                scene v15s21_13c
                with dissolve

                ro "Hmm, I think both of you are underestimating Mr. Lee."

                scene v15s21_13a
                with dissolve

                ro "He's a brilliant man and... believe it or not, he's incredibly understanding of women in today's modern society."

                ro "I'm sure he would've been difficult to persuade on something like this, but he always stays considerate and fair."

                scene v15s21_7l
                with dissolve

                cl "Yeah. Of course."

        scene v15s21_13a
        with dissolve

        ro "Now, I have another question."

        scene v15s21_7
        with dissolve

        cl "We're happy to answer."

        scene v15s21_13a
        with dissolve

        ro "How do you think the other sororities and frats will react, if they hear the Chicks are getting special treatment with reduced tuition fees?"

        scene v15s21_7l
        with dissolve

        u "Well..."

        scene v15s21_7f
        with dissolve

        menu:
            "They'll be motivated":
                $ v15s21_meeting_points += 1
                $ add_point(KCT.BRO)
                $ add_point(KCT.BOYFRIEND)

                show screen teacher_conviction_bar((v15s21_meeting_points + 4) * 100 / 11, "MS. ROSE")

                scene v15s21_13b
                with dissolve

                u "It'd be like lighting a match underneath them."

                scene v15s21_7
                with dissolve

                cl "Ha, yeah. A wake-up call almost."

                scene v15s21_13
                with dissolve

                ro "How so?"

                scene v15s21_13f
                with dissolve

                u "I think it would motivate them to want to achieve similar goals as the Chicks when they see what kind of things Chloe can achieve."

                u "Hopefully people will begin to look at the Chicks and realize that these young women are ambitious, determined, and aren't afraid to try."

                scene v15s21_13k # FPP. same as v15s21_13i Ms. Rose is looking at Mc, mouth is closed, still a full smile
                with dissolve

                pause 0.75

                scene v15s21_7u # FPP. same as v15s21_7c Chloe has a full smile, still looking at Mc, mouth is still closed
                with dissolve

                pause 0.75

                scene v15s21_13l # FPP. same as v15s21_13f Ms. Rose's mouth is open, still looking at Mc, still has a slight smile
                with dissolve

                ro "Very well said, [name]."

                scene v15s21_7
                with dissolve

                cl "Girl power! *Giggles*"

                cl "Honestly though, we can be the first to lead the way on this, and all the others can meet with the Dean once I'm finished."

                scene v15s21_13
                with dissolve

                ro "Ha. Alright, noted."

            "They'll get over it":
                $ add_point(KCT.TROUBLEMAKER)
                $ v15s21_meeting_points -= 1

                show screen teacher_conviction_bar((v15s21_meeting_points + 4) * 100 / 11, "MS. ROSE")

                scene v15s21_13b
                with dissolve

                u "They can get over it. With all due respect, just because they didn't think of the idea, doesn't mean the idea should get turned down."

                scene v15s21_13c
                with dissolve

                ro "Yes, I agree... But like it or not, we have to consider how this decision affects everyone, not just how it affects the Chicks."

                scene v15s21_7l
                with dissolve

                cl "Of course."

                scene v15s21_13a
                with dissolve

                ro "We must be fair, always."

        scene v15s21_13a
        with dissolve

        ro "There is the matter of your scholarship, too. That's also something we need to factor in here."

        scene v15s21_7t
        with dissolve

        cl "How is my scholarship relevant to this?"

        scene v15s21_13a
        with dissolve

        ro "I think it is, considering you get a free ride, just for winning an election."

        scene v15s21_7l
        with dissolve

        cl "I guess..."

        scene v15s21_13
        with dissolve

        ro "Would you even consider sacrificing those special benefits as a bargaining chip?"

        scene v15s21_7l
        with dissolve

        cl "But that's not the plan that we-"

        scene v15s21_7l
        with dissolve

        ro "Right, but what's the phrase? \"All for one and one for all\"?"

        scene v15s21_7f
        with dissolve

        u "(Chloe sacrificing her free tuition for the sake of all of the Chicks?)"

        menu:
            "She shouldn't do that":
                $ add_point(KCT.TROUBLEMAKER)
                $ add_point(KCT.BOYFRIEND)

                $ v15s21_meeting_points -= 1

                show screen teacher_conviction_bar((v15s21_meeting_points + 4) * 100 / 11, "MS. ROSE")

                scene v15s21_13b
                with dissolve

                u "That's ridiculous, she shouldn't do that!"

                scene v15s21_13m # FPP. same as v15s21_13b Ms. Rose has a disapointed expression, still looking at Mc, mouth is still closed
                with dissolve

                u "Chloe can't afford to sacrifice her scholarship, so we can't even consider that."

                scene v15s21_13c
                with dissolve

                ro "So, that's a point-blank refusal? Because that's what's best for Chloe?"

                scene v15s21_7l
                with dissolve

                cl "*Scoffs*"

                scene v15s21_7d
                with dissolve

                pause 0.75

                scene v15s21_7l
                with dissolve

                cl "How could I..."

                cl "Even continue studying... without the scholarship?"

                scene v15s21_13a
                with dissolve

                ro "Unfortunately, Chloe... that's the only way I see the Dean going forward with this proposal."

                scene v15s21_7d
                with dissolve

                pause 0.75

            "Consider it":
                $ add_point(KCT.BRO)
                
                $ v15s21_meeting_points += 1

                show screen teacher_conviction_bar((v15s21_meeting_points + 4) * 100 / 11, "MS. ROSE")

                scene v15s21_13b
                with dissolve

                u "It would depend on all the details... What exactly would that mean?"

                scene v15s21_7d
                with dissolve

                pause 0.75

                scene v15s21_13l
                with dissolve

                ro "I have an idea, I'm just working it through in my head, but... it might work if you're willing to make sacrifices."

        scene v15s21_13b
        with dissolve

        u "Okay. Well..."

        if v15_took_notes and opened_count >= 5: # -if TookNotes and clicks on the journal five times-:
            scene v15s21_13k
            with dissolve

            $ grant_achievement("too_much_information")
            ro "[name], If you stare at your notes for too long, you're going to end up missing the meeting. *Chuckles*"

            scene v15s21_13f
            with dissolve

            u "(Oh, shit...) Sorry, Ms. Rose."

            scene v15s21_13k
            with dissolve

            ro "Just focus on the job at hand, young man."

            scene v15s21_13f
            with dissolve

            u "(Oh, I'm trying to.)"

        scene v15s21_13
        with dissolve

        ro "Is there anything else we need to talk about?"

        if v13_perfume: # -if MC gave Ms. Rose the perfume bottle gift in Amsterdam (had scene 13.57 instead of 13.57a) = (bonus correct_points +1)
            $ v15s21_meeting_points += 1

            scene v15s21_7l
            with dissolve

            cl "Not really, no. But..."

            scene v15s21_7
            with dissolve

            cl "What is that perfume that you're wearing? *Sniffs*"

            scene v15s21_13
            with dissolve

            ro "Haha... Excuse me?"

            scene v15s21_13f
            with dissolve

            u "*Laughs*"

            scene v15s21_7
            with dissolve

            cl "Sorry, it just smells amazing, I had to ask."

            scene v15s21_13
            with dissolve

            pause 0.75

            show screen teacher_conviction_bar((v15s21_meeting_points + 4) * 100 / 11, "MS. ROSE")

            ro "Oh, it's okay! Thank you. It was actually a gift that [name] and Nora gave to me before we left Europe."

            if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                $ chloeSus += 1

                scene v15s21_7v # FPP. same as v15s21_7s Chloe raises an eyebrow, still slightly angry, still lookng at mc, mouth is still closed
                with dissolve

                cl "Oh, really?"

            else:
                scene v15s21_7a
                with dissolve

                cl "Oh, really?"

            scene v15s21_13k
            with dissolve

            u "Oh yeah, ha. I'm glad you like it."

            scene v15s21_13n # FPP. same as v15s21_13k Ms. Rose's mouth is open, still a full smile, still looking at Mc
            with dissolve

            ro "Yes, I do! I get compliments every time."

            scene v15s21_13n
            with dissolve

            pause 0.75

        scene v15s21_7k
        with dissolve

        cl "I think that's it. Right, [name]?"

        scene v15s21_7c
        with dissolve

        u "Yeah. So, what do you think?"

        scene v15s21_13o # FPP. same as v15s21_13n Ms. Rose has a serious expression, still looking at Mc, mouth is still closed
        with dissolve

        pause 0.75

        hide screen teacher_conviction_bar with dissolve

        hide screen v15_teacher_brief_icon

        if v15s21_meeting_points >= 5: #TBD optimal difficulty level
            if v15s21_meeting_points == 5 and kct == "confident":
                call screen kct_popup
        
            scene v15s21_13i
            with dissolve

            ro "I have to say, you both answered my questions honestly, and there's not much more I can ask for."

            scene v15s21_13n
            with dissolve

            ro "I think you have good intentions, so I'm happy to support you."

            scene v15s21_7k
            with dissolve

            cl "*Gasps*"

            scene v15s21_7u
            with dissolve

            u "Holy shi-"

            scene v15s21_12b # TPP. same as v15s21_12 MC is now sitting next to Chloe, Chloe and Mc look at each other and high five, both full smiles, both mouths open, Ms. Rose is still sitting down looking at Chloe, Still a slight smile, mouth is still closed
            with dissolve

            pause 0.75

        elif v15s21_meeting_points >= 3:
            scene v15s21_13a
            with dissolve

            ro "I still have a few uncertainties when it comes to your intentions..."

            scene v15s21_7l
            with dissolve

            cl "*Sighs*"

            scene v15s21_13
            with dissolve

            ro "But you did well. This is a great plan, and well executed."

            scene v15s21_7l
            with dissolve

            cl "Wait, you're on board?!"

            scene v15s21_13i
            with dissolve

            ro "I am."

            scene v15s21_7u
            with dissolve

            u "(Yes!)"

            scene v15s21_12b
            with dissolve

            pause 0.75

        elif v15s21_meeting_points >= 1:
            if v15s21_meeting_points == 1 and kct == "confident":
                call screen kct_popup

            scene v15s21_13a
            with dissolve

            ro "I'm not sure if you're both just feeling nervous today, or whatever it is..."

            ro "Either way, I know how much you want this for the Chicks, I can see it."

            scene v15s21_7l
            with dissolve

            cl "I really do..."

            scene v15s21_13
            with dissolve

            ro "So I'm going to give you a fighting chance with the Dean."

            scene v15s21_13b
            with dissolve

            u "Oh my... Thank you."

            scene v15s21_7l
            with dissolve

            cl "Yes, I-"

            cl "Thank you. Thank you so much."

            scene v15s21_12b
            with dissolve

            pause 0.75

        else:
            scene v15s21_13p # FPP. same as v15s21_13o Ms. Rose has a disapointed expression, mouth is open, still looking at Chloe
            with dissolve

            ro "I'm sorry you guys."

            scene v15s21_13q # FPP. same as v15s21_13p Ms. Rose is looking at mc, mouth is closed, still a disapointed expression
            with dissolve

            u "*Sighs*"

            scene v15s21_13p
            with dissolve

            ro "I just don't think I can support you at this time, Chloe. It's disappointing to have to say that, but..."

            ro "I can't trust your true intentions here."

            scene v15s21_7h
            with dissolve

            cl "So, what? You're not going to sign?"

            scene v15s21_13p
            with dissolve

            ro "I can't support something I don't believe in. But good luck with it. Maybe the Dean will feel differently."

            scene v15s21_7h
            with dissolve

            cl "Ha... Okay."

            scene v15s21_13r # FPP. Same as v15s21_13a Ms. Rose stands up from her seat, still looking at Chloe, still has no expression, mouth is still closed
            with dissolve

            ro "Have a good day, you two."

            scene v15s21_13s # FPP. Same as v15s21_13r Ms. Rose is looking at Mc, mouth is closed, still standing, still no expression
            with dissolve

            u "Yeah, you as well."

            scene v15s21_7f
            with dissolve

            cl "*Sighs*"

            scene v15s21_12a # TPP. Same as Ms. Rose v15s21_12 is walking away from the table, no expression, mouth is closed, Mc and Chloe are sitting at the table, looking at each other with a concerned expression, both mouths are closed
            with dissolve

            pause 0.75

            scene v15s21_7f
            with fade

            pause 0.75

            jump v15s22 # -Transition to Scene 22-

        scene v15s21_13
        with dissolve

        ro "Now, here's exactly what I'm thinking."

        ro "Chloe, if you offer to sacrifice your scholarship, the money from that can be used towards reducing the fees for all Chicks."

        ro "You'll have to start paying something, yes, but it will be reduced. The same as all the other Chicks."

        scene v15s21_7d
        with dissolve

        pause 0.75

        scene v15s21_7l
        with dissolve

        cl "I just-"

        scene v15s21_7d
        with dissolve

        pause 0.75

        scene v15s21_7l
        with dissolve

        cl "I'm not sure I can give up my scholarship just like that."

        scene v15s21_7d
        with dissolve

        u "I know."

        scene v15s21_13a
        with dissolve

        ro "I think it's the only way forward, truly."

        ro "The Dean will have to consider the financial implications."
        ro "There's no point in me signing off my support if we can't afford to go through with it."

        scene v15s21_7w # FPP. same as v15s21_7a Chloe has a conflicted expression, still looking at MC, mouth is still closed
        with dissolve

        pause 0.75

        scene v15s21_7f
        with dissolve

        cl "..."

        scene v15s21_7l
        with dissolve

        cl "Okay..."

        scene v15s21_7f
        with dissolve

        u "Okay?!"

        scene v15s21_7l
        with dissolve

        cl "Let's try it."

        scene v15s21_7f
        with dissolve

        u "Chloe..."

        if ms_rose.relationship.value >= Relationship.FWB.value:
            u "(I won't feel great about it, but if I can get Chloe to give me a few moments alone with Ms. Rose...)"
            u "(...I might be able to get exactly what we want from her. No special conditions.)"

            menu:
                "Ask Chloe for privacy":
                    $ add_point(KCT.BOYFRIEND)
                    $ add_point(KCT.BRO)

                    scene v15s21_7x # FPP. same as v15s21_7a MC moves closer to Chloe to speak quietly, mouth is still closed, Chloe still looking at Mc, still no expression
                    with dissolve

                    u "*Whispers* Okay, this might sound weird, but... trust me, okay?"

                    scene v15s21_7y # FPP. same as v15s21_7x Chloe's mouth is open, Mc and Chloe are still close, Chloe still looking at Mc, still no expression
                    with dissolve

                    cl "Okay...?"

                    scene v15s21_7x
                    with dissolve

                    u "*Whispers* Can you leave me alone with Ms. Rose for a few minutes? I think there's a way you can keep your scholarship."

                    scene v15s21_7y
                    with dissolve

                    cl "That's... a weird request, [name]. *Nervous chuckles*"

                    scene v15s21_7x
                    with dissolve

                    u "I know. Trust me."

                    if kct == "popular" or chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                        if chloe.relationship.value < Relationship.GIRLFRIEND.value:
                            call screen kct_popup

                        scene v15s21_7y
                        with dissolve

                        cl "Okay, I trust you."

                        scene v15s21_7l
                        with dissolve

                        cl "Please, excuse me for a minute, Ms. Rose. I'm just going to run to the restroom."

                        scene v15s21_13
                        with dissolve

                        ro "Oh, sure. No problem."

                        scene v15s21_12c # TPP. same as v15s21_12 Chloe is walking away from the table no expression mouth is closed Leaving behind a pen and paper on the desk, Ms. Rose is still sitting in her same seat, Mc has now sat down in the seat intended for him on right across from Ms. Rose, Chloe's seat is empty, Ms. Rose and Mc are looking at each other slight smiles, mouths are closed
                        with dissolve

                        pause 0.75

                        scene v15s21_14 # FPP. Show Chloe exiting the Private room and shutting the door, no expression, mouth is closed
                        with dissolve

                        pause 0.75

                        scene v15s21_13f
                        with dissolve

                        u "(Okay, how do we want to do this?"

                        scene v15s21_13t # FPP. same as v15s21_13n Show Ms. Rose looking at Mc seductively, slightly biting a finger
                        with dissolve

                        u "(Seduce her the easy way, or...?)" 
                        
                        scene v15s21_13u # FPP. same as v15s21_13t Render looks exactly like v15s21_13t except instead of a seductive expression, Ms. Rose has a concerned expression
                        with dissolve

                        u "(Should we take this relationship to a new... dark, level? *Chuckles*)"

                        scene v15s21_13f
                        with dissolve

                        menu:
                            "Seduce Ms. Rose":
                                $ v15_seduce_ms_rose = True
                                $ add_point(KCT.BRO)
                                
                                if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                                    $ add_point(KCT.TROUBLEMAKER)
                                else:
                                    $ add_point(KCT.BOYFRIEND)

                                scene v15s21_13f
                                with dissolve

                                u "Lorraine... We really need you to sign the paper, without it affecting Chloe's scholarship."

                                scene v15s21_13l
                                with dissolve

                                ro "Of course you do, [name]... *Laughs* But, I don't think that's the right way to go."

                                scene v15s21_13f
                                with dissolve

                                u "Y'know... I'd be truly grateful if, just this once... you went along with it."

                                scene v15s21_13v # FPP. same as v15s21_13f Ms. Rose smirks, still looking at Mc, mouth is still closed
                                with dissolve

                                pause 0.75

                                scene v15s21_13n
                                with dissolve

                                ro "Oh... Really?"

                                scene v15s21_13k
                                with dissolve

                                u "Mhmm..."

                                scene v15s21_13x # FPP. same as v15s21_13t Ms. Rose's mouth is open, still with a finger on her lip, stll looking at Mc seductively
                                with dissolve

                                ro "How grateful are we talking?"

                                scene v15s21_13t
                                with dissolve

                                u "How about..."

                                u "I'll do whatever you want."

                                scene v15s21_13y # FPP. same as v15s21_13t Ms. Rose lowers her finger to just below her lips and bites her lips, rolls her eyes in excitement
                                with dissolve

                                pause 0.75

                                scene v15s21_13t
                                with dissolve

                                u "You name it."

                                scene v15s21_13n
                                with dissolve

                                ro "Hmm, that could take a while. *Laughs*"

                                scene v15s21_13k
                                with dissolve

                                u "Good. I can't wait to hear what you ask for."

                                scene v15s21_13n
                                with dissolve

                                ro "Ha..."

                                scene v15s21_13z # FPP. same as v15s21_13n Ms. Rose blushes, still looking at Mc, still full smile, mouth is still open
                                with dissolve

                                ro "[name], stop... You're making me horny."

                                scene v15s21_15 # TPP. Show Ms. Rose sitting in her chair from previous renders, Mc is standing above her, and pulls her in for a passionate kiss
                                with dissolve

                                pause 0.75

                                scene v15s21_15a # TPP. same as v15s21_15 Ms. Rose and Mc are no longer kissing, Ms. Rose grasps Mc's shirt and pulls him close to whisper in his ear her mouth is open, Mc looks proud of himself mouth is closed
                                with dissolve

                                ro "Such a naughty boy, [name]! *Chuckles*"

                                scene v15s21_15b # TPP. same as v15s21_15a Everything is the same except Ms. Rose's mouth is closed and Mc's mouth is open
                                with dissolve

                                u "Ha, yeah, maybe."

                                scene v15s21_12d # FPP. same as v15s21_12c Chloe is no longer in the render, Ms. Rose is looking at Mc seductively, still sitting down, Mc is pulling out his chair to sit down looking at Ms. Rose with a smug expression.
                                with dissolve

                                pause 0.75

                                scene v15s21_13l
                                with dissolve

                                ro "So..."

                                scene v15s21_13n
                                with dissolve

                                ro "Anything I want?"

                                scene v15s21_13k
                                with dissolve

                                u "Yeah. Anything."

                                scene v15s21_13za # FPP. same as v15s21_13k Ms. Rose appears to be thinking, still smiling, still facing Mc, mouth is still closed
                                with dissolve

                                pause 0.75

                                scene v15s21_13n
                                with dissolve

                                ro "Deal."

                                scene v15s21_13zb # FPP. same as v15s21_13k Ms. Rose is signing her name to the paperwork Chloe left behind in render v15s21_12c, looking at the paperwok, still smiling, mouth is still closed
                                with dissolve

                                pause 0.75

                                scene v15s21_12e # FPP. Same as v15s21_12d Ms. Rose is walkng away waving and looking back at Mc smiling mouth is open, Mc is sitting down looking at Ms. Rose smug expression, Chloe is still not in the render
                                with fade

                                ro "I'll see you soon, handsome."

                                jump v15s22 # -Transition to Scene 22-

                            "Threaten Ms. Rose":
                                $ v15_threaten_ms_rose = True
                                $ ms_rose.relationship = Relationship.THREATEN
                                $ add_point(KCT.TROUBLEMAKER)

                                scene v15s21_13f
                                with dissolve

                                $ grant_achievement("emotional_blackmail")
                                u "Lorraine, look..."

                                scene v15s21_13b
                                with dissolve

                                u "We really need your signature in support of this whole thing, and I can't allow Chloe to give up her scholarship for the sake of it."

                                scene v15s21_13c
                                with dissolve

                                ro "I can't support that, [name]. I think I'm being fair with what I'm suggesting."

                                scene v15s21_13b
                                with dissolve

                                u "Okay, I don't feel great about saying this..."

                                u "But if you can't support what I'm asking..."

                                u "I'm not sure how much longer I can stay quiet about our relationship."

                                scene v15s21_13zc # FPP. same as v15s21_13b has a scared/shocked expression, holding a hand over her mouth, still looking at Mc
                                with dissolve

                                pause 0.75

                                scene v15s21_13zd # FPP. same as v15s21_13zc Ms. Rose has lowered her hand, she has a sad/scared expression, mouth is open, still looking at Mc
                                with dissolve

                                ro "What...?"

                                scene v15s21_13ze # FPP. same as v15s21_13zd Ms. Rose's mouth is closed, still a sad/scared expression, still looking at Mc
                                with dissolve

                                u "You heard me. It's quite simple."

                                scene v15s21_13zd
                                with dissolve

                                ro "You... wouldn't."

                                ro "It would ruin everything, I'd-"

                                ro "I'd lose my job, [name]. It would ruin my life."

                                scene v15s21_13zf # FPP. same as v15s21_13ze Ms. Rose has her hands clasped together and appears to be pleading with MC not to go through with his actions, still looking at Mc, still a sad/scared expression, mouth is still closed
                                with dissolve

                                pause 0.75

                                scene v15s21_13ze
                                with dissolve

                                u "It would. You're right."

                                scene v15s21_12f # FPP. same as v15s21_12d MC is standing next to Ms. Rose looking down at her with a bold expression, holding a pen out towards her and pushing paperwork towards her, his mouth is closed, Ms. Rose is still sitting down, looking up at Mc with a scared expression, mouth is closed
                                with dissolve

                                pause 0.75

                                scene v15s21_12g # FPP. same as v15s21_12f Mc's mouth is open, everything else is the same
                                with dissolve

                                u "And all I want is a tiny little signature."

                                scene v15s21_12f
                                with dissolve

                                pause 0.75

                                scene v15s21_12h # FPP. same as v15s21_12f Ms. Rose's mouth is open, everything else is the same
                                with dissolve

                                ro "Ha..."

                                scene v15s21_12g
                                with dissolve

                                u "It's not too much to ask for, is it?"

                                scene v15s21_16 # FPP. Ms. Rose is sitting in her chair turned away from the table and now facing Mc, she looks extremely sad, trying not to look at Mc, mouth is closed
                                with dissolve

                                pause 0.75

                                scene v15s21_16a # FPP same as v15s21_16 Ms. Rose's mouth is open, still tryng to avoid eye contact with Mc, still extremely sad, still sitting down
                                with dissolve

                                ro "[name]...?"

                                scene v15s21_16b # FPP. same as v15s21_16a Ms. Rose is looking directly at MC, mouth is closed, still sitting down, still extremly sad
                                with dissolve

                                pause 0.75

                                scene v15s21_16c # FPP. same as v15s21_16b Ms. Rose's mouth is open, she has now started crying extremely, she is still looking directly at Mc, she is still sitting down
                                with dissolve

                                ro "I can't believe you're doing this."

                                scene v15s21_16d # FPP. same as v15s21_16c Ms. Rose's mouth is closed, still crying, still looking at MC, still sitting down
                                with dissolve

                                u "(Fuck... Me neither...)"

                                scene v15s21_16c
                                with dissolve

                                ro "..."

                                scene v15s21_16e # FPP. same as v15s21_16c Ms. Rose wipes away her tears, mouth is open, not looking at Mc, still sitting down
                                with dissolve

                                ro "*Sniffles* Fine."

                                scene v15s21_12i # TPP. same as v15s21_12f Ms. Rose takes the paper and pen from Mc and signs it, Ms. Rose has a extremely sad/defeated expression looking at the paperwork mouth is closed, Mc now has a concerned expression, still standing next to Ms. Rose still looking at Ms. Rose his mouth is still closed
                                with dissolve

                                pause 0.75

                                scene v15s21_12j # TPP. same as v15s21_12i Ms. Rose stands up and shoves the pen and paperwork into Mc's chest avoiding eye contact with Mc and walks away mouth is closed, Mc has a shocked expression, looking at Ms. Rose as she walks away, still standing up
                                with dissolve

                                pause 0.75

                                scene v15s21_17 # TPP. close up shot of Mc with a shameful expression, mouth is open
                                with dissolve

                                u "*Sighs*"

                                u "Holy shit... What did I just do?"

                                scene v15s21_17a # TPP. same as v15s21_17 Mc holds his hand to cover the shame in his face
                                with fade

                                pause 0.75

                                jump v15s22 # -Transition to Scene 22-

                    else:
                        scene v15s21_7a
                        with dissolve

                        cl "*Whispers* I don't think she's not going to change her mind, okay? Let's just get her signature and leave."

                        scene v15s21_7f
                        with dissolve

                        u "(Yeah, let's not rock the boat any more... We got the signature, that's what we came for.)"

                "Don't mention it":
                    $ add_point(KCT.BRO)

                    scene v15s21_7f
                    with dissolve

                    u "(Yeah, let's not rock the boat any more... We got the signature, that's what we came for.)"

        scene v15s21_7
        with dissolve

        cl "Thank you, Ms. Rose."

        scene v15s21_13
        with dissolve

        ro "No, Chloe. Thank you. This is extremely brave and selfless of you, I'm proud."

        scene v15s21_7z # FPP. same as v15s21_7b Chloe holds out a pen as well as the paper towards the teacher, still a slight smile, mouth is still closed
        with dissolve

        pause 0.75

        scene v15s21_13zg # FPP. same as v15s21_13 Ms. Rose is now holding the paper and pen from render v15s21_7z, still looking at Chloe, still a slight smile, mouth is still open
        with dissolve

        ro "I'll just add something about what we've agreed."

        scene v15s21_7u
        with dissolve

        pause 0.75

        scene v15s21_13zh # FPP. same as v15s21_13zg Ms. Rose is signing the paperwork, looking at the paperwork, still a slight smile, mouth is still open
        with dissolve

        ro "And... there. Signed!"

        scene v15s21_13zi # FPP. same as v15s21_13zg Ms. Rose hands the paperwork and pen towards Chloe's direction, slight smile mouth is closed
        with dissolve

        pause 0.75

        scene v15s21_7
        with dissolve

        cl "You're the best. Really."

        scene v15s21_13f
        with dissolve

        u "Yeah, thanks for that."

        scene v15s21_13zj # FPP. same as v15s21_13 Ms. Rose stands up from her seat, still has a slight smile, still looking at Chloe, mouth is still open
        with dissolve

        ro "Any time, I'm always happy to help."

        ro "I hope your meeting with the Dean goes well."

        scene v15s21_7
        with dissolve

        cl "Thank you!"

        scene v15s21_12k # FPP. same as v15s21_12a Ms. Rose is walking away and waving goodbye to Mc and Chloe, Mc and Chloe are looking at Ms. Rose slight smiles mouths are closed, Mc and Chloe are still sitting down still sitting down
        with fade

        pause 0.75

        jump v15s22 # -Transition to Scene 22-