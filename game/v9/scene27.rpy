# SCENE 27: Training W/ Apes
# Locations: MC room at apes, Apes Gym
# Characters: MC (outfit 5), Cameron(outfit 2), ryan(gym clothes), caleb(gym clothes)
# Time: Friday Evening

label v9_train_w_apes:
    scene v9twa1 # FPP. Show Cameron in Bedroom, serious face, gesturing for MC to follow, mouth closed
    with dissolve

    pause 1

    scene v9twa2 # TPP. Show MC sat on his bed, surprised look, mouth closed
    with dissolve

    pause 1

    scene v9twa1
    with dissolve

    pause 1
    
    scene v9twa1a # FPP. Same camera as v9twa1, Show Cameron in Bedroom, serious face, gesturing for MC to follow, mouth open
    with dissolve
    ca "Let's go!"

    scene v9twa1b # FPP. Same camera as v9twa1, Show Cameron in Bedroom, serious face, arms now down, mouth closed
    with dissolve

    u "What's up? Is something wrong?"

    if hl_punch:
        scene v9twa1c # FPP. Same camera as v9twa1, Show Cameron in Bedroom, serious face, arms now down, mouth open
        with dissolve

        ca "Not for you, Rocky!"

        scene v9twa1b
        with dissolve

        u "(Whew!)"

        scene v9twa1c
        with dissolve

        ca "I'm just whipping you punks into shape for tomorrow."

    else:
        scene v9twa1c
        with dissolve

        ca "What's wrong is how a punk ass bitch got into my frat."

        scene v9twa1b
        with dissolve

        u "Who?"

        scene v9twa1c
        with dissolve

        ca "You're joking, right?"

        ca "Get in! I'm gonna whip your punk ass into shape if it kills you!"

    scene v9twa3 # TPP. Show MC and Cameron entering Apes gym, neutral look, mouths closed
    with dissolve

    pause 1

    scene v9twa4 # FPP. Show Caleb and Ryan in the Apes Gym, standing together, slight nervous look, mouthes closed
    with dissolve

    pause 1

    scene v9twa5 # FPP. Show Cameron, hands behind back, serious look, mouth open
    with dissolve

    ca "Maggots!"

    scene v9twa5a #FPP. Same Camera as v9twa5, Show Cameron, hands behind back, serious look, mouth closed
    with dissolve

    u "(What the fuck?)"

    scene v9twa5
    with dissolve

    ca "Today is my lucky day. I get to turn you boys into men!"

    if hl_punch:
        scene v9twa5a
        with dissolve

        u "Hey, man, I think you're nice and all but you're not my type."

        scene v9twa5
        with dissolve

        ca "Don't get too cocky yet, Rocky."

    else:
        scene v9twa5a
        with dissolve

        u "(Haha. I wonder if he even knows what he just said.)"

        scene v9twa5 # FPP. Same Camera as v9twa7, Show cameron punching bag, neutral expersion, mouth open
        with dissolve

        ca "You maggots think that was funny?"

    ca "If you assholes think you're making a fool out of this house tomorrow, you got another thing coming."

    if hl_punch:
        ca "This guy here! He's the only one of you shit stains I trust to wear our name. He's gonna pull a big crowd for the Brawl and they'll all be chanting his name. [name]! [name]!"

        scene v9twa5c # FPP. Same Camera as v9twa5, Show Cameron, holding fist up at camera, serious look, mouth open
        with dissolve

        ca "The rest of you, I don't trust for shit."

        scene v9twa5
        with dissolve

    else:
        ca "And you! How the fuck do you call yourself an Ape? Do you know how many people have seen you get your ass kicked? Right before the big fight? Could you be more stupid?"

        scene v9twa5a # FPP. Same Camera as v9twa5, Show Cameron, holding fist up at camera, serious look, mouth closed
        with dissolve

        u "(Not falling for that.)"

        scene v9twa5
        with dissolve

    ca "But that's all about to change."

    scene v9twa6 # TPP. Show Cameron pointing at Caleb, serious face, mouth open
    with dissolve

    ca "You. Weight bench. Don't stop til you puke!"

    scene v9twa6a #TPP. Same camera as v9twa6, Show Cameron pointing at Ryan, serious face, mouth open
    with dissolve

    ca "And you, go punch something."

    if hl_punch:
        scene v9twa5
        with dissolve

        ca "And Rocky. I'm sure you don't need my help. You're already famous."

        menu:
            "Be confident" (bro=1.0):
                $ reputation.add_point(RepComponent.BRO)

                scene v9twa5a
                with dissolve

                u "Yeah, I dropped that guy!"

                scene v9twa5
                with dissolve

                ca "Not so fast. There's more to being a champion than one lucky punch."

                scene v9twa5f # FPP. Same Camera as v9twa5, Show Cameron, holding hands up open palm to camera, serious look, mouth closed
                with dissolve

                ca "When I get done with you, no punk will even THINK about starting shit again. You hear me?"

            "Be humble" (boyfriend=1.0):
                $ reputation.add_point(RepComponent.BOYFRIEND)

                scene v9twa5a # FPP. Show Cameron, hands behind back, serious look, mouth open
                with dissolve

                u "Aww, I don't know. It wasn't that big a deal."

                scene v9twa5
                with dissolve

                ca "Nonsense!"

                ca "You're our main event! That's why we gotta make extra sure you're ready."

                scene v9twa5a
                with dissolve

                u "I feel alright."

                scene v9twa5
                with dissolve

                ca "Alright? Alright's not good enough! Let's go!"

        scene v9twa7 # FPP. Show cameron stood by punching bag, hand on bag, neutral expersion, mouth open
        with dissolve

        ca "You got an arm. That's clear. What you need is options."

        scene v9twa7a # FPP. Same Camera as v9twa7, Show cameron stood by punching bag, hand on bag, neutral expersion, mouth closed
        with dissolve

        u "Options?"

        scene v9twa7
        with dissolve

        ca "Chris is no dumbass. He's seen your punch a thousand times by now and he's training those Wolf cubs to strike first. They're gonna be worried about that punch, so we're not gonna give it to 'em."

        scene v9twa7a
        with dissolve

        u "Um."

        scene v9twa7
        with dissolve

        ca "At least not right away."

        scene v9twa7b # FPP. Same Camera as v9twa7, Show cameron punching bag, neutral expersion, mouth open
        with dissolve

        ca "Footwork. That's where it's at. You have the power behind that fist. They're expecting it. You gotta hit 'em WHERE they're not expecting."

        scene v9twa7c # FPP. Same Camera as v9twa7, Show cameron pointing at the floor, neutral expersion, mouth open
        with dissolve

        ca "BAM! See that?"

        ca "Those are baby Wolf nuts on the floor!"

        scene v9twa7
        with dissolve

        ca "Now your turn. Imagine him standing right in front of you and get as many sneak shots in as possible. Balls, kidneys, throat, I don't care. Go for the kill!"

        menu:
            "Be pumped" (bro=1.0):
                $ reputation.add_point(RepComponent.BRO)

                scene v9twa8 # TPP. Show MC Punching bag, back to camera, in boxing stance
                with dissolve

                u "Yeah!"

                u "Balls! Kidneys! Throat!"

                ca "Now you got it! I'm gonna go check on these punks. Make me proud!"

            "Be concerned":
                scene v9twa7a
                with dissolve

                u "(I'm not trying to send someone to the fucking hospital here.)"

                scene v9twa7d # FPP. Show cameron stood by punching bag, hand on bag, dissapointed expersion, mouth open
                with dissolve

                ca "Come on, man. We fight to win in this house. Are you an Ape or not?"

                scene v9twa7a
                with dissolve

                u "Of course!"

                scene v9twa7d
                with dissolve
                ca "Then show me!"

                scene v9twa8
                with dissolve

        ca "Good! I'll be back after I whip these pussies into something resembling a man."

    else:
        scene v9twa5
        with dissolve

        ca "Well, well, well."

        ca "What am I to do with you?"

        menu:
            "Ask for help":
                scene v9twa5a
                with dissolve

                u "You can show me some moves so I don't embarrass the fuck out of myself. And this house."

                scene v9twa5
                with dissolve

                ca "Smart man. I'd hate to have to knock your ass out so soon after your last beating."

                scene v9twa5a
                with dissolve

                u "*Grumbling* Thank you."

                scene v9twa5
                with dissolve

                ca "Great! Over here!"

            "Stay quiet" (boyfriend=1.0):
                $ reputation.add_point(RepComponent.BOYFRIEND)

                scene v9twa5a
                with dissolve

                u "(Great. If he's gonna make Caleb puke on the weight bench, I can't wait to see what he has in store for me.)"

                scene v9twa5
                with dissolve

                ca "Well? What should I do with you?"

                ca "Can't even stand up for yourself against one of us. How do you expect to represent the house in the Brawl?"

                scene v9twa5a
                with dissolve

                u "(Not like I was asked if I wanted to fight in the first place.)"

                u "Look. I was just trying not to fight in the middle of school. You want me to get expelled or something? Geez."

                scene v9twa5
                with dissolve

                ca "Come here."

        scene v9twa7
        with dissolve

        ca "If you were a Wolf and you knew your opponent was a pussy who got his ass knocked out, what would you be thinking?"

        scene v9twa7a
        with dissolve

        u "(No, tell me how you REALLY feel.)"

        u "I'd be thinking he had something to prove."

        scene v9twa5f # FPP. Same Camera as v9twa5, Show Cameron, holding hands up open palm to camera, serious look, mouth open
        with dissolve

        ca "And what would you do with that?"

        scene v9twa5e
        with dissolve

        u "Charge him."

        scene v9twa5
        with dissolve

        ca "Yes! Not useless after all."

        ca "Your guy's gonna come off that bell like a cheetah and you have to be ready."

        scene v9twa9 # FPP. Show cameron in boxing stance in centre of room, serious face, mouth closed
        with dissolve

        pause 0.75

        scene v9twa9a # FPP. Same camera as v9twa9, Show cameron in boxing stance in centre of room, punching forward,  serious face, mouth closed
        with dissolve

        pause 0.75

        scene v9twa10 # TPP. Show MC in boxing stance in centre of room, serious face, mouth closed
        with dissolve

        pause 0.75

        scene v9twa10a # TPP. same camera as v9twa10, Show MC in boxing stance in centre of room, punching forward,  serious face, mouth closed
        with dissolve

        pause 0.75

        scene v9twa11 # TPP. Show Cameron sweeping MC's Leg out from under him while MC in boxing position, MC surprised face, cameron neutral, mouths closed
        with dissolve

        pause 0.75

        scene v9twa12 # FPP. MC now on the floor, camera looking up at cameron, cameron smug look, mouth closed
        with dissolve

        u "Hey! What the fuck?"

        scene v9twa12a # FPP. same camera as v9twa12, MC now on the floor, camera looking up at cameron, cameron smug look, mouth closed
        with dissolve

        ca "Did you see that coming?"

        scene v9twa12
        with dissolve

        u "Fuck no!"

        scene v9twa12a
        with dissolve

        ca "Neither will he!"

        scene v9twa11a # TPP. Same camera as v9twa 11, Show Cameron helping MC up,neutral faced, Mc mouth closed, Cameron mouth open
        with dissolve

        ca "Now, give me a hundred of those. I want you sweeping legs in your sleep tonight!"

        scene v9twa11b # TPP. Same camera as v9twa 11, Show Mc Practicing sweeping leg, crouched position right leg stuck out to side, mouth closed
        with dissolve

        ca "When I get done with those guys, we'll talk about sneak shots. Balls, kidneys, throat. Sweep him to the ground and strike fast!"

        ca "One hundred. I'll be counting!"

        "*Crash*"

    scene v9twa13 # FPP. Show Caleb on the floor next to the weight bench (fallen off it ), looks in pain, mouth closed
    with fade

    ca "Alright maggots! That's your cue. Great workout!"

    scene v9twa14 # FPP. Show Ryan helping Caleb up off the floor, ryan neutral look, caleb looks in pain, mouths closed
    with dissolve

    ca "Took you long enough. Good job. I thought you'd drop a long time ago. Puke or pass out. That's how you know you're done!"

    scene v9twa15 # FPP. Show Ryan and Caleb walking out the gym, camera from behind them
    with dissolve

    pause 1
    
    jump v9_call_w_lindsey