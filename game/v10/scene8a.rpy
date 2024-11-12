# SCENE 8a: Fight Results
# Locations: Abandoned Warehouse
# Characters:MC (Outfit 7), Grayson (Outfit 3),Chris (Outfit 2)
# Time: Saturday Night
label v10_avoid_fight:
    $ renpy.end_replay()
    
    if not v10_ryan_fight and not v10_imre_fight:   
        scene v10frr1 # TPP. Show MC leaving the warehouse.(camera from inside wearhouse positioned behind mc)
        with dissolve

        play music music.ck1.v10.Track_Scene_8a fadein 2

        pause 0.75

        scene v10frr2 # TPP. Show MC having just left the warehouse (camera from outside, mc facing camera)        
        with dissolve

        if mc.frat == Frat.WOLVES:
            scene v10frr2a # TPP. same camera as v10frr2, Show MC having just left the warehouse (camera from outside, mc facing camera), Show chris just exiting the warehouse. MC mouth closed, Chris mouth open
            with dissolve

            ch "Hey!"

            u "(Really don't wanna talk right now.)"

            scene v10frr2c # TPP. same camera as v10frr2, Show chriss now right behind MC, Chris hand on MC shoulder, chris mouth open, MC mouth closed
            with dissolve

            ch "Hey! Man what was that? Why'd you run off like that?"

            scene v10frr3 # FPP. Show Chris, mouth closed, worried look.
            with dissolve

            u "*Sighs* Look I don't know okay."

            scene v10frr3a # FPP. same camera as v10frr3, Show Chris, mouth open, serious look.
            with dissolve

            ch "I'm going to try and be understanding, but it's really difficult for me to keep cool after I think about everything that's led up to this moment."

            scene s764 # Ignore this render, old image from 0.4
            with dissolve

            pause 0.4

            scene v10frr3a
            with dissolve

            ch "You were one of three pledges that got in even though many others fought for your spot."

            ch "And even now, here I am focusing on the guy that ran while everyone else, including Imre who did a spectacular job, is inside."

            ch "Busting their ass to show them they belong to the Wolves. Tonight was supposed to be a night of accomplishment and celebration."

            ch "If this is how you're going to act when push comes to shove then think real hard about if this is even for you."

            menu:
                "Apologize" (bro=1.0):
                    $ reputation.add_point(RepComponent.BRO)
                    scene v10frr3b # FPP. same camera as v10frr3, Show Chris, mouth closed, serious look.
                    with dissolve
                    u "*Sighs* What was I thinking? I shouldn't have let you guys down just because-"

                    scene v10frr3a
                    with dissolve

                    ch "Just because he's your friend?"

                    scene v10frr3b
                    with dissolve

                    u "Yeah... FUCK IT! I'll do it."

                    scene v10frr3a
                    with dissolve

                    ch "Glad you understand and got your head right, but that ship has sailed."

                    scene v10frr3b
                    with dissolve

                    u "I-"

                    scene v10frr3a
                    with dissolve

                    ch "It's probably best if you just go home. I don't think you wanna face the other Wolves right now."

                    scene v10frr3b
                    with dissolve

                    u "Chris, I-"

                    scene v10frr3a
                    with dissolve

                    ch "Just go home."

                "Stand your ground":
                    scene v10frr3b
                    with dissolve

                    u "I respect the Wolves, you guys are like family to me. But my friends are like family too."

                    scene v10frr3a
                    with dissolve

                    ch "Let me ask you this, would Ryan have hesitated to fight you?"

                    scene v10frr3b
                    with dissolve

                    u "He's my friend so-"

                    scene v10frr3a
                    with dissolve

                    ch "Be honest with yourself, would he have hesitated?"

                    scene v10frr3b
                    with dissolve

                    u "*Sighs* No."

                    scene v10frr3a
                    with dissolve

                    ch "It's probably best if you just go home. I don't think you wanna face the other Wolves right now."

                    scene v10frr3b
                    with dissolve
                    u "Chris, I-"

                    scene v10frr3a
                    with dissolve

                    ch "Just go home."
                    
        else:
            scene v10frr4 # TPP. Show MC stood near the side of the warehouse outside, Show Grayson approaching, grayson mouth open, MC mouth closed.
            with dissolve

            gr "Hey [name]!"

            u "(Really don't wanna talk right now.)"

            scene v10frr5 # FPP. Show Grayson, worried look, mouth open
            with dissolve

            gr "You okay, buddy? It looked like you were a bit overwhelmed there?"

            scene v10frr5a # FPP. Same camera as v10frr5, Show Grayson, worried look, mouth closed
            with dissolve

            u "I'm sorry, it was just. Would you have fought your friend like that?"

            scene v10frr5
            with dissolve

            gr "Ahhh, so that's the issue. You know, you actually remind me of a pledge we had last year... Him and I were real close."

            scene v10frr5a
            with dissolve

            u "Where is he now?"

            scene v10frr6 # TPP. Show MC and Grayson now stood by the corner of the building, both mouths closed.
            with dissolve

            pause 0.75

            scene v10frr6a # TPP. Same camera as v10frr6, Show MC and Grayson now stood around to corner with the door no exit no longer visable from where they're stood, both mouths closed.
            with dissolve

            scene v10frr7 # FPP. Show Grayson (now stood round the corner from v10frr5), worried look, mouth open
            with dissolve

            gr "Oh he dropped out of SVC. I think he ended up having some issues."

            scene v10frr7a # FPP. Show Grayson (now stood round the corner from v10frr5), worried look, mouth closed
            with dissolve

            u "What kind of issues?"

            u "Grayson?"

            u "What kind of issues?"

            scene v10frr8 # TPP. Show Grayson arm pulled back ready to punch MC.
            with dissolve

            pause 0.5

            scene v10frr8a # TPP. same camera as v10frr8, Show Grayson Punching MC in the stomach.
            with dissolve
            gr "He."

            scene v10frr8
            with dissolve

            pause 0.5

            scene v10frr8a
            with dissolve
            gr "Was."

            scene v10frr8
            with dissolve

            pause 0.5

            scene v10frr8a
            with dissolve
            gr "A."

            scene v10frr8
            with dissolve

            pause 0.5

            scene v10frr8a
            with dissolve
            gr "Fucking."

            scene v10frr8
            with dissolve

            pause 0.5

            scene v10frr8a
            with dissolve
            gr "Pussy!"

            scene v10frr7b # FPP. Same camera as v10frr7, Show Grayson angry look, mouth closed
            with dissolve

            u "Fuck! Why'd you do that?!"

            scene v10frr7c # FPP. Same camera as v10frr7, Show Grayson angry look, mouth open
            with dissolve

            gr "I don't care if we share the same fucking blood, a fight is a fight! You ever do any pussy shit like this again and you're out! You got that?"

            scene v10frr7b
            with dissolve

            u "*Cough* Yeah..."

            scene v10frr7c
            with dissolve

            gr "Now get the fuck out of here, I don't wanna see your face!"

            scene v10frr7b
            with dissolve

            u "(Fuck that hurt, I'm going home.)"

    stop music fadeout 3

    jump v10_leave_fight