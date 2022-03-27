# SCENE 25a: MC wakes up
# Locations: MC's Wolves Room/Apes Room, Aubrey's room at the Chick's house.
# Characters: MC (Outfit: Underwear to 9), AUBREY (Outfit: 3)
# Time: Morning

init python:
    def v16s25a_reply_thankyou():
        riley.messenger.newMessage("Thank you! :)")
    def v16s25a_reply_sorry():
        riley.messenger.newMessage("Um, no... As soon as he told me I got the job he acted like the search was over, haha. Sorry :(")
    def v16s25a_reply_assistant():
        riley.messenger.newMessage("Aw, well, who knows? Maybe I'll need an assistant one day.")
    def v16s25a_reply_tongue_emoji():
        riley.messenger.newMessage(":P")

label v16s25a:
    scene sleep_transition_fast # Ignore animation 
    with fade

    pause 2.2
    
    scene black
    with dissolve
        
    pause 1

    if joinwolves:
        scene v16s25a_1 # TPP. In wolves room. Show MC sitting up from bed and yawning his arms stretched, MC yawning (underware only).
        with dissolve

        pause 0.75

        play sound "sounds/vibrate.mp3"

        scene v16s25a_2 # TPP. In wolves room. Show MC grabbing his phone from off his nightstand, MC neutral face, mouth closed.
        with dissolve

        pause 0.75

        scene v16s25a_1a # TPP. In wolves room. Show MC looking at his phone, MC neutral face, mouth closed.
        with dissolve

        pause 0.75
        
        ### call phone and check for replies

        $ riley.messenger.newMessage("Guess who got the newspaper job?", force_send=True)
        $ riley.messenger.newMessage("MEEEEEEEEE!")
        $ riley.messenger.addReply("Haha, congrats!", v16s25a_reply_thankyou) 
        
        if v16s11_sign_up:
            $ riley.messenger.addReply("What about me? Do you know?", v16s25a_reply_sorry) 
            $ riley.messenger.addReply("Ouch. There go my journalist dreams :(")
            $ riley.messenger.addReply("Ah, nice. I was kind of hoping I didn't get it, haha.", v16s25a_reply_assistant) 
            $ riley.messenger.addReply("Jeez, the power is already going straight to your head...", v16s25a_reply_tongue_emoji) 

        scene v16s25a_1a
        with dissolve

        u "(Good for her. She really wanted that job and she'll be awesome at it. Having a school newspaper sounds kind of fun, too.)"

        scene v16s25a_3 # TPP. In wolves room. Show MC getting out of bed, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v16s25a_4 # TPP. In wolves room. Show MC standing in the middle of his room putting on his shirt for the day, face obscured by the shirt.
        with dissolve

        pause 0.75
        
        play sound "sounds/vibrate.mp3"

        scene v16s25a_4a # TPP. In wolves room. Show MC standing in the middle of his room looking at his phone, slight smile, mouth closed. 
        with dissolve

        pause 0.75

        scene v16s25a_4b # TPP. In wolves room. Show MC with the phone to his ear, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v16s25a_5 # TPP. Aubrey in the Chicks house in her room on the phone, slight smile, mouth open.
        with dissolve

        au "Hey, [name]. Did you guys have a power outage last night in the dorms?"

        scene v16s25a_5a # TPP. Aubrey in the Chicks house in her room on the phone, slight smile, mouth closed.
        with dissolve

        u "Um... No, not that I noticed."

        scene v16s25a_5
        with dissolve

        au "Hm, weird. Apparently, it's been happening a lot this week."

        scene v16s25a_5a
        with dissolve

        u "Well, if your freezer defrosts and you need to eat all the food before it spoils, let me know."

        scene v16s25a_5
        with dissolve

        au "Haha, I think it's mainly full of ice cream, so... The Chicks will definitely have that covered."

        scene v16s25a_5a
        with dissolve

        u "Haha, fair enough."

        scene v16s25a_5
        with dissolve

        au "Anyway, I'm telling people it might be a good idea to stock up on candles or flashlights."

        scene v16s25a_5a
        with dissolve

        u "Shit. SVC is going back to the stone age..."

        scene v16s25a_5
        with dissolve

        au "Yeah, exactly. *Laughs*"

        scene v16s25a_5a
        with dissolve

        u "Thanks for the heads up."

        scene v16s25a_5
        with dissolve

        au "No problem."

        if aubrey.relationship >= Relationship.TAMED:
            $ v16s25a_date_with_aubrey = True # TODO: Variable

            scene v16s25a_5b # TPP. Aubrey in the Chicks house in her room on the phone, slight smile, blushing, mouth open.
            with dissolve

            au "Also..."

            au "I'm free for a date tonight."

            scene v16s25a_5c # TPP. Aubrey in the Chicks house in her room on the phone, slight smile, blushing, mouth closed.
            with dissolve

            u "Oh. Are you?"

            scene v16s25a_5b
            with dissolve

            au "Yes. I thought that might be useful information for a certain gentleman. *Giggles*"

            scene v16s25a_5c
            with dissolve

            u "Hmm... Actually..."

            u "I think I know a certain gentleman who would be very interested to hear this information."

            scene v16s25a_5b
            with dissolve

            au "*Laughs* Let's do something. Something real."

            scene v16s25a_5c
            with dissolve

            u "You're serious? Like a serious date? You're ready?"

            scene v16s25a_5
            with dissolve

            au "Quit asking before I change my mind... Haha."

            scene v16s25a_5a
            with dissolve

            u "Okay, deal. Dinner tonight. I'll sort the details, stay by the phone."

            scene v16s25a_5
            with dissolve

            au "Ooh, sounds perfect."

            scene v16s25a_5a
            with dissolve

            u "Great, see you later."

            play sound "sounds/rejectcall.mp3"

        scene v16s25a_4c # TPP. In wolves room. Show MC standing in the middle of his room putting on his pants for the day, slight smile, mouth closed. 
        with dissolve

        pause 0.75

        scene v16s25a_6 # TPP. In wolves room, show MC looking at himself in the Mirror pointing finger guns and winking, slight smile, mouth open.
        with dissolve

        u "Let's get this day started, shall we?"

        play sound "sounds/dooropen.mp3"

        scene v16s25a_7 # TPP. In wolves room, show MC leaving his room.
        with dissolve

        pause 0.75

        jump v16s26

    else:
        scene v16s25a_8 # TPP. In Apes room. Show MC sitting up from bed and yawning his arms stretched, MC yawning.
        with dissolve

        pause 0.75

        play sound "sounds/vibrate.mp3"

        scene v16s25a_9 # TPP. In Apes room. Show MC grabbing his phone from off his nightstand, MC neutral face, mouth closed.
        with dissolve

        pause 0.75

        scene v16s25a_8a # TPP. In Apes room. Show MC looking at his phone, MC neutral face, mouth closed.
        with dissolve

        pause 0.75

        $ riley.messenger.newMessage("Guess who got the newspaper job?", force_send=True)
        $ riley.messenger.newMessage("MEEEEEEEEE!")
        $ riley.messenger.addReply("Haha, congrats!", v16s25a_reply_thankyou) 
        
        ### call phone and check for replies
        
        if v16s11_sign_up:
            $ riley.messenger.addReply("What about me? Do you know?", v16s25a_reply_sorry) 
            $ riley.messenger.addReply("Ouch. There go my journalist dreams :(")
            $ riley.messenger.addReply("Ah, nice. I was kind of hoping I didn't get it, haha.", v16s25a_reply_assistant) 
            $ riley.messenger.addReply("Jeez, the power is already going straight to your head...", v16s25a_reply_tongue_emoji) 

        scene v16s25a_8a
        with dissolve

        u "(Good for her. She really wanted that job and she'll be awesome at it. Having a school newspaper sounds kind of fun, too.)"

        scene v16s25a_10 # TPP. In Apes room. Show MC getting out of bed, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v16s25a_11 # TPP. In Apes room. Show MC standing in the middle of his room putting on his shirt for the day, face obscured by the shirt.
        with dissolve

        pause 0.75
        
        play sound "sounds/vibrate.mp3"

        scene v16s25a_11a # TPP. In Apes room. Show MC standing in the middle of his room looking at his phone, slight smile, mouth closed. 
        with dissolve

        pause 0.75

        scene v16s25a_11b # TPP. In Apes room. Show MC with the phone to his ear, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v16s25a_5 # TPP. Aubrey in the Chicks house in her room on the phone, slight smile, mouth open.
        with dissolve

        au "Hey, [name]. Did you guys have a power outage last night in the dorms?"

        scene v16s25a_5a # TPP. Aubrey in the Chicks house in her room on the phone, slight smile, mouth closed.
        with dissolve

        u "Um... No, not that I noticed."

        scene v16s25a_5
        with dissolve

        au "Hm, weird. Apparently, it's been happening a lot this week."

        scene v16s25a_5a
        with dissolve

        u "Well, if your freezer defrosts and you need to eat all the food before it spoils, let me know."

        scene v16s25a_5
        with dissolve

        au "Haha, I think it's mainly full of ice cream, so... The Chicks will definitely have that covered."

        scene v16s25a_5a
        with dissolve

        u "Haha, fair enough."

        scene v16s25a_5
        with dissolve

        au "Anyway, I'm telling people it might be a good idea to stock up on candles or flashlights."

        scene v16s25a_5a
        with dissolve

        u "Shit. SVC is going back to the stone age..."

        scene v16s25a_5
        with dissolve

        au "Yeah, exactly. *Laughs*"

        scene v16s25a_5a
        with dissolve

        u "Thanks for the heads up."

        scene v16s25a_5
        with dissolve

        au "No problem."

        if aubrey.relationship >= Relationship.TAMED:
            $ v16s25a_date_with_aubrey = True
        
            scene v16s25a_5b
            with dissolve

            au "Also..."

            au "I'm free for a date tonight."

            scene v16s25a_5c
            with dissolve

            u "Oh. Are you?"

            scene v16s25a_5b
            with dissolve

            au "Yes. I thought that might be useful information for a certain gentleman. *Giggles*"

            scene v16s25a_5c
            with dissolve

            u "Hmm... Actually..."

            u "I think I know a certain gentleman who would be very interested to hear this information."

            scene v16s25a_5b
            with dissolve

            au "*Laughs* Let's do something. Something real."

            scene v16s25a_5c
            with dissolve

            u "You're serious? Like a serious date? You're ready?"

            scene v16s25a_5
            with dissolve

            au "Quit asking before I change my mind... Haha."

            scene v16s25a_5a
            with dissolve

            u "Okay, deal. Dinner tonight. I'll sort the details, stay by the phone."

            scene v16s25a_5
            with dissolve

            au "Ooh, sounds perfect."

            scene v16s25a_5a
            with dissolve

            u "Great, see you later."

            play sound "sounds/rejectcall.mp3"

        scene v16s25a_11c # TPP. In Apes room. Show MC standing in the middle of his room putting on his pants for the day, slight smile, mouth closed. 
        with dissolve

        pause 0.75

        scene v16s25a_12 # TPP. In Apes room, show MC looking at himself in the Mirror pointing finger guns and winking, slight smile, mouth open.
        with dissolve
        
        u "Let's get this day started, shall we?"

        play sound "sounds/dooropen.mp3"

        scene v16s25a_13 # TPP. In Apes room, show MC leaving his room.
        with dissolve

        pause 0.75

        jump v16s26