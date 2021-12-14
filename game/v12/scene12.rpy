# SCENE 12: At the room with chloe or riley
# Locations: Hotel room
# Characters: MC (Outfit: 1), CHLOE (Outfit: 3), RILEY (Outfit: 3)
# Time: Night

label v12_room_chloe_riley:
    if not v11_riley_roomate:
        scene v12crm2 # FPP. MC looking at chloe laying down on her bed, mouth closed
        with dissolve

        u "Hey, hey. Thanks for checking us in."

        play music "music/v12/Track Scene 12_1.mp3" fadein 2

        scene v12crm2a # FPP. same as 2, smiling and mouth opened
        with dissolve

        cl "No worries, I was too excited to finally get in here and lay down. I'm so fucking tired right now, ha."

        scene v12crm2
        with dissolve

        u "You didn't sleep on the ferry?"

        scene v12crm2a
        with dissolve

        cl "Barely, I was so uncomfortable. Not only that, but I spent the first two hours walking around playing a poor girl... Not very fun by the way if you were wondering. *Chuckles*"

        scene v12crm2
        with dissolve

        u "Oh, I thought you'd enjoy being poor. *Chuckles* I was actually the one that suggested it to Mr. Lee."

        scene v12crm2b # FPP. Chloe looking mad, mouth opened
        with dissolve

        cl "YOU WHAT?! No you didn't [name], I swear I'll fight you right now. You better be joking!"

        scene v12crm2
        with dissolve

        u "Goodness, you really didn't like acting poor. *Chuckles*"

        menu:
            "Truth":
                $ add_point(KCT.BOYFRIEND)
                scene v12crm2
                with dissolve

                u "Honestly, I had nothing to do with his choices."

                scene v12crm2c # FPP. Same as 2a, slight smile
                with dissolve

                cl "Mhmm, sure. I'll be keeping my eyes on you."

            "Lie":
                $ add_point(KCT.TROUBLEMAKER)
                scene v12crm2 
                with dissolve

                u "I knew you wouldn't. Mr. Lee said he didn't think it was a good idea but I insisted."

                scene v12crm2d # FPP. Chloe grabs a pillow, looking mad
                with dissolve

                pause 0.75

                scene v12crm3 # TPP. Chloe throws the pillow at MC still looking mad
                with dissolve

                pause 0.6

                scene v12crm2c
                with dissolve

                cl "Jerk. *Chuckles* People have been making fun of me all day after that."

                scene v12crm2
                with dissolve

                u "*Laughs* You didn't find it funny?"

                scene v12crm2c
                with dissolve

                cl "No, I didn't."

                scene v12crm2
                with dissolve

                u "Haha, fine. This year I'll come by the shelter and donate some soup to you. Would you like a coat too, for the winter?"

                scene v12crm2b
                with dissolve

                cl "I'm going to actually kill you."

                scene v12crm2
                with dissolve

                u "Haha! You know I'm just joking right? I had nothing to do with his choices."

                scene v12crm2c
                with dissolve

                cl "Mhmm, sure. I'll be keeping my eyes on you."

        scene v12crm2
        with dissolve

        u "Haha, you do that."

        scene v12crm4 # TPP. MC turns off the lights
        with dissolve

        pause 0.75

        scene v12crm5 # TPP. MC lays on his bed with his hands behind his head
        with dissolve

        pause 0.75

        if chloe.relationship.value < Relationship.FWB.value:
            scene v12crm6 # FPP. MC now laying on his bed, lights off, looking at chloe on her bed, mouth opened
            with dissolve

            cl "Want me to wake you up in the morning?"

            scene v12crm6a # FPP. Same as 6, mouth closed
            with dissolve

            u "That'd be nice."

            scene v12crm6b # FPP. Same as 6, smiling
            with dissolve

            cl "Okay, goodnight jerk."

            scene v12crm6a
            with dissolve

            u "Goodnight you poor, poor girl. *Chuckles*"

            scene v12crm7 # TPP. Image of MC sleeping
            with dissolve

            pause 1

            scene black
            with dissolve
            
            pause 2

        else:
            scene v12crm8 # TPP. Chloe gets up out of her bed, lights off
            with dissolve

            pause 1.25

            scene v12crm9 # TPP. Chloe lays on MCs chest, lights off
            with dissolve

            pause 1.25

            scene v12crm10 # FPP. Chloe now laying on MCs chest, mouth closed, lights off
            with dissolve

            u "Oh, would you look at that. The poor girl must be seeking warmth."

            scene v12crm10a # FPP. Same as 10, mouth opened
            with dissolve

            cl "Oh, hush."

            scene v12crm10 
            with dissolve

            u "*Chuckles*"

            scene v12crm10a
            with dissolve

            cl "Want me to wake you up in the morning?"

            scene v12crm10
            with dissolve

            u "Yeah, that'd be nice."

            scene v12crm10a
            with dissolve

            cl "Okay, night."

            scene v12crm10
            with dissolve

            u "Night babe."

            scene v12crm11 # TPP. Chloe and MC sleeping
            with dissolve

            pause 1.75

            scene black
            with dissolve
            
            pause 2

    else: 

        scene v12crm12 # FPP. Now in the room, riley on her bed, slight smile, mouth opened
        with dissolve

        ri "About time! What were you doing, plotting your next murder?"

        play music "music/v12/Track Scene 12_2.mp3" fadein 2

        scene v12crm12a # FPP. looking at riley, mouth closed
        with dissolve

        u "Haha, no."

        scene v12crm12
        with dissolve

        ri "It bothers me that it was you the whole time. You're really good at deceiving people, and I don't know if that's a good thing or not."

        scene v12crm12a
        with dissolve

        u "Neither do I, but I'm leaning towards good. *Chuckles*"

        scene v12crm12b # FPP. Riley looking surpised, mouth opened
        with dissolve

        ri "Okay, but like... HOW? There were times where I was like \"okay maybe it's him\", but then I felt like I was just being biased."

        scene v12crm12a
        with dissolve

        u "Biased? So you wanted me to be the killer?"

        scene v12crm12b
        with dissolve

        ri "Yeah, of course. You were doing a bunch of suspicious shit but, everyone was being a little sus. Some people were even acting like the killer just to throw people off the trail..."
        ri "Damn imposters. Should've just trusted my gut and kept a better eye on you."

        scene v12crm12a
        with dissolve

        u "Shoulda, woulda, coulda. It's over now. *Chuckles*"

        scene v12crm12b
        with dissolve

        ri "You're a lot slicker than I thought... Maybe I just lowkey realized something about you that I didn't see before."

        scene v12crm12a 
        with dissolve

        u "Like what?"

        scene v12crm12b
        with dissolve

        ri "I don't know, maybe some of the stuff Charli says is right."

        scene v12crm12a 
        with dissolve

        u "Oh no, please. Don't let that shit get into your head."

        scene v12crm12
        with dissolve

        ri "Haha, I knew that'd hit a nerve. Did you get any sleep on the ferry?"

        scene v12crm12a
        with dissolve

        u "Barely."

        scene v12crm12
        with dissolve

        ri "Well, I didn't sleep at all. So now, I've officially been awake for over 24 hours now and I'm beat."

        scene v12crm12a
        with dissolve

        u "Thank fucking god... When you're asleep I don't have to hear you talk. *Chuckles* Over there sounding like a running faucet sometimes."

        scene v12crm12c # FPP. Riley looking annoyed, mouth opened
        with dissolve

        ri "I do not talk a lot...?"

        scene v12crm12a
        with dissolve

        u "..."

        scene v12crm12c
        with dissolve

        ri "I DON'T! [name], seriously!"

        scene v12crm12a
        with dissolve

        u "..."

        scene v12crm12c
        with dissolve

        ri "Okay... Maybe a little but not that much, really. You're overreacting"

        scene v12crm12a
        with dissolve

        u "..."

        scene v12crm12c
        with dissolve

        ri "Okay fine! Maybe I do."

        scene v12crm12a
        with dissolve

        u "*Laughs* I'm just messing with you. Thought I'd try to hit a nerve..."

        scene v12crm12
        with dissolve

        ri "Ha. Funny. Prick."

        scene v12crm4 
        with dissolve

        pause 0.75

        scene v12crm5 
        with dissolve

        pause 0.75

        scene v12crm13 # FPP. MC laying down on his bed, lights off, looking at riley, mouth closed
        with dissolve

        u "Goodnight."

        scene v12crm13a # FPP. Same as 13, mouth opened
        with dissolve

        ri "Yeah whatever, goodnight."

        scene v12crm13 
        with dissolve

        u "*Chuckles*"

        scene v12crm7 
        with dissolve

        pause 1.25

        scene black
        with dissolve
            
        pause 2

    stop music fadeout 3

    jump v12_cafe #scene 13