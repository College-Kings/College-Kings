# SCENE 25: Limousine & Private Club Price Haggling
# Locations: MC Wolves/Apes room, Booking Admin reception desk.
# Characters: MC (Outfit: 9), BOOKING ADMIN (Outfit: 1)
# Time: Morning

label v15s25:
    if joinwolves:
        play sound "sounds/dooropen.mp3"

        scene v15s25_1 # TPP. Show MC entering his Wolves frat room, slight smile, mouth closed.
        with dissolve

        pause 0.75

        play sound "sounds/doorclose.mp3"

        scene v15s25_2 # TPP. Show MC sitting at his study desk in his Wolves frat room, slight smile, mouth closed.
        with dissolve

        u "(Okay, now I'm in my office, time to make some business calls, haha.)"

        scene v15s25_3 # TPP. Show MC pulling out his phone from his pocket in his wolves frat room.
        with dissolve

        pause 0.75

        scene v15s25_2a # TPP. MC sitting at his study desk in his Wolves frat room pressing a button on his phone, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s25_2b # TPP. MC sitting at his study desk with his phone to his ear in his wolves frat room, slight smile, mouth closed.
        with dissolve
        
        pause 0.75

    else:
        play sound "sounds/dooropen.mp3"

        scene v15s25_4 # TPP. Show MC entering his apes frat room, slight smile, mouth closed.
        with dissolve

        pause 0.75

        play sound "sounds/doorclose.mp3"

        scene v15s25_5 # TPP. Show MC sitting at his study desk in his apes frat room, slight smile, mouth closed.
        with dissolve

        u "(Okay, now I'm in my office, time to make some business calls, haha.)"

        scene v15s25_6 # TPP. Show MC pulling out his phone from his pocket in his apes frat room.
        with dissolve

        pause 0.75

        scene v15s25_5a # TPP. MC sitting at his study desk in his apes frat room pressing a button on his phone, slight smile, mouth closed.
        with dissolve

        pause 0.75

        play sound "sounds/ring.mp3"

        scene v15s25_5b # TPP. MC sitting at his study desk with his phone to his ear in his apes frat room, slight smile, mouth closed.
        with dissolve
        
        pause 0.75

    scene v15s25_7 # TPP. Split Screen. First side, MC phone to ear sitting in an office chair only other thing in the shot a plain wall behind him, MC slight smile, mouth closed. Second side, Booking admin(Lady in her 20s, wearing glasses, hair tied back, white button up, headset on for calls.) at her reception desk, slight smile, mouth open.
    with dissolve

    admin "Hi, this is VIP bookings for the Mango Lounge. How can I help you?"

    scene v15s25_7a # TPP. Split Screen. First side, MC on the phone in the chair, slight smile, mouth open. Second side, Booking admin at her desk, slight smile, mouth closed.
    with dissolve

    u "Hi, yeah... Can I book the VIP party package, please?"

    scene v15s25_7
    with dissolve

    admin "That's a lot of P's, isn't it? *Giggles*"

    scene v15s25_7a
    with dissolve

    u "Haha, it is."

    scene v15s25_7
    with dissolve

    admin "What's your name?"

    scene v15s25_7a
    with dissolve

    u "[name]."

    scene v15s25_7
    with dissolve

    admin "When do you want to book it? And for how many people?"

    scene v15s25_7a
    with dissolve

    u "Tomorrow evening. There's five of us."

    scene v15s25_7
    with dissolve

    admin "Perfect. I've reserved a VIP area for you, and we'll send our finest limo so that you can all arrive in style."

    scene v15s25_7a
    with dissolve

    u "Sounds great!"

    scene v15s25_7
    with dissolve

    admin "I also need to ask, how old are the people in your group?"

    scene v15s25_7b # TPP. Split Screen. First side, MC on the phone in the chair, slight smile, mouth closed. Second side, Booking admin at her desk, slight smile, mouth closed.
    with dissolve

    u "(Damn, she's asking because we want to get drunk!)"

    menu:
        "Be honest":
            u "(Not everyone will have a fake ID. I need to be honest.)"

            scene v15s25_7a
            with dissolve

            u "We're all under twenty-one."

            scene v15s25_7
            with dissolve

            admin "Ooh... Well, in that case, we can't serve you the alcohol."

        "Lie":
            scene v15s25_7a
            with dissolve

            u "We're all twenty-one."

            scene v15s25_7
            with dissolve

            admin "Great! I must point out that even if one of you is underage, we won't be allowed to serve the alcohol."

            admin "But you're all twenty-one, so there's nothing to worry about!"

            scene v15s25_7b
            with dissolve

            u "(Yes... Right...)"

            scene v15s25_7
            with dissolve

            admin "Of course, we'll be checking your IDs when you arrive."

            scene v15s25_7c # TPP. Split Screen. First side, MC on the phone in the chair, neutral face, mouth open. Second side, Booking admin at her desk, slight smile, mouth closed.
            with dissolve

            u "Oh- Shit, really?"

            scene v15s25_7d # TPP. Split Screen. First side, MC on the phone in the chair, neutral face, mouth closed. Second side, Booking admin at her desk, slight smile, mouth open.
            with dissolve

            admin "Yes, It's standard procedure."

            scene v15s25_7e # TPP. Split Screen. First side, MC on the phone in the chair, neutral face, mouth closed. Second side, Booking admin at her desk, slight smile, mouth closed.
            with dissolve

            u "(Fuck... There's no way everyone has a fake ID.)"

            scene v15s25_7c
            with dissolve

            u "Sorry, I think you misheard me. I said we're not all twenty-one."

            scene v15s25_7d
            with dissolve

            admin "Oh, I'm pretty sure you said you were all-"

            scene v15s25_7a
            with dissolve

            u "Nope."

            scene v15s25_7
            with dissolve

            admin "Okay... Well, if you're underage then we won't be able to serve you alcohol."

    scene v15s25_7a
    with dissolve

    u "Yeah, I understand. It's just that..."

    u "Is there any way at all that we can get alcohol?"

    scene v15s25_7
    with dissolve

    admin "The policy is very strict, sir. I'm sorry."

    scene v15s25_7b
    with dissolve

    u "(Going to have to convince her somehow.)"

    scene v15s25_7a
    with dissolve

    u "Here's the thing..."

    menu:
        "It's important for us":

            u "It's an important night for us."

            scene v15s25_7
            with dissolve

            admin "Mhmm..."

            scene v15s25_7a
            with dissolve

            u "We have a presidential election going on at college and, if all goes well, this will help win votes with some influential people."

            scene v15s25_7
            with dissolve

            admin "That sounds great, honey... But if you're underage, we can't serve you alcohol. It's as simple as that."

            scene v15s25_7a
            with dissolve

            u "It's for my friend Lindsey, you see? I'm just trying to do everything I can to help her out."

            menu: 
                "She deserves to be president":

                    u "She really deserves to be president, she could really elevate the lives of everyone in her sorority."

                    scene v15s25_7
                    with dissolve

                    $ set_presidency_percent(v14_lindsey_popularity - 3)

                    admin "And I'm sure she will, but there's a legal drinking age. I'm sorry, there's nothing I can do."

                "Her mom passed away recently":
                    $ v15_lindsey_alcohol = True
           
                    u "Her mom passed away recently, and she's putting so much effort into her presidential campaign."

                    scene v15s25_7f # TPP. Split Screen. First side, MC on the phone in the chair, slight smile, mouth open. Second side, Booking admin at her desk, slight frown, mouth closed.
                    with dissolve

                    u "It's like she's doing it all for her mom, you know. And I don't want to let her down..."

                    scene v15s25_7g # TPP. Split Screen. First side, MC on the phone in the chair, neutral face, mouth closed. Second side, Booking admin at her desk, teary eyes, slight frown, mouth open.
                    with dissolve

                    admin "Oh... That's so sweet. *Sniffles* Bless her heart."

                    admin "I lost my mom last year, so I know exactly how she feels."

                    scene v15s25_7h # TPP. Split Screen. First side, MC on the phone in the chair, neutral, mouth open. Second side, Booking admin at her desk, wiping her eyes, slight smile, mouth closed.
                    with dissolve

                    u "Oh, I'm sorry for your loss."

                    scene v15s25_7
                    with dissolve

                    admin "*Clears throat* Mhmm, yes. Thank you."

                    admin "When my mom passed, I kept productive with some new hobbies, and it really helped. Sounds like your friend is doing the same."

                    scene v15s25_7a
                    with dissolve

                    u "Yeah, she's stronger than she appears. That's for sure."

                    scene v15s25_7
                    with dissolve

                    admin "Okay..."

                    admin "Listen, I'm not supposed to do this, but..."

                    $ set_presidency_percent(v14_lindsey_popularity + 3)

                    admin "I'll just leave this little tick box unchecked... So that you guys get some alcohol, and nobody checks your IDs, okay?"

                    scene v15s25_7a
                    with dissolve

                    u "That would be amazing! I-"

                    scene v15s25_7
                    with dissolve

                    admin "But please, be on your best behavior tomorrow night."

                    scene v15s25_7a
                    with dissolve

                    u "Don't worry, we're all very mature for our age."

                    scene v15s25_7
                    with dissolve

                    admin "You do sound mature for your age, so I think I can trust you."

                    scene v15s25_7a
                    with dissolve

                    u "You can, I promise. Thank you so much, you're incredible"

                    scene v15s25_7
                    with dissolve

                    admin "Let's just call it my good deed for the day, haha."

        "Disagree with the policy":

            u "I think you should check state legislation about the legal drinking age."

            scene v15s25_7
            with dissolve

            admin "Ha! Yeah?"

            scene v15s25_7a
            with dissolve

            u "Yeah. Underage people can drink as long as it remains under a certain amount."

            scene v15s25_7
            with dissolve

            admin "I don't think that's true."

            scene v15s25_7a
            with dissolve

            u "It says so on the internet, lady!"

            u "Legally speaking, we can have a couple of drinks, and then let's just see how the evening goes. How does that sound?"

            scene v15s25_7
            with dissolve

            admin "It sounds illegal, sir. And the internet isn't a trustworthy source of information, I'm sorry."

            scene v15s25_7a
            with dissolve

            u "How so?"

            scene v15s25_7
            with dissolve

            $ set_presidency_percent(v14_lindsey_popularity - 3)

            admin "False claims and not fact-checking can lead to dangerous mistakes."

            admin "Maybe you should do some more research, so you fully understand the law."

            scene v15s25_7b
            with dissolve

            u "(Dammit, she's too smart for me.)"

    if v15_lindsey_alcohol:
        scene v15s25_7
        with dissolve

        admin "So, the full party package is eight-hundred dollars. You'll need to pay as soon as you arrive."

        scene v15s25_7b
        with dissolve

        menu:
            "Accept the price":
                $ lindsey_board.money -= 800
                scene v15s25_7a
                with dissolve

                u "Just to confirm, this price includes the limo, the VIP booth, and alcohol?"

                scene v15s25_7
                with dissolve

                admin "Yeah, that's right. It's the full VIP party package."

                scene v15s25_7a
                with dissolve

                u "Okay, great. Sounds good."

                scene v15s25_7
                with dissolve

                admin "Perfect! All that's left for me to say is, thanks for choosing the Mango Lounge VIP party package! Have a great day!"

                scene v15s25_7a
                with dissolve

                u "You too! Bye."

            "Negotiate":
                scene v15s25_7a
                with dissolve

                u "Eight hundred seems a little steep..."

                scene v15s25_7
                with dissolve

                admin "It's the VIP party package. It's only designed for people who can afford the VIP lifestyle."

                scene v15s25_7b
                with dissolve

                menu:
                    "Be honest":
                        $ lindsey_board.money -= 400
                        scene v15s25_7a
                        with dissolve

                        u "I totally understand that, and we really want the VIP party package experience."

                        u "I was just hoping you could offer us a little discount."

                        scene v15s25_7
                        with dissolve

                        admin "Well..."

                        admin "The owner does sometimes offer an exclusive discount to his rich friends..."

                        admin "I think it would be nice if that sort of generosity was spread about a little more."

                        admin "What about a 50\% discount?"

                        scene v15s25_7a
                        with dissolve

                        u "That would be amazing! Thanks!"

                        scene v15s25_7
                        with dissolve

                        admin "I like the thought of making your friend happy after everything that's happened."

                        admin "I really hope it's a special night for her."

                        scene v15s25_7a
                        with dissolve

                        u "This is going to make her so happy!"

                        scene v15s25_7
                        with dissolve

                        admin "Aww, good. I'm glad. It'll help take her mind off things."

                        scene v15s25_7a
                        with dissolve

                        u "It will. She really needs it."

                        scene v15s25_7
                        with dissolve

                        admin "Goodbye then."

                        scene v15s25_7a
                        with dissolve

                        u "Bye!"

                    "Lie":
                        $ lindsey_board.money -= 800
                        scene v15s25_7a
                        with dissolve

                        u "But my uncle usually gives me the VIP package for free."

                        scene v15s25_7i # TPP. Split Screen. First side, MC on the phone in the chair, slight smile, mouth closed. Second side, Booking admin at her desk, confused, mouth open.
                        with dissolve

                        admin "Your uncle?"

                        scene v15s25_7j # TPP. Split Screen. First side, MC on the phone in the chair, slight smile, mouth open. Second side, Booking admin at her desk, confused, mouth closed.
                        with dissolve

                        u "Yeah, my uncle. The owner."

                        scene v15s25_7i
                        with dissolve

                        admin "Really?"

                        scene v15s25_7j
                        with dissolve

                        u "Yeah. So, can you just... You know, waive the fee?"

                        scene v15s25_7
                        with dissolve

                        admin "Um, no. I would have to believe you first. And I don't."

                        scene v15s25_7a
                        with dissolve

                        u "Well, don't blame me when you get into trouble over this."

                        scene v15s25_7
                        with dissolve

                        admin "I'll take my chances."

                        admin "So, eight-hundred dollars is the total."

                        scene v15s25_7a
                        with dissolve

                        u "...Okay. I'm sure I can get the money back after we resolve this confusion."

                        scene v15s25_7
                        with dissolve

                        admin "You can certainly try."

                        admin "I'm glad we got there in the end. Thanks for your custom."

                        scene v15s25_7a
                        with dissolve

                        u "Yeah, thanks."

                        scene v15s25_7
                        with dissolve

                        admin "Goodbye."

                        scene v15s25_7a
                        with dissolve

                        u "Bye."

    else:
        scene v15s25_7
        with dissolve

        admin "So, for the full VIP party package, without alcohol, that comes to $700. You'll need to pay as soon as you arrive."

        scene v15s25_7b
        with dissolve

        menu:
            "Accept the price":
                $ lindsey_board.money -= 700
                scene v15s25_7a
                with dissolve

                u "Just to confirm, the price includes the limo and the VIP booth?"

                scene v15s25_7
                with dissolve

                admin "Yeah. We can't serve you any alcohol, but you still get a range of mocktails, sodas and juices all included."

                scene v15s25_7a
                with dissolve

                u "Okay, I guess that's the best I'm going to get."

                scene v15s25_7
                with dissolve

                admin "Until you turn 21, it is."

                admin "We'll keep you hydrated. But we won't get you drunk."

                scene v15s25_7a
                with dissolve

                u "Haha, okay, message received."

                scene v15s25_7
                with dissolve

                admin "So that's everything confirmed?"

                scene v15s25_7a
                with dissolve

                u "Yeah. Thanks."

                scene v15s25_7
                with dissolve

                admin "We look forward to seeing you. Goodbye."

                scene v15s25_7a
                with dissolve

                u "Bye."

            "Negotiate":
                scene v15s25_7a
                with dissolve
            
                u "Seven hundred seems overpriced."

                scene v15s25_7
                with dissolve

                admin "It's the VIP party package. If it was cheap, it wouldn't be for VIPs."

                admin "You'll still get to choose from a range of mocktails, sodas and juices, all included in the price."
                
                scene v15s25_7b
                with dissolve

                menu:
                    "Lindsey's mom passed away recently":
                        $ lindsey_board.money -= 500
                        scene v15s25_7h
                        with dissolve

                        u "I understand. I'm just hoping you can offer a discount, even just a small one."
                        u "You see, my friend, Lindsey. It's her night really. I'm just helping her out."

                        u "Her mom passed away recently, and she's been putting so much effort into her presidential campaign at college."
                        u "That's what all this is for, you see."

                        u "And it might sound silly, but it's like she's doing it all for her mom, you know?"

                        scene v15s25_7g
                        with dissolve

                        admin "Oh. Oh, I see."

                        admin "No, it doesn't sound silly. My mom passed away recently too. Bless your friend."

                        scene v15s25_7h
                        with dissolve

                        u "Oh, I'm sorry for your loss."

                        scene v15s25_7
                        with dissolve

                        admin "Aww, thank you."

                        admin "It sounds like your friend's coping well by doing something productive. That definitely helped me."

                        scene v15s25_7a
                        with dissolve

                        u "Yeah, Lindsey's one of the best."

                        scene v15s25_7
                        with dissolve

                        admin "Let's see... Well, I think I can help you out a little bit."

                        admin "I can give you a 25% discount. That brings the price down to $600."

                        scene v15s25_7a
                        with dissolve

                        u "Amazing! Thanks!"

                        scene v15s25_7
                        with dissolve

                        admin "I hope your friend has a wonderful time."

                        scene v15s25_7a
                        with dissolve

                        u "This will help!"

                        u "Would you reconsider giving us alcohol now?"

                        scene v15s25_7
                        with dissolve

                        admin "Haha, I'm sorry, that ship has sailed. I'm sure you'll have a great time regardless."

                        scene v15s25_7a
                        with dissolve

                        u "Worth a try. *Nervous chuckles* Thanks anyway."

                        scene v15s25_7
                        with dissolve

                        admin "You're welcome. Goodbye."

                        scene v15s25_7a
                        with dissolve

                        u "Bye."

                    "Ask about student discounts":
                        $ lindsey_board.money -= 700
                        scene v15s25_7a
                        with dissolve

                        u "What about a student discount?"

                        scene v15s25_7i
                        with dissolve

                        admin "We're a lounge, we don't get that many students."

                        scene v15s25_7j
                        with dissolve

                        u "Well that's probably cause of your lack of discounts."

                        scene v15s25_7i
                        with dissolve

                        admin "Sadly I can't just create new discounts out of thin air. You're going to have to pay full price."

                        scene v15s25_7k
                        with dissolve

                        u "*Sighs* Okay, whatever."

                        u "We'll pay the seven hundred."

                        scene v15s25_7l
                        with dissolve

                        admin "Mhmm. Have a good one, sir."

                        scene v15s25_7k
                        with dissolve

                        u "Yeah... Bye."

    play sound "sounds/rejectcall.mp3"

    scene v15s25_8 # TPP. Just MC sitting in the chair plain wall in the background, MC pressing a button on his phone, MC slight smile, mouth closed.
    with dissolve

    pause 0.75

    $ aubrey.messenger.newMessage("Hey! Come to the Chicks house? I have an extra special surprise for you... I think you've earned it.", force_send=True)

    if aubrey.relationship.value >= Relationship.FWB.value:
        $ aubrey.messenger.addReply("A naked surprise? ;)")
        $ aubrey.messenger.newMessage("Haha you'll find out. Hurry up. I'm waiting :)", force_send=True)

    else:
        $ aubrey.messenger.addReply("Haha okay, see you there.")

    play sound "sounds/vibrate.mp3"

    scene v15s25_8a # TPP. Just MC sitting in the chair plain wall in the background, MC looking at his phone, MC slight smile, mouth closed.
    with dissolve

    u "(Fingers crossed that it's Nora...)"

    label v15s25_PhoneContinueAubrey:
    if aubrey.messenger.replies:
        call screen phone
    if aubrey.messenger.replies:
        u "(I should respond to Aubrey.)"
        jump v15s25_PhoneContinueAubrey

    scene v15s25_8b # TPP. Just MC sitting in the chair plain wall in the background, MC putting his phone away, MC slight smile, mouth open.
    with dissolve

    u "*Sighs* (Still no Nora, but it sounds like Aubrey's got something fun planned for me.)"

    jump v15s26
