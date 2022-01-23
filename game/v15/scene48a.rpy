# SCENE 48a: Nora sex scene
# Locations: Nora's Cabin
# Characters: NORA (Outfit: 1/Naked), MC (Outfit: 1/Naked)
# Time: Evening

label v15s48a:
    label v15s48a_norasg:

    play music "music/v15/Track Scene 48a.mp3" fadein 2

    $ sceneList.add("v15_nora")
    
    scene v15s48a_1 # TPP. Show Nora sitting down next to MC, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s48a_2 # FPP. Nora sitting on the couch next to MC, MC looking at Nora, Nora looking at MC, Nora smile, mouth open.
    with dissolve

    no "Thank you, [name]. For everything."

    scene v15s48a_2a # FPP. MC looking at Nora, Nora looking at MC, Nora smile, mouth closed.
    with dissolve

    u "Nora-"

    scene v15s48a_2
    with dissolve

    no "Seriously. You've always been there for me."

    no "Chris literally left me at the altar... and you were the only one who stepped up for me."

    no "It took you just a few seconds to stand up and take his place."

    if v12s16_kissnora:
        no "And who can forget that kiss?"

    scene v15s48a_2a
    with dissolve

    u "(Damn straight.)"

    if v10_help_nora_freeroam:
        $ v15s48a_norapoints += 1
        
        scene v15s48a_2
        with dissolve

        no "I mean, you helped me get people signed up for the Europe trip. And I didn't even have to ask."

    if v10_cheerfornora:
        $ v15s48a_norapoints += 1
        
        scene v15s48a_2
        with dissolve

        no "You cheered me on from the side-lines when I wrestled Chloe..."

        scene v15s48a_2a
        with dissolve

        u "Oh, that was nothing."

        scene v15s48a_2
        with dissolve

        no "Haha, yeah, I'm sure you enjoyed the big finale that day!"

        scene v15s48a_2a
        with dissolve

        u "*Laughs* I can't lie to you... Actually, no- I could, but I'm choosing not to."

        scene v15s48a_2
        with dissolve

        no "*Giggles*"

    if not v12_chase_robber:
        $ v15s48a_norapoints += 1
        
        scene v15s48a_2
        with dissolve

        no "When I got robbed in Europe, your first instinct was to make sure that I was okay."

    if v12_fight_win:
        $ v15s48a_norapoints += 1
        
        scene v15s48a_2
        with dissolve

        no "When my purse got stolen in Europe-"

        scene v15s48a_2a
        with dissolve

        u "Almost... Got stolen."

        scene v15s48a_2
        with dissolve

        no "*Chuckles* Almost because you kicked the guy's ass."

        scene v15s48a_2a
        with dissolve

        u "Of course, I did."

    if v12_followed_nora:
        $ v15s48a_norapoints += 1
        
        scene v15s48a_2
        with dissolve

        no "You didn't hesitate to choose me over \"the boys\"."

    scene v15s48a_2b # FPP. Nora leaning in closer to MC's face, Nora looking at MC, MC looking at Nora, Nora flirty, mouth open.
    with dissolve

    if v15s48a_norapoints > 1:
        no "I just can't believe how much time I've wasted without you, ha."

        no "It's been you all along."

    else:
        no "I just can't believe how much time I've wasted without you, ha."

    scene v15s48a_2c # FPP. Nora leaning in closer to MC's face, Nora looking at MC, MC looking at Nora, Nora biting her lip.
    with dissolve

    u "Well, we're here now."

    scene v15s48a_2b
    with dissolve

    no "Honestly, since the moment we met, you've made me feel... wanted."

    scene v15s48a_2c
    with dissolve

    menu:
        "You are wanted":
            $ add_point(KCT.BOYFRIEND)
            u "You are..."

            scene v15s48a_3 # TPP. MC kissing Nora's right cheek.
            with dissolve
            play sound "sounds/kiss.mp3"

            u "completely..."

            scene v15s48a_4 # TPP. MC kissing Nora's left cheek.
            with dissolve
            play sound "sounds/kiss.mp3"

            u "and utterly..."

            scene v15s48a_2d # FPP. MC kissing Nora
            with dissolve

            pause 1.25

            scene v15s48a_5 # TPP. Show MC and Nora kissing.
            with dissolve
            play sound "sounds/kiss.mp3"

            pause 1.25

            scene v15s48a_2c
            with dissolve

            u "wanted."

            scene v15s48a_2e # FPP. Nora still leaned in close to MC, MC looking at Nora, Nora looking at MC, Nora blushing, Nora smile, mouth open.
            with dissolve

            no "You are too..."

        "Just kiss her":
            $ add_point(KCT.BRO)

            scene v15s48a_2d
            with dissolve
            play sound "sounds/kiss.mp3"

            pause 1.25

            scene v15s48a_5
            with dissolve

            pause 1.25

            scene v15s48a_2b
            with dissolve

            no "It's about damn time. *Chuckles*"

            scene v15s48a_2c
            with dissolve

            u "I couldn't wait any longer."

            scene v15s48a_2b
            with dissolve

            no "Then don't."

    scene v15s48a_6 # TPP. Show MC and Nora kissing romantically on the couch with the fireplace with a fire in the shot.
    with dissolve

    play sound "sounds/kiss.mp3"

    pause 1.25

    if config_censored:
        call screen censored_popup("v15s48a_nsfwSkipLabel1")

    scene v15s48a_7 # TPP. Closer up of MC and Nora, MC taking off Nora's shirt her boobs out, Nora's face obscured by her shirt, MC slight smile, mouth closed.
    with dissolve

    pause 1.25

    scene v15s48a_7a # TPP. MC and Nora kissing, Nora is topless.
    with dissolve

    play sound "sounds/kiss.mp3"

    pause 1.25

    scene v15s48a_7b # TPP. Nora taking of MC's shirt, MC's face obscured by his shirt, Nora flirty, mouth closed.
    with dissolve

    pause 1.25

    scene v15s48a_7c # TPP. MC and Nora kissing, both topless.
    with dissolve

    play sound "sounds/kiss.mp3"

    pause 1.25
    
    scene v15s48a_8 # TPP. Nora laying on the couch fully nude, Nora's full body in the shot, Nora biting her lip.
    with fade

    pause 0

    $ sex_overlay_options = [
        [("Boobs", "v15s48a_boobs"), ("Feet", "v15s48a_feet"), ("Vagina", "v15s48a_vagina")],
    ]
    call screen sex_overlay("v15s48a_end")

label v15s48a_boobs:
    scene v15s48abo_1 # TPP. Close up of Nora's boobs as she lays on her back on the couch.
    with dissolve

    menu:
        "Massage":
            scene v15s48abo_2 # TPP. Show MC massaging Nora's boobs, MC slight smile, mouth closed, Nora flirty, mouth open.
            with dissolve

            no "Mmm, that feels so nice."

            scene v15s48abo_3 # FPP. MC looking down at Nora's boobs as he is massaging them.
            with dissolve

            u "Good. I'm doing the right thing, then."

            scene v15s48abo_4 # FPP. MC looking at Nora's face, MC's hand on her boobs still in shot, Nora flirty, mouth open.
            with dissolve

            no "You're so... attentive."

            scene v15s48abo_4a # FPP. MC looking at Nora's face, his hand massaging her boobs a different way, Nora biting her lip.
            with dissolve

            u "I just want to touch you; I want to feel every part of you."

            u "I want to make you feel good."

            scene v15s48abo_4
            with dissolve

            no "You're doing a really good job so far... *Giggles*"

        "Suck":
            scene v15s48abo_5 # TPP. MC sucking on Nora's right boob, Nora's face in shot, Nora flirty, mouth open.
            with dissolve

            no "*Gasps* Oh!"

            scene v15s48abo_6 # FPP. MC looking up at Nora her boobs in his face, Nora looking at MC, Nora biting her lip.
            with dissolve

            u "Do you like that?"

            scene v15s48abo_5
            with dissolve

            no "Of course I do..."

            no "You make me feel special, you know?"

            no "*Moans* You're so good to me."

            scene v15s48abo_6
            with dissolve

            u "Oh, come on... This is a pleasure."

            u "I could play with you all night."

            scene v15s48abo_5a # TPP. MC sucking on Nora's left boob, Nora's face in shot, Nora flirty, mouth open.
            with dissolve

            no "Mmm, not before I get to your dick."

            scene v15s48abo_6
            with dissolve

            u "Yeah?"

            scene v15s48abo_5
            with dissolve

            no "Then we'll see how horny you are."

            scene v15s48abo_6
            with dissolve

            u "Hmm, I guess we will."

    $ sex_overlay_options = [
        [("Boobs", "v15s48a_boobs"), ("Feet", "v15s48a_feet"), ("Vagina", "v15s48a_vagina")],
    ]
    call screen sex_overlay("v15s48a_end")

label v15s48a_feet:
    scene v15s48afe_1 # TPP. Close up of Nora's feet.
    with dissolve

    menu:
        "Massage":
            scene v15s48afe_2 # TPP. Show MC massaing Nora's feet, Nora flirty, mouth open.
            with dissolve

            no "Oh, [name]. Nobody's ever massaged my feet before."

            scene v15s48afe_3 # FPP. MC looking up at Nora, Nora biting her lip.
            with dissolve

            u "Do you like it?"

            scene v15s48afe_4 # FPP. MC massaing Nora's feet.
            with dissolve

            no "I love it."

            no "As long as your hands are touching me, I'm loving it. *Giggles*"

            scene v15s48afe_3
            with dissolve

            u "Good, because I love exploring your body."

            u "I can't wait to worship every inch of it."

        "Suck":
            scene v15s48afe_5 # TPP. Show MC sucking on Nora's big toe, Nora flirty, mouth open.
            with dissolve

            no "Oh! Fuck, [name]!"

            no "I didn't know you had a foot kink."

            scene v15s48afe_3
            with dissolve

            u "I'm full of surprises."

            scene v15s48afe_5a # TPP. Show MC sucking on a different toes, Nora flirty, mouth open.
            with dissolve

            no "Mmm, obviously."

            no "I've never had..."

            no "Oh!"

            no "My toes sucked before."

            scene v15s48afe_6 # TPP. Show MC kissing Nora's foot, Nora flirty, mouth open.
            with dissolve

            play sound "sounds/kiss.mp3"

            no "I think it's my new favorite thing."

            no "But I have a lot of favorites when it comes to sex..."

            scene v15s48afe_3
            with dissolve

            u "And I can't wait to find out what they are."

    $ sex_overlay_options = [
        [("Boobs", "v15s48a_boobs"), ("Feet", "v15s48a_feet"), ("Vagina", "v15s48a_vagina")],
    ]
    call screen sex_overlay("v15s48a_end")

label v15s48a_vagina:
    scene v15s48ava_1 # FPP. MC looking at Nora's vagina.
    with dissolve

    menu:
        "Tease with kissing":
            scene v15s48ava_2 # TPP. Show MC kissing Nora's inner thigh, Nora flirty, mouth open.
            with dissolve

            play sound "sounds/kiss.mp3"

            no "*Gasps*"

            no "You're such a fucking tease!"

            scene v15s48ava_3 # FPP. MC looking up at Nora, Nora biting her lip.
            with dissolve

            u "I want to make you feel good, but I'm still going to have some fun."

            scene v15s48ava_2a # TPP. Show MC kissing closer to Nora's vagina, Nora flirty, mouth open.
            with dissolve

            play sound "sounds/kiss.mp3"

            no "God, you're such a fucking turn on."

            scene v15s48ava_3
            with dissolve

            u "Haha, am I?"

            scene v15s48ava_2a
            with dissolve

            no "Just fuck me already."

        "Finger":
            scene v15s48ava_4 # FPP. MC looking at Nora his two fingers barely in her vagina, Nora flirty, mouth open.
            with dissolve

            no "Oh, [name]..."

            no "*Moans*"

            scene v15s48ava_4a # FPP. MC's two fingers all the way in Nora's vagina, Nora biting her lip.
            with dissolve

            u "You like that?"

            scene v15s48ava_4
            with dissolve

            no "Mmm, yeah... I do. But it's not what I want..."

            no "And you know it."

            scene v15s48ava_4a
            with dissolve

            u "Yeah? What do you want, Nora?"

            scene v15s48ava_4
            with dissolve

            no "Quit teasing!"

            scene v15s48ava_4b # FPP. MC's two fingers barely in Nora's vagina, Nora biting her lip.
            with dissolve

            pause 0.75

            scene v15s48ava_4a
            with dissolve

            pause 0.75

            scene v15s48ava_4b
            with dissolve

            pause 0.75

            scene v15s48ava_4a
            with dissolve

            u "Tell me what you want."

            scene v15s48ava_4
            with dissolve

            no "I want to feel you..."

            no "*Moans* Fuck me, [name]..."

            no "Oh, [name]. Please..."

    $ sex_overlay_options = [
        [("Boobs", "v15s48a_boobs"), ("Feet", "v15s48a_feet"), ("Vagina", "v15s48a_vagina")],
    ]
    call screen sex_overlay("v15s48a_end")

label v15s48a_end:
# -Clicking on Nora's mouth-
# -The option appears to end the free roam and move onto the sex animations-
# -End of free roam-

    scene v15s48aend_1 # FPP. MC hover over Nora on the couch, Nora looking at MC, MC looking at Nora, Nora biting her lip.
    with dissolve

    u "You want this dick now?"

    scene v15s48aend_1a # FPP. Nora looking at MC, MC looking at Nora, Nora flirty, mouth open.
    with dissolve

    no "More than anything."

    scene v15s48aend_1
    with dissolve

    u "Then come get it."

    scene v15s48aend_1a
    with dissolve

    no "Gladly. *Giggles*"
    
    scene v15s48a_98
    with dissolve
    
    pause 0.75

    image v15norbj = Movie(play="images/v15/Scene 48a/v15norbj.webm", loop=True, image="images/v15/Scene 48a/v15norbjStart.webp", start_image="images/v15/Scene 48a/v15norbjStart.webp")
    image v15norbjf = Movie(play="images/v15/Scene 48a/v15norbjf.webm", loop=True, image="images/v15/Scene 48a/v15norbjStart.webp", start_image="images/v15/Scene 48a/v15norbjStart.webp")
    image v15norbj2 = Movie(play="images/v15/Scene 48a/v15norbj2.webm", loop=True, image="images/v15/Scene 48a/v15norbj2Start.webp", start_image="images/v15/Scene 48a/v15norbj2Start.webp")
    image v15norbj2f = Movie(play="images/v15/Scene 48a/v15norbj2f.webm", loop=True, image="images/v15/Scene 48a/v15norbj2Start.webp", start_image="images/v15/Scene 48a/v15norbj2Start.webp")

    scene v15norbj # Ignore as anim
    with dissolve

    if voice_acted:
        $ renpy.sound.play("voice/v15/s48a/Scene 48a - bj_slow_2loops.mp3", loop=True)

    pause 0.75

    u "Ah, fuck... yeah."

    u "Wow, you REALLY want it!"

    scene v15norbj2 # Ignore as anim
    with dissolve

    pause 0.75

    no "Mhmm!"

    no "*Gagging*"

    scene v15norbjf # Ignore as anim
    with dissolve

    if voice_acted:
        $ renpy.sound.play("voice/v15/s48a/Scene 48a - bj_fast_2loops.mp3", loop=True)

    pause 0.75

    u "*Moans* Ssssshit Nora, you really know what you're doing."

    scene v15norbj2f # Ignore as anim
    with dissolve

    pause 0.75

    u "I'm not going to last much longer if you keep that up..."

    stop sound

    scene v15s48aend_2 # TPP. MC leading Nora over to the window, both naked, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s48aend_3 # TPP. MC pushing Nora's back towards the window, the window has a nice view with moonlight and stars and the forest, Nora biting her lip.
    with dissolve

    pause 0.75

    scene v15s48aend_3a # TPP. MC getting on his knees. While Nora stands with her back to the window, Nora biting her lip.
    with dissolve

    pause 0.75

    image v15noror = Movie(play="images/v15/Scene 48a/v15noror.webm", loop=True, image="images/v15/Scene 48a/v15nororStart.webp", start_image="images/v15/Scene 48a/v15nororStart.webp")
    image v15noror2 = Movie(play="images/v15/Scene 48a/v15noror2.webm", loop=True, image="images/v15/Scene 48a/v15noror2Start.webp", start_image="images/v15/Scene 48a/v15noror2Start.webp")

    scene v15noror # Ignore as anim 
    with dissolve

    if voice_acted:
        $ renpy.sound.play("voice/v15/s48a/Scene 48a - oral_slow_2loops.mp3", loop=True)

    pause 0.75

    no "Oh... Fuck!"

    no "*Panting* I've never felt this good before, [name]."

    stop sound

    scene v15s48aend_4 # FPP. MC looking up at Nora from on his knees, Nora looking down at MC, Nora biting her lip.
    with dissolve

    menu:
        "You deserve it":
            u "You do deserve the best, you know."

            scene v15s48aend_4a # FPP. MC looking up at Nora, Nora looking down at MC, Nora flirty, mouth open.
            with dissolve

            no "Ha, I guess..."

        "Get used to it":
            scene v15s48aend_4
            #with dissolve
            
            u "Good, get used to it."

            scene v15s48aend_4a
            with dissolve

            no "Ha! Should I?"

    no "Mmm..."

    scene v15s48aend_4
    with dissolve

    u "You're so fucking wet, Nora."

    scene v15noror2 # Ignore as anim
    with dissolve

    if voice_acted:
        $ renpy.sound.play("voice/v15/s48a/Scene 48a - oral_slow_2loops.mp3", loop=True)


    pause 0.75

    no "*Moans* Yeah?"

    u "You taste incredible..."

    no "Mhmm... Right..."

    no "You..."

    no "Y-you have to fuck me."

    stop sound

    scene v15s48aend_4
    with dissolve

    u "Do I?"

    scene v15s48aend_5 # TPP. MC standing back up now and turning Nora around so her chest faces the window, Nora shocked, mouth closed, MC cheeky smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s48aend_5a # TPP. MC pushing Nora against the window Nora's boobs pressed against the window.
    with dissolve

    pause 0.75

    scene v15s48aend_6 # TPP. (Only if this is possible) Shot of the window from outside with Nora's boobs pressed up against the glass, MC standing behind her.
    with dissolve

    pause 0.75

    scene v15s48aend_5b # TPP. Nora's face not shown, MC behind Nora with his hands on her hips as she is pressed against the window.
    with dissolve

    no "*Giggles* Got me where you want me?"

    u "For now."

    image v15norsdg = Movie(play="images/v15/Scene 48a/v15norsdg.webm", loop=True, image="images/v15/Scene 48a/v15norsdgStart.webp", start_image="images/v15/Scene 48a/v15norsdgStart.webp")
    image v15norsdgf = Movie(play="images/v15/Scene 48a/v15norsdgf.webm", loop=True, image="images/v15/Scene 48a/v15norsdgStart.webp", start_image="images/v15/Scene 48a/v15norsdgStart.webp")
    image v15norsdg2 = Movie(play="images/v15/Scene 48a/v15norsdg2.webm", loop=True, image="images/v15/Scene 48a/v15norsdg2Start.webp", start_image="images/v15/Scene 48a/v15norsdg2Start.webp")
    image v15norsdg2f = Movie(play="images/v15/Scene 48a/v15norsdg2f.webm", loop=True, image="images/v15/Scene 48a/v15norsdg2Start.webp", start_image="images/v15/Scene 48a/v15norsdg2Start.webp")

    scene v15norsdg # Ignore as anim 
    with dissolve

    if voice_acted:
        $ renpy.sound.play("voice/v15/s48a/Scene 48a - sdg_slow_2loops.mp3", loop=True)

    pause 0.75

    no "*Gasps*"

    u "*Groans*"

    scene v15norsdg2 # Ignore as anim 
    with dissolve
    
    pause 0.75

    no "Oh, shit!"

    scene v15norsdgf # Ignore as anim 
    with dissolve

    if voice_acted:
        $ renpy.sound.play("voice/v15/s48a/Scene 48a - sdg_fast_2loops.mp3", loop=True)

    pause 0.75

    u "You feel amazing, Nora..."

    scene v15norsdg2f # Ignore as anim
    with dissolve

    pause 0.75

    no "You... *Moans* Too..."

    stop sound

    scene v15s48aend_5c # TPP. Nora turned back around, Nora looking at MC, Nora biting her lip.
    with dissolve

    pause 0.75

    scene v15s48aend_7 # TPP. Close up of Nora's hand grabbing MCs.
    with dissolve

    pause 0.75

    scene v15s48aend_8 # TPP. Show Nora leading MC up the stairs to the bedroom by his hand, MC slight smile, mouth closed, Nora biting her lip.
    with dissolve

    pause 0.75

    scene v15s48aend_9 # TPP. MC and Nora standing by the bed upstairs, MC slight smile, Nora biting her lip.
    with fade

    pause 0.75

    scene v15s48aend_9a # TPP. MC picking up Nora, Nora surprised, mouth open.
    with dissolve

    no "Oooh... You're so strong, hehe."

    scene v15s48aend_9b # TPP. MC carrying Nora, Nora sitting on his dick with her legs wrapped around him, Nora flirty, mouht open.
    with dissolve

    no "Oh- fuck!"

    scene v15s48aend_9c # TPP. MC carrying Nora, Nora sitting on his dick with her legs wrapped around him, Nora biting her lip.
    with dissolve

    u "Too rough?"

    scene v15s48aend_9b
    with dissolve

    no "Ha! Too rough? Is that a thing?"

    scene v15s48aend_10 # TPP. Show MC and Nora falling onto the bed while her legs are still wrapped around him.
    with dissolve

    pause 0.75

    image v15normis = Movie(play="images/v15/Scene 48a/v15normis.webm", loop=True, image="images/v15/Scene 48a/v15normisStart.webp", start_image="images/v15/Scene 48a/v15normisStart.webp")
    image v15normisf = Movie(play="images/v15/Scene 48a/v15normisf.webm", loop=True, image="images/v15/Scene 48a/v15normisStart.webp", start_image="images/v15/Scene 48a/v15normisStart.webp")
    image v15normis2 = Movie(play="images/v15/Scene 48a/v15normis2.webm", loop=True, image="images/v15/Scene 48a/v15normis2Start.webp", start_image="images/v15/Scene 48a/v15normis2Start.webp")
    image v15normis2f = Movie(play="images/v15/Scene 48a/v15normis2f.webm", loop=True, image="images/v15/Scene 48a/v15normis2Start.webp", start_image="images/v15/Scene 48a/v15normis2Start.webp")

    scene v15normis # Ignore as anim
    with dissolve

    if voice_acted:
        $ renpy.sound.play("voice/v15/s48a/Scene 48a - missionary_slow_2loops.mp3", loop=True)

    pause 0.75

    no "Oh my- *Moans*"

    no "Harder, [name]. Please!"

    scene v15normis2 # Ignore as anim
    with dissolve

    pause 0.75

    u "You like that?"

    no "I... love that... Yes!"

    scene v15normisf # Ignore as anim
    with dissolve

    if voice_acted:
        $ renpy.sound.play("voice/v15/s48a/Scene 48a - missionary_fast_2loops.mp3", loop=True)

    pause 0.75

    no "*Whispers* You're so sexy, [name]..."

    u "I'm so close, I-"

    no "*Panting* Me too... Don't... Stop..."

    scene v15normis2f # Ignore as anim
    with dissolve

    pause 0.75

    u "I'm... *Moans* Nora-"

    no "Yes, baby..."

    stop sound

    scene v15s48aend_11 # FPP. MC and Nora in missionairy on the bed, MC close to her face, MC looking at Nora, Nora looking at MC, Nora with her hand on MC's cheek, Nora flirty, mouth open.
    with dissolve

    no "Cum in me."

    scene v15s48aend_11a # FPP. MC looking at Nora, Nora looking at MC, Nora with her hand on MC's cheek, Nora biting her lip.
    with dissolve

    u "Wha- Nora, I-"

    scene v15s48aend_11
    with dissolve

    no "*Whispers* Please..."

    scene v15s48aend_11a
    with dissolve

    u "Ahhh... (Fuck!)"

# -Timed Event
    menu (fail_label="v15s48a_cum"):
        "Cum inside Nora":
            label v15s48a_cum:
            
            $ v15_nora_cum = True
        
            scene v15s48aend_11a
            with vpunch

            u "*Groans* Mmm..."

            scene v15s48aend_11
            with dissolve

            no "I'm- I... *Moans* Yes, [name]..."

        "Pull out":
            u "(No. Fucking. Thank you.)"

            scene v15s48aend_12 # FPP. MC looking down at his dick inside of Nora as he is pulling it out.
            with dissolve

            pause 0.75

            scene v15s48aend_12a # FPP. MC's dick no longer in Nora
            with dissolve

            pause 0.75

            scene v15s48aend_13 # FPP. MC cumming on Nora's stomach, Nora biting her lip.
            with vpunch

            u "*Groans* Fuck..."

            scene v15s48aend_11b # Nora's hand no longer on MC's cheek, Nora slightly dissapointed, mouth open.
            with dissolve

            no "But-"

            scene v15s48aend_11c # Nora's hand no longer on MC's cheek, Nora slightly dissapointed, mouth closed.
            with dissolve

            u "I'm sorry."

            scene v15s48aend_15 # FPP. On the bed, MC's two fingers barely in Nora's vagina, Nora biting her lip.
            with dissolve

            pause 0.75

            scene v15s48aend_15a # FPP. On the bed, MC's two fingers all the way in Nora's vagina, Nora biting her lip.
            with dissolve

            pause 0.75
            
            scene v15s48aend_15
            with dissolve

            pause 0.75

            scene v15s48aend_15a
            with dissolve

            pause 0.75

            scene v15s48aend_15c # FPP. On the bed, MC's two fingers all the way in Nora's vagina, Nora flirty, mouth open.
            with vpunch

            no "Oh- *Moans* [name]... *Gasps*"

    scene v15s48aend_16 # FPP. Nora and MC both laying on the bed Nora on her side looking at MC, MC looking at Nora, Nora biting her lip.
    with dissolve

    u "*Panting*"

    scene v15s48aend_16a # FPP. Nora and MC both laying on the bed Nora on her side looking at MC, Nora slight smile, mouth open.
    with dissolve

    no "*Panting*"

    scene v15s48aend_16
    with dissolve

    u "That was-"

    scene v15s48aend_16b # FPP. Nora looking at MC, MC looking at Nora, Nora flirty, mouth open.
    with dissolve

    no "No, you are."

    stop music fadeout 3

    play music "music/v15/Track Scene 48b.mp3" fadein 2

    jump v15s48b