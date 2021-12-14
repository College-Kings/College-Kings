# SCENE 53: Sam Overdose Convo
# Locations: Apes Frat House
# Characters: SAMANTHA (Outfit: 1), MC (Outfit: 1)
# Time: Night
# Render 9 Unique 62 Total

label v14s53:
    play music "music/v13/Track Scene 16a_2.mp3" fadein 2

    scene v14s53_1 # TPP. MC enters the Apes Frat house, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v14s53_2 # TPP He's about to head up to his room but stops, and turns his head back downstairs to listen, no expression, mouth closed
    with dissolve

    sa "*Singing* (Inaudible)"

    scene v14s53_2a # TPP. same as v14s53_2 Mc, slight smile mouth open
    with dissolve

    u "(Is that Sam singing? Where's it coming from?)"

    stop music fadeout 3
    play music "music/v12/Track Scene 23_2.mp3" fadein 2
    scene v14s53_3 # TPP. MC walks into the apes Dream Room to find Samantha alone on the couch. She has a bottle of beer in hand. She swigs from it, Mc slight smile, mouth closed looking at samantha
    with dissolve

    pause 0.75

    scene v14s53_3a # TPP. Samantha doesn't see MC as he stands in the doorway watching her, she raises both her hands in the air in excitement, full smile, mouth open
    with dissolve

    sa "*Singing* And she goes ooh, ooh, yeaaaah... *Laughs*"

    scene v14s53_4 # FPP. Mc is still syanding in the doorway, only show sam still sitting on the couch, still holding her bottle, full smile, mouth open, arms waving in a different direction from v14s53_3a, she still hasn't seen mc and is looking somewhere else in the room
    with dissolve

    sa "*Singing* Maybe make her, maybe break her, the girl of your dreaaammss..."

    scene v14s53_4a # FPP. same as v14s53_4 Samantha suddenly becomes aware of MC, Samantha has a shocked expression, mouth open, looking directly at Mc, one hand clecnh's her chest and the other arm still holding the bottle in the air, some liquid spills from the bottle from her sudden movement
    with dissolve

    sa "Oh, my God! Haha... How long have you been standing there staring at me weirdo?"

    scene v14s53_4b # FPP. same as v14s53_4a Sam has a slight smile, mouth closed, still looking at mc, Sam has lowered her arms to her sides and is still holding the bottle
    with dissolve

    u "Not too long. Looks like you're having a great time there, Sam."

    scene v14s53_4c # FPP. same as v14s53_4b Sam's mouth is open
    with dissolve

    sa "I am."

    scene v14s53_4b
    with dissolve

    u "What song was that?"

    scene v14s53_4c
    with dissolve

    sa "I don't know. I was just making it up. Why, was it good?"

    scene v14s53_4b
    with dissolve

    menu:
        "Make a joke":
            $ v14_badsinging_Sam = True
            $ add_point(KCT.TROUBLEMAKER)

            scene v14s53_4c
            with dissolve

            u "Well, I don't think those lyrics are going to win any awards... like ever. *Chuckles*"

            scene v14s53_4d # FPP. same as v14s53_4b Sam has an angry expression
            with dissolve

            sa "Okay, dickhead. It's not like I was trying that hard! I'm just singing what comes naturally."

            scene v14s53_4e # FPP. same as v14s53_4d Sam's mouth is closed
            with dissolve

            u "Okay, okay... *Laughs* I'm only joking with you."

            scene v14s53_4d
            with dissolve

            sa "Why do guys have to be so stupid all the fucking time?"

            scene v14s53_4e
            with dissolve

            u "Stupid? I said I was joking, Sam."

            scene v14s53_4b
            with dissolve

            sa "Guess I forgot to laugh then..."

            scene v14s53_5 # FPP. close up shot of Sam winking and giving the thumbs up to mc, (Use this picture https://img.memecdn.com/i-amp-039-m-good_o_7184111.jpg as reference)
            with dissolve

        "Compliment her":
            $ add_point(KCT.BOYFRIEND)

            scene v14s53_4c
            with dissolve

            u "Yeah, you've got a nice voice. You should sing more often."

            scene v14s53_4f # FPP. same as v14s53_4a Sam has a full smile, happy expression
            with dissolve
            
            pause 0.75

            scene v14s53_4g # FPP. same as v14s53_4b Sam has a full smile
            with dissolve

            sa "Do you really think so? Thank you! I do enjoy it a lot, not many people know."

    scene v14s53_4c
    with dissolve

    u "What are you doing down here on your own anyway?"

    scene v14s53_4b
    with dissolve

    sa "I just wanted some privacy."

    scene v14s53_4h # FPP same as v14s53_4g She takes another swig of beer, not looking at mc, eyes closed
    with dissolve

    u "Sorry, should I leave you alone?"

    scene v14s53_4b
    with dissolve

    sa "Well, you're here now. You might as well come in and talk with me."

    scene v14s53_3b # TPP. same as v14s53_3a MC goes and sits down next to Samantha on the couch, a bottle is beside her, Samantha is looking at Mc, full smile, mouth open
    with dissolve

    pause 0.75

    scene v14s53_6 # FPP. Mc is sitting next to Sam on the couch, Show only Sam, Sam holds up and shows a small bag of pills towards mc with one of her hands with the bottle in the other hand, full smile, mouth open, looking at Mc
    with dissolve

    sa "I bought these pills today, but I don't even know what they are, haha!"

    scene v14s53_6a # FPP. same as v14s53_6 Sam has lowered both the bottle and pills to her sides
    with dissolve

    sa "My friend just said if I wanted a good time, this bag is full of them."

    scene v14s53_6b # FPP. same as v14s53_6a Sam's mouth is closed
    with dissolve

    u "Sam?! You don't know what they are?"

    scene v14s53_6a
    with dissolve

    sa "Oh, relax. I haven't taken any yet, daddy..."

    scene v14s53_6b
    with dissolve

    u "(Daddy?) *Chuckles* Well, that's good."

    scene v14s53_6a
    with dissolve

    sa "I'm thinking about it though."

    scene v14s53_6c # FPP. same as v14s53_6 Sam holds the bottle and pills in front of her and is looking at them, no expression, mouth closed
    with dissolve

    if v11_invite_sam_europe:
        scene v14s53_6d # FPP. same as v14s53_6c Sam is looking at MC, no expression, sams's mouth is open
        with dissolve

        sa "You know, I overdosed when we were in Amsterdam."

        if cameron.relationship.value >= Relationship.BRO.value:
            scene v14s53_6e # FPP. same as v14s53_6d Sam's mouth is closed
            with dissolve

            u "You overdosed? Shit, Sam... Cameron mentioned to me that you relapsed, but..."

            scene v14s53_6e
            with dissolve

            u "I didn't think that meant an overdose, though. I'm so sorry."

            if v11_invite_sam_europe and v13_invite_samantha:
                scene v14s53_6d
                with dissolve

                sa "For what? Haha... I make my own choices, you know."

            if v11_invite_sam_europe and not v13_invite_samantha:
                scene v14s53_6f # FPP. same as v14s53_6d Sam has a slight smile
                with dissolve

                sa "Oh, don't be. You did the right thing; I just like to rebel. *Chuckles*"

        else:
            scene v14s53_6e
            with dissolve

            u "What?! Sam, no. I had no idea."

            scene v14s53_6f
            with dissolve

            sa "Ha, yup..."

            scene v14s53_6g # FPP. same as v14s53_6f Sam's mouth is closed
            with dissolve

            u "An overdose? I can't believe Cameron didn't tell me."

            scene v14s53_6f
            with dissolve

            sa "Why would he? It's like family shame, haha. You keep that shit hidden."

    else:
        scene v14s53_6d
        with dissolve

        sa "I relapsed pretty badly while you guys were away..."

        scene v14s53_6e
        with dissolve

        u "Sam..."

        scene v14s53_6h # FPP same as v14s53_6c Sam's mouth is open
        with dissolve

        sa "Nothing bad, but... I just can't find another source of happiness or comfort, [name]."

        scene v14s53_6d
        with dissolve

        sa "Cameron knows something is up, but I can't talk to him. One mention of wanting to pop a pill, and he'll throw me into the hospital."

        scene v14s53_6e
        with dissolve

        u "You know you can talk to me."

        scene v14s53_6a
        with dissolve

        sa "*Chuckles*"

        scene v14s53_6b
        with dissolve

        pause 0.75

    scene v14s53_6a
    with dissolve

    sa "Anyway, that happened. I survived. And it wasn't on purpose, just so you know."

    scene v14s53_6b
    with dissolve

    u "Well, that's one positive thing that I've heard from this conversation at least."

    scene v14s53_6a
    with dissolve

    sa "I was just having a good time and went too far. I make a habit of that."

    scene v14s53_6b
    with dissolve

    u "You don't need a baggie full of \"good time\" pills to-"

    scene v14s53_6a
    with dissolve

    sa "Yeah, yeah. I don't need drugs to have fun. I get it, I know."

    scene v14s53_6b
    with dissolve

    u "So, why take them?"

    scene v14s53_6h
    with dissolve

    sa "I take drugs because I can't deal with any of my emotional baggage without them."

    scene v14s53_6d
    with dissolve

    sa "All the things that have happened in my life... It isn't easy coming from a broken home, you know?"

    scene v14s53_6i # FPP. same as v14s53_6 Samantha starts crying, looking at Mc, sad expression, mouth closed
    with dissolve
    
    pause 0.75

    scene v14s53_6j # FPP. same as v14s53_6i MC grabs Sam's hands and holds them, Sam's mouth is open, sam is still crying
    with dissolve

    sa "And when I'm around other people who take drugs... *Sniffles*"

    scene v14s53_6j
    with dissolve

    sa "It makes me feel like, like I belong somewhere... *Sniffles* Do you know what I mean?"

    scene v14s53_6k # FPP. same as v14s53_6j, Sam's mouth is closed, she is looking down and away from Mc feeling ashamed
    with dissolve

    u "(How do I want to go about this? Convince her to stay off drugs? Is that even possible? Or should I just let her continue, as she knows her own limits?"

    scene v14s53_6k
    with dissolve

    menu:
        "Help Samantha be clean":
            $ add_point(KCT.BOYFRIEND)
            $ add_point(KCT.BRO)

            scene v14s53_6k
            with dissolve

            if v14_amber_clean:
                $ grant_achievement("clean_it_up")

            u "I know exactly what you mean, Sam. Look at me."

            scene v14s53_6l # FPP. same as v14s53_6i Sam lifts her chin and wipes her tears, making eye contact with MC, sad expression
            with dissolve

            pause 0.75

            scene v14s53_6m # FPP. same as v14s53_6j Sam's mouth is closed
            with dissolve

            u "I know it's not easy. Everyone on this planet can tell you that life isn't easy."

            scene v14s53_6m
            with dissolve

            u "All I can say is what I see from the outside, and I can see that this shit is destroying your life. Look at you right now."

            scene v14s53_6j
            with dissolve

            sa "*Crying* But I don't know how to deal with any of my problems without drugs, [name]!"

            scene v14s53_6j
            with dissolve

            sa "*Crying* All of life's shit is just sitting there, waiting for me to come down from being high."

            scene v14s53_6m
            with dissolve

            u "Drugs give people a distraction from their problems for a moment, and that's fucking magical. I admit."

            if v11_invite_sam_europe:
                scene v14s53_6m
                with dissolve

                u "But you don't have enough self-control to live this way. You overdosed. You're risking your life, Sam."

            else:
                scene v14s53_6m
                with dissolve

                u "But you don't have enough self-control to live this way. You continue to relapse. You're dependent on drugs, Sam."

            scene v14s53_6n # FPP. same as v14s53_6a Sam puts down the bottle and pills to her side and buries her face in her hands, tears can be seen coming from her hands, Sam is crying
            with dissolve

            sa "*Sobbing*"

            scene v14s53_6n
            with dissolve

            u "I think you need to get help on how to deal with the emotional stuff. Real help. From people who want to help. There's a way out of all this."

            scene v14s53_6o # FPP. same as v14s53_6n Sam pulls her hands away from her face to her lap, Sam s not looking at Mc she is looking up at the ceiling, sad expression, she has wiped the tears from her face, mouth closed
            with dissolve

            sa "*Sniffles* ..."

            scene v14s53_6p # FPP. same as v14s53_6o Sam is now looking at MC, still a sad expression, mouth open
            with dissolve

            sa "Will you help me?"

            scene v14s53_6q # FPP. same as v14s53_6p Sam's mouth is closed
            with dissolve

            u "Of course, I will."

            scene v14s53_6r # FPP. same as v14s53_6q Sam looks intently into MC's eyes, mouth slight open like she wants to say something but doesn't, lustful expression
            with dissolve

            u "*Chuckles* What?"

            #if SamanthaRS:
            if samantha.relationship.value >= Relationship.MOVE.value:
                scene v14s53_3c # TPP. same as v14s53_3b Show sam pushing the bottle of beer and pills away from her on the couch, grabbing mc behind the head and pulling him in for a kiss, Sam's eyes are closed lustful expression, Mc's eyes are open slightly shocked expression
                with dissolve
                
                pause 0.75

                scene v14s53_6r
                with dissolve

                u "(Oh!)"

                scene v14s53_3d # TPP. same as v14s53_3c The bottle and pills are where she pushed them too from scene v14s53_3c, Sam now uses both hands to grab mc's head and pull him in for a kiss
                with dissolve

                menu:
                    "Accept the kiss":
                        $ add_point(KCT.BRO)

                        scene v14s53_3e # TPP. same as v14s53_3d MC grabs Sam's face, kiss her back passionately
                        with dissolve
                        
                        pause 0.75

                        scene v14s53_3f # TPP. same as v14s53_3e They pull away smiling from each other
                        with dissolve
                        
                        pause 0.75

                    "Reject the kiss":
                        $ add_point(KCT.BOYFRIEND)

                        scene v14s53_3g # TPP. same as v14s53_3d MC lightly pulls Sam off him, Mc is holding a hand to her cheek with one hand, and holding one of her hands with the other, Mc is looking at Sam with a compassionate not sexual expression, Sam has put both her hands to her side, looking at Mc slightly sad expression, mouth closed
                        with dissolve
                        
                        pause 0.75

                        scene v14s53_6s # FPP. same as v14s53_6r Sam has a slightly sad but understanding expression, slight smile, mouth closed, looking at mc
                        with dissolve

                        u "Mmm-"

                        scene v14s53_6s
                        with dissolve

                        u "Sorry, I just-"

                        scene v14s53_6t # FPP. same as v14s53_6s Sam's mouth is open
                        with dissolve

                        sa "It's okay. This is bad timing."

                        scene v14s53_6s
                        with dissolve

                        u "(Phew...)"

            scene v14s53_6u # FPP. same as v14s53_6 Sam has no expession looking at mc, mouth open, holding the pills towards Mc, the bottle is sitting beside her
            with dissolve

            sa "I uh, I don't want to take these pills anymore... Could you throw them away for me?"

            scene v14s53_6v # FPP. same as v14s53_6u Mc holds his hand out, Sam has a slight smile, mouth closed
            with dissolve

            u "Good idea. Absolutely."

            scene v14s53_6w # FPP same as v14s53_6v Samantha puts the pills into mc's hand, no expression, looking at the pills
            with dissolve
            
            pause 0.75

            scene v14s53_6x # FPP. same as v14s53_6w Mc's and sams hands are at their sides, the bottle is still sitting beside sam, Sam looks at mc and smiles, mouth open
            with dissolve

            sa "I need to go to bed now... Haha."

            scene v14s53_6y # FPP. same as v14s53_6x Sam's mouth is closed
            with dissolve

            u "Another great idea."

            scene v14s53_3h # TPP. same as v14s53_3g Samantha gives MC a friendly hug both arm's around his neck and shoulders, mc gives sam a friendly hug back, slight smiles, mouth closed, The bottle can be seen behind sam and the pills can be seen behind mc
            with dissolve

            sa "Thank you."

            scene v14s53_3i # TPP. same as v14s53_3h Samantha is looking down at the pills behind mc's back, no expression
            with dissolve

            u "You're welcome, Sam."

            scene v14s53_3h
            with dissolve

            pause 0.75

            scene v14s53_7 # FPP. Mc is sitting on the couch as Samantha walks out of the room, she is looking back at mc slight smile mouth closed, waving at mc
            with dissolve

            pause 0.75

            scene v14s53_8 # FPP. MC stays sitting alone for a moment, holding both the bottle and the pills in his hands in front of him
            with dissolve

            u "(*Sighs* I feel good about that. I think I did the right thing.)"

            stop music fadeout 3
            jump v14s53b

        "Let Samantha enjoy drugs":
            $ v14_SamanthaDrugs = True
            $ add_point(KCT.TROUBLEMAKER)

            scene v14s53_6k
            with dissolve

            u "Yeah, I know exactly what you mean."

            scene v14s53_6e
            with dissolve

            u "I'm not going to judge you, Sam. We all have different coping mechanisms for the things going on in our lives."

            scene v14s53_6g
            with dissolve

            u "This is yours. I'm sure you're capable of figuring out how to manage it better at some point."

            scene v14s53_6f
            with dissolve

            sa "Thank you. *Chuckles*"

            scene v14s53_6g
            with dissolve

            u "Of course, I'll be here no matter what."

            scene v14s53_6z # FPP. same as v14s53_6r Sam's mouth is open enough to talk now
            with dissolve

            sa "Sometimes I feel like you're the only one who's ever fully understood me."

            scene v14s53_6za # FPP. same as v14s53_6z Sam takes her top off, revealing her lacy black bra, mouth is closed
            with dissolve

            pause 0.75

            scene v14s53_6zb # FPP. same as v14s53_6za Sam's top is fully off, looking at mc with a lustful expression, mouth is still closed, full smile
            with dissolve

            u "(Oh... Wow.)"

            scene v14s53_6zc # FPP. same as v14s53_6zb Sam's mouth is open
            with dissolve

            sa "The last guy I let inside me never had anything nice to say... I always attract the jerks."

            scene v14s53_6zc
            with dissolve

            sa "But you're different... Aren't you?"

            scene v14s53_3j # TPP. same as v14s53_3d The bottle and pills are in between sam and mc, Sam has removed her shirt and is wearing the lacey black bra from render v14s53_6za
            with dissolve
            
            pause 0.75

            scene v14s53_6zb
            with dissolve

            u "(Oh my...)"

            scene v14s53_6zc
            with dissolve

            sa "Take these pants off. I want you. Now."

            scene v14s53_6zb
            with dissolve

            menu:
                "Take your pants off":
                    $ add_point(KCT.TROUBLEMAKER)
                    $ samantha.relationship = Relationship.FWB
                    $ sceneList.add("v14_samantha")
                    
                    label v14s53_sg:

                    scene v14s53_3k # FPP. same as v14s53_3j MC smirks and begins unbuttoning his pants, Sam leans slightly back and is grabbing in between mc's legs with one hand and has one hand down her shorts over her pussy with the other
                    with fade

                    pause 0.75

                    stop music fadeout 3

                    jump v14s53a

                "Don't take your pants off":
                    $ add_point(KCT.BOYFRIEND)
                    $ add_point(KCT.BRO)

                    scene v14s53_6zc
                    with dissolve

                    u "Um, actually... I don't think that's a good idea, Sam."

                    scene v14s53_6zd # FPP. same as v14s53_6zc Sam has a slightly angry expression, mouth is still open
                    with dissolve

                    sa "What? W- Why not?! You think I'm hot, don't you?"

                    scene v14s53_6ze # FPP. same as v14s53_6zc Sam's mouth is closed
                    with dissolve

                    u "That's not the point. You've been drinking, and I just don't think it's a good idea."

                    scene v14s53_6zd
                    with dissolve

                    sa "This is my second beer, [name]."

                    if v14_badsinging_Sam:
                        scene v14s53_6zf # FPP. same as v14s53_6zc Sam has increased to fully angry expression
                        with dissolve

                        sa "See, I was right! Ha! All of you are stupid dickheads. Every single one of you!"

                    else:
                        scene v14s53_6zc
                        with dissolve

                        sa "What the fuck do you want from me then, [name]? Why did you even come talk to me?"

                    scene v14s53_9 # FPP. Mc is still sitting on the couch, sam stands up in front of him and puts back on her shirt, angry expression, mouth closed not looking at mc
                    with dissolve

                    u "Sam..."

                    scene v14s53_7a # FPP. same as v14s53_7 Samantha is storming out of the room, angry expression, looking back at mc mouth closed, flipping mc off
                    with dissolve

                    u "Sam!"

                    scene v14s53_8
                    with dissolve

                    u "*Sighs* (I hope she doesn't hate me in the morning.)"

                    scene v14s53_8
                    with fade

                    pause 0.75

                    stop music fadeout 3

                    jump v14s53b