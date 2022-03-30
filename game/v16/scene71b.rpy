# SCENE 71b: The Dean returns
# Locations: Dean's Office, Hallway outside Dean's Office
# Characters: DEAN (Outfit: 1), PENELOPE (Outfit: 1), MC (Outfit: 5)
# Time: Friday Morning

label v16s71b: ### ERROR: 71b) The Dean returns
    if "v16_penelope" not in sceneList: # -if MC and Penelope did not have sex-
        # -Continuing from Scene 71, MC and Penelope are sat on the couch looking at Oscar sleeping-

        # -The Dean enters, looking straight over to Oscar-
        scene v16s71b_1 # TPP Dean enters through her office door
        with dissolve

        pause 0.75

        scene v16s71b_1a # TPP Close up: Oscar sleeping on the couch between MC and penelope
        with dissolve

        de "Aw, he's having his mid-morning nap."        

        scene v16s71b_2 # FPP Dean(neutral, mouth open) looking at MC and Penelope (OC)
        with dissolve

        de "Has he been good for you?"

        # -Penelope and MC stand-
        scene v16s71b_2a # TPP MC(smiling, mouth closed) and Penelope(smiling, mouth closed) standing up from the couch, looking at the Dean(nuetral, mouth closed)
        with dissolve

        pause 0.75
        
        scene v16s71b_3 # FPP Penelope (smiling, mouth open) looking the Dean (nuetral, mouth closed). 
        with dissolve

        pe "He's been perfect."

        scene v16s71b_2b # FPP Dean(neutral, mouth closed) looking at MC and Penelope (OC)
        with dissolve

        u "Yeah, we played for a while and then fed him some food."

        scene v16s71b_2
        with dissolve

        de "Oh, great. My little angel..."

        scene v16s71b_2b
        with dissolve

        u "(Angel...? Haha.)"

        scene v16s71b_2
        with dissolve

        de "Thanks again for doing this. I may call upon you again in the future, Penelope. If you're willing, that is."

        scene v16s71b_3
        with dissolve

        pe "Any time, Dean Harrison. Oscar is fun to be around."

        scene v16s71b_3a # FPP Penelope (smiling, mouth closed) and the Dean (neutral, mouth closed) looking at MC.
        with dissolve

        u "Yeah, I'm happy to help too."

        scene v16s71b_2c # FPP Dean(smiling, mouth open) lookingat MC and Penelope (OC)
        with dissolve

        de "Great. You guys are free to go now, thanks!"

        # -Penelope and MC exit with the Dean watching them go, all smiling. Oscar sound asleep-
        scene v16s71b_4 # TPP Penelope(smiling, mouth closed) and MC (smiling, mouth closed) exiting through the Dean's office door (POV from Hallway). The Dean in the background, smiling, watching them leave.
        with dissolve

        pause 0.75

    else: # -if MC and Penelope had sex-

        # -Continuing from Scene 71a, MC and Penelope are sat on the couch pulling on their last item of clothing, then they're full dressed again-
        
        scene v16s71a_5 # TPP Same as v16s71a_17(not a typo-- used this is the base image). Penelope and MC(concerned, mouths closed) now have their shirts on (fully clothed) looking at each other 
        with dissolve

        pause 0.75

        play sound "sounds/dooropen.mp3"

        scene v16s71a_5a # TPP Same as v16s71a_5 but Penelope and MC(concerned, mouths closed) both heads turned toward the direction of the Dean's door (OC)
        with dissolve

        pause 0.75
               
        # -The Dean enters, carrying Oscar. She puts him on the ground, and he goes to sit on his bed-        
        scene v16s71b_6 # FPP Dean (angry, mouth closed) stands in front of her closed door, holding Oscar.
        with dissolve

        pause 0.75

        scene v16s71b_6a # TPP Close on the Dean's hands putting Oscar on the floor by her feet.
        with dissolve

        pause 0.75

        scene v16s71b_2d # FPP Dean(angry, mouth open) looking at MC and Penelope (OC)
        with dissolve

        de "Why have I just found Oscar on his own, sniffing at a locker?!"

        scene v16s71b_3b # FPP Penelope (concerned, mouth open) looking the Dean (angry, mouth closed). 
        with dissolve

        pe "Dean Harrison! We were just-"

        scene v16s71b_2d
        with dissolve

        de "How did he get out if the two of you were watching him?!"

        scene v16s71b_2e # FPP Dean(angry, mouth closed) looking at MC and Penelope (OC)
        with dissolve

        u "(Shit, shit, shit... Think quick!)"        

        # -TIMED EVENT
        # -MC chooses event1 or event2
        # -event1 Lie
        # -event2 Be honest
        menu (fail_label="v16s71b_honest"):

        # -If time runs out before choice is made, MC will Be honest-

            "Lie": # -if Lie
                u "Um, we were just trying to train him to come back to us if he was ever lost."

                scene v16s71b_2d
                with dissolve

                de "Oh, really? And how were you doing that?"

                scene v16s71b_2e
                with dissolve

                u "Just by calling him and whistling."

                de "Hmm..."

                scene v16s71b_2d
                with dissolve

                de "Well, it looks like it didn't work. Wouldn't you say?"

                scene v16s71a_3c # FPP Penelope (neutral, mouth open) looking the Dean (angry, mouth closed). 
                with dissolve

                pe "I guess he needs more training. Sorry, Dean Harrison."

                scene v16s71b_2d
                with dissolve

                de "Not sure if it was the best idea to risk losing my dog just to test out a trick, [name]."

                de "It sounds rather foolish in all honesty. I would've thought that you two are more intelligent than that."                

            "Be honest": # -if Be honest
                label v16s71b_honest:

                scene v16s71b_2e:
                with dissolve

                u "We're sorry, Dean Harrison. We just got distracted and didn't notice that he slipped out."

                scene v16s71a_3c
                with dissolve

                pe "Yeah, seriously, I'm so sorry! He was literally right there just a few minutes ago..."

                scene v16s71b_2d
                with dissolve

                de "*Sighs* This is disappointing, Penelope. I didn't expect you to let me down with such a simple task."
                
                de "Anything could have happened to him!"

                scene v16s71b_3b
                with dissolve

                pe "I know... I'm really sorry."                

        # -Regardless of lying or not-
        
        # -The Dean looks over to Oscar's empty food bowl-
        scene v16s71a_7 # TPP Close on Oscar's empty food bowl.
        with dissolve

        pause 0.75

        scene v16s71b_2d
        with dissolve

        de "And you haven't fed him?!"        

        de "What did I say before I left?"

        scene v16s71b_3b
        with dissolve

        pe "You asked us to feed him before you came back..."

        scene v16s71b_2d
        with dissolve

        de "And you couldn't even do that?"

        scene v16s71b_2e
        with dissolve

        u "We can, yeah. We just-"

        scene v16s71b_2d
        with dissolve

        de "You just nothing. Next time I have a meeting I'll just take him with me."

        scene v16s71b_3b
        with dissolve

        pe "Dean Harrison, we just lost track of the time. That's all. We're very sorry."

        scene v16s71b_2d
        with dissolve

        de "Oscar can't fill his stomach on your worthless apologies, can he?"

        scene v16s71b_3b
        with dissolve

        pe "I'm-"

        scene v16s71b_2d
        with dissolve

        de "Leaving. You're both leaving."

        de "Before I really lose my temper."

        scene v16s71a_3c
        with dissolve

        pe "Yes, Ma'am. Come on, [name]."

        scene v16s71b_2e
        with dissolve

        u "(It's no fun making the Dean go psycho, but at least I got laid!)"

        # -Penelope and MC exit with the Dean watching them go, angry-
        scene v16s71b_4a # TPP Penelope(neutral, mouth closed) and MC (neutral, mouth closed) exiting through the Dean's office door (POV from Hallway). The Dean in the background, angry, watching them leave.
        with dissolve

        pause 0.75

    # -Regardless of sex or no sex-

    # -Closing the door behind them, MC and Penelope stand in the hallway-

    if "v16_penelope" not in sceneList: # -if no sex in Dean's office

        play sound "sounds/doorclose.mp3"

        scene v16s71a_8 # TPP MC and Penelope(smiling, mouths closed) looking at each other in front of the Dean's office door (Closed).
        with dissolve

        pause 0.75

        scene v16s71b_8a # FPP Penelope(smiling, mouth open) looking at MC
        with dissolve

        pe "Thanks for helping me with Oscar."

        scene v16s71b_8b # FPP Penelope(smiling, mouth closed) looking at MC
        with dissolve

        u "Of course. It was fun spending time with you... and Oscar."

        scene v16s71b_8a
        with dissolve

        pe "Haha, good. Maybe we can do it again sometime."
        
        # -Penelope hugs MC, then they walk separate ways, smiling-
        scene v16s71a_8f # TPP Penelope and MC (smiling, mouths closed) hug
        with dissolve

        pause 0.75

        scene v16s71a_8g # TPP Penelope and MC (smiling, mouths closed) walk away in opposite directions
        with dissolve

        pause 0.75

    else: # -if they had sex in Dean's office

        play sound "sounds/doorclose.mp3"
        
        scene v16s71a_9 # Same as v16s71a_8 but MC and Penlope concerned.
        with dissolve

        pause 0.75

        scene v16s71a_9a # Same as v16s71b_8a but Penelope concerned.
        with dissolve
        
        pe "*Sighs* That was so close!"

        scene v16s71a_9b # Same as v16s71b_8b but Penelope concerned. 
        with dissolve

        u "I know. Imagine if she had walked in on us?"

        scene v16s71a_9a
        with dissolve

        pe "I've really messed up now, though. I completely lost her trust."

        scene v16s71a_9b
        with dissolve

        u "We lost her trust. *Laughs* Maybe she'll give you another chance."

        scene v16s71a_9a
        with dissolve

        pe "I hope so... Now, I need to think of a way to get back on her good side."
        
        pe "Anyways."

        # -Penelope blushes a little-

        scene v16s71a_8c # FPP Penelope(smiling, blushing, mouth open) looking at MC.
        with dissolve

        pe "Thanks for..."

        scene v16s71a_8d # FPP Penelope(smiling, blushing, giggling, slightly shy, mouth open) looking at MC.
        with dissolve

        pe "Well, you know. *Giggles*"

        scene v16s71a_8e # FPP Penelope(smiling, blushing, mouth closed) looking at MC.
        with dissolve

        u "I do know, haha. And thank you too. I had a great morning with you."

        scene v16s71a_8c
        with dissolve

        pe "Hehe, you too, handsome. Hopefully we can do this again soon."

        scene v16s71a_8e
        with dissolve

        u "Preferably without the dean yelling at us afterwards."

        scene v16s71a_8d
        with dissolve

        pe "*Giggles* That would be ideal."

        # -They kiss, then they walk separate ways, smiling-
        scene v16s71a_8h # TPP Penelope and MC kiss (eyes closed)
        with dissolve

        pause 0.75

        scene v16s71a_8g
        with fade
        
        pause 0.75

# -Regardless-

# if still dating Ms. Rose, transition to scene 76
if not v16_ms_rose_breakup:
    jump v16s76

else:
    if v16s27_mc_baby_schedule["thursday"] == BabyDuty.ALONE:
        jump v16s46

    elif v16s27_mc_baby_schedule["thursday"] == BabyDuty.WITH_PARTNER:
        jump v16s47

    elif v16s27_mc_baby_sche["thursday"] == BabyDuty.PARTNER_ALONE:
        jump v16s42


