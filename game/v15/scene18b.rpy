# SCENE 18b: Lauren Halloween Party Gift Opening
# Locations: Deer's house
# Characters: MC (Outfit: Stripper Costume), AUBREY (Outfit: Clown Costume), RYAN (Outfit: Elvis Costume), AUTUMN (Outfit: Mummy), PENELOPE (Outfit: Sexy Witch), LAUREN (Outfit: Spider necklace costume), IMRE (Outfit: Cowboy Costume), RILEY (Outfit: Schoolgirl Costume), CHRIS (Outfit: Boxer Costume), AMBER (Outfit: Black bloody nurse costume)
# Time: Night

label v15s18b:
    $ freeroam13.add("lauren2")

    scene v15s18b_1 # TPP. Show Lauren sitting on the couch surrounded by gifts, slight smile, mouth open.
    #with dissolve
    
    la "Gather around, everyone! I'm going to open some of these gifts."

    scene v15s18b_2 # TPP. Shot of the while room everyone sitting in chairs and on the couch.
    with dissolve

    pause 1.25

    scene v15s18b_3 # TPP. Close up of Lauren so we don't have to render everyone, Lauren picking up a gift, slight smile, mouth closed.
    with dissolve

    pause 1.25

    scene v15s18b_3a # TPP. Lauren reading the label on the gift she is holding, Lauren slight smile, mouth open.
    with dissolve

    la "This one is from..."

    la "Imre!"

    scene v15s18b_3b # TPP. Lauren unwrapping the gift she is holding, Lauren slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s18b_4 # TPP. Close up of just Imre sitting somewhere in the room, Imre slight smile, mouth open.
    with dissolve

    imre "This will be the best gift she's ever gotten."

    scene v15s18b_3c # TPP. Lauren holding up a gift card, Lauren slight smile, mouth open.
    with dissolve

    la "It's a $50 gift card! Thank you, Imre. That's so thoughtful."

    if gift_card_50 in mc.inventory:
        scene v15s18b_5 # FPP. MC sitting on a chair in the area looking at Lauren, Lauren looking at the gift card, Lauren slight smile, mouth closed.
        with dissolve

        u "(Ah, fuck! Now I'm going to look like an idiot.)"

    scene v15s18b_4
    with dissolve

    imre "You're welcome! Ladies are too picky, so now you can just buy whatever you want with it."

    scene v15s18b_3c
    with dissolve

    la "Haha, smart idea."

    scene v15s18b_3d # TPP. Lauren holding up another gift, Lauren slight smile, mouth open.
    with dissolve

    la "And this one is from..."

    la "Amber."

    scene v15s18b_4
    with dissolve

    imre "It's going to be lube or something."

    scene v15s18b_6 # FPP. MC looking over at Imre, Imre looking over at MC, Imre slight smile, mouth closed.
    with dissolve

    u "Haha, nah, I don't think so."

    scene v15s18b_7 # FPP. MC looking over at Amber, Amber looking at MC, Amber slight smile, mouth open.
    with dissolve

    am "He isn't far off, actually. *Laughs*"

    scene v15s18b_7a # FPP. MC looking over at Amber, Amber looking at MC, Amber slight smile, mouth closed.
    with dissolve

    u "Really?"

    scene v15s18b_3e # TPP. Show Lauren holding up a pair of fluffy handcuffs, Lauren blushing, slight smile, mouth open.
    with dissolve

    la "Oh! Thanks, Amber. *Chuckles*"

    scene v15s18b_8 # TPP. Close up of just Amber looking in Lauren's direction, Amber slight smile, mouth open.
    with dissolve

    am "You'll either be using those on someone later or you'll be asking someone to use them on you. Whatever you prefer, haha."

    scene v15s18b_3f # TPP. Lauren looking over in Amber's direction, Lauren blushing, slight smile, mouth open.
    with dissolve

    la "You'll have to teach me how to use them."

    scene v15s18b_8a # TPP. Close up of just Amber looking in Lauren's direction, Amber winking, slight smile, mouth open.
    with dissolve

    am "No problem."

    scene v15s18b_4
    with dissolve

    imre "*Whispers* Can I watch?"

    scene v15s18b_3g # TPP. Lauren holding up a new gift, slight smile, mouth open.
    with dissolve

    la "This one is from..."

    la "[name]!"

    scene v15s18b_3i # TPP. Lauren unwrapping MC's gift, slight smile, mouth closed.
    with dissolve

    pause 0.75

    if lauren.relationship.value >= Relationship.GIRLFRIEND.value:
        scene v15s18b_9 # TPP. Shot of just Autumn looking in Lauren's direction, slight smile, mouth open.
        with dissolve

        aut "The moment of truth! Haha."

        scene v15s18b_5a # FPP. MC looking at Lauren, Lauren unwrapping MC's gift, Lauren slight smile, mouth closed.
        with dissolve

        u "(I hope she likes it...)"

    if gift_card_50 in mc.inventory:
        scene v15s18b_3c_alt
        with dissolve

        la "Oh, it's another $50 gift card. *Laughs* Did you go shopping with Imre?"

        scene v15s18b_6a # FPP. MC looking over at Imre, Imre looking at MC, Imre neutral face, mouth open.
        with dissolve

        imre "The fuck, [name]? You totally copied me!"

        scene v15s18b_6b # FPP. MC looking over at Imre, Imre looking at Mc, Imre neutral face, mouth closed.
        with dissolve

        u "No, haha. I just thought, what do you get the girl who already has everything?"

        u "A gift card is useful, you know, for a college student. You can get books or whatever..."

        if lauren.relationship.value >= Relationship.GIRLFRIEND.value:
            scene v15s18b_3h # TPP. Lauren holding the $50 gift card, Lauren unamused face, mouth open.
            with dissolve
            
            la "Yeah. That's true, I guess."

            scene v15s18b_7b # FPP. Mc looking at Amber, Amber looking at Mc, Amber neutral face, mouth open.
            with dissolve

            am "A gift card for your girlfriend, [name]? Really?"

            scene v15s18b_10 # TPP. Close up of just Ryan laying on the floor, Ryan looks miserable from being sick the whole party, Ryan frown, mouth open.
            with dissolve

            ry "That's pretty lame, bro. You should've gotten something more personal."

            scene v15s18b_4
            with dissolve

            imre "*Whispers* When the hell did Ryan get here?"

            scene v15s18b_11 # TPP. Just Riley looking in MC's direction, Riley slight smile, mouth open.
            with dissolve

            ri "Or jewelry!"

            scene v15s18b_6c # FPP. MC looking at Imre, Imre looking at MC, Imre slight smile, mouth open.
            with dissolve

            imre "Yeah! Where's the big diamond ring, huh?"

            scene v15s18b_5b # FPP. MC looking at Lauren, Lauren looking at the gift, Lauren frown, mouth closed.
            with dissolve

            menu:
                "Apologize":
                    $ add_point(KCT.BOYFRIEND)
                    
                    scene v15s18b_5c # FPP. MC looking at Lauren, Lauren looking at MC, Lauren slight frown, mouth closed.
                    with dissolve
                    
                    u "Look, I'm sorry, Lauren."

                    u "I didn't have much time and there weren't many options."

                    scene v15s18b_9a # TPP. Just Autumn looking in Lauren's direction, Autumn concerned, mouth open.
                    with dissolve

                    aut "It's the thought that counts. Right, Ren?"

                    scene v15s18b_5d # FPP. MC looking at Lauren, Lauren looking at Mc, Lauren slight frown, mouth open.
                    with dissolve

                    la "Uh, Yeah. Of course. Thank you, [name]."

                "Get offended":
                    $ add_point(KCT.BRO)
                    
                    scene v15s18b_17 # TPP. Frontal view of just MC, MC looking to his left, Arm expressions like he is mad, MC upset, mouth open.
                    with dissolve

                    u "Do you guys think you can stop shitting on me for a minute?"

                    scene v15s18b_17a # TPP. Frontal view of just MC, MC looking to his right, Arm expressions like he is mad, MC upset, mouth open.
                    with dissolve

                    u "I barely had any time to find a costume, let alone a gift."

                    scene v15s18b_18 # TPP. Just a shot of Chris, slight smile mouth open.
                    with dissolve

                    ch "We can tell, haha."

                    scene v15s18b_5c
                    with dissolve

                    u "*Sighs*"

                    scene v15s18b_5d
                    with dissolve

                    la "Well, thanks anyway. I guess it's the thought that counts, right?"

            scene v15s18b_5e # FPP. Lauren looking at MC, MC looking at Lauren, Lauren fake smile, mouth closed.
            with dissolve

            u "(*Sighs*)"

        else:
            scene v15s18b_3c_alt
            with dissolve

            la "Yeah. That's true, I guess."

    if white_horse_black_mane in mc.inventory:
        scene v15s18b_3j # TPP. Lauren holding up a white horse toy with a black mane, Lauren looking at the toy, Lauren excited, mouth open
        with dissolve

        la "Oh my! [name]..."

        scene v15s18b_5f # FPP. MC looking at Lauren, Lauren looking at MC, Lauren smile, mouth open.
        with dissolve

        la "This reminds me of a toy I had when I was a kid, I was obsessed with that thing!"

        scene v15s18b_5g # FPP. MC looking at Lauren, Lauren looking at MC, Lauren smile, mouth closed.
        with dissolve

        u "Haha, yeah. Autumn mentioned it to me, and I thought I'd get you one."

        scene v15s18b_5f
        with dissolve

        la "The horse I had was actually brown with a golden mane, but this one is really, really cute..."

        la "Thank you so much."

        scene v15s18b_5g 
        with dissolve

        u "(Dammit! I made the wrong choice with the color, but she still seems happy with it.)"

        u "You're welcome, I'm happy you like it."

    if brown_horse_golden_mane in mc.inventory:
        scene v15s18b_3q
        with dissolve

        la "*Gasps* [name]!"

        scene v15s18b_3n
        with dissolve

        la "I can't believe it, how did you know?!"

        scene v15s18b_9b # TPP. Close up of just Autumn looking in MC's direction with her thumb up and shooting him a wink, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s18b_5g
        with dissolve

        u "Haha, I have my methods."

        scene v15s18b_11a # TPP. Close up of just Riley looking Lauren's direction, slightly confused, mouth open.
        with dissolve

        ri "What even is it?"

        scene v15s18b_3k
        with dissolve

        la "It's just a horse, haha. It's a toy. But it looks exactly the same as the one I had when I was a kid."

        $ grant_achievement("childhood_memories")
        u "(Nice, picked the right color and everything. Phew!)"

        la "I would take it everywhere with me and then I lost it when we moved houses. That day made me so sad. Remember, Autumn?"

        scene v15s18b_9
        with dissolve

        aut "Oh, trust me. I remember. *Chuckles*"

        scene v15s18b_3k # TPP. Close up of just Lauren looking in Riley's direction, Lauren excited, mouth closed
        with dissolve

        la "But now we're reunited!"

        scene v15s18b_9
        with dissolve

        aut "It really does look the same, good job [name]."

        scene v15s18b_9c # TPP. Close up of just Autumn looking in MC's direction, slight smile, mouth closed.
        with dissolve

        u "Couldn't have done it without you!"

        scene v15s18b_3m # TPP. Show Lauren starting to stand up off the couch.
        with dissolve

        pause 0.5

        scene v15s18b_5h # FPP. Show Lauren walking over to MC, Lauren slight smile, mouth closed.
        with dissolve

        pause 0.5

        scene v15s18b_12 # FPP. MC standing up Lauren standing infront of him, MC looking at Lauren, Lauren looking at MC, Lauren excited, mouth closed.
        with dissolve

        pause 0.5
        
        if lauren.relationship.value >= Relationship.GIRLFRIEND.value:
            scene v15s18b_12a # FPP. Lauren giving MC a passionate kiss.
            with dissolve

            pause 0.75

            scene v15s18b_13a # TPP. Show just MC and Lauren passionately kissing.
            with dissolve
            play sound "sounds/kiss.mp3"
            pause 0.75

        else:
            scene v15s18b_13 # TPP. Show just MC and Lauren hugging, both slight smile, mouth closed.
            with dissolve
            
            pause 1

        scene v15s18b_12b # MC standing up Lauren standing infront of him, MC looking at Lauren, Lauren looking at MC, Lauren excited, mouth open.
        with dissolve

        la "This is my favorite gift ever. Thank you, [name]. This is so special!"

        scene v15s18b_12
        with dissolve

        u "You're very welcome. Happy Birthday!"

    if emerald_bracelet in mc.inventory or ruby_choker_necklace in mc.inventory:
        if lauren.relationship.value >= Relationship.GIRLFRIEND.value:
            scene v15s18b_3q
            with dissolve

            la "[name]!"

            scene v15s18b_3n # TPP. Lauren looking in the gift box none of the contents inside shown,Lauren excited, mouth open.
            with dissolve

            la "You bought me jewelry?!"

            scene v15s18b_15 # TPP. Close up of just Aubrey looking over in Lauren's direction, slight smile, mouth open.
            with dissolve

            au "Ooh! Try it on!"

            scene v15s18b_14 # TPP. Just a close up of Penelope looking over at Lauren's direction, slight smile, mouth open.
            with dissolve

            pe "Let's see it!"
            
            if ruby_choker_necklace in mc.inventory:
                scene v15s18b_3o # TPP. Show Lauren putting on the the Ruby Choker Necklace around her neck, Lauren excited, mouth closed.
                with dissolve

                pause 0.75

                scene v15s18b_3p # TPP. Show Lauren looking down at her chest and admiring the necklace, Lauren excited, mouth closed.
                with dissolve

                la "Wow. This is..."

            else:
                scene v15s18b_3r # TPP. Show Lauren putting the Emerald bracelet around her wrist, Lauren excited, mouth closed
                with dissolve

                pause 0.75

                scene v15s18b_3s # TPP. Show Lauren looking at her wrist with the emerald bracelet on, Lauren excited, mouth closed.
                with dissolve

                la "Wow. This is..."

            scene v15s18b_9
            with dissolve

            aut "Gorgeous! Holy shit, [name]!"

            scene v15s18b_8
            with dissolve

            am "Nice choice, [name]. That looks so pretty on you, Lauren."
            
            scene v15s18b_18
            with dissolve

            ch "Last year I bought Nora a new necklace. She really liked it, too."

            scene v15s18b_8b # TPP. Show just Amber looking in Chris's direction, Amber weirded out face, mouth closed.
            with dissolve

            pause 0.75

            scene v15s18b_15a # TPP. Show just Aubrey looking in Chris's direction, Aubrey weirded out, mouth closed.
            with dissolve

            pause 0.75

            scene v15s18b_3q
            with dissolve
            
            if ruby_choker_necklace in mc.inventory:
                la "I'll keep it safe here. Don't want my spidey to scratch it. *Chuckles*"
                
            else:
                la "I'll keep it here because this isn't really the outfit for it. *Chuckles*"

            scene v15s18b_3u # TPP. Lauren starting to get up off the couch, slight smile, mouth open.
            with dissolve

            la "But thanks to you this was the..."

            scene v15s18b_5h 
            with dissolve

            pause 0.75
            
            scene v15s18b_12b
            with dissolve

            la "Best birthday ever."

            scene v15s18b_12a 
            with dissolve
            pause 0.75

            scene v15s18b_13a
            with dissolve
            play sound "sounds/kiss.mp3"
            pause 1.25

            scene v15s18b_13b # TPP. Show just MC and Lauren kissing in a different position.
            with dissolve
            play sound "sounds/kiss.mp3"
            pause 1.25

            scene v15s18b_12
            with dissolve

            u "Wow, I should buy you jewelry more often. *Chuckles*"

            scene v15s18b_12b
            with dissolve

            la "*Laughs* You don't have to buy me more..."

            la "But I won't stop you if you want to, haha!"

            scene v15s18b_8
            with dissolve

            am "That's my girl. *Laughs*"

            scene v15s18b_12b
            with dissolve

            la "Thank you, [name]."

            scene v15s18b_12
            with dissolve

            u "Of course. Happy Birthday!"
            
        else:
            scene v15s18b_3n
            with dissolve

            la "Jewelry!? [name]... This is too much, ha."

            scene v15s18b_5g
            with dissolve

            u "No, come on. It's your birthday. There's no such thing as too much."

            scene v15s18b_5f
            with dissolve

            la "But this looks really expensive and romantic. *Chuckles*"

            scene v15s18b_5g
            with dissolve

            u "It's a present for your birthday, Lauren. I don't see the problem."

            scene v15s18b_6a
            with dissolve

            imre "It is a bit weird."

            scene v15s18b_7b
            with dissolve

            am "Yeah, cause you're not like, dating."

            scene v15s18b_7c # FPP. MC looking over at Amber, Amber looking at MC, Amber neutral face, mouth closed.
            with dissolve

            u "Really?"

            scene v15s18b_11
            with dissolve

            ri "Kinda, Yeah. That's not a gift that you give to a friend. *Laughs*"

            scene v15s18b_11b # TPP. Just Riley looking in MC's direction, Riley slight smile, mouth closed.
            with dissolve

            u "Well, fuck. I'm sorry for making it weird, I don't think-"

            scene v15s18b_9d # TPP. Autumn looking in MC's direction and winking at him, Slight smile, mouth open.
            with dissolve

            aut "Don't worry about it, I'll wear it if she doesn't. *Laughs*"

            scene v15s18b_5i # FPP. Lauren not holding anything, Lauren looking at MC, MC looking at Lauren, slight smile, mouth open.
            with dissolve

            la "Haha, It's okay. I appreciate it nonetheless."

            scene v15s18b_5j # FPP. Lauren not holding anything, Lauren looking at MC, MC looking at Lauren, slight smile, mouth closed.
            with dissolve

            u "(*Sighs* I hope so.)"

    scene v15s18b_3v # TPP. Lauren not holding anything her hands in the air, Lauren excited, mouth open.
    with dissolve

    la "Okay, I think that's enough gifts for now. I'll open the rest later after everyone leaves, haha. Let's get back to the party!"

    scene v15s18b_4a # TPP. Just Imre his hands in the air, Imre excited, mouth open.
    with dissolve

    imre "HELL YEAH!"

    scene v15s18b_9e # TPP. Just Autumn looking in Imre's direction, Autumn slight smile, mouth open.
    with dissolve

    aut "Imre, please, You're already the culprit of the Deer's first noise complaint, don't be the second one too."

    scene v15s18b_4a
    with dissolve

    imre "*Whispers* Hell yeaaaaahh!"

    scene v15s18b_9e
    with dissolve

    aut "*Chuckles* Better."

    scene v15s18b_16 # TPP. Show MC standing up slight smile, mouth closed.
    with dissolve

    pause 0.75

    $ v15s18b_kiwiiPost1= KiwiiPost(riley, "v15/rilpost1.webp", "Celebrating this pure soul tonight!", numberLikes=648)
    $ v15s18b_kiwiiPost1.newComment(lindsey, "So cute! Your costumes are perfect <3", numberLikes=renpy.random.randint(260, 560))
    $ v15s18b_kiwiiPost1.newComment(amber, "Ugh, where am I?!", numberLikes=renpy.random.randint(260, 560))
    $ v15s18b_kiwiiPost1.newComment(lauren, "Aw! Dammit Imre!", numberLikes=renpy.random.randint(260, 560))
    $ v15s18b_kiwiiPost1.addReply("Haha! Great pic you guys... Imre looks great!", numberLikes=renpy.random.randint(260, 560))
    $ v15s18b_kiwiiPost1.newComment(imre, "Oh hey! Hell yeah! I do look good...", numberLikes=renpy.random.randint(260, 560))

    jump v15s18c