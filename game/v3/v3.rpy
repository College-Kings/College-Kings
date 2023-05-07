label v3start:
    stop music fadeout 3

    scene s200 ## u reading a magazine on your bed (a couple hours later on cover)
    with Fade (1,0,1)

    stop music fadeout 3
    play sound sound.knock

    u "(Who could that be?)"

    play music "music/mlove2.mp3"

    scene s201 # open door and chloe embarrassed smile
    with fade
    # open door sound

    u "Chloe? What are you doing here?"

    scene s201a
    with dissolve

    cl "Hey, uhm... Do you have a minute?"

    scene s201
    with dissolve

    u "Sure, come in."

    scene s202  # you both sitting on your bed
    with dissolve

    pause 0.8

    scene s203 # chloe face front up
    with dissolve

    cl "How's your eye?"

    scene s203a
    with dissolve

    u "Uhm... not too bad. Thanks for asking."

    scene s203b # chloe concerned
    with dissolve

    cl "Look, about yesterday..."

    cl "Me and Grayson had a thing, a looong time ago."

    scene s203d
    with dissolve

    cl "But after a while, he started to lie and do shady shit and... you know, be the person he is. So I broke it off."

    cl "And ever since, he's just been... I guess trying to get back at me?"

    scene s203b
    with dissolve

    cl "I don't know..."

    scene s203c
    with dissolve

    u "If you don't even like Grayson, why were you at his party?"

    scene s203d # chloe thinkign
    with dissolve

    cl "It's complicated."

    cl "Girls join the Chicks 'cause they wanna party and have fun."

    cl "If I don't show up to Ape parties as the Chicks' President, I risk losing the relationships I've built and being voted out."

    scene s203e
    with dissolve

    u "It's just... we were having such a great night and then this kinda ruined it."

    scene s204 # chloe touching your leg, showing your both on bed
    with dissolve

    cl "I know and I'm so sorry."

    scene s204a #chloe standing up
    with dissolve

    cl "I have to go right now, but meet me at midnight behind the gym and I'll make it up to you."

    scene s204b # u standing up
    with dissolve

    u "What if I can't find you? Shouldn't you at least give me your number?"

    scene s204c
    with dissolve

    cl "Haha, I guess I'll have to... for safety reasons."

    scene s204d # chloe kissing you on the cheek
    with dissolve

    play sound sound.kiss
    pause 0.5

    scene s204c
    with dissolve

    cl "I'll see you at midnight. Don't be late."

    stop music fadeout 3

    scene s205 # Imre coming into the room
    with Fade (1,0,1)

    play sound sound.door_open

    pause 0.5

    play music "music/m6punk.mp3"

    scene s205a # I'mre close up
    with dissolve

    u "Imre, where have you been? There's no way the volleyball game went on for this long, did it?"

    scene s206 # I'mre close up
    with dissolve

    imre "Hello, my friend. A gentleman never tells."

    scene s206a
    with dissolve

    u "Wait, you were with a girl?"

    scene s206b # imre proud
    with dissolve

    imre "Well... Not exactly, but I did manage to hide inside the girls' locker room."

    menu:
        "You're crazy":
            $ reputation.add_point(RepComponent.BRO)

            scene s206c
            with dissolve

            u "Hahaha, man you're crazy."

        "That's not cool":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            $ notcool = True

            scene s206c
            with dissolve

            u "Dude, that's not cool. You're invading their privacy."

    label cm_bd: #for compatibility only
    scene s206d # imre mebarassed
    with dissolve

    imre "Yeah, turns out it wasn't a good idea at all. One of the girls had a mental breakdown and they consoled her for hours."

    imre "At one point they called in two different guidance counselors and then those two didn't get along as well..."

    imre "It was just an insane mess and I was stuck hiding in a pile of old jerseys."

    scene s206e
    with dissolve

    u "Well, I hope you learned your lesson."

    scene s206b
    with dissolve

    imre "Of course, next time I'll bring snacks."

    scene s206c
    with dissolve

    u "What? Not what I was-"

    u "You know what, good for you."

    scene s207 # Imre sitting down on the bed
    with dissolve

    imre "So, how has your evening been?"

    scene s207a
    with dissolve

    u "Well, I met this really nice girl called Penelope. And apparently, she's in our history class."

    scene s208
    with dissolve

    imre "Oh shit, is she hot?"

    menu:
        "Hell yeah":
            $ reputation.add_point(RepComponent.BRO)

            scene s208a
            with dissolve

            u "Oh, hell yeah! She's super hot."

            scene s208b # cheeky smile
            with dissolve

            imre "Well that's what I like to hear, go on."

        "She's alright":
            scene s208a
            with dissolve

            u "She's alright I guess."

            scene s208b
            with dissolve

            imre "Well that usually means she's better in bed 'cause she tries harder, go on."

    label cp_bd: #for compatibility only
    if costumeaubrey:
        scene s208c
        with dissolve

        u "Anyways, then I went costume shopping for Mr. Lee's class with Aubrey."

        scene s208d
        with dissolve # Imre pointer ifnger up and mouth open

        u "And before you ask, yes, she's hot."

        if v2_caughtpeeking:
            scene s208a
            with dissolve

            u "And then I might have gotten caught peeking on her while changing..."

            if notcool:
                scene s208b
                with dissolve

                imre "So much for invasion of privacy, huh?"

                scene s208c
                with dissolve

            else:
                scene s208
                with dissolve

                imre "The key is not to get caught, son."

                scene s208a
                with dissolve

            if evelynnumber:
                u "But then I got the cute shop clerk's number. So it turned out to be a blessing in disguise."

            else:
                scene s208a
                with dissolve

                u "But now comes the good part..."
                jump conl

        else:
            scene s208b
            with dissolve

            imre "Nnnice."

    else:
        scene s208c
        with dissolve

        u "Anyways, then I went costume shopping for Mr. Lee's class with her."

        if v2_caughtpeeking:
            u "And we were having a great time..."

            scene s208a
            with dissolve

            u "But... then I might have gotten caught peeking on her while changing."

            if notcool:
                scene s208b
                with dissolve

                imre "So much for invasion of privacy, huh?"

                scene s208c
                with dissolve

            else:
                scene s208
                with dissolve

                imre "The key is not to get caught, son."

                scene s208a
                with dissolve

            if evelynnumber:
                u "But then I got the cute shop clerk's number. So it turned out to be a blessing in disguise."

            else:
                scene s208a
                with dissolve

                u "But now comes the good part..."
                jump conl

        else:
            u "And we had a great time."

            scene s208
            with dissolve

            imre "That sounds great, man."

    scene s208a
    with dissolve

    u "But that's not even the best part..."

label conl:
    u "I'm not sure if I told you, but when I got punched in the face at the party, I was actually talking to the most beautiful girl I've seen in... probably my entire life."

    u "And 30 minutes ago, she knocked on our door, told me to come meet her at midnight behind the gym and kissed me on the cheek before she left."

    scene s208e # Imre super excited grabbing his hands to his head
    with dissolve

    imre "OH MY GOD! My boy is getting laid tonight! Behind the gym! That's amazing, man!"

    scene s208g
    with dissolve

    u "Dude, calm down. I don't think she's like that, haha."

    scene s208h
    with dissolve

    imre "Man, shut the fuck up. She so wants you!"

    scene s209 # Imre standing up
    with dissolve

    pause 0.5

    scene s209a # Imre standing up
    with dissolve

    pause 0.5

    scene s209a2 # Imre starts dancing
    with dissolve

    imre "My man's getting laid."

    scene s209b #different dancing position (other arm forward)
    with dissolve

    imre "My man's getting laid."

    scene s209c
    with dissolve

    u "*Laughs*"

    ### Different Clock scene from 11 pm to 11:50 pm
    stop music fadeout 3
    scene clock2
    with fade

    play sound sound.clock2

    pause (0.5)

    scene clock2a
    with dissolve

    pause (0.5)

    scene clock2b
    with dissolve

    pause (0.5)
    stop sound
    scene clock2c
    with dissolve

    u "(Okay, it's 11:50 pm. Time to go to the gym to meet Chloe.)"

    u "(I really hope she actually shows up.)"

    play music "music/m16punk.mp3"
    queue music [ "music/mchill1.mp3", "music/m7punk.mp3" ]

    scene s211 #you behind gym
    with Fade (1,0,1)

    u "(I guess I'm just gonna wait here.)"

    scene s211a #you behind gym
    with dissolve

    u "(Oh, there she is)"

    scene s212 # showing chloe walking towards you
    with dissolve

    cl "Hey! You came."

    scene s212a
    with dissolve

    u "Of course! I wanted to see how you're gonna make it up to me, haha."

    scene s212b # holding up key
    with dissolve

    cl "With this."

    scene s212c
    with dissolve

    u "A key? What's it for?"

    scene s212d #flirty
    with dissolve

    cl "Well, guess why I asked you to come to the gym."

    scene s212e
    with dissolve

    u "How did you get a key for the gym?"

    scene s212d
    with dissolve

    cl "Oh, I have my ways."

    cl "Wanna break into the gym with me?"

    scene s212e
    with dissolve

    u "I am so down."

    scene s213 # chloe opening the gym door
    with dissolve

    play sound sound.lock

    pause 1.0

    stop sound

    scene s214 # view of your backs standing in the gym door looking from the outside in
    with dissolve

    u "Woah, this is huge. But won't security see that the lights are on from outside?"

    cl "I mean possibly, but where's the fun without the chance of getting caught?"

    u "Fair enough."

    scene s215 # chloe walking ahead of you
    with dissolve

    u "So... is this where you take every guy you meet?"

    scene s215a # chloe turning around
    with dissolve

    cl "Believe it or not, this is actually the first time I've done this."

    scene s215b
    with dissolve

    u "Well now I feel honored."

    scene s215a
    with dissolve

    cl "As you should."

    scene s215d
    with dissolve
    u "(I wonder if she had more in mind when she said she wanted to make it up to me.)"

    menu:
        "Ask her about it":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            label cq_a: #for compatibility only

            scene s216 # chloe walking next to the volleyball
            with dissolve

            u "So, is this the surprise? Breaking into the gym?"

            scene s216a
            with dissolve

            cl "What, you don't like it?"

            scene s216
            with dissolve

            u "No, I do. It's just... I never thought of breaking into the gym."

            scene s216a
            with dissolve

            cl "Really? You never wanted to have the whole gym to yourself? To do whatever you want?"

            scene s216
            with dissolve

            u "I mean I can't say I have, but I'm starting to get the appeal."

            scene s216b
            with dissolve

            cl "Haha, good."

        "Don't question it":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            label cq_b: #for compatibility only

    scene s216c # cl grabs volleyball
    with fade

    cl "You know, I used to play volleyball in high school, you up for a challenge?"

    scene s216d
    with dissolve

    u "Bring it on."

    scene s217 # chloe behind volleyball net
    with fade
    play sound sound.volley3

    scene s217f
    with dissolve
    play sound sound.volley1

    pause 0.5

    scene s217a
    with dissolve
    play sound sound.volley2

    pause 0.5

    scene s217e
    with dissolve

    play sound sound.volley4

    pause 0.5

    scene s217c
    with dissolve

    play sound sound.volley3

    pause 0.5

    scene s217d
    with dissolve

    play sound sound.volley1

    pause 0.5

    scene s217b
    with dissolve

    play sound sound.volley2

    ############ volleyball scene with sounds

    scene s218 # volleyball over the next in the air, perfect for you to smash
    with dissolve

    menu:
        "Win the game":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            # volleybal hit sounds

            scene s218a # you hitting the volleyball
            with vpunch

            play sound sound.volley_hit

            pause 0.5

            ## volleyball floor sound

            scene s218b # ball hitting the floor next to chloe
            with dissolve

            play sound sound.volley_hit

            pause 0.5


            scene s219 # closeup of chloe disappointed
            with dissolve

            cl "Oh no, it was so close!"

            scene s219a
            with dissolve

            u "I'm sure you'll get me next time."

        "Let her win":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            scene s218c # you missing the ball
            with vpunch
            play sound sound.volley_hit

            pause 0.5

            ## volleyball floor sound

            scene s219b # chloe arms in the air celebrating
            with dissolve

            cl "Yaaay, I won!"

            scene s219c
            with dissolve

            u "Oh I'll get you next time."

    label cr_bd: #for compatibility only
    scene s220 # chloe walking down beneath net towards you
    with dissolve

    pause 0.5

    scene s220a # chloe close up right in front of you
    with dissolve

    cl "So there'll be a next time, huh?"

    scene s221a
    with dissolve

    pause 0.5

    scene s221 # showing chloe putting her arms behind your neck
    with dissolve

    pause 0.5

    scene s220b
    with dissolve

    u "I certainly hope so."

    stop music fadeout 3

    play sound sound.old_door

    # Door sound

    scene s220c # chloe in shockc face
    with dissolve

    pause 0.75
    sec "Hello? Is there anyone in here?"

    scene s220d
    with dissolve

    cl "Shit! We need to hide, we're not allowed to be here."

    play music "music/m12punk.mp3"

    scene s222 # showing you hiding behind bleachers
    with fade

    pause 0.5

    scene s223 # showing your view, security guard walking in.
    with dissolve

    sec "Anyone in here?"

    scene s223a # security walking towards light switch.
    with dissolve

    sec "I could have sworn I turned the lights off earlier."

    sec "Hmmm..."

    scene s223b # security guard walking back
    with dissolve

    pause 0.5

    play sound sound.switch
    scene s223c # security out, lights off

    pause 0.75

    scene s222b
    with dissolve

    u "Wow, that was close."

    stop music fadeout 3

    scene s222c
    with dissolve

    cl "Yeah, we should probably get out of here."

    scene s212d # outside of the gym, cl flirty
    with Fade (1,0,1)

    play music "music/mlove2.mp3"

    cl "So, are we even now?"

    scene s212e
    with dissolve

    u "Yeah, we definitely are. We should do this again sometime."

    u "Well, maybe not exactly this."

    scene s212d # cl laughing
    with dissolve

    cl "*Laughs* Yeah."

    cl "I should probably go now, but you have my number."

    cl "Bye, [name]."

    scene s212e # chloe turning around walking away
    with dissolve

    u "I'll see you, Chloe."

    stop music fadeout 3

    scene s225  #Showing you in bed
    with Fade (2,0,2)

    pause 0.5
    play sound sound.swoosh
    pause 0.5

    show fantasyoverlay onlayer foreground

    play music "music/mhorror.mp3"
    scene s226 # Dream with emily, fighting over a stuffed animal in bed
    with flash

    u "Hey, give that back to me."

    scene s226a # emily holding it behind her back away
    with dissolve

    em "You're gonna have to go and get it."

    scene s226b # you reaching over emily
    with dissolve

    u "Oh, I'll get it."

    scene s226c # emily moving it down to her ass
    with dissolve

    pause 0.5

    scene s226d # you grabbing her ass
    with dissolve

    pause 0.5

    scene s226e # em flirty smile
    with dissolve

    em "Uhm, I don't think that's what you wanted to grab."

    scene s226e2
    with dissolve

    u "Oh, I think it is."

    scene s227 # you kissing
    with dissolve

    image glitch = ("images/v3/glitch.webp")

    pause 0.5

    show glitch
    play sound sound.glitch

    pause 0.1

    hide glitch

    scene s228a # your door at night
    with hpunch ## GLITCH TRANSITION

    play sound sound.doorbell

    pause 1

    scene s228b
    with dissolve

    pause 1

    scene s229
    with dissolve

    pause 1

    play sound sound.door_open
    scene s230 # you open door and i's emily at night crying
    with dissolve

    u "Emily? It's 2 am, what are you doing here? I thought you were at your friend's birthday party?"

    scene s230a # emily crying
    with dissolve

    em "[name], I did something bad."

    show glitch
    play sound sound.glitch

    pause 0.1

    hide glitch
    # GLITCH SOUND

    scene s231 # You arguing
    with hpunch # GLITCH TRANSITION

    u "How could you do this to me?!"

    scene s231a
    with dissolve

    em "I'm sorry! I was vulnerable, okay?! Please, I need you."

    #Glitch sound

    scene s231b #You grabbing emily on her shoulders
    with hpunch # Glitch transition

    u "WHY DID YOU HAVE TO RUIN EVERYTHING?!"

    scene s231c
    with dissolve

    pause 0.5

    scene s231d # YOu pushing emily away
    with hpunch # GLITCH TRANSTIION

    u "NO! This is wrong. Just get out! Leave me alone!"

    play sound sound.swoosh

    stop music fadeout 3

    scene s225a # you open your eyes
    with flash
    hide fantasyoverlay onlayer foreground

    u "*Breathing heavily*"

    play music "music/mindie1.mp3"

    queue music [ "music/mindie2.mp3", "music/mindie3.mp3" ]

    scene s232 #Imre waking you op
    with Fade (2,0,2)

    pause 0.5

    scene s233 #Imre closeup
    with dissolve

    imre "Wake up! It's time for training."

    scene s233a
    with dissolve

    u "Huh?"

    scene s233
    with dissolve

    imre "You said you were gonna train with me."

    imre "Remember? Yesterday? In class?"

    scene s233a
    with dissolve

    u "Right, right. Uhm... give me 10 minutes okay?"

    scene s234 # way to the gym
    with Fade (1,0,1)

    u "So uh... where exactly are we going?"

    scene s235 # Imre close up
    with dissolve

    imre "Sports X, it's the cheapest gym in the area and it has basic fighting equipment."

    scene s235a
    with dissolve

    u "Oh, is that where the Wolves train as well?"

    scene s235
    with dissolve

    imre "No, the Wolves have their own fighting gym in the basement. My brother helped build a lot of it."

    scene s235a
    with dissolve

    u "Then why don't you train with them? Didn't you plan on doing that anyways?"

    scene s235
    with dissolve

    imre "You have to be a Wolf to train there. That's one of the reasons I can't wait to pledge, man."

    scene s235d
    with dissolve

    imre "It really sucks 'cause the pledging period doesn't start 'til two weeks after the year has begun."

    scene s235e
    with dissolve

    u "Come on, that's like 10 more days."

    scene s235d
    with dissolve

    imre "Yeah, I guess..."

    scene s236 # Gym reception showing you from the back, girl receptionist
    with fade

    imre "Hey there, my friend would like a trial pass."

    scene s237 # reception close up
    with dissolve

    li "Yeah, that's no problem. I just need an ID."

    scene s237a # showing you giving her an ID
    with dissolve

    imre "So uh... girl, you single?"

    scene s237c # showing you giving her an ID
    with dissolve

    u "Smooth..."

    scene s237b
    with dissolve

    li "Yes, I am."

    scene s237c
    with dissolve

    imre "Do you wanna maybe... you know, hang out sometime?"

    scene s237b
    with dissolve

    li "Hmmm... Do I wanna hang out with you?"

    li "On one hand..."
    li "You seem like a barely-legal-age wannabe jock that hits on any and every girl he sees, regardless of how appropriate or welcome it is."

    li "But on the other hand..."

    li "No, actually that's it."

    scene s237c
    with dissolve

    imre "So, that's a ye-"

    scene s237d
    with dissolve

    li "It's a no."

    scene s237e
    with dissolve

    imre "You're missing out, girl."

    scene s238 # you to near the boxing bag
    with fade

    u "It's interesting how you always find new ways to make women uncomfortable."

    scene s239 # Imre close up
    with dissolve

    imre "At least I try, man. Girls always expect you to make the first move."

    imre "Think about how many girls you could have had if you didn't pussy out everytime."

    scene s239a
    with dissolve

    u "Hey! When have I ever pussied out?"

    scene s239
    with dissolve

    imre "You know what? Never mind, player."

    # PATRON RELEASE END

    imre "Now, show me what you've got."

    menu:
        "Show off":
            $ reputation.add_point(RepComponent.BRO)
            label cw_a: #for compatibility only

            scene s240
            with dissolve

            pause 0.5

            play sound sound.hit

            scene s240d # you doing complicated kick
            with vpunch

            pause 0.2

            scene s240d2 # you on the floor
            with dissolve

            pause 0.2

            scene s240e # you on the floor
            with vpunch

            play sound sound.fall

            pause 0.5

            scene s241
            with dissolve

            imre "*Laughs* Great first move, flawless execution."

            imre "How about we start with the basics? Do you know how to throw a hook, jab and kick?"

            scene s241a
            with dissolve

            u "Uhm yeah, sure."

        "Stick to what you know":
            label cw_b: #for compatibility only
            pass

    scene s240
    with dissolve

    pause 0.5

    play sound sound.hit

    scene s240a
    with vpunch

    pause 0.5

    scene s240
    with dissolve

    pause 0.5

    play sound sound.hit

    scene s240b
    with vpunch

    pause 0.5

    scene s240
    with dissolve

    pause 0.5

    play sound sound.hit

    scene s240c
    with vpunch

    pause 0.5

    scene s241
    with dissolve

    imre "Alriiight. It wasn't exactly perfect form, but it's pretty good for a beginner."

    imre "Let me just go take a piss and we can get to work when I'm back."

    scene s241a
    with dissolve

    u "Okay, sounds good."

    scene s242 # you looking around gym
    with fade

    u "(Why do people come here so early in the morning just to work out?)"

    if not v2_made_a_move_on_evelyn: #if haven't made a move yet
        scene s243 # evelyn working out
        with dissolve

        u "(Isn't that the cute store clerk from the costume shop?)"

        menu:
            "Approach her":
                $ reputation.add_point(RepComponent.BRO)
                label cx_a: #for compatibility only

                scene s244
                with fade

                u "Hey, you were working in the costume shop yesterday, right?"

                scene s245 # eve closeup
                with dissolve

                ev "Yeah, and you're the kid that still calls it a costume shop even though I thoroughly explained that it's just a regular clothing shop now."

                scene s245a
                with dissolve

                u "Look, I think you're quite cute and my friend thinks I chicken out when it comes to girls..."

                u "Is there any chance I could get your number?"

                scene s245b
                with dissolve

                ev "I'm very flattered, but I'm 25 and you seem a bit too young for me."

                scene s245c
                with dissolve

                u "Give me one date to change your mind."

                u "Come on, it'll be fun."

                scene s245
                with dissolve

                ev "Give me one good reason to give you a chance."

                menu:
                    "Be smart":
                        $ evelynnumber = True

                        scene s245a
                        with dissolve

                        u "Look, I don't know and you don't know me. I'm [name] and I'm just looking for someone to have a good time with."

                        u "It's not gonna be the most exciting night of your life, and it's not gonna be a boring night at home playing jenga with the girls."

                        u "What this night will do, is serve as a benchmark for future dates with me."

                        u "What do you say?"

                        scene s245 # eve flirting
                        with dissolve

                        ev "Damn, that was convincing. Okay, I'm in."

                        ev "I'll give you my number, but you better bring your A-game."

                        scene s245a
                        with dissolve

                        u "Don't worry, you won't be disappointed."

                        scene s245b
                        with dissolve

                        ev "Well, I'm looking forward to it."

                        scene s245c
                        with dissolve

                        u "Great, I'll let you know."

                        scene s246 # you walking back
                        with fade

                        u "(I'm getting really good at this flirting thing...)"

                    "Be funny":
                        $ evelynnumber = False

                        scene s245a
                        with dissolve

                        u "How about I'll wear the costume I bought yesterday for our entire date?"

                        scene s245b
                        with dissolve

                        ev "Look, it's very cute that you'd do that for me, but I just don't think we'd be a great fit."

                        ev "I'm sure you'll find someone else."

                        scene s245c
                        with dissolve

                        u "Oh okay... I guess I'll see you around."

                        scene s246 # you walking back
                        with fade

                        u "(Damn, that didn't go as planned...)"

            "Leave it":
                $ reputation.add_point(RepComponent.BOYFRIEND)
                label cx_ad: #for compatibility only

    scene s247 # imre coming back
    with fade

    imre "Okayyy, let's do it."

    scene s248 # Imre in front boxing bag looking you
    with dissolve

    imre "Low-kicks target the legs and weaken the opponent's stance."

    imre "Jabs target the face and keep distance."

    imre "And hooks target the head and serve as hard hits that can knock out your opponent."

    scene s248b # imre finger pointing up
    with dissolve

    imre "But what's missing?"

    scene s248a
    with dissolve

    u "Enough human decency so fighting becomes an unnecessary relic of the past?"

    scene s248c
    with dissolve

    imre "No, body shots."

    imre "Hitting your opponent's body will leave them out of breath and in pain."

    imre "Perfect to get rid of a strong guard or a fast moving opponent."

    scene s248a
    with dissolve

    u "Alright. Show me how."

    scene s248e # Imre looking at the bag
    with dissolve

    imre "It's quite simple. Whenever your opponent leaves his torso open you simply use your left arm to throw a body hook."

    play sound sound.hit

    scene s248f # imre hitting punching bag
    with vpunch

    pause 0.5

    scene s248
    with dissolve

    imre "You wanna try?"

    scene s248a
    with dissolve

    u "Sure."

    scene s249
    with dissolve

    pause 0.5

    play sound sound.hit

    scene s249a
    with vpunch

    imre "Great job! Try it again."

    scene s249
    with dissolve

    pause 0.5

    play sound sound.hit

    scene s249a
    with vpunch
    $ bodyHook = True
    call screen fightPopup("Body Hook")

    play music "music/m16punk.mp3"

    scene s250 # walking back
    with Fade (1,0,1)

    u "That was actually really fun, thanks, Imre."

    scene s251 # Imre close up
    with dissolve

    imre "Yeah, no worries. Let me know if you wanna come with me next time as well."

    scene s251a
    with dissolve

    u "Yeah, I think I will."
    
    play sound sound.vibrate



    if costumeaubrey: # did you meet aubrey?
        if v2_caughtpeeking: # did she catch you?
            if v2_caughtpeekingcounter: # did you talk your way out?
                jump talkedout

            else: # caught and she's mad

                python:
                    MessengerService.new_message(aubrey, _("I wanna talk about what happened yesterday."))
                    MessengerService.new_message(aubrey, _("Any chance that you could come over now?"))
                    MessengerService.add_reply(aubrey, _("Yeah, I can."))
                    MessengerService.new_message(aubrey, _("My room has a window facing the backyard. Can you climb in through there? I'll leave it open."))
                    MessengerService.new_message(aubrey, _("I'd prefer if none of the girls saw you."))
                    MessengerService.add_reply(aubrey, _("Uhm... sure."))

                while MessengerService.has_replies(aubrey):
                    call screen phone
                    if MessengerService.has_replies(aubrey):
                        u "(I should probably check my phone.)"

                u "Sorry Imre, something came up. You're gonna have to go back by yourself, I gotta go."

                scene s251b
                with dissolve

                imre "A booty call this early in the day? Respect, my man."

                scene s251c
                with dissolve

                u "Imre, not everything is about sex, haha. I'll see you later."

                scene s251b
                with dissolve

                imre "I'll see you, player."

                stop music fadeout 3

                scene s252 # you in Aubrey's backyard looking at the house
                with Fade (1,0,1)

                u "(Okay, let's see. Which one's her room?)"

                play music "music/m4punk.mp3"

                u "(Oh no, the only open window is on the second floor.)"

                u "(Yeah, why would she want to mention that anyway...)"

                scene s253 ###### CLIMBING UP THE WINDOW SCENE
                with dissolve

                pause 0.5

                play sound sound.leaves

                scene s253a
                with dissolve

                pause 0.5

                scene s253b
                with dissolve

                pause 0.5

                stop sound

                play sound sound.thud

                scene s253c
                with dissolve

                pause 0.5

                ##################

                scene s254far ## looking into Aubrey's room
                with fade

                au "Did anyone see you?"

                scene s254a
                with dissolve

                u "I don't think so."

                u "You know, you could've really mentioned that your room is on the second floor."

                scene s254
                with dissolve

                au "Look, when you peeked on me and lied about it, I felt like you broke my trust."

                scene s254b
                with dissolve

                au "But, I haven't told anyone about it."

                au "Instead, I've watched a bunch of sitcoms and found a way for us to move past this."

                scene s254c
                with dissolve

                u "Yeah, anything. I'm just really sorry it happened. I shouldn't have-"

                scene s254b
                with dissolve

                au "We need to get even."

                scene s254c
                with dissolve

                u "Get even?"

                scene s254b
                with dissolve

                au "Yeah, level the playing field. Make it fair."

                scene s254c
                with dissolve

                u "Like... you get to peek on me changing?"

                scene s254d
                with dissolve

                au "Or..."
                au "You could just take your clothes off right now."

                scene s254e
                with dissolve

                u "Are you serious?"

                scene s254d
                with dissolve

                au "You said you'd do anything to make it right."

                label cy_a: #for compatibility only
                label cy_b: #for compatibility only
                menu:
                    "Take off your clothes":
                        $ reputation.add_point(RepComponent.BOYFRIEND)
                        $ reputation.add_point(RepComponent.BRO)

                        scene s256b #showing you pulling down your pants
                        with dissolve

                        u "You want me to take my clothes off? Fine, I'll do it."

                        scene s256b2
                        with dissolve

                        au "Good! Do it."

                        scene s256a #you no pants
                        with fade

                        pause 0.5

                    "Refuse":
                        $ reputation.add_point(RepComponent.TROUBLEMAKER)

                        scene s254e
                        with dissolve

                        u "I'm not gonna take my clothes off in front of you."

                        scene s254f
                        with dissolve

                        au "I thought you cared about this friendship?!"

                        scene s255 # aubrey hand grab
                        with dissolve

                        u "I do care!"

                        scene s256 #showing you pulling down your pants
                        with dissolve

                        u "You want me to take my clothes off to prove it?! Fine, I'll take them off."

                        scene s256a2
                        with dissolve

                        au "Good! Fucking do it!"

                        scene s256a #you no pants
                        with fade

                        pause 0.5

        else: # not caught peeking but met
            label talkedout:
                python:
                    MessengerService.new_message(aubrey, _("Hey, I really need your help."))
                    MessengerService.new_message(aubrey, _("Any chance that you could come over now?"))
                    MessengerService.add_reply(aubrey, _("Yeah, I'll be right there.."))
                    MessengerService.new_message(aubrey, _("My room has a window facing the backyard. Can you climb in through there instead of using the front door?"))
                    MessengerService.new_message(aubrey, _("I'll leave it open."))
                    MessengerService.add_reply(aubrey, _("Uhm... sure."))

                while MessengerService.has_replies(aubrey):
                    call screen phone
                    if MessengerService.has_replies(aubrey):
                        u "(I should probably check my phone.)"

                u "Sorry Imre, something came up. You're gonna have to go back by yourself, I gotta go."

                scene s251b
                with dissolve

                imre "A booty call this early in the day? Respect, my man."

                scene s251c
                with dissolve

                u "Imre, not everything is about sex, haha. I'll see you later."

                scene s251b
                with dissolve

                imre "I'll see you, player."

                stop music fadeout 3

                scene s252 # you in Aubrey's backyard looking at the house
                with Fade (1,0,1)

                u "(Okay, let's see. Which one's her room?)"

                play music "music/m4punk.mp3"

                u "(Oh no, the only open window is on the second floor.)"

                u "(Yeah, why would she want to mention that anyway...)"

                scene s253 ###### CLIMBING UP THE WINDOW SCENE
                with dissolve

                pause 0.5

                play sound sound.leaves

                scene s253a
                with dissolve

                pause 0.5

                scene s253b
                with dissolve

                pause 0.5

                stop sound

                play sound sound.thud

                scene s253c
                with dissolve

                pause 0.5

                ##################

                scene s254fars ## looking into Aubrey's room
                with fade

                au "[name], you made it!"

                scene s254h
                with dissolve

                u "Hey, so what do you need my help for?"

                scene s254g
                with dissolve

                au "I'm really bored... you wanna do something?"

                scene s254h
                with dissolve

                u "What? I came here as fast as I could 'cause you're bored??"

                scene s254j
                with dissolve

                au "Oh, like it's so bad spending time with me."

                scene s254k
                with dissolve

                u "That's not what I-"

                u "Doesn't matter, what do you wanna do?"

                scene s254g
                with dissolve

                au "Let's play truth or dare."

                scene s254h
                with dissolve

                u "Alright, you start."

                scene s254l
                with dissolve

                au "Uhm... Truth."

                scene s254m
                with dissolve

                u "Have you ever kissed a girl?"

                scene s254g
                with dissolve

                au "Once, Chloe. But it was just a quick mouth on mouth, no tongue."

                au "Your turn."

                menu:
                    "Truth":
                        $ reputation.add_point(RepComponent.BOYFRIEND)

                        scene s254h
                        with dissolve

                        u "Truth."

                        scene s254l
                        with dissolve

                        au "How many girls have you slept with?"

                        scene s254m
                        with dissolve

                        u "Two, both ex-girlfriends."

                        scene s254g
                        with dissolve

                        au "One of them's Emily, right?"

                        au "Nora told me about her, she seems nice."

                        scene s254h
                        with dissolve

                        u "Yeah, right... It's your turn."

                        scene s254l
                        with dissolve

                        au "Give me a dare."

                        scene s254m
                        with dissolve

                        u "Touch both your elbows in front of your chest."

                        if is_censored:
                            call screen censored_popup("v3_nsfwSkipLabel1")

                        scene s254p
                        with dissolve

                        au "Like this?"

                        label v3_nsfwSkipLabel1:
                            scene s254q
                            with dissolve

                            au "Oh, I see. Very funny."

                            scene s254r
                            with dissolve

                            u "Haha, I thought you did great."

                            scene s254l
                            with dissolve

                            au "Okay, now it's your turn again."


                    "Dare":
                        $ reputation.add_point(RepComponent.TROUBLEMAKER)
                        $ reputation.add_point(RepComponent.BRO)

                scene s254m
                with dissolve

                u "Dare me."

                scene s254l
                with dissolve

                au "Uhm... okay. Take your pants off."

                scene s254m
                with dissolve

                u "What?? I'm not gonna take my pants off."

                u "You gotta give me something I can actually do."

                scene s254l
                with dissolve

                au "I did! It's totally doable."

                scene s254m
                with dissolve

                u "I can't just-"

                scene s254l
                with dissolve

                au "Yeah, you can. See?"

                if is_censored:
                    call screen censored_popup("aubsexad")

                scene s254aa ## aubrey and you standing
                with dissolve

                pause 0.5

                scene s254ab # aubrey grabbing your pants
                with dissolve

                pause 0.5

                scene s254ac # your pants down aubrey forward
                with dissolve

                u "Did you just?"

                scene s256a
                with dissolve

                au "Yeah..."

    else: # you didn't meet aubrey
        python:
            MessengerService.new_message(aubrey, _("Hey, you know how you had to cancel on me yesterday and you really want to make it up to me?"))
            MessengerService.new_message(aubrey, _("Wanna come over now?"))
            MessengerService.add_reply(aubrey, _("Uhh... okay."))
            MessengerService.new_message(aubrey, _("My room has a window facing the backyard. Can you climb in through there instead of using the front door?"))
            MessengerService.new_message(aubrey, _("I'll leave it open."))
            MessengerService.add_reply(aubrey, _("Uhm... sure."))

        while MessengerService.has_replies(aubrey):
            call screen phone
            if MessengerService.has_replies(aubrey):
                u "(I should probably check my phone.)"

        u "Sorry Imre, something came up. You're gonna have to go back by yourself, I gotta go."

        scene s251b
        with dissolve

        imre "A booty call this early in the day? Respect, my man."

        scene s251c
        with dissolve

        u "Imre, not everything is about sex, haha. I'll see you later."

        scene s251b
        with dissolve

        imre "I'll see you, player."

        stop music fadeout 3

        scene s252 # you in Aubrey's backyard looking at the house
        with Fade (1,0,1)

        u "(Okay, let's see. Which one's her room?)"

        play music "music/m4punk.mp3"

        u "(Oh no, the only open window is on the second floor.)"

        u "(Yeah, why would she want to mention that anyway...)"

        scene s253 ###### CLIMBING UP THE WINDOW SCENE
        with dissolve

        pause 0.5

        play sound sound.leaves

        scene s253a
        with dissolve

        pause 0.5

        scene s253b
        with dissolve

        pause 0.5

        stop sound

        play sound sound.thud

        scene s253c
        with dissolve

        pause 0.5

        ##################

        scene s254fars ## looking into Aubrey's room
        with fade

        au "[name], you made it."

        scene s254h
        with dissolve

        u "Yeah, I did. So, how can I make it up to you?"

        scene s254g
        with dissolve

        au "I'm really bored... you wanna do something?"

        scene s254h
        with dissolve

        u "Sure, what do you wanna do?"

        scene s254g
        with dissolve

        au "Let's play truth or dare."

        scene s254h
        with dissolve

        u "Okay, you start."

        scene s254l
        with dissolve

        au "Uhm... Truth."

        scene s254m
        with dissolve

        u "Have you ever kissed a girl?"

        scene s254g
        with dissolve

        au "Once, Chloe. But it was just a quick mouth on mouth, no tongue."

        au "Your turn."

        menu:
            "Truth":
                $ reputation.add_point(RepComponent.BOYFRIEND)

                scene s254h
                with dissolve

                u "Truth."

                scene s254l
                with dissolve

                au "How many girls have you slept with?"

                scene s254m
                with dissolve

                u "Two, both ex-girlfriends."

                scene s254g
                with dissolve

                au "One of them's Emily, right?"

                au "Nora told me about her, she seems nice."

                scene s254h
                with dissolve

                u "Yeah, right... It's your turn."

                scene s254l
                with dissolve

                au "Give me a dare."

                scene s254m
                with dissolve

                u "Touch both your elbows in front of your chest."

                scene s254p
                with dissolve

                au "Like this?"

                scene s254q
                with dissolve

                au "Oh, I see. Very funny."

                scene s254r
                with dissolve

                u "Haha, I thought you did great."

                scene s254l
                with dissolve

                au "Okay, now it's your turn again."

            "Dare":
                $ reputation.add_point(RepComponent.TROUBLEMAKER)
                $ reputation.add_point(RepComponent.BRO)

        scene s254m
        with dissolve

        u "Dare me."

        scene s254l
        with dissolve

        au "Uhm... okay. Take your pants off."

        scene s254m
        with dissolve

        u "What?? I'm not gonna take my pants off."

        u "You gotta give me something I can actually do."

        scene s254l
        with dissolve

        au "I did! It's totally doable."

        scene s254m
        with dissolve

        u "I can't just-"

        scene s254l
        with dissolve

        au "Yeah, you can. See?"

        if is_censored:
            call screen censored_popup("aubsexad")

        scene s254aa ## aubrey and you standing
        with dissolve

        pause 0.5

        scene s254ab # aubrey grabbing your pants
        with dissolve

        pause 0.5

        scene s254ac # your pants down aubrey forward
        with dissolve

        u "Did you just?"

        scene s256a
        with dissolve

        au "Yeah..."

    scene aub1start
    with dissolve

    menu:
        "Kiss her":
            label continuem:
                $ CharacterService.set_relationship(aubrey, Relationship.FWB)
                $ sceneList.add("v3_aubrey")

                stop music fadeout 3
                play music music.ck1.sexy

                scene aub1
                pause 1.0

                scene aub2

                " "

                scene anew1 # aubrey after kiss laughingly
                with dissolve

                au "Is this such a good idea?"

                scene anew1a
                with dissolve

                u "What's the worst that could happen?"

                scene anew2 # right hand in her pants
                with dissolve

                pause 0.5

                scene anew3 # close up of her face aroused
                with dissolve

                au "*Quiet moan* Ohhh okay... definitely a good idea."

                scene anew4 # left hand on her boobs
                with dissolve

                pause 0.5

                scene anew4a # her hands lift her bra up
                with dissolve

                pause 0.5

                scene anew4b # her no bra
                with dissolve

                u "Wow..."

                scene anew2
                with dissolve

                au "*Moans*"

                scene asexnew1

                au "Oh, [name]!"

                au "Fuck..."

                scene anew5 # you grab her pants
                with dissolve

                pause 0.5

                scene anew5a # her pants down
                with dissolve

                pause 0.5

                scene anew5b # your hand on her panties
                with dissolve

                au "Wait."

                scene anew3a
                with dissolve

                au "Now it's my turn."

                scene s257c # aubrey underwear
                with dissolve

                " "

                scene aub3

                pause 1.5

                scene anew6
                with dissolve

                au "You have a nice cock, I could get used to this."

                scene anew6b
                with dissolve

                au "*Kiss*"

                scene anew6c
                with dissolve

                au "*Kiss*"

                scene anew6d
                with dissolve

                au "*Kiss*"

        "Stop it":
            scene s254c
            with dissolve

            u "Okay, you know what? That's enough. We shouldn't go any further than this."

            scene s254
            with dissolve

            au "Go further? What do you mean?"

            scene s254a
            with dissolve

            u "That look you just gave me... we were both thinking about it. It's just not a good idea."

            scene s254
            with dissolve

            au "I wasn't thinking anything."

            scene s254a
            with dissolve

            u "Maybe it's best if I go now."

            scene s254
            with dissolve

            au "Yeah, okay... whatever."
            $ renpy.end_replay()
            scene s264 # you going back to your dorm
            with Fade (1,0,1)

            u "(Oh god, did I just turn down Aubrey, or was I just reading into it?)"

            u "(I just don't know if it would be a good idea if we were to hook up. What if she tells Chloe? Would Chloe be okay with it?)"

            u "(Also, I barely know her...)"

            stop music fadeout 3

            jump aubsexad


label abj:
    show screen aubsex
    scene asexnew2start # aub bj start
    with dissolve

    pause 0.2

    scene asexnew2 #bj first person
    with dissolve

    u "Ahh, fuck!"

    " "
    scene asexnew3 # bj side view
    with dissolve

    u "Aubrey, this feels so fucking good."

    " "

    pause 1.0

    scene s258d # aubrey in bj position looking at you
    with dissolve

    pause 0.7

    scene s258e # you bent down to kiss her
    with dissolve

    scene aub5

    pause 1

    scene s259a
    with vpunch

    pause 0.5

    scene s259 # close up aubrey laughing face next to yours
    with dissolve

    au "*Laughing*"

    au "Lost your balance?"

    scene s259a
    with dissolve

    u "What? Nooo..."

    u "This was just one of my moves."

    scene s259 # close up aubrey laughing face next to yours
    with dissolve

    au "Oh really?"

    scene s259b # aubrey bites your ear
    with dissolve

    pause 1

    scene s259c # aubrey talking into your ear very close
    with dissolve

    au "*Whispers* Fuck me, [name]."

    scene s259d
    with dissolve

    pause 0.5

label amiss:
    scene s259e
    with vpunch

    pause 0.5

    scene asexnew4 # slow sex angle 1

    au "Yeah, that's good!"

    " "

    scene asexnew5 # slow sex angle 2

    au "*moans*"

    " "

    scene asexnew6 # fast sex angle 1

    au "Oh my god, [name]!"

    " "

    scene asexnew7 # fast sex angle 2

    au "*Squeals* Yes, yes, yes!"

    " "

    scene anew7 # aubrey close up seductive
    with dissolve

    au "I want to ride you."

    scene anew7a # roll over
    with vpunch

    pause 0.5

label acow:
    scene anew8 # aubrey sitting up on you
    with dissolve

    au "You ready for round two?"

    scene asexnew9 # slow sex angle 1

    au "Fuck yes!"

    " "

    scene asexnew11 # slow sex angle 2

    au "This feels amazing, [name]!"

    " "

    scene asexnew10 # fast sex angle 1

    au "Yes! Harder!"

    " "

    scene asexnew12 # fast sex angle 2

    au "I'm gonna cum!"

    u "Oh shit, so am I."

    au "Cum in me! It's okay, I'm on the pill."

label acream:
    scene asexnew13 # cum
    with dissolve

    au "AHHHHHH!"

    stop music fadeout 3

    hide screen aubsex

    scene s261 # you both lying on the floor satisfied
    with fade

    au "Oh my god... that was amazing."

    $ renpy.end_replay()

    play music "music/mlove2.mp3"

    scene s261a
    with dissolve

    u "I'm definitely glad I came over."
    u "Why did you want me to climb through the window anyway?"

    scene s261
    with dissolve

    au "Somehow I had a hunch that something might happen between us if I told you to come over..."

    au "And I assume you're talking to other girls and might wanna keep this a secret."

    au "Plus... the secrecy kinda makes it hotter."

    scene s261a
    with dissolve

    u "Haha, I can't disagree with that."

    u "(Damn... that was really thoughtful of her, but in a very weird way.)"

    u "I should probably get going soon."

    scene s261
    with dissolve

    au "Yeah, I need to get back to studying as well..."

    play sound sound.kiss

    scene s263 # kiss
    with dissolve

    pause 0.5

    scene s261
    with dissolve

    pause 0.5

    stop music fadeout 3

    scene s264 # you going back to your dorm
    with Fade (1,0,1)

    u "(I can't believe I just had sex with Aubrey... that was amazing.)"

    if CharacterService.is_girlfriend(lauren):
        u "(I wonder if Lauren would be upset if she knew. I guess I'll have to decide how honest I wanna be on our date tonight.)"

label aubsexad:
    pause 0.5

    play music "music/mchill1.mp3"

    queue music [ "music/mchill2.mp3"]


### Meet Lauren
    if CharacterService.is_girlfriend(lauren):
        jump continueq

    else: # you're not dating Lauren
        scene s265 # lauren sitting in front of your door
        with dissolve

        u "Lauren? What are you doing here?"

        if meetlauren and Moods.AWKWARD in lauren.mood: # you've met lauren in the cafe
            scene s266 # Lauren closeup awkward
            with dissolve

            la "Hey, uhm..."

            la "I'm here to ask you for a favor... as a friend."

            scene s266a
            with dissolve

            u "Uhm, okay... What is it?"

        elif meetlauren:
            scene s266b # lauren closeup smiling
            with dissolve

            la "Heyyy. I need a favor."

            scene s266c
            with dissolve

            u "Alright, how can I help?"

        else:
            scene s266 # Lauren closeup awkward
            with dissolve

            la "Hey, uhm... I know we haven't talked since the park."

            la "But I kinda need a favor... as a friend."

            scene s266a
            with dissolve

            u "Uhm, okay. What is it?"

label continuen:

    scene s267 # lauren sitting
    with dissolve

    pause 0.5

    scene s267a # lauren standing up
    with dissolve

    pause 0.5

    scene s268 # lauren close up
    with dissolve

    la "So you know how I'm majoring in psychology?"

    scene s268a
    with dissolve

    u "Uh..."

    scene s268
    with dissolve

    la "For one of my assignments I need to do several personality tests on someone and analyze them."


    la "Would you wanna be my test subject?"

    menu:
        "I'd love to":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            scene s268a
            with dissolve

            u "Yeah, I'd love to."

        "I don't know...":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            scene s268a
            with dissolve

            u "I don't know, Lauren. Sounds kinda weird."

            scene s268
            with dissolve

            la "[name], pleaaase. It's just answering a few questions."

            scene s268a
            with dissolve

            u "Okay, fine."

    label dc_bd: #for compatibility only
    scene s268 # Lauren happy
    with dissolve

    la "Thank you so much!"

    scene s269 # showing you and lauren standing from the side
    with dissolve

    pause 0.5

    scene s269a # lauren hugs you
    with dissolve

    pause 0.8

    scene s269
    with dissolve

    pause 0.5

    scene s268 # Lauren happy (closeup)
    with dissolve

    la "Let's meet up in the next couple days then and we'll go through the first personality test."

    scene s268a
    with dissolve

    u "Alright, just send me a text."

label continueq:
    scene s270 #showing you laying on your bed in your dorm thinking // top down camera slight angle
    with Fade (1,0,1)

    pause 0.5

    play sound sound.call

    scene s270a2
    with dissolve

    pause 0.5

    scene s270a # you looking at your phone in your hand
    with dissolve

    u "Huh? Julia's calling me."

    menu:
        "Answer":
            stop sound
            play sound sound.answer_call
            $ reputation.add_point(RepComponent.BOYFRIEND)

            scene s270b # you answer, hold phone next to your ear
            with dissolve

            u "Hey, Julia!"

            scene s271 # showing Julia in her kitchen on the phone smiling
            with dissolve

            ju "Hey honey, how are you?"

            scene s270b # you answer, hold phone next to your ear
            with dissolve

            u "I'm good, what's up?"

            scene s271 # you answer, hold phone next to your ear
            with dissolve

            ju "I was wondering if you would like to go shopping with me tomorrow morning?"

            ju "I would pick you up and you could tell me all about your first week at college."

            ju "And maybe we can buy you a nice new outfit for whatever girl you met?"

            scene s270c # you on the phone  concerned
            with dissolve

            u "(Shit... if I meet her, she'll see my bruises and get really worried.)"

            menu:
                "Shopping sounds great":
                    $ meetjulia = True
                    $ reputation.add_point(RepComponent.BOYFRIEND)

                    u "Yeah, shopping sounds great, Julia."

                    u "I'll see you tomorrow then."

                    scene s271
                    with dissolve

                    ju "Okay, honey. I'll call you when I'm at San Vallejo."

                    scene s270b
                    with dissolve

                    u "Alright, bye."

                    scene s271
                    with dissolve

                    ju "Bye, honey."

                    play sound sound.reject_call

                "I can't, sorry":
                    $ reputation.add_point(RepComponent.TROUBLEMAKER)

                    u "Sorry, Julia... I'm really busy this weekend."

                    scene s271a # Julia on the phone, a bit disappointed / sad
                    with dissolve

                    ju "Oh... okay, honey. Next time then."

                    scene s270c
                    with dissolve

                    u "Yeah... next time."

                    play sound sound.reject_call

        "Don't answer":
            stop sound
            play sound sound.reject_call

            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            # phone call declined sound

            scene s270
            with dissolve

            $ grant_achievement("not_now_mom")
                
            u "(I don't really feel like talking to her right now.)"

    label de_bd: #for compatibility only
    scene s270
    with fade
    play sound sound.knock

    pause 0.75
    scene s272 # showing you sitting on the side of bed pushing ready to stand up // camera angle to side of bed, looking at you from front
    with dissolve

    u "(I guess there goes my one minute of alone time...)"

    play sound sound.door_open

    scene s273 # FIRST PERSON: through your dorm door open seeing riley and ryan standing there happily looking at you, only seeing their upper body and faces, both mouths closed// ryan hold picnic basket
    with dissolve

    u "Hey guys."

    scene s273a # Ryan talking happy
    with dissolve

    ry "What's up, [name]?"

    scene s273b #Riley talking happy
    with dissolve

    ri "Wow, your face looks really as bad as Ryan said."

    scene s273
    with dissolve

    u "Thanks, Riley. What can I do for you?"

    scene s273b
    with dissolve

    ri "It's a really nice day, so we're going to go for a picnic. Wanna come?"

    scene s273a
    with dissolve

    ry "Plus there'll be some hotties in the park."

    scene s273c # Riley looking at ryan jokingly annoyed and talking, ryan looking at you
    with dissolve
    ri "Is that all you think about, Ryan?"

    menu:
        "Compliment Riley":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            scene s273d # Riley looking at ryan joking annoyed but her mouth is closed, ryan looking at her with a grin
            with dissolve

            u "I think Riley is all the hottie I need."

            scene s273e #Riley lookin happy (awww face) at you mouth open, ryan looking slightly annoyed at you , his head slightly tilted (like cmon man) mouth closed
            with dissolve

            ri "Awww, thank you."

            scene s273f # same as 273e but ryan mouth open and riley closed
            with dissolve

            ry "This guy..."

            ry "So, you coming, or what?"

            scene s273g # same as 273f but both mouths closed
            with dissolve

            u "Yeah, alright. Let me just change out of my gym clothes."

        "Agree with Ryan":
            $ reputation.add_point(RepComponent.BRO)

            scene s273d
            with dissolve

            u "Well, count me in then."

            scene s273h # Riley lookign jokingly annoyed at you mouth open, ryan looking happy at you grinning mouth closed
            with dissolve

            ri "Of course that's what made you wanna go. Why do I even spend time with you guys?"

            scene s273j # same as 273h but riley mouth closed
            with dissolve

            u "Oh come on, Riley. You're one of the hotties."

            scene s273h
            with dissolve

            ri "What a sincere compliment. Are you ready to go then?"

            scene s273j
            with dissolve

            u "Yeah, let me just change out of my gym clothes."

    label df_bd: #for compatibility only
    scene s274 # you different clothes, riley and ryan in the park, riley preparing the picnic blanket, all happy.  you talking."
    with Fade (1,0,1)

    u "This is a really nice spot."

    scene s275 # close up ryan happy standing FIRST PERSON
    with dissolve

    ry "Yeah, it really is."

    scene s276 # close up Riley curious she sitting down angle from you standing FIRST PERSON
    with dissolve

    ri "So uhm [name]... How are you gonna get back at Grayson?"

    scene s276a
    with dissolve

    u "What do you mean, get back?"

    scene s276
    with dissolve

    ri "You know, he punched you in front of so many people... how are you gonna avenge yourself?"

    scene s275ar  # ryan disturbed looking at riley
    with dissolve

    ry "Riley, I don't think [name] wants to get back into it with Grayson."

    stop music fadeout 3

    ry "Any retribution will only make it worse."

    play music "music/m9punk.mp3"

    scene s275br # ryan mouth closed disturbed looking at riley
    with dissolve

    u "Why?! Because he's some kind of god that can do whatever he wants?!"

    scene s275b # ryan disturbed looking at you mouth closed
    with dissolve

    u "I'm not scared of him."

    scene s275a # ryan disturbed mouth open looking at you
    with dissolve

    ry "I'm just saying that-"

    scene s275b
    with dissolve

    u "You know why Grayson punched me? Cause I was about to make out with Chloe and he's still not over her!"

    u "And guess who fucking came to my dorm to make it up to me yesterday evening? Chloe."

    scene s275c #ryan slightly surprised but still upset
    with dissolve

    ry "Did you hook up?"

    scene s275d #ryan slightly surprised but still upset mouth closed
    with dissolve

    u "I mean no, we just hung out at the gym, but if it wasn't for that stupid security guard-"

    u "You know, we'll get closer in the future."

    scene s275c
    with dissolve

    ry "Look, I don't wanna be that guy. but..."

    ry "Do you really think that pursuing Chloe is a good idea?"

    scene s275d
    with dissolve

    u "Why?! You think I should fear Grayson?! Fuck him. I couldn't care less."

    scene s275e # Ryan angry
    with dissolve

    ry "No, 'cause she's a bitch. After I went back to the party, Grayson told me about all the shady shit she did."

    scene s275f # Ryan angry mouth closed
    with dissolve

    u "Really?! Grayson?! Well I'm glad your new mentor gives such great advice."

    scene s275e
    with dissolve

    ry "When you were knocked out, who fucking came to help you?!"

    scene s275g # Ryan angry pointing at himself
    with dissolve

    ry "It was me! Chloe didn't give a fuck!"

    scene s275e
    with dissolve

    ry "She went after Grayson, 'cause she felt personally attacked! She thought about herself, not about you!"

    scene s275f
    with dissolve

    u "You don't know what you're talking about! Chloe likes me. She went after Grayson 'cause someone needed to."

    menu:
        "Insult Ryan":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            
            u "Cause you were too fucking pussy to do it yourself."

            scene s275e
            with dissolve

            ry "Fuck you! I looked after you, I brought you home!"

            ry "Chloe is playing you! Like she played Grayson! Don't fucking fall for it."

            scene s275f
            with dissolve

            u "You don't know Chloe at all! You're just fucking jealous!"

        "Walk away":
            $ reputation.add_point(RepComponent.BRO)

    scene s276b #RIley sad and concerned
    with dissolve

    ri "Guys, please stop fighting!"

    scene s277 # you angry looking at riley standing up showing both riley and ryan in the foreground but focus on you (looking over their backs)
    with dissolve

    u "No, fuck this, I'm leaving!"

    scene s277a # you walking away
    with dissolve

    pause 0.5

    scene s277b # you gone
    with dissolve

    pause 0.5

    scene s276b # riley looking concerned and shocked at Ryan
    with dissolve

    ri "Are you not gonna go after him?!"

    scene s275ar
    with dissolve

    ry "Nah, he's being a bitch."

    scene s276b # riley looking mad at Ryan
    with dissolve

    ri "Fine, then I'll go after him."

    stop music fadeout 3

    ################

    scene s278 # showing you walking behind a wooden cabin
    with fade

    ri "[name], wait!"

    play music "music/mlove1.mp3"

    scene s279 # Riley arriving at the spot behind the cabin , emphatic
    with dissolve

    ri "Hey, stop... I'm sure Ryan didn't mean what he said."

    scene s279a
    with dissolve

    u "I just don't get why he's siding with Grayson after what happened."

    u "He should be helping me get back at him instead of becoming his best friend."

    scene s279
    with dissolve

    ri "I know... can you please just come back and maybe we can talk it out?"

    scene s279a
    with dissolve

    u "There's no talking to him, he doesn't seem to understand what loyalty even is."

    scene s279
    with dissolve

    ri "If you don't wanna talk to him, can you at least talk to me?"

    scene s280 # showing both of you right in front of the back of the cabin , you mouth open
    with dissolve

    u "Fine."

    scene s280a # both sitting down with back against the cabin, quite close to each other ( their arms are clsoe to touching)
    with dissolve

    pause 0.5

    scene s281 # close up riley sitting empathy FIRST PERSON
    with dissolve

    ri "So what's going on between you and Chloe? She's the President of the Chicks, right?"

    menu:
        "I like her":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            scene s281a
            with dissolve

            u "Yeah, we met at the Apes' rush party and I really like her."

            u "We haven't done anything yet, but I feel like we really have a connection, you know?"

            scene s281b # riley a bit dissappointed
            with dissolve

            ri "Oh uhm... yeah, that sounds really good. I'm happy for you."

        "She's into me":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            scene s281a
            with dissolve

            u "Yeah, I mean it's nothing serious. She's really into me, but I don't know how I feel yet."

            u "You know, keeping my options open?"

            scene s281d #riley cute smile
            with dissolve

            ri "I can certainly see why she'd be into you."

            scene s281e
            with dissolve

            u "What do you mean?"

            scene s281d
            with dissolve

            ri "You're attractive and charismatic and-"

            menu:
                "Kiss her":
                    $ CharacterService.set_relationship(riley, Relationship.KISSED)
                    $ reputation.add_point(RepComponent.TROUBLEMAKER)

                    show rikiss2
                    pause 1
                    play sound sound.kiss

                    $ grant_achievement("lips_dont_lie")
                        
                    " "

                    scene s281f # riley stunned but happy
                    with dissolve

                    ri "*Blushes* Uhm..."

                    scene s281g
                    with dissolve

                    u "Sorry, I just had to."

                    scene s281f # riley stunned but happy
                    with dissolve

                    ri "I'm glad you did."

                "Don't kiss her":
                    $ reputation.add_point(RepComponent.BOYFRIEND)

                    ri "Just a really great guy."

                    scene s281e
                    with dissolve

                    u "Thanks, Riley."

    label dj_bd: #for compatibility only
    scene s281
    with dissolve
    ri "You know, Ryan is probably waiting for me to come back. Are you sure you wanna leave?"

    scene s281a
    with dissolve

    u "Yeah, I think I need some space from Ryan."

    scene s281
    with dissolve

    ri "Okay... I'll see you later then."

    scene s281a
    with dissolve

    u "Yeah, I'll see you."

    stop music fadeout 3

    if CharacterService.is_girlfriend(lauren): #LAUREN MOVIES
        play music "music/mindie2.mp3"

        scene s282  ## later that day transition pic
        with Fade (1,0,1)

        u "(I can't believe I'm finally going on a real date with Lauren...)"

        u "(I better not fuck this up.)"

        scene s284 # Knocking on lauren's dorm
        with Fade (1,0,1)
        play sound sound.knock
        pause 1

        play sound sound.door_open

        scene s285 # Lauren oppens the door smiling
        with dissolve
        pause 0.25

        la "Heyyy."

        scene s285a
        with dissolve

        u "Wow, you look incredible..."

        scene s285b # lauren cute
        with dissolve

        la "Awww, thank you, [name]."

        scene s285c
        with dissolve

        u "Are you ready to go?"

        scene s285b
        with dissolve

        la "Yeah, let's go."

        scene s286 # you two walking at night through the city
        with Fade (1,0,1)

        pause 0.7

        scene s287 # Lauren cute smile
        with dissolve

        la "So, what did you do all day?"

        if "v3_aubrey" in sceneList:
            scene s287a # lauren closeup while walking her mouth closed  FIRST PERSON
            with dissolve
            u "(Okay, time to make a decision. Should I tell her about what happened with Aubrey?)"

            menu:
                "Tell her what happened":
                    $ toldlauren = True
                    $ reputation.add_point(RepComponent.BOYFRIEND)
                    $ CharacterService.set_mood(lauren, Moods.MAD)
                    $ CharacterService.set_relationship(lauren, Relationship.FRIEND)

                    u "(Lauren values honesty and we're not in a relationship yet, so she'll probably be understanding as long as I tell her the truth.)"

                    u "Okay listen, I need to tell you something."

                    scene s287
                    with dissolve

                    la "What is it?"

                    scene s287a
                    with dissolve

                    u "This morning Aubrey invited me over..."

                    u "... and we had sex."

                    scene s287b # Lauren sad and shocked
                    with dissolve

                    la "What?"

                    scene s287c
                    with dissolve

                    u "I know how much you care about honesty and I wanted to start this right."

                    scene s287b
                    with dissolve

                    la "You had sex with another girl... right before our first date?"

                    scene s287c
                    with dissolve

                    u "Yeah, but it's not like we're in a relationship. You see, I did nothing wrong."

                    scene s287b
                    with dissolve

                    la "Right... Well great job on finding a loophole."
                    la "I don't think I wanna do this anymore."

                    scene s287d #la walks away the direction you cam from, her back to you (she turns around)
                    with dissolve

                    u "But we're not even dating?! I was just being real!"

                    scene s287e # Lauren turns around sad and slightly angry
                    with dissolve

                    la "Be real with someone else then."

                    scene s287f # Lauren gone
                    with dissolve

                    $ grant_achievement("truth_hurts")
                        
                    u "(Fuck me... I guess that's what honesty gets you.)"

                    jump dk_ad

                "Don't tell her":
                    $ reputation.add_point(RepComponent.TROUBLEMAKER)

                    u "(Lauren seems to value loyalty, she might be upset if she finds out and I don't wanna ruin our date before it even started.)"

        scene s287a # lauren closeup while walking her mouth closed  FIRST PERSON
        with dissolve

        label dk_bb: #for compatibility only
        u "Uhm... I went picnicking with Riley and Ryan. What about you?"

        scene s287
        with dissolve

        la "Mostly studying, I'm glad to finally do something exciting."

        scene s287a
        with dissolve

        u "I'll make sure this date won't disappoint then."

        stop music fadeout 3

        scene s289 # you two from front view in the last row at a cinema # check lighting
        with Fade (1,0,1)

        pause 0.5

        play music "music/mindie1.mp3"

        scene s290 # lauren close up whispering ironically FIRST PERSON
        with dissolve

        la "*Whispers* Why did you have to pick a horror film? Is fear really the emotion you want me to feel on our first date?"

        scene s290a
        with dissolve

        u "*Whispers* Oh come on, it's not that bad."

        scene s290
        with dissolve

        la "*Whispers* You just want me to hold your hand when you get scared."

        scene s290a
        with dissolve

        u "*Whispers* Now would that be so bad?"

        scene s290b # lauren cute also render s290c with mouth closed
        with dissolve

        la "*Whispers* I could think of worse."

        scene s289 # you both watching the movie front view
        with fade

        pause 0.5
        play sound sound.horror

        scene s289b # lauren grabs onto your arm scared
        with dissolve

        la "*Squeals*"

        scene s289c # Looking at lauren  you smiling
        with dissolve

        u "*Whispers* Now look who's getting scared."

        scene s289d # lauren smiling flirty back getting her face closer to yours
        with dissolve

        la "*Whispers* I was just making sure you're safe."

        label dl_a: #for compatibility only
        label dl_b: #for compatibility only
        menu:
            "Kiss her":
                scene laurenkiss2 #self explanatory, same camera as s289
                with dissolve

                pause 2.0

                menu:
                    "Reach under her skirt":
                        $ reputation.add_point(RepComponent.TROUBLEMAKER)

                        scene s291a # same camera angle but your hand is under her skirt
                        with dissolve

                        pause 0.5

                        la "[name], I don't think I want to do this."

                        menu:
                            "Keep going":
                                $ reputation.add_point(RepComponent.TROUBLEMAKER)
                                $ laurentoofar = True
                                $ CharacterService.set_mood(lauren, Moods.MAD)
                                $ CharacterService.set_relationship(lauren, Relationship.FRIEND)

                                scene s291b # your hand moves further up
                                with dissolve

                                pause 0.5

                                scene s290f # lauren horny face
                                with dissolve

                                la "*Moans quietly*"

                                stop music fadeout 3

                                play sound sound.slap

                                scene s291c # lauren smacks your hand away
                                with hpunch

                                pause 0.5

                                scene s290g # lauren upset
                                with dissolve

                                la "I told you I don't want to do this!"

                                scene s289f #Lauren standing up
                                with dissolve

                                pause 0.5

                                scene s289g # you showing remorse head in hands // lauren gone
                                with dissolve

                                u "(Shit, I pushed it too far.)"

                                jump dk_ad

                            "Stop":
                                $ reputation.add_point(RepComponent.BOYFRIEND)

                                scene s290b
                                with dissolve

                                la "Thank you, I just need some time."

                                pause 0.5

                                scene s290e # Lauren looking back at the movie screen with cute expression
                                with dissolve

                                pause 0.5

                    "Keep hands to yourself":
                        $ reputation.add_point(RepComponent.BOYFRIEND)

                        pause 1.0

                        scene s290c
                        with dissolve

                        pause 0.5

                        scene s290e # Lauren looking back at the movie screen with cute expression
                        with dissolve

                        pause 0.5

            "Continue watching":
                scene s290c
                with dissolve

                pause 0.5

                scene s290e # Lauren looking back at the movie screen with cute expression
                with dissolve

                pause 0.5

        # after movie
        stop music fadeout 3

        scene lanew1 # walking through park at night
        with Fade (1,0,1)

        la "After watching that movie, I'm just constantly scared a clown's gonna jump out of one of these bushes."

        scene lanew2a # lauren close up scared mouth closed
        with dissolve

        u "Haha, don't worry, I'll protect you."

        scene lanew2b # lauren flirty doubtful
        with dissolve

        la "I'm not sure you'd have much of a chance against a killer clown."

        scene lanew2c
        with dissolve

        u "Oh trust me, you just haven't seen my tickle attack."

        scene lanew2b
        with dissolve

        la "Your tickle attack?"

        scene lanew3 # you ticking lauren
        with dissolve

        la "*Laughs* Hahaha, stop."

        scene lanew2e # lauren smiling mouth closed
        with dissolve

        u "See? The clown wouldn't stand a chance."

        scene lanew2d # lauren smiling mouth open
        with dissolve

        la "Haha, maybe you're right."

        scene s292 # you two in front of laurens dorm room, lauren about to open the door
        with Fade (1,0,1)

        pause 0.5
        play music "music/mlove2.mp3"

        scene s293 # FIRST PERSON: lauren close up turns around looking at you cute
        with dissolve

        la "I had a great time tonight."

        scene s293a
        with dissolve

        u "Yeah, me too. We should do something this weekend."

        scene s293
        with dissolve

        la "Yeah, that sounds good."

        scene s293b # lauren curious
        with dissolve

        la "Also I was gonna ask you something."

        la "For one of my psychology assignments I need to do several personality tests on someone and analyze them."

        la "Would you wanna be my test subject?"

        scene s293c
        with dissolve

        u "Yeah, definitely!"

        scene s293
        with dissolve

        la "Really? Thank you so much."

        play sound sound.door_open

        scene s293d2 # lauren entering
        with dissolve

        pause 0.5

        scene s293d # lauren opens the door and steps forward one step
        with dissolve

        la "Good night, [name]."

        scene s293e
        with dissolve

        u "Yeah, good night, Lauren."

        play sound sound.door_close

        # door close sound

        scene s293g # door shut in front of you
        with dissolve

        pause 0.5

        stop music fadeout 3

    else:
        scene s282a  ## you in your dorm: It's the same day but It's nighttime now on laptop
        with Fade (1,0,1)

        stop music fadeout 3


        pause 1


        jump continues

label dk_ad:
    stop music fadeout 3

    scene s282b  ## you in your dorm: later that night on your laptop
    with Fade (1,0,1)

    pause 1

label continues: # This is after the date
    play music "music/horror2.mp3"

    play sound sound.call

    scene s294 # phone on table unknown number
    with dissolve

    u "(Huh, who would call me this late?)"

    stop sound

    play sound sound.answer_call

    scene s295 # you on the phone from the side
    with dissolve

    u "Hello?"

    scene s295a
    with dissolve

    unknown "Hello sir, am I talking to [name]?"

    scene s295
    with dissolve

    u "Yeah that's me, who is this?"

    scene s295a
    with dissolve

    unknown "This is Sarah Haddock calling from San Vallejo Hospital. Do you happen to know Imre Varga? You're listed as his emergency contact."

    scene s295b
    with dissolve

    u "Yes, he's my roommate. What happened?!"

    stop music fadeout 3

jump v4start
