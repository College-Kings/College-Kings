# SCENE 03d: If mc chose with him Sex scene with Escort
# Locations: Brothel private room
# Characters: SATIN (Outfit: x), MC (Outfit: 3)
# Time: 

label v14s03d:
    play music music.v14_Track_Scene_3d_1 fadein 2

    scene v14s03d_1 # TPP View from behind Satin, show Satin pushing MC into a sitting position with a hand on his shoulder, Satin's mouth open if visible
    with dissolve

    satin "So, have you ever been to a brothel before?"

    scene v14s03d_2 # FPP Show Satin standing in front of MC, who is smiling at him seductively, her mouth closed
    with dissolve

    u "Nope, I haven't."

    scene v14s03d_2a # FPP Same as 2, Satin's mouth open
    with dissolve

    satin "Good to know..."

    scene v14s03d_2b # FPP Same angle as 2, Satin has one eyebrow raised, smiling with mouth open
    with dissolve

    satin "Oh, and you aren't a virgin like your friend, right?"

    scene v14s03d_2c # FPP Same as 2b, Satin's mouth closed
    with dissolve

    u "Ha, no. Definitely not a virgin."

    scene v14s03d_2b
    with dissolve

    satin "You said that with a puffed out chest."

    scene v14s03d_2c
    with dissolve

    u "Wanted to be loud and clear, you know? I can't have you thinking that I'm slacking in what I'm packing. *Laughs*"

    scene v14s03d_2a
    with dissolve

    satin "*Laughs* Okay, sir. Sit back and just relax."

    scene v14s03d_2
    with dissolve

    u "As you wish..."

    scene v14s03d_3 # TPP Show Satin removing MC's clothes
    with dissolve

    pause 0.75

    if is_censored:
        call screen censored_popup("v14s03d_nsfwSkipLabel1")

    scene v14s03d_4 # FPP Show Satin removing her clothes
    with dissolve

    pause 0.75

    scene v14s03d_4a # FPP Same angle as 4, Satin starts posing for MC in a sexy position
    with dissolve

    pause 0.75

    scene v14s03d_4b # FPP Same angle as 4, Satin in a different sexy pose for MC
    with dissolve

    u "Satin, you- You have an amazing-"

    scene v14s03d_5 # TPP Close up side view of MC and Satin, showing just the sides of their faces which are close together, MC on the right. Satin is smiling at him, with her finger on his lips, her mouth open
    with dissolve

    satin "Shhh, just relax."

    scene v14s03d_5a # TPP Same angle as 5, Satin's finger no longer on MC's lips. Both smiling, Satin's mouth open
    with dissolve

    satin "No need for talking."

    scene v14s03d_6 # TPP Show Satin closing MC's eyes with her fingertips and gently tilting his head back
    with dissolve

    pause 0.75

    scene v14s03d_7 # TPP Show Satin getting on her knees between MC's legs, her hands on his naked thighs
    with dissolve

    pause 0.75

    # -Start of Sex Scene

    # -Satin begins deep throating Mc's dick-
    # From scene animations folder v14satdtFPP
    image v14satdtFPP = Movie(play="images/v14/Scene 3d/v14satdtFPP.webm", loop=True, image="images/v14/Scene 3d/v14satdtFPP.webp", start_image="images/v14/Scene 3d/v14satdtFPP.webp")
    image v14satdtFPPf = Movie(play="images/v14/Scene 3d/v14satdtFPPf.webm", loop=True, image="images/v14/Scene 3d/v14satdtFPP.webp", start_image="images/v14/Scene 3d/v14satdtFPP.webp")

    scene v14satdtFPP # Ignore as animation
    with dissolve
    if voice_acted:
        $ renpy.sound.play(music.ck1.v14.Scene_3d_bj_slow_4loops, loop=True)

    satin "*Gags* Mmmghh!"

    stop sound
    scene v14satdtFPPf # Ignore as animation
    with dissolve
    if voice_acted:
        $ renpy.sound.play(music.ck1.v14.Scene_3d_bj_fast_4loops, loop=True)

    u "S-shit! You're a fucking professional! (She's deepthroating like a goddess.)"

    # From scene animations folder v14satdtTPP
    image v14satdtTPP = Movie(play="images/v14/Scene 3d/v14satdtTPP.webm", loop=True, image="images/v14/Scene 3d/v14satdtTPP.webp", start_image="images/v14/Scene 3d/v14satdtTPP.webp")
    image v14satdtTPPf = Movie(play="images/v14/Scene 3d/v14satdtTPPf.webm", loop=True, image="images/v14/Scene 3d/v14satdtTPP.webp", start_image="images/v14/Scene 3d/v14satdtTPP.webp")

    stop sound
    scene v14satdtTPP # Ignore as animation
    with dissolve
    if voice_acted:
        $ renpy.sound.play(music.ck1.v14.Scene_3d_bj_slow_4loops, loop=True)

    u "*Moans* Satin... (If this is what being a \"nice guy\" gets you, then call me Mr. Nice Guy.)"

    stop sound
    scene v14satdtTPPf # Ignore as animation
    with dissolve
    if voice_acted:
        $ renpy.sound.play(music.ck1.v14.Scene_3d_bj_fast_4loops, loop=True)

    pause

    stop sound
    scene v14s03d_4c # FPP Same angle as 4, Satin doing a new sexy pose, her mouth open
    with dissolve

    satin "So, you're liking what you see?"

    scene v14s03d_4a
    with dissolve

    menu:
        "You get what you pay for":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            u "*Chuckles* Hey, you get what you pay for right?"

            scene v14s03d_4d # FPP Same angle as 4, Satin standing back looking offended, mouth open
            with dissolve

            satin "Umm, excuse me?"

            scene v14s03d_4e # FPP Same as 4d, Satin's mouth closed
            with dissolve

            u "What? I just mean- Like, you are a girl working at a brothel... So."

            scene v14s03d_4f # FPP Same angle as 4, Satin looks shocked and is covering herself with her clothes, mouth open
            with dissolve

            satin "I don't know what this sudden switch of personality is all about, but you're free to go."

            scene v14s03d_8 # FPP Show Satin getting dressed, she looks angry, mouth closed
            with dissolve

            u "I wasn't trying to offend you or anything I-"

            scene v14s03d_4g # FPP Same angle as 4, Satin, now dressed, looking at MC, angry with mouth open
            with dissolve

            satin "At this point, regardless of what you say, I'm not even in the mood."

            scene v14s03d_4h # FPP Same as 4g, Satin's mouth open
            with dissolve

            u "What? I'm sorry for-"

            scene v14s03d_4g
            with dissolve

            satin "Just! Leave! Okay?!"

            scene v14s03d_9 # TPP Satin throwing MC's clothes at him, she looks angry, mouth open
            with dissolve

            satin "I don't want to have to call security."

            scene v14s03d_9a # TPP Same angle as 9, MC now holding his clothes, looking ashamed, mouth open, Satin is pointing at the door, mouth closed
            with dissolve

            u "Fine, fine! Again, I'm sorry."

            scene v14s03d_10 # TPP Show MC getting dressed
            with dissolve

            pause 0.75

            scene v14s03d_11 # FPP MC's view as he leaves the room
            with dissolve

            u "(What the fuck is wrong with me?)"

        "Yes I do":
            u "Yes... I... do..."

            scene v14s03d_4i # FPP Same angle as 4, Satin leaning forward, her handson either side of MC's face, she's smiling with her mouth open, looking seductive
            with dissolve

            satin "*Chuckles* You're so fucking handsome..."

            # -Satin climbs on top of MC and starts riding him-
            scene v14s03d_12 # TPP Show Satin climbing onto MC to ride him
            with dissolve

            pause 0.75

            # From scene animations folder v14satcgTPP1
            image v14satcgTPP1 = Movie(play="images/v14/Scene 3d/v14satcgTPP1.webm", loop=True, image="images/v14/Scene 3d/v14satcgTPP1.webp", start_image="images/v14/Scene 3d/v14satcgTPP1.webp")
            image v14satcgTPP1f = Movie(play="images/v14/Scene 3d/v14satcgTPP1f.webm", loop=True, image="images/v14/Scene 3d/v14satcgTPP1.webp", start_image="images/v14/Scene 3d/v14satcgTPP1.webp")

            scene v14satcgTPP1 # Ignore as animation
            with dissolve
            if voice_acted:
                $ renpy.sound.play(music.ck1.v14.Scene_3d_cg_and_rcg_slow_4loops, loop=True)

            u "Oh f-fuck... You're soaking wet!"

            satin "*Moans* I guess having a nice guy for once is turning me on quite a bit."

            stop sound
            scene v14satcgTPP1f # Ignore as animation
            with dissolve
            if voice_acted:
                $ renpy.sound.play(music.ck1.v14.Scene_3d_cg_and_rcg_fast_8loops, loop=True)

            u "I... *Moans* Damn, Satin..."

            u "I can't even fucking concentrate right now..."

            # From scene animations folder v14satcgTPP2
            image v14satcgTPP2 = Movie(play="images/v14/Scene 3d/v14satcgTPP2.webm", loop=True, image="images/v14/Scene 3d/v14satcgTPP2.webp", start_image="images/v14/Scene 3d/v14satcgTPP2.webp")
            image v14satcgTPP2f = Movie(play="images/v14/Scene 3d/v14satcgTPP2f.webm", loop=True, image="images/v14/Scene 3d/v14satcgTPP2.webp", start_image="images/v14/Scene 3d/v14satcgTPP2.webp")

            stop sound
            scene v14satcgTPP2 # Ignore as animation
            with dissolve
            if voice_acted:
                $ renpy.sound.play(music.ck1.v14.Scene_3d_cg_and_rcg_slow_4loops, loop=True)

            satin "Ha! *Panting* You must be enjoying yourself."

            stop sound
            scene v14satcgTPP2f # Ignore as animation
            with dissolve
            if voice_acted:
                $ renpy.sound.play(music.ck1.v14.Scene_3d_cg_and_rcg_fast_8loops, loop=True)

            u "That's an understatement, baby."

            # -Satin stands, turns around and performs reverse cowgirl while MC is seated-
            stop sound
            scene v14s03d_12a # TPP Same angle as 12, Show Satin turning around to ride MC in reverse cowgirl
            with dissolve

            pause 0.75

            # From scene animations folder v14satrcgTPP1
            image v14satrcgTPP1 = Movie(play="images/v14/Scene 3d/v14satrcgTPP1.webm", loop=True, image="images/v14/Scene 3d/v14satrcgTPP1.webp", start_image="images/v14/Scene 3d/v14satrcgTPP1.webp")
            image v14satrcgTPP1f = Movie(play="images/v14/Scene 3d/v14satrcgTPP1f.webm", loop=True, image="images/v14/Scene 3d/v14satrcgTPP1.webp", start_image="images/v14/Scene 3d/v14satrcgTPP1.webp")

            scene v14satrcgTPP1 # Ignore as animation
            with dissolve
            if voice_acted:
                $ renpy.sound.play(music.ck1.v14.Scene_3d_cg_and_rcg_slow_4loops, loop=True)

            satin "*Moans* FUCK!"

            stop sound
            scene v14satrcgTPP1f # Ignore as animation
            with dissolve
            if voice_acted:
                $ renpy.sound.play(music.ck1.v14.Scene_3d_cg_and_rcg_fast_8loops, loop=True)

            u "Your body is so... goddamn perfect. Mmm!"

            # From scene animations folder v14satrcgTPP2
            image v14satrcgTPP2 = Movie(play="images/v14/Scene 3d/v14satrcgTPP2.webm", loop=True, image="images/v14/Scene 3d/v14satrcgTPP2.webp", start_image="images/v14/Scene 3d/v14satrcgTPP2.webp")
            image v14satrcgTPP2f = Movie(play="images/v14/Scene 3d/v14satrcgTPP2f.webm", loop=True, image="images/v14/Scene 3d/v14satrcgTPP2.webp", start_image="images/v14/Scene 3d/v14satrcgTPP2.webp")

            stop sound
            scene v14satrcgTPP2 # Ignore as animation
            with dissolve
            if voice_acted:
                $ renpy.sound.play(music.ck1.v14.Scene_3d_cg_and_rcg_slow_4loops, loop=True)

            satin "*Moans* Thank you, but... please... stop talking."

            u "(She wants me to just sit here?)"

            stop sound
            scene v14satrcgTPP2f # Ignore as animation
            with dissolve
            if voice_acted:
                $ renpy.sound.play(music.ck1.v14.Scene_3d_cg_and_rcg_fast_8loops, loop=True)

            satin "*Whispers* Ahh, yes! Fuck me... Will!"

            u "(Will?!)"

            stop sound
            scene v14s03d_13 # TPP Show satin standing in front of MC, holding his face in her hands and kissing him
            with dissolve

            pause 0.75

            scene v14s03d_13a # TPP Same angle as 13, Satin still holding MC's face, she is smiling at him with her mouth open
            with dissolve

            satin "Fuck me while I'm on my back."

            scene v14s03d_14 # TPP Show Satin laying on the bed on her stomach, smiling with her mouth open
            with dissolve

            satin "C'mon over here. What are you waiting for? *Chuckles*"

            scene v14s03d_14a # TPP Same angle as 14, MC climbing on top of Satin and getting ready to enter her, Satin's eyes closed, smiling with mouth open
            with dissolve

            satin "Now fuck me as hard as you can until you cum."

            scene v14s03d_15 # FPP Show Satin, face sideways on the bed, eyes and mouth closed
            with dissolve

            u "You want me to-"

            scene v14s03d_15a # FPP Same angle as 15, Satin is smiling with her eyes closed and mouth open
            with dissolve

            satin "Shhh..."

            scene v14s03d_15
            with dissolve

            u "Alright."

            scene v14s03d_16 # FPP Close up on MC's dick entering Satin in a prone position
            with dissolve

            satin "*Gasps* F-f-fuck!"

            scene v14s03d_15b # FPP Same angle as 15, Satin's eyes are closed she's biting her lower lip
            with dissolve

            u "You okay?"

            scene v14s03d_15a
            with dissolve

            satin "Yesss... *Moans* I'm fine."

            # -MC starts fucking Satin in prone position
            # From scene animations folder v14satbpTPP1
            image v14satbpTPP1 = Movie(play="images/v14/Scene 3d/v14satbpTPP1.webm", loop=True, image="images/v14/Scene 3d/v14satbpTPP1.webp", start_image="images/v14/Scene 3d/v14satbpTPP1.webp")
            image v14satbpTPP1f = Movie(play="images/v14/Scene 3d/v14satbpTPP1f.webm", loop=True, image="images/v14/Scene 3d/v14satbpTPP1.webp", start_image="images/v14/Scene 3d/v14satbpTPP1.webp")

            scene v14satbpTPP1 # Ignore as animation
            with dissolve
            if voice_acted:
                $ renpy.sound.play(music.ck1.v14.Scene_3d_backplank_slow_2loops, loop=True)

            satin "*Moans* So... fucking... good!"

            stop sound
            scene v14satbpTPP1f # Ignore as animation
            with dissolve
            if voice_acted:
                $ renpy.sound.play(music.ck1.v14.Scene_3d_backplank_fast_4loops, loop=True)

            satin "*Whisper* Fuck me, Will! Oh, yes... F-fuck..."

            u "(Will must be her boyfriend or something.)"

            # From scene animations folder v14satbpTPP2
            image v14satbpTPP2 = Movie(play="images/v14/Scene 3d/v14satbpTPP2.webm", loop=True, image="images/v14/Scene 3d/v14satbpTPP2.webp", start_image="images/v14/Scene 3d/v14satbpTPP2.webp")
            image v14satbpTPP2f = Movie(play="images/v14/Scene 3d/v14satbpTPP2f.webm", loop=True, image="images/v14/Scene 3d/v14satbpTPP2.webp", start_image="images/v14/Scene 3d/v14satbpTPP2.webp")

            stop sound
            scene v14satbpTPP2 # Ignore as animation
            with dissolve
            if voice_acted:
                $ renpy.sound.play(music.ck1.v14.Scene_3d_backplank_slow_2loops, loop=True)

            u "I'm... *Moans* I'm cumming... Fuckkk!"

            satin "Yes! Please... Cum in me!"

            stop sound
            scene v14satbpTPP2f # Ignore as animation
            with dissolve
            if voice_acted:
                $ renpy.sound.play(music.ck1.v14.Scene_3d_backplank_fast_4loops, loop=True)

            u "Mmm... AH I-, YES SATIN, YES!"

            stop sound
            scene v14s03d_16a # FPP Same angle as 16, MC cumming in Satin
            with dissolve

            pause

            scene v14s03d_15c # FPP Same angle as 15, Satin's eyes are open, she's smiling with her mouth open
            with dissolve

            satin "*Panting* That was amazing..."

            scene v14s03d_15d # FPP Same as 15c, Satin's mouth closed
            with dissolve

            u "I was thinking the same thing, ha."

            scene v14s03d_15c
            with dissolve

            satin "*Chuckles* Mind letting me up?"

            scene v14s03d_15d
            with dissolve

            u "If I have to... *Laughs*"

            stop music fadeout 3
            play music music.v14_Track_Scene_3d_2 fadein 2

            scene v14s03d_17 # TPP MC and Satin standing up, Satin looking at MC, looking embarrased with her mouth open
            with dissolve

            satin "I'm sorry that I kept asking you to be quiet..."

            scene v14s03d_18 # FPP MC looking at Satin, now standing. Satin looks embarrassed with her mouth open
            with dissolve

            satin "I just really have to put myself somewhere else mentally when I'm having sex."

            scene v14s03d_18a # FPP Same as 18, Satin's mouth closed
            with dissolve

            u "You mean think about Will?"

            scene v14s03d_18b # FPP Same angle as 18, Satin looks shocked, mouth open
            with dissolve

            satin "How do you know about Will?!"

            scene v14s03d_18c # FPP Same as 18b, mouth closed
            with dissolve

            u "You were whispering his name... *Laughs*"

            scene v14s03d_18d # FPP Same angle as 18, Satin has her face in her hands in embarrassment
            with dissolve

            satin "Oh my god... That's so embarrassing I-"

            u "It's fine, really. I get it."

            scene v14s03d_18e # FPP Same angle as 18, Satin looking at MC, she looks very sad, tears are filling up her eyes, mouth open
            with dissolve

            satin "I'm sorry..."

            scene v14s03d_18f # FPP Same as 18e, Satin's mouth closed
            with dissolve

            u "Really, it's fine-"

            scene v14s03d_18g # FPP Same angle as 18, Satin looking away, tears starting to stream down her face, mouth open
            with dissolve

            satin "I'm not trying to be mean, I just... I'm sorry, can you please go?"

            scene v14s03d_18h # FPP Same as 18g, Satin's mouth closed
            with dissolve

            u "Uh, yeah. I'll go."

            label v14s03d_nsfwSkipLabel1:

            scene v14s03d_10
            with dissolve

            pause 0.75

            scene v14s03d_11
            with dissolve

            u "(Well that didn't end exactly how I had imagined.)"

$ renpy.end_replay()
# -Regardless of choice scene continued
stop music fadeout 3
jump v14s03e # -Transition to Scene 3e