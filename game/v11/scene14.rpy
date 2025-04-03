# SCENE 14: Nora and Chris beef
# Locations: on the plane
# Characters: MC (outfit 1), Nora (outfit 1), Chris (outfit 1), Ms Rose (outfit 1))
# Time: night time

label v11_nora_chris_plane:
    scene v11noch1 # TPP. MC sitting on his seat and Ryan sitting next to him, MC is looking forward, Ryan is looking through the window, both mouths closed, neutral expressions
    with fade
    play music music.v11_Track_Scene_14 fadein 2
    pause 0.75

    scene v11noch2 # TPP. Show Chris looking at Nora, he is slightly nervous, mouth open, tryign to reason with Nora (Nora is out of shot, sat next to him, he has the window seat)
    with dissolve

    ch "*Whisper* Nora please, we shouldn't be arguing in the first place, but this definitely isn't the right time."

    scene v11noch3 # TPP. Show Nora looking at Chris, she is angry, mouth open, arguing with Chris (Chris is now out of shot, sat next to her, he has the window seat)
    with dissolve

    no "It's never the right time with you."

    scene v11noch2
    with dissolve

    ch "*Whisper* Can you please lower your voice?"

    scene v11noch3
    with dissolve

    no "*Whisper* Oh I'm sorry, am I interrupting your frat plans?"

    scene v11noch2
    with dissolve

    ch "*Whisper* Nora please."

    scene v11noch3
    with dissolve

    no "Don't \"Nora please\" me, Chris. You didn't tell me you were gonna be glued to your phone so much that you'd have no time for anything I wanted to do with you. Not a single thing, Chris?"

    no "Really? I don't understand how you can't see how fucked up that is. I ask for just a few hours and you tell me no, but the frat asks for a lifetime and you're all in."

    scene v11noch2
    with dissolve

    ch "Why don't you listen to me when I explain things? During the trip, in the day time, I gotta be on the phone with Sebastian to make sure this event is set up."

    scene v11noch3
    with dissolve

    no "The entire fucking trip?"

    scene v11noch2
    with dissolve

    ch "I'll be free at night!"

    scene v11noch3
    with dissolve

    no "So basically you're free to fuck, but not to spend time with me."

    scene v11noch2
    with dissolve

    ch "Nora, you know it's not like that. You've been looking forward to this trip, let's not ruin it. C'mon on now, you can enjoy yourself without me."

    scene v11noch3
    with dissolve

    no "You're right, I can."

    scene v11noch2
    with dissolve

    ch "Nora..."

    scene v11noch3
    with dissolve

    no "Just drop it."

    scene v11noch1
    with dissolve

    u "(Oh shit.)"

    scene v11noch2
    with dissolve

    ch "I'm trying to make this work, why can't we just-"

    scene v11noch4 # TPP. Ms Rose is standing in the plane corridor, looking towards the back of the plane, she is smiling, mouth open
    with dissolve

    ro "Alright everyone, wake up and yawn to pop your ears."

    scene v11noch5 # TPP. Show Imre sitting in his seat, he is slightly surprised, mouth open
    with dissolve

    imre "*Yawn* Oh shit, that actually works."

    scene v11noch4
    with dissolve

    ro "We're getting ready to deboard, you all need to make sure you collect your things and pick up any trash."

    ro "It's about 3 am local time, so let's make sure we get to the hotel as quickly as possible so we can all get to bed."

    scene v11noch6 # TPP. Nora is standing up from her seat, Chris is midway through standing up (Nora is angry, mouth closed, Chris is slightly annoyed, mouth closed)
    with dissolve

    pause 0.75

    scene v11noch6a # TPP. Same cam as v11noch6, Nora is now standing up in the corridor, opening the overhead bin, Chris is now standing up, mouth open
    with dissolve

    ch "Look Nora, just hear me out."

    scene v11noch6b # TPP. Same cam as v11noch6, Nora now has her luggage on hand, she is moving towards the exit of the plane, mouth closed, angry, Chris is looking at her, slightly sad, mouth closed
    with dissolve

    pause 0.75

    scene v11noch6c # TPP. Same cam as v11noch6, Nora is now out of shot, Chris is looking the same direction, slightly sad, mouth closed
    with dissolve

    ch "*Sighs*"

    scene v11noch7 # TPP. MC is standing with his luggage in the plane corridor, he is looking towards the exit of the plane, mouth closed, slightly worried look
    with dissolve
    stop music fadeout 3
    menu:
        "Chase after Nora":
            $ v11_check_on_nora = True
            scene v11noch7a # TPP. Same cam as v11noch7, but MC is now walking towards the plane exit, neutral expression, mouth closed
            with dissolve

            u "(I'll see if she's okay.)"

            scene v11noch8 # TPP. Show MC walking through the plane exit, he has mouth closed, worried expression
            with dissolve

            pause 0.75

            jump v11_nora_airport_convo

        "Leave her alone":
            scene v11noch7a
            with dissolve

            u "(I'll give her some space.)"

            scene v11noch8a # TPP. Same as v11noch8, but MC has neutral expression, mouth still closed
            with dissolve

            pause 0.75

            jump v11_lauren_airport_convo