# SCENE 25: Amber Hangout (WHO IS AMBER)
# Locations: Amber's house
# Characters: MC (Outfit: 9), AMBER (Outfit: 3)
# Time: Night 

label v14s25:
    play music "music/v12/Track Scene 3_4.mp3" fadein 2

    scene v14s25_1 # TPP. Show MC walking up to the front door of Amber's home, MC neutral expression, mouth closed.
    with fade

    pause 0.75

    play sound "sounds/knock.mp3"

    scene v14s25_1a # TPP. Same as v14s25_1, MC standing at the front of Amber's door and knocking on the door.
    with dissolve

    pause 0.75

    play sound "sounds/dooropen.mp3"

    scene v14s25_2 # FPP. The door opens from his knocking, nobody standing at the doorway.
    with dissolve

    u "(Oh... Hello?)"

    scene v14s25_3 # TPP. MC walking inside of Amber's house.
    with dissolve

    pause 0.75

    scene v14s25_4 # FPP. MC finds Amber in the living room sitting on the floor with her back against the couch as she is smoking, Amber not realising MC is in the room yet, Amber neutral smile, mouth closed.
    with dissolve

    pause 0.75

    scene v14s25_4a # FPP. Same as v14s25_4, Amber turns and has now seen MC, Amber slight smile, mouth open.
    with dissolve

    am "There you are."

    if not v14s03a_take_wallet: 
        scene v14s25_4b # FPP. Same as v14s25_4a, Amber starting to get up from off the floor, Amber slight smile, mouth closed
        with dissolve

        pause 0.75

        scene v14s25_4c # FPP. Same as v14s25_4b, Amber now standing up, Amber slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v14s25_4d # FPP. Same as v14s25_4c. Amber walking over to MC, Amber slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v14s25_4e # FPP. Same as v14s25_4d, Amber standing infront of MC, Looking at eachother, Amber slight smile, mouth closed.
        with dissolve

    else:
        scene v14s25_4e
        with dissolve

        u "Hey, I got you something."

        scene v14s25_4f # FPP. Same as v14s25_4e, Amber slight smile, mouth open.
        with dissolve

        am "Oh, wow. Ha..."

        scene v14s25_5 # TPP. Amber hugging MC tightly, both slight smile, mouth closed.
        with vpunch

        pause 0.75

        scene v14s25_4e
        with dissolve

        pause 0.75

        if not v14s24a_gummyfish:
            scene v14s25_4g # FPP. Same as v14s25_4f, Amber looking down as MC hands her the twezzlers candy, Amber slight smile, mouth open. 
            with dissolve

            $ grant_achievement("how_did_you_know")

            am "How did you know these were my favorite?"

            scene v14s25_4e
            with dissolve

            u "I took a wild guess."

            scene v14s25_4f
            with dissolve

            am "You know me too well."

        else:
            scene v14s25_4h # FPP. Same as v14s25_4g, Amber looking down as MC hands her the Gummy Fish candy, Amber slight smile, mouth closed
            with dissolve

            u "I didn't know what you liked."

            scene v14s25_4f
            with dissolve

            am "I've never tried these, I usually don't eat candy except for those red licorice things, but I'll definitely give these a shot."

            scene v14s25_4e
            with dissolve

            u "(Damn, should've gotten the Twezzlers...) Well, I hope you like them."

            scene v14s25_4f
            with dissolve

            am "Thank you."

    scene v14s25_4f
    with dissolve

    am "Did you have any trouble getting here?"

    scene v14s25_4e
    with dissolve

    u "No, why would I?"

    scene v14s25_4f
    with dissolve

    am "There's a weird lady that's been asking people for spare gum around here... She takes it, chews it and then throws it at you. *Chuckles*"

    scene v14s25_4e
    with dissolve

    u "What the fuck? I don't know if I should laugh or feel bad for wanting to laugh."

    scene v14s25_4f
    with dissolve

    am "I laugh my ass off everytime I see one of her victims. Especially the ones I've set up..."

    scene v14s25_4e
    with dissolve

    u "Haha evil! You're something else."

    scene v14s25_4f
    with dissolve

    am "Haha, c'mon. Let's go to my room."

    scene v14s25_4e
    with dissolve

    u "Want me to lock the door?"

    scene v14s25_4f
    with dissolve

    am "Nah, I never lock it, c'mon."

    scene v14s25_4e
    with dissolve

    u "If you say so."

    scene v14s25_6 # TPP. Show Amber grabbing MC by the hand and leading him to her room, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v14s25_7 # TPP. In Amber's room, MC and Amber sitting on her bed, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v12/Track Scene 35b_2.mp3" fadein 2

    scene v14s25_8 # FPP. MC and Amber on Amber's bed in her room, MC looking at Amber, Amber looking at MC, Amber slight smile, mouth open.
    with dissolve

    am "Are you used to being back on campus yet?"

    scene v14s25_8a # FPP. Same as v14s25_8, Amber slight smile, mouth closed.
    with dissolve

    u "Still getting into the swing of things, but I'll be back on it soon enough. You?"

    scene v14s25_8
    with dissolve

    am "Well, I'm not rushing it."

    scene v14s25_8b # FPP. Same as v14s25_8a, Amber reaching behind her pillow, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v14s25_8c # FPP. Same as v14s25_8, Amber holding a bottle of pills up, slight smile, mouth open.
    with dissolve

    am "As you can see, I'm still on vacation..."

    scene v14s25_8a
    with dissolve

    menu:

        "Nice pills you got there":

            $ add_point(KCT.TROUBLEMAKER)

            u "Nice pull you got there."

            scene v14s25_8
            with dissolve

            am "Thank you, I call 'em a good time."

            scene v14s25_8a
            with dissolve

            u "You don't think taking pills is a little too much?"


        "What are those, Amber?":

            $ add_point(KCT.BOYFRIEND)

            u "What are those, Amber?"

            scene v14s25_8
            with dissolve

            am "I call 'em a good time."

    scene v14s25_8a
    with dissolve

    u "You don't think taking pills is a little too much?"

    u "Where'd you get those from anyway?"

    scene v14s25_8
    with dissolve

    am "Haha, I can't remember where I get every single drug that I take."

    scene v14s25_8a
    with dissolve

    u "Okay... I know you like being wild, Amber. But you've always been responsible when it comes to this stuff."

    u "When Josh was at his lowest point, it was you that helped him."

    u "So, what's got you acting like this? Tell me."

    scene v14s25_8
    with dissolve

    am "Wow... So someone does see me as the responsible one!"

    am "But good ole Shane just thinks I'm another worthless junkie... Ha!"

    scene v14s25_8a
    with dissolve

    u "Who's Shane?"

    scene v14s25_8d # FPP. Same as v14s25_8, Amber slight frown, mouth open.
    with dissolve

    am "Shane is my friend- WAS my friend..."

    am "He doesn't want to talk to me anymore."

    scene v14s25_8e # FPP. Same as v14s25_8d, Amber slight frown, mouth closed.
    with dissolve

    u "I can tell this is serious for you, Amber... If you wanna talk we can talk or we can just leave it be."

    scene v14s25_8d
    with dissolve

    am "Ha! Why not talk about it, right?"

    am "Shane went to rehab and blocked me on everything. *Scoffs* He and I have been friends forever, and now that he wants to turn a new leaf..."

    am "He needs to cut me off since I'm such a bad influence."

    scene v14s25_8f # FPP. Same as v14s25_8e, Amber taking a hit from her vape.
    with dissolve

    pause 0.75

    scene v14s25_8g # FPP. Same as v14s25_8f, Amber blowing out the smoke from her vape.
    with dissolve

    u "He said that?"

    scene v14s25_8h # FPP. Same as v14s25_8e, Amber angry frown, mouth open.
    with dissolve

    am "He didn't have to, [name]."

    am "Telling me that he needs to better his life and then blocking me, pretty much said it for himself."

    scene v14s25_8i # FPP. Same as v14s25_8h, Amber angry frown, mouth closed.
    with dissolve

    menu: 

        "I'm sorry":

            $ add_point(KCT.BOYFRIEND)

            u "I'm sorry you're going through this, you-."

            scene v14s25_8h
            with dissolve

            am "Why? Haha..."

            scene v14s25_8f
            with dissolve

            pause 0.75

            scene v14s25_8g
            with dissolve

            pause 0.75

            scene v14s25_8d
            with dissolve

            am "You didn't do anything, it's all me."

            scene v14s25_8e
            with dissolve

            u "Amber..."

        "What a dick":

            $ add_point(KCT.BRO)

            u "The guy sounds like a dick."

            scene v14s25_8h
            with dissolve

            am "Right."


    scene v14s25_8d
    with dissolve

    am "It's obvious that everyone sees me as the girl who causes everyone around her to turn as bad and low as she is."

    scene v14s25_8e
    with dissolve

    u "Who is putting this in your head, Amber?"

    u "I've been your friend for a good while now, and anything I've ever done while with you was by my own choice. Just like any one of our other friends."

    u "Like I said earlier, do you not remember that it was you who went after Josh and helped clean him up?"

    scene v14s25_8d
    with dissolve

    am "I remember it clearly. I was also the one who got him going on the hard stuff to begin with."

    scene v14s25_8f
    with dissolve

    pause 0.75

    scene v14s25_8g
    with dissolve

    u "What? *Chuckles*"

    scene v14s25_8d
    with dissolve

    am "It's true!"

    scene v14s25_8e
    with dissolve

    u "No... Don't give yourself that much credit, ha. Josh was on that shit way before he met you."

    scene v14s25_8d
    with dissolve

    am "*Sighs*"

    scene v14s25_8e
    with dissolve

    u "Forgive yourself for what you have done in the past. If things happened outside of your control, then oh well."

    scene v14s25_8d
    with dissolve

    am "\"Forgive\"..."

    scene v14s25_8j # FPP. Same as v14s25_8d, Amber slight frown, Amber crying lightly, mouth open.
    with dissolve

    am "That's all my parents wanted me to do when I was little..."

    am "\"Just tell the priest what you did, Amber. Confess to your sins, Amber.\""

    scene v14s25_8k # FPP. Same as v14s25_8j, Amber slight frown, Amber crying lightly, mouth closed.
    with dissolve

    u "Your parents were Catholic?"

    scene v14s25_8j
    with dissolve

    am "My parents were dicks. That's what they were."

    scene v14s25_8l # FPP. Same as v14s25_8j, Amber slight smile, Amber crying lightly, mouth open.
    with dissolve

    am "Now that they're older they wanna go out all the time and have fun."

    am "If they would've acted how they do now when I was little, I probably wouldn't have been so rebellious. *Chuckles*"

    scene v14s25_8m # FPP. Same as v14s25_8l, Amber slight smile, Amber crying lightly, mouth closed.
    with dissolve

    u "Ha."

    scene v14s25_8l
    with dissolve

    am "I only got into trouble because their rules were so ridiculous. I mean..."

    am "I couldn't even sit back or slouch in my chair when I ate food at the dinner table, that's how strict they were."

    scene v14s25_8m
    with dissolve

    menu:

        "Empathize with her":
            $ add_point(KCT.BOYFRIEND)

            u "That sounds close to torture..."

            u "I hate that you've had to go through those things."

        "Stay quiet":
            $ add_point(KCT.BRO)


    scene v14s25_8l
    with dissolve

    am "I'm sure you already know but, Lauren has religious parents too, and I think that's the reason why we clicked so well in Europe."

    scene v14s25_8m
    with dissolve

    u "Yeah, I heard small things about her parents. I knew they were religious, but nothing compared to what you've dealt with."

    scene v14s25_8l
    with dissolve

    am "So, yeah. That's why I am who I am today."

    scene v14s25_9 # TPP. Close up of Amber looking at the pill bottle, MC off camera, slight frown, mouth closed.
    with dissolve

    pause

    scene v14s25_8d
    with dissolve

    am "I used to do these for fun, you know? But as life goes on, I find that sometimes you need things to help you stay happy."

    scene v14s25_8e
    with dissolve

    u "I don't know if you absolutely need those-"

    scene v14s25_8d
    with dissolve

    am "[name], if I didn't have one of these every now and again, especially on days like this..."

    scene v14s25_8j
    with dissolve

    am "It gets to the point where I can't stand to even be around myself anymore."

    menu:
        "No more drugs, Amber":
            $ add_point(KCT.BOYFRIEND)
            $ add_point(KCT.BRO)
            $ v14_amber_clean = True
            $ AmberLoyal = True
            scene v14s25_8k
            with dissolve

            u "Look at me, Amber."

            scene v14s25_10 # TPP. Show MC putting Amber's pills and vape on her nightstand.
            with dissolve

            pause 0.75

            scene v14s25_11 # TPP. Show MC and Amber holding hands, MC slight smile, mouth closed, Amber slight frown, Amber crying lightly, mouth closed.
            with dissolve

            pause 0.75

            scene v14s25_8k
            with dissolve

            u "Every single decision we make as human beings, is a decision that we make on our own."

            u "Unless you've put a pill into someone's unwilling mouth, there's nothing you've ever done that has forced anyone else to do the same as you."

            scene v14s25_8j
            with dissolve

            am "Yeah, but-"

            scene v14s25_8k
            with dissolve

            u "Let me finish, please?"

            scene v14s25_8j
            with dissolve

            am "*Scoffs*"

            scene v14s25_8k
            with dissolve

            u "*Chuckles* Even though you haven't forced anyone to do anything, it's true that many people really like you and your company."

            u "So, sometimes they'll actually do what you're doing in order to be liked, or to fit in with you."

            scene v14s25_8j
            with dissolve

            am "*Whispers* Why?"

            scene v14s25_8k
            with dissolve

            u "You're influential, Amber. And being influential is a great thing if you influence people to do good."

            u "Sadly..."

            scene v14s25_11a # TPP. Show MC and Amber still holding hands, MC's free hand holding up the bottle of pills.
            with dissolve

            pause 0.75

            scene v14s25_8k
            with dissolve

            u "This right here, isn't good. At all."

            u "If what you're feeling is guilt, don't feel guilty for the choices that others have made."

            u "Feel guilty for what choices you've allowed others to see you make, and think that they're safe, or \"good\" decisions to make."

            scene v14s25_8n # FPP. Same as v14s25_8m, Amber crying heavily with her face buried in her hands.
            with dissolve

            u "I'm sorry Amber, I didn't mean to..."

            scene v14s25_8o # FPP. Same as v14s25_8j, Amber looking at MC, Amber crying heavily, mouth open.
            with dissolve

            am "*Crying* No, no, I'm not mad..."

            am "Maybe most times I can throw on a tough girl attitude and avoid these types of conversations, but not when I know you're right."

            scene v14s25_8p # FPP. Same as v14s25_8o, Amber crying heavily, mouth closed.
            with dissolve

            u "This doesn't mean you're a bad person."

            scene v14s25_8o
            with dissolve

            am "*Crying* It doesn't make me a good person either, and that's what I want to be..."

            am "*Sniffles* So I've decided."

            scene v14s25_8p
            with dissolve

            u "Decided what?"

            scene v14s25_12 # TPP. Amber standing up from off the bed.
            with dissolve

            pause 0.75

            scene v14s25_13 # FPP. Amber standing up infront of MC, MC looking at Amber, Amber looking at MC, Amber slight smile, mouth open.
            with dissolve

            am "*Laughing* I'm done. Done with all drugs."

            scene v14s25_13a # FPP. Same as v14s25_13, Amber slight smile, mouth closed.
            with dissolve

            u "Wait, you're serious?"

            scene v14s25_13b # FPP. Same as v14s25_13, Show Amber wiping her face, Amber slight smile, mouth closed.
            with dissolve

            pause 0.75

            scene v14s25_13
            with dissolve

            am "You think I'm joking?"

            am "Stay here."

            scene v14s25_13c # FPP. Same as v14s25_13b, Show Amber walking away from MC, Amber holding the pill bottle in one hand, a bag of weed in her other hand, slight smile, mouth closed.
            with dissolve

            pause 0.75

            scene v14s25_13d # FPP. Same as v14s25_13c, MC looking at Amber's empty room.
            with dissolve

            pause 0.5

            play sound "sounds/flush.mp3"
            
            pause 0.5
            
            scene v14s25_13d
            with dissolve

            pause 1.5

            scene v14s25_14 # FPP. Amber walking back in the room towards MC, Amber slight smile, mouth closed
            with dissolve

            pause 0.75

            scene v14s25_8
            with dissolve

            stop sound
            am "That's the last time you'll ever see me with drugs."

            scene v14s25_8a
            with dissolve

            u "I'm speechless right now, Amber. I mean..."

            u "I'm so fucking proud of you."

            scene v14s25_8
            with dissolve

            am "Don't start acting all sappy, I'm still the same, snappy Amber."

            am "I'll beat your ass if you make fun of me about this or anything else."

            scene v14s25_8a
            with dissolve

            u "Haha, that's noted."

            scene v14s25_8
            with dissolve

            am "For real though, I needed to hear everything you said."

            am "And as my friend, I'd appreciate you keeping me accountable and helping make sure I stay clean?"

            scene v14s25_8a
            with dissolve

            menu:
                "That's a lot of pressure":
                    $ add_point(KCT.TROUBLEMAKER)

                    u "I don't know Amber. I'm happy you wanna stay clean, but I can't be responsible for you."

                    scene v14s25_8
                    with dissolve

                    am "I completely understand. It's my cross to carry. Anyways..."

                "Of course":
                    $ add_point(KCT.BOYFRIEND)

                    scene v14s25_8a
                    #with dissolve
                    
                    u "Of course, I want what's best for you."

                    scene v14s25_11b # TPP. Same as v14s25_11, Show Amber and MC hugging.
                    with dissolve

                    pause 0.75

                    scene v14s25_8
                    with dissolve

                    am "Thank you, [name]."

            am "I'm really glad you came by tonight. I'm sure things could've gone a lot differently if you hadn't."

            scene v14s25_8a
            with dissolve

            u "I'm glad I came too."

            scene v14s25_8
            with dissolve

            am "*Sighs* On other topics, Lindsey has her bake sale tomorrow and I'm actually looking forward to it."

            scene v14s25_8a
            with dissolve

            u "Why? *Chuckles* Do you like baked goods?"

            scene v14s25_8
            with dissolve

            am "Yeah, of course, but that's not why I'm going. *Laughs*"

            scene v14s25_8a
            with dissolve

            u "Haha, why are you going?"

            scene v14s25_8
            with dissolve

            am "I heard that she can't cook for shit. So..."

            am "Unless she has some help in the kitchen, it's gonna be hilarious."

            scene v14s25_8a
            with dissolve

            u "You're terrible..."

            scene v14s25_8
            with dissolve

            am "I'm Amber."

            scene v14s25_8a
            with dissolve

            u "Haha, that you are."

            u "Now, I'm gonna get out of here so you can get to sleep."

            scene v14s25_8
            with dissolve

            am "Did you not hear what I said about the gum lady? You're staying here tonight, big guy."

            scene v14s25_8a
            with dissolve

            u "Ha... Wait."

            u "For real?"

            scene v14s25_8q # FPP. Same as v14s25_8, Amber winking at MC, Amber flirtatious smile, mouth open.
            with dissolve

            am "Do you know how to lay in a bed with a female without trying to fuck her?"

            scene v14s25_11d # TPP. Same as v14s25_11b, Show MC doing the generic thinking pose, MC cheeky smirk, mouth closed.
            with dissolve

            pause 0.75

            scene v14s25_8a
            with dissolve

            u "Mmm..."

            u "I do, yeah."

            scene v14s25_8
            with dissolve

            am "Then yes, for real. *Laughs*"

            am "Go ahead and get comfy. I'm just gonna go change real quick."

            scene v14s25_15 # FPP. Amber walking out of the room.
            with dissolve

            pause 1 

            scene v14s25_16 # TPP. Show MC in his boxers.
            with fade

            pause 1

            #scene v14s25_17 # TPP. Show MC laying in Amber's Bed.
            #with fade

            #pause 1

            if config_censored:
                call screen censoredPopup("v14s25_nsfwSkipLabel1")

            scene v14s25_18 # TPP. (MC off Camera) Close up of Amber standing at the entrance of her room, Amber topless in a flirty pose, Wearing nothing but black panties, Amber Slight Smile, Mouth closed.
            with dissolve

            u "Amber..."

            scene v14s25_18a # TPP. Same as v14s25_18, Amber slight smile, mouth open.
            with dissolve

            am "What? You've seen tits before, haven't you?"

            scene v14s25_18
            with dissolve

            u "Yes Amber, but you-"

            scene v14s25_18a
            with dissolve

            am "I like sleeping naked, yes. Just control yourself."

            scene v14s25_18
            with dissolve

            u "I can do that. *Chuckles nervously*"

            scene v14s25_18a
            with dissolve

            am "Good, haha. Goodnight."

            scene v14s25_18b # TPP. Same as v14s25_18a, Amber flipping the light switch, Amber slight smile, mouth closed.
            with dissolve

            pause 0.75

            label v14s25_nsfwSkipLabel1:

            scene v14s25_17a # TPP. Same as v14s25_17, Show MC and Amber laying in bed, both slight smile, mouth closed.
            with dissolve

            pause 0.75

            scene v14s25_17b # TPP. Same as v14s25_17a, MC and Amber sleeping.
            with fade

            pause 0.75

            scene v14s25_17c # TPP. Same as v14s25_17b, MC and Amber sleeping in different positions.
            with fade

            pause 0.75

            scene v14s25_17d # TPP. MC wakes up with topless Amber sleeping on him.
            with dissolve

            menu:
                "Let her stay":
                    $ add_point(KCT.TROUBLEMAKER)
                    $ v14s25_letherstay = True
                    u "(Ha, hard as stone on the outside but a softie on the inside.)"

                    scene v14s25_17e # TPP. Show MC going back to sleep with his arm around Amber as she lays on him.
                    with dissolve

                "Move away":
                    $ add_point(KCT.BOYFRIEND)
                    u "(Sorry, Amber.)"

                    scene v14s25_17f # TPP. Show MC and Amber with their backs against each other sleeping.
                    with dissolve
            
            pause 0.75
            
            stop music fadeout 3
            jump v14s25b

        "Let Amber be Amber":
            $ add_point(KCT.TROUBLEMAKER)
            scene v14s25_8m
            with dissolve

            u "Look, Amber..."

            u "Fuck what other people think. You can't possibly blame yourself for the stupid shit that other people choose to do."

            u "No one is following you off the bridge if you jump. Sorry, but you don't have quite that much influence. *Chuckles*"

            scene v14s25_8l
            with dissolve

            am "Ha. *Sniffles*"

            scene v14s25_8m
            with dissolve

            u "Everyone should enjoy their life and some of us happen to enjoy the dark side."

            u "There's nothing wrong with that."

            scene v14s25_8l
            with dissolve

            am "That's all true, but I don't-"

            scene v14s25_8m
            with dissolve

            u "But nothing, Amber."

            u "You're not perfect and neither is anyone else. You can be and do whatever you want."

            u "So, be a good person when it counts and have fun while you still can. Yeah? *Laughs*"

            scene v14s25_10a # TPP. Same as v14s25_10, Show MC holding the pill bottle in one hand and taking one of the pills with his other hand.
            with dissolve

            pause 0.75

            scene v14s25_8l
            with dissolve

            am "*Gasps* [name]! *Laughs*"

            scene v14s25_8m
            with dissolve

            u "Something wrong?"

            scene v14s25_8l
            with dissolve

            am "No. Not at all."

            scene v14s25_8m
            with dissolve

            u "Good."

            scene v14s25_8r # FPP. Same as v14s25_8m, Amber opening her mouth as MC puts the pill in her mouth. 
            with dissolve

            pause 0.75

            scene v14s25_8l
            with dissolve

            am "We're about to have some fucking fun. Haha!"

            scene v14s25_19 # TPP. Double Vision (like in homecoming Amber sex scene), Show MC and Amber dancing, both slight smile, mouths closed.
            with fade

            pause 2.5
            
            if v14s03a_take_wallet and not v14s24a_gummyfish: # if bought Twezzlers
                scene v14s25_19a # TPP. Same as v14s25_19, Double Vision, Show MC and Amber eating snacks.
                with fade

                pause 2.5
            
            elif v14s03a_take_wallet: # if bought gummy fish
                scene v14s25_19c
                with fade
                
                pause 2.5
            
            scene v14s25_19b # TPP. Same as v14s25_19a, Double Vision, Show MC and Amber tongue-kissing,
            with fade
            
            pause 2.5

            scene v14s25_20 # TPP. Show Amber pinning MC against the wall as they kiss.
            with dissolve

            pause 1.75

            scene v14s25_21 # FPP. Amber pinning MC against the wall, Amber flirtatious smile, mouth open.
            with dissolve

            am "*Panting* This is the most fun I've had in such a long time, [name]."

            scene v14s25_20a # TPP. Same as v14s25_20, MC kissing Amber's neck.
            with fade

            pause 1.5

            scene v14s25_22 # TPP. Close up of just Amber's face, Amber biting her lip.
            with dissolve

            pause 0.75

            scene v14s25_22a # TPP. Same as v14s25_22, Amber flirtatious smile, mouth open.
            with dissolve

            am "*Moans* And it's definitely turning me on..."

            scene v14s25_23 # TPP. Amber's hand on MC's crotch.
            with dissolve

            pause 0.75

            scene v14s25_21
            with dissolve

            am "*Whispers* You wanna do something about that?"

            menu:
                "Yeah I fucking do":
                    $ add_point(KCT.TROUBLEMAKER)
                    $ sceneList.add("v14_amber")
                    $ amber.relationship = Relationship.FWB

                    scene v14s25_21a # FPP. Same as v14s25_21, Amber flirtatious smile, mouth closed.
                    with dissolve

                    u "Yeah I fucking do!"
                    
                    stop music fadeout 3
                    jump v14s25a

                "We really shouldn't...": 
                    $ add_point(KCT.BOYFRIEND)

                    scene v14s25_21a
                    with dissolve

                    u "We really shouldn't... *Panting*"

                    scene v14s25_21b # FPP. Same as v14s25_21a, Amber slightly disappointed, mouth closed.
                    with dissolve

                    u "Besides, I'm way too high for all that right now."

                    scene v14s25_21c # FPP. Same as v14s25_21b, Amber slightly disappointed, mouth open.
                    with dissolve

                    am "Bummer..."

                    scene v14s25_24 # TPP. Show Amber starting to undress.
                    with dissolve

                    u "U-uhm, sorry, should I leave?"

                    scene v14s25_18a
                    with dissolve

                    am "Do you not remember what I said about the gum lady? You're staying here tonight, get in the bed."

                    scene v14s25_18
                    with dissolve

                    u "I'm talking about you being naked..."

                    scene v14s25_18a
                    with dissolve

                    am "What? You've seen tits before haven't you?"

                    scene v14s25_18
                    with dissolve

                    u "Well, yes Amber of course, but-"

                    scene v14s25_18a
                    with dissolve

                    am "Well, I like sleeping naked. So control yourself."

                    scene v14s25_18
                    with dissolve

                    u "*Sighs* Okay. I can do that."

                    scene v14s25_18a
                    with dissolve

                    am "Great, goodnight [name]."

                    scene v14s25_18b
                    with dissolve

                    pause 0.75

                    scene v14s25_17a
                    with dissolve

                    pause 0.75

                    scene v14s25_17b
                    with fade

                    pause 0.75

                    scene v14s25_17c
                    with fade

                    pause 0.75

                    scene v14s25_17d
                    with dissolve

                    menu:
                        "Let her stay":
                            $ add_point(KCT.TROUBLEMAKER)
                            $ v14s25_letherstay = True
                            u "(Ha, hard as stone on the outside but a softie on the inside.)"

                            scene v14s25_17e
                            with dissolve

                        "Move away":
                            $ add_point(KCT.BOYFRIEND)
                            u "(Sorry, Amber.)"

                            scene v14s25_17f
                            with dissolve
                    
                    pause 0.75
                    
                    stop music fadeout 3
                    jump v14s25b