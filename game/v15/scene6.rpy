# SCENE 6: School hallway towards library
# Locations: School hallway
# Characters: MC (Outfit: 5), Chloe (Outfit: 2)
# Time: Friday

# SCENE 7: Chloe in front of library
# Locations: Hallway in front of library
# Characters: MC (Outfit: 5), CHLOE (Outfit: 2), FEMALE STUDENT (Outfit: x), MALE STUDENT (Outfit: x)
# Time: Friday

label v15s6:
    play music "music/v13/Track Scene 19_1.mp3" fadein 2

    scene v15s6_1 # TPP Show MC walking in school hallway toward library
    with fade

    pause 1

    if "diary" in freeroam12stolen or "cash_large" in freeroam12stolen or "cash_small" in freeroam12stolen: # -if MC stole any of Chloe's money and/or her diary from her room
        scene v15s6_2 # FPP Show Chloe exiting library, she is crying, using her hand to try and mask the tears
        with dissolve

        u "(There's Chloe. Oh shit- Is she crying?)"
        u "(Oh no, I think I know what this is about... *Sighs*)"
        
        stop music fadeout 3
        
        play music "music/v13/Track Scene 8.mp3" fadein 2

        scene v15s7_1 # FPP At entrance to library, Chloe is obviously crying and doing a bad job of hiding it with her hand
        with dissolve

        u "Hey, what's going on?"

        scene v15s7_1a # FPP Same angle as 1, Chloe has dropped her hand, crying with mouth open, looking at MC
        with dissolve

        cl "[name]... *Sniffles* I don't know what I'm going to do."

        if chloe.relationship >= Relationship.GIRLFRIEND:
            scene v15s7_2 # FPP MC reaches out and takes Chloe's hand
            with dissolve

            pause 0.75

        if "cash_large" in freeroam12stolen and not "cash_small" in freeroam12stolen: # -if the large cash was stolen
            if v14_realwolf:
                scene v15s7_1a
                with dissolve
                
                cl "Somebody stole my campaign money. *Sobbing* Five hundred fucking dollars, [name]."

            else:
                scene v15s7_1a
                with dissolve
                
                cl "Somebody stole my campaign money. *Sobbing* Nine hundred fucking dollars, [name]."
            
            cl "I don't know how I'm supposed to pay for- *Crying* I needed that money..."

            scene v15s7_1b # FPP Same as 1a, Chloe's mouth closed
            with dissolve

            u "(Well, fuck... So did we, ha.)"

            u "Shit, Chloe... They took everything you had?"

            scene v15s7_1a
            with dissolve

            cl "Well, I still had a few hundred in my purse that they didn't find."

            if "purse" in freeroam12: # -If MC checked the purse in v14.51 but did not take the money
                scene v15s7_1
                with dissolve

                u "(Eh, we found it.)"

            scene v15s7_1b
            with dissolve

            u "At least that's something, right?"

            scene v15s7_1a
            with dissolve

            cl "They were in my room! What if they were there while I was sleeping? I could be dead right now, I- *Sobs*"

        elif "cash_small" in freeroam12stolen and not "cash_large" in freeroam12stolen: # -if $300 was stolen
            scene v15s7_1a
            with dissolve

            cl "Somebody broke into my room... *Sobbing* They took three hundred dollars out of my purse..."

            scene v15s7_1b
            with dissolve

            u "Oh, Chloe... Holy shit, I- Is that all they took?"

            scene v15s7_1a
            with dissolve

            cl "*Sniffles* Yeah... Luckily, they didn't find my hidden stash with all the campaign money."

            if "closet" in freeroam12: # -If MC checked the closet in v14.51 but did not take the money
                scene v15s7_1
                with dissolve
    
                u "(Or maybe they did find it but decided not to rob you clean... Ha.)"

            scene v15s7_1b
            with dissolve

            u "That's good, yeah?"

            scene v15s7_1a
            with dissolve

            cl "It's not the end of the world but still, they were in my room. Someone was in my room..."
            cl "*Sobbing* It's so scary and creepy!"

        elif "cash_small" in freeroam12stolen and "cash_large" in freeroam12stolen: # -if $900 and $300 was stolen
            scene v15s7_1a
            with dissolve

            cl "They took all of it, [name]. All my campaign money... It's gone! *Sobbing*"

            scene v15s7_1b
            with dissolve

            u "Oh, shit... Wait, Who? How?"

            scene v15s7_1a
            with dissolve

            cl "I had it all in my room... Someone went in there and took it, it's all gone!"

            scene v15s7_1b
            with dissolve

            u "(Yeah... Sorry about that...)"

            scene v15s7_1
            with dissolve

            u "I'm so sorry, Chloe. Are you okay, though? Did they hurt you or-?"

            scene v15s7_1a
            with dissolve

            cl "I can't win now, [name]. There's no way that I could win with zero dollars. *Cries*"
        
        elif "diary" in freeroam12stolen and not ("cash_large" in freeroam12stolen or "cash_small" in freeroam12stolen): # -if ONLY Chloe's diary was stolen
            scene v15s7_1a
            with dissolve

            cl "Someone broke into my room and stole my... My diary! *Sobbing*"

            scene v15s7_1
            with dissolve

            u "(Oopsies...)"

            menu:
                "You have a diary?":
                    $ add_point(KCT.TROUBLEMAKER)

                    scene v15s7_1b
                    with dissolve

                    u "Holy shit... You have a diary?"

                    if chloe.relationship >= Relationship.GIRLFRIEND:
                        $ chloeSus += 1

                    scene v15s7_1c # FPP Same angle as 1, Chloe looking at MC, tears on her face, she looks angry
                    with dissolve
                
                    cl "Yes, [name]. I DID have a diary."

                    if chloe.relationship >= Relationship.FWB: #If Chloe GF or Chloe RS
                        scene v15s7_1a
                        with dissolve

                        cl "And your name is in it multiple times."

                        scene v15s7_1b
                        with dissolve

                        u "Why is- What does it, uh... say about me?"

                        scene v15s7_1a
                        with dissolve

                        cl "It's too late now, [name]. Who cares?"

                        scene v15s7_1d # FPP Same angle as 1, Chloe still sad and crying, throwing her hands in the air in exasperation and looking into the distance
                        with dissolve

                        u "(Me??? I do??? Fuck...)"

                    else:
                        scene v15s7_1a
                        with dissolve

                        cl "And I wrote every important moment of my life down in there... *Cries*"

                        scene v15s7_1b
                        with dissolve

                        u "(Good to know...)"

                "Why your diary?":
                    $ add_point(KCT.BOYFRIEND)
                    
                    scene v15s7_1b
                    with dissolve

                    u "Your diary? Why would they take that?"

                    scene v15s7_1d
                    with dissolve

                    cl "I don't know! *Crying*"

                    scene v15s7_1a
                    with dissolve

                    cl "But it's gone and I can't find it anywhere. Every single one of my most private thoughts are written down in there."
                    cl "I feel completely naked inside knowing that someone else is probably out there reading it. *Sniffles*"

        elif "diary" in freeroam12stolen and "cash_small" in freeroam12stolen and "cash_large" in freeroam12stolen: # -if $900, $300 and Chloe's diary was stolen
            scene v15s7_1a
            with dissolve

            cl "I give up completely. I'm done. *Sobbing*"

            scene v15s7_1b
            with dissolve

            u "Why? What happened, Chloe?"

            scene v15s7_1d
            with dissolve

            cl "Everything is gone. My campaign money, every dollar out of my purse... and my diary. *Sniffles*"

            scene v15s7_1b
            with dissolve

            u "(Shit...)"

            scene v15s7_1a
            with dissolve

            cl "Somebody broke into my room and took it all... *Crying*"

            scene v15s7_1b
            with dissolve

            u "Oh fuck, Chloe. I'm so sorry..."

            if chloe.relationship >= Relationship.FWB:
                scene v15s7_1a
                with dissolve

                cl "Yeah, me too... There's a lot written down in there, about both of us. *Sniffles* I'm so sorry."

                scene v15s7_1
                with dissolve

                u "(Oh... FUCK!)"

                scene v15s7_1b
                with dissolve

                u "*Sighs* It's not your fault, it's fine."

            scene v15s7_1
            with dissolve

            u "(How should I go about this?)"

            menu:
                "Sympathize":
                    $ add_point(KCT.BOYFRIEND)

                    scene v15s7_1b
                    with dissolve

                    u "Look..."

                    scene v15s7_1
                    with dissolve

                    u "This absolutely sucks, I know that. But it's not over Chloe. This isn't the end."

                    scene v15s7_1b
                    with dissolve

                    u "As long as you continue going towards your goal, which is to be the President of the Chicks... That's your goal, yeah?"

                    scene v15s7_1a
                    with dissolve

                    cl "*Sniffles* Yeah."

                    scene v15s7_1b
                    with dissolve

                    u "If you keep going towards that, you will not fail."

                    scene v15s7_1a
                    with dissolve

                    cl "*Sighs* Okay..."

                "Empathize":
                    $ add_point(KCT.BRO)
                    $ chloeSus += 1
                    $ v15s7_chloe_empathize = True

                    # -Chloe slowly gets annoyed with MC through this empathizing bit-
                    scene v15s7_1b
                    with dissolve

                    u "*Sighs* I'm so sorry Chloe, I can't imagine what you're going through right now..."

                    scene v15s7_1a
                    with dissolve

                    cl "I'm going through absolute shit, [name]!"

                    scene v15s7_1
                    with dissolve

                    u "I know you are, there's no denying that, ha. But-"

                    scene v15s7_1c
                    with dissolve

                    cl "What am I supposed to do? I literally got robbed! Do I go into a full investigation, or is that gonna cause me even more stress?"

                    scene v15s7_1
                    with dissolve

                    u "Probably more stress..."

                    scene v15s7_1d
                    with dissolve

                    cl "*Sighs* Fuck!"

        # -continue regardless-
        # -Chloe is feeling a bit better-
        scene v15s7_1e # FPP Same angle as 1, Chloe is wiping the tears out of her eyes, expression more neutral
        with dissolve

        cl "Alright. I have no other choice than to stand tall right now."

        scene v15s7_1f # FPP Same as 1e, Chloe's mouth closed
        with dissolve

        u "Damn straight."

        scene v15s7_1e
        with dissolve

        cl "If I lose the campaign, I'll lose my scholarship and that would lead to me dropping out, because I can't afford the last semester."

        scene v15s7_1g # FPP Same angle as 1, Chloe looking at MC with mouth open, neutral expression, tears and smeared mascara are looking better
        with dissolve

        cl "I can't let it happen."

        if v14_help_chloe: # -if MC is helping Chloe
            scene v15s7_1h
            with dissolve
                
            u "We won't. Don't even think about it."

        else: # -if MC is not helping Chloe
            scene v15s7_1h # FPP Same angle as 1, Chloe looking at MC with a slight smile, mouth closed
            with dissolve

            u "You won't. I know you won't."

        if chloe.relationship >= Relationship.GIRLFRIEND:
            play sound "sounds/kiss.mp3"
            
            scene v15s7_4 # TPP Chloe giving MC a kiss, a little bit of mascara still streaking her face
            with dissolve

            pause 1.75

            scene v15s7_3
            with dissolve

            pause 1
        
        elif chloe.relationship >= Relationship.FWB: # -if Chloe Rs, they hug tightly
            scene v15s7_3 # TPP Chloe giving MC a tight hug
            with dissolve

            pause 1.25

        else: # -if not Chloe RS or Chloe GF, Chloe gives MC a quick hug
            scene v15s7_3a # TPP Chloe giving MC a quick, friendly hug
            with dissolve

            pause 1

        scene v15s7_1i # FPP Same as 1h, Chloe's mouth open
        with dissolve

        cl "Okay, it's time to get to work."

        scene v15s7_1h
        with dissolve

        u "Haha, good."

        if v14_help_chloe: # -if MC is helping Chloe with planning board
            scene v15s7_1i
            with dissolve

            cl "Ready?"

            scene v15s7_1h
            with dissolve

            u "Yup, after you."

            scene v15s7_5 # TPP MC and Chloe walking into the library together
            with dissolve

            pause 0.75
        
            stop music fadeout 3
        
            jump v15s8

        else: # -if MC is not helping Chloe
            u "I'll see you later? Lauren's party?"

            scene v15s7_1j # FPP Same angle as 1, Chloe looking at MC, expression neutral, mouth open
            with dissolve

            cl "*Sighs* I'm way too busy, I already told her I couldn't make it."

            scene v15s7_1k # FPP Same as 1j, Chloe's mouth closed
            with dissolve

            u "Ah, that sucks... Well, good luck with it all."

            scene v15s7_1i
            with dissolve

            cl "Thanks, [name]."

            scene v15s7_1h
            with dissolve

            u "Don't mention it."

            if chloe.relationship >= Relationship.GIRLFRIEND:
                scene v15s7_1l # FPP Same angle as 1, Chloe looking down at MC's dick, sexy expression, mouth open
                with dissolve

                cl "Okay..."

                scene v15s7_6 # TPP Close up of Chloe's hand stroking MC's dick over his pants
                with dissolve

                cl "*Whispers* I won't mention it again."

                scene v15s7_1m # FPP Same as 1l, Chloe's mouth closed
                with dissolve

                u "Haha... Okay... Okay wait, you can mention whatever you want. *Chuckles*"

                scene v15s7_1i
                with dissolve

                cl "Haha, too late!"

                scene v15s7_4
                with dissolve

                pause 1
        
            scene v15s7_1i
            with dissolve

            cl "Later, gator."

            scene v15s7_1h
            with dissolve

            u "See ya, Chloe."

            scene v15s7_7 # FPP Show Chloe walking into the library
            with dissolve

            pause 0.75
        
            stop music fadeout 3
        
            jump v15s9

    else: # -if MC stole nothing from Chloe's room or never went to Chloe's room
        scene v15s6_2a # FPP Show Chloe near library door, smiling and chatting with two random students
        with dissolve

        u "(Oh, there's Chloe. Putting on the charm for support no doubt, haha.)"
        
        stop music fadeout 3
        
        play music "music/v13/Track Scene 8.mp3" fadein 2
        
        scene v15s7_8 # FPP At entrance to library, Chloe is talking to two random students, a man and a woman. Chloe smiling with mouth open
        with dissolve

        cl "...yeah, Lindsey has some nice posters, I'll give her that..."

        scene v15s7_8a # FPP Same angle as 8, Chloe holding up a finger to make a point, looking at the other random student, smiling with mouth open
        with dissolve

        cl "But a poster doesn't prove anything. *Chuckles* She doesn't have what it takes to be the Pres-"

        scene v15s7_8b # FPP Same angle as 8, Chloe looking at MC with a big smile, mouth open, random students not in shot
        with dissolve

        cl "Oh, hey [name]!"

        scene v15s7_8c # FPP Same angle as 8, Chloe looking at MC, slight smile with mouth closed, random students not in shot
        with dissolve

        u "Hey, Chloe."

        scene v15s7_8
        with dissolve

        cl "So, I can count on you guys for your support?"

        scene v15s7_9 # FPP Random student woman looking at Chloe, smiling with mouth open
        with dissolve

        fems "Yeah, sure!"

        scene v15s7_10 # FPP Random student man looking at Chloe, smiling with mouth open
        with dissolve

        males "Chloe for the win. No doubt."

        scene v15s7_8d # FPP Same angle as 8, Chloe looking at the random students, her hands clapped together, laughing with mouth open
        with dissolve

        cl "I love it! *Laughs* Thank you."

        scene v15s7_11 # FPP Show the two random students walking away down the hall
        with dissolve

        $ set_presidency_percent(v14_lindsey_popularity - 2)
        u "Chloe? Why do you care so much about two random people supporting you? Don't only Chicks have the right to vote?"

        scene v15s7_8b
        with dissolve

        cl "Yeah, but every Chick has friends outside the sorority. And every single one of them will be influenced by the opinion of the public."

        cl "That's why it's important that every person on campus supports me over Lindsey, not just Chicks."

        cl "The campaigning never stops."

        scene v15s7_8c
        with dissolve

        u "And the shit-talking Lindsey never stops either... Haha."

        scene v15s7_8b
        with dissolve

        cl "Hey, I say what I need to say to get the votes. That's politics. *Laughs*"

        scene v15s7_8c
        with dissolve

        u "You're a natural for this. *Chuckles*"

        scene v15s7_8e # FPP Same angle as 8, Chloe looking at MC with a shy smile, mouth open
        with dissolve

        cl "Aww, well thank you. I wish everyone felt that way, you know?"

        scene v15s7_8c
        with dissolve

        u "Yeah. But hey, that's politics. *Laughs*"

        scene v15s7_8b
        with dissolve

        cl "Nice...*Chuckles* Also true."

        if v14_help_chloe: # -if MC is helping Chloe
            cl "So, are we ready to get started for today?"

            scene v15s7_8c
            with dissolve

            u "Yes, I'm ready!"

            scene v15s7_8b
            with dissolve

            cl "Haha, let's go."

            scene v15s7_5
            with dissolve

            pause 0.75

            stop music fadeout 3

            jump v15s8

        else: # -if MC is not helping Chloe
            scene v15s7_8b
            #with dissolve
        
            cl "I should go get started on my next plan."

            scene v15s7_8c
            with dissolve

            u "Okay, I'll see you tonight? Lauren's party?"

            scene v15s7_8f # FPP Same angle as 8, Chloe looking at MC with neutral expression, mouth open
            with dissolve

            cl "Ah, no... I'm way too busy for a birthday party, haha. Have fun though!"

            scene v15s7_8c
            with dissolve

            u "Aw, okay. I'll try. *Chuckles*"

            if chloe.relationship >= Relationship.GIRLFRIEND:
                scene v15s7_8f
                with dissolve

                cl "I wish I could come though. I miss you..."

                scene v15s7_6
                with dissolve

                u "*Whispers* I wish you could cum too..."

                scene v15s7_8b
                with dissolve

                cl "*Giggles*"

                play sound "sounds/kiss.mp3"

                scene v15s7_4a # TPP Same as 4, Chloe giving MC a kiss, no mascara streaking
                with dissolve

                pause 1.75

            scene v15s7_8b
            with dissolve

            cl "Bye, [name]."

            scene v15s7_8c
            with dissolve

            u "Bye, Chloe. Good luck."

            scene v15s7_8b
            with dissolve

            cl "Thanks!"

            scene v15s7_7
            with dissolve

            pause 0.75
        
            stop music fadeout 3
        
            jump v15s9