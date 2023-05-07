# SCENE 22: Your Room Samantha
# Locations: MC Apes room
# Characters: MC (Outfit 3), Samantha (Outfit 1)
# Time: Friday Afternoon

label v9_room_w_sam:
    scene v9rwsa1 # TPP. Show MC's apes door.
    with dissolve

    play sound sound.knock

    "*Knock* *Knock*"

    scene v9rwsa2 # TPP. Show MC getting up from his desk to answer his door.
    with dissolve

    play music "music/v9/Track Scene 21.mp3" fadein 2

    pause 0.8

    scene v9rwsa3 # FPP. Show Lindsey stood outside MC's door, Lindsey mouth closed.
    with dissolve

    u "(Wow, didn't expect it to be her.)"

    u "Hey, what's up?"

    scene v9rwsa3a # FPP. Same camera as v9rwsa3, Lindsey mouth open.
    with dissolve

    sa "Can I come in?"

    scene v9rwsa3
    with dissolve

    u "Sure!"

    scene v9rwsa4 # TPP. Show MC moving out the way as Samantha walk into his room.
    with dissolve

    pause 1

    scene v9rwsa5 # TPP. Show Samantha turning MC's chair at his desk around as if she's about to sit on it.
    with dissolve

    pause 1

    scene v9rwsa6 # FPP. Show Samantha now sat on MC's chair, Samantha mouth closed.
    with dissolve

    u "Is everything OK?"

    scene v9rwsa6a # FPP. Same camera as v9rwsa6, Samantha mouth open.
    with dissolve

    sa "Yes, everything's fine. I just wanted to talk to you."

    scene v9rwsa6
    with dissolve

    u "I'm all ears."

    if hl_punch:
        scene v9rwsa6a
        with dissolve
        
        sa "First, I wanted to say I'm so sorry for how Cameron treated you earlier."
            
        scene v9rwsa6
        with dissolve
        
        u "Aww don't worry about me. I'm used to these guys."

        scene v9rwsa6a
        with dissolve

        sa "Still, it wasn't right. I had a firm talk with him after we left."

        scene v9rwsa6
        with dissolve

        u "And how did that go?"

        scene v9rwsa6b # FPP. Same camera as v9rwsa6, Samantha smile, mouth open.
        with dissolve

        sa "About as well as expected."

        scene v9rwsa6c # FPP. Same camera as v9rwsa6, Samantha smile, mouth closed.
        with dissolve

        u "I bet!"

    if not sideWithCameron:
        scene v9rwsa6d # FPP. Same camera as v9rwsa6, Samantha looks slightly sad, mouth open.
        with dissolve

        sa "I wanted to come apologize for dragging you into my mess. I'm so sorry you got caught up in all this."

        scene v9rwsa6e # FPP. Same camera as v9rwsa6, Samantha looks slightly sad, mouth closed.
        with dissolve

        u "What? No. Don't apologize. We all have our drama. You wouldn't believe some of the stuff that's happened in my life."

        scene v9rwsa6d
        with dissolve

        sa "I know, but sometimes Cameron can really be a... well, an Ape!"

        scene v9rwsa6e
        with dissolve

        u "He's definitely in the right frat!"

        scene v9rwsa6d
        with dissolve

        sa "He's been there for me though, and I know it hasn't been easy for him. I'm such a mess."

        scene v9rwsa6e
        with dissolve

        menu:
            "Understand Samantha":
                u "Yeah, I heard some of what you went through. Cam and I talked earlier."

                scene v9rwsa6f # FPP. Same camera as v9rwsa6, Samantha looks away from the camera slightly, embrassed, mouth open,
                with dissolve

                sa "Oh."

                scene v9rwsa6e
                with dissolve

                u "I totally understand though. He's your big brother."

                scene v9rwsa6d
                with dissolve

                sa "I think I made a mistake staying here. I don't want to cause more problems."

                scene v9rwsa6e
                with dissolve

                u "No! No, don't think like that. We're here to help you."

                scene v9rwsa6b
                with dissolve
                
                sa "You're so sweet. You're not like the other meatheads here."

                scene v9rwsa6c
                with dissolve

                u "I have my moments."                    
                
            "Console Samantha":
                $ reputation.add_point(RepComponent.BOYFRIEND)

                u "You're not a mess! You're figuring your life out. We're supposed to screw up."

                scene v9rwsa6d
                with dissolve

                sa "Not like this."

                scene v9rwsa6e
                with dissolve

                u "Maybe not everyone has gone through your troubles, but plenty have... and they've come back from it just fine."

                scene v9rwsa6a
                with dissolve

                sa "You think?"

                scene v9rwsa6
                with dissolve

                u "Sure do. I've seen it with my own eyes. And you look like the type to make something of herself."

                scene v9rwsa6b
                with dissolve

                sa "That would be nice."

    else:
        scene v9rwsa6b
        with dissolve

        sa "I wanted to come thank you for your support earlier, that thing with Cam and Grayson."

        scene v9rwsa6c
        with dissolve

        menu:
            "Play it off":
                $ reputation.add_point(RepComponent.BRO)

                u "No need to thank me. Really. it was nothing. I support my fellow Apes."

                scene v9rwsa6b
                with dissolve

                sa "It wasn't nothing to me. Things have been a mess lately and Cameron and I appreciate your support."
                
                scene v9rwsa6c
                with dissolve

                u "He said that?"

                scene v9rwsa6g # FPP. Same camera as v9rwsa6, Samantha laugh, mouth open.
                with dissolve

                sa "Well, not in so many words. But I know he feels it."
                
                scene v9rwsa6c
                with dissolve

                u "In that case, you're both welcome."

            "Accept the thanks":
                $ reputation.add_point(RepComponent.BOYFRIEND)

                u "Aww, you're welcome. Apes gotta stick together, you know. And that includes you now."

                scene v9rwsa6g
                with dissolve

                sa "Guess I gotta learn how to kick some ass."

                scene v9rwsa6c
                with dissolve

                u "You're definitely in the right place!"

        scene v9rwsa6a
        with dissolve

        sa "I hope you know I'm trying to turn things around. I don't want to be like this forever."

        scene v9rwsa6
        with dissolve

        u "And you won't be. I can see it in your eyes. You're strong. You've got this. And you've got us now, too."

        scene v9rwsa6b
        with dissolve

        sa "Thanks. That means a lot."

    scene v9rwsa7 # FPP. Show Samantha getting up from MC's chair, Samantha smile, mouth open.
    with dissolve

    sa "Alright, enough of that! I think I need some fresh air. You should come with me."

    scene v9rwsa7a # FPP. Same camera as v9rwsa7, show Samantha now fully stood up, smile, mouth closed.
    with dissolve

    u "Sure!"

    scene v9rwsa8 # TPP. Show Samantha and MC leaving the room together.
    with dissolve

    pause 1

    scene black
    with dissolve

    stop music fadeout 3

    pause 0.5

    jump v9_walk_w_sam