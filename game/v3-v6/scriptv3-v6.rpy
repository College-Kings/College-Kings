init python:
    persistent.ep = 10

define steam = False
define developer = True
define config.steam_appid = 1463120

define _game_menu_screen = "ingmenu"

label splashscreen:
    # Get Animation/Transform List
    show nohardfeelings at achievementShow
    $ achievementAtList = renpy.get_at_list("nohardfeelings")
    hide nohardfeelings

    # Splashscreen
    scene black
    with Pause(1)

    show splashone
    with dissolve
    with Pause(2)

    show splashtwo
    with dissolve
    with Pause(2)

    show splashthree
    with dissolve
    with Pause(2)

    scene black
    with dissolve
    with Pause(1)

    return

label clrep2a:
$ contact_Chloe.newMessage("I'm really busy today, but I could do tonight after 11 or so.")
$ contact_Chloe.addReply("Alright, cool. I'll be at yours for 11", "clrep3a")
call screen messager(contact_Chloe)

label clrep3a:
$ clrep3 = 1
$ contact_Chloe.newMessage("Sounds good :)")

call screen messager(contact_Chloe)


label jorep8a:
$ addPoint("bro", 1)
$ contact_Josh.newMessage("Dope")
$ contact_Josh.newMessage("Come by 995 Sereno Drive at 8, it's my friends house.")
call screen messager(contact_Josh)

label jorep8b:
$ contact_Josh.newMessage("Aww, come on. You'll be back by 11.")
$ contact_Josh.newImgMessage("images/text1.webp")
$ contact_Josh.newMessage("I told my friend Amber about you and she really wants to meet you.")
$ contact_Josh.addReply("Alright, I'll come.", "jorep12a")
$ contact_Josh.addReply("Josh, I don't know, man. I don't wanna be late.", "jorep12b")
call screen messager(contact_Josh)

label jorep12a:
$ jorep12 = 1
$ joisreply = 0
$ addPoint("bro", 1)
$ contact_Josh.newMessage("Dope")
$ contact_Josh.newMessage("Come by 995 Sereno Drive at 8, it's my friends house.")
call screen messager(contact_Josh)

label jorep12b:
$ contact_Josh.newMessage("Remember how you told me in high school that you felt like you always missed out on all the crazy stories?")
$ contact_Josh.newMessage("Don't miss out now.")
$ contact_Josh.addReply("Fine, I'll come. But I need to go before 11.", "jorep14a")
$ contact_Josh.addReply("I can't, sorry.", "jorep14b")
call screen messager(contact_Josh)

label jorep14a:
$ jorep14 = 1
$ joisreply = 0
$ contact_Josh.newMessage("Dope")
$ contact_Josh.newMessage("Come by 995 Sereno Drive at 8, it's my friends house.")
call screen messager(contact_Josh)

label jorep14b:
$ jorep14 = 2
$ joisreply = 0
$ addPoint("bf", 1)
$ contact_Josh.newMessage("This guy")
call screen messager(contact_Josh)

label amrep3a:
$ addPoint("bro", 1)
$ contact_Amber.newMessage("Oh really? How are you gonna do that?")
$ contact_Amber.addReply("I give some world-class massages", "amrep4a")
$ contact_Amber.addReply("I'll stay longer next time", "amrep4b")
call screen messager(contact_Amber)

label amrep3b:
$ contact_Amber.newMessage("Oh okay, hope everything's okay xx")
$ contact_Amber.addReply("Yeah, it's all good.", "amrep5a")
call screen messager(contact_Amber)

label amrep4a:
$ addPoint("tm", 1)
$ contact_Amber.newMessage("That does sound enticing ;)")

call screen messager(contact_Amber)

label amrep4b:
$ contact_Amber.newMessage("Deal xx")
call screen messager(contact_Amber)

label amrep5a:
$ contact_Amber.newMessage("Deal xx")
call screen messager(contact_Amber)

label amrep3aa:
$ addPoint("bro", 1)
$ contact_Amber.newMessage("Oh wow, I was just checking. :P")
$ contact_Amber.addReply("Don't worry, you'll see me soon", "amrep4aa") # Edited
$ contact_Amber.addReply("Haha, I'm fine.", "amrep4ba")
call screen messager(contact_Amber)

label amrep3ba:
$ contact_Amber.newMessage("Oh okay, hope you're good xx")
$ contact_Amber.addReply("Yeah, no worries", "amrep5aa")
call screen messager(contact_Amber)

label amrep4aa:
$ addPoint("tm", 1)
$ contact_Amber.newMessage("Was hoping xx")

call screen messager(contact_Amber)

label amrep4ba:
$ contact_Amber.newMessage("That's good xx")
call screen messager(contact_Amber)

label amrep5aa:
$ contact_Amber.newMessage("That's good xx")
call screen messager(contact_Amber)

label amrep3ab:
$ addPoint("bro", 1)
$ contact_Amber.newMessage("Oh shut up, I was just checking in")
$ contact_Amber.addReply("Don't worry, you'll see me again", "amrep4ab")
$ contact_Amber.addReply("Haha, I'm fine", "amrep4bb")
call screen messager(contact_Amber)

label amrep3bb:
$ contact_Amber.newMessage("Oh okay, hope you're good xx")
$ contact_Amber.addReply("Yeah, no worries", "amrep5ab")
call screen messager(contact_Amber)

label amrep4ab:
$ addPoint("tm", 1)
$ contact_Amber.newMessage("Was hoping xx")

call screen messager(contact_Amber)

label amrep4bb:
$ contact_Amber.newMessage("That's good xx")
call screen messager(contact_Amber)

label amrep5ab:
$ contact_Amber.newMessage("That's good xx")
call screen messager(contact_Amber)

label larep13a:
$ larep13 = 1
$ contact_Lauren.newMessage("Great :) Meet me at our economics' classroom.")
call screen messager(contact_Lauren)

label amrep8a:
$ contact_Amber.newMessage("Go somewhere where you're completely alone xx")
$ contact_Amber.newMessage("I got a surprise for you ;)")
jump phoneaa

label v3start:
    return # TEMP
    stop music fadeout 2.0

    scene s200 ## u reading a magazine on your bed (a couple hours later on cover)
    with Fade (1,0,1)

    stop music fadeout 2.0
    play sound "sounds/knock.mp3"

    "*Knock knock knock*"

    u "(Who could that be?)"

    play music "music/mlove2.mp3"

    scene s201 # open door and chloe embarassed smile
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

    cl "If I don't show up to Ape parties as the Chicks' president, I risk losing the relationships I've built and being voted out."

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

    play sound "sounds/kiss.mp3"
    pause 0.5

    scene s204c
    with dissolve

    cl "I'll see you at midnight. Don't be late."

    stop music fadeout 2.0

    scene s205 # Imre coming into the room
    with Fade (1,0,1)

    play sound "sounds/dooropen.mp3"

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
        "You're crazy.":
            $ addPoint("bro", 1)

            scene s206c
            with dissolve

            u "Hahaha, man you're crazy."

        "That's not cool.":
            $ addPoint("bf", 1)
            $ notcool = True

            scene s206c
            with dissolve

            u "Dude, that's not cool. You're invading their privacy."

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
        "Hell yeah.":
            $ addPoint("bro", 1)

            scene s208a
            with dissolve

            u "Oh, hell yeah! She's super hot."

            scene s208b # cheeky smile
            with dissolve

            imre "Well that's what I like to hear, go on."

        "She's alright.":
            scene s208a
            with dissolve

            u "She's alright I guess."

            scene s208b
            with dissolve

            imre "Well that usually means she's better in bed 'cause she tries harder, go on."

    if costumeaubrey:
        scene s208c
        with dissolve

        u "Anyways, then I went costume shopping for Mr. Lee's class with Aubrey."

        scene s208d
        with dissolve # Imre pointer ifnger up and mouth open

        u "And before you ask, yes, she's hot."

        if caughtpeekingaubrey:
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

        if caughtpeekingpenelope:
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
    stop music fadeout 2.0
    scene clock2
    with fade

    play sound "sounds/clock2.mp3"

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

    play sound "sounds/lock.mp3"

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
            $ addPoint("tm", 1)

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
            $ addPoint("bf", 1)

    scene s216c # cl grabs volleyball
    with fade

    cl "You know, I used to play volleyball in high school, you up for a challenge?"

    scene s216d
    with dissolve

    u "Bring it on."

    scene s217 # chloe behind volleyball net
    with fade
    play sound "sounds/volley3.mp3"

    scene s217f
    with dissolve
    play sound "sounds/volley1.mp3"

    pause 0.5

    scene s217a
    with dissolve
    play sound "sounds/volley2.mp3"

    pause 0.5

    scene s217e
    with dissolve

    play sound "sounds/volley4.mp3"

    pause 0.5

    scene s217c
    with dissolve

    play sound "sounds/volley3.mp3"

    pause 0.5

    scene s217d
    with dissolve

    play sound "sounds/volley1.mp3"

    pause 0.5

    scene s217b
    with dissolve

    play sound "sounds/volley2.mp3"

    ############ volleyball scene with sounds

    scene s218 # volleyball over the next in the air, perfect for you to smash
    with dissolve

    menu:
        "Win the game":
            $ addPoint("tm", 1)

            # volleybal hit sounds

            scene s218a # you hitting the volleyball
            with vpunch

            play sound "sounds/volleyhit.mp3"

            pause 0.5

            ## volleyball floor sound

            scene s218b # ball hitting the floor next to chloe
            with dissolve

            play sound "sounds/volleyimp.mp3"

            pause 0.5


            scene s219 # closeup of chloe disappointed
            with dissolve

            cl "Oh no, it was so close!"

            scene s219a
            with dissolve

            u "I'm sure you'll get me next time."

        "Let her win":
            $ addPoint("bf", 1)

            scene s218c # you missing the ball
            with vpunch
            play sound "sounds/volleyhit.mp3"

            pause 0.5

            ## volleyball floor sound

            scene s219b # chloe arms in the air celebrating
            with dissolve

            cl "Yaaay, I won!"

            scene s219c
            with dissolve

            u "Oh I'll get you next time."

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

    stop music fadeout 2.0

    play sound "sounds/olddoor.mp3"

    # Door sound

    scene s220c # chloe in shockc face
    with dissolve

    "*Metal Door Sound*"

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

    play sound "sounds/switch.mp3"
    scene s223c # security out, lights off

    "*Click*"

    scene s222b
    with dissolve

    u "Wow, that was close."

    stop music fadeout 2.0

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

    stop music fadeout 2.0

    scene s225  #Showing you in bed
    with Fade (2,0,2)

    pause 1.0

    show screen fantasyOverlay

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

    image glitch = ("images/glitch.webp")

    pause 0.5

    show glitch
    play sound "sounds/glitch.mp3"

    pause 0.1

    hide glitch

    scene s228a # your door at night
    with hpunch ## GLITCH TRANSITION

    play sound "sounds/doorbell.mp3"

    "*Doorbell rings*"

    scene s228b
    with dissolve

    pause 0.5

    scene s229
    with dissolve

    pause 0.5

    play sound "sounds/dooropen.mp3"
    scene s230 # you open door and i's emily at night crying
    with dissolve

    u "Emily? It's 2 am, what are you doing here? I thought you were at your friend's birthday party?"

    scene s230a # emily crying
    with dissolve

    em "[name], I did something bad."

    show glitch
    play sound "sounds/glitch.mp3"

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

    hide screen fantasyOverlay

    stop music fadeout 2.0

    scene s225a # you open your eyes
    with flash

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
            $ addPoint("bro", 1)

            scene s240
            with dissolve

            pause 0.5

            play sound "sounds/ks.mp3"

            scene s240d # you doing complicated kick
            with vpunch



            pause 0.2

            scene s240d2 # you on the floor
            with dissolve

            pause 0.2

            scene s240e # you on the floor
            with vpunch

            play sound "sounds/fall.mp3"

            pause 0.5

            scene s241
            with dissolve

            imre "*Laughs* Great first move, flawless execution."

            imre "How about we start with the basics? Do you know how to throw a hook, jab and kick?"

            scene s241a
            with dissolve

            u "Uhm yeah, sure."

        "Stick to what you know":
            pass

    scene s240
    with dissolve

    pause 0.5

    play sound "sounds/ks.mp3"

    scene s240a
    with vpunch

    pause 0.5

    scene s240
    with dissolve

    pause 0.5

    play sound "sounds/ks.mp3"

    scene s240b
    with vpunch

    pause 0.5

    scene s240
    with dissolve

    pause 0.5

    play sound "sounds/ks.mp3"

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

    if evelynmove:

        scene s243 # evelyn working out
        with dissolve

        u "(Isn't that the cute store clerk from the costume shop?)"

        menu:
            "Approach her":
                $ addPoint("bro", 1)

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
                $ addPoint("bf", 1)

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

    imre "No, body shots. "

    imre "Hitting your opponent's body will leave them out of breath and in pain."

    imre "Perfect to get rid of a strong guard or a fast moving opponent."

    scene s248a
    with dissolve

    u "Alright. Show me how."

    scene s248e # Imre looking at the bag
    with dissolve

    imre "It's quite simple. Whenever your opponent leaves his torso open you simply use your left arm to throw a body hook."

    play sound "sounds/ks.mp3"

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

    play sound "sounds/ks.mp3"

    scene s249a
    with vpunch

    imre "Great job! Try it again."

    scene s249
    with dissolve

    pause 0.5

    play sound "sounds/ks.mp3"

    scene s249a
    with vpunch

    call screen popup5

    label popup5:

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
    
    play sound "sounds/vibrate.mp3"



# label aubrep12ab:
# $ contact_Aubrey.newMessage("My room has a window facing the backyard. Can you climb in through there instead of using the front door?")
# $ contact_Aubrey.newMessage("I'll leave it open.")
# $ contact_Aubrey.addReply("Uhm... sure.")
# call screen messager(contact_Aubrey)

    if costumeaubrey: # did you meet aubrey?

        if caughtpeekingaubrey: # did she catch you?

            if caughtpeekingaubreycounter: # did you talk your way out?
                jump talkedout

            else: # caught and she's mad
                $ contact_Aubrey.newMessage("I wanna talk about what happened yesterday.", queue=False)
                $ contact_Aubrey.newMessage("Any chance that you could come over now?")
                $ contact_Aubrey.addReply("Yeah, I can.")
                $ contact_Aubrey.newMessage("My room has a window facing the backyard. Can you climb in through there? I'll leave it open.")
                $ contact_Aubrey.newMessage("I'd prefer if none of the girls saw you.")
                $ contact_Aubrey.addReply("Uhm... sure.")

                label repeatk:
                    call screen phone
                    if contact_Aubrey.getReplies():
                        u "(I should probably check my phone.)"
                        jump repeatk

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

                stop music fadeout 2.0

                scene s252 # you in Aubrey's backyard looking at the house
                with Fade (1,0,1)

                u "(Okay, let's see. Which one's her room?)"

                play music "music/m4punk.mp3"

                u "(Oh no, the only open window is on the second floor.)"

                u "(Yeah, why would she want to mention that anyway...)"

                scene s253 ###### CLIMBING UP THE WINDOW SCENE
                with dissolve

                pause 0.5

                play sound "sounds/leaves.mp3"

                scene s253a
                with dissolve

                pause 0.5

                scene s253b
                with dissolve

                pause 0.5

                stop sound

                play sound "sounds/thud.mp3"

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

                menu:
                    "Take off your clothes":
                        $ addPoint("bf", 1)
                        $ addPoint("bro", 1)

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
                        $ addPoint("tm", 1)

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
                $ contact_Aubrey.newMessage("Hey, I really need your help.", queue=False)
                $ contact_Aubrey.newMessage("Any chance that you could come over now?")
                $ contact_Aubrey.addReply("Yeah, I'll be right there..")
                $ contact_Aubrey.newMessage("My room has a window facing the backyard. Can you climb in through there instead of using the front door?")
                $ contact_Aubrey.newMessage("I'll leave it open.")
                $ contact_Aubrey.addReply("Uhm... sure.")

                " "

                label repeatl:
                    call screen phone
                    if contact_Aubrey.getReplies():
                        u "(I should probably check my phone.)"
                        jump repeatl

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

                stop music fadeout 2.0

                scene s252 # you in Aubrey's backyard looking at the house
                with Fade (1,0,1)

                u "(Okay, let's see. Which one's her room?)"

                play music "music/m4punk.mp3"

                u "(Oh no, the only open window is on the second floor.)"

                u "(Yeah, why would she want to mention that anyway...)"

                scene s253 ###### CLIMBING UP THE WINDOW SCENE
                with dissolve

                pause 0.5

                play sound "sounds/leaves.mp3"

                scene s253a
                with dissolve

                pause 0.5

                scene s253b
                with dissolve

                pause 0.5

                stop sound

                play sound "sounds/thud.mp3"

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
                        $ addPoint("bf", 1)

                        jump da_a


                    "Dare":
                        $ addPoint("tm", 1)
                        $ addPoint("bro", 1)

                        jump da_b

                label da_a:

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

                label da_b:

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
        $ contact_Aubrey.newMessage("Hey, you know how you had to cancel on me yesterday and you really want to make it up to me?")
        $ contact_Aubrey.newMessage("Wanna come over now?")
        $ contact_Aubrey.addReply("Uhh... okay.", "aubrep12ab")
        
        label repeatm:
        label phoneu:

        if contact_Aubrey.messages[-1].replies:

            if not msgApp.notification:

                u "(I should really reply to Aubrey.)"

            else:

                u "(I should probably check my phone.)"



            jump repeatm

        else:
            

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

            stop music fadeout 2.0

            scene s252 # you in Aubrey's backyard looking at the house
            with Fade (1,0,1)

            u "(Okay, let's see. Which one's her room?)"

            play music "music/m4punk.mp3"

            u "(Oh no, the only open window is on the second floor.)"

            u "(Yeah, why would she want to mention that anyway...)"

            scene s253 ###### CLIMBING UP THE WINDOW SCENE
            with dissolve

            pause 0.5

            play sound "sounds/leaves.mp3"

            scene s253a
            with dissolve

            pause 0.5

            scene s253b
            with dissolve

            pause 0.5

            stop sound

            play sound "sounds/thud.mp3"

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

                    $ addPoint("bf", 1)
                    jump db_a


                "Dare":

                    $ addPoint("tm", 1)
                    $ addPoint("bro", 1)
                    jump db_b

            label db_a:

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

            label db_b:

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

    image aub1 = Movie (play="images/aub1.webm", loop = False, image = "images/aub1.webp", start_image = "images/aub1start.webp")
    image aub2 = Movie (play="images/aub2.webm", loop = True, image = "images/aub2.webp", start_image = "images/aub1.webp")
    image aub3 = Movie (play="images/aub3.webm", loop = False, image = "images/aub3.webp", start_image = "images/aub3start.webp")
    image aub4 = Movie (play="images/aub4.webm", loop = True, image = "images/aub4.webp", start_image = "images/aub4start.webp")
    image aub5 = Movie (play="images/aub5.webm", loop = False, image = "images/aub5.webp", start_image = "images/aub5start.webp")
    image aub7 = Movie (play="images/aub7.webm", loop = True, image = "images/aub7.webp", start_image = "images/aub7start.webp")
    image aub8 = Movie (play="images/aub8.webm", loop = False, image = "images/aub8.webp", start_image = "images/aub8start.webp")
    image asexnew1 = Movie (play="images/asexnew1.webm", loop = True, image = "images/asexnew1end.webp", start_image = "images/asexnew1start.webp")
    image asexnew2 = Movie (play="images/asexnew2.webm", loop = True, image = "images/asexnew2end.webp", start_image = "images/asexnew2start.webp")
    image asexnew3 = Movie (play="images/asexnew3.webm", loop = True, image = "images/asexnew3end.webp", start_image = "images/asexnew3start.webp")
    image asexnew4 = Movie (play="images/asexnew4.webm", loop = True, image = "images/asexnew4end.webp", start_image = "images/asexnew4start.webp")
    image asexnew5 = Movie (play="images/asexnew5.webm", loop = True, image = "images/asexnew5end.webp", start_image = "images/asexnew5start.webp")
    image asexnew6 = Movie (play="images/asexnew6.webm", loop = True, image = "images/asexnew4end.webp", start_image = "images/asexnew4start.webp")
    image asexnew7 = Movie (play="images/asexnew7.webm", loop = True, image = "images/asexnew5end.webp", start_image = "images/asexnew5start.webp")
    image asexnew9 = Movie (play="images/asexnew9.webm", loop = True, image = "images/asexnew8end.webp", start_image = "images/asexnew8start.webp")
    image asexnew10 = Movie (play="images/asexnew10.webm", loop = True, image = "images/asexnew8end.webp", start_image = "images/asexnew8start.webp")
    image asexnew11 = Movie (play="images/asexnew11.webm", loop = True, image = "images/asexnew11end.webp", start_image = "images/asexnew11start.webp")
    image asexnew12 = Movie (play="images/asexnew12.webm", loop = True, image = "images/asexnew11end.webp", start_image = "images/asexnew11start.webp")
    image asexnew13 = Movie (play="images/asexnew13.webm", loop = False, image = "images/asexnew13end.webp", start_image = "images/asexnew13start.webp")

    scene aub1start
    with dissolve

    menu:

        "Kiss her":
            $ aubreysex = True
            jump aubsexa

        "Stop it":
            $ aubreysex = False
            jump aubsexb


    label aubsexa:

    stop music fadeout 2.0
    play music "music/msexy.mp3"

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

    stop music fadeout 2.0

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

    play sound "sounds/kiss.mp3"

    scene s263 # kiss
    with dissolve

    pause 0.5

    scene s261
    with dissolve

    pause 0.5

    stop music fadeout 2.0

    scene s264 # you going back to your dorm
    with Fade (1,0,1)

    u "(I can't believe I just had sex with Aubrey... that was amazing.)"

    if laurenrs == True:

        u "(I wonder if Lauren would be upset if she knew. I guess I'll have to decide how honest I wanna be on our date tonight.)"


    jump aubsexad

    label aubsexb:

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

    stop music fadeout 2.0

    label aubsexad:


    pause 0.5

    play music "music/mchill1.mp3"

    queue music [ "music/mchill2.mp3"]


### Meet Lauren

    if laurenrs == False: # you're not dating Lauren

        scene s265 # lauren sitting in front of your door
        with dissolve

        u "Lauren? What are you doing here?"

        if meetlauren == True: # you've met lauren in the cafe
            if laawk == True:

                scene s266 # Lauren closeup awkward
                with dissolve

                la "Hey, uhm..."

                la "I'm here to ask you for a favor... as a friend."

                scene s266a
                with dissolve

                u "Uhm, okay... What is it?"

                jump continuen

            else:

                scene s266b # lauren closeup smiling
                with dissolve

                la "Heyyy. I need a favor."

                scene s266c
                with dissolve

                u "Alright, how can I help?"

                jump continueo

        else:


            scene s266 # Lauren closeup awkward
            with dissolve

            la "Hey, uhm... I know we haven't talked since the park."

            la "But I kinda need a favor... as a friend."

            scene s266a
            with dissolve

            u "Uhm, okay. What is it?"

            jump continuep
    else:

        jump continueq

    label continuen:
    label continueo:
    label continuep:

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


        "I'd love to.":

            $ addPoint("bf", 1)
            jump dc_a

        "I don't know...":

            $ addPoint("tm", 1)
            jump dc_b

    label dc_a:

        scene s268a
        with dissolve

        u "Yeah, I'd love to."

        jump dc_ad

    label dc_b:

        scene s268a
        with dissolve

        u "I don't know, Lauren. Sounds kinda weird."

        scene s268
        with dissolve

        la "[name], pleaaase. It's just answering a few questions."

        scene s268a
        with dissolve

        u "Okay, fine."

        jump dc_bd

    label dc_ad:
    label dc_bd:


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

    play sound "sounds/call.mp3"

    scene s270a2
    with dissolve

    pause 0.5

    scene s270a # you looking at your phone in your hand
    with dissolve

    u "Huh? Julia's calling me."

    menu:


        "Answer":
            stop sound
            play sound "sounds/answercall.mp3"

            $ addPoint("bf", 1)
            jump dd_a


        "Don't answer":
            stop sound
            play sound "sounds/rejectcall.mp3"

            $ addPoint("tm", 1)
            $ dontanswerjulia = True
            jump dd_b

    label dd_a:

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

            "Shopping sounds great.":

                $ meetjulia = True
                $ addPoint("bf", 1)
                jump de_a

            "I can't, sorry.":

                $ meetjulia = False
                $ addPoint("tm", 1)
                jump de_b

    label de_a:

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

        play sound "sounds/rejectcall.mp3"

        jump de_ad

    label de_b:

        u "Sorry, Julia... I'm really busy this weekend."

        scene s271a # Julia on the phone, a bit disappointed / sad
        with dissolve

        ju "Oh... okay, honey. Next time then."

        scene s270c
        with dissolve

        u "Yeah... next time."

        play sound "sounds/rejectcall.mp3"

        jump de_bd



    label dd_b:

        # phone call declined sound

        scene s270
        with dissolve

        $ notnowmom = True
        if not steam:
            image notnowmom = "images/notnowmom.webp"
            show notnowmom:
                xpos 0
                ypos -200
                linear 0.5 xpos 0 ypos 0
                pause 2.0
                linear 0.5 xpos 0 ypos -200
        else:
            $ achievement.grant("not_now_mom")
            $ achievement.sync()

        u "(I don't really feel like talking to her right now.)"

        jump continuer

    label continuer:
    label de_ad:
    label de_bd:





    scene s270
    with fade
    play sound "sounds/knock.mp3"

    # knock sound

    "*Knock knock knock*"

    scene s272 # showing you sitting on the side of bed pushing ready to stand up // camera angle to side of bed, looking at you from front
    with dissolve

    u "(I guess there goes my one minute of alone time...)"

    play sound "sounds/dooropen.mp3"

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

            $ addPoint("bf", 1)
            jump df_a

        "Agree with Ryan":

            $ addPoint("bro", 1)
            jump df_b


    label df_a:

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

        jump df_ad

    label df_b:

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

        jump df_bd

    label df_ad:
    label df_bd:

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

    stop music fadeout 2.0

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

            $ addPoint("tm", 1)
            jump dg_a

        "Walk away":

            $ addPoint("bro", 1)
            jump dg_b

    label dg_a:

    u "Cause you were too fucking pussy to do it yourself."

    scene s275e
    with dissolve

    ry "Fuck you! I looked after you, I brought you home!"

    ry "Chloe is playing you! Like she played Grayson! Don't fucking fall for it."

    scene s275f
    with dissolve

    u "You don't know Chloe at all! You're just fucking jealous!"


    label dg_b:

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

    stop music fadeout 2.0

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


    ri "So what's going on between you and Chloe? She's the president of the Chicks, right?"

    menu:



        "I like her":

            $ rileykiss = False
            $ addPoint("bf", 1)
            jump dh_a


        "She's into me.":

            $ addPoint("tm", 1)
            jump dh_b

    label dh_a:

    scene s281a
    with dissolve

    u "Yeah, we met at the Apes' rush party and I really like her."

    u "We haven't done anything yet, but I feel like we really have a connection, you know?"

    scene s281b # riley a bit dissappointed
    with dissolve

    ri "Oh uhm... yeah, that sounds really good. I'm happy for you."


    jump dh_ad

    label dh_b:

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

            $ rileykiss = True
            $ addPoint("tm", 1)
            jump dj_a

        "Don't kiss her":

            $ addPoint("bf", 1)
            $ rileykiss = False
            jump dj_b



    label dj_a:

    image rikiss2 = Movie (play="images/rikiss.webm", loop = False, image = "images/rikiss.webp", start_image = "images/rikiss.webp")

    show rikiss2

    $ lipsdontlie = True
    if not steam:
        image lipsdontlie = "images/lipsdontlie.webp"
        show lipsdontlie:
            xpos 0
            ypos -200
            linear 0.5 xpos 0 ypos 0
            pause 2.0
            linear 0.5 xpos 0 ypos -200
    else:
        $ achievement.grant("lips_dont_lie")
        $ achievement.sync()

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

    jump dj_ad

    label dj_b:

    ri "Just a really great guy."

    scene s281e

    u "Thanks, Riley."

    jump dj_bd


    label dh_ad:
    label dj_ad:
    label dj_bd:

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

    stop music fadeout 2.0


    if laurenrs == True: #LAUREN MOVIES

        play music "music/mindie2.mp3"

        scene s282  ## later that day transition pic
        with Fade (1,0,1)

        u "(I can't believe I'm finally going on a real date with Lauren...)"

        u "(I better not fuck this up.)"


        scene s284 # Knocking on lauren's dorm
        with Fade (1,0,1)
        play sound "sounds/knock.mp3"

        "*Knock knock knock*"

        play sound "sounds/dooropen.mp3"

        scene s285 # Lauren oppens the door smiling
        with dissolve

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



        if aubreysex == True:

            scene s287a # lauren closeup while walking her mouth closed  FIRST PERSON
            with dissolve
            u "(Okay, time to make a decision. Should I tell her about what happened with Aubrey?)"

            menu:



                "Tell her what happened.":

                    $ toldlauren = True
                    $ addPoint("bf", 1)
                    $ laurenrs = False
                    jump dk_a

                "Don't tell her.":

                    $ toldlauren = False
                    $ addPoint("tm", 1)
                    jump dk_b

        else:
            $ toldlauren = False
            jump dk_bb

        label dk_a:

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

            $ truthhurts = True
            if not steam:
                image truthhurts = "images/truthhurts.webp"
                show truthhurts:
                    xpos 0
                    ypos -200
                    linear 0.5 xpos 0 ypos 0
                    pause 2.0
                    linear 0.5 xpos 0 ypos -200
            else:
                $ achievement.grant("truth_hurts")
                $ achievement.sync()

            u "(Fuck me... I guess that's what honesty gets you.)"

            jump dk_ad


        label dk_b:

        u "(Lauren seems to value loyalty, she might be upset if she finds out and I don't wanna ruin our date before it even started.)"

        label dk_bb:

        scene s287a # lauren closeup while walking her mouth closed  FIRST PERSON
        with dissolve

        u "Uhm... I went picnicking with Riley and Ryan. What about you?"

        scene s287
        with dissolve

        la "Mostly studying, I'm glad to finally do something exciting."

        scene s287a
        with dissolve

        u "I'll make sure this date won't disappoint then."

        stop music fadeout 2.0

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
        play sound "sounds/horrorsound.mp3"

        scene s289b # lauren grabs onto your arm scared
        with dissolve

        la "*Squeals*"

        scene s289c # Looking at lauren  you smiling
        with dissolve

        u "*Whispers* Now look who's getting scared."

        scene s289d # lauren smiling flirty back getting her face closer to yours
        with dissolve


        la "*Whispers* I was just making sure you're safe."

        menu:



            "Kiss her":

                $ laurenkissb = True
                jump dl_a

            "Continue watching":

                $ laurenkissb = False
                jump dl_b

        label dl_b:

        scene s290c
        with dissolve

        pause 0.5

        scene s290e # Lauren looking back at the movie screen with cute expression
        with dissolve

        pause 0.5

        jump dl_bd


        label dl_a:

        scene laurenkiss2 #self explanatory, same camera as s289
        with dissolve

        pause 2.0




        menu:

            "Reach under her skirt":

                $ addPoint("tm", 1)
                jump dm_a

            "Keep hands to yourself":

                $ addPoint("bf", 1)
                jump dm_b

        label dm_a:

        scene s291a # same camera angle but your hand is under her skirt
        with dissolve

        pause 0.5

        la "[name], I don't think I want to do this."


        menu:


            "Keep going":

                $ addPoint("tm", 1)
                $ laurentoofar = True
                $ laurenrs = False
                jump dn_a


            "Stop":

                $ addPoint("bf", 1)
                jump dn_b


        label dn_a:

        scene s291b # your hand moves further up
        with dissolve

        pause 0.5

        scene s290f # lauren horny face
        with dissolve

        la "*Moans quietly*"

        stop music fadeout 2.0

        play sound "sounds/slap.mp3"


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

        jump dn_ad


        label dn_b:

        scene s290b
        with dissolve

        la "Thank you, I just need some time."

        pause 0.5

        scene s290e # Lauren looking back at the movie screen with cute expression
        with dissolve

        pause 0.5

        jump dn_bd


        label dm_b:

        pause 1.0

        scene s290c
        with dissolve

        pause 0.5

        scene s290e # Lauren looking back at the movie screen with cute expression
        with dissolve

        pause 0.5

        jump dm_bd

    ##### after movie
        label dn_bd:
        label dm_bd:
        label dl_bd:

        stop music fadeout 2.0

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

        play sound "sounds/dooropen.mp3"

        scene s293d2 # lauren entering
        with dissolve

        pause 0.5

        scene s293d # lauren opens the door and steps forward one step
        with dissolve

        la "Good night, [name]."

        scene s293e
        with dissolve

        u "Yeah, good night, Lauren."

        play sound "sounds/doorclose.mp3"

        # door close sound

        scene s293g # door shut in front of you
        with dissolve

        pause 0.5

        stop music fadeout 2.0


        jump continuet




    else:

        scene s282a  ## you in your dorm: It's the same day but It's nighttime now on laptop
        with Fade (1,0,1)

        stop music fadeout 2.0


        pause 1


        jump continues

    label dk_ad:
    label dn_ad:
    label continuet:

    stop music fadeout 2.0


    scene s282b  ## you in your dorm: later that night on your laptop
    with Fade (1,0,1)

    pause 1

    label continues: # This is after the date


    play music "music/horror2.mp3"


    play sound "sounds/call.mp3"

    scene s294 # phone on table unknown number
    with dissolve

    u "(Huh, who would call me this late?)"

    stop sound

    play sound "sounds/answercall.mp3"

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

    stop music fadeout 2.0




    ############# V0.3 END

    play music "music/m4punk.mp3"

    scene s296 #Imre in the hospital bed heavily bruised laying under blanket showing you as well coming into his room
    with Fade (1,0,1)

    u "Imre? How you holding up buddy?"

    scene s297 # imre on light painkiller closeup FIRST PERSON serious look
    with dissolve

    imre "Hey, I'm fine. *winces in pain*"

    scene s297a
    with dissolve

    u "The nurse said you had 3 broken ribs! What the hell happened?"

    scene s297
    with dissolve

    imre "Well I was hitting on this girl but she wasn't really into talking so I just started grinding on her a bit."

    imre "Then all of the sudden... *winces in pain* this dude shows up super mad and starts pushing me around."

    scene s297b # slight smile in pain
    with dissolve
    imre "Turns out that it was Adam and I was grinding on his sister."

    scene s297c
    with dissolve

    u "Who's Adam?"

    scene s297
    with dissolve

    imre "My brother asked some of his friends in the Wolves... *winces in pain*"

    imre "And apparently Adam used to be an Ape, but last year one of his opponents wouldn't give up so he flipped and gouged his opponent's eyes."

    imre "*winces in pain* He was immediately disqualified and kicked out of the Apes."

    imre "Anyways, I obviously pushed him back and told to fuck off and then we got into a bit of a fight."

    scene s297a
    with dissolve

    u "A bit of a fight? You have three broken ribs..."

    scene s297d # imre mad
    with dissolve
    imre "Yeah whatever... *winces in pain* he caught me by surprise, it wasn't a fair fight."


    menu:


        "You should be more careful.":

            $ addPoint("bf", 1)
            jump do_a

        "Let's fuck him up.":

            $ addPoint("bro", 1)
            $ addPoint("tm", 1)
            $ revengeadam = True
            jump do_b


    label do_a:

    scene s297a
    with dissolve

    u "Imre, you need to be more careful, man!"

    u "You can't just try and fight everyone, what if he had a knife?"

    scene s297d
    with dissolve

    imre "I told you, it wasn't a fair fight! I'll fuck him up when I get out."

    menu:

        "Let me help.":

            $ revengeadam = True
            $ addPoint("bro", 1)
            jump dp_a

        "That's a dumb idea.":

            $ revengeadam = False
            $ addPoint("bf", 1)
            jump dp_b

    label dp_a:

    scene s297a
    with dissolve

    u "At least let me help you."

    scene s297
    with dissolve

    imre "Nah, this is my fight *winces in pain*."

    imre "If you wanna help, pick me up when I get out of here."

    scene s297a
    with dissolve

    u "The nurse said you need to stay in here for two more days so I'll pick you up on Sunday, alright?"

    scene s297
    with dissolve

    imre "Alright, player. *winces in pain*"

    scene s297a
    with dissolve

    u "I'll see you then, get better soon."

    jump dp_ad

    label dp_b:

    scene s297a
    with dissolve

    u "Dude, that's a dumb idea. He sounds dangerous, just go to the cops!"

    scene s297d
    with dissolve

    imre "I'll fuck him up myself! *winces in pain* Or do I look like a bitch to you?"

    scene s297a
    with dissolve

    u "No, just think about it, okay?"

    u "The nurse said you'd be in here for two more days. I'll pick you up on Sunday alright?"

    scene s297
    with dissolve

    imre "Alright, player. *winces in pain*"

    scene s297a
    with dissolve

    u "I'll see you then, get better soon."

    jump dp_bd

    label do_b:

    scene s297a
    with dissolve

    u "Fuck that guy, let's fuck him up!"

    scene s297
    with dissolve

    imre "Nah, this is my fight *winces in pain*."

    imre "I'll be okay... but could you pick me up when I get out?"

    scene s297a
    with dissolve

    u "Yeah of course, the nurse said you need to stay in here for two more days so I'll come back on Sunday, alright?"

    scene s297
    with dissolve

    imre "Alright, player. *winces in pain*"

    scene s297a
    with dissolve

    u "I'll see you then, get better soon."

    jump do_bd



    label dp_bd:
    label do_bd:
    label dp_ad:

    stop music fadeout 2.0



    scene s298 # shows a cab in the night from outside with you in the back possibly not seeing you due to dark windows
    with Fade (1,0,1)

    pause 0.5

    play music "music/mindie1.mp3"

    queue music [ "music/mindie2.mp3", "music/mindie3.mp3" ]

    scene s299 # you sititng in the back of the cab contemplating
    with dissolve

    u "(Holy fuck... I'm just glad he's okay. I need to talk to someone about this.)"

    u "(Riley's quite close with Imre, I'll call her.)"

    scene s299b # you on the phone mouth closed
    with dissolve

    play sound "sounds/calling.mp3"

    "*Phone calling*"

    stop sound

    scene s299b
    with dissolve

    ri "Hey [name], why you calling me so late?"
    ri "You know that booty calls nowadays aren't actually calls, people just text."

    scene s299c #you  mouth open
    with dissolve

    u "Riley, Imre's in the hospital. He got beat up and has three broken ribs."

    scene s299b
    with dissolve

    ri "What the hell?! Will he be okay?"

    scene s299c
    with dissolve

    u "Yeah, he's holding up. I'm just on my way back from the hospital. He has to stay there for two more days."

    u "The nurse said he's lucky there was no internal bleeding."

    scene s299b
    with dissolve

    ri "Oh my god... Let me know when you're back at your dorm. I'll come over straight away if you wanna talk about it."

    scene s299c
    with dissolve

    u "Yeah, okay. I won't be able to sleep right now anyway."

    scene s299d # you with out phone looking towards the front of the car
    with fade

    u "Here's good, thank you."

    scene s299e # ssame as 290d but mouth closed
    with dissolve

    uber "Please don't forget to rate me five stars if you enjoyed your journey."

    scene s300 # you in your dorm waiting for Riley to come
    with Fade (1,0,1)

    play sound "sounds/knock.mp3"

    "*Knock knock knock*"

    pause 0.5

    play sound "sounds/dooropen.mp3"


    scene s301 # Showing you from the back looking over your shoulder in front of open door with Riley standing outside sad
    with dissolve

    u "Hey..."

    scene s301a # riley hugging you strongly with her arms around your throat not torso (like she jumped onto you kinda)
    with dissolve

    ri "Hey, I still can't believe this happened."

    scene s301b # riley stops hugging you, stands right in front of you
    with dissolve

    u "Yeah, me neither..."

    scene s302 # riley and you walking over to the bed, bed is in the frame
    with dissolve

    u "He gets out on Sunday. If you want to, you can come with me when I pick him up."

    scene s302a # Riley and you sitting down on the bed, riley sad smile
    with dissolve

    ri "Of course."

    scene s303 # close up of Riley sad smile
    with dissolve

    ri "Imre said you started training with him..."

    ri "Does that mean I'll have to visit both of you in the hospital soon?"

    scene s303a
    with dissolve

    u "Come on Riley, you know I don't get mad as easily as Imre... it's just for self-defense."

    scene s303b #Riley concerned, embarrassed
    with dissolve

    ri "I mean you did seem quite angry at the park today..."


    menu:


        "Take responsibility":

            $ addPoint("bro", 1)
            $ addPoint("bf", 1)
            jump dq_a

        "Blame Ryan":

            $ addPoint("tm", 1)
            jump dq_b

    label dq_a:

    scene s303c
    with dissolve

    u "Yeah... I'm sorry. I shouldn't have acted out like that. Tomorrow I'll talk to Ryan and make things right."

    scene s303
    with dissolve

    ri "I think that'd be good."

    scene s303a
    with dissolve

    jump dq_ad

    label dq_b:

    scene s303c
    with dissolve

    u "That's just 'cause Ryan was completely out of line..."

    scene s303b
    with dissolve

    ri "Right... sorry for bringing it up."

    scene s303c
    with dissolve

    jump dq_bd

    label dq_ad:
    label dq_bd:

    u "Hey, isn't it kinda crazy that we all just met at the beginning of the week?"

    u "I mean so much has happened since then."

    scene s303d # Riley slight real smile without sadness no teeth, slight chance in hand position so it looks like more than her face is changing and the scene isnt boring
    with dissolve

    ri "Yeah, you're not wrong. That first night where we played truth or drink."

    scene s303e
    with dissolve

    u "You know, that night, Imre told me he wanted to get with you."

    scene s303d
    with dissolve

    ri "Oh reeeally?"

    scene s303e
    with dissolve

    u "Did you guys ever...?"

    scene s303f # Riley leans slightly back hand on chest like she's a bit perplexed by the question cheeky smile with one eyebrow raised
    with dissolve

    ri "Me and Imre? No."

    scene s303g # same as 303f but mouth closed
    with dissolve

    u "Would you ever...?"

    scene s303d
    with dissolve

    ri "Uhm... no, I don't think so. I like Imre, but he can be a bit gross, haha."


    if rileykiss == True:

        scene s303e
        with dissolve

        u "Haha, I get that. I'm a better kisser anyway."

        scene s303d
        with dissolve

        ri "Oh, so you've tried him?"

        scene s303e
        with dissolve

        u "Hey, that's not what I-"

        scene s303d
        with dissolve

        ri "I'm just kidding, haha."

        jump continueu

    else:

        scene s303e
        with dissolve

        u "Haha, good."

        scene s303d
        with dissolve

        ri "Good?"

        scene s303e
        with dissolve

        u "Uhm... you know, good for you that you made that decision."

        scene s303d
        with dissolve

        ri "Right..."

        jump continuev


    label continueu:
    label continuev:

    ri "It's getting quite late, I should probably head back to my dorm."

    menu:

        "Ask her to sleep here":

            jump dr_a


        "Don't ask":

            jump dr_b

    label dr_a:

        scene s304 # showing you sitting on bed, riley stood up, you looking at her, she's walking towards the door but still close to the bed
        with dissolve

        u "Or... you could sleep here. I mean, Imre's bed certainly isn't taken tonight."

        scene s304a # riley turning around smile
        with dissolve

        ri "Haha, I don't wanna find out what's underneath those covers."

        jump dr_ad


    label dr_b:

        scene s304
        with dissolve

        u "Yeah, thank you for coming though."

        scene s304a
        with dissolve

        ri "Not a problem at all."

        jump dr_bd

    label dr_ad:
    label dr_bd:
    stop music fadeout 2.0



    ######### CHLOE DREAM:

    scene s225 # already in the game, no need to render again
    with Fade (1,0,1)

    pause 0.5
    play music "music/mhorror.mp3"

    show screen fantasyOverlay

    scene s305 # Chloe closeup, she looks cute moutth clsoed, background should be wishy washy
    with flash

    u "Chloe, you are the most amazing girl I've ever met."

    u "You're funny, you're beautiful, you're kind..."

    u "We get along so well... I-"

    u "I really like you. Do you feel the same way?"

    scene s305a # chloe surpised laughing at you, like she cant bleeive you just said that in an evil way
    with dissolve

    cl "What?? Hahahaha!"

    cl "Did you really think a girl like me would ever go for a guy like you?!"

    scene s305b # chloe turning her head like she's talking to others you cant see in frame
    with dissolve

    cl "Guys, look at this loser!"

    scene s306 # Grayson laughing at you
    with dissolve

    gr "HAHAHA! This fucking idiot really fell for it!"

    u "What? I don't understand..."

    scene s307 # Ryan laughing at you
    with dissolve

    ry "[name], how could you ever think Chloe likes you?? Hahaha!"

    scene s308 #Riley laughing at you
    with dissolve

    ri "Everyone could see it. She was playing you! How could you be so blind?!"

    scene s309 # showing You hands to your head,screaming
    with dissolve

    u "Ahhh! Stop! Stop!"

    hide screen fantasyOverlay

    stop music fadeout 2.0

    scene s225a # already in the game, no need to render again
    with flash

    u "*Breathing heavily*"

    u "(What the hell was that dream? Ryan really made me second guess how things are going with Chloe.)"

    u "(I should talk to her tomorrow.)"

############## END CHLOE DREAM



########## NEXT MORNING (SATURDAY)

    scene s310 # you yawning in bed in the morning
    with Fade (1,0,1)

    u "*Yawn*"

    if meetjulia == True:

        play music "music/m11punk.mp3"

        scene s310a # no logner yawning
        with dissolve

        u "(Julia said she was gonna pick me up soon, I should head to the parking lot.)"

        scene s312 #you sitting on curb at parking lot
        with Fade (1,0,1)

        pause 0.5

        scene s312a # Tip of Julias car pulling in, same frame as before
        with fade

        play sound "sounds/carbrake.mp3"

        pause 0.5

        scene s314 # Julia getting out of the car
        with dissolve

        pause 0.5

        play sound "sounds/cardooropen.mp3"
        scene s314a # Julia getting out of the car
        with dissolve

        pause 0.5

        scene s315 # Julia close up shocked
        with dissolve

        ju "Oh my god, honey! What happened to your eye??"

        menu:


            "Someone punched me.":

                $ addPoint("bf", 1)
                $ liejulia = False
                jump du_a

            "It was an accident.":

                $ addPoint("tm", 1)
                $ liejulia = True
                jump du_b

        label du_a:

        scene s315a
        with dissolve

        u "I was at a party and some guy punched me out of nowhere."

        u "It's okay though. You don't need to worry."

        scene s315b # julia empathy
        with dissolve

        ju "Oh honey, that's horrible! Have you told the college? I don't want you to feel unsafe."

        scene s315c
        with dissolve

        u "No, it's fine. My roommate's actually been teaching me self-defense."

        scene s315b
        with dissolve

        ju "Well that's nice of him... I just hope you never have to use it."

        scene s315c
        with dissolve

        u "Please don't worry, Julia. It was just a one time thing."

        scene s315d # Julia emphatic smile
        with dissolve

        ju "Okay honey, let's go shopping then."

        jump du_ad

        label du_b:

        scene s315a
        with dissolve

        u "I was playing volleyball with some friends and got hit be the ball when I wasn't looking."

        scene s315b # julia empathy
        with dissolve

        ju "Oh honey, that volleyball must have been made out of steel."

        scene s315c
        with dissolve

        u "It was just a bit unfortunate, no big deal. It doesn't hurt much."

        scene s315d # Julia emphatic smile
        with dissolve

        ju "Well that's a relief. Let's go shopping then."

        jump du_bd

        label du_ad:
        label du_bd:
        stop music fadeout 2.0



        ######### THE FOLLOWING IMAGES HAVE TO BE RENDERED WITH NOT BACKGROUND AS A VIDEO OF MOVING ROADS WILL BE INSERTED

        image s316 = "images/s316.webp" # Julia looking forward talking smiling
        image s316a = "images/s316a.webp" # Julia looking forward talking smiling mouth closed
        image s316c = "images/s316c.webp" # Julia looking forward curious
        image s316d = "images/s316d.webp" # Julia looking forward curious mouth closed
        image s316b = "images/s316b.webp" # Julia looking at you smiling mouth open






        scene carback
        show s316
        with Fade (1,0,1)
        play music "sounds/driving1.mp3"

        ju "Sooo... have you met any girls yet?"

        hide s316
        show s316a
        with dissolve

        u "Yeah, a couple."

        hide s316a
        show s316b
        with dissolve

        ju "So is there anyone you like in particular?"

        hide s316b
        show s316a
        with dissolve

        u "Uhm... yeah."

        call screen girls

        label juchloe:


        $ girl = "Chloe"

        u "There's this girl called Chloe..."

        u "A couple nights ago we went to the gym at midnight just to play volleyball, it was super fun."

        u "It's just uhm... never mind."


        hide s316a
        hide s316d
        show s316c
        with dissolve

        ju "What is it, honey? You know you can always talk to me."

        hide s316c
        show s316d
        with dissolve

        u "Just my friend said some bad stuff about her and I don't know what to believe."

        hide s316d
        show s316
        with dissolve

        ju "Well have you talked to her about it?"

        hide s316
        show s316a
        with dissolve

        u "Not yet, but I'll ask her if we can talk today."

        hide s316a
        show s316b
        with dissolve

        ju "I think that's a good idea. I'm sure you'll figure it out."

        hide s316b
        show s316a
        with dissolve

        u "Thanks, Julia."



        jump jucona


        label juaubrey:

        $ girl = "Aubrey"

        u "There's this girl called Aubrey..."

        u "She's really fun and kinda wild. She just does stuff you wouldn't expect."

        jump juconb

        label julauren:

        $ girl = "Lauren"

        u "There's this girl called Lauren..."

        u "She's really sweet, but also funny."

        jump juconc

        label juriley:

        $ girl = "Riley"

        u "There's this girl called Riley..."

        u "She's fun, but also really honest and that makes her great to talk to."

        jump jucond

        label juemily:


        $ girl = "Emily"

        u "Actually, it's Emily..."

        hide s316a
        show s316c
        with dissolve

        $ relightthefire = True
        if not steam:
            image relightthefire = "images/relightthefire.webp"
            show relightthefire:
                xpos 0
                ypos -200
                linear 0.5 xpos 0 ypos 0
                pause 2.0
                linear 0.5 xpos 0 ypos -200
        else:
            $ achievement.grant("relight_the_fire")
            $ achievement.sync()

        ju "Emily? I thought you guys broke up?"

        hide s316c
        show s316d
        with dissolve

        u "Yeah, but I think she's changed. She seems to be really sorry for what she did."

        u "I don't know... we just get along so well."

        jump jucone

        label jupenelope:

        $ girl = "Penelope"

        u "There's this girl called Penelope..."

        u "She's a little quirky, but I really like that about her. It's different."

        jump juconf

        label juconb:
        label juconc:
        label jucond:
        label jucone:
        label juconf:

        hide s316a
        hide s316d
        show s316
        with dissolve

        ju "Aww honeeey! That sounds great, I'm really happy for you."

        hide s316
        show s316a
        with dissolve

        u "Thanks, Julia."

        label jucona:
        stop music fadeout 2.0


        scene s317 # you and julia at the start of clothing store there are some people there.
        with Fade (1,0,1)

        play music "music/m16punk.mp3"
        queue music [ "music/mchill1.mp3", "music/m7punk.mp3" ]

        ju "You know, I haven't been shopping in quite some time, this is gonna be fun."

        scene s318 #FIRST PERSON: Julia close up smiling looking at you
        with dissolve

        ju "If you find something you like, just let me know, I'll pay for it. I know how tight money can be as a student."

        scene s318a
        with dissolve

        u "You don't have to do that..."

        scene s318
        with dissolve

        ju "It's fine, honey. You wouldn't believe all the things I did for money when I was a student."

        ju "Let's go find you some nice clothes."

        scene s319 # FIRST PERSON Julia looking at clothes, Julia maybe holding onto one particular shirt // MAKE SURE THERE'S A SIMILAR LOOKING SHIRT TO TRY ON DOG
        with fade

        ju "What do you think of this one, honey?"

        # anchor

        scene s319a
        with dissolve

        u "Yeah, I like it."

        scene s319b
        with dissolve

        ju "How about you try it on and if I find anything else nice I'll bring it to you?"

        scene s319a
        with dissolve

        u "Okay, sure."

        scene s320 # You by yourself in a changing room with out shirt, just about to put on the new shirt
        with fade

        pause 0.5

        play sound "sounds/knock.mp3"

        "*Knock knock knock*"

        scene s320a # you turn around to look at door
        with dissolve

        ju "Honey, you in there?"

        scene s321# FIrst person: looking at closed changing room door
        with dissolve

        u "Yeah, just wai-"



        scene s321a # julia coming thorugh
        with dissolve

        ju "I found you a nice sweater that you might like."

        scene s321b # julia inside door closed now
        with dissolve

        u "Uhm.. thanks."

        scene s322 # showing you reaching for shirt to try on I guess? and julia
        with dissolve

        u "You didn't even leave me time to try this one on though."

        scene s322a #julia mouth open smiling as if it was obvious
        with dissolve

        ju "Well do it now, I wanna see what it looks like on you."

        scene s322b # julia feeling your biceps
        with dissolve

        ju "You've put on a bit of muscle, honey."

        scene s322c # julia puts her arm away
        with dissolve

        u "Uhm... thanks."

        scene s323 # Julia close up  FIRST PERSON, she looks at your torso smiling
        with fade

        ju "Wow, it looks great! What do you think, honey?"

        scene s323a # julia looking back at your face mouth closed
        with dissolve

        u "Yeah, it looks good. It's just a bit tight around the neck."

        scene s323b # julia know it better smile
        with dissolve

        ju "That's because you didn't adjust the collar correctly."

        scene s323c # julia arms on your collar
        with dissolve

        ju "Here, let me help you."

        scene s323d # her arm moves slightly
        with dissolve

        ju "How's that?"

        scene s323a
        with dissolve

        u "Yeah, that's better. Thanks."

        scene s323b
        with dissolve

        ju "Okay, I'm gonna look around some more. Let me know when you're ready to buy something."

        scene s323a
        with dissolve

        u "Alright."

        scene s324 # FIRST PERSON: Julia form the side looking through clothes
        with fade

        u "Julia, you ready to go?"


        scene s325 #you and Julia walking through mall
        with fade

        pause 0.5

        if girl == "Chloe":

            scene s325a # julia points at shop window with cool volleyball
            with dissolve

            ju "Honey, didn't you say you played volleyball with uhh... Chloe, was it?"

            scene s326 #close up of Volleyball
            with dissolve

            ju "Wouldn't that make a great gift for her?"


            menu:


                "Buy it":

                    $ volleyball = True
                    jump dv_a

                "Don't buy it":

                    $ volleyball = False
                    jump dv_b

            label dv_a:

            $ rematch = True
            if not steam:
                image rematch = "images/rematch.webp"
                show rematch:
                    xpos 0
                    ypos -200
                    linear 0.5 xpos 0 ypos 0
                    pause 2.0
                    linear 0.5 xpos 0 ypos -200
            else:
                $ achievement.grant("rematch")
                $ achievement.sync()

            u "Yeah, you're right. Maybe I could give it to her when we talk about what Ryan said."

            ju "That's a great idea, honey."

            jump dv_ad

            label dv_b:

            u "Uhm... I don't know. I wanna talk to her about what Ryan said first."

            ju "Alright, honey. It was just an idea."


            jump dv_bd

        else:

            scene s325b # you lookign at shop window with cool volley
            with dissolve

            u "(Chloe would probably love this volleyball.)"

            scene s326
            with dissolve



            menu:

                "Buy it":

                    $ volleyball = True
                    jump dv_c

                "Don't buy it":

                    $ volleyball = False
                    jump dv_d

        label dv_c:

        u "Hold up, Julia. I wanna buy this volleyball as gift for... a friend."

        ju "Alright, honey."

        jump dv_cd

        label dv_d:

        u "(I should probably talk to her about what Ryan said first and clear things up.)"

        jump dv_dd

        label dv_ad:
        label dv_cd:

        scene s327 # FIRST PERSON inside shop talking to cashier with volleyball on the cash register thing
        with fade

        clerk "Hey there, would you like a bag with that?"

        scene s327a # shop clerk scanning ball
        with dissolve

        u "No, it's fine, thanks. Can I pay by card, please."
        scene s327a2
        with dissolve

        clerk "That's $10.90, please."

        scene s327b # shop clerk looking down mouth closed (to where your scanning card would be)
        with dissolve

        pause 1.0

        scene s327a2
        with dissolve

        clerk "Thank you. Have a nice day."

        jump dv_add

        label dv_add:
        label dv_dd:
        label dv_bd:

        scene s328 # Showing you and Julia in the car driving back
        with Fade (1,0,1)

        pause 0.5

        scene s329 # you talking to juliaa (very close, about to hug)
        with Fade (1,0,1)

        ju "Thanks for coming along, honey. It was really nice to see you."

        scene s329a # hugging
        with dissolve

        u "Yeah Julia, it was fun. I'll see you again soon."

        jump continuew

    else:

        scene s310a
        with dissolve

        u "(Damn, I still need to finish my essay on transition slides...)"

        scene s311 # you working on your laptop at your desk transition slide : It's Saturday 1 pm
        with Fade (1,0,1)

        u "(Alright, all finished.)"

        jump continuex

    label continuew:
    label continuex:
    stop music fadeout 2.0






    scene s330
    with Fade (1,0,1)### you sitting on your bed with your phone in your hand //

    u "(I should text Chloe and see if she wants to meet up... I need to find out if there's any truth in what Ryan said.)"
    $ contact_Chloe.addReply("Hey Chloe, any chance you can meet up in a bit?", "clrep2a")

    play music "music/mindie4.mp3"
    call screen messager(contact_Chloe)
    label phonev:

    if contact_Chloe.messages[-1].replies:
        
        u "(I should message Chloe about meeting up later.)"

        jump phonev

    else:
        
        jump continuey

    label continuey:
    
    scene s330a # same as 330 but you looking up
    with dissolve

    u "(Shit, I just remembered that I still need a book for Ms. Rose's class...)"

    u "(The library should have it.)"

    #anchor
    stop music fadeout 2.0

    scene s331 # you walking into library
    with Fade (1,0,1)

    pause 0.5
    play music "music/mindie5.mp3"

    scene s332 # you skimming through bookshelves
    with dissolve

    u "(\"Economics Now\"... where are you?)"

    u "(There it is. I guess I'll sit down and get start on it.)"

    scene s333 # FIRST PERSON: you seeing Autumn sitting on table studying from afar
    with dissolve

    u "(Oh that's Lauren's sister Autumn...)"

    if laurenrs == False:

        if toldlauren == True:
            $ addPoint("tm", 1)
            u "(Hopefully Lauren didn't tell her about what happened...)"

            scene s334 # FIRST PERSON close up Autumn studying in front of you opposite of hte table (you're above since you're standing
            with dissolve

            u "Uhm... hey Autumn."

            scene s334a # autumn looks up slightly surprised mouth closed
            with dissolve

            pause 0.5

            scene s334b # Autumn dissapointed
            with dissolve

            aut "Please leave me alone..."

            menu:


                "Apologize":

                    jump ea_a

                "Sit somewhere else":

                    $ autumnmad = True
                    jump ea_b


            label ea_a:

            scene s334c
            with dissolve

            u "I'm sorry and I can see why Lauren would be upset."

            u "But... I can't change what happened, I was just trying to be honest."

            u "You have to believe me. I care about Lauren, I'd never do anything to hurt her."


            if kct == "loyal":
                call screen popup6
                label popup6:
                $ autumnmad = False
                scene s334d # autumn emphatic
                with dissolve

                aut "Hm... I know you guys weren't serious or anything yet."

                aut "But... you really hurt Lauren."



                scene s334e
                with dissolve

                u "I know and I'm really sorry. It won't happen again, I promise."

                scene s334d
                with dissolve

                aut "I believe you. At least you were honest about it and I don't think many guys would be."

                aut "I'll talk to Lauren about it."

                scene s334e
                with dissolve

                u "Thank you. Does that mean I can keep sitting here?"

                scene s334f #autumn kind smile
                with dissolve

                aut "Yeah, I guess."

                jump ea_ad


            else:
                $ autumnmad = True
                scene s334b
                with dissolve

                au "Right. Well actions speak louder than words, [name]."

                au "Now please leave me alone."

                scene s334c
                with dissolve

                u "Fine. I'll sit somewhere else."

                jump readmontaged


                label ea_b:
                label eb_b:
                    $ autumnmad = True
                    scene s334c
                    with dissolve

                    u "Fine. I'll sit somewhere else."

                    jump readmontagec


        else:

            if laurentoofar == True:
                $ addPoint("tm", 1)
                u "(Hopefully Lauren didn't tell her about what happened...)"

                scene s334
                with dissolve

                u "Uhm... hey Autumn."

                scene s334a
                with dissolve

                pause 0.5

                scene s334b
                with dissolve
                aut "Go away, creep."


                menu:

                    "Apologize":

                        jump eb_a

                    "Sit somewhere else":

                        $ autumnmad = True
                        jump eb_b


                label eb_a:

                scene s334c
                with dissolve

                u "I'm sorry and I understand why Lauren is upset."

                u "I just got carried away in the moment... I never meant to make her uncomfortable."

                u "You have to believe me. I care about Lauren, I'd never do anything to hurt her."



                if kct == "loyal":
                    call screen popup7
                    label popup7:
                    $ autumnmad = False
                    scene s334d # autumn emphatic
                    with dissolve

                    aut "[name]... I don't know."

                    aut "What you did was really messed up... you should have stopped when she told you to."

                    scene s334e
                    with dissolve

                    u "I know and I'm really sorry. I'll never do anything like that again, I promise."

                    scene s334d
                    with dissolve

                    aut "Hmmm... I mean I can understand that stuff like this can happen. It's just..."

                    aut "You know what? I'll talk to Lauren about it."

                    scene s334e
                    with dissolve

                    u "Thank you. Does that mean I can keep sitting here?"

                    scene s334f #autumn kind smile
                    with dissolve

                    aut "Yeah, alright."

                    jump eb_ad


                else:
                    $ autumnmad = True
                    scene s334b
                    with dissolve

                    aut "Right. Well actions speak louder than words, [name]."

                    aut "Now please leave me alone."

                    scene s334c
                    with dissolve

                    u "Fine. I'll sit somewhere else."

                    jump readmontaged

            else:
                $ addPoint("bf", 1)
                scene s334
                with dissolve

                u "Uhm... hey Autumn."

                scene s334a
                with dissolve

                pause 0.5

                scene s334f
                with dissolve

                aut "Hey, [name]. Haven't seen you in a while."

                scene s334g
                with dissolve

                u "You mean since you rescued me from Cameron?"

                scene s334f
                with dissolve

                aut "Well, I wasn't gonna put it like that."

                scene s334g
                with dissolve

                u "Haha it's okay, I'm still grateful. Do you mind if I sit down?"

                scene s334f
                with dissolve

                aut "Not at all."

                jump autumnsitb



    else:

        $ addPoint("bf", 1)
        scene s334
        with dissolve

        u "Uhm... hey Autumn."

        scene s334a
        with dissolve

        pause 0.5

        scene s334f
        with dissolve

        aut "Hey, [name]. I heard you went on a date with my sister last night."

        aut "How was it?"

        scene s334g
        with dissolve

        u "Yeah, it was good. We had a lot of fun."

        u "Do you mind if I sit down?"

        scene s334f
        with dissolve

        aut "Not at all."

        jump autumnsita


    label autumnsita:
    label autumnsitb:
    label ea_ad:
    label eb_ad:

    scene s335 # you sititng opposite to autumn eyeheight FIRST PERSON she's curious
    with dissolve

    aut "So uhm... what happened to your eye?"

    scene s335a
    with dissolve

    u "Oh, you know Grayson? He punched me at the Ape's rush party."

    scene s335b # Empathy
    with dissolve

    aut "Oh god, I'm so sorry."

    scene s335c
    with dissolve

    u "Yeah, it's okay."

    u "What are you uhm, studying for?"

    scene s335d # flirtyish smile, explanatory
    with dissolve

    aut "Well, I'm doing political science and I volunteered to write an essay on the government's contradictive stance on the feminist movement for extra credit."

    scene s335e
    with dissolve

    u "Ahhh... go women, right?"

    scene s335f # autumn laughing
    with dissolve

    aut "Haha, yeah. Go women, well put."

    scene s335g
    with dissolve

    u "So what do you do when you're not in the library?"

    scene s335d
    with dissolve

    aut "Well... I play lacrosse, I volunteer at the local dog shelter and I smoke weed."

    scene s335e
    with dissolve

    u "Ohhh, that's uh cool??"

    scene s335f
    with dissolve

    aut "Haha I'm kidding... thought I'd throw you off a bit."

    scene s335g
    with dissolve

    u "Haha, damn. You got me."

    u "So you work at the local dog shelter? That's awesome, I love dogs, but my parents would never let me get one."

    scene s335f
    with dissolve

    aut "You should come by when I'm working and then you can play with some of them if you want. They're really friendly."

    scene s335g
    with dissolve

    u "Oh my god, really? I'd love that, thank you so much."

    scene s335f
    with dissolve

    aut "Yeah, no worries. I'm there Monday to Thursday so just swing by."

    scene s335g
    with dissolve

    u "Alright cool, I definitely will."

    u "I should probably start reading now, I have a lot to get through."

    scene s335d
    with dissolve

    aut "Yeah, I should get back to my research as well."


    label readmontaged:
    label readmontagea:
    label readmontageb:
    label readmontagec:

    stop music fadeout 2.0


    scene s336 # you from front sitting down looking at the books cover.
    with fade

    u "(Alright... time to dig in.)"

    scene s336a #reading
    with Dissolve (1)

    pause 0.5

    scene s336b #reading bored
    with Dissolve (1)

    pause 0.5

    scene s336c # reading more bored
    with dissolve

    u "(Okay, that's enough for now.)"

    scene s337 # you walking through campus
    with fade

    play music "music/m12punk.mp3"

    pause 0.5

    scene s338 # ryan sitting somewhere (not cafeteria)
    with dissolve

    u "(Oh shit, there's Ryan.)"

    menu:


        "Talk to him":

            $ addPoint("bro", 1)
            jump ec_a

        "Ignore him":

            $ addPoint("tm", 1)
            jump ec_b


    label ec_a:

    scene s339 #you walking closer to Ryan
    with dissolve

    u "(Time to talk it out.)"

    scene s339a # Ryan looks over at you
    with dissolve

    ry "[name]?"

    pause 0.5

    scene s340a  # Ryan closer and standing up
    with dissolve

    u "Ryan, can we talk about yesterday?"

    scene s341 # Ryan close up apolegetic
    with dissolve

    ry "Yeah, man. I messed up, I'm sorry."

    jump ec_ad

    label ec_b:

    scene s339 #you walking closer to Ryan
    with dissolve

    u "(I'll just walk straight past him.)"

    scene s339a # Ryan looks over at you
    with dissolve

    ry "[name]?"

    pause 0.5

    scene s340  # Ryan closer and standing up
    with dissolve

    ry "Hey, can we talk?"

    scene s341a # Ryan close up mouth closed
    with dissolve

    u "Ok, let's talk."

    scene s341
    with dissolve

    ry "Look, man. I messed up, I'm sorry."

    jump ec_bd

    label ec_ad:
    label ec_bd:

    ry "I didn't mean to attack you like that. I just wanted to let you know about the things that I've heard. "

    ry "You know, so she doesn't play you."

    scene s341a
    with dissolve

    u "Dude, Chloe is no-"

    scene s341
    with dissolve

    ry "I know, she's not that kind of person."

    ry "And maybe she's not..."

    ry "But I'm just looking out for you, homie. Making sure, you see the bigger picture, you know what I mean?"

    scene s341a
    with dissolve

    u "Yeah, I get what you mean."

    scene s341b # ryan fist bump ready
    with dissolve

    ry "So we're cool?"

    scene s341c # fist bump
    with dissolve


    u "Yeah, we're cool."

    scene s341d # ryan smiling
    with dissolve

    ry "Awesome, man. I gotta go, I'll see you later."

    scene s341e
    with dissolve

    u "Yeah, see you later."

    ######

    scene s341f # Ryan gone
    with fade

    u "*Yawn*"

    u "(Why do I keep waking up in the middle of the night? It really fucks with my sleep.)"

    u "(I'll get a coffee, otherwise I'll be tired for the rest of the day.)"

    stop music fadeout 2.0
    scene s342 # in front of cafe
    with Fade (1,0,1)

    play music "music/mhappy.mp3"

    queue music [ "music/mlove.mp3" ]

    pause 0.5

    scene s343 # First person inside cafe # show penelope with coffe on laptop
    with dissolve

    if costumeaubrey == False: # costume w pen
        if caughtpeekingpenelope == True:
            if caughtpeekingpenelopecounter == True:
                jump continueaa

            else: # caught
                u "(Shit, Penelope's here. I wonder if she's still mad at me...)"

                u "(Maybe I should buy her something and apologize for peeking on her.)"

                scene s344 # in front of counter
                with dissolve
                clerk "Hello sir, what I can do for you?"

                menu:


                    "Buy Penelope a muffin":

                        $ addPoint("bf", 1)
                        $ muffin = True
                        $ caughtpeekingpenelopecounter = True
                        jump ed_a

                    "Buy Penelope a coffee":

                        $ muffin = False
                        jump ed_b

                label ed_a:
                scene s344a
                with dissolve

                $ keeneye = True
                if not steam:
                    image keeneye = "images/keeneye.webp"
                    show keeneye:
                        xpos 0
                        ypos -200
                        linear 0.5 xpos 0 ypos 0
                        pause 2.0
                        linear 0.5 xpos 0 ypos -200
                else:
                    $ achievement.grant("keen_eye")
                    $ achievement.sync()

                u "Can I get a muffin and a coffee please?"

                scene s344
                with dissolve

                clerk "Coming right up, sir."

                jump ed_ad

                label ed_b:
                scene s344a
                with dissolve

                u "Two coffees please."

                scene s344
                with dissolve

                clerk "Coming right up, sir."

                jump ed_bd


                label ed_ad:
                label ed_bd:

                scene s345 #standing in front of Penelope she looking down
                with fade

                u "Penelope?"

                scene s345a # pe looking up
                with dissolve

                pause 0.5

                scene s345b # pe upset
                with dissolve

                pe "Wha- what are you doing here, [name]?"

                scene s345c
                with dissolve

                u "Look I'm sorry for what happened."

                scene s345b
                with dissolve

                pe "Just- just go please. I don't feel comfortable around you anymore."

                scene s345c
                with dissolve

                if muffin == True:

                    u "Penelope, please... I brought you this muffin, I mean I saw you already had a coffee."

                    u "I'm really sorry. Please can we just forget about it?"

                    scene s345b
                    with dissolve

                    pe "Oh, that's really nice... I mean no, I mean I don't know. You broke my trust..."

                    pe "I thought you were my friend."

                    scene s345c
                    with dissolve

                    u "I am your friend... come on."

                    scene s345d #pen forgiving
                    with dissolve

                    pe "Okay uhm... you can sit down if you want."

                    scene s346 # you sitting in front of pen, her hands on table
                    with dissolve
                    u "Again, I'm really sorry."

                    menu:



                        "Grab her hand":

                            $ addPoint("bf", 1)
                            jump ef_a

                        "Leave it":

                            jump ef_b


                    label ef_a:
                    scene s347 # your hand grabbing her hand
                    with dissolve

                    pause 0.5

                    scene s346b # penelope slight smile
                    with dissolve

                    pe "It's okay."

                    scene s346c
                    with dissolve



                    menu:

                        "Kiss her":

                            $ addPoint("tm", 1)
                            $ penelopekiss = True
                            jump eg_a

                        "Don't kiss her":

                            jump eg_b

                    label eg_a:

                    scene s348 # you reaching for kiss, she's pulled away
                    with dissolve

                    pe "[name], what are you doing??"

                    scene s348a # u awkward head scratching
                    with dissolve

                    u "Uhh... I uhm-"

                    scene s348b
                    with dissolve

                    pe "Just 'cause I forgive you doesn't mean we have something."

                    scene s348a
                    with dissolve

                    u "Uhm, I should probably get going. Good to see you."

                    jump eg_ad

                    label ef_b:

                    scene s346b # penelope slight smile
                    with dissolve

                    pe "It's okay."

                    label eg_b:

                    scene s346c
                    with dissolve

                    u "Anyways, are you excited for history next week?"

                    jump ef_bd





                else:

                    u "Penelope, please... I got you a coffee."

                    u "I'm really sorry. Please can we just forget about it?"

                    scene s345b
                    with dissolve

                    pe "I already have a coffee. I don't need another one."

                    pe "I- I thought you were my friend and then you broke my trust."

                    scene s345c # pen
                    with dissolve

                    u "Penelope, I never-"

                    scene s345b
                    with dissolve

                    pe "Stop! Just leave please. I don't wanna be friends with someone I can't trust."

                    scene s345c
                    with dissolve

                    u "Alright... sorry."

                    jump continueac


        else: # not caught
            label continueaa:

            u "(Oh, Penelope's here, I should probably say hi.)"

            scene s345 #standing in front of Penelope she looking down
            with dissolve

            u "Penelope?"

            scene s345a # pe looking up
            with dissolve

            pause 0.5

            scene s349 #pen and you
            with dissolve

            pe "[name]!!!"

            pause 0.5

            scene s349a # she's standing up
            with dissolve

            pause 0.5

            scene s349b # pen hugging you
            with dissolve

            pe "Heyyy!"

            scene s349c # she standing in front of you smiling
            with dissolve
            pe "How did you know I was gonna be here?"

            menu:



                "Magic Powers.":

                    $ addPoint("bro", 1)
                    jump eh_a

                "I didn't.":

                    $ addPoint("bf", 1)
                    jump eh_b


            label eh_a:
            scene s349d
            with dissolve

            u "Magic powers, of course."

            scene s349e # pe touches your arm
            with dissolve

            pe "Haha, you're stupid."

            scene s349c
            with dissolve

            pe "You wanna sit down?"

            scene s349d
            with dissolve

            u "Yeah, sure."

            jump eh_ad

            label eh_b:

            scene s349d
            with dissolve

            u "I didn't, but I'm glad I came now"

            scene s349c
            with dissolve

            pe "Well, me too! Wanna sit down?"

            scene s349d
            with dissolve

            u "Yeah, sure."













    else: #shopping w aub
        u "(Oh, Penelope's here, I should probably say hi.)"

        scene s345 #standing in front of Penelope she looking down
        with dissolve

        u "Penelope?"

        scene s345a # pe looking up
        with dissolve

        pause 0.5

        scene s345f # pe happy
        with dissolve

        pe "[name]! Heyyy."


        pe "How did you know I was gonna be here?"

        menu:



            "Magic Powers.":

                $ addPoint("bro", 1)
                jump ej_a

            "I didn't.":

                $ addPoint("bf", 1)
                jump ej_b


        label ej_a:
        scene s345g
        with dissolve

        u "Magic powers, of course."

        scene s345f
        with dissolve

        pe "Haha, you're stupid."

        pe "You wanna sit down?"

        scene s345g
        with dissolve

        u "Yeah, sure."

        jump ej_ad

        label ej_b:

        scene s345g
        with dissolve

        u "I didn't, but I'm glad I came now."

        scene s345f
        with dissolve

        pe "Well, me too! Wanna sit down?"

        scene s345g
        with dissolve

        u "Yeah, sure."

        jump ej_bd

    #### Sitting down
    label eh_bd:
    label eh_ad:
    label ej_ad:
    label ej_bd:

    scene s350a #FIRST PERSON sititng across penelope smiling
    with dissolve

    u "Soo... are you excited for the history costume party next week?"

    label ef_bd:

    scene s350
    with dissolve

    pe "I am! I love costumes, I hope someone comes as in a giant full-body animal one."

    scene s350a
    with dissolve

    u "Penelope, you are aware that Mr. Lee said historically accurate, right?"

    scene s350b # penelope sad annoyed
    with dissolve

    pe "Aww, I forgot about that... why did he have to take all the fun out of it?"

    scene s350c
    with dissolve

    u "I know, it's a shame."

    u "What are you working on?"

    scene s350d # penelope awkward
    with dissolve

    pe "Uhm... nothing. Uni work. Homework. School stuff."

    pe "You know, nothing I shouldn't be doing."

    scene s350e
    with dissolve

    u "Haha, Penelope, that's not very convincing... Are you ok? You're acting weird."


    scene s350f # pen upset
    with dissolve

    pe "No, I'm not. You're acting weird!"

    pe "What are you working on? Huh?"

    scene s350g
    with dissolve

    u "Uhm... nothing I just got here."

    scene s350f
    with dissolve

    pe "Exactly."

    scene s350g
    with dissolve

    u "Penelope, come on. You can tell me. I am the world champion of keeping secrets."

    u "Literally had to go through a whole international tournament."

    scene s350h # annoyed smile
    with dissolve

    pe "*Chuckles* Why do you have to turn everything into a joke..."

    scene s350j
    with dissolve

    u "Okay, you don't have to tell me. But if I were you, I'd be more careful watching hardcore porn in a cafe."

    u "You don't wanna accidentally turn the speakers on, I mean we've all been there."

    scene s350k # pen laughing
    with dissolve

    pe "It's not porn!"

    scene s350o # pen shy
    with dissolve

    pe "I don't- I don't watch porn."

    scene s350p
    with dissolve
    u "Now we're getting into an interesting topic."

    menu:



        "We should watch some.":

            $ addPoint("tm", 1)
            $ pornpen = 1
            jump ek_a

        "You should try it.":

            $ addPoint("bro", 1)
            $ pornpen = 2
            jump ek_b

    label ek_a:

    u "You know, we should watch some together sometime."

    scene s350k
    with dissolve

    pe "*Laughs* Ewww... I don't think we should"

    scene s350l
    with dissolve

    u "The offer still stands, if you change your mind."

    scene s350k
    with dissolve

    pe "Right, thank you."

    jump ek_ad


    label ek_b:

    u "You know, you should try it sometime."

    scene s350k
    with dissolve

    pe "*Laughs* I don't know, I don't think I'd like it."

    scene s350l
    with dissolve

    u "Haha, I think you'd be surprised."

    label ek_ad:

    scene s350
    with dissolve
    pe "I have to go now and meet my friend. It uhm, it was nice to see you though."


    menu:



        "You wanna go bowling?":

            jump el_a

        "Yeah, it was nice.":

            $ bowling = False
            jump el_b

    label el_a:

    scene s350a
    with dissolve

    u "It was nice to see you too."

    u "Hey, you wanna go bowling with me sometime next week?"

    scene s350d
    with dissolve

    pe "I don't know, I have sooo much studying to do..."

    menu:



        "Encourage her":
            $ addPoint("bf", 1)
            $ bowling = True
            jump penea

        "Tease her":
            $ addPoint("bro", 1)
            $ bowling = False
            jump peneb


    label penea:

    scene s350e
    with dissolve

    u "Come on, having some fun won't ruin your grades, I promise."

    scene s350k
    with dissolve

    pe "Hmmm... alright. Let's go bowling next week."

    scene s350l
    with dissolve

    u "Cool, I'll see you."

    scene s350k
    with dissolve

    pe "Yeah, uhm, see you soon."

    jump el_ad

    label peneb:

    scene s350e
    with dissolve

    u "What, scared you can't beat me?"

    scene s350d
    with dissolve

    pe "Sorry, I- I really can't. I need to study."

    scene s350e
    with dissolve

    u "Alright... no worries. I'll see you."

    scene s350d
    with dissolve

    pe "Yeah, uhm, see you soon."

    jump el_ad



    label el_b:

    scene s350a
    with dissolve

    u "Yeah, it was nice to see you too."

    scene s350
    with dissolve

    pe "Bye bye, I'll see you later."

    scene s350a
    with dissolve

    u "Yeah, see you later."

    jump el_bd

    #### After cafe

    label continueac:
    label eg_ad:

    scene s351 # you walking back
    with fade

    u "(Shit, that didn't go as planned...)"

    jump continueab

    label el_bd:
    label el_ad:

    scene s351
    with fade

    u "(I wonder what Penelope was doing on that laptop...)"

    label continueab:
    stop music fadeout 2.0

    play sound "sounds/vibrate.mp3"

    play music "music/m9punk.mp3"

    
    $ contact_Josh.newMessage("Hey man, you wanna hang out with me and some friends tonight?")
    $ contact_Josh.addReply("Uhh, sure.", "jorep8a")
    $ contact_Josh.addReply("I'm meeting a friend at 11, so I can't really.", "jorep8b")

    label phonew:

    if contact_Josh.messages[-1].replies:

        u "(I should probably reply to my messages.)"

        jump phonew

    else:

        if contact_Josh.messages[-2].reply.message == "I can't, sorry.":

            u "(Fucking hell, I forgot how persistent Josh could be...)"
            
            jump jorepb

        else:

            u "(Okay, I need to make sure that I don't forget about meeting Chloe.)"
            
            jump jorepa







    # in the uber transition
    label jorepa:

    stop music fadeout 2.0
    scene s352
    with Fade (1,0,1)


    pause 0.7

    play music "music/mparty2.mp3"

    queue music [ "music/mparty3.mp3", "music/mparty4.mp3" ]

    scene s353 # knocking on josh door
    with fade

    play sound "sounds/knock.mp3"

    pause 0.5

    play sound "sounds/dooropen.mp3"

    scene s353a # josh opens door
    with dissolve


    jo "What's up, bro?"

    if jorep12 == 1:

        jo "Picture of Amber did it, eh?"

        scene s353b#
        with dissolve

        u "Oh, shut up."

        scene s353a
        with dissolve

        jo "Hahaha."

        jump continuead

    else:

        jo "Come in."

        jump continueae

    label continuead:
    label continueae:

    scene s354 # standing in living room First Person
    with dissolve

    jo "Amber, Kim, this is [name]."

    scene s354a # amber mouth open
    with dissolve

    am "Heyy! Nice black eye!"

    scene s354b # kim mouth open
    with dissolve

    ki "Hi."

    scene s355 # josh closeup
    with dissolve

    jo "So, what's your drink of choice?"


    scene s355a
    with dissolve

    u "I guess I'll take a beer."

    scene s355
    with dissolve

    jo "Alright, champ. Coming up."


    scene s356 # close up of amber and kim
    with dissolve

    am "Are you gonna sit down with us? We won't bite."

    scene s356a
    with dissolve

    u "Damn I was really hoping you would though."

    scene s356
    with dissolve

    am "Well then you'll have to get me a bit more drunk first."

    scene s358 # josh coming back
    with fade

    jo "Here you go, man."

    scene s359 # josh puts down drink
    with dissolve
    jo "I see you've taken my spot."


    menu:



        "I can move.":

            $ addPoint("bf", 1)
            $ addPoint("bro", 1)
            jump en_a

        "It's my spot now.":

            $ addPoint("tm", 1)
            jump en_b

    label en_a:
    scene s359a
    with dissolve

    u "Oh, I can move if you want."

    scene s359
    with dissolve

    jo "Hahaha, buddy I'm just kidding, stay put."

    jump en_ad

    label en_b:

    scene s359a
    with dissolve

    u "Yeah, I guess it's my spot now."

    scene s359
    with dissolve

    jo "Damn, alright. Hahaha."

    label en_ad:

    scene s357 # amber leaning forward curious
    with dissolve

    am "So, [name], have you thought about which fraternity you're gonna join, yet?"

    scene s357
    with dissolve

    u "Uhm, I-"

    scene s360 # kim looking at you
    with dissolve

    ki "Oh come on, this guy's obviously a Frog, look at him."

    scene s361 # josh looking at kim disgusted
    with dissolve

    jo "My man [name]?? No way, he's a natural born fighter."

    scene s361a # josh looking at you
    with dissolve

    u "Uhm..."

    scene s360a
    with dissolve

    u "I..."

    scene s357a
    with dissolve


    menu:

        "I'll join the Wolves.":

            $ addPoint("bro", 1)
            jump eo_a

        "I don't know yet.":

            $ addPoint("bf", 1)
            jump eo_b

    label eo_a:

    u "I'll join the Wolves."

    scene s361b # josh looking at Kim happy
    with dissolve

    jo "See? I knew he was a fighter."

    jump eo_ad

    label eo_b:

    u "I don't know yet."

    scene s360a # kim laughing at you
    with dissolve

    ki "Ha! Classic Frog."

    jump eo_bd

    label eo_ad:
    label eo_bd:

    scene s357d # laughing smile amber
    with dissolve

    am "I think you'd make a good fighter."

    am "You already have the look."

    scene s357e
    with dissolve

    u "Haha, thanks."

    scene s361d # josh with phone in hand looking up amber
    with dissolve

    jo "Alright, let's play some bangolo."

    scene s361e
    with dissolve

    u "What's bangolo?"

    scene s357
    with dissolve

    am "It's this knock-off drinking game app that Josh has 'cause he doesn't wanna pay for the original."

    scene s361d
    with dissolve

    jo "Hey, I just actually think it's better than the original, alright?"

    scene s361f # josh looking at you
    with dissolve

    jo "The rules are simple. The phone gives us tasks and how many sips to drink if we lose or are selected in some way or another."

    menu:



        "Sounds good.":
            $ addPoint("bro", 1)
            jump jonewa

        "I should stop here.":
            $ addPoint("bf", 1)
            jump jonewb


    label jonewb:

    scene s361f
    with dissolve

    u "Uhm, actually... I should stop here. I really have to go see my friend soon and I don't wanna be too drunk."

    scene s357
    with dissolve

    am "Oh come on, just stay a bit longer. You never know what you might miss out on."

    menu:

        "Alright, just for a bit.":
            jump jonewc

        "Sorry, I really can't.":
            jump jonewd


    label jonewd:

    scene s357a
    with dissolve

    u "Sorry, I really gotta go. But maybe I'll uhm... come back later."

    jump jorepb

    label jonewc:

    scene s357a
    with dissolve

    u "Alright, I'll stay a bit longer, let's play."

    scene s357
    with dissolve

    am "Good choice."

    jump jonewe

    label jonewa:

    scene s361g
    with dissolve

    u "Cool, sounds good."

    label jonewe:

    scene jomon2 # josh looking down at phone
    with dissolve

    jo "I just gotta put in our names."


    # montage style evening

    scene joclock1
    with Dissolve (1)

    pause 0.5

    scene jomon1 # kim drinking
    with Dissolve (1)

    scene jomon2 # josh looking at phone
    with Dissolve (1)

    jo "[name], do a handstand or drink three sips."

    scene jomon2a #josh looking at you mouth closed
    with dissolve

    u "Uhhh..."


    menu:



        "Do a handstand":

            $ addPoint("bro", 1)
            jump ep_a

        "Drink three sips":

            $ addPoint("bf", 1)
            jump ep_b

    label ep_b:

    u "I'll drink."

    scene jomon5 # you drinking
    with dissolve

    pause 0.5

    scene s357
    with dissolve

    am "Oh come on, I wanna see you do a handstand."

    scene s357a
    with dissolve

    label ep_a:

    u "You know what, I'll do it."

    scene jomon3 # handstand
    with dissolve

    pause 0.5

    scene jomon3a
    with dissolve

    pause 0.5

    play sound "sounds/fall.mp3"

    scene jomon3b
    with vpunch

    pause 0.5

    scene jomon4 # am laughing
    with dissolve

    am "Hahahaha!"

    scene joclock2
    with Dissolve (1)

    pause 0.5

    scene jomon2
    with Dissolve (1)

    jo "Kim, kiss one of the other players or finish your drink."

    scene jomon6 # kim standign up
    with dissolve

    ki "Come on Amber, let's give these boys something to watch."

    scene jomon6a # kiss before
    with dissolve

    pause 0.5

    play sound "sounds/kiss.mp3"

    scene jomon6b # kiss
    with dissolve

    pause 1.0

    scene jomon6a
    with dissolve

    pause 0.5

    scene jomon2b # josh looking at them
    with dissolve

    jo "Hell yeah!"

    scene joclock3
    with Dissolve (1)

    pause 0.5

    scene jomon2
    with Dissolve (1)

    jo "Amber, who's the most attractive guy in the room?"

    scene s361f # josh looking at you laughingly
    with dissolve

    jo "Sorry about that, [name]. I don't want you to feel bad. I'm sure you're a close second."

    scene s357
    with dissolve

    am "Actually, I prefer fresh meat over here."

    scene s361d
    with dissolve

    jo "What?"

    scene s357
    with dissolve

    am "Not gonna lie, I'm kinda digging the black eye."

    scene s357a
    with dissolve

    u "Thanks, I'm digging your regular eye too."

    scene s357d
    with dissolve

    am "Hahaha."


    scene joclock4 # ALL DRINKING
    with Dissolve (1)

    pause 0.5

    scene jomon5
    with Dissolve (1)

    pause 0.5

    scene jomon1
    with Dissolve (1)

    pause 0.5

    scene jomon7 # josh drinking
    with Dissolve (1)

    pause 0.5

    scene jomon8 # amber drinking
    with Dissolve (1)

    pause 0.5

    play sound "sounds/cup.mp3"
    scene jomon10 # cups on table # cups hits table sound
    with Dissolve (1)

    pause 0.5
    play sound "sounds/cup.mp3"
    scene jomon11 # cups on table # cups hits table sound
    with Dissolve (1)


    pause 0.5

    scene jomon2 # josh drunkenly reading off phone
    with Dissolve (1)

    jo "*Drunk* Okayy... last one."

    jo "*Drunk* [name], choose another player and do a tequila shot off of them."

    scene s361f # josh looks up at you laughing
    with dissolve

    jo "*Drunken Laugh* Nice one, mate."

    jo "*Drunk* So that means that you lick salt off their collarbone, then drink a shot of tequila out of their belly button and then bite into a lime that they're holding with their mouth."

    jo "*Drunk* I assume you won't pick me, so who's it gonna be?"

    scene s357a
    with dissolve

    jo "Amber?"

    scene s360a
    with dissolve

    jo "Or Kim?"


    scene s361g
    with dissolve
    u "*Drunk* Uhh..."

    menu:



        "Amber":

            $ shotamber = True
            jump eq_a

        "Kim":

            $ shotamber = False
            jump eq_b

    label eq_a:

    scene jomon14 # amber in bra ready for shot of her body
    with fade

    jo "*Drunk* Alright [name], lick the salt off her collarbone, drink the shot out of her belly button and bite the lime out of her mouth."

    scene jomon14a
    with dissolve

    pause 0.5

    scene jomon14b
    with dissolve

    pause 0.5

    scene jomon14c
    with dissolve

    pause 0.5

    scene jomon15 # close up of you with lemon in mouth right above ambers face
    with dissolve


    menu:

        "Kiss her":

            $ addPoint("tm", 1)
            $ kissamber = True
            jump er_a


        "Don't kiss her":

            $ addPoint("tm", 1)
            $ kissamber = False
            jump er_b




    label er_a:

    play sound "sounds/spit.mp3"

    scene jomon15a # spits out lemon
    with dissolve

    u "*Spits*"

    scene jomon15b # kiss
    with dissolve

    pause 1.0

    play sound "sounds/phonealarm.mp3"

    "*Phone alarm goes off*"

    scene jomon15c # you pull away and look down
    with dissolve

    pause 0.5

    jump er_ad

    label er_b:

    play sound "sounds/spit.mp3"

    scene jomon15a # spits out lemon
    with dissolve

    u "*Spits*"

    play sound "sounds/phonealarm.mp3"

    scene jomon15c # you pull away and look down
    with dissolve

    "*Phone alarm ringing*"

    jump er_bd

    label eq_b:

    scene jomon16 # kim in bra ready for shot of her body
    with fade

    jo "*Drunk* Alright [name], lick the salt off her collarbone, drink the shot out of her belly button and bite the lime out of her mouth."

    scene jomon16a
    with dissolve

    pause 0.5

    scene jomon16b
    with dissolve

    pause 0.5

    scene jomon16c
    with dissolve

    pause 0.5

    scene jomon17 # close up of you with lemon in mouth right above ambers face
    with dissolve


    menu:

        "Kiss her":

            $ addPoint("tm", 1)
            $ kisskim = True
            jump es_a


        "Don't kiss her":

            $ addPoint("tm", 1)
            $ kisskim = False
            jump es_b




    label es_a:

    play sound "sounds/spit.mp3"

    scene jomon17a # spits out lemon
    with dissolve

    u "*Spit sound*"

    scene jomon17b # kiss but she pulls aways
    with dissolve

    ki "Mhhh... no."

    scene jomon17b2
    with dissolve

    play sound "sounds/phonealarm.mp3"

    "*Phone alarm goes off*"

    scene jomon17c # you look down at your phone
    with dissolve

    pause 0.5

    jump es_ad

    label es_b:

    play sound "sounds/spit.mp3"

    scene jomon17a # spits out lemon
    with dissolve

    u "*Spits*"

    play sound "sounds/phonealarm.mp3"

    scene jomon17c # you look down at your phone
    with dissolve

    "*Phone alarm ringing*"

    jump es_bd



############# WALK TO CHLOE paranoia

    label er_ad:
    label er_bd:
    label es_ad:
    label es_bd:

    scene s362 # looking at your phone # chloe Alarm
    with dissolve

    u "(Shit, I gotta go meet Chloe!)"

    stop sound

    u "*Drunk* Guys, I really gotta go."

    u "*Drunk* Maybe I- I'll come back later."

    stop music fadeout 2.0

    scene s367 # you walking at night
    with Fade (1,0,1)

    u "(*Drunk* Okay, I- I just gotta ask her straight up.)"

    u "(*Drunk* Does she- does she like me or is she just- just using me to get back at Grayson?)"


    ############## At Chloe

    scene s368 # knocking on Chloes door
    with Fade (1,0,1)

    play sound "sounds/knock.mp3"

    "*Knock knock knock*"

    play sound "sounds/dooropen.mp3"

    play music "music/msad2.mp3"

    scene s369 # door opening sound chloe inside
    with dissolve

    cl "Hey. You wanna come in?"

    scene s369a
    with dissolve

    u "*Drunk* Hey uh, actually... can we- can we talk outside first? I- I just wanna clear something up."

    scene s369b
    with dissolve

    cl "[name], are you drunk?"

    scene s369c
    with dissolve

    u "*Drunk* Nah, I just had a drink with some friends."

    scene s369b
    with dissolve

    cl "Right... Let me just put on a sweater..."

    scene s370 # chloe close up outside
    with fade

    cl "So, what did you wanna talk to me about?"

    scene s370a
    with dissolve

    u "*Drunk* Well, Ryan... *deep breath* Ryan said you were playing me and just using me to get back at Grayson."

    scene s370b # chloe upset
    with dissolve

    cl "What?? [name], that's bullshit."

    scene s370c
    with dissolve

    u "*Drunk* He said Grayson, he- he told him about a lot of shady shit that you did in the past."

    scene s370b
    with dissolve
    cl "Well there you have it! Grayson put him up to this, just to fuck with me! I didn't do anything shady!"

    menu:



        "Accuse her of lying":

            $ addPoint("tm", 1)
            jump eu_a


        "Ask about the punch":

            scene s370c
            with dissolve
            jump eu_b


    label eu_a:

    scene s370c
    with dissolve

    u "*Drunk* You're lying! Yeah sure, the hottest girl in school wants me, the freshman who got beaten up at his first college party."

    u "*Drunk* Pretty realistic, isn't it?!"

    scene s370d # chloe sad desperate
    with dissolve

    cl "[name], I don't care about the fighting, or any of that shit. What Grayson did to you was pathetic. I like you 'cause you were funny and kind and ... and you cared."

    scene s370e
    with dissolve

    label eu_b:
    u "*Drunk* Really?? Then why did you go after Grayson instead of helping me up when he knocked me out??"

    scene s370d
    with dissolve

    cl "I- I..."

    cl "I told him to stop, okay?? I didn't know if he was gonna hurt you even more."

    scene s370e
    with dissolve

    u "*Drunk* Ryan said that you just saw his punch as a personal attack and didn't give one fuck about me being hurt. And you know what? Maybe he's right!"

    scene s370d
    with dissolve

    cl "What have I ever done for you not to fucking trust me one bit?!"

    scene s370e
    with dissolve
    u "*Drunk* Apparently a bunch of shady shit in the past!"


    scene s370f # Chloe really sad
    with dissolve

    cl "*Gasp*"

    cl "You know how you can be sure I wasn't just using you?"

    cl "Because if I was using you, I would probably try to seduce you back into trusting me right now."

    cl "But don't worry, I don't want that. We're done."

    scene s371
    with dissolve # scene chloe walking back into her house

    u "*Drunk* Chloe!"

    play sound "sounds/slam.mp3"

    scene s371a
    with hpunch #scene door slam

    "*Door slam*"

    scene s372 # you in front of wall angry
    with dissolve

    u "HNGGGG!"

    play sound "sounds/facepunch1.mp3"

    scene s372a # you punch the wall
    with vpunch

    pause 0.5

    scene s372b # your hand hurts you hold it, it's bloody
    with dissolve

    u "Ah, fuck!"

    unknown "[name], is that you??"

    scene s372c # you turn your head
    with dissolve

    stop music fadeout 2.0

    " "

    u "Oh shit..."

################ END OF V 0.4 ################



    scene s373 # nora approaching
    with dissolve
    play music "music/m16punk.mp3"
    no "What are you doing here? And why did you just punch the wall?"

    menu:



        "It's Chloe.":
            $ tellnora = 1

            jump ev_a

        "It's nothing.":
            $ tellnora = 0

            jump ev_b

    label ev_a:

    scene s374a # nora close up questioning
    with dissolve

    u "*Drunk* It's Chloe... I just- I just wanted to talk to her..."

    u "*Drunk* And now she's all mad and I don't even know what happened."

    scene s374c2 # nora thinking mouth close

    no "Hmmm..."

    scene s374b # mouth open
    with dissolve


    no "Chloe can be a bit overdramatic sometimes, you know."

    no "Maybe she'll calm down by tomorrow."


    scene s374c
    with dissolve

    u "*Drunk* Right..."

    scene s374b
    with dissolve

    no "Hey, it's none of my business, but... what did you guys talk about that made you wanna punch a wall after?"

    menu:



        "Tell her":

            $ tellnora = 2
            jump ew_a

        "Say you gotta go":

            $ tellnora = 1
            jump ew_b

    label ew_a:

    scene s374c
    with dissolve

    u "*Drunk* My uhm, my friend, he- he said that Chloe did some shady shit in the past and I just had to find out the truth!"

    scene s374d# nora slight laugh, cocky
    with dissolve

    no "And what did you find out?"

    scene s374e
    with dissolve

    u "*Drunk* Nothing! I think all I did was ruin our relationship..."

    scene s374d
    with dissolve

    no "Yeah, that sounds about right."

    scene s374e
    with dissolve

    u "*Drunk* What- What do you mean?"

    scene s374b
    with dissolve

    no "Dude, you're drunk, upset and don't even know the whole story. What did you think was gonna happen when you talk to her?"

    scene s374c
    with dissolve

    u "*Drunk* I don't know..."

    u "*Drunk* What do you mean the whole story?"

    scene s374d
    with dissolve

    no "It's late, I really don't wanna get into it. But hey, let me know how your little love story ends."

    no "Night, [name]."

    scene s374e
    with dissolve

    u "*Drunk* Night..."

    jump ew_ad

    label ew_b:

    scene s374c
    with dissolve

    u "*Drunk* Uhhh... nothing. It's not important."

    u "*Drunk* I should uhm... probably go home now, it's late."

    scene s374d
    with dissolve

    no "Alright, well let me know how your little love story ends."

    no "Night, [name]."

    scene s374c
    with dissolve

    u "*Drunk* Night..."

    jump ev_bd

    label ev_b:

    scene s374a
    with dissolve

    u "*Drunk* It's- it's nothing. I gotta go, I'll see you around, Nora."

    scene s374b
    with dissolve

    no "Alright, well let's hope you and our house don't get into another fight in the future."

    scene s374c
    with dissolve

    u "*Drunk* Yeah, right..."

    label ew_ad:
    label ev_bd:


    scene s375 # You walking home
    with Fade (1,0,1)

    u "(Way to mess things up with Chloe.... great fucking job, [name].)"

    stop music fadeout 2.0

    scene s376 # you in bed laying on your side looking at the wall
    with Fade (2,0,2)

    pause 0.5

    scene s376a # you opening your eyes
    with dissolve
    play music "music/mindie1.mp3"

    queue music [ "music/mindie2.mp3", "music/mindie3.mp3" ]

    u "(Oh man, I drank way too much last night...)"
    if volleyball == True:

        scene s376b # yawning and turning around
        with dissolve

        u "*Yawns*"

        scene s376c # surpisde
        with dissolve

        pause 0.5

        scene s377a # showing volleyball
        with dissolve

        u "(I completely forgot I bought this. I guess I can't really give it to Chloe anymore now, can I?)"
    else:
        scene s376b
        with dissolve

        u "*Yawns*"

    scene s376d # you touching your eye
    with dissolve

    u "(At least my eye is starting to heal...)"

    jump newchloec

    ############ Chloe Talk New

    label jorepb:

    scene jonew1 #transition "a bit later", walking to chloe
    with Fade (1,0,1)

    pause 1.0

    scene s368 # knocking on Chloes door
    with Fade (1,0,1)

    play sound "sounds/knock.mp3"

    "*Knock knock knock*"

    play sound "sounds/dooropen.mp3"

    play music "music/msad2.mp3"

    scene s369 # door opening sound chloe inside
    with dissolve

    cl "Hey. You wanna come in?"

    scene s369a
    with dissolve

    u "Hey uh, actually... can we- can we talk outside first? I- I just wanna clear something up."

    scene s369
    with dissolve

    cl "Uhm, yeah of course. Let me just put on my sweater."

    scene s370 # chloe close up outside
    with fade

    cl "So, what did you wanna talk to me about?"

    scene s370a
    with dissolve

    u "Well, Ryan... *deep breath* Ryan said you were playing me and just using me to get back at Grayson."

    scene s370
    with dissolve

    cl "What?? [name], I'm not, that's absurd..."

    scene s370a
    with dissolve

    u " He said Grayson told him about a lot of shady shit that you did in the past."

    scene s370
    with dissolve
    cl "I didn't do anything shady. Grayson is just spreading lies like he always is."


    menu:



        "I believe you.":

            $ addPoint("bf", 1)
            jump newchloea


        "You're lying.":

            $ addPoint("tm", 1)
            jump newchloeb

    label newchloea:

    $ chloemad = False

    scene s370
    with dissolve

    u "I believe you. I just had to make sure, you know?"

    scene clna
    with dissolve

    cl "Yeah, I get that."

    cl "Hey I don't have that much more time tonight, but how about we hang out tomorrow?"

    scene clnb
    with dissolve

    u "Yeah, sounds great. I'll see you then, good night."

    scene clna
    with dissolve

    cl "Good night, [name]."

    scene s375 # You walking home
    with Fade (1,0,1)

    u "(Good thing I didn't get drunk, that could have very easily gone wrong and ended in a big fight with Chloe.)"

    scene s376 # you in bed laying on your side looking at the wall
    with Fade (2,0,2)

    pause 0.5

    scene s376a # you opening your eyes
    with dissolve

    u "(Alright, time for a new day.)"
    if volleyball == True:

        scene s376b # yawning and turning around
        with dissolve

        u "*Yawns*"

        scene s376c # surpisde
        with dissolve

        pause 0.5

        scene s377a # showing volleyball
        with dissolve

        u "(I completely forgot I bought this. I should give it to Chloe when we hang out later today.)"
    else:
        scene s376b
        with dissolve

        u "*Yawns*"

    scene s376d # you touching your eye
    with dissolve

    u "(Hey, my eye is starting to heal...)"

    jump newchloec

    label newchloeb:

    scene s370a
    with dissolve

    u "You're lying. Yeah sure, the hottest girl in school wants me, the freshman who got beaten up at his first college party."

    scene s370e
    with dissolve

    u "That seems realistic, right?!"

    scene s370d # chloe sad desperate
    with dissolve

    cl "[name], I don't care about the fighting, or any of that shit. What Grayson did to you was pathetic. I like you 'cause you were funny and kind and ... and you cared."

    scene s370e
    with dissolve

    u "Then why did you go after Grayson instead of helping me up when he knocked me out??"

    scene s370d
    with dissolve

    cl "I- I..."

    cl "I told him to stop, okay?? I didn't know if he was gonna hurt you even more."

    scene s370e
    with dissolve

    u "*Ryan said that you just saw his punch as a personal attack and didn't give one fuck about me being hurt. And you know what? Maybe he's right!"

    scene s370d
    with dissolve

    cl "What have I ever done for you not to fucking trust me one bit?!"

    scene s370e
    with dissolve
    u "Apparently a bunch of shady shit in the past!"


    scene s370f # Chloe really sad
    with dissolve

    cl "*Gasp*"

    cl "You know how you can be sure I wasn't just using you?"

    cl "Because if I was using you, I would probably try to seduce you back into trusting me right now."

    cl "But don't worry, I don't want that. We're done."

    scene s371
    with dissolve # scene chloe walking back into her house

    u "Chloe!"

    play sound "sounds/slam.mp3"

    scene s371a
    with hpunch #scene door slam

    "*Door slam*"

    scene s372 # you in front of wall angry
    with dissolve

    u "HNGGGG!"

    play sound "sounds/facepunch1.mp3"

    scene s372a # you punch the wall
    with vpunch

    pause 0.5

    scene s372b # your hand hurts you hold it, it's bloody
    with dissolve

    u "Ah, fuck!"

    unknown "[name], is that you??"

    scene s372c # you turn your head
    with dissolve

    stop music fadeout 2.0

    " "

    u "Oh shit..."

    scene s373 # nora approaching
    with dissolve
    play music "music/m16punk.mp3"
    no "What are you doing here? And why did you just punch the wall?"

    menu:



        "It's Chloe.":

            $ tellnora = 1
            jump nna

        "It's nothing.":

            $ tellnora = 0
            jump nnb

    label nna:

    scene s374a # nora close up questioning
    with dissolve

    u "It's Chloe... I just- I just wanted to talk to her..."

    u "But it just got out of control..."

    scene s374c2 # nora thinking mouth close

    no "Hmmm..."

    scene s374b # mouth open
    with dissolve


    no "Chloe can be a bit overdramatic sometimes, you know."

    no "Maybe she'll calm down by tomorrow."


    scene s374c
    with dissolve

    u "Right..."

    scene s374b
    with dissolve

    no "Hey, it's none of my business, but... what did you guys talk about that made you wanna punch a wall after?"

    menu:



        "Tell her":

            $ tellnora = 2
            jump nnc

        "Say you gotta go":

            $ tellnora = 1
            jump nnd

    label nnc:

    scene s374c
    with dissolve

    u "My uhm, my friend said that Chloe did some shady shit in the past and I just had to find out the truth."

    scene s374d# nora slight laugh, cocky
    with dissolve

    no "And what did you find out?"

    scene s374e
    with dissolve

    u "Nothing! I think all I did was ruin our relationship..."

    scene s374d
    with dissolve

    no "Yeah, that sounds about right."

    scene s374e
    with dissolve

    u "What- What do you mean?"

    scene s374b
    with dissolve

    no "Dude, you're upset and don't even know the whole story. What did you think was gonna happen when you talk to her?"

    scene s374c
    with dissolve

    u "I don't know..."

    u "What do you mean the whole story?"

    scene s374d
    with dissolve

    no "It's late, I really don't wanna get into it. But hey, let me know how your little love story ends."

    no "Night, [name]."

    scene s374e
    with dissolve

    u "Night..."

    jump nncd

    label nnd:

    scene s374c
    with dissolve

    u "Uhhh... nothing. It's not important."

    u "I should uhm... probably go home now, it's late."

    scene s374d
    with dissolve

    no "Alright, well let me know how your little love story ends."

    no "Night, [name]."

    scene s374c
    with dissolve

    u "Night..."

    jump nnbd

    label nnb:

    scene s374a
    with dissolve

    u "It's- it's nothing. I gotta go, I'll see you around, Nora."

    scene s374b
    with dissolve

    no "Alright, well let's hope you and our house don't get into another fight in the future."

    scene s374c
    with dissolve

    u "Yeah, right..."

    label nncd:
    label nnbd:

    scene s375 # You walking home
    with Fade (1,0,1)

    u "(Way to mess things up with Chloe.... great fucking job, [name].)"

    stop music fadeout 2.0

    scene s376 # you in bed laying on your side looking at the wall
    with Fade (2,0,2)

    pause 0.5

    scene s376a # you opening your eyes
    with dissolve
    play music "music/mindie1.mp3"

    queue music [ "music/mindie2.mp3", "music/mindie3.mp3" ]

    pause 0.5

    if volleyball == True:

        scene s376b # yawning and turning around
        with dissolve

        u "*Yawns*"

        scene s376c # surpisde
        with dissolve

        pause 0.5

        scene s377a # showing volleyball
        with dissolve

        u "(I completely forgot I bought this. I guess I can't really give it to Chloe anymore now, can I?)"
    else:
        scene s376b
        with dissolve

        u "*Yawns*"

    scene s376d # you touching your eye
    with dissolve

    u "(At least my eye is starting to heal...)"


    label newchloec:


    scene s376e
    with dissolve

    #### Amber text
    play sound "sounds/vibrate.mp3"
    
    $ msgnot = 1
    $ ammsgnot = 1
    $ ammsg = 1
    $ amisreply = 1

    #################
    if kissamber == True:
        $ contact_Amber.newMessage("Hey, it's Amber")
        $ contact_Amber.newMessage("Josh gave me your number")
        $ contact_Amber.newMessage("You know, you never came back, I thought we were having a good time xx")
        $ contact_Amber.addReply("We did, I'll make it up to you.", "amrep3a")
        $ contact_Amber.addReply("Sorry, something came up.", "amrep3b")

    else:

        if contact_Josh.messages[-1].reply.message == "I can't, sorry.":
            $ contact_Amber.newMessage("Hey, it's Amber")
            $ contact_Amber.newMessage("Josh gave me your number")
            $ contact_Amber.newMessage("How come you didn't show up yesterday? Everything okay? xx")
            $ contact_Amber.addReply("Wow, you really wanted to see me, huh?", "amrep3aa")
            $ contact_Amber.addReply("Sorry, something came up.", "amrep3ba")

        else:
            $ contact_Amber.newMessage("Hey, it's Amber")
            $ contact_Amber.newMessage("Josh gave me your number")
            $ contact_Amber.newMessage("You know, you never came back, everything okay?")
            $ contact_Amber.addReply("Wow, you really missed me that much, huh?", "amrep3ab")
            $ contact_Amber.addReply("Sorry, something came up.", "amrep3bb")


    if toldlauren == False and laurentoofar == False:
        play sound "sounds/vibrate.mp3"

        $ contact_Lauren.newMessage("Hey")
        $ contact_Lauren.newMessage("Wanna do the personality tests today at noon?")
        $ contact_Lauren.addReply("Yeah, sure.", "larep13a")


        u "(Oh shit, I'm getting a bunch of messages.)"

        label phonex:

        if not contact_Lauren.messages[-1].replies:

            
            u "(Time to get ready.)"

            jump continuez

        else:

            u "(I should probably reply to some of them.)"

            jump phonex





    else:
        label phoney:

        "(Maybe it's Lauren and she wants to talk about what happened? I should definitely check.)"



        if not msgApp.notification:
            
            jump continueaf

        else:
            jump phoney




    ############### Lauren personality tests

    label continuez:

    pause 0.5

    scene s377 # in front of class, door is open
    with Fade (1,0,1)

    pause 0.5

    scene s378 # Laurens inside with some papers
    with dissolve

    u "Hey, Lauren."

    scene s379 # lauren (also showing you) walking towards you
    with dissolve

    la "Heyyy."

    # Kiss in public

    if laurenkissb == True:

        scene s379a # lauren kisses you
        with dissolve
        play sound "sounds/kiss.mp3"
        pause 0.5

        scene s380a
        with dissolve
        u "*Chuckles* Is that how we greet each other now?"

        scene s380 #lauren close up smiling
        with dissolve

        la "I mean we are kinda dating and I do enjoy kissing you, so if you don't have any complaints..."

        scene s380a
        with dissolve

        u "(If we kiss in public, other girls are bound to find out that I'm dating Lauren.)"

        menu:


            "Complaints? I love it.":

                $ laurenpublic = True
                $ addPoint("bf", 1)
                jump ex_a


            "I don't like kissing in public.":

                $ addPoint("tm", 1)
                jump ex_b

        label ex_a:

        u "Complaints? I love kissing you. I can't wait till we say goodbye and I can kiss you again. *Laughs*"

        scene s380
        with dissolve

        la "*Tsk* I feel like you saying you can't wait for us to finish hanging out isn't as romantic as you may think."

        scene s380a
        with dissolve

        u "Hahaha, oops."

        jump ex_ad

        label ex_b:

        u "Uhm, actually do you mind if we don't do that in public?"

        scene s380b # lauren sadish
        with dissolve

        la "Oh.... yeah, of course, I'm sorry, I didn't-"

        scene s380c
        with dissolve

        u "It's not that I don't like kissing you, it's just..."

        u "I'm not really into public displays of affection."

        u "It's uhm... how I was raised."

        scene s380d # lauren suspicious
        with dissolve

        la "Oh, and a little kiss like that is already too much?"

        la "I wasn't talking about a full on make out session, haha"

        la "Also, it's not like anyone will see us here."

        scene s380e
        with dissolve
        u "(Shit, she's pushing back. But if I want to avoid other girls finding out about us, I can't just kiss her in public.)"

        menu:



            "Sorry, not in public.":

                $ laurenpublic = False
                $ addPoint("tm", 1)
                jump ey_a

            "Actually, a kiss is fine.":

                $ laurenpublic = True
                jump ey_b

        label ey_a:
        $ onthelow = True
        if not steam:
            image onthelow = "images/onthelow.webp"
            show onthelow:
                xpos 0
                ypos -200
                linear 0.5 xpos 0 ypos 0
                pause 2.0
                linear 0.5 xpos 0 ypos -200
        else:
            $ achievement.grant("on_the_low")
            $ achievement.sync()

        u "Sorry, but can we just make sure we're alone before we do stuff like that. I just feel uncomfortable even just kissing in public."

        scene s380b
        with dissolve

        la "Okay, yeah. No public display of affection, I get it..."

        scene s380c
        with dissolve

        jump ey_ad

        label ey_b:

        u "Actually, you're right, sorry. A kiss is fine."

        u "Let's just not go overboard, haha."

        scene s380
        with dissolve

        la "Yeah, of course."

        scene s380f # lauren flirty
        with dissolve

        la "At least not in public."

        scene s380g
        with dissolve

        jump ey_bd


    else:
        scene s380a
        with dissolve

        u "So, why exactly are we doing this in a classroom?"

        jump continueag





    ###### continue

    label ex_ad:
    label ey_ad:
    label ey_bd:

    u "Anyways, why exactly are we doing this in a classroom?"

    label continueag:

    $ trolley = True

    scene s380
    with dissolve

    la "Well, my psychology teacher Mrs. Anderson said that she'd leave this room open over the weekend so that we can do the tests on neutral ground."

    scene s380a
    with dissolve

    u "Uhh... neutral ground?"

    scene s380
    with dissolve

    la "You know, your answers can be affected by the environment you're in and an empty classroom should minimize the impact of that."

    scene s380a
    with dissolve

    u "Uhm, sure."

    label gotest:

    scene s380
    with dissolve


    la "Alright, let's get started, shall we?"

    label gokissb:

    scene s381 #you and lauren sitting across each other lauren with paper in her hand.
    with fade

    pause 0.5

    scene s382 # la looking at you
    with dissolve

    la "So I'll tell you a series of statements and you just tell me if you agree or disagree, okay?"

    scene s382a
    with dissolve

    u "Yeah, sounds good."

    scene s382
    with dissolve

    la "Remember, there is no right or wrong, so just answer honestly."

    scene s382b # la reading of papers
    with dissolve
    la "Statement one: I struggle making difficult decisions."

    menu:




        "Agree":

            $ la1 = True
            $ addPoint("bf", 1)
            jump ez_a


        "Disagree":

            $ la1 = False
            $ addPoint("tm", 1)
            jump ez_b

    label ez_a:

    scene s382a
    with dissolve

    u "Agree."

    jump ez_ad

    label ez_b:

    scene s382a
    with dissolve

    u "Disagree."

    label ez_ad:

    scene s382b
    with dissolve
    la "Two: I consider myself an animal lover."

    menu:




        "Agree":

            $ addPoint("bf", 1)
            $ addPoint("bro", 1)
            $ la2 = True
            jump ez_c


        "Disagree":

            $ addPoint("tm", 1)
            $ la2 = False
            jump ez_d

    label ez_c:

    scene s382a
    with dissolve

    u "Uhm... agree I guess."

    jump ez_cd

    label ez_d:

    scene s382a
    with dissolve

    u "Hmm... disagree I guess."

    scene s382
    with dissolve

    la "Huh."

    label ez_cd:

    scene s382b # la reading of papers
    with dissolve
    la "Three: I consider myself a relationship person."

    menu:




        "Agree":

            $ addPoint("bf", 1)
            $ la3 = True
            jump ez_e


        "Disagree":

            $ addPoint("bro", 1)
            $ la3 = False
            jump ez_f

    label ez_e:



    scene s382a
    with dissolve

    u "I definitely do."

    if laurenrs == True:

        scene s382d # Lauren cheeky flirty smile
        with dissolve

        la "Right answer."

        scene s382e
        with dissolve

        u "Woah, I thought there was no right answer."

        scene s382d
        with dissolve

        la "Well, I may have lied about that."

        scene s382e
        with dissolve

        u "*Chuckles* I feel like this personality test is just a pretext so you can vet me."

        scene s382d
        with dissolve

        la "That is certainly a possibility."

        scene s382e
        with dissolve

        u "Am I passing?"

        scene s382d
        with dissolve

        la "So far..."

        jump continueah

    else:

        scene s382
        with dissolve

        la "Haha, I thought you were gonna say no."

        scene s382a
        with dissolve

        u "Really? Why?"

        scene s382
        with dissolve

        la "I don't know, you hang out with a lot of different girls, right?"

        scene s382a
        with dissolve

        u "Yeah, but that doesn't mean that I don't just have eyes for one of them."

        scene s382e
        with dissolve

        pause 0.5

        jump continueaj



    label ez_f:

    scene s382a
    with dissolve

    u "Not really, sooo... disagree."

    if laurenrs == True:

        $ addPoint("tm", 1)

        scene s382f # Lauren passive agressive
        with dissolve

        la "Well that's good to know."

        scene s382g
        with dissolve

        u "Lauren, it's not like-"

        scene s382f
        with dissolve

        la "Let's just move on."

        jump continueak

    else:

        scene s382d
        with dissolve

        la "That's what I thought, haha."

        scene s382e
        with dissolve

        u "Really? Why?"

        scene s382
        with dissolve

        la "I don't know, you hang out with a lot of different girls, right?"

        scene s382a
        with dissolve

        u "Yeah, I guess that's true."

        scene s382e
        with dissolve

        pause 0.5

        jump continueal

    label continueah:
    label continueaj:
    label continueak:
    label continueal:

    scene s382
    with dissolve

    la "So, these were the calibration questions and now we move on to some ethical dilemmas to test your character."

    scene s382a
    with dissolve

    u "What do you mean, test my character?"

    scene s382
    with dissolve

    la "Well we're supposed to cross-reference your answers to these questions with your behavior in difficult situations."

    la "Have you heard of the trolley problem?"


    menu:

        "Yes.":

            jump fa_a

        "No.":

            jump fa_b

    label fa_a:

    scene s382a
    with dissolve

    u "Yeah, it's about choosing who the train runs over right?"

    scene s382
    with dissolve

    la "Uhm yeah, that's broadly it."

    jump fa_ad

    label fa_b:

    scene s382a
    with dissolve

    u "Uhm, no I don't think so."

    scene s382
    with dissolve

    la "Hmm, maybe it's best if you just experience it."

    label fa_ad:

    la "Okay, I want you to rest your head on the table and close your eyes."

    scene s382a
    with dissolve

    u "What? Right now?"

    scene s382
    with dissolve

    la "Yeah. Come on, the personality test is only accurate if you participate."

    scene s382a
    with dissolve

    u "Alright."

    scene black
    with Fade (1,0,0)

    u "So, now what?"

    la "Now, imagine we're on a fast moving train."

    call screen trolleyskip

    label continuetrolley:
    stop music fadeout 2.0

    play music "sounds/train.mp3"
    scene s383a # you looking at lauren mouth closed on train
    with dissolve

    u "Done."

    scene s383
    with dissolve

    la "Turn to the front, imagine there's a big red lever."

    scene s384
    with dissolve

    u "Okay, yeah."

    if la1 == True:

        la "You said that you struggle making difficult decisions, let's see how that impacts your behavior in the following situation."

    else:

        la "You said that you don't struggle making difficult decisions, let's see how if that's still true in the following situation."


    la "As the train's moving forward you come closer to an intersection."

    scene s385 #far from intersection
    with dissolve

    la "The train's heading to the right side of the intersection, where five people are scared for their lives."

    scene s386a # closer, right only, people on the right side appear
    with dissolve

    la "Now, you could flick the lever in order for the train to switch to the left track. However, there's also a person scared for their life on that track."

    scene s387 # even closer, person on the left side appears
    with dissolve

    la "Now it's up to you, will you actively decide to kill someone to save five people or will you stand by and see five times as many people die as needed?"

    scene s388a
    with dissolve
    la "You can decide to switch the lever, but remember, you're on a timer. If you don't switch the lever within a few seconds, the train will keep its current course."
    play sound "sounds/countdown.mp3"
    call screen trolleya

    label trolleyaa: # you don't press the lever
    stop sound
    $ addPoint("bf", 1)
    $ trolleya = False

    scene s388 # hands away from lever
    with dissolve

    pause 0.5

    play sound "sounds/splat.mp3"

    scene s390 # your face full of blood
    with vpunch

    u "Holy fuck..."

    jump continueam

    label trolleyab: # you do press the lever
    stop sound
    $ addPoint("bro", 1)
    $ trolleya = True
    play sound "sounds/lever.mp3"
    scene s388e #you press lever
    with dissolve


    pause 0.5

    play sound "sounds/splat.mp3"

    scene s390a # your face full of blood
    with vpunch

    u "Holy fuck..."

    label continueam:
    stop music

    scene s382a
    with flash

    u "Jesus, that got pretty intense..."

    scene s382
    with dissolve

    la "I know these questions can be difficult..."

    la "Are you okay with doing another one?"


    menu:



        "Yeah, let's do it.":

            jump fb_a

        "I'd rather not.":

            $ trolleyskip = 2
            jump fb_b

    label fb_a:


    scene s382a
    with dissolve

    u "Yeah, let's do it."

    scene s382a
    with dissolve

    la "Alright, imagine yourself back on the train, moving as fast as before."

    scene s383a
    with Fade (1,0,0.5)

    play music "sounds/train.mp3"

    u "Okay, done."

    scene s383
    with dissolve

    la "Look out the front again."

    scene s384
    with dissolve

    u "Alright."

    if la2 == True:

        la "You said that you consider yourself an animal lover. Let's test how much you really love animals."

    else:

        la "You said that you wouldn't consider yourself an animal lover. Hopefully that'll make the next scenario easier."


    la "As the train's moving forward you come closer to another intersection."

    scene s385 #far from intersection
    with dissolve

    la "The train's heading to the right side of the intersection, where this time only one person's scared for their life."

    scene s386b # closer, woman on the right appears
    with dissolve

    la "Just as last time, you can flick the lever in order for the train to switch to the left track. However, this time there's a dog sitting on the other track."

    scene s387a # even closer, dog on the left side
    with dissolve

    la "Now it's up to you, will you actively decide to kill the dog to save a human life or will you idly stand by and let her die?"

    scene s388b
    with dissolve

    la "You can decide to switch the lever, but remember, you're on a timer. If you don't switch the lever within a few seconds, the train will keep its current course."
    play sound "sounds/countdown.mp3"
    call screen trolleyb

    label trolleyba: # you don't press the lever
    stop sound
    $ trolleyb = False
    $ addPoint("tm", 1)
    scene s388 # hands away from lever
    with dissolve

    pause 0.5
    play sound "sounds/splat.mp3"
    scene s390 # your face full of blood
    with vpunch

    u "Ahh fuck!"

    jump continuean

    label trolleybb: # you do press the lever
    stop sound
    $ trolleyb = True
    play sound "sounds/lever.mp3"
    scene s388e #you press lever
    with dissolve

    pause 0.5

    play sound "sounds/splat.mp3"

    scene s390a # your face full of blood
    with vpunch

    if trolleyb == True:
        if la2 == True:
            $ petapublicenemy = True
            if not steam:
                image petapublicenemy = "images/petapublicenemy.webp"
                show petapublicenemy:
                    xpos 0
                    ypos -200
                    linear 0.5 xpos 0 ypos 0
                    pause 2.0
                    linear 0.5 xpos 0 ypos -200
            else:
                $ achievement.grant("peta_public_enemy")
                $ achievement.sync()

    u "Ahh fuck!"

    label continuean:
    stop music

    scene s382a
    with flash

    u "Fucking hell, what is this personality test??"

    scene s382
    with dissolve

    la "Sorry, I know it's a lot but there's only one more to go."
    la "Are you okay with doing the last one?"

    menu:



        "Yeah, okay.":

            jump fb_c

        "I'd rather not.":

            $ trolleyskip = 1
            jump fb_b


    label fb_c:

    scene s382a
    with dissolve

    u "Yeah, okay."

    scene s382a
    with dissolve

    la "Alright, imagine yourself back on the train for one last time, moving as fast as before."

    scene s383a
    with Fade (1,0,0.5)
    play music "sounds/train.mp3"

    u "Okay, I'm on the train."

    scene s383
    with dissolve

    la "Look out the front again."

    scene s384
    with dissolve

    u "Sure thing."

    if la3 == True:

        la "You said that you consider yourself a relationship person, let's put that to the test."

    else:

        la "You said that you wouldn't consider yourself a relationship person, let's put that to the test."


    la "As the train's moving forward you come closer to another intersection."

    scene s385 #far from intersection
    with dissolve

    la "The train's heading to the right side of the intersection, where this time there's five people again, scared for their lives."

    scene s386a
    with dissolve

    la "As always, you can flick the lever in order for the train to switch to the left track. However, this time on the other track it's your ex-girlfriend Emily."

    u "Lauren, what the fuck?! How do you even know about Emily?"

    scene s387b # even closer, emily
    with dissolve

    la "There's no time for this right now. Will you actively decide to kill Emily to save five human lives or will you let the train run it's course, keeping her alive but killing five people in the process?"

    scene s388c
    with dissolve
    la "You can decide to switch the lever, but remember, you're on a timer. If you don't switch the lever within a few seconds, the train will keep its current course."
    play sound "sounds/countdown.mp3"
    call screen trolleyc

    label trolleyca: # you don't press the lever
    stop sound
    $ trolleyc = False
    $ addPoint("bro", 1)

    scene s388 # hands away from lever
    with dissolve

    pause 0.5

    play sound "sounds/splat.mp3"

    scene s390 # your face full of blood
    with vpunch

    u "Oh my god!"

    jump continueao

    label trolleycb: # you do press the lever
    stop sound
    $ trolleyc = True
    $ addPoint("bf", 1)
    play sound "sounds/lever.mp3"
    scene s388e #you press lever
    with dissolve


    pause 0.5

    play sound "sounds/splat.mp3"

    scene s390a # your face full of blood
    with vpunch

    u "Oh my god!"

    label continueao:
    stop music

    scene s382a
    with flash

    u "Lauren, what the fuck?? Emily??"

    scene s382
    with dissolve
    play music "music/mindie5.mp3"

    la "Sorry, I had to ask around in order to find a weak spot. My psych professor said this was essential for the last problem to work."

    menu:



        "At least we're done now.":

            $ addPoint("bf", 1)
            $ laurenokay = True
            jump fc_a

        "That was too far.":

            $ addPoint("tm", 1)
            $ laurenokay = False
            jump fc_b

    label fc_a:

    scene s382a
    with dissolve

    u "*Sigh* It's okay, at least we're done now."

    scene s382
    with dissolve

    la "Exactly, I'll let you know once I have analyzed the results."

    scene s382d
    with dissolve

    la "In the meantime, I could use a coffee, wanna come with me?"

    scene s382e
    with dissolve

    u "Sorry, Lauren. As much as I'd like to, I gotta pick up Imre from the hospital."

    scene s382
    with dissolve

    la "Oh, alright."

    scene s382a
    with dissolve

    u "I'll see you later, okay?"

    scene s382
    with dissolve

    la "Yeah."

    if laurenpublic == True:

        la "Are we still gonna kiss goodbye?"

        scene s382a
        with dissolve

        u "Oh yeah, of course."

        scene s392 # you and her accross table
        with dissolve

        pause 0.5

        scene s392a # kiss
        play sound "sounds/kiss.mp3"

        pause 0.5

        scene s392
        with dissolve

        scene s382a
        with dissolve

        u "Alright, bye."

        scene s382
        with dissolve

        la "Bye."

    jump hospitala


    label fc_b:

    scene s382a
    with dissolve

    u "Lauren, that was too fucking far. What are you, some mad scientist?"

    scene s382h # lauren sorry
    with dissolve

    la "[name], I'm sorry, please."

    la "How about we get a coffee and talk about it?"

    scene s382j
    with dissolve

    u "Uhm, I gotta pick up Imre from the hospital now."

    scene s382h
    with dissolve

    la "Oh, okay, yeah."

    scene s382j
    with dissolve

    u "I'll see you later, okay?"

    scene s382h
    with dissolve

    la "Yeah."

    jump hospitalb


    label skiptrolley:
    $ trolleyskip = 3
    scene s382
    with fade
    jump skiptrolleya

    ######## Skip trolley

    label fb_b:

    scene s382a
    with dissolve

    u "I'd rather not, can we just move on?"

    scene s382
    with dissolve

    la "Yeah of course."

    label skiptrolleya:

    play music "music/mindie5.mp3"



    la "That'd be all. I'll let you know once I have analyzed the results."

    scene s382d
    with dissolve

    la "In the meantime, I could use a coffee, wanna come with me?"

    scene s382e
    with dissolve

    u "Sorry, Lauren. As much as I'd like to, I gotta pick up Imre from the hospital."

    scene s382
    with dissolve

    la "Oh, alright."

    scene s382a
    with dissolve

    u "I'll see you later, okay?"

    scene s382
    with dissolve

    la "Yeah."

    if laurenpublic == True:

        la "Are we still gonna kiss goodbye?"

        scene s382a
        with dissolve

        u "Oh yeah, of course."

        scene s392 # you and her accross table
        with dissolve

        pause 0.5

        scene s392a # kiss
        play sound "sounds/kiss.mp3"

        pause 0.5

        scene s392
        with dissolve

        scene s382a
        with dissolve

        u "Alright, bye."

        scene s382
        with dissolve

        la "Bye."

    jump hospitalc



    ############ Lauren apology option

    label continueaf:
    u "(Damn, it wasn't from Lauren... I wonder if she's still mad at me.)"

    menu:



        "I should go apologize":

            $ apologize = True
            jump fd_a

        "I'll give her time":

            $ apologize = False
            jump fd_b

    label fd_b:

    u "(Maybe I should give her a bit more time.)"

    if autumnmad == False:

        u "(Afterall, Autumn said she'd talk to her.)"

    u "(It's probably time to go pick up Imre with Riley anyways.)"

    jump hospitala

    label fd_a: ############ Lauren Apology

    u "(I should go apologize.)"

    if autumnmad == False:

        u "(Hopefully Autumn has already put in a good word for me.)"

    scene s393 #you infront of Laurens dorm
    with Fade(1,0,1)

    u "(Alright, this is Lauren's dorm.)"

    scene s393a # you knock
    with dissolve
    play sound "sounds/knock.mp3"
    "*Knock knock knock*"

    scene s393
    with dissolve

    unknown "Who is it?"

    u "It's [name], is Lauren there?"

    if laurentoofar == True:

        unknown "Oh, you're the fucker that tried to molest her, right?"

        menu:



            "I'm someone else":

                $ addPoint("tm", 1)
                jump fe_a

            "I didn't mean to":

                $ addPoint("bf", 1)
                jump fe_b

        label fe_a:

        u "What? No, I'm just a friend looking for her, where is she?"

        if kct == "confident":

            call screen popup8

            label popup8:

            unknown "Uhm, alright, she's at some classroom for her personality test thing."

            u "Thanks"

            jump apo



        else:

            unknown "Yeah, right. Fuck off."
            $ apologize = False

            u "(Shit, I don't have time to search her all around campus... I guess I'll have to apologize to her another time.)"

            u "(I should probably pick up Riley so that we can go and get Imre)"

            jump hospitala

        label fe_b:

        u "I didn't mean to... it was a misunderstanding!"

        unknown "Yeah, right. Fuck off."
        $ apologize = False

        u "(Shit, I don't have time to search her all around campus... I guess I'll have to apologize to her another time.)"

        u "(I should probably pick up Riley so that we can go and get Imre)"

        jump hospitala


    else:

        unknown "Oh, you're the guy she cried about, right?"

        unknown "She's not here, I think she's in some classroom for her personality test thing."

        jump apo

    label apo:

    scene s394 ## you pulling on locked door
    with Fade (1,0,1)

    # locked sound

    "This door's locked."

    scene s395 ## you pulling on locked door2
    with dissolve

    #locked sound

    "Locked..."

    scene s377
    with dissolve

    u "(Huh, this one's open...)"

    scene s378
    with dissolve

    u "Lauren?"

    scene s380b
    with dissolve

    if laurentoofar == True:

        if autumnmad == True:

            la "[name], what are you doing here?"

            scene s380c
            with dissolve

            u "Listen, I wanted to apologize, I went too far and I'm sorry."

            u "I- I just got carried away."

            if kct == "loyal":

                call screen popup9

                label popup9:

                scene s380b
                with dissolve

                la "When you continued pushing your hand up my thigh after I told you I didn't want it, you... you made me feel disgusting."

                la "But I know that you're really sorry and I don't wanna be mad at you."

                la "That's if you're okay with just being friends again for now?"

                scene s380c
                with dissolve

                u "Yeah, of course."

                scene s380
                with dissolve

                la "Good."

                scene s380a
                with dissolve

                u "What are you doing here anyways?"

                scene s380d
                with dissolve

                la "For my psychology class I need someone to do a personality test with me which I can then analyze, but my friend just cancelled on me."

                scene s380e
                with dissolve

                u "I can do it."

                scene s380
                with dissolve

                la "Really? That'd be amazing."

                scene s380a
                with dissolve

                u "Yeah, sure."

                jump gotest



            else:

                la "When you continued pushing your hand up my thigh after I told you I didn't want it, you... you made me feel disgusting."

                la "I trusted you and you? You didn't seem to care one bit."

                scene s380c
                with dissolve

                u "Lauren, I-"

                scene s380b
                with dissolve

                la "Please just give me some time. I really don't wanna see you right now."

                scene s380c
                with dissolve

                u "Yeah, of course, sorry."

                u "(Fuck... but it's probably time to go pick up Imre with Riley anyways.)"

                $ laurenmad = True

                jump hospitala

        else:

            la "[name], what are you doing here?"

            scene s380c
            with dissolve

            u "Listen, I wanted to apologize, I went too far and I'm sorry."

            u "I- I just got carried away."

            scene s380b
            with dissolve

            la "When you continued pushing your hand up my thigh after I told you I didn't want it, you... you made me feel disgusting."

            la "But my sister helped me understand that you just made a mistake and I really don't wanna be mad you."

            la "That's if you're okay with just being friends again for now?"

            scene s380c
            with dissolve

            u "Yeah, of course."

            scene s380
            with dissolve

            la "Good."

            scene s380a
            with dissolve

            u "What are you doing here anyways?"

            scene s380d
            with dissolve

            la "For my psychology class I need someone to do a personality test with me which I can then analyze, but my friend just cancelled on me."

            scene s380e
            with dissolve

            u "I can do it."

            scene s380
            with dissolve

            la "Really? That'd be amazing."

            scene s380a
            with dissolve

            u "Yeah, sure."

            jump gotest






    else:

        if autumnmad == True:

            la "[name], what are you doing here?"

            scene s380c
            with dissolve

            u "Listen, I wanted to apologize, I was being insensitive and I'm sorry."

            u "I- I just wanted to be honest with you."

            if kct == "loyal":

                call screen popup10

                label popup10:

                $ laurenrs = True

                scene s380b
                with dissolve

                la "Thinking of you with another girl made me feel really weird."

                la "But I know that I shouldn't be mad because we weren't technically dating or anything."

                scene s380
                with dissolve

                la "So, how about we just continue where we left off?"

                scene s380a
                with dissolve

                u "Yeah, I'd love that."

                u "And don't worry, now that I know how important this is to you, I'll count it as us dating from now on."

                scene s380
                with dissolve

                la "Good."

                scene s380a
                with dissolve

                u "What are you doing here anyways?"

                scene s380d
                with dissolve

                la "For my psychology class I need someone to do a personality test with me which I can then analyze, but my friend just cancelled on me."

                scene s380e
                with dissolve

                u "I can do it."

                scene s380
                with dissolve

                la "Really? That'd be amazing."

                scene s380a
                with dissolve

                u "Yeah, sure."

                scene s379a
                with dissolve

                play sound "sounds/kiss.mp3"

                pause 0.5

                jump gokiss



            else:

                scene s380b
                with dissolve

                la "Thinking of you with another girl made me feel really weird."

                la "I don't wanna be mad at you, but can we just put a pause on the whole dating thing for now and go back to just being friends again?"

                scene s380c
                with dissolve

                u "Uhm... yeah, of course."

                scene s380
                with dissolve

                la "Good."

                scene s380a
                with dissolve

                u "What are you doing here anyways?"

                scene s380d
                with dissolve

                la "For my psychology class I need someone to do a personality test with me which I can then analyze, but my friend just cancelled on me."

                scene s380e
                with dissolve

                u "I can do it."

                scene s380
                with dissolve

                la "Really? That'd be amazing."

                scene s380a
                with dissolve

                u "Yeah, sure."

                jump gotest




        else:

            $ laurenrs = True

            scene s380b
            with dissolve

            la "Thinking of you with another girl made me feel really weird."

            la "But my sister really helped me understand that I shouldn't be mad at you for it."

            scene s380
            with dissolve

            la "So, how about we just continue where we left off?"

            scene s380a
            with dissolve

            u "Yeah, I'd love that."

            u "And don't worry, now that I know how important this is to you, I'll count it as us dating from now on."

            scene s380
            with dissolve

            la "Good."

            scene s380a
            with dissolve

            u "What are you doing here anyways?"

            scene s380d
            with dissolve

            la "For my psychology class I need someone to do a personality test with me which I can then analyze, but my friend just cancelled on me."

            scene s380e
            with dissolve

            u "I can do it."

            scene s380
            with dissolve

            la "Really? That'd be amazing."

            scene s380a
            with dissolve

            u "Yeah, sure."

            scene s379a
            with dissolve

            play sound "sounds/kiss.mp3"

            pause 0.5

            jump gokiss




    label gokiss:

    scene s380a
    with dissolve
    u "*Chuckles* What was that for?"

    scene s380 #lauren close up smiling
    with dissolve

    la "I mean we are kinda dating again and I felt like kissing you, so if you don't have any complaints..."

    scene s380a
    with dissolve
    u "(If we kiss in public, other girls are bound to find out that I'm dating Lauren.)"

    menu:


        "Complaints? I love it.":
            $ laurenpublic = True

            $ addPoint("bf", 1)
            jump fg_a


        "I don't like kissing in public.":
            $ addPoint("tm", 1)

            jump fg_b

    label fg_a:

    u "Complaints? Kissing you rules."

    scene s380f
    with dissolve

    la "That's what I wanted to hear."

    la "Alright, let's get started with the test, shall we?"

    jump gokissb

    label fg_b:

    u "Uhm, actually do you mind if we don't do that in public?"

    scene s380b # lauren sadish
    with dissolve

    la "Oh.... yeah, of course, I'm sorry, I didn't-"

    scene s380c
    with dissolve

    u "It's not that I don't like kissing you, it's just..."

    u "I'm not really into public displays of affection."

    u "It's uhm... how I was raised."

    scene s380d # lauren suspicious
    with dissolve

    la "Oh, and a little kiss like that is already too much?"

    la "I wasn't talking about a full on make out session, haha"

    la "Also, it's not like anyone will see us here."

    scene s380e
    with dissolve
    u "(Shit, she's pushing back. But if I want to avoid other girls finding out about us, I can't just kiss her in public.)"

    menu:



        "Sorry, not in public.":
            $ laurenpublic = False
            $ addPoint("tm", 1)

            jump fh_a

        "Actually, a kiss is fine.":
            $ laurenpublic = True

            jump fh_b

    label fh_a:
    $ onthelow = True
    if not steam:
        image onthelow = "images/onthelow.webp"
        show onthelow:
            xpos 0
            ypos -200
            linear 0.5 xpos 0 ypos 0
            pause 2.0
            linear 0.5 xpos 0 ypos -200
    else:
        $ achievement.grant("on_the_low")
        $ achievement.sync()

    u "Sorry, but can we just make sure we're alone before we do stuff like that. I just feel uncomfortable even just kissing in public."

    scene s380b
    with dissolve

    la "Okay, yeah. No public display of affection, I get it..."

    la "Let's just get started with the test."

    jump gokissb

    label fh_b:

    u "Actually, you're right, sorry. A kiss is fine."

    u "Let's just not go overboard, haha."

    scene s380
    with dissolve

    la "Yeah, of course."

    scene s380f # lauren flirty
    with dissolve

    la "At least not in public."

    scene s380g
    with dissolve

    u "Hahaha."

    scene s380f
    with dissolve

    la "Let's get started with the test, shall we?"

    jump gokissb


    ############## Bus to hospital with Riley

    label hospitala:
    label hospitalb:
    label hospitalc:
    stop music fadeout 2.0

    play music "sounds/bus.mp3"
    scene s399 #Riley and and MC are on the bus. They look at each other affectionately. MC readjusts awkwardly.
    with Fade (1,0,1)

    pause 0.5

    scene s399a
    with dissolve

    u "So you think Imre will be alright?"

    scene s400 #Riley close up emphatic
    with dissolve

    ri "You know Imre, he'll be fine. I'm sure
         once he's fully recovered he'll be
         twice as strong as before."

    scene s400c # riley gigle mouth closed
    with dissolve

    ri "*Giggles*"

    u "*Laughingly* Yeah, you're right. He's relentless. You should see how he
         trains me."

    scene s400b
    with dissolve

    ri "I bet that's a show."

    scene s400c
    with dissolve

    u "Yeah... he's got one tough head on his shoulder."

    scene s400d #riley awkward contempalting
    with dissolve

    ri "Yes, yes he does..."

    scene s400e
    with dissolve

    u " Mhmmm..."

    pause 0.5
    stop music fadeout 2.0

    play sound "sounds/busstop.mp3"

    "*Bus stops*"

    scene s401 # Riley and Mc get out of the bus
    with dissolve

    pause 0.5

    play music "music/m7punk.mp3"

    scene s402 # Imre half limping towards them in front of hospital
    with fade

    u "Aye! Imre."

    scene s403 # Imre close up
    with dissolve

    imre "What's up bro? Hey Riley. Thanks for coming guys."

    scene s404 # Riley close up
    with dissolve

    ri "Yeah, of course."

    scene s405 # Imre hand hug thing with u,
    with dissolve

    play sound "sounds/slap.mp3"
    pause 0.5

    scene s405a # pull in for the hug
    with dissolve

    imre "*Winces in pain*"

    scene s403b # Imre smiling in pain
    with dissolve

    imre "Ah, yeah, shit. Still tryin' to
recover."

    scene s403c
    with dissolve

    u "My bad."

    scene s403b
    with dissolve

    imre "It's cool, just a couple of broken
         ribs."

    scene s403c
    with dissolve

    u "Glad you're feeling a bit better."

    scene s403
    with dissolve

    imre "Yeah, me too."

    scene s404b
    with dissolve

    ri "Alright, I know you two love birds have
         a lot to catch up on, but I really
         don't wanna miss the next bus."

    scene s404c
    with dissolve

    imre "*Laughs*"

    u "*Laughingly* Yeah, alright."

    scene s406 #Riley, MC, and Imre walk back to the bus stop.
    with fade

    stop music fadeout 2.0

    pause 1.0



    scene s407 #Riley, MC, and Imre are now all sitting on the bus towards the back.
    with fade



    play music "sounds/bus.mp3"

    pause 1.0

    scene s408 # A few seats ahead sits a girl that from the back appears to be Emily.
    with dissolve

    pause 1.0

    scene s408a # focus on emily
    with dissolve

    u "(Is that Emily?)"

    play sound "sounds/swoosh.mp3"

    show screen fantasyOverlay

    scene s409 #MC and Emily are in a park, eating ice cream. Emily puts some on MC's nose. MC chases her as she runs away laughing.
    with flash

    pause 0.5

    scene s409a
    with dissolve

    em "You got some ice cream on your nose?"


    scene s409b # both laughing, you wiping the ice cream off
    with dissolve

    u "*Laughs* Hey!"

    play sound "sounds/swoosh.mp3"

    scene s410 #MC and Emily are dancing in the moonlight. MC presses his face into her hair as he holds her.
    with flash


    pause 0.5

    scene s410a # they both look at each other romantically
    with dissolve

    pause 1.0
    play sound "sounds/swoosh.mp3"
    scene s411 #MC and Emily are sitting on the couch watching a movie. Emily has her head on his shoulder.
    with flash

    pause 0.5

    scene s411a #She lifts her head for a moment and stares at him affectionately
    with dissolve

    pause 1.0

    scene s411b #mc looks back at Emily
    with dissolve

    pause 0.5

    u "What?"

    scene s411c
    with dissolve

    em "Nothing."

    scene s411b
    with dissolve

    u "Why are you looking at me like that?"

    scene s411c
    with dissolve

    em "I just love you."

    scene s411b
    with dissolve

    u "I love you too."

    scene s411d #kiss
    with dissolve

    play sound "sounds/kiss.mp3"

    pause 0.5
    play sound "sounds/swoosh.mp3"
    hide screen fantasyOverlay
    scene s408a
    with flash

    u "*Takes a deep breath*"

    scene s413 # you get up
    with dissolve

    u "I'll be right back guys."

    scene s413a # you walking forwards
    with dissolve

    pause 0.5

    scene s414 #he taps fake emily on the shoulder
    with dissolve

    u "Emily?"

    scene s414a # fake emily turns around
    with dissolve

    unknown "Huh?"

    scene s414b
    with dissolve

    u "Oh, sorry, I thought you were someone else."

    scene s415 #mc walks back
    with dissolve

    pause 0.5
    stop music fadeout 2.0

    scene s416 # Imre, Mc and Riley in front of your dorm
    with Fade(1,0,1)

    ri "I'll see you guys later."

    scene s416a
    with dissolve

    u "Yeah, sounds good."

    scene s416b
    with dissolve

    imre "Bye, Riley."
    play music "music/m4punk.mp3"

    scene s417 # you opening dorm door but Imre is walking somewhere else?
    with dissolve

    u "Where are you going?"

    scene s418 #Imre turns around closeup
    with dissolve

    imre "Don't worry about it."

    scene s418a
    with dissolve

    u "Imre-"

    scene s418
    with dissolve

    imre "I said don't worry about it."

    scene s418a
    with dissolve

    u "You really think you're gonna go fight
         that guy right now? You just got out
         of the hospital. You need to rest."

    scene s418
    with dissolve

    imre "I'm fine."

    scene s418a
    with dissolve

    u "Imre, you're in no condition to fight!"

    scene s418b # Imre angry
    with dissolve

    imre "I'm not gonna let this motherfucker think
         he can just come and lay one on me."

    scene s418c
    with dissolve

    u "You ever think if you try and fight
         like this, he's just gonna lay a
         second one on you?"

    scene s418b
    with dissolve

    imre "Don't fucking tell me when I can fight or not.
         I know myself. This is about me and
         him. I'll make him remember who
         he's fucking with."

    scene s418c
    with dissolve

    u "Imre, you need to chill out for a
         second and think this through. You've gone crazy!"

    scene s418b
    with dissolve

    imre "I have thought this through. I'm not
         gonna sit here looking like a little
         bitch. I'm gonna make him regret what he did."

    scene s418c
    with dissolve

    u "Look, I get that you want revenge, but you literally just got out of the hospital... if he hits you in the wrong spot that could kill you!"

    scene s418b
    with dissolve

    imre "Whatever, this son of a bitch will pay right now."

    scene s418d # Imre walks away
    with dissolve

    u "Imre! Come on."

    scene s418e # Imre gone
    with dissolve

    u "Fuck..."

    stop music fadeout 2.0

    scene s419  # u pacing around in room
    with fade

    pause 0.5

    play music "music/m9punk.mp3"
    scene s419a
    with dissolve

    pause 0.5

    scene s419b
    with dissolve

    pause 0.5

    scene s419c # sits down on bed
    with dissolve

    u "*Sighs*"

    scene s419d # pulls out phone
    with dissolve

    pause 0.5

    scene s419e # phone to head
    with dissolve

    play sound "sounds/calling.mp3"

    pause 0.5

    scene s420 # close up head
    with dissolve

    stop sound

    au "Hello?"

    scene s420a
    with dissolve

    u "Uhm... Hey Aubrey."

    scene s420
    with dissolve

    au "Something wrong? You sound tense."

    scene s420a
    with dissolve

    u "Uh... no, no. Everything's good. Uhm... I just had a quick question."

    scene s420
    with dissolve

    au "Yeah? What's up?"

    scene s420a
    with dissolve

    u "Do you uhm... happen to know a guy named Adam?"

    scene s420
    with dissolve

    au "*Hesitates*"

    au "Yeah. Why?"

    scene s420a
    with dissolve

    u "Do you know where he lives?"

    scene s420
    with dissolve

    au "Dorms, corridor B I believe. Why, what happened?"

    scene s420c # face tenses
    with dissolve

    u "Where in corridor B?"

    scene s420b
    with dissolve

    au "Uhm, first door on the left, I think. [name], what's going on?"

    scene s420c
    with dissolve

    u "Wait, did you say, first door on the
left?"

    scene s420b
    with dissolve

    au "Yes. Why? Is something wrong? Just
tell me!"

    scene s420d #name puts the phone down
    with dissolve

    pause 0.5

    scene s420e # looks at the door
    with dissolve

    pause 0.5

    scene s421 # show door
    with dissolve

    u "*Mumbles* That's right across from us."

    scene s420f # phone back at his head
    with dissolve

    au "Hello? Is everything okay??"

    scene s420g
    with dissolve

    u "Hey, sorry, I'll call you back Aubrey.
         I gotta go."

    scene s420e # phone away from ear
    with dissolve

    au "Don't-"

    scene s420e2 # phone away from ear
    with dissolve

    play sound "sounds/rejectcall.mp3"
    u "*Hangs up*"

    scene s422 # mc charges towards door
    with dissolve

    pause 0.5

    scene s396
    with dissolve

    pause 0.5

    scene s396a
    with dissolve

    u "*Deep breath*"

    menu:



        "Confront Adam":

            $ addPoint("bro", 1)
            $ confrontadam = True
            jump fj_a

        "Leave it":

            $ addPoint("bf", 1)
            $ confrontadam = False
            jump fj_b

    label fj_b:

    scene s397b
    with dissolve

    u "(It's not like I can do anything against him anyways...)"

    u "(Maybe I should tell the school, but Imre would be super pissed and Adam might try and kill me for it.)"
    u "(On the other hand, if I don't tell the school Imre might actually get himself killed trying to get revenge.)"

    menu:



        "Tell the school":

            $ tellschool = True
            $ addPoint("bf", 1)
            jump fl_a

        "Keep it to yourself":

            $ tellschool = False
            $ addPoint("bro", 1)
            jump fl_b


    label fj_a:

    scene s397
    with dissolve

    play sound "sounds/knock.mp3"

    "*Knock knock knock*"

    play sound "sounds/dooropen.mp3"

    scene s398
    with dissolve

    ad "Wrong dorm, pissbag. Now fuck off."


    menu:



        "Punch him":

            $ fightadam = True
            $ addPoint("tm", 1)
            jump fk_a

        "Talk to him":

            $ addPoint("bf", 1)
            jump fk_b

    label fk_b:
    scene s398a
    with dissolve

    u "You're Adam, right? Look, you beat up my friend Imre and-"

    scene s398b
    with dissolve

    ad "Ahh yeah, I remember, that was quite fun."

    scene s398
    with dissolve

    ad "So what are you gonna do about it, bitch?"

    menu:



        "Punch him":

            $ fightadam = True
            $ addPoint("tm", 1)
            jump fk_a

        "Threaten to tell school":

            $ addPoint("bf", 1)
            jump fk_c

    label fk_c:

    scene s398a
    with dissolve

    u "You find him and apologize or I'll tell the fucking school and you'll get kicked out and maybe even assault charges thrown your way."

    scene s398
    with dissolve

    ad "You do that and I'll come back for you and unlike your friend, you'll never leave the fucking hospital again."

    ad "Now fuck off."

    play sound "sounds/slam.mp3"

    scene s398c
    with vpunch

    u "(Fuck...)"

    u "(Great, if I tell the school about
     this, Imre will be pissed at me and Adam will try to fucking kill me, but if I don't, Imre
     is gonna get himself killed trying to
     get revenge.)"


    menu:



        "Tell the school":

            $ tellschool = True
            $ addPoint("bf", 1)
            jump fl_a

        "Keep it to yourself":

            $ tellschool = False
            $ addPoint("bro", 1)
            jump fl_b

########## Adam fight

    label fk_a:
    stop music fadeout 2.0
    image af2 = Movie(play="images/af2.webm", start_image="images/af2start.webp", image="images/af2pic.webp", loop = False)


    play sound "sounds/hs.mp3"
    scene af0close
    with hpunch

    pause 0.5

    scene af1
    with dissolve

    ad "Oh pissbag, you're about to die."

    scene af2
    $ renpy.pause(1.5)
    scene af2pic
    with hpunch

    pause 0.5

    scene af4
    with dissolve

    pause 0.5

    $ adamtut = True

    if fighttom == False:

        call screen skiptut2

    label fkcon:

    $ firstfight = False
    $ _game_menu_screen = "ingmenu"



    scene af4

    call screen af


    label playf2:
        $ youdmg = 0
        $ adamdmg = 0
        $ adamstance = renpy.random.choice([1, 2, 3, 4])
        $ adamattack = renpy.random.choice([1, 2, 3, 4])
        call screen af2

    label easy2:
        $ reaction = 3
        $ reactiona = 3.2
        $ adamhealth = 5
        $ youhealth = 5
        call screen af3

    label moderate2:
        $ reaction = 1.3
        $ reactiona = 1.5
        $ adamhealth = 6
        $ youhealth = 3
        call screen af3

    label hard2:
        $ reaction = 0.5
        $ reactiona = 0.7
        $ adamhealth = 8
        $ youhealth = 2
        call screen af3


    label simadamfight:
        $ simadamfight = True
        $ stance = 1
        $ adamhealth = 6
        $ youhealth = 3
        jump adamsimstart

    label autowinadam:
        $ simadamfight = True
        $ stance = 1
        $ youhealth = 100000
        $ adamhealth = 3
        jump adamsimstart

    label keys1:
        call screen keys1
    label keys2:
        call screen keys2
    label keys3:
        call screen keys3
    label keys4:
        call screen keys4





    #### Define videos for adam fight
    $ stance = 1
    image af5 = Movie(play="images/af5.webm", start_image="images/af5start.webp", image="images/af5pic.webp", loop = False)
    image af6 = Movie(play="images/af6.webm", start_image="images/af6start.webp", image="images/af6pic.webp", loop = False)
    image af7 = Movie(play="images/af7.webm", start_image="images/af7start.webp", image="images/af7pic.webp", loop = False)
    image af8 = Movie(play="images/af8.webm", start_image="images/af8start.webp", image="images/af8pic.webp", loop = False)
    image af9 = Movie(play="images/af9.webm", start_image="images/af9start.webp", image="images/af9pic.webp", loop = False)
    image af10 = Movie(play="images/af10.webm", start_image="images/af10start.webp", image="images/af10pic.webp", loop = False)
    image af11 = Movie(play="images/af11.webm", start_image="images/af11start.webp", image="images/af11pic.webp", loop = False)
    image af12 = Movie(play="images/af12.webm", start_image="images/af12start.webp", image="images/af12pic.webp", loop = False)
    image af13 = Movie(play="images/af13.webm", start_image="images/af13start.webp", image="images/af13pic.webp", loop = False)
    image af14 = Movie(play="images/af14.webm", start_image="images/af14start.webp", image="images/af14pic.webp", loop = False)
    image af15 = Movie(play="images/af15.webm", start_image="images/af15start.webp", image="images/af15pic.webp", loop = False)
    image af16 = Movie(play="images/af16.webm", start_image="images/af16start.webp", image="images/af16pic.webp", loop = False)
    image youfinishadam = Movie(play="images/youfinishadam.webm", start_image="images/youfinishadamstart.webp", image="images/youfinishadampic.webp", loop = False)
    image adamfinish = Movie(play="images/adamfinish.webm", start_image="images/adamfinishstart.webp", image="images/adamfinishpic.webp", loop = False)


    label adamkick1:

        if adamdmg >= adamhealth:

            scene youfinishadam
            $ renpy.pause(1)
            play sound "sounds/fall.mp3"
            $ stance = 0
            $ youdmg = 0
            scene youfinishadamclose
            with vpunch
            $ renpy.pause()

            jump youfinishadam

        else:
            $ adamdmg += 1
            scene af11
            $ renpy.pause(0.7)
            play sound "sounds/ks.mp3"
            scene af11close
            with hpunch

            pause 0.5
            jump adamattack

    label adamkick2:

            scene af12
            $ renpy.pause(0.7)
            play sound "sounds/ks.mp3"
            scene af12close
            with hpunch

            pause 0.5
            jump adamattack


    label adamhook1:

        if adamdmg >= adamhealth:

            scene youfinishadam
            $ renpy.pause(1)
            play sound "sounds/fall.mp3"
            $ stance = 0
            $ youdmg = 0
            scene youfinishadamclose
            with vpunch
            $ renpy.pause()

            jump youfinishadam

        else:
            $ adamdmg += 1
            scene af5
            $ renpy.pause(0.7)
            play sound "sounds/hs.mp3"
            scene af5close
            with hpunch

            pause 0.5
            jump adamattack

    label adamhook2:

            scene af6
            $ renpy.pause(0.7)
            play sound "sounds/bs.mp3"
            scene af6close
            with hpunch

            pause 0.5
            jump adamattack

    label adamjab1:

        if adamdmg >= adamhealth:

            scene youfinishadam
            $ renpy.pause(1)
            play sound "sounds/fall.mp3"
            $ stance = 0
            $ youdmg = 0
            scene youfinishadamclose
            with vpunch
            $ renpy.pause()

            jump youfinishadam

        else:
            $ adamdmg += 1
            scene af7
            $ renpy.pause(0.7)
            play sound "sounds/js.mp3"
            scene af7close
            with hpunch

            pause 0.5
            jump adamattack

    label adamjab2:

            scene af8
            $ renpy.pause(0.7)
            play sound "sounds/bs.mp3"
            scene af8close
            with hpunch

            pause 0.5
            jump adamattack

    label adambody1:

        if adamdmg >= adamhealth:

            scene youfinishadam
            $ renpy.pause(1)
            play sound "sounds/fall.mp3"
            $ stance = 0
            $ youdmg = 0
            scene youfinishadamclose
            with vpunch
            $ renpy.pause()

            jump youfinishadam

        else:
            $ adamdmg += 1
            scene af9
            $ renpy.pause(0.7)
            play sound "sounds/hs.mp3"
            scene af9close
            with hpunch

            pause 0.5
            jump adamattack

    label adambody2:

            scene af10
            $ renpy.pause(0.7)
            play sound "sounds/bs.mp3"
            scene af10close
            with hpunch

            pause 0.5
            jump adamattack

    label letsgoadam:
    $ simadamfight = False

    label adamsimstart:
    label adamattack:
    $ stance = 2

    if youdmg >= youhealth:

        scene adamfinish
        $ renpy.pause(1.3)
        play sound "sounds/fall.mp3"
        $ stance = 0
        $ youdmg = 0
        scene adamfinishclose
        with vpunch

        $ renpy.pause()


        jump adamfinish

    else:

        if adamattack == 1:

            scene af13
            $ renpy.pause(0.6)

            scene af13pic
            $ adamstance = renpy.random.choice([1, 2, 3, 4])
            $ simyou = renpy.random.choice([1, 2, 3, 4, 5, 6])

            if simadamfight == True:
                if simadam == 1 or simadam == 2 or simadam == 3:
                    jump adamhookhit
                if simadam == 4 or simadam == 5 or simadam == 6:
                    jump adamhookblocked

            else:
                call screen adamattack




        if adamattack == 2:

            scene af14
            $ renpy.pause(0.5)

            scene af14pic
            $ adamstance = renpy.random.choice([1, 2, 3, 4])
            $ simyou = renpy.random.choice([1, 2, 3, 4, 5, 6])

            if simadamfight == True:
                if simadam == 1 or simadam == 2 or simadam == 3:
                    jump adamjabhit
                if simadam == 4 or simadam == 5 or simadam == 6:
                    jump adamjabblocked

            else:
                call screen adamattack

        if adamattack == 3:

            scene af15
            $ renpy.pause(0.7)

            scene af15pic
            $ adamstance = renpy.random.choice([1, 2, 3, 4])
            $ simyou = renpy.random.choice([1, 2, 3, 4, 5, 6])

            if simadamfight == True:
                if simadam == 1 or simadam == 2 or simadam == 3:
                    jump adambodyhit
                if simadam == 4 or simadam == 5 or simadam == 6:
                    jump adambodyblocked

            else:
                call screen adamattack

        if adamattack == 4:

            scene af16
            $ renpy.pause(0.6)

            scene af16pic
            $ adamstance = renpy.random.choice([1, 2, 3, 4])
            $ simyou = renpy.random.choice([1, 2, 3, 4, 5, 6])

            if simadamfight == True:
                if simadam == 1 or simadam == 2 or simadam == 3:
                    jump adamkickhit
                if simadam == 4 or simadam == 5 or simadam == 6:
                    jump adamkickblocked

            else:
                call screen adamattack


    label adamhookhit:

        play sound "sounds/hs.mp3"
        $ youdmg += 1
        scene adamhookhit
        with hpunch

        pause 0.5
        $ stance = 1
        $ adamattack = renpy.random.choice([1, 2, 3, 4])
        $ simadam = renpy.random.choice([1, 2, 3, 4])

        if simadamfight == True:
            if adamstance == 1:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamjab1
            if adamstance == 2:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamjab2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamhook1
            if adamstance == 3:
                if simyou == 1:
                    jump adamjab2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adambody1
            if adamstance == 4:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamjab2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamkick1
        else:
            call screen youattack2

    label adamhookblocked:

        play sound "sounds/bs.mp3"
        scene adamhookblock
        with hpunch

        pause 0.5
        $ stance = 1
        $ adamattack = renpy.random.choice([1, 2, 3, 4])
        $ simadam = renpy.random.choice([1, 2, 3, 4])

        if simadamfight == True:
            if adamstance == 1:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamjab1
            if adamstance == 2:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamjab2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamhook1
            if adamstance == 3:
                if simyou == 1:
                    jump adamjab2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adambody1
            if adamstance == 4:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamjab2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamkick1
        else:
            call screen youattack2

    label adamjabhit:

        play sound "sounds/js.mp3"
        $ youdmg += 1
        scene adamjabhit
        with hpunch

        pause 0.5
        $ stance = 1
        $ adamattack = renpy.random.choice([1, 2, 3, 4])
        $ simadam = renpy.random.choice([1, 2, 3, 4])

        if simadamfight == True:
            if adamstance == 1:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamjab1
            if adamstance == 2:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamjab2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamhook1
            if adamstance == 3:
                if simyou == 1:
                    jump adamjab2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adambody1
            if adamstance == 4:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamjab2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamkick1
        else:
            call screen youattack2

    label adamjabblocked:

        play sound "sounds/bs.mp3"
        scene adamjabblock
        with hpunch

        pause 0.5
        $ stance = 1
        $ adamattack = renpy.random.choice([1, 2, 3, 4])
        $ simadam = renpy.random.choice([1, 2, 3, 4])

        if simadamfight == True:
            if adamstance == 1:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamjab1
            if adamstance == 2:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamjab2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamhook1
            if adamstance == 3:
                if simyou == 1:
                    jump adamjab2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adambody1
            if adamstance == 4:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamjab2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamkick1
        else:
            call screen youattack2

    label adambodyhit:

        play sound "sounds/hs.mp3"
        $ youdmg += 1
        scene adambodyhit
        with hpunch

        pause 0.5
        $ stance = 1
        $ adamattack = renpy.random.choice([1, 2, 3, 4])
        $ simadam = renpy.random.choice([1, 2, 3, 4])

        if simadamfight == True:
            if adamstance == 1:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamjab1
            if adamstance == 2:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamjab2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamhook1
            if adamstance == 3:
                if simyou == 1:
                    jump adamjab2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adambody1
            if adamstance == 4:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamjab2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamkick1
        else:
            call screen youattack2

    label adambodyblocked:

        play sound "sounds/bs.mp3"
        scene adambodyblock
        with hpunch

        pause 0.5
        $ stance = 1
        $ adamattack = renpy.random.choice([1, 2, 3, 4])
        $ simadam = renpy.random.choice([1, 2, 3, 4])

        if simadamfight == True:
            if adamstance == 1:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamjab1
            if adamstance == 2:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamjab2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamhook1
            if adamstance == 3:
                if simyou == 1:
                    jump adamjab2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adambody1
            if adamstance == 4:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamjab2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamkick1
        else:
            call screen youattack2

    label adamkickhit:

        play sound "sounds/ks.mp3"
        $ youdmg += 1
        scene adamkickhit
        with hpunch

        pause 0.5
        $ stance = 1
        $ adamattack = renpy.random.choice([1, 2, 3, 4])
        $ simadam = renpy.random.choice([1, 2, 3, 4])

        if simadamfight == True:
            if adamstance == 1:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamjab1
            if adamstance == 2:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamjab2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamhook1
            if adamstance == 3:
                if simyou == 1:
                    jump adamjab2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adambody1
            if adamstance == 4:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamjab2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamkick1
        else:
            call screen youattack2

    label adamkickblocked:

        play sound "sounds/ks.mp3"
        scene adamkickblock
        with hpunch

        pause 0.5
        $ stance = 1
        $ adamattack = renpy.random.choice([1, 2, 3, 4])
        $ simadam = renpy.random.choice([1, 2, 3, 4])

        if simadamfight == True:
            if adamstance == 1:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamjab1
            if adamstance == 2:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamjab2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamhook1
            if adamstance == 3:
                if simyou == 1:
                    jump adamjab2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamkick2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adambody1
            if adamstance == 4:
                if simyou == 1:
                    jump adambody2
                if simyou == 2:
                    jump adamhook2
                if simyou == 3:
                    jump adamjab2
                if simyou == 4 or simyou == 5 or simyou == 6:
                    jump adamkick1
        else:
            call screen youattack2




    label fl_b: # keep it to yourself
    $ tellschool = False

    u "(It's best if I keep to myself. Telling the school would turn both Imre and Adam against me...)"

    stop music fadeout 2.0

    u "(I need to find Imre before he finds Adam.)"

    jump findimre


    label fl_a:  # tell the school

    $ tellschool = True

    stop music fadeout 2.0

    $ snitch = True
    if not steam:
        image snitch = "images/snitch.webp"
        show snitch:
            xpos 0
            ypos -200
            linear 0.5 xpos 0 ypos 0
            pause 2.0
            linear 0.5 xpos 0 ypos -200
    else:
        $ achievement.grant("snitch")
        $ achievement.sync()


    u "(I need to tell the school, it's the only way to sort this out.)"

    scene s423 #mc before counselors office, opening door
    with Fade(1,0,1)
    play sound "sounds/dooropen.mp3"
    pause 0.5
    play music "music/m15punk.mp3"
    scene s424 #cam behind MC walks into the counselor's office. She is sitting at her desk.
    with dissolve

    co "Have a seat."

    scene s425 # counselor smiloing close up
    with dissolve

    co "How can I help you today?"

    scene s425a
    with dissolve

    u "Well, kinda hard to say. Not trying to
         start any issues, but I need to protect my friend."

    scene s425b # counselor contemplating
    with dissolve

    co "Mhm. I see. I can only help you, if you tell me the
         problem. Also you can be assured that whatever you tell me, your identity will be
         kept confidential. Feel free to share
         what's weighing on you."

    scene s425c
    with dissolve

    u "A close friend of
         mine got jumped by this guy. He got
         beat up pretty bad, broken ribs and
         all."

    scene s425b #counselor empathy
    with dissolve

    co "I'm very sorry to hear that."

    scene s425c
    with dissolve

    u "And now my friend, who isn't even
         fully recovered, is out trying to get
         revenge. He was this close to internal bleeding last time, if he gets beat up again..."

    scene s425b
    with dissolve

    co "I understand. I'll do my best to ensure your friend does not suffer any more violence."

    co "What is your friend's name?"


    scene s425c
    with dissolve

    u "Imre, Imre Varga."

    scene s425b
    with dissolve

    co "And do you happen to know the name of the other person involved? Assault is a serious crime."

    scene s425c
    with dissolve

    u "Uh yeah, his name's Adam. I don't know his last name, but he lives in corridor B."

    scene s425
    with dissolve

    co "Thank you, that will be all. I'm sorry about what happened
         to your friend, please try and
         keep a close eye on him until we can
         get this all sorted."

    scene s425a
    with dissolve

    u "So uhm... what will happen to Adam?"

    scene s425b
    with dissolve

    co "That won't be up to me, but expulsion is definitely a possibility."
    co "If your friend is willing to pursue this legally, I'd assume assault charges might also be on the table. However, I'm not a lawyer, so I can't speak with certainty on that."

    scene s425c
    with dissolve

    u "Alright, thanks. No one will know that I was the one who told you about this, right?"

    scene s425
    with dissolve

    co "Of course not. Your name will remain strictly confidential."

    scene s426 # Mc stands up
    with dissolve

    u "Good, thank you."

    scene s426a # mc walks away
    with dissolve

    co "You made the right decision coming here."

    scene s426b #mc turns around
    with dissolve

    u "Sorry?"

    scene s426c #co tlaking with mc turned around she's smiling and convinced / reassuring
    with dissolve

    co "A lot of students never tell us about their problems until it's too late to solve them. It's not \"uncool\" or \"cowardly\" to speak up."

    co "It's brave."

    scene s426b
    with dissolve

    u "Uhm, thanks."

    scene s426a # mc walks away
    with dissolve

    stop music fadeout 0.5

    u "(I need to find Imre.)"

    jump findimre


    label youfinishadam: #### You beat adam
    $ renpy.end_replay()
    $ winadam = True

    pause 0.5

    u "Never touch Imre again, you piece of shit."

    play music "music/m12punk.mp3"

    scene s427 #you in front of your dorm door about to open the door
    with dissolve

    unknown "Yo, did I just watch you knock out Adam?"

    scene s427a #you turn around
    with dissolve

    u "Look, he-"

    scene s428a #chrisclose up mouth closed impressed smile
    with dissolve

    u "Oh shit, you're Chris, president of the Wolves, right?"

    scene s428
    with dissolve

    ch "Yeah, and you're a freshman. How the hell did you manage to beat up Adam?"

    scene s428a
    with dissolve

    u "I don't know... I don't normally fight, it's just..."

    u "He hurt my friend."

    scene s428
    with dissolve

    ch "Christ man, you're a natural. Have you considered joining a frat?"

    menu:



        "Yeah, I'm interested.":

            $ addPoint("bro", 1)
            jump fm_a

        "Not really.":

            $ addPoint("bf", 1)
            jump fm_b

    label fm_b:
    scene s428a
    with dissolve

    u "Not really, I'm not a fighter, okay? This was a one time thing, I had no choice."

    scene s428b #chris convincing / understanding
    with dissolve

    ch "Not a single freshman last year could have beaten up Adam. You have talent, man. Come to our rush party on Tuesday, I promise you, you won't regret it."

    scene s428a
    with dissolve

    u "I promised my friend I'd go anyways. So yeah, I'll be there."

    scene s428
    with dissolve

    ch "That's good. I'll see you then, come talk to me when you're there."

    scene s428a
    with dissolve

    u "Yeah, will do."

    scene s427
    with dissolve

    u "(Actually, I should probably go find Imre and tell him about what happened.)"

    jump findimre

    label fm_a:

    scene s428a
    with dissolve

    u "Yeah, I'm definitely interested. Especially in the Wolves."

    scene s428b #chris convincing
    with dissolve

    ch "That's what I like to hear. Not a single freshman last year could have beaten up Adam. I assume you're gonna be at our rush party on Tuesday?"

    scene s428a
    with dissolve

    u "Yeah, I'll definitely be there."

    scene s428
    with dissolve

    ch "Cool, I'll see you then. Come talk to me when you're there."

    scene s428a
    with dissolve

    u "Yeah, will do."

    scene s427
    with dissolve

    stop music fadeout 2.0

    u "(Actually, I should probably go find Imre and tell him about what happened.)"

    jump findimre

    label adamfinish: ###Adam beats you
    $ renpy.end_replay()
    $ winadam = False

    pause 1.0
    play music "music/m12punk.mp3"

    scene s429 # showing Adam kicking you on the ground
    with vpunch

    u "*winces in pain*"

    scene s430 #FIRST PErson: looking at Adam spitting on you
    with dissolve
    play sound "sounds/spit.mp3"
    ad "*Spits*"

    scene s430b #adam disgusting grin
    with dissolve

    ad "You really thought you could beat me up, huh?"

    scene s429 # showing Adam kicking you on the ground
    with vpunch

    u "*winces in pain* Ahhh!"

    scene s430b
    with dissolve

    ad "Let's see how many ribs you're gonna break today."

    scene s430c
    with dissolve

    unknown "Leave him alone, Adam!"

    scene s431 # First Person : Looking at chris approaching from the doors (you're still on the ground)
    with dissolve

    ch "Or I'll beat you up myself."

    scene s430d # adam looking at chris (your bottom perspective stillk)
    with dissolve

    ad "You think I'm scared of you, Chris?"

    scene s432 # no longer your perspective: Chris and Adam about 1-2 metres apart staring each other down.
    with dissolve

    pause 1.0

    scene s432a
    with dissolve

    ch "Step. Away."

    scene s432
    with dissolve

    pause 0.5

    scene s432b # Adam walks back to his dorm
    with dissolve

    pause 0.5

    scene s433 # FIRST PERSON: Chris reaches with his hand to help you up
    with dissolve

    ch "You okay?"

    scene s433a # you grab his hand
    with dissolve

    u "Yeah, thanks."

    scene s428c
    with dissolve

    u "You're Chris, president of the Wolves, right?"

    scene s428b
    with dissolve

    ch "Yeah, that's me."

    ch "So, why did Adam wanna beat you up? Did you look at him the wrong way?"

    scene s428c
    with dissolve

    u "He beat up my friend. And when I confronted him, I just kinda lost it and punched him."

    scene s428b
    with dissolve

    ch "Fair enough. Do you fight a lot?"

    scene s428c
    with dissolve

    u "Not really. That's probably why I was the one on the ground and not him."

    scene s428b
    with dissolve

    ch "Trust me, not a single freshman last year could have beaten up Adam. He's not an easy opponent."

    scene s248c
    with dissolve

    u "Yeah..."

    scene s428b
    with dissolve

    ch "Look, people like Adam... they don't stop. At some point he'll find you by yourself and he'll try to fuck you up even more."

    ch "You should come to our rush party on Tuesday. As a Wolf, you'll learn how to defend yourself."

    scene s428c
    with dissolve

    u "Really? You see me get beaten up and you still want me to join the Wolves, who's only requirement for joining is being good at fighting?"

    scene s428b
    with dissolve

    ch "Well, you gave him a nosebleed, so you must have landed at least one good punch."

    ch "Also, fighting can be learned. We care about loyalty. And you trying to avenge your friend like that, without much fighting experience, that's honorable."

    ch "So, Tuesday?"

    scene s428c
    with dissolve

    u "Alright, I'll be there."

    scene s428
    with dissolve

    ch "Good, I'll see you then. Come talk to me when you're there."

    scene s428a
    with dissolve

    u "Yeah, will do."

    scene s427
    with dissolve

    u "(Actually, I should probably go find Imre and tell him about what happened.)"

    stop music fadeout 2.0

    u "(But first, I gotta wash the blood of my face.)"

    jump findimre

    label findimre:

    play music "music/m16punk.mp3"

    #### montage of you looking for Imre

    scene s434 #looking somewhere on campus
    with fade

    u "Imre?"

    scene s435 # talking to Elijah on campus
    with Dissolve (1)

    u "Have you seen Imre?"

    scene s436 # looking else where on campus
    with Dissolve (1)

    u "Imreee? Are you here?"

    scene s437 # talking to Mr. Lee
    with Dissolve (1)

    u "Mr. Lee, any chance you've seen Imre?"

    scene s438 # you looking into caferita seeing imre dissapointed sitting on a table
    with Dissolve (1)

    u "Imre, there you are!"

    scene s439 # Imre close up mad
    with dissolve

    imre "I can't fucking find him. He must be hiding or some shit. No one seems to know where he lives either."
    imre "Fucking bullshit, they're all just scared of him!"

    scene s439a
    with dissolve

    if fightadam == True:

        if winadam == True:
            $ imremad = True
            u "Actually, I uhm... I found Adam."

            scene s439b # Imre surprised but still a bit mad
            with dissolve

            imre "Where? Where is he?"

            scene s439c
            with dissolve

            u "He lives in the dorm opposite to us. But I already paid him a visit."

            scene s439b
            with dissolve

            imre "Fuck you mean you paid him a visit?"

            scene s439c
            with dissolve

            u "I beat him up. Knocked him out. Told him to leave you alone."

            scene s439
            with dissolve

            imre "You did what?! What the fuck is wrong with you?!"

            scene s439a
            with dissolve

            u "What?? That's what you wanted, right? He got beaten up."

            scene s440 # Imre stands up angry
            with dissolve

            imre "I wanted to beat him up! He was mine! You knew he was mine!"

            scene s440a
            with dissolve

            u "Imre, I-"

            scene s440
            with dissolve

            imre "You pretend like you're not a fighter, like you're not a Wolf..."

            imre "Well turns out you were right about one of those. Go join the fucking Apes!"

            scene s441 # Imre storms off
            with dissolve

            u "Imre!"

            scene s441a # Imre gone
            with dissolve

            u "Fuck!"

            jump continueba

        else:
            u "Actually, I uhm... I found Adam."

            scene s439b # Imre surprised but still a bit mad
            with dissolve

            imre "Where? Where is he?"

            scene s439c
            with dissolve

            u "He lives in the dorm opposite to us. I confronted him when I found out, but it got out of control and he beat me up."

            u "Luckily Chris stepped in, otherwise he would've sent me to the hospital as well."

            scene s439d # Imre slight cocky smile
            with dissolve

            imre "Well that was fucking stupid of you, wasn't it?"

            imre "I told you, I don't need your help, I got this."

            scene s439e
            with dissolve

            u "Yeah sorry, it's just... I don't wanna pick you up from the hospital again."

            scene s439d
            with dissolve

            imre "I'll get a cab next time."

            scene s439e
            with dissolve

            u "You know that's not what I meant."

            scene s439f # imre serious
            with dissolve

            imre "Look, I really appreciate that you're trying to help, but I know what I'm doing, okay?"

            scene s439g
            with dissolve

            u "Okay."

            u "Are you gonna try and fight him now?"

            scene s439f
            with dissolve

            imre "I have to do this."

            scene s439g
            with dissolve

            u "Can I at least-"

            scene s439f
            with dissolve

            imre "[name], please. Go take a walk. Let me handle this myself."

            scene s439g
            with dissolve

            u "Alright. Good luck, man."

            jump continueba


    else:
        if tellschool == True:

            $ imremad = True
            u "Actually, I uhm... I found Adam."

            scene s439b # Imre surprised but still a bit mad
            with dissolve

            imre "Where? Where is he?"

            scene s439c
            with dissolve

            u "He lives in the dorm opposite to us. But there's something else I need to tell you."

            u "I told the school about what happened. They're gonna take care of it."

            scene s439
            with dissolve

            imre "You did what?! What the fuck is wrong with you?!"

            scene s439a
            with dissolve

            u "Look, I know that's not what you wanted, but-"

            scene s440 # Imre stands up angry
            with dissolve

            imre "I told you to stay out of it! Now if I touch him the school will kick both of us out!"

            scene s440a
            with dissolve

            u "Imre, I-"

            scene s440
            with dissolve

            imre "I knew you weren't a fucking fighter, but I didn't know you were such a snitch!"

            imre "Stay the fuck out of my life!"

            scene s441 # Imre storms off
            with dissolve

            u "Imre!"

            scene s441a # Imre gone
            with dissolve

            u "Fuck!"

            jump continueba

        else:

            u "Actually, I uhm... I found Adam."

            scene s439b # Imre surprised but still a bit mad
            with dissolve

            imre "Where? Where is he?"

            scene s439c
            with dissolve

            u "You really wanna know? He lives in the dorm opposite to us."

            u "But you can't do this, man! At least not by yourself, let me come with you and we'll take him on together."

            scene s439d # Imre slight cocky smile
            with dissolve

            imre "I told you, I don't need your help, I got this."

            scene s439e
            with dissolve

            u "I get that, but... I don't wanna pick you up from the hospital again."

            scene s439d
            with dissolve

            imre "I'll get a cab next time."

            scene s439e
            with dissolve

            u "You know that's not what I meant."

            scene s439f # imre serious
            with dissolve

            imre "Look, I really appreciate that you're trying to help, but I know what I'm doing, okay?"

            scene s439g
            with dissolve

            u "Okay."

            u "Are you gonna try and fight him now?"

            scene s439f
            with dissolve

            imre "I have to do this."

            scene s439g
            with dissolve

            u "Can I at least-"

            scene s439f
            with dissolve

            imre "[name], please. Go take a walk, distract yourself. Let me handle this myself."

            scene s439g
            with dissolve

            u "Alright. Good luck, man."

            jump continueba




    label continueba:
    stop music fadeout 2.0



    scene s442 # you on a park bench depressed
    with Fade (1,0,1)
    play music "music/mindie1.mp3"

    queue music [ "music/mindie2.mp3", "music/mindie3.mp3" ]

    if imremad == True:

        u "(How the fuck did everything go so wrong??)"
        u "(A couple hours ago Imre was so happy to see me and now he probably hates me...)"

        u "(I need to go and talk to him again. He's probably in our dorm.)"


    else:

        u "(What am I doing? Adam could be beating Imre senseless at our dorms right now.)"

        u "(I know Imre said he didn't want me to help him, but I can't just do nothing.)"

    ##text message # You can text Amber you don't have time for this.


    $ noexit = True



    scene s442a # you stand up
    with dissolve

    play sound "sounds/vibrate.mp3"

    u "(Maybe that's Imre...)"




    if chloemad == True:
        $ contact_Amber.newMessage("Hey, you alone? xx")
        $ contact_Amber.addReply("I'm at the park, but I'm by myself.", "amrep8a")



        call screen contactsscreen

        label phoneaa:


        show screen messager(contact=contact_Amber)
        pause 0.5
        u "(Fuck, I don't have time for Amber right now, but I really wanna find out what surprise she has.)"
        hide screen messager
        if imremad == True:
            u "(I gotta make a decision. Should I find Imre, or keep talking to Amber?)"
        else:
            u "(I gotta make a decision. Should I help Imre, or keep talking to Amber?)"

        jump endaa

    else:

        $ contact_Chloe.newMessage("I got some free time right now :)")
        $ contact_Chloe.newMessage("Wanna go swimming?")
        $ contact_Chloe.addReply("Any chance we could do it later? Or tomorrow?", "clrep5a")


        call screen contactsscreen

        label phoneab:
        show screen messager(contact=contact_Chloe)
        pause 0.5
        u "(Fuck, I don't have time for this right now, but going swimming with Chloe sounds like the best possible way to get closer to her.)"

        hide screen messager

        if imremad == True:
            u "(I gotta make a decision. Should I find Imre, or meet Chloe?)"
        else:
            u "(I gotta make a decision. Should I help Imre, or meet Chloe?)"
        jump endaa

    label endaa:

    $ noexit = False
    if v06 == True:
        jump script06
    else:
        jump end_credits


    label end_credits:

    stop music fadeout 2.0
    image credits = Movie(play="images/credits.webm", Loop = True)


    play music "music/vocal.mp3"

    if not steam:
        show screen getaccess
        with dissolve
        " "
        hide screen getaccess


    show credits:
        ypos 50
        xalign 0.5

    call screen thx
