# SCENE 34: MC arrives back at home
# Locations: Wolves/apes room.
# Characters: MC (Outfit: Suit then outfit: 2)
# Time: Afternoon

label v15s34:
    play music "music/v13/Track Scene 52a.mp3" fadein 2

    if joinwolves:
        play sound "sounds/dooropen.mp3"

        scene v15s34_1 # TPP. Show MC entering his room in the Wolves room in his suit from the wedding, slight smile ,mouth closed.
        with dissolve

        pause 0.75

        if "v15_naomi" in sceneList: # Placeholder for naomi blowjob being true
            play sound "sounds/doorclose.mp3"

            scene v15s34_2 # TPP. Show MC in the middle of his wolves room, slight frown, mouth closed.
            with dissolve

            u "(Well, I'm glad that's over. I'm not surprised Aubrey didn't want to ride home with me.)"

            u "(I just hope I can fix things between us.)"

        else:
            play sound "sounds/doorclose.mp3"

            scene v15s34_2a # TPP. Show MC in the middle of his wolves room, slight smile, mouth closed.
            with dissolve

            u "(I really enjoyed my day with Aubrey.)"
            u "(She seems comfortable sharing so much of her life with me now and sees me as someone she can trust.)"

            if aubrey.relationship >= Relationship.TAMED:
                u "(And I'm so excited to see what's next for us...)"
        
        scene v15s34_3 # TPP. Show MC taking off the top part of his suit in the middle of his wolves room.
        with dissolve

        pause 0.75

        scene v15s34_3a # TPP. MC's top gone, MC taking off the bottom part of his suit in the middle of his wolves room, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s34_3b # TPP. MC standing in the middle of his wolves room in just his underwear, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s34_3c # TPP. MC standing in the middle of his wolves room putting on his shirt.
        with dissolve

        pause 0.75

        scene v15s34_3d # TPP. MC standing in the middle of his wolves room putting on his pants, slight smile, mouth closed.
        with dissolve

        pause 0.75

        play sound "sounds/vibrate.mp3"

        scene v15s34_3e # TPP. Show MC standing in the middle of his wolves room in the entire Outfit: 2, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s34_4 # TPP. Close up of MC in his wolves room pulling out his phone, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s34_4a # TPP. Close up of MC in his wolves room looking at his phone, slight smile, mouth close.
        with dissolve

        pause 0.75

        if v14_help_lindsey:
            if v15_lindsey_gamenight:
                $ lindsey.messenger.newMessage("Hey, our game night is starting in 15 minutes. Hope you're on your way now! :)", force_send=True)
                $ lindsey.messenger.addReply("Oh, yeah! I haven't forgotten ;) OMW.", func=None)
            else:
                $ lindsey.messenger.newMessage("Hey, I hope you're ready for our VIP night. We'll be picking you up in the limo in about 15 minutes!", force_send=True)
                $ lindsey.messenger.addReply("Yeah, let's get our VIP party on! See you soon :)", func=None)
        else:
            $ lindsey.messenger.newMessage("Hey, I'm having a game night to help secure some extra influence and votes for my campaign. Someone bailed on me at the last minute, so... Wanna come take their place? :)", force_send=True)
            $ lindsey.messenger.addReply("Hey! Yeah, sounds fun.")
            $ lindsey.messenger.newMessage("Amazing! Be at the Chicks house in 15 minutes :)")
            $ lindsey.messenger.addReply("Haha, that soon? Damn, okay. I'm OMW!", func=None)

        label v15s34_PhoneContinue:
            if lindsey.messenger.replies:
                call screen phone
            if lindsey.messenger.replies:
                u "(I should reply to Lindsey)"
                jump v15s34_PhoneContinue

        scene v15s34_3e 
        with dissolve

        u "(Just got home and now I'm heading out again... There's never a dull moment, haha.)"

        play sound "sounds/dooropen.mp3"

        scene v15s34_5 # TPP. Show MC leaving his wolves room, slight smile, mouth closed.
        with dissolve

        pause 0.75

        play sound "sounds/doorclose.mp3"

        pause 0.75

        stop music fadeout 3

        if v14_help_lindsey and not v15_lindsey_gamenight: #If Helping Lindsey with VIP Night, go there
            jump v15s38

        else: #If Helping Lindsey with Game Night, go there. If not helping Lindsey, go to Game Night too.
            jump v15s35

    else:
        play sound "sounds/dooropen.mp3"

        scene v15s34_6 # TPP. Show MC entering his room in the apes room in his suit from the wedding, slight smile ,mouth closed.
        with dissolve

        pause 0.75

        if "v15_naomi" in sceneList: # Placeholder for naomi blowjob being true
            play sound "sounds/doorclose.mp3"

            scene v15s34_7 # TPP. Show MC in the middle of his apes room, slight frown, mouth closed.
            with dissolve

            u "(Well, I'm glad that's over. I'm not surprised Aubrey didn't want to ride home with me.)"

            u "(I just hope I can fix things between us.)"

        else:
            play sound "sounds/doorclose.mp3"

            scene v15s34_7a # TPP. Show MC in the middle of his apes room, slight smile, mouth closed.
            with dissolve

            u "(I really enjoyed my day with Aubrey.)"
            u "(She seems comfortable sharing so much of her life with me now and sees me as someone she can trust.)"

            if aubrey.relationship >= Relationship.TAMED:
                u "(And I'm so excited to see what's next for us...)"
        
        scene v15s34_8 # TPP. Show MC taking off the top part of his suit in the middle of his apes room.
        with dissolve

        pause 0.75

        scene v15s34_8a # TPP. MC's top gone, MC taking off the bottom part of his suit in the middle of his apes room, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s34_8b # TPP. MC standing in the middle of his apes room in just his underwear, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s34_8c # TPP. MC standing in the middle of his apes room putting on his shirt.
        with dissolve

        pause 0.75

        scene v15s34_8d # TPP. MC standing in the middle of his apes room putting on his pants, slight smile, mouth closed.
        with dissolve

        pause 0.75

        play sound "sounds/vibrate.mp3"

        scene v15s34_8e # TPP. Show MC standing in the middle of his apes room in the entire Outfit: 2, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s34_9 # TPP. Close up of MC in his apes room pulling out his phone, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s34_9a # TPP. Close up of MC in his apes room looking at his phone, slight smile, mouth close.
        with dissolve

        pause 0.75

        if v14_help_lindsey:
            if v15_lindsey_gamenight:
                $ lindsey.messenger.newMessage("Hey, our game night is starting in 15 minutes. Hope you're on your way now! :)", force_send=True)
                $ lindsey.messenger.addReply("Oh, yeah! I haven't forgotten ;) OMW.", func=None)
            else:
                $ lindsey.messenger.newMessage("Hey, I hope you're ready for our VIP night. We'll be picking you up in the limo in about 15 minutes!", force_send=True)
                $ lindsey.messenger.addReply("Yeah, let's get our VIP party on! See you soon :)", func=None)

        else:
            $ lindsey.messenger.newMessage("Hey, I'm having a game night to help secure some extra influence and votes for my campaign. Someone bailed on me at the last minute, so... Wanna come take their place? :)", force_send=True)
            $ lindsey.messenger.addReply("Hey! Yeah, sounds fun.")
            $ lindsey.messenger.newMessage("Amazing! Be at the Chicks house in 15 minutes :)")
            $ lindsey.messenger.addReply("Haha, that soon? Damn, okay. I'm OMW!", func=None)

        label v15s34_PhoneContinueL:
            if lindsey.messenger.replies:
                call screen phone
            if lindsey.messenger.replies:
                u "(I should reply to Lindsey)"
                jump v15s34_PhoneContinueL

        scene v15s34_8e 
        with dissolve

        u "(Just got home and now I'm heading out again... There's never a dull moment, haha.)"

        play sound "sounds/dooropen.mp3"

        scene v15s34_10 # TPP. Show MC leaving his apes room, slight smile, mouth closed.
        with dissolve

        pause 0.75

        play sound "sounds/doorclose.mp3"

        pause 0.75

        stop music fadeout 3

        if v14_help_lindsey and not v15_lindsey_gamenight: #If Helping Lindsey with VIP Night, go there
            jump v15s38

        else: #If Helping Lindsey with Game Night, go there. If not helping Lindsey, go to Game Night too.
            jump v15s35