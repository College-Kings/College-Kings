# Sun Evening in Room
# Location: MC Wolves Room, MC Apes Room
# Outfits: MC Outfit 2
# Time: Sunday Evening

label sun_eve_room:
    $ showphone = True
    $ phoneexit = "s19_phoneExit"

    if joinwolves:
        scene v8sser1 # TPP. Show MC lying on his Wolves bed on his phone.
        with fade

        if not laurenrs:
            play sound "sounds/vibrate.mp3"
            $ contact_Amber.newMessage("Hey u up?")
            $ contact_Amber.addReply("Always for you ;)", "s19_reply1")
            call screen messager(contact_Amber)

            label s19_reply1:
                $ contact_Amber.newMessage("That's what I was hoping to hear")
                $ contact_Amber.addReply("I can be even more up if you want...", "s19_reply2")
                call screen messager(contact_Amber)
            label s19_reply2:
                $ contact_Amber.newMessage("Really? Just like that?")
                $ contact_Amber.addReply("What can I say? You're hot", "s19_reply3")
                call screen messager(contact_Amber)
            label s19_reply3:
                $ contact_Amber.newMessage("You're pretty hot yourself and I'm... thinking about things")
                $ contact_Amber.addReply("What kind of things? Same things I'm thinking? ;)", "s19_reply4")
                call screen messager(contact_Amber)
            label s19_reply4:
                $ contact_Amber.newMessage("I think so")
                $ contact_Amber.addReply("Wanna see what thinking about you has done to me?", "s19_reply5")
                $ contact_Amber.addReply("I look at your pic all the time...when I'm thinking about things", "s19_reply18")
                call screen messager(contact_Amber)
                
            label s19_reply5:
                $ contact_Amber.newMessage("It's only fair, right? Make us even")
                if joinwolves:
                    $ contact_Amber.addImgReply("images/v08/Scene 19/w_dick_pic.jpg", "s19_reply6")
                else:
                    $ contact_Amber.addImgReply("images/v08/Scene 19/a_dick_pic.jpg", "s19_reply6")
                call screen messager(contact_Amber)
            label s19_reply6:
                $ contact_Amber.newMessage("Wow, better than I thought")
                $ contact_Amber.addReply("So you thought about it?", "s19_reply7")
                call screen messager(contact_Amber)
            label s19_reply7:
                $ contact_Amber.newMessage("Maybe")
                $ contact_Amber.addReply("Aw man you're driving me crazy", "s19_reply8")
                call screen messager(contact_Amber)
            label s19_reply8:
                $ contact_Amber.newMessage("So do something about it")
                $ contact_Amber.addReply("Now? What about you?", "s19_reply9")
                call screen messager(contact_Amber)
            label s19_reply9:
                $ contact_Amber.newImgMessage("images/v08/Scene 19/amb_pussy_pic.jpg")
                $ contact_Amber.addReply("Aw fuck", "s19_reply10")
                call screen messager(contact_Amber)
            label s19_reply10:
                $ contact_Amber.newMessage("You like?")
                $ contact_Amber.addReply("I love! You're so hot!", "s19_reply11")
                call screen messager(contact_Amber)
            label s19_reply11:
                $ contact_Amber.newMessage("What would you do if you were here?")
                $ contact_Amber.addReply("I would eat you until you couldn't take it anymore", "s19_reply12")
                call screen messager(contact_Amber)
            label s19_reply12:
                $ contact_Amber.newMessage("And then what?")
                $ contact_Amber.addReply("I'd fuck you so good you'd scream my name", "s19_reply13")
                call screen messager(contact_Amber)
            label s19_reply13:
                $ contact_Amber.newMessage("I'm close. Will you finish with me?")
                $ contact_Amber.addReply("Oh, God yes!", "s19_reply14")
                call screen messager(contact_Amber)
            label s19_reply14:
                scene v8sser2 # TPP. Show MC jerking off.
                with dissolve

                $ contact_Amber.newMessage("NOW!")
                $ contact_Amber.addReply("NOW!", "s19_reply15")

                call screen messager(contact_Amber)
            label s19_reply15:
                scene v8sser2 # TPP. Show MC finished jerking off.
                with dissolve

                $ contact_Amber.addReply("Holy shit, Amber! You're amazing!", "s19_reply16")

                call screen messager(contact_Amber)
            label s19_reply16:
                $ contact_Amber.newMessage("You weren't too bad yourself. Next time we need to do this in person")
                $ contact_Amber.addReply("Give me 5 minutes ;)", "s19_reply17")
                call screen messager(contact_Amber)
            label s19_reply17:
                $ contact_Amber.newMessage("You're so cute! But it's time for bed. Dream about me ;)")
                $ contact_Amber.addReply("With pleasure! Night!", "s19_replyCont1")
                call screen messager(contact_Amber)

            label s19_reply18:
                $ contact_Amber.newMessage("Good. Maybe someday we can think about things in the same room and see what happens")
                $ contact_Amber.addReply("Please do", "s19_reply19")
                call screen messager(contact_Amber)
            label s19_reply19:
                $ contact_Amber.newMessage("I guess I better get back to studying. I keep getting distracted")
                $ contact_Amber.addReply("I'm not gonna be able to think of anything else now. I'm done studying", "s19_reply20")
                call screen messager(contact_Amber)
            label s19_reply20:
                $ contact_Amber.newMessage("Well, sleep tight then ;)") 
                jump s19_replyCont1

        else:
            # -MC's phone buzzes-
            $ contact_Lauren.newMessage("Hey, Sweetie, what are you up to?")
            $ contact_Lauren.addReply("Nothing, just catching up on some homework. You having a good night?", "s19_reply21")
            call screen messager(contact_Lauren)
            label s19_reply21:
                $ contact_Lauren.newMessage("It would be better if you were here...")
                $ contact_Lauren.addReply("Really?", "s19_reply22")
                call screen messager(contact_Lauren)
            label s19_reply22:
                $ contact_Lauren.newMessage("I could use some snuggles.")
                $ contact_Lauren.addReply("Aww, I'd love to get some snuggles. When can I see you again?", "s19_reply23")
                call screen messager(contact_Lauren)
            label s19_reply23:
                $ contact_Lauren.newMessage("I have a big test coming up but after that? I miss you")
                $ contact_Lauren.addReply("I miss you too. It's a date. Just let me know", "s19_reply24")
                call screen messager(contact_Lauren)
            label s19_reply24:
                $ contact_Lauren.newMessage("Goodnight")
                $ contact_Lauren.addReply("Goodnight", "s19_replyCont1")
                call screen messager(contact_Lauren)

        ### ERROR: -Continue after choices- [MC still in bed] ###
        label s19_replyCont1:
            if forgiveemily:
                # -MC's phone buzzes-
                ### ERROR: (Aww, she couldn't get enough of me) [I figure this line works for either scenario but let me know if I should change it] ###
                $ contact_Emily.newMessage("Hey, I was thinking")
                $ contact_Emily.addReply("Uh oh that can't be good ;)", "s19_reply25")
                call screen messager(contact_Emily)

                label s19_reply25:
                    $ contact_Emily.newMessage("Wanna meet up at the arcade?")

                if hcGirl == "emily":
                    $ contact_Emily.newMessage("I feel so bad about homecoming and want to make it up to you. My treat!")
                $ contact_Emily.addReply("Sure! Sounds like fun. I can be there in a few minutes", "s19_reply26")
                $ contact_Emily.addReply("I would but it's getting late and I haven't even started Mr. Lee's project", "s19_reply27")
                call screen messager(contact_Emily)

                label s19_reply26:
                    $ contact_Emily.newMessage("Great! See you there!")
                    call screen messager(contact_Emily)
                    jump emily_arcade

                label s19_reply27:
                    $ contact_Emily.newMessage("You sure you're not mad?")
                    $ contact_Emily.addReply("No, not at all. Just beat. I'd love to go some other time", "s19_reply28")
                    call screen messager(contact_Emily)
                label s19_reply28:
                    $ contact_Emily.newMessage("Okay talk to you soon")
                    $ contact_Emily.addReply("Goodnight", "s19_reply29")
                    call screen messager(contact_Emily)
                label s19_reply29:
                    scene v8sser1a # TPP. Same camera as v8sser1, show MC lying on his side as if to go to sleep.
                    with dissolve

                    u "(I think I'll get an early night)"

                    jump mon_morning_room

            else:
                scene v8sser1a
                with dissolve

                u "(I think I'll get an early night)"

                jump mon_morning_room

    else:
        scene v8sser4 # TPP. Show MC sat on his Apes bed on his phone.
        with fade

        if not laurenrs:
            play sound "sounds/vibrate.mp3"
            $ contact_Amber.newMessage("Hey u up?")
            $ contact_Amber.addReply("Always for you ;)", "s19_reply30")
            call screen messager(contact_Amber)
            label s19_reply30:
                $ contact_Amber.newMessage("That's what I was hoping to hear")
                $ contact_Amber.addReply("I can be even more up if you want...", "s19_reply31")
                call screen messager(contact_Amber)
            label s19_reply31:
                $ contact_Amber.newMessage("Really? Just like that?")
                $ contact_Amber.addReply("What can I say? You're hot", "s19_reply32")
                call screen messager(contact_Amber)
            label s19_reply32:
                $ contact_Amber.newMessage("You're pretty hot yourself and I'm... thinking about things")
                $ contact_Amber.addReply("What kind of things? Same things I'm thinking? ;)", "s19_reply33")
                call screen messager(contact_Amber)
            label s19_reply33:
                $ contact_Amber.newMessage("I think so")
                $ contact_Amber.addReply("Wanna see what thinking about you has done to me?", "s19_reply34")
                $ contact_Amber.addReply("I look at your pic all the time...when I'm thinking about things", "s19_reply47")
                call screen messager(contact_Amber)

            label s19_reply34:
                $ contact_Amber.newMessage("It's only fair, right? Make us even")
                # $ contact_Amber.newImgMessage(**[a_dick_pic]**, "s19_reply35")
                call screen messager(contact_Amber)
            label s19_reply35:
                $ contact_Amber.newMessage("Wow, better than I thought")
                $ contact_Amber.addReply("So you thought about it?", "s19_reply36")
                call screen messager(contact_Amber)
            label s19_reply36:
                $ contact_Amber.newMessage("Maybe")
                $ contact_Amber.addReply("Aw man you're driving me crazy", "s19_reply37")
                call screen messager(contact_Amber)
            label s19_reply37:
                $ contact_Amber.newMessage("So do something about it")
                $ contact_Amber.addReply("Now? What about you?", "s19_reply38")
                call screen messager(contact_Amber)
            label s19_reply38:
                # $ contact_Amber.newImgMessage(**[amb_pussy_pic]**)
                $ contact_Amber.addReply("Aw fuck", "s19_reply39")
                call screen messager(contact_Amber)
            label s19_reply39:
                $ contact_Amber.newMessage("You like?")
                $ contact_Amber.addReply("I love! You're so hot!", "s19_reply40")
                call screen messager(contact_Amber)
            label s19_reply40:
                $ contact_Amber.newMessage("What would you do if you were here?")
                $ contact_Amber.addReply("I would eat you until you couldn't take it anymore", "s19_reply41")
                call screen messager(contact_Amber)
            label s19_reply41:
                $ contact_Amber.newMessage("And then what?")
                $ contact_Amber.addReply("I'd fuck you so good you'd scream my name", "s19_reply42")
                call screen messager(contact_Amber)
            label s19_reply42:
                $ contact_Amber.newMessage("I'm close. Will you finish with me?")
                $ contact_Amber.addReply("Oh, God yes!")
                call screen messager(contact_Amber)
            label s19_reply43:
                scene v8sser5 # TPP. Show MC jerking off.
                with dissolve

                $ contact_Amber.newMessage("NOW!")
                $ contact_Amber.addReply("NOW!", "s19_reply44")
                call screen messager(contact_Amber)
            label s19_reply44:
                scene v8sser6 # TPP. Show MC finished jerking off.
                with dissolve

                $ contact_Amber.addReply("Holy shit, Amber! You're amazing!", "s19_reply45")
                call screen messager(contact_Amber)
            label s19_reply45:
                $ contact_Amber.newMessage("You weren't too bad yourself. Next time we need to do this in person")
                $ contact_Amber.addReply("Give me 5 minutes ;)", "s19_reply46")
                call screen messager(contact_Amber)
            label s19_reply46:
                $ contact_Amber.newMessage("You're so cute! But it's time for bed. Dream about me ;)")
                $ contact_Amber.addReply("With pleasure! Night!" , "s19_replyCont2") # replyCont2
                call screen messager(contact_Amber)


            label s19_reply47:
                $ contact_Amber.newMessage("Good. Maybe someday we can think about things in the same room and see what happens")
                $ contact_Amber.addReply("Please do", "s19_reply48")
                call screen messager(contact_Amber)
            label s19_reply48:
                $ contact_Amber.newMessage("I guess I better get back to studying. I keep getting distracted")
                $ contact_Amber.addReply("I'm not gonna be able to think of anything else now. I'm done studying", "s19_reply49")
                call screen messager(contact_Amber)
            label s19_reply49:
                $ contact_Amber.newMessage("Well, sleep tight then ;)")
                call screen messager(contact_Amber)
                jump s19_replyCont2

        else:
            # -MC's phone buzzes-
            $ contact_Lauren.newMessage("Hey, Sweetie, what are you up to?")
            $ contact_Lauren.addReply("Nothing, just catching up on some homework. You having a good night?", "s19_reply50")
            call screen messager(contact_Lauren)
            label s19_reply50:
                $ contact_Lauren.newMessage("It would be better if you were here...")
                $ contact_Lauren.addReply("Really?", "s19_reply51")
                call screen messager(contact_Lauren)
            label s19_reply51:
                $ contact_Lauren.newMessage("I could use some snuggles.")
                $ contact_Lauren.addReply("Aww, I'd love to get some snuggles. When can I see you again?", "s19_reply52")
                call screen messager(contact_Lauren)
            label s19_reply52:
                $ contact_Lauren.newMessage("I have a big test coming up but after that? I miss you")
                $ contact_Lauren.addReply("I miss you too. It's a date. Just let me know", "s19_reply53")
                call screen messager(contact_Lauren)
            label s19_reply53:
                $ contact_Lauren.newMessage("Goodnight")
                $ contact_Lauren.addReply("Goodnight", "s19_replyCont2")
                call screen messager(contact_Lauren)

        label s19_replyCont2:
            ### ERROR: -Continue after choices- [MC still in bed] ###
            if forgiveemily:
                # -MC's phone buzzes-
                ### ERROR: (Aww, she couldn't get enough of me) [I figure this line works for either scenario but let me know if I should change it] ###
                $ contact_Emily.newMessage("Hey, I was thinking")
                $ contact_Emily.addReply("Uh oh that can't be good ;)")
                call screen messager(contact_Emily)
                label s19_reply54:
                    $ contact_Emily.newMessage("Wanna meet up at the arcade?")

                if hcGirl == "emily":
                    $ contact_Emily.newMessage("I feel so bad about homecoming and want to make it up to you. My treat!")
                $ contact_Emily.addReply("Sure! Sounds like fun. I can be there in a few minutes", "s19_reply55")
                $ contact_Emily.addReply("I would but it's getting late and I haven't even started Mr. Lee's project", "s19_reply56")
                call screen messager(contact_Emily)

                # -Continue text with Emily-
                # -MC Can choose to accept the date or decline-
                # -If MC chooses to accept the date-
                label s19_reply55:
                    $ contact_Emily.newMessage("Great! See you there!")
                    call screen messager(contact_Emily)
                    jump emily_arcade

                label s19_reply56:
                    # -If MC chooses to decline the date-
                    $ contact_Emily.newMessage("You sure you're not mad?")
                    $ contact_Emily.addReply("No, not at all. Just beat. I'd love to go some other time", "s19_reply57")
                    call screen messager(contact_Emily)
                label s19_reply57:
                    $ contact_Emily.newMessage("Okay talk to you soon")
                    $ contact_Emily.addReply("Goodnight", "s19_reply58")
                    call screen messager(contact_Emily)
                label s19_reply58:
                    scene v8sser4a # TPP. Same camera as v8sser4, show MC lying on his side as if to go to sleep.
                    with dissolve

                    u "(I think I'll get an early night)"

                    jump mon_morning_room

            else:
                scene v8sser4a
                with dissolve

                u "(I think I'll get an early night)"

                jump mon_morning_room

label s19_phoneExit:
    if contact_Emily.messages[-1].replies or contact_Penelope.messages[-1].replies:
        jump sun_eve_room
    jump mon_morning_room