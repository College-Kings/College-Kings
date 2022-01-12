# SCENE 20: Chloe Brief
# Locations: Library
# Characters: CHLOE (Outfit: 3), MC (Outfit: 9)
# Time: Morning

label v15s20:
    play music "music/v13/Track Scene 18.mp3" fadein 2

    scene v15s20_1 # TPP. Show MC walking into the Libray, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s20_2 # TPP. MC looking over at Chloe who is sitting down at a table in the library, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s20_3 # FPP. MC standing over by the table, MC looking at Chloe, Chloe looking at MC, Chloe slight smile, mouth open.
    with dissolve

    cl "Hey, [name]. Come take a seat. Let's get started."

    scene v15s20_3a # FPP. Same as v15s20_3, Chloe slight smile, mouth closed.
    with dissolve

    u "Oh, okay, haha."

    scene v15s20_4 # TPP. Show MC taking a seat next to Chloe, Both slight smile, mouth closed.
    with dissolve

    pause 0.75

    if chloe.relationship >= Relationship.GIRLFRIEND:
        menu:
            "Ask for a kiss":
                $ add_point(KCT.BOYFRIEND)
                
                scene v15s20_5 # FPP. MC sitting next to Chloe. Chloe looking at MC, MC looking at Chloe, Chloe slight smile, mouth closed.
                with dissolve

                u "I know you're super busy, but can your boyfriend get a kiss first? *Chuckles*"

                scene v15s20_5a # FPP. Same as v15s20_5, Chloe slight smile, mouth open.
                with dissolve

                cl "Of course, haha. Sorry! My mind is just like, completely focused on this meeting with the Dean."

                play sound "sounds/kiss.mp3"

                scene v15s20_6 # TPP. Show MC and Chloe having a quick kiss.
                with dissolve

                pause 0.75

            "Say nothing":
                scene v15s20_5 # FPP. MC sitting next to Chloe. Chloe looking at MC, MC looking at Chloe, Chloe slight smile, mouth closed.
                with dissolve
                
                u "(I was expecting a hello kiss, but I'll keep quiet about it... I don't want to throw her off her game.)"

    if v15_chloe_mrleesupport: # Placeholder if MC chose to meet with Mr. Lee.
        scene v15s20_5a
        with dissolve

        cl "So, I've booked a meeting room and we'll head there when Mr. Lee arrives."

        scene v15s20_5
        with dissolve

        u "Nice, good idea."

        scene v15s20_5a
        with dissolve

        cl "Thanks, so here's my game plan so far... I've written down some notes."

        show screen v15_teacher_brief_icon("mr_lee")
        # -The UI pops up showing Mr. Lee's character brief-

        cl "We already have a good idea what Mr. Lee is all about. He likes professionalism and manners."

        cl "He's very detail-orientated and likes to talk about his philosophy on life..."

        scene v15s20_5
        with dissolve

        u "Yeah, that's him alright, haha. You could say he has a strong moral code."

        scene v15s20_5a
        with dissolve

        cl "Exactly, right. So, what he hates are things like lying and cheating. Not being honest with Mr. Lee will always backfire..."

        scene v15s20_5
        with dissolve

        u "(She says that like she knows from experience...)"

        scene v15s20_5a
        with dissolve

        cl "He's going to want to hear our true motives behind getting reduced tuition for all the Chicks."

        cl "And it must make sense for the college too, that's huge. So, we'll need to explain how the Chicks benefit SVC."

        scene v15s20_5
        with dissolve

        u "Okay, noted..."

        scene v15s20_5a
        with dissolve

        cl "We just need to be sure that we don't say anything to annoy him or piss him off."

        cl "Make sure we present only the best points of our proposal, no wasting time."

        scene v15s20_5
        with dissolve

        u "Yeah, and if we fail, we can just lock him in the meeting room until he agrees. *Laughs*"

        scene v15s20_5a
        with dissolve

        cl "Haha, shh! Come on, we need to focus."

    else: # if MsRoseMeeting:
        scene v15s20_5a
        with dissolve

        cl "When Ms. Rose arrives, we can head over to the meeting room I booked."

        scene v15s20_5
        with dissolve

        u "Sounds good."

        scene v15s20_5a
        with dissolve

        cl "I've also written down some notes for the meeting."

        show screen v15_teacher_brief_icon("ms_rose")
        # -The UI pops up showing Ms. Rose's character brief-

        cl "Basically, Ms. Rose is all about the girls. She loves to support other women, to help them reach their goals, etc..."

        cl "So personally, I think she'll like the idea of reduced tuition for all Chicks."

        cl "She's big into women being independent and the Chicks being a positive influence."
        cl "So I think she'll like that I'm being ambitious for the good of everyone here."

        scene v15s20_5
        with dissolve

        u "Sounds like a win-win to me. This might be easier than we think."

        scene v15s20_5a
        with dissolve

        cl "Also, I know she's hung out with the Dean outside of campus."

        cl "So as a close friend of the Dean, gaining Ms. Rose's signature should give us a huge chance of success."

        scene v15s20_5
        with dissolve

        u "Well, this is great. So, where do you think we could go wrong?"

        scene v15s20_5b # FPP. Same as v15s20_5a, Chloe sad face, mouth open.
        with dissolve

        cl "*Sighs* I just hope my issues with Nora don't work against us here..."

        scene v15s20_5c # FPP. Same as v15s20_5b, Chloe sad face, mouth closed.
        with dissolve

        u "You think they would?"

        scene v15s20_5b
        with dissolve

        cl "I can see Ms. Rose bringing her up in the conversation, because she's a Chick, and her stepdaughter..."

        cl "But I'd like to make sure we avoid that. This isn't about Nora. So, whatever you do, don't mention her."

        scene v15s20_5
        with dissolve

        u "Okay, I think I can handle that."

        scene v15s20_5a
        with dissolve

        cl "Also, something that Ms. Rose doesn't like is selfishness. I think that's been obvious since her split from Mr. Rose."

        cl "She hates the idea of men being large and in charge when it comes to her occupation..."

        if "v15_rose" in sceneList:
            scene v15s20_5
            with dissolve

            u "(Well, she loves it in the bedroom... Or should I say kitchen...)"

            if chloe.relationship >= Relationship.GIRLFRIEND:
                scene v15s20_5d # FPP. Same as v15s20_5c, Chloe confused, mouth open.
                with dissolve

                cl "Are you blushing? *Chuckles* What's happening?"

                scene v15s20_5e # FPP. Same as v15s20_5d, Chloe confused, mouth closed
                with dissolve

                u "What? Haha, no, sorry. Go on..."

        scene v15s20_5a
        with dissolve

        cl "Just tread carefully and make sure you don't interrupt either of us or sound like you're mansplaining anything, haha."

        scene v15s20_5
        with dissolve

        u "I've never mansplained anything in my life... ever."

        scene v15s20_5a
        with dissolve

        cl "*Laughs* Right..."

        scene v15s20_5
        with dissolve

        u "What is that supposed to mean?! *Chuckles*"

        scene v15s20_5a
        with dissolve

        cl "Shh... She'll be here any minute. We have to focus, haha."

    scene v15s20_5
    with dissolve

    u "*Sighs*"

    scene v15s20_5a
    with dissolve

    cl "Do you think we should take this cheat sheet with us? Or would that ruin everything?"

    if v15_chloe_mrleesupport:
        show screen v15_teacher_brief("mr_lee")
    else:
        show screen v15_teacher_brief("ms_rose")

    menu:
        "Take the notes":
            $ add_point(KCT.TROUBLEMAKER)
            $ v15_took_notes = True

            scene v15s20_5
            with dissolve

            u "Yeah, we better take them. As long as we aren't staring at it the whole time, I think it's helpful to refer to."

            scene v15s20_5a
            with dissolve

            cl "Just don't look at it too much, it might seem like you're not paying attention."

            scene v15s20_5
            with dissolve

            u "Got it."

        "Don't take the notes":
            $ add_point(KCT.BOYFRIEND)
            
            hide screen v15_teacher_brief_icon

            scene v15s20_5
            with dissolve

            u "Nah, I don't want to risk pissing anyone off. Besides, I remember it all anyway. You can put them away."

            scene v15s20_5a
            with dissolve

            cl "Haha, okay Mr. Confident. I trust you."

    stop music fadeout 3

    jump v15s21