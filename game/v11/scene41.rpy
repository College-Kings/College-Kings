# SCENE 41: Chloe hotel room locked in the bathroom
# Location: Hotel room
# Characters: MC (Outfit 9), hloe (Outfit 2)
# Time: Night

label v11_chloe_bathroom:
    scene v11chb1 # TPP. Show MC walking into the room, confused, mouth closed
    with dissolve
    play music music.ck1.v10.Track_Scene_40_3 fadein 2
    cl "*Crying*"

    scene v11chb2 # TPP. Show MC walking up to the bathroom door, worried expression, mouth closed
    with dissolve

    pause 0.75

    scene v11chb3 # TPP. Show MC placing his ear on the bathroom door, mouth open, worried expression
    with dissolve

    u "Chloe?"

    scene v11chb4 # TPP. Show Chloe sitting on the toilet, shocked, mouth slightly open, looking at the bathroom door, crying
    with dissolve

    cl "*Whisper* Oh gosh..."

    scene v11chb4a # TPP. Same as v11chb4, Chloe crying, mouth open
    with dissolve

    cl "Yeah?"

    scene v11chb4b # TPP. Same as v11chb4a, Chloe mouth closed
    with dissolve

    u "Is everything alright?"

    scene v11chb4a
    with dissolve

    cl "Um..."

    scene v11chb3a # TPP. Same as v11chb3, Show MC slightly opening the bathroom door, mouth closed, worried expression
    with dissolve

    pause 0.75

    scene v11chb3b # TPP. Same as v11chb3a, Show the door halfway open, MC mouth closed, worried expression
    with dissolve

    pause 0.75

    scene v11chb5 # TPP. Show the bathroom door fully open, MC walking inside, mouth closed, worried expression
    with dissolve

    pause 0.75

    scene v11chb6 # TPP. Show MC standing in front of Chloe, looking down at her, Chloe sitting on the toilet looking up at him, Chloe crying, mouth closed, MC worried, mouth closed
    with dissolve

    pause 0.75

    scene v11chb7 # TPP. Show MC kneeling in front of Chloe, placing a hand on her knee, Chloe and MC looking at each other, Chloe crying, mouth closed, MC mouth closed, worried
    with dissolve

    pause 0.75

    scene v11chb8 # FPP. Same character positioning as v11chb7, MC and Chloe looking at each other, Chloe crying, mouth closed
    with dissolve

    u "Tell me what's going on."

    scene v11chb8a # FPP. Same as v11chb8, Chloe crying, mouth open
    with dissolve

    cl "I'm just tired, [name]. I'm tired of all this drama. I don't want to have issues with Nora anymore, and I don't want the girls to keep looking at me the way they are."

    scene v11chb8
    with dissolve

    u "Chloe, you have to give things time. Eventually, it's going to resolve itself, all things do. This will be no different."

    scene v11chb8a
    with dissolve

    cl "You actually think so?"

    scene v11chb8b # FPP. Same as v11chb8, different pose
    with dissolve

    u "I know so. But we have to be patient when it comes to stupid shit like this."

    scene v11chb8c # FPP. Same as v11chb8b, Chloe crying, mouth open
    with dissolve

    cl "Do you think the things she said about me are true?"

    scene v11chb8b
    with dissolve

    u "I think Nora was frustrated and with everyone trying to figure things out... She was probably just taking a bunch of things out on you."

    scene v11chb8d # FPP. Same as v11chb8, Chloe wiping her face off, sad, mouth closed
    with dissolve

    pause 0.75

    scene v11chb6a # TPP. Same cam as v11chb6, Chloe and MC now standing up, Chloe grabbing his shirt, pulling him towards the bathroom door, Chloe slight grin, mouth closed, MC worried, mouth closed
    with dissolve

    pause 0.75

    scene v11chb3c # TPP. Same cam as v11chb3, Chloe and MC getting out of the bathroom, they're making out
    with dissolve

    pause 0.75

    play sound sound.kiss

    scene v11chb9 # TPP. Show MC and Chloe making out in the room
    with dissolve

    menu:
        "Pull back":
            scene v11chb9a # TPP. Same as v11chb9, MC pulling back from the kiss, Chloe slightly sad
            with dissolve

            pause 0.75

            scene v11chb10 # FPP. Same positioning as v11chb9a, MC and Chloe looking at each other, Chloe sad, mouth closed, MC's arms on her shoulders
            with dissolve

            u "Chloe..."

            scene v11chb9b # TPP. Same as v11chb9, MC and Chloe hugging tightly, MC mouth open, worried, Chloe sad, mouth closed
            with dissolve

            u "Not while you're stressed out, not like this. I wanna be there for you the right way."

            scene v11chb10a # FPP. Same as v11chb10, Chloe sad, mouth open
            with dissolve

            cl "*Sighs* I'm sorry. Thank you."

            scene v11chb11 # TPP. Show MC and Chloe walking over to the bed, MC worried, Chloe sad, both mouths closed
            with dissolve

            pause 0.75

            scene v11chb12 # TPP. Show MC and Chloe midway through sitting on Chloe's bed, Chloe sad, mouth closed, MC worried, mouth closed
            with dissolve

            pause 0.75

            scene v11chb12a # TPP. Same as v11chb12, MC and Chloe sitting next to each other on the bed, looking at each other, Chloe mouth closed, sad, MC worried, mouth closed
            with dissolve

            pause 0.75

            scene v11chb13 # FPP. MC sitting next to Chloe on Chloe's bed, Chloe sad, mouth closed, looking at MC
            with dissolve

            u "Like I said, all of this is going to work out. It may feel like it's all piling up on you right now, but it's a good thing that everything is coming out."

            scene v11chb13a # FPP. Same as v11chb13, Chloe slight smile, tears on her face, mouth closed
            with dissolve
            
            u "That just means in some way, all of this will soon be resolved."

            scene v11chb13b # FPP. Same as v11chb13, Chloe slight smile, tears on her face, mouth open
            with dissolve

            cl "I hope you're right. Either way, you always know exactly what I need to hear."
            
            cl "Sometimes it's still hard to believe that you're the same guy that had a black eye during our first week of school, all because of me. *Chuckles*"

            scene v11chb13a
            with dissolve

            u "You're right, that was your fault... *Chuckles*"

            scene v11chb13b
            with dissolve

            cl "You really have been there for me whenever I needed you, [name]. Thank you."

            if CharacterService.is_fwb(chloe) or CharacterService.is_girlfriend(chloe):
                scene v11chb12b # TPP. Same as v11chb12a, MC and Chloe kissing (just a peck on the lips)
                with dissolve
                play sound sound.kiss

                pause 0.75
            
            scene v11chb13a
            with dissolve

            u "Always. Try to get some sleep, okay?"

            scene v11chb13b
            with dissolve

            cl "I will."

            scene v11chb12c # TPP. Same as v11chb12, Chloe sitting on the bed, looking as MC is getting up from the bed, Chloe slight smile, tears on her face, MC slight smile, both mouths closed
            with dissolve

            pause 0.75

            scene v11chb14 # TPP. Show MC getting in his bed, he's slightly smiling, mouth closed
            with dissolve

            pause 0.75

            scene v11chb15 # TPP. Show MC sleeping
            with dissolve

            pause 0.75

            scene v11chb15a # TPP. Same as v11chb15, different pose
            with dissolve

            pause 0.75

            jump v11_hotel_lobby_rose

        "Continue":
            scene v11chb9c # TPP. Same as v11chb9, Show Chloe and MC making out intensly
            with dissolve

            pause 0.75

            scene v11chb9d # TPP. Same as v11chb9c, MC and Chloe making out, different pose, MC grabbing Chloe's ass
            with dissolve

            cl "*Moans*"

            if CharacterService.is_fwb(chloe) or CharacterService.is_girlfriend(chloe):
                $ sceneList.add("v11_chloe")
                $ CharacterService.set_relationship(chloe, Relationship.GIRLFRIEND)

                stop music fadeout 3
                jump v11_chloe_sex_scene

            else:            
                scene v11chb9e # TPP. Same as v11chb9a, but Chloe is the one pulling back from the kiss instead of MC
                with dissolve

                pause 0.75

                scene v11chb10b # FPP. Same as v11chb10, Chloe avoiding eye contact, mouth open, sad, MC's hands not on her shoulders
                with dissolve

                cl "I... I shouldn't have kissed you. I'm sorry."

                scene v11chb10
                with dissolve

                u "Chloe, really... It's fine."

                scene v11chb10a
                with dissolve

                cl "I'm just gonna try to get some sleep"

                scene v11chb10
                with dissolve

                u "Oh... okay."

                scene v11chb16 # TPP. Show Chloe getting in her bed, she's sad, mouth closed
                with dissolve

                pause 0.75

                scene v11chb14a # TPP. Same as v11chb14, MC slightly sad, mouth closed
                with dissolve

                pause 0.75

                scene v11chb17 # FPP. MC lying in his bed, looking at Chloe, Chloe lying down on her bed, looking at MC, slight smile, tears in her eyes, mouth open
                with dissolve

                cl "Goodnight."

                scene v11chb17a # FPP. Same as v11chb17, Chloe mouth closed, slight smile, tears in her eyes
                with dissolve

                u "Goodnight."

                scene v11chb15a
                with dissolve

                pause 0.75

                scene v11chb15
                with dissolve

                pause 0.75
                stop music fadeout 3
                jump v11_hotel_lobby_rose