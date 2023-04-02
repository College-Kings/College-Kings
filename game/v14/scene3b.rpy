# SCENE 03b: Brothel
# Locations: Brothel
# Characters: IMRE (Outfit: 1), MC (Outfit: 3), RYAN (Outfit: 1), EMERALD (Outfit: x)
# Time: Sunday

label v14s03b:
    play music "music/v13/Track Scene 11_1.mp3" fadein 2

    scene v14s03b_1 # TPP Show MC, Imre, and Ryan coming in the brothel door, Imre pointing and looking toward the girls, mouth open
    with dissolve

    imre "Woah... Look at those jugs..."

    scene v14s03b_2 # FPP Switch to MC's view, Imre pointing at the girls and looking at MC, mouth closed
    with dissolve

    u "*Whispers* Damn dude!"

    scene v14s03b_2a # FPP Same angle as 2, Imre no longer pointing, looking at MC and Ryan, smiling with mouth open
    with dissolve

    imre "*Laughs* Catch you guys later."

    scene v14s03b_3 # FPP Imre walking off toward the waiting girls
    with dissolve

    u "Wait, Imre... Aren't you-"

    scene v14s03b_3a # FPP Same angle as 3, Imre farther away, almost to girls, ignoring MC and Ryan
    with dissolve

    u "Nevermind."

    scene v14s03b_4 # FPP Show Ryan, looking at MC. Ryan has an awkward, embarrased expression, mouth open
    with dissolve

    ry "[name]."

    scene v14s03b_4a # FPP Same as 4, Ryan's mouth closed
    with dissolve

    u "Yeah?"

    scene v14s03b_4b # FPP Same angle as 4, Ryan looking around with his eyes, embarassed, mouth open
    with dissolve

    ry "*Whispers* Come here, get closer."

    scene v14s03b_5 # FPP MC closer to Ryan, Ryan still looking around, mouth closed
    with dissolve

    u "Why are you acting so weird?"

    scene v14s03b_5a # FPP Same as 5, Ryan's mouth open
    with dissolve

    ry "What is this place?"

    scene v14s03b_5
    with dissolve

    u "Are you being serious...?"

    scene v14s03b_5b # FPP Same angle as 5, Ryan is looking at MC, he looks confused and embarrased, mouth open
    with dissolve

    ry "All I know is that I have a boner watching naked women walk around this room."
    ry "But I have no idea what kind of place this is or what we're supposed to do here."

    scene v14s03b_5a
    with dissolve

    ry "Is it some type of... hotel?"

    scene v14s03b_5
    with dissolve

    u "*Chuckles* Yeah, kinda. A hotel for three minutes to an hour, depending on the type of man you are."

    scene v14s03b_5b
    with dissolve

    ry "Huh?"

    scene v14s03b_5
    with dissolve

    u "Bro, it's a brothel. You thought we'd come to the Red Light District without stopping here? Imre wouldn't miss out on a chance like this. *Laughs*"

    scene v14s03b_5a
    with dissolve

    ry "Is a brothel one of those old western places where you pay the girls to have sex? Kinda like a prostitute?"

    scene v14s03b_5
    with dissolve

    u "Yeah... I'm kinda shocked at how vanilla you are when it comes to all of this. *Chuckles*"

    scene v14s03b_5b
    with dissolve

    ry "Well, my name's Ryan. Not Imre."

    scene v14s03b_5
    with dissolve

    u "Well, are you gonna go get with a girl?"

    scene v14s03b_5a
    with dissolve

    ry "I don't know if I should."

    scene v14s03b_5
    with dissolve

    u "Because...?"

    scene v14s03b_5b
    with dissolve

    ry "Promise you won't tell anyone?"

    scene v14s03b_5c # FPP Same angle as 5, Ryan looking at MC, looking embarrassed, mouth closed
    with dissolve

    u "Okay... I promise."

    scene v14s03b_5b
    with dissolve

    ry "*Sighs* I'm a virgin."

    scene v14s03b_5c
    with dissolve

    menu:

        "Take him seriously":
            
            $ reputation.add_point(RepComponent.BRO)

            u "Oh shit."

        "Take it as a joke":

            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            u "*Laughs*"

            scene v14s03b_5d # FPP Same angle as 5, Ryan looking at MC, looking angry, mouth open
            with dissolve

            ry "*Whispers* Don't laugh!"

            scene v14s03b_5e # FPP Same as 5d, Ryan's mouth closed
            with dissolve

            u "Oh, you're being serious?"

            scene v14s03b_5d
            with dissolve

            ry "Yeah, I am... dickhead."

            scene v14s03b_5e
            with dissolve

            u "Oh damn..."

    # -If blessed with Emily (extra dialog)
    # I HAVE NO IDEA WHAT VARIABLE THIS IS ASKING FOR

    if v10s33_ryan_flirt_emily:
        scene v14s03b_5a
        with dissolve

        ry "Plus, things aren't going anywhere with Emily, so..."

    # -Regardless of everything scene continued

    scene v14s03b_5b
    with dissolve

    ry "Look, I guess I'm just... I'm a little nervous."

    scene v14s03b_5
    with dissolve

    u "Nervous about what?"

    scene v14s03b_5d
    with dissolve

    ry "*Whispers* Sex!"

    scene v14s03b_5a
    with dissolve

    ry "What if I'm sleeping with a girl and she doesn't like what I'm doing?"

    scene v14s03b_5b
    with dissolve

    ry "Having zero experience when having sex with a girl for the first time doesn't sound fun."

    scene v14s03b_5c
    with dissolve

    u "I mean, I feel where you're coming from. Everyone feels like that at first I think."

    scene v14s03b_5a
    with dissolve

    ry "Hmm..."

    scene v14s03b_5
    with dissolve

    u "What are you thinking about?"

    scene v14s03b_5f # FPP Same angle as 5, Ryan looking at MC, smiling with mouth open
    with dissolve

    ry "I'm wondering. Should I get some experience while we're here?"

    scene v14s03b_5g # FPP Same as 5f, Ryan's mouth closed
    with dissolve

    u "Like, hookup with someone? You wanna lose your virginity in a brothel?"

    scene v14s03b_5f
    with dissolve

    ry "Is that so bad?"

    scene v14s03b_5g
    with dissolve

    menu:
        "Go for it":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            u "Well, no. Honestly, if it's just for practice then there's probably no better place than this. Just make sure that's really what you want to do."

            scene v14s03b_5b
            with dissolve

            ry "So, you don't think it's weird?"

            scene v14s03b_5c
            with dissolve

            u "Not at all. I think you should go for it."

        "Don't ruin your first time":
            $ reputation.add_point(RepComponent.BRO)
            u "Well, honestly... I wouldn't want my first time to be in a brothel."

            scene v14s03b_5a
            with dissolve

            ry "*Sighs* I don't know how to feel at this point."

    # -Regardless of choice scene continued

    scene v14s03b_6 # TPP An escort, Emerald, walks up to MC and Ryan. She is smiling with her mouth open, looking the boys up and down, sizing them up
    with dissolve

    emerald "Hey boys... You two sure are handsome. *Chuckles*"

    scene v14s03b_7 # FPP Show Ryan, looking at Emerald, Ryan is confused, with mouth open
    with dissolve

    ry "Are you talking to us?"

    scene v14s03b_8 # FPP Show Emerald, looking at MC and Ryan, smiling with mouth open
    with dissolve

    emerald "Do you see any other handsome men around here?"

    scene v14s03b_8a # FPP Same as 8, Emerald's mouth closed
    with dissolve

    u "Thank you, you-"

    ry "What is it about me that you find so handsome?"

    scene v14s03b_9 # TPP Show Emerald putting her arms around Ryan's neck, her face close to his, she is smiling with her mouth open. MC is smiling
    with dissolve

    emerald "Well, to begin... That voice of yours is pretty sexy, but maybe I could find out a little bit more. After a few drinks?"

    scene v14s03b_9a # TPP Same as 9, Ryan's mouth is open, Emerald's mouth closed
    with dissolve

    ry "I like the sound of that."

    scene v14s03b_10 # FPP MC looking at Ryan and Emerald, Ryan smiling with mouth open, turning his head to look at MC
    with dissolve

    ry "Hey [name], would you mind-"

    scene v14s03b_10a # FPP Same as 10, Ryan's mouth closed
    with dissolve

    u "Yeah, I'll be right back."

    scene v14s03b_10
    with dissolve

    ry "*Chuckles* Thanks man."

    scene v14s03b_11 # TPP Show MC walking up to the brothel bar
    with dissolve

    pause 0.75

    stop music fadeout 3
    jump v14s03c # -Transition to Scene 3c-