# SCENE 25: Your Room Fri Evening
# Locations: MC Wolves/Apes room
# Characters: MC (Outfit 3)
# Time: Friday Evening

label v9_room_fri_eve:
    if mc.frat == Frat.WOLVES:
        scene v9rfe1 # TPP. Show MC on his bed in Wolves room reading a book.
        with fade

        u "(I wonder how much Mr. Lee expects us to remember from everyone else's Viking scenes. I was too busy looking at the costumes to pay attention.)"

        play music music.ck1.v9.Track_Scene_25 fadein 2

        scene v9rfe1a # TPP. Same camera as v9rfe1, show MC placing the book down and looking bored.
        with dissolve

        u "(I'm so bored.)"

        if CharacterService.is_girlfriend(lauren):
            scene v9rfe1b # TPP. Same camera as v9rfe1, show MC on his phone.
            with dissolve    

            u "(Wonder how Lauren's doing with the Deers charity.)"
            
            $ MessengerService.add_reply(lauren, _("How's it going? You still doing our statue idea?"))
            $ MessengerService.new_message(lauren, _("Of course. I'm glad you talked me into it."))
            $ MessengerService.add_reply(lauren, _("Me too. I don't think anyone's tried something like this before. You'll be the talk of the school!"))
            $ MessengerService.new_message(lauren, _("No, WE will. I couldn't have done it without your help."))
            $ MessengerService.add_reply(lauren, _("Don't mention it, talk soon?"))
            $ MessengerService.new_message(lauren, _("Sure!"))

            while MessengerService.has_replies(lauren):
                call screen phone
                if MessengerService.has_replies(lauren):
                    u "(I should text Lauren.)"

        scene v9rfe2 # TPP. Show MC's door.
        with dissolve

        play sound sound.knock

        "*Knock* *knock*"

        u "Come in!"
        
        jump v9_fri_training_w_wolves

    else:
        scene v9rfe3 # TPP. Show MC on his bed in Apes room reading a book.
        with fade

        u "(I wonder how much Mr. Lee expects us to remember from everyone else's Viking scenes. I was too busy looking at the costumes to pay attention.)"

        play music music.ck1.v9.Track_Scene_25 fadein 2

        scene v9rfe3a # TPP. Same camera as v9rfe3, show MC placing the book down and looking bored.
        with dissolve

        u "(I'm so bored.)"

        if CharacterService.is_girlfriend(lauren):
            scene v9rfe3b # TPP. Same camera as v9rfe3, show MC on his phone.
            with dissolve               

            u "(Wonder how Lauren's doing with the Deers charity.)"

            $ MessengerService.add_reply(lauren, _("How's it going? You still doing our statue idea?"))
            $ MessengerService.new_message(lauren, _("Of course. I'm glad you talked me into it."))
            $ MessengerService.add_reply(lauren, _("Me too. I don't think anyone's tried something like this before. You'll be the talk of the school!"))
            $ MessengerService.new_message(lauren, _("No, WE will. I couldn't have done it without your help."))
            $ MessengerService.add_reply(lauren, _("Don't mention it, talk soon?"))
            $ MessengerService.new_message(lauren, _("Sure!"))

            while MessengerService.has_replies(lauren):
                call screen phone
                if MessengerService.has_replies(lauren):
                    u "(I should text Lauren.)"

        scene v9rfe4 # TPP. Show MC's door.
        with dissolve

        play sound sound.knock

        "*Knock* *knock*"

        u "Come in!"
    
        stop music fadeout 3
        
        jump v9_train_w_apes