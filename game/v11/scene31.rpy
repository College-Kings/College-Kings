# SCENE 31: MC and Lindsey in the park
# Location: Park, Sidewalk, Hotel Lobby
# Characters: MC (Outfit 9), Lindsey (Outfit 2), Emily (Outfit 1)
# Time: Day

label v11_lindsey_park:
    scene v11lip1 # TPP. Show MC walking up to Lindsey, she is sitting down on the bench, slightly sad, mouth closed, looking at the trees, MC shown from behind
    with dissolve
    play music music.ck1.v11.Track_Scene_9_2 fadein 2
    pause 0.75

    scene v11lip2 # TPP. Show MC midway through sitting down, MC and Lindsey now looking at each other, both slight smiles, mouths closed
    with dissolve

    pause 0.75

    scene v11lip3 # FPP. MC now sitting next to Lindsey, both looking at each other, Lindsey slightly sad, mouth closed
    with dissolve

    u "Hey Linds, all by yourself?"

    scene v11lip3a # FPP. Same as v11lip3, Lindsey slightly sad, mouth open
    with dissolve

    li "Yeah, I'm just enjoying the park. There really is no better place than a good park. My mother and I used to go to parks all the time..."

    scene v11lip3
    with dissolve

    u "I have to be honest, the connection that you have with your mother is pretty amazing. And I'm glad you value it too."

    scene v11lip3a
    with dissolve

    li "Of course. She played so many roles in my life it'd be hard not to."

    scene v11lip3b # FPP. Same as v11lip3, different pose, Lindsey slightly sad, mouth closed
    with dissolve

    u "I wish more people valued the relationships they build with others."

    scene v11lip3c # FPP. Same as v11lip3b, Lindsey slightly sad, mouth open
    with dissolve

    li "Are you talking about anyone specifically?"

    scene v11lip3b
    with dissolve

    u "No, I just mean in general. I think a lot of people take more for granted than they should."

    scene v11lip3c
    with dissolve

    li "Well, sometimes people just don't know [name]. I was lucky enough to have a mother that made sure I knew how much she loved me, but some people don't have that."

    scene v11lip3a
    with dissolve
    
    li "Some people have others in their life that they care for deeply, but show it so poorly that those people never really know."

    scene v11lip3d # FPP. Same as v11lip3, Lindsey slight smile, mouth closed, different pose
    with dissolve

    u "Hmm... You're pretty insightful, Lindsey."

    scene v11lip3e # FPP. Same as v11lip3d, Lindsey slight smile, mouth open
    with dissolve

    li "Woah, no Linds? I just started getting used to it. *Chuckles*"

    scene v11lip3d
    with dissolve

    u "Haha, well... It felt like a serious moment."

    scene v11lip3f # FPP. Same cam as v11lip3, Lindsey looks away from MC, still show her face, she has a serious expression, mouth open
    with dissolve

    li "Speaking of serious, I've made a pretty big decision."

    scene v11lip3g # FPP. Same as v11lip3f, Lindsey serious expression, mouth closed
    with dissolve

    u "What's that?"

    scene v11lip3e
    with dissolve

    li "I'm one hundred percent certain that I'm running against Chloe to be Chicks President."

    scene v11lip3d
    with dissolve

    u "Wow... congrats! What made you decide?"

    scene v11lip3c
    with dissolve

    li "Honestly, she did. I sat and spoke with her about some of the Nora drama and how the rest of the girls feel about it and rather than taking any responsibility she blamed everything on Nora."

    scene v11lip3a
    with dissolve
    
    li "I tried getting her to see some of the things she's done that have contributed to the problem, but she's blind to all of that. She genuinely believes she's done nothing wrong."

    scene v11lip3
    with dissolve

    menu:
        "Defend Chloe":
            $ lindsey.points -= 1
            scene v11lip3b
            with dissolve

            u "Is it possible that with all the responsibility she has, it's hard for her to see her mistakes?"

        "Don't defend Chloe":
            $ lindsey.points += 1
            scene v11lip3d
            with dissolve

            u "I couldn't begin to guess what's led her to see things like that."

    scene v11lip3a
    with dissolve

    li "Regardless, any excuse is a bad excuse. And I don't want this to affect our friendship, but I can't let our feelings get in the way of doing what's right."

    scene v11lip3
    with dissolve

    menu:
        "Support Chloe":
            $ lindsey.points -= 1
            scene v11lip3b
            with dissolve

            u "I feel like your friendship is the key to all of this. Rather than running against her, maybe you should be trying to use your friendship as leverage to talk to her."

            scene v11lip3a
            with dissolve

            li "Like I said, I already tried that and she can't see past her ego. Don't get me wrong, I love Chloe... She's one of my best friends, I know her very well."
            
            li "And so I know this is the only way... unfortunate as it is."

            scene v11lip3
            with dissolve

            u "*Sighs* I just hope this doesn't make things worse or really hurt Chloe if she loses."

            scene v11lip3c
            with dissolve

            li "I'll make sure Chloe is taken care of, she's still my friend [name]."

            scene v11lip3b
            with dissolve

            u "I'm gonna hold you to that."

            scene v11lip3e
            with dissolve

            li "Always down for being held accountable."

        "Support Lindsey":
            $ v11_lindsey_run = True
            $ lindsey.points += 1

            scene v11lip3h # FPP. Same as v11lip3d, different pose
            with dissolve

            if politics:
                grant achievement("political_strategist", "Tell Autumn you're into politics and encourage Lindsey to run")

            u "I'm down to support you as long as all of this means a new beginning for the Chicks. I'm not in the business of switching out one problem for another, get what I'm saying?"

            scene v11lip3i # FPP. Same as v11lip3e, different pose
            with dissolve

            li "I hear you, and I want to make that clear to the girls too."

            scene v11lip3e
            with dissolve
            
            li "Chloe does too much without the input of the rest of the Chicks, no one is there to hold her accountable because no one knows what's going on. Not even Aubrey and she's the VP."

            scene v11lip3h
            with dissolve

            u "So you want to have sort of an open criticism policy?"

            scene v11lip3i
            with dissolve

            li "Of course, that's the only way to make sure everyone, or mostly everyone, is happy or approves of the decisions you are making as a leader."

    scene v11lip3j # FPP. Same as v11lip3, Lindsey serious, mouth closed
    with dissolve

    u "Seems like you have your mind set, so how does this all work?"

    scene v11lip3k # FPP. Same as v11lip3j, Lindsey serious, mouth open
    with dissolve

    li "Normally, we don't have these issues so the presidency is just passed on to whoever the former President wants."
    
    li "Who they choose or endorse rather is always approved by everyone else."

    scene v11lip3j
    with dissolve

    u "How often do you all decide on a new President?"

    scene v11lip3k
    with dissolve

    li "Every half semester we do a vote, but no one ever runs against the current President."
    
    li "So from what I've learned, people just suck up to the President and hope they're chosen when the President leaves."

    scene v11lip3j
    with dissolve

    u "So, you're gonna run against Chloe when we get back?"

    scene v11lip3k
    with dissolve

    li "Yep, but the Chicks have never had multiple candidates before so there's no precedent on how this will go. So, I'm taking upon myself to do this the only way I know how."

    scene v11lip3g
    with dissolve

    u "And how is that?"

    scene v11lip3f
    with dissolve

    li "My way."

    scene v11lip3j
    with dissolve

    u "*Laughs* And what's your way?"

    scene v11lip3k
    with dissolve

    li "I want to run a full campaign and really show the girls why I should be President."

    scene v11lip3j
    with dissolve

    u "How does that work?"

    scene v11lip3k
    with dissolve

    li "Well, it starts with me knowing why I want to be President and putting it into a concise message."

    scene v11lip3d
    with dissolve

    u "So... a slogan?"

    scene v11lip3e
    with dissolve

    li "Exactly, but I'm having trouble coming up with one. I actually planned on meeting with Charli and talking about it, he had some really good ideas."

    scene v11lip3d
    with dissolve

    u "Well, I can help with that. If someone was to ask, like if you were in an interview or something, why do you want to be the Chicks President? What would you say?"

    scene v11lip3e
    with dissolve

    li "Well, in the time that I've been a member of the Chicks, most of what I was led to believe was true is not."
    li "There isn't a strong sense of forever lasting friendship, there isn't women empowerment, there isn't a lot. So, I want to make the promise we were all given come true."

    scene v11lip3i
    with dissolve

    li "That's why I want to be President."

    scene v11lip3h
    with dissolve

    u "Damn, that was some genuine presidential stuff right there. *Chuckles*"

    scene v11lip3i
    with dissolve

    li "*Laughs* I was just being honest."

    scene v11lip3h
    with dissolve

    u "That gives me an idea for a slogan too."

    scene v11lip3i
    with dissolve

    li "What?"

    scene v11lip3d
    with dissolve

    menu:
        "Lindsey, Returning The Promise":
            $ v11_lindsey_slogan = 1

            scene v11lip3h
            with dissolve

            u "Lindsey, Returning The Promise. What do you think?"

        "Lindsey, Say Bye To The Bullshit":
            $ v11_lindsey_slogan = 2

            scene v11lip3h
            with dissolve

            u "Lindsey, Say Bye To The Bullshit. What do you think?"

    scene v11lip3e
    with dissolve

    li "Did you just come up with that off the top of your head?"

    scene v11lip3d
    with dissolve

    u "Well yeah, do you not like it?"

    scene v11lip3e
    with dissolve

    li "No, I love it! I'm just surprised you were able to just come up with a good slogan so quickly."

    scene v11lip3d
    with dissolve

    u "What can I say, I have a talent. Maybe you should ask me to be your VP."

    scene v11lip3i
    with dissolve

    li "Haha, I won't be replacing Aubrey but if I win I'll invite you to our little celebration."

    scene v11lip3h
    with dissolve

    u "You're gonna invite me to a Chicks party? Won't I be the only guy?"

    scene v11lip3i
    with dissolve

    li "Well, yeah. I guess you could bring a friend, though. Maybe Imre or Ryan?"

    scene v11lip3h
    with dissolve

    menu:
        "Imre":
            $ v11_linds_inv_imre = True

            scene v11lip3d
            with dissolve

            u "Imre would definitely be fun to bring."

        "Ryan":
            scene v11lip3d
            with dissolve

            u "Ryan could definitely use a good party."

    scene v11lip3e
    with dissolve

    li "Seems like everything is planned then."

    scene v11lip3d
    with dissolve

    u "What? There's gotta be more than just coming up with a slogan."

    scene v11lip3i
    with dissolve

    li "There is, and I've already got it handled. I'm treating all of the Chicks individually to lunch and telling them that I plan to run and why. Hopefully I'll have their support before the vote."

    scene v11lip3h
    with dissolve

    u "Are you going to tell Chloe?"

    scene v11lip3k
    with dissolve

    li "During the trip I want to give her time to change my mind about running. So I'm not gonna tell her just yet."

    scene v11lip3j
    with dissolve

    u "Sounds good."

    scene v11lip3e
    with dissolve

    li "You kinda got a bit more excited about all of this now with your little slogan. *Chuckles*"

    scene v11lip3d
    with dissolve

    u "My genius abilities cannot be taken lightly. *Laughs*"

    scene v11lip3e
    with dissolve

    li "*Laughs* I'm glad I came to the park today. I'm gonna go run over some more ideas and see what I can come up with."

    scene v11lip3d
    with dissolve

    u "You do that. Madame President. *Chuckles*"

    scene v11lip3i
    with dissolve

    li "Haha, bye [name]... And thanks."

    scene v11lip4 # TPP. Show Lindsey midway through standing up, MC still sitting down, both smiling, mouths closed
    with dissolve

    pause 0.75

    scene v11lip5 # TPP. Show Lindsey walking away, MC still sitting, both smiling, mouths closed
    with dissolve

    pause 0.75

    if v11_lauren_caught_aubrey: # Requirements for apology scene
        scene v11lip6 # TPP. Show MC sitting down he has a slightly relieved expression, mouth closed
        with dissolve

        u "(That was the mental break I needed, let's go ahead and get back to the hotel.)"

    else:
        scene v11lip6a # TPP. Same as v11lip6, MC big smile, mouth closed
        with dissolve

        u "(This day just gets better and better.)"

    stop music fadeout 3

    if emily_europe:
        scene v11lip7 # TPP. Show MC getting up from the bench, slight smile, mouth closed
        with dissolve

        pause 0.75

        scene v11lip8 # TPP. MC is walking on the sidewalk, slight smile, mouth closed
        with dissolve

        pause 0.75

        scene v11lip9 # FPP. MC walking on the sidewalk, he sees Emily walking towards him, she is looking down at her phone, slight smile, mouth closed
        with dissolve

        pause 0.75

        jump v11_emily_sidewalk

    else:
        scene v11lip7
        with dissolve

        pause 0.75

        scene v11lip8
        with dissolve

        pause 0.75

        scene v11lip10 # TPP. Show MC walking into the hotel lobby, mouth closed, slight smile
        with fade

        pause 0.75

        scene v11lip11 # TPP. Show MC walking through the hotel lobby, mouth closed, slight smile
        with dissolve

        pause 0.75

        jump v11_bar_chloe_and_aubrey