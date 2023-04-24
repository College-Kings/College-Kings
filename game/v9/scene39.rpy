# SCENE 39: Hanging/Making out with Lindsey
# Locations: Chicks House/Lindsey's Room
# Characters: MC (Outfit 3), Lindsey (Outfit 1)
# Time: Saturday Evening

label v9_hang_w_linds:
    scene v9hwl1 # TPP. Show MC knocking on the door of the chicks house.
    with fade

    play music "music/v9/Track Scene 8_1.mp3" fadein 2

    pause 1

    scene v9hwl2 # FPP. Show Lindsey opening to the door, Lindsey smile, mouth open.
    with dissolve

    li "Hey! You look rough. Bad day?"

    scene v9hwl2a # FPP. Same camera as v9hwl2, smile, mouth closed.
    with dissolve

    u "Nah, just frat drama. You know how it is."

    scene v9hwl2
    with dissolve

    li "Well, no, but I'm sure for boys it's a lot different."

    scene v9hwl2a
    with dissolve

    u "Yes, all that testosterone in one place."

    scene v9hwl2
    with dissolve

    li "Come in, sorry."

    scene v9hwl3 # TPP. Show MC walking into the chicks house.
    with dissolve
    
    pause 1

    scene v9hwl4 # TPP. Show MC and Lindsey now in Lindsey's room sat on the bed opposite eachother.
    with fade

    pause 1

    if not hl_punch:

        scene v9hwl5 # FPP. Show Lindsey, concerned, mouth open.
        with dissolve

        li "I was worried about you after what happened at school. Are you sure you're OK? You really do look..."

        scene v9hwl5a # FPP. Same camera as v9hwl5, concerned, mouth closed.
        with dissolve

        u "I'm fine. Please don't say how bad I look again, haha. My ego can't take it."

        scene v9hwl5b # FPP. Same camera as v9hwl5, smile, mouth open.
        with dissolve

        li "No, not like that, silly. Just... tired?"

        scene v9hwl5c # FPP. Same camera as v9hwl5, smile, mouth closed.
        with dissolve

        u "Yeah, definitely that. And it's gonna be a long night."

    else:
        scene v9hwl5b
        with dissolve

        li "So are you ready to kick ass again?"

        scene v9hwl5c
        with dissolve

        menu:
            "Play it cool":
                $ playCoolWLins = True
                $ reputation.add_point(RepComponent.BRO)

                u "Damn right! You gonna be there to cheer me on?"

                scene v9hwl5b
                with dissolve

                li "Maybe."

                scene v9hwl5c
                with dissolve

                u "Or will you wait to see how I'm doing first?"

                scene v9hwl5b
                with dissolve

                li "Of course! Can't be on the loser's side of the ring."

                scene v9hwl5c
                with dissolve

                u "Because you have a reputation to uphold."

                scene v9hwl5b
                with dissolve

                li "Sure do." 

            "Get real":
                $ reputation.add_point(RepComponent.BOYFRIEND)

                u "I'm sure everyone's expecting me to fall in my first fight."

                scene v9hwl5
                with dissolve

                li "Why?"

                scene v9hwl5a
                with dissolve
                
                u "Because that punch was a lucky shot."

                scene v9hwl5
                with dissolve

                li "No it wasn't! I saw the whole thing, remember?"

                scene v9hwl5b
                with dissolve

                li "You're gonna do great."
    label v9_make_out_w_lin:
    scene v9hwl5c
    with dissolve

    u "So why did you ask me to come over?"

    scene v9hwl6 # TPP. Show Lindsey reaching for MC's hand, compassionate expression, both looking at eachother.
    with dissolve

    image v9links = Movie(play="images/v9/Scene 39/v9links.webm", loop=True, image="images/v9/Scene 39/v9linksStart.webp", start_image="images/v9/Scene 39/v9linksStart.webp") # TPP. MC and Lindsey passionately making out.
    image v9linksf = Movie(play="images/v9/Scene 39/v9linksf.webm", loop=True, image="images/v9/Scene 39/v9linksStart.webp", start_image="images/v9/Scene 39/v9linksStart.webp")

    menu:
        "Let Lindsey grab your hand":
            if CharacterService.is_fwb(chloe):
                $ reputation.add_point(RepComponent.TROUBLEMAKER)

            else:
                $ reputation.add_point(RepComponent.BOYFRIEND)
            
            scene v9hwl6a # TPP. Same camera as v9hwl6, Lindsey now holding MC's hand, looking into his eyes.
            with dissolve

            li "I don't know why, but I can't help but worry about you."

            scene v9hwl5e # FPP. Same camera as v9hwl5, compassionate, mouth closed.
            with dissolve

            if playCoolWLins:
                u "I thought you said not to worry."

                scene v9hwl5d # FPP. Same camera as v9hwl5, compassionate, mouth open.
                with dissolve

                li "Yeah, for you not to. Let me worry for the both of us."

            else:
                scene v9hwl5e
                with dissolve

                u "So you agree it was just a lucky shot!"

                scene v9hwl5d
                with dissolve

                li "No! But it's still a fight and it could be dangerous."

            scene v9hwl7 # TPP. Show Lindsey pulling MC into a long hug, MC looks a little confused, Lindsey looks like she's enjoying it.
            with dissolve

            pause 2

            scene v9hwl7a # TPP. Same camera as v9hwl7, Show MC pulling out of the hug with Lindsey.
            with dissolve

            pause 1

            scene v9hwl8 # FPP. Close up of Lindsey, as if she is about to go in for a kiss with MC (camera).
            with dissolve
            
            stop music fadeout 3

            play music "music/v9/Track Scene 39_2.mp3" fadein 2


            menu:
                "Make out with Lindsey":
                    if CharacterService.is_fwb(chloe):
                        $ reputation.add_point(RepComponent.TROUBLEMAKER)
                    
                    else:
                        $ reputation.add_point(RepComponent.BOYFRIEND)

                    $ CharacterService.set_relationship(lindsey, Relationship.KISSED)
                    $ sceneList.add("v9_lindsey")
                    
                    scene v9links # Animations pls ignore
                    with dissolve

                    " "

                    scene v9hwl5c
                    with dissolve

                    u "You taste like... caramel?" 

                    scene v9hwl5b
                    with dissolve

                    li "My coffee. It has sooo much sugar, but it's a guilty pleasure. Sorry."

                    scene v9hwl5c
                    with dissolve

                    u "No! I like it. A lot."

                    scene v9linksf # Animation pls ignore 
                    with dissolve

                    " "

                    scene v9hwl5c
                    with dissolve

                    u "Very nice."

                    scene v9hwl5f # FPP. Same camera as v9hwl5, flirty, mouth open.
                    with dissolve

                    li "I want you."

                    scene v9hwl5g # FPP. Same camera as v9hwl5, flirty, mouth closed.
                    with dissolve

                    u "You can have me!"

                    scene v9hwl9 # TPP. Show MC lying on Lindsey's bed looking at Lindsey, both smiling.
                    with dissolve

                    play sound "sounds/phonealarm.mp3"

                    "*Phone alarm goes off*"

                    scene v9hwl9a # TPP. Same camera as v9hwl9, Lindsey giggle, MC fumbling around looking for his phone.
                    with dissolve

                    u "(No! Shit!)"

                    stop music fadeout 3
                    
                    scene v9hwl10 # FPP. Show Lindsey (camera as if MC has gotten off the bed but Lindsey still on it). Lindsey a little sad, mouth closed.
                    with dissolve

                    stop sound
                    u "Dammit! I have to get ready for the Brawl."

                    u "I'm so sorry. I really don't want to go... REALLY!"

                    scene v9hwl10a # FPP. Same camera as v9hwl10, Lindsey a little sad, mouth open.
                    with dissolve

                    li "I know. But your brothers are counting on you."

                    scene v9hwl10
                    with dissolve

                    u "Please say you'll come watch me?"

                    scene v9hwl10b # FPP. Same camera as v9hwl10, Lindsey flirt, mouth open.
                    with dissolve

                    li "Absolutely. And depending on how the night ends... maybe it can end up back here."

                    scene v9hwl10c # FPP. Same camera as v9hwl10, Lindsey flirt, mouth closed.
                    with dissolve

                    u "All the incentive I need!"

                    scene v9hwl11 # TPP. Show Lindsey standing up and kissing MC, Lindsey grazes MC's crotch with her hand.
                    with dissolve

                    u "Ugh, I can't believe my luck."

                    scene v9hwl12 # FPP. Show Lindsey, Lindsey flirt, mouth open.
                    with dissolve

                    li "Sorry, that was just to make sure you don't forget."

                    scene v9hwl12a # FPP. Same camera as v9hwl12, Lindsey flirt, mouth closed.
                    with dissolve

                    u "I could never forget."

                    scene v9hwl13 # TPP. Show MC kissing Lindsey again as he is leaving.
                    with dissolve

                    pause 1
                    $ renpy.end_replay()

                "Pull away":
                    if CharacterService.is_fwb(chloe):
                        $ reputation.add_point(RepComponent.BOYFRIEND)
                        
                    scene v9hwl7b # TPP. Same camera as v9hwl7, Show MC pulling away from Lindsey who is trying to kiss him.
                    with dissolve

                    pause 1

                    scene v9hwl5h # FPP. Same camera as v9hwl5, quite sad, mouth open.
                    with dissolve

                    $ grant_achievement("the_wrong_time")
                    li "What's wrong?"

                    scene v9hwl5i # FPP. Same camera as v9hwl5, quite sad, mouth closed.
                    with dissolve

                    u "Nothing. Seriously, you're amazing and I wish I could stay and... hang out with you. But I have to get ready for the fight."

                    scene v9hwl5h
                    with dissolve

                    u "Really, I'm sorry."

                    scene v9hwl5i
                    with dissolve

                    li "No, I get it. It's OK. Get ready for your fight. And be careful."

                    scene v9hwl5h
                    with dissolve

                    u "I will. And maybe I can text you later, after the fight."

                    scene v9hwl5i
                    with dissolve

                    li "Maybe. I'll probably be in bed, though."

                    scene v9hwl5h
                    with dissolve

                    u "(In bed! Geez why am I so stupid?)"

                    u "I promise this is only about the Brawl. Any other day I'd be-"

                    scene v9hwl5i
                    with dissolve

                    li "You better go."

                    scene v9hwl5i
                    with dissolve

                    u "Yeah. I'll talk to you later. Promise."

                    scene v9hwl14 # TPP. Show MC leaving Lindsey's room, Lindsey watching him, Lindsey looks quite sad.
                    with dissolve

                    pause 1
                    $ renpy.end_replay()

            if joinwolves:
                jump v9_wolves_pre_fight
            
            else:
                jump v9_apes_pre_fight
           
        "Pull away":
            scene v9hwl6b # TPP. Same camera as v9hwl6, MC moves his hand away as Lindsey is about to grab it, Lindsey sad, MC confused.
            with dissolve

            pause 1

            scene v9hwl5h
            with dissolve

            li "I just want to make sure you're OK before the fight is all."

            scene v9hwl5i
            with dissolve

            u "I'm good."

            scene v9hwl5h
            with dissolve

            li "What's wrong?"

            scene v9hwl5i
            with dissolve
            
            u "Nothing. Just in the zone I guess. Gotta keep my focus on the brawl. A lot's riding on it. On me."

            scene v9hwl5h
            with dissolve

            li "Yeah I guess."

            scene v9hwl5i
            with dissolve

            u "I really should go. I should have gone straight home. They're gonna be looking for me."

            scene v9hwl5h
            with dissolve

            li "Good luck tonight."

            scene v9hwl5i
            with dissolve

            u "Yeah, thanks."

            scene v9hwl14
            with dissolve
            
            pause 1
            $ renpy.end_replay()
    
            if joinwolves:
                jump v9_wolves_pre_fight
            
            else:
                jump v9_apes_pre_fight