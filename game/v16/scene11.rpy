# SCENE 11: Riley & Mc in Hallway
# Locations: SVC Hallways
# Characters: RILEY (Outfit: 3), MC (Outfit: 5), CHLOE (Outfit: 2)
# Time: Morning

init python:
    def v16s11_reply3():
        nora.messenger.newMessage("Perfect :)")

    def v16s11_reply4():
        nora.messenger.newMessage("Lmao, see u soon ")

label v16s11:
    scene v16s11_1 # TPP. Show MC walking the SVC hallways, MC slight smile, mouth closed.
    with fade

    pause 0.75

    scene v16s11_2 # TPP. Show Riley running up to MC from behind, MC slightly turning toward Riley, MC slight smile, mouth closed, Riley slight smile, mouth open.
    with vpunch

    ri "Hey, wait up."

    scene v16s11_1a # TPP. Show MC walking the SVC hallways with Riley, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v16s11_3 # FPP. Walking down the hallway, MC looking at Riley, Riley looking at MC, Riley slight smile, mouth closed.
    with dissolve

    u "Hey, Riley. How are you?"

    scene v16s11_3a # FPP. Walking down the hallway, MC looking at Riley, Riley looking at MC, Riley slight smile, mouth open.
    with dissolve

    ri "I'm good. Haven't gotten any more shit from Tom so far."

    scene v16s11_3
    with dissolve

    u "Glad to hear it."

    if not v16s1_win_fight_with_tom:
        scene v16s11_3a
        with dissolve

        ri "You look like you feel better too, ha."

        scene v16s11_3
        with dissolve

        u "Yeah, it's amazing what a good night's sleep will do."

        scene v16s11_3a
        with dissolve

        ri "Or maybe you're a superhuman."

        scene v16s11_3
        with dissolve

        u "Oh shit... You're right. What if I am?"

        scene v16s11_3a
        with dissolve

        ri "Wanna jump off the roof and test if you can fly?"

        scene v16s11_3
        with dissolve

        u "Hmm... Maybe later."

    else:
        scene v16s11_3a
        with dissolve

        ri "Thank you again. If you hadn't been there last night, I don't know where I'd be right now."

        scene v16s11_3
        with dissolve

        menu:
            "It was fun":
                $ add_point(KCT.TROUBLEMAKER)
                scene v16s11_3
                with dissolve

                u "Oh, it was fun actually."

                scene v16s11_3a
                with dissolve

                ri "Fun...? How was that fun?"

                scene v16s11_3
                with dissolve

                u "It was an absolute pleasure being able to beat him to a pulp."

                scene v16s11_3a
                with dissolve

                ri "*Sighs* Men and their violence..."
                
            "Don't think about it":
                $ add_point(KCT.BRO)
                scene v16s11_3
                with dissolve

                u "Don't even think about that. It didn't happen, and it's not gonna happen. Okay?"

                scene v16s11_3a
                with dissolve

                ri "Okay."

    # -Pinboard MUST include a sign up sheet for the newspaper. Dialogue that is used for it is "Looking for one to two more students to join the Newspaper squad". This does not need to be shown, we can be looking at riley while shes reading this line.
    # -Pinboard MUST include a notice about sex education week, and a note about how the nurse always has free condoms available to students in her office. MC reacts to this briefly.
    # -Pinboard MUST include chloe campaign poster, she reacts to it saying "its her bad side". We can use a photo that she's already posted for her campaign, or it can be new.

    scene v16s11_4 # TPP. MC and Riley walking up to a pinboard thats in the hallways somewhere, on the pinboard there is a sign up sheet for the newspaper on the paper it says "Looking for one to two more students to join the Newspaper squad!", a notice paper about sex education and that the school nurse provides free condoms to students, and  Chloe's presidential campaign poster.
    with dissolve

    pause 0.75

    scene v16s11_5 # FPP. MC looking at the pinboard. 
    with dissolve

    pause 0.75

    scene v16s11_6 # FPP. At the pinboard. MC looking at Riley, Riley looking at the Newspaper sign up sheet, Riley slight smile, mouth open.
    with dissolve

    ri "Oh, wait... Look at this."

    scene v16s11_7 # FPP. Close up of the note that the Nurse has free condoms.
    with dissolve

    u "What? Free condoms from the nurse? That's pretty common but, we can stop by if you-"

    scene v16s11_6a # FPP. At the pinboard. MC looking at Riley, Riley looking at the Newspaper sign up sheet, Mouth open.
    with dissolve

    ri "No, forget the condoms."

    scene v16s11_6b # FPP. At the pinboard, MC looking at Riley, Riley looking at the Newspaper sign up sheet, slight smile, mouth closed.
    with dissolve

    u "Oooh... Risky."

    if riley.relationship >= Relationship.LIKES: ###???
        scene v16s11_6c # FPP. At the pinboard, MC looking at Riley, Riley body facing the board, head turned toward MC, Riley laughing, mouth open.
        with dissolve

        ri "*Laughs* Are you done?"

        scene v16s11_6d # FPP. At the pinboard, MC looking at Riley, Riley body facing the board, head turned toward MC, Riley slight smile, mouth closed.
        with dissolve

        u "Yes. Finished. What are we looking at?"

    else:
        scene v16s11_6e # FPP. At the pinboard, MC looking at Riley, Riley body facing the board, head turned toward MC, Riley unamused slight glare, mouth closed.
        with dissolve

        u "*Clears throat* So, what are we looking at?"

    scene v16s11_6f # FPP. At the pinboard, MC looking at Riley, Riley body facing the board, left hand pointing at sign up sheet, head turned toward MC, Riley slight smile, mouth open.
    with dissolve

    ri "It's a sign-up sheet for the newspaper...?"

    scene v16s11_6b
    with dissolve

    u "I didn't know we had a newspaper..."

    scene v16s11_6f
    with dissolve

    ri "We didn't, haha. It's new."

    ri "Looks like Elijah's the Editor."

    scene v16s11_6b
    with dissolve

    u "Oh..."

    scene v16s11_6b
    with dissolve

    menu:
        "Be nice":
            $ add_point(KCT.BRO)
            scene v16s11_6b
            with dissolve

            u "Well, good for him. Maybe it could be cool."

            scene v16s11_6a
            with dissolve

            ri "Yeah, really cool."

        "Joke about Elijah":
            $ add_point(KCT.TROUBLEMAKER)
            scene v16s11_6b
            with dissolve

            u "Ew..."

            scene v16s11_6g # FPP. At the pinboard, MC looking at Riley, Riley body facing the board, head turned toward MC, Riley unamused slight glare, mouth open.
            with dissolve

            ri "Hey! Be nice."

    scene v16s11_6a
    with dissolve

    ri "\"Looking for one to two more students to join the Newspaper squad.\""

    scene v16s11_6b
    with dissolve

    u "Newspaper squad... *Snortles*"

    scene v16s11_6a
    with dissolve

    ri "*Giggles* Stop it!"

    scene v16s11_6b
    with dissolve

    u "I tried!"

    scene v16s11_6f
    with dissolve

    ri "I think I'm gonna do it."

    scene v16s11_6b
    with dissolve

    u "Wait, really?"

    scene v16s11_6f
    with dissolve

    ri "Yeah, why not? I could easily do some on-campus photography for it."

    ri "And honestly, it sounds kind of fun. Interviewing students and staff about important issues?"

    scene v16s11_6b
    with dissolve

    menu:
        "Support her":
            $ add_point(KCT.BRO)
            scene v16s11_6b
            with dissolve

            u "Ha, I agree. You should do it. Could be fun."

            scene v16s11_6f
            with dissolve

            ri "Right? Exactly!"

        "Elijah sucks though":
            $ add_point(KCT.TROUBLEMAKER)
            scene v16s11_6b
            with dissolve

            u "Elijah sucks though, Riley. Seriously."

            scene v16s11_6g
            with dissolve

            ri "[name]... *Sighs*"

            scene v16s11_6e
            with dissolve

            u "Okay, I tried to warn you. Just remember this moment."

            scene v16s11_6h # FPP. At the pinboard, MC looking at Riley, Riley body facing the board, head turned toward MC, Riley rolling her eyes, mouth closed.
            with dissolve

            pause 0.75

    scene v16s11_6i # FPP. At the pinboard, MC looking at Riley, Riley leaning over, using a PEN to sign her name, slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v16s11_6j # FPP. At the pinboard, MC looking at Riley, Riley looking at MC, handing PEN toward MC, Riley slight smile, mouth open.
    with dissolve

    ri "You should sign up too, you know. Even if it doesn't work out, it's a good experience to learn from."

    scene v16s11_6k # FPP. At the pinboard, MC looking at Riley, Riley looking at MC, MC reaching for the PEN, Riley slight smile, mouth closed.
    with dissolve

    u "Hmm... (She's not wrong though... It would look good on a resume if I took part in a student club.)"

    scene v16s11_8 # FPP. At the pinboard, MC at the sign up sheet, holding the PEN in his hand.
    with dissolve

    menu:
        "Sign up":
            $ v16s11_sign_up = True

            u "I hope I don't regret this."

            ri "Haha, come on! This will be so fun."

            scene v16s11_9 # TPP. Angle from behind showing Riley looking at MC, MC leaning over to sign the sheet, MC's face not seen, Riley slight smile, mouth open.
            with dissolve

            ri "Me, you, and Elijah. The three-"

            scene v16s11_9a # TPP. Angle from behind showing Riley looking at MC, MC leaning over to sign the sheet, MC's face not seen, Riley slight smile, mouth closed.
            with dissolve

            u "Stop it."

            scene v16s11_9
            with dissolve

            ri "*Laughs*"

        "Don't sign up":
            scene v16s11_8
            #with dissolve

            u "Nah, I'm good. Besides, I don't stand a chance against your creative eye and... superior intellect."

            ri "Haha, right. Whatever you say."

    scene v16s11_10 # TPP. Show Chloe walking up to MC and Riley, all slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v16s11_11 # FPP. At the pinboard, MC looking at Chloe, Chloe looking at MC, Chloe slight smile, mouth closed.
    with dissolve

    cl "Hey guys!"

    if chloe.relationship >= Relationship.GIRLFRIEND: 
        play sound "sounds/kiss.mp3"

        scene v16s11_11a # TPP. At the pinboard, MC looking at Chloe, Chloe leaning forward and kissing MC on the cheek.
        with dissolve

        pause 0.75

        if riley.relationship >= Relationship.LIKES: ###???
            scene v16s11_12 # TPP. Close up of Riley facing MC and Chloe but her she looks away from seeing MC and Chloe kiss.
            with dissolve

            pause 0.75

    scene v16s11_10a # TPP. Show Chloe standing with MC and Riley at the pinboard.
    with dissolve

    pause 0.75

    scene v16s11_11b # FPP. At the pinboard, MC looking at Chloe, Chloe looking at her campaign poster on the pinboard, Chloe neutral face, mouth open.
    with dissolve

    cl "Oh, are we checking out my campaign poster?"

    scene v16s11_6l # FPP. At the pinboard, MC looking at Riley, Riley looking past MC at Chloe, Riley slight smile, mouth open.
    with dissolve

    ri "We were actually-"

    scene v16s11_11b
    with dissolve

    cl "I'm not sure if I like it. Think that's my bad side."

    scene v16s11_6l
    with dissolve

    ri "Your bad side? Chloe, you don't have a bad side, haha."

    scene v16s11_11b
    with dissolve

    cl "Yes, I do! We all do. Maybe I'll just have Imre take them down."

    scene v16s11_6m # FPP. At the pinboard, MC looking at Riley, Riley looking at MC, Riley confused, mouth open 
    with dissolve

    ri "I think that's a bit extreme. [name]? Tell her."

    scene v16s11_11c # FPP. At the pinboard, MC looking at Chloe, Chloe looking at her campaign poster, Chloe neutral face, mouth closed.
    with dissolve

    menu:
        "You look great":
            $ add_point(KCT.BOYFRIEND)
            scene v16s11_11d # FPP. At the pinboard, MC looking at Chloe, Chloe looking at MC, Chloe slight smile, mouth closed.
            with dissolve

            u "Chloe, don't overthink it. You look great in every photo."

        "Not your best photo":
            $ add_point(KCT.TROUBLEMAKER)

            scene v16s11_11e # FPP. At the pinboard, MC looking at Chloe, Chloe looking at MC, Chloe neutral face, mouth closed.
            with dissolve

            u "I mean, it's not your best photo..."

            scene v16s11_11f # FPP. At the pinboard, MC looking at Chloe, Chloe looking at MC, Chloe slight smile, mouth open.
            with dissolve

            cl "See? Thank you for being honest."

            scene v16s11_6m
            with dissolve

            ri "What?! Ugh, no. No, no, no. Stop this."

            scene v16s11_6l
            with dissolve

            ri "You're not taking them down, you look fine."

    scene v16s11_11f
    with dissolve

    cl "Hmm, fine. The more of me that people see, the better, I guess."

    scene v16s11_6l
    with dissolve

    ri "Right... Oh- Look at the time! I've gotta go do some... work on the... Assignment."

    ri "Catch you guys later!"

    scene v16s11_10b # TPP. Show Riley walking away but looking back at MC and Chloe, slight smile, mouth closed, MC slight smile, mouth open, Chloe slight smile, mouth closed.
    with dissolve

    u "Ha, okay. Bye, Red."

    scene v16s11_11d
    with dissolve

    u "(I think Riley's over the Chicks at the moment.)"

# -if Announcement, and Chloe and Lindsey went to Mr. Lee's office
    if v15_lindsey_recording > 0: ### VERIFY This gets us annoucenment (and I think that will flow to Mr. Lee's office, otherwise we can add sceen8 to sceneList and check for that)
        scene v16s11_11d
        with dissolve

        u "So, how did it go with Mr. Lee?"

        scene v16s11_11f
        with dissolve

        cl "Oh... *Sighs* I don't even want to talk about it."

        scene v16s11_11d
        with dissolve

        u "Oh, that's okay. We don't have to-"

        scene v16s11_11f
        with dissolve

        cl "He takes us into his office and makes us look each other in the eye while we apologize."

        scene v16s11_11d
        with dissolve

        u "Oh-"

        scene v16s11_11f
        with dissolve

        cl "Then, after a few moral lectures about patience and gratitude and whatever the fuck else..."

        cl "He tells us both that if he doesn't see improvement in our attitudes, we have to come to his office once a week and tend to his bonsai trees."

        scene v16s11_11d
        with dissolve

        u "Wait...Seriously?"

        scene v16s11_11f
        with dissolve

        cl "Yeah. Bonsai trees are all about patience and discipline, [name]. Didn't you know that? *Chuckles*"

        scene v16s11_11d
        with dissolve

        u "Ha, wow. So, Mr. Lee's bonsai tree behavioral therapy sessions have officially begun, huh?"

        scene v16s11_11f
        with dissolve

        cl "Apparently."

        if not v13_perfume:
            scene v16s11_11f
            with dissolve

            cl "Thanks to you of course. That wonderful gift of yours gave him some terrific ideas."

            scene v16s11_11d
            with dissolve

            u "*Laughs* You're welcome."

        scene v16s11_11d
        with dissolve

        u "(So much for not wanting to talk about it.)"

    scene v16s11_11d
    with dissolve

    u "We were actually looking at the newspaper sign-up sheet, Riley and I."

    scene v16s11_11f
    with dissolve

    cl "Oh, really? Wait..."

    scene v16s11_13 # TPP. Close up of Chloe looking at the newspaper sheet, slight smile, mouth open.
    with dissolve

    cl "They're starting a newspaper for the school? Cool!"

    scene v16s11_11d
    with dissolve

    u "Yeah, I think Riley might-"

    scene v16s11_11f
    with dissolve

    cl "That's such a good idea! I could use this for my campaign!"

    if v14_help_chloe:
        scene v16s11_11f
        with dissolve

        cl "Come on. Let's go plan phase three, now!"

        scene v16s11_14 # TPP. Chloe leading MC by his arm along the hallway 
        with dissolve

        u "(Sure. Of course. I'd love to...)"

        play sound "sounds/vibrate.mp3"

        scene v16s11_15 # TPP. Chloe leading MC by his arm further down the hallway 
        with dissolve

        pause 0.75

        scene v16s11_16 # TPP. MC pulling his phone out of his pocket, [don't show Chloe so can be reused], slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v16s11_16a # TPP. MC looking at his phone, [don't show Chloe so can be reused], slight smile, mouth closed.
        with dissolve
        
        pause 0.75
        
        ### check queue
        
        $ nora.messenger.newMessage("Hey, it's too nice out to be inside all day. Come join me at the park for yoga?")
        $ nora.messenger.addReply("I do need a good stretch... lol. Got a few things left to do on campus, but I'll be there ASAP.")
        $ nora.messenger.newMessage("Perfect :)")
        $ nora.messenger.addReply("Sigh... If I have to... ;) Be there as soon as I finish up on campus.")
        $ nora.messenger.newMessage("Haha, sounds good.")

        label v16s11_phoneContinue:
            if nora.messenger.replies:
                call screen phone
            if nora.messenger.replies:
                u "(I should reply to Nora.)"
                jump v16s11_phoneContinue

        scene v16s11_17 # TPP. Chloe continues to pull MC by his arm even further, both slight smile, mouth closed.
        with dissolve

        pause 0.75

        jump v16s12

    else:
        scene v16s11_11f
        with dissolve

        cl "Sorry, [name]. But I just got the smartest idea, and I have to act now. Thank you!"

        scene v16s11_11d
        with dissolve

        u "Oh-"

        play sound "sounds/vibrate.mp3"

        scene v16s11_10c # TPP. Show Chloe walking away from MC, leaving MC the last at the pinboard, both slight smile, mouth closed.
        with dissolve

        u "(You're welcome?)"

        scene v16s11_16
        with dissolve

        pause 0.75
        
        scene v16s11_16a
        with dissolve

        pause 0.75

        $ nora.messenger.newMessage("Hey, It's such a nice day, it's too nice out to be inside all day. Come join me at the park for yoga?")
        $ nora.messenger.addReply("I do need a good stretch... lol. OMW", v16s11_reply3)
        $ nora.messenger.addReply("Sigh... If I have to... ;)", v16s11_reply4)

        label v16s11_phoneContinue2:
            if nora.messenger.replies:
                call screen phone
            if nora.messenger.replies:
                u "(I should reply to Nora.)"
                jump v16s11_phoneContinue2

        scene v16s11_18 # TPP. Show MC walking down the hallways towards the park, slight smile, mouth closed.
        with dissolve

        pause 0.75

        jump v16s13