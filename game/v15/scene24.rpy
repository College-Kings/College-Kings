# SCENE 24: Buy booze with a fake ID
# Locations: Convenient Store
# Characters: MC (Outfit: 9), LINDSEY (Outfit: 1), CASHIER (Outfit: x)
# Time: Morning

label v15s24:
    scene v15s24_1 # TPP. Show MC walking up to the convenient store, MC slightly confused, mouth closed.
    with dissolve

    pause 0.75

    scene v15s24_2 # FPP. MC looking at the front door to the store.
    with dissolve

    u "(Where's Lindsey? She said she would be here.)"

    li "Pssst! *Whispers* Hey, [name]."

    scene v15s24_3 # FPP. MC looking to the side and see's Lindsey peaking from around the corner of the store, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s24_4 # TPP. Show MC walking over to around the side of the store where Lindsey is, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s24_5 # FPP. MC and Lindsey on the side of the store, MC looking at Lindsey, Lindsey looking at MC, Lindsey slight smile, mouth closed.
    with dissolve

    u "Lindsey, what are you doing back there?"

    scene v15s24_5a # FPP. MC and Lindsey on the side of the store, MC looking at Lindsey, Lindsey looking at MC, Lindsey slight smile, mouth open.
    with dissolve

    li "I'm hiding! We're underage, remember?"

    li "You can't be seen with me before you go in."

    scene v15s24_5
    with dissolve

    u "Right... *Chuckles* So what's the plan?"

    scene v15s24_5a
    with dissolve

    li "Fake IDs."

    scene v15s24_6 # TPP. Show Lindsey's hand pulling out two ID's out of her pocket.
    with dissolve

    pause 0.75

    scene v15s24_5b # FPP. MC and Lindsey on the side of the store, MC looking at Lindsey, Lindsey looking at MC, Lindsey holding up the ID's for MC to see, Lindsey slight smile, mouth closed.
    with dissolve

    pause 0.75

    if v11_josh_nightclub:
        scene v15s24_5c # FPP. MC and Lindsey on the side of the store, MC looking at Lindsey, Lindsey looking at MC, Lindsey not holding up the ID's anymore but still in her hand, Lindsey slight smile, mouth closed.
        with dissolve

        u "Nice! My last one from Josh expired like a day after I got it, haha."

        u "(Speaking of Josh... Where the hell is he?)"

    scene v15s24_5d # FPP. MC and Lindsey on the side of the store, MC looking at Lindsey, Lindsey looking at MC, Lindsey not holding up the ID's anymore but still in her hand, Lindsey slight smile, mouth open.
    with dissolve

    li "Well, you have two to choose from."

    li "I didn't know which one was best, so I grabbed both."

    scene v15s24_5c
    with dissolve

    u "Okay, let's see..."

    scene v15s24_5e # FPP. MC looking at the ID's, Lindsey looking at MC, Lindsey holding the ID's up for MC to see. We should have a clear image of both ID's, both have a picture of MC on it, one with Name: Nancy Dick, Age: 21. The other ID Name: Andrew King, Age: 29.
    with dissolve

    pause 0.75

    menu:
        "Nancy Dick":
            $ v15s24_nancy_dick = True

            scene v15s24_5c
            with dissolve

            u "The age is right on this one, but..."

            u "Nancy Dick? Really?"

            scene v15s24_5d
            with dissolve

            li "Oh, come on. Nancy can be a boy's name."

            scene v15s24_5c
            with dissolve

            u "In what country? *Laughs*"

            scene v15s24_5d
            with dissolve

            li "Erm, somewhere in Europe? *Giggles*"

            scene v15s24_5c
            with dissolve

            u "And the surname... Dick?"

            scene v15s24_5f # FPP. MC looking at Lindsey, Lindsey looking at MC, Show Lindsey covering her mouth as she tries not to laugh.
            with dissolve

            u "Who made these ID's?"

            scene v15s24_5d
            with dissolve

            li "*Laughs* Trust me, these were the two best options."

            scene v15s24_5c
            with dissolve

            u "Well, age is most important, surely."

            u "I don't know if I could pass as a twenty-nine-year-old named Andrew."

            scene v15s24_5d
            with dissolve

            li "Wise decision, Nancy."

            scene v15s24_5c
            with dissolve

            u "*Sighs* Thanks..."

        "Andrew King": 
            scene v15s24_5c
            with dissolve

            u "Andrew King..."

            u "At least that sounds like an actual person."

            scene v15s24_5d
            with dissolve

            li "Haha, what's wrong with Nancy?"

            scene v15s24_5c
            with dissolve

            u "..."

            scene v15s24_7 # TPP. MC and Lindsey on the side of the store, MC looking at Lindsey with an Annoyed neutral face, mouth closed, Lindsey looking at Mc with a slight smile, mouth closed.
            with dissolve

            pause 0.75

            scene v15s24_5f
            with dissolve

            pause 0.75

            scene v15s24_5c
            with dissolve

            u "Twenty-nine though? I still get ID'd for candy... I'm not sure if I can pass as almost 30 years old."

            scene v15s24_5d
            with dissolve

            li "*Laughs* I could draw a beard on you, maybe."

            scene v15s24_5c
            with dissolve

            u "Hmm, you're right... Has that ever worked?"

            scene v15s24_5d
            with dissolve

            li "Meh, not in the movies, no."

            scene v15s24_7a # TPP. MC and Lindsey on the side of the store both laughing.
            with dissolve

            pause 0.75

            scene v15s24_5d 
            with dissolve

            li "It's all in the mindset, right?"

            li "Just carry yourself like a full-grown, responsible adult, and you'll ace it."

            scene v15s24_5c
            with dissolve

            u "Well, I may not be as full grown as a thirty-year-old, but I guess I can at least act responsible...? *Chuckles*"

            scene v15s24_5d
            with dissolve

            li "That's the attitude, yes!"
    
    scene v15s24_5d
    with dissolve

    li "Here some cash too."

    if lindsey.relationship.value >= Relationship.FWB.value: 
        scene v15s24_5c
        with dissolve

        u "Oooh, I could get used to this..."

        scene v15s24_5g # FPP. MC and Lindsey on the side of the store, MC looking at Lindsey, Lindsey looking at MC, Lindsey not holding up the ID's anymore but still in her hand, Lindsey smirking, mouth closed.
        with dissolve

        pause 0.75

        scene v15s24_5h # FPP. Show Lindsey leaning in towards MC.
        with dissolve

        pause 0.75

        play sound "sounds/kiss.mp3"

        scene v15s24_5i # FPP. Lindsey giving MC a kiss.
        with dissolve

        pause 0.75

        scene v15s24_5d
        with dissolve

        li "Do well in there, and you just might have to. *Giggles*"

    else:
        scene v15s24_5c
        with dissolve

        u "Isn't it supposed to be sugar daddy? Not-"

        scene v15s24_5d
        with dissolve

        li "Sugar mommy? Ha..."

        scene v15s24_7b # TPP. MC looking at Lindsey with a weirded out face, mouth closed, Lindsey slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s24_5d
        with dissolve

        li "What's wrong with a sugar mommy, huh?"

        scene v15s24_5c
        with dissolve

        u "Nothing... Let's, uh..."

        scene v15s24_5d
        with dissolve

        li "Hehe."

    scene v15s24_7c # TPP. Lindsey handing MC the ID and some money, don't show the name on the ID in this photo so it can be used for either ID choice, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s24_5a
    with dissolve

    li "Alright, you're all set. Go get 'em tiger!"

    scene v15s24_5
    with dissolve

    u "Thanks. I shall return victorious! *Laughs*"

    scene v15s24_5a
    with dissolve

    li "Please do... Honestly, haha. Good luck!"

    scene v15s24_4a # TPP. Show MC walking the otherway toward the door of the store, slight smile, mouth closed.
    with dissolve

    u "(No pressure...)"

    play sound "sounds/dooropen.mp3"

    scene v15s24_8 # TPP. Show MC entering the store, slight smile, mouth closed.
    with dissolve

    pause 0.75

    play sound "sounds/doorclose.mp3"

    scene v15s24_9 # TPP. Show MC in the Alcohol area of the convenient store looking at the selection of items, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s24_10 # FPP. MC looking at all the Alcohol in the store, somewhere in view a bag of candies with the Alcohol called "Condy's vodka candies".
    with dissolve

    pause 0.75

    scene v15s24_9a # TPP. Show MC reaching and grabbing bottles of Alcohol, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v15s24_11 # FPP. MC looking at the bag of "Condy's vodka candies".
    with dissolve

    u "(Hmm, Condy's vodka candies? These look interesting...)"

    u "(Candy that gets you drunk, ha! We're definitely getting some of these.)"

    scene v15s24_9b # TPP. Show MC reaching and grabbing the bag of candy, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s24_12 # TPP. Show MC walking up to the counter with the Alcohol and the Candy, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s24_13 # FPP. MC looking at the Cashier, The Cashier looking at MC, The cashier is a "potato-headed" 30 year old with glasses, wearing a shirt with a chest pocket a vape sitting inside the entire time, Cashier slight smile, mouth open.
    with dissolve

    cashier "Hey, man... Did you find everything you wanted?"

    scene v15s24_13a # FPP. MC looking at the Cashier, The Cashier looking at MC, The cashier is a "potato-headed" 30 year old with glasses, wearing a shirt with a chest pocket a vape sitting inside the entire time, Cashier slight smile, mouth closed.
    with dissolve

    u "Uh, yeah. Thanks."

    scene v15s24_13
    with dissolve

    cashier "Cool. I'm going to need to see your ID, please."

    scene v15s24_13a
    with dissolve

    u "Oh, of course."

    u "I'm used to not getting carded, haha."

    scene v15s24_13
    with dissolve

    cashier "Yeah, I get it. But... I gotta check."

    scene v15s24_14 # TPP. Show just MC's and the Cashier's hand, MC handing over the ID, Don't show the name or age of the ID so it can be used for either ID choice, the cashier grabbing the ID.
    with dissolve

    pause 0.75

    if v15s24_nancy_dick:
        scene v15s24_13b # FPP. MC looking at the Cashier, The cashier looking at the ID, Cashier slight smile, mouth open.
        with dissolve

        cashier "*Laughs* Oh my God... Are you serious?"

        scene v15s24_13c # FPP. MC looking at the Cashier, The cashier looking at the ID, Cashier slight smile, mouth closed.
        with dissolve

        u "What?"

        scene v15s24_15 # TPP. Just the Cashier with his hand on his stomach laughing.
        with dissolve

        pause 0.75

        scene v15s24_13
        with dissolve

        cashier "Nancy?"

        scene v15s24_13a
        with dissolve

        u "Yes, that's my name... Why are you laughing?"

        scene v15s24_13
        with dissolve

        cashier "Nancy Dick?! *Laughs*"

        scene v15s24_13a
        with dissolve

        u "Ahem..."

        scene v15s24_13
        with dissolve

        cashier "What's your middle name, Nancy?"

        scene v15s24_13a
        with dissolve

        u "Why does that-"

        scene v15s24_13
        with dissolve

        cashier "Eats?! Haha!"

        scene v15s24_13a
        with dissolve

        u "Nancy Eats Dick, wow. Funny!"

        scene v15s24_16 # TPP. MC looking at the Cashier with a straight face, mouth closed, the cashier laughing.
        with dissolve

        pause 0.75

        scene v15s24_13a
        with dissolve

        u "I've heard that one actually."

        scene v15s24_13
        with dissolve

        cashier "Ha... Oh, man. You're killing me..."

        cashier "*Chuckles* Phew..."

        scene v15s24_13a
        with dissolve

        u "Done yet?"

        scene v15s24_13
        with dissolve

        cashier "Worst fake ID ever, pal."

        scene v15s24_13a
        with dissolve

        u "Excuse me?"

        scene v15s24_13
        with dissolve

        cashier "There's no fucking way this is your real name, man. Explain it."

        scene v15s24_13a
        with dissolve

        u "My parents gave it to me, jackass. Want me to call them real quick and find out the origin for you?"

        scene v15s24_13
        with dissolve

        cashier "Pfft, whatever man..."

        cashier "Nancy is a name for females and... Well, you're clearly a dude."

        scene v15s24_13a
        with dissolve

        u "Who are you to decide what name belongs to which gender?"

        scene v15s24_13
        with dissolve

        cashier "Listen kid, even if your name is Nancy, and you're a fucking loser... *Laughs*"

        cashier "There's no way your last name is actually Dick."

        cashier "You're not fooling me with this shit. Not today!"

        scene v15s24_13a
        with dissolve

        u "(Fuck this guy... Should I stick with the fake story or just come clean at this point?)"

        menu:
            "Act offended":
                $ v15_lindsey_alcohol = True
                scene v15s24_16a # TPP. MC looking at the Cashier angrily, mouth closed, the cashier looks shocked, mouth closed
                with dissolve

                u "How dare you?!"

                scene v15s24_13d # FPP. MC looking at the Cashier, The cashier looking at MC, Cashier worried, mouth closed.
                with dissolve

                $ grant_achievement("karen")
                u "Where is your manager?!"

                scene v15s24_13e # FPP. MC looking at the Cashier, The cashier looking at MC, Cashier worried, mouth open.
                with dissolve

                cashier "I, uh... I..."

                scene v15s24_13d
                with dissolve

                u "You do know that type of behavior isn't acceptable in modern society, correct?"

                u "What are you, a Neanderthal?"

                scene v15s24_13e
                with dissolve

                cashier "I'm not a- Wait, what did you call me...?"

                scene v15s24_13d
                with dissolve

                u "This is borderline discrimination! Give me one good reason why I shouldn't have you fired?!"

                scene v15s24_13e
                with dissolve

                cashier "No, no, no... Please, don't..."

                scene v15s24_13d
                with dissolve

                u "You just made a big mistake..."

                u "(Huge. *Giggles*)"

                scene v15s24_13e
                with dissolve

                cashier "I didn't mean to offend you! I'm so sorry, sir..."

                cashier "I'll ring you up right now."

                scene v15s24_13d
                with dissolve

                u "(Yes!)"

                scene v15s24_13f # FPP. Show the cashier pressing buttons on the cash register in panic, Cashier worried, mouth closed.
                with dissolve

                u "You're lucky I'm in a rush... *Scoffs*"

                scene v15s24_13e
                with dissolve

                cashier "Your total is forty-"

                scene v15s24_16b # TPP. MC throwing cash on the counter, MC angry, mouth closed, Cashier worried, mouth closed.
                with dissolve

                pause 0.75

                scene v15s24_13g # FPP. The cashier gathering the cash in a hurry, Cashier worried, mouth closed.
                with dissolve

                u "Just take my damn money so I can get on with my day, would you?"

                scene v15s24_13h # FPP. The cashier putting the money in the register, Cashier worried, mouth open.
                with dissolve

                cashier "Yes... O-of course. I'm... I'm so sorry."

                scene v15s24_13i # FPP. The cashier handing out the bag and a handful of change over the counter, Cashier worried, mouth closed.
                with dissolve

                pause 0.75

                scene v15s24_13j # FPP. MC taking the bag of the items, Cashier worried, mouth closed.
                with dissolve

                u "Keep it."

                scene v15s24_13e
                with dissolve

                cashier "Yes. Of course..."

                scene v15s24_13d
                with dissolve

                u "If I ever come back in here, I expect better service... and a lifetime discount!"

                scene v15s24_13e
                with dissolve

                cashier "Anything, Mr. Dick! Anything we can do for you, we will."

                scene v15s24_13d
                with dissolve

                pause 0.75

                scene v15s24_16c # TPP. MC taking his ID from off the counter (Don't show the details of the ID), MC angry, mouth closed, Cashier worried, mouth closed
                with dissolve

                u "(Ha, perfect.)"

            "Come clean":
                scene v15s24_13a
                with dissolve

                u "(Fuck...)"

                u "*Sighs* Okay. Busted."

                scene v15s24_13k # FPP. MC looking at the Cashier, The cashier looking at the ID, Cashier slightly annoyed, mouth open.
                with dissolve

                cashier "Yeah, no shit. *Scoffs*"

                scene v15s24_13l # FPP. MC looking at the Cashier, The cashier looking at the ID, Cashier slightly annoyed, mouth closed.
                with dissolve

                u "But please... Can you just let it slide this one time? I swear to you, nobody will ever find out about this."

                scene v15s24_13k
                with dissolve

                cashier "Hell no, kid! I'd lose my job."

                scene v15s24_13l
                with dissolve

                u "I won't tell anyone, though! I promise."

                scene v15s24_13
                with dissolve

                cashier "Ha! Yeah right!"

                cashier "All of your high school friends will be soon trying to empty the shelves."
                cashier "If you stick around you can probably get a ride home from them. *Laughs*"

                scene v15s24_13a
                with dissolve

                u "Do I look like I'm in high school?"

                scene v15s24_13
                with dissolve

                cashier "Yeah, dude. 18 at most."

                scene v15s24_13a
                with dissolve

                u "I'm in college, bro!"

                scene v15s24_13
                with dissolve

                cashier "Tell that to your non-existent facial hair."

                scene v15s24_13a
                with dissolve

                u "(This motherfucker...)"

                u "How about I, you know... Give you a tip?"

                scene v15s24_13
                with dissolve

                cashier "I'm not selling you alcohol, kid."

                cashier "You can argue and bribe all you want, but it won't work. It never has, and it never will."

                cashier "It's best if you just leave."

                scene v15s24_13a
                with dissolve

                u "*Sighs*"

                u "(I fucked that up...)"

                u "Okay, sure. Sorry."

                scene v15s24_17 # TPP. Show MC walking towards the store door, MC frown, mouth closed.
                with dissolve

                pause 0.75

                if kct == "popular":
                    call screen kct_popup
                    $ v15_lindsey_alcohol = True

                    scene v15s24_17
                    with vpunch

                    cashier "Wait."

                    scene v15s24_13a
                    with dissolve

                    u "Yeah?"

                    scene v15s24_13m # FPP. MC looking at Cashier, The cashier squinting at and studying MC, Cashier slight smile, mouth closed.
                    with dissolve

                    pause 0.75

                    scene v15s24_13n # FPP. MC looking at Cashier, The cashier rolling his eyes, Cashier slight smile, mouth closed.
                    with dissolve

                    pause 0.75

                    scene v15s24_13
                    with dissolve

                    cashier "On second thought..."

                    cashier "*Whispers* Fifty bucks and you're free to go."

                    scene v15s24_13a
                    with dissolve

                    u "(Ha!) Deal!"

                    scene v15s24_18 # TPP. Close up of just the cashier scanning the items, slight smile, mouth closed.
                    with dissolve

                    pause 0.75

                    scene v15s24_18a # TPP. Close up of just the cashier bagging the items, slight smile, mouth closed
                    with dissolve

                    pause 0.75

                    scene v15s24_16d # TPP. Show MC putting cash on the counter, MC slight smile, mouth closed, Cashier slight smile, mouth closed
                    with dissolve

                    pause 0.75

                    scene v15s24_13o # FPP. MC looking at the Cashier, The cashier looking at MC, Cashier handing the bag of items over the counter, slight smile, mouth closed.
                    with dissolve

                    pause 0.75

                    scene v15s24_13a
                    with dissolve

                    u "Thanks for your help. This is amazing."

                    scene v15s24_13
                    with dissolve

                    cashier "Drink responsibly, Miss Dick! *Laughs*"

                    scene v15s24_13a
                    with dissolve

                    u "*Chuckles*"

    else:
        scene v15s24_13b
        with dissolve

        cashier "Andrew King, is it?"

        scene v15s24_13c
        with dissolve

        u "That's me, yeah."

        scene v15s24_13
        with dissolve

        cashier "Hmm, that's weird..."

        scene v15s24_13a
        with dissolve

        u "(Shit.)"

        scene v15s24_13
        with dissolve

        cashier "I had a buddy in high school named Andrew King."

        scene v15s24_13a
        with dissolve

        u "Oh, ha... Wow, what a coincidence. *Nervous chuckle*"

        scene v15s24_13m
        with dissolve

        cashier "So, twenty-nine?"

        scene v15s24_13a
        with dissolve

        u "Yep... Almost the big 30! Ha... *Clears throat*"

        scene v15s24_13
        with dissolve

        cashier "Ha."

        scene v15s24_14a # The cashier handing back the ID, MC grabbing the ID.
        with dissolve

        pause 0.75

        scene v15s24_13k
        with dissolve

        cashier "I think you should leave, pal."

        scene v15s24_13l
        with dissolve

        u "Wait, what?! Why? I-"

        scene v15s24_13k
        with dissolve

        cashier "There's no way in hell that you're almost thirty, my guy. Have you looked in the mirror lately? *Scoffs*"

        scene v15s24_13l
        with dissolve

        u "(Okay, asshole.)"

        scene v15s24_13k
        with dissolve

        cashier "Go on, kid. Scram."

        scene v15s24_13l
        with dissolve

        u "I'll have you know that I have a medical conditi-"

        scene v15s24_13k
        with dissolve

        cashier "Really? You're gonna play that card?"

        scene v15s24_13l
        with dissolve

        u "I do!"

        scene v15s24_13
        with dissolve

        cashier "*Chuckles* Yeah, okay. You have a medical condition that makes you look fifteen years old, and I have a bullshit detector. Take a hike!"

        scene v15s24_13a
        with dissolve

        u "You're making a big mistake."

        u "(Huge... *Giggles*)"

        scene v15s24_13k
        with dissolve

        cashier "Okay, fake Andrew. What do you do for a living? Huh?"

        scene v15s24_13l
        with dissolve

        u "Well, not that it's any of your business..."

        u "(Smart job, smart, smart job... What's a smart job?!)"

        scene v15s24_13
        with dissolve

        cashier "Yeah? Did you forget? *Laughs*"

        scene v15s24_13a
        with dissolve

        u "No, I'm..."

        menu:

            "Lawyer":
                scene v15s24_13l
                with dissolve

                u "A lawyer."

                scene v15s24_13k
                with dissolve

                cashier "Ha! A lawyer?"

                cashier "You're gonna walk around dressed like that, and expect people to believe that you're a lawyer?"

            "Astronaut":
                scene v15s24_13l
                with dissolve

                u "An astronaut."

                scene v15s24_13k
                with dissolve

                cashier "*Scoffs* An astronaut? Are you kidding me???"

                cashier "You're so full of shit."

                scene v15s24_13l
                with dissolve

                u "You better sell me some alcohol or I'm calling NASA."

        scene v15s24_13
        with dissolve

        cashier "*Laughs* You're one of the funniest scumbags I've met in this place."

        scene v15s24_13l
        with dissolve

        u "(Fuck's sake... How do I get out of this?)"

        menu:
            "Act offended":
                $ v15_lindsey_alcohol = True
                scene v15s24_13l
                with dissolve

                u "You're going to be sorry you ever said that."

                scene v15s24_13k
                with dissolve

                cashier "Huh?"

                scene v15s24_16e # TPP. Show MC pulling his phone out of his pocket, MC angry, mouth closed, Cashier confused, mouth open.
                with dissolve

                cashier "Wait, what are you doing?"

                scene v15s24_16f # TPP. MC with the phone to his ear, angry, mouth open, Cashier worried, mouth closed.
                with dissolve

                u "Yes, hello! I'd like to report a hate crime, please."

                scene v15s24_16g # TPP. MC with the phone to his ear, angry, mouth closed, Cashier worried, mouth open.
                with dissolve

                cashier "What?! What the fuck- Who are you even talking to?"

                scene v15s24_16f
                with dissolve

                u "The police, sir."

                scene v15s24_16g
                with dissolve

                cashier "The police?! Stop! What are you-"

                scene v15s24_16h # TPP. The cashier trying to reach over the counter and grab the phone, MC stepped back, MC angry, mouth closed, Cashier worried, mouth open.
                with dissolve

                cashier "Holy fuck, you psycho!"

                scene v15s24_16f
                with dissolve

                u "They're connecting me to the department for hate crimes right now, we're on hold."

                scene v15s24_16g
                with dissolve

                cashier "No, listen- You have to stop... Please, hang up!"

                cashier "It's okay. I-I, I believe you!"

                scene v15s24_16f
                with dissolve

                u "You're going to stop discriminating against people?"

                scene v15s24_16g
                with dissolve

                cashier "Yes... Yes. I'll do whatever, just..."

                scene v15s24_16i # TPP. Cashier with his hands together pleading to MC, MC angry on the phone mouth closed, Cashier worried, mouth closed.
                with dissolve

                u "(Damn, this guy is really afraid of the police. Lucky for me, ha!)"

                scene v15s24_16g
                with dissolve

                cashier "Please hang up."

                scene v15s24_16f
                with dissolve

                u "Fine."

                scene v15s24_16j # TPP. Show MC putting his phone away, MC angry, mouth closed, cashier worried, mouth closed.
                with dissolve

                pause 0.75

                scene v15s24_13d
                with dissolve

                u "Well, what are you waiting for?"

                scene v15s24_13e
                with dissolve

                cashier "Oh- Of course! Sorry..."

                scene v15s24_18b # TPP. Close up of just the cashier scanning the items, worried, mouth closed.
                with dissolve

                pause 0.75

                scene v15s24_18c # TPP. Close up of just the cashier bagging the items, worried, mouth closed
                with dissolve

                pause 0.75

                scene v15s24_16b 
                with dissolve

                pause 0.75

                scene v15s24_13i 
                with dissolve

                pause 0.75

                scene v15s24_13j 
                with dissolve

                u "Keep it."

                scene v15s24_13d
                with dissolve

                u "I expect you'll be more considerate of people with disabilities in the future."

                scene v15s24_13e
                with dissolve

                cashier "I, uh... I will."

                cashier "I'm so sorry for my behavior."

                scene v15s24_13d
                with dissolve

                u "You should be."

            "Come clean":
                scene v15s24_13l
                with dissolve

                u "*Sighs* Okay. You caught me."

                scene v15s24_13
                with dissolve

                cashier "Ha, wait- You're admitting it?"

                scene v15s24_13l
                with dissolve

                u "Yeah, I am. Happy?"

                scene v15s24_13k
                with dissolve

                cashier "Eh, more surprised than anything."

                scene v15s24_13l
                with dissolve

                u "Look, can we please just..."

                u "Work out some sort of a deal? I really need this alcohol, man."

                scene v15s24_13k
                with dissolve

                cashier "*Scoffs* Nobody needs alcohol, kid. The human body can survive just fine without it."

                scene v15s24_13l
                with dissolve

                u "You know what I mean, bro. It's college."

                u "Please?"

                scene v15s24_13k
                with dissolve

                cashier "No."

                scene v15s24_13l
                with dissolve

                u "What about an extra ten bucks?"

                scene v15s24_13k
                with dissolve

                cashier "I wouldn't even wipe my ass with your ten extra bucks."

                cashier "You think I want to risk my job and sell to an underage kid? Ha..."

                cashier "I'd be done for, and you're not worth it. Get out."

                scene v15s24_13l
                with dissolve

                u "*Sighs* Right... Sorry."

                scene v15s24_17
                with dissolve

                pause 0.75

                if kct == "popular":
                    call screen kct_popup
                    $ v15_lindsey_alcohol = True

                    scene v15s24_17
                    with vpunch

                    cashier "Ugh, wait..."

                    scene v15s24_13a
                    with dissolve

                    u "Huh?"

                    scene v15s24_13
                    with dissolve

                    cashier "Maybe I spoke too soon."

                    scene v15s24_13a
                    with dissolve

                    u "What do you mean?"

                    scene v15s24_13
                    with dissolve

                    cashier "Make it thirty extra and we've got a deal."

                    scene v15s24_13a
                    with dissolve

                    u "Ha. Really?"

                    scene v15s24_13
                    with dissolve

                    cashier "Just don't send any of your acne-infested friends in here thinking they'll get the same treatment, got it?"

                    scene v15s24_13a
                    with dissolve

                    u "Yeah, of course. Whatever you say!"

                    scene v15s24_18
                    with dissolve

                    pause 0.75

                    scene v15s24_18a
                    with dissolve

                    pause 0.75

                    scene v15s24_16d
                    with dissolve

                    pause 0.75

                    scene v15s24_13o
                    with dissolve

                    pause 0.75

                    scene v15s24_13a
                    with dissolve

                    u "Thank you so much... This is great."

                    scene v15s24_13
                    with dissolve

                    cashier "Yeah. Good luck growing in that beard, Andrew."

                    scene v15s24_13a
                    with dissolve

                    u "*Chuckles* Thanks."
    
    if v15_lindsey_alcohol:
        scene v15s24_8a # TPP. Show MC exiting the store with a bag of alcohol, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s24_5
        with dissolve

        u "One bag of alcohol for the pretty lady."

        scene v15s24_7d # TPP. MC handing Lindsey the bag of Alcohol, Lindsey grabbing the back, both slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s24_5a
        with dissolve

        li "Oh my god, it worked! You did it!"

        if lindsey.relationship.value >= Relationship.FWB.value: 
            play sound "sounds/kiss.mp3"

            scene v15s24_5i
            with dissolve

            pause 1.75 

            scene v15s24_5d
            with dissolve

            pause 0.75

        else: 
            scene v15s24_7e # TPP. Lindsey hugging MC, The alcohol bag in her hand as she hugs MC, both slight smile, mouth closed.
            with dissolve

            pause 0.75

        scene v15s24_5
        with dissolve

        u "I did. Barely. *Laughs*"

        scene v15s24_5a
        with dissolve

        li "You're amazing."

        scene v15s24_5
        with dissolve

        u "You only just realized that?"

        scene v15s24_7f # TPP. Lindsey slight nudging MC on the arm, both slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s24_5a
        with dissolve

        li "This is so perfect. I can't wait to make some killer cocktails for everyone!"

        scene v15s24_5
        with dissolve

        u "We've also got some new candy."

        scene v15s24_5a
        with dissolve

        li "Wait, Condy's?"

        scene v15s24_5
        with dissolve

        u "Yeah, that's what they are. Have you tried them?"

        scene v15s24_5a
        with dissolve

        li "*Chuckles* No, not yet..."

        li "I've heard they can really fuck you up though. They make you feel twenty different emotions all at once."

        scene v15s24_5
        with dissolve

        menu:
            "That sounds amazing":
                u "That sounds amazing...?"

                scene v15s24_5a
                with dissolve

                li "And also kind of terrifying... Haha."

                li "Can't wait. *Laughs*"

            "Is that a good thing?":
                u "Is that a good thing?"

                scene v15s24_5a
                with dissolve

                li "Are you kidding me? Of course it is!"

                li "Can't wait. *Laughs*"

    else:
        scene v15s24_8b # TPP. Show MC exiting the store empty handed, MC slight frown, mouth closed.
        with dissolve

        pause 0.75

        scene v15s24_5
        with dissolve

        u "I'm sorry, Linds... *Sighs*"

        scene v15s24_5j # FPP. # FPP. MC and Lindsey on the side of the store, MC looking at Lindsey, Lindsey looking at MC, Lindsey slight frown, mouth open.
        with dissolve

        li "Oh no! What happened?"

        scene v15s24_5k # FPP. MC and Lindsey on the side of the store, MC looking at Lindsey, Lindsey looking at MC, Lindsey slight frown, mouth closed
        with dissolve

        u "That guy is like a brick wall. He wouldn't listen to me, no matter what I said."

        scene v15s24_5j
        with dissolve

        li "Really? Ugh... This sucks."

        li "Well, I guess we'll be having mocktails instead."

        scene v15s24_5k
        with dissolve

        u "Mocktails?"

        scene v15s24_5j
        with dissolve

        li "Cocktails without alcohol, haha. Still fun I guess, but no buzz."

        scene v15s24_5k
        with dissolve

        u "Damn, I'm sorry I let you down."

        scene v15s24_5a
        with dissolve

        li "Oh, don't worry about it. I'm sure you did your best."

        li "Besides, those IDs were pretty shit, which didn't help us."

        scene v15s24_5
        with dissolve

        u "Ha, very true. Thanks for not being upset."

        scene v15s24_5a
        with dissolve

        li "You're taking time out of your day to help me, I couldn't be upset that you tried."

        scene v15s24_5
        with dissolve

        u "You're amazing."

        scene v15s24_5a
        with dissolve

        li "Yes. Yes, I am. *Giggles*"

    play sound "sounds/vibrate.mp3"

    scene v15s24_19 # TPP. Just MC on the side of the store pulling his phone out of his pocket, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s24_19a # TPP. Just Mc on the side of the store looking at his phone, slight smile, mouth closed.
    with dissolve

    pause 0.75

    $ aubrey.messenger.newMessage("Come to the Chicks house, asap! I have an extra special surprise for you. I think you've earned it ;)", queue=False)

    if aubrey.relationship.value >= Relationship.FWB.value: #if RS or Tamed 
        $ aubrey.messenger.addReply("Ooh, Is it a naked surprise? ;)", func=None)
        $ aubrey.messenger.newMessage("Haha, you'll have to come find out. Hurry up!", queue=False)

    else:
        $ aubrey.messenger.addReply("Ooh, okay. See you soon.", func=None)

    label v15s24_PhoneContinue:
    if aubrey.messenger.replies:
        call screen phone
    if aubrey.messenger.replies:
        u "(I should reply to Aubrey)"
        jump v15s24_PhoneContinue

    scene v15s24_19b # TPP. MC on the side of the store putting his phone away, slight smile, mouth closed.
    with dissolve

    u "(I wonder what the surprise could be... Only one way to find out!)"

    scene v15s24_5a
    with dissolve

    li "Are you being summoned? Haha."

    scene v15s24_5
    with dissolve

    u "Yeah, looks like I'm needed elsewhere."

    scene v15s24_5a
    with dissolve

    li "You're just a helpful kind of guy, huh?"

    scene v15s24_5
    with dissolve

    u "Mmm, yeah. That's me."

    if v15_lindsey_alcohol:
        $ lindsey_board.money -= 100
        scene v15s24_5a
        with dissolve

        li "Okay, have fun. I'll see you soon, yeah? Thanks again."

        scene v15s24_5
        with dissolve

        u "Yeah, no problem! See you later."

        scene v15s24_20 # FPP. MC watching Lindsey walk off with the bag of alcohol, Lindsey slight smile, mouth closed.
        with dissolve

        pause 0.75

    else:
        scene v15s24_5a
        with dissolve

        li "Well, good luck with whatever it is."

        li "I need to go practice making mocktails, ha. Thanks again for trying, [name]."
        li "At least we saved some money."

        scene v15s24_5
        with dissolve

        u "Of course. I'll see you later, Linds."

        scene v15s24_20a # FPP. MC watching Lindsey walk off empty handed, Lindsey neutral face, mouth closed.
        with dissolve

pause 0.75

jump v15s26
