# SCENE 18: Lauren Halloween Party Arrival
# Locations: Deer's House
# Characters: MC (Outfit: Stripper Costume), LAUREN (Outfit: "Spider Necklace" Costume), IMRE (Outfit: Cowboy Costume)
# Time: Evening

label v15s18:
    scene v15s18_1 # TPP. Behind shot of MC walking up to the Deer's house in his Stripper Costume.
    with dissolve

    u "(This costume is so fucking embarrassing...)"

    scene v15s18_2 # TPP. Show MC about to knock on the door for the Deer's house, neutral face, mouth open.
    with dissolve

    u "*Sighs*"

    scene v15s18_3 # TPP. Closer up shot of MC's costume, neutral face, mouth closed.
    with dissolve

    u "(There's no turning back now...)"

    play sound "sounds/dooropen.mp3"

    scene v15s18_4 # FPP. Show the door starting to open.
    with dissolve

    pause 0.75

    scene v15s18_4a # FPP. Same as v15s18_4, The door open Lauren standing at the door answering it, Lauren in her Spider Necklace costume looking at MC, Lauren slight smile, mouth closed
    with dissolve
    
    pause 0.75

    scene v15s18_4b # FPP. Same as v15s18_4a, Lauren looking down as she is checking out MC's outfit, Lauren slight shocked face, mouth open
    with dissolve

    la "Oh... Wow, [name]! That is quite the outfit. *Laughs*"

    scene v15s18_4a # FPP. Same as v15s18_4b, Lauren looking back up at MC, Lauren slight smile, mouth open.
    with dissolve

    u "Haha, yeah... Um, it was the only costume they had left..."

    scene v15s18_4c
    with dissolve

    la "It's not a surprise that nobody wanted to buy that thing, haha!"

    la "You should probably come inside before you get arrested for indecent exposure."

    scene v15s18_4a
    with dissolve

    u "*Laughs* Okay, okay... You've completely roasted me and I'm not even inside yet."

    scene v15s18_4d # FPP. Same as v15s18_4c, Lauren stepped to the side laughing and holding the door open for MC, Lauren slight smile, mouth closed.
    with dissolve

    pause 1

    scene v15s18_5 # TPP. Show MC walking into the Deer's house, slight smile, mouth closed.
    with dissolve

    pause 1

    play sound "sounds/doorclose.mp3"

    scene v15s18_6 # TPP. Show of some of the decorations in the house
    with dissolve

    pause 1.25

    scene v15s18_7 # TPP. More decorations in the house.
    with dissolve

    pause 1.25

    scene v15s18_8 # FPP. MC and Lauren inside the Deer's house. Lauren looking at MC, MC looking at Lauren, Lauren slight smile, mouth closed.
    with dissolve

    u "Wow, it looks amazing in here..."

    scene v15s18_8a # FPP. Same as v15s18_8, Lauren slight smile, mouth closed.
    with dissolve

    la "Really?! I spent a ton of time decorating... I'm so glad everyone likes it."

    scene v15s18_8
    with dissolve

    u "Really. And also, happy birthday."

    if lauren.relationship.value >= Relationship.GIRLFRIEND.value: 
        scene v15s18_8b # FPP. Same as v15s18_8a, Lauren much closer to MC with her arms wrappe around his neck as she looks in his eyes, Lauren biting her lip, slight smile, mouth closed.
        with dissolve

        pause 0.75

        play sound "sounds/kiss.mp3"

        scene v15s18_8c # FPP. Same as v15s18_8b, Lauren kissing MC
        with dissolve

        pause 0.75

        scene v15s18_9 # TPP. Shot of MC and Lauren kissing
        with dissolve

        pause 0.75

        la "Thank you, [name]."

    else:
        scene v15s18_8a
        with dissolve

        la "Hehe, thank you!"

    scene v15s18_8d # FPP. Same as v15s18_8a, Lauren back to standing a little further from MC, MC handing Lauren a gift, Lauren looking at the gift in his hand, slight smile, mouth closed.
    with dissolve
    
    u "Here's your gift, by the way."

    scene v15s18_8e # FPP. Same as v15s18_8d, Lauren grabbing the gift as MC hands it over to her, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s18_8f # FPP. Same as v15s18_8e, Lauren holding the gift now looking at MC, Lauren slight smile, mouth open.
    with dissolve

    la "Oh! You didn't have to- *Sighs* I have to quit saying that..."

    scene v15s18_8g # FPP. Same as v15s18_8f, Lauren slight smile, mouth closed.
    with dissolve

    u "Haha, I kinda did have to..."

    scene v15s18_8f
    with dissolve

    la "[name]!"

    scene v15s18_8g
    with dissolve

    u "I'm kidding! *Laughs* I hope you like it."

    scene v15s18_8f
    with dissolve

    la "I'm sure I'll love it, thank you. I'll go put it with the others. See you in a bit!"

    scene v15s18_8h # FPP. Same as v15s18_8g, Show Lauren walking away to the room with the gifts holding MC's gift.
    with dissolve
    
    pause 0.75

    if lauren.relationship.value >= Relationship.GIRLFRIEND.value:
        scene v15s18_10 # FPP. Refer to v15s18_8h, Close up of Lauren's ass as she is walking away.
        with dissolve
        
        pause 0.75

    play sound "sounds/dooropen.mp3"

    scene v15s18_8h
    with dissolve

    pause 0.75

    play sound "sounds/doorclose.mp3"

    scene v15s18_11 # FPP. MC looking at the entrance door to the deer's house. Show Imre in his cowboy costume closing the door the deer's house as he enters, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s18_11a # FPP. Same as v15s18_11, Imre with his hands in the air looking at the party, excited, mouth open.
    with vpunch

    imre "It's Halloween up in this bitch!"

    scene v15s18_11b # FPP. Same as v15s18_11b, Imre looking at MC, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s18_11c # FPP. Same as v15s18_11c, Imre looking down as he is looking at MC's whole costume, Imre jaw dropped.
    with dissolve

    pause 0.75

    scene v15s18_11d # FPP. Same as v15s18_11c, Imre looking back up at MC's face, Imre slight smile, mouth open.
    with dissolve

    imre "What the... hell are you wearing?"

    scene v15s18_11e # FPP. Same as v15s18_11c, Imre slight smile, mouth closed.
    with dissolve

    u "It's a stripper costume, can't you tell? *Laughs*"

    scene v15s18_11d
    with dissolve

    imre "I feel like I need to wash my eyes now."

    scene v15s18_11e
    with dissolve

    u "Ha, umm... Yeah, sorry. I uh, I made an error in judgment."

    scene v15s18_11d
    with dissolve

    imre "Why didn't you just wear the same costume you got for Mr. Lee's class?"

    scene v15s18_11e
    with dissolve

    u "I have no idea where I put that thing, dude. I think someone borrowed it or stole it."

    if joinwolves and costume == 3:
        u "In fact, is that my fucking cowboy costume?"

    elif costume == 3:
        u "It looked exactly like yours actually... Is that-"

    scene v15s18_11d
    with dissolve

    imre "No, no, no... I bought this thing weeks ago, bro. No last-minute costume stealing was necessary."

    scene v15s18_11e
    with dissolve

    u "Hmm... Okay, if you say so..."

    scene v15s18_11d
    with dissolve

    imre "I know you're just trying to change the subject from that awful thing you've got on, haha."

    scene v15s18_11e
    with dissolve

    u "Ha, is it really that bad?"

    if joinwolves:
        scene v15s18_11d
        with dissolve

        imre "Eh..."

        scene v15s18_11f # FPP. Same as v15s18_11e, Imre looking back down to check out MC's whole costume, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s18_11e
        with dissolve

        pause 0.75

        scene v15s18_11f
        with dissolve

        pause 0.75

        scene v15s18_11e
        with dissolve

        pause 0.75

        scene v15s18_11f
        with dissolve

        pause 0.75

        scene v15s18_11e
        with dissolve

        pause 0.75

        scene v15s18_12 # TPP. Close up of MC's face, MC slightly weirded out, mouth closed.
        with dissolve

        pause 0.75

        scene v15s18_11e
        with dissolve

        u "What-"

        scene v15s18_11d
        with dissolve

        imre "You'll be fine, just wear it with confidence. The girls will love it."

        scene v15s18_11e
        with dissolve

        u "You're right... Maybe I'll just act like it was planned, not a last-minute decision."

        scene v15s18_11d
        with dissolve

        imre "That's how I live my whole life, haha!"

        scene v15s18_11e
        with dissolve

        u "*Laughs*"

    else:
        scene v15s18_11d
        with dissolve

        imre "Man, I suspected you lost your damn mind after you joined the Apes. Then you ask me a question like that?"

        imre "*Laughs* \"Is it that bad?\""

        scene v15s18_11e
        with dissolve

        u "Okay, I get it... There was no thinking behind it, though. It just happened."

        scene v15s18_11d
        with dissolve

        imre "What needs to just happen is you putting on a coat... Haha!"

        scene v15s18_11e
        with dissolve

        u "*Sighs*"

    scene v15s18_11g # FPP. Same as v15s18_11f, Imre pulling out a piece of paper from his pocket, slight smile, mouth closed.
    with dissolve

    u "What's that?"

    scene v15s18_11h # FPP. Same as v15s18_11g, Imre looking at the piece of paper, slight smile, mouth open.
    with dissolve

    imre "Ah... It's this stupid list of challenges I've been trying to do at a couple of parties this week."

    imre "I swear it's impossible to complete any of these. All I've gotten so far is a slap in the face, and that's not even on the list!"

    scene v15s18_11i # FPP. Same as v15s18_11h, Imre looking at MC, slight smile, mouth closed.
    with dissolve

    u "Haha, come on. It can't be that hard... What kind of things are on the list?"

    scene v15s18_11j # FPP. Same as v15s18_11i, Imre holding out the paper and MC grabbing it, Imre slight smile, mouth open.
    with dissolve

    imre "Here, take a look for yourself."

    scene v15s18_13 # FPP. MC looking down at the paper in his hands, (writing can be added later in photoshop if need.) Challenge list: 1. Get Slapped, (Have this one crossed out because Imre already did it) 2. Have Sex, 3. Give Oral, 4. Get Orla, 5. Get a Handjob, 6. Finger a girl, 7. Make out, 8. Steal Someone's panties, 9. Find a condom.
    with dissolve

    pause 0.75

    python:
        v15_imre_checklist.add_item("Have Sex")
        v15_imre_checklist.add_item("Give Oral")
        v15_imre_checklist.add_item("Get Oral")
        v15_imre_checklist.add_item("Get a Handjob")
        v15_imre_checklist.add_item("Finger a girl")
        v15_imre_checklist.add_item("Make out")
        v15_imre_checklist.add_item("Steal someone's panties")
        v15_imre_checklist.add_item("Find a condom")

    show screen v15_imre_checklist_icon
    # -The Party Checklist UI pops up, showing the list of challenges-
    # -The UI list disappears when player chooses to close it-

    show screen v15_imre_checklist

    pause
    
 
    scene v15s18_11e
    with dissolve

    u "Well shit, that looks fun. *Chuckles*"

    scene v15s18_11d
    with dissolve

    imre "Yeah, fun as fuck if you're good with girls... Let's see you try it!"

    scene v15s18_11e
    with dissolve

    u "Ha, what? Really?"

    scene v15s18_11d
    with dissolve

    imre "Yeah, really. Keep it and see if you have any luck tonight."

    imre "Just remember, you can't do them all with the same girl. It must be a different girl for each challenge."

    scene v15s18_11e
    with dissolve

    menu:
        "I'm not interested":
            $ add_point(KCT.BOYFRIEND)

            u "Listen Imre, I appreciate the thought, but I'm not really looking to hook up with every girl at this party."

            scene v15s18_11d
            with dissolve

            imre "Hey man, I won't tell you what to do, but keep the list anyway. Maybe you'll change your mind."

            scene v15s18_11e
            with dissolve

            u "Maybe... *Laughs*"

        "Looks easy":
            $ add_point(KCT.TROUBLEMAKER)
            
            u "It looks too easy... Is there a longer list?"

            scene v15s18_11d
            with dissolve

            imre "Haha... You might be funny, [name]. But like I said, I've been trying this for weeks now."

            imre "If you get anything more than a slap, I'll be impressed."

            scene v15s18_11e
            with dissolve

            u "Ha! (Easy.)"

    scene v15s18_11d
    with dissolve

    imre "Anyways, good luck! I'm ready to get my party on!"

    scene v15s18_8i # FPP. Same as v15s18_8h, Show Imre walking away into the party
    with dissolve

    u "(Hmm, I guess if I want to play Imre's little game I can... Otherwise, I'm just here to have a good night and celebrate Lauren.)"

    pause 0.75

    jump v15s18a