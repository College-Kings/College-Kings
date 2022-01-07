# SCENE 23: MC Walking Home
# Locations: Sidewalk/Alley
# Characters: MC (Outfit 9), Josh (Outfit 1)
# Time: Afternoon
label v10_aft_walk_home:

    play music "music/v10/Track Scene 23.mp3" fadein 2

    scene v10smwh1 # TPP. Show MC walking on the sidewalk. Normal expression, mouth closed.
    with fade

    u "(Man, it feels like time is going by fast...)"

    scene v10smwh1a # TPP. Same camera as v10smwh1. MC stops on sidewalk outside of an alley because he sees something. Normal expression, mouth closed.
    with dissolve
    
    pause 0.75

    scene v10smwh2 # FPP. POV is MC looking into the alley. Show someone fishy in a hoodie handing something over to Josh.
    with dissolve
    
    pause 0.75

    scene v10smwh2a # FPP. Same camera as v10smwh2. Show someone fishy in a hoodie rushing away from Josh and disappearing.
    with dissolve

    u "(Is that Josh? And who in the world was that? Maybe I should check it out.)"

    scene v10smwh2b # FPP. Same camera as v10smwh2. Show Josh alone in the alley after the fishy guy rushes off.
    with dissolve
    menu:
        "Check it out":
            $ add_point(KCT.BRO)
            scene v10smwh3 # FPP. POV is MC and Josh close in the alley, talking. Show Josh, normal expression, mouth closed.
            with fade

            u "Hey bro, what are you doing here?"

            scene v10smwh3a # FPP. Same camera as v10smwh3. Show Josh, normal/content expression, mouth open.
            with dissolve

            jo "Hey [name]! Surprised to see you up this early, must've had a really boring night."

            if helpJosh: # If MC went to the drug deal with Josh
                scene v10smwh3
                with dissolve

                u "*Clears throat* Should I be prepared to get jumped again?"

                scene v10smwh3a
                with dissolve

                jo "Jumped! What are you talking about? Man I'm just hanging out in the-"    
            else: # If MC didn't go to the drug deal
                scene v10smwh3
                with dissolve

                u "*Clears throat* So, what brings you here?"

                scene v10smwh3a
                with dissolve

                jo "You know, I'm just chillin. Just hanging out in the-"

            scene v10smwh3a # FPP. Same camera as v10smwh3. Show Josh looking down towards the ground, sheepish/slightly embarrassed expression, mouth open.
            with dissolve

            jo "It would seem kinda stupid to just be hanging out in the alley huh?"

            scene v10smwh3c # FPP. Same camera as v10smwh3. Show Josh, sheepish/slightly embarrassed expression, mouth closed.
            with dissolve

            u "Just a little bit."

            scene v10smwh3a
            with dissolve

            jo "Look man, do we really have to talk about this?"

            scene v10smwh3c
            with dissolve
            menu:
                "Yes":
                    $ v10_josh_alley_yes = True
                    scene v10smwh3c
                    with dissolve

                    u "I just wanna make sure we don't have a repeat of last time."

                    scene v10smwh3d # FPP. Same camera as v10smwh3. Show Josh, smiling, mouth open.
                    with dissolve

                    jo "Trust me, you have nothing to worry about. That definitely taught me a lesson I won't forget. *Smiles* I'm being smart."

                    scene v10smwh3
                    with dissolve

                    u "I'm not judging and you can do whatever you want, but... I gotta ask, do you enjoy doing this?"

                    scene v10smwh3a
                    with dissolve

                    jo "Hell no, I hate this shit."

                    scene v10smwh3
                    with dissolve

                    u "Then why are you doing it?"

                    scene v10smwh3a
                    with dissolve

                    jo "I need the money."

                    scene v10smwh3
                    with dissolve

                    u "For what? Didn't your dad-"

                    scene v10smwh3a
                    with dissolve

                    jo "My dad cut me off."

                    scene v10smwh3
                    with dissolve

                    u "What?! I thought-"

                    scene v10smwh3a
                    with dissolve

                    jo "I didn't go to the military! So he cut me off."
                    jo "He said if I didn't spend at least four years in the military I wouldn't see a penny."
                    jo "So now I have to figure out how I'm gonna pay for school."

                    scene v10smwh3
                    with dissolve

                    u "Damn man, I'm sorry. I wish you would've told me sooner."

                    scene v10smwh3a
                    with dissolve

                    jo "I was just gonna do it until I had enough, but I'm hoping I won't have to do it much longer."
                    jo "I met this guy and he might be able to get me a scholarship."

                    scene v10smwh3e # FPP. Same camera as v10smwh3. Show Josh, smiling, mouth closed.
                    with dissolve

                    u "That'd be awesome. Shit, what's his name, maybe he can get me one too. *Chuckles*"

                    scene v10smwh3d
                    with dissolve

                    jo "Haha, he's some big shot. Can't remember his name honestly, but he's a bit intimidating."
                    jo "Kinda reminds me of my dad, but more flexible."
                
                "Let it go":
                    scene v10smwh3
                    with dissolve

                    u "As long as you know what you're doing."

                    scene v10smwh3a
                    with dissolve

                    jo "Thanks man."

            scene v10smwh3
            with dissolve

            u "Alright, let's get out of this alley."

            scene v10smwh3d
            with dissolve

            jo "Haha, yeah probably a good idea."

            scene v10smwh1b # TPP. Same camera as v10smwh1. MC and Josh walking out of the alley together, normal expressions, mouths closed.
            with fade

            pause 0.75

            scene v10smwh4 # FPP. POV is MC and Josh close on the sidewalk, talking. Show Josh, normal expression, mouth closed.
            with dissolve

            $ josh_europe = True
            u "I don't know why I haven't thought to ask you this before, but have you heard about the big Europe trip?"

            scene v10smwh4a # FPP. Same camera as v10smwh4. Show Josh, normal expression, mouth open.
            with dissolve

            jo "No, what's that?"

            scene v10smwh4
            with dissolve

            u "There's a student Europe trip that sounds pretty fun and I'm thinking about going. You interested?"

            scene v10smwh4a
            with dissolve

            jo "I don't know man, Europe's pretty far. Plus it's expensive. Who's going?"

            scene v10smwh4
            with dissolve
            menu:
                "I don't know":
                    scene v10smwh4
                    with dissolve

                    u "Honestly, I really don't know who's going, but it sounds fun, no?"

                    scene v10smwh4a
                    with dissolve

                    jo "Uhm, I don't really want to commit to anything, but I'll think about it some more and get back to you."

                    scene v10smwh4
                    with dissolve

                    u "Sounds good."
               
                "Hot girls":
                    scene v10smwh4c # FPP. Same camera as v10smwh4. Show Josh, smiling, mouth closed.
                    with dissolve

                    u "Lots of hot girls, that much I know. Reason enough for me to go!"

                    scene v10smwh4b # FPP. Same camera as v10smwh4. Show Josh, smiling, mouth open.
                    with dissolve

                    jo "Why didn't you lead with that? How many girls are we talking about?"

                    scene v10smwh4c
                    with dissolve

                    u "Loads and they're like reaaaallly hot. And anything can happen in Europe man."

                    scene v10smwh4b
                    with dissolve

                    jo "Damn, alright, sign me up dawg!"

                    scene v10smwh4c
                    with dissolve

                    u "Sick, I'll let the organizers know."

            scene v10smwh4
            with dissolve

            u "Anyway, I'ma head home now. Stay safe man."

            scene v10smwh4a
            with dissolve

            jo "Yeah, no doubt. I'll see you."

            scene v10smwh4d # FPP. Same camera as v10smwh4. Show Josh walking away down the sidewalk.
            with dissolve

            pause 0.5
        
        "Keep walking":
            $ add_point(KCT.TROUBLEMAKER)
            scene v10smwh2b
            with dissolve

            u "(No, that's his business. I'm not gonna babysit him.)"

    scene v10smwh1c # TPP. Same camera as v10smwh1. MC is standing on sidewalk when he notices that he just got a text. MC looks down at pocket.
    with fade

    u "(Phone buzzing, I should get that.)"

    scene v10smwh1c
    with dissolve

    play sound "sounds/vibrate.mp3"

    python:
        lauren.messenger.newMessage("Hey, wanna hang out? I have some free time in between study sessions.", force_send=True)
        lauren.messenger.addReply("Sure, on my way")
        lauren.messenger.newMessage(":)")

    label v10s23_phoneCheckLau:
        if lauren.messenger.replies:
            call screen phone
        if lauren.messenger.replies:
            u "(I should reply to Lauren)"
            jump v10s23_phoneCheckLau

    scene v10smwh1d # TPP. Same camera as v10smwh1. MC is looking at his phone.
    with dissolve
    
    u "(Guess I'm not going home.)"
   
    stop music fadeout 3
    jump v10_lauren_room