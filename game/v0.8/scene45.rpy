# Tuesday night in room
# Location: MC Apes Room, MC Wolves Room
# Outfits: MC Outfit 2
# Time: Tuesday Night

label tue_night_in_room:
    if joinwolves:
        scene v8star1 # TPP. Show MC lying on his bed in his Wolves room staring at the ceiling.
        with fade

        u "(Things are getting pretty interesting, lately)"

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

        $ contact_Sebastian.newMessage("Yo dude, just wanted to let you know... tonight was fun.")
        $ contact_Sebastian.addReply("Sure was... but it can be even better, right?")
        $ contact_Sebastian.addReply("Sure can! You'll see what being a Wolf is all about.")
        $ contact_Sebastian.addReply("Looking forward to it. :)")

        u "(Let's just see what Chloe's up to)"

        if chloers:
            $ contact_Chloe.addReply("I'm thinking about you...")
            $ contact_Chloe.newMessage("Really?")
            $ contact_Chloe.addReply("Well, about the thing you do best, really.")
            $ contact_Chloe.newMessage("Mmmh, I can almost feel it in my mouth. :)")
            $ contact_Chloe.addReply("I think I'm gonna keep it all in for our next meeting. :)")
            $ contact_Chloe.newMessage("And now I'm hungry.")
            $ contact_Chloe.addReply(";D")

        if not chloers:
            $ contact_Chloe.addReply("I've had a really crazy night...")
            $ contact_Chloe.newMessage("And you chose me to tell about it? :)")
            $ contact_Chloe.addReply("Oh c'mon, you've got a great pair of eyes. :)")
            $ contact_Chloe.newMessage("Maybe some other time. These eyes need some rest atm.")
            $ contact_Chloe.addReply("Sure, later.")

        u "(Well I'll be damned... This could actually be more fun than I ever thought it could be.)"

        scene v8star1
        with dissolve

        pause 0.5

        jump v8_ending

    else:
        scene v8star10 # TPP. Show MC lying on his bed in his Apes room staring at the ceiling.
        with dissolve

        u "(Things are getting pretty interesting, lately)"

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

        $ contact_Grayson.newMessage("Yo Ape, still ready for the surprise?")
        $ contact_Grayson.addReply("Are we still doing this?")
        $ contact_Grayson.newMessage("It's just so damn tempting. But you won't regret it.")
        $ contact_Grayson.addReply("Now I'm fucking couting on it!")
        $ contact_Grayson.newMessage("Couting on it or not, [name], it's happening!")
        $ contact_Grayson.addReply(":P")

        u "(Let's just see what Chloe's up to)"

        if chloers:
            $ contact_Chloe.addReply("I'm thinking about you...")
            $ contact_Chloe.newMessage("Really?")
            $ contact_Chloe.addReply("Well, about the thing you do best, really.")
            $ contact_Chloe.newMessage("Mmmh, I can almost feel it in my mouth. :)")
            $ contact_Chloe.addReply("I think I'm gonna keep it all in for our next meeting. :)")
            $ contact_Chloe.newMessage("And now I'm hungry.")
            $ contact_Chloe.addReply(";D")

        if not chloers:
            $ contact_Chloe.addReply("I've had a really crazy night...")
            $ contact_Chloe.newMessage("And you chose me to tell about it? :)")
            $ contact_Chloe.addReply("Oh c'mon, you've got a great pair of eyes. :)")
            $ contact_Chloe.newMessage("Maybe some other time. These eyes need some rest atm.")
            $ contact_Chloe.addReply("Sure, later.")

        u "(Well I'll be damned... This could actually be more fun than I ever thought it could be.)"

        scene v8star10
        with dissolve

        pause 0.5

        jump v8_ending
