# SCENE 35: Riley kinky sex scene
# Location: Hotel room, Hotel Corridor Outside Room
# Characters: MC (Outfit 9), Riley (Outfit 1)
# Time: Night (Day when specified)

label v11_riley_sex:
    play music "music/v10/Track Scene 40_2.mp3" fadein 2
    if riley.relationship.value < Relationship.FWB.value:

        scene v11ris1 # TPP. Show MC walking through the door to his hotel room, MC slight smile, mouth closed (Riley not in shot here)
        with dissolve

        pause 0.75

        scene v11ris2 # FPP. MC standing in the room, looking at Riley, Riley reading her book, she has a slight smile, mouth closed, lying on the bed
        with dissolve

        pause 0.75

        scene v11ris3 # FPP. MC is now sitting on his bed, looking at Riley, Riley looking at MC, she is still lying down, her mouth is closed, slight smile, still holding her book
        with dissolve

        u "You traveled halfway across the world to read a book? Wow..."

        scene v11ris3a # FPP. Same as v11ris3, Riley book down on bed now, Riley slight smile, mouth open
        with dissolve

        ri "Some of us actually enjoy a good book every once in a while to help us relax and stimulate our minds, but I guess it makes sense that you wouldn't understand..."
        
        ri "What did Mr. Lee call you again? Oh yeah, most trusted. *Chuckles*"

        scene v11ris3b # FPP. Same as v11ris3a, Riley slight smile, mouth closed
        with dissolve

        u "*Chuckles* Hey, just because I'm much more charming than you with these sparkling hazel eyes, doesn't mean you should take your frustration out on me."

        scene v11ris3a
        with dissolve

        ri "*Chuckles* What are you up to?"

        scene v11ris3b
        with dissolve

        u "Think I'm ready to sleep."

        scene v11ris3c # FPP. Same as v11ris3a, different pose
        with dissolve

        ri "Aww, no late night talks with your awesome roommate?"

        scene v11ris3d # FPP. Same as v11ris3b, different pose
        with dissolve

        u "I guess a short late night conversation won't hurt. *Chuckles*"

        scene v11ris3c
        with dissolve

        ri "Good, because I have a question for you. Well actually, Amber mentioned something and it kinda made me wonder..."

        scene v11ris3d
        with dissolve

        u "Oh boy... What did Amber say?"

        scene v11ris3a
        with dissolve

        ri "Were you as popular with girls in high school as you are now?"

        scene v11ris3b
        with dissolve

        u "What makes you think I'm popular with girls now?"

        scene v11ris3a
        with dissolve

        ri "...Really?"

        scene v11ris3b
        with dissolve

        u "Haha."

        scene v11ris3d
        with dissolve

        menu:
            "Ladies love me":
                $ add_point(KCT.BRO)

                scene v11ris3e # FPP. Same as v11ris3d, different pose
                with dissolve

                u "Truthfully, ladies loved me in school. I couldn't tell you why, but I've never really had a problem with girls."

                scene v11ris3f # FPP. Same as v11ris3c, different pose
                with dissolve

                ri "Never?"

                scene v11ris3e
                with dissolve

                u "Nope. I've watched plenty of my friends get turned down over the years, but never experienced it much personally."

                scene v11ris3f
                with dissolve

                ri "Oh, the joys of having a pretty face... Saves you from so many harsh realities."

                scene v11ris3b
                with dissolve

                u "We can't control the cards we're dealt, I just got a lucky hand."

                scene v11ris3a
                with dissolve

                ri "Haha, that you did."

                scene v11ris3g # FPP. Same as v11ris3, Riley now looking at book, slight smile, mouth closed, diff pose
                with dissolve

                u "In a way, you just called me irresistible."

                scene v11ris3h # FPP. Same as v11ris3g, Riley slight smile, mouth open
                with dissolve

                ri "*Chuckles* Just take the compliment."

                scene v11ris3g
                with dissolve

                u "Haha. Well in that case, thanks."

                scene v11ris3i # FPP. Same as v11ris3, Riley mouth open, slight smile, holding book, looking at MC 
                with dissolve

                ri "You're welcome. Now, since I finished a few chapters and had a good late-night chat, I'm so ready for bed. Night [name]."

                scene v11ris3
                with dissolve

                u "*Chuckles* Night Riley."

            "Wasn't a ladies man":
                $ add_point(KCT.BOYFRIEND)

                scene v11ris3e
                with dissolve

                u "Well, I wasn't really a ladies man back then."

                scene v11ris3f
                with dissolve

                ri "So you struggled with girls?"

                scene v11ris3b
                with dissolve

                u "I wouldn't say I struggled. I think dating just wasn't at the top of my list in high school."

                scene v11ris3g
                with dissolve

                ri "Hmm, that's weird."

                scene v11ris3h
                with dissolve

                u "What's weird?"

                scene v11ris3g
                with dissolve

                ri "Well, you're not a bad looking guy."

                scene v11ris3h
                with dissolve

                u "Are you saying I'm handsome?"

                scene v11ris3i
                with dissolve

                ri "*Chuckles* Just take the compliment."

                scene v11ris3h
                with dissolve

                u "Haha. Well in that case, thanks."

                scene v11ris3i
                with dissolve

                ri "You're welcome. Now, since I finished a few chapters and had a good late-night chat, I'm so ready for bed. Night [name]."

                scene v11ris3
                with dissolve

                u "*Chuckles* Night, Riley."

        scene v11ris4 # TPP. Show MC taking his shirt off, he has a slight smile, mouth closed, standing next to his bed
        with dissolve

        pause 0.75

        scene v11ris5 # TPP. Show MC lying down in his bed, under the covers, shirtless, eyes closed, mouth closed, sleeping
        with dissolve

        pause 0.75

        scene v11ris5a # TPP. Same as v11ris5, different sleeping position
        with dissolve

        pause 0.75

        scene black
        with vpunch

        ri "Wake up, [name]!"

        scene v11ris6 # FPP. MC lying on his bed, Riley standing next to him, looking down on him, her mouth closed, very slightly annoyed (day)
        with dissolve

        u "Is this wake up call gonna happen every morning?"

        scene v11ris6a # FPP. Same as v11ris6, Riley mouth open, very slightly annoyed (day)
        with dissolve

        ri "If you don't start getting up at a normal time like everyone else, then yeah."

        scene v11ris6
        with dissolve

        u "*Sighs*"

        scene v11ris7 # TPP. Show MC sitting up on his bed now, in his boxers, he is yawning and stretching (day)
        with dissolve

        pause 0.75

        scene v11ris7a # TPP. Same cam as v11ris7, MC is startled, mouth closed, still sitting down, looking at the door to the hallway direction (day)
        with vpunch

        play sound "sounds/fall.mp3"

        pause 0.75

        imre "GET THE FUCK OFF ME!"

        scene v11ris8 # TPP. Show MC getting up from his bed, he is startled, mouth closed (day)
        with dissolve

        pause 0.75

        scene v11ris9 # TPP. Show MC putting his shirt on (he already has pants on) (day)
        with dissolve

        pause 0.75

        scene v11ris10 # TPP. Show MC opening the door to the hallway, he is startled, mouth closed (day)
        with dissolve

        pause 0.75

        scene v11ris11 # TPP. Show MC looking down the hallway, very startled, mouth closed (day)
        with dissolve

        pause 0.75

        jump v11_imre_ryan_grapple

    else:
        label v11_riley_sex_sg:
        scene v11ris1
        with dissolve

        pause 0.75

        scene v11ris12 # FPP. MC standing in the room, Riley lying under the covers of MC's bed, only her shoulders showing (she's naked underneath), she is smiling at MC, mouth open
        with dissolve

        ri "So, you decided to get back early after all."

        scene v11ris12a # FPP. Same as v11ris12, Riley mouth closed, smiling
        with dissolve

        u "Well, it's been a pretty filled up day. Not stressful, just did a bunch of cool things... Laying in my bed, huh?"

        scene v11ris12
        with dissolve

        ri "*Chuckles* I do what I want... If you have a problem, come do something about it."

        scene v11ris12a
        with dissolve

        menu:
            "Not tonight":
                $ riley.points -= 1

                u "Sorry Riley, I'm not really in the mood for anything like that right now."

                scene v11ris12
                with dissolve

                ri "Aww, okay. I'll just crawl back over into my bed."

                scene v11ris12b # FPP. Same as v11ris12, show Riley getting out of the covers, sitting on the bed, mouth closed, slightly sad
                with dissolve

                pause 1

                scene v11ris12c # FPP. Same cam as v11ris12, Show Riley walking to her bed, she is slightly sad, mouth closed 
                with dissolve

                pause 1

                scene v11ris13 # FPP. Show Riley getting into her bed, she's slightly sad, mouth closed
                with dissolve

                pause 1

                scene v11ris13a # FPP. Same as v11ris13, Show Riley under the covers of her bed, with her chest covered up by it now, she has mouth closed slightly sad, looking at MC
                with dissolve

                pause 0.75

                scene v11ris4a # FPP. Same as v11ris4, MC tired, mouth closed
                with dissolve

                $ renpy.end_replay()

                pause 0.75

                scene v11ris14 # FPP. MC lying in his bed, looking at Riley, she's lying in her bed, slightly worried, mouth open (she's naked, but don't show anything here)
                with dissolve

                ri "You sure everything's okay? I thought you'd be excited for some fun."

                scene v11ris14a # FPP. Same as v11ris14, Riley mouth closed, slightly worried
                with dissolve

                u "Yeah, everything's cool. I'm just tired and have a lot on my mind."

                scene v11ris14
                with dissolve

                ri "[name]... No one on this trip is blind to the issues that you and Charli are having."

                scene v11ris14a
                with dissolve

                pause 0.5

                scene v11ris14
                with dissolve
                
                ri "We all overheard your conversation at the airport and Charli definitely has no problem sharing how he feels about you, but you should know something."
                
                ri "We're your friends and although we all like to have fun every once in a while, we aren't naive or gullible or helpless."

                scene v11ris14a
                with dissolve

                pause 0.5

                scene v11ris14
                with dissolve
                
                ri "We know what we're doing and we make our own choices. Stop being so hard on yourself."

                scene v11ris14b # FPP. Same as v11ris14, Riley different pose (in this pose, show some boob peeking out of the covers), slightly smiling, mouth closed
                with dissolve

                u "*Sighs* Thanks Riley. I really needed to hear that... Maybe tonight I'll be able to sleep without any negative thoughts clouding my mind."

                scene v11ris14c # FPP. Same as v11ris14b, Riley mouth open, slightly smiling
                with dissolve

                ri "I'm glad I could help a little. But you should know, that was your only free session. Any other sit downs with therapist Riley and I'll have to charge you. *Chuckles*"

                scene v11ris14b
                with dissolve

                u "*Chuckles* Noted... Goodnight, Riley."

                scene v11ris14c
                with dissolve

                ri "Night, [name]."

                scene v11ris5 
                with dissolve

                pause 0.75

                scene v11ris5a 
                with dissolve

                pause 0.75

                scene black
                with vpunch

                ri "[name], wake up! I think someone's fighting in the hall!"

                scene v11ris6b # FPP. Same as v11ris6, Riley worried, mouth closed (day)
                with dissolve

                u "Huh, what?"

                scene v11ris6c # FPP. Same as v11ris6, Riley worried, mouth open (day)
                with dissolve

                ri "It sounds like Imre and Ryan, they're yelling."

                scene v11ris6b
                with dissolve

                u "Fuck!"

                scene v11ris7a 
                with vpunch

                play sound "sounds/fall.mp3"

                pause 0.75

                imre "GET THE FUCK OFF ME!"

                scene v11ris8 
                with dissolve

                pause 0.75

                scene v11ris9 
                with dissolve

                pause 0.75

                scene v11ris10 
                with dissolve

                pause 0.75

                scene v11ris11 
                with dissolve

                pause 0.75

                jump v11_imre_ryan_grapple

            "Do something about it":
                $ sceneList.add("v11_riley")
                $ riley.points += 1

                u "Keep talking like that and I will."

                scene v11ris12
                with dissolve

                ri "Then I guess I'll say it again..."

                if config_censored:
                    call screen censoredPopup("v11s35_nsfwSkipLabel1")

                scene v11ris12d # FPP. Same as v11ris12, Riley no longer under the blanket, smiling seductively, mouth open
                with dissolve

                ri "Do something about it."
                stop music fadeout 3

                play music "music/v10/Track Scene 26_2.mp3" fadein 2
                scene v11ris15 # TPP. MC walking over to Riley, he is removing his shirt (Camera behind MC), show Riley big smile, mouth closed, she's getting close to the edge of the bed (not the sides, the side oposite the pillows)
                with dissolve

                pause 1

                scene v11ris16 # TPP. Show Riley laying down with her head hanging off the edge of the bed, belly up, her mouth is closed, big smile, MC is removing his boxers, he has a big smile, mouth closed
                with dissolve

                pause 1

                image v11ritf = Movie(play="images/v11/Scene 35/v11ritf.webm", loop=True, image="images/v11/Scene 35/v11ritfStart.webp", start_image="images/v11/Scene 35/v11ritfStart.webp") # Riley throat fuck
                image v11ritff = Movie(play="images/v11/Scene 35/v11ritff.webm", loop=True, image="images/v11/Scene 35/v11ritfStart.webp", start_image="images/v11/Scene 35/v11ritfStart.webp") # Riley throat fuck spedup
                image v11ritf2 = Movie(play="images/v11/Scene 35/v11ritfTPP.webm", loop=True, image="images/v11/Scene 35/v11ritfTPPStart.webp", start_image="images/v11/Scene 35/v11ritfTPPStart.webp") # Riley throat fuck
                image v11ritf2f = Movie(play="images/v11/Scene 35/v11ritfTPPf.webm", loop=True, image="images/v11/Scene 35/v11ritfTPPStart.webp", start_image="images/v11/Scene 35/v11ritfTPPStart.webp") # Riley throat fuck spedup

                scene v11ritf # Ignore as animation
                with dissolve
                pause

                u "How about this?"

                scene v11ritff
                with dissolve
                pause

                ri "*Gagging*"

                scene v11ritf2 # Ignore as animation
                with dissolve
                pause

                u "Bet you don't give me attitude again, huh?"

                scene v11ritf2f
                with dissolve
                pause

                ri "*Gagging*"

                scene v11ris17 # TPP. Show Riley moving to stand up in front of MC, he's standing, both smiling, mouths closed
                with dissolve

                pause 1

                scene v11ris18 # TPP. Show Riley standing in front of MC, MC's hands on her waist, her hands on his neck, both smiling, mouths closed
                with dissolve

                pause 1

                scene v11ris18a # TPP. Same cam as v11ris18, Show MC holding Riley up, she has her legs wrapped around his back, both smiling, mouths closed, MC holding her waist, Riley's arms wrapped around his neck
                with dissolve

                pause 1

                scene v11ris19 # TPP. Show MC walking towards the door, same pose as v11ris16a (Riley being held up by him with her legs wrapped around his back)
                with dissolve

                pause 1

                scene v11ris20 # TPP. MC has Riley with her back on the wall, he's holding her like in v11ris16a, Riley's arms to her side now, both looking at each other, smiling, mouths closed
                with dissolve

                pause 1

                image v11riwf = Movie(play="images/v11/Scene 35/v11riwf.webm", loop=True, image="images/v11/Scene 35/v11riwfStart.webp", start_image="images/v11/Scene 35/v11riwfStart.webp") # Riley fuck against wall
                image v11riwff = Movie(play="images/v11/Scene 35/v11riwff.webm", loop=True, image="images/v11/Scene 35/v11riwfStart.webp", start_image="images/v11/Scene 35/v11riwfStart.webp") # Riley fuck against wall spedup
                image v11riwf2 = Movie(play="images/v11/Scene 35/v11riwf2.webm", loop=True, image="images/v11/Scene 35/v11riwf2Start.webp", start_image="images/v11/Scene 35/v11riwf2Start.webp") # Riley fuck against wall
                image v11riwf2f = Movie(play="images/v11/Scene 35/v11riwf2f.webm", loop=True, image="images/v11/Scene 35/v11riwf2Start.webp", start_image="images/v11/Scene 35/v11riwf2Start.webp") # Riley fuck against wall spedup

                scene v11riwf # Ignore as animation
                with dissolve
                pause

                ri "OH MY GOD!"

                scene v11riwff # Inore as animaiton
                with dissolve
                pause

                ri "YESSSS!"

                scene v11riwf2
                with dissolve
                pause

                u "*Moans*"

                scene v11riwf2f
                with dissolve
                pause

                ri "*Moans loudly*"

                scene v11ris21 # TPP. Show MC putting Riley down, grabbing her neck both smiling, mouths closed
                with dissolve

                pause 1

                scene v11ris22 # TPP. Show MC bending Riley over the desk, Riley smiling, mouth closed, MC serious, mouth closed
                with dissolve

                pause 1

                image v11riod = Movie(play="images/v11/Scene 35/v11riod.webm", loop=True, image="images/v11/Scene 35/v11riodStart.webp", start_image="images/v11/Scene 35/v11riodStart.webp") # Riley fucked over desk
                image v11riodf = Movie(play="images/v11/Scene 35/v11riodf.webm", loop=True, image="images/v11/Scene 35/v11riodStart.webp", start_image="images/v11/Scene 35/v11riodStart.webp") # Riley fucked over desk spedup
                image v11riod2 = Movie(play="images/v11/Scene 35/v11riod2.webm", loop=True, image="images/v11/Scene 35/v11riod2Start.webp", start_image="images/v11/Scene 35/v11riod2Start.webp") # Riley fucked over desk
                image v11riod2f = Movie(play="images/v11/Scene 35/v11riod2f.webm", loop=True, image="images/v11/Scene 35/v11riod2Start.webp", start_image="images/v11/Scene 35/v11riod2Start.webp") # Riley fucked over desk spedup

                scene v11riod # Ignore as animation
                with dissolve
                pause

                u "You better start behaving, Riley..."

                scene v11riodf
                with dissolve
                pause

                ri "FUCK! I love this side of you..."

                scene v11riod2 # Ignore as animation
                with dissolve
                pause

                ri "*Moans* Harder!"

                scene v11riod2f
                with dissolve
                pause

                ri "I'm shaking!"

                scene v11ris22a # TPP. Same as v11ris22, MC's dick pulling out of her pussy
                with dissolve

                pause 1

                scene v11ris22b # TPP. Same as v11ris22, Show MC putting his dick in Riley's ass, MC slight smile, mouth closed, Riley mouth closed, she's startled, surprised
                with dissolve

                ri "*Gasps* OH FUCK!"

                image v11rioda = Movie(play="images/v11/Scene 35/v11rioda.webm", loop=True, image="images/v11/Scene 35/v11riodaStart.webp", start_image="images/v11/Scene 35/v11riodaStart.webp") # Riley fucked over desk anal
                image v11riodaf = Movie(play="images/v11/Scene 35/v11riodaf.webm", loop=True, image="images/v11/Scene 35/v11riodaStart.webp", start_image="images/v11/Scene 35/v11riodaStart.webp") # Riley fucked over desk anal sped up
                image v11rioda2 = Movie(play="images/v11/Scene 35/v11rioda2.webm", loop=True, image="images/v11/Scene 35/v11rioda2Start.webp", start_image="images/v11/Scene 35/v11rioda2Start.webp") # Riley fucked over desk anal
                image v11rioda2f = Movie(play="images/v11/Scene 35/v11rioda2f.webm", loop=True, image="images/v11/Scene 35/v11rioda2Start.webp", start_image="images/v11/Scene 35/v11rioda2Start.webp") # Riley fucked over desk anal sped up

                scene v11rioda # Ignore as animation
                with dissolve
                pause

                u "*Grunt*"

                scene v11riodaf # Ignore as animation
                with dissolve
                pause

                u "Fuck!"

                scene v11rioda2
                with dissolve
                pause
                
                ri "Yes! Yes! Don't stop!"

                scene v11rioda2f
                with dissolve
                pause

                u "Ah yes! Ah fuck!"

                scene v11ris23 # FPP. Same positioning as v11ris22, MC looking at Riley's back, filled with cum, she has her head turned towards him, smiling, mouth closed
                with flash

                u "Shit, that was nice."

                scene v11ris24 # FPP. Show Riley turning around to look at MC, she has a smile, mouth closed, same positioning as v11ris21
                with dissolve

                pause 1

                scene v11ris24a # FPP. Same as v11ris24, Riley now fully turned towards him, hands on his shoulders, mouth opened, big smile
                with dissolve

                ri "Wow... I like the kinky side of you. *Chuckles* I'm gonna go clean up... I'll be right back."

                scene v11ris25 # TPP. Show Riley walking towards the bathroom, MC putting his boxers on, both smiling, mouths closed
                with dissolve

                pause 1

                scene v11ris26 # TPP. Show MC getting in bed, he's smiling, mouth closed
                with dissolve
                stop music fadeout 3
                play music "music/v10/Track Scene 40_2.mp3" fadein 2
                pause 0.75

                scene v11ris26a # TPP. Same as v11ris26, MC is lying in his bed, looking at Riley, Riley is getting into bed, both smiling, mouths closed
                with dissolve

                pause 0.75

                scene v11ris26b # TPP. Same as v11ris26a, Show MC and Riley laying in bed looking at each other, both smiling, mouths closed
                with dissolve

                pause 0.75

                scene v11ris27 # FPP. MC and Riley laying next to each other, looking at each other, Riley smiling, mouth open
                with dissolve

                ri "I'm glad we're able to be close like this."

                scene v11ris27a # FPP. Same as v11ris27, Riley mouth closed, smiling
                with dissolve

                u "I am too."

                scene v11ris27b # FPP. Same as v11ris27, Riley slightly worried, mouth open
                with dissolve

                ri "[name]... No one on this trip is blind to the issues that you and Charli are having."
                
                ri "We all overheard your conversation at the airport and Charli definitely has no problem sharing how he feels about you, but you should know something."

                scene v11ris27c # FPP. Same as v11ris27a, Riley mouth closed, slightly worried
                with dissolve

                pause 0.5

                scene v11ris27b 
                with dissolve
                
                ri "We're your friends and although we all like to have fun every once in a while, we aren't naive or gullible or helpless."
                
                ri "We know what we're doing and we make our own choices. Stop being so hard on yourself."

                scene v11ris27c
                with dissolve

                u "*Sighs* Thanks Riley. I really needed to hear that... Maybe tonight I'll be able to sleep without any negative thoughts clouding my mind."

                scene v11ris27
                with dissolve

                ri "I'm glad I could help a little. But you should know, that was your only free session. Any other sit downs with therapist Riley and I'll have to charge you. *Chuckles*"

                scene v11ris27a
                with dissolve

                u "*Chuckles* Noted."

                scene v11ris27
                with dissolve

                ri "Well, after all that excitement you just put me through, I'm exhausted."

                scene v11ris28 # TPP. Show Riley walking towards the wall (she's going to turn off the lights, but just make her walk towards the wall, no need for light switch), Riley smiling, mouth closed
                with dissolve

                pause 0.75

                scene v11ris29 # TPP. Show Riley getting in bed, room is now dark, Riley mouth closed, smiling
                with dissolve

                pause 0.75

                label v11s35_nsfwSkipLabel1:

                scene v11ris27d # FPP. Same as v11ris27, Riley cuddled up to MC, looking at him, Riley mouth open, smiling, room dark
                with dissolve

                ri "Goodnight, [name]."

                scene v11ris27e # FPP. Same as v11ris27d, Riley mouth closed, smiling
                with dissolve

                u "Goodnight."

                scene v11ris30 # TPP. Show MC and Riley sleeping together
                with dissolve

                pause 1.25

                scene v11ris31 # MC and Riley sleeping together, different pose to v11ris28
                with dissolve

                pause 1.25

                scene black
                with fade
                
                pause 2
                
                scene black
                with vpunch

                $ renpy.end_replay()
                play music "music/v10/Track Scene 41a_2.mp3" fadein 2
                ri "[name], wake up! I think someone's fighting in the hall!"

                scene v11ris6b
                with dissolve

                u "Huh, what?"

                scene v11ris6c
                with dissolve

                ri "It sounds like Imre and Ryan, they're yelling."

                scene v11ris6b
                with dissolve

                u "Fuck!"

                scene v11ris7a 
                with vpunch

                play sound "sounds/fall.mp3"

                pause 0.75

                imre "GET THE FUCK OFF ME!"

                scene v11ris8 
                with dissolve

                pause 0.75

                scene v11ris9 
                with dissolve

                pause 0.75

                scene v11ris10 
                with dissolve

                pause 0.75

                scene v11ris11 
                with dissolve

                pause 0.75

                jump v11_imre_ryan_grapple