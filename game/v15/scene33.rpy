# SCENE 33: Aubrey's Parent's Wedding
# Locations: Aubrey's Parent's Wedding
# Characters: MC (Outfit: Wedding), AUBREY (Outfit: Wedding), NAOMI (Outfit: Wedding), AUBREY'S DAD (Outfit: Wedding), AUBREY'S MOM (Outfit: Wedding), UNCLE RICKY (Outfit: Wedding), WEDDING OFFICIAL (Outfit: 1)
# Time: Morning

label v15s33:
    scene v15s33_1 # TPP. Show the car that MC and Aubrey are in arrived at the Venue (The Venue is a huge white tent)
    with fade(1,0,1)

    pause 

    scene v15s33_2 # TPP. Show MC and Aubrey getting out of the car in their wedding outfits, both slight smile, mouth closed.
    with dissolve

    pause .5

    scene v15s33_3 # FPP. MC and Aubrey stopped on their trail to the Venue, facing each other, MC looking at Aubrey, Aubrey looking at MC, Aubrey concerned, mouth closed.
    with dissolve 

    u "Are you okay?"

    scene v15s33_3a # FPP. MC looking at Aubrey, Aubrey looking at MC, Aubrey concerned, mouth open.
    with dissolve

    au "Yeah..."

    scene v15s33_3
    with dissolve

    u "You don't look too sure."

    scene v15s33_3a
    with dissolve

    au "I'm just mentally preparing myself for all the usual favoritism stuff, ha."

    au "Big occasions with the family can be hard for me sometimes. Know what I mean?"

    scene v15s33_3
    with dissolve

    menu:
        "Be brutally honest.":
            $ add_point(KCT.TROUBLEMAKER)  
            u "To be honest, not really. I'm an only child."

            scene v15s33_3a
            with dissolve

            au "Oh, really? How did I not know that?"

            au "I wonder what else you're hiding from me, haha."

            scene v15s33_3
            with dissolve

            u "Who knows? I'm very mysterious, haha."
        "Reassure her.":    
            $ add_point(KCT.BOYFRIEND)  
            u "Try not to worry. You can talk to me about it whenever you want."

            u "If not, I have a bunch of awful jokes that are guaranteed to cheer you up. *Laughs*"

            scene v15s33_3b # FPP. MC looking at Aubrey, Aubrey looking at MC, Aubrey slight smile, mouth open.
            with dissolve

            au "Thanks, [name]. That's good to know."

    scene v15s33_3
    with dissolve

    u "Come on, let's go in."

    scene v15s33_4 # TPP. Show Mc and Aubrey entering the Venue, both slight smile, mouth closed.
    with fade(1,0,1) 

    pause 
 
    scene v15s33_5 # FPP. MC looking to his left after entering the venue seeing Naomi, Naomi looks a little drunk, smirking, mouth open.
    with vpunch

    na "Hey, I recognize you two! You're that cute couple from Paris, right? *Giggles*"

    scene v15s33_6 # TPP. Show Naomi standing infront of MC and Aubrey, Naomi a little drunk, smirking, mouth closed.
    with dissolve

    pause

    if aubrey_friend: 
        scene v15s33_7 # FPP. In the Venue MC looking at Aubrey, Aubrey looking at Naomi, slight smile, mouth open.
        with dissolve

        au "Naomi, for the one-hundredth time..."

        scene v15s33_8 # FPP. In the Venue MC looking at Naomi, Naomi looking at Aubrey, Naomi a little drunk, smirking, mouth open.
        with dissolve

        na "Yeah, yeah... \"We're not dating!\". Ha, you're so cute."

        na "More for me then, yeah?"

        scene v15s33_8a # FPP. Mc looking at Naomi, Naomi looking at Mc, Naomi a little drunk, winking at MC, biting her lip.
        with dissolve 

        u "(*Gulp*)"
    elif aubreyrs:
        scene v15s33_7
        with dissolve

        au "Haha, shut up."

        scene v15s33_8
        with dissolve

        na "Why?! Don't you want everyone here to know you got your hands all over this hunk?"

        scene v15s33_8a
        with dissolve

        u "Uh, thanks."

        scene v15s33_7a # FPP. MC looking at Aubrey, Aubrey looking at Naomi, slightly annoyed, mouth open.
        with dissolve

        au "*Sighs*"

    scene v15s33_8
    with dissolve

    na "I'm only kidding, sis."

    scene v15s33_8b # FPP. MC looking at Naomi, Naomi looking at MC, Naomi a little drunk, Naomi smirking, mouth closed.
    with dissolve

    u "How are you, Naomi?"

    scene v15s33_8c # FPP. MC looking at Naomi, Naomi looking at Mc, Naomi a little drunk, Naomi smirking, mouth open.
    with dissolve

    na "I'm a little drunk, hehe... You guys have some catching up to do!"

    scene v15s33_7
    with dissolve

    au "Oh, trust me, we'll get right on that. *Laughs*"

    au "Where's Mom? How does she look? Does she need-"

    scene v15s33_8
    with dissolve

    na "Aubrey! *Chuckles* Mom is fine, she looks fine, everything is fine..."

    na "And I must admit, you look gorgeous."

    scene v15s33_7
    with dissolve

    au "Oh, ha. Thanks. You do too."

    scene v15s33_8
    with dissolve

    na "Pfft, I know that already. Best dressed as always."

    scene v15s33_7
    with dissolve

    au "Ha."

    scene v15s33_7d # FPP. MC looking at Naomi, Naomi looking at Aubrey, Naomi a little drunk, smirking, mouth closed.
    with dissolve

    u "(Wow, arrogant much? I mean, she's obviously hot but still...)"

    scene v15s33_8c
    with dissolve

    na "You're looking pretty hot too, [name]."

    scene v15s33_8b
    with dissolve

    u "Thanks... I didn't do much but, at least I'm not wearing a stripper costume."

    scene v15s33_7b # FPP. MC looking at Aubrey, Aubrey looking at MC, Aubrey slight smile, mouth open.
    with dissolve

    au "*Laughs* True."

    scene v15s33_8
    with dissolve

    na "A stripper costume? Haha, what?"

    scene v15s33_7
    with dissolve

    au "Long story..."

    scene v15s33_8c
    with dissolve

    na "Well, even a stripper costume is better than what I last saw you in."

    scene v15s33_8b
    with dissolve

    u "Haha, wow. Thanks for the compliment?"

    scene v15s33_7
    with dissolve

    au "So, seriously... Where's Mom and Dad?"

    scene v15s33_8
    with dissolve

    na "Right over there. Worrying about the flowers or something."

    scene v15s33_7
    with dissolve

    au "Wait, worrying about the flowers? You said everything is fine!"

    scene v15s33_8
    with dissolve

    na "Everything is fine. *Scoffs* It's just flowers, Aubbie"

    scene v15s33_7a
    with dissolve

    au "*Sighs*"

    scene v15s33_9 # TPP. MC following behind, Show Aubrey walking over to her parent's, slightly annoyed, mouth closed, MC, slight smile, mouth closed.
    with dissolve

    pause 

    scene v15s33_10 # TPP. Close up of Naomi's hand grabbing MC's arm.
    with dissolve

    na "Oh, no, no..."

    scene v15s33_11 # FPP. MC turned around to face Naomi, Naomi's back to the entrance, MC looking at Naomi, Naomi looking at MC, Naomi, a little drunk, smirking, mouth open.
    with dissolve

    na "You're coming with me."

    scene v15s33_11a # FPP. MC looking at Naomi, Naomi looking at MC, Naomi a little drunk, Naomi smirking, mouth closed.
    with dissolve

    u "Um, okay... Do I have a choice?"

    scene v15s33_11
    with dissolve

    na "Nope!"

    scene v15s33_12 # FPP. MC sitting at the table, Naomi sitting on the other side, Naomi pouring shots into the first glass,MC looking at Naomi, Naomi looking at the first glass she is pouring into, Naomi smirking, mouth closed.
    with dissolve

    pause 

    scene v15s33_12a # FPP. MC looking at Naomi, Naomi leaning forward and looking at MC, Naomi handing MC one of the shots, Naomi a little drunk, smirking, mouth open.
    with dissolve

    na "You need a shot! Or two... *Giggles* Here."

    na "Cheers, baby!"

    scene v15s33_12b # FPP. MC looking at Naomi, Naomi leaning forward and looking at MC, Naomi handing MC one of the shots, Naomi a little drunk, smirking, mouth closed.
    with dissolve

    menu:
        "Take the shot.":
            $ add_point(KCT.TROUBLEMAKER)

            scene v15s33_13 # TPP. Show Naomi and MC clinking shot glasses, Naomi a little drunk, smirking looking at MC, MC looking at Naomi, slight smile, mouth closed.
            with dissolve

            pause 

            scene v15s33_12d # FPP. MC looking at Naomi, Naomi looking at MC, Naomi a little drunk, Naomi smirking, mouth open.
            with vpunch 

            u "Eurgh! What the..."

            u "What the fuck is that?"

            scene v15s33_12c # FPP. MC looking at Naomi, Naomi looking at MC, the third and fourth glass empty now, Naomi a little drunk, smirking, mouth open.
            with dissolve

            na "Sambuca!"

            scene v15s33_12d
            with dissolve

            u "Sambu- *Gags*"

            scene v15s33_12c
            with dissolve

            na "*Laughs* Not a fan?"

            scene v15s33_12d
            with dissolve

            u "Not at all. That's atrocious."

            scene v15s33_12c
            with dissolve

            na "No way! I love this stuff!"

            scene v15s33_12d
            with dissolve

            u "You're a psycho..."

            scene v15s33_12e # FPP. MC looking at Naomi, Naomi looking at MC, Naomi laughing.
            with dissolve

        "Pretend to take it.":
            $ add_point(KCT.BOYFRIEND)
            scene v15s33_13
            with dissolve

            pause 
            
            scene v15s33_82 # TPP. Close up of just MC's hand pouring his drink on the floor at the alcohol table, only show MC's hand pouring drink on the floor to be reused.
            with dissolve  

            pause

            scene v15s33_12d
            with dissolve

            u "Mmm... Delicious."

            scene v15s33_12c
            with dissolve

            na "Mmm, yes! Sambuca is just the best. You'll be as drunk as me in no time."

            scene v15s33_12d
            with dissolve

            u "Ha, can't wait."

    scene v15s33_12c
    with dissolve

    na "You know what's weird?"

    scene v15s33_12d
    with dissolve

    u "Having this many weddings? *Laughs*"

    scene v15s33_12c
    with dissolve

    na "Haha! Okay, besides that..."

    na "Taking shots kind of makes me horny."

    menu:
        "Flirt.":
            $ add_point(KCT.TROUBLEMAKER)
            $ v15s33_flirt = True

            scene v15s33_12d
            with dissolve

            u "Oh, really? Lucky me."

            scene v15s33_12c
            with dissolve

            na "*Chuckles* We'll see how lucky you are later."

            scene v15s33_12d
            with dissolve

            u "Ha, oh really?"

            scene v15s33_12c
            with dissolve

            na "Hmm, we'll see."
        "Don't flirt.":  
            $ add_point(KCT.BOYFRIEND)  
            scene v15s33_12d
            with dissolve

            u "Oh... *Laughs* Okay, good to know."

            scene v15s33_12c
            with dissolve

            na "Hehe, I'm glad."

    na "Ready for another one?"

    scene v15s33_12d
    with dissolve

    u "I should probably find Aubrey and introduce myself to your parents."

    scene v15s33_12c
    with dissolve

    na "Ugh, okay... Good luck with that!"

    scene v15s33_12d
    with dissolve

    u "Ha, thanks."

    scene v15s33_14 # TPP. MC peaking over the corner seeing Aubrey with her parents at the table with the flower arrangements, Aubrey looking at her dad, Her dad looking back at her, Her mom looking at her dad, all neutral face, mouth closed.
    with fade (1,0,1)

    pause 

    scene v15s33_15 # TPP. Close up of Aubrey's dad, Aubrey's dad looking at Aubrey(Aubrey off camera), Aubrey's dad, neutral face, mouth open.
    with dissolve 

    audad "All I'm saying, Brey, is you can't put all of your eggs into just one basket."

    scene v15s33_16 # TPP. Close up of just Aubrey, Aubrey looking at her dad(her dad off camera), Aubrey sad, mouth closed.
    with dissolve

    pause 

    scene v15s33_15 
    with dissolve 

    audad "Naomi has done exceptionally well, thankfully, but a modeling career requires a lot of hard work."

    aumom "And a lot of talent."

    scene v15s33_16
    with dissolve

    u "(The fuck?)"

    scene v15s33_15
    with dissolve

    audad "Don't you think you should just focus on your studies for right now, and plan on going for something more secure?"

    scene v15s33_17 # TPP. Close up of just Aubrey's mom, Aubrey's mom looking at Aubrey(Aubrey off-camera), Aubrey's mom neutral face, mouth open.
    with dissolve

    aumom "Exactly. Something more in line with your skillset."

    scene v15s33_16
    with dissolve

    au "I can do modeling though. I'm good at modeling. Ha, they hired me on the spot when-"

    scene v15s33_15
    with dissolve

    audad "You're Naomi's sister, honey. Of course they'd offer you a position."

    scene v15s33_17
    with dissolve

    aumom "I don't think you realize how ruthless it can get. Your sister can tell you; she works around the clock to keep her career going."

    scene v15s33_16a # TPP. Aubrey looking at the ground, sad, mouth open.
    with dissolve

    au "*Sighs* I know mom."

    scene v15s33_18 # TPP. Behind shot of MC walking up to Aubrey with her mom and dad, all neutral face, mouth open.
    with dissolve

    u "Hey, you. Is this Mom and Dad?"

    scene v15s33_19 # FPP. MC looking at Aubrey only show Aubrey, Aubrey looking at MC, Slight frown, mouth open.
    with dissolve

    au "Hey, yeah. So, you managed to get away from the superstar herself?"

    scene v15s33_19a # FPP. MC looking at Aubrey, Aubrey looking at MC, Aubrey slight frown, mouth closed.
    with dissolve

    u "Haha, yeah. Barely..."
    
    if aubrey_friend:
        scene v15s33_19b # FPP. MC looking at Aubrey, Aubrey looking at her parents, slight smile, mouth open.
        with dissolve

        au "This is my friend, [name]."
    elif aubreyrs:
        scene v15s33_19b
        with dissolve

        au "This is my date, [name]."

    scene v15s33_20 # FPP. MC looking at both of Aubrey's parents, Both her parents looking at MC, neutral face, mouth closed.
    with dissolve

    u "Pleased to meet you both. And congratulations on your second wedding day."

    scene v15s33_21 # TPP. Show MC and Aubrey's dad shaking hands, MC slight smile, mouth closed, Aubrey's dad neutral face, mouth open.
    with dissolve

    audad "It's very nice to meet you, [name]."

    scene v15s33_22 # FPP. MC looking at Aubrey's mom, Aubrey's mom looking at MC, Aubrey's mom neutral face, mouth open.
    with dissolve

    aumom "Yes, it is, and thank you..."

    aumom "I'm happy with the arrangements and all but I must say, we had much better flowers at our first wedding."

    scene v15s33_23 # FPP. MC looking at Aubrey's dad, Aubrey's dad looking at Aubrey's mom, Aubrey's dad neutral face, mouth open.
    with dissolve

    audad "Oh, my..."

    audad "I told you already, I'll get a refund."

    scene v15s33_22a # FPP. MC looking at Aubrey's mom, Aubrey's mom looking at Aubrey's dad, Aubrey's mom neutral face, mouth open.
    with dissolve

    aumom "How?! We're already using them!"

    scene v15s33_19c # FPP. MC looking at Aubrey, Aubrey looking at Aubrey's mom, Aubrey neutral face, mouth open.
    with dissolve

    au "Mom..."

    scene v15s33_22b # FPP. MC looking at Aubrey's mom, Aubrey's mom looking at Aubrey, Aubrey's mom neutral face, mouth open.
    with dissolve

    aumom "And it's not that they aren't pretty, they are... Pretty..."

    aumom "But they're just not what I was envisioning."

    scene v15s33_22d # FPP. MC looking at Aubrey's mom, Aubrey's mom looking at Aubrey, Aubrey's mom neutral face, mouth closed.
    with dissolve

    u "(Damn, we've got a bridezilla over here! Ha... Yikes.)"

    scene v15s33_19c
    with dissolve

    au "Can you please just try to forget about the flowers and enjoy your special day?"

    scene v15s33_22b
    with dissolve

    aumom "Flowers make a wedding, honey. You might not care much about it, but your grandma was a professional florist and I know a thing or two ab-"

    scene v15s33_19c
    with dissolve

    au "About arrangements. Yeah, so I've heard."

    scene v15s33_23a # FPP. MC looking at Aubrey's dad, Aubrey's dad looking at Aubrey, Aubrey's dad neutral face, mouth open.
    with dissolve

    audad "Your grandma had very high standards when it came to her flowers."

    scene v15s33_22b
    with dissolve

    aumom "She did indeed."

    scene v15s33_23a
    with dissolve

    audad "And even higher standards for potential husbands for her daughters."

    scene v15s33_22c # FPP. MC looking at Aubrey's mom, Aubrey's mom looking at Aubrey's dad, Aubrey's mom slight smile, mouth open.
    with dissolve

    aumom "True. So, how I ended up with you, no idea. *Chuckles*"

    scene v15s33_23b # FPP. MC looking at Aubrey's dad, Aubrey's dad looking at Aubrey's mom, Aubrey's dad slight smile, mouth closed.
    with dissolve

    audad "*Laughs* I should know better after all these years than to go fishing for a compliment"

    scene v15s33_22c
    with dissolve

    aumom "Haha, my silly man."

    scene v15s33_20a # FPP. Show Aubrey's parents kissing.
    with dissolve

    au "Gross..."

    u "(Very gross...)"

    scene v15s33_19d # FPP. MC looking at Aubrey, Aubrey facing MC again, Aubrey looking at MC, Aubrey grossed out, mouth open.
    with dissolve

    au "Let's get a drink?"

    scene v15s33_19e # FPP. MC looking at Aubrey, Aubrey looking at MC, Aubrey grossed out, mouth closed.
    with dissolve

    u "Absolutely."

    scene v15s33_24 # TPP. MC and Aubrey walking over to the drinks table, both slight smile, mouth closed.
    with dissolve 

    pause

    scene v15s33_25 # FPP. MC and Aubrey at the drinks table, Aubrey next to MC, MC looking at Aubrey, Aubrey looking at MC, slight smile, mouth open.
    with dissolve

    au "Let's have a shot. I need one after that, haha!"

    scene v15s33_25a # FPP. MC looking at Aubrey, Aubrey looking at MC, slight smile, mouth closed.
    with dissolve

    u "*Laughs* Okay, fair."

    scene v15s33_26 # FPP. MC looking down at the table pouring alcohol into a shot glass, there is two shot glasses in shot, First one being filled by MC.
    with dissolve

    pause 

    scene v15s33_27 # TPP. MC and Aubrey clinking shot glasses, MC looking at Aubrey, Aubrey looking at MC, Aubrey slight smile, mouth open.
    with dissolve 

    au "Cheers!"

    menu:
        "Take it.":
            $ add_point(KCT.BOYFRIEND)
            scene v15s33_13a # TPP. MC and Aubrey clinking shot glasses, Both slight smile, mouth closed.
            with dissolve

            pause 

            scene v15s33_25a 
            with vpunch

            u "Eurgh! Fuck Sambuca..."

            scene v15s33_25
            with dissolve

            au "Ha! What? You don't like it?"

            scene v15s33_25a
            with dissolve

            u "No, I don't like it! How the hell are you guys drinking this shit?"

            scene v15s33_25
            with dissolve

            au "*Laughs* Years of practice."

        "Pretend to take it.":
            $ add_point(KCT.TROUBLEMAKER)
            scene v15s33_13a
            with dissolve 

            pause

            scene v15s33_82
            with dissolve 

            pause

            scene v15s33_25a 
            with dissolve 

            u "Mmm...That hit the spot, ha."

            scene v15s33_25
            with dissolve

            au "Honestly, it's just what I needed."

    scene v15s33_25b # FPP. MC looking at Aubrey, Aubrey looking at her Uncle across the table, slight smile, mouth open.
    with dissolve

    au "Oh! There's my uncle Ricky."

    scene v15s33_28 # FPP. MC looking across the Drinks table and looking at Aubrey's Uncle(The uncle looks sort of like a redneck, flannel, brown pants, boots) who is next to Naomi, Aubrey's uncle holding a beer looking at Naomi, Aubrey's uncle slight smile, mouth open.
    with dissolve

    rick "I suspect that you encountered many fine cheeses while you were in Europe."

    scene v15s33_12h # FPP. MC looking at Naomi, Naomi facing and looking at Aubrey's Uncle, Naomi bored, mouth open.
    with dissolve

    na "Oh yeah, sure... France is full of cheese..."

    scene v15s33_28
    with dissolve

    rick "Oh, the French! Incredible cheese makers. Masters of the craft!"

    scene v15s33_28a # FPP. Aubrey's Uncle looking at Aubrey, MC looking at Aubrey's Uncle, Aubrey's uncle slight smile, mouth open.
    with dissolve

    rick "Oh! Hello, Aubrey."

    scene v15s33_25b
    with dissolve

    au "Hi, uncle Ricky."

    scene v15s33_28b # FPP. Aubrey's Uncle looking at Mc, MC looking at Aubrey's uncle, Aubrey's uncle slight smile, mouth open.
    with dissolve

    rick "And who's this young man you're dragging along with you?"

    scene v15s33_25b
    with dissolve

    au "*Giggles* This is [name]."

    scene v15s33_28c # FPP. Aubrey's Uncle looking at MC, MC looking at Aubrey's Uncle, Aubrey's uncle slight smile, mouth closed.
    with dissolve

    u "Hi."

    if aubreyrs:
        scene v15s33_25b
        with dissolve

        au "He's my date."

        scene v15s33_28b
        with dissolve

        rick "Well, it's a pleasure to meet you."

        scene v15s33_29 # TPP. Don't show Naomi or Aubrey so this can be reused :) Show MC and Aubrey's uncle shaking hands, both slight smile, mouth closed.
        with dissolve

        pause 

        scene v15s33_28a
        with dissolve 

        rick "Damn, Aubs. A pretty face and strong handshake! He might be a keeper, this one."

        scene v15s33_25c # FPP. Aubrey looking at MC, MC looking at Aubrey, Aubrey slight smile, Aubrey blushing, mouth closed.
        with dissolve

        pause

        scene v15s33_28c
        with dissolve 

        u "*Laughs* Thank you. I appreciate it. I hope she keeps me..."

        scene v15s33_30 # TPP. MC kissing Aubrey on the Cheek. Aubrey smiling and blushing, mouth closed.
        with dissolve
    else:
        scene v15s33_28b
        with dissolve

        rick "Hello, [name]. Are you a good friend to my favorite niece?"

        scene v15s33_28c
        with dissolve

        u "*Chuckles*"

        scene v15s33_12h
        with dissolve

        na "Hey! I'm right here you jackass."

        scene v15s33_25d # FPP. MC looking at Aubrey, Aubrey looking at Naomi, Aubrey smirking, mouth open.
        with dissolve

        au "Haha, we see you princess. Don't cry."

        u "(So, he's the second black sheep of the family I assume? Ha...)"

    scene v15s33_28b
    with dissolve

    rick "We were just discussing the different cheeses we have to choose from tonight."

    scene v15s33_28c
    with dissolve

    u "Ah, interesting."

    scene v15s33_28b
    with dissolve

    rick "I think so too! It's nice to have found another cheese connoisseur."

    scene v15s33_31 # TPP. Show Naomi and Aubrey stepped away from the group, Naomi looking at Aubrey, Aubrey looking at Naomi, Naomi smirking, mouth open, Aubrey smirking, mouth open.
    with dissolve

    na "*Whispers* Run away with me?"

    au "*Whispers* Right behind you."

    u "Where are you-"

    u "(*Sighs* They're most dangerous when they're together... Haha.)"

    scene v15s33_28b
    with dissolve

    rick "Tell me, [name], do you like blue cheese?"

    scene v15s33_28c
    with dissolve

    u "Um..."

    menu:
        "Blue cheese?":
            $ add_point(KCT.TROUBLEMAKER)
            u "Blue cheese? I'm pretty sure that if your cheese is blue, you shouldn't-"

            scene v15s33_28b
            with dissolve

            rick "Haha! You're pulling my leg, right?"

            rick "How can you not know what blue cheese is? What are they even teaching you kids these days?"

            scene v15s33_28c
            with dissolve

            u "Ha, well... Uh, economics and history? Things like that."

            scene v15s33_28b
            with dissolve

            rick "Ah, come on. That shit is old news... *Scoffs*"

            scene v15s33_28c
            with dissolve

            u "(You know what? I like this guy.) *Laughs*"

        "Blue cheese is great!":
            $ add_point(KCT.BRO)
            u "Are you kidding? Blue cheese is great. It's like, top tier of all cheeses."

            scene v15s33_28b
            with dissolve

            rick "Yes!"

            rick "You're a good man!"

            scene v15s33_28c
            with dissolve

            u "Haha..."

    scene v15s33_32 # TPP. Show Aubrey's Uncle picking up a cracker with cheese on it.          
    with dissolve

    rick "Here, try this and tell me what you think."

    scene v15s33_28d # FPP. Aubrey's Uncle holding the cheese and crackers infront of MC's face, Aubrey's uncle, slight smile, mouth closed.
    with dissolve

    u "Oh- Uh... (Am I about to eat cheese out of a grown man's hands?)"

    menu:
        "Eat it.":
            $ add_point(KCT.BRO)
            $ v15s33_cheese = True

            u "(Yes. Yes, I am.)"

            scene v15s33_33 # TPP. Show Aubrey's Uncle hand feeding MC the cheese and cracker, Aubrey's uncle slight smile, mouth closed.
            with dissolve

            pause

            scene v15s33_28c 
            with dissolve

            u "Mmm! *Coughs* Thanks..."

            u "(Man, what the hell is this stuff?)"

            scene v15s33_28b
            with dissolve

            rick "That's Stilton cheese, buddy! Do you feel it?"

            scene v15s33_28c
            with dissolve

            u "Ugh, I feel... Something... *Coughs*"

            scene v15s33_28b
            with dissolve

            rick "England's finest cheese! Imported specially for the wedding."

            scene v15s33_28c
            with dissolve

            u "(It smells like ass, dude... What the fuck?)"

            u "I can really taste the... (Ugh, fuck...) The quality."

            scene v15s33_28b
            with dissolve

            rick "I'm glad you approve! It's a family favorite."

            scene v15s33_28c
            with dissolve

            u "(This family and their weird taste buds...)"

        "Don't eat it.":
            $ add_point(KCT.TROUBLEMAKER)
            u "(Not a fucking chance.)"

            u "You know what, uh... Thanks, but I'm not feeling hungry right now."

            scene v15s33_28b
            with dissolve

            rick "This is Stilton, young man. A very popular cheese from England."

            rick "I imported it just for the wedding. My brother and his wife are huge fans of it."

            scene v15s33_28d
            with dissolve

            u "Wow, that's... Interesting."

            u "(Why the fuck does it smell so... Wrong?)"

            scene v15s33_28b
            with dissolve

            rick "*Sighs*"

            rick "Well, your loss. Make sure you try some before you go, I want to know what you think."

            scene v15s33_28c
            with dissolve

            u "Okay, yeah. Sure thing."

            scene v15s33_28b
            with dissolve

            rick "But hurry up before I eat it all! *Laughs*"

    if v15s33_cheese:
        scene v15s33_28b
        with dissolve

        rick "So, you and my little Brey are close?"

        scene v15s33_28c
        with dissolve

        u "Brey as in Aubrey, right? Haha."

        scene v15s33_28b
        with dissolve

        rick "Oh, yeah. Sorry, force of habit around here. She's always been my sidekick, little Brey."

        scene v15s33_28c
        with dissolve

        u "Ha, no worries. She seems to have smiled the most so far when speaking to you, so... *Chuckles*"
    
        u "But, uh, yeah... We go to college together, just met this year."

        scene v15s33_28b
        with dissolve

        rick "Lives in her older sister's shadow, you know."

        scene v15s33_28c
        with dissolve

        u "(No shit... We should play this safe though, ha.)"

        u "What do you mean by that?"

        scene v15s33_28b
        with dissolve

        rick "Naomi is clearly the favorite; everyone can see it. You don't have to act all, \"good\" around me, kid. Neither of you do."

        scene v15s33_28c
        with dissolve

        u "Oh, well, thanks. It's nice to see that Aubrey has always had someone on her side, I guess."

        scene v15s33_28b
        with dissolve

        rick "Ha. Yeah."

        scene v15s33_28c
        with dissolve

        u "Why is that, though? It's really unfair how hard everyone is on Aubrey."

        scene v15s33_28b
        with dissolve

        rick "Long story short? Naomi was planned, Aubrey wasn't."

        scene v15s33_28c
        with dissolve

        u "Damn."

        scene v15s33_28b
        with dissolve

        rick "Yep, so when Aubrey came along... *Sighs*"

        rick "They had to pull the plug on a big business venture they had planned. And this business plan had been the goal for... Years."


        scene v15s33_28b
        with dissolve

        rick "Between raising two girls and saving up for Aubrey's college education..."

        rick "Doing everything to ensure that your child has a solid start in life is always the plan, ha."

        scene v15s33_28b
        with dissolve

        rick "But they couldn't live the pretty life they pictured after Brey was born."

        scene v15s33_28c
        with dissolve

        u "(Fuck's sake...) That's just... I mean, it's horrible."

        scene v15s33_28b
        with dissolve

        rick "I don't think they're aware of it, but I do think there's a subconscious resentment there. Feel me?"

        scene v15s33_28c
        with dissolve

        u "I do, yeah. It's not her fault, though."

        scene v15s33_28b
        with dissolve

        rick "Not at all, no. And they're pushing her to do anything but be like Naomi, for what reason?"


        scene v15s33_28c
        with dissolve

        u "Ha... Yeah, I don't know. It's strange."

        scene v15s33_28b
        with dissolve

        rick "Whether you end up being just a friend or... Something more."

        rick "Make sure you look after her for me."

        scene v15s33_28c
        with dissolve

        u "I will, I do."

        u "Thanks... A lot. For sharing that with me."

        scene v15s33_28b
        with dissolve

        rick "That's okay. It's the cheese talking! *Laughs* Our little secret, alright?"

        scene v15s33_28c
        with dissolve

        u "Right."

        scene v15s33_29
        with dissolve 

        pause 

    play sound "sounds/bells.mp3"
    # Asked for hand bell sounds but we only have the clocktower bells.

    scene v15s33_28b
    with dissolve 

    rick "Oh shit- I believe that's lunch being served over there. Let's head over."

    scene v15s33_28c
    with dissolve

    u "Sounds good."

    scene v15s33_35 # TPP. Show Mc and Aubrey's Uncle sitting next to each other across from Naomi and Aubrey, Aubrey opposite of MC, Naomi opposite of Aubrey's Uncle, all slight smile, mouth closed.
    with fade (1,0,1)

    pause 

    scene v15s33_36 # FPP. MC looking at Aubrey's Uncle, Aubrey's uncle looking at the table, Naomi and Aubrey off camera not shown, Aubrey's uncle slight smile, mouth closed.
    with dissolve 

    rick "This looks wonderful!"

    scene v15s33_37 # TPP. Show MC, Aubrey's Uncle, Naomi, and Aubrey eating with food on their plates.
    with fade(1,0,1)

    pause 

    scene v15s33_38 # FPP. MC looking across the table at Aubrey, Aubrey looking at her plate as she eats oblivious to MC, Aubrey slight smile, mouth closed.
    with vpunch

    u "(Wait- What was that? I just felt something touch my leg...)"

    scene v15s33_39 # FPP. MC looking to the left of Aubrey at Naomi, Naomi looking at Mc subtly, Naomi smirking slightly, mouth closed.
    with dissolve

    u "(Holy sh- *Gasps*)"

    u "(There it was again! Is she...?)"

    scene v15s33_40 # FPP. MC looking under the table, Naomi's shoeless foot rubbing on MC's crotch.
    with dissolve

    u "(Oh... Shit...)"

    scene v15s33_38
    with dissolve

    pause 

    scene v15s33_39
    with dissolve 

    u "(*Moans* Okay, what the fuck... *Chuckles* Is she really doing this right now?)"

    scene v15s33_40
    with dissolve

    menu:
        "Push it away.":
            $ add_point(KCT.BOYFRIEND)
            u "(This is definitely not a good idea, haha. I'm eating lunch with her family for fucks sake...)"

            scene v15s33_40a # FPP. Show MC's hand gently pushing Naomi's foot away.
            with dissolve

            u "*Sighs*"

            scene v15s33_40
            with vpunch

            u "(What- Back again? She's being relentless...)"

        "Let her continue.":
            $ add_point(KCT.TROUBLEMAKER)
            u "(No harm in enjoying it, right? Ha... *Moans*)"

    scene v15s33_39a # FPP. MC looking at Naomi, Naomi looking at MC, Naomi winking at MC and biting her lip.
    with dissolve 

    u "(*Moans* Huh...? Wait-)"

    scene v15s33_38a # FPP. MC looking at Aubrey, Aubrey looking at MC, Aubrey confused, mouth open.
    with vpunch

    au "Hey, you okay...?"

    scene v15s33_38b # FPP. MC looking at Aubrey, Aubrey looking at MC, Aubrey confused, mouth closed.
    with dissolve

    u "(It's Naomi rubbing my dick?!)"

    scene v15s33_41 # FPP. MC now standing and looking at Aubrey, Aubrey looking up at MC, Aubrey confused, mouth closed.
    with dissolve

    u "Um, yeah. I, uh- Please excuse me... I just need to use the bathroom."

    scene v15s33_42 # FPP. MC standing looking to the left of Aubrey at Naomi, Naomi looking at MC, Naomi smirking, mouth open.
    with dissolve

    na "*Giggles* Okay!"

    scene v15s33_41a # FPP. MC looking at Aubrey, Aubrey looking at MC, Aubrey confused, mouth open.
    with dissolve

    au "Do you want me to come with you?"

    scene v15s33_41
    with dissolve

    u "No, no. It's fine, I promise. Enjoy your meal."

    scene v15s33_41a
    with dissolve

    au "Okay..."

    scene v15s33_43 # TPP. Show MC walking away from the table, Aubrey's uncle, Naomi, and Aubrey looking at MC leave, MC neutral face, mouth closed. Aubrey's Uncle confused, mouth closed. Naomi smirking, mouth closed. Aubrey concerned, mouth closed.
    with dissolve 

    pause

    play sound "sounds/doorclose.mp3"
    
    scene v15s33_44 # TPP. Show MC closing the bathroom door, neutral face, mouth closed.
    with dissolve 

    pause

    scene v15s33_45 # TPP. Show MC leaning against the wall in the bathroom as he thinkss, neutral face, mouth open.
    with dissolve 

    u "*Whispers* What the hell..."

    if v15s33_flirt:
        scene v15s33_45a # TPP. Show Mc leaning against the wall in the bathroom as he thinks, neutral face, mouth closed.
        with dissolve 

        u "(I didn't think she'd do something like that during the fancy lunch... Ha!)"
    else:
        if aubreyfriend:
            scene v15s33_45
            with dissolve

            u "What is wrong with Naomi? Why did she..."
        elif aubreyrs:
            scene v15s33_45a
            with dissolve 

            u "What was she thinking?! This is fucking crazy..."

    scene v15s33_45a 
    with dissolve 

    u "(And Aubrey was just sitting right there... Her entire family, too...) *Sighs*"

    play sound "sounds/dooropen.mp3"

    scene v15s33_44a # TPP. Show Naomi entering the bathroom, smirking, mouth closed.
    with dissolve

    pause

    play sound "sounds/doorclose.mp3"

    scene v15s33_44b # TPP. Show Naomi closing the bathroom door, smirking, mouth closed.
    with dissolve

    pause

    scene v15s33_46 # FPP. MC standing up straight, Naomi approaching MC, MC looking at Naomi, Naomi looking at MC, Naomi smirking, mouth open.
    with dissolve

    na "Creative thinking, cutie! Glad you picked up what I was putting down, haha."

    scene v15s33_46a # FPP. Naomi standing infront of MC, MC looking at Naomi, Naomi looking at MC, Naomi smirking, mouth closed.
    with dissolve

    u "Naomi, I think-"

    scene v15s33_46b # FPP. Naomi standing infront of MC, MC looking at Naomi, Naomi looking at MC, Naomi's hand on MC's cheek, Naomi smirking, mouth open.
    with dissolve

    na "You don't need to think, [name]... I told you..."

    na "*Whispers* I get horny after shots."

    scene v15s33_46c # FPP. Naomi looking at MC, MC looking at Naomi, Naomi's hand on MC's cheek, Naomi biting her lips as she looks at MC.
    with dissolve

    u "(Fuck...)"

    scene v15s33_46b
    with dissolve

    na "You're about to find out how talented I really am."

    scene v15s33_46c
    with dissolve

    u "(Okay, [name]... Use your head here...)"

    u "(No, no, no! Not that one, not that head!"

    scene v15s33_46b
    with dissolve

    na "Are you gonna help me get these things off you or what?"

    scene v15s33_46c
    with dissolve

    menu:
        "Refuse.":
            $ add_point(KCT.BOYFRIEND)
            u "Naomi, no..."

            scene v15s33_46d # FPP. Naomi steps back her hand no longer on MC's cheek, MC looking at Naomi, Naomi looking at MC, Naomi confused, mouth open.
            with dissolve

            na "Excuse me?"

            scene v15s33_46e # FPP. Naomi looking at MC, MC looking at Naomi, Naomi confused, mouth closed.
            with dissolve

            u "No. I said no."

            if v15s33_flirt:
                scene v15s33_46d
                with dissolve

                na "But you... Earlier we-"

                scene v15s33_46e
                with dissolve

                u "I know. I'm sorry."

                scene v15s33_46f # FPP. Naomi looking at MC, MC looking at Naomi, Naomi slightly angry, mouth open.
                with dissolve

                na "*Scoffs* You're sorry?"
            else:
                if aubrey_friend:
                    scene v15s33_46e
                    with dissolve

                    u "As much as I appreciate your interest in me, I'm here with Aubrey and for Aubrey."

                    scene v15s33_46d
                    with dissolve

                    na "Yeah, but you're not-"

                    scene v15s33_46e
                    with dissolve

                    u "I can't hook up with her sister in the bathroom."

                    scene v15s33_46d
                    with dissolve

                    na "Ha..."
                elif aubreyrs:
                    scene v15s33_46e
                    with dissolve

                    u "What the hell are you thinking? You know I'm dating your sister."

                    scene v15s33_46d
                    with dissolve

                    na "Oh, come on... Like that means anything."

                    scene v15s33_46e
                    with dissolve

                    u "What?"

                    scene v15s33_46g # FPP. Naomi looking at MC, MC looking at Naomi, Naomi smirking, mouth open.
                    with dissolve

                    na "She dates all the time, it means nothing to her! All of her exes know that, that's why they hook up with me... *Giggles*"

                    scene v15s33_46h # FPP. Naomi looking at MC, MC looking at Naomi, Naomi smirking, mouth closed.
                    with dissolve

                    u "(I don't hit women... I don't hit women... I don't hit women...)"
            scene v15s33_46e
            with dissolve

            u "*Sighs* And in case you forgot, this is your parent's wedding day."

            scene v15s33_46d
            with dissolve

            na "Their second wedding day!"

            scene v15s33_46e
            with dissolve

            u "I don't give a shit!"

            scene v15s33_46f
            with dissolve

            na "Are you being serious right now?"

            scene v15s33_46i # FPP. Naomi looking at MC, MC looking at Naomi, Naomi slightly angry, mouth closed.
            with dissolve

            u "As serious as I can possibly be."

            scene v15s33_46f
            with dissolve

            na "Who the fuck do you think you are? Nobody has turned me down. Ever."

            scene v15s33_46i
            with dissolve

            u "Sorry."

            u "I'm going back to the table."

            scene v15s33_46f
            with dissolve

            na "Ugh! Wait-"

            scene v15s33_47 # TPP. Close up of Naomi's hand pulling MC's phone out his pocket.
            with dissolve

            u "Naomi, stop! What are you doing?"

            scene v15s33_46j # FPP. Naomi looking at and tapping on MC's phone, MC looking at Naomi, Naomi neutral face, mouth open.
            with dissolve

            na "You're definitely not getting away this easily. *Scoffs*"

            scene v15s33_47a # TPP. Close up of Naomi's hand putting MC's phone back in his pocket.
            with dissolve

            pause 

            scene v15s33_46g
            with dissolve

            na "There. Now you have my number."

            scene v15s33_46h
            with dissolve

            u "Naomi..."

            scene v15s33_46g
            with dissolve

            na "This isn't over yet."

            scene v15s33_46h
            with dissolve

            u "*Sighs*"

            play sound "sounds/dooropen.mp3"

            scene v15s33_44f # FPP. Show MC leaving the bathroom after opening the door, neutral face, mouth closed.
            with dissolve

            u "(I can't believe that just happened...)"

            scene v15s33_34a # FPP. Show MC walking to the lunch area table, neutral face, mouth closed.
            with fade (1,0,1) 

            pause 

            scene v15s33_41a
            with dissolve 

            au "*Whispers* All good?"

            scene v15s33_38b
            with dissolve

            u "*Whispers* Yeah, yeah. Perfect."

            scene v15s33_48 # TPP. Close up of Aubrey at the table looking towards the bathroom, neutral face, mouth closed.
            with dissolve

            pause

            scene v15s33_38c # FPP. MC looking at Aubrey, Aubrey looking at MC, Aubrey slight smile, mouth closed.
            with dissolve 

            u "(Phew... Let's hope no one noticed any of that.))"

        "Let her continue.":
            $ add_point(KCT.TROUBLEMAKER)
            $ aubrey_mad = True

            u "(Why the hell not...?) Ha..."

            scene v15s33_50 # FPP. In the bathroom, Naomi on her knees infront of MC, MC looking down at Naomi, Naomi looking up at MC, smirking, mouth closed.
            with dissolve

            na "Ooh..."

            pause

            scene v15s33_50a # FPP. MC looking at Naomi, Naomi kissing the tip of MC's dick.
            with dissolve 

            pause

            scene v15s33_50b # FPP. MC looking at Naomi, Naomi looking at MC's dick, smirking, mouth open.
            with dissolve 

            na "Hello, big boy."

            scene v15s33_50a
            with dissolve

            u "(This is actually happening...)"
 
            image v15naobj = Movie(play="images/v15/Scene33/v15naobj.webm", loop=True, image="images/v15/Scene33/v15naobjStart.webp", start_image="images/v15/Scene33/v15naobjStart.webp")
            image v15naobjf = Movie(play="images/v15/Scene33/v15naobjf.webm", loop=True, image="images/v15/Scene33/v15naobjStart.webp", start_image="images/v15/Scene33/v15naobjStart.webp")
            image v15naohj = Movie(play="images/v15/Scene33/v15naohj.webm", loop=True, image="images/v15/Scene33/v15naohjStart.webp", start_image="images/v15/Scene33/v15naohjStart.webp")
            image v15naohjf = Movie(play="images/v15/Scene33/v15naohjf.webm", loop=True, image="images/v15/Scene33/v15naohjStart.webp", start_image="images/v15/Scene33/v15naohjStart.webp")

            scene v15naobj # Ignore as anim
            with dissolve
            pause

            na "Mmmm..."

            if aubreyrs:
                u "Fuuuuck... (This is so fucking wrong...)"
            elif aubrey_friend:
                u "Oh, my god... Naomi... (Aubrey probably wouldn't like this...)"

            u "*Moans*"

            scene v15naobjf # Ignore as anim
            with dissolve
            pause 

            u "(But it feels so... Right... Ha.)"

            u "Mmm, Naomi... *Moans*"

            na "*Mumbing* Mmm hmm?"

            u "Yesss..."

            scene v15naohj # Ignore as anim
            with dissolve
            pause 

            na "You like it when supermodels suck on your dick, huh? *Giggles*"

            scene v15naohjf # Ignore as anim
            with dissolve

            u "Are you..."

            u "Kidding? Ha..."

            scene v15naobjf
            with dissolve
            pause

            u "You're so fucking hot, Naomi-"

            play sound "sounds/dooropen.mp3"

            scene v15s33_51 # TPP. Close up of Aubrey at the entrance of the bathroom, Aubrey angry, mouth open.
            with vpunch

            au "I fucking KNEW IT!"

            scene v15s33_51a # FPP. CLose up of Aubrey at the entrance of the bathroom, Aubrey angry, mouth closed.
            with dissolve

            u "Aubrey-"

            scene v15s33_51
            with dissolve 

            au "Could you have been any more obvious?!"

            scene v15s33_49 # TPP. MC pulling up his pants.
            with dissolve

            pause
            
            scene v15s33_52 # TPP. Aubrey walking over to MC and Naomi, Aubrey angry, mouth closed.
            with dissolve

            pause 

            scene v15s33_53 # FPP. MC looking at Naomi, Naomi looking at Aubrey, Naomi smirking, mouth open.
            with dissolve 

            na "*Whispers* I mean... Probably."

            scene v15s33_54 # FPP. Aubrey in the bathroom with MC and Naomi, MC looking at Aubrey, Aubrey looking at MC, Aubrey angry, mouth open.
            with dissolve

            au "How could you do this, [name]? That's my..."

            scene v15s33_54a # FPP. MC looking at Aubrey, Aubrey looking at MC, Aubrey tearing up, Aubrey angry, mouth open.
            with dissolve

            au "*Whispers* That's my fucking sister, [name]..."

            scene v15s33_54b # FPP. MC looking at Aubrey, Aubrey looking at MC, Aubrey tearing up, Aubrey angry, mouth closed.
            with dissolve

            u "I know, Aubrey. I-"

            scene v15s33_54a
            with dissolve

            au "Any girl but my sister."

            scene v15s33_54c # FPP. MC looking at Aubrey, Aubrey looking at MC, Aubrey crying and sad, mouth open.
            with dissolve

            au "*Sobbing* How could you?"

            scene v15s33_54d # FPP. MC looking at Aubrey, Aubrey looking at Mc, Aubrey crying and sad, mouth open.
            with dissolve

            u "I'm sorry, Aubrey. We just-"

            scene v15s33_54c
            with dissolve

            au "Don't... Don't even try to talk yourself out of this."

            scene v15s33_54d
            with dissolve

            u "*Sighs*"

            scene v15s33_54c
            with dissolve

            au "Ha... Unbelievable."

            scene v15s33_53
            with dissolve

            na "Aubby, he didn't even cum yet, I mean-"

            scene v15s33_53a # FPP. MC looking at Naomi, Naomi looking at Aubrey, Naomi smirking, mouth closed.
            with dissolve

            u "(What... The fuck... Is wrong with this girl?)"

            scene v15s33_54e # FPP. MC looking at Aubrey, Aubrey looking at Naomi, Aubrey crying and angry, mouth open.
            with dissolve

            au "Naomi, shut your fake fucking mouth!"

            scene v15s33_53b # FPP. MC looking at Naomi, Naomi looking at Aubrey, Naomi shocked, mouth open.
            with dissolve

            na "But-"

            scene v15s33_54e
            with dissolve

            au "I have absolutely nothing to say to you. You're not the best person, and you're a pretty shit sister-"

            scene v15s33_53b
            with dissolve

            na "Uh, excuse me?!"

            scene v15s33_54e
            with dissolve

            au "But this? I can't believe you did this..."

            scene v15s33_54f # FPP. MC looking at Aubrey, Aubrey looking at MC, Aubrey crying and disappointed, mouth closed.
            with dissolve

            pause 

            scene v15s33_54g # FPP. Show Aubrey walking towards the bathroom door.
            with dissolve 

            pause 

            play sound "sounds/doorclose.mp3"

            scene v15s33_44c # TPP. Show Aubrey leaving the bathroom and slamming the door shut.
            with vpunch

            pause 

            scene v15s33_46e
            with dissolve

            u "Fuck!"

            scene v15s33_46d
            with dissolve

            na "Shit..."

            na "Well, I guess we got busted. Haha..."

            scene v15s33_46e
            with dissolve

            u "What the hell is wrong with you?"

            scene v15s33_46d
            with dissolve

            na "What's wrong with me?"

            scene v15s33_46e
            with dissolve

            u "Do you not care that she's upset?"

            scene v15s33_46g
            with dissolve

            na "Ah, don't worry. She'll be fine. Let her throw her usual little tantrum..."

            scene v15s33_46h
            with dissolve

            u "Seriously...?"

            scene v15s33_46g
            with dissolve

            na "We're sisters, [name]. She'll get over it."

            scene v15s33_46h
            with dissolve

            u "I highly doubt it."

            scene v15s33_46g
            with dissolve

            na "Give me your phone."

            scene v15s33_46h
            with dissolve

            u "Why?"

            scene v15s33_46h
            with dissolve

            na "Just give it to me. Why do you ask so many questions?"

            scene v15s33_46j
            with dissolve

            pause

            scene v15s33_47a
            with dissolve 

            pause

            scene v15s33_46g
            with dissolve

            na "Now you have my number, text me sometime soon. We have unfinished business to take care of."
            
            play sound "sounds/dooropen.mp3"

            scene v15s33_44d # TPP. Show Naomi opening the bathroom door.
            with dissolve 

            pause

            play sound "sounds/doorclose.mp3"

            scene v15s33_44e # FPP. Show Naomi leaving the bathroom.
            with dissolve 

            pause 

            scene v15s33_55 # FPP. MC looking at the empty bathroom.
            with dissolve 
            
            u "*Sighs* (This is such a fucking mess...)"

            u "(I hope she's not out there telling the entire party what just happened...)"

            u "(I'd better get back out there.) *Sighs*"

            scene v15s33_34a
            with fade (1,0,1)

            scene v15s33_41b # FPP. Aubrey gone, MC looking at the Empty seat Aubrey was at.
            with dissolve 

            u "(Where is she?)"

            scene v15s33_38f # FPP. Aubrey gone, MC looking across the table at the empty seat infront of him.
            with dissolve

            pause 

            scene v15s33_38d # FPP. Aubrey sitting down in her seat, Aubrey sad, mouth closed.
            with dissolve 

            pause

            scene v15s33_38e # FPP. Aubrey sat down in her seat, Aubrey looking down avoiding eye contact with anyone, Aubrey sad, mouth closed.
            with dissolve 

            u "(This is going to be fun...)"

            u "(I'll just leave her alone for now... Hopefully she'll calm down and I can talk to her later.)"

    if not aubrey_mad:
        scene v15s33_56 # TPP. MC and Aubrey sitting next to each other at the wedding ceremony, Naomi seated far away from them, Aubrey and MC slight smile, mouth closed.
        with fade (1,0,1)

        pause 

        scene v15s33_57 # FPP. Seated at the Ceremony, MC looking at Aubrey seated next to him, Aubrey looking at MC, Aubrey slight smile, mouth closed.
        with dissolve 

        u "It turned out really great."

        scene v15s33_57a # FPP. MC looking at Aubrey, Aubrey looking at MC, Aubrey slight smile, mouth closed.
        with dissolve

        au "Yeah, they look so happy... *Chuckles*"

        au "One day that will be me."

        scene v15s33_57
        with dissolve

        menu:
            "Hopefully.":
                $ add_point(KCT.TROUBLEMAKER)
                u "I mean, hopefully."

                scene v15s33_57a
                with dissolve

                au "Ha! You little shit..."

                scene v15s33_57
                with dissolve

                u "*Chuckles* I'm just saying! I mean, good luck."

                play sound "sounds/thud.mp3"

                scene v15s33_58 # TPP. Show Aubrey playfully punching MC's arm, slight smile, mouth closed.
                with dissolve

                pause 

            "It'll be us.":
                $ add_point(KCT.BOYFRIEND)
                u "One day it'll be us."

                if aubrey_friend:
                    scene v15s33_57a
                    with dissolve

                    au "We. Are. Just. Friends, [name]. *Giggles*"

                    scene v15s33_57
                    with dissolve

                    u "Yeah, yeah... Where did I go wrong?"

                    scene v15s33_57a
                    with dissolve

                    au "Oh jeez... Okay, here. How about if we're both still single when we're forty, then maybe you can propose."

                    scene v15s33_57
                    with dissolve

                    u "Haha, a pact?"

                    scene v15s33_57a
                    with dissolve

                    au "Sure, yeah."

                    scene v15s33_57
                    with dissolve

                    u "Okay, I can do that. I guess we all need someone to grow old with."

                    scene v15s33_57a
                    with dissolve

                    au "Ha, true."
                elif aubreyrs:
                    $ aubrey_tamed = True
                    
                    scene v15s33_57b # FPP. Aubrey looking at MC, MC looking at Aubrey, Aubrey looking at MC like she is in love, mouth closed.
                    with dissolve 

                    u "(That face... Irresistible.)"

                    scene v15s33_57a
                    with dissolve

                    au "You think so?"

                    scene v15s33_57
                    with dissolve

                    u "I know so."

                    scene v15s33_80 # TPP. Close up of Aubrey and MC's hands starting to hold each other.
                    with dissolve

                    pause 

                    scene v15s33_59 # TPP. Close up of just Aubrey looking at their hands, slight smile, mouth closed.
                    with dissolve 

                    pause
                    
                    scene v15s33_57c # FPP. MC looking at Aubrey, Aubrey looking at MC, Aubrey smirking, mouth open.
                    with dissolve 

                    au "Kiss me, you idiot."

                    scene v15s33_57d # FPP. MC looking at Aubrey, Aubrey looking at MC, Aubrey smirking, mouth closed.
                    with dissolve

                    u "*Laughs* Gladly."

                    scene v15s33_60 # TPP. At the ceremony in their seats, MC and Aubrey kissing each other romantically and holding each others hands.
                    with dissolve

                    pause

                    scene v15s33_61 # TPP. Close up of Aubrey's Mom and Dad looking in MC's and Aubrey's direction, both slight smile, mouth closed.
                    with dissolve 

                    pause

                    scene v15s33_62 # TPP. Close up of Naomi sat far away in her seat looking over in MC and Aubrey's direction, Naomi rolling her eyes, neutral face, mouth closed.
                    with dissolve 

                    pause 

                    scene v15s33_62a # TPP. Naomi smiling in their direction, mouth closed.
                    with dissolve 

                    if v15s33_cheese:
                        scene v15s33_63 # TPP. Close up of Aubrey's uncle, with one hand in the air and one hand on his beer as he looks at MC and Aubrey, slight smile, mouth open.
                        with dissolve 

                        rick "WOOOOH!"
                    else:
                        scene v15s33_63a # TPP. Close up of Aubrey's uncle no hands in the air looking in MC and Aubrey's direction slight smile, mouth closed.
                        with dissolve 
    else:
        scene v15s33_56a # TPP. MC and Naomi sitting next to each other at the wedding ceremony, Aubrey seated far away from them, MC neutral face, mouth closed, Naomi smirking, mouth closed.
        with dissolve 
        
        pause 

        scene v15s33_64 # FPP. MC looking at Aubrey as she is sat far away from him and Naomi, Aubrey sad looking at the ground, mouth closed.
        with dissolve 

        u "(She's really avoiding me, huh?)"

        scene v15s33_57e # FPP. MC sat next to Naomi, MC looking at Naomi, Naomi looking at MC, Naomi smirking, mouth open.
        with dissolve

        na "Getting married looks like it could be fun."

        scene v15s33_57f # FPP. MC sat next to Naomi, MC looking at Naomi, Naomi looking at MC, Naomi smirking, mouth closed.
        with dissolve

        menu:
            "Stay silent.":
                $ add_point(KCT.BRO)
                u "(I don't feel good about talking to her right now...) *Sighs*"

                scene v15s33_57e
                with dissolve

                na "I'll take that as a no. *Laughs*"
            "Agree.":
                $ add_point(KCT.BOYFRIEND)
                u "Yeah, it's supposed to be the best day of your life. Right?"

                scene v15s33_57e
                with dissolve

                na "I think so, yeah..."

                na "I've had a few offers already, ha! Turned them all down so far, of course. I'm way too young for marriage wrinkles..."

                scene v15s33_57f
                with dissolve

                u "(Marriage wrinkles...? Is that another supermodel term?)"

                scene v15s33_65 # TPP. Close up of Aubrey looking at MC and Naomi sitting next to each other at the wedding, Aubrey looks miserable and sad, mouth closed.
                with dissolve 

    scene v15s33_66 # TPP. Close up of the Wedding official standing between Aubrey's parents, Wedding official slight smile, mouth closed.
    with dissolve

    wedoff "Today is the most special and sacred day, as we celebrate the love held between two people whose bond grows stronger with each passing day..."

    scene v15s33_67 # TPP. Later in the day, Close up of Aubrey's Mom, looking at Aubrey's dad(off camera), Aubrey's mom tearing up, slight smile, mouth closed.
    with fade

    aumom "You are my best friend, you are my biggest hero, and my longest love."

    aumom "*Sniffles* Together, we built a beautiful home and created a terrific family..."

    if aubrey_mad: 
        scene v15s33_65a # TPP. Close up of Aubrey looking at her parents, Aubrey smirking but still sad, mouth closed.
        with dissolve 
    else:
        scene v15s33_58a # TPP. MC and Aubrey watching the ceremony and holding hands, Aubrey smiling, mouth closed.
        with dissolve 

    scene v15s33_68 # TPP. Close up of Aubrey's Dad, Aubrey's dad looking at Aubrey's mom, Aubrey's dad slight smile, mouth closed.
    with dissolve 

    audad "I affirm my commitment to you, my wonderful wife."

    audad "I promise to continue to love you in the good times and through all the bad, through the easy days and the rock hard..."

    u "(Ew, what?)"

    scene v15s33_63b # TPP. Close up of Aubrey's Uncle watching the ceremony and laughing.
    with dissolve

    pause  

    scene v15s33_69 # TPP. Close up of Aubrey's Mom and Aubrey's Dads hands. Aubrey's dad sliding a ring on to Aubrey's mom's finger.
    with fade (1,0,1)

    pause 

    scene v15s33_69a # TPP. Aubrey's Mom's hand now with a ring on her finger sliding a ring onto Aubrey's dad's finger.

    wedoff "You may now kiss the bride... Again."

    scene v15s33_70 # TPP. Show Aubrey's Mom and Dad kissing.
    with dissolve

    pause 

    scene v15s33_71 # TPP. A group of people smiling and clapping
    with dissolve

    pause 

    scene v15s33_72 # TPP. Shot of MC and Aubrey from behind approaching Aubrey's parents, both her parents slight smile, mouth closed.
    with dissolve 

    pause

    scene v15s33_73 # FPP. MC and Aubrey standing with her parents after the Ceremony, MC looking at Aubrey, Aubrey looking at her parents, Aubrey tiny smile, mouth open.
    with dissolve 

    au "Congratulations, you guys. That was so beautiful..."

    scene v15s33_74 # FPP. MC looking at both of Aubrey's parents, both slight smile, mouth closed.
    with dissolve

    u "Yeah, it really was."

    scene v15s33_81 # TPP. After the ceremony, Aubrey group hugging with her parents MC not in the hug.
    with dissolve

    pause

    scene v15s33_74a # FPP. MC looking at both of Aubrey's parents, both slight smile, Aubrey's dad's mouth open. Aubrey's mom mouth closed.
    with dissolve

    audad "Thank you, guys."

    scene v15s33_88 # FPP. After the ceremony MC and Aubrey with her parents, MC looking at Aubrey's mom, Aubrey's mom looking at Aubrey, slight smile, mouth open.
    with dissolve

    aumom "I'm amazed that your dad remembered all of his lines! *Giggles*"

    scene v15s33_76 # FPP. After the Ceremony MC and Aubrey standing with her parents, MC looking at Aubrey's dad, Aubrey's dad looking at Aubrey, slight smile, mouth open.
    with dissolve

    audad "I'm amazed too!"

    scene v15s33_73
    with dissolve

    au "Haha, you did great."

    scene v15s33_77 # TPP. Naomi standing off somewhere taking selfies on her phone after the ceremony, smirking, mouth closed.
    with dissolve

    aumom "Naomi. Come over here! Let's take a photo of all of us, please?"

    scene v15s33_73
    with dissolve

    au "Oh, that's a great idea."

    scene v15s33_76
    with dissolve

    audad "Here, use my phone."

    scene v15s33_78 # TPP. Aubrey's dad handing her his phone, Aubrey taking the phone, slight smile, mouth closed.
    with dissolve

    pause 

    scene v15s33_73a # FPP. MC looking at Aubrey, Aubrey looking at her dad, Aubrey slightly sad, mouth open.
    with dissolve

    au "Oh... I-"

    scene v15s33_79 # TPP. Show Naomi and Aubrey's parents posing and smiling for a photo.
    with dissolve

    pause

    scene v15s33_73a
    with dissolve 

    au "You want... Me to take the photo?"

    scene v15s33_76
    with dissolve

    audad "Yeah. Is the flash switched on?"

    scene v15s33_73a
    with dissolve

    au "Uh, yeah. Ready to go."

    scene v15s33_79
    with dissolve

    u "(Are you serious right now? They're taking a family photo without her...)"

    scene v15s33_79
    with dissolve

    menu:
        "Stay out of it.":
            $ add_point(KCT.BRO)
            
            u "(It's probably best if I don't get involved. *Sighs* That's so fucked.)"

            play sound "sounds/capture.mp3"

            scene v15s33_79
            with flash

            pause 

            scene v15s33_78a # TPP. Aubrey handing her dad back his phone, Aubrey sad, mouth closed.
            with dissolve 

            pause  

            scene v15s33_83 # TPP. Show Aubrey walking away from everyone after the photo, Aubrey sad, mouth closed.
            with dissolve 

        "Take the photo.":
            $ add_point(KCT.TROUBLEMAKER)
            $ v15s33_take_photo = True

            u "*Scoffs*"

            scene v15s33_73b # FPP. MC looking at Aubrey, Aubrey looking at MC, Aubrey small smile, mouth closed.
            with dissolve

            u "Aubrey, get in there."

            scene v15s33_73c # FPP. MC looking at Aubrey, Aubrey looking at MC, Aubrey small smile, mouth open.
            with dissolve

            au "Oh- Really?"

            scene v15s33_73b
            with dissolve

            u "Yeah, of course. It is a..."

            u "Family photo. Isn't it?"

            na "Right! Come on, sissy!"

            scene v15s33_81a # TPP. Aubrey and MC standing with her parents and Naomi after the ceremony, Aubrey handing MC her dad's phone.
            with dissolve

            if aubreytamed:
                pause

                scene v15s33_81b # TPP. Aubrey kissing MC's cheek.
                with dissolve 

            pause 

            scene v15s33_79a # TPP. Aubrey, her parents, and Naomi all standing and posing together smiling for a photo.
            with dissolve

            u "Give me a nice big, cheesy smile!"

            play sound "sounds/capture.mp3"

            scene v15s33_79a
            with flash

            pause

            scene v15s33_78a
            with dissolve 

            pause 

            scene v15s33_83
            with dissolve 

    scene v15s33_84 # TPP. MC sitting down next to Aubrey who is sitting on a bench overlooking the distant lake.
    with fade (1,0,1)

    pause 

    scene v15s33_75 # FPP. MC sitting down next to Aubrey on the bench, Aubrey looking at MC, MC looking at Aubrey, Aubrey upset, mouth closed.
    with dissolve 

    u "Hey... Are you okay?"

    if aubrey_mad:

        scene v15s33_75a # FPP. MC looking at Aubrey, Aubrey looking at MC, Aubrey upset, mouth open.
        with dissolve

        au "I'm still processing everything what happened today, [name]."

        scene v15s33_75
        with dissolve

        u "Yeah..."

        if aubreyrs:
            scene v15s33_75b # FPP. MC looking at Aubrey, Aubrey looking at MC, Aubrey angry, mouth open.
            with dissolve

            au "You're fucking disgusting. I'm questioning if I ever want to speak to you again."

            scene v15s33_75c # FPP. MC looking at Aubrey, Aubrey looking at MC, Aubrey angry, mouth closed.
            with dissolve

            u "That's completely fair, I just-"

        scene v15s33_75a
        with dissolve

        au "Can you just- Give me a few minutes? Please...?"

        scene v15s33_75
        with dissolve 

        menu:
            "Give her space.":
                $ add_point(KCT.BRO)
                u "I'm sorry. I'll go back inside. Just let me know if you want to talk, okay?"

                jump v15s34
            "Try to talk.":
                $ add_point(KCT.TROUBLEMAKER)
                scene v15s33_75
                with dissolve

                u "I'm so sorry for what I did, Aubrey. It's just that..."

                u "Your parents wanting a photo without you is, ugh..."

                scene v15s33_75b
                with dissolve

                au "I'm upset about a lot of things right now, [name]! I said leave me alone!"

                scene v15s33_86 # TPP. Aubrey walking away from the bench, Aubrey angry upset, Aubrey mouth closed, MC sitting on the bench neutral face, mouth closed.
                with dissolve 

                u "Fuck... I need to stop opening my mouth."

                jump v15s34
    else:
        scene v15s33_75a
        with dissolve

        au "They don't even see how much they hurt me when they do shit like that."

        scene v15s33_75
        with dissolve

        u "With the photo?"

        scene v15s33_75a
        with dissolve

        au "Yes."

        if aubrey_tamed:
            scene v15s33_87 # TPP. MC hugging Aubrey while they sit on the bench, Aubrey crying into his shoulder, MC slight frown, mouth closed.
            with dissolve
        elif aubrey_friend:
            scene v15s33_87a # TPP. MC rubbing Aubrey's back as she cries, MC slight frown, mouth closed.
            with dissolve 

        scene v15s33_75
        with dissolve

        u "That was the most awful thing I've ever seen them do to you."

        u "And you're right, ha. It's like they aren't even aware of their actions."

        if v15s33_take_photo:
            scene v15s33_75a
            with dissolve

            au "Thanks for stepping in like that."

            scene v15s33_75
            with dissolve

            u "I wasn't just going to stand by and let it happen."

            scene v15s33_75a
            with dissolve

            au "Well, thank you. It means a lot to me."

        scene v15s33_75
        with dissolve

        u "Remember what I said."

        u "I'll be here for you, complete with awful jokes. *Laughs*"

        scene v15s33_75a
        with dissolve

        au "Now would be a good time for one of those awful jokes..."

        scene v15s33_75
        with dissolve

        u "Okay, okay... Are you ready?"

        scene v15s33_75a
        with dissolve

        au "Hehe, yeah. Ready."

        scene v15s33_75d # FPP. MC looking at Aubrey, Aubrey looking at MC, Aubrey teary eyed, Aubrey slight smile, mouth closed
        with dissolve

        menu:
            "Science Joke.":
                $ add_point(KCT.BOYFRIEND)
                u "Did I tell you about the book I read on anti-gravity?"

                scene v15s33_75e # FPP. MC looking at Aubrey, Aubrey looking at MC, Aubrey teary eyed, Aubrey slight smile, mouth open.
                with dissolve

                au "No, you didn't."

                scene v15s33_75d
                with dissolve

                u "It was impossible to put down."

                scene v15s33_75f # FPP. MC looking at Aubrey, Aubrey looking at MC, Aubrey slight smile, rolling her eyes.
                with dissolve 
            "Monkey Joke.":
                $ add_point(KCT.BRO)
                scene v15s33_75e
                with dissolve

                u "Why did the monkey eat the banana?"

                scene v15s33_75d
                with dissolve

                au "I don't know... Why?"

                scene v15s33_75e
                with dissolve

                u "Well, because monkeys like bananas... Didn't you know that?"

        scene v15s33_75g # FPP. MC looking at Aubrey, Aubrey looking at MC, Aubrey slight smile, mouth open.
        with dissolve 

        au "Haha! That was awful, [name]."

        scene v15s33_75h # FPP. MC looking at Aubrey, Aubrey looking at MC, Aubrey slight smile, mouth closed.
        with dissolve

        u "*Laughs* I'm a man of my word."

        scene v15s33_75g
        with dissolve

        au "I'm happy you're here with me."

        if aubrey_friend:
            scene v15s33_75h
            with dissolve

            u "It's what friends are for."
        if aubrey tamed:
            scene v15s33_75h
            with dissolve

            u "I'm happy I'm with you."

            scene v15s33_89 # TPP. Shot from behind the bench. Looking at Aubrey resting her head on MC's shoulder, MC with his arm wrapped around Aubrey, They are looking out at the lake view.
            with dissolve 

        jump v15s34