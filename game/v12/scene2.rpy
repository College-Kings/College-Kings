# SCENE 2: Nora checks in on MC
# Location: Hotel room
# Characters: MC (Outfit 3), Nora (Outfit 2)
# Time: Night

label v12_nora_checks_mc:
    scene v12ncm1 # TPP. MC goes to answer the door
    with fade

    pause 0.75

    play music "music/v12/Track Scene 2.mp3" fadein 2

    scene v12ncm2 # FPP. MC opens the door and nora is standing there, mouth closed
    with dissolve

    u "Hey, Nora."

    scene v12ncm2a # FPP. Same as v12ncm2, mouth opened
    with dissolve

    no "Uhm, hey... Mind if I come in?"

    scene v12ncm2 
    with dissolve

    u "Of course not."

    scene v12ncm3 # TPP. MC and Nora walk in the room
    with dissolve

    pause 0.75

    scene v12ncm4 # TPP. MC and nora sit at the foot of mc's bed
    with dissolve

    pause 1

    if v12_chase_robber: 
        scene v12ncm5 # FPP. Nora looks at mc with a worried face, mouth opened
        with dissolve

        no "Are you okay?"

        if nora.relationship.value >= Relationship.LIKES.value:
            scene v12ncm5a # FPP. Nora with a slight smile, mouth opened
            with dissolve

            no "You always jump to do things for me, so I'm not surprised you went after him."

        else: 
            scene v12ncm5a
            with dissolve

            no "You were one of the last people I expected to do something like that for me."

        scene v12ncm5b # FPP, Same as 5a, mouth closed
        with dissolve

        u "I'm fine, really. I may have taken a few hits, but I'm alright. I planned on doing whatever it took to get it back to you, haha."

        scene v12ncm5a
        with dissolve

        no "For someone that just got into an alley fight with a robber from a foreign country, you're in an awfully good mood. *Chuckles* Are you sure you're okay?"

        scene v12ncm5b
        with dissolve

        u "I'm fine. *Chuckles*"

        scene v12ncm5c # FPP. Nora gets closer to mc
        with dissolve

        pause 0.75

        scene v12ncm6 # TPP. Nora grabs mc face and start looking him over
        with dissolve

        pause 0.75

        scene v12ncm5d # FPP. Nora looking over MC still, mouth opened
        with dissolve

        no "Hmm, no cuts or anything. Maybe you got hit in the head."

        scene v12ncm5e # FPP. Same as 5d, mouth closed
        with dissolve

        u "Maybe, but it didn't do anything if I did. I feel pretty good."

        scene v12ncm5d
        with dissolve

        no "My Uncle and my Dad got into a fight at our family cookout one time, and my uncle had a cut on his head that we didn't notice until later that day. Come here."

        scene v12ncm7 # TPP, Nora grabs MC's head and moves it down toward her breast as she looks at his head
        with dissolve

        pause 0.6

        scene v12ncm5l # FPP. Camera looking at nora's brest
        with dissolve

        u "*Gulp*"

        no "Hmm, maybe you are fine."

        scene v12ncm5f # FPP. MC sitting back up, looking at nora, mouth closed
        with dissolve

        u "Told you."

        scene v12ncm5g # FPP. Same as 5f, mouth opened
        with dissolve

        no "You know, guys only go out of their way for girls when they want something."

        if v11_kiss_nora:
            scene v12ncm5g
            with dissolve

            no "Sometimes I wonder if you're like that."

            scene v12ncm5f
            with dissolve

            u "I'd like to think I'm not. Sometimes I just do things because it's the right thing to do."

        else:
            scene v12ncm5h # FPP. nora looking puzzled, mouth opened
            with dissolve

            no "You've been nice to me though, just to be nice..."

            scene v12ncm5f 
            with dissolve

            u "Sometimes it's about just doing the right thing."

        scene v12ncm5g
        with dissolve

        no "The right thing for me tonight was to make sure I came over here and thanked you."

        scene v12ncm5f
        with dissolve

        u "Well, you're more than welcome. I just had a feeling that what you had in your bag tonight was important, so I didn't even second guess going after him."

    else:
        scene v12ncm5g
        with dissolve

        no "I... I really didn't like being surrounded like that after everything that happened."

        scene v12ncm5f
        with dissolve

        u "Oh, yeah I could see that. I'm really sorry I ran over there like that. I guess I was just really concerned about you."

        scene v12ncm5h 
        with dissolve

        no "You know... That's the odd thing. When I looked up and you were there, it didn't bother me. I was actually happy you ran over to me."
        no "It kinda seems like whenever I really need someone, even if it's just to talk, you're always around."

        scene v12ncm5f
        with dissolve

        u "Oh, that's just 'cause of my superpower. It lets me know when a helpless girl is in need."

        scene v12ncm5i # FPP. Nora looking annoyed, mouth opened
        with dissolve

        no "Are you calling me helpless?"

        scene v12ncm5f 
        with dissolve

        u "Haha, maybe."

        scene v12ncm5j # FPP. Nora makes an agressive face, mouth opened
        with dissolve

        no "Should I be regretting coming over here and thanking you?"

        scene v12ncm5f 
        with dissolve

        u "I was just-"

        scene v12ncm5a 
        with dissolve

        no "*Laughs* Too bad your powers don't tell you when someone's teasing."

        scene v12ncm5f 
        with dissolve

        u "*Laughs*"

        scene v12ncm5f 
        with dissolve

        u "Hey, um... I hope you don't mind me asking, but I assume whatever you had in that bag was pretty important? I don't think I've ever seen you with a bag before."

    scene v12ncm5g
    with dissolve

    no "It was pretty important."

    scene v12ncm5f
    with dissolve

    u "Do you want to talk about it?"

    scene v12ncm5a
    with dissolve

    no "It was a picture of me and my Dad. Back when he was more of a family man."

    scene v12ncm5f
    with dissolve

    u "Oh sorry, I didn't mean to open any wounds."

    scene v12ncm5a
    with dissolve

    no "You're fine, ha. You can't be mad at your knight in shining armor... or at least that's what Imre keeps saying."

    scene v12ncm5f
    with dissolve

    u "I was a little surprised with how much interest he's taken in this whole thing. I think his beef with Ryan and the fact that Chris has been so busy, is making him seek a new bromance. *Chuckles*"

    scene v12ncm5f
    with dissolve

    no "..."

    scene v12ncm5f
    with dissolve

    u "Sorry... I didn't mean to bring up Chris."

    scene v12ncm5i
    with dissolve

    no "*Sighs* It's fine. At least you didn't mean to. Chris is all Charli wants to talk about. He thinks talking about it will make me feel better."
    no "I get that he's trying to be nice, so I can't be mad... But jeez... Plus, I just met the guy you know?"

    scene v12ncm5f
    with dissolve

    u "Oh, I know. Please don't get me started on Charli..."

    scene v12ncm5a
    with dissolve

    no "Oh, I didn't know that you guys don't get along... I hadn't noticed. *Chuckles*"

    scene v12ncm5f
    with dissolve

    u "*Chuckles* Funny."

    scene v12ncm5k # FPP. Nora has a big smile, mouth opened
    with dissolve

    no "Haha, really though. I just wanted to come by and say thank you for being there for me. It's been hard to get that kind of loyalty from people lately."

    scene v12ncm5f
    with dissolve

    u "I'm always here."

    scene v12ncm5k
    with dissolve

    no "I like that."

    if nora.relationship.value >= Relationship.LIKES.value:
        scene v12ncm8 # TPP. Nora gives MC a hug
        with dissolve

        pause 1.25

        scene v12ncm9 # TPP. Nora leaves
        with dissolve

    else:
        scene v12ncm9
        with dissolve

    pause 1

    play sound "sounds/doorclose.mp3"

    stop music fadeout 3

    if v11_pen_goes_europe:
        jump v12_penelope_roof #scene 3
    
    else:
        jump v12_penelope_call #scene 3a