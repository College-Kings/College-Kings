# SCENE 43c: Working with Penelope
# Locations: Stairwell Use the background from v14s43b_16
# Characters: PENELOPE (Outfit: 1), MC (Outfit: 1)
# Time: Morning
# 12 Unique Renders, 53 Total Renders

label v14s43c:
    scene v14s43c_1 # FPP. MC looking at Penelope, Penelope looking at MC, Penelope slight smile, mouth open
    with dissolve

    pe "Honestly, I don't even need to read the pages. *Chuckles*"

    play music "music/v13/Track Scene 8.mp3" fadein 2

    scene v14s43c_1a # FPP. Penelope mouth closed
    with dissolve

    u "Ha, what? How?"

    scene v14s43c_1
    with dissolve

    pe "I already knew we were doing this because of the syllabus, so I prepared the skit already."

    scene v14s43c_1a
    with dissolve

    u "Damn, just like that?"

    scene v14s43c_1
    with dissolve

    pe "Just like that. *Laughs* Did you have any ideas for it, though?"

    scene v14s43c_1a
    with dissolve

    menu:
        "Romantic scene":
            $ v14_PenRomScene = True
            $ add_point(KCT.BOYFRIEND)
            $ add_point(KCT.BRO)

            scene v14s43c_1b # FPP. same as v14s43c_1a Penelope tilts her head to the side
            with dissolve

            u "I was hoping we could do something romantic? A little king and queen romance that ends with a sweet kiss."

            scene v14s43c_1c # FPP. same as v14s43c_1 penelope runs her hand through her hair and blushes, mouth open, full smile, looking at mc seductively
            with dissolve

            pe "Ooh, that sounds fun, yeah!"

            scene v14s43c_1b
            with dissolve

            u "See? I'm a genius."

            scene v14s43c_1
            with dissolve

            pe "*Chuckles* Right..."

            if penelope.relationship.value >= Relationship.LOYAL.value:
                scene v14s43c_1c
                with dissolve

                pe "Did I hear you say you want to end it with a kiss? *Chuckles*"

                scene v14s43c_1b
                with dissolve

                u "Haha. That's exactly what you heard."

                scene v14s43c_1
                with dissolve

                pe "You sure you're not just trying to steal a kiss in the middle of class?"

                scene v14s43c_1a
                with dissolve

                u "I can do that without a skit."

                scene v14s43c_2 # TPP. MC and Penelope still sitting on the stairs, MC leans in and kisses Penelope, one hand behind her head pulling her closer, Penelope has one hand up and touching Mc's chest and one on his leg
                with dissolve
                
                pause 0.75

                scene v14s43c_1c
                with dissolve

                pe "*Chuckles* Okay... Wow."

            scene v14s43c_1
            with dissolve

            pe "It's settled then, romantic scene it is."

        "Argument scene":
            $ add_point(KCT.TROUBLEMAKER)
            $ add_point(KCT.BRO)

            scene v14s43c_1a
            with dissolve

            u "I'm thinking of something combative, like maybe an argument scene?"

            scene v14s43c_1d # same as v14s43c_1 Penelope holds up both her fists in a boxers pose, slight smile, mouth open trying to act cute
            with dissolve

            pe "So, you wanna fight me?"

            scene v14s43c_1b
            with dissolve

            u "Not really, but I think people would enjoy it and it'd be fun to act out."

            scene v14s43c_1
            with dissolve

            pe "Hmm, okay... Let's roll with it, I guess."

    scene v14s43c_3 # TPP. show mc and penelope standing up facing each other, slight smiles, mouths closed, looking at each other
    with dissolve

    pause 0.75

    scene v14s43c_4 # FPP. Mc and Penelope are now standing up, show Penelope looking at MC, slight smile, mouth open
    with dissolve

    pe "So, let's try and base it off of some actual history, since it's a history class."

    scene v14s43c_4a # FPP. same as v14s43c_4 Penelope mouth closed
    with dissolve

    u "*Laughs* Okay, fair. What are you thinking?"

    scene v14s43c_4
    with dissolve

    pe "We'll be the king and queen of England and we'll do the scene that you said."

    scene v14s43c_4a
    with dissolve

    u "Okay, I don't know much about medieval times and being a King, but I'll play along. *Chuckles*"

    scene v14s43c_4b # FPP. same as v14s43c_4 Penelope increases to full smile, mouth open
    with dissolve

    pe "Haha, perfect."

    scene v14s43c_4
    with dissolve

    pe "Alright, let's improv for a bit and see where it takes us."

    scene v14s43c_4a
    with dissolve

    u "Okay, umm... You begin?"

    scene v14s43c_4
    with dissolve

    pe "*British accent* Good morning, love! How was the hunt?"

    scene v14s43c_4a
    with dissolve

    u "*British accent* The hunt went well, m'lady. A few targets got away but we made quite the haul nonetheless."

    scene v14s43c_4c # FPP. same as v14s43c_4 Penelope has a serious expression and holds a fist in the air, mouth open
    with dissolve

    pe "*British accent* I didn't mean the hunt for food, I meant the hunt for traitors."
    pe "*British accent* We need to find those who wish to destroy our society and remove them as a threat."

    scene v14s43c_4d # FPP. same as v14s43c_4c Penelope has lowered her fist, mouth closed
    with dissolve

    u "*British accent* You wish that I murder them?!"

    scene v14s43c_4a
    with dissolve

    u "That's harsh."

    scene v14s43c_4e # FPP. same as v14s43c_4d Penelope leans in closer to MC, mouth open
    with dissolve

    pe "*Whispers* Are you saying that as part of the script or as an actual question?"

    scene v14s43c_4d
    with dissolve

    u "Why are you whispering? *Laughs* But yes, it was an actual question."

    scene v14s43c_4e
    with dissolve

    pe "*Whispers* Oh okay, I'll change it. Ahem..."

    scene v14s43c_4c
    with dissolve

    pe "*British accent* We have to banish the traitors from our walls. Either they are with us or they are moved far, far away from us."

    scene v14s43c_4d
    with dissolve

    u "*British accent* I will see to it that that's done."

    scene v14s43c_4
    with dissolve

    pe "*British accent* Very well. Now, shall we enjoy some dinner for this evening before we deliver our plans to the troops?"

    scene v14s43c_4a
    with dissolve

    u "*British accent* Aye, let's get on with it."

    scene v14s43c_5 # TPP. Show MC and Penelope sitting back down on the stairs across from each other, facing each other
    with dissolve

    pause 0.75

    scene v14s43c_1e # FPP. same as v14s43c_1 Penelope raises an eyebrow
    with dissolve

    pe "*British accent* The meal they're serving tonight is supposed to be one to die for."

    scene v14s43c_1a
    with dissolve

    u "*British accent* Ah. *Nervous chuckle* Well, hopefully not literally."

    scene v14s43c_1e
    with dissolve

    pe "*British accent* Guess we'll find out, hm?"

    scene v14s43c_5a # TPP. same as v14s43c_5 MC looks up and away from Penelope mouth open with an arm extended out palm up and open towards where he is looking, Penelope looks where MC's hand is extending towards
    with dissolve

    u "*British accent* And here comes the food now."

    scene v14s43c_5b # TPP. same as v14s43c_5 MC and Penelope are fake eating, mouths open
    with dissolve

    pause 0.75

    scene v14s43c_5c # TPP. same as v14s43c_5b Penelope wipes pretend food away from Mc's mouth, Mc laughs mouth open
    with dissolve

    pause 0.75

    scene v14s43c_1
    with dissolve

    pe "*British accent* So, how was your meal?"

    scene v14s43c_1a
    with dissolve

    u "*British accent* Terrific."

    scene v14s43c_1f # FPP. same as v14s43c_1 Penelope increase to full smile, mouth open
    with dissolve

    pe "*British accent* I hope so."

    scene v14s43c_1g # FPP. same as v14s43c_1f Penelope leans in, has an evil look, mouth open, and one hand carressing mcs face 
    with dissolve

    pe "*British accent* Because it's the last meal you'll ever have with me."

    scene v14s43c_1a
    with dissolve

    u "*British accent* E-Excuse me?"

    scene v14s43c_1h # FPP. same as v14s43c_1b Penelope has a disgusted expression, mouth open
    with dissolve

    pe "*British accent* You heard me clear. I've been made aware of your outings with Lady Brittle, you slag."

    scene v14s43c_1i # FPP. same as v14s43c_1h Penelope mouth closed
    with dissolve

    u "*British accent* What?! But... I've done nothing of the sort!"

    scene v14s43c_1i
    with dissolve

    u "*British accent* I've been preparing for a potential war for weeks now... I don't even know the woman you speak of."

    scene v14s43c_1h
    with dissolve

    pe "*British accent* So, you continue to lie? *Scoffs*"

    scene v14s43c_1i
    with dissolve

    u "*British accent* I haven't lied!"

    if penelope.relationship.value >= Relationship.LOYAL.value and (chloe.relationship.value >= Relationship.GIRLFRIEND.value or lauren.relationship.value >= Relationship.GIRLFRIEND.value):
        scene v14s43c_1j #FPP. same as v14s43c_1b Penelope has a slightly confused expression, mouth closed
        with dissolve

        u "(Have I? Wait...)"

        scene v14s43c_1k # FPP. same as v14s43c_1j Penelope mouth open
        with dissolve

        pe "*Whispers* [name]...?"

    scene v14s43c_1a
    with dissolve

    u "*Whispers* Wait... Is this a romance or an argument scene?"

    scene v14s43c_1a
    with dissolve

    pe "*Whispers* Just play along! Ahem..."

    if v14_PenRomScene:
        scene v14s43c_1l # FPP. same as v14s43c_1 Penelope has a smug expression, mouth open
        with dissolve

        pe "*British accent* Prove it, then."

        scene v14s43c_1m # FPP. same as v14s43c_1l Penelope mouth closed
        with dissolve

        u "*British accent* Alright. Ask me something I'd only know if I was where I said I was that night."

        scene v14s43c_1l
        with dissolve

        pe "*British accent* Very well, then... On the night before last, at what time did General Pines leave to go to his quarters?"

        scene v14s43c_1m
        with dissolve

        u "*British accent* He went to his quarters at an hour 'til midnight. His wife was ill and I requested that we adjourn for his sake."

        scene v14s43c_1n # FPP. same as v14s43c_1 Penelope looks shocked/worried, both hands slightly covering her mouth, her mouth is open
        with dissolve

        pe "..."

        scene v14s43c_1n
        with dissolve

        u "*British accent* Well?"

        scene v14s43c_1o # FPP. same as v14s43c_1n has lowered her hands, mouth still open
        with dissolve

        pe "*British accent* That... That's exactly what the general's wife said..."

        scene v14s43c_1p # FPP. same as v14s43c_1o Penelopes mouth is closed
        with dissolve

        u "*British accent* And you dare accuse the king... Your accusation was out of line, you know where my loyalty lies."

        scene v14s43c_1o
        with dissolve

        pe "*British accent* My accusation was misplaced, yes, but sadly... It wasn't the worst thing I've done tonight."

        scene v14s43c_1p
        with dissolve

        u "*British accent* Explain yourself!"

        scene v14s43c_1q # FPP. same as v14s43c_1o Penelope begins tearing up, mouth open
        with dissolve

        pe "*British accent* My love, I'm so sorry... *Sniffles*"

        scene v14s43c_1r # FPP. same as v14s43c_1q Penelope's mouth is closed
        with dissolve

        u "*British accent* What have you done?! Tell me!"

        scene v14s43c_5d # TPP. same as v14s43c_5c Penelope goes over and caresses MC's face, Penelope has slight tears in her eyes sad expression mouth closed, Mc has a concerned expression, mouth closed
        with dissolve

        pause 0.75

        scene v14s43c_5e # TPP. same as v14s43c_5d Penelope kisses MC romantically, french kiss, Penelope has one hand behind mc's head and one on his cheek, Penelope's eyes are closed, Mc slightly shocked eyes open
        with dissolve
        
        pause 1.75

        scene v14s43c_1s # FPP. same as v14s43c_1c Penelope has slight tears in her eyes, mouth closed
        with dissolve

        u "(Oh, shit...)"

        scene v14s43c_1q
        with dissolve

        pe "*British accent* For my sins, I will join you."

        scene v14s43c_5f # TPP. same as v14s43c_5b looks down at his pretend food shocked expression mouth open, Penelope grabs pretend food from his plate slight tears in her eyes mouth closed sad expression
        with dissolve

        pause 0.75

        scene v14s43c_1t # FPP. same as v14s43c_1q Penelope pretends to eat food
        with dissolve

        u "*British accent* Wait... You... You poisoned me?!"

        scene v14s43c_1q
        with dissolve

        pe "*British accent* And now I have poisoned us both, my darling."

        scene v14s43c_1r
        with dissolve

        u "*British accent* Your mind is unsound, my Queen."

        scene v14s43c_1q
        with dissolve

        pe "*British accent* That may be true, but the insanity stems from the love that I have for you."

        scene v14s43c_1r
        with dissolve

        u "*British accent* The kingdom... The children! Who will be there if not we?"

        scene v14s43c_1q
        with dissolve

        pe "*British accent* We be only concerned with the now, my King."

        scene v14s43c_3a # TPP. MC starts acting dizzy, Penelope slight tears in her eyes, sad/worried expression, looking at MC
        with dissolve

        pause 0.75

        scene v14s43c_4f # FPP. same as v14s43c_4 Penelope has a sad/worried expression, slight tears in her eyes, mouth closed, looking at MC
        with dissolve

        u "*British accent* I... I'm fading..."

        scene v14s43c_3b # TPP. same as v14s43c_3a MC closes his eyes and lays down on the floor, Penelope looking at MC laying on the floor
        with dissolve

        pause 0.75

        scene v14s43c_6 # FPP. screen is blacked out because MC's eyes are closed
        with dissolve

        pe "*British accent* I will see you on the other side, my love."

        scene v14s43c_6
        with dissolve

        u "(She's lying on me?)"

        scene v14s43c_6
        with dissolve

        pe "*British accent* Goodbye, be free, and... *Sniffles* I'm sorry..."

        scene v14s43c_6
        with dissolve

        pe "And... SCENE!"

        scene v14s43c_7 # FPP. Mc is laying down so the background would resemble as such, Penelope is still laying on top of MC, one hand over his cheek, full smile, and blushing looking at MC, mouth closed
        with dissolve
        
        pause 0.75

        scene v14s43c_7a # FPP. same as v14s43c_7 Penelope's mouth is closed
        with dissolve

        u "*Laughs* That was actually really fun. Even went for a real kiss, huh?"

        scene v14s43c_7
        with dissolve

        pe "Gotta make it seem as real as possible, right?"

        scene v14s43c_3
        with dissolve

        pause 0.75

    else:
        scene v14s43c_1h
        with dissolve

        pe "No need for words, you dirty slag. Ole Brittle has sworn on her life and children that her accusations are true... and you dare say she's a liar?!"

        scene v14s43c_1i
        with dissolve

        u "I dare say plenty! She lies, my love!"

        scene v14s43c_1h
        with dissolve

        pe "I won't hear anymore of this. I'm finished."

        scene v14s43c_5g # TPP. same as v14s43c_5 Penelope is still sitting looking up at MC mouth closed, Mc looking down at Penelope slight sngry expression, mouth open
        with dissolve

        u "You dare speak to the king with such- *Gasps*"

        scene v14s43c_5h # TPP. same as v14s43c_5 MC blinks and stumbles backwards
        with dissolve

        u "*Coughs* I can't... breathe... I..."

        scene v14s43c_5i # TPP. same as v14s43c_5h Penelope stands up with an evil smile looking at MC, Mc stumbles back even more and blinks again
        with dissolve

        pause 0.75

        scene v14s43c_4g # FPP. same as v14s43c_4b Penelope has an evil smile, mouth closed
        with dissolve

        u "You! What... *Moans* What did you do to me?!"

        scene v14s43c_4h # FPP. same as v14s43c_4g Penelope's mouth is open
        with dissolve

        pe "I've saved our kingdom, my darling. I've killed the true snake by simply cutting off the head."

        scene v14s43c_4g
        with dissolve

        u "You sleazy son of a-"

        scene v14s43c_5j # TPP. same as MC v14s43c_5i clutches his chest
        with dissolve

        pause 0.75

        scene v14s43c_5k # TPP. same as v14s43c_5j MC collapses on the floor one arm raised towards Penelope mouth open dying expression, Penelope looking down at MC Full evil smile mouth closed
        with dissolve

        pause 0.75

        scene v14s43c_8 # FPP. Mc is laying on the ground looking up at Penelope, Penelope is kneeling over MC with one leg on either side of the MC's body, Evil smile mouth open, her dress/skirt is resting on her knees allowing for a view of her panties/thong (The ones she's wearing the night of the Homecoming Dance can be used as a reference)
        with dissolve

        pe "Goodnight, my former king."

        scene v14s43c_6
        with dissolve

        pe "And... SCENE!"

    scene v14s43c_3
    with dissolve

    pause 0.75

    scene v14s43c_4a
    with dissolve

    u "Not gonna lie, I had way more fun than I thought I would. *Laughs*"

    scene v14s43c_4
    with dissolve

    pe "Anything can be a fun if you're doing it with the right person."

    scene v14s43c_4a
    with dissolve

    u "Ha... ha... ha... *Chuckles* So, are we done?"

    scene v14s43c_4
    with dissolve

    pe "Yes, sirrrrrr. I need to run anyway, don't forget our scene by next week!"

    scene v14s43c_4a
    with dissolve

    u "I won't."

    scene v14s43c_4
    with dissolve

    pe "Good, see ya!"

    if penelope.relationship.value >= Relationship.LOYAL.value and v14_PenRomScene:

        scene v14s43c_3c # same as v14s43c_3c Penelope quickly kisses MC on the cheek, Penelope eyes closed, Mc eyes open, slight smile
        with dissolve
        
        pause 0.75

    scene v14s43c_9 # Penelope runs off down the hallway back turned to MC
    with dissolve

    u "Oh- (I didn't even say bye... *Laughs* Maybe she was in a rush?)"

    scene v14s43c_10 # TPP. Mc walks down the hallway, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v14s43c_11 # TPP. Mc leaves the school, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v14s43c_12 # TPP. MC starts walking along the sidewalk, slight smile, mouth closed
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v14s44