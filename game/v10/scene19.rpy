# SCENE 19: Text From Jenny
# Locations: Street Where MC Met Penelope
# Characters: MC (Outfit 1), Mr Lee (Outfit 1)
# Time: Sunday Night

label v10_walk_jenny_text:
    scene v10swjt1 # TPP. Show MC walking on the sidewalk where he originally met Penelope.
    with fade

    play music music.ck1.v10.Track_Scene_19 fadein 2

    pause 0.75

    scene v10swjt2 # TPP. Show MC stood exactly where he met Penelope, phone in hand.
    with dissolve

    play sound sound.vibrate

    u "(Phone buzzing, I should get that.)"

    $ MessengerService.new_message(jenny, "Hey [name], this is Jenny, a friend of Penelope. I've noticed she's been acting a little off.")
    $ MessengerService.new_message(jenny, "Btw, I got your number from her phone when she was in the bathroom.")
    $ MessengerService.add_reply(jenny, "Hey... yeah, Penelope has actually been dealing with some pretty heavy stuff. Also, the number stealing is a tad creepy, haha.")
    $ MessengerService.new_message(jenny, "I knew it!")
    $ MessengerService.new_message(jenny, "I didn't know any other way to get in contact with her new friends...")
    $ MessengerService.add_reply(jenny, "I think it's best to tell you about it all in person, if you're cool with that?")
    $ MessengerService.new_message(jenny, "Sure, when and where?")
    $ MessengerService.add_reply(jenny, "Cafe off of Stevenson Street tomorrow morning?")
    $ MessengerService.new_message(jenny, "Sounds good to me, thanks [name]!")

    while MessengerService.has_replies(jenny):
        call screen phone
        if MessengerService.has_replies(jenny):
            u "(I should reply to Jenny.)"

    u "(Hmm, maybe I should invite Penelope too, otherwise it's just me and Jenny.)"

    menu:
        "Invite Penelope" (boyfriend=1.0):
            $ penelope.points += 1
            $ v10_inv_pen_cafe = True
            $ reputation.add_point(RepComponent.BOYFRIEND)

            u "(Yeah, I should invite her. Best if she's the one that breaks the news to her.)"

            $ MessengerService.add_reply(penelope, "Hey, you free for coffee at the cafe in the morning?")
            $ MessengerService.new_message(penelope, "Special occasion?")
            $ MessengerService.add_reply(penelope, "Honestly, if you're okay with talking about it, I just wanted to see how you were doing with all the school stuff.")
            $ MessengerService.new_message(penelope, "That's sweet... thanks..")
            $ MessengerService.add_reply(penelope, "So are you free to meet?")
            $ MessengerService.new_message(penelope, "Yeah, of course. I'll see you in the morning.")
            $ MessengerService.add_reply(penelope, "See ya!")

            while MessengerService.has_replies(penelope):
                call screen phone
                if MessengerService.has_replies(penelope):
                    u "(I should text Penelope.)"

            u "(I hope this goes smooth, Jenny hearing it from Penelope will probably help them both process the situation.)"

        "Go alone":
            u "(On the other hand, maybe there's benefits to meeting Jenny alone...)"

    scene v10swjt3 # TPP. Show MC continuing to walk down the street, no longer holding phone.
    with dissolve

    pause 0.75

    scene v10swjt4 # FPP. Show Mr. Lee walking down the street towards camera, Lee notices MC and smiles.
    with dissolve

    pause 0.75

    scene v10swjt5 # FPP. Close up Lee, smile, mouth open.
    with dissolve

    lee "Ah [name], what are you doing out this late?"

    scene v10swjt5a # FPP. Same as 5, smile, mouth closed.
    with dissolve

    u "Hey Mr. Lee, not much, just taking a little walk. And you?"

    scene v10swjt5
    with dissolve

    lee "I'm just leaving from having dinner with a friend of mine."

    scene v10swjt5a
    with dissolve

    menu:
        "Make a joke":
            u "Teachers have friends?"

            scene v10swjt5
            with dissolve

            lee "Of course we do, son. We also have bedtimes and mine is coming up soon."

        "Don't make a joke":
            u "Sounds nice."

            scene v10swjt5
            with dissolve

            lee "Indeed it was, and now I should be headed home, it's my bedtime soon."
        

    scene v10swjt5a
    with dissolve

    u "It's not even that late."

    scene v10swjt5
    with dissolve

    lee "By the time I get done reading, grading papers and relaxing for a bit it will be."

    scene v10swjt5a
    with dissolve

    u "Guess I'll let you get to it."

    scene v10swjt5
    with dissolve

    lee "I'll see you in class!"

    scene v10swjt6 # TPP. Show MC and Mr. Lee walking off in opposite directions, MC slight grin.
    with dissolve

    u "(I'm seeing everybody today. It is getting a little dark, I'm gonna hurry up and get back.)"

    stop music fadeout 3

    jump v10_room_mon_night