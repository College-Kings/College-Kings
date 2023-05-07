# SCENE 24: MEETING JOSH
# Locations: Josh's room (most of the scene), city streets for showing MC walking around
# Characters: MC (outfit 3), Josh (outfit 1)
# Time: Monday morning to noon

label josh_room:
    scene v8josh1 # TPP. Showing MC walking in the streets, thinking, mouth closed
    with fade
    u "(What does Josh want now? He sounded a bit nervous on the phone.)"

    play music "music/m16punk.mp3" fadein 2

    scene v8josh2 # TPP (far shot). Showing Josh waiting outside his room, standing against a wall just looking at the ground, nervous, mouth closed. MC walking towards Josh, neutral expression, mouth closed
    with dissolve
    pause 0.5

    scene v8josh3 # TPP. Show MC and Josh doing a quick bro hug (the half hug handshake thingy). Josh happy, mouth open. Camera is on MC's side so Josh is the focus
    with dissolve
    jo "My man! Thanks for coming!"

    scene v8josh4 # FPP (continuation of v8josh3). Josh happy, mouth closed
    with dissolve
    u "Yeah, no problem, man. What's up?"

    scene v8josh4a # Same as v8josh4 but Josh mouth open
    with dissolve
    jo "Okay, so, it's like this. I got a little deal going on tonight that's gonna get me a thousand bucks."

    scene v8josh4b # Josh looking somewhat shady, mouth open
    with dissolve
    jo "Coke deal, you know *sniffs*, and I need someone I can trust to watch my ass, you know, in case they try to rob me."
    jo "Normally, my cousin does it but he broke his arm so he can't do shit. Can I count on you?"

    scene v8josh4c # Same as v8josh4b but Josh mouth closed
    with dissolve
    u "Man, Josh, I dunno. This is awfully risky and you know I'm not into that shit."

    scene v8josh4b
    with dissolve
    jo "I'm not asking you to do a few lines, man. Just watch my ass and make sure no one does anything freaky."

    scene v8josh4c
    with dissolve
    u "Fuck, ummm..."

    menu:
        "Agree to help":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            $ reputation.add_point(RepComponent.BRO)
            $ helpJosh = True

            u "Yeah, okay, I'll go. I can't let you do this alone."

            scene v8josh3
            with dissolve
            jo "My man! Thanks, bro! I really appreciate this!"

            scene v8josh4
            with dissolve
            u "Haha, I just hope we don't regret it."

            scene v8josh4a
            with dissolve
            jo "Nah, we won't! This'll go off smooth, bro, trust me."

            scene v8josh4
            with dissolve
            u "Sure it will."

            scene v8josh4a
            with dissolve
            jo "Deal goes down at 9 PM tonight. We'll meet here and go to the spot together, okay?"

            scene v8josh4
            with dissolve
            u "Yeah cool. I'll see you then."

            scene v8josh4a
            with dissolve
            jo "Yeah, see you then, bro!"

        "Say no":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            u "Honestly, man, I don't think so. This isn't me and I don't want to get caught, especially with that shit."

            scene v8josh4d # Josh disappointed, angry and mouth open
            with dissolve
            jo "Really? I thought you were my bro, man. I guess I was wrong about you."

            scene v8josh4e # Same a v8josh4d but Josh mouth closed
            with dissolve
            u "Man, don't be like that. You know that shit is gonna get you in trouble sooner or later. Why risk it?"

            scene v8josh4d
            with dissolve
            jo "Whatever, man. You can't do one favor for me. Some friend!"

            scene v8josh5 # FPP (Continuation of v8josh4d, but different frame number to allow for camera freedom). Josh turns around and starts walking away towards the door (angry, mouth closed if face is visible). Room door closed in this shot. MC's hand on his shoulder
            with dissolve
            u "Josh, c'mon man..."

            play sound sound.door_open

            scene v8josh5a # Josh opened the door and storming into his room. MC's hand still in air (as if Josh jerked his shoulder to get rid of MC's hand)
            with dissolve
            pause 0.5

            play sound sound.door_close

            scene v8josh5b # Josh went inside, door closed. MC's hand no longer in air
            with hpunch
            pause 0.5
            u "(Fuck. I should go after him, but I don't want to get caught up in that shit. Guess I'll go back to my room.)"

    stop music fadeout 3

    scene v8josh6 # TPP. Show MC walking away from Josh's room, neutral expression, mouth closed
    with dissolve
    pause 0.5

    if joinwolves:
        jump v8_scene24_wolves
    else:
        jump v8_scene24_apes
