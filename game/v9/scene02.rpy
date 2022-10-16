# SCENE 2: CAMERON'S ROOM POSTS
# Locations: MC's room in Apes house, Cameron's room in Apes house
# Characters: MC (outfit 2), Cameron (Outfit 1 boxers only, no shirt, no shoes)
# Time: Tuesday night

init python:
    def v9s2_reply1():
        ryan.messenger.newMessage(_("Damn right! You heading to the gym?"))
        ryan.messenger.addReply(_("Naw, I'm spent. But I have a feeling I'll be spending a lot of my time in there"))
        ryan.messenger.newMessage(_("Me too. See ya there!"))

    def v9s2_reply2():
        ryan.messenger.newMessage(_("Lucky we did, huh? I think we got a hand up on those baby apes"))
        ryan.messenger.addReply(_("Damn right! We got this! We need to hit the gym soon... after I get some sleep. I'm bout to pass out"))
        ryan.messenger.newMessage(_("Same! Talk soon"))

label v9_start_apes:

    play music "music/v9/Track Scene 1.mp3" fadein 2

    u "(I need to find out what's going on. This is insane!)"

    scene v9apost1 # TPP. MC outside Cameron's room, knocking the door, confused, mouth closed
    with fade

    play sound "sounds/knock.mp3"
    pause 2

    scene v9apost2 # FPP. Cameron opens the door slightly and peeks through the opening, slightly annoyed, mouth open
    with dissolve
    play sound "sounds/dooropen.mp3"
    ca "What you want, pledge?"

    scene v9apost3 # FPP (Can use the same camera as v9apost2 but different frame number to allow camera freedom). Cameron comes out and is standing in front of the MC now, looking slightly annoyed, mouth closed. Door still only half open.
    with dissolve

    menu:
        "Not a pledge anymore":
            $ reputation.add_point(Reputations.TROUBLEMAKER)

            u "Not a pledge anymore."

            scene v9apost3a # Same as v9apost3 but Cameron mouth open
            with dissolve
            ca "To me, you're a pledge 'til you prove yourself...{w} PLEDGE."

            scene v9apost3
            with dissolve
            u "I think I proved myself in the challenges but whatever."

            scene v9apost3a
            with dissolve
            ca "Shit no."

            scene v9apost3b # Cameron arrogant smile, mouth open
            with dissolve
            ca "But you're about to get that chance."

            scene v9apost3c # Same as v9apost3b but Cameron mouth closed
            with dissolve
            u "How?"

            scene v9apost3b
            with dissolve
            ca "Haven't you heard? It's all over."

            scene v9apost3c
            with dissolve
            u "Something's going on. I just don't know what."

        "Let it slide":
            $ reputation.add_point(Reputations.BRO)

            u "(Cam's just a dick. Not worth it.)"
            u "Do you know what's going on?"

            scene v9apost3b
            with dissolve
            ca "Of course I do. I'm an Ape!"

            scene v9apost3c
            with dissolve
            u "Can you tell me?"

            scene v9apost3b
            with dissolve
            ca "I don't think you're ready."

            scene v9apost3c
            with dissolve
            u "Ready for what?"

    scene v9apost4 # TPP. Show MC trying to enter the room/opening the door, but Cameron stopping him. Cameron neutral expression, mouth open
    with dissolve
    ca "Uh uh. You stay here, pledge." with hpunch

    scene v9apost5 # FPP. Same as v9apost3 but camera tilted down to show Cameron's shorts. If possible show a bulge implying an erect penis.
    with dissolve
    pause 0.5

    scene v9apost3
    with dissolve
    u "Is this a bad time?"

    scene v9apost3b
    with dissolve
    ca "Always... You know how it is."

    scene v9apost3c
    with dissolve
    unkfem "Come back in Cammiiieee!"
    u "Cammie *snickers*"

    scene v9apost3a
    with dissolve
    ca "Hey! If you ever get a girl in that room of yours, pledge... let her call you whatever she wants."

    scene v9apost3
    with dissolve

    menu:
        "Defend your honor":
            $ reputation.add_point(Reputations.TROUBLEMAKER)

            u "I do fine. And they ALL call me Big Daddy."

            scene v9apost3d # Cameron laughing sarcastically, mouth open
            with dissolve
            ca "What the fuck ever, dude. What do you want?"

            scene v9apost3c
            with dissolve
            u "I just want to know what's going on with this red square. Then I'll let you get back to disappointing that lovely lady inside."

            scene v9apost3d
            with dissolve
            ca "Oh shut the fuck up."

            scene v9apost3b
            with dissolve
            ca "That's for the Freshman Brawl! It's gonna be epic!"

        "Just ask him about the red square":
            $ reputation.add_point(Reputations.BRO)

            u "What's up with the red square? That's all I wanna know."

            scene v9apost3b
            with dissolve
            ca "The Freshman Brawl! It's gonna be epic!"


    scene v9apost3e # Cameron punching the MC's chest (not with an intention to hurt though), smirking, mouth open (this is still FPP and not TPP)
    with vpunch
    ca "Better beef up or you won't stand a chance."

    scene v9apost3c
    with dissolve
    u "A fight?"

    scene v9apost3b
    with dissolve
    ca "Not just a fight. A brawl! No holds barred. Every pledge for himself. Bloodbath!"

    scene v9apost3c
    with dissolve

    menu:
        "Excited reply":
            $ reputation.add_point(Reputations.TROUBLEMAKER)

            u "Pledge vs pledge!?"

            scene v9apost3b
            with dissolve
            ca "Yeah, and I expect you to wipe the floor with those pussy Wolves."

            scene v9apost3c
            with dissolve
            u "With pleasure."

            scene v9apost3b
            with dissolve
            ca "We're counting on you. Now go away!"

            scene v9apost3c
            with dissolve
            u "Wait... when is it? How long do I have to train?"

            scene v9apost3b
            with dissolve
            ca "Saturday."

            play sound "sounds/doorclose.mp3"

            scene v9apost3f # Cameron slammed the door and went inside, so just show a closed door
            with hpunch

            stop music fadeout 3

            pause

        "Hesitant reply":
            $ v9_brawl_hesitant = True
            $ reputation.add_point(Reputations.BOYFRIEND)

            u "(Bloodbath? I don't like the sound of that.)"
            u "Freshman Brawl? Sounds dangerous."

            scene v9apost3g # Cameron delighted/excited, punching the air, mouth open
            with dissolve
            ca "I know, right?"

            scene v9apost3a
            with dissolve
            ca "Now go away so she can finish what she started."

            scene v9apost3
            with dissolve
            u "Wait. When is this fight? How long do I have to train?"

            scene v9apost3b
            with dissolve
            ca "Saturday. Get to work!"

            play sound "sounds/doorclose.mp3"

            scene v9apost3f
            with hpunch
            pause
            u "(Saturday? Oh, shit!)"

            stop music fadeout 3

    scene v9apost6 # TPP. MC IN UNDERWEAR FROM NOW ON AND IT SHOULD BE DARK INSIDE THE ROOM. Show MC flexing one of his arms, looking at himself in mirror inside his room, neutral expression, mouth closed
    with Fade(0.75, 0.25, 0.75)
    pause 0.5

    play music "music/v9/Track Scene 3.mp3" fadein 2

    u "(Better amp up my workouts. Ryan too.)"

    scene v9apost7 # TPP (maybe from top). Show MC lying on his bed in his room, looking at his phone, neutral expression, mouth closed
    with dissolve
    pause 0.5

    $ ryan.messenger.addReply(_("You here yet?"))
    $ ryan.messenger.newMessage(_("Yeah, you ready?"))
    $ ryan.messenger.addReply(_("Hell no! But we need to get ready!"), v9s2_reply1)
    $ ryan.messenger.addReply(_("I think so, actually. You and Cameron really helped"), v9s2_reply2)

    label v9_phn_ryan1:
        if ryan.messenger.replies:
            call screen phone
        if ryan.messenger.replies:
            u "(I should talk to Ryan.)"
            jump v9_phn_ryan1

    scene v9apost7a # MC places his phone down on his bed, and is just lying on it now, thinking, mouth closed
    with dissolve
    u "(Freshman Brawl... sounds intense.)"

    if not v9_brawl_hesitant:
        u "(I think I got this.)"

    else:
        u "(I'm gonna get my ass kicked. I need to train hard the next few days.)"

    u "(Why is it so soon though? This Saturday?!)"
    u "*Sigh* (I gotta sleep.)"

    stop music fadeout 3

    scene v9apost7b # Same as v9wpost7a but MC's eyes closed
    with dissolve
    pause 0.5

    scene black
    with Dissolve(1)
    pause 0.5

    jump v9_dream


