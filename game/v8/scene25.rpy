# SCENE 24: MON AFTERNOON IN MC'S ROOM
# Locations: MC's room in Wolves house or MC's room in Apes house
# Characters: MC (outfit 3)
# Time: Monday afternoon

# Wolves version
label v8_scene24_wolves:
    scene v8monroom1 # TPP. MC in his room at Wolves house studying on his desk, neutral expression, mouth closed
    with Fade(1.25, 0.25, 0.5)
    pause
    u "(I gotta get out of here. Wonder what everyone's up to.)"

    # Kiwii Pic Description (mcpost1w.webp, 1920x1080): Selfie of MC sitting at his desk in Wolves house, looking bored and showing his books/laptop in the frame. Should be continuation of v8monroom1
    $ v8s25_kiwiiPost = KiwiiPost(mc, "phone/kiwii/Posts/v8/mcpost1w.webp", _("Ugh someone save me pls"), number_likes=2)

    scene v8monroom1a # MC looking at his phone now, neutral expression, mouth closed. Rest is same as v8monroom1
    with fade

    u "*Sigh*"
    jump phn_riley11_setup

    # Apes version
label v8_scene24_apes:
    scene v8monroom2 # TPP. MC in his room at Apes house studying on his desk, neutral expression, mouth closed
    with Fade(1.25, 0.25, 0.5)
    pause
    u "(I gotta get out of here. Wonder what everyone's up to.)"

    # Kiwii Pic Description (mcpost1a.webp, 1920x1080): Selfie of MC sitting at his desk in Apes house, looking bored and showing his books/laptop in the frame. Should be continuation of v8monroom2
    $ v8s25_kiwiiPost = KiwiiPost(mc, "phone/kiwii/Posts/v8/mcpost1a.webp", _("Ugh someone save me pls"), number_likes=2)

    scene v8monroom2a # MC looking at his phone now, neutral expression, mouth closed. Rest is same as v8monroom2
    with fade

    u "*Sigh*"
    jump phn_riley11_setup

label phn_riley11_setup:
    $ MessengerService.new_message(riley, _("Bad day?"))
    $ MessengerService.add_reply(riley, _("I've read the same page four times :/"))
    $ MessengerService.new_message(riley, _("At least you can read! I just found out I need glasses!"))
    $ MessengerService.add_reply(riley, _("I think you'd look cute in glasses."))
    $ MessengerService.new_message(riley, _("I don't know. Why don't you come with me and Aubrey to try some on?"))
    $ MessengerService.add_reply(riley, _("Sure, I will come. But where is the store?"))
    $ MessengerService.new_message(riley, _("Just down the road from the gym on the right hand side of the road"))
    $ MessengerService.add_reply(riley, _("Cool will meet you both there"))
    $ MessengerService.new_message(riley, _("Great!"))
    play sound sound.vibrate

    while MessengerService.has_replies(riley):
        call screen phone
        if MessengerService.has_replies(riley):
            u "(I should talk to Riley.)"

    if joinwolves:
        u "(Guess I'm not gonna be bored to death after all.)"

    else:
        scene v8monroom4 # TPP. Show MC leaving his room in Apes house, smiling a little, mouth closed
        with dissolve
        u "(Guess I'm not gonna be bored to death after all.)"

    jump s26
