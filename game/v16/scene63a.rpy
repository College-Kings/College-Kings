# SCENE 63a: Massages
# Locations: Chick's Theatre room 
# Characters: MC (Outfit: x), AUBREY (Outfit: dark red towel), NORA (Outfit: royal blue towel), LINDSEY (Outfit: purple towel)
# Time: Thursday Afternoon


label v16s63a: ### ERROR: 63a) Massages

    # -MC enters the candlelit Chicks theatre room. The coffee table has been moved out to make plenty of room for a massage table. Aubrey is already lying down on it, on her front, towel still around her but lowered so her back is exposed-
    scene v16s63a_1     # TPP MC enters through the door of the candlelit Chick's Theatre room that has been convereted for massages.
    with dissolve

    pause 0.75
    
    scene v16s63a_2     # TPP wide Aubrey(eyes open, smiling ,mouth closed,[OC looking the door where MC entered]) in lays on her stomach on the massage table in position A (https://www.hhhexpos.com/wp-content/uploads/Couples-Massage-640x427.jpg)[arms folded in front of her, head turned to camera side] Her back exposed, boobs squished into the table, side boob visible, and her towel draped over her butt.
    with dissolve

    u "Haha, ready to go already?"

    scene v16s63a_2a # FPP Aubrey (eyes open, smiling,mouth open, looking at MC) in lays on her stomach on the massage table in [POSITION A] Her back exposed, boobs squished into the table, side boob visible, and her towel draped over her butt.
    with dissolve

    au "I love getting massages."

    scene v16s63a_2c # FPP Aubrey(eyes closed, smiling, mouth closed) laying on her stomach on the massage table in POSITION A (Only show Aubrey, her boobs against the table and some of her back in the shot).
    with dissolve

    u "I'd better get my hands oiled up then."

    scene v16s63a_2d # FPP Aubrey(eyes open, glancing back toward MC, smiling, mouth open) laying on her stomach on the massage table in POSITION A (Only show Aubrey, her boobs against the table and some of her back in the shot).
    with dissolve

    au "Haha, yes, please."
    
    scene v16s63a_3     # TPP MC(smiling, mouth closed) pouring oil onto the palm of his opposite hand.
    with dissolve

    pause 0.75

    scene v16s63a_3a # TPP MC(smiling, mouth closed) rubbing his hands together. 
    with dissolve

    pause 0.75

    # -MC picks up a bottle of massage oil. He pours some on his hands, and then starts massaging Aubrey's upper back. Aubrey closes her eyes, a relaxed smile-
    # -if MC bought Calming citrus in Scene 35, or is not helping Chloe and was invited to help
    # MC is not helping chloe if v16s60_chloe_pb_override_mc_gives_massages is true (it means chloe invited him to help and he decided to give massages)
    
    if "citrus_oil0" in v16s35_mc_spa_shopping or v16s60_chloe_pb_override_mc_gives_massages:
        
        scene v16s63a_2b # FPP Aubrey(eyes closed, smiling, mouth open) laying on her stomach on the massage table in POSITION A (Only show Aubrey, her boobs against the table and some of her back in the shot).
        with dissolve
        
        au "Mmm, it smells so nice."

        scene v16s63a_4     # TPP MC(smiling, mouth open) behind and to the side of Aubrey(eyes closed, smiling, mouth closed) laying on her stomach on the massage table in POSITION /SHOT B (https://twohandsmobilemassage.com/wp-content/uploads/2020/02/015Joannie2020.jpg) resting her chin on her folded arms in front of her. [The only change from A to B is head position]
        with dissolve

        u "It's called \"Calming Citrus.\""

        scene v16s63a_4a # TPP MC(smiling, mouth closed) behind and to the side of Aubrey(eyes closed, smiling, mouth open) laying on her stomach on the massage table in POSITION /SHOT b resting her chin on her folded arms in front of her.
        with dissolve

        au "I'm already ten times calmer than when I came in here."

        scene v16s63a_4
        with dissolve

        u "Haha, that's my magic hands at work."

        scene v16s63a_4b # TPP MC(smiling, mouth closed) behind and to the side of Aubrey(eyes open, glancing back toward MC, smiling, mouth open) laying on her stomach on the massage table in POSITION /SHOT b resting her chin on her folded arms in front of her.
        with dissolve

        au "Mmm, it does feel good, [name]."        

    elif "tingle_mint_oil" in v16s35_mc_spa_shopping: # -if MC bought Tingling mint in Scene 35

        scene v16s63a_2b
        with dissolve
        
        au "Ooh, it's so tingly."

        scene v16s63a_4
        with dissolve

        u "Yeah, the label says it's called \"Tingling Mint."

        scene v16s63a_4a
        with dissolve

        au "It does smell minty."
        
        au "Ooh, it's really nice. I like that sensation."

        scene v16s63a_4
        with dissolve

        u "Tingly enough for you?"

        scene v16s63a_2d 
        with dissolve

        au "Haha, you know it."        

    # -Regardless of massage oil type-

    # -MC concentrates on massaging for a moment, moving to her lower back-

    scene v16s63a_5     # TPP MC's hands rubbing Aubrey's lower back close to where the towel covers her ass.
    with dissolve

    u "So, Chloe and Lindsey seem to be getting along tonight."

    scene v16s63a_4a
    with dissolve

    au "Yeah, I think they're just being super aware of their images tonight."

    au "Neither of them wants to come off as a bitch with the election so close."

    scene v16s63a_5a # TPP MC's hands massaging Aubrey's lower back in a different position close to where the towel covers her ass.
    with dissolve

    u "Have you settled on who you're voting for yet?"

    scene v16s63a_2b
    with dissolve

    au "Not really. It could go either way at this point."

    scene v16s63a_5
    with dissolve

    u "(Sounds like she could be easily persuaded... Should I try to swing her vote towards someone?)"    

    # -MC chooses event1, event2 or event3
    # -event1 Praise Chloe
    # -event2 Praise Lindsey
    # -event3 Praise nobody
    menu:

        "Praise Chloe": # -if Praise Chloe
            $ v16s63a_mc_influence_aubreys_vote = 1 # Chloe 

            u "I think Chloe deserves your vote. I've seen how hard she works for the Chicks, even if not everyone else can."

            scene v16s63a_2c
            with dissolve

            u "Plus, she's your friend, that's got to mean something, right?"

            scene v16s63a_2b
            with dissolve

            au "*Sighs* Yeah, I guess you're right. It does make the most sense. I should stick by her side, like I always have."            

        "Praise Lindsey": # -if Praise Lindsey
            $ v16s63a_mc_influence_aubreys_vote = 2 # Lindsey

            scene v16s63a_2c
            #with dissolve

            u "If I were you, Lindsey would have my vote. She's really had a fire inside of her throughout this whole election."

            scene v16s63a_2c
            with dissolve

            u "Plus, I think she's determined to follow through with all her promises."

            scene v16s63a_2b
            with dissolve

            au "*Sighs* Yeah, that's something to think about."
            
            au "Having Lindsey as our new president could be the change we need."            

        "Praise Nobody": # -if Praise nobody

            u "(Aubrey doesn't need my opinion. And besides, I'd rather concentrate on the job at hand...)"

    # -Regardless of convincing her or not-

    # -MC continues massaging, moving to her upper back again-

    scene v16s63a_5
    with dissolve

    au "Oh, wow..."

    scene v16s63a_4a
    with dissolve

    au "This is so relaxing. There should be a spa night every night of the week. *Giggles*"

    scene v16s63a_4
    with dissolve

    u "Haha, every night? I think my hands would fall off."

    scene v16s63a_4b
    with dissolve

    au "Ah, I guess we don't want that..."

    scene v16s63a_5a
    with dissolve

    u "No, I'm kind of attached to them, haha."

    scene v16s63a_2d
    with dissolve

    au "*Laughs* Wow..."

    # -Aubrey moves to sit up on the table-
    scene v16s63a_6     # FPP Aubrey(smiling, mouth open) sitting on the table wrapped in her towel.
    with dissolve

    au "Alright, I should probably head back down now. I don't want to get accused of hogging you for hours."

    scene v16s63a_6a # FPP Aubrey(smiling, mouth closed) sitting on the table wrapped in her towel. 
    with dissolve

    u "That's very considerate."

    scene v16s63a_6
    with dissolve

    au "I know. I'm the best, aren't I?"

    if aubrey.relationship == Relationship.TAMED: # -if AubreyTamed
        
        au "Here's a little something for you before I go."        

        # -Aubrey pulls MC closer. They kiss passionately. Aubrey's towel falls lower, exposing her boobs while they're kissing. She stops kissing to pull it back up-
        scene v16s63a_7a # TPP Aubrey and MC kissing (eyes closed) with tongue but enough room between Aubrey and MC to see Aubrey's chest.
        with dissolve

        pause 0.750

        scene v16s63a_7b # TPP Aubrey and MC kissing (eyes closed) with tongue but enough room between Aubrey and MC to see Aubrey's chest. Aubrey's towel falls to her lap, showing her boobs.
        with dissolve

        pause 0.75

        scene v16s63a_8     # FPP Aubrey(smiling sexy, mouth open) looking at MC-- Camera shows Aubrey and her boobs (uncovered). 
        with dissolve
        
        au "Oops, my towel fell."

        scene v16s63a_8a # FPP Aubrey(smiling sexy, mouth closed) looking at MC-- Camera shows Aubrey and her boobs (uncovered). 
        with dissolve

        u "You can leave it down. I'm not done with you yet."

        scene v16s63a_8
        with dissolve

        au "Haha, I told you after our dinner. I will be well worth the wait."

        scene v16s63a_8c # FPP Aubrey(smiling sexy, mouth closed) looking at MC-- Camera shows Aubrey and her boobs (covered with towel).
        with dissolve

        u "You always are."

        scene v16s63a_8b # FPP Aubrey(smiling sexy, mouth open) looking at MC-- Camera shows Aubrey and her boobs (covered with towel). 
        with dissolve

        au "Hehe, see you soon."

        scene v16s63a_7a
        with dissolve

        pause 0.75

        # -Another passionate kiss-

    # -Regardless of AubreyTamed-

    # -Aubrey leaves the room. MC watches her go. Both smiling-
    scene v16s63a_9     # TPP Aubrey(smiling, mouth closed) walking towards the door, giving a slight way to MC (smiling, mouth open) who is slightly behind her near the massage table. 
    with dissolve
    
    u "Have fun out there!"

    scene v16s63a_10    # TPP MC(smiling, mouth clsoed) thinking to himself.
    with dissolve

    u "(I'm really getting the hang of this masseuse thing! Who's next?)"
    
    # -In walks Nora-

    scene v16s63a_11     # FPP Nora(smiling, mouth open) enters through the door of the candlelit Chick's Theatre room that has been convereted for massages in her towel.
    with dissolve

    no "Hey."

    scene v16s63a_11a # FPP Nora(smiling, mouth closed) enters through the door of the candlelit Chick's Theatre room that has been convereted for massages in her towel.
    with dissolve

    u "Good evening, Miss. Please make yourself comfortable on my massage table."

    scene v16s63a_11
    with dissolve

    no "Haha... Why, thank you."

    # -Nora lies down, same position as Aubrey with lowered towel. MC starts massaging her upper back. She closes her eyes, relaxed smile-

    scene v16s63a_12     # TPP wide Nora(eyes open, glancing back toward MC[OC behind her] smiling ,mouth open), lays on her stomach on the massage table in position A [arms folded in front of her, head turned to camera side] Her back exposed, boobs squished into the table, side boob visible, and her towel draped over her butt.
    with dissolve

    no "You'll never guess what's going on in the living room."

    scene v16s63a_12a # TPP wide Nora(eyes open, glancing back toward MC[OC behind her] smiling ,mouth closed, lays on her stomach on the massage table in position A [arms folded in front of her, head turned to camera side] Her back exposed, boobs squished into the table, side boob visible, and her towel draped over her butt.
    with dissolve

    u "Oh, no. What are they up to now?"

    scene v16s63a_12
    with dissolve

    no "We've been making out."

    scene v16s63a_12a
    with dissolve

    u "You're what?"

    scene v16s63a_12
    with dissolve

    no "Haha, yeah."

    no "I sort of just made out with Chloe."

    scene v16s63a_12a
    with dissolve

    u "Are you serious...?"

    scene v16s63a_12
    with dissolve

    no "Yes, I'm serious!"

    scene v16s63a_12a
    with dissolve

    u "Uhh..."
    
    u "I'll be right back."

    scene v16s63a_12b # FPP Nora(eyes closed, smiling, mouth open) laying on her stomach on the massage table in POSITION A (Only show Nora, her boobs against the table and some of her back in the shot).
    with dissolve

    no "*Laughs* No, you're staying right here! Keep massaging me!"

    scene v16s63a_12c # FPP Nora(eyes closed, smiling, mouth closed) laying on her stomach on the massage table in POSITION A (Only show Nora, her boobs against the table and some of her back in the shot).
    with dissolve

    u "*Sighs* Fine... I guess I have a job to do."

    scene v16s63a_12b
    with dissolve

    no "A very important one..."

    if nora.relationship == Relationship.FRIEND: # -if NoraFriend

        scene v16s63a_13     # TPP MC(smiling, mouth open) behind and to the side of Nora(eyes closed, smiling, mouth closed) laying on her stomach on the massage table in POSITION /SHOT b resting her chin on her folded arms in front of her. [The only change from A to B is head position]
        with dissolve

        u "You've really been unwinding these last few days, huh?"

        scene v16s63a_13a # TPP MC(smiling, mouth closed) behind and to the side of Nora(eyes closed, smiling, mouth open) laying on her stomach on the massage table in POSITION /SHOT b resting her chin on her folded arms in front of her.
        with dissolve

        no "Starting with yoga, yes. *Chuckles* I love it now."

        scene v16s63a_14     # TPP MC's hands massaging Nora's lower back close to where the towel covers her ass.
        with dissolve

        no "I should do more relaxing things for myself like spa treatments and massages."

        scene v16s63a_14a # TPP MC's hands massaging Nora's lower back in a different position close to where the towel covers her ass.
        with dissolve

        no "I feel like a whole different person these days. It feels good."
        
        # -MC chooses event1 or event2
        # -event1 You seem different
        # -event2 Ask about Chris
        menu: 
            "You seem different": # -if You seem different

                scene v16s63a_13
                with dissolve

                u "You seem different, too. I mean, in a good way. Like, you're more relaxed or... Self-focused, I guess? *Laughs*"

                scene v16s63a_13a
                with dissolve

                no "Ha... I can see that. It's nice to hear, to be honest."                

                no "I was blinded by Chris for so long, I forgot how to have fun and live my own life."

                scene v16s63a_13b # TPP MC(smiling, mouth closed) behind and to the side of Nora(eyes open, glancing back toward MC, smiling, mouth open) laying on her stomach on the massage table in POSITION /SHOT b resting her chin on her folded arms in front of her.
                with dissolve

                no "But I'm back on track now. The new and improved Nora, haha."

                scene v16s63a_13
                with dissolve

                u "And you're not as stressed. The old Nora was stressed out all the time."

                scene v16s63a_13b
                with dissolve

                no "Yeah, you're not wrong."

                no "I guess sometimes a break-up can be a relief of stress."
                
                no "Massages being a very close second. *Laughs*"

                scene v16s63a_14a ### check mouth speaking 14a
                with dissolve

                u "Hmm, I guess I need to work harder if I'm trying to beat the feeling of freedom."                

            "Ask about Chris": # -if Ask about Chris
                scene v16s63a_13
                with dissolve
                
                u "Speaking of... Have you seen Chris at all since you've been back?"

                scene v16s63a_13a
                with dissolve

                no "Oh, you know what? I shouldn't have even brought him up. Sorry, ha."                

                no "I don't want to talk about him. I don't even want to hear myself say his name again."

                scene v16s63a_13
                with dissolve

                u "Oh, yeah, sorry."

                scene v16s63a_13b
                with dissolve

                no "It's fine. I haven't seen him."

                scene v16s63a_14 ### check mouth speaking 14
                with dissolve

                u "Gotcha."

                scene v16s63a_13a
                with dissolve

                no "Now, back to relaxing."

    elif nora.relationship == Relationship.FWB: # -if NoraRS

            scene v16s63a_13a
            with dissolve

            no "It feels amazing, by the way."

            scene v16s63a_13
            with dissolve

            u "Thanks."

            scene v16s63a_14
            with dissolve

            no "You have such big, warm hands..."

            scene v16s63a_13
            with dissolve

            u "Haha, thank you."

            scene v16s63a_13c # TPP MC(smiling, mouth closed) behind and to the side of Nora(eyes open- sexy, glancing back toward MC, smiling, mouth open) laying on her stomach on the massage table in POSITION /SHOT b resting her chin on her folded arms in front of her.
            with dissolve

            no "Mmm, I can't even begin to imagine the things you could do to me with those."

            scene v16s63a_14a
            with dissolve

            u "(She's definitely trying to spice up the conversation...)"

            # -MC chooses event1 or event2
            # -event1 Keep it friendly
            # -event2 Spice things up
            menu: 
                
                "Keep it friendly": # -if Keep it friendly

                    scene v16s63a_13
                    with dissolve

                    u "Yeah, ha... Hands are useful."
                    
                    u "They're one of the defining traits of primates. Makes us stand out from other species, you know?"

                    scene v16s63a_13b
                    with dissolve

                    no "...What are you saying?"

                    scene v16s63a_14a
                    with dissolve

                    u "Nothing, uh- Anyway, how are you liking this massage oil?"

                    scene v16s63a_13a
                    with dissolve

                    no "Um... Yeah, it's great."

                    scene v16s63a_14
                    with dissolve

                    u "Good, glad you like it."

                    scene v16s63a_13a
                    with dissolve

                    no "Smells good, so..."

                    scene v16s63a_13
                    with dissolve

                    u "Am I missing anything important out there?"

                    scene v16s63a_12b
                    with dissolve

                    no "Oh, nothing really. Just lots of kissing..."
                    
                    no "That seems to be the main event tonight."

                    scene v16s63a_12c
                    with dissolve

                    u "*Sighs* So unfair..."

                    scene v16s63a_13b
                    with dissolve

                    no "Aww, poor boy has to sit here and rub his hands all over my half-naked body..."

                    scene v16s63a_13
                    with dissolve

                    u "*Laughs* Okay, okay... You're right, I can't complain."

                    scene v16s63a_12b
                    with dissolve

                    no "Neither can I. You're doing a fantastic job for being a rookie."

                    scene v16s63a_12c
                    with dissolve

                    u "Hey, thanks. It's clearly a hidden talent of mine."                    

                "Spice things up": # -if Spice things up

                    scene v16s63a_14
                    with dissolve
                    
                    u "Yeah, these hands can work wonders."

                    scene v16s63a_12b
                    with dissolve

                    no "Hmm... Tell me, what can they do?"

                    scene v16s63a_14a
                    with dissolve

                    u "They can feel every inch of your beautiful skin."

                    scene v16s63a_13c
                    with dissolve

                    no "Yeah? Like what? What do they like to feel?"

                    scene v16s63a_14
                    with dissolve

                    u "(Shit, okay... I think she wants more than just a conversation here...)"
                    
                    # -MC chooses event1 or event2
                    # -event1 Let me show you
                    # -event2 Cool things down
                    menu:

                        "Let me show you": # -if Let me show you

                            $ sceneList.add("v16_nora") 
                            
                            image v16norfg = Movie(play="images/v16/scene63a/v16norfg.webm", loop=True, image="images/v16/scene63a/v16norfgStart.webp", start_image="images/v16/scene63a/v16norfgStart.webp")
                            image v16norfgf = Movie(play="images/v16/scene63a/v16norfgf.webm", loop=True, image="images/v16/scene63a/v16norfgStart.webp", start_image="images/v16/scene63a/v16norfgStart.webp")

                            scene v16s63a_13d # TPP MC(smiling, mouth open) behind and to the side of Nora(eyes open- sexy, glancing back toward MC, smiling, mouth closed) laying on her stomach on the massage table in POSITION /SHOT b resting her chin on her folded arms in front of her.
                            with dissolve

                            u "How about you let me show you instead?"

                            scene v16s63a_13c
                            with dissolve

                            no "Hehe... I love that idea. Less talking, more fingering."

                            scene v16s63a_15     # TPP Nora(smiling, sexy, mouth closed, looking at MC) turned over on her back, naked, legs spread apart, pussy showing (her towel is under her) directing MC's (smiling mouth closed) hand towards her pussy.
                            with dissolve

                            u "Yes, ma'am..."

                            # -Nora turns over onto her back. The towel falls to the floor. She's totally naked. She takes MC's hands and moves it to finger her, then she takes her hand away, leaving him to continue-

                            # -ANIMATION: MC fingering Nora-
                    
                            scene v16norfg #  ignore as animation
                            with dissolve

                            no "Mmm, yes..."                            

                            u "You like that?"
                            
                            no "I fucking love it..."                            

                            no "You're- *Gasps* Hitting my fucking g-spot..."

                            scene v16norfgf # ignore as animation
                            with dissolve

                            u "Right there?"                            

                            no "*Gasps* Fuck! Ye-yeah... There..."

                            no "*Moans* [name], I-"

                            no "I'm gonna cum... You..."

                            # -END OF ANIMATION-
                            
                            scene v16s63a_15a # TPP [Last frame of animation v16norfgf] Nora(eyes closed, orgasming, biting lip) clenching MC's arm that is fingering her to stay deep inside her (MC face not likely in frame, but if so smiling, mouth closed)
                            with dissolve

                            no "*Moans*"

                            scene v16s63a_15b # TPP Close up of v16s63a_15a, but Nora (eyes closed tighter, orgasming, mouth open [saying "Fuck"]) still clenching MC's arm that is fingering her (MC should not be in this shot-- All Nora showing the emotion of cumming hard).
                            with vpunch

                            no "Fuuuck..."

                            scene v16s63a_15c # TPP Close up of v16s63a_15a, but Nora (eyes open, super relaxed, pleasant smile, satisfied, mouth closed) looking at MC her legs still apart, pussy showing (wet optional). MC(smiling, mouth open) on hand on Nora's thigh the other on her stomach.
                            with dissolve

                            u "Trembling legs... Mission accomplished."

                            scene v16s63a_15d # TPP Close up of v16s63a_15a, but Nora (eyes open, super relaxed, pleasant smile, satisfied, mouth open) looking at MC her legs still apart, pussy showing (wet optional). MC(smiling, mouth closed) on hand on Nora's thigh the other on her stomach.
                            with dissolve

                            no "*Panting* Very, very accomplished."

                            scene v16s63a_15c
                            with dissolve

                            u "Haha, good."

                            scene v16s63a_15d
                            with dissolve

                            no "That's a damn good technique you have there."

                            scene v16s63a_15c
                            with dissolve

                            u "Pleased to be of service... Feel free to tip me on your way out."

                            scene v16s63a_15d
                            with dissolve

                            no "*Laughs* Sorry, no cash on me."

                            scene v16s63a_15c
                            with dissolve

                            u "That's what they all say..."
                                                        
                        "Cool things down": # -if Cool things down
                            
                            u "I could show you, but I think we should cool off... Don't want things to get too far and then have someone walk in on us. *Chuckles*"

                            scene v16s63a_13b
                            with dissolve

                            no "Oh, my God. You're right! That would be mortifying..."                            

                            if chloe.relationship == Relationship.GIRLFRIEND: # -if ChloeGF

                                no "Especially if it was your little girlfriend that walked in... *Giggles*"

                                scene v16s63a_13
                                with dissolve

                                u "...Yeah. That'd be something..."

                                scene v16s63a_14a
                                with dissolve

                                u "(Is she just casually bringing that up?)"

                                scene v16s63a_13a
                                with dissolve

                                no "We should probably discuss that soon, by the way."

                                scene v16s63a_13
                                with dissolve

                                u "Uh, yeah?"

                                scene v16s63a_13c
                                with dissolve

                                no "Ha, not too soon, don't worry."                                

                            # -regardless of chloegf-                            
                            
                            scene v16s63a_12b
                            with dissolve
                            
                            no "Being around you is just- I'm always so fucking horny when I'm with you. *Giggles*"

                            scene v16s63a_13
                            with dissolve

                            u "Oh... Haha, yeah?"

                            scene v16s63a_13c
                            with dissolve

                            no "Yes. Hell yes. But anyway... Enough chatting!"                            

    # -Regardless of all that-
    
    scene v16s63a_12
    with dissolve

    no "Just a little more on my lower back, and then I think I'll head back down."

    scene v16s63a_14a
    with dissolve

    u "Oh, sure thing."

    scene v16s63a_14
    with dissolve

    pause 0.75

    # -MC works on her lower back for a moment-

    # -Then he's finished. Nora stands up-

    scene v16s63a_16     # TPP Nora(smiling, mouth open) sitting on the table, wrapped in her towel looking at MC (smiling, mouth closed) looking at Nora.
    with dissolve

    no "*Moans* Thanks, [name]. That was a massage to remember."

    scene v16s63a_16a # TPP Nora(smiling, mouth closed) standing, wrapped in her towel, facing the door, looking at MC (smiling, mouth open) looking at Nora.
    with dissolve

    u "Haha, you're welcome. Remember to leave a five-star review online."

    scene v16s63a_16b # TPP Nora(smiling, mouth open) standing, wrapped in her towel, facing the door, looking at MC (smiling, mouth closed) looking at Nora.
    with dissolve

    no "Oof, I think I'm too busy... Sorry..."
    
    # -she smiles-

    if "v16_nora" in sceneList: # -if MC just fingered Nora

        # -They have a quick kiss-
        scene v16s63a_16c # TPP Nora and MC kissing (eyes closed).
        with dissolve
        
        pause 0.75
        
    # -Regardless of if MC just fingered Nora-

    scene v16s63a_16a
    with dissolve
    
    u "So who's next?"

    scene v16s63a_16b
    with dissolve

    no "I think you've got Lindsey coming in next."

    scene v16s63a_16a
    with dissolve

    u "Sounds good. Send her in!"

    # -Nora leaves the room. MC watches her go. Both smiling-

    scene v16s63a_10
    with dissolve

    u "(Two naked girls down. One more to go. I can think of worse ways to spend an evening, haha.)"

    # -In walks Lindsey-
    
    scene v16s63a_18     # FPP Lindsey(smiling, mouth open) enters through the door of the candlelit Chick's Theatre room that has been convereted for massages in her towel.
    with dissolve

    li "I'm sure you're ready for me now that you've warmed up on those two."

    scene v16s63a_18a # FPP Lindsey(smiling, mouth closed) enters through the door of the candlelit Chick's Theatre room that has been convereted for massages in her towel.
    with dissolve

    u "Haha, oh yeah. Best for last, just for you."

    # -Lindsey lies down, same position as the others with lowered towel. MC starts massaging her upper back. She closes her eyes, relaxed smile-

    pause 0.75

    scene v16s63a_20     # TPP MC's hands massaging Lindsey's lower back close to where the towel covers her ass.
    with dissolve

    pause 0.75
        
    scene v16s63a_19     # TPP wide Lindsey(eyes open, glancing back toward MC[OC behind her] smiling ,mouth open), lays on her stomach on the massage table in position A [arms folded in front of her, head turned to camera side] Her back exposed, boobs squished into the table, side boob visible, and her towel draped over her butt.
    with dissolve
    
    li "Ooh... I haven't been touched this much in so long, haha. Sorry if I'm ticklish."

    scene v16s63a_19a # TPP wide Lindsey(eyes open, glancing back toward MC[OC behind her] smiling ,mouth closed), lays on her stomach on the massage table in position A [arms folded in front of her, head turned to camera side] Her back exposed, boobs squished into the table, side boob visible, and her towel draped over her butt.
    with dissolve

    u "Ha, that long, huh?"

    scene v16s63a_19b # FPP Lindsey(eyes closed, smiling, mouth open) laying on her stomach on the massage table in POSITION A (Only show Lindsey, her boobs against the table and some of her back in the shot).
    with dissolve

    li "This campaign has taken up so much of my time and energy, I barely have enough time to blink."

    scene v16s63a_19c # FPP Lindsey(eyes closed, smiling, mouth closed) laying on her stomach on the massage table in POSITION A (Only show Lindsey, her boobs against the table and some of her back in the shot).
    with dissolve

    u "Damn. I'm glad you're here then, you need this."

    scene v16s63a_20a # TPP MC's hands massaging Lindsey's lower back in a different position close to where the towel covers her ass.
    with dissolve

    li "Ha, you have no idea."

    scene v16s63a_20
    with dissolve

    li "I haven't even- Never mind, haha."

    scene v16s63a_21     # TPP MC(smiling, mouth open) behind and to the side of Lindsey(eyes closed, smiling, mouth closed) laying on her stomach on the massage table in POSITION /SHOT b resting her chin on her folded arms in front of her. [The only change from A to B is head position]
    with dissolve

    u "Haven't even what?"

    scene v16s63a_21a # TPP MC(smiling, mouth closed) behind and to the side of Lindsey(eyes closed, smiling, mouth open) laying on her stomach on the massage table in POSITION /SHOT b resting her chin on her folded arms in front of her.
    with dissolve

    li "I haven't even touched myself for at least a week now. I'm just now realizing that I've been so busy..."

    scene v16s63a_20 ### check mouth speaking 20
    with dissolve

    u "Haha, you miss masturbating?"

    li "Well, not exactly that, but-"

    scene v16s63a_21b # TPP MC(smiling, mouth closed) behind and to the side of Lindsey(eyes open, glancing back toward MC, smiling, mouth open) laying on her stomach on the massage table in POSITION /SHOT b resting her chin on her folded arms in front of her.
    with dissolve

    li "Yeah, pretty much that. I just miss sex... *Sighs*"

    scene v16s63a_19c
    with dissolve

    u "Well..."

    scene v16s63a_21a
    with dissolve

    li "I'm so sorry! I'm just thinking out loud today..."

    scene v16s63a_20a ### check mouth speaking 20a
    with dissolve

    u "(Sounds like she could use some pleasure... Do I want to provide any?)"

    # -MC chooses event1 or event2
    # -event1 Keep it friendly
    # -event2 Turn up the heat
    menu:

        "Keep it friendly": # -if Keep it friendly
            u "You should try to make some time for yourself soon. It's important."

            scene v16s63a_19b
            with dissolve

            li "Yeah, I know. You're right..."            

            li "I think all the kissing out there has gotten a little flustered, haha."

            scene v16s63a_19c
            with dissolve

            u "*Laughs* Nora told me about that. Are you guys having fun?"

            scene v16s63a_19b
            with dissolve

            li "It's just some innocent experimentation."

            scene v16s63a_19c
            with dissolve

            u "Ah... Well, I just hope somebody's filming it. You know, for posterity."

            scene v16s63a_20
            with dissolve

            li "Haha, sorry but, we're all too busy making out, I think."

            scene v16s63a_21
            with dissolve

            u "It's times like this when I wish I could be in two places at once."

            scene v16s63a_21b
            with dissolve

            li "*Laughs* Focus on my needs, [name]! Not the kissing..."            

        "Turn up the heat": # -if Turn up the heat

            scene v16s63a_21
            with dissolve

            u "You know, you just need to say the word. There'd be a line of guys waiting to please you."

            scene v16s63a_21a
            with dissolve

            li "Oh, really?"

            scene v16s63a_21c # TPP MC(smiling, mouth closed) behind and to the side of Lindsey(eyes open- sexy, glancing back toward MC, smiling, mouth open) laying on her stomach on the massage table in POSITION /SHOT b resting her chin on her folded arms in front of her.
            with dissolve

            li "Maybe I have someone in mind already..."

            # -lindsey biting her lip-

            scene v16s63a_21d # TPP MC(smiling, mouth open) behind and to the side of Lindsey(eyes open- sexy, glancing back toward MC, smiling, biting lip) laying on her stomach on the massage table in POSITION /SHOT b resting her chin on her folded arms in front of her.
            with dissolve

            u "He'd be happy to help, I think."

            scene v16s63a_21c
            with dissolve

            li "Mmm, but I don't just want pleasure... I'd like to feel him in my mouth, too."
            
            # -Lindsey opens her eyes-

            if len(mc.girlfriends) > 0: # -if MC also has a GF

                scene v16s63a_21f # TPP MC(smiling, mouth closed) behind and to the side of Lindsey(eyes open, glancing back toward MC, neutral, mouth open) laying on her stomach on the massage table in POSITION /SHOT b resting her chin on her folded arms in front of her.
                with dissolve

                li "Oh, wait. Fuck. What am I saying? What are you saying?"

                scene v16s63a_20
                with dissolve

                u "I- We-"

                scene v16s63a_21f
                with dissolve

                li "Wait, stop... Don't even reply to that. You have a girlfriend and I'm just drunk and horny."

                scene v16s63a_21g # TPP MC(smiling, mouth open) behind and to the side of Lindsey(eyes open, glancing back toward MC, neutral, mouth closed) laying on her stomach on the massage table in POSITION /SHOT b resting her chin on her folded arms in front of her.
                with dissolve

                u "You don't seem drunk."

                scene v16s63a_21f
                with dissolve

                li "Okay, but very horny and not thinking straight. And you followed along!"

                scene v16s63a_21g
                with dissolve

                u "Yeah, uh... *Awkward laugh* Sorry, I was just playing along."

                scene v16s63a_21a
                with dissolve

                li "*Sighs* Anyway."

            elif len(mc.girlfriends) == 0 and lindsey.relationship == Relationship.FWB: # -if no GF and LindseyRS
                scene v16s63a_20
                with dissolve

                u "Yeah?"

                scene v16s63a_20a
                with dissolve

                li "Yeah."
                
                u "(Hmm, what's my move here?)"
                
                # -MC chooses event1 or event2
                # -event1 Satisfy her craving
                # -event2 Cool off
                menu:

                    "Satisfy her craving": # -if Satisfy her craving

                        # -MC starts pulling down Lindsey's towel-
                        scene v16s63a_20b # TPP MC's hands massaging Lindsey's lower ass cheeks and her towel is no longer covering her ass 
                        with dissolve

                        pause 0.75

                        # -Transition to Scene 63c-
                        jump v16s63c

                    "Cool off": # -if Cool off

                        scene v16s63a_21d
                        with dissolve
                        
                        u "Wait, I'm not sure if we should..."

                        scene v16s63a_21b
                        with dissolve

                        li "Why not?"

                        scene v16s63a_21
                        with dissolve

                        u "It just doesn't feel right, with everyone in the other room, I guess."

                        scene v16s63a_21h # TPP MC(smiling, mouth closed) behind and to the side of Lindsey(eyes closed, disappointed, mouth open) laying on her stomach on the massage table in POSITION /SHOT b resting her chin on her folded arms in front of her.
                        with dissolve

                        li "Oh, okay. I guess I'll have to take care of myself later tonight, then."

                        # -lindsey is disappointed-

            # -Regardless-

    # -if MC chose Keep conversation friendly, or chose Turn up the heat but has a GF, or chose Cool off
    if v16s63a_mc_choose_keep_convo_friendly or (not v16s63a_mc_choose_keep_convo_friendly and len(mc.girlfriends) > 0) or v16s63a_mc_choose_cool_convo:

        scene v16s63a_21h
        with dissolve

        li "We should probably head back down now... I think Chloe has something else planned."

        scene v16s63a_21
        with dissolve

        u "Oh, okay. Guess I'm done here?"

        scene v16s63a_22     # TPP Lindsey(smiling, mouth open) sitting on the table, wrapped in her towel looking at MC (smiling, mouth closed) looking at Lindsey.
        with dissolve

        li "Yup, you're free!"

        scene v16s63a_23    # FPP Lindsey(smiling, mouth closed) standing, wrapped in her towel looking at MC (smiling, mouth open) looking at Lindsey.
        with dissolve

        u "While we're on the subject, you two seem to be getting along tonight."

        scene v16s63a_23a # FPP Lindsey(smiling, mouth open) standing, wrapped in her towel looking at MC (smiling, mouth closed) looking at Lindsey.
        with dissolve

        li "Who? Chloe? Oh- *Chuckles*"

        li "Well, yeah... In politics, you have to play a lot of faces. That's what I'm discovering anyway."

        scene v16s63a_23
        with dissolve

        u "Yeah, I guess it takes a special person to be able keep up the act all day."

        scene v16s63a_23a
        with dissolve

        li "It can be quite tiring, but necessary."

        li "And this massage thing is, personally, a great idea, so I reluctantly give her credit where it's due."
        
    if v14_help_chloe and not v16s12_chloe_planboard_decide_newspaper_cover: # -if mc helped chloe with planning board and chose the spa night

        scene v16s63a_10
        with dissolve

        u "(Credit taken, thank you very much)."
        
    # -end if

    scene v16s63a_23
    with dissolve

    u "That's very mature of you."

    scene v16s63a_23a
    with dissolve

    li "I just wish I'd thought of it first..."

    scene v16s63a_23
    with dissolve

    u "Can't win them all, Linds."

    scene v16s63a_23a
    with dissolve

    li "Sadly... Come on, let's go."

    # -MC and Lindsey exit the room-

    scene v16s63a_24     # TPP Lindsey(smiling, mouth closed) exiting through the the door, with MC (smiling, mouth open) following behind her.
    with dissolve

    pause 0.75

    # -Transition to Scene 64-
    jump v16s64