# SCENE 45: Finding Nora, Interrogating Chloe
# Locations: Chicks Frat Houe
# Characters: AMBER (Outfit: 1), MC (Outfit: 1), CHLOE (Outfit: 5)
# Time: Morning
# Render Count 9 Unique 39 Total

label v15s45:
    scene v15s45_1 # TPP. MC and Amber are walking along the street, both no expressions, mouths are closed, looking directly ahead.
    with dissolve

    pause 0.75 
    
    scene v15s45_1a # TPP. Mc and Amber stop walking along the street, Amber pulls out her phone, and looks at her phone, no expression, mouths is closed, Mc is looking at Amber, no expression, mouth is closed
    with dissolve
    
    pause 0.75

    scene v15s45_2 # FPP. Show Amber on the sidewalk, looking directly Mc, no expression, mouth is open
    with dissolve

    am "Chloe's home right now."

    scene v15s45_2a # FPP. same as v15s45_2 Amber's mouth is closed, still no expression, still looking at Mc
    with dissolve

    u "How do you know?"

    scene v15s45_2
    with dissolve

    am "I've got an informant... Lindsey."

    scene v15s45_2a
    with dissolve

    u "You've secured a mole on the inside?"

    scene v15s45_2a
    with dissolve

    am "You haven't seen nothing yet, buster!"

    scene v15s45_1
    with fade

    pause 0.75

    scene v15s45_3 # TPP. MC and Amber walking up to the Chicks front door, no expressions, mouths are closed, looking directly ahead
    with dissolve

    pause 0.75

    scene v15s45_4 # TPP. Amber reaches out to knock on the door, but before she knocks, the door is opened by Chloe who steps outside, Mc is standing behind Amber, all of them have no expressions, Amber is looking at Chloe, Chloe is looking at Amber, Mc is looking at Chloe
    with dissolve

    pause 0.75

    scene v15s45_5 # FPP. Show Chloe standing in the Chicks doorway looking at Amber, Amber is seen standing just outside the doorway looking at Chloe, both of them no expressions, Chloe's mouth is open, Amber's mouth is closed
    with dissolve

    cl "Oh. Hey, you two. I was just heading to campus."

    scene v15s45_5a # FPP. same as v15s45_5 Amber's mouth is open, Chloe's mouth is closed, still no expressions, still looking at each other
    with dissolve

    am "Woah now... Hold on a minute there, missy."

    scene v15s45_5
    with dissolve

    cl "Missy?"

    scene v15s45_5a
    with dissolve

    am "We've got some questions for you."

    scene v15s45_5b # FPP. same as v15s45_5 Amber and Chloe are looking at Mc, still no expressions, mouths are still closed.
    with dissolve

    menu:
        "Be polite":
            if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                $ add_point(KCT.BOYFRIEND)
                
            elif nora.relationship.value >= Relationship.FWB.value:
                $ add_point(KCT.TROUBLEMAKER)
                
            else:
                $ add_point(KCT.BRO)

            scene v15s45_5b
            with dissolve

            u "Please, Chloe. If you don't mind, we'd like to sit and talk to you."

        "Be impatient":
            if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                $ add_point(KCT.BRO)
                
            elif nora.relationship.value >= Relationship.FWB.value:
                $ add_point(KCT.BOYFRIEND)
                
            else:
                $ add_point(KCT.TROUBLEMAKER)

            scene v15s45_5b
            with dissolve

            u "Go back inside, Chloe. We have important business to take care of."
        
        "State the facts" if detective == "professional":
            if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                $ add_point(KCT.BOYFRIEND)
                
            elif nora.relationship.value >= Relationship.FWB.value:
                $ add_point(KCT.BRO)
                
            else:
                $ add_point(KCT.TROUBLEMAKER)

            scene v15s45_5b
            with dissolve

            u "We're just looking for the facts, ma'am. If you're honest with us, this shouldn't take up much of your time."

        "Analyze Chloe" if detective == "psychologist":
            if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                $ add_point(KCT.BRO)
            elif nora.relationship.value >= Relationship.FWB.value:
                $ add_point(KCT.TROUBLEMAKER)
            else:
                $ add_point(KCT.BOYFRIEND)
                
            scene v15s45_5b
            with dissolve

            u "Heading out right as we're heading in, huh?"

            u "There's a weight on your shoulders, I can feel it. You need to talk to us. We can help you."

        "Threaten Chloe" if detective == "loose_cannon":
            if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                $ add_point(KCT.TROUBLEMAKER)

            elif nora.relationship.value >= Relationship.FWB.value: 
                $ add_point(KCT.BOYFRIEND)

            else:
                $ add_point(KCT.BRO)

            scene v15s45_5b
            with dissolve

            u "You need to turn yourself around right now and get back inside or I'll do it for you."

    scene v15s45_5c # FPP. same as v15s45_5b Chloe's mouth is open, Chloe and Amber are still looking at Mc, Amber's mouth is still closed.
    with dissolve

    cl "What? Wait, [name]... What's going on?"

    scene v15s45_5a
    with dissolve

    am "We're investigating the disappearance of Nora Rose."

    scene v15s45_5c
    with dissolve

    cl "Ugh..."

    scene v15s45_5d # FPP. same as v15s45_5 Chloe is rolling her eyes, facing Amber mouth is open, Amber's mouth is closed, Amber is still looking at Chloe
    with dissolve

    cl "I don't know where she is, nor do I care."

    scene v15s45_5b
    with dissolve

    u "We'll be the judge of what you know."

    scene v15s45_5c
    with dissolve

    cl "Ha! Excuse me?"

    scene v15s45_5a
    with dissolve

    am "Step back inside, please ma'am."

    scene v15s45_5d
    with dissolve

    cl "*Sighs* Whatever, weirdos."

    scene v15s45_5c
    with dissolve

    cl "I guess I've got a few minutes to spare."

    scene v15s45_6 # FPP. Chloe Amber and Mc enter the Chicks living room, Chloe sit's down and looks at Mc and Amber, Amber and Mc do not sit down and instead stand in front of Chloe, have a chair close by to Mc will be used in a future render, Amber and Mc are looking at Chloe, all of them have no expressions, all of their mouths are closed
    with dissolve

    pause 0.75

    scene v15s45_7 # FPP. Show only Chloe, Chloe is looking at Mc, mouth is open, no expression
    with dissolve

    cl "Are you not going to sit down?"

    scene v15s45_7a # FPP. Chloe's mouth is closed, still no expression, still looking at Mc
    with dissolve

    menu:
        "Be polite":
            if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                $ add_point(KCT.BOYFRIEND)

            elif nora.relationship.value >= Relationship.FWB.value:
                $ add_point(KCT.TROUBLEMAKER)

            else:
                $ add_point(KCT.BRO)
                        
            scene v15s45_7a
            with dissolve

            u "We like to think on our feet, thank you."

        "Be impatient":
            if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                $ add_point(KCT.BRO)

            elif nora.relationship.value >= Relationship.FWB.value:
                $ add_point(KCT.BOYFRIEND)

            else:
                $ add_point(KCT.TROUBLEMAKER)
                        
            scene v15s45_7a
            with dissolve

            u "Let's skip the pleasantries and get straight to the questions, okay?"
        
        "Speak your wisdom" if detective == "professional":
            if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                $ add_point(KCT.BOYFRIEND)

            elif nora.relationship.value >= Relationship.FWB.value:
                $ add_point(KCT.BRO)

            else:
                $ add_point(KCT.TROUBLEMAKER)
                
            scene v15s45_7a
            with dissolve

            u "If a detective sits down on his ass, he also sits down in his mind."

        "Analyze Chloe" if detective == "psychologist":
            if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                $ add_point(KCT.BRO)

            elif nora.relationship.value >= Relationship.FWB.value:
                $ add_point(KCT.TROUBLEMAKER)

            else:
                $ add_point(KCT.BOYFRIEND)
                
            scene v15s45_7a
            with dissolve

            u "Hmm, deflecting the attention to us this early in the conversation? You must be nervous, Chloe."

        "Kick a chair" if detective == "loose_cannon":
            if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                $ add_point(KCT.TROUBLEMAKER)

            elif nora.relationship.value >= Relationship.FWB.value: 
                $ add_point(KCT.BOYFRIEND)

            else:
                $ add_point(KCT.BRO)
                
            scene v15s45_6a # FPP. MC kicks the nearest chair, with a forceful expression, Amber has a slight smile looking at Mc mouth is closed, Chloe has a shocked expression, looking at Mc
            with dissolve

            u "That's what I think about sitting down!"

            if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                scene v15s45_7b # same as v15s45_7a Chloe gets a little turned on, looking at Mc seductively, with a smirk
                with dissolve

                pause 1.5

            else: 
                scene v15s45_7c # FPP. same as v15s45_7a Chloe has a weirded out expression, still looking at Mc, mouth is still closed
                with dissolve

                pause 0.75

    scene v15s45_7
    with dissolve

    cl "Okay, then."

    scene v15s45_7d # FPP. Chloe looks at her phone, still no expression, mouth is still closed
    with dissolve

    pause 0.75

    scene v15s45_7a
    with dissolve

    cl "I don't have much time for this, though so-"

    scene v15s45_8 # FPP. Show only Amber looking at Chloe, slightly serious expression, mouth is open
    with dissolve

    am "You're on our time now, missy. You leave when we say you can leave!"

    scene v15s45_7e # FPP. same as v15s45_7 Chloe is looking at Amber, still no expression, mouth is still open
    with dissolve

    cl "So, I'm being held hostage... In my own home?"

    scene v15s45_7a
    with dissolve

    u "Zip it, baby doll!"

    if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
        scene v15s45_7f # FPP. same as v15s45_7 Chloe has a slight smile, still looking at Mc, mouth is still open
        with dissolve

        cl "[name], why are you talking like that?"

        scene v15s45_7a
        with dissolve

        u "For the purposes of this conversation, you and I have had no previous contact. Do you understand, civilian?"

        scene v15s45_7
        with dissolve

        cl "Civilian?"

    else:
        scene v15s45_7
        with dissolve

    cl "Is this some kind of weird role-play?"

    scene v15s45_7a
    with dissolve

    u "Role-play? What's a role-play?"

    scene v15s45_7g # FPP. same as v15s45_7 Chloe has an annoyed expression, still looking at Mc, mouth is still open
    with dissolve

    cl "Okay, whatever. Just get on with whatever the hell you guys are doing."

    scene v15s45_7h # FPP. same as v15s45_7g Chloe's mouth is closed, still an annoyed expression, still looking at Mc
    with dissolve

    u "I'm glad you've finally decided to play ball."

    scene v15s45_7g
    with dissolve

    cl "I have no idea where Nora is, so you're wasting your time."

    cl "And if you haven't noticed, we're not exactly best friends. So why would I know anything?"

    scene v15s45_7h
    with dissolve

    menu:
        "Where do you think?":
            if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                $ add_point(KCT.BOYFRIEND)

            elif nora.relationship.value >= Relationship.FWB.value:
                $ add_point(KCT.TROUBLEMAKER)

            else:
                $ add_point(KCT.BRO)
                        
            scene v15s45_7h
            with dissolve

            u "Even so, you must have an idea where she might have gone?"

            scene v15s45_7
            with dissolve

            cl "I. Don't. Know."

            scene v15s45_8
            with dissolve

            am "Think harder, damnit!"

            scene v15s45_7a
            with dissolve

            u "Who would she run to in a time of need?"

            scene v15s45_7
            with dissolve

            cl "...Mr. Rose? I guess?"

        "Who was she with?":
            if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                $ add_point(KCT.BRO)

            elif nora.relationship.value >= Relationship.FWB.value:
                $ add_point(KCT.BOYFRIEND)

            else:
                $ add_point(KCT.TROUBLEMAKER)
                        
            scene v15s45_7a
            with dissolve

            u "Who was she last seen with?"

            scene v15s45_7
            with dissolve

            cl "Um, I saw her get into a cab after we landed... but she was alone. That's the last I saw of her, I swear."

            scene v15s45_7a
            with dissolve

            u "Okay, and any idea where she was headed?"

            scene v15s45_7g
            with dissolve

            cl "How would I know?"

            scene v15s45_8
            with dissolve

            am "Picture yourself in her shoes. She's in need, and wants to get away for a while... Who does she call?"

            scene v15s45_7e
            with dissolve

            cl "Probably Mr. Rose, her dad."

        "You're lying" if detective == "professional":
            if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                $ add_point(KCT.BOYFRIEND)
                
            elif nora.relationship.value >= Relationship.FWB.value:
                $ add_point(KCT.BRO)
                
            else:
                $ add_point(KCT.TROUBLEMAKER)
                
            scene v15s45_7h
            with dissolve

            u "You're already lying, but I don't think you realize it. You've known Nora for a long time..."

            scene v15s45_7g
            with dissolve

            cl "Yeah, so?"

            scene v15s45_7h
            with dissolve

            u "Let's just say she was desperate to get away, to feel protected. Who's she going to call?"

            scene v15s45_7f
            with dissolve

            cl "Mr. Rose, probably? Her daddy? *Giggles* Whatever she needs, he'll get it for her."

        "Appeal to her ego" if detective == "psychologist":
            if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                $ add_point(KCT.BRO)
                
            elif nora.relationship.value >= Relationship.FWB.value:
                $ add_point(KCT.TROUBLEMAKER)
                
            else:
                $ add_point(KCT.BOYFRIEND)

            scene v15s45_7h
            with dissolve

            u "It's obvious you're very intelligent, Chloe. You're kind and considerate."

            scene v15s45_7i # FPP. same as v15s45_7f Chloe's mouth is closed, still a slight smile, still looking at Mc
            with dissolve

            u "And I'll bet your observation skills are more powerful than you realize."

            scene v15s45_7f
            with dissolve

            cl "Well, thank you."

            scene v15s45_7i
            with dissolve

            u "It's probably easy for you to think of the one place Nora is most likely to go to in a time of need..."

            scene v15s45_7f
            with dissolve

            cl "Oh, well yeah. That would be her father."

        "Accuse Chloe" if detective == "loose_cannon":
            if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                $ add_point(KCT.TROUBLEMAKER)
                
            elif nora.relationship.value >= Relationship.FWB.value: 
                $ add_point(KCT.BOYFRIEND)
                
            else:
                $ add_point(KCT.BRO)
                
            scene v15s45_7h
            with dissolve

            u "You know because you know!"

            scene v15s45_7j # FPP. same as v15s45_7 Chloe is slightly angry, still looking at Mc, mouth is still open
            with dissolve

            cl "What does that even mean?! Why are you yelling?"

            scene v15s45_7k # FPP. same as v15s45_7j Chloe's mouth is closed, still slight angry expression, still looking at Mc
            with dissolve

            u "Who's to say you didn't team up with Chris and have Nora taken care of?! You both have a motive!"

            scene v15s45_8
            with dissolve

            am "*Gasps* He's right..."

            scene v15s45_7j
            with dissolve

            cl "What?! Are you guys fucking crazy?"

            scene v15s45_7k
            with dissolve

            u "Where's Nora, Chloe? Who could she be with right now?"

            scene v15s45_7j
            with dissolve

            cl "Stop yelling at me!"

            scene v15s45_7k
            with dissolve

            u "If we don't get answers soon, this is going to get real serious, real fast!"

            scene v15s45_6a
            with dissolve

            pause 0.75

            scene v15s45_7j
            with dissolve

            cl "Okay, okay! Can stop destroying things?! What the hell..."

            cl "She's probably with her fucking father. Mr. Rose."

            scene v15s45_7l # FPP. Chloe rolls her eyes, still a slight angry expression, mouth is still open, still looking at Mc
            with dissolve

            cl "Now calm the hell down, yeah? Jesus..."

    scene v15s45_8
    with dissolve

    am "She doesn't like her dad, though."

    scene v15s45_7e
    with dissolve

    cl "She wouldn't be there for emotional support, that's for sure."

    scene v15s45_7a
    with dissolve

    u "So, what else then?"

    scene v15s45_7
    with dissolve

    cl "He's the one with all the money, so maybe she'd go to him. Or use one of his places to hideout."
    $ v15_nora_clues.add("runs_dad")

    scene v15s45_8
    with dissolve

    am "And what about Ms. Rose?"

    scene v15s45_7e
    with dissolve

    cl "Lorraine?"

    scene v15s45_8
    with dissolve

    am "Would you say that Nora and Ms. Rose are close?"

    scene v15s45_7e
    with dissolve

    cl "Yeah, that's fair to say."

    scene v15s45_8
    with dissolve

    am "Really close?"

    scene v15s45_7e
    with dissolve

    cl "Yeah, I mean. She prefers to spend time with her."
    $ v15_nora_clues.add("close_rose")

    scene v15s45_8
    with dissolve

    am "Do you think Nora could be with Ms. Rose right now?"

    scene v15s45_7e
    with dissolve

    cl "It's possible, I guess."

    scene v15s45_7e
    with dissolve

    cl "Maybe she saw them both briefly to tell them about the breakup, who knows?"

    scene v15s45_7a
    with dissolve

    menu:
        "Who else?":
            if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                $ add_point(KCT.BOYFRIEND)

            elif nora.relationship.value >= Relationship.FWB.value:
                $ add_point(KCT.TROUBLEMAKER)

            else:
                $ add_point(KCT.BRO)
                        
            scene v15s45_7a
            with dissolve

            u "Is there anyone else that could be helping her, who she might have gone to?"

            scene v15s45_7m # FPP. same as v15s45_7a Chloe looks down, hand on chin, thinking for a moment
            with dissolve

            pause 0.75

            scene v15s45_7
            with dissolve

            cl "The only other person I can think of would be her ex-boyfriend."

            scene v15s45_8
            with dissolve

            am "Someone else this whole time? Now that would be a plot twist!"

            scene v15s45_8a # FPP. same as v15s45_8 Amber is looking at Mc, slight smile, mouth is closed
            with dissolve

            u "(No shit it would...)"

            scene v15s45_7
            with dissolve

            cl "Yeah, her ex from before."

            scene v15s45_7a
            with dissolve

            u "The ex-ex-boyfriend?"

            scene v15s45_7
            with dissolve

            cl "Yes, but I never met him. I just remember her talking about him."

            cl "But guys, this was like ages ago. So don't ask me for his name, I can't remember."

            cl "I think he lives round here though, or at least he used to."
            
            $ v15_nora_locations.add("ex")

            scene v15s45_7a
            with dissolve

            u "How conveniently vague..."

            scene v15s45_8a
            with dissolve

            am "Mhmm..."

            scene v15s45_7j
            with dissolve

            cl "It's not like that! All I remember is that she still kept in touch with the guy."

            scene v15s45_7
            with dissolve
    
            cl "But that's Nora for you, always looking to the past..."
            $ v15_nora_clues.add("likes_ex")

        "Refer to a past clue":
            if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                $ add_point(KCT.BRO)

            elif nora.relationship.value >= Relationship.FWB.value:
                $ add_point(KCT.BOYFRIEND)

            else:
                $ add_point(KCT.TROUBLEMAKER)
                        
            scene v15s45_7
            with dissolve

            u "So, we have it on good authority that Nora likes rubbing sticks in the wilderness."

            scene v15s45_7f
            with dissolve

            cl "Ha! Who told you that?"

            scene v15s45_7a
            with dissolve

            u "Um, someone was investigating her Kiwii profile..."

            scene v15s45_7
            with dissolve

            cl "Well, I mean... Sure, she likes nature. Who doesn't?"

            scene v15s45_7g
            with dissolve

            cl "But Nora? She's not slumming it in the woods, rubbing sticks together. She's too spoiled for that."

            scene v15s45_7h
            with dissolve

            u "Spoiled?"

            scene v15s45_7g
            with dissolve

            cl "Mr. Rose took her on a camping trip when she was a kid. She said she hated it..."
            cl "I think you might need to take another look at your evidence."
            $ v15_nora_clues.add("hates_camping")

            scene v15s45_8
            with dissolve

            am "Don't tell us how to do our job, blondie! This is our operation!"

        "Use your logic" if detective == "professional":
            if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                $ add_point(KCT.BOYFRIEND)

            elif nora.relationship.value >= Relationship.FWB.value:
                $ add_point(KCT.BRO)

            else:
                $ add_point(KCT.TROUBLEMAKER)
                
            scene v15s45_7a
            with dissolve

            u "Can you confirm that Nora loves nature?"

            scene v15s45_7f
            with dissolve

            cl "Oh, haha... She likes to say she does."

            cl "You know, a walk down a designated nature trail? But she's not the type to get her hands dirty, that's for sure."

            $ v15_nora_clues.add("hates_camping")
            cl "The first and last time she went camping was with her dad. She hated it! Couldn't stand the bugs and the cold."

            scene v15s45_8a
            with dissolve

            u "Hmm, interesting..."

            scene v15s45_8b # FPP. same as v15s45_8a Amber's mouth is open, still looking at Mc, still a slight smile
            with dissolve

            am "That's new information."

        "Extract relationship info" if detective == "psychologist":
            if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                $ add_point(KCT.BRO)

            elif nora.relationship.value >= Relationship.FWB.value:
                $ add_point(KCT.TROUBLEMAKER)

            else:
                $ add_point(KCT.BOYFRIEND)
                
            scene v15s45_7a
            with dissolve

            u "When a relationship breaks down, the mind tends to wander to the past. Reflecting on the good..."

            u "Is there anyone that Nora might be thinking about right now?"

            scene v15s45_7m
            with dissolve

            cl "Well..."

            scene v15s45_7a
            with dissolve

            cl "This was a long time ago, but I remember her telling me about her boyfriend before Chris. They seemed to stay in touch."

            scene v15s45_8
            with dissolve

            am "So maybe she still likes him, even now?"

            if nora.relationship.value >= Relationship.FWB.value:
                scene v15s45_8a
                with dissolve

                u "(*Sighs*)"

            scene v15s45_7
            with dissolve

            cl "No, no, no. She would never go back to him, it's just that they had good memories together, and always stayed friends."
            $ v15_nora_clues.add("likes_ex")

            scene v15s45_7a
            with dissolve

            u "Could she have gone to see him?"

            scene v15s45_7
            with dissolve

            cl "I can't say that she would have. He lives nearby, I think. Or he used to at least."

            $ v15_nora_locations.add("ex")

            cl "Like I said, it was a long time ago. I don't even remember his name."

        "Angry mode" if detective == "loose_cannon":
            if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                $ add_point(KCT.TROUBLEMAKER)

            elif nora.relationship.value >= Relationship.FWB.value: 
                $ add_point(KCT.BOYFRIEND)

            else:
                $ add_point(KCT.BRO)
                
            scene v15s45_7a
            with dissolve

            u "I can't stand these vague answers anymore!"

            scene v15s45_7k
            with dissolve

            u "It's just making me so... so... ANGRY!"

            scene v15s45_6b # TPP. same as v15s45_6 MC grabs his shirt, looking like he's trying to rip it off with a strained expression, Amber and Chloe looking at him with no expessions, mouths are still closed
            with dissolve

            pause 0.75

            scene v15s45_6c # TPP. same as v15s45_6b Mc loosens the grip on his shirt is looking at Chloe with a disappointed expression, Amber and Chloe are looking at Mc with awkward expressions, mouths are still closed
            with dissolve

            u "..."

            scene v15s45_8a
            with dissolve

            u "It always looks so easy in the movies..."

            scene v15s45_6d # TPP. same as v15s45_6c Mc has completely let go of his shirt hands to his sides still a disappointed expression, Amber and Chloe are looking at each other and laughing, mouths are open
            with dissolve

            pause 0.75

    scene v15s45_7d
    with dissolve

    pause 0.75

    scene v15s45_7g
    with dissolve

    cl "Okay. Now that I've given you ten minutes of my time, and you're both being freaks..."

    cl "I'm going to leave now."

    cl "Some people have important business to take care of."

    scene v15s45_6e # TPP. Chloe stands up walks away from Amber and Mc with an annoyed expression ignoring both of them, Amber is looking at Chloe holding out a hand towards Chloe serious expression mouth is open, Mc has a slightly serious expression looking at Chloe mouth is closed
    with dissolve

    am "Hey!"

    scene v15s45_9 # FPP. Show only Chloe walking out of the Chicks Frat House front door, her back is turned to Mc
    with dissolve

    pause 0.75

    scene v15s45_9a # FPP. same as v15s45_9 Chloe slams the door shut behind her
    with dissolve

    pause 0.75

    scene v15s45_9b # FPP. same as v15s45_9a Show Amber looking at the closed front door, mouth is open, slightly serious expression
    with dissolve

    am "Okay, yeah! You're dismissed."

    scene v15s45_9c # FPP. same as v15s45_9b Amber is now looking at Mc, mouth is closed, slight smile
    with dissolve

    u "Again... Already gone."

    scene v15s45_9d # FPP. same as v15s45_9c Amber's mouth is open, still looking at Mc, still a slight smile
    with dissolve

    am "We got what we needed anyway."

    scene v15s45_9c
    with dissolve

    u "We're kind of good at this."

    scene v15s45_9d
    with dissolve

    am "Right? I might do this more often, for missing dogs and things like that..."

    scene v15s45_9c
    with dissolve

    u "*Laughs* Sure, everyone needs a hobby."

    u "Should we head back now?"

    scene v15s45_9d
    with dissolve

    am "Yeah, let's return to HQ and wrap this thing up."

    scene v15s45_3a # FPP. same as v15s45_3 The front door is closed, Chloe is not in the render, Mc and Amber are walking away from the house, slight smiles, mouths are closed
    with fade

    pause 0.75

    jump v15s46