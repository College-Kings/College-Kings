# SCENE 1: CHRIS' ROOM POSTS
# Locations: MC's room in Wolves house, Chris' room in Wolves house
# Characters: MC (outfit 2), Chris (Outfit 1)
# Time: Tuesday night

label v9start:
    if joinwolves:
        jump v9_start_wolves
    else:
        jump v9_start_apes

label v9_start_wolves:
    play music "music/v9/Track Scene 1.mp3" fadein 2

    u "(I need to find out what's going on. This is insane!)"

    scene v9wpost1 # TPP. MC outside Chris' room, knocking the door, confused, mouth closed
    with fade

    play sound "sounds/knock.mp3"
    pause 0.5
    ch "Come in."

    play sound "sounds/dooropen.mp3"

    scene v9wpost2 # FPP. (MC entered the room now and is standing near Chris' desk). Show Chris sitting at his desk just chilling, looking at his phone, smiling, mouth closed (preferably phone screen not visible)
    with dissolve
    u "Dude, what's happening?"

    scene v9wpost2a # Chris turns his head to look into the camera (phone still in hand), excited and mouth open (preferably phone screen not visible)
    with dissolve
    ch "It's badass, right?"

    scene v9wpost2b # Same as v9wpost2a but Chris mouth closed
    with dissolve
    u "I don't know. What the hell is it? Kiwii's going crazy!"

    scene v9wpost2a
    with dissolve
    ch "I know! Everyone's talking about it."

    scene v9wpost2b
    with dissolve
    u "Talking about what? Do you know what's going on?"

    scene v9wpost2c # Chris placed his phone on the desk now and turned his whole body to face the MC, smiling and mouth open
    with dissolve
    ch "Of course! Didn't someone tell you when?"

    scene v9wpost2d # Same as v9wpost2c but Chris mouth closed
    with dissolve
    u "Naw, man. My phone just started blowing up."

    scene v9wpost2c
    with dissolve
    ch "Sorry, man. Guess I got busy. I should check on Imre and Perry, too. See if they heard."

    scene v9wpost2d
    with dissolve
    u "Heard what?"

    scene v9wpost3 # FPP (Continuation of v9wpost2d, different frame number to allow camera freedom). Chris gets up and stands up in front of the MC, smiling, mouth open
    with dissolve
    ch "A new tournament!"

    scene v9wpost3a # Same as v9wpost3 but Chris mouth closed
    with dissolve

    menu:
        "Excited reply":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            u "No shit! That's amazing!"

            scene v9wpost4 # TPP (Continuation of v9wpost3. Camera behind MC so his facial expression is not visible). Show Chris squeezing MC's bicep, smiling, mouth open
            with dissolve
            ch "You've been working out, right?"

            scene v9wpost3a
            with dissolve
            u "Yeah, Imre and Sebastian have both been training me."

            scene v9wpost3
            with dissolve
            ch "Great! We're gonna need it if we plan on beating the Apes."

        "Hesitant reply":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            $ v9_brawl_hesitant = True

            u "(I haven't been training enough for this.)"
            u "Um..."

            scene v9wpost4
            with dissolve
            ch "You've been working out, right?"

            scene v9wpost3a
            with dissolve
            u "A little... but I-I don't know."

            scene v9wpost3
            with dissolve
            ch "Come on, man. We're gonna need you to kick some Ape ass!"

    scene v9wpost3a
    with dissolve
    u "Apes? Grayson's the Fight King. I can't-"

    scene v9wpost3
    with dissolve
    ch "Grayson's not fighting. That's the best part!"

    scene v9wpost3a
    with dissolve
    u "Why wouldn't their best fighter participate in a tournament?"

    scene v9wpost3
    with dissolve
    ch "Because it's the Freshman Brawl!"

    scene v9wpost3b # Chris puts his hand on MC's shoulder, smiling, mouth open (this is still FPP and not TPP)
    with dissolve
    ch "Aww it's gonna be awesome! What better way to see what you pledges have in you?"

    scene v9wpost3a
    with dissolve
    u "How long do I have to get ready for this?"

    scene v9wpost3
    with dissolve
    ch "Plenty of time. It's not 'til Saturday."

    scene v9wpost3a
    with dissolve
    u "Saturday?!"

    scene v9wpost3b
    with dissolve
    ch "You're gonna do great! We'll double down on gym time to make sure, but I believe in you, man."

    scene v9wpost3c # Same as v9wpost3b but Chris mouth closed
    with dissolve

    menu:
        "Try to back out":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            $ v9_brawl_hesitant = True

            u "I don't know... I'm not ready for something like this. A... BRAWL?"

            scene v9wpost3d # Chris slightly annoyed, mouth open (no hands on shoulder)
            with dissolve
            ch "Come on. You knew what these frats were about when you pledged. We fight. It'll be fine."

            scene v9wpost3e # Same as v9wpost3d but Chris mouth closed
            with dissolve
            u "*Sigh* (What have I gotten myself into.)"
            u "You're right. Sebastian and Imre have shown me a lot. I'll be ready."

            scene v9wpost3b
            with dissolve
            ch "Damn right you will! That's the spirit. Now, I gotta finish spreading the word. Make sure you share the square!"

            stop music fadeout 3

        "Go with it":
            # $ reputation.add_point(RepComponent.TROUBLEMAKER)

            u "Wow, trial by fire!"

            scene v9wpost3
            with dissolve
            ch "Right? I'm so pumped! You're already much farther along than those punk ape pledges. We got this!"

            scene v9wpost3a
            with dissolve
            u "I have been pushing myself. I added some extra reps-"

            scene v9wpost3b
            with dissolve
            ch "Great! Keep that going. I gotta get back to spreading the word. You go hit the gym and make sure you share the square!"

            stop music fadeout 3

    scene v9wpost5 # TPP. Show MC leaving Chris' room, neutral expression, mouth closed. Chris is still standing as before and is looking at the MC, smiling, mouth closed
    with dissolve
    pause 0.75

    play music "music/v9/Track Scene 3.mp3" fadein 2

    scene v9wpost6 # TPP. MC IN UNDERWEAR FROM NOW ON AND IT SHOULD BE DARK INSIDE THE ROOM. Show MC flexing one of his arms, looking at himself in mirror inside his room, neutral expression, mouth closed
    with Fade(0.75, 0.25, 0.75)
    pause 0.5
    u "(Better amp up my workouts. Imre too.)"

    scene v9wpost7 # TPP (maybe from top). Show MC lying on his bed in his room, looking at his phone, neutral expression, mouth closed
    with dissolve
    pause 0.5

    python:
        v9s1_reply1 = MessageBuilder(imre)
        v9s1_reply1.new_message(_("Damn right! You heading to the gym?"))
        v9s1_reply1.add_reply(_("Naw, I'm spent. But I have a feeling I'll be spending a lot of my time in there"))
        v9s1_reply1.new_message(_("Me too. See ya there!"))

        v9s1_reply2 = MessageBuilder(imre)
        v9s1_reply2.new_message(_("Lucky we did, huh? I think we got a hand up on those baby apes"))
        v9s1_reply2.add_reply(_("Damn right! We got this! We need to hit the gym soon... after I get some sleep. I'm bout to pass out"))
        v9s1_reply2.new_message(_("Same! Talk soon"))

        MessengerService.add_reply(imre, _("You here yet?"))
        MessengerService.new_message(imre, _("Yeah, you ready?"))
        MessengerService.add_replies(imre, 
            Reply(_("Hell no! But we need to get ready!"), v9s1_reply1),
            Reply(_("I think so, actually. You and Sebastian really helped"), v9s1_reply2)
        )
        
    while MessengerService.has_replies(imre):
        call screen phone
        if MessengerService.has_replies(imre):
            u "(I should talk to Imre.)"
        
    scene v9wpost7a # MC places his phone down on his bed, and is just lying on it now, thinking, mouth closed
    with dissolve
    u "(Freshman Brawl... sounds intense.)"

    if not v9_brawl_hesitant:
        u "(I think I got this.)"

    else:
        u "(I'm gonna get my ass kicked. I need to train hard the next few days.)"

    u "(Why is it so soon though? This Saturday?!)"
    u "*Sigh* (I gotta sleep.)"

    stop music fadeout 3

    scene v9wpost7b # Same as v9wpost7a but MC's eyes closed
    with dissolve
    pause 0.5

    scene black
    with Dissolve(1)
    pause 0.5

    jump v9_dream