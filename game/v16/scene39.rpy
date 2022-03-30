# SCENE 39: Aubrey Date
# Locations: MC Aubrey Date Night Restauraunt
# Characters: WAITER (Outfit: 1), AUBREY (Outfit: DATE NIGHT OUTFIT), MC (Outfit: DATE NIGHT OUTFIT)
# Time: Evening

label v16s39:
    scene v16s39_1 # TPP. Aubrey removes her jacket and hands it to the waiter, MC and Aubrey slight smiles, mouths are closed, looking at the waiter, The waiter has a creepy smile, mouth is closed taking Aubrey's jacket from her, the background includes a "coat room," and possibly a sign included to that effect
    with dissolve

    pause 0.75

    scene v16s39_1a # TPP. The waiter heads into the "coat room" his back is turned towards the camera, MC and Aubrey look at each slight smiles, mouths are closed
    with dissolve

    pause 0.75

    scene v16s39_2 # TPP. The waiter exits the coat room and with an arm extended outwards leads MC and Aubrey to their table, Mc and Aubrey slight smiles mouths are closed walking behind the waiter, The waiter still has a creepy smile, mouth is open, looking back at MC and Aubrey
    with dissolve

    pause 0.75

    scene v16s39_3 # TPP. The waiter is standing at a table using an extended arm to show Mc and Aubrey that is their table creepy smile mouth is open, Mc pulls out Aubreys chair for her and Aubrey sit's down, Mc has a slight smile mouth is closed looking at Aubrey, Aubrey is slightly blushing looking up at MC slight smile, mouth is closed as she is sitting down
    with dissolve

    pause 0.75

    scene v16s39_4 # FPP. Show just the waiter standing at the table, creepy smile, mouth is open, looking at MC, the camera angle is from a seated position, holding an order pad
    with dissolve

    waiter "Good evening, my name is Sergio."

    waiter "Can I start you off with something to drink this evening?"

    scene v16s39_5 # FPP. Show just Aubrey sitting down in her chair at the table, slight smile, mouth is open, looking at the waiter
    with dissolve

    au "I'll just have a soda."

    scene v16s39_4a # FPP. Show just the waiter standing at the table, creepy smile, mouth is open, looking at Aubrey, the camera angle is from a seated position, holding an order pad
    with dissolve

    waiter "Something fruity? We have our own menu of signature sodas made in-house."

    scene v16s39_5
    with dissolve

    au "Sure, surprise me."

    scene v16s39_4b # FPP. Show just the waiter standing at the table, creepy smile, mouth is closed, looking at MC, the camera angle is from a seated position, holding an order pad
    with dissolve

    menu:
        "Have the same": #(ONE POINT)
            $ v16_aubrey_date_points += 1
            $ add_point(KCT.BOYFRIEND)

            scene v16s39_4b
            with dissolve

            u "That sounds good. I'll have the mystery soda too."

            scene v16s39_5a # FPP. Show just Aubrey sitting down in her chair at the table, slight smile, mouth is open, looking at MC
            with dissolve

            au "Looks like we're both taking a walk on the wild side tonight."

        "Order a beer":
            $ add_point(KCT.BRO)

            scene v16s39_4b
            with dissolve

            u "Um... A beer?"

            scene v16s39_4
            with dissolve

            waiter "Certainly. I'll just need to have a peek at your ID."

            scene v16s39_4b
            with dissolve

            u "A peek at my ID? Um..."

            scene v16s39_6 # TPP. Show MC sitting at the table, looking down with a hand in his pocket, checking his pocket, He DOESN'T have anything im his hand, no expression, mouth is closed, Aubrey is also sitting at the table, slight smile, mouth is closed, looking at MC, the waiter is standing in behind the table looking at MC, with a creepy smile, mouth is closed, holding an order pad
            with dissolve

            pause 0.75

            scene v16s39_4b
            with dissolve

            u "Oh. I must've left it in my other pants."

            scene v16s39_4c # FPP. Show just the waiter standing at the table, creepy half smile, mouth is open, looking at MC, the camera angle is from a seated position, holding an order pad
            with dissolve

            waiter "*Chuckles* Nice try."

            scene v16s39_4
            with dissolve

            waiter "A fruity soda?"

            scene v16s39_6a # TPP. Show MC sitting at the table, dissapointed expression, mouth is closed, looking at the waiter, Aubrey is also sitting at the table, slight smile, mouth is open, with a hand over her mouth to cover her from laughing, looking at MC, the waiter is standing in behind the table looking at MC, with a creepy smile, mouth is closed, holding an order pad
            with dissolve

            pause 1.5

            scene v16s39_4b
            with dissolve

            u "..."
            u "Yeah, okay then. A fruity soda."
            
            if v15s24_nancy_dick: 
                u "(It's probably for the best, I don't want to hear the name Nancy Dick ever again...)"
            elif v15_lindsey_gamenight:
                u "(It's probably for the best, I don't want to hear the name Andrew King ever again...)"

# -Regardless-
    scene v16s39_4
    with dissolve

    waiter "I'll be right back with your drinks."

    scene v16s39_4d # FPP. The waiter has walked a slight distance away from the table, back is turned towards the camera, his face is not visible
    with dissolve

    pause 0.75

    scene v16s39_5b # FPP. Show just Aubrey sitting down in her chair at the table, slight smile, mouth is closed, looking at MC
    with dissolve

    u "So the cab ride was okay?"

    scene v16s39_5a
    with dissolve

    au "Yeah, apart from the driver blasting his crappy music."

    au "He had it so loud! I tried yelling at him to turn it off but there was so way he could hear me."

    au "If the journey was any longer, I would've jumped out, haha."

    scene v16s39_5b
    with dissolve

    u "*Laughs* Sorry you had to suffer that."

    scene v16s39_4e # FPP. The waiter is the same distance from the table as in render v16s39_4d, facing the camera, looking at MC, carrying a tray with two "fruity soda's" on it, slightly creepy smile, mouth is closed
    with dissolve

    pause 0.75

    scene v16s39_4f # FPP. Show just the waiter standing at the table, handing out the two "fruity soda's", slightly creepy smile, mouth is open, looking at MC, the camera angle is from a seated position
    with dissolve

    waiter "Here we are. Two fruity sodas."

    scene v16s39_4g # FPP. Show just the waiter standing at the table, now holding an empty tray, slightly creepy smile, mouth is closed, looking at MC, the camera angle is from a seated position
    with dissolve

    u "Thanks."

    scene v16s39_5c # FPP. Show just Aubrey sitting down in her chair at the table, Aubrey sips her drink, slight smile, eyes are closed
    with dissolve

    pause 0.75

    scene v16s39_5d # FPP. Show just Aubrey sitting down in her chair at the table, Aubrey is holding her drink, slight smile, mouth is open, looking at the waiter
    with dissolve

    au "Oh, it's really flavorful!"

    scene v16s39_4h # FPP. Show just the waiter standing at the table, now holding an empty tray, slightly creepy smile, mouth is open, looking at Aubrey, the camera angle is from a seated position
    with dissolve

    waiter "It's made with our own special blend of summer fruits. It's one of our most popular beverages."

    scene v16s39_5d
    with dissolve

    au "Well, my compliments to the chef!"

    scene v16s39_4h
    with dissolve

    waiter "Oh, the chef doesn't make this. All of our drinks are prepared by our resident soda artist. He's truly a master of his craft."

    scene v16s39_4g
    with dissolve

    u "That's weird... I've never heard of a soda artist before."

    scene v16s39_4i # FPP. Show just the waiter standing at the table, now holding an empty tray, slightly creepy smile, mouth is open, looking at MC, the camera angle is from a seated position
    with dissolve

    waiter "Then you have not lived until now, my friend."

    waiter "I'll now give you some time to peruse the menu."

    scene v16s39_4g
    with dissolve

    u "(Peruse? Someone likes reading their thesaurus...)"

    scene v16s39_4j # FPP. The waiter has walked a slight distance away from the table, back is turned towards the camera, his face is not visible, carrying an empty tray
    with dissolve

    pause 0.75

    # scene v16s39_7 # TPP. We now enter a free roam screen from MC's POV. The player can click on Aubrey, Wall clock, MC (bottom of screen highlighted), and a food Menu. Clicking on the Menu will give the option to end the free roam-
    # with dissolve

    # pause 0.75

    # TODO: FREE ROAM GOES HERE 
    # 
    call screen v16s39_fr_screen1

    label v16s39_fr_aubrey_date_aubrey: # -if Aubrey
        $ freeroam17.add("aubrey")

        scene v16s39_5b
        with dissolve

        menu:
            "Compliment her": # ONE POINT 
                $ v16_aubrey_date_points += 1
                $ add_point(KCT.BOYFRIEND)

                scene v16s39_5b
                with dissolve

                u "I know you're feeling overdressed, but seriously, I think you look stunning tonight."

                u "And your necklace is beautiful."

                scene v16s39_5a
                with dissolve

                au "Oh! Thank you... This was a gift from my grandma."

                scene v16s39_5b
                with dissolve

                u "Oh, that's sweet."

                scene v16s39_5e # FPP. Show just Aubrey sitting down in her chair at the table, slight smirk, mouth is open, looking at MC
                with dissolve

                au "A gift to Naomi of course. *Scoffs* But she said they were, and I quote, \"ugly and dusty pearls\"."

                scene v16s39_5b
                with dissolve

                u "Sounds like Naomi... Ha."

                scene v16s39_5a
                with dissolve

                au "Yeah, but I love them. I thought for a minute I looked like a supermodel, but now I'm just thinking that I overdid it slightly..."

                scene v16s39_5b
                with dissolve

                u "Hey, I didn't realize this place was fancy enough to have its own master soda artist. If anything, I'm underdressed, haha."

                scene v16s39_5a
                with dissolve

                au "Aww, you're just trying to make me feel better."

                scene v16s39_5b
                with dissolve

                u "Not at all. I don't even need to look around the room to know I'm with the most stunning girl here."

                scene v16s39_5a
                with dissolve

                au "Haha, yeah. You're lucky, huh."

                scene v16s39_5b
                with dissolve

                u "I am and I know it."
            
                u "Besides, whatever dress you wear, it'll always look better on my bedroom floor. No matter what."

                scene v16s39_5f # FPP. Show just Aubrey sitting down in her chair at the table, full smile, mouth is open, looking at MC
                with dissolve

                au "*Laughs* Oh, my God. So smooth!"

                scene v16s39_5b
                with dissolve

                u "*Laughs*"

            "Compliment the restaurant":
                $ add_point(KCT.BOYFRIEND)
                $ add_point(KCT.BRO)

                scene v16s39_5b
                with dissolve

                u "How are you liking the restaurant? I think I chose well."

                scene v16s39_5a
                with dissolve

                au "Yeah, it looks like a good choice. The sodas are good, but I'll reserve judgment until I eat the food."

                scene v16s39_5b
                with dissolve

                u "Ooh, \"reserving judgment?\" Am I on a date with an undercover restaurant critic?"

                scene v16s39_5a
                with dissolve

                au "Haha, if I were a restaurant critic, I wouldn't be undercover. I'd want them to roll out the red carpet for me, I think."

                au "To be honest, I was kind of hoping we were going to the new seafood place."

                scene v16s39_5b
                with dissolve

                u "There's a seafood place?"

                scene v16s39_5a
                with dissolve

                au "Yeah, I was checking out their site earlier today. Ugh, I love seafood."

                scene v16s39_5b
                with dissolve

                u "*Laughs* (Well, shit. Next is seafood I suppose.)"

                scene v16s39_5a
                with dissolve

                au "The owners are fishermen too, so after catching the fish they serve it that day in the restaurant, super fresh."

                scene v16s39_5b
                with dissolve

                u "That does sound amazing... Wanna ditch this place and go there?"

                scene v16s39_5a
                with dissolve

                au "Haha, stop it, of course not. Italian food is great. I've just really wanted to check out that other place, you know?"

        call screen v16s39_fr_screen1 # -Return to free roam screen-

    label v16s39_fr_aubrey_date_clock: # -if Wall clock
        $ freeroam17.add("clock")

        scene v16s39_8 # FPP. Close up shot of the wall clock from the free roam, Show it on 9:45 PM
        with dissolve

        menu:
            "Complain about wait":
                $ add_point(KCT.TROUBLEMAKER)
                $ add_point(KCT.BRO)

                scene v16s39_5b
                with dissolve

                u "The waiter's a bit slow, isn't he?"

                u "I could've made those drinks quicker myself."

                scene v16s39_5a
                with dissolve

                au "What are you talking about? I think he's doing fine. Besides, I doubt you have what it takes to be a master soda artist, haha."

                scene v16s39_5b
                with dissolve

                u "Yeah, well, I'm keeping an eye on how long he's taking."

                scene v16s39_5a
                with dissolve

                au "Haha, are you sure you're not a secret restaurant critic?"

                scene v16s39_5b
                with dissolve

                u "Haha, well if I was, this place would be in trouble."

                scene v16s39_5a
                with dissolve

                au "I think someone is getting hangry."

            "Plenty of time left": # (ONE POINT)
                $ v16_aubrey_date_points += 1
                $ add_point(KCT.BOYFRIEND)
                $ add_point(KCT.BRO)

                scene v16s39_5a
                with dissolve

                au "Are you checking the time already?"

                scene v16s39_5b
                with dissolve

                u "I was just pleasantly surprised that it's not as late as I thought it was."

                u "The more time I get to spend with you the better, as far as I'm concerned."

                scene v16s39_5g # FPP. Show just Aubrey sitting down in her chair at the table, full smile, mouth is closed, looking at MC
                with dissolve

                pause 0.75

                scene v16s39_5a
                with dissolve

                au "Aw, now don't get too romantic on me, [name]."

                scene v16s39_5b
                with dissolve

                u "Haha, well, okay... I was also thinking about all the time we'd have for sex later, too."

                scene v16s39_5a
                with dissolve

                au "Haha, that's more like it."

        call screen v16s39_fr_screen1 # -Return to free roam screen-

    label v16s39_fr_aubrey_date_mc: # -if MC (bottom of screen highlighted)
        $ freeroam17.add("mc")

        scene v16s39_5a
        with dissolve

        menu:
            "Compliment yourself":
                $ add_point(KCT.TROUBLEMAKER)
                $ add_point(KCT.BRO)

                scene v16s39_5b
                with dissolve

                u "I must say, I think I'm looking pretty hot this evening."

                scene v16s39_5a
                with dissolve

                au "Someone's full of themself... Ha."

                scene v16s39_5b
                with dissolve

                u "Don't you agree?"

                scene v16s39_5a
                with dissolve

                au "Well, duh... You always look sexy in a suit, [name]."

                scene v16s39_9 # TPP. Show a side angle shot, camera is centered just above table level, Aubrey is looking at MC and smirking, mouth is closed, MC is looking at Aubrey with a proud smile, mouth is closed
                with dissolve

                pause 0.75

                scene v16s39_5b
                with dissolve

                u "I know. I just like to hear you say it."

                scene v16s39_5a
                with dissolve

                au "Hm... I didn't realize I was going out with a narcissist. *Laughs*"

                scene v16s39_5b
                with dissolve

                u "What can I say? Haha, I'm sexy and I know it."

            "Joke about yourself": # (ONE POINT)
                $ v16_aubrey_date_points += 1
                $ add_point(KCT.BOYFRIEND)
                $ add_point(KCT.BRO)

                scene v16s39_5b
                with dissolve

                u "You know in the movies when they dress up a monkey in human clothes?"

                scene v16s39_5a
                with dissolve

                au "Haha, where's this going?"

                scene v16s39_5b
                with dissolve

                u "I just feel a bit like that when I dress up really smart."

                scene v16s39_5a
                with dissolve

                au "*Laughs* You feel like a monkey?"

                scene v16s39_5b
                with dissolve

                u "Haha, no... I just mean I feel like a fish out of water, you know?"

                scene v16s39_5a
                with dissolve

                au "Are you kidding? I know exactly how you feel, just not sure about the monkey part..."

                scene v16s39_5b
                with dissolve

                u "Maybe I shouldn't compare myself to a monkey... or a fish, for that matter."

                scene v16s39_5a
                with dissolve

                au "Haha, it's okay. You're lucky you're cute."

                scene v16s39_5f
                with dissolve

                au "My little monkey boy. *Laughs*"

                scene v16s39_5b
                with dissolve

                u "*Groans* I hope that's not my new nickname."

                scene v16s39_5a
                with dissolve

                au "Hehe... We'll see."
            
        call screen v16s39_fr_screen1 # -Return to free roam screen-

    label v16s39_fr_aubrey_date_menu: # -if Menu, free roam ends
        $ freeroam17.add("menu")

        scene v16s39_9a # TPP. Show a side angle shot, camera is centered just above table level, Aubrey and MC are looking at their dinner menu's, slight smiles, mouths are closed, the waiter can be seen approaching them, slight creepy smile, mouth is closed
        with dissolve

        pause 0.75

        scene v16s39_4
        with dissolve

        waiter "Are we ready to order?"

        scene v16s39_4b
        with dissolve

        menu:
            "Order for Aubrey":
                $ add_point(KCT.TROUBLEMAKER)

                scene v16s39_4b
                with dissolve

                u "Yeah, I'll have the spaghetti and meatballs."

                scene v16s39_5
                with dissolve

                au "And-"

                scene v16s39_4b
                with dissolve

                u "And she'll have the pepperoni pizza?"

                scene v16s39_5i # FPP. Show just Aubrey sitting down in her chair at the table, stiff faced/confused/slightly angry expression, mouth is open, looking at MC
                with dissolve

                au "Um-"

                scene v16s39_4a
                with dissolve

                waiter "Wonderful choices. Two of our most popular dishes... You're in for a treat!"

                scene v16s39_9b # TPP. Show a side angle shot, camera is centered just above table level, Aubrey and MC are handig their menu's to the waiter, Aubrey has a slightly sad expression mouth is closed looking at MC, Mc has a slight smile mouth is closed looking at the waiter, The waiter has a creepy smile looking at MC mouth is closed
                with dissolve

                pause 0.75

                scene v16s39_5i
                with dissolve

                au "[name], I don't remember asking you to order for me."

                scene v16s39_5h # FPP. Show just Aubrey sitting down in her chair at the table, stiff faced/confused/slightly angry expression, mouth is closed, looking at MC
                with dissolve

                u "Oh, I thought it would be like a romantic thing to do."

                u "Besides, didn't you hear the waiter? They're both popular choices."

                scene v16s39_5i
                with dissolve

                au "What else would he have said? \"Oh, don't order that, it's gross.\"?"

                scene v16s39_5h
                with dissolve

                u "I mean, I'm sure it's going to be good. It's pizza and I know you like pizza."

                scene v16s39_5i
                with dissolve

                au "Hmph... If I don't like it, I get your pasta."

                scene v16s39_5b
                with dissolve

                u "Fair. And if you're still not happy?"

                scene v16s39_5f
                with dissolve

                au "If I'm still not happy, you'll be punished."

                scene v16s39_5b
                with dissolve

                u "*Chokes* Ha... *Coughs* What?"

                scene v16s39_5e
                with dissolve

                au "Naughty boys get punished, I don't make the rules. That's what you get for ordering for me."

            "Order for yourself": # (ONE POINT)
                $ v16_aubrey_date_points += 1
                $ add_point(KCT.BOYFRIEND)

                scene v16s39_5
                with dissolve

                au "Spaghetti and meatballs for me, please."

                scene v16s39_5b
                with dissolve

                u "Hey, I was going to order that... Cheater."

                scene v16s39_5a
                with dissolve

                au "Haha, cheater? Hmm... Okay, tell you what..."

                au "You have the spaghetti and meatballs and I'll have the pepperoni pizza. That way I can taste both."

                scene v16s39_5b
                with dissolve

                u "Haha, assuming that I'll share?"

                scene v16s39_5a
                with dissolve

                au "You will if you know what's good for you."

                scene v16s39_5j # FPP. Show just Aubrey sitting down in her chair at the table, winking at MC, slight smile, mouth is closed, looking at MC
                with dissolve

                pause 0.75

                scene v16s39_4
                with dissolve

                waiter "They are both equally delicious. You won't be disappointed."

                scene v16s39_4b
                with dissolve

                u "Okay, sounds good to me."

                scene v16s39_6b # TPP. Show MC and Aubrey sitting at the table, looking at each other and smiling, the waiter is standing in behind the table looking at MC, with a creepy smile, mouth is closed, holding an order pad
                with dissolve

                pause 0.75

                scene v16s39_9c # TPP. Show a side angle shot, camera is centered just above table level, Aubrey and MC are handig their menu's to the waiter, Aubrey and MC are looking at the waiter slight smiles, mouths are closed, The waiter has a creepy smile looking at MC mouth is closed
                with dissolve

                pause 0.75

                scene v16s39_4j
                with dissolve

                pause 0.75

        # -Regardless of ordering choice-

        scene v16s39_9d # TPP. Show a side angle shot, camera is centered just above table level, Aubrey and Mc are taking a drink from their fruity soda's, looking at each other slight smiles
        with dissolve

        pause 0.75

        scene v16s39_5c
        with dissolve

        u "I'm actually starving now. *Laughs* I can't wait to eat."

        scene v16s39_5a
        with dissolve

        au "Me too! I've waited all day for this meal."

        scene v16s39_5b
        with dissolve

        u "You starved yourself?"

        scene v16s39_5a
        with dissolve

        au "I was excited!"

        scene v16s39_5b
        with dissolve

        u "Haha... *Sighs*"

        scene v16s39_9e # TPP. Show a side angle shot, camera is centered just above table level, Aubrey and MC are looking at the waiter, slight smiles, mouths are closed, the waiter can be seen approaching them with their food on a tray, slight creepy smile, mouth is closed
        with fade

        pause 0.75

        scene v16s39_4i
        with dissolve

        waiter "And here we go... Two beautifully delicious, and deliciously beautiful plates of food."

        waiter "One authentic, Italian stone-baked pizza... And one spaghetti and meatballs with our signature tomato sauce."

        scene v16s39_5
        with dissolve

        au "*Sniffs* Mmmm... This smells so fucking g- Oh, excuse my language, haha! Sorry. It smells great."

        scene v16s39_4k # FPP. Show just the waiter standing at the table, now holding an empty tray, slightly creepy smile, mouth is closed, looking at MC, the camera angle is from a seated position
        with dissolve

        u "Yeah, thank you so much."

        scene v16s39_4h
        with dissolve

        waiter "Of course, and no need to apologize my dear. *Whispers* It is pretty fucking good."

        scene v16s39_5
        with dissolve

        au "*Chuckles*"

        scene v16s39_4i
        with dissolve

        waiter "I shall leave you to enjoy."

        scene v16s39_4j
        with dissolve

        pause 0.75

        scene v16s39_5b
        with dissolve

        u "Food!"

        scene v16s39_5a
        with dissolve

        au "Foooood!"

        # scene v16s39_10 # TPP. We enter the free roam screen from MC's POV. The player can click on Aubrey, Aubrey's food, MC's food, and Dessert menu. Clicking on the Dessert menu will give the option to end the free roam, Aubrey and MC are both looking at each other slight smiles, mouths are closed
        # with dissolve

        # pause 0.75

        call screen v16s39_fr_screen2 # The player can click on Aubrey, Aubrey's food, MC's food, and Dessert menu. Clicking on the Dessert menu will give the option to end the free roam, Aubrey and MC are both looking at each other slight smiles, mouths are closed

    label v16s39_fr_aubrey_date_aubrey2: # -if Aubrey
        $ freeroam17.add("aubrey2")

        scene v16s39_5b
        with dissolve

        menu:
            "Discuss her parents": # (ONE POINT)
                $ v16_aubrey_date_points += 1
                $ add_point(KCT.BOYFRIEND)
                $ add_point(KCT.BRO)

                scene v16s39_5b
                with dissolve

                u "So, how are your parents doing? Did they go on a second honeymoon?"

                scene v16s39_5a
                with dissolve

                au "Haha, yes. As crazy as it is... They flew out yesterday."

                au "They seem to be getting on better than ever, actually. It's nice to see."

                scene v16s39_5b
                with dissolve

                u "Where did they decide to go this time?"

                scene v16s39_5a
                with dissolve

                au "Mexico. They want to do a bunch of tourist stuff like check out the ancient ruins and hit all the beaches. It looks amazing there, to be honest."

                scene v16s39_5b
                with dissolve

                u "Really? Maybe we can go someday."

                scene v16s39_5a
                with dissolve

                au "Yes! I'd love that. That would be a vacation to remember for sure, haha."

            "Discuss the Chicks":
                $ add_point(KCT.TROUBLEMAKER)
                $ add_point(KCT.BRO)

                scene v16s39_5b
                with dissolve

                u "So, what's the latest gossip about the Chicks presidency?"

                scene v16s39_5k # FPP. Show just Aubrey sitting down in her chair at the table, no expression, mouth is open, looking at MC
                with dissolve

                au "*Sighs* I don't care about Chicks drama anymore. Not right now at least."

                au "I'm seriously at the point where I just want to ignore that it's even happening."

                scene v16s39_5l # FPP. Show just Aubrey sitting down in her chair at the table, no expression, mouth is closed, looking at MC
                with dissolve

                u "Aww, you don't want to... What's the saying? \"Spill all the hot goss\"?"

                scene v16s39_5a
                with dissolve

                au "*Giggles* No, sorry. The energy in the house feels so weird right now, I'm not even comfortable in my own room."

                scene v16s39_5b
                with dissolve

                u "Yeah, I can see how it might make everything stressful. It'll be nice once it's all settled, and the campaigning ends."

                scene v16s39_5a
                with dissolve

                au "Yeah, tell me about it! Ugh, I'm over it."
            
        call screen v16s39_fr_screen2 # -Return to free roam-

    label v16s39_fr_aubrey_date_aubrey_food: # -if Aubrey's food
        $ freeroam17.add("aubreyfood")

        scene v16s39_11 # FPP. Show a close up shot of the Pizza on the plate on the table that Aubrey is eating
        with dissolve

        menu:
            "Critique her food":
                $ v16s39_food_critic = True
                $ add_point(KCT.TROUBLEMAKER)

                scene v16s39_5b
                with dissolve

                u "Your pizza is supposed to be stone-baked, right?"

                scene v16s39_5k
                with dissolve

                au "Um, I think that's what he said... Why?"

                scene v16s39_5l
                with dissolve

                u "It looks like it's been microwaved. *Scoffs*"

                scene v16s39_5a
                with dissolve

                au "Are you serious? It tastes amazing to me, haha."

                scene v16s39_5l
                with dissolve

                u "Are you sure? It looks kinda soggy... We can always send it back if you'd like something else."

                scene v16s39_5a
                with dissolve

                au "[name]. Seriously, stop being weird about my food. If there was an issue, I'm perfectly capable of saying so."

                scene v16s39_5b
                with dissolve

                u "You're right, sorry. It just doesn't look as good as it did in the picture, I guess."

                scene v16s39_5a
                with dissolve

                au "Well, it tastes great."

                scene v16s39_5b
                with dissolve

                u "Good."

            "Compliment her food": # (ONE POINT)
                $ v16_aubrey_date_points += 1
                $ add_point(KCT.BOYFRIEND)
                $ add_point(KCT.BRO)

                scene v16s39_5b
                with dissolve

                u "The waiter wasn't lying... Your pizza looks delicious."

                scene v16s39_5a
                with dissolve

                au "Haha, it's so strange... It tastes so fresh and organic? If that's even a thing? *Laughs*"

                scene v16s39_5b
                with dissolve

                u "Do you feel like you're in Italy?"

                scene v16s39_5a
                with dissolve

                au "Not quite... But it does make me wonder if the pizza there is better than this masterpiece here."

                scene v16s39_5b
                with dissolve

                u "I guess we'll need to take another Europe trip to find out for sure."

                scene v16s39_5f
                with dissolve

                au "Haha, deal! Once my bank account has recovered from our first trip to Europe, though."

                scene v16s39_5g
                with dissolve

                u "*Laughs* Same."

        call screen v16s39_fr_screen2 # -Return to free roam-

    label v16s39_fr_aubrey_date_mc_food: # -if MC's food
        $ freeroam17.add("mcfood")

        scene v16s39_12 # FPP. Show a close up shot of the meatballs on the plate on the table that MC is eating
        with dissolve

        menu:
            "Critique your food":
                $ v16s39_food_critic = True
                $ add_point(KCT.TROUBLEMAKER)
                $ add_point(KCT.BRO)

                scene v16s39_13 # TPP. Show Just MC sitting at the table eating his meatballs, looking at his food.
                with dissolve

                pause 0.75

                scene v16s39_13a # TPP. Show Just MC sitting at the table looking at his meatballs with a slightly disgusted expression, mouth is closed
                with dissolve

                pause 0.75

                scene v16s39_5b
                with dissolve

                u "These meatballs..."

                scene v16s39_5k
                with dissolve

                au "What's wrong?"

                scene v16s39_5l
                with dissolve

                u "They're kinda stodgy."

                scene v16s39_5k
                with dissolve

                au "Stodgy?"

                scene v16s39_5l
                with dissolve

                u "Yeah, like- Chewy, but not in a good way."

                scene v16s39_5k
                with dissolve

                au "They look fine to me..."

                scene v16s39_5l
                with dissolve

                u "Try one."

                scene v16s39_9f # TPP. Show a side angle shot, camera is centered just above table level, MC's meatballs are plated in front of him, and Aubrey's pizza is plated in front of her, MC is feeding a meatball to Aubrey slight smile mouth is closed looking at Aubrey, Aubrey is eating the meatball off of his fork holding a napkin underneath of the fork, slightly shocked with excitement expression, looking at the meatball
                with dissolve

                pause 0.75

                scene v16s39_5m # FPP. Show just Aubrey sitting down in her chair at the table, confused expression, mouth is open, looking at MC
                with dissolve

                au "Are you insane?! That's the best meatball I've ever tasted, [name]."

                scene v16s39_5n # FPP. Show just Aubrey sitting down in her chair at the table, confused expression, mouth is closed, looking at MC
                with dissolve

                u "I guess my taste buds are just... more refined. *Snickers*"

                scene v16s39_5f
                with dissolve

                au "Ha, okay. Send it back then, master chef."

                scene v16s39_5b
                with dissolve

                u "No, no. It's okay. They're still edible."

                scene v16s39_5l
                with dissolve

                au "*Sighs*"

            "Compliment your food": # (ONE POINT)
                $ v16_aubrey_date_points += 1
                $ add_point(KCT.BOYFRIEND)
                $ add_point(KCT.BRO)

                scene v16s39_5b
                with dissolve

                u "I've got to say... I'm absolutely loving these meatballs. I mean-"

                scene v16s39_5a
                with dissolve

                au "*Giggles*"

                scene v16s39_5b
                with dissolve

                u "What? Ha."

                scene v16s39_5f
                with dissolve

                au "That's what I think to myself when I'm with you."

                scene v16s39_5g
                with dissolve

                u "*Laughs* Love this meatball?"

                scene v16s39_5a
                with dissolve

                au "Hehe, so you're happy with your choice then?"

                scene v16s39_5b
                with dissolve

                u "Very happy, it's the shit. *Chuckles*"

                scene v16s39_5a
                with dissolve

                au "Haha, give me a taste?"

                scene v16s39_9f
                with dissolve

                pause 0.75

                scene v16s39_5f
                with dissolve

                au "Oh, you weren't lying. Your meatballs are incredible! *Laughs*"

                scene v16s39_5b
                with dissolve

                u "Haha, thank you. You can feast on my meatballs anytime."

                scene v16s39_5f
                with dissolve

                au "*Laughs* You're ridiculous."

                scene v16s39_5g
                with dissolve

                u "You love it."

                scene v16s39_5a
                with dissolve

                au "You think so?"

                scene v16s39_5e
                with dissolve

                pause 0.75

                scene v16s39_5b
                with dissolve

                u "I know so."

                scene v16s39_9
                with dissolve

                pause 0.75

        call screen v16s39_fr_screen2 # -Return to free roam-

    label v16s39_fr_aubrey_date_dessert_menu: # -if Dessert menu, free roam ends
        $ freeroam17.add("dessertmenu")

        scene v16s39_9g # TPP. Show a side angle shot, camera is centered just above table level, Empty plates are in front of MC and Aubrey, Aubrey and MC are looking at their dessert menu's, slight smiles, mouths are closed, the waiter can be seen approaching them carrying an empty tray, slight creepy smile, mouth is closed
        with dissolve

        pause 0.75

        scene v16s39_4
        with dissolve

        waiter "I trust that everything was cooked to your satisfaction?"

        scene v16s39_5
        with dissolve

        au "Yes! It was great, thank you."

        scene v16s39_4b
        with dissolve

        u "Our compliments to the chef."

        if v16s39_food_critic: # -if mc critiqued his food, aubreys food, or both of them
            scene v16s39_5a
            with dissolve

            au "Ha. But you said-"

            scene v16s39_4b
            with dissolve

            u "I mean overall, it was good."

            # -end if

        scene v16s39_4
        with dissolve

        waiter "And now for dessert. What would you like?"

        scene v16s39_5b
        with dissolve

        menu:
            "Order dessert": # (ONE POINT)
                $ v16_aubrey_date_points += 1
                $ add_point(KCT.BOYFRIEND)

                scene v16s39_4b
                with dissolve

                u "We'll have a couple of slices of that chocolate cake."

                scene v16s39_4
                with dissolve

                waiter "Another excellent choice! I take a piece home every night... *Whispers* Don't tell anyone I said that."

                scene v16s39_4b
                with dissolve

                u "*Laughs* Your secret is safe with us."

                scene v16s39_5f
                with dissolve

                au "I wasn't planning on dessert but, then you said the word chocolate, so."

                scene v16s39_5g
                with dissolve

                u "Haha, oops."

                scene v16s39_5f
                with dissolve
                
                au "No, I'm excited now! You made it sound yummy. Let's do it."

            "Let her decide":
                $ add_point(KCT.TROUBLEMAKER)
                $ add_point(KCT.BRO)

                scene v16s39_5
                with dissolve

                au "I'm not sure if I want any dessert..."

                scene v16s39_4a
                with dissolve

                waiter "We have many homemade cakes and a list of different flavors of ice cream."

                scene v16s39_4b
                with dissolve

                u "I'll have a slice of chocolate cake."

                scene v16s39_4
                with dissolve

                waiter "Excellent, our chocolate cake is to die for. Shall I make it two slices, dear?"

                scene v16s39_5k
                with dissolve

                au "You just had to go and mention chocolate didn't you. *Sighs*"

                scene v16s39_5l
                with dissolve

                u "Haha, sorry. You don't have to get any if you don't want to."

                scene v16s39_5
                with dissolve

                au "Okay, fine. I'll try it."
            
    # -Regardless of ordering choice-
        scene v16s39_4a
        with dissolve

        waiter "Splendid."

        waiter "And if you don't mind, I'll clear these plates away for you. It's so nice to see them empty! I'll be right back with dessert."

        scene v16s39_4b
        with dissolve

        u "Thank you."

        scene v16s39_4l # FPP. The waiter has walked a slight distance away from the table, back is turned towards the camera, his face is not visible, carrying the empty plates on the tray
        with dissolve

        pause 0.75

        scene v16s39_5a
        with dissolve

        au "Aw! He's such a good waiter, isn't he?"

        scene v16s39_5b
        with dissolve

        u "Yeah, and very smiley. His face is probably stuck like that from smiling all day at customers."

        scene v16s39_5a
        with dissolve

        au "*Laughs* Maybe he's just a very happy man."

        if v16_aubrey_date_birthday: # -if MC made a Birthday reservation
            scene v16s39_4m # FPP. The waiter is the same distance from the table as in render v16s39_4d, facing the camera, looking at MC, carrying a tray with 2 desserts on it, and one of them has a lit candle on it, slightly creepy smile, mouth is closed
            with dissolve

            pause 0.75

            scene v16s39_5m
            with dissolve

            au "A candle? Why-"

            scene v16s39_4n # FPP. Show just the waiter standing at the table, now holding a single plate with a chocolate dessert on it with a lit candle on the dessert, full creepy smile, mouth is open, looking at Aubrey, the camera angle is from a seated position
            with dissolve

            waiter "*Loud singing* Happy birthday to you! Happy birthday to you!"

            scene v16s39_9h # TPP. Show a side angle shot, camera is centered just above table level, the waiter is standing at the table holding the dssert from render v16s39_4n, looking at Aubrey full creepy smile mouth is open, Aubrey has an embarrassed expression trying to look away from the waiter mouth is closed, MC is looking at Aubrey with a slight smile mouth is closed
            with dissolve

            pause 0.75

            scene v16s39_5o # FPP. Show just Aubrey sitting down in her chair at the table, embarrased expression, mouth is open, looking at MC
            with dissolve

            au "Oh, my god... [name]?"

            scene v16s39_5p # FPP. Show just Aubrey sitting down in her chair at the table, embarrased expression, mouth is closed, looking at MC
            with dissolve

            u "Happy birthday!"

            scene v16s39_5o
            with dissolve

            au "*Whispers* Everyone's looking at me right now..."

            scene v16s39_4n 
            with dissolve

            waiter "*Loud singing* Happy birthday, pretty lady!"

            scene v16s39_5q # FPP. Show just Aubrey sitting down in her chair at the table, embarrased expression, mouth is open, looking at the waiter
            with dissolve

            au "Stop, please. Can you stop singing?"

            scene v16s39_4o # FPP. Show just the waiter standing at the table, now holding a single plate with a chocolate dessert on it with a lit candle on the dessert, full creepy smile, mouth is open, looking at Aubrey, the hand holding the dessert is extended out towards Aubrey, with the other hand raised in the air like an Opera singer, the camera angle is from a seated position
            with dissolve

            waiter "*Loud singing* Happy birthday tooooooo..."

            scene v16s39_5q
            with dissolve

            au "Can you please-"

            scene v16s39_4p # FPP. Show just the waiter standing at the table, now holding a single plate with a chocolate dessert on it with a lit candle on the dessert, full creepy smile, mouth is open, looking at Aubrey, the waiter uses both hands to hold out the dessert towards Aubrey, the camera angle is from a seated position
            with dissolve

            waiter "*Loud singing* ...Youuuuu-"

            scene v16s39_9i # TPP. Show a side angle shot, camera is centered just above table level, the waiter is standing at the table holding the dssert from render v16s39_4n with both hands clenching the dessert back towards him with a shocked expression mouth is open looking at Aubrey, Aubrey has stood up and slammed her fists on the table extremely angry expression looking at the waiter mouth is open, Mc is looking at Aubrey an dalmost falls back in his chair with a shocked expression mouth is open
            with vpunch

            au "Just shut the fuck up!"

            scene v16s39_9j # TPP. Show a side angle shot, camera is centered just above table level, the waiter is standing at the table holding the dssert from render v16s39_4n with both hands clenching the dessert back towards him with no expression mouth is closed looking at Aubrey, Aubrey has sat back down looking extremly flustered looking away from MC and the Waiter, Mc has regained his compusure in his seat and is looking at Aubrey with no expression mouth is closed
            with dissolve

            pause 0.75

            scene v16s39_4q # FPP. Show just the waiter standing at the table, now holding a single plate with a chocolate dessert on it with a lit candle on the dessert close to his chest, no expression, mouth is open, looking at Aubrey, the camera angle is from a seated position
            with dissolve

            waiter "Oh-"

            scene v16s39_5q
            with dissolve

            au "It's not my birthday."

            scene v16s39_4q 
            with dissolve

            waiter "Oh, I'm so sorry... There must have been an error with the booking."

            scene v16s39_4r # FPP. Show just the waiter standing at the table, now holding a single plate with a chocolate dessert on it with a lit candle on the dessert close to his chest, no expression, mouth is open, looking at MC, the camera angle is from a seated position
            with dissolve

            u "(Well, I guess that backfired. Poor guy lost his smile...)"

            scene v16s39_4s # FPP. Show just the waiter standing at the table, he takes the candle out of the dessert and places the plate near Aubrey, no expression, mouth is closed, looking at Aubrey, the camera angle is from a seated position
            with dissolve

            pause 0.75

            scene v16s39_4j
            with dissolve

            pause 0.75

            scene v16s39_5r # FPP. Show just Aubrey sitting down in her chair at the table, angry expression, mouth is open, looking at MC
            with dissolve

            au "Fuck, that was so embarrassing! What just happened?"

            scene v16s39_5s # FPP. Show just Aubrey sitting down in her chair at the table, angry expression, mouth is closed, looking at MC
            with dissolve

            menu:
                "Confess your mistake": # (MINUS POINT)
                    $ v16_aubrey_date_points -= 1
                    $ add_point(KCT.TROUBLEMAKER)
                    $ add_point(KCT.BRO)

                    scene v16s39_5s
                    with dissolve

                    u "Um... I may have had something to do with that."

                    scene v16s39_5k
                    with dissolve

                    au "What do you mean, you may?"

                    scene v16s39_5l
                    with dissolve

                    u "I made a birthday reservation, so you'd get the free dessert. I thought you'd find it funny, I guess? It's free dessert."

                    scene v16s39_5r
                    with dissolve

                    au "What the fuck, [name]? I hated that."

                    scene v16s39_5s
                    with dissolve

                    u "Well, I know that now. I'm sorry."

                    scene v16s39_5k
                    with dissolve

                    au "*Sighs*"

                    scene v16s39_5l
                    with dissolve

                    u "I didn't mean to upset you with it, the intention was the complete opposite. Is there anything I can do to make it up to you?"

                    scene v16s39_5k
                    with dissolve

                    au "Just promise you'll never make me the center of attention like that, ever again."

                    scene v16s39_5l
                    with dissolve

                    u "I promise, no more surprises."

                    scene v16s39_5s
                    with dissolve

                    au "..."

                    scene v16s39_5l
                    with dissolve

                    u "Seriously, I promise."

                    u "Can you forgive me?"

                    scene v16s39_5k
                    with dissolve

                    au "Eventually... Probably."

                "Blame restaurant":
                    $ add_point(KCT.TROUBLEMAKER)
                    $ add_point(KCT.BOYFRIEND)

                    scene v16s39_5s
                    with dissolve

                    u "Yeah, jeez. Someone really messed up there. Are you okay?"

                    scene v16s39_5r
                    with dissolve

                    au "No! That was awful! I hate being the center of attention like that."

                    scene v16s39_5s
                    with dissolve

                    u "Yikes, I'm sorry. And I'm sure whoever made that mistake is also really, really sorry..."

                    scene v16s39_5t # FPP. Show just Aubrey sitting down in her chair at the table, Aubrey closes her eyes and puts her head back, mouth is open
                    with dissolve

                    au "*Exhales deeply*"

                    scene v16s39_5l
                    with dissolve

                    u "At least it's over now."

                    scene v16s39_5k
                    with dissolve

                    au "Trust me, I'll have nightmares tonight with his big smiling face singing at me."

                    scene v16s39_5l
                    with dissolve

                    u "Ha... (Shit.)"
            
        else: # -if MC made a Standard reservation (ONE POINT)
            $ v16_aubrey_date_points += 1

            scene v16s39_4t # FPP. The waiter is the same distance from the table as in render v16s39_4d, facing the camera, looking at MC, carrying a tray with 2 desserts on it, slightly creepy smile, mouth is closed
            with dissolve

            pause 0.75

            scene v16s39_4u # FPP. Show just the waiter standing at the table, he places the dessert plate with the chocalote dessert on it near Aubrey, creepy smile, mouth is open, looking at Aubrey, the camera angle is from a seated position
            with dissolve

            waiter "Two slices of incredible chocolate cake made by our resident cake artist and finished with a dollop of love."

            scene v16s39_5
            with dissolve

            au "Haha! Thank you so much."

            scene v16s39_4g
            with dissolve

            u "(How many artists do they have back there?)"

            scene v16s39_4j
            with dissolve

            pause 0.75

            scene v16s39_5u # FPP. Show just Aubrey sitting down in her chair at the table, with some chocalte dessert on her fork about to eat it, mouth is closed, looking at MC
            with dissolve

            u "This is going to hit the spot."

            scene v16s39_5v # FPP. Show just Aubrey sitting down in her chair at the table, with some chocalte dessert on her fork about to eat it, mouth is open, looking at MC
            with dissolve

            au "Wow, yeah... Good call."

            scene v16s39_14 # TPP. Aubrey and MC start eating their cake, slight smiles, looking at each other. In the background, the waiter delivers some desserts (something different to chocolate cake) to a middle-aged couple. The cake for the woman has a candle in it, The waiter has a creepy smile, mouth is open, holding the cake out towards the woman with one hand with the other hand in the air like an Opera singer, the middle aged couple are looking at the waiter with slight smiles, mouths are closed
            with dissolve

            waiter "*Loud singing* Happy birthday to you! Happy birthday to you!"

            scene v16s39_14a # TPP. same as v16s39_14 The only difference is that MC and Aubrey have stopped eating their desserts and are now looking at the waiter and the middle aged couple
            with dissolve

            pause 0.75

            scene v16s39_5f
            with dissolve

            au "Fuck, I'm glad that's not me. *Laughs* I'd be dying of embarrassment right now."

            scene v16s39_14a
            with dissolve

            waiter "*Loud singing* Happy birthday, pretty lady!"

            scene v16s39_5b
            with dissolve

            u "Haha, really? Not a fan of getting special treatment?"

            scene v16s39_5a
            with dissolve

            au "Absolutely not... The brighter the spotlight, the weaker I feel. It's strange but, yeah."

            scene v16s39_5b
            with dissolve

            u "(Good thing I didn't choose the birthday reservation...)"

            scene v16s39_14a
            with dissolve

            waiter "*Loud singing* Happy birthday tooooooooo youuuuuuuuu!"

            scene v16s39_5f
            with dissolve

            au "Haha, he has an amazing voice though!"

            scene v16s39_5b
            with dissolve

            u "Yeah, he does have an impressive pair of lungs on him."

            scene v16s39_5a
            with dissolve

            au "*Laughs*"

            scene v16s39_14b # TPP. same as v16s39_14 The waiter has finished singing and is now taking a bow creepy smile mouth is closed, Everyone in the render is looking at the Waiter full smiles and are clapping
            with dissolve

            pause 0.75

        scene v16s39_4v # FPP. Show just the waiter standing at the table, he holds out the bill towards MC, full creepy smile, mouth is closed, looking at MC, the camera angle is from a seated position
        with dissolve

        pause 0.75

        scene v16s39_2a # TPP. same as v16s39_2 Except the waiter is entering the coat room, his back is turned towards the camera, while Aubrey and MC wait outside of it for her jacket, slight smiles, looking at each other
        with dissolve

        pause 0.75

        scene v16s39_2b # TPP. MC helps Aubrey put on her jacket, both of them slight smiles, mouths are closed, looking at each other, The waiter is looking at Mc and Aubrey creepy smile mouth is closed
        with dissolve

        pause 0.75

        scene v16s39_2c # TPP. Aubrey now has her jacket on as her and MC leave the restaurant with slight smiles, mouths are closed, The waiter waves goodbye to MC and Aubrey with a creepy smile mouth is open
        with dissolve

        pause 0.75

        jump v16s40 # -Transition to Scene 40-