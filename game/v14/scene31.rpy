# SCENE 31: APES SUPPORT
# Locations: 
# Characters: MC (Outfit: 2), CHLOE (Outfit: 1)
# Time: Wednesday Afternoon

label v14s31:
    scene v14s31_1 # TPP Show MC holding and looking down at his phone
    with dissolve

    play music "music/v13/Track Scene 11_1.mp3" fadein 2

    play sound "sounds/vibrate.mp3"
    pause

    scene v14s31_2 # TPP Show MC with phone up to his ear, MC's mouth open
    with dissolve

    u "Hello?"

    scene v14s31_3 # FPP Show Chloe, holding the phone to her ear, smiling with mouth open
    with dissolve

    cl "Hey! I just wanted to call and let you know that everyone is on their way to the Apes house for the get together."

    scene v14s31_3a # FPP Same as 3, Chloe's mouth closed
    with dissolve

    u "Okay, sounds good. I'll meet you there?"

    scene v14s31_3b # FPP Same angle as 3, Chloe looks worried, with mouth open
    with dissolve

    cl "Yeah... Of course. Also, I know you know already, but please be very cautious of what you say."

    scene v14s31_3c # FPP Same angle as 3, Chloe has her hand on her forehead, looking annoyed, mouth open
    with dissolve

    cl "You know my relationship with the Apes is rocky because of me and Grayson."

    scene v14s31_3d # FPP Same as 3b, Chloe's mouth closed
    with dissolve

    u "I'm sure it'll be fine, Chloe."

    scene v14s31_3b
    with dissolve

    cl "Please take it seriously, [name]."

    cl "The slightest misstep can send him overboard and cause complete hell for the both of us."

    scene v14s31_3d
    with dissolve

    menu:
        "I got this":
            $ add_point(KCT.BOYFRIEND)
            u "Chloe, I got this. I know this is serious for you. I'm going to be on my best behavior."

        "Relax":
            $ add_point(KCT.BRO)
            u "Chloe, relax. I'm doing the best I can for you, and that's exactly what I promised."

    # -Continue regardless of choice
    scene v14s31_3e # FPP Same angle as 3, Chloe looks relieved with a slight smile, mouth open
    with dissolve

    cl "I know, I know. I'm sorry... Thank you. I'll see you soon."

    scene v14s31_3a
    with dissolve

    u "Alrighty."

    scene v14s31_3f # FPP Same angle as 3, Chloe hanging up her phone
    with dissolve

    play sound "sounds/rejectcall.mp3"
    pause 0.75

    scene v14s31_4 # TPP Show MC putting his phone away in his pocket
    with dissolve

    pause 0.75

    if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
        scene v14s31_4a # TPP Same angle as 4, MC crossing his arms over his chest and looking worried
        with dissolve

        u "(Damn, if I didn't know this campaign was important to her, I know now. She's not even thinking about us.)"

        menu:
            "I'm glad she's focused":
                $ add_point(KCT.BOYFRIEND)

                scene v14s31_5 # FPP Show Chloe's campaign poster hung nearby
                with dissolve

                u "(I'm glad she's focused, this is how it should be right now.)"

            "That's a turn-off":
                $ add_point(KCT.TROUBLEMAKER)

                scene v14s31_4b # TPP Same angle as 4, MC looks annoyed and repulsed, like he just tasted something bad
                with dissolve
                
                u "(And it's kind of a turn-off...)"

    # -Regardless of everything scene continued
    scene v14s31_6 # TPP Show MC heading out the door
    with dissolve

    pause 0.75

    stop music fadeout 3

    # -Transition to Scene 31a/31b based on planning board choices-
    if v14_chloe_cameron:
        jump v14s31a

    else:
        jump v14s31b