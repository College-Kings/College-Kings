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

    # Kiwii Pic Description (mcpost1w.png, 1920x1080): Selfie of MC sitting at his desk in Wolves house, looking bored and showing his books/laptop in the frame. Should be continuation of v8monroom1
    # $ mcKiwiiPost = KiwiiPost("MC", "images/mcpost1w.png", "Ugh someone save me pls", numberLikes=2)
    $ showphone = True
    $ phoneexit = "phn_riley11_setup"

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

    # Kiwii Pic Description (mcpost1a.png, 1920x1080): Selfie of MC sitting at his desk in Apes house, looking bored and showing his books/laptop in the frame. Should be continuation of v8monroom2
    # $ mcKiwiiPost = KiwiiPost("MC", "images/mcpost1a.png", "Ugh someone save me pls", numberLikes=2)
    $ showphone = True
    $ phoneexit = "phn_riley11_setup"

    scene v8monroom2a # MC looking at his phone now, neutral expression, mouth closed. Rest is same as v8monroom2
    with fade

    u "*Sigh*"
    jump phn_riley11_setup

label phn_riley11_setup:
    $ phoneexit = "phn_riley11"
    $ contact_Riley.newMessage("Bad day?")
    $ contact_Riley.addReply("I've read the same page four times :/", "phn_riley11_a")
    play sound "sounds/vibrate.mp3"
    call screen messager(contact_Riley)

label phn_riley11:
    if contact_Riley.messages[-1].replies:
        u "(I should talk to Riley.)"
        jump phn_riley11

    else:
        $ showphone = False
        jump phn_riley11_done

label phn_riley11_a:
    $ contact_Riley.newMessage("At least you can read! I just found out I need glasses!")
    $ contact_Riley.addReply("I think you'd look cute in glasses.", "phn_riley11_a1")
    call screen messager(contact_Riley)

label phn_riley11_a1:
    $ contact_Riley.newMessage("I don't know. Why don't you come with me and Aubrey to try some on?")
    $ contact_Riley.addReply("Sure! Meet you there?", "phn_riley11_a2")
    call screen messager(contact_Riley)

label phn_riley11_a2:
    $ contact_Riley.newMessage("Great!")
    call screen messager(contact_Riley)

label phn_riley11_done:
    if joinwolves:
        u "(Guess I'm not gonna be bored to death after all.)"

    else:
        scene v8monroom4 # TPP. Show MC leaving his room in Apes house, smiling a little, mouth closed
        with dissolve
        u "(Guess I'm not gonna be bored to death after all.)"

    jump s26
