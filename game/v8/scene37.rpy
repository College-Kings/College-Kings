# Tue Evening in Room
# Locations: MC's room in Wolves house, MC's room in Apes house
# Characters: MC (outfit 2)
# Time: Tuesday Evening

label v8_tues_evening:
    stop music fadeout 3
    if joinwolves:
        scene v8ster1 # TPP. Show MC sat at his desk in his Wolves room, make sure MC's phone is visible on the desk. MC studying.
        with fade

        u "(I must be imagining things... Or maybe I should just text someone?)"

        scene v8ster2 # TPP. Show MC still sat at his desk but now on his phone.
        with dissolve

        if lauren.relationship >= Relationship.GIRLFRIEND:
            $ lauren.messenger.addReply(_("Still fine with drinking instead of making out with me?"))
            $ lauren.messenger.newMessage(_("Of course, that drink was just my cup of tea. :)"))
            $ lauren.messenger.addReply(_("Oh haha, is that so? I think it at least poured a bit of courage in there."))
            $ lauren.messenger.newMessage(_("Don't flatter yourself, witty cowboy. :)"))
            $ lauren.messenger.addReply(_("You flatter me, ma'am."))
            $ lauren.messenger.newMessage(_("Miss you."))
            $ lauren.messenger.addReply(_("Kiss you*:)"))
            $ lauren.messenger.newMessage(_(":)"))

        else:
            $ lauren.messenger.addReply(_("Hey there, could you help me with studying?"))
            $ lauren.messenger.newMessage(_("Umm, sure?"))
            $ lauren.messenger.addReply(_("I'm puzzled just as much as I was back on that bench..."))
            $ lauren.messenger.newMessage(_("You texted me just to make that reference, right?"))
            $ lauren.messenger.addReply(_("Maybe?"))
            $ lauren.messenger.newMessage(_("Seriously [name], I have things to do!"))
            $ lauren.messenger.addReply(_("Later then."))

        label v8s37_phoneContinue1:
            if lauren.messenger.replies:
                call screen phone
            if lauren.messenger.replies:
                u "I should reply to Lauren."
                jump v8s37_phoneContinue1

        if riley.relationship >= Relationship.FWB:
            $ riley.messenger.addReply(_("If your legs were lies, you could call me a liar. For I would be gladly spreading them."))
            $ riley.messenger.newMessage(_("That was the most corny, idiotic joke I've ever heard, Mr. Liar. :)"))
            $ riley.messenger.addReply(_("Thinking of you makes it harder to study. And in some other places as well..."))
            $ riley.messenger.newMessage(_("I'll be the judge of that. :)"))
            $ riley.messenger.addReply(_("Can't wait. :)"))

        else:
            $ riley.messenger.addReply(_("I have a serious question to ask you."))
            $ riley.messenger.newMessage(_("What is it?"))
            $ riley.messenger.addReply(_("You get to chose between options A and B."))
            $ riley.messenger.newMessage(_("OK?"))
            $ riley.messenger.addReply(_("Option A is to make out with Mr. Lee."))
            $ riley.messenger.newMessage(_("B. I choose B. Option B."))
            $ riley.messenger.addReply(_("Haha"))
            $ riley.messenger.newMessage(_("*yuck*"))

        label v8s37_phoneContinue2:
            if riley.messenger.replies:
                call screen phone
            if riley.messenger.replies:
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

        if lauren.relationship >= Relationship.GIRLFRIEND:
            $ lauren.messenger.addReply(_("Still fine with drinking instead of making out with me?"))
            $ lauren.messenger.newMessage(_("Of course, that drink was just my cup of tea. :)"))
            $ lauren.messenger.addReply(_("Oh haha, is that so? I think it at least poured a bit of courage in there."))
            $ lauren.messenger.newMessage(_("Don't flatter yourself, witty cowboy. :)"))
            $ lauren.messenger.addReply(_("You flatter me, ma'am."))
            $ lauren.messenger.newMessage(_("Miss you."))
            $ lauren.messenger.addReply(_("Kiss you*:)"))
            $ lauren.messenger.newMessage(_(":)"))

        else:
            $ lauren.messenger.addReply(_("Hey there, could you help me with studying?"))
            $ lauren.messenger.newMessage(_("Umm, sure?"))
            $ lauren.messenger.addReply(_("I'm puzzled just as much as I was back on that bench..."))
            $ lauren.messenger.newMessage(_("You texted me just to make that reference, right?"))
            $ lauren.messenger.addReply(_("Maybe?"))
            $ lauren.messenger.newMessage(_("Seriously [name], I have things to do!"))
            $ lauren.messenger.addReply(_("Later then."))

        label v8s37_phoneContinue3:
            if lauren.messenger.replies:
                call screen phone
            if lauren.messenger.replies:
                u "I should reply to Lauren."
                jump v8s37_phoneContinue3

        if riley.relationship >= Relationship.FWB:
            $ riley.messenger.addReply(_("If your legs were lies, you could call me a liar. For I would be gladly spreading them."))
            $ riley.messenger.newMessage(_("That was the most corny, idiotic joke I've ever heard, Mr. Liar. :)"))
            $ riley.messenger.addReply(_("Thinking of you makes it harder to study. And in some other places as well..."))
            $ riley.messenger.newMessage(_("I'll be the judge of that. :)"))
            $ riley.messenger.addReply(_("Can't wait. :)"))

        else:
            $ riley.messenger.addReply(_("I have a serious question to ask you."))
            $ riley.messenger.newMessage(_("What is it?"))
            $ riley.messenger.addReply(_("You get to chose between options A and B."))
            $ riley.messenger.newMessage(_("OK?"))
            $ riley.messenger.addReply(_("Option A is to make out with Mr. Lee."))
            $ riley.messenger.newMessage(_("B. I choose B. Option B."))
            $ riley.messenger.addReply(_("Haha"))
            $ riley.messenger.newMessage(_("*yuck*"))

        label v8s37_phoneContinue4:
            if riley.messenger.replies:
                call screen phone
            if riley.messenger.replies:
                u "I should reply to my phone."
                jump v8s37_phoneContinue4
            
        u "(I guess this is just not my day for studying. Great job, [name]!)"

        scene v8ster6 # TPP. Show MC placing his phone on the desk, MC looking bored.
        with dissolve

        u "(If only something interesting would happen...)"

        jump gray_in_room
