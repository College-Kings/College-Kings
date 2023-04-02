# SCENE 20: Urban Exploring at the Baguette Factory
# Locations: Baguette Factory
# Characters: AUBREY (Outfit: x), NORA (Outfit: x), IMRE (Outfit: x), MC (Outfit: x)
# Time: Saturday
# Phone Images: 

label v12_urban_exploring:
    scene v12uex1 # TPP Show Imre, Aubrey, Nora, and MC walking and along sidewalk in Paris
    with fade

    pause 0.75

    play music "music/v12/Track Scene 20.mp3" fadein 2

    scene v12uex2 # FPP Show outside of abandoned commercial bakery
    with dissolve

    au "What... is this?"

    no "Uhh, it's the factory...? I think..."

    scene v12uex3 # FPP Show Aubrey, outside factory, neutral expression and mouth open
    with dissolve

    au "Not what I was expecting."

    scene v12uex4 # FPP Show Nora, outside factory, smiling with mouth open
    with dissolve

    no "Me either. *Chuckles* I thought it was a working factory."

    scene v12uex2
    with dissolve

    imre "Working for the rats. *Chuckles*"

    scene v12uex4
    with dissolve

    no "This kinda reminds me of my old school yard where we had recess."

    scene v12uex5 # FPP Show Imre, outside factory, smiling with mouth open
    with dissolve

    imre "Oh man... I was the coolest kid at recess."

    scene v12uex3a # FPP Same angle as v12uex3, Aubrey smiling with mouth open
    with dissolve

    au "You were probably the kid during freeze tag that got frozen right away and no one wanted to untag. *Laughs"

    scene v12uex5
    with dissolve

    imre "And you were probably the kid during hide and seek that no one ever cared to find."

    scene v12uex3a
    with dissolve

    au "*Laughs* Nice comeback, Imre. You're improving a lot. I'm proud."

    scene v12uex4
    with dissolve

    no "Aubrey, weren't you a cheerleader?"

    scene v12uex3a
    with dissolve

    au "Yeah, I was."

    scene v12uex4
    with dissolve

    no "I did gymnastics as a kid, do you remember any of your tumbling?"

    scene v12uex3a
    with dissolve

    au "I'm probably not as good as I used to be, but yeah. I'm sure I could pull off a few tricks."

    scene v12uex6 # FPP Show Aubrey and Nora standing next to each other, looking at each other, smiling with mouths closed
    with dissolve

    u "Am I sensing a contest?"

    scene v12uex4
    with dissolve

    no "*Chuckles* What do you say Aubrey?"

    scene v12uex3a
    with dissolve

    au "I never say no to a challenge, babe."

    scene v12uex5
    with dissolve

    imre "Umm, hello? Still here, and I bet I can do stunts way better than you girls."

    scene v12uex4
    with dissolve

    no "Ha! Really?"

    scene v12uex5
    with dissolve

    imre "Hell yeah, I used to do stunts with my mom all the time."

    scene v12uex4
    with dissolve

    no "Okay then, show us something."

    scene v12uex5
    with dissolve

    imre "Bet."

    scene v12uex7 # FPP Show Imre climbing up onto one of the concrete blocks
    with dissolve

    pause 0.5

    scene v12uex7a # FPP Same angle as v12uex7, Imre doing a backflip off of the concrete block
    with dissolve

    pause 0.5

    scene v12uex3a
    with dissolve

    au "Oh shit Imre! You weren't lying, haha..."

    scene v12uex5
    with dissolve

    imre "Why would I lie? Besides, that was just a little warm up!"

    scene v12uex4
    with dissolve

    no "Oh, you got more?"

    scene v12uex5a # FPP Same angle as v12uex5, Imre laughing and looking arrogant
    with dissolve

    imre "*Laughs*"

    scene v12uex8 # FPP Show Imre running to a wall and placing his foot against it, like he's about to run up it
    with dissolve

    pause 0.5

    scene v12uex8a # FPP Same angle as v12uex8, Imre kicking off of the wall and doing and back flip
    with dissolve

    pause 0.5

    scene v12uex3a
    with dissolve

    au "Impressive... But are flips the only thing you can do? *Chuckles*"

    scene v12uex5
    with dissolve

    imre "Yeah, pretty much. *Chuckles*"

    scene v12uex4
    with dissolve

    no "Haha... [name], can you do anything?"

    scene v12uex4a # FPP Same angle as v12uex4, Nora smiling with mouth closed
    with dissolve

    menu:
        "Of course":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            u "*Chuckles* Of course I can."

            scene v12uex4
            with dissolve

            no "Come on then! Show us something."

            scene v12uex9 # TPP Show MC doing a front flip
            with dissolve

            pause 0.5

            scene v12uex9a # TPP Same angle as v12uex9, MC lands after front flip
            with dissolve

            pause 0.5

            scene v12uex9b # TPP Same angle as v12uex9, MC doing a back flip
            with dissolve

            pause 0.5

            scene v12uex4
            with dissolve

            no "Oooo! The double flip... Very impressive, [name]. *Laughs*"

            scene v12uex5
            with dissolve

            imre "Showoff. *Chuckles*"

            scene v12uex5b # FPP Same angle as v12uex5, Imre smiling with mouth closed
            with dissolve

            u "*Laughs*"
        
        "Just watch":
            u "I'm just here to watch, actually... I was more of a monkey bars and seesaw kind of kid. *Laughs*"

            scene v12uex4
            with dissolve

            no "Hey, no shame in being the monkey bar kid. Those kids were strong... *Chuckles*"

    scene v12uex3a
    with dissolve

    au "Alright you wannabes... Make some room for the professional, would ya?"

    scene v12uex4
    with dissolve

    no "Uh, oh. *Chuckles*"

    # REVIEWER NOTE: I'M NOT SURE WHAT THE WRITERS INTENDED TO DISTINGUISH A BACK TUCK FROM A BACKFLIP - I CAN'T FIGURE OUT A DIFFERENCE. MIGHT NEED TO CLARIFY BEFORE RENDERING
    scene v12uex10 # FPP Show Aubrey doing a back tuck
    with dissolve

    pause 0.5

    scene v12uex10a # FPP Same angle as v12uex10, Aubrey landed after back tuck, arms in the air, with a big smile
    with dissolve

    u "Oh, shit... Aubrey, how the hell..."

    scene v12uex3a
    with dissolve

    au "Whew! That felt so good! *Laughs*"

    scene v12uex5
    with dissolve

    imre "Wait, was that not just a normal back flip?"

    scene v12uex3a
    with dissolve

    au "Back tuck, big difference. Let's go Nora, let me see that booty work. *Chuckles*"

    scene v12uex6a # FPP Same angle as v12uex6, Nora smiling with mouth open, Aubrey smiling with mouth closed
    with dissolve

    no "C'mon now, Aubs... I don't wanna embarrass you. *Chuckles*"

    scene v12uex6b # FPP Same angle as v12uex6, Aubrey smiling with mouth open, Nora smiling with mouth closed
    with dissolve

    au "You can try all you want, but you're not backing out now. *Chuckles*"

    scene v12uex6
    with dissolve

    u "I don't think she's backing out, I think she's giving you a warning. *Chuckles*"

    scene v12uex6b
    with dissolve

    au "Haha, okay then. Warning received, let's see it."

    scene v12uex6a
    with dissolve

    no "Okayyyy, but I did warn you."

    scene v12uex11 # FPP Show Nora performing a front hand spring
    with dissolve

    pause 0.5

    scene v12uex11a # FPP Same angle as v12uex11, Nora moving from front hand spring to a front tuck
    with dissolve

    pause 0.5

    scene v12uex11b # FPP Same angle as v12uex11, Nora landed after front tuck like an olympic gymnast
    with dissolve

    u "Let's gooooo!"

    scene v12uex3a
    with dissolve

    au "Damn, I didn't know you were actually that good, haha."

    scene v12uex4
    with dissolve

    no "I told you!"

    scene v12uex3a
    with dissolve

    au "Don't get all cocky just yet, hot stuff. you may be able to do some big stuff, but how are your basics? Can you do a perfect round off?"

    scene v12uex4
    with dissolve

    no "*Laughs* Yes, that's easy."

    scene v12uex3a
    with dissolve

    au "Prove it."

    scene v12uex4
    with dissolve

    no "Haha, okay..."

    scene v12uex12 # TPP Show Nora performing a round off toward MC
    with dissolve

    pause 0.5

    scene v12uex13 # FPP Show Nora coming toward MC, about to crash into him
    with dissolve

    menu (fail_label="v12s20_faillabel"):
        "Catch her":
            scene v12uex12a # TPP Same angle as v12uex12, show MC catching Nora from behind
            with dissolve

            pause 0.75

            scene v12uex4a
            with dissolve

            u "You good? *Chuckles*"

            scene v12uex4
            with dissolve

            no "Haha, yeah. Sorry I- Guess it went a little faster than I thought. Thanks for catching me, that probably would've hurt pretty bad."

            scene v12uex4a
            with dissolve

            u "Ha, don't worry about it."

        "Move":
            label v12s20_faillabel:
                $ reputation.add_point(RepComponent.TROUBLEMAKER)

                scene v12uex12b # TPP Same angle as v12uex12, show MC dodging out of the way of Nora
                with dissolve

                pause 0.75

                scene v12uex14 # FPP Show Nora sitting on the pavement with her hands on the ground behind her, as if she just landed hard, hurt expression, mouth open
                with dissolve

                no "Ow! Fuck... I went way too fast. Sorry [name], almost took you with me. *Chuckles*"

                scene v12uex14a # FPP Same angle as v12uex14, Nora with embarrassed expression, mouth closed
                with dissolve

                u "Haha, I made it out in time. You did come in pretty hot... *Laughs*"

    scene v12uex3a
    with dissolve

    au "Mhmm... Looking a little rusty, Nora. I thought you were once a pro?"

    scene v12uex14b # FPP Same angle as v12uex14, Nora getting up off the ground, embarrassed expression, mouth open
    with dissolve

    no "Okay... Maybe I have some warming up to do. *Chuckles*"

    scene v12uex5
    with dissolve

    imre "I can do a round off!"

    scene v12uex3a
    with dissolve

    au "Wait your turn little guy, gotta show off mine first."

    scene v12uex15 # FPP Show Aubrey beginning to do a roundoff
    with dissolve

    pause 0.5

    scene v12uex15a # FPP Show Aubrey falling while doing the roundoff
    with dissolve

    pause 0.5

    scene v12uex16 # FPP Show Aubrey on the ground, clutching her ankle, pained expression with mouth open
    with dissolve

    au "OH- FUCK... Oww! Ow, ow, ow..."

    scene v12uex17 # TPP Show MC, Imre, and Nora running toward Aubrey, who is on the ground, holding her ankle, in pain
    with dissolve

    pause 0.75

    scene v12uex18 # FPP Show Aubrey, closer now, still on the ground, in pain, mouth closed
    with dissolve

    u "Shit Aubrey, you alright?"

    scene v12uex18a # FPP Same angle as v12uex18, Aubrey in pain with mouth open
    with dissolve

    au "Fuck... No, I'm not. Landed right on my damn ankle."

    scene v12uex18
    with dissolve

    u "I swear, you and Riley with these weak ass ankles."

    scene v12uex18b # FPP Same angle as v12uex18, Aubrey still in pain but with a small smile, mouth open
    with dissolve

    au "That's my bestie, two weak ankle chicks. *Chuckles*"

    scene v12uex18c # FPP Same angle as v12uex18, Aubrey with neutral expression, looking down at her ankle, mouth open
    with dissolve

    au "I can tell it's just sprained, this has happened before believe it or not, haha. It'll be better by morning, but it hurts like fucking hell right now."

    scene v12uex4b # FPP Same angle as v12uex4, Nora with neutral expression, mouth open
    with dissolve

    no "We definitely gotta get you back, the quicker you ice it the better. Which seriously sucks 'cause I brought drinks for us all."

    scene v12uex18b
    with dissolve

    au "You don't have to leave because of me, Nora. I haven't seen you smile like this in a long time, so you're staying. One of the guys can stay with you and one can take me back...?"

    scene v12uex18
    with dissolve

    menu:
        "Walk Aubrey back to hotel":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            u "Of course, c'mon Aubrey. I'll walk you back."

            scene v12uex5
            with dissolve

            imre "Yessss!"

            scene v12uex18b
            with dissolve

            au "Way to make me feel loved, Imre."

            scene v12uex5
            with dissolve

            imre "Sorry Aubrey, but between the sunlight and the free drinks, this sounds like too good of a time to pass up."

            scene v12uex18
            with dissolve

            u "*Chuckles* Enjoy yourselves, c'mon Aubrey."

            scene v12uex19 # TPP Show MC helping Aubrey up from the ground
            with dissolve

            pause 0.75

            scene v12uex20 # TPP Show MC and Aubrey walking along sidewalk, Aubrey's arm over MC's shoulder for support
            with dissolve

            pause 0.75

            scene v12uex21 # TPP Show MC helping Aubrey to sit down on her hotel room bed
            with dissolve

            pause 0.75

            stop music fadeout 3
            
            jump v12_nursing_aubrey #scene 21a

        "Share a drink with Nora":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            u "Gotta be honest, cold drinks in the sun sounds pretty fucking nice. Imre, you're gonna have to walk Aubrey back."

            scene v12uex18b
            with dissolve

            au "Damn, \"have to?\" You make it sound like a chore. It's not like I chose to mess up my ankle."

            scene v12uex5c # FPP Same angle as v12uex5, Imre with neutral expression, mouth open
            with dissolve

            imre "And it's not like walking you back sounds fun, but I got drinks in my room. C'mon."

            scene v12uex19a # FPP Same angle as v12uex19, Imre helping Aubrey up from the ground
            with dissolve

            pause 0.75

            scene v12uex22 # FPP Show Imre and Aubrey walking away, Aubrey's arm over Imre's shoulder for support
            with dissolve

            pause 0.75
        
            stop music fadeout 3

            jump v12_nora_exploring #scene 21