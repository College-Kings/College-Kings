# SCENE 39: MC and Riley walk home
# Locations: Sidewalk by park
# Characters: MC (Outfit 9), Riley shoes and jeanshorts from outfit 2, hongyu-s bikini for v8, wave texture(red and white stripes) texture mud female geoshell- a little muddy - for character dirty look
# Time: Evening
label v10_riley_walk:

    scene v10srwh1 # FPP. Riley approaches MC from distance. She looks dirty, smiling, closed.
    with fade
    play music music.ck1.v10.Track_Scene_39 fadein 2
    pause 0.75

    scene v10srwh1a # FPP. Same camera as v10srwh1. Show Riley, smiling, mouth open.
    with dissolve

    ri "[name] did you see her kiss me? *Laughs*"

    scene v10srwh1b # FPP. Same camera as v10srwh1. Show Riley, smiling, mouth closed.
    with dissolve

    u "You looked like you enjoyed it. *Laughs*"

    scene v10srwh1a
    with dissolve

    ri "I was shocked, but as far as enjoying it, I don't know. Maybe. *Chuckles*"

    scene v10srwh1b
    with dissolve

    u "Amber can do that to you."

    scene v10srwh1a
    with dissolve

    ri "Haha. So, question, do you mind walking me home? I came here with Lauren, but she's going back to the Deer house."

    scene v10srwh1b
    with dissolve

    u "Yeah, I'll walk you home. The faster you get to the shower the better. *Laughs*"

    scene v10srwh1a
    with dissolve

    ri "Haha, true."

    scene v10srwh2 # TPP. Show MC and Riley (dirty) walking together, both smiling, mouth closed.
    with fade

    if v10s33_aubreyriley: # if spoke to Aubrey and RIley at dancing booth
        scene v10srwh3 # FPP. Show Riley as though she's walking next to MC, smiling, mouth open.
        with dissolve
        
        ri "Man, Aubrey's moves at the dance booth today were crazy."

        scene v10srwh3a # FPP. Same camera as v10srwh3. Show Riley as though she's walking next to MC, smiling, mouth closed.
        with dissolve

        u "Yeah, she's pretty good."

    else: # if not spoke to Aubrey and Riley at dancing 
        scene v10srwh3
        with dissolve
        
        ri "Did you see Aubrey at the dancing booth? I had no idea she could dance like that."

        if not "aubrey" in freeroam6: # -If spoke to Aubrey during freeroam
            scene v10srwh3a
            with dissolve

            u "Haha, yeah I saw her. She even wanted me to dance with her."

        else: # -If didn't speak to Aubrey during freeroam
            scene v10srwh3a
            with dissolve

            u "No, sadly I didn't see her until the mud wrestling."

    scene v10srwh3
    with dissolve

    ri "They say the better you are at dancing the better you are in bed. Something about rhythm. *Chuckles*"

    scene v10srwh3a
    with dissolve

    u "Riley did I ever tell you I'm a professional in all forms of dance?"

    scene v10srwh3
    with dissolve

    ri "You couldn't say that with a straight face. *Laughs*"
    
    ri "Now Aubrey on the other hand, she knows how to dance so I can only imagine. You know?"

    if CharacterService.is_fwb(aubrey): # -If MC slept with aubrey
        scene v10srwh3a
        with dissolve

        u "Oh I can imagine."

    else: # If MC didn't sleep with Aubrey
        scene v10srwh3a
        with dissolve

        u "Yeah, that's true."

    scene v10srwh3a
    with dissolve

    u "*Chuckles* So, what else were you looking at during the event?"

    scene v10srwh3
    with dissolve

    ri "Didn't really look at much, but I did speak to a lot of people. Everyone wanted to talk to me once they found out I was in the main event."

    scene v10srwh3a
    with dissolve

    u "I don't doubt it."

    scene v10srwh3
    with dissolve

    ri "Oh oh, you're gonna think this is hilarious. I was walking by the win a date booth right, and I saw Mr. Lee and Ms. Rose talking all excited so I listened for a little bit."
    
    ri "Did you know Mr. Lee ran for Mayor a few years ago?"

    scene v10srwh3a
    with dissolve

    u "*Chuckles* You serious?"

    scene v10srwh3
    with dissolve

    ri "His slogan was \"Let's Make History\". It's so ironic, it's hilarious."

    scene v10srwh3a
    with dissolve

    u "I bet Ms. Rose got a kick out of that."

    scene v10srwh3
    with dissolve

    ri "More than a kick, those two acted like they've been best friends since grade school."

    scene v10srwh3a
    with dissolve

    u "As much as Cameron teases him, Mr. Lee could use a friend. *Chuckles*"

    scene v10srwh3
    with dissolve

    ri "*Chuckles*"

    scene v10srwh3
    with dissolve

    ri "You know [name], I'm really glad we're friends."

    scene v10srwh3a
    with dissolve

    u "Me too."

    scene v10srwh3
    with dissolve

    ri "No for real for real. I get along with other girls, but as far as guys go there aren't many that I really feel that close with. But I do feel pretty close with you."

    if CharacterService.is_fwb(riley): # if MC and Riley had sex
        scene v10srwh3a
        with dissolve

        u "Haha I wonder why."

    else: # if MC and Riley didn't have sex
        scene v10srwh3a
        with dissolve

        u "Awww stop, you're gonna make me cry."

    scene v10srwh3
    with dissolve

    ri "Haha, stop it, I'm serious. Thanks for being a good friend."

    scene v10srwh3a
    with dissolve

    u "You're welcome."

    if CharacterService.is_fwb(riley):
        scene v10srwh3b # FPP. Same camera as v10srwh3. Show Riley as though she's walking next to MC, with more of a mischevious smile, mouth open.
        with dissolve

        ri "Buuut I'm also glad we're more than just friends. Especially because of what I have planned for tonight."

        scene v10srwh3a
        with dissolve

        u "Uhhh, you're gonna end up making Amber jealous. *Chuckles*"

        scene v10srwh3
        with dissolve

        ri "She can come too."

        scene v10srwh3a
        with dissolve

        u "What?"

        scene v10srwh3
        with dissolve

        ri "I'm just kidding... kinda. *Laughs*"

        scene v10srwh3a
        with dissolve

        u "*Chuckles*"

    scene v10srwh3
    with dissolve

    ri "Do you feel like you've gotten to know everyone on campus for the most part?"

    scene v10srwh3a
    with dissolve

    u "For the most part yeah."

    scene v10srwh3
    with dissolve

    ri "Not me, I swear I meet new people all the time. Today I met too many. It's safe to say that Jackson is a very popular name on campus."

    scene v10srwh3a
    with dissolve

    u "I don't know anyone named Jackson."

    scene v10srwh3
    with dissolve

    ri "I met five of them."

    scene v10srwh3a
    with dissolve

    u "Haha, the Jackson Five."

    scene v10srwh3c # FPP. Same camera as v10srwh3. Show Riley as though she's walking next to MC, with a curious expression and a slight smile, mouth open.
    with dissolve

    ri "Wait what?"

    scene v10srwh3d # FPP. Same camera as v10srwh3. Show Riley as though she's walking next to MC, with a curious expression and a slight smile, mouth closed.
    with dissolve

    u "You know, the brothers?"

    scene v10srwh3c
    with dissolve

    ri "I'm not following?"

    scene v10srwh3d
    with dissolve

    u "The group of brothers that used to sing together."

    scene v10srwh3c
    with dissolve

    ri "Wait, all of them did kinda look alike. I wonder if they were brothers. Jackson was probably their last name."
    
    ri "One of them just said \"we're all named Jackson\" so I... okay yeah it was definitely their last name. *Laughs*"

    scene v10srwh3a
    with dissolve

    u "A little slow there huh? *Chuckles*"

    scene v10srwh3
    with dissolve

    ri "*Laughs* No! I just needed to think about it out loud."

    scene v10srwh3a
    with dissolve

    u "If they all sang that would be cool, it'd be like a reincarnation of the past."

    scene v10srwh3
    with dissolve

    ri "Maybe they'll perform at one of the holiday events."

    scene v10srwh3a
    with dissolve

    u "That would be nice."

    scene v10srwh4 # TPP. Show MC and Riley standing in her dorm.
    with fade

    stop music fadeout 3
    
    jump v10_riley_sex