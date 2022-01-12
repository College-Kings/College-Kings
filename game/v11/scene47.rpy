# SCENE 47: Walking home, Nora screams cliffhanger
# Location: Sidewalk
# Characters: MC (Outfit 3), Charli (Outfit 1)
# Time: Night

label v11_walking_back:
    scene v11wb1 # TPP. Show MC walking on the sidewalk, Charli a few feet behind him, Charli smirking, mouth closed, MC mouth closed, slight smile
    with dissolve
    play music "music/v10/Track Scene 41_1.mp3" fadein 2
    pause 0.75
    
    scene v11wb1a # TPP. Same as v11wb1, Show MC looking back at Charli, Charli smirking, mouth closed, MC mouth closed, slightly annoyed
    with dissolve

    pause 0.75

    scene v11wb1b # TPP. Same as v11wb1a, MC looking forward, slightly annoyed, mouth slightly open, Charli smirking, mouth closed
    with dissolve

    u "*Sighs*"

    scene v11wb2 # TPP. Same as v11wb1b, but MC and Charli in a different place on the sidewalk. MC slightly surprised, mouth closed, Charli neutral expression, mouth closed
    with dissolve

    play sound "sounds/vibrate.mp3"

    if config_censored:
        $ jenny.messenger.newImgMessage("gui/censoredPopup/censoredBackground.webp", force_send=True)
    else:
        $ jenny.messenger.newImgMessage("images/v11/Scene 47/jennynude.webp", force_send=True) # Jenny nude pic (selfie or pic in a mirror)
    $ jenny.messenger.newMessage("OMG, I'M SO SORRY!", force_send=True)
    $ jenny.messenger.newMessage("I DID NOT MEAN TO SEND THAT!", force_send=True)
    $ jenny.messenger.addReply("Haha, don't worry about it.")

    u "(Wow... It's been so long since I've gotten a text, I forgot I even had this thing. *Chuckles*)"

    scene v11wb3 # TPP. Same position as v11wb2, show MC looking down at his phone, slightly surprised, mouth closed
    with dissolve

    label v11s47_PhoneContinueJenny:
        if jenny.messenger.replies:
            call screen phone
        if jenny.messenger.replies:
            u "(I should check my phone.)"
            jump v11s47_PhoneContinueJenny

    scene v11wb3a # TPP. Same as v11wb3, show MC putting his phone away, smiling, mouth closed
    with dissolve

    u "(Well... That was unexpected.)"

    scene v11wb4 # TPP. Same as v11wb1a, different place on the sidewalk, different poses
    with dissolve

    pause 0.75

    scene v11wb4a # TPP. Same as v11wb4, MC and Charli now standing next to each other (Charli walked to where MC is), they're looking at each other, Charli smirking, mouth closed, MC neutral expression, mouth closed
    with dissolve

    menu:
        "Apologize":
            scene v11wb5 # FPP. Same positioning as v11wb4a, MC and Charli looking at each other, Charli smirking, mouth closed
            with dissolve

            u "Hey man, look... Um. I know it's been a while since we last talked, but I just wanted to apologize for everything."

            scene v11wb5a # FPP. Same as v11wb5, different pose
            with dissolve
            
            u "I know we didn't exactly get off on the right foot since I was like, assuming things about you and that was really wrong of me. I shouldn't have gone about things the way that I did."

        "Tell him off":
            scene v11wb5a
            with dissolve

            u "You know... Since we last spoke I thought maybe, just maybe, I wasn't getting the \"bigger picture\"."

            scene v11wb5
            with dissolve
            
            u "But the truth is, after speaking with MY friends, I know damn well I'm not a bad person like you try to make me out to be. You're just a stuck up asshole that doesn't know how to mind his own business."

    scene v11wb5b # FPP. Same as v11wb5, Charli mouth open, smirking, different pose
    with dissolve

    charli "Haha, [name]... I couldn't care less what you think about me, good or bad. And frankly, it doesn't matter what the girls think either, because they're too blinded by your bullshit to see the truth."

    scene v11wb5c # FPP. Same as v11wb5b, Charli mouth open, slightly annoyed, different pose
    with dissolve
    
    charli "You may think you're some kind of womanizer or player or whatever you consider to be manly in your small, delusional mind."

    scene v11wb5d # FPP. Same as v11wb5c, Charli now pointing his finger at MC, Charli mouth open, slightly annoyed
    with dissolve
    
    charli "Let me be very clear, you're a sad, disloyal dirtbag, desperate for female attention, so desperate that you don't care who you're hurting in the process."

    scene v11wb5b
    with dissolve
    
    charli "And your friends might not see that yet, but soon they will, I'll make sure of that."

    scene v11wb5
    with dissolve

    u "*Scoffs* Wow, you really are a giant piece of-"

    scene v11wb4b # TPP. Same as v11wb4a, MC and Charli startled and scared, looking in front of them (looking at the same place), both mouths closed
    with vpunch

    no "AHHHH!!!!"
    stop music fadeout 3
    jump end11

label end11:
    if not renpy.loadable("v12/scene1.rpy"):
        scene savenow
        with Fade (1,0,1)
        " "

    if renpy.loadable("v12/scene1.rpy"):
        jump v12_start
    else:
        call screen end_screen