# Tue Evening in Room
# Locations: MC's room in Wolves house, MC's room in Apes house
# Characters: MC (outfit 2)
# Time: Tuesday Evening


label v8_tues_evening:
    if joinwolves:
        scene v8ster1 # TPP. Show MC sat at his desk in his Wolves room, make sure MC's phone is visible on the desk. MC studying.
        with fade

        u "(I must be imagining things... Or maybe I should just text someone?)"

        scene v8ster2 # TPP. Show MC still sat at his desk but now on his phone.
        with dissolve

        if laurenrs:
            $ contact_MC.newMessage("Still fine with drinking instead of making out with me?")
            $ contact_Lauren.addReply("Of course, that drink was just my cup of tea. :)")
            $ contact_MC.addReply("Oh haha, is that so? I think it at least poured a bit of courage in there.")
            $ contact_Lauren.addReply("Don't flatter yourself, witty cowboy. :)")
            $ contact_MC.addReply("You flatter me, ma'am.")
            $ contact_Lauren.addReply("Miss you.")
            $ contact_MC.addReply("Kiss you*:)")
            $ contact_Lauren.addReply(":)")

        if not laurenrs:
            $ contact_MC.newMessage("Hey there, could you help me with studying?")
            $ contact_Lauren.addReply("Umm, sure?")
            $ contact_MC.addReply("I'm puzzled just as much as I was back on that bench...")
            $ contact_Lauren.addReply("You texted me just to make that reference, right?")
            $ contact_MC.addReply("Maybe?")
            $ contact_Lauren.addReply("Seriously [name], I have things to do!")
            $ contact_MC.addReply("Later then.")

        if rileyrs:
            $ contact_MC.newMessage("If your legs were lies, you could call me a liar. For I would be gladly spreading them.")
            $ contact_Riley.addReply("That was the most corny, idiotic joke I've ever heard, Mr. Liar. :)")
            $ contact_MC.addReply("Thinking of you makes it harder to study. And in some other places as well...")
            $ contact_Riley.addReply("I'll be the judge of that. :)")
            $ contact_MC.addReply("Can't wait. :)")

        if not rileyrs:
            $ contact_MC.newMessage("I have a serious question to ask you.")
            $ contact_Riley.addReply("What is it?")
            $ contact_MC.addReply("You get to chose between options A and B.")
            $ contact_Riley.addReply("OK?")
            $ contact_MC.addReply("Option A is to make out with Mr. Lee.")
            $ contact_Riley.addReply("B. I choose B. Option B.")
            $ contact_MC.addReply("Haha")
            $ contact_Riley.addReply("*yuck*")

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
            $ contact_MC.newMessage("Still fine with drinking instead of making out with me?")
            $ contact_Lauren.addReply("Of course, that drink was just my cup of tea. :)")
            $ contact_MC.addReply("Oh haha, is that so? I think it at least poured a bit of courage in there.")
            $ contact_Lauren.addReply("Don't flatter yourself, witty cowboy. :)")
            $ contact_MC.addReply("You flatter me, ma'am.")
            $ contact_Lauren.addReply("Miss you.")
            $ contact_MC.addReply("Kiss you*:)")
            $ contact_Lauren.addReply(":)")

        if not laurenrs:
            $ contact_MC.newMessage("Hey there, could you help me with studying?")
            $ contact_Lauren.addReply("Umm, sure?")
            $ contact_MC.addReply("I'm puzzled just as much as I was back on that bench...")
            $ contact_Lauren.addReply("You texted me just to make that reference, right?")
            $ contact_MC.addReply("Maybe?")
            $ contact_Lauren.addReply("Seriously [name], I have things to do!")
            $ contact_MC.addReply("Later then.")

        if rileyrs:
            $ contact_MC.newMessage("If your legs were lies, you could call me a liar. For I would be gladly spreading them.")
            $ contact_Riley.addReply("That was the most corny, idiotic joke I've ever heard, Mr. Liar. :)")
            $ contact_MC.addReply("Thinking of you makes it harder to study. And in some other places as well...")
            $ contact_Riley.addReply("I'll be the judge of that. :)")
            $ contact_MC.addReply("Can't wait. :)")

        if not rileyrs:
            $ contact_MC.newMessage("I have a serious question to ask you.")
            $ contact_Riley.addReply("What is it?")
            $ contact_MC.addReply("You get to chose between options A and B.")
            $ contact_Riley.addReply("OK?")
            $ contact_MC.addReply("Option A is to make out with Mr. Lee.")
            $ contact_Riley.addReply("B. I choose B. Option B.")
            $ contact_MC.addReply("Haha")
            $ contact_Riley.addReply("*yuck*")

        u "(I guess this is just not my day for studying. Great job, [name]!)"

        scene v8ster6 # TPP. Show MC placing his phone on the desk, MC looking bored.
        with dissolve

        u "(If only something interesting would happen...)"

        jump gray_in_room
