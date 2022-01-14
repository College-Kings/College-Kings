init python:
    # Emily's messages
    def v1_reply1():
        grant_achievement("no_hard_feelings")

        emily.messenger.newMessage(_("Cool :)"))

    def v1_reply2():
        grant_achievement("open_wound")

        add_point(KCT.TROUBLEMAKER)
        emily.messenger.newMessage(_("Ugh :/"))

    # Julia messages
    def v1_reply3():
        add_point(KCT.BOYFRIEND)

    def v1_reply4():
        add_point(KCT.BRO)

    # Lauren messages
    def v1_reply5():
        add_point(KCT.BOYFRIEND)

    # Lauren messages
    def v1_reply6():
        add_point(KCT.BOYFRIEND)
        lauren.messenger.newMessage(_("Cool :)"))

    def v1_reply7():
        add_point(KCT.TROUBLEMAKER)
        lauren.messenger.newMessage(_("Idk, it's just feels kinda weird now. Can we please just talk tomorrow?"))
        lauren.messenger.addReply(_("Fine"))
        lauren.messenger.newMessage(_(":)"))

label v1start:
label starta: #for compatibility only
    if config.developer:
        show screen bugTesting_Overlay

    show screen fightDamage
    show screen fantasyOverlay
    
    $ options = [
        {
            "option": "Travel to the maldivas",
            "votes": [chloe, mc]
        },
        {
            "option": "Rock climb the everest",
            "votes": [chloe, mc]
        }
    ]


    # call screen would_you_rather("Would you rather eat your dad or your mum", options)
    play music "music/msexy.mp3"
    
    scene s0a
    with dissolve

    em "I know what I did was bad..."

    em "But I'll do anything to make it up to you."

    scene s0b
    with dissolve

    em "Anything."

    hide screen fantasyOverlay
    stop music fadeout 3

    scene s1
    with Fade(1, 0, 1)

    "Honey?"

    scene s1b
    with dissolve

    play music "music/m15punk.mp3"

    $ mc.username = name = renpy.input(_("What's your name?"), default=_("Alex")).strip() or _("Alex")

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

    scene v1jul1a
    with dissolve
    ju "Look at you, all grown-up. I'm so proud of you."

    scene s3f
    with dissolve

    ju "You better not forget to come visit."
    u "I'll think about it, if you make lasagna."

    scene v1jul1a
    with dissolve

    ju "I'm sure that could be arranged."

    ju "Anyway, we should get ready, you don't wanna be late on your first day of college!"
    
    scene v1jul1
    with dissolve

    u "Oh, you're dropping me off? I was gonna take the train."

    scene v1jul1a
    with dissolve

    ju "No way you're robbing me of the chance to embarrass you in front of your new friends."

    scene v1jul1
    with dissolve

    u "Thanks, Julia... I'll be 20 minutes."

    scene s11
    with Fade(1, 0, 1)
    
    u "(I better not lose this bag, Julia loves it.)"

    play sound "sounds/vibrate.mp3"

    u "(Huh?)"
    
    # Emily's messages
    $ emily.messenger.newMessage(_("Hey...\nI know we haven't talked much after we broke up, but I just wanted to let you know that I didn't get into Stanford, so I'll be going to San Vallejo as well.\nGuess I'll see you there. :)"))
    $ emily.messenger.addReply(_("Yeah... I'll see you there."), v1_reply1)
    $ emily.messenger.addReply(_("You cheated on me.\nGo to hell!"), v1_reply2)

    show screen tutorial([
        "This is the phone screen. You can access your phone whenever the phone icon in the top right corner appears.",
        "Blue dots show notifications. New notifications are usually accommpanied by a buzz sound. Currently you have a new message waiting for you.",
        "How you reply to messages matters just as much as any other decision.",
        "Over the course of the game you will also unlock all kinds of new apps, such as statistics or social media platforms.",
        "Lastly, if you ever need to get to the homescreen, just click the bottom border of the phone, or the phone icon.",
    ])
    call screen phone
    hide screen tutorial
    
    stop music fadeout 3
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

    u "Mhm..."

    hide s14a
    show s14
    with dissolve

    ju "You're not planning on joining one of those, are you?"

    show screen tutorial([
        "Your decisions strongly influence the way the story progresses and how other characters perceive you.",
        "With each choice you'll either gain Bro, Boyfriend or Troublemaker points.",
        "Bros put the squad first, boyfriends show strong affinity towards a few selected individuals and troublemakers seek thrills and take risks.",
        "These points are then used to identify your Key Character Trait (KCT).  Each KCT will unlock different possibilities and choices, but you can only have one active at a time.",
        "You can read more about each individual KCT in the Stats app on your phone.",
    ])
    
    menu:
        "Could be fun":
            hide s14
            show s14a
            with dissolve
            $ add_point(KCT.TROUBLEMAKER)

            u "I don't know... it might be fun."

        "No":
            hide s14
            show s14a
            with dissolve
            $ add_point(KCT.BOYFRIEND)

            u "No, I don't think so, Julia."

    hide screen tutorial

    label aa_db: #for compatibility only
    hide s14a
    show s15
    with dissolve

    $ stats_app.unlock()

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

    stop music fadeout 3

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

    stop music fadeout 3

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

    ca "Next time, Mommy won't be there to save you, asshole."

    stop music fadeout 3

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

    label ad_db: #for compatibility only
    scene s39
    with dissolve

    u "(Damn... she was really cute. Hopefully I'll get to see her again.)"

    u "(I should probably go to my induction class right now.)"

    stop music fadeout 3

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

    ry "And...their President is the current Fight King."

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

            $ elijah.relationship = Relationship.MAKEFUN
            $ add_point(KCT.TROUBLEMAKER)

            scene s46b
            with dissolve
            el "..."

        "Stay quiet":
            pass

    label ag_da: #for compatibility only
    scene s84a
    with dissolve

    ro "Here at San Vallejo College most courses start their first year with the same three classes: Biology, Economics and History."

    ro "Alcohol, smoking and any form of violence whilst on College grounds is strictly forbidden."

    ro "Classes start tomorrow, so you'll have plenty of time to explore the campus today."

    ro "Now, let's move on to some of the boring administrative stuff..."

    stop music fadeout 3
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
            $ add_point(KCT.BOYFRIEND)

            scene s50a
            with dissolve

            u "It really is."

            u "Does that mean not all girls here are into the fighting?"

            scene s52
            with dissolve

            la "Not at all, pretty much any girl that's part of the Deer hates it."

        "Disagree":
            $ add_point(KCT.TROUBLEMAKER)

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

    label af_db: #for compatibility only
    scene s51a
    with dissolve
    u "The Deer?"

    scene s52
    with dissolve
    la "They're one of the two sororities at San Vallejo. My sister Autumn is their President, so I know most of them quite well."

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
            $ add_point(KCT.BOYFRIEND)

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
            $ add_point(KCT.BOYFRIEND)

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

    label aj_db: #for compatibility only
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

    stop music fadeout 3

# Part 5 Free roam in the halls
    scene s50 # hallway 1 without freeroam
    with Fade(1, 0, 1)

    u "(I should probably go to my new dorm, but I might as well explore for a bit beforehand.)"

    play music "music/mchill2.mp3"

    scene s50 # freeroam
    with dissolve

    $ julia.messenger.newMessage(_("Hey honey,\nenjoy your time in college.\nStay safe and don't forget to visit me.\nLove you"), force_send=True)
    $ julia.messenger.addReply(_("Love you too."), v1_reply3)
    $ julia.messenger.addReply(_("Thanks, Julia :)"), v1_reply4)

    play sound "sounds/vibrate.mp3"
    
    # Enter free roam
    show screen tutorial([
        "At certain parts of the game, you'll unlock free roam.",
        "During free roam, you choose where you go and who you want to talk to next.",
        "You will also be able to use your phone and you might just find some hidden content."
    ], position=(1050, 700))
    call screen v1_freeRoam1_1
    with dissolve
    label fr1a2: #for compatibility only

    label v1_freeRoam1_riley:
        $ freeroam1.add("riley")
        
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
            "She's hot":
                $ add_point(KCT.BRO)

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

            "She seems nice":
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
        $ freeroam1.add("elijah")

        scene s50el
        u "Hey, you're Elijah right?"

        if elijah.relationship <= Relationship.MAKEFUN:
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
                $ add_point(KCT.TROUBLEMAKER)

                scene s50el2a
                with dissolve

                u "Sooo... the nerds?"

                scene s50el1
                with dissolve

                el "How dare you defy the frogs like that?!"

                el "Just get out of my face."

            "That's cool":
                $ add_point(KCT.BOYFRIEND)

                scene s50el2a
                with dissolve
                u "I think that's pretty cool."

                scene s50el1
                with dissolve

                el "It's not \"cool\"! It's prestigious and an incredible opportunity."

                el "Now go and bother someone else."
                
        call screen v1_freeRoam1_1

    label v1_freeRoam1_elijah2:
        
        scene s50el1a
        u "Elijah?"

        scene s50el1
        with dissolve
        el "Leave me alone."
        
        call screen v1_freeRoam1_1

    label v1_freeRoam1_chris:
        $ freeroam1.add("chris")
    
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
       
        call screen v1_freeRoam1_2

    label v1_freeRoam1_nora:
        $ freeroam1.add("nora")
    
        scene s56no1a
        u "Hey, could you tell me where the dorms are?"

        scene s56no1
        with dissolve
        no "They're right through the doors behind you."

        menu:
            "Flirt":
                $ add_point(KCT.TROUBLEMAKER)
                $ nora.relationship = Relationship.MOVE

                scene s56no1a
                with dissolve

                $ grant_achievement("keep_it_moving")

                u "Actually, I knew that. I just wanted to talk to you 'cause you're really cute."

                scene s56no1
                with dissolve
                no "Look, I've got a boyfriend, so keep it moving."

            "Leave":
                scene s56no1a
                with dissolve

                u "Thanks."

    call screen v1_freeRoam1_2

    label v1_freeRoam1_nora2:
        scene s56no1a
        
        u "Uhm..."
        if nora.relationship >= Relationship.MOVE:
            scene s56no1
            with dissolve
            no "Dude, keep it moving."

        else:
            scene s56no1
            with dissolve
            no "I'm busy."

        call screen v1_freeRoam1_2

    label v1_freeRoam1_aubrey:
        $ freeroam1.add("aubrey")
    
        if config_censored:
            call screen censoredPopup("v1_freeRoam1_aubrey2")

        scene adamaubrey36
        stop music fadeout 3
        play music "music/msexy.mp3"
        show adam1

        au "Ohhh shit, that feels good!"
        u "(Oh my god... she's so fucking hot.)"
        au "YESSSSS, FASTER!"
        u "(I should probably stop peeking, before I get caught.)"
        
        stop music fadeout 3
        call screen v1_freeRoam1_3

    label v1_freeRoam1_aubrey2:
        scene s58
        u "I shouldn't risk peeking again."
        call screen v1_freeRoam1_3

label efra:
    scene s59
    stop music fadeout 3
    play sound "sounds/knock.mp3"
    
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

    u "Oh, that's cool."

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
            $ add_point(KCT.TROUBLEMAKER)

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

        "The Wolves sound sick":
            $ add_point(KCT.BRO)

            scene s64a
            with dissolve
            u " Honestly, after listening to you, the Wolves sound sick!"

            scene s63d
            with dissolve

            imre "Yeahhhh! They fucking are man. That's what I've been trying to tell you."

    label an_bd: #for compatibility only
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

    label phonef: #for compatibility only
    imre "It better be a girl."

    scene s61a
    with dissolve

    $ lauren.messenger.addReply(_("Hey Lauren, would you want to hang out with me and my friends tonight?"))
    $ lauren.messenger.newMessage(_("Yeah sounds good :) Where do you wanna meet?"))
    $ lauren.messenger.addReply(_("Just come to dorm 109 at 8"))
    $ lauren.messenger.newMessage(_("Okay, will do"))
    $ lauren.messenger.addReply(_("See you later, cutie"), v1_reply5)
    $ lauren.messenger.addReply(_("Cool"))

    label v1_phoneCheck1:
        if lauren.messenger.replies:
            call screen phone
        if lauren.messenger.replies:
            "(I should reply to Lauren.)"

            scene s61
            with dissolve
            imre "Did you ask?"

            scene s61
            with dissolve
            u "Oops I forgot."

            jump v1_phoneCheck1

    label v1_phoneCheck2:
        if julia.messenger.replies:
            call screen phone
        if julia.messenger.replies:
            "(I should reply to Julia as well, by the way.)"
            jump v1_phoneCheck2

    scene s61a
    with dissolve

    u "Okay man, I did it."

    scene s61c
    with dissolve

    imre "Awesome! Get ready for a wild night, my man."

    label continueonea: #for compatibility only
    scene s65
    with Fade(1, 0, 1)
    stop music fadeout 3

    play sound "sounds/knock.mp3"
    pause 0.75

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

    if "riley" in freeroam1:
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

    label talktorib: #for compatibility only
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

        "Dodged a bullet there":
            $ add_point(KCT.TROUBLEMAKER)

            scene s73gr
            with dissolve

            u "Phew, dodged a bullet there."

            scene s72f
            with dissolve

            imre "Damn..."

    label ao_bd: #for compatibility only
    scene s72f
    with dissolve

    imre "Okay, it's your turn to dare someone, Lauren."

    scene s73bl
    with dissolve

    la "Riley, I dare you to let Imre slap your ass."

    scene s71cl
    with dissolve

    ri "Oh that's easy. Let's do it, Imre."

    scene s75
    with dissolve

    imre "Great idea, Lauren!"

    scene s75a
    with hpunch

    play sound "sounds/slap.mp3"
    pause 1.5

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
            $ add_point(KCT.TROUBLEMAKER)

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

    label ap_bd: #for compatibility only
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
        "Do it, or drink":
            $ add_point(KCT.BRO)

            scene s71ef
            with dissolve
            u "You gotta do the dare, or drink."

            scene s71cf
            with dissolve

            ri "Fine..."

            scene s77
            with dissolve

            " "

        "You're right":
            $ add_point(KCT.BOYFRIEND)
            
            scene s71ef
            with dissolve
            u "You're right, let's continue."

    scene s73cf
    with dissolve

    label ar_bd: #for compatibility only
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

    stop music fadeout 3

    ### Late night talk with Imre.
    scene s80
    with Fade(1, 0, 1)
    play music "music/msad.mp3"

    imre "Man, I can't wait to bang this Riley chick."

    menu:
        "Riley's mine":
            $ add_point(KCT.TROUBLEMAKER)

            scene s79b
            with dissolve

            u "What? I want Riley. You can have Lauren."

            scene s80e
            with dissolve

            imre "What the hell man?! I invited Riley. Back off."

            menu:
                "You're right, sorry":
                    $ add_point(KCT.BRO)

                    scene s79a
                    with dissolve

                    u "You're right, Riley is yours. I'm sorry."

                    scene s80a
                    with dissolve

                    imre "It's fine bro, I get it. She is really cute."

                "She wants me":
                    $ add_point(KCT.TROUBLEMAKER)

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

        "They're both hot":
            $ add_point(KCT.BRO)

            scene s79
            with dissolve
            u "Hahaha, to be honest they're both pretty hot."

    scene s80
    with dissolve

    imre "Oh man, we're gonna bang so many chicks this year. Trust me, all you need is confidence..."

label at_bd:
    imre "And to be part of a frat."

    if "aubrey" in freeroam1:
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

    stop music fadeout 3

    ### Sex dream
    label sexdream1: #for compatibility only
    show screen fantasyOverlay
    scene sda1  ### close to the kitchen counter
    with Fade (1,0,1)

    ri "Wow, you guys have a really nice house."

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

    if not _in_replay:
        if not config_censored:
            call screen nsfw_Toggle

        if config_censored:
            call screen censoredPopup("v1_nsfwSkipLabel1")

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
            $ sceneList.add("v1_riley")

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

                    image sdabj = Movie (play="images/v1/sdabj.webm", loop = True, image = "images/v1/sda4e")
                    image sdabjf = Movie (play="images/v1/sdabjf.webm", loop = True, image = "images/v1/sda4e")

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
            
label v1_nsfwSkipLabel1:
    hide screen fantasyOverlay

    stop music fadeout 3
    $ renpy.end_replay()

    ### Next morning in your dorm, Imre seems to be gone.
    if "v1_riley" in sceneList:
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
    stop music fadeout 3
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
            $ add_point(KCT.BOYFRIEND)

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

        "Bad roommates suck":
            $ add_point(KCT.BRO)

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
    stop music fadeout 3

    label au_bd: #for compatibility only
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
        "You could get any guy":
            scene s89d
            with dissolve
            u "I bet you could get any guy you want."

            scene s89f
            with dissolve
            la "Uhm... thanks. Not really though, haha."

        "Yet, you're here with me":
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

    label av_ad: #for compatibility only
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
        "I'm still in love with my ex":

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

        "I've broken into an Ikea":

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

label aw_bd:
    la "Right... almost forgot about that."

    la "I... I haven't actually had sex before."

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
        "You're really beautiful":
            $ add_point(KCT.BOYFRIEND)

            u "You know... you're really beautiful."

            scene s89
            with dissolve
            la "Awww."

        "You're not ugly":
            $ add_point(KCT.BRO)

            u "You know... you're not ugly."

            scene s89b
            with dissolve

            la "Wow, how flattering."

    scene s89k
    with dissolve

    label ax_bd: #for compatibility only
    u "(Is this the moment to kiss her?)"

    menu:
        "Kiss her":
            $ lauren.relationship = Relationship.MOVE

            if v1_laurenPoints == 2:
                scene s90
                with dissolve # kiss
                $ lauren.relationship = Relationship.KISS
                
                $ grant_achievement("romeo")

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

    label ay_bd: #for compatibility only
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

    if lauren.relationship >= Relationship.MOVE:
        u "(Fuck... why did I try to kiss her?! That just made everything weird.)"
    else:
        u "(Fuck... should I have kissed her? Now it's just weird between us.)"

    ### Back in your dorm with Imre
    stop music fadeout 3

    stop sound

    label next_scenea: #for compatibility prior to v10
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

    pause 1

    scene s96 #showing Imre in front of your bed looking down on you
    with dissolve

    imre "I take it your date didn't go as planned?"

    if lauren.relationship >= Relationship.KISS:
        scene s96a
        with dissolve
        u "I just don't get it..."

        u "I kissed her... and for a second she kissed me back."

        u "But then she pulled away and left."

        u "And now it's all just super weird."

    elif lauren.relationship >= Relationship.MOVE:
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

    label backtophone: #for compatibility only
    u "I guess..."

    scene s96c
    stop music fadeout 3
    play sound "sounds/vibrate.mp3"

    $ ryan.messenger.newMessage(_("Hey man, it's Ryan.\nThe Apes' rush party is tonight at 9. You're coming, right???"), force_send=True)
    $ ryan.messenger.addReply(_("Alright, but I'll only stay for a few hours."))
    $ ryan.messenger.newMessage(_("Haha, trust me, you're not gonna want to leave once you see all the hot chicks there."))
    $ ryan.messenger.newMessage(_("Just meet me in front of the Apes' frat house at 9."))
    $ ryan.messenger.addReply(_("Okay, will do."))

    label repeata:
        if ryan.messenger.replies:
            call screen phone
        if ryan.messenger.replies:
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

    stop music fadeout 3

    label nextscenef: #for compatibility only
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
    
    call screen v1_freeRoam2_1

label v1_freeRoam2_sam:
    $ freeroam2.add("sam")

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
    $ freeroam2.add("door")
    
    play music "music/mparty2.mp3"

    queue music [ "music/mparty3.mp3", "music/mparty4.mp3" ]
    
    scene s103

    ry "Alright man, I'm gonna look around, I'll see you in a bit."

    scene s103a

    u "Cool."

    u "(Great, now I'm all on my own.)"

    call screen v1_freeRoam2_2

label v1_freeRoam2_pool:
    if not "josh" in freeroam2:
        scene s102

        u "(I should talk to Josh first, I haven't seen him in a while.)"

        call screen v1_freeRoam2_2
    else:
        call screen v1_freeRoam2_3

label v1_freeRoam2_courtney:
    $ freeroam2.add("courtney")

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
    $ freeroam2.add("josh")

    scene fr2jo1a

    jo "[name]! I didn't know you're also going to San Vallejo. *sniff*"

    jo "This is uhhh... Aubrey!"

    scene fr2jo2a
    with dissolve

    au "Hey, nice to meet you."

    scene fr2jo2b
    with dissolve

    if "aubrey" in freeroam1:
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

    au "Oh no, I'm a junior, vice President of the Chicks actually."

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
                    $ add_point(KCT.TROUBLEMAKER)

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

                    scene fr2jo2a
                    with dissolve

                    au "He's the President of the Apes and the current Fight King."

                    au "I think he's upstairs, but I'm not sure."

                    scene fr2jo2b
                    with dissolve

                    u "Alright, I'll leave you guys alone and look around a bit more. Maybe I'll even talk to Grayson."

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

                    scene fr2jo2a
                    with dissolve

                    au "He's the President of the Apes and the current Fight King."

                    au "You'll never know, maybe if you meet some of the Apes, you'll change your mind about fighting."

                    scene fr2jo2b
                    with dissolve

                    u "(I doubt it, but I guess it won't hurt to talk to some of them.)"

                    u "Alright, I'll leave you guys alone and look around a bit more."

        "Ask if she likes fighters":
            $ add_point(KCT.BOYFRIEND)

            scene fr2jo2b
            with dissolve

            u "I've heard that all the Chicks are into fighters."

            scene fr2jo2c
            with dissolve

            au "I mean, I can't deny that most of the fighters are pretty sexy."

            au "They're ripped, confident and being able to beat other guys up certainly doesn't make them less attractive."

            au "Why are you asking? Are you planning on becoming a fighter?"

            menu:
                "I'll be the next Fight King":
                    $ add_point(KCT.TROUBLEMAKER)

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

                    scene fr2jo2a
                    with dissolve

                    au "He's the President of the Apes and the current Fight King."

                    au "I think he's upstairs, but I'm not sure."

                    scene fr2jo2b
                    with dissolve

                    u "Alright, I'll leave you guys alone and look around a bit more. Maybe I'll even talk to Grayson."

                "No, that's not for me":
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

                    au "He's the President of the Apes and the current Fight King."

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
    if not "josh" in freeroam2:
        scene s102

        u "(I should talk to Josh first, I haven't seen him in a while.)"

        call screen v1_freeRoam2_2
    else:
        call screen v1_freeRoam2_5

label v1_freeRoam2_camp:
    if not "josh" in freeroam2:
        scene s102

        u "(I should talk to Josh first, I haven't seen him in a while.)"

        call screen v1_freeRoam2_2

    else:
        play sound "sounds/vibrate.mp3"

        if not lauren.messenger.find_message("Hey :)\nSorry about today.\n\nCan we talk tomorrow?"):
            $ lauren.messenger.newMessage(_("Hey :)\nSorry about today.\n\nCan we talk tomorrow?"), force_send=True)
            $ lauren.messenger.addReply(_("Yeah, sure."), v1_reply6)
            $ lauren.messenger.addReply(_("What is there to talk about?"), v1_reply7)

        call screen v1_freeRoam2_4

label v1_freeRoam2_mason:
    $ freeroam2.add("mason")

    scene fr2ma1
    ma "Eyyyy, you're the kid that tried to fight Cameron yesterday!"

    scene fr2ma1a
    with dissolve
    u "What? I didn't-"

    scene fr2ma1b
    with dissolve

    jeremy "Damn, that takes balls, kid!"

    menu:
        "Yeah, he better watch out":
            $ add_point(KCT.TROUBLEMAKER)
            $ add_point(KCT.BRO)

            scene fr2ma1a
            with dissolve

            $ grant_achievement("big_mouth")
                
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

        "I didn't wanna fight him":
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
    $ freeroam2.add("katy")

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
    $ freeroam2.add("grayson")
    
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

    gr "We're building the Apes' legacy here. 10 years from now, I'll be the most successful Ape President in history."

    gr "And you could be the most successful vice President."

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
label fr2end: #for compatibility only

    stop music fadeout 3
    
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

    ry "I think that's Chloe, right? I talked to some of the Chicks and she's like their President."

    ry "Also, possibly the hottest girl I've seen in my life."

    u "And who's that guy she's talking to? Is that her boyfriend?"

    scene s108b
    with dissolve

    ry "Man, I don't know. Why don't you just go ask her yourself?"

    menu:
        "You're right, I'll talk to her":
            $ add_point(KCT.BRO)

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

        "She's occupied":
            scene s108c
            with dissolve

            u "I don't know... She's talking to someone right now and I don't wanna come off as rude."

            scene s108d
            with dissolve

            ry "I'm sure it's fine."

            scene s110 ### ryans hand on your back
            with dissolve

            pause 0.75

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

    label bd_bd: #for compatibility only
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
            $ add_point(KCT.BOYFRIEND)

            u "I'm really sorry for interrupting your conversation."

            scene s112b
            with dissolve

            cl "I should be thanking you for saving me. He literally spent the last 20 minutes talking about rocks."

            scene s112c
            with dissolve

            u "In that case, you're very welcome."

        "Make fun of him":
            $ add_point(KCT.BRO)

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

    label be_bd: #for compatibility only
    cl "Hey, do you wanna go outside and sit down? I could really use some fresh air."

    scene s112c
    with dissolve

    u "Yeah, sounds great."

    stop music fadeout 3

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

    scene s116a
    with dissolve
    
    scene s116
    with dissolve

    cl "Both of us then had to come to his office, so that the guy could apologize and give me my panties back right in front of the dean."

    cl "It was sooo embarrassing."

    scene s116a
    with dissolve

    menu:
        "Empathize":
            $ add_point(KCT.BOYFRIEND)

            u "Wow, that sounds awful."

            scene s116b
            with dissolve

            cl "It really was."

        "Poke fun":
            $ add_point(KCT.TROUBLEMAKER)

            u "Hahaha, sounds like the dean was into you."

            scene s116d
            with dissolve

            cl "Ewww. Don't say that, hahaha."

    scene s116c
    with dissolve

    label bf_bd: #for compatibility only
    u "So, you're the President of the Chicks, right?"

    scene s116b
    with dissolve

    cl "Yeah, I am."

    scene s116c
    with dissolve

    u "Are you close with Aubrey then? She told me she was the vice President."

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

    stop music fadeout 3

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

    pause 0.5
    scene s120a
    with dissolve
    pause 0.5

    stop music
    #####punch
    scene black
    $ renpy.movie_cutscene("v1/punchdemo.webm", loops=0)

jump v2start