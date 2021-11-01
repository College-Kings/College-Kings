# SCENE 25b: Wake up at Amber's
# Locations: Ambers Place
# Characters: MC (Outfit: 2), AMBER (Outfit: 4)
# Time: Morning

label v14s25b:
    scene v14s25b_1 # TPP. Show MC birds eye view in bed, looking up to the roof, slight smile, mouth closed, Amber beside him, sleeping on her right side though, neutral expression, mouth closed
    with dissolve

    u "(I'm not used to being the first one awake. *Chuckles*)"

    scene v14s25b_2 # TPP. Show MC getting out of bed, neutral expression, mouth closed
    with dissolve

    pause 0.75 

    scene v14s25b_3 # TPP. Show MC getting dressed, neutral expression, mouth closed
    with dissolve

    pause 0.75

    scene v14s25b_4 # TPP. Show MC walking to Ambers side of the bed, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v14s25b_5 # FPP. MC now looking at Amber, MC has both hands on Amber shaking her, Amber, eyes closed, neutral expression, mouth closed
    with dissolve

    pause 0.75

    scene v14s25b_5a # FPP. Same as v14s25b_5, MC shakes Amber, different posture
    with dissolve

    u "*Whispers* Amber... Amber!"

    if AmberClean: #placeholder
        scene v14s25b_6 # FPP. MC now looking at Amber as she is laying in bed, Amber, slight smile, mouth open
        with dissolve

        am "Hm? You headed out?"

        scene v14s25b_6a # FPP. Same as v14s25b_6, mouth closed
        with dissolve

        u "Yeah, gonna go check on this bakesale situation."

        scene v14s25b_6b # FPP. Same as v14s25b_6, Same as v14s25b_6, concerned expression
        with dissolve

        am "Be safe, okay? I'll be headed that way soon... I may or may not see you."

        scene v14s25b_6a
        with dissolve

        u "Sounds good, see you soon."

        scene v14s25b_6
        with dissolve

        am "Thank you for everything."

        scene v14s25b_7 # TPP. Show MC looking at Amber, MC, mouth closed, slight smile, Amber, slight smile, mouth closed
        with dissolve

        if v14s25_letherstay: #placeholder
            scene v14s25b_8 # TPP. Show MC tucking Amber in bed, MC, slight smile, mouth closed, Amber, eyes closed, slight smile, mouth closed
            with dissolve

            u "Always."

            scene v14s25b_8a # TPP. Same as v14s25b_8, MC kisses Amber on her forehead
            with dissolve

            pause 0.75 

    if v14_amber_drugs: #placeholder
        scene v14s25b_6c # FPP. Same as v14s25b_6, Amber now turns and faces away from MC while laying in bed, MC doesn't see her face
        with dissolve
    
        am "*Mumbles*"

        u "(Guess she's too fucked up from last night. *Chuckles*)"

        scene v14s25b_9 # TPP. Show MC thinking to himself, slight smile, mouth closed
        with dissolve

        u "(I'll catch up with her later. I gotta get to the bake sale and see how that's all going.)"
    
    scene v14s25b_10 # TPP. Show MC leaving Ambers room, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v14s25b_11 # TPP. Show MC walking back to Campus, neutral expression, mouth closed 
    with dissolve

    pause 0.75

    if v14_help_lindsey: 
        jump v14s26
    
    elif v14_lauren_sabotage:
        jump v14s26a

    else:
        jump v14s26a
