
# SCENE 19: Lauren's Dorm
# Locations: Lauren's Dorm
# Characters: MC (Outfit 3), Lauren (Outfit 3)
# Time: Friday Morning

label v9_lau_dorm:
    scene v9lau1 # TPP. Show MC walking up the hallway to Lauren's dorm.
    with fade

    play music "music/v9/Track Scene 8_1.mp3" fadein 2

    pause 0.8

    play sound sound.knock

    scene v9lau2 # TPP. Show MC knocking on Lauren's dorm door.
    with dissolve

    pause 0.8

    if CharacterService.is_girlfriend(lauren):
        scene v9lau3 # FPP. Show Lauren who has just opened the door, Lauren smile, mouth closed.
        with dissolve

        u "I've missed you."

        scene v9lau3a # FPP. Same camera as v9lau3, Lauren smile, mouth open.
        with dissolve

        la "Aww, I missed you, too. Come in."

    elif CharacterService.is_kissed(lauren):
        scene v9lau3
        with dissolve

        u "You look sexy."

        scene v9lau3a
        with dissolve

        la "Uh-uh, we're here to work."

        scene v9lau3
        with dissolve

        u "Just wanted to make sure you knew how cute you were."

        scene v9lau3b # FPP. Same camera as v9lau3, Lauren giggle, mouth closed.
        with dissolve

        la "*Giggles* Come in."

    else:
        scene v9lau3
        with dissolve

        u "Hey, hope you didn't start without me."

        scene v9lau3a
        with dissolve

        la "I did, but there's still so much to do."

        scene v9lau3
        with dissolve

        u "Well, let's get to it."

    scene v9lau4 # TPP. Show MC and Lauren walking towards Lauren's desk where there is 2 chairs.
    with dissolve
    
    pause 0.8

    scene v9lau5 # TPP. Show Lauren and MC taking a seat at Lauren's desk.
    with dissolve

    pause 0.8

    scene v9lau6 # FPP. Show Lauren, Lauren looks a little stressed, mouth open.
    with dissolve

    la "Thanks for helping me. I'm kinda lost right now."

    scene v9lau6a # FPP. Same camera as v9lau, Lauren looks a little stressed, mouth closed.
    with dissolve

    u "No problem. What do you have so far?"

    scene v9lau6
    with dissolve

    la "Not much. I've been spinning my wheels a bit."

    scene v9lau6a
    with dissolve

    if CharacterService.is_kissed(lauren) or CharacterService.is_girlfriend(lauren):
        menu:
            "Offer Lauren a back rub":
                $ reputation.add_point(RepComponent.BOYFRIEND)

                u "Here, let me help."

                scene v9lau8 # TPP. Show MC stood behind Lauren giving Lauren a backrub, Lauren smile, mouth closed.
                with dissolve

                la "Mmmm..."

                scene v9lau8a # TPP. Same camera as v9lau8a, Lauren smile, mouth open.
                with dissolve

                la "That feels so nice."

                scene v9lau6c
                with dissolve

                u "Feel better?"

                scene v9lau6b
                with dissolve

                la "Yeah! Let's get to work."

            "Offer Lauren a hug":
                $ reputation.add_point(RepComponent.BOYFRIEND)
            
                u "Aww, come here."

                scene v9lau7 # TPP. Show MC and Lauren hugging.
                with dissolve

                pause 1

                scene v9lau6b # FPP. Same camera as v9lau6, Lauren smile, mouth open.
                with dissolve

                la "That was nice."

                scene v9lau6c # FPP. Same camera as v9lau6, Lauren smile, mouth closed.
                with dissolve

                u "Wasn't it? I love your hugs. Feel better?"

                scene v9lau6b
                with dissolve
                
                la "Yeah."

                scene v9lau6c
                with dissolve

                u "Good! Now fill me in."

    else:
        menu:
            "Offer guidance":
                $ reputation.add_point(RepComponent.BRO)

                u "It's simple. Start with your main goal and work your way back to what to do now."

                scene v9lau6d # FPP. Same camera as v9lau6, Lauren looks annoyed, mouth open.
                with dissolve

                la "Did you just mansplain my own event to me?"

                scene v9lau6h # FPP. Same camera as v9lau6, Lauren annoyed, mouth closed
                with dissolve

                u "Wait, what?"
                
                scene v9lau6b
                with dissolve

                la "Gotcha!"

                scene v9lau6c
                with dissolve

                u "(Whew!)"

            "Just listen":
                $ reputation.add_point(RepComponent.BOYFRIEND)

                u "What part's giving you the most trouble? How can I help?"

                scene v9lau6b
                with dissolve

                la "I still don't know what my booth will be about. So I can't move forward."

                scene v9lau6c
                with dissolve
                
                u "Well, then that's where we'll start."

    scene v9lau6
    with dissolve

    la "I'm worried I can't compete with all the other booths, and I won't raise any money."

    scene v9lau6a
    with dissolve

    u "Of course you will. You always have great ideas."

    scene v9lau6
    with dissolve

    la "Thanks but, I'm not so sure this time."

    scene v9lau6a
    with dissolve

    u "What are you up against?"

    scene v9lau6b
    with dissolve

    la "Well, Autumn's setting up a mud wrestling ring!"

    scene v9lau6c
    with dissolve

    menu:
        "Be impressed":
            u "Wow! That I gotta see!"

            scene v9lau6
            with dissolve

            la "See! This is bad."

            scene v9lau6a
            with dissolve

            u "No! We can top that!"

        "Support Lauren":
            $ reputation.add_point(RepComponent.BOYFRIEND)
        
            u "Hmm. I see why you're stressed. But don't worry. We can come up with something just as awesome."

            scene v9lau6
            with dissolve

            la "You think so?"

            scene v9lau6a
            with dissolve

            u "Of course. With your brains and my beauty, we got this."

            scene v9lau6c
            with dissolve

    if CharacterService.is_kissed(lauren) or CharacterService.is_girlfriend(lauren):
        u "How about a hand job booth?"

        scene v9lau6e # FPP. Same camera as v9lau6, Lauren looks shocked, mouth closed.
        with dissolve

        u "Everyone but you, of course."

        scene v9lau6f # FPP. Same camera as v9lau6, neutral expression, mouth open.
        with dissolve

        la "You want me to run a booth of hand jobs and not participate?"

        scene v9lau6g # FPP. Same camera as v9lau6, neutral expression, mouth closed.
        with dissolve

        u "Oh, you can participate! I'll just buy all the tickets myself. Problem solved."

        scene v9lau6b
        with dissolve

        la "Keep thinking, mister."
    
    else:
        u "I'm sure there's already a kissing booth."

        scene v9lau6f
        with dissolve

        la "Not sure, but I don't think that would compete with mud wrestling."

        scene v9lau6g
        with dissolve

        u "On a college campus full of dudes? I think you'd raise the most money."

        scene v9lau6b
        with dissolve

        la "Let's put that one on the back burner."

    scene v9lau6c
    with dissolve

    u "I wonder where we could get a hot air balloon on short notice."

    scene v9lau6b
    with dissolve

    la "Liability."

    scene v9lau6c
    with dissolve

    if joinwolves:
        u "Five bucks to punch Grayson in the face-"

    else:
        u "Five bucks to punch Chris in the face. It's for charity. He'd do it."

    scene v9lau6f
    with dissolve

    la "Violence for charity. How noble. Next."

    scene v9lau6g
    with dissolve

    u "Hmmm."

    scene v9lau6f
    with dissolve

    la "I need something that won't cause too much trouble, but still earn for the charity. See why I'm having so much trouble!"

    scene v9lau6g
    with dissolve

    u "Well, I keep thinking about the old bake sales we always had at school. But then, I also saw a living statue in the park and that was pretty awesome."

    scene v9lau6b
    with dissolve

    la "Oh, yeah. Cakes are a classic at charity events. But the living statue does sound like it would draw a crowd. I don't know. What would you do if it were your booth?"

    scene v9lau6c
    with dissolve

    menu:
        "Bake Cakes":
            u "Why don't we keep it simple and bake some cakes?"

            scene v9lau6b
            with dissolve

            la "Great. Can't go wrong with food and drinks."

            scene v9lau6c
            with dissolve

            u "Yeah... but man, the more I think about that statue."

            scene v9lau6
            with dissolve

            la "It's such a hard decision."

            scene v9lau6a
            with dissolve

            u "Yeah, I guess it comes down to which you prefer? Playing it safe, or pushing the envelope."

            scene v9lau6
            with dissolve

            la "I've never been one for pushing the envelope."

            scene v9lau6a
            with dissolve

            u "Well, that's what college is for."

        "Living Statue":
            u "I definitely would do the statue. Can you imagine?"

            scene v9lau6f
            with dissolve

            la "Seems like a lot of work. And who would we get?"

            scene v9lau6g
            with dissolve

            u "You!"

            scene v9lau6
            with dissolve

            la "Are you insane? I can't stand in front of people and have them watch me all day."

            scene v9lau6a
            with dissolve

            u "Not all day. Just long enough to earn way more money than mud wrestling!"

            scene v9lau6
            with dissolve

            la "I don't know."

            scene v9lau6a
            with dissolve

            u "Come on. It'll be fun."

    scene v9lau9 # FPP. Show Lauren getting up from her chair and beginning to pace around her room.
    with dissolve

    pause 0.75

    scene v9lau10 # TPP. Show MC getting up from the chair and going over to Lauren.
    with dissolve

    pause 0.75

    scene v9lau11 # FPP. Show Lauren (Who is now stood up in her room), Lauren looks stressed, mouth closed.
    with dissolve

    if CharacterService.is_kissed(lauren) or CharacterService.is_girlfriend(lauren):
        u "Whatever you choose, I'll be there with you."

        scene v9lau11a # FPP. Same camera as v9lau11, Lauren smile, mouth open.
        with dissolve

        la "You're so sweet."

        scene v9lau11
        with dissolve

    else: 
        u "Don't overthink it. Just go with your gut."

    u "Quick. Answer now. One... two... three!"

    scene v9lau11c # FPP. Same camera as v9lau11, Lauren excitable smile, mouth open.
    with dissolve

    la "Statues!"

    scene v9lau11b # FPP. Same camera as v9lau11, Lauren smile, mouth closed.
    with dissolve

    u "There you go! Now let's start planning."

    scene v9lau12 # FPP. Show Lauren walking back to her desk to grab a pen and piece of paper.
    with dissolve

    pause 0.75

    scene v9lau13 # FPP. Show Lauren, stood near her desk, facing camera but looking at paper, writing on paper, mouth open.
    with dissolve

    la "We'll need paint, obviously. And something to stand on."

    scene v9lau13a # FPP. Same camera as v9lau13, Lauren looking at camera, no longer writing, mouth closed.
    with dissolve

    u "Oooh, I wonder if we can get a rotating base."

    scene v9lau13
    with dissolve

    la "And a cute bucket for donations."

    scene v9lau13a
    with dissolve

    u "I'm sure some of the theater kids would have supplies."

    scene v9lau13b # FPP. Same camera as v9lau13, Lauren looking at camera, no longer writing, mouth open.
    with dissolve

    la "Good thinking."

    scene v9lau13a
    with dissolve

    u "Man, my eyes are starting to cross. I gotta move around a bit."

    scene v9lau13c # FPP. Same camera as v9lau13, Lauren looking at camera, no longer writing, smile, mouth open.
    with dissolve

    la "Of course. Thank you so much for your help. I really appreciate it."

    scene v9lau13d # FPP. Same camera as v9lau13, Lauren looking at camera, no longer writing, smile, mouth closed.
    with dissolve

    u "No problem. If you need more help, just let me know."

    scene v9lau14 # FPP. Show Lauren placing the pen and paper back on her desk.
    with dissolve

    pause 0.75

    scene v9lau15 # TPP. Show Lauren and MC walking towards Lauren's dorm door.
    with dissolve

    pause 0.75

    scene v9lau16 # FPP. Show Lauren, now stood near the door of her dorm, smile, mouth open.
    with dissolve

    if CharacterService.is_kissed(lauren) or CharacterService.is_girlfriend(lauren):
        la "You were a lifesaver."

        scene v9lau16a # FPP. Same camera as v9lau16, Lauren smile, mouth closed.
        with dissolve

        if CharacterService.is_girlfriend(lauren):
            menu:
                "Flirt":
                    $ reputation.add_point(RepComponent.BOYFRIEND)

                    u "One might say, your hero?"

                    scene v9lau16b # FPP. Same camera as v9lau16, Lauren giggle, mouth open.
                    with dissolve

                    la "One might."

                "Be romantic":
                    $ reputation.add_point(RepComponent.BOYFRIEND)

                    u "I just want you to know you can count on me. Always."

                    scene v9lau16
                    with dissolve

                    la "I do."

                    scene v9lau16a
                    with dissolve

                    u "Good. You mean a lot to me, Lauren."

                    scene v9lau16
                    with dissolve

                    la "You mean a lot to me, too, [name]."

        else:
            u "That's what I'm here for."

            scene v9lau16
            with dissolve

            la "Thank you [name]."        

        scene v9lau16a
        with dissolve

        u "Talk to you soon?"

        scene v9lau16
        with dissolve

        la "Definitely."

        scene v9lau16a
        with dissolve

        if not CharacterService.is_girlfriend(lauren) and reputation() == Reputations.LOYAL:
            if reputation() == Reputations.LOYAL:
                call screen reputation_popup

            menu:
                "Kiss Lauren":
                    $ reputation.add_point(RepComponent.BOYFRIEND)

                    jump v9_lau_dorm_kiss

                "Leave":
                    jump v9_lau_dorm_no_kiss
                
        elif CharacterService.is_girlfriend(lauren):
            jump v9_lau_dorm_kiss

        else:
            jump v9_lau_dorm_no_kiss

    else:
        la "Really, thank you. You gave me the push I needed."

        scene v9lau16a
        with dissolve

        menu:
            "Credit Lauren":
                $ reputation.add_point(RepComponent.BOYFRIEND)

                u "It's gonna be a great event. Those Deer will be begging you to host every event from now on."

                scene v9lau16
                with dissolve

                la "You think so? It is fun. And I love giving back to the community."

                scene v9lau16a
                with dissolve

                u "I know so."

            "Take some credit":
                u "We make a great team."

                scene v9lau16
                with dissolve

                la "We do, don't we?"

                scene v9lau16a
                with dissolve

                u "Maybe one day we'll start a party planning business together!"

                scene v9lau16b
                with dissolve

                la "Great to have a backup plan."           

        jump v9_lau_dorm_no_kiss

label v9_lau_dorm_kiss:
    scene v9lau17 # TPP. Show Lauren and MC kissing.
    with dissolve

    play sound "sounds/kiss.mp3"

    pause 1

    jump v9_lau_dorm_no_kiss

label v9_lau_dorm_no_kiss:
    scene v9lau18 # TPP. Show Lauren opening to door to her room.
    with dissolve

    pause 0.75

    scene v9lau19 # FPP. Show Lauren (as if MC is now stood outside Lauren's door and Lauren is stood at the door in her room), smile, mouth open.
    with dissolve

    la "See you soon."

    scene v9lau19a # FPP. Same camera as v9lau19, Lauren smile, mouth closed.
    with dissolve

    u "Take care."

    scene v9lau20 # TPP. Show MC walking away down the hallway, camera from behind.
    with dissolve
    
    pause 1

    stop music fadeout 3

    scene black
    with dissolve

    pause 0.5

    jump v9_room_fri_aft