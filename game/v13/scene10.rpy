# SCENE 10: Imre and Ryan Pre Date
# Locations: Hotel Lobby
# Characters: RYAN (Outfit: 1), MC (Outfit: 2)
# Time: evening 

label v13s10:
    scene v13s10_1 # TPP Show MC and Chloe walking into the lobby
    with dissolve

    pause 0.75

    play music music.v13_Track_Scene_10 fadein 2

    scene v13s10_2 # FPP Chloe walking away while Ryan walks toward MC
    with dissolve

    pause 0.75

    if not v13s9_go_to_concert: # NEED PROPER VARIABLE NAME
        scene v13s10_3 # FPP Show Ryan talking to MC, smiling with mouth open
        with dissolve

        ry "Ready to go?"

        scene v13s10_3a # FPP Same angle as v13s10_3, Ryan smiling with mouth closed
        with dissolve

        u "Yeah man, I'm ready."

        scene v13s10_3
        with dissolve

        ry "Good, let's just sit over here until we see him walk out."

        scene v13s10_3a
        with dissolve

        u "Okay."

    else: # -If Don't go in Scene 9
        scene v13s10_3
        with dissolve

        ry "You sure you're not coming?"

        scene v13s10_3a
        with dissolve

        u "Yeah, man. I'm gonna sit here and wait for my concert companion. *Chuckles*"

        scene v13s10_3
        with dissolve

        ry "I'll sit with you, I'm waiting for Imre to leave so I can follow him out."

        scene v13s10_3a
        with dissolve

        u "Sounds good."

    # -Regardless of everything

    scene v13s10_4 # TPP Show MC and Ryan moving toward seats in the lobby
    with dissolve
    
    pause 0.75

    scene v13s10_5 # TPP MC and Ryan sitting in the lobby, waiting, looking bored
    with dissolve

    pause 0.75

    scene v13s10_5a # TPP Same angle as v13s10_3, Ryan looking at his phone, MC with his head hanging back in boredom
    with dissolve
    
    scene v13s10_6 # FPP Show Imre walking through lobby toward hotel doors
    with dissolve

    ry "There goes Imre."

    u "Yep."

    if not v13s9_go_to_concert: # NEED PROPER VARIABLE NAME
        scene v13s10_7 # FPP View of MC, sitting next to Ryan. Ryan smiling with mouth closed
        with dissolve

        u "Let's go play I Spy."

        scene v13s10_7a # FPP Same angle as v13s10_7, Ryan smiling with mouth open
        with dissolve

        ry "*Chuckles*"

        scene v13s10_8 # TPP Show Ryan and MC leaving the hotel, Imre visible just a bit ahead outside the door looking back at them, smiling
        with dissolve

        pause 0.75

    else: # -If Don't Go
        scene v13s10_7a
        with dissolve

        ry "I'll catch you later, man."

        scene v13s10_7
        with dissolve

        u "Call me if anything serious goes down."

        scene v13s10_7a
        with dissolve

        ry "Will do."

        scene v13s10_9 # FPP MC's view still sitting, Ryan walking away
        with dissolve

        pause 0.75
        
        # -MC gets a text from Aubrey or Penelope depending on who he's going with-

        if v13_aubrey_concert: # If invited Aubrey    
            scene v13s10_10 # FPP MC sitting in lobby, pulling his phone out of his pocket
            with dissolve

            u "Who's buzzing me?"

            play sound sound.vibrate

            $ MessengerService.new_message(aubrey, "Still getting ready, meet you in about an hour? We still have plenty of time.")
            $ MessengerService.add_reply(aubrey, "Haha, OK ")
    
            while MessengerService.has_replies(aubrey):
                call screen phone
                
                if MessengerService.has_replies(aubrey):
                    u "(I should check my phone.)"
    
        elif v13_penelope_concert: # If invited Penelope/Penelope invited MC    
            scene v13s10_10
            with dissolve

            u "Who's buzzing me?"

            play sound sound.vibrate

            $ MessengerService.new_message(penelope, "Trying to finish some things for Ms. Rose, give me about an hour?")
            $ MessengerService.add_reply(penelope, "No worries, we have time.")

            while MessengerService.has_replies(penelope):
                call screen phone
                if MessengerService.has_replies(penelope):
                    u "(I should check my phone.)"

        # SINCE IT IS POSSIBLE TO NOT GET CONCERT TICKETS AT ALL, I ADDED THIS LINE. IF THIS SCENE DOESN'T OCCUR IF MC DOESN'T GET THE TICKETS, REMOVE "ELSE" STATEMENT AND INDENT
        else: # If neither Penelope or Aubrey, then never got tickets
            scene v13s10_10
            with dissolve

            u "(What else have I got to do?)"

        # -Regardless of concert companion
        scene v13s10_11 # FPP Show Ryan at the hotel front door, about to leave
        with dissolve

        u "Hey, Ryan!"

        scene v13s10_11a # FPP Same angle as v13s10_11, Ryan turning around to look at MC, Ryan's mouth open
        with dissolve

        ry "Yeah?"

        scene v13s10_11b # FPP Same angle as v13s10_11, Ryan looking at MC, Ryan's mouth closed
        with dissolve

        u "I may not be able to stay forever, but I'm coming with you."

        scene v13s10_11a
        with dissolve

        ry "Hell yeah!"

        #scene v12sX_ # -MC and Ryan walk out of the hotel-
        #with dissolve

        #pause 0.75

    stop music fadeout 3
    
    jump v13s11