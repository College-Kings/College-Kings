# SCENE 26a: MC gets a rideshare with Chris
# Locations: Hotel Exterior, Road, Hospital
# Characters: CHRIS (Outfit: 1), MC (Outfit: 3), DRIVER (Outfit: 1)
# Time: Morning
# Phone Images: None

label v12_follow_chris:
    scene v12chf1 # TPP. Show Chris leaving the hotel, MC going after him, MC worried, mouth closed, Chris angry, mouth open, holding the wrist of the hand he used to punch
    with dissolve

    ch "Shit! Fuck!"

    play music "music/v12/Track Scene 26a_1.mp3" fadein 2

    scene v12chf2 # FPP. MC and Chris now outside the hotel, Chris looking at MC, Chris angry, holding his wrist, mouth open
    with dissolve

    ch "I'm such a fucking idiot!"

    scene v12chf2a # FPP. Same as v12chf2, Chris mouth closed, angry
    with dissolve

    u "Chris, what the hell is going on with you right now?"

    scene v12chf2
    with dissolve

    ch "What do you mean what's going on?! Did you not just see what I fucking did?! I just pulled the last straw with that one. She's not forgiving me after something like that."

    scene v12chf2b # FPP. Same as v12chf2, Chris pacing to the right, mouth open, angry, not looking at MC
    with dissolve

    ch "And I fucked up my wrist! MY FUCKING LIFE! It's so fucking stupid!"

    scene v12chf2a
    with dissolve

    u "Calm the fuck down, would you?"

    scene v12chf2c # FPP. Same as v12chf2, Chris pacing to the left, mouth closed, angry, not looking at MC
    with dissolve

    u "You guys caused a big enough scene already. Let's get you to the hospital to get your wrist checked out."

    scene v12chf2d # FPP. Same as v12chf2, Chris worried, mouth open
    with dissolve

    ch "*Sighs* I already called a rideshare. There it is right there."

    scene v12chf2e # FPP. Same as v12chf2d, Chris worried, mouth closed
    with dissolve

    u "Good, I'm coming with you."

    scene v12chf3 # TPP. Show MC and Chris getting into the back of the car, both worried, mouths closed
    with dissolve

    pause 1.25

    scene v12chf4 # FPP. MC and Chris sitting in the back of the car, MC looking at Chris, Chris looking out the window, very worried, mouth open
    with dissolve

    ch "This is it man, I really messed it up this time. I shouldn't have let it escalate that far..."

    scene v12chf4a # FPP. Same as v12chf4, Chris looking at MC, Chris very worried, mouth closed
    with dissolve

    u "Not gonna lie man, that was a really bad look. I almost felt the need to step in."

    scene v12chf4b # FPP. Same as v12chf4a, Chris very worried, mouth open
    with dissolve

    ch "She just... *Sighs*"

    scene v12chf4a
    with dissolve

    u "What caused you to explode like that? You fucking pushed her, Chris..."

    scene v12chf4b
    with dissolve

    ch "It's... *Sighs*"

    scene v12chf4
    with dissolve

    ch "It's what she said..."

    scene v12chf4a
    with dissolve

    u "I mean, she said a lot. What exactly did she say that got to you?"

    scene v12chf4c # FPP. Same as v12chf4b, Chris tears in his eyes, very worried, mouth open
    with dissolve

    ch "She brought up my dad, man."

    scene v12chf4d # FPP. Same as v12chf4c, Chris very worried, mouth closed
    with dissolve

    u "What about it bothered you so much?"

    scene v12chf4c
    with dissolve

    ch "It's personal, [name], but she knows."

    scene v12chf4
    with dissolve

    ch "And she was willing to put that out in the air knowing how It'd make me feel. She obviously doesn't give a fuck about how I feel, or at least she didn't five minutes ago."

    scene v12chf4a
    with dissolve

    u "Sounds to me like she was treating you, how she felt you were treating her. As a matter of fact, I'm pretty sure that's exactly what's happening."

    scene v12chf4b
    with dissolve

    ch "*Sighs* And? I feel like that all the time, but you don't see me overreacting the way she does, do you?"

    scene v12chf4a
    with dissolve

    menu:
        "She wasn't overreacting":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            $ CharacterService.set_mood(chris, Moods.MAD)

            scene v12chf4a
            with dissolve

            u "I don't think that was an overreaction, man..."

            scene v12chf4b
            with dissolve

            ch "What's that supposed to mean?"

            scene v12chf4e # FPP. Same as v12chf4a, Chris slightly annoyed, mouth closed
            with dissolve

            u "Nora had a really good point. Everyone on this trip knows that she's been begging you to spend some time with her."

            scene v12chf4f # FPP. Same as v12chf4e, different pose
            with dissolve

            u "Sounds like you finally had some free time and chose the guys over her. Seems pretty fucked up considering that you've been so busy lately, which has caused you to miss out on a lot."

            scene v12chf4e
            with dissolve

            u "I mean, genuinely, Chris? You literally left her at the altar the other day. *Chuckles*"

            scene v12chf4f
            with dissolve

            u "It may not have been real, but still... I think everyone felt a little awkward about what you did."

            scene v12chf4g # FPP. Same as v12chf4f, Chris slightly annoyed, mouth open
            with dissolve

            ch "So because I'm doing everything I can to give us an amazing future, I'm the bad guy? You gotta be kidding me..."

            scene v12chf4h # FPP. Same as v12chf4, Chris leaning forward, looking at the driver, Chris slightly annoyed, mouth open
            with dissolve

            ch "Are we almost there?"

            scene v12chf4i # FPP. Same as v12chf4h, Chris slightly annoyed, mouth closed
            with dissolve

            driver "Pulling up now, sir."

            scene v12chf4h
            with dissolve

            ch "Good."

            scene v12chf4e
            with dissolve

            u "Chris, I know you want everyone to see it from your perspective, but maybe for a second you need to try to see it from hers."

            scene v12chf4g
            with dissolve

            ch "Bro, I'm seriously done talking about this. You're just pissing me off even more."

            scene v12chf5 # TPP. Show the car pulling up at the hospital
            with dissolve

            pause 0.75

            scene v12chf4j # FPP. Same as v12chf4g, car pulled up at the hospital, Chris slightly annoyed, mouth closed
            with dissolve

            ch "You don't need to follow me. I insist."

            scene v12chf4k # FPP. Show Chris leaving the car
            with dissolve

            u "*Sighs*"

            scene v12chf6 # TPP. Show the driver, driver looking at the rearview, neutral expression, mouth open (Chris not in the car, only MC), MC worried, mouth closed
            with dissolve

            driver "Don't worry, I can take you back."

        "You're right":
            $ v12_help_chris += 1
            if v12_help_chris >= 4:
                if mc.frat == Frat.WOLVES:
                    $ grant_achievement("brotherhood_of_men")
                else:
                    $ grant_achievement("best_frenemies")
            
            $ reputation.add_point(RepComponent.BRO)
            scene v12chf4l # FPP. Same as v12chf4a, different pose
            with dissolve

            u "You're right, Chris. She took it too far but... I don't know what you can do to get her or anyone else to understand."

            scene v12chf4a
            with dissolve

            u "I wouldn't just give up on the situation yet, though. If I were you, I mean..."

            scene v12chf4l
            with dissolve

            u "Sure, you just gave yourself a pretty serious setback. That doesn't mean it's completely over. There's always more you can do."

            scene v12chf4b
            with dissolve

            ch "I'm glad I have you man, I feel like I've been alone with this whole situation. That's why I wanted to go out with the guys..."
            ch "I was hoping I could get some advice with the whole Nora situation, but obviously it doesn't even matter anymore."

            scene v12chf4a
            with dissolve

            u "How'd she find out you were going out with guys?"

            scene v12chf4b
            with dissolve

            ch "Well, I told her."

            scene v12chf4l
            with dissolve

            driver "*Whisper* Idiot."

            scene v12chf4b
            with dissolve

            ch "Did he just...?"

            scene v12chf4a
            with dissolve

            u "Not gonna lie, you should've known she'd get mad at you for hanging with someone other than her. Especially when she's been asking to hang out since the beginning."

            scene v12chf4
            with dissolve

            ch "Yeah, I know. I honestly didn't think about it. Since I was planning to do something for us it just didn't cross my mind."

            scene v12chf4l
            with dissolve

            u "Yeah man, I get it."

            scene v12chf5
            with dissolve

            pause 0.75

            scene v12chf6a # TPP. Same as v12chf6, Chris in the car, Chris and MC worried, mouths closed, Driver neutral expression, mouth open
            with dissolve

            driver "We are here."

            scene v12chf6b # TPP. Same as v12chf6a, MC mouth open, worried, Chris worried, mouth closed, driver neutral expression, mouth closed
            with dissolve

            u "Thank you. Hey, mind waiting for me?"

            scene v12chf6a
            with dissolve

            driver "Don't be long."

            scene v12chf7 # TPP. Show Chris and MC leaving the car in front of the hotel, both worried, mouths closed
            with dissolve

            pause 1.25

            scene v12chf8 # TPP. Show Chris and MC walking into the hotel, both worried, mouths closed
            with dissolve

            pause 1.25

            scene v12chf9 # TPP. Show Chris filling in a form, MC sitting down, both worried, mouths closed
            with dissolve

            pause 1.25

            stop music fadeout 3
            play music "music/v12/Track Scene 26a_2.mp3" fadein 2

            scene v12chf10 # FPP. Chris and MC now sitting in the waiting room, Chris worried, mouth open, looking at MC, MC looking at Chris
            with dissolve

            ch "*Sighs*"

            scene v12chf10a # FPP. Same as v12chf10, Chris worried, mouth closed
            with dissolve

            u "How's it feeling?"

            scene v12chf10b # FPP. Same as v12chf10, Chris slight smile, mouth open
            with dissolve

            ch "Hurts pretty fucking bad... I'm sure it's just a sprain, been in enough fights to know what a sprained wrist feels like. *Chuckles*"

            scene v12chf10c # FPP. Same as v12chf10b, Chris slight smile, mouth closed
            with dissolve

            u "*Chuckles* I'm sure you have. I don't think I've ever seen you that mad before. Think I may have seen a flash of Grayson in you for a minute."

            scene v12chf10
            with dissolve

            ch "I don't like getting mad like that, but I'd be lying if I said I didn't have my moments."

            scene v12chf10a
            with dissolve

            u "We all have our downfalls, no one's perfect."

            scene v12chf10d # FPP. Same as v12chf10, Chris looking towards the door, slight smile, mouth closed
            with dissolve

            nurse "Chris?"

            scene v12chf10b
            with dissolve

            ch "Hey man, thanks for the support. I'll see you back at the hotel."

            scene v12chf10c
            with dissolve

            u "Alright, sounds good. Call if you need me."

            scene v12chf11 # TPP. Show Chris walking towards the doctor's office, slight smile, mouth closed, MC walking towards the door, worried, mouth closed
            with dissolve

            pause 0.75

            scene v12chf7a # TPP. Same as v12chf7, only MC, MC getting into the car
            with dissolve

            pause 0.75

    scene v12chf12 # TPP. Show the car on the road
    with dissolve

    pause 0.75

    scene v12chf13 # TPP. Show MC leaving the car, car in front of the hotel lobby, MC worried, mouth closed
    with dissolve

    pause 0.75

    scene v12chf14 # TPP. Show MC walking towards the hotel entrance, mouth closed, worried
    with dissolve

    pause 0.75

    stop music fadeout 3

    if mc.frat == Frat.WOLVES:
        jump v12s27 #scene 27
    else:
        jump v12s27a #scene 27a