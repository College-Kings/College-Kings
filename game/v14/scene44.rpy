# SCENE 44: On your way out you walk past Elijah
# Locations: Campus Sidewalk, Parking lot.
# Characters: MC (Outfit: 1), ELIJAH (Outfit: 1), IMRE (Outfit: 2), Elijah's Mom (Outfit: 1)
# Time: Morning

label v14s44:
    scene v14s44_1 # TPP. Show MC walking down the sidewalk of campus near the parking lot, slight smile, mouth closed.
    with dissolve

    pause 0.75

    play music "music/v13/Track Scene 57.mp3" fadein 2

    scene v14s44_1a # TPP. Same as v14s44_1, Show MC squinting looking off at the distance, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v14s44_2 # TPP. Close up of just Elijah in the parking lot wearing a Team Chloe shirt, Elijah slight smile, mouth closed.
    with dissolve
    
    pause 0.75

    scene v14s44_3 # TPP. Close up of just the shirt Elijah is wearing. Focus in on Chloe's boobs.
    with dissolve
    
    pause 0.75

    scene v14s44_2
    with dissolve

    u "So you're supporting Chloe???"

    scene v14s44_2a # TPP. Same as v14s44_2, Elijah now looking at MC, Elijah neutral face, mouth closed.
    with dissolve

    pause 0.75

    scene v14s44_2b # TPP. Same as v14s44_2a, Show Elijah walking towards MC, Elijah, neutral face, mouth closed.
    with dissolve

    pause 0.75

    scene v14s44_4 # FPP. Elijah now standing infront of MC, Elijah looking at MC, MC looking at Elijah, Neutral face, mouth open.
    with dissolve

    el "Yes. She's the logical choice."

    scene v14s44_4a # FPP. Same as v14s44_4, Elijah neutral face, mouth closed.
    with dissolve

    u "What makes you say that?"

    scene v14s44_4
    with dissolve

    el "She's already President, so she's experienced. Again, logical choice."

    scene v14s44_4a
    with dissolve

    u "Is logic the only reason why you vote for things? *Chuckles*"

    scene v14s44_4
    with dissolve

    el "Why should we vote any differently? If the choice doesn't make logical sense, then why would I choose it?"

    scene v14s44_4a
    with dissolve

    u "New opportunities... Personal feelings... Etc?"

    scene v14s44_4
    with dissolve

    el "Nah, I'm sticking with Chloe. I trust tested waters over new boots."

    scene v14s44_4a
    with dissolve

    u "*Laughs*"

    scene v14s44_4
    with dissolve

    el "What?"

    scene v14s44_4a
    with dissolve

    u "Just the way you said that, it was funny."

    scene v14s44_4b # FPP. Same as v14s44_4a, Elijah unamused expression, mouth open.
    with dissolve

    el "*Scoffs* Anyway... Who are you supporting?"

    menu:
        "Chloe":
            if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                $ add_point(KCT.BOYFRIEND)
            elif lindsey.relationship.value >= Relationship.FWB.value:
                $ add_point(KCT.TROUBLEMAKER)
            
            scene v14s44_4
            with dissolve

            u "I'm also supporting Chloe."

            scene v14s44_4a
            with dissolve

            $ set_presidency_percent(v14_lindsey_popularity - 2) #tick
            el "See? Good, logical choice."

            scene v14s44_4
            with dissolve

            u "Ha. Yeah."

        "Lindsey":
            if lindsey.relationship.value >= Relationship.FWB.value:
                $ add_point(KCT.BOYFRIEND)
            elif chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                $ add_point(KCT.TROUBLEMAKER)
            scene v14s44_4
            with dissolve

            u "I'm gonna see what Lindsey has to offer."

            scene v14s44_4b
            with dissolve

            el "*Scoffs* Good luck with that."

            scene v14s44_4
            with dissolve

            u "What do you have against her?"

            scene v14s44_4a
            with dissolve

            el "It's not that I have anything against her, dude."

            el "I'm used to Chloe being President, you know?"

            scene v14s44_4
            with dissolve

            u "Yeah, I think everyone is. That's why most people are voting for Lindsey, ha."

            scene v14s44_4a
            with dissolve

            $ set_presidency_percent(v14_lindsey_popularity + 2) #tick
            el "Hmm..."

    play sound "sounds/carbrake.mp3"

    scene v14s44_5 # TPP. Of a nice car pulling into the parking lot, With Elijah's mom (Elijah's mom should look like a very young hot woman, she should be wearing a nice suite and nice jewelry showing she is rich, requested that she is of differen't ethnic background than most characters.) inside, Elijah's mom slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v14s44_6 # TPP. The nice car with Elija's mom parking near Elijah and MC, Elijah's Mom slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v14s44_7 # TPP. Close up of Elijah's mom standing outside of the car with the driver door open looking over at Elijah, Elijah's Mom slight smile, mouth open.
    with dissolve

    elm "Elijah, are you coming? I've been waiting over there for-"

    scene v14s44_4c # FPP. Same as v14s44_4a, Elijah looking over at his mom(Mom off-camera), Elijah neutral face, mouth open.
    with dissolve

    el "Yes mom, I'm coming. I was just talking to-"

    scene v14s44_7a # TPP. Same as v14s44_7, Elijah's mom looking at MC, Slight smile, mouth open.
    with dissolve

    elm "Wait a minute..."

    scene v14s44_8 # TPP. Close up of Elijah's mom walking up to Elijah and MC.
    with dissolve

    pause 0.75

    scene v14s44_9 # FPP. Elijah standing next to MC and Elijah, Elijah's mom looking at Elijah(Elijah Off-camera), Elijah's mom slight smile, mouth open.
    with dissolve

    elm "You didn't tell me you had a friend with you?!"

    scene v14s44_4d # FPP. Same as v14s44_4c, Elijah looking at his mom(Elijah's mom off-camera), Elijah slightly annoyed, mouth open.
    with dissolve

    el "I don't..."

    scene v14s44_9a # FPP. Same as v14s44_9, Elijah's mom slightly angry, mouth open/
    with hpunch

    elm "Well, for fuck's sake Eli. It wouldn't kill you to try and make one."

    scene v14s44_4d
    with dissolve

    el "*Sighs* Can we just go? Come on. Get back in the car before more people see you..."

    scene v14s44_9b # FPP. Same as v14s44_9a, Elijah's mom now looking at MC, Elijah's mom extending her hand out for MC to shake, Elijah's mom slight smile, mouth open.
    with dissolve

    elm "I apologize for my son, he can be rude from time to time. It was nice meeting you..."

    menu:
        "Introduce yourself":
            $ add_point(KCT.TROUBLEMAKER)
            scene v14s44_10 # TPP. Show MC shaking Elijah's mom's hand, Elijah's mom slight smile, mouth closed, MC slight smile, mouth open.
            with dissolve

            u "[name]."

            scene v14s44_9c # FPP. Same as v14s44_9a, Elijah's mom no longer extending her hand out for MC, Elijah's mom, slight smile, mouth open.
            with dissolve

            elm "[name], very good."

            scene v14s44_4d
            with dissolve

            el "*Sighs*"

            scene v14s44_8a # TPP. Same as v14s44_8a, Elijah's mom walking back to the car, waving at MC, Elija's mom slight smile, mouth closed.
            with dissolve

            pause 0.75

            scene v14s44_11 # TPP. Close up of Elijah's mom's butt to show MC checking her out as she walks away.
            with dissolve

            pause 0.75

            scene v14s44_7a
            with dissolve

        "I'm Eli's friend":
            $ add_point(KCT.BRO)
            $ elijah.relationship = Relationship.FRIEND

            scene v14s44_10
            with dissolve

            u "[name]. Eli's friend."

            scene v14s44_4e # FPP. Same as v14s44_4d, Elijah neutral face with raised eyebrows, mouth closed,
            with dissolve

            pause

            scene v14s44_4f # FPP. Same as v14s44_4e, Elijah slight smile, mouth closed.
            with dissolve

            pause 0.75

            scene v14s44_4e
            with dissolve

            pause 0.75

            scene v14s44_9d # FPP. Same as v14s44_9c, Elijah's mom looking over at him, slight smile, mouth closed.
            with dissolve

            pause

            scene v14s44_9c
            with dissolve

            elm "[name]. I'll remember that."

            scene v14s44_9e # FPP. Same as v14s44_9c, Elijah's mom looking at MC, slight smile, mouth closed.
            with dissolve

            u "I hope so."

            scene v14s44_9f # FPP. Same as v14s44_9e, Elijah's mom winking at MC, slight smile, mouth closed.
            with dissolve

            pause 

            scene v14s44_8a
            with dissolve

            pause 0.75

            scene v14s44_11
            with dissolve

            pause 0.75

            scene v14s44_7a
            with dissolve

    elm "Alright, we're leaving. Bye, [name]!"

    scene v14s44_12 # TPP. Show Elijah walking towards the car.
    with dissolve

    pause 0.75

    play sound "sounds/cardooropen.mp3"

    scene v14s44_12a # TPP. Same as v14s44_12, Show Elijah getting in the car.
    with dissolve

    play sound "sounds/doorclose.mp3"

    u "(I did not expect Elijah's mom to look like that. Damn...)"

    scene v14s44_6a # TPP. Same as v14s44_6a, Elijah's mom and Elijah in the car, the car backing out, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v14s44_5a # TPP. Same as v14s44_5, Elijah's mom and Elijah in the car driving out of the parking lot, both slight smile, mouth closed.
    with dissolve

    pause

    scene v14s44_13 # TPP. Show a close up of a finger tapping on MC's shoulder.
    with dissolve

    pause 0.75

    scene v14s44_14 # TPP. Show MC turned around in a fighting stance looking at Imre, Neutral expression, mouth closed.
    with dissolve

    pause 0.75
    
    scene v14s44_15 # FPP. MC looking at Imre, Imre looking at MC, Imre slight smile, mouth closed.
    with dissolve

    u "WHAT THE FUCK?! Imre!"

    u "Why the fuck are you running up on me like that?!"

    scene v14s44_15a # FPP. Same as v14s44_15, Imre slight smile, mouth open.
    with dissolve

    imre "*Laughs* Sorry, bro! My bad, my bad..."

    imre "Now, who the FUCK was that with Elijah? His sister?"

    scene v14s44_15
    with dissolve

    u "*Chuckles* Nah, dude. Try his Mom."

    scene v14s44_15a
    with dissolve

    imre "His Mom?! You're fucking kidding-"

    imre "Her? The one that just got in the car?"

    scene v14s44_15
    with dissolve

    u "Haha, yes. Her."

    scene v14s44_15a
    with dissolve

    imre "That's the finest mom I've ever seen, [name]."

    scene v14s44_15
    with dissolve

    menu:

        "She was pretty hot":
            $ add_point(KCT.BRO)

            u "She was pretty fucking hot. *Laughs*"

            scene v14s44_15a
            with dissolve

        "Meh, not my type":
            $ add_point(KCT.TROUBLEMAKER)

            u "Meh, she's not really my type."

            scene v14s44_15a
            with dissolve

            imre "Are you kidding me???"

    imre "I'm gonna have to apologize to my mom..."

    scene v14s44_15
    with dissolve

    u "Why? *Chuckles*"

    scene v14s44_15a
    with dissolve

    imre "'Cause I'm gonna have a new mommy here soon. Haha!"

    scene v14s44_15
    with dissolve

    u "Oh my god, no. *Laughs* Imre."

    u "Don't say it like that. Ever again."

    scene v14s44_15a
    with dissolve

    imre "It's the truth, bro."

    scene v14s44_15
    with dissolve

    u "*Laughs* Okay. Then tell me another truth, what did you send-"

    scene v14s44_15a
    with dissolve

    imre "Sorry, [name]! I'll catch you later. I've got something fun planned and I'm about to be late."

    scene v14s44_16 # FPP. Show Imre running off away from MC, Imre slight smile, mouth closed.
    with dissolve

    u "(Forgot all about the Riley thing, I guess? Either that or he's avoiding the hell out of it, ha.)"

    stop music fadeout 3

    jump v14s45