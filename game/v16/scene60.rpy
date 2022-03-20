# SCENE 60: Lindsey gets interviewed
# Locations: SVC Hallway, SVC Times Office
# Characters: LINDSEY (Outfit: Business Outfit), MC (Outfit: 2), ELIJAH (Outfit: 1), RILEY (Outfit: 3)
# Time: Thurdsay Afternoon

label v16s60:
    scene v16s60_1 # TPP. Show MC(slight smile, mouth closed) walking down the SVC HALLWAY close to the SVC Times Office.
    with dissolve

    pause 0.75

    scene v16s60_2 # TPP. Show MC(slight smile, mouth closed) approaching the door of the SVC Times Office.
    with dissolve

    li "*Laughs*"

    u "(Wait, what? Lindsey's already in there?)"

    scene v16s60_2
    with dissolve

    menu:
        "Knock on door.":
            $ add_Point(KCT.BRO)

            play sound "sounds/knock.mp3"

            scene v16s60_2a # TPP. Show MC(slight smile, mouth closed) knocking on the SVC Times Office door.
            with dissolve

            li "*Muffled* Oh, that must be [name]."

            li "You can come in!"

        "Shout through door.":
            $ add_Point(KCT.TROUBLEMAKER)

            scene v16s60_2b # TPP. Show MC(slight smile, mouth open) yelling through the closed door.
            with dissolve

            u "Hey, Lindsey, you in there?!"

            scene v16s60_2a
            with dissolve

            li "*Muffled* [name]? *Laughs* Crazy boy."

            li "Come on in!"

    play sound "sounds/dooropen.mp3"

    scene v16s60_3 # TPP. Show MC(slight smile,mouth closed.) opening the door and walking into the SVC Times Office
    with dissolve

    li "[name] is here just to take notes for me, I don't want to miss anything."

    if not v16s28_lindsey_pb_riley_interview:  # Elijah does the interview 

        scene v16s60_4 # FPP. MC looking at Lindsey(slight smile, mouth close) and Elijah (neutral face, mouth closed) sitting across from each other. Lindsey and Elijah both looking at MC.
        with dissolve

        u "You've started the interview already?"

        scene v16s60_4a # FPP. MC looking at Lindsey(slight smile, mouth open) and Elijah (neutral face, mouth closed) sitting across from each other. Lindsey and Elijah both looking at MC.
        with dissolve

        li "No, not yet."

        scene v16s60_4b # FPP. MC looking at Lindsey(slight smile, mouth close) and Elijah (neutral face, mouth open) sitting across from each other. Lindsey and Elijah both looking at MC.
        with dissolve

        el "I like to make sure people are relaxed before I start the interview."

        scene v16s60_4a
        with dissolve

        li "Elijah just showed me the most ridiculous cat video."

        scene v16s60_4
        with dissolve

        u "Oh, yeah?"

        scene v16s60_4a
        with dissolve

        li "There's a cat just sitting there with a bird on its head. And then another cat tries to get the bird, but it flies away."

        li "And then both cats fall into the fish pond. *Laughs* So stupid."

        scene v16s60_4b
        with dissolve

        el "Yeah, I'd show you too, but I can't be bothered to find it again."

        scene v16s60_4
        with dissolve

        u "It's fine. (Cat videos? I hope this is her way of sucking up to the interviewer, ha.)"

        scene v16s60_4b
        with dissolve

        el "Let's get started now. I prefer to make written notes. It's less intrusive."

        scene v16s60_4a
        with dissolve

        li "A true professional. *Giggles*"

        scene v16s60_5 # TPP. Close up of Elijah grabbing his pen and notepad.
        with dissolve

        pause 0.75

        # -Elijah picks up a pen and notepad. MC sits a little further away from them to observe-

        # -The progress bar for Lindsey's popularity appears, and changes depending on her answers-

        # -Whenever Lindsey is talking, Elijah can be writing notes (we never see what he's writing)-

        scene v16s60_6 # FPP. MC sitting to the side observing the interview. Lindsey (slight smile, mouth closed) looking at Elijah (neutral face,mouth open). Elijah looking back at Lindsey.
        with dissolve

        el "Here's an interesting one to start off... What do you admire about your presidential opponent?"

        scene v16s60_6d # FPP. MC sitting to the side observing the interview. Lindsey (slight smile, mouth closed) looking at Elijah(neutral face, mouth closed). Elijah looking at his notepad and writing.
        with dissolve

        u "(Damn, he's trying to unsettle her already)"

        # -if MC did not ask 'Can you say three positive things about your opponent?' or did ask the question and chose Sounds great in Scene 55 (LOSE 1 POPULARITY)
        if "three_positives" not in v16s55_lindsey_question_set or ("three_positives" in v16s55_lindsey_question_set and "sounds_great" in v16s55_lindsey_followup_question_set):

            $ set_presidency_percent(v14_lindsey_popularity - 1)

            scene v16s60_6a # FPP. MC sitting to the side observing the interview. Lindsey (slight smile, mouth open) looking at Elijah(Neutral face, mouth open). Elijah looking down at his notepad and writing (we don't see what he writes)
            with dissolve 

            li "I mean, Chloe looks amazing, doesn't she? She's great to look at with all of her physical... assets."

            li "Oh, and she's good at volleyball."

            scene v16s60_6
            with dissolve

            el "..."

            el "Oh, is that it?"

            scene v16s60_6b # FPP. MC sitting to the side observing the interview. Lindsey (slight smile, mouth open) looking at Elijah(Neutral face, mouth closed). Elijah looking back at Lindsey.
            with dissolve

            li "Um... I think so?"

            scene v16s60_6c # FPP. MC sitting to the side observing the interview. Lindsey(slight smile, mouth closed) looking at Elijah(Neutral face, mouth open). Elijah looking at his Notepad as he writes.
            with dissolve

            el "Okay... Interesting."

            # -if MC asked  'Can you say three positive things about your opponent?' and chose Make a suggestion in Scene 55 (GAIN 1 POPULARITY)
        elif "three_positives" in v16s55_lindsey_question_set and "make_suggestion" in v16s55_lindsey_followup_question_set:

            $ set_presidency_percent(v14_lindsey_popularity + 1)
        
            scene v16s60_6d
            with dissolve

            u "(Come on, you can do it, Linds. We practiced this.)"

            scene v16s60_6a
            with dissolve

            li "I think it's fair to say that we've developed a rivalry, but I still regard Chloe as my friend, and always as my sorority sister."

            li "Even with all the stress of campaigning, she's doing an amazing job. She never gives up, and I admire her for that."

            scene v16s60_6d
            with dissolve

            u "(Vague compliments. I've trained her well, haha.)"

            scene v16s60_6c
            with dissolve

            el "That's nice of you. Good answer."

            scene v16s60_6a
            with dissolve

            li "Thanks. It was a good question. I'm interested to hear what you're going to ask next."

            scene v16s60_6d
            with dissolve

            u "(And she's keeping it moving, controlling the interview. Nicely done!)"

            scene v16s60_6
            with dissolve

            el "I know people are going to want to hear your thoughts on this. Is there a specific quality that you feel every successful president should have?"

            # -if MC did not ask 'What is the most important quality of a good president?' or did ask the question and chose That'll do in Scene 55 (LOSE 1 POPULARITY)
        if "important_quality" not in v16s55_lindsey_question_set or ("important_quality" in v16s55_lindsey_question_set and "thatll_do" in v16s55_lindsey_followup_question_set ):        
            
            $ set_presidency_percent(v14_lindsey_popularity - 1)

            scene v16s60_6a
            with dissolve

            li "I think a good president should be someone who can keep everyone happy, you know?"

            li "Everyone has things they want, and a president should be able to deliver on that."

            scene v16s60_6c
            with dissolve

            el "Well, that would certainly be ideal, but I'm not sure that's a quality. Can you be more specific?"

            scene v16s60_6a
            with dissolve

            li "Um... Like... I don't know..."

            scene v16s60_6d
            with dissolve

            u "(Come on...)"

            scene v16s60_6a
            with dissolve

            li "Like, okay... If someone makes me breakfast and they know that I want blueberries on my pancakes, but the president puts honey on them."

            scene v16s60_6d
            with dissolve

            u "(What is she saying?)"

            scene v16s60_6a
            with dissolve

            li "A good president would know that I don't like honey and want blueberries."

            scene v16s60_6
            with dissolve

            el "So, what you're saying is, a good president should know what you like on your pancakes?"

            scene v16s60_6a
            with dissolve

            li "Yeah. It's a um, what do you call it?"

            scene v16s60_6c
            with dissolve

            el "A food analogy...?"

            scene v16s60_6a
            with dissolve

            li "Yeah, that's it. You're so smart..."

            scene v16s60_6d
            with dissolve

            u "(Clever.)"

            scene v16s60_6c
            with dissolve

            el "Interesting..."
            
            # -if MC asked  'What is the most important quality of a good president?' and chose Expand on that in Scene 55 (GAIN 1 POPULARITY)        
        elif "important_quality" in v16s55_lindsey_question_set and "expand" in v16s55_lindsey_followup_question_set:
            
            $ set_presidency_percent(v14_lindsey_popularity + 1)

            scene v16s60_6a
            with dissolve

            li "I think people skills are an incredibly important quality to have. But to give a more specific reply, I would say a good president needs to be an effective communicator."

            li "Being heard is crucial when talking to many different people, but more importantly, a strong president must be able to listen to the needs of her sisters."

            li "Without effective communication, you can't solve issues or maintain a happy environment."

            scene v16s60_6d
            with dissolve

            u "(Did she prepare that? Holy shit!)"

            scene v16s60_6c
            with dissolve

            el "That was an excellent answer, Lindsey."

            scene v16s60_6a
            with dissolve

            li "Thanks, Elijah."

            scene v16s60_6c
            with dissolve

            el "Very impressive."

        scene v16s60_6
        with dissolve

        el "I think it's important that people know you're a good person. So tell me, have you done anything recently to help someone other than yourself?"


        # -if MC did not ask 'What was your last random act of kindness?' or did ask the question and chose That's good enough in Scene 55 (LOSE 1 POPULARITY)        
        if "random_kindness" not in v16s55_lindsey_question_set or ("random_kindness" inv16s55_lindsey_question_set and "thats_good" in v16s55_lindsey_followup_question_set):

            $ set_presidency_percent(v14_lindsey_popularity - 1)

            scene v16s60_6a
            with dissolve

            li "Oh, that's easy. I donated to the local dog charity."

            scene v16s60_6c
            with dissolve

            el "Because you wanted to look good and secure more votes?"

            scene v16s60_6a
            with dissolve

            li "What? No. I like donating to charity."

            scene v16s60_6c
            with dissolve

            el "So, it wasn't just part of a strategy?"

            scene v16s60_6a
            with dissolve

            li "Of course not. That's horrible."

            # -if MC also chose Let's finish up in Scene 55 (LOSE 1 POPULARITY)
            if "finish_up" in v16s55_lindsey_followup_question_set:

                $ set_presidency_percent(v14_lindsey_popularity - 1 )
            
                scene v16s60_6a
                with dissolve

                li "Don't be a dick, Elijah."

                scene v16s60_6d
                with dissolve

                u "(Fuck! I know he's a dick but don't SAY it, Lindsey...)"

                scene v16s60_6c
                with dissolve

                el "Excuse me?"

                scene v16s60_6a
                with dissolve

                li "Next question."

                scene v16s60_6c
                with dissolve

                el "Ha."

            scene v16s60_6a
            with dissolve

            li "I'm sorry, but I'm not lying to you. I donate to charity out of the kindness of my heart."

            # -if MC asked  'What was your last random act of kindness?' and chose Ask her why in Scene 55 (GAIN 1 POPULARITY)
        elif "random_kindness" in v16s55_lindsey_question_set and "ask_why" in v16s55_lindsey_followup_question_set:

            $ set_presidency_percent(v14_lindsey_popularity + 1)
        
            scene v16s60_6a
            with dissolve

            li "I like to donate to charity whenever I can. I've been doing that ever since I was little."

            scene v16s60_6c
            with dissolve

            el "Oh, what is your favorite charity?"

            scene v16s60_6a
            with dissolve

            li "When I was younger I'd donate my entire allowance to help save the rainforest, haha. Probably that one still."

            scene v16s60_6c
            with dissolve

            el "And what was your most recent act of kindness?"

            scene v16s60_6a
            with dissolve

            li "Oh, I donated to the local dog charity! It just reopened today, and they need all the support they can get."

            li "They help so many dogs that have been abandoned. It's a really great cause, you should mention it in the paper if you aren't already."

            scene v16s60_6c
            with dissolve

            el "Well, that's very commendable of you. I will look into later."

            scene v16s60_6a
            with dissolve

            li "I just believe everyone should do whatever they can to make the world a better place."

            scene v16s60_6c
            with dissolve

            el "People will love hearing that."

        scene v16s60_6
        with dissolve

        el "Okay, I think I have enough for the article. Thanks, Lindsey."

        scene v16s60_6e # FPP. MC sitting to the side observing the interview. Lindsey (slight smile, mouth open.) looking at Elijah(neutral face, mouth closed). Elijah looking back at Lindsey.
        with dissolve

        li "Oh, no. Thank you, Elijah. I really appreciated this, I'm excited."

        scene v16s60_7 # TPP. Show MC (slight smile, mouth closed), lindsey(slight smile, mouth closed), and Elijah(neutral face, mouth closed.) all standing up from their seats in the room.
        with dissolve
        
        # -if MC chose More advice in Scene 55 (GAIN 1 POPULARITY)
        if "more_advice" in v16s55_lindsey_followup_question_set: 

            $ set_presidency_percent(v14_lindsey_popularity + 1)
    
            # -Lindsey gives Elijah a nice hug. Coming out of the hug, she squeezes his arm muscle-

            scene v16s60_8 # TPP. Close up of Lindsey(slight smile, mouth closed) giving Elijah(confused face,mouth closed.) a hug.
            with dissolve 

            pause 0.75

            scene v16s60_8a # TPP. Close up of Lindsey(slight smile, mouth open.) releasing from the hug and slightly touching Elijahs (confused, mouth closed) arm.
            with dissolve 

            li "Oh, wow, do you work out?"

            scene v16s60_9 # FPP. MC looking at Lindsey(slight smile, mouth closed) standing infront of Elijah(confused, mouth open.)
            with dissolve

            el "Um... Not really. Unless you count moving chess pieces as weightlifting, haha."

            scene v16s60_9a # FPP. MC looking at Lindsey(slight smile, mouth open) standing infront of Elijah(slight smile, mouth closed)
            with dissolve

            li "Well... Whatever you're doing, it's working."

            li "Let's grab a coffee sometime."

            scene v16s60_9b # FPP. MC looking at Lindsey(slight smile, mouth closed.) standing infront of Elijah(slight smile, mouth open)
            with dissolve

            el "Oh, okay... S-sure. That would be g-great!"

            scene v16s60_9c # FPP. MC looking at Lindsey(slight smile, mouth closed) standing infront of Elijah(slight smile, mouth closed)
            with dissolve

            u "(And there's the flirting that I suggested... She's a natural. *Laughs*)"
        scene v16s60_9a
        with dissolve

        li "Thanks again, Elijah. I'm really looking forward to reading the article."

        scene v16s60_9b
        with dissolve

        el "I promise you; it's going to be great."

        play sound "sounds/dooropen.mp3"

        scene v16s60_10 # TPP. Show MC(slight smile, mouth closed) and Lindsey(slight smile, mouth closed) leaving the SVC Times Office. Elijah(slight smile, mouth closed) behind them watching them leave.
        with dissolve
    else:
        scene v16s60_4c # FPP. MC looking at Lindsey(slight smile, mouth closed) and Riley (slight smile, mouth open) sitting across from each other. Lindsey and Riley both looking at MC.
        with dissolve

        ri "Hey, [name]."

        scene v16s60_4d # FPP. MC looking at Lindsey(slight smile, mouth closed) and Riley (slight smile, mouth closed) sitting across from each other. Lindsey and Riley both looking at MC.
        with dissolve

        u "Hey. Have you already started the interview?"

        scene v16s60_4e # FPP. MC looking at Lindsey(slight smile, mouth open) and Riley (slight smile, mouth closed) sitting across from each other. Lindsey and Riley both looking at MC. 
        with dissolve

        li "No, not yet. I just got here."

        scene v16s60_4c
        with dissolve

        ri "She sat down and almost fell off the chair! *Laughs*"

        scene v16s60_4e
        with dissolve

        li "*Laughs* So embarrassing. I think I've had too many coffees."

        scene v16s60_4d
        with dissolve

        u "Haha, at least you'll be alert for the interview."

        scene v16s60_4c
        with dissolve

        ri "Yeah, let's get serious now. I really want to get something good for the first edition."

        scene v16s60_4e
        with dissolve

        li "Me too."

        scene v16s60_5a # TPP. Close up of Riley's hand grabbing her pen and notepad.
        with dissolve

        # -Riley grabs a pen and notepad. MC sits a little further away from them to observe-

        # -The progress bar for Lindsey's popularity appears, and changes depending on her answers-

        # -Whenever Lindsey is talking, Riley can be writing notes (we never see what she's writing)-
        
        scene v16s60_11 # FPP. MC sitting to the side observing the interview. Lindsey (slight smile, mouth closed) looking at Riley (slight smile, mouth open). Riley looking back at Lindsey.
        with dissolve

        ri "Okay, here's an interesting one. What do you admire about your presidential opponent?"

        scene v16s60_11a # FPP. MC sitting to the side observing the interview. Lindsey(slight smile, mouth closed) looking at Riley (slight smile, mouth closed). Riley looking back at Lindsey.
        with dissolve

        u "(Keep it friendly, Linds.)"

        # -if MC did not ask 'Can you say three positive things about your opponent?' or did ask the question and chose Sounds great in Scene 55 (LOSE 1 POPULARITY)
        
        if "three_positives" not in v16s55_lindsey_question_set or ("three_positives" in v16s55_lindsey_question_set and "sounds_great" in v16s55_lindsey_followup_question_set):

            $ set_presidency_percent(v14_lindsey_popularity - 1)

            scene v16s60_11b # FPP. MC sitting to the side observing the interview. Lindsey (slight smile, mouth open) looking at Riley(slight smile, mouth closed). Riley looking at her notepad and writing.
            with dissolve

            li "What do I admire about Chloe? As her rival, can I really say nice things about her and mean it? *Chuckles*"

            scene v16s60_11
            with dissolve

            ri "Why don't you try, you know, for the article?"

            scene v16s60_11b
            with dissolve

            li "Okay, well... She's clearly hot. I mean, I admire her looks, if I can say that."

            li "Um... And she's really good at volleyball, so it helps her keep in good shape."

            scene v16s60_11c # FPP. MC sitting to the side observing the interview. Lindsey(slight smile,mouth closed) looking at Riley(slight smile,mouth open). Riley looking at her Notepad and writing.
            with dissolve

            ri "Anything else?"

            scene v16s60_11b
            with dissolve

            li "Um... Nothing comes to mind, sorry."

            scene v16s60_11c
            with dissolve

            ri "Okay, I guess that's something I can work with."

            scene v16s60_11d # FPP. MC sitting to the side observing the interview. Lindsey(slight smile, mouth closed) looking at Riley(slight smile, mouth closed) Riley looking at her Notepad and writing
            with dissolve

            u "(Damn, maybe I should've trained her better. But hindsight's 20/20!)"


        # -Riley takes a further moment writing-
        elif "three_positives" in v16s55_lindsey_question_set and "make_suggestion" in v16s55_lindsey_followup_question_set:

            # -if MC asked  'Can you say three positive things about your opponent?' and chose Make a suggestion in Scene 55 (GAIN 1 POPULARITY)
            $ set_presidency_percent(v14_lindsey_popularity + 1)

            scene v16s60_11b
            with dissolve

            li "Chloe's a great opponent, I have to say. I still look at her as my friend, my sorority sister."

            li "I admire her for the amazing job she's doing, it's not easy to be challenged for the presidency like this."

            scene v16s60_11d
            with dissolve

            u "(Well said!)"

            scene v16s60_11c
            with dissolve

            ri "It's really nice to hear you say that, Lindsey."
            # -Riley takes a further moment writing-

            scene v16s60_11d
            with dissolve

            pause 0.75

            scene v16s60_11b
            with dissolve
        
            li "Thanks, Riley. It was a great question, hehe."

        scene v16s60_11
        with dissolve

        ri "I'm interested to know, is there a specific quality that you feel every successful president should have?"

    # -if MC did not ask 'What is the most important quality of a good president?' or did ask the question and chose That'll do in Scene 55 (LOSE 1 POPULARITY)
        if "important_quality" not in v16s55_lindsey_question_set or ("important_quality" in v16s55_lindsey_question_set and "thatll_do" in v16s55_lindsey_followup_question_set ):        

            $ set_presidency_percent(v14_lindsey_popularity - 1)

            scene v16s60_11b
            with dissolve

            li "A good president should be able to keep everyone happy. I think that's a basic quality. Chloe hasn't managed to do that, unfortunately."

            scene v16s60_11c
            with dissolve

            ri "Excuse me for saying this, but that sounds a bit generic. Can you specify? How do you keep everyone happy?"

            scene v16s60_11b
            with dissolve

            li "Um... Just, like... get to know people and learn about what they want?"

            li "And Chloe's just not good at that. It's pretty straight forward. I don't know how else to explain it."

            scene v16s60_11c
            with dissolve

            ri "Okay... That's fine."

            ri "So, nothing else to add there?"

            scene v16s60_11b
            with dissolve

            li "Not really. I feel like I've answered that as best I can."

            scene v16s60_11d
            with dissolve

            # -Riley takes a further moment writing-

            u "(I don't think Riley was too impressed with that answer...)"

        elif "important_quality" in v16s55_lindsey_question_set and "expand" in v16s55_lindsey_followup_question_set:

            # -if MC asked  'What is the most important quality of a good president?' and chose Expand on that in Scene 55 (GAIN 1 POPULARITY)
            $ set_presidency_percent(v14_lindsey_popularity + 1)

            scene v16s60_11b
            with dissolve 

            li "Oh, it's people skills. You have to have great people skills as a president. To be even more specific, you need to be an effective communicator."

            li "You need to understand what people want in order to meet their needs. And also, it's really important that people feel heard."

            scene v16s60_11c
            with dissolve

            ri "And why?"

            scene v16s60_11b
            with dissolve

            li "Maybe someone is concerned about an issue on campus, and they talk to you about it. When you act to resolve the issue, they feel heard, and you earn their trust."

            scene v16s60_11c
            with dissolve

            ri "Wow, perfect. *Chuckles*"

            scene v16s60_11b
            with dissolve

            # -Riley takes a further moment writing-

            li "Thanks, Riley."

            scene v16s60_11d
            with dissolve

            u "(What can I say? She had an incredible teacher, haha.)"

        scene v16s60_11
        with dissolve 

        ri "This is quite a nice one, to show people your kind side. Have you done anything recently to help someone other than yourself?"

    # -if MC did not ask 'What was your last random act of kindness?' or did ask the question and chose That's good enough in Scene 55 (LOSE 1 POPULARITY)
        if "random_kindness" not in v16s55_lindsey_question_set or ("random_kindness" inv16s55_lindsey_question_set and "thats_good" in v16s55_lindsey_followup_question_set):
            
            $ set_presidency_percent(v14_lindsey_popularity - 1)

            scene v16s60_11b
            with dissolve

            li "Most recently, I donated to the local dog charity."

            scene v16s60_11c
            with dissolve

            ri "Oh, that's sweet!"

            scene v16s60_11b
            with dissolve

            li "Yeah. I mean, who doesn't love dogs?"

            scene v16s60_11c
            with dissolve

            ri "Cats don't like dogs, generally speaking, haha."

            ri "And to be honest... If I had to choose, I prefer cats."

            scene v16s60_11b
            with dissolve

            li "I'm not a big fan of cats. They're too... self-important? Ha. They don't care about their owners like dogs do."

            scene v16s60_11c
            with dissolve

            ri "I disagree. They're independent for sure, that's what I like about them."

        # -if MC also chose Let's finish up in Scene 55 (LOSE 1 POPULARITY)
            if "finish_up" in v16s55_lindsey_followup_question_set:

                $ set_presidency_percent(v14_lindsey_popularity - 1)

                scene v16s60_11b
                with dissolve 

                li "But dogs are so much better! Cats are dumb."

                scene v16s60_11e # FPP. MC sitting to the side observing the interview. Lindsey (slight smile, mouth closed) looking at Riley (upset, mouth closed)
                with dissolve

                u "(Stop shitting on cats, Lindsey!)"

                scene v16s60_11f # FPP. MC sitting to the side observing the interview. Lindsey (slight smile, mouth closed) looking at Riley (upset, mouth open.)
                with dissolve

                ri "And dogs aren't? *Scoffs*"

                ri "My mom breeds cats, some of them being award winners."

                ri "I've been around them my whole life and I can say they're some of the smartest creatures on the planet."

                scene v16s60_11e
                with dissolve

                u "(Well, Lindsey's just managed to insult Riley, her mother, and her mother's cats. Fuck.)"

            scene v16s60_11g # FPP. MC sitting to the side observing the interview. Lindsey (slight smile, mouth open) looking at Riley (rolling her eyes, neutral face, mouth closed). Riley looking and writing in her notepad.
            with dissolve

            # -Riley takes a further moment writing-

            li "Well, let's just agree to disagree then."

            # -if MC asked  'What was your last random act of kindness?' and chose Ask her why in Scene 55 (GAIN 1 POPULARITY)
        elif "random_kindness" in v16s55_lindsey_question_set and "ask_why" in v16s55_lindsey_followup_question_set:

            $ set_presidency_percent(v14_lindsey_popularity + 1)

            scene v16s60_11b
            with dissolve

            li "I've always donated to charity, ever since I was a little kid. I'd donate my allowance to things like saving the rainforest."

            scene v16s60_11c
            with dissolve

            ri "Aw, that's so cute."

            ri "What was the most recent one then?"

            scene v16s60_11b
            with dissolve

            li "I donated to the local dog charity. I feel so sad when I see all the dogs in there that've been abandoned, so I like to donate whenever I can."

            li "Everyone should help out, even if they can only send a dollar. That dollar helps keep the dogs safe and well-fed."

            scene v16s60_11c
            with dissolve

            ri "I love that! This is going to look great in the article."

            scene v16s60_11d
            with dissolve

            u "(What a reply! I've sculpted her into a master interviewee, haha!)"

        scene v16s60_11c
        with dissolve

        ri "Okay, I think that's enough for the article. Thanks for the interview, Lindsey."

        scene v16s60_11b
        with dissolve

        li "Thanks, Riley. It was fun."

        scene v16s60_7a # TPP. Show MC (slight smile, mouth closed), lindsey (slight smile, mouth closed), and Riley (slight smile, mouth closed) all standing up from their seats in the room.
        with dissolve

    # -if MC chose More advice in Scene 55 (GAIN 1 POPULARITY)
        if "more_advice" in v16s55_lindsey_followup_question_set: 

            $ set_presidency_percent(v14_lindsey_popularity + 1)

            # -Lindsey holds out her hand for Riley to shake it-
            scene v16s60_8b # TPP. Close up of Lindsey(slight smile, mouth closed) holding out her hand for Riley(slight smile, mouth open) to shake.
            with dissolve 

            ri "Oh."

            scene v16s60_8c # TPP. Close up of Lindsey(slight smile, mouth closed) shaking hands with Riley(slight smile, mouth open.) 
            with dissolve

            ri "Very professional with the handshake, hehe. I like it!"

            scene v16s60_9d # FPP. MC looking at Lindsey (slight smile, mouth open) standing infront of and looking at Riley(slight smile, mouth closed) who is looking back at Lindsey.
            with dissolve

            # -Lindsey smiles back at that-

            li "Oh, and you must tell me what product you're using on your hair. It's on fire today!"

            scene v16s60_9e # FPP. MC looking at Lindsey (slight smile, mouth closed) standing infront of and looking at Riley(slight smile, mouth open) who is looking back at Lindsey.
            with dissolve

            ri "Aw, thanks for noticing! I'm using a new conditioner my salon recommended, I think it's the coconut that makes it shine."

            scene v16s60_9d
            with dissolve

            li "Oh, for sure, I love it. Let's meet for a coffee sometime and you can give me some tips?"

            scene v16s60_9e
            with dissolve

            ri "Yeah, that sounds great!"

            scene v16s60_9f # FPP. MC looking at Lindsey (slight smile, mouth closed) standing infront of and looking at Riley(slight smile, mouth closed) who is looking back at Lindsey.
            with dissolve

            u "(The double-whammy! Keeping it professional and fitting in compliments. I'm glad she listened to my advice.)"

        scene v16s60_9d
        with dissolve

        li "Thanks again for the interview. I can't wait to read the article."

        scene v16s60_9e
        with dissolve

        ri "Yeah, I'm really looking forward to writing it!"

        play sound "sounds/dooropen.mp3"

        scene v16s60_10a # TPP. Show MC(slight smile, mouth closed) and Lindsey (slight smile, mouth closed) leaving the SVC Times Office. Riley(slight smile, mouth closed) in the back watching them leave.
        with dissolve
        # [End of Checkpoint 1.2. Continue to Checkpoint 2]

    # -Regardless of who interviewed Lindsey-

# [Checkpoint 2]

    play sound "sounds/doorclose.mp3"

    scene v16s60_12 # FPP. MC and Lindsey(slight smile, mouth open.) standing in the hallway looking at each other.
    with dissolve 

    li "Thank fuck that's over with, haha."

    li "How do you think I did?"

    scene v16s60_12a # FPP. MC and Lindsey(slight smile, mouth closed.) standing in the hallway looking at each other.
    with dissolve

    u "You did your best and you were genuine. That's the main thing."

    u "Time will tell on the article itself though. We're putting a lot of trust in them."

    scene v16s60_12
    with dissolve

    li "I know."

    li "Phew!"

    li "Now that it's done, let's see what happens."

    scene v16s60_12a
    with dissolve

    u "Yup."

    scene v16s60_12
    with dissolve

    li "Thanks for being there for me."

    scene v16s60_12a
    with dissolve

    u "No problem at all."

    scene v16s60_12
    with dissolve

    li "Catch up with you later?"

    scene v16s60_12a
    with dissolve

    u "Yeah, see you soon."

    scene v16s60_13 # TPP. Show MC(slight smile, mouth closed) looking at Lindsey(waving, slight smile, mouth closed) as she is walking away looking and waving at MC.
    with dissolve

    jump v16s61