# SCENE 25: Altercation at Ms. Rose's
# Locations: Ms. Rose's house.
# Characters: MC (Outfit 1), Mr Rose, Ms Rose,Nora
# Time: Monday Evening

label v10_ms_rose_fight:
    scene v10msf1 # FPP. Show MS rose's house, MS rose stood at the door, Mr rose stood infront of house. Ms rose angry look, Ms rose mouth closed, mr rose mouth open
    with dissolve

    play music "music/v10/Track Scene 25_1.mp3" fadein 2

    mrr "These things take time, how is that not clear? You can't expect a luxurious lifestyle if you're not willing to put the work in!"

    scene v10msf1a # FPP. same camera as v10msf1, Ms rose angry look hands raised, Ms rose mouth open, mr rose mouth closed
    with dissolve

    ro "I don't need any of that! All I wanted was a husband that committed more time to his wife than he does to company meetings!"

    scene v10msf1
    with dissolve

    mrr "Look, you knew my plans when you married me. We were doing good and real soon everything's gonna all come together."

    mrr "But here on the last stretch of the race, you wanna back out because I can't be home as much as you want?"

    mrr "Lolo, doesn't that sound ridiculous?"

    scene v10msf1a
    with dissolve

    ro "My name is Lorraine, not Lolo. And no it does not sound ridiculous. You make time for all those business dinners. When was the last time we went out?"

    scene v10msf1
    with dissolve

    mrr "As I said, this is the last stretch. I need to focus on this right now, then I can focus on us."

    scene v10msf1a
    with dissolve

    ro "*Sighs* Just leave."

    scene v10msf1
    with dissolve

    mrr "Lolo look-"

    scene v10msf1a
    with dissolve

    ro "LEAVE!!!"

    scene v10msf1
    with dissolve

    mrr "Just let me come in so we can-"

    menu:
        "Speak up":
            $ reputation.add_point(Reputations.BOYFRIEND)
            $ v10_ms_r_interfere = True
            scene v10msf2 # FPP. Show MR Rose in foreground facing camera, Show MS rose at the door facing camera, Mr Rose Mouth closed, Ms rose mouth closed.
            with dissolve

            u "Hey, is everything alright?"

            scene v10msf2a # FPP. same camera as v10msf2,Ms rose crying, Mr Rose Mouth open, Ms rose mouth closed.
            with dissolve

            mrr "We're doing just fine thank you."

            scene v10msf2b # FPP. same camera as v10msf2,Ms rose crying, Mr Rose Mouth closed, Ms rose mouth closed.
            with dissolve

            u "Well I heard yelling and I-"

            scene v10msf2a
            with dissolve

            mrr "Young man! Your concern is appreciated, but not necessary. My wife and I are trying to have an adult conversation. So if you'd just leave we'd be-"

            scene v10msf2c # FPP. same camera as v10msf2,Ms rose crying,Ms rose angry face, Mr Rose Mouth closed, Ms rose mouth open.
            with dissolve

            ro "LUCIOUS, YOU LEAVE!"

            scene v10msf2a
            with dissolve

            mrr "We're having a conver-"

            scene v10msf2c
            with dissolve

            ro "NOW!"

            scene v10msf2a
            with dissolve

            mrr "*Sighs* Fine."
            stop music fadeout 3
            play music "music/v10/Track Scene 25_2.mp3" fadein 2

            scene v10msf3 # FPP. Show Mr Rose walking away from the house
            with dissolve

            pause 0.5

        "Stay quiet":
            #scene v10msf2c
            scene v10msf1a
            with dissolve
            ro "I SAID NO! What do you not understand? We are done, there's nothing for you to explain. I don't care about your money, your cars, none of that! Leave!"

            #scene v10msf2a
            scene v10msf1
            with dissolve

            mrr "So that's it, you just want to give up on us?"

            #scene v10msf2c
            scene v10msf1a
            with dissolve

            ro "I didn't give up on us Lucious, you did. Please, just go."

            #scene v10msf2a
            scene v10msf1
            with dissolve

            mrr "When everything is said and done, you're gonna regret this."
            stop music fadeout 3
            play music "music/v10/Track Scene 25_2.mp3" fadein 2
            scene v10msf3
            with dissolve
            pause 0.75
    
    scene v10msf4 # FPP. Show MS rose, crying mouth open, FPP now from right infront of door to have conversation with ms rose.
    with dissolve

    ro "*Sighs* I'm sorry. He has no respect for anyone but himself."

    menu:
        "Insult him":
            $ reputation.add_point(Reputations.TROUBLEMAKER)
            scene v10msf4a # FPP. same camera as v10msf4, Show MS rose, crying mouth closed, FPP now from right infront of door to have conversation with ms rose.
            with dissolve

            u "I can't stand people like that."

            scene v10msf4
            with dissolve

            ro "Tell me about it."

        "Comfort her":
            scene v10msf4a 
            with dissolve

            u "Regardless, I think you handled the situation right."

            scene v10msf4b # FPP. same camera as v10msf4, Show MS rose, crying, slight smile, mouth open, FPP now from right infront of door to have conversation with ms rose.
            with dissolve

            ro "Thank you."

    scene v10msf4a
    with dissolve
    u "Do you feel safe here alone?"

    if v10_ms_r_interfere:
        scene v10msf4b
        with dissolve
        ro "Yes I'll be fine, I don't think he'd risk coming back after this."
        ro "Thank you though, it means a lot to me that you came. Who knows what would have happened if you hadn't."

        scene v10msf4a
        with dissolve

        u "It looked like you were handling him just fine, haha."

    else:
        scene v10msf4
        with dissolve

        ro "Yes I'll be fine, I don't think he'd risk coming back after this. And thanks for coming, I'm glad he left before you arrived though."

        scene v10msf4a
        with dissolve

        u "Yeah, it looked like you were handling him just fine, haha."

    scene v10msf4
    with dissolve
    ro "I swear, I have no idea how he found me. Knowing him he just sent someone to find me."

    scene v10msf4a
    with dissolve

    u "Sent someone?"

    scene v10msf4
    with dissolve

    ro "He knows a lot of people and is involved in a lot. He can just about do anything he wants."

    scene v10msf4a
    with dissolve

    u "That's crazy. Just call me if he ever makes you uncomfortable again. I'll rush here and put him in his place."

    scene v10msf5 # TPP. Show MS rose. Touching MC on the cheek, smiling, mouth open
    with dissolve

    ro "You're too sweet."

    menu:
        "Make a move":
            $ ms_rose.relationship = Relationship.KISS
            $ reputation.add_point(Reputations.BOYFRIEND)
            scene v10msf5a # TPP. same camera as v10msf5, Show MS rose. Touching MC on the cheek, smiling,MC hand on Ms Rose Waist.
            with dissolve

            pause 1

            scene v10msf5b # TPP. same camera as v10msf5, Show MS rose. hand on MC's shoulder, Now body to body with MC, MC hand on Ms. Rose's back.
            with dissolve

            pause 1

            play sound "sounds/kiss.mp3"

            scene v10msf6 # FPP. Show Close up of Ms. Rose and MC kissing.
            with dissolve

            pause 1.25

            scene v10msf5c # TPP. same camera as v10msf5, Show MS rose. Now having stepped back, embarrased smile, mouth open
            with dissolve

            $ grant_achievement("forbidden_romance")
            ro "Wow uhm... thank you [name]. For everything. I need to get back to work. Really, thank you."

            scene v10msf4c # FPP. same camera as v10msf4, Now Show Ms Rose closing the door.
            with dissolve

            u "(Did I really just do that?)"

        "Don't make a move":
            scene v10msf4a
            with dissolve
            u "That's how I was raised."

            scene v10msf4
            with dissolve

            ro "If only everyone was..."

            scene v10msf4a
            with dissolve

            u "I guess if there's nothing else, uhm I'll get back home. Call me if you need anything, Ms. Rose."

            scene v10msf4b
            with dissolve

            ro "Uh, yeah. Thank you, [name]."

    scene v10msf7 # TPP. Show MC Leaving, Nora on the sidewalk (as far away from house as is viable in shot), Nora phone to side of head, mouth open
    with dissolve

    u "(What's Nora doing here?)"

    no "Hey, so I just got to my stepmom's house. I'm gonna have to let you go."

    u "(Wait, her stepmom? Is Nora Ms. Rose's stepdaughter? What the fuck?!)"
    stop music fadeout 3
    jump v10_amber_skatepark
