# SCENE 35b: Game with roommate 
# Locations: Hotel Room 
# Characters: CHLOE (Outfit: 5), MC (Outfit: 2), RILEY (Outfit: 4)
# Time: Night
# Phone Images: None

label v12_game_roommate:
    if not v11_riley_roomate:
        scene v12grm1 # FPP. MC lying on his bed, looking as Chloe walks out of the bathroom, Chloe slight smile, mouth closed
        with dissolve

        pause 1.25

        play music "music/v12/Track Scene 35b_1.mp3" fadein 2

        scene v12grm2 # FPP. MC lying on his bed, looking at Chloe, Chloe sitting on her bed, looking at MC, slight smile, mouth open
        with dissolve

        cl "Hey!"

        scene v12grm2a # FPP. Same as v12grm2, Chloe slight smile, mouth closed
        with dissolve

        u "Hey, hey."

        scene v12grm2
        with dissolve

        cl "Am I crazy or did I hear yelling?"

        scene v12grm2a
        with dissolve

        u "You're not crazy, Nora and Chris are going at it."

        scene v12grm2b # FPP. Same as v12grm2, Chloe slightly worried, mouth open
        with dissolve

        cl "*Sighs* Her and I may not get along all the time, but no one should have to deal with all that bullshit."

        scene v12grm2c # FPP. Same as v12grm2b, Chloe slightly worried, mouth closed
        with dissolve

        u "Definitely does not look fun... I'll say that."

        if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
            scene v12grm2
            with dissolve

            cl "Luckily, my boyfriend would never put me through something like that, would he? *Chuckles*"

            scene v12grm2a
            with dissolve

            u "I wouldn't imagine it. *Chuckles*"

        scene v12grm2d # FPP. Same as v12grm2, Chloe holding her phone in landscape orientation, Chloe looking at phone, slight smile, mouth closed
        with dissolve

        u "\"You got games on your phone?\""

        scene v12grm2e # FPP. Same as v12grm2d, Chloe looking at MC, Chloe slight smile, mouth open
        with dissolve

        cl "Oh my god... You're not funny. *Chuckles*"

        scene v12grm2f # FPP. Same as v12grm2e, Chloe slight smile, mouth closed
        with dissolve

        u "Haha, I had to do it."

        scene v12grm2g # FPP. Same as v12grm2d, Chloe slight smile, mouth open
        with dissolve

        cl "Since you did ask though, yes. I just recently started playing this new life simulation game."

        scene v12grm2d
        with dissolve

        u "How do you play?"

        scene v12grm2g
        with dissolve

        cl "Basically, you create a character and just play with their life, but you have to complete milestones like get married, have kids, etc."

        scene v12grm3 # TPP. Show MC standing over Chloe, looking at her phone, both smiling, Chloe mouth closed, MC mouth open (Hide the phone screen)
        with dissolve

        u "That does not look like you... *Chuckles* Since when do you wear pigtails?"

        scene v12grm3a # TPP. Same as v12grm3, Chloe mouth open, smiling, MC mouth closed, smiling
        with dissolve

        cl "Stop it, [name]! I didn't have many options. *Chuckles*"

        scene v12grm3
        with dissolve

        u "Is that your house?"

        scene v12grm3a
        with dissolve

        cl "Yep, and that one right next to me just went for sale so when you download it in a second, that's the one you'll buy. *Chuckles*"

        scene v12grm3
        with dissolve

        u "Who said I was downloading it? *Chuckles*"

        scene v12grm3a
        with dissolve

        cl "I did, just now. *Laughs* Don't worry, I'll help you out."

        scene v12grm2d
        with dissolve

        u "Who made this game? It's pretty deep..."

        scene v12grm2e
        with dissolve

        cl "Some guy named, Undergrad Steve?"

        scene v12grm2f
        with dissolve

        u "Is he an undergrad? *Laughs*"

        scene v12grm2e
        with dissolve

        cl "Oh my gosh, I knew you were gonna say that... *Laughs*"

        scene v12grm2f
        with dissolve

        u "Just wanna make sure I have a good idea of the game, you know?"

        scene v12grm2g
        with dissolve

        cl "Mhmm. Okay, this game is based on your contacts so you'll be able to see the location of everyone in your phone if they're online. Can you see me?"

        scene v12grm2d
        with dissolve

        u "Yeah, I see you."

        scene v12grm2g
        with dissolve

        cl "Good, you should have some startup money so go ahead and buy this house next to me."

        scene v12grm2f
        with dissolve

        u "When did you start liking games?"

        scene v12grm2e
        with dissolve

        cl "I don't, but I do like this one. *Chuckles*"

        scene v12grm2f
        with dissolve

        u "*Chuckles* Alright, I got the house. Now what?"

        scene v12grm2g
        with dissolve

        cl "Now we build our characters' relationships until they can get married."

        scene v12grm2d
        with dissolve

        u "Married!?"

        if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
            scene v12grm2e
            with dissolve

            cl "What, you don't wanna marry me?"

            scene v12grm2f
            with dissolve

            u "Haha, I'd rather do that in real life."

            scene v12grm2e
            with dissolve

            cl "Wow... Good answer. Let's use this as a practice run though, I need the milestone. *Chuckles*"
        
        else:
            scene v12grm2h # FPP. Same as v12grm2e, Chloe different pose
            with dissolve

            cl "I need the milestone and you can only marry people from your contacts that you build a relationship with in game. Both people have to do it."

            scene v12grm2i # FPP. Same as v12grm2h, Chloe slight smile, mouth closed
            with dissolve

            u "This game is pretty serious."

            scene v12grm2h
            with dissolve

            cl "I know. Imre and Ryan play, but I wasn't about to sit there and play with them. *Laughs* Or marry them, not even in a game..."

            scene v12grm2i
            with dissolve

            u "*Laughs*"

        scene v12grm2h
        with dissolve

        cl "You talked about my character, yet yours look nothing like you! *Chuckles*"

        scene v12grm2i
        with dissolve

        u "That's probably 'cause I just hit randomize."

        scene v12grm2g
        with dissolve

        cl "Oh, come on! No creativity?"

        scene v12grm2d
        with dissolve

        u "I'll customize later, haha."

        scene v12grm2e
        with dissolve

        cl "Let's hurry up and get married so I can go to sleep. That sauna has really worn me out."

        scene v12grm4 # TPP. Same positioning as v12grm2h, show Chloe and MC playing on their phones, both smiling, mouths closed
        with dissolve

        pause 1.25
        
        scene v12grm4a # TPP. Same as v12grm4, different pose, show them laughing
        with dissolve

        pause 1.25

        scene v12grm4b # TPP. Same as v12grm4a, different pose, show them nudging each other, laughing
        with dissolve

        pause 1.25

        scene v12grm2e
        with dissolve

        cl "Alright, they're ready to get married! Let's see..."

        scene v12grm2g
        with dissolve

        cl "Ohhh, there's different types of weddings and depending on which one you choose, determines the wedding quality and what medal you get. We have to go with the big one!"

        scene v12grm2d
        with dissolve

        u "That's way too expensive!"

        scene v12grm2e
        with dissolve

        cl "So you just want your fiancée to be unhappy, huh?"

        scene v12grm2f
        with dissolve

        u "Hmmm, I think I have an idea..."

        scene v12grm2e
        with dissolve

        cl "What are you gonna do?"

        scene v12grm2f
        with dissolve

        u "Oh, you'll see."

        scene v12grm2d
        with dissolve

        menu:
            "Kill parents for insurance":
                $ add_point(KCT.TROUBLEMAKER)
                scene v12grm2f
                with dissolve

                u "How do you do the stealth thing?"

                scene v12grm2e
                with dissolve

                cl "Why do you need that?"

                scene v12grm2f
                with dissolve

                u "Nevermind. I figured it out."

                scene v12grm2j # FPP. Same as v12grm2g, Chloe mouth open, startled
                with dissolve

                cl "Wait, why did you need to- OH MY GOD! YOU KILLED YOUR PARENTS!?"

                scene v12grm2k # FPP. Same as v12grm2f, Chloe slightly worried, mouth closed
                with dissolve

                u "I prefer the phrase, \"got twelve million dollars\". Killed your parents sounds so harsh. *Chuckles*"

                scene v12grm2l # FPP. Same as v12grm2k, Chloe slightly worried, mouth open
                with dissolve

                cl "I don't get how you got the money though..."

                scene v12grm2f
                with dissolve

                u "My character background said my parents were rich, so I killed them and I got money in the will."

                scene v12grm2e
                with dissolve

                cl "This game allows that? Holy shit... *Chuckles*"

                scene v12grm2f
                with dissolve

                u "I guess so. *Laughs*"

            "Sell your house":
                $ add_point(KCT.BOYFRIEND)
                scene v12grm2d
                with dissolve

                u "Let's see, what's the best offer I can get?"

                scene v12grm2e
                with dissolve

                cl "Offers for what?"

                scene v12grm2f
                with dissolve

                u "You'll see."

                scene v12grm2j
                with dissolve

                cl "\"Meet your new neighbors\"? You sold your house!? It says you're homeless!"

                scene v12grm2k
                with dissolve

                u "It should say I'm homeless and rich... Got ten times more than what I bought it for."

                scene v12grm2l
                with dissolve

                cl "But you're homeless now, you did that for me?"

                scene v12grm2f
                with dissolve

                u "I'm playing the game for you. *Laughs*"

        scene v12grm2f
        with dissolve

        u "Now... Let's get to this wedding."

        scene v12grm2d
        with dissolve

        u "Alright, let's see... And... boom! Now, we're married."

        scene v12grm2e
        with dissolve

        cl "Yayyy! I got the milestone."

        scene v12grm2f
        with dissolve

        u "Oh cool! I got a millionaire milestone."

        scene v12grm2e
        with dissolve

        cl "We make a good team, but..."

        scene v12grm2
        with dissolve

        cl "...I'm going to bed now."

        scene v12grm2a
        with dissolve

        u "Awww! Just a little longer? I was starting to enjoy it... *Chuckles*"

        scene v12grm2
        with dissolve

        cl "No more for tonight."

        scene v12grm2a
        with dissolve

        u "Well, ain't that something... You risk everything to give a girl the wedding of her dreams and in the end she gives you the cold shoulder."

        scene v12grm2
        with dissolve

        cl "When I want the kids achievement, I'll call you."

        scene v12grm2a
        with dissolve

        u "Just want me when you need me... That's crazy..."

        scene v12grm2
        with dissolve

        cl "Welcome to the real world. *Chuckles*"

        scene v12grm2a
        with dissolve

        u "Actually, in the real world I can annoy you as much as I want."

        scene v12grm5 # TPP. Show MC tickling Chloe, Chloe laughing mouth open, MC smiling, mouth closed
        with dissolve

        cl "OH MY GOD! *Chuckles* STOP IT! [name]! PLEASE... PLEASE STOP! *Laughs*"

        if chloe.relationship.value >= Relationship.FWB.value:
            #scene v12grm2a
            scene v12grm5
            with dissolve

            u "*Laughs*"

            #scene v12grm2
            scene v12grm7a
            with dissolve

            cl "Just for that, you can sleep by yourself tonight."

            scene v12grm6 # TPP. Show MC sitting next to Chloe, Chloe slight smile, looking away from MC, MC close to her ear, mouth open, whispering, slight smile
            with dissolve

            u "*Whisper* You sure you don't want my company?"

            scene v12grm7 # FPP. MC and Chloe sitting next to each other on her bed, Chloe looking at MC, slight smile, mouth open
            with dissolve

            cl "Don't tease me, I'm tired! But, I guess you can stay and hold me... If you have to."

            scene v12grm7a # FPP. Same as v12grm7, Chloe slight smile, mouth closed
            with dissolve

            u "Is that your way of asking? *Chuckles*"

            scene v12grm7
            with dissolve

            cl "Please?"

            scene v12grm7a
            with dissolve

            u "Haha, as you wish. Let's head over to my bed."

            scene v12grm8 # TPP. Show MC and Chloe getting into MC's bed
            with dissolve

            pause 1.25

            scene v12grm9 # TPP. Show MC and Chloe sleeping together
            with dissolve

            pause 1.25

            scene v12grm9a # TPP. Same as v12grm9, different position
            with dissolve

            pause 1.25

            stop music fadeout 3

            jump v12_lindsey_lobby

        else:
            scene v12grm10 # TPP. MC was tickling Chloe, she pushes him off to the floor, MC startled, mouth closed, Chloe slightly worried mouth closed
            with dissolve

            pause 0.75

            scene v12grm11 # FPP. MC on the floor, looking up at Chloe who is sitting on her bed, Chloe slight smile, mouth open
            with vpunch
            play sound "sounds/fall.mp3"

            cl "Oh my god, are you okay?! *Chuckles?*"

            scene v12grm11a # FPP. Same as v12grm11, Chloe slight smile, mouth closed
            with dissolve

            u "Damn, you're pretty strong..."

            scene v12grm11
            with dissolve

            cl "Sorry, my reflexes kicked in. *Chuckles*"

            scene v12grm12 # TPP. Show MC getting up from the floor, slight smile, mouth closed
            with dissolve

            pause 0.75

            scene v12grm2a
            with dissolve

            u "Now I'm the tired one... Damn near knocked me out!"

            scene v12grm2
            with dissolve

            cl "*Laughs* You're exaggerating."

            scene v12grm2a
            with dissolve

            u "No I'm not! *Chuckles*"

            scene v12grm13 # TPP. Show Chloe turning off the lights
            with dissolve

            pause 0.75

            scene v12grm14 # FPP. MC lying down on his bed, Chloe lying down on her bed, MC looking at Chloe, Chloe looking at MC, Chloe slight smile, mouth open
            with dissolve

            cl "Goodnight, [name]."

            scene v12grm14a # FPP. Same as v12grm14, Chloe slight smile, mouth closed
            with dissolve

            u "Goodnight, Chloe."

            scene v12grm15 # TPP. Show MC sleeping alone in his bed
            with dissolve

            pause 0.75

            scene v12grm15a # TPP. Same as v12grm15, different position
            with dissolve

            pause 0.75

            stop music fadeout 3

            jump v12_lindsey_lobby

    else:
        scene v12grm1a # FPP. Same as v12grm1, Riley instead of Chloe, Riley mouth open, angry
        with dissolve

        ri "Steal anything else of mine while I was in the shower?"

        play music "music/v12/Track Scene 35b_2.mp3" fadein 2

        scene v12grm16 # FPP. Riley standing in front of MC's bed, Riley angry, mouth closed
        with dissolve

        u "Riley, I'm not doing this with you right now."

        scene v12grm16a # FPP. Same as v12grm16, Riley angry, mouth open
        with dissolve

        ri "If you didn't want me to be upset, you shouldn't have taken it. Even if you thought it was a joke or something, it's still not cool."

        scene v12grm16b # FPP. Same as v12grm16a, different pose
        with dissolve

        ri "Honestly... What's bothering me even more is that you keep lying."

        scene v12grm16
        with dissolve

        u "*Sighs*"

        scene v12grm16a
        with dissolve

        ri "So you're just gonna ignore me?"

        scene v12grm16
        with dissolve

        u "I already told you I didn't take it. Obviously no matter what I say, you're not gonna believe me."

        scene v12grm16c # FPP. Same as v12grm16, Riley walking away to her bed, scoffing, angry
        with dissolve

        ri "*Scoffs*"

        scene v12grm13a # TPP. Same as v12grm13, Riley turning off the lights instead of Chloe
        with dissolve

        pause 0.75

        scene v12grm15
        with dissolve

        pause 0.75

        scene v12grm15a
        with dissolve

        pause 0.75

        stop music fadeout 3

        jump v12_lindsey_lobby #scene 36 