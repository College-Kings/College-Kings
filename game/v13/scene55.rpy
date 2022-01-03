# SCENE 55: Nora in Lobby
# Locations: Hotel Lobby
# Characters: MC (Outfit: 3), NORA (Outfit: 1)
# Time: Morning

label v13s55:
# -MC sees Nora sitting in the lobby and goes over to sit by her-

    scene v13s55_1 # TPP. Show MC walking in the lobby and seeing Nora 
    with dissolve

    pause 0.75

    play music "music/v13/Track Scene 55.mp3" fadein 2

    scene v13s55_2 # TPP. MC sitting next to Nora, Nora looking at MC, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v13s55_3 # FPP. MC sitting in the chair besides Nora, Nora looking at MC, MC looking at Nora, Nora slight smile, mouth closed.
    with dissolve

    u "Hey, hey... Is it safe to sit by you or are you being watched?"

    scene v13s55_3a # FPP. Same as v13s55_3, Nora slight smile, mouth open.
    with dissolve

    no "*Chuckles* You're fine."

    scene v13s55_3
    with dissolve

    u "What are you doing out here?"

    scene v13s55_3a
    with dissolve

    no "I'm just thinking about what to get Ms. Rose and Mr. Lee."

    scene v13s55_3
    with dissolve

    u "Get them for what?"

    scene v13s55_3a
    with dissolve

    no "To thank them for chaperoning the trip, duh?"

    scene v13s55_3
    with dissolve

    u "Oh, I was thinking it was Teacher Appreciation Week or something. *Chuckles*"

    scene v13s55_3a
    with dissolve

    no "*Chuckles* In a way it is."

    scene v13s55_3
    with dissolve

    u "Haha, what are you planning on getting them?"

    scene v13s55_3b # FPP. Same as v13s55_3a, Nora different pose, slight smile, mouth open.
    with dissolve

    no "That's the thing, I don't have any money left so I'm trying to figure that out."

    scene v13s55_3c # FPP. Same as v13s55_3b, Nora slight smile, mouth closed.
    with dissolve

    u "Ask everyone to chip in."

    scene v13s55_3b
    with dissolve

    no "I asked a few people that I thought would want to help but they said no."

    scene v13s55_3c
    with dissolve

    u "You didn't ask me."

    scene v13s55_3a
    with dissolve

    no "I didn't think you would..."

    scene v13s55_3
    with dissolve

    u "Guess you won't know 'til you ask. *Chuckles*"

    scene v13s55_3a
    with dissolve

    no "*Shy* ..."

    scene v13s55_3
    with dissolve

    u "Waiting... *Chuckles*"

    scene v13s55_3b
    with dissolve

    no "Will you chip in to help with the gifts?"

    scene v13s55_3c
    with dissolve

    u "What's the magic word?"

    scene v13s55_3b
    with dissolve

    no "Really..."

    scene v13s55_3c
    with dissolve

    u "*Clears throat*"

    scene v13s55_3b
    with dissolve

    no "*Sighs* Please?"

    scene v13s55_3c
    with dissolve

    u "Of course I'll chip in. *Laughs* I don't have much so I don't know what we can get, but we can get something."

    scene v13s55_3a
    with dissolve

    no "*Chuckles* Good. Thank you."

    scene v13s55_3
    with dissolve

    u "Are you trying to go and get something now or...?"

    scene v13s55_3a
    with dissolve

    no "Is that okay?"

    scene v13s55_3
    with dissolve

    u "Yeah, I'm still trying to wake up but I'm up enough."

    scene v13s55_3a
    with dissolve

    no "Okay, let's go then."
    
    scene v13s55_4 # FPP. Nora standing up infront of her seat looking at MC, MC sitting down looking at Nora, Nora slight smile, mouth closed.
    with dissolve
    
    if v13s48_ryan_double_date:

        u "*Phone buzzes*"
    
        play sound "sounds/vibrate.mp3"

        u "One sec, let me check this."

        $ ryan.messenger.newMessage(_("Hey man, had a chat with Emily. The date went great!"), force_send=True)
        $ ryan.messenger.addReply(_("Yeah man, it was nice. Thanks again for setting it up."), func=None)
        $ ryan.messenger.addReply(_("For sure dude, I had a really fun night."), func=None) 
        $ ryan.messenger.newMessage(_("We'll have to do it again soon."))
        $ ryan.messenger.addReply(_("Sure man."), func=None)

        scene v13s55_5 # TPP. Show MC holding his phone sitting down, slight smile, mouth closed.
        with dissolve

        label v13s49_PhoneContinueRyan:
            if ryan.messenger.replies:
                call screen phone
            if ryan.messenger.replies:
                u "(I should check my phone.)"
                jump v13s49_PhoneContinueRyan 
       
        u "(Poor guy...)"

    scene v13s55_4
    with dissolve

    pause 0.75

    scene v13s55_6 # FPP. MC standing up looking at Nora, Nora looking at MC, Nora slight smile, mouth closed.
    with dissolve

    u "After you. *Chuckles*"

    scene v13s55_7 # TPP. Show MC and Nora walking towards the hotel entrance, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v13s55_7a # TPP. Same as v13s55_6, Hotel entrance open MC and Nora walking out, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v13s56