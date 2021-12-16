# SCENE 34: Autumn Announcement w/ Mud Wrestling
# Locations: Mud Wrestling Event / Campus
# Characters: MC (Outfit ?), Autumn (Outfit ?), Ms. Rose (Outfit ?), Deer Girl #1, Deer Girl #3, Perry (Outfit ?), Amber (Outfit ?), Riley (Outfit ?), Chloe (Outfit ?), Nora (Outfit ?)
# Characters cont.: Emily (Outfit ?), Chris (Outfit ?), Aaron (Outfit ?), Lindsey (Outfit ?), Ryan (Outfit ?), Random Guy
# Time: Day

label v10_autumn_announcement:
    scene v10samw1 # FPP. Show Autumn standing near the mud wrestling pool, smiling, mouth open.
    with dissolve
    stop music fadeout 3
    play music "music/v10/Track Scene 34.mp3" fadein 2

    aut "Alright everyone, if you could all gather around."

    scene v10samw2 # FPP. Show Ms. Rose, Deer girl 1 and Perry watching Autumn (not visible) make her announcement, all smiling, mouths closed.
    with dissolve

    pause 0.75

    scene v10samw1
    with dissolve

    aut "I want to first of all thank everyone for coming out. We really want to express our gratitude."

    aut "After a quick count we've already way surpassed our fundraising goal."

    aut "This means a lot to us, so thank you."

    scene v10samw3 # FPP. Show Deer girl 1 and 3, excited and smiling, mouth open as though cheering.
    with dissolve

    dg1 "Couldn't have done it without you Autumn!"

    dg3 "Yeah, cheers for Autumn!"

    scene v10samw1 
    with fade

    aut "Thanks everyone, means a lot. So our main event for today is of course the mud wrestling."

    scene v10samw4 # FPP. Same camera as v10samw4, smiling, mouth open as though yelling.
    with dissolve

    imre "LET'S GOOOOO!!!!"

    scene v10samw1
    with dissolve

    aut "Someone's excited! *Laughs*"

    scene v10samw1e # FPP, same 1 mouth closed.
    with dissolve

    ch "*Laughs*"

    guyd "*Laughs*"

    scene v10samw1
    with fade

    aut "Aside from myself, there will be one other commentator for the event. Everyone give a warm welcome to my friend, Aaron!"

    scene v10samw1b # FPP. Same camera as v10samw1. Show Autumn and Aaron, both smiling, mouths closed. Aaron is walking over to join her.
    with dissolve

    pause 0.75

    scene v10samw5 # TPP. Show MC and Chris, both clapping, smiling, Chris mouth open.
    with dissolve

    ch "That's my guy!"

    scene v10samw1
    with dissolve

    aut "The girls participating in the first matchup are Chloe and Nora!"


    scene v10samw2b # FPP. Same camera as v10samw2. Show Chris and Aaron talking to each other, both smiling, Chris mouth open.
    with dissolve

    pause 0.5

    scene v10samw6 # FPP. Show Chloe and Nora in the line-up of girls competing, both smiling, mouths closed.
    with fade
    menu:
        "Root for Chloe":
            $ chloe.points += 1
            $ nora.points -= 1
            $ add_point(KCT.BOYFRIEND)
            scene v10samw6 
            with dissolve
    
            u "Let's go Chloe!"

            if chloe.relationship.value <= Relationship.MAD.value: # chloe mad at mc
                scene v10samw7 # tpp. show mc hand in air mouth open
                with dissolve

                pause 0.75

            else: # chloe is not mad
                scene v10samw7
                with dissolve
                
                pause 0.75
        
        "Root for Nora":
            $ chloe.points -= 1
            $ nora.points += 1
            $ v10_cheerfornora = True
            scene v10samw6 
            with dissolve

            u "Let's go Nora!"

            li "Woohoo!"

            ro "Good luck Nora!"

    scene v10samw1
    with dissolve

    aut "The girls participating in the second matchup are Emily and Aubrey!"

    scene v10samw4d # FPP. Same camera as v10samw4. Show Ryan, a little smile, mouth closed. He looks like he's trying to get a good view.
    with dissolve

    pause 0.75

    scene v10samw6a # FPP. Same camera as v10samw6. Show Emily and Aubrey in the line-up of girls competing, both smiling, mouths closed.
    with fade
    menu:
        "Root for Aubrey":
            $ aubrey.points += 1
            scene v10samw7 
            with dissolve

            u "Okay Aubrey!"

        "Root for Emily":
            $ forgiveemily = True
            $ emily.points += 1
            $ add_point(KCT.BOYFRIEND)
            scene v10samw6a
            with dissolve

            u "Okay Emily!"
            
    scene v10samw1
    with dissolve

    aut "The girls participating in the final matchup are Amber and Riley!"

    scene v10samw6b # FPP. Same camera as v10samw6. Show Riley and Amber in the line-up of girls competing, both smiling, mouths closed.
    with fade
    menu:
        "Root for Riley":
            $ amber.points -= 1
            $ riley.points += 1
            $ add_point(KCT.BOYFRIEND)
            scene v10samw6b
            with dissolve

            u "Riley, Riley!"

            scene v10samw7
            with dissolve

            pause 0.75

        "Root for Amber":
            $ amber.points += 1
            $ riley.points -= 1

            scene v10samw7 
            with dissolve

            u "Amber, Amber!"

            aa "Did you see what that girl just did? She seems really into me." # random guy tag?

            scene v10samw2g # FPP. Same camera as v10samw2. Show a random guy talking to MC, smiling, mouth closed.
            with dissolve

            u "*Laughs* Sure buddy."
        
    scene v10samw1
    with fade

    aut "Please give a round of applause for all our participants."

    scene v10samw1d # FPP. Same camera as v10samw1. Show Autumn and Aaron standing side-by-side, both smiling, Aaron mouth open.
    with dissolve

    aa "I so graciously volunteered to deliver the bad... the rules."

    scene v10samw4
    with dissolve

    imre "Boo! No rules!"

    scene v10samw1d
    with dissolve

    aa "*Laughs* Okay, so the rules are pretty simple. No excessive moves such as biting, hair pulling, or choking."

    scene v10samw7g # FPP. Same camera as v10samw7. Show Amber smiling and laughing, mouth open.
    with dissolve

    am "Well damn, that's everything I like. *Chuckles*"

    scene v10samw1d
    with dissolve

    aa "*Laughs* Okay! There's also no removing of clothes."

    imre "Bro are you gay? What are these rules?"

    scene v10samw1d
    with dissolve

    aa "And the last one, no pushing out of the pool."

    scene v10samw1
    with dissolve

    aut "Alright, just so everyone knows, the participants submitted their own preferred matches. So with that said, let's get this going! Nora, Chloe?"

    scene v10samw8 # TPP. Same camera as v10samw8. Show Chloe and Nora in the pool, Choe smiling with her mouth open, Nora with her neutral expression, mouth closed.
    with dissolve

    cl "This is gonna be fun!"

    scene v10samw8a # TPP. Same camera as v10samw8. Show Chloe and Nora in the pool, Choe smiling with her mouth closed, Nora with her neutral expression, mouth open.
    with dissolve

    no "Oh shut up."
    stop music fadeout 3

    jump v10_chloe_vs_nora