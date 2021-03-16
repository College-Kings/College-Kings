# Sun Evening in Room
# Location: MC Wolves Room, MC Apes Room
# Outfits: MC Outfit 2
# Time: Sunday Evening

label sun_eve_room:
    if joinwolves:
        scene v8sser1 # TPP. Show MC lying on his Wolves bed on his phone.
        with fade

        if not laurenrs:
            # -Phone buzzes-
            ### $ contact_Amber.newMessage("Hey u up?")
            ### $ contact_MC.addReply("Always for you ;)")
            ### $ contact_Amber.addReply("That's what I was hoping to hear")
            ### $ contact_MC.addReply("I can be even more up if you want...")
            ### $ contact_Amber.addReply("Really? Just like that?")
            ### $ contact_MC.addReply("What can I say? You're hot")
            ### $ contact_Amber.addReply("You're pretty hot yourself and I'm... thinking about things")
            ### $ contact_MC.addReply("What kind of things? Same things I'm thinking? ;)")
            ### $ contact_Amber.addReply("I think so")

            # -MC can choose between Sending a dick pic or not-
            # -If MC chooses to send a dick pic-
            ### $ contact_Wanna.addReply("see what thinking about you has done to me?")
            ### $ contact_Amber.addReply("It's only fair, right? Make us even")
            ### $ contact_MC.newImgMessage(**[w_dick_pic]**)
            ### $ contact_Amber.addReply("Wow, better than I thought")
            ### $ contact_MC.addReply("So you thought about it?")
            ### $ contact_Amber.addReply("Maybe")
            ### $ contact_MC.addReply("Aw man you're driving me crazy")
            ### $ contact_Amber.addReply("So do something about it")
            ### $ contact_MC.addReply("Now? What about you?")
            ### $ contact_Amber.newImgMessage(**[amb_pussy_pic]**)
            ### $ contact_MC.addReply("Aw fuck")
            ### $ contact_Amber.addReply("You like?")
            ### $ contact_MC.addReply("I love! You're so hot!")
            ### $ contact_Amber.addReply("What would you do if you were here?")
            ### $ contact_MC.addReply("I would eat you until you couldn't take it anymore")
            ### $ contact_Amber.addReply("And then what?")
            ### $ contact_MC.addReply("I'd fuck you so good you'd scream my name")
            ### $ contact_Amber.addReply("I'm close. Will you finish with me?")
            ### $ contact_MC.addReply("Oh, God yes!")

            scene v8sser2 # TPP. Show MC jerking off.
            with dissolve

            ### $ contact_Amber.addReply("NOW!")
            ### $ contact_MC.addReply("NOW!")

            scene v8sser2 # TPP. Show MC finished jerking off.
            with dissolve

            ### $ contact_MC.addReply("Holy shit, Amber! You're amazing!")
            ### $ contact_Amber.addReply("You weren't too bad yourself. Next time we need to do this in person")
            ### $ contact_MC.addReply("Give me 5 minutes ;)")
            ### $ contact_Amber.addReply("You're so cute! But it's time for bed. Dream about me ;)")
            ### $ contact_MC.addReply("With pleasure! Night!")

            # -If MC chooses not to send a dick pic-
            ### $ contact_I.addReply("look at your pic all the time...when I'm thinking about things")
            ### $ contact_Amber.addReply("Good. Maybe someday we can think about things in the same room and see what happens")
            ### $ contact_MC.addReply("Please do")
            ### $ contact_Amber.addReply("I guess I better get back to studying. I keep getting distracted")
            ### $ contact_MC.addReply("I'm not gonna be able to think of anything else now. I'm done studying")
            ### $ contact_Amber.addReply("Well, sleep tight then ;)")

        if laurenrs:
            # -MC's phone buzzes-
            ### $ contact_Lauren.newMessage("Hey, Sweetie, what are you up to?")
            ### $ contact_MC.addReply("Nothing, just catching up on some homework. You having a good night?")
            ### $ contact_Lauren.addReply("It would be better if you were here...")
            ### $ contact_MC.addReply("Really?")
            ### $ contact_Lauren.addReply("I could use some snuggles.")
            ### $ contact_MC.addReply("Aww, I'd love to get some snuggles. When can I see you again?")
            ### $ contact_Lauren.addReply("I have a big test coming up but after that? I miss you")
            ### $ contact_MC.addReply("I miss you too. It's a date. Just let me know")
            ### $ contact_Lauren.addReply("Goodnight")
            ### $ contact_MC.addReply("Goodnight")

        ### ERROR: -Continue after choices- [MC still in bed] ###
        if forgiveemily:
            # -MC's phone buzzes-
            ### ERROR: (Aww, she couldn't get enough of me) [I figure this line works for either scenario but let me know if I should change it] ###
            ### $ contact_Emily.newMessage("Hey, I was thinking")
            ### $ contact_MC.addReply("Uh oh that can't be good ;)")
            ### $ contact_Emily.newMessage("Wanna meet up at the arcade?")

        ### ERROR: -If MC went to hoco with Emily- [only this one extra line from her on if on the hoco path] ###
        ### $ contact_Emily.newMessage("I feel so bad about homecoming and want to make it up to you. My treat!")

            # -Continue text with Emily-
            # -MC Can choose to accept the date or decline-
            # -If MC chooses to accept the date-
            ### $ contact_Sure!.addReply("Sounds like fun. I can be there in a few minutes")
            ### $ contact_Emily.addReply("Great! See you there!")

            # -If MC chooses to decline the date-
            ### $ contact_I.addReply("would but it's getting late and I haven't even started Mr. Lee's project")
            ### $ contact_Emily.addReply("You sure you're not mad?")
            ### $ contact_MC.addReply("No, not at all. Just beat. I'd love to go some other time")
            ### $ contact_Emily.addReply("Okay talk to you soon")
            ### $ contact_MC.addReply("Goodnight")

        if not forgiveemily:
            # -MC studies until it turns dark-

    else:
        scene v8sser4 # TPP. Show MC sat on his Apes bed on his phone.
        with fade

        if not laurenrs:
            # -Phone buzzes-
            ### $ contact_Amber.newMessage("Hey u up?")
            ### $ contact_MC.addReply("Always for you ;)")
            ### $ contact_Amber.addReply("That's what I was hoping to hear")
            ### $ contact_MC.addReply("I can be even more up if you want...")
            ### $ contact_Amber.addReply("Really? Just like that?")
            ### $ contact_MC.addReply("What can I say? You're hot")
            ### $ contact_Amber.addReply("You're pretty hot yourself and I'm... thinking about things")
            ### $ contact_MC.addReply("What kind of things? Same things I'm thinking? ;)")
            ### $ contact_Amber.addReply("I think so")

            # -MC can choose between Sending a dick pic or not-
            # -If MC chooses to send a dick pic-
            ### $ contact_Wanna.addReply("see what thinking about you has done to me?")
            ### $ contact_Amber.addReply("It's only fair, right? Make us even")
            ### $ contact_MC.newImgMessage(**[a_dick_pic]**)
            ### $ contact_Amber.addReply("Wow, better than I thought")
            ### $ contact_MC.addReply("So you thought about it?")
            ### $ contact_Amber.addReply("Maybe")
            ### $ contact_MC.addReply("Aw man you're driving me crazy")
            ### $ contact_Amber.addReply("So do something about it")
            ### $ contact_MC.addReply("Now? What about you?")
            ### $ contact_Amber.newImgMessage(**[amb_pussy_pic]**)
            ### $ contact_MC.addReply("Aw fuck")
            ### $ contact_Amber.addReply("You like?")
            ### $ contact_MC.addReply("I love! You're so hot!")
            ### $ contact_Amber.addReply("What would you do if you were here?")
            ### $ contact_MC.addReply("I would eat you until you couldn't take it anymore")
            ### $ contact_Amber.addReply("And then what?")
            ### $ contact_MC.addReply("I'd fuck you so good you'd scream my name")
            ### $ contact_Amber.addReply("I'm close. Will you finish with me?")
            ### $ contact_MC.addReply("Oh, God yes!")

            scene v8sser5 # TPP. Show MC jerking off.
            with dissolve

            ### $ contact_Amber.addReply("NOW!")
            ### $ contact_MC.addReply("NOW!")

            scene v8sser6 # TPP. Show MC finished jerking off.
            with dissolve

            ### $ contact_MC.addReply("Holy shit, Amber! You're amazing!")
            ### $ contact_Amber.addReply("You weren't too bad yourself. Next time we need to do this in person")
            ### $ contact_MC.addReply("Give me 5 minutes ;)")
            ### $ contact_Amber.addReply("You're so cute! But it's time for bed. Dream about me ;)")
            ### $ contact_MC.addReply("With pleasure! Night!")

            # -If MC chooses not to send a dick pic-
            ### $ contact_I.addReply("look at your pic all the time...when I'm thinking about things")
            ### $ contact_Amber.addReply("Good. Maybe someday we can think about things in the same room and see what happens")
            ### $ contact_MC.addReply("Please do")
            ### $ contact_Amber.addReply("I guess I better get back to studying. I keep getting distracted")
            ### $ contact_MC.addReply("I'm not gonna be able to think of anything else now. I'm done studying")
            ### $ contact_Amber.addReply("Well, sleep tight then ;)")

        if laurenrs:
            # -MC's phone buzzes-
            ### $ contact_Lauren.newMessage("Hey, Sweetie, what are you up to?")
            ### $ contact_MC.addReply("Nothing, just catching up on some homework. You having a good night?")
            ### $ contact_Lauren.addReply("It would be better if you were here...")
            ### $ contact_MC.addReply("Really?")
            ### $ contact_Lauren.addReply("I could use some snuggles.")
            ### $ contact_MC.addReply("Aww, I'd love to get some snuggles. When can I see you again?")
            ### $ contact_Lauren.addReply("I have a big test coming up but after that? I miss you")
            ### $ contact_MC.addReply("I miss you too. It's a date. Just let me know")
            ### $ contact_Lauren.addReply("Goodnight")
            ### $ contact_MC.addReply("Goodnight")

        ### ERROR: -Continue after choices- [MC still in bed] ###
        if forgiveemily:
            # -MC's phone buzzes-
            ### ERROR: (Aww, she couldn't get enough of me) [I figure this line works for either scenario but let me know if I should change it] ###
            ### $ contact_Emily.newMessage("Hey, I was thinking")
            ### $ contact_MC.addReply("Uh oh that can't be good ;)")
            ### $ contact_Emily.newMessage("Wanna meet up at the arcade?")

        ### ERROR: -If MC went to hoco with Emily- [only this one extra line from her on if on the hoco path] ###
        ### $ contact_Emily.newMessage("I feel so bad about homecoming and want to make it up to you. My treat!")

            # -Continue text with Emily-
            # -MC Can choose to accept the date or decline-
            # -If MC chooses to accept the date-
            ### $ contact_Sure!.addReply("Sounds like fun. I can be there in a few minutes")
            ### $ contact_Emily.addReply("Great! See you there!")

            # -If MC chooses to decline the date-
            ### $ contact_I.addReply("would but it's getting late and I haven't even started Mr. Lee's project")
            ### $ contact_Emily.addReply("You sure you're not mad?")
            ### $ contact_MC.addReply("No, not at all. Just beat. I'd love to go some other time")
            ### $ contact_Emily.addReply("Okay talk to you soon")
            ### $ contact_MC.addReply("Goodnight")

        if not forgiveemily:
            # -MC studies until it turns dark-
