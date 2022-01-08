# SCENE 18c: Lauren Halloween Party Free Roam part 2
# Locations: Deer's House/Rooms
# Characters: MC (Outfit: Stripper Costume), AUBREY (Outfit: Clown Costume), RYAN (Outfit: Elvis Costume), AUTUMN (Outfit: Mummy), PENELOPE (Outfit: Sexy Witch), LAUREN (Outfit: Spider necklace costume), IMRE (Outfit: Cowboy Costume), RILEY (Outfit: Schoolgirl Costume), CHRIS (Outfit: Boxer Costume), AMBER (Outfit: Black bloody nurse costume)
# Time: Night

label v15s18c:
    call screen v15s18a_livingroom

label v15s18c_riley:
    $ freeroam14.add("riley")

    scene v15s18c_ri_1 # TPP. Show MC walking into the bathroom, Riley adjusting her make up in front of the mirror, MC slightly startled, Riley slightly startled, both mouths closed
    #with dissolve

    pause 0.75

    scene v15s18c_ri_2 # FPP. MC in bathroom, Riley in front of mirror, Riley looking at MC through the mirror, she's still adjusting her make up, Riley slight smile, mouth closed
    with dissolve

    u "Oh- Hey, Riley. (I gotta start knocking...)"

    scene v15s18c_ri_2a # FPP. Same as v15s18c_ri_2, Riley slight smile, mouth open, change the positioning of her adjusting her makeup
    with dissolve

    ri "Hey, ever heard of knocking?"

    scene v15s18c_ri_2
    with dissolve

    u "Uh, yeah... Sounds familiar. *Laughs* Sorry."

    scene v15s18c_ri_2a
    with dissolve

    ri "Haha, no worries. I was just checking my makeup."

    if gift_card_50 in mc.inventory and lauren.relationship.value >= Relationship.GIRLFRIEND.value:
        scene v15s18c_ri_2b
        with dissolve

        ri "So, fifty bucks on your girlfriend's big day, huh? What a sugar daddy... *Chuckles*"

        scene v15s18c_ri_2c
        with dissolve

        u "Yeah, yeah..."

        scene v15s18c_ri_2b
        with dissolve

        ri "Next time you need to buy a gift for your girlfriend, just tell me. I can help, you know."

        scene v15s18c_ri_2c
        with dissolve

        menu:
            "Sounds great":
                $ add_point(KCT.BOYFRIEND)
                
                u "Seriously? That would be great, haha."

                if riley.relationship.value >= Relationship.FWB.value:
                    scene v15s18c_ri_2d # FPP. Same as v15s18c_ri_2c, Riley slightly sad, mouth open
                    with dissolve

                    ri "Yeah. Of course."
                
                else:
                    scene v15s18c_ri_2b
                    with dissolve

                    ri "Yeah, really. I'd be down whenever."

            "You can't shop for yourself":
                $ add_point(KCT.BRO)
                
                u "What? You can't shop for yourself, haha. That ruins the surprise."

                if riley.relationship.value >= Relationship.FWB.value:
                    scene v15s18c_ri_2e # FPP. Same as v15s18c_ri_2b, Riley smirking, mouth open
                    with dissolve

                    ri "Haha... You better watch yourself, handsome."
                
                else:
                    scene v15s18c_ri_2b
                    with dissolve

                    ri "Was that supposed to be a pick-up line? *Laughs* Wait, say it again?"

                    scene v15s18c_ri_2c
                    with dissolve

                    u "*Sighs* Nah, forget it."

        scene v15s18c_ri_2f # FPP. Same as v15s18c_ri_2b, different pose, slight smile, mouth open
        with dissolve

        ri "Besides... After the stunt you pulled tonight you need all the help you can get, haha."

        scene v15s18c_ri_2g # FPP. Same as v15s18c_ri_2f, slight smile, mouth closed
        with dissolve

        u "Yeah, hopefully she isn't too upset..."

        scene v15s18c_ri_2f
        with dissolve

        ri "Oh, please... It'll be just fine, [name]. She's having a good time."

        scene v15s18c_ri_2g
        with dissolve

        u "That's true, she is. She's had a smile on her face all night, apart from when she opened my gift..."

        scene v15s18c_ri_2h # FPP. Same as v15s18c_ri_2f, Riley putting her hand on MC's shoulder, slight smile, mouth open
        with dissolve

        ri "*Chuckles* Stop thinking about it and move on."

        scene v15s18c_ri_2g
        with dissolve

        u "Thanks. Good advice, Riley."

        scene v15s18c_ri_2f
        with dissolve

        ri "Anytime."

    elif gift_card_50 in mc.inventory: # and lauren.relationship == Relationship.FRIEND:
        scene v15s18c_ri_2b # FPP. Same as v15s18c_ri_2, Riley now turned to MC, not looking through the mirror anymore, Riley smiling, mouth open
        with dissolve

        ri "I can't believe you bought the same gift card as Imre..."

        scene v15s18c_ri_2c # FPP. Same as v15s18c_ri_2b, Riley smiling, mouth closed
        with dissolve

        u "Yeah... Neither can I, ha."

        u "*Sighs* It would have been a lot less embarrassing if she had opened mine first."

        scene v15s18c_ri_2b
        with dissolve

        ri "Haha, I wouldn't worry about it. Some people are really difficult to shop for."
    
    elif white_horse_black_mane in mc.inventory:
        scene v15s18c_ri_2b
        with dissolve

        ri "Nice job on the gift! Lauren really likes that little horse you bought her."

        scene v15s18c_ri_2c
        with dissolve

        u "Oh, thanks... Yeah, shame I didn't buy the right color though, ha."

        scene v15s18c_ri_2b
        with dissolve

        ri "Ah, don't worry about it."

        scene v15s18c_ri_2f
        with dissolve

        ri "It reminds her of the one from her childhood, and that was your goal, right?"

        scene v15s18c_ri_2g
        with dissolve

        u "That's true."

        scene v15s18c_ri_2g
        with dissolve

        ri "Of course it's true, why would I speak in lies?"
    
    elif brown_horse_golden_mane in mc.inventory:
        scene v15s18c_ri_2b
        with dissolve

        ri "Lauren is obsessed with that damn horse! *Laughs*"

        scene v15s18c_ri_2c
        with dissolve

        u "Good! Haha, luckily Autumn gave me that insider info."

        scene v15s18c_ri_2b
        with dissolve

        ri "Aw, that was sweet of her."

        scene v15s18c_ri_2c
        with dissolve

        u "For sure, Autumn is pretty great."

        scene v15s18c_ri_2b
        with dissolve

        ri "I don't know her that well, really. I should try to hang out with her more."

        scene v15s18c_ri_2c
        with dissolve

        u "Oh boy... You and Autumn in the same room together?"

        scene v15s18c_ri_2g
        with dissolve

        u "With your combined brainpower, you could take over the world. *Laughs*"

        scene v15s18c_ri_2f
        with dissolve

        ri "Take over the world... and fill it with puppies?!"

        scene v15s18c_ri_2g
        with dissolve

        u "That sounds like an extremely healthy ambition, haha. Good luck."

        scene v15s18c_ri_2f
        with dissolve

        ri "Why thank you, although I don't think we'll need it. Hehe..."
    
    elif (emerald_bracelet in mc.inventory or ruby_choker_necklace in mc.inventory) and lauren.relationship.value >= Relationship.GIRLFRIEND.value:
        scene v15s18c_ri_2b
        with dissolve

        ri "You did..."

        ri "An amazing job with Lauren's gift."

        scene v15s18c_ri_2c
        with dissolve

        u "Oh, phew... Thanks, haha."

        scene v15s18c_ri_2b
        with dissolve

        ri "It was stunning and she's clearly very happy with it, ha."

        scene v15s18c_ri_2c
        with dissolve

        u "I'm happy to hear that, it was pretty great to see how happy she was."

        scene v15s18c_ri_2g
        with dissolve

        u "I love seeing her smile, but being the reason for it is even better, you know?"

        if riley.relationship.value >= Relationship.FWB.value:
            scene v15s18c_ri_2i # FPP. Same as v15s18c_ri_2f, Riley slightly sad, looking down, mouth closed
            with dissolve

            pause 0.75

        scene v15s18c_ri_2f
        with dissolve

        ri "She'll be smiling for a long time after receiving that, haha."

        scene v15s18c_ri_2g
        with dissolve

        u "Ha, yeah hopefully."
    
    elif emerald_bracelet in mc.inventory or ruby_choker_necklace in mc.inventory: # and lauren.relationship == Relationship.FRIEND:
        scene v15s18c_ri_2b
        with dissolve

        ri "So, romantic jewelry? *Giggles* For a friend?"

        scene v15s18c_ri_2c
        with dissolve

        u "I don't-"

        u "I didn't know it would come off as weird, I swear."

        scene v15s18c_ri_2g
        with dissolve

        u "And the sales guy was all \"She'll be a friend for life!\" if I got her jewelry... *Sighs"

        scene v15s18c_ri_2f
        with dissolve

        ri "The sales guy?"

        scene v15s18c_ri_2g
        with dissolve

        u "Yeah, the-"

        scene v15s18c_ri_2f
        with dissolve

        ri "You mean the employee whose only goal and reason why he gets paid is to make sure people spend money?"

        scene v15s18c_ri_2g
        with dissolve

        u "Well, when you put it like that..."

        scene v15s18c_ri_2j # FPP. Same as v15s18c_ri_2g, Riley smiling, mouth closed, different pose
        with dissolve

        u "It sounds like he did his job well."

        scene v15s18c_ri_2k # FPP. Same as v15s18c_ri_2j, Riley smiling, mouth open
        with dissolve

        ri "Haha, he definitely did."

        scene v15s18c_ri_2j
        with dissolve

        u "*Sighs* Oh well. She didn't seem to hate it..."

        scene v15s18c_ri_2k
        with dissolve

        ri "Righttt... I wouldn't hate it either. Just a little creepy. *Chuckles*"

        scene v15s18c_ri_2j
        with dissolve

        u "(Okay, I'm done being bullied.)"

    scene v15s18c_ri_2j
    with dissolve

    u "Anyway... I'll leave you to it. Hurry up and get back to the party!"

    scene v15s18c_ri_2k
    with dissolve

    ri "Haha, okay! See you out there."

    scene v15s18c_ri_3 # TPP. Show MC leaving the bathroom, slight smile, mouth closed
    with dissolve

    pause 0.75

    call screen v15s18a_upstairsroom

label v15s18c_imre_aubrey:
    $ freeroam14.add("imre_aubrey")

    scene v15s18c_imau_1 # TPP. Show MC walking up to Imre and Aubrey, MC slight smile, mouth closed, Imre slight smile, mouth open, looking at Aubrey, Aubrey looking at Imre, mouth closed, slightly annoyed
    #with dissolve

    pause 0.75

    scene v15s18c_imau_2 # FPP. MC standing close to Aubrey and Imre, MC looking only at Imre, Imre looking at Aubrey, Imre slight smile, mouth open
    with dissolve

    imre "Did you see how happy she was with my gift card?"

    scene v15s18c_imau_3 # FPP. MC standing close to Aubrey and Imre, MC looking only at Aubrey, Aubrey looking at Imre, Aubrey slightly annoyed, mouth open
    with dissolve

    au "No, Imre. I didn't."

    scene v15s18c_imau_2a # FPP. Same as v15s18c_imau_2, Imre slightly annoyed, mouth open
    with dissolve

    imre "What do you mean?"

    scene v15s18c_imau_3
    with dissolve

    au "It was a gift card, Imre. Why would she be happy about that?"

    scene v15s18c_imau_2a
    with dissolve

    imre "You can buy whatever the fuck you want with it!"

    scene v15s18c_imau_3
    with dissolve

    au "Yeah, I understand the concept. It's just lazy."

    scene v15s18c_imau_2a
    with dissolve

    imre "If someone buys you a gift card in the future, you have to say that to their face."

    scene v15s18c_imau_3
    with dissolve

    au "That they're lazy? That it was a boring, sad, and lazy gift?"

    scene v15s18c_imau_4 # TPP. Show MC sitting down next to Aubrey, Imre very offended, mouth closed, Aubrey slightly annoyed, mouth open, Imre and Aubrey looking at each other
    with dissolve

    au "Okay. Done."

    scene v15s18c_imau_5 # FPP. MC sitting next to Aubrey, looking only at Imre, Imre looking at Aubrey, Imre slightly annoyed, mouth open
    with dissolve

    imre "I know sarcasm when I hear it, Aubrey."

    if gift_card_50 in mc.inventory:
        scene v15s18c_imau_5
        with dissolve

        imre "Obviously, it wasn't the worst idea since [name] got the exact same one. *Scoffs*"

        scene v15s18c_imau_5a # FPP. Same as v15s18c_imau_5, Imre looking at MC, Imre slightly annoyed, mouth closed
        with dissolve

        u "Imre, I didn't pick the same gift card as you on purpose. Are you fucking with me?"

        scene v15s18c_imau_5b # FPP. Same as v15s18c_imau_5a, Imre slightly annoyed, mouth open
        with dissolve

        imre "Wha- No! I mean... Yeah, I was just joking."

        scene v15s18c_imau_6 # FPP. MC sitting next to Aubrey, MC looking only at Aubrey, Aubrey looking at Imre, Aubrey slight smile, mouth open
        with dissolve

        au "Oh, is that why you've been calling him the gift copier?"

        scene v15s18c_imau_5a
        with dissolve

        u "Gift copier... Good one."

        scene v15s18c_imau_5b
        with dissolve

        imre "*Sighs* Alright, chill. I'm over it."

        scene v15s18c_imau_6
        with dissolve

        au "I would hope so... *Laughs*"

        scene v15s18c_imau_5
        with dissolve

        imre "Why are you being such a bitch tonight?"

        scene v15s18c_imau_5a
        with dissolve

        u "Whoa-"

        scene v15s18c_imau_5b
        with dissolve

        imre "Ohhh, okay... She gets to bully me about buying a gift card and I don't get to call her a bitch?"

        scene v15s18c_imau_5a
        with dissolve

        u "That's correct. Yeah."

        scene v15s18c_imau_6
        with dissolve

        au "*Giggles*"

        scene v15s18c_imau_5b
        with dissolve

        imre "Fuck this, man... I know Lauren's smiling right now because of me."

        scene v15s18c_imau_7 # FPP. MC watches as Imre storms off angrily
        with dissolve

        pause 0.75

    elif white_horse_black_mane in mc.inventory or brown_horse_golden_mane in mc.inventory:
        scene v15s18c_imau_6
        with dissolve

        au "A good gift is whatever the fuck [name] got, haha. It seemed to bring back some fun memories."

        scene v15s18c_imau_5
        with dissolve

        imre "Pfft... A toy?"

        scene v15s18c_imau_5a
        with dissolve

        u "Oh yeah, Autumn gave me the idea. I'm not sure what I would've gotten Lauren without her help, haha."

        scene v15s18c_imau_6a # FPP. Same as v15s18c_imau_6, Aubrey looking at MC, slight smile, mouth open
        with dissolve

        au "Hopefully not a gift card..."

        scene v15s18c_imau_6b # FPP. Same as v15s18c_imau_6a, Aubrey slight smile, mouth closed
        with dissolve

        u "Oh, God no... Of course not... *Chuckles*"

        scene v15s18c_imau_5b
        with dissolve

        imre "Okay-"

        scene v15s18c_imau_7
        with dissolve

        pause 0.75

    elif (emerald_bracelet in mc.inventory or ruby_choker_necklace in mc.inventory) and lauren.relationship.value >= Relationship.GIRLFRIEND.value:
        scene v15s18c_imau_6
        with dissolve

        au "An actual good gift was the jewelry that [name] got."

        scene v15s18c_imau_6b
        with dissolve

        u "Ha, thanks. Her reaction couldn't have been better."

        scene v15s18c_imau_5
        with dissolve

        imre "Yeah, but still... With my gift card, she can go out and buy something even better than that."

        scene v15s18c_imau_6
        with dissolve

        au "Imre, drop it. Your gift card was trash."

        scene v15s18c_imau_5a
        with dissolve

        u "What's better than jewelry?"

        scene v15s18c_imau_5b
        with dissolve

        imre "Umm, a lot of things?"

        scene v15s18c_imau_6
        with dissolve

        au "Go ahead, Imre. Name one. Name one thing that's better than jewelry."

        scene v15s18c_imau_5
        with dissolve

        imre "You know what? I don't need this."

        scene v15s18c_imau_7
        with dissolve

        pause 0.75

    elif emerald_bracelet in mc.inventory or ruby_choker_necklace in mc.inventory: # and lauren.relationship == Relationship.FRIEND:
        scene v15s18c_imau_5c # FPP. Same as v15s18c_imau_5b, Imre slight smile, mouth open
        with dissolve

        imre "At least I didn't buy her a romantic piece of jewelry, haha! That was so fucking awkward, dude."

        scene v15s18c_imau_5d # FPP. Same as v15s18c_5c, Imre slight smile, mouth closed
        with dissolve

        u "Seriously, guys... I didn't know it'd be weird."

        scene v15s18c_imau_6
        with dissolve

        au "I think getting creepy jewelry is much better than getting a plain piece of plastic with money on it..."

        u "(Creepy jewelry?)"

        scene v15s18c_imau_5
        with dissolve

        imre "Aubrey, enough is enough! My gift card is the reason that Lauren is so happy right now. Admit it."

        scene v15s18c_imau_6
        with dissolve

        au "Haha!"

        au "Okay, keep telling yourself that."

        scene v15s18c_imau_5
        with dissolve

        imre "I will."

        scene v15s18c_imau_7
        with dissolve

        pause 0.75

    scene v15s18c_imau_6a
    with dissolve

    au "*Laughs* Nice job! I've been trying to scare him away for years..."

    scene v15s18c_imau_6b
    with dissolve

    u "Haha, don't blame that on me! You're the one who got him fired up."

    scene v15s18c_imau_6a
    with dissolve

    au "Who cares? It's too easy. *Laughs*"

    scene v15s18c_imau_6b
    with dissolve

    u "Very true."

    if not v15s18_mention_list_aubrey:
        u "(Now is a good time to check something off the list, should I ask Aubrey for help?)"

        menu:
            "Ask for help":
                $ add_point(KCT.TROUBLEMAKER)
                $ add_point(KCT.BRO)
                
                u "So, I'm just curious..."

                scene v15s18c_imau_6c
                with dissolve

                au "Yeah?"

                scene v15s18c_imau_6d
                with dissolve

                u "If I told you I had this dumb list of tasks to complete by the end of the night, would you want to help me?"

                scene v15s18c_imau_6c
                with dissolve

                au "Hmm... What kind of tasks? *Laughs*"

                scene v15s18c_imau_6d
                with dissolve

                u "Uh, well..."

                scene v15s18c_imau_6e # FPP. Same as v15s18c_6d, MC handing the list to Aubrey, Aubrey grabbing the list, slight smile, mouth closed
                with dissolve

                pause 0.75

                scene v15s18c_imau_6f # FPP. Same as v15s18c_imau_6c, Aubrey looking at the list, slightly surprised, mouth open
                with dissolve

                au "Oh! Haha..."

                scene v15s18c_imau_6g # FPP. Same as v15s18c_imau_6f, Aubrey smirking, mouth closed, looking at MC
                with dissolve

                u "Yeah... I just thought I'd ask because-"
    
            "Don't mention it":
                $ add_point(KCT.BOYFRIEND)
                
                u "(Not feeling it...)"

                scene v15s18c_imau_6c # FPP. Same as v15s18c_imau_6a, Aubrey different pose, slight smile, mouth open
                with dissolve

                au "This might be shocking... But I'm kind of ready to leave, haha."

                scene v15s18c_imau_6d # FPP. Same as v15s18c_imau_6c, Aubrey slight smile, mouth closed
                with dissolve

                u "Wait, really? *Laughs* Since when do you get tired before midnight?"

                scene v15s18c_imau_6c
                with dissolve

                au "Right? I guess it's just been a lot lately, modelling and the wedding."

                scene v15s18c_imau_6d
                with dissolve

                u "Yeah. makes sense."

                u "You definitely need to get a good rest or else you'll be falling asleep during the vows, haha."

                scene v15s18c_imau_6c
                with dissolve

                au "*Chuckles* Yeah, I'm going to."

                scene v15s18c_imau_6d
                with dissolve

                u "Good..."

                u "I'm going to talk to the others before it's time to go, find me if you need me, yeah?"

                scene v15s18c_imau_6c
                with dissolve

                au "Okay. Will do."

                scene v15s18c_imau_6a
                with dissolve

                pause 0.75

                scene v15s18c_imau_8 # TPP. Show MC getting up and leaving, Aubrey stays behind, both slight smiles, mouths closed
                with dissolve

                pause 0.75

                call screen v15s18a_room

    else:
        scene v15s18c_imau_6c
        with dissolve

        au "So... Do you still need some help with that list you mentioned earlier?"

        scene v15s18c_imau_6d
        with dissolve

        u "Yeah, if you want-"

    scene v15s18c_imau_9 # TPP. Show Aubrey getting up, pulling MC by the arm, mouth open, looking sexily at him, MC slightly surprised, mouth closed
    with dissolve

    au "Come on then..."

    scene v15s18c_imau_10 # TPP. Show Aubrey leading MC upstairs (don't show Lauren in background please), both have sexy expressions, mouths closed
    with dissolve

    pause 0.75

    scene v15s18c_imau_11 # TPP. Show MC and Aubrey entering Aubrey's room, Aubrey smiling, mouth open, MC slightly worried, mouth closed
    with dissolve

    au "*Whispers* Nice! There's nobody in here..."

    scene v15s18c_imau_12 # FPP. MC and Aubrey in Autumn's room, Aubrey looking at MC, sexy expression, mouth closed
    with dissolve

    u "Autumn's room?"

    scene v15s18c_imau_12a # FPP. Same as v15s18c_imau_12, Aubrey sexy expression, mouth open
    with dissolve

    au "Yeah, so? What she doesn't know won't hurt her, hehe."

    scene v15s18c_imau_12
    with dissolve

    u "(Well, when you put it like that...)"

    scene v15s18c_imau_13 # TPP. Close up of Aubrey removing the bottom half of her costume
    with dissolve

    pause 0.75

    scene v15s18c_imau_14 # TPP. Close up of Aubrey getting on the bed, mouth open, sexy expression
    with dissolve

    au "Okay..."

    scene v15s18c_imau_15 # FPP. Aubrey laying on the bed, spreading her legs open, looking sexily of MC, mouth open
    with dissolve

    au "I'm all yours for pleasing."

    scene v15s18c_imau_15a # FPP. Same as v15s18c_imau_15, Aubrey looking sexily at MC, mouth closed
    with dissolve

    u "(Ha... Damn...)"

    scene v15s18c_imau_16 # TPP. Show MC joining Aubrey in bed, both looking sexily at each other, mouths closed
    with dissolve

    pause 0.75

    scene v15s18c_imau_17 # TPP. Show MC and Aubrey making out
    with dissolve

    pause 0.75

    scene v15s18c_imau_17a # TPP. Same as v15s18c_imau_17, making out more passionately, MC grabbing her breasts
    with dissolve

    pause 0.75

    scene v15s18c_imau_18 # TPP. Show MC kissing Aubrey's neck, Aubrey biting her lip, mouth closed
    with dissolve

    pause 0.75

    scene v15s18c_imau_19 # TPP. Show MC kissing Aubrey's abdomen, Aubrey mouth open, moaning
    with dissolve

    au "*Moans* Touch me..."

    scene v15s18c_imau_20 # TPP. Show MC licking Aubrey's clit
    with dissolve

    au "*Gasps* [name]..."

    scene v15s18c_imau_21 # TPP. Show MC positioning himself to finger Aubrey, Aubrey looking at him desperately, mouth open
    with dissolve

    au "Please."

    scene v15s18c_imau_22 # TPP. Show MC getting ready to put his finger inside her, looking at Aubrey, Aubrey looking at him, both looking sexily at each other, MC mouth open, Aubrey mouth closed
    with dissolve

    u "How about a finger?"

    image v15aubfin = Movie(play="images/v15/Scene 18c/v15aubfin.webm", loop=True, image="images/v15/Scene 18c/v15aubfinStart.webp", start_image="images/v15/Scene 18c/v15aubfinStart.webp") 
    image v15aubfinf = Movie(play="images/v15/Scene 18c/v15aubfinf.webm", loop=True, image="images/v15/Scene 18c/v15aubfinStart.webp", start_image="images/v15/Scene 18c/v15aubfinStart.webp") 
    image v15aubfin2 = Movie(play="images/v15/Scene 18c/v15aubfin2.webm", loop=True, image="images/v15/Scene 18c/v15aubfin2Start.webp", start_image="images/v15/Scene 18c/v15aubfin2Start.webp")
    image v15aubfin2f = Movie(play="images/v15/Scene 18c/v15aubfin2f.webm", loop=True, image="images/v15/Scene 18c/v15aubfin2Start.webp", start_image="images/v15/Scene 18c/v15aubfin2Start.webp")

    scene v15aubfin # IGNORE AS ANIMATION
    with dissolve

    pause 0.75

    au "Oh... Shhit... *Moans*"

    u "How does that feel?"

    au "Ha... *Panting* It feels amazing."

    scene v15aubfinf # IGNORE AS ANIMATION
    with dissolve

    pause 0.75
   
    au "*Moans* Yes... [name], please..."

    au "Mmm, fuck!"

    au "*Moans* YES!"

    scene v15aubfin2Start # IGNORE AS ALREADY RENDERED
    with dissolve

    menu:
        "Keep her quiet":
            $ add_point(KCT.BOYFRIEND)
            
            scene v15aubfin2 # IGNORE AS ANIMATION
            with dissolve

            pause 0.75

            u "Shh, shh, shh..."

            u "We don't want anyone interrupting us, do we?"

            scene v15aubfin2f # IGNORE AS ANIMATION
            with dissolve

            pause 0.75

            au "*Moans* N-no."
    
        "Let her be loud":
            $ add_point(KCT.TROUBLEMAKER)
            
            scene v15aubfin2
            with dissolve

            pause 0.75

            u "Ha, scream for me."

            au "*Moans* You- OH!"

            scene v15aubfin2f 
            with dissolve

            pause 0.75

            au "Fuck... You don't want that... Haha... *Moans*"

            u "(Maybe. But I definitely don't want anyone else to hear her, haha. Hmm...)"

    scene v15s18c_imau_23 # TPP. Show MC positioning himself so he can cover Aubrey's mouth with one hand while he fingers her with the other hand
    with dissolve

    pause 0.75
    
    image v15aubfing = Movie(play="images/v15/Scene 18c/v15aubfing.webm", loop=True, image="images/v15/Scene 18c/v15aubfingStart.webp", start_image="images/v15/Scene 18c/v15aubfingStart.webp") 
    image v15aubfingf = Movie(play="images/v15/Scene 18c/v15aubfingf.webm", loop=True, image="images/v15/Scene 18c/v15aubfingStart.webp", start_image="images/v15/Scene 18c/v15aubfingStart.webp") 
    image v15aubfing2 = Movie(play="images/v15/Scene 18c/v15aubfing2.webm", loop=True, image="images/v15/Scene 18c/v15aubfing2Start.webp", start_image="images/v15/Scene 18c/v15aubfing2Start.webp")
    image v15aubfing2f = Movie(play="images/v15/Scene 18c/v15aubfin2gf.webm", loop=True, image="images/v15/Scene 18c/v15aubfing2Start.webp", start_image="images/v15/Scene 18c/v15aubfing2Start.webp")

    scene v15aubfing # IGNORE AS ANIMATION
    with dissolve

    pause 0.75

    au "Mmm!"

    scene v15aubfingf # IGNORE AS ANIMATION
    with dissolve

    pause 0.75

    u "Faster?"

    scene v15aubfing2 # IGNORE AS ANIMATION
    with dissolve

    pause 0.75

    au "*Moans*"

    scene v15aubfing2f # IGNORE AS ANIMATION
    with dissolve

    pause 0.75

    u "You're so wet..."

    au "Mmm, mmm! *Moans*"

    scene v15s18c_imau_24 # TPP. MC fingering Aubrey, no longer covering her mouth (make it similar to the first animation positioning), Aubrey moaning, mouth open
    with dissolve

    au "I'm-"

    scene v15aubfin
    with dissolve

    pause 0.75

    au "Ffffuck... [name]."

    u "Are you gonna cum for me?"

    scene v15aubfinf
    with dissolve

    pause 0.75

    au "*Whispers* Yes..."

    u "Now?"

    scene v15aubfin2
    with dissolve

    pause 0.75

    au "Mmm, yes... *Moans* I-"

    scene v15aubfin2f
    with dissolve

    pause 0.75

    au "Fuck... Oh, [name]..."

    au "*Moans* I'm gonna cum."

    scene v15s18c_imau_25 # TPP. MC fingering Aubrey (finger not fully inside, Aubrey moaning, mouth closed (don't show MC's face), she is cumming her, make this very intense (maybe pulling bedsheets), finger fully inserted
    with dissolve

    u "Yeah?"

    scene v15s18c_imau_25a # TPP. Same as v15s18c_imau_25, Aubrey moaning, mouth open, she is cumming her, make this very intense (maybe pulling bedsheets), finger fully inserted
    with vpunch

    au "Yessss... Yes, yes!"

    scene v15s18c_imau_25
    with dissolve

    u "(And... check.)"

    scene v15s18c_imau_25a
    with dissolve

    au "*Groans*"

    scene v15s18c_imau_26 # FPP. MC in same position as fingering position, not fingering anymore Aubrey laying down, looking at the roof, MC looking at Aubrey, Aubrey smiling/excited (she just cummed so), mouth open
    with dissolve

    au "*Panting* Holy shit, [name]."

    scene v15s18c_imau_26a # FPP. Same as v15s18c_imau_26, Aubrey mouth closed
    with dissolve

    u "*Chuckles* Looked like you enjoyed that."

    scene v15s18c_imau_26
    with dissolve

    au "Yes... *Panting*"

    scene v15s18c_imau_27 # TPP. Show Aubrey taking MC's hands towards her mouth, mouth closed, sexy expression
    with dissolve

    pause 0.75

    scene v15s18c_imau_28 # TPP. Show Aubrey licking MC's hands
    with dissolve

    au "Mmmm..."

    scene v15s18c_imau_29 # FPP. MC standing up in front of Aubrey, she's now sitting up, Aubrey looking at MC, mouth open, sexy expression
    with dissolve

    au "I really, really, really did."

    scene v15s18c_imau_29a # FPP. Same as v15s18c_imau_29, Aubrey mouth closed, sexy expression
    with dissolve

    u "Well, I'm glad. And thank you, haha."

    scene v15s18c_imau_29
    with dissolve

    au "Are you kidding?"

    scene v15s18c_imau_29a
    with dissolve

    u "What?"

    scene v15s18c_imau_29
    with dissolve

    au "Thank me? Thank you."

    scene v15s18c_imau_30 # TPP. Show Aubrey moving to stand up in front of MC, both sexy expressions, mouths closed
    with dissolve

    pause 0.75

    scene v15s18c_imau_31 # TPP. Show Aubrey giving MC a passionate kiss
    with dissolve

    pause 0.75

    scene v15s18c_imau_32 # FPP. Aubrey standing in front of MC, Aubrey mouth closed, sexy expression
    with dissolve

    u "*Gulps* You're welcome."

    scene v15s18c_imau_32a # FPP. Same as v15s18c_imau_32, Aubrey mouth open, sexy expression
    with dissolve

    au "We better get back to the party now, heh."

    scene v15s18c_imau_32
    with dissolve

    u "Yeah, good idea, haha."

    if aubrey.relationship.value >= Relationship.FWB.value:
        scene v15s18c_imau_32a
        with dissolve

        au "I'll miss you."

    scene v15s18c_imau_33 # TPP. Close up of Aubrey getting dressed (pulling her panties up)
    with dissolve

    pause 0.75

    scene v15s18c_imau_34 # FPP. MC watches as Aubrey walks out of the room, she looks back at him over her shoulders, sexy expression, winking, mouth closed
    with dissolve

    $ sceneList.add("v15_aubrey")

    $ checklist[4].complete = True
    u "*Exhales* (Damn, what a night so far.)"

    scene v15s18c_imau_35 # TPP. Show MC walking towards the door, mouth closed, smiling
    with dissolve

    pause 0.75

    scene v15s18c_imau_36 # FPP. MC looks at a pile of folded clothes on a chair, there are some panties on top of the pile
    with dissolve

    u "(Now would be the perfect chance to steal a pair of panties for the list... I just hope Autumn won't notice.)"

    menu:
        "Steal the panties":
            $ add_point(KCT.TROUBLEMAKER)
            $ add_point(KCT.BRO)
            
            u "(Sorry, Autumn. I'm a man in need.)"

            scene v15s18c_imau_37 # TPP. Show MC taking the panties, smiliing, mouth closed
            with dissolve

            $ checklist[6].complete = True
            u "(Double check.)"

        "Don't steal the panties":
            $ add_point(KCT.BOYFRIEND)
            
            if lauren.relationship.value >= Relationship.GIRLFRIEND.value:
                u "(There's no way in hell I'm taking my girlfriend's sister's underwear. Not happening.)"

            else:
                u "(There's no way I'm taking those. Bad idea. Very, very bad idea.)"
        
    scene v15s18c_imau_38 # TPP. Show MC leaving the room, smiling, mouth closed
    with dissolve

    pause 0.75

    call screen v15s18a_room

label v15s18c_ryan:
    $ freeroam14.add("ryan")
    scene v15s18c_ry_1 # TPP. Show MC walking up to Ryan (Ryan is sleeping on the couch), MC mouth closed, slightly confused (make sure there is a visible condom in his shirt pocket)
    #with dissolve

    pause 0.75

    scene v15s18c_ry_2 # FPP. MC standing in front of Ryan, Ryan sleeping, mouth closed
    with dissolve

    u "Ryan? Are you sleeping?"

    scene v15s18c_ry_2a # FPP. Same as v15s18c_ry_2, Ryan mouth slightly open, still sleeping
    with dissolve

    ry "*Groans*"

    scene v15s18c_ry_2
    with dissolve

    u "Damn, dude... Still not feeling well?"

    scene v15s18c_ry_2a
    with dissolve

    ry "*Whining*"

    scene v15s18c_ry_2
    with dissolve

    u "(For fuck's sake...)"

    scene v15s18c_ry_2a
    with dissolve

    ry "I've gotten sick so many times I lost count."

    scene v15s18c_ry_2
    with dissolve

    u "Ugh, I'm sorry man. I wish I could do something to help."

    scene v15s18c_ry_2a
    with dissolve

    ry "Keep me away from candy. Forever..."

    scene v15s18c_ry_2
    with dissolve

    u "Ha, alright. Noted."

    scene v15s18c_ry_2b # FPP. Same as v15s18c_ry_2a, Ryan slightly sad, mouth open, still sleeping
    with dissolve

    ry "No... *Sniffles* There's nothing anyone can do."

    scene v15s18c_ry_2c # FPP. Same as v15s18c_ry_2b, Ryan mouth closed
    with dissolve

    u "(Is he... crying?)"

    scene v15s18c_ry_2b
    with dissolve

    ry "I'm gonna sleep now."

    scene v15s18c_ry_2c
    with dissolve

    u "Alright, are you sure you're okay?"

    scene v15s18c_ry_2a
    with dissolve

    ry "..."

    scene v15s18c_ry_2
    with dissolve

    u "Ryan?"

    ry "*Snoring*"

    u "*Sighs*"

    scene v15s18c_ry_3 # FPP. MC llooking at the condom sticking out of Ryan's shirt
    with dissolve

    u "(Oh, wait! I need that condom if I want to complete the list...)"

    menu:
        "Take the condom":
            $ add_point(KCT.TROUBLEMAKER)
            
            scene v15s18c_ry_4 # TPP. Show MC slowly grabbing the condom out of Ryan's pocket (it's fully in the poocket still)
            with dissolve

            u "(Sorry, bro...)"

            scene v15s18c_ry_4a # TPP. Same as v15s18c_ry_4, condom halfway out, Ryan moves, startling MC a bit
            with dissolve

            ry "*Groans*"

            u "(Fuck!)"

            ry "..."

            scene v15s18c_ry_4b # TPP. Same as v15s18c_ry_4a, condom fully out
            with dissolve

            u "Phew..."

            scene v15s18c_ry_5 # TPP. Show MC backing off, looking down at the condom, smiling, mouth closed
            with dissolve

            u "(This thing is definitely expired. *Laughs*)"

            scene v15s18c_ry_6 # FPP. MC standing up, backed off, looking at Ryan sleeping, Ryan snoring
            with dissolve

            $ checklist[7].complete = True
            u "*Whispers* Hey, thanks man!"

            ry "*Snoring*"

        "Don't take it":
            $ add_point(KCT.BRO)
            
            scene v15s18c_ry_2
            with dissolve

            u "(Ah, I can't do that to him...)"

            u "(He's probably had that thing for a few years, it'd be like stealing his best friend. *Laughs*)"

    scene v15s18c_ry_6
    with dissolve

    u "Good luck, Ryan."

    scene v15s18c_ry_7 # TPP. Show MC walking away from Ryan, smiling, mouth closed
    with dissolve

    pause 0.75

    call screen v15s18a_livingroom

label v15s18c_lauren:
    $ freeroam14.add("lauren")

    scene v15s18c_la_1 # TPP. Show MC walking on to the balcony, Lauren already there, looking at the view, both slight smiles, mouths closed
    #with dissolve

    pause 0.75

    scene v15s18c_la_2 # TPP. Show MC standing next to Lauren, both leaning on the rail, facing the view, mouths closed, slight smile, not looking at each other
    with dissolve

    pause 0.75

    scene v15s18c_la_3 # FPP. MC standing next to Lauren, Lauren looking at him,, slight smile, mouth closed
    with dissolve

    u "Hey, there you are. Hiding from your own party? *Laughs*"

    scene v15s18c_la_3a # FPP. Same as v15s18c_la_3, Lauren slight smile, mouth open
    with dissolve

    la "Oh, hey. *Chuckles*"

    la "No, I'm having a great time... Just taking a moment to soak it all in, you know?"

    scene v15s18c_la_3
    with dissolve

    u "Yeah, I get it."

    scene v15s18c_la_4 # TPP. Show MC and Lauren looking up at the sky, both slightly smiling, mouths closed
    with dissolve

    pause 0.75

    scene v15s18c_la_3
    with dissolve

    u "It's so nice up here."

    scene v15s18c_la_3a
    with dissolve

    la "Yeah, it is. I was a little salty about Autumn getting the bigger room when we first moved in, but..."

    la "I got this instead."

    scene v15s18c_la_3
    with dissolve

    menu:
        "Balcony is better":
            $ add_point(KCT.BOYFRIEND)

            $ add_point(KCT.BOYFRIEND)

            u "Eh, I like the balcony a lot better. I'd be out here all the time if I were you, haha."

            scene v15s18c_la_3a
            with dissolve

            la "*Chuckles* I am out here a lot, it's just relaxing."

        "Bigger the better":
            $ add_point(KCT.BRO)

            $ add_point(KCT.BRO)

            u "Yeah... Having a small room kind of sucks, the bigger the better in my opinion."

            scene v15s18c_la_3a
            with dissolve

            la "I mean it does suck sometimes, but I'd rather have this."

            scene v15s18c_la_3
            with dissolve

            u "To each their own, ha."

    scene v15s18c_la_3b # FPP. Same as v15s18c_la_3a, Lauren mouth open, looking at the view instead of at MC, slight smile
    with dissolve

    la "I can't believe how stressed I was about this party... I thought everything was going wrong, but... no."

    scene v15s18c_la_3a
    with dissolve

    la "It's all been perfect so far and everyone showed up! *Laughs*"

    scene v15s18c_la_3
    with dissolve

    u "Haha, of course everyone showed up! You're a pretty popular girl, Lauren."

    scene v15s18c_la_3a
    with dissolve

    la "Ha... I guess I just didn't see myself that way."

    scene v15s18c_la_3b
    with dissolve

    la "I'm so grateful for all of our friends."

    scene v15s18c_la_3c # FPP. Same as v15s18c_la_3b, Lauren mouth closed, slight smile
    with dissolve

    u "Me too, really. Everyone seems to be having a great time, too."

    if "ryan" in freeroam13 or "ryan" in freeroam14:
        scene v15s18c_la_3
        with dissolve

        u "Well, everyone besides Ryan..."

        scene v15s18c_la_3a
        with dissolve

        la "*Laughs* I know! *Sighs* I shouldn't be laughing..."
    
    else:
        scene v15s18c_la_3a
        with dissolve

        la "Besides Ryan, haha! He's been getting sick all night. Something about eating too much. *Giggles*"

    scene v15s18c_la_3
    with dissolve

    u "Haha, did he arrive like that? What even happened to him?"

    scene v15s18c_la_3b
    with dissolve

    la "No idea, ha."

    scene v15s18c_la_3a
    with dissolve

    la "He looked okay when he first got here, but I do remember him holding his stomach a lot."

    la "Then he just disappeared into the bathroom for ages."

    scene v15s18c_la_3
    with dissolve

    u "Jeez... Poor Ryan."

    scene v15s18c_la_3b
    with dissolve

    la "Hopefully he can recover enough to walk home."

    scene v15s18c_la_3c
    with dissolve

    u "*Scoffs*"

    scene v15s18c_la_3a
    with dissolve

    la "I mean, uh... Hopefully he feels better soon... *Giggles*"

    scene v15s18c_la_3
    with dissolve

    u "*Laughs* Yeah, I hope so too."

    if lauren.relationship.value >= Relationship.GIRLFRIEND.value:
        scene v15s18c_la_3
        with dissolve

        u "By the way, you look amazing tonight."

        scene v15s18c_la_3a
        with dissolve

        la "Aww! Come here, you."

        scene v15s18c_la_5 # TPP. Show Lauren giving MC a kiss
        with dissolve

        pause 0.75

        scene v15s18c_la_6 # FPP. Lauren now standing right in front of MC, slight smile, mouth open
        with dissolve

        la "Thank you, [name]."

        scene v15s18c_la_6a # FPP. Same as v15s18c_la_6, Lauren mouth closed
        with dissolve

        u "You're very welcome."

        scene v15s18c_la_7 # TPP. Show Lauren going back to her original position, blushing, mouth closed
        with dissolve

        pause 0.75

        scene v15s18c_la_3b
        with dissolve

        la "I don't know if I've ever felt happier... Ha."

        scene v15s18c_la_3
        with dissolve

        u "Me either."
    
    scene v15s18c_la_3d # FPP. Same as v15s18c_la_3a, Lauren mouth open, slightly worried
    with dissolve

    la "Well, speaking of Ryan..."

    la "*Sighs* I should take him some water and see how he's doing."

    scene v15s18c_la_3
    with dissolve

    u "Maybe. Or maybe you're always looking out for other people, and not enough for yourself..."

    scene v15s18c_la_3a
    with dissolve

    la "Hehe, that's what you're here for."

    scene v15s18c_la_8 # FPP. MC watches as Lauren walks inside, she looks back at him over her shoulder, winking at him, mouth closed
    with dissolve

    u "(Cheeky...)"

    scene v15s18c_la_9 # TPP. Show MC walking back inside, slight smile, mouth closed
    with dissolve

    pause 0.75

    call screen v15s18a_upstairsroom

label v15s18c_autumn_amber:
    $ freeroam14.add("autumn_amber")

    scene v15s18c_auam_1 # FPP. MC watchign Amber and Autumn at the bar from a slight distance, Autumn and Amber smiling, Autumn mouth open, Amber mouth closed
    #with dissolve

    aut "Haha, I swear! I have no idea what strain it is, I've never asked."

    scene v15s18c_auam_1a # FPP. Same as v15s18c_auam_1, Amber mouth open, Autumn mouth closed
    with dissolve

    am "Really?!"

    scene v15s18c_auam_1
    with dissolve

    aut "Really."

    scene v15s18c_auam_1a
    with dissolve

    am "Autumn, your entire world is going to open up once you start exploring different strains."

    scene v15s18c_auam_1
    with dissolve

    aut "*Laughs* You think so?"

    scene v15s18c_auam_2 # TPP. Show MC walking up to them at the bar, Amber rolling her eyes sarcastically, both mouths closed, smiling
    with dissolve

    pause 0.75

    scene v15s18c_auam_3 # FPP. MC standing in front of them, Amber and Autumn looking at each other, Amber mouth open, smiling, Autumn mouth closed, smiling
    with dissolve

    am "There are thousands of them, dude. And you can get blends, too."

    scene v15s18c_auam_3a # FPP. Same as v15s18c_auam_3, Autumn mouth open, Amber mouth closed
    with dissolve

    aut "Blends? Like coffee?"

    scene v15s18c_auam_3
    with dissolve

    am "Haha, yes! It's exactly like coffee you basic bitch."

    scene v15s18c_auam_3a
    with dissolve

    aut "*Gasps* How dare you? Haha."

    scene v15s18c_auam_3b # FPP. Same as v15s18c_auam_3, both looking at MC, both mouths closed, both smiling
    with dissolve

    u "Should I interfere in this drug debate?"

    scene v15s18c_auam_3c # FPP. Same as v15s18c_auam_3b, Amber mouth open, Autumn mouth closed
    with dissolve

    am "Maybe, ha."

    if v14_amber_clean:
        am "Although obviously... I don't do that anymore. But I can at least pass on my wisdom to others."

        scene v15s18c_auam_3b
        with dissolve

        u "True, true."

    scene v15s18c_auam_3c
    with dissolve

    am "I'm just excited to find someone interested in this stuff."

    scene v15s18c_auam_3b
    with dissolve

    u "I never would've expected you two hanging out together... Now I'm worried that I should start a bail fund."

    scene v15s18c_auam_3d # FPP. Same as v15s18c_auam_3b, Autumn mouth open, Amber mouth closed
    with dissolve

    aut "*Laughs* Don't worry about that, I can get us out of anything usually."

    scene v15s18c_auam_3
    with dissolve

    am "Haha, yes! That's my girl."

    scene v15s18c_auam_3b
    with dissolve

    u "Oh boy..."

    scene v15s18c_auam_3
    with dissolve

    am "I'll teach you a thing or two about weed, and you can show me your big brain power. *Chuckles*"

    scene v15s18c_auam_3a
    with dissolve

    aut "Okay, haha. Fair."

    scene v15s18c_auam_3a
    with dissolve

    am "I'm gonna run to the bathroom, be right back."

    scene v15s18c_auam_3b
    with dissolve

    u "I'll keep your spot warm!"

    scene v15s18c_auam_3c
    with dissolve

    am "You better be gone when I return!"

    scene v15s18c_auam_4 # TPP. Show Amber walking away to the bathroom, MC takes her seat, all smiling, MC and Amber mouth closed, watching her walk off, Autumn mouth open
    with dissolve

    aut "Haha, she's something."

    scene v15s18c_auam_5 # FPP. MC sitting next to Autumn, Autumn slight smile, mouth closed
    with dissolve

    u "Yes, yes, she is. *Chuckles*"

    scene v15s18c_auam_5a # FPP. Same as v15s18c_auam_5, Autumn slight smile, mouth open
    with dissolve

    aut "So, what have you been up to all night?"

    if not v15s18a_showlist_penelope_autumn:
        menu:
            "Mention the list":
                $ add_point(KCT.TROUBLEMAKER)
                
                scene v15s18c_auam_5
                with dissolve

                u "Well, you might have already heard, but I have this list of challenges that I've been working on."

                scene v15s18c_auam_5a
                with dissolve

                aut "Haha, yeah? I think I might have overheard something about that."

                scene v15s18c_auam_5
                with dissolve

                u "Oh... *Chuckles*"

                u "Well, I do have an easy one left, if you'd like to help me out?"
        
            "Don't mention the list":
                $ add_point(KCT.BOYFRIEND)
                
                scene v15s18c_auam_5
                with dissolve

                u "(Eh, I don't want to get Autumn involved in this...)"

                u "Honestly? I've just been making my rounds and trying to stay caught up with everyone, haha."

                scene v15s18c_auam_5a
                with dissolve

                aut "Yeah, I get that. Parties aren't exactly my thing either."

                scene v15s18c_auam_5
                with dissolve

                u "I don't mind them, there's always a lot going on though."

                scene v15s18c_auam_5a
                with dissolve

                aut "Speaking of a lot... I have a shit ton of homework."

                scene v15s18c_auam_5
                with dissolve

                u "Really?"

                scene v15s18c_auam_5a
                with dissolve

                aut "Look, I know it's nerdy to leave a party early for-"

                scene v15s18c_auam_5
                with dissolve

                u "You are a nerd."

                scene v15s18c_auam_5b # FPP. Same as v15s18c_auam_5a, Autumn larger smile, different pose, mouth open 
                with dissolve

                aut "Okay, fine! I'm a nerd!"

                scene v15s18c_auam_5c # FPP. Same as v15s18c_auam_5b, Autumn mouth closed
                with dissolve

                u "You wanna shout a little louder? *Chuckles*"

                scene v15s18c_auam_5b
                with dissolve

                aut "Haha, anyway... I should go get some work done before bed."

                scene v15s18c_auam_5c
                with dissolve

                u "Okay, okay. It was fun seeing you again, and great work on the decorations."

                scene v15s18c_auam_5b
                with dissolve

                aut "Oh, thank you! I'm glad everyone had fun tonight. I'll see you soon."

                scene v15s18c_auam_5c
                with dissolve

                u "Later. Good luck."

                scene v15s18c_auam_6 # FPP. MC watches as Autumn walks off
                with dissolve

                pause 0.75

                scene v15s18c_auam_7 # TPP. Show MC walking off, slight smile, mouth closed
                with dissolve

                pause 0.75

                call screen v15s18a_bar

    else:
        scene v15s18c_auam_5a
        with dissolve

        aut "Any luck with your little tasks?"

        scene v15s18c_auam_5
        with dissolve

        u "Haha, yeah. Some things are complete, still have a few left though."

    scene v15s18c_auam_5a
    with dissolve

    aut "Hmm, like what?"

    scene v15s18c_auam_5
    with dissolve

    menu:
        "Never mind":
            $ add_point(KCT.BOYFRIEND)
            
            u "(I can't ask Autumn to make out with me! What am I thinking?)"

            u "Actually, it's okay, haha. Never mind."

            scene v15s18c_auam_5c
            with dissolve

            u "It's a really dumb list."

            scene v15s18c_auam_5b
            with dissolve

            aut "Yeah, well... You did get it from Imre, hehe."

            scene v15s18c_auam_5c
            with dissolve

            u "Very true, ha."

            u "Anyway, I'm gonna go catch everyone else before the party ends."

            scene v15s18c_auam_5b
            with dissolve

            aut "Okay, sounds good. Later. I gotta head home to study anyways."

            scene v15s18c_auam_6
            with dissolve

            pause 0.75

            scene v15s18c_auam_7
            with dissolve

            pause 0.75

            call screen v15s18a_bar

        "Let's make out":
            $ add_point(KCT.TROUBLEMAKER)
            
            scene v15s18c_auam_5
            with dissolve

            u "Well, do you wanna make out?"

            if lauren.relationship.value >= Relationship.GIRLFRIEND.value:
                scene v15s18c_auam_5d # FPP. Same as v15s18c_auam_5a, Autumn angry, mouth open
                with dissolve

                aut "[name]! You're dating my sister, what are you-"

                scene v15s18c_auam_5e # FPP. Same as v15s18c_auam_5d, Autumn angry, mouth closed
                with dissolve

                u "Yeah, I know, I'm sorry... I just-"

                if kct == "loyal":
                    call screen kct_popup
                
                    scene v15s18c_auam_5f # FPP. Same as v15s18c_5e, Autumn slightly sad, mouth open
                    with dissolve

                    aut "*Sighs* Fine."

                    scene v15s18c_auam_5g # FPP. Same as v15s18c_5f, Autumn slightly sad, mouth closed
                    with dissolve

                    u "Wait, what?"

                    scene v15s18c_auam_5f
                    with dissolve

                    aut "I know this is just for some stupid list, haha... So..."

                    aut "It's fine."

                    scene v15s18c_auam_5g
                    with dissolve

                    u "Exactly, yeah. I would never do anything to hurt Lau-"

                    scene v15s18c_auam_5f
                    with dissolve

                    aut "No more talking. Seriously. Zip it."

                    scene v15s18c_auam_5g
                    with dissolve

                    u "Yup. Got it."

                    jump v15s18c_autumn_kiss

                else:
                    scene v15s18c_auam_5d
                    with dissolve

                    call screen kct_popup(required_kct="loyal")
                    aut "You just nothing. You're lucky I won't tell Lauren that you even asked me."

                    scene v15s18c_auam_5e
                    with dissolve

                    u "I'm sorry, Autumn. I thought-"

                    scene v15s18c_auam_5d
                    with dissolve

                    aut "This never happened, [name]. Go away."

                    scene v15s18c_auam_5e
                    with dissolve

                    u "Yeah. Okay..."

                    scene v15s18c_auam_6
                    with dissolve

                    u "(Well, fuck...)"
                
            else:
                if kct == "loyal" and not v11_lauren_caught_aubrey:
                    call screen kct_popup
                    
                    scene v15s18c_auam_5b
                    with dissolve

                    aut "Haha! What?"

                    scene v15s18c_auam_5c
                    with dissolve

                    u "I have to make out with someone, ha."

                    scene v15s18c_auam_5b
                    with dissolve

                    aut "Oh... Sure. That's easy. *Chuckles*"

                    scene v15s18c_auam_5c
                    with dissolve

                    u "Yeah!"

                    u "Wait, really?"

                    jump v15s18c_autumn_kiss

                elif kct == "loyal":
                    scene v15s18c_auam_5a
                    with dissolve

                    aut "Ha, I uh..."

                    aut "There's too much drama I think... Between you and Lauren."

                    aut "It's just hard to-"

                    scene v15s18c_auam_5
                    with dissolve

                    u "I understand. No worries."

                    scene v15s18c_auam_5a
                    with dissolve

                    aut "Okay, thanks."

                    aut "I'm gonna go force Amber out of the bathroom, haha! I have to pee really bad..."

                    scene v15s18c_auam_5
                    with dissolve

                    u "Haha, okay. See you around."

                    scene v15s18c_auam_5a
                    with dissolve

                    aut "Later!"

                    scene v15s18c_auam_6
                    with dissolve

                    u "(Well, that could've gone worse...)"
                
                else:
                    scene v15s18c_auam_5f
                    with dissolve

                    call screen kct_popup(required_kct="loyal")
                    aut "Hmm... I don't-"

                    scene v15s18c_auam_5g
                    with dissolve

                    u "It's cool, no worries."

                    scene v15s18c_auam_5f
                    with dissolve

                    aut "I'm just not feeling it... I'm sorry, [name]."

                    scene v15s18c_auam_5g
                    with dissolve

                    u "Really, it's okay. *Chuckles*"

                    scene v15s18c_auam_5f
                    with dissolve

                    aut "Thanks."

                    scene v15s18c_auam_5a
                    with dissolve

                    aut "I'm gonna go force Amber out of the bathroom, haha! I have to pee really bad..."

                    scene v15s18c_auam_5
                    with dissolve

                    u "Haha, okay. See you around."

                    scene v15s18c_auam_5a
                    with dissolve

                    aut "Later!"

                    scene v15s18c_auam_6
                    with dissolve

                    u "(Well, that could've gone worse...)"
                
                scene v15s18c_auam_7
                with dissolve

                pause 0.75

                call screen v15s18a_bar

label v15s18c_autumn_kiss:
    scene v15s18c_auam_8 # TPP. Show Autumn and MC leaving the bar, both slight smiles, mouths closed
    #with dissolve

    pause 0.75

    scene v15s18c_auam_9 # TPP. Show Autumb pulling MC over to under the stairs, both slight smiles, mouths closed
    with dissolve

    pause 0.75

    scene v15s18c_auam_10 # FPP. MC and Autumn under the stairs, Autumn slight smile, mouth open
    with dissolve

    aut "Let's make this quick. Under the stairs here, while nobody is looking."

    scene v15s18c_auam_10a # FPP. Same as v15s18c_auam_10, Autumn slight smile, mouth closed
    with dissolve

    u "Perfect."

    scene v15s18c_auam_10
    with dissolve

    aut "And no tongue, [name]."

    scene v15s18c_auam_10a
    with dissolve

    u "Haha, okay, no tongues."

    scene v15s18c_auam_11 # TPP. Show MC and Autumn kissing (no tongue)
    with dissolve

    pause 0.75

    scene v15s18c_auam_12 # TPP. MC and Autumn kissing (still no tongue), MC now putting his hand on her waist
    with dissolve

    pause 0.75

    scene v15s18c_auam_13 # TPP. MC and Autumn kissing (no tongue), MC now reaching for her ass
    with dissolve

    pause 0.75

    scene v15s18c_auam_14 # TPP. Show Autumn pulling back and removing MC's hand from her ass, both slight smiles, mouths closed
    with dissolve

    pause 0.75

    scene v15s18c_auam_10
    with dissolve

    aut "There. Good?"

    scene v15s18c_auam_10a
    with dissolve

    u "Mhmm... Yeah, all good."

    scene v15s18c_auam_10
    with dissolve

    aut "Haha."

    scene v15s18c_auam_10a
    with dissolve

    u "Thanks, Autumn."

    scene v15s18c_auam_10
    with dissolve

    aut "Mhmm... Now, go away."

    scene v15s18c_auam_10a
    with dissolve

    $ sceneList.add("v15_autumn")

    $ checklist[5].complete = True
    u "*Laughs* Okay."

    scene v15s18c_auam_15 # TPP. Show MC walking back to where he stands on the screen, sligth smile, mouth closed
    with dissolve

    pause 0.75

    call screen v15s18a_bar

label v15s18c_chris_penelope:
    $ freeroam14.add("chris_penelope")

    scene v15s18c_chpe_1 # FPP. MC watching Chris and Penelope from a slight distance, Chris cornering Penelope, Penelope uncomfortable, mouth closed, Chris slightly sad, mouth open Chris and Penelope looking at each other
    #with dissolve

    ch "Yeah, but... You know what it's like."

    ch "You've been single for how long now?"

    scene v15s18c_chpe_1a # FPP. Same as v15s18c_chpe_1, Penelope mouth open, Chris mouth closed
    with dissolve

    pe "A while, I guess..."

    scene v15s18c_chpe_1
    with dissolve

    ch "So, how do you deal with it?"

    scene v15s18c_chpe_1a
    with dissolve

    pe "With what?"

    scene v15s18c_chpe_1
    with dissolve

    ch "Being single."

    scene v15s18c_chpe_1b # FPP> Same as v15s18c_chpe_1, Chris and Penelope mouths closed
    with dissolve

    u "(Fuck's sake Chris...)"

    scene v15s18c_chpe_1a
    with dissolve

    pe "I don't understand..."

    scene v15s18c_chpe_1c # FPP. Same as v15s18c_chpe_1, Chris slight smile, mouth open, Penelope uncomfortable, mouth closed
    with dissolve

    ch "Haha, sorry. I'm not really thinking straight."

    ch "I'm such a lightweight these days, haha!"

    scene v15s18c_chpe_1d # FPP. Same as v15s18c_chpe_1c, Chris mouth closed, Penelope mouth open
    with dissolve

    pe "Oh, ha... Okay."

    scene v15s18c_chpe_1e # FPP. Same as v15s18c_chpe_1b, Chris slight smile, Penelope uncomfortable, mouths closed
    with dissolve

    menu:
        "Don't interrupt":
            $ add_point(KCT.BRO)
            
            u "(Sorry, Penelope. I don't want anything to do with sad boy Chris, I'm outta here!)"

            call screen v15s18a_upstairsroom

        "Save Penelope":
            $ add_point(KCT.BOYFRIEND)
            
            scene v15s18c_chpe_2 # TPP. Show MC walking up to Chris and Penelope, MC waving at Chris, MC mouth open, slight smile, Penelope slight smile, Chris slight smile, both looking at MC, mouths closed
            with dissolve

            u "Hey, Chris."

            scene v15s18c_chpe_3 # FPP. Show MC standing in front of Chris and Penelope, MC looking only at Chris, Chris mouth open, looking at MC, Chris slight smile
            with dissolve

            ch "Oh, hey [name]."

            scene v15s18c_chpe_3a # FPP. Same as v15s18c_chpe_3, Chris mouth closed, slight smile
            with dissolve

            u "I think Imre was looking for you, it sounded important."

            u "Something about Wolves and fighting, ha."

            scene v15s18c_chpe_3b # FPP. Same as v15s18c_chpe_3, Chris slightly sad, mouth open
            with dissolve

            ch "My whole life revolves around Wolves and fighting... Well, now that Nora's gone..."

            scene v15s18c_chpe_3
            with dissolve

            ch "Anyway, thanks man. See you guys."

            scene v15s18c_chpe_4 # TPP. Show Chris walking away as MC and Penelope stand next to each other, all slight smiles, mouths closed
            with dissolve

            pause 0.75

            scene v15s18c_chpe_5 # FPP. MC looking at Penelope, Penelope smiling, mouth open
            with dissolve

            pe "My hero! Thank you, [name]. *Laughs*"

            scene v15s18c_chpe_6 # TPP. Show Penelope hugging MC
            with dissolve

            u "Haha, you're welcome. I could see the pain in your eyes."

            scene v15s18c_chpe_5
            with dissolve

            pe "I've been stuck in that conversation for twenty minutes now..."

            pe "Chris is a nice guy, but damn! He can be boring as hell sometimes..."

            scene v15s18c_chpe_5a # FPP. Same as v15s18c_chpe_5, Penelope mouth closed, smiling
            with dissolve

            u "Haha, yeah. He's going through some stuff right now."

            scene v15s18c_chpe_5b # FPP. Same as v15s18c_chpe_5, Penelope slightly sad, mouth open
            with dissolve

            pe "*Sighs* True."

            if not v15s18a_showlist_penelope_autumn:
                scene v15s18c_chpe_5
                with dissolve

                pe "So, I heard about this little list you've been working on..."

                scene v15s18c_chpe_5a
                with dissolve

                u "Oh? From whom?"

                scene v15s18c_chpe_5
                with dissolve

                pe "Does it matter? *Chuckles* Let me see."

                scene v15s18c_chpe_7 # TPP. Show MC giving the list to Penelope, both smiling, mouths closed (make it so it could also look like Penelope is giving the list back if possible)
                with dissolve

                pause 0.75

                scene v15s18c_chpe_5c # FPP. Same as v15s18c_chpe_5, Penelope smiling, looking down at the list, mouth open
                with dissolve

                pe "Oooooh, okay..."

                scene v15s18c_chpe_7
                with dissolve

                pause 0.75

                scene v15s18c_chpe_5a
                with dissolve

                u "Yeah, Imre gave it to me."

                scene v15s18c_chpe_5
                with dissolve

                pe "Haha, that makes complete sense."
            
            else:
                scene v15s18c_chpe_5a
                with dissolve

                u "So, about that list I showed you earlier..."

                scene v15s18c_chpe_5
                with dissolve

                pe "Oh, yeah... That thing."

            if lauren.relationship.value >= Relationship.GIRLFRIEND.value:
                scene v15s18c_chpe_5d
                with dissolve

                pe "Um, I don't think we should do anything while we're here."

                scene v15s18c_chpe_5e
                with dissolve

                u "Oh, okay, sure."

                scene v15s18c_chpe_5d
                with dissolve

                pe "Sorry, I just don't feel comfortable."

            elif v14_penelope_date and (kct == "confident" or penelope.relationship.value >= Relationship.LOYAL.value):
                if penelope.relationship.value < Relationship.LOYAL.value:
                    call screen kct_popup
            
                scene v15s18c_chpe_5f # FPP. Same as v15s18c_chpe_5, Penelope flirty expression, mouth open
                with dissolve

                pe "So, what do you need help with?"

                scene v15s18c_chpe_5g # FPP. Same as v15s18c_chpe_5f, Penelope flirty expression, mouth closed
                with dissolve

                u "Follow me."

                scene v15s18c_chpe_8 # TPP. Show MC leading Penelope into the spare room, both sexy expressions, mouths closed
                with dissolve

                pause 0.75

                scene v15s18c_chpe_9 # FPP. MC and Penelope inside the spare room, looking at each other, Penelope sexy expression, mouth closed
                with dissolve

                u "I want to do something for you."

                scene v15s18c_chpe_9a # FPP. Same as v15s18c_chpe_9, Penelope sexy expression, mouth open
                with dissolve

                pe "Hmm, that would be nice."

                pe "Usually, I'm the one who does all the work, haha."

                scene v15s18c_chpe_9
                with dissolve

                u "Get comfortable."

                scene v15s18c_chpe_10 # TPP. Show Penelope taking her dress off, sexy expression and pose, mouth closed
                with dissolve

                pause 0.75

                scene v15s18c_chpe_11 # TPP. Show Penelope getting into bed, MC getting on his knees in front of her, sexy expressions, mouths closed (Penelope naked)
                with dissolve

                pause 0.75

                scene v15s18c_chpe_12 # FPP. MC kneeling in front of Penelope, her lags hanging off the bed, Penelope sexy expression, mouth open
                with dissolve

                pe "Oh, hehe..."

                pe "I see where this is going."

                image v15penor = Movie(play="images/v15/Scene 18c/v15penor.webm", loop=True, image="images/v15/Scene 18c/v15penorStart.webp", start_image="images/v15/Scene 18c/v15penorStart.webp") 
                image v15penorf = Movie(play="images/v15/Scene 18c/v15penorf.webm", loop=True, image="images/v15/Scene 18c/v15penorStart.webp", start_image="images/v15/Scene 18c/v15penorStart.webp") 
                image v15penor2 = Movie(play="images/v15/Scene 18c/v15penor2.webm", loop=True, image="images/v15/Scene 18c/v15penor2Start.webp", start_image="images/v15/Scene 18c/v15penor2Start.webp")
                image v15penor2f = Movie(play="images/v15/Scene 18c/v15penor2f.webm", loop=True, image="images/v15/Scene 18c/v15penor2Start.webp", start_image="images/v15/Scene 18c/v15penor2Start.webp")

                scene v15penor # IGNORE AS ANIMATION
                with dissolve

                pause 0.75

                pe "*Chuckles* Mmm..."

                pe "Oh... [name]..."

                pe "*Whispers* Fuck..."

                scene v15penorf # IGNORE AS ANIMATION
                with dissolve

                pause 0.75

                u "Do you like it when I taste you?"


                pe "*Moans* I love it, [name]... Fuck..."

                pe "You... *Gasps*"

                scene v15penor2 # IGNORE AS ANIMATION
                with dissolve

                pause 0.75

                pe "You really know what you're doing... Ha! Down there..."

                u "*Muffled* Mhmm..."

                pe "Yes, yes! *Moans* Just like that..."

                scene v15penor2f # IGNORE AS ANIMATION
                with dissolve

                pause 0.75

                pe "Oh, I can't believe we're doing this."

                u "(I can't believe how good you taste... Holy shit-)"

                pe "I'm going to cum! [name], I-"

                scene v15s18c_chpe_13 # TPP. MC giving Penelope oral, she holds his head in, she is moaning heavily
                with dissolve

                pe "I'm..."

                scene v15s18c_chpe_14 # TPP. MC giving Penelope oral, Penelope orgasming
                with dissolve

                pe "*Gasps* Mmm, fuck!"

                scene v15s18c_chpe_12
                with dissolve

                pe "Ha..."

                pe "You made me cum. *Panting*"

                scene v15s18c_chpe_12a # FPP. Same as v15s18c_chpe_12, Penelope sexy expression, mouth closed
                with dissolve

                u "I could tell. *Chuckles*"

                scene v15s18c_chpe_15 # TPP. MC climbs up on top of Penelope, both sexy expressions, mouths closed
                with dissolve

                pause 0.75

                scene v15s18c_chpe_16 # TPP. MC on top of Penelope, they're kissing
                with dissolve

                pause 0.75

                scene v15s18c_chpe_17 # TPP. MC getting off the bed, Penelope still laying down, both sexy expressions, mouths closed
                with dissolve

                pause 0.75

                scene v15s18c_chpe_18 # FPP. MC standing in front of Penelope, Penelope laying down, Penelope mouth open, smiling
                with dissolve

                pe "That was incredible..."

                scene v15s18c_chpe_18a # FPP. Same as v15s18c_chpe_18, Penelope smiling, mouth closed
                with dissolve

                u "I'm glad you enjoyed it, haha. Thanks for your help."

                scene v15s18c_chpe_18
                with dissolve

                pe "*Sighs* You're so welcome..."

                pe "I could lay here forever..."

                scene v15s18c_chpe_18a
                with dissolve

                u "People might start to wonder where we are, but same."

                scene v15s18c_chpe_18
                with dissolve

                pe "Haha, okay. You're right."

                scene v15s18c_chpe_19 # TPP. Show MC helping Penelope off the bed
                with dissolve

                pause 0.75

                scene v15s18c_chpe_20 # TPP. Show Penelope getting dressed
                with dissolve

                pause 0.75

                scene v15s18c_chpe_21 # FPP. MC and Penelope in the room, Penelope standing by the door, smiling, mouth open
                with dissolve

                pe "Ready?"

                scene v15s18c_chpe_21a # FPP. Same as v15s18c_chpe_21, Penelope smiling, mouth closed
                with dissolve

                $ sceneList.add("v15_penelope")

                $ checklist[1].complete = True
                u "After you."

                scene v15s18c_chpe_22 # TPP. Show Penelope leaving the room, MC leaving behind her, both smiling, mouths closed
                with dissolve

                pause 0.75

                call screen v15s18a_upstairsroom

            elif penelope.relationship.value < Relationship.LIKES.value:
                scene v15s18c_chpe_5d # FPP. Same as v15s18c_chpe_5, Penelope different pose, slightly uncomfortable, mouth open
                with dissolve

                pe "I think it would be kind of weird if we did anything on this list together."

                pe "Since we're just friends. You know?"

                scene v15s18c_chpe_5e # FPP. Same as v15s18c_chpe_5d, Penelope slightly uncomfortable, mouth closed
                with dissolve

                u "Yeah, I get that."

                scene v15s18c_chpe_5d
                with dissolve

                pe "Sorry, haha."
 
            else:
                if v14_penelope_date:
                    call screen kct_popup(required_kct="confident")
            
                scene v15s18c_chpe_5d
                with dissolve

                pe "Um, I don't think we should do anything while we're here."

                scene v15s18c_chpe_5e
                with dissolve

                u "Oh, okay, sure."

                scene v15s18c_chpe_5d
                with dissolve

                pe "Sorry, I just don't feel comfortable."

            scene v15s18c_chpe_5a
            with dissolve

            u "Trust me, don't worry about it. *Chuckles*"

            scene v15s18c_chpe_5
            with dissolve

            pe "Okay. Thanks."

            scene v15s18c_chpe_5a
            with dissolve

            u "Anyway, time to get back to the party. Ready?"

            scene v15s18c_chpe_5
            with dissolve

            pe "Yes! So ready, haha."

            scene v15s18c_chpe_23 # TPP. Show MC and Penelope going downstairs together, both smiling, mouths closed
            with dissolve

            pause 0.75

            call screen v15s18a_upstairsroom