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

        $ sebastian.messenger.newMessage(_("Yo dude, just wanted to let you know... tonight was fun."), force_send=True)
        $ sebastian.messenger.addReply(_("Sure was... but it can be even better, right?"))
        $ sebastian.messenger.newMessage(_("Sure can! You'll see what being a Wolf is all about."))
        $ sebastian.messenger.addReply(_("Looking forward to it. :)"))

        label v8s45_phoneContinue1:
            if sebastian.messenger.replies:
                call screen phone
            if sebastian.messenger.replies:
                u "I should really check my phone."
                jump v8s45_phoneContinue1

        u "(Let's just see what Chloe's up to.)"

        if chloe.relationship >= Relationship.FWB:
            $ chloe.messenger.addReply(_("I'm thinking about you..."))
            $ chloe.messenger.newMessage(_("Really?"))
            $ chloe.messenger.addReply(_("Well, about the thing you do best, really."))
            $ chloe.messenger.newMessage(_("Mmmh, I can almost feel it in my mouth. :)"))
            $ chloe.messenger.addReply(_("I think I'm gonna keep it all in for our next meeting. :)"))
            $ chloe.messenger.newMessage(_("And now I'm hungry."))
            $ chloe.messenger.addReply(_(";D"))

        else:
            $ chloe.messenger.addReply(_("I've had a really crazy night..."))
            $ chloe.messenger.newMessage(_("And you chose me to tell about it? :)"))
            $ chloe.messenger.addReply(_("Oh c'mon, you've got a great pair of eyes. :)"))
            $ chloe.messenger.newMessage(_("Maybe some other time. These eyes need some rest atm."))
            $ chloe.messenger.addReply(_("Sure, later."))

        label v8s45_phoneContinue2:
            if chloe.messenger.replies:
                call screen phone
            if chloe.messenger.replies:
                u "I should really check my phone."
                jump v8s45_phoneContinue2

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

        $ grayson.messenger.newMessage(_("Yo Ape, still ready for the surprise?"), force_send=True)
        $ grayson.messenger.addReply(_("Are we still doing this?"))
        $ grayson.messenger.newMessage(_("It's just so damn tempting. But you won't regret it."))
        $ grayson.messenger.addReply(_("Now I'm fucking couting on it!"))
        $ grayson.messenger.newMessage(_("Couting on it or not, [name], it's happening!"))
        $ grayson.messenger.addReply(_(":P"))

        label v8s45_phoneCheck:
            if grayson.messenger.replies:
                call screen phone
            if grayson.messenger.replies:
                u "I need to check my phone."
                jump v8s45_phoneCheck

        u "(Let's just see what Chloe's up to.)"

        if chloe.relationship >= Relationship.FWB:
            $ chloe.messenger.addReply(_("I'm thinking about you..."))
            $ chloe.messenger.newMessage(_("Really?"))
            $ chloe.messenger.addReply(_("Well, about the thing you do best, really."))
            $ chloe.messenger.newMessage(_("Mmmh, I can almost feel it in my mouth. :)"))
            $ chloe.messenger.addReply(_("I think I'm gonna keep it all in for our next meeting. :)"))
            $ chloe.messenger.newMessage(_("And now I'm hungry."))
            $ chloe.messenger.addReply(_(";D"))

        else:
            $ chloe.messenger.addReply(_("I've had a really crazy night..."))
            $ chloe.messenger.newMessage(_("And you chose me to tell about it? :)"))
            $ chloe.messenger.addReply(_("Oh c'mon, you've got a great pair of eyes. :)"))
            $ chloe.messenger.newMessage(_("Maybe some other time. These eyes need some rest atm."))
            $ chloe.messenger.addReply(_("Sure, later."))

        label v8s45_phoneCheck2:
            if chloe.messenger.replies:
                call screen phone
            if chloe.messenger.replies:
                u "I need to check my phone."
                jump v8s45_phoneCheck2
        
        u "(Well I'll be damned... This could actually be more fun than I ever thought it could be.)"

        scene v8star10
        with dissolve

        pause 0.5

        jump v8_ending
