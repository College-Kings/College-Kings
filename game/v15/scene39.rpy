# SCENE 39: Lindsey's VIP night Sebastian or Grayson
# Locations: VIP BAR
# Characters: BAR WAITRESS (Outfit: 1), GRAYSON (Outfit: Nice Suit), MC (Outfit: 10), SEBASTIAN (Outfit: Nice Suit), LINDSEY (Outfit: 4), AUTUMN (Outfit: 3), AUBREY (Outfit: 8)
# Time: Night
# Render Count: Unique 26 Total 113

label v15s39:
    scene v15s39_1 # TPP. Lindsey, Mc, first in line followed by, Autmun, and Aubrey are shown entering the club, all slight smiles, all mouths closed, all looking forward towards the club entrance. Have them in a staggered formation so it's believable that other characters are possibly off screen because either grayson or sebastian can be in this scene. But at this point don't show grayson or sebastian
    with dissolve

    pause 0.75

    scene v15s39_2 # TPP. MC and Lindsey and the Bar Waitress (BW) is shown, Lindsey and BR slight smiles, mouths open, Mc slight smile mouth closed, The BW is leading them to a booth.
    with dissolve

    pause 0.75

    scene v15s39_3 # TPP. Order of seating location is as follows, MC on the outside seat of the booth, Lindsey next MC, Autumn next to Lindsey, Aubrey next to Autumn, and an open spot for either Grayson or Sebastian on the other outside seat, Don't show Grayson or Sebastian in this render, Mc and Lindsey are looking at each other Lindey slight smile mouth open, Mc slight smile, mouth closed lookiing at Lindsey, Aubrey Slight smile mouth open looking at Autumn, Autumn slight smile mouth closed
    with dissolve

    pause 0.75

    if v15_lindsey_inviteseb:
        scene v15s39_4a # FPP. Show Sebastian instead of Grayson, Aubrey looking at Sebastian slight smile mouth closed, Sebastian looking at Mc slight smile mouth closed.
        with dissolve

        pause 0.75

    else:
        scene v15s39_4 # FPP. Show Grayson sitting down next to Aubrey, with a cocky look, looking at Aubrey, mouth closed, Aubrey looking at Mc slight smile, mouth closed
        with dissolve

        pause 0.75

    scene v15s39_5 # FPP. Show the BW standing up looking down at Mc, slight smile, mouth is open
    with dissolve

    barworker "So happy to see you all tonight. Welcome to the Mango Lounge VIP area!"

    if v15_lindsey_alcohol:
        scene v15s39_5
        with dissolve

        barworker "We have a full range of drinks for you tonight, from beer to prosecco to tequila, even cocktails, all included in your VIP party package."

        scene v15s39_5
        with dissolve

        barworker "Just give me a few minutes and I'll be back with your glasses."

        if v15_lindsey_inviteseb:
            scene v15s39_7 # FPP. Mc looks directrly ahead and see's Sebastian, sitting in the booth, Sebastian looking at MC, slight smile, mouth open
            with dissolve

            se "Holy shit, so many choices. I'm definitely feeling extra special tonight, haha."

            scene v15s39_8 # FPP. Lindsey is sitting in the booth, looking towards the seating location where either Sebastian or Grayson will be sitting, don't show Sebastian or Grayson, slight smile, mouth is open
            with dissolve

            li "This must be what a VIP feels like all the time... Could you imagine?"

            scene v15s39_7a # FPP. same as v15s39_7 Sebastian is looking towards Lindsey's seating Location, don't show Lindsey, still a slight smile, mouth is still open
            with dissolve

            se "Haha, I guess you're right. What a life!"

        else:
            scene v15s39_6 # FPP. Mc looks directly ahead and see's Grayson, sitting in the booth, Grayson looking at MC, slight smile, mouth open
            with dissolve

            gr "Now that's what I call service!"

            scene v15s39_6a # FPP. same as v15s39_6 Grayson's mouth is closed, still looking at Mc, still a slight smile
            with dissolve

            u "Well, this is VIP. *Chuckles*"

            scene v15s39_6
            with dissolve

            gr "Yeah, I could get used to this."

    else:
        scene v15s39_5a # FPP. same as v15s39_5 BW has no expression, still looking at MC, mouth is still open
        with dissolve

        barworker "I've been informed that you're underage, so although we can't serve you our normal alcoholic line-up..."

        scene v15s39_5
        with dissolve

        barworker "We do have a wide range of juices and sodas, and we can also create mocktails."

        if v15_lindsey_inviteseb:
            scene v15s39_7b # FPP. same as v15s39_7 Sebastian is now looking at the BW's location, raised eyebrow, mouth is still open, still a slight smile
            with dissolve

            se "Mocktails, like cocktails, but no buzz?"

            scene v15s39_5d # FPP. same as v15s39_5b BW has a slight smile, Still looking at Sebastian/Grayson's position, Still don't show sebastian or Grayson, mouth is still open
            with dissolve

            barworker "Yes, exactly. We do have a wide range to choose from."

            scene v15s39_5c
            with dissolve

            u "That sounds great, I'll take one."

            scene v15s39_8a
            with dissolve

            li "Yeah, we all will! Just surprise us, haha."

            scene v15s39_5d
            with dissolve

            barworker "Very well! I'll be right back with your drinks."

        else:
            scene v15s39_6b # FPP. same as v15s39_6 Show Grayson looking up towards where the BW is standing, aggravated expression, mouth is still open
            with dissolve

            gr "Got any milk and cookies? *Scoffs* We're in college, lady, not kindergarten."

            scene v15s39_5b # FPP. same as v15s39_5 BW is looking towards Grayson/Sebastian's seating location, don't show sebastian or grayson, annoyed expression, mouth is open
            with dissolve

            barworker "Would you prefer a mocktail, sir?"

            scene v15s39_6b
            with dissolve

            gr "Mocktails?"

            scene v15s39_5b
            with dissolve

            barworker "They're cocktails without alcohol."

            scene v15s39_5c # FPP. same as v15s39_5 BW's mouth is closed, still a slight smile, still looking at MC
            with dissolve

            u "I like the sound of a mocktail. I'll have one, thanks."

            scene v15s39_8a # FPP. same as v15s39_8 Lindsey is now looking at the BW's location, still a slight smile, mouth is still open
            with dissolve

            li "Same for us girls."

            scene v15s39_6b
            with dissolve

            gr "So, basically juice and soda in a fancy glass?"

            scene v15s39_5b
            with dissolve

            barworker "...Yes. I'll be back in a bit."

    scene v15s39_8h # FPP. same as v15s39_8a Lindsey is now looking at MC, still a slight smile, mouth is still closed
    with dissolve

    li "Oh, and I... Need to go pay for this whole thing before I forget."

    li "I'll be right back."

    scene v15s39_9 # TPP. Show lindsey getting up from her seat and stepping over MC her ass is right in MC's face, Lindsey has a slight smile, mouth closed, Mc is smirking and looking slightly away from her ass, Autumn has a slight smile, hand covering her mouth looking at Lindsey, Aubrey is laughing looking at MC, Don't show Grayson or Sebastian
    with dissolve

    pause 0.75

    scene v15s39_10 # FPP. Mc looks back and see's Lindsey waving down the BW, Lindsey's back is turned, The BW has a slight smile, mouth closed looking at Lindsey
    with dissolve

    pause 0.75

    scene v15s39_11 # FPP. Show Autumn sitting in the booth, looking at MC, slight smile, mouth is open
    with dissolve

    aut "She's really pulling out all the stops for us tonight!"

    scene v15s39_12 # FPP. show Aubrey sitting in the booth, looking at Autumn's location slight smile, mouth is open
    with dissolve

    au "Yeah, isn't this great?! I feel like royalty..."

    scene v15s39_11a # FPP. same as v15s39_11 Autumn's mouth is closed, still looking at MC, still a slight smile
    with dissolve

    u "It's really important to her that you all have a great time tonight."

    scene v15s39_11
    with dissolve

    aut "Yeah, I'm sure this isn't cheap either."

    if v15_lindsey_inviteseb:
        scene v15s39_7c # FPP. same as v15s39_7 Sebastian is looking at Autumn's location, still a slight smile, mouth is still open
        with dissolve

        se "Are you kidding? The Wolves looked into booking this place."

        scene v15s39_7d # FPP. same as v15s39_7 Sebastian's mouth is closed, still looking at MC, still a slight smile
        with dissolve

        u "Really?"

        scene v15s39_7
        with dissolve

        se "Oh, yeah. I was on the phone for hours with these people trying to get a cheaper price. It's close to a thousand bucks."

        scene v15s39_7c
        with dissolve

        u "(Damn right it is.)"

        if not v15_lindsey_alcohol:
            scene v15s39_7
            with dissolve

            se "But since it's mocktails instead, it might have been cheaper."

    elif v15_lindsey_alcohol:
        scene v15s39_6c # FPP. same as v15s39_6 Grayson is looking at Autumn's location, still a slight snmile, mouth is still open
        with dissolve

        gr "A full line up of endless liquor? Ha, no. This is not cheap."

    else:
        scene v15s39_6d # FPP. same as v15s39_6b Grayson is looking at Autumns location, still aggravted expression, mouth is still open
        with dissolve

        gr "Endless mocktails? *Scoffs*"

        scene v15s39_6e # FPP. same as v15s39_6d Grayson has no expression, still looking at Autumn's location, mouth is still open
        with dissolve

        gr "It's a really nice place though, so yeah. You're probably right."

        scene v15s39_6a
        with dissolve

        u "Exactly, it wasn't pocket change, that's for damn sure. But as long as we all have a great time, it'll be worth it."

    if v15_lindsey_inviteseb:
        scene v15s39_3e # same as v15s39_3a Sebastian instead of Grayson
        with dissolve

        pause 0.75

        scene v15s39_3f # same as v15s39_3e Sebastian instead of Grayson
        with dissolve

        pause 0.75

    else:
        scene v15s39_10a # same as v15s39_10 Lindsey is walking back to the table slight smile, mouth is closed, The BW is seen walking behind her carrying the drinks, slight smile, mouth is closed
        with dissolve

        pause 0.75

        scene v15s39_3a # same as v15s39_3 Show MC, Lindsey, Autumn, Aubrey, and Grayson sitting down from left to right, all of them have a fancy glass drink in their hand, all slight smiles, all mouths are open, all raising the glass towards the center of the table, Their table also now has a full range of glasses, bottles, ice buckets,
        with dissolve

        pause 0.75

        scene v15s39_3b # same as v15s39_3a Show Mc mouth open talking to Autumn, slight smiles, Autumn's is looking at Mc mouth is closed, Show Grayson mouth open talking to Aubrey and Lindesey, All slight smiles, Aubrey and Lindsey's mouths are closed looking at Grayson
        with dissolve

        pause 0.75

        scene v15s39_3c # same as v15s39_3b Show Lindsey talking to Mc mouth is open, MC slight smile mouth is closed, Show Autumn mouth open talking Aubrey, slight smiles, Aubrey's mouth is closed, Show Grayson pounding down another drink
        with dissolve

        pause 0.75

        if v15_lindsey_alcohol:
            scene v15s39_3d # same as v15s39_3a render is exactly the same except instead of fancy glasses they all have shot glasses
            with dissolve

            pause 0.75

    scene v15s39_8
    with dissolve

    u "(Tonight seems to be going well, but Lindsey hasn't mentioned anything about getting their support...)"

    scene v15s39_8c # FPP. same as v15s39_8b Lindsey's mouth is closed, still a smile, still looking at MC, Lindsey leans into listen to Mc
    with dissolve

    u "*Whispers* Hey. Lindsey. This might be a good time to talk about your campaign."

    scene v15s39_8u
    with dissolve

    li "Oh shit, yeah. Good idea!"

    scene v15s39_8
    with dissolve

    li "Hey, everyone... I just want to talk about something serious real quick, and then we can get straight back into having fun, okay?"

    if v15_lindsey_inviteseb:
        scene v15s39_7a
        with dissolve

        se "If it's about supporting you, you know you've got my vote."

        scene v15s39_8
        with dissolve

        li "Ha. Thanks, Seb."

        scene v15s39_7c
        with dissolve

        u "(So, they are really, really good friends. Interesting...)"

    else:
        scene v15s39_6f # FPP. same as v15s39_6b Grayson is looking at Lindsey, still aggravated, mouth is still open.
        with dissolve

        gr "Here we go... *Sighs* The hard and long sales pitch."

        scene v15s39_11b # FPP. same as v15s39_11 Autumn is looking at Sebastian/Grayson's location, no expression, mouth is open
        with dissolve

        aut "Just listen to what she has to say, Grayson. We've all been in her shoes at some point."

        scene v15s39_6f
        with dissolve

        gr "My ears are open, aren't they?"

    scene v15s39_8d # FPP. same as v15s39_8 Lindsey has no expression, mouth is still open, still looking at Sebastian/Grayson's location
    with dissolve

    li "You're right, it is about supporting me. That's the ultimate reason why I brought you all here to enjoy the night with me."

    li "I just want to ask, what has Chloe ever done for you?"

    li "Like, what has she ever actually done for you, herself?"

    if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
        scene v15s39_8b
        with dissolve

        u "Come on, guys..."

        if v15_lindsey_inviteseb:
            scene v15s39_3j # FPP. same as v15s39_3e for seating locations only, Show Mc Lindsey, Autumn, Aubrey and Sebastian from left to right all looking at each other awkwardly, all mouths are closed
            with dissolve

            pause 0.75

        else:
            scene v15s39_6g # FPP. same as v15s39_6f Grayson is looking at MC, still aggravated expression, mouth is still open
            with dissolve

            gr "Man... Chloe, Chloe, Chloe... Do people ever shut up about her?"

            scene v15s39_6g
            with dissolve

            gr "You know what? I'm not in the mood. I'm out of this one, you are hereby muted."

            scene v15s39_13 # FPP. Show the BW walking by, her back is turned and doesn't see Grayson, Grayson is checking out her ass, slight smile, mouth is closed, Aubrey is seen looking at Grayson with disgust in her face.
            with dissolve

            pause 0.75

            scene v15s39_12b # FPP. same as v15s39_12 Aubrey is looking at Grayson/Sebastian's location, slightly angry, mouth is open
            with dissolve

            au "Such a dick..."

            scene v15s39_3i # FPP. same as v15s39_3a for seating locations only, Show MC, Lindesey, Autumn, Aubrey, and Grayson from left to right all looking at each other awkwardly, all mouths are closed
            with dissolve

            pause 0.75

        scene v15s39_8d
        with dissolve

        li "It's just a question to prove a point, that's all."

    if v15_lindsey_inviteseb:
        scene v15s39_7e # FPP. same as v15s39_7a Sebastian has no expression, still looking at Lindsey, mouth is still open
        with dissolve

        se "I can't really comment. I don't know her well, we don't talk much. So technically, nothing."

        scene v15s39_8
        with dissolve

        li "Okay. That's fair. I won't even consider you then if that's okay. Haha."

        scene v15s39_7a
        with dissolve

        se "Ha, fair. I have nothing to say about Chloe, but at least a couple of good things to list about you."

        scene v15s39_8
        with dissolve

        li "Wow, thanks. *Chuckles*"

    if v15_chloe_lindseysabotage:
        scene v15s39_12a
        with dissolve

        u "(This would be a good time to try and record Lindsey saying something extra bitchy about Chloe. Hopefully I can catch something useful.)"

        scene v15s39_14 # TPP. Close up shot of MC pulling out his phone to one side, taps on it
        with dissolve

        pause 0.75

        scene v15s39_14a # TPP. same as v15s39_14 MC then puts his phone in his pocket again
        with dissolve

        u "(Okay, it's recording... If I'm careful, maybe I can try to trick her into saying something.)"

    scene v15s39_8e # FPP. same as v15s39_8d Lindsey is now looking at Aubrey, still no expression, mouth is still open
    with dissolve

    li "Well, what do you girls think?"

    scene v15s39_11c # FPP. same as v15s39_11b Autumn is now looking at Lindsey, no expression, mouth is still open
    with dissolve

    aut "Chloe's been good to me. She's helped me out with a few things in the past, but... Well, nothing lately."

    aut "I've invited her to participate in some of the Deer events, but she always bails. *Chuckles* Not even a message to say sorry usually."

    scene v15s39_12c # FPP. same as v15s39_12 Aubrey is now looking at Lindsey, no expression, mouth is still open
    with dissolve

    au "She is the type of person who makes a lot of promises. She tries to please everyone."

    scene v15s39_8e
    with dissolve

    li "Yeah, but she doesn't seem to follow through with those promises, does she?"

    scene v15s39_11c
    with dissolve

    aut "Not lately... But that doesn't mean she's a bad person."

    scene v15s39_8e
    with dissolve

    li "I'm not saying she's a bad person. I just don't think she's capable of doing the job that she's supposed to be doing."

    if v15_lindsey_inviteseb:
        scene v15s39_3l # TPP. same as v15s39_3k Sebastian instead of Grayson
        with dissolve

        pause 0.75

    else:
        scene v15s39_3k # TPP. same as v15s39_3i for seating locations only, Show MC, Lindesey, Autumn, Aubrey, and Grayson from left to right all looking at Lindsey no expressions mouths are closed, Lindsey is looking in the general direction of the group, Lindsey's mouth is open no expression
        with dissolve

        pause 0.75

    scene v15s39_8e
    with dissolve

    li "That's the whole reason behind why I'm challenging her, it's nothing personal."

    li "I just think she should be doing more as our President."

    scene v15s39_12c
    with dissolve

    au "You're right. She should be doing more."

    scene v15s39_8f # FPP. same as v15s39_8f Lindsey is now looking at Autumn, still no expression, mouth is still open
    with dissolve

    li "The Chicks' President should be supporting you at all your events, Autumn. Wouldn't you prefer that?"

    scene v15s39_11c
    with dissolve

    aut "Yeah, of course I would."

    scene v15s39_8f
    with dissolve

    li "I want to create an environment where we can rely on each other."

    scene v15s39_8f
    with dissolve

    li "To me, supporting other sororities benefits everyone, and that's why we're all here, right?"

    scene v15s39_8c
    with dissolve

    u "Mhmm. *Chuckles*"

    scene v15s39_8
    with dissolve

    li "We all want our experiences to be the best they can be."

    scene v15s39_8g # FPP. same as v15s39_8f Lindsey has a slight smile, still looking at Autumn, mouth is still open
    with dissolve

    li "We can maintain healthy rivalries or whatever, but we need to be there for each other. And Chloe doesn't seem to get that."

    scene v15s39_11c
    with dissolve

    aut "I do see where you're coming from..."

    scene v15s39_12c
    with dissolve

    au "I've been trying to stay out of this whole thing as much as possible... Really."

    au "But I have to agree with you on this, Lindsey. You make some valid points."

    scene v15s39_8h # FPP. same as v15s39_8g Lindsey is looking at Aubrey, still a slight smile, mouth is still open
    with dissolve

    li "Thank you. I really appreciate you saying that, Aubrey."

    if v15_chloe_lindseysabotage:
        if v15_lindsey_alcohol:
            scene v15s39_8e
            with dissolve

            u "(If Lindsey was more drunk, she'd be more likely to let something slip. Shots?)"

            menu:
                "Shots!":
                    $ add_point(KCT.TROUBLEMAKER)

                    if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                        $ add_point(KCT.BOYFRIEND)

                    scene v15s39_8b
                    with dissolve

                    u "Let's do some shots!"

                    scene v15s39_11
                    with dissolve

                    aut "Ha."

                    scene v15s39_8i # FPP. same as v15s39_8b Lindsey has no expression, still looking at MC, mouth is still open
                    with dissolve

                    li "We're kind of in the middle of something here, [name]."

                    scene v15s39_8j # FPP. same as v15s39_8i Lindsey's mouth is closed, still looking at MC, still no expression
                    with dissolve

                    u "Yeah, but... Come on, let's lighten the mood a bit!"

                    scene v15s39_15 # TPP. show just MC, Lindsey and Autumn, Mc is pouring shots slight smile mouth is closed, Lindsey and Autumn are looking at MC Lindsey has no expressions, Autumn is slightly smiling, both of their mouth's are closed
                    with dissolve

                    pause 0.75

                    scene v15s39_15a # TPP. same as v15s39_15 Lindsey is looking at Autumn her mouth is open no expression, Autumn is looking at Lindsey slight smile mouth is closed, Mc has grabbed another sized bottle with the same color liquid to pour into Lindsey's drink still slight smile mouth is still closed
                    with dissolve

                    u "(And something with a bit more punch for Lindsey...)"

                    scene v15s39_8i # FPP. same as v15s39_8j Mc is handing Lindsey a drink, Lindsey is still looking at MC, still no expression, mouth is still open
                    with dissolve

                    li "I'm already buzzed, [name]. I don't think I can handle another shot, haha."

                    scene v15s39_12d # FPP. same as v15s39_12a Aubrey has a slight smile, mouth is open, still looking at MC
                    with dissolve

                    au "I'd like one, please!"

                    scene v15s39_8j
                    with dissolve

                    u "Come on, Linds. One more won't hurt, right?"

                    scene v15s39_11d # FPP. same as v15s39_11c Autumn has a slight smile, still looking at Lindsey, mouth is still open
                    with dissolve

                    aut "You did say you were to have a great night..."

                    scene v15s39_11e # FPP. same as v15s39_11d Autumn has a smirk on her face, mouth is closed, still looking at Lindsey
                    with dissolve

                    pause 0.75

                    scene v15s39_8g
                    with dissolve

                    li "Okay, fine! Haha, one more then I'm done."

                    if v15_lindsey_inviteseb:
                        scene v15s39_3h
                        with dissolve

                        u "Cheers!"

                        scene v15s39_3n # FPP. same as v15s39_3h they all drink their shots
                        with dissolve

                        pause 0.75

                    else:
                        scene v15s39_3d
                        with dissolve

                        u "Cheers!"

                        scene v15s39_3m # FPP. same as v15s39_3d they all drink their shots
                        with dissolve

                        pause 0.75

                    scene v15s39_8g
                    with dissolve

                    li "Ugh... Okay, now what was I saying?"

                    u "(Now is the time to strike if we're gonna do this...)"

                    menu (fail_label="v15_change_subject"): 
                        "Change subject":
                            label v15_change_subject:
                            
                            $ add_point(KCT.BRO)

                            if hangOutWithLindsey:
                                $ add_point(KCT.BOYFRIEND)

                            if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                                $ add_point(KCT.TROUBLEMAKER)

                            scene v15s39_8c
                            with dissolve

                            u "Um, dancing?"

                            scene v15s39_8p
                            with dissolve

                            li "Ooh! Shall we go and dance now?"

                            scene v15s39_11
                            with dissolve

                            aut "Yeah, that's a great idea. I need to move! *Laughs*"

                            scene v15s39_12
                            with dissolve

                            au "Let's hit the dance floor, then."

                            if not v15_lindsey_inviteseb:
                                scene v15s39_6c
                                with dissolve

                                gr "You ladies hit the dance floor. I'll hit another drink..."

                                scene v15s39_12e # FPP. same as v15s39_12b Aubrey has a slight smile, still looking Grayson/Sebastian's location, mouth is still open
                                with dissolve

                                au "You're so lame!"

                            scene v15s39_8c
                            with dissolve
                            
                            pause 0.75

                        "Stay on topic":
                            $ add_point(KCT.TROUBLEMAKER)
                            $ v15_stay_on_topic = True

                            if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                                $ add_point(KCT.BOYFRIEND)

                            scene v15s39_8c
                            with dissolve

                            u "You were telling us what you don't like about Chloe. *Laughs*"

                            scene v15s39_8b
                            with dissolve

                            li "*Drunk* What I don't like about Chloe?"

                            scene v15s39_8c
                            with dissolve

                            u "Yeah. What annoys you about her?"

                            scene v15s39_12f # FPP. same as v15s39_12a Aubrey looks at MC with a concerned expression, mouth is still closed
                            with dissolve

                            pause 0.75

                            scene v15s39_8l # FPP. same as v15s39_8i Lindsey has an annoyed expression, still looking at MC, mouth is still open
                            with dissolve

                            li "*Drunk* What doesn't annoy me? Everything about her is annoying."

                            scene v15s39_8b
                            with dissolve

                            $ set_presidency_percent(v14_lindsey_popularity - 3)

                            li "*Drunk* She gets everything handed to her, even her fucking boobs!"

                            scene v15s39_12g # FPP. same as v15s39_12f Aubrey is now looking at Lindsey, mouth is open, still with a concerned expression
                            with dissolve

                            au "Hey, I think that's enough-"

                            scene v15s39_8m # FPP. same as v15s39_8b show Lindsey drinking from another glass, facing MC
                            with dissolve

                            pause 0.75

                            scene v15s39_12h # FPP. same as v15s39_12f Aubrey mouth is closed, is still looking at Lindsey, still with a concerned expression
                            with dissolve

                            pause 0.75

                            scene v15s39_12f
                            with dissolve

                            pause 0.75

                            scene v15s39_8b
                            with dissolve

                            $ set_presidency_percent(v14_lindsey_popularity - 3)

                            li "*Drunk* I mean no wonder she's such a bitch all the time..."

                            menu (fail_label="v15_stop_lindsey"):
                                "Stop Lindsey":
                                    label v15_stop_lindsey:
                                    
                                    $ add_point(KCT.BRO)

                                    if hangOutWithLindsey:
                                        $ add_point(KCT.BOYFRIEND)

                                    if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                                        $ add_point(KCT.TROUBLEMAKER)

                                    scene v15s39_8n # FPP. same as v15s39_8b Lindsey appears drunk, her face is flushed, she now has a full smile, mouth is still closed, still looking at MC
                                    with dissolve

                                    pause 0.75

                                    scene v15s39_8n
                                    with dissolve

                                    u "Lindsey, maybe take it easy. You've had a lot to drink, haha."

                                    scene v15s39_8o # FPP. same as v15s39_8n Lindsey is now looking at Aubrey, mouth is open, is slightly sad/concenred, still drunk appearance
                                    with dissolve

                                    $ set_presidency_percent(v14_lindsey_popularity + 3)

                                    li "*Drunk* Oh. Oh, yeah, I'm so sorry. That must have sounded so bitchy. Sorry, everyone."

                                    scene v15s39_11d
                                    with dissolve

                                    aut "I have an idea. Let's go dance."

                                    scene v15s39_12
                                    with dissolve

                                    au "That's an amazing idea."

                                    scene v15s39_8p # FPP. same as v15s39_8o Lindsey raises her arms in the air with excitement, full smile, still looking at Aubrey, mouth is still open, still drunk appearance
                                    with dissolve

                                    li "*Drunk* Yeah, okay, let's go dance! Wooo!"

                                "Say nothing":
                                    $ add_point(KCT.TROUBLEMAKER)
                                    $ v15_say_nothing = True

                                    if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                                        $ add_point(KCT.BOYFRIEND)

                                    scene v15s39_8n # FPP. same as v15s39_8b Lindsey appears drunk, her face is flushed, she now has a full smile, mouth is still closed, still looking at MC
                                    with dissolve

                                    pause 0.75

                                    scene v15s39_8q # FPP. same as v15s39_8n Lindsey's mouth is open, annoyed expression, still looking at Mc, still drunk appearance
                                    with dissolve

                                    li "*Drunk* She's constantly worried about losing her free ride to a degree."

                                    scene v15s39_8r # FPP. same as v15s39_8n Lindsey's mouth is open, still a full smile, still looking at MC, still drunk appearance
                                    with dissolve

                                    li "*Drunk* Without the President's scholarship, she'd have to sell all of that plastic back to the surgeons... *Laughs*"

                                    if v15_lindsey_inviteseb:
                                        scene v15s39_7d
                                        with dissolve

                                        se "Li-lindsey..."

                                        scene v15s39_8s # FPP. same as v15s39_8q Lindsey is looking at Sebastian/Grayson's location, still annoyed, mouth is still open, still a drunk appearance
                                        with dissolve

                                        li "*Drunk* What?"

                                        scene v15s39_7f # FPP. same as v15s39_7d Sebastian has a worried/concerned expression, still looking at Lindsey, mouth is still open
                                        with dissolve

                                        se "It's not like you to say something like that, ha. Come on..."

                                        scene v15s39_8o
                                        with dissolve

                                        li "*Drunk* Oh, shhhit... You're right! I'm so sorry, you guys. I-"

                                        li "That was so rude of me..."

                                        scene v15s39_11f # FPP. same as v15s39_11c Autumn has a worried/concenred expression, still looking at Lindsey, mouth is still open
                                        with dissolve

                                        aut "It's... It's okay. We all say things we don't mean sometimes."

                                        scene v15s39_12g
                                        with dissolve

                                        au "Stress and alcohol really don't mix well together, girl. *Chuckles*"

                                        scene v15s39_8t # FPP. same as v15s39_8o Lindsey has an embarrssed expression, holding her hands over her mouth, still looking at Aubrey, mouth is still open
                                        with dissolve

                                        pause 0.75

                                    else:
                                        scene v15s39_6h # FPP. same as v15s39_6f Grayson has a full smile, raising a fist in the air as in acceptance of what Lindsey said, still looking at Lindsey, mouth is still open
                                        with dissolve

                                        gr "Haha, holy fuck! Go Lindsey! That's hilarious, I love it... *Laughs*"

                                    scene v15s39_8t
                                    with dissolve

                                    u "(Fuck, that was amazing! Thank you, Lindsey. Chloe's going to be ecstatic.)"

                                    scene v15s39_11f
                                    with dissolve

                                    aut "I think it's probably a good time to hit the dance floor... No?"

                                    scene v15s39_12
                                    with dissolve

                                    au "Yes, please!"

                                    scene v15s39_8t
                                    with dissolve

                                    li "*Drunk* Yes, that's a great idea! Let's go... Woohoo!"

                "Don't mention it":
                    $ add_point(KCT.BRO)
                    if hangOutWithLindsey:
                        $ add_point(KCT.BOYFRIEND)

                    scene v15s39_8c
                    with dissolve

                    u "(On second thought, that's just not my style...)"

        else:
            scene v15s39_8e
            with dissolve

            u "(This is going to be difficult without alcohol. I can try to trick Lindsey but... I'll be seriously surprised if she slips up while sober.)"

            scene v15s39_8c
            with dissolve

            menu:
                "Try to trick her":
                    $ add_point(KCT.TROUBLEMAKER)

                    if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                        $ add_point(KCT.BOYFRIEND)

                    scene v15s39_8c
                    with dissolve

                    u "Lindsey, be honest. What do you hate most about Chloe?"

                    scene v15s39_12i # FPP. same as v15s39_12f Aubrey has a disgusted expression, mouth is open, still looking at Mc
                    with dissolve

                    pause 0.75

                    scene v15s39_8b
                    with dissolve

                    li "Haha, I don't hate her, [name]. Chloe's a Chick and will always be a sorority sister."

                    scene v15s39_8i
                    with dissolve

                    li "She's my rival right now, sure, but... I don't hate her."

                    scene v15s39_12j # FPP. same as v15s39_12 Aubrey is looking at Lindsey, still a slight smile, mouth is still closed
                    with dissolve

                    pause 0.75

                    scene v15s39_11e
                    with dissolve

                    pause 0.75

                    if v15_lindsey_inviteseb:
                        scene v15s39_7a
                        with dissolve

                        pause 0.75

                    else:
                        scene v15s39_6f
                        with dissolve

                        pause 0.75

                    scene v15s39_8c
                    with dissolve

                    u "Not even a little bit?"

                    scene v15s39_12k # FPP. same as v15s39_12i Aubrey raises her hands in a questioning manner, still a disgusted expression, still looking at Mc, mouth is still open
                    with dissolve

                    au "[name]."

                    scene v15s39_12f
                    with dissolve

                    u "(Sorry Aubrey... I'm trying to start a storm here.)"

                    if kct == "popular":
                        call screen kct_popup

                        scene v15s39_8c
                        with dissolve

                        li "What do you want me to say? That she gets everything handed to her?"

                        $ set_presidency_percent(v14_lindsey_popularity - 3)

                        li "Or that the only reason she wants to be President is because she can't afford tuition?"

                        scene v15s39_8u # FPP. same as v15s39_8c Lindsey shrugs her shoulders, increases to a full smile, still looking at MC, mouth is still open
                        with dissolve

                        li "Why would I say any of that, [name]? Haha..."

                        scene v15s39_12g
                        with dissolve

                        au "Wow, ha."

                        scene v15s39_11h # FPP. same as v15s39_11f Autumn is looking at Lindsey with a disapointed expression, mouth is closed
                        with dissolve

                        pause 0.75

                        scene v15s39_12l # FPP. same as v15s39_12g Aubrey is looking at Lindsey with a disappointed expression, mouth is closed
                        with dissolve

                        pause 0.75

                        if v15_lindsey_inviteseb:
                            scene v15s39_7g # FPP. same as v15s39_7e Sebastian has a disappointed expression, still looking at Lindsey, mouth is closed
                            with dissolve
                            
                            pause 0.75

                        else:
                            scene v15s39_6j # FPP. same as v15s39_6i Grayson has a pleased smirk on his face, not holding any drinks, still looking at Lindsey, mouth is still closed
                            with dissolve
                            
                            pause 0.75

                        scene v15s39_8c
                        with dissolve

                        u "I don't know... but you kind of just did. *Chuckles*"

                        scene v15s39_8
                        with dissolve

                        li "Yeah, but I didn't mean it, ha. It was just a joke, guys."

                        if not v15_lindsey_inviteseb:
                            scene v15s39_6k # FPP. same as v15s39_6 Grayson is looking at Lindsey has a full smile, mouth is open
                            with dissolve

                            gr "A really fucking good one too. *Laughs*"

                    else:
                        scene v15s39_8b
                        with dissolve

                        li "No. I don't... Now stop asking provocative questions, haha."

                        scene v15s39_8c
                        with dissolve

                        u "(*Sighs* That didn't work.)"

                    scene v15s39_12j
                    with dissolve

                    au "Can we stop talking about this now and go dance?"

                    scene v15s39_11g
                    with dissolve

                    aut "Yes, please!"

                    scene v15s39_8e
                    with dissolve

                    li "Oh, okay... Sure. A dance sounds good."

                "Don't risk it":
                    $ add_point(KCT.BRO)

                    if chloe.relationship.value >= Relationship.GIRLFRIEND.value:
                        $ add_point(KCT.TROUBLEMAKER)

                    if hangOutWithLindsey:
                        $ add_point(KCT.BOYFRIEND)

                    scene v15s39_8c
                    with dissolve

                    u "(I don't think it's even worth trying. She really needs to be drunk.)"

                    scene v15s39_12d
                    with dissolve

                    au "I think we've talked enough for now... Can we go dance?"

                    scene v15s39_11g # FPP. same as v15s39_11 Autumn is looking at Aubrey, still a slight smile, mouth is still open
                    with dissolve

                    aut "I'm so ready for a dance, yes!"

                    scene v15s39_8g
                    with dissolve

                    li "Okay, let's groove!"

                    if not v15_lindsey_inviteseb:
                        scene v15s39_6i # FPP. same as v15s39_6g Grayson has a drink in each hand, still looking at Lindsey, still a full smile
                        with dissolve

                        gr "Don't be surprised if there's no drinks left when you get back, haha."

    if not v15_chloe_lindseysabotage:
        scene v15s39_12
        with dissolve

        au "Of course... And now that you've won us all over, can we talk about something else? Or go for a dance?"

        scene v15s39_11g
        with dissolve

        aut "Oh, yeah! A dance sounds good to me."

        scene v15s39_8g
        with dissolve

        li "Okay, let's live this VIP experience to the fullest!"

    if v15_lindsey_inviteseb:
        scene v15s39_16 # TPP. Show Aubrey leading the way to the dance floor, her back is to the dance floor facing Lindsey and Autumn, holding a hand of both Autumn and Lindsey one in each hand above her head, all the girls have slight smiles, Aubreys mouth is open, looking at both Lindsey and Autumn, Lindsey and Autumns mouths are slightly open looking at Aubrey, Mc is following behind slight smile, mouth is closed, Sebastian is walking next to Mc, slight smile, mouth is closed
        with dissolve

        pause 0.75

        scene v15s39_17 # TPP. Show Aubrey, Autumn and Lindsey dancing with each other, all full smiles, mouths open or closed up to the renderer's decision
        with dissolve

        pause 0.75

        scene v15s39_18 # TPP. Show Sebastian is dancing with Lindsey full smile mouth open, Lindsey is dancing with Sebastian full smile mouth open, Show Aubrey and twerking on Mc full smile mouth is open looking back at Autumn laughing with a hand slightly over her mouth, Autumn is holding Mc's hands behind his back in a playful manner so he can't touch Aubrey she has a full smile mouth is closed looking at Mc, Mc is looking back at Autumn with a smirk on his
        with dissolve

        pause 0.75

        scene v15s39_19 # TPP. show Mc and Autumn dancing together full smiles mouths open, Show Sebastian sandwiched between Lindsey and Aubrey as they dance seductively on him, Sebastian has a full smile mouth open looking at either Aubrey or Lindsey
        with dissolve

        pause 0.75

        scene v15s39_20 # TPP. Show Sebastian, MC, Lindsey, Aubrey, and Autumn, meeting up at the table for one last drink, show the fancy glasses in their hands, they cheers the glasses, all slight smiles, all mouths open
        with dissolve

        pause 0.75

    else:
        scene v15s39_16a # TPP. same as v15s39_16 Sebastian is not in the render
        with dissolve

        pause 0.75

        scene v15s39_17
        with dissolve

        pause 0.75

        scene v15s39_18a # TPP. same as v15s39_18 Lindsey is dancing in front of Aubrey looking at Mc and laughing full smile
        with dissolve

        pause 0.75

        scene v15s39_21 # TPP. Show Grayson sitting alone at the booth checking out the BW bending over another table she is serving he is biting his fist full smile
        with dissolve

        pause 0.75

        scene v15s39_22 # TPP. same as v15s39_21 The BW turns around and see's Grayson checking her out she has a disgusted look on her face, he has a cocky expression looking at her full smile
        with dissolve

        pause 0.75

        scene v15s39_20a # TPP. Show Grayson instead of Sebastian
        with dissolve

        pause 0.75

    scene v15s39_23 # TPP. MC exits the club. Lindsey and Aubrey are ahead of him, getting into the limo
    with dissolve

    $ set_presidency_percent(v14_lindsey_popularity + 5)

    u "(So, that's what it's like to be a VIP, huh? I could get used to that...)"

    if v15_lindsey_alcohol:
        scene v15s39_23
        with dissolve

        u "(We got lucky with the alcohol, too.)"

    else:
        scene v15s39_23
        with dissolve

        u "(Still sucks that we couldn't get drunk, but you can't win 'em all, ha.)"

    if v15_chloe_lindseysabotage:
        if v15_lindsey_inviteseb:
            scene v15s39_24 # TPP. Show Sebastian being a gentlemen holding Autumns hand and helping Autumn into the Limo looking at Autumn slight smile mouth open, Autumn looking back at Sebastian slight smile mouth closed, Mc is taking his phone out of his pocket looking at his phone slight smile mouth is closed
            with dissolve

            u "(Just need to send the recording to Chloe... Hopefully she can find something to do with it.)"

            scene v15s39_25 # FPP. Close up shot of Mc's phone it shows Chloe as the person he has messaged, and a "message sent" text appears on his phone
            with dissolve

            pause 0.75

        else:
            scene v15s39_24a # TPP. same as v15s39_21 Show Autumn getting into the Limo by herself her back is turned to Grayson, Grayson is checking out Autumns ass with a smirk on his face, MC is still taking his phone out of his pocket looking at his phone slight smile mouth is closed
            with dissolve

            u "(Just need to send the recording to Chloe... Hopefully she can find something to do with it.)"

            scene v15s39_25
            with dissolve

            pause 0.75

    scene v15s39_26 # TPP. Show Mc getting into the Limo slight smile mouth is closed, no need to show anyone else.
    with fade

    pause 0.75

    $ v15s39_kiwiiPost1= KiwiiPost(lindsey, "v15_linpost1.webp", "Having the most luxurious night! #VIPs", numberLikes=931)
    $ v15s39_kiwiiPost1.newComment(imre, "The fuck? Where's my invite?", numberLikes=renpy.random.randint(360, 860))
    $ v15s39_kiwiiPost1.newComment(lauren, "That looks so fun... Where are you guys?!", numberLikes=renpy.random.randint(360, 860))

    if v15_lindsey_inviteseb:
        $ v15s39_kiwiiPost1.newComment(sebastian, "No idea, but a really sick nightclub, haha! Lindsey planned this amazing night, thank you Lindsey!", numberLikes=renpy.random.randint(360, 860))
    else:
        $ v15s39_kiwiiPost1.newComment(grayson, "Wouldn't you like to know? Haha! Thanks for the night out, Lindsey.", numberLikes=renpy.random.randint(360, 860))

    $ v15s39_kiwiiPost1.newComment(lindsey, "You're welcome guys! I wish we could've brought more people... Next time everyone goes.", numberLikes=renpy.random.randint(360, 860))
    $ v15s39_kiwiiPost1.addReply("Next time? I need a nap... Lol.", numberLikes=renpy.random.randint(360, 860))
    $ v15s39_kiwiiPost1.addReply("Let me know when, I'm down!", numberLikes=renpy.random.randint(360, 860))

    jump v15s40