# SCENE 46: Finding Nora, Solving the case
# Locations: Room 103 where the pinboard is.
# Characters: AMBER (Outfit: Detective), MC (Outfit: 1)
# Time: Morning

label v15s46:
    play sound "sounds/dooropen.mp3"

    scene v15s46_1 # TPP. Amber and MC entering the detective pinboard room, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    play sound "sounds/doorclose.mp3"

    scene v15s46_2 # TPP. Amber and MC inside the room, Amber turned around to face MC, MC looking at Amber, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s46_3 # FPP. MC looking at Amber, Amber looking at MC, Amber slight smile, mouth open.
    with dissolve

    am "I really hope we have enough clues to solve this now."

    am "We need to choose a location, detective. Remember, a young woman's life is at stake, so we can't take too long."

    scene v15s46_3a # FPP. MC looking at Amber, Amber looking at MC, Amber slight smile, mouth closed.
    with dissolve

    u "No pressure then!"

    u "Let's see if I can work my magic."

    scene v15s46_4 # TPP. Show MC walking up to the pinboard, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v15s46_5 # FPP. Looking at the pinboard.
    with dissolve

    pause 0.75

    # -The UI pops up to show all the clues achieved and any new ones from the Chloe interrogation (CHLOE CLUES UNLOCKED: Nora always runs to her Dad for materialistic help. Nora & Ms. rose are really close. Nora still likes her ex-boyfriend from before Chris. Nora hates camping. CHLOE LOCATIONS UNLOCKED: Ex-boyfriend's house.)-

    # -MC can study all the clues and locations, all of which have comments from Amber to help them (SEE MIRO). MC can choose one of the locations. Once MC has chosen the location they want to go with, they can exit the UI whenever. The correct location is Nora's Dad's cabin-

    if not nora_cabin: # Placeholder.
        scene v15s46_3b # FPP. MC looking at Amber, Amber looking at MC, Amber confused, mouth open.
        with dissolve

        am "Really?"

        scene v15s46_3c # FPP. MC looking at Amber, Amber looking at MC, Amber confused, mouth closed.
        with dissolve

        u "What?"

        scene v15s46_3b
        with dissolve

        am "You're happy with that choice?"

        scene v15s46_3c
        with dissolve

        u "Yeah, sure. Why not?"

        scene v15s46_3
        with dissolve

        am "You need to go back to detective school, [name]."

        scene v15s46_3a
        with dissolve

        u "I've had thirty years in this job! I know what I'm doing."

        scene v15s46_3
        with dissolve

        am "Haha, thirty years."

        am "Do you want me to spell it out for you?"

        scene v15s46_3a
        with dissolve

        u "..."

        u "Yes, please."

        scene v15s46_3
        with dissolve

        am "We know that Nora loves nature... Chris told us that Nora's aunt borrowed Mr. Rose's cabin... Nora went to see her aunt only briefly."

        am "Understand?"

        scene v15s46_3a
        with dissolve

        menu:
            "Nope, no idea":
                $ add_point(KCT.BRO)
                
                u "Nope. It's like you're talking in random words."

                scene v15s46_3
                with dissolve

                am "Oh, wow. You can't piece anything together?"

                scene v15s46_3a
                with dissolve

                u "Nope."

                scene v15s46_3
                with dissolve

                am "Nora's at her dad's cabin!"

                scene v15s46_3a
                with dissolve

                u "Is she? So why did she go to her aunt's at all?"

                scene v15s46_3
                with dissolve

                am "To pick up the key!"

                scene v15s46_3a
                with dissolve

                u "Oh, shit! That makes sense!"

                scene v15s46_3
                with dissolve

                am "Yeah! It makes sense because that's the answer, haha!"

            "Yeah, of course":
                scene v15s46_3a
                #with dissolve

                u "Yeah, of course!"

                scene v15s46_3
                with dissolve

                am "So, where is she?!"

                scene v15s46_3a
                with dissolve

                u "She's..."

                u "..."

                scene v15s46_3
                with dissolve

                am "At her dad's cabin?"

                scene v15s46_3a
                with dissolve

                u "You didn't let me finish!"

                scene v15s46_3
                with dissolve

                am "Oh, suuure! So, tell me, why did she go to her aunt's only briefly?"

                scene v15s46_3a
                with dissolve

                menu:
                    "To ask for her advice":
                        $ add_point(KCT.BRO)
                        
                        u "To ask her for advice, obviously."

                        scene v15s46_3
                        with dissolve

                        am "No!"

                        am "To pick up the key!"

                        scene v15s46_3a
                        with dissolve

                        u "Oh. Oh, yeah!"

                        u "I would've worked it out eventually."

                        scene v15s46_3
                        with dissolve

                        am "Haha, okay, Sherlock."

                    "To pick up something":
                        $ add_point(KCT.TROUBLEMAKER)
                        
                        scene v15s46_3a
                        #with dissolve

                        u "Because she needed to pick up something?"

                        scene v15s46_3
                        with dissolve

                        am "Exactly."

                        am "Which was?"

                        scene v15s46_3a
                        with dissolve

                        menu:
                            "Food supplies":
                                $ add_point(KCT.BRO)
                                
                                u "Well, to pick up some food for the cabin."

                                scene v15s46_3
                                with dissolve

                                am "Sure, she probably borrowed a twinkie or two, haha. But her aunt had something more important."

                                scene v15s46_3a
                                with dissolve

                                u "..."

                                scene v15s46_3
                                with dissolve

                                am "The key!"

                                scene v15s46_3a
                                with dissolve

                                u "Oh- Yeah, of course. Haha."

                            "The key":
                                $ add_point(KCT.BOYFRIEND)
                                
                                u "The key for the cabin."

                                scene v15s46_3
                                with dissolve

                                am "Is that your final answer?"

                                scene v15s46_3a
                                with dissolve

                                u "..."

                                u "Yes."

                                scene v15s46_3
                                with dissolve

                                am "Ding, ding, ding! We have a winner. *Chuckles*"

    else:
        if len(v15_nora_clues) == 9 and len(v15_nora_locations) == 6:
            $ grant_achievement("just_one_more_thing")

        scene v15s46_3a
        with dissolve

        u "She's at her dad's cabin, then."

        scene v15s46_3
        with dissolve

        am "Yeah, it has to be the place!"

        am "The other clues helped, but basically..."

        am "We know Nora loves nature..."

        am "Chris told us that Nora's aunt borrowed Mr. Rose's cabin, and..."

        am "Nora went to see her aunt only briefly."

        scene v15s46_3a
        with dissolve

        u "Right... That's all correct."

        scene v15s46_3
        with dissolve

        am "Which means..."

        scene v15s46_3a
        with dissolve

        u "She went to her aunt's to get the key."

        scene v15s46_3
        with dissolve

        am "Exactly!"

        am "We're the best detective duo ever. *Giggles*"

    scene v15s46_3
    with dissolve

    am "I'll send a message to Techie. She can find Mr. Rose's property records and find us an address."

    scene v15s46_3d # FPP. Amber taking out her phone, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s46_3e # FPP. Amber looking at her phone, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s46_3f # FPP. Amber pressing a button on her phone, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s46_3g # FPP. Amber putting her phone away, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s46_3a
    with dissolve

    u "We couldn't have solved this case without Penelope."

    scene v15s46_3
    with dissolve

    am "Yeah, I know. She's amazing at what she does, and she's the best."

    if penelope.relationship.value >= Relationship.LOYAL.value:
        scene v15s46_3a
        with dissolve

        u "Yeah, she really is the best. *Laughs* Not a lot of people realize it though."

        scene v15s46_3h # FPP. Amber looking at MC, MC looking at Amber, winking, slight smile, mouth open.
        with dissolve

        am "Good! More for us. Hehe..."

    else:
        scene v15s46_3a
        with dissolve

        u "Haha, true."

    scene v15s46_6 # TPP. Amber pouring a cup of coffe, slight smile, mouth open.
    with dissolve

    am "Time for one more..."

    play sound "sounds/vibrate.mp3"

    scene v15s46_3i # FPP. Amber chugging her coffee
    with dissolve

    pause 0.75

    scene v15s46_3
    with dissolve

    am "Wow, she's fast!"

    scene v15s46_3d
    with dissolve

    pause 0.75

    scene v15s46_3e
    with dissolve

    pause 0.75

    scene v15s46_3f
    with dissolve

    pause 0.75

    scene v15s46_3g
    with dissolve

    pause 0.75

    scene v15s46_3a
    with dissolve

    u "She already found the address?"

    scene v15s46_3
    with dissolve

    am "Yeah, isn't that insane?"

    scene v15s46_3a
    with dissolve

    u "Yeah, kinda scary, but... *Laughs*"

    scene v15s46_3
    with dissolve

    am "A scary victory!"

    scene v15s46_6
    with dissolve

    pause 0.75

    scene v15s46_3i
    with dissolve

    pause 0.75

    scene v15s46_3j # FPP. MC looking at Amber, Amber looking at MC, Amber frown, looks sick, mouth open.
    with dissolve

    am "*Stomach gurgles* Uh, oh."

    scene v15s46_3k # FPP. MC looking at Amber, Amber looking at MC, Amber frown, looks sick, mouth closed.
    with dissolve

    u "You don't look so good."

    scene v15s46_3j
    with dissolve

    am "I don't feel it, either."

    am "..."

    am "I think I need to go home."

    scene v15s46_3k
    with dissolve

    u "You should probably get some sleep, yeah? Haha."

    scene v15s46_3j
    with dissolve

    am "I'm probably close to like... forty-eight hours now without sleep, ha."

    am "I think I've hit a wall all of a sudden."

    scene v15s46_3k
    with dissolve

    u "Get yourself home before you pass out."

    scene v15s46_3j
    with dissolve

    am "Okay, good idea."

    am "I'll trust you to finish this mission on your own, detective."

    scene v15s46_3k
    with dissolve

    u "I've been trained by the best. I'm sure I can handle it from here."

    scene v15s46_3
    with dissolve

    am "Yeah, you got this. I'll text you the address. *Fake crying*"

    scene v15s46_3l # FPP. MC looking at Amber, Amber looking at MC, Amber frown, fake crying, mouth open.
    with dissolve

    pause 0.75

    scene v15s46_3a
    with dissolve

    u "Haha, stop it! I'll see you on the next case."

    scene v15s46_3
    with dissolve

    am "Make your partner proud!"

    play sound "sounds/dooropen.mp3"

    scene v15s46_7 # TPP. Show Amber leaving the room holding her stomach, amber frown, mouth closed.
    with dissolve

    pause 0.75

    jump v15s47