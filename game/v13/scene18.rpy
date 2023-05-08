# SCENE 18: Breakfast and Seeing Nora 
# Locations: Hotel Lobby
# Characters: MC (Outfit: 9), LUUK (Outfit: 1), NORA (Outfit: 2), CHRIS (Outfit: 2)
# Time: Morning

label v13s18:
    scene v13s18_1 # TPP. Show MC walking into Breakfast court in hotel lobby, slight smile, mouth open.
    with dissolve

    u "Hey Luuk, please tell me you got something for me today... *Chuckles*"

    play music music.v13_Track_Scene_18 fadein 2

    scene v13s18_2 # FPP. MC looking at Luuk, Luuk looking back at MC, slight smile, mouth open.
    with dissolve

    luuk "Indeed I do! Just have a seat while I whip it up."

    scene v13s18_98 # TPP. Show MC walking towards dining table, slight smile, mouth open.
    with dissolve

    u "My man... *Laughs*"

    scene v13s18_99 # TPP. Show MC pulling out the chair, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v13s18_3 # TPP. MC sitting in chair at the dining table.
    with dissolve

    pause 0.75

    scene v13s18_3a # TPP. Same as v13s18_3. MC looking at phone passing time.
    with dissolve

    pause 0.75

    scene v13s18_4 # TPP. Camera looking at the front of MC on his phone as Nora and Chris start walking by.
    with dissolve

    pause 0.75

    scene v13s18_4a # TPP. Same as v13s18_4. MC turning his head to see Nora and Chris walking past his chair. 
    with dissolve

    pause 0.75

    scene v13s18_5 # FPP. MC looking towards the hotel door where Chris and Nora are walking while holding hands.
    with dissolve

    pause 0.75

    scene v13s18_5a # FPP. Same as v13s18_5, Chris and Nora standing by the hotel door
    with dissolve

    pause 0.75

    scene v13s18_6 # TPP. Close up on Nora, Nora looking at Chris, Nora worried smile, mouth open, Chris slight smile, mouth closed.
    with dissolve

    no "*INAUDIBLE*"

    scene v13s18_7 # TPP. Close up on Chris, Chris looking at Nora, Chris slight smile, mouth open, Nora worried smile, mouth closed.
    with dissolve

    ch "*INAUDIBLE*"

    scene v13s18_6
    with dissolve

    no "*INAUDIBLE*"

    scene v13s18_7
    with dissolve

    ch "*INAUDIBLE*"

    scene v13s18_6
    with dissolve

    no "*INAUDIBLE*"

    scene v13s18_7
    with dissolve

    ch "*INAUDIBLE*"

    scene v13s18_5a
    with dissolve

    u "(What are they talking about?)"

    scene v13s18_7a # TPP. Same as v13s18_7, Chris looking out the hotel window, pointing at something on the street, slight smile, mouth open.
    with dissolve

    pause 0.75

    scene v13s18_6a # TPP. Same as v13s18_6, Nora still looking at Chris, Nora worried expression, mouth closed 
    with dissolve

    pause 0.75 

    scene v13s18_7
    with dissolve

    u "(Did they make up or what?)"

    scene v13s18_8 # TPP. Close up, Chris kissing Nora on the cheek, Nora worried smile, mouth closed.
    with dissolve

    pause 0.75

    scene v13s18_8a # TPP. Close up, Chris looking at Nora, Chris worried expression, mouth open, Nora looking down at the ground, worried smile, mouth closed
    with dissolve

    ch "Hey... You okay?"

    scene v13s18_6
    with dissolve

    no "Yeah. I'm fine... We're good."

    scene v13s18_7
    with dissolve

    ch "I'm glad to hear that, babe."

    scene v13s18_5b # FPP. Same as v13s18_5a, Mc looking at Nora, Nora looking at MC, Nora awkward smile, mouth closed
    with dissolve

    u "*Mouthing* What are you doing?"

    scene v13s18_9 # TPP. Chris gently pulling Nora by the arm outside the hotel, Nora following Chris outside.
    with dissolve

    ch "C'mon, there's the cab."

    scene v13s18_9a # TPP. Same as v13s18_9, Chris and Nora leaving through the hotel door.
    with dissolve

    pause 0.75

    scene v13s18_5c # FPP. Same as v13s18_5b MC looking at the Hotel entrance Chris and Nora gone.
    with dissolve

    if not "v12_nora" in sceneList:
        u "(Well... She looked... happy? *Chuckles*)"

    else:
        u "(We were just fucking the other night... and now she's back to holding hands with him?)"

        scene v13s18_3
        with dissolve

        u "(You know what? I think I'm gonna text her.)"

    menu:
        "Text Nora":
            $ MessengerService.add_reply(nora, _("What was that about, you guys all good now or something?"))
            $ MessengerService.new_message(nora, _("I know it's odd, but I'm trying to figure things out. Pls just... Let me handle it?"))
            $ MessengerService.add_reply(nora, _("Okay..."))
            
            while MessengerService.has_replies(nora):
                call screen phone
                if MessengerService.has_replies(nora):
                    u "(I should text Nora.)"
                    
            scene v13s18_4b # TPP. Show MC putting his phone away.
            with dissolve

            pause 0.75

        "Don't text Nora":
            scene v13s18_3
            with dissolve

            u "*Sighs* (Nah, nevermind. I'll just let this play out on its own...)"

    scene v13s18_10 # FPP. MC looking at Luuk standing next to the table with the food, Luuk slight smile, mouth open.
    with dissolve

    luuk "I worked hard on this masterpiece, so you better enjoy it... *Laughs*"

    scene v13s18_10a # FPP. Same as v13s18_10, Luuk slight smile, mouth closed
    with dissolve

    u "*Chuckles* I'm sure I will. Thanks."

    scene v13s18_10
    with dissolve

    luuk "Of course! So, you and Riley are getting ready to do your little \"Charli stunt\", huh?"

    scene v13s18_10a
    with dissolve

    u "*Shocked* How the fuck do you know that?"

    scene v13s18_10
    with dissolve

    luuk "I didn't, but I do now. *Laughs*"

    scene v13s18_10a
    with dissolve

    u "That's low man, real low."

    scene v13s18_10
    with dissolve

    luuk "It's part of my profession. Tell me how it goes later?"

    scene v13s18_10a
    with dissolve

    u "Haha, sure."

    scene v13s18_11 # FPP. MC looking at Luuk walk away.
    with dissolve

    pause 0.75

    scene v13s18_4c # TPP. Same as v13s18_4b, MC looking at plate of food.
    with dissolve

    pause 0.75

    scene v13s18_4d # TPP. Same as v13s18_4c, MC looking at empty plate.
    with fade

    pause 0.75

    stop music fadeout 3

    jump v13s19