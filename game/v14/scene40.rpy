# SCENE 40: MC GOES TO BED WOLVES
# Locations: MC Wolves Bedroom
# Characters: MC (Outfit: 2), LAUREN (Outfit: Nude)
# Time: Night

label v14s40:
# -Scene 40 and 41 are identical except for location
    scene v14s40_2 # TPP. MC plops on his wolves bed after removing his clothes, slight smile, mouth closed
    with fade

    u "(Finally, time for some sleep.)"

    play music "music/v12/Track Scene 24.mp3" fadein 2

    if lauren.relationship.value >= Relationship.GIRLFRIEND.value:
        play sound "sounds/vibrate.mp3"
        scene v14s40_2a # TPP. MC gets a call from Lauren, MC looks at his phone, no expression
        with dissolve

        u "*Sighs*"

        scene v14s40_2b # TPP. MC answers his phone
        with dissolve

        u "Hello?"

        scene v14s40_3 # FPP. Show a close up of laurens face talking on her phone, lauren is lying in her bed, slight smile, mouth open
        with dissolve

        la "Sorry, babe... I'm sure I just woke you but, I just had the most amazing experience of my life!"

        scene v14s40_3a # FPP. same as v14s40_3 laurens mouth is closed
        with dissolve

        u "What happened?"

        scene v14s40_3
        with dissolve

        la "Don't laugh but..."

        scene v14s40_4 # FPP. wide shot of lauren laying on her bed, one hand holding her phone, the other hand laying to her side, fully nude, hey body is sweaty, full smile, mouth open
        with dissolve

        la "I just masturbated for the first time and... it felt amazing."

        scene v14s40_4a # FPP. same as v14s40_4 lauren places her hand not holding the phone on one of her nipples
        with dissolve

        la "Honestly, haha. I just want to keep going."

        scene v14s40_4b # FPP. same as v14s40_4a laurens mouth is closed
        with dissolve

        u "Ha... Wow, I'm happy for you, I think? *Laughs* You've never touched yourself before?"

        scene v14s40_4a
        with dissolve

        la "Believe it or not, no. This was my first time."

        scene v14s40_4b
        with dissolve

        u "Well, there certainly is a first time for everything."

        u "(\"There's a first time for everything\", The fuck am I on about? I need sleep...)"

        scene v14s40_4
        with dissolve

        la "Haha, yeah I guess..."

        scene v14s40_4c # FPP. same as v14s40_4 lauren has a concerned expression, laurens mouth is closed
        with dissolve

        la "Are you tired or something? You don't sound like yourself..."

        menu:
            "What'd I say?":
                $ add_point(KCT.TROUBLEMAKER)

                scene v14s40_4b
                with dissolve

                u "What'd I say again? I don't even remember..."

                scene v14s40_4a
                with dissolve

                la "Haha, go to sleep. I'll talk to you tomorrow, handsome."

                scene v14s40_4b
                with dissolve

                u "I'm sorry, we'll talk soon."

                scene v14s40_4a
                with dissolve

                la "Ha, goodnight. I'll keep my late night adventures to myself for now."

            "Yeah I'm tired":
                $ add_point(KCT.BOYFRIEND)

                scene v14s40_4b
                with dissolve

                u "Honestly, yeah. I'm just so tired. Sorry if what I said sounded weird, ignore my stupid talk."

                u "So... did you watch porn while you touched yourself?"

                scene v14s40_4a
                with dissolve

                la "At first I didn't, but then after a few times on my own I gave it a try."

                scene v14s40_4b
                with dissolve

                u "And?"

                scene v14s40_4d # FPP. same as v14s40_4a lauren moves her hand from her nipple down below her bellow button and just above her vagina, mouth open
                with dissolve

                la "I liked it, a lot."

                scene v14s40_4e # FPP. same as v14s40_4d laurens mouth is closed
                with dissolve

                u "Ha, I'm glad. Most importantly, what did you wanna call and tell me?"

                scene v14s40_4d
                with dissolve

                la "I don't know, really. I just wanted you to be thinking about me, I guess."

                scene v14s40_4e
                with dissolve

                u "I'm always thinking about you. *Chuckles*"

                scene v14s40_4d
                with dissolve

                la "Hehe... Goodnight, sweet [name]. I want to see you soon, okay?"

                scene v14s40_4e
                with dissolve

                u "You will, goodnight babe."

                scene v14s40_2c # TPP. same as v14s40_2a MC puts the phone away and lays back down
                with dissolve

                u "(Finally...)"

    scene v14s40_5 # TPP. MC's bedroom lights are off, Mc is sleeping in his wolves bed
    with dissolve

    pause 0.75

    scene v14s40_5a # TPP. same as v14s40_5 differnet sleeping position
    with dissolve

    pause 0.75

    scene v14s40_5b # TPP. same as v14s40_5a differnet sleeping position
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v14s40a