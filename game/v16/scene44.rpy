# SCENE 44: Walk shelter dog with Lauren in park
# Locations: In the Park 
# Characters: MC (Outfit: 9), LAUREN (Outfit: 1), Jogger (Outfit: 1)
# Time: Evening

label v16s44:
    scene v16s44_1 # TPP. In the park, Lauren (slight smile, mouth is closed) is waiting with a huge dog on a leash. MC (slight smile, mouth is closed) approaches Lauren
    with dissolve

    pause 0.75

    scene v16s44_2 # FPP. Show just Lauren (### Editor Note ### -Trademark cute Lauren smile, mouth is closed, looking at MC)
    with dissolve

    u "Hey, Lauren."

    scene v16s44_2a # FPP. Show just Lauren (### Editor Note ### -Trademark cute Lauren smile, mouth is open, looking at MC)
    with dissolve

    la "Hey, [name]!"

    if lauren.relationship >= Relationship.GIRLFRIEND: # -if LaurenGF/RS, they have a nice kiss
        scene v16s44_3 # TPP. Show Lauren and MC kissing, Lauren still holding onto Rubius (the dog) with one hand, Rubio watche's MC and Lauren Kiss tilting his head tounge is out
        with dissolve

        pause 0.75

        scene v16s44_2
        with dissolve

        u "Well, you kept your promise. That was a nice kiss."

        scene v16s44_2a
        with dissolve

        la "Haha, yeah, I would give you a little bit more if I didn't have my hands full with this dog."

        scene v16s44_2
        with dissolve

        u "Haha, it's okay."

        if v16s10_let_lauren_continue_hj: # -if Lauren also gave MC a hand job in econ class
            scene v16s44_2
            with dissolve

            u "So, wanna talk about what happened in econ?"

            scene v16s44_2a
            with dissolve

            la "Haha, yeah. That was hot, wasn't it?"

            scene v16s44_2
            with dissolve

            u "It was. And super risky. *Laughs*"

            scene v16s44_2a
            with dissolve

            la "I love that we got away with doing something so naughty in a public place."

            scene v16s44_2
            with dissolve

            u "I never would've guessed you had an exhibition fetish! Should I be worried you'll try something like that again?"

            scene v16s44_2a
            with dissolve

            la "Oh, I guarantee it will happen again. *Giggles*"

# -Regardless of LaurenGF/RS and classroom hand job-

    scene v16s44_4 # FPP. Show just Rubius (the Dog) (mouth is open, happy demeanor, looking up at MC)
    with dissolve

    u "So, who's this fella? He's huge!"

    scene v16s44_2a
    with dissolve

    la "This is Rubius."

    scene v16s44_4
    with dissolve

    menu:
        "Greet Rubius":
            scene v16s44_4
            with dissolve

            u "Hey, Rubius. You're a handsome fella. Yes, you are."

            scene v16s44_4a # FPP. MC pats Rubius on the head. Rubius likes it. His tongue hanging out for a moment as he takes some head strokes
            with dissolve

            pause 0.75

            scene v16s44_2b # FPP. Show just Lauren (full smile, mouth is open, looking at MC)
            with dissolve

            la "He likes you!"

            scene v16s44_2
            with dissolve

            u "I have a way with animals. Must be my loving personality, haha."

        "Don't greet Rubius":
            scene v16s44_4
            with dissolve

            u "(Hmm, I could pat him on the head, but I don't wanna lose a finger today.)"

# -Regardless of greeting Rubius or not-

    scene v16s44_2a
    with dissolve

    la "He's actually being a good boy right now. A few minutes before you got here, he tried chasing a squirrel and I couldn't control him. He nearly dragged me across the park!"

    scene v16s44_2
    with dissolve

    u "That couldn't have been fun."

    scene v16s44_2a
    with dissolve

    la "It wasn't!"

    scene v16s44_2
    with dissolve

    u "Let's see how it goes and if he misbehaves again, I'll walk him instead."

    scene v16s44_2a
    with dissolve

    la "Deal!"

    scene v16s44_5 # TPP. MC, Lauren and Rubius walk through the park, all of them slight smiles, mouths are closed, Lauren is holding Rubius on the leash
    with dissolve

    pause 0.75

    scene v16s44_5a # TPP. Quick shots of Rubius smelling things, Mc and Lauren look at Rubius as he smells something (object up to the renderer), Lauren is holding Rubius on the leash
    with dissolve

    pause 0.75

    scene v16s44_5b # TPP. Rubius is peeing up a tree, it's a huge stream of piss, MC and Lauren (laughing, mouths are open, looking at Rubius), Lauren is holding Rubius on the leash
    with dissolve

    pause 0.75

    scene v16s44_5c # TPP. MC, Lauren (both slight smiles, mouths are closed, looking to cross the street), and Rubius arrive at the edge of the park a street is in front of them where they stop
    with dissolve

    pause 0.75

    scene v16s44_6 # FPP. Show just Lauren (slight smile, mouth is open, looking down at Rubius) Different park background from v16s44_2 renders, Rubius is not shown in the Render
    with dissolve

    la "Come on, Rubius. This way."

    scene v16s44_6a # FPP. Show just Lauren (slight smile, mouth is closed, looking at MC) Different park background from v16s44_2 renders
    with dissolve

    u "Is he being stubborn?"

    scene v16s44_6b # FPP. Show just Lauren (slight smile, mouth is open, looking at MC) Different park background from v16s44_2 renders
    with dissolve

    la "Yep! I guess when you're this huge, you get your own way all the time."

    scene v16s44_6
    with dissolve

    la "Rubius, we're staying in the park buddy!"

    scene v16s44_7 # FPP. Show just Rubius (the Dog) (mouth is open, happy demeanor, looking across the street, turned away from MC) Show a street in the background behind him
    with dissolve

    menu:
        "Stay in the park":
            $ v16s44_rubius_park_walk = True

            scene v16s44_7
            with dissolve

            u "Rubius, come on! Here boy!"

            scene v16s44_7a # FPP. Show just Rubius (the Dog) (mouth is open, tongue is hanging out, happy demeanor, looking up at MC) Show a street in the background behind him
            with dissolve

            pause 0.75

            scene v16s44_6b
            with dissolve

            la "Wow, look at you, dog whisperer, haha!"

            scene v16s44_7a
            with dissolve

            u "Good boy, Rubius!"

            scene v16s44_5d # TPP. same as v16s44_5c Just show them walking away from the street, everything else is the same
            with dissolve

            pause 0.75

            scene v16s44_8 # TPP. Show a male jogger (slight smile, mouth is closed, looking at Rubius) in shorts, tshirt, sneakers, coming towards Lauren (slight smile, mouth is closed, looking at the jogger), MC (slight smile, mouth is closed, looking at the jogger), and Rubius (mouth is open, tongue is hanging out, happy demeanor, looking up at the jogger)
            with dissolve

            pause 0.75

            scene v16s44_9 # FPP. Show the Jogger (slight smile, mouth is open, looking at Lauren), Lauren (slight smile, mouth is closed, looking at the jogger), and Rubius (mouth is open, tongue is hanging out, happy demeanor, looking up at the jogger)
            with dissolve

            jog "What a beautiful dog, mind if I pet him?"

            scene v16s44_9a # FPP. Show the Jogger (slight smile, mouth is closed, looking at Lauren), Lauren (slight smile, mouth is open, looking at the jogger), and Rubius (mouth is closed, happy demeanor, looking up at the jogger)
            with dissolve

            la "Of course! He's super friendly."

            scene v16s44_9b # FPP. Show the Jogger (slight smile, mouth is open, looking at Rubius) kneeling down to eye level with Rubius and holding a hand out to Rubius, Lauren (slight smile, mouth is closed, looking at the jogger), and Rubius (mouth is open, tongue is hanging out, happy demeanor, looking at the jogger)
            with dissolve

            jog "Hello, sir."

            scene v16s44_9c # FPP. Show the Jogger (full smile, mouth is open, looking at Rubius) kneeling down to eye level with Rubius and is now holding Rubius's paw, Lauren (slight happy shocked expression, mouth is open, looking at Rubius), and Rubius (mouth is open, tongue is hanging out, happy demeanor, looking at the jogger) putting his paw into the hand of the jogger
            with dissolve

            pause 0.75

            scene v16s44_9d # FPP. Show the Jogger (full smile, mouth is open, looking at Lauren) kneeling down to eye level with Rubius and is still holding Rubius's paw, Lauren (full smile, mouth is open, looking at Rubius), and Rubius (mouth is open, tongue is hanging out, happy demeanor, looking at the jogger) Rubius still has his paw in the jogger's hand
            with dissolve

            la "He shook your hand! I didn't know you could do that, buddy!"

            scene v16s44_9e # FPP. Show the Jogger (slight smile, mouth is open, looking at Rubius) kneeling down to eye level with Rubius and is still holding Rubius's paw, Lauren (slight smile, mouth is closed, looking at Rubius), and Rubius (mouth is open, tongue is hanging out, happy demeanor, looking at the jogger) Rubius still has his paw in the jogger's hand
            with dissolve

            jog "He's been trained well. Clever dog!"

            scene v16s44_9f # FPP. Show the Jogger (slight smile, mouth is open, looking at Rubius) kneeling down to eye level with Rubius and is still holding Rubius's paw and uses his other hand to pat Rubius on his head, Lauren (slight smile, mouth is closed, looking at Rubius), and Rubius (mouth is open, tongue is hanging out, happy demeanor, looking at the jogger) Rubius still has his paw in the jogger's hand
            with dissolve

            pause 0.75

            scene v16s44_9g # FPP. Show the Jogger (slight smile, mouth is closed, looking at Lauren) kneeling down to eye level with Rubius and is still holding Rubius's paw, Lauren (slight smile, mouth is open, looking at the jogger), and Rubius (mouth is open, tongue is hanging out, happy demeanor, looking at the jogger) Rubius still has his paw in the jogger's hand
            with dissolve

            la "Yeah, Rubius is one of the smartest dogs at the shelter."

            scene v16s44_9h # FPP. Show the Jogger (slight smile, mouth is open, looking at Lauren) kneeling down to eye level with Rubius and is still holding Rubius's paw, Lauren (slight smile, mouth is closed, looking at the jogger), and Rubius (mouth is open, tongue is hanging out, happy demeanor, looking at the jogger) Rubius still has his paw in the jogger's hand
            with dissolve

            jog "Rubius? Now, that's a stately name!"

            scene v16s44_9f
            with dissolve

            pause 0.75

            scene v16s44_10 # FPP. Close up shot of Rubius (happy deameanor, mouth is closed, he looks proud to be called a king)
            with dissolve

            jog "King Rubius!"

            scene v16s44_9h
            with dissolve

            jog "You said he's from the shelter?"

            scene v16s44_9g
            with dissolve

            la "Yeah, he needs a new home."

            scene v16s44_9h
            with dissolve

            jog "Hmm, you know, I think he would make the perfect jogging partner."

            jog "And I've been so lonely since my wife left me for a fellow runner."

            scene v16s44_9i # FPP. Show the Jogger (slight sad expression, mouth is closed, looking at Lauren) kneeling down to eye level with Rubius and is still holding Rubius's paw, Lauren (slight sad expression, mouth is open, looking at the jogger), and Rubius (mouth is open, tongue is hanging out, happy demeanor, looking at the jogger) Rubius still has his paw in the jogger's hand
            with dissolve

            la "Oh, I'm sorry to hear that."

            scene v16s44_9j # FPP. Show the Jogger (slight sad expression, mouth is open, looking at Lauren) kneeling down to eye level with Rubius and is still holding Rubius's paw, Lauren (slight sad expression, mouth is closed, looking at the jogger), and Rubius (mouth is open, tongue is hanging out, happy demeanor, looking at the jogger) Rubius still has his paw in the jogger's hand
            with dissolve

            jog "Yeah, ditched me for a guy who beat me in the local marathon. Talk about pouring salt on your wounds."

            scene v16s44_9f
            with dissolve

            u "(Damn, looks like he needs someone to trauma-dump to.)"

            scene v16s44_9j
            with dissolve

            jog "You know what? I'll come by the shelter and see about adopting him."

            scene v16s44_9i
            with dissolve

            la "What? Wait- Really?!"

            scene v16s44_9j
            with dissolve

            jog "Yeah, I can already tell we're going to be best friends!"

            scene v16s44_9i
            with dissolve

            la "Amazing! Thank you so much!"

            scene v16s44_9f
            with dissolve

            jog "See you tomorrow, big guy! I'm going to prepare for your arrival home. Thank you, guys!"

            scene v16s44_8a # TPP. Show a male jogger (slight smile, mouth is closed, looking at MC) waving goodbye to MC as he runs away from MC, Lauren and Rubius, Lauren (slight smile, mouth is closed, looking at the jogger) waving goodbye to the jogger and holding onto Rubius with the other hand, MC (slight smile, mouth is open, looking at the jogger) waving goodbye to the jogger, and Rubius (mouth is open, tongue is hanging out, happy demeanor, looking up at the jogger)
            with dissolve

            u "Thanks! See ya."

            scene v16s44_11 # FPP. Show just Lauren (full smile, mouth is open, looking at MC)
            with dissolve

            la "Autumn's going to freak out! I can't believe that just happened so easily..."

            scene v16s44_11a # FPP. Show just Lauren (full smile, mouth is closed, looking at MC)
            with dissolve

            u "Haha, yeah. At this rate she'll be asking you to walk all the dogs to the park from now on."

            scene v16s44_11
            with dissolve

            la "I hope not. I wouldn't have any time left to study, ha."

            scene v16s44_11a
            with dissolve

            u "I don't see any issues there..."

            scene v16s44_11
            with dissolve

            la "*Laughs* You're a horrible influence."

            la "Here, you take him for the last part of the walk."

            scene v16s44_11a
            with dissolve

            u "Oh, okay. Is your arm hurting?"

            scene v16s44_11
            with dissolve

            la "A little bit, yeah. *Chuckles*"

            scene v16s44_8b # TPP. The jogger is no longer in the render, Lauren (slight smile, mouth is closed, looking at MC) haning Rubios leash to MC, MC (slight smile, mouth is closed, looking at Lauren), and Rubius (mouth is open, tongue is hanging out, happy demeanor, looking up at MC)
            with dissolve

            pause 0.75

        "Follow Rubius":
            scene v16s44_6a
            with dissolve

            u "Let's see where he wants to take us."

            scene v16s44_6b
            with dissolve

            la "What? I don't want to be out all night! This big fella could lead us across the country, [name]."

            scene v16s44_6a
            with dissolve

            u "Haha, no, we'll just follow him for a little bit. Let him choose our path."

            scene v16s44_6b
            with dissolve

            la "Hmm, okay, fine. But we aren't going far, Rubius!"

            scene v16s44_5e # TPP. MC, Lauren (both slight smiles, mouths are closed, looking to cross the street), and Rubius (mouth is open, tongue is hanging out, happy demeanor, looking to cross the street) cross the street in render v16s44_5c
            with fade

            pause 0.75

            scene v16s44_12 # TPP. Show Mc (no expression, mouth is closed, looking down the alleyway,) Lauren (no expression, mouth is closed, looking down the alleyway,) and Rubius (mouth is open, tongue is hanging out, happy demeanor, looking down the alleyway) walking into an alleyway with a trash can, and random scattered trash and puddles of water on each side
            with dissolve

            pause 0.75

            scene v16s44_13 # FPP. Show just Lauren (no expression, mouth is open, looking at MC), alleyway background
            with dissolve

            la "Eurgh! He must've smelled something in here."

            scene v16s44_14 # FPP. Show trash on the ground, and what appears to be an old taco, and next to the taco is a promo leaflet for the Blue Lounge, alleyway background
            with dissolve

            u "Yeah, I think it was that old taco."

            # -if mc gagged at ryan in the bathroom at laurens birthday party
            if v15s18a_gag: # PlaceHOLDER 

                scene v16s44_14a # FPP. Close up shot of the taco and the promo leaflet for the Blue Lounge, alleyway background
                with dissolve

                u "(*Gags*) Oh... God..."

            # -end if

            scene v16s44_14b # FPP. Show Rubius licking the old Taco, alleyway background
            with dissolve

            la "Oh, shi- No, Rubius! So gross!"

            scene v16s44_15 # TPP. Show Lauren (slightly disgusted expression, mouth is closed, looking at Rubius) straining to pull Rubius away from the old taco from v16s44_14 renders, Rubius has his nose deep in the taco, mouth is closed, alleyway background
            with dissolve

            u "Come on, man..."

            scene v16s44_13
            with dissolve

            la "Tacos are not good for you, big guy! *Sighs*"

            scene v16s44_13a # FPP. Show just Lauren (no expression, mouth is closed, looking at MC), alleyway background
            with dissolve

            u "Hey, at least we can add tacos to his list of favorite foods."

            scene v16s44_13b # FPP. Show just Lauren (slight smile, mouth is open, looking at MC), alleyway background
            with dissolve

            la "Haha, you're right..."

            la "Okay, let's head back to the park, I guess."

            scene v16s44_12a # TPP. Show Mc (no expression, mouth is closed, looking down the alleyway,) Lauren (no expression, mouth is closed, looking down the alleyway,) and Rubius (mouth is open, tongue is hanging out, happy demeanor, looking down the alleyway) all of them are in the alleyway with a trash can, and random scattered trash and puddles of water on each side
            with dissolve

            pause 0.75

            scene v16s44_16 # FPP. Close up shot of a cat jumping out of a trash can
            with vpunch

            pause 0.75

            scene v16s44_12b # TPP. Show Mc (schocked expression, mouth is closed, looking at lauren,) Lauren (scared/shocked expression, mouth is open,) Lauren has fallen into a puddle of water, and Rubius (mouth is open, tongue is hanging out, happy demeanor, is chasing the cat), a cat is running away from Rubius all of them are in the alleyway with a trash can, and random scattered trash and puddles of water on each side
            with dissolve

            pause 0.75

            scene v16s44_12c # TPP. Show Mc (concerned expression, mouth is open, looking at lauren,) Mc is helping Lauren out of the water puddle, Lauren (disgusted expression, mouth is closed, looking up at Mc) Lauren is being helped up by MC out of the puddle, and Rubius (mouth is open, tongue is hanging out, happy demeanor, has stopped chasing the cat and is now running back to Lauren), the cat is no longer in the render all of them are in the alleyway with a trash can, and random scattered trash and puddles of water on each side
            with dissolve

            u "Oh, fuck! Lauren! Are you okay?"

            scene v16s44_17 # FPP. Close up shot of Laurens chest, her shirt is completely soaked and you can see the full shape of her boobs and clearly visibly see her nipples through the wet shirt, alleyway background
            with dissolve

            pause 0.75

            scene v16s44_18 # FPP. Show just Lauren (Disgusted expression, mouth is open, looking down at Rubius (Rubius is not shown,)) Laurens shirt is completely soaked and you can see the full shape of her boobs and clearly visibly see her nipples through the wet shirt, alleyway background
            with dissolve

            la "*Gasps* Eww! Rubius...!"

            scene v16s44_19 # FPP. Show just Rubius (Concerned deameanor, tilting his head, mouth is closed, looking up at MC and Lauren)
            with dissolve

            pause 0.75

            scene v16s44_18a # FPP. Show just Lauren (Disgusted expression, mouth is open, looking at MC) Laurens shirt is completely soaked and you can see the full shape of her boobs and clearly visibly see her nipples through the wet shirt, alleyway background
            with dissolve

            la "Look at my shirt... Ugh!"

            scene v16s44_17
            with dissolve

            pause 0.75

            scene v16s44_18b # FPP. Show just Lauren (concerned expression, mouth is closed, looking at MC) Laurens shirt is completely soaked and you can see the full shape of her boobs and clearly visibly see her nipples through the wet shirt, alleyway background
            with dissolve

            u "Oh, I am."

            if lauren.relationship >= Relationship.GIRLFRIEND: # -if laurengf

                scene v16s44_18c # FPP. Show just Lauren (Lauren smirks, slight smile, mouth is open, looking at MC) Laurens shirt is completely soaked and you can see the full shape of her boobs and clearly visibly see her nipples through the wet shirt, alleyway background
                with dissolve

                la "Ha, no, stop it! This is gross, and that's not polite to do..." 

                scene v16s44_18
                with dissolve

                la "Rubius! Look what you did to me."

                scene v16s44_19a # FPP. Show just Rubius (Proud deameanor, Big Proud smile, mouth is open, looking up at MC and Lauren)
                with dissolve

                pause 0.75

            else:

                scene v16s44_18a
                with dissolve

                la "Seriously, [name]?"

                scene v16s44_18b
                with dissolve

                u "Sorry, I-"
                
                scene v16s44_19b # FPP. Show just Rubius (Disapointed expression, if possible a raised eyebrow, mouth is closed, looking at MC)
                with dissolve

                u "Rubius... Bad!"

                scene v16s44_18
                with dissolve

                la "That was not very nice, Rubius! Look what you've done to my clothes."

                scene v16s44_19a
                with dissolve

                pause 0.75

            # -end if

            scene v16s44_18d # FPP. Show just Lauren (slightly sad expression, mouth is open, looking down at her chest,) puffing her chest out attempting to dry her shirt off, both hands are cupping her breasts exposing them even more if possible, Laurens shirt is still completely soaked and you can see the full shape of her boobs and clearly visibly see her nipples through the wet shirt, alleyway background
            with dissolve

            la "*Sighs* The one day I choose to go braless in public..."

            scene v16s44_18e # FPP. Show just Lauren (slightly sad expression, mouth is open, looking at MC,) Laurens shirt is still completely soaked and you can see the full shape of her boobs and clearly visibly see her nipples through the wet shirt, alleyway background
            with dissolve

            la "Can you take him now, please?"

            scene v16s44_18f # FPP. Show just Lauren (slightly sad expression, mouth is closed, looking at MC,) Laurens shirt is still completely soaked and you can see the full shape of her boobs and clearly visibly see her nipples through the wet shirt, alleyway background
            with dissolve

            u "Yeah, of course."

            scene v16s44_12d # TPP. Show Mc (no expression, mouth is closed, looking at Lauren,) Lauren (no expression, mouth is open, looking at MC,) and Rubius (mouth is open, tongue is hanging out, happy demeanor, looking at MC) all of them are in the alleyway with a trash can, and random scattered trash and puddles of water on each side
            with dissolve

            la "From now on, all walks stay WITHIN the park."

    scene v16s44_5d
    with dissolve

    pause 0.75

    scene v16s44_5f # TPP. same as v16s44_5b MC and Lauren are just walking the opposite direction and Rubius is where he peed in v16s44_5b
    with dissolve

    pause 0.75

    scene v16s44_5g # TPP. same as v16s44_5a MC and Lauren are just walking the opposite direction and Rubius is sniffing the same object from v16s44_5a
    with dissolve

    pause 0.75

    scene v16s44_2a
    with dissolve

    la "Well, here we are."

    la "Thanks a lot for coming."

    scene v16s44_2
    with dissolve

    u "Anytime. It was quite eventful in the end."

    if v16s44_rubius_park_walk: # -if you stayed in the park
        scene v16s44_2a
        with dissolve

        la "Right? I seriously can't believe he's getting adopted, ha!"

        la "And all we had to do was take a walk, one of his favorite things."

        scene v16s44_2
        with dissolve

        u "I think he's going to a good home, too."

        scene v16s44_2a
        with dissolve

        la "He'll love being that man's jogging buddy, I know it."

        scene v16s44_2
        with dissolve

        u "And a personal therapist, haha."

        scene v16s44_2a
        with dissolve

        la "Ha, maybe! Therapy dogs are pretty common, even if it's just for emotional support."

        scene v16s44_2
        with dissolve

        u "Yeah, I'm sure he'll be happy."

        scene v16s44_2a
        with dissolve

        la "Me too."

    else: # -if you followed Rubius
        scene v16s44_2c # FPP. Show just Lauren (no expression, mouth is open, looking at MC)
        with dissolve

        la "Eventful is one word for it. I'd call it disgusting."
 
        scene v16s44_2d # FPP. Show just Lauren (no expression, mouth is closed, looking at MC)
        with dissolve

        u "Haha, yeah... Guess we could have done without the visit to the alleyway."

        scene v16s44_2c
        with dissolve

        la "Yeah? And whose idea was that?"

        scene v16s44_2d
        with dissolve

        u "Hey, we were following the dog, remember?"

        scene v16s44_2e # FPP. Show just Lauren (no expression, mouth is open, looking at her chest) Lauren rubs her hands over her chest unintentionally puffing her breasts out, her shirt is dry and her nipples and breast CAN'T be seen through the shirt
        with dissolve

        la "Mhmm... At least my shirts dried off... kind of."

        scene v16s44_2
        with dissolve

        u "Ha, I'm glad."

# -Regardless of that-

    if 1 & v16s27_mc_baby_duty_night == 1: ### -if on baby duty alone Wednesday
        scene v16s44_2
        with dissolve

        u "And now, I need to go pick up a baby."

    elif 0x10 & v16s27_mc_baby_duty_night == 0x10: ### -if sharing baby duty Wednesday

        scene v16s44_2
        with dissolve

        u "And now, I need to go to the Chicks house for baby duty..."

    else: ### -if partner is on baby duty

        scene v16s44_2
        with dissolve

        u "And now, I should really get home and try to sleep as much as possible."

        scene v16s44_2a
        with dissolve

        la "Why's that?"

        scene v16s44_2
        with dissolve

        u "Because the next two nights, I'll be getting woken up hourly by a screaming infant."

    # -Regardless of which baby night-

    scene v16s44_2a
    with dissolve

    la "Oh, you're doing the baby project thing?"

    scene v16s44_2
    with dissolve

    u "Yep. I'm gonna be a dad. Must be punishment for my sins, haha."

    scene v16s44_2a
    with dissolve

    la "*Giggles* I'm sure you'll do fine. Good luck with it, though!"

    scene v16s44_2
    with dissolve

    u "Thanks. See you soon?"

    scene v16s44_2a
    with dissolve

    la "Of course."

    scene v16s44_2
    with dissolve

    pause 0.75

    if lauren.relationship >= Relationship.GIRLFRIEND: # -if LaurenGF, they have a quick goodbye kiss
        scene v16s44_3
        with dissolve

        pause 0.75

    else: # -if not LaurenGf, they do a side hug as lauren is holding the leash in one hand

        scene v16s44_3a # TPP. Show Lauren and MC giving each other a side hug Lauren still holding onto Rubius (the dog) with one hand, Rubio watch's MC and Lauren Kiss tilting his head tounge is out
        with dissolve

        pause 0.75

    scene v16s44_1a # TPP. same as v16s44_1 Mc is walking the other direction, and Lauren is waving goodbye
    with dissolve
    
    pause 0.75

    if 1 & v16s27_mc_baby_duty_night == 1: ### -if on baby duty alone Wednesday, transition to Scene45-

        jump v16s45

    elif 0x10 & v16s27_mc_baby_duty_night == 0x10: ### -if sharing baby duty Wednesday, transition to Scene47-
        
        jump v16s47
    else: ### -if partner is on baby duty Wednesday, transition to Scene42-
        
        jump v16s42