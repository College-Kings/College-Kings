# SCENE 1: If Wolves, Imre conversation and bedtime
# Locations: Wolves Frat House, 
# Characters: MC (Outfit: 1), IMRE (Outfit: 2)
# Time: Night
# Render Count: 6 Unique Renders 33 Total

init python:
    def v15s1_reply1():
        chloe.messenger.newMessage("You're unbelievable.")

    def v15s1_reply2():
        chloe.messenger.newMessage("Well, at least you admit it...")

label v15_start:
    $ autumn.relationship = Relationship.FRIEND #Reset Autumn to FRIEND
    $ imre.relationship = Relationship.FRIEND #Reset Imre to FRIEND

    if (v14_help_lindsey and not v14_lindsey_sell) and not v14_date_distraction:
        $ lindsey_board.money -= 100 # we forgot about this one in v14

    if joinwolves:
        jump v15s1
    else:
        jump v15s2

label v15s1:
    if v13_imre_disloyal:
        play music "music/v15/Track Scene 1_1.mp3" fadein 2
    
        scene v15s1_1 # TPP. Imre's looking fully angry, standing at the door close, MC is sitting at his study desk, turned in the chair, facing Imre
        with dissolve

        u "Imre, listen to me..."

        scene v15s1_2 # FPP. Imre shuts the door and walks towards MC, full Angry Expression, mouth closed
        with dissolve

        pause 0.75

        scene v15s1_3 # FPP. Imre is standing over mc looking at mc while mc is still sitting at his desk, Imre has a half angry expression, mouth closed
        with dissolve

        u "There's absolutely no way that I'm telling Chris about me and Nora! How is that going to help anything or anyone?"

        scene v15s1_3a # FPP. same as v15s1_3 Imre's mouth is open, holding a fist up towards mc
        with dissolve

        imre "Loyalty, fucker! Chris has no idea that the real reason why he and Nora broke up is because you were interfering with their relationship."

        scene v15s1_3
        with dissolve

        u "That's not true, man."

        scene v15s1_3b # FPP. same as v15s1_3a Imre holds both his hands up palms up, Imre's mouth is still open
        with dissolve

        imre "How is it not?!"

        scene v15s1_3
        with dissolve

        u "The only person to blame for their breakup is..."

        menu:
            "Blame Chris":
                $ add_point(KCT.TROUBLEMAKER)
                $ add_point(KCT.BOYFRIEND)

                scene v15s1_3c # FPP. same as v15s1_3b Imre increases to a fully angry expression, Imre places his hands to his sides
                with dissolve

                u "Chris."

                scene v15s1_3d # FPP. same as v15s1_3 Imre's mouth is slightly open
                with dissolve

                imre "*Scoffs*"

                scene v15s1_3
                with dissolve

                u "They broke up because Nora felt ignored. Worthless. Alone."

                u "Everyone knows that. Ask around, dude."

                u "Even when she took the time to tell Chris exactly what she needed from him..."
                u "He still didn't give her the love or affection that she was asking for."

            "Blame Nora":
                $ add_point(KCT.BRO)
                $ v15_blame_nora = True

                scene v15s1_3
                with dissolve

                u "Nora. It's not my problem that she didn't have enough patience to wait until Chris was \"less busy\" for her."

                scene v15s1_3a
                with dissolve

                imre "So, the fact that you stood on the side lines looking like a knight in shining armor, that has nothing to do with why they broke up?"

                imre "Ha! That's what you're trying to say to me?"
            
        scene v15s1_3
        with dissolve

        u "Nora just wanted things to get better. She wanted it to feel like nothing was changing, but it was, and still is. So..."

        u "Whatever the official reasons are, the bottom line is that they grew apart. That's why it's over between them."

        scene v15s1_3d
        with dissolve

        imre "*Sighs*"

        if v15_blame_nora:
            scene v15s1_3e # FPP. same as v15s1_3b Imre raises his hand above his head in anger, while rolling his eyes, mouth is still open
            with dissolve

            imre "This is so fucked, [name]. This is so fucking fucked, bro!"

            scene v15s1_3
            with dissolve

            u "Imre, I know, and I'm sorry that you got dragged in, but you have to realize the truth."

            scene v15s1_3b
            with dissolve

            imre "None of us even know the truth!"

            scene v15s1_3
            with dissolve

            u "Alright, that's fair..."

        else:
            scene v15s1_3
            with dissolve

        u "Just take some time to really think about it, Imre."

        scene v15s1_3a
        with dissolve

        imre "I already have taken some time."

        scene v15s1_3
        with dissolve

        u "Telling Chris about Nora and I will only tear the Wolves apart and make things even worse."

        scene v15s1_3f # FPP. same as v15s1_3 Imre has decreased to slightly angry, more calm, mouth open
        with dissolve

        imre "..."

        scene v15s1_3g # FPP. same as v15s1_3f Imre's mouth is closed
        with dissolve

        u "We need to lay low and let them work out their shit or else this drama never ends, Imre."

        stop music fadeout 3

        play music "music/v15/Track Scene 1_2.mp3" fadein 2

        scene v15s1_3f
        with dissolve

        imre "*Sighs* Yeah..."

        imre "You're right."

        scene v15s1_3g
        with dissolve

        u "(I am?)"

        scene v15s1_3f
        with dissolve

        imre "I don't like that you're right but... You are."

        scene v15s1_3g
        with dissolve

        u "(I am!)"

        u "Imre, I really-"

        scene v15s1_3f
        with dissolve

        imre "You're lucky I came to talk to you first, man... 'Cause I was more than ready to tell him everything I know."

        scene v15s1_3g
        with dissolve

        u "Well, thank you. Really, I'm glad you came to talk to me first."

        u "The consequences would have been shit for all of us."

        scene v15s1_3f
        with dissolve

        imre "I know, but this doesn't mean I'm okay with what you're doing."

        scene v15s1_3g
        with dissolve

        u "I know, trust me."

        scene v15s1_3e
        with dissolve

        imre "Dammit man, this feels just like when Ross and Rachel broke up..."

        scene v15s1_3m
        with dissolve

        menu:
            "They were on a break":
                scene v15s1_3m
                #with dissolve

                # $ mc.quirks["pop_culture"] = True # Being re-evaluated
                $ add_point(KCT.BRO)

                u "They were on a break, bro..."

                scene v15s1_3h # FPP. same as v15s1_3a Imre has a happy expression, slight smile, mouth is still open
                with dissolve

                imre "*Laughs* My man..."

                scene v15s1_3i # FPP. same as v15s1_3h Imre's mouth is closed, Imre places his hands to his sides
                with dissolve

                u "Haha."

            "Who?":
                scene v15s1_3m
                #with dissolve
                # $ mc.quirks["boomer"] = True # Being re-evaluated
                $ add_point(KCT.TROUBLEMAKER)

                u "Who?"

                scene v15s1_3j # FPP. same as v15s1_3b Imre has a slightly disgusted look on his face, not angry, and rolls his eyes
                with dissolve

                imre "*Sighs* Nothing, you boomer..."

                scene v15s1_3i
                with dissolve

                u "*Chuckles* Alright."
            
    else:
        play music "music/v15/Track Scene 1_2.mp3" fadein 2
    
        scene v15s1_2a # FPP. same as v15s1_2 MC is sitting at his study desk, looking at his phone. Imre enters the room. MC turns to Imre, and stays sat in the chair, Imre has a concerned expression, is not angry, mouth open, looking at mc
        with dissolve

        imre "I need to talk to someone about Chris and Nora... This is like when Ross and Rachel broke up, dude!"

        scene v15s1_3i
        with dissolve

        u "Ross and Rachel?"

        scene v15s1_3h
        with dissolve

        imre "Yeah. You know, that show about the group of friends? They fall in love, out of love, and there's a monkey..."

        scene v15s1_3i
        with dissolve

        menu:
            "Of course I know":
                scene v15s1_3i
                #with dissolve
                # $ mc.quirks["pop_culture"] = True # Being re-evaluated
                $ add_point(KCT.BRO)

                u "*Laughs* Yeah, of course I know"

                scene v15s1_3k # FPP. same as v15s1_3h Imre is clutching his heart with one hand, holding his other fist above his head, head facing towards his fist, eyes closed, mouth is still open
                with dissolve

                imre "Ah, man... My heart is being torn all over again."

                scene v15s1_3i
                with dissolve

                u "I didn't know how important their relationship was to you... *Chuckles*"

                scene v15s1_3l # FPP. same as v15s1_3h Imre has no expression, mouth open, Imre has placed his hands to his sides
                with dissolve

                imre "*Sighs*"

            "A monkey?":
                scene v15s1_3i
                #with dissolve
                # $ mc.quirks["boomer"] = True # Being re-evaluated
                $ add_point(KCT.TROUBLEMAKER)

                u "A monkey? What? *Laughs*"

                scene v15s1_3h
                with dissolve

                imre "You're kidding, right? Man... Girls love that shit."

                imre "That's the only reason I watch it... So, I have something in common with girls, you know."

                scene v15s1_3i
                with dissolve

                u "*Chuckles* Right...Yeah, no. I guess I don't watch a lot of television."

                scene v15s1_3j
                with dissolve

                imre "*Sighs* Boomer..."

    scene v15s1_3l
    with dissolve

    imre "So, what are we going to do?"

    scene v15s1_3m # FPP. same as v15s1_3l Imre's mouth is closed
    with dissolve

    u "About what? Chris and Nora?"

    scene v15s1_3l
    with dissolve

    imre "Yeah. I mean, I know this whole break up is totally on Nora because she's been acting like a bitch, but..."

    if v13_imre_disloyal:
        jump v15s1_saynothing

    scene v15s1_3m
    with dissolve

    menu:
        "Stick up for Nora":
            $ add_point(KCT.BOYFRIEND)
            $ add_point(KCT.TROUBLEMAKER)

            u "Wait, this isn't all on Nora. Haha, what are you talking about?"

            scene v15s1_3a
            with dissolve

            imre "How is it not? Chris did nothing wrong. Not a single-"

            scene v15s1_3c
            with dissolve

            u "Yikes, man... You really gotta start paying more attention around here."

            scene v15s1_3b
            with dissolve

            imre "What the fuck is that supposed to mean? I pay plenty of attention."

            scene v15s1_3c
            with dissolve

            u "If that was true then you'd know that Nora has felt alone, worthless, and unappreciated for months leading up to the breakup."

            scene v15s1_3f
            with dissolve

            imre "Yeah, but she-"

            scene v15s1_3g
            with dissolve

            u "I don't care if she looks like a bitch or acts like one. She kind of has every right to."

            scene v15s1_3f
            with dissolve

            imre "How-"

            scene v15s1_3g
            with dissolve

            u "She's put up with Chris' bullshit for longer than either of us are even aware of."

            u "So, we have no room to judge, but I know damn well that all of this isn't just because of Nora."

        "Say nothing":
            $ v15_blame_nora = True
            $ add_point(KCT.BRO)

            label v15s1_saynothing:
            
            u "Yeah?"

            scene v15s1_3l
            with dissolve

            imre "I just don't like seeing Chris upset."

            scene v15s1_3m
            with dissolve

            u "It's none of our business, Imre."

            scene v15s1_3l
            with dissolve

            imre "But-"

            scene v15s1_3m
            with dissolve

            u "If we get involved, you can bet your ass that someone's going to end up getting angry at us for doing exactly that."

            u "I really think we should just let the two of them work it out on their own."

            scene v15s1_3n # FPP. same as v15s1_3b Imre has a concerned expression instead of angry
            with dissolve

            imre "Ah, man... but it feels weird! We should really be trying to help Chris get her back."

            scene v15s1_3m
            with dissolve

            u "I don't think there's any chance of that happening."

            scene v15s1_3h
            with dissolve

            imre "But there's always a chance, dude. Just like Ross and Rachel."

            # if mc.quirks["pop_culture"]: # Being re-evaluated
                # scene v15s1_3o
                # with dissolve

                # u "*Chuckles*"

            # elif mc.quirks["boomer"]: # Being re-evaluated
            scene v15s1_3o # FPP. same as v15s1_3m Imre has a smug looking expression mouth is still closed
            with dissolve

            u "*Sighs*"

            scene v15s1_3l
            with dissolve

            imre "If we don't do something, Nora's going to hook up with a random fuckboy and then that'll be the end of it forever."

            scene v15s1_3m
            with dissolve

            u "It's not our place to decide what happens here, Imre."

    scene v15s1_3p # FPP. same as v15s1_3l Imre looks away from MC
    with dissolve

    imre "..."

    scene v15s1_3q # FPP. same as v15s1_3p Imre looks in the other direction and now has a slightly annoyed expression
    with dissolve

    u "Imre..."

    scene v15s1_3l
    with dissolve

    imre "Okay, fine..."

    imre "I guess you're right. I just don't like it when things change around here, you know?"

    scene v15s1_3m
    with dissolve

    u "I know. You'll grow up one day. *Laughs*"

    scene v15s1_3h
    with dissolve

    imre "Eh, not likely. *Chuckles*"

    scene v15s1_3l
    with dissolve

    imre "I'm heading out then, thanks for the chat."

    scene v15s1_3m
    with dissolve

    u "Yeah, of course. You too, man."

    scene v15s1_2b # FPP. same as v15s1_2 Imre turns his back and is leaving mc's room
    with dissolve

    pause 0.75
    
    stop music fadeout 3
    
    play music "music/v15/Track Scene 1_3.mp3" fadein 2

    scene v15s1_4 # TPP. Mc stands up from his desk and takes off his shirt, no expression, mouth is closed
    with dissolve

    pause 0.75

    scene v15s1_4a # TPP. same as v15s1_4 MC takes off his pants and undresses down to his underpants
    with dissolve

    pause 0.75

    scene v15s1_5 # TPP. Mc gets into bed with a pillow propped up behind his back and head in a sitting position legs stretched out one leg bent, looking at his phone, concerned expression, mouth closed
    with dissolve

    pause 0.75

    scene v15s1_5a # TPP. same as v15s1_5 different camera angle, show mc holding his phone looking at it with one hand, and the other holding his forehead
    with dissolve

    u "*Sighs* (Where the hell is Nora?)"

    u "(Maybe she lost her phone? Or it ran out of battery?)"

    u "(Hopefully I can find out some more tomorrow...)"

    play sound "sounds/vibrate.mp3"

    scene v15s1_5c # TPP. same as v15s1_5a Mc quickly sit's up to look at his phone, slightly shocked expression, mouth open
    with dissolve

    u "(No way that's her...)"

# -MC checks his texts and there's a message from Autumn-

    if v14_date_distraction:
        $ chloe.messenger.newMessage("So, you wanna tell me why you didn't come?") 
        $ chloe.messenger.addReply("Hey, I understand if you're upset. I'm sorry. Something came up, an emergency, and I couldn't make it.") 
        $ chloe.messenger.newMessage("What do you mean you couldn't make it? You told me to meet you there! What happened that was so important, you had to stand me up at a fancy restaurant?!")
        $ chloe.messenger.addReply("Chloe, I'm sorry. I can't talk about it, but everything's fine. It's over now, I just don't wanna talk about it.") 
        $ chloe.messenger.newMessage("Ha. You're sorry... And you don't want to talk about it? Well, bye then.")
        $ chloe.messenger.addReply("Chloe please, don't be mad about this.") 
        $ chloe.messenger.newMessage("Okay, I'll just forget it happened. Is that fair?")
        $ chloe.messenger.addReply(_("Thank you."),v15s1_reply1)
        $ chloe.messenger.addReply(_("It's not fair, no."), v15s1_reply2)
        $ chloe.messenger.newMessage("Just... stop talking about it.")
        $ chloe.messenger.addReply("Okay. Done.") 

    $ autumn.messenger.newMessage("Hey! Just reminding you that I'll be setting up the shelter tomorrow if you wanted to swing by? :)", force_send=True)
    $ autumn.messenger.addReply("Uhm, sure.")
    $ autumn.messenger.addReply("Of course! I'll always be there if there's puppies, haha.")

    label v15s1_PhoneContinueChl:
        if chloe.messenger.replies:
            call screen phone
        if chloe.messenger.replies:
            u "(I should reply to Chloe.)"
            jump v15s1_PhoneContinueChl

    label v15s1_PhoneContinueAut:
        if autumn.messenger.replies:
            call screen phone
        if autumn.messenger.replies:
            u "(I should reply to Autumn.)"
            jump v15s1_PhoneContinueAut
            
    scene v15s1_5
    with dissolve

    u "(Almost forgot about that... It'll be interesting to spend one on one time with Autumn.)"

    u "(I'd better set an alarm so I'm not late.)"

    scene v15s1_5d # TPP. same as v15s1_5 Mc touchs the screen of his phone
    with dissolve

    u "(And done. Now, it's time for be-)"

    scene v15s1_5c
    with dissolve
    play sound "sounds/vibrate.mp3"
    u "(The hell?)"

# -MC checks his texts and there's a message from Lauren-
    $ lauren.messenger.newMessage("Hey gang! You're invited to Lauren's birthday party tomorrow night at the Deer's house! It's a Halloween theme of course, so make sure you dress to impress your ghoulish empress, haha! -Lauren")

    call screen phone

    scene v15s1_5e # TPP. same as v15s1_5a Mc has a slight smile, and a happy expression
    with dissolve

    u "(\"Dress to impress your ghoulish empress...\") *Chuckles*"

    u "(Guess I need to go gift shopping... Maybe Autumn can give me ideas on what Lauren would like?)"
    
    u "(Or I can just get her some kind of gift card... She likes books, I think?)"

    scene v15s1_5a
    with dissolve

    u "(Now it's really time for bed...)"

    scene v15s1_5f # TPP. same as v15s1_5b mc stretches and yawns
    with dissolve

    pause 0.75

    scene v15s1_5g # TPP. same as v15s1_5 MC has turned off the lights, his phone is now on the nightstand next to his bed, and has rested his head onto his pillow to go to sleep, eyes closed, mnouth closed
    with dissolve

    pause 0.75
    
    scene black
    with dissolve
    
    pause 2

    scene sleep_transition_fast
    with fade
    
    pause 2.2

    scene v15s1_6 # FPP. Show just a black screen (MC's POV, eyes closed). Phone alarm sounds
    with dissolve
    play sound "sounds/phonealarm.mp3"
    u "*Groans* (No time for snoozing today... Need to get up.)"

    stop sound

    stop music fadeout 3

    jump v15s4