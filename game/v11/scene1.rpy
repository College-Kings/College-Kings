label v11_start:

    if path_builder and not pb_name_set:
        $ name = renpy.input(_("What's your name?"), default=name).strip() or _("Alex")
        $ pb_name_set = True

    scene v11coc1 # FPP. Show entrance of college
    with fade

    pause 0.75
    play music music.ck1.v11.Track_Scene_1_1 fadein 2
    scene v11coc1a # TPP. Same cam 1, MC now in shot running towards entrance
    with dissolve

    pause 0.75

    scene v11coc2 # TPP. Showing MC Outside door of meeting room
    with dissolve

    pause 0.75

    scene v11coc2a # TPP. Same cam 2, Show MC listening againt the meeting room door.
    with dissolve

    pause 0.75

    scene v11coc3 # TPP. Show Penelope, looking to her right at Jenny who is sat out of shot, nervous look, mouth open
    with dissolve

    pe "I'm super nervous, he promised he'd be here."

    scene v11coc4 # TPP. Show Jenny, looking to her left at Penelope who is out of shot, slight smile, mouth open
    with dissolve

    jen "We still have a few more minutes before we start, there's no reason to panic just yet."

    scene v11coc3
    with dissolve

    pe "He hasn't texted me back all morning, the odds of him showing up now are one in a million."
    stop music fadeout 3
    play music music.ck1.v11.Track_Scene_1_2 fadein 2
    scene v11coc5 # TPP. Show MC walking into the room (Camera behind MC, Penelope and Jenny in background, Penelope turned to look at MC)
    with dissolve

    pause 0.75

    scene v11coc6 # TPP. Show Penelope running towards MC
    with dissolve

    pause 0.75

    scene v11coc5a # TPP. Same cam 5, Show Penelope hugging MC. Penelope scared face
    with dissolve

    pause 0.75

    scene v11coc7 # FPP. Show MC looking at Penelope, she has a frown, mouth opened (Jenny sat at table behind Penelope, looking at MC)
    with dissolve

    pe "Where have you been?"

    scene v11coc7a # FPP. Same cam 7, Penelope frowned mouth closed
    with dissolve

    u "I'm sorry. Honestly, I woke up late, but I'm here now and ready to defend you."

    scene v11coc8 # FPP. Show Jenny looking at MC, slight smile, mouth open (Jenny is standing next to table, Penelope is standing next to MC, out of shot)
    with dissolve

    jen "It's about time. So what's the plan?"

    scene v11coc9 # FPP. Show Penelope looking at camera, nervous expression, mouth open (Same positioning as Cam 8, Jenny is out of shot)
    with dissolve

    pe "I honestly have no idea what we're doing. I watched a bunch of videos about this stuff, but it made me worry more than anything."

    scene v11coc9a # FPP. Same cam 9, Penelope slight smile, mouth closed
    with dissolve

    u "Don't worry, I got this."

    scene v11coc10 # TPP. Show the board walking through the door (Camera in front of the board, all of them with a serious look, slightly frowning)
    with dissolve

    pause 0.75

    scene v11coc11 # TPP. Show the board standing next to the chairs (Camera looking at the table with only the board in shot, neutral expressions)
    with dissolve

    pause 0.75

    scene v11coc11a # TPP. Same as cam 11. Show the board sat down
    with dissolve

    pause 0.75

    scene v11coc12 # TPP. Show Dean with mouth open, annoyed, looking at Penelope (MC is looking at the Dean)
    with dissolve

    de "Good morning, you may all take a seat. I can't help but notice we have two additional attendees today, would you mind explaining who they are and why they're here?"

    scene v11coc12a # TPP. Same as cam 12, Show Dean slightly less annoyed, mouth closed, looking at MC
    with dissolve

    u "I'm a close friend of Penelope and because of how serious the situation is, I'm here to represent her."

    scene v11coc13 # TPP. Show Jenny sat down, Jenny mouth open, looking at the board's direction, slightly nervous
    with dissolve

    jen "And I'm here as a character witness."

    scene v11coc14 # TPP. Show Lee with a neutral expression, mouth open, looking at Penelope
    with dissolve

    lee "Sounds appropriate, I find no fault."

    scene v11coc12
    with dissolve

    de "And you agree to this manner of representation, young lady?"

    scene v11coc15 # TPP. Show Penelope sat down mouth open, slightly nervous, looking at the board's direction
    with dissolve

    pe "Yes ma'am."

    scene v11coc12
    with dissolve

    de "So be it. Allow me to lay out the situation of this hearing."

    de "Miss Cross is being charged with interference in the application process in an effort to get her friend admitted into San Vallejo College."

    de "This was done by hacking into admissions and making necessary adjustments without any permission or legal access. Is this accurate, Miss Cross?"

    scene v11coc15
    with dissolve

    pe "Yes ma'am."

    scene v11coc12
    with dissolve

    de "Good, so with all that said, the position of the school is to establish a fine of $15,000 that is to be paid prior to the start of the next semester."

    de "Failure to do so, will result in you no longer being a student at San Vallejo College as well as possible legal prosecution."

    scene v11coc14
    with dissolve

    lee "However, no verdict is final until all parties have had the chance to fully explain themselves."

    scene v11coc12
    with dissolve

    de "Miss Cross, you have already admitted to being guilty of what you are accused of, so personally I see little here to debate and I expect this will be a very short hearing."

    scene v11coc14
    with dissolve

    lee "But in fairness, regardless of anyone's personal opinions, we'll stay as long as need be. The floor is yours."

    scene v11coc16 # TPP. Show MC and Penelope looking at each other, Penelope head slightly raised, with a very slight smile. MC is nervous
    with dissolve

    pause 0.5

    scene v11coc16a # TPP. Same as 16, Penelope head slightly lowered
    with dissolve

    pause 0.5

    scene v11coc16b # TPP. Same cam 16, MC and Penelope looking at the board, MC slight smile, mouth open, Penelope has a slight smile
    with dissolve

    u "Thank you."

    scene v11coc16c # TPP. Same as 16, MC is now standing
    with dissolve

    menu:
        "Speak about Penelope":
            $ v11s1_courtpoints += 1

            scene v11coc12b #FPP. Same as 12, but Dean, mouth closed, looking at MC
            with dissolve

            u "I don't wanna waste anyone's time, so let's start right away by talking about the person on trial, Penelope."

            scene v11coc12b
            with dissolve

            u "I remember the first time I met Penelope. As shy as she obviously was, she managed enough strength to approach me and introduce herself."

            u "When she did, I saw a sort of innocent kindness in her eyes. And-"

            scene v11coc12c # FPP. Same as 12b but Dean mouth open
            with dissolve

            de "We aren't here to talk about whatever you might be seeing in her facial features, young man. Please keep your anecdotes related to Ms. Cross' actions."

            scene v11coc12b
            with dissolve

            u "But that's exactly it. First impressions are actions. They're permanent marks we leave on other people. And the one Penelope leaves, is one of kindness and honesty."

            u "Aren't those the values you're trying to promote? Why punish someone for acting in line with the school's values?"

        "Introduce yourself":
            scene v11coc12b
            with dissolve

            u "Growing up I watched a lot of court shows so I already know what you guys are trying to do. I've seen this type of setup thousands of times."

            u "I may not be a real lawyer, but you won't win this case."

            scene v11coc12c
            with dissolve

            de "Are you here to tell us about yourself or Miss Cross?"

            scene v11coc12b
            with dissolve

            u "Penelope of course, but-"

            scene v11coc12c
            with dissolve

            de "Good, because we'd rather stick to the situation at hand than ramble about what we watched on cable television."

            scene v11coc12b
            with dissolve

            u "Sorry. I-"

    scene v11coc12c
    with dissolve

    de "San Vallejo College prides itself on our students' passion for helping each other. However that help has to be inside the boundaries of legality."

    de "Your friend disregarded those boundaries and ended up breaking the law which is unacceptable no matter the circumstances. Should we not punish those that commit crimes?"

    scene v11coc12b
    with dissolve

    menu:
        "Agree":
            scene v11coc12b
            with dissolve

            u "Yes, criminals should be punished, but-"

            scene v11coc12c
            with dissolve

            de "Miss Cross has already agreed that she committed a crime and you who are attempting to act as her representation say criminals should be punished."
            de "So by definition, Miss Cross should be punished."

            scene v11coc12b
            with dissolve

            u "Yes, but the punishment you have in mind is way too serious."

            scene v11coc12c
            with dissolve

            de "Serious crimes result in serious punishment."

        "Disagree":
            $ v11s1_courtpoints += 1

            scene v11coc12b
            with dissolve

            u "Boundaries may have been broken, but at what cost? Who was hurt in the process? No one."

            u "The intention, to help a fellow student, was pure and clearly without seeking any personal reward or benefit."

            u "When you care about someone, you end up doing whatever it takes to make them happy, even if it incriminates yourself."

            u "This was not a rebellious action intending to hurt the school, but rather a selfless act of kindness that we got to witness."

            u "Punishment would convey a message of the school's disregard for students' true intentions and would therefore not be true to SVC's values."

            u "Instead, using positive reinforcement by allowing Penelope's abilities, selflessness, and intelligence to flourish in an environment beneficial to the school would be more appropriate."

            scene v11coc12b
            with dissolve

            art "*Whisper* Damn this just got interesting."

            scene v11coc12b
            with dissolve

            u "What kind of school doesn't look to teach its students? Especially ones that are practically geniuses like Penelope."

            u "She's a contribution to this college, likely she could teach us all something."

            scene v11coc12c
            with dissolve

            de "Something about hacking?"

            scene v11coc14a # TPP. Same as 14, Mr Lee looking at the Dean
            with dissolve

            lee "Computer science is an incredibly useful field nowadays."

    scene v11coc12c
    with dissolve

    de "Another question, how long have you known Miss Cross and how often do you spend time with each other outside of class?"

    scene v11coc12b
    with dissolve

    menu :
        "Lie":
            scene v11coc12b
            with dissolve

            u "I've known Penelope for like three years now, we hang out all the time."

            scene v11coc12c
            with dissolve

            de "You met her when she was at an all girl's college?"

            scene v11coc12b
            with dissolve

            u "That's right. My sister and Penelope went to the same school."

            scene v11coc18 # FPP. MC is looking at Penelope, who is seated next to him, she is concerned and her mouth is slighlty open
            with dissolve

            pe "*Whisper* What are you doing?"

        "Truth":
            $ v11s1_courtpoints += 1

            scene v11coc12b
            with dissolve

            u "I met Penelope at the beginning of the semester right outside the cafe on Stevenson Street, since then we have seen each other a few times."

            scene v11coc12c
            with dissolve

            de "And you feel these few times are enough to fully understand her character?"

            scene v11coc12b
            with dissolve

            u "Anyone that spends even just a small amount of time with Penelope, could tell you how much of an amazing person she is."

            u "You may not believe my words, but my actions of coming here and doing everything I can to defend her should prove to you how much I think of her."

    scene v11coc12c
    with dissolve

    de "Regardless, when it comes to education, who we are on paper is what matters most."

    de "We may be different behind closed doors, but San Vallejo College can only judge what we show to the outside world. Do you agree?"

    scene v11coc12b
    with dissolve

    menu:
        "Agree":
            $ v11s1_courtpoints += 1

            scene v11coc12b
            with dissolve

            u "Yes, you're right. And on paper, outside of this one incident, Penelope is a honor roll student with several accolades to her name."

            u "She volunteers all the time and even the one blemish she has is just more proof of her care for others. So if on paper is what matters most, you should be agreeing with me."

            scene v11coc17 # TPP. Show Art Director, looking at Lee, mouth slightly open, slight smile, Mr Lee is looking back at her, mouth closed, neutral expression
            with dissolve

            art "*Whisper* Are we allowed to switch sides? That was a pretty good point."

            scene v11coc17a # TPP. Same cam as 17, Show Art Director, looking at Lee, mouth closed, slight smile, Mr Lee is looking back at her, mouth open, neutral expression
            with dissolve

            lee "*Whisper* Please, just sit there."

            scene v11coc12c
            with dissolve

            de "I can't help but say your point holds some weight to it."

        "Disagree":
            scene v11coc12b
            with dissolve

            u "I don't, there's so much stuff about people that is never shown on paper."

            scene v11coc12c
            with dissolve

            de "While that's true, what's on paper is what people decide to show the world. And your friend has shown she is willing to do whatever she must in order to get her way."

            de "Even if that's breaking the law."

    scene v11coc13
    with dissolve

    jen "May I say something?"

    scene v11coc17
    with dissolve

    art "*Whisper* Look at her, too bad she's a student."

    scene v11coc17a
    with dissolve

    lee "*Whisper* She's not a student, but regardless can you please pay attention. Your childish behavior may be funny to everyone else in the Professor's Lounge, but not here."

    scene v11coc17
    with dissolve

    art "*Whisper* Wait, she's not a student?"

    scene v11coc14
    with dissolve

    lee "*Sighs* Yes ma'am, please, go ahead."

    scene v11coc13
    with dissolve

    jen "Penelope is my friend, though I have to be honest, there's been a part of me that's always been a little jealous of her."

    scene v11coc19 # TPP. Penelope looking at Jenny, worried expression, mouth open, Jenny looking at the Board, mouth closed, slightly nervous
    with dissolve

    pe "Jenny?"

    scene v11coc12d # FPP. Same as 12, but Dean, slightly curious, mouth open, is looking at Jenny
    with dissolve

    de "How come?"

    scene v11coc13
    with dissolve

    jen "Penelope is sweet, a book whiz, and she's pretty. She could have the world if she wanted, but she never thinks about herself."

    jen "It's always \"I hope they're okay\" or \"I wanna help so and so with their studies''. I wish I was as good of a person as she is."

    jen "What makes it worse is that she did all of this because of me."

    scene v11coc12d
    with dissolve

    de "Elaborate."

    scene v11coc13
    with dissolve

    jen "I'm the one that wasn't smart enough to get into SVC on my own merit, so being the good person she is she tried getting me in."

    jen "She even kept it from me until recently, because she wanted me to think I did it on my own."

    scene v11coc12b
    with dissolve

    u "Wait."

    scene v11coc12b
    with dissolve

    menu:
        "Who hacked?":
            $ v11s1_courtpoints += 1

            scene v11coc12b
            with dissolve

            u "Dean, I assume since you've been so involved in this case you know all there is to know about it."

            scene v11coc12c
            with dissolve

            de "That's correct."

            scene v11coc12b
            with dissolve

            u "Good, I have a question then. What was used to hack the school?"

            scene v11coc12c
            with dissolve

            de "Well... a computer. Obviously."

            scene v11coc12b
            with dissolve

            u "Are you guessing or you know?"

            scene v11coc12c
            with dissolve

            de "I'm not certain of the equipment used to hack into the school, but based on evidence we traced and Miss Cross' own testimony we have proof that she did it. How she did it is irrelevant."

            scene v11coc12b
            with dissolve

            u "Is it though? What if she just asked someone in admissions to do it, what if it wasn't actually her that did the \"hacking\"?"

            u "Would that not make a difference if an employee of the school was the one actually changing the grade?"

            scene v11coc18a # FPP. Same as 18, but Penelope is tugging on MC
            with dissolve

            # -Penelope tugs on MC-

            pe "[name]..."

            scene v11coc12c
            with dissolve

            de "It would make a difference yes, she would be accused of encouraging misconduct which is far less of an accusation than where we currently stand."

            scene v11coc12b
            with dissolve

            u "So first you claim you know everything about the case, which we've proven is false. Now you say if other information was to be revealed, Penelope's punishment would be much less severe."

            scene v11coc12
            with dissolve

            de "Miss Cross, would you clear this up for us? How exactly did you manage to have the grades changed?"

            scene v11coc20 # TPP. Show Penelope halfway through getting up from her chair
            with dissolve

            pause 0.75

            scene v11coc20a # TPP. Same cam as 20, Penelope is standing up, looking at the Dean, very nervous, mouth open
            with dissolve

            pe "..."

            scene v11coc12
            with dissolve

            de "Miss Cross?"

            scene v11coc20a
            with dissolve

            pe "I... I'd rather not say."

            scene v11coc12
            with dissolve

            de "You understand that by choosing not to tell us we have no choice but to assume you did this on your own? Which makes you fully responsible."

            scene v11coc20a
            with dissolve

            pe "Yes ma'am, I understand."

            scene v11coc14
            with dissolve

            lee "One second there, Dean. Miss Cross, before I ask you this question you understand that lying can result in causing harm to your case, yes?"

            scene v11coc20b # TPP. Same as 20a, Penelope is looking at Mr Lee now
            with dissolve

            pe "Yes I do."

            scene v11coc14a
            with dissolve

            lee "Good. So my question is this, after hearing the words of your friends I am to believe you are a kind hearted person even at the risk of yourself."

            lee "Knowing how complicated the admission process is, unless you were simply a magician, I don't see how you could have done it without a school official's help."

            lee "I fear you are withholding who aided you in an attempt to protect them. Did someone within admission help you?"

            scene v11coc20c # TPP. Same cam as 20, Penelope looking down, mouth closed, nervous expression
            with dissolve

            pause 0.75

            scene v11coc14a
            with dissolve

            lee "My question was not who, but if anyone. I'm not asking you to identify who helped you, I just want to know if someone did."

            scene v11coc20d # TPP. Same as 20c, mouth open
            with dissolve

            pe "*Whisper* Yes."

            scene v11coc12
            with dissolve

            de "Please speak up so we may all hear you."

            scene v11coc20d
            with dissolve

            pe "Someone from admissions did help me."

            scene v11coc12
            with dissolve

            de "Who?"

            scene v11coc14a
            with dissolve

            lee "That's not necessary, the school's current investigation is concerning the role Miss Cross played."
            lee "We can look further into our own staff here at SVC if need be on another occasion."

        "Blame the school":
            scene v11coc12b
            with dissolve

            u "Isn't this just the school's fault if you really think about it? The school made their admissions system so simple that a student could hack into it."

            scene v11coc14c # TPP. Same as 14, Mr Lee looking at camera
            with dissolve

            lee "I personally know our admissions system is very complex, it would've taken a serious understanding of technology to hack our system."

            scene v11coc12c
            with dissolve

            de "The audacity to blame the school, the victim of the crime, is absurd and you should be ashamed."

            scene v11coc12b
            with dissolve

            u "I just feel like colleges should have better security."

            scene v11coc18a
            with dissolve

            pe "[name] please!"

    scene v11coc17b # TPP. Same cam as 17, Show Art director looking at Dean, mouth opened, neutral expression, Mr Lee is looking at him, mouth closed, slightly angry
    with dissolve

    art "I think we should speak with them privately, I'll take the blonde one and you guys decide who will take the other two."

    scene v11coc17c # TPP. Same cam as 17, Show Art Director looking at Lee, mouth closed, slight smirk, Mr Lee is looking back, mouth open, slightly angry
    with dissolve

    lee "Clayton, you are crossing a line of ethics at this point."

    scene v11coc12
    with dissolve

    de "Anyway, we've spent long enough on this as it is. Any last comments before we deliberate?"

    scene v11coc12b
    with dissolve

    menu:
        "Do what's right":
            scene v11coc12b
            with dissolve

            u "No further comments. I know you as the board will make the right decision."

        "I won":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            scene v11coc12b
            with dissolve

            u "It's pretty obvious we won so yeah, go deliberate."

    scene v11coc17d # TPP. Same cam as 17, Art Director is looking at MC, mouth open, neutral expression, Mr Lee is looking at MC, mouth closed, neutral expression
    with dissolve

    art "Bold..."

    stop music fadeout 3

    play music music.ck1.v11.Track_Scene_1_1 fadein 2

    scene v11coc21 # TPP. Show MC, Jenny and Penelope standing next to the chairs, neutral expressions, mouths closed
    with dissolve

    pause 0.75

    scene v11coc22 # TPP. Show MC, Jenny and Penelope leaving the room and entering the hallway, neutral expressions, mouths closed
    with dissolve

    pause 0.75

    scene v11coc23 # FPP. MC is looking at Jenny in the hallway, Jenny's mouth is open, nervous expression
    with dissolve

    jen "How do you think it'll go?"

    scene v11coc23a # FPP. Same as 23, Jenny's mouth is closed
    with dissolve

    u "I'm not sure, but I think we did good."

    scene v11coc24 # FPP. MC is looking at Penelope, she is about to be sick, mouth open
    with dissolve

    pe "I think I'm gonna be sick. Oh god..."

    scene v11coc24a # FPP. Same cam as 24, Penelope is turned away, and is running to the bathroom, still pretty close to MC
    with dissolve

    pause 0.75

    scene v11coc24b # FPP. Same as 24a, Penelope is almost out of view
    with dissolve

    pause 0.75

    scene v11coc23b # FPP. Same cam as 23, Jenny is pointing towards where Penelope went, worried expression, mouth open
    with dissolve

    jen "I'm gonna go check on her."

    scene v11coc23c # FPP. Same cam as 23, Jenny is running towards where Penelope was going
    with dissolve

    pause 0.75

    scene v11coc23d # FPP. Same cam as 23, Jenny is farther away
    with dissolve

    pause 0.75
    stop music fadeout 3

    play music music.ck1.v11.Track_Scene_1_4 fadein 2
    call screen v11s1_hallway1

label v11s1_riley:
    $ freeroam7.add("riley")

    if CharacterService.is_fwb(riley):
        scene v11cocri1 # FPP. MC and Riley looking at each other, Riley has mouth closed, neutral expression
        #with dissolve

        u "Hey, it's really cool to see that you came."
    else:
        scene v11cocri1 # FPP. MC and Riley looking at each other, Riley has mouth closed, neutral expression
        #with dissolve

        u "You came?"

    if CharacterService.is_fwb(riley):
        scene v11cocri1a # FPP. Same as ri1, Riley has mouth open, same expression
        with dissolve

        ri "Yeah, of course. I mentioned before that I wanted to support both of you. I've been here a while but I didn't want to walk in half way through."

    else:
        scene v11cocri1a # FPP. Same as ri1, Riley has mouth open, same expression
        with dissolve

        ri "Yeah, you guys had already started before I got here so I didn't wanna walk in. It sounded pretty heated, how did it go?"

    scene v11cocri1
    with dissolve

    menu:
        "It went well":
            scene v11cocri1
            with dissolve

            u "They're in deliberation right now, but I think we had a pretty good case."

            scene v11cocri1a
            with dissolve

            ri "I'm glad you're optimistic, I'm sure Penelope appreciates it."

        "I'm not sure":
            scene v11cocri1
            with dissolve

            u "The dean was pretty harsh, so I'm not sure how this'll go."

            scene v11cocri1a
            with dissolve

            ri "I'm sorry... Do your best to stay positive, Penelope needs all the support she can get at the moment."

            if CharacterService.is_fwb(riley):
                ri "It's really sweet of you to be so supportive of your friends."

    scene v11cocri1a
    with dissolve

    ri "So, how's Penelope? I saw her run to the restroom."

    scene v11cocri1
    with dissolve

    u "She said she was feeling sick. It didn't help that I got here late either. If it was me I'm not sure I'd be able to keep it together as well as she has."

    scene v11cocri1a
    with dissolve

    ri "It's probably hard for her to be optimistic at the moment."

    scene v11cocri1
    with dissolve

    u "Well, she didn't talk much in there to be fair. I think it's all too real. She's just now getting hit with the realization that this could have serious consequences."

    scene v11cocri1a
    with dissolve

    ri "I really wish there was something more I could do for her. It's a really bad situation, after all she only did this to help a friend in need."

    scene v11cocri1
    with dissolve

    u "I guess it's just one of those tough ethical dilemmas that you hear about in class. We should have a verdict here soon."

    scene v11cocri1a
    with dissolve

    ri "Well, you know I'm here for you both regardless. I'm gonna go check on Penelope and see if there's anything I can do to help settle her nerves."


    if CharacterService.is_fwb(riley):
        scene v11cocri1
        with dissolve

        u "Sounds good, it's really sweet of you to care so much."

    else:
        scene v11cocri1
        with dissolve

        u "Sounds good."

    scene v11cocri1b # FPP. Same cam as 28, show Riley walking away
    with dissolve

    pause 0.75

    call screen v11s1_hallway1

label v11s1_mrrose:
    if not "mr rose" in freeroam7:
        $ freeroam7.add("mr rose")

        if joinwolves:
            scene v11cocmrr1a # FPP. Same as mrr1, but Mr Rose mouth closed
            with dissolve

            u "Mr. Rose? What are you doing here?"

            scene v11cocmrr1 # FPP. MC and Mr Rose looking at each other, Mr Rose has a neutral expression, mouth open
            with dissolve

            mrr "Just enjoying the show."

            scene v11cocmrr1a
            with dissolve

            u "My friend getting scolded by a biased school board? Yeah, great show..."

            scene v11cocmrr1
            with dissolve

            mrr "Listen, [name]."
            mrr "I know we started off on a wrong foot, but I think your friend would be quite glad to know I'm here."

            scene v11cocmrr1a
            with dissolve

            u "Oh yeah? Why is that?"

            scene v11cocmrr1
            with dissolve

            mrr "Because I have connections champ. It's always better to have someone like me on your side."

            scene v11cocmrr1a
            with dissolve

            u "If you were really on our side you'd be in there helping her."

            scene v11cocmrr1
            with dissolve

            mrr "If you really believe you can help her from in there, you're a fool. The real game is played out here."

            scene v11cocmrr1a
            with dissolve

            u "Whatever man, at least I'm actually doing something. Now, if you'll excuse me I have a friend to fight for."

        else:

            scene v11cocmrr1
            #with dissolve

            mrr "[name], right?"

            scene v11cocmrr1a
            with dissolve

            u "Uhh, yeah..."
            u "Do I know you?"

            scene v11cocmrr1
            with dissolve

            mrr "No, you don't."

            scene v11cocmrr1a
            with dissolve

            u "Okayyy..."

        call screen v11s1_hallway2

    # -Back to free roam-

    ### ERROR: -If talk to Jenny ###

label v11s1_jenny:
    $ freeroam7.add("jenny")

    scene v11cocjen1 # FPP. MC and Jenny looking at each other, Jenny has a worried expression, mouth closed
    #with dissolve

    u "How is she?"

    scene v11cocjen1a # FPP. Same as jen1, but mouth open
    with dissolve

    jen "Not too good, she's really worried. I hope what we did in there helps out."

    scene v11cocjen1
    with dissolve

    u "I do too, that damn dean wouldn't let up. It stopped feeling like a hearing and more like a personal attack about half way through."

    scene v11cocjen1a
    with dissolve

    jen "The situation was already bad enough, but with how much she attacked Penelope it really makes me feel even worse for my part in this."

    scene v11cocjen1
    with dissolve

    u "Mr. Lee was being very fair and understanding though."

    scene v11cocjen1a
    with dissolve

    jen "I don't even know why that other guy is here."

    scene v11cocjen1
    with dissolve

    u "The Art Director?"

    scene v11cocjen1a
    with dissolve

    jen "I guess that's who that was, he was making me feel really uncomfortable. I heard him say some really weird stuff."

    scene v11cocjen1
    with dissolve

    u "Like what?"

    scene v11cocjen1a
    with dissolve

    jen "Something about getting me alone. It sent chills down my back, I almost felt like I was going to be sick."

    scene v11cocjen1
    with dissolve

    u "Yeah, that man is an actual creep. You should probably stay as far away from him as possible."

    scene v11cocjen1a
    with dissolve

    jen "I still can't help but feel this is all my fault."

    scene v11cocjen1
    with dissolve

    u "Beating up on yourself isn't going to help, what Penelope needs now is our support. All we can do is be there for her."

    scene v11cocjen1a
    with dissolve

    jen "Thanks, you're right. I'm going to take a minute to breathe and grab some water before they call us back in."

    call screen v11s1_hallway1

label v11s1_delib:
    if not "delib" in freeroam7:
        $ freeroam7.add("delib")

        scene v11coc77c
        #with dissolve

        lee "You should never have been a member of this board."

        scene v11coc77a
        with dissolve

        art "She's an adult, I don't see the issue here."

        scene v11coc77c
        with dissolve
        lee "You... you are the issue here Clayton. I do my best to keep a cool tone, but you're aggravating me."

        scene v11coc77e # TPP. Same cam as 17, Dean is looking at Art Director, mouth open, neutral expression, Art Director mouth closed, annoyed
        with dissolve

        de "Calm down Bruce, it's nearly time to wrap this up. Clayton, let the kids know we've made a decision."

        scene v11coc77f # TPP. Same cam as 17, Art Director is looking at Dean mouth open, angry, Dean is neutral, mouth closed
        with dissolve

        art "I'M NOT A SLAVE, I'M-"

        scene v11coc77g # TPP. Same cam as 17, everyone mouth closed, Dean is neutral, Art Director is annoyed
        with dissolve

        de "..."

        scene v11coc77b
        with dissolve

        art "...OK"

        call screen v11s1_hallway1

        # -Back to free roam-

label v11_case_verdict:
    scene v11coc22a # TPP. Same as cam 22, MC, Jenny and Penelope walking back in the room, nervous expression, mouth closed
    #with dissolve

    pause 0.75

    scene v11coc21
    with dissolve

    pause 0.75

    scene v11coc12
    with dissolve

    de "Please have a seat."
    stop music fadeout 3

    if v11s1_courtpoints >= 4:
        play music music.ck1.v11.Track_Scene_1_5 fadein 2
        $ v11_pen_goes_europe = True
        scene v11coc14b # TPP. Same as 14, Mr Lee looking at Penelope
        with dissolve

        lee "Based on testimony, it's clear that you are a loyal and caring friend. Sadly, in this case your loyalty resulted in a poor decision."

        lee "We must make it clear that this is a civil case at this point, charges will not be pressed unless you choose not to comply with the school's agreed upon discipline."

        scene v11coc14
        with dissolve

        lee "We acknowledge your great academic standing and the benefit you've been to this school, we feel to disregard that is in poor taste. However, we can't simply let you go for being a good student."

        lee "As always preferred, the board has decided to go with a more creative and case based discipline tailored to the events that have occurred."

        scene v11coc14b
        with dissolve

        lee "As punishment for the actions taken, you will be subject to attend this year's abroad trip to Europe. While attending, you will serve as an Assistant Chaperone and help with all the chaperones may need."

        lee "Alongside that, you will be volunteering with a university research company."
        lee "They're in great need of computer-inclined individuals such as yourself for the remainder of your time here at the college. Do you agree?"

        scene v11coc15a # TPP. Same as 15, but Penelope is shocked, mouth open
        with dissolve

        pe "Yes, wow. Thank you so much."

        scene v11coc14b
        with dissolve

        $ grant_achievement("perry_mason")
        lee "Don't thank us, thank your friend. He did a very good job representing you. We may just have a future lawyer in our midst."

        scene v11coc14c
        with dissolve

        u "Thank you, Mr. Lee."

        scene v11coc12
        with dissolve

        de "Since Mr. Lee is a primary chaperone on this trip he will oversee everything from here."

        de "The school considers this matter closed. If you'll excuse me I have some important things to attend to. You may leave."

        scene v11coc22
        with dissolve

        pause 0.75

        scene v11coc23e # FPP. Same as 23, Jenny is happy, mouth open
        with dissolve

        jen "What just happened?"

        scene v11coc24c # FPP. Same as 24, but Penelope's mouth is closed, she is very happy
        with dissolve

        u "Haha, we won. That's what happened."

        scene v11coc23f # FPP. Same as 23a, Jenny is happy, mouth closed
        with dissolve

        jen "This is amazing!"

        scene v11coc24c # FPP. Same as 24, but Penelope's mouth is closed, she is very happy
        with dissolve

        u "Feeling better now Penelope?"

        scene v11coc24d # FPP. Same as 24, Penelope is looking down
        with dissolve

        u "You okay?"

        scene v11coc25 # TPP. In hallway, Penelope is tightly hugging MC, Penelope is happy, mouth slightly open
        with dissolve

        pe "*Whisper* Thank you."

        scene v11coc25a # TPP. Same as 25, but Penelope's mouth is closed
        with dissolve

        u "*Whisper* You're welcome."

        if CharacterService.is_dating(penelope) or bowling or hcGirl == "penelope":
            scene v11coc24e # FPP. Same as 24c, but Penelope's mouth is open
            with dissolve

            pe "No I mean it, thank you. You have no idea how much this means to me. When I got that letter from the school I thought my life was ruined. I don't know what I would have done without you."

        else:
            scene v11coc24e # FPP. Same as 24c, but Penelope's mouth is open
            with dissolve

            pe "No I mean it, thank you."
            
        scene v11coc24c
        with dissolve

        u "Hey it's about time someone does something for you."

        scene v11coc23e
        with dissolve

        jen "Who knows, maybe this trip will still be a lot of fun."
        jen "[name] will make sure you still have a good time on the trip. Won't you, [name]?"

        scene v11coc26 # FPP. Penelope and Jenny are hugging
        with dissolve

        pause 0.75

        scene v11coc24c
        with dissolve

        u "You know it."

        scene v11coc23e
        with dissolve

        jen "I'm glad it ended in our favor, I'm sorry this all got so out of hand."

        scene v11coc23f
        with dissolve

        u "Ok guys. This has been stressful enough for all of us, let's put it in the past and make the most out of this year. Maybe we can all get together soon and do something a little less stressful."

        scene v11coc23e
        with dissolve

        jen "I'd like that. Anyways I have to run so I'll see you both soon."

        scene v11coc24e
        with dissolve

        pe "I have to get going as well, thankfully I still have a class to get to."

        if CharacterService.is_dating(penelope) or bowling or hcGirl == "penelope":
            scene v11coc25b # TPP. Same cam as 25, but Penelope is kissing MC on the cheek
            with dissolve

            play sound sound.kiss

            scene v11coc24e
            with dissolve

            pe "Really [name], I can't thank you enough for all you've done."

        else:
            scene v11coc24e
            with dissolve

            pe "Thanks again, bye."
            
    else:
        $ v11_pen_goes_europe = False
        play music music.ck1.v11.Track_Scene_1_1 fadein 2
        scene v11coc12
        with dissolve

        de "Despite the testimony of your friends, the decision of the board has not changed in the slightest."
        de "For your actions committed, a fine in the amount of $15,000 will be owed prior to you continuing as a student next semester. Do you understand these terms?"

        scene v11coc15a
        with dissolve

        pe "Yes, I understand. I'd also like to take this chance to apologize once again. I know what I did was stupid and I don't plan on repeating my mistakes."

        scene v11coc12
        with dissolve

        de "The school considers this matter closed so if you'll excuse me I have some important things to attend to. You may leave."

        scene v11coc22
        with dissolve

        pause 0.75

        scene v11coc23
        with dissolve

        jen "What just happened?"

        scene v11coc23a
        with dissolve

        u "We lost. I'm so sorry."

        scene v11coc24f # FPP. Same as 24, but Penelope is crying, mouth open
        with dissolve

        pe "I'm sorry guys, I have to go."

        scene v11coc24a
        with dissolve

        pause 0.75

        scene v11coc24b
        with dissolve

        pause 0.75

        scene v11coc23b
        with dissolve

        jen "I better run after her."

        scene v11coc23c
        with dissolve

        pause 0.75

        scene v11coc23d
        with dissolve

        pause 0.75

    scene v11coc27 # TPP. Third person view of MC, he is alone and has a tired expression, mouth closed, in the hallway
    with dissolve

    $ v11s1_kiwiiPost = KiwiiPost(autumn, "phone/kiwii/Posts/v11/v11_autumn_kiwii.webp", _("Best charity event yet, thanks for all the donations!"), number_likes=556)
    $ v11s1_kiwiiPost.newComment(aubrey, _("So psyched!"), number_likes=renpy.random.randint(200, 500))
    $ v11s1_kiwiiPost.newComment(cameron, _("What you doing later? ;)"), number_likes=renpy.random.randint(200, 500))
    $ v11s1_kiwiiPost.newComment(lindsey, _("It was an awesome day!"), number_likes=renpy.random.randint(200, 500))
    $ v11s1_kiwiiPost.addReply(_("Wish I could see more mud wrestling!"), number_likes=321)
    $ v11s1_kiwiiPost.addReply(_("Thanks for doing the event Autumn!"), number_likes=518)

    u "(Wow, what a way to start my day. *Phew* Let's see who's going to Europe.)"
    stop music fadeout 3
    jump v11_nora_chloe_hallway

    # -Transition to Scene 2-
