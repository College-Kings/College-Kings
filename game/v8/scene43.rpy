# Forest w Grayson
# Location: Forest
# Outfits: MC Outfit 2, Grayson Outfit 2
# Time: Tuesday Night

label for_w_gray:

    scene v8sfor1 # TPP. Show Grayson and MC walking through the forest, MC trailing behind Grayson.
    with fade

    u "(This isn't creepy at all...)"

    scene v8sfor2 # FPP. Show Grayson pointing at a rock on the floor, Grayson neutral expression, mouth open.
    with dissolve

    gr "Sit."

    scene v8sfor2 # FPP. You're now sat on the rock, show Grayson sitting on a rock opposite you.
    with dissolve

    pause 0.5

    scene v8sfor8e # FPP. Same camera as v8sfor3, Grayson now sat on the rock, looking at camera.
    with dissolve

    menu:
        "Ask questions":
            $ reputation.add_point(Reputations.TROUBLEMAKER)
            jump for_w_gray_q
        "Don't say anything":
            $ reputation.add_point(Reputations.BOYFRIEND)
            jump for_w_gray_no_q

label for_w_gray_q:
    u "Um, where's everyone else?"

    scene v8sfor8d # FPP. Same camera as v8sfor3, Grayson stern expression, mouth open.
    with dissolve

    gr "They don't matter. You're what matters."

    jump for_w_gray_cont

label for_w_gray_no_q:
    u "(I wonder where everyone else is)"

    scene v8sfor8d
    with dissolve

    gr "I bet you're wondering why I brought you here. And not all the other Apes."

    jump for_w_gray_cont

label for_w_gray_cont:
    scene v8sfor8c # FPP. Same camera as v8sfor3, Grayson slight grin, mouth open.
    with dissolve

    gr "I see something in you, [name]. Something big."

    scene v8sfor4 # FPP. Close up Grayson, Grayson pounding on his chest like fugazi from Wolf of Wallstreet, Grayson intense expression, mouth open.
    with dissolve

    gr "I see a Great Ape! Are you a Great Ape, [name]?"

    scene v8sfor4a # FPP. Same camera as v8sfor4, Grayson mouth closed.
    with dissolve

    menu:
        "Go along with it":
            $ reputation.add_point(Reputations.BRO)
            jump forest_fugazi
        "Stay quiet":
            $ reputation.add_point(Reputations.BOYFRIEND)
            jump forest_no_fugazi


    ### ERROR: -MC can choose to go along with it or stay quiet ###
label forest_fugazi:
    u "Yes!"

    scene v8sfor5 # TPP. Show MC pounding on his chest also along with Grayson, both intense expressions, Grayson mouth open.
    with dissolve

    gr "That's what I'm talkin' about! I knew it!"

    jump for_w_gray_cont_2

label forest_no_fugazi:
    u "(I don't know where this is going. Better let him talk)"

    scene v8sfor6 # FPP. Show Grayson pacing around the forest, pounding on his chest, intense expression, mouth closed.
    with dissolve
    u "I wanna be some day."

    scene v8sfor6a # FPP. Same camera as v8sfor6, Grayson still pacing the forest, now looking at camera, Grayson slight confused expression, Grayson mouth open.
    with dissolve

    gr "Some day?"

    scene v8sfor6b # FPP. Same camera as v8sfor6, Grayson stops and looks at camera, intense expression, still pounding on chest, mouth open.
    with dissolve

    gr "Do you have any idea what's in store for you now?"

    jump for_w_gray_cont_2

label for_w_gray_cont_2:
    scene v8sfor7 # TPP. Show Grayson squatting just infront of MC. Both looking at eachother, mouths closed.
    with dissolve

    pause 0.5

    scene v8sfor8 # FPP. Close up Grayson looking at camera, Grayson neutral expression, mouth open.
    with dissolve

    gr "The Apes will open a lot of doors for you, [name]."

    scene v8sfor8a # FPP. Same camera as v8sfor8, Grayson laughing, mouth open.
    with dissolve

    gr "And legs. Lots of legs."

    scene v8sfor8b # FPP. Same camera as v8sfor8, Grayson grin, mouth closed.
    with dissolve

    u "I'm down for that!"

    scene v8sfor8a
    with dissolve

    gr "I bet you are!"

    if apesVids == 4: # 1st
        scene v8sfor8c # FPP. Same camera as v8sfor8, Grayson slight smile, mouth open.
        with dissolve

        gr "I had a feeling about you before bringing you into the Apes. But the way you aced those challenges!"

        scene v8sfor8a
        with dissolve

        gr "Man you were awesome! And that's when I knew for sure."

        jump for_w_gray_cont_3

    elif apesVids >= 2: # 2nd
        scene v8sfor8c
        with dissolve

        gr "I had a feeling about you before bringing you into the Apes. And when you scored so well in the challenges, I knew I'd made the right choice."

        scene v8sfor8b
        with dissolve

        u "Thanks, man."

        jump for_w_gray_cont_3

    else: # 3rd
        scene v8sfor8d # FPP. Same camera as v8sfor8, Grayson concerned expression, mouth open.
        with dissolve

        gr "I gotta say though, I'm a bit concerned."

        scene v8sfor8e # FPP. Same camera as v8sfor8, Grayson concerned expression, mouth closed..
        with dissolve

        u "Why?"

        scene v8sfor8d
        with dissolve

        gr "You didn't do too well in the challenges. Are you sure you want to be an Ape?"

        scene v8sfor8e
        with dissolve

        menu:
            "I definitely want to be an Ape":
                $ reputation.add_point(Reputations.BRO)
                jump deffo_be_ape_for
            "I think I want to be an Ape":
                jump maybe_be_ape_for

label deffo_be_ape_for:
    u "YES! I'm in. Tell me what I need to do."

    scene v8sfor8c
    with dissolve

    gr "That's what I was hoping you'd say."

    jump for_w_gray_cont_3

label maybe_be_ape_for:
    u "I think so... I mean, yeah I want in. I'm just..."

    scene v8sfor8d
    with dissolve

    gr "Timid."

    scene v8sfor8e
    with dissolve

    u "I wouldn't say that."

    scene v8sfor8f # FPP. Same camera as v8sfor8, Grayson slight angry expression, mouth open.
    with dissolve

    gr "Then what would you call it? Cuz from here, you looked like a punk, and you made me look like one when I vouched for you."

    scene v8sfor8e
    with dissolve

    u "I... I didn't want to get in trouble. I worked hard to get in here."

    scene v8sfor8c
    with dissolve

    gr "Is that all? Dude, don't worry about that. You're an Ape now!"

    jump for_w_gray_cont_3

label for_w_gray_cont_3:
    scene v8sfor9 # FPP. Show Grayson standing back up, pounding on chest again, looking at camera, intense expression, mouth open.
    with dissolve

    gr "You're an Ape, man! Can you believe it?"

    scene v8sfor10 # FPP. Show Grayson now fully stood up, looking dow at camera, pounding on chest, intense expression, mouth closed.
    with dissolve

    u "I'm an Ape!"

    scene v8sfor11 # FPP. Show Grayson pacing the forest again, looking around, pounding on his chest, slight smile, mouth open.
    with dissolve

    gr "We run this college. Hell, you're looking at the Fight King! Come on! We got it made!"

    scene v8sfor12 # FPP. Show Grayson standing still, pounding on chest, neutral expression looking at camera, mouth closed.
    with dissolve

    u "Yeah!"

    scene v8sfor12a # FPP. Same camera as v8sfor12, Grayson grin, mouth open.
    with dissolve

    gr "You'll have your choice of babes. I'm dripping in pussy. Anytime I want it!"

    scene v8sfor12b # FPP. Same camera as v8sfor12, Grayson grin, mouth closed.
    with dissolve

    menu:
        "Agree with Grayson":
            $ reputation.add_point(Reputations.BRO)
            jump for_w_gray_agree
        "I joined for the fights":
            $ reputation.add_point(Reputations.TROUBLEMAKER)
            jump for_w_gray_fights

label for_w_gray_agree:
    u "That's why I pledged!"

    scene v8sfor12c # FPP. Same camera as v8sfor12, Grayson slight smug expression, mouth open.
    with dissolve

    gr "You haven't done too bad for yourself."

    scene v8sfor12d # FPP. Same camera as v8sfor12, Grayson slight smug expression, mouth closed.
    with dissolve

    u "I do alright."

    scene v8sfor12c
    with dissolve

    gr "Modest. I like it."

    jump for_w_gray_cont_4

label for_w_gray_fights:
    u "That's cool and all, but I joined so I could learn how to fight like you."

    scene v8sfor12c
    with dissolve

    gr "And you will. Maybe better."

    jump for_w_gray_cont_4

label for_w_gray_cont_4:
    scene v8sfor13 # FPP. Show Grayson sighing and beginning to pace the forest again, Grayson mouth open.
    with dissolve

    gr "I need someone who can take over when I graduate, and I want that person to be you."

    scene v8sfor13a # FPP. Same camera as v8sfor13, Grayson stops and is looking elsewhere, neutral expression, mouth closed.
    with dissolve

    u "Wow, I'm honored. But I'm sure there's more..."

    scene v8sfor13b # FPP. Same camera as v8sfor13, Grayson suddenly turns to look back at the camera, Grayson demanding expression, mouth open.
    with dissolve

    gr "It's you!"

    scene v8sfor13c # FPP. Same camera as v8sfor13, Grayson smirk, mouth closed.
    with dissolve

    u "Okay."

    scene v8sfor14 # TPP. Show Grayson signalling MC to stand up, both looking at eachother, Grayson neutral expression, mouth open, MC looks a little confused, MC mouth closed.
    with dissolve

    gr "Stand up."

    scene v8sfor15 # TPP. Show Grayson walking towards MC so he is stood infront of him, Grayson looking like he's about to give a speech, mouth open.
    with dissolve

    gr "You've got a few great years ahead of you, [name]. Parties. Booze. Babes."

    scene v8sfor16 # FPP. Close up Grayson, Grayson serious expression, mouth closed.
    with dissolve

    u "I'm all for it!"

    scene v8sfor16a # FPP. Same camera as v8sfor16, Grayson slight serious expression, mouth open.
    with dissolve

    gr "But on top of all the fun, is gonna be your training."

    scene v8sfor16
    with dissolve

    u "Training?"

    scene v8sfor16a
    with dissolve

    gr "There's a lot that goes into being the leader of the Apes and I need to show you all the stuff the other guys will never see."

    scene v8sfor16
    with dissolve

    menu:
        "Agree with Grayson":
            $ reputation.add_point(Reputations.BRO)
            jump for_w_gray_agree_2
        "Hesitate":
            $ hesitantwgrayson = True
            jump for_w_gray_hesitate


label for_w_gray_agree_2:
    u "Let's do it!"

    scene v8sfor16b # FPP. Same camera as v8sfor16, Grayson smile, mouth open.
    with dissolve

    gr "That's what I'm talking about!"

    jump for_w_gray_cont_5

label for_w_gray_hesitate:
    u "I don't know... Are you sure?"

    scene v8sfor17 # FPP. Show Grayson beginning to pace around again but looking at camera, pounding chest, grayson slight serious expression, mouth open.
    with dissolve

    gr "Of course I'm sure. But I need you to be sure! Say it!"

    scene v8sfor17a # FPP. Same camera as v8sfor17, Grayson pacing around, looking elsewhere, pounding chest, mouth closed.
    with dissolve

    u "I'm sure."

    scene v8sfor17b # FPP. Same camera as v8sfor17, Grayson looking at camera again, intense expression, shouting, mouth open.
    with dissolve

    gr "Louder!"

    scene v8sfor17a # FPP. Same camera as v8sfor17, Grayson pacing around again, looking elsewhere, intense expression, mouth closed.
    with dissolve

    u "I'm sure!"

    scene v8sfor17b # FPP. Same camera as v8sfor17, Grayson looking at camera again, intense expression, pounding chest, shouting louder, mouth open
    with dissolve

    gr "*yells* I'M SURE!"

    scene v8sfor17 # FPP. Same camera as v8sfor17, Grayson looking at camera, intense expression, pounding chest, mouth closed.
    with dissolve

    u "*yells* I'M SURE!"

    jump for_w_gray_cont_5

label for_w_gray_cont_5:
    scene v8sfor18 # TPP. Show MC and Grayson both pacing around, pounding their chests, intense expressions, Grayson shouting, mouth open.
    with dissolve

    gr "APES!"

    scene v8sfor19 # TPP. Show MC and Grayson still pacing around, pounding their chests, intense expressions, MC shouting, MC mouth open.
    with dissolve

    u "APES!"

    scene v8sfor20 # FPP. Close up Grayson, Grayson slight grin, mouth open.
    with dissolve

    gr "You ready to go back to the house and show these Apes how to be Great?"

    scene v8sfor20a # FPP. Same camera as v8sfor20, Grayson slight grin, mouth closed.
    with dissolve

    u "Yeah!"

    scene v8sfor21 # TPP. Show MC and Grayson leaving the spot they have been at for this scene, walking next to eachother, camera from behind.
    with dissolve

    jump walk_home_w_gray
