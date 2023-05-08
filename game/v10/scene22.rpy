# SCENE 22: 
# Locations: MC NEW Wolves/Apes Room & Cafe & Penelope Dorm, Town & Steets
# Characters: MC (Underwear/Outfit 9), Jenny (Outfit 2), Penelope (Outfit 3), Waitress (Outfit 1)
# Time: Tuesday Morning

# -MC wakes from his sleep-

label v10_cafe_w_jenny:
    play music music.ck1.v10.Track_Scene_22_2 fadein 2
    if joinwolves:
        scene v10scwj1 # TPP. Show MC waking up in his new Wolves room in underwear.
        with fade

        u "(Damn, morning comes fast. I need to get ready and head over to the cafe.)"

    else:
        scene v10scwj2 # TPP. Show MC waking up in his Apes room in underwear.
        with fade

        u "(Damn, morning comes fast. I need to get ready and head over to the cafe.)"

    scene v10scwj3 # TPP. Show MC walking towards a table in the café (now wearing outfit 9)
    with fade

    u "(I wonder what Jenny's gonna be like. She could be just as wild as Aubrey. I wonder what she looks like. I wonder if she's hot... Maybe I shouldn't be thinking like that... maybe.)"

    scene v10scwj4 # TPP. Show MC looking around whilst taking a seat at a table. (Make sure it is the table with four seats. Move one seat to the side: https://prnt.sc/12q1qkd)
    with dissolve

    u "(Guess no one's here yet.)"

    scene v10scwj5 # FPP. Show the waiter, camera from MC's perspective as if looking up at her from sitting down, waiter smile, mouth open.
    with dissolve

    waiter "Anything I can get you?"

    scene v10scwj5a # FPP. Same as 5, smile, mouth closed.
    with dissolve

    u "No thanks, I'm just here to meet someone."

    scene v10scwj5
    with dissolve

    waiter "No problem, just let me know if you change your mind."

    scene v10scwj6 # FPP. Show Jenny walking in through the Café door, Jenny should be looking around.
    with dissolve

    pause 0.75

    scene v10scwj6a # FPP. Same as 6, Jenny looks at camera, waves awkwardly, awkward smile.
    with dissolve

    pause 0.75

    scene v10scwj6b # FPP. Same as 6, Jenny now closer to camera, awkward smile, mouth open.
    with dissolve

    jen "[name] right?"

    scene v10scwj6c # FPP. Same as 6, Jenny awkward smile, mouth closed.
    with dissolve

    u "The one and only."

    scene v10scwj6b
    with dissolve

    jen "Heyyy."

    scene v10scwj6c
    with dissolve

    u "Uhm hey, haha."

    scene v10scwj7 # FPP. Close up Jenny who is now sat in the chair opposite MC. Jenny slight smile, mouth open.
    with fade

    jen "It's nice to finally meet you. I've heard a few things about you from Penelope, but not much."

    scene v10scwj7a # FPP. Same as 7, slight smile, mouth closed.
    with dissolve

    u "Good things I hope."

    scene v10scwj7
    with dissolve

    jen "Haha, yes. I don't think I've ever heard Penelope say anything bad about anyone ever, to be fair."

    scene v10scwj7a
    with dissolve

    u "Yeah she's just nice like that."

    scene v10scwj7b # FPP. Same as 7, neutral, mouth open.
    with dissolve

    jen "Okay, so tell me what's going on with her. I hope it's not too serious?"

    if not v10_inv_pen_cafe:
        scene v10scwj7c # FPP. same as 7, neutral, mouth closed.
        with dissolve

        u "It's a little more serious than we'd all like it to be."

        scene v10scwj7b
        with dissolve

        jen "That doesn't sound good."

        scene v10scwj7c
        with dissolve

        u "As we both know, Penelope is a really nice and caring person, but sometimes she cares a little too much... Her kindness just gets in the way of her judgment."

        scene v10scwj7
        with dissolve

        jen "Who'd she go saving now?"

        scene v10scwj7a
        with dissolve

        u "Well... you."

        scene v10scwj7b
        with dissolve

        jen "Wait what?"

        scene v10scwj7c
        with dissolve

        u "Well, Penelope told me a while ago that a friend of hers had some trouble and she wanted to do whatever she could to help her out."

        u "Come to find out, that \"whatever\" was hacking into the school system and getting her friend accepted into San Vallejo College."

        scene v10scwj7d # FPP. Same as 7, slight worry, mouth open.
        with dissolve

        jen "She did what???"

        scene v10scwj7e # FPP. Same as 7, slight worry, mouth closed.
        with dissolve

        u "When she told me I was pretty worried so I went to the dean to see what I could do. After our conversation things seemed better, but it's still pretty serious."

        scene v10scwj7d
        with dissolve

        jen "So that's how I... oh my god, I should've known. There was no way I was getting accepted, I had already given up." 
        jen "But Penelope just kept telling me not to worry about it and everything would work out."
        jen "Wow, this is all my fault. She wouldn't be in this mess if it wasn't for me. *Sigh* So much for being a good friend..."

        scene v10scwj7e
        with dissolve

        menu:
            "Reassure her":
                $ reputation.add_point(RepComponent.BOYFRIEND)
                $ jenny.points += 1

                u "Penelope always puts others before herself, even if you knew and tried to stop her, she probably still would've done it."

                scene v10scwj8 # FPP. Close up of MC placing his hand on Jenny's hand on the table caringly.
                with dissolve

                u "All we can do now is focus on what's next. No matter how rough it gets I'm sure it'll all gonna work out."

            "Stay positive":
                u "Let's try to stay positive. Focusing on the bad stuff isn't going to help. Let's just take it one step at a time."

        scene v10scwj7b
        with dissolve

        jen "You're right, I just wish she would've told me. Maybe I could've done something."
        jen "Penelope must really trust you to confide in you, she tends to keep stuff like that to herself..."

        scene v10scwj7c
        with dissolve

        u "Yeah, guess I just have that \"you can trust me\" face."

        scene v10scwj7
        with dissolve

        jen "I can see that."
        jen "Kinda off topic, but this is a really nice cafe. It has a really cute, rustic vibe."

        scene v10scwj7a
        with dissolve

        u "Yeah, I've been here a few times now. It's kinda becoming a favorite spot of mine."

        scene v10scwj7
        with dissolve

        jen "I can definitely see why."

        scene v10scwj7a
        with dissolve

        menu:
            "Flirt":
                $ reputation.add_point(RepComponent.BOYFRIEND)
                if reputation() == Reputations.POPULAR:
                    $ jenny.points += 1

                else:
                    $ jenny.points -= 1

                u "*Smirks* You're always welcome to join."

                scene v10scwj7
                with dissolve

                jen "Maybe I'll take you up on that some time."

            "Stay friendly":
                u "Yeah, they have really good muffins here as well..."

                scene v10scwj7
                with dissolve

                jen "I may just have to try one at some point."

        play sound sound.vibrate

        scene v10scwj9 # FPP. Show MC's phone in MC's hand, Camera as if MC is looking down at his phone screen. Use Penelope call texture.
        with dissolve

        u "(Penelope?)"

        scene v10scwj7c
        with dissolve

        u "Hold up."

        scene v10scwj10 # TPP. Show MC walking away from the table, phone to ear, MC mouth open.
        with dissolve

        u "Hello?"

        scene v10scwj12 # TPP. Show Penelope in her dorm, phone to ear, lying on her bed, slight worry expression, mouth open.
        with dissolve

        pe "Hey [name]."

        scene v10scwj11 # TPP. Show MC stood elsewhere in the Café on his phone, mouth open.
        with dissolve

        u "Everything alright?"

        scene v10scwj12
        with dissolve

        pe "In all honesty, no. But I don't wanna freak out, I'm trying to stay calm."

        scene v10scwj11
        with dissolve

        u "What happened?"

        scene v10scwj12
        with dissolve

        pe "Hmph, well I got some news from the school."

        scene v10scwj11
        with dissolve

        u "Yes?"

        scene v10scwj12
        with dissolve

        pe "The school is taking action regarding the $15,000 fine. On Thursday I have to face the school's disciplinary board."

        pe "I honestly can't believe this is really happening [name], I didn't think they'd actually take it this far."

        scene v10scwj11a # TPP. Same as 11, mouth closed.
        with dissolve

        menu:
            "Be helpful":
                $ reputation.add_point(RepComponent.BRO)

                scene v10scwj11
                with dissolve

                u "A school hearing? This isn't over then. Much better than actual court."

                u "We have time to prepare and it gives us an opportunity to explain the situation."

                u "They may not agree with what you did, but they will understand."

                scene v10scwj11b # TPP. Same as 11, laugh, mouth open.
                with dissolve

                u "And if they don't then I'll just rob a bank for you."

            "Be supportive":
                $ reputation.add_point(RepComponent.BOYFRIEND)
                $ penelope.points += 1

                scene v10scwj11
                with dissolve

                u "I'm positive everything's gonna work out just fine."

                scene v10scwj12
                with dissolve

                pe "I really hope so."

                scene v10scwj11
                with dissolve

                u "After all the kind stuff you've done, I'm sure some good karma is headed your way."

        scene v10scwj12a # TPP. Same as 12, neutral, mouth open.
        with dissolve

        pe "Thanks for trying to cheer me up. Please say you'll be at the hearing."

        scene v10scwj11
        with dissolve

        u "Of course I will. Not only will I be there, but I'll defend you. Like your own personal lawyer!"

        u "I will not rest until this injustice is rectified."

        scene v10scwj12b # TPP. Same as 12, slight smile, mouth open.
        with dissolve

        pe "Oh my god, really? That'd mean so much to me. I don't know anything about hearings or arguing."

        pe "Thank you [name], I really don't know where my head would be if I didn't have you."

        scene v10scwj11b
        with dissolve

        u "Knowing you, you'd probably find another stranger to introduce yourself to."

        scene v10scwj12b
        with dissolve

        pe "Looking back, how we met was way more awkward then how it went in my head."

        scene v10scwj11b
        with dissolve

        u "Haha."

        scene v10scwj12a
        with dissolve

        pe "I think I'm gonna go for a walk, clear my head a bit."

        scene v10scwj11
        with dissolve

        u "Sounds good, try to feel better."

        scene v10scwj12a
        with dissolve

        pe "I'll try, bye bye."

        scene v10scwj11
        with dissolve

        u "Bye."

        scene v10scwj10a # TPP. Show MC walking back towards the table, no longer on phone, mouth closed.
        with dissolve

        pause 0.75

        scene v10scwj13 # TPP. Show MC taking a seat in the same place he sat prior.
        with dissolve
    
        pause 0.75

        scene v10scwj7c
        with dissolve

        u "Sorry about that."

        scene v10scwj7b
        with dissolve

        jen "No you're fine."

        scene v10scwj7c
        with dissolve

        u "Believe it or not, that was actually Penelope."

        scene v10scwj7b
        with dissolve

        jen "Oh, is everything okay?"

        scene v10scwj7c
        with dissolve

        u "The school is moving forward and Penelope has a disciplinary hearing on Thursday."

        scene v10scwj7d
        with dissolve

        jen "Oh my god, she's probably feeling horrible right now. I need to call her right-"

        scene v10scwj7e
        with dissolve

        u "Relax... she's honestly holding up pretty well. We don't want to stress her out more than she already is."

        scene v10scwj7d
        with dissolve

        jen "Yeah you're right. I feel horrible, I wish there was something I could do."

        scene v10scwj7e
        with dissolve

        u "Well, now that I think about, there just may be."

        scene v10scwj7b
        with dissolve

        jen "Really? What?"

        scene v10scwj7c
        with dissolve

        u "I'm not too sure how the whole thing works, but if it's anything like the hearings on TV. You might be useful as a character witness. You know Penelope better than most people."

        scene v10scwj7
        with dissolve

        jen "Yeah you're right! Of course I'd do that. Maybe then they'd actually see how good of a person she is."

        scene v10scwj7a
        with dissolve

        u "In the meantime I'll prepare a defense."

        scene v10scwj7
        with dissolve

        jen "You'll prepare a defense? Like in those lawyer shows?"#

        scene v10scwj7a
        with dissolve

        u "I mean, I don't know how it works either, but I feel like someone's gotta defend her, right? *Chuckles*"

        scene v10scwj7b
        with dissolve

        jen "Yeah, I guess you're right I'm gonna have to head home now. But thank you so much for letting me know what was going on..."
        jen "I'll probably talk to Penelope later tonight."

        scene v10scwj7c
        with dissolve

        u "Sounds good."

        scene v10scwj14 # TPP. Show MC and Jenny standing up, both smile, jenny mouth open.
        with dissolve

        jen "It was really nice meeting you, I'm glad I reached out."
        

        scene v10scwj15 # FPP. Show Jenny, camera as if MC stood infront of her, Jenny smile, mouth closed.
        with dissolve

        u "I am too."

        scene v10scwj16 # TPP. Show Jenny and MC hugging.
        with dissolve

        pause 0.75

        scene v10scwj15a # FPP. Same as 15, mouth closed.
        with dissolve

        jen "Guess I'll see you at the hearing?"

        scene v10scwj15
        with dissolve

        u "See ya."

    else:
        scene v10scwj17 # FPP. Continuation from v10scwj7. Show Penelope walking into the Café, Penelope looks at camera, slight shock, mouth open.
        with dissolve

        pe "Jenny?"

        scene v10scwj18 # FPP. Show Jenny who is turning to Look at Penelope who is stood near the chair on the edge of the table. Both confused, Jenny mouth open.
        with dissolve

        jen "Oh, heyyy. I didn't know you were also coming."

        scene v10scwj19 # FPP. Show Jenny and Penelope (who is now sat down), both confused, mouths closed.
        with dissolve

        u "Yeah I should probably explain, I thought it'd be best if we all uhm... talked about the situation and laid everything out in the open."

        scene v10scwj20 # TPP. Show Penelope (Camera infront of her same as 7), slight sad, mouth open.
        with dissolve

        pe "Oh okay, that's... that's fine. I guess I needed to tell her at some point."

        scene v10scwj7d
        with dissolve

        jen "Can someone please fill me in, I'm starting to get worried."

        scene v10scwj20f
        with dissolve

        pe "I know I should've told you all of this before, or just not done it at all." 

        pe "But do you remember when you and I talked about you getting accepted to this school?"

        scene v10scwj7f
        with dissolve

        jen "Yeah, I was super nervous about not getting in. Then you said don't worry cause everything would work out and it did. You were right."

        scene v10scwj20f
        with dissolve

        pe "Yeah well... it worked out because I did something. I sort of hacked into the school and made sure you got accepted."

        scene v10scwj7f
        with dissolve

        jen "What???"

        scene v10scwj20f
        with dissolve

        pe "I know, but I couldn't have just sat by and let you not get in. They were going to deny you and you've been through enough already."

        scene v10scwj7f
        with dissolve

        jen "Oh my god Penelope, so I'm the reason you've been so upset all this time?"
        jen "Why didn't you tell me? I didn't want you to do this in the first place!"

        scene v10scwj20f
        with dissolve

        pe "I made the decision to do what I did, it's not your fault."

        scene v10scwj7f
        with dissolve

        jen "It's just- it's a lot to process."

        scene v10scwj20f
        with dissolve

        pe "I know and I'm sorry. Just this morning I actually got some more news from the school."

        scene v10scwj20f # TPP. Same as 20, slight sad, mouth closed.
        with dissolve

        u "Good news?"

        scene v10scwj20
        with dissolve

        pe "Sadly, no. Part of my situation involves a fine of $15,000 the school is handing me."

        pe "On Thursday there's going to be hearing with the disciplinary board."

        scene v10scwj7f
        with dissolve

        jen "Shit. Penelope I-"

        scene v10scwj20f
        with dissolve

        pe "It's not your fault."

        menu:
            "Be helpful":
                scene v10scwj20a
                with dissolve
                u "A school hearing? This isn't over then. Much better than actual court."

                u "We have time to prepare and the hearing alone gives us an opportunity to explain the situation."

                u "They may not agree with what you did, but they will understand. And if they don't then I'll just rob a bank for you."

                u "I'm sure there's someone we can talk to."

                scene v10scwj20
                with dissolve

                pe "Thanks for trying to cheer me up. Please say you'll be at the hearing."

                scene v10scwj20a
                with dissolve

                u "Of course I will. Not only will I be there, but I'll defend you. Like your own personal lawyer!"

            "Be supportive":
                scene v10scwj20a
                with dissolve
                u "I'm positive everything's gonna work out just fine."

                scene v10scwj20
                with dissolve

                pe "I really hope so."

                scene v10scwj20a
                with dissolve

                u "After all the kind stuff you've done, I'm sure some good karma should be headed your way. *Chuckles*"

                scene v10scwj20
                with dissolve

                pe "That would definitely be nice. Please tell me you'll be there."

                scene v10scwj20a
                with dissolve

                u "Of course I will."

                scene v10scwj20b # TPP. Same as 20, neutral, mouth open.
                with dissolve

                pe "Thanks for trying to cheer me up. Please say you'll be at the hearing."

                scene v10scwj20c # TPP. Same as 20, neutral, mouth closed.
                with dissolve

                u "Of course I will. Not only will I be there, but I'll defend you. Like your own personal lawyer!"

                u "I will not rest until this injustice is rectified."

                scene v10scwj20d # TPP. Same as 20, slight smile, mouth open.
                with dissolve

                pe "Oh my god, really? That'd mean so much to me."

                pe "I don't know anything about hearings or arguing."

                pe "Thank you [name], I really don't know where my head would be if I didn't have you to talk to."

        scene v10scwj7a
        with dissolve

        u "I'm not too sure how the whole thing works. But Jenny, you might be useful as a character witness. You know Penelope better than most people."

        scene v10scwj7
        with dissolve

        jen "Yeah you're right! Of course I'd do that. Maybe then they'd actually see how good of a person she is."

        scene v10scwj20d
        with dissolve

        pe "Thank you guys. That probably would help a lot."

        scene v10scwj20e # TPP. Same as 20, slight smile, mouth closed.
        with dissolve

        u "In the meantime, I'll prepare a defense."

        scene v10scwj7
        with dissolve

        jen "You'll prepare a defense? Like in those lawyer shows?"

        scene v10scwj7a
        with dissolve

        u "I mean, I don't know how it works either, but I feel like someone's gotta do it, right? *Chuckles*"

        scene v10scwj7f
        with dissolve

        jen "I guess that's true. It's a lot to process, but thanks for telling me guys. I'm really sorry about all this, Penelope."

        jen "I have to head home now, cause I promised my mom I'd help her out, but I'll see you guys soon, okay?"

        scene v10scwj20f
        with dissolve

        pe "Of course, I'm just glad you finally know."

        scene v10scwj14a # TPP. Same as 14, show MC, Jenny and Penelope standing up from the table, all smiles, Jenny mouth open.
        with dissolve

        jen "It was really nice meeting you, I'm glad I reached out."

        scene v10scwj15
        with dissolve

        u "I am too."

        scene v10scwj16
        with dissolve

        pause 0.75

        scene v10scwj16a # TPP. Same as 16, Jenny hugs Penelope who is stood next to her instead. MC looking at them both.
        with dissolve

        pause 0.75

        scene v10scwj15a
        with dissolve

        jen "Bye guys."

        scene v10scwj15
        with dissolve

        u "See ya."

        scene v10scwj21 # FPP. Show Penelope who is now stood up, neutral, mouth open.
        with dissolve

        pe "Bye bye."

        pe "I think I'm gonna leave as well, I don't think I've really processed everything yet."

        scene v10scwj21a # FPP. Same as 21, neutral, mouth closed.
        with dissolve

        u "Do you want me to go with you?"

        scene v10scwj21
        with dissolve

        pe "Thanks, but I'd rather just be alone."

        scene v10scwj21a
        with dissolve

        u "I understand."

        scene v10scwj21
        with dissolve

        pe "See you around and thank you. For everything..."

        scene v10scwj21a
        with dissolve

        u "Anytime, I'll see you soon..."

        scene v10scwj21
        with dissolve

        pe "Yeah, bye."

        scene v10scwj22 # FPP. Show Penelope leaving the café.
        with dissolve

        pause 0.75

    scene v10scwj23 # TPP. Show MC walking down the sidewalk.
    with Fade(1, 0, 1)
    
    stop music fadeout 3
    
    jump v10_aft_walk_home