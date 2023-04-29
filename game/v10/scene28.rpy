# SCENE 28: Talk with Nora
# Location: Hallway at school
# Characters: MC (Outfit 3),Nora (outfit 1)
# Time: Tuesday Morning
label v10_talk_nora:
    play music "music/v10/Track Scene 28.mp3" fadein 2
    scene v10hal1 # FPP. Show Nora in hallway, mouth closed
    with fade

    u "Hey Nora."

    scene v10hal1a # FPP. Same 1, mouth open
    with dissolve

    no "Hey."

    scene v10hal1
    with dissolve

    u "So how's the Europe hunt going?"

    scene v10hal1a
    with dissolve

    no "Going good, not finished yet though. Right now including myself I have five people going. Riley, Chris, and Lindsey are on that list."

    scene v10hal1
    with dissolve

    u "Chris decided to go? That'll be good for you guys."

    scene v10hal1a
    with dissolve

    no "An abroad trip is required for him to graduate. Otherwise he wouldn't be going, so I'm not too sure if I'm really that happy about him coming."
    no "I'm really looking forward to this trip and I don't want... \"us\" ruining it."

    scene v10hal1
    with dissolve

    u "Well I'll be there to make sure it's fun. *Chuckles* Where are we all going?"

    scene v10hal1a
    with dissolve

    no "First stop is going to be London. That's only if we get enough people though."

    scene v10hal1
    with dissolve

    u "I'm sure we will."

    scene v10hal1a
    with dissolve

    if v8_nora_likes_mc:
        scene v10hal1a
        with dissolve

        no "I've always dreamed of living in London. When I was little I was always fascinated with the Queen. I even thought I could be the Queen one day."

        scene v10hal1
        with dissolve

        u "You had quite the imagination. London wouldn't be such a bad place to live."

        scene v10hal1a
        with dissolve

        no "And I still do. *Chuckles*"

        if joinwolves:
            menu:
                "Mention last night":
                    scene v10hal1
                    with dissolve

                    u "Hey, when I was out walking last night I thought I saw you going to Ms. Rose's house."

                    scene v10hal1b # FPP. same 1, nervous look, mouth open
                    with dissolve

                    no "Yeah I was there, I was trying to see if she'd chaperone the trip."

                    scene v10hal1
                    with dissolve

                    u "(Guess she's not gonna break.)"

                    u "She's a great teacher, it'd be nice if she came."

                    scene v10hal1b
                    with dissolve

                    no "Yeah, I'm pretty sure she'll take us. She likes Europe as much as I do."

                "Leave it alone":
                    scene v10hal1
                    with dissolve

                    u "(I'll leave it alone as they'd rather keep it private.)"

    elif not joinwolves and not v8_nora_likes_mc:
        scene v10hal1a
        with dissolve

        no "If not I was wasting a whole lot of time."

        scene v10hal1
        with dissolve

        u "What about Grayson or Cameron?"

        scene v10hal1a
        with dissolve

        no "Bringing Chris' rivals isn't a good idea. I really don't want the drama."

        scene v10hal1
        with dissolve

        u "I get that..."
        
    menu:
        "Help Nora":
            $ v10_help_nora_freeroam = True

            scene v10hal1
            with dissolve
            u "The charity event is coming up tomorrow, I could try and find some people to go too."

            scene v10hal1b
            with dissolve

            no "That would be a big help. Thanks."

            scene v10hal1
            with dissolve

            u "No problem."
        "Don't help":
            scene v10hal1
            with dissolve

            u "I hope the search goes well."

            scene v10hal1a
            with dissolve

            no "Yeah, me too."

    scene v10hal1a
    with dissolve

    no "Alright, I gotta get to my next class."

    scene v10hal1
    with dissolve

    u "See ya."

    stop music fadeout 3
    
    jump v10_chloe_hallway
