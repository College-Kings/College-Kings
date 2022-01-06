# SCENE 48: Talking to Nora
# Locations: Nora's Cabin
# Characters: MC (Outfit: 1), NORA (Outfit: 1)
# Time: Evening

label v15s48:
    scene v15s48_1 # TPP. Show the cab showing up on a dirt road near the cabin, the cabin shown in the distance.
    with fade

    pause 0.75

    play sound "sounds/cardooropen.mp3"

    scene v15s48_2 # TPP. Show MC getting out of the cab on the road near the cabin, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s48_3 # TPP. Show the Cab driving off.
    with dissolve

    pause 0.75

    scene v15s48_4 # TPP. Shot from behind MC of him looking at all the forest near the cabin, slight smile, mouth closed.
    with dissolve

    u "(No wonder she wanted to hide out here. It's amazing!)"

    scene v15s48_5 # TPP. Show MC further down the road walking towards the cabin, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s48_6 # TPP. Show MC walking up to the front door of the cabin, slight smile, mouth closed.
    with fade

    pause 0.75

    scene v15s48_7 # FPP. MC looking through a window near the door of the cabin showing Nora on her knees with her back to MC with the fireplace warming her hands.
    with dissolve

    u "(There she is!) We found her."

    play sound "sounds/dooropen.mp3"

    scene v15s48_8 # TPP. Show MC entering the Cabin as he opens the door, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s48_9 # TPP. Show MC closing the door of the Cabin once he is inside, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s48_10 # FPP. Nora turned around looking at MC while on her knees. MC looking at Nora. Nora confused, mouth open.
    with dissolve

    no "[name]...? What the hell are you doing here?"

    scene v15s48_10a # FPP. Nora starting to stand up, MC looking at Nora, Nora confused, mouth closed.
    with dissolve

    pause 0.75

    scene v15s48_10b # FPP. Nora standing up looking at MC, MC looking at Nora, Nora confused, mouth closed.
    with dissolve

    menu:
        "I came to find you":
            $ add_point(KCT.BRO)
            
            scene v15s48_11 # TPP. MC walking closer to Nora, MC slight smile, mouth closed, Nora confused, mouth closed.
            with dissolve

            pause 0.75

            scene v15s48_12 # FPP. Nora standing infront of MC,Nora looking at MC, MC looking at Nora, Nora confused, mouth closed.
            with dissolve

            u "What do you think? I've been looking everywhere for you!"

            u "None of us knew if you were dead or alive or-"

            scene v15s48_12a # FPP. Nora looking at MC, MC looking at Nora, Nora confused, mouth open.
            with dissolve

            no "You can call off the search party. I'm fine."

        "Hug her":
            $ add_point(KCT.BOYFRIEND)
            
            scene v15s48_11
            with dissolve

            pause 0.75

            scene v15s48_13 # TPP. MC hugging Nora, Nora not hugging back but accepting the hug, slight smile, mouth closed, MC slight smile, mouth closed.
            with dissolve

            pause 0.75

            if nora.relationship.value >= Relationship.FWB.value:
                scene v15s48_13a # TPP. MC hugging Nora, Nora hugging MC back, Nora's eyes closed, Nora flirty, mouth open, MC slight smile, eyes's closed, mouth closed.
                with dissolve
               
                no "Ha... Hi. Did you miss me?"

                scene v15s48_13b # TPP. MC hugging Nora, Nora hugging MC back, Nora's eyes closed, Nora flirty, mouth closed, MC slight smile, eye's closed, mouth open.
                with dissolve

                u "Are you kidding? Of course I did. Everyone does!"

            else:
                scene v15s48_13  # TPP. MC hugging Nora, Nora not hugging back but accepting the hug, slight smile, mouth open, MC slight smile, mouth closed.
                with dissolve

                no "Oh, um... Hey there."

                scene v15s48_13d # TPP. MC hugging Nora, Nora not hugging back but accepting the hug, slight smile, mouth closed, MC slight smile, mouth open.
                with dissolve

                u "Hey there?"

    scene v15s48_12b # TPP. Nora looking at MC, MC looking at Nora, Nora slight smile, mouth closed.
    with dissolve

    u "What are you doing out here, Nora?"

    scene v15s48_12c # TPP. Nora looking at MC, MC looking at Nora, Nora slight smile, mouth open.
    with dissolve

    no "Am I not allowed to get away for a few days? Enjoy some peace and quiet?"

    scene v15s48_12b
    with dissolve

    u "Yeah, of course you can, but..."

    u "Going completely off the radar without telling anyone?"

    scene v15s48_12c
    with dissolve

    no "I didn't know I had to tell anyone I was going away. I'm an adult, [name]."

    scene v15s48_12b
    with dissolve

    u "No shit you're an adult."

    u "Which is why people expected to hear from you."

    u "Nobody's seen you or heard from you in days. We tried to call, we tried to text-"

    scene v15s48_12c
    with dissolve

    no "I turned my phone off."

    scene v15s48_12b
    with dissolve

    u "Why?"

    u "What are you running from?"

    scene v15s48_12d # TPP. Nora looking at MC, MC looking at Nora, Nora neutral, mouth open.
    with dissolve

    no "Nothing!"

    no "I'm not running from anything!"

    no "It just..."

    no "It all became way too real, after we landed. I needed time to..."

    scene v15s48_12e # TPP. Nora looking at MC, MC looking at Nora, Nora neutral, mouth closed.
    with dissolve

    menu:

        "Cool off":
            $ add_point(KCT.TROUBLEMAKER)

            u "Cool off."

            scene v15s48_12d # TPP. Nora looking at MC, MC looking at Nora, Nora neutral, mouth open.
            with dissolve

            no "Yeah... No, it's more about healing, you know?"

            scene v15s48_12e
            with dissolve

        "Heal":
            $ add_point(KCT.BRO)

            scene v15s48_12e
            #with dissolve

            u "Heal."

            scene v15s48_12c # TPP. Nora looking at MC, MC looking at Nora, Nora neutral, mouth open.
            with dissolve

            no "Yeah... exactly."

            scene v15s48_12b
            with dissolve

        "Stay quiet":
            $ add_point(KCT.BOYFRIEND)

            scene v15s48_12d
            with dissolve

            no "To heal."

            scene v15s48_12e
            with dissolve

    u "*Sighs* I'm sorry."

    scene v15s48_12c
    with dissolve

    no "You were worried, I get it... I should've at least told someone."

    scene v15s48_12b
    with dissolve

    u "You think?"

    no "..."

    u "We've all been thinking about you."

    scene v15s48_12c
    with dissolve

    no "I appreciate that."

    no "To tell you the truth, it is nice to see a friendly face."

    no "Come sit, I'll make you a tea. Do you have time?"

    if nora.relationship.value >= Relationship.FWB.value:
        scene v15s48_12b
        with dissolve

        u "We have all the time in the world."

        scene v15s48_12f # FPP. Nora's face closer to MC's as she caresses his cheek, Nora flirty, mouth closed.
        with dissolve

        pause 0.75

    else:
        scene v15s48_12b
        with dissolve

        u "Plenty. *Laughs*"

    scene v15s48_14 # TPP. MC sitting on the couch in the Cabin, Nora approaching the Couch coming from the kitchen area holding two cup's of tea, Nora slight smile, mouth closed, MC slight smile, mouth closed.
    with fade 

    pause 0.75

    scene v15s48_15 # TPP. MC sitting on the couch, Nora starting to sit on the couch while handing MC one of the cups, MC grabbing the cup, Nora slight smile, mouth closed, MC slight smile, mouth closed.
    with dissolve
    
    pause 0.75

    scene v15s48_16 # FPP. Sitting on the couch, Nora on the seat next to him, MC drinking the tea.
    with vpunch

    u "Ah fuck-"

    scene v15s48_17 # FPP. MC looking down at his hand holding his tea.
    with dissolve

    u "Shit, shit, shit! That's hot!"

    scene v15s48_18 # FPP. MC looking at Nora, Nora looking at MC, Nora slight smile, mouth open.
    with dissolve

    no "*Giggles* Sorry! I told you it was tea, you idiot..."

    no "My aunt always leaves loads of food whenever she stays here, and she makes sure to keep it stocked with my favorite tea."

    scene v15s48_16
    with dissolve

    u "Ooh, yeah..."

    scene v15s48_18
    with dissolve

    no "Haha, right?"

    scene v15s48_18a # FPP. MC looking at Nora, Nora looking at Mc, Nora slight smile, mouth closed.
    with dissolve

    u "It's like, strawberry flavor...?"

    scene v15s48_18
    with dissolve

    no "Yeah, exactly."

    scene v15s48_19 # TPP. Close up of just Nora drinking her tea, eyes closed.
    with dissolve

    pause 0.75

    scene v15s48_18 
    with dissolve

    no "I love it."

    scene v15s48_18a
    with dissolve

    u "So, you've been doing okay here on your own?"

    scene v15s48_18
    with dissolve

    no "Yeah, I've certainly had a lot of time to think."

    no "And nature gives your mind a chance to reset, you know?"

    scene v15s48_18a
    with dissolve

    u "Yeah. Especially this place. It's stunning."

    scene v15s48_18
    with dissolve

    no "Hah! My dad would love to hear that. He hates this old thing. Only keeps it out here for me, I think. *Chuckles*"

    scene v15s48_18a
    with dissolve

    u "Sounds like something a dad would do."

    scene v15s48_18b # FPP. MC looking at Nora, Nora looking at Mc, Nora neutral face, mouth open.
    with dissolve

    no "I've been reflecting on my past, with Chris."

    no "I was so... Unprioritized...?"

    scene v15s48_18c # FPP. MC looking at Nora, Nora looking at Mc, Nora neutral face, mouth closed.
    with dissolve

    u "That's a word..."

    scene v15s48_18
    with dissolve

    no "*Giggles* It is, yes..."

    no "For so long, I wasn't his world. I was just living in it."

    no "And at first, I felt so stupid..."

    scene v15s48_18a
    with dissolve

    menu:
        "You're not stupid":
            $ add_point(KCT.BOYFRIEND)
            $ v15s48_interrupt = True

            u "You're not stupid. Every one of-"

            scene v15s48_18
            with dissolve

            no "I know. Thank you, but... Let me finish."

            scene v15s48_18a
            with dissolve

            u "Yeah, sorry."

        "Don't interrupt":
            $ add_point(KCT.BRO)
            
            u "(I think she just needs someone to listen.)"

            scene v15s48_18
            with dissolve

            no "But not anymore."

    scene v15s48_18f
    with dissolve

    no "Chris wasn't my forever. I'm not stupid, because I tried."

    no "I'm not stupid, because I'm loyal."

    if "v12_nora" in sceneList:
        scene v15s48_18a
        with dissolve

        u "(Eh... Loyal? Not sure about that one... Haha.)"

        scene v15s48_18f
        with dissolve

    no "I'm not stupid, because I know my worth."

    no "You know?"

    scene v15s48_18a
    with dissolve

    u "Oh, I know."

    scene v15s48_18
    with dissolve

    no "*Laughs* I just mean-"

    scene v15s48_18a
    with dissolve

    u "You did nothing wrong."

    scene v15s48_18
    with dissolve

    no "I don't think I did either... I, honestly, gave everything I could to someone who was unworthy."

    no "And now, I'm fine."

    scene v15s48_18a
    with dissolve

    u "You are?"

    scene v15s48_18f # FPP. Nora looking at MC, MC looking at Nora, Nora studying MC, mouth open.
    with dissolve

    no "Yeah. I am. I'm fine, because... I still have me."

    scene v15s48_18a
    with dissolve

    menu:
        "And me":
            $ add_point(KCT.BOYFRIEND)

            u "And me."

            u "And a ton of others, who are like... Reaaally pissed at you right now, so..."

            scene v15s48_18
            with dissolve

            no "Right, right... *Chuckles* I have what I need."

        "You're pretty great to have":
            $ add_point(KCT.BRO)

            scene v15s48_18a
            #with dissolve

            u "You're pretty great to have."

            scene v15s48_18
            with dissolve

            no "Haha, thank you."

    scene v15s48_18a
    with dissolve

    u "So, what's next for Nora?"

    scene v15s48_18
    with dissolve

    no "Who knows? Haha."

    no "I'll most definitely focus on school."

    scene v15s48_16
    with dissolve

    pause 0.5

    scene v15s48_18
    with dissolve

    no "Probably stay single for a while..."

    if nora.relationship.value >= Relationship.FWB.value:
        scene v15s48_16
        with vpunch

        u "*Chokes* (Single?!)"

        u "Agh... *Coughs*"

        scene v15s48_18
        with dissolve

        no "*Giggles* You okay over there?"

        scene v15s48_18a
        with dissolve

        u "*Coughs* Ahem! Yes, I-"

        u "Excuse me..."

        scene v15s48_18
        with dissolve

        no "Was it something I said?"

        scene v15s48_18g # FPP. Nora looking at MC, MC looking at Nora, Nora smirking, mouth closed.
        with dissolve

        u "Ha... Maybe?"

        scene v15s48_18
        with dissolve

    else:
        scene v15s48_18a
        with dissolve

        u "Oh yeah? Gonna play the field a little?"

        scene v15s48_18
        with dissolve

        no "Pfft, no. Not in the slightest, haha."

    no "I'm just not sure what's best for me right now."

    scene v15s48_18a
    with dissolve

    u "(Gotta be careful here... Should we nudge her in the right direction?)"

    u "No matter what, you should do what makes you happy. But if you want my advice..."

    menu:
        "Follow your heart":
            $ add_point(KCT.BOYFRIEND)
            $ v15s48_follow_your_heart = True

            u "You should follow your heart. Whatever direction you're being pulled in, you should head there."

            scene v15s48_18
            with dissolve

            no "My heart is telling me to find real love."

            if nora.relationship.value >= Relationship.FWB.value:
                no "And to give it a chance."

            scene v15s48_18a
            with dissolve

            u "And?"

            scene v15s48_18
            with dissolve

            no "*Sighs*"

        "Listen to your head":
            $ add_point(KCT.BRO)
            
            scene v15s48_18a
            #with dissolve

            u "Listen to that little voice inside your head. What is she telling you to do?"

            if nora.relationship.value >= Relationship.FWB.value:
                scene v15s48_18f
                with dissolve
                
                pause 0.75

            scene v15s48_18
            with dissolve

            no "She's telling me to focus on me."

            no "Only me."

            scene v15s48_18a
            with dissolve

            u "And?"

            scene v15s48_18
            with dissolve

            no "I've never given that a try, I guess... Haha."

    no "I think I just feel a little guilty."

    scene v15s48_18a
    with dissolve

    u "For what?"

    scene v15s48_18
    with dissolve

    no "Moving on so quickly? Picking up, coming back, and acting like myself again?"

    scene v15s48_18a
    with dissolve

    menu:
        "You're not hurting anyone":
            $ add_point(KCT.BOYFRIEND)
            
            u "I understand you're afraid to upset people. You're done with the drama, yeah?"

            scene v15s48_18
            with dissolve

            no "So done. Beyond done. Haha..."

            no "I'm ready to move on."

            scene v15s48_18a
            with dissolve

            u "Then you do that, and you're not going to hurt anyone in the process of being happy."

            scene v15s48_18
            with dissolve

            no "Okay. You're right."

            if kct == "confident":
                scene v15s48_18a
                with dissolve

                u "I know. *Laughs*"

        "Don't worry about hurting Chris":
            $ add_point(KCT.TROUBLEMAKER)
            
            u "Okay, forgive me if I upset you, but..."

            if "chris_amber" in freeroam13 or "chris_penelope" in freeroam14:
                u "Chris tried his luck with a few people at Lauren's birthday party, and-"

                scene v15s48_18
                with dissolve

                no "Haha! You're kidding."

                if "chris_amber" in freeroam13 and "chris_penelope" in freeroam14:
                    scene v15s48_18a
                    with dissolve

                    u "Nope. In fact, I had to save both of them from him."

                else:
                    scene v15s48_18a
                    with dissolve

                    u "Nope. In fact, I had to save them from him."

                if "chris_amber" in freeroam13 and "chris_penelope" in freeroam14:
                    scene v15s48_18
                    with dissolve

                    no "*Laughs* Both?! Oh my god..."

                else:
                    scene v15s48_18
                    with dissolve

                    no "*Laughs* Oh my god..."

                no "Okay, fine. *Giggles* I don't feel guilty anymore."

                scene v15s48_18a
                with dissolve

                u "Haha, good!"

            else:
                u "Chris let go of an amazing human being, and that fucking sucks."

                u "For him."

                u "What's the point in wasting any more of your time worrying about him? Focus on you."

                scene v15s48_18
                with dissolve

                no "Wow, okay..."

                no "You're not wrong. *Sighs*"

    if nora.relationship.value < Relationship.FWB.value and not kct == "confident" and not (v15s48_follow_your_heart and not v15s48_interrupt):
        call screen kct_popup(required_kct="confident")

        if v15s48_follow_your_heart:
            scene v15s48_18
            with dissolve

            no "Well, cheers to following your heart! Actually-"

            no "I think we have wine... Be right back!"
            
        else:
            scene v15s48_18
            with dissolve

            no "Well, listening to the voices inside of our heads... Cheers to that! Actually-"

            no "I think we have wine... Be right back!"
        
        jump v15s48_norawine

    if nora.relationship.value >= Relationship.FWB.value:
        if v15s48_follow_your_heart:
            scene v15s48_18
            with dissolve

            no "Well, I guess I'm gonna follow my heart then..."

            scene v15s48_18a
            with dissolve

            u "You should."

        else:
            scene v15s48_18
            with dissolve

            no "The thing is though..."

            no "I don't want to focus on just me."

            scene v15s48_18a
            with dissolve

            u "You don't?"

            scene v15s48_18
            with dissolve

            no "Ha, no. I don't."
            
    elif (v15s48_follow_your_heart and not v15s48_interrupt) or kct == "confident":
        scene v15s48_18
        with dissolve

        no "So, when you say that I should follow my heart..."

        scene v15s48_18a
        with dissolve

        u "Yeah?"
    
    if (chloe.relationship.value >= Relationship.GIRLFRIEND.value or lauren.relationship.value >= Relationship.GIRLFRIEND.value or aubrey.relationship.value >= Relationship.TAMED.value) and not (kct == "confident"):
        scene v15s48_18
        with dissolve

        call screen kct_popup(required_kct="confident")

        no "[name]..."

        no "If only you were completely available, ha."

        scene v15s48_18a
        with dissolve

        u "Oh, your... It's me?"

        scene v15s48_18
        with dissolve

        no "Kinda? *Nervous chuckle*"

        no "You're a great guy, everyone can see that. And you obviously care about me, haha."

        scene v15s48_18a
        with dissolve

        u "I care more than you know. We all do, I think."

        scene v15s48_18
        with dissolve

        no "Thank you. It means a lot to know that I have you, even if just as a friend."

        scene v15s48_20 # TPP. Show MC and Nora hugging on the couch both slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s48_18
        with dissolve

        no "I think I need something stronger than this tea... *Laughs*"

        scene v15s48_18a
        with dissolve

        u "Haha, getting all soft on me now?"

        scene v15s48_18
        with dissolve

        no "Not for long! I'm pretty sure I saw some wine earlier. I'll go dig it out."

        label v15s48_norawine:

        scene v15s48_14a # TPP. MC sitting on the couch in the Cabin, Nora approaching the Couch coming from the kitchen area holding two glasses of wine, Nora slight smile, mouth closed, MC slight smile, mouth closed.
        with fade

        pause 0.75

        scene v15s48_21 # TPP. MC and Nora taking a sip of their wine.
        with dissolve

        pause 0.75

        scene v15s48_21a # TPP. MC and Nora putting their glasses of wine on the table near them, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s48_18a
        with dissolve

        u "Well, I wasn't expecting to be drinking wine by a fire tonight."

        scene v15s48_18
        with dissolve

        no "Right? This is nice."

        scene v15s48_18a
        with dissolve

        u "Yeah, it really is."

        scene v15s48_18
        with dissolve

        no "I'm glad you came, [name]."

        scene v15s48_18a
        with dissolve

        u "Me too."

        jump v15s48b

    else:
        if (chloe.relationship.value >= Relationship.GIRLFRIEND.value or lauren.relationship.value >= Relationship.GIRLFRIEND.value or aubrey.relationship.value >= Relationship.TAMED.value):
            call screen kct_popup
        
        scene v15s48_18h
        with dissolve

        no "[name]..."

        no "I want you."

        scene v15s48_18i
        with dissolve

        u "You do?"

        scene v15s48_18h
        with dissolve

        no "I..."

        no "I know there's a lot more involved than just me and you but..."

        if "v12_nora" in sceneList:
            no "I can't stop thinking about you."
        
        else:
            no "Do you think we could ever be more than friends? You and I?"
        
        scene v15s48_18i # FPP. MC looking at Nora, Nora looking at MC, Nora nervous, blushing, mouth closed.
        with dissolve

        u "Nora..."

        menu:
            "We should just be friends":
                $ add_point(KCT.BRO)
                $ v15_NoraFriendzone = True
                
                u "The relationship that we have is so strong, and fun... I think we should keep it that way."

                scene v15s48_18b
                with dissolve

                no "Oh... Yeah, okay."

                scene v15s48_18c
                with dissolve

                u "You're amazing, Nora. You know I think you're-"

                scene v15s48_18b
                with dissolve

                no "I get it, it's fine."

                scene v15s48_18c
                with dissolve

                u "No. Nora, seriously. You're one of the coolest people I've ever met, and I'm an idiot for letting you go."
                u "I just don't think I'm your forever either..."

                scene v15s48_18b
                with dissolve

                no "*Sighs*"

                if "v12_nora" in sceneList:
                    scene v15s48_18j # FPP. MC looking at Nora, Nora looking at MC, Nora with teary eyes but holding it back, neutral face, mouth closed.
                    with dissolve

                    pause 0.75

                scene v15s48_18b
                with dissolve

                no "Friends?"

                scene v15s48_18c
                with dissolve

                u "Yes, friends. Forever friends is something I can promise."

                scene v15s48_18b
                with dissolve

                no "Well, I'm happy with that, ha. Forever friends."

                scene v15s48_18c
                with dissolve

                u "Perfect."

                scene v15s48_20
                with dissolve

                pause 0.75

                scene v15s48_18
                with dissolve

                no "I feel like drinking some wine now."

                scene v15s48_18a
                with dissolve

                u "The tea isn't strong enough?"

                scene v15s48_18
                with dissolve

                no "Haha, no, it's not. I'll be right back."

                scene v15s48_14a
                with fade

                pause 0.75

                scene v15s48_21 # TPP. MC and Nora taking a sip of their wine.
                with dissolve

                pause 0.75

                scene v15s48_21a # TPP. MC and Nora putting their glasses of wine on the table near them, slight smile, mouth closed.
                with dissolve

                pause 0.75

                scene v15s48_18
                with dissolve

                no "I'm happy you're here, [name]."

                scene v15s48_18a
                with dissolve

                u "Me too."

                jump v15s48b

            "I want you too":
                scene v15s48_18k # FPP. MC looking at Nora, Nora looking at MC, Nora flirty, mouth closed.
                with dissolve

                u "I want you too."

            # -if they had sex in the past, Nora is thrilled, and hops up to give MC a passionate kiss

                if "v12_nora" in sceneList:
                    scene v15s48_22 # FPP. Nora standing up, Nora looking at MC, MC looking at Nora, Nora flirty, mouth closed.
                    with dissolve

                    pause 0.75

                    scene v15s48_23 # FPP. Nora standing infront of MC, Nora looking down at MC sitting on the couch, MC looking at Nora standing infront of him.
                    with dissolve

                    pause 0.75

                    scene v15s48_23a # FPP. Nora bending over and kissing MC.
                    with dissolve

                    u "(My god have I missed this...) *Moans*"

                else:
                    scene v15s48_18
                    with dissolve

                    no "You have no idea how happy I am."

                    scene v15s48_18a
                    with dissolve

                    u "I think I can guess... *Chuckles*"

                jump v15s48a