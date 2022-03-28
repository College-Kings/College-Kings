# SCENE 26: Walking to Sex Ed Event
# Locations: Walking the hallways of SVC
# Characters: MC (Outfit: 9), LINDSEY (Outfit: 1), PENELOPE (Outfit: 3)
# Time: Morning

label v16s26:
    scene v11coc1x
    with fade
    
    pause 0.75

    scene v16s26_1 # TPP. Show MC walking down the hallway of SVC, neutral face, mouth closed.
    with dissolve

    pause 0.75

    scene v16s26_2 # TPP. Show MC walking down the Hallway of SVC further down the hall, Lindsey now walking to next to MC but he doesn't notice, Lindsey slight smile, mouth closed, MC neutral face, mouth closed.
    with dissolve

    pause 0.75

    scene v16s26_2a # TPP. MC jumps back, slightly scared as he turns to see Lindsey next to him, Lindsey slight smile, mouth closed, MC surprised, mouth open.
    with dissolve

    u "Oh shi- Hey, Linds."

    scene v16s26_3 # FPP. MC and Lindsey standing still in the halls, MC looking at Lindsey, Lindsey looking at MC, Lindsey slight smile, mouth open.
    with dissolve

    li "Haha, did I make you jump?"

    scene v16s26_3a # FPP. MC and Lindsey standing still in the halls, MC looking at Lindsey, Lindsey looking at MC, Lindsey slight smile, mouth closed.
    with dissolve

    u "Not at all, ha."

    scene v16s26_3
    with dissolve

    li "Hmm... Looked like you jumped a bit. *Laughs*"

    scene v16s26_3a
    with dissolve

    u "No way. I'm unjumpable."

    scene v16s26_3
    with dissolve

    li "Unjumpable?"

    scene v16s26_3a
    with dissolve

    u "The opposite of \"jumpable\"?"

    scene v16s26_3
    with dissolve

    li "I don't think either of those are words..."

    scene v16s26_3a
    with dissolve

    u "Hmph. Agree to disagree."

    if v15_lindsey_recording > 0:
        scene v16s26_3a
        with dissolve

        u "How are you getting on with those bonsai therapy sessions?"

        scene v16s26_3
        with dissolve

        li "Ah, you heard about that."

        li "Mr. Lee's got us pruning his little trees for an hour every day."

        scene v16s26_3a
        with dissolve

        u "A whole hour?"

        scene v16s26_3
        with dissolve

        li "Yes... *Sighs*"

        li "It's the weirdest punishment ever. He even plays meditation music while we're doing it."

        scene v16s26_3a
        with dissolve

        u "*Laughs*"

        scene v16s26_3
        with dissolve

        li "It's not funny! He also reads out quotes from some book about positive thinking and the importance of respect... Ugh."

        scene v16s26_3a
        with dissolve

        u "Classic Mr. Lee... The man is an actual character."

        scene v16s26_3
        with dissolve

        li "*Sighs* Anyway, enough about that."

    li "Autumn was telling me about the dog shelter re-opening and how you've been helping her?"
    
    menu:
        "Yeah, it's great":
            $ add_point(KCT.BRO)
            
            scene v16s26_3a
            with dissolve

            u "Oh, yeah! It's been great. I'm excited to go back and see how the little guys are doing."

        "Yeah, she's great":
            $ add_point(KCT.BOYFRIEND)
            
            scene v16s26_3a
            with dissolve

            u "Oh, yeah! Autumn's great. She really cares about the animals and honestly, a lot cooler than I thought she was, haha."

            scene v16s26_3
            with dissolve

            li "I know! Ever since we hung out the other night, I can't help but love her. She's so chill."

            scene v16s26_3a
            with dissolve

            u "Yeah, for sure. Helping her out at the shelter has been a blast, the dogs are amazing."

    scene v16s26_3
    with dissolve

    li "Haha, that's sweet."

    li "I really wanted to attend the re-opening, but I won't have the time that day... Can you take the donation for me and make sure it gets into the right hands?"

    $ mc.money += 50

    scene v16s26_3a
    with dissolve

    u "Yeah, sure."

    scene v16s26_3b # FPP. MC and Lindsey still standing in the middle of the hallway, Lindsey handing MC some cash, Lindsey slight smile, mouth open.
    with dissolve

    li "Thanks. That should help a few fur babies."

    scene v16s26_3c # FPP. MC and Lindsey still standing in the middle of the hallway, MC grabbing the cash, Lindsey slight smile, mouth closed.
    with dissolve

    u "Haha, I'm sure they'll appreciate it. I'll give it Autumn as soon as I see her."

    scene v16s26_4 # TPP. Show Penelope walking up to Lindsey and MC, All slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v16s26_5 # FPP. MC looking at Penelope who is next to him and Lindsey(Lindsey off camera [MC is in between them]), Penlope looking at MC, Penelope slight smile, mouth open.
    with dissolve

    pe "Hey, you two!"

    scene v16s26_5a # FPP. MC looking at Penelope, Penelope looking at MC, slight smile, mouth closed.
    with dissolve

    u "Penelope, it's too early to be that happy... *Chuckles*"

    scene v16s26_5
    with dissolve

    pe "No, come on! Wake up! I have huge news, guys."

    scene v16s26_3
    with dissolve

    li "Uh, oh. Huge news, [name]."

    scene v16s26_5a
    with dissolve

    u "*Sighs* Okay, hit me with it."

    scene v16s26_5
    with dissolve

    pe "Okay... So, guess who's coming to perform a little concert for us tomorrow night, all because of me?"

    menu:
        "The music majors":
            scene v16s26_5a
            with dissolve

            u "The music majors?"

            scene v16s26_3
            with dissolve

            li "Oh, nice guess."

            scene v16s26_3a
            with dissolve

            u "Hey, thanks."

            scene v16s26_5
            with dissolve

            pe "Haha, no, you idiot!"

            scene v16s26_3
            with dissolve

            li "*Laughs*"

            scene v16s26_5
            with dissolve

            pe "Why would I- Nevermind, who cares. Anyway!"

        "No idea, who?":
            scene v16s26_5a
            with dissolve

            u "I've got no idea. Who?"

            scene v16s26_3d # FPP. MC looking at Lindsey, Lindsey looking at Penelope(Off-camera), Lindsey slight smile, mouth open.
            with dissolve

            li "Yeah, don't keep us in suspense over here!"

    scene v16s26_5
    with dissolve

    pe "Polly!"

    scene v16s26_3d
    with dissolve

    li "Polly? THE Polly?!"

    scene v16s26_5b # FPP. MC looking at Penelope, Penelope looking at Lindsey (off camera), Penelope slight smile, mouth open.
    with dissolve

    pe "The one and only Polly!"

    scene v16s26_3d
    with dissolve

    li "Wha- Ahh! That's amazing, Penelope!"

    scene v16s26_6 # TPP. Show Penelope and Lindsey holding hands around MC while jumping in the air (fangirling) while MC is stuck in the middle, MC awkward face, mouth closed, Lindsey and Penelope excited, mouth open.
    with dissolve

    li "OMG!"

    pe "EEEEE!"

    scene v16s26_3d
    with dissolve

    li "How the hell did you make friends with her?"

    if v13_penelope_concert:
        scene v16s26_3a
        with dissolve

        u "We went to her concert in Amsterdam."

        if len(v12s7_killList) >= 5:
            scene v16s26_5b
            with dissolve

            pe "Yeah, backstage passes and all!"

        elif v13_penelope_backstage: # TODO: Variable
            scene v16s26_5b
            with dissolve

            pe "Yeah, she invited us backstage!"

        scene v16s26_5b
        with dissolve

        pe "She really liked us for some reason, and we became best friends somehow... *Laughs* The craziest night of my life."

        scene v16s26_5a
        with dissolve

        u "Don't act all humble now. You're the one she liked."

        scene v16s26_3d
        with dissolve

        li "I'm so fucking jealous."

    elif not v13_penelope_concert: # TODO: Variable
        scene v16s26_5b
        with dissolve

        pe "There was a meet and greet recently where she was signing stuff and promoting her new single."

        pe "We just hit it off, I don't even know how to explain it. She said we were like long lost sisters or something, haha!"
        
        if v13_aubrey_concert: # TODO: Variable
            scene v16s26_5c # FPP. MC looking at Penelope, Penelope looking at Lindesy, Penelope slight smile, mouth closed.
            with dissolve

            u "(Polly's in town? Huh. I wonder if she'd recognize me?)"

    elif not v13_penelope_concert and not v13_aubrey_concert:
        scene v16s26_5a
        with dissolve

        u "Polly?"

        scene v16s26_5
        with dissolve

        pe "A pop sensation, [name]."

    scene v16s26_3d
    with dissolve

    li "Oh my god, you're living my actual dream!"

    scene v16s26_5b
    with dissolve

    pe "Haha, I connected with her on Kiwii and we've been talking about SVC."

    scene v16s26_5a
    with dissolve

    u "Oh, shit."

    scene v16s26_5
    with dissolve

    pe "She'll only have time to sing a few songs, but she's actually coming to our college, guys!"

    scene v16s26_3d
    with dissolve

    li "I can't believe it. Polly is coming here... To SVC!"

    scene v16s26_5b
    with dissolve

    pe "I know! *Screams*"

    pe "Make sure you're free that night. You'll know when."

    scene v16s26_5a
    with dissolve

    u "We will, for sure."

    scene v16s26_3d
    with dissolve

    li "Yeah, I wouldn't miss it for the world."

    scene v16s26_5
    with dissolve

    pe "Oh, [name], how did it go with Imre?"

    scene v16s26_5a
    with dissolve

    u "Ah, it's always drama with him. But I think he had real feelings for Karen, sadly. He really wanted a second date."

    scene v16s26_3
    with dissolve

    li "Wait. Imre and Karen? What happened?"

    scene v16s26_5b
    with dissolve

    pe "I'll tell you later, Linds, don't worry."

    scene v16s26_3d
    with dissolve

    li "Yeah, I need to hear all about that. *Chuckles*"

    scene v16s26_5a
    with dissolve

    u "What was Karen's excuse?"

    scene v16s26_5
    with dissolve

    pe "She didn't have one. That guy just told her she was hot and asked her for a kiss."

    scene v16s26_5a
    with dissolve

    u "And that worked?"

    scene v16s26_5
    with dissolve

    pe "Haha, yeah... I guess it works on some people. They're going on a date next week."

    scene v16s26_5a
    with dissolve

    u "Yikes, it sucks for Imre."

    scene v16s26_3
    with dissolve

    li "Yeah, but if you're with the wrong person, your heart will keep searching for the right one."

    scene v16s26_3a
    with dissolve

    u "Wow. Very wisdomous today."

    scene v16s26_3
    with dissolve

    li "Again, I don't think that's a word..."

    scene v16s26_5b
    with dissolve

    pe "But he's right. That was a smart sentence, I'm proud of you. *Giggles*"

    scene v16s26_3e # FPP. Lindsey jokingly pretending tobe upset, MC looking at Lindsey, Lindsey slight smile, mouth open.
    with dissolve

    li "Oh god... It's the therapy sessions!"

    u "*Laughs*"

    scene v16s26_5d # FPP. MC looking at Penelope, Penelope looking at her phone, slight smile, mouth open.
    with dissolve

    pe "We should probably get to class now."

    scene v16s26_3d
    with dissolve

    li "Oh, yeah! That's what I was going to tell you in the first place, haha!"

    li "Classes are cancelled today, but we're all supposed to attend a lecture about parenting or sex, or something."

    scene v16s26_3a
    with dissolve

    u "Hmm. Parenting or sex or something..."

    scene v16s26_5
    with dissolve

    pe "Wow. Well, let's find out, shall we? *Laughs*"

    scene v16s26_5a
    with dissolve

    u "We shall!"

    scene v16s26_7 # TPP. Show MC in the middle of Penelope and Lindsey, the girls arms linked with MC's arms as they skip/walk down the hallway, all slight smile, mouth closed.
    with dissolve

    pause 0.75

    jump v16s27