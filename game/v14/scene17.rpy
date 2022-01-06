# SCENE 17: Ms Rose Economics Class
# Locations: Economics Class
# Characters: MC (Outfit: 9), MS. ROSE (Outfit: 1), LAUREN (Outfit: 1)
# Time: Morning

label v14s17:
    play music "music/v12/Track Scene 26.mp3" fadein 2

    scene v14s17_1 # TPP. Show MC walking into class, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v14s17_2 # FPP. MC looking around at the class seeing people partnered up together, all slight smile, mouth closed
    with dissolve

    u "(Umm, this is different...)"

    scene v14s17_3 # TPP. Show MC up against wall, slight smile, mouth closed, Ms. Rose walking in beside him, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v14s17_4 # FPP. Ms. Rose looking at MC, slight smile, mouth open
    with dissolve

    ro "Hey [name], I'm sensing that you're a bit confused about the look of the classroom."

    scene v14s17_4a # FPP. Same as v14s17_4, mouth closed
    with dissolve

    u "Haha, yeah a bit. I don't think we've ever worked in groups before."

    scene v14s17_4
    with dissolve

    ro "You're right, we haven't, but because of the trip I wanted to give those of you who went a chance to catch up on the curriculum."

    scene v14s17_4b # FPP. Same as v14s17_4, different posture
    with dissolve

    ro "I had the TAs take notes for you all while we were gone. So, you and your partner will go over them together."

    scene v14s17_4a
    with dissolve

    u "Sounds good to me. Who am I working with?"

    scene v14s17_4c # FPP. Same as v14s17_4, slight laughing expression
    with dissolve

    ro "You're gonna be with Lauren today. I thought I'd pair my brightest student with the class clown."

    scene v14s17_4a
    with dissolve

    u "That's pretty messed up to call Lauren the class clown behind her back..."

    if ms_rose.relationship.value >= Relationship.FWB.value and joinwolves: #sanitizing pathbuilder input
        scene v14s17_4c
        with dissolve

        ro "*Laughs* And you continue to find new ways to make me laugh..."

        scene v14s17_4a
        with dissolve

        u "I'll always find new ways to-"

        scene v14s17_5 # TPP. Show Ms. Rose slapping MC on his ass with her hand, Ms. Rose slight smile, mouth closed, MC, slight surprised expression, mouth closed
        with hpunch

        pause 0.75

        scene v14s17_4d # FPP. Same as v14s17_4a, Smirking expression
        with dissolve

        u "Ow! What the hell-"

        scene v14s17_4
        with dissolve

        ro "Chop, chop! Your partner is waiting on you."

        scene v14s17_4a
        with dissolve

        u "Yes, ma'am..."

        scene v14s17_4c
        with dissolve

        ro "*Chuckles*"

        scene v14s17_6 # TPP. Show MC walking away towards his seat, slight smile, mouth closed, Ms. Rose in the background, slight smile, mouth closed
        with dissolve

        u "(Hot damn... I like when she does that sneaky shit, haha.)"

        scene v14s17_7 # TPP. MC Now sitting beside lauren, both looking at eachother, both slight smile, mouths closed
        with dissolve

        pause 0.75

    else:
        scene v14s17_4c
        with dissolve
        
        ro "*Laughs* See? My point exactly. Now, off you go. She's waiting for you."

        scene v14s17_4a
        with dissolve

        u "Yes, ma'am."

        scene v14s17_6
        with dissolve

        pause 0.75

        scene v14s17_7 
        with dissolve

        pause 0.75
    
    if lauren.relationship.value >= Relationship.GIRLFRIEND.value:
        scene v14s17_7a # TPP. Same as v14s17_7, Show MC and Lauren kissing
        with dissolve

        play sound "sounds/kiss.mp3"

        pause 1.5 

        scene v14s17_8 # FPP. Lauren looking at MC, slight smile, mouth open 
        with dissolve
    
        la "Hey, you." 

    scene v14s17_8a # FPP. Same as v14s17_8, mouth closed
    with dissolve

    u "If I know you as much as I think I do, you've already read through the notes and you were keeping up with the curriculum while we were in Europe?"

    scene v14s17_8b # FPP. Same as v14s17_8, slightly surprised expression
    with dissolve

    la "Wow..."

    scene v14s17_8
    with dissolve

    la "I don't know if I should be offended that you think my life revolves only around my education..."
    la "...or flattered because that just means you consider me responsible..."

    menu:
        "Joke":
            $ add_point(KCT.BRO)
            scene v14s17_8a
            with dissolve

            u "So, I was right then? Nothing else to do with your life? *Laughs*"

            scene v14s17_8c # FPP. Same as v14s17_8, slight laughing expression
            with dissolve

            la "*Laughs* You're not funny, [name]."

            scene v14s17_8a
            with dissolve

            u "Really? I think you're laughing..."

            scene v14s17_8c
            with dissolve

            la "Okay, okay... Fair enough."

        "Compliment":
            $ add_point(KCT.BOYFRIEND)
            scene v14s17_8a
            with dissolve

            u "Responsible would be an understatement. I've never seen you focus on anything other than your future..."

            scene v14s17_8
            with dissolve

            la "That's very kind of you, actually. Thanks."

            scene v14s17_8a
            with dissolve

            u "Ha... Just stating facts."

            u "And might also be trying to tell you that you should get out more, in the most subtle way possible of course..."

            scene v14s17_8c
            with dissolve

            la "Haha! I knew the compliment was too good to be true."

            scene v14s17_8a
            with dissolve

            u "*Chuckles*"

    if lauren.relationship.value > Relationship.GIRLFRIEND.value or not "v11_aubrey" in sceneList: #correction for saves where this variable was defaulting to True - which can't be the case if v11_aubreysex is False, or if lauren rs is still True
        $ v11_lauren_caught_aubrey = False

    if v11_lauren_caught_aubrey or toldlauren or laurentoofar:
        scene v14s17_8d # FPP. Same as v14s17_8, neutral expression
        with dissolve
        
        la "*Sighs*"

        scene v14s17_8e # FPP. Same as v14s17_8d, mouth closed
        with dissolve

        u "What is it?"

        scene v14s17_8d
        with dissolve

        la "I just..."

        scene v14s17_8f # FPP. Same as v14s17_8d, slightly annoyed expression
        with dissolve

        la "I really wish you hadn't done the things that you did... You know?"

        scene v14s17_8
        with dissolve

        la "We have so much in common, and I genuinely do think you're an amazing guy. It's just..."

        scene v14s17_8g # FPP. Same as v14s17_8f, different posture 
        with dissolve

        la "When you mess up, [name], you mess up in such horrible ways."

        scene v14s17_8e
        with dissolve

        u "Lauren, I..."

        u "I'm extremely sorry about all and any of the mistakes I've made, I really am."

        scene v14s17_8d
        with dissolve

        la "Yeah..."

        la "I've moved on from it regardless though... So..."

        scene v14s17_8e
        with dissolve

        u "(Yeah, sure as hell sounds like it...)"

    scene v14s17_8
    with dissolve

    la "Alright then, let's get to work."

    scene v14s17_8a
    with dissolve

    u "Yes, let's."

    scene v14s17_9 # TPP. Show MC looking at his book, slight smile, mouth closed, Lauren turning the page of her text book, slight smile, mouth closed 
    with dissolve

    pause 0.75

    scene v14s17_9a # TPP. Same as v14s17_9, MC in the proccess of turning his page in his textbook, Lauren now looking at some note paper
    with dissolve

    pause 0.75
    
    scene v14s17_10 # FPP. MC looking at Lauren, Lauren looking at her notes, slight smile, mouth slightly open
    with dissolve

    la "*Chuckles*"

    scene v14s17_10a # FPP. Same as v14s17_10, Lauren now looking at MC, mouth open
    with dissolve

    la "So... According to the notes, we're looking into macro versus micro economics."

    scene v14s17_10b # FPP. Same as v14s17_10a, mouth closed 
    with dissolve

    u "*Sighs* Okay..."

    u "(My brain is still in Europe I think...)"

    scene v14s17_10c # FFP. Same as v14s17_10b, Lauren tilting her head at MC
    with dissolve

    pause 0.75

    u "What?"

    scene v14s17_10a
    with dissolve

    la "Let's... Put this off for today, yeah?"

    scene v14s17_10b
    with dissolve

    u "*Scoffs* Easy for you to say! You were basically partnered with me to teach me... You already know all of this stuff."

    scene v14s17_10d # FPP. Same as v14s17_10a, slight laughing expression
    with dissolve

    la "*Laughs* That's true, but it's hard to learn when you're not interested or focused. And you sir, are definitely not interested or focused."

    scene v14s17_10a
    with dissolve

    la "So, I'm gonna send you a copy of the TA notes and you can just mull over it all in your own time, haha."

    scene v14s17_10b
    with dissolve

    u "Well, thanks... How do you have the TA notes?"

    scene v14s17_10a
    with dissolve

    la "I'm friends with the TA."

    scene v14s17_10b
    with dissolve

    menu:

        "Make fun of her":

            $ add_point(KCT.TROUBLEMAKER)

            u "Ooooohhh... *Coughs* Nerd! *Coughs*"

            scene v14s17_10d
            with dissolve

            la "Ugh, you are so rude! *Chuckles*"

            scene v14s17_10e # FPP. Same as v14s17_10b, different posture 
            with dissolve

            u "I mean, damn... Look at you getting in nice and good with the people on the inside."

            scene v14s17_10a
            with dissolve

            la "Mhmm, that's more like it."

        "Compliment her":

            $ add_point(KCT.BOYFRIEND)

            u "Damn, well done."

            scene v14s17_10d
            with dissolve

            la "Haha, thank you."

    scene v14s17_10b
    with dissolve

    u "So, what are we supposed to do now? Wanna take a nap like Ryan?"

    scene v14s17_11 # FPP. MC looks at Ryan who is sound asleep with his head lying on his desk, Ryan has saliva dripping out of his mouth
    with dissolve

    pause 1.5

    scene v14s17_10d
    with dissolve

    la "No... We can talk."

    scene v14s17_10e
    with dissolve

    u "Ooooh... About what?"

    scene v14s17_10a
    with dissolve

    la "Lindsey is really ramping up this campaign of hers and she decided to ask for some help from a very serious influencer."

    scene v14s17_12 # TPP. Show MC from Laurens perspective, MC looking to the right of him, serious expression, mouth closed
    with dissolve

    pause 0.75

    scene v14s17_12a # TPP. Same as v14s17_12, MC looking to the left of him
    with dissolve

    pause 0.75

    scene v14s17_10b
    with dissolve

    u "Who?"

    scene v14s17_10d
    with dissolve

    la "A girl named Lauren..."

    scene v14s17_10e
    with dissolve

    u "Oh, wow, I see... (Lindsey really has been busy...)"

    scene v14s17_10b
    with dissolve

    u "What'd she ask for from you?"

    scene v14s17_10a
    with dissolve

    la "She asked me if I would help her with a bake sale to raise money for her campaign."

    scene v14s17_10b
    with dissolve

    u "Are you gonna help her?"

    scene v14s17_10f # FPP. Same as v14s17_10a, Lauren shrugging her shoulders and slightly tilting her head to the side
    with dissolve

    la "I don't know."

    scene v14s17_10a
    with dissolve

    la "I'm always down for a bake sale, but I'm not exactly trying to get involved in any of this. Did you see all of her flyers?"

    scene v14s17_10e
    with dissolve

    u "How could I miss 'em?"

    scene v14s17_10a
    with dissolve

    la "Exactly, it's all kinda crazy right now..."

    scene v14s17_10g # FPP. Same as v14s17_10a, different posture
    with dissolve

    la "I mean, I appreciate Chloe and I've always seen her as the leader of the Chicks."

    scene v14s17_10a
    with dissolve

    la "I also have to admit though, Lindsey has great leadership potential and tons of new ideas that will greatly benefit not only the Chicks, but all sororities."

    scene v14s17_10b
    with dissolve

    u "Is this the part where you ask me what I think you should do?"

    scene v14s17_10d
    with dissolve

    la "Ha, yeah. What do you think I should do?"

    menu:
        "Help Lindsey":
            scene v14s17_10b
            with dissolve
            
            u "We both know you're a great baker and obviously Lindsey knows it too, so I think you should help her."

            scene v14s17_10g
            with dissolve

            la "Do you really think so?"

            scene v14s17_10e
            with dissolve

            u "I do. Lindsey has been working her ass off since the minute she decided to run for President, she really cares about the Chicks."

            scene v14s17_10b
            with dissolve

            u "Plus, she came to you, of all people, for a reason. She trusts you, and knows what you're capable of."

            if lauren.relationship.value >= Relationship.GIRLFRIEND.value or kct == "loyal":
                if lauren.relationship.value < Relationship.GIRLFRIEND.value:
                    call screen kct_popup
            
                $ v14_lauren_helps_lindsey = True
            
                scene v14s17_10g
                with dissolve
             
                $ set_presidency_percent(v14_lindsey_popularity + 3)
                la "You're right. I guess in the end it's all about loyalty, huh?"

                if v11_hp_points == 3:
                    scene v14s17_10b
                    with dissolve

                    u "A true Pofflehoof..."

                    scene v14s17_10d
                    with dissolve

                    la "Haha, I guess you're right."

                scene v14s17_10a
                with dissolve

                la "I'll talk to her and see what she needs me to do."

            else:
                scene v14s17_10g
                with dissolve

                call screen kct_popup(required_kct="loyal")
                la "You're right, but..."

                scene v14s17_10h # FPP. Same as v14s17_10a, serious expression 
                with dissolve

                $ set_presidency_percent(v14_lindsey_popularity + 1)
                la "I do want to think about it a bit more before I decide."

            scene v14s17_10e
            with dissolve

            u "Sounds like a plan."

        "Don't help Lindsey":
            scene v14s17_10b
            with dissolve

            u "Honestly, Lauren..."

            scene v14s17_10e
            with dissolve

            u "You really don't wanna get involved in any aspect of this mess."

            scene v14s17_10b
            with dissolve

            u "I seriously think it's best to just let Lindsey figure all of that out on her own."

            u "If she came to you for just another bake sale then it'd be different, but this is a bake sale with a hidden agenda."

            scene v14s17_10e
            with dissolve

            u "Plus... It's not your job to stress about this, you know?"

            scene v14s17_10b
            with dissolve

            u "Lindsey is the one running for President. Not you."

            scene v14s17_10a
            with dissolve

            la "*Sighs* You're right... Thank you."

            scene v14s17_10h
            with dissolve

            la "I'll tell her the truth about me just not wanting to choose sides."

            scene v14s17_10e
            with dissolve

            u "That sounds like a plan."

            u "(Unless...)"

            menu:
                "Ask Lauren to sabotage Lindsey":
                    $ add_point(KCT.TROUBLEMAKER)
                    scene v14s17_10b
                    with dissolve
                    
                    u "(That would be very beneficial for Chloe's campaign...)"

                    scene v14s17_10e
                    with dissolve

                    u "Unless..."

                    scene v14s17_10h
                    with dissolve

                    la "Hm?"

                    scene v14s17_13 # TPP. Show MC whispering into Lauren's ear, slight smile, mouth open, Lauren, slight smile, mouth closed
                    with dissolve

                    u "*Whispers* Do you think you could... \"sabotage\" Lindsey's bake sale?"

                    scene v14s17_14 # TPP. Show MC from Laurens perspective, MC with one finger over his mouth, shushing expression, slight smile, mouth slightly open
                    with dissolve

                    pause 0.75

                    scene v14s17_13a # TPP. Same as v14s17_13, Lauren now whispering back into MCs ear, Lauren, mouth open, MC, mouth closed
                    with dissolve

                    la "*Whisper* What?! Are you crazy?"

                    scene v14s17_10b
                    with dissolve

                    u "Probably a little, yeah."

                    scene v14s17_13a
                    with dissolve

                    la "*Whispers* Shhh! Why? You just said not to get involved."

                    scene v14s17_13
                    with dissolve

                    u "*Whispers* Truth is, I don't want her to win."

                    u "*Whispers* It's Chloe's last year and if I can keep Lindsey from taking over, that's what I'll do. She doesn't need to be President."

                    scene v14s17_13a
                    with dissolve

                    la "*Whispers* And you want me to help you do that?!"

                    scene v14s17_13
                    with dissolve

                    u "*Whispers* Only you can! You have a perfect opportunity."

                    scene v14s17_13a
                    with dissolve

                    la "*Whispers* [name]! This is something I'd never do for anyone, you know that."

                    scene v14s17_13
                    with dissolve

                    u "*Whispers* I know, because you're loyal to those who respect you and want things to be exactly the way they're supposed to be."

                    scene v14s17_10h
                    with dissolve

                    la "Right..."

                    scene v14s17_10e
                    with dissolve

                    u "You're the most loyal person I know, Lauren. That's why I'm asking you, the one person I trust with anything and everything."

                    if lauren.relationship.value >= Relationship.GIRLFRIEND.value or kct == "loyal":
                        if lauren.relationship.value < Relationship.GIRLFRIEND.value:
                            call screen kct_popup
                        
                        $ v14_lauren_sabotage = True
                    
                        scene v14s17_10a
                        with dissolve

                        $ set_presidency_percent(v14_lindsey_popularity - 2)
                        la "I guess you're that one person for me too. It must feel like Lindsey is crossing the line by running against Chloe, no?"

                        scene v14s17_10e
                        with dissolve

                        u "Yeah, it does. She did go behind her friend's back just to do all of this."

                        scene v14s17_10h
                        with dissolve

                        la "You really believe this is really the right thing to do?"

                        scene v14s17_10b
                        with dissolve

                        u "I do."

                        scene v14s17_15 # TPP. Show MC looking at Lauren, slight smile, mouth closed, Lauren looking at MC intently, mouth closed 
                        with dissolve

                        pause 0.75

                        scene v14s17_10i # FPP. Same as v14s17_10a, Lauren looking to the side, neutral expresssion, mouth open
                        with dissolve

                        la "*Sighs* Look..."

                        scene v14s17_13a
                        with dissolve

                        la "*Whispers* All I'm willing to do is tell her that I'll help her and then... not show up."

                        scene v14s17_10b
                        with dissolve

                        $ grant_achievement("beastie_boy")

                        u "You say that like it's nothing... Lauren, that's perfect. Everything will go south without you."

                        scene v14s17_10h
                        with dissolve

                        la "Okay, yeah I get it. Just don't bring it up again, okay?"

                        scene v14s17_10g
                        with dissolve

                        u "My lips are sealed."

                        scene v14s17_12b # TPP. Same as v14s17_12, MC looking at Lauren, pretending that he is zipping his lips, slight smile, mouth closed
                        with dissolve

                        pause 0.75
                        
                        if lauren.relationship.value >= Relationship.GIRLFRIEND.value:
                            scene v14s17_16 # TPP. Show MC, neutral expression, mouth closed, Lauren beside and looking at MC, Lauren puts both her hands together, begging expression, mouth open
                            with dissolve

                            la "With a kiss?"

                            scene v14s17_16a # TPP. Same as v14s17_16, MC, slight smile, mouth open, Lauren, slight smile, mouth closed 
                            with dissolve

                            u "With a kiss."

                            scene v14s17_16b # TPP. Same position as v14s17_16, Show MC and Lauren kissing
                            with dissolve

                            pause 1.75

                    else:
                        scene v14s17_17 # FPP. Lauren Looking at MC, serious expression, mouth open
                        with dissolve
                        
                        call screen kct_popup(required_kct="loyal")
                        $ set_presidency_percent(v14_lindsey_popularity + 1)
                        la "Exactly, the most loyal person you know, and that's why you of all people should know that I wouldn't do something like that."

                        scene v14s17_17a # FPP. Same as v14s17_17, mouth closed
                        with dissolve

                        u "*Awkward Chuckle* Yeah, yeah... I knew. I was just joking. *Laughs*"

                        scene v14s17_17
                        with dissolve

                        la "Mhmm, sure you were."

                        scene v14s17_17a
                        with dissolve

                        u "Ha! I was..."

                    jump v14s17_end
                
                "Don't ask her":
                    $ add_point(KCT.BOYFRIEND)
                    $ set_presidency_percent(v14_lindsey_popularity + 1) 
                    u "(I'm not getting involved in that...)"
                
                    jump v14s17_end
        
label v14s17_end:
    scene clock2c
    with fade

    pause 0.75

    scene v14s17_17b # FPP. Same as v14s17_17, slight smile
    with fade

    la "Oh perfect, class is over... Be careful about everything you do during this whole... \"mess\", okay?"

    scene v14s17_17c # FPP. Same as v14s17_17b, mouth closed
    with dissolve

    u "Yeah, I will. You too."

    scene v14s17_17b
    with dissolve

    la "Bye..."

    scene v14s17_17c
    with dissolve

    u "See you."

    scene v14s17_18 # TPP. MC and Lauren both stand up, both slight smile, mouths closed
    with dissolve

    pause 0.75

    if lauren.relationship.value >= Relationship.GIRLFRIEND.value: 
        scene v14s17_19 # TPP. Show MC and Lauren kissing
        with dissolve

        play sound "sounds/kiss.mp3"

        pause 1.5

        scene v14s17_20 # FPP. MC watches Lauren walk out of the classroom, Lauren's back facing MC
        with dissolve

        pause 0.75

        stop music fadeout 3
        jump v14s18

    else: 
        scene v14s17_20 
        with dissolve

        pause 0.75

        stop music fadeout 3
        jump v14s18