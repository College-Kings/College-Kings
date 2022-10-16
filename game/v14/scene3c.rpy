# SCENE 03c: Brothel Bar
# Locations: Brothel Bar
# Characters: MADAME (Outfit: 1), MC (Outfit: 3), Satin (Outfit: 1), Ryan (Outfit: 1), Emerald (Outfit: 1)
# Time: Night 

label v14s03c:
    play music "music/v13/Track Scene 62a.mp3" fadein 2

    scene v14s03c_1 # TPP. Show MC walking in the Brothel bar, slight smile, mouth open.
    with dissolve

    pause 0.75

    scene v14s03c_2 # TPP. Show MC sitting at a bar stool in the Brothel Bar, slight smile, mouth open.
    with dissolve

    pause 0.75

    scene v14s03c_3 # FPP. Madame standing infront of MC on the otherside of the bar, MC looking at Madame, Madame slight smile, mouth open.
    with dissolve

    madame "How are you, dear? What can I get you?"

    scene v14s03c_3a # FPP. Same as v14s03c_3, Madame slight smile, mouth closed.
    with dissolve

    u "Two of whatever you've got back there, please."

    scene v14s03c_3
    with dissolve

    madame "Haha, you definitely aren't picky... But I guess if a man comes to a place like this, he never was."

    scene v14s03c_3a
    with dissolve

    u "Ha... Right..."

    scene v14s03c_3
    with dissolve

    madame "I'll be right back with your drinks."

    scene v14s03c_3a
    with dissolve

    u "Thanks."

    scene v14s03c_2
    with fade

    pause 0.75

    scene v14s03c_2a # TPP. Show MC in a different pose while sitting on the bar stool, MC slight smile, mouth closed. 
    with fade

    pause 0.75

    scene v14s03c_3b # FPP. Same as v14s03c_3a, MC looking at the bar, Madame not in sight.
    with dissolve
    
    u "What is she doing?"

    scene v14s03c_4 # FPP. MC looking to his side where the rest of the bar stools are, Satin walking up to the stool next to MC, Satin slight annoyed face, mouth closed.
    with dissolve

    pause 0.75

    scene v14s03c_4a # FPP. Same as v14s03c_4, Satin sitting next to MC, MC looking at Satin, Satin looking forward at the bar, slightly annoyed, mouth open.
    with dissolve
    
    satin "*Sigh*"

    scene v14s03c_4b # FPP. Same as v14s03c_4a, Satin slightly annoyed, mouth closed.
    with dissolve

    u "Hey... Are you okay?"

    scene v14s03c_4c # FPP. Same as v14s03c_4b, Satin now looking at MC, Satin confused face, mouth open.
    with dissolve

    satin "What did you say?"

    scene v14s03c_4d # FPP. Same as v14s03c_4c, Satin confused face, mouth closed.
    with dissolve

    u "I asked if you were okay."

    scene v14s03c_4e # FPP. Same as v14s03c_4c, Satin slight smile, mouth open.
    with dissolve

    satin "A guy in a place like this, is asking a girl if she's okay? That's a first..."

    scene v14s03c_4f # FPP. Same as v14s03c_4c, Satin slight smile, mouth closed
    with dissolve

    u "A sad first, haha. What's your name?"

    scene v14s03c_4e
    with dissolve

    satin "Satin, you?"

    scene v14s03c_4f
    with dissolve

    u "[name]."

    scene v14s03c_4e
    with dissolve

    satin "Nice to meet you, [name]. You seem kind of young to be hanging around in a place like this."

    scene v14s03c_4f
    with dissolve

    menu:
        "Good genes":
            $ reputation.add_point(Reputations.BRO)

            u "Good genes. *Chuckles*"

            scene v14s03c_4e
            with dissolve

            satin "Same here."

        "My friends dragged me here":
            $ reputation.add_point(Reputations.BOYFRIEND)

            u "My friends dragged me in here."

            scene v14s03c_4e
            with dissolve

            satin "Haha, right."

    satin "So, what are you doing here at the bar all alone?"

    scene v14s03c_4f
    with dissolve

    u "I came here with two of my buddies, actually."

    u "One is off having a little fun somewhere else, or at least I hope... And the other is hitting it off with that girl right... there."

    scene v14s03c_5 # FPP. MC looking off past the bar pointing over at Ryan and Emerald, Ryan and Emerald both slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v14s03c_4g # FPP. Same as v14s03_4f, Satin looking at Emerald and Ryan(They are both off camera), Satin sligt smile, mouth open.
    with dissolve

    satin "Oh..."

    scene v14s03c_4f
    with dissolve

    u "Ha, uh oh... Why'd you say \"oh\" like that?"

    scene v14s03c_4e
    with dissolve

    satin "No reason. Do you and your friend come here often or...?"

    scene v14s03c_4f
    with dissolve

    u "Well, it's actually the last pitstop of our vacation."
    u "My friend Imre is a jack rabbit, but Ryan over there is a virgin. Something I found out minutes ago, actually."

    scene v14s03c_4e
    with dissolve

    satin "Oh, wow... It's rare for a virgin to walk in here. *Laughs*"

    satin "Is he planning on, you know... not being a virgin anymore?"

    scene v14s03c_4f
    with dissolve

    u "*Chuckles* Seems like it to me."

    scene v14s03c_4e
    with dissolve

    satin "Well, earlier when I said \"oh\" like that, it was because I'm pretty sure the girl he's talking to has an STD..."

    scene v14s03c_4f
    with dissolve

    u "Oh. I- Oh..."

    scene v14s03c_4e
    with dissolve

    satin "*Laughs*"

    scene v14s03c_4f
    with dissolve

    u "What? *Chuckles*"

    scene v14s03c_4e
    with dissolve

    satin "Haha, I'm sorry... It was just funny that you did exactly what I did. *Laughs*"

    scene v14s03c_4f
    with dissolve

    u "I guess I did, haha."

    scene v14s03c_4h # FPP. Same as v14s03c_4e, Satin different pose, slight smile, mouth open.
    with dissolve

    satin "I like you. You're not like most of the guys that walk in here."

    scene v14s03c_4i # FPP. Same as v14s03c_4f, Satin different pose, slight smile, mouth closed.
    with dissolve

    u "I try to be a little different."

    scene v14s03c_4h
    with dissolve

    satin "I'm curious though, are you looking for an escort?"

    scene v14s03c_4i
    with dissolve

    menu:
        "Yes, kinda":
            $ reputation.add_point(Reputations.BRO)
            u "Yeah, but I don't have that kind of money."

        "No, not really":
            $ reputation.add_point(Reputations.BOYFRIEND)
            u "Oh, no. I don't have that kind of money."

    scene v14s03c_4h
    with dissolve

    satin "I see..."

    satin "What if I gave you an entire hour for free?"

    scene v14s03c_4i
    with dissolve

    u "Oh, Satin... I don't-"

    scene v14s03c_4h
    with dissolve

    satin "Okay, first of all, don't say my name like that again unless you plan on fucking me afterwards."

    scene v14s03c_4i
    with dissolve

    u "*Gulps* I-"

    scene v14s03c_4h
    with dissolve

    satin "Secondly, before you answer, you should know that I was getting ready to go home anyways. *Chuckles*"

    satin "My shift has been over for a while now, but I like you. You're different and it's refreshing to meet someone who isn't a complete pervert."

    scene v14s03c_4i
    with dissolve

    u "Fair point."

    scene v14s03c_4e
    with dissolve

    satin "So, how about I make you an offer?"
    
    scene v14s03c_4f
    with dissolve

    u "I'm listening..."

    scene v14s03c_4e
    with dissolve

    satin "Since you've been so sweet I'll give you a free hour with me, to use one of two ways."

    scene v14s03c_4f
    with dissolve

    u "(Use?)"

    scene v14s03c_4h
    with dissolve

    satin "Either you and I go to the private booth and enjoy it together, or..."

    satin "If you're feeling generous enough, you can let me slide in and help out your virgin friend."

    menu:
        "Go with her":
            $ sceneList.add("v14_satin")
            $ satin.relationship = Relationship.FWB
            label v14s03c_sg:
                   
            $ reputation.add_point(Reputations.TROUBLEMAKER)

            scene v14s03c_4f
            with dissolve

            u "I can't pass up on an opportunity to be with you in a \"private booth\". *Chuckles*"

            scene v14s03c_4j # FPP. Same as v14s03c_4e, Satin slight smile, winking, mouth closed
            with dissolve

            pause 0.75

            scene v14s03c_4k # FPP. Same as v14s03c_4j, Satin standing up infront of the MC, slight smile, mouth closed.
            with dissolve

            pause 0.75

            scene v14s03c_4l # FPP. Same as v14s03c_4k, Satin holding MC's hand, Satin flirting smile, mouth open.
            with dissolve

            satin "Then follow me."

            scene v14s03c_6 # TPP. Show Satin holding MC's hand leading him towards the private booth, both slight smile, mouth closed.
            with dissolve

            pause 0.75

            stop music fadeout 3
            jump v14s03d
           
        "Help Ryan":
            $ reputation.add_point(Reputations.BRO)
            $ v14_ryan_satin = True

            scene v14s03c_5a # FPP. Same as v14s03c_5, Emerald on Ryan's lap, both slight smile, mouth closed.
            with dissolve

            u "*Sighs* As much as I'm gonna regret this..."

            scene v14s03c_4f
            with dissolve

            $ grant_achievement("saving_ryans_privates")

            u "Please go save my friend."

            scene v14s03c_4e
            with dissolve

            satin "Alright, then."

            scene v14s03c_4m # FPP. Same as v14s03c_4j, Satin slightly disappointed, mouth closed.
            with dissolve

            pause 0.75

            scene v14s03c_4n # FPP. Same as v14s03c_4m, Satin taking a sip of her drink.
            with dissolve

            pause 0.75

            scene v14s03c_5b # FPP. Same as v14s03c_5a, Show Satin walking towards Ryan and Emerald, Ryan and Emerald both slight smile, mouth closed.
            with dissolve

            pause 0.75

            scene v14s03c_5c # FPP. Same as v14s03c_5b, Satin taking Ryan's hand and pulling him away from Emerald, Satin slight smile, mouth closed, Emerald sad expression, mouth closed.
            with dissolve

            pause 0.75

            scene v14s03c_5d # FPP. Same as v14s03c_5c, Satin leading Ryan towards the private booth, Ryan excited expression looking at MC, mouth closed, Satin slight smile, mouth closed, Emerald sad expression, mouth closed.
            with dissolve

            u "(Can't believe I'm doing this for Ryan.)"

            scene v14s03c_3b
            with dissolve

            pause 0.75

            stop music fadeout 3
            jump v14s03e