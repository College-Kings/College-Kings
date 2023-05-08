# SCENE 11: Imre's Catfish Date
# Locations: sidewalk (1,2) street (1,2) in front of the bar, inside of the bar and hotel lobby
# Characters: IMRE (Outfit: 2), MC (Outfit: 2), RYAN (Outfit: 1)
# Time: Evening 

label v13s11:
    scene v13s11_1 # TPP. MC and Ryan behind imre on the sidewalk (location 1)
    with fade

    pause 0.75

    play music music.v13_Track_Scene_11_1 fadein 2

    scene v13s11_2 # FPP. Camera behind imre, imre is moving his head as if he was humming
    with dissolve

    imre "*Humming*"

    scene v13s11_2a # FPP. looking at ryan, smiling, mouth closed
    with dissolve

    u "*Whisper* Is this dude singing to himself? *Laughs*"

    scene v13s11_2b # FPP. Same as 2a, mouth opened
    with dissolve

    ry "*Whisper* He must be extra happy today. *Laughs*"

    scene v13s11_3 # FPP. Imre stops and looks left (location 2)
    with dissolve

    pause 0.6

    scene v13s11_3a # FPP. Imre still stopped looks right
    with dissolve

    u "*Whisper* Oh shit!"

    scene v13s11_4 # TPP. MC pushes rian against the wall, both looking worried
    with dissolve

    pause 0.75

    scene v13s11_5 # FPP. MC now besides ryan at the wall, ryan looking worried, mouth opened 
    with dissolve

    ry "*Whisper* You think he saw us?"

    scene v13s11_5a # FPP. same as 5, mouth closed
    with dissolve

    u "*Whisper* Not sure."

    scene v13s11_6 # FPP. ryan peeking the corner, seeing imre coming in their direction
    with dissolve

    pause 0.75

    scene v13s11_5
    with dissolve

    ry "*Whisper* Fuck, he's coming this way!"

    scene v13s11_5a
    with dissolve

    u "*Whisper* Well, shit Ryan! Do something!"

    scene v13s11_5
    with dissolve

    ry "*Whisper* You do something!"

    $ timed = True

    menu (fail_label="v13_push_ryan"):
        "Pretend to tie Ryan's shoe":
            $ reputation.add_point(RepComponent.BRO)
            scene v13s11_7 # TPP. MC bends down and pretends to tie ryan's shoe
            with dissolve

            pause 0.75

            scene v13s11_8 # FPP. Now on the ground, ryan freaking out, mouth opened
            with dissolve

            ry "*Whispers* What the fuck is that supposed to do?!"

            scene v13s11_8a # FPP. Same as 8, mouth closed
            with dissolve

            u "Just shut up and play along, would you?"

            scene v13s11_8
            with dissolve

            ry "I don't underst-"

            scene v13s11_9 # FPP. Imre pops arround the corner 
            with dissolve

            pause 0.6

            scene v13s11_9a # FPP. MC still on the ground Imre looks at ryan confused, mouth opened
            with dissolve

            imre "Ryan? What are you- Wait, [name]? What the fuck is going on?!"

            scene v13s11_9b # FPP. Imre looks down at mc, still confused, mouth opened
            with dissolve

            imre "Are you... Tying his shoes? What the hell..."

            scene v13s11_9c # FPP. Looking at ryan, slight smile and hand behind his head, mouth opened
            with dissolve

            ry "He treats me like royalty, unlike you. *Chuckles*"

            scene v13s11_9a
            with dissolve

            imre "He what? What the hell is happening? Were you two following me?!"

            jump v13_imre_continue

        "Push Ryan in front of Imre":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            pass

    label v13_push_ryan:
        
        scene v13s11_10 # TPP. MC pushes ryan off the wall into imres way of view
        with dissolve

        pause 0.75

        scene v13s11_11 # FPP. MC peeking the corner looking at ryan, who is looking back, whispering
        with dissolve

        ry "*Whispers* Hey! What are you-"

        scene v13s11_11a # FPP. Ryan running back to the wall, looking confused, mouth opened
        with dissolve

        ry "What was the point of that?!"

        scene v13s11_11b # FPP. Same as 11a, mouth cloed
        with dissolve

        u "*Chuckles* Sorry, I-"

        scene v13s11_12 # FPP. Imre picking the corner looking at ryan, MC behind another wall, imre's mouth opened
        with dissolve

        imre "Ryan? What are you doing? And why did you just..."

        scene v13s11_12a # FPP. Imre now looking at mc, looking disapointed, mouth closed  
        with dissolve

        u "Oh, hey man! What are you up to?"

        scene v13s11_12b # FPP. same as 12a, mouth opened
        with dissolve

        imre "I'm going on a date... Why are you hiding behind the wall?"

        scene v13s11_13 # TPP. MC walking to ryan and imre, hand behind head, slight smile
        with dissolve

        pause 0.75

        scene v13s11_14 # FPP. MC besides ryan, ryan looking at imre, mad face, mouth opened
        with dissolve

        ry "Because we were following you and he's an asshole. And a pussy."

        scene v13s11_14a # FPP. Ryan looking back at mc, mouth closed
        with dissolve

        u "You little shit..."

        scene v13s11_14b # FPP. Now looking at imre, imre looking confused, mouth opened
        with dissolve

        imre "He what? You're following me?! What the hell is going on?"

label v13_imre_continue:
    scene v13s11_14c # FPP. Same as 14b, mouth closed
    with dissolve

    u "Okay, look... Try not to take this in a weird way, but yeah, we were following you."

    scene v13s11_14b
    with dissolve

    imre "What? Why? I don't understand how I could take this in a \"not weird\" way."

    scene v13s11_14c
    with dissolve

    u "Well, there were some rumors about you going on some hot date and-"

    scene v13s11_14d # FPP. Looking at imre, slight smile on his face, one hand holding his chin, mouth opened
    with dissolve

    imre "Ahh, I get it... So you two are jealous and wanna ruin my date?"

    scene v13s11_14e # FPP. Same as 14d, mouth closed
    with dissolve

    u "Haha, I couldn't care less about that. We care about you, dude. You deserve a good date. But, we don't think this date is gonna be anything like what you're expecting it'll be."

    scene v13s11_14f # FPP. looking at imre, disapointed, mouth opened
    with dissolve

    imre "So, Ryan got you caught up in this catfish bullshit too?"

    scene v13s11_14g # FPP. Same as 14f, mouth closed
    with dissolve

    u "I'm not saying I do or don't believe it's a catfish, but what's the harm in us checking it out? Or at least sticking around in case it ends badly?"

    scene v13s11_14f
    with dissolve

    imre "You know what? You guys can follow me from a distance like the creeps you are, and when I walk in and you see the baddie I've been talking to, you guys can bounce your ugly asses out the door. Deal?"

    scene v13s11_14g
    with dissolve

    u "*Laughs* Deal."

    scene v13s11_14h # FPP. looking at ryan with a big smile on his face, mouth opened
    with dissolve

    ry "Perfect!"

    scene v13s11_14i # FPP. Imre walks off, moving his head a little as if he complaining
    with dissolve

    imre "I swear to god..."

    scene v13s11_14h
    with dissolve

    ry "*Whispers* He's not too happy about this..."

    scene v13s11_14j # FPP. Same as 14h, mouth closed
    with dissolve

    u "*Whispers* He'll get over it. *Chuckles* C'mon."

    scene v13s11_15 # TPP. MC and ryan following imre on the streets (location 1)
    with dissolve

    pause 0.6

    scene v13s11_16 # TPP. MC and ryan following imre on the streets (location 2)
    with dissolve

    pause 0.6

    scene v13s11_17 # TPP. MC and ryan following imre on the streets (in front of the bar)
    with dissolve

    pause 0.75

    scene v13s11_18 # FPP. Imre in front of the bar doors, flipping them off
    with dissolve

    pause 0.6

    scene v13s11_19 # TPP. MC and ryan going into the bar
    with dissolve

    pause 0.6

    scene v13s11_20 # TPP. MC and ryan sitting in a table at a distance from imre
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music music.ck1.v13.Track_Scene_11_2 fadein 2

    scene v13s11_21 # FPP. MC sitting from the other side of the table from ryan, with a view to imre, imre waiting in the back, ryan slight smiling, mouth closed
    with dissolve

    u "Looks like he beat his date..."

    scene v13s11_21a # FPP. same as 21, mouth opened
    with dissolve

    ry "We don't know what the girl, or guy, looks like. *Laughs* Who knows if they're here already..."

    scene v13s11_21
    with dissolve

    u "That's true. Let's hope this is legit."

    scene v13s11_21b # FPP. Imre in the back looking back at mc and ryan, imre's mouth opened
    with dissolve

    imre "*Inaudible*"

    scene v13s11_21
    with dissolve

    u "Looks like he's trying to figure out what the hold up is."

    scene v13s11_21a
    with dissolve

    ry "His date probably needed to shave his beard. *Chuckles*"

    scene v13s11_21
    with dissolve

    u "*Chuckles*"

    scene v13s11_21c # FPP. same as 21 fat and ugly guy sits next to imre
    with dissolve

    u "Oh, shit... Let's get closer."

    scene v13s11_22 # TPP. MC and ryan moving to a closer table
    with dissolve

    pause 0.6

    scene v13s11_23 # FPP. Now closer to imre's table, ryan sitting on the other side of the table, with a view to imre, imre sitting next to ugly guy, weirded out, looking away, ryan's mouth opened
    with dissolve

    ry "Haha!"

    scene v13s11_23a # FPP. A bar host approaches imre's table, ashton is really comfortable, mouth opened
    with dissolve

    ash "May I get a Biz Light?"

    scene v13s11_23b # FPP. Bar's host face is a little weirded out, mouth opened
    with dissolve

    barh "Umm... Sure."

    scene v13s11_23c # FPP. Bar host left the table, Ash puts his hand on imre's shoulder, with a smile on his face, mouth opened
    with dissolve

    ash "You aren't gonna say hi to me?"

    scene v13s11_23d # FPP. Imre takes ash's hand off his shoulder and has a freaked out face, mouth opened
    with dissolve

    imre "Bro, why are you touching me?"

    scene v13s11_23e # FPP. Ash poining his hands at his face, smiling, mouth opened
    with dissolve

    ash "That's a rude first impression... Don't you recognize me?"
    
    scene v13s11_23f # FPP. Imre with a mad face, mouth opened
    with dissolve

    imre "I have no idea who you are or what the hell you're talking about."

    scene v13s11_23e
    with dissolve

    ash "It's me, Ashton."

    scene v13s11_23f
    with dissolve

    imre "Don't play with me right now, where's the real Ashton?!"

    scene v13s11_23e
    with dissolve

    ash "I am the real Ashton, silly... I haven't updated my pictures in a while, but-"

    scene v13s11_23g # FPP. Imre stands up, looking really mad at ash, mouth opened
    with dissolve

    imre "You also have a fucking dick! You actually are a god damn catfish!"

    scene v13s11_23g
    with dissolve

    u "(This isn't gonna be good.)"

    scene v13s11_23h # FPP. Same as 23g, ash slight smiling looking at imre, imre's mouth closed ash mouth open
    with dissolve

    ash "It's not about how people look on the outside, it's about who we are on the inside..."
    
    scene v13s11_23g
    with dissolve

    imre "Please, shut the fuck up..."

    scene v13s11_23h
    with dissolve

    ash "You liked me over the phone, right? Or at least that's what I could tell from the pictures..."
    
    scene v13s11_23g
    with dissolve

    imre "I liked the girl in the pictures!"

    scene v13s11_23l # FPP. Same as 23g, imre's hand on his head
    with dissolve

    imre "I'm only gonna say this one time... It's best you leave because right now, you got me beyond pissed off."

    scene v13s11_23i # FPP. Ash grabs one of imre's hand, imre looks freaked out, ash mouth opened
    with dissolve

    ash "Imre, please."

    scene v13s11_23j # FPP. Imre uppercuts ashton
    with dissolve

    pause 0.6

    scene v13s11_23k # FPP. Ashton hits the ground, imre looking really mad, mouth opened
    with dissolve

    imre "I SAID I WAS ONLY GONNA SAY IT ONCE! GET. OUT."

    scene v13s11_24 # FPP. Angle change as if MC and ryan moved out of their table and are standing, ash is in the ground holding his face and crawling backwards, mouth opened
    with dissolve

    ash "You're c-crazy, man! You're f-fucking crazy!"

    scene v13s11_24a # FPP. Ashton gets up, hands still covering his face
    with dissolve

    pause 0.6

    scene v13s11_25 # FPP ashton runs out of the bar, back to the camera
    with dissolve

    pause 0.75

    scene v13s11_24b # FPP, MC looking at ryan, who is laughing
    with dissolve

    ry "*Laughs*"

    scene v13s11_24c # FPP. Imre is now standing in front of mc and ryan, looking really mad, mouth opened
    with dissolve

    imre "Shut the fuck up, Ryan! Before I rock your shit too."

    scene v13s11_24b
    with dissolve

    ry "Ha! You can try... Told your ass it was a catfish."

    scene v13s11_24c
    with dissolve

    imre "You know what..."

    scene v13s11_24d # TPP. Imre still really mad, walking towards ryan
    with dissolve

    pause 0.6

    scene v13s11_26 # TPP. MC puts himself between ryan and imre holding them both
    with dissolve

    pause 0.6

    scene v13s11_27 # FPP. MC between imre and ryan, looking at imre who still has a mad expression on, mouth closed
    with dissolve

    u "Chill, chill, chill... We all know you're upset, and have good reason to be."

    scene v13s11_27
    with dissolve

    u "Don't take it out on us, especially Ryan. It was his idea to follow you here and make sure you were good."

    scene v13s11_27a # FPP. Same as 27, mouth opened
    with dissolve

    imre "Yeah, whatever."

    stop music fadeout 3
    play music music.ck1.v13.Track_Scene_11_3 fadein 2

    scene v13s11_27b # FPP. The bar hosts walks by, standing besides imre, mouth opened
    with dissolve

    barh "I never like to assume, despite the number of times this happens... But, that guy has been pulling this stunt ever since I started working here. I always feel bad because I know his past..."

    scene v13s11_27c # FPP. Imre looking at the bar host, mouth opened
    with dissolve

    imre "You need to ban his ass."

    scene v13s11_27d # FPP. Same as 27b, bar host looking at imre, mouth opened
    with dissolve

    barh "So he can invite you somewhere else? At least here I can protect the victims if they can't protect themselves."

    scene v13s11_27d
    with dissolve
    
    barh "Plus... After what you just did, I don't think there'll be any more."
    
    scene v13s11_27c
    with dissolve

    imre "Man, fuck this... I'm out of here."

    scene v13s11_27e # FPP. Imre turns his back to mc and the bar host starting to walk out, bar host looking at him, mouth open
    with dissolve

    barh "Wait!"

    scene v13s11_27f # FPP. Imre looking at the bar host, sighing, mouth opened
    with dissolve

    imre "*Sighs?* Yeah?"

    scene v13s11_27g # FPP. Bar host looking at imre, mouth opened
    with dissolve

    barh "Look... I don't know your situation, who you are, or what you're looking for, but I do know there's a Simplr event coming up within the next few days. With real girls looking to meet real guys, like yourself."
    
    scene v13s11_27h # FPP. Same as 27g, mouth closed
    with dissolve

    imre "I'm listening, go on..."

    scene v13s11_27i # FPP. Same as 27g, bar host is smiling, mouth opened
    with dissolve

    barh "*Laughs* The event is being hosted right here actually and I'll be the one hosting."
    
    scene v13s11_27g
    with dissolve

    barh "I barely know all the details myself, but it's on their website. Come by and maybe you'll get something good out of this whole situation."
    
    scene v13s11_27j # FPP. Imre looking at MC, mouth opened
    with dissolve

    imre "You guys wanna go?"

    scene v13s11_27k # FPP. Same as 27j, mouth closed
    with dissolve

    u "For sure. I don't see why not."

    scene v13s11_27l # FPP. Looking at ryan, mouth opened
    with dissolve

    ry "Yeah, I'll go."

    scene v13s11_27m # FPP. Imre looking at ryan with a mad face, mouth opened
    with dissolve

    imre "I was asking [name]."

    scene v13s11_27n # FPP. Same as 27m, mouth closed
    with dissolve

    u "*Sighs*"

    scene v13s11_27o # FPP. Bar host smiling, mouth opened
    with dissolve

    barh "Guess I'll see you guys that night! Have a good evening, and thanks again."

    if v13_penelope_concert or v13_aubrey_concert:
        scene v13s11_28 # FPP. Angle change, ryan and imre standing in front of mc, mouth closed
        with dissolve

        u "I need to hurry and get back to the hotel, I got plans tonight."

    else:
        scene v13s11_28
        with dissolve
        
        u "Are we done here or do you have another date?"

    scene v13s11_28a # FPP. same as 28, imre's mouth opened 
    with dissolve

    imre "Yeah, I'm done here. Let's go."

    scene v13s11_29 # TPP. Imre mc and ryan walking off the bar
    with dissolve

    pause 0.6

    scene v13s11_30 # TPP. Imre mc and ryan in the sidewalk
    with dissolve

    pause 0.6

    scene v13s11_31 # TPP. MC ryan and imre in front of the hotel
    with dissolve

    pause 0.6

    scene v13s11_32 # TPP. MC ryan and imre in the hotel lobby
    with dissolve

    pause 0.75

    scene v13s11_33 # FPP. Now on the hotel lobby, ryan walks off
    with dissolve

    pause 0.6

    stop music fadeout 3
    play music music.ck1.v13.Track_Scene_11_4 fadein 2

    scene v13s11_33a # FPP. looking at imre, mouth closed
    with dissolve

    u "Hey, Imre?"

    scene v13s11_33b # FPP. Same as 33, mouth opened
    with dissolve

    imre "Yeah?"

    scene v13s11_33a
    with dissolve

    u "Look, man... I'm really sorry about what went down. You didn't deserve any of it."

    scene v13s11_33b
    with dissolve

    imre "I don't exactly wanna talk about it, but... I'm sure Ryan is gonna have a field day with this."

    menu:
        "Leave it alone":
            scene v13s11_33a
            with dissolve

            u "(I'm not getting involved in it.)"

        "Stick up for Ryan":
            if mc.frat == Frat.WOLVES:
                $ reputation.add_point(RepComponent.TROUBLEMAKER)
            else:
                $ reputation.add_point(RepComponent.BRO)
        
            scene v13s11_33a
            with dissolve

            u "Look man, you need to ease up on Ryan. He stuck his head out for you today and called me because he cared about you getting catfished... Maybe this can bridge the gap for you two."

            scene v13s11_33b
            with dissolve

            imre "I doubt it."

            scene v13s11_33a
            with dissolve

            u "*Sighs* Don't say I never tried."

    scene v13s11_33b
    with dissolve

    imre "Well... Later man."

    scene v13s11_33a
    with dissolve

    u "Later,"

    scene v13s11_33c # FPP. Imre walks off
    with dissolve

    u "(Hmm, I wonder what'll go down at that event. Definitely gonna be interesting.)"

    stop music fadeout 3

    if v13_aubrey_concert:
        jump v13s12a

    elif v13_penelope_concert:
        jump v13s12b

    else:
        jump v13s12c