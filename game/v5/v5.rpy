init python:
    # Amber messages
    def v5_reply1():
        reputation.add_point(RepComponent.BRO)
        amber.messenger.newMessage(_("Oh really? How are you gonna do that?"))
        amber.messenger.addReply(_("I give some world-class massages"), v5_reply2)
        amber.messenger.addReply(_("I'll stay longer next time"), v5_reply3)

    def v5_reply2():
        reputation.add_point(RepComponent.TROUBLEMAKER)
        amber.messenger.newMessage(_("That does sound enticing ;)"))

    def v5_reply3():
        amber.messenger.newMessage(_("Deal xx"))

    def v5_reply4():
        amber.messenger.newMessage(_("Oh okay, hope everything's okay xx"))
        amber.messenger.addReply(_("Yeah, it's all good."))
        amber.messenger.newMessage(_("Deal xx"))

    def v5_reply5():
        reputation.add_point(RepComponent.BRO)
        amber.messenger.newMessage(_("Oh wow, I was just checking. :P"))
        amber.messenger.addReply(_("Don't worry, you'll see me soon."), v5_reply6)
        amber.messenger.addReply(_("Haha, I'm fine."), v5_reply7)

    def v5_reply6():
        reputation.add_point(RepComponent.TROUBLEMAKER)
        amber.messenger.newMessage(_("Was hoping xx"))

    def v5_reply7():
        amber.messenger.newMessage(_("That's good xx"))

    def v5_reply8():
        amber.messenger.newMessage(_("Oh okay, hope you're good xx"))
        amber.messenger.addReply(_("Yeah, no worries"))
        amber.messenger.newMessage(_("That's good xx"))

    def v5_reply9():
        reputation.add_point(RepComponent.BRO)
        amber.messenger.newMessage(_("Oh shut up, I was just checking in"))
        amber.messenger.addReply(_("Don't worry, you'll see me again"), v5_reply10)
        amber.messenger.addReply(_("Haha, I'm fine"), v5_reply11)

    def v5_reply10():
        reputation.add_point(RepComponent.TROUBLEMAKER)
        amber.messenger.newMessage(_("Was hoping xx"))

    def v5_reply11():
        amber.messenger.newMessage(_("That's good xx"))

    def v5_reply12():
        amber.messenger.newMessage(_("Oh okay, hope you're good xx"))
        amber.messenger.addReply(_("Yeah, no worries"))
        amber.messenger.newMessage(_("That's good xx"))

label ev_a: #for compatibility only
label ev_b: #for compatibility only
label v5start:
    scene s373 # nora approaching
    with dissolve
    play music "music/m16punk.mp3"
    no "What are you doing here? And why did you just punch the wall?"

    menu:
        "It's Chloe":
            scene s374a # nora close up questioning
            with dissolve

            u "*Drunk* It's Chloe... I just- I just wanted to talk to her..."

            u "*Drunk* And now she's all mad and I don't even know what happened."

            scene s374c2 # nora thinking mouth close

            no "Hmmm..."

            scene s374b # mouth open
            with dissolve

            no "Chloe can be a bit overdramatic sometimes, you know."

            no "Maybe she'll calm down by tomorrow."

            scene s374c
            with dissolve

            u "*Drunk* Right..."

            scene s374b
            with dissolve

            no "Hey, it's none of my business, but... what did you guys talk about that made you wanna punch a wall after?"

            menu:
                "Tell her":
                    scene s374c
                    with dissolve

                    u "*Drunk* My uhm, my friend, he- he said that Chloe did some shady shit in the past and I just had to find out the truth!"

                    scene s374d # nora slight laugh, cocky
                    with dissolve

                    no "And what did you find out?"

                    scene s374e
                    with dissolve

                    u "*Drunk* Nothing! I think all I did was ruin our relationship..."

                    scene s374d
                    with dissolve

                    no "Yeah, that sounds about right."

                    scene s374e
                    with dissolve

                    u "*Drunk* What- What do you mean?"

                    scene s374b
                    with dissolve

                    no "Dude, you're drunk, upset and don't even know the whole story. What did you think was gonna happen when you talk to her?"

                    scene s374c
                    with dissolve

                    u "*Drunk* I don't know..."

                    u "*Drunk* What do you mean the whole story?"

                    scene s374d
                    with dissolve

                    no "It's late, I really don't wanna get into it. But hey, let me know how your little love story ends."

                    no "Night, [name]."

                    scene s374e
                    with dissolve

                    u "*Drunk* Night..."

                "Say you gotta go":
                    scene s374c
                    with dissolve

                    u "*Drunk* Uhhh... nothing. It's not important."

                    u "*Drunk* I should uhm... probably go home now, it's late."

                    scene s374d
                    with dissolve

                    no "Alright, well let me know how your little love story ends."

                    no "Night, [name]."

                    scene s374c
                    with dissolve

                    u "*Drunk* Night..."

        "It's nothing":
            scene s374a
            with dissolve

            u "*Drunk* It's- it's nothing. I gotta go, I'll see you around, Nora."

            scene s374b
            with dissolve

            no "Alright, well let's hope you and our house don't get into another fight in the future."

            scene s374c
            with dissolve

            u "*Drunk* Yeah, right..."

    label ev_bd: #for compatibility only
    scene s375 # You walking home
    with Fade (1,0,1)

    u "(Way to mess things up with Chloe... great fucking job, [name].)"

    stop music fadeout 3

    scene s376 # you in bed laying on your side looking at the wall
    with Fade (2,0,2)

    pause 0.5

    scene s376a # you opening your eyes
    with dissolve
    play music "music/mindie1.mp3"

    queue music [ "music/mindie2.mp3", "music/mindie3.mp3" ]

    u "(Oh man, I drank way too much last night...)"
    if volleyball:
        scene s376b # yawning and turning around
        with dissolve

        u "*Yawns*"

        scene s376c # surpisde
        with dissolve

        pause 0.5

        scene s377a # showing volleyball
        with dissolve

        u "(I completely forgot I bought this. I guess I can't really give it to Chloe anymore now, can I?)"

    else:
        scene s376b
        with dissolve

        u "*Yawns*"

    scene s376d # you touching your eye
    with dissolve

    u "(At least my eye is starting to heal...)"

    jump newchloec

    ############ Chloe Talk New

label jorepb:
    scene jonew1 #transition "a bit later", walking to chloe
    with Fade (1,0,1)

    pause 1.0

    scene s368 # knocking on Chloes door
    with Fade (1,0,1)

    play sound "sounds/knock.mp3"

    "*Knock knock knock*"

    play sound "sounds/dooropen.mp3"

    play music "music/msad2.mp3"

    scene s369 # door opening sound chloe inside
    with dissolve

    cl "Hey. You wanna come in?"

    scene s369a
    with dissolve

    u "Hey uh, actually... can we- can we talk outside first? I- I just wanna clear something up."

    scene s369
    with dissolve

    cl "Uhm, yeah of course. Let me just put on my sweater."

    scene s370 # chloe close up outside
    with fade

    cl "So, what did you wanna talk to me about?"

    scene s370a
    with dissolve

    u "Well, Ryan... *deep breath* Ryan said you were playing me and just using me to get back at Grayson."

    scene s370
    with dissolve

    cl "What?? [name], I'm not, that's absurd..."

    scene s370a
    with dissolve

    u "He said Grayson told him about a lot of shady shit that you did in the past."

    scene s370
    with dissolve
    cl "I didn't do anything shady. Grayson is just spreading lies like he always is."

    menu:
        "I believe you":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            scene s370
            with dissolve

            u "I believe you. I just had to make sure, you know?"

            scene clna
            with dissolve

            cl "Yeah, I get that."

            cl "Hey I don't have that much more time tonight, but how about we hang out tomorrow?"

            scene clnb
            with dissolve

            u "Yeah, sounds great. I'll see you then, good night."

            scene clna
            with dissolve

            cl "Good night, [name]."

            scene s375 # You walking home
            with Fade (1,0,1)

            u "(Good thing I didn't get drunk, that could have very easily gone wrong and ended in a big fight with Chloe.)"

            scene s376 # you in bed laying on your side looking at the wall
            with Fade (2,0,2)

            pause 0.5

            scene s376a # you opening your eyes
            with dissolve

            u "(Alright, time for a new day.)"

            if volleyball:
                scene s376b # yawning and turning around
                with dissolve

                u "*Yawns*"

                scene s376c # surpisde
                with dissolve

                pause 0.5

                scene s377a # showing volleyball
                with dissolve

                u "(I completely forgot I bought this. I should give it to Chloe when we hang out later today.)"

            else:
                scene s376b
                with dissolve

                u "*Yawns*"

            scene s376d # you touching your eye
            with dissolve

            u "(Hey, my eye is starting to heal...)"

            jump newchloec

        "You're lying":
            $ CharacterService.set_mood(chloe, Moods.MAD)
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            scene s370a
            with dissolve

            u "You're lying. Yeah sure, the hottest girl in school wants me, the freshman who got beaten up at his first college party."

            scene s370e
            with dissolve

            u "That seems realistic, right?!"

            scene s370d # chloe sad desperate
            with dissolve

            cl "[name], I don't care about the fighting, or any of that shit. What Grayson did to you was pathetic. I like you 'cause you were funny and kind and ... and you cared."

            scene s370e
            with dissolve

            u "Then why did you go after Grayson instead of helping me up when he knocked me out??"

            scene s370d
            with dissolve

            cl "I- I..."

            cl "I told him to stop, okay?? I didn't know if he was gonna hurt you even more."

            scene s370e
            with dissolve

            u "*Ryan said that you just saw his punch as a personal attack and didn't give one fuck about me being hurt. And you know what? Maybe he's right!"

            scene s370d
            with dissolve

            cl "What have I ever done for you not to fucking trust me one bit?!"

            scene s370e
            with dissolve

            u "Apparently a bunch of shady shit in the past!"

            scene s370f # Chloe really sad
            with dissolve

            cl "*Gasp*"

            cl "You know how you can be sure I wasn't just using you?"

            cl "Because if I was using you, I would probably try to seduce you back into trusting me right now."

            cl "But don't worry, I don't want that. We're done."

            scene s371
            with dissolve # scene chloe walking back into her house

            u "Chloe!"

            play sound "sounds/slam.mp3"

            scene s371a
            with hpunch #scene door slam

            "*Door slam*"

            scene s372 # you in front of wall angry
            with dissolve

            u "HNGGGG!"

            play sound "sounds/facepunch1.mp3"

            scene s372a # you punch the wall
            with vpunch

            pause 0.5

            scene s372b # your hand hurts you hold it, it's bloody
            with dissolve

            u "Ah, fuck!"

            unknown "[name], is that you??"

            scene s372c # you turn your head
            with dissolve

            stop music fadeout 3

            " "

            u "Oh shit..."

            scene s373 # nora approaching
            with dissolve
            play music "music/m16punk.mp3"
            no "What are you doing here? And why did you just punch the wall?"

            menu:
                "It's Chloe":
                    scene s374a # nora close up questioning
                    with dissolve

                    u "It's Chloe... I just- I just wanted to talk to her..."

                    u "But it just got out of control..."

                    scene s374c2 # nora thinking mouth close

                    no "Hmmm..."

                    scene s374b # mouth open
                    with dissolve

                    no "Chloe can be a bit overdramatic sometimes, you know."

                    no "Maybe she'll calm down by tomorrow."

                    scene s374c
                    with dissolve

                    u "Right..."

                    scene s374b
                    with dissolve

                    no "Hey, it's none of my business, but... what did you guys talk about that made you wanna punch a wall after?"

                    menu:
                        "Tell her":
                            scene s374c
                            with dissolve

                            u "My uhm, my friend said that Chloe did some shady shit in the past and I just had to find out the truth."

                            scene s374d # nora slight laugh, cocky
                            with dissolve

                            no "And what did you find out?"

                            scene s374e
                            with dissolve

                            u "Nothing! I think all I did was ruin our relationship..."

                            scene s374d
                            with dissolve

                            no "Yeah, that sounds about right."

                            scene s374e
                            with dissolve

                            u "What- What do you mean?"

                            scene s374b
                            with dissolve

                            no "Dude, you're upset and don't even know the whole story. What did you think was gonna happen when you talk to her?"

                            scene s374c
                            with dissolve

                            u "I don't know..."

                            u "What do you mean the whole story?"

                            scene s374d
                            with dissolve

                            no "It's late, I really don't wanna get into it. But hey, let me know how your little love story ends."

                            no "Night, [name]."

                            scene s374e
                            with dissolve

                            u "Night..."

                        "Say you gotta go":
                            scene s374c
                            with dissolve

                            u "Uhhh... nothing. It's not important."

                            u "I should uhm... probably go home now, it's late."

                            scene s374d
                            with dissolve

                            no "Alright, well let me know how your little love story ends."

                            no "Night, [name]."

                            scene s374c
                            with dissolve

                            u "Night..."

                "It's nothing":
                    scene s374a
                    with dissolve

                    u "It's- it's nothing. I gotta go, I'll see you around, Nora."

                    scene s374b
                    with dissolve

                    no "Alright, well let's hope you and our house don't get into another fight in the future."

                    scene s374c
                    with dissolve

                    u "Yeah, right..."

    label nnbd: #for compatibility only
    scene s375 # You walking home
    with Fade (1,0,1)

    u "(Way to mess things up with Chloe... great fucking job, [name].)"

    stop music fadeout 3

    scene s376 # you in bed laying on your side looking at the wall
    with Fade (2,0,2)

    pause 0.5

    scene s376a # you opening your eyes
    with dissolve
    play music "music/mindie1.mp3"

    queue music [ "music/mindie2.mp3", "music/mindie3.mp3" ]

    pause 0.5

    if volleyball:
        scene s376b # yawning and turning around
        with dissolve

        u "*Yawns*"

        scene s376c # surpisde
        with dissolve

        pause 0.5

        scene s377a # showing volleyball
        with dissolve

        u "(I completely forgot I bought this. I guess I can't really give it to Chloe anymore now, can I?)"

    else:
        scene s376b
        with dissolve

        u "*Yawns*"

    scene s376d # you touching your eye
    with dissolve

    u "(At least my eye is starting to heal...)"

label newchloec:
    scene s376e
    with dissolve

    #### Amber text
    play sound "sounds/vibrate.mp3"

    #################

    if amber.relationship >= Relationship.KISS:
        $ amber.messenger.newMessage(_("Hey, it's Amber"), force_send=True)
        $ amber.messenger.newMessage(_("Josh gave me your number"), force_send=True)
        $ amber.messenger.newMessage(_("You know, you never came back, I thought we were having a good time xx"), force_send=True)
        $ amber.messenger.addReply(_("We did, I'll make it up to you."), v5_reply1)
        $ amber.messenger.addReply(_("Sorry, something came up."), v5_reply4)

    elif len(josh.messenger.sent_messages) >= 2 and josh.messenger.sent_messages[-2].reply and josh.messenger.sent_messages[-2].reply.message == "I can't, sorry.":
        $ amber.messenger.newMessage(_("Hey, it's Amber"), force_send=True)
        $ amber.messenger.newMessage(_("Josh gave me your number"), force_send=True)
        $ amber.messenger.newMessage(_("How come you didn't show up yesterday? Everything okay? xx"), force_send=True)
        $ amber.messenger.addReply(_("Wow, you really wanted to see me, huh?"), v5_reply5)
        $ amber.messenger.addReply(_("Sorry, something came up."), v5_reply8)

    else:
        $ amber.messenger.newMessage(_("Hey, it's Amber"), force_send=True)
        $ amber.messenger.newMessage(_("Josh gave me your number"), force_send=True)
        $ amber.messenger.newMessage(_("You know, you never came back, everything okay?"), force_send=True)
        $ amber.messenger.addReply(_("Wow, you really missed me that much, huh?"), v5_reply9)
        $ amber.messenger.addReply(_("Sorry, something came up."), v5_reply12)

    if not toldlauren and not laurentoofar:
        play sound "sounds/vibrate.mp3"

        $ lauren.messenger.newMessage(_("Hey"), force_send=True)
        $ lauren.messenger.newMessage(_("Wanna do the personality tests today at noon?"), force_send=True)
        $ lauren.messenger.addReply(_("Yeah, sure."))
        $ lauren.messenger.newMessage(_("Great :) Meet me at our economics' classroom."))

        u "(Oh shit, I'm getting a bunch of messages.)"

        label phonex:
            if lauren.messenger.replies:
                call screen phone
            if lauren.messenger.replies:
                u "(I should probably reply to some of them.)"
                jump phonex
            
        u "(Time to get ready.)"

    else:
        label phoney:
            if amber.messenger.replies:
                call screen phone
            if amber.messenger.replies:
                u "(Maybe it's Lauren and she wants to talk about what happened? I should definitely check.)"
                jump phoney

        jump continueaf

    ############### Lauren personality tests

label continuez:
    pause 0.5

    scene s377 # in front of class, door is open
    with Fade (1,0,1)

    pause 0.5

    scene s378 # Laurens inside with some papers
    with dissolve

    u "Hey, Lauren."

    scene s379 # lauren (also showing you) walking towards you
    with dissolve

    la "Heyyy."

    # Kiss in public

    if CharacterService.is_girlfriend(lauren):
        scene s379a # lauren kisses you
        with dissolve
        play sound "sounds/kiss.mp3"
        pause 0.5

        scene s380a
        with dissolve

        u "*Chuckles* Is that how we greet each other now?"

        scene s380 #lauren close up smiling
        with dissolve

        la "I mean we are kinda dating and I do enjoy kissing you, so if you don't have any complaints..."

        scene s380a
        with dissolve

        u "(If we kiss in public, other girls are bound to find out that I'm dating Lauren.)"

        menu:
            "Complaints? I love it":
                $ laurenpublic = True
                $ reputation.add_point(RepComponent.BOYFRIEND)

                u "Complaints? I love kissing you. I can't wait till we say goodbye and I can kiss you again. *Laughs*"

                scene s380
                with dissolve

                la "*Tsk* I feel like you saying you can't wait for us to finish hanging out isn't as romantic as you may think."

                scene s380a
                with dissolve

                u "Hahaha, oops."

            "I don't like kissing in public":
                $ reputation.add_point(RepComponent.TROUBLEMAKER)

                u "Uhm, actually do you mind if we don't do that in public?"

                scene s380b # lauren sadish
                with dissolve

                la "Oh... yeah, of course, I'm sorry, I didn't-"

                scene s380c
                with dissolve

                u "It's not that I don't like kissing you, it's just..."

                u "I'm not really into public displays of affection."

                u "It's uhm... how I was raised."

                scene s380d # lauren suspicious
                with dissolve

                la "Oh, and a little kiss like that is already too much?"

                la "I wasn't talking about a full on make out session, haha."

                la "Also, it's not like anyone will see us here."

                scene s380e
                with dissolve

                u "(Shit, she's pushing back. But if I want to avoid other girls finding out about us, I can't just kiss her in public.)"

                menu:
                    "Sorry, not in public":
                        $ reputation.add_point(RepComponent.TROUBLEMAKER)
                        
                        $ grant_achievement("on_the_low")

                        u "Sorry, but can we just make sure we're alone before we do stuff like that. I just feel uncomfortable even just kissing in public."

                        scene s380b
                        with dissolve

                        la "Okay, yeah. No public display of affection, I get it..."

                        scene s380c
                        with dissolve

                    "Actually, a kiss is fine":
                        $ laurenpublic = True

                        u "Actually, you're right, sorry. A kiss is fine."

                        u "Let's just not go overboard, haha."

                        scene s380
                        with dissolve

                        la "Yeah, of course."

                        scene s380f # lauren flirty
                        with dissolve

                        la "At least not in public."

                        scene s380g
                        with dissolve

    else:
        scene s380a
        with dissolve

        u "So, why exactly are we doing this in a classroom?"

        jump continueag

    u "Anyways, why exactly are we doing this in a classroom?"

label continueag:
    scene s380
    with dissolve

    la "Well, my psychology teacher Mrs. Anderson said that she'd leave this room open over the weekend so that we can do the tests on neutral ground."

    scene s380a
    with dissolve

    u "Uhh... neutral ground?"

    scene s380
    with dissolve

    la "You know, your answers can be affected by the environment you're in and an empty classroom should minimize the impact of that."

    scene s380a
    with dissolve

    u "Uhm, sure."

label gotest:
    scene s380
    with dissolve

    la "Alright, let's get started, shall we?"

label gokissb:
    scene s381 #you and lauren sitting across each other lauren with paper in her hand.
    with fade

    pause 0.5

    scene s382 # la looking at you
    with dissolve

    la "So I'll tell you a series of statements and you just tell me if you agree or disagree, okay?"

    scene s382a
    with dissolve

    u "Yeah, sounds good."

    scene s382
    with dissolve

    la "Remember, there is no right or wrong, so just answer honestly."

    scene s382b # la reading of papers
    with dissolve

    la "Statement one: I struggle making difficult decisions."

    menu:
        "Agree":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            $ laurentest.add("q1")

            scene s382a
            with dissolve

            u "Agree."

        "Disagree":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            scene s382a
            with dissolve

            u "Disagree."

    scene s382b
    with dissolve

    la "Two: I consider myself an animal lover."

    menu:
        "Agree":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            $ reputation.add_point(RepComponent.BRO)
            $ laurentest.add("q2")

            scene s382a
            with dissolve

            u "Uhm... agree I guess."

        "Disagree":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            scene s382a
            with dissolve

            u "Hmm... disagree I guess."

            scene s382
            with dissolve

            la "Huh."

    scene s382b # la reading of papers
    with dissolve

    la "Three: I consider myself a relationship person."

    menu:
        "Agree":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            $ laurentest.add("q3")

            scene s382a
            with dissolve

            u "I definitely do."

            if CharacterService.is_girlfriend(lauren):
                scene s382d # Lauren cheeky flirty smile
                with dissolve

                la "Right answer."

                scene s382e
                with dissolve

                u "Woah, I thought there was no right answer."

                scene s382d
                with dissolve

                la "Well, I may have lied about that."

                scene s382e
                with dissolve

                u "*Chuckles* I feel like this personality test is just a pretext so you can vet me."

                scene s382d
                with dissolve

                la "That is certainly a possibility."

                scene s382e
                with dissolve

                u "Am I passing?"

                scene s382d
                with dissolve

                la "So far..."

            else:
                scene s382
                with dissolve

                la "Haha, I thought you were gonna say no."

                scene s382a
                with dissolve

                u "Really? Why?"

                scene s382
                with dissolve

                la "I don't know, you hang out with a lot of different girls, right?"

                scene s382a
                with dissolve

                u "Yeah, but that doesn't mean that I don't just have eyes for one of them."

                scene s382e
                with dissolve

                pause 0.5

        "Disagree":
            $ reputation.add_point(RepComponent.BRO)

            scene s382a
            with dissolve

            u "Not really, sooo... disagree."

            if CharacterService.is_girlfriend(lauren):
                $ reputation.add_point(RepComponent.TROUBLEMAKER)

                scene s382f # Lauren passive agressive
                with dissolve

                la "Well that's good to know."

                scene s382g
                with dissolve

                u "Lauren, it's not like-"

                scene s382f
                with dissolve

                la "Let's just move on."

            else:
                scene s382d
                with dissolve

                la "That's what I thought, haha."

                scene s382e
                with dissolve

                u "Really? Why?"

                scene s382
                with dissolve

                la "I don't know, you hang out with a lot of different girls, right?"

                scene s382a
                with dissolve

                u "Yeah, I guess that's true."

                scene s382e
                with dissolve

                pause 0.5

    scene s382
    with dissolve

    la "So, these were the calibration questions and now we move on to some ethical dilemmas to test your character."

    scene s382a
    with dissolve

    u "What do you mean, test my character?"

    scene s382
    with dissolve

    la "Well we're supposed to cross-reference your answers to these questions with your behavior in difficult situations."

    la "Have you heard of the trolley problem?"

    menu:
        "Yes":
            scene s382a
            with dissolve

            u "Yeah, it's about choosing who the train runs over right?"

            scene s382
            with dissolve

            la "Uhm yeah, that's broadly it."

        "No":
            scene s382a
            with dissolve

            u "Uhm, no I don't think so."

            scene s382
            with dissolve

            la "Hmm, maybe it's best if you just experience it."

    label fa_ad: #for compatibility only
    la "Okay, I want you to rest your head on the table and close your eyes."

    scene s382a
    with dissolve

    u "What? Right now?"

    scene s382
    with dissolve

    la "Yeah. Come on, the personality test is only accurate if you participate."

    scene s382a
    with dissolve

    u "Alright."

    scene black
    with Fade (1,0,0)

    u "So, now what?"

    la "Now, imagine we're on a fast moving train."

    call screen confirm(_("The trolley problem involves hypothetical people and/or animals being run over by a train and can be a lot to handle. The following scene might make you feel uncomfortable or uneasy. Do you wish to skip over the trolley problem scene?"),
        yes_action=[Hide("confirm"), Jump("skiptrolley")],
        no_action=[Hide("confirm"), Jump("continuetrolley")])

label continuetrolley:
    stop music fadeout 3

    play music "sounds/train.mp3"
    scene s383a # you looking at lauren mouth closed on train
    with dissolve

    u "Done."

    scene s383
    with dissolve

    la "Turn to the front, imagine there's a big red lever."

    scene s384
    with dissolve

    u "Okay, yeah."

    if "q1" in laurentest:
        la "You said that you struggle making difficult decisions, let's see how that impacts your behavior in the following situation."

    else:
        la "You said that you don't struggle making difficult decisions, let's see how if that's still true in the following situation."

    la "As the train's moving forward you come closer to an intersection."

    scene s385 #far from intersection
    with dissolve

    la "The train's heading to the right side of the intersection, where five people are scared for their lives."

    scene s386a # closer, right only, people on the right side appear
    with dissolve

    la "Now, you could flick the lever in order for the train to switch to the left track. However, there's also a person scared for their life on that track."

    scene s387 # even closer, person on the left side appears
    with dissolve

    la "Now it's up to you, will you actively decide to kill someone to save five people or will you stand by and see five times as many people die as needed?"

    scene s388a
    with dissolve

    la "You can decide to switch the lever, but remember, you're on a timer. If you don't switch the lever within a few seconds, the train will keep its current course."

    play sound "sounds/countdown.mp3"
    call screen trolleyProblem("trolleyaa", "trolleyab")

label trolleyaa: # you don't press the lever
    stop sound
    $ reputation.add_point(RepComponent.BOYFRIEND)

    scene s388 # hands away from lever
    with dissolve

    pause 0.5

    play sound "sounds/splat.mp3"

    scene s390 # your face full of blood
    with vpunch

    u "Holy fuck..."

    jump continueam

label trolleyab: # you do press the lever
    stop sound
    $ reputation.add_point(RepComponent.BRO)
    play sound "sounds/lever.mp3"
    scene s388e #you press lever
    with dissolve

    pause 0.5

    play sound "sounds/splat.mp3"

    scene s390a # your face full of blood
    with vpunch

    u "Holy fuck..."

label continueam:
    stop music

    scene s382a
    with flash

    u "Jesus, that got pretty intense..."

    scene s382
    with dissolve

    la "I know these questions can be difficult..."

    la "Are you okay with doing another one?"

    menu:
        "Yeah, let's do it":
            scene s382a
            with dissolve

            u "Yeah, let's do it."

            scene s382a
            with dissolve

            la "Alright, imagine yourself back on the train, moving as fast as before."

            scene s383a
            with Fade (1,0,0.5)

            play music "sounds/train.mp3"

            u "Okay, done."

            scene s383
            with dissolve

            la "Look out the front again."

            scene s384
            with dissolve

            u "Alright."

            if "q2" in laurentest:
                la "You said that you consider yourself an animal lover. Let's test how much you really love animals."

            else:
                la "You said that you wouldn't consider yourself an animal lover. Hopefully that'll make the next scenario easier."

            la "As the train's moving forward you come closer to another intersection."

            scene s385 #far from intersection
            with dissolve

            la "The train's heading to the right side of the intersection, where this time only one person's scared for their life."

            scene s386b # closer, woman on the right appears
            with dissolve

            la "Just as last time, you can flick the lever in order for the train to switch to the left track. However, this time there's a dog sitting on the other track."

            scene s387a # even closer, dog on the left side
            with dissolve

            la "Now it's up to you, will you actively decide to kill the dog to save a human life or will you idly stand by and let her die?"

            scene s388b
            with dissolve

            la "You can decide to switch the lever, but remember, you're on a timer. If you don't switch the lever within a few seconds, the train will keep its current course."
            
            play sound "sounds/countdown.mp3"
            call screen trolleyProblem("trolleyba", "trolleybb")

        "I'd rather not":
            jump fb_b

label trolleyba: # you don't press the lever
    stop sound
    $ reputation.add_point(RepComponent.TROUBLEMAKER)
    scene s388 # hands away from lever
    with dissolve

    pause 0.5
    play sound "sounds/splat.mp3"
    scene s390 # your face full of blood
    with vpunch

    u "Ahh fuck!"

    jump continuean

label trolleybb: # you do press the lever
    stop sound
    $ trolleyb = True
    play sound "sounds/lever.mp3"
    scene s388e #you press lever
    with dissolve

    pause 0.5

    play sound "sounds/splat.mp3"

    scene s390a # your face full of blood
    with vpunch

    if "q2" in laurentest:
        $ grant_achievement("peta_public_enemy")

    u "Ahh fuck!"

label continuean:
    stop music

    scene s382a
    with flash

    u "Fucking hell, what is this personality test??"

    scene s382
    with dissolve

    la "Sorry, I know it's a lot but there's only one more to go."
    la "Are you okay with doing the last one?"

    menu:
        "Yeah, okay":
            scene s382a
            with dissolve

            u "Yeah, okay."

            scene s382a
            with dissolve

            la "Alright, imagine yourself back on the train for one last time, moving as fast as before."

            scene s383a
            with Fade (1,0,0.5)
            play music "sounds/train.mp3"

            u "Okay, I'm on the train."

            scene s383
            with dissolve

            la "Look out the front again."

            scene s384
            with dissolve

            u "Sure thing."

            if "q3" in laurentest:
                la "You said that you consider yourself a relationship person, let's put that to the test."

            else:
                la "You said that you wouldn't consider yourself a relationship person, let's put that to the test."

            la "As the train's moving forward you come closer to another intersection."

            scene s385 #far from intersection
            with dissolve

            la "The train's heading to the right side of the intersection, where this time there's five people again, scared for their lives."

            scene s386a
            with dissolve

            la "As always, you can flick the lever in order for the train to switch to the left track. However, this time on the other track it's your ex-girlfriend Emily."

            u "Lauren, what the fuck?! How do you even know about Emily?"

            scene s387b # even closer, emily
            with dissolve

            la "There's no time for this right now. Will you actively decide to kill Emily to save five human lives or will you let the train run it's course, keeping her alive but killing five people in the process?"

            scene s388c
            with dissolve

            la "You can decide to switch the lever, but remember, you're on a timer. If you don't switch the lever within a few seconds, the train will keep its current course."
           
            play sound "sounds/countdown.mp3"
            call screen trolleyProblem("trolleyca", "trolleycb")

        "I'd rather not":

            jump fb_b

label trolleyca: # you don't press the lever
    stop sound
    $ reputation.add_point(RepComponent.BRO)

    scene s388 # hands away from lever
    with dissolve

    pause 0.5

    play sound "sounds/splat.mp3"

    scene s390 # your face full of blood
    with vpunch

    u "Oh my god!"

    jump continueao

label trolleycb: # you do press the lever
    stop sound
    $ reputation.add_point(RepComponent.BOYFRIEND)
    play sound "sounds/lever.mp3"
    scene s388e #you press lever
    with dissolve

    pause 0.5

    play sound "sounds/splat.mp3"

    scene s390a # your face full of blood
    with vpunch

    u "Oh my god!"

label continueao:
    stop music

    scene s382a
    with flash

    u "Lauren, what the fuck?? Emily??"

    scene s382
    with dissolve
    play music "music/mindie5.mp3"

    la "Sorry, I had to ask around in order to find a weak spot. My psych professor said this was essential for the last problem to work."

    menu:
        "At least we're done now":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            scene s382a
            with dissolve

            u "*Sigh* It's okay, at least we're done now."

            scene s382
            with dissolve

            la "Exactly, I'll let you know once I have analyzed the results."

            scene s382d
            with dissolve

            la "In the meantime, I could use a coffee, wanna come with me?"

            scene s382e
            with dissolve

            u "Sorry, Lauren. As much as I'd like to, I gotta pick up Imre from the hospital."

            scene s382
            with dissolve

            la "Oh, alright."

            scene s382a
            with dissolve

            u "I'll see you later, okay?"

            scene s382
            with dissolve

            la "Yeah."

            if laurenpublic:
                la "Are we still gonna kiss goodbye?"

                scene s382a
                with dissolve

                u "Oh yeah, of course."

                scene s392 # you and her accross table
                with dissolve

                pause 0.5

                scene s392a # kiss
                play sound "sounds/kiss.mp3"

                pause 0.5

                scene s392
                with dissolve

                scene s382a
                with dissolve

                u "Alright, bye."

                scene s382
                with dissolve

                la "Bye."

            jump hospitala

        "That was too far":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            scene s382a
            with dissolve

            u "Lauren, that was too fucking far. What are you, some mad scientist?"

            scene s382h # lauren sorry
            with dissolve

            la "[name], I'm sorry, please."

            la "How about we get a coffee and talk about it?"

            scene s382j
            with dissolve

            u "Uhm, I gotta pick up Imre from the hospital now."

            scene s382h
            with dissolve

            la "Oh, okay, yeah."

            scene s382j
            with dissolve

            u "I'll see you later, okay?"

            scene s382h
            with dissolve

            la "Yeah."

            jump hospitala

label skiptrolley:
    scene s382
    with fade

    jump skiptrolleya

    ######## Skip trolley

label fb_b:
    scene s382a
    with dissolve

    u "I'd rather not, can we just move on?"

    scene s382
    with dissolve

    la "Yeah of course."

    label skiptrolleya:

    play music "music/mindie5.mp3"

    la "That'd be all. I'll let you know once I have analyzed the results."

    scene s382d
    with dissolve

    la "In the meantime, I could use a coffee, wanna come with me?"

    scene s382e
    with dissolve

    u "Sorry, Lauren. As much as I'd like to, I gotta pick up Imre from the hospital."

    scene s382
    with dissolve

    la "Oh, alright."

    scene s382a
    with dissolve

    u "I'll see you later, okay?"

    scene s382
    with dissolve

    la "Yeah."

    if laurenpublic:
        la "Are we still gonna kiss goodbye?"

        scene s382a
        with dissolve

        u "Oh yeah, of course."

        scene s392 # you and her accross table
        with dissolve

        pause 0.5

        scene s392a # kiss
        play sound "sounds/kiss.mp3"

        pause 0.5

        scene s392
        with dissolve

        scene s382a
        with dissolve

        u "Alright, bye."

        scene s382
        with dissolve

        la "Bye."

    jump hospitala

    ############ Lauren apology option

label continueaf:
    u "(Damn, it wasn't from Lauren... I wonder if she's still mad at me.)"

    menu:
        "I should go apologize":
            $ apologize = True

            u "(I should go apologize.)"

            if not CharacterService.is_mad(autumn):
                u "(Hopefully Autumn has already put in a good word for me.)"

            scene s393 #you infront of Laurens dorm
            with Fade(1,0,1)

            u "(Alright, this is Lauren's dorm.)"

            scene s393a # you knock
            with dissolve
            play sound "sounds/knock.mp3"

            "*Knock knock knock*"

            scene s393
            with dissolve

            unknown "Who is it?"

            u "It's [name], is Lauren there?"

            if laurentoofar:
                unknown "Oh, you're the fucker that tried to molest her, right?"

                menu:
                    "I'm someone else":
                        $ reputation.add_point(RepComponent.TROUBLEMAKER)

                        u "What? No, I'm just a friend looking for her, where is she?"

                        if reputation() == Reputations.CONFIDENT:
                            call screen reputation_popup

                            unknown "Uhm, alright, she's at some classroom for her personality test thing."

                            u "Thanks"

                        else:
                            unknown "Yeah, right. Fuck off."

                            $ apologize = False

                            u "(Shit, I don't have time to search her all around campus... I guess I'll have to apologize to her another time.)"

                            u "(I should probably pick up Riley so that we can go and get Imre)"

                            jump hospitala

                    "I didn't mean to":
                        $ reputation.add_point(RepComponent.BOYFRIEND)

                        u "I didn't mean to... it was a misunderstanding!"

                        unknown "Yeah, right. Fuck off."
                        $ apologize = False

                        u "(Shit, I don't have time to search her all around campus... I guess I'll have to apologize to her another time.)"

                        u "(I should probably pick up Riley so that we can go and get Imre)"

                        jump hospitala

            else:
                unknown "Oh, you're the guy she cried about, right?"

                unknown "She's not here, I think she's in some classroom for her personality test thing."

        "I'll give her time":
            $ apologize = False

            u "(Maybe I should give her a bit more time.)"

            if not CharacterService.is_mad(autumn):
                u "(Afterall, Autumn said she'd talk to her.)"

            u "(It's probably time to go pick up Imre with Riley anyways.)"

            jump hospitala

    label apo: #for compatibility only
    scene s394 ## you pulling on locked door
    with Fade (1,0,1)

    # locked sound

    "This door's locked."

    scene s395 ## you pulling on locked door2
    with dissolve

    #locked sound

    "Locked..."

    scene s377
    with dissolve

    u "(Huh, this one's open...)"

    scene s378
    with dissolve

    u "Lauren?"

    scene s380b
    with dissolve

    if laurentoofar and CharacterService.is_mad(autumn):
        la "[name], what are you doing here?"

        scene s380c
        with dissolve

        u "Listen, I wanted to apologize, I went too far and I'm sorry."

        u "I- I just got carried away."

        if reputation() == Reputations.LOYAL:
            call screen reputation_popup

            scene s380b
            with dissolve

            la "When you continued pushing your hand up my thigh after I told you I didn't want it, you... you made me feel disgusting."

            la "But I know that you're really sorry and I don't wanna be mad at you."

            la "That's if you're okay with just being friends again for now?"

            scene s380c
            with dissolve

            u "Yeah, of course."

            scene s380
            with dissolve

            la "Good."

            scene s380a
            with dissolve

            u "What are you doing here anyways?"

            scene s380d
            with dissolve

            la "For my psychology class I need someone to do a personality test with me which I can then analyze, but my friend just cancelled on me."

            scene s380e
            with dissolve

            u "I can do it."

            scene s380
            with dissolve

            la "Really? That'd be amazing."

            scene s380a
            with dissolve

            u "Yeah, sure."

            jump gotest

        else:
            $ CharacterService.set_mood(lauren, Moods.MAD)

            la "When you continued pushing your hand up my thigh after I told you I didn't want it, you... you made me feel disgusting."

            la "I trusted you... And you didn't seem to care one bit."

            scene s380c
            with dissolve

            u "Lauren, I-"

            scene s380b
            with dissolve

            la "Please just give me some time. I really don't wanna see you right now."

            scene s380c
            with dissolve

            u "Yeah, of course, sorry."

            u "(Fuck... but it's probably time to go pick up Imre with Riley anyways.)"

            jump hospitala

    elif laurentoofar:
        la "[name], what are you doing here?"

        scene s380c
        with dissolve

        u "Listen, I wanted to apologize, I went too far and I'm sorry."

        u "I- I just got carried away."

        scene s380b
        with dissolve

        la "When you continued pushing your hand up my thigh after I told you I didn't want it, you... you made me feel disgusting."

        la "But my sister helped me understand that you just made a mistake and I really don't wanna be mad you."

        la "That's if you're okay with just being friends again for now?"

        scene s380c
        with dissolve

        u "Yeah, of course."

        scene s380
        with dissolve

        la "Good."

        scene s380a
        with dissolve

        u "What are you doing here anyways?"

        scene s380d
        with dissolve

        la "For my psychology class I need someone to do a personality test with me which I can then analyze, but my friend just cancelled on me."

        scene s380e
        with dissolve

        u "I can do it."

        scene s380
        with dissolve

        la "Really? That'd be amazing."

        scene s380a
        with dissolve

        u "Yeah, sure."

        jump gotest

    elif CharacterService.is_mad(autumn):
        la "[name], what are you doing here?"

        scene s380c
        with dissolve

        u "Listen, I wanted to apologize, I was being insensitive and I'm sorry."

        u "I- I just wanted to be honest with you."

        if reputation() == Reputations.LOYAL:
            call screen reputation_popup

            $ CharacterService.set_relationship(lauren, Relationship.GIRLFRIEND, mc)

            scene s380b
            with dissolve

            la "Thinking of you with another girl made me feel really weird."

            la "But I know that I shouldn't be mad because we weren't technically dating or anything."

            scene s380
            with dissolve

            la "So, how about we just continue where we left off?"

            scene s380a
            with dissolve

            u "Yeah, I'd love that."

            u "And don't worry, now that I know how important this is to you, I'll count it as us dating from now on."

            scene s380
            with dissolve

            la "Good."

            scene s380a
            with dissolve

            u "What are you doing here anyways?"

            scene s380d
            with dissolve

            la "For my psychology class I need someone to do a personality test with me which I can then analyze, but my friend just cancelled on me."

            scene s380e
            with dissolve

            u "I can do it."

            scene s380
            with dissolve

            la "Really? That'd be amazing."

            scene s380a
            with dissolve

            u "Yeah, sure."

            scene s379a
            with dissolve

            play sound "sounds/kiss.mp3"

            pause 0.5

        else:
            scene s380b
            with dissolve

            la "Thinking of you with another girl made me feel really weird."

            la "I don't wanna be mad at you, but can we just put a pause on the whole dating thing for now and go back to just being friends again?"

            scene s380c
            with dissolve

            u "Uhm... yeah, of course."

            scene s380
            with dissolve

            la "Good."

            scene s380a
            with dissolve

            u "What are you doing here anyways?"

            scene s380d
            with dissolve

            la "For my psychology class I need someone to do a personality test with me which I can then analyze, but my friend just cancelled on me."

            scene s380e
            with dissolve

            u "I can do it."

            scene s380
            with dissolve

            la "Really? That'd be amazing."

            scene s380a
            with dissolve

            u "Yeah, sure."

            jump gotest

    else:
        $ CharacterService.set_relationship(lauren, Relationship.GIRLFRIEND, mc)

        scene s380b
        with dissolve

        la "Thinking of you with another girl made me feel really weird."

        la "But my sister really helped me understand that I shouldn't be mad at you for it."

        scene s380
        with dissolve

        la "So, how about we just continue where we left off?"

        scene s380a
        with dissolve

        u "Yeah, I'd love that."

        u "And don't worry, now that I know how important this is to you, I'll count it as us dating from now on."

        scene s380
        with dissolve

        la "Good."

        scene s380a
        with dissolve

        u "What are you doing here anyways?"

        scene s380d
        with dissolve

        la "For my psychology class I need someone to do a personality test with me which I can then analyze, but my friend just cancelled on me."

        scene s380e
        with dissolve

        u "I can do it."

        scene s380
        with dissolve

        la "Really? That'd be amazing."

        scene s380a
        with dissolve

        u "Yeah, sure."

        scene s379a
        with dissolve

        play sound "sounds/kiss.mp3"

        pause 0.5

    label gokiss: #for compatibility only
    scene s380a
    with dissolve

    u "*Chuckles* What was that for?"

    scene s380 #lauren close up smiling
    with dissolve

    la "I mean we are kinda dating again and I felt like kissing you, so if you don't have any complaints..."

    scene s380a
    with dissolve

    u "(If we kiss in public, other girls are bound to find out that I'm dating Lauren.)"

    menu:
        "Complaints? I love it":
            $ laurenpublic = True
            $ reputation.add_point(RepComponent.BOYFRIEND)

            u "Complaints? Kissing you rules."

            scene s380f
            with dissolve

            la "That's what I wanted to hear."

            la "Alright, let's get started with the test, shall we?"

            jump gokissb


        "I don't like kissing in public":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            u "Uhm, actually do you mind if we don't do that in public?"

            scene s380b # lauren sadish
            with dissolve

            la "Oh... yeah, of course, I'm sorry, I didn't-"

            scene s380c
            with dissolve

            u "It's not that I don't like kissing you, it's just..."

            u "I'm not really into public displays of affection."

            u "It's uhm... how I was raised."

            scene s380d # lauren suspicious
            with dissolve

            la "Oh, and a little kiss like that is already too much?"

            la "I wasn't talking about a full on make out session, haha."

            la "Also, it's not like anyone will see us here."

            scene s380e
            with dissolve

            u "(Shit, she's pushing back. But if I want to avoid other girls finding out about us, I can't just kiss her in public.)"

            menu:
                "Sorry, not in public":
                    $ reputation.add_point(RepComponent.TROUBLEMAKER)
                    
                    $ grant_achievement("on_the_low")

                    u "Sorry, but can we just make sure we're alone before we do stuff like that. I just feel uncomfortable even just kissing in public."

                    scene s380b
                    with dissolve

                    la "Okay, yeah. No public display of affection, I get it..."

                    la "Let's just get started with the test."

                    jump gokissb

                "Actually, a kiss is fine":
                    $ laurenpublic = True

                    u "Actually, you're right, sorry. A kiss is fine."

                    u "Let's just not go overboard, haha."

                    scene s380
                    with dissolve

                    la "Yeah, of course."

                    scene s380f # lauren flirty
                    with dissolve

                    la "At least not in public."

                    scene s380g
                    with dissolve

                    u "Hahaha."

                    scene s380f
                    with dissolve

                    la "Let's get started with the test, shall we?"

                    jump gokissb

    ############## Bus to hospital with Riley

label hospitala:
    stop music fadeout 3

    play music "sounds/bus.mp3"
    scene s399 #Riley and and MC are on the bus. They look at each other affectionately. MC readjusts awkwardly.
    with Fade (1,0,1)

    pause 0.5

    scene s399a
    with dissolve

    u "So you think Imre will be alright?"

    scene s400 #Riley close up emphatic
    with dissolve

    ri "You know Imre, he'll be fine. I'm sure once he's fully recovered he'll be twice as strong as before."

    scene s400c # riley gigle mouth closed
    with dissolve

    ri "*Giggles*"

    u "*Laughingly* Yeah, you're right. He's relentless. You should see how he trains me."

    scene s400b
    with dissolve

    ri "I bet that's a show."

    scene s400c
    with dissolve

    u "Yeah... he's got one tough head on his shoulder."

    scene s400d #riley awkward contempalting
    with dissolve

    ri "Yes, yes he does..."

    scene s400e
    with dissolve

    u "Mhmmm..."

    pause 0.5
    stop music fadeout 3

    play sound "sounds/busstop.mp3"

    "*Bus stops*"

    scene s401 # Riley and Mc get out of the bus
    with dissolve

    pause 0.5

    play music "music/m7punk.mp3"

    scene s402 # Imre half limping towards them in front of hospital
    with fade

    u "Aye! Imre."

    scene s403 # Imre close up
    with dissolve

    imre "What's up bro? Hey Riley. Thanks for coming guys."

    scene s404 # Riley close up
    with dissolve

    ri "Yeah, of course."

    scene s405 # Imre hand hug thing with u,
    with dissolve

    play sound "sounds/slap.mp3"
    pause 0.5

    scene s405a # pull in for the hug
    with dissolve

    imre "*Winces in pain*"

    scene s403b # Imre smiling in pain
    with dissolve

    imre "Ah, yeah, shit. Still tryin' to recover."

    scene s403c
    with dissolve

    u "My bad."

    scene s403b
    with dissolve

    imre "It's cool, just a couple of broken ribs."

    scene s403c
    with dissolve

    u "Glad you're feeling a bit better."

    scene s403
    with dissolve

    imre "Yeah, me too."

    scene s404b
    with dissolve

    ri "Alright, I know you two love birds have a lot to catch up on, but I really don't wanna miss the next bus."

    scene s404c
    with dissolve

    imre "*Laughs*"

    u "*Laughingly* Yeah, alright."

    scene s406 #Riley, MC, and Imre walk back to the bus stop.
    with fade

    stop music fadeout 3

    pause 1.0

    scene s407 #Riley, MC, and Imre are now all sitting on the bus towards the back.
    with fade

    play music "sounds/bus.mp3"

    pause 1.0

    scene s408 # A few seats ahead sits a girl that from the back appears to be Emily.
    with dissolve

    pause 1.0

    scene s408a # focus on emily
    with dissolve

    u "(Is that Emily?)"

    play sound "sounds/swoosh.mp3"

    show screen fantasyOverlay

    scene s409 #MC and Emily are in a park, eating ice cream. Emily puts some on MC's nose. MC chases her as she runs away laughing.
    with flash

    pause 0.5

    scene s409a
    with dissolve

    em "You got some ice cream on your nose?"

    scene s409b # both laughing, you wiping the ice cream off
    with dissolve

    u "*Laughs* Hey!"

    play sound "sounds/swoosh.mp3"

    scene s410 #MC and Emily are dancing in the moonlight. MC presses his face into her hair as he holds her.
    with flash

    pause 0.5

    scene s410a # they both look at each other romantically
    with dissolve

    pause 1.0
    play sound "sounds/swoosh.mp3"
    scene s411 #MC and Emily are sitting on the couch watching a movie. Emily has her head on his shoulder.
    with flash

    pause 0.5

    scene s411a #She lifts her head for a moment and stares at him affectionately
    with dissolve

    pause 1.0

    scene s411b #mc looks back at Emily
    with dissolve

    pause 0.5

    u "What?"

    scene s411c
    with dissolve

    em "Nothing."

    scene s411b
    with dissolve

    u "Why are you looking at me like that?"

    scene s411c
    with dissolve

    em "I just love you."

    scene s411b
    with dissolve

    u "I love you too."

    scene s411d #kiss
    with dissolve

    play sound "sounds/kiss.mp3"

    pause 0.5
    play sound "sounds/swoosh.mp3"
    hide screen fantasyOverlay

    scene s408a
    with flash

    u "*Takes a deep breath*"

    scene s413 # you get up
    with dissolve

    u "I'll be right back guys."

    scene s413a # you walking forwards
    with dissolve

    pause 0.5

    scene s414 #he taps fake emily on the shoulder
    with dissolve

    u "Emily?"

    scene s414a # fake emily turns around
    with dissolve

    unknown "Huh?"

    scene s414b
    with dissolve

    u "Oh, sorry, I thought you were someone else."

    scene s415 #mc walks back
    with dissolve

    pause 0.5
    stop music fadeout 3

    scene s416 # Imre, Mc and Riley in front of your dorm
    with Fade(1,0,1)

    ri "I'll see you guys later."

    scene s416a
    with dissolve

    u "Yeah, sounds good."

    scene s416b
    with dissolve

    imre "Bye, Riley."
    
    play music "music/m4punk.mp3"

    scene s417 # you opening dorm door but Imre is walking somewhere else?
    with dissolve

    u "Where are you going?"

    scene s418 #Imre turns around closeup
    with dissolve

    imre "Don't worry about it."

    scene s418a
    with dissolve

    u "Imre-"

    scene s418
    with dissolve

    imre "I said don't worry about it."

    scene s418a
    with dissolve

    u "You really think you're gonna go fight that guy right now? You just got out of the hospital. You need to rest."

    scene s418
    with dissolve

    imre "I'm fine."

    scene s418a
    with dissolve

    u "Imre, you're in no condition to fight!"

    scene s418b # Imre angry
    with dissolve

    imre "I'm not gonna let this motherfucker think he can just come and lay one on me."

    scene s418c
    with dissolve

    u "You ever think if you try and fight like this, he's just gonna lay a second one on you?"

    scene s418b
    with dissolve

    imre "Don't fucking tell me when I can fight or not. I know myself. This is about me and him. I'll make him remember who he's fucking with."

    scene s418c
    with dissolve

    u "Imre, you need to chill out for a second and think this through. You've gone crazy!"

    scene s418b
    with dissolve

    imre "I have thought this through. I'm not gonna sit here looking like a little bitch. I'm gonna make him regret what he did."

    scene s418c
    with dissolve

    u "Look, I get that you want revenge, but you literally just got out of the hospital... if he hits you in the wrong spot that could kill you!"

    scene s418b
    with dissolve

    imre "Whatever, this son of a bitch will pay right now."

    scene s418d # Imre walks away
    with dissolve

    u "Imre! Come on."

    scene s418e # Imre gone
    with dissolve

    u "Fuck..."

    stop music fadeout 3

    scene s419  # u pacing around in room
    with fade

    pause 0.5

    play music "music/m9punk.mp3"
    scene s419a
    with dissolve

    pause 0.5

    scene s419b
    with dissolve

    pause 0.5

    scene s419c # sits down on bed
    with dissolve

    u "*Sighs*"

    scene s419d # pulls out phone
    with dissolve

    pause 0.5

    scene s419e # phone to head
    with dissolve

    play sound "sounds/calling.mp3"

    pause 0.5

    scene s420 # close up head
    with dissolve

    stop sound

    au "Hello?"

    scene s420a
    with dissolve

    u "Uhm... Hey Aubrey."

    scene s420
    with dissolve

    au "Something wrong? You sound tense."

    scene s420a
    with dissolve

    u "Uh... no, no. Everything's good. Uhm... I just had a quick question."

    scene s420
    with dissolve

    au "Yeah? What's up?"

    scene s420a
    with dissolve

    u "Do you uhm... happen to know a guy named Adam?"

    scene s420
    with dissolve

    au "*Hesitates*"

    au "Yeah. Why?"

    scene s420a
    with dissolve

    u "Do you know where he lives?"

    scene s420
    with dissolve

    au "Dorms, corridor B I believe. Why, what happened?"

    scene s420c # face tenses
    with dissolve

    u "Where in corridor B?"

    scene s420b
    with dissolve

    au "Uhm, first door on the left, I think. [name], what's going on?"

    scene s420c
    with dissolve

    u "Wait, did you say, first door on the left?"

    scene s420b
    with dissolve

    au "Yes. Why? Is something wrong? Just tell me!"

    scene s420d #name puts the phone down
    with dissolve

    pause 0.5

    scene s420e # looks at the door
    with dissolve

    pause 0.5

    scene s421 # show door
    with dissolve

    u "*Mumbles* That's right across from us."

    scene s420f # phone back at his head
    with dissolve

    au "Hello? Is everything okay??"

    scene s420g
    with dissolve

    u "Hey, sorry, I'll call you back Aubrey. I gotta go."

    scene s420e # phone away from ear
    with dissolve

    au "Don't-"

    scene s420e2 # phone away from ear
    with dissolve

    play sound "sounds/rejectcall.mp3"

    u "*Hangs up*"

    scene s422 # mc charges towards door
    with dissolve

    pause 0.5

    scene s396
    with dissolve

    pause 0.5

    scene s396a
    with dissolve

    u "*Deep breath*"

    label fj_a: #for compatibility only
    label fj_b: #for compatibility only

    menu:
        "Confront Adam":
            $ reputation.add_point(RepComponent.BRO)

            scene s397
            with dissolve

            play sound "sounds/knock.mp3"

            "*Knock knock knock*"

            play sound "sounds/dooropen.mp3"

            scene s398
            with dissolve

            ad "Wrong dorm, pissbag. Now fuck off."

            menu:
                "Punch him":
                    $ fightadam = True
                    $ reputation.add_point(RepComponent.TROUBLEMAKER)

                    jump fk_a

                "Talk to him":
                    $ reputation.add_point(RepComponent.BOYFRIEND)

                    scene s398a
                    with dissolve

                    u "You're Adam, right? Look, you beat up my friend Imre and-"

                    scene s398b
                    with dissolve

                    ad "Ahh yeah, I remember, that was quite fun."

                    scene s398
                    with dissolve

                    ad "So what are you gonna do about it, bitch?"

                    menu:
                        "Punch him":
                            $ fightadam = True
                            $ reputation.add_point(RepComponent.TROUBLEMAKER)

                            jump fk_a

                        "Threaten to tell school":
                            $ reputation.add_point(RepComponent.BOYFRIEND)

                            scene s398a
                            with dissolve

                            u "You find him and apologize or I'll tell the fucking school and you'll get kicked out and maybe even assault charges thrown your way."

                            scene s398
                            with dissolve

                            ad "You do that and I'll come back for you and unlike your friend, you'll never leave the fucking hospital again."

                            ad "Now fuck off."

                            play sound "sounds/slam.mp3"

                            scene s398c
                            with vpunch

                            u "(Fuck...)"

                            u "(Great, if I tell the school about this, Imre will be pissed at me and Adam will try to fucking kill me, but if I don't, Imre is gonna get himself killed trying to get revenge.)"

                            menu:
                                "Tell the school":
                                    $ tellschool = True
                                    $ reputation.add_point(RepComponent.BOYFRIEND)

                                    jump fl_a

                                "Keep it to yourself":
                                    $ reputation.add_point(RepComponent.BRO)

                                    jump fl_b

        "Leave it":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            scene s397b
            with dissolve

            u "(It's not like I can do anything against him anyways...)"
            u "(Maybe I should tell the school, but Imre would be super pissed and Adam might try and kill me for it.)"
            u "(On the other hand, if I don't tell the school Imre might actually get himself killed trying to get revenge.)"

            menu:
                "Tell the school":
                    $ tellschool = True
                    $ reputation.add_point(RepComponent.BOYFRIEND)
                    jump fl_a

                "Keep it to yourself":
                    $ reputation.add_point(RepComponent.BRO)
                    jump fl_b

########## Adam fight

    label fk_a:
    stop music fadeout 3
    image af2 = Movie(play="images/v5/af2.webm", start_image="images/v5/af2start.webp", image="images/v5/af2pic.webp", loop = False)


    play sound "sounds/hs.mp3"
    scene af0close
    with hpunch

    pause 0.5

    scene af1
    with dissolve

    ad "Oh pissbag, you're about to die."

    scene af2
    pause 1.5
    scene af2pic
    with hpunch

    pause 0.5

    scene af4
    with dissolve

    pause 0.5

    $ adamtut = True


    label fkcon:

    $ firstfight = False

    scene af4

    # TODO: Update Adam Fight
    call screen confirm(_("Would you like to play the fighting tutorial?"),
        yes_action=[SetVariable("fight_tutorial", True), Call("fight_tutorialLabel")],
        no_action=[SetVariable("fight_tutorial", False), Return()])

    scene af4

    call screen fight_typeMenu

    if fight_type == "normal":
        $ simadamfight = False

        call screen fight_selectDifficulty

        call screen fight_keybindOptions
    
    elif fight_type == "simReal" or fight_type == "simWin":
        $ simadamfight = True
        
    $ stance = 1
    $ adamstance = renpy.random.choice([1, 2, 3, 4])
    $ adamattack = renpy.random.choice([1, 2, 3, 4])
    $ simadam = renpy.random.choice([1, 2, 3, 4, 5, 6])
    $ simyou = renpy.random.choice([1, 2, 3, 4, 5, 6])

    if fight_type == "simWin":
        $ youHealth = 100000
    else:
        $ youHealth = 3

    $ enemyhealth = 6
    $ youDamage = 0
    $ adamdmg = 0

    label letsgoadam:
    label adamsimstart:
    label adamattack:
    $ stance = 2

    if youDamage >= youHealth:

        scene adamfinish
        $ renpy.pause(1.3)
        play sound "sounds/fall.mp3"
        $ stance = 0
        $ youDamage = 0
        scene adamfinishclose
        with vpunch

        $ renpy.pause()


        jump adamfinish

    else:

        if adamattack == 1:

            scene af13
            $ renpy.pause(0.6)

            scene af13pic
            $ adamstance = renpy.random.choice([1, 2, 3, 4])
            $ simyou = renpy.random.choice([1, 2, 3, 4, 5, 6])

            if simadamfight:
                if simadam == 1 or simadam == 2 or simadam == 3:
                    jump adamhookhit
                if simadam == 4 or simadam == 5 or simadam == 6:
                    jump adamhookblocked

            else:
                call screen adamattack




        if adamattack == 2:

            scene af14
            $ renpy.pause(0.5)

            scene af14pic
            $ adamstance = renpy.random.choice([1, 2, 3, 4])
            $ simyou = renpy.random.choice([1, 2, 3, 4, 5, 6])

            if simadamfight:
                if simadam == 1 or simadam == 2 or simadam == 3:
                    jump adamjabhit
                if simadam == 4 or simadam == 5 or simadam == 6:
                    jump adamjabblocked

            else:
                call screen adamattack

        if adamattack == 3:

            scene af15
            $ renpy.pause(0.7)

            scene af15pic
            $ adamstance = renpy.random.choice([1, 2, 3, 4])
            $ simyou = renpy.random.choice([1, 2, 3, 4, 5, 6])

            if simadamfight:
                if simadam == 1 or simadam == 2 or simadam == 3:
                    jump adambodyhit
                if simadam == 4 or simadam == 5 or simadam == 6:
                    jump adambodyblocked

            else:
                call screen adamattack

        if adamattack == 4:

            scene af16
            $ renpy.pause(0.6)

            scene af16pic
            $ adamstance = renpy.random.choice([1, 2, 3, 4])
            $ simyou = renpy.random.choice([1, 2, 3, 4, 5, 6])

            if simadamfight:
                if simadam == 1 or simadam == 2 or simadam == 3:
                    jump adamkickhit
                if simadam == 4 or simadam == 5 or simadam == 6:
                    jump adamkickblocked

            else:
                call screen adamattack


    label adamhookhit:

        play sound "sounds/hs.mp3"
        $ youDamage += 1
        scene adamhookhit
        with hpunch

        pause 0.5
        $ stance = 1
        $ adamattack = renpy.random.choice([1, 2, 3, 4])
        $ simadam = renpy.random.choice([1, 2, 3, 4])

        if simadamfight:
            if adamstance == 1:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamjab1
            if adamstance == 2:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamjab2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamhook1
            if adamstance == 3:
                if simyou == 1:
                    jump adamjab2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adambody1
            if adamstance == 4:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamjab2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamkick1
        else:
            call screen youattack2

    label adamhookblocked:

        play sound "sounds/bs.mp3"
        scene adamhookblock
        with hpunch

        pause 0.5
        $ stance = 1
        $ adamattack = renpy.random.choice([1, 2, 3, 4])
        $ simadam = renpy.random.choice([1, 2, 3, 4])

        if simadamfight:
            if adamstance == 1:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamjab1
            if adamstance == 2:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamjab2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamhook1
            if adamstance == 3:
                if simyou == 1:
                    jump adamjab2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adambody1
            if adamstance == 4:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamjab2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamkick1
        else:
            call screen youattack2

    label adamjabhit:

        play sound "sounds/js.mp3"
        $ youDamage += 1
        scene adamjabhit
        with hpunch

        pause 0.5
        $ stance = 1
        $ adamattack = renpy.random.choice([1, 2, 3, 4])
        $ simadam = renpy.random.choice([1, 2, 3, 4])

        if simadamfight:
            if adamstance == 1:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamjab1
            if adamstance == 2:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamjab2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamhook1
            if adamstance == 3:
                if simyou == 1:
                    jump adamjab2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adambody1
            if adamstance == 4:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamjab2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamkick1
        else:
            call screen youattack2

    label adamjabblocked:

        play sound "sounds/bs.mp3"
        scene adamjabblock
        with hpunch

        pause 0.5
        $ stance = 1
        $ adamattack = renpy.random.choice([1, 2, 3, 4])
        $ simadam = renpy.random.choice([1, 2, 3, 4])

        if simadamfight:
            if adamstance == 1:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamjab1
            if adamstance == 2:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamjab2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamhook1
            if adamstance == 3:
                if simyou == 1:
                    jump adamjab2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adambody1
            if adamstance == 4:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamjab2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamkick1
        else:
            call screen youattack2

    label adambodyhit:

        play sound "sounds/hs.mp3"
        $ youDamage += 1
        scene adambodyhit
        with hpunch

        pause 0.5
        $ stance = 1
        $ adamattack = renpy.random.choice([1, 2, 3, 4])
        $ simadam = renpy.random.choice([1, 2, 3, 4])

        if simadamfight:
            if adamstance == 1:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamjab1
            if adamstance == 2:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamjab2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamhook1
            if adamstance == 3:
                if simyou == 1:
                    jump adamjab2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adambody1
            if adamstance == 4:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamjab2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamkick1
        else:
            call screen youattack2

    label adambodyblocked:

        play sound "sounds/bs.mp3"
        scene adambodyblock
        with hpunch

        pause 0.5
        $ stance = 1
        $ adamattack = renpy.random.choice([1, 2, 3, 4])
        $ simadam = renpy.random.choice([1, 2, 3, 4])

        if simadamfight:
            if adamstance == 1:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamjab1
            if adamstance == 2:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamjab2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamhook1
            if adamstance == 3:
                if simyou == 1:
                    jump adamjab2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adambody1
            if adamstance == 4:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamjab2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamkick1
        else:
            call screen youattack2

    label adamkickhit:

        play sound "sounds/ks.mp3"
        $ youDamage += 1
        scene adamkickhit
        with hpunch

        pause 0.5
        $ stance = 1
        $ adamattack = renpy.random.choice([1, 2, 3, 4])
        $ simadam = renpy.random.choice([1, 2, 3, 4])

        if simadamfight:
            if adamstance == 1:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamjab1
            if adamstance == 2:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamjab2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamhook1
            if adamstance == 3:
                if simyou == 1:
                    jump adamjab2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adambody1
            if adamstance == 4:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamjab2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamkick1
        else:
            call screen youattack2

    label adamkickblocked:

        play sound "sounds/ks.mp3"
        scene adamkickblock
        with hpunch

        pause 0.5
        $ stance = 1
        $ adamattack = renpy.random.choice([1, 2, 3, 4])
        $ simadam = renpy.random.choice([1, 2, 3, 4])

        if simadamfight:
            if adamstance == 1:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamjab1
            if adamstance == 2:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamjab2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamhook1
            if adamstance == 3:
                if simyou == 1:
                    jump adamjab2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adambody1
            if adamstance == 4:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamjab2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamkick1
        else:
            call screen youattack2

    label adamkick1:

        if adamdmg >= enemyhealth:

            scene youfinishadam
            $ renpy.pause(1)
            play sound "sounds/fall.mp3"
            $ stance = 0
            $ youDamage = 0
            scene youfinishadamclose
            with vpunch
            $ renpy.pause()

            jump youfinishadam

        else:
            $ adamdmg += 1
            scene af11
            $ renpy.pause(0.7)
            play sound "sounds/ks.mp3"
            scene af11close
            with hpunch

            pause 0.5
            jump adamattack

    label adamkick2:

            scene af12
            $ renpy.pause(0.7)
            play sound "sounds/ks.mp3"
            scene af12close
            with hpunch

            pause 0.5
            jump adamattack


    label adamhook1:

        if adamdmg >= enemyhealth:

            scene youfinishadam
            $ renpy.pause(1)
            play sound "sounds/fall.mp3"
            $ stance = 0
            $ youDamage = 0
            scene youfinishadamclose
            with vpunch
            $ renpy.pause()

            jump youfinishadam

        else:
            $ adamdmg += 1
            scene af5
            $ renpy.pause(0.7)
            play sound "sounds/hs.mp3"
            scene af5close
            with hpunch

            pause 0.5
            jump adamattack

    label adamhook2:

            scene af6
            $ renpy.pause(0.7)
            play sound "sounds/bs.mp3"
            scene af6close
            with hpunch

            pause 0.5
            jump adamattack

    label adamjab1:

        if adamdmg >= enemyhealth:

            scene youfinishadam
            $ renpy.pause(1)
            play sound "sounds/fall.mp3"
            $ stance = 0
            $ youDamage = 0
            scene youfinishadamclose
            with vpunch
            $ renpy.pause()

            jump youfinishadam

        else:
            $ adamdmg += 1
            scene af7
            $ renpy.pause(0.7)
            play sound "sounds/js.mp3"
            scene af7close
            with hpunch

            pause 0.5
            jump adamattack

    label adamjab2:

            scene af8
            $ renpy.pause(0.7)
            play sound "sounds/bs.mp3"
            scene af8close
            with hpunch

            pause 0.5
            jump adamattack

    label adambody1:

        if adamdmg >= enemyhealth:

            scene youfinishadam
            $ renpy.pause(1)
            play sound "sounds/fall.mp3"
            $ stance = 0
            $ youDamage = 0
            scene youfinishadamclose
            with vpunch
            $ renpy.pause()

            jump youfinishadam

        else:
            $ adamdmg += 1
            scene af9
            $ renpy.pause(0.7)
            play sound "sounds/hs.mp3"
            scene af9close
            with hpunch

            pause 0.5
            jump adamattack

    label adambody2:

            scene af10
            $ renpy.pause(0.7)
            play sound "sounds/bs.mp3"
            scene af10close
            with hpunch

            pause 0.5
            jump adamattack

label fl_b: # keep it to yourself
    u "(It's best if I keep to myself. Telling the school would turn both Imre and Adam against me...)"

    stop music fadeout 3

    u "(I need to find Imre before he finds Adam.)"

    jump findimre

label fl_a:  # tell the school
    $ tellschool = True

    stop music fadeout 3

    $ grant_achievement("snitch")

    u "(I need to tell the school, it's the only way to sort this out.)"

    scene s423 #mc before counselors office, opening door
    with Fade(1,0,1)
    play sound "sounds/dooropen.mp3"
    pause 0.5
    play music "music/m15punk.mp3"
    scene s424 #cam behind MC walks into the counselor's office. She is sitting at her desk.
    with dissolve

    co "Have a seat."

    scene s425 # counselor smiloing close up
    with dissolve

    co "How can I help you today?"

    scene s425a
    with dissolve

    u "Well, kinda hard to say. Not trying to start any issues, but I need to protect my friend."

    scene s425b # counselor contemplating
    with dissolve

    co "Mhm. I see. I can only help you, if you tell me the problem. Also you can be assured that whatever you tell me, your identity will be kept confidential. Feel free to share what's weighing on you."

    scene s425c
    with dissolve

    u "A close friend of mine got jumped by this guy. He got beat up pretty bad, broken ribs and all."

    scene s425b #counselor empathy
    with dissolve

    co "I'm very sorry to hear that."

    scene s425c
    with dissolve

    u "And now my friend, who isn't even fully recovered, is out trying to get revenge. He was this close to internal bleeding last time, if he gets beat up again..."

    scene s425b
    with dissolve

    co "I understand. I'll do my best to ensure your friend does not suffer any more violence."

    co "What is your friend's name?"

    scene s425c
    with dissolve

    u "Imre, Imre Varga."

    scene s425b
    with dissolve

    co "And do you happen to know the name of the other person involved? Assault is a serious crime."

    scene s425c
    with dissolve

    u "Uh yeah, his name's Adam. I don't know his last name, but he lives in corridor B."

    scene s425
    with dissolve

    co "Thank you, that will be all. I'm sorry about what happened to your friend, please try and keep a close eye on him until we can get this all sorted."

    scene s425a
    with dissolve

    u "So uhm... what will happen to Adam?"

    scene s425b
    with dissolve

    co "That won't be up to me, but expulsion is definitely a possibility."
    co "If your friend is willing to pursue this legally, I'd assume assault charges might also be on the table. However, I'm not a lawyer, so I can't speak with certainty on that."

    scene s425c
    with dissolve

    u "Alright, thanks. No one will know that I was the one who told you about this, right?"

    scene s425
    with dissolve

    co "Of course not. Your name will remain strictly confidential."

    scene s426 # Mc stands up
    with dissolve

    u "Good, thank you."

    scene s426a # mc walks away
    with dissolve

    co "You made the right decision coming here."

    scene s426b #mc turns around
    with dissolve

    u "Sorry?"

    scene s426c #co tlaking with mc turned around she's smiling and convinced / reassuring
    with dissolve

    co "A lot of students never tell us about their problems until it's too late to solve them. It's not \"uncool\" or \"cowardly\" to speak up."
    co "It's brave."

    scene s426b
    with dissolve

    u "Uhm, thanks."

    scene s426a # mc walks away
    with dissolve

    stop music fadeout 3

    u "(I need to find Imre.)"

    jump findimre

label youfinishadam: #### You beat adam
    $ renpy.end_replay()
    $ winadam = True

    pause 0.5

    u "Never touch Imre again, you piece of shit."

    play music "music/m12punk.mp3"

    scene s427 #you in front of your dorm door about to open the door
    with dissolve

    unknown "Yo, did I just watch you knock out Adam?"

    scene s427a #you turn around
    with dissolve

    u "Look, he-"

    scene s428a #chrisclose up mouth closed impressed smile
    with dissolve

    u "Oh shit, you're Chris, President of the Wolves, right?"

    scene s428
    with dissolve

    ch "Yeah, and you're a freshman. How the hell did you manage to beat up Adam?"

    scene s428a
    with dissolve

    u "I don't know... I don't normally fight, it's just..."

    u "He hurt my friend."

    scene s428
    with dissolve

    ch "Christ man, you're a natural. Have you considered joining a frat?"

    menu:
        "Yeah, I'm interested":
            $ reputation.add_point(RepComponent.BRO)

            scene s428a
            with dissolve

            u "Yeah, I'm definitely interested. Especially in the Wolves."

            scene s428b #chris convincing
            with dissolve

            ch "That's what I like to hear. Not a single freshman last year could have beaten up Adam. I assume you're gonna be at our rush party on Tuesday?"

            scene s428a
            with dissolve

            u "Yeah, I'll definitely be there."

            scene s428
            with dissolve

            ch "Cool, I'll see you then. Come talk to me when you're there."

            scene s428a
            with dissolve

            u "Yeah, will do."

            scene s427
            with dissolve

            stop music fadeout 3

            u "(Actually, I should probably go find Imre and tell him about what happened.)"

            jump findimre

        "Not really":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            scene s428a
            with dissolve

            u "Not really, I'm not a fighter, okay? This was a one time thing, I had no choice."

            scene s428b #chris convincing / understanding
            with dissolve

            ch "Not a single freshman last year could have beaten up Adam. You have talent, man. Come to our rush party on Tuesday, I promise you, you won't regret it."

            scene s428a
            with dissolve

            u "I promised my friend I'd go anyways. So yeah, I'll be there."

            scene s428
            with dissolve

            ch "That's good. I'll see you then, come talk to me when you're there."

            scene s428a
            with dissolve

            u "Yeah, will do."

            scene s427
            with dissolve

            u "(Actually, I should probably go find Imre and tell him about what happened.)"

            jump findimre

label adamfinish: ###Adam beats you
    $ renpy.end_replay()
    $ winadam = False

    pause 1.0
    play music "music/m12punk.mp3"

    scene s429 # showing Adam kicking you on the ground
    with vpunch

    u "*winces in pain*"

    scene s430 #FIRST PErson: looking at Adam spitting on you
    with dissolve
    play sound "sounds/spit.mp3"
    ad "*Spits*"

    scene s430b #adam disgusting grin
    with dissolve

    ad "You really thought you could beat me up, huh?"

    scene s429 # showing Adam kicking you on the ground
    with vpunch

    u "*winces in pain* Ahhh!"

    scene s430b
    with dissolve

    ad "Let's see how many ribs you're gonna break today."

    scene s430c
    with dissolve

    unknown "Leave him alone, Adam!"

    scene s431 # First Person : Looking at chris approaching from the doors (you're still on the ground)
    with dissolve

    ch "Or I'll beat you up myself."

    scene s430d # adam looking at chris (your bottom perspective stillk)
    with dissolve

    ad "You think I'm scared of you, Chris?"

    scene s432 # no longer your perspective: Chris and Adam about 1-2 metres apart staring each other down.
    with dissolve

    pause 1.0

    scene s432a
    with dissolve

    ch "Step. Away."

    scene s432
    with dissolve

    pause 0.5

    scene s432b # Adam walks back to his dorm
    with dissolve

    pause 0.5

    scene s433 # FIRST PERSON: Chris reaches with his hand to help you up
    with dissolve

    ch "You okay?"

    scene s433a # you grab his hand
    with dissolve

    u "Yeah, thanks."

    scene s428c
    with dissolve

    u "You're Chris, President of the Wolves, right?"

    scene s428b
    with dissolve

    ch "Yeah, that's me."

    ch "So, why did Adam wanna beat you up? Did you look at him the wrong way?"

    scene s428c
    with dissolve

    u "He beat up my friend. And when I confronted him, I just kinda lost it and punched him."

    scene s428b
    with dissolve

    ch "Fair enough. Do you fight a lot?"

    scene s428c
    with dissolve

    u "Not really. That's probably why I was the one on the ground and not him."

    scene s428b
    with dissolve

    ch "Trust me, not a single freshman last year could have beaten up Adam. He's not an easy opponent."

    scene s248c
    with dissolve

    u "Yeah..."

    scene s428b
    with dissolve

    ch "Look, people like Adam... they don't stop. At some point he'll find you by yourself and he'll try to fuck you up even more."

    ch "You should come to our rush party on Tuesday. As a Wolf, you'll learn how to defend yourself."

    scene s428c
    with dissolve

    u "Really? You see me get beaten up and you still want me to join the Wolves, who's only requirement for joining is being good at fighting?"

    scene s428b
    with dissolve

    ch "Well, you gave him a nosebleed, so you must have landed at least one good punch."

    ch "Also, fighting can be learned. We care about loyalty. And you trying to avenge your friend like that, without much fighting experience, that's honorable."

    ch "So, Tuesday?"

    scene s428c
    with dissolve

    u "Alright, I'll be there."

    scene s428
    with dissolve

    ch "Good, I'll see you then. Come talk to me when you're there."

    scene s428a
    with dissolve

    u "Yeah, will do."

    scene s427
    with dissolve

    u "(Actually, I should probably go find Imre and tell him about what happened.)"

    stop music fadeout 3

    u "(But first, I gotta wash the blood of my face.)"

label findimre:
    play music "music/m16punk.mp3"

    #### montage of you looking for Imre

    scene s434 #looking somewhere on campus
    with fade

    u "Imre?"

    scene s435 # talking to Elijah on campus
    with Dissolve (1)

    u "Have you seen Imre?"

    scene s436 # looking else where on campus
    with Dissolve (1)

    u "Imreee? Are you here?"

    scene s437 # talking to Mr. Lee
    with Dissolve (1)

    u "Mr. Lee, any chance you've seen Imre?"

    scene s438 # you looking into caferita seeing imre dissapointed sitting on a table
    with Dissolve (1)

    u "Imre, there you are!"

    scene s439 # Imre close up mad
    with dissolve

    imre "I can't fucking find him. He must be hiding or some shit. No one seems to know where he lives either."
    imre "Fucking bullshit, they're all just scared of him!"

    scene s439a
    with dissolve

    if fightadam and winadam:
        $ CharacterService.set_mood(imre, Moods.MAD)
        
        u "Actually, I uhm... I found Adam."

        scene s439b # Imre surprised but still a bit mad
        with dissolve

        imre "Where? Where is he?"

        scene s439c
        with dissolve

        u "He lives in the dorm opposite to us. But I already paid him a visit."

        scene s439b
        with dissolve

        imre "Fuck you mean you paid him a visit?"

        scene s439c
        with dissolve

        u "I beat him up. Knocked him out. Told him to leave you alone."

        scene s439
        with dissolve

        imre "You did what?! What the fuck is wrong with you?!"

        scene s439a
        with dissolve

        u "What?? That's what you wanted, right? He got beaten up."

        scene s440 # Imre stands up angry
        with dissolve

        imre "I wanted to beat him up! He was mine! You knew he was mine!"

        scene s440a
        with dissolve

        u "Imre, I-"

        scene s440
        with dissolve

        imre "You pretend like you're not a fighter, like you're not a Wolf..."

        imre "Well turns out you were right about one of those. Go join the fucking Apes!"

        scene s441 # Imre storms off
        with dissolve

        u "Imre!"

        scene s441a # Imre gone
        with dissolve

        u "Fuck!"

    elif fightadam:
        u "Actually, I uhm... I found Adam."

        scene s439b # Imre surprised but still a bit mad
        with dissolve

        imre "Where? Where is he?"

        scene s439c
        with dissolve

        u "He lives in the dorm opposite to us. I confronted him when I found out, but it got out of control and he beat me up."

        u "Luckily Chris stepped in, otherwise he would've sent me to the hospital as well."

        scene s439d # Imre slight cocky smile
        with dissolve

        imre "Well that was fucking stupid of you, wasn't it?"

        imre "I told you, I don't need your help, I got this."

        scene s439e
        with dissolve

        u "Yeah sorry, it's just... I don't wanna pick you up from the hospital again."

        scene s439d
        with dissolve

        imre "I'll get a cab next time."

        scene s439e
        with dissolve

        u "You know that's not what I meant."

        scene s439f # imre serious
        with dissolve

        imre "Look, I really appreciate that you're trying to help, but I know what I'm doing, okay?"

        scene s439g
        with dissolve

        u "Okay."

        u "Are you gonna try and fight him now?"

        scene s439f
        with dissolve

        imre "I have to do this."

        scene s439g
        with dissolve

        u "Can I at least-"

        scene s439f
        with dissolve

        imre "[name], please. Go take a walk. Let me handle this myself."

        scene s439g
        with dissolve

        u "Alright. Good luck, man."

    elif tellschool:
        $ CharacterService.set_mood(imre, Moods.MAD)
        
        u "Actually, I uhm... I found Adam."

        scene s439b # Imre surprised but still a bit mad
        with dissolve

        imre "Where? Where is he?"

        scene s439c
        with dissolve

        u "He lives in the dorm opposite to us. But there's something else I need to tell you."

        u "I told the school about what happened. They're gonna take care of it."

        scene s439
        with dissolve

        imre "You did what?! What the fuck is wrong with you?!"

        scene s439a
        with dissolve

        u "Look, I know that's not what you wanted, but-"

        scene s440 # Imre stands up angry
        with dissolve

        imre "I told you to stay out of it! Now if I touch him the school will kick both of us out!"

        scene s440a
        with dissolve

        u "Imre, I-"

        scene s440
        with dissolve

        imre "I knew you weren't a fucking fighter, but I didn't know you were such a snitch!"

        imre "Stay the fuck out of my life!"

        scene s441 # Imre storms off
        with dissolve

        u "Imre!"

        scene s441a # Imre gone
        with dissolve

        u "Fuck!"

    else:
        u "Actually, I uhm... I found Adam."

        scene s439b # Imre surprised but still a bit mad
        with dissolve

        imre "Where? Where is he?"

        scene s439c
        with dissolve

        u "You really wanna know? He lives in the dorm opposite to us."

        u "But you can't do this, man! At least not by yourself, let me come with you and we'll take him on together."

        scene s439d # Imre slight cocky smile
        with dissolve

        imre "I told you, I don't need your help, I got this."

        scene s439e
        with dissolve

        u "I get that, but... I don't wanna pick you up from the hospital again."

        scene s439d
        with dissolve

        imre "I'll get a cab next time."

        scene s439e
        with dissolve

        u "You know that's not what I meant."

        scene s439f # imre serious
        with dissolve

        imre "Look, I really appreciate that you're trying to help, but I know what I'm doing, okay?"

        scene s439g
        with dissolve

        u "Okay."

        u "Are you gonna try and fight him now?"

        scene s439f
        with dissolve

        imre "I have to do this."

        scene s439g
        with dissolve

        u "Can I at least-"

        scene s439f
        with dissolve

        imre "[name], please. Go take a walk, distract yourself. Let me handle this myself."

        scene s439g
        with dissolve

        u "Alright. Good luck, man."

    label continueba: #for compatibility only
    stop music fadeout 3

    scene s442 # you on a park bench depressed
    with Fade (1,0,1)
    play music "music/mindie1.mp3"

    queue music [ "music/mindie2.mp3", "music/mindie3.mp3" ]

    if CharacterService.is_mad(imre):
        u "(How the fuck did everything go so wrong??)"
        u "(A couple hours ago Imre was so happy to see me and now he probably hates me...)"

        u "(I need to go and talk to him again. He's probably in our dorm.)"

    else:
        u "(What am I doing? Adam could be beating Imre senseless at our dorms right now.)"

        u "(I know Imre said he didn't want me to help him, but I can't just do nothing.)"

    ##text message # You can text Amber you don't have time for this.

    scene s442a # you stand up
    with dissolve

    play sound "sounds/vibrate.mp3"

    u "(Maybe that's Imre...)"

    if CharacterService.is_mad(chloe):
        $ amber.messenger.newMessage(_("Hey, you alone? xx"), force_send=True)
        $ amber.messenger.addReply(_("I'm at the park, but I'm by myself."))
        $ amber.messenger.newMessage(_("Go somewhere where you're completely alone xx"))
        $ amber.messenger.newMessage(_("I got a surprise for you ;)"))

        call screen phone

        pause 0.5

        u "(Fuck, I don't have time for Amber right now, but I really wanna find out what surprise she has.)"

        if CharacterService.is_mad(imre):
            u "(I gotta make a decision. Should I find Imre, or keep talking to Amber?)"
        else:
            u "(I gotta make a decision. Should I help Imre, or keep talking to Amber?)"

    else:
        $ chloe.messenger.newMessage(_("I got some free time right now :)"), force_send=True)
        $ chloe.messenger.newMessage(_("Wanna go swimming?"), force_send=True)
        $ chloe.messenger.addReply(_("Any chance we could do it later? Or tomorrow?"))
        $ chloe.messenger.newMessage(_("I'm busy later tonight and I'm pretty much booked for the entire week :/"))

        call screen phone

        pause 0.5

        u "(Fuck, I don't have time for this right now, but going swimming with Chloe sounds like the best possible way to get closer to her.)"

        if CharacterService.is_mad(imre):
            u "(I gotta make a decision. Should I find Imre, or meet Chloe?)"
        else:
            u "(I gotta make a decision. Should I help Imre, or meet Chloe?)"

    jump v6start
