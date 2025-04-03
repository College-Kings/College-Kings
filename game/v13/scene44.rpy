# SCENE 44: Lauren and MC in The Hallway
# Locations: Hotel Hallways, Hotel lobby.
# Characters: LAUREN (Outfit: 3), MC (Outfit: 1)
# Time: Morning

label v13s44:
    scene v13s44_1 # TPP. Show MC walking down the hallway, Lauren slightly behind him, both Slight smile, both mouth open.
    with dissolve

    pause 0.75

    play music music.ck1.v13.Track_Scene_44 fadein 2

    scene v13s44_1a # TPP. Same as v13s44_1a, Lauren caught up to MC, MC slight smile, mouth closed, Lauren slight smile, mouth open.
    with dissolve
    
    if v11_lauren_caught_aubrey:
        $ CharacterService.set_relationship(lauren, Relationship.FRIEND, mc)
        $ CharacterService.remove_mood(lauren, Moods.MAD)
        
        la "[name]?"

        scene v13s44_3 # FPP. MC looking at Lauren, Lauren looking at MC, neutral expression, mouth closed
        with dissolve

        u "Oh, hey Lauren."

        scene v13s44_3a # FPP. Same as v13s44_3, Lauren neutral expression, mouth open.
        with dissolve

        la "*Sighs* You can stop acting awkward around me, okay?"

        scene v13s44_3
        with dissolve

        u "I know you say that, but I still don't sit right with what I did to you."

        scene v13s44_3a
        with dissolve

        la "Well, I hope you never feel \"good\" about what you did..."

        la "Look, I'm not going to hold your hand and start calling you babe again, but we can be friends. I'm not in a \"holding a grudge\" type of mood anyway."

        scene v13s44_3
        with dissolve

        u "You sure?"

        scene v13s44_3a
        with dissolve

        la "*Sighs* Yes, I'm sure. Now, look..."

    elif CharacterService.is_girlfriend(lauren):
        la "Hey babe!"

        scene v13s44_2 # TPP. Show Lauren kissing MC.
        with dissolve

        pause 0.75

    else:
        scene v13s44_4 # FPP. MC looking at Lauren, Lauren looking at MC, Lauren slight smile, mouth open.
        with dissolve

        la "Hey, [name]?"

        scene v13s44_4a # FPP. Same as v13s44_4, Lauren slight smile, mouth closed.
        with dissolve

        u "Lauren."

    scene v13s44_4 
    with dissolve
    
    la "Were you headed somewhere?"

    scene v13s44_4a
    with dissolve

    u "Nope, just got out of bed and ready to start the Amsterdam Day. *Chuckles*"

    scene v13s44_4b # FPP. Same as v13s44_4, Lauren different pose.
    with dissolve

    la "Me too, haha. Wanna go do something together?"

    scene v13s44_4a
    with dissolve

    u "What do you have in mind?"

    scene v13s44_4b
    with dissolve

    la "There's a really nice little bike trail up the street and I thought it'd be nice to take a ride for a bit."

    scene v13s44_4a
    with dissolve

    u "That does sound kinda nice. Plus, I probably should start getting back into shape. *Chuckles*"

    scene v13s44_4b
    with dissolve

    la "*Laughs* Let's go then."

    if v13_lauren_smoke:
        scene v13s44_4a
        with dissolve

        u "Oh shit I can't believe I almost forgot. How are you feeling after the hospital?"

        scene v13s44_4c # FPP. Same as v13s44_4b, Lauren different pose.
        with dissolve

        la "I'm fine, really. I definitely won't be trying anything like that again... Peer pressure is a no go."

        scene v13s44_4a
        with dissolve

        u "Yeah, I'm- I'm really sorry about that, Lauren."

        scene v13s44_4c
        with dissolve

        la "*Chuckles* Don't mention it, I'm responsible for my own decisions at the end of the day."

    scene v13s44_5 # TPP. Lauren and MC walking down the hallway, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v13s44_6 # TPP. Lauren and MC in the hotel lobby walking towards the door.
    with fade

    pause 0.75

    scene v13s44_7 # TPP. Lauren and MC exiting the hotel
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v13s45