init python:
    # Josh messages
    def v4_reply1():
        add_point(KCT.BRO)
        josh.messenger.newMessage(_("Dope"))
        josh.messenger.newMessage(_("Come by 995 Sereno Drive at 8, it's my friends house."))

    def v4_reply2():
        josh.messenger.newMessage(_("Aww, come on. You'll be back by 11."))
        josh.messenger.newImgMessage("images/v4/text1.webp")
        josh.messenger.newMessage(_("I told my friend Amber about you and she really wants to meet you."))
        josh.messenger.addReply(_("Alright, I'll come."), v4_reply1)
        josh.messenger.addReply(_("Josh, I don't know, man. I don't wanna be late."), v4_reply3)

    def v4_reply3():
        josh.messenger.newMessage(_("Remember how you told me in high school that you felt like you always missed out on all the crazy stories?"))
        josh.messenger.newMessage(_("Don't miss out now."))
        josh.messenger.addReply(_("Fine, I'll come. But I need to go before 11."), v4_reply4)
        josh.messenger.addReply(_("I can't, sorry."), v4_reply5)

    def v4_reply4():
        josh.messenger.newMessage(_("Dope"))
        josh.messenger.newMessage(_("Come by 995 Sereno Drive at 8, it's my friends house."))

    def v4_reply5():
        add_point(KCT.BOYFRIEND)
        josh.messenger.newMessage(_("This guy"))

label v4start:
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
        "You should be more careful":
            $ add_point(KCT.BOYFRIEND)

            scene s297a
            with dissolve

            u "Imre, you need to be more careful, man!"

            u "You can't just try and fight everyone, what if he had a knife?"

            scene s297d
            with dissolve

            imre "I told you, it wasn't a fair fight! I'll fuck him up when I get out."

            menu:
                "Let me help":
                    $ add_point(KCT.BRO)

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

                "That's a dumb idea":
                    $ add_point(KCT.BOYFRIEND)

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

        "Let's fuck him up":
            $ add_point(KCT.BRO)
            $ add_point(KCT.TROUBLEMAKER)

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

    label dp_ad: #for compatibility only
    stop music fadeout 3

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
            $ add_point(KCT.BRO)
            $ add_point(KCT.BOYFRIEND)

            scene s303c
            with dissolve

            u "Yeah... I'm sorry. I shouldn't have acted out like that. Tomorrow I'll talk to Ryan and make things right."

            scene s303
            with dissolve

            ri "I think that'd be good."

            scene s303a
            with dissolve

        "Blame Ryan":
            $ add_point(KCT.TROUBLEMAKER)

            scene s303c
            with dissolve

            u "That's just 'cause Ryan was completely out of line..."

            scene s303b
            with dissolve

            ri "Right... sorry for bringing it up."

            scene s303c
            with dissolve

    label dq_bd: #for compatibility only
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

    if riley.relationship.value >= Relationship.MOVE.value:
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

    label continuev: #for compatibility only
    ri "It's getting quite late, I should probably head back to my dorm."

    menu:
        "Ask her to sleep here":
            scene s304 # showing you sitting on bed, riley stood up, you looking at her, she's walking towards the door but still close to the bed
            with dissolve

            u "Or... you could sleep here. I mean, Imre's bed certainly isn't taken tonight."

            scene s304a # riley turning around smile
            with dissolve

            ri "Haha, I don't wanna find out what's underneath those covers."

        "Don't ask":
            scene s304
            with dissolve

            u "Yeah, thank you for coming though."

            scene s304a
            with dissolve

            ri "Not a problem at all."

    label dr_bd: #for compatibility only
    stop music fadeout 3

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

    stop music fadeout 3

    scene s225a # already in the game, no need to render again
    with flash
    hide screen fantasyOverlay

    u "*Breathing heavily*"

    u "(What the hell was that dream? Ryan really made me second guess how things are going with Chloe.)"

    u "(I should talk to her tomorrow.)"

############## END CHLOE DREAM


########## NEXT MORNING (SATURDAY)

    scene s310 # you yawning in bed in the morning
    with Fade (1,0,1)

    u "*Yawn*"

    if meetjulia:
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
            "Someone punched me":
                $ add_point(KCT.BOYFRIEND)

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

            "It was an accident":
                $ add_point(KCT.TROUBLEMAKER)

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

        label du_bd: #for compatibility only
        stop music fadeout 3

        ######### THE FOLLOWING IMAGES HAVE TO BE RENDERED WITH NOT BACKGROUND AS A VIDEO OF MOVING ROADS WILL BE INSERTED
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

            jump jucon2

        label juaubrey:
            $ girl = "Aubrey"

            u "There's this girl called Aubrey..."

            u "She's really fun and kinda wild. She just does stuff you wouldn't expect."

            jump jucon1

            label julauren:

            $ girl = "Lauren"

            u "There's this girl called Lauren..."

            u "She's really sweet, but also funny."

            jump jucon1

        label juriley:
            $ girl = "Riley"

            u "There's this girl called Riley..."

            u "She's fun, but also really honest and that makes her great to talk to."

            jump jucon1

        label juemily:
            $ girl = "Emily"

            u "Actually, it's Emily..."

            hide s316a
            show s316c
            with dissolve

            $ grant_achievement("relight_the_fire")
                
            ju "Emily? I thought you guys broke up?"

            hide s316c
            show s316d
            with dissolve

            u "Yeah, but I think she's changed. She seems to be really sorry for what she did."

            u "I don't know... we just get along so well."

            jump jucon1

        label jupenelope:
            $ girl = "Penelope"

            u "There's this girl called Penelope..."

            u "She's a little quirky, but I really like that about her. It's different."

            jump jucon1

        label jucon1:
            hide s316a
            hide s316d
            show s316
            with dissolve

            ju "Aww honeeey! That sounds great, I'm really happy for you."

            hide s316
            show s316a
            with dissolve

            u "Thanks, Julia."

        label jucon2:
            stop music fadeout 3

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

            scene s321 # FIrst person: looking at closed changing room door
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
                    
                    $ grant_achievement("rematch")

                    u "Yeah, you're right. Maybe I could give it to her when we talk about what Ryan said."

                    ju "That's a great idea, honey."

                "Don't buy it":

                    u "Uhm... I don't know. I wanna talk to her about what Ryan said first."

                    ju "Alright, honey. It was just an idea."

                    jump dv_dd

        else:
            scene s325b # you lookign at shop window with cool volley
            with dissolve

            u "(Chloe would probably love this volleyball.)"

            scene s326
            with dissolve

            menu:
                "Buy it":
                    $ volleyball = True

                    u "Hold up, Julia. I wanna buy this volleyball as gift for... a friend."

                    ju "Alright, honey."

                "Don't buy it":
                    $ volleyball = False

                    u "(I should probably talk to her about what Ryan said first and clear things up.)"

                    jump dv_dd

        label dv_cd: #for compatibility only
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

        label dv_dd:
            scene s328 # Showing you and Julia in the car driving back
            with Fade (1,0,1)

            pause 0.5

            scene s329 # you talking to juliaa (very close, about to hug)
            with Fade (1,0,1)

            ju "Thanks for coming along, honey. It was really nice to see you."

            scene s329a # hugging
            with dissolve

            u "Yeah Julia, it was fun. I'll see you again soon."

    else:
        scene s310a
        with dissolve

        u "(Damn, I still need to finish my essay on transition slides...)"

        scene s311 # you working on your laptop at your desk transition slide : It's Saturday 1 pm
        with Fade (1,0,1)

        u "(Alright, all finished.)"

    stop music fadeout 3

    scene s330
    with Fade (1,0,1)### you sitting on your bed with your phone in your hand //

    u "(I should text Chloe and see if she wants to meet up... I need to find out if there's any truth in what Ryan said.)"

    $ chloe.messenger.addReply(_("Hey Chloe, any chance you can meet up in a bit?"))
    $ chloe.messenger.newMessage(_("I'm really busy today, but I could do tonight after 11 or so."))
    $ chloe.messenger.addReply(_("Alright, cool. I'll be at yours for 11"))
    $ chloe.messenger.newMessage(_("Sounds good :)"))

    play music "music/mindie4.mp3"

    label phonev:
        if chloe.messenger.replies:
            call screen phone
        if chloe.messenger.replies:
            u "(I should message Chloe about meeting up later.)"
            jump phonev
    
    scene s330a # same as 330 but you looking up
    with dissolve

    u "(Shit, I just remembered that I still need a book for Ms. Rose's class...)"

    u "(The library should have it.)"

    #anchor
    stop music fadeout 3

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

    if toldlauren:
        $ add_point(KCT.TROUBLEMAKER)

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
                scene s334c
                with dissolve

                u "I'm sorry and I can see why Lauren would be upset."

                u "But... I can't change what happened, I was just trying to be honest."

                u "You have to believe me. I care about Lauren, I'd never do anything to hurt her."

                if kct == "loyal":
                    call screen kct_popup

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

                    jump autumnsita

                else:
                    $ autumn.relationship = Relationship.MAD
                    scene s334b
                    with dissolve

                    au "Right. Well actions speak louder than words, [name]."

                    au "Now please leave me alone."

                    scene s334c
                    with dissolve

                    u "Fine. I'll sit somewhere else."

                    jump readmontagea

            "Sit somewhere else":
                $ autumn.relationship = Relationship.MAD

                jump ea_b


    elif laurentoofar:
        $ add_point(KCT.TROUBLEMAKER)

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
                scene s334c
                with dissolve

                u "I'm sorry and I understand why Lauren is upset."

                u "I just got carried away in the moment... I never meant to make her uncomfortable."

                u "You have to believe me. I care about Lauren, I'd never do anything to hurt her."

                if kct == "loyal":
                    call screen kct_popup

                    $ autumn.relationship = Relationship.FRIEND
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

                    jump autumnsita

                else:
                    $ autumn.relationship = Relationship.MAD
                    
                    scene s334b
                    with dissolve

                    aut "Right. Well actions speak louder than words, [name]."

                    aut "Now please leave me alone."

                    scene s334c
                    with dissolve

                    u "Fine. I'll sit somewhere else."

                    jump readmontagea

            "Sit somewhere else":
                $ autumn.relationship = Relationship.MAD

                jump ea_b

    elif lauren.relationship.value < Relationship.GIRLFRIEND.value: #if not a girlfriend, but not because messed up date
        $ add_point(KCT.BOYFRIEND)
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

        jump autumnsita

    else:
        $ add_point(KCT.BOYFRIEND)
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

label ea_b:
    $ autumn.relationship = Relationship.MAD
    scene s334c
    with dissolve

    u "Fine. I'll sit somewhere else."

    jump readmontagea


label eb_ad: #for compatibility only
label ea_ad: #for compatibility only
label autumnsita:
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

label readmontagec: #for compatibility only
label readmontagea:
    stop music fadeout 3

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
            $ add_point(KCT.BRO)

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

        "Ignore him":
            $ add_point(KCT.TROUBLEMAKER)

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

    label ec_bd: #for compatibility only
    ry "I didn't mean to attack you like that. I just wanted to let you know about the things that I've heard."

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

    stop music fadeout 3
    scene s342 # in front of cafe
    with Fade (1,0,1)

    play music "music/mhappy.mp3"

    queue music [ "music/mlove.mp3" ]

    pause 0.5

    scene s343 # First person inside cafe # show penelope with coffe on laptop
    with dissolve

    if not (not costumeaubrey and v2_caughtpeeking and not v2_caughtpeekingcounter): # did not have bad outcome when shopping with penelope
        label continueaa: #for compatibility only
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
            "Magic Powers":
                $ add_point(KCT.BRO)

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

            "I didn't":
                $ add_point(KCT.BOYFRIEND)

                scene s349d
                with dissolve

                u "I didn't, but I'm glad I came now."

                scene s349c
                with dissolve

                pe "Well, me too! Wanna sit down?"

                scene s349d
                with dissolve

                u "Yeah, sure."

    elif (not costumeaubrey and v2_caughtpeeking and not v2_caughtpeekingcounter): # caught
        u "(Shit, Penelope's here. I wonder if she's still mad at me...)"

        u "(Maybe I should buy her something and apologize for peeking on her.)"

        scene s344 # in front of counter
        with dissolve
        clerk "Hello sir, what I can do for you?"

        menu:
            "Buy Penelope a muffin":
                $ add_point(KCT.BOYFRIEND)
                $ muffin = True
                $ v2_caughtpeekingcounter = True

                scene s344a
                with dissolve

                $ grant_achievement("keen_eye")

                u "Can I get a muffin and a coffee please?"

                scene s344
                with dissolve

                clerk "Coming right up, sir."

            "Buy Penelope a coffee":
                scene s344a
                with dissolve

                u "Two coffees please."

                scene s344
                with dissolve

                clerk "Coming right up, sir."

        label ed_bd: #for compatibility only
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

        if muffin:
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
                    $ add_point(KCT.BOYFRIEND)

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
                            $ add_point(KCT.TROUBLEMAKER)
                            $ penelopekiss = True

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

                            jump continueac

                        "Don't kiss her":
                            jump eg_b

                "Leave it":
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
            "Magic Powers":
                $ add_point(KCT.BRO)

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

            "I didn't":
                $ add_point(KCT.BOYFRIEND)

                scene s345g
                with dissolve

                u "I didn't, but I'm glad I came now."

                scene s345f
                with dissolve

                pe "Well, me too! Wanna sit down?"

                scene s345g
                with dissolve

                u "Yeah, sure."

    label ej_bd: #for compatibility only
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
        "We should watch some":
            $ add_point(KCT.TROUBLEMAKER)

            u "You know, we should watch some together sometime."

            scene s350k
            with dissolve

            pe "*Laughs* Ewww... I don't think we should."

            scene s350l
            with dissolve

            u "The offer still stands, if you change your mind."

            scene s350k
            with dissolve

            pe "Right, thank you."

        "You should try it":
            $ add_point(KCT.BRO)

            u "You know, you should try it sometime."

            scene s350k
            with dissolve

            pe "*Laughs* I don't know, I don't think I'd like it."

            scene s350l
            with dissolve

            label ek_ad: #for compatibility only
            u "Haha, I think you'd be surprised."

    scene s350
    with dissolve

    pe "I have to go now and meet my friend. It uhm, it was nice to see you though."

    menu:
        "You wanna go bowling?":
            scene s350a
            with dissolve

            u "It was nice to see you too."

            u "Hey, you wanna go bowling with me sometime next week?"

            scene s350d
            with dissolve

            pe "I don't know, I have sooo much studying to do..."

            menu:
                "Encourage her":
                    $ add_point(KCT.BOYFRIEND)
                    $ bowling = True

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

                "Tease her":
                    $ add_point(KCT.BRO)
                    $ bowling = False

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

        "Yeah, it was nice":
            $ bowling = False

    scene s350a
    with dissolve

    u "Yeah, it was nice to see you too."

    scene s350
    with dissolve

    pe "Bye bye, I'll see you later."

    scene s350a
    with dissolve

    u "Yeah, see you later."

    jump el_ad

    #### After cafe

label continueac:
    scene s351 # you walking back
    with fade

    u "(Shit, that didn't go as planned...)"

    jump continueab

label el_ad:
    scene s351
    with fade

    u "(I wonder what Penelope was doing on that laptop...)"

label continueab:
    stop music fadeout 3

    play sound "sounds/vibrate.mp3"

    play music "music/m9punk.mp3"

    $ josh.messenger.newMessage(_("Hey man, you wanna hang out with me and some friends tonight?"), queue=False)
    $ josh.messenger.addReply(_("Uhh, sure."), v4_reply1)
    $ josh.messenger.addReply(_("I'm meeting a friend at 11, so I can't really."), v4_reply2)

    label phonew:
        if josh.messenger.replies:
            call screen phone
        if josh.messenger.replies:
            u "(I should probably reply to my messages.)"
            jump phonew

    if josh.messenger.sent_messages[-2].reply and josh.messenger.sent_messages[-2].reply.message == "I can't, sorry.":
        u "(Fucking hell, I forgot how persistent Josh could be...)"
        jump jorepb

    else:
        u "(Okay, I need to make sure that I don't forget about meeting Chloe.)"

    label jorepa: #for compatibility only
    stop music fadeout 3
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

    if josh.messenger.sent_messages[-2].reply and josh.messenger.sent_messages[-2].reply.message == "Alright, I'll come.":
        jo "Picture of Amber did it, eh?"

        scene s353b
        with dissolve

        u "Oh, shut up."

        scene s353a
        with dissolve

        jo "Hahaha."

    else:
        jo "Come in."

    label continueae: #for compatibility only
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
        "I can move":
            $ add_point(KCT.BOYFRIEND)
            $ add_point(KCT.BRO)

            scene s359a
            with dissolve

            u "Oh, I can move if you want."

            scene s359
            with dissolve

            jo "Hahaha, buddy I'm just kidding, stay put."

        "It's my spot now":
            $ add_point(KCT.TROUBLEMAKER)

            scene s359a
            with dissolve

            u "Yeah, I guess it's my spot now."

            scene s359
            with dissolve

            jo "Damn, alright. Hahaha."

    label en_ad: #for compatibility only
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
        "I'll join the Wolves":
            $ add_point(KCT.BRO)

            u "I'll join the Wolves."

            scene s361b # josh looking at Kim happy
            with dissolve

            jo "See? I knew he was a fighter."

        "I don't know yet":
            $ add_point(KCT.BOYFRIEND)

            u "I don't know yet."

            scene s360a # kim laughing at you
            with dissolve

            ki "Ha! Classic Frog."

    label eo_bd: #for compatibility only
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
        "Sounds good":
            $ add_point(KCT.BRO)

            scene s361g
            with dissolve

            u "Cool, sounds good."

        "I should stop here":
            $ add_point(KCT.BOYFRIEND)

            scene s361f
            with dissolve

            u "Uhm, actually... I should stop here. I really have to go see my friend soon and I don't wanna be too drunk."

            scene s357
            with dissolve

            am "Oh come on, just stay a bit longer. You never know what you might miss out on."

            menu:
                "Alright, just for a bit":
                    $ chloe.relationship = Relationship.MAD
                    scene s357a
                    with dissolve

                    u "Alright, I'll stay a bit longer, let's play."

                    scene s357
                    with dissolve

                    am "Good choice."

                "Sorry, I really can't":
                    scene s357a
                    with dissolve

                    u "Sorry, I really gotta go. But maybe I'll uhm... come back later."

                    jump jorepb

    label jonewe: #for compatibility only
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
            $ add_point(KCT.BRO)

        "Drink three sips":
            $ add_point(KCT.BOYFRIEND)
            
            u "I'll drink."

            scene jomon5 # you drinking
            with dissolve

            pause 0.5

            scene s357
            with dissolve

            am "Oh come on, I wanna see you do a handstand."

            scene s357a
            with dissolve

    label ep_a: #for compatibility only
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
                    $ add_point(KCT.TROUBLEMAKER)
                    $ amber.relationship = Relationship.KISS

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

                "Don't kiss her":
                    $ add_point(KCT.TROUBLEMAKER)

                    play sound "sounds/spit.mp3"

                    scene jomon15a # spits out lemon
                    with dissolve

                    u "*Spits*"

                    play sound "sounds/phonealarm.mp3"

                    scene jomon15c # you pull away and look down
                    with dissolve

                    "*Phone alarm ringing*"

        "Kim":
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
                    $ add_point(KCT.TROUBLEMAKER)

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

                "Don't kiss her":
                    $ add_point(KCT.TROUBLEMAKER)

                    play sound "sounds/spit.mp3"

                    scene jomon17a # spits out lemon
                    with dissolve

                    u "*Spits*"

                    play sound "sounds/phonealarm.mp3"

                    scene jomon17c # you look down at your phone
                    with dissolve

                    "*Phone alarm ringing*"

    label es_bd: #for compatibility only
    scene s362 # looking at your phone # chloe Alarm
    with dissolve

    u "(Shit, I gotta go meet Chloe!)"

    stop sound

    u "*Drunk* Guys, I really gotta go."

    u "*Drunk* Maybe I- I'll come back later."

    stop music fadeout 3

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
            $ add_point(KCT.TROUBLEMAKER)

            scene s370c
            with dissolve

            u "*Drunk* You're lying! Yeah sure, the hottest girl in school wants me, the freshman who got beaten up at his first college party."

            u "*Drunk* Pretty realistic, isn't it?!"

            scene s370d # chloe sad desperate
            with dissolve

            cl "[name], I don't care about the fighting, or any of that shit. What Grayson did to you was pathetic. I like you 'cause you were funny and kind and ... and you cared."

            scene s370e
            with dissolve

        "Ask about the punch":
            scene s370c
            with dissolve

    label eu_b: #for compatibility only
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

    stop music fadeout 3

    " "

    u "Oh shit..."

jump v5start