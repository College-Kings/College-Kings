# SCENE 50: Mc goes to bed WOLVES OR APES (both)
# Locations: Ape Dorm Room, Wolves Dorm Room 
# Characters: MC (Outfit: Boxers/Underwear), [BABY_NAME] (Outfit: None), NORA (Outfit: 1), CHLOE (Outfit: 3)
# Time: Wednesday Night

label v16s50:  ### ERROR: 50) Baby night, Partner only
    if not joinwolves:        
        # -reminder that [baby_name] with Nora can be Henry or PlayerChosen and Chloe's can be Plastic or PlayerChosen
        # -MC's phone vibrates, making him jolt-
        play sound "sounds/vibrate.mp3"
        
        scene v16s50_1   # TPP Close up on MC' face (surprised, eyes wide open, mouth open) laying in his bed [APE ROOM]
        with vpunch
        
        u "(Huh? Who's calling this late?)"

        scene v16s50_2   # TPP MC (no expression, mouth closed) sits up in his bed [APE ROOM]
        with dissolve

        pause 0.75

        scene v16s50_3   # TPP MC (no expression, mouth closed) [sitting on edge of bed near nightstand] takes his phone off the night stand [APE ROOM]
        with dissolve

        pause 0.75

        play sound "sounds/vibrate.mp3"
        
        # -MC looks at his phone-
        scene v16s50_4   # TPP MC (no expression, mouth closed) sits on the his bed, his back against the corner looking at his phone [APE ROOM]
        with dissolve

        u "(Oh, shit. Must be about [v16_baby_name]...)"

    else: # WOLF ROOM 
        # -reminder that [baby_name] with Nora can be Henry or PlayerChosen and Chloe's can be Plastic or PlayerChosen
        # -MC's phone vibrates, making him jolt-
        play sound "sounds/vibrate.mp3"
        
        scene v16s50_11   # TPP Close up on MC' face (surprised, eyes wide open, mouth open) laying in his bed [WOLF ROOM]
        with vpunch
        
        u "(Huh? Who's calling this late?)"

        scene v16s50_12   # TPP MC (no expression, mouth closed) sits up in his bed [WOLF ROOM]
        with dissolve

        pause 0.75

        scene v16s50_13   # TPP MC (no expression, mouth closed) [sitting on edge of bed near nightstand] takes his phone off the night stand [WOLF ROOM]
        with dissolve

        pause 0.75

        play sound "sounds/vibrate.mp3"
        
        # -MC looks at his phone-
        scene v16s50_14   # TPP MC (no expression, mouth closed) sits on the his bed, his back against the corner looking at his phone [WOLF ROOM]
        with dissolve

        u "(Oh, shit. Must be about [v16_baby_name]...)"

    if not v16s27_parent_chloe:  # -if partner is Nora [Checkpoint 1.1]
        # -Split-screen with Nora?-
        scene v16s50_5   # SPLIT MC (worried, mouth open) holding his phone with his right hand to his ear [generic wall behind him]/ Nora (tired, mouth closed) holding phone with left hand [any Chicks room behind her].
        with dissolve

        u "Hey, Nora. Everything okay with [v16_baby_name]?"

        play sound "sounds/babycry.mp3"

        scene v16s50_5a  # SPLIT MC (worried, mouth closed) holding his phone with his right hand to his ear [generic wall behind him]/ Nora (tired, mouth open) holding phone with left hand [any Chicks room behind her].
        with dissolve

        baby "*Crying*"
        
        no "No, not really! All I want to do is sleep and the baby won't let me..."

        scene v16s50_5
        with dissolve

        u "You can't make it stop?"

        play sound "sounds/babycry.mp3"
        
        baby "*Crying*"

        scene v16s50_5a
        with dissolve

        no "I'm just too tired right now to remember what key we use for feeding it... I'm so sorry to have woken you up, but- Can you remember?"
        
        menu: 
        # -MC chooses event1, event2 or event3
        # -event1 Blue (CORRECT)
        # -event2 Green
        # -event3 Orange

            "Blue": # -if Blue
                scene v16s50_5
                with dissolve

                u "It's the blue one, I think."

                play sound "sounds/babycry.mp3"

                baby "*Crying*"
                
                scene v16s50_5b   # SPLIT MC (worried, mouth closed) holding his phone with his right hand to his ear [generic wall behind him]/ Nora (tired, mouth open) holding phone with left hand, looking down [At baby OC in her lap]) [any Chicks room behind her].
                with dissolve

                no "Blue? Let's see..."

                play sound "sounds/babycoo.mp3"

                scene v16s50_6   # SPLIT MC (slight smile, mouth closed) holding his phone with his right hand to his ear [generic wall behind him]/ Nora (relieved, smiling, mouth open) holding phone with left hand. [any Chicks room behind her].
                with dissolve

                no "Yes! It stopped crying! Okay, so it's blue for feeding, green for burping, orange for diaper change, right?"

                scene v16s50_6a   # SPLIT MC (slight smile, mouth open) holding his phone with his right hand to his ear [generic wall behind him]/ Nora (relieved, smiling, mouth closed) holding phone with left hand. [any Chicks room behind her].
                with dissolve

                u "Yeah, think that's right."

                scene v16s50_6  
                with dissolve

                no "I've got it clear in my head again now, thank you!"
                
            "Green": # -if Green
                scene v16s50_5
                with dissolve

                u "Green? I think?"

                scene v16s50_5a
                with dissolve

                no "You think?"

                play sound "sounds/babycry.mp3"
                
                baby "*Crying*"

                scene v16s50_5
                with dissolve

                u "I'm pretty sure."

                scene v16s50_5b
                with dissolve

                no "Okay, let's see..."

                play sound "sounds/babycry.mp3"

                baby "*Crying*"

                scene v16s50_5a
                with dissolve

                no "No, it didn't work."

                play sound "sounds/babycry.mp3"

                baby "*Crying*"

                scene v16s50_5b
                with dissolve
                
                no "Maybe it's blue...?"

                play sound "sounds/babycoo.mp3"

                scene v16s50_6
                with dissolve

                no "Ah ha! There. It stopped."
                
                no "Damn, I hope using the wrong key this one time doesn't affect our evaluation too much."

                scene v16s50_6a
                with dissolve

                u "Hmm, yeah, I don't know how we're being graded."

                scene v16s50_6
                with dissolve

                no "I think green is for burping, since I'm pretty sure orange is for diaper change."

                scene v16s50_6a
                with dissolve

                u "Okay, got it. Next time we'll get it right."
                
            "Orange": # -if Orange
                scene v16s50_5
                with dissolve

                u "Let's go with orange."

                scene v16s50_5a
                with dissolve

                no "That doesn't sound right."

                scene v16s50_5
                with dissolve

                u "I'm pretty sure, Nora."

                play sound "sounds/babycry.mp3"
                
                baby "*Crying*"

                scene v16s50_5b
                with dissolve

                no "Okay..."

                play sound "sounds/babycry.mp3"

                baby "*Crying*"

                scene v16s50_5a
                with dissolve

                no "Nope! I knew that wasn't it, fuck..."

                scene v16s50_5
                with dissolve

                u "Shit. Sorry."

                play sound "sounds/babycry.mp3"

                baby "*Crying*"

                scene v16s50_5b
                with dissolve

                no "It must be blue, let's see..."

                play sound "sounds/babycoo.mp3"

                scene v16s50_6
                with dissolve

                no "It worked! Okay, so... Yeah, I think orange is for diaper change, and green is for burping."
                
                no "I hope that didn't affect our evaluation too much."

                scene v16s50_6a
                with dissolve

                u "All parents make mistakes occasionally, ha. I'm sure we'll be okay."

        # -Regardless of color choice-
        scene v16s50_6
        with dissolve

        no "Well, thank you, [name]. Sorry for waking you."

        scene v16s50_6a
        with dissolve

        u "No problem. I need to get used to being woken up, anyway. Dad life."

        scene v16s50_6
        with dissolve

        no "*Laughs* Right, goodnight dad!"

    ### ERROR: [End of Checkpoint 1.1. Continue to Checkpoint 2]

    else: # -if partner is Chloe [Checkpoint 1.2]
        # -Split-screen with Chloe, she's pissed and tired-
        scene v16s50_7   # SPLIT MC (worried, mouth open) holding his phone with his right hand to his ear [generic wall behind him]/ Chloe (angry, mouth closed) holding phone with left hand [any Chicks room behind her].
        with dissolve

        u "Hey, Chloe. How-"

        play sound "sounds/babycry.mp3"

        baby "*Crying*"

        scene v16s50_7a  # SPLIT MC (worried, mouth closed) holding his phone with his right hand to his ear [generic wall behind him]/ Chloe (angry, mouth open) holding phone with left hand [any Chicks room behind her].
        with dissolve

        cl "Help me turn this fucking thing off [name]!"

        scene v16s50_7
        with dissolve

        u "What's wrong with it? Have you tried the keys?"

        scene v16s50_7a
        with dissolve

        cl "You mean the one tool we have to get this toy to stop making noise? Yes, [name]. I've tried everything!"

        play sound "sounds/babycry.mp3"

        baby "*Crying*"
        
        cl "I think this one's defective, I'm not kidding. We've got a broken baby!"

        play sound "sounds/babycry.mp3"

        baby "*Crying*"
    
        cl "Shut up, already!"

        play sound "sounds/babycry.mp3"
        
        baby "*Crying*"

        scene v16s50_7
        with dissolve

        u "Maybe we should figure out what it wants. When did you last feed it?"

        scene v16s50_7b  # SPLIT MC (worried, mouth closed) holding his phone with his right hand to his ear [generic wall behind him]/ Chloe (angry, mouth open, screaming) holding phone in front of her mouth with her left hand. [any Chicks room behind her].
        with dissolve

        cl "I've tried all the keys! Why aren't you listening?"

        menu:
        # -MC chooses event1 or event2
        # -event1 Be calm
        # -event2 Be frustrated

            "Be calm": # -if Be calm
                scene v16s50_7c   # SPLIT MC (worried, mouth open) holding his phone with his right hand to his ear [generic wall behind him]/ Chloe (angry, mouth closed) holding phone with right hand [any Chicks room behind her].
                with dissolve

                u "Just relax and think for a second... When did you last feed it?"

                scene v16s50_7d  # SPLIT MC (worried, mouth closed) holding his phone with his right hand to his ear [generic wall behind him]/ Chloe (angry, mouth open) holding phone with right hand [any Chicks room behind her].
                with dissolve

                cl "I haven't fed it once! It won't let me!"

                play sound "sounds/babycry.mp3"

                baby "*Crying*"
                
                cl "It doesn't respond to anything!"

                play sound "sounds/babycry.mp3"

                baby "*Crying*"

                scene v16s50_7c
                with dissolve

                u "It's programmed to respond to the correct key."

                scene v16s50_7d
                with dissolve

                cl "*Scoffs* You're no help."            

                # -Chloe hangs up-
                play sound "sounds/hangup.mp3"

            "Be frustrated": # -if Be frustrated
                scene v16s50_7e   # SPLIT MC (frustrated, mouth open) holding his phone with his right hand to his ear [generic wall behind him]/ Chloe (angry, mouth closed) holding phone with right hand [any Chicks room behind her].
                with dissolve
                
                u "I'm trying to help you, Chloe. Stop yelling and think for a second! Have any of the keys worked since you picked up the baby?"

                scene v16s50_7f  # SPLIT MC (frustrated, mouth closed) holding his phone with his right hand to his ear [generic wall behind him]/ Chloe (angry, mouth open) holding phone with right hand [any Chicks room behind her].
                with dissolve

                cl "No! I just told you-"

                play sound "sounds/babycry.mp3"

                baby "*Crying*"

                scene v16s50_7e
                with dissolve

                u "So, try them all again! Start with the blue key."

                scene v16s50_7f
                with dissolve

                cl "Blue is for feeding! I've already done that."

                play sound "sounds/babycry.mp3"

                baby "*Crying*"

                scene v16s50_7e
                with dissolve

                u "Try. It. Again."

                scene v16s50_7b
                with dissolve

                cl "O-fucking-kay!"

                scene v16s50_7g   # SPLIT MC (frustrated, mouth closed) holding his phone with his right hand to his ear [generic wall behind him]/ Chloe (angry, mouth closed) holding phone with right hand, slightly looking down [At baby OC in her lap] [any Chicks room behind her].
                with dissolve

                cl "..."

                scene v16s50_7h   # SPLIT MC (frustrated, mouth open) holding his phone with his right hand to his ear [generic wall behind him]/ Chloe (surprised, mouth closed) holding phone with right hand, slightly looking down [At baby OC in her lap] [any Chicks room behind her].
                with dissolve

                u "So?"

                scene v16s50_7i   # SPLIT MC (frustrated, mouth closed) holding his phone with his right hand to his ear [generic wall behind him]/ Chloe (surprised, mouth closed) holding phone with right hand [any Chicks room behind her].
                with dissolve

                pause 0.75

                play sound "sounds/babycoo.mp3"

                scene v16s50_7j   # SPLIT MC (neutral, mouth closed) holding his phone with his right hand to his ear [generic wall behind him]/ Chloe (surprised, mouth open) holding phone with right hand [any Chicks room behind her].
                with dissolve

                cl "It stopped."

                scene v16s50_7k   # SPLIT MC (neutral, mouth open) holding his phone with his right hand to his ear [generic wall behind him]/ Chloe (surprised, mouth closed) holding phone with right hand, [any Chicks room behind her].
                with dissolve

                u "Hmm. Interesting."

                scene v16s50_7i
                with dissolve

                cl "..."

                scene v16s50_7j
                with dissolve

                cl "I swear I had tried that already."
                
                u "(What a nightmare...)"

                play sound "sounds/babycry.mp3"

                baby "*Crying*"

                scene v16s50_7f
                with dissolve

                cl "Oh, what the actual fuck?! It's crying again, [name]!"

                scene v16s50_7e
                with dissolve

                u "Chloe, probably because you're yelling curse words!  It probably needs burping. Use the-"

                scene v16s50_7b
                with dissolve

                cl "Screw the fucking keys! I'll show it how to burp alright-"

                play sound "sounds/hangup.mp3"
                
            # -Chloe hangs up-
                if not joinwolves:
                    scene v16s50_8    # TPP MC (neutral, mouth open) looking at his phone that he holds in his right hand [APE ROOM].
                    with dissolve

                    u "Chloe? *Sighs*"

                    scene v16s50_8a    # TPP MC (neutral, mouth closed) looking at his phone that he holds in his right hand [APE ROOM]
                    with dissolve

                    u "(Jeez... Poor [v16_baby_name]... At least she's not yelling at me anymore.)"

                else: # WOLF
                    scene v16s50_18    # TPP MC (neutral, mouth open) looking at his phone that he holds in his right hand [WOLF ROOM].
                    with dissolve

                    u "Chloe? *Sighs*"

                    scene v16s50_18a    # TPP MC (neutral, mouth closed) looking at his phone that he holds in his right hand [WOLF ROOM]
                    with dissolve

                    u "(Jeez... Poor [v16_baby_name]... At least she's not yelling at me anymore.)"

        # -Regardless of response-

    ### ERROR: [End of Checkpoint 1.2. Continue to Checkpoint 2]

    #-Regardless-

    ### ERROR: [Checkpoint 2]

    if not joinwolves:
        # -MC puts the phone down, gets comfy for sleep again-
        scene v16s50_8b   # TPP MC (no expression, mouth closed) [sitting on edge of bed near nightstand] places his phone on the night stand [APE ROOM]
        with dissolve

        pause 0.75

        scene v16s50_8c    # TPP MC (no expression, mouth closed, eyes closed) under the covers laying in bed [APE ROOM].
        with dissolve

        u "(I really hope there's no more calls tonight...)"

        scene v16s50_8d    # TPP MC Close up on MC's face (no expression, mouth closed, eyes) (OC under the covers laying in bed) [APE ROOM].
        with dissolve

        u "(I'd mute my phone but, this is part of the project, I guess... Let's see how the rest of the night goes.)"
    
    else: # Wolves
        # -MC puts the phone down, gets comfy for sleep again-

        scene v16s50_18b    # TPP MC (no expression, mouth closed) [sitting on edge of bed near nightstand] places his phone on the night stand [WOLF ROOM]
        with dissolve

        pause 0.75

        scene v16s50_18c    # TPP MC (no expression, mouth closed, eyes closed) under the covers laying in bed [WOLF ROOM].
        with dissolve

        u "(I really hope there's no more calls tonight...)"

        scene v16s50_18d    # TPP MC Close up on MC's face (no expression, mouth closed, eyes) (OC under the covers laying in bed) [WOLF ROOM].
        with dissolve

        u "(I'd mute my phone but, this is part of the project, I guess... Let's see how the rest of the night goes.)"

    # -Transition to Scene 50a-

    # Set v16s50a_dotw to Thursday for s50a
    $ v16s50a_dotw = 5

    jump v16s50a