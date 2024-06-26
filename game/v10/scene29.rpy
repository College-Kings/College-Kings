# SCENE 29: MC runs into Chloe
# Locations: College Hallways
# Characters: MC (Outfit 3), Chloe (Outfit 5), Aubrey (Outfit 2)
# Time: Tuesday Morning

label v10_chloe_hallway:
    play music music.ck1.v10.Track_Scene_29 fadein 2
    scene v10such1 # TPP. Show MC walking down the school hallway after exiting econ class, to the side in the distance near lockers should be Chloe and Aubrey.
    with fade

    pause 0.75

    scene v10such2 # TPP. Show MC now walking past Chloe and Aubrey, both of them looking at MC, MC looking at them both.
    with dissolve

    pause 0.75

    scene v10such3 # FPP. Close up Chloe and Aubrey, both neutral, Aubrey mouth open.
    with dissolve

    au "[name], settle an argument for us."

    if CharacterService.is_mad(chloe):
        scene v10such3a # FPP. Same as 3, Aubrey smile, Chloe slightly annoyed, Chloe mouth open.
        with dissolve

        cl "*Annoyed* Don't bring him into this."

        scene v10such3b # FPP. Same as 3, Aubrey smile, Chloe slightly annoyed, Aubrey mouth open.
        with dissolve

        au "Oh shush. Okay, so I told Chloe she looks really cute today, but she said cute makes it sound really childish so she'd rather look sexy."
        
        au "Which do you think describes Chloe better?"

        scene v10such3c # FPP. Same as 3, aubrey smile, chloe slightly annoyed, both mouths closed.
        with dissolve

        menu:
            "Cute" (boyfriend=1.0):
                $ reputation.add_point(RepComponent.BOYFRIEND)

                u "I'd say cute fits better..."

                scene v10such3a
                with dissolve

                cl "Ugh, who cares what you think?"

            "Sexy":
                if not reputation() == Reputations.POPULAR:
                    u "No, sexy definitely describes her better."

                    scene v10such3a
                    with dissolve

                    cl "Ugh, I don't care what you think."

                else:
                    call screen reputation_popup

                    u "No, sexy definitely describes her better."

                    scene v10such3d # FPP. Same as 3, aubrey smile, chloe awkward smile, Chloe mouth open.
                    with dissolve

                    cl "Uhm... thanks."

                    scene v10such3e # FPP. Same as 3, aubrey smile, chloe awkward smile, Aubrey mouth open.
                    with dissolve

                    au "Someone looks happy with his answer. Guess that means you guys have some catching up to do. Bye bye."

                    scene v10such4a # TPP. Same as 4, Aubrey walking away instead, Chloe and MC watching her.
                    with dissolve

                    pause 0.75

                    scene v10such5 # FPP. Close up Chloe, Chloe neutral, mouth closed.
                    with dissolve

                    menu:
                        "Ask Chloe how she is" (chloe=1.0):
                            $ reputation.add_point(RepComponent.BOYFRIEND)
                            $ chloe.points += 1

                            u "So uhm... how have you been?"

                            scene v10such5a # FPP. Same as 5, neutral, mouth open.
                            with dissolve

                            cl "Pretty stressed, but I'm managing. I could really use a break you know?"

                            scene v10such5
                            with dissolve

                            u "Yeah, I feel you on that."

                            scene v10such5a
                            with dissolve

                            cl "Do you remember that time we uhm... played volleyball?"

                            scene v10such5
                            with dissolve

                            u "Of course."

                            scene v10such5b # FPP. Same as 5, smile, mouth open.
                            with dissolve

                            cl "Any chance you want a rematch?"

                            scene v10such5c # FPP. Same as 5, smile, mouth closed.
                            with dissolve

                            u "Right now?"

                            scene v10such5b
                            with dissolve

                            cl "Uhhh, yeah. If you want?"

                            scene v10such5c
                            with dissolve

                            menu:
                                "Have a Rematch" (chloe=1.0):
                                    $ reputation.add_point(RepComponent.BOYFRIEND)
                                    $ CharacterService.set_relationship(chloe, Relationship.FRIEND, mc)
                                    $ CharacterService.remove_mood(chloe, Moods.MAD)
                                    grant Achievement("on_the_court", "Have a rematch with Chloe")

                                    u "Yeah let's go."

                                    jump v10_chloe_gym

                                "Decline a Rematch" (chloe=-1.0):
                                    $ reputation.add_point(RepComponent.TROUBLEMAKER)
                                    $ chloe.points -= 1

                                    u "Uhm, I shouldn't, I have a lot to do. Sorry."

                                    scene v10such5a
                                    with dissolve

                                    cl "Oh, yeah okay... no worries. Guess I'll see you around then."

                        "Leave":
                            u "I should probably go too. Uhm nice seeing you."

                            scene v10such5a
                            with dissolve

                            cl "Yeah. Alright."   

        if not reputation() == Reputations.POPULAR:
            scene v10such4 # TPP. Show Chloe walking away, Aubrey and MC watching her.
            with dissolve

            pause 0.75

            scene v10such6 # FPP. Close up Aubrey, Aubrey smile, mouth open.
            with dissolve

            au "She's not your biggest fan."

            scene v10such6a # FPP. Same as 6, smile, mouth closed.
            with dissolve

            u "That obvious, huh?"

            scene v10such6b # FPP. Same as 6, laugh, mouth open.
            with dissolve

            au "Yes, very. I'm gonna get to class, see you around."

            scene v10such4b # TPP. Same as 4, Aubrey walking away, Chloe not in view, MC watching Aubrey walk away.
            with dissolve

            u "(Wow, she was cold.)"

        else:
            scene v10such4c # TPP. Same as 4, MC walking away, Chloe watching him, Aubrey not in view.
            with dissolve

            pause 0.75

    else:
        scene v10such3f # FPP. Same as 3, both smile, aubrey mouth open.
        with dissolve

        au "Okay, so I told Chloe she looks really cute today, but she said cute makes it sound really childish and so she'd rather look... sexy."

        scene v10such3g # FPP. Same as 3, both smile, Chloe mouth open.
        with dissolve

        cl "Which one do you think describes me better?"

        scene v10such3h # FPP. Same as 3, both smile, mouths closed.
        with dissolve

        menu:
            "Cute":
                $ aubrey.points += 1

                u "Cute. Definitely..."

                scene v10such3g
                with dissolve

                cl "Ugh, really?"

                scene v10such3f
                with dissolve

                au "I told ya!"
                au "Anyways, I'm gonna head to class, see you guys."

            "Sexy":
                $ reputation.add_point(RepComponent.BOYFRIEND)
                $ chloe.points += 1

                u "Definitely gotta go with sexy."

                scene v10such3g
                with dissolve

                cl "See, I was right."

                scene v10such3f
                with dissolve

                au "Typical guy. Well, I'm gonna head to class, see you guys."

        scene v10such4a
        with dissolve

        pause 0.75

        scene v10such5c
        with dissolve

        u "So... how's life?"

        scene v10such5b
        with dissolve

        cl "Pretty stressed, but I'm managing. I could really use a break you know?"

        scene v10such5c
        with dissolve

        u "I feel you on that."

        scene v10such5b
        with dissolve

        cl "I know a nice way we could pass some time. You remember when we played Volleyball?"

        scene v10such5b
        with dissolve

        u "Yeah, of course."

        scene v10such5d # FPP. Same as 5, flirty smile, mouth open.
        with dissolve

        cl "How about a rematch?"

        scene v10such5e # FPP. Same as 5, flirty smile, mouth closed.
        with dissolve

        menu:
            "Have a Rematch" (chloe=1.0):
                $ reputation.add_point(RepComponent.BOYFRIEND)
                $ chloe.points += 1
                
                grant Achievement("on_the_court", "Have a rematch with Chloe")

                u "Let's do it, but I won't be going easy on you."

                scene v10such5d
                with dissolve

                cl "Please, that's how I like it."

                scene v10such7 # TPP. Show Chloe and MC walking away down the hallway together, both laughing, camera from front.
                with dissolve

                pause 0.75

                jump v10_chloe_gym

            "Decline a Rematch":
                u "I shouldn't, I have a lot to do. Sorry."

                scene v10such5a
                with dissolve

                cl "Oh, yeah okay... no worries. Guess I'll see you around then."

        scene v10such4d # TPP. Same as 4, Chloe walking away, MC watching her, Aubrey not in view.
        with dissolve

        pause 0.75
        stop music fadeout 3

    jump v10_emily_course