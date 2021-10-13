# SCENE 30b: Looking at the pictures together with Chloe
# Locations: Campus, Wolves/Apes room.
# Characters: CHLOE (Outfit: 1), MC (Outfit: 2)
# Time: Afternoon


label v14s30b:
    scene v14s30b_1 # TPP. Show MC and Chloe walking on the Campus sidewalk, Both slight smile, mouth closed.
    with fade

    pause .25

    scene v14s30b_2 # FPP. MC looking at Chloe, Chloe looking down at her phone, Chloe slight smile, mouth open.
    with dissolve

    cl "Alright… Let’s get a good look at these."

    scene v14s30b_2a # FPP. Same as v14s30b_2, Chloe slight smile, mouth closed.
    with dissolve

    u "Do you like what you see so far?"

    scene v14s30b_2
    with dissolve

    cl "I do. I also think this helps the campaign a lot."

    cl "Of the two frats, the Wolves are way more respected than the Apes and so…"

    cl "Just strategically speaking, this helps a lot."

    scene v14s30b_2a
    with dissolve

    u "That's what I like to hear."

    scene v14s30b_2
    with dissolve

    cl "My posing definitely isn't as good as Aubrey's though. *Chuckles*"

    scene v14s30b_2a
    with dissolve

    u "So you know about Lew’s and all that?"

    scene v14s30b_2
    with dissolve

    cl "Haha, I know more about Aubrey than most."

    scene v14s30b_2a
    with dissolve

    u "*Chuckles* She is your VP."

    scene v14s30b_2
    with dissolve

    cl "Exactly, and hopefully she chooses to stay on after we win."

    scene v14s30b_2a
    with dissolve

    u "I'm sure she will."

    scene v14s30b_2
    with dissolve

    cl "Ha, glad you think so. Now..."

    if v14_pw_half_chris_support or v14_low_chris_support:

        cl "I'm not sure how these will be perceived and all you know? With us having a fake wolf, but I still think the pictures are really good."

        scene v14s30b_3 # FPP. MC looking at the phone showing the first image, Chloe standing next to the plush wolf, smiling proudly with her hand on her hip. (Possible leave the phone screen blank and photoshop the scene from the photoshoot onto the phone :D )
        with dissolve

        pause

        scene v14s30b_3a # FPP. Same as v14s30b_3, The second image now on the phone, The photo of Chloe holding the plush wolf in one arm and her other hand in the air like she is chairing. (Like the other scene may be possible to edit that scene onto the phone in photoshop :D )
        with dissolve

        cl "Which one is your favorite?"

        menu:
            "Chloe standing next to the plush wolf...":
                $ v14s30b_pw_image_one = True

                scene v14s30b_3
                with dissolve

            "Chloe holding plush wolf and cheering...":
                $ v14s30b_pw_image_two = True

                scene v14s30b_3a 
                with dissolve
            
        u "That one."

        scene v14s30b_2
        with dissolve

        cl "Good call, *Chuckles*. I'm gonna post that one on Kiwii."

    if v14_full_chris_support or v14_rw_half_chris_support:
     
        cl "I know the entire school is gonna be off the wall about these photos, haha."

        scene v14s30b_3b # FPP. Same as v14s30b_3a, First image of real wolf photoshoot, Chloe standing next to wolf smiling, one hand on hip, one on wolf's head on the phone screen.
        with dissolve

        pause 

        scene v14s30b_3c # FPP. Same as v14s30b_3b, Second Image of the real wolf photoshoot, Chloe giving the real wolf a high five photo on the phone screen.
        with dissolve

        cl "Which one is your favorite?"

        menu:
            "Chloe standing next to the real wolf...":
                $ v14s30b_rw_image_one = True

                scene v14s30b_3b
                with dissolve
            "Chloe high fiving the real wolf...":
                $ v14s30b_rw_image_two = True

                scene v14s30b_3c
                with dissolve
            
        u "That one."

        scene v14s30b_2
        with dissolve


        cl "Good call, *Chuckles*. I'm gonna post that one on Kiwii."

    scene v14s30b_2a
    with dissolve

    u "What about your caption?"

    scene v14s30b_2
    with dissolve

    cl "Well, I’ll definitely include “#PresidentialStatus”."

    menu:
        "It's perfect...":
            $ v14s30b_its_perfect = True
            $ LindseyPopularity += 3

            scene v14s30b_2a
            with dissolve

            u "Yeah, that’s perfect. Standing tall and proud with a short and sweet caption."

            scene v14s30b_2
            with dissolve

            cl "*Chuckles* Exactly."

        "What about something else?":
            $ LindseyPopularity -= 3

            scene v14s30b_2a
            with dissolve

            u "What about something else?"

            scene v14s30b_2
            with dissolve

            cl "Something else?"

            scene v14s30b_2a
            with dissolve

            u "Well, yeah. Like something about the Chicks and the Wolves."

            scene v14s30b_2
            with dissolve

            cl "I guess that makes sense considering it’s an alliance announcement, as well as a good pic for my feed, haha."

            scene v14s30b_2a
            with dissolve

            u "Exactly, so maybe something like, “#TheChicksWhoCriedWolves”."

            scene v14s30b_2
            with dissolve

            cl "You’re right! That’s perfect, [name]."

            scene v14s30b_2a
            with dissolve

            u "*Laughs* You’re welcome."

    scene v14s30b_4 # FPP. Chloe looking at MC, MC looking at Chloe, Chloe slight smile, mouth open.
    with dissolve

    cl "Well, this has been a lot better than I had imagined. I'm off to get it all set in stone."

    cl "Thanks again for everything."

    scene v14s30b_4a # FPP. Same as v14s30b_4a, Chloe slight smile, mouth closed.
    with dissolve

    u "Of course! I’ll be on the lookout for your big announcement."

    scene v14s30b_4
    with dissolve

    cl "*Chuckles*"

    if chloegf:
        play sound "sounds/kiss.mp3"
        scene v14s30b_5 # FPP. Chloe kissing MC.
        with dissolve

    scene v14s30b_6 # FPP. Show Chloe running off away from MC.
    with dissolve

    pause .25

    scene v14s30b_7 # TPP. Show MC walking down the Campus sidewalk.
    with dissolve

    if joinwolves:
        scene v14s30b_8 # TPP. Show MC walking into the wolves house.
        with fade

        pause .5

        play sound "sounds/doorclose.mp3"

        scene v14s30b_9 # TPP. MC sitting on his bed in the Wolves room, slight smile, mouth closed.
        with dissolve
    if joinapes:
        scene v14s30b_10 # TPP. Show MC walking into the Apes house.
        with fade

        pause .5

        play sound "sounds/doorclose.mp3"

        scene v14s30b_11 # TPP. Show MC sitting on his bed in the Apes room, slight smile, mouth closed.

    if v14s30b_pw_image_one and v14s30b_its_perfect:
        $ kiwii_post = KiwiiPost("Chloe", In the woods Chloe standing next to the plush wolf, smiling proudly with her hand on her hip, _("What’s a chick without her wolf? <3 #PresidentialStatus #Vote4ChloeVote4Wolves"), numberLikes=712)
        if v14_pw_half_chris_support:
            $ kiwii_post.newComment("Chris", _("Haha, perfect! #Vote4Chloe"))
        $ kiwii_post.newComment("Aubrey", _("Aww! Hell yeah! This is so cute, Chlo <3"))
        $ kiwii_post.newComment("Imre", _("Yessss!!!!!"))
        $ kiwii_post.newComment("Grayson", _("LMAO you’re down bad, huh?"))
        $ kiwii_post.newComment("Chloe", _("Be civil at least, Grayson"), mentions="Grayson")
        $ kiwii_post.newComment("Riley", _("Omg! Can I have that thing?"))
        $ kiwii_post.addReply(_("These turned out perfect! #Vote4Chloe"))
        $ kiwii_post.addReply(_("Aww, haha. Congrats!"))

    if v14s30b_pw_image_one and not v14s30b_its_perfect:
        $ kiwii_post = KiwiiPost("Chloe", In the woods Chloe standing next to the plush wolf, smiling proudly with her hand on her hip, _("It’s official! The Wolves and The Chicks are uniting as one to ensure that I stay president and furthermore, bring a wonderful balance to our new and improved sorority. #TheChicksWhoCriedWolves #Vote4ChloeVote4Wolves"), numberLikes=812)
        if v14_pw_half_chris_support:
            $ kiwii_post.newComment("Chris", _("Haha, perfect! #Vote4Chloe"))
        $ kiwii_post.newComment("Aubrey", _("Aww! Hell yeah! This is so cute, Chlo <3"))
        $ kiwii_post.newComment("Imre", _("Yessss!!!!!"))
        $ kiwii_post.newComment("Grayson", _("LMAO you’re down bad, huh?"))
        $ kiwii_post.newComment("Chloe", _("Be civil at least, Grayson"), mentions="Grayson")
        $ kiwii_post.newComment("Riley", _("Omg! Can I have that thing?"))
        $ kiwii_post.addReply(_("These turned out perfect! #Vote4Chloe"))
        $ kiwii_post.addReply(_("Aww, haha. Congrats!"))

    if v14s30b_pw_image_two and v14s30b_its_perfect:
        $ kiwii_post = KiwiiPost("Chloe", In the woods Chloe smiling mouth slightly open holding the plush wolf and one hand in the air like she’s cheering, _("I’d like to officially announce The Chick’s partnership with The Wolves! <3 #PresidentialStatus #Vote4ChloeVote4Wolves"), numberLikes=756)
        if v14_pw_half_chris_support:
            $ kiwii_post.newComment("Chris", _("Haha, perfect! #Vote4Chloe"))
        $ kiwii_post.newComment("Aubrey", _("Aww! Hell yeah! This is so cute, Chlo <3"))
        $ kiwii_post.newComment("Imre", _("Yessss!!!!!"))
        $ kiwii_post.newComment("Grayson", _("LMAO you’re down bad, huh?"))
        $ kiwii_post.newComment("Chloe", _("Be civil at least, Grayson"), mentions="Grayson")
        $ kiwii_post.newComment("Riley", _("Omg! Can I have that thing?"))
        $ kiwii_post.addReply(_("These turned out perfect! #Vote4Chloe"))
        $ kiwii_post.addReply(_("Aww, haha. Congrats!"))

    if v14s30b_pw_image_two and not v14s30b_its_perfect:
        $ kiwii_post = KiwiiPost("Chloe", In the woods Chloe smiling mouth slightly open holding the plush wolf and one hand in the air like she’s cheering, _("It’s official! The Wolves and The Chicks are uniting as one to ensure that I stay president and furthermore, bring a wonderful balance to our new and improved sorority. #TheChicksWhoCriedWolves #Vote4ChloeVote4Wolves"), numberLikes=856)
        if v14_pw_half_chris_support:
            $ kiwii_post.newComment("Chris", _("Haha, perfect! #Vote4Chloe"))
        $ kiwii_post.newComment("Aubrey", _("Aww! Hell yeah! This is so cute, Chlo <3"))
        $ kiwii_post.newComment("Imre", _("Yessss!!!!!"))
        $ kiwii_post.newComment("Grayson", _("LMAO you’re down bad, huh?"))
        $ kiwii_post.newComment("Chloe", _("Be civil at least, Grayson"), mentions="Grayson")
        $ kiwii_post.newComment("Riley", _("Omg! Can I have that thing?"))
        $ kiwii_post.addReply(_("These turned out perfect! #Vote4Chloe"))
        $ kiwii_post.addReply(_("Aww, haha. Congrats!"))

    if v14s30b_rw_image_one and v14s30b_its_perfect:
        $ kiwii_post = KiwiiPost("Chloe", In the woods Chloe standing next to the real wolf smiling with one hand on her hip and one on the wolf’s head, _("What’s a chick without her wolf? <3 #PresidentialStatus #Vote4ChloeVote4Wolves"), numberLikes=973)
        if v14_pw_half_chris_support:
            $ kiwii_post.newComment("Chris", _("Haha, perfect! #Vote4Chloe"))
        $ kiwii_post.newComment("Aubrey", _("Aww! Hell yeah! This is so cute, Chlo <3"))
        $ kiwii_post.newComment("Imre", _("Yessss!!!!!"))
        $ kiwii_post.newComment("Grayson", _("LMAO you’re down bad, huh?"))
        $ kiwii_post.newComment("Chloe", _("Be civil at least, Grayson"), mentions="Grayson")
        $ kiwii_post.newComment("Riley", _("Omg! Can I have that thing?"))
        $ kiwii_post.addReply(_("These turned out perfect! #Vote4Chloe"))
        $ kiwii_post.addReply(_("Aww, haha. Congrats!"))

    if v14s30b_rw_image_one and not v14s30b_its_perfect:
        $ kiwii_post = KiwiiPost("Chloe", In the woods Chloe standing next to the real wolf smiling with one hand on her hip and one on the wolf’s head, _("A vote for me is a vote for The Chicks AND a vote for The Wolves :) #TheChicksWhoCriedWolves #Vote4ChloeVote4Wolves"), numberLikes=1273)
        if v14_pw_half_chris_support:
            $ kiwii_post.newComment("Chris", _("Haha, perfect! #Vote4Chloe"))
        $ kiwii_post.newComment("Aubrey", _("Aww! Hell yeah! This is so cute, Chlo <3"))
        $ kiwii_post.newComment("Imre", _("Yessss!!!!!"))
        $ kiwii_post.newComment("Grayson", _("LMAO you’re down bad, huh?"))
        $ kiwii_post.newComment("Chloe", _("Be civil at least, Grayson"), mentions="Grayson")
        $ kiwii_post.newComment("Riley", _("Omg! Can I have that thing?"))
        $ kiwii_post.addReply(_("These turned out perfect! #Vote4Chloe"))
        $ kiwii_post.addReply(_("Aww, haha. Congrats!"))

    if v14s30b_rw_image_two and v14s30b_its_perfect:
        $ kiwii_post = KiwiiPost("Chloe", In the woods Chloe smiling while she gives the real wolf a high five, _("Teamwork makes the dreamwork! <3 #PresidentialStatus #Vote4ChloeVote4Wolves"), numberLikes=981)
        if v14_pw_half_chris_support:
            $ kiwii_post.newComment("Chris", _("Haha, perfect! #Vote4Chloe"))
        $ kiwii_post.newComment("Aubrey", _("Aww! Hell yeah! This is so cute, Chlo <3"))
        $ kiwii_post.newComment("Imre", _("Yessss!!!!!"))
        $ kiwii_post.newComment("Grayson", _("LMAO you’re down bad, huh?"))
        $ kiwii_post.newComment("Chloe", _("Be civil at least, Grayson"), mentions="Grayson")
        $ kiwii_post.newComment("Riley", _("Omg! Can I have that thing?"))
        $ kiwii_post.addReply(_("These turned out perfect! #Vote4Chloe"))
        $ kiwii_post.addReply(_("Aww, haha. Congrats!"))

    if v14s30b_rw_image_two and not v14s30b_its_perfect:
        $ kiwii_post = KiwiiPost("Chloe", In the woods Chloe smiling while she gives the real wolf a high five, _("Teamwork makes the dreamwork! <3 #TheChicksWhoCriedWolves #Vote4ChloeVote4Wolves"), numberLikes=1294)
        if v14_pw_half_chris_support:
            $ kiwii_post.newComment("Chris", _("Haha, perfect! #Vote4Chloe"))
        $ kiwii_post.newComment("Aubrey", _("Aww! Hell yeah! This is so cute, Chlo <3"))
        $ kiwii_post.newComment("Imre", _("Yessss!!!!!"))
        $ kiwii_post.newComment("Grayson", _("LMAO you’re down bad, huh?"))
        $ kiwii_post.newComment("Chloe", _("Be civil at least, Grayson"), mentions="Grayson")
        $ kiwii_post.newComment("Riley", _("Omg! Can I have that thing?"))
        $ kiwii_post.addReply(_("These turned out perfect! #Vote4Chloe"))
        $ kiwii_post.addReply(_("Aww, haha. Congrats!"))

    jump v14s33