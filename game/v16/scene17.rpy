# SCENE 17: Mc talks to Imre
# Locations: Street, bridge
# Characters: MC (Outfit: 5), IMRE (Outfit: 1)
# Time: Tuesday

label v16s17: # 17) MC catches up to Imre
    # -Imre walks along a street, onto a remote bridge. MC catches up to him 
    # (This scene's tone is drama with some humor. Slightly adjusted from original Miro outline, we need to avoid any suggestion of suicidal thoughts or making fun/being dismissive of suicidal thoughts)

    scene v16s17_1 # TPP Show Imre walking along the street, MC a ways behind him, rushing to catch up
    with fade

    pause 0.75

    scene v16s17_2 # TPP View over MC's shoulder from behind, ahead of him Imre is walking on to the remote bridge. MC's hand is up, waving to Imre
    with dissolve

    u "Imre, wait!"

    scene v16s17_3 # TPP Show MC next to Imre on the bridge. Imre has his hands on the stone railing, looking out, angry expression, mouth open
    with dissolve

    imre "It never works out!"

    scene v16s17_4 # FPP Imre looking at MC, angry expression, mouth open
    with dissolve

    imre "No matter what I do, it never works out! I'm sick of it."

    scene v16s17_4a # FPP Same angle as 4, Imre looking out over the side of the bridge, angry expression, mouth open
    with dissolve

    imre "She said no kissing on the first date."

    scene v16s17_4
    with dissolve

    imre "So, what the fuck was she doing making out with some random dude like that!?"

    scene v16s17_4b # FPP Same angle as 4, Imre looking at MC, angry expression, mouth closed
    with dissolve

    menu:
        "Support Imre":
            u "I don't know why she did it, but you can't blow up like this, Imre. Don't let her get to you."

            scene v16s17_4
            with dissolve

            imre "Ha! Easy for you to say. I'm the one who always gets shit on!"

            scene v16s17_4a
            with dissolve

            imre "I can't catch a fucking break."

        "Support Karen":
            scene v16s17_4b
            #with dissolve

            u "Well, don't take this personally, but..."

            u "You did try to shove a hotdog in her mouth, and she's vegan."

            scene v16s17_4
            with dissolve

            imre "So what? I make a mistake and she finds the first guy she can to lock lips with?"

            scene v16s17_4b
            with dissolve

            u "Maybe he was vegan too? That would've caught her attention."

            scene v16s17_4a
            with dissolve

            imre "What the fuck, [name]. Whose side are you on here?"

    # -Regardless of who you support-
    scene v16s17_4c # FPP Same angle as 4, Imre looking over the side of the bridge and slightly down, his expression more sad than angry, mouth open
    with dissolve

    imre "I could disappear so easily. No one would notice."

    scene v16s17_4a
    with dissolve

    imre "There wouldn't be any hot girls crying at my funeral, that's for sure..."

    scene v16s17_4b
    with dissolve

    u "Is that really what you're worried about? Hot girls being at your funeral?"

    scene v16s17_4c
    with dissolve

    imre "*Sighs*"

    scene v16s17_4d # FPP Same angle as 4, Imre looking at MC with a slight smile, mouth open
    with dissolve

    imre "I want a girl who's happy to eat my meat... Even if she's vegan, you know."

    scene v16s17_4e # FPP Same angle as 4, Imre looking at MC, neutral expression, mouth closed
    with dissolve

    u "(For fuck's sake...)"

    menu:
        "Be brutally honest":
            scene v16s17_4f # FPP Same angle as 4, Imre looking out over the side of the bridge, leaning over the stone rail (if possible), neutral expression, mouth closed
            with dissolve

            u "This is just another girl, that you don't actually like, but that you expected more from. Forget Karen, honestly. She's not even hot!"

            scene v16s17_4
            with dissolve

            imre "Uh- She was hot to me!"

            scene v16s17_4b
            with dissolve

            u "Give it a week. You'll feel fine."

            scene v16s17_4e
            with dissolve

            imre "..."

            scene v16s17_4f
            with dissolve
            
            u "Seriously, you'll forget about her as soon as you someone else who's hotter. *Laughs*"

            scene v16s17_4g # FPP Same angle as 4, Imre looking out over the side of the bridge, leaning over the stone rail (if possible), neutral expression, mouth open
            with dissolve

            imre "Maybe you're right. I don't know..."

            scene v16s17_3a # TPP Same angle as 3, Imre standing by the stone rail of the bridge, looking down at his hands on the rail, MC looking at him. Imre's mouth open
            with dissolve

            imre "I'm gonna head home. I uh, I need to think."

            scene v16s17_4e
            with dissolve

            u "Alright, we can-"

            scene v16s17_4c
            with dissolve

            imre "Nah, I need to be alone."

            scene v16s17_5 # FPP Show Imre walking away from the bridge
            with dissolve

            u "(Damn, I've never seen him down like this before. Did he really like her that much?)"

            u "*Sighs* (Let's go home.)"

        "Keep him calm":
            scene v16s17_4f
            with dissolve

            u "Come on, Imre."

            scene v16s17_4e
            with dissolve

            u "There's plenty of fish in SV Sea..."

            scene v16s17_4d
            with dissolve

            imre "*Scoffs*"

            scene v16s17_4e
            with dissolve

            u "C'mon you know that was good."

            scene v16s17_4f
            with dissolve

            imre "..."
            
            u "Seriously though, you have no idea. You might meet your future wife next week."

            scene v16s17_4g
            with dissolve

            imre "Yeah, I guess you're right..."

            scene v16s17_4f
            with dissolve

            u "Where's that Imre optimism?"

            scene v16s17_4g
            with dissolve

            imre "Okay, okay... I'll get my head back in the game."

            scene v16s17_4d
            with dissolve

            imre "I need to go to a party or something. Try out some new pick-up lines."

            scene v16s17_4i # FPP Same angle as 4, Imre looking at MC with a slight smile, mouth closed
            with dissolve

            u "That's the spirit. Now you sound like yourself again. *Laughs*"
            
            scene v16s17_6 # TPP Imre gives MC a "bro hug," (Imre's right shoulder to MC's right sholder) [similar to this: https://hhsadvocate.com/wp-content/uploads/2016/05/Screen-Shot-2016-05-02-at-10.40.52-AM.png or https://gifimage.net/wp-content/uploads/2017/07/bro-hug-gif-21.gif]
            with dissolve

            pause 0.75

            scene v16s17_4d
            with dissolve

            imre "Thanks for the chat, [name]."

            scene v16s17_4i
            with dissolve

            u "No problem."

            if joinwolves: # -if Wolves
                scene v16s17_4j # FPP Same angle as 4, Imre and MC still gripping each other's right hand from the bro hug, Imre with a slight smile, mouth open
                with dissolve

                imre "You're a brother for life, man. I'm glad you were here with me tonight."

                scene v16s17_4i
                with dissolve

                u "Haha, me too. It was kind of fun up until- Well, you know."

                scene v16s17_4d
                with dissolve

                imre "Haha, yeah, true."

                imre "Are you ready to head home?"

                scene v16s17_4i
                with dissolve

                u "Yeah, let's go."

                scene v16s17_4d
                with dissolve

                imre "Cool. *Sighs* Let's draw a fat line under this shit-show of a night..."

                scene v16s17_7 # TPP View from behind of MC and Imre walking away from the bridge together
                with dissolve

                pause 0.75

            else: # -if Apes
                scene v16s17_4d
                with dissolve

                imre "I don't know if I've said this before, but you're okay for a stinky Ape."

                scene v16s17_4i
                with dissolve

                u "Haha, thanks for the compliment."

                scene v16s17_4d
                with dissolve

                imre "I think I'm gonna head back alone and really think about things. Later, man."

                scene v16s17_4i
                with dissolve

                u "Yeah, see you, Imre. Good luck."

                scene v16s17_5
                with dissolve

                pause 0.75

    jump v16s18 # -Transition to Scene 18-