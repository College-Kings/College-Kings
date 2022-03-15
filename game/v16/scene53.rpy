# SCENE 53: Transition Mc walks home WOLVES OR APES
# Locations: MC walking to Wolves or Apes Room
# Characters: MC (Outfit: 2)
# Time: Morning

label v16s53:

    scene v16s53_1 # TPP. Show MC(Slight smile, mouth closed) walking down the street towards the Campus from the Dog shelter.
    with dissolve

    u "(The Dean coming in to psychologically kick that trucker in the nuts and adopt Oscar like that, really made my day. *Laughs*)"

    if lindsey_polly_endorsement: #Placeholder

        play sound "sounds/vibrate.mp3"

        scene v16s53_2 # TPP. Show MC(neutral face, mouth closed.) stood still on the street reaching in his pocket
        with dissolve 

        pause 0.15

        scene v16s53_2a # TPP. Show MC(Neutral face, mouth closed.) holding his phone and looking at it.
        with dissolve

        $ lindsey.messenger.newMessage("You're not going to believe this, but I found out that Polly is staying at a hotel where my friend works!", force_send=True)
        $ lindsey.messenger.addReply("That's not creepy at all... What's the plan?", v16s53_Reply1)
        $ lindsey.messenger.addReply("Oh, nice! So what's the plan? Just knock on the door? Lol", v16s53_Reply2)
        $ lindsey.messenger.newMessage("Meet me there this afternoon and we can discuss it. Sending you a ping now.")
        $ lindsey.messenger.addReply("Okay, I'll see you soon.")

        label v16s53_PhoneContinueReply:
            if lindsey.messenger.replies:
                call screen phone
            if lindsey.messenger.replies:
                u "(I should reply to Lindsey.)"
                jump v16s53_PhoneContinueReply

        scene v16s53_2a
        with dissolve

        u "(Well, that wasn't very hard...)"

    if lindsey_newspaper_interview:
        scene v16s53_3 # TPP. MC(neutral face, mouth closed) walking further down the street.
        with dissolve

        jump v16s54 
    else:
        if joinwolves:
            scene v16s53_3
            with dissolve

            jump v16s56
        else:
            scene v16s53_3
            with dissolve

            jump v16s57
