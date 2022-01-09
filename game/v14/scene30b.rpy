# SCENE 30b: Looking at the pictures together with Chloe
# Locations: Campus, Wolves/Apes room.
# Characters: CHLOE (Outfit: 1), MC (Outfit: 2)
# Time: Afternoon

label v14s30b:
    scene v14s30b_1 # TPP. Show MC and Chloe walking on the Campus sidewalk, Both slight smile, mouth closed.
    with fade

    pause 0.75

    play music "music/v13/Track Scene 30_1.mp3" fadein 2

    scene v14s30b_2 # FPP. MC looking at Chloe, Chloe looking down at her phone, Chloe slight smile, mouth open.
    with dissolve

    cl "Alright... Let's get a good look at these."

    scene v14s30b_2a # FPP. Same as v14s30b_2, Chloe slight smile, mouth closed.
    with dissolve

    u "Do you like what you see so far?"

    scene v14s30b_2
    with dissolve

    cl "I do. I also think this helps the campaign a lot."

    cl "Of the two frats, the Wolves are way more respected than the Apes and so..."

    cl "Just strategically speaking, this helps a lot."

    scene v14s30b_2a
    with dissolve

    u "That's what I like to hear."

    scene v14s30b_2
    with dissolve

    cl "My posing definitely isn't as good as Aubrey's though."

    scene v14s30b_2a
    with dissolve

    u "So you know about Lew's and all that?"

    scene v14s30b_2
    with dissolve

    cl "Haha, I know more about Aubrey than most."

    scene v14s30b_2a
    with dissolve

    u "She is your VP..."

    scene v14s30b_2
    with dissolve

    cl "Exactly, and hopefully she chooses to stay on after we win."

    scene v14s30b_2a
    with dissolve

    u "I'm sure she will."

    scene v14s30b_2
    with dissolve

    cl "Ha, glad you think so. Now..."

    if not v14_realwolf:
        cl "I'm not sure how these will be perceived and all you know? With us having a fake wolf, but I still think the pictures are really good."

        scene v14s30b_3 # FPP. MC looking at the phone showing the first image, Chloe standing next to the plush wolf, smiling proudly with her hand on her hip. (Possible leave the phone screen blank and photoshop the scene from the photoshoot onto the phone :D )
        with dissolve

        pause

        scene v14s30b_3a # FPP. Same as v14s30b_3, The second image now on the phone, The photo of Chloe holding the plush wolf in one arm and her other hand in the air like she is chairing. (Like the other scene may be possible to edit that scene onto the phone in photoshop :D )
        with dissolve

        cl "Which one is your favorite?"

        menu:
            "Standing next to the plush":
                $ v14s30b_image = 1

                scene v14s30b_3
                with dissolve

            "Holding the plush and cheering":
                $ v14s30b_image = 2

                scene v14s30b_3a 
                with dissolve
            
        u "That one."

        scene v14s30b_2
        with dissolve

        cl "Good call. I'm gonna post that one on Kiwii then."

    else:
        cl "I know the entire school is gonna be off the wall about these photos, haha."

        scene v14s30b_3b # FPP. Same as v14s30b_3a, First image of real wolf photoshoot, Chloe standing next to wolf smiling, one hand on hip, one on wolf's head on the phone screen.
        with dissolve

        pause 

        scene v14s30b_3c # FPP. Same as v14s30b_3b, Second Image of the real wolf photoshoot, Chloe giving the real wolf a high five photo on the phone screen.
        with dissolve

        cl "Which one is your favorite?"

        menu:
            "Standing next to the wolf":
                $ v14s30b_image = 1

                scene v14s30b_3b
                with dissolve

            "High-fiving the wolf":
                $ v14s30b_image = 2

                scene v14s30b_3c
                with dissolve
            
        u "That one."

        scene v14s30b_2
        with dissolve

        cl "Good call. I'm gonna post that one on Kiwii then."

    scene v14s30b_2a
    with dissolve

    u "What about your caption?"

    scene v14s30b_2
    with dissolve

    cl "Well, I'll definitely include \"#PresidentialStatus\". Then something about voting for me."

    menu:
        "It's perfect":
            $ add_point(KCT.BOYFRIEND)
            $ v14s30b_its_perfect = True

            scene v14s30b_2a
            with dissolve

            u "Yeah, that's perfect. Standing tall and proud with a short and sweet caption, the main feature is you."

            scene v14s30b_2
            with dissolve

            cl "*Chuckles* Exactly."

        "What about something else?":
            $ add_point(KCT.TROUBLEMAKER)
            scene v14s30b_2a
            with dissolve

            u "What about something else?"

            scene v14s30b_2
            with dissolve

            cl "Something else?"

            scene v14s30b_2a
            with dissolve

            u "Well, yeah. Like something about the Chicks and the Wolves, so it feel like a team effort?"

            scene v14s30b_2
            with dissolve

            cl "I guess that makes sense considering it's an alliance announcement, as well as a good pic for my feed, haha."

            scene v14s30b_2a
            with dissolve

            u "Exactly, so maybe something like, \"#TheChicksWhoCriedWolves\"."

            scene v14s30b_2
            with dissolve

            cl "You're right! That's perfect, [name]."

            scene v14s30b_2a
            with dissolve

            u "*Laughs* You're welcome."

    scene v14s30b_4 # FPP. Chloe looking at MC, MC looking at Chloe, Chloe slight smile, mouth open.
    with dissolve

    cl "Well, this has been a lot better than I had imagined. I'm off to get it all set in stone."

    cl "Thanks again for everything."

    scene v14s30b_4a # FPP. Same as v14s30b_4a, Chloe slight smile, mouth closed.
    with dissolve

    u "Of course! I'll be on the lookout for your big announcement."

    scene v14s30b_4
    with dissolve

    cl "*Chuckles*"

    if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
        play sound "sounds/kiss.mp3"
        scene v14s30b_5 # FPP. Chloe kissing MC.
        with dissolve
        
        pause 1.5

    scene v14s30b_6 # FPP. Show Chloe running off away from MC.
    with dissolve

    pause 0.75

    scene v14s30b_7 # TPP. Show MC walking down the Campus sidewalk.
    with dissolve

    pause 0.75

    if joinwolves:
        scene v14s30b_8 # TPP. Show MC walking into the wolves house.
        with fade

        pause 0.75

        play sound "sounds/doorclose.mp3"

        scene v14s30b_9 # TPP. MC sitting on his bed in the Wolves room, slight smile, mouth closed.
        with dissolve

        pause 0.75

    else:
        scene v14s30b_10 # TPP. Show MC walking into the Apes house.
        with fade

        pause 0.75

        play sound "sounds/doorclose.mp3"

        scene v14s30b_11 # TPP. Show MC sitting on his bed in the Apes room, slight smile, mouth closed.
        with dissolve

        pause 0.75
    
    # Don't know if it was done correctly I tried my best :P
    if not v14_realwolf and v14s30b_image == 1 and v14s30b_its_perfect:
        $ v14s30b_kiwiiPost1 = KiwiiPost(chloe, "v14/v14s30b_pw_image_one.webp", _("What's a Chick without her Wolf? <3 #PresidentialStatus #Vote4ChloeVote4Wolves"), numberLikes=712)
        if v14_chrissupport > 1:
            $ v14s30b_kiwiiPost1.newComment(chris, _("Haha, perfect! #Vote4Chloe"), numberLikes=renpy.random.randint(300, 600), force_send=True)
        $ v14s30b_kiwiiPost1.newComment(aubrey, _("Aww! Hell yeah! This is so cute, Chloe <3"), numberLikes=renpy.random.randint(300, 600), force_send=True)
        $ v14s30b_kiwiiPost1.newComment(imre, _("Yessss!!!!!"), numberLikes=renpy.random.randint(300, 600), force_send=True)
        $ v14s30b_kiwiiPost1.newComment(grayson, _("LMAO you're down bad, huh?"), numberLikes=renpy.random.randint(300, 600), force_send=True)
        $ v14s30b_kiwiiPost1.newComment(chloe, _("Be civil at least, Grayson"), numberLikes=renpy.random.randint(300, 600), mentions=[grayson], force_send=True)
        $ v14s30b_kiwiiPost1.newComment(riley, _("Omg! Can I have that thing?"), numberLikes=renpy.random.randint(300, 600), force_send=True)
        $ v14s30b_kiwiiPost1.addReply(_("These turned out perfect! #Vote4Chloe"), numberLikes=renpy.random.randint(300, 600))
        $ v14s30b_kiwiiPost1.addReply(_("Aww, haha. Congrats!"), numberLikes=renpy.random.randint(300, 600))

    elif not v14_realwolf and v14s30b_image == 1:
        $ v14s30b_kiwiiPost2 = KiwiiPost(chloe, "v14/v14s30b_pw_image_one.webp", _("It's official! The Wolves and The Chicks are uniting! #TheChicksWhoCriedWolves #Vote4ChloeVote4Wolves"), numberLikes=812)
        if v14_chrissupport > 1:
            $ v14s30b_kiwiiPost2.newComment(chris, _("Haha, perfect! #Vote4Chloe"), numberLikes=renpy.random.randint(350, 650), force_send=True)
        $ v14s30b_kiwiiPost2.newComment(aubrey, _("Aww! Hell yeah! This is so cute, Chloe <3"), numberLikes=renpy.random.randint(350, 650), force_send=True)
        $ v14s30b_kiwiiPost2.newComment(imre, _("Yessss!!!!!"), numberLikes=renpy.random.randint(350, 650), force_send=True)
        $ v14s30b_kiwiiPost2.newComment(grayson, _("LMAO you're down bad, huh?"), numberLikes=renpy.random.randint(350, 650), force_send=True)
        $ v14s30b_kiwiiPost2.newComment(chloe, _("Be civil at least, Grayson"), numberLikes=renpy.random.randint(350, 650), mentions=[grayson], force_send=True)
        $ v14s30b_kiwiiPost2.newComment(riley, _("Omg! Can I have that thing?"), numberLikes=renpy.random.randint(350, 650), force_send=True)
        $ v14s30b_kiwiiPost2.addReply(_("These turned out perfect! #Vote4Chloe"), numberLikes=renpy.random.randint(350, 650))
        $ v14s30b_kiwiiPost2.addReply(_("Aww, haha. Congrats!"), numberLikes=renpy.random.randint(350, 650))

    elif not v14_realwolf and v14s30b_image == 2 and v14s30b_its_perfect:
        $ v14s30b_kiwiiPost3 = KiwiiPost(chloe, "v14/v14s30b_pw_image_two.webp", _("I'd like to officially announce The Chicks' partnership with The Wolves! <3 #PresidentialStatus #Vote4ChloeVote4Wolves"), numberLikes=756)
        if v14_chrissupport > 1:
            $ v14s30b_kiwiiPost3.newComment(chris, _("Haha, perfect! #Vote4Chloe"), numberLikes=renpy.random.randint(300, 600), force_send=True)
        $ v14s30b_kiwiiPost3.newComment(aubrey, _("Aww! Hell yeah! This is so cute, Chloe <3"), numberLikes=renpy.random.randint(300, 600), force_send=True)
        $ v14s30b_kiwiiPost3.newComment(imre, _("Yessss!!!!!"), numberLikes=renpy.random.randint(300, 600), force_send=True)
        $ v14s30b_kiwiiPost3.newComment(grayson, _("LMAO you're down bad, huh?"), numberLikes=renpy.random.randint(300, 600), force_send=True)
        $ v14s30b_kiwiiPost3.newComment(chloe, _("Be civil at least, Grayson"), numberLikes=renpy.random.randint(300, 600), mentions=[grayson], force_send=True)
        $ v14s30b_kiwiiPost3.newComment(riley, _("Omg! Can I have that thing?"), numberLikes=renpy.random.randint(300, 600), force_send=True)
        $ v14s30b_kiwiiPost3.addReply(_("These turned out perfect! #Vote4Chloe"), numberLikes=renpy.random.randint(300, 600))
        $ v14s30b_kiwiiPost3.addReply(_("Aww, haha. Congrats!"), numberLikes=renpy.random.randint(300, 600))

    elif not v14_realwolf and v14s30b_image == 2:
        $ v14s30b_kiwiiPost4 = KiwiiPost(chloe, "v14/v14s30b_pw_image_two.webp", _("It's official! The Wolves and The Chicks are uniting! #TheChicksWhoCriedWolves #Vote4ChloeVote4Wolves"), numberLikes=856)
        if v14_chrissupport > 1:
            $ v14s30b_kiwiiPost4.newComment(chris, _("Haha, perfect! #Vote4Chloe"), numberLikes=renpy.random.randint(300, 700), force_send=True)
        $ v14s30b_kiwiiPost4.newComment(aubrey, _("Aww! Hell yeah! This is so cute, Chloe <3"), numberLikes=renpy.random.randint(300, 700), force_send=True)
        $ v14s30b_kiwiiPost4.newComment(imre, _("Yessss!!!!!"), numberLikes=renpy.random.randint(300, 700), force_send=True)
        $ v14s30b_kiwiiPost4.newComment(grayson, _("LMAO you're down bad, huh?"), numberLikes=renpy.random.randint(300, 700), force_send=True)
        $ v14s30b_kiwiiPost4.newComment(chloe, _("Be civil at least, Grayson"), numberLikes=renpy.random.randint(300, 700), mentions=[grayson], force_send=True)
        $ v14s30b_kiwiiPost4.newComment(riley, _("Omg! Can I have that thing?"), numberLikes=renpy.random.randint(300, 700), force_send=True)
        $ v14s30b_kiwiiPost4.addReply(_("These turned out perfect! #Vote4Chloe"), numberLikes=renpy.random.randint(300, 700))
        $ v14s30b_kiwiiPost4.addReply(_("Aww, haha. Congrats!"), numberLikes=renpy.random.randint(300, 700))

    elif v14s30b_image == 1 and v14s30b_its_perfect:
        $ v14s30b_kiwiiPost5 = KiwiiPost(chloe, "v14/v14s30b_rw_image_one.webp", _("What's a Chick without her Wolf? <3 #PresidentialStatus #Vote4ChloeVote4Wolves"), numberLikes=973)
        if v14_chrissupport > 1:
            $ v14s30b_kiwiiPost5.newComment(chris, _("Haha, perfect! #Vote4Chloe"), numberLikes=renpy.random.randint(400, 800), force_send=True)
        $ v14s30b_kiwiiPost5.newComment(aubrey, _("Aww! Hell yeah! This is so cute, Chloe <3"), numberLikes=renpy.random.randint(400, 800), force_send=True)
        $ v14s30b_kiwiiPost5.newComment(imre, _("Yessss!!!!!"), numberLikes=renpy.random.randint(400, 800), force_send=True)
        $ v14s30b_kiwiiPost5.newComment(grayson, _("LMAO you're down bad, huh?"), numberLikes=renpy.random.randint(400, 800), force_send=True)
        $ v14s30b_kiwiiPost5.newComment(chloe, _("Be civil at least, Grayson"), numberLikes=renpy.random.randint(400, 800), mentions=[grayson], force_send=True)
        $ v14s30b_kiwiiPost5.newComment(riley, _("Omg! Can I have that thing?"), numberLikes=renpy.random.randint(400, 800), force_send=True)
        $ v14s30b_kiwiiPost5.addReply(_("These turned out perfect! #Vote4Chloe"), numberLikes=renpy.random.randint(400, 800))
        $ v14s30b_kiwiiPost5.addReply(_("Aww, haha. Congrats!"), numberLikes=renpy.random.randint(400, 800))

    elif v14s30b_image == 1:
        $ v14s30b_kiwiiPost6 = KiwiiPost(chloe, "v14/v14s30b_rw_image_one.webp", _("   A vote for me is a vote for The Chicks AND a vote for The Wolves :) #TheChicksWhoCriedWolves #Vote4ChloeVote4Wolves"), numberLikes=1273)
        if v14_chrissupport > 1:
            $ v14s30b_kiwiiPost6.newComment(chris, _("Haha, perfect! #Vote4Chloe"), numberLikes=renpy.random.randint(400, 1000), force_send=True)
        $ v14s30b_kiwiiPost6.newComment(aubrey, _("Aww! Hell yeah! This is so cute, Chloe <3"), numberLikes=renpy.random.randint(400, 1000), force_send=True)
        $ v14s30b_kiwiiPost6.newComment(imre, _("Yessss!!!!!"), numberLikes=renpy.random.randint(400, 1000), force_send=True)
        $ v14s30b_kiwiiPost6.newComment(grayson, _("LMAO you're down bad, huh?"), numberLikes=renpy.random.randint(400, 1000), force_send=True)
        $ v14s30b_kiwiiPost6.newComment(chloe, _("Be civil at least, Grayson"), numberLikes=renpy.random.randint(400, 1000), mentions=[grayson], force_send=True)
        $ v14s30b_kiwiiPost6.newComment(riley, _("Omg! Can I have that thing?"), numberLikes=renpy.random.randint(400, 1000), force_send=True)
        $ v14s30b_kiwiiPost6.addReply(_("These turned out perfect! #Vote4Chloe"), numberLikes=renpy.random.randint(400, 1000))
        $ v14s30b_kiwiiPost6.addReply(_("Aww, haha. Congrats!"), numberLikes=renpy.random.randint(400, 1000))

    elif v14s30b_image == 2 and v14s30b_its_perfect:
        $ v14s30b_kiwiiPost7 = KiwiiPost(chloe, "v14/v14s30b_rw_image_two.webp", _("Teamwork makes the dreamwork! <3 #PresidentialStatus #Vote4ChloeVote4Wolves"), numberLikes=981)
        if v14_chrissupport > 1:
            $ v14s30b_kiwiiPost7.newComment(chris, _("Haha, perfect! #Vote4Chloe"), numberLikes=renpy.random.randint(350, 850), force_send=True)
        $ v14s30b_kiwiiPost7.newComment(aubrey, _("Aww! Hell yeah! This is so cute, Chloe <3"), numberLikes=renpy.random.randint(350, 850), force_send=True)
        $ v14s30b_kiwiiPost7.newComment(imre, _("Yessss!!!!!"), numberLikes=renpy.random.randint(350, 850), force_send=True)
        $ v14s30b_kiwiiPost7.newComment(grayson, _("LMAO you're down bad, huh?"), numberLikes=renpy.random.randint(350, 850), force_send=True)
        $ v14s30b_kiwiiPost7.newComment(chloe, _("Be civil at least, Grayson"), numberLikes=renpy.random.randint(350, 850), mentions=[grayson], force_send=True)
        $ v14s30b_kiwiiPost7.newComment(riley, _("Omg! Can I have that thing?"), numberLikes=renpy.random.randint(350, 850), force_send=True)
        $ v14s30b_kiwiiPost7.addReply(_("These turned out perfect! #Vote4Chloe"), numberLikes=renpy.random.randint(350, 850))
        $ v14s30b_kiwiiPost7.addReply(_("Aww, haha. Congrats!"), numberLikes=renpy.random.randint(350, 850))

    else: #possible because scene30b implies photoshoot
        $ v14s30b_kiwiiPost8 = KiwiiPost(chloe, "v14/v14s30b_rw_image_two.webp", _("Teamwork makes the dreamwork! <3 #TheChicksWhoCriedWolves #Vote4ChloeVote4Wolves"), numberLikes=1294)
        if v14_chrissupport > 1:
            $ v14s30b_kiwiiPost8.newComment(chris, _("Haha, perfect! #Vote4Chloe"), numberLikes=renpy.random.randint(400, 1000), force_send=True)
        $ v14s30b_kiwiiPost8.newComment(aubrey, _("Aww! Hell yeah! This is so cute, Chloe <3"), numberLikes=renpy.random.randint(400, 1000), force_send=True)
        $ v14s30b_kiwiiPost8.newComment(imre, _("Yessss!!!!!"), numberLikes=renpy.random.randint(400, 1000), force_send=True)
        $ v14s30b_kiwiiPost8.newComment(grayson, _("LMAO you're down bad, huh?"), numberLikes=renpy.random.randint(400, 1000), force_send=True)
        $ v14s30b_kiwiiPost8.newComment(chloe, _("Be civil at least, Grayson"), numberLikes=renpy.random.randint(400, 1000), mentions=[grayson], force_send=True)
        $ v14s30b_kiwiiPost8.newComment(riley, _("Omg! Can I have that thing?"), numberLikes=renpy.random.randint(400, 1000), force_send=True)
        $ v14s30b_kiwiiPost8.addReply(_("These turned out perfect! #Vote4Chloe"), numberLikes=renpy.random.randint(400, 1000))
        $ v14s30b_kiwiiPost8.addReply(_("Aww, haha. Congrats!"), numberLikes=renpy.random.randint(400, 1000))

    u "Let me check how the announcement came out."

    if v14s30b_its_perfect:
        $ set_presidency_percent(v14_lindsey_popularity - 1) #tick
    else:
        $ set_presidency_percent(v14_lindsey_popularity - 3) #tick
    call screen phone

    stop music fadeout 3

    jump v14s33