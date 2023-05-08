# SCENE 37: Walk with Imre and Ryan/Ride with Mr. Lee
# Location: Road
# Characters: MC (Outfit 9), Imre (Outfit 1), Ryan (Outfit 1), Mr. Lee (Outfit 1)
# Time: Morning

label v11_walk_or_ride:
    play music "music/v10/Track Scene 17_1.mp3" fadein 2
    menu:
        "Ride with Mr. Lee":
            $ v11_ride_with_mrlee = True

            scene v11wap11 # TPP. Show MC running towards Mr. Lee, MC screaming, mouth open, slightly worried
            with dissolve

            u "Mr. Lee, wait up!"

            jump v11_ride_with_mrlee

        "Stay with Imre and Ryan":
            u "(*Sighs* This is some bullshit.)"

            jump v11_imre_and_ryan

label v11_ride_with_mrlee:
    scene v11wir1 # TPP Show MC running toward Mr. Lee. Mr. Lee is approaching his car.
    with dissolve

    pause 0.75

    scene v11wir2 # FPP Show Mr. Lee, standing outside, annoyed or dissapointed expression, mouth closed
    with dissolve

    u "You're just going to leave them out here?"

    scene v11wir2a # FPP Same angle as v11wir2, Mr. Lee with dissapointed expression, mouth open
    with dissolve

    lee "Why not? They're grown men and have made it clear that they have no interest in doing anything I suggest, so I'll just excuse myself. Did you not want to stay with them?"

    scene v11wir2
    with dissolve

    u "I'd rather not listen to them fight all the way back to the hotel."

    scene v11wir2a
    with dissolve

    lee "*Sighs* I guess you're a little bit more mature than your friends. Either that or you just wanted a ride."

    scene v11wir2
    with dissolve

    u "*Laughs* A little bit of both."

    scene v11wir2a
    with dissolve

    lee "I appreciate the honesty. I have a question if you'll indulge me."

    scene v11wir2
    with dissolve

    u "Sure."

    scene v11wir2b # FPP Same angle as v11wir2, Mr. Lee with curious expression, mouth open
    with dissolve

    lee "If I was to ask which of those two boys you felt you had more in common with, who would you say?"

    scene v11wir2c # FPP Same angle as v11wir2, Mr. Lee with curious expression, mouth closed
    with dissolve

    menu:
        "Imre":
            u "I'd probably say Imre."

        "Ryan":
            u "I'd probably say Ryan."

    scene v11wir2b # FPP Same angle as v11wir2, Mr. Lee with neutral expression, mouth open
    with dissolve

    lee "I ask you that question because both of those boys have their personalities written on their forehead."
    lee "Imre clearly speaks his mind without much care, he's loyal to a fault, but can't tolerate being betrayed or disrespected. Though at times even he betrays or disrespects others."

    scene v11wir2d # FPP Same angle as v11wir2, Mr. Lee with neutral expression, mouth closed
    with dissolve

    u "(Does he know something about Imre that I don't?)"
    u "What about Ryan?"

    scene v11wir2b
    with dissolve

    lee "Ryan is more complicated, yet still clear enough. He is a reactor rather than an actor such as Imre is. Ryan doesn't tell the world how to move."
    lee "He watches the world move and then decides what he'll do. Look at them right now."

    scene v11wir2d
    with dissolve

    scene v11wir2b
    with dissolve

    lee "Ask yourself, if Imre had never said a word during the multiple times they went at it, would they have gone at it at all?"

    scene v11wir2d
    with dissolve

    u "No, probably not. Are you trying to say it's all Imre's fault?"

    scene v11wir2b
    with dissolve

    lee "Not at all. If I'm punching near your face and you put your head directly in the path of one of my blows then that's your fault."
    lee "Ryan lets Imre bother him. He could easily \"be the better man\" and walk away, but he doesn't because they act like children."

    scene v11wir3 # TPP Show Mr. Lee and MC getting into the car
    with dissolve

    pause 0.75

    scene v11wir4 # FPP Show Mr. Lee driving car, looking forward, neutral expression, mouth open
    with dissolve

    lee "[name], do you know what it means to be a man and act as an adult?"

    scene v11wir4a # FPP Same angle as v11wir4, Mr. Lee with neutral expression, mouth closed
    with dissolve

    menu:
        "Having responsibility":
            u "Well, those that have responsibilities don't have a choice but to act like an adult so I guess having responsibility."

        "Acting mature":
            u "Well, to be either of those you have to act mature."

    scene v11wir4
    with dissolve

    lee "To be a man, to be an adult, it's imperative that we are aware of our position and act accordingly. If you are a husband, father, and employee then you must be aware of that and act accordingly."

    scene v11wir4b # FPP Same angle as v11wir4, Mr. Lee looking toward MC with neutral expression, mouth open
    with dissolve

    lee "You and all of your friends are students that are under mine and Ms. Rose's care."

    scene v11wir4
    with dissolve

    lee "So to act accordingly means to behave as if you were at school and follow any appropriate and reasonable instructions we give. Your two friends back there don't understand that."

    scene v11wir4a
    with dissolve

    u "Yeah, it was getting pretty hard to handle them."

    scene v11wir4
    with dissolve

    lee "That would be an understatement. Maybe being forced to work together on finding a way home will help them with their issues."
    lee "This is exactly why I despise modern day Greek culture. It destroys morality in place of loyalty."

    scene v11wir4a
    with dissolve

    u "Were you in a fraternity?"

    scene v11wir4
    with dissolve

    lee "I was, and proud to be. It was nothing like the fraternities we have today. If I had a say in how things were run at our school, it would be quite different."

    scene v11wir4a
    with dissolve

    u "(Good thing you don't have a say.)"

    scene v11wir4b
    with dissolve

    lee "Honestly, what do you get out of being in a fraternity?"

    scene v11wir4a
    with dissolve

    u "You mean me, personally?"

    scene v11wir4
    with dissolve

    lee "Yes, you. What do you get out of it? As a matter of fact, I asked Imre this same question before he pledged to the Wolves and I wasn't too happy with his answer."

    scene v11wir4a
    with dissolve

    u "What he'd say?"

    scene v11wir4
    with dissolve

    lee "That's neither here nor there, but I'll tell you this, if you say anything about girls being your reason I'll let you out to walk the rest of the way right now."

    scene v11wir4a
    with dissolve

    u "*Laughs*"

    menu:
        "Brotherhood":
            u "I enjoy the brotherhood, really. At the end of the day I know they all have my back."

        "Excitement":
            u "Well honestly, I enjoy the excitement. At first I wasn't sure if I wanted to join a frat, but I'm glad I did."
            u "You never know what to expect and regardless of what crazy things may happen, at least you can never say you're bored. *Chuckles*"

    scene v11wir4
    with dissolve

    lee "Well, that's definitely a better answer than I've been given before."

    scene v11wir4a
    with dissolve

    u "Mr. Lee, I have to ask. Why does this whole thing matter to you so much that you were willing to drag us all the way out here just to smooth things over?"
    u "Any other teacher would've just separated, disciplined, and called it a day."

    scene v11wir4
    with dissolve

    lee "*Sighs* As I was trying to explain earlier, I see much of my younger self in the situations that you students experience."
    lee "If I'm able to help one of you or all of you, that makes it worth it. But I'm not going to babysit anyone. Instead, I'll give you all clarity and a fair shot."

    scene v11wir4b
    with dissolve

    lee "It may not sound like much when I put it that way, but most never even get that."

    scene v11wir4a
    with dissolve

    u "No I get it, that's actually really cool of you. I really respect that."

    scene v11wir4
    with dissolve

    lee "Let me tell you something [name], in our lives we make mistakes, and we also make choices that in our opinion aren't mistakes, but others are hurt by them."

    scene v11wir4b
    with dissolve

    lee "Listen closely to what I'm about to say."

    scene v11wir4
    with dissolve

    lee "Don't regret the decisions you've made up to this point in your life. Own your decisions and remember that the world will go on regardless of what you do."
    lee "So enjoy your life. Walking around regretting the past will just ruin your future. The past is the past, the future is the future, but right here, right now... this is a gift."

    scene v11wir4c # FPP Same angle as v11wir4, Mr. Lee looking forward with small smile, mouth open
    with dissolve

    lee "That's why it's called the present. Don't let others ruin your present. Do you understand what I'm saying?"

    scene v11wir4a
    with dissolve

    u "(Does he know everything that's going on?)"
    u "Pretty sure that's exactly what I needed to hear Mr. Lee. I've been going through a lot lately and some self reflecting has been a part of it."

    scene v11wir4
    with dissolve

    lee "I know [name], I know."

    scene v11wir4a
    with dissolve

    u "Wait, you know about... everything?"

    scene v11wir4
    with dissolve

    lee "Let me clarify... I don't know exactly what's going on, but you're my student. If I didn't notice a change in your behavior or interactions with other students I'd be a poor professor."
    lee "I've noticed some of your conversations with one particular student and I've seen you acting a bit unlike yourself lately. Just live your life, okay? A mature, responsible life, but your life."

    scene v11wir4a
    with dissolve

    u "Yeah, for sure. Um, thank you Mr. Lee, really."

    scene v11wir4c
    with dissolve

    lee "Thank you for actually listening. Being in teaching for years really helps you learn to know if people are actually listening to you or not."
    lee "We're pulling up to the hotel, I'll let you enjoy the rest of your day. We do have a group event tonight, just so you know."

    scene v11wir4a
    with dissolve

    u "Cool, thanks again Mr. Lee."

    scene v11wir5 # TPP Show MC and Mr. Lee walking into the hotel lobby
    with fade

    pause 0.75

    scene v11wir6 # FPP Show Mr. Lee walking away from MC down the hall, away from the lobby
    with dissolve

    u "(I really respect that guy.)"

    jump v11_amber_bar

label v11_imre_and_ryan:
    scene v11wir1a # TPP Same angle as v11wir1, show Mr. Lee walking to his car
    with dissolve

    pause 0.75

    scene v11wir7 # FPP Show Imre and Ryan glaring at each other, both angry with mouths closed
    with dissolve

    u "Honestly, I can't be mad at him for this. What is wrong with you guys? That was fucking embarrassing."
    u "You do realize he's going to get back to the hotel alone and people are going to be asking him where we are? What's he going to say, that we all went out for coffee?"

    scene v11wir7a # FPP Same angle as v11wir7a, Ryan looking at MC with mouth open
    with dissolve

    ry "Bro, relax. I already said I'm sorry that you got dragged into this mess. We just need to get back before Mr. Lee does or come up with a story explaining where we've been."

    scene v11wir7b # FPP Same angle as v11wir7, Ryan and Imre looking at each other, angry, Imre's mouth open
    with dissolve

    imre "Why don't you take responsibility? This is your fault."

    scene v11wir7c # FPP Same angle as v11wir7, Ryan and Imre looking at each other, angry, Ryan's mouth open
    with dissolve

    ry "How is it my fault?"

    scene v11wir7b
    with dissolve

    imre "Like I said before, if you didn't talk shit about me, we wouldn't have any issues outside of the fact that you're an Ape."

    if mc.frat == Frat.APES:
        scene v11wir7
        with dissolve

        u "I'm an Ape too."

        scene v11wir7d # FPP Same angle as v11wir7, Imre looking at MC, angry with mouth open
        with dissolve

        imre "That's another problem, for another time."

    scene v11wir7c
    with dissolve

    ry "I WASN'T MAKING FUN OF YOU! YOUR DUMB ASS DOESN'T EVEN KNOW WHAT THE FUCK GRAYSON SAID, DO YOU?"

    scene v11wir7b
    with dissolve

    imre "I don't need to know what he said, I know he was talking about me and you thought the shit was funny, end of story."

    scene v11wir7c
    with dissolve

    ry "I swear you Wolves are fucking idiots."

    if mc.frat == Frat.WOLVES:
        scene v11wir7
        with dissolve

        u "Bro, chill with the frat insults."

        scene v11wir7a
        with dissolve

        ry "Sorry, but he's pissing me off."

    scene v11wir7b
    with dissolve

    imre "If it wasn't anything bad and I'm acting crazy then tell me what he said."

    scene v11wir7c
    with dissolve

    ry "I don't have to tell you what he said."

    scene v11wir7b
    with dissolve

    imre "No, you really do. If he didn't say anything bad about me and you weren't a part of the joke or whatever it was, I'll apologize and this will all be over."

    scene v11wir7c
    with dissolve

    ry "I don't even remember."

    scene v11wir7
    with dissolve

    menu:
        "Side with Imre":
            if mc.frat == Frat.WOLVES:
                $ reputation.add_point(RepComponent.BRO)

            u "Ryan, really? You remember what he said."

        "Side with Ryan":
            if mc.frat == Frat.APES:
                $ reputation.add_point(RepComponent.BRO)

            u "If he doesn't even remember it must not have been that serious."

            scene v11wir7d
            with dissolve

            imre "What? You can't start believing his bullshit too. What did Grayson say, Ryan?"

    scene v11wir7e # FPP Same angle as v11wir7, Ryan and Imre looking at each other, Ryan with neutral expression, mouth open
    with dissolve

    ry "*Sighs* Fine. Grayson said, and I'm quoting him, these are his words not mine. \"Imre is a sorry ass fighter just like his brother was. I'd be surprised if he makes it thirty seconds."
    ry "The only time he works hard is if there's pussy involved.\" It was at that point that I laughed."

    scene v11wir7f # FPP Same angle as v11wir7, Imre and Ryan looking at each other, Imre angry, Ryan neutral, both mouths closed
    with dissolve

    u "So you didn't even say anything?"

    scene v11wir7a
    with dissolve

    ry "No, that's what I've been saying this whole time."

    scene v11wir7b
    with dissolve

    imre "Well you should have, I knew you guys were talking about my brother and that's what really pissed me off. You should've said something to Grayson or at least not laughed."

    scene v11wir7e
    with dissolve

    ry "You, your brother, and Grayson-all of that is none of my business. That obviously wasn't the reason I laughed."

    scene v11wir7b
    with dissolve

    imre "You shouldn't have laughed at all. You should've either said something about him talking shit or stayed quiet."

    scene v11wir7c
    with dissolve

    ry "Okay bitch, what now? It's done and over with so what now?"

    scene v11wir7
    with dissolve

    u "Can we figure out how we're gonna get back to the hotel?"

    scene v11wir7a
    with dissolve

    ry "What? Bro, just call a rideshare."

    scene v11wir7c
    with dissolve

    ry "Now, like I said, what now Imre? What do you want?"

    scene v11wir7b
    with dissolve

    imre "I want you to apologize."

    scene v11wir7c
    with dissolve

    ry "*Scoffs* I barely apologize when I actually do something wrong, and I'm definitely not when I didn't do shit."

    scene v11wir7b
    with dissolve

    imre "Then we still have a problem."

    scene v11wir7c
    with dissolve

    ry "So be it. I'll tell you this though, keep coming at me and making your little side comments, and I'm gonna put an end to it real fast."

    scene v11wir7b
    with dissolve

    imre "Just say when, I'm always ready."

    scene v11wir7c
    with dissolve

    ry "Just like you were ready when Adam beat your ass? Hmph, please."

    scene v11wir8 # FPP Show Imre squarring up to Ryan like he is going to fight him, both are angry, Imre's mouth open
    with dissolve

    imre "You'll find out, motherfu-"

    scene v11wir8a # FPP Same angle as v11wir8, Imre and Ryan both angry with mouths closed
    with dissolve

    u "Can you guys chill the fuck out for two seconds!? Some of us want to go back to the hotel."
    u "Kinda didn't want to be dragged here in the first place and definitely didn't want to be left with you two arguing."

    scene v11wir7c
    with dissolve

    ry "I'll get an Uber."

    scene v11wir9 # FPP Show Ryan turning around and looking down at his phone
    with dissolve

    pause 0.75

    scene v11wir10 # FPP Show Imre with angry expression, mouth closed
    with dissolve

    u "Seems to me like this really has more to do with your brother than Ryan."

    scene v11wir10a # FPP Same angle as v11wir10, Imre with angry expression, mouth open
    with dissolve

    imre "No, it has to do with them all talking shit about my brother and Ryan not being able to own up to it."
    imre "He was doing a whole lot of talking at the warehouse to have only laughed at that one part. He's a liar."

    scene v11wir10
    with dissolve

    u "Can't you just let it go?"

    scene v11wir10a
    with dissolve

    imre "I'm not letting anything go."

    scene v11wir7c
    with dissolve

    ry "If you're done talking shit, the Uber will be here in like two minutes. There was one nearby."

    scene v11wir7
    with dissolve

    u "Good."

    scene v11wir11 # TPP Show MC, Ryan, and Imre standing by the road, all angry, not looking at each other, MC between Imre and Ryan
    with dissolve

    pause 0.75

    scene v11wir11a # TPP Same angle as v11wir11a, Ryan and Imre giving each other dirty looks, MC looking down and looking frustrated
    with dissolve

    pause 0.75

    scene v11wir12 # FPP Show rideshare arriving
    with dissolve

    pause 0.75

    scene v11wir13 # TPP Show Ryan rushing to the passenger door of the ride share, angry expression, mouth open, while MC and Imre are left standing by the back doors
    with dissolve

    ry "You can sit in the back with the cry baby."

    scene v11wir14 # FPP Show Ryan getting into the front passenger seat of the ride share
    with dissolve

    u "(*Sighs* I'm starting to see what Mr. Lee was talking about.)"

    scene v11wir13a # TPP Same angle as v11wir13, show MC and Imre climbing into the back seats of the ride share, Ryan is already in the front
    with dissolve
    
    pause 0.75
    
    scene v11wir15 # TPP Show MC, Imre, and Ryan all sitting in the ride share, everyone looking angry and not looking at each other
    with dissolve

    pause 0.75

    scene v11wir5a # TPP Same angle as v11wir5, show MC, Ryan, and Imre walking into the hotel lobby, all looking angry
    with fade

    pause 0.75
    
    scene v11wir6a # FPP Same angle as v11wir6, show Ryan and Imre walking away from MC down the hall, away from the lobby
    with dissolve

    pause 0.75
    stop music fadeout 3
    jump v11_amber_bar