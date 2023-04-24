label v12s7_free_roam_spoken(backgroundImg, returnScreen, seenList, victim):
    $ v12s7_seenList = seenList

    show screen murder_button_overlay(victim)

    scene expression backgroundImg
    u "(I've already spoken to them, but I could still murder them)"
    scene black
    $ renpy.call_screen(returnScreen)

label v12s7fr:
    image ferry_depart = Movie(play="images/v12/Scene 7/animations/Ferry A - From UK.webm", loop=False)
    
    scene ferry_depart
    with fade
    play sound "images/v12/Scene 7/animations/Track Scene - Ferry Ride (5 sec).mp3"

    pause 3.5

    $ v12s7_victims = 12
    $ v12s7_victims += sum([ v11_invite_sam_europe, emily_europe, josh_europe, v11_pen_goes_europe ])

    scene v12fer1 # FPP. Show Mr Lee, smiling mouth open
    with fade

    lee "Students, please gather around. I have something very exciting to announce."

    play music "music/v12/Track Scene 7_1.mp3" fadein 2

    scene v12fer2 # TPP. Show Aubrey,riley, mc, imre all mouths closed
    with dissolve

    pause 0.75

    scene v12fer1
    with dissolve

    lee "First of all, it's been brought to my attention that many of you were unaware that we'd be taking the ferry rather than flying."
    lee "This was a last-minute adjustment, so I do apologize. Although, I think this voyage will be well worth it."

    if v11_invite_sam_europe:
        scene v12fer3 # FPP. Show cameron, annoyed look, mouth open
        with dissolve

        ca "It's costing me a lot of money to look out for you, ya know?"

        scene v12fer4 # FPP. Show samantha, looking fed up, mouth open
        with dissolve

        sa "Then go home."

    scene v12fer1
    with dissolve

    lee "As you all know, I take great pride in seizing every opportunity I can to teach my students and this ferry ride will be no different."
    lee "Decades ago, a famous murder was committed on this ferry. A murder that we will, in a way, be re-enacting."

    scene v12fer5 # FPP. Show riley, excited, mouth open
    with dissolve

    ri "Wait, will we be playing characters?!"

    scene v12fer6 # FPP. Show Aubrey, smiling mouth open
    with dissolve

    au "I hope so. Murder and roleplay? I'm getting a little too excited... *Chuckles*"

    scene v12fer5
    with dissolve

    ri "*Laughs* I hope you don't have to play a virgin nun."

    scene v12fer1
    with dissolve

    lee "Each student will be given a role to play because we will be re-enacting this murder by playing a murder mystery."

    scene v12fer7 # FPP. Show Mr Lee handing riley a role card
    with dissolve

    pause 0.75

    scene v12fer8 # FPp. Show Mr Lee handing Aubrey a role card
    with dissolve

    pause 0.75

    scene v12fer9 # FPP. Mr. Lee hands MC his card that says Famous Boxer and Murderer in the corner
    with dissolve

    u "(Well, would you look at that. Looks like I'm going to be getting some blood on these hands.)"

    scene v12fer1
    with dissolve

    lee "On each card there is a detailed description of the character you'll be playing. As well as a marker saying whether or not you are the murderer."

    scene v12fer10 # FPP. Show Imre, neutral look mouth open
    with dissolve

    imre "Can we please just choose our characters instead?"

    scene v12fer1
    with dissolve

    lee "You can not. I purposefully chose the roles you are each being given."
    lee "As I said, one of you is the murderer and it's the murderer's job to kill as many students as they can without being caught. Once the murderer is discovered, the game is over."

    scene v12fer10
    with dissolve

    imre "Wait, really?"

    scene v12fer1
    with dissolve

    lee "Yes."

    scene v12fer10a # FPP. same 10, hand in air, excited look mouth open
    with dissolve

    imre "YEAHHH BOY!"

    scene v12fer1
    with dissolve

    lee "*Sighs* Why does that excite you, Imre?"

    scene v12fer10
    with dissolve

    imre "Because, I'll just find out who the murderer is and force them to fess up and then boom, game over and I can sleep the rest of the boat ride. *Laughs*"

    scene v12fer1
    with dissolve

    lee "That's not possible."

    scene v12fer10
    with dissolve

    imre "How is it not? It doesn't break any rules."

    scene v12fer1
    with dissolve

    lee "As a matter of fact, it does. Students will be FORBIDDEN from breaking character until the murderer has been identified."

    scene v12fer10
    with dissolve

    imre "And what happens if we do?"

    scene v12fer1
    with dissolve

    lee "Do you know how to swim, Imre?"

    scene v12fer10
    with dissolve

    imre "Yeah...?"

    scene v12fer1
    with dissolve

    lee "Good. Because after you choose to break character, you'll be swimming to Paris."

    scene v12fer10b # FPP. same 10, show imre laughing, mouth slightly open
    with dissolve

    imre "*Laughs*"

    scene v12fer10c # FPP. Same 10, show imre nervous, mouth open
    with dissolve

    imre "Oh, you're not joking."

    scene v12fer13
    with dissolve
    
    am "What if the killer never gets caught? *Laughs*"

    scene v12fer1
    with dissolve

    lee "That would be very, very impressive and also requires the murderer to be a great listener, someone who is very perceptive, and also a person who can smooth through conversations easily." 

    scene v12fer1a
    with dissolve

    lee "Those three are key."

    scene v12fer6
    with dissolve

    au "Okay, so... Do we get anything for doing this? Besides it being fun and something to keep us busy... *Chuckles*"

    scene v12fer1
    with dissolve

    lee "Based on how well the murderer does, and how many kills they achieve... I might be able to think of some type of reward. But, it must wait until Amsterdam to take place as our Paris schedule is already very full."

    scene v12fer12a
    with dissolve

    ry "*Scoffs* So if we aren't the murderer, our only goal is to not get killed? And we don't get rewarded for it?"

    scene v12fer1
    with dissolve

    lee "I know this sounds... Unfair. All in all, the mass murder we will be reenacting today was not fair to the victims."
    lee "Your goal is to make sure the murderer does not get a reward, by catching them as soon as possible." 
    lee "Now, If the murderer does get a reward... I suppose the \"prize\" could be something catered for two. So the murderer will have to share it with one of his or her victims... Fair?"

    scene v12fer12a
    with dissolve

    ry "I mean... I guess?"

    scene v12fer1a # FPP. same 1, pointing towards students, (not directly at the camera but close to it)
    with dissolve

    lee "Let me emphasize that again, DO NOT BREAK CHARACTER. If you think you're safe from prying eyes and free to do whatever you please, you're not."
    lee "You must assume that I'm always there watching, because I will be. If you have something to say, you must say it in character."

    scene v12fer5
    with dissolve

    ri "*Southern Accent* Once again, the wealthy are being brought down by the ways of the lazy."

    scene v12fer1
    with dissolve

    lee "And that's why she's my favorite student! Already playing her rich woman role."

    scene v12fer10e # FPP. same 10, annoyed look, hands up in annoyance, mouth open, pose something like this https://www.psychmechanics.com/wp-content/uploads/2015/06/angry-expression-e1595044726433.jpg
    with dissolve

    imre "BRO WHAT?! YOU MADE ME SOMEONE'S WIFE?!?!"

    scene v12fer11 # FPP. Show charli, laughing, mouth open
    with dissolve

    charli "*Laughs*"

    scene v12fer12 # FPP. Show ryan laughing, mouth open
    with dissolve

    ry "*Laughs*"

    scene v12fer1
    with dissolve

    lee "I wouldn't be so quick to laugh, Ryan. You're playing his spouse."

    scene v12fer12a # FPP. Same 12, unhappy, mouth open
    with dissolve

    ry "WAIT, WHAT?"

    scene v12fer11
    with dissolve

    charli "*Laughs* Welcome to the club \"rainbow unicorn\"."

    scene v12fer10d # FPP. Same 10, annyoed look, mouth open, 
    with dissolve

    imre "I don't care if I have to act like a girl or not, I'll still beat your ass Charli."

    scene v12fer1
    with dissolve

    lee "That won't be possible either. Students, please understand something. I, as your teacher, see and observe everything. Your personalities, your interactions with each other, etc."
    lee "The roles I've chosen for you are intended to help you or for my own personal enjoyment. Charli will be playing the role of the Captain."

    scene v12fer11
    with dissolve

    charli "Ooh, I like the sound of that. A position of authority."

    scene v12fer1
    with dissolve

    lee "And with power comes great responsibility. So, you will be limited to the Captain's Quarters at all times."

    scene v12fer11a # fPP. same 11, neutral, mouth open
    with dissolve

    charli "I'm not able to walk around the ship?"

    scene v12fer1
    with dissolve

    lee "You are not."

    scene v12fer11a
    with dissolve

    charli "*Scoffs* Then how could I possibly catch the murderer?"

    scene v12fer1
    with dissolve

    lee "You'll have to depend on your security, Amber. You'll also be able to make announcements over the PA."

    scene v12fer11a
    with dissolve

    charli "Hmm, I guess that'll do."

    scene v12fer13 # FPP. Show amber, slight smile mouth open
    with dissolve

    am "Ahh yeah, I'm so ready to play into this. I'm not holding back either. This was probably the worst role I could've been given."

    scene v12fer1
    with dissolve

    lee "Or the best."

    scene v12fer14 # FPP. Show Chloe, neutral look, mouth open
    with dissolve

    cl "So how do we know who the murderer is? Like, how will they \"kill\" people?"

    scene v12fer1
    with dissolve

    lee "The murderer will kill people by pointing at them with a fake finger gun. If you get killed then quietly make your way to the dining hallway. Do not give any hints to any of the players that haven't been killed."

    scene v12fer10d
    with dissolve

    imre "Wait, so-"

    scene v12fer1
    with dissolve

    lee "Using any sort of loophole as a way to sabotage the game will result in you getting thrown overboard."

    scene v12fer10d
    with dissolve

    imre "*Chuckles* You can't actually throw us overboard."

    scene v12fer1
    with dissolve

    lee "Oh? I'm pretty sure your school waiver says I can do anything with the intention of education as long as it doesn't harm the students. And you'll definitely be learning a lesson as you struggle your way to Paris."

    scene v12fer10d
    with dissolve

    imre "Okay, fine. I won't mess up your stupid game."

    scene v12fer1
    with dissolve

    lee "Very good. Again everyone, the only way the murderer gets caught is by someone witnessing the crime. Does anyone have any questions?"

    scene v12fer10d
    with dissolve

    imre "Umm, is it okay if I just don't play at all?"

    scene v12fer1
    with dissolve

    lee "Do you have a reason for skipping the activity other than just not wanting to?"

    scene v12fer10d
    with dissolve

    imre "..."

    scene v12fer1
    with dissolve

    lee "I'm not giving you time to think of one, Imre."

    lee "Everyone will be participating. If that's all then please, grab some props that fit your role and enjoy the murder mystery."

    scene v12fer15 # FPP. show chloe, riley and ryan at a chest looking for props.
    with dissolve

    pause 0.75

    scene v12fer16 # TPP. Show MC grabbing boxing gloves from the chest
    with dissolve

    pause 1.5

    # Murder Mystery Tutorial
    show murder_tutorial1 at truecenter
    pause
    hide murder_tutorial1

    show murder_tutorial2 at truecenter
    pause
    hide murder_tutorial2

    if (v12s7_victims == 16) or (v12s7_victims == 15 and joinwolves):
        show murder_tutorial3 at truecenter
        pause
        hide murder_tutorial3
    else:
        show murder_tutorial3b at truecenter
        pause
        hide murder_tutorial3b

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_seating_front

label v12s7_aubrey1:
    $ freeroam9.add("aubrey")
    $ v12s7_seenList = [nora]

    show screen murder_button_overlay(aubrey)

    scene v12ferau1 # FPP. Note for renderer, all scene images starting v12ferau will be the first conversation with Aubrey on the upper front balcony of the boat. Her and Nora are both up there but the conversations are completely seperate. Show Aubrey, flirty look, mouth open
    #with dissolve

    au "Hey there, handsome. Please make sure you're being careful, okay? I'd hate for you to get hurt, but if you do find yourself needing some love and care, don't forget to come see your favorite nurse. *Chuckles*"

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    scene v12ferau1a # FPP. Same 1, mouth closed
    with dissolve

    u "Well, my travelling nurse may get a little jealous."
    
    u "As a world-famous boxer I'm always getting bumps and bruises so I have to travel with a nurse, but I wanted a little break from everyone so she's not here."
    u "I actually do have a little pain from my last fight, but that's to be expected after all the adrenaline's worn off."

    scene v12ferau1
    with dissolve

    au "Aww, you poor thing. Don't force yourself to sit in pain. I can help work out the tension if you'd like?"

    scene v12ferau1a
    with dissolve

    u "*Chuckles* I'm fine, trust me."

    scene v12ferau1
    with dissolve

    au "If you say so. *Chuckles* So, tell me about that last fight of yours. I don't get to see much of the outside world since I'm always working on the ship. Was it a pretty big fight?"

    menu:
        "Major fight":
            $ reputation.add_point(RepComponent.BRO)
            scene v12ferau1a
            with dissolve

            u "It was a serious fight. I'm surprised you haven't heard about it yet. It feels as if the whole world watched it."

        "Light work":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            scene v12ferau1a
            with dissolve

            u "Nah, it was light work. No fight is a big fight for me anymore."

            scene v12ferau1
            with dissolve

            au "*Laughs*"

    scene v12ferau1a
    with dissolve

    u "So this is how it starts. The bell rings and he just dashes towards me throwing swing after swing. I'm dodging and weaving, dodging and weaving. He's not landing a single hit."

    scene v12ferau1b # FPP. same as 1, hand on hip mouth open
    with dissolve

    au "Wowww! You're that good, huh?"

    scene v12ferau1c # FPP. same as 1a, hand on hip, mouth closed
    with dissolve

    u "Never lost a fight."

    scene v12ferau1b
    with dissolve

    au "Ooh, impressive. *Chuckles* What happened next?"

    scene v12ferau1c
    with dissolve

    u "So like I said, I'm dodging every swing and thinking that he's got nothing on me."
    u "I end up getting a little cocky and drop my arms to taunt him a bit, when suddenly out of nowhere he slugs me real good right across the jaw."
    u "He didn't knock me out, but the hit was just hard enough for me to start taking the fight a little bit more seriously."

    scene v12ferau1
    with dissolve

    au "Is that why you're hurting a bit, from the jaw punch?"

    scene v12ferau1a
    with dissolve

    u "That punch and many more."

    scene v12ferau1b
    with dissolve

    au "So how'd you come back and win it after that horrible hit?"

    scene v12ferau1c
    with dissolve

    u "Apparently he could tell how good of a hit he got on me because with a big smile on his face he began raising his hands in the air as if he had won, and that was all I needed to finish him."

    scene v12ferau1b
    with dissolve

    au "*Gasps* Finish him?! *Chuckles*"

    scene v12ferau1a
    with dissolve

    u "*Chuckles* I hit him as hard as I could square in the gut. Then again and again until he couldn't even manage to block himself."
    u "He clung on to me in an attempt to not fall down. Finally, I landed my last gut punch as hard as I could and he fell to the ground, knocked out cold."

    scene v12ferau1d # FPP. same as 1, slight worried look, mouth open, hands linked like this https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.shutterstock.com%2Fnb%2Fvideo%2Fclip-34665853-close-up-wringing-nervous-woman-hands&psig=AOvVaw2gzL8mvR-BApik2Uv-BwlR&ust=1626649215565000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCLjcw9ua6_ECFQAAAAAdAAAAABAO
    with dissolve

    au "Oh my goodness... I can't even imagine. He must have needed some serious medical attention after the fight."

    scene v12ferau1e # FPP. same as 1d, mouth closed
    with dissolve

    u "Oh yeah. They actually had to carry him out of the place. I'm one tough son of a bitch."

    scene v12ferau1
    with dissolve

    au "I think I'd like to see exactly how tough you actually are. I... I think I see some bruising. Oh my gosh, and your eye is cut! I'm gonna need to patch that up immediately."

    menu:
        "It does hurt pretty bad":
            $ v12s7_aubrey_moved = True
            $ reputation.add_point(RepComponent.BOYFRIEND)
            scene v12ferau1
            with dissolve

            au "Oh, sweetie. If I didn't take a look at this I wouldn't be able to call myself a nurse. Please come by my office so I can get you fixed up."

            if aubrey.relationship >= Relationship.FWB:
                au "I'll need some privacy to give the best treatment possible."

                scene v12ferau2 # TPP. Show Aubrey wispering in mc's ear
                with dissolve

                au "*Whisper* Meet me in the bathroom."

            else:
                scene v12ferau2
                with dissolve

                au "I'd prefer a little bit of privacy away from hawkeye Mr. Lee, so come hang with me in the bathroom."

                scene v12ferau1a
                with dissolve

                u "Whatever you say Miss Nurse. *Chuckles*"

                scene v12ferau1
                with dissolve

                au "Good, and try not to take too long. Those injuries look very, very bad. *Chuckles*"
            
            stop music fadeout 3
            play music "music/v12/Track Scene 7_2.mp3" fadein 2

            call screen v12s7_balcony_right
            
        "Didn't even feel it":
            $ reputation.add_point(RepComponent.BRO)
            scene v12ferau1a
            with dissolve

            u "Haha, really? I didn't even feel it. After my fight I left the arena and hopped right on the ship. Haven't even had a moment to take a look."

            scene v12ferau1
            with dissolve

            au "My oh my... You really are one tough cookie I suppose. Maybe you could protect me from whoever this murderer may be?"

            scene v12ferau1a
            with dissolve

            u "I'd love to stick around but I've got more investigating to do... Although, no need to worry. I'll be back to check on you... *Chuckles*"

            scene v12ferau1
            with dissolve

            au "Looking forward to it, Mr. Boxer."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_balcony_right

label v12s7_aubrey2:
    $ freeroam9.add("aubrey2")
    $ v12s7_seenList = []

    show screen murder_button_overlay(aubrey)
    
    scene v12ferauh1 # FPP. Location is in the bathroom on the ship, Show aubrey, seductive look, mouth open
    #with dissolve

    au "Finally! Took you long enough..."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_3.mp3" fadein 2

    scene v12ferauh1a # FPP. same 1, mouth closed
    with dissolve

    u "What can I say, a lot of people are interested in champ's attention."

    scene v12ferauh1
    with dissolve

    au "You don't have to be in character here. *Laughs*"

    scene v12ferauh1a
    with dissolve

    u "You sure? I'm not in the mood for a swim."

    scene v12ferauh1
    with dissolve

    au "*Laughs* I'd save you, don't worry."

    scene v12ferauh1a
    with dissolve

    u "Is that so?"

    scene v12ferauh1
    with dissolve

    au "That's so. Now, how about we make this murder mystery a little more... exhilarating."

    scene v12ferauh1a
    with dissolve

    u "Exhilarating? What do you have in mind, doc? *Chuckles*"

    scene v12ferauh2 # TPP. Show aubrey grabbing mc's crotch, mouth closed
    with dissolve

    menu:
        "Let her":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            scene v12ferauh2a # TPP. same 2, mc mouth open
            with dissolve
            
            $ grant_achievement("doctors_orders")
            u "Oh... Yeah, this is definitely more interesting than a murder."

            scene v12ferauh3 # TPP. Show aubrey kissing mc, placing his hand on her ass.
            with dissolve

            pause

            scene v12ferauh4 # FPP. Show aubrey looking at camera, close up, seductive look, mouth open
            with dissolve
            au "Let's make this a little more enjoyable, shall we [name]?"

            scene v12ferauh4a #FPP. Same 4, mouth closed
            with dissolve

            u "Absolu-"
            play sound "sounds/dooropen.mp3"

            unknown "Could've sworn I heard people talking in here... Guess not."

            play sound "sounds/doorclose.mp3"

            scene v12ferauh4
            with dissolve

            au "Look at us getting into trouble together. *Chuckles*"

            scene v12ferauh4a
            with dissolve

            u "I'm just following the doctor's orders."

            scene v12ferauh1
            with dissolve

            au "Haha, we better get out of here if we want to avoid getting into trouble. You go ahead and leave first, I'll be out in a few."

            scene v12ferauh1a
            with dissolve

            u "Yes ma'am."

            scene v12ferauh5 # TPP. Show MC walking out the bathroom door
            with dissolve

            pause 0.75

            stop music fadeout 3
            play music "music/v12/Track Scene 7_2.mp3" fadein 2

            call screen v12s7_bathroom

        "Kill her":
            $ v12s7_killList.add(aubrey)
            label v12s7_aubrey_kill:
            hide screen murder_button_overlay

            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            scene v12ferauh6 # TPP. Show MC pointing finger gun at aubrey, mc mouth open, aubrey mouth closed
            with dissolve

            u "Boom."

            stop music fadeout 3
            play music "music/v12/Track Scene 7_4.mp3" fadein 2

            scene v12ferauh6a # TPP. Show MC pointing finger gun at aubrey, mc mouth closed, aubrey mouth open
            with dissolve

            au "What? Ah, ohhhhhh. *Laughs* You're the murderer. So you get a pretty, innocent girl like me alone in the bathroom and decide to kill her, huh?"

            scene v12ferauh1a
            with dissolve

            u "The perfect crime."

            scene v12ferauh1
            with dissolve

            au "*Laughs*"

            scene v12ferauh1a
            with dissolve

            if len(v12s7_killList) == v12s7_victims:
                u "We'll catch up later. I've got things to see still."
            else:
                u "We'll catch up later. I've got things to see and people to kill."

            scene v12ferauh1
            with dissolve

            au "What's wrong, [name]? You don't wanna kiss the pretty zombie girl?"

            scene v12ferauh1a
            with dissolve

            u "*Chuckles* I'm good, thanks."

            scene v12ferauh5
            with dissolve

            pause 0.75

            stop music fadeout 3
            play music "music/v12/Track Scene 7_2.mp3" fadein 2

            call screen v12s7_bathroom

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

label v12s7_riley1:
    $ freeroam9.add("riley")

    if "josh" in freeroam9 or not josh_europe:
        $ v12s7_seenList = [chloe]
    else:
        $ v12s7_seenList = [chloe, josh]

    show screen murder_button_overlay(riley)

    scene v12ferri1 # FPP. location is the upper rear outside seating area on the right side of the ship as seen on miro. Show chloe(from a distance as mc is overhearing the convo), looking at riley out of shot, slight annoyed look, mouth open
    #with dissolve

    cl "Rich people are the actual problem. You guys get to sit around on stacks of money and the little guys like me have to pick up the slack for this entire country."
    cl "People like you never wanna pay your taxes but I barely have two pennies to rub together and I still have to pay mine."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_5.mp3" fadein 2

    scene v12ferri2 # FPP. Show riley(from a distance as mc is overhearing the convo), smug look, looking at chloe out of shot, mouth open.
    with dissolve

    ri "*Southern accent* You don't get rich by spending money, you get rich by saving it. If I'm smart enough to avoid paying taxes then that must mean I'm an extremely smart business woman."

    scene v12ferri1
    with dissolve

    cl "So you let your greed cause a burden on us lower classes and just don't care?"

    scene v12ferri2
    with dissolve

    ri "*Southern accent* Look, I know what it's like to be poor. I used to wear your shoes, but you have no idea what it means to be rich."
    ri "So do not judge a life you've never lived. The aid I provide for charity couldn't possibly be matched by the number on your taxes or even what you consider to be a fair share."

    scene v12ferri1
    with dissolve

    cl "Hmph, I can't stand rich people."

    scene v12ferri2
    with dissolve

    ri "And I can't stand the fact that I paid good money for this ride and yet I'm accompanied by the likes of your sort of people."

    scene v12ferri1
    with dissolve

    cl "You lack a heart, lady. And what happened to your accent? *Chuckles*"

    scene v12ferri2
    with dissolve

    ri "*Southern accent* I don't know what you're talking about. *Chuckles*"

    scene v12ferri3 # FPP. Show chloe and riley, now looking at the camera, mouths closed, neutral look
    with dissolve

    u "You ladies have room over here for a world renowned boxer such as myself?"

    scene v12ferri4 # FPP. Show riley, shocked look, mouth open
    with dissolve

    ri "*Southern accent* Tell me eyes deceive me! You're the fighter that took down George Knight The Giant."

    scene v12ferri4a # FPP. Same 4, mouth closed
    with dissolve

    u "That would be me."

    scene v12ferri4
    with dissolve

    ri "*Southern accent* And now my confusion is all too much. It makes sense why the wealthy and a man such as yourself would be here..."
    ri "But I can't understand why Miss Blue Collar here would be allowed to join us."

    if CharacterService.is_girlfriend(chloe, Relationship.GIRLFRIEND):
        # -Chloe kisses MC-
        scene v12ferri5 # FPP. Show chloe, looking at camera, neutral look mouth open
        with dissolve
        cl "I'm actually quite sure he enjoys my company more than yours."

        scene v12ferri4
        with dissolve

        ri "*Shocked* Oh... I see."

    else:
        scene v12ferri5
        with dissolve

        cl "The boxer comes from a humble beginning as well and I'm sure he's not as demeaning as you are towards people during these hard times."

        scene v12ferri5a # FPP. same 5, mouth closed
        with dissolve

        u "Of course, we can all get along no matter who we are or where we've come from."

        scene v12ferri4
        with dissolve

        ri "*Southern accent* I suppose."

    scene v12ferri5b # FPP. same 5, Chloe presses her finger to her lip
    with dissolve

    cl "..."

    u "What?"

    scene v12ferri5
    with dissolve

    cl "I'm running out of things to talk about. *Chuckles*"

    scene v12ferri4
    with dissolve

    ri "*Southern accent* That's to be expected. Those of the lower classes aren't familiar with as many social topics as the wealthy. Isn't that right, Mr. Boxer?"

    menu:
        "I'm poor":
            scene v12ferri4a
            with dissolve

            $ grant_achievement("zero_to_hero")
            u "I'm actually quite poor myself. My manager takes nearly all of my winnings and after expenses, I'm usually left with hardly anything."

            scene v12ferri4
            with dissolve

            ri "*Southern accent* Well, your name alone puts you at a higher caliber."

            scene v12ferri4a
            with dissolve

            u "I actually take pride in being without excess. I have exactly what I need and nothing more. So if there's any outsider here, it'd be you."

            scene v12ferri4
            with dissolve

            ri "*Southern accent* Absurd."

        "I'm rich":
            scene v12ferri4a
            with dissolve
            u "The ways of the rich are quite different from the ways of the poor. You've got guys practicing how to throw balls around with a dream of becoming some sports star as we converse our way to changing the world."

            scene v12ferri5
            with dissolve

            cl "But... You yourself are a sports entertainer."

            scene v12ferri5a
            with dissolve

            u "I've long surpassed dreaming, but I was where you and your people are. So I know what it's like to be there."

            scene v12ferri4
            with dissolve

            ri "*Southern accent* As do I."

    scene v12ferri5
    with dissolve

    cl "Okay guys, serious talk. Have either of you actually seen Mr. Lee? I haven't but, after his little introduction earlier I'm getting kinda freaked out. It feels like I'm being watched."

    scene v12ferri5a
    with dissolve

    u "Feeling a little paranoid, huh? I'm pretty sure that was his goal. *Chuckles*"

    scene v12ferri4
    with dissolve

    ri "I wouldn't jump to conclusions, but I'm pretty sure he's got cameras set up or something."

    scene v12ferri4a
    with dissolve

    u "You don't think that's a little much?"

    scene v12ferri5
    with dissolve

    cl "He's always been serious about his history stuff, or whatever this is supposed to be. *Laughs*."

    scene v12ferri5a
    with dissolve

    u "Yeah, that's something I learned the hard way thanks to Imre and Ryan."

    scene v12ferri5
    with dissolve

    cl "Wait, what happened?"

    scene v12ferri5a
    with dissolve

    u "Long story short, when we were in London and they had that argument at the hotel, Mr. Lee tried to get them to work it out."

    u "You can probably guess that they didn't listen to him, and He. Was. Pissed. The walk back to the hotel from being in the middle of nowhere was probably well deserved."

    scene v12ferri5
    with dissolve
    cl "*Laughs* Yeah, that's the Mr. Lee I know."

    scene v12ferri4
    with dissolve

    ri "If we don't get back into character we're most likely gonna end up getting some of that same wrath. *Chuckles*"

    scene v12ferri4a
    with dissolve

    u "Have you two found any hints on who may be the murderer?"

    scene v12ferri5
    with dissolve

    cl "We've honestly just been messing around with our character., I actually started enjoying it with Riley here acting all serious and feisty. *Chuckles*"

    scene v12ferri4b # FPP. same 4, different pose, mouth open
    with dissolve

    ri "What if I wasn't acting? *Chuckles* Uh, oh!"

    menu:
        "Leave":
            scene v12ferri4a
            with dissolve

            u "Alright, ladies. You two enjoy your little rich versus poor debate I've gotta go hit a punching bag or something. *Chuckles*"

            call screen v12s7_left_viewpoint

        "Make Riley leave":
            $ v12s7_riley_moved = True
            scene v12ferri4a
            with dissolve

            u "Since you're so into this Miss Rich, maybe you should be helping find the killer."

            scene v12ferri4
            with dissolve

            ri "*Southern accent* And once again, the rich bear the responsibility. *Laughs* I'll catch you guys later."

            scene v12ferri5
            with dissolve

            cl "She's really good at that accent, haha."

            scene v12ferri5a
            with dissolve

            u "A little too good. *Chuckles*"

            scene v12ferri5
            with dissolve

            cl "I'm gonna stand over here by myself for a while so I don't have to be in character. *Chuckles*"

            scene v12ferri5a
            with dissolve

            u "Haha, alright. I'll catch up with you later."

            if chloe.relationship >= Relationship.FWB:
                scene v12ferri6 # TPP. Show MC kissing chloe
                with dissolve
                play sound "sounds/kiss.mp3"
                
                pause 0.75
    
    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_left_viewpoint

label v12s7_chloe1:
    $ freeroam9.add("chloe")

    $ v12s7_seenList = []

    if josh_europe and not "josh" in freeroam9:
        $ v12s7_seenList.append(josh)

    show screen murder_button_overlay(chloe)

    scene v12ferch1 # FPP Show chloe slight smile, mouth closed
    #with dissolve

    u "Well, well. If it isn't the richest woman alive."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_6.mp3" fadein 2

    scene v12ferch1a # FPP. same 1, mouth open
    with dissolve

    cl "*Chuckles* I'm the poor one, remember?"

    scene v12ferch1
    with dissolve

    u "Not at all. We're all rich in our own ways and look at you, you're obviously rich in beauty."

    scene v12ferch1a
    with dissolve

    cl "If you're just trying to butter me up so you can sneak a kill, keep going. *Chuckles* I'm enjoying the compliments... It's hard being poor."

    scene v12ferch1
    with dissolve

    u "Being poor is nothing more than a setting stone to being rich, because no one chooses to be poor. That's why I donate half of all my fight proceeds to those in need."

    scene v12ferch1a
    with dissolve

    cl "Oh, so you're a generous type of man."

    scene v12ferch1
    with dissolve

    u "How could I not be? After looking into your eyes it feels like I witnessed a Greek tragedy."

    scene v12ferch1a
    with dissolve

    cl "Haha, okay. Mr. Lee is definitely getting to you."

    scene v12ferch1
    with dissolve

    u "I only thought of that because of the viking thing he made us do in class. *Chuckles*"

    scene v12ferch1a
    with dissolve

    cl "What do Vikings and the Greeks have to do with each other? *Chuckles*"

    scene v12ferch1
    with dissolve

    u "Haha, I have no idea. So, is our poor girl ready for more of Europe or is she starting to get homesick?"

    scene v12ferch1a
    with dissolve

    cl "Hmm... A little bit of both I guess?"
    cl "I'm excited to see Paris because that's something I've always wanted to do, but I have to admit I do feel out of place sometimes considering we're in a completely different country."

    scene v12ferch1
    with dissolve

    u "Well, as a fighter I've traveled the world but could never replace home. That's for sure."

    scene v12ferch1a
    with dissolve

    cl "Ha, yeah... *Sighs*"

    scene v12ferch1
    with dissolve

    u "What's going on in that blonde head of yours? *Chuckles*"

    scene v12ferch1b # FPP. same 1a, new pose, mouth open
    with dissolve

    cl "*Chuckles* It's just... I know that once we get back, this whole Chicks thing is gonna explode and I just really hope I'm gonna be able to handle it all. Even if I can, it's still gonna be super stressful."

    menu:
        "Plan for it":
            scene v12ferch1c # FPP same 1, new pose, mouth closed
            with dissolve
            
            u "Maybe you can get a plan together so that when you get back you're at least mentally prepared."

            scene v12ferch1b
            with dissolve

            cl "I thought about that, but I also want to enjoy this trip. This just might be the last thing I get to enjoy before all the Chicks stuff blows up right in my face."

            scene v12ferch1c
            with dissolve

            u "Yeah, I get that. It wouldn't be too fun having to plan for the Chicks apocalypse while in Europe. *Chuckles*"

            scene v12ferch1b
            with dissolve

            cl "Exactly. So, I don't know. I'm doing my best to not think about it..."

        "Enjoy Europe":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            scene v12ferch1c
            with dissolve
            
            u "Let's just enjoy Europe for right now, yeah? Let all that shit come when it comes. There's no reason to be stressed while we're in Europe."

            scene v12ferch1b
            with dissolve

            cl "You always know what to say, huh?"

            scene v12ferch1c
            with dissolve

            u "Maybe I just know what you need to hear. *Chuckles*"

    scene v12ferch1b
    with dissolve
    cl "Okay so... I know this is off topic, but I just thought of something. What if Mr. Lee bugged the props and that's how he's \"always watching\"."

    scene v12ferch2 # FPP. Show Mc's gloves, looking down at them held out infront of him
    with dissolve

    u "That's actually not a bad theory, but... I don't see anything on mine."

    scene v12ferch1b
    with dissolve

    cl "Just in case you're listening Mr. Lee, my \"poor girl\" character has been having problems with her sorority back at home and just needed to vent..."

    scene v12ferch1c
    with dissolve

    u "Wow... *Chuckles* You're actually scared of Mr. Lee."

    scene v12ferch1b
    with dissolve

    cl "*Whisper* He was really harsh on me when I had him as a teacher. It was sort of my fault, but still."
    cl "That man is relentless when you don't do what he asks. I don't know if he's bipolar or if he just really doesn't like being disobeyed."

    scene v12ferch1c
    with dissolve

    u "Haha, probably a bit of both..."

    scene v12ferch1b
    with dissolve

    cl "*Laughs* So... You've come to talk to me twice now. How do you know I'm not the killer?"

    scene v12ferch1c
    with dissolve

    u "I don't know, just do."

    scene v12ferch1b
    with dissolve

    cl "The only way you could really know is if you were the killer."

    scene v12ferch1c
    with dissolve

    u "Or... I know who is the killer and don't plan on snitching because one, I'm not a snitch and two, I'm not in the mood get thrown overboard for calling the person out without witnessing a murder. Boom."

    scene v12ferch1d # FPP. Same 1, different pose again, mouth open
    with dissolve

    cl "*Chuckles* That was pretty convincing, did you write that down?"

    scene v12ferch1e # FPP. same 1d, mouth closed.
    with dissolve

    u "No, but maybe I should. *Chuckles* Really though, I'm not the killer."

    scene v12ferch1d
    with dissolve

    cl "Mhmm, sure... Good defense. *Laughs*"

    scene v12ferch1e
    with dissolve

    u "Hey, just because you haven't gotten around and talked to other people doesn't mean you can just assume it's me. *Laughs*"

    scene v12ferch1d
    with dissolve

    cl "Seeing is believing and I've only seen you and Riley. And I think we both know she isn't the killer."

    scene v12ferch1e
    with dissolve

    u "Do we, though? She could be dragging this whole thing out just so she can keep playing the game, haha."

    scene v12ferch1d
    with dissolve

    cl "That's actually a good point... Okay, now I'm not so sure about you being the killer. *Chuckles*"

    if chloe.relationship >= Relationship.FWB:
        scene v12ferch3 # TPP. Show chloe, hand on mc's chest, chloe mouth open
        with dissolve

        cl "If I... do something for you, will you tell me? A little, quid pro quo?"

        scene v12ferch1e
        with dissolve

        u "Hmm, so your worries about Mr. Lee have just suddenly gone away? That's a little sus."

        scene v12ferch1d
        with dissolve

        cl "Hey, I'm just playing the game Mr. Boxer..."

        scene v12ferch4 # TPP. Show chloe kissing MC
        with dissolve
        play sound "sounds/kiss.mp3"

        pause 1.5

        scene v12ferch1a
        with dissolve

        cl "So, are you the killer? Seriously, [name]."

        scene v12ferch1
        with dissolve

        u "There's only one way to find out who the killer is, my love."

        scene v12ferch5 # TPP. Show MC wispering in chloe's ear
        with dissolve

        u "You just have to catch them in the act..."

        scene v12ferch6 # TPP. Show Mc walking away.
        with dissolve

        pause 0.75

        stop music fadeout 3
        play music "music/v12/Track Scene 7_2.mp3" fadein 2

        call screen v12s7_left_viewpoint

    else:
        scene v12ferch1e
        with dissolve

        u "There's only one way to find out who the killer is... You just have to catch them in the act."

        scene v12ferch6 # TPP. Show Mc walking away.
        with dissolve

        pause 0.75

        stop music fadeout 3
        play music "music/v12/Track Scene 7_2.mp3" fadein 2

        call screen v12s7_left_viewpoint

label v12s7_chloe_kill:
    hide screen murder_button_overlay

    scene v12ferch7 # TPP. show mc, pointing finger guns at chloe, mouth open
    with dissolve

    u "Boom."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_7.mp3" fadein 2

    scene v12ferch1d
    with dissolve

    cl "*Smiling* You sneaky little snake. You were the murderer the entire fucking time and I knew it."

    scene v12ferch1e
    with dissolve

    u "Haha, how'd you know?"

    scene v12ferch1d
    with dissolve

    cl "Because Mr. Lee has played a murder mystery before and he always chooses the same type of student to be the murderer."

    scene v12ferch1e
    with dissolve

    u "Wait, really? *Laughs* And what type of student is that?"

    scene v12ferch1d
    with dissolve

    cl "The student that knows everyone, has plenty of friends, plenty of foes, and all around just a well-balanced student."

    scene v12ferch1e
    with dissolve

    u "Well, thank you, I think... Is being labeled well-balanced a good thing?"

    scene v12ferch1d
    with dissolve

    cl "It is to me. *Laughs* I can't believe you just killed me though!"

    scene v12ferch1e
    with dissolve

    u "Think about it this way: The faster I kill, the faster this is over."

    scene v12ferch1d
    with dissolve

    cl "Yeah, yeah, whatever. Go finish your massacre Mr. Boxer."

    scene v12ferch1
    with dissolve

    u "*Chuckles*"

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_left_viewpoint

label v12s7_riley3:
    $ freeroam9.add("riley3")

    if riley in v12s7_endtalkList:
        $ v12s7_endtalkList.remove(riley)

    $ v12s7_seenList = [chloe]
    if josh_europe and not "josh" in freeroam9:
        $ v12s7_seenList.append(josh)

    show screen murder_button_overlay(riley)

    scene v12ferric1 # FPP. Show riley and chloe stood together, mouths closed
    #with dissolve

    u "Seeing you guys together again in the same exact location is a little suspicious."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_5.mp3" fadein 2

    scene v12ferric2 # FPP. Show riley, slight smile, mouth open
    with dissolve

    ri "*Chuckles* *Southern accent* Sure do keep checking in on us, partner! I've seen the way you knock men out in the ring..."
    ri "I always wondered if your opponents were able to walk out of there alive and now I'm starting to wonder if we will. Are you a killer, Mr. Boxer?"

    scene v12ferric3 # FPP. Show Chloe, mouth open
    with dissolve

    cl "I was already suspicious of him, but now I have no doubts."

    scene v12ferric3a # FPP. Same 3, mouth closed
    with dissolve

    u "What have I done that makes me look like the killer?"

    scene v12ferric3
    with dissolve

    cl "Oh, I don't know. Suggesting that people go roam around, causing us to separate?"

    scene v12ferric3a
    with dissolve

    u "Okay, I can see how that could be suspicious. But as always, innocent until proven guilty."
    u "And both of you are throwing a lot of heat on me, so how do I know this isn't one of your guys' plans to just throw the attention off of yourselves?"

    scene v12ferric1a # FPP. Show riley looking closer at chloe, mouth open
    with dissolve

    ri "*Southern accent* Hmm, our little blue collar girl here could be the killer. You a killer, girl?"

    scene v12ferric3
    with dissolve

    cl "Umm, no."

    scene v12ferric2a # FPP. Same 2, looking at chloe, mouth popen
    with dissolve

    ri "*Southern accent* Why the \"umm\", then honey?"

    scene v12ferric3b # FPP. Same 3, looking at riley, mouth open
    with dissolve

    cl "I'm just a little shocked that you'd think it's me since I've literally been right here, in the same spot, this whole time. *Chuckles*"

    scene v12ferric3c # FPP. Same 3, mouth closed, looking at camera
    with dissolve

    u "There are other people playing this game and there's a lot going on outside of what us three are doing. Why are you guys being so narrow-minded?"

    scene v12ferric2a
    with dissolve

    ri "*Southern accent* Hmm, I guess you're right. Who else though?"
    ri "Imre and Ryan are chasing each other around. So it'd be really strange if one of them was the killer and plus, I don't think Mr. Lee would've chosen them."

    scene v12ferric2b # FPP. same 2, looking at camera, mouth closed
    with dissolve

    u "Who would you least expect?"

    scene v12ferric3
    with dissolve

    cl "Lindsey."

    scene v12ferric3a
    with dissolve

    u "Then let's start with her."

    scene v12ferric3
    with dissolve

    cl "Okay, but... That doesn't mean we've cleared you as not-guilty. This just means we're exploring other options. Don't put all your eggs in one basket and all that, right?"

    scene v12ferric2
    with dissolve

    ri "*Southern accent* That's a rule the poor and the rich can both live by."

    scene v12ferric2b
    with dissolve

    u "Is there a sign on me that says \"killer\" or something? *Chuckles* I haven't done anything."

    scene v12ferric3
    with dissolve

    cl "There might as well be considering how sketchy you've been. *Chuckles*"

    scene v12ferric3a
    with dissolve

    u "Hmm... Then I guess I'll just have to change up my tactics."

    scene v12ferric2
    with dissolve

    ri "*Southern accent* \"Tactics\"? That sounds like a murder plotting term to me..."

    scene v12ferric2b
    with dissolve

    u "No, I just meant... You know what, nevermind. *Chuckles* I'll let you two run your brains dry."

    scene v12ferric3
    with dissolve

    cl "Ha, good luck not dying... or should I say killing people? *Laughs*"

    scene v12ferric4 # TPP. Show mc walking away
    with dissolve

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    $ v12s7_endtalkList.append(riley)

    call screen v12s7_left_viewpoint
    
label v12s7_riley3a:
    $ freeroam9.add("riley3")

    $ v12s7_seenList = []
    if josh_europe and not "josh" in freeroam9:
        $ v12s7_seenList.append(josh)

    show screen murder_button_overlay(riley)

    scene v12ferril1 # FPP. Show riley, slight smile mouth closed.
    #with dissolve

    u "Still alive out here, huh?"

    stop music fadeout 3
    play music "music/v12/Track Scene 7_5.mp3" fadein 2

    scene v12ferril1a # FPP. Same 1, mouth open
    with dissolve

    ri "*Southern accent* I am, but I'm not sure if our poor girl is. I know she planned on staying in the same spot, but now she's gone."
    ri "I was enjoying our conversations so much... I was starting to grow a little attached to her."

    scene v12ferril1
    with dissolve

    u "If that's the case then she probably got killed."

    scene v12ferril1a
    with dissolve

    ri "*Southern accent* But by who? If she really was killed it had to be someone that's moving around. Based on what I heard Imre say earlier I have to assume it's him for now."

    scene v12ferril1
    with dissolve

    u "What'd Imre say?"

    scene v12ferril1a
    with dissolve

    ri "*Southern accent* Imre said he's just gonna hurry up and make sure everyone gets killed."

    scene v12ferril1
    with dissolve

    u "(How is he gonna do that? *Laugh*)"

    u "That does indeed sound suspicious, maybe I should check in on them and see what I can find out."

    scene v12ferril1a
    with dissolve

    ri "*Southern accent* Well, wait a minute. You were here with Chloe when I left, what'd she say while I was gone?"

    menu:
        "Me":
            $ reputation.add_point(RepComponent.BRO)
            scene v12ferril1
            with dissolve

            u "Honestly, she thought it was me, but I can't blame her since you and I were the only people she talked to. She has to accuse somebody. *Chuckles*"

            scene v12ferril1a
            with dissolve

            ri "*Southern accent* Someone else must come by when neither of us were with her."

        "You":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            scene v12ferril1
            with dissolve

            u "She thought you were the killer and assumed you were playing so hardcore to throw people off."

            scene v12ferril1a
            with dissolve

            ri "*Whisper* Hey, I am not playing hardcore. I just don't wanna get in trouble and I'll have you know I actually enjoy stuff like this."
            ri "You gotta admit, Mr. Lee creates very interactive situations for us students. I appreciate that."

            scene v12ferril1
            with dissolve

            u "Haha, suck up."

    scene v12ferril1b # Fpp. Same 1, different pose, mouth open
    with dissolve

    ri "*Whisper* You need to go check in with Imre and Ryan, you're friends with them. If Imre really is the killer you'll be able to call him out."

    scene v12ferril1c # Fpp. Same 1, different pose, mouth closed
    with dissolve

    u "True, I'm on it."

    scene v12ferril2 # FPP. Show MC walking away.
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_left_viewpoint

label v12s7_riley_kill:
    hide screen murder_button_overlay

    scene v12ferril3 # TPP. Show mc pointing finger gun at riley, mouth open
    with dissolve

    u "Boom."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_7.mp3" fadein 2

    scene v12ferril4 # FPP. Show riley, slight smile, mouth open
    with dissolve

    ri "*Whisper* You little liar."

    scene v12ferril4a # FPP. same 4, mouth closed
    with dissolve

    u "Haha, Mr. Lee chose a good murderer."

    scene v12ferril4
    with dissolve

    ri "How'd I not know? So many people thought it was Imre. As like revenge for Mr. Lee or something. *Chuckles*"

    scene v12ferril4a
    with dissolve

    u "Nope, it was the beautiful famous boxer. *Laughs*"

    scene v12ferril4
    with dissolve

    ri "Wow, well I guess since you killed me I can root for you now. So good luck."

    scene v12ferril4a
    with dissolve

    u "Haha, thanks."

    scene v12ferril2 # FPP. Show MC walking away.
    with dissolve

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_left_viewpoint

label v12s7_lauren1:
    $ freeroam9.add("lauren")

    $ v12s7_seenList = []
    if emily_europe and not "emily" in freeroam9:
        $ v12s7_seenList.append(emily)

    show screen murder_button_overlay(lauren)

    scene v12ferla1 # FPP. Show lauren, mouth closed
    #with dissolve

    u "There you are."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_8.mp3" fadein 2

    if v11_lauren_caught_aubrey:
        scene v12ferla1a # FPP. same 1, mouth open
        with dissolve

        la "Don't try an use the game as a way of talking to me."

        menu:
            "Apologize":
                $ reputation.add_point(RepComponent.BOYFRIEND)
                scene v12ferla1
                with dissolve
                
                u "Sorry, uhm bye."

                u "(Damn, she's still really pissed.)"

            "Kill her":
                $ reputation.add_point(RepComponent.TROUBLEMAKER)
                $ v12s7_killList.add(lauren)
                scene v12ferla1
                with dissolve

                u "Yeah uhm, I know you're mad right now but I gotta play the game so..."

                stop music fadeout 3
                play music "music/v12/Track Scene 7_7.mp3" fadein 2

                scene v12ferla2 # TPP. Show mc pointing finger gun at lauren, mouth open
                with dissolve

                u "Boom."

                scene v12ferla1a
                with dissolve

                la "Not surprising you got chosen as the murderer, Mr. Lee must know a bad guy when he sees one."

                scene v12ferla3 # FPP. Show lauren walking away
                with dissolve

                u "(Damn, she's still really pissed.)"
        
        stop music fadeout 3
        play music "music/v12/Track Scene 7_2.mp3" fadein 2

        call screen v12s7_seating_back

    scene v12ferla1a
    with dissolve

    la "And there you are."

    if CharacterService.is_girlfriend(lauren, Relationship.GIRLFRIEND):
        scene v12ferla5 # TPP. Show lauren kissing mc.
        with dissolve
        play sound "sounds/kiss.mp3"

        pause 1.5

    scene v12ferla1
    with dissolve

    u "You haven't been killed yet, guess that's good."

    scene v12ferla1a
    with dissolve

    la "It actually isn't, everyone thinks I'm the killer."

    scene v12ferla1
    with dissolve

    u "Why?"

    scene v12ferla1a
    with dissolve

    la "Because that's my character, he's a killer on the run."

    scene v12ferla1
    with dissolve

    u "*Laughs* Wait, you're character is a killer on the run but you're saying you're not the killer? I don't know if I can believe that."

    scene v12ferla1b # FPP. same 1, Show lauren annoyed, mouth open
    with dissolve

    la "See! You and everyone else, I don't know why Mr. Lee would do that. No one will come near me 'cause they don't wanna be killed. Except for Imre, he actually begged me to kill him haha."

    scene v12ferla1
    with dissolve

    u "I don't know... What if you're just smart enough to come up with that story?"

    scene v12ferla1a
    with dissolve

    la "I'm not."

    scene v12ferla1
    with dissolve

    u "You're not smart? *Chuckles*"

    scene v12ferla1b
    with dissolve

    la "No, stop, I mean I'm not making it up."

    scene v12ferla1
    with dissolve

    u "Hmmm, very suspicious."

    scene v12ferla1a
    with dissolve

    la "If you really think I'm the killer then why are you around me, huh? The only people that would come around me either want to be killed or are the killer because they can kill me easily."

    scene v12ferla1c # FPP. same 1, Show lauren, new pose, mouth closed
    with dissolve

    u "Okay, good point. Are you asking me to leave then?"

    scene v12ferla1d # FPP. same 1, Show lauren, new pose, mouth open
    with dissolve

    la "No, I'm not just saying that, oh nevermind. Even if you were the killer I wouldn't care, but at least spend some time with me before you kill me."

    scene v12ferla1c
    with dissolve

    u "Aww, are you really that lonely? *Chuckles*"

    scene v12ferla1d
    with dissolve

    la "It sounds sad when you put it that way, I just don't like it when everyone's avoiding me."

    scene v12ferla1c
    with dissolve

    u "It seems as though Mr. Lee had multiple motives for the roles he gave us."

    scene v12ferla1d
    with dissolve

    la "That would explain why he was so serious about us not breaking character."

    scene v12ferla1c
    with dissolve

    u "And him watching over us all rather than playing a role himself."

    scene v12ferla1d
    with dissolve

    la "Why a boxer for you then? It's not like he's concerned about the frat stuff."

    scene v12ferla1c
    with dissolve

    u "I don't think it has anything to do with that, I'm actually not sure about my own role. But everyone else seems to have a personal conflict or serious joy in their role."

    scene v12ferla1d
    with dissolve

    la "Yeah, Amber got security or whatever and she's taking advantage of it. She took my gum earlier after she searched me saying it was contraband. *Laughs*"
    la "She could've just asked for some gum, but Mr. Lee was nearby and I guess that's how she chose to stay in character."

    scene v12ferla1c
    with dissolve

    u "Haha, sounds like her."

    scene v12ferla1d
    with dissolve

    la "*Sighs* I can't wait to get to Paris."

    scene v12ferla1c
    with dissolve

    u "How come?"

    scene v12ferla1d
    with dissolve

    la "There's just a lot I want to do, I made some promises to myself and I'm going to keep them."

    scene v12ferla1c
    with dissolve

    u "You're pretty philosophical for a killer on the run. *Chuckles*"

    scene v12ferla4 # FPP. Show lauren punching towards camera as if punching mc in the arm playfully, smiling, mouth open
    with dissolve

    la "You know what, go bother someone else. *Chuckles* Maybe someone will kill you for me. *Laughs*"

    if CharacterService.is_girlfriend(lauren, Relationship.GIRLFRIEND):
        scene v12ferla1d
        with dissolve

        la "At least kiss me first before you die."

        scene v12ferla6 # TPP. Show Lauren and mc kissing
        with dissolve
        play sound "sounds/kiss.mp3"
        pause 1.5

    scene v12ferla1
    with dissolve

    u "Off to die, bye."

    scene v12ferla1a
    with dissolve

    la "*Chuckles* Bye."

    scene v12ferla7 # TPP. Show MC walking away
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_seating_back

label v12s7_lauren_kill:
    hide screen murder_button_overlay

    scene v12ferla8 # TPP. Show mc pointing finger gun at lauren, mouth open
    with dissolve

    u "Boom."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_7.mp3" fadein 2

    scene v12ferla1d
    with dissolve

    la "Wow, you just gonna take me out like that. My living as a suspected criminal wasn't bad enough?"

    scene v12ferla1c
    with dissolve

    u "I thought I'd end your misery for you."

    scene v12ferla1d
    with dissolve

    la "Oh wow, so sweet."

    scene v12ferla1c
    with dissolve

    u "Us criminals have to support each other."

    scene v12ferla1d
    with dissolve

    la "Oh my gosh."

    scene v12ferla7
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_seating_back

label v12s7_ryan_imre1:
    $ freeroam9.add("imre")
    
    $ v12s7_seenList = [ryan, imre, amber]
    if v12s7_riley_moved and not "riley2" in freeroam9:
        $ v12s7_seenList.remove(amber)

    show screen murder_button_overlay(imre)

    scene v12ferryi1 # FPP. Show ryan from a distance looking at imre off screen, mouth open
    #with dissolve

    ry "Wow, look at this beautiful day, if only my wife was just as beautiful."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_5.mp3" fadein 2

    scene v12ferryi2 # FPP. Show imre from a distance looking at ryan off screen mouth open
    with dissolve

    imre "You call me your wife again and we're gonna have a problem."

    scene v12ferryi3 # FPP. Show Mr Lee from a distance at imre while Mr Lee is holding a boyancy ring, mouth open
    with dissolve

    lee "Did you say something Mrs.?"

    scene v12ferryi2a # FPP. Same 2, now looking at mr lee off screen, mouth open
    with dissolve

    imre "Just having a little spat with my husband. He likes to make the meanest little jokes."

    scene v12ferryi3
    with dissolve

    lee "Mhm, as long as you're enjoying yourselves."

    scene v12ferryi1
    with dissolve

    ry "Of course we are, my lovely wife here just doesn't get my humor from time to time. He, I mean she, has the brain of a chicken sometimes."

    scene v12ferryi4 # FPP. Show imre punching ryan in the shoulder, mouth open
    with dissolve

    imre "Ha ha ha, that's so funny. Look at me laughing."

    scene v12ferryi3
    with dissolve

    lee "*Chuckles*"

    scene v12ferryi5 # FPP. Show Mr lee walking off.
    with dissolve

    pause 0.75

    scene v12ferryi1
    with dissolve

    ry "Why'd you hit me so hard???"

    scene v12ferryi2
    with dissolve

    imre "Told you not to call me your wife."

    scene v12ferryi1
    with dissolve

    ry "Chill out, it's not my fault we have to do this. I'm not for hitting a woman, but I will beat the shit out of you."

    scene v12ferryi1a # FPP. same 1, mouth closed
    with dissolve

    u "*Laughs*"

    scene v12ferryi6 # FPP. Show imre and ryan looking at mc.
    with dissolve

    pause 0.75

    scene v12ferryi7 # FPP. Show imre and ryan now closer looking at camera, mouths closed
    with dissolve
    
    u "You two are idiots, literally the funniest thing I've seen in my entire life was watching you guys for the last five minutes."

    scene v12ferryi8 # FPP. Show imre, mouth open
    with dissolve

    imre "It's not supposed to be funny. I'm just doing this 'cause I think the teach may just really throw me overboard."

    scene v12ferryi9 # FPP. Show ryan, mouth open
    with dissolve

    ry "He keeps following us around because my wife here won't stay in character."

    scene v12ferryi8
    with dissolve

    imre "..."

    scene v12ferryi8a # FPP. Same 8, mouth closed
    with dissolve

    u "Not gonna hit him again for calling you his wife?"

    scene v12ferryi8
    with dissolve

    imre "He's being given the silent treatment."

    scene v12ferryi8a
    with dissolve

    u "*Laughs* You guys are like a real couple."

    scene v12ferryi9
    with dissolve

    ry "We are a real couple. We're the Storks and we're from South Africa exploring the world together. The attraction of this ship drew us in so much we decided to take it for our honeymoon."

    scene v12ferryi9a # FPP. same 9, mouth closed
    with dissolve

    u "*Chuckles* So this is your honeymoon?"

    scene v12ferryi9
    with dissolve

    ry "Yep, we're proud newlyweds."

    menu:
        "Tease Imre":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            scene v12ferryi9a
            with dissolve
            
            u "Well allow me to congratulate the lovely couple! As a gift, feel free to come to my next fight as VIP's. I'll be sure to put you on the list as Mr. and Mrs. Stork."

            scene v12ferryi9
            with dissolve

            ry "That's so nice of you!"

            scene v12ferryi8
            with dissolve

            imre "We won't be going."

            scene v12ferryi8a
            with dissolve

            u "Oh, that's unfortunate."

        "Tell Ryan to cool it":
            $ reputation.add_point(RepComponent.BRO)
            
            scene v12ferryi9a
            with dissolve
            
            u "As funny as it is, chill a little bit Ryan. You wouldn't be so happy if you were playing the wife. I'm sure Imre would be giving it to you good."

            scene v12ferryi8
            with dissolve

            imre "BRO!!"

            scene v12ferryi8a
            with dissolve

            u "What?"

            scene v12ferryi8
            with dissolve

            imre "Watch what you say! At least follow it with \"no homo\" or something!"

            scene v12ferryi8a
            with dissolve

            u "*Laughs* My bad, you guys should come out to my next fight as VIPs. It's on me."

            scene v12ferryi8
            with dissolve

            imre "Yeah, we won't be going."

            scene v12ferryi8a
            with dissolve

            u "Oh, that's unfortunate."

    scene v12ferryi9
    with dissolve

    ry "Why can't we go?"

    scene v12ferryi8
    with dissolve

    imre "We can't go because this man here is a lazy dumbass that quit his job. Now he's broke and living with me until he gets his life together. That's literally what our cards said."

    scene v12ferryi8a
    with dissolve

    u "Damn Ryan, you're kind of a dumbass."

    scene v12ferryi10 # FPP. Show ryan grabbing imre's hand, ryan mouth open
    with dissolve

    ry "What can I say, it was in the pursuit of true love."

    scene v12ferryi10a # FPP. same 10, Show imre pulling his hand away. imre mouth open
    with dissolve

    imre "Bro I'm not playing with you."

    scene v12ferryi10b # FPP. Same 10, show ryan puckering up to ryan for a kiss
    with dissolve

    ry "Aww, baby just give me a kiss."

    u "*Laughs*"

    scene v12ferryi8
    with dissolve

    imre "Fuck you guys."

    scene v12ferryi11 # FPP. Show imre walking off
    with dissolve

    pause 0.75

    scene v12ferryi11a # FPP. Show Imre now sprinting away.
    with dissolve

    ry "Oh my gosh, this is gold."

    u "It is kind of funny."

    scene v12ferryi9
    with dissolve

    ry "He's always the one instigating me and now the tables have turned."

    scene v12ferryi9a
    with dissolve

    u "But hey, don't mess with him too much. I wouldn't be surprised if he actually hit you."

    scene v12ferryi9
    with dissolve

    ry "Haha, I may not be a famous boxer, but I'll be just fine."

    scene v12ferryi9a
    with dissolve

    u "Alright man."

    scene v12ferryi13 # FPP. Show mc walking away
    with dissolve
    
    pause 0.75

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_right_gallery_back

label v12s7_ryan1:
    $ freeroam9.add("ryan")

    $ v12s7_seenList = [amber]
    if (v12s7_riley_moved and not "riley2" in freeroam9) or amber in v12s7_killList:
        $ v12s7_seenList = []

    show screen murder_button_overlay(ryan)

    scene v12ferry1 # FPP. Show ryan, slight smile, mouth closed
    #with dissolve

    u "Your wife still hasn't come back?"

    stop music fadeout 3
    play music "music/v12/Track Scene 7_5.mp3" fadein 2

    scene v12ferry1a # FPP. Same 1, mouth open
    with dissolve

    ry "Nope, and I haven't seen Mr. Lee either so I'm just waiting here. *Chuckles*"

    scene v12ferry1
    with dissolve

    u "Wow, you guys just won't ever get along, huh?"

    scene v12ferry1a
    with dissolve

    ry "Probably not, I can get over being in different frats, but I can't get over his disrespect. I know he's your friend and he's cool with you, but he's not cool with me."

    scene v12ferry1
    with dissolve

    u "Ever thought about just apologizing to squash the beef?"

    scene v12ferry1a
    with dissolve

    ry "Ugh, no. *Chuckles* Being cool with him doesn't make my life any better."

    scene v12ferry1
    with dissolve

    u "Isn't being at odds with him making your life worse?"

    scene v12ferry1a
    with dissolve

    ry "No not really, honestly, it's the only thing that's really kept me from being bored on this trip."

    scene v12ferry1
    with dissolve

    u "You're not enjoying Europe?"

    scene v12ferry1a
    with dissolve

    if emily_europe:
        scene v12ferry1a
        with dissolve
        
        ry "Well, there is a certain someone that's been making it a little better."
    else:
        scene v12ferry1a
        with dissolve
        
        ry "Nope, all of my friends are back on campus for the most part."

    scene v12ferry1
    with dissolve

    u "Well, we're gonna be here in Paris for a bit and still have another stop after that so you should definitely try and enjoy it while you're here."

    scene v12ferry1a
    with dissolve

    ry "Honestly I wouldn't know how else I can play into this role without continuing to piss Imre off. *Chuckles*"

    scene v12ferry1
    with dissolve

    u "Yeah, it does seem to be part of your role."

    scene v12ferry1b # FPP. Same 1, new pose, mouth open
    with dissolve

    ry "He's sensitive to anything gay, it makes it so easy to bother him. I told him I can't wait till tonight, that I was gonna show him a good time."
    ry "If Mr. Lee wasn't nearby I don't know what he would've done, but his face got super red. *Laughs*"

    scene v12ferry1c # FPP. same 1, new pose, mouth closed
    with dissolve

    u "*Laughs* Be careful, this is gonna be over eventually and he won't be worried about Mr. Lee anymore. He may just throw you overboard himself."

    scene v12ferry1b
    with dissolve

    ry "That would suck. I can barely swim."

    scene v12ferry1c
    with dissolve

    u "What? *Chuckles*"

    scene v12ferry1b
    with dissolve

    ry "What do you mean \"what\"?There's a lot of adults that don't know how to swim, and I'm not saying I don't know how to, I'm saying I barely know how to."

    scene v12ferry1c
    with dissolve

    u "*Laughs* How do you barely know how to swim?"

    scene v12ferry1b
    with dissolve

    ry "Because, I've never been swimming before, but like, I'm sure it's not that hard."

    scene v12ferry1c
    with dissolve

    u "YOU'VE NEVER BEEN SWIMMING?"

    scene v12ferry1b
    with dissolve

    ry "Bro chill, why you so loud? No, I haven't been swimming before. I don't see the big deal."

    scene v12ferry1c
    with dissolve

    u "Maybe because we live in California right next to an ocean?"

    scene v12ferry1b
    with dissolve

    ry "I don't really like the ocean. You know we've only discovered like five percent of it? Nobody knows what's in there, and I'm not gonna be fish food."

    scene v12ferry1c
    with dissolve

    u "Haha, I'm gonna go let Mr. Lee know you want to get in the water."

    scene v12ferry1a
    with dissolve

    ry "You do that and I'll let Charli know you want to be roommates in Paris."

    scene v12ferry1
    with dissolve

    u "I may be willing to take that risk. *Chuckles*"

    scene v12ferry1a
    with dissolve

    ry "You're brave. *Chuckles*"

    scene v12ferry2 # TPP. Show mc walking away
    with dissolve

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_right_gallery_back

label v12s7_ryan_kill:
    hide screen murder_button_overlay

    scene v12ferry3 # TPP. Show MC pointing finger gun at ryan, mouth open
    with dissolve

    u "Boom."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_7.mp3" fadein 2

    scene v12ferry1a
    with dissolve

    ry "Wait, you're the killer?"

    scene v12ferry1
    with dissolve

    u "Yep."

    scene v12ferry1b
    with dissolve

    ry "Oh shoot, that's great. The one thing Imre and I agree on is ending this game so hurry up and kill everyone."

    scene v12ferry1c
    with dissolve

    u "Haha, okay."

    scene v12ferry2 # TPP. Show mc walking away
    with dissolve

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_right_gallery_back

label v12s7_imre2:
    $ freeroam9.add("imre2")
    $ v12s7_seenList = []

    show screen murder_button_overlay(imre)

    scene v12ferim1 # FPP. Show imre, mouth closed
    #with dissolve

    u "Hello Mrs."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_9.mp3" fadein 2

    scene v12ferim1a # FPP. Same 1, mouth open
    with dissolve

    imre "Get out of here with that shit bro."

    scene v12ferim1
    with dissolve

    u "Bro chill out, why do you let that bother you so much?"

    scene v12ferim1a
    with dissolve

    imre "It's not bothering me anymore than it would bother anyone else. You guys are acting like I'm actually gay or something."

    scene v12ferim1
    with dissolve

    u "I don't think that's what anyone is doing. *Chuckles*"

    scene v12ferim1a
    with dissolve

    imre "Yeah you are, and we both know that's far from true. Always have and always will be a man of the ladies."

    scene v12ferim1
    with dissolve

    u "Not being able to take a joke and being super sensitive makes you look way more sus."

    scene v12ferim1a
    with dissolve

    imre "No it doesn't, it needs to be known I don't rock like that. You, Charli and Ryan may think it's all fun and games, but I don't."

    scene v12ferim1
    with dissolve

    u "If it really bothers you I can try and reel it back, but I can't make any promises. *Chuckles* At least not during the game."

    scene v12ferim1a
    with dissolve

    imre "Man fuck this game, Mr. Lee literally did all of this just to fuck with me."

    scene v12ferim1
    with dissolve

    u "You sure about that?"

    scene v12ferim1a
    with dissolve

    imre "Ugh duh. He gave me the worst character, he's following me around, and threating to throw me in the fucking water. Yeah, he's just doing this to be a dick."
    imre "If I wasn't here you guys would be kicking back enjoying the breeze. If the fucking murderer would do his job or hurry up and get caught this would finally be over with."

    scene v12ferim1
    with dissolve

    u "So I guess that means you haven't found the killer and aren't the killer."

    scene v12ferim1a
    with dissolve

    imre "I would've shut this shit down a long time ago if I was the killer."

    scene v12ferim1
    with dissolve

    u "So what's your plan to catch the killer then?"

    scene v12ferim1a
    with dissolve

    imre "I haven't been able to do anything, because Mr. Lee won't let me breathe. He got distracted and it gave me a chance to get over here. He hasn't found me yet."
    imre "If the killer would just kill me so I can be done with this that'd be great. Then Ryan can be a dumbass widow with no job on a cruise by himself walking around like an idiot."

    scene v12ferim1
    with dissolve

    u "Seems like you're enjoying his character's sad story quite a bit."

    scene v12ferim1a
    with dissolve

    imre "It just fits him well."

    scene v12ferim1
    with dissolve

    u "Well, good luck dying."

    scene v12ferim1a
    with dissolve

    imre "This is the first time I've said \"kill me now\" and actually meant it. *Laughs*"

    scene v12ferim1
    with dissolve

    u "*Laughs*"

    scene v12ferim1a
    with dissolve

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_foyer

label v12s7_imre_kill:
    hide screen murder_button_overlay

    scene v12ferim2 # TPP. Show MC pointing finger gun at imre, mouth open
    with dissolve

    u "Boom."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_7.mp3" fadein 2

    scene v12ferim1b # FPP. same 1,new pose, mouth open
    with dissolve

    imre "Please tell me you're not joking with me right now?"

    scene v12ferim1c # FPP. same 1,new pose, mouth closed
    with dissolve

    u "Haha, nope, I'm actually the killer."

    scene v12ferim1b
    with dissolve

    $ grant_achievement("mercy_killing")
    imre "FREEDOM!!!"

    scene v12ferim1c
    with dissolve

    u "Bro hush. *Chuckles* I have more people to kill."

    scene v12ferim1b
    with dissolve

    imre "Sorry man, I just feel so good right now. It feels good to be dead. Thanks man."

    scene v12ferim1c
    with dissolve

    u "Haha, you're welcome."

    scene v12ferim3 # TPP. Show mc walking away (back to camera)
    with dissolve

    u "(He's crazy. *Chuckles*)"

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_foyer

label v12s7_lindsey_charlie1:
    $ freeroam9.add("lindsey")
    $ v12s7_seenList = [lindsey, charli]

    show screen murder_button_overlay(lindsey)

    scene v12ferlich1 # FPP. Show charli, mouth closed
    #with dissolve

    u "Surprised we haven't crashed yet."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_10.mp3" fadein 2

    scene v12ferlich1a # FPP. Same 1, rolling eyes
    with dissolve

    pause 0.75

    scene v12ferlich2 # FPP. Show lindsey, slight smile, mouth open
    with dissolve

    li "Hey hey, got any good leads for us? I ran everything over with the Captain and we haven't come up with anything."

    scene v12ferlich2a # FPP. Same 2, mouth closed
    with dissolve

    u "I've got nothing, haven't been doing much looking around."

    scene v12ferlich1b # FPP. Same 1, mouth open
    with dissolve

    charli "Murderers don't need to look around for the murderer."

    scene v12ferlich2
    with dissolve

    li "And you think he's the murderer because..."

    scene v12ferlich1b
    with dissolve

    charli "Mr. Lee gave us our roles and it would make sense to me that he'd choose [name] as the killer."

    scene v12ferlich2
    with dissolve

    li "Well, let's not jump to conclusions. So far, based on my notes I've ruled out some people. I've ruled out Imre, Ryan, and Amber."

    scene v12ferlich2a
    with dissolve

    u "How'd you rule them out?"

    scene v12ferlich2
    with dissolve

    li "Well, it was actually Charli. Charli, do you want to explain?"

    scene v12ferlich1b
    with dissolve

    charli "You may have a hard time understanding so try and focus."

    scene v12ferlich1
    with dissolve

    u "*Sighs*"

    scene v12ferlich1b
    with dissolve

    charli "Imre wants the game to be over, if he was the murderer he would've killed Ryan in front of someone in order to get caught."
    charli "Ryan would have killed Imre out of frustration and Amber has had too many opportunities to kill people yet she hasn't. So we know none of them are the killer."

    scene v12ferlich1
    with dissolve

    u "Are there people you're suspicious of?"

    scene v12ferlich1b
    with dissolve

    charli "Outside of you, no."

    scene v12ferlich2
    with dissolve

    li "I have other suspicions, as a detective it's my job to be open minded. I'm suspecting Lauren."

    scene v12ferlich1b
    with dissolve

    charli "Because she's a criminal."

    scene v12ferlich2
    with dissolve

    li "Well, yes."

    scene v12ferlich1b
    with dissolve

    charli "*Chuckles* It's definitely not her, too obvious and Mr. Lee would never choose her."

    scene v12ferlich2
    with dissolve

    li "Or that's what he wants you to think. When solving a problem, you always gotta work backwards, that way you're never surprised by what's to come."

    scene v12ferlich2a
    with dissolve

    u "Yeah, c'mon now Charli."

    scene v12ferlich1b
    with dissolve

    charli "I'm not sure that applies here., I'm itching to use my PA system though, so once you find something worth announcing please let me know."

    scene v12ferlich2
    with dissolve

    li "Only if you let me join you."

    scene v12ferlich1b
    with dissolve

    charli "I don't see why not."

    scene v12ferlich2
    with dissolve

    li "Good, [name]. You sure there's nothing you've seen?"

    menu:
        "Ryan is suspicious":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            scene v12ferlich2a
            with dissolve
            
            u "Well, I did see Ryan say something about wiping everyone out. He said it to Imre, but I don't know what the context was."

            scene v12ferlich1b
            with dissolve

            charli "Throwing the blame, huh?"

            scene v12ferlich1
            with dissolve

            u "Uhh no, just saying what I heard."

        "No, nothing":
            scene v12ferlich2a
            with dissolve
            
            u "Nope, nothing. Haven't got a clue who it is."

            scene v12ferlich1b
            with dissolve

            charli "Don't want to admit it's you, but also don't want to look suspicious by passing the blame. You're too predictable."

            scene v12ferlich1
            with dissolve

            u "Whatever you say man. Don't let that Captain shit go to your head."

    scene v12ferlich2b # fpp. same 2, new pose, mouth open
    with dissolve

    li "Hmmm, well I'm gonna start with Ryan. I know we ruled him out but I'm still suspicious."

    scene v12ferlich1c # FPP. same 1, new pose, mouth open
    with dissolve

    charli "So you're leaving me here then?"

    scene v12ferlich2b
    with dissolve

    li "Yeah, sorry. *Chuckles*"

    menu:
        "Smarter to stay here":
            scene v12ferlich2a
            with dissolve

            u "Isn't it smarter to stay up here the whole time? You know Charli isn't the killer, plus Amber is supposed to be keeping you guys updated, right?"

            scene v12ferlich2b
            with dissolve

            li "True... It's probably more fun out there though."

            scene v12ferlich1c
            with dissolve

            charli "Oh..."

            scene v12ferlich2b
            with dissolve

            li "No, I- I didn't mean it like that, I... Nevermind. *Laughs* I'm just gonna stay here. Where we're both safe..."

            scene v12ferlich1c
            with dissolve

            charli "Yay!"

            scene v12ferlich1d # FPP. same 1, new pose to match 1c, mouth closed
            with dissolve

            u "(Yay...) Well, I'll come check on you in a bit, yeah?"

            scene v12ferlich2b
            with dissolve

            li "Sounds good!"

        "More investigators":
            $ v12s7_lindsey_moved = True
            
            scene v12ferlich2a
            with dissolve

            u "The more people we have investigating, the quicker we can find out who the killer is."

            scene v12ferlich2b
            with dissolve

            li "Exactly. I'll come check on you every so often, okay? *Chuckles*"

            scene v12ferlich1c
            with dissolve

            charli "If you come back and I'm not here then [name] was the killer."

            scene v12ferlich2b
            with dissolve

            li "Noted."

            scene v12ferlich3 # FPP. show lindsey walking away
            with dissolve

            pause 0.75

            scene v12ferlich1c
            with dissolve
            
            charli "Hurry up and get it over with."

            scene v12ferlich1d
            with dissolve

            u "Ha, I couldn't be a good guy to you even in a made up scenario."

            scene v12ferlich1c
            with dissolve

            charli "Nope."

            scene v12ferlich1d
            with dissolve

            u "Well, definitely not hanging around you for fun, later Charli."

            scene v12ferlich1c
            with dissolve

            charli "..."

            scene v12ferlich1d
            with dissolve

            u "(Asshole.)"

    scene v12ferlich4 # FPP. Show mc walking away
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_captains_room

label v12s7_lindsey2:
    $ freeroam9.add("lindsey2")
    $ v12s7_seenList = []

    show screen murder_button_overlay(lindsey)

    scene v12ferli1 # FPP. Show lindsey from a distance, mouth open 
    #with dissolve

    li "Come over here citizen."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_5.mp3" fadein 2

    scene v12ferli2 # TPP. Show mc walking closer to lindsey
    with dissolve

    pause 0.75

    scene v12ferli3 # FPP. Show Lindsey, slight smile, mouth closed
    with dissolve

    u "Yes ma'am. *Chuckles*"

    scene v12ferli3a # FPP. Same 3, mouth open
    with dissolve

    li "I'm getting a lot closer to cracking this case."

    scene v12ferli3
    with dissolve

    u "Is that so?"

    scene v12ferli3a
    with dissolve

    li "It is, several people on board have told me Ryan aka Mr. Stork has not only mentioned killing people, but that he wants to see if he can kill everyone on board without being caught."

    scene v12ferli3
    with dissolve

    u "That would explain why he hasn't killed Imre or anyone in front of Imre."

    scene v12ferli3a
    with dissolve

    li "Exactly, because it's Imre's or Mrs. Stork's ultimate goal to end the game."

    scene v12ferli3
    with dissolve

    u "Have you spoken to the Storks, maybe try and get them to separate?"

    scene v12ferli3a
    with dissolve

    li "I considered it, but it's too risky. With it being so easy to murder without being caught and me being the main one interested in catching the murderer, I can't risk getting killed."

    scene v12ferli3
    with dissolve

    u "Well... sacrifice someone."

    scene v12ferli3a
    with dissolve

    li "*Chuckles* I considered that, but I'm having a hard time choosing who."

    menu:
        "Me":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            scene v12ferli3
            with dissolve
            
            u "I can be your distraction. I'll just try and separate them... then see if I get murked or not."

        "Charli":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            scene v12ferli3
            with dissolve

            u "Let Charli be your distraction."

            scene v12ferli3a
            with dissolve

            li "Charli can't leave his spot though."

            scene v12ferli3
            with dissolve

            u "Just start talking to people about how vulnerable Charli is and see who takes the bait."

    scene v12ferli3a
    with dissolve

    li "Hmmm, not a bad idea."

    scene v12ferli3
    with dissolve

    u "*Whisper* Why are you taking this so serious?"

    scene v12ferli3a
    with dissolve

    li "The same reason you're whispering. *Chuckles* But I'm also having fun with it."

    scene v12ferli3
    with dissolve

    u "Keeping your mind off the Chicks stuff?"

    scene v12ferli3a
    with dissolve

    li "I'm not even worried about all that anymore."

    scene v12ferli3
    with dissolve

    u "Wait, you're not running anymore?"

    scene v12ferli3b # FPP. same 3, new pose, mouth open
    with dissolve

    li "Oh no, I'm definitely running. I'm saying I'm not stressed about it anymore. Most of the girls are cool with me running, I have a gameplan to persuade the others, so right now I'm happy just enjoying Europe."

    scene v12ferli3c # FPP. Same 3, new pose to match 3b, mouth closed
    with dissolve

    u "You never fail to amaze me Lindsey."

    scene v12ferli3b
    with dissolve

    li "I didn't become a detective by not being great."

    scene v12ferli3c
    with dissolve

    u "Mr. Lee obviously chose all of our characters with a purpose. Why do you think he chose for you to be a detective?"

    scene v12ferli3b
    with dissolve

    li "I'm not sure, but I have been wondering."

    scene v12ferli3c
    with dissolve

    u "Does he know about the Chicks stuff?"

    scene v12ferli3b
    with dissolve

    li "There's no telling what he knows and doesn't know. It seems as though Mr. Lee knows everything."

    scene v12ferli3c
    with dissolve

    u "You're not wrong about that. Question, why didn't you think I was the killer?"

    scene v12ferli3b
    with dissolve

    li "I wouldn't say I didn't think you were. I wasn't one way or the other, but Charli just had such an obvious bias so I didn't want to be blinded by that."

    scene v12ferli3c
    with dissolve

    u "What if you're blinded by liking me?"

    scene v12ferli3b
    with dissolve

    li "Who says I like you?"

    scene v12ferli3c
    with dissolve

    u "Oh so you don't like me? *Chuckles*"

    scene v12ferli3b
    with dissolve

    li "Oh that's not fair, you just tried to hit me with a trap question. *Chuckles*"

    scene v12ferli3c
    with dissolve

    u "Oh no it's fine, Charli's got me used to not being liked."

    scene v12ferli3b
    with dissolve

    if lindsey.relationship >= Relationship.KISS:
        scene v12ferli5 # TPP. Show mc and lindsey kissing
        with dissolve

        pause 1.75

    scene v12ferli3b
    with dissolve

    li "Well, I definitely don't dislike you... But that has nothing to do with the game and I'm not getting thrown overboard so I'm getting back to my investigation."

    scene v12ferli3c
    with dissolve

    u "Ha, you do that."

    scene v12ferli6 # FPP. Show lindsey walking away
    with dissolve

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    $ v12s7_endtalkList.append(lindsey)

    call screen v12s7_rear

label v12s7_lindsey_kill:
    hide screen murder_button_overlay

    scene v12ferli7 # TPP. Show mc, mouth open, pointing finger guns at lindsey
    with dissolve

    u "Boom."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_7.mp3" fadein 2

    scene v12ferli8 # FPP. Show lindsey, slight smile, mouth open
    with dissolve

    li "You've got to be kidding me."

    scene v12ferli8a # FPP. same 8, mouth closed
    with dissolve

    u "I'm not though. *Chuckles*"

    scene v12ferli8
    with dissolve

    li "Maybe I should listen to Charli more often. *Chuckles*"

    scene v12ferli8a
    with dissolve

    u "Or not, that'd work too."

    scene v12ferli8
    with dissolve

    li "Haha, good luck murderer."

    scene v12ferli9 # FPP. Show lindsey walking away
    with dissolve

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_rear

label v12s7_charli2:
    $ freeroam9.add("charli")
    $ v12s7_seenList = []

    show screen murder_button_overlay(charli)

    scene v12fercha1 # FPP. Show charli alone, mouth closed
    #with dissolve

    u "Still alone huh?"

    stop music fadeout 3
    play music "music/v12/Track Scene 7_10.mp3" fadein 2

    scene v12fercha1a # FPP. Same 1, mouth open
    with dissolve

    charli "And so are you."

    scene v12fercha1
    with dissolve

    u "Haven't heard you on the PA."

    scene v12fercha1a
    with dissolve

    charli "Haven't had anything to say."

    scene v12fercha1
    with dissolve

    u "You have the most annoying voice I've ever heard."

    scene v12fercha1a
    with dissolve

    charli "And you have the most annoying personality."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    $ v12s7_endtalkList.append(charli)

    call screen v12s7_captains_room

label v12s7_charli_kill:
    hide screen murder_button_overlay
    
    scene v12fercha2 # TPP. Show MC pointing a finger gun at charli, mouth open
    with dissolve

    if len(v12s7_killList) == v12s7_victims:
        $ grant_achievement("best_for_last")

    u "Boom."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_4.mp3" fadein 2

    scene v12fercha1a
    with dissolve

    charli "Took you long enough."

    scene v12fercha1
    with dissolve

    u "Don't act like you actually knew it was me. You're just happy because you got lucky and now it looks you were right all along."

    scene v12fercha1a
    with dissolve

    charli "Think what you want to think."

    scene v12fercha3 # FPP. Show charli leaving
    with dissolve

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_captains_room

label v12s7_msrose1:
    $ freeroam9.add("rose")

    $ v12s7_seenList = []
    if v11_invite_sam_europe and not "samantha" in freeroam9:
        $ v12s7_seenList.append(samantha)

    show screen murder_button_overlay(ms_rose)

    scene v12fermsr1 # FPP. Show ms rose, seductive look, mouth open
    #with dissolve

    ro "Hello there world-famous boxing champion."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_10.mp3" fadein 2

    scene v12fermsr1a # FPP. same 1, mouth closed
    with dissolve

    u "And you are?"

    scene v12fermsr1
    with dissolve

    ro "*Shocked* You don't know who I am?"

    scene v12fermsr1a
    with dissolve

    u "I'm sorry, but no."

    scene v12fermsr1
    with dissolve

    ro "I'm the world renowned and very beloved Mia Scarlett. Most known for my role in the movie \"History Class\"."

    scene v12fermsr1a
    with dissolve

    u "*Laughs* \"History Class\"? Oh yeah, I think I have seen you in a few films."

    scene v12fermsr1
    with dissolve

    ro "In films? That's it? You don't remember meeting me at your special Christmas wonderland fight?"

    scene v12fermsr1a
    with dissolve

    u "Hmm, I'm not sure?"

    scene v12fermsr1
    with dissolve

    ro "Poofy hair doesn't ring a bell?"

    scene v12fermsr1a
    with dissolve

    u "Still not clicking for me."

    scene v12fermsr6 # FPP. Show ms rose, seductive look, finger on her lip
    with dissolve

    pause 0.75

    scene v12fermsr1
    with dissolve

    ro "Do I ring a bell now?"

    scene v12fermsr1a
    with dissolve

    u "OH THAT MIA, MIA SCARLETT!!! YES, I REMEMBER!"

    scene v12fermsr1
    with dissolve

    ro "Thought that'd help jog your memory."

    scene v12fermsr1a
    with dissolve

    u "Hard not to remember after that."

    scene v12fermsr1
    with dissolve

    ro "Usually I have to be wary of people because most people only associate with me for my fame and money, yet you couldn't even remember who I was. Are you that self-centered?"

    scene v12fermsr1a
    with dissolve

    u "I just treat everyone as a regular person, fame and wealth mean nothing to me."

    scene v12fermsr1
    with dissolve

    ro "Mr. Humble huh?"

    scene v12fermsr1a
    with dissolve

    u "I do my best."

    scene v12fermsr1
    with dissolve

    ro "So, have you heard about the famous killer aboard the ship?"

    scene v12fermsr1a
    with dissolve

    u "I have. Do you know anything about that? Ideas on who it may be?"

    scene v12fermsr1
    with dissolve

    ro "Honestly, no."

    scene v12fermsr3 # TPP. Show ms rose, whispering in mc's ear.
    with dissolve

    ro "*Whisper* I was left out of the loop on most things."

    scene v12fermsr1a
    with dissolve

    u "*Whisper* Oh okay."

    scene v12fermsr1
    with dissolve

    ro "Are you worried at all about getting killed while on board?"

    scene v12fermsr1
    with dissolve

    menu:
        "Not really":
            $ reputation.add_point(RepComponent.BRO)
            scene v12fermsr1a
            with dissolve
            
            u "No not really, if anyone runs up on me I have two guns waiting for them."

        "Who wouldn't be":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            scene v12fermsr1a
            with dissolve
            
            u "Yes, but who wouldn't be."

    scene v12fermsr1b # FPP. same 1, new pose, mouth open
    with dissolve

    ro "Yes or no, either one just makes me think you're just trying to take suspicion off yourself."

    scene v12fermsr1c # FPP. same 1, new pose to match 1b, mouth closed
    with dissolve

    u "So there's no right answer then huh?"

    scene v12fermsr1b
    with dissolve

    ro "Not when talking to me."

    scene v12fermsr1c
    with dissolve

    u "Shame. No other suspects?"

    scene v12fermsr1b
    with dissolve

    ro "A few, but a smart player never shows her hand."

    scene v12fermsr1c
    with dissolve

    u "Tough cookie to crack, I'll keep my eye on you."

    scene v12fermsr1b
    with dissolve

    ro "And I on you, little boxer boy."

    scene v12fermsr2 # TPP. Show mc leaving.
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_seating_front

label v12s7_ms_rose_kill:
    hide screen murder_button_overlay

    scene v12fermsr4 # TPP. MC points a finger gun at Ms. Rose, mc mouth open
    with dissolve

    u "Boom."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_4.mp3" fadein 2

    scene v12fermsr1b
    with dissolve

    ro "That sly Bruce..."

    scene v12fermsr1c
    with dissolve

    u "Haha, what?"

    scene v12fermsr1b
    with dissolve

    ro "He went on and on about how he wasn't going to choose you as the murderer, but that's exactly what he did."

    scene v12fermsr1c
    with dissolve

    u "Tada."

    scene v12fermsr1b
    with dissolve

    ro "I was convinced he'd choose you, but he made it seem so clear that it wouldn't be you. I'm actually shocked."

    scene v12fermsr1c
    with dissolve

    u "I'm shocked he didn't tell you and made you actually play a role."

    scene v12fermsr1b
    with dissolve

    ro "That was because I lost a bet. *Chuckles*"

    scene v12fermsr1c
    with dissolve

    u "Ahhh okay."

    scene v12fermsr1b
    with dissolve

    ro "Good luck, hope you get everyone."

    scene v12fermsr5 # FPP. Show Ms rose leaving.
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_seating_front

label v12s7_penelope1:
    $ freeroam9.add("penelope")
    $ v12s7_seenList = []

    show screen murder_button_overlay(penelope)

    scene v12ferpen1 # FPP. Show penelope, neutral look, mouth closed
    #with dissolve

    u "Hey hey hey!"

    stop music fadeout 3
    play music "music/v12/Track Scene 7_11.mp3" fadein 2

    scene v12ferpen1a # FPP. same 1, mouth open
    with dissolve

    pe "Please sir, I was told not to speak to any of the passengers."

    scene v12ferpen1
    with dissolve

    u "I won't tell if you won't."

    scene v12ferpen1a
    with dissolve

    pe "I really should be cleaning before he comes back and checks up on me. I've been in the same place for like ten minutes because this one little spot won't clean."

    scene v12ferpen1
    with dissolve

    u "Wait, is he actually making you clean the boat?"

    scene v12ferpen1a
    with dissolve

    pe "Yes, he said why not kill two birds with one stone and told the actual Captain I'd help with the cleaning while on board."

    scene v12ferpen1
    with dissolve

    u "That's a little harsh."

    scene v12ferpen1a
    with dissolve

    pe "I could've enjoyed a nice ride without being bothered if I had just kept my mouth shut. I said that I couldn't wait to get on the ferry and relax and he heard me... now here we are."

    menu:
        "Let her work":
            $ reputation.add_point(RepComponent.BRO)
            scene v12ferpen1
            with dissolve
            
            u "It's got to be hard enough having to clean, so I'm sure it sucks cleaning in character. I'll leave you alone so I don't get you in trouble and are given even more work."

            scene v12ferpen1a
            with dissolve

            pe "Thanks."

            scene v12ferpen2 # TPP. Show Mc walking away
            with dissolve

            pause 0.75

            call screen v12s7_left_walkway_front

        "Help her out":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            scene v12ferpen1
            with dissolve

            u "You need to apply pressure to it."

            scene v12ferpen1a
            with dissolve

            pe "I am."

            if penelope.relationship >= Relationship.LIKES:
                scene v12ferpen1
                with dissolve

                u "*Sighs* Like this."

                scene v12ferpen3 # TPP. Show MC gets behind Penelope and wraps his arms around her grabbing her hand and applying pressure to the spot on the wall.
                with dissolve

                pe "Oh... *Chuckles*"

                u "And look at that, spot's gone."

                scene v12ferpen1a
                with dissolve

                pe "Guess I just needed a little bit of man strength."

                scene v12ferpen1
                with dissolve

                u "Just a little."

                scene v12ferpen1a
                with dissolve

                pe "What are you supposed to be again?"

                scene v12ferpen4 # TPP. Show MC punching forward, mouth open
                with dissolve

                u "I'm a famous boxer."

                scene v12ferpen1a
                with dissolve

                pe "And your name is?"

                scene v12ferpen1
                with dissolve

                u "Haha, I have no idea. My card just said famous boxer... I've been making up my story."

                scene v12ferpen1a
                with dissolve

                pe "So have you made up a name?"

                menu:
                    "John Paris":
                        scene v12ferpen1
                        with dissolve
                        
                        u "Uhm... yeah, it's John Paris."

                        scene v12ferpen1a
                        with dissolve

                        pe "*Laughs* \"John Paris\"? Not very creative huh?"

                        scene v12ferpen1
                        with dissolve

                        u "I just said what came to me."

                        scene v12ferpen1a
                        with dissolve

                        pe "That's obvious."

                    "Chase Lysol":
                        scene v12ferpen1
                        with dissolve
                        
                        u "Sure have, it's Chase Lysol."

                        scene v12ferpen1a
                        with dissolve

                        pe "Oooo, I see what you did there. Very creative."

                        scene v12ferpen1
                        with dissolve

                        u "What can I say, I'm talented like that."

                        scene v12ferpen1a
                        with dissolve

                        pe "I see."

                scene v12ferpen1b # FPP. same 1, new pose, mouth closed
                with dissolve

                u "Hey, would you like me to say something to Mr. Lee about possibly easing up on you."

                scene v12ferpen1c # FPP. same 1, new pose, mouth open
                with dissolve

                pe "That's sweet, but I'd rather just put on a brave face and get through it. I always remember it's better than $15,000."

                scene v12ferpen1b
                with dissolve

                u "That's true, but I still want you to be able to relax. I'll make sure you get to do something fun whilst in Paris."

                scene v12ferpen1c
                with dissolve

                pe "Haha, I appreciate that."

                scene v12ferpen1b
                with dissolve

                u "Take care."

                scene v12ferpen5 # TPP. Show mc starting to leave.
                with dissolve

                pause 0.75

                scene v12ferpen1c
                with dissolve

                pe "Wait a minute."

                scene v12ferpen1b
                with dissolve

                u "What-"

                scene v12ferpen6 # TPP. Show Penelope kissing mc.
                with dissolve
                play sound "sounds/kiss.mp3"

                pause 1.5

                scene v12ferpen1b
                with dissolve

                u "Oh, what was that for?"

                scene v12ferpen1c
                with dissolve

                pe "I thought you wanted me to do something fun?"

                scene v12ferpen1b
                with dissolve

                u "*Chuckles* I said in Paris."

                scene v12ferpen1c
                with dissolve

                pe "*Chuckles* Well I couldn't wait that long."

                scene v12ferpen1b
                with dissolve

                u "Haha, I'll see you later."

                scene v12ferpen2
                with dissolve
                
                pause 0.75

                stop music fadeout 3
                play music "music/v12/Track Scene 7_2.mp3" fadein 2

                call screen v12s7_left_walkway_front

            else:
                scene v12ferpen2
                with dissolve
                
                pause 0.75

                stop music fadeout 3
                play music "music/v12/Track Scene 7_2.mp3" fadein 2
                
                call screen v12s7_left_walkway_front

label v12s7_penelope_kill:
    hide screen murder_button_overlay

    scene v12ferpen7 # TPP. Show mc pointing finger gun at penelope, mc mouth open
    with dissolve

    u "Boom."
    stop music fadeout 3
    play music "music/v12/Track Scene 7_7.mp3" fadein 2

    scene v12ferpen8 # TPP. Show Penelope hugging mc
    with dissolve

    pause 1.25

    scene v12ferpen1
    with dissolve

    u "Never seen anyone hug the person that shot them. *Chuckles*"

    scene v12ferpen1a
    with dissolve

    pe "Well, now I can relax. Mr. Lee said go to the hallway if you're killed so that's where I'm going."

    scene v12ferpen1
    with dissolve

    u "Haha, you do that."

    scene v12ferpen9 # FPP. Show Penelope walking away
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_left_walkway_front

label v12s7_amber1:
    $ freeroam9.add("amber")
    
    $ v12s7_seenList = [imre, ryan]
    if "imre" in freeroam9:
        $ v12s7_seenList = []

    show screen murder_button_overlay(amber)

    scene v12feram1 # FPP. Show amber from a distance, slight smile, mouth open
    #with dissolve

    am "Hey you!"
    
    stop music fadeout 3
    play music "music/v12/Track Scene 7_12.mp3" fadein 2

    scene v12feram1a # FPP. same 1, mouth closed
    with dissolve

    u "Me?"

    scene v12feram1
    with dissolve

    am "Yeah you, come over here."

    scene v12feram2 # TPP. Show mc walking closer to amber
    with dissolve

    pause 0.75

    scene v12feram3 # TPP. Show amber(now closed), slight smile, mouth closed
    with dissolve

    u "How can I help you, officer?"

    scene v12feram3a # TPP. same 3, mouth open
    with dissolve

    am "Don't try and play all innocent, I heard all about you."

    scene v12feram3
    with dissolve

    u "What?"

    scene v12feram3a
    with dissolve

    am "Don't what me!"

    scene v12feram3
    with dissolve

    u "*Chuckles* What?"

    scene v12feram3a
    with dissolve

    am "Say what one more time and you're gonna regret it. There's several reports that someone fitting your description is carrying contraband onboard the ship. Is this true?"

    scene v12feram3
    with dissolve

    u "What is even considered contraband?"

    scene v12feram3a
    with dissolve

    am "Okay, so you think this is a game!"

    scene v12feram4 # TPP. Show amber pinning mc to the floor. amber mouth open
    with dissolve

    am "I told you not to say \"what\" anymore!"

    scene v12feram5 # TPP. Show amber sitting on mc's back. mouth open
    with dissolve

    am "Now I'm gonna ask you again, are you carrying contraband?"

    scene v12feram5a # TPP. same 5, mc mouth open
    with dissolve

    u "What... I mean, I don't know what's considered contraband."

    scene v12feram5
    with dissolve

    am "You still said what, now I feel like you're just trying to make me angry. You wouldn't like me when I'm angry."

    scene v12feram5a
    with dissolve

    u "Wait, this isn't already you being angry?"

    scene v12feram6 # TPP. Show amber patting down mc's pants pocket
    with dissolve

    am "Let's see what you got in these pockets."

    scene v12feram7 # TPP. Show mc still on the floor, mouth open
    with dissolve

    u "I don't have anything except my phone and my wallet."

    scene v12feram8 # TPP. Show amber close up, mouth open
    with dissolve

    am "Then what's this hard stick huh, some type of weapon?"

    scene v12feram7
    with dissolve

    u "Haha, some girls have thought that."

    scene v12feram8
    with dissolve

    am "Oh shit, that's your... why are you hard right now? Are you turned on by this?"

    menu:
        "A little":
            $ reputation.add_point(RepComponent.BRO)
            scene v12feram7
            with dissolve
            
            u "Getting slammed to the ground and sat on by a hot chick isn't something I thought I'd enjoy, but I'm kinda into it."

            scene v12feram8
            with dissolve

            am "Hmmm, good to know. I'll remember that for future reference."

        "No":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            scene v12feram7
            with dissolve
            
            u "Getting slammed to the ground isn't something that turns me on, but you are jerking my dick around from my pocket."

            scene v12feram8
            with dissolve

            am "Guess you don't like it rough, too bad."

    am "I didn't find anything on you, but I still don't like your tone."

    scene v12feram9 # TPP. Show amber getting off mc
    with dissolve

    pause 0.75

    scene v12feram3
    with dissolve

    u "Well I'm not sure WHAT type of tone you want me to have, but WHAT I do know is that I'll talk however I please."

    scene v12feram3a
    with dissolve

    am "You're walking on thin ice."

    scene v12feram3
    with dissolve

    u "Good thing I brought skates. *Chuckles*"

    scene v12feram3a
    with dissolve

    am "*Whisper* So you go from a boxer to an ice skater? Pick a lane. *Chuckles*"

    scene v12feram3
    with dissolve

    u "*Laughs* I'll try. But why are you being so rough?"

    scene v12feram3a
    with dissolve

    am "I'm just doing my job and should just learn to comply."

    scene v12feram3
    with dissolve

    u "Goddamn cops..."

    scene v12feram3a
    with dissolve

    am "I'm security, get it straight."

    scene v12feram3
    with dissolve

    u "Yes ma'am. *Chuckles*"

    scene v12feram3a
    with dissolve

    am "Now go about your business."

    scene v12feram3
    with dissolve

    u "Whatever you say."

    scene v12feram10 # TPP. Show mc walking away
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    $ v12s7_endtalkList.append(amber)

    call screen v12s7_right_gallery_front

label v12s7_amber_kill:
    hide screen murder_button_overlay

    scene v12feram11 # TPP. Show MC pointing finger gun at amber, mc mouth open
    with dissolve

    u "Boom."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_7.mp3" fadein 2

    scene v12feram3a
    with dissolve

    am "Damn, I hope I die like this. This is hot."

    am "Too bad I can't fuck with people anymore. Oh well, go kill some bitches."

    scene v12feram12 # TPP. Show amber walking away
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_right_gallery_front

label v12s7_riley2:
    $ freeroam9.add("riley2")
    $ v12s7_seenList = []

    show screen murder_button_overlay(riley)

    scene v12ferrile1 # FPP. Show riley, slight smile, mouth closed
    #with dissolve

    u "What's going on?"

    stop music fadeout 3
    play music "music/v12/Track Scene 7_5.mp3" fadein 2

    u "*Southern accent* I mean, what's going on?"

    scene v12ferrile1a # FPP. Same 1, mouth open
    with dissolve

    ri "Ewww, it sounds weird when you try to do it."

    scene v12ferrile1
    with dissolve

    u "Fine then, I won't do it. *Chuckles* Why aren't you being all serious, you were so excited about this."

    scene v12ferrile1a
    with dissolve

    ri "Chris is just upsetting me a bit."

    scene v12ferrile1
    with dissolve

    u "How come?"

    scene v12ferrile1a
    with dissolve

    ri "He isn't taking his role seriously at all, he's literally doing nothing."

    scene v12ferrile1
    with dissolve

    u "Maybe this just isn't for everybody."

    scene v12ferrile1a
    with dissolve

    ri "I know it's not for everybody, but there's more to it than that. As I've gotten to know and been around Chris it just seems as though he only does what he wants to do."
    ri "Most times what he wants to do is the right thing, but it's still a little selfish in my opinion."

    scene v12ferrile1
    with dissolve

    u "I didn't know you had beef with Chris."

    scene v12ferrile1a
    with dissolve

    ri "I wouldn't call it beef, it's not that serious, just forget I ever said anything."

    scene v12ferrile1
    with dissolve

    u "Gonna be a little hard to just forget. *Chuckles*"

    scene v12ferrile1a
    with dissolve

    ri "If I knock you out will that help?"

    scene v12ferrile1
    with dissolve

    u "So many violent people on this ship."

    scene v12ferrile1a
    with dissolve

    ri "One is a violent murderer and if Chris would take his role seriously it'd be easier to find out who. He's literally the only cook."

    scene v12ferrile1
    with dissolve

    u "How can the cook be helpful? *Chuckles*"

    scene v12ferrile1a
    with dissolve

    ri "I asked Mr. Lee if we could get hints from the people in the hallway and he said the only person able to talk to the people in the hallway for clues is the cook aka Chris. I talked to Chris and he refused to help."

    scene v12ferrile1
    with dissolve

    u "Why'd he refuse?"

    scene v12ferrile1a
    with dissolve

    ri "Like I said, selfish. He's just holding his phone trying to get a signal like it's gonna magically connect even though it's not working for anyone."

    scene v12ferrile1
    with dissolve

    u "He's trying to get back in touch with Sebastian, he's been on the phone a lot so whatever they're discussing must be major. His head may be in a whole other world. Then add on top of that his issues with Nora."

    scene v12ferrile1a
    with dissolve

    ri "He wouldn't have issues with Nora if he'd know how to prioritize."

    scene v12ferrile1
    with dissolve

    u "On another topic..."

    scene v12ferrile1a
    with dissolve

    ri "You're right, not my business. Gosh, I just want to find out who the killer is already."

    scene v12ferrile1
    with dissolve

    u "Don't we all?"

    scene v12ferrile1a
    with dissolve

    ri "Not everyone."

    scene v12ferrile1
    with dissolve

    u "Well, I am."

    scene v12ferrile1a
    with dissolve

    ri "I see that boxer boy. Go find out something important and report back alright."

    scene v12ferrile1
    with dissolve

    u "I'm a successful and famous boxer, I don't take orders."

    scene v12ferrile1a
    with dissolve

    ri "*Southern accent* Look here champ, take a few benjamins for yourself and just do what I asked, alright?"

    scene v12ferrile1
    with dissolve

    u "Hmmm, I guess I could make that happen."

    scene v12ferrile1a
    with dissolve

    ri "*Southern accent* Good, get to it."

    scene v12ferrile2 # TPP. Show mc walking away
    with dissolve

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    $ v12s7_endtalkList.append(riley)

    call screen v12s7_right_gallery_front

label v12s7_riley_kill2:
    hide screen murder_button_overlay

    scene v12ferrile3 # TPP. Show mc pointing finger gun at riley, mc mouth open
    with dissolve

    u "Boom."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_7.mp3" fadein 2

    scene v12ferrile1a
    with dissolve

    ri "*Whisper* You little liar."

    scene v12ferrile1
    with dissolve

    u "Haha, Mr. Lee chose a good murderer."

    scene v12ferrile1a
    with dissolve

    ri "How'd I not know? So many people thought it was Imre as he was getting on Mr. Lee's nerves. *Chuckles*"

    scene v12ferrile1
    with dissolve

    u "Nope, it was the beautiful famous boxer. *Laughs*"

    scene v12ferrile1a
    with dissolve

    ri "Wow, well I guess since you killed me I can root for you. So good luck."

    scene v12ferrile1
    with dissolve

    u "Haha, thanks."

    scene v12ferrile4 # TPP. Show riley walking away
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_right_gallery_front

label v12s7_riley2_amber:
    $ freeroam9.add("riley2")

    $ v12s7_seenList = [amber, ryan, imre]
    if "ryan" in freeroam9:
        $ v12s7_seenList = [amber]

    show screen murder_button_overlay(riley)

    scene v12feramb1 # FPP. Show amber, from a distance, looking at riley out of shot, mouth open
    #with dissolve

    am "I'm just not ready for all that, I think you're really amazing, but I'm just not the relationship person."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_5.mp3" fadein 2

    scene v12feramb2 # Show riley, from a distance, looking at amber out of shot, mouth closed
    with dissolve

    ri "We don't have to rush into anything, we can just ease into it."

    scene v12feramb1
    with dissolve

    am "I wouldn't want to give you any false hope or lead you on though."

    scene v12feramb3 # TPP. Show mc walking closer
    with dissolve

    pause 1

    scene v12feramb4 # FPP. Show riley, neutral face, mouth closed
    with dissolve

    u "Hey guys."

    scene v12feramb4a # FPP. Same 4, mouth open
    with dissolve

    ri "Uhm... hey."

    scene v12feramb5 # FPP. Show Amber, mouth open
    with dissolve

    am "Hey, do you mind giving us a second to talk?"

    scene v12feramb5a # fPP. same 5, mouth closed
    with dissolve

    u "Oh, yeah, no problem."

    scene v12feramb6 # TPP. Show mc leaving
    with dissolve

    pause 0.75
    
    scene v12feramb2
    with dissolve
    
    "*Inaudible*"
    
    scene v12feramb1
    with dissolve
    
    "*Inaudible*"

    scene v12ferrile4
    with dissolve
    
    pause 1

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_front_gallery

label v12s7_sam_cameron:
    $ freeroam9.add("samantha")
    $ v12s7_seenList = [ms_rose]

    show screen murder_button_overlay(samantha)

    scene v12fersaca1 # FPP. Show sam, slight smile, mouth open
    #with dissolve

    sa "Hey hey boxer!"

    stop music fadeout 3
    play music "music/v12/Track Scene 7_6.mp3" fadein 2

    scene v12fersaca1a # FPP. same 1, mouth closed
    with dissolve

    u "Hey!"

    scene v12fersaca2 # FPP. show cameron, mouth open
    with dissolve

    ca "[name]."

    scene v12fersaca2a # FPP. same 2, mouth closed
    with dissolve

    u "Cameron."

    scene v12fersaca1
    with dissolve

    sa "It's nice that you got to be a fighter, it was the perfect choice."

    scene v12fersaca1a
    with dissolve

    u "*Whisper* Thanks, what are you guys' characters?"

    scene v12fersaca1
    with dissolve

    sa "I'm a once famous novelist that fell off, but my upcoming novel is finally gonna turn my career around."

    scene v12fersaca1a
    with dissolve

    u "Nice nice, and what about Cameron?"

    scene v12fersaca1
    with dissolve

    sa "He doesn't have a role, because he's not part of the trip. He's just following me around, remember?"

    scene v12fersaca1a
    with dissolve

    u "Oh yeah."

    scene v12fersaca2
    with dissolve

    ca "Don't talk about me like I'm not sitting right here. I do have a role, I'm a famous comedian."

    scene v12fersaca2a
    with dissolve

    u "You just decided that yourself? *Chuckles*"

    scene v12fersaca2
    with dissolve

    ca "It was the best one for me, I'm the funniest dude alive."

    scene v12fersaca1
    with dissolve

    sa "Oh god."

    scene v12fersaca1a
    with dissolve

    u "Tell me a joke then."

    scene v12fersaca1
    with dissolve

    sa "Don't have him do that, he's been doing it all ride long."

    scene v12fersaca2
    with dissolve

    ca "Check this out. Why can't orphans play baseball?"

    scene v12fersaca2a
    with dissolve

    u "Why?"

    scene v12fersaca2
    with dissolve

    ca "'Cause they don't know where home is."

    menu:
        "Laugh":
            $ reputation.add_point(RepComponent.BRO)
            scene v12fersaca2a
            with dissolve
            
            u "*Laughs*"

            scene v12fersaca1
            with dissolve

            sa "His jokes aren't funny."

        "Don't laugh":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            scene v12fersaca2a
            with dissolve
            
            u "Not funny, man."

            scene v12fersaca1
            with dissolve

            sa "Exactly."

    scene v12fersaca1
    with dissolve

    sa "All of his jokes are about orphans, it's like he has something against orphans or something."

    scene v12fersaca2
    with dissolve

    ca "Don't critique my art because you don't understand it."

    scene v12fersaca1
    with dissolve

    sa "I understand it perfectly fine, I just think it's in poor taste."

    scene v12fersaca2
    with dissolve

    ca "Do you prefer something with a little more flavor?"

    scene v12fersaca2b # FPP. Show samantha in complete shock, mouth open
    with dissolve

    # -Cameron farts on Samantha-

    sa "I KNOW YOU DIDN'T JUST FUCKING FART ON ME! YOU'RE FUCKING GROSS!"

    scene v12fersaca3 # FPP. Show samantha storming off
    with dissolve

    pause 0.75

    scene v12fersaca2a
    with dissolve

    u "That was weird."

    scene v12fersaca2
    with dissolve

    ca "Not my fault you guys can't take a joke."

    scene v12fersaca2a
    with dissolve

    u "That wasn't even a joke, you were just being a dick to your sister."

    scene v12fersaca2
    with dissolve

    ca "What's this, you tryna be her hero or something? Just because Mr. Lee handed you those gloves doesn't mean you can fight me. Unless you wanna find out."

    scene v12fersaca2a
    with dissolve

    u "Chill out."

    scene v12fersaca2
    with dissolve

    ca "Yeah, you not ready for none of this. *Chuckles* I'm the best fighter here right now."

    scene v12fersaca2a
    with dissolve

    u "You really think you can take on Chris?"

    scene v12fersaca2
    with dissolve

    ca "With one hand behind my back."

    scene v12fersaca2a
    with dissolve

    u "Right."

    scene v12fersaca4 # TPP. Show mc walking away
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_seating_front

label v12s7_sam2:
    $ freeroam9.add("samantha2")
    $ v12s7_seenList = []

    show screen murder_button_overlay(samantha)

    scene v12fersam1 # FPP. Show samantha neutral look, mouth closed
    #with dissolve

    u "No bodyguard?"

    stop music fadeout 3
    play music "music/v12/Track Scene 7_5.mp3" fadein 2

    scene v12fersam1a # FPP. same 1, mouth open
    with dissolve

    sa "You mean no stalker."

    scene v12fersam1
    with dissolve

    u "Haha, you really weren't enjoying his jokes were you?"

    scene v12fersam1a
    with dissolve

    sa "Not at all. Even if some of them were a little funny, I don't think it's cool that all of his jokes are about orphans. The whole idea of orphans just isn't funny to me at all."

    scene v12fersam1
    with dissolve

    u "I feel where you're coming from."

    scene v12fersam1a
    with dissolve

    sa "*Whisper* He should know better."

    scene v12fersam1
    with dissolve

    u "Is there anything I can do to cheer you up a bit?"

    scene v12fersam1a
    with dissolve

    sa "Besides distracting my mind with something else? *Chuckles*"

    menu:
        "Focus on the game":
            $ reputation.add_point(RepComponent.BRO)
            scene v12fersam1b # FPP. same 1, new pose, mouth closed
            with dissolve

            u "Wanna focus on the game? That's the point of all of this, I think... To make us focus on something else for a while."

        "Go for the kiss":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            scene v12fersam1b
            with dissolve
            
            u "I think this might help you think about something else..."

            scene v12fersam1c # FPP. same 1, new pose, mouth open
            with dissolve

            sa "What-"

            scene v12fersam2 # TPP. Show mc and samantha kissing, mc's hand on samantha's cheek
            with dissolve
            play sound "sounds/kiss.mp3"

            pause 1.5

            scene v12fersam1c
            with dissolve

            sa "Oh... Yeah. *Chuckles* That definitely helps."

            scene v12fersam1b
            with dissolve

            play sound "sounds/doorclose.mp3"

            u "(Shit!) That might be Mr. Lee, shh!"

    scene v12fersam1c
    with dissolve

    sa "Quick, talk murder to me. *Laughs*"

    scene v12fersam1b
    with dissolve
    
    u "Well, let's see, novelist, can you pinpoint our murderer?"

    scene v12fersam1c
    with dissolve

    sa "Well if I was writing this, I'd probably choose Lauren to be the murderer."

    scene v12fersam1b
    with dissolve

    u "What? There's no way it'd be her."

    scene v12fersam1c
    with dissolve

    sa "See, that's exactly why I'd choose her. No one would suspect her. She wouldn't even suspect herself. *Chuckles*"

    scene v12fersam1b
    with dissolve

    u "Hmm, that's pretty smart."

    scene v12fersam1c
    with dissolve

    sa "You sound surprised. *Chuckles* Did you think I was stupid?"

    scene v12fersam1b
    with dissolve

    u "I may have wondered if it ran in the family."

    scene v12fersam1c
    with dissolve

    sa "My brother took all the stupid."

    scene v12fersam1b
    with dissolve

    u "That's believable."

    scene v12fersam1c
    with dissolve

    sa "Honestly, my life sucks. I'm an adult in college, but instead of having friends and living the life I want to live..."
    sa "I'm smothered by my brother for literally no reason except he has nothing better to do. I just want to be my own person."

    scene v12fersam1b
    with dissolve

    u "Get a restraining order."

    scene v12fersam1c
    with dissolve

    sa "I've thought about it, but I don't want to take it that far. I just want him to take my wishes into consideration for once."

    scene v12fersam1b
    with dissolve

    u "Maybe he does it because he cares, but gets carried away."

    scene v12fersam1c
    with dissolve

    sa "He sure gets carried away a lot."

    scene v12fersam1b
    with dissolve

    u "Haha, yeah. You mentioned Lauren, do you talk to her?"

    scene v12fersam1c
    with dissolve

    sa "I haven't, but I don't think we'd get along, she's too soft."

    scene v12fersam1b
    with dissolve

    u "I wouldn't jump to conclusions, just because someone is kind doesn't mean they're soft."

    scene v12fersam1c
    with dissolve

    sa "I've never seen or heard of her doing anything exciting."

    scene v12fersam1b
    with dissolve

    u "Well, you're not in her circle. Would you believe it if I told you on the very first day of school Riley, Imre, Lauren and I played Drink or Strip?"

    scene v12fersam1c
    with dissolve

    sa "There's no way Lauren played that with you guys."

    scene v12fersam1b
    with dissolve

    u "She did. C'mon now, don't judge a book until you've read it all the way through."

    scene v12fersam1c
    with dissolve

    sa "Hmm, maybe I should try talking to her. Someone I definitely wanna talk to though is Amber."
    sa "After seeing how feisty she's been with the whole security thing I definitely wanna get to know her. She seems like my type of person, plus I know her and Riley are cool."

    scene v12fersam1b
    with dissolve

    u "See, look at that, so many opportunities."

    scene v12fersam1a
    with dissolve

    sa "Yeah, I guess you're right."

    scene v12fersam1
    with dissolve

    u "When am I not?"

    scene v12fersam1a
    with dissolve

    sa "Don't ruin the moment."

    scene v12fersam1
    with dissolve

    u "Haha, my bad."

    scene v12fersam1a
    with dissolve

    sa "Well, I need to finish my book. If I don't, no one will. See you around [name] and thanks for the talk."

    scene v12fersam1
    with dissolve

    u "Anytime."

    scene v12fersam3 # FPP. Show sam walking away
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2
    
    call screen v12s7_right_walkway_back

label v12s7_samantha_kill:
    hide screen murder_button_overlay

    scene v12fersam4 # TPP. Show mc, mouth open, pointing finger fun at sam.
    with dissolve

    $ grant_achievement("talk_murder_to_me")
    u "Boom."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_7.mp3" fadein 2

    scene v12fersam1c
    with dissolve

    sa "There's no way he chose you as the killer."

    scene v12fersam1b
    with dissolve

    u "He did."

    scene v12fersam1c
    with dissolve

    sa "I'm having a hard time believing that."

    scene v12fersam1b
    with dissolve

    u "Why is that so hard to believe?"

    scene v12fersam1c
    with dissolve

    sa "You don't fit any killer theories."

    scene v12fersam1
    with dissolve

    u "Doesn't that make me the perfect choice then?"

    scene v12fersam1a
    with dissolve

    sa "I guess. Why didn't you kill me earlier?"

    scene v12fersam1
    with dissolve

    u "You were with your brother, and I didn't want to get caught."

    scene v12fersam1a
    with dissolve

    sa "He's not a part of the game idiot?"

    scene v12fersam1
    with dissolve

    u "*Laughs* Oh yeah."

    scene v12fersam1a
    with dissolve

    sa "Enjoy your little killing spree, good luck."

    scene v12fersam1
    with dissolve

    u "Later."

    scene v12fersam3
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_right_walkway_back

label v12s7_cameron2:
    $ freeroam9.add("cameron")
    $ v12s7_seenList = []

    show screen murder_button_overlay(cameron)

    scene v12fercam1 # FPP. Show cameron from a distance, mouth open
    #with dissolve

    ca "Hey [name], get over here."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_12.mp3" fadein 2

    scene v12fercam2 # TPP. Show mc walking over to cameron
    with dissolve

    pause 0.75

    scene v12fercam3 # FPP. Show cameron, slight smile, mouth closed
    with dissolve

    u "What's up?"

    scene v12fercam3a # FPP. same 3, mouth open
    with dissolve

    ca "I whipped up some more jokes."

    scene v12fercam3
    with dissolve

    u "Are they orphan jokes?"

    scene v12fercam3a
    with dissolve

    ca "I'm sticking to my specialty."

    scene v12fercam3
    with dissolve

    u "*Sighs*"

    scene v12fercam3a
    with dissolve

    ca "Alright, so tell me, what's the difference between and orphan and an apple?"

    scene v12fercam3
    with dissolve

    u "What?"

    scene v12fercam3a
    with dissolve

    ca "An apple gets picked. *Laughs*"

    scene v12fercam3
    with dissolve

    u "That's dark."

    scene v12fercam3a
    with dissolve

    ca "I got more, I got more."

    scene v12fercam3
    with dissolve

    u "Alright, let's hear it."

    scene v12fercam3a
    with dissolve

    ca "Do you know what an orphan's favorite movie is?"

    scene v12fercam3
    with dissolve

    u "What's an orphan's favorite movie?"

    scene v12fercam3a
    with dissolve

    ca "Home Alone. *Laughs* Oh my god I'm too good."

    scene v12fercam3
    with dissolve

    u "Oh god..."

    scene v12fercam4 # TPP. Show mc walking away
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_rear_gallery

label v12s7_cameron_kill:
    hide screen murder_button_overlay

    scene v12fercam5 # TPP. Show mc, mouth open, pointing finger fun at cameron
    with dissolve

    u "Boom."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_7.mp3" fadein 2

    scene v12fercam3a
    with dissolve

    ca "That's stupid. Why are you tryna kill me... you already know I'm not really part of the game."

    scene v12fercam3
    with dissolve

    u "Then why am I wasting my time with you?"

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_rear_gallery

label v12s7_nora1:
    $ freeroam9.add("nora")
    $ v12s7_seenList = []

    if not v12s7_aubrey_moved:
        $ v12s7_seenList.append(aubrey)

    if v12s7_riley_moved and not "riley2" in freeroam9:
        $ v12s7_seenList.append(riley)

    show screen murder_button_overlay(nora)

    scene v12fernor1 # FPP. Show nora, mouth closed
    #with dissolve

    u "Hey, nice to meet you. I'm sure you recognize me."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_5.mp3" fadein 2

    scene v12fernor1a # FPP. same 1, mouth open
    with dissolve

    no "Please don't come over here with all that, I'm not trying to do this right now."

    scene v12fernor1
    with dissolve

    u "Oh, damn. Sorry."

    scene v12fernor1a
    with dissolve

    no "This is a stupid fucking game, I've literally just dealt with a fucking robbery last night and this felt like a good idea?"

    scene v12fernor1
    with dissolve

    u "Maybe it was planned prior, I'm sure it was."

    scene v12fernor1a
    with dissolve

    no "Then he should've been a little more considerate and canceled it."

    scene v12fernor1
    with dissolve

    u "Well, do you want me to kill you?"

    scene v12fernor1a
    with dissolve

    no "The quicker the killer murders me, the better."

    scene v12fernor1
    with dissolve

    u "Hmm, noted. I hope that happens for you."

    scene v12fernor1a
    with dissolve

    no "Yeah, you and I both."

    scene v12fernor1
    with dissolve

    u "(She's really not into this.)"

    u "Alright um, I'll talk to you once all this is over."

    scene v12fernor1a
    with dissolve

    no "Alright, sorry. I'm not trying to be a bitch. I'm just not in the mood for this."

    menu:
        "See you later":
            $ reputation.add_point(RepComponent.BRO)
            scene v12fernor1
            with dissolve
            
            u "No, don't worry. I get it. We'll talk later."

            scene v12fernor2 # TPP. Show mc walking away
            with dissolve

            stop music fadeout 3
            play music "music/v12/Track Scene 7_2.mp3" fadein 2

            $ v12s7_endtalkList.append(nora)

            call screen v12s7_balcony_left

        "Want some company?":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            scene v12fernor1b # FPP. same 1, new pose,annoyed look, mouth closed
            with dissolve
            
            u "Do you want some company?"

            scene v12fernor1c # FPP. Same 1, new pose,annoyed look, mouth open
            with dissolve

            no "Are you sure you don't want to pay attention to the game? I'm not taking the blame if Mr. Lee sees us talking out of character."

            scene v12fernor1b
            with dissolve

            u "*Chuckles* It's fine. So, how are you feeling after last night?"

            scene v12fernor1c
            with dissolve

            no "I really don't want to think about it..."

            scene v12fernor1b
            with dissolve

            u "Shouldn't of brought it up."

            scene v12fernor1c
            with dissolve

            no "*Chuckles* It's alright. At least you actually asked. It's nice to know that someone cares."

            menu:
                "Chris cares about you":
                    $ v12_help_chris += 1
                    $ reputation.add_point(RepComponent.BRO)
                    scene v12fernor1b
                    with dissolve

                    u "Nora, I know it's hard to see while we're on the trip but Chris cares about you. I know he's super busy and it sucks not being able to-"

                    scene v12fernor1c
                    with dissolve

                    no "Look, [name]. Everything you're saying? I've heard it. About a thousand times now. And I'm so fucking over it. Why can't anyone understand this from my point of view?"

                    scene v12fernor1b
                    with dissolve

                    u "I think we do but-"

                    scene v12fernor1c
                    with dissolve

                    no "Just go, please. This isn't helping the way I thought it would."

                    scene v12fernor1b
                    with dissolve

                    u "Nora, I'm sorry. I didn't mean to-"

                    scene v12fernor1c
                    with dissolve

                    no "Please, just go. I wanna be alone."

                    scene v12fernor1b
                    with dissolve

                    u "(Fuck. I never say the right things to her, do I?)"

                    scene v12fernor3 # TPP. Show mc walking away
                    with dissolve

                    stop music fadeout 3
                    play music "music/v12/Track Scene 7_2.mp3" fadein 2

                    $ v12s7_endtalkList.append(nora)

                    call screen v12s7_balcony_left

                "Of course I care":
                    $ reputation.add_point(RepComponent.BOYFRIEND)

                    scene v12fernor1b
                    with dissolve

                    u "Nora, of course I care. I've always cared."

            scene v12fernor1c
            with dissolve

            no "It's always going to come down to me or him. You know that, right?"

            no "Eventually there will come a time when you can't play both sides. Either he'll get mad that you're talking to me or I'll get mad because you're talking to him."
            no "It's going to happen, so what would be your choice?"

            if joinwolves:
                scene v12fernor1c
                with dissolve

                no "Nevermind, I already know you're going to say him."

            menu:
                "Sounds like you're dumping him":
                    $ reputation.add_point(RepComponent.TROUBLEMAKER)
                    scene v12fernor1b
                    with dissolve

                    u "This is all starting to sound like you've decided on dumping Chris... Are you really doing this?"

                    scene v12fernor1c
                    with dissolve

                    no "Ha. Nice."

                    scene v12fernor1b
                    with dissolve

                    u "What?"

                    scene v12fernor1a
                    with dissolve

                    no "Nothing, I got my answer. You can go. Thanks for the talk."

                    scene v12fernor1
                    with dissolve

                    u "Nora, come on ple-"

                    scene v12fernor1a
                    with dissolve

                    no "It's fine. I'm fine. Just go."

                    scene v12fernor2
                    with dissolve

                    pause 0.75

                    stop music fadeout 3
                    play music "music/v12/Track Scene 7_2.mp3" fadein 2

                    $ v12s7_endtalkList.append(nora)
                    
                    call screen v12s7_balcony_left
                    
                "I'd choose you":
                    $ reputation.add_point(RepComponent.BOYFRIEND)
                    $ nora.relationship = Relationship.LIKES

                    scene v12fernor1
                    with dissolve

                    u "There's no choice."

                    if joinwolves:
                        scene v12fernor1
                        with dissolve

                        u "And there really never has been."

                    scene v12fernor1
                    with dissolve

                    u "It's always been you over him. Always will be."

                    scene v12fernor1d # FPP. Same 1, nora slight smile mouth open.
                    with dissolve

                    no "Really?"

                    scene v12fernor1e # FPp. same 1d, mouth closed
                    with dissolve

                    u "For sure. You're way more fun to be around, and a hell of a lot more attractive. *Chuckles*"

                    scene v12fernor1d
                    with dissolve

                    no "Haha! You aren't wrong. *Chuckles*"

                    scene v12fernor1e
                    with dissolve

                    u "Well, now that you're smiling again, I should get back to the game. Talk later?"

                    scene v12fernor1d
                    with dissolve

                    no "Yeah. And... thank you, really."

                    scene v12fernor1e
                    with dissolve

                    u "Of course."

                    scene v12fernor2
                    with dissolve

                    pause 0.75

                    stop music fadeout 3
                    play music "music/v12/Track Scene 7_2.mp3" fadein 2
                    $ v12s7_endtalkList.append(nora)

                    call screen v12s7_balcony_left

label v12s7_nora_kill:
    hide screen murder_button_overlay

    scene v12fernor4 # TPP. Show mc, pointing finger gun at nora, mouth open
    with dissolve

    u "Boom."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_7.mp3" fadein 2

    scene v12fernor5 # FPP. Show nora mouth closed, smiling
    with dissolve

    pause 0.75

    if nora.relationship >= Relationship.LIKES:
        scene v12fernor5a # FPP. Show nora, slight smile mouth open
        with dissolve

        no "I could kiss you right now."

        scene v12fernor6 # TPP. Show nora hugging mc.
        with dissolve

        pause

        scene v12fernor5a
        with dissolve

        no "Thanks."

        scene v12fernor5
        with dissolve

        u "Haha, you're welcome."

        scene v12fernor2
        with dissolve

        pause 0.75

        stop music fadeout 3
        play music "music/v12/Track Scene 7_2.mp3" fadein 2

        call screen v12s7_balcony_left
    else:
        scene v12fernor5a
        with dissolve

        no "It's about damn time! Thanks [name]."

        scene v12fernor5
        with dissolve

        u "Ha, no problem."

        scene v12fernor2
        with dissolve

        pause 0.75

        stop music fadeout 3
        play music "music/v12/Track Scene 7_2.mp3" fadein 2

        call screen v12s7_balcony_left

label v12s7_chris1:
    $ freeroam9.add("chris")
    $ v12s7_seenList = []

    show screen murder_button_overlay(chris)

    if "emily" in freeroam9 and emily not in v12s7_killList:
        scene v12ferchr1 # FPP. show chris, Chris is holding his phone up trying to get a signal, looking up at phone, mouth closed
        #with dissolve
    else:
        scene v12ferchrnoem1
        #with dissolve

    u "What are you doing?"

    stop music fadeout 3
    play music "music/v12/Track Scene 7_9.mp3" fadein 2

    if "emily" in freeroam9 and emily not in v12s7_killList:
        scene v12ferchr1a # FPP. Same 1, phone still in air, looking at mc, mouth open
        with dissolve
    else:
        scene v12ferchrnoem1a
        with dissolve

    ch "I'm trying to get a signal. I heard if you put foil around your phone in direct sunlight you'll get at least a bar of service. Do you know where I can find some foil?"

    if "emily" in freeroam9 and emily not in v12s7_killList:
        scene v12ferchr1b # FPP. same 1, now facing mc phone by his side, mouth closed
        with dissolve
    else:
        scene v12ferchrnoem1b
        with dissolve

    u "You need your phone that bad?"

    if "emily" in freeroam9 and emily not in v12s7_killList:
        scene v12ferchr1c # FPP. Same 1b, mouth open
        with dissolve
    else:
        scene v12ferchrnoem1c
        with dissolve

    ch "Yeah I do."

    if "emily" in freeroam9 and emily not in v12s7_killList:
        scene v12ferchr1b
        with dissolve
    else:
        scene v12ferchrnoem1b
        with dissolve

    u "You and Sebastian must be planning something big."

    if "emily" in freeroam9 and emily not in v12s7_killList:
        scene v12ferchr1c
        with dissolve
    else:
        scene v12ferchrnoem1c
        with dissolve

    ch "It's more than just us, what's going on is a serious tradition for both frats and something that needs one hundred percent focus and respect."

    if "emily" in freeroam9 and emily not in v12s7_killList:
        scene v12ferchr1b
        with dissolve
    else:
        scene v12ferchrnoem1b
        with dissolve

    u "Well man, your phone isn't going to work out here. It just won't."

    if "emily" in freeroam9 and emily not in v12s7_killList:
        scene v12ferchr1c
        with dissolve
    else:
        scene v12ferchrnoem1c
        with dissolve

    ch "*Sighs*"

    if "emily" in freeroam9 and emily not in v12s7_killList:
        scene v12ferchr1b
        with dissolve
    else:
        scene v12ferchrnoem1b
        with dissolve

    scene v12ferchr2 # Fpp. Show chris now sat down, head back against the wall looking up at mc, mouth open
    with dissolve

    ch "Then I guess, I might as well make up for the sleep I didn't get last night."

    scene v12ferchr2a # Fpp. same 2, Show chris now sat down, head back against the wall looking up at mc, mouth closed
    with dissolve

    u "Why didn't you get any sleep?"

    scene v12ferchr2
    with dissolve

    ch "Nora just kept wanting to argue, when I started ignoring her instead of arguing back with her she still just nagged me. So I was up all night."

    scene v12ferchr2a
    with dissolve

    u "Wow."

    scene v12ferchr2
    with dissolve

    ch "Yeah, but I don't want to talk about her or any of what's going on. I honestly don't even know what's going on."

    scene v12ferchr2a
    with dissolve

    u "That tired huh?"

    scene v12ferchr2
    with dissolve

    ch "Yeah, that tired."

    scene v12ferchr2a
    with dissolve

    u "Well, I guess I'll let you chill then."

    scene v12ferchr2
    with dissolve

    ch "Thanks."

    if "emily" in freeroam9 and emily not in v12s7_killList:
        scene v12ferchr3 # TPP. Show mc walking away
        with dissolve
    else:
        scene v12ferchrnoem3
        with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    $ v12s7_endtalkList.append(chris)
    call screen v12s7_kitchen

label v12s7_chris_kill:
    hide screen murder_button_overlay

    scene v12ferchr4 # TPP. Show mc pointing finger gun at chris, mc mouth open.
    with dissolve

    u "Boom."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_7.mp3" fadein 2

    if "emily" in freeroam9 and emily not in v12s7_killList:
        scene v12ferchr1c # FPP. show chris, Chris is holding his phone up trying to get a signal, looking up at phone, mouth closed
        with dissolve
    else:
        scene v12ferchrnoem1c
        with dissolve

    ch "What are you doing?"

    if "emily" in freeroam9 and emily not in v12s7_killList:
        scene v12ferchr1b # FPP. show chris, Chris is holding his phone up trying to get a signal, looking up at phone, mouth closed
        with dissolve
    else:
        scene v12ferchrnoem1b
        with dissolve

    u "I just killed you."

    if "emily" in freeroam9 and emily not in v12s7_killList:
        scene v12ferchr1c # FPP. show chris, Chris is holding his phone up trying to get a signal, looking up at phone, mouth closed
        with dissolve
    else:
        scene v12ferchrnoem1c
        with dissolve

    ch "What are you talking about?"

    if "emily" in freeroam9 and emily not in v12s7_killList:
        scene v12ferchr1b # FPP. show chris, Chris is holding his phone up trying to get a signal, looking up at phone, mouth closed
        with dissolve
    else:
        scene v12ferchrnoem1b
        with dissolve

    u "The game that we're all doing, I'm the killer, I just killed you."

    if "emily" in freeroam9 and emily not in v12s7_killList:
        scene v12ferchr1c # FPP. show chris, Chris is holding his phone up trying to get a signal, looking up at phone, mouth closed
        with dissolve
    else:
        scene v12ferchrnoem1c
        with dissolve

    ch "Okay cool, I'm dead."

    if "emily" in freeroam9 and emily not in v12s7_killList:
        scene v12ferchr1b # FPP. show chris, Chris is holding his phone up trying to get a signal, looking up at phone, mouth closed
        with dissolve
    else:
        scene v12ferchrnoem1b
        with dissolve

    u "*Chuckles* Bro, you gotta go sit in the hallway."

    if "emily" in freeroam9 and emily not in v12s7_killList:
        scene v12ferchr1c # FPP. show chris, Chris is holding his phone up trying to get a signal, looking up at phone, mouth closed
        with dissolve
    else:
        scene v12ferchrnoem1c
        with dissolve

    ch "I'm really not tryna move."

    if "emily" in freeroam9 and emily not in v12s7_killList:
        scene v12ferchr1b # FPP. show chris, Chris is holding his phone up trying to get a signal, looking up at phone, mouth closed
        with dissolve
    else:
        scene v12ferchrnoem1b
        with dissolve

    u "Those are the rules."

    if "emily" in freeroam9 and emily not in v12s7_killList:
        scene v12ferchr1c # FPP. show chris, Chris is holding his phone up trying to get a signal, looking up at phone, mouth closed
        with dissolve
    else:
        scene v12ferchrnoem1c
        with dissolve

    ch "*Sighs*"

    scene v12ferchr5 # FPP . show chris walking away
    with dissolve

    u "(He's having a hard time.)"

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_kitchen

label v12s7_mrlee:
    $ freeroam9.add("lee")

    scene v12ferlee1 # FPP. Show mr lee, neutral face, mouth closed
    #with dissolve

    u "Hello there, you fan of boxing? If so, did you catch my last fight?"

    stop music fadeout 3
    play music "music/v12/Track Scene 7_13.mp3" fadein 2

    scene v12ferlee1a # FPP. same 1, mouth open
    with dissolve

    lee "You can't talk to the Gamemaster."

    scene v12ferlee1
    with dissolve

    u "Who's that?"

    scene v12ferlee1a
    with dissolve

    lee "What? Me, obviously."

    scene v12ferlee1
    with dissolve

    u "Haha, I know, just teasing."

    scene v12ferlee2 # TPP. Show mc walking off
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_rear_gallery

label v12s7_josh1:
    $ freeroam9.add("josh")

    $ v12s7_seenList = []
    if (not v12s7_riley_moved or "riley2" in freeroam9) and riley not in v12s7_killList:
        $ v12s7_seenList.append(riley)
    if chloe not in v12s7_killList:
        $ v12s7_seenList.append(chloe)

    show screen murder_button_overlay(josh)

    scene v12ferjo1 # FPP. Show josh, slight smile, mouth closed
    #with dissolve

    u "What are you supposed to be?"

    stop music fadeout 3
    play music "music/v12/Track Scene 7_5.mp3" fadein 2

    scene v12ferjo1a # FPP. same 1, mouth open
    with dissolve

    jo "Boy, watch your tone when you talk to me, don't you know who you're talking to?"

    scene v12ferjo1
    with dissolve

    u "*Chuckles* No I don't, that's why I just asked."

    scene v12ferjo1a
    with dissolve

    jo "Boy, you're talking to the one and only Leopard Lord."

    scene v12ferjo1
    with dissolve

    u "What exactly is a Leopard Lord?"

    scene v12ferjo1a
    with dissolve

    jo "It's this kind of disrespect that the bitch Racheal Cracken almost got killed for. We all know she killed her man, probably fed him to the Leopards. Distasteful."

    scene v12ferjo1
    with dissolve

    u "Killing her husband or feeding him to the leopards?"

    scene v12ferjo1a
    with dissolve

    jo "No one cared about that wrinkly old man, it's a shame the leopards had to eat his crusty ass."

    menu:
        "Really care about cats, huh?":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            $ CharacterService.set_mood(josh, Moods.MAD)
            scene v12ferjo1
            with dissolve

            u "*Laughs* You really care about your cats, huh?"

            scene v12ferjo1b # FPP. Show josh, angry, mouth open
            with dissolve

            jo "Cats? CATS!!? Don't disrespect them like that! They are the pinnacle of all felines. The leopard is a dignified creature handcrafted by God. Also... *Whispers* Don't fucking laugh at me."

            scene v12ferjo1c # FPP. Show josh, angry, mouth closed
            with dissolve

            u "*Laughs* Have you seen yourself?"

        "You're the best actor here":
            $ reputation.add_point(RepComponent.BRO)
            scene v12ferjo1
            with dissolve

            u "Josh, you're definitely doing the best acting job out of everyone here. *Chuckles*"

            scene v12ferjo1a
            with dissolve

            jo "Don't disrespect me, you will address me correctly. I am the Leopard Lord."

            scene v12ferjo1
            with dissolve

            u "Getting pretty deep into this, huh?"

            scene v12ferjo1a
            with dissolve

            jo "Look, I have no idea what you're talking about, but once we arrive in Paris I'd be happy to take you to my Paris zoo location if you'd like to meet my Leopards."

            scene v12ferjo1
            with dissolve

            u "Umm yeah... I'll keep that in mind."

            scene v12ferjo1a
            with dissolve

            jo "You do that, there is no greater sight than that of the mighty leopard."

            scene v12ferjo1
            with dissolve

            u "Okayyy..."

            scene v12ferjo2 # FPP. Show mc walkign away.
            with dissolve
    
            pause 0.75
    
    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_right_viewpoint

label v12s7_josh2:
    $ freeroam9.add("josh2")
    $ v12s7_seenList = []

    show screen murder_button_overlay(josh)

    scene v12ferjos1 # FPP. Show josh, from a distance, mouth open
    #with dissolve

    jo "Hey you there mister?"

    stop music fadeout 3
    play music "music/v12/Track Scene 7_5.mp3" fadein 2

    scene v12ferjos2 # TPP. Show MC walking over to josh
    with dissolve

    pause 0.75

    if not v12s7_aubrey_moved:
        scene v12ferjos3 # FPP. Show josh(now infront of camera), mouth closed
        with dissolve
    else:
        scene v12ferjos3noau
        with dissolve
    
    u "Yes?"

    if not v12s7_aubrey_moved:
        scene v12ferjos3a # FPP. Same 3, mouth open
        with dissolve
    else:
        scene v12ferjos3anoau
        with dissolve

    jo "I have a little proposition."

    if not v12s7_aubrey_moved:
        scene v12ferjos3 # FPP. Show josh(now infront of camera), mouth closed
        with dissolve
    else:
        scene v12ferjos3noau
        with dissolve

    u "What is that?"

    if not v12s7_aubrey_moved:
        scene v12ferjos3a # FPP. Same 3, mouth open
        with dissolve
    else:
        scene v12ferjos3anoau
        with dissolve

    jo "How'd you like to own your very own leopard?"

    if not v12s7_aubrey_moved:
        scene v12ferjos3 # FPP. Show josh(now infront of camera), mouth closed
        with dissolve
    else:
        scene v12ferjos3noau
        with dissolve

    u "It's not something I've thought about."

    if not v12s7_aubrey_moved:
        scene v12ferjos3a # FPP. Same 3, mouth open
        with dissolve
    else:
        scene v12ferjos3anoau
        with dissolve

    jo "Well now's the time to start thinking. I have a magnificent baby boy leopard that needs the care of an individual home."

    if not v12s7_aubrey_moved:
        scene v12ferjos3 # FPP. Show josh(now infront of camera), mouth closed
        with dissolve
    else:
        scene v12ferjos3noau
        with dissolve

    u "Why can't he be with the rest?"

    if not v12s7_aubrey_moved:
        scene v12ferjos3a # FPP. Same 3, mouth open
        with dissolve
    else:
        scene v12ferjos3anoau
        with dissolve

    jo "Well you see, he was bullied by the nearby monkeys and they ripped off his tail."

    if not v12s7_aubrey_moved:
        scene v12ferjos3 # FPP. Show josh(now infront of camera), mouth closed
        with dissolve
    else:
        scene v12ferjos3noau
        with dissolve

    u "*Laughs* They ripped off your baby leopard's tail?"

    if not v12s7_aubrey_moved:
        scene v12ferjos3a # FPP. Same 3, mouth open
        with dissolve
    else:
        scene v12ferjos3anoau
        with dissolve

    jo "This ain't no laughing matter boy, the future king of leopard land is without a tail and this is how you behave. Shame on you, shame!"

    if not v12s7_aubrey_moved:
        scene v12ferjos3 # FPP. Show josh(now infront of camera), mouth closed
        with dissolve
    else:
        scene v12ferjos3noau
        with dissolve

    u "I didn't know it was that serious, sorry dude."

    if not v12s7_aubrey_moved:
        scene v12ferjos3a # FPP. Same 3, mouth open
        with dissolve
    else:
        scene v12ferjos3anoau
        with dissolve

    jo "You didn't know it was... who even are you? You are not the man I thought you to be. There's no way I'd dare let you care for the king of the land."

    if not v12s7_aubrey_moved:
        scene v12ferjos3 # FPP. Show josh(now infront of camera), mouth closed
        with dissolve
    else:
        scene v12ferjos3noau
        with dissolve

    u "Oh wow, that sucks... I really wanted to."

    if not v12s7_aubrey_moved:
        scene v12ferjos3a # FPP. Same 3, mouth open
        with dissolve
    else:
        scene v12ferjos3anoau
        with dissolve

    jo "Should've thought about that before you landed your insults. Good day sir."

    scene v12ferjos4 # FPP. Show josh walking away
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_utility

label v12s7_josh_kill:
    hide screen murder_button_overlay

    scene v12ferjos5 # TPP. Show mc pointing finger gun at josh, mc mouth open
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v12/Track Scene 7_7.mp3" fadein 2

    if not v12s7_aubrey_moved:
        scene v12ferjos3a # FPP. Same 3, mouth open
        with dissolve
    else:
        scene v12ferjos3anoau
        with dissolve
    jo "What? No, please don't kill me yet. I was having a lot of fun."

    if not v12s7_aubrey_moved:
        scene v12ferjos3 # FPP. Show josh(now infront of camera), mouth closed
        with dissolve
    else:
        scene v12ferjos3noau
        with dissolve

    u "Too much fun."

    if not v12s7_aubrey_moved:
        scene v12ferjos3a # FPP. Same 3, mouth open
        with dissolve
    else:
        scene v12ferjos3anoau
        with dissolve

    jo "I don't want to stop acting like Leopard Lord."

    if not v12s7_aubrey_moved:
        scene v12ferjos3b # FPp. same 3, new pose, mouth closed
        with dissolve
    else:
        scene v12ferjos3bnoau
        with dissolve

    u "Don't then, but act like him as a corpse in the hallway."

    if not v12s7_aubrey_moved:
        scene v12ferjos3c # FPP. Same 3b, mouth open
        with dissolve
    else:
        scene v12ferjos3cnoau
        with dissolve

    jo "*Sighs* Sounds like a plan."

    scene v12ferjos4
    with dissolve

    u "(Freaking goofball.)"

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_utility

label v12s7_emily1:
    $ freeroam9.add("emily")
    $ v12s7_seenList = [lauren]

    show screen murder_button_overlay(emily)

    scene v12ferem1 # FPP. Show emilty from a distance mouth open
    #with dissolve

    em "Hmmm, I can see it, when alone and solely alone the passengers will be swept away from the life they've always know."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_10.mp3" fadein 2

    scene v12ferem2 # TPP. Show mc walking closer to emily
    with dissolve

    pause 0.75

    scene v12ferem3 # FPP. Show emily, mouth closed
    with dissolve

    u "Talking to yourself?"

    scene v12ferem3a # FPP. Show emily, mouth open
    with dissolve

    em "I'm a psychic, I'm enjoying relaxing while talking to myself, NOT being bothered."

    scene v12ferem3
    with dissolve

    u "I got stuck as the boxer."

    scene v12ferem3a
    with dissolve

    em "I don't really care, but I just got a pretty clear vision of you walking away."

    scene v12ferem3
    with dissolve

    u "I can take a hint."

    scene v12ferem3a
    with dissolve

    em "Good."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_seating_back

label v12s7_emily2:
    $ freeroam9.add("emily2")
    $ v12s7_seenList = []

    show screen murder_button_overlay(emily)

    scene v12feremi1 # FPP. Show emily annoyed look, mouth closed
    #with dissolve

    u "Hey."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_5.mp3" fadein 2

    scene v12feremi1a # FPP. same 1, mouth open
    with dissolve

    em "Oh my gosh, can you stop using the game as an excuse to talk to me?"

    scene v12feremi1
    with dissolve

    u "I'm just trying to... *Sighs* Nevermind."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    $ v12s7_endtalkList.append(emily)
    call screen v12s7_bow

label v12s7_emily_kill:
    hide screen murder_button_overlay

    scene v12feremi3 # TPP. Show mc pointing finger gun at Emily, mc mouth open
    with dissolve

    u "Boom."

    stop music fadeout 3
    play music "music/v12/Track Scene 7_7.mp3" fadein 2

    scene v12feremi4 # FPP. Show emily, annoyed look, mouth open
    with dissolve

    em "Cool, I'm dead."

    scene v12feremi5 # FPP. Show emily walking away.
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v12/Track Scene 7_2.mp3" fadein 2

    call screen v12s7_bow

label v12s7_mc_caught:
    scene black
    hide screen murder_button_overlay
    
    stop music fadeout 3
    play music "music/v12/Track Scene 7_7.mp3" fadein 2

    if len(v12s7_killList) == 0:
        $ grant_achievement("weapons_down")

    unknown "I found the murderer!"

    stop music fadeout 3

    jump v12_murder_mystery_reveal