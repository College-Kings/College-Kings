# SCENE 24: MC gets a text from Amber
# Locations: Side walk, Gas Station (TPP View only)
# Characters: MC (Outfit: 9)
# Time: Evening (Tuesday)

label v14s24:
    play music "music/v12/Track Scene 30.mp3" fadein 2

    $ amber.messenger.newMessage("Hey.", force_send=True)
    $ amber.messenger.newMessage("Are you busy?", force_send=True)
    $ amber.messenger.addReply("Nope, what's up?")
    $ amber.messenger.newMessage("I could really use a friend right now.")
    $ amber.messenger.addReply("I'm on my way, ok?")
    $ amber.messenger.newMessage("Okay");

    play sound "sounds/vibrate.mp3"

    scene v14s24_2 # FPP. MC looking down at his phone while on the sidewalk.
    with dissolve

    pause 1

    label v14s24_PhoneContinueAmber:
        if amber.messenger.replies:
            call screen phone
        if amber.messenger.replies:
            u "(I should check my phone.)"
            jump v14s24_PhoneContinueAmber
    
    scene v14s24_3 # TPP. MC, putting his phone in his pocket, thinking, mouth closed.
    with dissolve
    
    u "*Sighs* (She's been acting off for a few days and now she \"could use a friend\"... Who knows what's going on now.)"

    if v14s03a_take_wallet:
        scene v14s24_4 # TPP. MC, happy, smiling mouth closed.
        with dissolve

        u "(Oh, shit... You know what? I still have some extra money from that scummy night gambler.)"

        scene v14s24_5 # FPP. MC looks ahead (or across the street) and see's a gas station not too far from him.
        with dissolve

        u "(I'm gonna go ahead and get her something from the gas station.)"

        scene v14s24_6 # TPP. MC walking a head of the camera towards the gas station.
        with dissolve

        pause 0.75

        stop music fadeout 3
        jump v14s24a 

    else:
        scene v14s24_8 # TPP. MC walking down the side walk towards Amber's house. 
        with dissolve
        
        pause 0.75
        
        stop music fadeout 3
        jump v14s25