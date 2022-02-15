# SCENE 14: Nora & Ms Rose yoga in park scene
# Locations: Park
# Characters: MC (Outfit: GYM), NORA (Outfit: GYM), MS. ROSE (Outfit: GYM), PENELOPE (Outfit: 2)
# Time: Afternoon


label v16s14:

# -MC gym outfit, Nora & Rose yoga outfits. Nora's wearing her fav color royal blue if possible (just bc she looks good af in it), i'm gonna assume we should take advantage of this situation and have them be barefoot, especially the girls (painted nails plz)-

    scene v16s14_1 # FPP. MC sees Nora in the distance, leaning on a tree in the park, Nora slight smile, looking at MC, waving at him, mouth closed, three yoga mats are on the ground, one of the mats is behind the other 2
    with dissolve

    pause  

    scene v16s14_2 #  TPP. Show MC walking over to Nora, both slight smiles, mouths closed
    with dissolve

    pause  

    scene v16s14_3 # FPP. MC standing in front of Nora, Nora slight smile, mouth closed
    with dissolve

    u "Hey, Nora."

    scene v16s14_3a # FPP. Same as v16s14_3, Nora slight smile, mouth open
    with dissolve

    no "Hey, [name]. Can you believe this weather? It's the perfect day for yoga."

    scene v16s14_3
    with dissolve

    u "Ha, yeah. It's refreshing."

    if norars: # TODO Variable

        scene v16s14_4 # TPP. SHow MC giving Nora a kiss, she is still leaning on the tree
        with dissolve

        pause  0.75

        scene v16s14_3a
        with dissolve

        no "Mm, that's the sort of hello a girl could get used to."

        no "You'll have to control yourself though. We're expecting company."
    
    elif norafriend: # TODO Variable

        u "Are we ready to start?"

        scene v16s14_3a
        with dissolve

        no "Almost. We just need to wait for our yoga instructor."

    scene v16s14_3
    with dissolve

    u "Oh... We have an instructor?"

    scene v16s14_3a
    with dissolve

    no "Haha, yes... And she should be here any min-"

    scene v16s14_3b # FPP. Nora looking to the side, smiling, mouth open
    with dissolve

    no "Ah! Here she comes now."

    scene v16s14_5 # FPP. MC turns and sees Ms. Rose approaching from a distance, Ms. Rose smiling, waving, mouth closed
    with dissolve

    pause 0.75

    if norars: # TODO Variable
        scene v16s14_5a # FPP. Same as v16s14_5, Ms. Rose closer, smiling, not waving anymore, still walking towards MC and Nora, mouths closed
        with dissolve

        u "(Seriously? There goes my alone time with Nora.)"
    
    elif norars and not msrosers: # TODO Variables
        scene v16s14_5a
        with dissolve

        u "Ms. Rose? (This could be interesting!)"

    scene v16s14_6 # FPP. Ms. Rose now standing next to MC and Nora, MC looking at Ms. Rose, Ms. Rose looking at Nora, Ms. Rose slight smile, mouth open
    with dissolve

    ro "Oh, Nora. You didn't say anything about [name] being here."

    scene v16s14_3b
    with dissolve

    no "I said a friend was coming."

    if not msrosers: # TODO Variable If never dated ms. rose, idk the variable
        scene v16s14_6a # FPP. Same as v16s14_6, Ms. Rose looking at MC, Ms. Rose smiling, mouth open
        with dissolve

        ro "Nice to see you, [name]."

        scene v16s14_6b # FPP. Same as v16s14_6a, Ms. Rose smiling, mouth closed
        with dissolve

        u "Ms. Rose, I didn't know you were a yoga guru."

        scene v16s14_6a
        with dissolve

        ro "I'm a woman of many talents."
    
    elif msrosers: # TODO Variable if still dating ms. rose
        scene v16s14_6b
        with dissolve

        u "(Act normal, act normal, act-)"

        scene v16s14_6a
        with dissolve

        ro "No worries, the more the merrier."

        scene v16s14_6c # FPP. Same as v16s14_6a, Ms. Rose mouth closed, giving a sexy wink to MC (don't make it super obvious, Nora can't notice the wink)
        with dissolve

        pause 0.75 

        scene v16s14_6a
        with dissolve

        ro "Now..."
    
    else: # if broke up with ms. rose
        scene v16s14_6d # FPP. Same as v16s14_6, Ms. Rose slightly stunned, mouth open
        with dissolve

        ro "Right, yes. You did. Sorry."

        scene v16s14_3c # FPP. Same as v16s14_3b, Nora slightly worried, mouth open
        with dissolve

        no "Are you feeling okay? You look a little pale."

        scene v16s14_6
        with dissolve

        ro "Oh, Nora... You sound like your father."

        scene v16s14_3d # FPP. Same as v16s14_3b, Nora rolling her eyes, mouth open
        with dissolve

        no "Ugh..."

        scene v16s14_6
        with dissolve

        ro "I'm fine, I promise. But..."

    scene v16s14_6
    with dissolve

    ro "I don't have a whole lot of time, as we've got a faculty meeting about this week's events."

    scene v16s14_6b
    with dissolve

    u "This week's events? What events?"

    scene v16s14_6a
    with dissolve

    ro "Sorry [name] but, yoga is about relaxing, and I can't relax when we discuss work."

    scene v16s14_3a
    with dissolve

    no "Yeah. No school, no work, no stress."

    scene v16s14_3
    with dissolve

    u "You're right, sorry guys."

    scene v16s14_6
    with dissolve

    ro "Let's begin?"

    scene v16s14_3b
    with dissolve

    no "Yes! Let's do it. Wait-"

    no "How do we start?"

    scene v16s14_6
    with dissolve

    ro "We'll keep it simple for today, you should be able to catch on quickly."

    scene v16s14_6a
    with dissolve

    ro "Just do what I do."

    scene v16s14_7 # TPP. Show the three of them walking towards their mats, all slight smiles, mouths closed (MC is walking towards the mat that is behind the other 2)
    with dissolve

    pause  

    scene v16s14_8 # TPP. Camera looking at Ms. Rose, Ms. Rose looking at Nora's direction, Ms. Rose smiling, mouth open
    with dissolve

    ro "Are we ready?"

    scene v16s14_9 # TPP. Camera looking at Nora, Nora looking at Ms. Rose's direction, Nora smiling, mouth open
    with dissolve

    no "Yeah."

    scene v16s14_10 # TPP. Wide shot that shows both Nora and Ms. Rose (full bodies), both smiling, mouths closed (MC is in the background, hide him behind Nora or something so we don't have to show his face)
    with dissolve

    u "Yep."

    scene v16s14_8a # TPP. Same as v16s14_8, Ms. Rose looking forward, smiling, mouth open
    with dissolve

    ro "Let's start with the cow and cat pose."

    scene v16s14_10a # TPP. Same as v16s14_10. Show Ms. Rose getting on her hands and knees, Nora and MC watching Ms. Rose getting on her hands and knees
    with dissolve

    pause 0.75

    scene v16s14_10b # TPP. Same as v16s14_10a, the three of them on their hands and knees, all smiling, Nora and MC mouths closed, Ms. Rose mouth open
    with dissolve

    ro "So from this neutral pose, push your stomach down and your chin up to form the cow pose."

    scene v16s14_10c # TPP. Same as v16s14_10b, Ms. Rose doing the "cow and cat pose", MC and Nora watching her do the pose (both on their hands and knees)
    with dissolve

    pause 0.75

    scene v16s14_10d # TPP. Same as v16s14_10c, all three of them doing the "cow and cat pose"
    with dissolve

    pause  0.75

    scene v16s14_11 # FPP. MC on his hands and knees, he looks forward, seeing both Nora and Ms. Rose with their asses sticking out from doing the pose
    with dissolve

    u "(Holyyyyy... We've got the best seat in the house!)"

    menu:
        "Stare at Nora":
            scene v16s14_12 # FPP. MC focusing only on Nora's ass while she does the cow pose
            with dissolve

            ro "Now take a deep breath in... and"

            ro "Hold it..."

            scene v16s14_12a # FPP. Same as v16s14_12, Nora curving her back into a catlike pose
            with dissolve

            ro "And on the exhale, curve your back to go into a cat-like pose."

            u "(Ooh... I feel something burning. Is that good?)"

            scene v16s14_12b # FPP. Same as v16s14_12, more neutral position, Nora inhaling before going into the cat or cow pose
            with dissolve

            ro "Now inhale... And hold."

            scene v16s14_12a
            with dissolve

            ro "Now when we release, we form into our cow pose again."

            ro "And repeat."

            scene v16s14_12
            with dissolve

            no "I'm really... *Grunts* Feeling this."

            ro "Does it feel okay?"

            scene v16s14_12b
            with dissolve

            pause 0.75

            scene v16s14_12a
            with dissolve

            no "Yeah. Just tight."

            no "How's it going back there, [name]?"

            scene v16s14_12b
            with dissolve

            u "Fantastic, thanks."

            pause 0.75

            scene v16s14_12
            with dissolve

            pause 0.75

        "Stare at Ms. Rose":
            scene v16s14_13 # FPP. MC focusing only on Ms. Rose's ass while she does the cow pose
            with dissolve

            ro "Now take a deep breath in... and"

            ro "Hold it..."

            scene v16s14_13a # FPP. Same as v16s14_13, Ms. Rose curving her back into a catlike pose
            with dissolve

            ro "And on the exhale, curve your back to go into a cat-like pose."

            u "(Ooh... I feel something burning. Is that good?)"

            scene v16s14_13b # FPP. Same as v16s14_13, more neutral position, Ms. Rose inhaling before going into the cat or cow pose
            with dissolve

            ro "Now inhale... And hold."

            scene v16s14_13a
            with dissolve

            ro "Now when we release, we form into our cow pose again."

            ro "And repeat."

            scene v16s14_13
            with dissolve

            no "I'm really... *Grunts* Feeling this."

            ro "Does it feel okay?"

            scene v16s14_13b
            with dissolve

            pause 0.75

            scene v16s14_13a
            with dissolve

            no "Yeah. Just tight."

            no "How's it going back there, [name]?"

            scene v16s14_13b
            with dissolve

            u "Fantastic, thanks."

            pause 0.75

            scene v16s14_13
            with dissolve

            pause 0.75
            
        "Stay focused":
            scene v16s14_10e # TPP. Same as v16s14_10d, all doing the cow pose
            with dissolve

            ro "Now take a deep breath in... and"

            ro "Hold it..."

            scene v16s14_10f # TPP. Same as v16s14_10e, all curving their backs into a catlike pose
            with dissolve

            ro "And on the exhale, curve your back to go into a cat-like pose."

            u "(Ooh... I feel something burning. Is that good?)"

            scene v16s14_10g # TPP. # FPP. Same as v16s14_10e, more neutral position, they're inhaling before going into the cat or cow pose
            with dissolve

            ro "Now inhale... And hold."

            scene v16s14_10f
            with dissolve

            ro "Now when we release, we form into our cow pose again."

            ro "And repeat."

            scene v16s14_10e
            with dissolve

            no "I'm really... *Grunts* Feeling this."

            ro "Does it feel okay?"

            scene v16s14_10g
            with dissolve

            pause 0.75

            scene v16s14_10f
            with dissolve

            no "Yeah. Just tight."

            no "How's it going back there, [name]?"

            scene v16s14_10g
            with dissolve

            u "Fantastic, thanks."

            pause 0.75

            scene v16s14_10e
            with dissolve

            pause 0.75

    scene v16s14_10b
    with dissolve

    ro "Now..."

    scene v16s14_10h # TPP. Same as v16s14_10b, Nora stretching her right leg behind her, Rose mouth open, smiling, rest only on hands and knees
    with dissolve

    ro "Stretch your right leg straight out behind you. *Moans*"

    u "(Are these noises necessary?)"

    scene v16s14_10i # TPP. Same as v16s14_10h, Nora lifting her leg up, align it with her spine, Rose mouth open, smiling
    with dissolve

    ro "Lift it up, into the air..."

    ro "So, it's in line with your spine, and then we're going to hold it there."

    scene v16s14_10j # TPP. Same as v16s14_10i, all three doing the pose, MC mouth open, rest mouth closed, slightly struggling
    with dissolve

    u "Mnngh... What's this one called?"

    scene v16s14_10k # TPP. Same as v16s14_10j, Ms. Rose mouth open, rest mouth closed, slightly struggling
    with dissolve

    ro "Umm... I don't remember. Leg pose, something... Stretch?"

    scene v16s14_10l # TPP. Same as v16s14_10j, Nora mouth open, rest mouth closed, slightly struggling
    with dissolve

    no "*Chuckles* Leg pose stretch?"

    scene v16s14_10j
    with dissolve

    u "Are you sure it's not, \"the flamingo burn\"?"

    scene v16s14_10k
    with dissolve

    ro "Haha..."

    scene v16s14_10l
    with dissolve

    no "That's the one. *Grunts*"

    scene v16s14_10k
    with dissolve

    ro "And now we're going to do the same for your left leg."

    scene v16s14_10m # TPP. Same as v16s14_10j, ligting the left leg instead of the right leg, all mouths closed
    with dissolve

    pause 0.75

    scene v16s14_10b
    with dissolve

    ro "Okay. Now it's time for downward-facing dog."

    scene v16s14_10n # TPP. Same as v16s14_10b, Ms. Rose and MC mouths closed, Nora mouth open
    with dissolve

    no "Oh, I've heard of this one."

    scene v16s14_11a # FPP. Same as v16s14_11, MC watching at girls' asses as they are doing the downard-facing dog
    with dissolve

    u "(Come on, [name]... Try to keep a straight face.)"

    menu:
        "Stare at Nora":
            scene v16s14_12c # FPP. Same as v16s14_12, now they are doing the downward-facing dog pose. Nora is lifting her hips up, as to make a triangle shape with her body
            with dissolve

            ro "Lift your hips up, so you're making a triangle shape"

            ro "You can bend your knees if it helps... *Moans* Feel the stretch."

            scene v16s14_14 # TPP. Close up of Nora (show more of her chest and face here) doing the pose, she's struggling, sweaty, mouth slightly open
            with dissolve

            no "Oh, fuck..."

            scene v16s14_12c
            with dissolve

            u "(Is this what people mean when they say \"hot yoga\"?)"

            scene v16s14_15 # TPP. Close up of Nora (show more of her ass) doing the pose, she's struggling, sweaty, mouth closed
            with dissolve

            ro "Press your chest towards your legs, as far as possible without hurting yourself."

            ro "Hold it for a moment longer."

            scene v16s14_14
            with dissolve

            no "*Grunts*"

            scene v16s14_12c
            with dissolve

            ro "Now..."

            ro "Without standing up, just walk yourself to the top of your mat. Stay bent over."

            scene v16s14_15
            with dissolve

            ro "You can bend your knees a little, and feel free to sway side to side, whatever feels good."

            u "(Yeah, whatever... Feels... Good...)"

        "Stare at Ms. Rose":
            scene v16s14_13c # FPP. Same as v16s14_12, now they are doing the downward-facing dog pose. Ms. Rose is lifting her hips up, as to make a triangle shape with her body
            with dissolve

            ro "Lift your hips up, so you're making a triangle shape"

            ro "You can bend your knees if it helps... *Moans* Feel the stretch."

            scene v16s14_16 # TPP. Close up of Ms. Rose (show more of her chest and face here) doing the pose, she's slightly smiling, sweaty, mouth closed
            with dissolve

            no "Oh, fuck..."

            scene v16s14_13c
            with dissolve

            u "(Is this what people mean when they say \"hot yoga\"?)"

            scene v16s14_17 # TPP. Close up of Ms. Rose (show more of her ass) doing the pose, she's slightly smiling, sweaty, mouth open
            with dissolve

            ro "Press your chest towards your legs, as far as possible without hurting yourself."

            ro "Hold it for a moment longer."

            scene v16s14_16
            with dissolve

            no "*Grunts*"

            scene v16s14_13c
            with dissolve

            ro "Now..."

            ro "Without standing up, just walk yourself to the top of your mat. Stay bent over."

            scene v16s14_17
            with dissolve

            ro "You can bend your knees a little, and feel free to sway side to side, whatever feels good."

            scene v16s14_16
            with dissolve

            u "(Yeah, whatever... Feels... Good...)"

        "Stay focused":
            scene v16s14_10o # TPP. Same as v16s14_10n, Ms. Rose doing the pose, Ms. Rose mouth open
            with dissolve

            ro "Lift your hips up, so you're making a triangle shape"

            ro "You can bend your knees if it helps... *Moans* Feel the stretch."

            scene v16s14_10p # TPP. Same as v16s14_10o, Ms. Rose and Nora doing the pose, MC watching, Nora mouth slightly open
            with dissolve

            no "Oh, fuck..."

            u "(Is this what people mean when they say \"hot yoga\"?)"

            scene v16s14_10q # TPP. Same as v16s14_10p, all three doing the pose now, Ms. Rose mouth open
            with dissolve

            ro "Press your chest towards your legs, as far as possible without hurting yourself."

            ro "Hold it for a moment longer."

            scene v16s14_18 # TPP. Show all three doing the pose (focus more on Nora here), all mouths closed, Ms. Rose slight smile, MC and Nora slightly struggling
            with dissolve

            no "*Grunts*"

            scene v16s14_19 # TPP. Show all three doing the pose (focus more on Ms. Rose here), Ms. Rose mouth open, MC and Nora mouths closed, Ms. Rose slight smile, MC and Nora slightly struggling
            with dissolve

            ro "Now..."

            ro "Without standing up, just walk yourself to the top of your mat. Stay bent over."

            scene v16s14_10q
            with dissolve

            ro "You can bend your knees a little, and feel free to sway side to side, whatever feels good."

            scene v16s14_18
            with dissolve

            u "(This is more painful than I thought it was going to be... I might be sore tomorrow, haha.)"

    scene v16s14_10r # TPP. Same as v16s14_10q, all three of them pushing their stomachs in, Ms. Rose mouth open
    with dissolve

    ro "And now push your stomach in, and slowly unroll your spine until you're standing straight."

    scene v16s14_10s # TPP. Same as v16s14_10r, all three of them unrolling their spine, all mouths closed
    with dissolve

    no "*Exhales*"

    scene v16s14_10t # TPP. Same as v16s14_10s, all three standing straight, holding their hands up, stretching, Ms. Rose mouth open, rest mouths closed
    with dissolve

    ro "Then reach up with both hands and hold it there for our final stretch."

    scene v16s14_10u # TPP. Same as v16s14_10t, all three standing straight, holding their hands up, stretching, MC mouth opem, rest mouths closed
    with dissolve

    u "Ahh... Wow. I feel like jelly. *Laughs*"

    scene v16s14_99: # TPP. Ms. Rose and Nora standing next to each other, Nora drinking some water, Ms. Rose stretching, they're both sweaty, make this shot look very sexy please (RENDER THIS IMAGE IN 1920x5000 pixels, since it will be a panning image, similar to the Chloe one after homecoming. DM Peace/Mozzart if you have any questions about this)
        subpixel True
        yalign 1.0
        linear 6.0 yalign 0.0
    with fade

    scene v16s14_20 # FPP. MC, Nora and Ms. Rose standing on their mats, facing each other, MC looking at Ms. Rose, Ms. Rose looking at Nora, Ms. Rose smiling, mouth open
    with dissolve

    ro "So, did you guys enjoy your session today?"

    scene v16s14_21 # FPP. Same positioning as v16s14_20, MC looking at Nora, Nora looking at Ms. Rose, Nora smiling, mouth open
    with dissolve

    no "I loved it! Especially out here in the wind and the sun... It feels amazing."

    scene v16s14_20
    with dissolve

    ro "Good, honey. I'm glad."

    scene v16s14_21a # FPP. Same as v16s14_21, Nora looking at MC, smiling, mouth open
    with dissolve

    no "What did you think, [name]?"

    scene v16s14_22 # FPP. Show both Nora and Ms. Rose looking at MC, both slightly smiling, sweaty, slightly sexy poses, mouths closed
    with dissolve

    menu:
        "It was relaxing":
            
            u "Yeah, it was relaxing to be honest. I feel rejuvenated."

            scene v16s14_21b # FPP. Same as v16s14_21a, Nora smiling, mouth closed
            with dissolve

            u "It's like I'm a whole new man!"

            scene v16s14_21a
            with dissolve

            no "You still have the same forehead... Or... I mean- Fivehead, sorry."

            scene v16s14_21b
            with dissolve

            u "Who started this joke? What's wrong with my forehead? You have seen Cameron's forehead, right?"

            scene v16s14_21c # FPP. Same as v16s14_21b, Nora gigging
            with dissolve

            no "*Giggles*"

            scene v16s14_20a # FPP. Same as v16s14_20, Ms. Rose looking at MC, Ms. Rose smiling, mouth open
            with dissolve

            ro "*Sighs* Careful, [name]. Getting fired up is exactly what she wants."

            scene v16s14_21d # FPP. Same as v16s14_21b, Nora looking mischievously at MC and smirking
            with dissolve

            pause 0.75 

        "It was painful":

            u "Um... I mean, it was kind of painful...?"

            scene v16s14_20b # FPP. Same as v16s14_20a, Ms. Rose hiding a laugh with her hand, mouth closed
            with dissolve

            u "Unless pulled muscles are supposed to be the main benefit of yoga..."

            u "I think I just prefer a more traditional workout."

            scene v16s14_21a
            with dissolve

            no "Traditional? What's more traditional than using your breathing and your body to work out your muscles?"

            scene v16s14_21b
            with dissolve

            u "I don't know, weightlifting?"

            scene v16s14_21a
            with dissolve

            no "*Sighs* Ignorant frat boys..."

            scene v16s14_20
            with dissolve

            ro "Nora."

            scene v16s14_21a
            with dissolve

            no "Sorry. Not ignorant. Still a frat boy though."

            scene v16s14_21b
            with dissolve

            u "Ha."

    scene v16s14_20
    with dissolve

    ro "Well, I still have a little bit of time left... Did you want to go talk about things, Nora? Coffee and cake?"

    scene v16s14_21
    with dissolve

    no "Uh, yeah. Sure. But honestly, not for long, okay? I'm ready to relax and just forget about things with Chris."

    scene v16s14_20
    with dissolve

    ro "Right. Of course."

    scene v16s14_23 # TPP. Show MC reaching into his pocket, slight smile, mouth open
    with vpunch

    u "Oh, excuse me for a minute."

    scene v16s14_24 # TPP. MC turning his back to the girls (don't show them in background), MC slight smile, putting his phone to his ear, mouth closed
    with dissolve

    pause 0.75

    scene v16s14_25 # TPP. MC mouth closed, slight smile // Penelope at the pier, slightly annoyed, mouth open
    with dissolve

    pe "Hey, I need you to come to the pier. Like right now."

    scene v16s14_25a # TPP. Same as v16s14_25, MC mouth open, slightly confused // Penelope slightly annoyed, mouth closed
    with dissolve

    u "The pier? Why are you at the pier?"

    scene v16s14_25b # TPP. Same as v16s14_25a, MC mouth closed, slightly confused // Penelope slightly annoyed, mouth open
    with dissolve

    pe "I don't know how it happened, but... I'm stuck being the third wheel on a date and I could use a partner."

    scene v16s14_25a
    with dissolve

    u "Um, okay? Whose date?"

    scene v16s14_25b
    with dissolve

    pe "Imre and Karen. He won that thing from the Deer's event where he got a free date."

    scene v16s14_25a
    with dissolve

    u "But why are you at the pier with them anyway?"

    scene v16s14_25b
    with dissolve

    pe "Not with them, I was just here and Imre basically cuffed me to his wrist when he saw me."

    scene v16s14_25c # TPP. Same as v16s14_25b, MC mouth closed, slight smile // Penelope slight smile, mouth open
    with dissolve

    pe "Please just come save me? You can ask as many questions as you want once you're here. *Giggles*"

    scene v16s14_25d # TPP. Same as v16s14_25c, MC mouth open, slight smile // Penelope slight smile, mouth closed
    with dissolve

    u "Okay, I just need to go get changed, and I'll meet you there."

    scene v16s14_25c
    with dissolve

    pe "Ugh, I seriously love you. Thank you! I'll meet you by the entrance."

    scene v16s14_25d
    with dissolve

    u "Sounds good."

    scene v16s14_26 # TPP. Show MC putting his phone away and turning back to face the girls, all smiling, mouths closed
    with dissolve

    pause 0.75  

    scene v16s14_21b
    with dissolve

    u "Well, another friend in need. I should go."

    scene v16s14_21a
    with dissolve

    no "You're always saving someone, haha. We're going to grab coffee so, I'll catch up with you later?"

    scene v16s14_21b
    with dissolve

    u "Absolutely, you will. Thanks for inviting me to my first ever yoga session."

    scene v16s14_21a
    with dissolve

    no "Haha, no problem! It was nice spending time with you."

    scene v16s14_20d # FPP. Same as v16s14_20a, Ms. Rose smiling, mouth closed
    with dissolve

    u "And thank you, Lorraine, for being our instructor."

    scene v16s14_20c # FPP. Same as v16s14_20a, Ms. Rose smiling, mouth open
    with dissolve

    ro "Of course, thanks for joining us."

    if msrosers or neverwasrosers: # TODO Variable
        scene v16s14_20c
        with dissolve

        ro "Enjoy the rest of your day."

        scene v16s14_20a
        with dissolve

        u "Thanks, you too."

    scene v16s14_22
    with dissolve

    u "Bye guys!"

    scene v16s14_21a
    with dissolve

    no "See ya, [name]!"

    scene v16s14_27 # TPP. MC walking away, smiling, Nora and Ms. Rose watching him go, Nora smiling, Ms. Rose neutral expression. Ms. Rose is giving MC a small wave, all mouths closed
    with dissolve

    pause 0.75

    jump v16s15