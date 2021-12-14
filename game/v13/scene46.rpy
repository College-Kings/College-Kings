# SCENE 46: Bike Tour with Lauren
# Locations: Bike Trail
# Characters: MC (Outfit: 1), LAUREN (Outfit: 3)
# Time: Afternoon

label v13s46:
    scene v13s46_1 # TPP. Show MC and Lauren riding their bikes on the trail, both slight smiles, mouths closed
    with dissolve

    pause 0.75

    play music "music/v13/Track Scene 46_1.mp3" fadein 2

    scene v13s46_2 # FPP. Show lauren riding her bike on MC's right side, slight smile, mouth closed, forest background
    with dissolve

    u "It feels great out here..."

    scene v13s46_2a # FPP. same as v13s46_2 different forest background, mouth open
    with dissolve

    la "Yeah. Are you an outdoorsy person?"

    scene v13s46_2
    with dissolve

    menu:
        "I love the outdoor":
            scene v13s46_2
            with dissolve

            u "I absolutely love the outdoors. Just the smell of nature, like the rain and sunshine, always puts me in a good mood."

            scene v13s46_2a
            with dissolve

            la "I'm the same exact way. *Chuckles*"

        "I'm a city man":
            scene v13s46_2
            with dissolve

            if v13_emmy_points >= 2:
                $ grant_achievement("urbanizer_womanizer")

            u "I don't hate being outside, but... *Chuckles* I'm definitely a city person."

            scene v13s46_2a
            with dissolve

            la "Really? *Chuckles* I love the outdoors."

            scene v13s46_2
            with dissolve

            u "So, you love getting chewed up by mosquitos?"

            scene v13s46_2a
            with dissolve

            la "Okay, I admit it does have some downsides."

    scene v13s46_2a
    with dissolve

    la "What's amazing about being outside is all the random stuff that happens. Stuff that'd you'd never see if you were stuck in the house all day."

    scene v13s46_2
    with dissolve

    u "Such as?"

    scene v13s46_2a
    with dissolve

    la "Animals, people needing help, a funny looking tree that you just have to climb for no reason... I could keep going. *Chuckles*"

    scene v13s46_2
    with dissolve

    u "Oh, I see... You're really into the outdoors, huh?"

    scene v13s46_2a
    with dissolve

    la "I love it."

    scene v13s46_3 # TPP. MC's bike shakes and he almost falls off but catches himself, slight shock, mouth open
    with dissolve

    pause 0.75

    scene v13s46_4 # FPP. same as v13s46_2a show an open field with a few trees
    with dissolve

    u "Fuck, that was close."

    scene v13s46_4a # FPP. same as v13s46_4 show tall grass instead of trees
    with dissolve

    la "*Laughs* What happened?"

    scene v13s46_4
    with dissolve

    u "I don't know, I think I hit a rock or something."

    scene v13s46_4a
    with dissolve

    la "Or you don't know how to ride a bike. *Chuckles*"

    scene v13s46_4
    with dissolve

    u "*Mocking* \"Or you don't know how to ride a bike.\" *Laughs*"

    scene v13s46_4a
    with dissolve

    la "*Chuckles* I do not sound like that!"

    scene v13s46_4
    with dissolve

    u "..."

    scene v13s46_4a
    with dissolve

    la "What?! My voice is not that soft..."

    scene v13s46_4
    with dissolve

    u "..."

    scene v13s46_4a
    with dissolve

    la "Okay fine, whatever. Maybe it is. *Chuckles*"

    scene v13s46_4
    with dissolve

    u "*Laughs*"

    scene v13s46_4a
    with dissolve

    la "*Whispers* Shhh! Slow down! Stop here..."

    stop music fadeout 3
    play music "music/v13/Track Scene 46_2.mp3" fadein 2

    scene v13s46_4b # FPP. same as v13s46_4 Lauren looks off into the background and then her face shows shock
    with dissolve

    u "*Whispers* What's going on?"

    scene v13s46_5 # TPP. show MC and lauren stop their bicycles and get off, lauren looking into the field at a deer slight smile mouth closed, MC looking lauren no expression mouth closed
    with dissolve

    pause 0.75

    scene v13s46_6 # FPP. show lauren in the field points to the deer in the background eating grass, full smile, mouth open
    with dissolve

    la "Look! It's a deer."

    scene v13s46_7 # FPP. # close-up shot of a deer is seen grazing
    with dissolve

    pause 0.75

    scene v13s46_8 # FPP. # Lauren pulls a granola bar from her purse
    with dissolve

    pause 0.75

    scene v13s46_6a # FPP. same as v13s46_6 MC is standing a few feet back from lauren, Lauren begins getting closer to the deer still eating, her back is turned to the MC
    with dissolve

    u "Why are you walking towards it?!"

    scene v13s46_6b # FPP. v13s46_6a lauren looking at MC, slight smile, mouth open, deer still eating but is now within arms reach.
    with dissolve

    la "*Whispers* I want to see if it'll eat out of my hand! I have some snacks in my pocket..."

    scene v13s46_6c # FPP. same as v13s46_6b Lauren holds out her hand holding the granola bar towards the deer, deer is still eating, laurens face is visible, slight smile, mouth open
    with dissolve

    la "*Whispers* Here Deerie, Deerie!"

    scene v13s46_6d # FPP. same as v13s46_6c laurens mouth closed
    with dissolve

    u "*Whisper* LAUREN!!"

    scene v13s46_6c
    with dissolve

    la "Shhh..."

    scene v13s46_6c
    with dissolve

    la "Here Deerie, Deerie."

    scene v13s46_6e # same as v13s46_6c the deer looks up at Lauren and slowly starts walking toward her
    with dissolve

    la "*Whispers* It's actually coming to me!"

    scene v13s46_6f # same as v13s46_6e FPP. The deer gets up to Lauren and eats the granola bar out of her hand
    with dissolve

    la "*Whispers* Oh my gosh, [name]! Walk over here already, would you?"

    scene v13s46_6f
    with dissolve

    u "*Sighs*"

    scene v13s46_6g # FPP. same as MC v13s46_6f walks over to Lauren and the deer and is also now within arms reach of the MC
    with dissolve

    u "He must be used to people. How is he so calm?"

    scene v13s46_6g
    with dissolve

    la "I'm sure some of the people who come on this trail feed him snacks every once in a while."

    scene v13s46_6h # FPP. same as v13s46_6g The deer looks at the MC and starts sniffing
    with dissolve

    la "He's looking for food from you."

    scene v13s46_9 # TPP. the deer sniffs the MC's crotch, MC shocked mouth open, Lauren full smile mouth open with a hand attempting to cover her mouth
    with dissolve

    pause 0.75

    scene v13s46_10 # FPP. show just the deer Mc puts his hand out to the deers mouth
    with dissolve

    u "Sorry, buddy. I don't have anything, see?"

    scene v13s46_10a # FPP. The deer bites MC's hand
    with dissolve

    u "OWWWUH! WHAT THE FUCK?!"

    scene v13s46_11 # FPP. show deer running away, show lauren laughing, full smile, mouth open
    with dissolve

    la "What happened?! *Laughs*"

    scene v13s46_11a # FPP. same as v13s46_11 lauren no longer laughing, mouth closed
    with dissolve

    u "He fucking bit me!"

    scene v13s46_11
    with dissolve

    la "*Laughs* Should've had some food for him."

    scene v13s46_11a
    with dissolve

    u "You're actually blaming me for what a deer did?"

    scene v13s46_11
    with dissolve

    la "Nature is closed-minded, you should've known better. *Chuckles*"

    scene v13s46_11a
    with dissolve

    u "So, I gotta be smart because he's stupid, is basically what you're saying?"

    scene v13s46_11
    with dissolve

    la "If that's how you wanna put it. *Chuckles*"

    scene v13s46_11a
    with dissolve

    u "I'm getting back on my bike."

    scene v13s46_11b # FPP. same as v13s46_11 no longer laughing, head tilted, slight smile, mouth open
    with dissolve

    la "Aww! Poor baby."

    scene v13s46_12 # TPP. MC and Lauren get back on the bike
    with dissolve

    pause 0.75

    if lauren.relationship.value >= Relationship.GIRLFRIEND.value:
        scene v13s46_4a
        with dissolve

        la "I hope this is what it's always like."

        scene v13s46_4
        with dissolve

        u "What do you mean?"

        scene v13s46_2a
        with dissolve

        la "Us, just us. Out here in the world just enjoying life."

        scene v13s46_2a
        with dissolve

        la "No matter what may happen, I don't want life to become dull."

        scene v13s46_2
        with dissolve

        menu:
            "Keep the spark":
                scene v13s46_2
                with dissolve

                u "We'll keep the spark alive, Lauren. It's important for any couple to do that. Can't just grow old and bitter, haha."

                scene v13s46_2a
                with dissolve

                la "*Chuckles* We think alike."

            "We'll get tired":
                scene v13s46_2
                with dissolve

                u "Like everyone Lauren, we'll get tired eventually and grow old one day. That's just how things work, you know?"

                scene v13s46_2a
                with dissolve

                la "That doesn't mean we can't attempt to keep the spark alive. Instead of biking the trail next time we could walk it."

                scene v13s46_2
                with dissolve

                u "If my legs work, maybe. *Chuckles* Who knows, I may be in a wheelchair by then."

                scene v13s46_2a
                with dissolve

                la "*Laughs* Oh my gosh, stop."

    else: 
        scene v13s46_2a
        with dissolve

        la "Doing this sort of thing with a friend is nice, but I can imagine growing old and walking these trails with my partner one day."

        scene v13s46_2
        with dissolve

        u "It's a pretty long walk. *Chuckles*"

        scene v13s46_2a
        with dissolve

        la "*Laughs* Oh my gosh, stop."

    scene v13s46_2b # FPP. same as v13s46_2a Lauren stops her bike, and gets off her bike
    with dissolve

    la "*Whispers* [name], stop! For real, stop..."

    stop music fadeout 3
    play music "music/v13/Track Scene 46_3.mp3" fadein 2

    scene v13s46_2c # FPP. same as v13s46_2b MC stops his bike, and gets off his bike
    with dissolve

    u "What, more deer?"

    scene v13s46_13 # FPP. lauren looking at MC, slight smile, mouth open, show a slightly hidden path heading into the forest where a small clearing is slightly visible
    with dissolve

    la "No. *Chuckles* Do you hear that noise?"

    scene v13s46_13a # FPP. v13s46_13 lauren mouth closed
    with dissolve

    u "What noise?"

    scene v13s46_13
    with dissolve

    la "Listen... It sounds like crying! This way."

    scene v13s46_14 # TPP. show lauren heading into the hidden path with MC following behind her
    with dissolve

    pause 0.75

    scene v13s46_13b # FPP. same as v13s46_13 lauren and MC are deeper in the woods just outside the small clearing where a womans head is slightly visible, mouth open, eyes closed, having sex expression
    with dissolve

    la "I... I think they're having sex!"

    scene v13s46_13c # FPP. same as v13s46_13b laurens mouth is closed
    with dissolve

    u "Holy..."

    scene v13s46_13b
    with dissolve

    la "We should get closer and see. *Chuckles*"

    scene v13s46_13c
    with dissolve

    menu:
        "What?! No way":
            scene v13s46_13c
            with dissolve

            u "What?! No way... You're being extra freaky right now. *Chuckles*"

            scene v13s46_13b
            with dissolve

            la "Okay, maybe I am. *Laughs*"

            scene v13s46_13c
            with dissolve

            u "Let's go ahead and head back before they see us creepin', you weirdo."

        "Haha, okay":
            $ add_point(KCT.TROUBLEMAKER)
            scene v13s46_13b
            with dissolve

            $ grant_achievement("voyeur")
            u "Okay, lead the way. *Chuckles*"

            scene v13s46_15 # FPP. MC and Lauren sneak closer to the couple, just laurens head is visible full smile mouth open looking at the couple and find them fully nude in the arch sex position, male body should resemble an arch, google search sex position 173 arch, first google image for reference
            with dissolve

            pause 0.75

            scene v13s46_15a # FPP. same as v13s46_15 womans feet flat with the ground, man and woman are looking at each other, man mouth closed, woman mouth open, both smiles
            with dissolve

            pause 0.75

            scene v13s46_15b # FPP v13s46_15a womans extends legs to be on tippy toes, woman mouth closed, man mouth open
            with dissolve

            pause 0.75

            scene v13s46_15a
            with dissolve

            pause 0.75

            scene v13s46_15b
            with dissolve

            pause 0.75

            play sound "sounds/twig.mp3"
            scene v13s46_16 # FPP. show just laurens foot stepping on a branch
            with dissolve

            pause 0.75

            scene v13s46_15c # FPP. same as v13s46_15a lauren looking at MC slight scared mouth open, man and woman looking at MC and lauren, man is fully angry, mouth open, woman is fully shocked, mouth open, attempting to cover her body
            with dissolve

            la "*Whisper* Shoot!"

            scene v13s46_15d # FPP. same as v13s46_15c lauren looking at the couple, lauren mouth closed
            with dissolve

            gitw "HEY YOU FUCKING WEIRDOS! CAN'T YOU SEE THAT WE WANTED SOME PRIVACY?! FUCKING PERVERTS!"

            scene v13s46_15e # FPP. same as v13s46_15d lauren mouth open
            with dissolve

            la "So sorry! W-we were just... BYE!"

            scene v13s46_15d
            with dissolve

            u "*Laughs* Busted..."

    scene v13s46_17 # TPP. Mc and Lauren start walking toward the bikes, looking at each other, half smiles, mouths open
    with dissolve

    pause 0.75

    scene v13s46_13a
    with dissolve

    u "You really wanted to be a peeping Tom today, huh?"

    scene v13s46_13
    with dissolve

    la "Oh, come on! I was just curious.*Chuckles*"

    scene v13s46_13a
    with dissolve

    u "Hmm, okay. Whatever you say..."

    scene v13s46_18 # TPP. # MC and Lauren get on their bikes and leave to the pick/drop spot at the beach
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v13s47