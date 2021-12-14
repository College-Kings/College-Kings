# SCENE 21: If chloe rs Having sex and help Chloe
# Locations: Outside Front of School building. And Parking lot.
# Characters: CHLOE (Outfit: 2), MC (Outfit: 9)
# Time: Afternoon

label v14s21:
    play music "music/v13/Track Scene 30_1.mp3" fadein 2

    scene v14s21_1 # TPP. Show MC walking outside infront of the school, slight smile, mouth closed.
    with dissolve

    cl "[name]!"

    scene v14s21_1a # TPP. Show MC starting to turn around, slight smile, mouth closed.
    with dissolve

    cl "[name]! Wait up!"

    scene v14s21_2 # FPP. Chloe running towards MC, Chloe slight smile, mouth open.
    with dissolve
   
    pause 0.75

    scene v14s21_2a # FPP. Same as v14s21_2, Chloe getting close to MC's position.
    with dissolve

    pause 0.75

    scene v14s21_2b # FPP. Same as v14s21_2a, Chloe reaches MC and is standing still infront of him, Chloe looking at MC, Chloe slight smile, mouth closed.
    with dissolve

    u "What's happening? Something wrong?"

    scene v14s21_2c # FPP. Same as v14s21_2b, Chloe slight smile, mouth open.
    with dissolve

    cl "No, no, nothing's wrong. *Panting*"

    cl "Are you busy right now?"

    scene v14s21_2b
    with dissolve

    u "Not at this very moment, no."

    scene v14s21_2c
    with dissolve

    cl "Okay, well..."

    cl "When I left the library earlier, I couldn't help but feel like I didn't really translate how thankful I am for all of your help."

    scene v14s21_2b
    with dissolve
    
    pause 0.01 #close and open mouth due to many dialogue lines
    
    scene v14s21_2c
    with dissolve

    cl "You're not only there for me in private but now in public as well. That's something I can't thank you enough for."

    cl "A lot of people that I know tend to avoid hanging out with me, because of the rumors or preconceived images that float around. But..."

    scene v14s21_2b
    with dissolve
    
    pause 0.01 #close and open mouth due to many dialogue lines
    
    scene v14s21_2c
    with dissolve

    cl "You don't care what people say. And that's what I appreciate the most."

    scene v14s21_3 # TPP. Show MC holding Chloe's face, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    play sound "sounds/kiss.mp3"

    scene v14s21_3a # TPP. Same as v14s21_3, MC kissing Chloe on the forehead, Chloe with her eyes closed, Chloe blushing, Chloe slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v14s21_3
    with dissolve

    pause 0.75

    scene v14s21_2d # FPP. Same as v14s21_2c, MC holding Chloe's face, Chloe slight smile, mouth closed.
    with dissolve

    u "I enjoy being there for you."

    u "I adore seeing you happy, a-and excited..."

    scene v14s21_2e # FPP. Same as v14s21_2d, Chloe slight smile, mouth open.
    with dissolve

    cl "*Chuckles*"

    scene v14s21_2d
    with dissolve

    u "And honestly Chloe, I'll do whatever I can to help keep that gorgeous smile on your face for as long as humanly possible."

    scene v14s21_2f # FPP. Same as v14s21_2d, MC no longer holding Chloe's face, Chloe's arms wrapped around MC's neck, Chloe slight smile, mouth open.
    with dissolve

    cl "You're the most amazing person I've ever met, do you know that?"

    scene v14s21_2g # FPP. Same as v14s21_2f, Chloe slight smile, mouth closed.
    with dissolve

    u "I do now, I suppose. Although, I'm not completely agreeing with you on that one..."

    scene v14s21_2f
    with dissolve

    cl "*Chuckles*"

    cl "You know, I think I need to apologize in advance."

    scene v14s21_2g
    with dissolve

    u "Apologize? For what?"

    scene v14s21_2f
    with dissolve

    cl "I mean, with the campaign being this real and competitive, I'm gonna have a lot less time than what we're used to."

    cl "So, sadly that means we'll have less time to be together, you know?"

    scene v14s21_2g
    with dissolve

    menu:
        "That does kinda suck":
            $ add_point(KCT.TROUBLEMAKER)
            u "That does kinda suck. I guess we'll have to make the most out of the time we have."

        "Don't worry about it":
            $ add_point(KCT.BOYFRIEND)
            u "I'm a patient man when it comes to the things I care about, Chloe. I know your situation and I understand that this campaign is more important right now."

            scene v14s21_2f
            with dissolve

            cl "*Sighs* You really are the best."

            scene v14s21_2g
            with dissolve

            u "Thank you, you are too."

    scene v14s21_2f
    with dissolve

    cl "You know, I have some time right now..."

    scene v14s21_2g
    with dissolve

    u "Oh, yeah?"

    scene v14s21_2f
    with dissolve

    cl "Yeah... I think I have a nice idea in mind to kick off our campaign as well."

    scene v14s21_2g
    with dissolve

    u "What's that?"

    scene v14s21_2f
    with dissolve

    cl "Hmm..."

    scene v14s21_4 # TPP. Chloe with her arms wrapped around MC, leaning in to whisper into MC's ear, MC slight smile, mouth closed, Chloe flirtatious smile, mouth open.
    with dissolve

    cl "*Whispers* Let me show you."

    scene v14s21_5 # TPP. Chloe pulling MC by his hand, MC following willingly, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v14s21_6 # TPP. Chloe pulling MC by his hand, Now at the parking lot of the school, both slight smile, mouth closed.
    with fade

    pause 0.75

    scene v14s21_7 # TPP. Chloe pulling MC by his hand, Now in an area of the parking lot where no one will go to, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v14s21_8 # FPP. In the back area of the parking lot, MC looking at Chloe, Chloe looking at MC, Chloe slight smile, mouth closed.
    with dissolve

    u "Is there a reason we're in the parking lot?"

    scene v14s21_8a # FPP. Same as v14s21_8, Chloe slight smile, mouth open.
    with dissolve

    cl "No one ever comes back here, you know?"

    cl "I used to sit out here and study everyday after class during my first couple of years on campus."

    cl "One of the very few places on campus where I know I won't be bothered."

    scene v14s21_8
    with dissolve

    u "So, we're here to study?"

    scene v14s21_8a
    with dissolve

    cl "*Chuckles*"

    scene v14s21_9 # FPP. MC looking down at his hands, Chloe know holding his hands and standing closer to him.
    with dissolve

    cl "We can call it that."

    scene v14s21_10 # TPP. Show Chloe kissing MC.
    with dissolve
    play sound "sounds/kiss.mp3"

    pause 1.5

    scene v14s21_10a # TPP. Chloe and MC kissing in a different position.
    with dissolve
    play sound "sounds/kiss.mp3"

    menu:
        "Continue":
            $ add_point(KCT.BOYFRIEND)
            $ add_point(KCT.TROUBLEMAKER)
            $ sceneList.add("v14_chloe")
            stop music fadeout 3
            jump v14s21a
        
        "Pull back":
            $ add_point(KCT.BOYFRIEND)
            scene v14s21_10b # TPP. MC pulling away from the kissing, MC slight smile, mouth closed, Chloe confused expression, mouth open
            with dissolve

            cl "Hm? Is something wrong?"

            scene v14s21_8b # FPP. Same as v14s21_8a, Chloe confused expression, mouth closed.
            with dissolve

            u "N-No... Nothing's wrong at all, I just-"

            scene v14s21_8c # FPP. Same as v14s21_8b, Chloe sad and confused expression, mouth closed.
            with dissolve

            u "Look, Chloe... I don't want you to feel like you owe me anything just for supporting you."

            scene v14s21_8d # FPP. Same as v14s21_8c, MC holding Chloe's face, Chloe sad and confused expression, mouth closed.
            with dissolve

            u "I do these things because I care about you and want you to succeed."

            u "I don't do it just because I expect something from you in the end."

            scene v14s21_8e # FPP. Same as v14s21_8d, Chloe smiling, mouth closed.
            with dissolve

            pause 0.75

            scene v14s21_8f # FPP. Same as v14s21_8e, Chloe kissing MC.
            with dissolve
            play sound "sounds/kiss.mp3"

            pause 1.5

            scene v14s21_8a
            with dissolve

            cl "I've never been with a man like you, but I'm sure as hell happy that I am."

            scene v14s21_8
            with dissolve

            u "I'm happy we're together too."

            u "And I want to see you win. So you go ahead and get things done that need to be done."

            u "I'm gonna go talk to Chris."

            scene v14s21_8a
            with dissolve

            cl "Thank you, baby. So much."

            scene v14s21_8
            with dissolve

            u "Always!"

            scene v14s21_8a
            with dissolve

            cl "I'll meet you there soon, okay?"

            scene v14s21_8
            with dissolve

            u "Of course."

            scene v14s21_8e
            with dissolve

            pause 0.75

            scene v14s21_8f 
            with dissolve
            play sound "sounds/kiss.mp3"

            pause 1.5

            scene v14s21_8g # FPP. Same as v14s21_8f, Chloe walking away from MC.
            with dissolve

            u "(She's something else.)"

            stop music fadeout 3
            jump v14s21b