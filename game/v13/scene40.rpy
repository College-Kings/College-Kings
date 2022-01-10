# SCENE 40: Chloe Sex Free Roam
# Locations: Hotel Room
# Characters: CHLOE (Outfit: 1/Naked), MC (Outfit: 5/Naked)
# Time: Night

label v13s40:
    scene v13s40_1 # TPP. Show MC standing in the lobby, Chloe walking towards him, both slight smiles, mouths closed
    with Fade(1,1,1)

    pause 0.75

    play music "music/v13/Track Scene 40_1.mp3" fadein 2

    scene v13s40_2 # FPP. MC and Chloe looking at each other, in lobby, Chloe slight smile, mouth open
    with dissolve

    cl "Hey, handsome."

    scene v13s40_2a # FPP. Same as v13s40_2, Chloe slight smile, mouth closed
    with dissolve

    u "Haha, hey."

    scene v13s40_2
    with dissolve

    u "(Oh shoot, I almost forgot. I picked up a few surprises for Chloe.)"

    scene v13s40_2a
    with dissolve

    u "What are you up to?"

    scene v13s40_2
    with dissolve

    cl "Bored and looking for something to do... *Chuckles*"

    scene v13s40_2a
    with dissolve

    u "What if I told you I had something special for you? Special based on some of those fantasies you told me about."

    scene v13s40_2
    with dissolve

    cl "Oh, really?"

    scene v13s40_2a
    with dissolve

    u "Yes, really."

    scene v13s40_2
    with dissolve

    cl "Then I'd say what are we doing down here? *Chuckles*"

    scene v13s40_3 # TPP. Show MC whispering in Chloe's ear, Chloe slight smile, mouth closed, MC slight smile, mouth open
    with dissolve

    u "*Whispers* Lead the way."

    $ sceneList.add("v13_chloe")

    scene v13s40_4 # TPP. Show Chloe grabbing MC's hand and walking through the hotel lobby, both slight smiles, mouths closed
    with dissolve

    pause 1

    scene v13s40_5 # TPP. Show Chloe still holding MC's hand, walking through the hotel corridor, both slight smiles, mouths closed
    with dissolve

    pause 1

    scene v13s40_6 # TPP. Show Chloe pulling MC by the arm into her room, both slight smiles, mouths closed
    with dissolve

    pause 1

    scene v13s40_7 # TPP. Show MC and Chloe in her room, Chloe wrapping her arms around MC
    with dissolve

    pause 1

    stop music fadeout 3
    play music "music/v13/Track Scene 40_2.mp3" fadein 2

    label v13s40_sg:
        if _in_replay:
            $ mc.money += 1000
            $ mc.inventory.add_item(honey)
            $ mc.inventory.add_item(butt_plug)
            $ mc.inventory.add_item(spankers)
            $ mc.inventory.add_item(feather)

    scene v13s40_8 # FPP. Chloe wrapping her arms around MC, looking at him, Chloe sexy look, mouth open
    with dissolve

    cl "What now, Sir?"

    scene v13s40_8a # FPP. Same as v13s40_8, Chloe mouth closed
    with dissolve

    u "Lay back on the bed and close your eyes."

    scene v13s40_9 # TPP. Show Chloe getting into her bed, slight smile, mouth closed
    with dissolve

    pause 1

    scene v13s40_10 # FPP. MC looking at Chloe laying on her bed, mouth open, slight smile
    with fade

    cl "I'm a little nervous, but plenty excited... *Chuckles*"

    scene v13s40_10a # FPP. Same as v13s40_10, Chloe mouth closed
    with dissolve

    u "Haha, just try to relax."

    if config_censored:
        call screen censoredPopup("v13s40_nsfwSkipLabel1")

    scene v13s40_11 # TPP. Show MC removing Chloe's top, both slight smiles, mouths closed, Chloe's eyes closed
    with dissolve

    pause

    scene v13s40_11a # TPP. Same as v13s40_11, MC blindfolding Chloe, Chloe's pants removed
    with fade

    pause

    scene v13s40_11b # TPP. Same as v13s40_11a, MC tying Chloe's arms to the bed
    with dissolve

    pause

    scene v13s40_12 # FPP. Chloe same as v13s40_11b, MC standing next to bed, looking at Chloe, Chloe slight smile, mouth open
    with dissolve

    cl "[name], you remembered my confession."

    scene v13s40_12a # FPP. Same as v13s40_12, Chloe mouth closed
    with dissolve

    u "*Chuckles* Shhh."

    $ sex_overlay_options = [
        [],
        [("Neck", "v13s40_neck"), ("Chest", "v13s40_chest"), ("Back", "v13s40_back"), ("Shoulders", "v13s40_shoulder")]
    ]

    if mc.has_item(honey):
        $ sex_overlay_options[0].append((honey.name, "v13s40_honey"))
    if mc.has_item(spankers):
        $ sex_overlay_options[0].append((spankers.name, "v13s40_spanker"))
    if mc.has_item(feather):
        $ sex_overlay_options[0].append((feather.name, "v13s40_feather"))

    call screen sex_overlay("v13s40_end_free_roam")

label v13s40_honey:
    $ chloeturnedon.add("honey")

    scene v13s40ho_1 # TPP. Show MC pouring the honey on Chloe's breasts, Chloe slight smile, mouth closed
    #with dissolve

    pause

    scene v13s40ho_2 # TPP. Show MC licking the honey off of Chloe's boobs, Chloe slight smile, mouth open
    with dissolve

    cl "Ahh, that... *Chuckles* That feels good..."

    scene v13s40ho_3 # FPP. MC standing next to the bed, looking down at Chloe, Chloe slight smile, breasts with honey, mouth closed
    with dissolve

    u "Call me Pinnie Wooh."

    scene v13s40ho_3a # FPP. Same as v13s40ho_3, Chloe mouth open
    with dissolve

    cl "*Chuckles*"

    play sound "sounds/kiss.mp3"
    scene v13s40ho_4 # TPP. Show MC kissing Chloe's boobs with honey, mouths closed, slight smiles
    with dissolve

    pause

    scene v13s40ho_5 # TPP. Show MC sucking on Chloe's boobs with honey, she is smiling, mouth closed
    with dissolve

    pause

    scene v13s40ho_3b # FPP. Same as v13s40ho_3a, Chloe sexy look, mouth open, no more honey on her boobs
    with dissolve

    cl "Mmm... Kiss me."

    scene v13s40ho_6 # TPP. Show MC kissing Chloe
    with dissolve

    pause

    scene v13s40ho_3c # FPP. Same as v13s40ho_3b, Chloe mouth closed
    with dissolve

    u "I've got plenty more where that came from."

    call screen sex_overlay("v13s40_end_free_roam")

label v13s40_feather:
    $ chloeturnedon.add("feather")
    scene v13s40fe_1 # TPP. Show MC taking the feather and placing it on her chest, Chloe smiling, mouth closed
    #with dissolve

    pause

    scene v13s40fe_1a # TPP. Same as v13s40fe_1, feather slightly lower, Chloe mouth open
    with dissolve

    cl "*Moans* [name]!"

    scene v13s40fe_1b # TPP. Same as v13s40fe_1a, feather on her stomach
    with dissolve

    cl "*Laughs* That tickles."

    scene v13s40fe_1c # TPP. Same as v13s40fe_1b, Chloe mouth closed
    with dissolve

    u "Want me to stop?"

    scene v13s40fe_1b
    with dissolve

    cl "No... Please, keep going. *Chuckles*"

    scene v13s40fe_1d # TPP. Same as v13s40fe_1c, MC tickling Chloe's pussy with the feather, Chloe moaning
    with dissolve

    cl "*Moans*"

    scene v13s40fe_2 # TPP. Close up of MC tickling her legs with the feather (show her pussy too)
    with dissolve

    pause

    scene v13s40fe_3 # TPP. Close up of MC ticklig her feet with the feather
    with dissolve

    cl "Ooh, ha! Okay... Way too ticklish... *Chuckles*"

    scene v13s40fe_3a # TPP. Same as v13s40fe_3, MC no longer tickling her feet
    with dissolve

    u "We can try something else..."

    call screen sex_overlay("v13s40_end_free_roam")

label v13s40_spanker:
    $ chloeturnedon.add("spanker")
    scene v13s40sp_1 # TPP. Show MC untying Chloe, both smiling, mouths closed
    #with dissolve

    pause
    
    scene v13s40sp_2 # TPP. Show MC turning Chloe around, both smiling, mouths closed
    with dissolve

    pause

    scene v13s40sp_3 # TPP. Show MC tying Chloe again, both smiling, mouths closed
    with dissolve

    pause

    scene v13s40sp_4 # TPP. Show MC brushing the spanker on Chloe's back, don't show MC or Chloe's face
    with dissolve

    cl "Oooh, is that what I think it is? *Chuckles*"

    scene v13s40sp_4a # TPP. Same as v13s40sp_4, spanker slightly lower
    with dissolve

    u "Yes ma'am..."

    scene v13s40sp_5 # TPP. Same as v13s40sp_4, but on Chloe's ass
    with dissolve

    cl "Mmmm, please don't be too rough..."

    scene v13s40sp_5a # TPP. Same as v13s40sp_5, spanker slightly above Chloe's ass, he is about to spank her
    with dissolve

    pause

    scene v13s40sp_5b # TPP. MC spanking Chloe's ass
    with vpunch

    cl "Ahh!"

    scene v13s40sp_5
    with dissolve

    u "Too hard?"

    scene v13s40sp_5a
    with dissolve

    cl "N-No, not at all. *Chuckles* Keep going."

    scene v13s40sp_5b
    with vpunch

    cl "Ahh! Yes! Harder..."

    scene v13s40sp_5c # TPP. Same as v13s40sp_5a, spanker even higher above her ass
    with dissolve

    pause

    scene v13s40sp_5b
    with vpunch

    cl "Oh! My... My god!"

    scene v13s40sp_5
    with dissolve

    u "(She's really into this...) *Chuckles*"

    scene v13s40sp_3a # TPP. Same as v13s40sp_3, MC untying Chloe
    with dissolve
    
    pause 1

    scene v13s40sp_2a # TPP. Same as v13s40sp_2, MC flipping Chloe the other way (stomach upwards)
    with dissolve

    pause 1

    scene v13s40sp_1a # TPP. Same as v13s40sp_1, MC tying Chloe back to the bed
    with dissolve

    pause

    call screen sex_overlay("v13s40_end_free_roam")

label v13s40_neck:
    scene v13s40neck_1 # TPP. Close up of Chloe's neck
    #with dissolve

    menu:
        "Choke":
            $ chloeturnedon.add("neck")

            scene v13s40neck_2 # TPP. Close up of MC's hand choking Chloe's neck, Chloe smiling, mouth closed
            with dissolve

            pause

        "Kiss":
            scene v13s40neck_3 # TPP. Show MC kissing Chloe's neck, Chloe slight smile, mouth closed
            with dissolve

            pause
        
    call screen sex_overlay("v13s40_end_free_roam")

label v13s40_chest:
    scene v13s40chest_1 # TPP. Close up of Chloe's boobs
    #with dissolve

    menu:
        "Kiss":
            scene v13s40chest_2 # TPP. Show MC kissing Chloe's boobs, Chloe slight smile, mouth closed
            with dissolve

            pause

            scene v13s40chest_2a # TPP. Same as v13s40chest_2, MC licking Chloe's nipple
            with dissolve

            pause

            scene v13s40chest_2b # TPP. Same as v13s40chest_2, MC sucking on Chloe's other boob
            with dissolve

            pause

        "Massage":
            $ chloeturnedon.add("chest")

            scene v13s40chest_3 # TPP. Show MC massaging Chloe's boobs, Chloe smiling, mouth closed
            with dissolve

            pause

            scene v13s40chest_3a # TPP. Same as v13s40chest_3, MC different massage pose (still boobs)
            with dissolve

            pause

            scene v13s40chest_3b # TPp. Same as v13s40chest_3a, MC different massage pose (still boobs)
            with dissolve

            pause
    
    call screen sex_overlay("v13s40_end_free_roam")

label v13s40_back:
    scene v13s40back_1 # TPP. Close up of Chloe's back
    #with dissolve

    menu:
        "Massage":
            $ chloeturnedon.add("back")

            scene v13s40back_2 # TPP. MC massaging Chloe's back, Chloe smiling, mouth closed
            with dissolve

            pause 

            scene v13s40back_2a # TPP. Same as v13s40back_2, different massage pose (still back)
            with dissolve

            pause

            scene v13s40back_2b # TPP. Same as v13s40back_2a, different massage pose (still back)
            with dissolve

            pause

        "Kiss":
            scene v13s40back_3 # TPP. Show MC kissing Chloe's upper back, Chloe slight smile, mouth closed
            with dissolve

            pause

            scene v13s40back_3a # TPP. Same as v13s40back_3, MC kissing her middle back
            with dissolve

            pause

            scene v13s40back_3b # TPP. Same as v13s40back_3, MC kissing her lower back
            with dissolve

            pause
    
    call screen sex_overlay("v13s40_end_free_roam")

label v13s40_shoulder:
    scene v13s40shoulder_1 # TPP. Close up of Chloe's shoulder
    #with dissolve

    menu:
        "Massage":
            $ chloeturnedon.add("shoulder")

            scene v13s40shoulder_2 # TPP. Show MC massaging Chloe's shoulder, Chloe smiling, mouth closed
            with dissolve

            pause

            scene v13s40shoulder_2a # TPP. Same ass v13s40shoulder_2, different massage pose (still shoulder)
            with dissolve

            pause

        "Kiss":
            $ chloeturnedon.add("shoulder")
            scene v13s40shoulder_3 # TPP. Show MC kissing Chloe left shoulder, Chloe slight smile, mouth closed
            with dissolve

            pause

            scene v13s40shoulder_4 # TPP. Show MC kissing Chloe right shoulder, Chloe slight smile, mouth closed
            with dissolve

            pause
    
    call screen sex_overlay("v13s40_end_free_roam")
        
label v13s40_end_free_roam:
    if len(chloeturnedon) >= 2:
    
        scene v13s40end_1 # FPP. MC standing next to Chloe, Chloe looking up at MC, Chloe smiling, mouth open
        #with dissolve

        cl "Hurry and untie me..."

        scene v13s40end_2 # TPP. Show MC untying Chloe, both smiling, mouths closed
        with dissolve

        pause 1

        scene v13s40end_3 # TPP. Show Chloe removing her blindfold, sitting on the bed, MC same position as v13s40end_2, both smiling, mouths closed
        with dissolve

        pause 1

        scene v13s40end_4 # TPP. Show Chloe pushing MC on the bed, Chloe mouth open, smiling, MC smiling, mouth closed
        with dissolve

        cl "I want you."

        scene v13s40end_5 # FPP. MC laying down on the bed, looking at Chloe as she mounts on top of him, mouth open, sexy expression
        with dissolve

        cl "Right now!"

        scene v13s40end_5a # FPP. Same as v13s40end_5, Chloe removing MC's pants, Chloe smiling, mouth closed, MC mouth closed, smiling
        with dissolve

        u "(She's being wild right now!)"

        scene v13s40end_6 # TPP. Show Chloe removing MC's shirt, both smiling, mouths closed
        with dissolve

        pause

        scene v13s40end_7 # TPP. Show Chloe getting ready to squat on MC's dick, both sexy expressions, mouths closed
        with dissolve

        pause

        image v13chlsd = Movie(play="images/v13/Scene 40/v13chlsd.webm", loop=True, image="images/v13/Scene 40/v13chlsdStart.webp", start_image="images/v13/Scene 40/v13chlsdStart.webp") # Chloe squatting
        image v13chlsdf = Movie(play="images/v13/Scene 40/v13chlsdf.webm", loop=True, image="images/v13/Scene 40/v13chlsdStart.webp", start_image="images/v13/Scene 40/v13chlsdStart.webp") # Chloe squatting spedup
        image v13chlsd2 = Movie(play="images/v13/Scene 40/v13chlsd2.webm", loop=True, image="images/v13/Scene 40/v13chlsd2Start.webp", start_image="images/v13/Scene 40/v13chlsd2Start.webp") # Chloe squatting FPP
        image v13chlsd2f = Movie(play="images/v13/Scene 40/v13chlsd2f.webm", loop=True, image="images/v13/Scene 40/v13chlsd2Start.webp", start_image="images/v13/Scene 40/v13chlsd2Start.webp") # Chloe squatting FPP spedup

        scene v13chlsd # Ignore as anim
        with dissolve
        pause

        cl "*Moans* F-fuck baby... No one's ever been able to bring this side out of me!"

        scene v13chlsdf # Ignore as anim
        with dissolve
        pause

        u "You're getting ready to bring a new side out of me too..."

        scene v13chlsd2 # Ignore as anim
        with dissolve
        pause

        cl "Show me then... Mmm, show me that side!"

        scene v13chlsd2f # Ignore as anim
        with dissolve
        pause

        cl "*Moans*"

        scene v13s40end_8 # TPP. MC getting up, turning Chloe around (she will have her back to MC)
        with dissolve

        pause

        scene v13s40end_9 # TPP. Show MC pushing Chloe's hed into the bed, ready to fuck her from behind
        with dissolve

        pause

        image v13chlf0 = Movie(play="images/v13/Scene 40/v13chlf0.webm", loop=True, image="images/v13/Scene 40/v13chlfStart.webp", start_image="images/v13/Scene 40/v13chlfStart.webp") # Chloe flatiron
        image v13chlf0f = Movie(play="images/v13/Scene 40/v13chlf0f.webm", loop=True, image="images/v13/Scene 40/v13chlfStart.webp", start_image="images/v13/Scene 40/v13chlfStart.webp") # Chloe flatiron spedup
        image v13chlf02 = Movie(play="images/v13/Scene 40/v13chlf02.webm", loop=True, image="images/v13/Scene 40/v13chlf2Start.webp", start_image="images/v13/Scene 40/v13chlf2Start.webp") # Chloe flatiron FPP
        image v13chlf02f = Movie(play="images/v13/Scene 40/v13chlf02f.webm", loop=True, image="images/v13/Scene 40/v13chlf2Start.webp", start_image="images/v13/Scene 40/v13chlf2Start.webp") # Chloe flatiron FPP spedup

        scene v13chlf0 # Ignore as anim
        with dissolve
        pause

        cl "I... *Moans* Like it... Rough... *Whispers* F-Fuck... Like this... [name]!"

        scene v13chlf0f # Ignore as anim
        with dissolve
        pause

        u "How much do you like it?"

        scene v13chlf02 # Ignore as anim
        with dissolve
        pause

        cl "*Moans* I like it... a lot..."

        scene v13chlf02f # Ignore as anim
        with dissolve
        pause

        cl "FUCK! I LOVE THIS, [name]!"

        scene v13s40end_10 # TPP. MC turning Chloe around
        with dissolve

        pause

        scene v13s40end_11 # TPP. MC getting ready to fuck Chloe's face, she's laying down on bed
        with dissolve

        pause

        image v13chlff = Movie(play="images/v13/Scene 40/v13chlff.webm", loop=True, image="images/v13/Scene 40/v13chlffStart.webp", start_image="images/v13/Scene 40/v13chlffStart.webp") # Chloe face fuck
        image v13chlfff = Movie(play="images/v13/Scene 40/v13chlfff.webm", loop=True, image="images/v13/Scene 40/v13chlffStart.webp", start_image="images/v13/Scene 40/v13chlffStart.webp") # Chloe face fuck spedup
        image v13chlff2 = Movie(play="images/v13/Scene 40/v13chlff2.webm", loop=True, image="images/v13/Scene 40/v13chlff2Start.webp", start_image="images/v13/Scene 40/v13chlff2Start.webp") # Chloe face fuck FPP
        image v13chlff2f = Movie(play="images/v13/Scene 40/v13chlff2f.webm", loop=True, image="images/v13/Scene 40/v13chlff2Start.webp", start_image="images/v13/Scene 40/v13chlff2Start.webp") # Chloe face fuck FPP spedup

        scene v13chlff
        with dissolve
        pause

        cl "*Gags*"

        scene v13chlfff # ignore as anim
        with dissolve
        pause

        u "Mmhmm!"

        scene v13chlff2 # ignore as anim
        with dissolve
        pause

        cl "*Moans*"

        u "Damn it Chloe... Those perfect lips."

        scene v13chlff2f # Ignore as anim
        with dissolve
        pause

        u "Way too fucking good... *Moans*"

        scene v13s40end_12 # TPP. Show MC pushing Chloe further back on the bed while choking her
        with dissolve

        pause

        scene v13s40end_13 # TPP. Show MC getting ready to fuck her while her legs are off the bed
        with dissolve

        pause

        image v13chltt = Movie(play="images/v13/Scene 40/v13chltt.webm", loop=True, image="images/v13/Scene 40/v13chlttStart.webp", start_image="images/v13/Scene 40/v13chlttStart.webp") # Chloe Table top
        image v13chlttf = Movie(play="images/v13/Scene 40/v13chlttf.webm", loop=True, image="images/v13/Scene 40/v13chlttStart.webp", start_image="images/v13/Scene 40/v13chlttStart.webp") # Chloe Table top spedup
        image v13chltt2 = Movie(play="images/v13/Scene 40/v13chltt2.webm", loop=True, image="images/v13/Scene 40/v13chltt2Start.webp", start_image="images/v13/Scene 40/v13chltt2Start.webp") # Chloe Table top FPP
        image v13chltt2f = Movie(play="images/v13/Scene 40/v13chltt2f.webm", loop=True, image="images/v13/Scene 40/v13chltt2Start.webp", start_image="images/v13/Scene 40/v13chltt2Start.webp") # Chloe Table top FPP spedup

        scene v13chltt # Ignore as anim
        with dissolve
        pause

        cl "Ohh, fuck! [name]! [name]... I-I'm cumming... *Moans*"

        scene v13chlttf # Ignore as anim
        with dissolve

        cl "[name]! *Gasps* F-f-uck... *Moans*"

        scene v13chltt2 # ignore as anim
        with dissolve
        pause

        u "Ah, shit Chlo... *Moans* You- I'm-"

        scene v13chltt2f # ignore as anim
        with dissolve
        pause

        u "*Moans* I'm gonna... Ohhh, my fucking... god!"

        scene v13s40end_14 # TPP. MC cumming in Chloe
        with vpunch

        pause

        stop music fadeout 3
        play music "music/v13/Track Scene 40_3.mp3" fadein 2

        scene v13s40end_15 # FPP. MC laying on top of Chloe, looking into her eyes, Chloe smiling, mouth open
        with dissolve

        cl "That was the best sex I've ever had! *Laughs* Holy shit..."

        scene v13s40end_15a # FPP. Same ass v13s40end_15, Chloe mouth closed
        with dissolve

        u "I can say the same."

        scene v13s40end_15
        with dissolve

        cl "It's gonna be hard to top that, you know? *Chuckles*"

        scene v13s40end_15a
        with dissolve

        u "I can say the same to you!"

        scene v13s40end_15
        with dissolve

        cl "Oh, really? *Chuckles*"

        scene v13s40end_15a
        with dissolve

        u "Really."

        scene v13s40end_15
        with dissolve

        cl "Oh my god, okay... Get up and let me go to the bathroom real quick. You're making me blush. *Chuckles*"

        scene v13s40end_15a
        with dissolve

        u "Haha."

        scene v13s40end_16 # TPP. Show MC getting in bed, Chloe getting up, both smiling, mouths closed
        with dissolve

        pause

        scene v13s40end_17 # FPP. MC laying down in bed, watching as Chloe walks into the bathroom, focus a bit on her ass
        with dissolve

        pause

        scene v13s40end_18 # TPP. Show MC laying in bed, naked, smiling, mouth closed
        with dissolve

        $ grant_achievement("we_like_them_wild")
        
        u "(This girl is gonna drive me crazy...) *Laughs*"

        scene v13s40end_17a # FPP. Same as v13s40end_17, Chloe coming out of bathroom, smiling, mouth closed, naked
        with dissolve

        pause

        scene v13s40end_19 # TPP. Show MC getting out of bed, Chloe getting in to bed, slight smiles, mouths closed
        with dissolve

        pause

        scene v13s40end_20 # TPP. Show MC putting on his clothes, slight smile, mouth closed
        with dissolve

        pause 1

        $ renpy.end_replay()

        stop music fadeout 3

        jump v13s40a

    else:
        scene v13s40end_2
        #with dissolve

        pause 1

        stop music fadeout 3
        play music "music/v13/Track Scene 40_3.mp3" fadein 2

        scene v13s40end_3
        with dissolve

        pause 1

        scene v13s40end_21 # TPP. Show Chloe hugging MC, Chloe mouth open, MC mouth closed, both smiling (this is right after v13s40end_3)
        with dissolve

        cl "That was fun. *Chuckles* A little more different than expected, but fun."

        scene v13s40end_22 # FPP. MC standing next to Chloe, Chloe smiling, mouth open, looking up at MC, she is still laying down
        with dissolve

        cl "You should stay and cuddle with me... After all that, I'm pretty tired."

        scene v13s40end_22a # FPP. Same v13s40end_22, Chloe mouth closed
        with dissolve

        u "*Chuckles* I'd be happy to."

        scene v13s40end_20
        with dissolve

        $ renpy.end_replay()

        pause 1

        stop music fadeout 3

        jump v13s40a