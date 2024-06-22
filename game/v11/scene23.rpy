# SCENE 23: Small Free Roam at Museum
# Location: Museum entrance hall
# Characters: MC(outfit 1), Riley(outfit 2), Mr. Lee (Outfit 1), Nora (Outfit 1), Chris (Outfit 2), Penelope (Outfit 1)
# Time: Evening

#screen 1: Riley(standing by the front of the triceratops),nora(sat on the black couch) (starting screen)
#screen 2: Chris(stood at the top of stairs next to armour case), Mr Lee(stood by male bust at bottom of stairs)(second screen moving forward from screen 1)
#screen 3: Penelope(Stood at the helm display)(to the right of screen 2)

label v11s23_freeroamstart: # Start of freeroam
    play music music.v11_Track_Scene_14 fadein 2
    call screen v11s23_entrance
    
label v11s23_chris1:
    $ freeroam8.add("chris")

    scene v11frmch1 # FPP Show Chris talking on the phone, neutral expression, mouth closed
    #with dissolve

    u "What's up Chris?"

    scene v11frmch1a # FPP Same angle as v11frmch1, Chris holding phone away from his head and looking at MC, mouth open
    with dissolve

    ch "Look man, I'm sorry but I need to handle this right now. I can't talk."

    if mc.frat == Frat.APES: # if Apes
        scene v11frmch1
        with dissolve

        u "Right, sorry."
    
    else: # if Wolves
        scene v11frmch1
        with dissolve

        u "Right, sorry... Is Sebastian still trying to prank the Apes?"

        scene v11frmch1b # Same angle as v11frmch1, Chris holding phone away from his head, smiling at MC, mouth open
        with dissolve

        ch "More than trying, he's planned a lot. It'll have to wait till we get back though."

    # Regardless of frat scene continued
    scene v11frmch1
    with dissolve

    u "Real quick, mind if I talk to you about something?"

    scene v11frmch1c # FPP Same angle as v11frmch1, Chris talking on the phone, mouth open
    with dissolve

    ch "*Sigh* Give me a second Sebastian."

    # -Anytime Chris talks to Sebastian then MC it needs to be different images-
    scene v11frmch1a
    with dissolve

    ch "What's up?"

    menu:
        "Mention Nora":
            scene v11frmch1d
            with dissolve

            u "Have you talked to Nora today?"

            scene v11frmch2 # FPP Show Nora sitting on black seating across entrance hall of museum, Nora looks upset, mouth closed
            with dissolve

            u "She doesn't look like she's enjoying herself very much."

            scene v11frmch1a
            with dissolve

            ch "I don't think she wants to talk to me right now, plus I need to handle this. She knew I'd be busy."

            scene v11frmch2
            with dissolve

            u "Dude, look at her, she's not happy."

            scene v11frmch1a
            with dissolve

            ch "If you want to try to cheer her up, then be my guest. I've tried talking to her and she doesn't listen. I can only do so much."

            scene v11frmch1d
            with dissolve

            u "I get what you're saying but... I don't know, man."

            scene v11frmch1a
            with dissolve

            ch "I gotta get back to this, [name] I only have 30 mins of battery left."

            scene v11frmch1
            with dissolve

            u "Alright."

        "Don't mention Nora":
            scene v11frmch1d # FPP Same angle as v11frmch1, Chris holding phone away from his head and looking at MC, mouth closed
            with dissolve

            u "Actually, nevermind."

            scene v11frmch1a
            with dissolve

            ch "You sure?"

            scene v11frmch1d
            with dissolve

            u "Yeah man, sorry."

            scene v11frmch1a
            with dissolve

            ch "No worries, talk to you later."

            scene v11frmch1c
            with dissolve

            ch "Bash, I'm back."

    # Back to free roam
    call screen v11s23_mid

label v11s23_mrlee1:
    $ freeroam8.add("lee")

    scene v11frmlee1 # FPP Show Mr. Lee with bust behind him, Mr. Lee looking at MC, neutral expression, mouth open
    #with dissolve

    lee "[name], did I ever tell you about when I lived here in London?"

    scene v11frmlee1a # FPP Same angle as v11frmlee1, Mr. Lee with neutral expression, mouth closed
    with dissolve

    u "You said you went on an abroad trip to China, but you never told me you've been to London."

    scene v11frmlee1
    with dissolve

    lee "Oh, I've lived in many places. I actually toured this museum many years ago."

    scene v11frmlee1a
    with dissolve

    u "That's nice."

    scene v11frmlee1
    with dissolve

    lee "It sure was, it was the year 1985."

    scene v11frmlee1b # FPP Same angle as v11frmlee1, Mr. Lee looking off into the distance in memory, mouth closed
    with dissolve

    u "(What the fuck is happening?)"

    scene v11frmlee1
    with dissolve

    lee "I was a good looking young man and just as fascinated with history as I am now."

    scene v11frmlee1a
    with dissolve

    u "I don't doubt it."

    scene v11frmlee1
    with dissolve

    lee "I had long black hair. People assumed I was a good fighter, because I was... well you know. Bruce was really famous around that time and everyone wanted to do some sort of martial arts."
    lee "Studios were popping up everywhere. I had family in the States so I visited during the summer. Have you ever been outside of the US?"

    scene v11frmlee1a
    with dissolve

    u "Well, I'm in Europe right now."

    scene v11frmlee1c # FPP Same angle as v11frmlee1, Mr. Lee smiling at MC, mouth open
    with dissolve

    lee "Ha, very true."

    scene v11frmlee1a
    with dissolve

    u "Uh... Mr. Lee, I'm gonna go check out some other stuff."

    scene v11frmlee1c
    with dissolve

    lee "And miss the best part of my story?"

    scene v11frmlee1a
    with dissolve

    u "*Sighs*"

    scene v11frmlee1
    with dissolve

    lee "I met a beautiful young lady in America. She was an artist, sculptor to be exact. She carved the finest things."
    lee "She wanted to run away from school and everything, so I took her with me to Europe."

    scene v11frmlee1a
    with dissolve

    u "Is the woman you're talking about your wife now?"

    scene v11frmlee1
    with dissolve

    lee "Oh never... We had our time, but she ruined it. I decided to continue attending school in London despite her wanting me to quit."
    lee "For months she became more and more distant until one day... she left."

    scene v11frmlee1b
    with dissolve

    u "Sounds like you missed her."

    scene v11frmlee1
    with dissolve

    lee "Well, when she left, she left behind a sculpture of a man's head. She'd been working on it for a long time."
    lee "Using what strings I had, I got her work put into this very museum. This sculpture is hers."

    scene v11frmlee1d # FPP Same angle as v11frmlee1, Mr. Lee turning and pointing at the statute, mouth closed
    with dissolve

    u "That's amazing."

    scene v11frmlee1e # FPP Same angle as v11frmlee1, Mr. Lee looking annoyed, mouth open
    with dissolve

    lee "No, no it isn't. Come to find out this sculpture is of a man she was cheating on me with and to think I'm actually the one that gifted it to the museum where it's been for 36 years."

    menu:
        "Laugh" (troublemaker=1.0):
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            scene v11frmlee1a
            with dissolve

            u "*Laughs* I'm sorry, but that was the best ending to a story I've ever heard."

            scene v11frmlee1c
            with dissolve

            lee "It wasn't so funny back then."

        "Feel bad" (bro=1.0):
            $ reputation.add_point(RepComponent.BRO)
            scene v11frmlee1b
            with dissolve

            u "Uh, I'm really sorry..."

    scene v11frmlee1e
    with dissolve

    lee "Every time I come back and it's still here it ruins my mood. I've petitioned too many times for it to be removed."

    scene v11frmlee1a
    with dissolve

    u "Maybe you should just stop coming to see it."

    scene v11frmlee1
    with dissolve

    lee "Coming to see it is the only way I know if it's gone. The museum stopped corresponding with me."

    scene v11frmlee1a
    with dissolve

    u "Oh... wow."

    scene v11frmlee1
    with dissolve

    lee "*Sighs* Give me a moment, will you [name]?"

    scene v11frmlee1a
    with dissolve

    u "Sure."

    scene v11frmlee1f # FPP same angle as v11frmlee1, Mr. Lee frowning and looking at the bust, mouth closed
    with dissolve

    u "(I hope he's alright.)"

    # Back to free roam
    call screen v11s23_mid

label v11s23_riley1:
    $ freeroam8.add("riley")

    scene v11frmri1 # FPP Show Riley leaning over barrier and reaching her arm out toward triceratops, Riley smiling with mouth closed
    #with dissolve

    u "*Whisper* Riley, you can't touch it!"

    scene v11frmri1a # FPP Same angle as v11frmri1, Riley smiling and looking at MC with mouth open
    with dissolve

    ri "Oh hush, no one's looking."

    scene v11frmri1
    with dissolve

    u "They will if you break it."

    scene v11frmri1a
    with dissolve

    ri "Look out for me, okay?"

    scene v11frmri2 # FPP Show Riley climbing under ropes to get to the triceratops
    with dissolve

    pause 0.75

    scene v11frmri2a # FPP Same angle as v11frmri2, Riley very close to triceratops skull, examining closely, mouth open
    with dissolve

    ri "Look how big this thing is! I wonder if it was a boy or a girl..."
    ri "If these things were alive right now you know we could hang out with them and pet them and they wouldn't attack us? They're grazing herbivores."

    scene v11frmri2b # FPP Same as v11frmri2a, Riley's mouth closed
    with dissolve

    u "Like prehistoric cows."

    scene v11frmri2a
    with dissolve

    ri "Exactly."

    scene v11frmri2b
    with dissolve

    u "Why are you nerding out so much right now?"

    scene v11frmri2a
    with dissolve

    ri "I'm just trying to enjoy myself."

    scene v11frmri2b
    with dissolve

    u "Shooting off a random guy's gun isn't enough excitement? *Chuckles*"

    scene v11frmri2a
    with dissolve

    ri "Yeah, no. Not really *Chuckles*"

    scene v11frmri2c # FPP Same angle as v11frmri2, Riley climbing back under ropes to get out of triceratops exhibit
    with dissolve

    u "You're lucky no one's watching you. You're gonna get us kicked outta here."

    scene v11frmri3 # FPP Show Riley looking at MC with a big smile, mouth open
    with dissolve

    ri "*Mocking voice* You're gonna get us kicked out of here! *Laughs*"

    menu:
        "Seek revenge" (troublemaker=1.0):
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            scene v11frmri3a # FPP Same angle as v11frmri3, Riley smiling with mouth closed
            with dissolve
            
            u "Haha, okay. I see how we're playing today."

            scene v11frmri3
            with dissolve

            ri "Huh? *Chuckles*"

            scene v11frmri3a
            with dissolve

            u "Yeah, just a little bit of excitement..."

            if CharacterService.is_friend(riley):
                scene v11frmri3b # FPP Same angle as v11frmri3, Riley raising her eyebrow and smiling, mouth open
                with dissolve

                ri "You don't want to start a war, [name]. I never lose."

            else:
                scene v11frmri3c # FPP Same angle as v11frmri3, Riley leaning in close to MC, Riley has a sexy expression, mouth open
                with dissolve

                ri "*Whisper* Sounds fun to me. But, don't make a promise you can't keep, [name]."

                scene v11frmri3d # FPP Same as v11frmri3c, Riley's mouth closed
                with dissolve

                u "I always keep my promises."

                scene v11frmri3c
                with dissolve

                ri "Good."

                scene v11frmri3b
                with dissolve

                ri "Now, if you were trying to be a bit more friendly instead... Just know I never lose."
    
        "Laugh it off":
            scene v11frmri3a
            with dissolve

            u "*Laughs* And then you'll be upset when you've got nothing exciting to do. You'll be screaming for my attention..."

            scene v11frmri3
            with dissolve

            ri "*Chuckles*"

            scene v11frmri3a
            with dissolve

            u "See? It's true."

            scene v11frmri3
            with dissolve

            ri "I only scream for one reason and it's not because I want attention..."

            scene v11frmri3a
            with dissolve

            u "What's the reason then?"

            if CharacterService.is_friend(riley):
                scene v11frmri3b
                with dissolve

                ri "Wouldn't you like to know?"

                scene v11frmri3a
                with dissolve

                u "That's why I asked. *Chuckles*"

                scene v11frmri3b
                with dissolve

                ri "Maybe one day you'll find out."

                scene v11frmri3a
                with dissolve

                u "(Suggestive just enough.)"

                scene v11frmri3b
                with dissolve

                ri "Also, you don't want to start a war, [name]. I never lose."
            
            else:
                scene v11frmri3c
                with dissolve

                ri "*Whisper* You already know, but I can show you again."

                scene v11frmri3d
                with dissolve

                u "Sounds good to me."

                scene v11frmri3b
                with dissolve

                ri "Also, you don't want to start a war, [name]. I never lose."

    scene v11frmri3a
    with dissolve

    u "You lost against Amber."

    scene v11frmri3 # FPP Same angle as v11frmri3, Riley looking offended, mouth open
    with dissolve

    ri "That was just one fight! And she played dirty... don't worry, I'll get her back."

    scene v11frmri3a
    with dissolve

    u "Sounds like a threat."

    scene v11frmri3
    with dissolve

    ri "More like a promise. *Chuckles*"

    scene v11frmri4 # FPP Show Mr. Lee walking by
    with dissolve

    menu:
        "Snitch on Riley":
            scene v11frmri4
            with dissolve

            u "RILEY, YOU'RE NOT SUPPOSED TO TOUCH THE DINOSAURS!"

            scene v11frmri3f # FPP Same angle as v11frmri3, Riley looking shocked with her mouth hanging open
            with dissolve

            pause 0.75

            scene v11frmri5 # FPP Show Mr. Lee and Riley standing near triceratops, Mr. Lee with mouth open, Riley with an ashamed expression and mouth closed
            with dissolve

            lee "Please tell me you're not touching them. It would cost a fortune to fix."

            scene v11frmri5a # FPP Same as v11frmri5, but Mr. Lee's mouth closed and Riley's mouth open
            with dissolve

            ri "No, uhm... I was just-"

            scene v11frmri5
            with dissolve

            lee "Please just be more mindful."

            scene v11frmri4a # FPP Same angle as v11frmri4, Mr. Lee walking away
            with dissolve

            pause 0.75

            scene v11frmri3e
            with dissolve

            ri "You just started a war, [name], I hope you're ready."

        "Don't snitch on Riley":
            scene v11frmri3a
            with dissolve

            u "*Whisper* Mr. Lee, Riley is touching the dinosaurs."

            scene v11frmri6 # TPP Show Riley playfully punching MC in the arm, both smiling, Riley's mouth open
            with dissolve

            ri "Be quiet before he actually hears you!"

            scene v11frmri3a
            with dissolve

            u "Oh, you don't like having fun?"

            scene v11frmri3b
            with dissolve

            ri "I told you not to start a war with me, but you couldn't resist. I hope you're ready."

    scene v11frmri3a
    with dissolve

    u "Oh I am! *Chuckles*"

    scene v11frmri4b # FPP Same angle as v11frmri4, Riley walking away
    with dissolve

    u "(She's a bit more feisty than I thought.)"

    # -Back to free roam-
    call screen v11s23_entrance

label v11s23_penelope1:
    $ freeroam8.add("penelope")

    scene v11frmpe1 # FPP Show Penelope starting to walk away from helmet exhibit right as MC goes to talk to her
    #with dissolve

    pause 0.75

    scene v11frmpe2 # TPP Show MC's hand grabbing Penelope's exactly like the first time they met
    with dissolve

    u "Hey."

    scene v11frmpe3 # FPP Show Penelope looking back and down at her and MC's hand, she's smiling with mouth closed
    with dissolve

    pause 0.75

    scene v11frmpe3a # FPP Same angle as v11frmpe3, Penelope looking at MC and smiling, mouth open
    with dissolve

    pe "Yes?"

    scene v11frmpe3b # FPP Same angle as v11frmpe3, Penelope looking at MC, smiling with mouth closed
    with dissolve

    u "Why are you smiling like that?"

    scene v11frmpe3a
    with dissolve

    pe "I just got deja vu of when we first met. When I started to walk off you grabbed my hand, just like that."

    scene v11frmpe3b
    with dissolve

    u "Haha, I did do that."

    scene v11frmpe3a
    with dissolve

    pe "So what's up? Did Mr. Lee ask you to have me do something else?"

    scene v11frmpe3b
    with dissolve

    u "What? No. *Chuckles* Why'd you ask that?"

    scene v11frmpe3a
    with dissolve

    pe "Because he's still making me do everything. Even the smallest little things he doesn't want to do, he'll ask me."

    scene v11frmpe3b
    with dissolve

    u "What are you headed to do now?"

    scene v11frmpe3c # FPP Same angle as v11frmpe3, Penelope looking at MC, she looks annoyed with mouth open
    with dissolve

    pe "He asked me to get water in case anyone wanted one. I've already looked around, but I can't find them."

    scene v11frmpe3d # FPP Same angle as v11frmpe3, Penelope looking at MC, neutral expression, mouth closed
    with dissolve

    u "Where'd he say they were?"

    scene v11frmpe3c
    with dissolve

    pe "He said the staff said it was okay if we got some from the staff closet, but I didn't see one."

    scene v11frmpe3d
    with dissolve

    u "I'll help you."

    scene v11frmpe3a
    with dissolve

    pe "[name] it's okay, really."

    scene v11frmpe3b
    with dissolve

    u "Do you really think telling me that will stop me from helping you?"

    scene v11frmpe3a
    with dissolve

    pe "*Sighs* Haha, no."

    scene v11frmpe3b
    with dissolve

    u "Let's find that closet."

    scene v11frmpe4 # TPP Show MC and Penelope looking around museum back hallways
    with dissolve

    pause 0.75

    scene v11frmpe6 # FPP View looking into a big supply closet from the doorway
    with dissolve

    u "Found it."

    scene v11frmpe7 # FPP View from inside closet, looking at cases of bottled water on the shelf
    with dissolve

    u "They're right there."

    scene v11frmpe8 # FPP Looking down at Penelope, who is sitting down on the floor of the closet. Penelope with neutral expression, mouth open
    with dissolve

    pe "Thanks for helping me. Feel free to go back, I'm gonna hide in here for a second."

    scene v11frmpe8a # FPP Same as v11frmpe8, Penelope with mouth closed
    with dissolve

    u "Haha."

    scene v11frmpe9 # TPP Show MC sitting down on the closet floor next to Penelope
    with dissolve

    pause 0.75

    scene v11frmpe10 # FPP View of MC looking at Penelope, both sitting on closet floor. Penelope with neutral expression, mouth closed
    with dissolve

    u "I'll wait with you."

    scene v11frmpe10a # FPP Same angle as v11frmpe10, Penelope looking curious with mouth open
    with dissolve

    pe "Why are you so nice to me?"

    scene v11frmpe10
    with dissolve

    u "Should I not be?"

    scene v11frmpe10a
    with dissolve

    pe "No no, it's not that. I'm just not used to it. You literally go out of your way to help me."

    if CharacterService.is_dating(penelope):
        menu:
            "Flirt" (boyfriend=1.0):
                $ v11s23_penelope_date = True
                $ reputation.add_point(RepComponent.BOYFRIEND)

                scene v11frmpe10
                with dissolve

                u "Who wouldn't help someone as pretty as you?"

                scene v11frmpe10b # FPP Same angle as v11frmpe10, Penelope smiling with mouth open
                with dissolve

                pe "*Chuckles* Did you just call me pretty?"

                scene v11frmpe10c # FPP Same angle as v11frmpe10, Penelope smiling with mouth closed
                with dissolve

                u "Pretty sure I did."

                play sound sound.kiss

                scene v11frmpe11 # TPP Show Penelope leaning over and kissing MC on the lips
                with dissolve

                pause 0.75

                scene v11frmpe10b
                with dissolve

                pe "I really like you, [name]."

                scene v11frmpe10c
                with dissolve

                u "I like you too."

                scene v11frmpe10b
                with dissolve

                pe "When we get back do you think we could go on a real date?"

                if bowling:
                    scene v11frmpe10c
                    with dissolve

                    u "I'd love that."

                    scene v11frmpe10b
                    with dissolve

                    pe "We can't go bowling though, I wouldn't want to do that to you. *Chuckles*"

                scene v11frmpe10c
                with dissolve

                u "Haha, what do you wanna do?"

                scene v11frmpe10b
                with dissolve

                pe "Don't laugh, but I really wanna go on a picnic. I've never been on one."

                scene v11frmpe10c
                with dissolve

                u "I can make that happen. Maybe. *Chuckles*"

                scene v11frmpe10b
                with dissolve

                pe "You're not funny. *Laughs*"

                scene v11frmpe10c
                with dissolve

                u "Then why are you laughing?"

                scene v11frmpe10b
                with dissolve

                pe "Okay... you're a little funny."

            "Just being me":
                scene v11frmpe10c
                with dissolve

                u "Haha, I'm just being myself."

                scene v11frmpe10b
                with dissolve

                pe "Well, yourself is a really good person."

                scene v11frmpe10c
                with dissolve

                u "Thanks."

                scene v11frmpe10b
                with dissolve

                pe "There should really be more people like you."

                scene v11frmpe10c
                with dissolve

                u "Okay stop, I'm not all that."

                scene v11frmpe10b
                with dissolve

                pe "You really are though! First you save me from paying $15,000 and now you're helping me with the water. Big problems or small problems, you're there to help."

                scene v11frmpe10c
                with dissolve

                u "I should sign up to be a superhero."

                scene v11frmpe10d # FPP Same angle as v11frmpe10, Penelope laughing hard
                with dissolve

                pe "Captain Lawyer Waterboy. *Laughs*"

                scene v11frmpe10c
                with dissolve

                u "Nevermind... scratch that idea."

    else:
        menu:
            "Just being me":
                scene v11frmpe10c
                with dissolve

                u "Haha, I'm just being myself."

                scene v11frmpe10b
                with dissolve

                pe "Well, yourself is a really good person."

                scene v11frmpe10c
                with dissolve

                u "Thanks."

                scene v11frmpe10b
                with dissolve

                pe "There should really be more people like you."

                scene v11frmpe10c
                with dissolve

                u "Okay stop, I'm not all that."

                scene v11frmpe10b
                with dissolve

                pe "You really are though! First you save me from paying $15,000 and now you're helping me with the water. Big problems or small problems, you're there to help."

                scene v11frmpe10c
                with dissolve

                u "I should sign up to be a superhero."

                scene v11frmpe10d
                with dissolve

                pe "Captain Lawyer Waterboy. *Laughs*"

                scene v11frmpe10c
                with dissolve

                u "Nevermind... scratch that idea."

            "Make a joke":
                scene v11frmpe10c
                with dissolve

                u "Oh I'm only helping you to win your trust. After I've gained your trust I'm gonna get you to give me your bank information and rob you for everything you've got."

                scene v11frmpe10b
                with dissolve

                pe "I get you're trying to be funny, but I'm actually dumb enough to fall for that. *Chuckles*"

                scene v11frmpe10c
                with dissolve

                u "The genius Penelope is gullible?"

                scene v11frmpe10b
                with dissolve

                pe "A little bit."

                scene v11frmpe10c
                with dissolve

                u "Don't worry, I'm pretty gullible too. That's why I got bullied so much when I was little."

                scene v11frmpe10a
                with dissolve

                pe "Oh wow, I'm so sorry about that."

                scene v11frmpe10
                with dissolve

                u "It's okay."

                scene v11frmpe10a
                with dissolve

                pe "How is it okay that you got bullied?"

                scene v11frmpe10
                with dissolve

                u "*Chuckles* Because I never did, Miss Gullible."

                scene v11frmpe11a # TPP Same angle as v11frmpe11, Penelope playfully punching MC in the arm, Penelope smiling with mouth open
                with dissolve

                pe "That's not funny."

    # Regardless of everything scene continued
    scene v11frmpe10b
    with dissolve

    pe "You know, you remind me of my favorite actor. *Chuckles*"

    scene v11frmpe10c
    with dissolve

    u "Haha, who?"

    scene v11frmpe10b
    with dissolve

    pe "Don't be offended, okay?"

    scene v11frmpe10c
    with dissolve

    u "Well now I feel like I'm going to be."

    scene v11frmpe10b
    with dissolve

    pe "It's not that bad. You remind me of Channing Tatum."

    scene v11frmpe10c
    with dissolve

    u "The one from the stripper movie? So I remind you of a stripper?"

    scene v11frmpe10b
    with dissolve

    pe "No no, you just look like him."

    scene v11frmpe10c
    with dissolve

    u "Oh okay, sure. I thought you found out about my stripper abilities."

    scene v11frmpe10d
    with dissolve

    pe "Haha, I know about them now."

    scene v11frmpe10c
    with dissolve

    u "So, do you think we should be taking these waters back now? *Chuckles*"

    scene v11frmpe10b
    with dissolve

    pe "Oh shoot, I literally forgot, haha."

    scene v11frmpe10c
    with dissolve

    u "*Chuckles* Let's go."

    scene v11frmpe12 # TPP Show MC and Penelope picking up as many bottles of water as they can carry
    with dissolve

    pause 0.75

    scene v11frmpe13 # TPP Show MC and Penelope carrying bottles of water into museum entrance hall
    with dissolve

    pause 0.75

    scene v11frmpe3a
    with dissolve

    pe "Thanks again."

    scene v11frmpe3b
    with dissolve

    u "Of course."

    scene v11frmpe3a
    with dissolve

    pe "Back to slaving away."

    scene v11frmpe3b
    with dissolve

    u "Haha, I'll catch up with you later."

    # -Back to free roam-
    call screen v11s23_helm

label v11s23_freeroamend:
    scene v11frm1 # FPP Show Nora sitting on black seating looking annoyed and not looking at anything in particular, arms crossed over her chest, mouth closed
    #with dissolve

    u "*Singing* She's a lonely lonely girl, in a lonely lonely world."

    scene v11frm1a # FPP Same angle as v11frm1, Nora looking at MC, looking annoyed with mouth open
    with dissolve

    no "What do you want? You trying to fill in for Charli?"

    scene v11frm1b # FPP Same angle as v11frm1, Nora looking at MC, looking annoyed with mouth closed
    with dissolve

    u "I want you to enjoy the trip you spent weeks planning."

    scene v11frm1a
    with dissolve

    no "*Sighs* How? By not getting attention from a workaholic boyfriend, being around a fake bitch named Chloe, or by walking around this boring ass museum?"

    scene v11frm1
    with dissolve

    u "I can tell this isn't how you thought the trip would go."

    scene v11frm1a
    with dissolve

    no "No it isn't. And shit, like... this is boring. I had way better things in mind to do and see in London."

    scene v11frm1b
    with dissolve

    u "Like what?"

    scene v11frm1a
    with dissolve

    no "A lot. I was headed to see the Big Ben but Mr. Lee made us come here."

    menu:
        "Agree":
            scene v11frm1b
            with dissolve
    
            u "Yeah it's pretty boring, but maybe it'll get better."

            scene v11frm1a
            with dissolve

            no "I thought so too, but I'm really starting to doubt it."

            scene v11frm2 # FPP Show Mr. Lee standing in center of Museum entrance hall, mouth open making an announcement
            with dissolve

            lee "Let's go students! Hope you enjoyed the museum, I know Riley did."

            scene v11frm3 # FPP Show Riley walking toward museum entrance, she has a big smile on her face and is chuckling through her teeth
            with dissolve

            ri "*Chuckles*"

            scene v11frm1a
            with dissolve

            no "At least someone enjoyed themselves. We literally wasted so much time here it's already starting to get dark."

            if v11_pen_goes_europe:
                scene v11frm4 # TPP Show all characters in scene getting on to shuttle bus
                with fade
            else:
                scene v11gtm8
                with fade

            pause 0.75

            scene v11bb12
            with fade
            
            pause 0.75

            # Transition to Scene 25
            jump v11_hotel_bar

        "Sneak out" (troublemaker=1.0):
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            scene v11frm1b
            with dissolve

            u "Let's go see it then."

            scene v11frm1a
            with dissolve

            no "We can't just leave."

            scene v11frm1b
            with dissolve

            u "Why not?"

            scene v11frm5 # FPP Show Nora standing up and smiling at MC, mouth closed
            with dissolve

            pause 0.75

            scene v11frm5a # FPP Same angle as v11frm5, Nora looking around the museum entrance hall
            with dissolve
        
            pause 0.75

            scene v11frm5b # FPP Same angle as v11frm5, Nora leaning close to MC, she's smiling with mouth open
            with dissolve

            no "You really wanna do this?"

            scene v11frm5a
            with dissolve

            u "Hey, this is our trip. If we aren't enjoying ourselves then why stay?"

            scene v11frm5b
            with dissolve

            no "*Chuckles* How are we gonna get out of here without getting caught?"

            scene v11frm5a
            with dissolve

            u "Like this."

            scene v11frm6 # TPP Show MC grabbing Nora's hand and pulling her toward the museum entrance
            with dissolve

            pause 0.75

            scene v11frm7 # FPP Outside of museum on sidewalk, sun has just set, looking at Nora who is smiling with mouth closed
            with dissolve

            u "Freedom!"

            scene v11frm8 # TPP Outside of museum on sidewalk, Nora giving MC a big hug, her body pressed against his
            with dissolve

            pause 0.75

            scene v11frm7
            with dissolve

            u "Oh..."

            scene v11frm7a # FPP Same angle as v11frm7, Nora smiling with mouth open
            with dissolve

            no "I can finally start enjoying this trip. Thank you, [name]."

            scene v11frm7
            with dissolve

            u "Glad I could help."
    stop music fadeout 3
    # -Transition to Scene 24-
    jump v11_big_ben