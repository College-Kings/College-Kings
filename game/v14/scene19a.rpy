# SCENE 19a: Chloe convo after plan for phase 1 is confirmed
# Locations: Library
# Characters: CHLOE (Outfit: x), MC (Outfit: 1), UNKNOWN (Outfit: N/A (not seen))
# Time: 

label v14s19a:
    play music "music/v12/Track Scene 27a_3.mp3" fadein 2

    scene v14s19a_1 # FPP Show Chloe, in library, looking at MC, smiling with mouth open
    with dissolve

    cl "I really think this is the most solid plan."

    scene v14s19a_1a # FPP Same as 1, Chloe's mouth closed
    with dissolve

    u "I do too."

    if v14_chloe_wolves:

        scene v14s19a_1
        with dissolve

        cl "Especially since I basically already have the Wolves' support, I feel confident about this."

        scene v14s19a_1a
        with dissolve

        u "Oh, yeah? How'd that come about?"

        scene v14s19a_1b # FPP Same angle as 1, Chloe looks confused and curious, mouth open
        with dissolve

        cl "How did what come about?"

        scene v14s19a_1c # FPP Same angle as 1, Chloe with neutral expression, mouth closed
        with dissolve

        u "The Wolves supporting you already? I ran into Imre this morning while he was chanting in your favor."

        scene v14s19a_2 # TPP Chloe talking to MC, Chloe's hand on MC's arm, Chloe laughing, mouth open
        with dissolve

        cl "Oh.. That's simple."

        scene v14s19a_2a # TPP Same angle as 2, Chloe standing with her arms folded across her chest, smiling and addressing MC like a speech
        with dissolve

        cl "Chris and I share the same principles when it comes to leadership and loyalty."
        cl "You can't blame all of the issues on the leader and give up on them, throwing them away, thinking that'll change things."

        scene v14s19a_1d # FPP Same angle as 1, Chloe with her arms out to her sides, smiling like she's giving a speech
        with dissolve

        cl "You have to work on improving the leadership that's already comfortably in place."

        scene v14s19a_1a
        with dissolve

        u "So, you and Chris aren't that close? Just share some perspectives?"

        scene v14s19a_1
        with dissolve

        cl "Well, no... I mean, we're pretty close."

        scene v14s19a_1a
        with dissolve

        u "Even with Nor-"

        scene v14s19a_1e # FPP Same angle as 1, Chloe holding her hand out in a «hold on» gesture, smiling with mouth open
        with dissolve

        cl "I already know what you're gonna say, haha."

        scene v14s19a_1
        with dissolve

        cl "Whatever's happening between Chris and Nora is their business..."
        cl "And I think because I don't get involved as much as others, we have this unspoken respective relationship, you know?"

        scene v14s19a_1a
        with dissolve

        u "Yeah, makes sense, the Wolves are very much about loyalty."

        scene v14s19a_2
        with dissolve

        cl "Exactly, and though Chris may support me as a leader, it doesn't mean all of the Wolves will want to..."
        cl "That's where a little favor from my favorite guy comes in."

        scene v14s19a_2b # TPP Same angle as 2, Chloe's hand still on MC's arm, Chloe smiling, mouth closed, MC smiling and rolling his eyes, mouth open
        with dissolve

        u "*Sighs* What now?"

        scene v14s19a_1f # FPP Same angle as 1, Chloe looking slightly nervous or worried, mouth open
        with dissolve

        cl "Am I asking you for too much?"

        scene v14s19a_1a
        with dissolve

        u "Haha, no... I'm just teasing."

        scene v14s19a_1
        with dissolve

        cl "Okay good, ha. I was nervous for a second..."

        scene v14s19a_1a
        with dissolve

        u "*Laughs* No, go ahead. What's the favor?"

        scene v14s19a_1f
        with dissolve

        cl "I was wondering if you could talk to Chris about the Wolves actively supporting me."

        scene v14s19a_1c
        with dissolve

        u "Is he not already? I told you, Imre said he was rooting for you. He was screaming it to the world in fact, haha."

        scene v14s19a_1
        with dissolve

        cl "*Chuckles* Rooting for and actively supporting are two very different things."

        scene v14s19a_1d
        with dissolve

        cl "I need the Wolves' help with things on a grand scale if I want to beat Lindsey."

        scene v14s19a_1
        with dissolve

        cl "And honestly when it comes to Imre, he's had a crush on me for as long as I can remember. *Laughs*"
        cl "When I called him this morning he picked up right away and was way too excited to help..."

        scene v14s19a_1a
        with dissolve

        u "*Laughs* That's amazing."

        scene v14s19a_1f
        with dissolve

        cl "So, do you think you can talk to Chris about this? Today?"

        if not v14_help_lindsey: # -If don't help Lindsey
            $ chloe.points += 1
            $ v14_talk_to_chris = True

            scene v14s19a_1g # FPP Same as 1f, Chloe's mouth closed, she is biting her lower lip slightly
            with dissolve

            u "Of course I can."

            scene v14s19a_2
            with dissolve

            cl "Perfect! Thank you so so so much, [name]."

        else: # If helped Lindsey
            scene v14s19a_1g
            with dissolve

            u "(Damn, I promised to go meet Lindsey later. Do I have time for both? This \"double agent\" life might get tricky...)"

            menu:
                "Talk to Chris":
                    $ add_point(KCT.BOYFRIEND)
                    $ chloe.points += 1
                    $ v14_talk_to_chris = True

                    u "Of course I can."

                    scene v14s19a_2
                    with dissolve

                    cl "Perfect! Thank you so much, [name]. This means the world to me."

                "Make an excuse":
                    $ add_point(KCT.BRO)
                    
                    scene v14s19a_1g
                    #with dissolve
                    
                    u "I hate to state the obvious but, Chris and I aren't on the best of terms right now... And he's got Nora on his mind, so..."

                    scene v14s19a_1c
                    with dissolve

                    u "It's probably not best if I'm the one who talks to him."

                    scene v14s19a_1h # FPP Same angle as 1, Chloe looking a bit sad and dissapointed, mouth open
                    with dissolve

                    cl "*Sighs* Yeah, I get it. His head isn't in the right space around you. Smart thinking."
    else:
        
        scene v14s19a_1
        with dissolve

        cl "So yeah, I'll set everything up and will let you know when it's ready."

        scene v14s19a_1a
        with dissolve

        u "Awesome."

    # -Continue regardless of everything
    stop music fadeout 3
    play music "music/v14/Track Scene 19a_2.mp3" fadein 2

    scene v14s19a_3 # Show a book dropping flat on the ground with a loud "smack"
    with vpunch
    play sound "sounds/hs.mp3"

    pause 0.75

    scene v14s19a_4 # FPP Show Chloe jumping, pulling her arms in to her chest and screaming
    with dissolve

    cl "*Screams* AH!"

    scene v14s19a_4a # FPP Same angle as 4, Chloe still looking toward the source of the sound and looking a little scared, mouth closed
    with dissolve

    u "Relax..."

    scene v14s19a_4b # FPP Same angle as 4, Chloe looking at MC, still jumpy but more relaxed, mouth open
    with dissolve

    cl "That scared me!"

    # -An unknown that isn't seen speaks-
    scene v14s19a_5 # Show a bookshelf, the type in a library with books on both sides, someone not visible on the other side of the shelf
    with dissolve

    unknown "SHHH!"

    scene v14s19a_1
    with dissolve

    cl "Cliche library kids."

    scene v14s19a_1a
    with dissolve

    u "Haha. Just like in the movies."

    scene v14s19a_1
    with dissolve

    cl "Right. Well, I need to be on my way. Thanks again for helping me with the plan."

    scene v14s19a_1a
    with dissolve

    u "Always."

    scene v14s19a_6 # FPP Chloe walking off out of the library
    with dissolve

    pause 0.75

    scene v14s19a_7 # TPP Show MC leaving the library
    with dissolve

    pause 0.75

    scene v14s19a_8 # TPP Show MC arriving in the school halls
    with dissolve

    pause 0.75

    stop music fadeout 3
    jump v14s20 # -Transition to Scene 20-