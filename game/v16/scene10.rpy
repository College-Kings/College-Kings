# SCENE 10: Ms. Rose Econ Class
# Locations: Ms. Rose's classroom
# Characters: LAUREN (Outfit: 3), MC (Outfit: 5), Ms. Rose (Outfit: 2)
# Time: Morning (Tuesday)

label v16s10: # Econ class
    scene v16s10_1 # TPP Show MC entering Ms. Rose's classroom along with several other students
    with dissolve
    
    pause 0.75

    scene v16s10_2 # TPP Show MC taking a seat in the back row of the class, the empty seat next to him in view
    with dissolve

    pause 0.75
        
    scene v16s10_2a # TPP Same angle as 2, Lauren taking her normal seat next to MC, Lauren smiling at MC with mouth open
    with dissolve

    la "Hey, [name]."

    scene v16s10_3 # FPP View of Lauren sitting next to MC. Lauren smiling with mouth closed
    with dissolve

    u "Hey, Lauren. Have you recovered from your epic party yet?"

    scene v16s10_3a # FPP Same angle as 3, Lauren smiling with mouth open
    with dissolve

    la "Haha, yeah, just about."

    scene v16s10_3
    with dissolve

    u "I had a lot of fun that night."

    scene v16s10_3a
    with dissolve

    la "I think we all did."
    
    if "v15_lauren" in sceneList: # if MC and Lauren had sex after Lauren's party 
        #scene v16s10_3b # FPP Same angle as 3, Lauren looking down with a shy expression, slight smile, mouth open
        scene v16s10_3a
        with dissolve

        la "I was really looking forward to class today."

        scene v16s10_3
        with dissolve

        u "Do you have a passion for economics now?"

        scene v16s10_3a
        with dissolve

        la "Not quite. I was actually excited because I could sit next to you."

        la "I can't stop thinking about us having sex. All the things you did to me. *Giggles*"
        
        if "v12_lauren" not in sceneList: # if it was also Lauren's first time
            scene v16s10_3b
            with dissolve

            la "People talk about your first time being special. That certainly was."

        # -Regardless of it being Lauren's first time-
        scene v16s10_3
        with dissolve

        u "Well, I'm happy to be of service, haha."

        scene v16s10_3a
        with dissolve

        la "We'll have to do it again. Really soon."

        scene v16s10_3
        with dissolve

        u "Definitely. I'd like that a lot."

    # -Regardless of if MC and Lauren had sex after Lauren's party-
    scene v16s10_4 # FPP Show Ms. Rose at the front of the class, looking over the students, neutral expression, mouth open
    with dissolve

    ro "Okay, let's stop the chatter and settle down, please. We have a lot to go through today."

    ro "We're going to start off with one of your favorites. A slideshow presentation!"

    scene v16s10_5 # TPP View of the students in the class, they all look annoyed, many mouths open to groan
    with dissolve
    
    alls "*Groans*" # NOT SURE HOW TO CODE IT FOR ALL STUDENTS

    scene v16s10_4
    with dissolve
    
    ro "Sorry guys, no one said economics was fun!"
    
    if lauren.relationship >= Relationship.FWB: # -if LaurenRS or LaurenSex
        scene v16s10_2b # TPP Same angle as 2, Lauren passing MC a note under the table, Lauren has a naughty smile
        with dissolve

        pause 0.75

        scene v16s10_6 # FPP Show the note from Lauren. It just says, "I'm horny"
        with dissolve

        u "(Oh, shit... What is she trying to do?)"

        scene v16s10_2c # TPP Same angle as 2, Lauren reaching her hand over to MC's thigh under the table
        with dissolve

        u "(Oh, my... She actually wants to do this.)"

        scene v16s10_7 # FPP MC looking down at his lap, where Lauren, reaching under the table, is rubbing his crotch
        with dissolve

        u "(I mean, it feels good, but...)"

        u "(Damn, it feels really good.)"

    else:
        scene v16s10_2d # TPP Same angle as 2, Lauren passing MC a note under the table, Lauren with a slight smile, mouth closed
        with dissolve

        u "(Haha, Lauren must be as bored as me.)"

        scene v16s10_6a # FPP Same angle as 6, note from Lauren says, "Do you think Ms. Rose and Mr. Lee have ever..."
        with dissolve

        u "(Do you think Ms. Rose and Mr. Lee have ever...)"

        menu:
            "Hooked up with each other":
                scene v16s10_8 # TPP MC leaning over to whisper in Lauren's ear, mouth slighly open
                with dissolve

                u "*Whispers* They've definitely banged each other. Probably right here in the classroom!"

            "Hooked up with the Dean":
                scene v16s10_8
                with dissolve

                u "*Whispers* Had sex with the Dean? Of course they have! All three of them, in her office."

    # -Regardless of LaurenFriend note reply choice-
    scene v16s10_2e # TPP Same angle as 2, Lauren laughing quietly, mouth slighly open.
    with dissolve

    la "*Laughs*"

    scene v16s10_2f # TPP Same angle as 2, Lauren with mouth closed, slight smile like she's trying not to laugh, eyes forward, hands on the table in front of her
    with dissolve

    pause 0.75

    # -Regardless of which note was passed-
    scene v16s10_4a # FPP Same angle as 4, Ms. Rose looking directly at MC, she looks annoyed, mouth open
    with dissolve

    ro "[name]!"

    scene v16s10_4b # FPP Same angle as 4, Ms. Rose looking directly at MC, she looks annoyed, mouth closed
    with dissolve

    u "Huh?"

    scene v16s10_4a
    with dissolve

    ro "Please answer the question."

    scene v16s10_4b
    with dissolve

    u "Oh, okay... Um..."

    scene v16s10_4a
    with dissolve

    ro "You were listening, weren't you?"

    scene v16s10_4b
    with dissolve

    u "O-of course."

    scene v16s10_4a
    with dissolve

    ro "So, what's the answer?"

    scene v16s10_4b
    with dissolve

    menu (fail_label="v16s10_dontknow"):
        "Forty-two?":
            $ grant_achievement("the_answer_to_everything")

            u "Uh, the answer is forty-two?"

            scene v16s10_4c # FPP Same angle as 4, Ms. Rose looking at MC, neutral expression, mouth open
            with dissolve

            ro "Nice try. You were close. It's actually forty-seven."

            scene v16s10_4d # FPP Same angle as 4, Ms. Rose looking at MC, neutral expression, mouth closed
            with dissolve

            u "(How the fuck did I even get close?)"

            u "Right, yeah... Sorry."

        "I don't know":
            label v16s10_dontknow:
            
            u "Sorry, I don't know. I... was thinking about something else."

            scene v16s10_4a
            with dissolve

            ro "Do I need to separate you and Lauren?"

            scene v16s10_3c # FPP Same angle as 3, Lauren looking forward and giggling, hand over her mouth
            with dissolve

            la "*Giggles*"

            scene v16s10_4b
            with dissolve

            u "No, it's okay. You have my full attention."

            scene v16s10_4c
            with dissolve

            ro "Good, please concentrate. I'd hate to fail my students just because they can't focus."

    # -Regardless of choice-
    if lauren.relationship >= Relationship.FWB: # -if LaurenRS or LaurenSex
        scene v16s10_2c
        with dissolve

        u "(What has gotten into her...?)"

        scene v16s10_7
        with dissolve

        u "(*Moans* Fuck, Lauren...)"

        menu:
            "Stop her":
                scene v16s10_2g # TPP Same angle as 2, MC pushing Lauren's hand away, Lauren looks disappointed
                with dissolve

                u "*Whispers* Not now, Lauren."

                scene v16s10_3d # FPP Same angle as 3, Lauren looking forward, arms crossed over her chest, pouting in disappointment
                with dissolve

                pause 1.25

            "Let her continue":
                label v16s10_sg:
            
                $ sceneList.add("v16_lauren")
                $ add_point(KCT.BOYFRIEND)

                scene v16s10_7a # FPP Same angle as 7, Lauren's hand is fumbling at MC's pants, pulling the top down to get to his dick
                with dissolve

                u "(Fuck, she's actually doing it!)"

                scene v16s10_7b # FPP Same angle as 7, Lauren has pulled down MC's pants to just above his knees and is holding his dick in her hand
                with dissolve

                u "(Oh, shhhiittt...)"

                scene v16s10_7c # FPP Same angle as 7, MC's dick is now hard and Lauren is giving him a hand job under the table
                with dissolve

                u "(This is... *Moans* This is so wrong.)"

                # -ANIMATION: We see Lauren's face, how much she's enjoying giving the handjob-
                image v16lahjTPP = Movie(play="images/v16/Scene_10/v16lahjTPP.webm", loop=True, image="images/v16/Scene_10/v16lahjTPP.webp", start_image="images/v16/Scene_10/v16lahjTPP.webp")

                # Second angle - FPP of handjob
                image v16lahjFPP = Movie(play="images/v16/Scene_10/v16lahjFPP.webm", loop=True, image="images/v16/Scene_10/v16lahjFPP.webp", start_image="images/v16/Scene_10/v16lahjFPP.webp")

                scene v16lahjTPP # Ignore - animation
                with dissolve
            
                u "(What if someone sees this? This is so damn kinky!)"

                scene v16lahjFPP # Ignore - animation
                with dissolve

                u "(Fuck...)"

                # Same third person handjob animation, but faster
                image v16lahjTPPf = Movie(play="images/v16/Scene_10/v16lahjTPPf.webm", loop=True, image="images/v16/Scene_10/v16lahjTPP.webp", start_image="images/v16/Scene_10/v16lahjTPP.webp")

                # Second angle - FPP of handjob, but faster
                image v16lahjFPPf = Movie(play="images/v16/Scene_10/v16lahjFPPf.webm", loop=True, image="images/v16/Scene_10/v16lahjFPP.webp", start_image="images/v16/Scene_10/v16lahjFPP.webp")

                scene v16lahjTPPf # Ignore - animation
                with dissolve

                u "(I'm gonna cum! Where's it all going to go?)"

                scene v16lahjFPPf # Ignore - animation
                with dissolve

                u "*Grunts*"

                scene v16s10_7d # FPP Same angle as 7, MC cumming between his legs onto the floor
                with dissolve

                pause 0.75
            
                scene v16s10_4e # FPP Same angle as 4, Ms. Rose looking at MC with her eyebrow raised in curiousity, mouth closed
                with dissolve

                u "(Shit! Did she hear me?)"

                scene v16s10_4d
                with dissolve

                u "(Oh god, please tell me she didn't see anything.)"

                scene v16s10_2h # FPP Same angle as 2, MC pulling his pants back up, Lauren still with a naughty smile, looking forward but leaning toward MC, mouth open
                with dissolve

                la "*Whispers* I hope you enjoyed that as much as I did."

                scene v16s10_3c
                with dissolve

                u "*Whispers* What was that all about, you sexy freak?"

                scene v16s10_3e # FPP Same angle as 3, Lauren looking forward, slight smile, mouth open
                with dissolve

                la "*Soft giggle* Just having a little fun, that's all."

                scene v16s10_2f
                with dissolve

                u "(She's gonna be the death of me. Lauren of all people... Damn.)"

                $ renpy.end_replay()

    else: # -if LaurenFriend
        scene v16s10_4d
        with dissolve

        u "(I'd better concentrate now. I hate being called out like that...)"

    # -Regardless of all-
    scene v16s10_9 # FPP View of clock in the classroom, set at time for class to end
    with fade

    pause 0.75

    scene v16s10_4f # FPP Same angle as 4, Ms. Rose smiling out over the class, mouth open
    with dissolve

    ro "See, that wasn't so bad, huh? You all survived."

    scene v16s10_4
    with dissolve

    ro "And if I'm lucky, some of you learned a thing or two as well."

    scene v16s10_10 # TPP MC and Lauren getting out of their seats.
    with dissolve

    pause 0.75

    if lauren.relationship >= Relationship.FWB: 
        scene v16s10_11 # TPP MC walking toward the door to the classroom, Lauren catches him by grabbing his upper arm from behind
        with dissolve

        pause 0.75

        if "v16_lauren" in sceneList:
            scene v16s10_12 # TPP MC and Lauren standing at back of the classroom, close up view of Lauren whispering in MC's ear, slight smile, mouth open
            with dissolve

            la "Next time, I want you inside of me."

        else: # -if stop her
            scene v16s10_12
            with dissolve

            la "I hope you plan on making it up to me later."

        scene v16s10_13 # TPP MC and Lauren standing at back of the classroom, Lauren kissing MC on the cheek
        with dissolve

        pause 0.75

    # -regardless-
    jump v16s11 # -Transition to Scene 11-