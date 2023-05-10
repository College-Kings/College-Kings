# SCENE 26: Your Room Fri Night
# Locations: MC Wolves Room/Wolves gym
# Characters: MC (Outfit 3) Chris (Outfit 1), Imre (Outfit 3), Perry (Outfit 2)
# Time: Friday Night

label v9_fri_training_w_wolves:
    scene v9tww1 # TPP. Show Chris walking into MC's room.
    with dissolve

    pause 0.75

    scene v9tww2 # FPP. Show Chris, Chris looking into camera (Camera as if MC sat on bed), Chris neutral expression, mouth closed.
    with dissolve

    u "Hey, how's it going?"

    scene v9tww2a # FPP. Same camera as v9tww2, Chris neutral expression, mouth open.
    with dissolve

    ch "Good. Just getting some of the guys together in the gym. Can you join us?"

    scene v9tww2
    with dissolve

    u "Yeah, sure. I'm not doing anything."

    scene v9tww2a
    with dissolve

    ch "Great, thanks. Sorry it's such short notice."

    scene v9tww2
    with dissolve

    u "Hey, don't worry about it. Saves me from passing out on my History book again."

    scene v9tww2b # FPP. Same camera as v9tww2, Chris laugh, mouth open.
    with dissolve

    ch "I know what you mean. Haha."

    scene v9tww3 # TPP. Show Chris and MC leaving MC's room, MC following behind Chris.
    with dissolve
    
    pause 0.75
      
    scene v9tww4 # TPP. Show MC, Imre and Perry stood in a line next to eachother, Chris stood opposite to them. (Now in Wolves gym)
    with fade

    pause 1

    play music music.ck1.v9.Track_Scene_1 fadein 2

    scene v9tww5 # FPP. Show Chris, neutral expression, mouth open.
    with dissolve

    ch "I'm sure you can guess why I brought you guys here tonight."

    scene v9tww5a # FPP. Same camera as v9tww5, neutral expression, mouth closed.
    with dissolve

    menu: 
        "Answer": 
            $ reputation.add_point(RepComponent.BRO)

            u "The Brawl."

            scene v9tww5
            with dissolve

            ch "Right."

        "Keep quiet":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
    
            pause 1

            scene v9tww5
            with dissolve

            ch "Don't be shy."

            guyd "Uhh, the Brawl?"

            scene v9tww5b # FPP. Same camera as v9tww5, Chris not looking at Camera, but looking where Perry would be in the line, neutral expression, mouth open.
            with dissolve

            ch "Thank you."

    scene v9tww5c # FPP. Same camera as v9tww5, Chris pacing the room, neutral expression, mouth open.
    with dissolve

    ch "I'm sure you all thought about getting in a bunch of workouts before tomorrow's fight, and I appreciate your dedication."

    scene v9tww5d # FPP. Same camera as v9tww5, Chris pacing the room elsewhere, neutral expression, mouth closed.
    with dissolve
    u "(It's like he read my mind.)"

    scene v9tww5e # FPP. Same camera as v9tww5, Chris now stops in whatever position he paced to before, looking back at camera, neutral expression, mouth open.
    with dissolve

    ch "But you have to be careful. There's a fine line between getting in the zone and hitting the wall."

    scene v9tww5f # FPP. Same camera as v9tww5, Chris in same position as v9tww5e, neutral expression, mouth closed.
    with dissolve

    menu: 
        "Make joke": 
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            u "I think punching an Ape's thick skull is gonna be like hitting a wall."

            scene v9tww5e
            with dissolve

            ch "Yes, I'm sure it will be."

        "Agree":
            $ reputation.add_point(RepComponent.BRO)

            u "(I don't want to interrupt.)"
   
    scene v9tww5e
    with dissolve

    ch "I can almost guarantee you Grayson's running your competition into the ground right now."

    scene v9tww6 # TPP. Show Imre, Imre looking disgusted (Like ewww what's that smell), mouth open.
    with dissolve

    imre "Ugh. Could you imagine the stench in that gym?"

    scene v9tww7 # TPP. Show Perry, same expression as Imre in v9tww6, mouth open.
    with dissolve

    guyd "Gross. Don't make me think about that."

    scene v9tww5g # FPP. Same camera as v9tww5, Chris pacing back to the same position priot to v9tww5c (center to camera), neutral expression, mouth open.
    with dissolve

    ch "I wanna win this thing just as bad as the Apes wanna win, maybe more since Grayson's already got the title on his side."

    scene v9tww5a
    with dissolve

    if hl_punch:
        u "Not for long."

        scene v9tww8 # FPP. Show Chris, stood every close to MC, smile, mouth open.
        with dissolve

        ch "Not if you have anything to say about it, huh?"

        scene v9tww8a # FPP. Same camera as v9tww8, Chris mouth closed.
        with dissolve

        u "Damn right!"

        scene v9tww9 # TPP. Show Chris with his hand on MC's shoulder, Perry and Imre looking at Chris, MC smile, Chris smile, mouth open.
        with dissolve

        ch "I can't tell you if the Apes will be harder to beat than that guy, but they certainly won't be easier. The Apes have a proven track record in the ring."

        ch "But... now we have our champ here. I know for a fact those Apes are shitting their pants after that knockout."

        scene v9tww9a # TPP. Same camera as v9tww9, all smiling, Imre mouth open.
        with dissolve

        imre "As they should!"
        
    else:
        u "(What did I get myself into?)"

        scene v9tww9b # TPP. Same camera as v9tww9, neutral expressions, MC looks slightly worried, Chris mouth open.
        with dissolve

        ch "It's important we don't get stuck in our own heads."

        scene v9tww10 # TPP. Show Chris stood infront of MC but looking at Imre, everyone looking at Chris, neutral expressions, Chris mouth open.
        with dissolve
        
        ch "Nothing that happened before this moment will matter tomorrow. We're all in this together."

    
    scene v9tww5
    with dissolve

    ch "Now! What we're gonna do is work on form. Keep your cover. Watch for weaknesses, openings. Never drop your guard."

    scene v9tww11 # TPP. Show Chris pointing at Imre and MC, Chris mouth open.
    with dissolve

    ch "You two spread out a bit."

    scene v9tww11a # TPP. Same camera as v9tww11, Chris no Longer pointing, MC now further away from Perry, Imre now further away from MC, Chris smile, mouth open.
    with dissolve

    ch "Alright! Let's get you guys in fighting shape!"

    scene v9tww5a
    with dissolve

    u "Yeah!"

    guyd "Woo!"

    imre "Let's do this!"

    scene v9tww5
    with dissolve

    ch "You're all Wolves now! And by the time we're done here, you're gonna show those Ape pledges what real fighting looks like."

    ch "You're gonna fight like champs tomorrow!"

    scene v9tww5h # FPP. Same camera as v9tww5, same pos as v9tww5, Chris yelling, mouth open.
    with dissolve

    ch "*Yelling* Who are you?"

    scene v9tww5i # FPP. Same camera as v9tww5, same pos as v9tww5, Chris smile, mouth closed.
    with dissolve

    u "WE ARE WOLVES!"

    scene v9tww5h
    with dissolve

    ch "And what are you gonna do?"

    scene v9tww5i
    with dissolve

    guyd "Fight like champs!"
    
    scene v9tww5
    with dissolve

    ch "Damn right!"

    ch "Imre, I want you over on the weight bench. Get those arms pumped!"

    scene v9tww12 # FPP. Show Imre walking over to the weight bench.
    with dissolve

    imre "Woo!"

    scene v9tww5
    with dissolve

    ch "Perry, hit the jump rope. Let's get that stamina up!"

    ch "And [name], I want you on the punching bag."

    scene v9tww13 # TPP. Show MC walking over to the punching bag, Chris following behind him.
    with dissolve

    pause 0.75
    
    scene v9tww14 # TPP. Show MC punching the bag whilst Chris watching.
    with dissolve

    pause 0.75

    if hl_punch:
        scene v9tww14a # TPP. Same camera as v9tww14, MC punching harder, Chris watching, mouth open.
        with dissolve

        ch "We're counting on you to bring that magic tomorrow, but chances are you won't get a KO right out of the corner."

        scene v9tww15 # FPP. Show Chris, neutral, mouth closed.
        with dissolve
        
        menu: 
            "Be cocky": 
                $ reputation.add_point(RepComponent.TROUBLEMAKER)

                u "Never know."

                scene v9tww15a # FPP. Same camera as v9tww15, neutral, mouth open.
                with dissolve

                ch "You're right, but we gotta plan for the worst case scenario."

                scene v9tww15
                with dissolve

                u "What's that?"

            "Agree":
                $ reputation.add_point(RepComponent.BRO)

                u "Yeah that was kinda lucky."

                scene v9tww15a
                with dissolve

                ch "I'm sure there's some skill in there, too. But we gotta be prepared."

        scene v9tww15a
        with dissolve

        ch "We have to assume the whole school has seen your video by now."

        scene v9tww15
        with dissolve

        u "Sure feels like it."

        scene v9tww15a
        with dissolve

        ch "Right, so now the Apes know what you're capable of."

        scene v9tww15
        with dissolve

        u "Shit."

        scene v9tww15a
        with dissolve

        ch "Exactly. No element of surprise."

        scene v9tww15
        with dissolve

        u "Aww, sorry, man. I wasn't thinking."

        scene v9tww15a
        with dissolve

        ch "No, that guy had it coming. Don't worry. It just means we have to come up with something better. Something they aren't expecting."

        scene v9tww15
        with dissolve

        u "And what's that?"

        scene v9tww15a
        with dissolve

        ch "We gotta fake 'em out."

        scene v9tww15
        with dissolve

        u "Okay. How?"

        scene v9tww15a
        with dissolve

        ch "If you knew someone could knock you out in one punch, what would you do?"

        scene v9tww15
        with dissolve

        menu: 
            "Hit first": 
                $ reputation.add_point(RepComponent.BRO)

                u "Hit first."

                scene v9tww15a
                with dissolve

                ch "Right! That's what they're gonna do. Come out swinging."

                scene v9tww15
                with dissolve

                u "Sooooo?"

                scene v9tww15a
                with dissolve

                ch "So you have to be ready for it."

            "Run":
                $ reputation.add_point(RepComponent.TROUBLEMAKER)

                u "Run!"

                scene v9tww15b # FPP. Same camera as v9tww15, smile, mouth open.
                with dissolve

                ch "You say that now, but you had the chance to run already and didn't. You chose fight over flight."

                scene v9tww15c # FPP. Same camera as v9tww15, smile, mouth closed.
                with dissolve

                u "I didn't choose anything... I don't think."

                scene v9tww15a
                with dissolve

                ch "You're hardwired to be a fighter. So let's use that to our advantage."

        ch "Now, this is gonna feel wrong, but trust me, OK?"

        ch "I want you to back up."

        scene v9tww16 # TPP. Show MC backing up, Chris smile, mouth open.
        with dissolve

        ch "No! Not now! Tomorrow. When the fight starts and you have an Ape charging at you, step back."

        ch "He won't expect you to retreat right away. And that's when you get him!"

        scene v9tww17 # FPP. Show Chris punching the bag hard, slip punch ref: https://static.wikia.nocookie.net/boxing/images/f/fd/Boxing-punches.gif/revision/latest/scale-to-width-down/300?cb=20180528173756
        with dissolve

        u "Whoa!"

        scene v9tww17a # FPP. Show Chris, now looking at camera, smile, mouth open.
        with dissolve

        ch "Whoa is right. All his weight will be on that front leg. He'll practically punch himself with your fist!"

        scene v9tww14a
        with dissolve

        ch "Nice! Let's practice a few of those. I'm gonna check on the other guys."

        scene v9tww14b # TPP. Same camera as v9tww14, MC punches the bag again, Chris watching, mouth open.
        with dissolve

        ch "You're gonna make us proud, man. I have faith in you."

    else:
        scene v9tww14a
        with dissolve

        ch "I know you're probably replaying what happened over and over, but we're gonna get you out of your head."

        scene v9tww15
        with dissolve

        u "Nah, I'm not in my head."

        menu:
            "Act cool":
                $ reputation.add_point(RepComponent.TROUBLEMAKER)

                scene v9tww15a
                with dissolve

                ch "Hey, anyone would be. Don't sweat it. We got this."

                scene v9tww15
                with dissolve

                u "How?"

            "Ask for help":
                $ reputation.add_point(RepComponent.BRO)

                u "I need it. I don't know what happened."

                scene v9tww15a
                with dissolve

                ch "Seriously, don't let it get to you. Nobody knows how they'll react in a situation like that until it happens to them."

                scene v9tww15
                with dissolve

                u "I'm not much of a fighter if I can't defend myself against one random asshole."

                scene v9tww15a
                with dissolve

                ch "That's not what I saw."

                ch "I saw someone try to avoid a public confrontation."

                scene v9tww15
                with dissolve

                u "(I guess he's half right.)"

                scene v9tww15a
                with dissolve

                ch "So what happened in the end is on that guy, not you."

                scene v9tww15
                with dissolve

                u "Okay."

                scene v9tww15
                with dissolve

                ch "But tomorrow's different. You're gonna be up against real opponents who are expecting a full on fight. We gotta give it to 'em."

                scene v9tww15
                with dissolve

                u "And how do I do that?"

        scene v9tww15a
        with dissolve

        ch "Like this."

        scene v9tww17
        with dissolve

        u "Shit!"

        scene v9tww17a
        with dissolve

        ch "Let's be real."

        scene v9tww17b # FPP. Same camera as v9tww17b, smile, mouth closed.
        with dissolve

        u "Okay."

        scene v9tww17a
        with dissolve

        ch "They aren't scared of you right now." 

        scene v9tww17b
        with dissolve
    
        menu:
            "Agree":
                $ reputation.add_point(RepComponent.BRO)

                u "Yeah, I know."

                scene v9tww17a
                with dissolve

                ch "So we use that to our advantage."

            "Defend yourself":
                $ reputation.add_point(RepComponent.TROUBLEMAKER)

                u "I mean, it's not my first fight ever. I can still have some tricks up my sleeve."

                scene v9tww17a
                with dissolve

                ch "You're only as big as your last match, and that one didn't go your way."

                ch "But THIS is your trick up your sleeve."

                scene v9tww17b
                with dissolve

                u "They'll never see it coming."

                scene v9tww17a
                with dissolve

                ch "Exactly! Your opponent will be expecting a sniveling wimp!"

                scene v9tww17b
                with dissolve

                u "Hey!"

                scene v9tww17a
                with dissolve

                ch "But he's gonna run into a fist!"

                scene v9tww17b
                with dissolve

                u "Yeah!"

                scene v9tww17a
                with dissolve

                ch "As soon as that bell rings, I want to see blood on those knuckles!"

                scene v9tww14a
                with dissolve

                ch "Good. Good. Keep going. Timing is everything. I want you to hear the bell ring and BAM! Bloody knuckles!"

                scene v9tww14b
                with dissolve

                ch "Awesome. I'm gonna check on the other guys. You keep at it."

    scene v9tww18 # TPP. Show Chris addressing everyone in the gym, Chris mouth open.
    with fade

    ch "Alright! Time! Great job guys."

    scene v9tww19 # TPP. Show everyone in the gym lined up again looking tired with Chris stood opposite them.
    with dissolve

    pause 1

    scene v9tww20 # FPP. Show Chris, neutral, mouth open.
    with dissolve

    ch "I gotta say I'm impressed. You all did way better than I expected tonight. You've got that fighting Wolf pack spirit in you!"

    ch "Now, we've done all we can training-wise. The only thing left for you to do is rest your weapons."

    ch "Now, I want you to go back to your rooms and rest. Seriously. No parties. No booze."

    scene v9tww20a # FPP. Same camera as v9tww20, neutral, mouth closed.
    with dissolve

    u "(Please don't say no girls.)"

    scene v9tww20b # FPP. Same camera as v9tww20, smile, mouth open.
    with dissolve

    ch "Don't worry. I'm not gonna say \"no women\"."

    ch "Let's consider all forms of... stress relief... as rest, shall we?"

    scene v9tww21 # TPP. Show Imre, smile, mouth open.
    with dissolve

    imre "We shall!"

    scene v9tww20b
    with dissolve 
  
    ch "Alright, let's get out of here."

    scene v9tww22 # TPP. Show everyone leaving the gym, pledges looking tired, chris smile.
    with dissolve

    stop music fadeout 3

    pause 1

    jump v9_call_w_lindsey