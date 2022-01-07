# SCENE 12: Going home from airport
# Locations: Street to San Vallejo College
# Characters: MC (Outfit: 5), JULIA (Outfit: 1)
# Time: Afternoon 

init python:
    def v14_emmy_simplr1():
        emmy.simplr.newMessage("I never said we didn't")
        emmy.simplr.newMessage("I just wanted you to know the truth before I was gone. What we did was a mistake.")
        emmy.simplr.addReply("No, it wasn't")
        emmy.simplr.addReply("Yeah, it was.")
        emmy.simplr.newMessage("Goodbye, [name].")
        simplr_contacts.remove(emmy.simplr)
    
    def v14_emmy_simplr2():
        emmy.simplr.newMessage("That's completely fair")
        emmy.simplr.newMessage("I just wanted you to know the truth before I was gone. What we did was a mistake.")
        emmy.simplr.addReply("No, it wasn't")
        emmy.simplr.addReply("Yeah, it was.")
        emmy.simplr.newMessage("Goodbye, [name].")
        simplr_contacts.remove(emmy.simplr)

    def v14_emmy_simplr3():
        emmy.simplr.newMessage("Well, regardless of what it is I've chosen to delete this app. So, this is goodbye.")
        simplr_contacts.remove(emmy.simplr)

label v14s12:
    play music "music/v12/Track Scene 33_2.mp3" fadein 2

    scene v14s12_1 # TPP. MC walking down the sidewalk back to San Vallejo, slight smile, mouth closed. 
    with fade
    play sound "sounds/call.mp3"

    pause 0.75

    scene v14s12_2 # TPP. MC standing still further down the side walk. Reaching for his pocket, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v14s12_2a # TPP. Same as v14s12_2, Show MC looking down at his phone which he is holding, slight smile, mouth closed
    with dissolve
    
    pause 0.75

    stop sound
    play sound "sounds/rejectcall.mp3"

    scene v14s12_2b # TPP. Same as v14s12_2b, MC holding phone to his ear, slight smile, mouth open.
    with dissolve

    u "Hello?"

    scene v14s12_3 # TPP. Show Julia on the phone at her home, slight smile, mouth open.
    with dissolve

    ju "Hey honey! Just calling to check in. Today was the day you got back in town, right?"

    scene v14s12_3a # TPP. Same as v14s12_3, Julia slight smile, mouth closed.
    with dissolve

    u "Sure was, I'm headed to my room now."

    scene v14s12_3
    with dissolve

    ju "That's great to hear, honey. I'm glad you made it back safe and sound."

    scene v14s12_3a
    with dissolve

    u "Safe or not, I'm happy to be back."

    scene v14s12_3
    with dissolve

    ju "Oh hush."

    scene v14s12_3a
    with dissolve

    u "Haha. So what's up?"

    scene v14s12_3
    with dissolve

    ju "Well honey, I do have some unfortunate news to share with you."

    scene v14s12_3a
    with dissolve

    u "Oh... Alright. What's that?"

    scene v14s12_3
    with dissolve

    ju "Remember how I said I'd come see you the minute you got back?"

    scene v14s12_3a
    with dissolve

    u "Yes, I remember."

    scene v14s12_3
    with dissolve

    ju "Well, not only will I have to break that promise, but I don't know when I'll see you next."

    scene v14s12_3a
    with dissolve

    u "Is something wrong, or...?"

    scene v14s12_3
    with dissolve

    ju "It's work. They're pulling me away to New York."

    scene v14s12_3a
    with dissolve

    u "Are you going to keep hiding this secret job from me? What is it that you actually do? *Chuckles*"

    scene v14s12_3
    with dissolve

    ju "For as long as they make me keep it a secret, yes. I am keeping it from you. *Laughs*"

    scene v14s12_3a
    with dissolve

    u "Are you an FBI Agent or something?"

    scene v14s12_3
    with dissolve

    ju "*Chuckles* I'm the \"or something\"."

    scene v14s12_3a
    with dissolve

    u "Haha, okay. I couldn't picture you in the FBI anyway."

    scene v14s12_3b # TPP. Same as v14s12_3, Julia different pose, slight smile, mouth open.
    with dissolve

    ju "Ha! How come? I'm smart and in good shape..."

    scene v14s12_3c # TPP. Same as v14s12_3b, Julia slight smile, mouth closed
    with dissolve

    u "Do you really want me to go into detail on why I think you wouldn't be good for the FBI?"

    scene v14s12_3b
    with dissolve

    ju "Eh... Good call, you can keep it to yourself. *Laughs*"

    scene v14s12_3c
    with dissolve

    u "Haha..."

    u "Well, how long do you think you'll be away?"

    scene v14s12_3b
    with dissolve

    ju "I have no idea, that's why I wanted to call."

    scene v14s12_3c
    with dissolve

    u "I got it, just keep me posted and we'll go from there. Okay?"

    scene v14s12_3b
    with dissolve

    ju "I will honey. Be safe, and please don't hesitate to call if you need me... I love you."

    scene v14s12_3c
    with dissolve

    u "Love you too."

    scene v14s12_3b
    with dissolve

    ju "Goodbye."

    scene v14s12_3c
    with dissolve

    u "Bye."

    play sound "sounds/rejectcall.mp3"

    scene v14s12_4 # FPP. MC walking down the side walk looking at the San Vallejo college.
    with dissolve

    u "(Still keeping this job a secret is really suspicious... And having to go to New York of all places is pretty... odd. Oh, well.)"

    if emmy.simplr in simplr_contacts:
        if "v13_emmy" in sceneList:
            $ emmy.simplr.newMessage("Oh, hey...", force_send=True)
            $ emmy.simplr.addReply("Hey, we had a great time together, hope to see you again <3")
            $ emmy.simplr.newMessage("I had a good time as well, but...")
            $ emmy.simplr.newMessage("I have to be honest with you")
            $ emmy.simplr.addReply("Oof, I sense that a bomb is about to drop, haha")
            $ emmy.simplr.newMessage("Well, yeah. Um, I have a boyfriend actually")
            $ emmy.simplr.addReply("What the fuck?! Wait, you... what?")
            $ emmy.simplr.newMessage("Trust me, I already know what you're thinking.")
            $ emmy.simplr.addReply("I'm not sure that you do")
            $ emmy.simplr.newMessage("Well, regardless of what it is I've chosen to delete this app. So, this is goodbye.")
            $ emmy.simplr.newMessage("And most importantly I want to apologize for not telling you the truth. I was just trying to have a good time, you know?")
            $ emmy.simplr.addReply(_("We did. We had a good time."), v14_emmy_simplr1)
            $ emmy.simplr.addReply(_("Apology not accepted..."), v14_emmy_simplr2)
        else:
            $ emmy.simplr.newMessage("Oh, hey...", force_send=True)
            $ emmy.simplr.newMessage("I have to be honest with you", force_send=True)
            $ emmy.simplr.addReply("Oof, I sense that a bomb is about to drop, haha")
            $ emmy.simplr.newMessage("Well, yeah. Um, I have a boyfriend actually")
            $ emmy.simplr.addReply("What the fuck?! Wait, you... what?")
            $ emmy.simplr.newMessage("Trust me, I already know what you're thinking.")
            $ emmy.simplr.addReply(_("I'm not sure that you do"), v14_emmy_simplr3)
    elif emmy.simplr in simplr_pendingContacts:
        $ emmy.simplr.removeContact()

    stop music fadeout 3
    if joinwolves:
        scene v14s12_5 # TPP. MC opening the door to the wolves frat house, slight smile, mouth closed.
        with fade

        pause 0.75

        jump v14s13
        
    else:
        scene v14s12_6 # TPP. MC opening the doorr to the apes frat house, slight smile, mouth closed
        with fade

        pause 0.75

        jump v14s13a