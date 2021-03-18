# Sun Evening in Room
# Location: MC Wolves Room, MC Apes Room
# Outfits: MC Outfit 2
# Time: Sunday Evening

default s19_dickPic = False
default s19_dateEmily = False

label sun_eve_room:
    if joinwolves:
        scene v8sser1 # TPP. Show MC lying on his Wolves bed on his phone.
        with fade

        if not laurenrs:
            # -Phone buzzes-
            $ contact_Amber.newMessage("Hey u up?")
            $ contact_Amber.addReply("Always for you ;)")
            $ contact_Amber.newMessage("That's what I was hoping to hear")
            $ contact_Amber.addReply("I can be even more up if you want...")
            $ contact_Amber.newMessage("Really? Just like that?")
            $ contact_Amber.addReply("What can I say? You're hot")
            $ contact_Amber.newMessage("You're pretty hot yourself and I'm... thinking about things")
            $ contact_Amber.addReply("What kind of things? Same things I'm thinking? ;)")
            $ contact_Amber.newMessage("I think so")

            label s19_reply1:
                menu:
                    "Send Amber a dick picture":
                        $ s19_dickPic = True
                    "Don't send Amber a dick picture":
                        $ s19_dickPic = False
                
            if s19_dickPic:
                $ contact_Amber.addReply("Wanna see what thinking about you has done to me?")
                $ contact_Amber.newMessage("It's only fair, right? Make us even")
                # $ contact_Amber.ImgReply(**[w_dick_pic]**)
                $ contact_Amber.newMessage("Wow, better than I thought")
                $ contact_Amber.addReply("So you thought about it?")
                $ contact_Amber.newMessage("Maybe")
                $ contact_Amber.addReply("Aw man you're driving me crazy")
                $ contact_Amber.newMessage("So do something about it")
                $ contact_Amber.addReply("Now? What about you?")
                # $ contact_Amber.newImgMessage(**[amb_pussy_pic]**)
                $ contact_Amber.addReply("Aw fuck")
                $ contact_Amber.newMessage("You like?")
                $ contact_Amber.addReply("I love! You're so hot!")
                $ contact_Amber.newMessage("What would you do if you were here?")
                $ contact_Amber.addReply("I would eat you until you couldn't take it anymore")
                $ contact_Amber.newMessage("And then what?")
                $ contact_Amber.addReply("I'd fuck you so good you'd scream my name")
                $ contact_Amber.newMessage("I'm close. Will you finish with me?")
                $ contact_Amber.addReply("Oh, God yes!")

                scene v8sser2 # TPP. Show MC jerking off.
                with dissolve

                $ contact_Amber.newMessage("NOW!")
                $ contact_Amber.addReply("NOW!")

                scene v8sser2 # TPP. Show MC finished jerking off.
                with dissolve

                $ contact_Amber.addReply("Holy shit, Amber! You're amazing!")
                $ contact_Amber.newMessage("You weren't too bad yourself. Next time we need to do this in person")
                $ contact_Amber.addReply("Give me 5 minutes ;)")
                $ contact_Amber.newMessage("You're so cute! But it's time for bed. Dream about me ;)")
                $ contact_Amber.addReply("With pleasure! Night!")

            else:
                $ contact_Amber.addReply("I look at your pic all the time...when I'm thinking about things")
                $ contact_Amber.newMessage("Good. Maybe someday we can think about things in the same room and see what happens")
                $ contact_Amber.addReply("Please do")
                $ contact_Amber.newMessage("I guess I better get back to studying. I keep getting distracted")
                $ contact_Amber.addReply("I'm not gonna be able to think of anything else now. I'm done studying")
                $ contact_Amber.newMessage("Well, sleep tight then ;)")

        if laurenrs:
            # -MC's phone buzzes-
            $ contact_Lauren.newMessage("Hey, Sweetie, what are you up to?")
            $ contact_Lauren.addReply("Nothing, just catching up on some homework. You having a good night?")
            $ contact_Lauren.newMessage("It would be better if you were here...")
            $ contact_Lauren.addReply("Really?")
            $ contact_Lauren.newMessage("I could use some snuggles.")
            $ contact_Lauren.addReply("Aww, I'd love to get some snuggles. When can I see you again?")
            $ contact_Lauren.newMessage("I have a big test coming up but after that? I miss you")
            $ contact_Lauren.addReply("I miss you too. It's a date. Just let me know")
            $ contact_Lauren.newMessage("Goodnight")
            $ contact_Lauren.addReply("Goodnight")

        ### ERROR: -Continue after choices- [MC still in bed] ###
        if forgiveemily:
            # -MC's phone buzzes-
            ### ERROR: (Aww, she couldn't get enough of me) [I figure this line works for either scenario but let me know if I should change it] ###
            $ contact_Emily.newMessage("Hey, I was thinking")
            $ contact_Emily.addReply("Uh oh that can't be good ;)")
            $ contact_Emily.newMessage("Wanna meet up at the arcade?")

        if hcGirl == "emily":
            $ contact_Emily.newMessage("I feel so bad about homecoming and want to make it up to you. My treat!", "s19_reply2")

            label s19_reply2:
                menu:
                    "Go on a date with Emily":
                        $ s19_dateEmily = True
                    "Don't go on a date with Emily":
                        $ s19_dateEmily = False


            if s19_dateEmily:
                $ contact_Emily.addReply("Sure! Sounds like fun. I can be there in a few minutes")
                $ contact_Emily.newMessage("Great! See you there!")

                jump emily_arcade

            else:
                $ contact_Emily.addReply("I would but it's getting late and I haven't even started Mr. Lee's project")
                $ contact_Emily.newMessage("You sure you're not mad?")
                $ contact_Emily.addReply("No, not at all. Just beat. I'd love to go some other time")
                $ contact_Emily.newMessage("Okay talk to you soon")
                $ contact_Emily.addReply("Goodnight")

                scene v8sser1a # TPP. Same camera as v8sser1, show MC lying on his side as if to go to sleep.
                with dissolve

                u "(I think I'll get an early night)"

                jump mon_morning_room

        if not forgiveemily:
            scene v8sser1a
            with dissolve

            u "(I think I'll get an early night)"

            jump mon_morning_room

    else:
        scene v8sser4 # TPP. Show MC sat on his Apes bed on his phone.
        with fade

        if not laurenrs:
            # -Phone buzzes-
            $ contact_Amber.newMessage("Hey u up?")
            $ contact_Amber.addReply("Always for you ;)")
            $ contact_Amber.newMessage("That's what I was hoping to hear")
            $ contact_Amber.addReply("I can be even more up if you want...")
            $ contact_Amber.newMessage("Really? Just like that?")
            $ contact_Amber.addReply("What can I say? You're hot")
            $ contact_Amber.newMessage("You're pretty hot yourself and I'm... thinking about things")
            $ contact_Amber.addReply("What kind of things? Same things I'm thinking? ;)")
            $ contact_Amber.newMessage("I think so", "s19_reply3")

            label s19_reply3:
                menu:
                    "Send Amber a dick picture":
                        $ s19_dickPic = True
                    "Don't send Amber a dick picture":
                        $ s19_dickPic = False

            if s19_dickPic:
                $ contact_Amber.addReply("Wanna see what thinking about you has done to me?")
                $ contact_Amber.newMessage("It's only fair, right? Make us even")
                # $ contact_Amber.newImgMessage(**[a_dick_pic]**)
                $ contact_Amber.newMessage("Wow, better than I thought")
                $ contact_Amber.addReply("So you thought about it?")
                $ contact_Amber.newMessage("Maybe")
                $ contact_Amber.addReply("Aw man you're driving me crazy")
                $ contact_Amber.newMessage("So do something about it")
                $ contact_Amber.addReply("Now? What about you?")
                # $ contact_Amber.newImgMessage(**[amb_pussy_pic]**)
                $ contact_Amber.addReply("Aw fuck")
                $ contact_Amber.newMessage("You like?")
                $ contact_Amber.addReply("I love! You're so hot!")
                $ contact_Amber.newMessage("What would you do if you were here?")
                $ contact_Amber.addReply("I would eat you until you couldn't take it anymore")
                $ contact_Amber.newMessage("And then what?")
                $ contact_Amber.addReply("I'd fuck you so good you'd scream my name")
                $ contact_Amber.newMessage("I'm close. Will you finish with me?")
                $ contact_Amber.addReply("Oh, God yes!")

                scene v8sser5 # TPP. Show MC jerking off.
                with dissolve

                $ contact_Amber.newMessage("NOW!")
                $ contact_Amber.addReply("NOW!")

                scene v8sser6 # TPP. Show MC finished jerking off.
                with dissolve

                $ contact_Amber.addReply("Holy shit, Amber! You're amazing!")
                $ contact_Amber.newMessage("You weren't too bad yourself. Next time we need to do this in person")
                $ contact_Amber.addReply("Give me 5 minutes ;)")
                $ contact_Amber.newMessage("You're so cute! But it's time for bed. Dream about me ;)")
                $ contact_Amber.addReply("With pleasure! Night!")

            else:
                $ contact_Amber.addReply("I look at your pic all the time...when I'm thinking about things")
                $ contact_Amber.newMessage("Good. Maybe someday we can think about things in the same room and see what happens")
                $ contact_Amber.addReply("Please do")
                $ contact_Amber.newMessage("I guess I better get back to studying. I keep getting distracted")
                $ contact_Amber.addReply("I'm not gonna be able to think of anything else now. I'm done studying")
                $ contact_Amber.newMessage("Well, sleep tight then ;)")

        if laurenrs:
            # -MC's phone buzzes-
            $ contact_Lauren.newMessage("Hey, Sweetie, what are you up to?")
            $ contact_Lauren.addReply("Nothing, just catching up on some homework. You having a good night?")
            $ contact_Lauren.newMessage("It would be better if you were here...")
            $ contact_Lauren.addReply("Really?")
            $ contact_Lauren.newMessage("I could use some snuggles.")
            $ contact_Lauren.addReply("Aww, I'd love to get some snuggles. When can I see you again?")
            $ contact_Lauren.newMessage("I have a big test coming up but after that? I miss you")
            $ contact_Lauren.addReply("I miss you too. It's a date. Just let me know")
            $ contact_Lauren.newMessage("Goodnight")
            $ contact_Lauren.addReply("Goodnight")

        ### ERROR: -Continue after choices- [MC still in bed] ###
        if forgiveemily:
            # -MC's phone buzzes-
            ### ERROR: (Aww, she couldn't get enough of me) [I figure this line works for either scenario but let me know if I should change it] ###
            $ contact_Emily.newMessage("Hey, I was thinking")
            $ contact_Emily.addReply("Uh oh that can't be good ;)")
            $ contact_Emily.newMessage("Wanna meet up at the arcade?")

        if hcGirl == "emily":
            $ contact_Emily.newMessage("I feel so bad about homecoming and want to make it up to you. My treat!", "s19_reply4")

            label s19_reply4:
                menu:
                    "Go on a date with Emily":
                        $ s19_dateEmily = True
                    "Don't go on a date with Emily":
                        $ s19_dateEmily = False

            # -Continue text with Emily-
            # -MC Can choose to accept the date or decline-
            # -If MC chooses to accept the date-
            if s19_dateEmily:
                $ contact_Emily.addReply("Sure! Sounds like fun. I can be there in a few minutes")
                $ contact_Emily.newMessage("Great! See you there!")

                jump emily_arcade
            else:
                # -If MC chooses to decline the date-
                $ contact_Emily.addReply("I would but it's getting late and I haven't even started Mr. Lee's project")
                $ contact_Emily.newMessage("You sure you're not mad?")
                $ contact_Emily.addReply("No, not at all. Just beat. I'd love to go some other time")
                $ contact_Emily.newMessage("Okay talk to you soon")
                $ contact_Emily.addReply("Goodnight")

                scene v8sser4a # TPP. Same camera as v8sser4, show MC lying on his side as if to go to sleep.
                with dissolve

                u "(I think I'll get an early night)"

                jump mon_morning_room

        if not forgiveemily:
            scene v8sser4a
            with dissolve

            u "(I think I'll get an early night)"

            jump mon_morning_room
