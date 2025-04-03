# SCENE 28: Riley storms up to MC in the lobby
# Locations: Hotel Lobby 
# Characters: RILEY (Outfit: 3), MC (Outfit: 3)
# Time: Evening
# Phone Images: None

label v12_riley_lobby:
    scene v12ril1 # FPP. MC standing in the hotel lobby, Riley is pretty far away from MC. MC looking at Riley, Riley very angry, mouth closed, walking over to MC
    with dissolve

    pause 0.75
    play music music.ck1.v12.Track_Scene_28 fadein 2

    scene v12ril1a # FPP. Same as v12ril1, Riley now in talking distance to MC, Riley very angry, mouth open
    with dissolve

    ri "[name]! HOW COULD YOU DO SOMETHING LIKE THAT TO ME?!"

    scene v12ril1b # FPP. Same as v12ril1a, Riley very angry, mouth closed
    with dissolve

    u "What are you talking about, Riley? What's going on?!"

    scene v12ril1c # FPP. Same as v12ril1a, Riley crying and angry, mouth open
    with dissolve

    ri "*Crying* Don't \"what are you talking about\" me! You hung my picture up for everyone to see!"

    scene v12ril1d # FPP. Same as v12ril1c, Riley crying and angry, mouth closed
    with dissolve

    u "What?! No, no, no! I didn't, I haven't even been here. I just got back from getting a ta-"

    scene v12ril1c
    with dissolve

    ri "So I go my entire time in college without a problem and then coincidentally after I tell you about my picture, it's hanging up in the lobby? Sounds like bullshit!"

    scene v12ril1d
    with dissolve

    u "I don't know what happened, or who did it, but it wasn't me."

    scene v12ril1e # FPP. Same as v12ril1d, Riley different pose
    with dissolve

    u "You should probably consider how you're talking to me right now 'cause whenever you find out what actually happened, you're gonna feel horrible for the way you're treating me."

    scene v12ril1f # FPP. Same as v12ril1e, Riley very angry and crying, mouth open
    with dissolve

    ri "No I'm not, because I already know who did it, it was you. I'm not fucking stupid, [name]."

    scene v12ril1c
    with dissolve

    ri "It's common sense that you took it considering you're the only person who knows about it besides myself. I don't know why you would do this to me after I told you how I felt."

    scene v12ril1f
    with dissolve

    ri "I literally told you I'd hate you if you ever showed it to anyone and you showed it to everyone, so just consider yourself hated."

    scene v12ril1g # FPP. Same as v12ril1, Riley walking away, back turned to MC
    with dissolve

    u "RILEY!"

    scene v12ril2 # TPP. Show MC looking at Riley walking away, MC confused, mouth closed, Riley's back to the camera
    with dissolve

    u "(What the fuck?!)"

    scene v12ril3 # TPP. Show MC walking over to the couch in the hotel lobby, angry, mouth closed
    with dissolve

    u "(I get why she'd blame me, but I didn't do that shit. Who the fuck could've known about it?)"
    u "(The door was open, so really... Anyone could've been listening, but the only person I know that was around was...)"

    scene v12ril4 # TPP. Show MC sitting on the couch, he's angry, mouth closed
    with dissolve

    pause 1.25

    scene v12ril4a # TPP. Same as v12ril4, MC different pose
    with dissolve

    u "(Charli. That motherfucker. I wouldn't be surprised if it was him, but at the same time I'd be absolutely amazed.)"

    stop music fadeout 3
    
    if (CharacterService.is_kissed(lauren) or CharacterService.is_girlfriend(lauren)) and not "v11_aubrey" in sceneList:
        jump v12_lauren_sex #scene 29
    else:
        jump v12_late_night_workout #scene 29a