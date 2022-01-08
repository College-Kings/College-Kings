# SCENE 15: At Ms. Rose House
# Locations: Ms. Rose House
# Characters: Ms. Rose (Outfit: 1), MC (Outfit: 5)
# Time: Afternoon

# SCENE 16: MC leaves mad or not mad
# Locations: Outside Ms. Rose's house on the way to Lauren's party
# Characters: MC (Outfit: 5)
# Time: Evening

label v15s15:
    scene v15s15_1 # TPP. Show MC and Ms. Rose entering the dining room, Ms. Rose slight smile, MC slightly annoyed, mouths closed
    with dissolve

    pause 0.75

    scene v15s15_2 # FPP. MC and Ms. Rose in the dining room, MC looking at Ms. Rose, Ms. Rose looking at Ms. Rose slightly smiling, mouth open
    with dissolve

    ro "Take a seat and make yourself comfortable. I'll be right back with your starter..."

    scene v15s15_2a # FPP. MC and Ms. Rose in the dining room, MC looking at Ms. Rose, Ms. Rose looking at Ms. Rose slightly smiling, mouth closed
    with dissolve

    menu:
        "Be polite":
            $ add_point(KCT.BOYFRIEND)
            
            u "Sounds like I'm getting a three-course meal. *Chuckles* I'm looking forward to it."

        "Be impatient":
            $ add_point(KCT.BRO)
            
            u "Okay, but hurry. I'm actually starting to starve..."

    scene v15s15_2
    with dissolve

    ro "I'm glad to hear it. I like a young man with a big appetite..."

    scene v15s15_2a
    with dissolve

    u "*Gulps*"

    scene v15s15_3 # FPP. MC watches Ms. Rose as she exits the room, focusing a bit on her ass as she looks seductively at MC over her shoulder
    with dissolve

    pause 0.75

    scene v15s15_4 # TPP. Show MC walking over to the head of the dining table, the end that faces the door Ms. Rose just went through, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v15s15_5 # TPP. Show MC sitting down at the head of the dining table, slight smile, mouth closed
    with dissolve

    pause 0.75

    label v15s15sg:

    scene v15s15_6: # TPP. Ms. Rose at the door, mouth closed, seductive look, posing seductively, wearing lingerie, a pearl necklace and a jar of honey in hand (RENDER THIS IMAGE IN 1920x5000 pixels, since it will be a panning image, similar to the Chloe one after homecoming. DM Peace/Mozzart if you have any questions about this)
        subpixel True
        yalign 1.0
        linear 6.0 yalign 0.0
    with fade

    u "(Oh... Wow... That is not what I was expecting!)"

    scene v15s15_7 # FPP. MC sitting at the head of the table Ms. Rose at the door, mouth open, seductive look, posing seductively, wearing lingerie, a pearl necklace and a jar of honey in hand
    with dissolve

    ro "Do you like the presentation of your meal, [name]?"

    scene v15s15_7a # FPP. MC sitting at the head of the table Ms. Rose at the door, mouth open, seductive look, posing seductively, showing off her ass, wearing lingerie, a pearl necklace and a jar of honey in hand
    with dissolve

    ro "It's a new outfit... I especially love the necklace."

    scene v15s15_7b # FPP. MC sitting at the head of the table Ms. Rose walking over to MC mouth open, seductive look, wearing lingerie, a pearl necklace and a jar of honey in hand
    with dissolve

    ro "I wanted to look good for you."

    scene v15s15_7c # FPP. MC sitting at the head of the table Ms. Rose now standing close to MC, mouth closed, seductive look, wearing lingerie, a pearl necklace and a jar of honey in hand
    with dissolve

    u "Y- Yeah, you look good, but-"

    scene v15s15_7d # FPP. MC sitting at the head of the table Ms. Rose now standing close to MC, mouth open, seductive look, wearing lingerie, a pearl necklace, the honey jar is now on the table
    with dissolve

    ro "Here's your starter..."

    scene v15s15_7e # FPP. MC sitting at the head of the table Ms. Rose now standing close to MC, mouth closed, seductive look, wearing lingerie, a pearl necklace, the honey jar on the table
    with dissolve

    u "A jar of honey?"

    scene v15s15_7f # FPP. MC sitting at the head of the table Ms. Rose now standing close to MC, mouth open, seductive look, wearing lingerie, a pearl necklace, she is pouring honey on her boobs, she pulled her top down, but it's still on her
    with dissolve

    ro "I'm serving you some delicious pancakes..."

    scene v15s15_8 # TPP. Show MC getting up from the table, neutral expression, mouth closed
    with dissolve

    pause 0.75

    scene v15s15_9 # FPP. MC standing in front of Ms. Rose, Ms. Rose has her boobs covered in honey, she is looking seductively at MC, mouth closed
    with dissolve

    menu:
        "Reject her":
            $ add_point(KCT.TROUBLEMAKER)

            scene v15s15_9a # FPP. MC standing in front of Ms. Rose, Ms. Rose has her boobs covered in honey, shocked, mouth closed
            with dissolve

            u "What the fuck? I came here for dinner."

            scene v15s15_9b # FPP. MC standing in front of Ms. Rose, Ms. Rose has her boobs covered in honey, shocked, mouth open
            with dissolve

            ro "Yes, and I'm the meal... Don't you like it?"

            scene v15s15_9a
            with dissolve

            u "No, I don't! You said dinner. This is not dinner."

            scene v15s15_9b
            with dissolve

            ro "So, you're not in the mood?"

            scene v15s15_9a
            with dissolve

            u "Damn right, I'm not in the mood."

            scene v15s15_10 # TPP. MC walking out of the dining room, angry, mouth closed, Ms. Rose shocked, reaching out to him as he walks out, boobs still covered in honey, mouth open
            with dissolve

            ro "[name]! Wait!"
            
            $ renpy.end_replay()
            
            # Scene 16
            scene v15s16_1 # TPP. Show MC walking out of Ms. Rose's house, MC mad, mouth closed.
            with dissolve

            u "(I know she was trying, but- Seriously???"

            scene v15s16_2 # TPP. Show MC starting to walk down sidewalk towards Lauren's party, MC mad, mouth closed.
            with dissolve

            u "(She might have fucked up my life by giving me a drink that night.)"

            scene v15s16_3 # TPP. Show MC further down the sidewalk, MC mad, mouth closed.
            with dissolve

            u "(If they find any trace of that drug in my system, I'm done for...)"

            scene v15s16_4 # TPP. MC stopped in place with his eyes closed, MC neutral face, mouth closed.
            with dissolve

            u "*Sighs* (Now it's time for Lauren's party... Game face on, [name].)"

            scene v15s16_5 # TPP. MC starting to walk again, MC neutral face, mouth closed.
            with dissolve

            u "(Time for shopping.)"
            
            stop music fadeout 3
            
            jump v15s17

        "Lick the honey":
            $ grant_achievement("honey_bear")
            $ sceneList.add("v15_rose")
            u "(Don't mind if I do...)"

            scene v15s15_11 # TPP. Show MC licking the honey off Ms. Rose's boobs, Ms. Rose making a sexy face, mouth open as she grabs MC's hair
            with dissolve

            ro "Mmm, yeah... Bon Appetit, [name]."

            scene v15s15_9c # FPP. MC standing in front of Ms. Rose, Ms. Rose has her boobs no longer have honey, she is looking seductively at MC, mouth closed, she is pulling her top back on
            with dissolve

            u "I think I wanna taste the next course..."

            scene v15s15_12 # TPP. Show Ms. Rose removing her panties, sexy look, mouth closed (bra will always), MC removing his clothes, mouth closed
            with dissolve

            pause 0.75

            scene v15s15_13 # TPP. Show Ms. Rose getting on the table, panties off, sexy look, mouth closed
            with dissolve

            pause 0.75

            scene v15s15_14 # FPP. MC standing in front of Ms. Rose, she is laying on her back, legs spread open, panties off, sexy look, mouth closed
            with dissolve

            pause 0.75

            image v15rosoral = Movie(play="images/v15/Scene 15/v15rosoral.webm", loop=True, image="images/v15/Scene 15/v15rosoralStart.webp", start_image="images/v15/Scene 15/v15rosoralStart.webp") 
            image v15rosoral2 = Movie(play="images/v15/Scene 15/v15rosoral2.webm", loop=True, image="images/v15/Scene 15/v15rosoral2Start.webp", start_image="images/v15/Scene 15/v15rosoral2Start.webp")

            scene v15rosoral # IGNORE AS ANIMATION
            with dissolve

            pause 0.75

            ro "*Moans* Oh... Yes... You are a hungry boy! *Laughs*"

            ro "Fuck... Yeah... Does it taste good, baby? Do you love it?"

            scene v15rosoral2 # IGNORE AS ANIMATION
            with dissolve

            pause 0.75

            u "*Muffled* Yes, I love it..."

            ro "I'm so... *Gasps* Happy to hear you say that... *Panting*"

            ro "I think it's time you flip this pancake over and fuck it."

            scene v15s15_15 # TPP. Show MC standing, flipping Ms. Rose over, he's getting ready to fuck her from behind
            with dissolve

            pause 0.75

            image v15rosffb = Movie(play="images/v15/Scene 15/v15rosffb.webm", loop=True, image="images/v15/Scene 15/v15rosffbStart.webp", start_image="images/v15/Scene 15/v15rosffbStart.webp") 
            image v15rosffbf = Movie(play="images/v15/Scene 15/v15rosffbf.webm", loop=True, image="images/v15/Scene 15/v15rosffbStart.webp", start_image="images/v15/Scene 15/v15rosffbStart.webp") 
            image v15rosffb2 = Movie(play="images/v15/Scene 15/v15rosffb2.webm", loop=True, image="images/v15/Scene 15/v15rosffb2Start.webp", start_image="images/v15/Scene 15/v15rosffb2Start.webp")
            image v15rosffb2f = Movie(play="images/v15/Scene 15/v15rosffb2f.webm", loop=True, image="images/v15/Scene 15/v15rosffb2Start.webp", start_image="images/v15/Scene 15/v15rosffb2Start.webp")

            scene v15rosffb # IGNORE AS ANIMATION
            with dissolve

            pause 0.75

            ro "*Moans* Are you... still angry with me, [name]?"

            scene v15rosffbf # IGNORE AS ANIMATION
            with dissolve

            pause 0.75

            u "Of course I'm still angry."

            scene v15rosffb2 # IGNORE AS ANIMATION
            with dissolve

            pause 0.75

            ro "Ha, mmm..."
            
            ro "That's such a fucking turn on..."

            scene v15rosffb2f # IGNORE AS ANIMATION
            with dissolve

            pause 0.75

            ro "Show me how angry you are..."

            scene v15s15_16 # TPP. MC fucking Ms. Rose from behind, she has her mouth closed, MC mouth closed (MC in max penetration)
            with dissolve

            menu:
                "Spank her":
                    $ add_point(KCT.BRO)
                    scene v15s15_16a # TPP. MC fucking Ms. Rose from behind, she has her mouth closed, MC mouth open (MC not in max penetration, this is to make it look like there is movement, as if he were thrusting)
                    with dissolve

                    u "Alright then..."

                    play sound "sounds/slap.mp3"

                    scene v15s15_16b # TPP. MC fucking Ms. Rose from behind, she is moaning, mouth open, MC smacking her ass, mouth closed, MC in max penetration
                    with hpunch

                    ro "*Gasps* I..."

                    scene v15s15_16c # TPP. MC fucking Ms. Rose from behind, mouth open, MC is grabbing her ass, not slapping it, mouth closed, MC not in max penetration
                    with dissolve

                    ro "I'm so sorry... *Moans* I'm so bad..."

                    scene v15s15_17 # FPP. MC looking down at Ms. Rose's ass, he is in max penetration, he is slapping her ass, it's red where he hit it
                    with dissolve

                    u "Damn right you are!"

                    scene v15s15_17a # FPP. MC looking down at Ms. Rose's ass, he is not in max penetration, he is grabbing her ass now, it's red where he hit it
                    with dissolve

                    ro "*Moans* Fuck... Yes, [name]..."

                "Degrade her":
                    $ add_point(KCT.TROUBLEMAKER)
                    scene v15s15_18 # TPP. MC fucking Ms. Rose from behind (different camera angle than v15s15_16), MC, mouth open, slightly angry, Ms. Rose mouth closed, in max penetration
                    with dissolve

                    u "Okay then, you fucking slut."

                    scene v15s15_18a # TPP. MC fucking Ms. Rose from behind, MC, mouth closed, slightly angry, grabbing her hair tightly, Ms. Rose moaning, not in max penetration
                    with dissolve

                    ro "Ah... Ah..."

                    scene v15s15_18b # TPP. MC fucking Ms. Rose from behind, MC, mouth open, slightly angry, grabbing her hair tightly, Ms. Rose moaning, in max penetration
                    with dissolve

                    u "This... Is how fucking angry I am..."

                    scene v15s15_18c # TPP. MC fucking Ms. Rose from behind, MC, mouth open, slightly angry, grabbing her hair tightly, Ms. Rose moaning, not in max penetration
                    with dissolve

                    u "*Moans* You like making me angry?"

                    scene v15s15_18d # TPP. MC fucking Ms. Rose from behind, MC, mouth closed, slightly angry, grabbing her hair tightly, Ms. Rose mouth open, in max penetration
                    with dissolve

                    ro "I... *Panting* Mmm, yes... I do."

                    scene v15s15_19 # FPP. MC looking down at Ms. Rose's back (from her ass to her head if possible), he is pulling her hair, not in max penetration
                    with dissolve

                    u "Such..."

                    scene v15s15_19a # FPP. MC looking down at Ms. Rose's back (from her ass to her head if possible), he is pulling her hair, in max penetration
                    with dissolve

                    u "A fucking..."

                    scene v15s15_19
                    with dissolve

                    u "Bitch..."

                    scene v15s15_18d
                    with dissolve

                    ro "*Moans* Fuck, [name]!"

            scene v15s15_19b # FPP. MC looking down at Ms. Rose's back (from her ass to her head if possible), not pulling her hair, Ms. Rose looking over her shoulder at MC, mouth closed, not in max penetration
            with dissolve

            u "If you're my dinner, it makes sense to fuck you in the kitchen too..."

            scene v15s15_19c # FPP. MC looking down at Ms. Rose's back (from her ass to her head if possible), not pulling her hair, Ms. Rose looking over her shoulder at MC, mouth open, in max penetration
            with dissolve

            ro "Oh, yeah, of course! Please, [name]."

            scene v15s15_20 # TPP. Show MC leading Ms. Rose to the kitchen
            with dissolve

            pause 0.75

            scene v15s15_21 # TPP. Show MC putting her up against the refrigerator, getting ready to fuck her from behind
            with dissolve

            pause 0.75

            image v15rossd = Movie(play="images/v15/Scene 15/v15rossd.webm", loop=True, image="images/v15/Scene 15/v15rossdStart.webp", start_image="images/v15/Scene 15/v15rossdStart.webp") 
            image v15rossdf = Movie(play="images/v15/Scene 15/v15rossdf.webm", loop=True, image="images/v15/Scene 15/v15rossdStart.webp", start_image="images/v15/Scene 15/v15rossdStart.webp") 
            image v15rossd2 = Movie(play="images/v15/Scene 15/v15rossd2.webm", loop=True, image="images/v15/Scene 15/v15rossd2Start.webp", start_image="images/v15/Scene 15/v15rossd2Start.webp")
            image v15rossd2f = Movie(play="images/v15/Scene 15/v15rossd2f.webm", loop=True, image="images/v15/Scene 15/v15rossd2Start.webp", start_image="images/v15/Scene 15/v15rossd2Start.webp") 

            scene v15rossd # IGNORE AS ANIMATION
            with dissolve

            pause 0.75

            ro "I've never..."

            scene v15rossdf # IGNORE AS ANIMATION
            with dissolve

            pause 0.75

            ro "Been fucked..."

            scene v15rossd2 # IGNORE AS ANIMATION
            with dissolve

            pause 0.75

            ro "Against the refrigerator before, haha... *Moans*"

            scene v15rossd2f # IGNORE AS ANIMATION
            with dissolve

            pause 0.75

            u "(Mmm, fuck...) There's a first time for everything, huh?"

            scene v15rossd # IGNORE AS ANIMATION
            with dissolve

            pause 0.75

            ro "God, yes! Yes!"

            scene v15s15_22 # TPP. Show MC fucking Ms. Rose in standign doggy, she is leaning on the fridge, MS. Rose mouth closed, MC mouth open
            with dissolve

            u "I'm... About to... Where do you want dessert? *Moans*"

            scene v15s15_23 # FPP. MC looks over at the stove
            with dissolve

            u "The stove?"

            scene v15s15_22a # TPP. Show MC fucking Ms. Rose in standign doggy, she is leaning on the fridge, MS. Rose mouth open, MC mouth closed
            with dissolve

            ro "Yes... [name], please... Give it to me."

            scene v15s15_24 # TPP. Show MC and Ms. Rose moving towards the stove
            with dissolve

            pause 0.75

            scene v15s15_25 # TPP. Show MC bending Ms. Rose over the stove
            with dissolve

            pause 0.75

            image v15rosffbstove = Movie(play="images/v15/Scene 15/v15rosffbstove.webm", loop=True, image="images/v15/Scene 15/v15rosffbstoveStart.webp", start_image="images/v15/Scene 15/v15rosffbstoveStart.webp") 
            image v15rosffbstovef = Movie(play="images/v15/Scene 15/v15rosffbstovef.webm", loop=True, image="images/v15/Scene 15/v15rosffbstoveStart.webp", start_image="images/v15/Scene 15/v15rosffbstoveStart.webp") 
            image v15rosffbstove2 = Movie(play="images/v15/Scene 15/v15rosffbstove2.webm", loop=True, image="images/v15/Scene 15/v15rosffbstove2Start.webp", start_image="images/v15/Scene 15/v15rosffbstove2Start.webp") # NOT USING THIS CAUSE OF DIALOGUE
            image v15rosffbstove2f = Movie(play="images/v15/Scene 15/v15rosffbstove2f.webm", loop=True, image="images/v15/Scene 15/v15rosffbstove2Start.webp", start_image="images/v15/Scene 15/v15rosffbstove2Start.webp") 

            scene v15rosffbstove # IGNORE AS ANIMATION
            with dissolve

            pause 0.75

            ro "Yes! Keep going! *Moans* Just like that..."

            scene v15rosffbstovef # IGNORE AS ANIMATION
            with dissolve

            pause 0.75

            ro "You're hitting the... spot... perfec-"

            ro "Ohh, fuuuck! I'm cumming, I'm cu-"

            scene v15rosffbstove2f # IGNORE AS ANIMATION
            with dissolve

            pause 0.75

            ro "*Moans* Oh, [name]... Oh, honey..."

            ro "*Panting* You're so-"

            scene v15s15_26 # TPP. MC pushing Ms. Rose down on her knees so he can cum on her face
            with dissolve

            u "Get on your knees."

            scene v15s15_27 # FPP. Show MC stroking his dick (near the tip), Ms. Rose on her knees, looking up at him, smiling sexily, mouth open (not talking, just waiting for him to cum)
            with dissolve

            u "*Moans* You beautiful psycho..."

            scene v15s15_27a # FPP. Show MC stroking his dick (near the base), Ms. Rose on her knees, looking up at him, smiling sexily, mouth open (not talking), her face full of cum
            with vpunch

            u "*Chuckles* Now you're covered in cream."

            scene v15s15_27b # FPP. MC not stroking his dick anymore, Ms. Rose on her knees, looking up at him, smiling sexily, face full of cum, mouth open (talking)
            with dissolve

            ro "Oh, wow... *Giggles* What an incredible experience that was."

            ro "Let me go clean up, be back in a bit."

            scene v15s15_28 # TPP. Show MC back by the dining table, getting dressed, smiling, mouth closed
            with fade

            u "*Sighs* (Well, the make-up sex is always great, huh? Haha...)"

            $ renpy.end_replay()

            scene v15s15_29 # FPP. MC looking at the door, Ms. Rose entering, she is dressed and cleaned up now, smiling, mouth closed
            with dissolve

            pause 0.75

            scene v15s15_29a # FPP. Ms. Rose now in talking distance to MC, Ms. Rose smiling, mouth open
            with dissolve

            ro "So, how did you enjoy the meal, [name]?"

            scene v15s15_29b # FPP. Ms. Rose now in talking distance to MC, Ms. Rose smiling, mouth closed
            with dissolve

            menu:
                "Compliment":
                    $ add_point(KCT.BOYFRIEND)
                    $ add_point(KCT.BRO)
                    
                    u "I enjoyed it a lot more than I thought I would, actually. It might just be my new favorite meal. *Chuckles*"

                "Still angry":
                    $ add_point(KCT.TROUBLEMAKER)
                    
                    u "It was a good start, but I'm still not entirely happy with you."

            scene v15s15_29a
            with dissolve

            ro "Well, maybe I'll see you again soon? So I can serve you something... extra delicious?"

            scene v15s15_29b
            with dissolve

            u "Yeah, we'll see. I need to go now, I've got things to do."

            scene v15s15_29a
            with dissolve

            ro "Okay. Bye, [name]."

            scene v15s15_29b
            with dissolve

            u "Bye."

            scene v15s15_30 # TPP. Show MC leaving the dining room, Ms. Rose watching him leave, both smiling, mouths closed
            with dissolve

            pause 0.75

            # Scene 16
            scene v15s16_1a # TPP. Same as v15s16_1, MC slight smile, mouth closed.
            with dissolve

            u "(Phew! She drives me absolutely wild... Haha.)"

            scene v15s16_2a # TPP. Same as v15s16_2, MC slight smile, mouth closed.
            with dissolve

            u "(Something about mature women and their cougar-ish ways...)"

            scene v15s16_3a # TPP. Same as v15s16_3, MC slight smile, mouth closed.
            with dissolve

            u "(Okay, snap out of it, [name]. We've got a party to get to!)"

            scene v15s16_4a # TPP. Same as v15s16_4, MC stopped in place with his eyes open, MC slight smile, mouth closed.
            with dissolve

            u "(And a costume to find...)"

            scene v15s16_5a # TPP. Same as v15s16_5, MC worried smile, mouth closed.
            with dissolve

            u "(And a gift to buy... Fuck.)"

            stop music fadeout 3

            jump v15s17