# SCENE 23a: MC chilling in his room
# Locations: 
# Characters: MC (Outfit: 9), SAMANTHA (Outfit: 1), CAMERON (Outfit: 3)
# Time: Night

label v12_mc_chilling:
    if not v11_riley_roomate:
        scene v12mor1 # TPP. MC leaving riley's room
        with fade 
        play sound sound.door_close

        pause 0.75

        play music music.v12_Track_Scene_23a fadein 2

        scene v12mor2 # TPP. MC on the hotel hallway
        with dissolve

        pause 0.75

        scene v12mor3 # TPP. MC arriving on his room
        with dissolve
        play sound sound.door_open

        pause 1

        scene v12mor4 # TPP. MC going to his bed
        with dissolve

        pause 1

        scene v12mor5 # TPP. MC Laying on his bed
        with dissolve

    else:
        scene v12mor4
        with dissolve

        pause 0.75

        play music music.v12_Track_Scene_23a fadein 2

        scene v12mor5
        with dissolve

    pause 0.75
    scene v12mor6 # TPP. MC laying in bed, hands behind his back, mouth closed
    with dissolve

    u "(I feel like I haven't had any time to just lay back and chill. There's always so-)"

    if v11_invite_sam_europe:
        scene v12mor7 # FPP. Samantha bursts into MC's room holding a bottle of alcohol, looking drunk, mouth opened
        with dissolve

        sa "*Drunk* No one wants to hang out with me! Why is everyone ignoring me?!"

        scene v12mor8 # FPP. Samantha comes in mc's direction, smiling and drunk, mouth closed
        with dissolve
        
        pause 1

        scene v12mor9 # FPP. Samantha plops on mc's bed still looking drunk, mouth closed
        with dissolve

        u "Sam... Are you drunk right now? I thought you weren't drinking?"

        scene v12mor9a # FPP. Same as 9 smiling, mouth opened
        with dissolve

        sa "*Drunk* This is only my first drink."

        scene v12mor9 
        with dissolve

        u "*Chuckles* That might be your first drink, but that's a big ass bottle."

        scene v12mor9a
        with dissolve

        sa "*Drunk* I'm good... Promise!"

        scene v12mor9
        with dissolve

        u "What do you mean people are ignoring you?"

        scene v12mor9a
        with dissolve

        sa "*Drunk* I went to everyone's door, but none of them were open... Yours was unlocked, though!"

        scene v12mor9
        with dissolve

        u "(My luck.)"

        scene v12mor9
        with dissolve

        u "So, you were just trying to walk into random people's rooms? You know we aren't the only guests in the hotel right? *Chuckles*"

        scene v12mor9b # FPP. Same as 9, sam looking confused, mouth opened
        with dissolve

        sa "*Drunk* Wait, we're not?"

        scene v12mor9
        with dissolve

        u "Haha, no."

        scene v12mor9a
        with dissolve

        sa "*Drunk* Ohhhhh, that must be why that guy was yelling at me to leave him alone. I thought it was Ryan... *Chuckles*"

        scene v12mor9
        with dissolve

        u "Oh my god. *Laughs* Where's your brother?"

        scene v12mor9c # FPP. Same as 9, sam looking mad, mouth opened
        with dissolve

        sa "*Drunk* Why do you care where my stupid brother is? Why can't you just spend time with me?"

        scene v12mor9
        with dissolve

        u "I can, I just worry he'll run in here and try to fight me 'cause you're drunk."

        scene v12mor9c
        with dissolve

        sa "*Drunk* He's sleeping, okay? Happy now?"

        scene v12mor9
        with dissolve

        u "I am, yeah."

        scene v12mor9a
        with dissolve

        sa "*Drunk* Do you think I'm pretty?"

        menu:
            "What?" (troublemaker=1.0):
                $ reputation.add_point(RepComponent.TROUBLEMAKER)
                scene v12mor9
                with dissolve

                u "What? That's a really random question."

                scene v12mor9d # FPP. Same as 9, sam looking sad, mouth opened
                with dissolve

                sa "*Drunk* Which shouldn't take this long to answer... I get it..."

                scene v12mor9 
                with dissolve

                u "No, Sam. I mean, yeah. Of course you're pretty. I just wasn't expecting that question I guess."

            "Yes" (boyfriend=1.0):
                $ reputation.add_point(RepComponent.BOYFRIEND)
                scene v12mor9
                with dissolve

                u "Of course I do."

                scene v12mor9a
                with dissolve

                sa "*Drunk* Do you really think so? Like, do you think I'm really pretty?"

                scene v12mor9
                with dissolve

                u "Yes, Sam. I think you're very pretty. *Chuckles*"
   
        scene v12mor9c
        with dissolve

        sa "*Drunk* No you don't."

        scene v12mor9
        with dissolve

        u "Why'd you even ask me if you aren't gonna believe my answer?"

        scene v12mor9d
        with dissolve

        sa "*Drunk* Just wanted to see what you'd say... But, I know you don't think I'm \"that\" pretty."

        scene v12mor9
        with dissolve

        u "Ha, what? How do you know that?"

        scene v12mor10 # TPP. Samantha climbs on top of mc
        with dissolve

        pause 0.75

        scene v12mor11 # FPP. Samantha on top of mc, making a seductive face, mouth opened
        with dissolve

        sa "*Drunk* If you think I'm pretty... Then why haven't we done anything yet, huh? Why haven't you kissed me? Don't you wanna kiss me?"

        scene v12mor11a # FPP, Same as 11, mouth closed
        with dissolve

        u "Sam... Uh, my roommate could walk in here at any minute."

        scene v12mor11b # FPP. Sam still on top of mc, looking mad and drunk, mouth opened
        with dissolve

        sa "*Drunk* What? I'm not sexy enough to show off? See, I knew you didn't like me..."

        scene v12mor12 # TPP. Sam rolls of mc drunk, laying on his bed next to him
        with dissolve

        pause 0.75

        scene v12mor13 # FPP. sam looking drunk, next to mc on his bed, mouth opened
        with dissolve

        sa "*Drunk* I just want someone to really like me. Someone that's strong and can protect me... Oh, and he has to be able to beat up my brother!"

        scene v12mor13a # FPP. Same as 13, mouth closed
        with dissolve

        u "*Chuckles* What if he can't beat up your brother?"

        scene v12mor13
        with dissolve

        sa "*Drunk* Then he's not the right guy..."

        scene v12mor13b # FPP. same as 13, sam smiling and still drunk, mouth opened
        with dissolve

        sa "You know something I really want?"

        scene v12mor13a
        with dissolve

        u "What?"

        scene v12mor13b
        with dissolve

        sa "*Drunk* I wanna have sex in a pool."

        scene v12mor13b
        with dissolve

        sa "That's what I wanna do while I'm in college... Get a strong boyfriend that fucks me in the pool every, single, night."

        scene v12mor13a
        with dissolve

        u "Sam... Where is all this coming from?"

        scene v12mor13c # FPP.same as 13, Sam thinking looking away from MC at the ceiling, mouth opened
        with dissolve

        sa "*Drunk* Do you know if there's a pool on campus?"

        scene v12mor13a
        with dissolve

        u "There is, actually. I got invited to go swimming there once."

        scene v12mor13d # FPP. same as 13, Sam looking really excited, mouth opened
        with dissolve

        sa "*Drunk* Did you have sex in the pool?!"

        scene v12mor13a
        with dissolve

        u "*Chuckles* No. I didn't."

        scene v12mor13b
        with dissolve

        sa "*Drunk* Would you want to?"

        menu:
            "Yes":
                $ v12s23a_sam += 1
                scene v12mor13a 
                with dissolve
                
                u "Does sound kinda refreshing. *Laughs*"

                scene v12mor13b
                with dissolve

                sa "*Drunk* Good... Right answer."

            "No" (troublemaker=1.0):
                $ reputation.add_point(RepComponent.TROUBLEMAKER)
                scene v12mor13a
                with dissolve

                u "No, I don't think so."

                scene v12mor13e # FPP. Same as 13, sam booing, mouth opened
                with dissolve

                sa "*Drunk* Booooo... Wrong answer."

        scene v12mor13a
        with dissolve

        u "Haha, I didn't know there was a right and wrong answer."

        scene v12mor13f # FPP. same as 13, Sam trying to look serious, mouth opened
        with dissolve

        sa "*Drunk* Every choice is important... Now, can you beat up my brother?"

        scene v12mor13a
        with dissolve

        u "Cameron?"

        scene v12mor13b
        with dissolve

        sa "*Drunk* No, Chris... *Chuckles* What other brother is there?"

        menu:
            "I can beat Cameron":
                $ v12s23a_sam += 1
                $ reputation.add_point(RepComponent.TROUBLEMAKER)
                
                scene v12mor13a
                with dissolve
            
                u "Yeah. Of course I can take him. He may be a lunatic, but I can handle that."

            "Not fighting your brother" (bro=1.0):
                $ reputation.add_point(RepComponent.BRO)
                scene v12mor13a 
                with dissolve
                
                u "Nope, not wasting any time on that fight. Your brother's a psychopath. Sorry."

                scene v12mor13b 
                with dissolve

                sa "*Drunk* Ughhh, such a pussy. *Chuckles*"

        if v12s23a_sam == 2:
            scene v12mor13d
            with dissolve
            
            sa "*Drunk* Perfect! You can be my boyfriend then."

            scene v12mor13a
            with dissolve

            u "*Laughs* What?"

            scene v12mor13b
            with dissolve

            sa "*Drunk* Yeah! You can kick Cameron's ass when he's bothering me and also fuck me in the pool every day."

            scene v12mor13b
            with dissolve

            sa "That's all I want, and you can do it... So, you can be my boyfriend!"

            scene v12mor13a
            with dissolve

            u "Sam, I think you're really-"

            scene v12mor14 # TPP. Sam climbs on top of mc and kisses him
            with dissolve

            pause 0.75

            scene v12mor15 # FPP. Sam making a seductive face, still drunk, mouth opened
            with dissolve

            sa "*Drunk* Take your clothes off, boyfriend."

            scene v12mor15a # FPP. Same as 15, mouth closed
            with dissolve

            u "Sam, you're completely wasted right now."

            scene v12mor15
            with dissolve

            sa "*Drunk* And?"

            scene v12mor15a
            with dissolve

            u "And... So maybe we should relax, and like I said, my roommate could come in anytime."

        else:
            scene v12mor13f
            with dissolve

            sa "*Drunk* Well, whatever... No matter what, you can't be my boyfriend 'cause you don't meet my standards."

            scene v12mor13a
            with dissolve

            u "Your standards are beating up your brother and fucking you in a pool everyday?"

            scene v12mor13f
            with dissolve

            sa "*Drunk* Yeah, what's wrong with that?"

            scene v12mor13a
            with dissolve

            u "Those aren't real standards. *Chuckles*"

        scene v12mor16 # TPP. Samantha getting up from MC's bed
        with dissolve

        pause 0.75

        scene v12mor17 # FPP. MC looking at sam heading to his roomate's bed, back to the camera
        with dissolve

        sa "*Drunk* Ughhh, whatever!"

        scene v12mor18 # FPP. Sam laying in MC's roomate's bed, back turned to MC as if ignoring him
        with dissolve

        u "Sam?"

        sa "*Drunk* Leave me alone."

        u "Sam, c'mon."

        sa "..."

        u "Sam?"

        scene v12mor19 # TPP. MC getting out of his bed
        with dissolve

        pause 1

        scene v12mor20 # FPP. MC Checking on sam sleeping
        with dissolve

        u "Haha, I've seen this before."

        scene v12mor21 # TPP. MC tucks samantha into the bed
        with dissolve

        pause 0.75

        scene v12mor22 # TPP. MC laying back down on his bed
        with dissolve

        menu:
            "Call Cameron" (bro=1.0):
                $ reputation.add_point(RepComponent.BRO)

                scene v12mor23 # TPP. MC holding his phone, mouth closed
                with dissolve
                u "(*Sighs* He should at least know she's drunk.)"

                scene v12mor24 # TPP. MC with the phone to his ear, mouth closed
                with dissolve
                play sound sound.answer_call

                pause 0.75

                scene v12mor25 # TPP. Cameron picks up laying in his bed, mouth opened
                with dissolve

                ca "Huh? [name]? What do you want?"

                scene v12mor24a # TPP. Same as 24, mouth opened
                with dissolve

                u "Hey man, I was just calling you to let you know that your sister got wasted tonight."

                scene v12mor25a # TPP. Same as 25, cameron looking mad, mouth opened
                with dissolve

                ca "YOU'RE WITH MY SISTER?!"

                scene v12mor24b # TPP. same as 24, MC looking worried, mouth opened
                with dissolve

                u "(Fuck...) No, no, she's with the girls. They're taking care of her, but I just wanted to let you know that I guess she's drinking again."

                scene v12mor25
                with dissolve

                ca "What room is she in?"

                scene v12mor24a
                with dissolve

                u "I'm not sure, but I'm positive she'll be fine, man. The girls got her. I just wanted you to know."

                scene v12mor25
                with dissolve

                ca "*Sighs* Okay, later."

                scene v12mor24a
                with dissolve

                u "Later man."

                scene v12mor25b # TPP. same as 25, Cameron looking grateful, mouth opened
                with dissolve

                ca "Hey, [name]! Wait..."

                scene v12mor24a
                with dissolve

                u "Yeah?"

                scene v12mor25b
                with dissolve

                ca "It was cool of you to call me. You didn't have to do that, but you did anyway. You're a real Ape, I won't forget this."

                scene v12mor24c # TPP. same as 24, MC smiling, mouth opened 
                with dissolve

                u "No worries, Cam. I'd want someone to call me, it's no big deal."

                scene v12mor25b
                with dissolve

                ca "No man, it is. Thanks."

                scene v12mor24c
                with dissolve

                u "You're welcome. Goodnight, bro."

                scene v12mor25b
                with dissolve

                ca "Night."

                scene v12mor24e # TPP. MC puts his phone away, slight smile
                with dissolve
                play sound sound.reject_call

                pause 0.75

            "Don't call Cameron" (boyfriend=1.0):
                $ reputation.add_point(RepComponent.BOYFRIEND)
                scene v12mor22
                with dissolve

                u "(Not even gonna attempt to open up that door.)" 

        scene v12mor22
        with dissolve

        if v11_riley_roomate:
            u "(Don't know where Riley went, but she's gonna have to deal with Sam from here on out. I'm going to sleep.)"
        else:
            u "(Don't know where Chloe went, but she's gonna have to deal with Sam from here on out. I'm going to sleep.)"

        scene v12mor27 # TPP. MC shuts down the lights
        with dissolve

        pause 0.75

    else: 
        play sound sound.call

        pause 1.25

        scene v12mor23
        with dissolve

        pause 1

        scene v12mor24a
        with dissolve
        stop sound
        play sound sound.answer_call

        u "Hello?"

        scene v12mor28 # TPP. Samantha drunk holding her phone, screaming, mouth opened
        with dissolve

        sa "*Drunk* HELLO? CAN YOU HEAR ME?!"

        scene v12mor24b
        with dissolve

        u "Sam, are you drunk right now? I thought you weren't drinking?"

        scene v12mor28a # TPP. Samantha slight smiling, mouth opened
        with dissolve

        sa "*Drunk* This is only my first drink."

        scene v12mor24b
        with dissolve

        u "Fine, I won't push you. Remember you're lightweight though, yeah?"

        scene v12mor28a
        with dissolve

        sa "*Drunk* I'm fine... What are you doing?"

        scene v12mor24a
        with dissolve

        u "I'm just laying in bed, getting ready to go to sleep."

        scene v12mor28a
        with dissolve

        sa "*Drunk* Do you miss me?"

        menu:
            "Yes, I miss you":
                scene v12mor24c 
                with dissolve

                u "Honestly, yeah. It'd be really nice to have you here right now."

                scene v12mor28a
                with dissolve

                sa "*Drunk* Awww, I wish I was there too."


            "No, I don't miss you (Joke)" (troublemaker=1.0):
                $ reputation.add_point(RepComponent.TROUBLEMAKER)
                scene v12mor24a
                with dissolve

                u "Nope, I'm actually super happy that you're not here."

                scene v12mor28
                with dissolve

                sa "*Drunk* WHAT!? That's so mean!"

                scene v12mor24c
                with dissolve

                u "Haha, I'm just messing with you."

                scene v12mor28a
                with dissolve

                sa "*Drunk* Don't play around like that with me! You scared me... Jerk. *Chuckles*"

                scene v12mor24c
                with dissolve

                u "*Chuckles* My bad."

        scene v12mor28b # TPP. Samantha making a seducing face, mouth opened
        with dissolve

        sa "*Drunk* What would you do to me if I was there?"

        scene v12mor24b
        with dissolve

        u "Sam, where are these questions coming from? Where are you right now?"

        scene v12mor28a
        with dissolve

        sa "*Drunk* Umm, I don't know..."

        scene v12mor24b
        with dissolve

        u "What do you mean you \"don't know\"?"

        scene v12mor28c # TPP. Sam smiling, mouth opened
        with dissolve

        sa "*Drunk* What do you mean, what do I mean?  How'd you make it into college?!"

        scene v12mor28c
        with dissolve

        sa "*Drunk* You're so silly... *Laughs*"

        scene v12mor24b
        with dissolve

        u "Sam, where's your brother?"

        scene v12mor28d # TPP. Sam looking confused, mouth opened
        with dissolve

        sa "*Drunk* Why does it matter? I don't need him to babysit me."

        scene v12mor24b
        with dissolve

        u "I just wanna make sure everything's okay. You have me a little worried. You're calling super late, you don't know where you are, and you're drunk."

        scene v12mor28c
        with dissolve

        sa "*Drunk* Awww, you're worried about me? *Chuckles* You just wanna get into my pants like all the other guys..."

        scene v12mor24b
        with dissolve

        u "Sam, I'm trying to be serious with you!"

        scene v12mor28e # TPP. Sam looking disapointed, mouth opened
        with dissolve

        sa "*Drunk* And I actually thought you were a nice guy, but you're just like all the rest..."

        scene v12mor24b
        with dissolve

        u "Sam, what the fuck are you talking about? I'm trying to make sure you're okay. Where is y-"

        scene v12mor28e
        with dissolve

        sa "*Drunk* Forget my number, you stupid fuckboy!"

        play sound sound.reject_call

        scene v12mor24b
        with dissolve

        u "Sam? Hello? Hello?!"

        scene v12mor24d # TPP. MC looking at his phone, worried face, mouth closed
        with dissolve

        u "(She hung up on me. Guess I'll call her back.)"

        scene v12mor24
        with dissolve

        u "(Fucking voicemail.)"

        scene v12mor24e
        with dissolve

        menu:
            "Call Cameron" (bro=1.0):
                $ reputation.add_point(RepComponent.BRO)

                scene v12mor24d
                with dissolve

                u "(*Sighs* He should know that she's drunk.)"

                play sound sound.answer_call

                pause 0.75
                scene v12mor25
                with dissolve

                ca "Huh? [name]? What do you want?"

                scene v12mor24a
                with dissolve

                u "Hey man, I was just calling you to let you know that your sister's drunk."

                scene v12mor25
                with dissolve

                ca "What? How would you know?"

                scene v12mor24a
                with dissolve

                u "She just called saying a bunch of crazy shit. She couldn't even tell me where she is right now."

                scene v12mor25
                with dissolve

                ca "What did she say?"

                scene v12mor24a
                with dissolve

                u "None of it made any sense. When I tried figuring out where she was, she hung up and then wouldn't answer when I called back."

                scene v12mor25
                with dissolve

                ca "*Sighs* Okay, man."

                scene v12mor24a
                with dissolve

                u "Try and figure it out, good luck. Later."

                scene v12mor25
                with dissolve

                ca "Hey [name]! Wait..."

                scene v12mor24a
                with dissolve

                u "Yeah?"

                scene v12mor25b
                with dissolve

                ca "It was cool of you to call me. You didn't have to do that, but you did anyway. You're a real Ape, I won't forget this."

                scene v12mor24a
                with dissolve

                u "I'd want someone to call me too. It's no big deal."

                scene v12mor25b
                with dissolve

                ca "No man, it is. Thanks."

                scene v12mor24a
                with dissolve

                u "You're welcome, goodnight bro."

                scene v12mor25b
                with dissolve

                ca "Night."

                scene v12mor24e
                with dissolve

                pause 0.75

            "Don't call Cameron" (boyfriend=1.0):
                $ reputation.add_point(RepComponent.BOYFRIEND)
                scene v12mor22
                with dissolve

                u "(Not even gonna attempt to open up that door.)"

        scene v12mor22
        with dissolve

        if v11_riley_roomate:
            u "(Don't know where Riley went, but I'm going to sleep now.)"
        else:
            u "(Don't know where Chloe went, but I'm going to sleep now.)"

        scene v12mor27
        with dissolve

        pause 0.75
        
    scene v12mor29 # TPP. Same as 22, different position
    with dissolve

    pause 0.75

    scene black
    with fade
    
    pause 2.25

    stop music fadeout 3

    jump v12_simplr_convo #scene 24