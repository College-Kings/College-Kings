# SCENE 43: Finding Nora, Interrogating Chris
# Locations: Wolves house
# Characters: MC (Outfit: 1), AMBER (Outfit: Detective), CHRIS (Outfit: 2)
# Time: Morning


label v15s43:
    scene v15s43_1 # TPP. Show MC and Amber walking up to the wolves front door, both slight smile, mouths closed.
    with fade (1,0,1)

    pause  

    play sound "sounds/knock.mp3"

    scene v15s43_2 # FPP. Amber and MC at the front of the wolves house, MC looking at Amber, Amber looking at the door, Amber knocking on the door, Amber slight smile, mouth closed.
    with dissolve 

    pause  

    scene v15s42_2a # FPP. Amber and MC both looking at the door waiting for an answer, Amber slight smile, mouth closed.
    with dissolve 

    if joinwolves:
        scene v15s43_2b # FPP. Amber looking at MC, MC looking at Amber, Amber slight smile, mouth closed.
        with dissolve

        u "Why are we even knocking on the door? I live here."

        scene v15s43_2c # FPP. Amber looking at MC, MC looking at Amber, Amber slight smile, mouth open.
        with dissolve

        am "Haha, shhh... Detective's don't live in frats!"

        scene v15s43_2b
        with dissolve

        u "Haha, of course."

        pause  

        scene v15s42_2a 
        with dissolve 

        menu:
            "Try the door handle.":
                $ add_point(KCT.BRO)
                play sound "sounds/dooropen.mp3"

                scene v15s42_3 # TPP. Close up shot of MC's hand turning the door knob and opening the door.
                with dissolve

                u "It's unlocked."

                scene v15s43_2c
                with dissolve

                am "This is just like in the movies!"

                am "We really need guns for this, though."

                scene v15s43_2b
                with dissolve

                u "We really don't. *Chuckles*"

            "Keep waiting.":
                $ add_point(KCT.BOYFRIEND)
                scene v15s43_2c
                with dissolve

                am "How long should we wait for?"

                scene v15s43_2b
                with dissolve

                u "I don't know, you're the lead detective on this case."

                scene v15s43_2c
                with dissolve

                am "Maybe we can find an open window to climb through?"

                scene v15s43_2b
                with dissolve

                u "Haha, climb up the house? Go right ahead, I'll watch."

                scene v15s43_2c
                with dissolve

                am "Let me just try this first."

                play sound "sounds/dooropen.mp3"

                scene v15s43_3a # TPP. Close up shot of Amber's hand turning the door knob and opening the door.
                with dissolve

                am "It's fucking open!"

                scene v15s43_2b
                with dissolve

                u "Dammit, I wanted to see you squeeze through that tiny window..."

                scene v15s43_2d # FPP. Amber looking at MC, MC looking at Amber, Amber giving him the middle finger while laughing.
                with dissolve
            "(Professional:) Strategize."  if detective == "professional":
                scene v15s43_2b
                with dissolve

                u "Maybe one of us should go around the back. We don't want our suspect escaping."

                scene v15s43_2c
                with dissolve

                am "That's true. But he's not going to think we're a danger to him anyway."

                scene v15s43_2b
                with dissolve

                u "Why? We're detectives."

                scene v15s43_2c
                with dissolve

                am "Yeah, but we're undercover detectives. Deep undercover.... We don't even carry badges. *Giggles*"

                scene v15s43_2b
                with dissolve

                u "Right... We could anybody."

                scene v15s43_2c
                with dissolve

                am "Exactly. Hello, sir! We're selling insurance for your windows. And BAM! We're inside interrogating that punk."

                scene v15s43_2b
                with dissolve

                u "You are an absolute genius."

                scene v15s43_2e # FPP. Amber looking at MC, MC looking at Amber, Amber winking, slight smile, mouth open.
                with dissolve

                am "Thank you."

                scene v15s43_2b
                with dissolve

                u "*Chuckles*"

                scene v15s43_2c
                with dissolve

                am "I'm done waiting. We're breaking in."

                play sound "sounds/dooropen.mp3"

                scene v15s43_3a
                with dissolve

                u "Already unlocked?"

                scene v15s43_2c
                with dissolve

                am "I didn't think it would be that easy, haha."

            "(Psychologist:) What's Chris thinking?" if detective == "psychologist":
            
                scene v15s43_2b
                with dissolve

                u "I bet he's wondering who's at the door."

                scene v15s43_2c
                with dissolve

                am "I'm sure he is."

                scene v15s43_2b
                with dissolve

                u "Hmm... What could we want?"

                u "Should he even risk opening the door? Hmm..."

                scene v15s43_2c
                with dissolve

                am "*Chuckles* Okay, wow... You'd make a mean psychologist."

                scene v15s43_2b
                with dissolve

                u "He's making us wait a long time. Showing signs of narcissism."

                scene v15s43_2c
                with dissolve

                am "Let's just try the door."

                play sound "sounds/dooropen.mp3"

                scene v15s43_3a
                with dissolve

                am "Oh, that was too easy."

                scene v15s43_2b
                with dissolve

                u "He's already playing mind games with us, this isn't good."
            "(Loose Cannon:) Kick the door open" if detective == "loose cannon":
                scene v15s43_2b
                with dissolve

                u "Watch out, back up."

                scene v15s43_2c
                with dissolve

                am "Huh?"

                play sound "sounds/thud.mp3"

                scene v15s43_4 # TPP. Show MC kicking open the door and the door flying open.
                with dissolve

                pause

                scene v15s43_2c
                with dissolve

                am "Oh, fuck [name]! You weren't kidding about being a loose cannon."

                scene v15s43_2b
                with dissolve

                u "I ain't got time to fuck around with these punk ass kids!"

                scene v15s43_2c
                with dissolve

                am "*Laughs* Woah there, okay! Calm down big guy, you're starting to turn green..."

                scene v15s43_2b
                with dissolve

                u "Ha. Okay, sorry. Got a little carried away..."

                scene v15s43_2c
                with dissolve

                am "*Whispers* A little?"

    scene v15s43_5 # TPP. Show MC and Amber entering the wolves house, both slight smile, mouth closed.
    with dissolve

    u "Chris?"

    scene v15s43_6 # TPP. Close up of just Amber in the wolves house, her hand in the shape like a gun, Amber suspicious, mouth open.
    with dissolve

    am "Chris, we know you're in here!"

    scene v15s43_7 # TPP. Show MC and Amber walking into the living room, Amber keeping her hands in the gun shape, Amber suspicious, mouth closed.
    with dissolve

    pause  

    scene v15s43_8 # TPP. MC and Amber standing in the living room, MC looking at Amber, Amber looking at MC, Amber suspicious, mouth closed, MC suspicious, mouth closed.
    with dissolve 

    menu:
        "Call for Chris":
            $ add_point(KCT.TROUBLEMAKER)
            scene v15s43_9 # TPP. Close up of MC, looking at the room, suspicious, mouth open.
            with dissolve

            u "Chris? Come on out!"

            scene v15s43_10 # TPP. Close up of Amber, hands in the shape of a gun, looking at the room, suspicious, mouth open.
            with dissolve

            am "Don't worry, we'll go easy on you. Just come out and put your hands where I can see them!"

        "Stay Quiet":
            $ add_point(KCT.BRO)
            scene v15s43_9
            with dissolve

            u "*Whispers* No sign of him."

            scene v15s43_10
            with dissolve

            am "Chris, get your ass downstairs!"
        
        "(Professional:) Use your instinct." if detective == "professional":
            scene v15s43_9
            with dissolve

            u "Something doesn't feel right about this..."

            u "We should call for backup and get forensics in here."

            scene v15s43_10
            with dissolve

            am "Ha, wait... What makes you say that?"

            scene v15s43_9
            with dissolve

            u "I know when something isn't right, okay? I can feel it!"

        "(Psychologist:) Analyze how you feel." if detective == "psychologist":
            scene v15s43_9
            with dissolve

            u "I feel like he's watching us. Studying us. The observers have become the observed."

            scene v15s43_10
            with dissolve

            am "Eww, stop... You're creeping me out! Like he's in the walls or something."

            scene v15s43_9
            with dissolve

            u "*Gasps* A psychological horror!"

        "(Loose Cannon:) Be angry." if detective == "loose cannon":

            scene v15s43_11 # TPP. View showing MC on one side of a couch in the living room, Amber on the other side with her hands in the shape of a gun, both suspicious, mouth closed.
            with dissolve

            pause  

            scene v15s43_11a # TPP. Show MC kicking the couch, Amber slightly shocked, mouth closed, MC angry, mouth open.
            with dissolve

            u "Come on out, Chris! We don't play these hide and seek games!"

            scene v15s43_11b # TPP. Show Amber kicking the couch, Amber angry, mouth open, MC angry, mouth closed.
            with dissolve

            am "Yeah!"

            scene v15s43_11c # TPP. Show MC and Amber looking at each other from across the couch both laughing.
            with dissolve

            pause 

    scene v15s43_12 # TPP. Close up of Chris walking into the living room, Chris confused, mouth open.
    with dissolve

    ch "Hey, guys? What's with all the yelling...?"

    scene v15s43_10a # TPP. Show Amber putting her hand gun into her pocket, suspicious, mouth open.
    with dissolve

    am "Take a seat, Chris. This won't take long."

    scene v15s43_12
    with dissolve

    ch "W-what's going on? Why are you acting weird?"

    scene v15s43_10b # TPP. Amber with her hands on her hips looking in Chris's direction, suspicous, mouth open.
    with dissolve

    am "We'll ask the questions here. Please, take a seat."

    scene v15s43_13 # TPP. Chris sitting on the couch, a coffee table infront of the couch, MC standing on the right of the couch facing Chris, Amber standing on the left of the table facing Chris, Amber and MC faces not shown in the shot, Chris confused, mouth closed, 
    with fade(1,0,1)

    pause  

    scene v15s43_14 # FPP. MC standing on the right of the coffee table, MC looking at Chris, Chris looking at MC, Chris confused, mouth closed.
    with dissolve

    u "Relax, Chris. We just need to get to the bottom of something."

    scene v15s43_14a # FPP. MC looking at Chris, Chris looking at MC, Chris confused, mouth open.
    with dissolve

    ch "Of what?"

    scene v15s43_15 # FPP. MC looking across the coffee table at Amber, Amber looking at Chris, Amber suspicious, mouth open.
    with dissolve

    am "Nora's been missing since Tuesday."

    scene v15s43_14b # FPP. MC looking at Chris, Chris looking at Amber, Chris neutral face, mouth open.
    with dissolve

    ch "Oh. I don't have anything to say about Nora."

    scene v15s43_14
    with dissolve

    u "We'll be the judge of that."

    scene v15s43_14a
    with dissolve

    ch "Huh?"

    if wolves:
        ch "What do you mean, [name]?"
    else:
        ch "What are you talking about?"

    scene v15s43_15
    with dissolve

    am "We haven't seen Nora or heard from her since we left the airport on Tuesday."

    am "That's kind of suspicious, don't you think?"

    scene v15s43_14c # FPP. MC looking at Chris, Chris avoiding eye-contact with Amber, Chris neutral face, mouth open.
    with dissolve

    ch "No."

    scene v15s43_15
    with dissolve

    am "The obvious answer is that she's at her dad's house, or her stepmother's..."

    scene v15s43_14d # FPP. MC looking at Chris, Chris looking at Amber, Chris nervous, mouth closed.
    with dissolve

    $ parents_house_clue = True

    scene v15s43_15
    with dissolve

    am "Care to comment on that?"

    scene v15s43_14e # FPP. MC looking at Chris, Chris looking at Amber, Chris nervous, mouth open.
    with dissolve

    ch "No."

    scene v15s43_14f # FPP. MC looking at Chris, Chris looking at MC, Chris nervous, mouth closed.
    with dissolve

    u "One-word answers... Huh. That's never convincing, is it detective?"

    scene v15s43_15a # FPP. MC looking at Amber, Amber looking at MC, Amber suspicious, mouth open.
    with dissolve

    am "Not at all, my protege... Not at all."

    scene v15s43_14f
    with dissolve

    ch "Okay then, I don't think she's with either of them. Happy now?"

    scene v15s43_15
    with dissolve

    am "No. You're hiding something."

    scene v15s43_14b
    with dissolve

    ch "She wanted to be alone after we broke up. I'm respecting that wish."

    ch "And I suggest you should respect that too."

    $ clue_alone = True

    scene v15s43_14g # FPP. MC looking at Chris, Chris looking at MC, Chris neutral face, mouth closed.
    with dissolve

    menu:
        "Where did she go?":
            $ add_point(KCT.BRO)
            u "Where did she go? She must have told you."

            scene v15s43_14h # FPP. MC looking at Chris, Chris looking at MC, Chris neutral face, mouth open.
            with dissolve

            ch "I've already said that I'm respecting her by not telling anyone anything."

            scene v15s43_15
            with dissolve

            am "The quicker you tell us, the quicker we leave you alone. Capeesh?"

            scene v15s43_14b
            with dissolve

            $ clue_camping = True

            ch "Why are you acting so weird? Listen, I don't know where she is. She could have gone camping for all I know."

            ch "Just wait until she comes back. She's fine. I swear she's fine. (LOCATION UNLOCKED: CAMPING BY HERSELF.)"

        "Did she see someone?":
            $ add_point(KCT.TROUBLEMAKER)
            u "Did she go see someone else?"

            scene v15s43_14h
            with dissolve

            ch "No, she wanted to be alone, like I just said."

            scene v15s43_15
            with dissolve

            am "That's no good, Chris. You need to start telling us something we can use."

        "(Professional:) You're lying." if detective == "professional":
            u "You're lying straight to our faces! You know exactly where she is and it's only a matter of time before we find out."

            scene v15s43_14h
            with dissolve

            $ clue_camping = True

            ch "I swear, man! She could have gone away camping for all I know. I really have no idea. You gotta believe me."


        "(Psychologist:) Analayze Chris." if detective == "psychologist":

            u "You're enjoying this aren't you? Do you get joy out of withholding information from us?"

            scene v15s43_14h
            with dissolve

            ch "Wha- No!"

            scene v15s43_14g
            with dissolve

            u "I wonder what else was said in your last conversation that made Nora want to completely disappear..."

            scene v15s43_15
            with dissolve

            am "Oooooooooh. That one hurt."

            scene v15s43_14b
            with dissolve

            $ clue_camping = True

            ch "Why are you talking like this? I seriously don't know! Maybe she went camping or something..."
        "(Loose Cannon:) Accuse Chris." if detective == "loose cannon":
            play sound "sounds/thud.mp3"

            scene v15s43_16 # TPP. Show MC slamming his hands on the table, MC angry, mouth open.
            with dissolve 

            u "You're respecting nobody with that attitude!"

            scene v15s43_14g
            with dissolve

            u "We're Nora's friends and we're concerned about her."

            scene v15s43_17 # TPP. Show MC up in Chris's face, pointing his finger at Chris, Chris confused, mouth closed, MC angry, mouth open.
            with dissolve

            u "The least you can do, as her ex-boyfriend for the last who the fuck cares how many years... Is tell us where in the hell she is!"

            scene v15s43_15
            with dissolve

            am "He's right."

            scene v15s43_14g
            with dissolve

            u "Did she really want to be alone? Or are you keeping her somewhere? You need to tell us, Chris, before it's too late."

            scene v15s43_14h
            with dissolve

            ch "What the hell is wrong with you?"

            ch "Did you start taking improv classes or some shit? I don't fucking know where she is, [name]."

    scene v15s43_15
    with dissolve

    am "What about other family members, other properties her dad owns, anything like that?"

    scene v15s43_14b
    with dissolve

    ch "Um... She has an aunt."

    scene v15s43_14g
    with dissolve

    u "How is that supposed to help?"

    scene v15s43_14h
    with dissolve

    $ clue_mr_rose_cabin = True

    ch "Her aunt... Oh yeah! Sometimes her aunt will rent out her dad's cabin."

    ch "And there, that answers your question about other properties, too. Can you leave me alone now?"

    scene v15s43_15
    with dissolve

    am "Not so fast, wise guy."

    scene v15s43_14g
    with dissolve

    menu:
        "She's close with her Aunt?":
            $ add_point(KCT.BOYFRIEND)

            u "This aunt-"

            scene v15s43_15
            with dissolve

            am "If she even exists..."

            scene v15s43_14g
            with dissolve

            u "Yeah. If she exists... Is Nora close to her?"

            scene v15s43_14h
            with dissolve

            ch "I don't know if they're close, but I think she lives nearby. And no, I'm not sure where."

            scene v15s43_15
            with dissolve

            am "Oh yeah? How sure?"

        "She's not with Mr. Rose?":
            $ add_point(KCT.TROUBLEMAKER)
            u "So you're sure that Nora's not with Mr. Rose, or... Her dad, I mean?"

            scene v15s43_14h
            with dissolve

            ch "I don't think she would go to her dad's house."

            scene v15s43_15
            with dissolve

            am "Why?"

            scene v15s43_14b
            with dissolve

            $ clue_nora_hates_her_dad = True

            ch "She pretty much hates him. That's the last place she'd go."

            scene v15s43_15
            with dissolve

            am "Hmm... I don't know if we can trust you."
        "(Professional:) Use logic." if detective == "professional":
            u "This aunt is around often?"

            scene v15s43_14h
            with dissolve

            ch "Yeah, I think she lives close to campus, but no idea where."

            scene v15s43_14g
            with dissolve

            u "Nora has an aunt that lives near campus, sounds like they're close.... And as her ex-boyfriend of multiple years, you have no idea where she lives?"

            scene v15s43_15
            with dissolve

            am "Ha. That doesn't add up."

            scene v15s43_14g
            with dissolve

            u "Help us make sense out of what you're saying, Chris!"
        "(Psychologist:) Examine Further." if detective == "psychologist"
            u "This aunt. Does Nora like her?"

            scene v15s43_14h
            with dissolve

            ch "Yeah, I think so. I don't know where you can find her though."

            scene v15s43_14g
            with dissolve

            u "Insecurity within oneself leads to a lack of connection to others. A lack of attentiveness... Why do you think that is, Chris?"

            scene v15s43_14h
            with dissolve

            ch "What?"

            scene v15s43_15
            with dissolve

            am "*Sighs* Are you sure she's not with her dad?"

            scene v15s43_14b
            with dissolve

            $ clue_nora_hates_her_dad = True

            ch "I doubt it. She hates her dad. (CLUE UNLOCKED: NORA HATES HER DAD.)"

            scene v15s43_14g
            with dissolve

            u "Hate is a very strong word. Are those your words or Nora's words?"
        "(Loose Cannon:) Shout at Chris?"
            scene v15s43_14g
            with vpunch

            u "Tell us where the aunt lives, now!"

            scene v15s43_15
            with dissolve

            am "Well, wait. Is Nora even close with her?"

            scene v15s43_14b
            with dissolve

            ch "I think she is. She lives nearby, I know that much, but I swear I don't know any more than that."

            scene v15s43_14g
            with dissolve

            u "I can't believe what I'm hearing, ha."

            scene v15s43_14h
            with dissolve

            ch "What?"

            scene v15s43_14g
            with dissolve

            u "You expect us to believe that you were Nora's boyfriend for years and know nothing about her aunt?"

            scene v15s43_15
            with dissolve

            am "You're sure she's not with her dad?"

            scene v15s43_14b
            with dissolve

            $ clue_nora_hates_her_dad = True

            ch "She hates her dad. She wouldn't go to him."

            scene v15s43_16a # TPP. Show MC kicking the coffee table, MC angry, mouth open.
            with dissolve

            u "Hate? I'll tell you about hate, Chris! I hate not getting a straight answer out of you."

    scene v15s43_14h
    with dissolve

    ch "What the hell are you on today? Is this a prank? Am I on camera right now?"

    scene v15s43_15
    with dissolve

    am "No, this is not a prank. We take our jobs very seriously."

    scene v15s43_14b
    with dissolve

    ch "Jobs? What jobs?"

    scene v15s43_15
    with dissolve

    am "Answer the questions!"

    scene v15s43_14b
    with dissolve

    ch "I have nothing else to say!"

    scene v15s43_17a # TPP. MC and Amber closer to Chris both of them looking at Chris suspiciously, mouth closed, Chris confused, mouth closed.
    with dissolve

    pause  

    scene v15s43_15
    with dissolve

    am "How very intriguing."

    scene v15s43_14b
    with dissolve

    ch "It's not intriguing. I have nothing to say."

    ch "I have no idea what drugs you are on but you both need to get help. I'm getting the hell out of here."

    scene v15s43_18 # TPP. Show Chris leaving the living room, Chris confused, mouth closed.
    with dissolve

    pause 

    scene v15s43_15

    am "Yeah, you're free to leave. Thanks for the cooperation, jackass."

    scene v15s43_15b # FPP. MC looking at Amber, Amber looking at MC, Amber slight smile, mouth closed.
    with dissolve

    u "He's already gone, Amber."

    scene v15s43_15c # FPP. MC looking at Amber, Amber looking at MC, Amber slight smile, mouth open.
    with dissolve

    am "Oh-"

    am "*Laughs* That was brilliant!"

    am "Let's get back to the board, I think we have a few ideas now."

    scene v15s43_15b
    with dissolve

    u "Great idea, chief."

    if detective == "loose cannon":
        menu:
            "Kick Table.":
                $ add_point(KCT.TROUBLEMAKER)
                $ add_point(KCT.BRO)
                scene v15s43_19 # TPP. Show MC kicking the coffee table, slightly angry, mouth open.
                with dissolve

                u "Gah! That's what you get!"

                scene v15s43_15c
                with dissolve

                am "For fuck's sake..."

            "Don't kick table.":
                $ add_point(KCT.BOYFRIEND)
                scene v15s43_20 # FPP. MC looking at the coffee table.
                with dissolve

                u "(I think I've done enough damage to this room already, haha.)"

    scene v15s43_21 # TPP. Show MC and Amber leaving the wolve's house, both slight smile, mouth closed.
    with dissolve

    jump v15s44