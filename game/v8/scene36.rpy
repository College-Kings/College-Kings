# SCENE 36: ON THE PHONE WITH JULIA
# Locations: MC's room in Wolves house, MC's room in Apes house, Julia's home
# Characters: MC (outfit 2), Julia
# Time: Tuesday afternoon
# Note: There's two versions for MC's renders in this scene. They're both the same essentially except one of them is in Wolves house (starting with "v8room20") and the other is in Apes house (starting with "v8room21")

label v8_julia_call:
    if joinwolves:
        scene v8room20a # MC holding his phone to his ear, neutral expression, mouth closed
        with dissolve
        play sound sound.calling
        pause 1

        stop sound

        scene v8room20b # Same as v8room20a but MC smiling a little, mouth open
        with dissolve
        u "Hey, how's it going?"

        scene v8room22 # TPP (This is in Julia's home) Show Julia sitting on a couch (or something similar, just relaxing at home), holding her phone to her ear, happy, mouth open
        with dissolve
        ju "Hey, Sweetie! Everything alright?"

        scene v8room20a
        with dissolve
        menu:
            "Excited reply":
                scene v8room20c # Same as v8room20a but MC excited, happy, mouth open
                with dissolve
                u "More than alright!"

                scene v8room22
                with dissolve
                ju "Really? That's great! What's going on?"

                scene v8room20c
                with dissolve
                u "The school is offering a trip abroad. And if we get enough people, they'll pay half!"

                scene v8room22
                with dissolve
                ju "Wow! I wish we had that when I was in school."

                scene v8room22a # Same as v8room22 but Julia mouth closed
                with dissolve
                u "Yeah, seems like an opportunity I don't want to miss."

                scene v8room22
                with dissolve
                ju "We'll make it happen! I miss you!"

                scene v8room22a
                with dissolve
                u "Miss you too. I better get some work done. I was just so excited, I had to tell you."

                scene v8room22
                with dissolve
                ju "I'm glad you did. Have a good night, and take care!"

            "Chill reply":
                scene v8room20b
                with dissolve
                u "Yeah, just touching base."

                scene v8room20a
                with dissolve
                ju "Anything new?"

                scene v8room20b
                with dissolve
                u "Actually, there's this cool trip the school is setting up."

                scene v8room22
                with dissolve
                ju "Trip? To where?"

                scene v8room22a
                with dissolve
                u "EUROPE! If we can get enough people to sign up, they'll even cover half the cost."

                scene v8room22
                with dissolve
                ju "That sounds like a once in a lifetime opportunity."

                scene v8room22a
                with dissolve
                u "Yeah, it would be cool to try if I can keep up my grades and stuff."

                scene v8room22b # Same as v8room22 but Julia proud, smiling, mouth open
                with dissolve
                ju "You're such a responsible young man."

                scene v8room22a
                with dissolve
                u "Don't make me blush."

                scene v8room22b
                with dissolve
                ju "I'm just so proud of you."

                scene v8room22a
                with dissolve
                u "Well I better get back to my homework or you won't be!"

                scene v8room22
                with dissolve
                ju "Keep in touch, honey! Take care!"

        play sound "sounds/rejectcall.mp3"

        scene v8room20
        with dissolve
        u "(Well, back to studying I go.)"

    else:
        scene v8room21a # MC holding his phone to his ear, neutral expression, mouth closed
        with dissolve
        play sound sound.calling
        pause 1

        stop sound

        scene v8room21b # Same as v8room21a but MC smiling a little, mouth open
        with dissolve
        u "Hey, how's it going?"

        scene v8room22
        with dissolve
        ju "Hey, Sweetie! Everything alright?"

        scene v8room21a
        with dissolve
        menu:
            "Excited reply":
                scene v8room21c # Same as v8room21a but MC excited, happy, mouth open
                with dissolve
                u "More than alright!"

                scene v8room22
                with dissolve
                ju "Really? That's great! What's going on?"

                scene v8room21c
                with dissolve
                u "The school is offering a trip abroad. And if we get enough people, they'll pay half!"

                scene v8room22
                with dissolve
                ju "Wow! I wish we had that when I was in school."

                scene v8room22a
                with dissolve
                u "Yeah, seems like an opportunity I don't want to miss."

                scene v8room22
                with dissolve
                ju "We'll make it happen! I miss you!"

                scene v8room22a
                with dissolve
                u "Miss you too. I better get some work done. I was just so excited, I had to tell you."

                scene v8room22
                with dissolve
                ju "I'm glad you did. Have a good night, and take care!"

            "Chill reply":
                scene v8room21b
                with dissolve
                u "Yeah, just touching base."

                scene v8room21a
                with dissolve
                ju "Anything new?"

                scene v8room21b
                with dissolve
                u "Actually, there's this cool trip the school is setting up."

                scene v8room22
                with dissolve
                ju "Trip? To where?"

                scene v8room22a
                with dissolve
                u "EUROPE! If we can get enough people to sign up, they'll even cover half the cost."

                scene v8room22
                with dissolve
                ju "That sounds like a once in a lifetime opportunity."

                scene v8room22a
                with dissolve
                u "Yeah, it would be cool to try if I can keep up my grades and stuff."

                scene v8room22b
                with dissolve
                ju "You're such a responsible young man."

                scene v8room22a
                with dissolve
                u "Don't make me blush."

                scene v8room22b
                with dissolve
                ju "I'm just so proud of you."

                scene v8room22a
                with dissolve
                u "Well I better get back to my homework or you won't be!"

                scene v8room22
                with dissolve
                ju "Keep in touch, honey! Take care!"

        play sound "sounds/rejectcall.mp3"

        scene v8room21
        with dissolve
        u "(Well, back to studying I go.)"

    jump v8_tues_evening
