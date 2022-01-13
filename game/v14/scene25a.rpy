# SCENE 25a: Druggy Amber Sex
# Locations: Amber's house
# Characters: MC (Outfit: 9), AMBER (Outfit: 3)
# Time: Tuesday night

label v14s25a:
    # -Amber and MC remove their clothes, vision is a little foggy, maybe colored lights are going-
    scene v14s25a_1 # TPP Show MC and Amber removing their clothes
    with dissolve

    pause 0.75

    play music "music/v14/Track Scene 25a_1.mp3" fadein 2

    scene v14s25a_2 # FPP Show Amber, smiling with mouth closed, image should have foggy, trippy effects
    with dissolve

    u "*Drowsy* I'm so high... right now... Haha..."

    scene v14s25a_2a # FPP Same as 2, Amber's mouth open
    with dissolve

    am "*Drowsy* Ha, me too. *Moans*"

    scene v14s25a_2
    with dissolve

    u "*Drowsy* Get over here, you..."

    if config_censored:
        call screen censoredPopup("v14s25a_nsfwSkipLabel1")

    scene v14s25a_3 # TPP Show Amber landing on the bed, smiling with mouth open, MC with arms out as if he just threw her onto the bed
    with dissolve

    am "*Laughs* Wow! Okay, big guy..."

    scene v14s25a_4 # TPP Closer view of MC kissing Amber on the lips. Amber is laying on the bed with her arms back above her head
    with dissolve

    pause 0.75

    scene v14s25a_5 # TPP MC kissing Amber on her chest
    with dissolve

    pause 0.75
    
    scene v14s25a_6 # TPP MC kissing Amber near her belly button
    with dissolve

    pause 0.75

    scene v14s25a_7 # TPP MC kissing Amber at the top of her vulva, right where the split begins
    with dissolve

    am "*Moans*"

    scene v14s25a_8 # FPP Show Amber, eyes closed in pleasure, smiling with mouth open
    with dissolve

    am "Ssshitt... [name], stop teasing me..."

    scene v14s25a_8a # FPP Same as 8, Amber's mouth closed, biting her lower lip
    with dissolve

    u "What do you want then?"

    scene v14s25a_7a # TPP Same angle as 7, MC teasing Amber's clitoris with his finger
    with dissolve

    pause 0.75

    scene v14s25a_9 # TPP Show Amber arching her back in pleasure on the bed while MC teases her clitoris, Amber's mouth open
    with dissolve

    am "Fuck me, [name]. Please... *Moans* Fuck me!"

    scene v14s25a_10 # FPP MC's view as he gets on top of Amber and looks down as he puts his dick in her
    with dissolve

    pause 0.75

    # ANIMATION: Amber and MC fucking missionary in Amber's bed, Amber has her arms back behind her head
    image v14ambmFPP = Movie(play="images/v14/Scene 25a/v14ambmFPP.webm", loop=True, image="images/v14/Scene 25a/v14ambmFPP.webp", start_image="images/v14/Scene 25a/v14ambmFPP.webp")
    image v14ambmFPPf = Movie(play="images/v14/Scene 25a/v14ambmFPPf.webm", loop=True, image="images/v14/Scene 25a/v14ambmFPP.webp", start_image="images/v14/Scene 25a/v14ambmFPP.webp")

    scene v14ambmFPP # Missionary
    with dissolve
    if voice_acted:
        $ renpy.sound.play("music/v14/va/Scene 25a - bm_slow_4loops.mp3", loop=True)

    am "*Moans* It feels..."
  
    stop sound
    scene v14ambmFPPf # Missionary faster
    with dissolve
    if voice_acted:
        $ renpy.sound.play("music/v14/va/Scene 25a - bm_fast_4loops.mp3", loop=True)

    pause

    # ANIMATION: Mission angle 2
    image v14ambmTPP = Movie(play="images/v14/Scene 25a/v14ambmTPP.webm", loop=True, image="images/v14/Scene 25a/v14ambmTPP.webp", start_image="images/v14/Scene 25a/v14ambmTPP.webp")
    image v14ambmTPPf = Movie(play="images/v14/Scene 25a/v14ambmTPPf.webm", loop=True, image="images/v14/Scene 25a/v14ambmTPP.webp", start_image="images/v14/Scene 25a/v14ambmTPP.webp")

    stop sound
    scene v14ambmTPP # Missionary angle 2
    with dissolve
    if voice_acted:
        $ renpy.sound.play("music/v14/va/Scene 25a - bm_slow_4loops.mp3", loop=True)

    am "So much better..."

    stop sound
    scene v14ambmTPPf # Missionary angle 2 faster
    with dissolve
    if voice_acted:
        $ renpy.sound.play("music/v14/va/Scene 25a - bm_fast_4loops.mp3", loop=True)

    pause

    # ANIMATION: Butterfly position - Amber now has her legs over MC's shoulders, they're both close together
    image v14ambtbFPP = Movie(play="images/v14/Scene 25a/v14ambtbFPP.webm", loop=True, image="images/v14/Scene 25a/v14ambtbFPP.webp", start_image="images/v14/Scene 25a/v14ambtbFPP.webp")
    image v14ambtbFPPf = Movie(play="images/v14/Scene 25a/v14ambtbFPPf.webm", loop=True, image="images/v14/Scene 25a/v14ambtbFPP.webp", start_image="images/v14/Scene 25a/v14ambtbFPP.webp")

    stop sound
    scene v14ambtbFPP # Butterfly
    with dissolve
    if voice_acted:
        $ renpy.sound.play("music/v14/va/Scene 25a - tb_slow_4loops.mp3", loop=True)

    u "*Moans* Fuck..."

    stop sound
    scene v14ambtbFPPf # Butterly faster
    with dissolve
    if voice_acted:
        $ renpy.sound.play("music/v14/va/Scene 25a - tb_fast_4loops.mp3", loop=True)

    am "When you're... High, haha... Mmmmhh!"

    # ANIMATION: Butterly angle 2
    image v14ambtbTPP = Movie(play="images/v14/Scene 25a/v14ambtbTPP.webm", loop=True, image="images/v14/Scene 25a/v14ambtbTPP.webp", start_image="images/v14/Scene 25a/v14ambtbTPP.webp")
    image v14ambtbTPPf = Movie(play="images/v14/Scene 25a/v14ambtbTPPf.webm", loop=True, image="images/v14/Scene 25a/v14ambtbTPP.webp", start_image="images/v14/Scene 25a/v14ambtbTPP.webp")

    stop sound
    scene v14ambtbTPP # Butterfly angle 2
    with dissolve
    if voice_acted:
        $ renpy.sound.play("music/v14/va/Scene 25a - tb_slow_4loops.mp3", loop=True)

    u "Yes! You're so fucking amazing, Amber... Holy-"

    stop sound
    scene v14ambtbTPPf #Butterfly angle 2 faster
    with dissolve
    if voice_acted:
        $ renpy.sound.play("music/v14/va/Scene 25a - tb_fast_4loops.mp3", loop=True)

    am "Fffffffuck!"

    stop sound
    scene v14s25a_11 # TPP Amber now standing, pushing MC to sit down on the edge of the bed with his legs hanging off
    with dissolve

    pause 0.75

    # ANIMATION: MC now laying on the bed and Amber performing reverse cowgirl on him, MC's legs are hanging off the bed
    image v14ambrcgFPP = Movie(play="images/v14/Scene 25a/v14ambrcgFPP.webm", loop=True, image="images/v14/Scene 25a/v14ambrcgFPP.webp", start_image="images/v14/Scene 25a/v14ambrcgFPP.webp")
    image v14ambrcgFPPf = Movie(play="images/v14/Scene 25a/v14ambrcgFPPf.webm", loop=True, image="images/v14/Scene 25a/v14ambrcgFPP.webp", start_image="images/v14/Scene 25a/v14ambrcgFPP.webp")

    scene v14ambrcgFPP # Reverse cowgirl
    with dissolve
    if voice_acted:
        $ renpy.sound.play("music/v14/va/Scene 25a - rcg_slow_4loops.mp3", loop=True)

    am "*Gasps* Mmmh!"

    stop sound
    scene v14ambrcgFPPf # Reverse cowgirl faster
    with dissolve
    if voice_acted:
        $ renpy.sound.play("music/v14/va/Scene 25a - rcg_fast_4loops.mp3", loop=True)

    am "*Panting* Why ride a horse when you can ride a cowboy? *Laughs*"

    # ANIMATION: Reverse cowgirl angle 2
    image v14ambrcgTPP = Movie(play="images/v14/Scene 25a/v14ambrcgTPP.webm", loop=True, image="images/v14/Scene 25a/v14ambrcgTPP.webp", start_image="images/v14/Scene 25a/v14ambrcgTPP.webp")
    image v14ambrcgTPPf = Movie(play="images/v14/Scene 25a/v14ambrcgTPPf.webm", loop=True, image="images/v14/Scene 25a/v14ambrcgTPP.webp", start_image="images/v14/Scene 25a/v14ambrcgTPP.webp")

    stop sound
    scene v14ambrcgTPP # Reverse cowgirl angle 2
    with dissolve
    if voice_acted:
        $ renpy.sound.play("music/v14/va/Scene 25a - rcg_slow_4loops.mp3", loop=True)

    u "*Moans* Haha... Ride 'em cowgirl..."

    stop sound
    scene v14ambrcgTPPf # Reverse cowgirl angle 2 faster
    with dissolve
    if voice_acted:
        $ renpy.sound.play("music/v14/va/Scene 25a - rcg_fast_4loops.mp3", loop=True)

    pause

    stop sound
    scene v14s25a_11a # TPP Same angle as 11, Amber on MC in reverse cowgirl position, waving her hand in the air like a bull rider, mouth open
    with dissolve

    am "WOOHOO!!! *Moans* Oh... Fuck, [name]..."

    scene v14s25a_11b # TPP Same as 11a, Amber's mouth closed
    with dissolve

    u "(Damn, girl...)"

    scene v14s25a_12 # FPP Amber standing in front of MC, who is sitting on the bed. Amber's mouth open
    with dissolve

    am "I wanna catch your cum in my mouth..."

    scene v14s25a_12a # FPP Same as 12, Amber's mouth closed
    with dissolve

    u "Let's do it, then."

    scene v14s25a_13 # TPP Amber gets onto her knees on the ground with her mouth open, MC stands in front of her with his dick in his hand
    with dissolve

    pause 0.75

    # ANIMATION: Amber on her knees, in front of MC, with her mouth open, MC jerking off, getting ready to cum in her mouth (they are about 3 feet apart)
    image v14ambjoFPP = Movie(play="images/v14/Scene 25a/v14ambjoFPP.webm", loop=True, image="images/v14/Scene 25a/v14ambjoFPP.webp", start_image="images/v14/Scene 25a/v14ambjoFPP.webp")
    image v14ambjoFPPf = Movie(play="images/v14/Scene 25a/v14ambjoFPPf.webm", loop=True, image="images/v14/Scene 25a/v14ambjoFPP.webp", start_image="images/v14/Scene 25a/v14ambjoFPP.webp")

    scene v14ambjoFPP # Jerkoff
    with dissolve
    if voice_acted:
        $ renpy.sound.play("music/v14/va/Scene 25a - jo_slow_4loops.mp3", loop=True)

    am "AHHHH!"

    stop sound
    scene v14ambjoFPPf # Jerkoff faster
    with dissolve
    if voice_acted:
        $ renpy.sound.play("music/v14/va/Scene 25a - jo_fast_4loops.mp3", loop=True)

    u "*Whispers* All he had to do was aim..."

    # ANIMATION: Jerkoff angle 2
    image v14ambjoTPP = Movie(play="images/v14/Scene 25a/v14ambjoTPP.webm", loop=True, image="images/v14/Scene 25a/v14ambjoTPP.webp", start_image="images/v14/Scene 25a/v14ambjoTPP.webp")
    image v14ambjoTPPf = Movie(play="images/v14/Scene 25a/v14ambjoTPPf.webm", loop=True, image="images/v14/Scene 25a/v14ambjoTPP.webp", start_image="images/v14/Scene 25a/v14ambjoTPP.webp")

    stop sound
    scene v14ambjoTPP # Jerkoff angle 2
    with dissolve
    if voice_acted:
        $ renpy.sound.play("music/v14/va/Scene 25a - jo_slow_4loops.mp3", loop=True)

    u "Oh shittttt! It's coming..."

    u "I'm cumming, Amb-."

    stop sound
    scene v14ambjoTPPf # Jerkoff angle 2 faster
    with dissolve
    if voice_acted:
        $ renpy.sound.play("music/v14/va/Scene 25a - jo_fast_4loops.mp3", loop=True)

    u "AHH! *Moans*"

    stop sound
    scene v14s25a_14 # FPP MC cumming, most going into Amber's mouth, a bit on her face
    with dissolve

    pause 0.75

    scene v14s25a_14a # FPP Same angle as 14, Amber closing her mouth and swallowing
    with dissolve

    pause 0.75

    scene v14s25a_14b # FPP Same angle as 14, Amber's mouth open, now empty, smiling
    with dissolve

    am "Fuck, yes!"

    scene v14s25a_15 # FPP Amber sucking MC's dick clean
    with dissolve

    am "Mmm..."

    scene v14s25a_15a # FPP Same angle as 15, Amber getting the last of MC's cum into her mouth with her finger
    with dissolve

    u "Ha... Oh-oh, thank you."

    scene v14s25a_16 # TPP Amber standing up now, pushing MC back onto the bed
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v13/Track Scene 16a_2.mp3" fadein 2

    scene v14s25a_17 # TPP Show Amber laying on the bed next to MC, her mouth open
    with dissolve

    am "*Panting* After a night like that, you have to stay here. We're high as fuck! *Laughs*"

    scene v14s25a_18 # FPP MC's view of Amber, who is laying close to him on the bed, mouth closed
    with dissolve

    u "Whoa, I can't even feel my fingers..."

    scene v14s25a_18a # FPP Same as 18, Amber's mouth open
    with dissolve

    am "When you're high like this, it always feels good to just stop moving and let yourself float in time until you pass out."

    scene v14s25a_17a # TPP Same angle as 17, MC's eyes closed, about to pass out. Amber's mouth open
    with dissolve

    am "[name]? [name]? What are you doing?"

    scene v14s25a_18
    with dissolve

    u "I'm letting myself pass out..."

    scene v14s25a_18a
    with dissolve

    am "Oh, yeahhhh... I'm so stupid, I forgot what I just said to you. *Laughs* Goodnight."

    #scene v14s25a_17b # TPP Same angle as 17, show MC and Amber sleeping together in some weird position - something that would only be comfortable when you're high
    #with dissolve

    #pause 1.25

    $ renpy.end_replay()

    label v14s25a_nsfwSkipLabel1:

    scene black
    with fade
    
    pause 0.75

    stop music fadeout 3

    jump v14s25b # -Transition to Scene 25b-