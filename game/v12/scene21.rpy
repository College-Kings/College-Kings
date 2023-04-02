# SCENE 21: Exploring with Nora
# Locations: Factory, Sidewalk, Hotel Lobby, Hotel Room Corridor, Hotel Room
# Characters: MC (Outfit: 9), NORA (Outfit: 1), CRAZY LADY (Outfit: 1), AUBREY (Outfit: 1), IMRE (Outfit: 2)
# Time: Evening
# Phone Images: None

label v12_nora_exploring:
    scene v12noe1 # TPP. Show MC midway through sitting down on the concrete block, Nora midway through sitting on the ground, both slight smiles, mouths closed
    with dissolve

    pause 0.75

    play music "music/v12/Track Scene 21_1.mp3" fadein 2

    scene v12noe2 # FPP. MC sitting on the concrete block, Nora sitting on the ground. Both of them looking at each other, Nora slight smile, mouth closed
    with dissolve

    u "So, what'd you bring?"

    scene v12noe2a # FPP. Same as v12noe2, Nora slight smile, mouth open
    with dissolve

    no "Nothing too fancy."

    scene v12noe2b # FPP. Same as v12noe2, Nora grabbing a drink from her bag, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v12noe2c # FPP. Same as v12noe2b, Nora handing the drink to MC, Nora slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v12noe2d # FPP. Same as v12noe2, Nora holding the drink, slight smile, mouth open
    with dissolve

    no "Ahh... The sun feels so nice on my face..."

    scene v12noe2e # FPP. Same as v12noe2, Nora's drink on the ground next to her as she is removing her top, she has a bra on, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v12noe2f # FPP. Same as v12noe2e, Nora in her bra, Nora leaning back, slightly worried, mouth open
    with dissolve

    no "Oh shit, you don't mind me taking my top off do you? Sorry..."

    scene v12noe2g # FPP. Same as v12noe2f, Nora slightly worried, mouth closed
    with dissolve

    menu:
        "Not at all":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            scene v12noe2h # FPP. Same as v12noe2f, Nora taking a sip of her drink
            with dissolve

            u "No, not at all. *Chuckles* You're good."

        "A little surprising...":
            $ reputation.add_point(RepComponent.BRO)
            scene v12noe2i # FPP. Same as v12noe2f, Nora slight smile, mouth closed
            with dissolve

            u "I mean no, not really. But you did surprise me a little bit..."

            scene v12noe2j # FPP. Same as v12noe2j, Nora slight smile, mouth open
            with dissolve

            no "Just imagine I'm in a bikini, yeah?"

            scene v12noe2h
            with dissolve

            u "Haha, right. Okay. *Chuckles*"

    scene v12noe2g
    with dissolve

    u "*Deep breath* Is Europe turning out to be everything you dreamed it would?"

    scene v12noe2f
    with dissolve

    no "Yes and no..."

    scene v12noe2k # FPP. Same as v12noe2f, different pose
    with dissolve

    no "I think I might just do a poor job of realizing that we aren't in a fairytale land."

    scene v12noe2l # FPP. Same as v12noe2k, Nora slightly worried, mouth closed
    with dissolve

    u "Hey, I mean... It's definitely nice to believe that the grass is greener on the other side."

    scene v12noe2k
    with dissolve

    no "Yet it usually never is."

    scene v12noe2l
    with dissolve

    u "Right... But just because your problems followed you, doesn't mean the place itself isn't amazing."

    scene v12noe2k
    with dissolve

    no "I mean, Europe's been great, I'm not gonna lie. There's been a lot I wanted to see that I got to see and I got a little of a vacation."
    no "I just didn't get to escape every problem like I expected to, but maybe it was immature to think I could."

    scene v12noe2h
    with dissolve

    u "It's not immature, just impossible. This wasn't just you on vacation by yourself. Chris and Chloe came so, your problems with him and your problems with the Chicks followed you."

    scene v12noe2f
    with dissolve

    no "Yeah, you're right. And seriously sucks that this factory is all messed up. The Mahoo article said nothing about it being closed... *Sighs*"

    scene v12noe2i
    with dissolve

    u "Mahoo?! *Laughs* Who even uses that anymore. That's a dead search engine."

    scene v12noe2j
    with dissolve

    no "Yeah, it must be. 'Cause this place is a whole fuckin' mess. *Chuckles*"

    scene v12noe2i
    with dissolve

    u "Well, just because it's a mess doesn't mean we can't check it out..."

    scene v12noe1a # TPP. Same as v12noe1, Show MC getting up, looking into the factory, Nora sitting on the ground, both slight smiles, mouths closed
    with dissolve

    pause 0.75

    scene v12noe3 # FPP. Show MC looking into the factory
    with dissolve

    u "Okay, nevermind. There's nothing in there worth checking out."

    scene v12noe4 # TPP. Show the crazy lady charging MC, MC startled, mouth closed, lady angry, mouth closed
    with dissolve

    pause 0.75

    scene v12noe5 # FPP. Crazy lady standing in front of MC, both of them looking at each other, lady angry, mouth closed
    with dissolve

    u "WHAT THE FUCK?!"

    scene v12noe5a # FPP. Same as v12noe5, lady angry, mouth open
    with dissolve

    clady "GET OUT OF MY HOUSE! Va t'en! Va t'en!"

    scene v12noe4a # TPP. Same as v12noe4, lady hitting MC as he tries to block. MC and lady both angry, lady mouth closed, MC mouth open
    with dissolve

    u "Whoa- Chill! CHILL! Please lady, chill... What the fuck is wrong with you?"

    scene v12noe4b # TPP. Same as v12noe4a, Nora pushing the lady away from MC, MC angry, mouth closed, Nora mouth open, angry, lady angry, mouth closed
    with dissolve

    no "What is wrong with you?!"

    scene v12noe6 # FPP. Same positioning as v12noe5, Nora standing next to MC, Nora looking at MC, worried, mouth open, she has her hands on his face
    with dissolve

    no "Are you okay?!"

    scene v12noe6a # FPP. Same as v12noe6, Nora worried, mouth closed
    with dissolve

    u "Yeah I'm fine... Thanks."

    scene v12noe6b # FPP. Same as v12noe6, Nora looking at the crazy lady, Nora angry, mouth open, Nora no longer with her hands on MC
    with dissolve

    no "Why did you just attack him?"

    scene v12noe5b # FPP. Same as v12noe5, lady angry, mouth open, looking at Nora
    with dissolve

    clady "Because you kids are messing around in my damn house!"

    scene v12noe6b
    with dissolve

    no "This is an abandoned factory, how could this possibly be your home?"

    scene v12noe5b
    with dissolve

    clady "I claimed this land... Now be gone! Before I call upon my troops to destroy you..."

    scene v12noe6c # FPP. Same as v12noe6, Nora no longer with her hands on MC, Nora slight smile, mouth closed
    with dissolve

    u "*Whisper* Okay, this bitch is officially crazy."

    scene v12noe6d # FPP. Same as v12noe6c, Nora slight smile, mouth open
    with dissolve

    no "*Whisper* You didn't think that when she attacked you?"

    scene v12noe6c
    with dissolve

    u "*Whisper* Now I know for sure."

    scene v12noe5a
    with dissolve

    clady "Va t'en!"

    scene v12noe6b
    with dissolve

    no "We don't speak French!"

    scene v12noe5b
    with dissolve

    clady "LEAVEEEEEEE!!!"

    scene v12noe5
    with dissolve

    menu:
        "Speak her language":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            scene v12noe6c
            with dissolve

            u "*Whisper* You should try speaking her language?"

            scene v12noe6d
            with dissolve

            no "*Whisper* French?"

            scene v12noe6c
            with dissolve

            u "*Whisper* No, crazy."

            scene v12noe6d
            with dissolve

            no "*Whisper* You just wanna see me look stupid."

            scene v12noe6c
            with dissolve

            u "*Whisper* Maybe. *Chuckles*"

            scene v12noe6e # FPP. Same as v12noe6d, Nora slightly annoyed, mouth open
            with dissolve

            no "Ugh! This fucking trip..."

            scene v12noe6b
            with dissolve

            no "Look lady, your home has been chosen for inspection by King [name]."

            if nora.relationship >= Relationship.LIKES:
                scene v12noe6b
                with dissolve

                no "I am his wife, Queen Nora."

            scene v12noe5c # FPP. Same as v12noe5, lady worried, mouth closed
            with dissolve

            u "The King has finished his inspection and we will be leaving now."

            scene v12noe5d # FPP. Same as v12noe5c, lady worried, mouth open
            with dissolve

            clady "*British accent* Wait, your majesty. Might you stay for a cup of tea?"

            scene v12noe6c
            with dissolve

            u "*Whisper* Did she just get a British accent? *Chuckles*"

            scene v12noe6b
            with dissolve

            no "I'm sorry but, we can't stay. We have other homes to inspect... And the king forbids you from attacking anyone else, understand?"

            scene v12noe5e # FPP. Same as v12noe5b, lady worried, mouth open
            with dissolve

            clady "Yes... So sorry my lady, I'll punish myself appropriately..."

            scene v12noe6f # FPP. Same as v12noe6b, Nora slightly smiling, mouth open
            with dissolve

            no "Oh- no! Th-That won't be necessary. *Chuckles*"

            scene v12noe5f # FPP. Same as v12noe5e, lady slightly smiling, mouth open
            with dissolve

            clady "You're... so kind! Thank you! Thank you..."

        "Tell her off":
            $ reputation.add_point(RepComponent.BRO)
            scene v12noe6g # FPP. Same as v12noe6e, Nora slightly annoyed, mouth closed
            with dissolve

            u "*Whisper* Oooo, I think you made her angry. You just gonna let her talk to you like that?"

            scene v12noe6b
            with dissolve

            no "*Scoffs* Look lady, it's obvious that you're homeless and probably just need some help."

            scene v12noe5b
            with dissolve

            clady "I'm not homeless, you're on my lawn right now! Take your wife and leave this instant."

            if nora.relationship >= Relationship.LIKES:
                scene v12noe6d
                with dissolve

                no "His wife..."

                scene v12noe6b
                with dissolve
                
                no "Will leave when she wants."

            else:
                scene v12noe6b
                with dissolve

                no "I'm not his wife and I'm not your daughter, so don't think you can just order me around."

            scene v12noe5b
            with dissolve

            clady "Don't make me call the army! My husband is the commander."

    scene v12noe6d
    with dissolve

    no "Okay... Let's go, [name]. Quickly... *Chuckles*"

    scene v12noe7 # TPP. Show Nora putting her shirt back on, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v12noe8 # TPP. Show Nora grabbing her bag and pulling MC by the arm as they walk away from the crazy lady, both slightly smiling, mouths closed, lady angry, gesticulating at them in the background, mouth closed
    with dissolve

    pause 0.75

    scene v12noe9 # TPP. Show MC and Nora walking through the streets, both slightly smiling, mouths closed
    with fade

    pause 0.75

    if nora.relationship >= Relationship.LIKES:
        scene v12noe10 # FPP. Nora and MC stop walking, they're on the sidewalk, looking at each other, Nora slight smile, avoiding eye contact, blushing, mouth closed
        with dissolve

        u "So... You're my wife now? *Chuckles*"

        scene v12noe10a # FPP. Same as v12noe10, Nora looking at MC, Nora slight smile, mouth open
        with dissolve

        no "*Chuckles* I said a lot of things to that crazy lady, don't read to far into it."

        scene v12noe10b # FPP. Same as v12noe10a, Nora slight smile, mouth closed
        with dissolve

        u "Alright..."

    else:
        scene v12noe10b
        with dissolve

        u "You were so brave, I don't know what I would've done if you weren't there... My hero!"

        scene v12noe10a
        with dissolve

        no "Very funny but honestly, you gotta start being careful. I won't always be there to save you. *Chuckles*"

        scene v12noe10b
        with dissolve

        u "*Laughs* Okay, got it."

    scene v12noe11 # TPP. Show MC and Nora walking close to the hotel, both slightly smiling, mouths closed
    with fade

    pause 0.75

    scene v12noe12 # TPP. Show MC and Nora walking into the hotel lobby, both slightly smiling, mouths closed
    with dissolve

    pause 0.75

    scene v12noe13 # TPP. Show MC and Nora walking through the hotel lobby, towards the rooms, both slightly smiling, mouths closed
    with dissolve

    pause 0.75

    scene v12noe14 # TPP. Show MC and Nora walking through the hotel room corridor, both slightly smiling, mouths closed
    with dissolve

    pause 0.75

    scene v12noe15 # TPP. Show MC and Nora entering Aubrey's hotel room, both slightl smiling, mouths closed
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v12/Track Scene 21_2.mp3" fadein 2

    scene v12noe16 # FPP. MC and Nora standing next to each other in the room, Aubrey lying on her bed, with her phone, Imre drunk sitting on the floor, MC looking at Aubrey, Aubrey looking at MC, Aubrey slight smile, mouth open (Only Aubrey in shot)
    with dissolve

    u "Hey, hey. We made it back."

    scene v12noe17 # FPP. Same positioning as v12noe17, MC looking at Nora, Nora looking at MC, Nora slight smile, mouth open
    with dissolve

    no "Barely..."

    scene v12noe16
    with dissolve

    u "*Laughs* How are you feeling, Aubrey?"

    scene v12noe16a # FPP. Same as v12noe16, Aubrey slight smile, mouth open
    with dissolve

    au "A lot better. Imre massaged my ankle for me, but he's been drinking so much I doubt he remembers. *Chuckles*"

    scene v12noe18 # FPP. Same positioning as v12noe16, MC looking at Imre, Imre looking at Aubrey, Imre drunk, smiling, mouth open
    with dissolve

    imre "*Drunk* I do rememberrr!"

    scene v12noe18a # FPP. Same as v12noe18, Imre looking as MC, Imre drunk, smiling, mouth open
    with dissolve

    imre "*Loud drunk whisper* She has such pretty feet..."

    scene v12noe17a # FPP. Same as v12noe17, Nora looking at Imre, Nora smiling, mouth open
    with dissolve

    no "*Laughs* Wow..."

    scene v12noe16
    with dissolve

    u "Well, alright then. *Chuckles* Just wanted to make sure you were doing good."

    scene v12noe16a
    with dissolve

    au "*Laughs* Yeah, thank you. Did you guys have fun?"

    scene v12noe16
    with dissolve

    u "I did, I don't know about Nora though. *Chuckles*"

    scene v12noe16a
    with dissolve

    au "*Chuckles* Oh no... What happened?"

    scene v12noe16
    with dissolve

    u "I'll let her tell you all about it. Later guys."

    scene v12noe17
    with dissolve

    no "Bye [name], thanks for hanging with me."

    scene v12noe17b # FPP. Same as v12noe17, Nora slight smile, mouth closed
    with dissolve

    u "Anytime."

    scene v12noe19 # TPP. Show MC leaving the hotel room and going to the hallway, slight smile, mouth closed
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v12_riley_room #scene 22