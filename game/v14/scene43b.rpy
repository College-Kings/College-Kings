# SCENE 43b: Mr. Lee's History Class
# Locations: Mr. Lees Classrom
# Characters: MR. LEE (Outfit: 1), MC (Outfit: 1), RILEY (Outfit: 4), CAMERON (Outfit: 3), IMRE (Outfit: 2), PENELOPE (Outfit: 1)
# Time: Morning
# Kiwi Post: v14kw43b - Sexy pic of Chloe is on Kiwii from Ryan, Grayson and Cameron's accounts-
# 22 Unique Renders, 46 Total

init python:
    def v14_iris_simplr1():
        iris.simplr.addReply(_("I'm more than happy that we matched, especially after knowing that you're just as excited as I am, haha!"), v14_iris_simplr2)

    def v14_iris_simplr2():
        iris.simplr.addReply(_("So, how are you? Who are you? What are you up to? Lmao"), v14_iris_simplr3)
        iris.simplr.addReply(_("You're single, right?"), v14_iris_simplr4)
        
    def v14_iris_simplr3():
        iris.simplr.newMessage(":) I am doing perfectly well now that I'm talking to you, hehe.", force_send=True)
        iris.simplr.newMessage("I'm a 20 year old college student, studying Literature. And at this very moment I am practicing my French. As that's where I'm currently studying, haha", force_send=True)
        iris.simplr.addReply(_("You're in France?! We literally just got back to America from a class trip to Europe..."),v14_iris_simplr6)
        
    def v14_iris_simplr4():
        setattr(store, "irisStrikes", irisStrikes +1)
        iris.simplr.newMessage("Umm, yes? I wouldn't be here if I weren't. Aren't you?", force_send=True)
        iris.simplr.addReply(_("Uh, yeah. Of course! I just felt like I needed to ask for some reason."), v14_iris_simplr5)
        
    def v14_iris_simplr5():
        iris.simplr.newMessage("Right...", force_send=True)
        iris.simplr.addReply("So, single Iris... How are you, who are you and what are you up to?")
        iris.simplr.newMessage("I'm a 20 year old college student, studying Literature. And at this very moment I am practicing my French. As that's where I'm currently studying, haha", force_send=True)
        iris.simplr.addReply(("You're in France?! We literally just got back to America from a class trip to Europe..."), v14_iris_simplr6)
        
    def v14_iris_simplr6():
        iris.simplr.newMessage("No way! I guess fate decided that we shouldn't have met...")
        iris.simplr.addReply("Not yet, at least ;) Maybe this is where our love story begins?")
        iris.simplr.newMessage("...")
        iris.simplr.newMessage("You can't say things like that unless you mean it.")
        iris.simplr.addReply("What makes you think I didn't mean it?")
        iris.simplr.newMessage("Haha... Okay, Prince Charming.")
        iris.simplr.newMessage("I better sign off of here before I fall too fast... Lol")
        iris.simplr.addReply("Yeah, me too... Sheesh...")
        iris.simplr.newMessage("Oh, whatever! Hahaha. Talk again soon?")
        iris.simplr.addReply("Looking forward to it :)")
        iris.simplr.addReply(_("Sure thing, hottie."), v14_iris_simplr7)
        
    def v14_iris_simplr7():
        setattr(store, "irisStrikes", irisStrikes +1)

label v14s43b:
    if iris.simplr in simplr_contacts:
        $ iris.simplr.newMessage("Soooo....", force_send=True)
        $ iris.simplr.newMessage("I'm guessing you aren't that happy about it considering it's been a few days now with no response, haha. Sorry.", force_send=True)
        $ iris.simplr.addReply(_("Hey, Iris. So sorry if you felt like I wasn't interested, my Simplr has just been glitchy and I've been stuck out of it for a while. Back for good now."), v14_iris_simplr1)

    scene v14s43b_1 # FPP. Mr. Lee walks into the classroom happy and cheery, mouth open
    with dissolve

    lee "Good morning, students!"

    play music "music/v13/Track Scene 24_1.mp3" fadein 2

    scene v14s43b_2 # FPP. Mr. Lee walks further into the classroom, happy and cheery, mouth closed
    with dissolve

    u "(What's he so excited about?)"

    scene v14s43b_3 # FPP. Show Mr. Lee, full body shot, standing by his podium, fully smiling, mouth open, looking at MC, Mr. Lee and Podium are slightly left of center of the screen
    with dissolve

    lee "Today is a very good day, everyone. Although, I understand that you're unaware."

    scene v14s43b_4 # FPP. Show Riley sitting a row just behind of MC and to MC's Left, Riley has a slight smile, mouth open, looking at Mr. Lee
    with dissolve

    ri "Mind letting us know what's happening?"

    scene v14s43b_3a # FPP. same as v14s43b_3 Mr. Lee looks slightly to his right at Riley
    with dissolve

    lee "Riley! Yes! I'm so glad you asked."

    scene v14s43b_3
    with dissolve

    lee "The college has recently begun to advance its usage of the teacher assistant program and so have I."

    scene v14s43b_3b # FPP. same as v14s43b_3 Mr. Lee's mouth is closed
    with dissolve

    u "(Oh, haha... That's why Riley is here.)"

    scene v14s43b_3c # FPP. same as v14s43b_3 extends one arm outward towards MC's direction palm up
    with dissolve

    lee "Let me introduce my new student assistant..."

    scene v14s43b_4
    with dissolve

    u "Oh!"

    scene v14s43b_3d # FPP. same as v14s43b_3c Mr. lee Mr. Lee looks slightly to his right at Riley and extends his arm and open palm towards Riley
    with dissolve

    lee "Riley!"

    scene v14s43b_4a # FPP. same as v14s43b_4 Riley has a shocked expression, mouth open, looking at Mr. Lee
    with dissolve

    ri "I, thank you... I mean, you could've just told me that's what was happening. *Chuckles* But really, thanks. Im excited!"

    scene v14s43b_3e # FPP. same as v14s43b_3d Mr. Lee raises his eyebrow
    with dissolve

    lee "So are we. Right class?"

    scene v14s43b_4b # FPP. same as v14s43b_4a Riley slightly scared, mouth open, looking at Mr. Lee
    with dissolve

    ri "Haha, it's okay."

    scene v14s43b_3b
    with dissolve

    u "(This should be interesting... haha.)"

    scene v14s43b_3d
    with dissolve

    lee "Come introduce yourself to the class."

    scene v14s43b_4a
    with dissolve

    ri "Really? Now?"

    scene v14s43b_3a
    with dissolve

    lee "Really. Now."

    scene v14s43b_4c # FPP. same as v14s43b_4a Riley no expression, mouth closed
    with dissolve

    ri "Okay..."

    scene v14s43b_4d # FPP. same as v14s43b_4c Riley stands where she is and starts speaking, nervous expression, mouth open
    with dissolve

    ri "For all of you who don't know me, my name is Riley. I'm a freshman and a free spirit..."

    scene v14s43b_3a
    with dissolve

    lee "True, tried, and tested!"

    scene v14s43b_4d
    with dissolve

    ri "Ahem, I uh... I'm very approachable, so I don't know what all my responsibilities will be as a teacher's assistant, but feel free to talk to me."

    scene v14s43b_4c
    with dissolve

    pause 0.75

    scene v14s43b_3a
    with dissolve

    lee "Very good! Thank you. Now, on to class..."

    scene v14s43b_3
    with dissolve

    lee "Today we will once again be doing a roleplay."

    scene v14s43b_5 # FPP. Show Cameron sitting a row just behind Mc to his right, slightly annoyed, mouth slightly open, looking at MC
    with dissolve

    ca "*Mumbles* Fuck!"

    scene v14s43b_3
    with dissolve

    lee "It's all about the relationship between a king and a queen during medieval times."
    lee "Each gentleman will be paired with a lady, but we will need Riley to take part to make sure everyone can be paired up."

    scene v14s43b_4e # FPP. same as v14s43b_4c Riley's mouth is open
    with dissolve

    ri "Oh."

    scene v14s43b_3
    with dissolve

    lee "Start pairing up!"

    scene v14s43b_6 # FPP. show Penelope and Riley walking on MCs left towards Mr. Lee at the podium, and show Cameron and Imre walking on Mc's right
    with dissolve

    pause 0.75

    scene v14s43b_7 # FPP. MC has walked towards the front of the class and see's Riley talking to Mr. Lee, Mr. Lee's mouth is closed slight smile Riley's is open no expression, Imre is walking by Riley avoiding eye contact with her, Penelope and Cameron are standing awakwardly next to each other, Penelope no expression mouth closed, cameron no expression mouth closed
    with dissolve

    pause 0.75

    scene v14s43b_7a # FPP. same as v14s43b_7 Penelope has walked away from Cameron and is walking by MC, looking at MC slight smile mouth closed, Mr. Lee has started looking at and talking to Imre, Mr. Lee mouth open slight smile Imre mouth closed no expression looking at Mr. Lee, Riley and Cameron are now standing facing each other and talking, no expressions, Cameron mouth open, Riley's mouth closed
    with dissolve

    pause 0.75

    scene v14s43b_7b # FPP. same as v14s43b_7a Close up shot of Penelope
    with dissolve

    u "Guess we were meant to work together."
    
    scene v14s43b_7c
    with dissolve

    pause 0.75
    
    scene v14s43b_8 # FPP. Mc is still standing, show Penelope sitting down in a seat looking at Mc slight smile mouth closed
    with dissolve
    
    pause 0.75

    scene v14s43b_9 # FPP. Show just imre looking at MC, no expression, mouth open, Mc has shifted his view to his left to look only at Imre
    with dissolve

    imre "Hey."

    scene v14s43b_9a # FPP same as v14s43b_9 imre mouth closed
    with dissolve

    u "What?"

    scene v14s43b_9
    with dissolve

    imre "Were you getting ready to go over there and work with Penelope?"

    scene v14s43b_9a
    with dissolve

    u "Yeah. Why?"

    scene v14s43b_9
    with dissolve

    imre "I was actually already planning to."

    scene v14s43b_9a
    with dissolve

    u "Why is it that you're always trying to stop me?"

    scene v14s43b_9b # FPP. same as v14s43b_9 imre has a nervous expression, hand behind his head, mouth open
    with dissolve

    imre "Look man... Ugh, please? Just let me work with her."

    scene v14s43b_9a
    with dissolve

    u "I need an answer first. Why?"

    scene v14s43b_9
    with dissolve

    imre "*Sighs* Okay fine, I sent some drunk texts to Riley last night and she hasn't replied, so it'd be awkward having to work with her. You know?"

    scene v14s43b_9a
    with dissolve

    u "*Laughs* Yeah. I get that..."

    menu:
        "Work with Penelope":
            $ v14_PenelopePartner = True

            if penelope.relationship >= Relationship.LOYAL:
                $ add_point(KCT.BOYFRIEND)

            else:
                $ add_point(KCT.TROUBLEMAKER)

            u "But sorry, man. This will be too good to miss."

            scene v14s43b_9c # FPP. same as v14s43b_9 shocked expression, mouth open
            with dissolve

            imre "Bro, please."

            scene v14s43b_9a
            with dissolve

            u "Nope."

            scene v14s43b_7c # FPP. same as v14s43b_7 Penelope is no longer visible, Mr. Lee is standing at his podium looking at paperwork no expression mouth closed, Imre has joined Riley and Cameron all awkwardly standing with and looking at each other, no expressions, mouths closed
            with dissolve

            pause 0.75

            scene v14s43b_8
            with dissolve

            u "Me and you?"

            scene v14s43b_8b # FPP. same as v14s43b_8 mc has walked to Penelopes side and kneels down to penelopes eye level, Penelope slight smile, mouth open
            with dissolve

            pe "You and me?"

            scene v14s43b_8c # FPP. same as v14s43b_8b Penelope mouth closed
            with dissolve

            u "No, no, no. Me and you."

            if penelope.relationship >= Relationship.LOYAL:
                scene v14s43b_8b
                with dissolve

                pe "No, no, no. You..."

                scene v14s43b_10 # TPP. Penelope gets close to mc's lips without kissing them, Mc full smile mouth closed, Penelope full smile, mouth slightly open
                with dissolve

                pe "*Whispers* And me. *Chuckles*"

            else:
                scene v14s43b_8b
                with dissolve

                pe "No, no, no. You and me. *Chuckles*"

            scene v14s43b_8c
            with dissolve

            u "Fine... You and me."

            scene v14s43b_8d # FPP. same as v14s43b_8b Penelope full smile 
            with dissolve

            pe "Yay."

            scene v14s43b_11 # TPP. Mc sits back down with Penelope, slight smiles, mouths closed, looking towards Mr. Lee at the front of the class
            with dissolve

            pause 0.75

            scene v14s43b_3
            with dissolve

            lee "Everyone's paired up? Good!"

            lee "Now, once I'm finished speaking you may leave the classroom and begin reading pages 100-103 in your textbook."

            lee "After that, you'll come up with a short scene involving a king and a queen interaction that you'll present next week to the rest of the class."

            if v14_ApesPostChloePics:
                scene v14s43b_12 # FPP. MC looks at Penelope in the seat next to him, Penelope looking at MC, slight smile, mouth open
                with dissolve

                pe "Ooh, this sounds fun."

                play sound "sounds/vibrate.mp3"

                scene v14s43b_12a # FPP. Penelope mouth closed
                with dissolve

                u "Hmm? Let me check this real quick."

                scene v14s43b_13 # FPP. MC looks down at his phone in his hand and checks his phone, Only show Mc's hand and lap in the render, no other characters present
                with dissolve

                # Kiwi Post: v14kw43b - Sexy pic of Chloe is on Kiwii from Ryan, Grayson and Cameron's accounts- Private sexy pic of chloe same photo as in scene 41a

                $ v14s43b_kiwiiPost1 = KiwiiPost(grayson, "v14/v14kw43b.webp", "#Vote4Chloe is a #Vote4Whore", mentions=[chloe], numberLikes=255)
                $ v14s43b_kiwiiPost1.newComment(chloe, "You weren't calling me a whore when I was in your bed all of last year. Wonder what changed? #Salty", numberLikes=renpy.random.randint(100, 200), force_send=True)
                $ v14s43b_kiwiiPost1.newComment(aubrey, "Grayson, what the fuck?! Did Lindsey put you up to this?!", numberLikes=renpy.random.randint(100, 200), force_send=True)
                $ v14s43b_kiwiiPost1.newComment(lindsey, "I would never, ever, EVER tell them to do this.", numberLikes=renpy.random.randint(100, 200), force_send=True)
                $ v14s43b_kiwiiPost1.newComment(imre, "Ok sure, whatever Linds. Doesn't matter to anyone, Chloe's never going to lose against someone who reaches this low to win.", numberLikes=renpy.random.randint(100, 200), force_send=True)

                $ v14s43b_kiwiiPost2 = KiwiiPost(ryan, "v14/v14kw43b.webp", "#Vote4Chloe and she'll send you pics, just like this!", mentions=[chloe], numberLikes=157)
                $ v14s43b_kiwiiPost2.newComment(chloe, "You too? Wow, why don't you just suck Grayson's dick while you're at it, huh?", numberLikes=renpy.random.randint(100, 200), force_send=True)
                $ v14s43b_kiwiiPost2.newComment(imre, "Ha, you fucking idiot. Choke on it, too.", numberLikes=renpy.random.randint(100, 200), force_send=True)
                $ v14s43b_kiwiiPost2.newComment(ryan, "Sure Imre, right after you stop sucking on Chloe's tits all the fucking time.", numberLikes=renpy.random.randint(100, 200), force_send=True)
                $ v14s43b_kiwiiPost2.newComment(aubrey, "ENOUGH", numberLikes=renpy.random.randint(100, 200), force_send=True)

                $ v14s43b_kiwiiPost3 = KiwiiPost(cameron, "v14/v14kw43b.webp", "Vote for Lindsey, not for this.", numberLikes=417)
                $ v14s43b_kiwiiPost3.newComment(chloe, "This? Wow, Cam. Thanks...", numberLikes=renpy.random.randint(150, 350), force_send=True)
                $ v14s43b_kiwiiPost3.newComment(samantha, "Cam, what are you doing?!", numberLikes=renpy.random.randint(150, 350), force_send=True)
                $ v14s43b_kiwiiPost3.newComment(cameron, "Frat shit. What else would I be doing?", numberLikes=renpy.random.randint(150, 350), force_send=True)
                $ v14s43b_kiwiiPost3.newComment(sebastian, "This is too far for just \"frat shit\".", numberLikes=renpy.random.randint(150, 350), force_send=True)
                $ v14s43b_kiwiiPost3.newComment(aubrey, "Pathetic.", numberLikes=renpy.random.randint(150, 350), force_send=True)

                $ chloe.messenger.newMessage("GRAYSON IS SUCH AN ASSHOLE", force_send=True)
                $ chloe.messenger.newMessage("FUCK HIM AND FUCK THE APES AND FUCK THEIR KIWIIS!!!!", force_send=True)
                $ chloe.messenger.newMessage("UGH! I'm going to turn this around. It won't hurt my campaign even a little bit, I'll make sure of it.", force_send=True)

                $ chloe.messenger.addReply("I'm so sorry that this is happening. I don't even know what to say.")
                $ chloe.messenger.newMessage("I know, I know... I'm just venting.")
                if not joinwolves:
                    $ chloe.messenger.newMessage("And I'm really thankful that you didn't post anything.")
                    $ chloe.messenger.addReply("I'd never do that.")

                label v14s43Chloe_PhoneContinue1:
                    if chloe.messenger.replies:
                        call screen phone
                    if chloe.messenger.replies:
                        u "(I should reply to Chloe.)"
                        jump v14s43Chloe_PhoneContinue1

                $ set_presidency_percent(v14_lindsey_popularity + 3) #tick
                if joinwolves:
                    u "(Fuck... Where did that come from?)"

                else:
                    u "(Fuck... I'm glad I didn't go through with posting that shit.)"

                scene v14s43b_12
                with dissolve

                pe "Ready to go?"

                scene v14s43b_12a
                with dissolve

                u "*Sighs* Yeah, sorry. Where to?"

                scene v14s43b_12
                with dissolve

                pe "We can just go sit outside on the stairs and work, if that's cool."

                scene v14s43b_12a
                with dissolve

                u "Sounds good, lead the way."

                scene v14s43b_14 # TPP. show mc and penelope stand up and walk away from there seats, slight smiles, mouths closed
                with dissolve

                pause 0.75

                scene v14s43b_15 # TPP. MC follows Penelope outside of the classroom, slight smiles mouths closed
                with dissolve

                pause 0.75

                scene v14s43b_16 # TPP. Mc and Penelope sit on the steps of the stairwell slight smiles, mouths closed.
                with dissolve

                pause 0.75

                stop music fadeout 3

                jump v14s43c

            else: 
                scene v14s43b_12
                with dissolve

                pe "Ooh, this sounds fun."

                pe "We can just go sit outside on the stairs and work, if that's cool."

                scene v14s43b_12a
                with dissolve

                u "Sounds good, lead the way."

                scene v14s43b_14
                with dissolve

                pause 0.75

                scene v14s43b_15
                with dissolve

                pause 0.75

                scene v14s43b_16
                with dissolve

                pause 0.75

                stop music fadeout 3

                jump v14s43c

        "Work with Riley":
            $ add_point(KCT.BRO)
            u "But sorry, bro..."

            scene v14s43b_9a
            with dissolve

            u "(Let's mess with him a bit.) I'm working with Penelope."

            scene v14s43b_9c
            with dissolve

            imre "Bro, please."

            scene v14s43b_9a
            with dissolve

            u "Sorry, man. What are you gonna do about the Riley situation?"

            scene v14s43b_9
            with dissolve

            imre "Fuck, dude... I don't know. Maybe she'll pretend like it never happened? Or should I bring it up? What the fuck should i do here?"

            scene v14s43b_9a
            with dissolve

            u "Haha... I just wanted to see you squirm for a second. I wouldn't actually do you like that, have fun with Penelope."

            scene v14s43b_9d # FPP. same as same as v14s43b_9c Imre happy expression, slight smile, mouth open
            with dissolve

            imre "Oh shit, haha... Thanks man."

            scene v14s43b_9a
            with dissolve

            u "No problem. Just be more careful, yeah?"

            scene v14s43b_9
            with dissolve

            imre "No shit."

            scene v14s43b_10a # TPP. same as v14s43b_10 Imre instead of MC, Imre goes and sits next to Penelope, Imre looking at Penelope slight smile mouth open, Penelope slight disgusted exression, mouth closed, eyes wide open looking at Imre
            with dissolve

            pause 0.75

            scene v14s43b_17 # FPP. MC walks towards Riley, Cameron is seen walking away just looking where he is walking no expression mouth closed, Riley slight smile mouth closed looking at mc
            with dissolve

            u "*Whisper* I'll be the \"additional gentleman\", just for you."

            scene v14s43b_17a # FPP. same as v14s43b_17 Riley mouth open, Cameron has walked away and is no longer visible on screen
            with dissolve

            ri "*Whispers* Thank you, so so so much."

            scene v14s43b_18 # TPP. Riley and mc walk with each other to the left side of the classroom to a couple seats and sit down, both slight smiles, mouths closed
            with dissolve

            pause 0.75

            if "v14_threesome" in sceneList:
                scene v14s43b_19 # FPP. Riley and MC have sat down and Riley grabs and holds MC's hand under the table they sat at from v14s43b_18, Riley half smile, mouth closed looking at MC
                with dissolve

                pause 0.75

            scene v14s43b_3f # FPP. same as v14s43b_3 Mr. Lee. is centered in the middle of the screen
            with dissolve

            lee "Everyone's paired up? Good!"

            lee "Now, once I'm finished speaking you may leave the classroom and begin reading pages 100-103 in your textbook."

            lee "After that, you'll come up with a short scene involving a king and a queen interaction that you'll present next week to the rest of the class."

            if v14_ApesPostChloePics:
                scene v14s43b_20 # FPP. MC and Riley are sitting at the desk they sat in from v14s43b_18, Riley is looking at MC, slight smile, mouth open
                with dissolve

                ri "Oh, that seems easy enough."

                play sound "sounds/vibrate.mp3"

                scene v14s43b_20a # FPP. Rileys mouth is closed
                with dissolve

                u "Hmm? Let me check this real quick."

                scene v14s43b_13
                with dissolve

                # Kiwi Post: v14kw43b - Sexy pic of Chloe is on Kiwii from Ryan, Grayson and Cameron's accounts- Private sexy pic of chloe same photo as in scene 41a

                $ v14s43b_kiwiiPost4 = KiwiiPost(grayson, "v14/v14kw43b.webp", "#Vote4Chloe is a #Vote4Whore", mentions=[chloe], numberLikes=255)
                $ v14s43b_kiwiiPost4.newComment(chloe, "You weren't calling me a whore when I was in your bed all of last year. Wonder what changed? #Salty", numberLikes=renpy.random.randint(100, 200), force_send=True)
                $ v14s43b_kiwiiPost4.newComment(aubrey, "Grayson, what the fuck?! Did Lindsey put you up to this?!", numberLikes=renpy.random.randint(100, 200), force_send=True)
                $ v14s43b_kiwiiPost4.newComment(lindsey, "I would never, ever, EVER tell them to do this.", numberLikes=renpy.random.randint(100, 200), force_send=True)
                $ v14s43b_kiwiiPost4.newComment(imre, "Ok sure, whatever Linds. Doesn't matter to anyone, Chloe's never going to lose against someone who reaches this low to win.", numberLikes=renpy.random.randint(100, 200), force_send=True)

                $ v14s43b_kiwiiPost5 = KiwiiPost(ryan, "v14/v14kw43b.webp", "#Vote4Chloe and she'll send you pics, just like this!", mentions=[chloe], numberLikes=157)
                $ v14s43b_kiwiiPost5.newComment(chloe, "You too? Wow, why don't you just suck Grayson's dick while you're at it, huh?", numberLikes=renpy.random.randint(50, 100), force_send=True)
                $ v14s43b_kiwiiPost5.newComment(imre, "Ha, you fucking idiot. Choke on it, too.", numberLikes=renpy.random.randint(50, 100), force_send=True)
                $ v14s43b_kiwiiPost5.newComment(ryan, "Sure Imre, right after you stop sucking on Chloe's tits all the fucking time.", numberLikes=renpy.random.randint(50, 100), force_send=True)
                $ v14s43b_kiwiiPost5.newComment(aubrey, "ENOUGH", numberLikes=renpy.random.randint(50, 100), force_send=True)

                $ v14s43b_kiwiiPost6 = KiwiiPost(cameron, "v14/v14kw43b.webp", "Vote for Lindsey, not for this.", numberLikes=417)
                $ v14s43b_kiwiiPost6.newComment(chloe, "This? Wow, Cam. Thanks...", numberLikes=renpy.random.randint(150, 350), force_send=True)
                $ v14s43b_kiwiiPost6.newComment(samantha, "Cam, what are you doing?!", numberLikes=renpy.random.randint(150, 350), force_send=True)
                $ v14s43b_kiwiiPost6.newComment(cameron, "Frat shit. What else would I be doing?", numberLikes=renpy.random.randint(150, 350), force_send=True)
                $ v14s43b_kiwiiPost6.newComment(sebastian, "This is too far for just \"frat shit\".", numberLikes=renpy.random.randint(150, 350), force_send=True)
                $ v14s43b_kiwiiPost6.newComment(aubrey, "Pathetic.", numberLikes=renpy.random.randint(150, 350), force_send=True)

                $ chloe.messenger.newMessage("GRAYSON IS SUCH AN ASSHOLE", force_send=True)
                $ chloe.messenger.newMessage("FUCK HIM, AND FUCK THE APES!!!!", force_send=True)
                $ chloe.messenger.newMessage("UGH! I'm going to turn this around. It won't hurt my campaign even a little bit, I'll make sure of it.", force_send=True)

                $ chloe.messenger.addReply("I'm so sorry that this is happening. I don't even know what to say.")
                $ chloe.messenger.newMessage("I know, I know... I'm just venting.")
                if not joinwolves:
                    $ chloe.messenger.newMessage("And I'm really thankful that you didn't post anything.")
                    $ chloe.messenger.addReply("I'd never do that.")

                label v14s43Chloe_PhoneContinue2:
                    if chloe.messenger.replies:
                        call screen phone
                    if chloe.messenger.replies:
                        u "(I should reply to Chloe.)"
                        jump v14s43Chloe_PhoneContinue2

                scene v14s43b_13
                with dissolve

                $ set_presidency_percent(v14_lindsey_popularity + 3) #tick
                if joinwolves:
                    u "(Fuck... Where did that come from?)"

                else:
                    u "(Fuck... I'm glad I didn't go through with posting that shit.)"
                    
                scene v14s43b_20a
                with dissolve

                u "*Sighs* Okay, are you ready to go?"

                scene v14s43b_20
                with dissolve

                ri "Yeah, but where do you wanna work?"

                scene v14s43b_20a
                with dissolve

                u "Let's just work in the classroom across the hall, it's always empty."

                scene v14s43b_20
                with dissolve

                ri "Okay, then. Sure."

                scene v14s43b_21 # TPP. show mc and riley stand up and walk away from there seats, slight smiles, mouths closed
                with dissolve

                pause 0.75

                scene v14s43b_15a # TPP. Show Riley instead of Penelope
                with dissolve

                pause 0.75

                scene v14s43b_22 # TPP. Show MC following Riley to the empty classroom and they sit
                with dissolve

                pause 0.75

                stop music fadeout 3

                jump v14s43d

            else:
                scene v14s43b_20
                with dissolve

                ri "Oh, that seems easy enough."

                scene v14s43b_20a
                with dissolve

                u "Okay, are you ready to go?"

                scene v14s43b_20
                with dissolve

                ri "Yeah, but where do you wanna work?"

                scene v14s43b_20a
                with dissolve

                u "Let's just work in the classroom across the hall, it's always empty."

                scene v14s43b_20
                with dissolve

                ri "Okay, then. Sure."

                scene v14s43b_21
                with dissolve

                pause 0.75

                scene v14s43b_15a
                with dissolve

                pause 0.75

                scene v14s43b_22
                with dissolve

                pause 0.75

                stop music fadeout 3

                jump v14s43d