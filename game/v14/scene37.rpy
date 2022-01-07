# SCENE 37: Penelope date night.
# Locations: Penelope date restaurant 
# Characters: MC (Outfit: Date Outfit), Penelope (Outfit: Date Dress)
# Time: Night

label v14s37:
    $ v14_penelope_date = True

    scene v14s37_1 # TPP. Show MC arriving at the restaurant wearing the nice clothes he put on in scene 34, his clothes slightly blowing from the wind, MC slight smile, mouth closed. 
    with fade

    pause 0.75

    play music "music/v13/Track Scene 42.mp3" fadein 2

    scene v14s37_2 # TPP. Show MC spotting Penelope in the dress she put on in scene 34 outside of the restraunt and walking towards her, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v14s37_2a # TPP. Same as v14s37_2, MC standing infront of Penelope, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    menu:
        "Greet":
            scene v14s37_3
            with dissolve

            u "Hey, you."

            scene v14s37_3a
            with dissolve

            pe "Hey, handsome."

        "Greet with a compliment":
            $ add_point(KCT.BOYFRIEND)
            $ penelope.points += 1

            scene v14s37_3
            with dissolve

            u "Hello, gorgeous."

            scene v14s37_3a
            with dissolve

            pe "Haha, hi."

            scene v14s37_3
            with dissolve

            u "You seriously look amazing."

            scene v14s37_3a
            with dissolve

            pe "*Chuckles* Thank you. You too. As always."

    scene v14s37_3
    with dissolve

    u "*Laughs* I thought I'd get here before you and try to get us a table, didn't think you'd get here so fast."

    scene v14s37_3a
    with dissolve

    pe "If I'm being honest, I started getting dressed as soon as you called and got here as quickly as I could."

    scene v14s37_3
    with dissolve

    u "Wait... Haha, what? You should've told me you were moving at lightning speed. *Laughs* It's too windy out here for you to be waiting."

    scene v14s37_3a
    with dissolve

    pe "Haha, no worries. I love this weather. You ready?"

    scene v14s37_3
    with dissolve

    u "Yes, please."

    scene v14s37_4 # TPP. Show MC holding the door open for Penelope, Penelope not entering yet, MC slight smile, mouth open, Penelope slight smile, mouth closed.
    with dissolve

    u "After you, m'lady."

    scene v14s37_4a # TPP. Penelope walking into the restaurant as MC holds open the door, MC slight smile, mouth closed, Penelope slight smile, mouth open.
    with dissolve

    pe "*Chuckles*"

    stop music fadeout 3
    play music "music/v13/Track Scene 50_2.mp3" fadein 2

    scene v14s37_5 # FPP. MC and Penelope standing next to each other at the front reception of the restaurant, Camera facing the host, Host slight smile, mouth open
    with dissolve

    host "Hello, hello! Just the two of you tonight?"

    scene v14s37_6 # FPP. MC looking at Penelope, Penelope looking at the Host, Penelope slight smile, mouth open.
    with dissolve

    pe "Just two."

    scene v14s37_5
    with dissolve

    host "Perfect, follow me if you would please."

    scene v14s37_7 # TPP. Show MC and Penelope following the Host to their table.
    with dissolve

    pause 0.75

    scene v14s37_8 # TPP. Show MC and Penelope pulling out their seats from under the table.
    with dissolve

    pause 0.75

    scene v14s37_9 # FPP. MC and Penelope(Penelope off camera) sitting at the table. MC looking at the host, Host looking at MC, Host slight smile, mouth open.
    with dissolve

    host "Can I get you guys started with something to drink?"

    scene v14s37_9a # FPP. Same as v14s37_9, Host slight smile, mouth closed.
    with dissolve

    u "I'll just have water, please."

    scene v14s37_10 # FPP. MC and Penelope still sitting down, MC looking at Penelope, Penelope looking at Host (Host off camera), Penolope slight smile, mouth open.
    with dissolve

    pe "Yeah, water for me too."

    scene v14s37_9b # FPP. Same as v14s37_9, Host looking at Penelope (Penelope Off-camera), Host slight smile, mouth open.
    with dissolve

    host "Got it, and do you guys need a minute to look or are you ready to order now?"

    scene v14s37_10
    with dissolve

    pe "I need a few minutes."

    scene v14s37_9b
    with dissolve

    host "Of course, take your time. I'll be back with two waters."

    scene v14s37_9c # FPP. Same as v14s37_9b, Show the Host walking off.
    with dissolve

    pause 0.75

    scene v14s37_10a # FPP. Same as v14s37_10, Penelope looking at MC, MC looking at Penelope, Penelope slight smile, mouth open.
    with dissolve

    pe "I'll be honest... I'm not hungry at all."

    scene v14s37_10b # FPP. Same as v14s37_10a, Penelope slight smile, mouth closed.
    with dissolve

    u "Haha, then why'd you suggest coming here?"

    scene v14s37_10a
    with dissolve

    pe "I just really like this place! Is it bad if I don't order anything?"

    scene v14s37_10b
    with dissolve

    u "Haha no, I won't force you to."

    scene v14s37_10a
    with dissolve

    pe "Hehe, good. I'll just leave a big tip for my water. *Laughs*"

    scene v14s37_10b
    with dissolve

    u "*Chuckles* I've never heard anyone say that."

    scene v14s37_10a
    with dissolve

    pe "I'm a trendsetter, [name]. You can still order whatever you want, though."

    scene v14s37_10b
    with dissolve

    u "It's fine, I'm not gonna eat if you're not."

    scene v14s37_10a
    with dissolve

    pe "Oh... Are you sure?"

    scene v14s37_10b
    with dissolve

    u "Yeah, positive. I'm not really that hungry either, just wanted to be here."

    scene v14s37_11 # TPP. Shot of Penelope and MC staring in each others eyes and smiling at each other, both mouth closed.
    with dissolve

    pause 1.25 
    
    scene v14s37_10a
    with dissolve

    pe "Guess that makes two of us."

    scene v14s37_9d # FPP. Same as v14s37_9c, the host putting the glasses of water on the table for Penelope and MC.
    with dissolve

    host "Here you go, guys."

    scene v14s37_9a
    with dissolve

    u "Thank you."

    scene v14s37_9
    with dissolve

    host "Of course! Still need time or are we ready?"

    scene v14s37_10
    with dissolve

    pe "We're still deciding if we're even hungry, haha, I hope that's okay."

    scene v14s37_9b
    with dissolve

    host "I know what you mean. You two just enjoy your evening and if you want anything, just let me know."

    scene v14s37_9a
    with dissolve

    u "We will, thank you."

    scene v14s37_9c
    with dissolve

    pause 0.75

    scene v14s37_12 # TPP. Show the host walking over to a table with another couple that is sat close to MC and Penelope.
    with dissolve

    pause 0.75

    scene v14s37_13 # TPP. Close up of the Host at a table with the other couple, the gentleman, slight frown, mouth closed, the lady upset expression, mouth closed, host slight smile, mouth open.
    with dissolve

    host "How are you two doing over here? Are we ready to order?"

    scene v14s37_14 # TPP. Close up of just the Gentleman, looking at the Host (Host off-camera), gentleman slight frown, mouth open.
    with dissolve

    gentleman "I apologize, could you give us just a few more-"

    scene v14s37_15 # TPP. Close up of just the lady looking at the Gentleman(Gentleman off-camera), upset expression, mouth open. 
    with dissolve

    lady "Oh my good god, if you gave him all day, he'd take all day. We're ready to order."

    scene v14s37_15a # TPP. Same as v14s37_15, The lady looking at the Host (Host Off-camera), upset expression, mouth open.
    with dissolve

    lady "I'll have a house salad and he'll have the same."

    scene v14s37_16 # TPP. Close up of just the host, the host looking at the lady, host confused face, mouth open.
    with dissolve

    host "Um, okay. Two house salads, with what dressing?"

    scene v14s37_14
    with dissolve

    gentleman "Do you have-"

    scene v14s37_15a
    with dissolve
    
    lady "None."

    scene v14s37_16a # TPP. Same as v14s37_16, Host looking at the gentleman, host confused face, mouth open.
    with dissolve

    host "Anything for you sir?"

    scene v14s37_14
    with dissolve

    gentleman "Hmm, do you guys have a dessert menu? I didn't find one..."

    scene v14s37_15
    with dissolve

    lady "For fuck's sake, you're like a child. That'll be all for now."

    scene v14s37_14a # TPP. Same as v14s37_14, Gentleman looking at the lady (Lady off-camera), gentleman slight frown, mouth open.
    with dissolve

    gentleman "I wanted a-"

    scene v14s37_15
    with dissolve

    lady "If we want dessert, we'll get it later."

    scene v14s37_16
    with dissolve

    host "Okay. Sure."

    scene v14s37_12a # TPP. Same as v14s37_12, The host walking away from the table, confused face, mouth closed.
    with dissolve

    pause 0.75

    scene v14s37_10c # FPP. Same as v14s37_10b, MC looking at Penelope, Penelope looking at MC, Penlope slight sad face, mouth open.
    with dissolve

    pe "*Whispers* That girl is being so mean to her date!"

    scene v14s37_10d # FPP. Same as v14s37_10c, Penelope slight sad face, mouth closed.
    with dissolve

    u "*Whispers* She was pretty rude, yeah. Jeez."

    scene v14s37_10c
    with dissolve

    pe "*Sighs* Some people..."

    scene v14s37_10e # FPP. Same as v14s37_10d, Penlope turning to look over at the previous couple that was having issues, Penelope sad face, mouth closed.
    with dissolve

    pause 0.75

    scene v14s37_10d
    with dissolve

    u "So, what did you do today?"

    scene v14s37_10c
    with dissolve

    pe "I actually had an interview for an on-campus job, but it got cancelled."

    scene v14s37_10e
    with dissolve

    pause 0.75

    scene v14s37_10d
    with dissolve

    u "Oooh, what job?"

    scene v14s37_10c
    with dissolve

    pe "Nope. You're gonna laugh..."

    scene v14s37_10d
    with dissolve

    u "Haha, I promise I won't."

    scene v14s37_10a
    with dissolve

    pe "You already are! *Chuckles*"

    scene v14s37_10b
    with dissolve

    u "Haha, okay, okay... Phew. I'm ready."

    scene v14s37_10a
    with dissolve

    pe "*Sighs* Positive?"

    scene v14s37_10b
    with dissolve

    u "Positive."

    scene v14s37_10a
    with dissolve

    pe "I signed up to be a hall monitor."

    menu:
        "Be serious":
            $ add_point(KCT.BOYFRIEND)
            scene v14s37_10b
            with dissolve
            
            u "Woah, I didn't know that was a thing. Why'd it get cancelled?"

        "Laugh":
            $ add_point(KCT.TROUBLEMAKER)
            scene v14s37_10b
            with dissolve
            
            u "*Laughs* I'm sorry... I-"

            scene v14s37_10c
            with dissolve

            pe "*Sighs*"

            scene v14s37_10d
            with dissolve

            u "I'm sorry. I just... I thought of a cartoon I used to watch that had a hall monitor episode, and it made me-"

            scene v14s37_10f # FPP. Same as v14s37_10c, Penelope neutral face as she is unamused, mouth closed.
            with dissolve

            u "*Coughs* Ahem, excuse me... So, why'd it get cancelled?"

    scene v14s37_10c
    with dissolve

    pe "*Sighs* It was the dean, I swear she's out to get me."

    scene v14s37_10d
    with dissolve

    u "Wait, why?"

    scene v14s37_10c
    with dissolve

    pe "Because of the case I had, for some reason she thinks I'm the devil now. I tried to-"

    scene v14s37_15
    with vpunch

    lady "Get your elbows off of the table! What part of that seems mature to you?"

    lady "I ask for one nice dinner, no hassle and this is the bullshit you give me. *Whispers* What a fucking loser..."

    scene v14s37_14a
    with dissolve

    gentleman "Can you please not speak to me that way? I'm trying to give us a nice evening out."

    scene v14s37_15
    with dissolve
    
    lady "Try harder!"

    scene v14s37_10g # FPP. Same as v14s37_10e, Penelope looking at the couple having issues, Penelope angry expression, mouth open.
    with dissolve

    pe "*Scoffs*"

    scene v14s37_10h # FPP. Same as v14s37_10c, Penlope looking at MC, Penelope angry expression, mouth closed.
    with dissolve

    u "What the hell is her problem?"

    scene v14s37_10i # FPP. Same as v14s37_10h, Penelope angry expression, mouth open.
    with dissolve

    pe "*Whispers* I'm about to say something."

    scene v14s37_10e
    with dissolve

    menu:
        "Same here":
            $ add_point(KCT.BRO)
            scene v14s37_10h
            with dissolve

            u "If she keeps going at him like that, I am too."

        "Focus on us":
            $ add_point(KCT.BOYFRIEND)
            $ v14s37_focus_on_us = True
            scene v14s37_10h
            with dissolve

            u "*Sighs* Penelope, look at me."

            u "I know she's saying mean things, but we came here for us."

            scene v14s37_10c
            with dissolve

            pause 0.75

            scene v14s37_10j # FPP. Same as v14s37_10i, MC holding Penelope's hands across the table, Penelope slight sad face, mouth closed.
            with dissolve

            u "To have a good night on our first real date. I'd like to enjoy that."

            scene v14s37_10k # FPP. Same as v14s37_10j, MC holding Penelope's hand, Penelope slight smile, mouth open.
            with dissolve

            pe "I'm sorry, you're right. She's just-"

            scene v14s37_10l # FPP. Same as v14s37_10k, Penelope slight smile, mouth closed.
            with dissolve

            u "Trust me, I understand."

            scene v14s37_10k
            with dissolve

            pe "*Sighs* Okay."

    scene v14s37_10a
    with dissolve

    pe "So, are you happy to be back from the trip? I've noticed everything is already back in full swing."

    scene v14s37_10b
    with dissolve

    u "Definitely feels like we didn't miss a beat. Classes, frat stuff, Julia across the country... Everything just picked right back up."

    scene v14s37_10m # FPP. Same as v14s37_10a, Penelope confused worried face, mouth open.
    with dissolve

    pe "Julia...?"

    scene v14s37_10b
    with dissolve

    u "Oh! Shit! No, no. It's not what you're thinking. She's my dad's ex. The person who raised me pretty much."

    scene v14s37_10a
    with dissolve

    pe "Oh! *Laughs* I'm sorry, haha."

    scene v14s37_10b
    with dissolve

    u "Haha, no need to apologize. I didn't realize I never really speak about her to anyone."

    scene v14s37_10n # FPP. Same as v14s30_10m, Penelope full smile, mouth closed.
    with dissolve

    pause 0.75

    scene v14s37_10b
    with dissolve

    u "She's in New York for work, and probably won't be back for a while. So with that and school and the frat... Yeah, it's a lot."

    scene v14s37_10a
    with dissolve

    pe "It's kinda weird listening to how involved you are in everything and here I am with nothing to do."

    scene v14s37_10b
    with dissolve

    u "Join a sorority."

    scene v14s37_10a
    with dissolve

    pe "..."
    
    scene v14s37_10b
    with dissolve

    u "No?"

    scene v14s37_10a
    with dissolve

    pe "*Laughs* Those girls would eat me alive like a pack of wolves. No pun intended..."

    scene v14s37_10b
    with dissolve

    u "*Laughs* Maybe they'd like you! All they'd want is for you to hack the school and change their grades to at least a passing level."

    scene v14s37_10a
    with dissolve

    pe "*Chuckles* Not funny."

    scene v14s37_10b
    with dissolve

    u "Too soon? *Chuckles*"

    scene v14s37_10a
    with dissolve

    pe "No, but it was unexpected. I'm trying to forget that whole experience, ha."

    scene v14s37_10b
    with dissolve

    u "The dean obviously isn't letting you forget, so we might as well laugh about it at this point."

    scene v14s37_10a
    with dissolve

    pe "Yeah, you're right. Again. Ugh..."

    scene v14s37_10b
    with dissolve

    u "*Laughs*"

    scene v14s37_10o # FPP. Same as v14s37_10n, Penelope taking a drink of her water.
    with dissolve

    pause 0.75

    scene v14s37_10b
    with dissolve

    u "Remind me again, though. You actually do want the hall monitor job, right?"

    scene v14s37_10a
    with dissolve

    pe "Yeah, I do. It pays really good and literally no one else has applied in the last two weeks that the posting has been up."

    scene v14s37_10b
    with dissolve

    u "And the dean is blocking you from having an interview?"

    scene v14s37_10a
    with dissolve

    pe "Yes. I think she said something to the school board so that they didn't want to give me a chance."

    scene v14s37_10b
    with dissolve

    u "Sounds like slander, bullying, all of the above..."

    scene v14s37_10a
    with dissolve

    pe "Feels a lot like it too."

    scene v14s37_10b
    with dissolve

    u "Why don't you say something to the board?"

    scene v14s37_10a
    with dissolve

    pe "I'd rather not get in any more trouble than I already am. Don't need you worrying about running to my defense all over again."

    scene v14s37_10b
    with dissolve

    u "Haha. That was fun, what are you talking about?"

    scene v14s37_10a
    with dissolve

    pe "Fun for you maybe."

    scene v14s37_10b
    with dissolve

    u "For real though, say something to her about what she's doing and go get your job. She may even respect you for sticking up for yourself."

    scene v14s37_10a
    with dissolve

    pe "That's a long shot, but I'll give it a try."

    scene v14s37_10b
    with dissolve

    u "Good. And if it fails, I will gladly come running to your defense."

    scene v14s37_17 # TPP. Shot of both Penelope and MC starting to lean over the table to kiss each other.
    with dissolve

    pause 1.25

    scene v14s37_17a # TPP. Same as v14s37_17, Penelope and MC kissing across the table.
    with dissolve
    play sound "sounds/kiss.mp3"

    pause 1.75

    scene v14s37_10a
    with dissolve

    pe "I love how you're always looking out for me. Makes me feel like I can be completely vulnerable around you..."

    scene v14s37_10b
    with dissolve

    u "I'll always be there for you, you know that."

    scene v14s37_10a
    with dissolve

    pe "Yeah, I do."

    scene v14s37_15
    with vpunch

    lady "And that's also why you can't keep a fucking job, you're a loser!"

    if v14s37_focus_on_us or kct == "confident":
        scene v14s37_10i
        with dissolve

        pe "*Sighs* [name]... I don't want to ruin our night, but-"

        scene v14s37_10h
        with dissolve

        u "Say no more, let's go. We'll come back another time."

        scene v14s37_10a
        with dissolve

        pe "Thank you."

        scene v14s37_10b
        with dissolve

        u "Always."

        scene v14s37_25 # TPP. Show Penelope leaving money on the table for the waitress, Penlope slight smile, mouth closed.
        with dissolve

        u "(The nicest human in the entire world.)"

        scene v14s37_26 # FPP. MC standing next to the table and holding Penelope's hand and helping her get up, Penelope slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v14s37_23
        with dissolve

        pause 0.75

        stop music fadeout 3
        play music "music/v13/Track Scene 42.mp3" fadein 2

        scene v14s39_1 # FPP. MC and Penelope walking down the side walk, Penelope looking at MC, MC looking at Penelope, Penlope neutral face, mouth open.
        with fade

        pe "That woman was so terrible! How could that man just sit there and take all of her shit?"

    else:
        scene v14s37_10g
        with dissolve

        $ grant_achievement("wrath_of_pen")

        pe "Okay, that's it!"

        scene v14s37_10p # FPP. Same as v14s37_10o, Penelope starting to get up from her seat, Penelope angry face, mouth closed.
        with dissolve

        u "Wait-"

        scene v14s37_18 # TPP. Penelope walking up to the table that the gentleman and the lady are at, Penelope angry face, mouth closed.
        with dissolve

        pause 0.75

        scene v14s37_19 # TPP. Close up of Penelope putting her finger in the ladies face, Penleope angry face, mouth open, Lady shocked face, mouth closed.
        with dissolve

        pe "Listen up, Princess! I came here to go on a wonderful date, just like you. And I CAN'T DO THAT because YOU won't stop being a BITCH!"

        scene v14s37_20 # TPP. Close up of Penelope and the Gentleman looking at each other, Gentleman slight frown, mouth closed, Penelope angry face, mouth open.
        with dissolve

        pe "Sir, kindly, BE A MAN AND STAND UP FOR YOURSELF."

        scene v14s37_19a # TPP. Same as v14s37_19, Penelope with a disgusted angry face, mouth open, Lady shocked face, mouth closed.
        with dissolve

        pe "And you."

        pe "Keep your shitty attitude, and your miserable life to yourself, okay?"
        pe "This world doesn't revolve around you. If I ever see you again and you're speaking to someone like this, I'll have more than just words to say next time."

        scene v14s37_19b # TPP. Same as v14ss37_19a, Penelope with a disgusted angry face, mouth closed, Lady shocked face, mouth open.
        with dissolve

        lady "*Gasps*"

        scene v14s37_20a # TPP. Same as v14s37_20, Penelope angry face, mouth closed, Gentleman slight frown, mouth open.
        with dissolve

        gentleman "I-..."

        scene v14s37_21 # TPP. Close up of just Penelope, Penelope angry face, mouth open.
        with dissolve

        pe "Let's go, [name]."

        scene v14s37_22 # FPP. Penelope and MC standing in the dining area, MC looking at Penelope, Penelope looking at MC, Penelope slightly angry, mouth closed.
        with dissolve

        u "You sure?"

        scene v14s37_22a # FPP. Same as v14s37_22, Penelope slightly angry, mouth closed.
        with dissolve

        pe "Positive."

        scene v14s37_23 # TPP. Show Penelope and MC walking away from the front of the Restaurant/ 
        with dissolve

        pause 0.75

        stop music fadeout 3
        play music "music/v13/Track Scene 42.mp3" fadein 2

        #scene v14s37_24 # FPP. MC and Penelope on the sidewalk, Penelope looking at MC, MC looking at Penelope, Penelope slight smile, mouth closed.
        scene v14s39_1a
        with fade

        u "Are you all good?"

        #scene v14s37_24a # FPP. Same as v14s37_24, Penelope slight smile, mouth open.
        scene v14s39_1
        with dissolve
        
        pe "Yeah, I'm fine. She just really pissed me off, that's all."

        #scene v14s37_24
        scene v14s39_1a
        with dissolve

        u "I understand why."

        scene v14s39_1 # FPP. MC and Penelope walking down the side walk, Penelope looking at MC, MC looking at Penelope, Penlope neutral face, mouth open.
        with dissolve

        pe "That woman was so terrible! How could that man just sit there and take all of her shit?"
    
    stop music fadeout 3

    jump v14s39