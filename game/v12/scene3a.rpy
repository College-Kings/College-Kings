# SCENE 3a: Penelope calls MC
# Location: Hotel room
# Characters: MC (Outfit 3), Penelope (Outfit 1)
# Time: Night

label v12_penelope_call:
    scene v12pec1 # TPP. Show MC sitting on the foot of his bed, slight smile, mouth closed
    with fade

    pause 0.75

    play music "music/v12/Track Scene 3a.mp3" fadein 2
    
    play sound sound.call

    scene v12pec1a # TPP. Same as v11pec1, MC slightly startled, mouth closed
    with dissolve

    pause 0.75

    scene v12pec2 # FPP. Same position as v12pec1, MC looking down at his phone (Penelope caller ID)
    with dissolve

    u "(It's Penelope.)"

    menu:
        "Answer":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            scene v12pec2b # FPP. Same as v11pec2, show MC clicking to accept the call
            with dissolve

            stop sound
            play sound "sounds/answercall.mp3"

            pause 0.75

            scene v12pec1b # TPP. Same as v12pec1, show MC talking on the phone, mouth open, slight smile
            with dissolve

            u "Hello?"

            scene v12pec3 # TPP. Show Penelope talking on a phone in the campus, slightly worried, mouth open
            with dissolve

            pe "Hey, hey! I didn't wake you, did I?"

            scene v12pec3a # TPP. Same as v12pec3, Penelope slight smile, mouth closed
            with dissolve

            u "Nope. I'm wide awake, what's up?"

            scene v12pec3b # TPP. Same as v12pec3a, Penelope slight smile, mouth open
            with dissolve

            pe "Oh, nothing really. I won't go into details, but all the money I owe the school is being handled. I met a good guy that's really helping me out."

            scene v12pec3a
            with dissolve

            u "A \"good guy\" is helping out... Interesting."

            scene v12pec3b
            with dissolve

            pe "*Laughs* From an actual loan place, [name]. I met him through Lindsey, actually."

            scene v12pec3c # TPP. Same as v12pec3a, different pose
            with dissolve

            u "*Chuckles* Wow, that's really great to hear. I'm really happy that it's all finally over, for both of us."

            scene v12pec3d # TPP. Same as v12pec3c, Penelope slight smile, mouth open
            with dissolve

            pe "Me too. So what's up with you? How's Europe, anything exciting?"

            scene v12pec3e # TPP. Same as v12pec3, Penelope very worried, mouth closed
            with dissolve

            u "Is watching someone get robbed considered exciting?"

            scene v12pec3f # TPP. Same as v12pec3e, Penelope very worried, mouth open
            with dissolve

            pe "WHAT!? Who got robbed? It wasn't one of you guys was it?"

            scene v12pec3e
            with dissolve

            u "It was actually Nora, and it happened in front of everyone."

            scene v12pec3f
            with dissolve

            pause 0.75

            if v12_chase_robber:
                scene v12pec3e
                with dissolve

                u "I had a little scuffle with the guy, but everyone is doing fine."

                scene v12pec3f
                with dissolve

                pe "YOU WHAT?!"

                scene v12pec3e
                with dissolve

                u "*Chuckles* Trust me, it's not bad at all. I'm perfectly fine and just laying here relaxing in my room. It feels good knowing you care so much though."

            else:
                scene v12pec3e
                with dissolve

                u "He got what he deserved though, Amber didn't respond too well to what he did."

                scene v12pec3f
                with dissolve

                pe "Is she okay?"

                scene v12pec3e
                with dissolve

                u "It's Amber... Do you really have to ask? *Chuckles* We're all fine, even Nora. It feels good knowing you care so much though."

            scene v12pec3g # TPP. Same as v12pec3, Penelope slightly sad, mouth open, different pose
            with dissolve

            pe "Of course I care, it almost makes me wish I was there to look out for you guys."

            scene v12pec3h # TPP. Same as v12pec3g, Penelope slightly sad, mouth closed
            with dissolve

            u "Last time you were looking out for people it got you in trouble."

            scene v12pec3g
            with dissolve

            pe "And? I'd do it again."

            scene v12pec3h
            with dissolve

            u "How noble? *Chuckles*"

            scene v12pec3i # TPP. Same as v12pec3, Penelope slightly sad, looking towards the end of the corridor, mouth closed
            with dissolve

            unknown "Young lady, international calls are not allowed on campus phones."

            scene v12pec3h
            with dissolve

            u "*Laughs* Who's that?"

            scene v12pec3g
            with dissolve

            pe "Umm, sorry [name]. I gotta go. It was really nice to hear from you."

            scene v12pec3h
            with dissolve

            u "Hey, wait!"

            scene v12pec3g
            with dissolve

            pe "Yeah?"

            menu:
                "Never mind":
                    $ reputation.add_point(RepComponent.BRO)
                    scene v12pec3c
                    with dissolve

                    u "Oh uhm, never mind... Sorry. Talk to you later."

                    scene v12pec3d
                    with dissolve

                    pe "*Chuckles* Alrighty, bye."

                "I miss you":
                    $ reputation.add_point(RepComponent.BOYFRIEND)
                    $ penelope.points += 1

                    scene v12pec3c
                    with dissolve

                    u "I just wanted to say I really miss you. It's weird being all the way across the world and not being able to see you, or even talk to you every day."

                    scene v12pec3d
                    with dissolve

                    pe "Aww... That was way too sweet, [name]. *Chuckles* I miss you too. Hurry back, okay?"

                    scene v12pec3a
                    with dissolve

                    u "Haha, I will. Bye."

                    scene v12pec3b
                    with dissolve

                    pe "Bye."

            scene v12pec2c # FPP. Same as v12pec2a, show MC clicking to end the call
            with dissolve

            play sound "sounds/rejectcall.mp3"
            pause 0.75
            stop music fadeout 3

            jump v12_roomate_talk #scene 4
            
        "Don't answer":
            $ reputation.add_point(RepComponent.BRO)
            scene v12pec2a # FPP. Same as v12pec2, show MC clicking to reject the call
            with dissolve

            stop sound
            play sound "sounds/rejectcall.mp3"

            u "(If it's serious she'll call again or leave a message.)"

            jump v12_roomate_talk