# SCENE 02: Imre and Ryan Walk to RLD
# Locations: Hotel Lobby, Outside Hotel
# Characters: MC (Outfit: 3), IMRE (Outfit: 2), RYAN (Outfit: 1)
# Time: Night

label v14s02:
    play music music.ck1.v13.Track_Scene_36 fadein 2
    scene v14s02_1 # TPP. show mc in the hotel lobby and looking around everywhere, no expression, mouth closed
    with dissolve

    pause 0.75

    scene v14s02_1a # TPP. same as v14s02_1 different angle
    with dissolve

    pause 0.75

    scene v14s02_1b # TPP. same as v14s02_1a show imre sneaking up on mc, slight smile mouth closed
    with dissolve

    u "(Please don't tell me everyone is gone or asleep.)"

    scene v14s02_1c # TPP. imre taps mc's shoulder from behind, mc slight shock, mouth open
    with dissolve

    imre "BOO!"

    scene v14s02_2 # FPP. mc turns around and sees imre, imre slight smile, mouth open
    with dissolve

    imre "Did I scare you?"

    scene v14s02_2a # FPP. imre slight smile mouth closed
    with dissolve

    menu:

        "A little bit":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            u "Maybe a little bit."

            scene v14s02_2
            with dissolve

            imre "Haha, I knew it."

        "Not at all":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            scene v14s02_2a
            #with dissolve
            
            u "Not at all, bro."

            scene v14s02_2
            with dissolve

            imre "Damnit! I'll get you one day, for sure."

    scene v14s02_2a
    with dissolve

    u "Haha, what are you doing tonight?"

    scene v14s02_2
    with dissolve

    imre "I was just coming to get you actually."

    scene v14s02_2a
    with dissolve

    u "For?"

    scene v14s02_2b # FPP. same as v14s02_2 imre is excited
    with dissolve

    imre "Ryan and I are headed to the Red Light District for our last night in Europe. You wanna come with?"

    scene v14s02_2c # FPP. same as v14s02_2b imre mouth closed
    with dissolve

    u "Wait, you're hanging out with Ryan now?"

    scene v14s02_2d # FPP. same as v14s02_2b imre slightly serious
    with dissolve

    imre "We've been hanging out a bit, but we're not friends. I've decided I'd at least give the \"acquaintance\" thing a chance."

    scene v14s02_2a
    with dissolve

    u "*Laughs* Look at you. Being mature and all."

    scene v14s02_2e # FPP. same as v14s02_2d imre rolls his eyes
    with dissolve

    pause 0.75
    
    scene v14s02_2
    with dissolve

    imre "Yeah, don't get too excited. We'll see how long it lasts."

    scene v14s02_2a
    with dissolve

    u "*Laughs*"

    scene v14s02_2f # FPP. same as v14s02_2a Ryan walks up behind imre, looking at imre, imre turns around to look at ryan, ryan no expression mouth open, imre mouth closed no expression
    with dissolve

    ry "Imre, he isn't in his-"

    scene v14s02_2g # FPP. same as v14s02_2f ryan is standing beside imre, imre and ryan looking at mc
    with dissolve

    ry "Oh... Hey [name]."

    scene v14s02_2h # FPP. same as v14s02_2g ryans mouth closed
    with dissolve

    u "How did you not see me standing here?"

    scene v14s02_2g
    with dissolve

    ry "I don't know... Did Imre fill you in?"

    scene v14s02_2i # FPP. same as v14s02_2h ryan and imre slight smiles
    with dissolve

    u "Ha, yeah. He did."

    scene v14s02_2j # FPP. same as v14s02_2i ryans mouth open
    with dissolve

    ry "Good. Are we ready to go?"

    scene v14s02_2i
    with dissolve

    u "Lead the way."

    scene v14s02_2k # FPP. same as v14s02_2j imres mouth open
    with dissolve

    imre "Alright titties, here I come!"

    scene v14s02_2i
    with dissolve

    u "*Sighs* Typical Imre."

    scene v14s02_3 # TPP. mc, ryan, and imre walk towards the hotels front door, all slight smiles, mouths closed, looking straight ahead
    with dissolve

    pause 0.75

    scene v14s02_4 # TPP. mc, ryan, and imre seen leaving the hotel from the street view, all slight smiles, mouths closed, looking straight ahead
    with dissolve

    pause 0.75

    scene v14s02_5 # TPP. mc, ryan, and imre seen walking down the sidewalk, all slight smiles, mouths closed, looking straight ahead
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v14s03