# SCENE 42: Arriving at Warehouse
# Locations: Abandoned Warehouse
# Characters: MC (Outfit 7), Grayson (Outfit 3), Ryan (Outfit 2), Caleb (Outfit 2), Cameron (Outfit 3), Sam (Outfit 2), Chris (Outfit 2), Imre (Outfit 4), Perry (Outfit 3), Sebastian (Outfit 1), Marcus (Outfit 2)
# Time: Saturday Night

label v9_at_warehouse:
    if mc.frat == Frat.WOLVES:
        scene v9aaw1 # FPP. Show Sebastian removing the blindfold being removed from Camera, blurry image (As if adjusting to the light).
        with fade
        
        play music music.ck1.v9.Track_Scene_42 fadein 2

        pause 1

        scene v9aaw1a # FPP. Same camera as v9aaw1, Sebastian stood infront of MC smiling, mouth closed.
        with dissolve

        menu:
            "Be upset":
                $ reputation.add_point(RepComponent.BOYFRIEND)

                u "Shit, Sebastian, was that really necessary?"

                scene v9aaw1b # FPP. Same camera as v9aaw1, Sebastian stood infront of MC smiling, mouth open.
                with dissolve

                se "You tell me."

            "Be excited":
                $ reputation.add_point(RepComponent.BRO)

                u "Mysterious! I like it."

                scene v9aaw1b
                with dissolve

        se "Check it out!"

        scene v9aaw2 # FPP. Sweeping shot of the warehouse, boxing ring should be main focus.
        with dissolve

        u "What is this place?"

        scene v9aaw1b
        with dissolve

        se "Well kept secret. Hence the blindfolds."

        scene v9aaw3 # FPP. Show Imre and Perry stood next to eachother, Perry excited, Imre neutral, Perry mouth open.
        with dissolve

        guyd "Holy shit, guys. This is major!"

        scene v9aaw3a # FPP. Same camera as v9aaw3, Perry excited, Imre neutral, Imre mouth open.
        with dissolve

        imre "Yeah, I wasn't expecting all this."

        scene v9aaw4 # FPP. Show Chris, Chris neutral, mouth open.
        with dissolve

        ch "I know."

        scene v9aaw1c # FPP. Same camera as v9aaw1, Sebastian angry, mouth open.
        with dissolve

        se "Wolves do things right. This took a lot of work. But it's gonna be worth it when you guys wipe the floor with those Apes."

        scene v9aaw4
        with dissolve

        ch "Alright. Let's keep it civil."

        ch "For now."

        scene v9aaw1c
        with dissolve

        se "For now."

        scene v9aaw4
        with dissolve

        ch "Sorry about that. He's still pissed about how his fight went."

        scene v9aaw4a # FPP. Same camera as v9aaw4, Chris neutral, mouth closed.
        with dissolve

        u "(Sebastian lost? Shit. I don't stand a chance.)"

        scene v9aaw4
        with dissolve

        ch "But we're not gonna have that problem tonight, because I know you guys are here to WIN!"

        scene v9aaw3b # FPP. Same camera as v9aaw3, both excited, Perry mouth open.
        with dissolve

        guyd "YEAH!"

        scene v9aaw3c # FPP. Same camera as v9aaw3, both excited, Imre mouth open.
        with dissolve

        imre "YEAH!"

        scene v9aaw1c
        with dissolve

        se "I WAS WINNING!"

        scene v9aaw4
        with dissolve

        ch "You guys trained very well, better than expected, really."

        scene v9aaw5 # FPP. Show Imre, Imre neutral expression, mouth closed.
        with dissolve

        menu:
            "Talk about Ryan":
                $ reputation.add_point(RepComponent.TROUBLEMAKER)

                u "*Whispers* Hey, Im, if I draw Ryan first, want me to warm him up for you?"

                scene v9aaw5a # FPP. Same camera as v9aaw5a, Imre angry, mouth open.
                with dissolve

                imre "Fuck no! I want you to hand him over."

            "Keep quiet":
                u "(Better not rile him up.)"

                
        scene v9aaw4
        with dissolve

        ch "You have a challenge ahead of you. I'm not gonna lie."

        scene v9aaw4a
        with dissolve

        if hl_punch:

            u "(I have a reputation to uphold.)"

        else:
            # -If MC got punched in 12-
            u "(Oh, God what if they boo me when I get in the ring?)"

            show glitch
            play sound sound.glitch
            pause 0.1
            hide glitch

            if dreamFightChoice == "ryan":
                scene v9dream12a # IGNORE THIS
                with hpunch

                pause 1

                play sound sound.fall

                scene v9dream12b # IGNORE THIS
                with hpunch

                pause 1

            elif dreamFightChoice == "caleb":
                scene v9dream14a # IGNORE THIS
                with hpunch

                pause 1

                play sound sound.fall

                scene v9dream14b # IGNORE THIS
                with hpunch

                pause 1
            
            show glitch
            play sound sound.glitch
            pause 0.1
            hide glitch

        scene v9aaw4
        with dissolve

        ch "They're gonna fight dirty. But you can't stoop to their level."

        scene v9aaw6 # FPP. Show Imre, Perry and Chris, Imre and Perry looking at Chris, Imre frown, mouth open.
        with dissolve

        imre "Aww, man."

        scene v9aaw6a # FPP. Same camera as v9aaw6a, Chris mouth open.
        with dissolve

        ch "Is there something I should know?"

        scene v9aaw6b # FPP. Same camera as v9aaw6, Chris mouth closed.
        with dissolve

        menu:
            "Tell Chris about Ryan":
                $ reputation.add_point(RepComponent.TROUBLEMAKER)
                
                u "(If I don't say something, this could get out of hand.)"

                u "Sorry man."

                u "Ryan started some shit earlier and I had to pull Imre off of him."

                scene v9aaw6a
                with dissolve

                ch "Ah, told ya man, fighting dirty. But that's fine. He started shit, you finish it in the ring. That goes for all of you."

                scene v9aaw6c # FPP. Same camera as v9aaw6, Chris smile, mouth open.
                with dissolve


            "Keep quiet":
                $ reputation.add_point(RepComponent.BRO)

                u "(Not my place.)"

                scene v9aaw6c
                with dissolve

                ch "Fine. Let's just keep it clean 'til we're in the ring."

        ch "Okay, guys. Go check out the place, chill for a bit. Get familiar with the setup. And let's meet up five minutes before first bell. I'm rooting for you."

        scene v9aaw7 # FPP. Show everyone splitting up and walking their own way.
        with dissolve

    else:
        scene v9aaw8 # FPP. Show Cameron removing the blindfold being removed from Camera, blurry image (As if adjusting to the light).
        with fade

        play music music.ck1.v9.Track_Scene_42 fadein 2

        pause 1

        scene v9aaw8a # FPP. Same camera as v9aaw8, Cameron stood infront of MC, looking agitated, mouth closed. (Image no longer blurry going forward)
        with dissolve

        menu:
            "Complain":
                $ reputation.add_point(RepComponent.TROUBLEMAKER)

                u "What the fuck, man?"

                scene v9aaw8b # FPP. Same canera as v9aaw8, Cameron agitated, mouth open.
                with dissolve

                ca "Deal with it!"

                scene v9aaw8a
                with dissolve

                u "Geez."

            "Deal with it":
                $ reputation.add_point(RepComponent.BRO)

                u "(A bit over the top with the ambiance, bro.)"

                scene v9aaw9 # FPP. Show Cameron removing Calebs blindfold.
                with dissolve

                pause 1

                scene v9aaw9a # FPP. Same camera as v9aaw9, Caleb looking pissed, Cameron agitated, Caleb mouth open.
                with dissolve

                cal "What the fuck?"

                scene v9aaw9b # FPP. Same camera as v9aaw9, Show Cameron slapping Caleb upside the head, Cameron mouth open.
                with dissolve
                
                ca "Deal with it!"

        scene v9aaw10 # FPP. Show Grayson, serious expression, mouth open.
        with dissolve

        gr "Take it all in boys."

        scene v9aaw2
        with dissolve

        u "Big time."

        scene v9aaw10a # FPP. Same camera as v9aaw10, Grayson serious smile, mouth open.
        with dissolve

        gr "Damn right!"

        if hl_punch:
            scene v9aaw11 # TPP. Show Grayson slapping MC on the arm in a good way, MC smile, Grayson smile mouth open.
            with dissolve

            gr "Nothing but the best for Rocky, here!"

            scene v9aaw11a # TPP. Same camera as v9aaw11, Grayson stood infront of MC smiling, mouth closed.
            with dissolve

            u "(I wonder if that's gonna stick. Not bad as far as nicknames go, though.)"
        
        else:
            scene v9aaw11b # TPP. Same camera as v9aaw11, show Grayson stood right in MC's face, serious expression, mouth open.
            with dissolve

            gr "*Whispers* Don't let me down, freshman."

        scene v9aaw12 # FPP. Show Grayson pacing around, Cameron stood behind Grayson agitated expression, looking at something out of view. Grayson serious expression, Mouths closed.
        with dissolve

        u "(Hmm, what's that about?)"

        scene v9aaw12a # FPP. Same camera as v9aaw12, Grayson pacing elsewhere serious expression, mouth open. (Cameron still behind Grayson)
        with dissolve

        gr "There's a lot riding on this fight. Not only our reputations, but power over the whole school. You can walk through the halls and KNOW you won't be fucked with."

        scene v9aaw12b # FPP. Same camera as v9aaw12, Grayson stops pacing and looks directly at camera, serious expression, mouth open. (Cameron still behind Grayson)
        with dissolve

        gr "You're Apes now! And with great honor comes great responsibility."

        scene v9aaw13 # FPP. Show Sebastian stood in the distance (same direction where Cameron was looking) Sebastian angry, mouth closed.
        with dissolve

        pause 1

        scene v9aaw12c # FPP. Same camera as v9aaw12, Grayson stopped pacing, looking at camera, serious expression, mouth closed. (Cameron still behind Grayson)
        with dissolve

        menu:
            "Say something":
                $ reputation.add_point(RepComponent.TROUBLEMAKER)
                u "Um... what's up with Cam?"

                scene v9aaw12d # FPP. Same camera as v9aaw12, Grayson turns to face cameron, Cameron looks at Grayson, Cameron angry, Grayson serious, Grayson mouth open.
                with dissolve

                gr "Cam! I told you to chill. Wait."

                scene v9aaw12c
                with dissolve

                u "(Wait? For what? What the hell is happening?)"

            "Keep quiet":
                u "(He's sure amped up, but what's Sebastian got to do with it?)"


        scene v9aaw12e # FPP. Same camera as v9aaw12, Grayson gestures cameron to come over, Grayson serious expression, mouth open.
        with dissolve

        gr "Come take over. I have to make sure shit's ready to go."

        scene v9aaw14 # FPP. Show Grayson walking away and Cameron walking over, Cameron looking at camera, mouth open.
        with dissolve

        ca "Hello again, maggots."

        scene v9aaw14a # FPP. Show Cameron looking in the same direction he was before, angry, mouth open.
        with dissolve

        ca "Where were we?"

        scene v9aaw14b # FPP. Same camera as v9aaw14, angry, mouth closed.
        with dissolve

        ry "Great responsibility?"

        scene v9aaw14c # FPP. Same camera as v9aaw14, Cameron looking at camera, slight agitated, mouth open.
        with dissolve

        ca "Yeah... forget that shit. Listen, you gotta pound those pups into the ground. You hear me?"

        scene v9aaw14d # FPP. Same camera as v9aaw14, Cameron no longer looking at the camera looking at the other pledges next to MC.
        with dissolve

        ry "Yeah!"

        scene v9aaw14e # FPP. Same camera as v9aaw14, Cameron super angry shouting, mouth open.
        with dissolve

        ca "YOU HEAR ME?!"

        scene v9aaw14f # FPP. Same camera as v9aaw14, Cameron super angry, mouth closed.
        with dissolve

        menu:
            "Get pumped":
                $ reputation.add_point(RepComponent.BRO)

                u "They're going down!"
                
                cal "They'll wish they never even pledged in the first place!"

                scene v9aaw14e
                with dissolve

                ca "Come out swinging and leave nothing to chance. Fuck their shit up!"

            "Ask Cameron what's up":
                u "What's going on? Why do you keep looking over there?"

                scene v9aaw14c
                with dissolve

                ca "Unfinished business."

                scene v9aaw14b
                with dissolve

                ry "Ha! Same, bro. Same."

                scene v9aaw15 # TPP. Show Cameron in Ryan's face, Cameron angry, mouth open.
                with dissolve

                ca "Well you make sure you handle your business in that ring, you hear?"

                scene v9aaw15a # TPP. Same camera as v9aaw15, Cameron now stepped slightly back away form Cameron, Ryan mouth open.
                with dissolve

                ry "Fuck yeah."

        scene v9aaw14c
        with dissolve

        ca "Apes don't fail and failures can't be Apes. Am I clear?"

        scene v9aaw14b
        with dissolve

        u "(Shit, really?)"

        scene v9aaw14c
        with dissolve

        ca "Am I clear?!"

        scene v9aaw14b
        with dissolve
        
        u "Yes!"

        ry "Yes!"

        cal "Yes!"

        scene v9aaw14c
        with dissolve

        ca "I'm gonna go finish my business. Get out of my face!"

        scene v9aaw16 # TPP. Show Ryan Caleb and MC stood next to eachother, Cameron walking away agitated expression, mouths closed.
        with dissolve

        stop music fadeout 3

        pause 1

    jump v9_warehouse_josh