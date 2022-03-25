# SCENE 23: MC meets Amber at strip club
# Locations: Blue Lounge Strip Club Entrance (outside), Blue Lounge Strip Club Bar, Blue Lounge Strip Club Entrace catwalk, Blue Lounge Strip Club Entrace Provate Booth, Blue Lounge Strip Club Entrace (inside)
# Characters: MC (Outfit: 5), AMBER (Outfit: Stripper Outfit), DRUNK SLEAZE (Outfit: 1)
# Time: Tuesday night

label v16s23: # 23) Meet Amber at strip club
    # -MC arrives at the front entrance of The Blue Lounge to see Amber smoking a cigarette, wearing a flirty stripper outfit 
    # (very close to being nude but please remember there are what we call "incels" who will not appreciate their love interest being fully nude for others :))-

    scene v16s23_1 # TPP Show MC approaching Amber outside of the strip club. Amber is smoking a cigarette, not looking at MC. MC's mouth open, if visible, and he's waving at Amber [OUTSIDE ENTRANCE]
    with fade

    u "Hey, Amber."

    scene v16s23_2 # FPP Show Amber looking at MC, she looks excited or nervous, mouth open [OUTSIDE ENTRANCE]
    with dissolve

    am "[name]! Did you get my charger?"

    scene v16s23_2a # FPP Same angle as 2, MC holding a phone charger out to Amber. Amber is looking at the charger with a slight smile, mouth closed [OUTSIDE ENTRANCE]
    with dissolve

    u "Yeah, here it is."

    scene v16s23_2b # FPP Same angle as 2, Amber has taken the charger from MC. She looks relieved, with a slight smile, mouth open [OUTSIDE ENTRANCE]
    with dissolve

    am "You saved my fucking life."

    scene v16s23_3 # TPP Show Amber throwing away her cigarette, the phone charger in her other hand [OUTSIDE ENTRANCE]
    with dissolve

    pause 0.75

    scene v16s23_3a # TPP Same angle as 3. Show Amber giving MC a hug, the phone charger in her hand [OUTSIDE ENTRANCE]
    with dissolve

    pause 0.75

    if v16s20_take_twazzlers: # -if MC also took the Twazzlers # TODO:Variable
        scene v16s23_2c # FPP Same angle as 2, Amber with a slight smile, mouth closed, MC is holding Twazzlers package out to her [OUTSIDE ENTRANCE]
        with dissolve

        u "I grabbed these too. Thought you might appreciate it."

        scene v16s23_2d # FPP Same angle as 2, Amber taking the Twazzlers with a big smile, mouth open [OUTSIDE ENTRANCE]
        with dissolve

        am "Amazing! I haven't eaten all day!"

        scene v16s23_2e # FPP Same angle as 2, Amber eating one of the Twazzlers [OUTSIDE ENTRANCE]
        with dissolve

        pause 0.75

        scene v16s23_2f # FPP Same angle as 2, Amber looking into the now empty Twazzlers package. She looks angry or annoyed, mouth open [OUTSIDE ENTRANCE]
        with dissolve

        am "Only one?!"

        scene v16s23_2g # FPP Same angle as 2, Amber looking at MC and holding empty Twazzlers package, neutral expression, mouth closed [OUTSIDE ENTRANCE]
        with dissolve

        u "Aw, shit, really? Sorry, I just grabbed them off the table."

        scene v16s23_2h # FPP Same angle as 2, Amber looking at MC and holding empty Twazzlers package, neutral expression, mouth open [OUTSIDE ENTRANCE]
        with dissolve

        am "Ah, it'll be enough to keep me going."

        scene v16s23_3b # TPP Same angle as 3. Show Amber throwing the empty Twazzlers package on the ground [OUTSIDE ENTRANCE]
        with dissolve

        pause 0.75
    
    # -Regardless of Twazzlers-
    
    scene v16s23_2i # FPP Same angle as 2, Amber looking at MC with a neutral expression, mouth open [OUTSIDE ENTRANCE]
    with dissolve

    am "Let's go inside."

    scene v16s23_4 # TPP Show Amber walking into the strip club, with MC following close behind [OUTSIDE ENTRANCE]
    with dissolve

    pause 0.75

    scene v16s23_5 # FPP Show Amber barely visible behind the bar, she is bending over to plug in her phone. Her face is not visible, MC looking at her ass. [CHECKPOINT A]
    with dissolve

    am "I'm so glad you brought my charger. My phone has been dead for hours now."

    u "Ha, no worries."

    scene v16s23_6 # FPP MC's view as he looks around the inside of the strip club [standing at: CHECKPOINT A, Looking at: CHECKPOINT 1]
    with dissolve

    u "So, this is where the magic happens?"

    scene v16s23_7 # FPP View from another angle of the interior of the strip club [standing at: CHECKPOINT A, Looking at CHECKPOINT 2]
    with dissolve

    am "Yeah, what do you think?"

    scene v16s23_8 # FPP A stripper (random character) walks by wearing nothing but a thong. She is looking at MC side-eyed with a slight smile [ SEE MOZZART for DIAMOND chaacter]
    with dissolve

    u "I'm warming up to it, haha."

    scene v16s23_9 # FPP Amber back from behind the bar, looking at MC with a slight smile, mouth open [CHECKPOINT A]
    with dissolve

    am "*Giggles* Thought you might want to stick around for a bit. Let's sit down."

    scene v16s23_10 # TPP Show MC and Amber taking seats next to the catwalk. MC is looking at Amber, mouth open
    with dissolve

    u "So, are you enjoying it here?"

    scene v16s23_11 # FPP Show Amber in her seat next to the catwalk, looking at MC with a slight smile, mouth open [CHECKPOINT B, MC left seat, Amber right seat]
    with dissolve

    am "Honestly, yes. I mean-"

    scene v16s23_11a # FPP Same angle as 11, Amber looking up at the catwalk, slight smile, mouth open [CHECKPOINT B, MC left seat, Amber right seat]
    with dissolve

    am "The crowd isn't so great on weekdays, but on weekends..."

    scene v16s23_11b # FPP Same angle as 11, Amber leaning toward MC with a large, sneaky smile, mouth open [CHECKPOINT B, MC left seat, Amber right seat]
    with dissolve

    am "I make bank!"

    scene v16s23_11a
    with dissolve

    am "The louder the crowd, the higher the payout."

    scene v16s23_12 # TPP They are interrupted as a drunk guy sits on the other side of Amber (right side). It's the same guy who was the Male Buyer in v15 scene 10 (MC selling Lindsey's car). His mouth is open [CHECKPOINT B, MC left seat, Amber right seat, CHECKPOINT C, Sleazy Drunk, to the right of Amber]
    with dissolve

    ds "Hey sweetheart, aren't you gonna get up there and dance for me?"

    scene v16s23_12a# TPP Same angle as 12, The drunk guy's mouth is closed. MC looks very annoyed [CHECKPOINT B, MC left seat, Amber right seat, CHECKPOINT C, Sleazy Drunk, to the right of Amber]
    with dissolve

    u "(The fuck?)"

    menu:
        "We're talking":
            $ add_point(KCT.TROUBLEMAKER)
            
            scene v16s23_13 # FPP MC is looking up at the drunk guy, who sits on the other side of Amber (right side). The drunk guy is looking at Amber, Amber has a slight smile [CHECKPOINT B, MC left seat, Amber right seat, CHECKPOINT C, Sleazy Drunk, to the right of Amber]
            with dissolve

            u "Um, we're in the middle of a conversation, dude. Do you mind?"

            scene v16s23_13a # FPP Same angle as 13, Drunk guy is now looking at MC with an angry expression, mouth open [CHECKPOINT B, MC left seat, Amber right seat, CHECKPOINT C, Sleazy Drunk, to the right of Amber]
            with dissolve

            ds "Yeah, I mind, you little twerp."

            ds "She's wasting her time on you when she's supposed to be lookin' sexy up there for me."

            scene v16s23_13
            with dissolve

            u "Dude, what the-"

            scene v16s23_13b # FPP Same angle as 13, Drunk guy is looking back at Amber. If his face is visible, he is smiling with his mouth open [CHECKPOINT B, MC left seat, Amber right seat, CHECKPOINT C, Sleazy Drunk, to the right of Amber]
            with dissolve

            ds "Come on, angel... Let me see how good you are."

        "Stay quiet":
            scene v16s23_13
            with dissolve

            u "(*Sighs* Let's see how Amber handles this...)"

    # -Regardless-

    scene v16s23_13c # FPP Same angle as 13, Amber looking at the drunk guy, slight smile and mouth open [CHECKPOINT B, MC left seat, Amber right seat, CHECKPOINT C, Sleazy Drunk, to the right of Amber]
    with dissolve

    am "Sorry, honey. I'm with another client right now. I'll come find you later, okay?"

    scene v16s23_13d # FPP Same angle as 13. Drunk guy looking at Amber, but pointing at MC . His face has an annoyed expression, mouth open [CHECKPOINT B, MC left seat, Amber right seat, CHECKPOINT C, Sleazy Drunk, to the right of Amber]
    with dissolve

    ds "This kid? *Scoffs* I've got two-hundred dollars to spend tonight, ha!"

    scene v16s23_13b
    with dissolve

    ds "It can all be yours, baby."

    scene v16s23_13c
    with dissolve

    am "That sounds amazing, but it'll have to wait until later."

    scene v16s23_13e # FPP Same angle as 13. Amber is still looking at Drunk Guy with a slight smile, but she is holding her hand up, palm out, in front of her [CHECKPOINT B, MC left seat, Amber right seat, CHECKPOINT C, Sleazy Drunk, to the right of Amber]
    with dissolve

    am "But just so we're clear, all you're getting is a dance."

    scene v16s23_13b
    with dissolve

    ds "Haha... The future remains to be seen, sweetheart!"

    scene v16s23_13f # FPP Same angle as 13. Drunk guy leaning over to whisper in Amber's (listening, mouth closed) ear, smiling with mouth open [CHECKPOINT B, MC left seat, Amber right seat, CHECKPOINT C, Sleazy Drunk, to the right of Amber]
    with dissolve

    ds "*Whispers* You just haven't fallen for my charm yet."

    scene v16s23_13c
    with dissolve

    am "Hmm... Maybe."

    if v14_pics_with_linds: # TODO: VARIABLE # PLACEHOLDER VARIABLE # -if MC met Male Buyer in v15 scene10
        scene v16s23_13
        with dissolve

        u "Wait a minute... Didn't you buy Lindsey's car?"

        scene v16s23_13g # FPP Same angle as 13. Drunk guy turning to look at MC, he has a drunken smile, mouth open [CHECKPOINT B, MC left seat, Amber right seat, CHECKPOINT C, Sleazy Drunk, to the right of Amber]
        with dissolve

        ds "Huh? Oh... Yeah!"

        scene v16s23_13h # FPP Same angle as 13. Drunk guy now facing MC, he still has a drunken smile, mouth open [CHECKPOINT B, MC left seat, Amber right seat, CHECKPOINT C, Sleazy Drunk, to the right of Amber]
        with dissolve

        ds "Hey, man, thanks again. That car cleaned up real nice. Fucked my girlfriend in the back seat a few nights ago."

        ds "Not as bad as you'd think."

        scene v16s23_13i # FPP Same angle as 13. Drunk guy facing MC. Amber (disgusted expression, mouth open) is looking at Drunk guy [CHECKPOINT B, MC left seat, Amber right seat, CHECKPOINT C, Sleazy Drunk, to the right of Amber]
        with dissolve

        am "...Wow."

        scene v16s23_13j # FPP Same angle as 13. Drunk guy facing MC with a drunken smile, mouth closed [CHECKPOINT B, MC left seat, Amber right seat, CHECKPOINT C, Sleazy Drunk, to the right of Amber]
        with dissolve

        u "You have a girlfriend and you're begging for a strip dance?"

        scene v16s23_13h
        with dissolve

        ds "Hey, don't judge me, man. I've got oats to sow. You know?"

        scene v16s23_13j
        with dissolve

        u "Not at all, actually."

    scene v16s23_13b
    with dissolve

    ds "Come find me when you're finished with this loser."

    scene v16s23_12b # TPP Same angle as 12. The drunk guy is walking away, MC and Amber watch him go [CHECKPOINT B, MC left seat, Amber right seat]
    with dissolve

    pause 0.75

    scene v16s23_11c # FPP Same angle as 11. Amber looking at MC with a slight smile, mouth closed [CHECKPOINT B, MC left seat, Amber right seat]
    with dissolve

    u "You showed a lot of self-control there."

    scene v16s23_11
    with dissolve

    am "Haha, yeah, I know. Normally I'd have punched him in the throat, but..."

    scene v16s23_11a
    with dissolve

    am "Management frowns upon dancers beating up customers so I have to let it slide. *laughs*"

    scene v16s23_11c
    with dissolve

    u "I get it, but it must be hard sometimes."

    scene v16s23_11
    with dissolve

    am "Trust me, I'm used to it. Plus, it's part of the job."

    scene v16s23_11c
    with dissolve

    u "Yeah, guess you're right."

    scene v16s23_11a
    with dissolve

    am "Come on. Follow me."

    scene v16s23_14 # TPP Show Amber up from her seat, MC is getting up to follow her [CHECKPOINT B]
    with dissolve

    pause 0.75

    scene v16s23_15 # TPP Show Amber and MC entering private booth [CHECKPOINT C: MC in the middle seat, Amber to his right (Amber and the stripper pole are in frame)]
    with dissolve

    pause 0.75

    scene v16s23_16 # TPP Show MC and Amber sitting next to each other in the private booth, Amber looking at MC with a slight smile, mouth open [CHECKPOINT C] 
    with dissolve

    am "So, it went okay, getting into my place?"

    scene v16s23_17 # FPP View of Amber next to MC in the private booth. She is looking at MC with a slight smile, mouth closed [CHECKPOINT C]
    with dissolve

    u "Oh, yeah. Found the key, went inside. Easy enough."

    scene v16s23_17a # FPP Same angle as 17, Amber looking at MC with a slight smile, mouth open [CHECKPOINT C]
    with dissolve

    am "Good. People tell me not to keep a key under the mat, but it's saved me so many times, haha."

    if "bills" in freeroam16: # if MC looked at the Unpaid bills
        scene v16s23_17
        with dissolve

        u "(Should I bring up the stack of bills that I saw? Even though it's really none of my business...)"

        menu:
            "Ask about bills":
                $ v16s23_mention_bills = True
                $ add_point(KCT.TROUBLEMAKER)

                u "I did kind of notice that you had some unpaid bills. Is everything okay?"

                scene v16s23_17b # FPP Same angle as 17, Amber looking at MC with an angry expression, mouth open [CHECKPOINT C]
                with dissolve

                am "You were looking at my mail? My bills?"

                scene v16s23_17c # FPP Same angle as 17, Amber looking at MC with a slightly angry expression, mouth closed [CHECKPOINT C]
                with dissolve

                u "I just saw them when I was looking for the charger."

                scene v16s23_17d # FPP Same angle as 17, Amber looking at MC with a neutral expression, mouth open [CHECKPOINT C]
                with dissolve

                am "Okay... Well, for starters, don't read my mail ever again."

                scene v16s23_17e # FPP Same angle as 17, Amber looking at MC with a neutral expression, mouth closed [CHECKPOINT C]
                with dissolve

                u "(Noted.)"

                scene v16s23_17d
                with dissolve

                am "And lastly, mind your own business. If there's something going on I'll let you know."

                scene v16s23_17e
                with dissolve

                u "Right, yeah. I'm sorry."

            "Don't mention them":

                u "(Not a good idea. I don't think she'd be happy to know I peeked at those.)"

    # -Regardless-
    
    if "laptop" in freeroam16: # if MC looked at the Open laptop
        scene v16s23_17
        with dissolve

        u "(I kinda want to hear the story behind that erotic novel she's been reading... Should I mention it?)"

        menu:
            "Mention her laptop":
                $ v16s23_mention_laptop = True
                $ add_point(KCT.TROUBLEMAKER)

                u "So... Erotic fan fiction...?"

                scene v16s23_17f # FPP Same angle as 17, Amber looking at MC and laughing, mouth open [CHECKPOINT C]
                with dissolve

                am "Haha! Shit! You saw that, huh?"

                scene v16s23_17
                with dissolve

                u "*Laughs* Yeah... I mean to each their own, as they say."


                scene v16s23_17a
                with dissolve

                am "Honestly, it's fun to read that stuff! Lauren got me into it, haha."

                if lauren.relationship >= Relationship.GIRLFRIEND: # TODO: Variable # -if LaurenGF (extra dialogue)
                    scene v16s23_17
                    with dissolve

                    u "(Of course she did... Haha.)"

                    scene v16s23_17a
                    with dissolve

                    am "You should give it a go sometime, seriously. You might even pick up some ideas for your next hot date. *Chuckles*"

                    scene v16s23_17
                    with dissolve

                    u "Haha, okay. Thanks for the advice."


                    scene v16s23_17a
                    with dissolve

                    am "For sure. Oh, and [name]?"

                else:
                    scene v16s23_17a
                    with dissolve

                    am "Oh, and [name]?"

                scene v16s23_17
                with dissolve

                u "Yeah?"

                scene v16s23_17a
                with dissolve

                am "If I ever find out that you looked at my computer again, I'll end your life."

                scene v16s23_17
                with dissolve

                u "Ha. Okay. Understood. (*Gulps*)"

            "Keep it a secret":
                u "(If I don't keep that a secret, I'll leave here tonight with a few bruises... Maybe even worse.)"

    # -Regardless-
    
    if "photos" in freeroam16: # if MC looked at the Photos
        scene v16s23_17
        with dissolve

        u "(I wonder if she's willing to open up about those pictures I saw in her house...)"

        menu:
            "Ask about photos":
                u "Those photos on your wall..."

                scene v16s23_17a
                with dissolve

                am "What about them?"

                scene v16s23_17
                with dissolve

                u "Is it you playing the violin?"

                scene v16s23_17a
                with dissolve

                am "Haha, yeah..."

                # -stoned and druggy amber loses her happy, excitement for a moment as shes reminder of her childhood-
                scene v16s23_17g # FPP Same angle as 17, Amber is looking away, neutral expression, mouth open [CHECKPOINT C]
                with dissolve

                am "I used to love that thing. I think that photo was on the day that I won my first trophy."

                scene v16s23_17e
                with dissolve

                u "Oooh, I can't wait to hear you play one day."

                scene v16s23_17d
                with dissolve

                am "Oh, no. That violin is long gone, ha..."

                # -she snaps back into fun, druggy amber as if she's ignoring the pain-
                scene v16s23_17a
                with dissolve

                am "Besides, there's no way I would even remember how to play it."

                scene v16s23_17
                with dissolve

                u "Ah, that's a shame."

                scene v16s23_17a
                with dissolve

                am "I guess, haha."

                scene v16s23_17
                with dissolve

                u "And who's the kid in the other photo?"

                scene v16s23_17e
                with dissolve

                am "..."

                u "Sorry, should I not have mentioned it?"

                scene v16s23_17d
                with dissolve

                am "It's okay, it's just... A lot of people don't know the whole story."

                scene v16s23_17e
                with dissolve

                u "I get it. We don't have to talk about it if you-"

                # -If AmberRS, she opens up about her brother.
                # -if not AmberRS but MC passes a Amber KCT check (i believe it's currently confident), Amber also opens up about her brother
                if amber.relationship >= Relationship.FWB or (amber.relationship < Relationship.FWB and kct == "popular" ): # TODO: Variable # This is a guess based on the new relationship system. It would be nice if everyone was using the same language for relationship stuff
                    scene v16s23_17d
                    with dissolve

                    am "No, it's fine. I trust you."

                    scene v16s23_17a
                    with dissolve

                    am "That's my little brother, Damian."

                    scene v16s23_17
                    with dissolve

                    u "What? I had no idea."

                    scene v16s23_17a
                    with dissolve

                    am "*Laughs* I don't talk about him much because he's like... Really special to me, I guess?"

                    scene v16s23_17
                    with dissolve

                    u "Yeah?"

                    scene v16s23_17a
                    with dissolve

                    am "Yeah. He's the coolest, ha. I don't get to see him as often as I'd like to, but he's safe with my dad and our bitch of a stepmother."

                    scene v16s23_17e
                    with dissolve

                    u "*Scoffs* Not a fan?"

                    scene v16s23_17h # FPP Amber looking annoyed and rolling her eyes, mouth open [CHECKPOINT C]
                    with dissolve

                    am "*Exhales dramatically* You have no idea."

                    scene v16s23_17e
                    with dissolve

                    u "(Yikes.)"

                    u "Well, he looks like a good kid."

                    scene v16s23_17a
                    with dissolve

                    am "Yeah, he's something."

                elif (amber.relationship < Relationship.FWB and not kct == "popular" ): # -if not AmberRS, and MC does not pass an Amber KCT check, she doesn't up about her brother
                    scene v16s23_17d
                    with dissolve

                    am "Yeah, sorry. He's just really special to me."

                    scene v16s23_17e
                    with dissolve

                    u "Of course. I understand."

                    scene v16s23_17d
                    with dissolve

                    u "(Must be some rough history there...)"

            "Leave it alone":
                u "(Maybe another day.)"

    # -Regardless of all that-
    # -if AmberRS [Checkpoint 1.1]
    if amber.relationship >= Relationship.FWB:
        scene v16s23_18 # FPP Amber stepping up onto the small table in the private booth [CHECKPOINT C: on table]
        with dissolve

        u "Oh, are you going to show me some of your dancing skills?"

        scene v16s23_19 # FPP Amber now standing on the table, smiling down at MC, mouth open [CHECKPOINT C: on table]
        with dissolve

        am "Haha, angling for a freebie?"

        scene v16s23_19a # FPP Same angle as 19, Amber on the table smiling down at MC, mouth closed [CHECKPOINT C: on table]
        with dissolve

        u "Would that be against the rules?"

        scene v16s23_19
        with dissolve

        am "Hmm... I can give you a free sample, I guess."

        # -Amber starts dancing for MC, get creative with poses and camera angles, make it visually enjoyable for the players-
        scene v16s23_19b # FPP Same angle as 19, Amber beginning to dance sexy for MC, slight smile, mouth closed [CHECKPOINT C: on table]
        with dissolve

        u "Damn... You're pretty good at this, Amber!"

        scene v16s23_20 # FPP Show Amber removing her top while she dances for MC. He is smiling and Amber is smiling with her mouth open [CHECKPOINT C: on table]
        with dissolve

        am "I would hope so, haha."

        scene v16s23_19c # FPP Same angle as 19, Amber in a different pose dancing for MC, she is now topless [CHECKPOINT C: on table]
        with dissolve

        u "I'm starting to get flashbacks of Lauren's birthday party..."

        scene v16s23_21 # TPP Amber, now topless, dancing for MC. She is now on her hands and knees on the table, one finger pushing on MC's chest, her mouth open [CHECKPOINT C: on table]
        with dissolve

        am "Haha, why is it that every guy starts talking to me about sex when I dance for them?"

        scene v16s23_19d # FPP Same angle as 19, Amber dancing for MC, she is laying on the table on her back with her legs in the air
        with dissolve

        u "It can't be helped... You're sexually hypnotic."

        scene v16s23_22 # TPP Amber is now on the table on her knees with her back to MC, her hands up in her hair, mouth open [CHECKPOINT C: on table]
        with dissolve

        am "Sexually hypnotic, huh? Never heard that one before."

        scene v16s23_23 # FPP Amber is done dancing, getting down from the table [CHECKPOINT C: on table]
        with dissolve

        u "Aw, is it over already?"

        scene v16s23_24 # FPP Amber is standing in front of MC, putting her top back on, slight smile at MC with her mouth open [CHECKPOINT C]
        with dissolve

        am "Afraid so. I need to go find some actual paying customers."

        scene v16s23_25 # TPP Show MC standing up in front of Amber [CHECKPOINT C]
        with dissolve

        menu:
            "Be thankful":
                $ add_point(KCT.BOYFRIEND)

                scene v16s23_26 # FPP MC's view standing in front of Amber. Amber has a slight smile, mouth closed [CHECKPOINT C]
                with dissolve

                u "I appreciate the freebie. I really enjoyed watching you."

                scene v16s23_26a # FPP Same angle as 26, Amber with a slight smile, mouth open
                with dissolve

                am "You're most welcome. But next time you're going to pay me, haha."

            "Complain":
                $ add_point(KCT.TROUBLEMAKER)

                scene v16s23_26
                with dissolve

                u "Aww, come on. Can't you get back up there for another twenty minutes or so?"

                scene v16s23_26b # FPP Same angle as 26, Amber laughing at MC, playfully pushing him, her mouth open [CHECKPOINT C]
                with dissolve

                am "Haha, fuck off. You need to get that wallet out if you want any more out of me."

        # -Regardless-

        scene v16s23_26a
        with dissolve

        am "Come on. Out you go. I'm sure you can find some other girl to strip for you for free."

        scene v16s23_26
        with dissolve

        u "Haha, fingers crossed."

        scene v16s23_26a
        with dissolve

        am "Thanks again for bringing my charger."

        scene v16s23_26
        with dissolve

        u "No problem."

        scene v16s23_27 # TPP MC and Amber having a quick hug [CHECKPOINT C]
        with dissolve

        pause 0.75

        scene v16s23_28 # TPP MC leaving the private booth, Amber smiling and watching him go [CHECKPOINT C]
        with dissolve

        pause 0.75

    # [End of Checkpoint 1.1. Continue to Checkpoint 2]]

    else: # -if AmberFriend [Checkpoint 1.2]
        scene v16s23_18 
        with dissolve

        u "Am I getting a preview?"

        scene v16s23_19
        with dissolve

        am "Haha, no! Just testing my balance in these heels."

        scene v16s23_19e # FPP Same angle as 19, Amber standing on the table, testing her balance [CHECKPOINT C: on table]
        with dissolve

        pause 0.75

        scene v16s23_23a # FPP Same angle as 23. Amber getting down from the table, but her top is on. She has a slight smile, mouth open [CHECKPOINT C: on table]
        with dissolve

        am "Should be good."

        scene v16s23_23b # FPP Amber stepping off the small table toward her seat in the provate room [CHECKPOINT C]
        with dissolve

        pause 0.75

        scene v16s23_17
        with dissolve

        u "You know, seeing you like this tonight, I'm starting to get flashbacks to Lauren's party."

        scene v16s23_17a
        with dissolve

        am "Haha! I was just helping you out with that list, [name]. It was a one-time deal."

        scene v16s23_17i # FPP Amber looking at MC, smiling while raising one eyebrow, mouth open
        with dissolve

        am "No blowjobs happening in the private booth."

        scene v16s23_17
        with dissolve

        u "Ha, no, I didn't mean-"

        scene v16s23_17a
        with dissolve

        am "I know what you meant. Don't worry."

        am "But the guys here are always trying to pay me to blow them or fuck them."

        scene v16s23_17
        with dissolve

        u "Really? Doesn't that get annoying?"

        scene v16s23_17a
        with dissolve

        am "Of course, it gets annoying. But the money I go home with in my pocket is worth having to fake a smile during their bullshit."

        menu:
            "Support her":
                $ v16s23_support_amber = True
                $ add_point(KCT.BOYFRIEND)

                scene v16s23_17
                with dissolve

                u "As long as it's still what you want to do, you've got my support."

                scene v16s23_17a
                with dissolve

                am "Ha, thanks, [name]."

                scene v16s23_17
                with dissolve

                u "I know you can handle yourself."

                scene v16s23_17i
                with dissolve

                am "Yeah, I know a few different ways to punish a guy..."

            "Tell her to quit":
                scene v16s23_17
                with dissolve

                u "Amber, I know I supported you in the beginning of this, but you shouldn't have to deal with all these creeps just because you make a good amount of money."

                scene v16s23_17e
                with dissolve

                u "I don't think this is good for you."

                scene v16s23_17h
                with dissolve

                am "*Scoffs*"

                scene v16s23_17e
                with dissolve

                u "What if someone tries to hurt you? At least at Lew's you were safe and it was decent."

                scene v16s23_17d
                with dissolve

                am "I wouldn't say it was decent."

                scene v16s23_17e
                with dissolve

                u "But still, you didn't have to deal with guys trying to pay you to fuck them. Maybe you should try to get your job back."

                scene v16s23_17b
                with dissolve

                am "What? Why the hell would I do that?"

                scene v16s23_17d
                with dissolve

                am "I like it here, [name]. I get to be whoever I want to be. And I can be a different person every night if I wanted to."

                scene v16s23_17e
                with dissolve

                u "But Amber-"

                scene v16s23_17d
                with dissolve

                am "Don't try to convince me to quit, [name]. I'm not interested in hearing it."

                scene v16s23_17e
                with dissolve

                u "(Fuck, I should've known that'd piss her off. I'm just worried about her here... It's gross.)"

        # -Regardless-
        scene v16s23_29 # FPP Amber stands up in the private booth. Amber has a slight smile, mouth open [CHECKPOINT C]
        with dissolve

        am "Anyways, I should probably go back to work."

        scene v16s23_30 # FPP Amber, now standing, is looking at MC with a slight smile, mouth closed
        with dissolve

        u "Yeah, okay. I'll leave you to it."

        scene v16s23_30a # FPP Same angle as 30. Amber, now standing, is looking at MC with a slight smile, mouth open
        with dissolve

        am "Thanks again for bringing my charger."

        scene v16s23_30
        with dissolve

        u "Anytime, just call."

        # -if Support her: They have a quick hug. MC leaves. Amber watches him go, smiling
        # -if Tell her to quit: MC leaves. Amber watches him go, neutral expression
        if v16s23_support_amber:
            scene v16s23_27
            with dissolve

            pause 0.75

            scene v16s23_28
            with dissolve

            pause 0.75

        else:
            scene v16s23_28a # TPP Same angle as 28. MC is leaving the booth toward the entrance, Amber watching him go with a neutral expression.
            with dissolve

            pause 0.75

    # [End of Checkpoint 1.2. Continue to Checkpoint 2]
    # -Regardless-
    # [Checkpoint 2]

    scene v16s23_31 # TPP Show MC walking out of the strip club [CHECKPOINT D]
    with dissolve

    pause 0.75

    scene v16s23_32 # TPP MC is back outside the strip club, where Amber was smoking, and the drunk idiot from earlier is leaning against the wall with one hand and urinating, mouth open [OUTSIDE ENTRANCE]
    with dissolve

    ds "Ahhh... The seal has been broken!"

    scene v16s23_33 # FPP MC looking at the drunk guy, who is finishing up the process of urinating on the wall [OUTSIDE ENTRANCE]
    with dissolve

    u "(What a dickhead.)"

    menu:
        "Knock him out":
            $ add_point(KCT.TROUBLEMAKER)

            scene v16s23_34 # TPP Show MC walking toward the drunk guy, who is zipping his pants. MC looks angry and is yelling [OUTSIDE ENTRANCE]
            with dissolve

            u "Hey dickhead!"

            scene v16s23_35 # TPP Show MC sucker-punching the drunk guy right in the jaw [OUTSIDE ENTRANCE]
            with dissolve
            play sound "sounds/facepunch1.mp3" ### play sound
            pause 0.75

            scene v16s23_36 # FPP MC looking down at drunk guy, who is on the ground rubbing his jaw, mouth closed [OUTSIDE ENTRANCE]
            with dissolve

            u "Don't ever speak to a woman like you did in there again. You hear me?"

            scene v16s23_36a # FPP Same angle as 36, MC looking down at the drunk guy, who is on the ground rubbing his jaw, mouth open [OUTSIDE ENTRANCE]
            with dissolve

            ds "*Crying* W-wh-where's my mommy..."

            scene v16s23_37 # TPP MC walking away from the strip club, a self-satisfied smirk on his face, rubbing the knuckles of the hand he used to punch the drunk guy [OUTSIDE ENTRANCE]
            with dissolve

            pause 0.75

        "Give him a break":
            u "(The dude's already drunk out of his mind, I'll let him go this time. Can't promise that no one else won't kick his ass tonight, haha.)"

            scene v16s23_37a # TPP Same angle as 37. MC walking away from the strip club [OUTSIDE ENTRANCE]
            with dissolve

            pause 0.75

    # -regardless of choice-
    jump v16s24 # -Transition to Scene 24-