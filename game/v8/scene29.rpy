# SCENE 29: JOSH'S HOUSE
# Locations: Josh's room
# Characters: MC (outfit 3), Josh (outfit 1), Amber (outfit 3)
# Time: Monday night, Tuesday morning
# IMPORTANT_NOTE: Josh is injured for the entire duration, so he should look the same as how he was at the end of Scene 28. Unless otherwise mentioned, Josh should be looking weak and in pain for the entire scene until Tuesday morning

### Extra audio files needed (coded but commented out for now) ###
# TV_amb.mp3 - Generic TV show sound for ambience
# flush.mp3 - Toilet flushing sound

label after_drugs:
    if not helpJosh:
        scene v8josh10 # TPP. Showing Josh sitting on the ground outside his room door supporting himself using the wall
        with Fade(0.75, 0.25, 0.75)
        pause 0.75

        scene v8josh11 # TPP. Showing MC rushing towards Josh, looking concerned
        with dissolve
        pause 0.75

        scene v8josh12 # TPP. Showing MC picking Josh up from the ground, concerned, mouth open
        with dissolve
        u "Hey man, are you alright?"

        scene v8josh12a # TPP. Josh is now standing with MC's support, with his hands draped around MC's shoulders. Josh mouth open
        with dissolve
        jo "Y-yeah, I'm fi-fine *Groans*"

    else:
        scene v8josh13 # TPP (This is not the continuation of v8josh12a, so they're far from the door still). Showing MC and Josh walking towards his room door, with Josh's hands draped around MC's shoulders
        with Fade(0.75, 0.25, 0.75)
        pause 0.5
        jo "*Groans*"

    play sound "sounds/dooropen.mp3"
    play music "music/mchill1.mp3"

    scene v8josh14 # TPP (This is the next scene for both v8josh12a and v8josh13, in different paths of course, so both the transitions should look smooth). Show MC opening the room door (half open) with Josh still taking support from MC
    with dissolve
    pause 0.75

    scene v8josh15 # TPP. MC walking Josh inside the building (they crossed the doorway and entered the living room now). Josh looking towards the couch (the first one after entering), mouth open
    with dissolve
    jo "Ju- Just lay me on the couch. Can't go all the way upstairs at the moment."

    scene v8josh16 # TPP. MC laid Josh down on the couch (the first one after entering) with his head towards right side, propped his head up with a pillow and is now standing near the couch looking at Josh
    with dissolve
    pause 0.75

    scene v8josh17 # FPP (Continuation of v8josh16). Josh looking into the camera, mouth closed
    with dissolve
    u "Hey man, can I get you anything? Water? A blanket?"

    scene v8josh17a # Same as v8josh17 but Josh mouth open
    with dissolve
    jo "Water. And ice. A bag of ice."

    scene v8josh17
    with dissolve
    u "Be right back."

    scene v8josh18 # TPP. MC placed a glass of water on a stool (like the one from kitchen) near the couch and is now giving Josh an ice pack or a bag of ice
    with dissolve
    u "Here. I put a glass of water on the stool. Tell me if you need more."

    scene v8josh19 # FPP (Continuation of v8josh18). Josh holding the ice pack to his face while looking into the camera, mouth open
    with dissolve
    jo "Thanks man. I'm sorry."

    scene v8josh19a # Same as v8josh19 but Josh mouth closed
    with dissolve
    if helpJosh:
        u "It's ok man. I'm just glad we weren't killed. Do you want me to take you to the hospital?"
    else:
        u "Don't be. I'm just glad you got out alive. Do you want me to take you to the hospital?"

    scene v8josh19
    with dissolve
    jo "No, no, man. No hospitals. I'll be fine I just gotta..."

    scene v8josh19b # Josh groaning in pain, eyes closed and teeth clenched
    with dissolve
    jo "*Groans*"

    scene v8josh19
    with dissolve
    jo "...relax and take it easy."

    scene v8josh19a
    with dissolve
    u "Yeah, you do that. I'll be right here."

    scene v8josh19d # FPP (This should not be using the same camera as v8josh19, treat it as a standalone render). View of the living room (the TV, table, etc. There's a TV remote on the table) as seen from MC's position
    with dissolve
    u "Anything else you want me to..."

    scene v8josh19c # Josh falling asleep, eyes closed and somewhat relaxed face
    with dissolve
    u "(Oh...)"
    u "(Guess I'm staying here for a few hours.)"

    scene v8josh20 # TPP. MC taking the TV remote from the table
    with dissolve
    pause 1

    # $ renpy.music.set_volume(0.5, channel="ambience")
    # play ambience "sounds/TV_amb.mp3" fadein 2

    scene v8josh21 # TPP. Show MC holding the remote and turning the TV on while sitting on the other couch (TV screen is on in this image). Neutral expression, mouth closed if his face is visible
    with dissolve
    pause 0.5

    scene v8josh22 # TPP. Close up of MC looking at his phone, neutral expression, mouth closed
    with dissolve
    u "(I should call Amber and tell her what happened.)"

    play sound "sounds/calling.mp3"

    scene v8josh22a # MC holding the phone to his face, looking somewhat upset, mouth closed
    with dissolve
    pause 1

    play sound "sounds/answercall.mp3"

    scene v8josh22a
    with dissolve
    am "Heyyyy!"

    scene v8josh22b # Same as v8josh22a but MC mouth open
    with dissolve
    u "Hey."

    scene v8josh22a
    with dissolve
    am "What's wrong? You sound upset."

    scene v8josh22b
    with dissolve
    u "I am. I'm at Josh's house. He did a uhh, drug deal and got beaten up pretty bad. I'm here keeping an eye on him."

    scene v8josh22a
    with dissolve
    am "What!? Ugh, that fucking idiot."
    am "I'll be right over. I'm gonna give him so much shit!"

    scene v8josh22b
    with dissolve
    u "He's sleeping at the moment, Amber, and I..."

    play sound "sounds/rejectcall.mp3"
    pause 0.5

    scene v8josh22
    with dissolve
    u "(Great. Can this day get any worse?)"

    scene v8josh23 # TPP. Show MC sitting on the couch watching TV, neutral expression, mouth closed
    with Fade(1, 0.25, 0.5)
    pause 0.75

    play sound "sounds/knock.mp3"
    pause 0.75

    scene v8josh21
    with dissolve
    stop ambience
    pause 0.5

    play sound "sounds/dooropen.mp3"

    scene v8josh24 # TPP. Show MC opening the door (Door is half open. For context, Amber is standing outside)
    with dissolve
    pause 0.5

    scene v8josh24a # (Door open now) Amber storming inside brushing past the MC, looking upset but also slightly angry, mouth open. MC slightly taken aback from her reaction, mouth closed
    with dissolve
    am "WHERE IS HE!?"

    scene v8josh24b # Amber walked past MC (but still near the doorway). She's still looking upset, mouth closed. MC turned towards Amber, looking a bit concerned, mouth open
    with dissolve
    u "He's sleeping on the couch now. He had it pretty bad."

    scene v8josh25 # FPP (Continuation of v8josh24b). Amber turned towards the MC. She's looking upset, concerned, mouth open
    with dissolve
    am "Fuck! What the hell was he thinking?"

    scene v8josh25a # Same as v8josh25 but Amber mouth closed
    with dissolve
    u "I dunno, he wanted money and thought it was a good way to get some."

    scene v8josh25
    with dissolve
    am "And he thought he could do this alone? Idiot!"

    if helpJosh:
        scene v8josh25a
        with dissolve
        u "Actually, uhh... I went with him."

        scene v8josh25b # Amber looking shocked, mouth open
        with dissolve
        am "You did? How did you let this happen?"

        if s28_fightWinner == "MC": # MC beat the thugs:
            scene v8josh25c # Same as v8josh25b but Amber mouth closed
            with dissolve
            u "I tried to stop it. There were two of them and one had a pipe."
            u "While I fought the fat guy, the other guy got into it with Josh."
            u "By the time I was done beating that guy's ass, Josh was already on the ground all fucked up."

            if v8_dodged_pipe:
                scene v8josh25b
                with dissolve
                am "And the other guy?"

                scene v8josh25c
                with dissolve
                u "I beat the shit outta him."

            scene v8josh25d # Amber less upset, relaxed and smiling a little, mouth open
            with dissolve
            am "Well, that is something at least."

            scene v8josh25e # Amber serious, mouth open
            with dissolve
            am "Thank you for being there for him. I would have talked him out of it."

            scene v8josh25f # Same as v8josh25e but Amber mouth closed
            with dissolve
            u "I tried. But he wouldn't listen. Maybe I should have tried harder."

            #scene v8josh25g # Amber brushing MC's cheek, empathetic, comforting smile, mouth open (Use DoF so Amber's hand is blurred)
            scene v8josh25d
            with dissolve
            am "Hey, it's not your fault. I'm sorry I yelled. You did more than anyone had a right to expect."

            #scene v8josh25h # Same as v8josh25g but Amber mouth closed
            scene v8josh25c
            with dissolve
            u "It's ok. I mean, we're alive, and I swiped the cash from them."

            scene v8josh25e
            with dissolve
            am "Do you still have the shit?"

            scene v8josh25f
            with dissolve
            u "Yeah I do, why?"

            scene v8josh25e
            with dissolve
            am "Give it to me."

            scene v8josh25f
            with dissolve
            u "Why?"

            scene v8josh25e
            with dissolve
            am "Just give it to me. Trust me."

            scene v8josh25f
            with dissolve
            u "Alright. Let me get it."

            scene v8josh29 # TPP. Show Amber standing near Josh (who is resting on the couch) looking at him, upset and mouth closed
            with dissolve
            pause 2

            scene v8josh26 # TPP. (For context, MC and Amber walked into the living room) MC handing over the cocaine bag (from scene 28) to Amber somewhere in front of Josh's couch. Amber looking serious, mouth open. MC neutral expression, mouth open
            with fade
            u "Here."
            am "Be right back."

            scene v8josh27 # TPP (continuation of v8josh26). MC sits on the couch (the one in front of TV) neutral expression, mouth closed. Amber is not in the shot
            with dissolve
            u "(What is she up to?)"

            play sound "sounds/flush.mp3"
            pause 0.75

            scene v8josh27a # Amber walking towards the couch to sit beside MC, looking at him neutral expression. MC neutral expression, mouth open
            with dissolve
            u "Did you just..."

            stop sound
            scene v8josh27c # Amber sits beside MC, smiling a little, looking at him, mouth closed. MC neutral expression, mouth closed
            with dissolve
            pause 0.75

            scene v8josh28 # FPP (continuation of v8josh27c, so both MC and Amber are sitting on the couch. MC is sitting towards Josh to avoid showing him in all renders). Amber confident, smiling a little, mouth open
            with dissolve
            am "You bet your ass I did. Why?"

            scene v8josh28a # Same as v8josh28 but Amber mouth closed
            with dissolve
            u "I'm actually glad you did that. I don't want him doing this shit or being involved with it all."

            if ending == "amber":
                scene v8josh28
                with dissolve
                am "You didn't have a problem with it when we did it, did you?"

                scene v8josh28a
                with dissolve
                u "Not enough to say no if it meant I could spend time with you."

                scene v8josh28b # Amber flirty grin, mouth open
                with dissolve
                am "Wow, that was smooth. Not bad, [name]. Not bad."

                scene v8josh28a
                with dissolve
                u "Haha, thanks."
                u "I'm staying here. You doing anything tonight?"

            else:
                scene v8josh28
                with dissolve
                am "I don't care that he does it, since we all have problems..."

                scene v8josh28c # Amber concerned, mouth open
                with dissolve
                am "...but to think he was in any frame of mind to pull this off is just stupid."
                am "He needs to stop before he's caught... or gets killed."

                scene v8josh28d # Same as v8josh28c but Amber mouth closed
                with dissolve
                u "Yeah, I agree with you there."
                "..."

                scene v8josh28
                with dissolve
                am "So, now what?"

                scene v8josh28a
                with dissolve
                u "I'm staying here. You doing anything tonight?"

        else:
            scene v8josh25c
            with dissolve
            u "I tried to stop it. There were two of them and one had a pipe."
            u "While I fought the guy with the pipe, the other guy got into it with Josh."

            scene v8josh25a
            with dissolve
            u "I just... wasn't good enough to stop them I guess."

            scene v8josh25g
            with dissolve
            am "Hey, it's ok. You tried. You did more than anyone had a right to expect."

            scene v8josh25h
            with dissolve
            u "Thanks. Let's uhh... go inside."

            scene v8josh29
            with dissolve
            pause 2

            scene v8josh27
            with dissolve
            pause 0.5

            scene v8josh27a
            with dissolve
            pause 0.5

            scene v8josh27c
            with dissolve
            pause 0.5

            scene v8josh28
            with dissolve
            am "*Sigh* So, now what?"

            scene v8josh28a
            with dissolve
            u "I'm staying here. You doing anything tonight?"

    else:
        scene v8josh25a
        with dissolve
        u "Yeah, I don't know what the hell he was thinking."
        u "I told him not to risk it but he wouldn't listen and went alone anyway."
        u "I uh... probably should've gone with him and maybe then this wouldn't have happened."

        scene v8josh25e
        with dissolve
        am "Hey, at least you're here taking care of him. I've had friends that wouldn't bat an eye."
        am "*Sigh* He needs to stop before he's caught... or worse, gets killed."

        scene v8josh25f
        with dissolve
        u "Yeah, I agree with you there."
        u "Let's uhh... go inside?"

        scene v8josh25e
        with dissolve
        am "Yeah..."

        scene v8josh29
        with dissolve
        pause 2

        scene v8josh27
        with dissolve
        pause 0.5

        scene v8josh27a
        with dissolve
        pause 0.5

        scene v8josh27c
        with dissolve
        pause 0.5

        scene v8josh28
        with dissolve
        am "*Sigh* So, now what?"

        scene v8josh28a
        with dissolve
        u "I'm staying here. You doing anything tonight?"

    scene v8josh28
    with dissolve
    am "And I'm staying here to help you with Dummy over there."

    scene v8josh28a
    with dissolve
    u "Oh! I'm glad. Wanna watch a movie to pass time?"

    scene v8josh28
    with dissolve
    am "Why not? Let me grab a beer and I'll be right with you. You want one?"

    scene v8josh28a
    with dissolve
    u "Yeah, a beer sounds fucking great, haha."

    scene v8josh28
    with dissolve
    am "I got you. Can you grab a blanket and a few pillows from the hall closet in the meantime?"

    scene v8josh28a
    with dissolve
    u "Yeah, of course!"

    scene v8josh28
    with dissolve
    am "Perfect!"

    scene v8josh30 # TPP. Show Amber and MC sitting on the couch with beers in hand and legs stretched with the table in front of them as leg-rest, and their legs covered in a single huge blanket. Place two fluffy pillows wherever you deem fit. They're both looking towards the TV, smiling and mouth closed. Show them from the front (maybe not directly front but from an angle) so the TV screen is not in the shot. From here on, room main lights should be turned off until next day morning, so the images should be darker. Avoid showing Josh's couch (which means MC is sitting towards Josh because otherwise he will be seen in FPP renders)
    with Fade(0.5, 0.25, 1.25)
    pause 1

    scene v8josh31 # FPP (Continuation of v8josh30 and beer in her hand in all renders starting with v8josh31). Amber looking into the camera, romantic smile and mouth open
    with dissolve
    am "Okay, fire it up!"

    # play ambience "sounds/TV_amb.mp3" fadein 2

    scene v8josh32 # FPP. Show the TV screen as seen from the MC's position. MC and Amber's legs can be seen in the shot (or the blanket covering their legs to be precise, try to show more of Amber)
    with Dissolve(1.5)
    pause 1

    scene v8josh30a # Show MC taking a sip from his beer, rest is essentially same
    with dissolve
    pause 1

    scene v8josh31
    with dissolve
    am "This is nice."

    scene v8josh31a # Same as v8josh31 but Amber mouth closed
    with dissolve
    u "Yeah..."

    scene v8josh31b # Amber looking towards the TV screen, smiling and mouth closed
    with dissolve
    pause 0.5

    scene v8josh32a # Same as v8josh32 but credits playing on TV screen and Amber is taking a sip from her beer
    with Fade(1, 0.25, 0.5)
    pause 1

    stop ambience fadeout 3

    scene v8josh31b
    with dissolve
    u "Damn, I love that movie."

    scene v8josh31a
    with dissolve
    pause 0.5

    scene v8josh31
    with dissolve
    am "Me too! Always makes me think of my dad playing this when we were kids."

    scene v8josh31a
    with dissolve
    u "You get along with your folks well?"

    scene v8josh31c # Amber melancholy, regret, mouth open
    with dissolve
    am "Not as much as I'd like. My mom is always criticizing us, my sister and I, like, nothing we do is ever good enough, you know?"

    scene v8josh31d # Same as v8josh31c but Amber mouth closed
    with dissolve
    u "Yeah, I know what you mean. My dad is never around and all I have is Julia, my stepmom."

    scene v8josh31c
    with dissolve
    am "What's she like?"

    scene v8josh31d
    with dissolve
    u "Funny. Kind. Really pretty and is always smiling."

    scene v8josh31c # Amber sarcastic smile, mouth open
    with dissolve
    am "Pretty, huh? You like her?"

    scene v8josh31a
    with dissolve
    u "No! Not like that!"

    scene v8josh31f # Amber laughing, mouth open
    with dissolve
    am "Hahaha! You should have seen your face!"

    scene v8josh33 # TPP. Show MC hitting Amber with a pillow playfully, both of them laughing and mouth open (beers still in hand, at least Amber's)
    with dissolve
    u "Not funny, Amber haha!"
    am "Hey, it was a bit funny, haha!"

    scene v8josh31a
    with dissolve
    u "What about your dad?"

    scene v8josh31c
    with dissolve
    am "We don't talk. It's kind of a sore subject at the moment."

    scene v8josh31d
    with dissolve
    u "I got you. No worries. You ever need to talk, you know where to find me."

    scene v8josh31
    with dissolve
    am "I do, and thanks for that. I may take you up on it one day."
    am "I'm really wiped though. I need to get some rest."

    scene v8josh31a
    with dissolve
    u "Yeah, me too. I'm beat. I'll take the floor, you get the couch."

    scene v8josh31
    with dissolve
    am "Aww, thanks. Goodnight, [name]!"

    stop music fadeout 3

    scene v8josh31a
    with dissolve
    u "Night, Amber."

    scene v8josh34 # TPP. Show MC, Amber and Josh sleeping in the living room, it's almost midnight. MC is sleeping on the floor (on a carpet or something), Amber is on the couch in front of TV and Josh is on the other bigger couch in the corner (If three of them don't fit in a single frame, show only MC and Amber) (MC and Amber sleeping in their outfits and not just underwear)
    with Dissolve(1.5)
    pause 2

    scene black
    with Dissolve(1)
    pause 0.5

    if ending == "amber" or reputation() == Reputations.POPULAR:
        if ending != "amber":
            call screen reputation_popup

        $ amberSexOfferAtJoshs = True

        scene black
        with hpunch
        am "*Whispers* Hey, wake up..."

        scene black
        with hpunch
        am "*Whispers* [name], sleepyhead, wake up..."

        scene v8josh35 # FPP. (For context, MC is sleeping on the floor like in v8josh34 and Amber is waking him up) Show Amber crouched near the MC, looking at him and nudging him to wake up. Amber looking horny, giving a sexy smile and mouth closed
        with Dissolve(0.25)
        pause 0.1

        scene black
        with Dissolve(0.25)
        pause 0.25

        scene v8josh35
        with Dissolve(0.75)
        u "*Whispers* Amber? What's wrong?"

        scene v8josh35a # Same as v8josh35 but Amber mouth open
        with dissolve
        am "*Whispers* Nothing's wrong. Wanna sneak into another room?"

        scene v8josh35
        with dissolve
        u "*Whispers* For what?"

        scene v8josh35a
        with dissolve
        am "*Whispers* What do you think, genius?"

        scene v8josh35
        with dissolve

        menu:
            "Go with her":
                $ sceneList.add("v8_amber2")
                $ amber.relationship = Relationship.FWB
                if lauren.relationship >= Relationship.GIRLFRIEND:
                    $ reputation.add_point(RepComponent.TROUBLEMAKER)
                else:
                    $ reputation.add_point(RepComponent.BOYFRIEND)

                u "*Whispers* Fuck yes! Let's go!"

                jump amber_sex_at_joshs

            "Reject her advances":
                $ amber.relationship = Relationship.FRIEND
                if lauren.relationship >= Relationship.GIRLFRIEND:
                    $ reputation.add_point(RepComponent.BOYFRIEND)

                u "*Whispers* Sorry Amber, I'm not feeling it tonight."

                scene v8josh35b # Amber disappointed, mouth open
                with dissolve
                am "*Whispers* Oh, okay. Sorry I woke you up at midnight."

                scene v8josh35c # Same as v8josh35b but Amber mouth closed
                with dissolve
                u "*Whispers* Goodnight."

                scene v8josh35b
                with dissolve
                am "*Whispers* Y-yeah, goodnight."

                jump tues_morning_at_joshs

    else:
        jump tues_morning_at_joshs

label tues_morning_at_joshs:
    if "v8_amber2" in sceneList:
        scene v8josh36 # TPP. (For context, it's morning now and everyone except MC woke up) Showing MC waking up on the bed (in Josh's bedroom, upstairs) in underwear
        with Fade(0.75, 0.25, 0.75)
        pause 0.5

        scene v8josh36a # MC woke up and is looking at the other side of the bed for Amber (but she's not there). Neutral expression, mouth closed
        with dissolve
        u "(Oh, looks like Amber is up already.)"
        u "(I should get dressed and see how Josh is doing.)"

        play music "music/mfunk.mp3"

        scene v8josh39 # FPP. MC walking down the stairs into the kitchen, no others should be seen in the shot (For context, Josh is making breakfast and Amber is sitting at the table talking to Josh but they should not be visible in this shot)
        with dissolve
        jo "No, I'm telling you I got this."

        scene v8josh40 # FPP (MC is inside the kitchen now). Josh (still wounded, here and in all further renders, looking a bit more energetic than last night but still struggling) is making breakfast and Amber (sitting on the stool) is looking at him, neutral expression, mouth open
        with dissolve
        am "If you say so."

        scene v8josh41 # TPP (same as how an FPP camera from MC's position would be but zoomed in to focus only on Amber). Amber cheerful, looking into the camera, mouth open
        with dissolve
        am "Hey! Good morning, [name]."

        scene v8josh42 # TPP (same as how an FPP camera from MC's position would be but zoomed in to focus only on Josh). Josh turned towards the MC with a pan in hand, looking a bit less weak compared to last night, smiling, looking into the camera and mouth open
        with dissolve
        jo "Hey! Morning bro! Sleep good?"

        scene v8josh42a # Same as v8josh42 but Josh mouth closed
        with dissolve
        u "Hey guys, and yeah..."

        scene v8josh41a # Amber flirty, looking into the camera, mouth closed
        with dissolve
        u "...I slept great."

        scene v8josh42a
        with dissolve
        u "Need any help with that? You should be resting bro."

        scene v8josh41b # Amber looking towards Josh (not visible in frame), rolling her eyes, chuckling a little and mouth open
        with dissolve
        am "Good luck with that. Mr. Responsible here says he feels \"obligated\"."

        scene v8josh42
        with dissolve
        jo "Yeah, man, it's the least I could do. Grab a seat and I'll get you guys sorted."

        scene v8josh41c # Amber looking into the camera, shrugging and mouth closed
        with dissolve
        pause

        scene v8josh42a
        with dissolve
        u "Sit down. We got this."

        scene v8josh42b # Amber walked in and is taking the pan from him (as if suddenly and Josh wasn't expecting it, but he's not resisting), smiling, mouth open. Josh looking confused, mouth open.
        with dissolve
        jo "But..."
        am "No buts. Sit down and relax before you hurt yourself more."

        scene v8josh43 # TPP (Again, similar to an FPP camera from MC's new position near the stove but zoomed in). Josh sitting on the stool now, looking towards MC and Amber (who are now in Josh's previous position), happy and mouth open.
        with dissolve
        jo "*Sigh* Thanks guys."

        scene v8josh44 # TPP (like Josh's POV). Amber and MC turned towards the stove and making breakfast, standing slightly apart. Pan in Amber's hands (their faces are not visible)
        with dissolve
        am "You make the eggs, I'll get the bacon?"
        u "Yeah, that sounds perfect. I suck at making bacon."

        scene v8josh43
        with dissolve
        jo "Thanks for all this guys. I mean it."

        scene v8josh43a # Same as v8josh43 but Josh mouth closed
        with dissolve
        u "No worries, man. Glad you're feeling a bit better."

        scene v8josh44
        with dissolve
        am "No more deals for you, dummy."
        jo "Awww, c'mon, it was one t-"

        scene v8josh44a # Same as v8josh44 but Amber turns around with a hand on her waist, looking towards Josh (so, into the camera) and warning Josh (not seriously though, more like how you would warn a child), mouth open
        with dissolve
        am "Uh uh. Shut up. Just sit there and wait for your food."

        scene v8josh44
        with dissolve
        pause 1

        scene v8josh44b # Amber comes closer and playfully nudging the MC with her hips (their faces are probably not visible, but they're laughing)
        with dissolve
        am "*Giggles*"

        scene v8josh44c # MC is now nudging her similarly
        with dissolve
        u "*Giggles*"

        scene v8josh43
        with dissolve
        jo "Get a room!"

        scene v8josh44b
        with dissolve
        am "We did! *laughs*"
        stop music fadeout 3
        u "*Laughs*"

        jump v8_tues_eco_class

    else:
        scene v8josh37 # TPP. (For context, it's morning now and everyone except MC woke up) Showing MC waking up on the floor in living room (where he slept in v8josh34). Include both the couches in the frame each with a pillow on it
        with Fade(0.75, 0.25, 0.75)
        pause 0.5

        scene v8josh37a # MC looking towards the couches, neutral expression, mouth closed
        with dissolve
        u "(Oh, looks like Josh and Amber are up already.)"
        u "(Guess I better get up and see how he is.)"

        play music "music/mfunk.mp3"

        scene v8josh38 # FPP. MC walking into the kitchen but just outside it, so no others should be seen in the shot (For context, Josh is making breakfast and Amber is sitting at the table talking to Josh but they should not be visible in this shot)
        with dissolve
        jo "No, I'm telling you I got this."

        scene v8josh40
        with dissolve
        am "If you say so."

        scene v8josh41d # Amber neutral expression, looking into the camera, mouth open
        with dissolve
        am "Hey. Good morning [name]."

        scene v8josh42
        with dissolve
        jo "Hey! Morning bro! Sleep good?"

        if amberSexOfferAtJoshs:
            scene v8josh42a
            with dissolve
            u "Hey guys, and yeah, I slept okay..."

            scene v8josh41e # Amber slightly disappointed, not looking into the camera, mouth closed
            with dissolve
            u "...I guess."

            scene v8josh42a
            with dissolve
            u "Need any help with that? You should be resting."

        else:
            scene v8josh42a
            with dissolve
            u "Hey guys, and yeah, I slept okay, I guess."
            u "Need any help with that? You should be resting."

        scene v8josh41b
        with dissolve
        am "Good luck with that. Mr. Responsible here says he feels \"obligated\"."

        scene v8josh42
        with dissolve
        jo "Yeah, man, it's the least I could do. Grab a seat and I'll get you guys sorted."

        scene v8josh41c
        with dissolve
        pause

        scene v8josh42a
        with dissolve
        u "Sit down. We got this."

        scene v8josh42b
        with dissolve
        jo "But..."
        am "No buts. Sit down and relax before you hurt yourself more."

        scene v8josh43
        with dissolve
        jo "*Sigh* Thanks guys."

        scene v8josh44
        with dissolve
        am "You make the eggs, I'll get the bacon?"
        u "Yeah, that sounds perfect. I suck at making bacon."

        scene v8josh43
        with dissolve
        jo "Thanks for all this guys. I mean it."

        scene v8josh43a
        with dissolve
        u "No worries, man. Glad you're feeling a bit better."

        scene v8josh44
        with dissolve
        am "No more deals for you, dummy."
        jo "Awww, c'mon, it was one t-"

        scene v8josh44a
        with dissolve
        am "Uh uh. Shut up. Just sit there and wait for your food."

        stop music fadeout 3

        scene v8josh44
        with dissolve
        pause 1

        scene black
        with fade
        
        pause 1

        jump v8_tues_eco_class