# SCENE 2: If Apes, Cameron Interrogation
# Locations: Ape's house
# Characters: MC (Outfit: 1), CAMERON (Outfit: 3)
# Time: Night

label v15s2:
    scene v15s2_1 # FPP. Show the material of the bag over MC's head. (Maybe reuse the same images from the dungeon in v13)
    with dissolve

    u "What the fuck?! Hey!"

    scene v15s2_2 # TPP. Close up of MC with the bag on his head pushed with his back against the wall, the arm of Cameron (who we don't see yet) holding him against the wall.
    with dissolve

    u "Who the fu-"

    scene v15s2_3 # TPP. Show Cameron holding MC against the wall while MC has the bag against his head, Cameron angry, mouth open.
    with dissolve

    ca "Shut up, pledge!"

    scene v15s2_3a # TPP. Same as v15s2_3, Cameron angry, mouth closed.
    with dissolve

    u "Cameron?!"

    u "Pledge?! We're back to this shit now? What the hell are you doing?!"

    play sound "sounds/slap.mp3"

    scene v15s2_3b # TPP. Same as v15s2_3a, Show Camerona smacking MC on the top of the head, Cameron angry, mouth open.
    with vpunch

    ca "I'll be the one asking the questions!"

    scene v15s2_3
    with dissolve

    ca "What the fuck were you doing with my sister?"

    scene v15s2_3a
    with dissolve

    menu:
        "We were just talking":
            u "T-talking! W-we were just talking!"

            scene v15s2_3
            with dissolve

            ca "And drinking! I know she drinks when I'm not around."

        "None of your business":
            u "None of your business, Cameron."

            u "So lay off."

            scene v15s2_3
            with dissolve

            ca "Were you drinking?! I know she drinks when I'm not around."

    if not v14_SamanthaDrugs:
        scene v15s2_3a
        with dissolve

        u "I heard her singing, and came down here to find her drinking, yes..."

        u "But we talked about how she can get help to quit."

        u "I-I'm trying to help her, Cameron. I actually care about her, okay?!"

        scene v15s2_3c # TPP. Same as v15s2_3, Cameron serious face, mouth open.
        with dissolve

        ca "..."

        scene v15s2_3d # TPP. Same as v15s2_3c, Cameron serious face, mouth closed
        with dissolve

        u "Cameron?"

        scene v15s2_3c
        with dissolve

        ca "You better be telling the truth."

        scene v15s2_3d
        with dissolve

        u "I am, man. Look at me."

        scene v15s2_3e # TPP. Same as v15s2_3d, Cameron taking the bag off of MC's head, Cameron serious face, mouth closed.
        with dissolve

        pause 1
        
        scene v15s2_4 # FPP. Cameron standing infront of MC, Cameron serious face, mouth open.
        with dissolve

        ca "So, how are you helping her?"

        scene v15s2_4a # FPP. Same as v15s2_4, Cameron serious face, mouth closed.
        with dissolve

        u "I told her about some people who are trained to help with this kind of stuff, to get her off the drinks and drugs forever."

        scene v15s2_4
        with dissolve

        ca "*Scoffs* You really think that's possible?"

        scene v15s2_4a
        with dissolve

        u "*Sighs* Who knows, Cam. All we can do is try our best."

        u "She needs more positivity in her life. The moment she feels like shit, she goes right back to it."

        scene v15s2_4
        with dissolve

        ca "...Yeah."

        ca "You heard her singing, huh? Ha..."

        scene v15s2_4a
        with dissolve

        u "Yeah. She seems to enjoy it."

        scene v15s2_4
        with dissolve

        ca "She always has. Even if she just sounds like a dying whale..."

        scene v15s2_4a
        with dissolve

        u "So that's something you can encourage her to do more of."
        u "It'll get her to focus on something that makes her happy instead of all the other emotional shit."

        scene v15s2_4
        with dissolve

        ca "I guess you're right..."

        scene v15s2_4a
        with dissolve

        u "(No shit.)"

        scene v15s2_4
        with dissolve

        ca "Sorry about the sack over your head..."

        menu:
            "Laugh it off":
                scene v15s2_4a
                with dissolve

                u "*Chuckles* It was a bit extreme..."

                scene v15s2_4
                with dissolve

                ca "Yeah, but that's my style."

                scene v15s2_5 # TPP. Show MC walking away from Cameron, both serious face, Cameron mouth closed, MC mouth open.
                with dissolve

                u "Night, Cameron. Get some rest, man."

            "Say nothing":
                scene v15s2_5
                with dissolve
                       
                u "Night, Cameron. Get some rest, man."

        scene v15s2_5a # TPP. Same as v15s2_5, Cameron mouth open, MC mouth closed.
        with dissolve

        ca "Yeah, catch you later, [name]."

    else:
        scene v15s2_3
        with dissolve
        
        u "I'm just letting her be who she is!"

        u "Do you really think you can stop her from doing what she wants all the time?"

        scene v15s2_3a
        with dissolve

        ca "Who the fuck do you think you're talking to?! I've known her all my life!"

        ca "That's not who she is, she's-"

        scene v15s2_3
        with dissolve

        u "So, what are you going to do about it? Huh?! You can't be her prison guard forever."

        scene v15s2_3a
        with dissolve

        ca "Keep talking to me like that, [name], and I'll knock your teeth out."

        scene v15s2_3
        with dissolve

        u "I accept her for who she is, Cameron. She's not a fucking kid anymore."

        u "You need to let her live her life the way she wants to."

        scene v15s2_3a
        with dissolve

        ca "Stop... talking..."

        scene v15s2_3
        with dissolve

        u "One day, she may decide to live her life a different way, but that will be her choice. Not yours. Not mine. Hers."

        scene v15s2_3a
        with dissolve

        ca "Stay the fuck out of it, [name]!"

        scene v15s2_3f # TPP. Same as v15s2_3a, Cameron squeezing MC's throat with his hand, Cameron angry, mouth open.
        with dissolve

        ca "If you're not going to help me stop her, then stay the hell away from her. Understand?"

        scene v15s2_3g # TPP. Same as v15s2_3f, Cameron angry face, mouth closed.
        with dissolve

        u "*Choking* I- I-"

        scene v15s2_3
        with dissolve

        u "*Coughing*"

        scene v15s2_3h # TPP. Same as v15s2_3g, Show Cameron storming off away from MC, Cameron angry, mouth closed.
        with dissolve

        pause 0.75

        scene v15s2_3i # TPP. Same as v15s2_3h, Show MC pulling the bag off his head.
        with dissolve

        pause 0.75

        scene v15s2_3j # TPP. Same as v15s2_3i, Show MC looking down at the bag that was on his head now in his hands, MC slightly worried, mouth closed.
        with dissolve

        u "(Fuck!) *Panting*"

        u "(So, this is what living with a psychopath is like? For fuck's sake...)"

        if "v14_samantha" in sceneList:
            u "(I wouldn't have made it out of that conversation alive if he knew what we actually did in there...)"
            u "(Damn, we're so lucky he didn't hear us.)"

        scene v15s2_5b # Same as v15s2_5a, Show MC walking away no Cameron in sight. MC slightly worried, mouth closed.
        with dissolve

        pause 0.75

    play sound "sounds/doorclose.mp3"

    scene v15s2_6 # TPP. Show MC in his room pulling the door closed, MC serious face, mouth closed.
    with dissolve

    pause 0.75

    scene v15s2_7 # TPP. Show MC standing in the middle of his room taking his shirt off, serious face, mouth closed.
    with dissolve

    pause 0.75

    scene v15s2_7a # TPP. Same as v15s2_7, MC taking off his pants now only in his underwear, serious face, mouth closed.
    with dissolve

    pause 0.75

    scene v15s2_8 # TPP. Show MC getting into his bed, serious face, mouth cloesd.
    with dissolve

    pause 0.75

    scene v15s2_9 # TPP. Aerial Camera view looking down at MC who is staring up at his ceiling, serious face, mouth closed.
    with dissolve

    u "*Sighs* (So much drama...)"

    u "(I wonder how many people have had that sack treatment from Cameron.)"

    u "(He's one crazy motherfucking Ape.)"

    play sound "sounds/vibrate.mp3"

    u "(Ah, shit... What now?)"

    scene v15s2_9a # TPP. Show MC holding his phone up infront of his face, serious face, mouth closed.
    with dissolve
    
    pause 0.75

    $ autumn.messenger.newMessage(_("Hey! Just reminding you that I'll be setting up the shelter tomorrow if you wanted to swing by? :)"), force_send=True)
    $ autumn.messenger.addReply(_("Yeah, looking forward to it. See you there!"))
    $ autumn.messenger.addReply(_("Of course! I'll always be there if there's puppies, haha."))

    label v15s2_PhoneContinue:
        if autumn.messenger.replies:
            call screen phone
        if autumn.messenger.replies:
            u "(I should reply to Autumn.)"
            jump v15s2_PhoneContinue

    u "(Almost forgot about that... It'll be interesting to spend some one-on-one time with Autumn.)"

    u "(Should probably set an alarm...)"

    u "(And... done. Now, it's time for be-)"

    scene v15s2_9b # TPP. Same as v15s2_9, MC closing his eyes getting ready for bed, neutral face, mouth closed.
    with dissolve

    pause 0.75

    $ lauren.messenger.newMessage("Hey gang! You're invited to Lauren's birthday party tomorrow night at the Deer's house! It's a Halloween theme of course, so make sure you dress to impress your ghoulish empress, haha! -Lauren", force_send=True)

    play sound "sounds/vibrate.mp3"

    scene v15s2_9
    with vpunch

    u "(The hell?)"

    scene v15s2_9a
    with dissolve

    pause 0.75

    call screen phone

    u "(\"Dress to impress your ghoulish empress...\") *Chuckles*"

    u "(Guess I need to go gift shopping...)"
    u "(Maybe Autumn can give me ideas on what Lauren would like, or I can just get her some kind of gift card... She likes books, I think?)"

    scene v15s2_9c # TPP. Same as v15s2_9b, Show MC yawning and stretching while laying down, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s2_9d # TPP. Same as v15s2_9c, Show MC laying in a different position with his eyes closed.
    with dissolve

    u "(Finally...)"

# -Add the night to morning transition-
# -Night to morning transition-

    scene black
    with dissolve
    
    pause 2

    scene sleep_transition_fast
    with fade
    
    pause 2.2

    scene v15s2_10 # FPP. Just a black screen
    with dissolve
    play sound "sounds/phonealarm.mp3"
    u "*Groans* (No time for a snooze today. Need to get up.)"

    stop sound

    if v14_ApesPostChloePics and not joinwolves:
        jump v15s3

    elif v14_ApesPostChloePics:
        if v14_PenelopePartner:
            $ v14s43b_kiwiiPost1.remove_post()
            $ v14s43b_kiwiiPost2.remove_post()
            $ v14s43b_kiwiiPost3.remove_post()
        else:
            $ v14s43b_kiwiiPost4.remove_post()
            $ v14s43b_kiwiiPost5.remove_post()
            $ v14s43b_kiwiiPost6.remove_post()
        
        jump v15s4

    else: 
        jump v15s4