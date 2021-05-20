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
            $ contact_Lauren.addReply(_("Still fine with drinking instead of making out with me?"))
            $ contact_Lauren.newMessage(_("Of course, that drink was just my cup of tea. :)"))
            $ contact_Lauren.addReply(_("Oh haha, is that so? I think it at least poured a bit of courage in there."))
            $ contact_Lauren.newMessage(_("Don't flatter yourself, witty cowboy. :)"))
            $ contact_Lauren.addReply(_("You flatter me, ma'am."))
            $ contact_Lauren.newMessage(_("Miss you."))
            $ contact_Lauren.addReply(_("Kiss you*:)"))
            $ contact_Lauren.newMessage(_(":)"))

        else:
            $ contact_Lauren.addReply(_("Hey there, could you help me with studying?"))
            $ contact_Lauren.newMessage(_("Umm, sure?"))
            $ contact_Lauren.addReply(_("I'm puzzled just as much as I was back on that bench..."))
            $ contact_Lauren.newMessage(_("You texted me just to make that reference, right?"))
            $ contact_Lauren.addReply(_("Maybe?"))
            $ contact_Lauren.newMessage(_("Seriously [name], I have things to do!"))
            $ contact_Lauren.addReply(_("Later then."))

        label v8s37_phoneContinue1:
            if contact_Lauren.getReplies():
                call screen phone
            if contact_Lauren.getReplies():
                u "I should reply to Lauren."
                jump v8s37_phoneContinue1

        if rileyrs:
            $ contact_Riley.addReply(_("If your legs were lies, you could call me a liar. For I would be gladly spreading them."))
            $ contact_Riley.newMessage(_("That was the most corny, idiotic joke I've ever heard, Mr. Liar. :)"))
            $ contact_Riley.addReply(_("Thinking of you makes it harder to study. And in some other places as well..."))
            $ contact_Riley.newMessage(_("I'll be the judge of that. :)"))
            $ contact_Riley.addReply(_("Can't wait. :)"))

        else:
            $ contact_Riley.addReply(_("I have a serious question to ask you."), "v8s37_phoneReply10")
            $ contact_Riley.newMessage(_("What is it?"))
            $ contact_Riley.addReply(_("You get to chose between options A and B."))
            $ contact_Riley.newMessage(_("OK?"))
            $ contact_Riley.addReply(_("Option A is to make out with Mr. Lee."))
            $ contact_Riley.newMessage(_("B. I choose B. Option B."))
            $ contact_Riley.addReply(_("Haha"))
            $ contact_Riley.newMessage(_("*yuck*"))

        label v8s37_phoneContinue2:
            if contact_Riley.getReplies():
                call screen phone
            if contact_Riley.getReplies():
                u "I should reply to Riley."
                jump v8s37_phoneContinue2

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
            $ contact_Lauren.addReply(_("Still fine with drinking instead of making out with me?"))
            $ contact_Lauren.newMessage(_("Of course, that drink was just my cup of tea. :)"))
            $ contact_Lauren.addReply(_("Oh haha, is that so? I think it at least poured a bit of courage in there."))
            $ contact_Lauren.newMessage(_("Don't flatter yourself, witty cowboy. :)"))
            $ contact_Lauren.addReply(_("You flatter me, ma'am."))
            $ contact_Lauren.newMessage(_("Miss you."))
            $ contact_Lauren.addReply(_("Kiss you*:)"))
            $ contact_Lauren.newMessage(_(":)"))

        else:
            $ contact_Lauren.addReply(_("Hey there, could you help me with studying?"))
            $ contact_Lauren.newMessage(_("Umm, sure?"))
            $ contact_Lauren.addReply(_("I'm puzzled just as much as I was back on that bench..."))
            $ contact_Lauren.newMessage(_("You texted me just to make that reference, right?"))
            $ contact_Lauren.addReply(_("Maybe?"))
            $ contact_Lauren.newMessage(_("Seriously [name], I have things to do!"))
            $ contact_Lauren.addReply(_("Later then."))

        label v8s37_phoneContinue3:
            if contact_Lauren.getReplies():
                call screen phone
            if contact_Lauren.getReplies():
                u "I should reply to Lauren."
                jump v8s37_phoneContinue3

        if rileyrs:
            $ contact_Riley.addReply(_("If your legs were lies, you could call me a liar. For I would be gladly spreading them."))
            $ contact_Riley.newMessage(_("That was the most corny, idiotic joke I've ever heard, Mr. Liar. :)"))
            $ contact_Riley.addReply(_("Thinking of you makes it harder to study. And in some other places as well..."))
            $ contact_Riley.newMessage(_("I'll be the judge of that. :)"))
            $ contact_Riley.addReply(_("Can't wait. :)"))

        else:
            $ contact_Riley.addReply(_("I have a serious question to ask you."))
            $ contact_Riley.newMessage(_("What is it?"))
            $ contact_Riley.addReply(_("You get to chose between options A and B."))
            $ contact_Riley.newMessage(_("OK?"))
            $ contact_Riley.addReply(_("Option A is to make out with Mr. Lee."))
            $ contact_Riley.newMessage(_("B. I choose B. Option B."))
            $ contact_Riley.addReply(_("Haha"))
            $ contact_Riley.newMessage(_("*yuck*"))

        label v8s37_phoneContinue4:
            if contact_Riley.getReplies():
                call screen phone
            if contact_Riley.getReplies():
                u "I should reply to my phone"
                jump v8s37_phoneContinue4
            
        u "(I guess this is just not my day for studying. Great job, [name]!)"

        scene v8ster6 # TPP. Show MC placing his phone on the desk, MC looking bored.
        with dissolve

        u "(If only something interesting would happen...)"

        jump gray_in_room
