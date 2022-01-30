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

        $ imre.messenger.newMessage(_("Dude, you see this shit on Kiwii?"), force_send=True)
        $ imre.messenger.addReply(_("No, what?"))
        $ imre.messenger.newMessage(_("IDK, it's crazy"))

        $ newKiwiiPost = KiwiiPost(chris, "v8/red_square.webp", "", numberLikes=renpy.random.randint(100, 200))
        $ newKiwiiPost = KiwiiPost(grayson, "v8/red_square.webp", "", numberLikes=renpy.random.randint(100, 200))
        $ newKiwiiPost = KiwiiPost(aaron, "v8/red_square.webp", "", numberLikes=renpy.random.randint(100, 200))
        $ newKiwiiPost = KiwiiPost(cameron, "v8/red_square.webp", "", numberLikes=renpy.random.randint(100, 200))
        $ newKiwiiPost = KiwiiPost(aubrey, "v8/red_square.webp", "", numberLikes=renpy.random.randint(100, 200))
        $ newKiwiiPost = KiwiiPost(samantha, "v8/red_square.webp", "", numberLikes=renpy.random.randint(100, 200))
        
        scene v8send4 # TPP. Show MC, MC looks really confused.
        with dissolve

        u "(What the...? Is this about the upcoming fight?)"

        jump v8end

    else:
        scene v8send5 # TPP. Show MC lying on his Apes bed, looking tired.
        with dissolve

        u "(Man, what a crazy day!)"

        if not hesitantwgrayson:
            u "(Grayson and I really hit it off in the woods, though that was some creepy shit. I think I made some headway with him, though)"

        else:
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
        

        $ ryan.messenger.newMessage(_("What the hell's happening on Kiwii?"), force_send=True)
        $ ryan.messenger.addReply(_("I don't know. What is it?"))
        $ ryan.messenger.newMessage(_("Fuckin check it out man. Crazy shit"))

        $ newKiwiiPost = KiwiiPost(chris, "v8/red_square.webp", "", numberLikes=renpy.random.randint(100, 200))
        $ newKiwiiPost = KiwiiPost(grayson, "v8/red_square.webp", "", numberLikes=renpy.random.randint(100, 200))
        $ newKiwiiPost = KiwiiPost(aaron, "v8/red_square.webp", "", numberLikes=renpy.random.randint(100, 200))
        $ newKiwiiPost = KiwiiPost(cameron, "v8/red_square.webp", "", numberLikes=renpy.random.randint(100, 200))
        $ newKiwiiPost = KiwiiPost(aubrey, "v8/red_square.webp", "", numberLikes=renpy.random.randint(100, 200))
        $ newKiwiiPost = KiwiiPost(samantha, "v8/red_square.webp", "", numberLikes=renpy.random.randint(100, 200))

        label v8s46_phoneCheck:
            if ryan.messenger.replies:
                call screen phone
            if ryan.messenger.replies:
                u "I need to check my phone."
                jump v8s46_phoneCheck

        u "(What the...? Is this about the upcoming fight?)"

        scene v8send8 # TPP. Show MC, MC looks really confused.
        with dissolve

        jump v8end

label v8end:
    if not renpy.loadable("v9/scene01.rpy"):
        call screen save_now(9)
        with Fade(1, 0, 1)

    jump v9start
