# SCENE 48: Baby Night with Chloe
# Locations: Chicks house
# Characters: CHLOE (Outfit: 3), MC (Outfit: 9), WOMAN ON TV SHOW (Outfit: x), MAN ON TV SHOW (Outfit: x), [BABY_NAME] (Outfit: x)
# Time: Wednesday night


label v16s48: # 48) Baby night: Chloe & MC
    scene v16s48_1 # TPP Show MC following Chloe into the living room of the Chicks house, the baby is visible face down at the far side of couch
    with dissolve

    cl "There it is."

    scene v16s48_2 # FPP MC's view of the baby doll on the couch
    with dissolve

    u "(Poor [v16_baby_name]... Is this child neglect?) *Laughs*"

    scene v16s48_3 # FPP Show Chloe (annoyed expression, mouth open) looking at MC
    with dissolve

    cl "I guess we'll just watch TV and wait for the hell to begin?"

    scene v16s48_3a # FPP Same angle as 3, Chloe (annoyed expression, mouth closed) looking at MC
    with fade

    u "*Chuckles* Sounds like a plan."

    # -Fade to MC sat next to Chloe on the couch. The baby is still lying face down, next to Chloe. They are watching TV (or laptop that's on the coffee table, whichever works best)-
    
    scene v16s48_4 # TPP MC and Chloe sitting on the couch watching TV (not visible, but lighting them with a blue light). Baby is still face down, next to Chloe, ignored.
    with dissolve

    wtv "Listen, Corey... just because you're a robot, it doesn't mean I can't love you."

    mtv "Wait, how did you know? What I truly am?"

    scene v16s48_5 # TPP Close on Chloe watching TV from the TV POV (light from the TV slighly shines on her face).
    with dissolve

    wtv "I've always known the truth about you."

    scene v16s48_5a # TPP Close on MC watching TV from the TV POV (light from the TV slighly shines on his face).
    with dissolve

    mtv "But... How?"

    scene v16s48_5
    with dissolve

    wtv "...Because Corey, I created you."

    # TODO: *Dramatic music*
    play sound "sounds/horrorsound.mp3" # DON'T KNOW IF THIS IS THE BEST SOUND, OR IF A NEW ONE IS BEING CREATED.

    play sound "sounds/babycry.mp3"

    scene v16s48_2
    with dissolve

    baby "*Crying*"

    scene v16s48_6 # FPP View of Chloe (angry expression, mouth open) next to MC on the couch, looking at the baby doll
    with dissolve

    cl "Fucking great! Just when it's getting good, the thing starts crying. *Scoffs*"

    scene v16s48_6a # FPP Same angle as 6, Chloe (angry expression, mouth closed) next to MC on the couch, looking at the baby doll
    with dissolve

    u "It's fine, probably just needs feeding. Where are the keys?"

    play sound "sounds/babycry.mp3"

    scene v16s48_2
    with dissolve

    baby "*Crying*"

    scene v16s48_6b # FPP Same angle as 6, Chloe (annoyed, mouth open) next to MC, handing him the baby and looking back at the TV
    with dissolve

    cl "I don't know. Somewhere around here."

    scene v16s48_6c # FPP Same angle as 6, Chloe (neutral expression, mouth closed) next to MC. He is taking the doll from her, she is looking at the TV
    with dissolve

    u "Are you serious?"

    scene v16s48_6d # FPP Same angle as 6, Chloe (neutral expression, mouth open) next to MC. She is watching the TV
    with dissolve

    cl "Yes, they're somewhere! I'm watching this, though. You find them."

    play sound "sounds/babycry.mp3"

    scene v16s48_7 # FPP MC, sitting on the couch, holding the baby doll out in front of him
    with dissolve

    baby "*Crying*"

    scene v16s48_8 # TPP MC stands up and looks around, holding the doll. He is looking at the keys next to Chloe, where to doll had been. Chloe is watching the TV
    with dissolve

    u "(Wow... Having this baby has made Chloe reach a whole new level of not giving a fuck.)"

    scene v16s48_9 # FPP MC reaching across Chloe to grab the keys on the couch next to her, Chloe (mouth closed) shifting to look around MC's arm at the TV
    with dissolve

    u "Okay, um... which one's for feeding?"

    scene v16s48_10 # FPP Show MC holding the doll and the keys in front of him
    with dissolve

    play sound "sounds/babycry.mp3"

    baby "*Crying*"

    u "Chloe? Do you remember?"

    scene v16s48_9a # FPP Same angle as 9. Chloe (neutral, mouth open) watching the TV intently
    with dissolve

    cl "Who cares, [name]? Just try them all! And quickly, please."

    # -If MC chooses an incorrect key, the choice menu appears again for another attempt-
    $ v16_wrong_key = True 
    while v16_wrong_key:
        menu:
            "Blue":
                $ v16_wrong_key = False
                play sound "sounds/babycoo.mp3"

                scene v16s48_11 # FPP Show close up of MC using the blue key on the baby
                with dissolve

                baby "*Soft coos*"

                scene v16s48_12 # TPP MC holding the baby up in front of him with one hand raised in victory
                with dissolve

                u "Yes! That was it."

            "Green":
                play sound "sounds/babyscream.mp3"
                
                scene v16s48_11a # FPP Same angle as 11, close up of MC using the green key on the baby
                with dissolve

                baby "*Screaming cries*"

                scene v16s48_13 # FPP MC looking at the 3 keys
                with dissolve

                u "(No, not green. What about...)"

            "Orange":
                play sound "sounds/babycry.mp3"

                scene v16s48_11b # FPP Same angle as 11, close up of MC using the orange key on the baby
                with dissolve

                baby "*Cries*"

                scene v16s48_13
                with dissolve

                u "(Orange isn't working...)"

    scene v16s48_14 # TPP MC flopped on the couch, still holding the baby, Chloe (slight smile, mouth open) looking at the TV
    with dissolve

    cl "Finally! I didn't think it was going to stop, ha."

    scene v16s48_7
    with dissolve

    u "Yeah... *Sighs*"

    scene v16s48_14a # TPP Same angle as 14. Chloe (sleepy expression, mouth closed) sinking in to the couch, as if falling asleep. MC (mouth closed) still holding the baby
    with fade

    pause 0.75

    scene v16s48_14b # TPP Same angle as 14. Chloe (eyes closed, mouth closed) has her head on MC's shoulder. MC has his eyes closed, and the baby has fallen out of his arms
    with fade

    pause 0.75

    play sound "sounds/babycry.mp3"

    scene v16s48_15 # FPP Baby next to MC where it has fallen
    with dissolve

    baby "*Crying*"

    scene v16s48_14c # TPP Same angle as 14. Chloe (eyes still closed, mouth open) lifting her head from MC's shoulder. MC has eyes wide, startled
    with dissolve

    cl "Oh, for fuck's sake!"

    scene v16s48_15
    with dissolve

    u "*Groans*"

    cl "Make it shut up!"

    play sound "sounds/babycry.mp3"

    baby "*Crying*"

    scene v16s48_16 # FPP MC looking at Chloe (sleepy expression, mouth closed)
    with dissolve

    u "I was having such a nice dream, too... *Groans*"

    scene v16s48_16a # FPP Same angle as 16. Chloe (sleepy, mouth open) looking at MC
    with dissolve

    cl "[name], please?"

    scene v16s48_15
    with dissolve

    cl "Get it to stop!"

    menu:
        "Care for baby":
            
            play sound "sounds/babycry.mp3"

            u "I'm guessing it needs the burping key now?"

            baby "*Crying*"

            scene v16s48_16b # FPP Same angle as 16. Chloe (mouth open) covering her eyes with her hand in exhaustion
            with dissolve

            cl "Maybe you should take it home, you seem like you've got this under control."

            scene v16s48_16a
            with dissolve

            cl "I can get some sleep then."

            scene v16s48_16
            with dissolve

            u "Haha, no way. This is what the project is about. We've got to share the burden."

            play sound "sounds/babycry.mp3"

            scene v16s48_15
            with dissolve

            baby "*Cries*"

            u "[v16_baby_name] just needs to burp and then we can get back to sleep."

            scene v16s48_16a
            with dissolve

            cl "*Scoffs* Calling it [v16_baby_name]. It's a piece of plastic, [name]!"

            scene v16s48_16
            with dissolve

            u "Hey, now. That's no way to talk about your child. *Chuckles*"

            scene v16s48_16b
            with dissolve

            cl "*Groans*"

            scene v16s48_10
            with dissolve
            u "Now, let's see..."
            
            # -If MC chooses an incorrect key, the choice menu appears again for another attempt-
            $ v16_wrong_key = True

            while v16s48_wrong_key:
                menu:
                    "Blue":
                        play sound "sounds/babycry.mp3"

                        scene v16s48_11
                        with dissolve

                        baby "*Crying*"

                        scene v16s48_13
                        with dissolve

                        u "(Nope. I've fucked up.)"

                    "Green":
                        $ v16_wrong_key = False
                        play sound "sounds/babycoo.mp3"

                        scene v16s48_11a
                        with dissolve

                        u "Yes! There we go."

                        scene v16s48_17 # TPP MC (slight smile, mouth open) standing with baby on his shoulder like he's burping it. Chloe (annoyed, mouth closed) has her head back, exhausted
                        with dissolve

                        u "All burped up."

                    "Orange":
                        play sound "sounds/babycry.mp3"
                        
                        scene v16s48_11b
                        with dissolve

                        baby "*Crying*"

                        scene v16s48_13
                        with dissolve

                        u "(Nope! I think that one's for a diaper change...)"

            scene v16s48_17a # TPP Same angle as 17. Chloe (annoyed expression, mouth open) looking at MC (slight smile, mouth closed) and the baby
            with dissolve

            cl "*Sighs* Good. I can hear my own thoughts now."

            scene v16s48_18 # FPP MC looking down at Chloe (annoyed, mouth closed). She is sitting far back on the couch in exhaustion
            with dissolve

            u "You're so harsh. The poor thing can't help it."

            scene v16s48_18a # FPP Same angle as 18. Chloe (annoyed, mouth open) looking up at MC
            with dissolve

            cl "*Scoffs* You're ridiculous."

            scene v16s48_17b # TPP Same angle as 17. Chloe has streched out to take up most the couch, leaving a small gap, eyes closed. MC (mouth closed) is holding the baby and looking down at her
            with dissolve

            u "(Yeah, I'm totally a single dad here.)"

            scene v16s48_19 # TPP MC sits down in the small gap left by Chloe on the couch, holding the baby
            with dissolve

            pause 0.75

            ### ERROR: [End of Checkpoint 1.1. Continue to Checkpoint 2]        
        "Complain about baby":
            $ add_point(KCT.TROUBLEMAKER)

            u "I am so fucking done with this doll!"

            scene v16s48_16b
            with dissolve

            cl "Honestly, see if you can rip out its battery."

            scene v16s48_16
            with dissolve

            u "*Sighs* We'd fail the assignment."

            play sound "sounds/babycry.mp3"

            scene v16s48_15
            with dissolve

            baby "*Crying*"

            scene v16s48_16a
            with dissolve

            cl "It probably needs to burp considering it ate earlier before you came."

            scene v16s48_16
            with dissolve

            u "Okay, do you know what key that is?"

            scene v16s48_16b
            with dissolve

            cl "No, and I don't care.  Just hurry up and make it stop."

            scene v16s48_10
            with dissolve

            u "Right, then..."

            $ v16_wrong_key = True

            # -If MC chooses an incorrect key, the choice menu appears again for another attempt-
            while v16_wrong_key:
                menu:
                    "Blue":
                        play sound "sounds/babycry.mp3"

                        scene v16s48_11a
                        with dissolve

                        baby "*Crying*"

                        scene v16s48_13
                        with dissolve

                        u "(Nope, nope, nope!)"

                    "Green":
                        $ v16_wrong_key = False

                        play sound "sounds/babycoo.mp3"

                        scene v16s48_11a
                        with dissolve

                        u "There, [v16_baby_name]. You've burped. Now leave us in peace!"

                    "Orange":
                        play sound "sounds/babycry.mp3"

                        scene v16s48_11b
                        with dissolve

                        baby "*Crying*"

                        scene v16s48_13
                        with dissolve

                        u "(Still crying...)"

            scene v16s48_14d # TPP Same angle as 14. Chloe (tired expression, mouth closed) looking at MC (annoyed, mouth open) who is on the couch, the baby carelessly tossed to the end
            with dissolve

            u "I don't think we're cut out for parenthood."

            scene v16s48_16a
            with dissolve

            cl "What are they even trying to teach us with this? That raising a child is practically hell?"

            scene v16s48_16
            with dissolve

            u "Ha, I know. It seems like they're trying to scare us into never having kids."

            scene v16s48_16a
            with dissolve

            cl "Well, they have me convinced."

            scene v16s48_16
            with dissolve

            u "*Scoffs* Really? A plastic baby doll has ruined the idea of becoming a parent?"

            scene v16s48_16b
            with dissolve

            cl "That crying is just.... So. Annoying."

            scene v16s48_16
            with dissolve

            u "Well, yeah."

            scene v16s48_16a
            with dissolve

            cl "Like, It's still ringing in my head."

            if chloe.relationship == Relationship.GIRLFRIEND: # -if ChloeGF
                scene v16s48_16c # FPP Same angle as 16. Chloe (eyebrow raised, mouth open) looking at MC
                with dissolve

                cl "Help me take my mind off it?"

                scene v16s48_16d # FPP Same angle as 16. Chloe (naughty smile, eyebrow raised, mouth closed) looking at MC
                with dissolve

                u "Hmm, I can always try..."

                scene v16s48_20 # TPP MC and Chloe start making out on the couch
                with dissolve

                pause 0.75
                
                scene v16s48_20a # TPP Same angle as 20. MC and Chloe stop kissing and look at the baby, anticipating it crying
                with dissolve

                pause 0.75

            # -Regardless of ChloeGF-
            play sound "sounds/babycry.mp3"

            scene v16s48_21 # FPP View of baby where MC tossed it when he sat down
            with dissolve

            baby "*Crying*"

            scene v16s48_20b # TPP Same angle as 20. MC looks annoyed, Chloe (annoyed, mouth open) is reaching across MC to grab the baby doll
            with dissolve

            cl "Oh, my fucking-"

            scene v16s48_21a # FPP Same angle as 21. Chloe's hand is grabbing the baby doll roughly (maybe by the leg or something, depending on its position)
            with dissolve

            baby "*Crying*"

            scene v16s48_22 # TPP Chloe(annoyed, mouth open) holding the doll and walking away from the couch toward the sliding glass door, MC looks wide-eyed and confused
            with dissolve

            cl "No. Nope. I'm done! We. Are. Done."

            scene v16s48_23 # TPP Show Chloe (neutral expression, mouth open) casually tossing the baby doll out the open sliding glass door. 
            with dissolve

            cl "There! Problem solved. Ha!"

            menu:
                "Freak out":
                    scene v16s48_24 # FPP MC's view from behind Chloe as she closes the sliding glass door
                    with dissolve

                    u "Chloe! Have you lost your mind?!"

                    scene v16s48_24a # FPP Same angle as 24, Chloe (slight smile, mouth closed) has now turned to look at MC
                    with dissolve

                    u "You just defenestrated our baby!"

                    scene v16s48_24b # FPP Same angle as 24, Chloe (slight smile, mouth open) facing MC
                    with dissolve

                    cl "I don't know what that word means, [name], but-"

                    scene v16s48_24a
                    with dissolve

                    u "It means you threw it out the fucking window!"

                    scene v16s48_24b
                    with dissolve

                    cl "Yes, and?"

                    scene v16s48_24c # FPP Same angle as 24, Chloe (slight smile, mouth open) hooking her thumb back to point toward the sliding glass door
                    with dissolve

                    cl "You can go fetch it if you want, but do not bring that thing back here."

                    scene v16s48_24a
                    with dissolve

                    u "Chloe. You're serious?"

                    scene v16s48_24b
                    with dissolve

                    cl "Dead serious. I'm going back to sleep. Goodnight!"

                    scene v16s48_25 # TPP Chloe (slight smile, mouth closed) laying on the couch, eyes closed
                    with dissolve

                    pause 0.75

                    scene v16s48_26 # FPP MC looking down at Chloe. She looks like she's already asleep
                    with dissolve

                    u "*Sighs* (I can't believe she just did that)"

                    scene v16s48_27 # TPP MC (tired, mouth closed) yawning and stretching, closing his eyes
                    with dissolve

                    u "(I'm sure it can wait 'til morning... We've probably already failed.)"

                "Laugh":
                    $ add_point(KCT.TROUBLEMAKER)

                    scene v16s48_24
                    with dissolve

                    u "*Laughs* Wow! Worst mom of the year award goes to..."

                    scene v16s48_24b
                    with dissolve

                    cl "Don't act like you're not relieved."

                    scene v16s48_24a
                    with dissolve

                    u "Oh, I'm extremely relieved. I just didn't realize you were a psychopath, haha."

                    scene v16s48_28 # TPP Show Chloe (slight smile, mouth closed) walking up to MC (slight smile, mouth closed)
                    with dissolve

                    pause 0.75

                    if chloe.relationship == Relationship.FRIEND: # -if ChloeFriend
                        scene v16s48_28a # TPP Same angle as 28. Chloe (slight smile, mouth open) pointing her finger into MC's chest
                        with dissolve

                        cl "It pushed me too far!"

                        scene v16s48_29 # FPP View of Chloe (slight smile, mouth closed) looking up at MC
                        with dissolve

                        u "I can tell."

                        scene v16s48_29a # FPP Same angle as 29. Chloe (slight smile, mouth open) looking up at MC
                        with dissolve

                        cl "Let's get back to sleep. Now."

                        scene v16s48_25
                        with dissolve

                        pause 0.75

                    elif chloe.relationship == Relationship.GIRLFRIEND: # -if ChloeGF
                        scene v16s48_29b # FPP Same angle as 29. Chloe (flirty smile, eyebrow raised, mouth open) looking up at MC
                        with dissolve

                        cl "You wanna see how bad I can be?"

                        menu:
                            "Hell yes":
                                $ add_point(KCT.BOYFRIEND)

                                scene v16s48_29c # FPP Same angle as 29, Chloe (flirty smile, eyebrow raised, mouth closed) looking up at MC
                                with dissolve

                                u "Hell yeah, I do."

                                scene v16s48_29b
                                with dissolve

                                cl "Hehe... Good, because I've got a lot of anger to work off."

                                jump v16s48a # -Transition to Scene 48a-
                            
                            "I'm too tired":
                                scene v16s48_29c
                                with dissolve

                                u "I don't know, Chloe. I can barely keep my eyes open right now, ha."

                                scene v16s48_29d # FPP Same angle as 29. Chloe (faking being angry, slight smile, mouth open) looking up at MC and putting her hand on his chest
                                with dissolve

                                cl "You see?! This baby bullshit ruins everything."

                                scene v16s48_29
                                with dissolve

                                u "I'm sorry, Chloe."

                                scene v16s48_29a
                                with dissolve

                                cl "*Sighs* It's fine, I get it. Let's just get some sleep."

                                scene v16s48_25
                                with dissolve

                                pause 0.75

    scene v16s48_30 # TPP MC sits in the small gap Chloe left at the end of the couch, looking sleepy
    with dissolve

    pause 0.75

    scene v16s48_30a # TPP Same angle as 30. MC and Chloe has slightly shifted positions, both have their eyes closed
    with fade

    pause 0.75

    scene v16s48_30b # TPP Same angle as 30. MC's eyes open, he's reaching around to rub his lower back
    with dissolve

    u "(This couch is so uncomfortable... Might just be the worst sleep I've ever had in my life.)"

    scene v16s48_31 # FPP MC looks at Chloe, who is fast asleep on the couch
    with dissolve

    u "(She's still fast asleep. Probably a good time for me to sneak off and go home.)"

    jump v16s49a # -Transition to Scene 49a-