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
    $ v8s25_kiwiiPost = KiwiiPost(mc, "v8/mcpost1w.webp", _("Ugh someone save me pls"), numberLikes=2)

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
    $ v8s25_kiwiiPost = KiwiiPost(mc, "v8/mcpost1a.webp", _("Ugh someone save me pls"), numberLikes=2)

    scene v8monroom2a # MC looking at his phone now, neutral expression, mouth closed. Rest is same as v8monroom2
    with fade

    u "*Sigh*"
    jump phn_riley11_setup

label phn_riley11_setup:
    $ riley.messenger.newMessage(_("Bad day?"), force_send=True)
    $ riley.messenger.addReply(_("I've read the same page four times :/"))
    $ riley.messenger.newMessage(_("At least you can read! I just found out I need glasses!"))
    $ riley.messenger.addReply(_("I think you'd look cute in glasses."))
    $ riley.messenger.newMessage(_("I don't know. Why don't you come with me and Aubrey to try some on?"))
    $ riley.messenger.addReply(_("sure I will come but where is the store ?"))
    $ riley.messenger.newMessage(_("Just down the road from the gym on the right hand side of the road"))
    $ riley.messenger.addReply(_("Cool will meet you both there"))
    $ riley.messenger.newMessage(_("Great!"))
    play sound "sounds/vibrate.mp3"

label phn_riley11:
    if riley.messenger.replies:
        call screen phone
    if riley.messenger.replies:
        u "(I should talk to Riley.)"
        jump phn_riley11

    if joinwolves:
        u "(Guess I'm not gonna be bored to death after all.)"

    else:
        scene v8monroom4 # TPP. Show MC leaving his room in Apes house, smiling a little, mouth closed
        with dissolve
        u "(Guess I'm not gonna be bored to death after all.)"

    jump s26
