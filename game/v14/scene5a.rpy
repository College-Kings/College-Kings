# SCENE 05a: Going to bed - Riley Roommate
# Locations: Hotel Room
# Characters: MC (Outfit: 3), RILEY (Outfit: 5)
# Time: Night

label v14s05a:
    play music "music/v13/Track Scene 40_3.mp3" fadein 2

    play sound "sounds/dooropen.mp3"
    pause 0.51

    scene v14s05a_1 # TPP. Show walking into his room, neutral expression, mouth closed
    with dissolve
    pause 0.75

    scene v14s05a_2 # FPP. Show Riley sitting on the side of her bed, slight smile, mouth closed
    with dissolve
    pause 0.75

    scene v14s05a_3 # FPP. MC, closer to Riley, slight smile, mouth closed
    with dissolve
    
    u "*Sighs*"

    scene v14s05a_3a # FPP. Same as v14s05a_3, mouth open
    with dissolve

    ri "Yikes... You sound stressed."

    scene v14s05a_3
    with dissolve

    u "Crazy night, sorry."

    scene v14s05a_4 # TPP. MC changes into his boxers, neutral expression, mouth closed 
    with dissolve

    pause 0.75

    scene v14s05a_5 # TPP. Show MC starting to get into his bed, neutral expression, mouth closed
    with dissolve

    pause 0.75

    scene v14s05a_6 # TPP. Show Mc lying down into his bed, looking up to the roof, slight smile, mouth closed
    with dissolve

    pause 0.75

    if "v14_threesome" in sceneList:
        scene v14s05a_7 # FPP. Riley just beside MC on her bedside sitting up straight, slight smile, mouth open
        with dissolve

        ri "It was a crazy day too."

        scene v14s05a_7a # FPP. Same as v14s05a_7, mouth closed
        with dissolve

        u "That was definitely unexpected, but well appreciated of course."

        scene v14s05a_7
        with dissolve

        ri "Aubrey and I just felt like you could've used a little, pick me up."

        scene v14s05a_7a
        with dissolve

        u "It definitely picked me up... *Laughs*"

        scene v14s05a_7b # FPP. Same as v14s05a_7, different posture
        with dissolve
        ri "I've always wanted to do these kinds of things, but never had the chance."

        scene v14s05a_7
        with dissolve

        ri "I was hoping I could get to that point with Amber eventually, but she isn't as accepting as Aubrey."

        scene v14s05a_7a
        with dissolve

        u "That's kind of surprising."

        scene v14s05a_7
        with dissolve

        ri "Ha, yeah. I thought the same thing."

        scene v14s05a_7a
        with dissolve

        u "Well..."

        scene v14s05a_7
        with dissolve

        ri "Well..."

        scene v14s05a_8 # TPP. Show Riley standing up, slight smile, mouth closed, MC, slight smile, mouth closed
        with dissolve

        pause 0.75

        scene v14s05a_9 # TPP. Show Riley moving closer to MC, Riley, slight smile, mouth closed, MC slighty smile, mouth closed
        with dissolve
        
        pause 0.75

        scene v14s05a_10 # FPP. Riley beside MC looking at him, slight smile, mouth open
        with dissolve

        ri "I would invite you to cuddle but I don't want to risk anything else happening today..."

        scene v14s05a_11 # TPP. Closeup of Riley and MC kissing
        with dissolve

        play sound "sounds/kiss.mp3"
        pause 0.75

        scene v14s05a_11a # TPP. Same postion as v14s05a_11, Riley slight smile, mouth closed, MC, slight smile, mouth closed
        with dissolve

        pause 0.75

        scene v14s05a_10
        with dissolve

        ri "Plus, I think I've had enough of you for today. *Chuckles*"

        scene v14s05a_12 # TPP. Show Riley getting into her bed, slight smile, mouth closed
        with dissolve

        pause 0.75

        scene v14s05a_13 # FPP. Riley now laying in her bed, looking at MC, slight smile, mouth closed
        with dissolve

        u "Haha, is that so?"

        scene v14s05a_13a # FPP. Same as v14s05a_13, mouth open
        with dissolve

        ri "Yes sir, it is."

        scene v14s05a_13
        with dissolve

        u "Goodnight Riley."

        scene v14s05a_13a
        with dissolve

        ri "Goodnight, handsome."

    else:
        scene v14s05a_7
        with dissolve

        ri "Wanna talk about it?"

        scene v14s05a_7a
        with dissolve
        u "Not particularly, no. Same old shit really..."

        scene v14s05a_7b
        with dissolve

        ri "Haha, okay. I can respect that."

        scene v14s05a_7a
        with dissolve

        u "What's going with you?"

        scene v14s05a_7
        with dissolve

        ri "I'm just trying to get to know all the Chicks and see what they're all really about."

        scene v14s05a_7a
        with dissolve

        u "Yeah? How come?"

        scene v14s05a_7c # FPP. Same as v14s05a_7, excited expression
        with dissolve

        ri "Well, I'm starting to really consider joining them."

        scene v14s05a_7a
        with dissolve

        u "Really?"

        scene v14s05a_7c
        with dissolve

        ri "Haha, yep."

        scene v14s05a_7a
        with dissolve

        menu:
            "I think you should":
                $ v14s5a_riley_should_join_chicks = True
                $ reputation.add_point(RepComponent.BRO)

                u "I think you should. You'd really fit in there."

            "You sure it's for you?":
                $ reputation.add_point(RepComponent.BOYFRIEND)

                u "Hmm, are you sure it's for you?"

        scene v14s05a_7b
        with dissolve

        ri "I guess. I really don't know yet, to be honest. For now, I'm going to sleep."

        scene v14s05a_12
        with dissolve

        pause 0.75

        scene v14s05a_13
        with dissolve

        u "Alrighty... One last thing though."

        scene v14s05a_13a
        with dissolve

        ri "What is it?"

        scene v14s05a_13
        with dissolve

        u "Who are you supporting in this whole race to presidency?"

        scene v14s05a_13a
        with dissolve

        ri "I've been trying to avoid this question, I'm so biased. Who would you pick?"

        menu: 
            "Help Chloe":
                if CharacterService.is_girlfriend(chloe, Relationship.GIRLFRIEND):
                    $ reputation.add_point(RepComponent.BOYFRIEND)
                elif lindsey.relationship >= Relationship.FWB:
                    $ reputation.add_point(RepComponent.TROUBLEMAKER)
                scene v14s05a_13
                with dissolve

                u "Well, I'd support Chloe."

            "Help Lindsey":
                if lindsey.relationship >= Relationship.FWB:
                    $ reputation.add_point(RepComponent.BOYFRIEND)
                elif CharacterService.is_girlfriend(chloe, Relationship.GIRLFRIEND):
                    $ reputation.add_point(RepComponent.TROUBLEMAKER)
                scene v14s05a_13
                with dissolve

                u "Well, I'd help Lindsey."

        scene v14s05a_13b # FPP. Same as v14s05a_13a, Riley having a thoughtful expression
        with dissolve

        ri "Interesting..."

        scene v14s05a_13a
        with dissolve

        ri "Well, I'll keep that in mind. For now, I'm shutting my mind off."

        scene v14s05a_13
        with dissolve

        u "Haha, goodnight Riley."

        scene v14s05a_13a
        with dissolve

        ri "Goodnight."

    scene v14s05a_14 # TPP. Show MC leaning over to turn off the light, neutral expression, mouth closed 
    with dissolve

    pause 0.75

    scene v14s05a_15 # TPP. Show MC birds eye view laying in bed, eyes closed, neutral expression, mouth closed
    with dissolve

    pause 0.75

    stop music fadeout 3
    jump v14s06