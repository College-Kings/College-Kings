# SCENE 29: MC back at the hotel room
# Location: Hotel room, Hotel Corridor Outside Room
# Characters: MC (Outfit 1), Riley (Outfit 1), Chloe (Outfit 2)
# Time: night/day

label v11_hotel_room:
    play music "music/mhorror.mp3"
    play sound sound.swoosh
    scene s587
    with flash
    ri "He's coming!"

    scene s588  
    with dissolve

    la "I can't run any faster!"

    scene s589 
    with dissolve

    u "Fuck guys! We can't go any further, there's a cliff!"

    scene s590 
    with dissolve

    u "Guys?"

    scene s590a 
    with dissolve

    pause 0.5

    scene v11bane1 # FPP. Show MC holding two guns this time aimed at the girls heads. Mouth open 
    with dissolve

    u "I guess it's time for you two to die."
    u "3..."
    u "2..."

    menu (fail_label="v11timera"):
        "Save Lauren":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            $ v11save = 1

            scene v11bane5 # Mc tackles Lauren out of the guns aim (replace bane like character for MC )
            with dissolve

            u "1..."
            play sound "sounds/fall.mp3"

            scene s593 # Mc and Lauren on the ground terrified
            with vpunch

            play sound sound.gun
            pause 0.5

            scene s593a # mc looks back and screams
            with dissolve

            u "Nooo!"

            scene v11bane4a # FPP. Show charli on the floor screaming over Riley's dead body
            with dissolve

            pause 1.5

            jump v11wakeupa

        "Save Riley":
            $ reputation.add_point(RepComponent.BRO)
            $ v11save = 2

            scene v11bane6 # Mc tackles Riley out of the guns aim (replace bane character with MC, Mc should still be tackling Riley out the way)
            with dissolve

            u "1..."
            play sound "sounds/fall.mp3"

            scene s595 # Mc and Riley on the ground terrified
            with vpunch

            play sound sound.gun
            pause 0.5

            scene s595a # mc looks back and screams
            with dissolve

            u "Nooo!"

            scene v11bane4 # FPP. Show charli on the floor screaming over chloe's dead body
            with dissolve
            
            pause 1.5
            
            jump v11wakeupa

label v11timera:
    $ save = 0

    scene s596 # close up of your face terried
    with dissolve

    u "1..."
    play sound sound.gun

    scene s596a # Mc screaming terrified
    with vpunch

    u "Nooo!"

label v11wakeupa:
    stop sound
    hide fantasyoverlay onlayer foreground
    play sound sound.swoosh

    if not v11_riley_roomate:
        scene v11bane2 # TPP. Close up of mc, MC jumps awake from the dream. Sitting up in bed, scared face
        with flash

        u "Ahh! (What the fuck is going on inside my head?!)"

        scene v11bane3 # FPP. Show Chloe, worried look mouth open, hand reaching forward as if on mc's arm
        with dissolve

        cl "Woah! You okay, [name]?"

        scene v11bane3a # FPP. Same 3, mouth closed
        with dissolve

        u "Oh, uh... yeah. Just a bad dream I guess... You're up early."

        play music "music/v11/Track Scene 19_1.mp3" fadein 2
        scene v11bane3b # FPP. Same 3, chloe now looking at her suitcase accross the room, mouth open.
        with dissolve

        cl "I'm trying to finish unpacking. Something I haven't had a chance to do somehow, ha."

        scene v11hr3 # FPP. MC is now standing next to Chloe, Chloe looking at MC, Chloe mouth closed, slight smile
        with dissolve

        u "Probably because you brought a house's worth of stuff. Here, let me help you."

        if CharacterService.is_mad(chloe):
            scene v11hr3a # FPP. Same as v11hr3, Chloe slight smile, mouth open
            with dissolve

            cl "I'm good."

            scene v11hr3
            with dissolve

            u "You sure?"

            scene v11hr3b # FPP. Same as v11hr3, Chloe neutral expression, mouth open
            with dissolve

            cl "More than sure."

            scene v11hr3c # FPP. Same as v11hr3, Chloe neutral expression, mouth closed
            with dissolve

            u "Okay, well..."

        else:
            scene v11hr3a
            with dissolve

            cl "You don't have to."

            scene v11hr3
            with dissolve

            u "I want to."

            scene v11hr4 # FPP. MC looking in her luggage, grabbing a piece of clothing
            with dissolve
            
            pause 0.75

            scene v11hr4a # FPP. Same cam as v11hr4, MC sees a teddy bear
            with dissolve

            pause 0.75

            scene v11hr5 # FPP. MC is holding the teddy bear, looking at it
            with dissolve

            u "Who's this? *Chuckles*"

            scene v11hr3d # FPP. Same as v11hr3, Chloe worried face, mouth open
            with dissolve

            cl "Huh? Oh!"

            scene v11hr3e # FPP. Same as v11hr3, Chloe worried face, mouth closed, reaching for the teddy bear that is in MC's hand
            with dissolve

            pause 0.75

            scene v11hr3f # FPP. Same as v11hr3, Chloe is slightly embarrassed, mouth open, looking down, holding the teddy bear
            with dissolve

            cl "It's nothing, I uh... I won it in a little contest the other day."

            scene v11hr3g # FPP. Same as v11hr3f, Chloe is slightly embarrassed, mouth closed, looking at MC, she is holding the teddy bear
            with dissolve

            u "You won a teddy bear in a contest the other day and stuffed him in the bottom of your bag under everything else?"

            scene v11hr3f
            with dissolve

            cl "*Sighs* Okay, okay... it's my teddy bear. I bring it with me everywhere I go and have ever since I was little. Do we have to talk about it any longer?"

            scene v11hr3g
            with dissolve

            u "Aww, how cute. *Chuckles*"

            scene v11hr3f
            with dissolve

            cl "Stop, you're embarrassing me."

            if CharacterService.is_fwb(chloe) or CharacterService.is_girlfriend(chloe):
                scene v11hr3h # FPP. Same cam as v11hr3, Show MC grabbing Chloe's chin, she's slightly embarrassed, mouth closed, looking at MC
                with dissolve

                u "I was talking about you, not the bear."

                scene v11hr6 # TPP. Show MC kissing Chloe while holding her chin, same position as v11hr3
                with dissolve

                play sound sound.kiss

                pause 1

                scene v11hr7 # TPP. Show Chloe wrapping her arms around MC while he holds her chin, they've moved a bit inside the room
                with dissolve

                pause 1

                scene v11hr7a # TPP. Same cam as v11hr7, Chloe has her arms wrapped around MC, he is grabbing her waist
                with dissolve

                pause 1

                scene v11hr8 # FPP. Same positioning as v11hr7, MC and Chloe now stopped kissing, Chloe looking at MC, smiling, mouth closed
                with dissolve

                pause 0.75

                scene v11hr8a # FPP. Same as v11hr8, Chloe looking down and blushing, slightly embarrassed, mouth open
                with dissolve

                cl "Don't look at me like that."

                scene v11hr8b # FPP. Same as v11hr8a, Chloe looking at MC, blushing, slightly embarrassed, mouth closed
                with dissolve

                u "Like what? Like out of eight billion people I'm only focused on one?"

                scene v11hr8c # FPP. Same as v11hr8b, Chloe blusing, slightly embarrassed, mouth open
                with dissolve

                cl "Exactly."

                scene v11hr8b
                with dissolve

                u "Haha, you make it hard not to."

                scene v11hr8c
                with dissolve

                cl "*Chuckles* So sweet..."

                scene v11hr8b
                with dissolve

                u "I'm gonna head down and see what's buzzing in the lobby. I'll let you finish your bags, I'd hate to find anything else embarrassing. *Laughs*"

                scene v11hr8c
                with dissolve

                cl "Oh my gosh, go."

            else:
                scene v11hr3g
                with dissolve

                u "Embarrassing you? Me? I'd never."

                scene v11hr3i # FPP. Same as v11hr3, Chloe holding teddy bear, slight smile, mouth open
                with dissolve

                cl "Oh my gosh, go find something to do."

                scene v11hr3j # FPP. Same as v11hr3i, Chloe slight smile, mouth closed, holding teddy bear
                with dissolve

                u "I'll go see what's buzzing in the lobby."

    else:
        scene black
        with vpunch

        ri "[name]! Get up! You can't just sleep all day."

        play music "music/v11/Track Scene 19_1.mp3" fadein 2

        scene v11hr9 # FPP. MC is lying in his bed, he is looking at Riley, who is standing next to him, she is slightly angry, mouth closed
        with fade

        u "I could if you weren't waking me up."

        scene v11hr10 # TPP. Show Riley pulling MC's arm, he is startled, almost falling off the bed
        with dissolve

        pause 0.75

        scene v11hr11 # FPP. MC is now standing up next to Riley, she is looking at him, slightly angry, mouth closed
        with dissolve

        u "Damnit, Riley! Okay, I'm up."

        scene v11hr11a # FPP. Same as v11hr11, Riley slightly angry, mouth open
        with dissolve

        ri "I stayed up all night waiting for you thinking we could hang out. Where were you?"

        scene v11hr11
        with dissolve

        u "I was at the bar."

        scene v11hr11a
        with dissolve

        ri "Sure... you were with some London girl, weren't you?"

        scene v11hr11
        with dissolve

        menu:
            "Tease":
                $ reputation.add_point(RepComponent.TROUBLEMAKER)
                $ riley.points -= 1

                scene v11hr11
                with dissolve

                u "What, you jealous?"

                scene v11hr11a
                with dissolve

                ri "You wish."

            "Flirt":
                $ reputation.add_point(RepComponent.BOYFRIEND)
                $ riley.points += 1

                scene v11hr11b # FPP. Same as v11hr11, Riley slightly smiling, mouth closed
                with dissolve

                u "Never, only got eyes for you."

                scene v11hr11c # FPP. Same as v11hr11, Riley slightly smiling, mouth open
                with dissolve

                ri "Oh really?"

                scene v11hr11b
                with dissolve

                u "Of course."

                scene v11hr11c
                with dissolve

                ri "Sure. *Chuckles*"
            
        scene v11hr11c
        with dissolve

        ri "I don't know about you, but I've been doing my best to enjoy Europe and all it has to offer. I plan to take the bike tour of London today."

        scene v11hr11b
        with dissolve

        u "And I didn't get an invite? Wow..."

        if CharacterService.is_fwb(riley):
            scene v11hr11d # FPP. Same as v11hr11, Riley seductive look, mouth open
            with dissolve

            ri "Well, if you get to the room a little earlier than last night, maybe we can hang out."

            scene v11hr11e # FPP. Same as v11hr11, Riley seductive look, mouth closed
            with dissolve

            u "*Chuckles* Sounds good to me."

        else:
            scene v11hr11c
            with dissolve

            ri "Hey, you're free to do your own thing."

            scene v11hr11b
            with dissolve

            u "Obviously not, you just dragged me out of bed."

            scene v11hr11c
            with dissolve

            ri "Don't be a baby."

        scene v11hr11c
        with dissolve

        ri "Go enjoy your day."

        scene v11hr11b
        with dissolve

        u "Yes, your majesty."

        scene v11hr11c
        with dissolve

        ri "Actually... I like the sound of that... say it more often. *Chuckles*"

        scene v11hr11b
        with dissolve

        u "Haha."

    #scene v11hr12 # TPP. Show MC getting dressed (neutral expression, mouth closed) (only mc is in this shot)
    #with dissolve

    #pause 0.75

    #scene v11hr13 # TPP. Show MC going out the door of his hotel room (only mc is in this shot)
    #with dissolve

    #pause 0.75

    #scene v11hr14 # TPP. Show MC walking in the corridor outside his hotel room (only mc is in the shot)
    #with dissolve

    #pause 0.75
    stop music fadeout 3
    if v11_lauren_caught_aubrey:
        jump v11_lauren_apology
    else:
        jump v11_lauren_store