# SCENE 53: Transition Mc walks home WOLVES OR APES
# Locations: MC walking on the sidewalk
# Characters: MC (Outfit: 2)
# Time: Morning

label v16s53:
    scene v16s53_1 # TPP. Show MC (Slight smile, mouth closed) walking down the sidewalk towards the Campus from the Dog shelter.
    with dissolve

    u "(The Dean coming in to psychologically kick that trucker in the nuts and adopt Oscar like that, really made my day. *Laughs*)"

    if not v16s28_lindsey_pb_intereview_polly_choice: # Get Polly to endorse Lindsey
        play sound "sounds/vibrate.mp3"

        scene v16s53_2 # TPP. Show MC (neutral face, mouth closed) standing on the sidewalk reaching in his pocket
        with dissolve 

        pause 0.75

        scene v16s53_2a # TPP. Show MC (neutral face, mouth closed) holding his phone and looking at it.
        with dissolve

        pause 0.75

        $ lindsey.messenger.newMessage("You're not going to believe this, but I found out that Polly is staying at a hotel where my friend works!", force_send=True)
        $ lindsey.messenger.addReply("That's not creepy at all... What's the plan?")
        $ lindsey.messenger.addReply("Oh, nice! So what's the plan? Just knock on the door? Lol")
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

    if v16s28_lindsey_pb_intereview_polly_choice: # Lindsey school intereview with
        scene v16s53_3 # TPP. MC (neutral face, mouth closed) walking further down the sidewalk.
        with dissolve

        pause 0.75

        jump v16s54 
    
    else:
        if joinwolves:
            scene v16s53_3
            with dissolve

            pause 0.75

            jump v16s56
        
        else:
            scene v16s53_3
            with dissolve

            pause 0.75

            jump v16s57