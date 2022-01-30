# SCENE 23: Wolves Support
# Locations: Wolves House
# Characters: MC (Outfit: 9), CHRIS (Outfit: 2), CHLOE (Outfit: 2)
# Time: Evening 

label v14s23:
    play music "music/v12/Track Scene 18_4.mp3" fadein 2

    scene v14s23_1 # TPP. Show MC walking up to the steps of the wolves house and seeing Chris, Chris looking at the sky, Both slight smile, mouth closed.
    with fade

    pause 0.75

    scene v14s23_1a # TPP. Same as v14s23_1, MC starting to sit next to Chris, Chris still looking at the sky, both slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v14s23_2 # FPP. MC and Chris sitting on the porch of the Wolves house, MC looking at Chris, Chris looking at the sky, Chris slight smile, mouth closed.
    with dissolve

    u "Hey, Chris."

    scene v14s23_2a # FPP. Same as v14s23_2, MC looking at Chris, Chris looking at MC, Chris slight smile, mouth open.
    with dissolve

    ch "Hey, [name]."

    scene v14s23_2b # FPP. Same as v14s23_2a, Chris slight smile, mouth closed.
    with dissolve

    u "Just enjoying the weather or is something else on your mind?"

    scene v14s23_2a
    with dissolve

    ch "Just enjoying the sunset is all."

    scene v14s23_3 # FPP. Pretty shot of the sun setting infront of the wolves house.
    with dissolve

    u "I gotta admit, SVC does get some of the best sunsets."

    scene v14s23_2a
    with dissolve

    ch "Yeah..."

    ch "Sometimes taking a moment to relax despite having too much shit to do, is what you need to do most."

    scene v14s23_2b
    with dissolve

    u "That's a very \"Mr. Lee\" thing to say."

    scene v14s23_2a
    with dissolve

    ch "Dammit... I knew I spent too much time around that boomer while we were away..."

    scene v14s23_2b
    with dissolve

    u "*Laughs*"

    scene v14s23_2a
    with dissolve

    ch "I just wish I learned that lesson sooner rather than later."

    scene v14s23_2b
    with dissolve

    u "I can understand that."

    u "Well man, the reason I came is because-"

    scene v14s23_2a
    with dissolve

    ch "Chloe? You're here because of Chloe, right?"

    scene v14s23_2b
    with dissolve

    u "Uhh, yeah... How'd you know?"

    scene v14s23_2a
    with dissolve

    ch "News travels fast when it comes to stuff like this, man."

    ch "Everyone is on the lookout for the next scoop of drama these days."

    scene v14s23_2b
    with dissolve

    u "Is supporting Chloe considered drama?"

    scene v14s23_2a
    with dissolve

    ch "For some maybe not. But, when you're dating her biggest enemy it may be a bit difficult."

    scene v14s23_2b
    with dissolve

    u "You mean Nora, right?"

    scene v14s23_2a
    with dissolve

    ch "Exactly."

    ch "Supporting Chloe was pretty much the last straw for her. But I live by doing what's right, not what I prefer or want."

    scene v14s23_2b
    with dissolve

    menu: 
        "That's very selfless":
            $ add_point(KCT.BRO)

            u "That's a very selfless way to live."

            scene v14s23_2a
            with dissolve

            ch "I try to be. Chloe should be here-"

        "It sounds inconsiderate":
            $ add_point(KCT.TROUBLEMAKER)

            scene v14s23_2b
            #with dissolve
            
            u "I don't know man, it sounds a bit inconsiderate."

            scene v14s23_2a
            with dissolve

            ch "I don't think you get what's at stake here. Chloe-"

    stop music fadeout 3
    play music "music/v12/Track Scene 18_3.mp3" fadein 2

    scene v14s23_1b # TPP. Same as v14s23_1a, Show MC and Chris sitting on the porch, Chloe running towards the porch back facing the camera, MC and Chris both slight smile, mouth closed.
    with dissolve

    cl "HEY GUYS!"

    scene v14s23_1c # TPP. Same as v14s23_1b, Chloe getting closer to MC and Chris.
    with dissolve

    pause 0.75

    scene v14s23_1d # TPP. Same as v14s23_1c, Chloe standing infront of MC and Chris.
    with dissolve

    pause 0.75

    scene v14s23_2c # FPP. Same as v14s23_2b, Chris looking at Chloe (Chloe off camera) standing infront of them, slight smile, mouth open.
    with dissolve

    ch "Speaking of the devil."

    scene v14s23_4 # FPP. MC looking at Chloe, Chloe looking at Chris (Chris off camera), Chloe confused smile, mouth open.
    with dissolve

    cl "What?"

    scene v14s23_2c
    with dissolve

    ch "I had just said your name as you came running."

    scene v14s23_4a # FPP. Same as v14s23_4, Chloe slight smile, mouth open.
    with dissolve

    cl "Oh. *Chuckles* That's why I felt my ears burning..."

    scene v14s23_4b # FPP. Same as v14s23_4a, Chloe now looking at MC, slight smile, mouth open.
    with dissolve

    cl "Have you guys gotten started on talking about things?"

    scene v14s23_4c # FPP. Same as v14s23_4b, Chloe slight smile, mouth closed.
    with dissolve

    u "We haven't."

    scene v14s23_4b
    with dissolve

    cl "Good, I wanted to be here."

    scene v14s23_2c
    with dissolve

    ch "Now look, Chloe... I did agree to help you, but I didn't specify how involved or supportive I'd be."

    ch "Putting my head out there in full support of you means that the Wolves must all be convinced."
    ch "Or else we'll have a divided frat with similar issues to what you have now."

    scene v14s23_4a
    with dissolve

    cl "I understand that, and that's why I was hoping that after we all talked, you could make a clearer decision."

    scene v14s23_2c
    with dissolve

    ch "Great, just making sure things are clear."

    scene v14s23_4a
    with dissolve

    cl "Of course, and it means a lot to me that you understand what it means to have a divided house. It's not fun."

    scene v14s23_2c
    with dissolve

    ch "I wouldn't wish that on anyone, and as a fellow President you have my best wishes."

    scene v14s23_4a
    with dissolve

    cl "Thank you, but after this plan and my reelection hopefully the Chicks will be back!"

    scene v14s23_4c
    with dissolve

    u "I like the motivation."

    scene v14s23_4b
    with dissolve

    cl "Haha, thanks. Now, rather than just having the support of the Wolves for namesake, I'd like to really show our unity."

    scene v14s23_2c
    with dissolve

    ch "How do you propose we do that?"

    scene v14s23_4a
    with dissolve

    cl "We've decided that we will pull off a major photoshoot."

    scene v14s23_2c
    with dissolve

    ch "Photoshoots are expensive, especially with a lot of people."

    menu:
        "Agree":
            $ v14s23_agree = True
            $ add_point(KCT.BOYFRIEND)

            scene v14s23_2b
            with dissolve

            u "You're right. It is expensive, but money is just an object when it comes to keeping the Chicks legacy in good hands."
            
        "Disagree":
            $ add_point(KCT.TROUBLEMAKER)
            $ add_point(KCT.BRO)
            scene v14s23_2b
            with dissolve

            u "I have to disagree because we could always just have an amateur shoot with our phones. It doesn't have to be spectacular."

            scene v14s23_2a
            with dissolve

            ch "Chloe knows hard and well that when it comes to these things, nothing can be done amateurly."

    scene v14s23_4a
    with dissolve

    cl "Doing a professional shoot will cost us some money, but before we start talking about the bill, let me at least show you what I'd like to order."

    scene v14s23_2c
    with dissolve

    ch "Of course, go on."

    scene v14s23_4a
    with dissolve

    cl "So, this is what I'm thinking."

    cl "Let's have members from the Chicks and Wolves get together and pose in front of a white backdrop making us the centerpiece."

    cl "In one of the shots, Chris and I will pose together with the caption #PresidentialStatus."

    scene v14s23_4c
    with dissolve

    u "Actually, for this... it's probably best if it's just you and Chris, right?"

    u "It's better not to drag anyone else into this, I think. Don't wanna cause any unintended tension for others."

    scene v14s23_4b
    with dissolve

    cl "That's true... A lot of the girls are already stressed about choosing sides so, yeah. Just you and I then, Chris."

    scene v14s23_2c
    with dissolve

    ch "Any props in mind or is there a theme? If seeing us together is the only thing, I can think of better ways to get you more votes."

    if v14_realwolf: #Placeholder for choosing real wolf on planning board
        scene v14s23_4a
        with dissolve

        cl "I'm glad you asked, hehe..."

        cl "A really good friend of mine is willing to let us shoot with her for a fee, but with her we'll get to pose with a real life wolf!"

        scene v14s23_2d # FPP. Same as v14s23_2c, Chris shocked smile, mouth open.
        with dissolve

        ch "Are you guys... serious?"

        scene v14s23_2b
        with dissolve

        u "When Chloe and I talked about it I knew you'd like the idea."

        scene v14s23_4a
        with dissolve

        cl "Haha, that's what I was thinking too. We'd not only be getting support from the SVC Wolves, but giving support to the Wolf Sanctuary as well."

        scene v14s23_2c
        with dissolve

        ch "Sheesh..."

        scene v14s23_4a
        with dissolve

        cl "It'd give the Wolves a really good look, Chris."

        cl "The Apes are always looked at as the tough guys, right? But this..."

        cl "This would change that."

        scene v14s23_2c
        with dissolve

        ch "You guys are approaching this with a lot of respect for the Wolves and I."

        ch "I won't lie though, I thought you'd come here trying to squeeze whatever you could out of us, regardless of what it made us look like."

        scene v14s23_4a
        with dissolve

        cl "Oh no, Chris. I'd never do that."
        cl "The whole reason I want your support is because I believe the Wolves are a well-respected frat and deserving of a brotherhood title."

        scene v14s23_2c
        with dissolve

        ch "Haha! If kissing ass was a profession, you'd be making a really good salary, Chloe."

        scene v14s23_4c
        with dissolve

        u "*Laughs*"

        scene v14s23_4d # FPP. Same as v14s23_4a, Chloe looking at Chris, Chloe grumpy smile, mouth open.
        with dissolve

        cl "Ugh, asshole! *Chuckles* I'm being serious."
     
        if v14s23_agree:
            $ v14_chrissupport = 3
            scene v14s23_2c
            with dissolve

            ch "Haha, you know what?"

            scene v14s23_4a
            with dissolve

            cl "What?"

            scene v14s23_2c
            with dissolve

            ch "I'm gonna back you a hundred percent."

            scene v14s23_4a
            with dissolve

            cl "Wait, what?!"

            scene v14s23_2c
            with dissolve

            ch "All of it."

            scene v14s23_2e # FPP. Same as v14s23_2c, Chris slight smile, mouth closed.
            with dissolve

            u "You mean..."

            scene v14s23_2c
            with dissolve

            ch "The photoshoot, the fee for the wolf, everything. The Wolves have got you covered."

            scene v14s23_4a
            with dissolve

            cl "Chris... You're joking, right?"

            scene v14s23_2c
            with dissolve

            $ set_presidency_percent(v14_lindsey_popularity - 5) #tick
            ch "I'm very serious. I like the plan you guys came up with, I like the respect you're giving to the Wolves, and I like you as President."

            scene v14s23_5 # TPP. Show Chloe hugging Chris, Chris not hugging her back yet, Chris surprised face, Chloe excited smile, both mouth closed
            with dissolve

            pause 0.75

            scene v14s23_5a # TPP. Same as v14s23_5, Chris hugging Chloe back, slight smile, mouth closed.
            with dissolve

            pause 0.75

            scene v14s23_4a
            with dissolve

            cl "Thank you so fucking much, Chris! You have no idea how helpful this is going to be."

            scene v14s23_2c
            with dissolve

            ch "That's what I'm-"

        else:
            $ v14_chrissupport = 2
            scene v14s23_2c
            with dissolve

            ch "Haha, you know what?"

            scene v14s23_4a
            with dissolve

            cl "What?"

            scene v14s23_2c
            with dissolve

            ch "I'm gonna back you halfway."

            scene v14s23_4a
            with dissolve

            cl "Wait, what?!"

            scene v14s23_2c
            with dissolve

            ch "Half of everything."

            ch "The photoshoot, the fee for the wolf, everything. The Wolves have got half of it all."

            scene v14s23_2e
            with dissolve

            u "Chris..."

            scene v14s23_4a
            with dissolve

            cl "You're joking..."

            scene v14s23_2c
            with dissolve

            $ set_presidency_percent(v14_lindsey_popularity - 1) #tick
            ch "I'm very serious. I like the plan you guys came up with, I like the respect you're giving to the Wolves, and I like you as President."

            scene v14s23_5
            with dissolve

            pause 0.75
            
            scene v14s23_5a
            with dissolve

            pause 0.75

            scene v14s23_4a
            with dissolve

            cl "Thank you so much, Chris! This is going to help tremendously."

            scene v14s23_2c
            with dissolve

            ch "That's what I'm-"

    else:
        scene v14s23_4a
        with dissolve

        cl "I'm glad you asked, hehe..."

        cl "After a quick talk with [name], we've decided that we're gonna get this really cute plush toy Wolf to pose with."

        scene v14s23_2c
        with dissolve

        ch "*Laughs* I know you're joking."

        scene v14s23_4a
        with dissolve

        cl "I'm serious! I think it'd be cute."

        scene v14s23_2c
        with dissolve

        ch "I agree, it would be cute. Cute isn't the kind of image I'm trying to have on the Wolves."

        scene v14s23_4e # FPP. Same as v14s23_4a, Chloe slight pouty face, mouth open.
        with dissolve

        cl "Maybe you're right..."

        scene v14s23_4f # FPP. Same as v14s23_4b, Chloe looking at MC with puppy dog eyes and pouty face, mouth closed.
        with dissolve

        menu:
            "Agree with Chris":
                $ add_point(KCT.BRO)
                $ v14_chrissupport = 3

                scene v14s23_2b
                with dissolve

                u "Looking back on it now, a plush toy probably wasn't the best idea..."
                u "But let's be clear, any \"image\" that gets out will be the image of supporting Chloe's campaign."

                u "It's not really about what the Wolves will look like."

                if joinwolves:
                    u "The only thing put on the Wolves is that you're supporting Chloe because you're respectable and trustworthy, and that's the image you want right?"
                else:
                    u "The only thing put on the Wolves is that we're supporting Chloe because we're respectable and trustworthy, and that's the image you want right?"

                scene v14s23_2a
                with dissolve

                $ set_presidency_percent(v14_lindsey_popularity - 2) #tick
                ch "Okay, damn, you little politician... *Laughs* I'm not all for the idea of it, but if you think that's our best option, I trust you."

                scene v14s23_4a
                with dissolve

                cl "Financially I think it's best, but I also just think it's extremely adorable."

                scene v14s23_2e
                with dissolve

                u "*Chuckles*"

                scene v14s23_2c
                with dissolve

                ch "*Whispers* Adorable..."

            "Disagree with Chris":
                $ v14s23_disagree = True
                $ add_point(KCT.BOYFRIEND)
                scene v14s23_2b
                with dissolve
                
                u "I gotta disagree. Having a real wolf would look like you're pandering to a masculine audience."

                scene v14s23_2a
                with dissolve

                ch "We're a male fraternity, we're not pandering to a feminine audience."

                scene v14s23_4a
                with dissolve

                cl "*Chuckles* Oh-"

                cl "Sorry for laughing, honestly. It's just..."

                cl "I know you're not some fruity fraternity and everyone else knows that too."

                scene v14s23_4c
                with dissolve

                u "*Laughs* I would hope so."

                scene v14s23_4a
                with dissolve

                cl "This entire photoshoot is for the Chicks to show our support of the Wolves, as we get the same in return."

                cl "I mean... Imagine how cute it'd be seeing all the girls walk around with little wolf plushies."

                scene v14s23_2c
                with dissolve

                ch "Hmm... You're not wrong... That's pretty damn cute."

                scene v14s23_2b
                with dissolve

                u "Good marketing right there."

                scene v14s23_2a
                with dissolve

                ch "Haha, you two are something else, really."
                
                if v14s23_agree:
                    $ v14_chrissupport = 2

                    scene v14s23_2c
                    with dissolve

                    ch "Honestly, I wish we were taken a bit more seriously than posing with toys, but..."

                    ch "I see the vision you guys have and I support the trust and respect that comes with this alliance. So, this is what I'm gonna do."

                    ch "I'm gonna back you halfway."

                    scene v14s23_4a
                    with dissolve

                    cl "Wait, what?!"

                    scene v14s23_2c
                    with dissolve

                    ch "Half of everything."

                    $ set_presidency_percent(v14_lindsey_popularity - 1) #tick
                    ch "The photoshoot, the fee for the wolf, everything. The Wolves have got half of it all."

                    scene v14s23_2e
                    with dissolve

                    u "Chris..."

                    scene v14s23_4a
                    with dissolve

                    cl "You're joking...?"

                    scene v14s23_2c
                    with dissolve

                    ch "I'm very serious. I like the plan you guys came up with, I like the respect you're giving to the Wolves, and I like you as President."

                    scene v14s23_5
                    with dissolve

                    pause 0.75

                    scene v14s23_5a
                    with dissolve

                    pause 0.75

                    scene v14s23_4a
                    with dissolve

                    cl "Thank you so much, Chris! This is going to help tremendously."

                    scene v14s23_2c
                    with dissolve

                    ch "That's what I'm-"
                        
                else:
                    $ v14_chrissupport = 1
                    scene v14s23_2c
                    with dissolve

                    ch "Overall, I hope you guys know through and through that I'm on board with supporting you and this campaign."

                    ch "However, I don't wanna be in a photoshoot with a wolf plushie."

                    scene v14s23_2b
                    with dissolve

                    u "I'm sorry man, we can try to-"

                    scene v14s23_2c
                    with dissolve

                    $ grant_achievement("agree_to_disagree")
                    ch "Don't change the plan because of me, it's really not a bad idea, but I don't wanna do it with you guys."

                    $ set_presidency_percent(v14_lindsey_popularity + 3) #tick
                    ch "I wish you luck with the campaign of course and I want the best for you, but this isn't the move for the Wolves or myself."

                    ch "Maybe something else will come up later on and I can help you out."

                    scene v14s23_4g # FPP. Same as v14s23_4a, Chloe looking at Chris, Sad expression, mouth open
                    with dissolve

                    cl "*Sighs* I understand... I will make sure it blows up though."

                    scene v14s23_4a
                    with dissolve

                    cl "When the Wolves' recruiting numbers are doubled next year, you better be thanking me."

                    scene v14s23_2c
                    with dissolve

                    ch "Haha, we'll see."

                    scene v14s23_4a
                    with dissolve

                    cl "Thanks for talking with me. I know it's-"

    play sound "sounds/vibrate.mp3"

    u "*Phone vibrates*"

    scene v14s23_2a
    with dissolve

    ch "Oh, you can get that, bro."

    scene v14s23_2b
    with dissolve

    u "Nah, it shouldn't be important. It's okay."

    play sound "sounds/vibrate.mp3"
    u "*Phone vibrates*"

    scene v14s23_4b
    with dissolve

    cl "*Laughs* Really, it's fine."

    if chloe.relationship >= Relationship.GIRLFRIEND: 
        scene v14s23_4h # FPP. Same as v14s23_4b, Chloe kissing MC on the cheek.
        with dissolve

        pause 0.75

    scene v14s23_4b
    with dissolve

    cl "You can check your phone and I'll catch up with you guys later. I have some calls to make, anyway."

    scene v14s23_2c
    with dissolve

    ch "Have a good-"

    scene v14s23_6 # TPP. Chloe dashing off away from the Wolves house, all slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v14s23_2c
    with dissolve

    ch "*Chuckles* Okay."

    scene v14s23_2b
    with dissolve

    u "I'm gonna figure out who's blowing my phone up, I'll talk to you real soon Chris."

    scene v14s23_2a
    with dissolve

    ch "Sounds good, man. Thanks for the chat."

    scene v14s23_2b
    with dissolve

    u "You too."

    scene v14s23_7 # TPP. MC walking off and looking at his phone, slight smile, mouth closed.
    with dissolve

    pause 0.75

    stop music fadeout 3
    jump v14s24