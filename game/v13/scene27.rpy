# SCENE 27: Text from Amber
# Locations: Simplr Bar, Sidewalk
# Characters: MC (Outfit: 9)
# Time: Evening

label v13s27:
    scene v13s27_1 # TPP. Show MC sitting down in the same place as the end of scene 26, MC slightly smiling, looking at the dance floor, mouth closed
    with dissolve

    pause 0.75

    play music "music/v13/Track Scene 27_1.mp3" fadein 2

    play sound "sounds/vibrate.mp3"

    scene v13s27_1a # TPP. Same as v13s27_1, MC slightly surprised, going to grab his phone, mouth closed
    with dissolve

    u "Wow... Perfect timing, who is it this time?"

    $ MessengerService.new_message(amber, "Meet me at the bus stop near the hotel.")
    $ MessengerService.add_reply(amber, "For?")
    $ MessengerService.new_message(amber, "...")

    scene v13s27_1b # TPP. Same as v13s27_1, MC slight smile, looking at his phone, mouth closed
    with dissolve

    label v13s27_PhoneContinueAmber:
        if MessengerService.has_replies(amber):
            call screen phone
        if MessengerService.has_replies(amber):
            u "(I should check my phone.)"
            jump v13s27_PhoneContinueAmber

    scene v13s27_1c # TPP. Same as v13s27_1, MC suspicious, mouth closed
    with dissolve

    u "(She wants me to drag my ass over there without knowing a damn thing about what we're doing?)"

    scene v13s27_1
    with dissolve

    u "*Sighs* (I'd rather just go instead of getting my shit rocked by Amber.)"

    scene v13s27_1d # TPP. Same as v13s27_1, MC looking around, mouth closed, slight smile
    with dissolve

    u "(I don't even know where Ryan and Imre are.)"

    scene v13s27_1
    with dissolve

    u "*Chuckles* (Oh well.)"

    scene v13s27_2 # TPP. Show MC getting up, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v13s27_3 # TPP. Show MC leaving the simplr bar, slight smile, mouth closed
    with fade

    pause 0.75

    stop music fadeout 3
    play music "music/v13/Track Scene 27_2.mp3" fadein 2

    scene v13s27_4 # TPP. Show MC walking in the street, slight smile, mouth closed
    with fade

    pause 0.75

    jump v13s28