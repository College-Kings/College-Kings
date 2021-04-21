# SCENE 25: Your Room Fri Evening
# Locations: MC Wolves/Apes room
# Characters: MC (Outfit 3)
# Time: Friday Evening

label v9_room_fri_eve:
    if joinwolves:
        scene v9rfe1 # TPP. Show MC on his bed in Wolves room reading a book.
        with fade

        u "(I wonder how much Mr. Lee expects us to remember from everyone else's Viking scenes. I was too busy looking at the costumes to pay attention.)"

        scene v9rfe1a # TPP. Same camera as v9rfe1, show MC placing the book down and looking bored.
        with dissolve

        u "(I'm so bored.)"

        if laurenrs:
            scene v9rfe1b # TPP. Same camera as v9rfe1, show MC on his phone.
            with dissolve    

            u "(Wonder how Lauren's doing with the Deers charity)"

            $ phoneexit = "s25_ContinueW"

            $ contact_Lauren.addReply("How's it going? You still doing our statue idea?", "s25_LauReplyW1")

            $ showphone = True
            call screen phone

            label s25_LauReplyW1:
                $ contact_Lauren.newMessage("Of course. I'm glad you talked me into it.")
                $ contact_Lauren.addReply("Me too. I don't think anyone's tried something like this before. You'll be the talk of the school!", "s25_LauReplyW2")

                call screen messager(contact_Lauren)

            label s25_LauReplyW2:
                $ contact_Lauren.newMessage("No, WE will. I couldn't have done it without your help.")
                $ contact_Lauren.addReply("Don't mention it, talk soon?", "s25_LauReplyW3")

                call screen messager(contact_Lauren)

            label s25_LauReplyW3:
                $ contact_Lauren.newMessage("Sure!")

                call screen messager(contact_Lauren)

            label s25_ContinueW:
                if contact_Lauren.messages[-1].replies:
                    "(I should text Lauren.)"
                    jump s25_ContinueW

            $ showphone = False

        scene v9rfe2 # TPP. Show MC's door.
        with dissolve

        play sound "sounds/knock.mp3"

        "*knock* *knock*"

        u "Come in!"
        
        jump v9_fri_training_w_wolves

    else:
        scene v9rfe3 # TPP. Show MC on his bed in Apes room reading a book.
        with fade

        u "(I wonder how much Mr. Lee expects us to remember from everyone else's Viking scenes. I was too busy looking at the costumes to pay attention.)"

        scene v9rfe3a # TPP. Same camera as v9rfe3, show MC placing the book down and looking bored.
        with dissolve

        u "(I'm so bored.)"

        if laurenrs:
            scene v9rfe3b # TPP. Same camera as v9rfe3, show MC on his phone.
            with dissolve               

            u "(Wonder how Lauren's doing with the Deers charity)"

            $ phoneexit = "s25_ContinueA"

            $ contact_Lauren.addReply("How's it going? You still doing our statue idea?", "s25_LauReplyA1")

            $ showphone = True
            call screen phone

            label s25_LauReplyA1:
                $ contact_Lauren.newMessage("Of course. I'm glad you talked me into it.")
                $ contact_Lauren.addReply("Me too. I don't think anyone's tried something like this before. You'll be the talk of the school!", "s25_LauReplyA2")

                call screen messager(contact_Lauren)

            label s25_LauReplyA2:
                $ contact_Lauren.newMessage("No, WE will. I couldn't have done it without your help.")
                $ contact_Lauren.addReply("Don't mention it, talk soon?", "s25_LauReplyA3")

                call screen messager(contact_Lauren)

            label s25_LauReplyA3:
                $ contact_Lauren.newMessage("Sure!")

                call screen messager(contact_Lauren)

            label s25_ContinueA:
                if contact_Lauren.messages[-1].replies:
                    "(I should text Lauren.)"
                    jump s25_ContinueA

            $ showphone = False

        scene v9rfe4 # TPP. Show MC's door.
        with dissolve

        play sound "sounds/knock.mp3"

        "*knock* *knock*"

        u "Come in!"
    
        jump v9_train_w_apes