# SCENE 32: Gym session with Imre
# Locations: The Gym
# Characters: MC (Outfit: 2), IMRE (Outfit: 1), RUBEE (Outfit: 1)
# Time: Afternoon

label v14s32:
    scene v14s32_1 # TPP. MC walking into the Gym, slight smile, mouth closed
    with dissolve

    pause 0.75

    play music "music/v12/Track Scene 27_3.mp3" fadein 2

    play sound "sounds/hs.mp3"

    scene v14s32_2 # FPP. MC looking at Imre who is punching the punching bag, Imre slight smile, mouth closed.
    with dissolve

    u "Getting a headstart, huh?"

    play sound "sounds/hs.mp3"

    scene v14s32_2a # FPP. Same as v14s32_2, Imre not looking at MC yet punching at the punching bag with his other hand, Imre slight smile, mouth open.
    with dissolve

    imre "Yep, tryna break a sweat before you even enter the building."

    scene v14s32_2b # FPP. Same as v14s32_2a, Imre punches the bag hard, Imre slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v14s32_2c # FPP. Same as v14s32_2b, Imre now looking at MC, shocked smile, mouth open.
    with dissolve

    imre "What are you wearing? *Laughs* Why didn't you come dressed to work out?"

    scene v14s32_2d # FPP. Same as v14s32_2c, Imre slight smile, mouth closed.
    with dissolve

    u "What do you mean, dickhead? I came straight over when you called. *Laughs*"

    u "When I said that I was heading straight over, what part of that sounded like I was heading home to change first?"

    scene v14s32_2e # FPP. Same as v14s32_2d, Imre slight smile, mouth open.
    with dissolve

    imre "If you needed some time to change, you should've just said that."

    scene v14s32_2d
    with dissolve

    u "I'll be fine."

    scene v14s32_2e
    with dissolve

    imre "Your call, man. Don't come crying to me if you get hurt."

    scene v14s32_2d
    with dissolve

    u "Ha... I won't be crying."

    scene v14s32_2e
    with dissolve

    imre "Good, that's one less dude I have to worry about being a bitch."

    scene v14s32_2d
    with dissolve

    u "Who are you talking about now?"

    scene v14s32_2e
    with dissolve

    imre "I'm sure you can guess."

    scene v14s32_2d
    with dissolve

    menu:
        "Chris":
            $ add_point(KCT.TROUBLEMAKER)

            u "Chris?"

            scene v14s32_2e
            with dissolve

            imre "What? No. Ryan."

        "Ryan":
            $ add_point(KCT.BRO)

            scene v14s32_2d
            #with dissolve
            
            u "Ryan?"

            scene v14s32_2e
            with dissolve

            imre "Bingo."

    scene v14s32_2d
    with dissolve

    u "*Sighs* What's going on now?"

    scene v14s32_2e
    with dissolve

    imre "He's going around telling everyone that I beat up a guy in Europe and took all of his money."

    scene v14s32_2d
    with dissolve

    u "He-"

    scene v14s32_2e
    with dissolve

    imre "Let me just add, he isn't telling the whole story."

    imre "He didn't mention that the guy was a piece of shit, who stole the money from other people in the first place."

    imre "Hell, I mean... I was basically giving back."

    scene v14s32_2d
    with dissolve
    
    menu:
        "You're right":
            $ add_point(KCT.BRO)

            u "Yeah, I guess it is kinda messed up that Ryan doesn't tell the whole story."

            scene v14s32_2e
            with dissolve

            imre "Exactly. That's what I'm saying!"

        "Please just get along":
            $ add_point(KCT.BOYFRIEND)

            scene v14s32_2d
            #with dissolve
            
            u "*Sighs*"

            u "It'd be really nice if you two just got along."

            scene v14s32_2e
            with dissolve

            imre "Not gonna happen, don't even start. I tried and he fucked me over again."

            scene v14s32_2d
            with dissolve

            u "Whatever man, but don't say I didn't tell you that this is going to cause more harm than good, for both of you."

            scene v14s32_2e
            with dissolve

            imre "Uh-huh."

    scene v14s32_2d
    with dissolve

    u "On a more positive note, we never talked about the Red Light District after what went down."

    u "Did you have fun? I don't even know what you did the entire time."

    scene v14s32_2e
    with dissolve

    imre "*Laughs* I had a really good time."

    imre "If you wanna know the truth, I went back to the hotel, got money from Chris and then went right back to the brothel. *Chuckles*"

    scene v14s32_2d
    with dissolve

    u "That's why I couldn't find you..."

    scene v14s32_2e
    with dissolve

    imre "Huh?"

    scene v14s32_2d
    with dissolve

    u "I went looking for you after you stormed off."

    scene v14s32_2e
    with dissolve

    imre "Oh shit, my bad."

    imre "I was just pissed and focused on getting laid so, I wanted to enjoy that combo with some angry sex."

    scene v14s32_2d
    with dissolve

    u "Okay... That sounds healthy."

    scene v14s32_2e
    with dissolve

    imre "Don't act brand new, you know how I am. *Laughs*"

    scene v14s32_2d
    with dissolve

    u "*Chuckles* That I do."

    scene v14s32_3 # TPP. MC walking up to the punching bag, Imre standing off to MC's side, Both slight smile, mouth closed.
    with dissolve

    pause 0.75

    play sound "sounds/hs.mp3"

    scene v14s32_3a # TPP. Same as v14s32_3, MC throwing a punch at the punching bag.
    with dissolve

    pause 0.75

    play sound "sounds/hs.mp3"

    scene v14s32_3b # TPP. Same as v14s32_3a, MC throwing a punch with his other hand.
    with dissolve

    pause 0.75

    play sound "sounds/hs.mp3"

    scene v14s32_3c # TPP. MC hits the bag hard, Imre slight smile, mouth open.
    with dissolve

    imre "Okay, I see you."

    scene v14s32_2d
    with dissolve

    u "Just some light work."

    scene v14s32_2e
    with dissolve

    imre "You've been practicing already?"

    scene v14s32_2d
    with dissolve

    u "No, I'm just good."

    scene v14s32_2e
    with dissolve

    imre "Wait..."

    scene v14s32_2d
    with dissolve

    u "*Chuckles* What?"

    scene v14s32_2f # FPP. Same as v14s32_2e, Imre staring off past MC, shocked face, mouth closed.
    with dissolve

    pause 0.75

    scene v14s32_2g # FPP. Same as v14s32_2f, Imre pointing behind MC, shocked face, mouth closed.
    with dissolve

    pause 0.75

    scene v14s32_4 # FPP. MC looking behind him and sees Rubee kickboxing with a punching with her male personal trainer holding the bag, Rubee and Trainer neutral face, Rubee mouth open, Trainer mouth closed.
    with dissolve

    rub "*Grunts*"

    scene v14s32_4a # FPP. Same as v14s32_4, Trainer neutral face, mouth open, Rubee Neutral face, mouth closed.
    with dissolve

    trainer "Perfect, two more."

    scene v14s32_4
    with dissolve

    rub "No... *Grunts* Five more..."

    scene v14s32_4b # FPP. Same as v14s32_4a, Trainer slight smile, mouth open, Rubee Neutral face, mouth closed.
    with dissolve

    trainer "*Chuckles"

    scene v14s32_2h # FPP. Same as v14s32_2f,Imre looking at MC, Imre shocked face, mouth open.
    with dissolve

    imre "She looks like a warrior..."

    scene v14s32_2i # FPP. Same as v14s32_2h, Imre shocked face, mouth closed.
    with dissolve

    u "Yeah, like she could snap you in half. *Laughs*"

    scene v14s32_2h
    with dissolve

    imre "No... shit..."

    scene v14s32_5 # TPP. (Similar to v14s32_4) Close up of Rubee bending over and picking up her gym bag, camera focused in on her butt mainly.
    with dissolve

    u "(Holy hell...)"

    scene v14s32_5a # TPP. Same as v14s32_5, Rubee stands up straight.
    with dissolve

    pause 0.75

    scene v14s32_5b # TPP. Rubee turned around and starting to walk towards MC and Imre.
    with dissolve
    
    pause 0.75

    scene v14s32_2h
    with dissolve

    imre "Shit! Here she comes..."

    scene v14s32_2i
    with dissolve

    u "*Chuckles*"

    scene v14s32_6 # FPP. Rubee standing next to MC and Imre, slight smile, mouth open.
    with dissolve

    rub "Hey... I'm Rubee."

    rub "Sorry if this is weird, but... Do you have an older sister? Named Kylie?"

    scene v14s32_6a # FPP. Same as v14s32_6, slight smile, mouth closed.
    with dissolve

    u "Uhh, no-"

    scene v14s32_6
    with dissolve

    rub "It's just that, one of my military friends..."

    rub "She looks... just like you. Haha..."
    
    rub "The female version of you pretty much. *Chuckles*"

    scene v14s32_6a
    with dissolve

    u "Oh, haha. No, as far as I know I'm an only child."

    scene v14s32_6
    with dissolve

    rub "As far as you know..."

    rub "Just kidding, haha. Sorry about that, though. It's been a while since we've all gotten home so maybe I'm just imagining things."

    scene v14s32_6a
    with dissolve

    u "No, no worries. And thank you, for your service."

    scene v14s32_6
    with dissolve

    rub "Oh, of course. Thank you!"

    scene v14s32_2j # FPP. Same as v14s32_2i, Imre looking at Rubee with his jaw dropped, Shocked face, mouth open.
    with dissolve

    imre "*Whispers* You're a total badass..."

    scene v14s32_6
    with dissolve

    rub "*Laughs* Yeah, I am. Well, thanks anyway, bye!"

    scene v14s32_6a
    with dissolve

    u "Bye. Good luck finding your friend."

    scene v14s32_5c # TPP. Same as v14s32_5b, Rubee starting to walk to the gym door.
    with dissolve

    pause 0.75

    play sound "sounds/dooropen.mp3"

    scene v14s32_5d # TPP. Same as v14s32_5c, Rubee holding the door open for herself and looking back at MC, slight smile, mouth open.
    with dissolve

    rub "Thanks!"

    play sound "sounds/doorclose.mp3"

    scene v14s32_5e #TPP. Same as v14s32_5d, The gym door closed and Rubee gone(Don't show Rubee here anywhere to reuse for Imre leaving.).
    with dissolve

    pause 0.75

    scene v14s32_7 # FPP. MC and Imre now at the bench pressing stations, Imre sitting on the benchpress, slight smile, mouth open.
    with dissolve

    imre "*Sighs* What do I gotta do to get a chick like that?"

    scene v14s32_7a # FPP. Same as v14s32_7, Imre slight smile, mouth closed.
    with dissolve

    u "Quit whispering compliments to them when they're standing right next to you?"

    scene v14s32_7
    with dissolve

    imre "Ha ha. Kicking people while they're down is one of your favorite things to do, huh?"

    scene v14s32_7a
    with dissolve

    u "Eh, it depends on the day. *Laughs*"

    scene v14s32_7
    with dissolve

    imre "Speaking of women..."

    imre "Has Chloe been talking about me at all?"

    scene v14s32_7a
    with dissolve

    u "Not really, why?"

    scene v14s32_7
    with dissolve

    imre "Just wondering, since I'm helping her with her campaign and all."

    scene v14s32_7a
    with dissolve

    u "You're helping or supporting?"

    scene v14s32_7
    with dissolve

    imre "Is there really a difference?"

    scene v14s32_7a
    with dissolve

    u "Uh, yeah. One of those includes her asking for your help."

    scene v14s32_7
    with dissolve

    imre "I know she likes my help."

    scene v14s32_7a
    with dissolve

    u "But did she ask?"

    scene v14s32_7
    with dissolve

    imre "She didn't have to, I saw a need and I filled it."
    
    if v14_chrissupport > 1 or not v14_help_chloe:
        imre "Chris got on board to have the Wolves support her because of me."

    if not v14_help_chloe:
        $ v14s32_kiwiiPost1 = KiwiiPost(chloe, "v14/v14s30b_pw_image_two.webp", _("I'd like to officially announce The Chicks' partnership with The Wolves! <3 #PresidentialStatus #Vote4ChloeVote4Wolves"), numberLikes=756)
        $ v14s32_kiwiiPost1.newComment(chris, _("Haha, perfect! #Vote4Chloe"), numberLikes=renpy.random.randint(300, 600), force_send=True)
        $ v14s32_kiwiiPost1.newComment(aubrey, _("Aww! Hell yeah! This is so cute, Chloe <3"), numberLikes=renpy.random.randint(300, 600), force_send=True)
        $ v14s32_kiwiiPost1.newComment(imre, _("Yessss!!!!!"), numberLikes=renpy.random.randint(300, 600), force_send=True)
        $ v14s32_kiwiiPost1.newComment(grayson, _("LMAO you're down bad, huh?"), numberLikes=renpy.random.randint(300, 600), force_send=True)
        $ v14s32_kiwiiPost1.newComment(chloe, _("Be civil at least, Grayson"), numberLikes=renpy.random.randint(300, 600), mentions=[grayson], force_send=True)
        $ v14s32_kiwiiPost1.newComment(riley, _("Omg! Can I have that thing?"), numberLikes=renpy.random.randint(300, 600), force_send=True)

        $ set_presidency_percent(v14_lindsey_popularity - 2)
        imre "She just made an announcement on Kiwii, did you see it yet?"

        call screen phone

    scene v14s32_7a
    with dissolve

    u "Ha... Why are you so supportive of her?"

    u "I know what you said in the hall, but it seems like there's more to it than that."

    scene v14s32_7b # FPP. Same as v14s30_7, Imre looking away from MC, Slight smile, mouth open.
    with dissolve

    imre "I just want her to win, that's all."

    scene v14s32_7a
    with dissolve

    u "(He's obviously hiding something.)"

    u "If you say so."

    scene v14s32_7
    with dissolve

    imre "Man, are we working out or are we talking?"

    scene v14s32_7a
    with dissolve

    u "My bad, my bad!"

    scene v14s32_8 # TPP. Show MC and Imre walking back over to the Punching bag.
    with dissolve

    pause 0.75

    scene v14s32_2e
    with dissolve

    imre "Let me show you something I've been working on. I'm thinking about calling it \"Combo Imre.\""

    scene v14s32_2d
    with dissolve

    u "Wow, you thought about that for a long time, didn't you?"

    scene v14s32_2e
    with dissolve

    imre "No, not really, it's kinda simple..."

    scene v14s32_2d
    with dissolve

    u "Obviously Imre, I was being-"

    u "Nevermind, forget it."

    scene v14s32_2e
    with dissolve

    imre "Okay... Anyways, it's a simple jab jab roundhouse. Watch!"

    scene v14s32_9 # TPP. Close up of Imre hitting the punching bag with his left fist.
    with dissolve
    play sound "sounds/hs.mp3"

    pause 0.75

    play sound "sounds/hs.mp3"
    scene v14s32_9a # TPP. Same as v14s32_9, Imre hitting the punching bag with his right fist.
    with dissolve

    pause 0.75

    play sound "sounds/js.mp3"
    scene v14s32_9b # TPP. Same as v14s32_9a, Imre kicking the punching bag with a roundhouse kick.
    with dissolve

    pause 0.75

    scene v14s32_2e
    with dissolve

    imre "Thoughts?"

    scene v14s32_2d
    with dissolve

    u "Damn!"

    scene v14s32_2e
    with dissolve

    imre "What?"

    scene v14s32_2d
    with dissolve

    u "That was slick."

    scene v14s32_2e
    with dissolve

    imre "You think so?"

    scene v14s32_2d
    with dissolve

    u "I do, let me try it."

    scene v14s32_9c # TPP. Same as v14s32_9, MC punching the bag with his left fist.
    with dissolve
    play sound "sounds/hs.mp3"

    pause 0.75

    play sound "sounds/hs.mp3"
    scene v14s32_9d # TPP. Same as v14s32_9a, MC punching the bag with his right fist.
    with dissolve

    pause 0.75

    play sound "sounds/js.mp3"
    scene v14s32_9e # TPP. Same as v14s32_9b, MC kicking the punching bag with a roundhouse kick.
    with dissolve

    pause 0.75

    scene v14s32_2e
    with dissolve

    imre "Shit! *Laughs* Watching someone else do it makes me realize how cool it actually is. I need to trademark this!"

    scene v14s32_2d
    with dissolve

    u "*Laughs* Do it fast."

    scene v14s32_2e
    with dissolve

    imre "Ha."

    scene v14s32_2d
    with dissolve


    u "So, why'd you need to blow off steam?"

    scene v14s32_2e
    with dissolve

    imre "You really wanna know?"

    scene v14s32_2d
    with dissolve

    u "That's why I asked, ha."

    scene v14s32_2e
    with dissolve

    imre "*Sighs* It's Chris."

    scene v14s32_2d
    with dissolve

    u "What'd he do?"

    scene v14s32_2e
    with dissolve

    imre "He didn't do anything, someone did something to him."

    scene v14s32_2d
    with dissolve

    u "Oh... Who?"

    scene v14s32_2e
    with dissolve

    imre "Nora. She went the entire trip complaining about where Chris was and what he was doing, but guess what?"

    imre "Ever since we've been back, she's been gone."

    scene v14s32_2d
    with dissolve

    u "What do you mean gone?"

    scene v14s32_2e
    with dissolve

    imre "I mean gone. None of us have seen her."

    scene v14s32_2d
    with dissolve

    u "At all?"

    scene v14s32_2e
    with dissolve

    imre "At all."

    scene v14s32_2d
    with dissolve

    u "I'm sure Chris knows where she is."

    scene v14s32_2e
    with dissolve

    imre "I bet not, but maybe. I don't know..."

    imre "Either way, she hasn't been around."

    scene v14s32_2d
    with dissolve

    u "Chris is taking that pretty badly I assume?"

    scene v14s32_2e
    with dissolve

    imre "He's broken, whether he's showing it or not."

    scene v14s32_2d
    with dissolve

    u "*Sighs* That's rough."

    scene v14s32_2e
    with dissolve

    imre "Yeah it is, and you know what?"

    scene v14s32_2d
    with dissolve

    u "Huh?"

    scene v14s32_2e
    with dissolve

    imre "Instead of being here, I should be with him."

    scene v14s32_2d
    with dissolve

    u "Oh, okay."

    scene v14s32_2e
    with dissolve

    imre "Sorry. Later man."

    scene v14s32_2d
    with dissolve

    u "Uh, bye."

    scene v14s32_5f # TPP. Show Imre leaving towards the gym door.
    with dissolve

    pause 0.75

    if v13_imre_disloyal:
        scene v14s32_5g # TPP. Same as v14s32_5e, Imre looks over his shoulder, Imre neutral face, mouth open.
        with dissolve

        imre "And just so you know, I'm having a really hard time not telling Chris about you and Nora."

        scene v14s32_5h # TPP. Same as v14s32_5g, Imre neutral face, mouth closed.
        with dissolve

        u "Imre-"

        scene v14s32_5g
        with dissolve

        imre "Part of me feels like you had a lot to do with the problems they've been having."

        scene v14s32_5h
        with dissolve

        u "I know what I did wasn't right, but I'm not involved in their relationship like that."

        scene v14s32_5g
        with dissolve

        imre "*Sighs* Whatever man."

    scene v14s32_5i # FPP. Same as v14s32_5h, Show Imre opening the door to leave the gym, Imre slight smile, mouth closed. 
    with dissolve

    pause 0.75 

    scene v14s32_5j # FPP. Same as v14s32_5i, Show Imre leaving the gym. 
    with dissolve

    pause 0.75

    scene v14s32_5e
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v14s33