# SCENE 4: MC talks to the roommate (Chole or Riley) about the robbery
# Location: Hotel room
# Characters: MC (Outfit 3), Riley (Outfit 2), Chloe (Outfit 1)
# Time: Night

label v12_roomate_talk:
    if not v11_riley_roomate:
        scene v12rcr1 # TPP. Show MC sitting at the front of his bed
        with fade 

        pause 0.75

        play music "music/v12/Track Scene 4.mp3" fadein 2

        scene v12rcr2 # FPP. Show chloe walking into the room, looking at MC, mouth closed
        with dissolve

        u "Where have you been?"

        scene v12rcr2a # FPP. Same as 2,smile on her face, mouth opened
        with dissolve

        cl "What, were you worried about me? *Chuckles*"

        menu:
            "Yes":
                $ reputation.add_point(Reputations.BOYFRIEND)
                scene v12rcr2
                with dissolve

                u "Yeah, kinda... It's not like we weren't just in the middle of a robbery or anything."

            "No":
                $ reputation.add_point(Reputations.BRO)
                scene v12rcr2
                with dissolve
                       
                u "Haha no, I was just curious. I know you can take care of yourself."

        if chloe.relationship >= Relationship.FWB:
            scene v12rcr3 # TPP. Chloe gives MC a kiss
            with dissolve

            play sound "sounds/kiss.mp3"

            pause 0.75

            scene v12rcr4 # TPP. Chloe sits on her bed 
            with dissolve

            pause 0.75
            
        else:
            scene v12rcr4
            with dissolve

            pause 0.75

            scene v12rcr5 # FPP. Chloe sitting on her bed, smiling mouth opened
            with dissolve

        cl "*Chuckles* I just wanted a drink to calm my nerves so I was down at the bar."

        scene v12rcr5a # FPP. Same as v12rcr5, mouth closed
        with dissolve

        u "Ahh, gotcha."

        scene v12rcr5
        with dissolve

        cl "Don't take this as me being mean or anything, but he was lucky he snagged Nora's bag. If he had taken a bag from Amber or Cameron... he wouldn't have made it far. *Chuckles*"

        scene v12rcr5a
        with dissolve

        u "What about me? You don't think I would've given him trouble?"

        scene v12rcr5
        with dissolve

        cl "*Chuckles* Not like Amber or Cameron."

        if v12_fight_win:
            scene v12rcr5a 
            with dissolve

            u "You know I chased down the guy, beat his ass and got her bag back... Right?"

            scene v12rcr5b # FPP. Same as v12rcr5, chloe has a suprised look
            with dissolve

            cl "WHAT?! No... I didn't know that! You actually did that?"

            scene v12rcr5a
            with dissolve

            u "Ha, yes. Where's my apology?"

            scene v12rcr5c # FPP. Same as v12rcr5b, has a teasing expression
            with dissolve

            cl "Hmm, maybe I was wrong... Sorry. Didn't know my roommate was the ultimate bodyguard."

        else:
            scene v12rcr5a
            with dissolve

            u "*Laughs* Don't doubt me just because you don't know what I'm capable of."

            scene v12rcr5c
            with dissolve

            cl "My bad, guess I need to see you fight up close..."

        scene v12rcr5a
        with dissolve

        u "Haha, so you were drinking by yourself?"

        scene v12rcr5d # FPP. Chloe looking at mc, mouth opened
        with dissolve

        cl "At first yeah, but then Ryan actually came to the bar and we talked for a little bit."

        scene v12rcr5a
        with dissolve

        u "About anything interesting?"

        scene v12rcr5d
        with dissolve

        cl "Mainly about him getting strong enough to take on Grayson."

        scene v12rcr5a
        with dissolve

        u "*Laughs* Good luck with that. Definitely don't see him being able to do that any time soon."

        scene v12rcr5d
        with dissolve

        cl "You don't think Ryan's a good fighter?"

        menu:
            "He is":
                $ reputation.add_point(Reputations.BRO)
                scene v12rcr5a
                with dissolve

                u "He is, I just don't think he's at Grayson level. You have to be a bit crazy to fight like him."

                scene v12rcr5d
                with dissolve

                cl "Well, he's definitely crazy."

                scene v12rcr5a
                with dissolve

                u "Not Grayson-level crazy. *Laughs*"

            "Nope":
                $ reputation.add_point(Reputations.TROUBLEMAKER)
                scene v12rcr5a
                with dissolve

                u "Not really... He may be motivated, but he's not good enough to take on someone like Grayson. Not yet, at least."

                scene v12rcr5d
                with dissolve

                cl "Come on, [name]. He's not that bad."

                scene v12rcr5a
                with dissolve

                u "Not that bad doesn't mean he's good. *Chuckles*"

        scene v12rcr5e # FPP. Chloe has a hiccup, with her hand covering her mouth
        with dissolve

        cl "*Hiccup* Oh my gosh, excuse me. *Chuckles* I'm so sorry."

        scene v12rcr5a
        with dissolve

        u "Drink too much?"

        scene v12rcr5
        with dissolve

        cl "Not enough, haha. I don't know why, but I've had the hiccups so much lately."
            
        scene v12rcr5e
        with dissolve

        cl "*Hiccup* They say hiccups are a sign that you're growing. I hope not."

        scene v12rcr5a
        with dissolve

        u "Maybe it means you're growing as a person. *Chuckles*"

        scene v12rcr5e
        with dissolve

        cl "*Hiccup* Haha, maybe."

        scene v12rcr5d
        with dissolve

        cl "Let's get to bed. If I don't go to sleep now, I won't get up in time to leave."

        scene v12rcr5a
        with dissolve

        u "Haha, same."

        if chloe.relationship >= Relationship.FWB:
            scene v12rcr6 # TPP. Chloe gets off her bed 
            with dissolve

            pause 0.75

            scene v12rcr7 # TPP. Chloe lays on MC's bed
            with dissolve

            pause 0.75

            scene v12rcr8 # FPP. Chloe now laying in MC's bed, mouth closed
            with dissolve

            u "Someone's looking real comfortable in my bed."

            scene v12rcr8a # FPP. Chloe smiling, mouth opened
            with dissolve

            cl "Our bed now, silly... Turn the light off so we can go to sleep. And hurry! I'm cold. *Chuckles*"

            scene v12rcr8
            with dissolve

            u "*Chuckles* (What is this girl doing to me?)"

            scene v12rcr9 # TPP. MC turns off the lights
            with dissolve
                
            pause 0.75

            scene v12rcr10 # TPP. MC cuddles with chloe and goes to sleep
            with dissolve

            pause 1.25

        else: 
            scene v12rcr5 
            with dissolve

            cl "Can you turn the light off, please? Thank you. *Chuckles*"

            scene v12rcr5a
            with dissolve

            u "*Chuckles*"

            scene v12rcr9 
            with dissolve

            pause 0.75

            scene v12rcr11 # TPP. MC lays in his bed and goes to sleep
            with dissolve

            pause 0.75

    else: 
        scene v12rcr1 
        with dissolve

        pause 0.75

        scene v12rcr12 # FPP. Show riley walking into the room, looking at MC, mouth closed
        with dissolve

        u "Where have you been?"

        scene v12rcr12a # FPP. Riley is now smiling, mouth opened
        with dissolve

        ri "*Chuckles* What are you, the hall monitor?"

        scene v12rcr12
        with dissolve

        u "What? *Chuckles* I was just curious where you went after everything that happened. I thought you were gonna be in the room."

        scene v12rcr12a
        with dissolve

        ri "I was out with Lindsey actually."

        scene v12rcr12
        with dissolve

        u "Oh, yeah? Where at?"

        scene v12rcr12a
        with dissolve

        ri "Someone sure has a lot of questions. *Chuckles* Were you wishing I was here with you or something?"

        menu:
            "A little":
                $ reputation.add_point(Reputations.BOYFRIEND)
                scene v12rcr12
                with dissolve

                u "A little bit, it is a lot nicer when you're around."

                scene v12rcr12b # FPP. Riley making a delightful expression, mouth opened
                with dissolve

                ri "Aww. I guess I can't be upset at you for missing me. *Chuckles*"

            "Not really":
                $ reputation.add_point(Reputations.BRO)
                scene v12rcr12 
                with dissolve

                u "Haha, not really. I was kinda enjoying the alone time. I just wanted to know what you were doing so I know how to keep you occupied the next time I wanna be alone."

                scene v12rcr12a
                with dissolve

                ri "Uhh, rude. *Chuckles*"

        scene v12rcr13 # FPP. Riley walks to her bed
        with dissolve

        pause 0.75

        scene v12rcr13a # FPP. Riley plops on her bed, mouth opened
        with dissolve

        ri "Ahh, so comfy."

        scene v12rcr13b # FPP. Same as v12rcr13, riley is now sideways on the bed looking at mc mouth closed
        with dissolve

        u "I thought you'd be a little more stressed out after what just happened."

        scene v12rcr13c # FPP. Same as v12rcr13b, mouth opened
        with dissolve

        ri "Why? It's not like I got robbed, that would've had me spooked for sure."

        if v12_fight_win: 
            scene v12rcr13c
            with dissolve

            ri "Plus, you handled him. If anything he's the one that should be stressed out."

        else:
            scene v12rcr13c 
            with dissolve

            ri "Nora got robbed so if anyone is stressed out, it's her."

        scene v12rcr13b
        with dissolve

        u "You aren't wrong."

        scene v12rcr13c
        with dissolve

        ri "So you wanna know what Lindsey and I were up to?"

        scene v12rcr13b
        with dissolve

        u "Haha, sounds like you do want me to know."

        scene v12rcr13d # FPP. Same as v12rcr13c, riley smiling
        with dissolve

        ri "Oh, whatever. *Chuckles* I told Lindsey I was on the fence about joining a sorority because my family was against it, but that I've been really considering it lately."
        ri "She asked me what I thought about the Chicks and I was honest. I think they have a lot of drama."

        scene v12rcr13b
        with dissolve

        u "So is there another one you're looking at?"

        scene v12rcr13c
        with dissolve

        ri "Well there was, but then Lindsey agreed that there was a lot of drama but promised me she was planning on running for President against Chloe."

        menu:
            "I know":
                $ reputation.add_point(Reputations.TROUBLEMAKER)
                scene v12rcr13b
                with dissolve

                u "Yeah, I actually know already. Her and I have actually talked about it a few times."

                scene v12rcr13e # FPP. same as v12rcr13d, Riley looking excited, mouth opened
                with dissolve

                ri "You should've told me! That's huge news."

                scene v12rcr13b
                with dissolve

                u "She wants it to be kept under wraps for now."

                scene v12rcr13d
                with dissolve

                ri "Well I'm glad you told me, because I didn't know that. *Chuckles*"

            "Really?":
                scene v12rcr13b
                with dissolve

                u "Oh, really?"

                scene v12rcr13c
                with dissolve

                ri "Yeah... She's got an entire campaign slogan and everything."

                scene v12rcr13b
                with dissolve

                u "Wow, that's some major news. I'm kinda nervous to see how all that plays out."

                scene v12rcr13c
                with dissolve

                ri "Me too. She didn't ask me to not tell anyone, but just in case we should probably keep it to ourselves."

                scene v12rcr13b
                with dissolve

                u "Of course, I'm not getting mixed up in any of that. *Chuckles*"

        scene v12rcr13c
        with dissolve

        ri "It sucks that we can't all hang out at night and do what we want you know? Like without Mr. Lee and Ms. Rose."

        scene v12rcr13b
        with dissolve

        u "What are you wanting to do?"

        scene v12rcr13c
        with dissolve

        ri "I don't know, like a little sleepover or something."

        scene v12rcr13b
        with dissolve

        u "(Everyone sleeping in the same room with no teachers around?) That does sound pretty fun."

        scene v12rcr13e
        with dissolve

        ri "Right? Maybe I'll talk to Aubrey about it. Maybe she and I could set something up in Paris."

        scene v12rcr13b
        with dissolve

        u "If anyone can make it happen, it's you guys. *Chuckles*"

        scene v12rcr13c
        with dissolve

        ri "You know what I'm about to make happen right now?"

        scene v12rcr13b
        with dissolve

        u "What?"

        scene v12rcr13c
        with dissolve

        ri "Sleep. Shut the light off and let me catch some Z's."

        scene v12rcr13b
        with dissolve

        u "Haha, goodnight loser."

        #scene v12rcr9
        #with dissolve

        #pause 0.75

        scene v12rcr11
        with fade

        pause 0.75

        scene black
        with fade
        pause 2.5

        stop music fadeout 3

    jump v12_morning_london #scene 5