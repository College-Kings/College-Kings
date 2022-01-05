# SCENE 4: Set up grand reopening of dog shelter
# Locations: Dog Shelter
# Characters: MC (Outfit: 5), Autumn (Outfit: 1)
# Time: Morning

label v15s4:
    scene v15s4_1 # TPP. Show MC walking up to the main entrance of the dog shelter, slight smile, mouth closed.
    with dissolve

    u "(Damn, this place really got an upgrade...)"

    scene v15s4_1a # TPP. Same as v15s4_1, Show MC looking a little off in the distance, slight smile, mouth closed.
    with dissolve

    u "(Oh, there's Autumn.)"

    scene v15s4_2 # TPP. Close up of just Autumn carrying two boxes one stacked on top of the other while she walks towards MC oblivious that he is at the entrance, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s4_2a # TPP. Same as v15s4_2, Autumn much closer to MC now not noticing him, slight smile, mouth closed.
    with dissolve

    pause 0.75

    menu:
        "Offer to help":
            $ AutumnLunchBreak = True
            $ add_point(KCT.BOYFRIEND)
            scene v15s4_3 # FPP. MC looking at Autumn. The boxes she is carrying obscuring her face from being seen.
            with dissolve

            u "Hey, there. Need a hand?"

            scene v15s4_3a # FPP. Same as v15s4_3, Autumn peeking from the side of the boxes to see MC, Autumn slight smile, mouth open.
            with dissolve

            au "Who- Oh! Hey, [name]! *Chuckles*"

            au "Yes, please... If you don't mind."

            scene v15s4_3b # FPP. Same as v15s4_3a, Autumn slight smile, mouth closed.
            with dissolve

            u "That's what I'm here for, haha."

            scene v15s4_3a
            with dissolve

            au "Thank you. *Laughs*"

            au "Just go ahead and take the top one. That's the heaviest anyway."

            scene v15s4_4 # TPP. Show MC grabbing the top box that Autumn is carrying, both slight smile, mouth closed.
            with dissolve
        
            pause 0.75

            scene v15s4_3c # FPP. Same as v15s4_3b, MC looking at Autumn now carrying the heavier box that Autumn was carrying, Autumn slight smile, mouth open.
            with dissolve

            au "Ahh... So much better, haha."

            u "(Damn, this is pretty heavy.)"

            scene v15s4_5 # TPP. Show MC and Autumn carrying the boxes into the reception are of the dog shelter, the reception center having no one else in it.
            with dissolve

            pause 0.75

            scene v15s4_6 # FPP. Show Autumn looking at MC as she sets the box she was carrying on the reception center desk, slight smile, mouth closed.
            with dissolve

            u "What the hell is in here? Bricks?"

            scene v15s4_6a # FPP. Same as v15s4_6, Autumn already having placed the box on the desk standing infront of the desk looking at MC, slight smile, mouth open.
            with dissolve

            au "*Grunts* Yup!"

            scene v15s4_7 # FPP. MC looking and walking towards the reception desk carrying the box
            with dissolve

            u "Wait, what?"

            scene v15s4_8 # FPP. MC putting the box up ontop of the reception desk.
            with dissolve

            pause 0.75

            scene v15s4_9 # FPP. MC looking at Autumn, Autumn looking at MC, Both not carrying a box anymore, Autumn slight smile, mouth open.
            with dissolve

            au  "Kidding. *Chuckles* It's actually a ton of coffee mugs that we plan to sell at the re-opening."

            menu:
                "You think you're funny?":
                    $ add_point(KCT.BRO)
                    scene v15s4_9a # FPP. Same as v15s4_9, Autumn slight smile, mouth closed.
                    with dissolve

                    u "Oh... *Chuckles* You think you're funny, huh?"

                    scene v15s4_9b # FPP. Same as v15s4_9, Autumn winking at MC, slight smile, mouth open.
                    with dissolve

                    au "Oh, please... I know I'm funny."

                    scene v15s4_9a
                    with dissolve

                    u "*Laughs*"

                "I want one":
                    $ add_point(KCT.BOYFRIEND)
                    $ AutumnFreeMug = True
                    scene v15s4_9a
                    with dissolve
                    
                    u "Oh, that makes sense *Laughs*"

                    u "Can I have one?"

                    scene v15s4_9
                    with dissolve

                    au "Haha, sure. Thirty bucks, though."

                    scene v15s4_9a
                    with dissolve

                    u "Thirty bucks?!"

                    scene v15s4_9
                    with dissolve

                    au "Hey, it's not cheap to run a non-profit. *Chuckles*"

                    scene v15s4_9a
                    with dissolve

                    u "Yeah, yeah... I get it."

                    scene v15s4_9
                    with dissolve

                    au "Haha, I'll give you a mug at the re-opening. Promise."

        "Say hello":
            $ add_point(KCT.BRO)
            scene v15s4_2
            with dissolve    

            u "Hey, Autumn."

            scene v15s4_2a
            with dissolve

            au "Oh! Hey, [name]. *Grunts* Thanks for coming..."

            scene v15s4_2
            with dissolve

            u "No problem, how's everything going so far?"

            scene v15s4_5a # TPP. Same as v15s4_5, Autumn carrying both boxes, MC carrying none, both slight smile, mouth closed.
            with dissolve

            pause 0.75

            play sound "sounds/slam.mp3"

            scene v15s4_6c # FPP. Same as v15s4_6, Autumn putting down both the boxes on the reception center desk, neutral face, mouth closed.
            with vpunch

            au "Oh no..."

            scene v15s4_6b # FPP. Same as v15s4_6a, Autumn looking in the box with the mugs, frustrated face, mouth closed.
            with dissolve

            u "That doesn't sound too good..."

            scene v15s4_9c # FPP. Same as v15s4_9, Autumn frustrated face, mouth open.
            with dissolve

            au "It's the sound of three broken coffee mugs... *Sighs*"

            au "It's going great so far! Can't you tell? Ha..."

            menu:
                "I'm sorry":
                    $ add_point(KCT.BOYFRIEND)
                    $ AutumnLunchBreak = True
                    scene v15s4_9d # FPP. Same as v15s4_9c, Autumn frustrated face, mouth closed.
                    with dissolve

                    u "I'm sorry, I should have-"

                    scene v15s4_9e # FPP. Same as v15s4_9d, Autumn with her eyes closed inhaling deeply, mouth open.
                    with dissolve

                    pause 0.75

                    scene v15s4_9f # FPP. Same as v15s4_9e, Autumn with her eyes closed exhaling deeply, mouth open.
                    with dissolve

                    pause 0.75

                    scene v15s4_9g # FPP. Same as v15s4_9c, Autumn neutral face, mouth open.
                    with dissolve

                    au "No, no, no... I'm sorry."

                    scene v15s4_9
                    with dissolve

                    au "This has nothing to do with you. *Chuckles* Thanks for being here."
                    
                "Just breathe":
                    $ add_point(KCT.TROUBLEMAKER)
                    $ add_point(KCT.BRO)
                    scene v15s4_9d
                    with dissolve

                    u "Just take a deep breath, haha. It's not the end of the world."

                    scene v15s4_9c
                    with dissolve

                    au "No, it's not. But it is special merchandise that we handmade to sell at the re-opening..."

                    scene v15s4_9d
                    with dissolve

                    u "Oh... Shit. Well, how much are they worth? Can you just-"

                    scene v15s4_9c
                    with dissolve

                    au "Thirty bucks, ha."

                    au "But... Yeah. I'll pay it off, don't worry."

                    scene v15s4_9d
                    with dissolve

                    u "Thirty dollars for a coffee mug?!"

                    scene v15s4_9c
                    with dissolve

                    au "Mhmm. Anyway..."

                    u "(I think she's over this conversation...)"

    scene v15s4_9a
    with dissolve

    u "So, what's first on our list of things to do?"

    scene v15s4_9
    with dissolve

    au "Our list... *Chuckles*"

    scene v15s4_9a
    with dissolve

    u "What?"

    scene v15s4_9
    with dissolve

    au "Nothing. It's just..."

    au "I'm not used to having help, I guess. I don't usually rely on other people."

    scene v15s4_9a
    with dissolve

    u "Well today, you can."

    u "So, first?"

    scene v15s4_9
    with dissolve

    au "First... Blue. Follow me."

    scene v15s4_10 # FPP. MC looking at Autum infront of one of the dog enclosures, Autumn slight smile , mouth closed.
    with fade

    pause 0.75

    scene v15s4_10a # FPP. Same as v15s4_10, Show Autumn opening the door, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s4_11 # FPP. Inside the dog enclosure looking at the dog. The dog a scrappy looking Male dog. The dog is a golden blonde color with its tongue hanging out, the dog dirty and needing to be cleaned.
    with dissolve

    u "Oh my..."

    scene v15s4_12 # FPP. Inside the dog enclosure, MC looking at Autumn, Autumn looking at the dog, Autumn slight smile, mouth open.
    with dissolve

    au "We found this little guy on the side of the road last night."

    scene v15s4_13 # FPP. MC looking at Autumn as she is down on one knee petting the dog, Autumn slight smile, mouth open.
    with dissolve

    au "Hi! Hello! *Chuckles* Cutie..."

    menu:
        "Agree":
            $ add_point(KCT.BOYFRIEND)
            scene v15s4_13a # FPP. Same as v15s4_13, Autumn slight smile, mouth closed.
            with dissolve

            u "He is adorable, not gonna lie. *Laughs*"

            scene v15s4_13
            with dissolve

            au "How could someone give up on you, bud?"

        "Flirt":
            $ add_point(KCT.BOYFRIEND)
            scene v15s4_13a
            with dissolve

            u "You? Or the dog?"

            if laurenrs:
                $ add_point(KCT.TROUBLEMAKER)
                scene v15s4_13
                with dissolve

                au "Ha. Good one, [name]. You should use it on my sister next time."

                scene v15s4_13a
                with dissolve

                u "Yeah, for sure. Ha! She'd like that..."
                
                scene v15s4_13
                with dissolve
                
                au "Hopefully we can find you a good home."

            else:
                scene v15s4_13
                with dissolve

                au "Hmm... Both?"

                scene v15s4_13a
                with dissolve

                u "Fair."

                scene v15s4_13
                with dissolve

                au "*Chuckles* Hopefully we can find you a good home."

    menu:
        "Good luck":
            $ add_point(KCT.BRO)
            scene v15s4_13a
            with dissolve

            u "Pfft, good luck with that. *Laughs*"

            scene v15s4_13b # FPP. Same as v15s4_13a, Autumn looking up at MC, Autumn slight frown, mouth open.
            with dissolve

            au "Don't be mean! He's had a hard life..."

            scene v15s4_13a
            with dissolve

            u "Yeah, I can tell. Haha."

            scene v15s4_13
            with dissolve

            au "*Whispers* I promise I'll try my best, okay?"

            scene v15s4_14 # TPP. Close up of the dog licking Autumn's nose, Autumn slight smile, mouth closed.
            with dissolve

        "We will":
            $ add_point(KCT.BOYFRIEND)
            $ mc.quirks["animal_lover"] = True
            scene v15s4_13a
            with dissolve

            u "We will, I know it."

            scene v15s4_13
            with dissolve

            au "*Chuckles* Yeah?"

            scene v15s4_13a
            with dissolve

            u "Yeah. In fact..."

            scene v15s4_15 # FPP. The MC on one knee petting the dog.
            with dissolve

            u "*Whispers* I'll make sure of it, okay?"

            scene v15s4_16 # TPP. Close up of the dog licking MC's nose, MC slight smile, mouth closed.
            with dissolve

            pause 0.75

            scene v15s4_17 # TPP. Close up of Autumn looking at MC like she adores him, Autumn smile, mouth closed.
            with dissolve

    scene v15s4_12
    with dissolve

    au "He was starving when we found him..."

    au "He already ate three servings of food throughout the night, haha."

    scene v15s4_12a # FPP. Same as v15s4_12, Autumn slight smile, mouth closed.
    with dissolve

    u "Good. Well, I mean, not good. But-"

    scene v15s4_12
    with dissolve

    au "*Laughs* I got you."

    scene v15s4_12a
    with dissolve

    u "I'm glad he's in good hands now."

    scene v15s4_12
    with dissolve

    au "Yeah, he is. Little Blue."

    scene v15s4_12a
    with dissolve

    u "Blue?"

    scene v15s4_12
    with dissolve

    au "Oh, haha. I've just been calling him that today."

    scene v15s4_12a
    with dissolve

    u "Why Blue?"

    scene v15s4_12
    with dissolve

    au "I mean, he was so sad when we found him. I instantly thought like, he's got the blues."

    scene v15s4_12a
    with dissolve

    u "*Laughs*"

    scene v15s4_12
    with dissolve

    au "What?! *Chuckles*"

    scene v15s4_12a
    with dissolve

    u "He's got the blues? Haha... That's the reason?"

    scene v15s4_12
    with dissolve

    au "Well, he also prefers his blue bone over any other toy we offer him. So-"

    scene v15s4_12a
    with dissolve

    u "Okay, next time someone asks, just start with that. *Laughs*"

    scene v15s4_12
    with dissolve

    au "*Chuckles* Okay, smartass."

    au "You think we should change it to something else?"

    menu:
        "No, don't change it":
            $ add_point(KCT.BOYFRIEND)
            scene v15s4_12a
            with dissolve

            u "No, let's not. I kinda like Blue, actually."

            scene v15s4_12
            with dissolve

            au "Good, me too."

            scene v15s4_18 # FPP. Show Autumn bending over and petting the dog.
            with dissolve

            au "Okay, Blue. I'll be back later to play with you and take you for a walk."
            
            menu:
                "Peek":
                    $ add_point(KCT.TROUBLEMAKER)
                    scene v15s4_19 # FPP. Similar to v15s4_18, Close up of Autumn's ass.
                    with dissolve

                    u "(Damn!!)"

                    if laurenrs:
                        u "(Is it weird to check out Lauren's sister?)"

                "Don't peek":
                    $ add_point(KCT.BOYFRIEND)
                    scene v15s4_18
                    with dissolve

                    u "(Glad I can control myself, good job [name]!)"
                    if laurenrs:
                        u "(It would be weird if I checked out Autumn while I'm with Lauren...)"
            
            scene v15s4_63 # FPP. MC turned around looking at the dog as him and Autumn are leaving, Autumn off-camera.
            with dissolve    

            u "Bye, Blue!"

        "Yeah, lets change it":
            $ add_point(KCT.TROUBLEMAKER)
            scene v15s4_12a
            with dissolve

            u "Yeah, I think we should."

            scene v15s4_12
            with dissolve

            au "Okay, what should we call him then?"

            label v15s4_dog:
            $ dog_name = renpy.input(_("Choose the dog's name:"), default=_("Blue")).strip() or _("Blue")

            if dog_name.lower() == "blue":
                u "(I should come up with a better name than that...)"
                jump v15s4_dog

            scene v15s4_12a
            with dissolve

            u "He looks like a [dog_name] to me."

            scene v15s4_12
            with dissolve

            au "[dog_name]? Huh..."

            au "It's weirdly perfect..."

            scene v15s4_12a
            with dissolve

            u "Right? *Chuckles*"

            scene v15s4_12
            with dissolve

            au "Okay, [dog_name], I'll be back later to play with you and take you for a walk."

            scene v15s4_18
            with dissolve

            u "Bye, [dog_name]."

    scene v15s4_20 # TPP. Show MC and Autumn leaving the dog's enclosure, the dog in the background, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s4_9a
    with fade 

    u "So, what's next?"

    scene v15s4_9
    with dissolve

    au "We have a huge banner to hang up and I could really use your help with that, so let's get it done really quick."

    scene v15s4_21 # TPP. Show Autumn and MC walking outside, both slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v15s4_22 # TPP. MC holding a ladder while Autumn is at the top of the ladder hanging up the banner, the banner says "GRAND RE-OPENING!" with pictures of dogs, bones, and paw prints on it.
    with fade

    au "Hold it tight!"

    scene v15s4_23 # TPP. Close up of just Autumn stretching out to hang up part of the banner.
    with dissolve

    menu:
        "Make a joke":
            $ add_point(KCT.BOYFRIEND)
            scene v15s4_24 # FPP. MC looking up at Autumn, Autumn not looking at MC she conversates as she is putting up the banner, Autumn slight smile, mouth closed.
            with dissolve

            u "Hey, wanna hear a joke?"

            scene v15s4_24a # FPP. Same as v15s4_24, Autumn slight smile, mouth open.
            with dissolve

            au "Ha. Okay, sure."

            scene v15s4_24
            with dissolve

            u "Did you hear about the dog that had a hangover?"

            scene v15s4_24a
            with dissolve

            au "Hmm, nope."

            scene v15s4_24
            with dissolve

            u "He said he was feeling ruff!"

            scene v15s4_24a
            with dissolve

            au "*Laughs* You owe me for having to listen to that."

        "Look at her ass":
            $ add_point(KCT.TROUBLEMAKER)
            $ add_point(KCT.BRO)
            $ AutumnLunchBreak = False
            scene v15s4_24
            with dissolve
    
            u "(I mean, how could you pass on an opportunity like this?)"

            scene v15s4_25 # TPP. Close up of Autumn's ass as she is reaching out to hang the banner on the ladder.
            with dissolve

            pause 0.75

            scene v15s4_24b # FPP. Same as v15s4_24a, Autumn looking down at MC while she is standing on the ladder, Autumn upset, mouth open
            with vpunch

            au "Hey! Eyes up, horn dog! Are you just here to enjoy the view?"

            scene v15s4_24c # FPP. Same as v15s4_24b, Autumn upset, mouth closed.
            with dissolve

            u "(Can you blame me?) Sorry, I got distracted."

            if laurenrs:
                scene v15s4_24b
                with dissolve

                au "I hope you don't act like this around my sister. *Scoffs*"

                scene v15s4_24c
                with dissolve

                u "No, I-"

    scene v15s4_24b
    with dissolve

    au "Save your words, your actions speak louder."

    scene v15s4_26 # TPP. Show Autumn climbing down the ladder slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s4_27 # TPP. Autumn and MC standing a bit back from the the Dog Shelter looking at the banner on display, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s4_28 # FPP. MC and Autumn standing where they were in v15s4_27, MC looking at Autumn, Autumn looking at MC, Autumn slight smile, mouth open.
    with dissolve

    au "We did it!"

    scene v15s4_28a # FPP. Same as v15s4_28, Autumn slight smile, mouth closed.
    with dissolve

    u "Well, you did it. I just held a ladder... Haha."

    scene v15s4_28
    with dissolve

    au "Exactly, we did great. *Chuckles* Good job."

    scene v15s4_29 # TPP. Show MC and Autumn high fiving, both slight smile, mouths closed.
    with dissolve
    
    pause 0.75

    scene v15s4_28
    with dissolve

    au "And don't worry, we're both about to do some real work. Ready?"

    scene v15s4_28a
    with dissolve

    u "As I'll ever be."

    scene v15s4_30 # TPP. Show just MC putting up a dog poster on the wall in the Shelter, slight smile, mouth closed
    with fade 

    pause 0.75

    scene v15s4_31 # TPP. Show just Autumn putting up a dog poster on the wall somewhere else in the Shelter, slight smile, mouth closed.
    with fade

    pause 0.75 

    scene v15s4_32 # TPP. Show MC and Autumn putting down a table in an empty part of the Room against the wall, neutral expression, mouth closed.
    with fade

    pause 0.75

    scene v15s4_33 # TPP. Show MC and Autumn putting chairs down in the empty space arranging a waiting area.
    with fade

    pause 0.75

    scene v15s4_34 # FPP. MC and Autumn standing in the waiting area they just made, Autumn looking at MC, MC looking at Autumn, Autumn slight smile, mouth open.
    with dissolve

    au "That looks pretty good, yeah?"

    scene v15s4_34a # FPP. Same as v15s4_34, Autumn slight smile, mouth closed.
    with dissolve

    u "Yeah, it looks cozy."

    scene v15s4_35 # TPP. Show MC struggling to carry a potted plant while Autumn is sitting down pointing to a spot in the corner near the table and chairs, MC exhausted face, mouth closed, Autumn slight smile, mouth closed.
    with fade

    pause 0.75

    scene v15s4_36 # TPP. Show just MC putting down the potted plant in the corner, MC exhausted face, mouth closed
    with dissolve

    pause 0.75

    scene v15s4_37 # FPP. MC standing infront of Autumn who is sitting down in a chair, Autumn looking up at MC, Autumn slight smile, mouth closed.
    with dissolve

    u "Okay... *Panting* Now I'm sweating."

    scene v15s4_37a # FPP. Same as v15s4_37, Autum slight smile, mouth open.
    with dissolve

    au "*Chuckles* You can relax a little. I saved the least physical task for last..."

    scene v15s4_37
    with dissolve

    u "Oh, no. It can't be worse than a two-hundred-pound potted plant, can it?"

    scene v15s4_37a
    with dissolve

    au "No, haha. It's the lightest thing ever, actually..."

    scene v15s4_37b # FPP. Same as v15s4_37a, Autumn reaching into her pocket, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s4_37c # FPP. Same as v15s4_37b, Autumn looking at MC and holding a bag of balloons, slight smile, mouth open.
    with dissolve

    au "Balloons!"

    scene v15s4_37
    with dissolve

    u "*Chuckles* Okay, that works. I can do balloons."

    scene v15s4_38 # TPP. Autumn and MC sitting next to each other, a few already blown up balloons on the floor, both blowing up balloons.
    with fade

    pause 0.75

    scene v15s4_23a # TPP. Same as v15s4_23, Autumn putting balloons on the banner, slight smile, mouth closed.
    with fade

    pause 0.75

    scene v15s4_38a # TPP. Same as v15s4_38, More balloons on the floor, Autumn and MC putting strings on balloons, both slight smile, mouth closed.
    with fade

    pause 0.75

    scene v15s4_39 # FPP. MC sitting looking up at Autumn, Autumn now standing up with her back turned to MC, putting a string on a balloon.
    with dissolve

    u "(Hmm... I could give her a good scare right now...)"

    menu:
        "Pop a balloon":
            $ add_point(KCT.TROUBLEMAKER)
            $ mc.quirks["prankster"] = True
            scene v15s4_40 # FPP. MC behind Autumn, holding a tack/pen/scissors(whatever we have available) and a balloon by Autumn's ear, Autumn unaware with her back turned.
            with dissolve

            pause 0.75

            play sound "sounds/slap.mp3"

            scene v15s4_40a # FPP. Same as v15s4_40, MC pushing the item into the balloon and popping it by Autumn's ear.
            with dissolve

            pause 0.75

            scene v15s4_40b # FPP. Same as v15s4_40a, Autumn's head turned to the side a little from the loud noise, her face visible to MC, Autumn scared, mouth open.
            with dissolve

            au "*Gasps* You-"

            scene v15s4_40c # FPP. Same as v15s4_40b, Autumn turned around and looking at MC now, Autumn slight smile, mouth open.
            with dissolve

            au "You fucker! *Laughs*"

            scene v15s4_40d # FPP. Same as v15s4_40c, Autumn slight smile, mouth closed.
            with dissolve

            u "*Laughs* That was too easy."

            scene v15s4_40c
            with dissolve

            au "Oh, okay... Go ahead."

            au "Laugh all you want now, but I'll get my revenge [name]. You better learn how to sleep with one eye open."

            scene v15s4_40d
            with dissolve

            u "I always sleep with one eye open. *Chuckles*"

            scene v15s4_40c
            with dissolve

            au "*Laughs* You're so annoying."
            
        "Don't pop a balloon":
            $ add_point(KCT.BOYFRIEND)
            u "(Not worth the chance of getting accidentally punched in the face...)"

            scene v15s4_41 # TPP. Show MC with his back turned to Autumn looking at the balloons on the floor, both slight smile, mouth open.
            with dissolve

            pause 0.75

            scene v15s4_41a # TPP. Show Autumn popping a balloon next to MC's ear, Autumn slight smile, mouth closed, MC scared, mouth open.
            with dissolve

            pause 0.75

            scene v15s4_40d
            with dissolve

            u "Agh! What the-"

            scene v15s4_40c
            with dissolve

            au "Haha! That was the saddest scream I've ever heard! *Laughs*"

            scene v15s4_40d
            with dissolve

            u "You... Little shit. *Chuckles* You're dead to me."

            scene v15s4_40c
            with dissolve

            au "That's fine, I can die happily after witnessing that. Haha! Phew..."

            scene v15s4_40d
            with dissolve

            u "Get back to work."

    scene v15s4_40c
    with dissolve

    au "Okay, okay... back to work."

    scene v15s4_42 # FPP. MC looking at the area they just created with no balloons on the floor, balloons scattered around the room into decoration.
    with fade

    u "Alrighty..."

    scene v15s4_43 # FPP. In the decorated area, Autumn looking at MC, MC looking at Autumn, Autumn slight smile, mouth open.
    with dissolve

    au "That's it?"

    scene v15s4_43a # FPP. Same as v15s4_43, Autumn slight smile, mouth closed.
    with dissolve

    u "That's it! Let's have a look."

    scene v15s4_44 # TPP. MC and Autumn standing next to each other looking at the room, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s4_43a
    with dissolve

    u "Great job! Seriously, you're really good at this."

    scene v15s4_43
    with dissolve

    au "Haha, thank you. I appreciate your help."

    scene v15s4_43a
    with dissolve

    u "I can see why you're President of the Deer. *Chuckles*"

    scene v15s4_43
    with dissolve

    au "Oh, yeah. It's a lot of work, but it's rewarding. I have fun and I learn a lot."

    scene v15s4_43a
    with dissolve

    u "For sure, it looks super stressful."

    scene v15s4_43
    with dissolve

    au "It definitely can be, but not as stressful as the Chicks make it seem, haha."

    scene v15s4_43a
    with dissolve

    u "Haha, that's good to hear. It's crazy out there right now... Who do you think will win?"

    scene v15s4_43
    with dissolve

    au "The strongest candidate. *Laughs* That seems like such a shit answer, but honestly..."

    au  "Whoever deserves it the most will end up being President. Let the voters speak!"

    scene v15s4_43a
    with dissolve

    u "That's a very diplomatic way of putting it. *Chuckles*"

    scene v15s4_43
    with dissolve

    au "Hey, I didn't get to where I am today without these amazing diplomacy skills."

    scene v15s4_43a
    with dissolve

    u "I can see that, haha. It just makes me wonder what you're really thinking."

    scene v15s4_43
    with dissolve

    au "*Laughs* Maybe you'll find out one day."

    scene v15s4_43a
    with dissolve

    u "Hmm... Maybe..."

    scene v15s4_45 # TPP. Close up of Oscar the dog and his owner walking into the shelter, Oscar's owner slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s4_45a # TPP. Same as v15s4_45, Oscar and his Owner walking to MC and Autumn.
    with dissolve

    pause 0.75

    scene v15s4_43b # FPP. Show Autumn facing and looking over and Oscar and his owner, slight smile, mouth open.
    with dissolve

    au "Oh, hello! Wait, it's Oscar!"

    scene v15s4_46 # FPP. Autumn on one knee petting Oscar, Autumn slight smile, mouth open.
    with dissolve

    au  "Hey, little guy..."

    scene v15s4_46a # FPP. Same as v15s4_46, Autumn slight smile, mouth closed.
    with dissolve

    u "I haven't seen you in a while, bud. Lookin' good!"

    scene v15s4_47 # FPP. Show Oscar the dog running away from Autumn towards MC excitedly, Autumn slight smile, mouth closed.
    with dissolve

    au "I think he remembers you! Haha, that's so cute..."

    scene v15s4_48 # FPP. MC on one knee and petting Oscar who is at his feet, don't show any other characters legs just MC's hand and Oscar.
    with dissolve

    u "*Chuckles* How are you, buddy? Good?"

    scene v15s4_43b
    with dissolve

    au "And hello Mr... Um, Oscar's owner..."

    au "How are you guys?"

    scene v15s4_49 # FPP. MC standing back up and looking up at Oscar's Owner,Oscar's owner looking at Autumn, Oscar's owner neutral face, mouth open.
    with dissolve

    oscars_owner "Actually... I'm sorry I have to do this, but I'm here to give Oscar back."

    scene v15s4_43c # FPP. Same as v15s4_43b, Autumn looking at Oscar's owner, Autumn confused, mouth open,
    with dissolve

    au "Wha- Give back?! I... Why?"

    scene v15s4_49
    with dissolve

    oscars_owner "Long story short, I'm moving upstate to take over my grandpa's farm."

    u "(And?)"

    oscars_owner "It's not exactly the best place for Oscar."

    scene v15s4_49a # FPP. Same as v15s4_49, Oscar's owner looking at MC, Oscar's owner neutral face, mouth closed.
    with dissolve

    u "What do you mean? Ha, a farm is one the most ideal places for a dog to live... Right?"

    scene v15s4_43i # FPP. Same as v15s4_43c, Autumn's body facing towards Oscar's owner, Autumn looking at MC, Autumn confused, mouth open,
    with dissolve

    au "Exactly."

    scene v15s4_49
    with dissolve

    oscars_owner "Yeah, except this is a weed farm..."

    scene v15s4_43c
    with dissolve

    au "Oh, well-"

    scene v15s4_49
    with dissolve

    oscars_owner "And he likes weed. Like, a lot. So-"

    scene v15s4_43c
    with dissolve

    au "What do you mean he... How do you... Huh?"

    scene v15s4_49a
    with dissolve

    u "You gave him weed!?"

    scene v15s4_49b # FPP. Same as v15s4_49a, Oscar's owner looking at MC, Neutral face, mouth open.
    with dissolve

    oscars_owner "I didn't exactly give it to him, no... It was an accident."

    scene v15s4_43c
    with dissolve

    au "Say no more. Just, go. Please go."

    scene v15s4_50 # TPP. Show Oscar's owner walking out of the shelter, waving while he exits.
    with dissolve

    pause 0.75

    scene v15s4_43d # FPP. Same as v15s4_43c, Autumn looking down at Oscar, Autumn upset, mouth open.
    with dissolve

    au "*Sighs* My poor little Oscar..."

    au "What did he do to you, huh? Are you okay?"

    scene v15s4_43e # FPP. Same as v15s4_43d, Autumn upset, mouth closed.
    with dissolve

    u "He looks alright, thankfully."

    scene v15s4_43d
    with dissolve

    au "Yeah, but look at this face, [name]. He doesn't even know what just happened."

    au "You're not alone, bud. It might feel like it, but you aren't."

    scene v15s4_43f # FPP. Same as v15s4_43d, Autumn wiping away a tear, Autumn upset, mouth closed.
    with dissolve

    u "(She's really torn up about this...)"

    menu:
        "Threaten Oscar's owner":
            $ add_point(KCT.TROUBLEMAKER)
            $ mc.quirks["hardass"] = True
            scene v15s4_43g # FPP. Autumn looking at MC, Autumn upset, mouth closed.
            with dissolve

            u "You know, he was most likely lying about that whole weed farm story. I can catch up with him and fuck him up if you-"

            scene v15s4_43h # FPP. Autumn upset, mouth open.
            with dissolve

            au "No, no... Please don't do that, ha. It's okay."

            scene v15s4_43g
            with dissolve

            u "You sure?"

            scene v15s4_43h
            with dissolve

            au "Yeah, I'm sure. I mean, thanks for offering, but this kind of thing happens every day. Some people just can't handle the responsibility when it comes down to it."

            scene v15s4_43g
            with dissolve

            u "If only they'd realize that before they chose to adopt..."

            scene v15s4_43
            with dissolve
            
            au "Hopefully we can find the perfect owner for him at the re-opening."

        "Comfort Oscar":
            $ add_point(KCT.BOYFRIEND)
            scene v15s4_48
            with dissolve

            u "You're honestly better off without that guy, bud. *Laughs* You'll find your forever home soon."

            au "Ha, yeah. He will."

            u "Are you hungry? Want some food?"

            scene v15s4_51 # TPP. Show Oscar hopping up and licking MC's face, MC slight smile, mouth closed.
            with dissolve

            pause 0.75

            scene v15s4_43
            with dissolve

            au "I think he likes you..."

            scene v15s4_43a
            with dissolve

            u "*Chuckles* Too bad I can't take you back to campus with me."

            scene v15s4_43
            with dissolve

            au "Ugh, I know right. That's the only downside of working here, haha."

            au "Hopefully we can find the perfect owner for him at the re-opening."

    scene v15s4_43a
    with dissolve

    u "I'm sure we will."

    if not AutumnLunchBreak:
        scene v15s4_43
        with dissolve

        au "Alright, I better get him fed and bathed before I go on break. I'm due for some \"me time\" *Laughs*"

        scene v15s4_43a
        with dissolve

        u "Yeah, you deserve a break at the very least, haha."

        scene v15s4_43
        with dissolve

        au "Thanks again for all your help today."

        scene v15s4_43a
        with dissolve

        u "Oh, sure thing. It wasn't a bad start to my day, so thank you as well."

        scene v15s4_52 # TPP. Autumn and MC hugging, both slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s4_43
        with dissolve

        au "I'll see you later at Lauren's party, right?"

        scene v15s4_43a
        with dissolve

        u "Yeah! See you there."

        scene v15s4_53 # TPP. Show MC walking out of the Dog Shelter waving as he goes, Autumn and Oscar watching him leave.
        with dissolve

    else:
        scene v15s4_43
        with dissolve

        au  "Alright, well... I'm gonna go put him in a cozy spot with some fresh food and water, but I think we've earned a break. Don't you?"

        scene v15s4_43a
        with dissolve

        u "I'd have to agree."

        scene v15s4_43
        with dissolve

        au "Great, just wait for me in the parking lot."

        scene v15s4_43a
        with dissolve

        u "Can do."

        scene v15s4_54 # TPP. Show MC standing in the parking lot of the dog shelter waiting/
        with fade

        pause 0.75

        scene v15s4_55 # FPP. MC waiting for Autumn in the parking lot.
        with dissolve

        u "(Got a pretty good workout this morning. Almost as good as the gym, haha.)"

        au "Hey, weirdo! Over here!"

        scene v15s4_56 # FPP. MC looking to his side and seeing Autumn stood by her car, Autumn slight smile, mouth open.
        with dissolve

        au "Come on!"

        scene v15s4_57 # FPP. MC further ahead from where he was walking towards Autumn who is starting to get in the car.
        with dissolve

        pause 0.75

        scene v15s4_58 # FPP. MC getting in the passenger seat, Autumn sitting in the driver seat with her door closed.
        with dissolve

        pause 0.75

        scene v15s4_59 # FPP. MC sitting in the passenger seat with his door closed, looking at Autumn in the driver seat, Autumn looking at MC, Autumn slight smile, mouth closed.
        with dissolve

        u "Where are we going?"

        scene v15s4_59a # FPP. Same as v15s4_59, Autumn slight smile, mouth open.
        with dissolve

        au "Nowhere, haha. Just getting some peace and quiet..."

        scene v15s4_59b # FPP. Same as v15s4_59a, Show Autumn pulling out a joint and fancy lighter from her pocket, Autumn slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s4_59c # FPP. Same as v15s4_59b, Show Autumn holding the joint with her lips and lighting it.
        with dissolve

        u "Oh, I see. *Chuckles* Wow, that's kinda surprising."

        scene v15s4_59d # FPP. Same as v15s4_59c, Autumn holding the joint in her hand and looking at MC, smoke coming off the joint, Autumn slight smile, mouth open..
        with dissolve

        au "What is?"

        scene v15s4_59e # FPP. Same as v15s4_59c, Autumn taking a big toke of the joint.
        with dissolve

        u "I had no idea you were a stoner. *Laughs*"

        scene v15s4_59d
        with dissolve

        au "*Chuckles* Yeah... No one has any idea what I am."

        scene v15s4_59f # FPP. Same as v15s4_59d, Autumn looking at MC holding the joint, smoke coming off the joint, Autumn slight smile, mouth closed.
        with dissolve

        u "Ha... (I wonder what she means by that?)"

        scene v15s4_59d
        with dissolve

        au "Want a hit?"

        menu:
            "Smoke weed":
                $ add_point(KCT.TROUBLEMAKER)
                $ smoked_with_autumn = True
                scene v15s4_59f
                with dissolve

                u "Yeah, thanks."

                scene v15s4_59g # FPP. Same as v15s4_59f, Autumn holding out the joint for MC, Autumn slight smile, mouth closed.
                with dissolve

                pause 0.75

                scene v15s4_59h # FPP. Same as v15s4_59g, MC taking the joint from Autumn, Autumn slight smile, mouth closed.
                with dissolve

                pause 0.75

                scene v15s4_60 # TPP. Show MC in the car taking a big puff of the joint.
                with dissolve

                pause 0.75

                scene v15s4_60a # TPP. Same as v15s4_60, MC blowing out the smoke.
                with dissolve

                pause 0.75

                scene v15s4_59h
                with dissolve

                pause 0.75

                scene v15s4_59g
                with dissolve
                
                pause 0.75

                scene v15s4_59f
                with dissolve

                u "*Inhaling* This is a nice bonding experience... Haha."

            "Don't smoke weed":
                $ add_point(KCT.BOYFRIEND)
                scene v15s4_59f
                with dissolve

                u "Ah, no thanks. Need to stay clean for fighting."

                scene v15s4_59d
                with dissolve

                au "Hey, no judgment here. More for me, hehe."

        scene v15s4_59e
        with dissolve

        pause 0.75

        scene v15s4_59f
        with dissolve

        u "You do this a lot on break?"

        scene v15s4_59d
        with dissolve

        au "You said it yourself, [name]. Being President is stressful. *Chuckles*"

        scene v15s4_59f
        with dissolve

        u "Ahhh... So, the key to being the perfect president is marijuana?"

        scene v15s4_59d
        with dissolve

        au "*Laughs* Sure, yeah. Let's go with that..."

        if smoked_with_autumn:
            scene v15s4_59g # FPP. Same as v15s4_59f, Autumn holding out the joint for MC, Autumn slight smile, mouth closed.
            with dissolve

            pause 0.75

            scene v15s4_59h # FPP. Same as v15s4_59g, MC taking the joint from Autumn, Autumn slight smile, mouth closed.
            with dissolve

            pause 0.75

            scene v15s4_60 # TPP. Show MC in the car taking a big puff of the joint.
            with dissolve

            pause 0.75

            scene v15s4_60a # TPP. Same as v15s4_60, MC blowing out the smoke.
            with dissolve

            pause 0.75

            scene v15s4_59h
            with dissolve

            pause 0.75

            scene v15s4_59g
            with dissolve
            
            pause 0.75

            scene v15s4_59f
            with dissolve

            pause 0.75

            scene v15s4_59i # FPP. Same as v15s4_59h, Show Autumn pinching off the end of the joint for later, Autumn slight smile, mouth closed
            with dissolve

            pause 0.75

            scene v15s4_59j # FPP. Same as v15s4_59i, Show Autumn putting away the joint and lighter into her pocket, Autumn slight smile, mouth closed.
            with dissolve

            pause 0.75

        else: 
            scene v15s4_59i # FPP. Same as v15s4_59h, Show Autumn pinching off the end of the joint for later, Autumn slight smile, mouth closed
            with dissolve

            pause 0.75

            scene v15s4_59j # FPP. Same as v15s4_59i, Show Autumn putting away the joint and lighter into her pocket, Autumn slight smile, mouth closed.
            with dissolve

            pause 0.75
        
        scene v15s4_59a
        with dissolve

        au "So, I assume you're coming to Lauren's party tonight?"

        scene v15s4_59
        with dissolve

        u "Oh, yeah! I'm kind of looking forward to it..."

        scene v15s4_59a
        with dissolve

        au "Me too, I need a fun night."

        scene v15s4_59
        with dissolve

        u "Actually, you might be able to help me with something..."

        scene v15s4_59a
        with dissolve

        au "Well, after today I definitely owe you one... So, what is it?"

        scene v15s4_59
        with dissolve

        u "I have a few ideas already, but do you have any birthday gift suggestions?"

        scene v15s4_59a
        with dissolve

        au "Hmm... Good question."

        scene v15s4_59
        with dissolve

        u "I know, thanks."

        scene v15s4_59a
        with dissolve

        au "Ha... I remember when we were young, she had this little toy horse that she would take everywhere. I don't think we have any family photos where she isn't holding it... *Chuckles*"

        scene v15s4_59
        with dissolve

        u "*Laughs* That's cute."

        scene v15s4_59a
        with dissolve

        au "It was brown, with light golden hair on it's mane. She had this dream of owning a real horse just like it when she got older."

        scene v15s4_59
        with dissolve

        u "You're suggesting that I buy your sister a horse?"

        scene v15s4_59a
        with dissolve

        au "*Laughs* What? Is that impossible or something?"

        scene v15s4_59 
        with dissolve

        u "I-"

        scene v15s4_59a
        with dissolve

        au "I'm kidding, haha. No, not a real horse, a toy one."

        au "When we moved out of our childhood home it ended up getting lost somewhere along the way."

        au "So, If you found something similar to that, she'd probably die. *Laughs*"

        if laurenrs:
            au "But she's never gotten jewellery from a boyfriend before, and she's always mentioning that. So, either way I think you're good."

        scene v15s4_59
        with dissolve

        u "That's really helpful. Thanks, Autumn."

        scene v15s4_59a
        with dissolve

        au "For sure. I've enjoyed spending time with you more than I thought I would. *Chuckles*"

        scene v15s4_59
        with dissolve

        u "Haha, thank you. I think..."

        scene v15s4_59a
        with dissolve

        au "You're so welcome. *Laughs*"

        scene v15s4_59
        with dissolve

        u "I better start heading to campus, see you later?"

        scene v15s4_59a
        with dissolve

        au "Yeah, I'll see you tonight! Bye, [name]."

        scene v15s4_61 # TPP. Show MC getting out of Autumn's car, MC slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s4_62 # TPP. Show MC a bit away from the car walking towards campus, slight smile, mouth closed.
        with dissolve

        pause 0.75

        if msrosers:
            jump v15s5
        else:
            jump v15s6