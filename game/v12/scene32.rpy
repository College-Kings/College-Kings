# SCENE 32:
# Locations: Sidewalk, Photoshoot with 2 sets and flower bouquet stand
# Characters: MC (Outfit: 3), AUBREY (Outfit: 2), NAOMI (Outfit: 1), PHOTOGRAPHER (Outfit: 1)
# Time: Morning
# Phone Images: YES
# v12aumcsexy (MC and Aubrey sexy pose)
# v12aunaselfie (Aubrey and Naomi selfie wearing bras, both smiling, mouths closed)
# v12aucar (Aubrey sexy pic on car)

init python:
    def v12s32kiwiiPost1_Reply1():
        v12s32kiwiiPost1.newComment(naomi, _("Hehe, you too! Hope to see you soon...;)"), number_likes=renpy.random.randint(583, 912))
        v12s32kiwiiPost1.newComment(chloe, _("OMG!?!?!?!"), number_likes=renpy.random.randint(124,354))
        v12s32kiwiiPost1.newComment(imre, _("Bro... Is that you?!"), mentions=[mc], number_likes=renpy.random.randint(53,93))
    
    def v12s32kiwiiPost1_Reply2():
        v12s32kiwiiPost1.newComment(aubrey, _("You're so welcome... Today was amazing. <3"), number_likes=renpy.random.randint(253, 462))
        v12s32kiwiiPost1.newComment(chloe, _("OMG!?!?!?!"), number_likes=renpy.random.randint(124,354))
        v12s32kiwiiPost1.newComment(imre, _("Bro... Is that you?!"), mentions=[mc], number_likes=renpy.random.randint(53,93))

label v12s32:
# -MC and Aubrey are walking along the sidewalk-

    scene v12s32_1 # TPP show mc and aubrey walking along the side walk, make sure Aubrey is on the side of the wall, not the street for easier backgrounds in FPP. Mc looking at aubrey, mc mouth open, curious
    with fade

    u "So, where exactly are they doing the shoot?"

    play music "music/v12/Track Scene 32_1.mp3" fadein 2

    scene v12s32_2 # FPP, close up AUbrey looking at mc, but walking forwards. Aubrey slightly nervous not smiling, mouth open
    with dissolve

    au "It's at a Lew's store."

    scene v12s32_2a # same as 2, mouth closed
    with dissolve

    u "*Laughs* Tell me why I thought it was just at a random photography studio..."

    scene v12s32_2
    with dissolve

    au "Ha, that's what I thought at first too..."

    scene v12s32_2a
    with dissolve

    u "You seem a little off, everything okay?"

    scene v12s32_2
    with dissolve

    au "Yeah, everything's great. It's just..."

    au "I haven't seen my sister in a really long time and... Well, you'll see how she acts."

    scene v12s32_2a
    with dissolve

    u "What does that mean? Should I be preparing for something?"

    scene v12s32_2b # same as 2, aubrey slight smile, mouth open
    with dissolve

    au "You have nothing to worry about, I'm the one that has to get ready. *Chuckles*"

    scene v12s32_2c # same as 2b, mouth closed
    with dissolve

    u "You're starting to actually scare me... *Chuckles*"

    scene v12s32_3 # tpp Aubrey and mc enter the photoshoot place
    with fade

    pause 0.7

    stop music fadeout 3
    play music "music/v12/Track Scene 32_2.mp3" fadein 2

    scene v12s32_4 # FPP shows photographer taking pictures of Naomi (Aubrey's sister)
    with dissolve

    au "Leave it to my sister to get started early..."

    scene v12s32_5 # FPP close up aubrey looking at naomi, shouting, mouth open
    with dissolve

    au "NAOMI!"

    scene v12s32_4a # same as 4, naomi looks to aubrey with a smile
    with dissolve

    pause 0.7

    scene v12s32_6 # FPP show naomi walking towards AUbrey and mc, big smile, mouth open, looking at Aubrey
    with dissolve

    na "Sister sister, with a mister mister! Oooooh..."

    scene v12s32_7 #FPP show naomi close up standing, looking at mc (camera), mouth open, cheeky smile
    with dissolve

    na "Who's your boyfriend?"

    scene v12s32_5b # same as 5, aubrey a little annoyed, mouth open
    with dissolve

    au "He's just my friend, Naomi."

    scene v12s32_7
    with dissolve

    na "*Chuckles* Good to know!"

    na "So what's your name \"just a friend\"?"

    scene v12s32_7a # same as 7, mouth closed
    with dissolve

    u "My name's [name]. Nice to meet you."

    scene v12s32_7
    with dissolve

    na "Well, it's very nice to meet you too!"

    scene v12s32_7b # same as 7, naomi looking at aubrey, confident expression, mouth open
    with dissolve
    
    na "You guys are teensy bit late, though."

    scene v12s32_5b
    with dissolve

    au "No we aren't, we still have two minutes 'til start..."

    scene v12s32_7b
    with dissolve

    na "Early is on time, sister! I already shot most of my needed pics. You guys get to have a good time now."

    scene v12s32_7c # same as 7b, mouth closed
    with dissolve

    u "Wait, we're taking pictures?"

    scene v12s32_7
    with dissolve

    na "Of course you are, cutie... As much as I'd love for you to sit and watch me, today's shoot is for everybody."

    scene v12s32_5c # same as 5b, mouth closed
    with dissolve

    u "Uhm... Aubrey???"

    scene v12s32_5d # same as 5b, aubrey embarassed smile, mouth open, looking at mc
    with dissolve

    au "I felt like you'd try skipping out if I told you we were taking pictures too."

    scene v12s32_5e # same as 5d, mouth closed
    with dissolve

    u "Maybe I would've... Nevertheless, I'm here now, aren't I?"

    scene v12s32_7
    with dissolve

    na "Yes, you are! Captive by the camera. *Laughs*"

    scene v12s32_7a
    with dissolve

    u "So, is there a quick walkthrough or are we just jumping into it?"

    scene v12s32_8 #FPP close up of photographer, neutral expression, mouth open, looking at mc
    with dissolve

    pg "Have you ever done modeling before?"

    scene v12s32_5f # same as 5d, aubrey looking at photographer (off-screen), excited smile, mouth open
    with dissolve

    au "I have!"

    scene v12s32_7d # same as 7b, naomi looking at photographer (off-screen) confident smile, mouth open
    with dissolve

    na "Even if she hadn't, she's my sister. It's in her blood."

    scene v12s32_8a # same as 8, mouth closed
    with dissolve

    u "I haven't done anything this serious before."

    scene v12s32_7
    with dissolve

    na "Well, today's the day!"

    scene v12s32_10 # TPP naomi dragging mc towards the white backdrop setup
    with dissolve

    pause 0.7

    scene v12s32_11 # TPP show mc and aubrey in front of the white backdrop, mc confudsed, aubrey curious smile,mouth open
    with dissolve

    au "Are we doing candid or posing?"

    scene v12s32_12 # FPP close up naomi, looking at aubrey (off-screen), cheeky smile, mouth open
    with dissolve

    na "Posing of course! I wanna see the skills. *Chuckles*"

    scene v12s32_13 # FPP close up photographer, camera in hands not looking into his camera tho, looking at aubrey, serious face, mouth open, explaining
    with dissolve

    pg "Alright, alright! Listen up..."

    pg "We're gonna take a few pics here based on my instructions. Then we're gonna move over to the car and pose with that. Questions?"

    scene v12s32_13a # same as 13, mouth closed
    with dissolve

    u "Nope."

    scene v12s32_14 # FPP close up Aubrey, (who's standing next to mc) looking at mc, slightly concerned for mc, whispering, mouth open
    with dissolve

    au "*Whisper* You're cool with all this right? I'm sorry if you feel kind of thrown into this, I just really wanted to do this shoot and I was too shy to come by myself."

    scene v12s32_14a # same as 14, mouth closed
    with dissolve

    u "*Whisper* But your sister's here?"

    scene v12s32_14
    with dissolve

    au "*Whisper* That's the person I didn't want to be by myself with."

    scene v12s32_14a
    with dissolve

    u "*Whisper* Why don't you-"

    scene v12s32_13
    with dissolve

    pg "You said no questions yet you're yapping away! Let's get posing people!"

    scene v12s32_14
    with dissolve

    au "We'll talk later."

    scene v12s32_13b # same as 13, photographer now looking into his camera, ready to take pictures, mouth open, neutral expression
    with dissolve

    pg "I want you posing together, get sexy!"

    stop music fadeout 3
    play music "music/v12/Track Scene 32_3.mp3" fadein 2

    scene v12s32_15 # TPP show Aubrey and mc, Aubrey looking at the camera, mc confused looking at aubrey, mouth open
    with dissolve

    u "Oh umm..."

    menu:
        "Turn your back to Aubrey":
            $ reputation.add_point(Reputations.BRO)
            scene v12s32_15a #same 15, MC crosses his arms and puts his back to Aubrey, aubrey a bit dissapointed, mouth upen
            with dissolve

            au "Oh, okay."

            scene v12s32_15b # -Aubrey crosses her arms and poses with her back to MC-
            with dissolve

            pause 0.7

            scene v12s32_15b # -Aubrey crosses her arms and poses with her back to MC-
            with flash

            pause 0.7

            scene v12s32_13b
            with dissolve

            pg "I wouldn't call that sexy but, alright..."

        "Put your arms around Aubrey":
            $ reputation.add_point(Reputations.BOYFRIEND)
            scene v12s32_15c #same 15, Aubrey has her back to MC and he wraps his arms around her, squeezing her in tight, Aubrey smiles at him, mouth closed
            with dissolve

            na "Oooh! I'm liking what I see!"

            scene v12s32_15c 
            with flash

            pause 0.7

            scene v12s32_13b
            with dissolve

            pg "This is what you call perfection!"

            scene v12s32_15d # same 15c, aubrey mouth open
            with dissolve

            au "I think they like us. *Chuckles*"

            scene v12s32_15e # same 15d, aubrey mouth closed, mc mouth open smiling
            with dissolve

            u "And so do I."

    scene v12s32_15f #same 15, aubrey and mc do a different photo-pose (choose one from a pose pack or do one yourself). 
    with dissolve

    pause 0.7

    scene v12s32_15f
    with flash

    pause 0.7

    scene v12s32_13b
    with dissolve

    pg "Let's do one more!"

    scene v12s32_15g #same 15f, aubrey and mc do another different photo-pose (choose one from a pose pack or do one yourself). 
    with dissolve

    pause 0.7

    scene v12s32_15g
    with flash

    pause 0.7

    scene v12s32_13
    with dissolve

    pg "Alright, these are very good shots and I guarantee they'll help the brand a lot. I can't wait to get these on our store Kiwii. You two have Kiwii's, right?"

    scene v12s32_14b # same 14, aubrey looking at photographer (off-screen), excited, mouth open
    with dissolve

    au "We do! I didn't know we were gonna get to be on the store page!"

    scene v12s32_13
    with dissolve

    pg "Of course you are!"

    scene v12s32_14d # same 14, aubrey looking at mc super excited, mouth open
    with dissolve

    au "Oh my god, [name]... This is so fucking sick!"

    scene v12s32_12
    with dissolve

    na "Following in your sister's footsteps... This is how it starts Aubby!"

    scene v12s32_14c # same 14b, mouth closed
    with dissolve

    u "*Chuckles* \"Aubby\"?"

    scene v12s32_14
    with dissolve

    au "It's just something she does, please don't read into it..."

    scene v12s32_13
    with dissolve

    pg "Off to the next set people!"

    scene v12s32_16 # TPP show mc and aubrey walking towards the next set, the car chloe and mc rode in in front of a backdrop, both smiling
    with dissolve

    pause 0.7

    scene v12s32_17 #FPP close up of the set with no people on it
    with dissolve

    u "(This is the same car Chloe and I rode in.)"

    scene v12s32_18 # FPP photographer looking at mc (who's not standing on the set, but before it), mouth open, holding camera but not looking into it
    with dissolve

    pg "We want to get a few spicy photos for this setup. Don't worry, we're photoshopping your clothes."

    scene v12s32_19 # FPP naomi walks onto the set, confident smile, mouth open
    with dissolve

    na "I'll show you how this is done. *Chuckles*"

    scene v12s32_18a #same 18 FPP photographer looking at naomi (off-screen, she's at the car now), mouth open, smiling
    with dissolve

    pg "Ahh, my goddess..."

    scene v12s32_20a # FPP close up Aubrey, who's standing next to you,looking at naomi (off-screne), mouth close, slightly concerned expression
    with dissolve

    u "She's confident!"

    scene v12s32_20b # same as 20a, aubrey now looking at mc, mouth open, slightly concerned expression
    with dissolve

    au "Sometimes too confident..."

    scene v12s32_21 #FPP closeup  naomi, in front of the car, starts taking off her top (has bra beneath)
    with dissolve

    pause 0.7

    scene v12s32_21a #same as 21 naomi, now just in bra, smiling at mc
    with dissolve

    u "(Damn!)"

    scene v12s32_21b # same 21, naomi poses seductively in front of the car in just her bra
    with dissolve

    pause 0.7

    scene v12s32_21b
    with flash

    pause 0.7

    scene v12s32_18b # same 18a, close up photographer now taking pictures of naomi (off screen), mouth open, excited
    with dissolve

    pg "YES, MA'AM!! Give it to us..."

    scene v12s32_21c # same 21, naomi poses seductively, in a different pose in front of the car in just her bra
    with dissolve

    pause 0.7

    scene v12s32_21c
    with flash

    pause 0.7

    scene v12s32_18b
    with dissolve

    pg "Yes, girl!"

    scene v12s32_20 # same 2a, mouth open
    with dissolve

    au "*Whisper to self* I'll never be that fucking good..."

    scene v12s32_20a
    with dissolve

    u "Huh?"

    scene v12s32_20b
    with dissolve

    au "What? Oh, nothing. She's really good."

    scene v12s32_20c # same 20b, mouth closed
    with dissolve

    u "(I think she's jealous of her sister or something, maybe I should boost her up.)"

    menu:
        "Boost Aubrey":
            $ reputation.add_point(Reputations.TROUBLEMAKER)
            $ v12s32_Aubrey_Boost = True
            $ aubrey.points += 1

            scene v12s32_21c 
            with dissolve
            u "You thought that was good? Aubrey can do that, and better... Get up there Aubrey!"

            scene v12s32_20b
            with dissolve
            au "*Whisper* [name]!"

            scene v12s32_21d # same 21c, naomi looking at Aubrey (off-screen), mouth open, excited, with one eyebrow raised
            with dissolve

            na "Ooohh! Someone sure has a lot of faith in you to think you can out do me. *Chuckles* Get up here little sis, let's see it!"

            scene v12s32_20a
            with dissolve

            u "*Whisper* You got this, just be yourself."

        "Leave it alone":
            $ reputation.add_point(Reputations.BRO)
            scene v12s32_21c 
            with dissolve

            u "(She's already pressured by her sister, I shouldn't add to it.)"

            scene v12s32_21d
            with dissolve

            na "Hey Aubby, hope you were paying close attention 'cause it's your turn."

            scene v12s32_20
            with dissolve

            au "*Whisper to self* Let's get this over with."

    if aubrey.points == 0:
        scene v12s32_20
        with dissolve

        au "*Sighs* Fine..."

    if aubrey.points > 0:
        scene v12s32_20d # same as 20b, aubrey cute smile at mc, mouth open
        with dissolve

        au "Wish me luck?"

        scene v12s32_20e # same as 20d, mouth closed
        with dissolve

        u "You don't need luck... Look at you."

        scene v12s32_20d
        with dissolve

        au "*Chuckles*"

        scene v12s32_22 #TPP aubrey kisses mc on the cheek
        with dissolve

        pause 0.7

    scene v12s32_23 # FPP closeup aubrey walking towards the car, starts taking her top off (bra underneath)
    with dissolve

    pause 0.7

    scene v12s32_24 # FPP closeup Aubrey makes a pose towards the camera in front of the car in her bra
    with dissolve

    u "(Damn, she really is good!)"

    scene v12s32_24
    with flash

    pause 0.7

    scene v12s32_18b
    with dissolve

    pg "You're a natural! Naomi, you may have some competition..."

    pg "I bet out of all the photos we take today, these are gonna be the ones they want."

    scene v12s32_25 # FPP Closeup Naomi looking at Aubrey (Off-screen), cheeky smile, mouth open
    with dissolve

    na "Maybe I showed her a little too much of my talent... *Chuckles*"

    scene v12s32_18b
    with dissolve

    pg "I don't know! This all seems all nat-u-ral!"

    scene v12s32_24a # same 24, aubrey looking at the camera (off-screen), mouth open, smiling
    with dissolve

    au "*Chuckles* Can I see the pictures?"

    scene v12s32_18a
    with dissolve

    pg "Of course! I'm going to send all of them to you."

    scene v12s32_24a
    with dissolve

    au "Thank you so much!"

    scene v12s32_26 # FPP Aubrey walking towards you smiling, still in bra
    with dissolve

    pause 0.7

    stop music fadeout 3
    play music "music/v12/Track Scene 32_4.mp3" fadein 2

    if v12s32_Aubrey_Boost:
        scene v12s32_27 # TPP show aubrey hugging mc, aubrey mouth open, cute smile
        with dissolve

        au "Thanks for the support, that was definitely the boost of confidence I needed."

        scene v12s32_27a # same 27, aubrey mouth closed, mc mouth open smiling
        with dissolve

        u "Of course. I'll always be there for you."

    scene v12s32_28 # FPP close up photographer looking at Aubrey (off-camera, standing near mc), mouth open,thinking smile
    with dissolve

    pg "Have you thought about going into modeling? I think you'd make an amazing Kiwii model... And if you're worried about looking like you're riding your sister's road to fame, don't."

    pg "With pictures like this... You'll make it all on your own."

    scene v12s32_29 # FPP close up Aubrey, mouth open, smile, looking at photographer (off-camera)
    with dissolve

    au "I've always thought about it, even before my sister started modeling I wanted to, but when she started and blew up I never thought I could match her speed. I mean, look at her."

    scene v12s32_28
    with dissolve

    pg "Your sister is great in her own ways, but you yourself have a serious natural talent."
    pg "Your sister and I have worked together for a long while and I know you're from the States, but if you'd be willing to work with me I'd be able to make you famous."

    scene v12s32_29
    with dissolve

    au "I... I really want to, but-"

    scene v12s32_30 # FPP close up naomi, looking at photographer (off-camera), mouth open, cheeky smile
    with dissolve

    na "She'll do it."

    scene v12s32_29b #same 29, aubrey surprised, mouth open, looking at naomi (off-camera)
    with dissolve

    au "NAOMI!?"

    scene v12s32_29c # same 29b, mouth closed
    with dissolve

    u "Aubrey, you looked good doing that. Really fucking good!"

    scene v12s32_29d # same 29b, looking at mc (into the camera), cute smile,mouth open
    with dissolve

    au "Do you... You actually mean that?"

    scene v12s32_29e # same 29d, mouth closed
    with dissolve

    u "I do. It's the happiest you've looked in a long time."

    scene v12s32_29d
    with dissolve

    au "*Chuckles* Okay."

    scene v12s32_29
    with dissolve

    au "If [name] thinks I'd be good, then I'll give it a try."

    scene v12s32_28
    with dissolve

    pg "Perfect! Naomi, would you mind taking your sister over there to get her info set up?"

    scene v12s32_30
    with dissolve

    na "*Sighs* Yeah, guess we're on that \"out with the old and in with the new\" type of vibe... C'mon Aubrey."

    scene v12s32_31 #FPP Aubrey and Naomi walk off with each other
    with dissolve

    pause 0.7

    scene v12s32_28b #FPP same as 28, photographer looking at mc (at the camera), jealous smile, mouth open
    with dissolve

    pg "You're a lucky guy, my friend."

    scene v12s32_28c # same 28b, mouth closed
    with dissolve

    u "Why do you say that?"

    scene v12s32_28b
    with dissolve

    pg "I've been trying to get with Naomi for years..."

    pg "You walk in and not only does she like you but, it's clear you've also got a shot with her sister. Honestly, her sister is badder than she is. *Chuckles*"

    scene v12s32_28c
    with dissolve

    u "Aubrey isn't the relationship type."

    scene v12s32_28b
    with dissolve

    pg "*Laughs* Don't ever believe that BS... Everyone is the relationship type. You just have to tame the beast."

    scene v12s32_28c
    with dissolve

    u "I'll keep that in mind..."

    scene v12s32_28b
    with dissolve

    pg "Don't just keep it in mind, act on it. Get her something. Make her see you. There's some flowers right there, feel free to grab a bouquet."
    pg "Hell, if I can't get her, I'd rather you than no one. Make me proud!"

    scene v12s32_28d # same 28b, photographer walks off
    with dissolve

    pause 0.7

    scene v12s32_32 # TPP mc walks over to the flower stand
    with dissolve

    u "(Hmmm...)"

    scene v12s32_33 # FPP, close up Aubrey standing in fron mc, looking at mc, slight smile, mouth open
    with dissolve

    au "They got me all set up! I think my sister is a little salty because she's just packed up and left... She said she had somewhere to be and that we'll talk later. *Sighs*"

    scene v12s32_33a # same 33, mouth closed
    with dissolve

    u "Guess it bothered her how great you were."

    scene v12s32_33
    with dissolve

    au "I did alright I guess."

    scene v12s32_33a
    with dissolve

    u "I've never seen you flustered or even bothered, yet with this you've been acting unlike yourself. As if you're worried about impressing your sister or something."

    scene v12s32_33
    with dissolve

    au "Or something, yeah."

    au "I really like modeling and I think becoming a Kiwii model would be great, but I don't want to look like I'm doing it just because of her."
    au "I also don't want any success if it feels like I only got it because of her."

    au "I get she's older and everything, but this was my dream first... She wanted to be a vet. *Chuckles*"

    scene v12s32_33a
    with dissolve

    u "Then don't worry about her and live out your dream."

    scene v12s32_33
    with dissolve

    au "Thanks, I'm feeling a lot better about doing just that... The staff gave me the pictures and they really do look amazing."

    au "I wanna get back as soon as possible and show these to everyone. I posted a few on Kiwii and my sister did too. Let's hurry back."

    python:
        v12s32kiwiiPost1 = KiwiiPost(lews_official, "phone/kiwii/Posts/v12/v12s32_15g.webp", _("New faces in our new pieces! Check out the new Lavish Line on our website ;)"), number_likes=3889)
        v12s32kiwiiPost1.newComment(naomi, _("That's my baby sis! <3"), number_likes=renpy.random.randint(952, 1512))
        v12s32kiwiiPost1.newComment(aubrey, _("Thank you so much for having us! Can't wait for the future..."), number_likes=renpy.random.randint(367, 526))
        v12s32kiwiiPost1.newComment(chloe, _("OMG!?!?!?!"), number_likes=renpy.random.randint(124,354))
        v12s32kiwiiPost1.newComment(imre, _("Bro... Is that you?!"), mentions=[mc], number_likes=renpy.random.randint(53,93))

        v12s32kiwiiPost2 = KiwiiPost(naomi, "phone/kiwii/Posts/v12/v12s32_24.webp", _("When little sis visits you at work and leaves with your JOB! #ProudBigSis"), number_likes=2107)
        v12s32kiwiiPost2.newComment(aubrey, _("Haha! I love you boo... Thank you for today :)"), mentions=[naomi], number_likes=renpy.random.randint(278, 363))
        v12s32kiwiiPost2.newComment(naomi, _("You're sooo welcome sissy. #ItRunsInTheFamily"), mentions=[aubrey], number_likes=renpy.random.randint(747, 973)) 
        v12s32kiwiiPost2.newComment(nora, _("Hotties!! Hope you had an amazing time... Can't wait to see all the pics!"), number_likes=renpy.random.randint(253, 462))
        v12s32kiwiiPost2.newComment(chloe, _("JOB?!?!?!"), number_likes=renpy.random.randint(245, 587))
        v12s32kiwiiPost2.newComment(naomi, _("Thank you... <3"), number_likes=renpy.random.randint(346, 579))
        v12s32kiwiiPost2.newComment(aubrey, _("Thanks guys... I'll tell you all about it Chlo! Lol"), number_likes=renpy.random.randint(253, 462))

        v12s32kiwiiPost3 = KiwiiPost(aubrey, "phone/kiwii/Posts/v12/v12s32_33.webp", _("You're looking at the newest Lew's model! #BestDayEver"), number_likes=934)
        v12s32kiwiiPost3.newComment(naomi, _("Watch out world, there's two of us... ;)"), number_likes=renpy.random.randint(532, 737))
        v12s32kiwiiPost3.newComment(chloe, _("Holy shit, Aubs! Fucking HOTTTT!!!"), number_likes=renpy.random.randint(320, 479))
        v12s32kiwiiPost3.newComment(aubrey, _("Haha, thank you babes <3"), number_likes=renpy.random.randint(253, 462))
        v12s32kiwiiPost3.addReply(_("Absolutely deserved."), number_likes=renpy.random.randint(126, 367))
        v12s32kiwiiPost3.newComment(ryan, _("Holy..."), number_likes=renpy.random.randint(78, 153))
        v12s32kiwiiPost3.newComment(imre, _("Pick up your jaw idiot! LOL"), mentions=[ryan], number_likes=renpy.random.randint(69, 178))


#    python:
#        v12s32kiwiiPost1 = KiwiiPost(lews_official, "v12/v12aumcsexy.webp", _("New faces in our new pieces! Check out the new Lavish Line on our website ;)"), number_likes=3889)
#        v12s32kiwiiPost1.newComment(naomi, _("That's my baby sis! <3"), number_likes=renpy.random.randint(952, 1512))
#        v12s32kiwiiPost1.newComment(aubrey, _("Thank you so much for having us! Can't wait for the future..."), number_likes=renpy.random.randint(367, 526))
#        v12s32kiwiiPost1.addReply(_("Thanks for the invite! It was really nice to meet you..."), v12s32kiwiiPost1_Reply1, mentions=[naomi], number_likes=renpy.random.randint(278,421))
#        v12s32kiwiiPost1.addReply(_("Had an amazing time today... Thank you, gorgeous!"), v12s32kiwiiPost1_Reply2, mentions=[aubrey])
#
#        v12s32kiwiiPost2 = KiwiiPost(naomi, "v12/v12aunaselfie.webp", _("When little sis visits you at work and leaves with your JOB! #ProudBigSis"), number_likes=2107)
#        v12s32kiwiiPost2.newComment(aubrey, _("Haha! I love you boo... Thank you for today :)"), mentions=[naomi], number_likes=renpy.random.randint(278, 363))
#        v12s32kiwiiPost2.newComment(naomi, _("You're sooo welcome sissy. #ItRunsInTheFamily"), mentions=[aubrey], number_likes=renpy.random.randint(747, 973)) 
#        v12s32kiwiiPost2.addReply(_("Even more beautiful in person..."), number_likes=renpy.random.randint(562, 789))
#        v12s32kiwiiPost2.addReply(_("Aww, love this pic of you guys!"), number_likes=renpy.random.randint(578, 865))
#        v12s32kiwiiPost2.newComment(nora, _("Hotties!! Hope you had an amazing time... Can't wait to see all the pics!"), number_likes=renpy.random.randint(253, 462))
#        v12s32kiwiiPost2.newComment(chloe, _("JOB?!?!?!"), number_likes=renpy.random.randint(245, 587))
#        v12s32kiwiiPost2.newComment(naomi, _("Thank you... <3"), number_likes=renpy.random.randint(346, 579))
#        v12s32kiwiiPost2.newComment(aubrey, _("Thanks guys... I'll tell you all about it Chlo! Lol"), number_likes=renpy.random.randint(253, 462))
#
#        v12s32kiwiiPost3 = KiwiiPost(aubrey, "v12/v12aucar.webp", _("You're looking at the newest Lew's model! #BestDayEver"), number_likes=934)
#        v12s32kiwiiPost3.newComment(naomi, _("Watch out world, there's two of us... ;)"), number_likes=renpy.random.randint(532, 737))
#        v12s32kiwiiPost3.newComment(chloe, _("Holy shit, Aubs! Fucking HOTTTT!!!"), number_likes=renpy.random.randint(320, 479))
#        v12s32kiwiiPost3.newComment(aubrey, _("Haha, thank you babes <3"), number_likes=renpy.random.randint(253, 462))
#        v12s32kiwiiPost3.addReply(_("Absolutely deserved."), number_likes=renpy.random.randint(126, 367))
#        v12s32kiwiiPost3.newComment(aubrey, _(":) Thanks to you..."), number_likes=renpy.random.randint(167, 241))
#        v12s32kiwiiPost3.newComment(ryan, _("Holy..."), number_likes=renpy.random.randint(78, 153))
#        v12s32kiwiiPost3.newComment(imre, _("Pick up your jaw idiot! LOL"), mentions=[ryan], number_likes=renpy.random.randint(69, 178))

    scene v12s32_33b # same 33, -Aubrey starts walking away-
    with dissolve

    menu: 
        "Get Aubrey flowers":
            $ s12v32_get_aubrey_flowers = True
            $ reputation.add_point(Reputations.BOYFRIEND)
            u "Wait a minute, Aubrey."

            scene v12s32_33d # aubrey turns around, looks at mc, curious, mouth open
            with dissolve

            au "Yeah?"

            scene v12s32_34 # TPP, Mc grabs some flowers
            with dissolve

            pause 0.75

            scene v12s32_35 # FPP, mc extends Aubrey flowers (she doesn't take them yet) (show her face like a normal close up, looking at mc) (just show the flowers handed in first person), AUbrey surprised smiled
            with dissolve

            u "Your first gift as a future Kiwii modeling star!"

            scene v12s32_35b # same as 35 looks at mc (into the camera), mouth open, surprised smile
            with dissolve

            au "Haha, what!? You didn't have to get me these..."

            scene v12s32_35c # same as 35b, mouth closed
            with dissolve

            u "There's only one girl like you in this world and before all the Kiwii simps start lining up, I wanna be here at the beginning. *Chuckles*"

            scene v12s32_35b
            with dissolve

            au "For once [name], I'll try not to be an asshole. *Chuckles*"

            scene v12s32_35d # same as 35, aubrey takes the flowers, mouth open, genuine smle
            with dissolve

            au "Thank you."

            scene v12s32_35e # same 35d, mouth closed
            with dissolve

            u "You're very welcome."

            scene v12s32_35d
            with dissolve

            au "Now c'mon, let's hurry back so I can get these into some water."

            scene v12s32_35e
            with dissolve

        "Don't get her flowers":
            u "(That'd be doing too much... We're just friends.)"

    u "Right, let's go."

    stop music fadeout 3
    jump v12s33 #scene 33