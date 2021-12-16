# SCENE 30a: Emily First Responders Course
# Locations: College Hallways & Any Empty Room in FGU University, Libary
# Characters: MC (Outfit 3), Emily (Outfit 3)
# Time: Tuesday Afternoon

label v10_emily_course:
    scene v10semi1 # TPP. Show MC walking down the college hallways, towards a slightly open door.
    with fade

    play music "music/v10/Track Scene 27.mp3" fadein 2

    pause 0.75

    scene v10semi2 # TPP. Show the inside of the first responders class (camera as if MC peaking in) Emily practicing CPR on a dummy, Ben & Jerry watching. 1 or 2 other random students in the class.
    with dissolve

    menu:
        "Leave":
            u "(I should probably just get straight to studying. Getting a headstart on some of that Econ work might be a good idea.)"

            scene v10semi3 # TPP. Show MC now in the fgu library, looking at some books.
            with fade

            u "(I don't even know if I have credit yet?)"

            scene v10semi4 # TPP. Show MC now looking at a different set of books.
            with dissolve

            u "(How much money do I even have?)"

            scene v10semi5 # TPP. Show MC now looking at another different set of books.
            with dissolve

            u "(No one taught me this in school...)"

        "Watch":
            u "(I didn't know she was into first responder work.)"

            scene v10semi6 # FPP. Return to 2, MC now walks futher into the first responder class and everyone inside turns to look at him, Emily mouth open.
            with dissolve

            if forgiveemily:
                em "Oh hey [name]."

                scene v10semi6a # FPP. Same as 6, Ben mouth open.
                with dissolve

                be "Ahh you have a visitor, perfect timing for a five minute break."

                scene v10semi7 # FPP. Emily get's up from the floor and gets close to MC, neutral, mouth open.
                with dissolve

                em "What are you doing here?"

                scene v10semi7a # FPP. Same as 7, neutral, mouth closed.
                with dissolve

                u "Well I was just passing by and thought I heard your voice so I peeked in. I didn't know you were into this kind of stuff."

                scene v10semi7
                with dissolve

                em "I've been trying out a lot of new things recently, a friend suggested this course so I'm trying it out."

                scene v10semi7a
                with dissolve

                u "Good to see you trying new things."

                scene v10semi7
                with dissolve

                em "Yeah, it's been a while since I-"

                scene v10semi8 # TPP. Show Jerry, looking in the direction of emily, mouth open.
                with dissolve

                jer "Emily we're ready to get going again."

                scene v10semi7
                with dissolve

                em "Looks like I gotta go. You know what... you should join us. I'd enjoy the company... and only three of us showed up, so there's plenty of space."

                scene v10semi7a
                with dissolve

                menu:
                    "Join Emily":
                        $ add_point(KCT.BOYFRIEND)
                        $ emily.points += 1

                        u "I'm sure I could try it out."

                        scene v10semi9 # TPP. Show Emily and MC walking to the center of the room where the dummy is, Ben and Jerry looking at them both, Ben mouth open.
                        with dissolve

                        be "Will your friend be joining us?"

                        scene v10semi10 # FPP. Show Ben & Jerry, both smile, mouths closed.
                        with dissolve

                        u "Sure will."

                        scene v10semi10a # FPP. Same as 10, smiles, Jerry mouth open.
                        with dissolve

                        jer "Let's get to it then!"

                        scene v10semi11 # FPP. Show Emily doing CPR on the dummy, camera as if MC is kneeled down next to her.
                        with fade

                        u "Emily you're pretty good at this."

                        scene v10semi10b # FPP. Same as 10, smiles, ben mouth open.
                        with dissolve

                        be "You should think about becoming a nurse young lady."

                        scene v10semi11a # FPP. Same as 11, Emily turns to look at camera, doing cpr, laugh, mouth open.
                        with dissolve

                        em "\"Staying alive, staying alive!\""

                        scene v10semi12 # FPP. Show Emily lying down, acting like she's dead.
                        with dissolve

                        u "Emily?"

                        scene v10semi12a # FPP. Same as 12, Emily turns to look at camera, still pretending she's dead, mouth open.
                        with dissolve

                        em "*Whisper* I can't breath, will anyone save me?"

                        scene v10semi12
                        with dissolve

                        menu:
                            "Save Emily":
                                $ add_point(KCT.BOYFRIEND)

                                u "Don't you die on us!"

                                be "Looks like you two are really getting into it."                                

                            "Don't save Emily":
                                $ add_point(KCT.TROUBLEMAKER)
                            
                                u "Oh no, if only someone could save her."

                                scene v10semi12b # FPP. Same as 12, Emily sits up, looks at camera, laughs, mouth open.
                                with dissolve

                                em "Oh you're no fun."

                        scene v10semi10b
                        with dissolve

                        be "Alright, that's all for today. I wish we had more students, but you guys still made it a wonderful class. Will any of you be joining us for another class?"

                        scene v10semi14 # FPP. Show Emily as if she is sat next to MC on the floor, Emily looking at camera, smile, mouth open.
                        with dissolve

                        em "I know I will. I honestly could really see myself being a nurse. What do you think, [name]?"

                        scene v10semi14a # FPP. Same as 14, smile, mouth closed.
                        with dissolve

                        menu:
                            "Agree with Emily":
                                $ add_point(KCT.BOYFRIEND)
                                $ emily.points += 1

                                u "Yeah, I could be down."

                                scene v10semi14
                                with dissolve

                                em "Amazing."

                            "Disagree with Emily":
                                u "I don't know. It was fun and all, but I think I'm not made to be a first responder."

                                scene v10semi14
                                with dissolve

                                em "Maybe in another life."

                        scene v10semi14a
                        with dissolve

                        u "Shoot, what time is it?"

                        scene v10semi14
                        with dissolve

                        em "About seven."

                        scene v10semi14a
                        with dissolve

                        u "Oh damn, I need to go. I haven't studied for my assignment at all."

                        scene v10semi14b # FPP. Same as 14, neutral, mouth open.
                        with dissolve

                        em "Oh, well I don't want to keep you."

                        scene v10semi15 # TPP. Show Emily and MC hugging, camera from behind MC.
                        with dissolve

                        u "I'll see you around."

                        scene v10semi14b
                        with dissolve

                        em "See you [name]. Thanks for hanging with me."

                        scene v10semi14c # FPP. Same as 14, neutral, mouth closed.
                        with dissolve

                        u "Of course."

                        jump v10_late_alley

                    "Leave":
                        $ add_point(KCT.TROUBLEMAKER)

                        u "Shoot, what time is it?"

                        scene v10semi7
                        with dissolve

                        em "About seven."

                        scene v10semi7a
                        with dissolve

                        u "Oh damn, I need to go. I haven't studied for my assignment at all."

                        scene v10semi7b # FPP. Same as 7, slight sad, mouth open.
                        with dissolve

                        em "Oh, well I don't want to keep you."

                        scene v10semi7c # FPP. Same as 7, slight sad, mouth closed.
                        with dissolve

                        u "I'll see you around."

                        jump v10_late_alley

            else:
                em "Oh uhm... hey [name]."

                scene v10semi6a
                with dissolve

                be "Ahh you have company, perfect timing for a five minute break."

                scene v10semi7
                with dissolve

                em "What are you... what are you doing here? I'm a little surprised to see you."

                scene v10semi7a
                with dissolve

                u "Well I was just passing by and thought I heard your voice so I peeked in. I didn't know you were into this kind of stuff."

                scene v10semi7
                with dissolve

                em "Oh well... I've been trying out a lot of new things recently, a friend suggested this course so I'm trying it out."

                scene v10semi7a
                with dissolve

                u "Good to see you trying new things."

                scene v10semi7d # FPP. Same as 7, slight nervous, mouth open.
                with dissolve

                em "We haven't really spoken much, I thought you were mad at me."

                scene v10semi7e # FPP. Same as 7, slight nervous, mouth closed.
                with dissolve

                u "I wasn't mad, I just- I just needed time to process everything that happened."

                scene v10semi7d
                with dissolve

                em "I understand that."

                scene v10semi8
                with dissolve

                jer "Emily we're ready to get going again."

                scene v10semi7d
                with dissolve

                em "Looks like I gotta go. You know what... you should join us. I'd enjoy the company... and only three of us showed up, so there's plenty of space."

                scene v10semi7e
                with dissolve

                menu:
                    "Join Emily":
                        $ add_point(KCT.BOYFRIEND)
                        $ emily.points += 1
                        $ forgiveemily = True

                        u "I'm sure I could try it out."

                        scene v10semi9
                        with dissolve

                        be "Will your friend be joining us?"

                        scene v10semi10
                        with dissolve

                        u "Sure will."

                        scene v10semi10a
                        with dissolve

                        jer "Let's get to it then!"

                        scene v10semi11
                        with fade

                        u "Emily you're pretty good at this."

                        scene v10semi10b
                        with dissolve

                        be "You should think about becoming a nurse young lady."

                        scene v10semi11a
                        with dissolve

                        em "\"Staying alive, staying alive!\""

                        scene v10semi12
                        with dissolve

                        u "Emily?"

                        scene v10semi12a
                        with dissolve

                        em "*Whisper* I can't breath, will anyone save me?"

                        scene v10semi12
                        with dissolve

                        menu:
                            "Save Emily":
                                $ add_point(KCT.BOYFRIEND)

                                u "Don't you die on us!"

                                be "Looks like you two are really getting into it."                                

                            "Don't save Emily":
                                $ add_point(KCT.TROUBLEMAKER)
                            
                                u "Oh no, if only someone could save her."

                                scene v10semi12b
                                with dissolve

                                em "Oh you're no fun."

                        scene v10semi10b
                        with dissolve

                        be "Alright, that's all for today. I wish we had more students, but you guys still made it a wonderful class. Will any of you be joining us for another class?"

                        scene v10semi14
                        with dissolve

                        em "I know I will. I honestly could really see myself being a nurse. What do you think, [name]?"

                        scene v10semi14a
                        with dissolve

                        menu:
                            "Agree with Emily":
                                $ add_point(KCT.BOYFRIEND)
                                $ emily.points += 1

                                u "Yeah, I could be down."

                                scene v10semi14
                                with dissolve

                                em "Amazing."

                            "Disagree with Emily":
                                u "I don't know. It was fun and all, but I think I'm not made to be a first responder."

                                scene v10semi14
                                with dissolve

                                em "Maybe in another life."

                        scene v10semi14a
                        with dissolve

                        u "Shoot, what time is it?"

                        scene v10semi14
                        with dissolve

                        em "About seven."

                        scene v10semi14a
                        with dissolve

                        u "Oh damn, I need to go. I haven't studied for my assignment at all."

                        scene v10semi14b
                        with dissolve

                        em "Oh, well I don't want to keep you."

                        scene v10semi15
                        with dissolve

                        u "I'll see you around."

                        scene v10semi14b
                        with dissolve

                        em "See you [name]. Thanks for hanging with me."

                        scene v10semi14c
                        with dissolve

                        u "Of course."

                        jump v10_late_alley

                    "Leave":
                        $ add_point(KCT.TROUBLEMAKER)

                        u "Shoot, what time is it?"

                        scene v10semi7
                        with dissolve

                        em "About seven."

                        scene v10semi7a
                        with dissolve

                        u "Oh damn, I need to go. I haven't studied for my assignment at all."

                        scene v10semi7b
                        with dissolve

                        em "Oh, well I don't want to keep you."

                        scene v10semi7c
                        with dissolve

                        u "I'll see you around."

                        jump v10_late_alley
    stop music fadeout 3
    
    jump v10_late_alley