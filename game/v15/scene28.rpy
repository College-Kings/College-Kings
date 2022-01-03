# SCENE 28: Underground Bar
# Locations: Underground Bar
# Characters: MC (Outfit: 9), JENNY (Outfit: x), PENELOPE (Outfit: 3), SAMANTHA (Outfit: 1), BAR WORKER (Outfit: x)
# Time: Saturday night

label v15s28:
    scene v15s28_1 # TPP Show MC walking into the underground bar
    with dissolve

    pause 0.75

    scene v15s28_2 # FPP MC sees Penelope and Jenny sitting next to each other at a booth. They are laughing and there are a couple empty shot glasses in front of them
    with dissolve

    pause 0.75
    
    scene v15s28_3 # FPP MC sitting across the booth from Penelope and Jenny. They are both smiling at him, mouths closed, and look a little drunk already
    with dissolve

    u "Evening, ladies."

    scene v15s28_3a # FPP Same angle as 3, Penelope smiling with mouth closed, Jenny smiling at MC with mouth open
    with dissolve

    jen "Ooh, here he is. Have your ears been burning?"

    scene v15s28_3
    with dissolve

    u "Haha, no. Why should they?"

    if jenny.relationship.value >= Relationship.FWB.value: # -if JennyRs
        scene v15s28_3b # FPP Same angle as 3, Penelope smiling at MC with mouth open, Jenny smiling at MC with mouth closed
        with dissolve

        pe "We've just been talking about you, haha"

        scene v15s28_3a
        with dissolve

        jen "Yeah, all your sordid secrets are out, [name], *Laughs*"

        scene v15s28_3
        with dissolve

        u "What do you mean?"

        scene v15s28_3a
        with dissolve

        jen "*Chuckles* She knows."

        scene v15s28_3
        with dissolve

        u "Knows what?"

        scene v15s28_3a
        with dissolve

        jen "About the fun we had at the lagoon, duh!"

        scene v15s28_3
        with dissolve

        u "Oh... Haha, okay. You told her about that?"

        scene v15s28_3a
        with dissolve

        jen "We tell each other everything, babe. *Laughs*"

        if penelope.relationship.value >= Relationship.LIKES.value: # -if PenelopeRS
            scene v15s28_3c # FPP Same angle as 3, Penelope looks a little sad and is looking down, mouth open
            with dissolve

            pe "Yeah, I mean..."

            scene v15s28_3d # FPP Same angle as 3, Penelope looking at Jenny with a sad smile, mouth open
            with dissolve

            pe "It's great to hear that you two have a good thing going."

            scene v15s28_3e # FPP Same angle as 3, Penelope looking at MC, slightly sad, mouth closed
            with dissolve

            u "Penelope..."

            scene v15s28_3d
            with dissolve

            pe "No, really. That's extremely romantic. Going to a lagoon like that?"

            scene v15s28_3f # FPP Same angle as 3, Jenny looking at Penelope with slight smile and mouth open, Penelope with sad smile and mouth closed
            with dissolve

            jen "Hey, it was my idea!"

            scene v15s28_3d
            with dissolve

            pe "Well, whoever's idea it was... Nice work. My best friends deserve the best."

            scene v15s28_3g # FPP Same angle as 3, Penelope looking at MC with a slight smile, mouth closed
            with dissolve

            u "(That felt bittersweet...)"

        else: # -if PenelopeFriend
            scene v15s28_3h # FPP Same angle as 3, Penelope looking at Jenny with big, excited smile, mouth open, hands over her heart
            with dissolve

            pe "Haha, yep! My two closest friends are dating, eeeeep! *Chuckles*"

            scene v15s28_3b
            with dissolve

            pe "I think I deserve a pat on the back for playing matchmaker, don't you think?"

            scene v15s28_3
            with dissolve

            u "(*Sighs*)"

        scene v15s28_3
        with dissolve

        u "Calm down, haha. It's not like I'm going to propose or anything."

        scene v15s28_3i # FPP Same angle as 3, Jenny looking at MC with her eyebrow raised, mouth open
        with dissolve

        jen "Why? What's wrong with me? *Laughs*"

        scene v15s28_3b
        with dissolve

        pe "Nothing! She's a real catch, [name]! *Giggles*"

        scene v15s28_3j # FPP Same angle as 3, Jenny looking at Penelope, pretending to be angry, playfully slapping Pen on the arm
        with dissolve

        jen "Oh, my God... Was that sarcasm I heard? Bitch!"

        scene v15s28_3k # FPP Same angle as 3, Penolope play-fighting with Jenny, both laughing
        with dissolve

        u "Hey, ladies, no need to fight. *Chuckles* Why don't I keep the peace with some drinks?"

        scene v15s28_3b
        with dissolve

        pe "Hey, yeah... Our glasses are empty!"

        scene v15s28_3l # FPP Same angle as 3, Jenny looking at the empty drink glasses and shouting, holding her arm in the air
        with dissolve

        jen "More drinks!"

        scene v15s28_3m # FPP Same angle as 3, Penelope looking at the empty drink glasses and shouting, holding her arm in the air
        with dissolve

        pe "More drinks!"

        scene v15s28_3n # FPP Same angle as 3, Jenny and Penelope banging empty shot glasses on the table and shouting
        with dissolve

        jen "More drinks!"
        
        pe "More drinks!"

        jen "More drinks!"
        
        pe "More drinks!"

        scene v15s28_3o # FPP Same angle as 3, Jenny and Penelope holding empty shot glasses and smiling at MC
        with dissolve

        u "Okay! Relax!"

        scene v15s28_3
        with dissolve

        u "Jeez, are you sure you guys haven't had enough already?"

        scene v15s28_3p # FPP Same angle as 3, Jenny and Penelope both laughing
        with dissolve

        jen "*laughs*"

        pe "*laughs*"

        scene v15s28_3b
        with dissolve

        pe "Go!"

        scene v15s28_3
        with dissolve

        u "I'm going!"

        scene v15s28_4 # TPP MC getting up from booth to head to the bar, everyone laughing
        with dissolve

        pause 1

    elif jenny.relationship.value >= Relationship.FRIEND.value and penelope.relationship.value >= Relationship.LOYAL.value: # -if JennyFriend and PenelopeLoyal
        scene v15s28_3a
        with dissolve

        jen "Penelope's been telling me about your sexy little rendezvous!"

        scene v15s28_3q # FPP Same angle as 3, Penelope looking at the table, looking embarrassed, mouth open
        with dissolve

        pe "Ugh! Jenny!"

        scene v15s28_3r # FPP Same angle as 3, Jenny smiling at Penelope, mouth open, Penelope blushing and looking embarrassed, mouth closed
        with dissolve

        jen "You cute little cuddle bugs!"

        scene v15s28_3s # FPP Same angle as 3, Penelope still looking embarrassed, looking at MC, Jenny smiling at Penelope
        with dissolve

        u "Haha, it was a legendary cuddle."

        scene v15s28_3q
        with dissolve

        pe "Stop it, you two... *Chuckles*"

        scene v15s28_3r
        with dissolve

        jen "Aw, look... she's gone red!"

        scene v15s28_3t # FPP Same angle as 3, Jenny smiling at MC with mouth open, Penelope still looking embarrassed
        with dissolve

        jen "That means she really likes you."

        scene v15s28_3u # FPP Same angle as 3, Penelope still looking embarrassed, Jenny winking at MC
        with dissolve

        pause 0.75

        scene v15s28_3s
        with dissolve

        u "That's good to know because I really like her too."

        scene v15s28_3v # FPP Same angle as 3, Penelope smiling and touching MC's hand on the table, Jenny with big, excited smile, mouth open, hands over heart
        with dissolve

        jen "Eeeeeep!"

        scene v15s28_3j
        with dissolve

        jen "Okay, that's enough cuteness for one round. More drinks please!"

        scene v15s28_3
        with dissolve

        u "Yeah, looks like I've got some catching up to do... *Laughs*"

        scene v15s28_3l
        with dissolve

        jen "More drinks!"

        scene v15s28_3m
        with dissolve

        pe "More drinks!"

        scene v15s28_3n
        with dissolve

        jen "More drinks!"
        
        pe "More drinks!"

        jen "More drinks!"
        
        pe "More drinks!"

        scene v15s28_3o
        with dissolve

        u "I'm going! I'm going!"

        scene v15s28_ # -All three laugh. MC goes to the bar-
        with dissolve

        pause 1

    else: # -if JennyFriend and PenelopeFriend
        scene v15s28_3a
        with dissolve

        jen "We were just trying to guess who your current bae is. *Giggles*"

        scene v15s28_3b
        with dissolve

        pe "Yeah, I can't actually remember who it is today... Lauren, I think?"

        scene v15s28_3w # FPP Same angle as 3, Penelope and Jenny smiling at each other, Penelope's mouth open
        with dissolve

        pe "Or wait, the blonde one? Ah... Who knows, hehe."

        scene v15s28_3
        with dissolve

        u "(Nice joke...)"

        scene v15s28_3b
        with dissolve

        pe "These shots have gone straight to my head! *Laughs*"

        scene v15s28_3a
        with dissolve

        jen "Me too! Haha..."

        scene v15s28_3b
        with dissolve

        pe "So? Spill it [name]! Who's your current prey?"

        scene v15s28_3x # FPP Same angle as 3, Jenny roaring and making a clawing motion in the air, impersonating a lion
        with dissolve

        jen "*Roars*"

        scene v15s28_3
        with dissolve

        u "Excuse me? *Chuckles*"

        scene v15s28_3b
        with dissolve

        pe "Haven't you got a gazelle in your sights, hehe?"

        scene v15s28_3
        with dissolve

        u "Haha, umm... You know what?"

        u "You ladies keep guessing because a gentleman never tells."

        scene v15s28_5 # TPP Show MC, sitting in the booth, winking at Penelope and Jenny
        with dissolve

        pause 1

        scene v15s28_3y # FPP Same angle as 3, Jenny looking at MC with a fake angry expression, mouth open, giving him a "thumbs down" gesture
        with dissolve

        jen "Boooo!"

        scene v15s28_3z # FPP Same angle as 3, Penelope looking at MC with a fake angry expression, mouth open, giving him a "thumbs down" gesture
        with dissolve

        pe "Yeah, boooo!"

        scene v15s28_3
        with dissolve

        u "*Laughs*"

        scene v15s28_3a
        with dissolve

        jen "Give us the juicy gossip! Tell us who you're fucking!"

        scene v15s28_3p
        with dissolve

        u "Wow, haha. Okay, seems like you two have had enough."

        scene v15s28_3b
        with dissolve

        pe "Hell no!"

        scene v15s28_3a
        with dissolve

        jen "Yeah, we've only just begun!"

        scene v15s28_3l
        with dissolve

        jen "More drinks!"

        scene v15s28_3m
        with dissolve

        pe "More drinks!"

        scene v15s28_3n
        with dissolve

        jen "More drinks!"
        
        pe "More drinks!"

        jen "More drinks!"
        
        pe "More drinks!"

        scene v15s28_3o
        with dissolve

        u "Girls gone wild... *Sighs*"

        scene v15s28_3x
        with dissolve

        jen "*Roars*"

        scene v15s28_4
        with dissolve

        pause 1

        scene v15s28_6 # TPP Show MC walking toward the bar from the booth, Penelope and Jenny still laughing at booth in the background
        with dissolve

        u "(That was a little scary...)"

    # -Regardless-
    scene v15s28_7 # TPP Show MC at the bar, just the edge of Samantha's bar stool visible next to him, bartender behind the bar looking at MC, mouth open
    with dissolve

    barworker "What can I get you?"

    scene v15s28_8 # FPP MC's view of the barworker behind the bar, neutral expression, mouth closed
    with dissolve

    u "(Oh, wow. As easy as that? No ID check at all!)"

    u "Six tequilas, please."

    scene v15s28_8a # FPP Same angle as 8, barworker looking at MC, neutral expression, mouth open
    with dissolve

    barworker "Sure thing! Coming right up."

    scene v15s28_7a # TPP Same angle as 7, Bartender is busy getting a drink, Samantha barely visible at the edge of the frame, looking at MC with mouth open
    with dissolve

    sa "Someone's feeling brave..."

    scene v15s28_7b # TPP Same angle as 7, Bartender is busy getting a drink, Samantha barely visible at the edge of the frame, mouth closed, MC turning his head to look at her, mouth open
    with dissolve

    u "Huh?"

    scene v15s28_9 # FPP MC has turned to look at Samantha, who is sitting on a bar stool holding a beer bottle, looking at MC
    with dissolve

    pause 0.75

    if joinwolves: # -if Wolves
        scene v15s28_9a # FPP Same angle as 9, Samantha taking a drink of her beer
        with dissolve

        u "Oh, hey. I think I've seen you around campus before, no?"

        scene v15s28_9b # FPP Same angle as 9, Samantha talking to MC, neutral expression, mouth open
        with dissolve

        sa "Yeah, I'm Samantha. Cameron's sister."

        scene v15s28_9
        with dissolve

        u "No fucking way... *Chuckles* Yeah, I know Cameron."

        scene v15s28_9b
        with dissolve

        sa "I bet you wish you didn't..."

        scene v15s28_9c # FPP Same angle as 9, Samantha looking at MC with a slight smile, mouth open
        with dissolve

        sa "I wish I didn't, ha."

        scene v15s28_9
        with dissolve

        menu:
            "Say nothing":
                $ add_point(KCT.BRO)

                scene v15s28_9a
                with dissolve

                u "(I really don't want to get involved in Cameron drama...)"
            
            "Ask why":
                scene v15s28_9a
                with dissolve

                u "Do you really mean that? Or is this just a case of your regular sibling rivalry?"

                scene v15s28_9d # FPP Same angle as 9, Samantha looking at MC with an annoyed expression, mouth open
                with dissolve

                sa "Ugh, he's a jerk!"

                scene v15s28_9b
                with dissolve

                sa "He thinks he knows better than everyone else..."

                scene v15s28_9d
                with dissolve

                sa "You just watch, he'll probably bust through that door and start lecturing me any minute. You too probably. *Sighs*"

                scene v15s28_9a
                with dissolve

                u "(Maybe I shouldn't have asked...)"

                scene v15s28_9
                with dissolve

                u "I uh, yeah. That sucks. Family can be tricky sometimes."

                scene v15s28_9e # FPP Same angle as 9, Samantha looking at MC with a slight smile, mouth closed
                with dissolve

                pause 0.75

        # -Regardless-
        scene v15s28_9b
        with dissolve

        sa "You're [name], aren't you?"

        scene v15s28_9
        with dissolve

        u "Yeah. That's me."

        scene v15s28_9b
        with dissolve

        sa "And you're with the Wolves?"

        scene v15s28_9
        with dissolve

        u "I am."

        scene v15s28_9b
        with dissolve

        sa "That's a shame... I don't fuck Wolves."

        scene v15s28_9a
        with dissolve

        u "(I would hope not-)"

        scene v15s28_9c
        with dissolve

        sa "Apes all the way, baby! Leave the stinky dogs and join the Apes, then we can talk. Okay?"

        scene v15s28_9e
        with dissolve

        u "Umm, I don't think it works like that. But good to know, haha."

        scene v15s28_9a
        with dissolve

        u "Have a good night."

        scene v15s28_9b
        with dissolve

        sa "Yeah, you too. Enjoy your six tequilas."

    elif not v14_SamanthaDrugs: # -if Apes and SamanthaSober from 14.53a (MC
        scene v15s28_9
        with dissolve

        u "Oh hey, Samantha. I didn't even see you there."

        scene v15s28_9c
        with dissolve

        sa "It's okay. No one ever does, ha."

        scene v15s28_9a
        with dissolve

        u "I thought you were going to try and quit drinking?"

        scene v15s28_9c
        with dissolve

        sa "I am..."

        scene v15s28_9e
        with dissolve

        u "You're literally holding a beer, Sam."

        scene v15s28_9c
        with dissolve

        sa "It's 0\% alcohol. Look."

        # -Samantha holds the bottle so MC can read it, we don't need to read it, just let him do it, unless you can afford to fake an entire bottle label-
        scene v15s28_9f # FPP Same angle as 9, Samantha holding bottle out for MC to read the label
        with dissolve

        u "Oh, wow... Sorry, haha. That's awesome though, Sam."

        scene v15s28_9c
        with dissolve

        sa "Yeah, it kinda is..."

        scene v15s28_9e
        with dissolve

        u "Isn't it hard going to bars like this and not drinking?"

        scene v15s28_9b
        with dissolve

        sa "Sometimes, but at least this way I don't have to stay in and die of boredom."

        scene v15s28_9c
        with dissolve

        sa "I can still go out, I just don't get fucked up, y'know?"

        scene v15s28_9e
        with dissolve

        u "Yeah, that's really cool. Congrats."

        scene v15s28_9c
        with dissolve

        sa "It's relaxing for a change. I'm making better choices with the guys I hook up with too..."

        scene v15s28_9g # FPP Same angle as 9, Samantha leaning back and laughing, mouth open
        with dissolve

        sa "No more beer goggles in the bedroom, haha."

        scene v15s28_9e
        with dissolve

        u "Haha, beer goggles have helped ugly guys get laid for generations."

        scene v15s28_9c
        with dissolve

        sa "Well, I'll happily give mine up."

        scene v15s28_9e
        with dissolve

        u "Cheers to sober sex!"

        scene v15s28_9h # FPP Same angle as 9, Samantha raising her beer bottle in a "cheers" gesture, mouth open
        with dissolve

        sa "Yes!"

        scene v15s28_9g
        with dissolve

        sa "*laughs*"

        u "*laughs*"

        scene v15s28_9e
        with dissolve

        u "It's good to see you doing well, Sam."

        scene v15s28_9c
        with dissolve

        sa "Ha, thanks [name]."

        scene v15s28_9b
        with dissolve

        sa "For everything, okay?"

        sa "Taking the time to talk to me the other night, it really helped me re-evaluate some things."

        scene v15s28_9c
        with dissolve

        sa "So, thanks... Again *Awkward laugh*"

        scene v15s28_9e
        with dissolve

        u "Anytime, honestly. For the third time, you're welcome. *Chuckles*"

        scene v15s28_9c
        with dissolve

        sa "Ha. Well, have a good night. I'll be heading home soon to pass out."

        scene v15s28_9e
        with dissolve

        u "Yeah, you too. Be safe."

    elif "v14_samantha" not in sceneList: # -if Apes and SamanthaDrugs from 14.53a (let her continue drugs) and DENIED sex afterwards
        scene v15s28_9a
        with dissolve

        u "Hey, Sam. Party for one I see?"

        scene v15s28_9c
        with dissolve

        sa "Haha, for now. Someone will try to swoop in soon enough, they always do."

        scene v15s28_9
        with dissolve

        u "How have you been since we last spoke?"

        scene v15s28_9b
        with dissolve

        sa "Same old shit, ha. You know it is."

        scene v15s28_9
        with dissolve

        u "I see..."

        scene v15s28_9b
        with dissolve

        sa "But thanks again for the chat we had the other night..."

        scene v15s28_9c
        with dissolve

        sa "It's really comforting to know that someone accepts me for who I am."

        scene v15s28_9e
        with dissolve

        u "Yeah, of course. It's your choice at the end of the day, I'll support you no matter what."

        scene v15s28_9
        with dissolve

        u "(Even if your psycho brother won't...)"

        scene v15s28_9h
        with dissolve

        sa "Cheers to that, haha."

        scene v15s28_9a
        with dissolve

        u "Cheers. Have a good night."

        scene v15s28_9c
        with dissolve

        sa "I will."

    else: # -if Apes and SamanthaDrugs from 14.53a (let her continue drugs) and ACCEPTED sex
        scene v15s28_9
        with dissolve

        u "Oh, hey, Sam. Didn't see you there, haha."

        scene v15s28_9b
        with dissolve

        sa "A guy fucks me and then acts like I don't exist anymore, what a shocker! Haha..."

        scene v15s28_9
        with dissolve

        u "Shit, Sam... I didn't mean it like that, come on."

        scene v15s28_9b
        with dissolve

        sa "I know, I know, I'm kidding."

        scene v15s28_9c
        with dissolve

        sa "Seriously, I had fun the other night."

        scene v15s28_9e
        with dissolve

        u "Yeah?"

        scene v15s28_9i # FPP Same angle as 9, Samantha raising her eyebrow at MC with a slight smile, mouth closed
        with dissolve

        sa "Mhmm..."

        scene v15s28_9e
        with dissolve

        u "Good, because I did too. I really enjoy hanging out with you, Sam."

        scene v15s28_9c
        with dissolve

        sa "Well, then let's make sure we do it again sometime soon."

        scene v15s28_9j # FPP Same angle as 9, Samantha giving MC a wink, mouth closed
        with dissolve

        pause 0.75

        scene v15s28_9e
        with dissolve

        u "Definitely. (If Cameron doesn't kill me first.)"

        scene v15s28_9c
        with dissolve

        sa "You have a good night, okay?"

        scene v15s28_9e
        with dissolve

        u "Yeah, you too. I'll catch you later."

        scene v15s28_9c
        with dissolve

        sa "Yup, I know. *Giggles*"

    # -Regardless-
    scene v15s28_10 # FPP MC looks down at the counter in front of him and sees six shots of tequila on a tray
    with dissolve

    barworker "Here are your drinks."

    scene v15s28_10a # FPP Same angle as 10, MC taking his card back from the bartender
    with dissolve

    u "Thanks."

    scene v15s28_7c # TPP Same angle as 7, MC turning away from the bar with six tequila shots on a tray
    with dissolve

    pause 1

    scene v15s28_4a # TPP Same angle as 4, MC sliding into the booth across from Penelope and Jenny and placing the tray of shots on the table
    with dissolve

    pause 0.75

    scene v15s28_3a
    with dissolve

    jen "You took forever! What the fuck, dude?"

    scene v15s28_3b
    with dissolve

    pe "Yeah, I'm sobering up over here!"

    scene v15s28_3
    with dissolve

    u "Six shots of water for the two wasted women in the corner... *Laughs*"

    scene v15s28_3aa # FPP Same angle as 3, Penelope with a fake angry expression looking at MC, mouth open
    with dissolve

    pe "It better not be water, [name]!"

    scene v15s28_3ab # FPP Same angle as 3, Jenny with a fake angry expression looking at MC, mouth open
    with dissolve

    jen "He lies!"

    scene v15s28_3aa
    with dissolve

    pe "He lies!"

    scene v15s28_11 # TPP Penelope, Jenny, and MC all tip back a shot of tequila
    with dissolve

    pause 0.75

    scene v15s28_11a # TPP Same angle as 11, Penelope, Jenny, and MC each lick salt off the back of their hand
    with dissolve

    pause 0.75

    scene v15s28_11b # TPP Same angle as 11, Penelope, Jenny, and MC each suck on a wedge of lime
    with dissolve

    pause 0.75

    scene v15s28_3ac # FPP Same angle as 3, Jenny and Penelope with that slightly disgusted face people get after a shot when they're not used to it and putting empty shot glasses down, Jenny's mouth open
    with dissolve

    jen "Ewugh! That's one!"

    scene v15s28_11
    with dissolve

    pause 0.75

    scene v15s28_11a
    with dissolve

    pause 0.75

    scene v15s28_11b
    with dissolve

    pause 0.75

    scene v15s28_3ad # FPP Same angle as 3, Jenny and Penelope with that slightly disgusted face people get after a shot when they're not used to it and putting empty shot glasses down, Penelope's mouth open
    with dissolve

    pe "*Gags* That's two!"

    scene v15s28_3ae # FPP Same angle as 3, Jenny and Penelope with the disgusted "just took a shot" face, looking at MC
    with dissolve

    u "*Laughs*"

    scene v15s28_3b
    with dissolve

    pe "And..."

    scene v15s28_3a
    with dissolve

    jen "Hey, we've run out of tequila!"

    scene v15s28_3b
    with dissolve

    pe "What's next?!"

    if penelope.relationship.value >= Relationship.LOYAL.value: # -if PenelopeLoyal
        scene v15s28_15 # FPP Closer view of Penelope, who is giving MC a slight smile across the table
        with dissolve

        menu:
            "Kiss Penelope":
                $ add_point(KCT.TROUBLEMAKER)

                scene v15s28_16 # TPP MC leans across the table and kisses Penelope on the lips. Jenny (if visible) smiling at them, mouth open
                with dissolve

                jen "Ooh, lover boy is in the mood tonight!"

                scene v15s28_3af # FPP Same angle as 3, Penelope blushing and slightly smiling at MC, mouth open, Jenny smiling at Penelope
                with dissolve

                pe "Well, that was a nice surprise..."

                scene v15s28_3s
                with dissolve

                u "Sorry, I don't know what came over me..."

                scene v15s28_3u
                with dissolve

                u "I blame the tequila. *Chuckles*"

                scene v15s28_3af
                with dissolve

                pe "Why blame anything for such perfection?"

                scene v15s28_16a # TPP MC and Penelope each lean part way across the table for a gentle kiss
                with dissolve

                pause 0.75

                scene v15s28_3a
                with dissolve

                jen "I can't believe I'm saying this but... Get a room."

                scene v15s28_3
                with dissolve

                u "Ha... We will."

                scene v15s28_3s
                with dissolve

                pause 0.75

            "Don't kiss her":
                scene v15s28_14
                with dissolve

                u "(The tequila is trying to take control...Stay strong, [name].)"

    elif jenny.relationship.value >= Relationship.FWB.value: # -if JennyRs
        scene v15s28_12 # FPP Closer view of Jenny, who is giving MC a smile across the table
        with dissolve

        menu:
            "Kiss Jenny":
                $ add_point(KCT.TROUBLEMAKER)

                scene v15s28_13 # TPP MC leans across the table and kisses Jenny on the lips, Penelope (if visible) leaning away from them with mouth open
                with dissolve

                pe "Woah... Okay, lovebirds!"

                scene v15s28_3b
                with dissolve

                pe "That was impulsive... Hehe. I think someone's had enough to drink."

                scene v15s28_3a
                with dissolve

                jen "No, let him drink more. *Giggles* I might have to get you another one of those!"

                scene v15s28_3
                with dissolve

                u "Sorry, it's the tequila's fault. I just couldn't help myself."

                scene v15s28_12
                with dissolve

                pause 0.75

                scene v15s28_13a # TPP Same angle as 13, Jenny leaning across the table to kiss MC this time, Penelope (if visible) smiling and rolling her eyes, mouth closed
                with dissolve

                pause 0.75

            "Don't kiss her":
                scene v15s28_14 # FPP MC looks down at all the empty shot glasses on the table, maybe the image is a bit fuzzy from the drinking
                with dissolve

                u "(This tequila is getting the best of me. Must... Resist...)"

    # -Regardless-
    # -A quick series of shots showing MC, Penelope and Jenny sat at the table, laughing and drinking. Different drinks appear on the table, the drinks get drunk, more empty glasses etc, as the night goes on-
    scene v15s28_17 # TPP Show MC, Penelope, and Jenny sitting in the booth laughing, with some fresh drinks in front of them
    with dissolve

    pause 0.75

    scene v15s28_11
    with dissolve

    pause 0.75

    scene v15s28_17a # TPP Same angle as 17, Penelope and Jenny looking at each other and laughing at something, MC taking a drink of a beer
    with dissolve

    pause 0.75

    scene v15s28_3ag # FPP Same angle as 3, Jenny and Penelope looking out over the bar room, Penelope's mouth open
    with dissolve

    pe "Oh, shit! They'll be closing in a few minutes. We should probably try to beat the rush."

    scene v15s28_3
    with dissolve

    u "Time flies when you're getting wasted, ha."

    u "Did you guys have a good time?"

    scene v15s28_3a
    with dissolve

    jen "Yeah, for sure. I'm ready for bed, haha."

    scene v15s28_3b
    with dissolve

    pe "Same... I could fall asleep right now. *Giggles*"

    scene v15s28_3
    with dissolve

    u "Let's get out of here then, before you make the world's most uncomfortable bed out of this table. *Laughs*"

    scene v15s28_18 # TPP Show MC, Jenny, and Penelope all getting up from the booth to leave
    with dissolve

    pause 0.75

    if jenny.relationship.value >= Relationship.FWB.value and penelope.relationship.value >= Relationship.LIKES.value: # -if JennyRs and PenelopeRs (Lagoon with Jenny but had RS with Penelope prior to that)
        scene v15s28_19 # TPP Show Penelope stopping MC by grabbing his arm, Penelopewith neutral expression and mouth open, Jenny walking away toward the door in the background
        with dissolve

        pe "Hey, [name]. Come here for a sec?"

        scene v15s28_20 # FPP Show Penelope looking at MC, both standing, Penelope with neutral expression and mouth closed
        with dissolve

        u "Sure."

        scene v15s28_20a # FPP Same angle as 20, Penelope looking at MC, both standing, Penelope with neutral expression, mouth open
        with dissolve

        pe "I just wanted to say..."

        scene v15s28_20b # FPP Same angle as 20, Penelope looking at MC with a slight smile, mouth open
        with dissolve

        pe "I'm really happy that you've been having a good time with Jenny."

        scene v15s28_20a
        with dissolve

        pe "I thought there was something more between you and I, and if there was, just..."

        scene v15s28_20b
        with dissolve

        pe "Jenny's awesome and I know you'll be happy with her."

        scene v15s28_20
        with dissolve

        u "Thanks Penelope. Really. And, if I upset you in any way, I am sorry"

        scene v15s28_19a # TPP Same angle as 19, Penelope giving MC and quick hug
        with dissolve

        pause 0.75

        scene v15s28_20b
        with dissolve

        pe "We're good."

    elif penelope.relationship.value >= Relationship.LOYAL.value: # -if PenelopeLoyal
        scene v15s28_19b # TPP Same angle as 19, show Jenny stopping MC by grabbing his arm, Jenny smiling with mouth open, Penelope walking away toward the door in the background
        with dissolve

        jen "Hey, [name]..."

        scene v15s28_21 # FPP Show Jenny looking at MC, both standing, Jenny with a slight smile, mouth open
        with dissolve

        jen "You know, I'm happy that you and Penelope are getting on so well."

        scene v15s28_21a # FPP Same angle as 21, Jenny looking at MC with a slight smile, mouth closed
        with dissolve

        u "Yes, thank you. *Laughs*"

        scene v15s28_21b # FPP Same angle as 21, Jenny looking over at Penelope walking away, Jenny with slight smile and mouth open
        with dissolve

        jen "She likes to take things slow. You already know that, but..."

        scene v15s28_21
        with dissolve

        jen "I promise you, if you keep doing whatever you're doing to her, one day she'll give you every ounce of her."

        scene v15s28_21c # FPP Same angle as 21, Jenny winking and smiling at MC, mouth closed
        with dissolve

        pause 0.75

        scene v15s28_21a
        with dissolve

        u "She's worth the wait."

        scene v15s28_21
        with dissolve

        jen "Yes! She is! Say it louder!"

        scene v15s28_21a
        with dissolve

        u "Haha, I will."

        scene v15s28_19c # TPP Same angle as 19, Jenny giving MC a quick side hug as they turn to leave the bar
        with dissolve

        pause 0.75

    # -Regardless-
    scene v15s28_22 # TPP Show MC, Penelope, and Jenny leaving the bar
    with dissolve

    pause 0.75

    scene v15s28_23 # TPP Show Penelope, MC, and Jenny walking down the street, all a bit drunk, MC in the middle, Jenny's mouth open
    with fade

    jen "Come on, guys!"

    scene v15s28_24 # FPP MC's view of Jenny as they walk down the street. Jenny with a slight smile, a bit drunk, looking at MC with mouth open
    with dissolve

    jen "Let's sing a song! Please?"

    scene v15s28_25 # FPP MC's view of Penelope as they walk down the street. Penelope is a bit drunk with a slight smile, looking across MC at Jenny, mouth open
    with dissolve

    pe "What shall we sing?"

    scene v15s28_25a # FPP Same angle as 25. Penelope looking at MC with a slight smile, a bit drunk, mouth closed
    with dissolve

    u "I know one."

    scene v15s28_25b # FPP Same angle as 25. Penelope looking at MC with a slight smile, a bit drunk, mouth open
    with dissolve

    pe "Go on then!"

    scene v15s28_23a # TPP Same angle as 23, Penelope, MC, and Jenny walking down the street, all a bit drunk, MC in the middle, all mouths closed
    with dissolve

    menu:
        "Sing a silly song":
            $ add_point(KCT.TROUBLEMAKER)
                
            scene v15s28_23b # TPP Same angle as 23, Penelope, MC, and Jenny walking down the street, all a bit drunk, MC in the middle, MC's mouth open, singing loudly
            with dissolve

            u "Twinkle twinkle, little star..."

            scene v15s28_23c # TPP Same angle as 23, Penelope, MC, and Jenny walking down the street, all a bit drunk, MC in the middle, singing loudly, looking another direction, holding his arms out
            with dissolve

            u "Take me to the nearest bar..."

            scene v15s28_23d # TPP Same angle as 23, Penelope, MC, and Jenny walking down the street, all a bit drunk, MC in the middle, all laughing with mouths open
            with dissolve

            pe "Good one, Grandpa!"

            scene v15s28_24
            with dissolve

            jen "You're so stupid... *Giggles*"

        "Whistle instead":
            scene v15s28_23e # TPP Same angle as 23, Penelope, MC, and Jenny walking down the street, all a bit drunk, MC in the middle, MC pursing his lips and whistling
            with dissolve

            u "*Whistles*"

            scene v15s28_23d
            with dissolve

            pause 0.75

            scene v15s28_25b
            with dissolve

            pe "That's not singing!"

            scene v15s28_25a
            with dissolve

            u "I'm using my voice, aren't I? ."

            scene v15s28_24
            with dissolve

            jen "What even is that?"

            scene v15s28_24a # FPP Same angle as 24, Jenny looking at MC with a slight smile, mouth closed
            with dissolve

            u "I was singing Happy Birthday..."

            scene v15s28_24
            with dissolve

            jen "..."

            scene v15s28_25b
            with dissolve

            pe "Wow, you're so talented..."

    # -Regardless-
    scene v15s28_23d
    with dissolve

    pause 1

    if joinwolves: # -if Wolves, transition to Scene 29-
        jump v15s29

    else: # -if Apes, transition to Scene 30-
        jump v15s30