# SCENE 5: MsRose at night outside the frat house
# Locations: Outside Frat House. 
# Characters: MC (Outfit: 1), Ms. Rose (Outfit: 1)
# Time: Night

label v16s5:
    scene v16s5_1 # TPP. Shot from behind of MC, MC walking towards Ms. Rose who is standing by a tree (FRAT HOUSE NOT SHOWN), Ms. Rose, neutral face, mouth closed.
    with dissolve

    pause 0.75

    scene v16s5_2 # FPP. MC standing infront of Ms. Rose, MC looking at Ms. Rose, Ms.Rose looking at MC, Ms.Rose neutral face, mouth closed [DO NOT SHOW FRAT HOUSE].
    with dissolve

    u "This is risky, Lorraine. You shouldn't be here."

    scene v16s5_2a # FPP. MC standing infront of Ms. Rose, MC looking at Ms. Rose, Ms. Rose looking at MC, Ms. Rose neutral face, mouth open [DO NOT SHOW FRAT HOUSE].
    with dissolve

    ro "I know, but I had to come see you."

    if v15_mad_at_ms_rose and not "v15_rose" in sceneList:
        scene v16s5_2a
        with dissolve

        ro "I know you've been angry with me."

        if v15_seduce_ms_rose:
            scene v16s5_2a
            with dissolve

            ro "But, when you came with Chloe to ask for my support, and you made those... promises to persuade me to sign, and I still don't know if you really meant it."
        
        ro "I just need to know... Do you want to keep seeing me? Or is this..."

        menu:
            "Of course I do":
                $ add_point(KCT.BOYFRIEND)
                scene v16s5_2
                with dissolve

                u "Yeah, I want to be with you, of course I do. Are you crazy?"

                scene v16s5_2a
                with dissolve
                
                ro "So, you forgive me...?"

                scene v16s5_2b # FPP. MC standing infront of Ms. Rose, MC looking at Ms. Rose, Ms. Rose looking at MC, Ms. Rose slight smile, mouth closed  [DO NOT SHOW FRAT HOUSE].
                with dissolve

                u "I could never hold anything against you to the point where I'd push you out of my life. I want you in it. Forgiven and forgotten."

                scene v16s5_3 # TPP. Show Ms. Rose with her arms wrapped around MC hugging him, One of her legs lifted back the generic happy lady hug (https://thumbs.dreamstime.com/z/close-up-couple-wearing-jeans-white-sneakers-standing-hugging-kissing-outdoors-park-romantic-young-girlfriend-124813754.jpg), Ms. Rose smile, mouth closed, MC slight smile, mouth closed  [DO NOT SHOW FRAT HOUSE].
                with dissolve

                pause 0.75

                scene v16s5_2c # FPP. MC standing infront of Ms. Rose, MC looking at Ms. Rose, Ms. Rose looking at MC, Ms. Rose slight smile, mouth open [DO NOT SHOW FRAT HOUSE].
                with dissolve

                ro "I'm so glad you said that. Because to celebrate that, I want to plan a little treat for us."

                scene v16s5_2
                with dissolve

                u "Does it involve spiking my drink again?"

                scene v16s5_2d # FPP. MC standing infront of Ms. Rose, MC looking at Ms. Rose, Ms. Rose looking at MC, Ms. Rose neutral face, rolling her eyes, mouth open [DO NOT SHOW FRAT HOUSE].
                with dissolve
                
                ro "*Sighs* No..." 

                scene v16s5_2b
                with dissolve

                u "*Laughs* So, what is it?"

                scene v16s5_2c
                with dissolve
                
                ro "There's a performance on Friday evening at the opera house that's just out of town. Do you know the one?"

                scene v16s5_2b
                with dissolve

                u "Yeah, sure. The guys and I go there all the time."

                scene v16s5_2e # FPP. MC standing infront of Ms. Rose, MC looking at Ms. Rose, Ms. Rose looking at MC, Ms. Rose confused, mouth open [DO NOT SHOW FRAT HOUSE].
                with dissolve
                
                ro "...Really?"

                scene v16s5_2b
                with dissolve

                u "No. I know absolutely nothing about the opera, haha."

                scene v16s5_2c
                with dissolve

                ro "*Laughs* It'll be fun. I promise."

                scene v16s5_2b
                with dissolve

                u "It sounds awfully public... I just want to make sure you don't get in any trouble."

                scene v16s5_2c
                with dissolve

                ro "Don't worry about that, I'll even get us a private balcony."

                scene v16s5_2b
                with dissolve

                u "Private balcony? That does sound kind of nice."

                u "(And incredibly fancy...)"

                scene v16s5_2c
                with dissolve

                ro "It will be extremely nice. I can't wait, but now I should go."

                scene v16s5_2b
                with dissolve

                u "Okay, sounds great. I'll see you soon."

                play sound "sounds/kiss.mp3"

                scene v16s5_4 # TPP. Show MC and Ms. Rose sharing a kiss.
                with dissolve

                pause 0.75

                scene v16s5_1a # TPP. Show MC walking the way he came from in v16s5_1, Ms. Rose in the background walking away from MC, MC neutral face, mouth closed [DO NOT SHOW FRAT HOUSE].
                with dissolve

                u "(Another day of dressing up and impressing ladies... Sign me up!)"

            "It's over":
                $ add_point(KCT.BRO)
                
                $ ms_rose.relationship = Relationship.FRIEND
                $ v16_ms_rose_breakup = True
                
                scene v16s5_2
                with dissolve

                u "I'm sorry, Lorraine. I'm just not feeling this anymore."

                scene v16s5_2f # FPP. MC standing infront of Ms. Rose, MC looking at Ms. Rose, Ms. Rose looking at the ground, Ms. Rose sad, mouth closed [DO NOT SHOW FRAT HOUSE].
                with dissolve

                ro "..."

                scene v16s5_2a
                with dissolve

                ro "So, you're saying it's over?"

                scene v16s5_2
                with dissolve

                u "Yeah, I just... I think we've come to the end of whatever this was."

                scene v16s5_2f
                with dissolve

                pause 0.75

                scene v16s5_2g # FPP. MC standing infront of Ms. Rose, MC looking at Ms. Rose, Ms. Rose looking at MC, Ms. Rose upset, Ms. Rose mouth open [DO NOT SHOW FRAT HOUSE].
                with dissolve

                ro "Oh. Okay... I understand." 
                
                ro "I guess it was just a casual thing that got out of hand, huh?"

                scene v16s5_2h # FPP. MC standing infront of Ms. Rose, MC looking at Ms. Rose, Ms. Rose looking at MC, Ms. Rose upset, Ms. Rose mouth closed [DO NOT SHOW FRAT HOUSE].
                with dissolve

                u "Yeah, some things got out of hand for sure."

                scene v16s5_2g
                with dissolve

                ro "Yeah, I'm sorry. I'd better go now."

                ro "Bye, [name]."

                scene v16s5_2h
                with dissolve

                u "Bye, Lorraine."

                scene v16s5_1a
                with dissolve

                u "(Breakups suck... Fuck.)"

                # [End of Checkpoint 1.1. Continues to Checkpoint 2]

    elif v15_threaten_ms_rose: 
        # [Checkpoint 1.2]
        scene v16s5_2a
        with dissolve

        ro "I still can't quite believe that you threatened me to support Chloe..."

        scene v16s5_2
        with dissolve

        u "I did what I had to do, Lorraine."

        scene v16s5_2g
        with dissolve
        
        ro "I can see now how little you think of me."

        scene v16s5_2h
        with dissolve

        u "But I-"

        scene v16s5_2g
        with dissolve

        ro "There's no point discussing this. You know what you did."

        ro "I've just come here to tell you this little 'arrangement' of ours is over."

        scene v16s5_2h
        with dissolve

        u "Lorraine..."

        scene v16s5_2g
        with dissolve

        ro "I simply can't trust you anymore, [name]. Ever again."

        scene v16s5_1a
        with dissolve

        u "(Did I just get dumped?)"

        menu:
            "Say sorry":
                $ add_point(KCT.BRO)
                scene v16s5_1b # TPP. MC and Ms. Rose walking away (only a few steps from MC) with their backs to each other. Close enough for Ms. Rose to hear MC, MC slight frown, looking at the ground, mouth open [DO NOT SHOW FRAT HOUSE].
                with dissolve

                u "I'm sorry, Lorraine. I really am."

                u "I hope one day you can forgive me."

            "Insult her":
                $ add_point(KCT.TROUBLEMAKER)
                scene v16s5_1c # TPP. MC and Ms. Rose walking away (only a few steps from MC) with their backs to each other. Close enough for Ms. Rose to hear MC, MC angry, looking at the ground, mouth open [DO NOT SHOW FRAT HOUSE].
                with dissolve

                u "Have fun finding someone your own age!"

        scene v16s5_1d # TPP. MC and Ms. Rose walking away from each other, further away from each other (increase distance), MC neutral face looking at the ground as he walks toward frat house [DO NOT SHOW FRAT HOUSE].
        with dissolve

        pause 0.75

        #[End of Checkpoint 1.2. Continues to Checkpoint 2]

    else:
    # [Checkpoint 1.3]

        scene v16s5_2c
        with dissolve

        ro "I've been really enjoying the time we spend together lately... and I want us to go somewhere a little different."

        scene v16s5_2b
        with dissolve

        u "Okay, I'm intrigued... What is it?"

        scene v16s5_2c
        with dissolve
        
        ro "There's a performance Friday evening at the Opera house. It's the one just out of town."

        menu:
            "Be excited":
                $ add_point(KCT.BOYFRIEND)
                scene v16s5_2b
                with dissolve

                u "I don't know anything about opera but, sounds different! I'm already looking forward to it."

                scene v16s5_2c
                with dissolve

                ro "I think it'll be a lot of fun; I love going. I'm gonna book a private balcony for us too."

                scene v16s5_2b
                with dissolve

                u "A private balcony? Lorraine!"
                
                scene v16s5_2c
                with dissolve

                ro "Only the best for my baby. *Laughs quietly*"

            "Be unsure":
                $ add_point(KCT.TROUBLEMAKER)
                scene v16s5_2b
                with dissolve

                u "Oh... Uhm, opera..."

                u "Yeah, I love opera! My favorite part is the... Uh..."

                u "The singing."

                scene v16s5_2c
                with dissolve

                ro "The singing?"

                scene v16s5_2b
                with dissolve

                u "The costumes are cool, I guess."

                scene v16s5_2c
                with dissolve

                ro "You've never been to the opera, have you?"

                scene v16s5_2b
                with dissolve

                u "*Sighs* No, never."

                scene v16s5_2c
                with dissolve

                ro "*Laughs* Don't worry, I promise it will be fun. I'll dress up nice for you and I'll book us a private area..."

                scene v16s5_5 # TPP. Shot of Ms. Rose playing with the Collar of MC's shirt, Ms. Rose flirty, mouth closed, MC slight smile, mouth closed [DO NOT SHOW FRAT HOUSE].
                with dissolve

                pause 0.75

                scene v16s5_2i # FPP. Ms. Rose close to MC's face biting her lip and playing with MC's collar [DO NOT SHOW FRAT HOUSE].
                with dissolve

                u "It's sounding much more interesting now, haha."

                scene v16s5_2j # FPP. Ms. Rose close to MC's face, playing with MC's collar, flirty face, mouth open [DO NOT SHOW FRAT HOUSE].
                with dissolve

                ro "Is it?"

                scene v16s5_2i
                with dissolve

                u "What can I say, you make everything interesting."

                scene v16s5_2j 
                with dissolve

                ro "Ha, well thank you."

        scene v16s5_2c
        with dissolve
        
        ro "You deserve it. I'll see you soon, okay?"

        scene v16s5_2b
        with dissolve

        u "Yeah, for sure."

        play sound "sounds/kiss.mp3"

        scene v16s5_4
        with dissolve

        pause 0.75

        scene v16s5_1a
        with dissolve

        u "(Well, that was an exciting, late-night, risky adventure... Seriously hope no one saw any of that, ha.)"

    #[End of Checkpoint 1.3. Continues to Checkpoint 2]

    #[Checkpoint 2]

    jump v16s4a