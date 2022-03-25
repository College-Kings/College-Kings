
# TO DO LIST:
#() Add image names to scenes for all name2 labels (search for "scene #")

#FPP Show Aubrey, Looking at mc, happy smile, mouth open

# Free Roam 4, Screens

# Show("confirm", message="Are you sure you want to end the free roam?", yes_action=[Hide("confirm"), Jump("fr6end")])


# TOP: xalign 0.5
# RIGHT: align (1.0, 0.5)
# BOTTOM: align (0.5, 1.0)
# LEFT: yalign 0.5

label v10_charity_freeroam:
    # -MC arrives at the charity event and prior to the freeroam we have an image and a dialog line from MC-
    scene ent7
    with fade

    u "(Now this is an event!)"
    play music "music/v10/Track Scene 33.mp3" fadein 2

    jump v10s33_autumn1

label v10s33_autumn1:
    $ freeroam6.add("autumn")

    scene v10cfraut1a #FPP Show Autumn, Looking at mc, smile with stressed eyes, mouth closed
    with dissolve

    u "Hey Autumn! This is really nice."

    scene v10cfraut1 #FPP same 1a, mouth open
    with dissolve

    aut "Thanks. It took a lot of work, but I love how it's all turned out."

    scene v10cfraut1a
    with dissolve

    u "Did everything go as planned?"

    scene v10cfraut1
    with dissolve

    aut "Little bumps and bruises here and there, but for the most part it did."
    aut "Our little thrift sale was a last minute decision so I had to stay up all night sorting through old clothes."

    scene v10cfraut1a
    with dissolve

    u "Since everything is running smoothly, do you at least get to relax now?"

    scene v10cfraut1
    with dissolve

    aut "Not if I want to keep it that way. Best if I just push through and relax when it's all over."

    scene v10cfraut1a
    with dissolve

    u "Lauren said this event was really important to you. Why's that?"

    scene v10cfraut1b #same 1, autumn thoughtful
    with dissolve

    aut "I mean, it's one of if not our biggest event of the year." 

    scene v10cfraut1
    with dissolve
    
    aut "Also, it's for a good cause. *Chuckles* I'm a sucker for good causes."

    scene v10cfraut1a
    with dissolve

    u "I can only imagine all the behind the scenes work. Surprised you didn't have the pledges do most of the heavy lifting."

    scene v10cfraut1
    with dissolve

    aut "I take a more uhm... lead by example approach, instead of just passing out orders. Though some were more eager to help than others. *Chuckles*"

    scene v10cfraut1a
    with dissolve

    u "I assume you're talking about Lauren?"

    scene v10cfraut1
    with dissolve

    aut "Yep, she not only helped with everything I had already planned, but she contributed a lot as well."

    scene v10cfraut1a
    with dissolve

    u "Seems like you guys are really close."

    scene v10cfraut1
    with dissolve

    aut "We really are, it means a lot to me that she decided to pledge. It isn't something I expected from her, but regardless it's a good thing."

    scene v10cfraut1a
    with dissolve

    menu:
        "Ask why":
            $ add_point(KCT.BOYFRIEND)
            $ autumn.points += 1
            u "Why wouldn't you expect her to pledge?"

            scene v10cfraut1b
            with dissolve

            aut "She's just a little shy. Even when we were kids she was shy. Being in a big group isn't really her thing, she's a really private person. If she does share something personal with you it's because she trusts you."

            scene v10cfraut1c #same 1b, mouth closed
            with dissolve

            u "(I doubt she's told many people everything she's told me.)"

        "Leave it be":
            $ add_point(KCT.BRO)
            u "(Not really my business.)"

    scene v10cfraut1
    with dissolve

    aut "So... plan on sticking around?"

    scene v10cfraut1a
    with dissolve

    u "Of course, I've been looking forward to this."

    scene v10cfraut1d #same as 1, cheeky, mouth open
    with dissolve

    aut "Is that so? A lot of guys told me they were really excited once they had heard about the mud wrestling."

    scene v10cfraut1e #same as 1d, mouth closed
    with dissolve

    menu:
        "That's the main reason":
            $ add_point(KCT.BRO)
            u "I'll be sure to try the other things too, but it's definitely the main attraction."
        
        "I'd be here without it":
            $ add_point(KCT.BOYFRIEND)
            $ autumn.points += 1
            u "I didn't even know about the mud wrestling until recently, I'd be here with or without it."

    scene v10cfraut1d
    with dissolve
    aut "As long as we raise enough money I'll be happy. *Laughs* That's why I decided on mud wrestling in the first place. Gotta know your audience."

    scene v10cfraut1e
    with dissolve
    u "*Laughs* What are you guys raising money for?"

    scene v10cfraut1b
    with dissolve

    aut "We decided we're going to start raising funds at our charity events for our local animal shelters in serious need."

    scene v10cfraut1c
    with dissolve

    u "That's really cool!"

    if v10_help_nora_freeroam:
        u "You know, might be good for you to find a way to relax after this."

        scene v10cfraut1
        with dissolve

        aut "I'm definitely going to need to."

        scene v10cfraut1a
        with dissolve

        u "I don't know if you'd be up for it, but Nora is actually getting people together for us all to take a trip to Europe. Does that sound like something you'd be interested in doing? I'm definitely going."

        scene v10cfraut1b
        with dissolve

        aut "Hmm, I don't know. It sounds fun, but the Deers may feel neglected if I'm gone for too long."

        scene v10cfraut1c
        with dissolve

        u "*Chuckles* You say it like they're your kids. I'm sure they can take care of themselves while you're on vacation."

        scene v10cfraut1
        with dissolve

        aut "I guess that's true. Maybe I'll talk to Nora about signing up."

    else:
        scene v10cfraut1
        with dissolve

    ### ERROR: -Regardless of anything conversation continued ###

    aut "Anyway, I better get back to running everything, see you around."

    scene v10cfraut1c
    with dissolve

    u "See ya."

    call screen v10s33_entrance

    # -Transition to Scene 34-

label v10s33_deergirl11:
    $ freeroam6.add("rachel")
    
    scene v10cfrdg11 # FPP. Show dg1, looking towards perry out of shot, mouth open
    #with dissolve
    dg1 "Haha, I don't think I've met anyone less coordinated. It's the dab, it's pretty simple."

    scene v10cfrdg11a # FPP. Same 11, dabbing, mouth closed. (should be simple to pose, refer to Migos "Look At My Dab (Bitch Dab)" (WSHH Exclusive - Official Music Video))
    with dissolve

    pause 0.75

    scene v10cfrdg11
    with dissolve

    dg1 "See?"

    scene v10cfrdg12 # FPP. Show Perry dabbing
    with dissolve

    pause 0.75
    
    scene v10cfrdg11
    with dissolve
    dg1 "There you go!"

    scene v10cfrdg12a # FPP. same 12,Show perry, looking at dg1 out of shot, mouth open
    with dissolve
    guyd "Only took me a thousand tries."
    
    if joinwolves:
        scene v10cfrdg12b # FPP. same 12, show perry looking at camera, mouth open
        with dissolve

        guyd "Hey [name], please come help me."
    else:
        scene v10cfrdg11b # FPP. same 11 looking at camera, mouth open
        with dissolve
        
        dg1 "Hey you, c'mon over here."

    scene v10cfrdg11b
    with dissolve
    
    dg1 "I'm trying to teach Perry some new dances, but he's having some trouble."

    scene v10cfrdg11g # FPP. same 11b, mouth closed.
    with dissolve

    u "What kind of dances?"

    scene v10cfrdg12b
    with dissolve

    guyd "If you were scrolling on your phone late at night and kept seeing a bunch of short videos type dances."

    scene v10cfrdg12c # FPP. same as 12c, mouth closed.
    with dissolve

    u "Haha, oh! Those are easy."

    scene v10cfrdg12b
    with dissolve

    guyd "Don't speak too soon."

    scene v10cfrdg11b
    with dissolve

    dg1 "He's just bad at them. *Laughs* Try this one?"

    scene v10cfrdg11c # FPP. same 12, dg looking at camera, right hand held out to right, mouth closed.
    with dissolve

    pause 0.5

    scene v10cfrdg11d # FPP. same 12c, now both hands held out like a T pose.
    with dissolve
    
    pause 0.5
    
    scene v10cfrdg11e # FPP. same 12d, now both hands anime peace sign infront of face
    with dissolve

    menu:
        "Arm Arm Pose":
            scene v10cfrdg14 # TPP. Show MC looking at camera, right hand held out to right, mouth closed.
            with dissolve

            pause 0.5

            scene v10cfrdg13a #TPP. same 13, now both hands held out like a T pose.
            with dissolve

            pause 0.5

            scene v10cfrdg13b # TPP. now both hands anime peace sign infront of face
            with dissolve

            pause 0.5

            scene v10cfrdg11b
            with dissolve
            dg1 "Look at you!"

            scene v10cfrdg12b
            with dissolve

            guyd "You probably practiced these before."

            scene v10cfrdg12c
            with dissolve

            u "*Laughs* No, but it's not that hard."

        "Pose Pose Arm":
            scene v10cfrd13 
            with dissolve

            pause 0.5

            scene v10cfrdg13a 
            with dissolve

            pause 0.5

            scene v10cfrdg11c
            with dissolve

            u "What was that last part?"

            scene v10cfrdg12b
            with dissolve

            guyd "Haha, thought they were easy?"

    scene v10cfrdg11b
    with dissolve
    
    dg1 "Let's try one more."

    scene v10cfrdg11f # FPP. same 11, Show dg1 leant back arms crossed, mouth closed
    with dissolve

    pause 0.5

    scene v10cfrdg11g2 # FPP. same 11, leant forward arms down.
    with dissolve
    
    pause 0.5
    
    scene v10cfrdg11h # FPP. same 11, silly face with jazz hands
    with dissolve

    menu:
        "Cross Lean Face":
            scene v10cfrdg13c # TPP. same 13, Show mc leant back arms crossed, mouth closed
            with dissolve

            dg1 "See, it's easy for him. Why are you so stiff? *Laughs*"

            scene v10cfrdg13d # TPP. same 13, leant forward arms down.
            with dissolve

            guyd "Honestly, I'd just be embarrassed to do that."

            scene v10cfrdg13e # TPP. same 13, silly face with jazz hands
            with dissolve

            pause 0.75

        "Lean Face Cross":
            scene v10cfrdg13d # TPP. same 13, leant forward arms down.
            with dissolve
            
            pause 0.5
            
            scene v10cfrdg13c # TPP. same 13, Show mc leant back arms crossed, mouth closed
            with dissolve

            pause 0.75

            scene v10cfrdg13f # TPP same 13c, show mc Bumping into perry. perry mouth open
            with dissolve

            guyd "Well, I'm not the only one struggling."

            scene v10cfrdg11b
            with dissolve

            dg1 "Guess dancing isn't for everyone. *Laughs*"

    scene v10cfrdg11g
    with dissolve

    u "Well as fun as that was, I'm gonna look around some."

    scene v10cfrdg11b
    with dissolve

    dg1 "If you're interested in learning any more dances, you know where to find me."

    if joinwolves:
        menu:
            "Make fun of Perry":
                scene v10cfrdg12c
                with dissolve

                u "Or I could find Perry, he was doing great. *Chuckles*"

                scene v10cfrdg12b
                with dissolve

                guyd "Funny."

            "Encourage Perry":
                scene v10cfrdg12c
                with dissolve

                u "Keep going at it Perry, I'm sure you'll get it."

                scene v10cfrdg12b
                with dissolve

                guyd "Thanks man."

    call screen v10s33_stage

    label v10s33_aubrey1:
    $ freeroam6.add("aubrey")

    scene v10cfrau1 #FPP, Aubrey is doing the Zero Two TikTok dance, refer to https://youtu.be/4b69koOYry4, left pose

    pause 0.5

    scene v10cfrau1a #same as 1, right pose
    with dissolve
    
    pause 0.5

    scene v10cfrau1
    with dissolve

    pause 0.5
    
    scene v10cfrau1a
    with dissolve

    u "Someone's having fun!"

    scene v10cfrau2  #FPP Show Aubrey, Looking at mc, happy smile, mouth open
    with dissolve

    au "Oh hey [name]. Caught me dancing."

    scene v10cfrau2a # same 2, mouth closed
    with dissolve

    u "You look like you know what you're doing."

    scene v10cfrau2b # same 2, ironic "you don't say"-kinda smile, mouth open
    with dissolve

    au "If I didn't I would've wasted a lot of time as a kid."

    scene v10cfrau2c # same 2b, mouth closed
    with dissolve

    u "What do you mean?"

    scene v10cfrau2 
    with dissolve

    au "I've always loved dancing. I did it for fun all the time growing up, then I stopped for a long time."

    au "But I heard being a good dancer makes you better in bed. *Laughs* So I picked it back up a few months ago."

    scene v10cfrau2a
    with dissolve

    u "*Laughs*"

    scene v10cfrau2
    with dissolve

    au "Wanna dance with me?"

    scene v10cfrau2a
    with dissolve

    menu:
        "Sure":
            u "Sure."
            $ add_point(KCT.BOYFRIEND)
            $ aubrey.points += 1
            scene v10cfrau5 #TPP, Aubrey grabs MC holding his hands, they're both smiling, mouth closed
            with dissolve

            pause 0.5

            scene v10cfrau5a # same 5a, Aubrey sways to one side
            with dissolve

            pause 0.5

            scene v10cfrau5b # same 5a, Aubrey sways to the other side
            with dissolve

            pause 0.5

            scene v10cfrau5a
            with dissolve

            pause 0.5

            scene v10cfrau5b
            with dissolve

            menu:
                "Twirl her":
                    scene v10cfrau5c #same 5b, mc twirls aubrey start
                    with dissolve

                    pause 1.0

                    scene v10cfrau5d #same 5c, mc twirls aubrey end, aubrey mouth open, cheeky
                    with dissolve

                    au "Someone's old school."

                "Dip her":
                    $ aubrey.points += 1
                    scene v10cfrau5e #same 5b, mc dips aubrey start
                    with dissolve

                    pause 1.0

                    scene v10cfrau5f #same 5e, mc dips aubrey end, aubrey mouth open, cheeky
                    with dissolve

                    au "So you know a little bit about dancing too."

            scene v10cfrau5
            with dissolve

            u "*Laughs*"

            scene v10cfrau3 # TPP showing Aubrey and Mc sitting down (in the movement of sitting down)
            with dissolve

            pause 0.5

            scene v10cfrau4 #FPP, show Aubrey, sat down looking at mc, cute smile, mouth open
            with dissolve

            au "I haven't danced with someone else in a long time."

            scene v10cfrau4a #same 4, mouth closed
            with dissolve

            u "Do you remember who your last dance partner was?"

            scene v10cfrau4
            with dissolve

            au "I don't, high school prom date. *Laughs*"

        "No way":
            $ aubrey.points -= 1
            $ add_point(KCT.BRO)
            u "Oh no way, I don't wanna be an embarrassment. *Laughs*"

            scene v10cfrau2b
            with dissolve

            au "Your loss sir."

            scene v10cfrau3 # TPP showing Aubrey and Mc sitting down (in the movement of sitting down)
            with dissolve

            pause 0.5

    scene v10cfrau4a
    with dissolve

    u "You know what I've always liked about you?"

    scene v10cfrau4
    with dissolve

    au "What's that?"

    scene v10cfrau4a
    with dissolve

    u "You're always so positive. I don't think I've ever seen you down."

    scene v10cfrau4
    with dissolve

    au "Ha, what's the point in being down? I just think life is short and you should enjoy it. I don't wanna waste time pouting around or being pissed off."

    scene v10cfrau4a
    with dissolve

    u "I rate that."

    scene v10cfrau4b #same 4, cheeky/ flirty, mouth open
    with dissolve

    au "Speaking of rating, I'm curious, what would you rate the girls on campus?"

    scene v10cfrau4c #same 4b, mouth closed
    with dissolve

    u "What do you mean?"

    scene v10cfrau4b
    with dissolve

    au "Like a one to ten? What would you rate them? Looks only."
    au "Matter of fact, I'll make it even easier for you. I'll say a girl's name and you say if she's hot or not. No reason you can't be honest."

    scene v10cfrau4c
    with dissolve

    u "Go ahead."

    scene v10cfrau4d # same 4b, curious, mouth open
    with dissolve

    au "Chloe?"

    scene v10cfrau4e # same 4d, mouth closed
    with dissolve

    menu:
        "Hot":
            $ add_point(KCT.BRO)
            u "Hot."

            scene v10cfrau4b
            with dissolve

            au "Of course she is!"
       
        "Not":
            $ add_point(KCT.TROUBLEMAKER)

            u "Not."

            scene v10cfrau4f # same 4d, shocked, mouth open
            with dissolve

            au "What?! You must be blind."
           
    scene v10cfrau4d # same 4b, curious, mouth open
    with dissolve
    
    au "Alright, Nora?"

    scene v10cfrau4e
    with dissolve

    menu:
        "Hot":
            $ add_point(KCT.TROUBLEMAKER)
            u "Hot."

            scene v10cfrau4b
            with dissolve

            au "Not gonna lie, if I ever went for a girl from the Chicks... Whew!"

        "Not":
            $ add_point(KCT.BRO)
            u "Not."

            scene v10cfrau4f
            with dissolve

            au "You must be joking!"

    scene v10cfrau4d
    with dissolve

    au "What about Lindsey?"

    scene v10cfrau4e
    with dissolve

    menu:
        "Hot":
            $ add_point(KCT.BRO)
            u "Hot."

            scene v10cfrau4d
            with dissolve

            au "Cute, but I don't know about hot."
        
        "Not":
            $ add_point(KCT.TROUBLEMAKER)
            u "Not."

            scene v10cfrau4d
            with dissolve

            au "She's not that bad."

    scene v10cfrau4e
    with dissolve

    u "*Chuckles* Are you planning on asking me about every girl on campus you know?"

    scene v10cfrau4
    with dissolve

    au "Haha, maybe. Let's keep going." 

    scene v10cfrau4d
    with dissolve
    
    au "Lauren?"

    scene v10cfrau4e
    with dissolve

    menu:
        "Hot":
            $ add_point(KCT.BOYFRIEND)
            if lauren.relationship >= Relationship.GIRLFRIEND:
                u "Hot, obviously."

                scene v10cfrau4
                with dissolve

                au "Oh yeah, duh. *Laughs*"

            else:
                u "Hot."

                scene v10cfrau4b
                with dissolve

                au "Her little innocent attitude is pretty hot."

        "Not":
            $ add_point(KCT.BRO)
            u "Not."

            scene v10cfrau4b
            with dissolve

            au "What, don't like the little innocent ones?"

            scene v10cfrau4c
            with dissolve

            u "*Laughs*"

    scene v10cfrau4d
    with dissolve

    au "Riley?"

    scene v10cfrau4e
    with dissolve

    menu:
        "Hot":
            $ aubrey.points += 1
            $ add_point(KCT.BRO)
            u "Hot."

            scene v10cfrau4
            with dissolve

            au "Exactly!"
            au "It seems we both have good taste."

        "Not":
            $ add_point(KCT.TROUBLEMAKER)
            u "Not."

            scene v10cfrau4f
            with dissolve

            au "I don't think you know what the word \"hot\" means."

    scene v10cfrau4b
    with dissolve
    au "Okay last one, what about Ms. Rose?"

    scene v10cfrau4c
    with dissolve

    if joinwolves:
        u "*Blushes* Uhhh'"

        scene v10cfrau4b
        with dissolve

        au "*Chuckles* Guess I have my answer to that."

        scene v10cfrau4c
        with dissolve

        u "No I just-"

        scene v10cfrau4
        with dissolve

        au "You don't have to explain to me."

    else:
        menu:
            "Hot":
                $ add_point(KCT.BRO)
                u "Hot."

                scene v10cfrau4
                with dissolve

                au "Definitely too cute to be a Professor."

            "Not":
                $ add_point(KCT.BOYFRIEND)

                u "Not."

                scene v10cfrau4f
                with dissolve

                au "What? You're definitely wrong on that one."

    scene v10cfrau4a
    with dissolve

    u "*Laughs* Oh man, what a game."

    scene v10cfrau4
    with dissolve

    au "Haha!"

    scene v10cfrau4a
    with dissolve

    if v10_help_nora_freeroam:
        menu:
            "Invite her to Europe":
                $ aubrey.points += 1
                $ add_point(KCT.BOYFRIEND)

                u "Before I forget, do you know about the Europe trip?"

                scene v10cfrau4
                with dissolve

                au "That's the trip where we all go to Australia right?"

                scene v10cfrau4a
                with dissolve

                u "What? *Chuckles*"

                scene v10cfrau4
                with dissolve

                au "Haha, I'm just playing. *Laughs* Yes I know about the trip. Why?"

                scene v10cfrau4a
                with dissolve

                u "Well I'm planning on going and I was wondering if you wanna come with me."

                scene v10cfrau4
                with dissolve

                au "Well since you're inviting me I assume that means you'll keep me company if I go?"

                scene v10cfrau4a
                with dissolve

                u "Of course I will."

                scene v10cfrau4
                with dissolve

                au "Then sure I'll go then."

                scene v10cfrau4a
                with dissolve

                u "Great!"

            "Don't invite her":
                $ aubrey.points -= 1
                $ add_point(KCT.TROUBLEMAKER)

                u "(If she goes she goes, if she doesn't she doesn't.)"

    u "I'm gonna go check out some more stuff."

    scene v10cfrau4
    with dissolve

    au "Alright, see ya."

    call screen v10s33_stage

label v10s33_chloe1:
    $ freeroam6.add("chloe")
    if chloe.relationship <= Relationship.MAD:
        scene v10cfrcl1 # FPP. Show Chloe, mouth closed
        
        u "I think Chloe's still mad at me, I'd rather not talk to her."
        call screen v10s33_centeraisle

        label v10s33_chloe2:
        
        scene #mudwrestling screen
        u "(I already talked to her.)"

        call screen v10s33_centeraisle

    scene v10cfrcl1 # FPP. Show Chloe, mouth closed
    #with dissolve
    
    u "Hey Chloe."

    scene v10cfrcl1a # FPP. same1, mouth open
    with dissolve

    cl "Hey."

    scene v10cfrcl1
    with dissolve

    u "There may be a lot of people here, but you're pretty easy to spot in a crowd, you know?"

    scene v10cfrcl1a
    with dissolve

    cl "I don't know if that's supposed to be a compliment or not. *Chuckles*"

    scene v10cfrcl1
    with dissolve

    u "It's a compliment. Just don't think about it for too long, cause I kinda see now that there's other ways to interpret it. *Laughs*"

    scene v10cfrcl1a
    with dissolve

    cl "Thanks. You are right though, there are a lot of people here. Way more than The Deers pulled in last year."

    cl "Us Chicks are going to have to step up our game if we're gonna be able to compete with this. Autumn deserves a round of applause."

    scene v10cfrcl1
    with dissolve

    u "She did work pretty hard on this."

    scene v10cfrcl1a
    with dissolve

    cl "It's always interesting how most of the time we're all doing our own thing."
    
    cl "But an event like this comes up and all of the sudden each of us has the same few hours on a Wednesday locked in on the calendar."

    scene v10cfrcl1
    with dissolve

    u "Isn't there a theory or something about that?"

    scene v10cfrcl1b # FPP. same1,slight smile, mouth open
    with dissolve

    cl "I wouldn't know. *Laughs*"

    scene v10cfrcl1
    with dissolve

    u "*Laughs*"

    scene v10cfrcl2 # FPP. Show the win a date stand
    with dissolve

    u "I wonder who's idea this was?"

    scene v10cfrcl1b
    with dissolve

    cl "Someone clever."

    scene v10cfrcl1
    with dissolve

    u "Or someone hoping to get a date. *Laughs*"

    scene v10cfrcl1b
    with dissolve

    cl "You're so mean! *Laughs*"

    menu:
        "Date with Chloe":
            $ chloe.points += 1
            if chloe.relationship >= Relationship.FWB:
                scene v10cfrcl1
                with dissolve

                u "I wish I could win a date with you."

                scene v10cfrcl1b
                with dissolve

                cl "Anytime!"

            else:
                scene v10cfrcl1
                with dissolve
                
                u "I wish I could win a date with you."

                scene v10cfrcl1b
                with dissolve

                cl "That's cute."

        "Who would you date?":
                scene v10cfrcl1
                with dissolve

                u "Who would you wanna win a date with?"

                scene v10cfrcl1b
                with dissolve

                cl "Can I choose cartoon characters? *Chuckles*"

                scene v10cfrcl1
                with dissolve

                u "That's one way to say no man is good enough for me. *Chuckles*"

                scene v10cfrcl1b
                with dissolve

                cl "What? No, I was just thinking about what'd it'd be like to go on a date in a cartoon because in a cartoon anything could happen."

                cl "I could be like... like a princess or something. *Laughs*"

                scene v10cfrcl1
                with dissolve

                u "Haha, I guess that's true."

    scene v10cfrcl1
    with dissolve
    
    u "Not to change subjects, but how's the sorority going? Any more troubles?"

    scene v10cfrcl1b
    with dissolve

    cl "None that I know of."

    if v10_nora_bitch_about_chloe:
        menu:
            "Tell Chloe about Nora":
                $ chloe.points += 1
                $ v10s33_toldChloe = True
                scene v10cfrcl1c # FPP. same1,slight angry look, closed
                with dissolve

                u "Well, not to be that guy, but I ask cause Nora was actually talking about you earlier."

                scene v10cfrcl1d # FPP. same1,slight angry look, open
                with dissolve

                cl "What was she saying?"

                scene v10cfrcl1c
                with dissolve

                $ grant_achievement("hard_decisions")
                u "She said a lot, but to sum up everything, she called you fake. Said you do a bunch of pretending for sympathy points from people."

                scene v10cfrcl1d # FPP. same1,slight angry look, mouth open
                with dissolve

                cl "Are you serious? You know what..."

                scene v10cfrcl3 # FPP. Show Chlow from behind now at bag toss walking towards nora, nora facing chloe as she approaches
                with fade

                cl "NORA WHAT'S THE DEAL?"

                scene v10cfrcl3a # FPP. Show Chlow from behind now at bag toss walking towards nora, nora facing chloe as she approaches, nora annoyed face, nora mouth open
                with dissolve

                no "What are you talking about?"

                scene v10cfrcl3
                with dissolve

                cl "Don't act clueless, I heard what you said about me to [name]."

                scene v10cfrcl3a
                with dissolve


                no "And? I didn't say anything that wasn't true. You're a manipulative person that does anything to get what she wants."

                scene v10cfrcl3
                with dissolve

                cl "Oh stop! I don't know if you're jealous or what."
                
                cl "You've had something against me from the second I became President and I'm honestly getting sick of it!"
                
                cl "Let's settle this right here right now, in the ring!"

                scene v10cfrcl3b # FPP. same 3, nora arms up in air in anger, mouth open
                with dissolve

                no "OH YEAH, THEN GET IN THE RING ALREADY!"

                call screen v10s33_mudwrestling

            "Don't tell Chloe":
                scene v10cfrcl1
                with dissolve
                
                u "(Let's not start anything.)"
                u "That's good, it's best if you guys are getting along."

                scene v10cfrcl1a
                with dissolve

                cl "Yeah, true."

                if v10_help_nora_freeroam:
                    menu:
                        "Invite to Europe":
                            scene v10cfrcl1
                            with dissolve
                            
                            u "Speaking of getting along, are you going on the Europe trip? I know I am."

                            scene v10cfrcl1d
                            with dissolve

                            cl "I'm not trying to be on a long trip in another country with Nora, if I'm being honest."

                            menu:
                                "Convince her":
                                    $ chloe.points += 1
                                    scene v10cfrcl1
                                    with dissolve

                                    u "Europe is a big place, I'm sure you can find a way to enjoy yourself and not be around her if that's what you want."

                                    scene v10cfrcl1a
                                    with dissolve

                                    if kct == "popular" or chloe.relationship >= Relationship.FWB:
                                        scene v10cfrcl1a
                                        with dissolve

                                        cl "Okay, I'll think about it."

                                    else:
                                        scene v10cfrcl1a
                                        with dissolve

                                        cl "Yeah... I don't know."

                                "Let her decide":
                                    scene v10cfrcl1
                                    with dissolve

                                    u "I understand, it's your choice."

                        "Don't invite":
                            scene v10cfrcl1
                            with dissolve

                            u "(I'll let her decide if she goes.)"  

    scene v10cfrcl1a
    with dissolve

    cl "Anyway, I want to look around some more, so I'll catch up with you."

    scene v10cfrcl1
    with dissolve

    u "Later."

    call screen v10s33_centeraisle

label v10s33_deergirl21:

    $ freeroam6.add("eleanor")
    
    scene v10cfrdg21 #FPP Show DG2, Looking at mc, happy, cute smile, mouth open

    dg2 "Hey you!"

    scene v10cfrdg21a #same 1, mouth closed
    with dissolve

    u "Me?"

    scene v10cfrdg21
    with dissolve

    dg2 "Yeah, come try out my game."

    scene v10cfrdg22 # shows the throwing bags game
    with dissolve

    u "I used to play this back in school."

    scene v10cfrdg21
    with dissolve

    dg2 "Some people have done amazing, others... not so much. *Chuckles*"

    scene v10cfrdg29 # showing sexual prizes
    with dissolve

    u "What are these prizes?"

    scene v10cfrdg21
    with dissolve

    dg2 "Just a few things to spice up your uhm... life."

    scene v10cfrdg21a
    with dissolve

    menu:
        "Make a joke":
            $ add_point(KCT.BRO)

            u "If I win the lingerie I get to see you in it right? *Chuckles*"

            scene v10cfrdg21b # same 1, dg2 frowns, mouth open
            with dissolve

            dg2 "Not a chance!"

            scene v10cfrdg21c #same 1b, mouth closed
            with dissolve

            u "My bad, I didn't mean to... I'm just gonna go."

        "Play the game":
            $ add_point(KCT.BOYFRIEND)

            u "Mind if I play a game?"

            scene v10cfrdg21
            with dissolve

            dg2 "Please do."

            scene v10cfrdg23 #TPP shows mc throwing version 1
            with dissolve

            pause 0.8

            scene v10cfrdg24 # closeup bag missing version 1
            with vpunch

            pause 0.8

            scene v10cfrdg23a #TPP shows mc throwing version 2
            with dissolve

            pause 0.8

            scene v10cfrdg24a # closeup bag missing version 2
            with vpunch

            pause 0.8

            scene v10cfrdg23b #TPP shows mc throwing version 3
            with dissolve

            pause 0.8

            scene v10cfrdg24b # closeup bag missing version 3
            with vpunch

            pause 0.8

            scene v10cfrdg21
            with dissolve
            
            dg2 "I'll put you in the category of those who did... not so well."

            scene v10cfrdg21a
            with dissolve

            u "Yep, and that's my cue to leave. Thanks."

    call screen v10s33_bagtoss

    label v10s33_deergirl31:

    $ freeroam6.add("karen")

    scene v10cfrdg31a #FPP, showing dg3, sitting if she's seated,looking at you, crazy smile with a hint of sadness, mouth closed
    #with dissolve

    u "You know I didn't expect to see one of these at the event. What made you want to do one of these?"

    scene v10cfrdg31 #same 1a, mouth open
    with dissolve

    dg3 "I'm lonely."

    scene v10cfrdg31a
    with dissolve

    u "That's it?"

    scene v10cfrdg31
    with dissolve

    dg3 "I don't think you understand, I'm really lonely. No guys ever talk to me."
    
    dg3 "With this, one guy will be forced to go out with me and I'll never be lonely again."

    scene v10cfrdg31a
    with dissolve

    u "(Okay, I see why she's lonely now.)"

    u "Are a lot of people getting tickets?"

    scene v10cfrdg31
    with dissolve

    dg3 "Not yet, but they will. My mom said it's a great idea."

    scene v10cfrdg31a
    with dissolve

    menu:
        "Get a lottery ticket":
            $ freeroam6.add("karen_ticket")
            $ add_point(KCT.BOYFRIEND)
            u "Well I'll take one."

            scene v10cfrdg31b #same 1, happy, hands out ticket to mc
            with dissolve

            dg3 "Yayyyy! I mean okay, thank you. Here you go."

            scene v10cfrdg31a 
            with dissolve

            u "Thanks."

        "Don't get a ticket":
            $ add_point(KCT.TROUBLEMAKER)
            u "Well, good luck."

            scene v10cfrdg31d #same 1, dissappointed, mouth open
            with dissolve

            dg3 "You don't want one?"

            scene v10cfrdg31e #same 1d, mouth closed
            with dissolve

            u "Oh uhm... I have a girlfriend."

            scene v10cfrdg31d
            with dissolve

            dg3 "The good ones are always taken."

    call screen v10s33_centeraisle
    
    label v10s33_laurenbake1:
    $ freeroam6.add("lauren")

    if lauren.relationship >= Relationship.GIRLFRIEND:
        scene v10cfrla1 #FPP Show Lauren, Looking at mc, happy smile, mouth open
        la "Hey babe!"

        scene v10cfrla2 #TPP showing Mc kissing Lauren over the table
        with dissolve

        play sound "sounds/kiss.mp3"

        pause 0.5

        scene v10cfrla1a #same 1, mouth closed
        with dissolve

    else:
        scene v10cfrla1a
    u "How are the sales going? Good I'm assuming..."

    scene v10cfrla1b #same 1,lauren sarcastic, slight concern, mouth open
    with dissolve

    la "Do pigs fly?"

    scene v10cfrla1c #same 1b, mouth closed
    with dissolve

    u "What? *Chuckles*"

    scene v10cfrla1b
    with dissolve

    la "Haha, to answer your question, bad. Sales are going bad. I only sold one and that was to my mother when she stopped by earlier."

    if lauren.relationship >= Relationship.GIRLFRIEND:
        scene v10cfrla1
        with dissolve

        la "It would've been nice if you two could've met."

    scene v10cfrla1a
    with dissolve

    u "Well I wish sales were going better for you. Maybe if you get Autumn to give a kiss to everyone that buys a cake they'll sell faster."

    scene v10cfrla1
    with dissolve

    la "Knowing her, if she knew it'd make the event better then she'd do it."

    scene v10cfrla1a
    with dissolve

    u "That's dedication. Speaking of making the event better, I know what would."

    scene v10cfrla1d #same 1, cheeky & curious (funnily doubtful), mouth open
    with dissolve

    la "What?"

    scene v10cfrla1e #same 1d, mouth closed
    with dissolve

    u "You plus mud wrestling."

    scene v10cfrla1d
    with dissolve

    la "Funny, but I can't leave my stand."

    scene v10cfrla1e
    with dissolve

    u "Just put a cardboard cut out in your place, you'll still sell the same amount."

    scene v10cfrla1
    with dissolve

    la "You're not funny."

    scene v10cfrla1a
    with dissolve

    u "Haha, you know... a lot of people showed up. Even the not so social ones."

    scene v10cfrla1
    with dissolve

    la "We do have a really good turn out and everyone's booths turned out great."

    scene v10cfrla1a
    with dissolve

    u "Yeah they did, \"Lauren's Moist Muffins\". *Laughs*"

    scene v10cfrla1
    with dissolve

    la "Oh my god stop. *Smiles*"

    scene v10cfrla1a
    with dissolve

    u "Mind if I try one?"

    scene v10cfrla1d
    with dissolve

    la "Sure, for $2.50."

    scene v10cfrla1e
    with dissolve

    u "Oh?"

    scene v10cfrla1b
    with dissolve

    la "What?"

    scene v10cfrla1c
    with dissolve

    u "I actually didn't bring any money?"

    scene v10cfrla1b
    with dissolve

    la "You came to a charity event with no money? Please tell me you're joking."

    scene v10cfrla1c
    with dissolve

    u "Haha, yes I'm just playing around. I brought some money, but I'm not spending it on a cake."
    u "I'm not even hungry, I'd rather spend it on something a little bit more fun."

    scene v10cfrla1b
    with dissolve

    la "Like?"

    scene v10cfrla1c
    with dissolve

    u "Like every other booth."

    scene v10cfrla1b
    with dissolve

    la "Now I feel silly for choosing the bake sale."

    scene v10cfrla1c
    with dissolve

    u "I'm sure you people are gonna get hungry at some point."

    if lauren.relationship >= Relationship.GIRLFRIEND:
        u "I know, I'd love some of... Lauren's Moist Muffins."

        scene v10cfrla1d
        with dissolve

        la "[name] you're gonna get me in trouble."

        scene v10cfrla1e
        with dissolve

        u "Haha!"

        u "Oh I wanted to ask, I'm planning on going on this year's Europe trip. Would you want to go?"

        scene v10cfrla1
        with dissolve

        la "Hmm, I hadn't thought about it, but since you're wanting to I'll think about it."

        scene v10cfrla1a
        with dissolve

        u "Great."

    else:
        if v10_help_nora_freeroam:
            menu:
                "Invite her to Europe":
                    $ add_point(KCT.BOYFRIEND)

                    u "Oh I wanted to ask, I'm planning on going on this year's Europe trip. Would you want to go?"

                    if kct == "loyal":
                        call screen kct_popup

                        scene v10cfrla1
                        with dissolve

                        la "Hmm, I hadn't thought about it, but since you're wanting to I'll think about it."

                        scene v10cfrla1a
                        with dissolve

                        u "Great."

                    else:
                        scene v10cfrla1
                        with dissolve

                        la "Hmm, I hadn't thought about it, I'm not sure."

                        scene v10cfrla1a
                        with dissolve

                        u "No problem, you still have some time to decide."

                "Don't invite her":
                    $ add_point(KCT.BRO)
                    u "(I don't really feel like inviting Lauren.)"

    u "I'm gonna check out some more stuff, I'll check back in later."

    scene v10cfrla1
    with dissolve

    la "See ya."

    call screen v10s33_cakestatue

    label v10s33_laurenstatue1:
    $ freeroam6.add("lauren")

    scene v10cfrla3 #FPP, lauren as statue, not looking at mc, mouth closed
    #with dissolve

    u "What a beautiful statue."

    if lauren.relationship >= Relationship.GIRLFRIEND:
        scene v10cfrla4 #TPP shows mc leaning in for the kiss, but lauren holds him back, lauren mouth open, neutral face
        with dissolve

        la "Sorry babe, the paint."

    scene v10cfrla3b #same 3, lauren looking at mc, "This was a bad idea" doubtful smile, mouth open
    with dissolve

    la "Just so you know, this was a horrible idea. It's too hot to be standing here like this."

    scene v10cfrla3c #same 3b, mouth closed
    with dissolve

    menu:
        "Say you're sorry":
            $ add_point(KCT.BOYFRIEND)
            u "It is, I'm sorry. Maybe it's not a good idea to follow my ideas from now on."

            scene v10cfrla3b
            with dissolve

            la "You think? *Chuckles*"
    
            scene v10cfrla3c
            with dissolve

            u "It does look like you got quite a bit of donations though."

            scene v10cfrla3d #same 3b, cute, positive slightly surprised smile, mouth open
            with dissolve

            la "Really? I hadn't even had a chance to look."

            scene v10cfrla3e #same 3d, mouth closed
            with dissolve

            u "Yeah there's at least $100 in here."

            scene v10cfrla3d
            with dissolve

            la "Oh, well maybe the idea wasn't so bad. *Laughs*"

            scene v10cfrla3e
            with dissolve

            u "*Laughs*"

        "Joke around":
            $ add_point(KCT.TROUBLEMAKER)
            u "Oh my gosh, did that statue just talk to me? Everyone, that statue just talked!"

            scene v10cfrla3b
            with dissolve

            la "I'm never taking your advice again."

            scene v10cfrla3c
            with dissolve

            u "Hey, at least it made you money. There's at least $100 in here already."

            scene v10cfrla3d
            with dissolve

            la "Are you serious?"

            scene v10cfrla3e
            with dissolve

            u "Yeah, for real."

            scene v10cfrla3d
            with dissolve

            la "Oh, well maybe the idea wasn't so bad then. *Laughs*"

            scene v10cfrla3e
            with dissolve

            u "*Laughs*"

    scene v10cfrla3f # same 3b, lauren worried, mouth open
    with dissolve
    la "But I am super itchy, this paint is really bothering me. And I'm kinda worried it won't wash off."

    scene v10cfrla3g # same 3f, mouth closed
    with dissolve

    u "If not, can I pose you in my room? I think you'd make a great addition. *Laughs*"

    scene v10cfrla3b
    with dissolve

    la "Not funny."

    scene v10cfrla3c
    with dissolve

    u "Well I wish it was going better for you."
    
    u "Maybe if you get Autumn to sell fake oil cans people can act as though they're loosening your joints, Mrs. Tin Man. *Laughs*"

    scene v10cfrla3d
    with dissolve

    la "Knowing her, if she knew it'd make the event better then she'd do it."

    scene v10cfrla3e
    with dissolve

    u "Speaking of making the event better, I know what would."

    scene v10cfrla3d
    with dissolve

    la "What?"

    scene v10cfrla3e
    with dissolve

    u "You plus mud wrestling."

    scene v10cfrla3b
    with dissolve

    la "Funny, but I can't leave my stand. I'm a statue remember?"

    scene v10cfrla3c
    with dissolve

    u "So committed, we love to see it."

    if lauren.relationship >= Relationship.GIRLFRIEND:
        u "Oh I wanted to ask, I'm planning on going on this year's Europe trip. Would you want to go?"

        scene v10cfrla3d
        with dissolve

        la "Hmm, I hadn't thought about it, but since you're wanting to I'll think about it."

        scene v10cfrla3e
        with dissolve

        u "Great."

    else:
        if v10_help_nora_freeroam:
            menu:
                "Invite her to Europe":
                    $ add_point(KCT.BOYFRIEND)

                    u "Oh I wanted to ask, I'm planning on going on this year's Europe trip. Would you want to go?"

                    if kct == "loyal":
                        call screen kct_popup

                        scene v10cfrla3d
                        with dissolve

                        la "Hmm, I hadn't thought about it, but since you're wanting to I'll think about it."

                        scene v10cfrla3e
                        with dissolve

                        u "Great."

                    else:
                        scene v10cfrla3d
                        with dissolve

                        la "Hmm, I hadn't thought about it, I'm not sure."

                        scene v10cfrla3e
                        with dissolve

                        u "No problem, you still have some time to decide."

                "Don't invite her":
                    $ add_point(KCT.BRO)
                    u "(I don't really feel like inviting Lauren.)"

    u "I'm gonna check out some more stuff, I'll check back in later."

    scene v10cfrla3d
    with dissolve

    la "See ya."

    call screen v10s33_cakestatue

    label v10s33_lindsey1:
        $ freeroam6.add("lindsey")
        
        scene v10cfrfrli1 # FPP. Show Lindsey stood by the body paint stand in a bikini. Lindsey looking at camera, smile, mouth closed.

        menu:
            "Compliment":
                $ add_point(KCT.BOYFRIEND)
                $ lindsey.points += 1
                u "Look at you! This alone is a reason to give all my money away."

                scene v10cfrfrli1a # FPP. Same as 1, smile, mouth open.
                with dissolve

                li "Haha, you like it?"

                scene v10cfrfrli1
                with dissolve

                u "Yes, it looks nice."

                scene v10cfrfrli1a
                with dissolve

                li "Thanks, I didn't get a second opinion when I got it, but as long as you like it that works for me."

                scene v10cfrfrli1
                with dissolve

                u "Glad my opinion is valued so much."

                scene v10cfrfrli1a
                with dissolve

                li "Of course, I'm thinking of spicing it up with some more paint."

                scene v10cfrfrli1
                with dissolve

                menu:
                    "Paint Lindsey":
                        u "Sounds good to me, I'll do it."

                        scene v10cfrfrli2 # TPP. Show MC getting some brushes from a pot, Lindsey with her back turned.
                        with dissolve

                        pause 1.75
                        
                        scene v10cfrfrli3 # FPP. Show Lindsey's back, MC places the brush on Lindsey's back.
                        with dissolve

                        li "Oh, that tickles. *Laughs*"

                        u "Just stay still."

                        scene v10cfrfrli4 # FPP. Show Lindsey as if she has turned around to MC, Lindsey smile, mouth open.
                        with dissolve

                        li "Please don't paint anything embarrassing. Ooh, can you give me wings?"

                        scene v10cfrfrli4a # FPP. Same as 4, smile, mouth closed.
                        with dissolve

                        u "Sure!"

                        scene v10cfrfrli4
                        with dissolve

                        li "Oh, and a tail."

                        scene v10cfrfrli4a
                        with dissolve

                        u "On it."

                        scene v10cfrfrli5 # TPP. Show MC looking at MC's back, unsure expression.
                        with dissolve

                        u "(Uhm, how am I supposed to do this? Ahh, I know!)"

                        scene v10cfrfrli3a # FPP. Same as 3, MC begins to paint a devil tail coming out of the top of Lindsey's panties.
                        with dissolve

                        pause 1.75

                        scene v10cfrfrli5a # TPP. Same as 5, Lindsey now has a painted devil tail coming from the top of her panties and wings on her back, MC looks impressed.
                        with fade

                        pause 1.75

                        scene v10cfrfrli4b # FPP. Same as 4, nervous, mouth open.
                        with dissolve

                        li "You didn't draw anything bad did you?"

                        scene v10cfrfrli4c # FPP. Same as 4, nervous, mouth closed.
                        with dissolve

                        u "Of course not, you can trust me."

                        scene v10cfrli4f
                        with dissolve

                        li "Alright, [name]."

                    "Don't paint Lindsey":
                        u "*Laughs* You should."

            "Ask how she's doing":
                u "Hey Lindsey, how are you doing?"

                scene v10cfrfrli1a
                with dissolve

                li "Oh hey [name]! I'm doing better."
                li "Today is not a day to be sad, today is a day to raise money for a good cause!"

                scene v10cfrfrli1
                with dissolve

                u "Very true."

        scene v10cfrfrli6 # FPP. Show Lindsey, now stood with her back to the paint booth, camera as if MC is stood infront of her. Lindsey smile, mouth closed.
        with dissolve

        u "Oh Nora told me you're planning on going with us on the Europe trip?"

        scene v10cfrfrli6a # FPP. Same as 6, smile, mouth open.
        with dissolve

        li "Sure am! I am so excited, I've never been out of the state let alone the country. And I think it'll distract me from everything here."

        scene v10cfrfrli6
        with dissolve

        u "I'm sure it will."

        u "Anyways, I'll see you around, gonna make sure I get to see everything."

        scene v10cfrfrli6a
        with dissolve

        li "Sounds good, see ya."

        call screen v10s33_bodypaint

    label v10s33_msrose1:
        $ freeroam6.add("rose")

        scene v10cfrcfrro1 # FPP. Close up Lee and Rose, infront of the body painting booth having a conversation with eachother. Lee mouth open.

        lee "This is a serious form of art."
        lee "History has shown this, name a war prior to modern days where body paint wasn't a significant symbol at minimum."
        lee "I'd much rather do this than bag toss."

        scene v10cfrcfrro1a # FPP. Same as 1, Rose mouth open.
        with dissolve

        ro "It definitely isn't my area of expertise, but I don't see the major significance."
        ro "This is a child's thing. Bag toss at least takes some skill."

        scene v10cfrcfrro1
        with dissolve

        lee "And painting doesn't? This is why I became a history teacher. Someone has to pass along the great traditions of our species."

        scene v10cfrcfrro1b # FPP. Same as 1, both mouths closed.
        with dissolve

        menu:
            "Side with Mr. Lee":
                $ mr_lee.points += 1
                u "I overheard your conversation and I have to be honest, body painting is still pretty major. I know I love it."

                scene v10cfrcfrro1c # FPP. Same as 1, both looking at camera (MC), both smile, lee mouth open.
                with dissolve

                lee "A student that understands. Marvelous."

                scene v10cfrcfrro1d # FPP. Same as 1, both looking at camera, both smile, rose mouth open.
                with dissolve

                ro "Alright then Bruce, you win. If you really think that being painted is so much more fun, prove it. I'll paint you right now."

                scene v10cfrcfrro1c
                with dissolve

                lee "Easy enough."

                scene v10cfrcfrro2 # FPP. Show Mr. Lee taking his pants off, MC laugh, Ms. Rose looks shocked, rose mouth open.
                with dissolve

                ro "UPPER BODY BRUCE! UPPER BODY!"

                scene v10cfrcfrro2a # TPP. Same as 2, Mr. Lee pants around akles, looking at MC, mc laugh, rose shocked, mouths closed.
                with dissolve

                pause 0.75

                scene v10cfrcfrro2b # TPP. Same as 2a, Lee now looking at rose, lee mouth open.
                with dissolve

                lee "Oh yes, of course."

                scene v10cfrcfrro3 # FPP. Same as 1 (different due to clothing). Lee now shirtless with pants on, rose and lee looking at eachother, rose mouth open.
                with dissolve

                ro "You actually want to do this? I didn't expect you to follow through. Now I'm the nervous one."

                scene v10cfrcfrro3a # FPP. Same as 3, lee mouth open.
                with dissolve

                lee "I'm a man of action."

                scene v10cfrcfrro3b # FPP. Same as 3, both mouths closed.
                with dissolve

                menu:
                    "Encourage her":
                        u "You sort of have to now, it's a matter of principle."

                        scene v10cfrcfrro3c # FPP. Same as 3, rose sigh, rose mouth open.
                        with dissolve

                        ro "*Sighs*"
                        
                        scene v10cfrcfrro4 # FPP. Show Ms Rose leaning in to paint on Mr. Lee's chest, MC watching smiling.
                        with dissolve

                        pause 0.75

                        scene v10cfrcfrro5 # TPP. Close up of Ms. Rose's hand painting on lee's chest, painting of roses name with a peach under it should be half done.
                        with dissolve

                        lee "That tickles quite a bit."

                        scene v10cfrcfrro5a # TPP. Same at 5, roses hand no longer in view, painting finished (roses name with peach under it)
                        with fade

                        pause

                        scene v10cfrcfrro3d # FPP. Same as 3, both looking at camera, both smile, lee with roses name and peach painted on his chest, rose mouth open.
                        with dissolve

                        ro "What do you think [name]?"

                        scene v10cfrcfrro5a # FPP. Same as 3d, both smiling, mouths closed.
                        with dissolve

                        u "Perfect!"

                        scene v10cfrcfrro3f # FPP. Same as 3, both smiling, Lee mouth open.
                        with dissolve

                        lee "Better keep this shirt on before my wife starts asking questions."

                        scene v10cfrcfrro1e # FPP. Same as 1, both looking at camera, both smile, both mouths closed.
                        with dissolve

                    "Let it go":
                        scene v10cfrcfrro3c
                        with dissolve

                        ro "Fine, you win, body paint is a fun and serious thing. But I'm not painting you."

                        scene v10cfrcfrro3a
                        with dissolve

                        lee "Bruce's three to Lorraine's two."

                        scene v10cfrcfrro3b
                        with dissolve

                        u "Huh?"

                        scene v10cfrcfrro3c
                        with dissolve

                        ro "We have these little debates all the time and one of us always comes out on top. He randomly started keeping score."

                        scene v10cfrcfrro1e
                        with dissolve

                if v10_help_nora_freeroam:
                    menu:
                        "Invite Ms. Rose to Europe":
                            u "I wanted to ask you Ms. Rose, are you planning on going on the Europe trip?"

                            scene v10cfrcfrro1c
                            with dissolve

                            lee "Oh, no invite for me?"

                            scene v10cfrcfrro1d
                            with dissolve

                            ro "Haha, Mr. Lee and I both may be going as chaperones. Nora and I have spoken about the trip quite a bit. She really wants to go."

                            scene v10cfrcfrro1e
                            with dissolve

                            u "Great!"

                        "Don't invite her":
                            u "(I'm sure Nora will ask her if she wants her to go.)"
                        
            "Side with Ms. Rose":
                $ ms_rose.points += 1
            
                u "I overheard your conversation and I have to be honest, body paint is sort of a kids game nowadays."
                u "It may have been major a long time ago, but living in castles and riding horses was major a long time ago too. Bag toss is better."

                scene v10cfrcfrro1d
                with dissolve

                ro "I think your teacher here gets caught up in his books so much he gets removed from reality."

                scene v10cfrcfrro1c
                with dissolve

                lee "Or everyone else is just lost."

        scene v10cfrcfrro1e
        with dissolve

        u "I'll see you both in class."

        call screen v10s33_bodypaint

label v10s33_riley1:
    $ freeroam6.add("riley")
    
    scene v10cfrri1 # FPP. Show Riley at the thrift shop looking at a top, mouth open.

    ri "Okay, this is way too big for me."

    scene v10cfrri1a # FPP. same 1, now looking at camera,mouth closed
    with dissolve

    u "Looking to add to your closet?"

    scene v10cfrri1b # FPP. same 1, now looking at camera, mouth open
    with dissolve

    ri "Something like that. What made you wanna show up?"

    scene v10cfrri1a
    with dissolve

    u "Just here to support."

    scene v10cfrri1b
    with dissolve

    ri "Yeah sure, here to support girls in their bikinis throwing mud all over each other."

    menu:
        "Joke":
            scene v10cfrri1a
            with dissolve

            u "Maybe I came to throw you in the mud."

            scene v10cfrri1b # FPP. same 1, slight smile,now looking at camera, mouth open
            with dissolve

            ri "Haha, I dare you."

            scene v10cfrri1d # FPP. same 1, slight smile,now looking at camera, closed
            with dissolve

            u "Be careful what you wish for."

            scene v10cfrri1b
            with dissolve

            ri "Do you know how long I'd be in the shower trying to get all that mud out of my hair?"

            scene v10cfrri1d
            with dissolve

            u "No, but I could watch and time you. Then I'd know."

            scene v10cfrri1b
            with dissolve

            ri "You'd be too distracted."

            scene v10cfrri1d
            with dissolve

            u "Maybe. *Chuckles*"

        "Confess":
            scene v10cfrri1d
            with dissolve
            
            u "Hey, it's the main attraction. *Laughs* It'd be wrong of me not to support it."

            scene v10cfrri1b
            with dissolve

            ri "Such a gentleman. *Chuckles*"

    scene v10cfrri1d
    with dissolve
    
    u "Are you going to buy any clothes or just look? Don't tell me you're a window shopper."

    scene v10cfrri1b
    with dissolve

    ri "If I can find something that fits I'll buy it. Everything is either too big or too small."

    scene v10cfrri1d
    with dissolve

    u "Does that make you \"just right\"? *Chuckles*"

    scene v10cfrri1b
    with dissolve

    ri "Of course it does."

    scene v10cfrri1d
    with dissolve

    u "*Laughs*"

    scene v10cfrri2 # FPP. Show close up of riley, slight worried look, mouth open
    with dissolve

    ri "I actually wanted to talk to you about something now that I think about it."

    scene v10cfrri2a # FPP. same 2, mouth closed
    with dissolve

    u "What's up?"

    scene v10cfrri2
    with dissolve

    ri "That \"friend\" of yours, the one that's a little shy, I think her name's Penelope?"
    
    ri "I heard some people talking about her and they were spreading some pretty serious rumors."

    scene v10cfrri2a
    with dissolve

    u "Uhm, what kind of rumors?"

    scene v10cfrri2
    with dissolve

    ri "Something about her getting in trouble with the school, because she hacked their system to help someone get in."
    ri "I didn't see her as the type of person to do something like that."

    menu:
        "It sucks":
            scene v10cfrri2a
            with dissolve

            u "Yeah, it really sucks. She was just trying to be a good friend and now she has to deal with all of this."
            
            u "I get what she did was wrong, but it still doesn't seem fair."

            scene v10cfrri2
            with dissolve

            ri "Some people said she's going to jail."

            scene v10cfrri2a
            with dissolve

            u "Nothing's been decided, people should stop spreading rumors."

            scene v10cfrri2
            with dissolve

            ri "Yeah, true."

        "Don't believe rumors":
            scene v10cfrri2a
            with dissolve

            u "You can't believe everything you hear."

            scene v10cfrri2
            with dissolve

            ri "Yeah, true."

    ri "I haven't spoken to her really, but I hate the thought of her going through whatever this is."
    ri "If you happen to see her soon, let her know if she needs anything she can come talk to me. I'd support her as much as I could."

    scene v10cfrri2a
    with dissolve

    u "That's kind of you."

    scene v10cfrri2b # FPP. same 2, cheeky smile, mouth open
    with dissolve

    ri "I'm a kind person."

    scene v10cfrri2c # FPP. same 2, cheeky smile, mouth closed
    with dissolve

    u "..."

    scene v10cfrri2b 
    with dissolve

    ri "What? I am?"

    scene v10cfrri2c
    with dissolve

    u "..."

    scene v10cfrri2b
    with dissolve

    ri "Okay, I can be. *Laughs*"

    scene v10cfrri2c
    with dissolve

    u "Haha, but yeah, I'll tell her. I'm sure she'll appreciate knowing people are looking out for her."

    scene v10cfrri2d # FPP. same 2, cheeky smile,putting on a hat, mouth open
    with dissolve

    # -Riley tries on a hat-

    ri "Now this I can work with! What do you think?"

    menu:
        "It looks good":
            scene v10cfrri2e # FPP. same 2, cheeky smile,wearing a hat from here on, mouth closed
            with dissolve
            u "I wouldn't wear it, but on you it looks great."

            scene v10cfrri2f # FPP. same 2, cheeky smile,wearing a hat from here on, mouth open
            with dissolve

            ri "Really, you like it?"

            scene v10cfrri2e
            with dissolve

            u "Sure do."

            scene v10cfrri2f
            with dissolve

            ri "Good, then I found something I'll get."

        "No way":
            scene v10cfrri2e
            with dissolve

            u "I wouldn't wear it."

            scene v10cfrri2f
            with dissolve

            ri "That's not what I asked."

            scene v10cfrri2e
            with dissolve

            u "It's okay."

            scene v10cfrri2f
            with dissolve

            ri "You obviously have no fashion sense. *Chuckles* I'm gonna get it."

    scene v10cfrri2e
    with dissolve

    u "Way to support."

    scene v10cfrri2f
    with dissolve

    ri "Like I said, I'm a kind person. *Chuckles* Have you been to the dance stand?"

    if "rachel" in freeroam6 or "aubrey" in freeroam6:

        scene v10cfrri2e
        with dissolve
        
        u "Some people are great dancers and others should just watch."

    else:
        scene v10cfrri2e
        with dissolve
        
        u "Not yet, may be good to avoid it."

    scene v10cfrri2f
    with dissolve

    ri "Haha, well I'm gonna go over there and show Aubrey my new hat. Wanna come with me?"

    scene v10cfrri2e
    with dissolve

    u "Maybe later."

    scene v10cfrri2f
    with dissolve

    ri "Okay, see ya."

    scene v10cfrri2e
    with dissolve

    u "See ya."

    call screen v10s33_thrift
    ### ERROR: -If MC speaks to Riley again ###

label v10s33_riley2:
    $ v10s33_aubreyriley = True
    scene v10cfrriau1 # FPP. Show Riley and aubrey, Riley mouth open
    #with dissolve

    ri "I actually just got it from the thrift booth. [name] helped me pick it out."

    scene v10cfrriau2 # FPP. Show Aubrey, slight smile mouth open
    with dissolve

    au "I really like it, if it goes missing it wasn't me. *Chuckles* You look like a real dancer in that hat."

    scene v10cfrriau3 # FPP. Show Riley, slight smile mouth open
    with dissolve

    ri "Uhm, I am a real dancer. *Laughs*"

    scene v10cfrriau2
    with dissolve

    au "Almost falling on a slippery road but managing to catch yourself isn't dancing. *Chuckles*"

    scene v10cfrriau3
    with dissolve

    ri "Hey! I can dance. I can probably dance better than you."

    scene v10cfrriau2
    with dissolve

    au "Now you're just trying to embarrass yourself."

    scene v10cfrriau3
    with dissolve

    ri "It's a scientific fact that redheads are the best dancers."

    scene v10cfrriau2
    with dissolve

    au "What scientist taught you that? *Chuckles*"

    scene v10cfrriau3
    with dissolve

    ri "..."

    scene v10cfrriau2
    with dissolve

    au "Dr...?"

    scene v10cfrriau3
    with dissolve

    ri "It was my mom. But I'll still whoop you in a dance competition anytime."

    scene v10cfrriau2
    with dissolve

    au "Haha, I wish your mom was here to see what I'm about to do. Let's see..."

    # -AUBREY is looking around before noticing notices MC-
    scene v10cfrriau2a # FPP. Show Aubrey, slight smile mouth open, looking at camera
    with dissolve

    au "Hey [name]! Mind coming over here for a sec?"

    scene v10cfrriau2b # FPP. Show Aubrey, slight smile mouth closed, looking at camera
    with dissolve

    u "What's up?"

    scene v10cfrriau2a
    with dissolve

    au "Our friend Riley here has insisted she's better at dancing than me so her and I are getting ready to have a dance contest and you're going to judge."

    scene v10cfrriau3 # FPP. Show Riley, slight smile mouth open, looking at camera
    with dissolve

    ri "Right now?"

    scene v10cfrriau2
    with dissolve

    au "What's wrong redhead? *Chuckles* Scared?"

    scene v10cfrriau3
    with dissolve

    ri "Never, let's do it. But we need more judges."

    if "rachel" in freeroam6:
    ### ERROR: -If spoke to DG1 and PERRY ###
        scene v10cfrriau3b # FPP. same 3a, mouth closed
        with dissolve

        u "I know the perfect people."

        scene v10cfrriau4 # FPP. Show dg1 and perry looking at each other
        with dissolve

        u "Hey! You two come here real quick."

    else:
        scene v10cfrriau3a
        with dissolve

        ri "I know who can do it."

        scene v10cfrriau4
        with dissolve

        u "Hey! You two come here real quick."

    # -Perry and DG1 walk over-
    scene v10cfrriau5 # FPP. Show Perry, mouth open
    with dissolve

    guyd "What's up?"

    scene v10cfrriau5a #  FPP. Same 5 mouth closed.
    with dissolve

    u "Dance contest, we're the judges."

    scene v10cfrriau6 # FPP. Show dg1, slight smile mouth open
    with dissolve

    dg1 "Oh this ought to be fun."

    scene v10cfrriau7 # FPP. Show dg1 pressing play on jukebox by stage, mouth open
    with dissolve

    dg1 "This'll be good to dance to!"

    scene v10cfrriau5
    with dissolve

    guyd "A little seductive for a dance battle though. Shouldn't it be a more upbeat song?"

    scene v10cfrriau6
    with dissolve

    dg1 "Not with these two beautiful ladies."

    scene v10cfrriau2a
    with dissolve

    au "Alright then, have a seat judges."

    scene v10cfrriau8 # TPP. Show dg1 and perry sat at table, show mc sat on edge of the table.
    with dissolve

    pause 0.5

    scene v10cfrriau9 # TPP. Show perry now sat at table, mouth open
    with dissolve

    guyd "Who's first?"

    scene v10cfrriau3a
    with dissolve

    ri "[name]?"

    menu:
        "Riley":
            scene v10cfrriau3b
            with dissolve

            u "Riley you're up."

            scene v10cfrriauhat # Putting down/ picking up hat
            with dissolve

            pause 0.5            

            scene v10cfrriau9other # FPP. Show Riley, on stage, mouth closed, stood normally.
            with dissolve

            pause 0.5

            scene v10cfrriau9a # FPP. Show Riley, on stage, mouth closed, legs slightly parted, arms held out to the side. 
            with dissolve

            pause 0.5

            # scene v10cfrriau9b # FPP. Show Riley, on stage, mouth closed, like this https://static1.bigstockphoto.com/8/9/1/large2/198566380.jpg
            # with dissolve

            # pause 0.5

            scene v10cfrriau9c # FPP. Same 9b, now leant towards front leg, palms on floor.
            with dissolve

            pause 0.5

            scene v10cfrriau9
            with dissolve

            pause 0.5

            scene v10cfrriau10 # FPP. Show riley now right infront of mc, mouth closed, seductive look.
            with dissolve

            dg1 "SHE KNOWS HOW TO WIN! WOOHOO!"

            scene v10cfrriau10a # FPP. Show riley now right infront of mc, mouth open, seductive look.
            with dissolve

            ri "The best dancers don't hold back."

            scene v10cfrriau2a
            with dissolve

            au "True, that's why I'm about to win."

            scene v10cfrriau11 # FPP. FPP. Show Aubrey, on stage, mouth closed, stood normally.
            with dissolve

            pause 0.5

            scene v10cfrriau11a # FPP. Show Aubrey bent forward blowing kiss
            with dissolve

            pause 0.5

            scene v10cfrriau11b # FPP. Show aubrey facing away from camera bent over touching the floor
            with dissolve

            pause 0.5

            scene v10cfrriau11c # FPP. Show aubrey stood up, body facing away from cam, head turned towards cam, blowing kiss, one hand on her ass.
            with dissolve

            pause 0.5

            scene v10cfrriau11
            with dissolve

            pause 0.5

        "Aubrey":
            ### ERROR: -If choose Aubrey ###
            scene v10cfrriau11 # FPP. FPP. Show Aubrey, on stage, mouth closed, stood normally.
            with dissolve

            u "Aubrey you're up."

            scene v10cfrriau11a # FPP. Show Aubrey bent forward blowing kiss
            with dissolve

            pause 0.5

            scene v10cfrriau11b # FPP. Show aubrey facing away from camera bent over touching the floor
            with dissolve

            pause 0.5

            scene v10cfrriau11c # FPP. Show aubrey stood up, body facing away from cam, head turned towards cam, blowing kiss, one hand on her ass.
            with dissolve

            pause 0.5

            scene v10cfrriau11
            with dissolve

            guyd "AND WE HAVE A WINNER!"

            scene v10cfrriau3b
            with dissolve

            dg1 "Slow your roll, show them what you got girl!"

            scene v10cfrriau3a
            with dissolve

            ri "Oh I will."

            scene v10cfrriau9 # FPP. Show Riley, on stage, mouth closed, stood normally.
            with dissolve

            pause 0.5

            scene v10cfrriauhat
            with dissolve

            pause 0.5
            
            scene v10cfrriau9a # FPP. Show Riley, on stage, mouth closed, legs slightly parted, arms held out to the side. 
            with dissolve

            pause 0.5

            scene v10cfrriau9b # FPP. Show Riley, on stage, mouth closed, like this https://static1.bigstockphoto.com/8/9/1/large2/198566380.jpg
            with dissolve

            pause 0.5

            scene v10cfrriau9c # FPP. Same 9b, now leant towards front leg, palms on floor.
            with dissolve

            pause 0.5

            scene v10cfrriau9
            with dissolve

            pause 0.5

            scene v10cfrriau10 # FPP. Show riley now right infront of mc, mouth closed, seductive look.
            with dissolve

            dg1 "SHE KNOWS HOW TO WIN! WOOHOO!"

    scene v10cfrriau8
    with dissolve

    dg1 "Good job to both of you, but it's pretty obvious who won."

    scene v10cfrriau9
    with dissolve

    guyd "Yeah sorry, but it's pretty obvious."

    scene v10cfrriau8
    with dissolve

    dg1 "Riley."

    scene v10cfrriau9
    with dissolve

    guyd "Aubrey."

    scene v10cfrriau2a
    with dissolve

    au "*Laughs* Guess that makes you the tie breaker [name] so who won?"

    menu:
        "Riley":
            scene v10cfrriau3b
            with dissolve

            u "I gotta give it to Riley."

            scene v10cfrriau9
            with dissolve

            guyd "Guess a man knows what he likes."

            scene v10cfrriau8
            with dissolve

            dg1 "I think you both did good."

            scene v10cfrriau2a
            with dissolve

            au "Guess my little show wasn't good enough for you."

            scene v10cfrriau2b
            with dissolve

            u "I just-"

            scene v10cfrriau2a
            with dissolve

            au "*Laughs* I'm just messing with you."

            scene v10cfrriau3
            with dissolve

            ri "Good battle, loser. *Chuckles*"

            scene v10cfrriau2a
            with dissolve

            au "We'll rematch again."

            scene v10cfrriau3
            with dissolve

            ri "Someday."

            scene v10cfrriau2a
            with dissolve

            au "Thanks [name]."

            scene v10cfrriau2b
            with dissolve

            u "No problem, see you guys later."

            call screen v10s33_stage

        "Aubrey":
            scene v10cfrriau2b
            with dissolve

            u "I gotta give it to Aubrey."

            scene v10cfrriau9
            with dissolve

            guyd "Guess a man knows what he likes."

            scene v10cfrriau8
            with dissolve

            dg1 "I think you both did good."

            scene v10cfrriau3
            with dissolve

            ri "These male judges are too easily influenced."

            scene v10cfrriau2a
            with dissolve

            au "Should I rub it in now or later? *Chuckles*"

            scene v10cfrriau3
            with dissolve

            ri "Oh wow, you just wait till we have some proper judges..."

            scene v10cfrriau2a
            with dissolve

            au "Can't wait to see that. *Laughs*"

            call screen v10s33_stage

    label v10s33_amber1:
    # -if things are awkward with Amber after the skatepark-   
    
    if v10_amber_awkward:
        scene fr6mudwrestling

        u "(Things are a bit awkward between us, I'd rather avoid her today.)"

        call screen v10s33_mudwrestling

    $ freeroam6.add("amber")
    scene v10cfram1 #FPP Show Amber, Looking at mc, flirty smile, mouth open
    #with dissolve

    am "Hey handsome!"

    scene v10cfram1a #same 1, mouth closed
    with dissolve

    u "You're not looking bad yourself."

    scene v10cfram1
    with dissolve

    am "I know what you're here for."

    scene v10cfram1a
    with dissolve

    u "And what's that?"

    scene v10cfram1
    with dissolve

    am "The mud wrestling duh?"

    scene v10cfram1a
    with dissolve

    u "I'm just here to-"

    scene v10cfram1b # same 1, wide smile, mouth open
    with dissolve

    am "Oh please, remember who you're talking to. *Chuckles*"

    scene v10cfram1c #same 1c, mouth closed
    with dissolve

    u "Yeah, you're right. I can't wait for it."

    scene v10cfram1
    with dissolve

    am "I'm looking forward to a good little catfight. It would be even better though if it was the guys doing the wrestling."

    scene v10cfram1a
    with dissolve

    menu:
        "Witty retort":
            $ add_point(KCT.TROUBLEMAKER)
            u "Ha, you just wanna see me shirtless wrestling other guys."

            scene v10cfram1
            with dissolve

            am "Isn't that why you're here?"

            scene v10cfram1a
            with dissolve

            u "Yeah of course."

            scene v10cfram1
            with dissolve

            am "Ha, so I'm not the only one wanting to see the guys wrestle."

            scene v10cfram1a
            with dissolve

            u "*Chuckles* You know that's not what I meant."

        "Flirt":
            $ add_point(KCT.BOYFRIEND)
            u "And here I was thinking you wanted to put on a little show for me."

            scene v10cfram1
            with dissolve

            am "Maybe another time, haha."

            scene v10cfram1a
            with dissolve

            u "*Laughs*"

    if v10_help_nora_freeroam:
        menu:
            "Invite her to Europe":
                u "Are you going on the Europe trip?"

                scene v10cfram1d # same 1, amber curious, mouth open
                with dissolve

                am "What Europe trip?"

                scene v10cfram1e #same 1d, mouth closed
                with dissolve

                u "A few of us are going, Nora is setting it up. I'm going."

                scene v10cfram1d
                with dissolve

                am "Yeah, I'd go."

                scene v10cfram1e
                with dissolve

                u "Cool."

            "Don't invite her":
                u "(She'll find out about it and go if she wants to.)"

    scene v10cfram1b
    with dissolve

    am "Gonna go get ready for the big show."

    scene v10cfram1c
    with dissolve

    u "You do that."

    call screen v10s33_mudwrestling

    label v10s33_chris1:

    if not joinwolves:
        if v10s33_toldChloe:
            scene fr6bagtossnonora
        else:
            scene fr6bagtoss
        
        u "I should probably not be seen talking to the Wolves' frat leaders."

        call screen v10s33_bagtoss

    $ freeroam6.add("chris")
    
    scene v10cfrch1 #FPP showing Aaron and Chris looking at each other, like they were talking
    #with dissolve

    u "Hey Aaron, it's great to see you back man, but where the hell did you go? You just vanished on us?"

    scene v10cfrch2 #FPP showing Aaron closeup,looking at mc, slight smile, mouth open
    with dissolve

    aa "Yeah man, I had to fly out and take care of my Aunt, she got really sick. I asked Chris to keep it under wraps."

    scene v10cfrch2a #same as 2, mouth closed
    with dissolve

    u "Oh fuck man, is everything okay?"

    scene v10cfrch3 #FPP showing Chris closeup,looking at mc, slight smile, mouth open
    with dissolve

    ch "He's cool now and he's back where he belongs, but because of her support network he was a little worried he may not be able to return to college."

    scene v10cfrch2a
    with dissolve

    u "Well, glad to see you're back."

    scene v10cfrch2
    with dissolve

    aa "Yeah everything is fine now. My mom and dad actually moved her in with them until she recovers, but things are looking good."

    scene v10cfrch3b
    with dissolve

    ch "Now that you're back man, you and [name] should play a game. First one to get one in is the Wolves' new President. *Laughs*"

    scene v10cfrch3b # Show Aaron
    with dissolve

    menu:
        "Play":
            scene v10cfrch2
            with dissolve

            u "Let's go Aaron."

            scene v10cfrdg23 
            with dissolve

            pause 0.8

            scene v10cfrdg24
            with vpunch

            pause 0.8

            scene v10cfrch4 # showing Aaaron throwing version 1
            with dissolve

            pause 0.8

            scene v10cfrdg24b 
            with vpunch

            scene v10cfrdg23a 
            with dissolve

            pause 0.8

            scene v10cfrdg24a
            with vpunch

            pause 0.8

            scene v10cfrch4a # showing Aaaron throwing version 2
            with dissolve

            pause 0.8

            scene v10cfrdg24 
            with vpunch

            scene v10cfrdg23b 
            with dissolve

            pause 0.8

            scene v10cfrdg24b 
            with vpunch

            pause 0.8

            scene v10cfrch4b # showing Aaaron throwing version 3
            with dissolve

            pause 0.8

            scene v10cfrdg24c # closeup bag hitting the hole
            with vpunch

            aa "Hand over the crown Chris. *Laugh*"

            u "Damnit."

            scene v10cfrch2a
            with fade

            u "Okay, I'ma check out some other stations. I'll see you guys around."

            scene v10cfrch2
            with dissolve

            aa "See ya, good catching up."

        "Don't play":
            u "I don't want to hurt anyone's feelings over a game, I'm too good at this, it wouldn't be fair."
            u "Also, the presidency is all yours Chris. *Laughs*"

            scene v10cfrch3
            with dissolve

            ch "Fair enough."

            scene v10cfrch2a
            with dissolve

            u "I'll see you guys around."

            scene v10cfrch2
            with dissolve

            aa "See ya, good catching up."

    call screen v10s33_bagtoss

    label v10s33_nora1:
    $ freeroam6.add("nora")

    scene v10cfrno1 # fpp, from the side, nora playing bag toss, mouth closed concentrated
    #with dissolve

    u "So... you good at this?"

    scene v10cfrno1b # same 1, nora looking at mc, mouth open
    with dissolve

    no "I'm more than good. I'm actually the one that suggested it to Autumn."
    no "A lot of us Chicks offered to help out today."
    no "Girls supporting girls and all that."

    scene v10cfrno1c #same 1b, mouth closed
    with dissolve

    menu:
        "Show me what you got":
            $ add_point(KCT.BRO)

            u "You should show me what you got... since you're such a pro."

            scene v10cfrno1b
            with dissolve

            no "I can manage that."

            scene v10cfrno1d #same 1b, Nora throws version 1
            with dissolve

            pause 0.8

            scene v10cfrno2 # closeup bag goes in version 1
            with vpunch

            pause 0.8

            scene v10cfrno1e #same 1b, Nora throws version 2
            with dissolve

            pause 0.8

            scene v10cfrno2a # closeup bag goes in version 2
            with vpunch
            
            pause 0.8

            scene v10cfrno1f #same 1b, Nora throws version 3
            with dissolve

            pause 0.8

            scene v10cfrno2b # closeup bag goes in version 3
            with vpunch

            u "Woah, you really are good."

            scene v10cfrno3 #fpp nora normal stace, looking at mc, mouth open, confident smile
            with dissolve

            no "Told you."

            scene v10cfrno3a # same 3, mouth closed
            with dissolve

            u "Sorry for doubting your skill."

            scene v10cfrno4 # DG2 hands Nora a voucher for lingerie at an adult store (not the one on the shelf, cause it's just a representative)
            with dissolve

            dg2 "Here you go!"

            scene v10cfrno3b # same 3, nora looks down at the voucher, mouth closed, a bit surprised
            with dissolve

            u "Interesting prize, I heard that lingerie store called Oli's gets a lot of customers."

            scene v10cfrno3d #same 3b, (she's put her arms down so the voucher is no longer in the shot) Nora looks up at mc, annoyed
            with dissolve

            no "Too bad I won't be using it."

            scene v10cfrno3e #same 3d, mouth closed
            with dissolve

            u "Why not?"

            scene v10cfrno3d
            with dissolve

            no "Who am I gonna wear it for? Myself? Chris is too busy to see me on a regular day."

            scene v10cfrno3e
            with dissolve

            u "Ahh, not my business."

        "Ask about sorority life":
            $ add_point(KCT.BOYFRIEND)
            $ v10_nora_bitch_about_chloe = True
            u "How's sorority life?"

            scene v10cfrno3d
            with dissolve

            no "Drama as always."

            scene v10cfrno3e
            with dissolve

            u "What do you mean?"

            scene v10cfrno3d
            with dissolve

            no "Chloe's just doing more of what Chloe does."

            scene v10cfrno3e
            with dissolve

            u "And what is that?"

            scene v10cfrno3d
            with dissolve

            no "Being fake. Acting like a little fragile flower."

            scene v10cfrno3e
            with dissolve

            menu:
                "What do you mean?":
                    $ add_point(KCT.BRO)
                    u "What do you mean by that?"

                    scene v10cfrno3d
                    with dissolve

                    no "I just feel like she's fake. She pretends to be all fragile so she can get sympathy points from people."
                    no "Just yesterday I heard her making a fuss in the hallway because Aubrey called her \"cute\". Like, are you kidding me?"

                    scene v10cfrno3e
                    with dissolve

                    u "She can be a little... extra sometimes."

                "Defend Chloe":
                    $ add_point(KCT.BOYFRIEND)
                    u "Well, she might be acting that way because of all the pressure she's under. Conversations behind her back probably aren't helping with that."

                    scene v10cfrno3d
                    with dissolve

                    no "I'm not saying anything that isn't true, and I'm not saying anything I wouldn't say to her face."

                    scene v10cfrno3e
                    with dissolve

                    u "Right."

    u "I'm gonna go check out some of the other booths."

    scene v10cfrno3d
    with dissolve

    no "Okay."

    call screen v10s33_bagtoss

    label v10s33_ryan1:
        $ freeroam6.add("ryan")

        scene v10cfrry1 # FPP. Close up Ryan stood by the central aisle, Ryan smile, mouth closed.

        u "Hey man! Enjoying yourself?"

        scene v10cfrry1a # FPP. Same as 1, smile, mouth open.
        with dissolve

        ry "Big time."

        scene v10cfrry1
        with dissolve

        u "What have you been doing?"

        scene v10cfrry1a
        with dissolve

        ry "Well to be honest there's this amazing girl I've kinda been following around. She and I spoke for a little bit and just wow. She's beautiful, smart, funny, just everything."

        scene v10cfrry1
        with dissolve

        u "Where is she?"

        scene v10cfrry1a
        with dissolve

        ry "Oh I'm not gonna tell you, so you can swoop in and steal her. I'm good, thanks."

        scene v10cfrry1
        with dissolve

        u "Haha, c'mon man. For real, point her out to me."

        scene v10cfrry1a
        with dissolve

        ry "Even your laugh sounds like you have an evil plan, I'll pass."

        scene v10cfrry1
        with dissolve

        u "At least tell me her name."

        scene v10cfrry1a
        with dissolve

        ry "You just don't know when to give up."

        scene v10cfrry1
        with dissolve

        u "Okay, I'll leave it alone."

        scene v10cfrry1b # FPP. Same as 1, looking down awkwardly, mouth cloused.
        with dissolve

        u "What?"

        scene v10cfrry1c # FPP. Same as 1, ryan back at camera, awkwardly, mouth open.
        with dissolve

        ry "Okay look, don't be mad, but the girl I'm talking about is Emily."
        ry "I know you guys dated, but I... I really like her. Is it okay with you if I ask her out?"

        scene v10cfrry1d # FPP. Same as 1, ryan looking at camera, awkwardly, mouth closed.
        with dissolve

        menu:
            "It's okay":
                $ add_point(KCT.BRO)
                $ ryan.points += 1
                $ v10s33_ryan_flirt_emily = True

                u "Don't you think it's weird to date your friend's ex? You can do what you want though, it doesn't bother me."

                scene v10cfrry1a
                with dissolve

                ry "For real? Dude I'm so glad you're not pissed. So, any pointers? What's the fastest way I can get her in the bed?"

                scene v10cfrry1
                with dissolve

                u "Bro, you're doing a little too much."

                scene v10cfrry1a
                with dissolve

                ry "My bad. But thanks, I'm gonna go talk to her."

                scene v10cfrry2 # FPP. Show Ryan walking over to Emily, Emily awkward, ryan confident, mouths closed.
                with dissolve

                pause 0.75
                
                scene v10cfrry3 # TPP. Show Ryan and Emily talking, Ryan mouth open.
                with dissolve

                ry "Hey gorgeous, how about you and I get out of here together."

                scene v10cfrry3a # TPP. Same as 3, emily awkward smile, mouth open.
                with dissolve

                em "Uhm... sorry, hard pass."

                scene v10cfrry3b # TPP. Same as 3, ryan dissapointed, emily awkward smile, ryan mouth open.
                with dissolve

                ry "Yeah yeah, uhm... that's cool. See you around."

            "It's not okay": 
                $ add_point(KCT.TROUBLEMAKER)
                u "You would really ask me that? Why would I be cool with my friend dating my ex?!"

                scene v10cfrry1c
                with dissolve

                ry "I just thought... nevermind. I get it. Later man."

        scene v10cfrry4 # FPP. Show Ryan walking to wherever he is in his appearance at the toilets.
        with dissolve

        pause 0.75

        call screen v10s33_centeraisle

    label v10s33_toiletryan1:
        $ freeroam6.add("ryan2")
        scene v10cfrry5 # FPP. Show Ryan at the toilets, Ryan slight upset, mouth closed.
        u "(He looks upset.)"

        if not v10s33_ryan_flirt_emily:
            u "Hey man, I didn't mean to ruin your mood."

            scene v10cfrry5a # FPP. Same as 5, ryan slight upset, mouth open.
            with dissolve

            ry "It's fine."

            scene v10cfrry5
            with dissolve

            u "There's plenty of girls here that would be happy to talk to you."
            u "Have you checked out the Win A Date booth? That girl's alright, go get a ticket."

            scene v10cfrry5a
            with dissolve

            ry "I'm good man, honestly I just want to be left alone."

            scene v10cfrry5
            with dissolve

            u "You like her like that huh?"

            scene v10cfrry5a
            with dissolve

            ry "Yeah..."

            scene v10cfrry5
            with dissolve

            u "Alright man, I'll leave you alone."

        else:
            u "Hey man, you good?"

            scene v10cfrry5a 
            with dissolve

            ry "No..."

            scene v10cfrry5
            with dissolve

            u "What's wrong?"

            scene v10cfrry5a
            with dissolve

            ry "I talked to Emily and she completely rejected me..."

            scene v10cfrry5a
            with dissolve

            u "Damn man, sorry to hear that. There's plenty of girls here that would be happy to talk to you."
            u "Have you checked out the Win A Date booth? That girl's alright, go get a ticket."

            scene v10cfrry5
            with dissolve

            ry "I'm good man, honestly I just want to be left alone."

            scene v10cfrry5
            with dissolve

            u "You like her like that huh?"

            scene v10cfrry5a
            with dissolve

            ry "Yeah..."

            scene v10cfrry5
            with dissolve

            u "Alright man, I'll leave you alone."

        call screen v10s33_toilet

label v10s33_emily1:
    $ freeroam6.add("emily")

    if not forgiveemily:
        if v10s33_toldChloe:
            scene fr6benchchloenoraatmudwrestling
        else:
            scene fr6bench

        u "(I don't feel like talking to her.)"
        
        call screen v10s33_bench

    scene v10cfrem1a #FPP, shows emily sat on the bench from the side as if mc is sitting next to her, looking at mc cute smile, mouth closed

    u "Hey, why aren't you looking around like everyone else?"

    scene v10cfrem1 # same 1a, mouth open
    with dissolve

    em "I've been walking around all morning. I just needed a breather, I'm getting a little nervous about the mud wrestling event."

    scene v10cfrem1a
    with dissolve

    u "Wait, you're in it?"

    scene v10cfrem1b #same 1, emily nervous, mouth open
    with dissolve

    em "Yep, I don't know why I agreed to do it. I'm super nervous."

    scene v10cfrem1c #same 1b, mouth closed
    with dissolve

    u "I'm surprised, but if you're nervous why don't you just back out?"

    scene v10cfrem1b
    with dissolve

    em "It's too late for all that, I'd ruin the event if I didn't do it. Definitely don't want everyone to be upset because of me."

    scene v10cfrem1c
    with dissolve

    u "True, that's definitely not a good look."

    scene v10cfrem1b
    with dissolve

    em "All the guys here just came to look at a bunch of cute girls."

    scene v10cfrem1c
    with dissolve

    u "And you're in the event so that means you're one of those cute girls."

    scene v10cfrem1
    with dissolve

    em "*Chuckles* Whatever."

    scene v10cfrem1a
    with dissolve

    if v10_help_nora_freeroam:
        menu:
            "Invite her to Europe":
                $ emily_europe = True
                u "Oh, while it's on my mind. Do you want to go on the Europe trip with me and some others?"

                scene v10cfrem1d #same 1, happy, slightly surprised, mouth open
                with dissolve

                em "You're actually inviting me?"

                scene v10cfrem1e #same 1d, mouth closed
                with dissolve

                u "Yeah. I think it'll be fun."

                scene v10cfrem1d 
                with dissolve

                em "It does sound fun."

                scene v10cfrem1e
                with dissolve

                u "I'm not sure about all the details. but I know we're going to some pretty cool places."

                scene v10cfrem1d
                with dissolve

                em "I don't see why I wouldn't want to go. Especially since you're inviting me."

                scene v10cfrem1e
                with dissolve

                u "Great!"

            "Don't invite her":
                u "(I honestly don't know if I want her there.)"

    u "I'm pretty sure the event starts soon, I wanna make sure I get around before it does."

    scene v10cfrem1
    with dissolve

    em "See you around then, wish me luck."

    scene v10cfrem1a
    with dissolve

    u "Good luck."

    call screen v10s33_bench
    
    label v10s33_evelyn1:
    $ freeroam6.add("evelyn")

    if evelyn.relationship >= Relationship.LIKES: #If Date successful
        scene v10cfrev1a

        u "Out of everyone here, I'm most surprised to see you."

        scene v10cfrev1b #same 1, evelyn smile, mouth open
        with dissolve

        ev "I'm surprised to see you here too."

        scene v10cfrev1c #same 1b, mouth closed
        with dissolve

        u "So you're into mud wrestling?"

        scene v10cfrev1b
        with dissolve

        ev "Uhm, no. *Chuckles* I'm here for the charity. I love events like this, community things always make me happy."

        scene v10cfrev1c
        with dissolve

        u "It is nice seeing everyone in one place. It feels nice."

        scene v10cfrev1b
        with dissolve

        ev "Maybe they should sell tickets to the toilet so people can go when they need to, I'm sure that would bring in some money. *Chuckles*"

        scene v10cfrev1c
        with dissolve

        u "Was that a joke you just made? Didn't see that coming? I'm a little proud. Guess there's still a lot I have to learn about you."

        scene v10cfrev1b
        with dissolve

        ev "There definitely is. We could make that happen by going on a second date. I think it's about time we do."

        scene v10cfrev1c
        with dissolve
        menu:
            "Let's do it right now":
                $ add_point(KCT.BOYFRIEND)
                $ v10s33_ev_date_now = True
                u "Wanna go now?"

                scene v10cfrev1b
                with dissolve

                ev "Someone's eager. *Chuckles* Soon, but let's enjoy the event for today."

            "I'll think about it":
                $ add_point(KCT.TROUBLEMAKER)
                u "I'll think about it. *Chuckles*"

                scene v10cfrev1b
                with dissolve

                ev "You do that."

        scene v10cfrev1c
        with dissolve

        u "Well, I'll see you around then."

        call screen v10s33_toilet

    elif evelyn.relationship >= Relationship.DATE: #if Date but unsuccessful
        if not "ryan" in freeroam6:
            scene fr6toilet # toilet screen
        else:
            scene fr6toiletwithryan

        u "(What's she doing here? I'd rather avoid her after how our date went.)"

        call screen v10s33_toilet

    else: #if no date with Evelyn
        scene v10cfrev1a #fpp, shows evelyn looking at mc, neutral expression mouth closed

        u "Out of everyone here, I'm most surprised to see you."

        scene v10cfrev1 #same 1a, mouth open
        with dissolve

        ev "Do I know you?"

        scene v10cfrev1a
        with dissolve

        u "Uhm, it's me [name], I bought that costume a while back."

        scene v10cfrev1
        with dissolve

        ev "Oh yeah."

        scene v10cfrev1a
        with dissolve

        u "Lots of new customers asking for costumes?"

        scene v10cfrev1
        with dissolve

        ev "Nope, just you."

        scene v10cfrev1a
        with dissolve

        u "(Okay, someone isn't interested in talking.)"

        u "Well, see you around."

        call screen v10s33_toilet

label v10s33_deergirl41:
    if "riley" in freeroam6:
        scene fr6thriftnoriley

    else:
        scene fr6thrift

    u "(I'd rather not get talked into buying one of these hats.)"
    
    call screen v10s33_thrift