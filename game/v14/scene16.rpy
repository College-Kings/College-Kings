# SCENE 16: Chloe and MC in the Hallway
# Locations: School Hallway
# Characters: CHLOE (Outfit: 2), MC (Outfit: 9)
# Time: Morning

label v14s16:
    scene v14s16_1 # TPP. MC starting to turn around, Chloe running towards him from a distance, MC slight smile, mouth closed, Chloe slightly annoyed, mouth closed.
    with dissolve

    pause 0.75

    scene v14s16_1a # TPP. Same as v14s16_1, MC turned around his back facing the camera, Chloe running up to MC, MC slight smile, mouth closed, Chloe slightly annoyed, mouth closed.
    with dissolve

    pause 0.75

    scene v14s16_2 # FPP. MC looking at Chloe, Chloe looking at MC, Chloe slightly annoyed, mouth open.
    with dissolve

    cl "There you are! Are you seeing what I'm seeing?!"

    scene v14s16_2a # FPP. Same as v14s16_2, Chloe slightly annoyed, mouth close.
    with dissolve

    u "I'm seeing it, she's definitely serious about this."

    scene v14s16_2
    with dissolve

    cl "“Serious” isn't even close."

    scene v14s16_2
    with dissolve
    
    if chloegf:
        scene v14s16_3 # TPP. Close up of MC and Chloe, MC kissing Chloe's forehead, both slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v14s16_3a # TPP. Chloe with her eyes closed, Chloe slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v14s16_4 # TPP. MC stepping back from Chloe so they aren't as close, both slight smile, mouth closed.
        with dissolve

    scene v14s16_2
    with dissolve

    cl "*Sighs* I thought we'd get back and have a chance to get comfortable first, but I literally walked into a pro-Lindsey campus."

    scene v14s16_2a
    with dissolve

    u "Have you talked to Lindsey or any of the other Chicks yet?"

    scene v14s16_2
    with dissolve

    cl "I didn't have a choice... I just wanted to go home and sleep last night,  yet I was up for hours being a part of non-stop sorority bickering."

    scene v14s16_2a
    with dissolve

    u "Non-stop? Sheesh... About what?"

    scene v14s16_2
    with dissolve

    cl "Really, [name]? About all of this, obviously!"

    cl "Like, this is low-key bullshit."

    scene v14s16_2a
    with dissolve

    u "I admit, I didn't expect it to be... This much."

    u "I mean... Did she do all of this overnight?"

    scene v14s16_2
    with dissolve

    cl "That's where it gets even fucking worse, 'cause I thought the same thing."

    cl "Come to find out that this shit has been up for at least a week. She's been having people work for her while we were away."

    scene v14s16_2
    with dissolve

    u "(Damn, Lindsey. That's good.)"

    scene v14s16_2a
    with dissolve

    cl "*Speaking fast* Like, what the actual fuck!? Am I missing something?! I have to win this race! She can't just, fuck everything up all because she's doesn't trust me!"

    show screen loyalty_tutorial # Placeholder

    hide screen loyalty_tutorial # Placeholder

    scene v14s16_2a
    with dissolve

    cl "I need a lot of help if I'm going to beat her, [name]. It won't be as easy as I thought either."

    cl "Chris has pretty much promised that the Wolves will side with me so that's a blessing, but the main person I need support from is you."

    cl "I know I've asked you before, but this time I need a final answer. Are you going to help me with this campaign so I can beat Lindsey?"

    cl "It would include planning campaign events like parties, making T-shirts, that kind of stuff."

    if v13_help_chloe:
        cl "I remember how you said you'd help me before but..."
   
    scene v14s16_2b # FPP. Same as v14s16_2a, Chloe cute pose, pouting face, mouth open.
    with dissolve

    cl "If you'd be willing to help me win, I'd be so grateful..."

    cl "I'd do anything to thank you."

    if chloers or chloegf:
        scene v14s16_2c # FPP. Same as v14s16_2a, Chloe winking, slight smile, mouth open.
        with dissolve

        cl "*Chuckles* I can think of a few rewards already..."

        scene v14s16_5 # FPP. MC looking down at his arm as Chloe starts to run her finger down MC's arm, flirting smile, mouth open.
        with dissolve

        pause 0.75

        scene v14s16_2d # FPP. Same as v14s16_2c, Chloe leaning in towards MC's ear and whispering to him, Chloe flirting smile, mouth open.
        with dissolve

        cl "*Whispering* Plus, the president always needs an assistant and if it's my job to, you know... Take care of you, while also running the sorority..."

        cl "*Whispering* I might end up needing someone to help me with all of that... And all of you..."

        cl "*Whispering* Following me?"

        scene v14s16_2b
        with dissolve

        u "(I think she means having an assistant in the bedroom...?!) I'm definitely following."

    scene v14s16_2b
    with dissolve

    cl "So, what's your answer? Will you help me try and win this campaign?"

    menu:
        "I'll help...":
            scene v14s16_2e # FPP. Same as v14s16_2, Chloe slight smile, mouth closed.
            with dissolve

            u "You know how I feel when it comes to you being President, Chlo."

            u "Honestly, I don't think I could ever see anyone filling that role other than you."

            u "Not only that, but you know I'm always gonna be there for you, supporting you in whatever you may need. Of course I'll help you win."

            scene v14s16_6 # TPP. Chloe with her arms wrapped around MC hugging him tight, MC slight smile, mouth closed, Chloe excited smile, mouth open.
            with dissolve

            cl "THANK YOU, THANK YOU, THANK YOU!"

            scene v14s16_2f # FPP. Same as v14s16_2e, Chloe excited smile, mouth open.
            with dissolve

            cl "Thank you so much, [name]."

            scene v14s16_2g # FPP. Same as v14s16_2f, Chloe exited smile, mouth closed.
            with dissolve

            u "You're welcome, Chloe. *Chuckles*"

            scene v14s16_2f
            with dissolve

            cl "Meet me after your class in the library, we have lots to discuss!"

            if chloers or chloegf:
                scene v14s16_6a # TPP. Same as v14s16_6, Chloe kisses MC.
                with dissolve

                pause 0.75

                scene v14s16_2h # FPP. Same as v14s16_2f, Chloe walking away from MC. (Just Chloe's backside so we can reuse the scene for other outcomes.)
                with dissolve

                u "(If her goal was to make me feel sorry enough for her that I would agree to help, she succeeded.) *Chuckles* (I don't wanna get in my head too much about what her intentions are... I want to help her, so that's what I'm gonna do.)"

                scene v14s16_2i # FPP. Same as v14s16_2h, Chloe further away from MC. 
                with dissolve

                u "(Time for class!)"

            else:
                scene v14s16_2h 
                with dissolve

                pause 0.75

                scene v14s16_2i 
                with dissolve

                pause 0.75
                
        "I don't have the time...":
            scene v14s16_2
            with dissolve

            u "Chloe I... I want to help you, but I don't have the time."

            scene v14s16_2a
            with dissolve

            cl "You can't make an ounce of time to help me out? With any of this?"

            scene v14s16_2
            with dissolve

            u "I'm sorry, Chloe. I'm just really busy now that we're back on campus and things with the-."

            if chloegf:
                scene v14s16_2j # FPP. Same as v14s16_2a, Chloe angry expression, mouth open.
                with dissolve

                cl "*Scoffs* What do you mean you don't have time?! You have time to fuck me, but no time to talk?"

                scene v14s16_2k # FPP. Same as v14s16_2j, Chloe angry expression, mouth closed.
                with dissolve

                u "Chloe, woah. That's not what I meant, at all."

                scene v14s16_2j
                with dissolve

                cl "I just don't see how you could choose not to help me."

                scene v14s16_2k
                with dissolve

                u "It's not that I don't want to Chlo, it's just that I'm kinda busy with my own Greek life. We just got back to campus for crying out loud, I mea-"

                scene v14s16_2j
                with dissolve

                cl "It's fine, really."

                cl "I'll remember just how busy you are the next time you want to \"hangout\"."

                scene v14s16_2h

                u "*Sighs* (This is gonna cause some serious issues for us. Fuck... Kinda surprised she didn't break up with me right there... Chloe's way or no way.)"

                scene v14s16_2i
                with dissolve

                u "(Well, time for class!)"

            else:
                scene v14s16_2
                with dissolve

                cl "*Sighs* I'm always having to do things on my own."

                scene v14s16_2a
                with dissolve

                u "I really am sorry, Chloe."

                scene v14s16_2
                with dissolve

                cl "Don't be."

                cl "With or without your help I'm winning this thing."

                cl "I wanted your help because I appreciate your opinion, but also because I thought it'd be nice to spend time together."

                cl "But since you don't have time, I'll leave you be. See you later."

                scene v14s16_2a
                with dissolve

                u "Chloe... Chloe, wait!"

                scene v14s16_2h
                with dissolve

                u "*Sighs* (I knew she wouldn't take that well, Chloe's way or no way.)"

                scene v14s16_2i
                with dissolve

                u "(Oh, well... Time for class!)"

    scene v14s16_7 # TPP. MC standing next to Mrs. Rose's classroom, slight smile, mouth open.
    with dissolve

    u "*Exhales* (Feels so good to be back.)"

    scene v14s16_7a # TPP. Same as v14s16_7a, slight smile, mouth closed.
    with dissolve

    jump v14s17