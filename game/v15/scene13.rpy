# SCENE 13: MC studying
# Locations: MC's Wolves Bedroom, MC's Apes Bedroom
# Characters: MC (Outfit: 5), IMRE (Outfit: 1), GRAYSON (Outfit: 3)
# Time: Afternoon
# Render Count: 12 Unique Renders, 33 Total

init python:
    def v15s13_reply1():
        riley.messenger.newMessage("Good luck! You're gonna need it...")

label v15s13:
    if joinwolves:
        scene v15s13_1 # TPP. MC enters his WOLVES bedroom, carrying a small bag of donuts, He leaves the door half open, slight smile, mouth closed
        with dissolve

        u "(Lauren's party isn't for a while so maybe I should get some studying in... It's not fun, but neither is failing.)"

        scene v15s13_2 # TPP. MC is in his WOLVES bedroom and sits at his WOLVES study desk and opens a book to read, no expression, mouth closed, the bag of doughnuts can be seen on his desk
        with dissolve

        pause 0.75

        scene v15s13_2a # TPP. same as v15s13_2 Mc leans back in his chair, one arm resting on his lap the other holding the book open in front of him
        with dissolve

        pause 0.75
        
        scene v15s13_2b # TPP. same as v15s13_2a drops both arms dangling to his sides still holding the book, mouth slightly open with an annoyed expression, rolling his eyes
        with dissolve

        pause 0.75
        
        scene v15s13_2c # TPP. same as v15s13_2 MC puts down the book, and grabs a donut
        with dissolve

        u "Okay, break time."

        scene v15s13_3 # FPP. MC's WOLVES bedroom door swings open suddenly with Imre standing in the doorway looking at MC with a disgusted expression, hands and palms up raised to chest level, mouth open
        with dissolve

        pause 0.75

        scene v15s13_4 # TPP. Show MC at his WOLVES desk about to eat a donut, with a shocked expression, mouth open, looking at Imre
        with dissolve

        pause 0.75

        scene v15s13_3a # FPP. same as v15s13_3 Imre has put his hands down to his sides
        with dissolve

        imre "Hey, what the hell are you snacking on sugar for? You need to maintain the shape of a fighting machine, bro."

        scene v15s13_3b # FPP. same as v15s13_3a Imre's mouth is closed
        with dissolve

        menu:
            "Agree with Imre":
                $ add_point(KCT.BRO)
                
                u "Yeah, I know... I'll do better next time."

                scene v15s13_3a
                with dissolve

                imre "I just saved you from obesity."

                scene v15s13_3b
                with dissolve

                u "Haha, you did. Thanks."

                scene v15s13_3c # FPP. same as v15s13_3a Imre has a slight smile, happy expression
                with dissolve

                imre "That's what I'm here for, man!"

            "Dismiss Imre":
                $ add_point(KCT.TROUBLEMAKER)
                
                scene v15s13_3b # FPP. same as v15s13_3a Imre's mouth is closed
                #with dissolve

                u "Why are you creeping outside my room, Imre? I'm trying to study here."

                scene v15s13_3c
                with dissolve

                imre "Whatever, man. Just showing that I care! Enjoy your high cholesterol."

                scene v15s13_3b
                with dissolve

                u "I will. *Chuckles*"

        play sound "sounds/vibrate.mp3"
        $ riley.messenger.newMessage("Hey! I'm assuming you'll be at Lauren's Halloween birthday party later?", force_send=True)
        $ riley.messenger.addReply("Yeah, I'll be there!", func=None)
        $ riley.messenger.newMessage("Just FYI, the stores are running low on costumes so if you haven't got one already, hurry up and get one... lol")
        $ riley.messenger.addReply("Shit... I haven't got one yet, haha.", func=None)
        $ riley.messenger.newMessage("Why am I not surprised? :D")
        $ riley.messenger.addReply("I'm on my way out now, wish me luck!", v15s13_reply1)

        scene v15s13_3d # FPP. same as v15s13_3 Imre disappears again, closing the door
        with dissolve

        pause 0.75

        scene v15s13_2d # TPP. same as v15s13_2c MC puts down the donut on his WOLVES desk, pulls out his phone and checks his texts to see a message from Riley, slight smile, mouth closed, looking at his phone
        with dissolve

        pause 0.75
        
        label v15s13_PhoneContinue:
            if riley.messenger.replies:
                play sound "sounds/vibrate.mp3"
                call screen phone
            if riley.messenger.replies:
                u "(I should reply to Riley.)"
                jump v15s13_PhoneContinue
                
        scene v15s13_2e # TPP. same as v15s13_2d MC exits his texts, puts his phone away, and looks down at the donut he put on his WOLVES desk
        with dissolve

        u "(That's enough studying for right now anyway. Time to get Lauren's gift and find a costume!)"

        menu:
            "Eat the donut":
                $ add_point(KCT.TROUBLEMAKER)
                $ grant_achievement("mmmm_donut")
                
                u "(I'll just do an extra gym session this week to even things out.) *Chuckles*"

                scene v15s13_2f # TPP. same as v15s13_2e MC grabs the donut and shoves it in his mouth
                with dissolve

                pause 0.75

            "Don't eat the donut":
                $ add_point(KCT.BRO)
                
                u "(Next time I'll get a healthier snack...)"
            
        scene v15s13_5 # show MC standing up and throwing away the donut bag in his WOLVES room, no expression, mouth closed
        with dissolve

        pause 0.75

        scene v15s13_6 # show MC walking out of his WOLVES bedroom, no expression, mouth closed
        with dissolve

        pause 0.75

        jump v15s17

    else:
        scene v15s13_7 # TPP. MC enters his APES bedroom, carrying a small bag of donuts, He leaves the door half open, slight smile, mouth closed
        with dissolve

        u "(Lauren's party isn't for a while so maybe I should get some studying in... It's not fun, but neither is failing.)"

        scene v15s13_8 # TPP. MC is in his APES bedroom and sits at his APES study desk and opens a book to read, no expression, mouth closed, the bag of doughnuts can be seen on his desk
        with dissolve

        pause 0.75
        
        scene v15s13_8a # TPP. same as v15s13_8 Mc leans back in his chair, one arm resting on his lap the other holding the book open in front of him
        with dissolve

        pause 0.75
        
        scene v15s13_8b # TPP. same as v15s13_8a drops both arms dangling to his sides still holding the book, mouth slightly open with an annoyed expression, rolling his eyes
        with dissolve

        pause 0.75
        
        scene v15s13_8c # TPP. same as v15s13_8 MC puts down the book, and grabs a donut
        with dissolve

        u "Okay, break time."

        scene v15s13_9 # FPP. MC's APES bedroom door swings open suddenly with Grayson standing in the doorway looking at MC with a disgusted expression, hands and palms up raised to chest level, mouth open
        with dissolve

        pause 0.75

        scene v15s13_10 # TPP. Show MC at his APES desk about to eat a donut, with a shocked expression, mouth open, looking at Grayson
        with dissolve

        pause 0.75

        scene v15s13_9a # FPP. same as v15s13_9 Grayson has put his hands down to his sides
        with dissolve

        gr "The fuck?"

        scene v15s13_9b # FPP. same as v15s13_9a Grayson's mouth is closed
        with dissolve

        u "What?"

        scene v15s13_9a
        with dissolve

        gr "If you keep eating like that, you're gonna end up looking like the bubble gum girl from that chocolate factory movie..."

        scene v15s13_9b
        with dissolve

        menu:
            "A blueberry?":
                # $ mc.quirks["pop_culture"] = True # Being re-evaluated
                $ add_point(KCT.BRO)
                
                u "Donuts turn you into blueberries?"

                scene v15s13_9c # FPP. same as v15s13_9a Grayson has a laughing expression, mouth open
                with dissolve

                gr "Nah, dude. They turn you into fat balloons, and I don't wanna be rolling your ass to the gym. *Laughs*"

                scene v15s13_9b
                with dissolve

                u "Haha! Nice one, dude. I actually laughed at that."

                scene v15s13_9c
                with dissolve

                gr "Ha, fuck you."

            "Chocolate factory movie?":
                # $ mc.quirks["boomer"] = True # Being re-evaluated
                $ add_point(KCT.TROUBLEMAKER)
                
                scene v15s13_9b
                #with dissolve

                u "Chocolate factory movie? Are you feeling okay? *Chuckles*"

                scene v15s13_9a
                with dissolve

                gr "Yeah you prick, I feel great. Not my fault you're a boomer."

                scene v15s13_9b
                with dissolve

                u "Ha, whatever you say man."

        scene v15s13_9a
        with dissolve

        gr "Regardless, that's not the diet of a fight champion. Do better."

        scene v15s13_9b
        with dissolve

        menu:
            "I will":
                $ add_point(KCT.BRO)
                
                u "I know, I will. This is only my first just so you know."

                scene v15s13_9c
                with dissolve

                gr "Well, keep it that way. Unless you want frat boy to turn into fat boy, haha!"

                scene v15s13_9b
                with dissolve

                u "Haha, wow... You're on fire today with these jokes, huh?"

                scene v15s13_9d # FPP. same as v15s13_9a Grayson has an angry expression
                with dissolve

                gr "Whatever, I didn't come here to amuse you."

                scene v15s13_9b
                with dissolve

                u "Alright, okay. No donuts."

                scene v15s13_9d
                with dissolve

                gr "Good."

                scene v15s13_9e # FPP. same as v15s13_9d Grayson turns his back to MC and starts to walk out
                with dissolve

                pause 0.75

            "You don't eat donuts?":
                $ add_point(KCT.TROUBLEMAKER)
                
                u "Are you serious right now? You're telling me that you never have donuts, or cake, or cola?"

                scene v15s13_9d
                with dissolve

                gr "You think I got to be the fight king by eating that shit? *Scoffs*"

                scene v15s13_9b
                with dissolve

                u "I know for a fact that you eat this shit, Grayson. Get off my back, it's a donut."

                scene v15s13_9a
                with dissolve

                gr "Suit yourself, fat boy."

                scene v15s13_9e
                with dissolve

                u "(Such a dick.)"

        play sound "sounds/vibrate.mp3"
        $ riley.messenger.newMessage("Hey! I'm assuming you'll be at Lauren's Halloween birthday party later?", force_send=True)
        $ riley.messenger.addReply("Yeah, I'll be there!", func=None)
        $ riley.messenger.newMessage("Just FYI, the stores are running low on costumes so if you haven't got one already, hurry up and get one... lol")
        $ riley.messenger.addReply("Shit... I haven't got one yet, haha.", func=None)
        $ riley.messenger.newMessage("Why am I not surprised? :D")
        $ riley.messenger.addReply("I'm on my way out now, wish me luck!", v15s13_reply1)

        scene v15s13_9f # FPP. same as v15s13_9 Grayson disappears again, closing the door
        with dissolve

        pause 0.75

        scene v15s13_8d # TPP. same as v15s13_8c MC puts down the donut on his APES desk, pulls out his phone and checks his texts to see a message from Riley, slight smile, mouth closed, looking at his phone
        with dissolve

        pause 0.75

        label v15s13_PhoneContinue2:
            if riley.messenger.replies:
                play sound "sounds/vibrate.mp3"
                call screen phone
            if riley.messenger.replies:
                u "(I should reply to Riley.)"
                jump v15s13_PhoneContinue2

        scene v15s13_8e # TPP. same as v15s13_8d MC exits his texts, puts his phone away, and looks down at the donut he put on his APES desk
        with dissolve

        u "(That's enough studying for right now anyway. Time to get Lauren's gift and find a costume!)"

        menu:
            "Eat the donut":
                $ add_point(KCT.TROUBLEMAKER)
                
                $ grant_achievement("mmmm_donut")
                u "(I'll just do an extra gym session this week to even things out.) *Chuckles*"

                scene v15s13_8f # TPP. same as v15s13_8e MC grabs the donut and shoves it in his mouth
                with dissolve

                pause 0.75

            "Don't eat the donut":
                $ add_point(KCT.BRO)
                
                u "(Next time I'll get a healthier snack...)"
            
        scene v15s13_11 # show MC standing up and throwing away the donut bag in his APES room, no expression, mouth closed
        with dissolve

        pause 0.75

        scene v15s13_12 # show MC walking out of his APES bedroom, no expression, mouth closed
        with dissolve

        pause 0.75
        jump v15s17