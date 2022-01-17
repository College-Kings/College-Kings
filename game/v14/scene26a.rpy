# SCENE 26a: else LINDSEY
# Locations: On Campus
# Characters: MC (Outfit: 2), LINDSEY (Outfit: 1), AMBER (Outfit: 2)
# Time: Morning
# Kiwi Post: v14kw26a - Lindsey Selfie in front of her banner (Lindsey, Returning The Promise) on the banner
# Kiwi Post: v14kw26a_1 - Lindsey Selfie in front of her banner (Lindsey, Say Bye To The Bullshit) on the banner

label v14s26a:
    scene v14s26a_1 # TPP. You can use the render from v14s26_1 because they are the same scene. Otherwise the description is as follows: Show mc slight smile, mouth closed, walking through campus and MC heads to the bake sale and sees Lindsey behind the counter
    with dissolve

    pause 0.75

    play music "music/v13/Track Scene 18.mp3" fadein 2

    scene v14s26a_2 # FPP. You can use the render from v14s26_2 because they are the same scene. Otherwise the description is as follows: Show lindsey behind the counter looking at mc, frustrated expression, mouth closed, also show 1 bar on each side of the counter holding up a banner, just show the botton part of the banner, don't show any wording the wording comes into play later
    with dissolve

    u "Hey, hey! How's it going?"

    scene v14s26a_2a # FPP. show lindsey no expression, mouth open
    with dissolve

    li "It'd be going a hell of a lot better if I had any help... Ha."

    scene v14s26a_2b # FPP. same as v14s26a_2a show lindsey mouth closed
    with dissolve

    u "I'm sorry I couldn't help, was there no one else willing to help you?"

    if v14_lauren_sabotage:
        scene v14s26a_2a
        with dissolve

        li "I asked Lauren, but even with her help things aren't going very well."

        scene v14s26a_2b
        with dissolve

        u "(So Lauren did end up helping... Or did she fake help?)"

    else:
        scene v14s26a_2a
        with dissolve

        li "I asked Lauren but she ended up not feeling well enough to come over last night... Something about a stomach ache. *Sighs*"

        scene v14s26a_2b
        with dissolve

    u "Well, what's going on? Everyone loves baked goods... *Laughs*"

    scene v14s26a_2a # FPP. same as v14s26a_2a Show lindsey slightly upset
    with dissolve

    li "Apparently not, [name]."

    li "So far most of what I could sell as to my family. *Sighs*"

    scene v14s26a_2b
    with dissolve

    u "Damn. Okay, well..."

    u "Do you have a plan to get it going?"

    scene v14s26a_2a
    with dissolve

    li "The only way this bake sale can be saved is..."

    scene v14s26a_2d # FPP. same as v14s26a_2a lindsey slight smile, mouth open
    with dissolve

    li "If I get naked, stand on this table and start shaking my ass for sales."

    scene v14s26a_2e # FPP. same as v14s26a_2d lindsey mouth closed
    with dissolve

    u "And...?"

    scene v14s26a_2f # FPP. same as v14s26a_2a lindsey is angry, mouth open
    with dissolve

    li "And? I'm not doing that!"

    scene v14s26a_2g # FPP. same as v14s26a_2f lindsey's decreased to slightly angry, mouth closed
    with dissolve

    u "You're pretty pissed about this, aren't you?"

    scene v14s26a_2f
    with dissolve

    li "Surprise, surprise!"

    if not v14_help_lindsey:
        scene v14s26a_2g
        with dissolve

        u "Lindsey, I know this is important. Just try to breathe for-"

        scene v14s26a_2h # FPP same as v14s26a_2a lindsey is slightly sad, mouth open
        with dissolve

        li "I'm not trying to put this on you, [name] because it's not like the whole campaign depended on you, but..."

        li "I was counting on you, and this."

        scene v14s26a_2i # FPP. same as v14s26a_2h lindsey's mouth is closed
        with dissolve

        u "I'm sorry Lindsey, but-"

        scene v14s26a_2k # FPP. same as v14s26a_2g lindsey's mouth is is open
        with dissolve

        li "Like I said before, I'm not interested in hearing your reasons for not being able to help me."

        li "Because honestly, if the reason isn't a good one it's just gonna upset me even more than I already am."

    scene v14s26a_2g
    with dissolve

    u "Well, okay. I'm just gonna go then, I guess. Text me if you need me, okay?"

    scene v14s26a_3 # TPP. MC begins to walk away, slight frown, mouth closed
    with dissolve

    pause 0.75

    scene v14s26a_2a
    with dissolve

    li "*Sighs* Look, [name]. I'm not mad at you, okay?"

    li "I don't want you thinking that."

    scene v14s26a_2c
    with dissolve

    u "It's fine, Linds."

    scene v14s26a_2a
    with dissolve

    li "No, it's not. You know what?"

    scene v14s26a_2j # FPP. same as v14s26a_2a Lindsey grabs a cake and hands it to MC, no expression, mouth open
    with dissolve

    li "Here. Take one for the road."

    if v14_lauren_sabotage:
        scene v14s26a_2d
        with dissolve

        li "Lauren helped make them and they tasted great last night, but I guess something went wrong because they aren't exactly the best now. *Chuckles*"

        scene v14s26a_2i
        with dissolve

        u "(Damn, so that's how she sabotaged her. Good cooking, Lauren!)"

    u "I'm sure it'll be fine... Thanks, Lindsey."

    scene v14s26a_2h
    with dissolve

    li "Yeah, of course."

    scene v14s26_7 # Ignore as reused from another scene
    with fade

    pause 0.75

    scene v14s26_8 # Ignore as reused from another scene
    with dissolve
    
    pause 0.75

# -Kiwii post of Lindsey's bake sale, 2 different renders needed for seperate slogans-

# Kiwi Post: v14kw26a - Lindsey Selfie in front of her banner (Lindsey, Returning The Promise) on the banner

    if v11_lindsey_slogan == 1:
        #Lindsey by herself infront of slogan banner half-smiling that says Lindsey, Returning The Promise
        $ v14s26a_kiwiiPost1 = KiwiiPost(lindsey, "v14/v14kw26a.webp", "Still selling treats to raise money for my campaign and the future of the Chicks! Don't forget to stop by <3 #Vote4Lindsey", numberLikes=593)
        $ v14s26a_kiwiiPost1.newComment(lauren, "#Vote4Lindsey! <3", numberLikes=renpy.random.randint(200, 500), force_send=True)
        # $ v14s26a_kiwiiPost1.newComment(nora, "Cutie <3", numberLikes=renpy.random.randint(200, 500), force_send=True)
        $ v14s26a_kiwiiPost1.newComment(imre, "Actually, that cookie this morning made me shit myself!", numberLikes=renpy.random.randint(200, 500), force_send=True)
        $ v14s26a_kiwiiPost1.newComment(chloe, "Eww...", numberLikes=renpy.random.randint(200, 500), force_send=True)
        $ v14s26a_kiwiiPost1.newComment(lindsey, "Really, Imre... Please stop.", numberLikes=renpy.random.randint(200, 500), mentions=[imre], force_send=True)
        $ v14s26a_kiwiiPost1.newComment(sebastian, "Yeah dude, and you gave me one of them...", numberLikes=renpy.random.randint(200, 500), force_send=True)
        $ v14s26a_kiwiiPost1.newComment(imre, "Sorry dude! I thought I was doing something nice...", numberLikes=renpy.random.randint(200, 500), force_send=True)
        $ v14s26a_kiwiiPost1.newComment(chloe, "Omg, you guys will have to try my family's chocolate chip cookies! Maybe I'll make some soon :)", numberLikes=renpy.random.randint(200, 500), force_send=True)
        $ v14s26a_kiwiiPost1.newComment(imre, "Hell yeah Chloe", numberLikes=renpy.random.randint(200, 500), force_send=True)
        $ v14s26a_kiwiiPost1.addReply("Thank you for the cake! Mine tastes perfectly fine :)", numberLikes=renpy.random.randint(200, 500), mentions=[lindsey])
        $ v14s26a_kiwiiPost1.newComment(lindsey, "<3", numberLikes=renpy.random.randint(200, 500))

# Kiwi Post: v14kw26a_1 - Lindsey Selfie in front of her banner (Lindsey, Say Bye To The Bullshit) on the banner

    else: 
        #Lindsey by herself infront of slogan banner half-smiling that says Lindsey, Say Bye To The Bullshit
        $ v14s26a_kiwiiPost2 = KiwiiPost(lindsey, "v14/v14kw26a_1.webp", "Still selling treats to raise money for my campaign and the future of the Chicks! Don't forget to stop by <3 #Vote4Lindsey", numberLikes=593)
        $ v14s26a_kiwiiPost2.newComment(lauren, "#Vote4Lindsey! <3", numberLikes=renpy.random.randint(200, 500), force_send=True)
        # $ v14s26a_kiwiiPost2.newComment(nora, "Cutie <3", numberLikes=renpy.random.randint(200, 500), force_send=True)
        $ v14s26a_kiwiiPost2.newComment(imre, "Actually, that cookie this morning made me shit myself!", numberLikes=renpy.random.randint(200, 500), force_send=True)
        $ v14s26a_kiwiiPost2.newComment(chloe, "Eww...", numberLikes=renpy.random.randint(200, 500), force_send=True)
        $ v14s26a_kiwiiPost2.newComment(lindsey, "Really, Imre... Please stop.", mentions=[imre], numberLikes=renpy.random.randint(200, 500), force_send=True)
        $ v14s26a_kiwiiPost2.newComment(sebastian, "Yeah dude, and you gave me one of them...", numberLikes=renpy.random.randint(200, 500), force_send=True)
        $ v14s26a_kiwiiPost2.newComment(imre, "Sorry dude! I thought I was doing something nice...", numberLikes=renpy.random.randint(200, 500), force_send=True)
        $ v14s26a_kiwiiPost2.newComment(chloe, "Omg, you guys will have to try my family's chocolate chip cookies! Maybe I'll make some soon :)", numberLikes=renpy.random.randint(200, 500), force_send=True)
        $ v14s26a_kiwiiPost2.newComment(imre, "Hell yeah Chloe", numberLikes=renpy.random.randint(200, 500), force_send=True)
        $ v14s26a_kiwiiPost2.addReply("Thank you for the cake! Mine tastes perfectly fine :)", numberLikes=renpy.random.randint(200, 500), mentions=[lindsey])
        $ v14s26a_kiwiiPost2.newComment(lindsey, "<3", numberLikes=renpy.random.randint(200, 500))

    if not v14_amber_clean:
        play sound "sounds/vibrate.mp3"

        scene v14s26_9
        with dissolve

        u "Hello?"

        scene v14s26_10 # Ignore as reused from another scene
        with dissolve

        am "[name]! Are you okay?! Where are you?"

        scene v14s26_10a # Ignore as reused from another scene
        with dissolve

        u "Uhh, I'm at Lindsey's bake sale."

        scene v14s26_10b # Ignore as reused from another scene
        with dissolve

        am "You're not hurt or anything are you?"

        scene v14s26_10c # Ignore as reused from another scene
        with dissolve

        u "What? No."

        u "Are you all good? What's going on?"

        scene v14s26_10b # Ignore as reused from another scene
        with dissolve

        am "I'm fine, sorry..."

        am "I was just scared 'cause when I woke up you weren't here."

        scene v14s26_10c # Ignore as reused from another scene
        with dissolve

        u "Haha, I didn't wanna wake you."

        scene v14s26_10e # Ignore as reused from another scene
        with dissolve

        am "Haha, oh ok. Sorry for panicking, talk to you later?"

        scene v14s26_10f # Ignore as reused from another scene
        with dissolve

        u "For sure. See ya."

        scene v14s26_11 # Ignore as reused from another scene
        with dissolve

        u "(She's a handful.)"

    scene v14s26_12 # Ignore as reused from another scene
    with dissolve

    pause 0.75

    scene v14s26_2 # Ignore as reused from another scene
    with dissolve

    u "So? How'd you do?"

    if not v14_lauren_sabotage:
        scene v14s26a_2a
        with dissolve

        $ lindsey_board.money += 150
        li "*Sighs* It was a mini success, I banked $150 so, I'm not too mad."

        scene v14s26a_2b
        with dissolve

        u "That's good, at least you made a small profit. Are you closing up shop now?"

    else:
        scene v14s26a_2a
        with dissolve

        $ lindsey_board.money += 100
        li "$100 for the day. Honestly, this was a complete waste of time."

        scene v14s26a_2b
        with dissolve

        u "Hey... Trial and error, right?"

        u "Plus, promoting your campaign and being out here doing this, is the entire point of having a bake sale, remember?"

        scene v14s26a_2a
        with dissolve

        li "Yeah I guess."

        scene v14s26a_2b
        with dissolve

        u "Are you closing up now?"

    scene v14s26a_2d
    with dissolve

    li "Yeah, I am. I'm ready for a nap."

    scene v14s26a_2e
    with dissolve

    u "Okay, well. Let me know when it's time for your next event and I'll be there."

    scene v14s26a_2d
    with dissolve

    li "Sounds good."

    scene v14s26a_2e
    with dissolve

    u "See you around, Linds."

    scene v14s26a_2d
    with dissolve

    li "See you, [name]."

    if v14_lauren_sabotage:
        u "(It's a sad day for honesty.)"

    scene v14s26_14 # Ignore as reused from another scene
    with dissolve

    pause 0.75

    scene v14s26_15 # Ignore as reused from another scene
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v14s27