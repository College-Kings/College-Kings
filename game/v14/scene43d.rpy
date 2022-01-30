# SCENE 43d: Working with Riley
# Locations: Empty Classroom
# Characters: RILEY (Outfit: 4), MC (Outfit: 1)
# Time: Morning

label v14s43d:
# -MC and Riley are sitting across from each other in the empty classroom-
    scene v14s43d_1 # TPP. Show MC and Riley sitting across from each other in the class room.
    with dissolve

    pause 0.75

    play music "music/v13/Track Scene 8.mp3" fadein 2

    scene v14s43d_2 # FPP. MC and Riley sitting across from each other. MC looking at Riley, Riley looking at MC, Riley slight smile, mouth open.
    with dissolve

    ri "Thank you for pairing with me by the way."

    scene v14s43d_2a # FPP. Same as v14s43d_2, Riley slight smile, mouth closed.
    with dissolve

    u "Oh, of course."

    scene v14s43d_2
    with dissolve

    ri "I saw Imre floating around the room and I thought I was gonna have to be with him for a second, but thankfully... You came to the rescue. *Laughs*"

    scene v14s43d_2a
    with dissolve

    u "Haha, it's no problem. He actually told me what he did and begged me to work with you so that it wasn't awkward for either of you."

    scene v14s43d_2
    with dissolve

    ri "Ah, I see. Did he go into detail at all? About what he did?"

    scene v14s43d_2a
    with dissolve

    u "No, he just said that he was drunk texting you last night and you never responded."

    scene v14s43d_2
    with dissolve

    ri "Well, I hope he was drunk... 'cause that was some harsh shit, ha."

    scene v14s43d_2a
    with dissolve

    u "*Sighs* Do I wanna know?"

    scene v14s43d_2
    with dissolve

    ri "You don't."

    scene v14s43d_2a
    with dissolve

    u "*Laughs*"

    scene v14s43d_2
    with dissolve

    ri "Let's get started on this before I get bored. I don't plan on being here long."

    if riley.relationship >= Relationship.FWB:
        scene v14s43d_2b # FPP. Same as v14s43d_2a, Riley flirtatious smile, mouth closed
        with dissolve

        u "No problem. Really though, you okay?"

        scene v14s43d_2c # FPP. Same as v14s43d_2b, Riley Flirtation smile, mouth open.
        with dissolve

        ri "Yeah, ha. I am now... Yeah."

    scene v14s43d_2a
    with dissolve

    u "Alright, well... What ideas did you have for the scene?"

    scene v14s43d_2
    with dissolve

    ri "None, really. I just know one thing I wanna do."

    scene v14s43d_2a
    with dissolve

    u "And that is?"

    scene v14s43d_2
    with dissolve

    ri "*Clears throat* Drumroll please!"

    scene v14s43d_2a
    with dissolve

    u "..."

    scene v14s43d_2
    with dissolve

    ri "Please?"

    scene v14s43d_2a
    with dissolve

    u "C'mon already, weirdo. I thought you didn't wanna be here long? *Chuckles*"

    scene v14s43d_2
    with dissolve

    ri "*Sighs* You're no fun..."

    ri "The one thing I really wanna do is improv."

    scene v14s43d_2a
    with dissolve

    u "You mean you wanna wing it? *Chuckles* Be lazy and come up with nothing?"

    scene v14s43d_2
    with dissolve

    ri "Well... We can come up with a premise."

    scene v14s43d_2a
    with dissolve

    u "Explain..."

    scene v14s43d_2d # FPP. Same as v14s43_2c, Riley new pose, slight smile, mouth open.
    with dissolve

    ri "First off, I'm the queen. So obviously, I expect to be treated like one."

    scene v14s43d_2e # FPP. Same as v14s43_2d, in the same pose from last scene, Riley slight smile, mouth closed.
    with dissolve

    u "Ha, okay. And how is that?"

    if riley.relationship >= Relationship.FWB:
        scene v14s43d_2f # FPP. Same as v14s43_2e,in the same pose from last scene, Riley flirtatious smile, mouth open.
        with dissolve

        ri "Well, the King thinks that above all, the Queen should always be treated."

        scene v14s43d_2g # FPP. Same as v14s43_2, in the same pose from last scene, Riley flirtatious smile, mouth closed.
        with dissolve

        u "*Gulp* Always?"

        scene v14s43d_2f
        with dissolve

        ri "*Laughs* Yeah, always."

        scene v14s43d_2h # FPP. Same as v14s43_2g, Riley leaning in slightly towards the MC across the table, Riley Flirtatious smile, mouth open.
        with dissolve

        ri "*Whispers* And he loves treating her just as much as she loves being treated..."

        scene v14s43d_2g
        with dissolve

        u "Hmm... Okay, I think I understand. (This scene is gonna be hot as fuck...)"

        scene v14s43d_2f
        with dissolve

        ri "*Chuckles*"

    else:
        scene v14s43d_2
        with dissolve

        ri "I don't need to explain myself to you! King or not, you will do as the Queen demands. And that's final."

        scene v14s43d_2a
        with dissolve

        u "Oh, shit... How the hell am I supposed to compete with an A-list actress?"

        scene v14s43d_2
        with dissolve

        ri "*Laughs*"

    scene v14s43d_2
    with dissolve

    ri "I really wanna make the whole class squirm, and Mr. Lee too for hitting me with that bomb today."

    scene v14s43d_2a
    with dissolve

    u "Ha, okay. How are you planning to do that?"

    scene v14s43d_2
    with dissolve

    ri "You couldn't tell? Obviously I wanna do a little sub/dom action."

    menu:
        "I'm dominant": # ;)
            $ add_point(KCT.BRO)

            scene v14s43d_2b
            with dissolve

            u "Well if that's the case, I'm the dominant."

            scene v14s43d_2
            with dissolve

            ri "Oh... You like taking control, huh?"

        "I'm submissive": # ;O 
            $ add_point(KCT.BOYFRIEND)

            scene v14s43d_2b
            with dissolve
            
            u "If that's the case, I'll play the submissive."

            scene v14s43d_2
            with dissolve

            ri "You like being told what to do, huh?"

            scene v14s43d_2b
            with dissolve

            u "Haha. Umm..."

    if "v14_threesome" in sceneList:
        u "You already know the answer to that question, I think."

        scene v14s43d_3 # TPP. Show MC winking at Riley, Both slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v14s43d_2i # FPP. Same as v14s43_2b, Riley looking at MC, super flirtatious smile, mouth open.
        with dissolve

        ri "Haha, that I do..."

    scene v14s43d_2
    with dissolve

    ri "Okay, nevermind. Focus!"

    scene v14s43d_2a
    with dissolve

    u "Yes, my Queen."

    scene v14s43d_2
    with dissolve

    ri "Good start."

    ri "Also, we'll have to include at least something about history so that we don't mess it up by giving Mr. Lee the chance to interrupt."

    scene v14s43d_2a
    with dissolve

    u "*Laughs* Fair enough."

    scene v14s43d_2
    with dissolve

    ri "Alright, so... We're good for next week then?"

    scene v14s43d_2a
    with dissolve

    u "Haha, yep. We're all good."

    scene v14s43d_2
    with dissolve

    ri "Great, I gotta go chat with Aubrey. Catch you later?"

    if "v14_threesome" in sceneList:
        scene v14s43d_2g
        with dissolve

        u "Don't have too much fun without me. *Chuckles*"

        scene v14s43d_2j # FPP. Same as v14s43d_2f, Riley blushing, Riley flirtatious smile, mouth open.
        with dissolve

        ri "No promises, hehe."

        scene v14s43d_2g
        with dissolve

        u "*Laughs* (She can't get enough of her Aubs, can she?)"

        scene v14s43d_2a
        with dissolve

        u "Later!"

    else:
        scene v14s43d_2a
        with dissolve
        
        u "Yeah, later."

    scene v14s43d_4 # TPP. Show Riley walking out of the classroom, slight smile, mouth closed.
    with dissolve

    u "(Should've known she'd choose to do the whole thing on a whim...)"
    u "(As long as I get a passing grade, she can have as much fun as she wants with the class, haha.)"

    scene v14s43d_5 # TPP. Show MC walking outside of the Campus building, slight smile, mouth closed
    with fade

    pause 0.75

    scene v14s43d_6 # TPP. MC walking down the sidewalk of campus
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v14s44