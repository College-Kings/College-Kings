# Tuesday night in room
# Location: MC Apes Room, MC Wolves Room
# Outfits: MC Outfit 2
# Time: Tuesday Night

label v8_ending:
    if joinwolves:
        scene v8send1 # TPP. Show MC lying on his Wolves bed, looking tired.
        with dissolve

        u "(Man what a crazy day)"

        if climbwseb:
            u "(I can't believe Sebastian got me to climb that hospital. But I did it)"

        if not climbwseb:
            u "(I hope Sebastian doesn't think less of me for chickening out at the hospital. Wasn't very wolflike of me)"

        scene v8send2 # FPP. Show MC's phone on his bed, buzzing as if it has got a notification.
        with dissolve

        pause 0.5

        scene v8send1a # TPP. Same camera as v8send1, MC yawning.
        with dissolve

        pause 0.5

        scene v8send2
        with dissolve

        u "(What the...?)"

        scene v8send3 # TPP. Show MC sitting up and picking up his phone, confused expression.
        with dissolve

        pause 0.5

        scene v8send3a # TPP. Same camera as v8send3, MC checking his phone, looking confused.
        with dissolve

        $ contact_Imre.newMessage("Dude, you see this shit on Kiwii?")
        $ contact_MC,.addReply("No, what?")
        $ contact_Imre.newMessage("IDK, it's crazy")

        $ newKiwiiPost = KiwiiPost("Aubrey", **"IMAGE"**, "[image: red square]", **numberLikes=999**)
        $ contact_Penelope.addReply("???")
        $ contact_Riley.addReply("What?")

        $ newKiwiiPost = KiwiiPost("Chris", **"IMAGE"**, "[image:red square]", **numberLikes=999**)
        $ contact_Sebastian.addReply("Dude?")
        $ contact_Riley.addReply("Wtf is going on? It's everywhere")

        $ newKiwiiPost = KiwiiPost("Grayson", **"IMAGE"**, "[image: red square]", **numberLikes=999**)
        $ contact_Kai.addReply("Bout time!")
        $ contact_Chloe.addReply("Seriously?")

        scene v8send4 # TPP. Show MC, MC looks really confused.
        with dissolve

        u "(What the...?)"

        jump ending8

    if not joinwolves:
        scene v8send5 # TPP. Show MC lying on his Apes bed, looking tired.
        with dissolve

        u "(Man what a crazy day)"

        if not hesitantwgrayson:
            u "(Grayson and I really hit it off in the woods, though that was some creepy shit. I think I made some headway with him, though)"

        if hesitantwgrayson:
            u "(Grayson was acting strange in the woods. Wonder what that was all about)"

        scene v8send6 # FPP. Show MC's phone on his bed, buzzing as if it has got a notification.
        with dissolve

        pause 0.5

        scene v8send5a # TPP. Show MC lying on his Apes bed, looking tired.]
        with dissolve

        pause 0.5

        scene v8send6
        with dissolve

        u "(What the...?)"

        scene v8send7 # TPP. Show MC sitting up and picking up his phone, confused expression.
        with dissolve

        pause 0.5

        scene v8send7a # TPP. Same camera as v8send7, MC checking his phone, looking confused.
        with dissolve

        $ contact_Ryan.newMessage("What the hell's happening on Kiwii?")
        $ contact_MC.addReply("I don't know. What is it?")
        $ contact_Ryan.newMessage("Fuckin check it out man. Crazy shit")

        $ newKiwiiPost = KiwiiPost("Aubrey", **"IMAGE"**, "[image: red square]", **numberLikes=999**)
        $ contact_Penelope.addReply("???")
        $ contact_Riley.addReply("What?")

        $ newKiwiiPost = KiwiiPost("Chris", **"IMAGE"**, "[image:red square]", **numberLikes=999**)
        $ contact_Sebastian.addReply("Dude?")
        $ contact_Riley.addReply("Wtf is going on? It's everywhere")

        $ newKiwiiPost = KiwiiPost("Grayson", **"IMAGE"**, "[image: red square]", **numberLikes=999**)
        $ contact_Kai.addReply("Bout time!")
        $ contact_Chloe.addReply("Seriously?")

        u "(What the...?)"

        scene v8send8 # TPP. Show MC, MC looks really confused.
        with dissolve

        jump ending8

label ending8:

    if persistent.ep == 8:
        jump end8
    else:
        jump start9

label end8:
    scene savenow
    with Fade (1,0,1)
    " "
    if persistent.ep == 8:
        jump end_credits
    else:
        jump start9
