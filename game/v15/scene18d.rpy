# SCENE 18d: Lauren Halloween Party End of Night
# Locations: Deer's house
# Characters: CHRIS (Outfit: Boxer costume), LAUREN (Outfit: Spider Costume), IMRE (Outfit: Cowboy costume), MC (Outfit: Stripper costume)
# Time: 

label v15s18d:
    scene v15s18d_1 # TPP. Show Lauren holding the door open for all the guest to leave, Lauren slight smile, mouth closed.
    with fade

    pause 0.75
    
    scene v15s18d_2 # TPP. Show MC standing by the stairs with a drink in his hand watching people leave, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v15s18d_3 # TPP. Show Chris stopped at Lauren holding the door open, Both slight smile, Chris mouth open, Lauren mouth closed.
    with dissolve

    ch "Happy birthday, Lauren. It was a great party."

    scene v15s18d_3a # TPP. Show Chris stopped at Lauren holding the door open, Both slight smile, Chris mouth closed, Lauren mouth open.
    with dissolve

    la "Thank you, Chris! I'm glad you had a good time."

    scene v15s18d_3
    with dissolve

    ch "Thanks for inviting me. I appreciate it."

    scene v15s18d_4 # TPP. Show Chris exitting the house and leaving the party, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s18d_2a # TPP. Show MC standing by the stairs with a drink Imre stepping infront of him.
    with dissolve

    pause 0.75

    scene v15s18d_5 # FPP. MC looking at Imre, Imre looking at MC, Imre slight smile, mouth open.
    with dissolve

    imre "Let's see how you did with the list, huh?"

    hide screen v15_imre_checklist_icon with dissolve

    scene v15s18d_6 # FPP. MC looking down at his and Imre's hands as MC hands Imre the list of challenges.
    with dissolve
    
    pause 0.75

    if len(checklist.get_completed()) > 4:
        scene v15s18d_5a # FPP. MC looking at Imre, Imre looking at the List, Imre slight smile, mouth open.
        with dissolve

        imre "Oh! You actually did pretty well..."

        if len(checklist.get_completed()) == 8:
            $ grant_achievement("taskmaster")

        imre "I'm impressed."

        scene v15s18d_7 # TPP. Shot of Imre putting the challenge list in his pocket while infront of MC, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s18d_5b # FPP. MC looking at Imre, the list gone, Imre looking at MC, Imre slight smile, mouth closed.
        with dissolve

        u "Ha, thanks. It's a fun side game to play while you're partying."

        scene v15s18d_5
        with dissolve

        imre "I bet it is, haha! I still haven't found out exactly how much fun... But one day I hope to."

        scene v15s18d_5b
        with dissolve

        u "I'm sure you will."

        scene v15s18d_5
        with dissolve

        imre "Thanks, man."

        imre "The night isn't over yet. You can still get at least one more, like the sex."

    elif len(checklist.get_completed()) > 0:
        scene v15s18d_5a
        with dissolve

        imre "Hey! You did alright."

        scene v15s18d_5c # FPP. MC looking at Imre, Imre looking at the List, Imre slight smile, mouth closed.
        with dissolve

        u "Yeah, nothing too crazy. It was fun, though."

        scene v15s18d_7
        with dissolve

        pause 0.75

        scene v15s18d_5
        with dissolve

        imre "I'm proud of you."

        scene v15s18d_5b
        with dissolve

        u "*Laughs* Thanks, Imre..."

        scene v15s18d_5
        with dissolve

        imre "The night isn't over yet. You can still get at least one more, like the sex."

    else:
        scene v15s18d_5a
        with dissolve

        imre "What? Nothing?! *Laughs*"

        scene v15s18d_7
        with dissolve

        pause 0.75

        scene v15s18d_5
        with dissolve

        imre "Looks like we got the same score."

        scene v15s18d_5b
        with dissolve

        u "Yeah, what can I say? Maybe I should've tried harder..."

        scene v15s18d_5
        with dissolve

        imre "Trust me, dude. This thing is cursed."

        imre "The night isn't over yet. You can still get at least one, like the sex."


    scene v15s18d_1a # TPP. Show Lauren holding the door open for all the guest to leave, now looking over in Imre and MC's direction, Lauren with a raised brow, confused, mouth open.
    with dissolve
    
    la "One what? Sex?"

    scene v15s18d_8 # FPP. Show Lauren walking over to MC and Imre, Lauren slightly confused, mouth open.
    with dissolve

    pause 0.75

    scene v15s18d_5d # FPP. MC looking at Imre, Imre looking at Lauren, Imre slight smile, mouth open.
    with dissolve

    imre "Oh, shit! Hi, Lauren. *Laughs* You really snuck up on us there."

    imre "Hey, uh... It was a great party! I'll see you later, tomorrow... Happy birthday!"

    scene v15s18d_8a # FPP. Lauren standing infront of MC, MC looking at Lauren, Lauren looking at Imre, Lauren confused smile, mouth open.
    with dissolve

    la "Uh, thank you? Haha."

    scene v15s18d_9 # TPP. Show Imre walking towards the front door of the Deer's house, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s18d_10 # FPP. MC looking past Lauren at Imre, Imre at the front door looking at MC, Imre holding up his pointer finger and his other hand into a clenched fist as he is imitating intercourse, Imre slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s18d_10a # FPP. MC looking past Lauren at Imre, Imre at the front door looking at MC, Imre putting his pointer finger into his other hand that is a clenched fist as he is imitating intercours, Imre slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s18d_8b # FPP. Lauren standing infront of MC, MC looking at Lauren, Lauren looking at MC, Imre in the background, Lauren confused smile, mouth open.
    with dissolve

    la "What was he talking about?"

    scene v15s18d_8c # FPP. Lauren standing infront of MC, MC looking at Lauren, Lauren looking at MC, Imre in the background, Lauren confused smile, mouth closed.
    with dissolve

    u "Haha, ah... You know Imre, always saying ridiculous things."

    scene v15s18d_10b # FPP. MC looking past Lauren at Imre, Imre at the front door looking at MC, Imre flipping off MC, laughing.
    with dissolve

    pause 0.75

    scene v15s18d_11 # TPP. Show Imre walking away from the house, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s18d_8d # FPP. Lauren standing infront of MC, MC looking at Lauren, Lauren looking at MC, Imre gone, Lauren confused smile, mouth open.
    with dissolve

    la "He thinks you should have sex with me?"

    scene v15s18d_8e # FPP. Lauren standing infront of MC, MC looking at Lauren, Lauren looking at MC, Imre gone, Lauren confused smile, mouth closed.
    with dissolve

    u "(Fuck.) Um, yeah. That's basically what he was suggesting, haha."

    menu:
        "Try to have sex":
            $ add_point(KCT.BRO)
            
            scene v15s18d_8e
            with dissolve

            u "But I'd only want to if you wanted-"

            if lauren.relationship.value >= Relationship.GIRLFRIEND.value:
                $ add_point(KCT.BOYFRIEND)
                $ v15s18_LaurensBed = True

                if gift_card_50 in mc.inventory:
                    scene v15s18d_8i # FPP. Lauren standing infront of MC, MC looking at Lauren, Lauren looking at MC, Imre gone, Lauren fake smile, mouth open.
                    with dissolve

                    la "To be honest, you got me a gift card for my birthday."

                    scene v15s18d_8j # FPP. Lauren standing infront of MC, MC looking at Lauren, Lauren looking at MC, Imre gone, Lauren fake smile, mouth closed.
                    with dissolve

                    u "Yeah..."

                    scene v15s18d_8i
                    with dissolve

                    la "You didn't put much thought into it, did you? *Giggles*"

                    scene v15s18d_8j
                    with dissolve

                    u "I was in the store for ages."

                    scene v15s18d_8i
                    with dissolve

                    la "I don't know about that..."

                    scene v15s18d_8j
                    with dissolve

                    u "I'm sorry, ha."

                    scene v15s18d_8f
                    with dissolve

                    la "Don't worry about it..."

                    la "Anyway, you can sleep in my bed tonight, but there's not going to be any sex."

                    scene v15s18d_8h
                    with dissolve

                    u "That's perfectly fine. Thank you."

                    scene v15s18d_12b
                    with dissolve
                    
                    pause 0.75

                    stop music fadeout 3

                    jump v15s18f

                else:
                    scene v15s18d_8f
                    with dissolve

                    la "Hmm..."

                    la "I think you've earned it."

                    scene v15s18d_8h
                    with dissolve

                    u "Yeah?"

                    scene v15s18d_8f
                    with dissolve

                    la "Yeah, especially after the gift you gave me, hehe. Best boyfriend ever."

                    scene v15s18d_14a # TPP. Show MC and Lauren having a passionate kiss
                    with dissolve

                    pause 0.75

                    scene v15s18d_8f
                    with dissolve

                    la "And now you can give me an extra special birthday treat."

                    scene v15s18d_8h
                    with dissolve

                    u "Don't mind if I do."

                    scene v15s18d_12c # TPP. Show Lauren leading MC upstairs by his hand, MC slight smile, mouth closed, Lauren biting her lip.
                    with dissolve

                    pause 0.75

                    stop music fadeout 3

                    jump v15s18e

            else: 
                if kct == "loyal" and lauren.relationship.value >= Relationship.KISS.value and not v11_lauren_caught_aubrey: # and not "v12_lauren" in sceneList, but this is implied by not having Lauren GIRLFRIEND
                    $ v15s18_LaurensBed = True
                    call screen kct_popup
                    
                    scene v15s18d_8f
                    with dissolve

                    la "You know... I still haven't even had sex. *Laughs*"

                    scene v15s18d_8h
                    with dissolve

                    u "Ha."

                    scene v15s18d_8f
                    with dissolve

                    la "I think it's time."

                    scene v15s18d_8h
                    with dissolve

                    u "You do?"

                    scene v15s18d_8f
                    with dissolve

                    la "And I think you're the right person for me to do it with... You know, for the first time?"

                    scene v15s18d_8h
                    with dissolve

                    u "You- Wait, really?"

                    scene v15s18d_8k # FPP. Lauren standing infront of MC, MC looking at Lauren, Lauren looking at the ground, Lauren nervous, mouth open.
                    with dissolve

                    la "Yeah... I..."

                    la "Come on, before I change my mind. *Laughs*"

                    scene v15s18d_12b
                    with dissolve

                    pause 0.75

                    stop music fadeout 3

                    jump v15s18e
                
                else:
                    if lauren.relationship.value >= Relationship.KISS.value and not v11_lauren_caught_aubrey:
                        call screen kct_popup(required_kct="loyal")
                
                    scene v15s18d_8f
                    with dissolve

                    la "Ha. I don't think that's going to happen."

                    la "You can sleep here tonight if you need to, but only on the couch."

                    scene v15s18d_8h
                    with dissolve

                    u "Oh, okay. Yeah, that's fine."

                    scene v15s18d_8f
                    with dissolve

                    la "Let me grab you a pillow and a blanket."

                    scene v15s18d_8h
                    with dissolve

                    u "Okay. Thanks."

                    u "(Damn, I just got shut down hard. Ouch.)"

                    scene v15s18d_12
                    with dissolve

                    pause 0.75

                    scene v15s18d_12a 
                    with dissolve

                    pause 0.75

                    scene v15s18d_8f
                    with dissolve

                    la "Sleep tight!"

                    scene v15s18d_8h
                    with dissolve

                    u "You too, birthday girl. Goodnight."

                    scene v15s18d_13 # TPP. Show just MC sitting on the couch with the blanket and pillow the lights in the room on, slight smile, mouth closed
                    with dissolve

                    pause 0.75

                    scene v15s18d_13a # TPP. Show just MC sitting on the couch with the blanket and pillow the lights in the room off, slight smile, mouth closed
                    with dissolve

                    pause 0.75
                    
                    stop music fadeout 3
                    
                    jump v15s18f

        "Don't try":
            u "But I don't want to do that to you, just ignore him. He's trying to get me to play this stupid game."

            if lauren.relationship.value >= Relationship.GIRLFRIEND.value:
                scene v15s18d_8g # FPP. Lauren standing infront of MC, MC looking at Lauren, Lauren looking at MC, Imre gone, Lauren confused, mouth open.
                with dissolve

                la "You don't want to have sex with your girlfriend on her birthday?"

            else:
                $ add_point(KCT.BOYFRIEND)
                
                scene v15s18d_8f # FPP. Lauren standing infront of MC, MC looking at Lauren, Lauren looking at MC, Imre gone, Lauren slight smile, mouth open.
                with dissolve

                la "Haha, yeah... I figured that's what you were going to say."

            scene v15s18d_8e
            with dissolve

            u "I'm kind of struggling to keep my eyes open right now, haha."

            scene v15s18d_8f
            with dissolve

            la "Ah, okay. *Chuckles*"

            scene v15s18d_8h # FPP. Lauren standing infront of MC, MC looking at Lauren, Lauren looking at MC, Imre gone, Lauren slight smile, mouth closed.
            with dissolve

            u "It's been a long day, but what an amazing party! Did you enjoy it?"

            scene v15s18d_8f
            with dissolve

            la "Yeah, it was great! I'm so happy everyone had a good time."

            if lauren.relationship.value >= Relationship.GIRLFRIEND.value:
                $ v15s18_LaurensBed = True
                scene v15s18d_8f
                with dissolve

                la "Let's head to bed now, yeah? I'm ready for a cozy birthday sleep... You can be the big spoon."

                scene v15s18d_8h
                with dissolve

                u "Haha... Okay, little spoon. Let's go."

                scene v15s18d_14 # TPP. Show MC kissing Lauren's forehead, Lauren slight smile, eyes closed, mouth closed.
                with dissolve

                pause 0.75

                scene v15s18d_12b # TPP. Show Lauren and MC walking up the stairs, both slight smile, mouth closed.
                with dissolve

                pause 0.75

            else:
                la "You don't have to go home tonight, by the way. You can just sleep on the couch if you want."

                scene v15s18d_8h
                with dissolve

                u "That would be great, actually."

                scene v15s18d_8f
                with dissolve

                la "I'm gonna grab you a pillow and a blanket, I'll be right back."

                scene v15s18d_8h
                with dissolve

                u "Thanks, Lauren."

                scene v15s18d_12 # TPP. Show Lauren walking up the stairs empty handed.
                with dissolve

                pause 0.75

                scene v15s18d_12a # TPP. Show Lauren walking down the stairs with a blanket and pillow.
                with fade

                pause 0.75

                scene v15s18d_8f
                with dissolve

                la "Sleep tight!"

                scene v15s18d_8h
                with dissolve

                u "You too, birthday girl. Goodnight."

                scene v15s18d_13 # TPP. Show just MC sitting on the couch with the blanket and pillow the lights in the room on, slight smile, mouth closed
                with dissolve

                pause 0.75

                scene v15s18d_13a # TPP. Show just MC sitting on the couch with the blanket and pillow the lights in the room off, slight smile, mouth closed
                with dissolve

                pause 0.75

            stop music fadeout 3

            jump v15s18f