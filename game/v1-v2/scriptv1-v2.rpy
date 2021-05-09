# The game starts here.
label start:
    # Get Animation/Transform List
    show nohardfeelings at achievementShow
    $ achievementAtList = renpy.get_at_list("nohardfeelings")
    hide nohardfeelings

    call screen realmode
    show screen phoneIcon

label v1:
    play music "music/msexy.mp3"
    show screen fantasyOverlay

    scene s0a
    with dissolve

    em "I know what I did was bad..."

    em "But I'll do anything to make it up to you."

    scene s0b
    with dissolve

    em "Anything."

    hide screen fantasyOverlay
    stop music fadeout 2.0

    scene s1
    with Fade(1, 0, 1)

    "Honey?"

    scene s1b
    with dissolve

    play music "music/m15punk.mp3"

    $ name = renpy.input(_("What's your name?"), default=_("Alex")).strip() or _("Alex")
    $ kiwiiUsers["MC"]["username"] = name

    u "Hmm...?"

    scene s2
    with dissolve

    ju "Breakfast is ready!"

    scene s1a
    with dissolve

    u "Mhmm... I'll be right down."
    u "(What am I doing dreaming about Emily?!)"

    scene s3
    show s3a
    with Fade(1, 0, 1)

    ju "Good morning, honey."

    hide s3a
    with dissolve

    u "Morning, Julia."

    show s3a
    with dissolve

    ju "Are you excited for today?"

    hide s3a
    with dissolve

    u "Excited?"

    show s3a
    with dissolve

    ju "Honey, it's your first day of college. That's a big deal!"

    hide s3a
    with dissolve

    u "I guess you're right."

    show s3b
    with dissolve
    ju "Have you packed all your stuff? Have you printed out all the documents you need? Have you-"

    hide s3b
    show s3c
    with dissolve

    u "Julia, it's fine. I packed yesterday."

    hide s3c
    show s3d
    with dissolve
    ju "Look at you, all grown-up. I'm so proud of you."

    scene s3f
    with dissolve

    ju "You better not forget to come visit."
    u "I'll think about it, if you make lasagna."

    show s3d
    with dissolve

    ju "I'm sure that could be arranged."

    ju "Anyway, we should get ready, you don't wanna be late on your first day of college!"

    hide s3d
    show s3e
    with dissolve

    u "Oh you're dropping me off? I was gonna take the train."

    hide s3e
    show s3d
    with dissolve

    ju "No way you're robbing me of the chance to embarrass you in front of your new friends."

    hide s3d
    show s3e
    with dissolve

    u "Thanks, Julia... I'll be 20 minutes."

    scene s11
    with Fade(1, 0, 1)
    
    u "(I better not lose this bag, Julia loves it.)"

    play sound "sounds/vibrate.mp3"

    u "(Huh?)"
    
    # Emily's messages
    python:
        def v1_reply1():
            setattr(store, "nohardfeelings", True)
            if not steam:
                renpy.show("nohardfeelings", at_list=achievementAtList)
            else:
                achievement.grant("no_hard_feelings")
                achievement.sync()

            contact_Emily.newMessage(_("Cool :)"))

        def v1_reply2():
            setattr(store, "openwound", True)
            if not steam:
                renpy.show("openwound", at_list=achievementAtList)
            else:
                achievement.grant("open_wound")
                achievement.sync()

            addPoint("tm", 1)
            contact_Emily.newMessage(_("Ugh :/"))

        contact_Emily.newMessage(_("Hey...\nI know we haven’t talked much after we broke up, but I just wanted to let you know that I didn’t get into Stanford, so I’ll be going to San Vallejo as well.\nGuess I’ll see you there. :)"), queue=False)
        contact_Emily.addReply(_("Yeah... I’ll see you there."), v1_reply1)
        contact_Emily.addReply(_("You cheated on me.\nGo to hell!"), v1_reply2)

    show screen phoneTutorial
    call screen phone
    hide screen phoneTutorial
    
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

    show screen kctTutorial
    menu:
        "Could be fun":
            hide s14
            show s14a
            with dissolve
            $ addPoint("tm", 1)

            u "I don't know... it might be fun."

        "No":
            hide s14
            show s14a
            with dissolve
            $ addPoint("bf", 1)

            u "No, I don't think so, Julia."

    hide screen kctTutorial

    hide s14a
    show s15
    with dissolve

    $ statsApp.unlock()

    play sound "sounds/vibrate.mp3"

    ju "Fraternities can be dangerous, honey."
    
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

    hide s15
    show s14a
    with dissolve

    u "Whatever... me and Josh haven't really talked much lately."

    u "(I wonder if he's still dealing...)"

    stop music fadeout 2.0

    car "*stops*"

    scene homepage2
    with Fade(1, 0, 1)

    ju "Well, this is it. San Vallejo College."

    show intro
    with flash

    " "

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

        "Inquire":
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

    scene s39
    with dissolve

    u "(Damn... she was really cute. Hopefully I'll get to see her again.)"

    u "(I should probably go to my induction class right now.)"

    stop music fadeout 2.0

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
            scene s46a
            with dissolve

            u "Wow Elijah, way to start the fun."

            $ funofelijah = True
            $ addPoint("tm", 1)

            scene s46b
            with dissolve
            el "..."

        "Stay quiet":
            pass

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

            scene s50a
            with dissolve

            u "It really is."

            u "Does that mean not all girls here are into the fighting?"

            scene s52
            with dissolve

            la "Not at all, pretty much any girl that's part of the Deer hates it."

        "Disagree":
            $ addPoint("tm", 1)

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
            scene s50a
            with dissolve

            u "Yeah, I get that."

            scene s54
            with dissolve

            la "I bet you think she's cute, don't you?"

        "Defend Autumn":
            $ addPoint("bf", 1)

            scene s50a
            with dissolve

            u "I think that's pretty cool."

            scene s54
            with dissolve

            la "Ohhh... so you think she's cute?"

    menu:
        "You're cuter":
            scene s53a
            with dissolve

            u "I think you're cuter."

            scene s54
            with dissolve
            la "Haha, prince charming huh?"

            scene s53a
            with dissolve

            u "Only for the right girl."

        "Yeah, kinda":
            $ addPoint("bf", 1)

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

    stop music fadeout 2.0

# Part 5 Free roam in the halls
    scene s50 # hallway 1 without freeroam
    with Fade(1, 0, 1)

    u "(I should probably go to my new dorm, but I might as well explore for a bit beforehand.)"

    play music "music/mchill2.mp3"

    scene s50 # freeroam
    with dissolve

    python:
        def v1_reply3():
            addPoint("bf", 1)

        def v1_reply4():
            addPoint("bro", 1)

        contact_Julia.newMessage(_("Hey honey,\nenjoy your time in college.\nStay safe and don't forget to visit me.\nLove you"), queue=False)
        contact_Julia.addReply(_("Love you too."), v1_reply3)
        contact_Julia.addReply(_("Thanks, Julia :)"), v1_reply4)

    play sound "sounds/vibrate.mp3"
    
    # Enter free roam
    $ freeRoam = True
    show screen freeRoamTutorial
    call screen v1_freeRoam1_1
    with dissolve

    label v1_freeRoam1_riley:
        $ v1_talkToRiley = True
        
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

            "She seems nice.":
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

        $ v1_freeRoam1_riley = True
        call screen v1_freeRoam1_1
        with dissolve

    label v1_freeRoam1_riley2:
        scene s50ri1a

        u "You should really consider sitting in the last row."

        scene s50ri1
        with dissolve

        ri "Yeah.. you're probably right haha."
        
        call screen v1_freeRoam1_1

    label v1_freeRoam1_elijah:
        scene s50el
        u "Hey, you're Elijah right?"

        if funofelijah:
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

                scene s50el2a
                with dissolve

                u "Sooo... the nerds?"

                scene s50el1
                with dissolve

                el "How dare you defy the frogs like that?!"

                el "Just get out of my face."

            "That's cool.":
                $ addPoint("bf", 1)

                scene s50el2a
                with dissolve
                u "I think that's pretty cool."

                scene s50el1
                with dissolve

                el "It's not \"cool\"! It's prestigious and an incredible opportunity."

                el "Now go and bother someone else."
                
        $ v1_freeRoam1_elijah = True

        call screen v1_freeRoam1_1

    label v1_freeRoam1_elijah2:
        
        scene s50el1a
        u "Elijah?"

        scene s50el1
        with dissolve
        el "Leave me alone."
        
        call screen v1_freeRoam1_1

    label v1_freeRoam1_chris:
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
        $ v1_freeRoam1_chrisGone = True
        
        call screen v1_freeRoam1_2

    label v1_freeRoam1_nora:
        scene s56no1a
        u "Hey, could you tell me where the dorms are?"

        scene s56no1
        with dissolve
        no "They're right through the doors behind you."

        menu:
            "Flirt":
                $ addPoint("tm", 1)
                $ v1_hitOnNora = True

                scene s56no1a
                with dissolve

                $ keepitmoving = True
                if not steam:
                    show keepitmoving at achievementShow
                else:
                    $ achievement.grant("keep_it_moving")
                    $ achievement.sync()

                u "Actually, I knew that. I just wanted to talk to you 'cause you're really cute."

                scene s56no1
                with dissolve
                no "Look, I've got a boyfriend, so keep it moving."

            "Leave":
                scene s56no1a
                with dissolve

                u "Thanks."

    $ v1_freeRoam1_nora = True
    call screen v1_freeRoam1_2

    label v1_freeRoam1_nora2:
        scene s56no1a
        
        u "Uhm..."
        if v1_hitOnNora:
            scene s56no1
            with dissolve
            no "Dude, keep it moving."

        else:
            scene s56no1
            with dissolve
            no "I'm busy."

        call screen v1_freeRoam1_2

    label v1_freeRoam1_aubrey:
        scene adamaubrey36
        stop music fadeout 2.0
        play music "music/msexy.mp3"
        show adam1

        au "Ohhh shit, that feels good!"
        u "(Oh my god... she's so fucking hot.)"
        au "YESSSSS, FASTER!"
        u "(I should probably stop peeking, before I get caught.)"

        $ v1_freeRoam1_aubrey = 1
        
        stop music fadeout 2.0
        call screen v1_freeRoam1_3

    label v1_freeRoam1_aubrey2:
        scene s58
        u "I shouldn't risk peeking again."
        call screen v1_freeRoam1_3

label efra:
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

            scene s63a
            with dissolve

            u "Soo.. they're equally good?"

            scene s64
            with dissolve

            imre "Noooo! The Wolves are better. How are you not getting this?!"

            scene s64a
            with dissolve

            u "I feel like your math doesn't add up there."

            scene s63d
            with dissolve

        "The Wolves sound sick.":
            $ addPoint("bro", 1)

            scene s64a
            with dissolve
            u " Honestly, after listening to you, the Wolves sound sick!"

            scene s63d
            with dissolve

            imre "Yeahhhh! They fucking are man. That's what I've been trying to tell you."

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

    python:
        def v1_reply5():
            addPoint("bf", 1)

        contact_Lauren.addReply(_("Hey Lauren, would you want to hang out with me and my friends tonight?"))
        contact_Lauren.newMessage(_("Yeah sounds good :) Where do you wanna meet?"))
        contact_Lauren.addReply(_("Just come to dorm 109 at 8"))
        contact_Lauren.newMessage(_("Okay, will do"))
        contact_Lauren.addReply(_("See you later, cutie"), v1_reply5)
        contact_Lauren.addReply(_("Cool"))


    label v1_phoneCheck1:
        call screen phone
        if contact_Lauren.getReplies():
            scene s61
            with dissolve
            imre "Did you ask?"

            scene s61
            with dissolve
            u "Oops I forgot."

            jump v1_phoneCheck1

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

    if v1_talkToRiley:
        scene s67
        with dissolve
        ri "Yeah, we've met."

        scene s67a
        with dissolve
        imre "Oh really?"

        scene s67a
        with dissolve
        u "Yeah, we were in the same induction class."

    else:
        scene s67
        with dissolve
        ri "Hey, you were in my induction class, right?"

        scene s67a
        with dissolve
        u "Yeah, that's right. Good to see you again."

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
            scene s73gr
            with dissolve

            u "Wow... you're missing out, Lauren."

            scene s73ar
            with dissolve

            la "I guess we'll never know."

        "Dodged a bullet there.":
            $ addPoint("tm", 1)

            scene s73gr
            with dissolve

            u "Phew, dodged a bullet there."

            scene s72f
            with dissolve

            imre "Damn..."

    scene s72f
    with dissolve

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

            scene s76
            with dissolve

            u "There you go. Happy now?"

            scene s71cf
            with dissolve

            ri "Very happy."

            scene s71ef
            with dissolve

            u "Well then, Riley, I dare you to also take your shirt off."

        "Drink instead":
            scene s76a
            with dissolve

            " "

            scene s71bf
            with dissolve

            ri "Really? That was such an easy dare."

            scene s71ef
            with dissolve

            u "If that's what you think, then I dare you to take your shirt off."

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

            scene s71ef
            with dissolve
            u "You gotta do the dare, or drink."

            scene s71cf
            with dissolve

            ri "Fine..."

            scene s77
            with dissolve

            " "

        "You're right.":
            $ addPoint("bf", 1)
            
            scene s71ef
            with dissolve
            u "You're right, let's continue."

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

    ### Late night talk with Imre.
    scene s80
    with Fade(1, 0, 1)
    play music "music/msad.mp3"
    imre "Man, I can't wait to bang this Riley chick."

    menu:
        "Riley's mine.":
            $ addPoint("tm", 1)

            scene s79b
            with dissolve
            u "What? I want Riley. You can have Lauren."

            scene s80e
            with dissolve
            imre "What the hell man?! I invited Riley. Back off."

            menu:
                "You're right, sorry.":
                    $ addPoint("bro", 1)

                    scene s79a
                    with dissolve
                    u "You're right, Riley is yours. I'm sorry."

                    scene s80a
                    with dissolve

                    imre "It's fine bro, I get it. She is really cute."

                "She wants me.":
                    $ addPoint("tm", 1)

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

        "They're both hot.":
            $ addPoint("bro", 1)

            scene s79
            with dissolve
            u "Hahaha, to be honest they're both pretty hot."

    scene s80
    with dissolve

    imre "Oh man, we're gonna bang so many chicks this year. Trust me, all you need is confidence..."

label at_bd:
    imre "And to be part of a frat."

    if v1_freeRoam1_aubrey:
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

    ### Sex dream

    scene s1  ### close to the kitchen counter
    with Fade (1,0,1)

    ri "Wow, you guys have a really nice house."

    show screen fantasyOverlay
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
            $ v1_sda = True

            scene sda3a
            with fade

            ri "*Chuckles* You're hard already."

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

                "Footjob":

                    scene sda3b
                    with dissolve

                    u "I want you to use your feet."

                    scene sda3a
                    with dissolve

                    ri "I was hoping you'd say that."

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

            scene aftercum
            show sdacum2
            with dissolve

            u "Hngh..."

            scene sda7
            with dissolve

            ri "My legs are shaking."

        "Wake up":
            pass

    hide screen fantasyOverlay

    stop music fadeout 2.0
    $ renpy.end_replay()

    ### Next morning in your dorm, Imre seems to be gone.

    if v1_sda:
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

        "Bad roommates suck.":
            $ addPoint("bro", 1)

            scene s87a
            with dissolve
            u "I get that, bad roommates suck."

            scene s87
            with dissolve

            la "It was just such a bad start into the day. I really didn't wanna be late to my first real class."

            scene s87a
            with dissolve
            u "How about we go to the park this afternoon? I'll bring some sandwiches and we'll make your day better."

    scene s87b
    with dissolve
    stop music fadeout 2.0

    la "Yeah, I'd like that."

    ### park with Lauren (secret sharing)

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
            scene s89d
            with dissolve
            u "I bet you could get any guy you want."

            scene s89f
            with dissolve
            la "Uhm... thanks. Not really though, haha."

        "Yet, you're here with me.":
            $ v1_laurenPoints += 1

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

            scene s89f
            with dissolve

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

        "I've broken into an Ikea.":

            $ v1_laurenPoints += 1
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

            u "You know... you're really beautiful."

            scene s89
            with dissolve
            la "Awww."

        "You're not ugly.":
            $ addPoint("bro", 1)

            u "You know... you're not ugly."

            scene s89b
            with dissolve

            la "Wow, how flattering."

    scene s89k
    with dissolve

    u "(Is this the moment to kiss her?)"

    menu:
        "Kiss her":
            $ v1_laurenKiss = True

            if v1_laurenPoints == 2:
                scene s90
                with dissolve # kiss
                $ v1_kissLauren = True

                $ romeo = True
                if not steam:
                    show romeo at achievementShow
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

        "Don't kiss her":

            scene s90b # you scratching your head
            with dissolve
            " "

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

    if v1_laurenKiss:
        u "(Fuck... why did I try to kiss her?! That just made everything weird.)"
    else:
        u "(Fuck... should I have kissed her? Now it's just weird between us.)"

    ### Back in your dorm with Imre
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

    if v1_laurenKiss and v1_laurenPoints == 2:
        scene s96a
        with dissolve
        u "I just don't get it..."

        u "I kissed her... and for a second she kissed me back."

        u "But then she pulled away and left."

        u "And now it's all just super weird."

    elif v1_laurenKiss:
        scene s96a
        with dissolve

        u "I just don't get it..."

        u "She gave me all the signs, so I went for a kiss."

        u "But she pulled away and left."

        u "And now it's all just super weird."

    else:
        scene s96a
        with dissolve

        u "I just don't get it..."

        u "Everything was going great, until there was this moment."

        u "Maybe she wanted me to kiss her, but... I didn't go for it."

        u "And then she just left..."

        u "And now it's all just super weird."

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

    scene s96c
    stop music fadeout 2.0
    play sound "sounds/vibrate.mp3"
    python:
        contact_Ryan.newMessage(_("Hey man, it's Ryan.\nThe Apes' rush party is tonight at 9. You're coming, right???"), queue=False)
        contact_Ryan.addReply(_("Alright, but I'll only stay for a few hours."))
        contact_Ryan.newMessage(_("Haha, trust me, you're not gonna want to leave once you see all the hot chicks there."))
        contact_Ryan.newMessage(_("Just meet me in front of the Apes' frat house at 9."))
        contact_Ryan.addReply(_("Okay, will do."))

    label repeata:
        call screen phone
        if contact_Ryan.getReplies():
            u "(I should really check who texted me.)"
            jump repeata

    scene s96c
    with dissolve
    
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

    ### In front of the ape's house ryan is texting
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

    $ freeRoam = True
    call screen v1_freeRoam2_1

label v1_freeRoam2_sam:
    $ v1_samTalk = True

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

    call screen v1_freeRoam2_1

label v1_freeRoam2_sam2:

    scene s100a

    u "(I don't wanna risk getting dragged into their argument.)"

    call screen v1_freeRoam2_1

label v1_freeRoam2_door:
    play music "music/mparty2.mp3"

    queue music [ "music/mparty3.mp3", "music/mparty4.mp3" ]
    
    $ v1_fr2door = True
    scene s103

    ry "Alright man, I'm gonna look around, I'll see you in a bit."

    scene s103a

    u "Cool."

    u "(Great, now I'm all on my own.)"

    call screen v1_freeRoam2_2

label v1_freeRoam2_pool:
    if not v1_joshTalk:
        scene s102

        u "(I should talk to Josh first, I haven't seen him in a while.)"

        call screen v1_freeRoam2_2
    else:
        call screen v1_freeRoam2_3

label v1_freeRoam2_courtney:
    $ v1_courtneyTalk = True

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

    call screen v1_freeRoam2_2

label v1_freeRoam2_courtney2:
    scene fr2co2
    with dissolve

    courtney "I said leave me alone, perv."

    scene fr2co2a
    with dissolve

    u "Right..."

    call screen v1_freeRoam2_2

label v1_freeRoam2_josh:
    $ v1_joshTalk = True

    scene fr2jo1a

    jo "[name]! I didn't know you're also going to San Vallejo. *sniff*"

    jo "This is uhhh... Aubrey!"

    scene fr2jo2a
    with dissolve

    au "Hey, nice to meet you."

    scene fr2jo2b
    with dissolve

    if v1_freeRoam1_aubrey:
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
                    $ v1_aubreywannafight = True

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

                "Say you're not a fighter":
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

        "Ask if she likes fighters":
            $ addPoint("bf", 1)

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
                    $ v1_aubreywannafight = True

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

                "No, that's not for me.":
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

    scene fr2jo2a
    with dissolve

    au "He's the president of the Apes and the current Fight King."

    if v1_aubreywannafight:
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

    call screen v1_freeRoam2_2

label v1_freeRoam2_josh2:
    scene s102

    u "(I should talk to some other people around here and make some new friends.)"

    call screen v1_freeRoam2_2

label v1_freeRoam2_stairs:
    if not v1_joshTalk:
        scene s102

        u "(I should talk to Josh first, I haven't seen him in a while.)"

        call screen v1_freeRoam2_2
    else:
        call screen v1_freeRoam2_5

label v1_freeRoam2_camp:
    if not v1_joshTalk:
        scene s102

        u "(I should talk to Josh first, I haven't seen him in a while.)"

        call screen v1_freeRoam2_2

    else:
        play sound "sounds/vibrate.mp3"

        python:
            def v1_reply6():
                addPoint("bf", 1)
                contact_Lauren.newMessage(_("Cool :)"))

            def v1_reply7():
                addPoint("tm", 1)
                contact_Lauren.newMessage(_("Idk, it's just feels kinda weird now. Can we please just talk tomorrow?"))
                contact_Lauren.addReply(_("Fine"))
                contact_Lauren.newMessage(_(":)"))

            contact_Lauren.newMessage(_("Hey :)\nSorry about today.\n\nCan we talk tomorrow?"), queue=False)
            contact_Lauren.addReply(_("Yeah, sure."), v1_reply6)
            contact_Lauren.addReply(_("What is there to talk about?"), v1_reply7)

        call screen v1_freeRoam2_4

label v1_freeRoam2_mason:
    $ v1_masonTalk = True

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

            scene fr2ma1a
            with dissolve

            $ bigmouth = True
            if not steam:
                show bigmouth at achievementShow
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

        "I didn't wanna fight him.":
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

    call screen v1_freeRoam2_3


label v1_freeRoam2_mason2:
    scene s104

    u "I've already talked to these guys."

    call screen v1_freeRoam2_3

label v1_freeRoam2_katy:
    $ v1_katyTalk = True

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

    call screen v1_freeRoam2_3

label v1_freeRoam2_katy2:
    scene s104

    u "(I'm definitely not going back there.)"

    call screen v1_freeRoam2_3

label v1_freeRoam2_grayson:
    $ v1_graysonTalk = True
    
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

    call screen v1_freeRoam2_5

label v1_freeRoam2_grayson2:
    scene s105
    with dissolve

    u "(Somehow barging into a private conversation of two violence-addicted frat guys doesn't sound appealing to me.)"

    call screen v1_freeRoam2_5

label v1_freeRoam2_end:
    stop music fadeout 2.0
    
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

        "She's occupied.":
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

            u "I'm really sorry for interrupting your conversation."

            scene s112b
            with dissolve

            cl "I should be thanking you for saving me. He literally spent the last 20 minutes talking about rocks."

            scene s112c
            with dissolve

            u "In that case, you're very welcome."

        "Make fun of him":
            $ addPoint("bro", 1)

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

            scene s116a
            with dissolve

            u "Wow, that sounds awful."

            scene s116b
            with dissolve

            cl "It really was."

        "Poke fun":
            $ addPoint("tm", 1)

            scene s116a
            with dissolve

            u "Hahaha, sounds like the dean was into you."

            scene s116d
            with dissolve

            cl "Ewww. Don't say that, hahaha."

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
    pause 0.5

    stop music
    #####punch
    $ renpy.movie_cutscene("punchdemo.webm", loops=0)

    " "

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

            scene s123d
            with dissolve
            u "Hmm... maybe."

            scene s123
            with dissolve
            imre "Just think about it, okay? I'll see you later."

        "I'm not fighting.":
            $ addPoint("bf", 1)

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

                    scene s123d
                    with dissolve
                    u "Look, I'll think about it. But don't get your hopes up."

                    scene s123
                    with dissolve
                    imre "That's all I'm asking for. I'll see you later."

                "I won't fight.":
                    $ addPoint("bf", 1)

                    scene s123d
                    with dissolve
                    u "I'm not fighting. That's final."

                    scene s123c
                    with dissolve

                    imre "You're being stupid, man. Whatever, suit yourself."

    scene s96g
    with fade

    play sound "sounds/vibrate.mp3"
    queue sound "sounds/vibrate.mp3"

    python:
        def v1_reply8():
            addPoint("bro", 1)
            contact_Ryan.newMessage(_("Look, I know what Grayson did was a dick move, but he was just being overprotective of Chloe"))
            contact_Ryan.addReply(_("Whatever"), v1_reply9)
            contact_Ryan.addReply(_("Don't you dare defend that guy"), v1_reply10)

        def v1_reply9():
            addPoint("bro", 1)

        def v1_reply10():
            addPoint("tm", 1)
            contact_Ryan.newMessage(_("Sorry..."))

        def v1_reply11():
            addPoint("tm", 1)
            contact_Ryan.newMessage(_("Look, I know what Grayson did was a dick move, but he was just being overprotective of Chloe"))
            contact_Ryan.addReply(_("Whatever"), v1_reply9)
            contact_Ryan.addReply(_("Don't you dare defend that guy"), v1_reply10)

        contact_Ryan.newMessage(_("You okay?"), queue=False)
        contact_Ryan.addReply(_("I'm fine"), v1_reply8)
        contact_Ryan.addReply(_("No, wtf was that?! Fuck Grayson and fuck the Apes"), v1_reply11)


        def v1_reply12():
            setattr(store, "meetlauren", True)
            addPoint("bf", 1)
            contact_Lauren.newMessage(_("Great, I'll see you then :)"))

        def v1_reply13():
            setattr(store, "mixedfeelings", True)
            if not steam:
                renpy.show("mixedfeelings", at_list=achievementAtList)
            else:
                achievement.grant("mixed_feelings")
                achievement.sync()

            addPoint("tm", 1)
            contact_Lauren.newMessage(_("Is everything okay?"))
            contact_Lauren.addReply(_("Yeah, I'm fine."))
            contact_Lauren.newMessage(_("Okay..."))

        if contact_Lauren.getReplies():
            contact_Lauren.newMessage(_("Hello?? Can we please talk today?"), queue=False)
            contact_Lauren.addReply(_("Yeah, SV cafe in 20 mins?"), v1_reply12)
            contact_Lauren.addReply(_("Sorry, I can't"), v1_reply13)
        else:
            contact_Lauren.newMessage(_("Are we still on for today? :)"), queue=False)
            contact_Lauren.addReply(_("Yeah, SV cafe in 20 mins?"), v1_reply12)
            contact_Lauren.addReply(_("Sorry, I can't"), v1_reply13)

    " "

    scene s96g
    with dissolve

    label repeatb:
        call screen phone
        if contact_Lauren.getReplies():
            u "(Damn, my phone's blowing up. I should probably check my messages.)"

            jump repeatb

    if meetlauren:
        u "(Well, time to head to the cafe to meet Lauren.)"

    else:
        u "(There's too much on my mind to be dealing with Lauren right now.)"

        u "(Maybe taking a walk will relax me.)"

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
            jump v1_tomShoutBack

        "Keep walking":
            scene s125a
            with dissolve

            tom "Yeah, you better keep walking, pussy."

            menu:
                "Shout back":
                    jump v1_tomShoutBack

                "Walk away":
                    $ fighttom = False

                    jump v1_tomWalkAway

label v1_tomShoutBack:
    $ fighttom = True

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

    scene tompush
    pause 0.7
    play sound "sounds/push.mp3"
    scene push12
    with vpunch

    tom "Fuck you!"

    stop music fadeout 2.0

# Tom Fight
label gb:
    if not adamtut:

        scene sf1
        with dissolve
        " "

    $ stance = 1

    scene tomstancekick
    with dissolve

    if not adamtut:
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
        elif s28_LarsFight:
            jump s28_LarsFightCont
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

        if s28_LarsFight:
            call screen af3

        elif adamtut:
            call screen s28_LarsKeybindOptions

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

    jump v1_tomWalkAway



label youfinish:
    if reaction == 0.5:
        $ thenotorious = True
        if not steam:
            show thenotorious at achievementShow
        else:
            $ achievement.grant("the_notorious")
            $ achievement.sync()
    $ wintom = True

    menu:

        "Kick him":
            $ addPoint("tm", 1)

            play sound "sounds/js.mp3"
            scene yf
            with vpunch

            u "Fuck you!"

        "Walk away":
            $ addPoint("bro", 1)

label v1_tomWalkAway:
    $ firstfight = False

    $ renpy.end_replay()

    if not meetlauren:
        $ laawk = True
        scene s133
        with Fade (1,0,1) # in front of san vallejo
        if fighttom and not wintom:
            u "(Fuck, I feel like shit...)"

        elif fighttom:
            u "(Holy shit, I just knocked someone out...)"

        else:
            u "(What a douchebag...)"

        u "(Also, what am I gonna do about Lauren? I can't avoid her forever.)"

        jump history2

    else:
        jump meet_lauren2


label meet_lauren2:
    play music "music/mlove2.mp3"

    if fighttom and not wintom:
        scene s128a #outside of cafe with bloody nose
        with Fade (1,0,1)
        u "(Fuck, I feel like shit...)"

        u "(Hopefully Lauren doesn't make a big deal out of my bruises.)"

    elif fighttom:
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

    if fighttom and not wintom:
        u "(And also I just got beaten up by another guy on the way here...)"

    elif fighttom:
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

    la "About yesterday in the park..."

    show screen influenceTutorial

    menu:
        "There was something there.":
            $ addPoint("bf", 1)
            
            if v1_laurenKiss and v1_laurenPoints == 2:
                    scene s130c
                    with dissolve
                    u "I know you stopped kissing me after about a second..."

                    u "But that second was amazing."

                    u "There was something real there and you know it."

            elif v1_laurenKiss:
                scene s130c
                with dissolve

                u "I don't know why you pulled away when I tried to kiss you..."

                u "Maybe you were scared..."

                u "But there was something real there and you know it."

            else:
                scene s130c
                with dissolve

                u "We had this moment where I wanted to kiss you, but I didn't..."

                u "And I should have. There was something real there. Between us."

            hide screen influenceTutorial

            if kct == "loyal" or v1_kissLauren:
                $ laurenrs = True

                if kct == "loyal":
                    call screen popup1

                scene s131 ### Lauren grabbing your hand on the table
                with dissolve

                " "

                scene s130d # Lauren romancing at you holding your hand
                with dissolve

                $ anewbeginning = True
                if not steam:
                    show anewbeginning at achievementShow
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

                if fighttom and not wintom:
                    scene s130e
                    with dissolve

                    u "(I should probably wash the blood off my face in the restroom before I go to class.)"

                jump history

            else:
                scene s130f # lauren flustered
                with dissolve

                la "[name], I really like you..."

                la "... but I think we're just better as friends."

                la "I don't wanna jeopardize our friendship."

                menu:
                    "Give me a chance.":
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

                        if fighttom and not wintom:
                            scene s132 ## empty table, Lauren gone
                            with fade
                            u "(Shit, I forgot I have class right now.)"

                            u "(I should probably wash the blood off my face before I go.)"

                        jump history

                    "You're right.":
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

                        if fighttom and not wintom:
                            scene s130j
                            with dissolve

                            u "(I should probably wash the blood off my face in the restroom before I go to class.)"

                        jump history

        "Let's forget about it.":
            $ addPoint("bro", 1)
            $ laawk = False

            scene s130a
            with dissolve

            if v1_laurenKiss:
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

            if fighttom and not wintom:
                scene s130j
                with dissolve

                u "(I should probably wash the blood off my face in the restroom before I go.)"

            jump history

label history:
    scene s133
    with Fade (1,0,1)

    stop music fadeout 2.0

label history2:
    play sound "sounds/vibrate.mp3"

    python:
        def v1_reply14():
            addPoint("bro", 1)
            contact_Josh.newMessage(_("It's fine, you go get her."))

        def v1_reply15():
            addPoint("bf", 1)
            contact_Josh.newMessage(_("Nah, you don't want a bitch like her."))
            contact_Josh.addReply(_("Yeah, I guess you're right."), v1_reply16)
            contact_Josh.addReply(_("Dude, what the fuck?!"), v1_reply17)

        def v1_reply16():
            addPoint("bro", 1)
            contact_Josh.newMessage(_("Hahaha, I'm just kidding, yo."))
            contact_Josh.newMessage(_("Of course I gave her your number."))
            contact_Josh.addReply(_("Damn, you got me."))

        def v1_reply17():
            addPoint("tm", 1)
            contact_Josh.newMessage(_("Hahaha, I'm just kidding, yo."))
            contact_Josh.newMessage(_("Of course I gave her your number."))
            contact_Josh.addReply(_("Damn, you got me."))

        contact_Josh.newMessage(_("Dude, I talked to this Aubrey chick the entire night and guess who's number she wanted..."), queue=False)
        contact_Josh.newMessage(_("YOURS"))
        contact_Josh.newMessage(_("What a bitch..."))
        contact_Josh.addReply(_("Sorry, man. She doesn't know what she's missing."), v1_reply14)
        contact_Josh.addReply(_("Sooo, did you give it to her?"), v1_reply15)

    scene s133
    with dissolve

    u "(Time to sit through another boring ass lecture.)"

    play music "music/m16punk.mp3"
    scene s136 ## seeing Imre in lecture room looking apologetic
    with Fade (1,0,1)

    imre "Hey man, about earlier, I-"

    if fighttom and wintom:
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

        if meetlauren:
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

    elif fighttom:
        scene s136b
        with dissolve #Imre surprised

        imre "Dude, did you get beaten up again?! You look like shit!"

        scene s136f # Imre angry
        with dissolve

        imre "Was it another ape??? Tell me who, I'll fuck them up!"

        if meetlauren:
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

    else:
        scene s136a
        with dissolve

        u "Imre, another guy tried to fight me today."

        scene s136b
        with dissolve

        imre "Oh shit, what happened? Another Ape?"

        if meetlauren:
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

    if v1_hitOnNora:
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

        "No, sorry.":
            $ emilyandben = True
            $ forgiveemily = False
            $ addPoint("tm", 1)

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

        "I'm still single.":
            $ addPoint("bf", 1)

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

            hide s145c
            show s145d
            with dissolve #u looking romantic


            u "No way, you looked so adorable."

            hide s145d
            show s145f
            with dissolve
            em "What was adorable was how much you cared for me. I remember you bringing me a care package full of like a hundred different soups."

            em "It was so thoughtful."

        "It was so funny.":
            $ addPoint("bro", 1)

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

    stop music
    play sound "sounds/busstop.mp3"

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

            scene s148b
            with dissolve

            $ overit = True
            if not steam:
                show overit as achievementShow:

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

        "Stay away from her.":
            $ emilyandben = False
            $ addPoint("bf", 1)

            scene s148b
            with dissolve

            u "Just - just stay away from her, okay?"

            scene s148a
            with dissolve

            ben "Fine, bro. Sorry for asking."

    scene s149 # emily in waiting room
    with fade

    em "All done with the forms?"

    menu:
        "Tell Emily about Benjamin":
            $ addPoint("bf", 1)
            $ addPoint("tm", 1)

            scene s149a
            with dissolve

            u "Yeah, but while I was doing it Benjamin asked me if he could make a move on you."

            scene s150 # em close up flirting
            with dissolve

            em "Oh really, are you my guardian now?"

            scene s150a # em curious
            with dissolve
            em "What did you say?"

            if emilyandben:
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

        "Don't tell Emily":
            $ addPoint("bro", 1)

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

    u "Uhm... no, that's fine. It doesn't hurt too badly."

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

    if forgiveemily:
        u "(Even though that just cost me almost a hundred dollars, it was kinda nice to spend time with Emily.)"

        u "(Still... I don't know if I can ever fully forgive her for what she did.)"

    # text from aubrey
    play sound "sounds/vibrate.mp3"

    python:
        def v1_reply18():
            addPoint("bro", 1)
            contact_Aubrey.newMessage(_("Yeah, I mean they had a thing a while ago but she broke it off 'cause he lied about some shit."))
            contact_Aubrey.newMessage(_("So... tomorrow?"))
            contact_Aubrey.addReply(_("My day tomorrow is quite full, but how about today?\n\nI need to buy a costume."), v1_reply19)

        def v1_reply19():
            addPoint("bf", 1)
            contact_Aubrey.newMessage(_("I've got dance practice tonight :("))
            contact_Aubrey.addReply(_("I'm not talking tonight, I can pick you up right now."))
            contact_Aubrey.newMessage(_("Oh wow, that's spontaneous, I like it haha.\n\nI guess come to the Chicks' house whenever you're ready and then we can go costume shopping."))
            contact_Aubrey.addReply(_("Cool, I'll be 20 mins."))

        contact_Aubrey.newMessage(_("Hey,\nJosh gave me your number\n\nI hope your face is feeling better after the shit that Grayson pulled..."))
        contact_Aubrey.newMessage(_("He's not even dating Chloe and you guys didn't even do anything so I don't know what he was thinking.\n\nAnyway, do you wanna like... hang out tomorrow?"))
        contact_Aubrey.addReply(_("Wait they're not dating?"), v1_reply18)
        contact_Aubrey.addReply(_("My day tomorrow is quite full, but how about today?\n\nI need to buy a costume."), v1_reply19)

    u "(Oh, I just got a message.)"

    label repeatc:
        call screen phone
        if contact_Aubrey.getReplies():
            u "(I should check my messages.)"
            jump repeatc
    
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

    python:
        def v1_reply20():
            setattr(store, "costumeaubrey", True)
            addPoint("bf", 1)
            contact_Aubrey.newMessage(_("Good :)"))

        def v1_reply21():
            setattr(store, "costumeaubrey", False)
            addPoint("tm", 1)
            contact_Aubrey.newMessage(_("Oh, okay. Guess we'll have to postpone the costume buying."))

        contact_Aubrey.newMessage(_("Hey, are you nearby?"))
        contact_Aubrey.addReply(_("Yeah, I'm just on my way, I'll be right there."), v1_reply20)
        contact_Aubrey.addReply(_("Sorry, something came up and I can't make it."), v1_reply21)

    u "(Fuck, I totally forgot about Aubrey. I guess it's time to make a decision.)"

    label repeatg:
        call screen phone
        if contact_Aubrey.getReplies():
            u "(Aubrey's waiting for me, I need to let her know whether I'm coming or not.)"

            jump repeatg

    if costumeaubrey:
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
    if try1done:
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

            scene s164 # Aubrey changing bad view
            with dissolve

            u "(Holy shit, if I could just stick my head through a bit further, I could get a way better view."

            menu:
                "Risk it":
                    $ caughtpeekingaubrey = renpy.random.choice([True, False])

                    if not caughtpeekingaubrey:
                        scene s164a # Aubrey changing good view
                        with dissolve

                        u "(Oh my god, her ass is perfect.)"

                        u "(I should stop peeking now, or I'll get caught.)"

                    else:
                        jump caughta

                "Stop peeking":
                    pass

        "Don't peek":
            $ addPoint("bf", 1)

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

        "It's definitely something.":
            $ addPoint("bro", 1)

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

            scene s168 # Aubrey changing bad view
            with dissolve

            u "(Wow... if I could just stick my head through a bit further, I could get a way better view."

            menu:
                "Risk it":
                    $ caughtpeekingaubrey = renpy.random.choice([True, False])

                    if not caughtpeekingaubrey:
                        scene s168a # Aubrey changing good view
                        with dissolve

                        u "(Damn, what I wouldn't give to touch her ass right now.)"

                        u "(I should stop peeking now, or I risk getting caught.)"

                    else:
                        jump caughtb

                "Stop peeking":
                    pass

        "Don't peek":
            $ addPoint("bf", 1)

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

        "certainly practical.":
            $ addPoint("bro", 1)

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

            scene s172 # Aubrey changing bad view
            with dissolve

            u "(Fuck... if I could just stick my head through a bit further, I could get a way better view."

            menu:
                "Risk it":
                    $ caughtpeekingaubrey = renpy.random.choice([True, False])

                    if not caughtpeekingaubrey:
                        scene s172a # Aubrey changing good view
                        with dissolve

                        u "(In all fairness, whenever I watch porn, the person getting caught spying gets to fuck the girl right afterwards.)"

                        u "(Still... I better stop peeking now, it's too risky.)"
                    else:
                        jump caughtc

                "Stop peeking":
                    pass

        "Don't peek":
            $ addPoint("bf", 1)

    scene s171
    with dissolve

    u "Man she's gonna love this costume."

    scene s199 # showing u in front of closed stall with Aubrey
    with Fade (1,0,1)

    u "Aubrey? Are you coming out?"

    au "This costume is literally just historic lingerie."

    show screen influenceTutorial

    au "I'm not showing you this, haha."

    menu:
        "Oh come on.":
            hide screen influenceTutorial
            $ addPoint("tm", 1)

            u "Oh come on, Aubrey. I wanna see."

            if kct == "popular":
                call screen popup2
            else:
                au "Sorry but... I'm gonna get dressed again."


                u "Alright, fine."

                jump by_bd

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

        "Fine.":
            hide screen influenceTutorial
            $ addPoint("bf", 1)

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
    if try4done:
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

            scene s183 # penelope changing bad view
            with dissolve

            u "(Holy shit, if I could just stick my head through a bit further, I could get a way better view.)"

            menu:
                "Risk it":
                    $ caughtpeekingpenelope = renpy.random.choice([True, False])

                    if not caughtpeekingpenelope:
                        scene s183a # pen changing good view
                        with dissolve

                        u "(Oh my god, her ass is so nice.)"

                        u "(I should stop peeking now, or I'll get caught.)"

                    else:
                        jump caughtd

                "Stop peeking":
                    pass

        "Don't peek":
            $ addPoint("bf", 1)

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

        "I guess it's nice":
            $ addPoint("bro", 1)

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

    if try5done:
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

            scene s183 # pen changing bad view
            with dissolve

            u "(Wow... if I could just stick my head through a bit further, I could get a way better view."

            menu:
                "Risk it":
                    $ caughtpeekingpenelope = renpy.random.choice([True, False])

                    if not caughtpeekingpenelope:
                        scene s183a
                        with dissolve

                        u "(Damn, what I wouldn't give to touch her ass right now.)"

                        u "(I should stop peeking now, or I risk getting caught.)"
                    else:
                        jump caughte

                "Stop peeking":
                    pass

        "Don't peek":
            $ addPoint("bf", 1)

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

            u "Yeah, maybe it's like the costume of two lovers, you know... historically speaking."

            scene s182
            with dissolve

            pe "Haha, I'm sure that's the case."

            if penoutfits < 3:
                pe "Let's continue, I wanna try another outfit."

            else:
                pe "Are you ready to buy an outfit?"

        "Agree":
            $ addPoint("bro", 1)

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
    if try6done:
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

            scene s180 # pen changing bad view
            with dissolve

            u "(Fuck... if I could just stick my head through a bit further, I could get a way better view."

            menu:
                "Risk it":
                    $ caughtpeekingpenelope = renpy.random.choice([True, False])

                    if not caughtpeekingpenelope:
                        scene s180a # pen changing good view
                        with dissolve

                        u "(In all fairness, whenever I watch porn, the person getting caught spying gets to fuck the girl right afterwards.)"

                        u "(Still... I better stop peeking now, it's too risky.)"
                    else:
                        jump caughtf

                "Stop peeking":
                    pass

        "Don't peek":
            $ addPoint("bf", 1)

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

            u "Oh come on, Penelope. I wanna see."


            pe "Sorry but... I'm gonna get dressed again."


            u "Alright, fine."

        "Fine.":
            $ addPoint("bf", 1)

            u "Okay, fine."

            u "Then get dressed quickly, so that you can see my costume."

            pe "Yeah, just give me a minute."

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

    jump v1_caughtContinue

label caughtb:
    scene s168a # Aubrey changing good view
    with dissolve

    u "(Damn, what I wouldn't give to touch her ass right now.)"

    u "(I should stop peeking now, or I risk getting caught.)"

    scene s167
    with dissolve

    jump v1_caughtContinue

label caughtc:
    scene s172a # Aubrey changing good view
    with dissolve

    u "(In all fairness, whenever I watch porn, the person getting caught spying gets to fuck the girl right afterwards.)"

    u "(Still... I better stop peeking now, it's too risky.)"

    scene s171
    with dissolve

    jump v1_caughtContinue

label v1_caughtContinue:
    au "[name], did I just see you pull your head out from underneath the dividers?"

    scene s177d # closeup aubrey outside in regular clothes angry
    with Fade (1,0,1)

    au "[name]? Did you just peek on me?"

    menu:
        "Apologize":
            $ addPoint("bf", 1)
            $ caughtpeekingaubreycounter = True

            scene s177e
            with dissolve

            u "Aubrey, I'm so sorry. It was just..."

            u "...so tempting."

            scene s177d # aubrey disappointed
            with dissolve

            au "Honestly, it's okay. It was just kinda surprising."

            au "How about we just buy a costume and get going?"

        "Deny it":
            $ addPoint("tm", 1)

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


    jump v1_caughtContinue_pen

label caughte:
    scene s183a
    with dissolve

    u "(Damn, what I wouldn't give to touch her ass right now.)"

    u "(I should stop peeking now, or I risk getting caught.)"

    scene s167
    with dissolve

    jump v1_caughtContinue_pen

label caughtf:
    scene s180a # pen changing good view
    with dissolve

    u "(In all fairness, whenever I watch porn, the person getting caught spying gets to fuck the girl right afterwards.)"

    u "(Still... I better stop peeking now, it's too risky.)"

    scene s171
    with dissolve

    jump v1_caughtContinue_pen

label v1_caughtContinue_pen:
    pe "Oh my god! [name], did I just see you pull your head out from underneath the dividers??"

    pe "Did you spy on me??"

    scene s186 # closeup pen outside in regular clothes upset
    with Fade (1,0,1)

    show screen influenceTutorial
    pe "[name]! What were you thinking?!"

    menu:
        "Apologize":
            hide screen influenceTutorial
            $ addPoint("bf", 1)

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

        "Deny it":
            hide screen influenceTutorial
            $ addPoint("tm", 1)

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

label v1_gocostumes:
    call screen costumes

# Purchase with Aubrey

label buy1:
    $ costume = 1
    jump buyCont
label buy2:
    $ costume = 2
    jump buyCont
label buy3:
    $ costume = 3
    jump buyCont

label buyCont:
    if caughtpeekingaubrey:
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

        jump v1_endShop

label buy1p:
    $ costume = 1
    jump v1_buyContinuePenelope
label buy2p:
    $ costume = 2
    jump v1_buyContinuePenelope
label buy3p:
    $ costume = 3
    jump v1_buyContinuePenelope

label v1_buyContinuePenelope:
    if caughtpeekingpenelope:
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

        jump v1_endShop

label eve1:
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

                "Be funny":
                    $ evelynnumber = False

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

        "Leave":
            $ addPoint("bf", 1)

            scene s188d
            with dissolve

            u "Thank you, have a nice day."

            scene s188b # eve smiling
            with dissolve

            ev "You too."

label v1_endShop:
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

jump v3start