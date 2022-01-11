# SCENE 37: Garden Free Roam
# Locations: Garden
# Characters: LINDSEY (Outfit: 1), CHRIS (Outfit: 1), MC (Outfit: 5), NORA (Outfit: 1), IMRE (Outfit: 2)
# Time: Evening

label v13s37:
    scene v13s37_1 # TPP. Show MC, Chris, Nora, Lindsey and Imre standing in the garden, all slight smiles, mouths closed, standing in a circle as if they were chatting
    with dissolve

    pause 0.75

    play music "music/v13/Track Scene 37_1.mp3" fadein 2

    scene v13s37_2 # FPP. Same positioning as v13s37_1, MC looking at Lindsey, Lindsey looking at Chris' direction (Only Lindsey in shot), Lindsey slight smile, mouth open
    with dissolve

    li "Well, you didn't come short in choosing a location, Chris... I gotta give you that."

    scene v13s37_2
    with dissolve

    li "This is beyond gorgeous."

    scene v13s37_3 # FPP. Same as v13s37_1, MC looking at Chris, Chris looking at Lindsey, only Chris in shot, Chris slight smile, mouth open
    with dissolve

    ch "Thanks Lindsey, Ms. Rose suggested it to me when I told her I wanted a relaxing environment for the day."

    scene v13s37_2
    with dissolve

    li "Well, her suggestions never disappoint. *Chuckles*"

    scene v13s37_2a # FPP. Same as v13s37_2, Lindsey mouth closed
    with dissolve

    u "(You can say that a million times again...)"

    scene v13s37_3a # FPP. Same as v13s37_3, Chris looking at Nora, Chris slight smile, mouth open
    with dissolve

    ch "Do you like it, Nora?"

    scene v13s37_4 # FPP. Same positioning as v13s37_1, MC looking at Nora, Nora looking at Chris, only Nora in shot, Nora slight smile, mouth open
    with dissolve

    no "Yeah, it's really nice."

    scene v13s37_5 # FPP. Same positioning as v13s37_1, MC looking at Imre, Imre looking at Lindsey, only Imre in shot, Imre slight smile, mouth open
    with dissolve

    imre "I could see myself building a house on some land with this as my backyard."

    scene v13s37_2b # FPP. Same a sv13s37_2, Lindsey looking at Imre
    with dissolve

    li "Oooh, okay! I may have to hang out at your house... *Laughs*"

    scene v13s37_5
    with dissolve

    imre "You can always just come by my room if you're tryna chill, Linds..."

    scene v13s37_2b
    with dissolve

    li "*Chuckles* Not like that, fuckboy."

    if lindsey.relationship >= Relationship.FWB:
        li "And don't call me Linds... Only the girls and [name] get to call me that. *Laughs*"

    scene v13s37_5
    with dissolve

    imre "Well, damn. *Chuckles*"

    scene v13s37_5a # FPP. Same as v13s37_5, Imre looking at MC
    with dissolve

    imre "[name], when I have this at my crib we're gonna have to host fights in the yard and shit."

    scene v13s37_5b # FPP. Same as v13s37_5b, Imre mouth closed
    with dissolve

    u "Ha... Like a little fight club?"

    scene v13s37_5a
    with dissolve

    imre "Yes! Exactly like that."

    scene v13s37_5b
    with dissolve

    u "Do I get a cut of the bet?"

    scene v13s37_5a
    with dissolve

    imre "We'll discuss your cut of profits at a later date..."

    scene v13s37_5b
    with dissolve

    u "Haha, okay boss. You got it."

    scene v13s37_3b # FPP. Same as v13s37_3, Chris looking at MC
    with dissolve

    ch "Let's go enjoy ourselves, people."

    stop music fadeout 3
    play music "music/v13/Track Scene 37_2.mp3" fadein 2
    call screen v13s37_garden1

label v13s37_nora:
    $ freeroam11.add("nora")

    scene v13s37no_1 # TPP. Show MC approaching Nora, she's sitting and hiding behind a big rock, hiding, both mouths closed, MC slight smile, Nora slightly sad
    #with dissolve

    pause 0.75

    scene v13s37no_2 # FPP. MC standing in front of Nora, Nora looking at MC, Nora slight smile, mouth closed
    with dissolve

    u "Hiding?"

    scene v13s37no_2a # FPP. Same as v13s37no_2, Nora mouth open
    with dissolve

    no "Obviously not good enough... *Chuckles*"

    no "But it's no surprise you'd be the one to find me."

    scene v13s37no_2b # FPP. Same as v13s37no2, Nora slightly sad, mouth closed
    with dissolve

    u "It is a surprise seeing you and Chris together, holding hands and still slightly smiling at each other after everything that's happened."

    scene v13s37no_2c # FPP. Same as v13s37no_2b, mouth open
    with dissolve

    no "If it wasn't obvious to you already, I've been feeling pretty awkward around him lately."

    no "I'm not even confident about my relationship and he's starting to do all of the things that I asked for."

    scene v13s37no_2b
    with dissolve

    pause

    scene v13s37no_2c
    with dissolve

    no "Right after he was a dick to me for weeks and shoved me to the fucking ground... Like, am I supposed to be happy? Pissed off? Sad? Or grateful..."

    scene v13s37no_2b
    with dissolve

    u "I saw you avoiding him and it looks as though every smile you give is forced so hard that you're going to throw up. *Chuckles*"

    scene v13s37no_2c
    with dissolve

    no "Is it super obvious? He hasn't seemed to notice and... This is the first time someone's said anything to me ."

    scene v13s37no_2b
    with dissolve

    u "They may not have said anything, but it's obvious to most of your friends."

    scene v13s37no_2d # FPP. Same as v13s37no_2b, Nora looking down
    with dissolve

    u "You're not so sure about everything like you used to be, and Chris is a good actor, but you can't fool the people who truly pay attention."

    scene v13s37no_2b
    with dissolve

    u "He's acting as if everything that happened didn't happen and he's acting like he doesn't notice the tension."

    scene v13s37no_2c
    with dissolve

    no "*Sighs* And then there's Lindsey..."

    no "She's been spying on me and Imre's been doing the same to Chris. We didn't invite them, they invited themselves as our plus ones."

    scene v13s37no_2b
    with dissolve

    u "Lindsey really cares about you, and Imre is very loyal to Chris so it makes a lot of sense."

    scene v13s37no_2e # FPP. Same as v13s37no_2d, Nora hands on her face, mouth open, slightly sad
    with dissolve

    no "*Sighs* *Muffled* What am I going to do?"

    scene v13s37no_2c
    with dissolve

    no "I need advice from someone who really knows me."

    scene v13s37no_2b
    with dissolve

    u "Am I not that kind of someone?"

    scene v13s37no_2c
    with dissolve

    no "Not yet... You may someday, but I'm talking about my family. Specifically my stepmom."

    if joinwolves:
        scene v13s37no_2d
        with dissolve

        u "(I wonder if she'll confess about Ms. Rose.)"

    scene v13s37no_2b
    with dissolve

    u "I don't think you've ever said much to me about your family, what's your stepmom like?"

    scene v13s37no_2c
    with dissolve

    no "*Sighs* Please try not to overreact when I tell you this... And I beg you, don't go around telling everybody, but..."

    no "Ms. Rose is actually my stepmom."

    scene v13s37no_2d
    with dissolve

    u "...You're joking."

    scene v13s37no_2c
    with dissolve

    no "I'm really not. I'll go into more detail another time, but that's why Chris and the rest of the Wolves are so close with her."

    scene v13s37no_2f # FPP. Same as v13s37no_2c, different pose
    with dissolve

    no "She wanted to help me out so she tried to make Chris' life easier."

    scene v13s37no_2b
    with dissolve

    u "That's a lot to process. I won't harp on it right now though."

    scene v13s37no_2c
    with dissolve

    no "Thank you."

    scene v13s37no_3 # TPP. Show MC moving to sit down next to Nora, both slight sad mouths closed
    with dissolve

    pause 0.75

    scene v13s37no_4 # FPP. MC sitting next to Nora, both looking at each other, Nora slighty sad, mouth closed
    with dissolve

    u "*Sighs* I'm gonna sit here and act like this situation doesn't bother me."

    scene v13s37no_4a # FPP. Same as v13s37no_4, Nora looking down
    with dissolve

    u "Seeing you uncomfortable alone is enough to bother me. I just wish I could wave a wand and fix all of your problems."

    scene v13s37no_4b # FPP. Same as v13s37no_4, Nora mouth open
    with dissolve

    no "You and I both..."

    if nora.relationship < Relationship.FWB:
        scene v13s37no_4a
        with dissolve

        u "I'm sure you came over here for some alone time before I interrupted, so I'll leave you be."

        scene v13s37no_4
        with dissolve

        u "You come find me if there's anything I can do, okay?"

        scene v13s37no_4c # FPP. Same as v13s37no_4b, Nora slight smile
        with dissolve

        no "I will, thanks [name]."

        scene v13s37no_4d # FPP. Same as v13s37no_4, Nora slight smile
        with dissolve

        u "Anytime."

        scene v13s37no_5 # TPP. Show MC getting up, Nora still sitting down, both slight smiles, mouths closed
        with dissolve

        pause 0.75

        scene v13s37no_1a # TPP. Same as v13s37no_1, MC walking away
        with dissolve

        pause 0.75

    else:
        scene v13s37no_6 # TPP. Same positioning as v13ss37_4, Nora putting her head on MC's shoulder, Nora eyes closed, MC mouth closed, surprised, Nora mouth closed, slightly sad
        with dissolve

        u "(Oh wow, she... She does look to me.)"

        scene v13s37no_4a
        with dissolve

        u "Nora, look at me."

        scene v13s37no_4
        with dissolve

        u "You know how I feel about you, I feel like I've proved that already."

        scene v13s37no_4a
        with dissolve

        u "So during this period of time where you're thinking your life out, remember me, okay?"

        scene v13s37no_4b
        with dissolve

        no "[name]..."

        scene v13s37no_4
        with dissolve

        u "Okay?"

        scene v13s37no_4c
        with dissolve

        no "I... Yeah. I'll remember."

        scene v13s37no_4d
        with dissolve

        u "Good."

        scene v13s37no_4c
        with dissolve

        menu:
            "Kiss her forehead":
                play sound "sounds/kiss.mp3"
                scene v13s37no_7 # TPP. Show MC kissing Nora's forehead, Nora slight smile, mouth closed
                with dissolve

                pause

                scene v13s37no_5
                with dissolve

                pause 0.75

                scene v13s37no_1a
                with dissolve

                pause 0.75

            "Kiss her lips":
                $ v13_imre_disloyal = True

                play sound "sounds/kiss.mp3"
                scene v13s37no_8 # TPP. MC and Nora kissing
                with dissolve

                pause

                scene v13s37no_9 # TPP. MC and Nora kissing, Nora's hand on MC's head, MC's hand on her neck
                with dissolve

                pause

                scene v13s37no_10 # TPP. MC and Nora kissing, Nora's hand on MC's hand and thigh, MC's hand over one of her boobs, other one on her neck
                with dissolve

                pause

                scene v13s37no_11 # TPP. Show MC and Nora pulling away from kiss, Imre standing in front of them, MC and Nora startled, mouths closed, Imre mouth open, angry
                with dissolve

                imre "*Whisper* What the fuck are you doing?!"

                scene v13s37no_12 # FPP. Same positioning as v13s37no_11, MC looking at Imre, Imre looking at MC, Imre angry, mouth closed
                with dissolve

                u "Imre! We uhh..."

                scene v13s37no_12a # FPP. Same as v13s37no_12, Imre mouth open
                with dissolve

                imre "Don't even try gaslighting me into not believing what the fuck I just saw."

                scene v13s37no_12b # FPP. Same as v13s37no_12a, Imre looking at Nora
                with dissolve

                imre "How could you guys do this to Chris?! Nora, you're dating Chris..."

                scene v13s37no_4e # FPP. Same as v13s37no_4, Nora looking at Imre, Nora worried, mouth open
                with dissolve

                no "Imre, I know you and Chris are really close, but I'm really need you to not say anything."

                scene v13s37no_12b
                with dissolve

                imre "Ha! Why the hell not?"

                scene v13s37no_4e
                with dissolve

                no "It'd destroy him, Imre! Okay?"

                scene v13s37no_12b
                with dissolve

                imre "So, you want me to act like this just didn't happen? I can't do that shit."

                scene v13s37no_12
                with dissolve

                u "Imre, please bro."

                scene v13s37no_12a
                with dissolve

                imre "Don't \"bro\" me right now!"

                scene v13s37no_12c # FPP. Same as v13s37no_12a, Imre pointing at MC
                with dissolve

                imre "You obviously don't even understand the meaning of the fucking word."

                scene v13s37no_4f # FPP. Same as v13s37no_4e, Nora slightly annoyed, mouth open
                with dissolve

                no "Imre... Do not act like my relationship with Chris has been perfect, and for fuck's sake, don't act like the problems we've had are my fault."

                scene v13s37no_4g # FPP. Same as v13s37no_4f, Nora pointing at Imre
                with dissolve

                no "Sure. He's been a good boyfriend for two days. But what about the weeks before that?!"

                scene v13s37no_4f
                with dissolve

                no "[name] has been there for me as a friend but, in ways that I'd expect my perfect man to be there for me."

                scene v13s37no_4g
                with dissolve

                no "You may be loyal to Chris and I get that, but please Imre. Don't act as though he's perfect."

                scene v13s37no_12b
                with dissolve

                imre "*Sighs* Ahhh!"

                scene v13s37no_12a
                with dissolve

                imre "Why would you put me in a situation like this?!"

                scene v13s37no_12c
                with dissolve

                imre "You know what? I'm gonna be quiet. But not because of you. Or you, for that matter."

                scene v13s37no_12b
                with dissolve

                imre "I'm doing it for Chris. And I already was, but I'll be even more determined to convince him to leave your cheating ass."

                scene v13s37no_12c
                with dissolve

                imre "And normally [name], I'd be giving you props, but you messed with the homie's girl, and you know that crosses a line."

                scene v13s37no_12a
                with dissolve

                imre "So right now you're on my shit list."

                scene v13s37no_12d # FPP. Same as v13s37no_12, Imre walking away, angry, mouth open, showing his middle finger to MC and Nora
                with dissolve

                imre "Fuck you both!"

                scene v13s37no_4
                with dissolve

                u "*Sighs* Fuck..."

                scene v13s37no_4b
                with dissolve

                no "Don't worry about him... He won't say anything and he'll only be mad at you for a few days."

                scene v13s37no_4c
                with dissolve

                no "He'll most likely take all of his anger out on me, but that's nothing new. *Chuckles*"

                scene v13s37no_4d
                with dissolve

                u "I don't know if I like that too much."

                scene v13s37no_4c
                with dissolve

                no "Just leave it be for now, okay?"

                scene v13s37no_4d
                with dissolve

                u "Yeah, if you say so."

                scene v13s37no_8
                with dissolve

                pause

                scene v13s37no_4d
                with dissolve

                u "I'm gonna give you some space."

                scene v13s37no_5
                with dissolve

                pause 0.75

                scene v13s37no_2a
                with dissolve

                no "Thank you for everything... Really, I mean it."

                scene v13s37no_2
                with dissolve

                u "Always."

                scene v13s37no_1a
                with dissolve

                pause 0.75

    call screen v13s37_garden1

label v13s37_chris:
    $ freeroam11.add("chris")

    if chris.relationship <= Relationship.MAD:
        scene v13s37ch_1 # TPP. Show MC walking over to Chris, Chris slightly angry, mouth closed, MC slight smile, mouth closed
        #with dissolve

        pause 0.75

        scene v13s37ch_2 # FPP. MC standing in front of Chris, Chris slightly angry, mouth closed, looking at MC
        with dissolve

        u "Hey Chris."

        scene v13s37ch_2a # FPP. Same as v13s37ch_2, Chris mouth open
        with dissolve

        ch "Hmph... Here to tell me how shitty of a boyfriend I am, and what I need to be doing in my relationship?"

        scene v13s37ch_2
        with dissolve

        u "No, I came to see how you were doing. You seem to be in better spirits."

        scene v13s37ch_2a
        with dissolve

        ch "I'm not really in the talking mood right now to be honest, but I'll say this. Things aren't always as they seem."

        scene v13s37ch_2
        with dissolve

        u "Noted."

        scene v13s37ch_2
        with dissolve

        u "(He's still pissed at me for what I said when we went to the hospital.)"

        scene v13s37ch_3 # TPP. Show MC walking away from Chris, Chris slightly annoyed, mouth closed, MC neutral expression, mouth closed
        with dissolve

        pause 0.75
    
    else:
        if nora.relationship < Relationship.FWB:
            scene v13s37ch_1a # TPP. Same as v13s37ch_1, Chris slightly sad, MC slight smile
            #with dissolve

            pause 0.75

            scene v13s37ch_2b # FPP. Same as v13s37ch_2, Chris slightly sad
            with dissolve

            u "Chilling by yourself, huh?"

            scene v13s37ch_2c # FPP. Same ass v13s37ch_2b, Chris mouth open
            with dissolve

            ch "Nora said she had to make a call. *Sighs* I know she just wanted to step away for a minute."

            scene v13s37ch_2b
            with dissolve

            u "You guys are still slightly smiling and holding each others' hands, one would think things are good between you guys."

            scene v13s37ch_2c
            with dissolve

            ch "Ha, please... I'm doing my best to put on a good show and act like nothings going on, but it's obvious she's lost a lot of confidence in our relationship."

            scene v13s37ch_2b
            with dissolve

            u "So, where do you think that's gonna leave you guys?"

            scene v13s37ch_2c
            with dissolve

            ch "I have no clue, but I'm not too optimistic. I'm just trying to ride this out with a smile on my face."

            scene v13s37ch_2d # FPP. Same as v13s37ch_2c, Chris looking down
            with dissolve

            ch "And what's crazy is that, outside of pushing her, I still don't feel like I did a damn thing wrong. But don't let her hear me say that."

            scene v13s37ch_2b
            with dissolve

            u "Yeah, you guys are viewing things a little differently at the moment."

            scene v13s37ch_2c
            with dissolve

            ch "A little is an understatement. But, I'm gonna play my role right and see if she will too. If not, then I guess we'll be done."

            scene v13s37ch_2b
            with dissolve

            u "I'm sorry to hear that man, I really am."

            scene v13s37ch_2c
            with dissolve

            ch "You don't have to be sorry, it's not like you had anything to do with it."

            scene v13s37ch_2b
            with dissolve

            u "Well yeah, you're right. *Chuckles*"

            scene v13s37ch_2c
            with dissolve

            ch "Mind giving me some time alone?"

            scene v13s37ch_2b
            with dissolve

            u "You got it, man."

            scene v13s37ch_3a # TPP. Same as v13s37ch_3, Chris slightly sad
            with dissolve

            pause 0.75

        else:
            scene v13s37ch_1a 
            #with dissolve

            pause 0.75

            scene v13s37ch_2b
            with dissolve

            u "Chilling by yourself, huh?"

            scene v13s37ch_2c
            with dissolve

            ch "Nora said she had to make a call. *Sighs* I know she just wanted to step away for a minute."

            scene v13s37ch_2b
            with dissolve

            u "You guys are still slightly smiling and holding each others' hands, one would think things are good between you guys."

            scene v13s37ch_2c
            with dissolve

            ch "Ha, please. I'm doing my best to put on a good show and act like nothings going on, but it's obvious she's lost a lot of confidence in our relationship."

            scene v13s37ch_2b
            with dissolve

            u "So where do you think that's gonna leave you guys?"

            scene v13s37ch_2c
            with dissolve

            ch "I have no clue, but I'm not too optimistic. I'm just trying to ride this out with a smile on my face."
            ch "And what's crazy is that outside of pushing her I still don't feel like I did a damn thing wrong. But don't let her hear me say that."

            scene v13s37ch_2e # FPP. Same as v13s27ch_2b, different pose
            with dissolve

            u "Yeah, you guys are viewing things a little differently."

            scene v13s37ch_2f # FPP. Same as v13s37ch_2e, Chris mouth open
            with dissolve

            ch "A little is an understatement. But I'm gonna play my role right and see if she will too. If not, then I guess we'll be done."

            scene v13s37ch_2e
            with dissolve

            u "I'm sorry to hear that man, I really am."

            scene v13s37ch_2f
            with dissolve

            ch "You don't have to be sorry, it's not like you had anything to do with it."

            scene v13s37ch_2e
            with dissolve

            u "Well yeah, you're right. *Chuckles*"

            scene v13s37ch_2f
            with dissolve

            ch "I will say this..."

            scene v13s37ch_2d
            with dissolve

            ch "I've caught her flinching or kind of like, moving away when I touch her."

            scene v13s37ch_2c
            with dissolve

            ch "I don't know, I just... With the way she's been acting, it seems like she's feeling guilty about something."

            scene v13s37ch_2b
            with dissolve

            u "Do you have something specific you're thinking of?"

            scene v13s37ch_2c
            with dissolve

            ch "Yeah, actually... I'm pretty sure her ass cheated on me, ha."

            scene v13s37ch_2b
            with dissolve

            u "Wait... What? What makes you think that?"

            scene v13s37ch_2c
            with dissolve

            ch "Man, when you've been with someone as long as Nora and I have been together, you just know these things."

            scene v13s37ch_2b
            with dissolve

            u "Well, I'm not gonna act like I'm a professional in your relationship and challenge what you believe."

            scene v13s37ch_2e
            with dissolve

            u "Do you have an idea who with or when this switch in her started?"

            scene v13s37ch_2d
            with dissolve

            ch "It was very recent, I can tell. I have no idea who with, but there's not many guys on this trip. Let alone, many she'd be willing to mess with."

            scene v13s37ch_2f
            with dissolve

            ch "'Cause honestly, the only guys she can even tolerate are you and Charli, so it must've been some random dude that she met."

            scene v13s37ch_2d
            with dissolve

            u "(Thought he was actually suspecting me for a second.)"

            scene v13s37ch_2e
            with dissolve

            u "You think she was like, seeking it? Or do you think she made a mistake?"

            scene v13s37ch_2f
            with dissolve

            ch "That's what I don't know and I'm hoping to find out."

            scene v13s37ch_2e
            with dissolve

            u "Shit, man... Well, you and I both."

            scene v13s37ch_2b
            with dissolve

            u "I don't like seeing you like this."

            scene v13s37ch_2g # FPP. Same as v13s37ch_2c, Chris slight smile
            with dissolve

            ch "Well, you can always look away. *Chuckles*"

            scene v13s37ch_2h # FPP. Same as v13s37ch_2g, Chris mouth closed
            with dissolve

            u "*Chuckles* Is that your way of asking for some alone time?"

            scene v13s37ch_2g
            with dissolve

            ch "I think so."

            scene v13s37ch_2h
            with dissolve

            u "I'll leave you to it, keep your chin up."

            scene v13s37ch_3a
            with dissolve

            pause 0.75

    call screen v13s37_garden1

label v13s37_end:
    scene v13s37end_1 # TPP. Show MC walking over to Lindsey, both slight smiles, mouths closed
    #with dissolve

    pause 0.75

    scene v13s37end_2 # FPP. MC standing in front of Lindsey, Lindsey looking at MC, Lindsey slight smile, mouth closed
    with dissolve

    u "How do you think this is going?"

    scene v13s37end_2a # FPP. Same as v13s37end_2, Lindsey mouth open
    with dissolve

    li "You mean this con job? *Chuckles*"

    scene v13s37end_2
    with dissolve

    u "Please, elaborate. *Laughs*"

    scene v13s37end_2b # FPP. Same as v13s37end_2a, Lindsey slightly annoyed
    with dissolve

    li "Chris. Everything he's doing is an attempt to get Nora to forget about the fact that he's just an overall shitty boyfriend."

    scene v13s37end_2c # FPP. Same as v13s37end_2b, different pose
    with dissolve

    li "Being a good boyfriend for two days doesn't make up for months of trash. Like, c'mon now..."

    scene v13s37end_2d # FPP. Same as v13s37end_2b, mouth closed
    with dissolve

    u "Yeah, sometimes things aren't as they seem, though."

    scene v13s37end_2e # FPP. Same as v13s27end_2c, mouth closed
    with dissolve

    u "Maybe he knows he fucked up and is trying to make amends. Have you thought about that?"

    scene v13s37end_2b
    with dissolve

    li "I did, and I realized that in order for that to be true, he would have to think what he's been doing prior to this was wrong. And he doesn't think that."

    scene v13s37end_2d
    with dissolve

    u "I thought I had a good defense, but that was a damn good point."

    scene v13s37end_2a
    with dissolve

    li "Exactly, lawyer Lindsey will be here all day winning arguments. *Chuckles*"

    scene v13s37end_2
    with dissolve

    u "*Chuckles*"

    if cuffs not in mc.inventory:
        scene v13s37end_2a
        with dissolve

        li "Before I forget, did you see that big ferris wheel they have a few blocks from here?"

        scene v13s37end_2
        with dissolve

        u "I didn't see any ferris wheel."

        scene v13s37end_2a
        with dissolve

        li "Well, there's one really close by and I kinda wanna check it out, but I'm not getting up there on that thing without knowing it's safe. *Laughs*"

        scene v13s37end_2
        with dissolve

        u "I wouldn't either, haha. I'll have to look into this ferris wheel and get back to you..."

        scene v13s37end_2a
        with dissolve

        li "You do that. *Chuckles*"

    scene v13s37end_3 # TPP. Show Chris, Nora and Imre walking over to MC and Lindsey, Chris and Nora slightly sad, mouths closed, MC and Lindsey slight smiles, mouths closed, Imre slightly annoyed, mouth closed
    with dissolve

    pause 0.75

    scene v13s37end_4 # FPP. MC, Chris, Nora, Lindsey and Imre in a circle, MC looking at Nora, Nora looking at Lindsey (Only Nora in shot), Nora slight smile, mouth open
    with dissolve

    no "Ms. Rose called Chris and needed some help from him so he dashed off. Lindsey, you wanna walk back with me?"

    scene v13s37end_2f # FPP. Same as v13s37end_2, Lindsey looking at Nora, Lindsey slight smile, mouth open
    with dissolve

    li "Sure, and the boys can stick together."

    scene v13s37end_2a
    with dissolve

    li "Bye boys."

    scene v13s37end_5 # TPP. Show MC and Imre walking away from Nora and Lindsey (they're walking to the opposite direction). Imre slightly annoyed, mouth closed, rest mouth closed slight smiles
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v13_walk_imre