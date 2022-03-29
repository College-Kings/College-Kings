# SCENE 52: Dog Shelter reopening
# Locations: Dog Shelter
# Characters: MC (Outfit: 2), AUTUMN (Outfit: 2), LAUREN (Outfit: 3), MALE PEDESTRIAN (Outfit: x), THE DEAN (Outfit: 1), TRUCKER (Outfit: x), OSCAR (Outfit: x)
# Time: Thursday Morning

label v16s52:
    play sound "sounds/dooropen.mp3"

    scene v16s52_1 # TPP. Show MC(neutral face, mouth closed.) opening the door to the dog shelter and walking in.
    with fade

    pause 0.75

    play sound "sounds/doorclose.mp3"

    scene v16s52_2 # TPP. Show MC(neutral face, mouth closed.) walked inside of the shelter the door closing behind him.
    with dissolve

    pause 0.75

    scene v16s52_3 # TPP. MC (neutral face, mouth closed) in the lobby, looking to his right he sees two people that seem to be talking (both slight smile, mouth open.)
    with dissolve 

    pause 0.75

    scene v16s52_4 # TPP. MC (neutral face, mouth closed) walks a little further through the lobby and finds a wall that has a pic of dogs and their new owners (We need a picture with Blue/dog_name from v15s4 and their new owner and a picture of the jogger and Rubius from v16s44.)
    with dissolve 

    pause 0.75

    scene v16s52_5 # FPP. MC looking at the wall of the dogs with their new owners.
    with dissolve

    pause 0.75

    scene v16s52_6 # TPP. Close up of the picture of Blue/dog_name with his new owner.
    with dissolve
    
    pause 0.75

    if not dog_name.lower() == "blue":
        scene v16s52_6
        with dissolve

        u "(Oh, awesome, [dog_name] got adopted! He looks so happy now.)"

    else:
        scene v16s52_6
        with dissolve

        u "(Aww! Blue doesn't look so blue anymore... Haha. Looks like he went to a happy home.)"

    if v16s44_rubius_park_walk:
        scene v16s52_7 # TPP. Close up of the picture of Rubius and the Jogger.
        with dissolve

        u "(Oh, and there's Rubius! That guy must've gotten here as soon as they opened this morning...)"

    scene v16s52_8 # TPP. Show Autumn(slight smile, mouth open) walking up to MC (Slight smile, mouth closed) standing at the adoption wall.
    with dissolve

    aut "I see you're admiring our adoption wall."

    scene v16s52_9 # FPP. MC(slight smile, mouth open.) looking at Autumn (slight smile, mouth closed.) who is looking back at him. as they stand by the adoption wall.
    with dissolve

    u "Yeah, it's looking great! Seems like lots of dogs are finding new homes."

    scene v16s52_9a # FPP. MC looking at Autumn (slight smile, mouth open.) who is looking back at him. as they stand by the adoption wall.
    with dissolve

    aut "It's the best part of working here, seriously. Hopefully we can get even more pups sent to good homes today."

    scene v16s52_8a # TPP. Show Lauren(slight smile, mouth open) walking up to MC(slight smile, mouth closed) and Autumn(slight smile, mouth closed)
    with dissolve

    la "Morning!"

    if lauren.relationship >= Relationship.GIRLFRIEND:
        scene v16s52_10 # FPP. MC looking at Lauren(slight smile, mouth closed), Lauren looking at MC, Autumn (slight smile, mouth closed.) standing next to Lauren. Autumn looking at MC. 
        with dissolve

        u "Hey, beautiful. I didn't know you were coming today."

        scene v16s52_11 # TPP. Show MC and Lauren sharing quick kiss while Autumn looks away awkwardly.
        with dissolve

        pause 0.75

        scene v16s52_10a # FPP. MC looking at Lauren(winking, slight smile, mouth open). Lauren looking at MC, Autumn (slight smile, mouth closed.) standing next to Lauren. Autumn looking at MC. 
        with dissolve 

        la "Well, surprise! *Giggles*"

        scene v16s52_9b # FPP. MC looking at Autumn (slight smile, mouth open.). Autumn standing next to and looking at Lauren(slight smile, mouth closed.). Lauren looking at Autumn.
        with dissolve

        aut "Hi!"

    else:
        scene v16s52_9b
        with dissolve

        aut "Hi!"

        scene v16s52_10
        with dissolve

        u "Hey, Lauren. Good to see you."

        scene v16s52_10b # FPP. MC looking at Lauren(slight smile, mouth open) Lauren looking at MC, Autumn (slight smile, mouth closed) standing next to Lauren. Autumn looking at Lauren.
        with dissolve

        la "You too!"

    scene v16s52_10b 
    with dissolve 

    la "Sorry but... I can't stay long."

    scene v16s52_12 # TPP. Close up of Lauren (slight smile, mouth closed) digging through her pockets for money.
    with dissolve

    pause 0.75

    scene v16s52_9b
    with dissolve

    aut "Busy today?"

    scene v16s52_10c # FPP. MC looking at Lauren(slight smile, mouth open) Lauren looking at Autumn(slight smile, mouth closed). Autumn standing next to Lauren. Autumn looking at Lauren.
    with dissolve

    la "Yeah, kind of. I've got to get to campus early because there's a new girl, and I'm helping her get caught up on the coursework."

    u "(New girl? Hm...)"

    scene v16s52_9b
    with dissolve

    aut "Oh, I see. Well, she's learning from the best, haha."

    if lauren.relationship >= Relationship.GIRLFRIEND:
        scene v16s52_10
        with dissolve

        u "Very true..."

    scene v16s52_10c
    with dissolve

    la "Thank you. *Laughs*"

    la "Here, I just came to drop off a donation."

    scene v16s52_12a # TPP. Close up of Lauren(slight smile, mouth closed) giving Autumn(slight smile, mouth closed) some money.
    with dissolve

    pause 0.75

    scene v16s52_9b
    with dissolve

    aut "Aw, thanks, sissy! That's sweet... You know, you do enough around here already, you didn't have to-"

    scene v16s52_10c
    with dissolve

    la "Stop it. Take the donation, Autumn."

    scene v16s52_9b
    with dissolve

    aut "Haha, okay. Thank you."
        
    if v16_lindsey_donation >= 10: # TODO: Variable
        scene v16s52_9d # FPP. MC looking at Autumn slight smile, mouth closed.) Autumn looking at MC and standing next to Lauren.
        with dissolve

        u "Oh, yeah... Here's a small donation from Lindsey too. She asked me to pass it on."

        scene v16s52_13 # TPP. close up. show MC(slight smile, mouth closed) giving Autumn(slight smile, mouth closed) some money.
        with dissolve

        pause 0.75

        if v16_lindsey_donation == 10:
            scene v16s52_9c # FPP. MC looking at Autumn (slight smile, mouth open.). Autumn looking at MC and standing next to Lauren(slight smile, mouth closed.). Lauren looking at Autumn. 
            with dissolve

            aut "Thanks, [name]. That's really kind of her!"

            if mc.money >= 10:
                $ mc.money -= 10 

        elif v16_lindsey_donation == 50:
            if mc.money >= 50:
                $ mc.money -= 50

            scene v16s52_9c 
            with dissolve

            aut "Small?! Fifty dollars isn't exactly small... Haha. That's great!"

            scene v16s52_10c
            with dissolve

            la "Oh, yeah, for sure!"

            scene v16s52_10
            with dissolve

            u "Well, good. I'll let her know it means a lot."

            scene v16s52_9c
            with dissolve

            aut "Yeah, please do."

    elif v16_lindsey_donation == 0:
        scene v16s52_10
        with dissolve

        u "(If I hadn't spent all of Lindsey's donation money, I'd be able to offer a little bit too, but... Eh, priorities.)"

    scene v16s52_10c
    with dissolve

    la "Now I gotta run, but good luck for the day! You guys did such a great job with the place."

    scene v16s52_9b
    with dissolve

    aut "Thank you! I'll let you know how it goes, call me later?"

    scene v16s52_10b
    with dissolve

    la "Yup! I will. Bye, [name]!"

    if lauren.relationship >= Relationship.GIRLFRIEND:
        scene v16s52_10d # FPP. MC looking at Lauren. Lauren backing away and blowing a kiss at MC. Autumn (slight smile, mouth closed) looking at Lauren.
        with dissolve

        u "Laters, baby."

        scene v16s52_10e # FPP. MC looking at Lauren. Lauren turned around walking away while she laughs.
        with dissolve

        pause 0.75

        scene v16s52_9a
        with dissolve

        aut "*Laughs* Laters baby?"

        scene v16s52_9
        with dissolve

        u "Uh, I don't know where that came from actually... Can we just act like-"

        scene v16s52_9a
        with dissolve

        aut "Haha, yes... Let's pretend you didn't just say that. *Giggles*"

    else:
        scene v16s52_10
        with dissolve

        u "See ya, Lauren."

        scene v16s52_10f # FPP. MC looking at Lauren. Lauren turned around walking away.
        with dissolve

        pause 0.75

    if v15_autumn_freemug:
        scene v16s52_9a
        with dissolve

        aut "Oh! Before I forget..."

        aut "I promised you a free mug, didn't I?"

        scene v16s52_9
        with dissolve

        u "You certainly did, thanks for remembering."

        scene v16s52_9a
        with dissolve

        aut "A promise is a promise, [name]. *Chuckles*"

        aut "But I didn't bring it because I didn't want you to have to carry it around with you all day... Haha."

        scene v16s52_9
        with dissolve

        u "Ah, smart idea."

        scene v16s52_9a
        with dissolve

        aut "I set it aside back at the Deer's house, so you can just come by whenever to pick it up."

        scene v16s52_9
        with dissolve

        u "Okay, cool. I can't wait to drink out of my mutt mug."

        scene v16s52_9a
        with dissolve

        aut "*Gasps* I should've named them that!"

        scene v16s52_14 # TPP. MC and Autumn both laughing.
        with dissolve

        pause 0.75

    scene v16s52_9a
    with dissolve

    aut "Hmm..."

    scene v16s52_9
    with dissolve

    u "Hmm... what?"

    scene v16s52_9a
    with dissolve

    aut "*Chuckles* Well... You've been such a huge help already, but I was just wondering if you might be able to assist me with one more thing today?"

    scene v16s52_9
    with dissolve

    u "What's that?"

    scene v16s52_9a
    with dissolve

    aut "To be honest with you, we're not hitting any of our donation goals. Partly because not many people have shown up besides our regular volunteers."

    scene v16s52_9
    with dissolve

    u "Damn, okay. Do you have any ideas on how to get more people to come?"

    scene v16s52_9a
    with dissolve

    aut "That's what I was going to ask. There are two options."

    aut "Do you know anyone with a big number of followers, who could do a Kiwii post about us?"

    scene v16s52_9
    with dissolve

    u "Um, well maybe-"

    scene v16s52_9a
    with dissolve

    aut "Or maybe you can spin a sign out front? That's the other option. *Laughs*"

    scene v16s52_9
    with dissolve

    u "Wait, do you even have a sign?"

    scene v16s52_9a
    with dissolve

    aut "Yeah, I had one made specifically for today but nobody's confident enough to try it out."

    scene v16s52_9
    with dissolve

    u "No one wants to stand by the street flipping a sign around? You're kidding..."

    scene v16s52_9e # FPP. MC looking at Autumn (rolling eyes,slight smile, mouth closed.) who is looking back at him. as they stand by the adoption wall.
    with dissolve

    aut "I know it doesn't sound very fun but, what do you think?"

    scene v16s52_9
    with dissolve

    menu:
        "Kiwii post":
            $ add_Point(KCT.BOYFRIEND)
            scene v16s52_9
            with dissolve

            u "I think a Kiwii Post is a great idea."

            scene v16s52_9a
            with dissolve

            aut "Yeah, but who posts it? I don't have that many followers and you barely have-"

            scene v16s52_9
            with dissolve

            u "Woah, okay. No need to shame."

            scene v16s52_9a
            with dissolve

            aut "Haha, I'm just saying!"

            scene v16s52_9
            with dissolve

            u "The most ideal person for a post would probably be Aubrey. She is modeling for Lew's these days, haha."

            scene v16s52_9a
            with dissolve

            aut "Oh, shit! That's a great idea! I didn't even think of that. Are you sure she'd help?"

            scene v16s52_9
            with dissolve

            u "I don't see why not, but I'll text her for you."

            scene v16s52_9a
            with dissolve

            aut "Ugh, you're the best."

            scene v16s52_15 # TPP. Show MC(slight smile, mouth closed) looking at his phone, Autumn (slight smile, mouth closed) infront of MC.
            with dissolve

            pause 0.75

            $ aubrey.messenger.addReply("Hey, Aubrey. I'm with Autumn right now at the dog shelter for the re-opening, and we kind of need your help.")
            $ aubrey.messenger.newMessage("I'm not able to come, but can I help from here?")
            $ aubrey.messenger.addReply("Yeah, we don't need much at all. The thing is, we need more donations. Well, more people with donations...")
            $ aubrey.messenger.newMessage("Hmm... Where do I come in? Lmao")
            $ aubrey.messenger.addReply("What about using your modeling powers, aka your large fanbase, and encouraging people to show up??? I'll make it up to you... ;)")
            
            if aubrey.relationship == Relationship.FRIEND or aubrey.relationship == Relationship.TAMED: ###???
                $ aubrey.messenger.newMessage("Oh, yea. No prob, I'll be happy to help :) I've got the perfect pic for it too!")
                $ aubrey.messenger.addReply("Thank you! You're the best!")
                $ aubrey.messenger.newMessage("You owe me, haha :P")
                
                label v16s52_PhoneContinueAub:
                    if aubrey.messenger.replies:
                        call screen phone
                    if aubrey.messenger.replies:
                        u "(I should reply to Aubrey.)"
                        jump v16s52_PhoneContinueAub

                scene v16s52_9
                with dissolve
                
                u "She's gonna do it."

                scene v16s52_9a
                with dissolve

                aut "Amazing! I love her so much."

                scene v16s52_9
                with dissolve

                u "Haha, she's pretty great."

                #! v16s52kw_1 Aubrey in a comfy sweater and blue jeans, professional photo shoot photo with a puppy in her lap

                $ v16s52_kiwiiPost1 = KiwiiPost(aubrey, "v16/v16s52_aubpost1.webp", "Good morning people! Today is such a huge day for a friend of mine. The re-opening of the local dog shelter is taking place right now, and they could use any help they can get! Head over there to donate, adopt, or even shop; They've got some really cute merchandise. #AdoptDon'tShop #OrDoBoth <3", numberLikes=3718)
                $ v16s52_kiwiiPost1.new_comment(autumn, "Thank you Aubrey! <3 We can't wait to see everyone. Address is 0417 Alanis Street near SVC :)", numberLikes=1518, force_send=True)
                $ v16s52_kiwiiPost1.new_comment(chloe, "When did you do this photoshoot, omg?!", numberLikes=417, force_send=True)
                $ v16s52_kiwiiPost1.new_comment(imre, "Aw man! I want a puppy!", numberLikes=545, force_send=True)
                $ v16s52_kiwiiPost1.new_comment(sebastian, "Hmm... A puppy, eh?", numberLikes=961, force_send=True)
                $ v16s52_kiwiiPost1.new_comment(lauren, "This is so cool of you, Aubrey <3", numberLikes=1070, force_send=True)
                $ v16s52_aubrey_kiwii_post_for_donations = True

                if False: # For Lint
                    scene v16s52_aubpost1
                    with dissolve

            elif v16_aubrey_date and aubrey.relationship < Relationship.TAMED:
                $ aubrey.messenger.newMessage("Sorry, [name]... But I don't want to risk interfering with my brand. Lew's might not like me doing free dog shelter promoting, you know?", force_send=True)
                $ aubrey.messenger.addReply("Oh, yeah. I get it, that's okay. Thanks")
                $ aubrey.messenger.newMessage("Good luck")

                label v16s52_PhoneContinueAub2:
                if aubrey.messenger.replies:
                    call screen phone
                if aubrey.messenger.replies:
                    u "(I should reply to Aubrey.)"
                    jump v16s52_PhoneContinueAub2

                scene v16s52_9
                with dissolve

                u "*Sighs* (She's been nothing but short with me since our date...)"

                scene v16s52_9a
                with dissolve

                aut "No luck?"

                scene v16s52_9
                with dissolve

                u "She's too busy right now. I'll do one instead. though."

                scene v16s52_9a
                with dissolve

                aut "Oh... Alright, hopefully it'll still bring a few people around."

                scene v16s52_9
                with dissolve

                u "Grabbing a random photo from the internet..."

                scene v16s52_9a
                with dissolve

                aut "Haha, professional."

                scene v16s52_9
                with dissolve

                u "And... Posted."

                #! v16s52kw_2 A stock photo that mc found on the internet of a puppy
                $ v16s52_mc_dogshelter_kiwii_post = True

                $ v16s52_kiwiiPost2 = KiwiiPost(mc, "v16/v16s52_post2.webp", "The puppies need you! Come to 0417 Alanis Street near SVC if you're looking to adopt or donate. We need all the help we can get! :)", numberLikes=479)
                $ v16s52_kiwiiPost2.new_comment(autumn, "Yes, please come see us! We have merchandise too <3", numberLikes=47, force_send=True)
                $ v16s52_kiwiiPost2.new_comment(lindsey, "Hope you got my donation!", numberLikes=25, force_send=True)
                
                if False: # For Lint
                    scene v16s52_post2
                    with dissolve
                
                if v16_lindsey_donation >= 10:
                    $ v16s52_kiwiiPost2.new_comment(autumn, "Yes, received! Thank you so so much :D", mentions=lindsey, numberLikes=146, force_send=True)
                
                elif v16_lindsey_donation == 0:
                    $ v16s52_kiwiiPost2.new_comment(autumn, "Must have missed it... Where did you send it?", mentions=lindsey, numberLikes=119, force_send=True)
                
                $ v16s52_kiwiiPost2.new_comment(aubrey, "Good luck u guys :)", numberLikes=91, force_send=True)
                $ v16s52_kiwiiPost2.new_comment(lauren, "Sending everyone I run into over to you guys!", numberLikes=46, force_send=True)

            scene v16s52_9
            with dissolve 

            u "Let's see what happens, I guess."

            scene v16s52_9a
            with dissolve

            aut "Yay! Thanks, [name]."

            scene v16s52_9
            with dissolve

            u "Now we just sit back and watch the cash roll in, haha."

            scene v16s52_9a
            with dissolve

            aut "I wish... We need every dollar we can get."

            scene v16s52_16 # TPP. Show MC (Slight smile, mouth closed) playing with dogs in the play area.
            with fade

            pause 0.75

            scene v16s52_17 # TPP. Show MC (Slight smile, mouth closed) looking at a poster in the dog shelter
            with fade

            pause 0.75

            scene v16s52_17a # TPP. Show MC (slight smile, mouth closed) looking at a poster in the dog shelter while Autumn (slight smile, mouth closed) taps on his shoulder from behind.
            with dissolve 

            pause 0.75

            play sound "sounds/dooropen.mp3"

            scene v16s52_18 # TPP. Show MC (slight smile, mouth closed) turning around to see Autumn (slight smile, mouth open). Autumn pointing at the entrance showing the Dean(neutral face, mouth closed) walking in the dog shelter.
            with dissolve

            aut "Oh, sh- *Whispers* [name], look who it is!"

            play sound "sounds/doorclose.mp3"

            scene v16s52_19 # TPP. Close up of the Dean (neutral face, mouth closed) standing in the lobby as the door closed behind her.
            with dissolve

            u "Is she looking to adopt?"

            aut "Guess we'll find out."

        "Spin sign":
            $ add_Point(KCT.BRO)
            scene v16s52_9
            with dissolve

            u "I'll take the sign out for a spin, I guess."

            scene v16s52_9a
            with dissolve

            aut "Aw, perfect! Let me go fetch it for you."

            aut "Err, I mean... Grab it for you. Sorry, dog brain. *Laughs*"

            scene v16s52_9f # FPP. MC watching Autumn walk away from him to go grab the sign.
            with dissolve 
            
            pause 0.75

            scene v16s52_20 # TPP. Show MC (slight smile, mouth closed) outside by the entrance of the Dog shelter holding a big arrow sign "Love dogs? Come say hello!" with a dog picture if possible.
            with fade

            pause 0.75

            scene v16s52_20a # TPP. Show MC (slight smile, mouth closed) outside by the entrance of the Dog Shelter trying to spin the sign.
            with dissolve 

            pause 0.75

            play sound "sounds/thud.mp3"

            scene v16s52_20b # TPP. Show MC (slight smile, mouth closed) about to catch the sign but drops it and it hits the floor.
            with vpunch

            u "(Fuck. This is harder than it looks.)"

            scene v16s52_21 # TPP. Close up of MC (neutral face, mouth closed) picking up the sign off the floor.
            with dissolve

            u "(Fucking thing... Why did I just assume I could do this?)"

            scene v16s52_22 # FPP. MC bent over looking up at the Male Pedestrian(smirk, mouth open) who is walking by looking at MC.
            with dissolve

            mped "Don't quit your day job, kid. *Laughs*"

            scene v16s52_23 # FPP. MC standing up straight looking at the Male Pedestrian walking away, the Male Pedestrian looking ahead and doesn't look back at MC.
            with dissolve

            menu:
                "I'm unemployed":
                    scene v16s52_23
                    with dissolve

                    u "Haha, the joke's on you. I'm unemployed!"

                    scene v16s52_23a # FPP MC standing up straight looking at the Male Pedestrian now further ahead, the Male Pedestrian looking ahead and doesn't look back at MC.
                    with dissolve

                    mped "*Scoffs* Say it louder, loser."

                "Fuck off":
                    $ add_Point(KCT.TROUBLEMAKER)
                    scene v16s52_23
                    with dissolve 

                    u "Fuck off, man. This is for a good cause!"

                    mped "Hey! Fuck you too!"

                    scene v16s52_23a
                    with dissolve

                    u "Ah, go suck a fat fuckin' egg would ya?"

                    scene v16s52_23b # MC standing up straight looking at the Male Pedestrian(Confused, mouth opened.) stood still now turning back to look at MC. 
                    with dissolve

                    mped "\"Go suck an egg?\" Nice one, pal."

                    scene v16s52_23a
                    with dissolve

                    u "(Why did I just say that...? *Sighs* This job is changing me.)"

    scene v16s52_20
    with dissolve

    u "(I didn't come out here to yell at people... We're here for donos.)"

    scene v16s52_20a
    with dissolve

    pause 0.75

    play sound "sounds/thud.mp3"

    scene v16s52_20b
    with vpunch

    u "(It's just demeaning at this point...)"

    scene v16s52_24 # FPP. MC looking at the Dean(neutral face, mouth closed) walking to the Dog Shelter entrance.
    with dissolve

    u "Oh- Hello, Dean Harrison."

    scene v16s52_24a # FPP. MC looking at the Dean(neutral face, mouth opened) now standing still and looking back at MC.
    with dissolve

    de "Hi, [name]. It's nice to see you helping out the community. Keep persevering, you'll get the hang of it eventually."

    play sound "sounds/dooropen.mp3"

    scene v16s52_25 # TPP. Show the Dean(neutral face, mouth closed.) walking into the dog shelter.
    with dissolve

    u "Haha, thanks."

    u "(Hmm, maybe she's thinking about adopting?)"

    play sound "sounds/doorclose.mp3"

    scene v16s52_25a # TPP. Show just the Dog shelter entrance door closed.
    with dissolve

    u "(I might as well throw in the towel and go find out... This sign isn't getting us anywhere.)"

    ### ERROR: [End of Checkpoint 1.2. Continue to Checkpoint 2]

### ERROR: [Checkpoint 2]

# -Oscar the dog is sitting by the reception desk. A man wearing a trucker cap looks down at him-
    scene v16s52_26 # TPP. Inside of the dog shelter show Oscar the dog sitting by the reception desk with a happy oblivious look. A trucker(disgusted face, mouth open.) wearing a cap near Oscar looking down at him
    with fade

    trucker "Ah, man. Look at that ugly face... What a mutt!"

    trucker "I've never seen such a gross looking creature, haha!"

    u "(Well, that's rude.)"

    scene v16s52_27 # FPP. MC looking ahead at Autumn(slightly angry, mouth open) who is walking infront of him towards the trucker(disgusted face, mouth closed.) who is looking at Autumn as she approaches.
    with dissolve

    aut "Hey-"

    scene v16s52_28 # FPP. MC looking at the Dean(angry, mouth open) walking up to the trucker(disgusted, mouth closed.) Oscar sitting nearby looking at them oblivious.
    with vpunch

    de "Excuse me?"

    scene v16s52_28a # FPP. MC looking at the Dean (angry, mouth closed) looking at the trucker(confused, mouth open.) who is looking back at her.
    with dissolve

    trucker "Hm?"

    scene v16s52_28b # FPP. MC looking at the Dean (angry, mouth open) looking at the trucker(confused, mouth closed.) who is looking back at her.
    with dissolve

    de "Don't speak to him like that."

    scene v16s52_28a
    with dissolve

    trucker "Why not? Don't start acting like he can understand anything I'm sayin' lady."

    scene v16s52_28b
    with dissolve

    de "You're clearly an uneducated individual."

    scene v16s52_28a
    with dissolve

    trucker "I'm a what?"

    scene v16s52_28b
    with dissolve

    de "This is a wonderful looking dog, and you've been disrespectful."

    scene v16s52_28c # FPP. MC looking at the Dean (angry, mouth closed) and trucker(angry, mouth open.) who is looking back at her.
    with dissolve

    trucker "Look, I'm going to pretend that I didn't just hear you call me an idiot... 'Cause I'm not here to waste my time on an argument."

    scene v16s52_28d # FPP. MC looking at the Dean (angry, mouth open) looking at the trucker(angry, mouth closed.) who is looking back at her.
    with dissolve

    de "Right then, why are you here?"

    scene v16s52_28e # FPP. MC looking at the Dean (angry, mouth closed) looking at the trucker(angry, mouth closed) who is looking back at her.
    with dissolve

    aut "Dean Har-"

    scene v16s52_28c
    with dissolve

    trucker "I wanted to see what kind of dogs that had locked up in here, now I can clearly see they're just a range of dirty mutts."

    scene v16s52_28d
    with dissolve

    de "Hm. I think I see what's happening here."

    scene v16s52_28e
    with dissolve

    u "You do?"

    scene v16s52_28d
    with dissolve

    de "Of course, students. This gentleman must feel so sad, so... Impotent."

    scene v16s52_28e
    with dissolve

    aut "Ha!"

    scene v16s52_28d
    with dissolve

    de "Such a sad, angry man..."

    scene v16s52_28c
    with dissolve

    trucker "Listen here, you-"

    scene v16s52_28d
    with dissolve

    de "No one left to put up with your negative attitude towards life, so you've come here to take your frustration out on those who can't talk back."

    de "That's rather pathetic, don't you think?"

    scene v16s52_28c
    with dissolve

    trucker "Who are you calling impotent, you evil bitch?"

    scene v16s52_28e
    with dissolve

    aut "Um, excuse me! You need to leave, sir. That language is unacceptable."

    scene v16s52_29 # FPP. MC looking at the trucker (angry, mouth open) who is looking at Autumn.
    with dissolve

    trucker "*Scoffs* Whatever, forget this place anyway!"

    play sound "sounds/dooropen.mp3"

    scene v16s52_30 # TPP. Show MC (Neutral face, mouth open) opening the door for the Trucker(angry, mouth closed)
    with dissolve

    u "Alright, come on-"

    scene v16s52_31 # TPP. Close up of the Trucker(angry, mouth open) flipping off the group as he leaves.
    with dissolve

    trucker "I'll go somewhere else where there aren't any crying bitches!"

    scene v16s52_30a # TPP. Show MC (Neutral face, mouth open) closing the door the trucker now gone.
    with dissolve

    pause 0.75

    scene v16s52_32 # FPP. Standing by the reception desk MC looking at the Dean (neutral face, mouth open) who is looking at him and Autumn.
    with dissolve 

    de "The general public these days... I'm beginning to worry about this world."

    scene v16s52_33 # FPP. Standing by the reception desk MC looking at Autumn(Neutral face, mouth open) who is looking at the Dean.
    with dissolve

    aut "Oh?"

    scene v16s52_32a # FPP. Standing by the reception desk MC looking at the Dean(slight smile, mouth open) who is looking down at Oscar.
    with dissolve

    de "*Baby voice* That big meanie doesn't know what he's talking about, huh? You're the most handsome little fella here, aren't you?"

    scene v16s52_34 # TPP. Shot from behind the Dean of her bending over and patting Oscar on the head.
    with dissolve

    pause 0.75

    scene v16s52_33 
    with dissolve

    aut "Thanks for that."

    scene v16s52_32b # FPP. Standing by the reception desk MC looking at the Dean(slight smile, mouth open) who is looking at MC and Autumn.
    with dissolve

    de "Don't mention it, Autumn. Men like that are barely worth wasting our breath on... I was just a little bored. *Chuckles*"

    scene v16s52_35 # TPP. Cute shot of Oscar the dog with his tongue out and his ears up.
    with dissolve

    de "So, what's his name?"

    aut "Oscar."

    de "Oscar, hm? Seems to fit, you're happy with it?"

    scene v16s52_35a # TPP. Cute shot of Oscar the dog barking.
    with dissolve

    oscar_dog "Arf! *Panting*."

    scene v16s52_32b
    with dissolve

    de "Very well. What paperwork do I need to sign?"

    scene v16s52_33
    with dissolve

    aut "Um, paperwork?"

    scene v16s52_32b
    with dissolve

    de "To adopt him?"

    scene v16s52_33a # FPP. Standing by the reception desk MC looking at Autumn(slight smile, mouth open) who is looking at the Dean.
    with dissolve

    aut "Oh, sorry, haha! You want to adopt him? Just like that? I mean-"

    scene v16s52_32b
    with dissolve

    de "Yes, let's get on with it. I have a busy day ahead."

    scene v16s52_33
    with dissolve

    aut "S-sure thing! Please follow me, and we'll get everything sorted. [name], do you want to stay here with him?"

    scene v16s52_33b # FPP. Standing by the reception desk MC looking at Autumn(slight smile, mouth closed) who is looking back at MC.
    with dissolve

    u "Yeah, no problem."

    scene v16s52_36 # FPP. MC looking at Autumn and the Dean walk away to do paperwork.
    with dissolve

    pause 0.75

    scene v16s52_37 # TPP. A shot of MC(slight smile, mouth open) sitting on the floor with Oscar sitting next to him. Oscar and MC looking at each other.
    with dissolve

    u "Well done, little guy! Looks like you've got a new mom. Are you excited?"

    scene v16s52_37a # TPP. Show MC(slight smile, mouth closed) playing with Oscar.
    with dissolve

    pause 0.75

    scene v16s52_38 # FPP. MC looking at the Dean (slight smile, mouth closed) who has Oscar on a leash and Autumn(slight smile, mouth open). Autumn looking at the Dean and the Dean looking back at her.
    with dissolve 

    aut "And just one final thing before you take him home... A photo for our adoption wall, say cheese!"

    play sound "sounds/capture.mp3"

    scene v16s52_39 # TPP. Shot infront of the Dean and Oscar smiling for the photo
    with flash

    aut "Thank you!"

    scene v16s52_40 # FPP. Outside the shelter. Shot of the Dean and Oscar walking away from the Dog shelter.
    with dissolve

    de "Come on, Oscar. Let's get home!"

    scene v16s52_41 # FPP. MC and Autumn(slight smile, mouth open.) standing outside. MC looking at Autumn. Autumn looking back at MC.
    with dissolve 

    aut "Aw, I'm so happy for him! And I don't think she'll have any weed lying around for him to eat... *Giggles*"

    scene v16s52_41a # FPP. MC and Autumn(slight smile, mouth closed) standing outside. MC looking at Autumn. Autumn looking back at MC.
    with dissolve

    u "Haha, yeah. Me neither. I think Oscar has finally found his forever home."

    scene v16s52_41
    with dissolve

    aut "Me too, I've never seen her smile that much before! Haha..."

    aut "Anyways, I appreciate you coming. You don't have to hang around any longer, I know you've got an entire day ahead of you, haha."

    scene v16s52_41a
    with dissolve

    u "That I do. *Chuckles* Thanks for the invite though, I had fun."

    scene v16s52_41
    with dissolve

    aut "Of course! You're welcome here anytime."

    if autumn.relationship >= Relationship.KISS:
        scene v16s52_41a
        with dissolve

        u "Will I see you again soon?"

        scene v16s52_41
        with dissolve

        aut "I suppose you might..."

        play sound "sounds/kiss.mp3"

        scene v16s52_42 # TPP. Show MC kissing Autumn(blushing, smile, mouth closed)
        with dissolve

        pause 0.75

    scene v16s52_41a 
    with dissolve

    u "Okay. Bye, Autumn."

    scene v16s52_41
    with dissolve

    aut "Bye!"

    scene v16s52_43 # TPP. Shot from the front of MC(slight smile,mouth closed) walking away from the dog shelter. Autumn(smile, mouth closed.) in the background waving.
    with dissolve

    pause 0.75

    jump v16s53