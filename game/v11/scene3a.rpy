# SCENE 03A: Wolves Packing, Convo w/ Chris
# Locations: MC's Wolf Bedroom
# Characters: MC (New outfit from scene 1), Chris (Outfit 1)
# Time: Thursday afternoon
label v11_wolves_packing_chris:

    scene v10swpc1 # FPP. MC is in his Wolves room, looking at his clothes. 
    with fade
    play music "music/v11/Track Scene 3.mp3" fadein 2
    u "(I really should get some more clothes.)"

    scene v10swpc2 # FPP. MC looks at the door in his Wolves room. It's closed.
    with fade

    play sound sound.knock

    scene v10swpc2a # FPP. Same camera as v10swpc2. MC's door opens and Chris starts walking in. Show Chris, smiling, mouth open.
    with dissolve

    ch "Hey man, saw you come home. You usually aren't here around this time and everyone else is out. What are you up to?"

    play sound "sounds/dooropen.mp3"

    scene v10swpc2b # FPP. Same camera as v10swpc2. Show a closer shot of Chris after walking in to talk w/ MC. Smiling, mouth closed.
    with dissolve

    u "I'm just getting things situated for the trip. You already packed up?"

    scene v10swpc2c # FPP. Same camera as v10swpc2. Show a closer shot of Chris after walking in to talk w/ MC. Smiling, mouth open.
    with dissolve

    ch "Yeah, I packed last week except for bathroom stuff."

    scene v10swpc2b
    with dissolve

    u "Ahh that was smart, I don't know what I was doing. I thought we still had another week."

    scene v10swpc2c
    with dissolve

    ch "*Sigh* You wouldn't be the only one lately that doesn't know what they're doing."

    scene v10swpc2b
    with dissolve

    u "What do you mean?"

    scene v10swpc3 # TPP. Same camera as v10swpc3. Show Chris and MC sitting on MC's bed. Chris looks thoughtful, MC has a normal expression. Chris is sighing, MC mouth closed.
    with fade

    ch "*Sighs*"

    scene v10swpc4 # FPP. Same camera as v10swpc4. Show Chris sitting on MC's bed, thoughtful expression, mouth closed.
    with dissolve

    u "What's wrong?"

    scene v10swpc4a # FPP. Same camera as v10swpc4. Show Chris sitting on MC's bed, thoughtful expression, mouth open.
    with dissolve

    ch "It's Nora... Her and I are having some... issues."

    scene v10swpc4
    with dissolve

    u "Oh..."

    scene v10swpc4a
    with dissolve

    ch "You don't mind me opening up to you do you? I just really haven't had a chance to vent."

    scene v10swpc4
    with dissolve
    menu:
        "Let him":
            $ reputation.add_point(RepComponent.BRO)
            scene v10swpc4
            with dissolve

            u "Of course, I don't mind."

            scene v10swpc4a
            with dissolve

            ch "Let me ask you this, do you think Nora and I are right for each other?"

            scene v10swpc4
            with dissolve
            menu:
                "Of course":
                    $ reputation.add_point(RepComponent.BRO)
                    scene v10swpc4
                    with dissolve

                    u "Of course, I couldn't see you guys without each other."

                "I don't know":
                    scene v10swpc4
                    with dissolve

                    u "I wouldn't wanna try and play matchmaker or anything. So I don't really know."

            scene v10swpc4a
            with dissolve

            ch "Right now, I have no idea."
            
            ch "The last time I saw her smile was at homecoming and that was only for a moment. And even that night didn't end well."

            scene v10swpc4
            with dissolve

            u "What's causing you guys to have problems?"

            scene v10swpc4a
            with dissolve

            ch "It's a whole mess really. I love Nora, more than anything. She's been there for me in ways I can't even explain."
            
            ch "I've known her forever. I mean, we've been dating since high school. But ever since I became Wolves President it's like I'm being torn two ways."
            
            ch "It seems impossible for me to do everything I need to do for the frat and still give Nora the attention she deserves."
            
            ch "I've tried explaining to her that this is just temporary, but that didn't really make things better."

            scene v10swpc4
            with dissolve

            u "I get it, sometimes it's hard to know what the right thing to do is... But can you blame her for being upset that you're prioritizing the frat?"

            scene v10swpc4a
            with dissolve

            ch "That's just it, I can't. I completely understand her point of view and I wish things were different, but they can't be while I'm President."

            scene v10swpc4
            with dissolve
            menu:
                "Talk to her":
                    scene v10swpc4
                    with dissolve

                    u "Sounds like the best thing to do is just sit down and talk with her."

                    scene v10swpc4a
                    with dissolve

                    ch "Believe me, I've tried. We just see things differently. There's no getting her to understand, all I can do is hope she hangs in there while my time in the frat lasts."

                    scene v10swpc4
                    with dissolve

                    u "She may not be willing to make that sacrifice. What then?"

                    scene v10swpc4a
                    with dissolve

                    ch "Then I lose the love of my life. My grandfather used to say \"we can love people all we want, but if we can't provide for those we love then we don't love them at all\"."
                    
                    ch "This frat opens so many doors for me. Job opportunities, leadership programs, scholarships... All I need to do is finish what I've started."

                    scene v10swpc4
                    with dissolve

                    u "Does Nora know all of this?"

                    scene v10swpc4a
                    with dissolve

                    ch "*Sighs* Yes, but she- she doesn't care. She feels I can still do better and that I'm using the frat as an excuse."

                    scene v10swpc4
                    with dissolve

                    u "Maybe on the trip you'll have the chance to get that spark back."

                    scene v10swpc4a
                    with dissolve

                    ch "I wish, but I don't think that's gonna happen either."

                    scene v10swpc4
                    with dissolve

                    u "How come?"

                    scene v10swpc4a
                    with dissolve

                    ch "I'm only going on the trip because I need it to graduate. Otherwise I'd be staying to take care of things for the frat, we have some major things coming up."
                    
                    ch "I'm gonna be spending most of the trip on the phone with Sebastian. And I don't think that's gonna solve our issues."

                    scene v10swpc4
                    with dissolve

                    u "Damn man, you sure there's no way for you to take a break?"

                    scene v10swpc4a
                    with dissolve

                    ch "If I slack off now, everything I've done up until this point would be meaningless."
                    ch "I've set an example of what it means to lead the Wolves and I won't ruin that for a vacation."

                    scene v10swpc4
                    with dissolve

                    u "Sounds like your mind's made up."

                    scene v10swpc4a
                    with dissolve

                    ch "Maybe, I mean, I'm still confused. I just need her to understand."

                    scene v10swpc4c # FPP. Same camera as v10swpc4. Show Chris sitting on MC's bed, looking down towards the ground, thoughtful/slightly upset expression, mouth open.
                    with dissolve

                    ch "Does she not understand how much I love her?"

                    scene v10swpc4d # FPP. Same camera as v10swpc4. Show Chris sitting on MC's bed, looking down towards the ground, thoughtful/slightly upset expression, mouth closed.
                    with dissolve

                    u "I've never known you to not figure something out. I'm sure this'll be no different."

                    scene v10swpc4c 
                    with dissolve

                    ch "I hope you're right."
                
                "Her or the frat":
                    $ reputation.add_point(RepComponent.TROUBLEMAKER)
                    scene v10swpc4
                    with dissolve

                    u "Sounds like you need to decide between her or the frat."

                    scene v10swpc4a
                    with dissolve

                    ch "I can't... I'm not abandoning her or the frat. Both need me. I just wish the frat needed me a little less. You know, sometimes I wish I wasn't even President."

                    scene v10swpc4
                    with dissolve

                    u "I can't picture the frat without you as President, but it would give you more time for Nora."

                    scene v10swpc4d
                    with dissolve

                    ch "..."

                    scene v10swpc4d
                    with dissolve

                    u "Chris?"

                    scene v10swpc4c
                    with dissolve

                    ch "I shouldn't even have let an idea like that slip into my head. This frat is home and has provided so much for me. Job opportunities, leadership programs, scholarships..."

                    scene v10swpc4
                    with dissolve

                    u "That's amazing, does she not know all this?"

                    scene v10swpc4a
                    with dissolve

                    ch "*Sighs* Yes, but she doesn't care. She feels I can still do better and that I'm using the frat as an excuse."

                    scene v10swpc4
                    with dissolve

                    u "Maybe on the trip you'll have the chance to get that spark back."

                    scene v10swpc4a
                    with dissolve

                    ch "I wish, but that's not gonna happen either."

                    scene v10swpc4
                    with dissolve

                    u "How come?"

                    scene v10swpc4a
                    with dissolve

                    ch "I'm only going on the trip because I need it to graduate. Otherwise I'd be staying to take care of things for the frat, we have some major things coming up."
                    
                    ch "I'm gonna be spending most of the trip on the phone with Sebastian. And I don't think that's gonna solve our issues."

                    scene v10swpc4
                    with dissolve

                    u "Damn man, you sure there's no way for you to take a break?"

                    scene v10swpc4a
                    with dissolve

                    ch "If I slack off now, everything I've done up until this point would be meaningless."
                    ch "I've set an example of what it means to lead the Wolves and I won't ruin that for a vacation."

                    scene v10swpc4
                    with dissolve

                    u "Sounds like your mind's made up."

                    scene v10swpc4a
                    with dissolve

                    ch "Maybe, I mean, I'm still confused. I just need her to understand."

                    scene v10swpc4c
                    with dissolve

                    ch "Does she not understand how much I love her?"

                    scene v10swpc4d
                    with dissolve

                    u "I've never known you to not figure something out. I'm sure this'll be no different."

                    scene v10swpc4c
                    with dissolve

                    ch "I hope you're right."

            scene v10swpc4e # FPP. Same camera as v10swpc4. Show Chris sitting on MC's bed, head in his hands, leaning over and starting to tear up.
            with dissolve

            pause 0.75

            scene v10swpc4f # FPP. Same camera as v10swpc4. Show Chris starting to stand up from the bed. He's wiping/covering his eyes, mouth closed.
            with dissolve

            pause 0.75

            scene v10swpc2e # FPP. Same camera as v10swpc2. Show a closer shot of Chris, wiping/covering his eyes, mouth open.
            with dissolve

            ch "Thanks for the talk [name]. I appreciate it."

            scene v10swpc2f # FPP. Same camera as v10swpc2. Show a closer shot of Chris, wiping/covering his eyes, mouth closed.
            with dissolve

            u "Of course man, anytime."

            scene v10swpc2d
            with dissolve

            pause 0.75

            play sound "sounds/doorclose.mp3"

            scene v10swpc2
            with dissolve

            u "(THAT. WAS. ROUGH.)"

            play sound "sounds/call.mp3"
            pause 2.25

        "Don't let him":
            scene v10swpc4
            with dissolve

            u "Honestly, I'd rather not know what goes on in your relationship. I feel like that's between you and Nora."

            scene v10swpc4a
            with dissolve

            ch "I get that."

            scene v10swpc4b # FPP. Same camera as v10swpc4. Show Chris starting to stand up from the bed. A little smile, mouth closed.
            with dissolve

            pause 0.75

            scene v10swpc2c
            with dissolve

            ch "I'm gonna go find Sebastian, gonna need him to take over while I'm gone."

            scene v10swpc2b
            with dissolve

            u "See ya."

            scene v10swpc2d # FPP. Same camera as v10swpc2. Show Chris walking out of MC's room.
            with dissolve

            pause 0.75

            play sound "sounds/doorclose.mp3"

            scene v10swpc2
            with dissolve

            play sound "sounds/call.mp3"
            pause 2.25
        
    stop music fadeout 3
jump v11_cafe_with_riley