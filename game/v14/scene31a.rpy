# SCENE 31a: Talk to Cameron about forming a strategic alliance
# Locations: Apes' house exterior
# Characters: MC (Outfit: 2), CAMERON (Outfit: 2), CHLOE (Outfit: 1)
# Time: Wednesday evening

label v14s31a:
    scene v14s31a_1 # TPP Show MC arriving at Apes' house # -MC arrives at the Apes house and Cameron is outside working out-
    with fade

    pause 0.75

    play music "music/v13/Track Scene 46_1.mp3" fadein 2

    scene v14s31a_2 # FPP Show Cameron working out outside of Apes' house
    with dissolve

    pause 0.75

    scene v14s31a_3 # FPP Show Cameron working out, conversation distance now. Cameron looks focused, not looking at MC
    with dissolve

    u "Putting in a set instead of enjoying the party?"

    scene v14s31a_3a # FPP Same angle as 3, Cameron now looking at MC, smiling with mouth open
    with dissolve

    ca "Can't be walking around looking like a little bitch boy. Too much partying does that to you, you know."

    scene v14s31a_3b # FPP Same as 3a, Cameron's mouth closed
    with dissolve

    u "Couldn't have said it better myself."

    scene v14s31a_3a
    with dissolve

    ca "You need to work out too, you look like a fucking fifth grader."

    scene v14s31a_3c # FPP Same angle as 3, Cameron laughing with his eyes closed
    with dissolve

    ca "Ah! Couldn't have said that better myself."

    scene v14s31a_3b
    with dissolve

    u "Ha! Alright..."

    # MIGHT NEED TO ADJUST TIMING OF THESE NEXT SCENES - PUSHUPS AND SITUPS
    # -MC drops down and bust out five pushups-
    scene v14s31a_4 # TPP Show MC on the ground on his chest in a lower pushup position
    with dissolve

    pause 0.75

    scene v14s31a_4a # Same angle as 4, MC arms extended in upper pushup position # up 1
    with dissolve

    pause 0.75

    scene v14s31a_4
    with dissolve

    pause 0.75

    scene v14s31a_4a # up 2
    with dissolve

    pause 0.75

    scene v14s31a_4
    with dissolve

    pause 0.75

    scene v14s31a_4a # up 3
    with dissolve

    pause 0.75

    scene v14s31a_4
    with dissolve

    pause 0.75

    scene v14s31a_4a # up 4
    with dissolve

    pause 0.75

    scene v14s31a_4
    with dissolve

    pause 0.75

    # jumps to his feet at 5
    scene v14s31a_4b # TPP Same angle as 4, show MC jumping to his feet between his hands, which are flat on the ground
    with dissolve

    pause 0.5

    scene v14s31a_3d # FPP Same angle as 3, Cameron looking at MC with neutral expression, mouth open
    with dissolve

    ca "Okay, good form. I'll give you that. How are your sit ups?"

    # -MC does a few sit ups-
    scene v14s31a_4c # TPP Same angle as 4, MC laying on the ground in lower situp position, knees bent, feet flat, arms over chest
    with dissolve

    pause 0.75

    scene v14s31a_4d # TPP Same angle as 4, MC in upper situp position, arms crossed over chest, elbows touching knees # up 1
    with dissolve

    pause 0.75

    scene v14s31a_4c
    with dissolve

    pause 0.75

    scene v14s31a_4d # up 2
    with dissolve

    pause 0.75

    scene v14s31a_4c
    with dissolve

    pause 0.75

    scene v14s31a_4d # up 3
    with dissolve

    pause 0.75

    scene v14s31a_4e # TPP Same angle as 4, MC getting up from the ground to his feet
    with dissolve

    pause 0.5

    scene v14s31a_3d
    with dissolve

    ca "Acceptable, but you shouldn't be lying all the way down, resting every new rep."

    scene v14s31a_3e # FPP Same as 3d, Cameron's mouth closed
    with dissolve

    u "Got it, coach."

    scene v14s31a_3d
    with dissolve

    ca "Alright, stop the bullshit and say what you need to say."

    scene v14s31a_3e
    with dissolve

    u "Huh?"

    scene v14s31a_3d
    with dissolve

    ca "I'm pretty slow, [name], but I'm not stupid. You've never come to work out with me before."

    if joinwolves: # -If Wolves (extra dialog)
        scene v14s31a_3f # FPP Same angle as 3, Cameron looks annoyed, mouth open
        with dissolve

        ca "On top of that, you're a fucking wolf. So what is it?"

    # -Continue regardless of frat
    scene v14s31a_3e
    with dissolve

    u "Damn, okay... I mean, shit..."

    menu:

        "Butter him up":
            $ add_point(KCT.BOYFRIEND)
            u "I did have something I wanted to talk to you about, but I was enjoying our bonding experience."

            scene v14s31a_3f
            with dissolve

            ca "I take working out too seriously for anyone to enjoy working out with me. Let alone call it a \"bonding experience.\""

            scene v14s31a_3e
            with dissolve

            u "Ta-fucking-da! Here I am."

            u "Maybe if you didn't assume that no one enjoyed you, you'd find out that they actually do."

            scene v14s31a_3f
            with dissolve

            ca "Yeah, yeah."

            scene v14s31a_3d
            with dissolve

            ca "What do you want?"

            scene v14s31a_3e
            with dissolve

        "Cut to the chase":
            $ add_point(KCT.BRO)

    u "I wanna talk to you about what everyone is talking about."

    scene v14s31a_3d
    with dissolve

    ca "What is everyone talking about?"

    scene v14s31a_3e
    with dissolve

    u "The Chicks race?"

    scene v14s31a_3d
    with dissolve

    ca "*Scoffs* I couldn't care less about that, man."

    scene v14s31a_3e
    with dissolve

    u "Really?"

    scene v14s31a_3d
    with dissolve

    ca "Yes, really."

    scene v14s31a_3e
    with dissolve

    u "Well, sorry to tell you this but..."

    scene v14s31a_3f
    with dissolve

    ca "But what?"

    scene v14s31a_5 # FPP Show Chloe walking up, looking at Cameron, smiling with mouth open
    with dissolve

    cl "Hey, you two."

    scene v14s31a_3g # FPP Same angle as 3, Cameron looking at Chloe, annoyed expression, mouth open
    with dissolve

    ca "Ahh shit... Look, I don't have time for this. This is not what I came out here for."

    scene v14s31a_5a # FPP Same angle as 5, Chloe closer now, looking at Cameron, smiling with mouth open
    with dissolve

    cl "Yeah, you're out here because they're being annoying in there. You're welcome. I wanted to talk."

    scene v14s31a_3e
    with dissolve

    u "Cameron, look, just hear us out. Can you do that?"

    scene v14s31a_3h # FPP Same angle as 3, Cameron looking down, as if thinking, neutral expression, mouth closed
    with dissolve

    ca "..."

    scene v14s31a_5b # FPP Same angle as 5, Chloe looking at Cameron with a pleading expression, mouth open
    with dissolve

    cl "Please?"

    scene v14s31a_3i # FPP Same angle as 3, Cameron looking at Chloe with neutral expression, mouth open
    with dissolve

    ca "What is it?"

    scene v14s31a_3f
    with dissolve

    ca "And keep it simple for fucks sake. Explain it to me like I'm five."

    scene v14s31a_3e
    with dissolve

    u "Of course."

    scene v14s31a_3h
    with dissolve

    u "We want the Apes to form an alliance with Chloe, making The Chicks the sister frat of the Apes."

    scene v14s31a_3d
    with dissolve

    ca "Why would I care about that?"

    scene v14s31a_3e
    with dissolve

    menu:
        "So Lindsey doesn't win":
            $ add_point(KCT.BOYFRIEND)
            u "Duh, so Lindsey doesn't win."

            scene v14s31a_3a
            with dissolve

            ca "I ain't got shit against her, haha. Why would I care who wins?"

            scene v14s31a_5b
            with dissolve

            cl "Because you know me, Cam."

            scene v14s31a_3i
            with dissolve

            ca "And I know her too. You're basically one in the same."

            scene v14s31a_5c # FPP Same angle as 5, Chloe looking annoyed and rolling her eyes, mouth open
            with dissolve

            cl "*Scoffs*"

            scene v14s31a_5d # FPP Same angle as 5, Chloe looking at MC, annoyed expression and mouth closed
            with dissolve

            u "Chloe..."

            scene v14s31a_3f
            with dissolve

            ca "Try again."

        "To strengthen the Apes":
            $ add_point(KCT.BRO)
            u "To strengthen the Apes."

            scene v14s31a_3d
            with dissolve

            ca "How would an alliance with a bunch of chicks strengthen us?"

            scene v14s31a_3e
            with dissolve

            u "You may be slow, but you aren't stupid, right?"

            scene v14s31a_3d
            with dissolve

            ca "Right."

            scene v14s31a_3e
            with dissolve

            u "So think about it, the most popular sorority matched with the Apes. It makes the Apes look damn good and leaves the Wolves looking completely alone."

            scene v14s31a_3j # FPP Same angle as 3, Cameron looking at MC, curious expression with eyebrow raised, mouth closed
            with dissolve

            u "They can't throw a good party after an alliance like that has been made."

            scene v14s31a_3h
            with dissolve

            ca "Hmm..."

            scene v14s31a_5e # FPP Same angle as 5, Chloe looking at Cameron, neutral expression, mouth open
            with dissolve

            cl "Don't think too hard, this is a favor for you and the Apes just as much as it's a favor for me."

            scene v14s31a_5a
            with dissolve

            cl "That's why it's called an alliance."

            scene v14s31a_3i
            with dissolve

            ca "Good point..."

    # -Continue regardless of choice
    scene v14s31a_3e
    with dissolve

    ca "You already got a shit ton of beef with Grayson. How would an alliance work if the President doesn't even fuck with you like that?"

    scene v14s31a_3d
    with dissolve

    u "That's why we came to you, you're someone he does listen to."

    scene v14s31a_3j
    with dissolve

    u "Grayson doesn't have many people he'll take advice from, but you're one of those people."

    scene v14s31a_3d
    with dissolve

    ca "Fair enough, so what exactly are you wanting me to do?"

    scene v14s31a_3e
    with dissolve

    menu:
        "Say Chloe is the hotter chick":
            $ add_point(KCT.BRO)
            u "Tell everyone Chloe is the hotter chick and that the hottest chick should be the Chicks President."

            scene v14s31a_3a
            with dissolve

            ca "Yeah... Again, that means nothing to me."

        "Collaboration":
            $ add_point(KCT.BOYFRIEND)
            u "I don't know exactly, we haven't decided just yet."

            u "Maybe just some sort of collaborative post on Kiwii would get the ball rolling and make people start talking."

            scene v14s31a_3d
            with dissolve

            ca "And how do you suggest that I convince Grayson?"

            scene v14s31a_5e
            with dissolve

            cl "No different than you would for anything else, just tell him what's best for the Apes... Be honest."

    # -Continue regardless of choice
    scene v14s31a_3k # FPP Same as 3h, Cameron's mouth open
    with dissolve

    ca "I hear what you guys are saying and I get what you're trying to do, but I'm not sold on anything just yet."

    scene v14s31a_6 # FPP Show Chloe looking closely into Cameron's eyes, Chloe smiling with mouth open, Cameron neutral expression with mouth closed
    with dissolve

    cl "Cameron."

    scene v14s31a_6a # FPP Same as 6, both mouths closed
    with dissolve

    u "(Here come the voodoo eyes...)"

    scene v14s31a_6
    with dissolve

    cl "We never talk much but we do know each other very well."

    cl "I know you well enough to know exactly what your aspirations are and so all I'll say is this..."

    scene v14s31a_6b # FPP Same angle as 6, Chloe with neutral expression and mouth open, Cameron's mouth closed
    with dissolve

    cl "If you back me in my campaign, I'll back you in any race you plan to take on. And I mean any."

    scene v14s31a_6c # FPP Same angle as 6, Cameron has taken a step back and looks shocked, mouth open. Chloe's mouth closed
    with dissolve

    ca "How did you know I wanted to run for President?"

    scene v14s31a_5e
    with dissolve

    cl "Your actions say it all. You're a natural leader."

    scene v14s31a_3k
    with dissolve

    ca "*Sighs*"

    scene v14s31a_3e
    with dissolve

    u "She's not wrong."

    scene v14s31a_7 # FPP Show Cameron looking up at the Apes' house with a thoughtful expression, mouth closed
    with dissolve

    pause 1

    scene v14s31a_3i
    with dissolve

    $ set_presidency_percent(v14_lindsey_popularity - 1)
    ca "Fine. I'll talk to Grayson."

    scene v14s31a_5f # FPP Same angle as 5, Chloe looking at Cameron, she looks very excited, like she's bouncing, mouth open
    with dissolve

    cl "Thank you! *Squeals* Thank you so much, Cameron."

    scene v14s31a_3l # FPP Same angle as 3, Cameron looking at Chloe, smiling with mouth open
    with dissolve

    ca "Yep."

    scene v14s31a_5a
    with dissolve

    cl "I'm off to talk to a few more people. Thanks for the nice chat! I appreciate it."

    scene v14s31a_5g # FPP Same angle as 5, Chloe looking at MC, smiling with mouth closed
    with dissolve

    u "See you-"

    scene v14s31a_8 # FPP Show Chloe walking away into the Apes' house
    with dissolve

    pause 0.75

    scene v14s31a_3m # FPP Same angle as 3, Cameron watching Chloe walk away, neutral expression, mouth closed
    with dissolve

    u "Ha... So?"

    scene v14s31a_3e
    with dissolve

    u "President, huh?"

    if joinwolves: # -If Wolves
        scene v14s31a_3f
        with dissolve

        ca "That's Ape business only."

        scene v14s31a_3e
        with dissolve

        u "Haha, okay."

        scene v14s31a_9 # TPP Show MC turning to walk away
        with dissolve

        ca "You think everything she said was true?"

        scene v14s31a_3j
        with dissolve

        u "Hm?"

        scene v14s31a_3d
        with dissolve

        ca "Or do you think she just knows exactly what to say, to get you on board?"

        scene v14s31a_3e
        with dissolve

        u "(He's talking about Chloe...)"

        menu:
            "She means what she says":
                $ add_point(KCT.BOYFRIEND)
                u "She means every word that she says. She wouldn't say it to you if she didn't believe it, or mean it."

                scene v14s31a_3a
                with dissolve

                ca "Ha... Alright."

            "She says what she needs to": # -If She says what she needs to (creates cameron Bro for Wolves)
                $ add_point(KCT.BRO)
                $ cameron.relationship = Relationship.BRO
                u "She knows what she needs to say. She's damn good at it too."

                scene v14s31a_3c
                with dissolve

                ca "Ha."

                scene v14s31a_3a
                with dissolve

                ca "You catch on quick."

                scene v14s31a_3b
                with dissolve

                u "Do I? *Chuckles*"

        # -continue regardless of choice-
        scene v14s31a_3j # -Cameron looks at MC like he knows something that MC doesn't but wants to protect him from it -
        with dissolve

        ca "..."

        scene v14s31a_3d
        with dissolve

        ca "I'll see you later, man."

        scene v14s31a_3e
        with dissolve

        u "Yeah, see ya."

    else: # -If Apes
        scene v14s31a_3d
        with dissolve

        ca "Yeah, so what?"

        scene v14s31a_3e
        with dissolve

        u "Nothing, and it's not surprising. Your whole attitude screams Apes."

        scene v14s31a_3a
        with dissolve

        ca "I'm glad you think so. I guess I should take running more seriously then?"

        scene v14s31a_3b
        with dissolve

        u "You should, yeah."

        scene v14s31a_3a
        with dissolve

        ca "I'm gonna go make a call."

        scene v14s31a_3b
        with dissolve

        u "Haha, you do that."

        if cameron.relationship.value >= Relationship.BRO.value:
            scene v14s31a_3a
            with dissolve

            ca "And just so you know, helping Chloe wasn't even a question."

            ca "You've been there for Sam so obviously you have good judgement. If you think Chloe is what's best for us as Apes, then I'm on board."

            scene v14s31a_3b
            with dissolve

            u "Thanks Cam."

            scene v14s31a_3a
            with dissolve

            ca "You bet."

        # -Continue regardless of BrotherCameron
        scene v14s31a_10 # FPP Show Cameron turning to walk away toward the Apes' house
        with dissolve

        u "(President Cam... *Laughs* I can't even begin to imagine how Grayson would react to that.)"

    scene v14s31a_9
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v14s33