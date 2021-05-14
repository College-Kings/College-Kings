# Tue Evening in Room
# Locations: MC's room in Wolves house, MC's room in Apes house
# Characters: MC (outfit 2)
# Time: Tuesday Evening


label v8_tues_evening:
    stop music fadeout 2
    if joinwolves:
        scene v8ster1 # TPP. Show MC sat at his desk in his Wolves room, make sure MC's phone is visible on the desk. MC studying.
        with fade

        u "(I must be imagining things... Or maybe I should just text someone?)"

        scene v8ster2 # TPP. Show MC still sat at his desk but now on his phone.
        with dissolve

        if laurenrs:
            $ contact_Lauren.addReply("Still fine with drinking instead of making out with me?", "v8s37_phoneReply1")
            call screen messager(contact_Lauren)

            label v8s37_phoneReply1:
                $ contact_Lauren.newMessage("Of course, that drink was just my cup of tea. :)")
                $ contact_Lauren.addReply("Oh haha, is that so? I think it at least poured a bit of courage in there.", "v8s37_phoneReply2")
                call screen messager(contact_Lauren)

            label v8s37_phoneReply2:
                $ contact_Lauren.newMessage("Don't flatter yourself, witty cowboy. :)")
                $ contact_Lauren.addReply("You flatter me, ma'am.", "v8s37_phoneReply3")
                call screen messager(contact_Lauren)

            label v8s37_phoneReply3:
                $ contact_Lauren.newMessage("Miss you.")
                $ contact_Lauren.addReply("Kiss you*:)", "v8s37_phoneReply4")
                call screen messager(contact_Lauren)

            label v8s37_phoneReply4:
                $ contact_Lauren.newMessage(":)")
                call screen messager(contact_Lauren)

        else:
            $ contact_Lauren.addReply("Hey there, could you help me with studying?", "v8s37_phoneReply5")
            call screen messager(contact_Lauren)

            label v8s37_phoneReply5:
                $ contact_Lauren.newMessage("Umm, sure?")
                $ contact_Lauren.addReply("I'm puzzled just as much as I was back on that bench...", "v8s37_phoneReply6")
                call screen messager(contact_Lauren)

            label v8s37_phoneReply6:
                $ contact_Lauren.newMessage("You texted me just to make that reference, right?")
                $ contact_Lauren.addReply("Maybe?", "v8s37_phoneReply7")
                call screen messager(contact_Lauren)

            label v8s37_phoneReply7:
                $ contact_Lauren.newMessage("Seriously [name], I have things to do!")
                $ contact_Lauren.addReply("Later then.", "v8s37_phoneContinue1")
                call screen messager(contact_Lauren)

        label v8s37_phoneContinue1:
            if contact_Lauren.getReplies():
                u "I should reply to Lauren"
                jump v8s37_phoneContinue1

        if rileyrs:
            $ contact_Riley.addReply("If your legs were lies, you could call me a liar. For I would be gladly spreading them.", "v8s37_phoneReply8")
            call screen messager(contact_Riley)

            label v8s37_phoneReply8:
                $ contact_Riley.newMessage("That was the most corny, idiotic joke I've ever heard, Mr. Liar. :)")
                $ contact_Riley.addReply("Thinking of you makes it harder to study. And in some other places as well...", "v8s37_phoneReply9")
                call screen messager(contact_Riley)

            label v8s37_phoneReply9:
                $ contact_Riley.newMessage("I'll be the judge of that. :)")
                $ contact_Riley.addReply("Can't wait. :)", "v8s37_phoneContinue2")
                call screen messager(contact_Riley)

        else:
            $ contact_Riley.addReply("I have a serious question to ask you.", "v8s37_phoneReply10")
            call screen messager(contact_Riley)

            label v8s37_phoneReply10:
                $ contact_Riley.newMessage("What is it?")
                $ contact_Riley.addReply("You get to chose between options A and B.", "v8s37_phoneReply11")
                call screen messager(contact_Riley)

            label v8s37_phoneReply11:
                $ contact_Riley.newMessage("OK?")
                $ contact_Riley.addReply("Option A is to make out with Mr. Lee.", "v8s37_phoneReply12")
                call screen messager(contact_Riley)

            label v8s37_phoneReply12:
                $ contact_Riley.newMessage("B. I choose B. Option B.")
                $ contact_Riley.addReply("Haha", "v8s37_phoneReply13")
                call screen messager(contact_Riley)

            label v8s37_phoneReply13:
                $ contact_Riley.newMessage("*yuck*")
                call screen messager(contact_Riley)

        label v8s37_phoneContinue2:
            if contact_Riley.getReplies():
                u "I should reply to Riley"
                jump v8s37_phoneContinue1
            

        u "(I guess this is just not my day for studying. Great job, [name]!)"

        scene v8ster3 # TPP. Show MC placing his phone on the desk, MC looking bored.
        with dissolve

        u "(If only something interesting would happen...)"

        jump seb_in_room

    if not joinwolves:
        scene v8ster4 # TPP. Show MC sat at his desk in his Apes room, make sure MC's phone is visible on the desk. MC studying.
        with fade

        u "(I must be imagining things... Or maybe I should just text someone?)"

        scene v8ster5 # TPP. Show MC still sat at his desk but now on his phone.
        with dissolve

        if laurenrs:
            $ contact_Lauren.addReply("Still fine with drinking instead of making out with me?", "v8s37_phoneReply14")
            call screen messager(contact_Lauren)

            label v8s37_phoneReply14:
                $ contact_Lauren.newMessage("Of course, that drink was just my cup of tea. :)")
                $ contact_Lauren.addReply("Oh haha, is that so? I think it at least poured a bit of courage in there.", "v8s37_phoneReply15")
                call screen messager(contact_Lauren)

            label v8s37_phoneReply15:
                $ contact_Lauren.newMessage("Don't flatter yourself, witty cowboy. :)")
                $ contact_Lauren.addReply("You flatter me, ma'am.", "v8s37_phoneReply16")
                call screen messager(contact_Lauren)

            label v8s37_phoneReply16:
                $ contact_Lauren.newMessage("Miss you.")
                $ contact_Lauren.addReply("Kiss you*:)", "v8s37_phoneReply17")
                call screen messager(contact_Lauren)

            label v8s37_phoneReply17:
                $ contact_Lauren.newMessage(":)")
                call screen messager(contact_Lauren)

        else:
            $ contact_Lauren.addReply("Hey there, could you help me with studying?", "v8s37_phoneReply18")
            call screen messager(contact_Lauren)

            label v8s37_phoneReply18:
                $ contact_Lauren.newMessage("Umm, sure?")
                $ contact_Lauren.addReply("I'm puzzled just as much as I was back on that bench...", "v8s37_phoneReply19")
                call screen messager(contact_Lauren)

            label v8s37_phoneReply19:
                $ contact_Lauren.newMessage("You texted me just to make that reference, right?")
                $ contact_Lauren.addReply("Maybe?", "v8s37_phoneReply20")
                call screen messager(contact_Lauren)

            label v8s37_phoneReply20:
                $ contact_Lauren.newMessage("Seriously [name], I have things to do!")
                $ contact_Lauren.addReply("Later then.", "v8s37_phoneContinue3")
                call screen messager(contact_Lauren)

        label v8s37_phoneContinue3:
            if contact_Lauren.getReplies():
                u "I should reply to Lauren"
                jump v8s37_phoneContinue3

        if rileyrs:
            $ contact_Riley.addReply("If your legs were lies, you could call me a liar. For I would be gladly spreading them.", "v8s37_phoneReply21")
            call screen messager(contact_Riley)

            label v8s37_phoneReply21:
                $ contact_Riley.newMessage("That was the most corny, idiotic joke I've ever heard, Mr. Liar. :)")
                $ contact_Riley.addReply("Thinking of you makes it harder to study. And in some other places as well...", "v8s37_phoneReply22")
                call screen messager(contact_Riley)

            label v8s37_phoneReply22:
                $ contact_Riley.newMessage("I'll be the judge of that. :)")
                $ contact_Riley.addReply("Can't wait. :)", "v8s37_phoneContinue4")
                call screen messager(contact_Riley)

        else:
            $ contact_Riley.addReply("I have a serious question to ask you.", "v8s37_phoneReply23")

            label v8s37_phoneReply23:
                $ contact_Riley.newMessage("What is it?")
                $ contact_Riley.addReply("You get to chose between options A and B.", "v8s37_phoneReply24")
                call screen messager(contact_Riley)

            label v8s37_phoneReply24:
                $ contact_Riley.newMessage("OK?")
                $ contact_Riley.addReply("Option A is to make out with Mr. Lee.", "v8s37_phoneReply25")
                call screen messager(contact_Riley)

            label v8s37_phoneReply25:
                $ contact_Riley.newMessage("B. I choose B. Option B.")
                $ contact_Riley.addReply("Haha", "v8s37_phoneReply26")
                call screen messager(contact_Riley)

            label v8s37_phoneReply26:
                $ contact_Riley.newMessage("*yuck*")
                call screen messager(contact_Riley)

        label v8s37_phoneContinue4:
            if contact_Riley.getReplies():
                u "I should reply to my phone"
                jump v8s37_phoneContinue2
            

        u "(I guess this is just not my day for studying. Great job, [name]!)"

        scene v8ster6 # TPP. Show MC placing his phone on the desk, MC looking bored.
        with dissolve

        u "(If only something interesting would happen...)"

        jump gray_in_room
