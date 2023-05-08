# SCENE 43: MC Wakes To Jenny Call
# Locations: MC's Room, Cafe
# Characters: MC (Outfit: Boxers/1), JENNY (Outfit: 1)
# Time: Morning

label v13s43:
    scene v13s43_1 # TPP. Show MC in bed, phone buzzing on nightstand, eyes closed, neutral expression, mouth closed
    with dissolve

    play music music.ck1.v13.Track_Scene_43 fadein 2 

    pause 0.75

    scene v13s43_2 # TPP. Show MCs phone ringing, MC in the process of picking it up from nightstand, neutral expression, mouth closed 
    with dissolve

    pause 1.25

    scene v13s43_3 # TPP. Show MC having phone to his ear while in bed, slight smile, mouth open
    with dissolve

    u "Hello?"

    scene v13s43_4 # TPP. Show Jenny in cafe, phone to her ear, slight smile, mouth open
    with dissolve

    jen "Hey [name]! It's Jenny."

    scene v13s43_4a # TPP. Same as v13s43_4, mouth closed 
    with dissolve

    u "*Yawn* Jenny? Hey... What's up?"

    scene v13s43_4
    with dissolve

    jen "I'm sorry, did I wake you?"

    scene v13s43_4a 
    with dissolve

    u "Yeah, kinda. *Chuckles* But you're good, I shouldn't sleep in all day on vacation."

    scene v13s43_4b # TPP. Same as v13s43_4, slight laughing expression  
    with dissolve

    jen "*Chuckles* I'm such an idiot... I forgot about the time zones."

    scene v13s43_4a
    with dissolve

    u "It's all good, what's up?"

    if not v11_pen_goes_europe: #placeholder
        scene v13s43_4
        with dissolve

        jen "I just wanted to give you a heads up on Penelope..."

        scene v13s43_4c # TPP. Same as v13s43_4, nervous expression 
        with dissolve

        jen "Don't freak out but... She's missing."

        scene v13s43_4d # TPP. Same as v13s43_4a, nervous expression
        with dissolve

        u "What?! How can I not freak- *Sighs*"

        scene v13s43_4d
        with dissolve

        u "What do you mean she's missing?"

        scene v13s43_4c
        with dissolve

        jen "It's been two days and I haven't seen or heard from her at all."

        scene v13s43_4d
        with dissolve

        u "*Sighs* Do you think it's serious?"

        scene v13s43_4e # TPP. Same as v13s43_4c, different posture
        with dissolve

        jen "Yeah, I do... She wouldn't just ignore me like this."

        scene v13s43_4d
        with dissolve

        u "Fuck, okay... Has anything odd been going on lately?"

        scene v13s43_4c
        with dissolve

        jen "Not that I can think of, I've been considering everything. Things seemed perfectly normal two days ago."

        scene v13s43_4d
        with dissolve

        u "Have you contacted law enforcement or told the school?"

        scene v13s43_4e
        with dissolve

        jen "I haven't contacted-"

        scene v13s43_4b
        with dissolve

        jen "Oh... *Chuckles* Uhh..."

        scene v13s43_4a
        with dissolve

        u "What?"

        scene v13s43_4
        with dissolve

        jen "She just texted me."

        scene v13s43_4a
        with dissolve

        u "And? What'd she say?"

        scene v13s43_5 # TPP. Show Jenny looking at her phone, slight smile, mouth open
        with dissolve

        jen "It says, \"Sorry I got a new phone and had to get my contacts transferred. I haven't been ignoring you on purpose.\""

        scene v13s43_4a
        with dissolve

        u "*Laughs* Well, there we go. That says it all."

        scene v13s43_4b
        with dissolve

        jen "*Chuckles* I can't believe I had us both panicking for no reason. I'm so sorry, haha."

        scene v13s43_4a
        with dissolve

        u "It's fine, Jenny. *Chuckles* It was good to hear from you-"

        scene v13s43_4f # TPP. Same as v13s43_4, surprised expression 
        with dissolve

        jen "Oh my gosh, now she's calling me. Sorry I called and freaked you out like that, [name]. Talk to you soon?"

        scene v13s43_4a
        with dissolve

        u "Sounds good, bye."

        scene v13s43_4
        with dissolve

        jen "Bye."

        scene v13s43_6 # TPP. Show MC putting phone back on nightstand, slight smile, mouth closed 
        with dissolve

        pause 0.75 

        scene v13s43_7 # TPP. Show MC lying in bed, looking up at the roof, slight smile, mouth closed
        with dissolve

        u "(That's one way to wake up in the morning.)"

        scene v13s43_8 # TPP . Show MC getting out of bed, neutral expression, mouth closed
        with dissolve

        pause 0.75

        scene v13s43_9 # TPP. Show MC getting dressed, neutral expression, mouth closed
        with dissolve

        pause 0.75 

        scene v13s43_10 # TPP. Show MC leaving his room, neutral expression, mouth closed
        with dissolve

        pause 0.75 

        stop music fadeout 3

        jump v13s44

    else:
        scene v13s43_4
        with dissolve
        
        jen "I was just calling to see how Penelope is doing. Is she okay?"

        scene v13s43_4a
        with dissolve

        u "She's doing good I think, outside of the thousands of tasks they're giving her."

        scene v13s43_4c
        with dissolve

        jen "*Sighs* I assumed they'd be working her like crazy. Is she at least getting to have fun with everyone?"

        scene v13s43_4d
        with dissolve

        u "No, not really."

        if v13_penelope_concert:
            scene v13s43_4a 
            with dissolve
            
            u "I did get the chance to take her to a concert though."

            scene v13s43_4f
            with dissolve

            jen "What?! Who was the artist?"

            scene v13s43_4a
            with dissolve

            u "Polly..."

            scene v13s43_4g # TPP. Same as v13s43_4, different posture 
            with dissolve

            jen "Oh, wow! Penelope loves her... Did she enjoy herself?"

            scene v13s43_4a
            with dissolve

            u "Yeah, I think she had a memorable night."

        scene v13s43_4g
        with dissolve

        jen "Well, I wish she could enjoy the trip a bit more, but I'd rather her be there doing chores than being here worrying about possible jail time."

        scene v13s43_4a
        with dissolve

        u "You and I both, truly."

        scene v13s43_4h # TPP. Same as v13s43_4, serious expression
        with dissolve

        jen "You're such a caring person, [name]..."

        scene v13s43_4b
        with dissolve

        jen "When I'm ready to settle down and have a boyfriend, I just may have to send you an application. *Chuckles*"

        scene v13s43_4a
        with dissolve

        u "Haha, that's not what I expected to wake up to."

        scene v13s43_4b
        with dissolve

        jen "I'm just teasing... *Chuckles* You have a good rest of your day [name], and again, I'm so sorry I woke you."

        scene v13s43_4a
        with dissolve

        u "Really, haha... No worries Jenny, later."

        scene v13s43_4
        with dissolve

        jen "Bye."

        scene v13s43_6 
        with dissolve

        pause 0.75
        
        scene v13s43_7 
        with dissolve

        u "(That's one way to wake up in the morning.)"

        scene v13s43_8 
        with dissolve

        pause 0.75

        scene v13s43_9 
        with dissolve

        pause 0.75 

        scene v13s43_10 
        with dissolve

        pause 0.75

        stop music fadeout 3

        jump v13s44