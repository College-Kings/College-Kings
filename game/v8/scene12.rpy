# Locations: MC's dorm (only one render), Apes house main room and the den, College surroundings for statue scene
# MC's outfit: Nice suit, but not over the top. But should strike different from casual wear
# Everyone else's outfits: Casual wear for pledges (Kai, Caleb, Cooper, Ryan) and Apes in their jackets
# Time: Saturday afternoon (Immediate continuation of Apes branching in scene 9)

### SCENE 12: APES CEREMONY
label apes_join_ceremony:

    scene v8apes1 # TPP. MC in his new outfit looking at himself in the mirror in his dorm with a confident smile, mouth closed
    with fade
    u "(Looking good there, [name].)"

    play music "music/mindie1.mp3" fadein 2
    queue music ["music/m15punk.mp3", "music/m2punk.mp3"]

    if "v8_riley" in sceneList:
        u "(I hope I run into Riley tonight. Last night was great.)"
    elif ending == "riley":
        u "(I hope I run into Riley tonight. She had me intrigued with that secret.)"
    elif ending == "chloe":
        u "(Could be fun if I run into Chloe tonight. If only that girl hadn't interrupted at the perfect moment *sigh*)"
    elif ending == "lauren":
        u "(I hope I run into Lauren tonight. Could always spend my nights cuddling with that cutie.)"
    else:
        u "(I hope I run into Amber tonight. Last night was fun. A bit weird but fun nonetheless.)"

    scene v8apes2 # TPP. Shot of MC entering Apes house, nobody else in the shot
    with Fade(0.75, 0.25, 0.75)
    pause 0.5

    scene v8apes3 # FPP. MC inside Apes main hall. Caleb, Ryan, Kai visible in shot talking to each other (all in casual clothes). MC not too close to them
    with dissolve
    u "(What the hell? Maybe I have time to change into something casual.)"

    scene v8apes3a # Now they're looking at MC and laughing. Kai and Ryan talking. Kai pointing at the MC
    with dissolve
    kai "Shit man, is this fucker going to prom or what?"
    ry "Damn, [name], did your mommy pick that out for you?"

    scene v8apes4 # TPP. Shot of Cameron (in the same room but not close to the three pledges) looking towards the MC (not visible in shot), laughing and talking. Nobody else in shot
    with dissolve
    ca "Did you really-"

    scene v8apes5 # TPP. Shot of Grayson entering from a door while talking, nobody else need to be in the shot
    with dissolve
    gr "Alright, alright, let's get this party started. Gather around."

    scene v8apes6 # FPP. Grayson laughing and talking looking slightly to his left and not into the camera. Others need not be visible. (For context, all the pledges lined up in front of Grayson. From Grayson's POV, it's Kai, Ryan, MC, Caleb, Cooper from left to right. Please read through the scene and give suitable positions for Sam and Mason)
    with fade
    gr "As you all know, only three pledges can make it into the Apes."
    gr "You were judged on how well you performed your challenges with your coaches."

    scene v8apes6a # Grayson laughing and talking different pose, looking towards his right this time (slightly off from the camera)
    with dissolve
    gr "Caleb, which was your favorite challenge?"

    scene v8apes7 # TPP. Close up shot of Caleb laughing and talking
    with dissolve
    cal "Gotta be the look on Mr. Brooke's face when he realized his pants were down around his ankles."
    "*laughs*"

    scene v8apes6a
    with dissolve
    gr "Ah, man, I'm so glad we got that on camera!"

    scene v8apes6
    with dissolve
    gr "Ryan, how about you?"

    scene v8apes8 # TPP. Close up shot of Ryan laughing and talking
    with dissolve
    ry "Totally the girls locker room. I saw so many tits that day!"

    scene v8apes6
    with dissolve
    gr "Dude... I think you got the most of anyone! Great work. You'll be a great Ape... maybe."

    scene v8apes6a
    with dissolve
    gr "I gotta say, it might be less flashy, but I loved watching the chaos you pledges created gluing the doors."

    scene v8apes6
    with dissolve
    gr "I didn't have to go to Math for two fucking days!"

    scene v8apes6b # Grayson serious and talking, looking towards his right (slightly off from the camera)
    with dissolve
    gr "NOW! Down to business."
    gr "Who has what it takes to be one of us?"

    if apesVids == 4:
        u "(Why is he avoiding looking at me? He did not ask me anything either.)"
    else:
        u "(Man, Grayson didn't ask me anything. Or even look at me. This can't be good.)"

    scene v8apes6c # Grayson serious and talking, looking towards his left (slightly off from the camera)
    with dissolve
    gr "Who's gonna be a Great Ape and who's gonna walk away a Chumpy Chimp?"

    scene v8apes6b
    with dissolve
    gr "Let's find out who the worthy ones are."

    if apesVids == 4:
        scene v8apes6c
        with dissolve
        gr "I had great expectations from this pledge but I haven't seen a perfect score in a while."

        scene v8apes6
        with dissolve
        gr "The exceptional performer who did everything told without question, and our first Ape is..."

        scene v8apes6d # Grayson looking into the camera and talking, proud and smiling
        with dissolve
        gr "...[name]! Well fucking done my man!"

        scene v8apes10 # TPP. Shot of Mason and Sam clapping and cheering, mouths half-open (meaning should work for both talking and non-talking)
        with dissolve
        sam "Woah! Hell yeeahhh!"
        u "(Holy shit! I did it. I'm in! And first in that!)"
        ma "Nicely done, [name]!"

        scene v8apes9 # TPP. Shot of Cameron somewhere in the room (ideally just standing against a wall with his hands folded and one leg against the wall), smiling, proud and looking towards the MC (not visible in shot), mouth closed. Not a close up shot
        with dissolve
        pause

        scene v8apes6
        with dissolve
        gr "And right under [name], our number two spot is Ryan!"

        scene v8apes8a
        with dissolve
        ry "Woohoo!!!"

        scene v8apes6a
        with dissolve
        gr "And our last spot goes to... Caleb!"

        scene v8apes10
        with dissolve
        ma "Congrats Ryan and Caleb!"

        jump after_apes_ranking

    elif apesVids >= 2:
        scene v8apes6
        with dissolve
        gr "Let's go ahead and put Ryan out of his misery. Congrats man, you're first. Way to go!"

        scene v8apes8a # TPP. Close up shot of Ryan very excited, smiling wide
        with dissolve
        ry "Woohoo!!!"

        scene v8apes10
        with dissolve
        sam "Hah! Of course he did great. This guy was planning to join us even before coming to San Vallejo."

        scene v8apes6
        with dissolve
        gr "Second place, with a close call, is..."

        scene v8apes6d
        with dissolve
        gr "...my man [name]! You're in!"

        scene v8apes10
        with dissolve
        ma "Well done, champ!"
        u "(Wow, I made it in!)"

        scene v8apes9
        with dissolve
        pause

        scene v8apes6a
        with dissolve
        gr "And our last spot goes to... Caleb!"

        scene v8apes10
        with dissolve
        sam "Welcome to the Apes, Caleb!"

        jump after_apes_ranking

    elif apesVids == 1:
        scene v8apes6
        with dissolve
        gr "Let's go ahead and put Ryan out of his misery. Congrats man, you're first. Way to go!"

        scene v8apes8a
        with dissolve
        ry "Woohoo!!!"

        scene v8apes10
        with dissolve
        sam "Hah! Of course he did great. This guy was planning to join us even before coming to San Vallejo."

        scene v8apes6a
        with dissolve
        gr "Next Ape with an impressive score is gonna be..."
        gr "Caleb!"

        scene v8apes10
        with dissolve
        ma "Cheers Cal! I knew you had in you my dude!"
        u "(Aw man, one spot left.)"

        scene v8apes9a # Same as v8apes9 but Cameron serious with a tinge of anger
        with dissolve
        pause

        scene v8apes6b
        with dissolve
        gr "Our final spot goes to..."

        scene v8apes6d
        with dissolve
        gr "...[name]!"

        scene v8apes10
        with dissolve
        sam "Congrats my dude!"
        u "(Phew, that was close.)"

        jump after_apes_ranking

    else:
        scene v8apes6
        with dissolve
        gr "Let's go ahead and put Ryan out of his misery. Congrats man, you're first. Way to go my man!"

        scene v8apes8a
        with dissolve
        ry "Woohoo!!!"

        scene v8apes10
        with dissolve
        sam "Hah! Of course he did great. This guy was planning to join us even before coming to San Vallejo."

        scene v8apes6a
        with dissolve
        gr "Next Ape with an impressive score is gonna be..."
        gr "Caleb!"

        scene v8apes10
        with dissolve
        ma "Cheers Cal! I knew you had in you my dude!"
        u "(Aw man, one spot left.)"

        scene v8apes9a
        with dissolve
        pause

        scene v8apes6c
        with dissolve
        gr "Alright now, fellas, hold up here. We have a situation, an unusual one."

        scene v8apes6b
        with dissolve
        gr "Kai, Cooper and [name]..."
        u "(Fuck!)"
        gr "...didn't do any of the tasks they were told to do."

        scene v8apes6c
        with dissolve
        gr "Why, I don't care. But I see potential and need one of you in."
        gr "So, to remedy this situation, we're gonna have a face-off."
        u "(Oh man, do I have to fight now?)"

        scene v8apes6b
        with dissolve
        gr "Cameron, tell these three chimp-boys what they're doing."

        scene v8apes9b # Cameron starts walking towards the pledges with a serious face, mouth closed
        with dissolve
        gr "Let's get this shit over with so we can drink!"

        jump apes_faceoff_task

label apes_faceoff_task:
    scene v8apes11 # FPP. (For context: MC, Cooper and Kai gather around Cameron). Cameron talking with a serious face while looking into the camera. Others need not be visible in the shot
    with dissolve
    ca "Ok pukes. Now pay some fucking attention."

    scene v8apes11a # Same as v8apes11 but looking not into the camera
    with dissolve
    ca "For your face-off challenge, you must do something ridiculous on campus without alerting security."
    ca "I don't care what you do, just don't let it come back to us, or I'll kick all your sorry asses!"

    scene v8apes11
    with dissolve
    ca "Get video of whatever you do and send it to me. We'll then review it with interest."

    scene v8apes11a
    with dissolve
    ca "You have 3 hours now. So, hurry the fuck up!"

    scene v8apes12 # FPP. (For context: Cameron left now) Kai and Cooper nervous and looking at each other
    with dissolve
    pause

    menu:
        "Wish them good luck":
            $ reputation.add_point(Reputations.BRO)

            u "Good luck, guys!"

            scene v8apes12a # Kai and Cooper nervous, both looking at the camera and talking
            with dissolve
            kai "Thanks brother! To you too."
            coop "Let the best man win."

        "Just get to the task":
            $ reputation.add_point(Reputations.TROUBLEMAKER)

    scene black
    with dissolve
    u "(I gotta make sure I do something they'll be satisfied with now.)"
    u "(Otherwise I'm not making the cut and I don't wanna stay in that dorm forever.)"

    scene v8apes13 # TPP. MC walking towards the statue in front of the college or someplace else. Maybe like the founder's statue. He has a giant dildo in his hand. (This is continuation of v8apes12, so time and costumes need to be consistent)
    with Fade(0, 0.25, 0.75)
    u "(There's nobody around. This is the perfect moment.)"

    scene v8apes14 # TPP. MC taping the giant dildo to the head of the statue, mouth closed and silly smile
    with dissolve
    u "(I don't know whose statue this is and this is so wrong...)"

    scene v8apes15 # FPP. MC looking at the upper half part of the statue. Make it look funny
    with dissolve
    u "(...but that guy looks so stupid now hahaha. No way these guys are gonna beat me.)"
    u "(I gotta record and get away from soon here. Don't wanna risk anybody spotting me.)"

    scene v8apes6e # Grayson looking at his phone with a silly smile
    with Fade(0.75, 0.25, 0.75)
    pause

    scene v8apes6b
    with dissolve
    gr "So. Your 3 hours are up and here you all are. I was sure one of you wasn't gonna show."

    scene v8apes6c
    with dissolve
    gr "Guess you guys proved me wrong after all. At least that's not a disappointment."

    scene v8apes6a
    with dissolve
    gr "Cooper. Not bad! Bananas in the tailpipe of 3 security cars."
    gr "One of them couldn't even start for more than an hour, the way I heard it."

    scene v8apes6
    with dissolve
    gr "Kai. Not bad as well, sneaking into the cafeteria and adding Ex Lax to the beef stew."
    gr "Campus bathrooms are gonna be busy today!"

    scene v8apes6d
    with dissolve
    gr "Now there's you. [name]."
    gr "Taping a giant dildo to the school's statue without being caught is ballsy and absolutely hilarious! Good job, my man!"

    scene v8apes6
    with dissolve
    gr "I know I made up my mind. What about you Cam?"

    scene v8apes16 # TPP. Close up shot of Cameron (somewhere in the room) looking towards Grayson (not visible in shot) and talking seriously
    with dissolve
    ca "I know you know who I picked."

    scene v8apes6b
    with dissolve
    gr "Right. All of you did a good job, but for this challenge, the clear winner is..."

    scene v8apes6d
    with dissolve
    gr "...[name]!"
    u "*Sigh* (Finally.)"

    scene v8apes12a
    with dissolve
    kai "Congrats man!"
    coop "That was ballsy dude, well done."
    u "Thanks guys!"

    scene v8apes12
    with dissolve
    pause 0.5

    scene v8apes11a
    with dissolve
    ca "You both still in here? Beat it!"
    jump after_apes_ranking

label after_apes_ranking:
    scene v8apes6
    with fade
    gr "Apes, please escort the two losers out of the house."

    scene v8apes17 # TPP. Mason taking Kai out of the room, grabbing him by the arm (as if by force). Kai looking disappointed
    with dissolve
    pause 0.5
    if apesVids <= 1:
        u "(Whew, glad I made it in somehow. Last thing I need right now is Cameron kicking me out of here.)"

    scene v8apes17a # Sam taking Cooper out of the room, grabbing him by the arm (as if by force). Cooper looking disappointed
    with fade
    pause 0.5
    gr "While they're at it, others follow me to the den. We have a party to start!"

    scene v8apes18 # New location from now on - a room in Apes house called "The Den". TPP. Shot of Grayson cheersing with a beer bottle in hand and talking, happy. (For context, MC, Ryan, Caleb, Grayson and Cameron are in the location. They're all just drinking and chilling on sofas. Cameron sits beside the MC. Position others suitably.)
    with Fade(0.75, 0.2, 0.5)
    gr "Congrats Apes! I'm glad with the picks this year."
    gr "Look forward to the training and fights. We're gonna make beasts out of you guys."

    scene v8apes19 # TPP. Ryan and Caleb with beer bottles in hand, cheersing and talking
    with dissolve
    ry "Hell yeah!"
    cal "Cheers! I'm gonna make us proud!"

    if apesVids <= 1:
        scene v8apes20 # TPP. Cameron leaning in to whisper something to the MC. Mouth half-open, serious expression and slight aggression. (Both of them holding beers too.)
        with dissolve
        ca "Mason and Sam are gonna waste their whole night consoling those two losers. That's not really my thing."
        ca "You're lucky you made it. I don't know what I would've done to you if you made me lose."

        scene v8apes20a # Same as v8apes20 but MC talking (neutral expression) and Cameron mouth closed, neutral expression
        with dissolve
        u "Relax man. Can we be civil and try to get along? We're family now."

        scene v8apes20b # Cameron stands up and starts walking away. MC looks at him. Cameron's face is out of the shot (above the screen)
        with dissolve
        ca "Let's see about that."

    else:
        scene v8apes20c # Same as v8apes20, but Cameron happy and talking
        with dissolve
        ca "Well done, man. I really didn't want you crying on my shoulder like the other two losers are doing."
        ca "And if you lost, that means I lost as a coach as well. And I hate losing."

        scene v8apes20a
        with dissolve
        u "Heh. Glad to have made it in. I don't know how I'd have reacted if I lost either."

        play sound "sounds/toast.mp3"

        scene v8apes20d # Cameron and MC cheers toasting their beers. Cameron talking
        with Dissolve(0.3)
        ca "Cheers to winning, my man!"

    scene black
    with Dissolve(1.25)
    pause 0.5

    jump after_apes_ceremony
