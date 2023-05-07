# SCENE 11: 11) MC at Lindsey's Room
# Locations: Lindseys room
# Characters: MC (Outfit 1), Lindsey(Outfit 1)
# Time: Sunday Morning

label v10_linds_room:
    scene v10slds1 # TPP. Show MC arriving at the door to Lindsey's house and knocking. Normal expression, mouth closed.
    with fade

    play sound sound.knock

    play music "music/v10/Track Scene 11.mp3" fadein 2

    pause 0.75
    
    scene v10slds1a # TPP. Same camera as v10slds1. Show MC and Lindsey. Lindsey answers the door. Sad expression, mouth closed.
    with dissolve

    pause 0.75

    scene v10slds2 # FPP. Lindsey just answered the door with MC standing outside. Show Lindsey, sad expression, mouth open.
    with dissolve

    li "Hey [name], *sniffs* thanks for coming over."

    scene v10slds2a # FPP. Same camera as v10slds2. Show Lindsey, sad expression, mouth closed.
    with dissolve

    u "Of course, you seemed really upset and I just wanted to make sure everything was okay."

    scene v10slds2
    with dissolve

    li "It really means a lot to me... I just needed someone to talk to."

    scene v10slds2a # FPP. Same camera as v10slds2. Show Lindsey, sad expression, mouth closed.
    with dissolve

    u "We all do sometimes."

    scene v10slds3 # FPP. MC and Lindsey are in Lindsey's room, sitting on her bed. Show Lindsey, sad expression, mouth open.
    with fade

    li "Do you ever feel like life just never slows down? Like as soon as things start to mellow out here comes that next big thing?"

    scene v10slds3a # FPP. Same camera as v10slds3. Show Lindsey, sad expression, mouth closed.
    with dissolve

    u "Yeah, especially since college started. Even though it can be exciting it's still just a lot sometimes."

    scene v10slds3
    with dissolve

    li "Before you came to college what was your life like? Big family, small family, parents?"

    scene v10slds3a
    with dissolve

    u "Uhm... my life was alright."

    u "My mom was always quite a... uhm... cold person. When I was a kid she just really wanted to travel the world, so she and my dad split and I stayed with him."
    
    u "Then he married my stepmom Julia. But you could tell that this wasn't the kind of family he wanted. It seemed like he saw our family as broken."

    u "So at some point he just got really distant, cheated on Julia and started a new family."

    u "I really liked her though and as I was already quite old at that point, I just decided to stay with her."

    u "It's not like my dad wanted me to go with him anyway."

    scene v10slds3
    with dissolve

    li "Oh... I'm sorry you had to go through that."

    scene v10slds3a
    with dissolve

    u "Don't get me wrong, it wasn't all that bad."

    u "Living as if you're an only child with a stepmother that's set on spoiling you."

    u "Lots of love and attention in order to make up for the lack of blood relation isn't the worst life in the world. *Chuckles*"

    scene v10slds3b # FPP. Same camera as v10slds3. Show Lindsey, uncomfortable expression, mouth closed.
    with dissolve
    
    pause 0.75

    scene v10slds3a
    with dissolve

    u "I'm sorry, I shouldn't be talking about me, I came over here for you. Mind telling me what's got you down?"

    scene v10slds3
    with dissolve

    li "Well, I'm not sure if you've heard or not, but recently my mother passed away."

    li "And this morning... it just kinda hit me. I thought I was doing fine, I was distracted and I didn't even think about it much, you know?"

    li "But when I woke up... my world just collapsed..."

    scene v10slds3a
    with dissolve

    menu:
        "Yeah, I heard":
            scene v10slds3a
            with dissolve

            u "Yeah, I heard. I'm really sorry for your loss."
            
            u "I kinda assumed that's why you're upset, but I didn't wanna bring it up, in case it was something else."

            scene v10slds3
            with dissolve

            li "If you've heard about it then I'm sure others have as well *sighs*, we all know bad news travels faster than good news."

        "No, I had no clue":
            scene v10slds3a
            with dissolve

            u "Oh my God, no I hadn't heard. I'm so sorry for your loss."

            scene v10slds3
            with dissolve

            li "I'm kinda glad you haven't heard. People not knowing makes it easier to ignore..."

    scene v10slds3a
    with dissolve
    
    u "So... were you guys close? You and your mom?"

    scene v10slds3c # FPP. Same camera as v10slds3. Show Lindsey, with a sad (wistful) smile, mouth open.
    with dissolve

    li "Close would be an understatement. *Chuckles* My mother and I did everything together and she knew everything about me. She was so beautiful too."

    li "When we used to travel people would think we were sisters. Sometimes when we went on vacations we'd act as if we were sisters and flirt with guys."
    
    li "We goofed off a lot, but it was always so much fun with her."

    scene v10slds3d # FPP. Same camera as v10slds3. Show Lindsey, with a sad (wistful) smile, mouth closed.
    with dissolve

    u "Honestly, I'm fortunate enough that I haven't had to experience losing someone I'm really close to. I can't even begin to imagine that kind of pain that is."

    scene v10slds3c
    with dissolve

    li "It hurts, but my mother raised me to believe a piece of our loved ones are always with us in some way."

    li "Every time I look in the mirror, or hear my laugh I see my mother. We really had that much in common. She cared so much about me, sometimes too much."

    scene v10slds3d
    with dissolve

    u "Wow... that's a really beautiful thought."

    scene v10slds3c
    with dissolve

    li "In a way, she really was my North Star. I never did anything without her input." 

    li "She always knew what I needed to hear and now here I am without her and I have no idea what I'm going to do."

    li "I don't have the motivation to do anything. School seems pointless, home seems pointless, everything seems pointless."

    li "I know it's okay to be sad, but sometimes I'm not just sad... I get really angry... I just... I can't believe she's really gone. And she's never coming back."

    scene v10slds3d
    with dissolve

    menu:
        "Keep listening":
            scene v10slds3c
            with dissolve
            
            li "Sad thing is, I spent so much time with my mother and our personalities resemble each other so much that even though she's not here I know EXACTLY what she would say."

            scene v10slds3d
            with dissolve

            u "And what is it she'd say?"

            scene v10slds3c
            with dissolve

            li "\"Stop moping, start hoping!\" Haha, she said the same thing anytime I was sad ever since I was a little girl."

            li "Being sad around my mother was a big no no. My mother had this \"always be positive\" attitude about her."

            scene v10slds3d
            with dissolve

            menu:
                "Talk about her mother":
                    scene v10slds3d
                    with dissolve
                   
                    u "Your mother seems very wise."

                "Talk about her":
                    scene v10slds3d
                    with dissolve
                    u "Sometimes it's good to be sad."

                    scene v10slds3c
                    with dissolve

                    li "You really are a good listener. I knew reaching out to you was the best thing I could do."

                    li "Honestly, just venting it all out already has me feeling a lot better."

        "Make a joke":
            if reputation() == Reputations.CONFIDENT:
                scene v10slds3e # FPP. Same camera as v10slds3. Show Lindsey, with a somewhat amused smile, mouth closed.
                with dissolve

                u "Hey, at least you're not gonna end up like that sailor that followed the North Star and ended up freezing to death in a snow storm, right?"

                call screen reputation_popup
                
                scene v10slds3f # FPP. Same camera as v10slds3. Show Lindsey, with a somewhat amused smile, mouth open.
                with dissolve

                li "Haha, that's true. Guess that wasn't the best reference."

                scene v10slds3e
                with dissolve

                u "Haha, just teasing you."

                scene v10slds3f
                with dissolve

                li "Haha, yeah I know I know. It does suck though because even though I'm wishing my mother was here to talk to me I already know exactly what she would say if she was."

                scene v10slds3e
                with dissolve

                u "And what is it she'd say?"

                scene v10slds3f
                with dissolve

                li "\"Stop moping, start hoping!\" She never let me walk around sad, even when I wanted to."
                
                li "My mom was positive even when being positive was hard. So I guess I kinda already know what I need to do."

                scene v10slds3e
                with dissolve

                menu:
                    "Speak on her mother":
                        scene v10slds3e
                        with dissolve
                        
                        u "Your mother seems very wise."

                        scene v10slds3c
                        with dissolve

                        li "Yeah... she was."

                    "Speak on her":
                        scene v10slds3e
                        with dissolve

                        u "Sometimes it's good to be sad."

            else: # RCS - kct is not confident
                $ sadlind_reaction = True # RCS - variable for MC getting bad reaction from Lindsey
                
                scene v10slds3d
                with dissolve
                
                u "Hey, at least you're not gonna end up like that sailor that followed the North Star and ended up freezing to death in a snow storm, right?"

                scene v10slds3c
                with dissolve

                li "What?"

                scene v10slds3d
                with dissolve

                u "Oh, it was just- it was just a joke..."

                scene v10slds3c
                with dissolve

                li "Yeah... I don't really feel like I can get into a joking spirit right now."

                scene v10slds3d
                with dissolve

                u "Oh uhm my bad, thought I'd try lightening the mood."

                scene v10slds3c
                with dissolve

                li "It's fine, because I wish my mother was here... but I also already know exactly what she'd say."

                scene v10slds3d
                with dissolve

                u "And that is?"

                scene v10slds3f
                with dissolve

                li "\"Stop moping, start hoping!\" She never let me walk around sad, even when I wanted to."

                li "My mom was positive even when being positive was hard. So I guess I kinda already know what I need to do."

                scene v10slds3e
                with dissolve

                menu:
                    "Speak on her mother":
                        scene v10slds3e
                        with dissolve

                        u "Your mother seems very wise."

                        scene v10slds3c
                        with dissolve

                        li "Yeah... she was."

                    "Speak on her":
                        scene v10slds3e
                        with dissolve
                    
                        u "Sometimes it's good to be sad."


    scene v10slds3d 
    with dissolve

    u "I'm just happy you feel a bit better."

    scene v10slds3c
    with dissolve

    li "I wouldn't feel better if it wasn't for you. I'm glad I called you before anyone else."

    scene v10slds3g # FPP. Same camera as v10slds3. Show Lindsey, looking away from MC with her hand on her ear, a bit of a thoughtful/shy expression, mouth closed.
    with dissolve

    pause 0.75

    scene v10slds3f
    with dissolve

    li "I'm sorry I don't know if I should've been as forward and flirty as I was before."

    scene v10slds3e
    with dissolve

    menu:
        "I like it":
            if reputation() == Reputations.CONFIDENT:
                scene v10slds3e
                with dissolve
                u "I'd never say no to any attention you wanted to give."

                call screen reputation_popup

                scene v10slds3f
                with dissolve

                li "Really? I just may have to take you up on that sometime."

                scene v10slds3e
                with dissolve

                u "Just say the word."

            else: # RCS - MC is not KCT confident
                $ sadlind_reaction = True # RCS - variable for MC getting bad reaction from Lindsey

                scene v10slds3d
                with dissolve
                u "I'd never say no to any attention you wanted to give."

                scene v10slds3c
                with dissolve

                li "I'm just not sure this is the best time..."

                scene v10slds3b
                with dissolve

                u "Uhm yeah... no... I get that. We don't have to, you know... ugh nevermind."
   
        "I understand":
            scene v10slds3e
            with dissolve

            u "Oh, don't worry about it. You're going through stuff, I completely understand."

            scene v10slds3f
            with dissolve

            li "Thanks [name], that really means a lot to me."

            scene v10slds3e
            with dissolve

            u "Anytime."

    scene v10slds3c
    with dissolve

    li "Thanks for coming [name]."

    scene v10slds3d
    with dissolve

    u "Yeah, of course."

    if not sadlind_reaction: # -If no bad reaction (no flirting, no joke without KCT)-
        scene v10slds4 # TPP. Show Lindsey leaning over and hugging MC while they sit on the bed. MC facing away from camera. Lindsey has a little smile, mouth open.
        with dissolve

        li "I'm sure I've taken up enough of your day with all my sad talk, I'll stop holding you hostage. Hopefully I'll see you soon."

        scene v10slds4a # TPP. Same camera as v10slds4. Show Lindsey leaning over and hugging MC while they sit on the bed. MC facing away from camera. Lindsey has a little smile, mouth closed.
        with dissolve

        u "I'll make sure you do."

        scene v10slds5 # TPP. Show MC leaving Lindsey's house. She is standing in the open doorway, watching him leave with a little smile, mouth closed.
        with fade

    else: # -If bad reactions-
        scene v10slds3c
        with dissolve
        
        li "So uhm, I guess I should let you go huh?"

        scene v10slds3d
        with dissolve

        u "As long as you're feeling okay."

        scene v10slds3c
        with dissolve

        li "Yeah I'm feeling fine."

        scene v10slds3d
        with dissolve

        u "Good to hear. Guess I'll see you around."

        scene v10slds3c
        with dissolve

        li "Yeah, see you [name]."

        scene v10slds5a # TPP. Same camera as v10slds5. Show MC leaving Lindsey's house. The door is closed behind him. (Lindsey is not in sight.)
        with fade

    stop music fadeout 3

if joinwolves: # I don't know this variable name
    jump v10_wolves_redec

else: # RCS - if MC is an ape?
    jump v10_apes_samantha



