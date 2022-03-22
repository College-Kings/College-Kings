# SCENE 56: Wolves Living Room Chris apologizes
# Locations: Wolves living room
# Characters: CHRIS (Outfit: 1), MC (Outfit: 2), IMRE (Outfit: 1), SEBASTIAN (Outfit: x)
# Time: Thursday Morning

label v16s56: # 56) Wolves Living Room, Chriss apologizes
    scene v16s56_1 # TPP Show MC entering Wolves' front door
    with fade

    pause 0.75

    scene v16s56_2 # FPP In entryway of Wolves's house. Chris (neutral expression, mouth open) in entryway near door toward living room
    with dissolve

    ch "Hey, [name]. Please could you come into the living room for a minute?"

    scene v16s56_2a # FPP Same angle as 2. Chris (neutral expression, mouth closed, if visible) walking away from MC toward living room
    with dissolve

    u "Um... Okay, sure."

    scene v16s56_3 # TPP MC following Chris into the living room
    with dissolve

    pause 0.75

    scene v16s56_4 # FPP MC now in living room. Sebastion and Imre on sofa, Imre in the middle. Imre has his arms crossed, looking angry, avoiding eye contact
    with dissolve

    u "(Oh, shit. What now?)"

    scene v16s56_5 # FPP MC sits down on the couch next to Imre. Chris (mouth open, if visible) remains standing and faces the group on the couch
    with dissolve

    ch "Thanks for coming guys. I'll be quick."

    scene v16s56_6 # FPP Chris (neutral expression, mouth open) standing in front of group, looking at Imre
    with dissolve

    ch "I just wanted to say how sorry I am for what happened."

    ch "Imre, I hit you and I was wrong to do that. You're my brother and no matter what you said to me, I should've controlled myself."

    scene v16s56_7 # FPP Imre (angry expression, mouth open) looking up at Chris
    with dissolve

    imre "Like I give a fuck about what you have to say."

    scene v16s56_8 # FPP Sebastian (neutral expression, mouth open) leaning forward and looking at Imre (angry expression, mouth closed)
    with dissolve

    se "Imre, just hear him out."

    scene v16s56_7a # FPP Imre (angry expression, mouth open) looking away. Sebastian (neutral expression, mouth closed) in background
    with dissolve

    imre "*Scoffs* He's wasting his breath."

    scene v16s56_6
    with dissolve

    ch "I just want to put an end to all this hostility. I'm going through some stuff right now but I'm working on my anger issues..."

    scene v16s56_6a # FPP Chris (sad expression, mouth open) standing in front of group, holding his fists in front of him, pleading
    with dissolve

    ch "I promise you; I'm working on it."

    scene v16s56_6b # FPP Chris (sad expression, mouth closed) looking down at his feet
    with dissolve

    u "(He does seem sincere. But I think we've learned Chris can flip any second if someone says the wrong thing to him.)"

    scene v16s56_7
    with dissolve

    imre "Is that it? Can we go now?"

    scene v16s56_6
    with dissolve

    ch "I just want you to understand how sorry I am."

    scene v16s56_6a
    with dissolve

    ch "I'm apologizing to you, Imre, but also to the rest of you. It wasn't the behavior of a president that you can trust."

    scene v16s56_7
    with dissolve

    imre "Damn right about that."

    scene v16s56_6
    with dissolve

    ch "So, can you all forgive me?"

    scene v16s56_6b
    with dissolve

    menu:
        "Accept apology":
            $ add_point(KCT.BRO)

            u "I can forgive you, Chris."

            scene v16s56_6c # FPP Chris (hopeful expression, mouth closed) looking at MC
            with dissolve

            u "I just want things to get back to normal around here."

            scene v16s56_7b # FPP Imre (angry expression, mouth open) looking at MC.
            with dissolve

            imre "Really, [name]? You think we can just pretend like none of this ever happened?"

            scene v16s56_7
            with dissolve

            imre "I don't accept shit. I don't trust you Chris, and I'll probably never trust you ever again."

            scene v16s56_7c # FPP Imre (angry expression, mouth closed) sitting back into the couch, not looking at anybody
            with dissolve

            u "Imre, holding a grudge won't do us any favors."

            scene v16s56_7b
            with dissolve

            imre "Neither will having a cheating sleazebag as a president."

        "Hold a grudge":
            $ add_point(KCT.TROUBLEMAKER)

            scene v16s56_6b
            #with dissolve

            u "An apology doesn't take the punch back, you know?"

            scene v16s56_7b
            with dissolve

            imre "Exactly. Bullshit apology."

            scene v16s56_6b
            with dissolve

            u "What's done is done, and I'm not sure how long it's going to be before we can trust you like we did before."

            scene v16s56_7
            with dissolve

            imre "Oh I am. Never."

    scene v16s56_6d # FPP Chris (very sad, maybe tears in his eyes, mouth open) with his hands out, palms up, looking at the group
    with dissolve

    ch "So, you can't even forgive a brother for fucking up one time, huh?"

    scene v16s56_8a # FPP Sebastian (neutral expression, mouth open) leaning forward and looking up at Chris
    with dissolve

    se "You'll always be my brother, Chris, but I think we're all still processing how you've changed lately."

    scene v16s56_6a
    with dissolve

    ch "I know. All I can do is say sorry."

    scene v16s56_6b
    with dissolve

    ch "..."

    scene v16s56_6
    with dissolve

    ch "Anyway, that's all I wanted to say. I'm going to go think a few things over. You know how to reach me."

    scene v16s56_9 # FPP Show Chris leaving the living room
    with dissolve

    pause 0.75

    scene v16s56_8
    with dissolve

    se "Whatever you're feeling right now, just try to remember that Chris is feeling bad too. He's really cut up about all of this."

    scene v16s56_7a
    with dissolve

    imre "Yeah, he fucked up."

    scene v16s56_8
    with dissolve

    se "Let's just ride this thing out and see what happens. Chris might make changes on his own, without anyone having to yell at him."

    scene v16s56_7c
    with dissolve

    u "Whatever creates less drama, I'm all for it."

    scene v16s56_7a
    with dissolve

    imre "You already know how I feel. Fuck that guy."

    scene v16s56_10 # FPP Show Imre leaving the living room
    with dissolve

    se "*Sighs* I guess in the meantime, let's try and keep those two apart?"

    scene v16s56_11 # FPP MC, now standing, looking down at Sebastian (neutral expression, mouth closed) who is now alone on the couch, looking up at MC
    with dissolve

    u "Yeah, agreed."

    scene v16s56_12 # TPP Show MC (neutral expression, mouth closed) leaving the living room
    with dissolve

    pause 0.75

    if v14_help_lindsey: # TODO: Variable PLACEHOLDER VARIABLE # -if helping Lindsey, transition to Scene 58-
        jump v16s58

    else: # -if not helping Lindsey, transition to Scene 61-
        jump v16s61