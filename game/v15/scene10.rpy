# SCENE 10: Creepy or Nice Car Buyer
# Locations: Place where Lindsey's car photos were shot.
# Characters: LINDSEY (Outfit: 1), MC (Outfit: 5), male_buyer (Outfit: x), female_buyer (Outfit: x)
# Time: Afternoon

label v15s10:
# -Car totals for this scene can be calculated via Oscar or the document that Cheex can give you access to-
# -MC arrives at the Lindsey car location. The car is in the same position as before. Lindsey is leaning against it, waiting. She turns to see MC approaching and gives him a nice smile-

    scene v15s10_1 # TPP. Show MC walking down the sidewalk near where they took the picture for lindsey car, Slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s10_2 # TPP. Show MC walking towards the car, Lindsey leaning against the car waiting, Lindsey on her phone, neutral face, mouth closed
    with dissolve

    pause 0.75

    scene v15s10_3 # FPP. Show Lindsey turning her head as MC approaches her, Lindsey slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s10_4 # FPP. MC standing infront of Lindsey, Lindsey still leaning against the car, Lindsey slight smile, mouth open.
    with dissolve

    li "Hey! Thanks for coming. I'm going to let you be the sales negotiator. *Laughs* I think you'll be better at it than me."

    scene v15s10_4a # FPP. Same as v15s10_4, Lindsey slight smile, mouth closed.
    with dissolve

    u "No pressure then, haha."

    scene v15s10_4
    with dissolve

    li "You'll be fine! I believe in you, [name]."

    if v14_pics_with_linds:
        if "v14s47_passenger_2b.webp" in v14s47_car_pics:
            $ v14s48_car_price += 50
        scene v15s10_5 # FPP. Show a creepyish guy approaching, the man dressed in a smart casual sense, the man slight smile, mouth closed
        with dissolve

        pause 0.75

        scene v15s10_5a # FPP. The man getting close and his attention set on Lindsey, the man creepy smile, mouth open.
        with dissolve

        male_buyer "Hey, pretty lady! I recognize you from the photos. Honestly, that's the only reason I'm here. *Laughs*"

        scene v15s10_4b # FPP. MC looking at Lindsey, Lindsey looking down at her phone, Lindsey weirded out face, mouth open.
        with dissolve

        li "Oh... Well, that's nice..."

        scene v15s10_5b # FPP. Same as v15s10_5a, The man looking over at MC and realizing he has been there the whole time, the man surprised, mouth closed.
        with dissolve

        u "So, here's the car."

        scene v15s10_5c # FPP. Same as v15s10_5b, The man slight smile, mouth open.
        with dissolve

        male_buyer "Hey, my dude!"

        male_buyer "Listen, I am fully interested in the car. Money is not a problem, so I'm happy to negotiate a price."

        scene v15s10_5d # FPP. Same as v15s10_5c, The man slight smile, mouth closed.
        with dissolve

        u "You haven't even looked at it yet haha."

        scene v15s10_6 # TPP. Of the man pulling MC aside and facing their back towards Lindsey, Lindsey in the background looking at her phone not paying attention, Lindsey neutral face, mouth closed, the man slight smile, mouth closed, MC slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s10_7 # FPP. Just able to see the man next to him, the man looking at MC, the man slight smile, mouth open.
        with dissolve

        male_buyer "Bro, this girl is worth whatever price you're asking for. It's like a two for one deal!"

        scene v15s10_7a # FPP. The man, slight smile, mouth closed.
        with dissolve

        u "Sadly, my guy, the girl isn't for sale."

        scene v15s10_7
        with dissolve

        male_buyer "Okay then, so give me her number. *Whispers* I'll slip you an extra fifty bucks."

        scene v15s10_8 # TPP.The man next to MC, MC turned around looking at Lindsey, MC slight smile, mouth open.
        with dissolve

        u "He said he'll give us an extra fifty if I give him your number!"

        scene v15s10_7b # FPP. Same as v15s10_7a, The man neutral expression, mouth open.
        with dissolve

        male_buyer "Dude what the fu- *Whispers* Not. Cool."

        scene v15s10_9 # TPP. Close up of Lindsey with a weirded out face looking at her phone still, mouth open.
        with dissolve

        li "Um... Sorry, I- I already have a boyfriend."

        scene v15s10_7c # FPP. Same as v15s10_7b, The man looking back at Lindsey and pointing at MC, the man neutral face, mouth open.
        with dissolve

        male_buyer "This guy?"

        if lindsey.relationship.value >= Relationship.FWB.value:
            scene v15s10_10 # FPP. MC turned around looking at Lindsey (v15s10_8 just FFP), Lindsey looking straight ahead at MC while she leans against the car, winking at MC, slight smile, mouth open.
            with dissolve

            li "Uhh, yes?"

            scene v15s10_7d # Same as v15s10_7c, still looking at Lindsey, the man slight smile, mouth open.
            with dissolve

            male_buyer "*Scoffs* Yeah, right!"

            scene v15s10_7b
            with dissolve

            u "Haha no, he's actually an MMA fighter. In New York this week, right?"

            scene v15s10_10a # FPP. Same as v15s10_10, Lindsey no longer winking, back to looking at her phone, slight smile, mouth open.
            with dissolve

            li "Oh, yeah. He's really fit... Like super fit, you know. Like, muscles and... All of that."

            scene v15s10_10b # FPP. Same as v15s10_10a, Lindsey slight smile, mouth closed.
            with dissolve

            u "*Laughs*"

        else:
            scene v15s10_10a
            with dissolve

            li "No, my boyfriend is a big guy. He's a professional MMA fighter, so he's really fit and muscular..."

            scene v15s10_10b
            with dissolve

            u "*Chuckles*"

        scene v15s10_7b
        with dissolve

        male_buyer "Oh, shit. Well, I gotta respect that. Don't want to be messing with a fighter's girl... Not after last time."

        scene v15s10_7d
        with dissolve

        male_buyer "You know, you don't even have to try... You can just stand pretty right there all day, just like in the photos."

        scene v15s10_10c # FPP. Same as v15s10_10b, Lindsey looking at her phone still, slightly weirded out, mouth open.
        with dissolve

        li "Um... Thanks."

        scene v15s10_7d
        with dissolve

        male_buyer "Like, I really loved them."

        male_buyer "I printed that one out and stuck it on my wall."

        scene v15s10_10d # FPP. Same as v15s10_10c, Lindsey disgusted, mouth closed.
        with dissolve

        li "Ugh."

        scene v15s10_7a
        with dissolve

        u "Maybe you should keep that information to yourself."

        scene v15s10_7
        with dissolve

        male_buyer "No way, bro! Always show your appreciation to the babes, my friend, and you'll go far."

        scene v15s10_7a
        with dissolve

        u "You do seem like an expert in that-"

        scene v15s10_7
        with dissolve

        male_buyer "You know it!"

        male_buyer "Let me take a look at this piece of junk then."

        if v14s48_car_description == CarDescription.LIE:
            $ v14s48_car_price -= 200
            scene v15s10_11 # TPP. Show MC and the man walking towards the car, Lindsey walking off to the side still looking at her phone.
            with dissolve

            pause 0.75

            scene v15s10_12 # FPP. The man looking at the car, neutral expression, mouth closed.
            with dissolve

            pause 0.75

            scene v15s10_12a # FPP. Same as v15s10_12, The man looking looking at MC, the man unamused, mouth closed.
            with dissolve
            
            u "It's an exceptional vehicle. We've had a lot of interest in it."

            scene v15s10_12b # FPP. Same as v15s10_12, the man unamused, mouth open.
            with dissolve

            male_buyer "Exceptional my ass! This car does not fit the description in the advertisement at all. Are you sure this is the same car?"

            scene v15s10_12a
            with dissolve

            u "Same one, swear. And every word in that ad is accurate. This is a modern, imported, classic sports car."

            scene v15s10_12b
            with dissolve

            male_buyer "No, my dude... I'm looking right at it. You totally lied... I hate being lied to!"

            male_buyer "This chunk of metal is on its last legs, and I need something to entice the babes... This ain't it."

            male_buyer "I'm out."

            scene v15s10_12c # FPP. Same as v15s10_12b, The man starting to walk away from the area, his face not shown.
            with dissolve
            
            pause 0.75

            scene v15s10_13 # FPP. MC looking at Lindsey, Lindsey in panic coming up with something, Lindsey looking past MC at the man, Lindsey slight smile, mouth open.
            with vpunch

            li "Hey! Come back here, you... sexy man!"

            scene v15s10_13a # FPP. Same as v15s10_13, Lindsey slight smile, mouth closed.
            with dissolve

            u "*Laughs* Sexy man?"

            scene v15s10_13b # FPP. Same as v15s10_13a, Lindsey looking at MC now, Lindsey winking at MC, slight smile, mouth open.
            with dissolve

            li "Shh, just go with it..."

            scene v15s10_12c
            with dissolve

            pause 0.75

            scene v15s10_12d # FPP. Same as v15s10_12c, The man stopped in place his back still turned.
            with dissolve

            pause 0.75

            scene v15s10_12k # FPP. The man walking back towards them and the car, looking past MC and staring straight at Lindsey, The man smiling, mouth open.
            with dissolve

            male_buyer "Oh, so you've changed your mind about me now, baby?"

            scene v15s10_13c # FPP. Same as v15s10_13b, Lindsey looking past MC at the man, Lindsey slight smile, mouth open.
            with dissolve

            li "Uh, yeah, I'd hate to see you walk away from such an amazing deal..."

            li "And maybe if you buy it, I'll give you my number after all."

            scene v15s10_12l # FPP. Same as v15s10_12c, the man stopped next to MC by the car, looking over at Lindsey, the man smiling, mouth open.
            with dissolve

            male_buyer "For real? Seriously?!"

            scene v15s10_13a
            with dissolve

            u "Yeah, Linds, for real?"

            scene v15s10_13c
            with dissolve

            li "For real."

            scene v15s10_12d
            with dissolve

            male_buyer "Okay, umm... This still isn't the car I thought I was coming to see, I mean..."

            male_buyer "It needs a lot of work, but it does have potential."

            male_buyer "This is the best I can do."

        # -[CarTotal] pops up on screen based on the pay out sums (if lied, total they can receive is minus200$ off the car's worth price)-
        # Hi Oscar :D
            
            scene v15s10_12e # FPP. Same as v15s10_12d, Man holding cash up, slight smile, mouth closed.
            with dissolve

            pause 0.75

            scene v15s10_14 # FPP. MC looking down at his hands counting the money.
            with dissolve

            u "(That's two hundred dollars less than what this thing is worth! What should I do here?)"

            menu:
                "Refuse offer":
                    scene v15s10_12f # FPP. same as v15s10_12e, Man not holding cash anymore, neutral face, mouth closed.
                    with dissolve

                    u "I'm sorry but... We need more than that."

                    scene v15s10_12g # FPP. Same as v15s10_12f, the man neutral face, mouth open.
                    with dissolve

                    male_buyer "I'm not going a cent higher, mister pants on fire..."

                    scene v15s10_12f
                    with dissolve

                    u "*Scoffs* Come on, it-"

                    scene v15s10_13d # FPP. Lindsey looking at Mc, Lindsey neutral face, mouth open
                    with dissolve

                    li "It's fine."

                    scene v15s10_13e # FPP. Same as v15s10_13d, Lindsey neutral face, mouth closed.
                    with dissolve

                    u "What? Are you sure?"

                    scene v15s10_13d
                    with dissolve

                    li "Yeah. We'll take it. We'll take anything we can get at this point."

                "Accept offer":
                    scene v15s10_14
                    with dissolve

                    u "Okay, yeah. I guess that's fair."
                
            scene v15s10_12h # FPP. Same as v15s10_12g, looking at mc, slight smile, mouth open.
            with dissolve

            male_buyer "Great! It's been a pleasure doing business with you folks."

            scene v15s10_15 # TPP. Show Lindsey giving the man the keys, Lindsey neutral face, mouth closed, The man looking at Lindsey creepily, mouth closed.
            with dissolve

            pause 0.75

            play sound "sounds/cardooropen.mp3"

            scene v15s10_16 # TPP. Just show the man opening the door to the car.
            with dissolve

            pause 0.75

            play sound "sounds/doorclose.mp3"

            scene v15s10_16a # TPP. Same as v15s10_16, The man sitting in the car closing the door.
            with dissolve

            pause 0.75

            scene v15s10_17 # FPP. MC looking at Lindsey, Lindsey standing by the driver side window looking at MC who is standing by the back driver side window, Lindsey looking at MC, Lindsey slight smile, mouth closed.
            with dissolve

            pause 0.75

            scene v15s10_18 # TPP. Close up of the window rolling down at halfway, seeing the man a little bit as he sits in the drive side window just his upper face.
            with dissolve

            pause 0.75

            scene v15s10_19 # FPP. Angle that shows both Lindsey and the man. I'd say a little diagonal from the car. The window of the driver side rolled down all the way, the man looking out the window at lindsey, Lindsey not looking at him yet, The man looking at lindsey with a smile, mouth open.
            with dissolve

            male_buyer "So, what's your number, baby?"

            scene v15s10_19a # FPP. Same as v15s10_19a, Show Lindsey looking at MC, Lindsey disgusted face, mouth closed.
            with dissolve

            pause 0.75

            scene v15s10_19b # FPP. Same as v15s10_19a, Lindsey turned around looking at the man in the car, Lindsey neutral face, mouth open, the man slight smile, mouth closed.
            with dissolve

            li "The extra $50 first."

            scene v15s10_19c # FPP. Same as v15s10_19b, The man holding out the money for Lindsey, neutral face, mouth open.
            with dissolve

            male_buyer "*Sighs*"

            scene v15s10_20 # TPP. Show a close up of the man looking excitedly at his phone typing in numbers, mouth closed.
            with dissolve

            li "Okay, yeah, so... it's 8-0-0-8-5."

            scene v15s10_19d # FPP. Same as v15s10_19c, The man looking out the window at Lindsey, the man confused, mouth open, Lindsey slight smile, mouth closed.
            with dissolve

            male_buyer "80085? That ain't no phone number! Boobs? It spells boobs!"

            scene v15s10_19b
            with dissolve

            u "*Laughs*"

            scene v15s10_19e # FPP. Same as v15s10_19d, Lindsey looking at the man, slight smile, mouth open.
            with dissolve

            li "Yeah, and they're the only boobs you'll be getting from me. *Laughs* Enjoy your car!"

            scene v15s10_19f # FPP. Same as v15s10_19e, Lindsey walking away from the car towards MC, slight smile, mouth closed.
            with dissolve

            pause 0.75

            scene v15s10_21 # TPP. Frontal shot of MC and Lindsey walking away as laughing as they look at each other, The man looking at them out the car in the background, slightly upset, his mouth open.
            with dissolve

            male_buyer "Hey!"

            male_buyer "That isn't cool!"

            scene v15s10_22 # TPP. Shot of the man sitting in the car with the keys in the lock cylinder,the man frustrated, mouth closed.
            with dissolve

            pause 0.75

            scene v15s10_22a # TPP. Same as v15s10_22, The man turning the key in the lock cylinder.
            with dissolve

            pause 0.75

            scene v15s10_22
            with dissolve

            pause 0.75

            scene v15s10_22a
            with dissolve

            pause 0.75

            scene v15s10_22
            with dissolve

            pause 0.75

            scene v15s10_22a
            with dissolve

            pause 0.75

            scene v15s10_23 # TPP. Shot from behind the car smoke coming out of the exhaust because it finally started.
            with dissolve

            pause 0.75

            scene v15s10_24 # TPP. Show the man looking out the window for MC and Lindsey but they are no where in sight, the man frowning, mouth closed.
            with dissolve

            pause 0.75

            scene v15s10_25 # TPP. Lindsey and MC off on some other street stopped talking to each other.
            with fade

            pause 0.75

            scene v15s10_26 # FPP. MC looking at Lindsey, Lindsey looking at MC, Lindsey slight smile, mouth closed.
            with dissolve

            u "That was hilarious, Linds. Well played."

            scene v15s10_26a # FPP. Same as v15s10_26, Lindsey slight smile, mouth open.
            with dissolve

            li "Haha, thanks. I can't help feeling a little sad that we just sold my grandpa's car, ha."

            scene v15s10_26
            with dissolve

            u "Aw, I know. But it's for a good cause, yeah? This money is going to help you win the presidency."

            scene v15s10_26a
            with dissolve

            li "That's true. *Sighs* Okay. You know what time it is now?"

            scene v15s10_26
            with dissolve

            u "Time for a nap?"

            scene v15s10_26a
            with dissolve

            li "Haha, such a lazy boy!"

            li "It's time for us to decide on our next action plan."

            scene v15s10_26
            with dissolve

            u "More plans and then a nap!"

            scene v15s10_26a
            with dissolve

            li "*Laughs* We'll see about that nap."

            if lindsey.relationship.value >= Relationship.FWB.value:
                scene v15s10_26b # FPP. Same as 26a, Lindsey winking at MC, slight smile, mouth closed.
                with dissolve
                
                pause 1

            scene v15s10_27 # TPP. Show MC and Lindsey walking further down the side walk smiling as they walk, both mouths closed.
            with dissolve

            pause 0.75

            jump v15s12
            
        else:
            scene v15s10_12a
            with dissolve

            male_buyer "Damn, son... You weren't lying in the advert about this thing needing some TLC. *Laughs*"

            scene v15s10_12j # Same as v15s10_12b, The man looking at MC by the car, Slight smile, mouth open.
            with dissolve

            male_buyer "I appreciate your honesty on that, truly. Luckily, I've got the Benjamins to pump into it."

            scene v15s10_13c
            with dissolve

            li "I'm glad to hear that. I want it to be in good hands."

            scene v15s10_12d
            with dissolve

            male_buyer "Oh, it'll be in soft, gentle hands, baby."

            scene v15s10_13f # FPP. Same as v15s10_13e, Lindsey looking at MC with a disgusted face looking like she is gagging.
            with dissolve

            pause 0.75

            scene v15s10_12j
            with dissolve

            male_buyer "I can take it to my cousin's workshop and get it pimped out, then we'll be good to go!"

            scene v15s10_12m # FPP. Same as v15s10_12j, The man slight smile, mouth closed.
            with dissolve

            u "I'm glad you can see its potential."

            scene v15s10_12j
            with dissolve

            male_buyer "You have to be a visionary genius to see the potential in a car like this, good for you, I am one."

            scene v15s10_12h
            with dissolve

            u "(Wow, ego much?)"

            u "Ha! Lucky for us! So, let's talk about the price."

            scene v15s10_12e
            with dissolve

            male_buyer "Here's my offer based on everything I'm seeing here. Plus a tip for the girl. *Chuckles*"

            scene v15s10_13g # FPP. Same as v15s10_13f, Lindsey rolling her eyes, unamused face, mouth closed.
            with dissolve

            li "Gee, thanks."

            pause 0.75

            scene v15s10_14 # -[CarTotal] pops up on screen based on the payout sums- # Hi Again Oscar! :D
            with dissolve
            
            menu:
                "Refuse offer":
                    scene v15s10_12f
                    with dissolve

                    u "Uh, I don't know... I think we can go a little higher than that."

                    scene v15s10_12g
                    with dissolve

                    male_buyer "Bro, the car is worth what it's worth. No more, no less."

                    scene v15s10_12f
                    with dissolve

                    u "I think you can do a little bit better."

                    scene v15s10_12g
                    with dissolve

                    male_buyer "I can walk away with all the money that I came with. Maybe that would be better?"

                    scene v15s10_13d
                    with dissolve

                    li "Okay, let's just take the offer, [name]."

                    scene v15s10_13e
                    with dissolve

                    u "You sure?"

                    scene v15s10_13d
                    with dissolve

                    li "Yeah, I'd rather walk away with some rather than none."

                    scene v15s10_12j
                    with dissolve

                    male_buyer "See? Now that's how you close a deal. Someone makes an offer, and you accept it."

                    scene v15s10_12h
                    with dissolve

                    u "(What a clown.)"

                "Accept offer":
                    scene v15s10_12h
                    with dissolve

                    u "Okay, yeah. That's a good deal, great."

            scene v15s10_15 
            with dissolve

            pause 0.75

            play sound "sounds/cardooropen.mp3"

            scene v15s10_16
            with dissolve

            pause 0.75

            play sound "sounds/doorclose.mp3"

            scene v15s10_16a
            with dissolve

            pause 0.75

            scene v15s10_21a # TPP. Same angle as v15s10_21, MC and Lindesy back facing away from the camera looking at the car as the man sits in it.
            with dissolve

            pause 0.75

            scene v15s10_22 
            with dissolve

            pause 0.75

            scene v15s10_22a
            with dissolve

            pause 0.75

            scene v15s10_22
            with dissolve

            pause 0.75

            scene v15s10_22a
            with dissolve

            pause 0.75

            scene v15s10_22
            with dissolve

            pause 0.75

            scene v15s10_22a
            with dissolve

            pause 0.75

            scene v15s10_23
            with dissolve

            pause 0.75

            scene v15s10_28 # TPP. Show the car driving away.
            with dissolve

            pause 0.75

            scene v15s10_29 # FPP. MC looking at Lindsey in the spot the man and car gone, Lindsey looking at MC, Lindsey slight smile, mouth open.
            with dissolve

            li "It's bittersweet to see Grandpa's old car driving away."

            scene v15s10_29a # FPP. Same as v15s10_29, Lindsey slight smile, mouth closed.
            with dissolve

            u "Yeah, but just think about all the good you can do with that money."

            scene v15s10_29
            with dissolve

            u "It's a small sacrifice if it helps you win."

            scene v15s10_29a
            with dissolve

            li "*Sighs* Very true... Somebody's full of wisdom today. *Chuckles*"

            scene v15s10_29
            with dissolve

            u "Just go ahead and start calling me Buddha."

            scene v15s10_29a
            with dissolve

            li "Haha, you're a loser."

            li "Now that the car's sold, it's time to plan our next steps."

            scene v15s10_29
            with dissolve

            u "Okay, back to the janitor's closet?"

            scene v15s10_29a
            with dissolve

            li "Yes, back to Lindsey's super-secret presidential office. *Chuckles*"

            scene v15s10_27
            with fade
            
            pause 0.75
            
            jump v15s12
    else:
        scene v15s10_femalebuyer_1 # FPP. Show a shy hot woman looking to be in her mid 30s walking up to the area with the car, her clothes librarian like, gentle awkward smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s10_femalebuyer_1a # FPP. Same as v15s10_femalebuyer_1, The woman getting closer.
        with dissolve

        pause 0.75

        scene v15s10_femalebuyer_2 # FPP. MC looking at the Lady, Lindsey off camera, The lady looking at MC, gentle awkward smile, mouth closed.
        with dissolve

        female_buyer "..."

        scene v15s10_femalebuyer_3 # FPP. MC looking at Lindsey who is leaning against the car, Lindsey looking at the lady(the lady off-camera), Lindsey slight smile, mouth open.
        with dissolve

        li "Hello, are you here to look at the car?"

        scene v15s10_femalebuyer_2a # FPP. Same as v15s10_femalebuyer_2, The lady looking at Lindsey, gentle akward smile, mouth open.
        with dissolve

        female_buyer "Yes, that's right. You're the ones selling it?"

        scene v15s10_femalebuyer_2
        with dissolve

        u "We are. Would you like to take a closer look?"

        scene v15s10_femalebuyer_2b # FPP. Same as v15s10_femalebuyer_2a, The lady looking at MC, gentle awkward smile, mouth open.
        with dissolve

        female_buyer "I can take a little look, but I already saw from the photos that it's a very nice car."

        scene v15s10_femalebuyer_2
        with dissolve

        u "(She seems like a really nice person, this should be easy.)"

        if "v14s47_passenger_2f.webp" in v14s47_car_pics:
            $ v14s48_car_price += 50
            scene v15s10_femalebuyer_2a
            with dissolve

            female_buyer "I really loved the photos you took... Especially the one with the bird on the car. *Chuckles*"

            scene v15s10_femalebuyer_3
            with dissolve

            li "Oh, yeah! Haha, it was a cute little bird."

            scene v15s10_femalebuyer_2b
            with dissolve

            female_buyer "It was!"

            female_buyer "I remember thinking if the bird likes the car... Then it's the right car for me..."

            scene v15s10_femalebuyer_2
            with dissolve

            u "(Is she high?)"

            scene v15s10_femalebuyer_2b
            with dissolve

            female_buyer "Is the bird here?"

            scene v15s10_femalebuyer_2
            with dissolve

            u "(Don't laugh, don't laugh, don't laugh...)"

            u "No, I'm sorry. It flew away after we took the photo."

            scene v15s10_femalebuyer_2b
            with dissolve

            female_buyer "Oh, that's a shame. He was magnificent..."

        if v14s48_car_description == CarDescription.LIE:
            $ v14s48_car_price -= 200
            scene v15s10_femalebuyer_4 # FPP. MC looking at the lady as she is checking out the car, the lady gentle awkward smile, mouth closed.
            with dissolve
            
            u "As you can see, it's a modern, imported, classic sports car. All original and in excellent condition."

            u "Just run your hand across that bodywork... They don't make them like this anymore."

            scene v15s10_femalebuyer_3a # FPP. Same as v15s10_femalebuyer_3, Lindsey looking at MC, slight smile, mouth open.
            with dissolve

            li "*Chuckles*"

            scene v15s10_femalebuyer_4a # FPP. Same as v15s10_femalebuyer_4, The lady looking at MC, the lady unamused face, mouth open.
            with dissolve

            female_buyer "I know I might sound a little slow, but... I do know when I'm being lied to, young man."

            scene v15s10_femalebuyer_4b # FPP. Same as v15s10_femalebuyer_4a, the lady unamused face, mouth closed.
            with dissolve

            u "I promise I'm not lying to you, this thing is-"

            scene v15s10_femalebuyer_4a
            with dissolve

            female_buyer "Trash? I just ran my hand across the bodywork, and some of it is crumbling off."

            female_buyer "You need to start being honest with people."

            scene v15s10_femalebuyer_4b
            with dissolve

            u "I- I am being honest."

            scene v15s10_femalebuyer_4a
            with dissolve

            female_buyer "Be honest starting now or I'm walking away. I don't mind taking the bus for the rest of my life."

            scene v15s10_femalebuyer_5 # TPP. The lady starting to walk away, unamused face, mouth closed.
            with dissolve

            u "Okay, wait! I'm sorry. Let's try this again."

            scene v15s10_femalebuyer_4c # FPP. Same as v15s10_femalebuyer_4b, the lady slight smile, mouth open.
            with dissolve

            female_buyer "That's better."

            scene v15s10_femalebuyer_3b # FPP. Same as v15s10_femalebuyer_3a, Lindsey looking at the lady, Lindsey neutral face, mouth closed.
            with dissolve

            li "It's not the best car, okay?"

            scene v15s10_femalebuyer_4b
            with dissolve

            u "I'll admit, this thing is definitely a fixer-upper, but it can get you from point A to point B with no problem."

            scene v15s10_femalebuyer_4c
            with dissolve

            female_buyer "That's what I do on the bus... I go from stop A to stop B... How ironic."

            scene v15s10_femalebuyer_4b
            with dissolve

            u "Uh, yeah! Exactly. But you can do it in the comfort of your own car from now on with this purchase today."

            scene v15s10_femalebuyer_3b
            with dissolve

            li "Don't you find the bus, kind of... stinky sometimes?"

            scene v15s10_femalebuyer_4d # FPP. Same as v15s10_femalebuyer_4c, The lady looking at lindsey, the lady unamused face, mouth open.
            with dissolve

            female_buyer "I do. It can be very stinky, depending who's on it."

            scene v15s10_femalebuyer_4b
            with dissolve

            u "Well, there we go then. You can drive your own car in comfort. No stinky people."

            u "You can even hang an air freshener inside and it will smell amazing."

            scene v15s10_femalebuyer_4e # FPP. Same as v15s10_femalebuyer_4d, the lady looking at MC, the lady slight smile, mouth open.
            with dissolve

            female_buyer "I hadn't thought of that... An air freshener would be amazing. What scents do they make?"

            scene v15s10_femalebuyer_4f # FPP. Same as v15s10_femalebuyer_4e, the lady slight smile, mouth closed.
            with dissolve

            u "(Is she serious right now?)"

            scene v15s10_femalebuyer_3c # FPP. Same as v15s10_femalebuyer_3c, Lindsey looking at the lady, slight smile, mouth closed.
            with dissolve

            li "Oh, so many smells! There's lemon, cherry, blueberry, bubblegum-"

            scene v15s10_femalebuyer_4g # FPP. Same as v15s10_femalebuyer_4f, The lady looking at lindsey, slight smile, mouth open.
            with dissolve

            female_buyer "Bubblegum smell?!"

            scene v15s10_femalebuyer_4f
            with dissolve

            u "Yeah."

            scene v15s10_femalebuyer_4e
            with dissolve

            female_buyer "I love bubblegum..."

            scene v15s10_femalebuyer_3c
            with dissolve

            li "*Giggles*"

            scene v15s10_femalebuyer_4f
            with dissolve

            u "Okay, that's great. Good. So, let's move onto the price."

            scene v15s10_femalebuyer_4e
            with dissolve

            female_buyer "I can't overlook the things you've lied about, but I do love the idea of the bubblegum smell when I'm driving. So, this is what I can offer..."

            scene v15s10_femalebuyer_4h # FPP. Same as v15s10_femalebuyer_4g, The lady holding up cash, looking at MC, slight smile, mouth closed.
            with dissolve # -[CarTotal] pops up on screen based on the pay out sums(if lied, total they can receive is minus200$ off the car's worth price)- # Third times a charm. Hi Oscar :D

            menu:
                "Refuse offer":
                    scene v15s10_femalebuyer_4i # FPP. Same as v15s10_femalebuyer_4h, the lady with cash in her hand still, looking at MC, neutral face, mouth closed.
                    with dissolve

                    u "We can't accept that, I'm sorry. Can you go any higher?"

                    scene v15s10_femalebuyer_4j # FPP. Same as v15s10_femalebuyer_4i, the lady with cash in her hand, neutral face, mouth open.
                    with dissolve

                    female_buyer "I've told you. I'm happy to take the bus forever, even if it is stinky. So, you can take my offer or I'm leaving."

                    scene v15s10_femalebuyer_4i
                    with dissolve

                    u "(Wow, so much for negotiating...)"

                    scene v15s10_femalebuyer_3b
                    with dissolve

                    li "Let's just take it. It's a fair price, I guess."

                "Accept offer":
                    scene v15s10_femalebuyer_4k # FPP. Same as v15s10_femalebuyer_4j, the lady with cash in her hand, slight smile, mouth closed.
                    with dissolve

                    u "Okay, sure. You've got yourself a deal."

            scene v15s10_femalebuyer_6 # TPP. Close up of the lady handing Lindsey the cash, faces not seen.
            with dissolve

            pause 0.75

            scene v15s10_femalebuyer_6a # TPP. Same as v15s10_femalebuyer_6, Lindsey putting the cash in her pocket.
            with dissolve

            female_buyer "Don't spend it all at once."

            scene v15s10_femalebuyer_6b # TPP. Same as v15s10_femalebuyer_6a, Lindsey dropping the car keys in the ladies hand.
            with dissolve

            pause 0.75

            scene v15s10_femalebuyer_7 # TPP. Show MC and Lindsey, walking away from the area looking at each other smiling.
            with dissolve

            pause 0.75

            scene v15s10_femalebuyer_7a # TPP. Same as v15s10_femalebuyer_7, Show MC and Lindsey with their backs faced to the camera angle, looking back at the car.
            with dissolve

            pause 0.75

            scene v15s10_femalebuyer_8 # TPP. Show the Lady in the car with the key in the lock cylinder
            with dissolve

            pause 0.75

            scene v15s10_femalebuyer_8a # TPP. Same as v15s10_femalebuyer_8, the lady turning the key in the lock cylinder
            with dissolve

            pause 0.75

            scene v15s10_femalebuyer_8
            with dissolve

            pause 0.75

            scene v15s10_femalebuyer_8a
            with dissolve

            pause 0.75

            scene v15s10_femalebuyer_8
            with dissolve

            pause 0.75

            scene v15s10_femalebuyer_9 # TPP. Shot of the back of the car, smoke coming out of the exhaust as it starts.
            with dissolve

            pause 0.75

            scene v15s10_femalebuyer_10 # TPP. Show the car driving away from the area.
            with dissolve

            pause 0.75

            scene v15s10_femalebuyer_11 # FPP. MC looking at Lindsey, Lindsey looking at MC, slight smile, mouth open.
            with dissolve

            li "I'm kind of sad to see it go... Poor Grandpa's car."

            scene v15s10_femalebuyer_11a # FPP. Same as v15s10_femalebuyer_11, Lindsey slight smile, mouth closed.
            with dissolve

            u "Yeah, but I think she'll look after it. And now you have more money."

            scene v15s10_femalebuyer_11
            with dissolve

            li "For the greater good."

            scene v15s10_femalebuyer_11a
            with dissolve

            u "The greater good. *Chuckles*"

            scene v15s10_femalebuyer_11
            with dissolve

            li "Let's get back to the planning board now and prepare for phase two."

            scene v15s10_femalebuyer_11a
            with dissolve

            u "Sounds good."

            scene v15s10_femalebuyer_12 # TPP. Show MC and Lindsey walking back to campus,both slight smile, mouth closed.
            with dissolve

            pause 0.75

            jump v15s12

        else:
            scene v15s10_femalebuyer_4e
            with dissolve

            female_buyer "The advert was right. This is a nice, old car, in need of some tough love and major attention."

            scene v15s10_femalebuyer_4f
            with dissolve

            u "It certainly is. I'm glad you can appreciate our honesty, ha."

            scene v15s10_femalebuyer_4e
            with dissolve

            female_buyer "I like it. I think I'll call him Fred."

            scene v15s10_femalebuyer_4f
            with dissolve

            u "You're already naming him? So you're ready to buy?"

            scene v15s10_femalebuyer_4e
            with dissolve

            female_buyer "I am. It's an honest price for an honest seller. Here's my total offer:"

            scene v15s10_femalebuyer_4h
            with dissolve

            pause 0.75

    # -[CarTotal] pops up on screen based on the payout sums-
    # Oscar ;)
        menu:
            "Refuse offer":
                scene v15s10_femalebuyer_4i
                with dissolve

                u "I'm sorry, but... We need a little more than that."

                scene v15s10_femalebuyer_4j
                with dissolve

                female_buyer "This is a take it or leave it type of offer, young man."

                scene v15s10_femalebuyer_4i
                with dissolve

                u "(Damn, she's not as slow as I thought she'd be.)"

                scene v15s10_femalebuyer_3
                with dissolve

                li "Okay, we have a deal."

                scene v15s10_femalebuyer_3d # FPP. Same as v15s10_female_buyer_3, Lindsey looking at MC, slight smile, mouth closed.
                with dissolve

                u "Really?"

                scene v15s10_femalebuyer_3a
                with dissolve

                li "Yeah, it's going to a good owner, and we need whatever we can get."

            "Accept offer":
                scene v15s10_femalebuyer_4k
                with dissolve
    
                u "Okay, we accept."

        scene v15s10_femalebuyer_6 # TPP. Close up of the lady handing Lindsey the cash, faces not seen.
        with dissolve

        pause 0.75

        scene v15s10_femalebuyer_6a # TPP. Same as v15s10_femalebuyer_6, Lindsey putting the cash in her pocket.
        with dissolve

        female_buyer "Thank you, dear!"

        scene v15s10_femalebuyer_7
        with dissolve

        female_buyer "Let's go home, Fred."

        scene v15s10_femalebuyer_7a
        with dissolve

        pause 0.75

        scene v15s10_femalebuyer_8
        with dissolve

        pause 0.75

        scene v15s10_femalebuyer_8a
        with dissolve

        pause 0.75

        scene v15s10_femalebuyer_8
        with dissolve

        pause 0.75

        scene v15s10_femalebuyer_8a
        with dissolve

        pause 0.75

        scene v15s10_femalebuyer_8
        with dissolve

        pause 0.75

        scene v15s10_femalebuyer_9 
        with dissolve

        pause 0.75

        scene v15s10_femalebuyer_10 
        with dissolve

        pause 0.75

        scene v15s10_femalebuyer_11 
        with dissolve

        li "It's a bittersweet moment, seeing Grandpa's car go."

        scene v15s10_femalebuyer_11a
        with dissolve

        u "Yeah, but now you have some sweet campaign money."

        scene v15s10_femalebuyer_11
        with dissolve

        li "Haha, true."

        scene v15s10_femalebuyer_11a
        with dissolve

        u "And I'm sure Fred is happy with his new owner."

        scene v15s10_femalebuyer_11
        with dissolve

        li "Fred! *Laughs* That's so funny, I can't wait to tell Grandpa about that..."

        scene v15s10_femalebuyer_11a
        with dissolve

        u "*Laughs*"

        scene v15s10_femalebuyer_11
        with dissolve

        li "Let's head back to campus now and plan the next phase."

        scene v15s10_femalebuyer_11a
        with dissolve

        u "Alrighty."

        scene v15s10_femalebuyer_12
        with dissolve

        pause 0.75

        jump v15s12
