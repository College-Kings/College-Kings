
# steam and developer options

default persistent.ep = 7

default steam = True

default developer = False

define config.steam_appid = 1463120

#Splashscreen
label splashscreen:
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


# The script of the game goes in this file.

###########
###########




default flash = Fade(.25, 0, .75, color="#fff")

label pref:

call screen preferences

label rmlon:
    $ realmode = True
    $ config.rollback_enabled = False
    $ wton = False
    $ showkct = False
    call screen preferences

label rmloff:
    $ realmode = False
    $ config.rollback_enabled = True
    call screen preferences

label scenegal:
    call screen spoiler

label spoilergo:
    call screen scenegal

label showkcton:
    $ showkct = True
    call screen preferences

label showkctoff:
    $ showkct = False
    call screen preferences



label rollbackfalse:
    define config.rollback_enabled = False
    call screen preferences

label rollbacktrue:
    define config.rollback_enabled = True
    call screen preferences


label exitphone:
$ renpy.jump("".join([phoneexit]))

label frcontinue:
$ renpy.jump("".join([endfrlabel]))

label frgoback:
$ renpy.jump("".join([backfrlabel]))

label achievements:
    $ achievementsnot = 0
    call screen achievements

label homescreen:
    #### fr1
    if phoneexit == "phonec":
        scene s50
    if phoneexit == "phoned":
        scene s55
    if phoneexit == "phonedtwo":
        scene s56
    if phoneexit == "phonee":
        scene s58
    ###### fr2
    if phoneexit == "phoneh":
        scene s100
    if phoneexit == "phonej":
        scene s102
    if phoneexit == "phonel":
        scene s104
    if phoneexit == "phonem":
        scene s105
    if phoneexit == "phonen":
        scene s106

    call screen phone



label emrep1a:
$ nohardfeelings = True
if steam == False:
    image nohardfeelings = "images/nohardfeelings.png"
    show nohardfeelings:
        xpos 0
        ypos -200
        linear 0.5 xpos 0 ypos 0
        pause 2.0
        linear 0.5 xpos 0 ypos -200
else:
    $ achievement.grant("no_hard_feelings")
    $ achievement.sync()


$ contact_Emily.newMessage(emilyMessage2a)
call screen messager(contact_Emily)

label emrep1b:
$ openwound = True
if steam == False:
    image openwound = "images/openwound.png"
    show openwound:
        xpos 0
        ypos -200
        linear 0.5 xpos 0 ypos 0
        pause 2.0
        linear 0.5 xpos 0 ypos -200
else:
    $ achievement.grant("open_wound")
    $ achievement.sync()
$ addPoint("tm", 1)
$ contact_Emily.newMessage(emilyMessage2b)
call screen messager(contact_Emily)

label stats:
$ statsnot = 0
$ freeroamtut = 0
call screen stats

label larep1a:
$ contact_Lauren.newMessage(laurenMessage1)
call screen messager(contact_Lauren)

label larep2a:
$ contact_Lauren.newMessage(laurenMessage2)
call screen messager(contact_Lauren)

label larep3a:
$ addPoint("bf", 1)
call screen messager(contact_Lauren)

label larep3b:
call screen messager(contact_Lauren)

label larep4a:
$ larep4 = 1
$ addPoint("bf", 1)
$ contact_Lauren.newMessage(laurenMessage5a)
call screen messager(contact_Lauren)

label larep4b:
$ larep4 = 2
$ addPoint("tm", 1)
$ contact_Lauren.newMessage(laurenMessage5b)
call screen messager(contact_Lauren)

label larep5b:
$ contact_Lauren.newMessage(laurenMessage6)
call screen messager(contact_Lauren)

label jurep1a:
$ addPoint("bf", 1)
call screen messager(contact_Julia)

label jurep1b:
$ addPoint("bro", 1)
call screen messager(contact_Julia)

label ryrep1a:
$ ryanreply = 1
$ contact_Ryan.newMessage(ryanMessage2)
$ contact_Ryan.newMessage(ryanMessage3)
call screen messager(contact_Ryan)

label ryrep3a:
call screen messager(contact_Ryan)

label ryrep4a:
$ addPoint("bro", 1)
$ contact_Ryan.newMessage(ryanMessage5)
call screen messager(contact_Ryan)

label ryrep4b:
$ addPoint("tm", 1)
$ contact_Ryan.newMessage(ryanMessage5)
call screen messager(contact_Ryan)

label ryrep5a:
$ addPoint("bro", 1)
call screen messager(contact_Ryan)

label ryrep5b:
$ addPoint("tm", 1)
$ contact_Ryan.newMessage(ryanMessage6)
call screen messager(contact_Ryan)

label larep8a:
$ larep8 = 1
$ meetlauren = True
$ addPoint("bf", 1)
$ contact_Lauren.newMessage(laurenMessage11)
call screen messager(contact_Lauren)

label larep8b:
$ larep8 = 2
$ mixedfeelings = True
if steam == False:
    image mixedfeelings = "images/mixedfeelings.png"
    show mixedfeelings:
        xpos 0
        ypos -200
        linear 0.5 xpos 0 ypos 0
        pause 2.0
        linear 0.5 xpos 0 ypos -200
else:
    $ achievement.grant("mixed_feelings")
    $ achievement.sync()
$ addPoint("tm", 1)
$ contact_Lauren.newMessage(laurenMessage9)
call screen messager(contact_Lauren)

label larep9a:
$ contact_Lauren.newMessage(laurenMessage10)
call screen messager(contact_Lauren)

label jorep3a:
$ addPoint("bro", 1)
$ contact_Josh.newMessage(joshMessage4)
call screen messager(contact_Josh)

label jorep3b:
$ addPoint("bf", 1)
$ contact_Josh.newMessage(joshMessage5)
call screen messager(contact_Josh)

label jorep4a:
call screen messager(contact_Josh)

label jorep5a:
$ addPoint("bro", 1)
$ contact_Josh.newMessage(joshMessage6)
$ contact_Josh.newMessage(joshMessage7)
call screen messager(contact_Josh)

label jorep5b:
$ addPoint("tm", 1)
$ contact_Josh.newMessage(joshMessage6)
$ contact_Josh.newMessage(joshMessage7)
call screen messager(contact_Josh)

label jorep7a:
call screen messager(contact_Josh)

label aubrep2a:
$ addPoint("bro", 1)
$ contact_Aubrey.newMessage(aubreyMessage3)
$ contact_Aubrey.newMessage(aubreyMessage4)
call screen messager(contact_Aubrey)

label aubrep2b:
$ addPoint("bf", 1)
$ contact_Aubrey.newMessage(aubreyMessage5)
call screen messager(contact_Aubrey)

label aubrep5a:
$ contact_Aubrey.newMessage(aubreyMessage7)
call screen messager(contact_Aubrey)

label aubrep7a:
$ aubrep7 = 1
call screen messager(contact_Aubrey)


label aubrep8a:
$ costumeaubrey = True
$ addPoint("bf", 1)
$ contact_Aubrey.newMessage(aubreyMessage10)
call screen messager(contact_Aubrey)

label aubrep8b:
$ costumeaubrey = False
$ addPoint("tm", 1)
$ contact_Aubrey.newMessage(aubreyMessage9)
call screen messager(contact_Aubrey)

label aubrep12aa:
$ contact_Aubrey.newMessage(aubreyMessage13a)
$ contact_Aubrey.newMessage(aubreyMessage14a)
call screen messager(contact_Aubrey)

label aubrep12a:
$ contact_Aubrey.newMessage(aubreyMessage13)
$ contact_Aubrey.newMessage(aubreyMessage14)
call screen messager(contact_Aubrey)

label aubrep12ab:
$ contact_Aubrey.newMessage(aubreyMessage13b)
$ contact_Aubrey.newMessage(aubreyMessage14b)
call screen messager(contact_Aubrey)

label aubrep14a:
$ aubrep14 = 1
call screen messager(contact_Aubrey)
label aubrep14aa:
$ aubrep14 = 1
call screen messager(contact_Aubrey)
label aubrep14ab:
$ aubrep14 = 1
call screen messager(contact_Aubrey)

label clrep2a:
$ contact_Chloe.newMessage(chloeMessage3)
call screen messager(contact_Chloe)

label clrep3a:
$ clrep3 = 1
$ contact_Chloe.newMessage(chloeMessage4)
call screen messager(contact_Chloe)


label jorep8a:
$ addPoint("bro", 1)
$ contact_Josh.newMessage(joshMessage9)
$ contact_Josh.newMessage(joshMessage10)
call screen messager(contact_Josh)

label jorep8b:
$ contact_Josh.newMessage(joshMessage11)
$ contact_Josh.newMessage(joshMessage12a)
$ contact_Josh.newMessage(joshMessage12)
call screen messager(contact_Josh)

label jorep12a:
$ jorep12 = 1
$ joisreply = 0
$ addPoint("bro", 1)
$ contact_Josh.newMessage(joshMessage9)
$ contact_Josh.newMessage(joshMessage10)
call screen messager(contact_Josh)

label jorep12b:
$ contact_Josh.newMessage(joshMessage13)
$ contact_Josh.newMessage(joshMessage14)
call screen messager(contact_Josh)

label jorep14a:
$ jorep14 = 1
$ joisreply = 0
$ contact_Josh.newMessage(joshMessage9)
$ contact_Josh.newMessage(joshMessage10)
call screen messager(contact_Josh)

label jorep14b:
$ jorep14 = 2
$ joisreply = 0
$ addPoint("bf", 1)
$ contact_Josh.newMessage(joshMessage15)
call screen messager(contact_Josh)

label amrep3a:
$ addPoint("bro", 1)
$ contact_Amber.newMessage(amberMessage4)
call screen messager(contact_Amber)

label amrep3b:
$ contact_Amber.newMessage(amberMessage5)
call screen messager(contact_Amber)

label amrep4a:
$ addPoint("tm", 1)
$ contact_Amber.newMessage(amberMessage6)
call screen messager(contact_Amber)

label amrep4b:
$ contact_Amber.newMessage(amberMessage7)
call screen messager(contact_Amber)

label amrep5a:
$ contact_Amber.newMessage(amberMessage7)
call screen messager(contact_Amber)

label amrep3aa:
$ addPoint("bro", 1)
$ contact_Amber.newMessage(amberMessage4a)
call screen messager(contact_Amber)

label amrep3ba:
$ contact_Amber.newMessage(amberMessage5a)
call screen messager(contact_Amber)

label amrep4aa:
$ addPoint("tm", 1)
$ contact_Amber.newMessage(amberMessage6a)
call screen messager(contact_Amber)

label amrep4ba:
$ contact_Amber.newMessage(amberMessage7a)
call screen messager(contact_Amber)

label amrep5aa:
$ contact_Amber.newMessage(amberMessage7a)
call screen messager(contact_Amber)

label amrep3ab:
$ addPoint("bro", 1)
$ contact_Amber.newMessage(amberMessage4b)
call screen messager(contact_Amber)

label amrep3bb:
$ contact_Amber.newMessage(amberMessage5b)
call screen messager(contact_Amber)

label amrep4ab:
$ addPoint("tm", 1)
$ contact_Amber.newMessage(amberMessage6b)
call screen messager(contact_Amber)

label amrep4bb:
$ contact_Amber.newMessage(amberMessage7b)
call screen messager(contact_Amber)

label amrep5ab:
$ contact_Amber.newMessage(amberMessage7b)
call screen messager(contact_Amber)

label larep13a:
$ larep13 = 1
$ contact_Lauren.newMessage(laurenMessage14)
call screen messager(contact_Lauren)

label amrep8a:
$ contact_Amber.newMessage(amberMessage9)
$ contact_Amber.newMessage(amberMessage10)
jump phoneaa


# The game starts here.

label start:
    $ addReplies()
    $ _game_menu_screen = "ingmenu"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #### Pre Questions

    call screen realmode

label rme:
    $ realmode = True
    $ config.rollback_enabled = False
    $ showkct = False
    jump starta

label rmd:
    $ realmode = False
    $ config.rollback_enabled = True
    $ showkct = True
    jump starta

#Chapter 1
label starta:

    # Part 0: Dream
    play music "music/msexy.mp3"
    $ fantasy = True
    scene s0a
    with dissolve

    em "I know what I did was bad..."

    em "But I'll do anything to make it up to you."

    scene s0b
    with dissolve

    em "Anything."
    $ fantasy = False
    #Part 1: Meeting Julia
    stop music fadeout 2.0
    #$ renpy.random.shuffle (playlist1)
    #$ renpy.music.queue (playlist1, fadein=2)
    scene s1
    with Fade(1, 0, 1)

    "Honey?"

    scene s1b
    with dissolve

    play music "music/m15punk.mp3"

    $ name = renpy.input("What's your name?", default="Alex").strip() or "Alex"
    $ kiwiiUsers["MC"]["username"] = name

    u "Hmm...?"

    scene s2
    with dissolve
    ju "Breakfast is ready!"


    scene s1a
    with dissolve
    u "Mhmm... I'll be right down."
    u "(What am I doing dreaming about Emily?!)"

    scene s3a
    with Fade(1, 0, 1)
    ju "Good morning, honey."

    scene s3
    with dissolve

    u "Morning, Julia."

    scene s3a
    with dissolve


    ju "Are you excited for today?"

    scene s3
    with dissolve

    u "Excited?"

    scene s3a
    with dissolve

    ju "Honey, it's your first day of college. That's a big deal!"

    scene s3
    with dissolve

    u "I guess you're right."

    scene s3b
    with dissolve
    ju "Have you packed all your stuff? Have you printed out all the documents you need? Have you-"

    scene s3c
    with dissolve

    u "Julia, it's fine. I packed yesterday."

    scene s3d
    with dissolve
    ju "Look at you, all grown-up. I'm so proud of you."

    scene s3f
    with dissolve

    ju "You better not forget to come visit."
    u "I'll think about it, if you make lasagna."

    scene s3d
    with dissolve

    ju "I'm sure that could be arranged."

    ju "Anyway, we should get ready, you don't wanna be late on your first day of college!"

    scene s3e
    with dissolve
    u "Oh you're dropping me off? I was gonna take the train."
    scene s3d
    with dissolve

    ju "No way you're robbing me of the chance to embarrass you in front of your new friends."
    scene s3e
    with dissolve
    u "Thanks, Julia... I'll be 20 minutes."

    scene s11
    with Fade(1, 0, 1)
    u "(I better not lose this bag, Julia loves it.)"

    play sound "sounds/vibrate.mp3"

    u "(Huh?)"

    $ wt = 1
    $ contact_Emily.newMessage(emilyMessage1)
    # $ msgnot = 1
    # $ emilymsgnot = 1
    # $ emilymsg = 1
    # $ emisreply = 1
    # $ emilymsg1 = "Hey...\nI know we haven’t talked much after we broke up, but I just wanted to let you know that I didn’t get into Stanford, so I’ll be going to San Vallejo as well.\nGuess I’ll see you there. :)"
    # $ emreply1a = "Yeah... I’ll see you there."
    # $ emilymsg2 = "Cool :)"
    # $ emreply1b = "You cheated on me.\nGo to hell!"
    # $ emilymsg3 = "Ugh :/"
    $ showphone = True

    call screen phone

$ phoneexit = "phonea"

label phonea:
    $ wt = 0
    $ phonetut = 0
    $ showphone = False
    stop music fadeout 2.0
    scene s11
    with dissolve
    u "(Fuck, I really don't want to see her again after what happened.\nHopefully I can avoid her as much as possible.)"
    scene carback
    show s14
    with fade
    play music "sounds/driving1.mp3"

    ju "You know, when I was in college, there were these fraternities and sororities that everyone wanted to join."

    ju "I always thought they were stupid. Binge drinking, idiotic challenges and fighting..."
    hide s14
    show s14a
    with dissolve
    u "Mhm...."
    hide s14a
    show s14
    with dissolve
    ju "You're not planning on joining one of those, are you?"
    $ wt = 2
    menu:

        "Could be fun":
            $ wt = 0
            jump aa_a

        "No":
            $ wt = 0
            jump aa_b

    label aa_a:
        hide s14
        show s14a
        with dissolve
        $ addPoint("tm", 1)

        u "I don't know... it might be fun."

        jump aa_da

    label aa_b:
        hide s14
        show s14a
        with dissolve
        $ addPoint("bf", 1)

        u "No, I don't think so, Julia."

        jump aa_db

    label aa_da:
    label aa_db:

    hide s14a
    show s15
    with dissolve
    $ wt = 3
    $ phoneexit = "phoneb"
    $ showphone = True
    # $ kcttut = 0
    $ statsApp.unlock()
    $ realkcttut = 0
    play sound "sounds/vibrate.mp3"
    $ statsnot = 1
    ju "Fraternities can be dangerous, honey."
    label phoneb:
    $ wt = 0
    $ showphone = False
    hide s15
    show s14
    with dissolve
    ju "My boyfriend in college almost got suspended because he had to steal one of the lecturer's underwear."
    hide s14
    show s14a
    with dissolve
    u "*Chuckles*"
    hide s14a
    show s14
    with dissolve
    ju "Believe me, it's not as fun as it sounds."

    hide s14
    show s14a
    with dissolve
    u "Relax, Julia. Over the last couple years colleges have become a lot stricter."

    u "I doubt stuff like that happens anymore."

    hide s14a
    show s14b
    with dissolve
    ju "Well, that would be a relief."

    hide s14b
    show s16
    with dissolve
    ju "Anyways..."

    hide s16
    show s14b
    with dissolve
    ju "Sophia told me that Josh is also going to San Vallejo."

    hide s14b
    show s14c
    with dissolve
    u "You hang out with Josh's mom?"

    hide s14c
    show s15
    with dissolve
    ju "We go to the same nail salon."
    image collegepan = Movie(play="images/collegepan.webm")

    hide s15
    show s14a
    with dissolve
    u "Whatever... me and Josh haven't really talked much lately."

    u "(I wonder if he's still dealing...)"
    stop music fadeout 2.0
    car "*stops*"
#########Intro
    scene homepage2
    with Fade(1, 0, 1)
    ju "Well, this is it. San Vallejo College."


    image intro = Movie(play="images/intro.webm", start_image="images/s1.jpg", image="images/s1.jpg", loop = False)


    show intro
    with flash
    " "

################Intro
    scene s17a
    with Fade(1, 0, 1)

    u "Alright, let me grab my bag and I'm ready."

    scene s17
    with dissolve

    play music "music/mfunk.mp3"

    ju "Don't worry, I'll get it for you, honey."

    play sound "sounds/trunkopen.mp3"

    scene s18
    with dissolve
    " "

    scene s19
    with dissolve

    ju "Here you go."

    scene s19a
    with dissolve

    u "Thanks, Julia."

    scene s20
    with dissolve

    ju "Enjoy college, honey."

    ju "Don't forget to visit me."

    scene s20a
    with dissolve

    u "I won't, I'll see you soon."


#Part 3:

    scene s25
    with Fade(1, 0, 1)

    u "(Holy shit. I'm actually a college freshman now.)"

    u "(And already... so many hot girls.)"

    scene s26
    with dissolve

    ca "I'm telling you, she was trying to suck me off, while I was taking a shit."

    scene s27
    with dissolve
    ma "Dude, that's my sister you're talking about!"

    stop music fadeout 2.0


    scene s28
    with hpunch

    " "

    scene s29
    with dissolve

    play music "music/m3punk.mp3"

    ca "Yo, watch where you're fucking walking, bitch!"

    scene s30
    with dissolve

    u "Sorry man, I didn't mean to..."

    scene s29
    with dissolve

    ca "Fuck you, if you want a fucking problem, I'll give you a fucking problem!"

    scene s31
    with dissolve

    aut "Leave him alone Cameron."
    aut "Otherwise I'll post the pics and I'm sure you don't want that."

    scene s32
    with dissolve

    ca "Fine..."

    ca  "Next time, Mommy won't be there to save you, asshole."

    stop music fadeout 2.0

    $ wt = 4

    scene s33
    with dissolve

    aut "You okay?"
    scene s33a
    with dissolve

    play music "music/mlove1.mp3"

    u "Yeah...thanks."

    u "I'm [name] by the way."

    scene s33c
    with dissolve

    aut "I'm Autumn."
    aut "You're new here right?"

    scene s33d
    with dissolve

    u "Yeah, is it that obvious?"


    scene s33c
    with dissolve
    aut "It's just that most people would avoid bumping into Cameron at any cost."


    menu:

        "Flirt":

            jump ad_a

        "Inquire":

            jump ad_b

    label ad_a:
        scene s33d
        with dissolve

        u "It's not as bad if you get to meet a pretty girl afterwards."

        scene s33
        with dissolve

        aut "Uhm..."

        scene s33d
        with dissolve

        u "(Way to make her uncomfortable, Casanova.)"

        scene s33c
        with dissolve

        aut "Anyways, I gotta go. Nice to meet you."

        jump ad_da

    label ad_b:
        scene s33d
        with dissolve

        u "Why is that?"

        scene s36
        with dissolve

        aut "He's uhm-"

        aut "Let's just say he doesn't have the best of tempers."
        scene s33c
        with dissolve
        aut "Anyways, I gotta go. Nice to meet you."

        jump ad_db

    label ad_da:
    label ad_db:

        scene s39
        with dissolve

        u "(Damn... she was really cute. Hopefully I'll get to see her again.)"

        u "(I should probably go to my induction class right now.)"

        stop music fadeout 2.0

###Part 4

    scene s40
    with Fade(1, 0, 1) #you're late and everyone's looking at you rose bend over laptop

    u "Sorry for being late, I couldn't find the classroom."

    scene s41
    with dissolve  #Rose annoyed bend over laptop

    play music "music/m6punk.mp3"

    ro "It's fine, just take a seat."

    scene s41a
    with dissolve # rose looking at laptop

    ro "We won't be starting 'til I can fix this damn laptop."

    scene s42
    with fade
#you next to ryan"

    ry "Nice job being late on your first day, man."

    scene s42a
    with dissolve

    u "Thanks..."

    scene s43
    with dissolve

    ry "I'm Ryan."

    scene s42a
    with dissolve

    u "I'm [name]."

    scene s43
    with dissolve

    ry "10 minutes late, sitting in the back row. Man, you'd make a perfect Ape."

    scene s43a
    with dissolve

    u "Ape? Are you calling me a chimpanzee?"

    scene s44a
    with dissolve

    ry "Nooo, the Apes, you don't know them?"

    ry "They're the best fraternity in the entire University. They get so many girls."

    ry "And...their president is the current Fight King."

    scene s44c
    with dissolve

    u "Fight King? What are you talking about?"

    scene s44b
    with dissolve

    ry "Don't tell me you don't know about the Summer Showdown?!"

    scene s43a
    with dissolve

    u "Never heard of it."

    scene s44
    with dissolve

    ry "Duuude!"

    scene s44a
    with dissolve

    ry "Every year the two most popular fraternities, the Apes and the Wolves, host an MMA fighting tournament called the Summer Showdown."

    ry "The winner of the final fight is crowned the Fight King."

    scene s44c
    with dissolve

    u "Well that seems pretty violent..."

    scene s43
    with dissolve

    ry "You don't get it... The Fight King gets sooo many girls."
    ry "I can't wait to become an Ape and compete."

    scene s43a
    with dissolve

    u "You want to fight?"

    scene s44a
    with dissolve

    ry "Did you not hear what I said? Sooo many girls."

    scene s44c
    with dissolve

    u "Yeah, but do you even know how to fight?"

    scene s43
    with dissolve

    ry "Not yet, but the fraternities train you. After all, they want someone from their frat to win."

    scene s43a
    with dissolve

    u "Knock yourself out... Fighting is not really for me."

    scene s44b
    with dissolve

    ry "Trust me dude, if you're not a fighter, you're a nobody."

    ry "You won't be invited to any parties and you won't get any hot girls."

    scene s46
    with fade
    ro "It seems that Elijah here fixed the laptop and we can start the induction. Thank you, Elijah."


    menu:


        "Make fun of Elijah":

            jump ag_a

        "Stay quiet":

            jump ag_b

    label ag_a:
        scene s46a
        with dissolve
        u "Wow Elijah, way to start the fun."
        $ funofelijah = 1
        $ addPoint("tm", 1)

        scene s46b
        with dissolve
        el "..."

        jump ag_da

    label ag_b:
    $ funofelijah = 0
    label ag_da:

    scene s84a
    with dissolve
    ro "Here at San Vallejo College most courses start their first year with the same three classes: Biology, Economics and History."

    ro "Alcohol, smoking and any form of violence whilst on College grounds is strictly forbidden."

    ro "Classes start tomorrow, so you'll have plenty of time to explore the campus today."

    ro "Now, let's move on to some of the boring administrative stuff..."

    stop music fadeout 2.0
    scene clocka
    with fade

    play sound "sounds/clock2.mp3"

    pause (0.5)

    scene clockb
    with dissolve

    pause (0.5)

    scene clockc
    with dissolve

    pause (0.5)

    scene clockd
    with dissolve

    pause (0.5)
    stop sound
    scene clocke
    with dissolve

    scene s48
    with fade # ryan standing up

    play music "music/mchill1.mp3"

    ry "[name], give me your number and I'll hit you up for the Apes' rush party tomorrow."

    ry "Then you'll see how sick they are."

    scene s48a
    with dissolve

    u "Alright, sure."

    scene s48
    with dissolve # ryan standing up

    ry "Awesome, I'll see you later."

    scene s49
    with fade

    la "You know... you don't have to join a frat to get girls."

    scene s50a
    with dissolve # Turning to lauren

    u "Huh?"

    scene s49
    with dissolve
    la "Sorry... I overheard you guys talking and I just wanted to say that... this fighting thing? It's really stupid."

    menu:

        "Agree":

            $ addPoint("bf", 1)
            jump af_a

        "Disagree":

            $ addPoint("tm", 1)
            jump af_b

    label af_a:
        scene s50a
        with dissolve

        u "It really is."

        u "Does that mean not all girls here are into the fighting?"
        scene s52
        with dissolve
        la "Not at all, pretty much any girl that's part of the Deer hates it."

        jump af_da

    label af_b:
        scene s50a
        with dissolve

        u "I mean it is kinda cool, I just wish I knew how to fight."

        scene s51
        with dissolve

        la "It's not cool, it's dangerous!"

        la "You know, there's a bunch of girls that would rather date a guy that doesn't fight."

        scene s51a
        with dissolve
        u "Really?"

        scene s49
        with dissolve
        la "Yeah, most of the Deer for example."

        jump af_db

    label af_da:
    label af_db:


        scene s51a
        with dissolve
        u "The Deer?"

        scene s52
        with dissolve
        la "They're one of the two sororities at San Vallejo. My sister Autumn is their president, so I know most of them quite well."

        scene s53a
        with dissolve
        u "Autumn? I've actually met her just before this class."

        scene s52
        with dissolve
        la "You did? I hope she didn't weird you out. She can be a bit much."

        scene s51a
        with dissolve
        u "Really? She was super nice to me."

        scene s49
        with dissolve
        la "Well... she's really passionate about political stuff and that can be a bit annoying haha."

        menu:


            "Don't defend Autumn":

                jump ah_a

            "Defend Autumn":

                $ addPoint("bf", 1)
                jump ah_b

        label ah_a:
            scene s50a
            with dissolve
            u "Yeah, I get that."

            scene s54
            with dissolve
            la "I bet you think she's cute, don't you?"



            menu:
                "You're cuter":

                    jump aj_a

                "Yeah, kinda":

                    $ addPoint("bf", 1)
                    jump aj_b



        label ah_b:
            scene s50a
            with dissolve
            u "I think that's pretty cool."

            scene s54
            with dissolve
            la "Ohhh... so you think she's cute?"


            menu:
                "You're cuter":

                    jump aj_a

                "Yeah, kinda":

                    $ addPoint("bf", 1)
                    jump aj_b

            label aj_a:
                scene s53a
                with dissolve

                u "I think you're cuter."

                scene s54
                with dissolve
                la "Haha, prince charming huh?"

                scene s53a
                with dissolve

                u "Only for the right girl."

                jump aj_da

            label aj_b:
                scene s53a
                with dissolve
                u "Yeah, she's kinda cute."

                scene s49
                with dissolve

                la "She's always been the pretty one."
                scene s53a
                with dissolve
                u "Oh cmon, you're just as pretty."

                scene s54
                with dissolve

                la "Smooth, haha."

                jump aj_db

            label aj_da:
            label aj_db:

            scene s53a
            with dissolve

            u "We should hang out sometime, what's your number?"

            scene s54
            with dissolve

            la "Wow, you don't even know my name and you're gonna ask for my number?"

            scene s50a
            with dissolve

            u "Uhhhh..."

            scene s49
            with dissolve

            la "I'm just kidding, I'm Lauren. I'll put my number into your phone."
            scene s53a
            with dissolve

            u "Haha phew... I'm [name] by the way."

            u "I'll text you later then, Lauren."

            scene s52
            with dissolve

            la "Sounds good. I'll see you later."

            # $ lauren_number = 1 - DELETE
            $ contact_Lauren.unlock()

    stop music fadeout 2.0

# Part 5 Free roam in the halls
    scene s50 #hallway 1 without freeroam
    with Fade(1, 0, 1)

    u "(I should probably go to my new dorm, but I might as well explore for a bit beforehand.)"

    play music "music/mchill2.mp3"

    scene s50 #freeroam
    with dissolve
    $ freeroamtut = 1
    $ phonetut = 0
    $ showphone = True
    $ phoneexit = "phonec"
    $ msgnot = 1
    $ jumsgnot = 1
    $ jumsg = 1
    $ contact_Julia.unlock()
    $ juisreply = 1
    $ contact_Julia.newMessage(juliaMessage1)
    $ jumsg1 = "Hey honey,\nenjoy your time in college.\nStay safe and don't forget to visit me.\nLove you"
    $ jurep1a = "Love you too."
    $ jurep1b = "Thanks, Julia :)"
    play sound "sounds/vibrate.mp3"
    call screen freeroam1a
    with dissolve


    label fr1a1:
    label fr1a2:
        call screen freeroam1a

    label fr1riley1:
        $ talktori = 1
        $ showphone = False
        $ freeroamtut = 0
        scene s50ri
        u "Hey, you were the girl sitting next to Elijah!"
        scene s50ri1
        with dissolve
        ri "Haha, you caught me. That's what I'm known for."
        scene s50ri1a
        with dissolve
        u "I'm [name]."
        scene s50ri1
        with dissolve
        ri "I'm Riley."
        scene s50ri2
        with dissolve
        ri "So what did you think of Ms. Rose?"

        menu:
            "She's hot.":

                $ addPoint("bro", 1)
                jump ak_a

            "She seems nice.":

                jump ak_b

        label ak_a:
            scene s50ri2a
            with dissolve

            u "Oh, she's super hot."

            scene s50ri1
            with dissolve

            ri "Haha, I meant her teaching style."

            scene s50ri1a
            with dissolve

            u "Ooops... I mean, yeah me too."

            scene s50ri4
            with dissolve

            ri "You didn't pay much attention did you?"

            scene s50ri2a
            with dissolve

            u "To be fair, the induction talk was reeeally boring."

            scene s50ri1
            with dissolve

            ri "Trueee, I wish I had sat further back. I had to look like I was engaged the entire time, or I would have left a bad first impression."

            scene s50ri1a
            with dissolve
            u "Next time, just sit with me. Sitting in the last row is where it's at."

            scene s50ri4
            with dissolve

            ri "Hmmm.. I'll think about it."
            $ fr1riley = 1
            $ showphone = True
            call screen freeroam1a
            with dissolve

            label ak_b:
            scene s50ri2a
            with dissolve
            u "I guess she seems pretty nice. I didn't really pay much attention haha."

            scene s50ri1
            with dissolve

            ri "Yeah, I wish I had sat further back. I had to look like I was engaged the entire time, or I would have left a bad first impression."

            scene s50ri1a
            with dissolve
            u "Next time, just sit with me. Sitting in the last row is where it's at."

            scene s50ri4
            with dissolve

            ri "Hmmm.. I'll think about it."
            $ fr1riley = 1
            $ showphone = True
            call screen freeroam1a
            with dissolve

    label fr1riley2:
        $ showphone = False
        scene s50ri1a
        u "You should really consider sitting in the last row."
        scene s50ri1
        with dissolve
        ri "Yeah.. you're probably right haha."
        $ showphone = True
        call screen freeroam1a

    label fr1elijah1:
        $ freeroamtut = 0
        $ showphone = False
        scene s50el
        u "Hey, you're Elijah right?"

        if funofelijah == 1:
            scene s50el1
            with dissolve

            el "What do you want?"

            scene s50el1a
            with dissolve

            u "Sorry for what I said earlier, it was just a stupid joke."

            scene s50el1a
            with dissolve

            u "Are you going to this rush party thing tomorrow?"

            scene s50el2
            with dissolve

            el "Rush party? Please."

            el "I got invited to the Frogs' Chess Night."
            jump elcontinue1

        else:

            scene s50el1
            with dissolve

            el "Yeah, how can I help you?"

            scene s50el1a
            with dissolve

            u "Do you know much about this rush party thing tomorrow?"

            scene s50el2
            with dissolve

            el "Rush parties are just a way for idiots to justify binge drinking."

            el "I'll be going to the Frogs' Chess Night."

            jump elcontinue2

            label elcontinue1:
            label elcontinue2:
                scene s50el2a
                with dissolve

                u "More animal names...? Go on, tell me about the Frogs..."

                scene s50el2
                with dissolve

                el "The Frogs are the elite fraternity at San Vallejo."
                el "Only the brightest of minds are allowed to join."

                menu:

                    "So... the nerds?":

                        $ addPoint("tm", 1)
                        jump al_a

                    "That's cool.":

                        $ addPoint("bf", 1)
                        jump al_b

                label al_a:
                    scene s50el2a
                    with dissolve

                    u "Sooo... the nerds?"

                    scene s50el1
                    with dissolve

                    el "How dare you defy the frogs like that?!"

                    el "Just get out of my face."
                    $ showphone = True
                    $ fr1elijah = 1

                    call screen freeroam1a

                label al_b:
                    scene s50el2a
                    with dissolve
                    u "I think that's pretty cool."

                    scene s50el1
                    with dissolve

                    el "It's not \"cool\"! It's prestigious and an incredible opportunity."

                    el "Now go and bother someone else."
                    $ showphone = True
                    $ fr1elijah = 1

                    call screen freeroam1a
    label fr1elijah2:
        $ showphone = False
        scene s50el1a
        u "Elijah?"

        scene s50el1
        with dissolve
        el "Leave me alone."
        $ showphone = True
        call screen freeroam1a

    label fr1b2:
    label fr1b:
        $ phoneexit = "phoned"
        $ freeroamtut = 0
        if chrisgone == 0:
            call screen freeroam1b
        else:
            label phonedtwo:
            call screen freeroam1b2

    label phonec:
        call screen freeroam1a

    label phoned:
        call screen freeroam1b

    label fr1chris1:
        $ showphone = False
        scene s55ch1
        ch "Babe... you know I gotta prepare our rush party."

        scene s55ch1a
        with dissolve
        no "It's just annoying, you haven't come to mine in like a week."

        scene s55ch1
        with dissolve
        ch "Most years there's only one or two good fighters. I can't risk letting the Apes get them... Not again."

        scene s55ch1a
        with dissolve
        no "Then why did you even delay your guys' party by a week? Won't everyone have already joined the Apes by then?"

        scene s55ch2
        with dissolve
        ch "Naah, everyone will come to our party and since they've already been to the Apes' party, they'll be able to tell how much better the Wolves are."

        scene s55ch2a
        with dissolve
        no "Okay... well, I hope your plan works."

        scene s55ch2
        with dissolve
        ch "Trust me babe, it will."
        ch "Okay I have to find Aaron, we were gonna buy some new speakers for the party."

        scene s55ch3
        with dissolve
        play sound "sounds/kiss.mp3"
        " "

        scene s55ch4
        with dissolve

        ch "Bye babe."

        no "Bye."
        $ chrisgone = 1
        $ showphone = True
        $ phoneexit = "phonedtwo"
        call screen freeroam1b2

    label fr1nora1:
        $ showphone = False
        $ fr1nora = 1
        scene s56no1a
        u "Hey, could you tell me where the dorms are?"

        scene s56no1
        with dissolve
        no "They're right through the doors behind you."


        menu:

            "Flirt":

                $ addPoint("tm", 1)
                $ hitonnora = 1
                jump am_a

            "Leave":

                $ hitonnora = 0
                jump am_b

        label am_a:
            scene s56no1a
            with dissolve

            $ keepitmoving = True
            if steam == False:
                image keepitmoving = "images/keepitmoving.png"
                show keepitmoving:
                    xpos 0
                    ypos -200
                    linear 0.5 xpos 0 ypos 0
                    pause 2.0
                    linear 0.5 xpos 0 ypos -200
            else:
                $ achievement.grant("keep_it_moving")
                $ achievement.sync()

            u "Actually, I knew that. I just wanted to talk to you 'cause you're really cute."

            scene s56no1
            with dissolve
            no "Look, I've got a boyfriend, so keep it moving."
            $ showphone = True
            call screen freeroam1b2

        label am_b:
            scene s56no1a
            with dissolve

            u "Thanks."
            $ showphone = True
            call screen freeroam1b2

    label fr1nora2:
        scene s56no1a
        $ showphone = False
        u "Uhm..."
        if hitonnora == 1:

            scene s56no1
            with dissolve
            no "Dude, keep it moving."
            $ showphone = True
            call screen freeroam1b2
        else:
            scene s56no1
            with dissolve
            no "I'm busy."
            $ showphone = True
            call screen freeroam1b2

    label fr1c:
        $ phoneexit = "phonee"
        call screen freeroam1c
    label bfra:
    label phonee:
        call screen freeroam1c

    label fr1adam1:
        scene adamaubrey36
        stop music fadeout 2.0

        $ showphone = False
        image adam1 = Movie(play="images/adamau.webm")
        play music "music/msexy.mp3"
        show adam1
        au "Ohhh shit, that feels good!"
        u "(Oh my god... she's so fucking hot.)"
        au "YESSSSS, FASTER!"
        u "(I should probably stop peeking, before I get caught.)"
        $ fr1adam = 1
        $ showphone = True
        stop music fadeout 2.0
        call screen freeroam1c

    label fr1adam2:
        scene s58
        u "I shouldn't risk peeking again."
        call screen freeroam1c



    label fr1end:
        scene s58
        call screen endfreeroam

    label efra:

        $ showphone = False
        scene s59
        stop music fadeout 2.0
        play sound "sounds/knock.mp3"
        "*Knock knock knock*"

        scene s60
        with dissolve

        play music "music/m16punk.mp3"

        imre "Yooo, what's up my man?"

        scene s60a
        with dissolve

        u "Hey man, I'm your new roommate."

        scene s60
        with dissolve

        imre "Aww, sick! Come in!"

        scene s62
        with dissolve

        imre "This is your bed. I took the other one 'cause I'm hoping for some sexy noises from the chick next door."

        scene s62a
        with dissolve
        u "Oh, does she make a lot of \"sexy noises\"?"

        scene s63d
        with dissolve

        imre "I don't know, it's my first day. But a man can dream."

        imre "I'm Imre by the way."

        scene s63e
        with dissolve

        u "I'm [name]... did you say Imre? First time I'm hearing that name."
        scene s63d
        with dissolve
        imre "It's Hungarian. My family and I moved to the States about eight years ago."
        scene s63e
        with dissolve

        u "Oh that's cool."

        scene s63d
        with dissolve
        imre "And, I got some weights as well, so we can get a pump before going to parties."
        scene s63e
        with dissolve
        u "Haha, seems like you got it all figured out."

        scene s63d
        with dissolve

        imre "Exactly, which is also why I'm joining the Wolves."

        scene s63e
        with dissolve

        u "The Wolves? I thought the Apes were the best frat to get girls?"

        scene s64
        with dissolve

        imre "Who told you that?! That's bullshit."

        imre "The Apes are disloyal pieces of shit. The Wolves are real brothers and they get mad pussy."

        scene s64a
        with dissolve

        u "Didn't you say it's your first day? How do you know the frats so well?"

        scene s63
        with dissolve

        imre "It is, but my brother used to be a Wolf and he told me about all the shady shit that the Apes would do."

        scene s63a
        with dissolve

        u "I heard the Apes won last year's Summer Showdown."

        scene s63
        with dissolve
        imre "Yeah they did, but that doesn't mean shit. The Wolves have won 5 out of the last 10 years."


        menu:

            "So, they're equally good?":

                $ addPoint("tm", 1)
                jump an_a

            "The Wolves sound sick.":

                $ addPoint("bro", 1)
                jump an_b

        label an_a:
            scene s63a
            with dissolve

            u "Soo.. they're equally good?"

            scene s64
            with dissolve

            imre "Noooo! The Wolves are better. How are you not getting this?!"

            scene s64a
            with dissolve

            u "I feel like your math doesn't add up there."

            jump an_ad

        label an_b:
            scene s64a
            with dissolve
            u " Honestly, after listening to you, the Wolves sound sick!"

            scene s63d
            with dissolve

            imre "Yeahhhh! They fucking are man. That's what I've been trying to tell you."

            jump an_bd

        label an_ad:
        scene s63d
        with dissolve
        label an_bd:


        imre "Honestly I think you'd make a great Wolf as well."

        scene s63e
        with dissolve

        u "I don't know how to fight haha, so it's probably not for me."

        scene s63d
        with dissolve

        imre "Man, fighting's easy. They teach you everything. I've been training with my brother and it's so much fun."

        scene s63e
        with dissolve
        u "Hmm... I'll give it a think."

        scene s63d
        with dissolve

        imre "You're definitely going to the Wolves' rush party with me."

        scene s63e
        with dissolve

        u "Fine..."

        u "(Great... another party where I won't fit in.)"

        scene s63d
        with dissolve

        imre "That's the spirit!"

        scene s61
        with fade

        imre "By the way, I met a hot fresher today and she's coming over later to hang out with me and my friends."

        scene s61a
        with dissolve

        u "Oh, so your friends are coming as well?"

        scene s61
        with dissolve

        imre "See, that's where you come in. None of my friends went to San Vallejo."
        imre "Instead, I thought my new roommate could invite a cute girl as well, so that it's not as awkward?"

        scene s61a
        with dissolve

        u "But... you didn't even know me at the time. What if I was a huge dick to you? Or-"

        scene s61
        with dissolve

        imre "You gotta risk it for a biscuit. Or in this case... the pussy."

        scene s61a
        with dissolve

        u "Fair enough. Only problem is, I don't actually know that many people here. It is also my first day after all."

        scene s61
        with dissolve

        imre "Oh come on. There's gotta be some girl that you've talked to today?"

        scene s61a
        with dissolve

        u "(I guess I could ask Lauren...)"

        u "Alright, I think I know who I could ask."

        scene s61
        with dissolve

        imre "It better be a girl."

        scene s61a
        with dissolve
        $ phoneexit = "phonef"
        $ laisreply = 1
        $ lamsg = 1
        $ lamsgnot = 1
        $ msgnot = 1
        $ contact_Lauren.newMessage(laurenMessage0)
        $ lareply1a = "Hey Lauren, would you want to hang out with me and my friends tonight?"
        $ lamsg1 = "Yeah sounds good :) Where do you wanna meet?"
        $ lareply2a = "Just come to dorm 109 at 8"
        $ lamsg2 = "Okay, will do"
        $ lareply3a = "See you later, cutie"
        $ lareply3b = "Cool"
        $ showphone = True

        call screen phone

        label phonef:
        if not laurenMessage2.reply: # Edited
            scene s61
            with dissolve
            imre "Did you ask?"

            scene s61
            with dissolve
            u "Oops I forgot."

            call screen phone

        else:
            $ showphone = False
            scene s61a
            with dissolve

            u "Okay man I did it."

            scene s61c
            with dissolve

            imre "Awesome! Get ready for a wild night, my man."

            scene s65
            with Fade(1, 0, 1)
            stop music fadeout 2.0
            " "

            jump continueonea

    label continueonea:
    play sound "sounds/knock.mp3"
    "*Knock knock knock*"

    scene s66
    with dissolve
    play music "music/mparty.mp3"
    imre "I think the ladies are here!"

    scene s67
    with fade
    ri "Heyyyy!"

    scene s67a
    with dissolve
    imre "Hey, come on in Riley. This is my roommate [name]."

    if talktori == 1:
        scene s67
        with dissolve
        ri "Yeah, we've met."

        scene s67a
        with dissolve
        imre "Oh really?"

        scene s67a
        with dissolve
        u "Yeah, we were in the same induction class."

        jump talktoria

    else:
        scene s67
        with dissolve
        ri "Hey, you were in my induction class, right?"

        scene s67a
        with dissolve
        u "Yeah, that's right. Good to see you again."
        jump talktorib

    label talktoria:
    label talktorib:

    scene s68
    with fade

    ri "Sooo, is it just us three for tonight?"

    scene s68a
    with dissolve

    imre "No, [name]'s friend is coming as well."

    scene s68a
    with dissolve

    u "Yeah, she should be here any minute."

    play sound "sounds/knock.mp3"

    "*Knock knock knock*"

    scene s68a
    with dissolve

    imre "Speak of the devil..."

    scene s69a
    with fade

    u "Hey Lauren!"

    scene s69
    with dissolve

    la "Heyyy..."

    scene s69a
    with dissolve

    u "I wasn't sure if you were gonna come."

    scene s69
    with dissolve

    la "I was only 2 minutes late."

    scene s70
    with dissolve

    u "This is my roommate Imre and his friend Riley."

    scene s70a
    with dissolve

    la "Oh, you were in our induction class right?"

    scene s71u
    with dissolve

    ri "Yeah, that's right."

    scene s72f
    with dissolve

    imre "Enough of the shit chat you guys... let's get drunk!"

    scene s71al
    with dissolve

    ri "Shit chat, really? ... You got drinks?"

    scene s72ar
    with dissolve

    imre "Hell yeah, I snuck in a beer bottle filled with vodka."
    scene s71dl
    with dissolve

    ri "You know that beer is also not allowed on campus right?"

    scene s72ar
    with dissolve

    imre "Whatever, we've got it now."

    scene s73f
    with dissolve

    la "Do you at least have mixer?"

    scene s72af
    with dissolve

    imre "Oh come on, we'll just drink out of the bottle."

    scene s74f
    with dissolve

    u "You're crazy."

    scene s72f
    with dissolve

    imre "You guys know drink or dare?"

    scene s71cl
    with dissolve

    ri "Of course, but you gotta start."

    scene s72r
    with dissolve

    imre "Fine, give me a dare then."

    scene s71cl
    with dissolve

    ri "I dare you to seduce your dumbbell."

    scene s72br
    with dissolve

    imre "Trust me, you're gonna wish you were this dumbbell."

    scene s71dl
    with dissolve

    ri "I doubt it."

    scene s72c
    with dissolve

    imre "Oh hello there mister, are your parents terrorists?"

    imre "Cause you look bomb."

    scene s71dl
    with dissolve

    ri "Hahahaha, why did you say mister?"

    scene s72dr
    with dissolve

    imre "It wasn't... I'm not... The dumbbell is just a manly thing."

    imre "It's a mister."

    scene s73f
    with dissolve

    la "Yeah, it's definitely not highlighting your subconscious preferences."

    scene s72ef
    with dissolve

    imre "Oh shut up, Lauren. Your turn."

    scene s73f
    with dissolve

    la "Alright, what do you want me to do?"

    scene s72bf
    with dissolve

    imre "I dare you to make out with [name]."

    scene s71cf
    with dissolve

    ri "Ahahahaha wow."

    scene s73ar
    with dissolve
    la "I think I'll drink."

    menu:


        "You're missing out":

            jump ao_a

        "Dodged a bullet there.":

            $ addPoint("tm", 1)
            jump ao_b

    label ao_a:
        scene s73gr
        with dissolve

        u "Wow... you're missing out, Lauren."

        scene s73ar
        with dissolve

        la "I guess we'll never know."

        jump ao_ad
    label ao_b:
        scene s73gr
        with dissolve

        u "Phew, dodged a bullet there."

        scene s72f
        with dissolve

        imre "Damn..."

        jump ao_bd

    label ao_ad:
    scene s72f
    with dissolve
    label ao_bd:

    imre "Okay, it's your turn to dare someone, Lauren."

    scene s73bl
    with dissolve

    la "Riley, I dare you to let Imre slap your ass."

    scene s71cl
    with dissolve

    ri "Oh that's easy. Let's do it, Imre"

    scene s75
    with fade

    imre "Great idea, Lauren!"

    scene s75a
    with hpunch

    play sound "sounds/slap.mp3"

    "*Slap*"

    scene s75b
    with dissolve

    ri "Imre! You went way too hard."

    scene s75c
    with dissolve

    imre "My bad, it looked so juicy."

    scene s73bl
    with dissolve

    la "Haha, oh god."

    scene s71cf
    with fade

    ri "Alright [name], your turn."

    scene s71ef
    with dissolve

    u "I'm ready."

    scene s71cf
    with dissolve
    ri "Take your shirt off."

    menu:


        "Take your shirt off":

            $ addPoint("tm", 1)
            $ shirtoff = 1
            jump ap_a

        "Drink instead":

            $ shirtoff = 0
            jump ap_b

    label ap_a:
        scene s76
        with dissolve

        u "There you go. Happy now?"

        scene s71cf
        with dissolve

        ri "Very happy."

        scene s71ef
        with dissolve

        u "Well then, Riley, I dare you to also take your shirt off."

        jump ap_ad
    label ap_b:
        scene s76a
        with dissolve

        " "

        scene s71bf
        with dissolve

        ri "Really? That was such an easy dare."

        scene s71ef
        with dissolve

        u "If that's what you think, then I dare you to take your shirt off."

        jump ap_bd

        label ap_ad:
        label ap_bd:

        scene s71bl
        with dissolve
        ri "What?! Can he just dare me back like that?"

        scene s72r
        with dissolve

        imre "Normally it's not allowed, but I think for this one we'll make an exception."

        scene s71cf
        with dissolve

        ri "I'm not wearing a bra."

        imre "Nnnnnnice."


        scene s71cf
        with dissolve
        ri "So I feel like that dare is kinda unfair."



        menu:



            "Do it, or drink.":

                $ addPoint("bro", 1)
                jump ar_a

            "You're right.":

                $ addPoint("bf", 1)
                jump ar_b

        label ar_a:
            scene s71ef
            with dissolve
            u "You gotta do the dare, or drink."

            scene s71cf
            with dissolve

            ri "Fine..."

            scene s77
            with dissolve

            " "
            jump ar_ad

        label ar_b:
            scene s71ef
            with dissolve
            u "You're right, let's continue."
            jump ar_bd

        label ar_ad:
        label ar_bd:

        scene s73cf
        with dissolve

        la "Guys, I don't wanna kill the vibe, but we have class pretty early tomorrow and I don't wanna be late for my first Economics class."

        scene s72ef
        with dissolve

        imre "What? But we were just getting started."

        scene s71cf
        with dissolve

        ri "She's right, we should get going. We'll see you tomorrow."

        scene s71ef
        with dissolve

        u "Alright, see ya."

        stop music fadeout 2.0

####### Late night talk with Imre.

        scene s80
        with Fade(1, 0, 1)
        play music "music/msad.mp3"
        $ rileyfight = 0
        imre "Man, I can't wait to bang this Riley chick."

        menu:



            "Riley's mine.":

                $ addPoint("tm", 1)
                jump as_a

            "They're both hot.":

                $ addPoint("bro", 1)
                jump as_b

        label as_a:
            scene s79b
            with dissolve
            u "What? I want Riley. You can have Lauren."

            scene s80e
            with dissolve
            imre "What the hell man?! I invited Riley. Back off."


            menu:



                "You're right, sorry.":

                    $ addPoint("bro", 1)
                    jump at_a

                "She wants me.":

                    $ addPoint("tm", 1)
                    $ rileyfight = 1
                    jump at_b

            label at_a:
                scene s79a
                with dissolve
                u "You're right, Riley is yours. I'm sorry."

                scene s80a
                with dissolve

                imre "It's fine bro, I get it. She is really cute."

                jump at_ad
            label at_b:
                scene s79b
                with dissolve
                u "She wanted to see ME shirtless, not you. Face it, she wants me."

                scene s80e
                with dissolve

                imre "Man, that was drink or dare, get over yourself."

                imre "What happened to bros before hoes..."

                scene s79a
                with dissolve

                u "Shit... You're right, sorry. I shouldn't have..."

                scene s80a
                with dissolve
                imre "It's alright man, I get it."
                scene s80
                with dissolve
                imre "Trust me, we're gonna bang so many chicks this year. All we need is confidence..."
                jump at_bd

    label as_b:
        scene s79
        with dissolve
        u "Hahaha, to be honest they're both pretty hot."

        jump as_bd

    label as_ad:
    label as_bd:
    label at_ad:
        scene s80
        with dissolve

        imre "Oh man, we're gonna bang so many chicks this year. Trust me, all you need is confidence..."
        label at_bd:
        imre "And to be part of a frat."

        if fr1adam == 1:

            scene s79a
            with dissolve

            u "Why do people keep saying that? I saw a guy fucking a really hot chick in the room opposite to ours."

            u "And all the frat guys live in the frat houses right? So he got chicks without being in a frat."


        else:

            scene s79a
            with dissolve

            u "Why do people keep saying that? I've heard from some girls that they date guys that aren't in a frat."

        scene s80a
        with dissolve
        imre "Man, I'm not saying it's impossible, but why make it so hard for yourself?"

        imre "Being in a frat is the easiest way to get girls, plus you get to fight."

        scene s79d
        with dissolve

        u "But I don't wanna fight man! I'm scared, okay?!"

        u "I don't know how to fight, I don't know how to pick up girls, I don't know anything about college life."

        scene s80a
        with dissolve

        imre "It's alright man, don't beat yourself up."

        imre "Look, I'm a first year too, but the Wolves are a brotherhood. They support each other."

        imre "You'll learn everything over time. And trust me, fighting is a lot more fun than you'd think."

        scene s79a
        with dissolve

        u "It might be right for you, but frat life is just not for me."

        u "I'm not a fighter and I don't want to be one."

        scene s80a
        with dissolve

        imre "Alright man, good night."

        scene s79a
        with dissolve

        u "Night."

        stop music fadeout 2.0

        jump sexdream1


    ######### sexdream

    label sexdream1:

    label ga:
    $ _game_menu_screen = "ingmenu"

    scene s1  ### close to the kitchen counter
    with Fade (1,0,1)

    ri "Wow, you guys have a really nice house."
    $ fantasy = True
    scene sda1a
    with dissolve

    u "I'm glad you like it."

    scene sda1
    with dissolve

    ri "Pretty big for just the two of you."

    scene sda1a
    with dissolve

    u "Yeah, it can seem a bit empty now that... never mind."

    scene sda1
    with dissolve

    ri "When will she be back? I can't wait to meet her."

    scene sda1a
    with dissolve

    u "Probably not for a few hours yet."

    play music "music/msexy.mp3"
    scene sda2
    with dissolve

    ri "I have an idea about how we can fill the time."

    scene sda2a ## riley grabbing his dick and seeing both
    with dissolve
    " "

    scene sdakisso
    with dissolve


    " "
    u "(Okay, this is definitely a dream, but I do like where this is going.)"
    menu:


        "Keep dreaming":

            $ sda = True
            jump dream

        "Wake up":

            $ sda = False
            jump skipdream

    label dream:
    scene sda3a
    with fade

    ri "*Chuckles* You're hard already."

    ### your pants down

    scene sda3
    with dissolve

    ri "Oh wow."

    scene sda4
    with dissolve

    ri "How does that feel?"

    scene sda3a
    with dissolve
    ri "Tell me what you want."

    menu:


        "Blowjob":

            jump bg_b

        "Footjob":

            jump bg_c


    label bg_b:

        scene sda3b
        with dissolve

        u "I want you to suck my dick."

        scene sda3a
        with dissolve

        ri "I was hoping you'd say that."

        image sdabj = Movie (play="images/sdabj.webm", loop = True, image = "images/s1")
        image sdabjf = Movie (play="images/sdabjf.webm", loop = True, image = "images/sda4e")

        show sdabj
        with fade
        u "You look so pretty with my cock in your mouth."

        ri "*Gasp* You taste so good."

        ri "Just make sure you don't come yet."

        u "I won't, I won't. You can go faster."

        show sdabjf
        with dissolve

        ri "*Gasp* Like this?"

        u "Fuuuuck. Yes, exactly like that."

        u "I can't hold it much longer."

        ri "*Gasp* Okay enough, I need your dick inside of me."

        jump bg_bd

    label bg_c:

        scene sda3b
        with dissolve

        u "I want you to use your feet."

        scene sda3a
        with dissolve

        ri "I was hoping you'd say that."



        image sdafj = Movie (play="images/sdafj.webm", loop = True, image = "images/s1")
        image sdafjf = Movie (play="images/sdafjf.webm", loop = True, image = "images/sda4e")

        show sdafj
        with fade
        ri "Wow, I've never done this before. Does it feel good?"

        u "Yes, it feels fantastic, Riley."

        ri "Just make sure you don't cum yet."

        u "I won't, I won't. You can go faster."

        show sdafjf
        with dissolve

        ri "Like this?"

        u "Fuuuuck. Yes, exactly like that."

        u "I can't hold it much longer."

        ri "Okay enough, I need your dick inside of me."

        jump bg_cd



    label bg_ad:
    label bg_bd:
    label bg_cd:

    scene sda4e
    with fade

    ri "What's next?"

    scene sda4b ## grabbing her shoulders
    with dissolve

    u "I'll show you what's next."

    scene sda4c ## turning her around
    with dissolve
    u "Bend over."

    scene sda4d ## grabing her neck
    with dissolve
    pause (0.5)
    scene sda5 ## slamming her onto the counter
    with vpunch

    ri "Fuck yes, [name]!"

    scene sda5a # her face on the counter to the side with your arm pushing her down
    with dissolve

    ri "Yes! I love it when you dominate me."

    scene sda60
    with dissolve

    pause 0.3
    play sound "sounds/slap.mp3"
    scene sda60a
    with vpunch

    ri "*Squeals*"

    scene sda60
    with dissolve

    pause 0.3
    play sound "sounds/slap.mp3"
    scene sda60a
    with vpunch

    ri "Harder!"

    scene sda60
    with dissolve

    pause 0.3
    play sound "sounds/slap.mp3"
    scene sda60a
    with vpunch

    ri "*Squeals*"

    scene sda7
    with dissolve #her face looking back at you

    ri "Please... fuck me. I want you so bad."


    scene sda7a ## her face on the counter
    with vpunch

    ri "Oh my god!"

    image sdasex = Movie (play="images/sdasex.webm", loop = True, image = "images/sda7a")

    show sdasex
    with dissolve

    ri "Yesss! Faster!"

    ri "You feel so good inside of me, [name]."

    u "(She's so fucking hot.)"

    ri "Don't stop!"

    ri "[name], I'm gonna cum!"

    u "I can't hold it any longer!"

    scene sda7a
    with dissolve

    ri "Cum inside me, [name]! Please fill me up!"

    image sdacum2 = Movie (play="images/sdacum2.webm", image = "images/aftercum.jpg", loop = False)
    scene aftercum
    show sdacum2
    with dissolve
    u "Hngh..."

    scene sda7
    with dissolve

    ri "My legs are shaking."
    label skipdream:

    $ fantasy = False

    stop music fadeout 2.0
    $ renpy.end_replay()

    ####next morning in your dorm, Imre seems to be gone.


    if sda == True:
        scene s81
        with Fade (1,0,1)

        u "*Yawn*"

        play music "music/mfunk.mp3"

        u "(That was the most amazing dream of my life.)"
        u "(I wish I could sleep some more, but I gotta get to class.)"
        u "(I just hope I don't get a boner whenever I see Riley from now on.)"

        scene s82
        with Fade (1,0,1)

        ri "Heyyy, I've switched to the last row now."

        scene s82a
        with dissolve

        u "(Okay I need to be cool, even though all I can think about is my dream.)"

        u "Oh, so you decided to join the cool club."

        u "Where's Imre and Lauren?"

        scene s82
        with dissolve

        ri "Imre doesn't need to take economics for his course and Lauren, I don't know."

        scene s82a
        with dissolve

        u "(Shit, I need to talk to someone else, I'm already starting to get hard just talking to her.)"

    else:
        scene s81
        with Fade (1,0,1)

        u "*Yawn*"

        play music "music/mfunk.mp3"

        u "(What a weird dream...)"

        u "(Alright [name], just forget about it and go to class.)"

        scene s82
        with Fade (1,0,1)

        ri "Heyyy, I've switched to the last row now."

        scene s82a
        with dissolve

        u "(Stay cool, she doesn't know about your dream.)"

        u "Oh, so you decided to join the cool club."

        u "Where's Imre and Lauren?"

        scene s82
        with dissolve

        ri "Imre doesn't need to take economics for his course and Lauren, I don't know."


    scene s83a #sits down
    with fade

    u "Hey, man."

    scene s83
    with dissolve

    ry "What's up, dude? You ready for some teacher staring?"

    scene s83a
    with dissolve

    u "Teacher staring?"

    scene s83
    with dissolve
    ry "You know, 'cause the class is boring as shit, but at least the teacher's hot."

    scene s84 #showing ms rose bendt over forwards
    with dissolve

    u "(He does have a point...)"

    scene s84a
    with dissolve
    ro "Good morning everyone. Welcome to your first economics class."

    ro "Today, we're gonna learn about-"

    play sound "sounds/dooropen.mp3"

    scene s85 ###Lauren comes in, her roomates a dick so she wants to stay with you whenever Imre's gone."
    with dissolve

    la "Sorry! My roommate thought it'd be a good \"prank\" to steal my phone, so that I couldn't hear my alarm."

    scene s84b
    with dissolve

    ro "Very well, I'm sorry to hear that."
    ro "Just sit down, so that we can get started on the material."
    #####clock video
    stop music fadeout 2.0
    play sound "sounds/clock2.mp3"
    scene clocka
    with fade

    pause (0.5)

    scene clockb
    with dissolve

    pause (0.5)

    scene clockc
    with dissolve

    pause (0.5)

    scene clockd
    with dissolve

    pause (0.5)

    scene clocke
    with dissolve
    # disscussiion after class with Lauren

    scene s86
    with fade

    ry "This class is so damn boring..."

    play music "music/m11punk.mp3"
    scene s86a
    with dissolve
    ri "Agreed. Also Ms. Rose offers no chances to show that we've actually done the prereading."
    scene s86b
    with dissolve
    ry "Yeah, 'cause she knows that no one actually does that shit anyways."
    scene s86a
    with dissolve
    ri "Uhm... right."

    scene s87a
    with dissolve
    u "So... trouble with your roommate?"

    scene s87
    with dissolve

    la "Yep... she's just so annoying. I wish I could still move dorms."

    menu:

        "Move in with me?":

            $ addPoint("bf", 1)
            jump au_a

        "Bad roommates suck.":

            $ addPoint("bro", 1)
            jump au_b

    label au_a:
        scene s87a
        with dissolve
        u "You should move in with me."

        scene s87b
        with dissolve

        la "Haha definitely, I'm sure Imre would looove to swap rooms with me."

        la "It's fine, it was just such a bad start to the day. I really didn't wanna be late to my first real class."

        scene s87c
        with dissolve
        u "How about we go to the park this afternoon? I'll bring some sandwiches and we'll make your day better."

        jump au_ad
    label au_b:
        scene s87a
        with dissolve
        u "I get that, bad roommates suck."

        scene s87
        with dissolve

        la "It was just such a bad start into the day. I really didn't wanna be late to my first real class."

        scene s87a
        with dissolve
        u "How about we go to the park this afternoon? I'll bring some sandwiches and we'll make your day better."

        jump au_bd


        label au_ad:
        label au_bd:

        scene s87b
        with dissolve
        stop music fadeout 2.0

        la "Yeah, I'd like that."

###### park with Lauren (secret sharing)

scene s88
with Fade (1,0,1)

play music "music/mlove1.mp3"
play sound "sounds/park.mp3"

la "This park is really nice. I've never been here before."

scene s88a
with dissolve

u "Oh, are you from here?"

scene s89
with dissolve

la "Yeah, my family lives about 20 minutes from here."

scene s89a
with dissolve

u "Oh cool."

u "Lauren, I gotta be honest..."

u "I've got good news, but I've also got some bad news."

scene s89b
with dissolve

la "Alright, tell me."

scene s89d
with dissolve

u "So, the good news is that I made us some delicious sandwiches."

scene s89
with dissolve

la "That's so cute!"

scene s89a
with dissolve

u "The bad news is that I forgot them in my dorm and Imre has probably eaten them by now."

scene s89b
with dissolve

la "Haha, oh wow. So you're just gonna tease me with the possibility of eating a delicious sandwich only to then take that away from me?"

la "That's some pretty messed up stuff."

scene s89d
with dissolve

u "If it makes you feel any better, I'm just as disappointed as you are."

scene s89e #(Lauren drinking)
with dissolve
" "
u "So... what do you think of the guys at San Vallejo?"

scene s89b
with dissolve

la "I've met a couple cute guys so far..."

scene s89d
with dissolve

u "A couple huh?"

menu:

    "You could get any guy.":

        jump av_a

    "Yet, you're here with me.":

        $ laurenlike += 1
        jump av_b

label av_a:
    scene s89d
    with dissolve
    u "I bet you could get any guy you want."

    scene s89f
    with dissolve
    la "Uhm... thanks. Not really though, haha."

    jump av_ad
label av_b:
    scene s89d
    with dissolve
    u "And yet, you're here with me. How surprising."

    scene s89b
    with dissolve
    la "Okay Casanova, I'm pretty sure you invited me and not the other way around."

    scene s89d
    with dissolve
    u "Let's not get caught up on the details."

    u "I'm gonna assume that there's no jealous boyfriend or ex that'll beat me up after this?"
    scene s89
    with dissolve
    la "Don't worry, I haven't had a boyfriend since 10th grade."
    jump av_bd

    label av_bd:
        scene s89f
        with dissolve
    label av_ad:
        la "I haven't even..."

        la "Never mind..."

        scene s89g
        with dissolve

        u "Oh come on! You can tell me."

        scene s89f
        with dissolve

        la "I'd rather not, it's kinda embarrassing."

        scene s89g
        with dissolve

        u "I'll tell you one of my secrets as well."

        scene s89b
        with dissolve

        la "Fine, but you have to start."


        menu:


            "I'm still in love with my ex.":

                jump aw_a

            "I've broken into an Ikea.":

                $ laurenlike += 1
                jump aw_b

        label aw_a:
            scene s89d
            with dissolve
            u "Hmmm... okay. I'm - I'm still in love with my... ex."

            scene s89h
            with dissolve
            la "Oh shit... what happened between you guys?"

            scene s89j
            with dissolve
            u "I broke up with her a couple of months ago, 'cause she cheated on me."

            scene s89h
            with dissolve
            la "Damn... I'm really sorry."

            scene s89j
            with dissolve
            u "Yeah, it's whatever."

            u "Now it's time for your secret."

            jump aw_ad

        label aw_b:
            scene s89d
            with dissolve
            u "Hmm... okay. A couple years ago me and my best friend Josh saw this video of a guy staying 24 hours in an Ikea store."

            scene s89j
            with dissolve
            u "It looked so cool that we decided to try the same thing."

            u "We were gonna hide inside the closets until they closed the doors."

            u "But I got cold feet and left the building instead of hiding."

            u "Then Josh texted me, asking where I was."

            scene s89
            with dissolve

            la "So what did you do?"

            scene s89a
            with dissolve

            u "Well I didn't want to admit that I pussied out, so I found a back door that seemed to be unlocked and got back in."

            scene s89h
            with dissolve

            la "Oh shit."

            scene s89j
            with dissolve
            u "Yeah, the stupid thing was that it triggered the silent alarm."

            u "Just a few minutes later we got escorted out by the police."

            u "Honestly, I got really lucky. Ikea didn't press any charges."

            scene s89
            with dissolve

            la "Oh wow, I guess you should have hid in the closet, haha."

            scene s89a
            with dissolve

            u "I'm glad you're amused, because now it's time for your secret."

            jump aw_bd

        label aw_ad:
        label aw_bd:

            scene s89f
            with dissolve

            la "Right... almost forgot about that."

            la "I...I haven't actually had sex before."

            scene s89g
            with dissolve

            u "You?"

            scene s89f
            with dissolve

            la "I mean I've done stuff... just not sex."

            scene s89g
            with dissolve

            u "You haven't had sex?"

            scene s89f
            with dissolve

            la "Yeah..."

            scene s89g
            with dissolve

            u "Your vagina - has never seen a penis?"

            scene s89f
            with dissolve

            la "Right, but..."

            scene s89g
            with dissolve

            u "Your donut - has not been glazed?"

            scene s89f
            with dissolve

            la "Yes, but..."

            scene s89g
            with dissolve

            u "Your jigsaw puzzle - has not been completed?"

            scene s89
            with dissolve

            la "Okay, how many of these did you have ready to go?"

            scene s89a
            with dissolve

            u "Haha, just enough to show my surprise."

            scene s89
            with dissolve

            la "Oh come on, it's not that weird."

            scene s89a
            with dissolve

            u "It's not weird, it's just..."


            menu:


                "You're really beautiful.":

                    $ addPoint("bf", 1)
                    jump ax_a

                "You're not ugly.":

                    $ addPoint("bro", 1)
                    jump ax_b

            label ax_a:

                u "You know... you're really beautiful."

                scene s89
                with dissolve
                la "Awww."

                jump ax_ad

            label ax_b:

                u "You know... you're not ugly."

                scene s89b
                with dissolve

                la "Wow, how flattering."

                jump ax_bd


            label ax_ad:
            label ax_bd:

            scene s89k
            with dissolve

            u "(Is this the moment to kiss her?)"


            menu:


                "Kiss her":

                    $ lakiss = 1
                    jump ay_a

                "Don't kiss her":

                    $ lakiss = 0
                    jump ay_b

            label ay_a:
                if laurenlike >= 2:
                    scene s90
                    with dissolve # kiss
                    $ firstkisslauren = True

                    $ romeo = True
                    if steam == False:
                        image romeo = "images/romeo.png"
                        show romeo:
                            xpos 0
                            ypos -200
                            linear 0.5 xpos 0 ypos 0
                            pause 2.0
                            linear 0.5 xpos 0 ypos -200
                    else:
                        $ achievement.grant("romeo")
                        $ achievement.sync()

                    play sound "sounds/kiss.mp3"
                    " "
                    scene s90a
                    with dissolve
                    " "
                else:
                    scene s90a
                    with dissolve
                    " "
                jump ay_ad

            label ay_b:
                scene s90b # you scratching your head
                with dissolve
                " "
                jump ay_bd

            label ay_ad:

            label ay_bd:


            scene s89h
            with dissolve

            la "Uhh... [name]... I..."
            la "I should go."

            scene s91 ##Lauren stood up
            with dissolve

            u "Lauren, wait!"

            scene s91a #Lauren turns around
            with dissolve

            la "Sorry, but..."
            la "I'll see you tomorrow, [name]."

            scene s92 # you head in hands
            with dissolve

            if lakiss == 1:
                u "(Fuck... why did I try to kiss her?! That just made everything weird.)"

            else:
                u "(Fuck... should I have kissed her? Now it's just weird between us.)"


            jump next_scenea
########## Back in your dorm with Imre
    label next_scenea:
    stop music fadeout 2.0

    stop sound

    scene s93
    with Fade (1,0,1) # Imre in your dorm

    imre "Oh hey man, are you back from your date?"

    scene s93a
    with dissolve

    play music "music/msad.mp3"

    u "For the last time, it wasn't a date."

    scene s93
    with dissolve

    imre "By the way, I very much appreciated the sandwiches you left for me."

    scene s94 #you walking to your bed
    with dissolve

    u "Right, glad you enjoyed them."
    play sound "sounds/impactbed.mp3"
    scene s95 # you falling onto bed
    with vpunch

    "*Hmpf*"

    scene s96 #showing Imre in front of your bed looking down on you
    with dissolve

    imre "I take it your date didn't go as planned?"

    if lakiss == 1:

        if laurenlike >= 2:
            scene s96a
            with dissolve
            u "I just don't get it..."

            u "I kissed her... and for a second she kissed me back."

            u "But then she pulled away and left."

            u "And now it's all just super weird."

            jump nextscenec

        else:
            scene s96a
            with dissolve

            u "I just don't get it..."

            u "She gave me all the signs, so I went for a kiss."

            u "But she pulled away and left."

            u "And now it's all just super weird."

            jump nextscened

    else:
        scene s96a
        with dissolve

        u "I just don't get it..."

        u "Everything was going great, until there was this moment."

        u "Maybe she wanted me to kiss her, but... I didn't go for it."

        u "And then she just left..."

        u "And now it's all just super weird."

        jump nextscenee

    label nextscenec:
    label nextscened:
    label nextscenee:

    scene s96
    with dissolve

    imre "Shit man... maybe she's just unsure about her emotions or some shit."

    imre "You know how girls are."

    scene s96a
    with dissolve

    u "Yeah maybe..."

    scene s96b
    with dissolve

    imre "We'll party tonight with some new chicks and you'll forget all about it."

    scene s96c
    with dissolve

    u "I guess..."

    label backtophone:
    scene s96c
    stop music fadeout 2.0
    play sound "sounds/vibrate.mp3"
    $ showphone = True
    # $ ryanreply = 0
    # $ ryisreply = 1
    # $ ryfirst = 1
    $ contact_Ryan.unlock()
    # $ rymsgnot = 1
    # $ msgnot = 1
    # $ rymsg = 1
    $ contact_Ryan.newMessage(ryanMessage1)
    # $ rymsg1 = "Hey man, it's Ryan.\nThe Apes' rush party is tonight at 9. You're coming, right???"
    # $ ryrep1a = "Alright, but I'll only stay for a few hours."
    # $ rymsg2 = "Haha, trust me, you're not gonna want to leave once you see all the hot chicks there."
    # $ rymsg3 = "Just meet me in front of the Apes' frat house at 9."
    # $ ryrep2a = "Okay, will do."
    $ phoneexit = "phoneg"

    " "
    label phoneg:
    label repeata:
    if not ryanMessage1.reply:

        u "(I should really check who texted me.)"

        jump repeata

    else:
        scene s96c
        with dissolve
        $ showphone = False

        play music "music/m3punk.mp3"

        u "Actually dude, I can't make tonight. I'm going to the Apes' rush party with my friend."

        scene s96d
        with dissolve

        imre "Man, fuck the Apes! What do you want there anyways?!"

        scene s96e
        with dissolve

        u "Look, I know you don't like them, but I told my friend I'd go with him."

        scene s96d
        with dissolve

        imre "Whatever dude, do what the fuck you want. I'm outta here."

        scene s96g
        with fade

        u "(Great... now I've fucked up two friendships today.)"

        stop music fadeout 2.0

        jump nextscenef


    #### In front of the ape's house ryan is texting
    label nextscenef:
    scene s97
    with Fade (1,0,1)

    u "(Holy shit, their house is huge. I guess someone here has rich parents.)"

    play music "music/muffledparty.mp3"

    u "(Looks like Ryan's right there as well, waiting for me.)"

    scene s98
    with dissolve

    u "Ryan! What's up?"

    scene s98a
    with dissolve

    ry "[name]! Hey man, how's it going? You ready for the party?"

    scene s99a
    with dissolve

    u "Yeah, but you know how you said there's gonna be so many hot chicks here?"

    scene s99
    with dissolve

    ry "Haha, don't worry player, there are."

    scene s99a
    with dissolve

    u "It's not that, I was just wondering why a frat rush party would have girls in the first place. Aren't rush parties about potential pledges getting to know the fraternity?"

    scene s99
    with dissolve

    ry "Well yeah, but both the Apes and the Wolves want the best fighters to join their frat, so they use hot girls to show them the benefits of joining."

    scene s99a
    with dissolve

    u "Hmm... I guess that makes sense."

    scene s99
    with dissolve

    ry "How about we stop talking about girls and start talking to them?"

    scene s99a
    with dissolve

    u "Alright, let's go."

    #freeroam2

    $ latext = 0
    $ showphone = True
    $ phoneexit = "phoneh"
    $ samtalk = 0
    $ joshtalk = 0
    $ graysontalk = 0
    $ courtneytalk = 0
    $ masontalk = 0
    $ katytalk = 0

    label phoneh:
    call screen freeroam2a

    label fr2sam:
        $ showphone = False
        $ samtalk = 1
        scene s101
        sam "... and that's why I purposefully lost that fight."

        scene s101a
        with dissolve

        karen "I'm pretty sure I heard you scream \"help\" multiple times."

        ry "Hey man, are you an Ape?"

        scene s101c
        with dissolve

        sam "Yeah, what's up man?"

        scene s101b
        with dissolve

        ry "Aren't you guys supposed to wear your jackets for the rush party?"

        scene s101c
        with dissolve

        sam "What are you, the jacket police? It's warm outside, I'm not gonna wear a jacket, jeez."

        scene s101b
        with dissolve

        ry "Uhh... I didn't mean to..."

        scene s101c
        with dissolve

        sam "Yeah and now piss off man, I'm trying to score here."

        scene s101d
        with dissolve

        karen "What?! I have a boyfriend."

        scene s101e
        with dissolve

        sam "Wait what?! You've led me on all night!"

        scene s101f
        with dissolve

        karen "We were just talking, that's what friends do!"

        u "(We should probably leave them alone before we get dragged into this.)"

        $ showphone = True

        call screen freeroam2a

    label fr2sam2:

        scene s100a

        u "(I don't wanna risk getting dragged into their argument.)"

        call screen freeroam2a

    label fr2door:
        play music "music/mparty2.mp3"

        queue music [ "music/mparty3.mp3", "music/mparty4.mp3" ]
        $ showphone = False
        $ fr2door = 1
        $ phoneexit = "phonej"
        scene s103

        ry "Alright man, I'm gonna look around, I'll see you in a bit."

        scene s103a

        u "Cool."

        u "(Great, now I'm all on my own.)"

        $ showphone = True

        call screen freeroam2b

    label phonej:
    label fr2door2:
    label fr2poolback:
    label fr2campback:
    label fr2down:
        $ phoneexit = "phonej"
        call screen freeroam2b

    label fr2outside:
        $ phoneexit = "phonek"
    label phonek:
        call screen freeroam2a

    label fr2pool:
        if joshtalk == 0:

            scene s102

            u "(I should talk to Josh first, I haven't seen him in a while.)"

            call screen freeroam2b
        else:
            $ phoneexit = "phonel"
    label phonel:

        call screen freeroam2c

    label fr2courtney:

        $ showphone = False

        $ courtneytalk = 1

        scene fr2co1

        u "Hey there."

        scene fr2co2
        with dissolve

        courtney "Ughh, get in line. You're not getting in there before me."

        scene fr2co2a
        with dissolve

        u "Sorry, in where exactly?"

        scene fr2co2
        with dissolve

        courtney "The bathroom??? I've been waiting for over an hour."

        scene fr2co2a
        with dissolve

        u "You've been waiting for over an hour?! Are you sure that's the bathroom? That seems way too long."

        scene fr2co2b
        with dissolve

        courtney "Oh my god, how stupid do you think I am?! I think I know what the bathroom looks like."

        scene fr2co2c
        with dissolve

        u "You are aware that this is literally just a regular white door, right? There's like 10 of these in this house."

        scene fr2co2b
        with dissolve

        courtney "Just leave me alone, perv."

        scene fr2co2c
        with dissolve

        u "What?? I didn't even... whatever."

        $ showphone = True

        call screen freeroam2b

    label fr2courtney2:

        $ showphone = False

        scene fr2co2
        with dissolve

        courtney "I said leave me alone, perv."

        scene fr2co2a
        with dissolve

        u "Right..."

        $ showphone = True

        call screen freeroam2b


    label fr2josh:

        $ showphone = False

        $ joshtalk = 1
        scene fr2jo1a

        jo "[name]! I didn't know you're also going to San Vallejo. *sniff*"

        jo "This is uhhh... Aubrey!"

        scene fr2jo2a
        with dissolve

        au "Hey, nice to meet you."

        scene fr2jo2b
        with dissolve
        if fr1adam == 1:
            u "(Holy shit, is this the girl that got fucked in the dorm opposite of ours?!)"

            u "(She's so fucking hot.)"

        else:

            u "(Damn, she's hot)"

        u "Hey, I'm-"

        scene fr2jo2c
        with dissolve

        au "Let me guess, [name]."

        scene fr2jo2d
        with dissolve

        u "Haha. Wow, you're good."

        scene fr2jo2a
        with dissolve

        au "I try my best."

        scene fr2jo1a
        with dissolve

        jo "You know, me and [name] go way back. *sniff*"

        jo "Best friends through all of middle school."

        jo "I mean, we drifted apart in high school, but... *sniff*"

        jo "Now we're reunited, baby! "

        scene fr2jo1b
        with dissolve

        u "Josh, are you okay?"

        scene fr2jo1c
        with dissolve

        jo "Yeah. *sniff* Yeah, I'm - I'm fine."

        jo "It's just uhhh... hay fever, you know."

        scene fr2jo1d
        with dissolve

        u "(Right, sure it is.)"

        scene fr2jo2c
        with dissolve

        au "So... [name], does that mean you're a freshman as well?"

        scene fr2jo2d
        with dissolve

        u "Yeah, what about you?"

        scene fr2jo2a
        with dissolve

        au "Oh no, I'm a junior, vice president of the Chicks actually."


        menu:


            "Flirt":

                jump az_a

            "Ask if she likes fighters":

                $ addPoint("bf", 1)
                jump az_b

        label az_a:

            scene fr2jo2b
            with dissolve

            u "Oh, trying to impress me with your rank?"

            scene fr2jo2c
            with dissolve

            au "Haha, maybe."

            au "Nothing wrong with warming up the new batch of fighters, is there?"

            menu:


                "Say you're a fighter":

                    $ addPoint("tm", 1)
                    $ aubreywannafight = 1
                    jump ba_a

                "Say you're not a fighter":

                    $ aubreywannafight = 0
                    jump ba_b

            label ba_a:

                scene fr2jo2d
                with dissolve

                u "Well, you're certainly warming up the right guy."

                scene fr2jo2c
                with dissolve

                au "And why is that?"

                scene fr2jo2d
                with dissolve

                u "Cause I'll be the next Fight King."

                u "(Shit, why did I say that?? I don't even know how to fight and I don't really want to either.)"

                scene fr2jo2a
                with dissolve

                au "Oh wow, big words. Have you met Grayson yet? I'm sure he'd like your confidence."

                scene fr2jo2b
                with dissolve

                u "Who's Grayson?"

                jump ba_ad

            label ba_b:

                scene fr2jo2b
                with dissolve

                u "Oh, I don't really plan on becoming a fighter."

                scene fr2jo2e
                with dissolve

                au "Really? Well, then what are you doing at the Apes' rush party?"

                au "Grayson doesn't accept non-fighters."

                scene fr2jo2f
                with dissolve

                u "Who's Grayson?"

                jump ba_bd

        label az_b:

            scene fr2jo2b
            with dissolve

            u "I've heard that all the Chicks are into fighters."

            scene fr2jo2c
            with dissolve

            au "I mean, I can't deny that most of the fighters are pretty sexy."

            au "They're ripped, confident and being able to beat other guys up certainly doesn't make them less attractive."

            au "Why are you asking? Are you planning on becoming a fighter?"

            menu:


                "I'll be the next Fight King.":

                    $ addPoint("tm", 1)
                    $ aubreywannafight = 1
                    jump bb_a

                "No, that's not for me.":

                    $ aubreywannafight = 0
                    jump bb_b

            label bb_a:

                scene fr2jo2d
                with dissolve

                u "Hell yeah! I'll be the next Fight King."

                u "(Shit, why did I say that?? I don't even know how to fight and I don't really want to either.)"

                scene fr2jo2a
                with dissolve

                au "Oh wow, big words. Have you met Grayson yet? I'm sure he'd like your confidence."

                scene fr2jo2b
                with dissolve

                u "Who's Grayson?"

                jump bb_ad

            label bb_b:

                scene fr2jo2b
                with dissolve

                u "No, I don't think that's for me."

                scene fr2jo2e
                with dissolve

                au "Really? Well, then what are you doing at the Apes' rush party?"

                au "Grayson doesn't accept non-fighters."

                scene fr2jo2f
                with dissolve

                u "Who's Grayson?"

                jump bb_bd


        label ba_ad:
        label ba_bd:
        label bb_ad:
        label bb_bd:

        scene fr2jo2a
        with dissolve

        au "He's the president of the Apes and the current Fight King."

        if aubreywannafight == 1:

            au "I think he's upstairs, but I'm not sure."

            scene fr2jo2b
            with dissolve

            u "Alright, I'll leave you guys alone and look around a bit more. Maybe I'll even talk to Grayson."
        else:

            au "You'll never know, maybe if you meet some of the Apes, you'll change your mind about fighting."

            scene fr2jo2b
            with dissolve

            u "(I doubt it, but I guess it won't hurt to talk to some of them.)"

            u "Alright, I'll leave you guys alone and look around a bit more."

        scene fr2jo2a
        with dissolve

        au "I'll see you later, [name]."

        scene fr2jo1a
        with dissolve

        jo "Yeah bro, hit me up sometime."

        $ showphone = True

        call screen freeroam2b

    label fr2josh2:

        scene s102

        u "(I should talk to some other people around here and make some new friends.)"

        call screen freeroam2b

    label fr2stairs:
        if joshtalk == 0:

            scene s102

            u "(I should talk to Josh first, I haven't seen him in a while.)"

            call screen freeroam2b
        else:

            $ phoneexit = "phonem"
    label phonem:

        call screen freeroam2e


    label fr2camp:
        if joshtalk == 0:

            scene s102

            u "(I should talk to Josh first, I haven't seen him in a while.)"

            call screen freeroam2b
        else:
            if latext == 0:
                play sound "sounds/vibrate.mp3"
                $ laisreply = 1
                $ lamsgnot = 1
                $ msgnot = 1
                $ contact_Lauren.newMessage(laurenMessage4)
                $ lamsg4 = "Hey :)\nSorry about today.\n\nCan we talk tomorrow?"
                $ larep4a = "Yeah, sure."
                $ larep4b = "What is there to talk about?"
                $ lamsg5 = "Cool :)"
                $ lamsg6 = "Idk, it's just feels kinda weird now. Can we please just talk tomorrow?"
                $ larep6a = "Fine."
                $ lamsg7 = ":)"
                $ lamsg = 4
                $ latext = 1

            $ phoneexit = "phonen"

    label fr2dontend:
    label phonen:
        call screen freeroam2d

    label fr2mason:

        $ showphone = False
        $ masontalk = 1

        scene fr2ma1
        ma "Eyyyy, you're the kid that tried to fight Cameron yesterday!"

        scene fr2ma1a
        with dissolve
        u "What? I didn't-"

        scene fr2ma1b
        with dissolve

        jeremy "Damn, that takes balls, kid!"


        menu:


            "Yeah, he better watch out.":

                $ addPoint("tm", 1)
                $ addPoint("bro", 1)
                jump bc_a

            "I didn't wanna fight him.":

                jump bc_b

        label bc_a:

            scene fr2ma1a
            with dissolve

            $ bigmouth = True
            if steam == False:
                image bigmouth = "images/bigmouth.png"
                show bigmouth:
                    xpos 0
                    ypos -200
                    linear 0.5 xpos 0 ypos 0
                    pause 2.0
                    linear 0.5 xpos 0 ypos -200
            else:
                $ achievement.grant("big_mouth")
                $ achievement.sync()

            u "Yeah, he better watch out, or I'll kick his ass."

            u "(Yeah [name], that seems like a brilliant thing to say about a hyper-aggressive idiot that prides himself in his fighting skills.)"

            scene fr2ma1b
            with dissolve

            jeremy "That's some big words, kid."

            scene fr2ma1a
            with dissolve

            ma "We're doing a small tournament in the basement, you should sign up. We can put you up against Cameron if you want."


            scene fr2ma2
            with dissolve

            jeremy "Mason, that's a little much, no? He's just a kid."

            scene fr2ma2a
            with dissolve

            ma "Bullshit, he's a freshman and he can handle it! And if he wants to be an Ape, he's gonna have to fight Cameron anyways at some point."

            scene fr2ma2b
            with dissolve

            u "Alright guys, I'll definitely uhm..."

            scene fr2ma1a
            with dissolve

            u "I'll uh..."

            u "I need to go, but I'll talk to you later."

            scene s104

            u "(Oh no, what have I gotten myself into?!)"

            $ showphone = True

            call screen freeroam2c

        label bc_b:

            scene fr2ma1a
            with dissolve

            u "I uhh... I didn't actually wanna fight Cameron. I just bumped into him by accident."

            scene fr2ma1b
            with dissolve

            jeremy "Ahh, that makes more sense, 'cause you don't really seem like you have it in you."

            scene fr2ma2d
            with dissolve

            ma "Damn, and just as I thought we had a good one, he's just another pussy. Why are there always so many losers that try to get into the Apes?!"

            scene fr2ma2b
            with dissolve

            u "Hey! I'm not a loser, or a pussy. I would totally fight Cameron and he'd probably end up begging for mercy."

            scene fr2ma1b
            with dissolve

            u "(Fuck, why did I just say that?! I can't even fucking fight and that guy is a hyper-aggressive idiot that prides himself in his fighting skills.)"

            scene fr2ma1b
            with dissolve

            jeremy "That's some big words, kid."

            scene fr2ma1a
            with dissolve

            ma "You know, we're doing a small fighting tournament in the basement, you should sign up. We can put you up against Cameron if you want."

            scene fr2ma1b
            with dissolve

            jeremy "Yeah, show us what you got. If you beat Cameron, you're pretty much guaranteed to become an Ape."

            scene fr2ma1a
            with dissolve

            u "Alright guys, I'll definitely uhm..."

            u "I'll uh..."

            u "I need to go, but I'll talk to you later."

            scene s104

            u "(Oh no, what have I gotten myself into?!)"

            $ showphone = True

            call screen freeroam2c

    label fr2mason2:

        scene s104

        u "I've already talked to these guys."

        call screen freeroam2c

    label fr2katy:

        $ showphone = False

        $ katytalk = 1

        scene fr2ka1

        katy "And then she said \"Those jeans look so good on you.\" Can you believe that?!"

        katy "That stupid bitch is always saying stuff like that even though she knows exactly what it means."

        scene fr2ka1a
        with dissolve

        sarah "Katy, are you sure that she didn't just give you a compliment?"

        scene fr2ka1
        with dissolve

        katy "Oh my god, you sound just like my mom."

        scene fr2ka1b
        with dissolve

        u "Uhm... hey guys."

        scene fr2ka2
        with dissolve

        katy "Oh, hey there, handsome."

        scene fr2ka2a
        with dissolve

        sarah "Katy! You have a boyfriend."

        scene fr2ka2b
        with dissolve

        katy "Uuugh, fiiine."

        scene fr2ka2c
        with dissolve

        katy "Hey there, ugly."

        scene fr2ka2d
        with dissolve

        u "Uh... hey. What are you guys up to tonight?"

        scene fr2ka2e
        with dissolve

        katy "Partying, obviously."

        scene fr2ka2d
        with dissolve

        u "Cool uhm... me too."

        scene fr2ka2e
        with dissolve

        katy "Yeah, duh. Geez, small talk much???"

        scene fr2ka2g
        with dissolve

        sarah "Katy! Play nice."

        scene fr2ka2b
        with dissolve

        katy "Whatever, this guy's a dork."

        scene fr2ka2f
        with dissolve

        sarah "She doesn't mean that."

        scene fr2ka2d
        with dissolve

        u "It's fine, I'll leave."

        call screen freeroam2c

        label fr2katy2:

        scene s104

        u "(I'm definitely not going back there.)"

        $ showphone = True

        call screen freeroam2c

    label fr2grayson:

        $ graysontalk = 1
        $ showphone = False

        scene fr2gr1

        ca "Dude, all these freshmen are shit. I've been watching most of tonight's fights and they're garbage."

        scene fr2gr2
        with dissolve

        gr "They're rookies, we'll find the best and train them 'til they're good."

        scene fr2gr2a
        with dissolve

        ca "I still think we're wasting our time."

        scene fr2gr2
        with dissolve

        gr "I'm not allowing the Wolves to get any good rookies this year."

        gr "Without new talent, they've already lost. Because currently, Chris and his lackeys don't stand a chance against me."

        scene fr2gr2a
        with dissolve

        ca "Sure, but... none of the rookies would stand a chance against us either."

        scene fr2gr3
        with dissolve

        gr "Cameron, Cameron - do you trust me?"

        scene fr2gr3a
        with dissolve

        ca "Uhh... yeah. Of course, man."

        scene fr2gr3
        with dissolve

        gr "Then find the best freshmen and recruit them."

        scene fr2gr2b
        with dissolve

        gr "We're building the Apes' legacy here. 10 Years from now, I'll be the most successful Ape president in history."

        gr "And you could be the most successful vice president."

        scene fr2gr2c
        with dissolve

        ca "Alright man. Whatever you say."

        scene s105
        with dissolve

        u "(Is that this Grayson guy that Aubrey talked about? He sounds like even more of a dick than Cameron.)"

        $ showphone = True
        call screen freeroam2e

    label fr2grayson2:
        scene s105
        with dissolve

        u "(Somehow barging into a private conversation of two violence-addicted frat guys doesn't sound appealing to me.)"

        call screen freeroam2e

    label fr2chloe:

    scene s106

    call screen endfreeroam2

label fr2end:


    stop music fadeout 2.0
    $ showphone = False
    scene chloelook:
        subpixel True
        size (1920, 1080) crop (0, 0, 7680, 4320) #first tuple is the size of game screen, second is size of picture in pixels
        linear 0 crop (2700, 3000, 1920, 1080) # first float is time in seconds, tuples are coordinates of the upper left corner of a rectangle, and the second tuple is the size of that rectangle
        linear 8.0 crop (2700, 0, 1920, 1080) #here we change the y coordinate over 8 seconds to pan the image up

    " "

    u "Ryan?"

    play music "music/mlove.mp3"
    scene s108
    with dissolve

    ry "What's up, man? You enjoying the party?"

    scene s108a
    with dissolve

    u "Who is that?"

    scene s109
    with dissolve

    ry "I think that's Chloe, right? I talked to some of the Chicks and she's like their president."

    ry "Also, possibly the hottest girl I've seen in my life."

    u "And who's that guy she's talking to? Is that her boyfriend?"

    scene s108b
    with dissolve

    ry "Man, I don't know. Why don't you just go ask her yourself?"


    menu:



        "You're right, I'll talk to her.":

            $ addPoint("bro", 1)
            jump bd_a

        "She's occupied.":

            jump bd_b

    label bd_a:

        scene s108e
        with dissolve

        u "Yeah, you're right! I'm gonna go over there and talk to her right now."

        scene s108
        with dissolve

        ry "Good luck, man."

        scene s108f
        with dissolve

        u "(Here I go.)"

        scene s109
        with dissolve

        u "Hey there, guys."

        scene s112b
        with dissolve

        cl "Hey, what's your name?"

        jump bd_ad

    label bd_b:

        scene s108c
        with dissolve

        u "I don't know... She's talking to someone right now and I don't wanna come off as rude."

        scene s108d
        with dissolve

        ry "I'm sure it's fine."

        scene s110 ### ryans hand on your back
        with dissolve

        "*Push*"

        scene s111 ### you stumbling into chloe and the guy
        with vpunch

        u "Woah!"

        scene s112 ## chloe looking at you
        with dissolve

        cl "Are you okay?"

        scene s112a
        with dissolve

        u "Yeah, my friend just pushed me, sorry."

        scene s112b
        with dissolve

        cl "It's fine, haha. What's your name?"

        jump bd_bd

    label bd_ad:
    label bd_bd:

    scene s112c
    with dissolve

    u "I'm [name] and you?"

    scene s112b
    with dissolve

    cl "I'm Chloe."

    scene s113
    with dissolve

    tom "Hey champ, it's cool that you're talking to new people, et cetera, but we were kinda in the middle of something."
    tom "So you should probably... you know, leave."

    scene s112d
    with dissolve

    cl "Tom, come on. Why are you being such a dick? We're at a party."

    scene s113a
    with dissolve

    tom "Yeah, but we were in the middle of a conversation."

    scene s112d
    with dissolve

    cl "You were telling me about your rock collection... I'm actually quite happy we've moved on from that."

    scene s113a
    with dissolve

    tom "They're minerals!"
    tom "You know what, fine. Enjoy talking to this loser, 'cause I'm outta here."

    scene s112e
    with dissolve


    menu:

        "Apologize":

            $ addPoint("bf", 1)
            jump be_a

        "Make fun of him":

            $ addPoint("bro", 1)
            jump be_b

    label be_a:

        u "I'm really sorry for interrupting your conversation."

        scene s112b
        with dissolve

        cl "I should be thanking you for saving me. He literally spent the last 20 minutes talking about rocks."

        scene s112c
        with dissolve

        u "In that case, you're very welcome."

        jump be_ad

    label be_b:

        u "Don't worry, I'm not gonna start talking about my rock collection."

        scene s112b
        with dissolve

        cl "Oh that's too bad, I only go for guys that brag about them constantly."

        scene s112c
        with dissolve

        u "Aww damn. I think your dream guy just ran off."

        scene s112f
        with dissolve

        cl "I guess I'll have to make do with you."

        scene s112g
        with dissolve

        u "Haha, I guess you will."

        jump be_bd

    label be_ad:
    label be_bd:

    scene s112b
    with dissolve

    cl "Hey, do you wanna go outside and sit down? I could really use some fresh air."

    scene s112c
    with dissolve

    u "Yeah, sounds great."

    stop music fadeout 2.0

    scene s114 ## walking on the outside , use night filter
    with fade

    cl "So you're a first year, huh? Are you excited to get into the college lifestyle?"

    play music "music/mlove2.mp3"
    scene s114a
    with dissolve

    u "I mean, I guess. I don't really know what that includes to be honest."

    scene s114
    with dissolve

    cl "You know, parties, drinking, wild sex..."

    scene s114c
    with dissolve

    u "Are you just describing your weekend?"

    scene s114b
    with dissolve

    cl "Hahaha, maybe."

    scene s115
    with fade

    cl "Let's sit down here."

    scene s116
    with dissolve

    cl "I remember being so nervous in my first year."

    cl "One time a guy stole my underwear and somehow the dean found out about it."

    cl "Both of us then had to come to his office, so that the guy could apologize and give me my panties back right in front of the dean."

    cl "It was sooo embarrassing."


    menu:


        "Empathize":

            $ addPoint("bf", 1)
            jump bf_a

        "Poke fun":

            $ addPoint("tm", 1)
            jump bf_b

    label bf_a:

        scene s116a
        with dissolve

        u "Wow, that sounds awful."

        scene s116b
        with dissolve

        cl "It really was."

        jump bf_ad

    label bf_b:

        scene s116a
        with dissolve

        u "Hahaha, sounds like the dean was into you."

        scene s116d
        with dissolve

        cl "Ewww. Don't say that, hahaha."

        jump bf_bd

    label bf_ad:
    label bf_bd:

    scene s116c
    with dissolve

    u "So, you're the president of the Chicks, right?"

    scene s116b
    with dissolve

    cl "Yeah, I am."

    scene s116c
    with dissolve

    u "Are you close with Aubrey then? She told me she was the vice president."

    scene s116d
    with dissolve

    cl "Oh yeah, she's my best friend. Haha, why are you asking?"

    scene s116e
    with dissolve

    u "Just wondering. Do you know Josh as well then?"

    scene s116d
    with dissolve

    cl "Josh...? Oh is that the guy she's been talking to all night?"

    scene s116e
    with dissolve

    u "Yeah, I've known him since middle school and let's just say he's always been very eager to get with girls."

    scene s116b
    with dissolve

    cl "Hahaha, Aubrey's also not the shy type."

    cl "Could you imagine if they were sitting here by themselves right now?"

    scene s117
    with dissolve

    u "He'd just be like..."

    scene s117a
    with dissolve

    u "\"*Yawn* I guess I might as well leave my arm here.\""

    scene s117b
    with dissolve

    cl "Hahaha, and she'd just be like..."

    scene s117c
    with dissolve

    cl "\"Oh no, my hand landed on your abs, but I might as well feel them for a bit.\""

    scene s117d
    with dissolve

    u "Hahaha."

    scene s117e #both looking at each other pre kiss
    with dissolve

    " "
    scene s117c
    with dissolve

    cl "It's getting pretty cold. Should we go back inside?"

    stop music fadeout 2.0

    scene s117f
    with dissolve

    u "Uhh... yeah, let's go."
    play music "music/mparty2.mp3"
    scene s118 # looking from behind main room at l and chloe
    with fade

    cl "Oh look, they're still talking and now they're even closer to each other, haha."


    scene s119d # chloe close up
    with dissolve

    u "You know what they should just skip to?"

    scene s119
    with dissolve

    cl "What?"

    scene s119a
    with dissolve

    u "The part where he grabs her head like this..."

    scene s119c
    with dissolve

    u "Pulls her in..."

    u "And goes for the..."

    scene s120 ### hand grabbing on your shoulder
    with vpunch

    "Hey!"

    scene s121 #loooking at angry Grayson"
    with dissolve

    " "
    scene s120a
    with dissolve

    scene s1
    stop music
    #####punch
    $ renpy.movie_cutscene("punchdemo.webm", loops=0)
    scene s1

    " "




############## END OF DEMO




################


    #  blurry # muffled sounds
    play music "music/muffledparty.mp3"
    scene s121a
    with Fade (1,0,1)


    cl "*Muffled* Why did you do that?! We were just talking!"

    scene s121b
    with dissolve
    ry "*Muffled* [name]?! Are you okay??"

    stop music fadeout 2.0

    # you wake up in your room with Imre

    scene s123
    with Fade (3,0,3)

    imre "Hey man, did you have a good night?"

    play music "music/m9punk.mp3"
    scene s123a
    with dissolve

    u "What? How did I get here?"

    scene s123
    with dissolve

    imre "Some Ryan guy dropped you off, after you got yourself beaten up."

    scene s123a
    with dissolve

    u "Shit... my head hurts so much."

    scene s123
    with dissolve

    imre "I mean, have you seen your face?"

    imre "Here, I took a picture last night when you came home."

    scene s123b
    with fade ## holding phone with picture of you beaten up on it
    " "

    scene s123a
    with fade

    u "Man, Grayson is such an asshole. I didn't even do anything."

    scene s123c
    with dissolve

    imre "What did you expect? I told you the Apes are dogshit."

    imre "If you knew how to fight, maybe he wouldn't fuck with you."

    menu:



        "Hmm... maybe.":

            $ addPoint("bro", 1)
            $ imrethinkaboutit = True
            jump bh_a

        "I'm not fighting.":

            $ addPoint("bf", 1)
            $ imrethinkaboutit = False
            jump bh_b



    label bh_a:
        scene s123d
        with dissolve
        u "Hmm... maybe."

        scene s123
        with dissolve
        imre "Just think about it, okay? I'll see you later."

        jump bh_ad






    label bh_b:
        scene s123d
        with dissolve
        u "I'm not fighting. I'll just stay away from them."

        scene s123c
        with dissolve

        imre "Dude, you don't know what Grayson's like."

        imre "If he sees you looking at him wrong from now on, you'll end up in the hospital."

        menu:


            "I'll think about it.":

                $ addPoint("bro", 1)
                $ imrethinkaboutit = True
                jump bjj_a

            "I won't fight.":

                $ addPoint("bf", 1)
                $ imrethinkaboutit = False
                jump bjj_b



        label bjj_a:
            scene s123d
            with dissolve
            u "Look, I'll think about it. But don't get your hopes up."

            scene s123
            with dissolve
            imre "That's all I'm asking for. I'll see you later."

            jump bjj_ad




        label bjj_b:
            scene s123d
            with dissolve
            u "I'm not fighting. That's final."

            scene s123c
            with dissolve

            imre "You're being stupid, man. Whatever, suit yourself."

            jump bjj_bd

        label bh_ad:
        label bjj_ad:
        label bjj_bd:


        scene s96g
        with fade


        play sound "sounds/vibrate.mp3"
        queue sound "sounds/vibrate.mp3"

        $ showphone = True
        $ msgnot = 1
        $ rymsgnot = 1
        $ lamsgnot = 1
        $ ryisreply = 1
        $ rymsg = 4
        $ contact_Ryan.newMessage(ryanMessage4)
        $ rymsg4 = "You okay?"
        $ ryrep4a = "I'm fine"
        $ ryrep4b = "No, wtf was that?! Fuck Grayson and fuck the Apes"
        $ rymsg5 = "Look, I know what Grayson did was a dick move, but he was just being overprotective of Chloe"
        $ ryrep5a = "Whatever"
        $ ryrep5b = "Don't you dare defend that guy"
        $ rymsg6 = "Sorry..."
        $ lamsg = 8
        $ larep8a = "Yeah, SV cafe in 20 mins?"
        $ larep8b = "Sorry, I can't"
        $ lamsg9 = "Is everything okay?"
        $ larep9a = "Yeah, I'm fine."
        $ lamsg10 = "Okay..."
        $ lamsg11 = "Great, I'll see you then :)"
        $ temp_MessageNot = True
        $ phoneexit = "phoneo"
        if not laurenMessage4.reply:
            $ contact_Lauren.newMessage(laurenMessage8b)
        else:
            $ contact_Lauren.newMessage(laurenMessage8a)


        " "
        label repeatb:
        label phoneo:

        scene s96g
        with dissolve

        if not laurenMessage8a.reply and not laurenMessage8b.reply:
            u "(Damn, my phone's blowing up. I should probably check my messages.)"

            jump repeatb

        else:
            $ showphone = False
            if meetlauren == True:
                u "(Well, time to head to the cafe to meet Lauren.)"

                jump meet_lauren1

            else:
                u "(There's too much on my mind to be dealing with Lauren right now.)"

                u "(Maybe taking a walk will relax me.)"

                jump walk1

    label meet_lauren1:
    label walk1:
    stop music fadeout 2.0
    scene s124
    with Fade (1,0,1)

    u "(I can't believe I got knocked out in front of everyone...)"

    play music "music/m4punk.mp3"

    u "(Especially in front of Chloe, that's so humiliating.)"

    scene s124a
    with dissolve

    u "(Is she dating Grayson? I really thought she was flirting with me.)"

    u "(But why would Grayson punch me otherwise?)"

    u "(Just thinking about all this shit makes me so mad.)"

    scene s125
    with dissolve

    tom "Eyy, Mr. steal-your-girl got beaten up. *laughs*"

    tom "That's what you get for being such a little bitch."

    menu:



        "Shout back":

            $ fighttom = True
            jump bj_a

        "Keep walking":

            jump bj_b


    label bj_b:

    scene s125a
    with dissolve

    tom "Yeah, you better keep walking, pussy."

    menu:


        "Shout back":

            $ fighttom = True
            jump bk_a

        "Walk away":

            $ fighttom = False
            jump bk_b

    label bj_a:
    label bk_a:

    scene 126a # tom close up
    with dissolve

    u "The fuck did you just say to me?!"

    scene s126
    with dissolve

    tom "You heard me. You're a fucking bitch that tried to cockblock me."

    scene 126a
    with dissolve

    u "Dude, she wanted to talk to me. She was happy that you left. You bored her."
    scene push12
    image tompush = Movie(play="images/tompush.webm", start_image="images/126a.jpg", image="images/push12.jpg", loop = False)


    scene tompush
    $ renpy.pause(0.7)
    play sound "sounds/push.mp3"
    scene push12
    with vpunch

    tom "Fuck you!"

    stop music fadeout 2.0



    label gb:
    $ _game_menu_screen = "ingmenu"
    $ firstfight = True
    if adamtut == False:

        scene sf1
        with dissolve
        " "

    $ stance = 1
    image abo = "images/abo.png"
    image aboq = "images/q button.png"
    image abow = "images/w button.png"
    image abor = "images/r button.png"
    image abod = "images/abod.png"
    image bboq = "images/block q.png"
    image bbow = "images/block w.png"
    image bbor = "images/block r.png"
    image 3hits = "images/3 hits.png"
    image 4hits = "images/4 hits.png"
    image 5hits = "images/5 hits.png"
    image jab2movie = Movie(play="images/jab2.webm", start_image="images/jab2start.jpg", image="images/jab2pic.jpg", loop = False)
    image tomfinishmovie = Movie(play="images/tomfinish.webm", start_image="images/tomfinishstart.jpg", image="images/tomfinish.jpg", loop = False)
    image youfinishmovie = Movie(play="images/youfinish.webm", start_image="images/youfinishstart.jpg", image="images/youfinish.jpg", loop = False)
    image hook2movie = Movie(play="images/hook2.webm", start_image="images/hook2start.jpg", image="images/hook2pic.jpg", loop = False)
    image kick1movie = Movie(play="images/kick1.webm", start_image="images/kick1start.jpg", image="images/kick1pic.jpg", loop = False)
    image tomjabmovie = Movie(play="images/tomjab.webm", start_image="images/tomjabstart.jpg", image="images/tomjab.jpg", loop = False)
    image tomkickmovie = Movie(play="images/tomkick.webm", start_image="images/tomkickstart.jpg", image="images/tomkick.jpg", loop = False)
    image kick2movie = Movie(play="images/kick2.webm", start_image="images/kick2start.jpg", image="images/kick2pic.jpg", loop = False)
    image tomhookmovie = Movie(play="images/tomhook.webm", start_image="images/tomhookstart.jpg", image="images/tomhook.jpg", loop = False)
    image hook1movie = Movie(play="images/hook1.webm", start_image="images/hook1start.jpg", image="images/hook1pic.jpg", loop = False)
    image jab1movie = Movie(play="images/jab1.webm", start_image="images/jab1start.jpg", image="images/jab1pic.jpg", loop = False)
    image hookcountermovie = Movie(play="images/hookcounter.webm", start_image="images/hookcounterstart.jpg", image="images/hookcounter.jpg", loop = False)
    image jabcountermovie = Movie(play="images/jabcounter.webm", start_image="images/jabcounterstart.jpg", image="images/jabcounter.jpg", loop = False)

    image farrow1 = "images/farrow1.png"
    image targets = "images/targets.png"
    scene tomstancekick
    with dissolve

    if adamtut == False:
        call screen skiptut
    label sta:


    tut "In every fight, you'll have positions from which you can attack and positions from which you'll need to defend."

    tut "In attacking positions you'll have a set of offensive actions, as shown on the left."

    tut "Since you're new to fighting, you only have 3 simple attacks:"

    $ hl = 1
    tut "{b}Q{/b}: a quick, left-handed jab to create distance and attack the opponent's face from the front."
    $ hl = 2
    tut "{b}W{/b}: a strong, right-handed hook to attack the opponent's head from the side."
    $ hl = 4
    tut "And {b}R{/b}: a right-footed kick to attack the opponent's legs."
    $ hl = 0
    tut "As you learn more about fighting, you'll gain new attack moves."

    tut "When attacking, look at the opponent's stance and try to identify possible points of attack."
    show targets
    tut "With your three actions, there are three possible points of attack."
    $ hl = 4
    tut "Since Tom has his guard up and could probably block both a jab and a hook, try to kick him by pressing {b}R{/b} in the upcoming screen."
    $ hl = 0
    hide targets
    with dissolve


    $ stance = 1


    $ tomattack = renpy.random.choice([1, 2, 3])

    call screen tomtut1

    label tomtut1kick:


        scene kick2movie
        $ renpy.pause(0.7)
        play sound "sounds/ks.mp3"
        scene kick2pic
        with hpunch

        tut "Great job! You've hit Tom and hurt him. He's now more likely to get tired, give up or even get knocked out."
        tut "Beware, since you've let your guard down to attack, he's going to try and abuse it with an attack of his own."
        $ stance = 2


        scene tomhookmovie
        $ renpy.pause(0.7)

        scene tomhook

        tut "Now it's time to block Tom's attack."

        $ hl = 1
        tut "{b}Q{/b} lets you block your head from heavy attacks such as hooks, which come from a slight angle."
        $ hl = 2
        tut "In order to protect yourself from attacks flying straight at your face, such as jabs, press {b}W{/b}."
        $ hl = 4
        tut "Lastly, you can protect your legs, from low kicks for example, by pressing {b}R{/b}."
        $ hl = 1
        tut "As of right now, there's a hook flying at your head, press {b}Q{/b} in the upcoming screen in order to block it."
        $ hl = 0
        call screen kickcounter

    label tomtut1hook:


        scene hook1movie
        $ renpy.pause(0.7)
        play sound "sounds/bs.mp3"
        scene hook1pic
        with hpunch

        tut "Yeah, why follow what the tutorial says?? It's not like it's trying to help you or anything."

        tut "Because you decided to attack Tom's guarded areas, he was able to block your attack easily."

        tut "He can now counter attack."
        $ stance = 2


        scene hookcountermovie
        $ renpy.pause(0.7)

        scene hookcounter

        $ hl = 1

        tut "{b}Q{/b} lets you block your head from heavy attacks such as hooks, which come from a slight angle."
        $ hl = 2
        tut "In order to protect yourself from attacks flying straight at your face, such as jabs, press {b}W{/b}."
        $ hl = 4
        tut "Lastly, you can protect your legs, from low kicks for example, by pressing {b}R{/b}."
        $ hl = 2
        tut "As of right now, there's a jab flying at your face, press {b}W{/b} in the upcoming screen in order to block it."
        $ hl = 0


        call screen hookcounter


    label tomtut1jab:


        scene jab1movie
        $ renpy.pause(0.7)
        play sound "sounds/bs.mp3"
        scene jab1pic
        with hpunch

        tut "Yeah, why follow what the tutorial says?? It's not like it's trying to help you or anything."

        tut "Because you decided to attack Tom's guarded areas, he was able to block your attack easily."

        tut "He can now counter attack."

        $ stance = 2



        scene jabcountermovie
        $ renpy.pause(0.7)

        scene jabcounter

        tut "Now it's time to block Tom's attack."
        $ hl = 1

        tut "{b}Q{/b} lets you block your head from heavy attacks such as hooks, which come from a slight angle."
        $ hl = 2
        tut "In order to protect yourself from attacks flying straight at your face, such as jabs, press {b}W{/b}."
        $ hl = 4
        tut "Lastly, you can protect your legs, from low kicks for example, by pressing {b}R{/b}."
        $ hl = 1
        tut "As of right now, there's a hook flying at your head, press {b}Q{/b} in the upcoming screen in order to block it."
        $ hl = 0

        call screen jabcounter

    label tuthookblock2:
    label tuthookblock:


        play sound "sounds/bs.mp3"
        scene tomhookblock
        with hpunch

        tut "Great job, you blocked Tom's hook."

        scene tomstancehook

        tut "This ends the tutorial. The real fight will test your reaction times."

        if adamtut == True:
            jump fkcon
        else:
            call screen ft1

    label tuthookhit1:
    label tuthookhit2:
    label tuthookhit3:
    label tuthookhit4:

        play sound "sounds/hs.mp3"
        scene tomhookhit
        with hpunch

        tut "You did not block your head by pressing {b}Q{/b} and got hit. Next time, try to block the correct part of your body."

        scene tomstancehook

        tut "This ends the tutorial. The real fight will test your reaction times."

        if adamtut == True:
            jump fkcon
        else:
            call screen ft1

    label tutjabblock:
        play sound "sounds/bs.mp3"
        scene tomjabblock
        with hpunch

        tut "Great job, you blocked Tom's jab."

        scene tomstancehook

        tut "This ends the tutorial. The real fight will test your reaction times."

        if adamtut == True:
            jump fkcon
        else:
            call screen ft1

    label tutjabhit:
    label tutjabhit2:

        play sound "sounds/js.mp3"
        scene tomjabhit
        with hpunch

        tut "You did not block your face by pressing {b}W{/b} and got hit. Next time, try to block the correct part of your body."

        scene tomstancehook

        tut "This ends the tutorial. The real fight will test your reaction times."

        if adamtut == True:
            jump fkcon
        else:
            call screen ft1

        ########FIGHT SYSTEM


        label stb:

        call screen ft1



    label playf1:

        $ youdmg = 0
        $ tomdmg = 0
        $ tomstance = renpy.random.choice([1, 2, 3])
        $ tomattack = renpy.random.choice([1, 2, 3])
        call screen ft2

    label easy:
        $ reaction = 3
        $ reactiona = 3.2
        $ tomhealth = 3
        $ youhealth = 7
        jump fgo1

    label moderate:
        $ reaction = 1.3
        $ reactiona = 1.5
        $ tomhealth = 6
        $ youhealth = 4
        jump fgo2

    label hard:
        $ reaction = 0.5
        $ reactiona = 0.7
        $ tomhealth = 8
        $ youhealth = 3
        jump fgo3


    label simtomfight:
        $ simtomfight = True
        $ stance = 1
        jump tomsimstart

    label autowin:
        $ simtomfight = True
        $ stance = 1
        $ youhealth = 100000
        $ tomhealth = 3
        jump tomsimstart2

    label fgo1:
    label fgo2:
    label fgo3:
        call screen ft3


    label letsgo:
        $ stance = 1
        call screen youattack

    label changekeys:
        scene jab1pic
        with dissolve

        python:
            w = renpy.input("Which button should be hook / block face?")
            if w == "": w = "w"

        scene hook1pic
        with dissolve

        python:
            q = renpy.input("Which button should be jab / block head?")
            if q == "": q = "q"

        scene kick1pic
        with dissolve

        python:
            r = renpy.input("Which button should be kick / block leg?")
            if r == "": r = "r"

        if adamtut == True:
            call screen af3

        else:

            call screen ft3


    label tomkick1:

        if tomdmg >= tomhealth:

            scene youfinishmovie
            $ renpy.pause(1)
            play sound "sounds/fall.mp3"
            $ stance = 0
            $ youdmg = 0
            scene youfinish
            with vpunch
            $ renpy.pause()

            jump youfinish

        else:
            $ tomdmg += 1
            scene kick2movie
            $ renpy.pause(0.7)
            play sound "sounds/ks.mp3"
            scene kick2pic
            with hpunch

            pause 0.5 #Variable here
            jump tomattack1




    label tomkick2:
        if youdmg >= youhealth:

            scene tomfinishmovie
            $ renpy.pause(1)
            play sound "sounds/fall.mp3"
            $ stance = 0
            $ youdmg = 0
            scene tomfinish
            with vpunch

            $ renpy.pause()


            jump tomfinish6
        else:


            scene hook1movie
            $ renpy.pause(0.7)
            play sound "sounds/bs.mp3"
            scene hook1pic
            with hpunch

            pause 0.5
            jump tomattack2



    label tomkick3:
        if youdmg >= youhealth:

            scene tomfinishmovie
            $ renpy.pause(1)
            play sound "sounds/fall.mp3"
            $ stance = 0
            $ youdmg = 0
            scene tomfinish
            with vpunch

            $ renpy.pause()

            jump tomfinish6
        else:

            scene jab1movie
            $ renpy.pause(0.7)
            play sound "sounds/bs.mp3"
            scene jab1pic
            with hpunch

            pause 0.5

            jump tomattack3


    label tomsimstart2:
    label tomsimstart:
    label tomhook1:
        if tomdmg >= tomhealth:

            scene youfinishmovie
            $ renpy.pause(1)
            play sound "sounds/fall.mp3"
            $ stance = 0
            $ youdmg = 0
            scene youfinish
            with vpunch
            $ renpy.pause()

            jump youfinish


        else:

            scene hook2movie
            $ renpy.pause(0.7)
            play sound "sounds/hs.mp3"
            scene hook2pic
            with hpunch

            pause 0.5


            $ tomdmg += 1
            jump tomattack4

    label tomhook2:
        if youdmg >= youhealth:

            scene tomfinishmovie
            $ renpy.pause(1)
            play sound "sounds/fall.mp3"
            $ stance = 0
            $ youdmg = 0
            scene tomfinish
            with vpunch

            $ renpy.pause()

            jump tomfinish1
        else:


            scene jab1movie
            $ renpy.pause(0.7)
            play sound "sounds/bs.mp3"
            scene jab1pic
            with hpunch

            pause 0.5

            jump tomattack5

    label tomhook3:
        if youdmg >= youhealth:

            scene tomfinishmovie
            $ renpy.pause(1)
            play sound "sounds/fall.mp3"
            $ stance = 0
            $ youdmg = 0
            scene tomfinish
            with vpunch

            $ renpy.pause()

            jump tomfinish2
        else:


            scene kick1movie
            $ renpy.pause(0.7)
            play sound "sounds/ks.mp3"
            scene kick1pic
            with hpunch

            pause 0.5

            jump tomattack6


    label tomjab1:

        if tomdmg >= tomhealth:

            scene youfinishmovie
            $ renpy.pause(1)
            play sound "sounds/fall.mp3"
            $ stance = 0
            $ youdmg = 0
            scene youfinish
            with vpunch
            $ renpy.pause()

            jump youfinish

        else:


            scene jab2movie
            $ renpy.pause(0.7)
            play sound "sounds/js.mp3"
            scene jab2pic
            with hpunch


            $ tomdmg += 1

            pause 0.5

            jump tomattack7


    label tomjab2:
        if youdmg >= youhealth:


            scene tomfinishmovie
            $ renpy.pause(1)
            play sound "sounds/fall.mp3"
            $ stance = 0
            $ youdmg = 0
            scene tomfinish
            with vpunch

            $ renpy.pause()

            jump tomfinish3
        else:
            scene hook1movie
            $ renpy.pause(0.7)
            play sound "sounds/bs.mp3"
            scene hook1pic
            with hpunch

            pause 0.5

            jump tomattack8


    label tomjab3:

        if youdmg >= youhealth:


            scene tomfinishmovie
            $ renpy.pause(1)

            play sound "sounds/fall.mp3"
            $ stance = 0
            $ youdmg = 0
            scene tomfinish
            with vpunch

            $ renpy.pause()

            jump tomfinish4
        else:


            scene kick1movie
            $ renpy.pause(0.7)
            play sound "sounds/ks.mp3"
            scene kick1pic
            with hpunch

            pause 0.5
            jump tomattack9


    label tomattack1:
    label tomattack2:
    label tomattack3:
    label tomattack4:
    label tomattack5:
    label tomattack6:
    label tomattack7:
    label tomattack8:
    label tomattack9:
    label timer1:
    label timer2:
    label timer3:
        $ stance = 2

        if tomattack == 1:


            scene tomhookmovie
            $ renpy.pause(0.4)

            scene tomhook
            $ tomstance = renpy.random.choice([1, 2, 3])
            $ simyou = renpy.random.choice([1, 2, 3, 4])

            if simtomfight == True:
                if simtom == 1:
                    jump tomhookhit2
                if simtom == 2:
                    jump tomhookhit
                if simtom == 3 or 4:
                    jump tomhookblocked

            else:
                call screen tomattack




        if tomattack == 2:




            scene tomjabmovie
            $ renpy.pause(0.4)

            scene tomjab
            $ tomstance = renpy.random.choice([1, 2, 3])
            $ simyou = renpy.random.choice([1, 2, 3, 4])

            if simtomfight == True:
                if simtom == 1:
                    jump tomjabhit2
                if simtom == 2:
                    jump tomjabhit
                if simtom == 3 or 4:
                    jump tomjabblocked

            else:
                call screen tomattack

        if tomattack == 3:



            scene tomkickmovie
            $ renpy.pause(0.4)

            scene tomkick
            $ tomstance = renpy.random.choice([1, 2, 3])
            $ simyou = renpy.random.choice([1, 2, 3, 4])


            if simtomfight == True:
                if simtom == 1:
                    jump tomkickhit
                if simtom == 2:
                    jump tomkickhit2
                if simtom == 3 or 4:
                    jump tomkickblocked
            else:
                call screen tomattack


    label tomhookhit:
    label tomhookhit2:
    label timer4:

        play sound "sounds/hs.mp3"
        $ youdmg += 1
        scene tomhookhit
        with hpunch

        pause 0.5
        $ stance = 1
        $ tomattack = renpy.random.choice([1, 2, 3])
        $ simtom = renpy.random.choice([1, 2, 3, 4])

        if simtomfight == True:
            if tomstance == 1:
                if simyou == 1:
                    jump tomkick2
                if simyou == 2:
                    jump tomkick3
                if simyou == 3 or 4:
                    jump tomkick1
            if tomstance == 2:
                if simyou == 1:
                    jump tomhook2
                if simyou == 2:
                    jump tomhook3
                if simyou == 3 or 4:
                    jump tomhook1
            if tomstance == 3:
                if simyou == 1:
                    jump tomjab2
                if simyou == 2:
                    jump tomjab3
                if simyou == 3 or 4:
                    jump tomjab1
        else:
            call screen youattack

    label tomhookblocked:

        play sound "sounds/bs.mp3"
        scene tomhookblock
        with hpunch

        pause 0.5
        $ stance = 1
        $ tomattack = renpy.random.choice([1, 2, 3])
        $ simtom = renpy.random.choice([1, 2, 3, 4])
        if simtomfight == True:
            if tomstance == 1:
                if simyou == 1:
                    jump tomkick2
                if simyou == 2:
                    jump tomkick3
                if simyou == 3 or 4:
                    jump tomkick1
            if tomstance == 2:
                if simyou == 1:
                    jump tomhook2
                if simyou == 2:
                    jump tomhook3
                if simyou == 3 or 4:
                    jump tomhook1
            if tomstance == 3:
                if simyou == 1:
                    jump tomjab2
                if simyou == 2:
                    jump tomjab3
                if simyou == 3 or 4:
                    jump tomjab1
        else:
            call screen youattack

    label tomjabhit:
    label tomjabhit2:
    label timer5:

        play sound "sounds/js.mp3"
        scene tomjabhit
        with hpunch

        pause 0.5
        $ youdmg += 1
        $ stance = 1
        $ tomattack = renpy.random.choice([1, 2, 3])
        $ simtom = renpy.random.choice([1, 2, 3, 4])
        if simtomfight == True:
            if tomstance == 1:
                if simyou == 1:
                    jump tomkick2
                if simyou == 2:
                    jump tomkick3
                if simyou == 3 or 4:
                    jump tomkick1
            if tomstance == 2:
                if simyou == 1:
                    jump tomhook2
                if simyou == 2:
                    jump tomhook3
                if simyou == 3 or 4:
                    jump tomhook1
            if tomstance == 3:
                if simyou == 1:
                    jump tomjab2
                if simyou == 2:
                    jump tomjab3
                if simyou == 3 or 4:
                    jump tomjab1
        else:
            call screen youattack

    label tomjabblocked:

        play sound "sounds/bs.mp3"
        scene tomjabblock
        with hpunch

        pause 0.5
        $ stance = 1
        $ tomattack = renpy.random.choice([1, 2, 3])
        $ simtom = renpy.random.choice([1, 2, 3, 4])
        if simtomfight == True:
            if tomstance == 1:
                if simyou == 1:
                    jump tomkick2
                if simyou == 2:
                    jump tomkick3
                if simyou == 3 or 4:
                    jump tomkick1
            if tomstance == 2:
                if simyou == 1:
                    jump tomhook2
                if simyou == 2:
                    jump tomhook3
                if simyou == 3 or 4:
                    jump tomhook1
            if tomstance == 3:
                if simyou == 1:
                    jump tomjab2
                if simyou == 2:
                    jump tomjab3
                if simyou == 3 or 4:
                    jump tomjab1
        else:
            call screen youattack

    label tomkickhit:
    label tomkickhit2:
    label timer6:

        play sound "sounds/ks.mp3"
        scene tomkickhit
        with hpunch

        pause 0.5
        $ youdmg += 1
        $ stance = 1
        $ tomattack = renpy.random.choice([1, 2, 3])
        $ simtom = renpy.random.choice([1, 2, 3, 4])
        if simtomfight == True:
            if tomstance == 1:
                if simyou == 1:
                    jump tomkick2
                if simyou == 2:
                    jump tomkick3
                if simyou == 3 or 4:
                    jump tomkick1
            if tomstance == 2:
                if simyou == 1:
                    jump tomhook2
                if simyou == 2:
                    jump tomhook3
                if simyou == 3 or 4:
                    jump tomhook1
            if tomstance == 3:
                if simyou == 1:
                    jump tomjab2
                if simyou == 2:
                    jump tomjab3
                if simyou == 3 or 4:
                    jump tomjab1
        else:
            call screen youattack

    label tomkickblocked:

        play sound "sounds/ks.mp3"
        scene tomkickblock
        with hpunch

        pause 0.5
        $ stance = 1
        $ tomattack = renpy.random.choice([1, 2, 3])
        $ simtom = renpy.random.choice([1, 2, 3, 4])
        if simtomfight == True:
            if tomstance == 1:
                if simyou == 1:
                    jump tomkick2
                if simyou == 2:
                    jump tomkick3
                if simyou == 3 or 4:
                    jump tomkick1
            if tomstance == 2:
                if simyou == 1:
                    jump tomhook2
                if simyou == 2:
                    jump tomhook3
                if simyou == 3 or 4:
                    jump tomhook1
            if tomstance == 3:
                if simyou == 1:
                    jump tomjab2
                if simyou == 2:
                    jump tomjab3
                if simyou == 3 or 4:
                    jump tomjab1
        else:
            call screen youattack


    label tomfinish1:
    label tomfinish2:
    label tomfinish3:
    label tomfinish4:
    label tomfinish5:
    label tomfinish6:

    $ wintom = False

    scene tf

    " "

    jump tf2



    label youfinish:
        if reaction == 0.5:
            $ thenotorious = True
            if steam == False:
                image thenotorious = "images/thenotorious.png"
                show thenotorious:
                    xpos 0
                    ypos -200
                    linear 0.5 xpos 0 ypos 0
                    pause 2.0
                    linear 0.5 xpos 0 ypos -200
            else:
                $ achievement.grant("the_notorious")
                $ achievement.sync()
        $ wintom = True

        menu:

            "Kick him":
                $ addPoint("tm", 1)

                jump yf1

            "Walk away":
                $ addPoint("bro", 1)

                jump yf2


    label yf1:
        play sound "sounds/js.mp3"
        scene yf
        with vpunch

        u "Fuck you!"

        jump yf3
###############
    label bk_b:
    label yf3:
    label yf2:
    label tf2:
    $ firstfight = False

    $ renpy.end_replay()







    if meetlauren == False:

        jump walk2

    else:
        jump meet_lauren2


    label meet_lauren2:



    play music "music/mlove2.mp3"

    if fighttom == True:
        if wintom == False:
            scene s128a #outside of cafe with bloody nose
            with Fade (1,0,1)
            u "(Fuck, I feel like shit...)"

            u "(Hopefully Lauren doesn't make a big deal out of my bruises.)"

        else:
            scene s128 #outside of cafe
            with Fade (1,0,1)
            u "(Holy shit, I just knocked someone out...)"

            u "(Hopefully Lauren doesn't make a big deal out of my bruises.)"

    else:
        scene s128 #outside of cafe
        with Fade (1,0,1)
        u "(What a douchebag...)"

        u "(Hopefully Lauren doesn't make a big deal out of my bruises.)"

    scene s129 # seeing Lauren on a table in the cafe
    with fade

    la "Heyyy-"

    scene s129b
    with dissolve

    la "Oh my god! What happened to your face?!"

    scene s129c
    with dissolve

    u "Some asshole punched me in the face at the Apes' rush party last night."

    if fighttom == True:
        if wintom == False:
            u "(And also I just got beaten up by another guy on the way here...)"

        else:
            u "(And also I just beat a guy up on the way here...)"

    scene s130 # lauren accross table # your hands are on the table
    with fade

    la "[name], fighting is so stupid. Please don't get sucked up into it. You're way too smart for that."

    scene s130a
    with dissolve

    u "No but... I didn't even do anything."

    scene s130 # lauren accross table # your hands are on the table
    with dissolve

    la "Ugh okay...I hope that's true. Anyway..."







    scene s130b
    with dissolve
    $ influencetut = True
    $ itpage = 1

    la "About yesterday in the park..."

    menu:


        "There was something there.":

            $ addPoint("bf", 1)
            jump bl_a

        "Let's forget about it.":

            $ addPoint("bro", 1)
            jump bl_b

    label bl_a:

    if lakiss == 1:

        if laurenlike >= 2:
            scene s130c
            with dissolve
            u "I know you stopped kissing me after about a second..."

            u "But that second was amazing."

            u "There was something real there and you know it."

            jump nextscenek

        else:
            scene s130c
            with dissolve

            u "I don't know why you pulled away when I tried to kiss you..."

            u "Maybe you were scared..."

            u "But there was something real there and you know it."

            jump nextsceneg

    else:
        scene s130c
        with dissolve

        u "We had this moment where I wanted to kiss you, but I didn't..."

        u "And I should have. There was something real there. Between us."

        jump nextsceneh

    label nextscenek:
    label nextsceneg:
    label nextsceneh:

    $ influencetut = False

    if kct == "loyal" or firstkisslauren:

        $ laurenrs = True
        if kct == "loyal":
            call screen popup1

        label popup1:

        scene s131 ### Lauren grabbing your hand on the table
        with dissolve

        " "

        scene s130d # Lauren romancing at you holding your hand
        with dissolve

        $ anewbeginning = True
        if steam == False:
            image anewbeginning = "images/anewbeginning.png"
            show anewbeginning:
                xpos 0
                ypos -200
                linear 0.5 xpos 0 ypos 0
                pause 2.0
                linear 0.5 xpos 0 ypos -200
        else:
            $ achievement.grant("a_new_beginning")
            $ achievement.sync()

        la "Maybe you're right."


        scene s130e
        with dissolve

        u "Then let's go on a date. A real date."

        u "How about the movies? Tomorrow night."

        scene s130d
        with dissolve

        la "Okay yeah, let's do it."

        scene s130e
        with dissolve

        u "I'm really sorry, I'm late for class, but I'll see you tomorrow."

        scene s130d
        with dissolve

        la "Alright, see you tomorrow."

        if fighttom == True:
            if wintom == False:

                scene s130e
                with dissolve

                u "(I should probably wash the blood off my face in the restroom before I go to class.)"

        jump historya




    else:

        scene s130f # lauren flustered
        with dissolve

        la "[name], I really like you..."

        la "... but I think we're just better as friends."

        la "I don't wanna jeopardize our friendship."

        menu:



            "Give me a chance.":

                jump bm_a

            "You're right.":

                jump bm_b

        label bm_a:

        $ laawk = True

        scene s130g
        with dissolve

        u "Lauren, please... give me a chance."

        scene s130f
        with dissolve

        la "[name], I'm sorry. I just don't think we're right for each other."

        la "Look, I gotta go to class. I'm really sorry."

        scene s130g
        with dissolve

        u "Okay..."
        if fighttom == True:
            if wintom == False:

                scene s132 ## empty table, Lauren gone
                with fade
                u "(Shit, I forgot I have class right now.)"

                u "(I should probably wash the blood off my face before I go.)"


        jump historyb

        label bm_b:

        $ laawk = True

        scene s130g
        with dissolve

        u "Yeah, you're probably right. Let's just forget about it."

        scene s130j ## lauren smile
        with dissolve
        u "I'm late for class, but I'll see you later, okay?"

        scene s130h
        with dissolve

        la "Yeah, okay."

        if fighttom == True:
            if wintom == False:

                scene s130j
                with dissolve

                u "(I should probably wash the blood off my face in the restroom before I go to class.)"


        jump historyc

    label bl_b:

    $ laawk = False
    scene s130a
    with dissolve

    if lakiss == 1:

        u "That was uhm... nothing."

        u "Let's just forget that ever happened."

    else:

        u "I mean nothing happened... Maybe it was awkward, but let's just forget about it."

    u "We just spent some nice time in the park together... as friends."

    scene s131
    with dissolve

    " "

    scene s130d
    with dissolve

    la "I'm really glad to have you as a friend, [name]."

    scene s130j
    with dissolve

    u "Yeah, I'm glad too."

    u "I have class right now, but I'll see you later, okay?"



    scene s130h
    with dissolve

    la "Yeah, sounds great."

    if fighttom == True:
        if wintom == False:

            scene s130j
            with dissolve

            u "(I should probably wash the blood off my face in the restroom before I go.)"

    jump historyd



    label walk2:
    $ laawk = True
    scene s133
    with Fade (1,0,1) # in front of san vallejo
    if fighttom == True:
        if wintom == False:
            u "(Fuck, I feel like shit...)"

        else:

            u "(Holy shit, I just knocked someone out...)"

    else:
        u "(What a douchebag...)"

    u "(Also, what am I gonna do about Lauren? I can't avoid her forever.)"

    jump historye

    label historya:
    label historyb:
    label historyc:
    label historyd:
    scene s133
    with Fade (1,0,1)

    stop music fadeout 2.0


    label historye:

    play sound "sounds/vibrate.mp3"

    $ showphone = True
    $ msgnot = 1
    $ contact_Josh.unlock()
    $ jomsgnot = 1
    $ joisreply = 1
    $ jomsg = 1
    $ contact_Josh.newMessage(joshMessage1)
    $ contact_Josh.newMessage(joshMessage2)
    $ contact_Josh.newMessage(joshMessage3)
    $ jomsg1 = "Dude, I talked to this Aubrey chick the entire night and guess who's number she wanted..."
    $ jomsg2 = "YOURS"
    $ jomsg3 = "What a bitch..."
    $ jorep1a = "Sorry, man. She doesn't know what she's missing."
    $ jorep1b = "Sooo, did you give it to her?"
    $ jomsg4 = "It's fine, you go get her."
    $ jorep4a = "Thanks, I'll try my best."
    $ jomsg5 = "Nah, you don't want a bitch like her."
    $ jorep5a = "Yeah, I guess you're right."
    $ jorep5b = "Dude, what the fuck?!"
    $ jomsg6 = "Hahaha, I'm just kidding, yo."
    $ jomsg7 = "Of course I gave her your number."
    $ jorep7a = "Damn, you got me."
    $ phoneexit = "phonep"

    scene s133
    with dissolve

    " "


    label phonep:
    $ showphone = False

    u "(Time to sit through another boring ass lecture.)"

    play music "music/m16punk.mp3"
    scene s136 ## seeing Imre in lecture room looking apologetic
    with Fade (1,0,1)
    imre "Hey man, about earlier, I-"

    if fighttom == True:
        if wintom == True:
            scene s136a
            with dissolve

            u "Imre, I just beat someone up."

            scene s136d #Imre excited
            with dissolve

            imre "Holy shit, was it Grayson?!"

            scene s136e
            with dissolve

            u "Nah, his name's Tom, I think."

            scene s136d
            with dissolve

            imre "What happened?"

            if meetlauren == True:
                scene s136e
                with dissolve
                u "I don't know, he walked by me on my way to meet with Lauren and just started to insult me."
            else:
                scene s136e
                with dissolve
                u "I don't know, he walked by me on my walk and just started to insult me."


            scene s136b
            with dissolve
            imre "So you just knocked him out?!"

            scene s136c
            with dissolve

            u "I mean no, I just confronted him about it, he pushed me and next thing I know, we're fighting."

            u "And then I just landed a couple good punches and suddenly he was laying on the floor bleeding."

            scene s136h # Imre holding his hands in front of mouth
            with dissolve

            imre "Holy shit, you're a natural, dude"

            scene s136d
            with dissolve

            imre "Train with me. Just once. Just to see if you like it. Please."

            scene s136e
            with dissolve

            u "Fine, I'll train with you. But just one time."

            jump nextsceneo




        else:

            scene s136b
            with dissolve #Imre surprised

            imre "Dude, did you get beaten up again?! You look like shit!"

            scene s136f # Imre angry
            with dissolve

            imre "Was it another ape??? Tell me who, I'll fuck them up!"


            if meetlauren == True:
                scene s136g
                with dissolve
                u "Thanks.... and I don't know if he was an Ape, but he was also at the party and he started insulting me on my way to meet with Lauren."
            else:
                scene s136g
                with dissolve
                u "Thanks... and I don't know if he was an Ape, but he was also at the party and he started insulting me on my walk."


            scene s136f
            with dissolve
            imre "What did you do?"

            scene s136g
            with dissolve

            u "I confronted him, then he pushed me and then we started fighting."

            scene s136c
            with dissolve

            u "And then he just landed a couple good punches and suddenly I was laying on the floor bleeding."

            scene s136b
            with dissolve
            imre "Shit, man..."

            scene s136c
            with dissolve

            u "Honestly, maybe you're right and I do need to learn to defend myself."

            scene s136b
            with dissolve

            imre "Look, I'm gonna train tomorrow. Why don't you train with me?"

            scene s136c
            with dissolve

            u "Yeah, okay. Thanks Imre."

            jump nextscenen

    else:


        scene s136a
        with dissolve

        u "Imre, another guy tried to fight me today."

        scene s136b
        with dissolve

        imre "Oh shit, what happened? Another Ape?"

        if meetlauren == True:
            scene s136b
            with dissolve
            u "I don't know if he was an Ape, but he was also at the party and he started insulting me on my way to meet with Lauren."
        else:
            scene s136b
            with dissolve
            u "I don't know if he was an Ape, but he was also at the party and he started insulting me on my walk."


        scene s136b
        with dissolve
        imre "What did you do?"

        scene s136c
        with dissolve
        u "Well I didn't wanna get beaten up again, so I just walked away."

        scene s136b
        with dissolve

        imre "Dude, if you keep this up, you're gonna get treated like crap."

        imre "Look, I'm gonna train tomorrow. Why don't you train with me?"

        scene s136c
        with dissolve

        u "Okay... I guess I'll try it."

        jump nextscenem


    label nextscenem:
    label nextscenen:
    label nextsceneo:

    scene s134g  ### in lecture room, asian teacher Mr.Lee far away
    with fade

    lee "Welcome to History 101, I'm Mr. Lee."

    lee "I know that some of you have put this class off for multiple years, while others of you are taking it in their first year."

    scene s134 # closer
    with dissolve
    lee "Even though it is unfathomable to me how you could actively try to avoid the most exciting subject in the world..."

    lee "I guess there is something to be said about saving the best for last."



    scene s134a #walking to the side
    with dissolve

    lee "So what is history?"

    scene s134a2 #walking to the side
    with dissolve

    lee "Many people believe that history is about analyzing and understanding the past."

    scene s134b #finger pointing up
    with dissolve
    lee "But it's quite the contrary."

    scene s135 #lee face close up
    with dissolve
    lee "History is looking to the future... but backwards."


    scene s137
    with dissolve
    imre "*Whispers* What is he talking about??" ## Imre laughingly

    scene s137a
    with dissolve # you wispher back laughingly

    u "*Whispers* I don't know."

    scene s134
    with dissolve

    lee "Over the course of this year, you're not just going to learn about history."

    lee "You're going to live history, immerse yourself within it and understand what life was truly like in the past."

    scene s138 # Cameron shouts
    with dissolve

    ca "Yo teach, we get that you love the past, but don't you think the museum wants its shoes back?" ### item

    scene s139 # item closeup
    with dissolve

    "*Class laughing*"

    scene s134c #lee creepy smile
    with dissolve

    lee "What's your name, young man?"

    scene s138a # carmeron sarcasam
    with dissolve

    ca "It's Cameron, teach."

    scene s134c
    with dissolve

    lee "Mr. Cameron, if clothing is what gets you to pay attention in this class, then I suggest you dress up as a historical character for our next lesson."
    lee "As a matter of fact, I insist you do."

    scene s138a # cameron confident
    with dissolve

    ca "Sure, but I'll steal the show."

    scene s134d
    with dissolve

    lee "Perhaps you're right. Everyone should be wearing historically accurate costumes for the next lecture."

    "*Class confused*"

    lee "Come without costume and you've earned your first fail."

    lee "You've got Mr. Cameron to thank for that."

    stop music fadeout 2.0
    scene clocka
    with fade

    play sound "sounds/clock2.mp3"

    pause (0.5)

    scene clockb
    with dissolve

    pause (0.5)

    scene clockc
    with dissolve

    pause (0.5)

    scene clockd
    with dissolve

    pause (0.5)
    stop sound
    scene clocke
    with dissolve

    scene s140 # You and Imre in hallway
    with Fade (1,0,1)

    play music "music/m11punk.mp3"

    imre "I can't believe he's making us come in costume."

    scene s140a
    with dissolve

    u "Yeah, I don't even have anything I could wear. That's so annoying."

    u "Can we go to the mall later?"

    scene s140
    with dissolve

    imre "Sorry man, I heard the girls' volleyball team is playing and I'm not gonna miss that."

    scene s140a
    with dissolve

    u "I didn't know you were into volleyball."

    scene s140
    with dissolve

    imre "Oh, I'm not."

    scene s140a
    with dissolve

    u "Then why are you-"

    u "Oh..."

    scene s140b
    with dissolve

    imre "Hot girls in shorts getting sweaty? What more could I ask for?"

    scene s140c
    with dissolve

    u "Haha, you're impossible."



    scene s140b
    with dissolve

    imre "I got another class now, I'll see you later."


    ##############

    # PATRON RELEASE END

    #####


    scene s141 # Emily in corridor talking to nora
    with Fade (1,0,1)

    u "(Great... I guess it was only a matter of time 'til I saw Emily.)"


    scene s141a # Emily's head turns
    with dissolve

    em "[name]?"

    scene s142 # closeup
    with dissolve

    em "Oh my god, what happened to you?"


    scene s142b
    with dissolve

    no "Looks like he got beaten up."

    if hitonnora == 1:

        scene s142a # both mouths shut
        with dissolve

        u "I didn't-"

        scene s142b # Nora
        with dissolve

        no "Wait, you're the same kid that hit on me a few days ago."

        scene s142c # emily
        with dissolve

        em "Charming."

        scene s142d

        u "First of all, I was just telling you that you're cute."

        u "Secondly, the guy who punched me came out of nowhere, it wasn't a fair fight."

    else:


        scene s142a # Nora
        with dissolve

        u "I- I didn't get beaten up, okay? A guy just punched me out of nowhere, it wasn't a fair fight."

    scene s142e # Emily empathy
    with dissolve

    em "You know, your eye looks pretty swollen. You really need to get that checked out."

    scene s142f
    with dissolve

    u "It's fine."

    scene s142e
    with dissolve

    em "I'll come with you if you want."

    scene s142f
    with dissolve

    u "Emily, we're not-"

    scene s142g # Nora with fingers pointing no looking at em
    with dissolve

    no "Look, I'm sensing some weird energy between you two, so I'ma leave."


    no "Bye Emily."

    scene s142j # no looking at you em looking at no
    with dissolve

    no "Bye weirdo."

    scene s142k # no walking away
    with dissolve

    u "What? I didn't even-"

    em "I'll see you later, Nora."

    scene s144 # only emily
    with fade

    em "Come on, let's-"

    scene s144a
    with dissolve

    u "Emily, we're not friends. You cheated on me."



    scene s144b
    with dissolve


    em "[name], I know I fucked up. I'm really sorry, okay?"

    em "We hit a rough patch and I was drunk and..."

    em "I just miss us. Even if it's just as friends."

    em "Can we please just hang out?"



    menu:



        "Okay, I guess.":

            $ forgiveemily = True
            $ addPoint("bf", 1)


            jump bo_a



        "No, sorry.":
            $ emilyandben = True
            $ forgiveemily = False
            $ addPoint("tm", 1)


            jump bo_b


    label bo_a:

    scene s144c
    with dissolve

    u "Fine, let's go then."

    scene s144d #em happy
    with dissolve

    em "Really? Where do you wanna go?"

    scene s144e
    with dissolve

    u "I thought we're going to the doctor's office? Or are you gonna tell me that your concern was merely an attempt to hang out with me?"

    scene s144d
    with dissolve

    em "Right, of course not. Let's go."

    jump bo_ad

    label bo_b:

    scene s144c
    with dissolve

    u "No Emily."

    scene s144c # em sad mouth close
    with dissolve

    u "I can't just forgive you like that. You don't know what you put me through."

    scene s144b
    with dissolve

    em "Oh..."

    em "I'll go then..."

    scene s144c
    with dissolve

    u "Goodbye, Emily."

    jump bo_bd


label bo_ad:



    play music "sounds/bus.mp3"



    image s145far = ("images/s145far.png")
    image s145 = ("images/s145.png")
    image s145a = ("images/s145a.png")
    image s145b = ("images/s145b.png")
    image s145c = ("images/s145c.png")
    image s145d = ("images/s145d.png")
    image s145e = ("images/s145e.png")
    image s145bl = ("images/s145bl.png")
    image s145f = ("images/s145f.png")


    scene carback

    show s145far # bus with emily, animation???? seeing obth bus sounds
    with Fade (1,0,1)

    pause 0.5

    hide s145far
    show s145
    with dissolve

    em "Sooo... did you text your new girlfriend that you're hanging out with your ex?"



    menu:


        "Yeah, of course. (joke)":

            $ addPoint("tm", 1)
            jump bp_a

        "I'm still single.":

            $ addPoint("bf", 1)
            jump bp_b

    label bp_a:

    hide s145
    show s145a
    with dissolve

    u "Yeah, of course I did. I tell her everything."

    hide s145a
    show s145b
    with dissolve

    em "Oh... okay. That's- that's good. You should tell her stuff like this."

    hide s145b
    show s145bl
    with dissolve

    u "*Laughs* Emily, I'm kidding. I'm still single, I mean we only broke up a couple months ago."

    hide s145bl
    show s145c
    with dissolve

    em "[name], you gotta stop messing with me, haha."

    hide s145c
    show s145d
    with dissolve

    u "Oh come on, don't act like you didn't miss this."

    hide s145d
    show s145c
    with dissolve

    em "Maybe a little bit."

    jump bp_ad

    label bp_b:

    hide s145
    show s145e
    with dissolve

    u "Believe it or not, I'm still single."

    hide s145e
    show s145d
    with dissolve

    u "I mean we only broke up a couple months ago."

    hide s145d
    show s145f
    with dissolve

    em "I guess you're right. I was just... you know, curious."

    jump bp_bd

    label bp_ad:
    label bp_bd:
    hide s145c
    hide s145f
    show s145d
    with dissolve

    u "Hey, you remember the time you had your wisdom teeth pulled out and you looked like a hamster for 2 weeks straight?"

    hide s145d
    show s145c
    with dissolve

    em "Are you ever gonna stop bringing that up?"

    menu:



        "It was adorable.":

            $ addPoint("bf", 1)
            jump bq_a


        "It was so funny.":

            $ addPoint("bro", 1)
            jump bq_b

    label bq_a:

    hide s145c
    show s145d
    with dissolve #u looking romantic


    u "No way, you looked so adorable."

    hide s145d
    show s145f
    with dissolve
    em "What was adorable was how much you cared for me. I remember you bringing me a care package full of like a hundred different soups."

    em "It was so thoughtful."

    jump bq_ad

    label bq_b:

    hide s145c
    show s145d
    with dissolve

    u "It was sooo funny though."

    hide s145d
    show s145c
    with dissolve

    em "You're the one to talk, your face is literally swollen up right now."

    hide s145c
    show s145d
    with dissolve

    u "It's not my whole face, it's just my eye."

    u "Plus, it looks badass."

    hide s145d
    show s145c
    with dissolve

    em "Haha, I'm not sure who told you that."

    jump bq_bd


    label bq_ad:
    label bq_bd:

    stop music
    play sound "sounds/busstop.mp3"

    # bus stop sound

    hide s145c
    hide s145f
    show s145j
    with dissolve

    u "Shit, we gotta get off at this stop."

    stop sound

    scene s146far # doctors reception
    with Fade (1,0,1)

    play music "music/m16punk.mp3"

    u "Hey there, you accept walk-ins right?"

    u "I need someone to look at my eye."

    scene s146a # giving you forms
    with dissolve

    ben "Yeah, sure thing. Fill out these forms and then take a seat in the waiting room and I'll let you know when Dr. Ehrmantraut can slot you in."

    scene s147 #em pointing
    with dissolve

    em "Hey, I've seen you before, you went to school with my sister."

    em "Benjamin, right?"

    scene s146b
    with dissolve

    ben "Oh, I remember. You're Hannah's sister."

    scene s147a
    with dissolve

    em "Didn't you wanna become a lawyer?"

    scene s146c ## hands shrugigng to the side like IDK
    with dissolve

    ben "I mean yeah, but technically - I didn't get into law school."

    scene s146b
    with dissolve

    ben "But this is actually a really good job, you know."

    ben "It pays well. And I get benefits. Dental benefits."

    ben "So really, dream job."

    scene s147b # em smiling
    with dissolve

    em "Well, I'm glad you found something you like."

    scene s147c # em looking at you
    with dissolve

    em "Okay, I'm gonna go sit down in the waiting room while you fill out your forms."


    scene s147d
    with dissolve

    u "Cool, I'll be done in a second."


    # benjamin leaning over the counter while em goes to wait and you fill out forms

    scene s148
    with fade

    ben "So uhhh, are you hitting that, or can a bro make a move?"

    scene s148a # u lookiing up
    with dissolve

    ben "You know, even if you are hitting that... I'm totally fine with like a dual type of arrangement."

    scene s148b
    with dissolve

    u "Dude... aren't you like 30 or something?"

    scene s148a2
    with dissolve

    ben "What? I'm 24."

    menu:



        "Sure, knock yourself out.":

            $ emilyandben = True
            $ addPoint("bro", 1)
            jump br_a

        "Stay away from her.":

            $ emilyandben = False
            $ addPoint("bf", 1)
            jump br_b

    label br_a:

    scene s148b
    with dissolve

    $ overit = True
    if steam == False:
        image overit = "images/overit.png"
        show overit:
            xpos 0
            ypos -200
            linear 0.5 xpos 0 ypos 0
            pause 2.0
            linear 0.5 xpos 0 ypos -200
    else:
        $ achievement.grant("over_it")
        $ achievement.sync()

    u "Sure, knock yourself out, man. We're not an item."

    scene s148d
    with dissolve

    ben "Thanks, bro! I'll think of you when I'm doing her."

    scene s148e
    with dissolve

    u "Please don't..."

    jump  br_ad

    label br_b:

    scene s148b
    with dissolve

    u "Just - just stay away from her, okay?"

    scene s148a
    with dissolve

    ben "Fine, bro. Sorry for asking."

    jump br_bd


    label br_ad:
    label br_bd:

    scene s149 # emily in waiting room
    with fade

    em "All done with the forms?"


    menu:


        "Tell Emily about Benjamin":

            $ addPoint("bf", 1)
            $ addPoint("tm", 1)
            jump bs_a

        "Don't tell Emily":

            $ addPoint("bro", 1)
            jump bs_b


    label bs_a:

    scene s149a
    with dissolve

    u "Yeah, but while I was doing it Benjamin asked me if he could make a move on you."

    scene s150 # em close up flirting
    with dissolve

    em "Oh really, are you my guardian now?"

    scene s150a # em curious
    with dissolve
    em "What did you say?"

    if emilyandben == False:

        scene s150b
        with dissolve

        u "Uhm... I told him off."

        u "You know, just to protect you from having to deal with a creep."

        scene s150
        with dissolve

        em "Oh, so you're \"protecting\" me now, huh?"

        scene s150c # em flirting close
        with dissolve

        u "Oh shut up, if you wanna give him your phone number and have the worst date of your life, you're free to do so."

        scene s150d
        with dissolve

        em "Haha, I think I'm good."

        jump bs_ada

    else:

        scene s150b
        with dissolve

        u "I told him he should."

        u "I mean there's no way you'd go for him anyways."

        scene s150d
        with dissolve
        em "Haha, he is kinda cute."

        em "Plus he has a job."

        scene s150e
        with dissolve

        u "As a receptionist."

        jump bs_adb

    label bs_b:

        scene s149a
        with dissolve

        u "Yeah, I did. I guess now we gotta wait."

        u "What did you think of Benjamin by the way?"

        scene s150a
        with dissolve

        em "What do you mean?"

        scene s150b
        with dissolve

        u "You know, as a guy."

        scene s150d
        with dissolve

        em "I guess he's kinda cute, but also a bit weird."

        scene s150a
        with dissolve

        em "Why are you asking?"

        scene s150b
        with dissolve

        u "Just wondering."

        jump bs_bd

    label bs_ada:
    label bs_adb:
    label bs_bd:

    ### door opening benjamin coming in
    scene s151
    with dissolve

    ben "Dr. Ehrmantraut is now ready for you."

    scene s150d
    with dissolve

    em "I'll wait here, I saw a bunch of Vogues I wanna dig into."

    scene s152far ## doctors office
    with Fade (1,0,1)


    ehr "Okay, looking at you I'm gonna assume you're here because of your black eye?"

    scene s152far1
    with dissolve

    u "(Holy shit, I thought Dr. Ehrmantraut was a guy.)"

    scene s152far2
    with dissolve
    u "Uhh... yeah, my friend dragged me here in order to get it looked at."

    scene s152
    with dissolve

    ehr "Alright, let me have a closer look and see if there's anything unusual about it."

    scene s152b ## dr bending over to inspect your eye
    with dissolve

    ehr "Hmm..."

    ehr "It all looks fine to me."

    scene s152c
    with dissolve

    ehr "When did this happen?"

    scene s152d
    with dissolve

    u "Yesterday. I got punched in the face out of nowhere."

    scene s152c
    with dissolve

    ehr "Does it hurt a lot? I could prescribe you a week's worth of painkillers."

    scene s152d
    with dissolve

    u "(Why can't life be more like porn...? Sex with her would take any pain away.)"

    u "Uhm... no, that's fine. I doesn't hurt too badly."

    scene s152c
    with dissolve

    ehr "Well then, your face should be back to normal in a week. If it doesn't get better, please come see me again."

    scene s152d
    with dissolve

    u "Thanks, will do."

    u "(Now I really hope it doesn't get better...)"

    scene s153 ## em in waiting room reading vogue
    with Fade (1,0,1)

    u "Are you ready to go?"

    scene s153a
    with dissolve

    em "Yeah, let's leave."



label bo_bd:


    stop music fadeout 2.0

    scene s154 ## text from aubrey & you walking back alone
    with Fade (1,0,1)

    if forgiveemily == True:

        u "(Even though that just cost me almost a hundred dollars, it was kinda nice to spend time with Emily.)"

        u "(Still... I don't know if I can ever fully forgive her for what she did.)"


    # text from aubrey
    play sound "sounds/vibrate.mp3"
    $ phoneexit = "phoneq"
    $ showphone = True
    $ msgnot = 1
    $ contact_Aubrey.unlock()
    $ aubmsgnot = 1
    $ aubisreply = 1
    $ aubmsg = 1
    $ contact_Aubrey.newMessage(aubreyMessage1)
    $ contact_Aubrey.newMessage(aubreyMessage2)
    $ aubmsg1 = "Hey,\nJosh gave me your number\n\nI hope your face is feeling better after the shit that Grayson pulled..."
    $ aubmsg2 = "He's not even dating Chloe and you guys didn't even do anything so I don't know what he was thinking.\n\nAnyway, do you wanna like... hang out tomorrow?"
    $ aubrep2a = "Wait they're not dating?"
    $ aubrep2b = "My day tomorrow is quite full, but how about today?\n\nI need to buy a costume."
    $ aubmsg3 = "Yeah, I mean they had a thing a while ago but she broke it off 'cause he lied about some shit."
    $ aubmsg4 = "So... tomorrow?"
    $ aubmsg5 = "I've got dance practice tonight :("
    $ aubrep5a = "I'm not talking tonight, I can pick you up right now."
    $ aubmsg7 = "Oh wow, that's spontaneous, I like it haha.\n\nI guess come to the Chicks' house whenever you're ready and then we can go costume shopping."
    $ aubrep7a = "Cool, I'll be 20 mins."


    u "(Oh , I just got a message.)"
    label phoneq:
    label repeatc:
    if aubreyMessage2.reply == False:
        u "(I should check my messages.)"
        jump repeatc

    elif not aubreyMessage7.reply:
        u "(I should really reply to Aubrey.)"
        jump repeatc

    label continuec:
    $ showphone = False

    play music "music/mlove.mp3"



    scene s155
    with fade
    pe "Uhm... excuse me."

    pe "I- I know you-"

    scene s155a
    with dissolve

    u "Let me guess, you saw me get punched in the face at a party."

    scene s155
    with dissolve

    pe "Uhm, no, but that would explain your swollen eye."

    pe "You're in my History 101 class."

    scene s155a
    with dissolve

    u "With Mr. Lee?"

    scene s155b # pe smiling
    with dissolve

    pe "Yes. What other History 101 class is there?"

    scene s155c
    with dissolve

    u "Fair point. So... what's up? How can I help you?"

    scene s155
    with dissolve

    pe "Oh, well I saw you and I thought to myself \"Hey, I know this person and I should talk to him.\""

    scene s155a
    with dissolve
    u "Uhm, okay so-"

    scene s155
    with dissolve

    pe "And then I thought \"But what if I'm disturbing him?\" So I decided not to say anything."

    scene s155a
    with dissolve

    u "Well you're not-"

    scene s155
    with dissolve

    pe "But then I was like \"Penelope, you need to start talking to people at some point\" and then I approached you."


    scene s155a
    with dissolve

    u "Okay... I'm [name] and-"

    scene s155d #pe scared
    with dissolve

    pe "Oh god, is it weird? Did I make it weird?"

    pe "I should leave, this was a bad idea. Good bye."

    scene s155e # penelope turns around
    with dissolve

    pause 0.5

    scene s155f # you grab her arm
    with hpunch

    u "Wait."

    scene s155g # penelope turns head
    with dissolve

    u "There's no need to be nervous."

    u "So your name is Penelope right?"

    scene s155h
    with dissolve

    pe "Yes."

    scene s155g
    with dissolve

    u "So, what did you mean by \"you need to start talking to people at some point\"? Are you a freshman?"

    scene s155 # pe turns back around
    with dissolve

    pe "No, I'm a junior, but I just transferred to San Vallejo 'cause I got kicked out of my old college."

    pe "And my dad paid a lot of money so I could go to my old college and now he's super mad and he said I'll have to get a job 'cause he's gonna cut my money off."

    pe "And then I called my mom and said \"Mom, help! Dad is going crazy!\" But my mom was like \"You need to talk to him yourself.\""

    pe "I mean they don't really talk to each other since the divorce and it's like-"

    scene s155a
    with dissolve

    u "Okay, calm down. You-"

    scene s155d
    with dissolve

    pe "Oh god, am I oversharing again? I am, aren't I?"

    scene s155d2
    with dissolve

    u "It's all good. It's just... Why did you get kicked out of your old college?"

    scene s155
    with dissolve

    pe "Oh, I don't wanna say."

    scene s155a
    with dissolve

    u "Really? That's where you draw the line of not sharing?"

    scene s155
    with dissolve

    pe "Sorry but... it's bad, really bad."

    scene s155a
    with dissolve

    u "Come on, you can tell me."

    scene s155
    with dissolve

    pe "I'm really sorry, but I can't tell you. Please stop pressing me about it."



    scene s155a
    with dissolve

    u "Ugh... alright."

    play sound "sounds/vibrate.mp3"
    $ phoneexit = "phoner"
    $ msgnot = 1
    $ contact_Aubrey.unlock()
    $ aubmsgnot = 1
    $ aubisreply = 1
    $ contact_Aubrey.newMessage(aubreyMessage8)
    $ aubmsg = 8
    $ aubmsg8 = "Hey, are you nearby?"
    $ aubrep8a = "Yeah, I'm just on my way, I'll be right there."
    $ aubrep8b = "Sorry, something came up and I can't make it."
    $ aubmsg9 = "Oh, okay. Guess we'll have to postpone the costume buying."
    $ aubmsg10 = "Good :)"
    $ showphone = True

    u "(Fuck, I totally forgot about Aubrey. I guess it's time to make a decision.)"


    label phoner:
    label repeatg:

    if not aubreyMessage8.reply:

        u "(Aubrey's waiting for me, I need to let her know whether I'm coming or not.)"

        jump repeatg

    else:

        $ showphone = False

        if costumeaubrey == True:

            u "Penelope, I'm really sorry, but I have to go and meet my friend. It was nice seeing you."

            scene s155
            with dissolve

            pe "Oh, I understand. I guess I'll see you around."

            scene s155a
            with dissolve

            u "Yeah, definitely. See you later."

            stop music fadeout 2.0

            jump csaub


        else:
            u "Sorry, I just had to reply to someone."

            u "Hey, do you also need a costume for Mr. Lee's class?"


            scene s155b
            with dissolve

            pe "Yeah, I was just on my way to buy one."

            scene s155c
            with dissolve

            u "Wanna go together? I need one as well."

            scene s155b
            with dissolve

            pe "I'd love that!"

            stop music fadeout 2.0

            jump cspe

    label csaub:



    # In front of chick's house

    scene s156
    with Fade (1,0,1)

    # nora opens the door

    # play knock sound

    play sound "sounds/knock.mp3"

    "*Knock knock knock*"

    play sound "sounds/dooropen.mp3"

    play music "music/m7punk.mp3"

# play dsoor open sound
    scene s157
    with dissolve

    no "Oh, look who it is."

    scene s157a # nora shouting back
    with dissolve

    no "Aubrey, your lover boy is here."

    u "Thanks, for the kind introduction."

    scene s157 # fake smile
    with dissolve

    no "You're welcome."

    play sound "sounds/dooropen.mp3"

# door open sound
    scene s157d # aubrey appears
    with dissolve

    au "Hey."

    scene s157f
    with dissolve

    u "Hey, you ready to go?"


    scene s157e
    with dissolve

    au "Yeah, I would show you the house, but we don't have that much time 'cause I've got dance practice later."

    au "Plus there's a bunch of girls in their underwear in here right now. You wouldn't wanna see that."

    scene s157f
    with dissolve

    u "Yeah, that does sound horrible."

    scene s157e
    with dissolve

    au "Haha, I thought so. Let's go then."

    stop music fadeout 2.0


    scene s158 # at the clothing store # showing aubrey and u from behind
    with Fade (1,0,1)

    u "Didn't you say this was a costume shop?"

    play music "music/mindie1.mp3"

    queue music [ "music/mindie2.mp3", "music/mindie3.mp3" ]

    au "It was! At least the last time I was here."

    scene s159 # au talking to store ev
    with dissolve

    au "Excuse me, wasn't this a costume shop?"

    scene s159a
    with dissolve

    ev "Well, we were last year, but after Halloween was over sales plummeted."

    ev "So the owners had this crazy idea of Halloween in January, but the surprising increase of in-store injuries and following lawsuits quickly made it go bust."

    ev "We had to put in a new floor and change the branding, so now we just sell regular clothing in all months of the year."

    scene s159b
    with dissolve

    au "Damn, this was the only costume store nearby..."

    scene s159c
    with dissolve

    ev "I can check if we still have some costumes in the back, but it'll be a limited selection."



    scene s159d # aubrey smiloing
    with dissolve

    au "Yeah, that'd be amazing, thank you so much."

    scene s161 # in changing rooms room
    with Fade (1,0,1)

    pause 0.5

    scene s161a # ev comming with box
    with dissolve

    ev "So in this box are all the remaining costumes we have, I hope that's enough."

    scene s161b # puts box down
    with dissolve

    ev "Let me know if there's anything else you need."

    u "Thank you."

    scene s162a # looking at aubrey
    with dissolve

    u "Okay, let's have a look at some of these."

    scene s162
    with dissolve

    au "If there's any female ones in there, I'm trying them on."

    call screen costumes # choice between 3 costumes button try and button buy below, every time you try, Aubrey comes out in a different outfit, you can peek while changing

    # chnace to flirt with ev
    # chance to get caught when risky peeking



############ VIKING AUBREY
    label try1: # viking

    if try1done == True:
        jump try1done
    else:
        $ try1done = True
        jump try1new

    label try1done:
    scene s163
    with Fade (1,0,1)

    "(Yeah- still look the same as a viking as I did before.)"

    "(I should really just choose a costume to buy.)"

    call screen costumes


    label try1new:

        $ auboutfits += 1

        scene s163 # in changing room
        with Fade (1,0,1)

        u "(Alright, rocking the Viking look.)"

        u "(I wonder what Aubrey is changing into.)"

        menu:



            "Peek":

                $ addPoint("tm", 1)
                jump bt_a

            "Don't peek":

                $ addPoint("bf", 1)
                jump bt_b


    label bt_a:

        scene s164 # Aubrey changing bad view
        with dissolve

        u "(Holy shit, if I could just stick my head through a bit further, I could get a way better view."

        menu:



            "Risk it":
                $ caughtpeekingaubrey = renpy.random.choice([True, False])

                if caughtpeekingaubrey == False:
                    jump br_aa
                else:
                    jump caughta

            "Stop peeking":

                jump br_ba

    label br_aa:
        scene s164a # Aubrey changing good view
        with dissolve

        u "(Oh my god, her ass is perfect.)"

        u "(I should stop peeking now, or I'll get caught.)"

        jump br_ada

    label bt_b:
    label br_ba:
    label br_ada:

    scene s163
    with dissolve

    u "(Let's see what Aubrey thinks of this costume.)"

    scene s165 # showing u and aubrey in costume
    with Fade (1,0,1)

    pause 0.5

    scene s166 # aubrey close up
    with dissolve

    au "Oh my god, you make an adorable Viking."

    scene s166a
    with dissolve

    u "Really? Adorable? How about hot?"

    scene s166b # flirty
    with dissolve

    au "Haha, what do you think of my outfit?"


    menu:



        "It's kinda hot.":

            $ addPoint("bf", 1)
            jump bu_a

        "It's definitely something.":

            $ addPoint("bro", 1)
            jump bu_b

    label bu_a:
        scene s166c
        with dissolve

        u "I'm not gonna lie, it's kinda hot."

        u "You could be like my Viking queen."

        scene s166b
        with dissolve

        au "I think you've put me in the wrong time period, buddy."

        if auboutfits < 3:
            scene s166
            with dissolve

            au "Let's try some of the other outfits."

        else:
            scene s166
            with dissolve

            au "Have you decided which one to buy yet?"

        call screen costumes

    label bu_b:

        scene s166c
        with dissolve

        u "I mean, it's definitely something."

        u "I'm not sure if you should replace your everyday clothes with it though."

        scene s166
        with dissolve

        if auboutfits < 3:

            au "I'll guess I'll have to try some of the other outfits then."

        else:

            au "Have you decided which one to buy yet?"

        call screen costumes
######### VIKING AUBREY

############ KNIGHT AUBREY
    label try2:

    if try2done == True:
        jump try2done
    else:
        $ try2done = True
        jump try2new

    label try2done:
    scene s167
    with Fade (1,0,1)

    "(I mean looking at the Knight costume now, I notice that...)"

    "(... it looks exactly the same as before.)"

    call screen costumes


    label try2new:

        $ auboutfits += 1

        scene s167 # in changing room
        with Fade (1,0,1)

        u "(I definitely do not fit into these shoulder pads.)"

        u "(Aubrey is changing right next to me...)"

        menu:



            "Peek":

                $ addPoint("tm", 1)
                jump bv_a

            "Don't peek":

                $ addPoint("bf", 1)
                jump bv_b


    label bv_a:

        scene s168 # Aubrey changing bad view
        with dissolve

        u "(Wow... if I could just stick my head through a bit further, I could get a way better view."

        menu:



            "Risk it":
                $ caughtpeekingaubrey = renpy.random.choice([True, False])

                if caughtpeekingaubrey == False:
                    jump bw_a
                else:
                    jump caughtb

            "Stop peeking":

                jump bw_b

    label bw_a:
        scene s168a # Aubrey changing good view
        with dissolve

        u "(Damn, what I wouldn't give to touch her ass right now.)"

        u "(I should stop peeking now, or I risk getting caught.)"

        jump bw_ad

    label bv_b:
    label bw_b:
    label bw_ad:

    scene s167
    with dissolve

    u "(Time to show this to Aubrey)"

    scene s169 # showing u and aubrey in costume
    with Fade (1,0,1)

    pause 0.5

    scene s170 # aubrey close up flirting
    with dissolve

    au "Damn, I like your outfit."

    scene s170a
    with dissolve

    u "Well thank you, milady."

    u "Yours is uhhh..."


    menu:



        "looking mighty fine.":

            $ addPoint("bf", 1)
            jump bx_a

        "certainly practical.":

            $ addPoint("bro", 1)
            jump bx_b

    label bx_a:

        u "...looking mighty fine as well."

        scene s170b # questioning
        with dissolve

        au "Is it weird that you talking like that kinda turns me on?"

        scene s170c
        with dissolve

        u "Wait really? Should I keep going?"


        scene s170d # aubrey laughing
        with dissolve

        au "Hahaha, no. I was just joking."

        if auboutfits < 3:

            au "Let's switch outfits."

        else:

            au "Are you gonna buy this one?"

        call screen costumes

    label bx_b:

        u "... certainly practical."

        scene s170d
        with dissolve

        au "That is the single greatest compliment I think I've ever received."

        scene s170e
        with dissolve

        u "I am kinda known for my charm."

        scene s170
        with dissolve

        au "Really? I thought it was for getting punched in the face."

        scene s170a
        with dissolve

        u "Wow, low blow."

        scene s170d

        if auboutfits < 3:

            au "Let's switch outfits."

        else:

            au "So are you gonna buy this one?"

        call screen costumes
######### KNIGHT AUBREY

    ### aubrey third costume

    # okay this one is literally just a bra and panties. I'm not wearing that.
    # oh come on, I wanna see! # popularity check

############ COWBOY AUBREY
    label try3:

    if try3done == True:
        jump try3done
    else:
        $ try3done = True
        jump try3new

    label try3done:
    scene s171
    with Fade (1,0,1)

    "(The more I wear this, the more I feel like I would make a great cowboy.)"

    call screen costumes


    label try3new:

        $ auboutfits += 1

        scene s171 # in changing room
        with Fade (1,0,1)

        u "(Yeehaw!)"

        u "(I can hear Aubrey sliding her clothes off...)"

        menu:



            "Peek":

                $ addPoint("tm", 1)
                jump bz_a

            "Don't peek":

                $ addPoint("bf", 1)
                jump bz_b


    label bz_a:

        scene s172 # Aubrey changing bad view
        with dissolve

        u "(Fuck... if I could just stick my head through a bit further, I could get a way better view."


        menu:

            "Risk it":

                $ caughtpeekingaubrey = renpy.random.choice([True, False])
                if caughtpeekingaubrey == False:
                    jump ca_a
                else:
                    jump caughtc

            "Stop peeking":

                jump ca_b

    label ca_a:
        scene s172a # Aubrey changing good view
        with dissolve

        u "(In all fairness, whenever I watch porn, the person getting caught spying gets to fuck the girl right afterwards.)"

        u "(Still... I better stop peeking now, it's too risky.)"

        jump ca_ad

    label bz_b:
    label ca_b:
    label ca_ad:

    scene s171
    with dissolve

    u "Man she's gonna love this costume."

    scene s199 # showing u in front of closed stall with Aubrey
    with Fade (1,0,1)

    u "Aubrey? Are you coming out?"

    au "This costume is literally just historic lingerie."


    $ influencetut = True

    au "I'm not showing you this, haha."

    menu:



        "Oh come on.":

            $ addPoint("tm", 1)
            $ influencetut = False
            jump by_a

        "Fine.":

            $ addPoint("bf", 1)
            $ influencetut = False
            jump by_b



    label by_a:

    u "Oh come on, Aubrey. I wanna see."

    if kct == "popular":

        call screen popup2
    else:

        jump by_ad

    label popup2:

    au "Okay, fine. Just for you."

    scene s175 # showing u in costume and aubrey in custome
    with Fade (1,0,1)

    pause 0.5

    scene s176a # aubrey like  I told you
    with dissolve

    u "Holy shit, you weren't exaggerating. That is revealing."

    scene s176
    with dissolve

    au "See what I mean now? Can I get dressed again?"

    scene s176a
    with dissolve

    u "You sure you don't wanna keep this on for the rest of the day?"

    scene s176b # aub laughing
    with dissolve

    au "Haha yes. I hope you got a good look, 'cause I'm changing back."

    au "Also, this cowboy outfit is probably the worst thing I've ever seen anyone wear."

    au "So let's get out of these outfits."

    call screen costumes


    label by_ad:

    au "Sorry but... I'm gonna get dressed again."


    u "Alright, fine."

    jump by_bd

    label by_b:

    u "Alright, fine."

    u "Then get dressed quickly, so that you can see my costume."

    au "Yeah, just give me a minute."

    label by_bd:
    scene s173 # showing u in costume and aubrey in regular clothes
    with Fade (1,0,1)

    pause 0.5

    scene s174 # aubrey close up laughing
    with dissolve

    au "Oh god, that looks so bad on you."

    scene s174a
    with dissolve

    u "What?? I considered cowboy to be a serious career path for me after I saw myself in this outfit."

    scene s174
    with dissolve

    au "Oh no. Just whatever you do, do not buy this costume."

    au "I think you should get out of that as quickly as you can."

    call screen costumes

######### COWBOY AUBREY



    label surebuy1:
        call screen surebuy1

    label surebuy2:
        call screen surebuy2

    label surebuy3:
        call screen surebuy3

    label surebuy1p:
        call screen surebuy1p

    label surebuy2p:
        call screen surebuy2p

    label surebuy3p:
        call screen surebuy3p






######################SHOPPING WITH PENELOPE shop2

    label cspe:



    scene s158v2
    with Fade (1,0,1)

    u "I swear Google maps said this was a costume shop."

    play music "music/mindie1.mp3"

    queue music [ "music/mindie2.mp3", "music/mindie3.mp3" ]

    pe "Maybe we can ask the lady over there, she seems to work here."

    scene s159v2
    with dissolve

    pe "Excuse me, is this not a costume shop?"

    scene s159a
    with dissolve

    ev "Well, we were last year, but after Halloween was over sales plummeted."

    ev "So the owners had this crazy idea of Halloween in January, but the surprising increase of in-store injuries and following lawsuits quickly made it go bust."

    ev "We had to put in a new floor and change the branding, so now we just sell regular clothing in all months of the year."

    scene s159bv2
    with dissolve

    pe "Oh, wow, well that's very unfortunate. We were looking to buy some costumes."

    scene s159c
    with dissolve

    ev "If you want, I can check if we still have some in the back, but it'll be a limited selection."


    scene s159dv2
    with dissolve

    pe "Yes, that would be amazing. We'd really appreciate it, thank you."



    scene s161v2 # in changing rooms room
    with Fade (1,0,1)

    pause 0.5

    scene s161av2 # ev comming with box
    with dissolve

    ev "So in this box are all the remaining costumes we have, I hope that's enough."

    scene s161b # puts box down
    with dissolve

    ev "Let me know if there's anything else you need."

    u "Thank you."

    scene s162av2
    with dissolve

    u "Okay, let's have a look at some of these."

    scene s162v2
    with dissolve

    pe "I'm actually really excited to buy a costume."
    pe "At my old college we weren't even allowed to wear costumes on Halloween, because of the dress code."


    call screen costumes # choice between 3 costumes button try and button buy below, every time you try, Aubrey comes out in a different outfit, you can peek while changing

    # chnace to flirt with ev
    # chance to get caught when risky peeking



############ VIKING PENELOPE shop3
    label try1p: # viking

    if try4done == True:
        jump try4done
    else:
        $ try4done = True
        jump try4new

    label try4done:
    scene s163
    with Fade (1,0,1)

    "(Yeah- still look the same as a Viking as I did before.)"

    "(I should really just choose a costume to buy.)"

    call screen costumes


    label try4new:

        $ penoutfits += 1

        scene s163 # in changing room
        with Fade (1,0,1)

        u "(Alright, rocking the Viking look.)"

        u "(I wonder what Penelope is changing in to.)"

        menu:



            "Peek":

                $ addPoint("tm", 1)
                jump cc_a

            "Don't peek":

                $ addPoint("bf", 1)
                jump cc_b


    label cc_a:

        scene s183 # penelope changing bad view
        with dissolve

        u "(Holy shit, if I could just stick my head through a bit further, I could get a way better view.)"

        menu:



            "Risk it":

                $ caughtpeekingpenelope = renpy.random.choice([True, False])
                if caughtpeekingpenelope == False:
                    jump cd_a
                else:
                    jump caughtd

            "Stop peeking":

                jump cd_b

    label cd_a:
        scene s183a # pen changing good view
        with dissolve

        u "(Oh my god, her ass is so nice.)"

        u "(I should stop peeking now, or I'll get caught.)"

        jump cd_ad

    label cc_b:
    label cd_b:
    label cd_ad:

    scene s163
    with dissolve

    u "(Let's see what Penelope thinks of this costume.)"

    scene s179far # showing u and pen in costume
    with Fade (1,0,1)

    pause 0.5

    scene s179 # pen close up
    with dissolve

    pe "Oh I don't think you should get that costume."

    scene s179a
    with dissolve

    u "Why? Do I look too dashing?"

    scene s179
    with dissolve

    pe "No, it's just that Vikings didn't actually have horns on their helmets."

    pe "And Mr. Lee said that the costumes should be historically accurate."

    scene s179a
    with dissolve

    u "Oh, right. Totally."

    scene s179
    with dissolve
    pe "So uhm... what do you think of my outfit?"


    menu:


        "You look beautiful.":

            $ addPoint("bf", 1)
            jump ce_a

        "I guess it's nice":

            $ addPoint("bro", 1)
            jump ce_b

    label ce_a:
        scene s179a
        with dissolve

        u "You look beautiful. Do you like it?"

        scene s179b # romantic smile
        with dissolve

        pe "Awww, thank you."

        pe "Yeah, it's kinda cool."

        if penoutfits < 3:

            pe "Should we try some other outfits?"

        else:


            pe "Are you ready to buy an outfit?"

        call screen costumes

    label ce_b:
        scene s179a
        with dissolve

        u "I guess it's kinda nice. What do you think"

        scene s179b # romantic smile
        with dissolve

        pe "I like it, but I'm not sure."

        if penoutfits < 3:

            pe "Should we try some other outfits?"

        else:


            pe "Are you ready to buy an outfit?"

        call screen costumes


######### VIKING PEN

############ KNIGHT PEN shop4
    label try2p:

    if try5done == True:
        jump try5done
    else:
        $ try5done = True
        jump try5new

    label try5done:
    scene s167
    with Fade (1,0,1)

    "(I mean looking at the Knight costume now, I notice that...)"

    "(... it looks exactly the same as before.)"

    call screen costumes


    label try5new:

        $ penoutfits += 1

        scene s167 # in changing room
        with Fade (1,0,1)

        u "(I definitely do not fit into these shoulder pads.)"

        u "(Penelope is changing right next to me...)"


        menu:



            "Peek":

                $ addPoint("tm", 1)
                jump cf_a

            "Don't peek":

                $ addPoint("bf", 1)
                jump cf_b


    label cf_a:

        scene s183 # pen changing bad view
        with dissolve

        u "(Wow... if I could just stick my head through a bit further, I could get a way better view."


        menu:



            "Risk it":

                $ caughtpeekingpenelope = renpy.random.choice([True, False])
                if caughtpeekingpenelope == False:
                    jump cg_a
                else:
                    jump caughte

            "Stop peeking":

                jump cg_b

    label cg_a:
        scene s183a
        with dissolve

        u "(Damn, what I wouldn't give to touch her ass right now.)"

        u "(I should stop peeking now, or I risk getting caught.)"

        jump cg_ad

    label cf_b:
    label cg_b:
    label cg_ad:

    scene s167
    with dissolve

    u "(Time to show this to Penelope)"

    scene s181 # showing u and penelope in costume
    with Fade (1,0,1)

    pause 0.5

    scene s182 # pen happy
    with dissolve

    pe "Oh, you're a knight!"

    scene s182a
    with dissolve

    u "Yeah and you're like a female with shoulder pads?"

    scene s182
    with dissolve

    pe "Sir, your perception skills are outstanding."

    scene s182a
    with dissolve

    u "Well thank you, milady."

    scene s182
    with dissolve

    pe "You know, our costumes fit quite well together."


    menu:


        "Flirt":

            $ addPoint("bf", 1)
            jump ch_a

        "Agree":

            $ addPoint("bro", 1)
            jump ch_b

    label ch_a:

        u "Yeah, maybe it's like the costume of two lovers, you know... historically speaking."

        scene s182
        with dissolve

        pe "Haha, I'm sure that's the case."

        if penoutfits < 3:

            pe "Let's continue, I wanna try another outfit."

        else:

            pe "Are you ready to buy an outfit?"

        call screen costumes

    label ch_b:

        u "Yeah, it would be a cool partner costume."

        scene s182
        with dissolve

        pe "That's a sweet idea. Maybe we can do something like that."

        if penoutfits < 3:

            pe "But let's check out the other outfits first."

        else:

            pe "Would you be ready to buy an outfit?"

        call screen costumes
######### KNIGHT PEN

    ### aubrey third costume

    # okay this one is literally just a bra and panties. I'm not wearing that.
    # oh come on, I wanna see! # popularity check

############ COWBOY PEN shop5
    label try3p:

    if try6done == True:
        jump try6done
    else:
        $ try6done = True
        jump try6new

    label try6done:
    scene s171
    with Fade (1,0,1)

    "(The more I wear this, the more I feel like I would make a great cowboy.)"

    call screen costumes


    label try6new:

        $ penoutfits += 1

        scene s171 # in changing room
        with Fade (1,0,1)

        u "(Yeehaw!)"

        u "(I can hear Penelope sliding her clothes off...)"


        menu:



            "Peek":

                $ addPoint("tm", 1)
                jump cj_a

            "Don't peek":

                $ addPoint("bf", 1)
                jump cj_b


    label cj_a:

        scene s180 # pen changing bad view
        with dissolve

        u "(Fuck... if I could just stick my head through a bit further, I could get a way better view."


        menu:



            "Risk it":

                $ caughtpeekingpenelope = renpy.random.choice([True, False])
                if caughtpeekingpenelope == False:
                    jump ck_a
                else:
                    jump caughtf

            "Stop peeking":

                jump ck_b

    label ck_a:
        scene s180a # pen changing good view
        with dissolve

        u "(In all fairness, whenever I watch porn, the person getting caught spying gets to fuck the girl right afterwards.)"

        u "(Still... I better stop peeking now, it's too risky.)"

        jump ck_ad

    label cj_b:
    label ck_b:
    label ck_ad:


    scene s171
    with dissolve

    u "Man she's gonna love this costume."

    scene s199
    with Fade (1,0,1)

    u "Penelope? Are you coming out?"

    pe "Well I was trying on a costume, but after seeing I realize that it shows way too much skin to wear it to class."

    u "Can I see?"

    pe "No, haha. Sorry."


    menu:


        "Oh come on.":

            $ addPoint("tm", 1)
            jump cl_a

        "Fine.":

            $ addPoint("bf", 1)
            jump cl_b



    label cl_a:

    u "Oh come on, Penelope. I wanna see."


    pe "Sorry but... I'm gonna get dressed again."


    u "Alright, fine."

    jump cl_ad

    label cl_b:


    u "Okay, fine."

    u "Then get dressed quickly, so that you can see my costume."

    pe "Yeah, just give me a minute."

    label cl_ad:
    scene s184 # showing u in costume and aubrey in regular clothes
    with Fade (1,0,1)

    pause 0.5

    scene s185 # pe close up laughing
    with dissolve

    pe "Wow, I'm not sure how I feel about the cowboy look."

    scene s185a
    with dissolve

    u "What?? I considered cowboy to be a serious career path for me after I saw myself in this outfit."

    scene s185a
    with dissolve

    pe "Yeah... you should probably rethink that, haha."

    if penoutfits < 3:

        pe "Let's check out something different."

    else:

        pe "Are you ready to buy an outfit?"

    call screen costumes

######### COWBOY PEN shop6


    ##### Aubrey caught peeking:

    label caughta:

        scene s164a # Aubrey changing good view
        with dissolve

        u "(Oh my god, her ass is perfect.)"

        u "(I should stop peeking now, or I'll get caught.)"

        scene s163
        with dissolve

        jump caughtaa
    label caughtb:

        scene s168a # Aubrey changing good view
        with dissolve

        u "(Damn, what I wouldn't give to touch her ass right now.)"

        u "(I should stop peeking now, or I risk getting caught.)"

        scene s167
        with dissolve

        jump caughtba

    label caughtc:


        scene s172a # Aubrey changing good view
        with dissolve

        u "(In all fairness, whenever I watch porn, the person getting caught spying gets to fuck the girl right afterwards.)"

        u "(Still... I better stop peeking now, it's too risky.)"

        scene s171
        with dissolve

        jump caughtca

    label caughtaa:
    label caughtba:
    label caughtca:



    au "[name], did I just see you pull your head out from underneath the dividers?"

    scene s177d # closeup aubrey outside in regular clothes angry
    with Fade (1,0,1)

    au "[name]? Did you just peek on me?"



    menu:

        "Apologize":

            $ addPoint("bf", 1)
            jump cb_a

        "Deny it":

            $ addPoint("tm", 1)
            jump cb_b

    label cb_a:

    $ caughtpeekingaubreycounter = True

    scene s177e
    with dissolve

    u "Aubrey, I'm so sorry. It was just..."

    u "...so tempting."

    scene s177d # aubrey disappointed
    with dissolve

    au "Honestly, it's okay. It was just kinda surprising."

    au "How about we just buy a costume and get going?"

    call screen costumes

    label cb_b:

    scene s177e
    with dissolve

    u "What are you talking about? You probably just saw my foot."

    if kct == "confident":

        call screen popup3

        label popup3:

        $ caughtpeekingaubreycounter = True

        scene s177d # aub embarassed
        with dissolve

        au "Wait really?"

        au "Ooops, I guess never mind, let's just buy a costume."

        scene s177e
        with dissolve

        u "Yeah, it's fine. I'll pick one."

        call screen costumes

    else:

        scene s177b # aubrey disappointed
        with dissolve

        au "Yeah, right."

        au "Honestly, I didn't even mind, but why would you lie about it, that's messed up."

        au "I'm gonna leave, I guess I'll see you around."

        scene s177c # empty
        with fade

        u "(Fuck, I shouldn't have lied to her.)"

        u "(And I still need to buy a costume...)"

        call screen costumes


    ##### Penelope caught peeking: shop7


    label caughtd:

        scene s180a # pen changing good view
        with dissolve

        u "(Oh my god, her ass is so nice.)"

        u "(I should stop peeking now, or I'll get caught.)"

        scene s163
        with dissolve


        jump caughtda
    label caughte:

        scene s183a
        with dissolve

        u "(Damn, what I wouldn't give to touch her ass right now.)"

        u "(I should stop peeking now, or I risk getting caught.)"

        scene s167
        with dissolve

        jump caughtea

    label caughtf:

        scene s180a # pen changing good view
        with dissolve

        u "(In all fairness, whenever I watch porn, the person getting caught spying gets to fuck the girl right afterwards.)"

        u "(Still... I better stop peeking now, it's too risky.)"

        scene s171
        with dissolve

        jump caughtfa

    label caughtda:
    label caughtea:
    label caughtfa:


    pe "Oh my god! [name], did I just see you pull your head out from underneath the dividers??"

    pe "Did you spy on me??"

    scene s186 # closeup pen outside in regular clothes upset
    with Fade (1,0,1)

    $ influencetut = True
    pe "[name]! What were you thinking?!"

    menu:


        "Apologize":

            $ addPoint("bf", 1)
            $ influencetut = False
            jump cn_a

        "Deny it":

            $ addPoint("tm", 1)
            $ influencetut = False
            jump cn_b

    label cn_a:

    scene s186a
    with dissolve

    u "Penelope, I'm so sorry. It was just..."

    u "...so tempting."

    scene s186b # penelope sad
    with dissolve

    pe "I don't know how to deal with this right now."

    pe "I'm gonna leave, goodbye."

    scene s177c # empty
    with dissolve

    u "(Fuck, I shouldn't have risked it.)"

    u "(And I still need to buy a costume...)"

    call screen costumes

    label cn_b:

    scene s186
    with dissolve

    u "What are you talking about? You probably just saw my foot."

    if kct == "confident":

        call screen popup4

        label popup4:

        $ caughtpeekingpenelopecounter = True

        scene s186d # pen embarassed
        with dissolve

        pe "Wait really?"

        pe "I'm so sorry, I just... I just thought-"

        pe "Let's just both buy a costume and get out of here."

        scene s186e
        with dissolve

        u "Yeah, it's fine. I'll pick one."

        call screen costumes

    else:

        scene s186b
        with dissolve

        pe "[name], I know what I saw."

        pe "Why can't you just admit it?"

        pe "I don't know how to deal with this right now. Goodbye."

        scene s177c # empty
        with fade

        u "(Fuck, I shouldn't have risked it.)"

        u "(And I still need to buy a costume...)"

        call screen costumes


    label gocostumes1:
    label gocostumes2:
    label gocostumes3:
    label gocostumes4:
    label gocostumes5:
    label gocostumes6:

    call screen costumes


    ### purchase with Aubrey

    label buy1:
        $ costume = 1
        jump buy1a
    label buy2:
        $ costume = 2
        jump buy2a
    label buy3:
        $ costume = 3
        jump buy3a

    label buy1a:
    label buy2a:
    label buy3a:

        if caughtpeekingaubrey == True:
            jump eve1

        else:
            scene s189  # at checkout with aubrey
            with Fade (1,0,1)

            u "I'll take this one, please."

            u "Pay by card."

            scene s188 # close up eve looking at cash register
            with dissolve

            ev "Well I'm glad you guys found something."

            scene s188a # close up eve head turn
            with dissolve

            u "Thanks again so much for helping us out."

            scene s188b
            with dissolve

            ev "Yeah, it's no worry."

            scene s188c #presents bag
            with dissolve

            ev "Alright, here you go."

            scene s188d
            with dissolve

            u "Thank you, have a nice day."

            scene s188b # eve smiling
            with dissolve

            ev "You too."

            scene s194 # walking home with aubrey
            with Fade (1,0,1)

            au "I had a really great time today."

            scene s195 # closeup
            with dissolve

            au "But I wouldn't mind doing something different than costume shopping next time."

            scene s195a
            with dissolve

            u "Haha, I'm sure we'll find something fun to do."

            u "I gotta go right here, so I'll see you later, okay?"

            scene s195
            with dissolve

            au "Yeah, goodbye [name]."

            jump endshopb

    label buy1p:
        $ costume = 1
        jump buy1pa
    label buy2p:
        $ costume = 2
        jump buy2pa
    label buy3p:
        $ costume = 3
        jump buy3pa

    label buy1pa:
    label buy2pa:
    label buy3pa:

        if caughtpeekingpenelope == True:
            jump eve1

        else:
            scene s190 # at check out, pen looking at you
            with Fade (1,0,1)

            pe "Hey, sorry to ask this, but could you lend me the money for this? My dad just sent me a text that he froze my card."

            scene s190a
            with dissolve

            u "Oh shit. Yeah, of course."

            u "I'll take these two, please."

            u "Pay by card."

            scene s188 # close up eve looking at cash register
            with dissolve

            ev "Well I'm glad you guys found something."

            scene s188a # close up eve head turn
            with dissolve

            u "Thanks again so much for helping us out."

            scene s188b
            with dissolve

            ev "Yeah, it's no worry."

            scene s188c #presents bag
            with dissolve

            ev "Alright, here you go."

            scene s188d
            with dissolve

            u "Thank you, have a nice day."

            scene s188b # eve smiling
            with dissolve

            ev "You too."

            scene s192 # walking home with evelyn
            with Fade (1,0,1)

            pe "Thanks for paying for me."

            scene s193 # closeup
            with dissolve

            pe "If you give me your number, I can let you know as soon as I have the money to pay you back."

            scene s193a
            with dissolve

            u "Yeah sounds, good."

            u "I gotta go right here, so I'll see you later, okay?"

            scene s193
            with dissolve

            pe "Okay, bye [name]."

            jump endshopb

    label eve1:
    label eve2:

    scene s187  # you alone at checkout
    with Fade (1,0,1)

    u "I'll take this one, please."

    u "Pay by card."

    scene s188 # close up eve looking at cash register
    with dissolve

    ev "Well I'm glad you found something."

    scene s188a # close up eve head turn
    with dissolve

    ev "Even though you seem to have a lost a person on the way."

    scene s188b
    with dissolve

    u "Yeah, she had to get home."

    scene s188c #presents bag
    with dissolve

    ev "Alright, here you go."



    menu:

        "Make a move.":
            $ evelynmove = True
            $ addPoint("bro", 1)
            jump co_a

        "Leave":

            $ addPoint("bf", 1)
            jump co_b

    label co_b:

    scene s188d
    with dissolve

    u "Thank you, have a nice day."

    scene s188b # eve smiling
    with dissolve

    ev "You too."

    jump co_bd

    label co_a:

    scene s188d
    with dissolve

    u "Thanks."

    u "Hey, is there any chance I could get your number?"

    scene s188b
    with dissolve

    ev "I'm very flattered, but I'm 25 and you seem a bit too young for me."

    scene s188d
    with dissolve

    u "Give me one date to change your mind."

    u "Come on, it'll be fun."

    ev "Give me one good reason to give you a chance."

    scene s188g
    with dissolve

    menu:

        "Be smart":
            $ evelynnumber = True
            $ contact_Evelyn.unlock()
            jump evelyna

        "Be funny":

            $ evelynnumber = False
            jump evelynb


    label evelynb:

    scene s188h
    with dissolve

    u "How about I'll wear the costume I bought yesterday for our entire date?"

    scene s188b
    with dissolve

    ev "Look, it's very cute that you'd do that for me, but I just don't think we'd be a great fit."

    ev "I'm sure you'll find someone else."

    scene s188d
    with dissolve

    u "Oh okay... I guess I'll see you around."

    u "(Damn, that didn't go as planned...)"

    jump evelynbd

    label evelyna:

    scene s188h
    with dissolve

    u "Look, I don't know and you don't know me. I'm [name] and I'm just looking for someone to have a good time with."

    u "It's not gonna be the most exciting night of your life, and it's not gonna be a boring night at home playing jenga with the girls."

    u "What this night will do, is serve as a benchmark for future dates with me."

    u "What do you say?"

    scene s188g
    with dissolve

    ev "Damn, that was convincing. Okay, I'm in."

    ev "I'll give you my number, but you better bring your A-game."

    scene s188h
    with dissolve

    u "Don't worry, you won't be disappointed."

    scene s188b
    with dissolve

    ev "Well, I'm looking forward to it."

    scene s188d
    with dissolve

    u "Great, I'll let you know."

    u "(I'm getting really good at this flirting thing...)"

    jump co_ad

    label evelynbd:
    label co_ad:
    label co_bd:
    label endshopa:
    label endshopb:

    stop music fadeout 2.0

    scene s196
    with Fade (1,0,1)

    u "(The Wolves? What are they doing here?)"

    scene s197 # aaron pointing at you
    with dissolve

    aa "Hey, you're the guy that got punched by Grayson!"

    scene s197c
    with dissolve

    u "Really? Is that what I'm gonna be known for from now on?"

    scene s197b
    with dissolve

    ch "It doesn't have to be."

    ch "Look, Grayson's an asshole. If you wanna get back at him, you should pledge the Wolves."

    ch "If you're the right fit, you'll become one of us and trust me, next year a Wolf is gonna beat the shit out of Grayson and take the fucking crown."

    scene s197c
    with dissolve

    u "Uhm..."

    scene s197b
    with dissolve

    ch "Just think about it."

    scene s197d # walking away
    with dissolve

    u "(Hmmm...)"

    scene s198 # zoom on poster
    with dissolve

    u "(The Wolves... huh.)"



############## END OF V 0.2



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

    $ contact_Chloe.unlock()

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
            $ notcool = False
            jump cm_a

        "That's not cool.":

            $ addPoint("bf", 1)
            $ notcool = True
            jump cm_b



    label cm_a:
        scene s206c
        with dissolve

        u "Hahaha, man you're crazy."

        jump cm_ad

    label cm_b:
        scene s206c
        with dissolve

        u "Dude, that's not cool. You're invading their privacy."

        jump cm_ad



    label cm_ad:
    label cm_bd:


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
            jump cp_a

        "She's alright.":

            jump cp_b

    label cp_a:

        scene s208a
        with dissolve

        u "Oh, hell yeah! She's super hot."

        scene s208b # cheeky smile
        with dissolve

        imre "Well that's what I like to hear, go on."

        jump cp_ad

    label cp_b:

        scene s208a
        with dissolve

        u "She's alright I guess."

        scene s208b
        with dissolve

        imre "Well that usually means she's better in bed 'cause she tries harder, go on."


        jump cp_bd


    label cp_ad:
    label cp_bd:


    if costumeaubrey == True:

        scene s208c
        with dissolve

        u "Anyways, then I went costume shopping for Mr. Lee's class with Aubrey."

        scene s208d
        with dissolve # Imre pointer ifnger up and mouth open

        u "And before you ask, yes, she's hot."

        if caughtpeekingaubrey == True:

            scene s208a
            with dissolve

            u "And then I might have gotten caught peeking on her while changing..."

            if notcool == True:

                scene s208b
                with dissolve

                imre "So much for invasion of privacy, huh?"

                scene s208c
                with dissolve

                jump cona

            else:

                scene s208
                with dissolve

                imre "The key is not to get caught, son."

                scene s208a
                with dissolve

                jump conb

            label cona:
            label conb:

            if evelynnumber == True:

                u "But then I got the cute shop clerk's number. So it turned out to be a blessing in disguise."

                jump conc

            else:

                jump cond


        else:

            scene s208b
            with dissolve

            imre "Nnnice."

            jump cone



    else:

        scene s208c
        with dissolve

        u "Anyways, then I went costume shopping for Mr. Lee's class with her."

        if caughtpeekingpenelope == True:

            u "And we were having a great time..."

            scene s208a
            with dissolve

            u "But... then I might have gotten caught peeking on her while changing."

            if notcool == True:

                scene s208b
                with dissolve

                imre "So much for invasion of privacy, huh?"

                scene s208c
                with dissolve

                jump conf

            else:

                scene s208
                with dissolve

                imre "The key is not to get caught, son."

                scene s208a
                with dissolve

                jump cong

            label conf:
            label cong:

            if evelynnumber == True:

                u "But then I got the cute shop clerk's number. So it turned out to be a blessing in disguise."

                jump conh

            else:

                jump conj


        else:

            u "And we had a great time."

            scene s208
            with dissolve

            imre "That sounds great, man."

            jump conk




    label conc:
    label cone:
    label conh:
    label conk:

    scene s208a
    with dissolve

    u "But that's not even the best part..."

    jump conl


    label conj:
    label cond:

    scene s208a
    with dissolve

    u "But now comes the good part..."

    jump conm

    label conl:
    label conm:

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

    ########




    u "(Okay, It's 11:50 pm. Time to go to the gym to meet Chloe.)"

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
            jump cq_a

        "Don't question it":

            $ addPoint("bf", 1)
            jump cq_b

    label cq_a:

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

    label cq_b:

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
            jump cr_a

        "Let her win":

            $ addPoint("bf", 1)
            jump cr_b


    label cr_a:

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

    jump cr_ad

    label cr_b:

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

    jump cr_bd

    label cr_ad:
    label cr_bd:


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

    $ fantasy = True

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

    image glitch = ("images/glitch.png")

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

    $ fantasy = False


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
            jump cw_a

        "Stick to what you know":

            jump cw_b

    label cw_a:

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

    label cw_b:

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

    if evelynmove == False:

        scene s243 # evelyn working out
        with dissolve

        u "(Isn't that the cute store clerk from the costume shop?)"

        menu:


            "Approach her":

                $ addPoint("bro", 1)
                jump cx_a

            "Leave it":

                $ addPoint("bf", 1)
                jump cx_b


        label cx_a:



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
                $ contact_Evelyn.unlock()
                jump evea

            "Be funny":

                $ evelynnumber = False
                jump eveb


        label eveb:

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

        jump evebd

        label evea:

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

        jump cx_ad

    else:
        label evebd:
        label cx_b:
        label cx_ad:


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


    $ msgnot = 1
    $ aubmsgnot = 1
    $ aubisreply = 1
    $ showphone = True

    play sound "sounds/vibrate.mp3"


    if costumeaubrey == True: # did you meet aubrey?

        if caughtpeekingaubrey == True: # did she catch you?

            if caughtpeekingaubreycounter == True: # did you talk your way out?
                jump talkedout

            else: # caught and she's mad

            # 1
                $ aubmsg = 11
                $ contact_Aubrey.newMessage(aubreyMessage11)
                $ contact_Aubrey.newMessage(aubreyMessage12)
                $ aubmsg11 = "I wanna talk about what happened yesterday."
                $ aubmsg12 = "Any chance that you could come over now?"
                $ aubrep12a = "Yeah, I can."
                $ aubmsg13 = "My room has a window facing the backyard. Can you climb in through there? I'll leave it open."
                $ aubmsg14 = "I'd prefer if none of the girls saw you."
                $ aubrep14a = "Uhm... sure."
                $ phoneexit = "phones"

                " "

                label repeatk:
                label phones:

                if not aubreyMessage14.reply and not aubreyMessage14a.reply and not aubreyMessage14b.reply:

                    if not msgApp.notification:

                        u "(I should really reply to Aubrey.)"

                    else:

                        u "(I should probably check my phone.)"



                    jump repeatk

                else:

                    $ showphone = False

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
                            jump cy_a

                        "Refuse":

                            $ addPoint("tm", 1)
                            jump cy_b

            label cy_b:

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

            jump continuek

            label cy_a:

            scene s256b #showing you pulling down your pants
            with dissolve

            u "You want me to take my clothes off? Fine, I'll do it."

            scene s256b2
            with dissolve

            au "Good! Do it."

            scene s256a #you no pants
            with fade

            pause 0.5

            jump continuej


        else: # not caught peeking but met
            label talkedout:

            $ aubmsg = 11
            $ contact_Aubrey.newMessage(aubreyMessage11a)
            $ contact_Aubrey.newMessage(aubreyMessage12a)
            $ aubmsg11a = "Hey, I really need your help."
            $ aubmsg12a = "Any chance that you could come over now?"
            $ aubrep12aa = "Yeah, I'll be right there.."
            $ aubmsg13a = "My room has a window facing the backyard. Can you climb in through there instead of using the front door?"
            $ aubmsg14a = "I'll leave it open."
            $ aubrep14aa = "Uhm... sure."
            $ phoneexit = "phonet"

            " "

            label repeatl:
            label phonet:

            if not aubreyMessage14.reply and not aubreyMessage14a.reply and not aubreyMessage14b.reply:

                if not msgApp.notification:

                    u "(I should really reply to Aubrey.)"

                else:

                    u "(I should probably check my phone.)"



                jump repeatl

            else:

                $ showphone = False

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


                jump continuel




    else: # you didn't meet aubrey
        $ contact_Aubrey.newMessage(aubreyMessage11b)
        $ contact_Aubrey.newMessage(aubreyMessage12b)
        $ aubmsg = 11
        $ aubmsg11 = "Hey, you know how you had to cancel on me yesterday and you really want to make it up to me?"
        $ aubmsg12 = "Wanna come over now?"
        $ aubrep12a = "Uhh... okay."
        $ aubmsg13 = "My room has a window facing the backyard. Can you climb in through there instead of using the front door?"
        $ aubmsg14 = "I'll leave it open."
        $ aubrep14a = "Uhm... sure."
        $ phoneexit = "phoneu"

        " "

        label repeatm:
        label phoneu:

        if not aubreyMessage14.reply and not aubreyMessage14a.reply and not aubreyMessage14b.reply:

            if not msgApp.notification:

                u "(I should really reply to Aubrey.)"

            else:

                u "(I should probably check my phone.)"



            jump repeatm

        else:
            $ showphone = False

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

            jump continuem


    label continuek:
    label continuej:
    label continuel:
    label continuem:


    label gc:
    $ _game_menu_screen = "ingmenu"


    image aub1 = Movie (play="images/aub1.webm", loop = False, image = "images/aub1.jpg", start_image = "images/aub1start.jpg")
    image aub2 = Movie (play="images/aub2.webm", loop = True, image = "images/aub2.jpg", start_image = "images/aub1.jpg")
    image aub3 = Movie (play="images/aub3.webm", loop = False, image = "images/aub3.jpg", start_image = "images/aub3start.jpg")
    image aub4 = Movie (play="images/aub4.webm", loop = True, image = "images/aub4.jpg", start_image = "images/aub4start.jpg")
    image aub5 = Movie (play="images/aub5.webm", loop = False, image = "images/aub5.jpg", start_image = "images/aub5start.jpg")
    image aub7 = Movie (play="images/aub7.webm", loop = True, image = "images/aub7.jpg", start_image = "images/aub7start.jpg")
    image aub8 = Movie (play="images/aub8.webm", loop = False, image = "images/aub8.jpg", start_image = "images/aub8start.jpg")
    image asexnew1 = Movie (play="images/asexnew1.webm", loop = True, image = "images/asexnew1end.jpg", start_image = "images/asexnew1start.jpg")
    image asexnew2 = Movie (play="images/asexnew2.webm", loop = True, image = "images/asexnew2end.jpg", start_image = "images/asexnew2start.jpg")
    image asexnew3 = Movie (play="images/asexnew3.webm", loop = True, image = "images/asexnew3end.jpg", start_image = "images/asexnew3start.jpg")
    image asexnew4 = Movie (play="images/asexnew4.webm", loop = True, image = "images/asexnew4end.jpg", start_image = "images/asexnew4start.jpg")
    image asexnew5 = Movie (play="images/asexnew5.webm", loop = True, image = "images/asexnew5end.jpg", start_image = "images/asexnew5start.jpg")
    image asexnew6 = Movie (play="images/asexnew6.webm", loop = True, image = "images/asexnew4end.jpg", start_image = "images/asexnew4start.jpg")
    image asexnew7 = Movie (play="images/asexnew7.webm", loop = True, image = "images/asexnew5end.jpg", start_image = "images/asexnew5start.jpg")
    image asexnew9 = Movie (play="images/asexnew9.webm", loop = True, image = "images/asexnew8end.jpg", start_image = "images/asexnew8start.jpg")
    image asexnew10 = Movie (play="images/asexnew10.webm", loop = True, image = "images/asexnew8end.jpg", start_image = "images/asexnew8start.jpg")
    image asexnew11 = Movie (play="images/asexnew11.webm", loop = True, image = "images/asexnew11end.jpg", start_image = "images/asexnew11start.jpg")
    image asexnew12 = Movie (play="images/asexnew12.webm", loop = True, image = "images/asexnew11end.jpg", start_image = "images/asexnew11start.jpg")
    image asexnew13 = Movie (play="images/asexnew13.webm", loop = False, image = "images/asexnew13end.jpg", start_image = "images/asexnew13start.jpg")

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
        if steam == False:
            image notnowmom = "images/notnowmom.png"
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

    image rikiss2 = Movie (play="images/rikiss.webm", loop = False, image = "images/rikiss.jpg", start_image = "images/rikiss.jpg")

    show rikiss2

    $ lipsdontlie = True
    if steam == False:
        image lipsdontlie = "images/lipsdontlie.png"
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
            if steam == False:
                image truthhurts = "images/truthhurts.png"
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

    $ fantasy = True

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

    $ fantasy = False

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

        image s316 = "images/s316.png" # Julia looking forward talking smiling
        image s316a = "images/s316a.png" # Julia looking forward talking smiling mouth closed
        image s316c = "images/s316c.png" # Julia looking forward curious
        image s316d = "images/s316d.png" # Julia looking forward curious mouth closed
        image s316b = "images/s316b.png" # Julia looking at you smiling mouth open






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
        if steam == False:
            image relightthefire = "images/relightthefire.png"
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
            if steam == False:
                image rematch = "images/rematch.png"
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
    $ contact_Chloe.unlock()
    $ contact_Chloe.newMessage(chloeMessage1)
    $ msgnot = 1
    $ showphone = True
    $ clmsg = 1
    $ clisreply = 1
    $ clrep1a = "Hey Chloe"
    $ clrep2a = "Any chance you can meet up in a bit?"
    $ clmsg3 = "I'm really busy today, but I could do tonight after 11 or so."
    $ clrep3a = "Alright, cool. I'll be at yours for 11"
    $ clmsg4 = "Sounds good :)"
    $ phoneexit = "phonev"

    play music "music/mindie4.mp3"
    call screen messager(contact_Chloe)
    label phonev:

    if not chloeMessage3.reply:
        $ showphone = True
        u "(I should message Chloe about meeting up later.)"

        jump phonev

    else:
        $ showphone = False
        jump continuey

    label continuey:
    $ showphone = False
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

                u "You mean since you rescued me from Cameron?."

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

    u "Ryan, can we talk about yesterday?."

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
                if steam == False:
                    image keeneye = "images/keeneye.png"
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

        pe "Well, me too!. Wanna sit down?"

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



    $ msgnot = 1
    $ jomsgnot = 1
    $ joisreply = 1
    $ showphone = True
    $ contact_Josh.newMessage(joshMessage8)
    $ jomsg = 8
    $ jomsg8 = "Hey man, you wanna hang out with me and some friends tonight?"
    $ jorep8a = "Uhh, sure."
    $ jorep8b = "I'm meeting a friend at 11, so I can't really."
    $ jomsg9 = "Dope"
    $ jomsg10 = "Come by 995 Sereno Drive at 8, it's my friends house."
    $ jomsg11 = "Aww, come on. You'll be back by 11."
    $ jomsg12 = "I told my friend Amber about you and she really wants to meet you."
    $ jorep12a = "Alright, I'll come."
    $ jorep12b = "Josh, I don't know, man. I don't wanna be late."
    $ jomsg13 = "Remember how you told me in high school that you felt like you always missed out on all the crazy stories?"
    $ jomsg14 = "Don't miss out now."
    $ jorep14a = "Fine, I'll come. But I need to go before 11."
    $ jorep14b = "I can't, sorry."
    $ jomsg15 = "This guy"
    $ phoneexit = "phonew"
    " "
    label phonew:

    if not joshMessage8.reply:

        u "(I should probably reply to my messages.)"

        jump phonew

    else:

        if joshMessage14.reply == "I can't, sorry.":

            u "(Fucking hell, I forgot how persistent Josh could be...)"
            $ showphone = False
            jump jorepb

        else:

            u "(Okay, I need to make sure that I don't forget about meeting Chloe.)"
            $ showphone = False
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

    if joshMessage12.reply:

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

    u "(Alright, time for an new day.)"
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
    $ showphone = True
    $ msgnot = 1
    $ ammsgnot = 1
    $ contact_Amber.unlock()
    $ ammsg = 1
    $ amisreply = 1

    #################
    if kissamber == True:
        $ contact_Amber.newMessage(amberMessage1)
        $ contact_Amber.newMessage(amberMessage2)
        $ contact_Amber.newMessage(amberMessage3)
        $ ammsg1 = "Hey, it's Amber"
        $ ammsg2 = "Josh gave me your number"
        $ ammsg3 = "You know, you never came back, I thought we were having a good time xx"
        $ amrep3a = "We did, I'll make it up to you."
        $ amrep3b = "Sorry, something came up."
        $ ammsg4 = "Oh really? How are you gonna do that?"
        $ amrep4a = "I give some world-class massages"
        $ amrep4b = "I'll stay longer next time"
        $ ammsg5 = "Oh okay, hope everything's okay xx"
        $ amrep5a = "Yeah, it's all good."
        $ ammsg6 = "That does sound enticing ;)"
        $ ammsg7 = "Deal xx"

    else:

        if joshMessage14.reply == "I can't, sorry.":
            $ contact_Amber.newMessage(amberMessage1a)
            $ contact_Amber.newMessage(amberMessage2a)
            $ contact_Amber.newMessage(amberMessage3a)

            $ ammsg1 = "Hey, it's Amber"
            $ ammsg2 = "Josh gave me your number"
            $ ammsg3 = "How come you didn't show up yesterday? Everything okay? xx"
            $ amrep3a = "Wow, you really wanted to see me, huh?"
            $ amrep3b = "Sorry, something came up."
            $ ammsg4 = "Oh wow, I was just checking. :P"
            $ amrep4a = "Don't worry, you'll see me soon"
            $ amrep4b = "Haha, I'm fine."
            $ ammsg5 = "Oh okay, hope you're good xx"
            $ amrep5a = "Yeah, it's fine"
            $ ammsg6 = "Was hoping xx"
            $ ammsg7 = "That's good xx"


        else:
            $ contact_Amber.newMessage(amberMessage1b)
            $ contact_Amber.newMessage(amberMessage2b)
            $ contact_Amber.newMessage(amberMessage3b)

            $ ammsg1 = "Hey, it's Amber"
            $ ammsg2 = "Josh gave me your number"
            $ ammsg3 = "You know, you never came back, everything okay?"
            $ amrep3a = "Wow, you really missed me that much, huh?"
            $ amrep3b = "Sorry, something came up."
            $ ammsg4 = "Oh shut up, I was just checking in"
            $ amrep4a = "Don't worry, you'll see me again"
            $ amrep4b = "Haha, I'm fine"
            $ ammsg5 = "Oh okay, hope you're good xx"
            $ amrep5a = "Yeah, it's fine"
            $ ammsg6 = "Was hoping xx"
            $ ammsg7 = "That's good xx"


    if toldlauren == False and laurentoofar == False:
        play sound "sounds/vibrate.mp3"
        $ phoneexit = "phonex"
        $ laisreply = 1
        $ lamsgnot = 1
        $ temp_MessageNot = True
        $ contact_Lauren.newMessage(laurenMessage12)
        $ contact_Lauren.newMessage(laurenMessage13)
        $ lamsg12 = "Hey"
        $ lamsg13 = "Wanna do the personality tests today at noon?"
        $ larep13a = "Yeah, sure."
        $ lamsg14 = "Great :) Meet me at our economics' classroom."

        u "(Oh shit, I'm getting a bunch of messages.)"

        label phonex:

        if laurenMessage13.reply:

            $ showphone = False
            u "(Time to get ready.)"

            jump continuez

        else:

            u "(I should probably reply to some of them.)"

            jump phonex





    else:


        $ phoneexit = "phoney"
        label phoney:

        "(Maybe it's Lauren and she wants to talk about what happened? I should definitely check.)"



        if not msgApp.notification:
            $ showphone = False
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
        if steam == False:
            image onthelow = "images/onthelow.png"
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

    la "Now it's up to you, will you actively decide to kill the dog to save a human life or will you idly stand by and let the her die?"

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
            if steam == False:
                image petapublicenemy = "images/petapublicenemy.png"
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
    if steam == False:
        image onthelow = "images/onthelow.png"
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

    $ fantasy = True

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
    $ fantasy = False
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
    image af2 = Movie(play="images/af2.webm", start_image="images/af2start.jpg", image="images/af2pic.jpg", loop = False)


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
    image af5 = Movie(play="images/af5.webm", start_image="images/af5start.jpg", image="images/af5pic.jpg", loop = False)
    image af6 = Movie(play="images/af6.webm", start_image="images/af6start.jpg", image="images/af6pic.jpg", loop = False)
    image af7 = Movie(play="images/af7.webm", start_image="images/af7start.jpg", image="images/af7pic.jpg", loop = False)
    image af8 = Movie(play="images/af8.webm", start_image="images/af8start.jpg", image="images/af8pic.jpg", loop = False)
    image af9 = Movie(play="images/af9.webm", start_image="images/af9start.jpg", image="images/af9pic.jpg", loop = False)
    image af10 = Movie(play="images/af10.webm", start_image="images/af10start.jpg", image="images/af10pic.jpg", loop = False)
    image af11 = Movie(play="images/af11.webm", start_image="images/af11start.jpg", image="images/af11pic.jpg", loop = False)
    image af12 = Movie(play="images/af12.webm", start_image="images/af12start.jpg", image="images/af12pic.jpg", loop = False)
    image af13 = Movie(play="images/af13.webm", start_image="images/af13start.jpg", image="images/af13pic.jpg", loop = False)
    image af14 = Movie(play="images/af14.webm", start_image="images/af14start.jpg", image="images/af14pic.jpg", loop = False)
    image af15 = Movie(play="images/af15.webm", start_image="images/af15start.jpg", image="images/af15pic.jpg", loop = False)
    image af16 = Movie(play="images/af16.webm", start_image="images/af16start.jpg", image="images/af16pic.jpg", loop = False)
    image youfinishadam = Movie(play="images/youfinishadam.webm", start_image="images/youfinishadamstart.jpg", image="images/youfinishadampic.jpg", loop = False)
    image adamfinish = Movie(play="images/adamfinish.webm", start_image="images/adamfinishstart.jpg", image="images/adamfinishpic.jpg", loop = False)


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
    if steam == False:
        image snitch = "images/snitch.png"
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

    ad "You think I'm scared of you , Chris?"

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

    ch "Well, you gave him a nose bleed, so you must have landed at least one good punch."

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
    $ contact_Chloe.unlock()
    $ contact_Amber.unlock()




    scene s442a # you stand up
    with dissolve

    play sound "sounds/vibrate.mp3"

    u "(Maybe that's Imre...)"




    if chloemad == True:
        $ contact_Amber.newMessage(amberMessage8)
        $ amisreply = 1
        $ ammsgnot = 1
        $ ammsg = 8
        $ ammsg8a = 1
        $ ammsg8 = "Hey, you alone? xx"
        $ amrep8a = "I'm at the park, but I'm by myself."
        $ ammsg9 = "Go somewhere where you're completely alone xx"
        $ ammsg10 = "I got a surprise for you ;)"
        $ phoneexit = "phoneaa"


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

        $ clisreply = 1
        $ clmsgnot = 1
        $ clmsg = 4
        $ clmsg4a = 1
        $ contact_Chloe.newMessage(chloeMessage4a)
        $ contact_Chloe.newMessage(chloeMessage5)
        $ clmsg4b = "I got some free time right now :)"
        $ clmsg5 = "Wanna go swimming?"
        $ clrep5a = "Any chance we could do it later? Or tomorrow?"
        $ clmsg6 = "I'm busy later tonight and I'm pretty much booked for the entire week :/"
        $ phoneexit = "phoneab"


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

    if steam == False:
        show screen getaccess
        with dissolve
        " "
        hide screen getaccess


    show credits:
        ypos 50
        xalign 0.5

    call screen thx
