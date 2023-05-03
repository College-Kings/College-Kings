# Locations: MC's dorm (only a couple of renders). MC's new room and the den (left room after entering the building) in Apes house
# MC's outfit: Casual wear but something that can be worn for a party
# Everyone else's outfits: Similar casual wear for new Apes (Caleb, Ryan) and Apes in their jackets
# Characters needed: MC (outfit 3), Grayson (outfit 3), Chloe (outfit 2 or put together some other revealing outfit), Caleb (outfit 1), Cameron (outfit 3), Ryan (outfit 1), Sam (outfit 2), Mason (outfit 1), Some other random chick in a revealing outfit
# Time: Saturday evening to night

# SCENE 13: MOVING INTO THE APES
label after_apes_ceremony:
    scene v8apes21 # TPP. MC in his dorm packing his bag (finished it), smiling and mouth closed
    with Dissolve(1)
    u "(...and done!)"

    # [Grayson has made a Kiwii post that MC, Ryan, and Caleb are the new Apes. If MC got first place, Grayson also says Congrats to the prodigal son, [name] for getting our top score. Looks like somebody's coming for my throne!]

    # Kiwii post pic description: Grayson popping a champagne in Apes den with MC, Ryan and Caleb around him (make sure they're wearing the same outfits as in scene 12)
    $ v8s13_kiwiiPost = KiwiiPost(grayson, "phone/kiwii/Posts/v8/grpost1.webp", _("[name], Ryan and Caleb are the new proud Apes! I can see this fight season turning out well for us!"), number_likes=renpy.random.randint(320, 350))
    if apesVids == 4:
        $ v8s13_kiwiiPost.newComment(grayson, _("And congrats to the prodigal son, [name], for getting the perfect score. Looks like somebody's coming for my throne!"), number_likes=renpy.random.randint(140, 150))
    $ v8s13_kiwiiPost.newComment(ryan, _("Apes baby! Woohoooo!!!"), number_likes=renpy.random.randint(60, 70))
    $ v8s13_kiwiiPost.newComment(caleb, _("GO APES!!!"), number_likes=renpy.random.randint(60, 70))
    $ v8s13_kiwiiPost.newComment(parker, _("Congrats guys!"), number_likes=renpy.random.randint(40, 50))
    if apesVids == 4:
        $ v8s13_kiwiiPost.newComment(aubrey, _("Damn, perfect score? Would love to see you in action in the ring ;)"), mentions=[mc], number_likes=renpy.random.randint(80, 90))
    else:
        $ v8s13_kiwiiPost.newComment(aubrey, _("Congrats guys! Couldn't be at the ceremony cause of some stupid shit :/"), number_likes=renpy.random.randint(50, 60))
    $ v8s13_kiwiiPost.newComment(mason, _("So proud of you guys especially my man"), mentions=[caleb], number_likes=renpy.random.randint(40, 50))
    $ v8s13_kiwiiPost.newComment(emily, _("Yaayyy! Congrats"), mentions=[mc], number_likes=renpy.random.randint(25, 35))
    if apesVids == 4:
        $ v8s13_kiwiiPost.newComment(elijah, _("Hmph ridiculous! Like those are the perfect scores that matter..."), number_likes=renpy.random.randint(3, 6))
        $ v8s13_kiwiiPost.newComment(cameron, _("Just shut the fuck up and never come back"), mentions=[elijah], number_likes=renpy.random.randint(75, 85))
        $ v8s13_kiwiiPost.newComment(cameron, _("That is unless you want me to kick your ass, then of course knock yourself out"), mentions=[elijah], number_likes=renpy.random.randint(110, 120))
    $ v8s13_kiwiiPost.newComment(amber, _("Congrats people!!!"), mentions=[mc, ryan, caleb], number_likes=renpy.random.randint(50, 60))
    $ v8s13_kiwiiPost.newComment(caleb, _("Thanks everyone!"), number_likes=renpy.random.randint(20, 30))

    python:
        v8s13_reply1 = MessageBuilder(chloe) # phn_chloe11_a
        v8s13_reply1.new_message(_("Guess you'll have to wait and see ;)"))
        v8s13_reply1.add_reply(_("I'm moving my stuff now. How about we get started tonight?"))
        v8s13_reply1.new_message(_("You're such a flirt. Have a good night!"))

        v8s13_reply2 = MessageBuilder(chloe) # phn_chloe11_b
        v8s13_reply2.new_message(_("Aww, I like talking to you too. You're sweet."))
        v8s13_reply2.add_reply(_("Sweet? Not hot? Or sexy? Or... anything but sweet?"))
        v8s13_reply2.new_message(_("Sweet and cute ;)"))
        v8s13_reply2.add_reply(_("I'll take it. For now. Talk to you when I get settled."))
        v8s13_reply2.new_message(_("Good night."))

        MessengerService.new_message(chloe, _("Congrats on getting in. Looks like we'll be seeing a lot of each other."))
        MessengerService.add_replies(chloe,
            Reply(_("Exactly how much is a lot? ;)"), v8s13_reply1),
            Reply(_("Hope so. I like talking to you."), v8s13_reply2)
        )

    play sound sound.vibrate

    scene v8apes21a # MC looking at his phone, mouth closed
    with dissolve

    while MessengerService.has_replies(chloe):
        call screen phone
        if MessengerService.has_replies(chloe):
            u "(I should probably reply.)"

        u "(Gotta get going.)"
        jump phn_chloe11_done

label phn_chloe11_done:
    scene v8apes22 # TPP. MC leaving out of his dorm with his bag, smiling and mouth closed
    with dissolve
    u "(An Ape. That's who I am now.)"
    u "(Can't believe I'm gonna live in a frat house.)"

    scene v8apes23 # TPP. MC in his room in Apes house. He's unpacking his stuff from bag
    with Fade(0.75, 0.25, 0.75)
    pause

    scene v8apes24 # TPP. MC placing books and other stuff on his new desk
    with dissolve
    u "(This room is miles better than the dorm I was in.)"

    play sound sound.knock
    "*Knock knock knock*"

    scene v8apes25 # FPP. Shot of the door in his room closed
    with dissolve
    pause 0.5

    play sound "sounds/dooropen.mp3"

    scene v8apes25a # Door open now. Grayson is standing there with his hands behind his back (He's holding two beer bottles). He's in a party mood, smiling and mouth closed
    with dissolve
    pause 0.5

    scene v8apes25b # Same as v8apes25a but Grayson mouth closed
    with dissolve
    gr "Hey man, just checking on my new guys. How's it going?"

    scene v8apes25a
    with dissolve
    u "Great! I was just unpacking."

    scene v8apes25b
    with dissolve
    gr "Naw, there's plenty of time for that. Let's celebrate!"

    scene v8apes25c # Grayson reveals the beers from behind his back and hands one to the MC. Same expression as v8apes25a (mouth closed)
    with dissolve
    u "It's great to be an Ape!"

    scene v8apes25d # Grayson with one beer in his hand. Same expression as v8apes25a (mouth closed)
    with dissolve
    u "Come in..."

    scene v8apes25e # Same as v8apes25d but Grayson talking
    with dissolve
    gr "No, {i}you{/i} come out. We're all chilling in the den."
    gr "And some of the Chicks are here too..."

    menu:
        "Party":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            scene v8apes25d
            with dissolve
            u "Even better!"

            scene v8apes25e
            with dissolve
            gr "Awesome. Follow me."

            scene v8apes25g # Grayson turned back and starts walking away (facial expression should not be visible)
            with dissolve
            pause 0.5

        "Stay back and study":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            scene v8apes25d
            with dissolve
            u "I better finish up. Thanks for the beer, though."

            scene v8apes25e
            with dissolve
            gr "You can do that later, don't be such a killjoy now."

            scene v8apes25d
            with dissolve
            u "I'm already behind on my work. I really need to focus."

            u "Don't want to get kicked out of school now that I'm finally an Ape!"

            scene v8apes25f # Grayson disbelief, disappointed and talking
            with dissolve
            gr "Whatever, dude. I thought you were one of us."

            scene v8apes25g
            with dissolve
            u "(*Sigh* Do I really have to ditch bonding time with the guys?)"
            u "Grayson, wait!"

    # TO RENDERERS: Things happening in this scene: 1 - Chloe talking to Caleb somewhere in the room and 2 - Cameron sitting all alone by himself and contemplating stuff. 3 - Ryan, Sam and the random chick just drinking and chitchatting on the couches.
    scene v8apes26 # FPP. MC is following Grayson and they're entering the den. Grayson is just inside the room with one of his hands raised (beer in hand, and his mouth open if face is visible)
    with fade
    pause 0.5
    gr "Woooooo!"

    scene v8apes27 # TPP. Shot of Ryan, Sam cheering with their bottles raised while looking towards Grayson entering (need not be visible in the shot). Ryan mouth open. The other girl is just looking towards Grayson, smiling
    with dissolve
    ry "Woohoooo!"

    if MessengerService.find_message(chloe, "Guess you'll have to wait and see ;)"):
        scene v8apes28 # FPP. MC inside the room now and he notices Chloe and Caleb chitchatting
        with dissolve
        u "(Oh, Chloe is here.)"

        scene v8apes29 # FPP. MC approaches them so close up shot of Chloe talking now. Caleb need not be in the shot. Chloe looking into the camera, smiling with teeth visible (not talking)
        with dissolve
        u "Guess you were right about seeing a lot of each other."

        scene v8apes29a # Same as v8apes29 but Chloe talking
        with dissolve
        cl "Told ya. Like your new room?"

        scene v8apes29
        with dissolve
        u "Could use a woman's touch. Wanna come check it out?"

        scene v8apes29a
        with dissolve
        cl "Plenty of time for that. Let's have some fun first."

        scene v8apes29
        with dissolve
        u "That's what I'm trying to do! You look like a lot of fun..."

        scene v8apes29b # Chloe checking you out, flirty face, mouth open
        with dissolve
        cl "So do you. But I'm on Chicks duty. Gotta welcome you new boys to the house."

        scene v8apes29c # Chloe flirty, mouth closed
        with dissolve
        u "Raincheck?"

        scene v8apes29d # Chloe flirty mouth open
        with dissolve
        cl "Raincheck."

    else:
        scene v8apes28
        with dissolve
        u "(There's Chloe. But she looks busy. I shouldn't bother her.)"

        scene v8apes28a # Chloe noticed the MC and is now waving at him, smiling
        with dissolve
        u "(Well...)"

        scene v8apes29
        with dissolve
        u "Hey, I wasn't gonna bother you. You looked busy."

        scene v8apes29a
        with dissolve
        cl "Told ya you were sweet."

        scene v8apes30 # FPP. Same as v8apes29 but MC is looking Chloe up and down. So maybe just tilt the camera to show Chloe's body
        with dissolve
        pause

        scene v8apes29c
        with dissolve
        u "Not always."

        scene v8apes29d
        with dissolve
        cl "If I wasn't on Chicks duty, I might call your bluff."

        scene v8apes29c
        with dissolve
        u "Maybe after..."

        scene v8apes29d
        with dissolve
        cl "Maybe."

    scene v8apes31 # TPP. Chloe and MC same as before but MC noticed Cameron now and is looking towards him (Cam need not be in the shot)
    with dissolve
    u "(Hmm? What's wrong with him?)"

    scene v8apes32 # TPP. Shot of Cameron serious and deeply contemplating something (not looking into the camera). Has a drink beside him but not drinking it
    with dissolve
    pause

    scene v8apes29
    with dissolve
    u "Excuse me, I need to talk to Cameron."

    scene v8apes29a
    with dissolve
    cl "Sure. Talk to you later."

    scene v8apes33 # TPP. MC walking towards where Cameron is sitting. Cameron doesn't notice him and has similar expression as in v8apes32
    with dissolve
    pause 1

    scene v8apes33a # MC sits beside him, Cameron notices him now
    with dissolve
    pause 0.5

    scene v8apes34 # FPP. Cameron still the same expression, mouth closed
    with dissolve
    u "Hey man, you alright?"

    scene v8apes34a # Cameron same expression, talking now
    with dissolve
    ca "I uh-"

    scene v8apes34b # Cameron forcing a smile and talking
    with dissolve
    ca "Of course, yeah. Uh... congrats on getting in. How you enjoying tonig-"

    scene v8apes34c # Same as 34b but mouth closed
    with dissolve
    u "For real dude, what's up?"

    scene v8apes34b
    with dissolve
    ca "Nothing's up. Just lame hanging out with you new kids."

    menu:
        "Press it":
            $ reputation.add_point(RepComponent.BRO)

            scene v8apes34c
            with dissolve
            u "Yeah, sure. Like it's not obvious something's wrong."

            scene v8apes34a
            with dissolve
            ca "It's just..."

        "Let it go":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            scene v8apes34c
            with dissolve
            u "OK, man. I'll leave you to it."

            scene v8apes35 # TPP. MC about to get up and leave (he turned but did not fully get up). Cameron looking towards the MC and talking seriously
            with dissolve
            ca "It's just..."

    scene v8apes36 # TPP. Shot of Sam and Ryan talking at the couches. The other random girl is also there, just listening. Sam talking and laughing, Ryan laughing. Beers in their hands
    with dissolve
    sam "And then she was all like-"

    scene v8apes34
    with dissolve
    ry "HAHAH OH GOD!"
    u "Wanna talk outside?"

    scene v8apes34a
    with dissolve
    ca "Yeah, alright."

    ### Location change ###
    scene v8apes37 # FPP. MC and Cameron walk outside the house to somewhere there's silence. Cameron serious and mouth closed
    with fade
    u "So, what's really up?"

    scene v8apes37a # Cameron serious and talking
    with dissolve
    ca "It's Sam..."

    scene v8apes37
    with dissolve
    u "Oh no, is she OK?"

    scene v8apes37a
    with dissolve
    ca "She's... I'm worried sick about her. I found her passed out in her room last night."

    scene v8apes37b # Cameron talking seriously but with a tinge of sadness
    with dissolve
    ca "She... she wouldn't wake up. I thought she was..."

    scene v8apes37c # Same as 37b but Cameron mouth closed
    with dissolve
    u "Aw, man, I'm so sorry. Is she OK now? Where is she?"

    scene v8apes37a
    with dissolve
    ca "I have a neighbor sitting with her until I get done here."

    scene v8apes37
    with dissolve
    u "Shit, Cam, I'm sure Grayson won't mind. Go be with your sister."

    scene v8apes37d # Cameron talking sarcastically and laughing a little
    with dissolve
    ca "Grayson would kill me if I left. It's ceremony night."

    scene v8apes37e # Same as 37d but mouth closed
    with dissolve
    u "What about your family? Any brothers or sisters who can come help?"
    u "Or better yet, your parents? They would definitely know what to do."

    scene v8apes37a
    with dissolve
    ca "My parents are the reason she's going through this. I'm surprised I'm not in an alley with a needle in my arm!"

    scene v8apes37
    with dissolve
    u "Wanna talk about it? Get it off your chest?"

    scene v8apes37a
    with dissolve
    ca "I don't know man. It's personal."

    scene v8apes37
    with dissolve
    u "I get it. But who else you gonna talk to? Does anyone know besides me?"

    scene v8apes37f # Cameron sigh, not looking into the camera
    with dissolve
    ca "*Sigh*"

    scene v8apes37a
    with dissolve
    ca "If you tell a soul, I'll kick your ass."

    scene v8apes37
    with dissolve
    u "I would never. We may have had our differences, but this is real shit."

    scene v8apes37a
    with dissolve
    ca "It's the same old story. She got in with the wrong crowd and it just kinda escalated."

    scene v8apes37b
    with dissolve
    ca "I didn't think she'd get this bad. My parents have their own demons. Apple didn't fall far..."
    ca "But they tried forcing her to go to treatment but she always runs away. Nothing's working."

    scene v8apes37c
    with dissolve
    u "Wow, I'm sorry, man. I don't know what to say."

    scene v8apes37a
    with dissolve
    ca "It's not your problem. I'm her big brother. I should be able to fix this... but..."

    scene v8apes37b
    with dissolve
    ca "How the hell am I supposed to know what to do?"

    scene v8apes37
    with dissolve
    u "You're not. It's too much. But... how can I help? We're brothers now, too. Apes stick together."

    scene v8apes37b
    with dissolve
    ca "I just... don't know."

    scene v8apes37g # MC places a hand on Cameron's shoulder. Cameron relieved, mouth closed
    with dissolve
    u "Don't worry. We'll help her together."

    scene v8apes37h # Same as 37g but Cameron talking
    with dissolve
    ca "Thanks man."

    scene v8apes37a
    with dissolve
    ca "We better get back inside before Grayson comes looking for me. I can't deal with him right now."

    scene v8apes37
    with dissolve
    u "Yeah, let's talk later. I got your back."

    scene v8apes38 # TPP. Showing MC, Cameron and Ryan just chitchatting on the couches in the den. A couple of empty beer bottles by their side. Cameron laughing and talking. Ryan laughing and talking. MC laughing (It's really late at night now)
    with Fade(1.25, 0.75, 0.5)
    ca "That was my worst fucking rodeo ever! I couldn't sleep peacefully that night."
    ry "Oh man *laughs*"

    scene v8apes39 # TPP. Mason just walks in through the door. He's looking sleepy and talking
    with dissolve
    ma "Wow, you guys still up?"

    scene v8apes39a # Same as apes39 but mouth closed
    with dissolve
    u "We were just gonna shoot."

    scene v8apes39
    with dissolve
    ma "Well, g'night then. I'm gonna doze off."

    stop music fadeout 3

    scene v8apes40 # FPP. Showing Ryan and Cameron walking out of the den. MC behind them
    with dissolve
    pause 1

    scene v8apes41 # TPP. Showing MC going to bed in his new room in underwear
    with Fade(0.5, 0.5, 0.5)
    pause 1

    scene black
    with Dissolve(1)
    pause 0.5

    jump mc_apes_sun_morn
