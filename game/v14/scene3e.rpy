# SCENE 03e: Talk after sex
# Locations: Brothal
# Characters: MC (Outfit: 3), RYAN (Outfit: 1), IMRE (Outfit: 2)
# Time: Night

label v14s03e:
    play music "music/v13/Track Scene 10.mp3" fadein 2

    if v14_ryan_satin: 
        scene v14s03e_1 # TPP. Show MC standing outside of room, neutral expression, mouth closed 
        with fade

        pause 0.75

        scene v14s03e_1a # TPP. Same as v14s03e_1, different posture 
        with fade

        pause 0.75

        scene v14s03e_1
        with fade

        pause 0.75

        scene v14s03e_2 # TPP. Show MC standing outside of room, neutral expression, mouth closed, Ryan opens door and starts walking out, slight smile, mouth closed
        with dissolve

        pause 0.75

        scene v14s03e_3 # FPP. Ryan looking at MC, slight smile, mouth closed
        with dissolve

        u "Umm, hey... Back already, huh?"

        scene v14s03e_3a # FPP. Same as v14s03e_3, slight laughing expression, mouth open
        with dissolve

        ry "Yeah, I came pretty quick. *Laughs* I'm not proud of it, but she didn't mind."

        scene v14s03e_3
        with dissolve

        menu: 
            "Good to hear":
                $ add_point(KCT.BRO)
                
                u "Oh, good to hear..."

                scene v14s03e_3b # FPP. Same as v14s03e_3, mouth open
                with dissolve

                ry "Damn right it's good!" 

            "Oof, poor Satin":
                $ add_point(KCT.TROUBLEMAKER)

                scene v14s03e_3
                #with dissolve

                u "Oof, poor Satin, haha."

                scene v14s03e_3b # FPP. Same as v14s03e_3, mouth open
                with dissolve

                ry "Oh shut up." 
        
        ry "She said I was the best virgin she's ever had."

        scene v14s03e_3
        with dissolve

        u "Haha. Best three minutes of her life, huh?"

        scene v14s03e_3b
        with dissolve

        ry "You know it!"

    else:
        scene v14s03e_4 # TPP. Show MC walking through brothal corridor, neutral expression, mouth closed 
        with dissolve

        pause 0.75

        scene v14s03e_5 # TPP. Show MC walking over to Ryan sitting at the bar, neutral expression, mouth closed, Ryan's back facing MC
        with dissolve
       
        pause 0.75

        scene v14s03e_6 # FPP. Ryan looking at MC, slight smile, mouth closed
        with dissolve

        u "Hey, hey!"

        scene v14s03e_6a # FPP. Same as v14s03e_6, mouth open
        with dissolve

        ry "Hey man."

        scene v14s03e_6
        with dissolve

        u "Imre's not back yet?"

        scene v14s03e_6a
        with dissolve

        ry "I guess, yeah. I haven't seen him."

        scene v14s03e_6b # FPP. Same as v14s03e_6a, different posture
        with dissolve

        ry "I didn't know you had left either. Spent the past fifteen minutes looking for your big ass head."

        scene v14s03e_6
        with dissolve

        u "Oh, my bad. I was, you know... busy. You weren't?"

        scene v14s03e_6a
        with dissolve

        ry "Nope, I decided to wait for my first time to be a little more... clean."

        scene v14s03e_6
        with dissolve

        menu:
            "I'm glad you waited":
                $ add_point(KCT.BRO)
                u "I'm glad you did."

                scene v14s03e_6b
                with dissolve

                ry "Ha... Why are you glad?"

                scene v14s03e_6
                with dissolve

                u "That girl you were talking to... She had herpes."

            "You should've done it":
                $ add_point(KCT.TROUBLEMAKER)

                u "I don't know man, I think you should've done it."

                scene v14s03e_6b
                with dissolve

                ry "Shit, you really think so?"

                scene v14s03e_6
                with dissolve

                u "Although, that girl did have herpes."

        scene v14s03e_6c # FPP. Same as v14s03e_6a, angry expression, mouth open 
        with dissolve

        ry "WHAT THE FUCK?!"

        scene v14s03e_6d # FPP. Same as v14s03e_6c, different posture
        with dissolve

        ry "WHY DIDN'T YOU TELL ME!?"

        scene v14s03e_6e # FPP. Same as v14s03e_6c, mouth closed
        with dissolve

        u "Sorry bro, I wasn't thinking with my head..."

        u "I was thinking with my... head."

        scene v14s03e_6f # FPP. Same as v14s03e_6c, annoyed expression
        with dissolve

        ry "Yeah, yeah. Whatever, [name]."

        ry "I'll give you a pass this time since nothing happened."

        scene v14s03e_6e
        with dissolve

        u "Haha, thanks. I promise next time I'll-"

        scene v14s03e_6f
        with dissolve

        ry "You'll tell me if the chick I'm about to bang is carrying a disease?"

        scene v14s03e_6
        with dissolve

        u "Yeah... that."

    scene v14s03e_7 # TPP. Show Imre walking up to MC and Ryan, Imre, annoyed expression, mouth open, MC and Ryan, both neutral expression, mouth closed
    with dissolve

    imre "This is bullshit!"

    scene v14s03e_8 # FPP. Imre looking at MC, slightly annoyed expression, mouth closed
    with dissolve

    u "What's wrong with you?"

    scene v14s03e_8a # FPP. Same as v14s03e_8, mouth open 
    with dissolve

    imre "Bro, I can't afford any of these damn hoes."

    scene v14s03e_9 # FPP. Ryan looking in Imre's direction, slight smile, mouth open
    with dissolve

    ry "Not even with all the money you stole?"

    scene v14s03e_8b # FPP. Same as v14s03e_8a, Imre looking in Ryans direction
    with dissolve

    imre "No, not even with the money I sto-"

    scene v14s03e_8c # FPP. Same as v14s03e_8, Imre looks down and feels over his pockets.
    with dissolve

    pause 0.75

    scene v14s03e_8d # FPP. Same v14s03e_8b, slight smile
    with dissolve

    imre "The money was put into good hands."

    scene v14s03e_9
    with dissolve

    ry "Ahh, that's how you're putting it?"

    scene v14s03e_8d
    with dissolve

    imre "Exactly."

    scene v14s03e_9
    with dissolve

    ry "Well, I actually have some news that you might be interested in."

    scene v14s03e_8d
    with dissolve

    imre "What's up?"

    scene v14s03e_9a # FPP. Same as v14s03e_9, different posture
    with dissolve

    ry "There's a girl named Ashley here... She's in booth two, and in my opinion, she's the hottest girl here."

    scene v14s03e_9
    with dissolve

    ry "If you wanna get with her Imre, I'm willing to pay half."

    scene v14s03e_8e # FPP. Same as v14s03e_8d, surprised expression
    with dissolve

    imre "*Gasps* Ryan... Bro... Are you serious right now?"

    scene v14s03e_9a
    with dissolve

    ry "I'm deadass right now, dude."

    scene v14s03e_8d
    with dissolve

    imre "Hell yeah I'll do it! Thanks man, really."

    scene v14s03e_8f # FPP. Same as v14s03e_8d, different posture
    with dissolve

    imre "Guess you're not so bad after all."

    scene v14s03e_9
    with dissolve

    ry "Haha, yeah... I did try to tell you that."

    scene v14s03e_10 # FPP. Show Ryan giving Imre money, Ryan slight smile, mouth open, Imre, slight smile, mouth closed
    with dissolve

    pause 0.75

    ry "Here you go. Now enjoy."

    scene v14s03e_10a # FPP. Same as v14s03e_10, Ryan, hands down at side, mouth closed, Imre looking at money in one hand, mouth open 
    with dissolve

    imre "Haha, yes! I appreciate it, Ryan."

    scene v14s03e_11 # TPP. MC and Ryan watch as Imre walks off around a corner, MC and Ryan, both slight smile, mouth closed, Imre back facing them
    with dissolve

    pause 0.75

    scene v14s03e_12 # FPP. Ryan looking at MC, slight smile, mouth closed
    with dissolve

    u "That was... disgustingly nice of you..."

    scene v14s03e_12a # FPP. Same as v14s03e_12, laughing expression, mouth open
    with dissolve

    ry "*Laughs* No it wasn't."

    scene v14s03e_12b # FPP. Same as v14s03e_12a, slight smile
    with dissolve

    ry "Ashley is a man."

    scene v14s03e_12a
    with dissolve

    ry "*Laughs* Emerald told me about him."

    scene v14s03e_12
    with dissolve

    menu:

        "Laugh":
            $ add_point(KCT.TROUBLEMAKER)
            u "*Laughs* Oh god."

        "Get mad":
            $ add_point(KCT.BRO)
            u "What the fuck?!"

    u "So you set Imre up? I thought you two were finally getting along."

    scene v14s03e_12a
    with dissolve

    ry "So did he. *Laughs*"

    menu:
        "Tell Imre":
            
            scene v14s03e_12c # FPP. Same as v14s03e_12, serious expression
            with dissolve
            
            u "Bro, that's fucked up. What if the guy tries to-"

            u "Nah... I gotta stop this from happening, Ryan."

        "Don't tell Imre":
            scene v14s03e_12
            with dissolve

            u "That's cold as hell Ryan, but... he's on his own with this one."

    scene v14s03e_13 # TPP. Show MC walking away towards Imre's direction, neutral expression, mouth closed 
    with dissolve

    pause 0.75

    scene v14s03e_14 # TPP. Show Imre charging around the corner, angry expression, mouth closed, MC, neutral expression, mouth closed 
    with dissolve

    pause 0.75
    
    scene v14s03e_15 # TPP. Show MC grabing and holding Imre back, MC back facing camera while holding Imre, Imre, angry expression, mouth open 
    with dissolve

    imre "Get over here you punk ass bitch!"

    scene v14s03e_15a # TPP. Same postioning as v14s03e_15, MC looking at Imre, serious expression, mouth open, Imre, angry expression, mouth closed
    with dissolve

    u "Imre, calm down!"

    scene v14s03e_16 # TPP. Show Imre breaking free from MC, angry expression, mouth closed, MC, surprised expression, mouth closed
    with dissolve

    pause 0.75

    scene v14s03e_17 # FPP. Imre tries to punch Ryan but Ryan dodges all his attacks, Imre, angry expression, mouth closed, Ryan, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v14s03e_17a # FPP. Same as v14s03e_17, Ryan dodges in a different postion
    with dissolve

    pause 0.75

    scene v14s03e_17b # FPP. Same as v14s03s_17, Ryan dodges in a different postion
    with dissolve
    
    pause 0.75

    scene v14s03e_18 # FPP. Imre looking in Ryans direction, annoyed expression, mouth open
    with dissolve

    imre "I don't have time to fuck with you and your bullshit pranks!"

    scene v14s03e_18a # FPP. Same as v14s03e_18, Imre middle fingers Ryan
    with dissolve

    pause 1.25

    scene v14s03e_19 # FPP. Imre's back facing MC as he watches him walk back from where he came from
    with dissolve

    pause 0.75

    scene v14s03e_20 # FPP. Ryan looking at MC, slight laughing expression, mouth open
    with dissolve

    ry "*Laughs* Oh my god... That was a lot funnier than I expected it to be, he couldn't land a single hit! *Laughs*"

    scene v14s03e_20a # FPP. Same as v14s03e_20, slight smile, mouth closed
    with dissolve

    menu:
        "That was hilarious":
            $ add_point(KCT.TROUBLEMAKER)
            u "Haha, that was hilarious."

            scene v14s03e_20
            with dissolve

            ry "Right???"

        "Not cool, Ryan":
            $ add_point(KCT.BOYFRIEND)
            
            scene v14s03e_20a
            #with dissolve
            
            u "Not cool, Ryan."

            scene v14s03e_20
            with dissolve

            ry "How is weaving every punch he throws, \"not cool\"?"

            scene v14s03e_20a
            with dissolve

            u "*Sighs* That's not what I'm talking about, and you know it."

            scene v14s03e_20b # FPP. Same as v14s03e_20, serious expression 
            with dissolve

            ry "Ha, alright [name]. Chill out."

    scene v14s03e_21 # TPP. Show MC and Ryan leaving the brothal, both neutral expression, mouth closed 
    with dissolve

    pause 0.75

    scene v14s03e_22 # TPP. Show MC and Ryan crossing the road, both neutral expression, mouth closed
    with dissolve

    pause 0.75

    scene v13s31_19
    with dissolve
    
    pause 0.75

    stop music fadeout 3
    jump v14s04