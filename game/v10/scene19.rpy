# SCENE 19: Text From Jenny
# Locations: Street Where MC Met Penelope
# Characters: MC (Outfit 1), Mr Lee (Outfit 1)
# Time: Sunday Night

default penelopelike = 0
default mrleelike = 0

label v10_walk_jenny_text:
    scene v10swjt1 # TPP. Show MC walking on the sidewalk where he originally met Penelope.
    with fade

    pause 0.75

    scene v10swjt2 # TPP. Show MC stood exactly where he met Penelope, phone in hand.
    with dissolve

    play sound "sounds/vibrate.mp3"

    u "(Phone buzzing, I should get that.)"

    $ phoneexit = "v10s19_PhoneContinue"

    $ contact_Jenny.newMessage("Hey [name], this is Jenny, a friend of Penelope. I've noticed she's been acting a little off.")
    $ contact_Jenny.newMessage("Btw, I got your number from her phone when she was in the bathroom.")
    $ contact_Jenny.addReply("Hey... yeah, Penelope has actually been dealing with some pretty heavy stuff. Also, the number stealing is a tad creepy, haha.", "v10s19_ReplyJen1")
    $ showphone = True
    call screen phone

    label v10s19_ReplyJen1:
        $ contact_Jenny.newMessage("I knew it!")
        $ contact_Jenny.newMessage("I didn’t know any other way to get in contact with her new friends...")
        $ contact_Jenny.addReply("I think it's best to tell you about it all in person, if you're cool with that?", "v10s19_ReplyJen2")
        call screen messager(contact_Jenny)

    label v10s19_ReplyJen2:
        $ contact_Jenny.newMessage("Sure, when and where?")
        $ contact_Jenny.addReply("Cafe off of Stevenson Street tomorrow morning?", "v10s19_ReplyJen3")
        call screen messager(contact_Jenny)

    label v10s19_ReplyJen3:
        $ contact_Jenny.newMessage("Sounds good to me, thanks [name]!")
        call screen messager(contact_Jenny)

    label v10s19_PhoneContinue:
        if contact_Jenny.messages[-1].replies:
        "(I should reply to Jenny.)"
        jump v10s19_PhoneContinue      

    $ showphone = False

    u "(Hmm, maybe I should invite Penelope too, otherwise it’s just me and Jenny.)"

    menu:
        "Invite Penelope":
            $ penelopelike += 1
            $ addPoint("bf", 1)

            u "(Yeah, I should invite her. Best if she's the one that breaks the news to her.)"

            $ showphone = True

            $ contact_Penelope.addReply("Hey, you free for coffee at the cafe in the morning?", "v10s19_ReplyPen1")
            call screen phone

            label v10s19_ReplyPen1:
                $ contact_Penelope.newMessage("Special occasion?")
                $ contact_Penelope.addReply("Honestly, if you're okay with talking about it, I just wanted to see how you were doing with all the school stuff.", "v10s19_ReplyPen2")
                call screen messager(contact_Penelope)

            label v10s19_ReplyPen2:
                $ contact_Penelope.newMessage("That’s sweet… thanks..")
                $ contact_Penelope.addReply("So are you free to meet?")
                call screen messager(contact_Penelope)

            label v10s19_ReplyPen3:
                $ contact_Penelope.newMessage("Yeah, of course. I’ll see you in the morning.")
                $ contact_Penelope.addReply("See ya!", "v10s19_PhoneContinue1")
                call screen messager(contact_Penelope)

            label v10s19_PhoneContinue1:
                if contact_Penelope.messages[-1].replies:
                "(I should text to Penelope.)"
                jump v10s19_PhoneContinue1     

            $ showphone = False

            u "(I hope this goes smooth, Jenny hearing it from Penelope will probably help them both process the situation.)"

        "Go Alone":
            u "(On the other hand, maybe there’s benefits to meeting Jenny alone…)"

    scene v10swjt3 # TPP. Show MC continuing to walk down the street, no longer holding phone.
    with dissolve

    pause 0.75

    scene v10swjt4 # FPP. Show Mr. Lee walking down the street towards camera, Lee notices MC and smiles.
    with dissolve

    pause 0.75

    scene v10swjt5 # FPP. Close up Lee, smile, mouth open.
    with dissolve

    lee "Ah [name] , what are you doing out this late?"

    scene v10swjt5a # FPP. Same as 5, smile, mouth closed.
    with dissolve

    u "Hey Mr. Lee, not much, just taking a little walk. And you?"

    scene v10swjt5
    with dissolve

    lee "I'm just leaving from having dinner with a friend of mine."

    scene v10swjt5a
    with dissolve

    menu:
        "Make A Joke":
            $ mrleelike += 1
            $ addPoint("tm", 1)

            u "Teachers have friends?"

            scene v10swjt5
            with dissolve

            lee "Of course we do, son. We also have bedtimes and mine is coming up soon."

        "Don't Make A Joke":
            u "Sounds nice."

            scene v10swjt5
            with dissolve

            lee "Indeed it was, and now I should be headed home, it’s my bedtime soon."
        

    scene v10swjt5a
    with dissolve

    u "It's not even that late."

    scene v10swjt5
    with dissolve

    lee "By the time I get done reading and, grading papers and relaxing for a bit it will be."

    scene v10swjt5a
    with dissolve

    u "Guess I'll let you get to it."

    scene v10swjt5
    with dissolve

    lee "I'll see you in class!"

    scene v10swjt6 # TPP. Show MC and Mr. Lee walking off in opposite directions, MC slight grin.
    with dissolve

    u "(I'm seeing everybody today. It is getting a little dark, I'm gonna hurry up and get back.)"

    jump v10_room_mon_night