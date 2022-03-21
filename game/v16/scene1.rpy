# SCENE 1: Tom Fight Scene
# Locations: Tom/MC fight place
# Characters: RILEY (Outfit: 2), MC (Outfit: 1), TOM (outfit: 1)
# Time: Night

label v16_start:
    play music "<from 28>music/v15/Track Scene 49.mp3" fadein 2 ### from 28 ?
label v16s1:
### ERROR: 1) Fight with Tom

# -We fight Tom with the new fight mechanic system-

# -if MC lost [Checkpoint 1.1]

label v16s1_lose:
    scene v16s1_lose_1 # TPP. MC on the ground, holding his stomach, he is in pain, mouth closed, Riley running towards him, very worried, mouth open, Tom walking away, grinning, mouth closed
    with fade

    play music "music/v15/Track Scene 28_2.mp3" fadein 2

    ri "Oh, my God, [name]! Are you okay?"
    
    scene v16s1_lose_1a # TPP. Riley now standing next to MC, Riley very worried, mouth closed, MC still in pain, looking up at Riley, MC mouth open, in pain, Tom not in shot anymore
    with dissolve

    u "*Grunts* I've felt better."

    scene v16s1_lose_1b # TPP. Show Riley helping MC up, MC in pain, Riley very worried, both mouths closed
    with dissolve

    pause 0.75

    scene v16s1_lose_2 # FPP. MC and Riley standing up, Riley has her arm around him, helping him keep standing up, MC looking at Riley, Riley looking at MC, Riley very worried, mouth open
    with dissolve

    ri "Seriously, [name], are you okay?"

    scene v16s1_lose_2a # FPP. Same as v16s1_lose_2a. Riley mouth closed, very worried
    with dissolve

    menu:
        "I'm fine":
            u "Yeah, I'm fine."

            u "He just got a few lucky hits, that's all."

            scene v16s1_lose_2
            with dissolve

            ri "Ha, right."

        "It hurts like hell":
            scene v16s1_lose_2a
            #with dissolve
            
            u "Honestly, no. It hurts like hell."

            scene v16s1_lose_2
            with dissolve

            ri "I can't even imagine... *Sighs*"

            scene v16s1_lose_2a
            with dissolve

            u "I don't think I've ever been hit that hard before."

    scene v16s1_lose_2
    with dissolve

    ri "Where does it hurt most?"

    scene v16s1_lose_2a
    with dissolve

    u "Is everywhere an option?"

    scene v16s1_lose_2
    with dissolve

    ri "Tom is crazy! He just came out of nowhere and started demanding things about Charli and-"

    scene v16s1_lose_2a
    with dissolve

    u "I know, I heard."

    scene v16s1_lose_2
    with dissolve

    ri "*Sighs* Okay, let's just head out before he decides to come back."

    scene v16s1_lose_2b # FPP. Same as v16s1_lose_2, Riley slightly different pose, still worried, mouth open
    with dissolve

    ri "You can walk, right?"

    scene v16s1_lose_2c # FPP. Same as v16s1_lose_2b, but Riley mouth closed
    with dissolve

    u "Yeah... *Grunts* I'm just tired as fuck, and everything hurts. I'm so ready to go home."

    scene v16s1_lose_2b
    with dissolve

    ri "I'm sure you are, but sadly, you're not going home."

    scene v16s1_lose_2c
    with dissolve

    u "Wha-"

    scene v16s1_lose_2
    with dissolve

    ri "You're coming home with me. I need to keep an eye on you."

    scene v16s1_lose_2a
    with dissolve

    u "I'm just going to sleep, ha. Are you going to watch me sleep?"

    scene v16s1_lose_2
    with dissolve

    ri "Yes. Look for signs of concussion, make sure you wake up in the morning, things like that."

    scene v16s1_lose_2a
    with dissolve

    u "Ugh, Riley..."

    scene v16s1_lose_2b
    with dissolve

    ri "[name]... Who knows what injuries you have?"

    if "v14_threesome" in sceneList:
        scene v16s1_lose_2d # FPP. Same as v16s1_lose_2, Riley slight smirk, mouth open
        with dissolve

        ri "Especially since this isn't the first time you've been knocked on that big head of yours..."

        scene v16s1_lose_2e # FPP. Same as v16s1_lose_2d, Riley slight smirk, mouth closed
        with dissolve

        u "Hey, my head is not that big!"

        scene v16s1_lose_2d
        with dissolve

        ri "*Giggles* Whatever. You know what I mean."

    scene v16s1_lose_2
    with dissolve

    ri "It could be nothing, it could be something. Just let me take care of you..."

    scene v16s1_lose_2a
    with dissolve

    u "(Hmm... I wouldn't mind a tiny bit of attention... But then again, I'm not sure I'm in the mood for anything besides my pillow and a blanket.)"

    scene v16s1_lose_2b
    with dissolve

    ri "Please?"

    scene v16s1_lose_2c
    with dissolve

    menu:
        "Go home alone":
            u "Honestly, I just want to go home and crash in my own bed. I'm exhausted."

            scene v16s1_lose_2b
            with dissolve

            ri "*Sigh* Are you sure? I can make you a cup of tea and find a nice frozen pack of peas."

            scene v16s1_lose_2a
            with dissolve

            u "Haha, thanks for the offer, but no. Sorry."

            scene v16s1_lose_2f # FPP. Same as v16s1_lose_2, Riley eye rolling, slight smile, mouth open
            with dissolve

            ri "It's fiiiine..."

            scene v16s1_lose_2g # FPP. Same as v16s1_lose_2f, Riley looking at MC, not eye rolling, slight smile, mouth closed
            with dissolve

            ri "Well, make sure you get lots of rest, and send me an update when you're feeling better, okay?"

            scene v16s1_lose_2h # FPP. Same as v16s1_lose_2g, Riley slight smile, mouth closed
            with dissolve

            u "Okay, I will. Thank-"

            scene v16s1_lose_2g
            with dissolve

            ri "Stop thanking people when you're the hero."

            if riley.relationship >= Relationship.FWB:
                scene v16s1_lose_3 # TPP. Riley giving MC a quick kiss on the cheek, MC feeling pain, mouth open
                with vpunch

                u "Ow!"

                scene v16s1_lose_2
                with dissolve

                ri "Oh! Sorry, I-"

                scene v16s1_lose_2h
                with dissolve

                u "*Chuckles* Kidding."

                scene v16s1_lose_2g
                with dissolve

                ri "Ugh! Get out of here before I punch you a few times myself."

                scene v16s1_lose_2h
                with dissolve

                u "Ha, okay. See you later."
            
            else:
                scene v16s1_lose_2h
                with dissolve

                u "Ha, okay. I'll try. See you later."

            scene v16s1_lose_2g
            with dissolve

            ri "I hope!"

            scene v16s1_lose_4 # TPP. MC walking away in pain, mouth closed, Riley watching him go, she is worried, mouth closed
            with dissolve

            pause 0.75

        "Go home with Riley":
            $ v16_home_riley = True

            u "..."

            scene v16s1_lose_2h
            with dissolve

            u "Can I have ice cream?"

            scene v16s1_lose_2g
            with dissolve

            ri "Haha... Yeah, you can have ice cream."

            scene v16s1_lose_2h
            with dissolve

            u "And you're going to bandage me up, right?"

            scene v16s1_lose_2g
            with dissolve

            ri "Mmhmm... Maybe I can even find you a pink band-aid. Would you like that, princess?"

            scene v16s1_lose_2h
            with dissolve

            u "Well-"

            scene v16s1_lose_2g
            with dissolve

            ri "*Laughs* Okay, come on. Let's get out of here."

            scene v16s1_lose_2h
            with dissolve

            u "But the pink band-aid..."

            scene v16s1_lose_2g
            with dissolve

            ri "Shh... There, there..."

            scene v16s1_lose_4a # TPP. Same angle as v16s1_lose_4, Riley and MC walking away, Riley still supporting him with her arm around her as they walk away, MC in pain, Riley worried, mouths closed
            with dissolve

            pause 0.75

    jump v16s1_end

label v16s1_win:
    scene v16s1_win_1 # TPP. Tom is on the ground, in pain, MC is looking at him, MC very angry, both mouths closed
    with dissolve

    pause 0.75
    play music "music/v15/Track Scene 28_2.mp3" fadein 2

    scene v16s1_win_2 # TPP. Show Tom walking away in pain in the background, Riley running towards MC, Riley excited, mouth open, MC mouth closed, slight smile, looking at Riley
    with dissolve
    
    ri "[name], holy shit! You kicked his ass!"

    scene v16s1_win_3 # FPP. Riley standing in front of MC, slight smile, mouth closed
    with dissolve

    u "You sound surprised... Ha."

    scene v16s1_win_3a # FPP. Same as v16s1_win_3, Riley slightly worried, mouth open
    with dissolve

    ri "No, no, it's not that...It's just-"

    scene v16s1_win_3b # FPP. Same as v16s1_win_3, Riley slight smile, mouth open
    with dissolve

    ri "I was worried about you, for a second. Obviously, I don't need to be, though."

    scene v16s1_win_3
    with dissolve

    u "I'm just glad you aren't hurt. You aren't, right?"

    scene v16s1_win_3b
    with dissolve

    ri "Yeah, no, I'm fine. Thanks for dealing with that... psycho."

    scene v16s1_win_3
    with dissolve

    u "Of course, are you kidding?"

    scene v16s1_win_3a
    with dissolve

    ri "I don't know what would've happened to me if you hadn't shown up like that."

    scene v16s1_win_3
    with dissolve

    menu:
        "We got lucky":
            scene v16s1_win_3c # FPP. Same as v16s1_win_3a, Riley slightly worried, mouth closed
            with dissolve

            u "Yeah, we got lucky. I was just in the right place at the right time."

            scene v16s1_win_3a
            with dissolve

            ri "I know..."

            scene v16s1_win_3c
            with dissolve

            u "I heard the shouting, and... I wasn't about to let that asshole lay a finger on you."

        "Always count on me":
            u "You can always count on me, Riley."

            scene v16s1_win_3b
            with dissolve

            ri "Ha, thanks."

            scene v16s1_win_3c
            with dissolve

            u "He won't bother you again, but if he tries, you let me know, yeah?"

            scene v16s1_win_3b
            with dissolve

            ri "Of course."

    scene v16s1_win_3d # FPP. Same as v16s1_win_3, Riley slightly scared, mouth open
    with dissolve

    ri "I'm still shaking..."

    scene v16s1_win_3e # FPP. Same as v16s1_win_3d, Riley slightly scared, mouth closed
    with dissolve

    u "You're safe now, he's gone."

    scene v16s1_win_3d
    with dissolve

    ri "Yeah, I know. It's just that I've never been threatened like that before, you know?"

    ri "I just don't feel safe going home alone right now."

    scene v16s1_win_3e
    with dissolve

    u "(Hmm, should I offer to stay with Riley? Or just enjoy a peaceful night at home?)"

    menu:
        "Go home alone":
            u "You'll be okay, I promise. Just order a cab."

            scene v16s1_win_3d
            with dissolve

            ri "I guess so... You wouldn't wanna come over, would you?"

            scene v16s1_win_3e
            with dissolve

            u "Not tonight, Riley. I'm sorry. Especially after all of that, this day has been the longest of my life, haha."

            scene v16s1_win_3d
            with dissolve

            ri "Yeah, I bet you're exhausted. I get it."

            scene v16s1_win_3e
            with dissolve

            u "Yeah, I'm just going to crash, I think."

            scene v16s1_win_3d
            with dissolve

            ri "Okay, well...Thanks again."

            if riley.relationship >= Relationship.FWB:
                scene v16s1_win_4 # TPP. Riley giving MC a kiss on the cheek
                with dissolve

                pause 0.75

                scene v16s1_win_3 
                with dissolve

                u "Of course."

            else:
                scene v16s1_win_3
                with dissolve

                u "Anytime, Riley. Goodnight."

                scene v16s1_win_3b
                with dissolve

                ri "Night."

            scene v16s1_win_5 # TPP. Show MC walking away, slight smile, mouth closed, Riley watchign him walk away, she is slightly scared, mouth closed
            with dissolve

            pause 0.75

        "Go home with Riley":
            $ v16_home_riley = True
            
            scene v16s1_win_3
            with dissolve

            u "How about I come with you?"

            scene v16s1_win_3b
            with dissolve

            ri "Really?!"

            scene v16s1_win_3
            with dissolve

            u "Of course. I can't let you walk home alone in the dark, especially if you're not feeling safe, ha."

            scene v16s1_win_3b
            with dissolve

            ri "Thanks, [name]... You don't know how much this means to me. I'll make it up to you, I swear!"

            scene v16s1_win_3
            with dissolve

            u "Don't worry, I'm sure we'll have fun."

            scene v16s1_win_3b
            with dissolve

            ri "Oh, we will... *Chuckles*"
            
            scene v16s1_win_5a # TPP. Same angle as v16s1_win_5, Riley and MC walking away together, both slightly smiling, mouths closed
            with dissolve

            pause 0.75

    jump v16s1_end

label v16s1_end:
    jump v16s2