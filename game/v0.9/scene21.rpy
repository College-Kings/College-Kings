# SCENE 21: Your Room Fri Afternoon
# Locations: MC Wolves room
# Characters: MC (Outfit 3)
# Time: Friday Afternoon

label v9_room_w_chris:
    scene v9rwc1 # TPP. Show MC sat at his desk, continuing on from v9fra2a.
    with dissolve

    pause 1

    scene v9rwc2 # TPP. Show MC's wolves door.
    with dissolve

    play sound "sounds/knock.mp3"

    "*knock* *knock*"

    scene v9rwc3 # TPP. Show MC getting up from his chair to answer the door.
    with dissolve

    pause 1

    scene v9rwc4 # FPP. Close up Chris at the door, neutral expression, mouth open.
    with dissolve

    ch "Hey man, you busy?"

    scene v9rwc4a # FPP. Same camera as v9rwc4, neutral expression, mouth closed.
    with dissolve

    u "Nah, what's up?"

    scene v9rwc4
    with dissolve

    ch "I just spoke to Ms. Rose."

    scene v9rwc4a
    with dissolve

    u "Is everything alright?"

    scene v9rwc4
    with dissolve

    ch "Yeah, she's fine. She took the afternoon to finish setting up her new place and wants those of us who helped her move to come over for dinner."

    scene v9rwc4a
    with dissolve

    u "Of course. I've been wondering how she's doing. What time?"

    scene v9rwc4
    with dissolve

    ch "Now, kinda. I'm rounding up the other guys."

    scene v9rwc4a
    with dissolve

    u "Great. I'll meet you outside and we can go together."

    scene v9rwc4
    with dissolve

    ch "Sure, give me a few."

    scene v9rwc4b # FPP. Same camera as v9rwc4, show Chris walking away.
    with dissolve

    u "(Thinking about what Ms. Rose is going through has me missing Julia. I should check on things back home.)"

    scene v9rwc5 # TPP. Show MC checking his phone.
    with dissolve

    $ phoneexit = "s21_PhoneContinue"

    $ contact_Julia.addReply("Hey, how's it going?", "s21_JulReply1")
    $ showphone = True
    call screen phone

    label s21_JulReply1:
        $ contact_Julia.newMessage("Hey! I was just thinking about you, how's school?")
        $ contact_Julia.addReply("Good! About to go have dinner with some of the guys in my house", "s21_JulReply2")

        call screen messager(contact_Julia)

    label s21_JulReply2:
        $ contact_Julia.newMessage("I'm glad you're making friends, I'm so proud of you!")
        $ contact_Julia.addReply("Aww don't make me blush! They'll be here any second, I'll talk to you later", "s21_JulReply3")

        call screen messager(contact_Julia)

    label s21_JulReply3:
        $ contact_Julia.newMessage("<3")

        call screen messager(contact_Julia)

    label s21_PhoneContinue:
        if contact_Julia.messages[-1].replies:
            "(I should text Julia.)"
            jump s21_PhoneContinue

    $ showphone = False

    u "(I should probably head over to Ms. Roses.)"

    pause 1

    jump v9_dinner_w_rose



































