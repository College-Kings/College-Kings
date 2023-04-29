# Tuesday night in room
# Location: MC Apes Room, MC Wolves Room
# Outfits: MC Outfit 2
# Time: Tuesday Night

label tue_night_in_room:
    stop music fadeout 3
    if joinwolves:
        scene v8star1 # TPP. Show MC lying on his bed in his Wolves room staring at the ceiling.
        with fade

        u "(Things are getting pretty interesting, lately.)"

        scene v8star2 # TPP. Show MC getting up from his bed and walking over to the window.
        with dissolve

        pause 0.5

        scene v8star3 # FPP. Show a view from through the window as if MC is looking out.
        with dissolve

        u "(Especially tonight...)"

        scene v8star4 # FPP. Show MC's phone on the desk lighting up as if he's got a notification.
        with dissolve


        u "(Oh, it's Seb.)"

        scene v8star6 # TPP. Show MC sat on the edge of his bed checking his phone.
        with dissolve

        $ MessengerService.new_message(sebastian, _("Yo dude, just wanted to let you know... tonight was fun."))
        $ MessengerService.add_reply(sebastian, _("Sure was... but it can be even better, right?"))
        $ MessengerService.new_message(sebastian, _("Sure can! You'll see what being a Wolf is all about."))
        $ MessengerService.add_reply(sebastian, _("Looking forward to it. :)"))

        while MessengerService.has_replies(sebastian):
            call screen phone
            if MessengerService.has_replies(sebastian):
                u "I should really check my phone."

        u "(Let's just see what Chloe's up to.)"

        if CharacterService.is_fwb(chloe):
            $ MessengerService.add_reply(chloe, _("I'm thinking about you..."))
            $ MessengerService.new_message(chloe, _("Really?"))
            $ MessengerService.add_reply(chloe, _("Well, about the thing you do best, really."))
            $ MessengerService.new_message(chloe, _("Mmmh, I can almost feel it in my mouth. :)"))
            $ MessengerService.add_reply(chloe, _("I think I'm gonna keep it all in for our next meeting. :)"))
            $ MessengerService.new_message(chloe, _("And now I'm hungry."))
            $ MessengerService.add_reply(chloe, _(";D"))

        else:
            $ MessengerService.add_reply(chloe, _("I've had a really crazy night..."))
            $ MessengerService.new_message(chloe, _("And you chose me to tell about it? :)"))
            $ MessengerService.add_reply(chloe, _("Oh c'mon, you've got a great pair of eyes. :)"))
            $ MessengerService.new_message(chloe, _("Maybe some other time. These eyes need some rest atm."))
            $ MessengerService.add_reply(chloe, _("Sure, later."))

        while MessengerService.has_replies(chloe):
            call screen phone
            if MessengerService.has_replies(chloe):
                u "I should really check my phone."

        u "(Well I'll be damned... This could actually be more fun than I ever thought it could be.)"

        scene v8star1
        with dissolve

        pause 0.5

        jump v8_ending

    else:
        scene v8star10 # TPP. Show MC lying on his bed in his Apes room staring at the ceiling.
        with dissolve

        u "(Things are getting pretty interesting, lately.)"

        scene v8star11 # TPP. Show MC getting up from his bed and walking over to the window.
        with dissolve

        pause 0.5

        scene v8star12 # FPP. Show a view from through the window as if MC is looking out.
        with dissolve

        u "(Especially tonight...)"

        scene v8star13 # FPP. Show MC's phone on the desk lighting up as if he's got a notification.
        with dissolve

        u "(Grayson's texting me already? Haha...)"

        scene v8star15 # TPP. Show MC sat on the edge of his bed checking his phone.
        with dissolve

        $ MessengerService.new_message(grayson, _("Yo Ape, still ready for the surprise?"))
        $ MessengerService.add_reply(grayson, _("Are we still doing this?"))
        $ MessengerService.new_message(grayson, _("It's just so damn tempting. But you won't regret it."))
        $ MessengerService.add_reply(grayson, _("Now I'm fucking couting on it!"))
        $ MessengerService.new_message(grayson, _("Couting on it or not, [name], it's happening!"))
        $ MessengerService.add_reply(grayson, _(":P"))

        while MessengerService.has_replies(grayson):
            call screen phone
            if MessengerService.has_replies(grayson):
                u "I need to check my phone."

        u "(Let's just see what Chloe's up to.)"

        if CharacterService.is_fwb(chloe):
            $ MessengerService.add_reply(chloe, _("I'm thinking about you..."))
            $ MessengerService.new_message(chloe, _("Really?"))
            $ MessengerService.add_reply(chloe, _("Well, about the thing you do best, really."))
            $ MessengerService.new_message(chloe, _("Mmmh, I can almost feel it in my mouth. :)"))
            $ MessengerService.add_reply(chloe, _("I think I'm gonna keep it all in for our next meeting. :)"))
            $ MessengerService.new_message(chloe, _("And now I'm hungry."))
            $ MessengerService.add_reply(chloe, _(";D"))

        else:
            $ MessengerService.add_reply(chloe, _("I've had a really crazy night..."))
            $ MessengerService.new_message(chloe, _("And you chose me to tell about it? :)"))
            $ MessengerService.add_reply(chloe, _("Oh c'mon, you've got a great pair of eyes. :)"))
            $ MessengerService.new_message(chloe, _("Maybe some other time. These eyes need some rest atm."))
            $ MessengerService.add_reply(chloe, _("Sure, later."))

        while MessengerService.has_replies(chloe):
            call screen phone
            if MessengerService.has_replies(chloe):
                u "I need to check my phone."
        
        u "(Well I'll be damned... This could actually be more fun than I ever thought it could be.)"

        scene v8star10
        with dissolve

        pause 0.5

        jump v8_ending
