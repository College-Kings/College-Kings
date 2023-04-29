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

        if CharacterService.is_girlfriend(lauren):
            $ MessengerService.add_reply(lauren, _("Still fine with drinking instead of making out with me?"))
            $ MessengerService.new_message(lauren, _("Of course, that drink was just my cup of tea. :)"))
            $ MessengerService.add_reply(lauren, _("Oh haha, is that so? I think it at least poured a bit of courage in there."))
            $ MessengerService.new_message(lauren, _("Don't flatter yourself, witty cowboy. :)"))
            $ MessengerService.add_reply(lauren, _("You flatter me, ma'am."))
            $ MessengerService.new_message(lauren, _("Miss you."))
            $ MessengerService.add_reply(lauren, _("Kiss you*:)"))
            $ MessengerService.new_message(lauren, _(":)"))

        else:
            $ MessengerService.add_reply(lauren, _("Hey there, could you help me with studying?"))
            $ MessengerService.new_message(lauren, _("Umm, sure?"))
            $ MessengerService.add_reply(lauren, _("I'm puzzled just as much as I was back on that bench..."))
            $ MessengerService.new_message(lauren, _("You texted me just to make that reference, right?"))
            $ MessengerService.add_reply(lauren, _("Maybe?"))
            $ MessengerService.new_message(lauren, _("Seriously [name], I have things to do!"))
            $ MessengerService.add_reply(lauren, _("Later then."))

        while MessengerService.has_replies(lauren):
            call screen phone
            if MessengerService.has_replies(lauren):
                u "I should reply to Lauren."

        if riley.relationship >= Relationship.FWB:
            $ MessengerService.add_reply(riley, _("If your legs were lies, you could call me a liar. For I would be gladly spreading them."))
            $ MessengerService.new_message(riley, _("That was the most corny, idiotic joke I've ever heard, Mr. Liar. :)"))
            $ MessengerService.add_reply(riley, _("Thinking of you makes it harder to study. And in some other places as well..."))
            $ MessengerService.new_message(riley, _("I'll be the judge of that. :)"))
            $ MessengerService.add_reply(riley, _("Can't wait. :)"))

        else:
            $ MessengerService.add_reply(riley, _("I have a serious question to ask you."))
            $ MessengerService.new_message(riley, _("What is it?"))
            $ MessengerService.add_reply(riley, _("You get to chose between options A and B."))
            $ MessengerService.new_message(riley, _("OK?"))
            $ MessengerService.add_reply(riley, _("Option A is to make out with Mr. Lee."))
            $ MessengerService.new_message(riley, _("B. I choose B. Option B."))
            $ MessengerService.add_reply(riley, _("Haha"))
            $ MessengerService.new_message(riley, _("*yuck*"))

        while MessengerService.has_replies(riley):
            call screen phone
            if MessengerService.has_replies(riley):
                u "I should reply to Riley."

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

        if CharacterService.is_girlfriend(lauren):
            $ MessengerService.add_reply(lauren, _("Still fine with drinking instead of making out with me?"))
            $ MessengerService.new_message(lauren, _("Of course, that drink was just my cup of tea. :)"))
            $ MessengerService.add_reply(lauren, _("Oh haha, is that so? I think it at least poured a bit of courage in there."))
            $ MessengerService.new_message(lauren, _("Don't flatter yourself, witty cowboy. :)"))
            $ MessengerService.add_reply(lauren, _("You flatter me, ma'am."))
            $ MessengerService.new_message(lauren, _("Miss you."))
            $ MessengerService.add_reply(lauren, _("Kiss you*:)"))
            $ MessengerService.new_message(lauren, _(":)"))

        else:
            $ MessengerService.add_reply(lauren, _("Hey there, could you help me with studying?"))
            $ MessengerService.new_message(lauren, _("Umm, sure?"))
            $ MessengerService.add_reply(lauren, _("I'm puzzled just as much as I was back on that bench..."))
            $ MessengerService.new_message(lauren, _("You texted me just to make that reference, right?"))
            $ MessengerService.add_reply(lauren, _("Maybe?"))
            $ MessengerService.new_message(lauren, _("Seriously [name], I have things to do!"))
            $ MessengerService.add_reply(lauren, _("Later then."))

        while MessengerService.has_replies(lauren):
            call screen phone
            if MessengerService.has_replies(lauren):
                u "I should reply to Lauren."

        if riley.relationship >= Relationship.FWB:
            $ MessengerService.add_reply(riley, _("If your legs were lies, you could call me a liar. For I would be gladly spreading them."))
            $ MessengerService.new_message(riley, _("That was the most corny, idiotic joke I've ever heard, Mr. Liar. :)"))
            $ MessengerService.add_reply(riley, _("Thinking of you makes it harder to study. And in some other places as well..."))
            $ MessengerService.new_message(riley, _("I'll be the judge of that. :)"))
            $ MessengerService.add_reply(riley, _("Can't wait. :)"))

        else:
            $ MessengerService.add_reply(riley, _("I have a serious question to ask you."))
            $ MessengerService.new_message(riley, _("What is it?"))
            $ MessengerService.add_reply(riley, _("You get to chose between options A and B."))
            $ MessengerService.new_message(riley, _("OK?"))
            $ MessengerService.add_reply(riley, _("Option A is to make out with Mr. Lee."))
            $ MessengerService.new_message(riley, _("B. I choose B. Option B."))
            $ MessengerService.add_reply(riley, _("Haha"))
            $ MessengerService.new_message(riley, _("*yuck*"))

        while MessengerService.has_replies(riley):
            call screen phone
            if MessengerService.has_replies(riley):
                u "I should reply to my phone."
            
        u "(I guess this is just not my day for studying. Great job, [name]!)"

        scene v8ster6 # TPP. Show MC placing his phone on the desk, MC looking bored.
        with dissolve

        u "(If only something interesting would happen...)"

        jump gray_in_room
