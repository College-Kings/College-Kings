# SCENE 22a: Lindsey convo after plan
# Locations: School Hallway
# Characters: LINDSEY (Outfit: 1), MC (Outfit: 9)
# Time: Evening

label v14s22a:
    play music "music/v13/Track Scene 39a.mp3" fadein 2

    scene v14s22a_1 # FPP. show just lindsey, looking at mc, half smile, mouth open, hand up gesture
    with dissolve

    li "So... People have been treating me like the Vice President of the United States."

    scene v14s22a_1a # FPP. same as v14s22a_1 lindsey's hand is down mouth closed
    with dissolve

    u "*Laughs* What makes you say that?"

    scene v14s22a_1b # FPP. same as v14s22a_1a lindsey mouth open
    with dissolve

    li "They either respect, love and pray that I succeed, or they completely despise me and won't even look in my direction."

    scene v14s22a_1a
    with dissolve

    u "Welcome to the world of fame, baby! *Chuckles*"

    u "Everyone knows who you are now, Lindsey. That's what you wanted, right?"

    scene v14s22a_1
    with dissolve

    li "It's what I needed, yes. If you ask me what I wanted we'd be speaking of fantasies."

    scene v14s22a_1a
    with dissolve

    u "That I can understand."

    scene v14s22a_1b
    with dissolve

    li "At the end of the day, as long as all of this was worth something, I'll be happy. People's radical emotions will calm down after the election, right?"

    scene v14s22a_1a
    with dissolve

    u "Let's hope so, yeah. But regardless, these next few weeks are gonna be rough for you."

    scene v14s22a_1
    with dissolve

    li "*Sighs* You're preaching to the choir."

    scene v14s22a_1a
    with dissolve

    u "You know I'm here for you though."

    scene v14s22a_1
    with dissolve

    li "Yeah, I know that."

    play sound "sounds/vibrate.mp3"

    u "*Phone vibrates*"
    
    scene v14s22a_1b
    with dissolve

    li "Your phone is buzzing I think."

    if v14_talk_to_chris:
        scene v14s22a_1a
        with dissolve

        u "Yeah, I should probably take this."

        scene v14s22a_1
        with dissolve

        li "Alright, I need to run anyway."

        scene v14s22a_1b
        with dissolve

        li "Thank you, once again, for everything."

        scene v14s22a_1a
        with dissolve

        u "Once again, always."

        scene v14s22a_2 # TPP. lindsey waves good bye, full smile, mouth open and rushes off 
        with dissolve

        pause 0.75

        scene v14s22a_3 # TPP. MC starts walking outside and is looking at his phone as he walks
        with dissolve

        u "(Oh, right, Chloe's on her way to the Wolves house. Need to rush now.)"

        stop music fadeout 3
        jump v14s23

    else:
        scene v14s22a_1a
        with dissolve

        u "Yeah, oh well. It can wait."

        scene v14s22a_1
        with dissolve

        li "No, no. It may be important. Besides, I need to run anyway."

        scene v14s22a_1b
        with dissolve

        li "Thank you, once again, for everything."

        scene v14s22a_1a
        with dissolve

        u "Once again, always."

        scene v14s22a_2 # TPP. lindsey waves good bye, full smile, mouth open and rushes off 
        with dissolve

        pause 0.75

        scene v14s22a_3 # TPP. MC starts walking outside and is looking at his phone as he walks
        with dissolve

        u "(Let's see who this is...)"

        stop music fadeout 3
        jump v14s24