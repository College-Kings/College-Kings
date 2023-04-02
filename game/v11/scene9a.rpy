# SCENE 9: Wolves Chris Prank
# Location: Wolves house/College Campus/ Car/ Airport
# Characters: MC(outfit 1) /Imre(Outfit 2)/Perry(Outfit 1)/Sebastian(Outfit 1)
# Time: Night and Day

label v11_wolves_seb_prank:
    scene v11wsp1 # TPP. Show MC walking in through the Wolves house door, he has a neutral expression, mouth closed
    with fade

    pause 0.75
    play music "music/v11/Track Scene 9a_1.mp3" fadein 2
    scene v11wsp2 # FPP. MC is walking in to the living room, he can not see anyone yet, just a bit of the inside of the living room
    with dissolve

    imre "*Laughs* He's a pretty deep sleeper so I'm sure we'll get away with it."

    scene v11wsp3 # FPP. MC is now inside the living room, MC can now see most of the living room (he's coming around the door, he can see Imre and Perry sitting, Imre and Perry looking at each other, smiling, Perry mouth open, Imre mouth closed)
    with dissolve

    guyd "*Laughs* I don't wanna know what happens if we don't."

    scene v11wsp4 # FPP. MC and Imre looking at each other, Imre smiling, mouth closed (Imre and Perry still seating)
    with dissolve

    u "What are you guys doing?"

    scene v11wsp4a # FPP. Same as v11wsp4, Imre mouth open, smiling
    with dissolve

    imre "Coming up with the best prank ever."

    scene v11wsp5 # FPP. MC looking at Perry, Perry is looking at Imre (Imre out of shot), Perry slightly worried, mouth open (Imre sitting next to Perry, like in v11wsp3 and v11wsp4)
    with dissolve

    guyd "Best prank if we don't get caught..."

    scene v11wsp4
    with dissolve

    u "Who are we pranking?"

    scene v11wsp4a
    with dissolve

    imre "Sebastian."

    scene v11wsp4
    with dissolve

    u "Oh, nice! What's the plan so far?"

    scene v11wsp6 # TPP. Show MC sitting down between Imre and Perry (Imre and Perry on the same side as v11wsp3)
    with dissolve

    pause 0.75

    scene v11wsp7 # FPP. MC and Perry looking at each other, Perry slightly smiling, mouth open
    with dissolve

    guyd "Staying up all night is step one."

    scene v11wsp7a # FPP. Same as v11wsp7, Perry slightly smiling, mouth closed
    with dissolve

    u "Wait, what?"

    scene v11wsp7
    with dissolve

    guyd "Well, we have to wait until he falls asleep."

    scene v11wsp8 # FPP. MC and Imre looking at each other, Imre smiling, mouth open
    with dissolve

    imre "Once he's asleep we're gonna drag him across campus in his sleeping bag. We'll leave him right in the middle of the college."

    scene v11wsp8a # FPP. Same as v11wsp7, Imre smiling, mouth closed
    with dissolve

    u "How are you gonna put him in a sleeping bag and get him across campus without waking him up?"

    scene v11wsp8
    with dissolve

    imre "See, that's why this prank is so perfect. Sebastian likes falling asleep to this weird fucking country-folk yee-haw shit music, but it doesn't bother him while he sleeps because he's such a deep sleeper."
    
    imre "Plus, he already sleeps in a sleeping bag because he's too lazy to make his bed. *Chuckles*"

    scene v11wsp8a
    with dissolve

    u "So this is a revenge plan over him being a deep sleeper?"

    scene v11wsp8
    with dissolve

    imre "It's a revenge plan over the fact that I can't sleep because he's playing that damn music!"

    scene v11wsp8a
    with dissolve

    u "Ah, I get it now."

    scene v11wsp8
    with dissolve

    imre "So, you in?"

    scene v11wsp8a
    with dissolve

    menu:
        "Not for me":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            scene v11wsp8a
            with dissolve

            u "Nah guys, that's not for me. I'm going to get some extra sleep so I'm ready for the trip."

            scene v11wsp8
            with dissolve

            imre "Aww, c'mon man."

            scene v11wsp8a
            with dissolve

            u "Sorry dude."

            scene v11wsp9 # TPP. Show MC going up the stairs (he has a neutral expression, he is in the middle of the stairs at this point)
            with dissolve

            pause 0.75

            scene v11wsp10 # TPP. MC is going through his room's door, he has a slight smile, mouth closed
            with dissolve

            u "(Those guys are gonna be in for it.)"

            scene v11wsp10a # TPP. Same cam as v11ws10, but MC is touching the light switch
            with dissolve

            pause 0.75

            scene v11wsp11 # TPP. Show MC sleeping in his bed (he is in his underwear), it's now dark in his room
            with dissolve

            pause 0.75

            scene black
            with fade
            
            pause 0.75

            scene v11wsp11a # TPP. Show MC waking up, he is sitting on his bed, yawning, it's now day
            with fade

            pause 0.75

            scene v11wsp10b # TPP. Same cam as v11wsp10, MC is now leaving his room, fully dressed
            with dissolve

            pause 0.75

            scene v11wsp9a # TPP. Same cam as v11wsp9, MC is going down the stairs now
            with dissolve

            pause 0.75

            scene v11wsp3a # FPP. Same as v11wsp3, but it's daytime now and Perry mouth closed
            with dissolve

            pause 0.75

            scene v11wsp4b # FPP. Same as v11wsp4, but daytime
            with dissolve

            u "So how'd your little stunt go?"

            scene v11wsp4c # FPP. Same as v11wsp4b, Imre mouth open, smiling
            with dissolve

            imre "It was amazing! The picture is going viral on Kiwii."

            scene v11wsp4b
            with dissolve

            u "What picture?"

            scene v11wsp4c
            with dissolve

            imre "Check it out."

            scene v11wsp4b
            with dissolve

            $ v11s9a_kiwiiPost1 = KiwiiPost(caleb, "phone/kiwii/Posts/v11/sebnaked.webp", _("Someone had a fun time last night!"), number_likes=556) # Sebastian naked in the middle of campus stood over his sleeping bag looking confused
            $ v11s9a_kiwiiPost1.newComment(aubrey, _("Suns out, Buns out!"), number_likes=renpy.random.randint(100, 300))
            $ v11s9a_kiwiiPost1.newComment(samantha, _("A little early in the morning to go streaking isn't it? lol"), number_likes=renpy.random.randint(100, 300))
            $ v11s9a_kiwiiPost1.newComment(lindsey, _("Spicy!"), number_likes=renpy.random.randint(100, 300))
            $ v11s9a_kiwiiPost1.addReply(_("Getting ready to go skinny dipping?"), number_likes=321)
            $ v11s9a_kiwiiPost1.addReply(_("Someone's got \"balls\""), number_likes=334)

            label v11s9a_kiwiiPost1_continue:
                if v11s9a_kiwiiPost1.replies:
                    call screen phone
                if v11s9a_kiwiiPost1.replies:
                    u "(I should reply on Kiwii)"
                    jump v11s9a_kiwiiPost1_continue

            scene v11wsp4b
            with dissolve

            u "You took his clothes off?!"

            scene v11wsp4c
            with dissolve

            imre "*Laughs* No, he must sleep naked."

            scene v11wsp5a # FPP. Same as v11wsp5, but Perry is looking at MC now, Perry slightly worried, mouth open
            with dissolve

            guyd "I honestly kinda feel bad."

        "Sure":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            scene v11wsp4
            with dissolve

            u "Sure, I'll join you."

            scene v11wsp4a
            with dissolve

            imre "Nice... wake me up when it's time?"

            scene v11wsp4
            with dissolve

            u "Nope. This was your idea. You wake me up when it's time!"

            scene v11wsp12 # TPP. MC sat in between Imre and Perry in living room, but MC is the only one in shot, show him sleeping while sitting on the couch, mouth closed, neutral expression
            with dissolve

            pause 0.75

            scene v11wsp13 # FPP. MC is still sitting on the couch, Imre is standing in front of him, Imre mouth open, neutral expression
            with dissolve

            imre "*Whisper* It's time man!"

            stop music fadeout 3
            play music "music/v11/Track Scene 9_3.mp3" fadein 2

            scene v11wsp13a # FPP. Same as v11wsp13, Imre mouth closed
            with dissolve

            u "*Sleepy* Just two more minutes."

            scene v11wsp13
            with dissolve

            imre "*Whisper* Bro c'mon!"

            scene v11wsp13a
            with dissolve

            u "Ugh okay."

            scene v11wsp14 # FPP. MC is behind Imre, Imre is walking inside Sebastian's room, MC is at the door, Imre is sneaking
            with dissolve

            pause 0.75

            scene v11wsp15 # FPP. MC, Perry and Imre are holding Sebastian in his sleeping bag, those who have face in shot have slightly scared expressions, mouths closed
            with dissolve

            pause 0.75

            scene v11wsp16 # TPP. Show MC, Perry and Imre putting Sebastian in the back of wagon (Sebastian is still in his sleeping bag)
            with dissolve

            pause 0.75

            scene v11wsp17 # FPP. MC is looking at Imre, Imre mouth open, neutral expression (Imre is standing next to the wagon)
            with dissolve

            imre "*Whisper* Alright, let's go."

            scene v11wsp18 # TPP. Show MC and Perry walking next to each other and Imre pulling the wagon (Imre next to MC and Perry as well, they're walking through the college campus), everyone neutral expression, closed mouth
            with dissolve

            pause 0.75

            scene v11wsp19 # FPP. Same character positioning as v11wsp18, make sure they've moved a bit further ahead, MC and Perry looking at each other, Perry mouth open, neutral expression
            with dissolve

            guyd "*Whisper* How is he still sleeping?"

            scene v11wsp20 # FPP. Same character positioning as v11wsp19, make sure they've moved in even more, MC looking at Imre, Imre mouth open, neutral expression
            with dissolve

            imre "Told you he was a deep sleeper. See? We don't even have to whisper."

            scene v11wsp20a # FPP. Same as v11wsp20, Imre mouth closed, neutral expression
            with dissolve

            u "Are we planning on staying out here all night?"

            scene v11wsp20
            with dissolve

            imre "Hell no, dude! This is my one chance to get a good night's sleep."

            scene v11wsp19a # FPP. Same as v11wsp19, Perry looking forward, mouth open, he is trying to warn Imre
            with dissolve

            guyd "Hey watch out for that hole!"

            scene v11wsp20b # FPP. Same as v11wsp20, Imre looking forward, mouth open, slightly confused
            with dissolve

            imre "I don't see a-"

            scene v11wsp21 # TPP. Show the wagon hitting a hole (the wagon can be slightly tilted, as if it were falling)
            with dissolve

            u "*Whisper* Oh shit!"

            scene v11wsp22 # FPP. MC, Perry and Imre standing behind the wagon, MC looking at Sebastian who is in his bodybag inside the wagon
            with dissolve

            se "Mmmm..."

            scene v11wsp23 # FPP. Same positioning as v11wsp22, MC and Perry looking at each other, Perry mouth open, worried expression
            with dissolve

            guyd "*Whisper* Is he waking up?"

            scene v11wsp24 # FPP. Same as v11wsp24a, Imre mouth closed, neutral expression
            with dissolve

            u "..."

            scene v11wsp40 # FPP. Same positioning as v11wsp22, Imre is looking in the wagon (wagon interior out of shot, focus only on Imre), Imre worried, mouth closed
            with dissolve

            imre "..."

            scene v11wsp23a # FPP. Same as v11wsp23, Perry is looking in the wagon now (wagon interior out of shot, focus only on Perry), Perry worried, mouth closed
            with dissolve

            guyd "..."

            scene v11wsp24a # FPP. Same as v11wsp24, Imre is now looking at MC, Imre mouth open, neutral expression 
            with dissolve

            imre "I think we're good."

            scene v11wsp24
            with dissolve

            u "Fuck, that was too close."

            scene v11wsp23b # FPP. Same as v11wsp23, Perry is pointing at the middle of the college, mouth open, neutral expression
            with dissolve

            guyd "That's where you wanted to put him right?"

            scene v11wsp24b # FPP. Same as v11wsp24a, Imre is looking towards where Perry is pointing in v11wsp22b, Imre mouth open, neutral expression
            with dissolve

            imre "That's it."

            scene v11wsp24
            with dissolve

            u "We're just gonna lay him on the ground?"

            scene v11wsp24a
            with dissolve

            imre "Yep."

            scene v11wsp24
            with dissolve

            u "We're gonna be fucked when he wakes up."

            scene v11wsp25 # TPP. Show MC and Imre getting Sebastian out of the wagon
            with dissolve

            pause 0.75

            scene v11wsp26 # TPP. Show MC and Imre lowering Sebastian on the ground where Perry was pointing at in v11wsp23b
            with dissolve

            pause 0.75

            scene v11wsp27 # FPP. MC, Imre and Perry standing around the body, MC and Imre looking at each other, Perry out of shot, Imre mouth closed, slight smile
            with dissolve

            u "Now what? We just leave him?"

            scene v11wsp27a # FPP. Same as v11wsp27, Imre mouth open, slight smile
            with dissolve

            imre "Yep! This is pretty major for Perry's first prank."

            scene v11wsp28 # FPP. Same character positioning as v11wsp27, MC and Perry looking at each other, Perry mouth closed, slight smile
            with dissolve

            u "This is your first prank?"

            scene v11wsp28a # FPP. Same as v11wsp28, Perry smiling, mouth open
            with dissolve

            guyd "Sure is."

            scene v11wsp29 # TPP. Show MC, Perry and Imre walking back to the Wolves house, they are all smiling, mouths closed
            with dissolve

            pause 0.75

            scene v11wsp30 # FPP. MC is behind Imre as Imre opens the door inside the Wolves house.
            with fade

            pause 0.75

            scene v11wsp31 # FPP. Imre is standing in the living room with MC, they are looking at each other, Imre mouth open, slight smile
            with dissolve

            imre "And now it's time for some peace and quiet."

            scene v11wsp9 # TPP. Show MC going up the stairs (he has a neutral expression, he is in the middle of the stairs at this point)
            with dissolve

            pause 0.75

            scene v11wsp10 # TPP. MC is going through his room's door, he has a slight smile, mouth closed
            with dissolve

            u "(This is either gonna be hilarious or a complete shit show.)"

            scene v11wsp10a # TPP. Same cam as v11ws10, but MC is touching the light switch
            with dissolve

            pause 0.75

            scene v11wsp11
            with dissolve

            pause 0.75

            scene v11wsp11a
            with fade

            pause 0.75

            scene v11wsp10b # TPP. Same cam as v11wsp10, MC is now leaving his room, fully dressed
            with dissolve

            pause 0.75
            stop music fadeout 3
            play music "music/v11/Track Scene 9a_2.mp3" fadein 2
            scene v11wsp9a # TPP. Same cam as v11wsp9, MC is going down the stairs now
            with dissolve

            pause 0.75

            scene v11wsp4b
            with dissolve

            u "So how'd our prank go?"

            scene v11wsp4c
            with dissolve

            imre "It was amazing, the picture on Kiwii is going viral."

            scene v11wsp4b
            with dissolve

            u "What picture?"

            scene v11wsp4c
            with dissolve

            imre "Check Kiwii."

            $ v11s9a_kiwiiPost2 = KiwiiPost(caleb, "phone/kiwii/Posts/v11/sebnaked.webp", _("Someone had a fun time last night!"), number_likes=556) # Sebastian naked in the middle of campus stood over his sleeping bag looking confused
            $ v11s9a_kiwiiPost2.newComment(aubrey, _("Suns out, Buns out!"), number_likes=renpy.random.randint(100, 300))
            $ v11s9a_kiwiiPost2.newComment(samantha, _("A little early in the morning to go streaking isn't it? lol"), number_likes=renpy.random.randint(100, 300))
            $ v11s9a_kiwiiPost2.newComment(lindsey, _("Spicy!"), number_likes=renpy.random.randint(100, 300))
            $ v11s9a_kiwiiPost2.addReply(_("I wonder how this happened..."), number_likes=321)
            $ v11s9a_kiwiiPost2.addReply(_("Someone's got \"balls\""), number_likes=218)

            label v11s9a_kiwiiPost2_continue:
                if v11s9a_kiwiiPost2.replies:
                    call screen phone
                if v11s9a_kiwiiPost2.replies:
                    u "(I should reply on Kiwii)"
                    jump v11s9a_kiwiiPost2_continue

            scene v11wsp4b
            with dissolve

            u "I'm confused... Why is he naked?"

            scene v11wsp4c
            with dissolve

            imre "*Laughs* He must sleep naked."

            scene v11wsp5a
            with dissolve

            guyd "I honestly kinda feel bad."

    scene v11wsp4b
    with dissolve

    u "Where is he now?"

    scene v11wsp32 # TPP. Show Sebastian running in to the Wolves living room with the sleep bag around his waist, scared, mouth closed
    with dissolve

    pause 0.75

    scene v11wsp33 # FPP. MC, Perry and Imre are standing next to each other looking at Sebastian, MC looking at Sebastian, Sebastian is very angry, mouth closed
    with dissolve

    pause 0.75

    scene v11wsp33a # FPP. Same as v11wsp33, Sebastian laughing, mouth open
    with dissolve

    se "*Laughs*"

    scene v11wsp34 # FPP. Same character positioning as v11wsp33, MC is now looking at Imre, Imre looking at Sebastian, Imre laughing, mouth open
    with dissolve

    imre "*Laughs*"

    scene v11wsp33a
    with dissolve

    u "*Laughs*"

    scene v11wsp35 # FPP. Same character positioning as v11wsp33, MC is now looking at Perry, Perry looking at Sebastian, slightly worried, mouth open
    with dissolve

    guyd "You're not mad?"

    scene v11wsp33b # FPP. Same as v11wsp33a, but Sebastian looking at Perry
    with dissolve

    se "Mad? Why would I be mad? If anything, I'm fired up. You better watch your backs, boys. *Chuckles*"

    scene v11wsp35
    with dissolve

    guyd "What about the picture though?"

    scene v11wsp33b
    with dissolve

    se "What picture?"

    scene v11wsp34
    with dissolve

    imre "*Laughs* Check Kiwii."

    scene v11wsp36 # TPP. Show Sebastian running up the stairs, sleeping bag around his waist, smiling, mouth closed
    with dissolve

    pause 0.75

    scene v11wsp33c # FPP. Same as v11wsp32a, Sebastian wearing shorts, mouth open, slightly smiling, looking at his phone
    with dissolve

    se "Bro, who took this?"

    scene v11wsp33d # FPP. Same as v11wsp32c, but Sebastian mouth closed, looking at MC
    with dissolve

    u "*Laughs* Wasn't us! We did the drop off, not the set up."

    scene v11wsp33c
    with dissolve

    se "Says @CalebTheApeBoy posted it. That's the new Ape pledge. Oh, it's on now."

    scene v11wsp33d
    with dissolve

    u "Planning some frat versus frat revenge?"

    scene v11wsp33e # FPP. Same as v11wsp32d, but Sebastian mouth open
    with dissolve

    se "I am now."

    scene v11wsp33d
    with dissolve

    u "Too bad we can't help... Imre and I are going to Europe."

    scene v11wsp33e
    with dissolve

    se "Oh don't worry, I got this. Perry will help me too. I'll have it all set up by the time you get back."

    scene v11wsp34a # FPP. Same as v11wsp34, Imre now looking at MC, mouth open, slight smile
    with dissolve

    imre "Speaking of Europe... We should get going."

    scene v11wsp34b # FPP. Same as v11wsp34a, Imre mouth closed
    with dissolve

    u "*Laughs* Alright."

    scene v11wsp41 # TPP. Show MC grabbing his luggage in his room, MC slight smile, mouth closed
    with dissolve

    pause 0.75
    
    scene v11wsp37 # TPP. Show Imre and MC leaving the Wolves house with their luggage, both smiling, mouth closed
    with dissolve

    pause 0.75

    scene v11wsp38 # TPP. Show a car on the road
    with dissolve

    pause 0.75

    scene v11wsp39 # FPP. Show Imre walking ahead of MC into the airport, show Ms Rose, Nora and Mr Lee in the backrgound
    with fade

    pause 0.75
    stop music fadeout 3
    jump v11_airport_arrival