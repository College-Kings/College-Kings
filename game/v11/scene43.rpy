# SCENE 43: At the Bank
# Location: Bank
# Characters: MC (Outfit 3), Penelope (outfit1), Samantha (outfit1), Charli (outfit 1), Cameron (outfit1), Emily (outfit2), Josh(outfit1), Riley(Outfit 2), amber(outfit 2), Mr Lee(outfit 1), imre(outfit 1), ryan(outfit 1), nora(Outfit 2), chloe(outfit 1), chris(outfit 1), ms rose (outfit 1)
# Time: daytime

label v11_at_the_bank:
    scene v11bank1 # TPP Show Amber, Riley, MC, Ryan, Ms. Rose, and Nora arriving at the bank, bank teller is waiting and waiving to them
    with fade
    play music "music/v11/Track Scene 19_1.mp3" fadein 2
    pause 1
    
    scene v11bank1a # TPP Same angle as v11bank1, bank teller's mouth open
    with dissolve

    bank "Hello everyone, I am so pleased to meet you all. Believe it or not, this is actually my first time ever meeting Americans."

    scene v11bank2 # FPP Show Riley smiling with mouth open
    with dissolve

    ri "*Southern Accent* Well, it's mighty nice to meet you, too. I'm surprised you never came across any of us."

    scene v11bank3 # FPP Show bank teller smiling with mouth open
    with dissolve

    bank "Wow, I love your accent! You sound just like the people in the movies."

    scene v11bank2
    with dissolve

    ri "*Southern Accent* So I've been told. Even thought about being an actress, honestly."

    scene v11bank3
    with dissolve

    bank "You have the perfect movie-screen smile."

    scene v11bank2
    with dissolve

    ri "*Southern Accent* Why, thank you!"

    scene v11bank4 # FPP Show Ms. Rose laughing, mouth open
    with dissolve

    ro "*Laughs* I apologize, I can't hold it in any longer. Our little actress here is just teasing. Very few Americans sound like... whatever that was exactly. *Chuckles*"

    scene v11bank3
    with dissolve

    bank "Haha, it was very convincing. So, allow me to say that I've never given a tour of the bank, so this is a very rare occurrence. However, I am very excited to do so."

    scene v11bank2a # FPP Same angle as v11bank2, Riley with curious expression, mouth open
    with dissolve

    ri "What exactly will we be touring? I kinda just assume your banks are very different from ours."

    scene v11bank3
    with dissolve

    bank "Wow, you really were just using an accent..."

    scene v11bank2
    with dissolve

    ri "*Chuckles* Yes."

    scene v11bank3
    with dissolve

    bank "Impressive... But, yes, and no. Our banks are very similar, however, our currencies are not."
    bank "You all will have an opportunity to explore our vault today, we'll quiz your current knowledge and so forth."

    scene v11bank4a # FPP Same angle as v11bank4, Ms. Rose smiling, mouth open
    with dissolve

    ro "Sounds excellent."

    scene v11bank3a # FPP Same angle as v11bank3, bank teller with curious expression, mouth open
    with dissolve

    bank "Before I continue, am I mistaken in thinking that there were many more of you?"

    scene v11bank4b # FPP Same angle as v11bank4, Ms. Rose with neutral expression, mouth open
    with dissolve

    ro "There are, but we were told there was a limit to how many students could be with one guide."

    scene v11bank3
    with dissolve

    bank "Ah yes, the others must be in Jerry's group."

    if not v11_lauren_caught_aubrey: #if MC went to HP event
        scene v11bank3b # FPP Same angle as v11bank3, bank teller smiling with mouth closed
        with dissolve

        u "(Jerry?)"

    scene v11bank4b
    with dissolve

    ro "Perfect. I wonder why they haven't come in yet, they were right behind us."

    scene v11bank3
    with dissolve

    bank "I'm sure Jerry just stopped them out front. We have a capacity limit for security purposes."

    scene v11bank4b
    with dissolve

    ro "Understandable."

    scene v11bank3
    with dissolve

    bank "So, shall we begin?"

    scene v11bank3b
    with dissolve

    u "*Yawn*"

    scene v11bank3a
    with dissolve

    bank "Am I boring you already, young man?"

    scene v11bank3b
    with dissolve

    menu:
        "Just tired":
            u "Oh, no, sorry. I'm just a little tired."

            scene v11bank3c # FPP Same angle as v11bank3, bank teller with neutral expression, mouth open
            with dissolve

            bank "Ahh, I see. Let's begin."

        "A little":
            $ add_point(KCT.TROUBLEMAKER)

            u "A little... I'm just not interested in all this kind of stuff I guess."

            scene v11bank3
            with dissolve

            bank "*Laughs* Neither was I when I was your age. Let's begin."

    scene v11bank5 # TPP Show bank teller leading the group into the bank vault
    with dissolve

    pause 0.75

    scene v11bank6 # FPP Show bank teller, in vault, smiling with mouth open
    with dissolve

    bank "I wanted to start with what would be the main attraction, our vault. As you can see, our vault looks pretty similar to what you may see in a movie."
    bank "And here's a fun fact for you: Statistics show that less than one percent of people have ever actually seen the inside of a vault in person."

    scene v11bank7 # FPP Show Ryan, in vault, smiling with mouth open
    with dissolve

    ry "Make room for us! The top one percent."

    scene v11bank6
    with dissolve

    bank "Haha, usually we save that term for the wealthy."

    scene v11bank7
    with dissolve

    ry "How do you know I'm not wealthy?"

    scene v11bank6a # FPP Same angle as v11bank6, bank teller looks embarrassed with mouth open
    with dissolve

    bank "..."

    scene v11bank7
    with dissolve

    ry "Nevermind, just forget I asked."

    scene v11bank6
    with dissolve

    bank "Let us continue. May I ask, does anyone know what currency we use?"

    scene v11bank8 # FPP Show Nora, in vault, neutral expression, mouth open
    with dissolve

    no "Euros?"

    scene v11bank6
    with dissolve

    bank "Ahh, the most common American answer. Due to you being on European trip and Euro sounding so close in name, many Americans assume we use the Euro, when in actuality, we use the Pound."

    scene v11bank8a # FPP Same angle as v11bank8, Nora smiling with mouth open
    with dissolve

    no "Ahh... Yeah, yeah, yeah. *Chuckles* That's it."

    scene v11bank6
    with dissolve

    bank "Let me ask another, do you know which is worth more? The US Dollar or the Pound?"

    scene v11bank8
    with dissolve

    no "Well, right now the pound is."

    scene v11bank6
    with dissolve

    bank "Correct, and I like that you say right now. As I'm sure you all know, currency values can fluctuate."

    scene v11bank9 # TPP Amber leaning to whisper into MC's ear, smiling with mouth open, Riley is near enough to hear
    with dissolve

    am "*Whisper* This shit is boring... I wish we had our go-kart suits right now."

    scene v11bank10 # FPP Show Amber, in vault, smiling with mouth closed
    with dissolve

    u "*Whisper* Why?"

    scene v11bank10a # FPP Same angle as v11bank10, Amber smiling with mouth open
    with dissolve

    am "So we could rob the bank... *Chuckles*"

    scene v11bank11 # FPP Show Riley, in vault, shocked expression, mouth open
    with dissolve

    ri "*Whisper* AMBER!"

    scene v11bank10b # FPP Same angle as v11bank10, Amber smiling, eyebrow raised, mouth open
    with dissolve

    am "What? It'd be better than taking this stupid tour."

    scene v11bank11a # FPP Same angle as v11bank11, Riley with neutral expression, mouth open
    with dissolve

    ri "You could at least try to enjoy it."

    scene v11bank10a
    with dissolve

    am "Or I can think of different ways I could rob the place. What do you think, [name]? Are you more of a stealth man or do you enjoy complete chaos?"

    scene v11bank10
    with dissolve

    menu:
        "Stealth":
            u "Stealth obviously. You know they have silent security measures all throughout this entire place."

            scene v11bank10a
            with dissolve

            am "Yes! Stealth is definitely the way to go here."
        
        "Chaos":
            $ add_point(KCT.TROUBLEMAKER)
            u "I'm more of a guns blazing, lots of action guy. Go in hard or don't go at all."

            scene v11bank10a
            with dissolve

            am "As fun as it would be to raise hell in a place like this, stealth is the smartest way to go about doing this."

    scene v11bank11
    with dissolve

    ri "Stop it! No way is a good way. We need to stop talking about this before they think we're actually planning something."

    scene v11bank10b
    with dissolve

    am "\"We're?\" So you're in on it, too?"

    scene v11bank11b # FPP Same angle as v11bank11, Riley smiling with mouth open
    with dissolve

    ri "*Chuckles* No... But if you succeed and get a shit ton of money, I'd be looking for my cut."

    scene v11bank11c # FPP Same angle as v11bank11, Riley smiling with mouth closed
    with dissolve

    u "Haha, what? You gotta help somehow if you want to get a cut."

    scene v11bank10a
    with dissolve

    am "So, how would you help?"

    scene v11bank11b
    with dissolve

    ri "Hmm, I'll distract the tour guide."

    scene v11bank11c
    with dissolve

    u "What do you mean, entertain? Are you gonna perform a skit in your southern accent? *Chuckles*"

    scene v11bank10b
    with dissolve

    am "Yeah, I need to know if what you have in mind will actually work on them."

    scene v11bank12 # FPP Show Riley, in vault, leaning very close to Amber, Riley's hand on Amber's shoulder, both smiling, Riley's mouth open
    with dissolve
    
    ri "Excuse me, hi! I was just wondering... Someone said the pound was worth more than our dollars? So if I moved to London would I become rich? What if I get lonely in a new country, all by myself?"

    scene v11bank10c # FPP Same angle as v11bank10, Amber looking surprised, mouth open
    with dissolve

    am "..."

    scene v11bank11c
    with dissolve

    u "Haha, looks like it's working Riley. Welcome to the team."

    scene v11bank10b
    with dissolve

    am "...I was just surprised."

    scene v11bank11b
    with dissolve

    ri "*Chuckles* That wasn't so hard to do..."

    scene v11bank10a
    with dissolve

    am "We could literally rob this place right now... We don't even have to break in, we're already inside the vault."

    scene v11bank10b
    with dissolve

    am "*Chuckles* We could just slide some money in our clothes and act like nothing's happening..."

    scene v11bank11b
    with dissolve

    u "You're starting to sound like you're actually considering this. *Chuckles*"

    scene v11bank10b
    with dissolve

    am "Maybe I am."

    scene v11bank11b
    with dissolve

    ri "Don't let her get in your head, [name]. She won't do anything."

    scene v11bank10a
    with dissolve

    am "But I could. *Chuckles* All I'd have to do is knock out the teller."

    scene v11bank13 # FPP Show bank teller looking over at MC from across the vault, curious expression, mouth closed
    with dissolve
    
    u "*Whisper* Hey, let's be quiet with all this. The tour guide just looked at us."

    scene v11bank10a
    with dissolve

    am "Probably because we're not paying attention to the tour. *Chuckles*"

    scene v11bank10
    with dissolve

    u "Haha, you're probably right."

    scene v11bank10b
    with dissolve

    am "So, how are we gonna do this? Riley distraction or Amber distraction?"

    scene v11bank11a
    with dissolve

    ri "We're still talking about this?"

    scene v11bank10a
    with dissolve

    am "Better this than listening to the tour."

    scene v11bank10
    with dissolve

    menu:
        "Amber":
            u "Let's go with an Amber distraction, we know she won't get nervous or mess anything up. *Chuckles*"

            scene v11bank10a
            with dissolve

            am "Haha, you got that right. Operation Amber is a go."

        "Riley":
            scene v11bank11c
            with dissolve

            u "We already know Riley's plan works on Amber, so let's go with that. *Chuckles*"

            scene v11bank11
            with dissolve

            ri "No, no, no. There is no Riley plan."

            scene v11bank10a
            with dissolve

            am "Lame. *Laughs* Operation Amber it is, then."

    scene v11bank13a # FPP Same angle as v11bank13, Amber with hand on bank teller's shoulder, Amber smiling with mouth closed
    with dissolve

    ri "*Whisper* AMBER!"

    scene v11bank13b # FPP Same as v11bank13a, Amber with mouth open
    with dissolve

    am "Excuse me miss, earlier you said that pounds are worth more than the dollar. Does that mean that if I moved here and converted my currency I'd be a rich woman?"

    scene v11bank11
    with dissolve

    ri "That... that's my line."

    scene v11bank13c # FPP Same as v11bank13a, bank teller looks shocked with mouth open, Amber smiling with mouth closed
    with dissolve

    bank "*Gasps* I can't believe it."

    scene v11bank14 # FPP Show bank teller dragging Amber out of the vault by her arm, Amber looks surprised, mouth open
    with dissolve

    am "Hey, wait! Ouch!"

    scene v11bank14
    with dissolve

    u "Wait, what?"

    scene v11bank11
    with dissolve

    ro "What's going on?!"

    scene v11bank15 # TPP Show MC and Riley leaving vault, both look confused
    with dissolve

    pause 1

    scene v11bank16 # FPP Show Amber sitting in secluded area, bank teller standing in front of her, bank teller looks angry with mouth open
    with dissolve

    bank "You two sit down as well. Immediately."

    scene v11bank16a # FPP Same angle as v11bank16, bank teller with mouth closed
    with dissolve

    u "Okay..."

    scene v11bank17 # TPP Show MC and Riley sitting down next to Amber, everyone looks confused, Riley's mouth open
    with dissolve

    ri "Excuse me, but this is a bit unprofessional. Why are we here, and what is going on?"

    scene v11bank18 # FPP Show bank teller, looking angry, mouth open
    with dissolve

    bank "I would've never expected you of all people to do such a thing."

    scene v11bank18a # FPP Same angle as v11bank18, bank teller looking angry with mouth closed
    with dissolve

    u "Wait, do what?"

    scene v11bank18
    with dissolve

    bank "I know the three of you are attempting to rob this bank."

    scene v11bank17a # TPP Same angle as v11bank17, MC and Riley looking at Amber with neutral expressions, Amber smiling with mouth open
    with dissolve

    am "So you caught us, now what?"

    scene v11bank18
    with dissolve

    bank "Now you suffer the consequences."

    scene v11bank17a
    with dissolve

    am "They'll never take us in for this. *Chuckles* You have no proof."

    scene v11bank18
    with dissolve

    bank "There's audio and video recording at all times inside the vault. Not only that, but I overheard everything you said."

    scene v11bank19 # FPP Show Amber, looking at MC, smiling with mouth open
    with dissolve

    am "Guess we're going to jail. *Chuckles*"

    scene v11bank19a # FPP Same angle as v11bank19, Amber smiling with mouth closed
    with dissolve

    menu:
        "Yep":
            $ add_point(KCT.TROUBLEMAKER)
            u "I guess so, and to think I had such a bright future. Fuck..."

            scene v11bank19
            with dissolve

            am "Yeah, about as bright as a rusted quarter. *Laughs* Riley, maybe we'll be cellmates. There's a bright side to all of it."

            scene v11bank20 # FPP Show Riley, sitting next to MC, rolling her eyes and smiling with mouth open
            with dissolve

            ri "Yeah, you'll probably have a whole gang or something. *Chuckles*"

            scene v11bank19
            with dissolve

            am "You know me so well, haha."

            scene v11bank18
            with dissolve

            bank "Do the three of you not understand the severity of this situation? This is a serious crime."
            bank "You'll be considered international criminals, meaning your lives are now over. I wouldn't be so-"

            scene v11bank17b # TPP Same angle as v11bank17, MC and Riley smiling, Amber laughing with mouth open
            with dissolve

            am "*Laughs* I'm sorry... I can't hold it in any longer. I can't believe you actually thought we were going to rob a bank in plain daylight."
            am "*Laughs* We were just bored of your little vault tour and started joking around. You took it way too seriously, ma'am."

            scene v11bank18
            with dissolve

            bank "Planning to rob a bank is not a joking matter."

            scene v11bank20a # FPP Same angle as v11bank20, Riley looking at bank teller with a small smile, mouth open
            with dissolve

            ri "I apologize, but you must realize this isn't at all what we've been looking forward to doing while on vacation in Europe. There's so much more we could be experiencing."

            scene v11bank18b # FPP Same angle as v11bank18, bank teller looking annoyed, mouth closed
            with dissolve

            u "I could be sleeping."

            scene v11bank18c # FPP Same angle as v11bank18, bank teller looking annoyed, mouth open
            with dissolve

            bank "I'm not convinced. The line you said to me was the very thing I heard you say you would use to \"distract me.\""

            scene v11bank20a
            with dissolve

            ri "That's because in our \"robbing a bank\" scenario they wouldn't give me a cut unless I helped with the robbery. I was supposed to play my southern-belle role and ask you the rich person questions."

            scene v11bank18b
            with dissolve

            u "Alright, as fun as this has been, I think it's starting to get pretty out of hand. I never thought I'd be explaining that I had no real intentions of robbing a bank in London."

        "Stop playing":
            u "Alright, as fun as this has been, I think it's starting to get pretty out of hand. I never thought I'd be explaining that I had no real intentions of robbing a bank in London."
    
    scene v11bank17b
    with dissolve

    am "Although if I planned on robbing a bank it would be one in London. The money is worth more compared to ours. *Laughs*"

    scene v11bank18c # FPP Same angle as v11bank18, bank teller with a small, relieved smile, mouth open
    with dissolve

    bank "Haha, wow... Well, at least you all learned something during the tour."

    scene v11bank20a
    with dissolve

    ri "See? All fun and games."

    scene v11bank18c
    with dissolve

    bank "*Sighs* I wish I had the fun and youthful spirit you all have. Although, no more jokes about robbing banks, okay?"

    scene v11bank21 # FPP Show Ms. Rose entering secluded area, neutral expression, mouth open
    with dissolve

    ro "Is everything alright?"

    scene v11bank18
    with dissolve

    bank "You have very imaginative students, but they are free to go. I apologize for cutting the end of the tour short."

    scene v11bank21
    with dissolve

    ro "Will someone please explain to me exactly what has happened?"

    if ms_rose.relationship >= Relationship.FWB and joinwolves: #sanitizing pathbuilder input
        scene v11bank18
        with dissolve

        bank "I'd really like to get the rest of the group situated, I shouldn't have left my post. I can get in a lot of trouble for leaving a tour group in the vault, cameras or not. *Chuckles*"

        scene v11bank21
        with dissolve

        ro "Yes I understand, [name] can fill me in."

        scene v11bank22 # FPP Show Amber, Riley, and bank teller leaving the area
        with dissolve

        pause 0.5

        scene v11bank21a # FPP Same angle as v11bank21, Ms. Rose with neutral expression, mouth closed
        with dissolve

        u "It really wasn't anything-"

        scene v11bank23 # TPP Show Ms. Rose pushing MC up against a wall and making out with him
        with dissolve

        play sound "sounds/kiss.mp3"
        
        pause 1

        scene v11bank23a # TPP Same angle as v11bank23a, Ms. Rose leaning back from kissing MC, she is smiling with mouth open
        with dissolve

        ro "Mmm. Excuse me, I couldn't control myself."

        scene v11bank22a # FPP Same angle as v11bank22, show Ms. Rose leaving the area
        with dissolve

        u "(Wow...)"

        scene v11bank24 # FPP Show view of MC entering the bank lobby, where everyone else is waiting for him
        with dissolve

        pause 1
    
    else:
        scene v11bank18
        with dissolve

        bank "I'd like to get the rest of the group situated, I shouldn't have left my post. I can get in a lot of trouble for leaving a tour in the vault, cameras or not. *Chuckles*"

        scene v11bank21
        with dissolve

        ro "Yes. I understand, let's go."

        scene v11bank25 # TPP Amber, Riley, Ms. Rose, and bank teller leaving the area, MC following
        with dissolve

        pause 1
        
        scene v11bank24
        with dissolve

        pause 1

    scene v11bank26 # FPP Show Mr. Lee standing by Ms. Rose, they are looking at each other, both smiling Mr. Lee's mouth open
    with dissolve

    lee "How did things go with your group?"

    scene v11bank26a # FPP Same angle as v11bank26, Mr. Lee's mouth closed, Ms. Rose looking over at MC, mouth open
    with dissolve

    ro "Three of them almost got convicted as international criminals for attempted bank robbery."

    scene v11bank26
    with dissolve

    lee "*Sighs* I could almost laugh. My students want to walk, how do you plan to get back? Either way we'll make it just in time for the event tonight."

    scene v11bank26b # FPP Same angle as v11bank26, Mr. Lee and Ms. Rose looking at each other, Ms. Rose's mouth open
    with dissolve

    ro "I think we'll take the underground, I personally want to."

    scene v11bank26
    with dissolve

    lee "And I personally wanted to stretch my legs. *Chuckles*"

    scene v11bank26b
    with dissolve

    ro "*Laughs* Very well, we'll meet back up in the hotel lobby?"

    scene v11bank26
    with dissolve

    lee "Sounds like a plan."

    scene v11bank27 # FPP Show Mr. Lee standing in the middle of the lobby addressing the students
    with dissolve

    lee "Alright students, you have two choices. Students that go back with me will be enjoying a bit sightseeing while we take a nice walk back."
    lee "And the students that choose to go with Ms. Rose will be riding the underground back to the hotel."

    scene v11bank27a # FPP Same as v11bank27, Mr. Lee's mouth closed
    with dissolve

    menu:
        "Go with Mr. Lee":
            u "(I'd rather just walk.)"

            scene v11bank28 # TPP Show MC following Mr. Lee out of the bank
            with dissolve

            pause 1

            scene v11bank29 # TPP Show Mr. Lee, Nora, Imre, Riley, Amber, and MC walking along the sidewalk
            with fade

            pause 0.75
            stop music fadeout 3
            jump v11_nora_lingerie

        "Go with Ms. Rose":
            $ v11_underground_rose = True
            u "(I'm definitely not walking back.)"

            scene v11bank28a # TPP Show Ms. Rose, Nora, Amber, Riley, and MC leaving the bank
            with dissolve

            pause 1 
            
            scene v11bank30 # TPP Show Ms. Rose, Nora, Amber, Riley, and MC heading down into the underground
            with fade

            pause 0.75
            
            scene v11bank31 # TPP Show Ms. Rose, Nora, Amber, Riley, and MC getting on to a train in the underground
            with fade

            pause 0.75
            stop music fadeout 3
            jump v11_rose_underground