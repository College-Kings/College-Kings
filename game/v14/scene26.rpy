# SCENE 26: If lauren helps lindsey LAUREN AND LINDSEY BAKE SALE
# Locations: On Campus
# Characters: MC (Outfit: 2), LINDSEY (Outfit: 1), LAUREN (Outfit: 3), AMBER (Outfit: 2)
# Time: Morning
# Kiwi Post: v14kw26 - Lindsey and Lauren Selfie in front of her banner (Lindsey, Returning The Promise) on the banner
# Kiwi Post: v14kw26_1 - Lindsey and Lauren Selfie in front of her banner (Lindsey, Say Bye To The Bullshit) on the banner

label v14s26:
    scene v14s26_1 # TPP. Show mc slight smile, mouth closed, walking through campus and MC heads to the bake sale and sees Lindsey behind the counter
    with dissolve

    pause 0.75

    play music "music/v13/Track Scene 18.mp3" fadein 2

    scene v14s26_2 # FPP. Show lindsey behind the counter looking at mc, slight smile, mouth closed, also show 1 bar on each side of the counter holding up a banner, just show the botton part of the banner, don't show any wording the wording comes into play later
    with dissolve

    u "Hey, hey! How's it going?"

    scene v14s26_2a # FPP. same as v14s26_2 lindsey's mouth is now open
    with dissolve

    li "Hey, you! It's going good, actually..."

    scene v14s26_2b # FPP. same as v14s26_2a increase lindsey to full smile
    with dissolve

    li "I just opened up about an hour ago and I've already made like $100."

    scene v14s26_2
    with dissolve

    u "Wait, what?! *Laughs*"

    scene v14s26_2b
    with dissolve

    li "*Laughs* That's the same reaction I had when I saw it in real time."

    scene v14s26_2
    with dissolve

    u "Who's been buying all your treats?"

    scene v14s26_2c # FPP. same as v14s26_2b lindsey has a slightly shocked expression, expresssive hand gesture
    with dissolve

    li "Strangers, professors, and the most shocking of them all... Grayson."

    scene v14s26_2
    with dissolve

    u "That's a very diverse clientele."

    scene v14s26_2b
    with dissolve

    li "Exactly, that's why this was such a good idea."

    scene v14s26_2a
    with dissolve

    li "Everyone has to eat and most people love to, so food is always a safe route to take."

    scene v14s26_2
    with dissolve

    u "Is there anything I can do to help?"

    scene v14s26_2d # FPP. same as v14s26_2b lindsey is holding up a cake
    with dissolve

    li "You can buy some cake! *Chuckles*"

    scene v14s26_2 
    with dissolve

    u "Hmm... I don't think I'm that hungry today, but..."

    scene v14s26_2a
    with dissolve

    li "Haha, just kidding. Everything is running smoothly thanks to Lauren and her amazing baking skills."

    scene v14s26_2
    with dissolve

    u "Oh, yeah! Where is she?"

    scene v14s26_2e # FPP. Lindsey has a sinister looking expression
    with dissolve

    la "Right behind you..."

    scene v14s26_3 # FPP. MC swings around and sees Lauren, Lauren has her hands up with a scary expression on her face
    with dissolve

    pause 0.75

    scene v14s26_4 # TPP. Show mc jumping back with a shocked expression, Lindsey is behind the mc still behind the counter laughing, Lauren is in front of mc laughing, both of them looking at the mc
    with dissolve

    pause 0.75

    scene v14s26_4a # TPP. same as v14s26_4 mc turns to face lindsey, and lauren walking around the counter with lindsey, lauren approaches and stands on lindseys left
    with dissolve

    pause 0.75

    scene v14s26_5 # FPP. show lauren and lindsey, lauren on the left and lindsey on the right, both of them smiling, both mouths closed, both looking at mc
    with dissolve

    u "Scared the shit out of me! *Laughs*"

    scene v14s26_5a # FPP. same as v14s26_5 lauren mouth open, lindeys mouth closed, the counter looks the same as v14s26_2
    with dissolve

    la "*Laughs* My bad. Let me make it up to you by giving you some cake."

    scene v14s26_5
    with dissolve

    menu:
        "Oh thanks":
            scene v14s26_5
            with dissolve

            u "Wow, that's... Thanks. *Chuckles*"
        
            scene v14s26_5a
            with dissolve

            la "Of course! Just give me like... five dollars."

            scene v14s26_5
            with dissolve

            u "Oh, I thought..."
        
        "I'm not hungry":
            scene v14s26_5
            with dissolve

            u "Oh, no thanks, haha. I'm not hungry."

            scene v14s26_5a
            with dissolve

            la "Good, cause that would've been five dollars!"

            scene v14s26_5
            with dissolve

            u "Oh shit, okay..."

    scene v14s26_5b # FPP. same as v14s26_5 lauren mouth closed, lindeys mouth open
    with dissolve

    li "*Laughs*"

    scene v14s26_5a
    with dissolve

    la "*Laughs*"

    scene v14s26_5b
    with dissolve

    li "We can give you a free cake, silly. You're on the team."

    scene v14s26_5
    with dissolve

    u "Well, it's good to know I'm special."

    if v11_lindsey_slogan == 1:
        scene v14s26_6 # FPP. Mc looks up at the banner above the counter, The banner reads "Lindsey, Returning The Promise"
        with dissolve

    else:
        scene v14s26_6a # FPP. same as v14s26_6 The banner instead reads "Lindsey, Say Bye To The Bullshit"
        with dissolve

    pause 0.75

    scene v14s26_5
    with dissolve

    u "Wait a minute, is that the slogan I came up with?"

    scene v14s26_5b
    with dissolve

    li "I was waiting for you to notice, haha."

    scene v14s26_5
    with dissolve

    u "I didn't think you took what I said all that seriously, or even remembered."

    scene v14s26_5c # FPP. same as v14s26_5 MC and Lindsey smile at each other
    with dissolve

    pause 0.75

    scene v14s26_5b
    with dissolve

    li "Of course I did, ha. You're the reason I decided to run in the first place."

    scene v14s26_5d # FPP. same as v14s26_5 lauren and lindsey are looking at each other, lauren's mouth is open
    with dissolve

    la "Now all we need to know is, if you win do [name] and I get a special position?"

    scene v14s26_5e # FPP. same as v14s26_5d lindsey's mouth is open, lauren's mouth is closed
    with dissolve

    li "Haha, I don't know about [name], but if you join the Chicks I can help you, Lauren."

    li "Or I could even do some partnership work with the Deers, you know."

    scene v14s26_5d
    with dissolve

    la "See? This is exactly why I'm supporting you."

    scene v14s26_5e
    with dissolve

    li "Thanks babe, I just wish your sister felt the same..."

    scene v14s26_5d
    with dissolve

    la "*Scoffs* Don't we all."

    scene v14s26_5b
    with dissolve

    li "Well, here you go [name]. Thanks again for everything so far."

    scene v14s26_5f # FPP. same as v14s26_5a Lindsey hands MC a cake
    with dissolve

    la "Enjoy! It was made with love."

    scene v14s26_5
    with dissolve

    u "Haha, I will. I'm gonna sit back and relax for a minute while I enjoy this."

    scene v14s26_5b
    with dissolve

    li "Haha, okay. See you in a bit."

    scene v14s26_5
    with dissolve

    u "Yeah, good luck you two!"

    scene v14s26_7 # TPP. MC goes and sits on a bench nearby and eats his cake
    with dissolve

    pause 0.75

    scene v14s26_8 # TPP. MC checks his phone
    with dissolve

    pause 0.75

# -Kiwii post of Lindsey's bake sale, 2 different renders needed for seperate slogans-

# Kiwi Post: v14kw26 - Lindsey and Lauren Selfie in front of her banner (Lindsey, Returning The Promise) on the banner
    if v11_lindsey_slogan == 1:
        #Selfie with Lauren in front of slogan banner that says Lindsey, Returning The Promise
        $ v14s26_kiwiiPost1 = KiwiiPost(lindsey, "v14/v14kw26.webp", "Don't forget to stop by and pick up one of Lauren's famous cakes today! For the future of the Chicks! <3", mentions=[lauren], numberLikes=748)
        $ v14s26_kiwiiPost1.newComment(lauren, "#Vote4Lindsey! <3", force_send=True, numberLikes=382)
        # $ v14s26_kiwiiPost1.newComment(nora, "Cuties <3", numberLikes=renpy.random.randint(150, 300), force_send=True)
        $ v14s26_kiwiiPost1.newComment(imre, "Actually that cookie this morning made me shit myself!", numberLikes=renpy.random.randint(150, 300), force_send=True)
        $ v14s26_kiwiiPost1.newComment(chloe, "Eww...", numberLikes=renpy.random.randint(150, 300), force_send=True)
        $ v14s26_kiwiiPost1.newComment(lauren, "Oh, is that why you came back for three more?", mentions=[imre], numberLikes=renpy.random.randint(150, 300), force_send=True)
        $ v14s26_kiwiiPost1.newComment(sebastian, "Yeah dude, you gave me one of them, lol. Tasted great ladies!", numberLikes=renpy.random.randint(150, 300), force_send=True)
        $ v14s26_kiwiiPost1.newComment(imre, "Whatever, so what?", numberLikes=renpy.random.randint(150, 300), force_send=True)
        $ v14s26_kiwiiPost1.newComment(chloe, "...", numberLikes=renpy.random.randint(150, 300), force_send=True)
        $ v14s26_kiwiiPost1.addReply("Thank you for the cake! It's amazing you guys...", numberLikes=renpy.random.randint(150, 300), mentions=[lindsey])
        $ v14s26_kiwiiPost1.newComment(lindsey, "<3", numberLikes=renpy.random.randint(150, 300))
        $ v14s26_kiwiiPost1.newComment(lauren, ":)", numberLikes=renpy.random.randint(150, 300))

# Kiwi Post: v14kw26_1 - Lindsey and Lauren Selfie in front of her banner (Lindsey, Say Bye To The Bullshit) on the banner
    else:
        #Selfie with Lauren in front of slogan banner that says Lindsey, Say Bye To The Bullshit
        $ v14s26_kiwiiPost2 = KiwiiPost(lindsey, "v14/v14kw26_1.webp", "Don't forget to stop by and pick up one of Lauren's famous cakes today! For the future of the Chicks! <3", mentions=[lauren], numberLikes=748)
        $ v14s26_kiwiiPost2.newComment(lauren, "#Vote4Lindsey! <3", numberLikes=renpy.random.randint(300, 600), force_send=True)
        # $ v14s26_kiwiiPost2.newComment(nora, "Cuties <3", numberLikes=renpy.random.randint(300, 600), force_send=True)
        $ v14s26_kiwiiPost2.newComment(imre, "Actually that cookie this morning made me shit myself!", numberLikes=renpy.random.randint(300, 600), force_send=True)
        $ v14s26_kiwiiPost2.newComment(chloe, "Eww...", numberLikes=renpy.random.randint(300, 600), force_send=True)
        $ v14s26_kiwiiPost2.newComment(lauren, "Oh, is that why you came back for three more?", mentions=[imre], numberLikes=renpy.random.randint(300, 600), force_send=True)
        $ v14s26_kiwiiPost2.newComment(sebastian, "Yeah dude, you gave me one of them, lol. Tasted great ladies!", numberLikes=renpy.random.randint(300, 600), force_send=True)
        $ v14s26_kiwiiPost2.newComment(imre, "Whatever, so what?", numberLikes=renpy.random.randint(300, 600), force_send=True)
        $ v14s26_kiwiiPost2.newComment(chloe, "...", numberLikes=renpy.random.randint(300, 600), force_send=True)
        $ v14s26_kiwiiPost2.addReply("Thank you for the cake! It's amazing you guys...", numberLikes=renpy.random.randint(300, 600), mentions=[lindsey])
        $ v14s26_kiwiiPost2.newComment(lindsey, "<3", numberLikes=renpy.random.randint(300, 600))
        $ v14s26_kiwiiPost2.newComment(lauren, ":)", numberLikes=renpy.random.randint(300, 600))

    if not v14_amber_clean:
        play sound "sounds/vibrate.mp3"

        scene v14s26_9 # TPP. MC gets a call from Amber and answers
        with dissolve

        u "Hello?"

        scene v14s26_10 # FPP. show Amber mouth open fully scared talking on the phone in her house
        with dissolve

        am "[name]! Are you okay?! Where are you?"

        scene v14s26_10a # FPP. same as v14s26_10 Amber half scared, mouth closed
        with dissolve

        u "Uhh, I'm at Lindsey's bake sale."

        scene v14s26_10b # FPP. same as v14s26_10 Show Amber concerned
        with dissolve

        am "You're not hurt or anything are you?"

        scene v14s26_10c # FPP. same as v14s26_10b show amber with no expression, mouth closed
        with dissolve

        u "What? No. *Chuckles*"

        u "Are you all good? What's going on?"

        scene v14s26_10b
        with dissolve

        am "I'm fine, sorry..."

        am "I was just scared 'cause when I woke up you weren't here."

        scene v14s26_10c
        with dissolve

        u "That's okay."

        scene v14s26_10d # FPP. same as v14s26_10c show amber slight smile, mouth open
        with dissolve

        am "I don't remember much from last night, ha. Did we have fun?"

        scene v14s26_10c
        with dissolve

        u "One of the best nights of my life."

        scene v14s26_10e # FPP. same as v14s26_10d show amber full smile, mouth open
        with dissolve

        am "Haha, well I'm glad. Sorry for panicking, talk to you later?"

        scene v14s26_10f # FPP. same as v14s26_10e show amber mouth closed
        with dissolve

        u "For sure. See ya."

        scene v14s26_11 # TPP. MC hangs up the phone, slight smile, mouth closed
        with dissolve

        u "(She's a handful.)"

    scene v14s26_12 # TPP. MC gets up and heads over to Lindsey's stand, Lauren has left
    with dissolve

    pause 0.75

    scene v14s26_2
    with dissolve

    u "So? How'd it go?"

    scene v14s26_2b
    with dissolve

    li "It went great! I'm closing up now."

    scene v14s26_2
    with dissolve

    u "How much did you end up making?"

    scene v14s26_2b
    with dissolve

    $ lindsey_board.money +=450
    li "I made $450... *Laughs*"

    scene v14s26_2
    with dissolve

    u "Damn, Linds! You made that in what... Like, two hours?"

    scene v14s26_2a
    with dissolve

    li "Just about, yeah. If you don't include the hours we stayed up making these things last night."

    scene v14s26_2
    with dissolve

    u "Hell yeah... Really, though. I'm impressed."

    scene v14s26_2a
    with dissolve

    li "And I'm so thankful. You and Lauren are the best, haha."

    scene v14s26_2
    with dissolve

    u "Maybe..."

    u "Let me know when it's time for your next event and I'll be there."

    scene v14s26_2a
    with dissolve

    li "Sounds good."

    scene v14s26_2
    with dissolve

    u "See you around, Linds."

    if lindsey.relationship >= Relationship.FWB:
        scene v14s26_13 # FPP. Lindsey winks at MC, slight smile, mouth open
        with dissolve

        li "See you, [name]."

    scene v14s26_14 # TPP. mc walks away from lindsey, no expression, mouth closed
    with dissolve

    pause 0.75

    scene v14s26_15 # TPP. mc walking through the campus, no expression, mouth closed
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v14s27