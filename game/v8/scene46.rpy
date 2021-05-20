# Tuesday night in room
# Location: MC Apes Room, MC Wolves Room
# Outfits: MC Outfit 2
# Time: Tuesday Night

label v8_ending:
    if joinwolves:
        scene v8send1 # TPP. Show MC lying on his Wolves bed, looking tired.
        with fade

        u "(Man, what a crazy day!)"

        if climbwseb:
            u "(I can't believe Sebastian got me to climb that hospital. But I did it!)"

        if not climbwseb:
            u "(I hope Sebastian doesn't think less of me for chickening out at the hospital. Wasn't very Wolflike of me.)"

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

        $ contact_Imre.newMessage(_("Dude, you see this shit on Kiwii?"), queue=False)
        $ contact_Imre.addReply(_("No, what?"))
        $ contact_Imre.newMessage(_("IDK, it's crazy"))

        $ newKiwiiPost = KiwiiPost("Aubrey", "v8/red_square.webp", "[[image: red square]", numberLikes=renpy.random.randint(100, 200))
        # $ newKiwiiPost.addReply("???", numberLikes=999)
        # $ newKiwiiPost.addReply("What?", numberLikes=999)

        $ newKiwiiPost = KiwiiPost("Chris", "v8/red_square.webp", "[[image: red square]", numberLikes=renpy.random.randint(100, 200))
        # $ newKiwiiPost.addReply("Dude?", numberLikes=999)
        # $ newKiwiiPost.addReply("Wtf is going on? It's everywhere", numberLikes=999)

        $ newKiwiiPost = KiwiiPost("Grayson", "v8/red_square.webp", "[[image: red square]", numberLikes=renpy.random.randint(100, 200))
        # $ newKiwiiPost.addReply("Bout time!", numberLikes=999)
        # $ newKiwiiPost.addReply("Seriously?", numberLikes=999)

        scene v8send4 # TPP. Show MC, MC looks really confused.
        with dissolve

        u "(What the...?)"

        jump v8end

    if not joinwolves:
        scene v8send5 # TPP. Show MC lying on his Apes bed, looking tired.
        with dissolve

        u "(Man, what a crazy day!)"

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
        

        $ contact_Ryan.newMessage(_("What the hell's happening on Kiwii?"), queue=False)
        $ contact_Ryan.addReply(_("I don't know. What is it?"))
        $ contact_Ryan.newMessage(_("Fuckin check it out man. Crazy shit"))

        $ newKiwiiPost = KiwiiPost("Aubrey", "v8/red_square.webp", "[[image: red square]", numberLikes=renpy.random.randint(100, 200))
        # $ newKiwiiPost.addReply("???", numberLikes=999)
        # $ newKiwiiPost.addReply("What?", numberLikes=999)

        $ newKiwiiPost = KiwiiPost("Chris", "v8/red_square.webp", "[[image: red square]", numberLikes=renpy.random.randint(100, 200))
        # $ newKiwiiPost.addReply("Dude?", numberLikes=999)
        # $ newKiwiiPost.addReply("Wtf is going on? It's everywhere", numberLikes=999)

        $ newKiwiiPost = KiwiiPost("Grayson", "v8/red_square.webp", "[[image: red square]", numberLikes=renpy.random.randint(100, 200))
        # $ newKiwiiPost.addReply("Bout time!", numberLikes=999)
        # $ newKiwiiPost.addReply("Seriously?", numberLikes=999)

        call screen phone
        label v8s46_phoneCheck:
            if contact_Ryan.getReplies():
                u "I need to check my phone."
                jump v8s46_phoneCheck

        u "(What the...?)"

        scene v8send8 # TPP. Show MC, MC looks really confused.
        with dissolve

        jump v8end

label v8end:
    if persistent.ep < 9:
        scene savenow
        with Fade (1,0,1)
        " "

    if persistent.ep < 9:
        jump end_credits
    else:
        jump v9start
