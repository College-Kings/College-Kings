# SCENE 46a: Lauren hypnotizes you
# Locations: Hallway to Lauren's room, Lauren's Room
# Characters: LAUREN (Outfit: 1), MC (Outfit: 1, Swim Trunks), Dream Girl (sexy bikini)
# Time: Evening

label v14s46a:
    play music "music/v12/Track Scene 29_8.mp3" fadein 2
    scene v14s46a_1 # TPP. MC knocking on Lauren's door.
    with dissolve

    pause 0.75

    scene v14s46a_1a # FPP. Lauren, excited, smiling, door open, mouth open.
    with dissolve

    la "Hi."

    scene v14s46a_1b # FPP. Same as v14s46a_1a, but Lauren's mouth closed.
    with dissolve

    u "Hello, Dr. Lauren. I'm here for my hypnosis appointment."

    scene v14s46a_1a
    with dissolve

    la "*Laughs* Come on in, silly."

    scene v14s46a_2 # TPP. Lauren leading MC into her bedroom, both smiling, mouths closed.
    with dissolve
    
    pause 0.75

    scene v14s46a_3 # TPP. MC and Lauren, both smiling, standing in Lauren's room, next to her bed.
    with dissolve

    pause 0.75

    scene v14s46a_4 # FPP. Lauren, excited, smiling, mouth open.
    with dissolve

    la "Go ahead and lie down on the bed."

    if lauren.relationship >= Relationship.GIRLFRIEND:
        scene v14s46a_4a # FPP. Same as v14s46a_3, but Lauren's mouth closed.
        with dissolve

        u "Damn, okay. I like where this is going already."

        scene v14s46a_4 
        with dissolve

        la "*Chuckles* Stop it. You have to focus."

    else: # -IF LaurenFriend
        scene v14s46a_4a
        with dissolve

        u "Okay sure, but I can't promise you that I'll be able to stay awake."

        scene v14s46a_4
        with dissolve

        la "We'll see about that..."

    scene v14s46a_4a
    with dissolve

    u "Haha, okay. So, we're just going straight into it? No chit-chat?"

    scene v14s46a_4
    with dissolve

    la "Oh, right. I'm sorry, [name]. I'm just super excited to try this, haha."

    scene v14s46a_4a
    with dissolve

    u "It's fine, I'm just teasing."

    if lauren.relationship >= Relationship.GIRLFRIEND:
        label v14s46a_sga:
            if _in_replay:
                $ lauren.relationship = Relationship.GIRLFRIEND
        
    else:
        label v14s46a_sgb:

    scene v14s46a_5 # TPP. MC lays on Lauren bed.
    with dissolve

    pause 0.75

    scene v14s46a_5a # TPP. Lauren sits in the chair next to her bed, close to MC's head.
    with dissolve

    pause 0.75
    
    scene v14s46a_6 # TPP. Camera at the foot of the bed capturing MC, laying down, eyes open, smiling, and Lauren (to MC's left), sitting in the chair next to him, smiling, mouth open.
    with dissolve

    la "Okay... Now close your eyes."

    scene v14s46a_6a # TPP. Same as v14s46a_6 except MC, eyes closed, relaxed smile.
    with dissolve

    la "*Softly* Let's start by getting nice and relaxed with some breathing exercises."

    scene v14s46a_7 # FPP. Lauren, smiling, mouth open.
    with dissolve

    la "Breathe in slowly for 5 seconds... *Inhales*"

    scene v14s46a_6b # TPP. Same as v14s46a_6a, but Lauren's mouth closed.
    with dissolve

    u "*Inhales*"

    scene v14s46a_7
    with dissolve

    la "*Softly* Hold it for 2 seconds..."

    scene v14s46a_6b
    with dissolve

    u "..."

    if v13_smoke_weed or v14s31b_smoke_weed_with_aubrey: # -If smoked weed in Amsterdam or at Apes house with Aubrey
        scene v14s46a_6c # TPP. Same as v14s46a_6b, but MC slightly sitting up, covering mouth with hand, coughing.
        with dissolve

        u "*Coughs* Fuck, haha. Sorry. *Inhales*"

        scene v14s46a_7
        with dissolve

        la "*Chuckles* Stoner much?"

        scene v14s46a_6d # TPP. Same as v14s46a_6b, but MC making a "shhh" gesture with his hand, laying down, eyes closed.
        with dissolve

        pause 0.75

    scene v14s46a_7
    with dissolve

    la "Now breathe out... *Exhales* All the way..."

    scene v14s46a_6b
    with dissolve

    u "*Exhales*"

    scene v14s46a_6a
    with dissolve

    la "*Softly* And again. Breathe in... breathe out... in... out..."

    scene v14s46a_6b
    with dissolve

    u "*Inhales* *Exhales*"

    scene v14s46a_7
    with dissolve

    la "*Softly* You are now falling into deep relaxation..."

    scene v14s46a_6a
    with dissolve

    la "*Softly* Falling deeper and deeper..."

    la "*Softly* As you listen to the sound of my voice..."

    scene v14s46a_7
    with dissolve

    la "*Softly* My voice is all you can hear as you sink deeper and deeper... into a peaceful... pleasant... relaxing state."

    scene v14s46a_6e # TPP. Same as v14s46a_6b, but MC laughing, eyes open, mouth open.
    with dissolve

    u "*Laughs*"

    scene v14s46a_7a # FPP. Lauren, slight smile, but serious expression, mouth open.
    with dissolve

    la "[name]! Come on... *Chuckles* Please take this seriously."

    scene v14s46a_6f # TPP. Same as v14s46a_6a, but MC eye's open, mouth open, smiling, looking at Lauren.
    with dissolve

    u "Haha... Okay... Okay. Sorry."

    u "I'll try again."

    stop music fadeout 3

    if lauren.relationship >= Relationship.GIRLFRIEND:
        play music "music/v14/Track Scene 46a_2.mp3" fadein 2
        #  replace with -LaurenGF plays some incredibly calming meditation music with an ocean gently lapping from her phone or radio.
     
    else: 
        play music "music/v14/Track Scene 46a_3.mp3" fadein 2
        # replace with -LaurenFriend plays some incredibly calming meditation music with birds singing in the background from her phone or radio.

    scene v14s46a_7
    with dissolve

    la "*Softly* You are starting to feel relaxed... You are feeling safe... And completely comfortable."

    scene v14s46a_8 # FPP. MC's perspective, head turned looking at Lauren, who is smiling, mouth open.
    with dissolve

    la "*Softly* As you drift off into a deep and pleasant state of relaxation, deeper and deeper..."
    la "*Softly* Listening and feeling the gentle caress of the natural elements around you."

    scene v14s46a_8a # FPP. Same as v14s46a_8, but Photoshop MC's vision closing his eyes 1/4 (simulate getting drowsy).
    with dissolve

    la "*Softly* The longer you listen to my voice, the deeper you sink into pure relaxation."

    scene v14s46a_8b # FPP. Same as v14s46a_8a, but Photoshop MC's vision closing his eyes 1/2.
    with dissolve

    u "(Oh, wow... Is this shit actually... working?)"

    scene v14s46a_8c # FPP. Same as v14s46a_8b, but Photoshop MC's vision closing his eyes 3/4
    with dissolve

    la "*Softly* Deeper and deeper..."

    la "*Whispers* More relaxed than you've ever felt before."

    scene v14s46a_8d # FPP. Black screen as if MC has his eyes completely closed.
    with dissolve

    u "(Zzzz...)"

    if lauren.relationship >= Relationship.GIRLFRIEND:
        scene v14s46a_7
        with dissolve

        la "*Softly* You are now walking along a beach. It's the most beautiful day. So sunny and warm, you can feel the light dancing on your skin."

        la "*Softly* The sand between your toes is soft to the touch and feels like a freshly dried blanket. You're calm... you're relaxed..."

        scene v14s46a_6a
        with dissolve

        la "*Softly* You've never felt this relaxed before... You're the happiest you've ever been."

        scene v14s46a_8d
        with dissolve

        u "(Zzzz...) *Heavy breathing*"

        show screen fantasyOverlay
        scene v14s46a_9 # TPP. MC, wearing swim trunks, walking along a sandy beach, smiling.
        with dissolve
        
        la "*Softly* There's a girl in a bikini, laying on a beach towel. Do you see her?"

        scene v14s46a_9a # TPP. Same as v14s46a_9, but MC looking left (as if searching for someone).
        with dissolve

        pause 0.75

        scene v14s46a_9b # TPP. Same as v14s46a_9, but MC looking right (as if searching for someone).
        with dissolve

        pause 0.75
        
        scene v14s46a_10 # FPP. DREAM GIRL, smiling, mouth closed ( [random girl] Long blonde hair, blue eyes, tan, smoking hot body, and sexy bikin) lays on a towel on her stomach in the beach sand with a bottle of sun tan lotion next to her.
        with dissolve
        
        u "Hm..."

        scene v14s46a_10a # FPP. Same as v14s46a_10, but Dream Girls motions MC to join her
        with dissolve

        la "She calls over to you and asks you to rub lotion on her skin. You can help her."

        # -MC walks to the girl as we get a slow-mo view of her, she's laying on her stomach, straps of her top are untied if possible, bottle of sunscreen next to her-
        
        scene v14s46a_11 # TPP. MC, back to camera, walking towards Dream Girl, who is laying on her stomach on a towel on the beach with sun tan lotion.
        with dissolve

        pause 1.5

        scene v14s46a_12 # FPP. MC looking down at Dream Girl, laying on her stomach, sun tan lotion by her head, hair pulled to the side, tan body, bikini top untied showing a generous view of side boob.
        with dissolve

        pause 1.5

        scene v14s46a_13 # TPP. MC smiling, sitting behind dream girl, rubbing lotion on her back. Dream Girl, smiling, eyes closed.
        with dissolve

        la "*Softly* As you rub the lotion into her back, she removes her bikini top and turns around to face you."
        la "*Softly* She's now asking you to massage the lotion into her breasts."

        if config_censored:
            call screen censoredPopup("v14s46_nsfwSkipLabel1")

        scene v14s46a_14 # FPP. MC looking down at Dream Girl, eyes open, smiling sexy, laying on her back, breasts fully exposed, holding the bottle of lotion towards her breasts.
        with dissolve

        u "(Zzzz...) Hmm..."

        scene v14s46a_15 # FPP. MC looking down at Dream Girl, eyes closed, smiling sexy, hands to her side while MC's hands cup her breasts as if he's rubbing lotion on them (keep the nipples visible).
        with dissolve

        la "*Softly* Rubbing into her soft skin you can feel her nipples, getting excited by your touch."

        scene v14s46a_16 # FPP. Close up on Dream Girl's nipple(s) showing the nipples slightly raised.
        with dissolve

        pause 0.75

        scene v14s46a_16a # FPP. Same as v14s46a_16, but nipples raised more than previous. 
        with dissolve

        pause 0.75

        scene v14s46a_16b # FPP. Same as v14s46a_16a, but nipples are fully erect and hard.
        with dissolve

        pause 0.75

        scene v14s46a_17 # FPP. Close up of Dream Girl's hand feeling MC's dick that is bulging in his swim trunks. 
        with dissolve

        la "*Softly* She feels your... pulsing cock. *Embarrassed giggle* It's hard. Your swim trunks feel like they're about to burst at the seams..."

        scene v14s46a_17a # FPP. Same as v14s46a_17, but slightly different hand position (as if Dream girl is rubbing MC's cock). 
        with dissolve

        u "(Zzzz...) *Moans*"

        scene v14s46a_18 # TPP. MC's legs spread out (like "V")(trunks off) with Dream Girl between his legs, laying on her stomach, eyes looking up at MC, with the tip of her mouth on the head MC's fully erect cock.
        with dissolve

        pause 0.75

        scene v14s46a_18a # TPP. Same as v14s46a_18, but Dream Girl's mouth 1/2 of the way down on MC's erect cock, her eyes closed.
        with dissolve

        pause 0.75

        scene v14s46a_18b # TPP. Same as v14s46a_18a, but Dream Girl's mouth all the way down on MC's erect cock.
        with dissolve

        la "*Softly* She slowly pulls them down and immediately takes your full, throbbing member in her mouth."
        la "*Softly* She starts to suck on it, her soft lips hugging every inch of you. Sucking and sucking and sucking until–"

        scene v14s46a_18c # FPP. Same as v14s46a_18b, but different camera angle (from MC's perspective looking down at her sucking his cock.)
        with vpunch

        u "*Moans* Fuck..."

        label v14s46_nsfwSkipLabel1:

        la "*Laughs* Oh my God. I'm so sorry, I didn't think you'd-"

        hide screen fantasyOverlay

        stop music fadeout 3

        play music "music/v12/Track Scene 18_3.mp3" fadein 2
        scene v14s46a_6g # TPP. Same as v14s46a_6, but MC, mouth open, shocked, sitting up in bed (legs remain out), looking down at the large wet spot in the crotch of his pants, Lauren sitting next to him, look at his wet spt, laughing, mouth closed.
        with dissolve

        u "What the... fuck?!"

        scene v14s46a_6h # TPP. Same as v14s46a_6g, but MC mouth closed, looking at Lauren, Lauren looking at MC, smiling, mouth open.
        with dissolve

        $ grant_achievement("your_eyelids_are_heavy")

        la "I'm so sorry! *Laughs* It was fun though, right? Did it feel real?"

        scene v14s46a_6i # TPP. Same as v14s46a_6h, but MC mouth open and Lauren mouth closed.
        with dissolve

        u "I have cum all over myself, Lauren. It felt pretty fucking real! How am I supposed to walk home like this?!"

        scene v14s46a_7
        with dissolve

        la "That's so crazy... You can just go in the bathroom and clean yourself up, ha."

        scene v14s46a_6i
        with dissolve

        u "So funny."

        scene v14s46a_6h
        with dissolve

        la "I said sorry!"

        scene v14s46a_19 # TPP. MC, frustrated, mouth closed, getting up from the bed with a large wet spot in his crotch, Lauren sitting next to the bed, smiling, mouth open.
        with dissolve

        la "But the hypnosis worked really well then, don't you think?"

        scene v14s46a_20 # TPP. Camera stays in Lauren's room, pointing at the door to her bathroom with MC entering the bathroom.
        with dissolve

        pause 0.75

        # play sound of running water 

        scene v14s46a_20a # TPP. Sames as v14s46a_20, but with the door slightly open (MC inside the bathroom off camera).
        with dissolve
        
        u "If that's what you wanted to happen, then sure. It went great."

        scene v14s46a_7
        with dissolve

        la "You can dry off with my beach towel in there."

        scene v14s46a_20a
        with dissolve

        u "Ah, a beach towel. Good one."

        # -The running water stops

        scene v14s46a_20b # TPP. Same as v14s46a_20, but with MC, smiling, exiting the bathroom into Lauren's room, the stain on his pants is gone
        with dissolve

        pause 0.75

        scene v14s46a_21 # TPP. MC, standing, smiling, mouth closed, facing Lauren (right) and Lauren, standing, smiling, mouth closed, facing MC (left).
        with dissolve

        pause 0.75

        scene v14s46a_22 # FPP. Lauren, smiling, mouth open.
        with dissolve
        
        la "I didn't know what was going to happen, [name]. I was just exploring."

        scene v14s46a_22a # FPP. Same as v14s46a_22, but Lauren's mouth closed.
        with dissolve

        u "You were exploring and I was exploding..."

        scene v14s46a_22
        with dissolve

        la "*Laughs*"
        $ renpy.end_replay()

        scene v14s46a_22a
        with dissolve

        u "*Laughs* That was such a weird experience. Where did you learn this?"

        scene v14s46a_22
        with dissolve

        la "I guess I've just been watching a little too much porn lately... I can't stop thinking about sex."

        scene v14s46a_22a
        with dissolve

        u "Haha, wow..."

        scene v14s46a_22
        with dissolve

        la "You still love me, right?"

        menu: # -MC chooses Event1 or Event2
            "Of course I do": # -Event1 Of course I do
                scene v14s46a_22a
                with dissolve

                u "Of course I do."

            "Even more":
                $ v14s46a_love_lauren_more = True
                $ add_point(KCT.BOYFRIEND)
                
                scene v14s46a_22a
                with dissolve

                u "Even more than I did before."

                scene v14s46a_22b # FPP. Same as v14s46a_22, but Lauren's eyes are open wider, she wears a subtle sexy smile, mouth open.
                with dissolve

                la "Really?"

                scene v14s46a_22a
                with dissolve

                u "I mean, I kinda feel like your guinea pig all the time..."

                scene v14s46a_22
                with dissolve

                la "*Laughs* My poor guinea pig."

                scene v14s46a_22a
                with dissolve

                u "But experimenting like this and seeing how excited you are, it reminds me of how much I like you."

        # -They both smile at each other-
        scene v14s46a_21
        with dissolve

        pause 0.75

        scene v14s46a_22
        with dissolve

        la "Aww."

        if not v14s46a_love_lauren_more:
            play sound "sounds/kiss.mp3"
            
            scene v14s46a_23 # TPP. MC and Lauren kiss each other on the lips.
            with dissolve

            pause 1

        else:
            play sound "sounds/kiss.mp3"
        
            scene v14s46a_23a # TPP. MC and Lauren kiss each each other passionately.
            with dissolve

            pause 1.75

            scene v14s46a_22
            with dissolve

            la "I'm glad."

    else: # -If LaurenFriend or else
        scene v14s46a_7
        with dissolve

        la "*Softly* You are now walking through a fresh, grassy field in your bare feet."
        la "*Softly* It's the most beautiful day. So sunny and warm, you can feel the light dancing on your skin."

        la "*Softly* The grass between your toes is gentle to the touch. You're calm... you're relaxed... you're the happiest you've ever been..."

        scene v14s46a_8d
        with dissolve

        u "*Zzzz...* *Heavy breathing*"

        show screen fantasyOverlay
        scene v14s46a_24 # TPP. MC, smiling, mouth closed, walking BAREFOOT (normal clothes) through a green grassy field, with a bright sunny sky above him.
        with dissolve

        pause 1.25

        scene v14s46a_25 # FPP. MC looking out in the distance of the green grassy field, watching a horse trotting towards him.
        with dissolve
                
        la "*Softly* You see a majestic horse trotting towards you. The closer it gets, the more calm you feel."

        scene v14s46a_26 # FPP. Close up of MC hand, holding a red apple.
        with dissolve

        la "*Softly* You notice you have an apple in your hand."

        scene v14s46a_25a # FPP. MC looking at the horse standing in front of him, the horse is looking at the apple in MC's hand. 
        with dissolve

        pause 1.25

        scene v14s46a_27 # TPP. MC, smiling, relaxed mouth closed standing in the green grassy field, using his right hand to feed an apple to the horse.
        with dissolve
        
        la "*Softly* You feed it to the horse."

        scene v14s46a_8d
        with dissolve

        u "*Zzzz...* Hm..."

        scene v14s46a_27a # TPP. MC smiling, relaxed mouth closed standing in the green grassy field, with the bottom of MC's shirt stuck in the horse's mouth (or something to suggest the horse is eating his shirt) similar to v14s46a_27
        with dissolve

        la "*Softly* The horse has finished the apple, but he's still hungry... He starts to eat your shirt."

        scene v14s46a_27b # TPP. Similar to v14s46a_27a with the horse still eating the shirt, but now half of MC's shirt is gone. 
        with dissolve

        pause 0.75

        scene v14s46a_27c # TPP. Simliar to v14s46a_27b but MC TOPLESS (NO SHIRT) and the horse still stands in front of MC.
        with dissolve
        
        la "*Softly* You can't stop him! In an instant, he's eaten your whole shirt..."

        scene v14s46a_28 # TPP. MC with a slight frown, concerns, standing in the green grassy field TOPLESS (NO SHIRT).
        with dissolve

        la "*Softly* But he's not stopping there... He's hungry for something else now. Before you know it, he's chewing at your dick."

        scene v14s46a_29 # TPP. MC mouth open, shocked awake, standing in the grassy field with his hands out trying to prevent the horse from nudging his critch with its nose.
        with dissolve

        pause 0.75

        scene v14s46a_30 # TPP. MC, expression: having a bad dream, hands out protecting his crotch, eyes closed laying in Lauren's bed in Lauren's room.
        with dissolve
        
        u "*Zzzz...* *Grunts*"

        scene v14s46a_31 # TPP. Green Grassy Field: Close up of the horse frowning (angry) and nipping at MC's crotch area.
        with dissolve

        la "*Softly* He's starting to get angry. You can feel his teeth trying to bite their way through the fabric of your jeans... but you can't move."

        scene v14s46a_32 # TPP. MC shocked, standing in the green grassy field, naked with his hands covering his crotch 
        with dissolve

        la "*Softly* Your feet are glued to the ground as you try to push the horse away, but somehow he manages to rip off your pants."

        scene v14s46a_33 # TPP. CLOSEUP: Horse's mouth nipping towards MC's (naked) hands that are covering his crotch.
        with dissolve

        la "*Softly* The horse has his eyes on the prize now... Before you know it, he takes one quick bite towards your dick and-"

        scene v14s46a_34 # TPP. SHOT OF MC waste up: MC, mouth open, SCREAMING IN PAIN, hands down towards his crotch.
        with dissolve

        u "Aahhh! Fuck! Oww! M-My balls!"

        hide screen fantasyOverlay

        stop music fadeout 3

        play music "music/v12/Track Scene 18_3.mp3" fadein 2

        scene v14s46a_35 # TPP. MC, in Lauren's bed, shocked (liked he snapped out of a bad dream),sitting up but legs extended out on the bed, slightly angry, mouth open.
        with dissolve

        pause 0.75

        scene v14s46a_36 # FPP. MC looking at the foot of the bed seeing Lauren with a big smile, holding the straw side of the broom with the broom handle against MC's balls.
        with dissolve

        pause 1.25

        scene v14s46a_35
        with dissolve

        u "What the fuck?!"

        scene v14s46a_37 # FPP. Lauren, smiling, mouth open holding the staw end of a broom.
        with dissolve

        la "*Laughs* I'm sorry, [name]! It was too good of an opportunity! I didn't think the horse dream would actually work on anyone... *Chuckles*"

        scene v14s46a_37a # FPP. Sames as v14s46a_37, but mouth closed.
        with dissolve

        u "What? Why did you do that?"

        scene v14s46a_37
        with dissolve

        la "All in the name of science, I promise. You should be very proud of yourself. It worked perfectly."

        scene v14s46a_37a
        with dissolve

        u "You're some kind of mad scientist, aren't you?"

        scene v14s46a_37
        with dissolve

        la "*Chuckles* I watched a few videos, and I wanted to see if it worked."

        scene v14s46a_37a
        with dissolve

        u "*Laughs* That was such a weird experience... My balls... They actually hurt a little."

        scene v14s46a_37
        with dissolve

        la "Haha! Perfect."
        
    $ renpy.end_replay()

    scene v14s46a_38 # FPP. Lauren, smiling, mouth open, in her room.
    with dissolve

    la "Now, I've gotta get caught up on homework, so."

    scene v14s46a_38a # FPP. Same as v14s46a_38, but mouth closed.
    with dissolve

    u "Kicking me out?"

    scene v14s46a_38
    with dissolve

    la "Yeah..."

    scene v14s46a_39 # TPP. Lauren, smiling, walks MC, smiling, both mouths closed, to the her dormroom door.
    with dissolve

    pause 0.75

    scene v14s46a_40 # TPP. Lauren, smiling opens the door for MC, smiling
    with dissolve

    pause 0.75

    scene v14s46a_41 # TPP. Camera behind Lauren standing at her room door, facing MC (smiling, mouth closed,) standing in the hallway facing Lauren.
    with dissolve

    pause 0.75

    scene v14s46a_1a
    with dissolve

    la "Thanks for doing that with me."

    scene v14s46a_1b
    with dissolve

    u "You're welcome, I guess."

    scene v14s46a_1a
    with dissolve

    la "Haha... We'll do something again soon?"

    scene v14s46a_1b
    with dissolve

    u "Yeah sure, but if it's another hypnosis session... Maybe I'll send Imre instead."

    scene v14s46a_1a
    with dissolve

    la "*Chuckles* Please don't do that to me."

    scene v14s46a_1b
    with dissolve

    u "Haha, see ya."

    scene v14s46a_1a
    with dissolve

    la "Bye, [name]."

    play sound "sounds/doorclose.mp3"

    scene v14s46a_42 # TPP. MC standing in front of Lauren's closed door.
    with dissolve

    u "(Hmm, well that was interesting...)"

    stop music fadeout 3


    if joinwolves: # -If Wolves, transition to scene 52
        jump v14s52
    
    else: # -If Apes, transition to scene 53
        jump v14s53