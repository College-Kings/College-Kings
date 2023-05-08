# SCENE 8: The Nora Discussion 
# Locations: Hotel Lobby, Hotel Corridor, Hotel Room
# Characters: MC (Outfit: 2), NORA (Outfit: 1) CHRIS (Outfit 1)
# Time: Morning

label v13s8:
    scene v13s8_1 # FPP. MC in hotel lobby, looking at Chris, Chris is walking out of the hotel, neutral expression, mouth closed
    with dissolve

    u "(Hmm, maybe now would be a good time to try and talk to Nora.)"

    play music music.v13_Track_Scene_8 fadein 2

    scene v13s8_2 # TPP. Show MC walking in the hotel lobby towards the corridor, MC slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v13s8_3 # TPP. Show MC walking in the hotel corridor, slight smile, mouth closed
    with dissolve

    pause 0.75

    play sound sound.knock

    scene v13s8_4 # TPP. Show MC knocking on Nora's hotel room door, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v13s8_5 # TPP. Show Nora lying down on her bed, slight smile, mouth open looking at the hotel room door
    with dissolve

    no "Chris? What did you forget?"

    scene v13s8_5a # TPP. Same as v13s8_5, Nora slight smile, mouth closed
    with dissolve

    u "Umm, it's not Chris. It's me, [name]."

    scene v13s8_5
    with dissolve

    no "Oh, one sec."

    scene v13s8_6 # FPP. MC looking at the door, door is being opened by Nora, Nora slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v13s8_6a # FPP. Same as v13s8_6, Nora slight smile, mouth open, door fully open now
    with dissolve

    no "Hey... What's up?"

    scene v13s8_6b # FPP. Same as v13s8_6a, Nora slight smile, mouth closed
    with dissolve

    u "I was just wondering if we could talk?"

    scene v13s8_6a
    with dissolve

    no "Sure, come in."

    scene v13s8_7 # TPP. Show MC walking into the room, following Nora, both slight smiles, mouths closed
    with dissolve

    pause 0.75

    scene v13s8_8 # TPP. Show MC and Nora sitting across each other in the chairs in the room, both slightly smiling, mouths closed
    with dissolve

    pause 0.75

    if "v12_nora" in sceneList:
        scene v13s8_9 # FPP. MC and Nora sitting across each other, Nora slightly worried, mouth open, looking at MC
        with dissolve

        no "I'm sure you want to talk about the other night, right?"

        scene v13s8_9a # FPP. Same as v13s8_9, Nora slightly worried, mouth closed
        with dissolve

        u "Yeah... Right."

        scene v13s8_9
        with dissolve

        no "*Sighs* I knew we'd have to have this conversation sooner or later... I was hoping later so I could prepare myself a bit better."

        scene v13s8_9a
        with dissolve

        u "What do you mean?"

        scene v13s8_9
        with dissolve

        no "Well, I don't know how you're gonna take what I have to say."

        scene v13s8_9a
        with dissolve

        u "Only one way to find out, Nora."

        scene v13s8_9
        with dissolve

        no "Okay... You're right."

        scene v13s8_9b # FPP. Same as v13s8_9, Nora avoiding eye contact, slightly worried, mouth open
        with dissolve

        no "Well... I honestly just feel pretty shitty about the whole thing. Regardless of Chris being a dumbass or not, I shouldn't have done what I did..."

        scene v13s8_9
        with dissolve

        no "I don't believe in cheating at all. I'm so sorry I got you mixed up in all of this... I should have never d-"

        scene v13s8_9c # FPP. Same as v13s8_9a, Nora avoiding eye contact, slightly worried, mouth closed
        with dissolve

        menu:
            "Agree":
                u "*Sighs* I'm not going to sit here and say I didn't enjoy what we shared the other night."

                scene v13s8_9a
                with dissolve

                u "I'm also not gonna act like I don't like you or have no feelings for you, but I do agree. We shouldn't have done what we did while you're in a relationship."

            "Disagree":
                $ nora.points += 1

                scene v13s8_9a
                with dissolve

                u "Nora, you don't have to apologize for anything. You didn't make this decision on your own. I wanted this... I want this."

                scene v13s8_9c
                with dissolve

                u "I understand not believing in cheating, so leave him then. You say that you know he's doing wrong by you, yet you're still wanting to do right by him and it's completely contradicting."

                scene v13s8_9b
                with dissolve

                no "[name], I-"

                scene v13s8_9a
                with dissolve

                u "I mean it when I say this, Nora. I'm not gonna walk around feeling bad for what we did. I didn't do it because I hate Chris, I did it because I really, really like you."

        scene v13s8_9
        with dissolve

        no "*Sighs* This is a lot, [name]. In the moment it felt right but... Now I know for sure that it wasn't."

        scene v13s8_9b
        with dissolve

        no "I can't be a cheater... Regardless of the situation..."

        no "I hope you can understand, [name], I... I don't know what's gonna end up happening between me and Chris, but right now I'd..."

        scene v13s8_9
        with dissolve

        no "I'd rather not make any more mistakes while I'm still in a relationship."

        scene v13s8_9a
        with dissolve

        u "*Sighs* I understand where you're coming from. How do you plan to go about this with Chris?"

        scene v13s8_9b
        with dissolve

        no "I'm not sure, I really just need time to figure everything out. So for now, can we just act as if nothing happened between us?"

        scene v13s8_9c
        with dissolve

        u "I can give you that for right now, but please don't keep me in the dark too much longer."

        scene v13s8_9
        with dissolve

        no "Trust me, I know what it's like wanting someone to communicate. I'll be sure to talk to you about everything as soon as I'm ready."

        scene v13s8_9a
        with dissolve

        u "Ha, okay. Good."

    else:
        scene v13s8_9
        with dissolve

        no "I'm sure like everyone else, you want to know how things are between me and Chris?"

        scene v13s8_9d # FPP. Same as v13s8_9a, Nora slight smile, mouth closed
        with dissolve

        u "Well, I'm more focused on seeing how you are rather than being nosey about your situation."

        scene v13s8_9e # FPP. Same as v13s8_9d, Nora slight smile, mouth open
        with dissolve

        no "Ha, right... I forgot. You're the one who actually cares from time to time."

        scene v13s8_9d
        with dissolve

        u "Yep, that's me. Mr. Cares A Lot."

        scene v13s8_9e
        with dissolve

        no "Haha, well..."

        scene v13s8_9
        with dissolve
        
        no "Things are in a weird place right now. I don't know how to feel about everything and I'm pretty embarrassed with how things went down the other day."

        scene v13s8_9a
        with dissolve

        u "You mean in the lobby?"

        scene v13s8_9
        with dissolve

        no "Yeah. I just feel like him and I need to have a real heart to heart, but he's acting like nothing happened."

        scene v13s8_9c
        with dissolve

        u "Does that bother you?"

        scene v13s8_9
        with dissolve

        no "It does and it doesn't. I want to talk about what happened and where we stand, but I'm also enjoying us just being okay."
        no "He's not busy as much anymore and he's actually been trying to spend time with me, so it's all conflicting."

        scene v13s8_9d
        with dissolve

        u "That's a real pickle you're in. *Chuckles*"

        scene v13s8_9a
        with dissolve

        u "Planning on just letting time tell?"

        scene v13s8_9
        with dissolve

        no "That's exactly my plan, I think."

        scene v13s8_9d
        with dissolve

        u "Let's just hope that the ending is a good one."

        scene v13s8_9e
        with dissolve

        no "I'll be praying for it."

        scene v13s8_9d
        with dissolve

        u "Haha, good."

    scene v13s8_9f # FPP. Same as v13s8_9d, Nora different pose
    with dissolve

    u "Anything changed in the Nora and Chloe story?"

    scene v13s8_9g # FPP. Same as v13s8_9f, Nora slight smile, mouth open
    with dissolve

    no "Yeah. #LindseyForPresident."

    scene v13s8_9f
    with dissolve

    u "So, you know about that?"

    scene v13s8_9g
    with dissolve

    no "Everyone does, haha. All of the Chicks are secretly deciding who they'll vote for when it all goes down."

    scene v13s8_9d
    with dissolve

    u "And you're voting for Lindsey?"

    scene v13s8_9e
    with dissolve

    no "Wouldn't you?"

    scene v13s8_9d
    with dissolve

    menu:
        "Yeah":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            scene v13s8_9f
            with dissolve

            u "Yeah, I think I'd have to pick Lindsey at the moment."

        "I haven't decided yet":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            scene v13s8_9f
            with dissolve

            u "I wouldn't go one way or the other just yet."

    scene v13s8_9g
    with dissolve

    no "I have to go for Lindsey, regardless of what I just found out."

    scene v13s8_9f
    with dissolve

    u "What is it that you just found out?"

    scene v13s8_9g
    with dissolve

    no "You probably already know, but the fact that Chloe has to be the President of Chicks in order to keep her Greek scholarship?"

    scene v13s8_9d
    with dissolve

    u "Wait, what? I didn't know that!"

    scene v13s8_9h # FPP. Same as v13s8_9d, Nora slightly serious expression, mouth open
    with dissolve

    no "I assumed since you guys are close, that you'd know..."

    scene v13s8_9i # FPP. Same as v13s8_9h, Nora slightly serious, mouth closed
    with dissolve

    u "I had no idea... Damn, a scholarship? Why does she have to be President though? She can't just be a member?"

    scene v13s8_9h
    with dissolve

    no "Nope, it's limited to Presidents and if she loses it, she'll have to find another way to pay for next semester."

    scene v13s8_9b
    with dissolve

    no "I feel bad, but I'm not going to give her a pity vote. If the whole story of her situation got out to everyone then she may get some pity votes, but not from me."

    scene v13s8_9i
    with dissolve

    u "Wow, that adds a whole other dynamic to this situation."

    scene v13s8_9h
    with dissolve

    no "Yep, it's crazy how much this Chicks stuff has affected everyone. You wouldn't believe it, but Chloe and I used to be really close."

    scene v13s8_9d
    with dissolve

    u "You're right, I wouldn't believe it. *Laughs*"

    scene v13s8_9e
    with dissolve

    no "Haha, we were! But once we got involved in the Chicks, things changed."

    scene v13s8_9d
    with dissolve

    u "It's like that sometimes. I would've thought it'd only make you guys closer..."

    scene v13s8_9g
    with dissolve

    no "It did at first, but then she became President and our disagreements started to show."

    scene v13s8_9f
    with dissolve

    u "Yeah, except this time it's not just you with those disagreements. Let's hope everything works out."

    scene v13s8_9g
    with dissolve

    no "You and I both."

    scene v13s8_9d
    with dissolve

    u "I'm gonna get out of your hair then. We'll talk soon I hope?"

    scene v13s8_9e
    with dissolve

    no "We will, thanks for coming by."

    scene v13s8_9d
    with dissolve

    u "Of course."

    scene v13s8_10 # TPP. Show MC and Nora getting up from the chair, both slightly smiling, mouths closed
    with dissolve

    pause 0.75

    scene v13s8_11 # TPP. Show MC and Nora hugging
    with dissolve

    pause 1.75

    scene v13s8_12 # TPP. Show MC walking out of the room, slight smile, mouth closed
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v13s9