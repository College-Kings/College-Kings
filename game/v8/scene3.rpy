### SCENE 3: v7 Riley romance ending continued
label v8_ri_start:
    # Note to renderers: Make sure the MC is in his suit and Riley is in her HoCo dress. Any other props are the same as Riley's lewd ending in v7. Context: MC and Riley are both sitting on her bed in her room and she's whispering in his ear
    stop music fadeout 3

    $ sceneList.add("v8_riley")
    $ CharacterService.set_relationship(riley, Relationship.FWB)
    $ CharacterService.remove_mood(riley, Moods.TEASED)

    scene v8s25 # Same as sfr4ri55 (from v7) but MC talking now
    with dissolve
    u "Mhm... Tell me more."

    if is_censored:
        call screen censored_popup("v8s3_nsfwSkipLabel1")

    scene v8s26 # FPP (MC still sitting on the bed). Riley stands up and is looking into the camera and talking seductively, about to take her dress off. She should be visible at least down until her knees
    with dissolve
    ri "I'd rather show you instead."

    play music music.ck1.sexy ###CHECK - Maybe add more sexy time music?

    scene v8s26a # Riley's dress is off now. She's wearing a sexy red lingerie underneath and showing off her body, seductive expression and mouth closed
    with fade
    pause

    scene v8s26b # Same as v8s26a but Riley mouth open
    with dissolve
    ri "You like it?"

    scene v8s26a
    with dissolve
    u "A pretty red-head in a sexy red lingerie?"
    u "I say Christmas came early this year!"

    scene v8s26b
    with dissolve
    ri "*Chuckles* Why don't you start unwrapping your present fully then?"

    if "v7_riley" in sceneList:
        u "(Damn, did not expect Riley had this in her.)"

    scene v8s26a
    with dissolve
    u "Wow Riley, you-"

    scene v8s26b
    with dissolve
    ri "Shh! Less talking, more action."

    scene v8s27 # TPP (MC is now standing too. Both of them should be visible down until bellies at least). He is kissing Riley's neck with one hand on her boob. Riley enjoying it, mouth closed, her hand in MC's hair
    with dissolve
    pause

    scene v8s27a # MC pulls back and has his both hands on Riley's lingerie top, about to remove it
    with dissolve
    pause

    scene v8s27b # MC kissing/sucking on Riley's boob, Riley enjoying it (mouth closed)
    with dissolve
    ri "Mmmmh..."

    scene v8s27c # MC pulled back. Riley's hands on MC's chest, and mouth open
    with dissolve
    ri "Let's get these off."

    scene v8s27d # MC fully naked. Riley still has her bottom on
    with fade
    pause 1

    scene v8s28 # TPP. MC crouched and has his hands on her panties, about to remove it. Close up shot so that MC's face, hands and Riley's bottom is visible
    with dissolve
    pause 0.5

    scene v8s28a # Panties off, MC is just staring at her wet pussy
    with dissolve
    pause 0.5

    scene v8s28c
    with dissolve
    pause
    ri "Ahh... [name]..."
    ri "I want to... *moans* ride you so badly right now!"

    # CHECK - Modified because of missing image (v8s28b)
    # scene v8s28b # MC kissing/licking her pussy, deep into it
    # with dissolve
    # pause
    # ri "*Moans*"

    # scene v8s28c # Same as v8s28b but slightly different shot (head tilt, etc)
    # with dissolve
    # ri "Ahh... [name]..."

    # scene v8s28b
    # with dissolve
    # ri "I want to... *moans*"

    # scene v8s28c
    # with dissolve
    # ri "...ride you so badly right now!"

    scene v8s29 # TPP. MC is in the bed, turned towards Riley who is still standing and hand gesturing her to come. Camera behind Riley's ass and focus on it (DOF blur on MC). Note: s29 will be leading up to the posture in Animation 1 in three frames. Check at the end for reference (just posture, camera angle is different)
    with fade
    pause

    show screen v8s3_rileySexOverlay

    scene v8s29a # Riley climbing on the bed and MC is getting on his back now
    with dissolve
    pause 0.5

    scene v8s29b # Posture from animation 1
    with dissolve
    pause

    image v8ricg1 = Movie(play="images/v8/Scene 3/v8ricg1.webm", loop=True, image="images/v8/Scene 3/risex000.webp", start_image="images/v8/Scene 3/risex000.webp") # CG TPP
    image v8ricg1f = Movie(play="images/v8/Scene 3/v8ricg1f.webm", loop=True, image="images/v8/Scene 3/risex000.webp", start_image="images/v8/Scene 3/risex000.webp")
    image v8ricg2 = Movie(play="images/v8/Scene 3/v8ricg2.webm", loop=True, image="images/v8/Scene 3/risex2_000.webp", start_image="images/v8/Scene 3/risex2_000.webp") # CG FPP
    image v8ricg2f = Movie(play="images/v8/Scene 3/v8ricg2f.webm", loop=True, image="images/v8/Scene 3/risex2_000.webp", start_image="images/v8/Scene 3/risex2_000.webp")
    image v8ridg1 = Movie(play="images/v8/Scene 3/v8ridg1.webm", loop=True, image="images/v8/Scene 3/risex3000.webp", start_image="images/v8/Scene 3/risex3000.webp") # Doggy smooth
    image v8ridg1f = Movie(play="images/v8/Scene 3/v8ridg1.webm", loop=True, image="images/v8/Scene 3/risex3000.webp", start_image="images/v8/Scene 3/risex3000.webp")
    image v8ridg2 = Movie(play="images/v8/Scene 3/v8ridg2.webm", loop=True, image="images/v8/Scene 3/risex4_000.webp", start_image="images/v8/Scene 3/risex4_000.webp") # Doggy rough
    image v8ridg2f = Movie(play="images/v8/Scene 3/v8ridg2f.webm", loop=True, image="images/v8/Scene 3/risex4_000.webp", start_image="images/v8/Scene 3/risex4_000.webp")
    image v8ridg3 = Movie(play="images/v8/Scene 3/v8ridg3.webm", loop=True, image="images/v8/Scene 3/risex5_00.webp", start_image="images/v8/Scene 3/risex5_00.webp") # Doggy smooth angle 2
    image v8ridg3f = Movie(play="images/v8/Scene 3/v8ridg3.webm", loop=True, image="images/v8/Scene 3/risex5_00.webp", start_image="images/v8/Scene 3/risex5_00.webp")

label v8s3_rileyCowgirl:
    scene v8ricg1
    with dissolve
    pause 3
    ri "Mmmm..."
    u "(She's so wet, she slipped right through.)"
    pause

    scene v8ricg2
    with dissolve
    pause 2
    ri "*Moans lightly*"
    ri "[name]... you feel so good!"
    pause

    scene v8ricg2f
    with dissolve
    u "(Oh, she's starting to pick up the pace.)"
    ri "Oh yes!"
    pause

    scene v8ricg1f
    with dissolve
    pause 3
    u "Ahh! You're so hot, Riley!"
    pause
    ri "You want me to go faster?"
    u "If you can, yeah."
    pause

    scene v8ricg2f
    with dissolve
    pause 3
    u "(She's trying, but hasn't actually sped up much.)"
    ri "[name]... Let's change up."
    ri "*Moans* I want you to fuck me from behind."
    pause

label v8s3_rileyLiftDoggy:
    scene v8s30 # TPP. Check animation 2 at the end for pose reference, maintain a similar camera angle but zoom in a little on the face. Riley turned her head a little with cornered eyes trying to look backside, curious, mouth open. Add DOF if possible.
    with fade
    ri "Well, what are you waiting for?"

    scene v8ridg1
    with dissolve
    pause 5
    ri "Oh God! Yes!"
    pause

    scene v8ridg3
    with dissolve
    u "Ahh fuck!"
    ri "*Moans* Harder!"

    scene v8ridg1
    with dissolve
    pause 3
    u "Hngh!"
    ri "Fuck yes! Just like that!"
    pause

    scene v8ridg3f
    with dissolve
    ri "*Moans loudly*"
    ri "Harder! Show me your... *moans* best."
    u "Ahh! Get your hands here."

label v8s3_rileyDoggy:
    scene v8ridg2
    with dissolve
    pause 3
    u "You like that?"
    ri "Yes! Yes! God yes!"
    pause
    ri "Oh God baby, you feel so... *moans*"
    ri "...fucking good!!!"
    u "It's about to feel better now."

    scene v8ridg2f
    with dissolve
    pause 2
    ri "Yes! Yes! Don't stop!"
    pause
    ri "[name]... Fuck! I'm about to... *moans*"
    u "Ahh! I'm also close. Fuck!"
    ri "*Moans really loud*" with hpunch
    u "Did you-"
    ri "Yes! *moans*"
    pause 2
    ri "Cum in me. I want it. Now!!!"
    u "You sure?"
    ri "Yes, I'm on the pill."
    pause 5
    u "Ah yes! Ahhh fuck!" with hpunch

    scene v8s31 # TPP. Close up creampie shot. Slightly more than tip of the dick inside her and cum is leaking
    with flash
    pause

    stop music fadeout 3
    
    ri "Mmmmm!"

    hide screen v8s3_rileySexOverlay

    scene v8s32 # TPP (not a close up). MC and Riley laying in bed facing each other in their underwear
    with Fade(0.5, 0.5, 0.5)
    pause 1

    scene v8s33 # FPP. Riley talking, smiling, relaxed
    with dissolve
    ri "Fuck me. That was so good!"

    $ renpy.end_replay()

    play music "music/mlove.mp3" fadein 2

    scene v8s33a # Same as v8s33 but Riley mouth closed
    with dissolve
    u "Agreed."

    scene v8s33
    with dissolve
    ri "I haven't had such an orgasm in like... ever!"

    scene v8s33a
    with dissolve
    u "Haha, glad to be of service!"
    ri "*Chuckles*"


    scene v8s33_2 # TPP. Close up of MC and Riley kissing from top
    with dissolve
    play sound "sounds/kiss.mp3"
    pause 0.5

    scene v8s33a
    with dissolve
    u "By the way, where's your roommate?"

    scene v8s33
    with dissolve
    ri "She isn't gonna be back until noon tomorrow."

    if "v7_riley" in sceneList:
        scene v8s33b # Riley slightly flirty and mouth open
        with dissolve
        ri "Which is why you're gonna sleep here this time *Chuckles*"

    else:
        scene v8s33b
        with dissolve
        ri "Which is why I wish you stay here until the morning."

    scene v8s33a
    with dissolve
    u "Why? You wanna go another round after waking up?"

    scene v8s33b
    with dissolve
    ri "Haha, I didn't mean that, but we'll see."

    scene v8s33a
    with dissolve
    u "Mhmm. You tired?"

    scene v8s33
    with dissolve
    ri "Very."

    scene v8s33a
    with dissolve
    u "Get some rest then."

    scene v8s33
    with dissolve
    ri "Good night, [name]."

label v8s3_nsfwSkipLabel1:
    scene v8s33_2
    with dissolve
    play sound "sounds/kiss.mp3"
    pause 0.5

    scene v8s32a # MC on his back and Riley leaning over on him and sleeping
    with dissolve
    pause 1

    scene v8s34 # FPP. MC waking up in bed looking at Riley writing something at her desk. She's still in underwear
    with Fade(1.5, 0.75, 1)
    pause 1
    u "(She's up already.)"

    scene v8s35 # FPP. MC walks up to her. She's looking into the camera, smiling wide and talking. There's notebooks and stuff in front of her
    with dissolve
    ri "Well, good morning to you!"

    scene v8s35a
    with dissolve
    u "Morning! What are you up to?"

    scene v8s35
    with dissolve
    ri "Oh nothing, just this assignment I had pending."

    scene v8s35a
    with dissolve
    u "Riley... It's 7AM!"

    scene v8s35b # Riley slightly embarrassed but smiling and talking
    with dissolve
    ri "Well..."

    scene v8s35c # Same as v8s35b but Riley mouth closed
    with dissolve
    u "On a Saturday!"

    scene v8s35b
    with dissolve
    ri "It's-"

    scene v8s35c
    with dissolve
    u "Just after homecoming night."

    scene v8s35
    with dissolve
    ri "Oh, will you stop already? *laughs*"

    scene v8s35b
    with dissolve
    ri "I just like to finish up my work as early as I can so I have free time later."

    if walkedRileyHome:
        scene v8s35a
        with dissolve
        u "No wonder you were able to add 35 references in your Econ assignment *laughs*"

        scene v8s35b
        with dissolve
        ri "It's, uh... 47 now."

        scene v8s35c
        with dissolve
        u "Are you kidding me!?"

    else:
        scene v8s35a
        with dissolve
        u "Unbelievable."

        scene v8s35b
        with dissolve
        ri "Hey, it's not that weird, is it now?"

        scene v8s35c
        with dissolve
        u "Haha, not really. I just did not expect it."

    scene v8s35a
    with dissolve
    u "Anyway, carry on I guess. I'll go freshen up."

    scene v8s36 # TPP. Riley stands up (MC is still in underwear)
    with dissolve
    pause 0.5

    play sound "sounds/kiss.mp3"

    scene v8s36a # Riley gives a quick peck on MC's lips
    with dissolve
    pause 0.5

    scene v8s36
    with dissolve
    pause 0.5

    scene v8s37 # FPP. Riley laughing a little and talking
    with dissolve
    ri "At least get dressed before you go hotshot."

    scene v8s37a # Same as v8s37 but Riley mouth closed
    with dissolve
    u "Oops, haha yeah."

    scene v8s37a
    with fade
    u "Well... See you later."

    stop music fadeout 3

    scene v8s37
    with dissolve
    ri "Hit me up when you're free. Byeee."

    scene black
    with Dissolve(1)
    pause 0.5

    jump aft_amb_night

    ### Animation references:
    # MC and Riley in Riley's dorm, on her bed. Both of them fully naked. Please use Riley's expressions according to the animation mood.
    #
    # Animation 1:
    # - Position: Cowgirl (passionate)
    # - Direction: MC with his head on the pillow side of the bed
    # - Description: MC's hands on Riley's waist. Riley's hands on MC's chest/belly and she's slightly leaning toward him. Full eye contact. (Make sure Riley's hands don't obstruct her boobs)
    # - Cameras: One FPP and one TPP animation (angle approximately 45% from front and side). Make sure Riley is fully visible on TPP one
    #
    # Animation 2:
    # - Position: Doggy Style (not totally rough, not totally smooth)
    # - Direction: Both of them facing towards the door to allow more camera angle possibilities
    # - Description: Doggy style with MC's hands on Riley's hips. Riley on all fours.
    # - Camera: Only one TPP animation. Angle approximately 45% from front and side
    #
    # Animation 3:
    # - Immediate continuation of Animation 2. So same direction and camera
    # - Position: Doggy Style (on the rougher side)
    # - Description: Doggy style with Riley's hands crossed on her back. MC is holding them with his hand (the one which is closer to the camera)
