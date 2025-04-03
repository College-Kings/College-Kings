# SCENE 40: Carriage ride
# Location: Carriage, Hotel Lobby, Hotel Corridor
# Characters: MC (Outfit 9), Lindsey (Outfit 1), Chloe (Outfit 2), Nora (Outfit 2), Mr Lee (Outfit 1), Imre (Outfit 1), Charli (Outfit 1), Aubrey (Outfit 2)
# Time: Night

label v11_carriage_ride:
    scene v11car1 # FPP. MC standing in the lobby next to the other students (Charli leaning on the wall, Imre, Lindsey, out of shot), looking at Mr Lee in front of the counter, Mr Lee slight smile, mouth open
    with dissolve
    play music music.ck1.v10.Track_Scene_10 fadein 2
    lee "Settle down, everyone... If you haven't yet heard from your fellow students or myself, we have a planned event tonight. An event that I certainly will enjoy, and I believe you all will as well..."

    scene v11car2 # FPP. Same positioning as v11car1, MC looking at Imre, Imre looking at Mr Lee's direction, Imre slight grin, mouth open
    with dissolve

    imre "Are you gonna make us walk home again this time?"

    scene v11car1a # FPP. Same as v11car1, Mr Lee looking towards Imre, Mr Lee stern face, mouth closed
    with dissolve

    pause 0.75

    scene v11car1
    with dissolve

    lee "Tonight students, we're going on carriage rides."

    scene v11car3 # FPP. Same positioning as v11car1, MC looking at Lindsey, Lindsey looking towards Mr Lee, Lindsey big smile, mouth open
    with dissolve

    li "Really?! Like a princess? With horses??"

    scene v11car1b # FPP. Same as v11car1, Mr Lee looking towards Lindsey, Mr Lee smiling, mouth open
    with dissolve

    lee "Exactly like a princess. *Chuckles* And yes, horses too. You'll be in groups of four, as these are historical carriages that replicate earlier London times."

    lee "Use this opportunity to converse, enjoy the sights, and have fun. Now, if a few of you would please come up and find out what your groups are, we can get started."

    scene v11car3a # FPP. Show Lindsey running towards Mr Lee, she is very excited, mouth closed
    with dissolve

    u "(Haha, gotta admire the enthusiasm.)"

    scene v11car4 # FPP. Same positoning as v11car1, MC looking at Charli who is leaning on the wall, Charli looking at MC, Charli mocking look, mouth closed
    with dissolve

    u "Did you need something?"

    scene v11car4a # FPP. Same as v11car4, Charli mocking look, mouth slightly open
    with dissolve

    charli "*Scoffs*"

    scene v11car4b # FPP. Same as v11car4, Show Lindsey walking towards MC, Charli mocking look, mouth closed, Lindsey smiling, mouth closed
    with dissolve

    pause 1.25

    scene v11car4c # FPP. Same as v11car4, Lindsey standing in front of MC, blocking the view of Charli, she's looking back at Charli, she's slightly worried, mouth closed
    with dissolve

    pause 0.75

    scene v11car4d # FPP. Same as v11car4c, Lindsey looking at MC, she's slightly worried, mouth open
    with dissolve

    li "Hey, everything okay?"

    scene v11car4e # FPP. Same as v11car4d, Lindsey slightly worried, mouth closed
    with dissolve

    u "Yeah, why?"

    scene v11car4f # FPP. Same as v11car4d, Lindsey slight smile, mouth open, different pose
    with dissolve

    li "'Cause you and Charli were just looking at each other like you're rivals or something. *Chuckles*"

    scene v11car4g # FPP. Same as v11car4f, Lindsey slight smile, mouth closed
    with dissolve

    u "Haha, yeah, I'm fine. There may be some bad blood, but I'm not getting hung up over it right now. We have carriages to ride, remember? *Chuckles*"

    scene v11car4h # FPP. Same as v11car4g, Lindsey huge smile, at the top of a jump, mouth closed
    with dissolve

    pause 0.75

    scene v11car4i # FPP. Same as v11car4h, Lindsey huge smile, not jumping anymore, mouth open, different pose
    with dissolve

    li "I KNOW! I'm so fucking excited! Mr. Lee mentioned that we were doing something I'd really enjoy, but I had no idea it was this... We literally had like, one conversation about horses I think."

    li "*Chuckles* I'm pretty sure all I said to him was that I want a horse and carriage at my wedding. I don't know how he remembered that."

    scene v11car4j # FPP. Same as v11car4i, Lindsey huge smile, mouth closed
    with dissolve

    u "Well, some people may not want to admit it but, Mr. Lee is actually a really good professor."

    scene v11car4i
    with dissolve

    li "You're definitely not wrong. Also, I looked at the list and you and I are riding together."

    scene v11car4j
    with dissolve

    u "Oh, perfect. Who else are we with?"

    scene v11car4d
    with dissolve

    li "Well, that's the not so exciting part. We're with Nora..."

    scene v11car4e
    with dissolve

    u "Well, that's not exactly bad. Who else?"

    scene v11car4d
    with dissolve

    li "Chloe."

    scene v11car4e
    with dissolve

    u "Ah... Now I see the problem. *Chuckles*"

    scene v11car4i
    with dissolve

    li "Who knows, though. Maybe nothing bad will happen."

    scene v11car4j
    with dissolve

    u "Hopefully."

    scene v11car1
    with dissolve

    lee "Attention students! There's only two carriages so you'll be taking turns. The first two groups are Lindsey's group and Amber's group."

    scene v11car4i
    with dissolve

    li "Oh, we're first!"

    scene v11car4k # FPP. Same as v11car4j, different pose, Lindsey slightly pouting, mouth closed
    with dissolve

    u "Not gonna lie, I've been out exploring all day, so it'll be nice to relax for a bit. Maybe I'll even take a nap on the ride, haha."

    scene v11car4l # FPP. Same as v11car4k, Lindsey slightly pouting, mouth open
    with dissolve

    li "Come on, [name]. You'll actually miss this whole experience for a nap? Also, if you're sleeping, I'll have to deal with those two all by myself."

    scene v11car4k
    with dissolve

    menu:
        "Tease" (troublemaker=1.0):
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            scene v11car4m # FPP. Same as v11car4l, different pose, Lindsey slightly sad, mouth closed
            with dissolve

            u "I'm sorry Lindsey, I can barely keep my eyes open."

            scene v11car4n # FPP. Same as v11car4m, Lindsey slightly sad, mouth open
            with dissolve

            li "*Sighs* Okay, I understand."

            scene v11car4g
            with dissolve

            u "*Chuckles* Awww, you look so sad! I was just teasing. *Laughs*"

            scene v11car4f
            with dissolve

            li "Oh, haha. Well don't play like that... There's no way I could sit alone on a carriage between those two. *Chuckles*"

            scene v11car4g
            with dissolve

            u "Haha, sorry. Don't worry though, you're not alone. And look, I think Chloe and Nora are ready to go."

        "Relax her":
            scene v11car4g
            with dissolve

            u "Don't worry, I wouldn't do that to you. *Chuckles* That'd be like me having to ride with Charli, Imre and Ryan."

            u "There's no telling what would happen on that ride, but it's most likely not gonna end well."

            scene v11car4f
            with dissolve

            li "Haha, very true. We're stuck in this together. *Chuckles*"

            scene v11car4g
            with dissolve

            u "Oh, hey, it looks like Chloe and Nora are ready."

    scene v11car5 # FPP. MC looks to see Chloe and Nora next to the hotel lobby door, Nora looking bored, Chloe looking at her phone, slight smile, both mouths closed
    with dissolve

    pause 0.75

    scene v11car4i
    with dissolve

    li "C'mon, let's go."

    scene v11car6 # FPP. MC slightly behind Lindsey, they're both exiting the hotel lobby door, Chloe and Nora next to the door, out of shot, Lindsey looking towards Chloe, Lindsey smiling, mouth open
    with dissolve

    li "Let's go guys! You all know how these things work, we only have until midnight. *Laughs* I don't want our ride to transform into a pumpkin and rats."

    scene v11car7 # FPP. Same positioning as v11car6, MC looking at Chloe, she's slightly smiling, mouth slightly open
    with dissolve

    cl "*Chuckles*"

    scene v11car8 # TPP. Show MC getting on the carriage and Lindsey close behind him, both smiling, mouths closed
    with dissolve

    pause 0.75

    scene v11car9 # FPP. MC is in the carriage, sitting, he sees Lindsey climbing in, Lindsey smiling, mouth closed
    with dissolve

    pause 0.75

    scene v11car10 # FPP. MC sees Chloe poking her head in the carriagem she's looking towards Lindsey (Lindsey sitting next to MC), Chloe mouth slightly open, slightly sad
    with dissolve

    cl "*Sighs*"

    scene v11car11 # FPP. Chloe sitting in front of MC, she has a slight smile, mouth closed
    with dissolve

    u "*Whisper* Everything okay?"

    scene v11car11a # FPP. Same as v11car11, Chloe slight smile, mouth open
    with dissolve

    cl "*Whisper* Yeah, I'm fine. Thanks for asking."

    scene v11car9a # FPP. Same cam as v11car9, Chloe sitting in front of MC, slightly annoyed, mouth closed, Nora climbing in, Nora slightly annoyed, mouth closed, both of them looking at each other
    with dissolve

    pause 0.75

    scene v11car12 # FPP. MC looking at Chloe and Nora sitting in the seat in front of him, both girls turned away from each other, slightly annoyed, mouths closed
    with dissolve

    u "(This is really awkward.)"

    scene v11car13 # TPP. Show Mr Lee standing outside the carriage, hands on his mouth as he is screaming, mouth open, smiling
    with dissolve

    lee "Alright, the first cavalry is off!"

    scene v11car12a # FPP. Same as v11car12, Chloe and Nora both startled, mouths closed
    with hpunch

    pause 0.75

    scene v11car14 # FPP. Same positioning as v11car12, MC looking at Nora, she's looking at him, slightly startled, mouth open
    with dissolve

    no "Woah..."

    scene v11car14a # FPP. Same as v11car14, Nora holding her stomach as if she were to be sick, looking at MC, mouth closed
    with dissolve

    u "*Laughs* Made me nervous for a second too."

    scene v11car14b # FPP. Same as v11car14a, Nora mouth open, holding her stomach as if she were to be sick
    with dissolve

    no "I can't stand any kind of ride like this. Horse, carriage, wagon, boat, I don't know what it is but it always makes me sick."

    scene v11car14a
    with dissolve

    u "Like being seasick except... well not on the sea?"

    scene v11car14b
    with dissolve

    no "Something like that, yeah."

    scene v11car14a
    with dissolve

    u "So... I'm pretty sure I've seen all of you during the trip so far, but outside of that, have you guys done anything interesting?"

    scene v11car11b # FPP. Chloe looking at MC, neutral expression, mouth closed
    with dissolve

    cl "..."

    scene v11car14a
    with dissolve

    no "..."

    scene v11car15 # FPP. MC looking at Lindsey who is seated next to him, she's looking at MC, bored expression, mouth closed
    with dissolve

    li "..."

    scene v11car15a # FPP. Same as v11car15, Lindsey slight smile, mouth closed, different pose
    with dissolve

    u "Don't all speak at once. *Chuckles*"

    scene v11car15b # FPP. Same as v11car15a, Lindsey slight smile, mouth open
    with dissolve

    li "Haha, I was just thinking for a sec. I did go to a really nice ice cream place with Aubrey. She eats ice cream like a crazy person. *Chuckles*"

    scene v11car11c # FPP. Same as v11car11, Chloe looking at Lindsey, Chloe slight smile, mouth open
    with dissolve

    cl "How does a crazy person eat ice cream?"

    scene v11car15c # FPP. Same as v11car15a, different pose, Lindsey looking at Chloe, Lindsey mouth open, slight smile
    with dissolve

    li "She bites it, but she bites it with her front teeth. I'd be in so much pain."

    scene v11car15a
    with dissolve

    u "Haha, most people would. That's some high pain tolerance."

    scene v11car15b
    with dissolve

    li "I wish I had that gift."

    scene v11car15a
    with dissolve

    u "You're acting like it's a superpower or something. *Chuckles*"

    scene v11car15b
    with dissolve

    li "It might as well be! I love ice cream, but it always bothers my teeth so I can never eat too much. Do you know how much ice cream I'd eat if it didn't hurt so much?"

    scene v11car14c # FPP. Same as v11car14a, Nora looking at Lindsey, Nora different pose, mouth open, slight smile
    with dissolve

    no "Probably a lot."

    scene v11car15d # FPP. Same as v11car15, Lindsey looking at Nora, Lindsey different pose, mouth open, slight smile
    with dissolve

    li "Exactly, a lot!"

    scene v11car15c
    with dissolve

    li "*Chuckles* Speaking of gifts, that reminds me that there's something I wanted to bring up with you Chloe, cause you'd make the final call."

    scene v11car15d
    with dissolve

    li "But it'd be good for you to hear this too Nora. I already spoke to Aubrey and she loved my idea."

    scene v11car11c
    with dissolve

    cl "Like an idea for the Chicks?"

    scene v11car15c
    with dissolve

    li "Yeah, for the Chicks."

    scene v11car11d # FPP. Same as v11car11c, different pose, Chloe slightly surprised, mouth open
    with dissolve

    cl "Oh, okay."

    scene v11car12b # FPP. Same as v11car12, Nora and Chloe looking at Lindsey, both slightly smiling, mouths closed, they're very interested
    with dissolve

    pause 0.75

    scene v11car15a
    with dissolve

    u "Guess I'll just talk to myself over here in the meantime..."

    scene v11car15b
    with dissolve

    li "Haha, you can tell me what you think too."

    scene v11car15c
    with dissolve

    li "Okay, so as you two know, when we're recruited into the Chicks we're told that though we are sisters, and always have this in common, we still must celebrate our individual differences."

    scene v11car15d
    with dissolve

    li "I want to take that belief and go deeper. I studied a bit with Ms. Rose, who come to find out, was also in a sorority during college, and she said they all had nicknames."

    scene v11car14c
    with dissolve

    no "What kind of nicknames?"

    scene v11car15d
    with dissolve

    li "The nicknames are based upon your personality, things you do, etc. And you don't get to choose your nickname, your sisters come up with ideas and they vote on a name for you."

    scene v11car15b
    with dissolve

    li "I spoke to some of the frat heads too and they think it'd be a fun idea for the guys as well."

    li "It's a good way to not only see how your brothers or sisters feel about you, but it also adds that element of individuality. You know what I mean?"

    scene v11car14d # FPP. Same as v11car14c, different pose
    with dissolve

    no "I know I'm not one to get super excited or anything, but I have to be honest... I really like that idea. I can already think of a few names for some of the girls. *Chuckles*"

    scene v11car15e # FPP. Same as v11car15d, different pose
    with dissolve

    li "Haha, me too."

    scene v11car15f # FPP. Same as v11car15c, different pose
    with dissolve

    li "What do you think, Chloe?"

    scene v11car11e # FPP. Same as v11car11d, Chloe slightly skeptical, mouth open, different pose
    with dissolve

    cl "I... I don't know."

    scene v11car14e # FPP. Same as v11car14d, Nora looking at Chloe, Nora angry, mouth open
    with dissolve

    no "What do you mean \"you don't know\"? It's not complicated at all. It's a good way for us to bond with each other, and very easy to implement."

    scene v11car11f # FPP. Same as v11car11e, Chloe looking at Nora, Chloe slightly skeptical, mouth open
    with dissolve

    cl "I mean... I don't know, have the Chicks ever done this sort of thing before?"

    scene v11car15c
    with dissolve

    li "They have, actually, I guess I should've led with the fact that this wasn't exactly an original idea, but instead a discovered tradition."

    li "They've been doing this since the beginning of the Chicks, but one year a President didn't give the pledges any nicknames and after a few years of that, the whole thing disappeared."

    scene v11car11e
    with dissolve

    cl "Well I'm sure there's a good reason the President didn't continue it."

    scene v11car14e
    with dissolve

    no "Yeah, it's called being a lazy President."

    scene v11car11g # FPP. Same as v11car11f, Chloe annoyed, mouth open, different pose
    with dissolve

    cl "Are you trying to say something?"

    scene v11car14f # FPP. Same as v11car14e, Nora mouth open, angry, arms folded, different pose
    with dissolve

    no "I'm not trying, I am. It's a great idea, and the only reason it went away and never got brought back was because of the poor choices of one President."

    scene v11car11g
    with dissolve

    cl "Ever thought about the tension a poorly chosen nickname could cause? The bullying that could lead to? I guess you wouldn't care, it's not like you give a fuck about other people's happiness."

    scene v11car12c # FPP. Same as v11car12, Nora and Chloe looking at each other, Nora angry, mouth closed, arms folded, Chloe angry, mouth closed
    with dissolve

    menu:
        "Side with Nora" (nora=1.0, chloe=1.0):
            $ nora.points += 1
            $ chloe.points -= 1

            scene v11car11h # FPP. Same as v11car11, Chloe annoyed, mouth closed, looking at MC, different pose
            with dissolve

            u "I actually think it's really cool, too. I'm sure the benefits would outweigh the negatives. I already have nicknames for some of my frat bros in mind... *Chuckles*"

        "Side with Chloe" (nora=-1.0, chloe=1.0):
            $ nora.points -= 1
            $ chloe.points += 1

            scene v11car14g # FPP. Same as v11car14, Nora annoyed, mouth closed, looking at MC, different pose
            with dissolve

            u "Look, the idea sounds good, but I do see the tension it could cause and you guys certainly have enough of that. I think it's best to keep things as is."

            scene v11car14h # FPP. Same as v11car14g, Nora annoyed, mouth open
            with dissolve

            no "Yeah sure, but you can't just turn the idea down right away when one of your sisters is coming to you with something that could be really awesome."

    scene v11car15g # FPP. Same as v11car15e, Lindsey slightly worried, mouth open, different pose
    with dissolve

    li "Guys, I wasn't trying to start something. I just thought everyone would like it and it'd be something neat for us to talk about."

    scene v11car14i # FPP. Same as v11car14d, Nora annoyed, mouth open, different pose
    with dissolve

    no "That's what I first thought when you brought it up, but obviously not everyone is open to new suggestions."

    scene v11car11g
    with dissolve

    cl "Don't be mad at me for being skeptical... Someone has to and it's my job to make sure our sorority is taken care of."

    scene v11car14f
    with dissolve

    no "It's your job to do a lot of things that you don't do."

    scene v11car11g
    with dissolve

    cl "Oh really? Like what?"

    scene v11car14e
    with dissolve

    no "Do I really need to read from the list?"
    no "One thing I can say about Chris is that even though he's so fucking busy and never has time for me, the dedication he has for the Wolves is clearly seen in every single thing he does..."

    scene v11car14f
    with dissolve

    no "As President, you could've at least told her it was great that she tried to improve the sorority, before you completely rejected the idea..."

    scene v11car15g
    with dissolve

    li "Guys, I-"

    scene v11car11i # FPP. Same as v11car11c, Chloe annoyed, mouth open
    with dissolve

    cl "Lindsey, you're fine. This has nothing to do with your idea. Clearly Nora has been itching to get these things off her chest for a while."

    scene v11car11j # FPP. Same as v11car11g, different pose
    with dissolve

    cl "So go ahead Nora, what's the big picture?"

    scene v11car14e
    with dissolve

    no "You don't want to do this right now, okay?"

    scene v11car11j
    with dissolve

    cl "I don't see why not. We're gonna be here for a while."

    scene v11car12c
    with dissolve

    u "(For fucks sake, here we go.)"

    scene v11car14e
    with dissolve

    no "Fine Chloe, if you want to know so bad. YOU'RE A HORRIBLE PRESIDENT! The only reason you were picked was because you're a pretty blonde with nice tits and a big ass."

    scene v11car14f
    with dissolve

    no "You know the last President only cared about what the Chicks looked like. Will guys think we're hot, will we be good enough for parties, etc."

    scene v11car14e
    with dissolve

    no "You were the perfect poster child, and you never should've been chosen. Everything the Chicks stand for, or are supposed to stand for, just isn't true with us. Because you don't lead."

    scene v11car11g
    with dissolve

    cl "You really believe all that?"

    scene v11car14f
    with dissolve

    no "I said it, didn't I?"

    scene v11car11g
    with dissolve

    cl "You know, I bust my ass for the Chicks, I keep the girls happy, I keep us out of trouble, I shut down conflicts between girls... And what do I get???"

    scene v11car11j
    with dissolve

    cl "Your horrible, backstabbing and truly hurtful comments that undermine every fucking thing I do!"

    cl "You're the reason we're stagnating, because I can't even think about leading a sorority if you constantly try to rally the girls against me and I have to spend my time fighting stupid accusations!"

    scene v11car11g
    with dissolve

    cl "How do you not understand that?"

    scene v11car14e
    with dissolve

    no "Don't you fucking put this on me! Lindsey's literally right here in front of you trying to help you grow the sorority and you're blocking the sunlight for her."

    scene v11car14f
    with dissolve

    no "You only cared about the way you as President looked from day one. It was never about the Chicks!"

    scene v11car12c
    with dissolve

    cl "..."

    scene v11car14g
    with dissolve

    u "Oh, hey! Did you guys know there's a statue at the museum Mr. Lee took us to that was sculpted by his ex, and is actually the resemblance of the guy she cheated on him with?"

    scene v11car11h
    with dissolve

    u "Not only that, but Mr. Lee is the one that submitted it to the museum. *Chuckles*"

    scene v11car11k # FPP. Same as v11car11h, Chloe mouth open, annoyed
    with dissolve

    cl "[name]... Thanks for trying to change the subject, but I'm glad this is finally being addressed."

    scene v11car11j
    with dissolve

    cl "I have been taking the fall for everything bad the Chicks are being accused of since the day I became President, you really think I'm the one that posted that picture of Sarah to embarrass her?"

    cl "That I'm the one that sabotaged the Deers car washing event cause they were earning more than us???"

    scene v11car11g
    with dissolve

    cl "Fuck no, I took the fall for everything, because some Chick fucks up and I'm not gonna let them ruin their college life over one mistake. I can take the hit, cause that's what I always do."

    scene v11car11j
    with dissolve

    cl "If you really think that I'm doing all this shit for myself, you really don't know me at all."

    scene v11car14f
    with dissolve

    no "Sure Chloe, you're a fucking hero! And all those times you had us spend money we didn't have on throwing a party so you could get back with Grayson?"

    scene v11car14e
    with dissolve

    no "What about the time you told a Chick to leave campus cause she was wearing the same dress as you?!"

    scene v11car11j
    with dissolve

    cl "I'm not the only one that makes mistakes, Nora... Let's not pretend like I'm the only one here that people are upset with from time to time."

    scene v11car14e
    with dissolve

    no "It doesn't matter what people think about me, I'm not the President! How you treat your sisters is part of your job. I just want a President that's not just there for the fucking attention!"

    scene v11car11g
    with dissolve

    cl "Fuck off, Nora. All you do is stir shit, and then act like you don't fucking enjoy the drama you're causing! Guess what? I'm not the one that picked this fight."

    scene v11car11j
    with dissolve

    cl "I'm not the one that's been in a toxic relationship for over a year, you're the fucking common denominator. Take some responsibility."

    scene v11car11l # FPP. Same as v11car11, Chloe looking away from everybody, towards the window, mouth slightly open, angry, different pose
    with dissolve

    cl "*Whisper* Probably need some dick since Chris hasn't given you any lately."

    scene v11car14e
    with dissolve

    no "What'd you just say?"

    scene v11car11l
    with dissolve

    cl "I'm not repeating myself."

    scene v11car14f
    with dissolve

    no "You're gonna fuck around and say the wrong thing to me one day and end up getting your ass beat."

    scene v11car11j
    with dissolve

    cl "Ready when you are, bitch."

    scene v11car12c
    with dissolve

    pause 0.75

    scene v11car12a
    with hpunch

    pause 0.75

    scene v11car12d # FPP. Same as v11car12c, Nora and Chloe looking at MC, both angry, mouths closed
    with dissolve

    u "And look at that, we're back! Wasn't that fun?"

    scene v11car16 # TPP. Show Nora and Chloe trying to get out of the carriage at the same time, Nora mouth open, angry, Chloe angry mouth closed
    with dissolve

    no "Can you not fucking wait? Oh my god."

    scene v11car17 # TPP. Show Nora and Chloe falling out towards the ground
    with dissolve

    pause 0.75
    play sound sound.fall

    scene v11car18 # TPP. Show Nora and Chloe on the ground, both angry, mouths closed
    with vpunch

    # -Both Nora and Chloe fall out of the carriage onto the ground-

    cl "*Grunts*"

    scene v11car18a # TPP. Same as v11car18, Nora and Chloe different pose
    with dissolve

    no "*Grunts*"

    scene v11car19 # FPP. MC out of the carriage, he sees Mr Lee walking towards them, Mr Lee concerned, mouth closed
    with dissolve

    pause 0.75

    scene v11car19a # FPP. Same as v11car19, Mr Lee now in talking distance, Mr Lee concerned and worried, mouth open, looking down at Nora and Chloe (they're out of shot)
    with dissolve

    lee "What's going on? Are you two alright?"

    scene v11car19b # FPP. Same as v11car19a, Mr Lee eyebrow raised, skeptical expression, mouth closed, looking at MC
    with dissolve

    u "They were just so excited to be back they tried running and fell, can you believe that? *Chuckles nervously*"

    scene v11car19c # FPP. Same as v11car19b, Mr Lee mouth open, eyebrow raised, skeptical expression
    with dissolve

    lee "...Hardly."

    scene v11car18b # TPP. Show Nora and Chloe getting up, both angry, mouths closed
    with dissolve

    pause 0.75

    scene v11car20 # TPP. Show Nora and Chloe walking towards the hotel lobby, show MC and Lindsey going towards hotel lobby too, but relatively behind Nora and Chloe, Nora and Chloe angry, Lindsey and MC worried, everyone mouths closed
    with dissolve

    pause 0.75

    scene v11car21 # TPP. Show MC and Lindsey walking through the hotel lobby door, camera is behind them, show Aubrey walking up towards them
    with dissolve

    pause 0.75

    scene v11car22 # FPP. MC and Lindsey standing next to each other in the lobby (Lindsey out of shot), Aubrey in front of them, looking at MC, Aubrey mouth open, pointing her thumb behind her towards the elevator, confused expression
    with dissolve

    au "What was all that about?"

    scene v11car23 # FPP. Same positioning as v11car22, MC and Lindsey looking at each other, Lindsey slight smile, mouth closed
    with dissolve

    u "I'll see you tomorrow, alright Lindsey?"

    scene v11car23a # FPP. Same as v11car23, Lindsey mouth open, slight smile
    with dissolve

    li "Alright, thanks again."

    scene v11car23
    with dissolve

    u "Of course."

    scene v11car24 # TPP. Show Lindsey walking away, MC and Aubrey standing in front of each other in the background, everyone slightly smiling, mouths closed (Lindsey and MC same positioning as v11car22)
    with dissolve

    pause 0.75

    scene v11car22a # FPP. Same as v11car22, Aubrey looking at MC, Aubrey concerned, mouth closed
    with dissolve

    u "They were going at each other pretty bad on the ride."

    scene v11car22b # FPP. Same as v11car22a, Aubrey concerned, mouth open
    with dissolve

    au "*Sighs* This is starting to get ridiculous."

    scene v11car22a
    with dissolve

    u "I'll be honest, I thought it was all personal, but it seemed pretty clear that a lot of it stems from Chicks related issues as well."

    scene v11car22b
    with dissolve

    au "It all does, and I'm not trying to put up with it, even as VP. We need to do something."

    scene v11car22a
    with dissolve

    menu:
        "Tell her about Lindsey" (troublemaker=1.0):
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            $ v11_told_aubrey = True

            scene v11car22c # FPP. Same as v11car22a, different pose, Aubrey curious, mouth closed
            with dissolve

            u "Look, you're right. Someone needs to do something and someone is."

            scene v11car22d # FPP. Same as v11car22c, Aubrey curious, mouth open
            with dissolve

            au "Who?"

            scene v11car22c
            with dissolve

            u "She hasn't announced it yet but Lindsey is going to run for President."

            scene v11car22d
            with dissolve

            au "I've noticed that she's been getting more involved, but I didn't know why. Her ideas and everything... Now it all makes sense."

            scene v11car22a
            with dissolve

            u "Yeah. She has some great ideas, Aubrey."

            scene v11car22b
            with dissolve

            au "Well, you know... I have to tell Chloe."

            scene v11car22a
            with dissolve

            menu:
                "I know":
                    scene v11car22e # FPP. Same as v11car22c, different pose, Aubrey slight smile, mouth closed
                    with dissolve

                    u "I know, I can't expect you to keep this from her. Besides, she needs to know anyway."

                    scene v11car22f # FPP. Same as v11car22e, Aubrey slight smile, mouth open
                    with dissolve

                    au "I'm glad you understand that. Thanks [name]."

                    scene v11car22e
                    with dissolve

                    u "Of course, have a good night."

                    scene v11car22f
                    with dissolve

                    au "You too."

                    scene v11car25 # TPP. Show Aubrey walking away and MC standing in the lobby, Aubrey slightly concerned, mouth closed, MC slightly worried, mouth closed
                    with dissolve

                    pause 0.75

                "Don't":
                    scene v11car22g # FPP. Same as v11car22a, different pose
                    with dissolve

                    u "I don't think you should tell her, it could cause some real issues between her and Lindsey. Can't it wait until Lindsey announces that she's running?"

                    scene v11car22h # FPP. Same as v11car22g, Aubrey concerned, mouth open
                    with dissolve

                    au "She deserves to know now so she can prepare. Lindsey shouldn't be able to make moves in secret."

                    scene v11car22g
                    with dissolve

                    u "Yeah, I guess you're right. I just don't want any more drama between you guys."

                    scene v11car22f
                    with dissolve

                    au "Well, we'll see. Thanks for telling me. I'm headed to my room. Goodnight."

                    scene v11car22e
                    with dissolve

                    u "Goodnight."

                    scene v11car25
                    with dissolve

                    pause 0.75

        "Don't tell her about Lindsey":
            scene v11car22g
            with dissolve

            u "Yeah, hopefully a miracle will happen, you know?"

            scene v11car22h
            with dissolve

            au "If only... Well, thanks for telling me what was going on. It's less stressful when you're actually in the loop."

            scene v11car22f
            with dissolve

            au "*Chuckles* I'm gonna head to my room. Goodnight."

            scene v11car22e
            with dissolve

            u "Yeah, of course. Goodnight."

            scene v11car25
            with dissolve

            pause 0.75

    scene v11car26 # TPP. Show MC walking in the hotel lobby, slightly concerned, mouth closed
    with dissolve

    pause 0.75

    scene v11car27 # TPP. Show MC in the hotel room corridor walking, mouth closed, slightly concerned
    with dissolve

    pause 0.75
    stop music fadeout 3
    if v11_riley_roomate:
        jump v11_riley_amber_smoking

    else:
        jump v11_chloe_bathroom
