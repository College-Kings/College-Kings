init python:
    def v6_reply1():
        add_point(KCT.BRO)
        amber.messenger.newMessage(_("I'm playing drink or dare and got dared to send an underwear pic to a guy."))
        amber.messenger.addReply(_("And you chose me, huh?"), v6_reply2)
        amber.messenger.addReply(_("Feel free to do so anytime :)"), v6_reply3)

    def v6_reply2():
        add_point(KCT.BRO)
        amber.messenger.newMessage(_("Maybe I picked someone at random ;)"))

    def v6_reply3():
        add_point(KCT.BOYFRIEND)
        amber.messenger.newMessage(_("Maybe if you're lucky xx"))

    def v6_reply4():
        add_point(KCT.BOYFRIEND)
        amber.messenger.newMessage(_("I'm glad you like it xx"))
        amber.messenger.addReply(_( "I hope there's more of that in the future :P"))
        amber.messenger.newMessage(_("Maybe if you're lucky xx"))

    def v6_reply5():
        add_point(KCT.TROUBLEMAKER)
        add_point(KCT.BRO)
        amber.messenger.newMessage(_("Moment's passed..."))

    def v6_reply6():
        add_point(KCT.BOYFRIEND)
        amber.messenger.newMessage(_("You better xx"))

    def v6_reply7():
        setattr(store, "meetaubrey", True)
        aubrey.messenger.newMessage(_(":)"))

    def v6_reply8():
        aubrey.messenger.newMessage(_("Oh, okay"))

    def v6_reply9():
        amber.messenger.newMessage(_("Yeah maybe we should xx"))

    def v6_reply10():
        add_point(KCT.BOYFRIEND)
        setattr(store, "homrworkout", False)

    def v6_reply11():
        amber.messenger.addReply(_("I'm alone now, if the surprise is still on ;)"), v6_reply5)
        amber.messenger.addReply(_("I'll make it up to you tho"), v6_reply6)

label script06: #for compatibility only
label v6start:
    if imre.relationship <= Relationship.MAD and chloe.relationship <= Relationship.MAD:
        menu:
            "Find Imre":
                $ add_point(KCT.BRO)
                $ chooseimre = True

                jump imrecona

            "Keep talking to Amber":
                $ add_point(KCT.TROUBLEMAKER)
                $ chooseimre = False

                jump imreconc

    elif imre.relationship <= Relationship.MAD:
        menu:
            "Find Imre":
                $ add_point(KCT.BRO)
                $ chooseimre = True

                jump imrecona

            "Meet Chloe":
                $ add_point(KCT.BOYFRIEND)
                $ chooseimre = False
                $ meetchloe = True

                jump imrecond


    elif chloe.relationship <= Relationship.MAD:
        menu:
            "Help Imre":
                $ add_point(KCT.BRO)
                $ chooseimre = True

                jump imreconb

            "Keep talking to Amber":
                $ add_point(KCT.TROUBLEMAKER)
                $ chooseimre = False

                jump imreconc

    else:
        menu:
            "Help Imre":
                $ add_point(KCT.BRO)
                $ chooseimre = True

                jump imreconb

            "Meet Chloe":
                $ add_point(KCT.BOYFRIEND)
                $ chooseimre = False
                $ meetchloe = True

                jump imrecond


label imrecona: # Find Imre
    u "(I need to find Imre and apologize. He's probably in our dorm room.)"

    scene s443 # you entering dorm
    with fade
    play sound "sounds/dooropen.mp3"
    pause 0.5

    scene s444 # Imre packing his bag
    with dissolve

    u "Imre, look-"

    u "Wait, what are you doing???"

    scene s445 # Imre turned around closeup dissapointed
    with dissolve

    imre "I'm moving out."

    scene s445a
    with dissolve

    u "What?! Dude, we had one little argument."

    scene s445b # Imre angry
    with dissolve
    imre "You decided what was right for me, without even asking. You got no type of loyalty at all!"

    menu:
        "Explain yourself":
            $ add_point(KCT.BRO)

            scene s445c
            with dissolve

            u "Look, you're injured and I don't want you to bleed internally. I did what I had to!"

            u "You know our friendship comes first, but sometimes loyalty means protecting each other even if we don't wanna be protected."

            if kct == "loyal":
                call screen kct_popup

                $ imreforgives = True

                scene s445
                with dissolve

                imre "Even if you're right, that was my fight..."

                scene s445a
                with dissolve

                u "I'm sorry, you'll get your revenge someday... but not while you're injured."

                scene s445
                with dissolve

                imre "Yeah, I guess..."

                scene s447 # Imre sits down contemplating looking at the floor
                with dissolve

                pause 0.5

                u "Does that mean you're staying?"

                scene s447a # Imre looks at you
                with dissolve

                imre "Alright."

                scene s447a2
                with dissolve

                u "Brothers?"

                scene s447a # Imre thoughtful
                with dissolve

                imre "Brothers."

                imre "I need some time to think. I'll see you later."

                scene s447a2
                with dissolve

                u "Alright, let me know if there's anything else I can do."

                scene s450b # Imre stands up and walks away
                with dissolve

                pause 0.5

                scene s450c # Imre gone
                with dissolve

                pause 0.5

                jump continuebb

            else:
                $ imreforgives = False
                scene s445b
                with dissolve

                imre "Fuck do you know about loyalty?! You just wanna be in control!"

        "Apologize":
            $ add_point(KCT.BOYFRIEND)
            $ imreforgives = False

            scene s445c
            with dissolve

            u "I'm sorry. I shouldn't have done what I did."

            u "I'm really sorry."

            scene s445b
            with dissolve

            imre "Fuck you! Your shitty apologies mean nothing!"

    imre "I'm fucking done with you! I'm staying with a friend 'till they find me a new dorm."

    scene s450b # Imre walking out
    with dissolve

    u "Come on Imre, you're overreacting!"

    play sound "sounds/slam.mp3"

    scene s450c # Imre gone
    with vpunch

    u "FUCK!"

    jump continuebb

label imreconb: # Help Imre

    $ grant_achievement("bros_before_hoes")

    u "(I need to help Imre, Adam will destroy him in his current condition.)"

    scene s448 ### FIRST PERSON: MC finds Imre banigng on Adams door
    with fade

    imre "Come out you piece of shit!"

    imre "You can't fucking hide from me forever!"

    scene s448a
    with dissolve

    u "Shit, is Adam hiding from you in his room?"

    scene s449 # Imre turns to you close up, slightly mad confused
    with dissolve

    imre "I mean, I didn't see him go in there..."

    scene s449a
    with dissolve

    u "Oh, so he's probably not in the dorm...?"

    scene s449
    with dissolve

    imre "Or he's hiding."

    scene s449a
    with dissolve

    u "Can we just sit down in our dorm room and talk?"

    u "He's clearly not here anyways."

    scene s449
    with dissolve

    imre "Fine..."

    scene s450 # Imre sitting on his bed in your dorm close, dissapointed
    with fade

    imre "You know, it's just... my brother would never let someone do that to him."

    scene s450a
    with dissolve

    u "Yeah but that doesn't mean your brother would just risk his life fighting with broken ribs."

    scene s450
    with dissolve

    imre "You're right, he would have beaten Adam up the first time and would've never gotten injured."

    scene s450a
    with dissolve

    u "Look, there's a time to get revenge, but it's not now."

    scene s450
    with dissolve

    imre "Mhm..."

    imre "I need some time to think. I'll see you later."

    scene s450a
    with dissolve

    u "Alright, let me know if there's anything else I can do."

    scene s450b # Imre stands up and walks away
    with dissolve

    pause 0.5

    scene s450c # Imre gone
    with dissolve

    pause 0.5

    jump continuebb

label imreconc: # Keep talking to Amber
    u "(Fuck it, Imre can wait.)"

    u "(I know a spot where I'm completely alone...)"

    scene s475 # MC in a remote location
    with fade

    $ amber.messenger.addReply(_("I'm all by myself now."))
    $ amber.messenger.newImgMessage("images/v6/text2.webp")
    $ amber.messenger.addReply(_("Woah, what was that for?"), v6_reply1)
    $ amber.messenger.addReply(_("Oh wow, you're so fucking hot"), v6_reply4)

    label phonead:
        if amber.messenger.replies:
            call screen phone
        if amber.messenger.replies:
            u "(Time to text Amber.)"
            jump phonead

    u "(Amber is so fucking hot, I hope she sends more pictures like that in the future.)"

    u "(Although I feel like I could've just received this in the park.)"

    u "(I should probably go back to my dorm and check on Imre now.)"

    jump fs_bd

label imrecond: # Meet Chloe
    u "(Fuck it, Chloe's more important.)"

    $ chloe.messenger.addReply(_("I'll make time for you :)"))
    $ chloe.messenger.newMessage(_("That's what I like to hear :*"))
    $ chloe.messenger.newMessage(_("Meet me at the school's swimming pool"))
    $ chloe.messenger.addReply(_("Cool, see you there"))

    label phoneac:
        if chloe.messenger.replies:
            call screen phone
        if chloe.messenger.replies:
            u "(I should reply to Chloe.)"
            jump phoneac

    stop music fadeout 3

    u "(Time to go swimming with the hottest girl in school...)"

    scene s451 ## FIRST PERSON: you see chloe sitting in bikini at the pool staring at the water
    with Fade (1,0,1)
    play music "music/m16punk.mp3"

    queue music [ "music/mchill1.mp3", "music/m7punk.mp3" ]

    pause 0.5

    u "Hey, Chloe."

    scene s451a #chloe turns around smiling
    with dissolve

    cl "Heyyy!"

    scene s452 # Chloe walks towards Mc
    with dissolve

    pause 0.5

    scene s452a # they hug
    with dissolve

    pause 0.5

    scene s452b # chloe stands in front of mc smiling
    with dissolve

    pause 0.5

    scene s453a # FIRST PERSON: Chloe close up in front of you smiling
    with dissolve

    u "So... swimming, huh?"

    scene s453b # Chloe flirty
    with dissolve

    cl "What, you don't wanna see me in a bikini?"

    scene s453c
    with dissolve

    u "That's definitely not it, haha."

    u "Uhm, thinking about it, I did kinda forget to bring swimming trunks."

    scene s453b
    with dissolve

    cl "Well then you'll have to swim in your boxers."

    cl "You're not leaving here without getting into the water with me."

    scene s453c
    with dissolve

    u "I guess I don't have a choice."

    scene s453d # chloe checking you out
    with fade

    u "What are you looking at?"

    scene s453e # chloe playful
    with dissolve

    cl "*Chuckles* Hey, you stare at me all the time."

    cl "I'm just trying to get us even."

    scene s453f
    with dissolve

    u "Stare at you? You wish."

    scene s455 # Chloe trying to push Mc in (close to the edge of the pool)
    with dissolve

    cl "So, you're jumping in first, right?"

    scene s455a # you defend yourself by grabbing chloe
    with dissolve

    u "Hey, you're gonna-"

    play sound "sounds/splash.mp3"

    scene s456 # they fall into the water
    with vpunch

    cl "*High pitched scream*"

    scene s457 #FIRST PERSON: close up chloe in the water laughing(wet hair & body)
    with dissolve

    cl "*Laughingly* Wow. I can't believe you did that."

    scene s457a
    with dissolve

    u "Well if I'm going down, you're going down with me."

    scene s457b # chloe comes a bit closer, flirty, tilts her head slightly
    with dissolve

    cl "That's fair."

    scene s457c
    with dissolve

    pause 0.5

    play sound "sounds/splash2.mp3"
    scene s457e2 # chloe moves a bit away and splashes wateer
    with vpunch

    "*Splash*"

    scene s457e
    with dissolve

    u "Ey!"

    scene s457f #chloe swims away
    with dissolve

    cl "*Laughs*"

    scene s458 # mc chases chloe mc hair wet too
    with dissolve

    u "I'll get you for that!"

    scene s458a # mc catches her
    with dissolve

    cl "*Laughs* You're too fast for me!"

    scene s459 #mc and arms around her waist
    with dissolve

    pause 0.5

    scene s459a # she leans in a bit closer , tilts her head a bit
    with dissolve

    pause 0.5

    play sound "sounds/ring.mp3"

    "*Phone rings*"

    scene s459b # Chloe pulls back
    with dissolve

    menu:
        "Just let it ring":
            $ add_point(KCT.TROUBLEMAKER)
            $ add_point(KCT.BOYFRIEND)

            scene s460a # FIRST PERSON: chloe close up, she's turned around looking at her phone
            with dissolve

            u "Just let it ring..."

            scene s460b # chloe looks back at you with a smiling likde "you're stupid" kinda playful
            with dissolve

            cl "What if it's important?"

            scene s460c
            with dissolve

            u "*Sighs* Alright."

            scene s460b
            with dissolve

            cl "I'll be right back."

        "You should get that":
            $ add_point(KCT.BRO)

            scene s460a
            with dissolve

            u "You should probably get that, huh?"

            scene s460b
            with dissolve

            cl "Yeah... I'll be right back."

    label fo_ad: #for compatibility only
    scene s460d # cl swims towards her phone
    with dissolve

    pause 0.5

    scene s461 # cl lift herself out of the pool
    with dissolve

    pause 0.5

    scene s462 # chloe on the phone
    with dissolve

    cl "Hey, what's up?"

    scene s462a
    with dissolve

    pause 0.5

    scene s462
    with dissolve

    cl "Already? Yeah, alright..."

    scene s462a
    with dissolve

    pause 0.5

    scene s462
    with dissolve

    cl "No one. I'll see you in a bit."

    scene s462a
    with dissolve

    pause 0.5

    scene s462
    with dissolve

    cl "Yeah, haha. Bye."

    play sound "sounds/rejectcall.mp3"

    scene s463 # mc sitting on the side of the pool with a towel as Chloe walks back to him with towel, mc looking at the water
    with dissolve

    menu:
        "Ask about the call":
            $ add_point(KCT.BOYFRIEND)

            scene s463a # chloe sits down next to you with towel , mc looks at her mouth open
            with dissolve

            u "So, who called you?"

            scene s464 # FIRST PERSON chloe close up sitting next to you wrapped in a towel
            with dissolve

            cl "Oh, just a friend."

        "Don't ask":
            $ add_point(KCT.BRO)

            scene s463b # same as s463a but mouth closed
            with dissolve

            pause 0.5

            scene s464
            with dissolve

    label fp_ad: #for compatibility only
    cl "I gotta go soon, but this was really fun."

    scene s464a
    with dissolve

    u "Oh, already? You really are busy."

    scene s464b # chloe confident / cheeky
    with dissolve

    cl "What can I say? I'm just that important. *Chuckles*"

    scene s465 #no longer first person: Chloe stood up, you're still sitting, towel in her hand
    with dissolve

    cl "I'm gonna get dressed. I'll see you sometime soon, okay?"

    scene s465a # you stand up
    with dissolve

    u "Yeah, sounds good."

    scene s465b # Chloe comes closer
    with dissolve

    cl "Bye."

    scene s465d # chloe kisses you on your cheek
    with dissolve
    play sound "sounds/kiss.mp3"
    pause 1.0

    scene s465b # same as s465b but your mouth open adn chloes closed
    with dissolve

    u "Bye."

    scene s466 #EVENING lighting: outside of the college, you see chloe in the distance walking away
    with fade

    u "(I wonder if she's meeting up with another guy, it did sound kinda suspicious.)"

    menu:
        "Follow her":
            $ add_point(KCT.TROUBLEMAKER)

            scene s466a # chloe walked a bit further
            with dissolve

            u "(I should follow her. What if Ryan wasn't so wrong about Chloe after all?)"

            scene s467 #Mc follows Chloe , some place
            with fade

            pause 0.5

            scene s468 # mc hiding behind bush, can't see who chloe's talking to
            with dissolve

            cl "Heyyy!"

            scene s468a # Aubrey hugs Chloe, becomes visible
            with dissolve

            au "Did you just come out of the shower?"

            scene s468b
            with dissolve

            u "(Phew, it's just Aubrey. I should probably get out of here before they find me...)"

            u "(I wonder if they talk about me though. I could just stay a bit longer.)"

            menu:
                "Stay and listen":
                    $ chloe.relationship = Relationship.MAD
                    $ chloecaught = True
                    $ add_point(KCT.TROUBLEMAKER)

                    scene s469 # chloe and Aubrey close up talking
                    with dissolve

                    cl "I was swimming, actually."

                    scene s469a
                    with dissolve

                    au "Uhh, with who?"

                    scene s469
                    with dissolve

                    cl "With [name]."

                    scene s469a
                    with dissolve

                    au "He's cute, isn't he?"

                    scene s469
                    with dissolve

                    cl "And he, like, actually cares... unlike some other guys."

                    scene s469a
                    with dissolve

                    au "Yeah, unlike Grayson."

                    scene s469
                    with dissolve

                    cl "Exactly."

                    play sound "sounds/twig.mp3"

                    scene s469b # both girls look in your direction but not directly at you
                    with dissolve

                    "*Twig cracks*"

                    u "(Shit.)"

                    scene s469c
                    with dissolve

                    cl "What was that?"

                    scene s470 # First person: Chloe comes closer and spots you, you're sitll hiding in the bush so she looks down
                    with dissolve

                    cl "[name]?!"

                    u "I... uh... I can explain."

                    scene s471 #FIRST PERSON:Aubrey face  suprised slight laughing but not upset(she's standing behind chloe to one side, enough not to be in chloe's shots following, now you stood up so camera is eye height
                    with dissolve

                    au "Were you spying on us?"

                    scene s471a
                    with dissolve

                    u "No I... I was just worried you know."

                    scene s472 # FIRST PERSON: Chloe looking at you eyeheight mad
                    with dissolve

                    cl "About what?"

                    scene s472a
                    with dissolve

                    u "Nothing, I just thought..."

                    scene s472
                    with dissolve

                    cl "Do you not trust me? What? Did you think I was off meeting up with another guy?!"

                    scene s472a
                    with dissolve

                    u "It's not like that, it's just... the phone call, I-"

                    scene s472
                    with dissolve

                    cl "That was from Aubrey. I can't believe you..."

                    scene s472b # chloe turns towards aubrey
                    with dissolve

                    cl "Come on Aubrey."

                    scene s473 # chloe and Aubrey walk away
                    with dissolve

                    u "Chloe! Chloe wait! Ugh..."

                    scene s473a
                    with dissolve

                    pause 0.5

                    scene s474 # Mc walking ghome depressed
                    with fade

                    u "*Sighs*"

                "Leave":
                    $ add_point(KCT.BRO)

                    u "(No, I should just get out of here and stop spying on her.)"

        "Trust her":
            $ add_point(KCT.BOYFRIEND)
            
            $ grant_achievement("credulous")

            u "(I shouldn't spy on her. It's not right.)"

# opening the room of your dorm after not choosing Imre, if imre mad, find a note of him moved out, if = False, he's gone and you call imre and he tells you that ADAM wasnt in his dorm, you have the same talk as if you had visited him over the phone
label fs_bd:
    play sound "sounds/dooropen.mp3"
    scene s476 # you Entering your dorm room # cant look inside yet
    with Fade (1,0,1)

    pause 1.0

    if imre.relationship <= Relationship.MAD:
        scene s477 # FIRST PERSON you look at Imre's bed, all his stuff is gone, you find a note on his bed
        with dissolve

        u "(What's this?)"

        # show note about how Imre moved out

        u "(He moved out???)"

        u "(Fuck, maybe I could've stopped him if I had just talked to him immediately...)"

        # note closes

        scene s478 # No longer first person: you walk towards your bed
        with dissolve

        pause 0.5

        scene s478a # you laying on your bed sadly contemplating  looking at the ceiling
        with dissolve

        pause 0.5

        scene s479 # same as before but camera perspective from above
        with dissolve

        u "*Sighs*"

    else:
        scene s480 # you come into your dorm but Imre's stuff is still there
        with dissolve

        u "(Fuck, Imre isn't here... I hope he's okay, I better call him.)"

        scene s481 # you calling Imre scared
        with dissolve

        play sound "sounds/calling.mp3"

        pause 0.5

        stop sound
        imre "Yeah?"

        scene s481a
        with dissolve

        u "Imre, you okay? What happened?"

        scene s481
        with dissolve

        imre "Well I was banging on this bastard's door, but he was too pussy to open."

        scene s481a
        with dissolve

        u "Shit, he was hiding from you?"

        scene s481
        with dissolve

        imre "I mean he didn't say shit, so yeah."

        scene s481b # u ironic disappointment
        with dissolve

        u "Oh, so he wasn't home."

        scene s481c
        with dissolve

        imre "Or he was hiding. Whatever."

        scene s481d # u empathy
        with dissolve

        u "Where are you now?"

        scene s481e
        with dissolve

        imre "Walking round town, trying to think."

        scene s481d
        with dissolve

        u "Alright, I'm here if you wanna talk."

        scene s481e
        with dissolve

        imre "Alright, see you later."

        scene s481d
        with dissolve

        u "Yeah, bye."

        play sound "sounds/rejectcall.mp3"

label continuebb:
    scene s482 # transition slide from your dorm, you doing something
    with Fade (1,0,1)

    pause 1.0

    # amber texts if chloe not mad
    # if you chose imre chloe and amber both text you depending on chloe mad that you msised out etc.

    if chooseimre and chloe.relationship <= Relationship.MAD: # Amber texts why you never got back to her
        play sound "sounds/vibrate.mp3"
        
        $ amber.messenger.newMessage(_("I guess you didn't want my surprise :/"), force_send=True)
        $ amber.messenger.addReply(_("Sorry something important came up and I didn't have time."), v6_reply11)

        " "

        label phoneae:
            if amber.messenger.replies:
                call screen phone
            if amber.messenger.replies:
                u "(I should probably reply to my messages.)"
                jump phoneae

        jump continuebd

    elif chooseimre: # Amber texts you about the pic, chloe texts you about you not responding
        play sound "sounds/vibrate.mp3"
        $ chloe.messenger.newMessage(_("I guess we'll do it another time..."), force_send=True)
        $ chloe.messenger.addReply(_("Sorry, something really important came up. Definitely another time"))
        $ chloe.messenger.newMessage(_("Okay"))

    elif chloe.relationship <= Relationship.MAD and not chloecaught:
        jump continuebd
            
    play sound "sounds/vibrate.mp3"
    
    $ amber.messenger.newMessage(_("Hey, you alone? xx"), force_send=True)
    $ amber.messenger.addReply(_("Yeah, I'm in my dorm, why?"))
    $ amber.messenger.newImgMessage("images/v6/text2.webp")
    $ amber.messenger.addReply(_("Woah, what was that for?"), v6_reply1)
    $ amber.messenger.addReply(_("Oh wow, you're so fucking hot"), v6_reply4)

    " "

    label phoneaf:
        if amber.messenger.replies:
            call screen phone
        if amber.messenger.replies:
            u "(I should probably reply to my messages.)"
            jump phoneaf

    u "(Amber is so fucking hot, I hope she sends more pictures like that in the future.)"

label continuebd:
    scene s483 # FIRST PERSON: Looking at your bed
    with fade

    u "(I should probably go to bed now, I got class at 9 am tomorrow.)"
    stop music fadeout 3
    scene s484 # MC NO LONGER HAS BLACK EYE  in bed
    with Fade (1,0,1)
    play music "music/m15punk.mp3"
    pause 0.5

    scene s484a # mc yawns
    with dissolve

    u "*Yawns*"

    scene s484
    with dissolve

    u "(Time for another boring-ass economics lecture...)"

    scene s485 # you come into econimics class room # but you cant really see the peopkle sitting in there yet
    with Fade (1,0,1)

    if (laurentoofar or toldlauren) and not apologize:
        $ lauren.relationship = Relationship.MAD

    pause 0.5

    if lauren.relationship >= Relationship.GIRLFRIEND:
        scene s486 #You stnad in between  riley and Lauren sitting in the back, seat in between them is emmpty, seat next to Lauren's right is also empty ALWAYS SHOW CLASSROOM STUFF FROM THE FRONT if it's last row so you don't have to show 50 students sitting but instead jsut the back wall
        with dissolve

        u "Hey guys."

        if laurenpublic:
            scene s486a # Lauren talking smiling
            with dissolve

            la "Heyyy."

            scene s486b # You bend down, you and Lauren kiss
            with dissolve

            play sound "sounds/kiss.mp3"

            pause 1.5

            scene s486d # You sit down
            with dissolve

            pause 0.5

            scene s487 # CLOSEUP Riley surprised, smile
            with dissolve

            ri "Are you two dating?"

            scene s487e # CLOSEUP Lauren shy smile
            with dissolve

            la "I don't know. Maybe... yes."

            scene s487b # Riley slightly embarrassed
            with dissolve

            ri "Wow, I really had no idea."

            scene s490
            with dissolve

            ro "Alright class, let's get started. Open your books to page 225."

            stop music fadeout 3
            scene clocka
            with fade

            play sound "sounds/clock2.mp3"

            pause (0.5)

            scene clockb
            with dissolve

            pause (0.5)

            scene clockc
            with dissolve

            pause (0.5)

            scene clockd
            with dissolve

            pause (0.5)
            stop sound
            scene clocke
            with dissolve

            pause 0.5

            scene s491 # (Showing you and Lauren standing at your desks after classs) Lauren kisses you goodbye
            with fade

            play sound "sounds/kiss.mp3"

            pause 1.5

            scene s491a # Lauren looking at you
            with dissolve

            la "I gotta go, I have to finish a paper. I'll see you later."

            scene s491b
            with dissolve

            u "Alright, bye."

            scene s492 # CLOSEUP: Riley standing, slightly jealous but also intrigued
            with dissolve

            ri "So, you and Lauren, huh?"

            scene s492a
            with dissolve

            u "Oh, yeah... me and Lauren."

            scene s492
            with dissolve

            ri "I uhm... I'm happy for you guys."

            scene s492a
            with dissolve

            u "Thanks."

        else:

            scene s486a # Lauren talking smiling
            with dissolve

            la "Heyyy."

            scene s486c # Lauren slightly touches your hand, smiling at you
            with dissolve

            pause 0.5

            scene s486d
            with dissolve

            pause 0.5

            scene s490
            with dissolve

            ro "Alright class, let's get started. Open your books to page 225."

            stop music fadeout 3
            scene clocka
            with fade

            play sound "sounds/clock2.mp3"

            pause (0.5)

            scene clockb
            with dissolve

            pause (0.5)

            scene clockc
            with dissolve

            pause (0.5)

            scene clockd
            with dissolve

            pause (0.5)
            stop sound
            scene clocke
            with dissolve

            pause 0.5

            scene s491a
            with fade

            la "I gotta go, I have to finish a paper. I'll see you later."

            scene s491b
            with dissolve

            u "Alright, bye."

            scene s492b # CLOSEUP: Riley standing, teasing you
            with dissolve

            ri "You and Lauren seem to have been getting along quite well today."

            scene s492a
            with dissolve

            u "*Grins* Whatever."

    elif lauren.relationship <= Relationship.MAD:
            scene s486e # you standing next to riley who's alone in the backrow, lauren's sitting somewhere else
            with dissolve

            pause 0.5

            scene s486f # you sit down looking at Riley.
            with dissolve

            u "Hey."

            scene s487d # CLOSEUP: Riley curious
            with dissolve

            ri "Hey."

            scene s489 # showing Lauren sitting by herself on the otherside of the room
            with dissolve

            ri "Is she mad at you or something?"

            scene s487e
            with dissolve

            u "I don't know. Maybe."

            scene s487d
            with dissolve

            ri "What for?"

            scene s487e
            with dissolve

            u "It doesn't matter."

            scene s487f # Riley looking back at her desk mouth distrusting
            with dissolve

            ri "Mhmmm..."

            u "Where's Ryan?"

            scene s487g # Riley looking at you a bit distrusting and empty, she doesn't lift her head up fully, just as much as she has to
            with dissolve

            ri "I don't know."

            scene s490
            with dissolve

            ro "Alright class, let's get started. Open your books to page 225."

            stop music fadeout 3
            scene clocka
            with fade

            play sound "sounds/clock2.mp3"

            pause (0.5)

            scene clockb
            with dissolve

            pause (0.5)

            scene clockc
            with dissolve

            pause (0.5)

            scene clockd
            with dissolve

            pause (0.5)
            stop sound
            scene clocke
            with dissolve

            pause 0.5

            scene s493 # FIRST PERSON: Lauren standing up (she's sitting on the other side of class) SHOW the entire wall of the class till the door
            with fade

            pause 0.5

            scene s493a # Lauren walking quickly out of class
            with dissolve

            u "(Maybe I should talk to her, doesn't seem like she's forgiven me.)"

            menu:
                "Call after her":
                    $ add_point(KCT.BRO)

                    scene s493b # Lauren at door
                    with dissolve

                    u "Lauren! ... Lauren!"

                    scene s493c # Lauren gone
                    with dissolve

                    u "Damn it."

                "Leave her be":
                    $ add_point(KCT.BOYFRIEND)

                    scene s493b
                    with dissolve

                    u "(No, she just needs some more time.)"

                    scene s493c
                    with dissolve

                    u "*Sighs*"

            scene s492h # Riley emphatic
            with dissolve

            ri "You good?"

            scene s492j
            with dissolve

            u "Yeah, I'm fine."

            scene s492h
            with dissolve

            ri "Okay, just making sure."

    else:
        scene s486 #You stnad in between  riley and Lauren sitting in the back, seat in between them is emmpty, seat next to Lauren's right is also empty
        with dissolve

        u "Hey guys."

        scene s486a # Lauren talking smiling
        with dissolve

        la "Heyyy."

        scene s486d # You sit down
        with dissolve

        u "Where's Ryan?"

        scene s487 # CLOSEUP Riley surprised, smile
        with dissolve

        ri "I don't know, but he said he's already falling behind on the classwork, so I don't think him skipping class is a good idea."

        scene s490
        with dissolve

        ro "Alright class, let's get started. Open your books to page 225."

        stop music fadeout 3
        scene clocka
        with fade

        play sound "sounds/clock2.mp3"

        pause (0.5)

        scene clockb
        with dissolve

        pause (0.5)

        scene clockc
        with dissolve

        pause (0.5)

        scene clockd
        with dissolve

        pause (0.5)
        stop sound
        scene clocke
        with dissolve

        pause 0.5

        scene s491a # Lauren looking at you
        with fade

        la "I gotta go, I have to finish a paper. I'll see you guys later."

        scene s491b
        with dissolve

        u "Alright, bye."

        scene s492d # CLOSEUP: Riley standing, curious
        with dissolve

        ri "So, how are things with Chloe?"

        if chloe.relationship <= Relationship.MAD:
            scene s492e
            with dissolve

            u "Uhm, could be better."

            scene s492h # Riley emphatic
            with dissolve

            ri "Oh no, what happened?"

            scene s492j
            with dissolve

            u "I don't really wanna get into it."

            scene s492h
            with dissolve

            ri "Okay..."

        else:
            scene s492e
            with dissolve

            u "Yeah uhm, good."

            scene s492f # riley smiling
            with dissolve

            ri "I'm glad. You deserve to be happy."

            scene s492g
            with dissolve

            u "Thanks, Riley."

    play music "music/m4punk.mp3"

    queue music [ "music/m9punk.mp3"]

    label afterclass: #for compatibility only
    scene s494 # showing your and rileys backs leaving the classroom
    with dissolve

    pause 0.5

    scene s495 # FIRST PERSON: Ryan approaches you in a hurry.
    with dissolve

    ry "[name], I need to talk to you. Now."

    scene s495a # Ryan now standing still mouth closed
    with dissolve

    u "Hey, what's the hurry?"

    scene s496 # First Person: Riley from the side talking to Ryan
    with dissolve

    ri "You just missed class, you know that?"

    scene s495b # same as 495a but ryan mouth open
    with dissolve

    ry "It's urgent."

    scene s495a
    with dissolve

    u "Alright, well I wanted to talk to you anyways."

    scene s495b
    with dissolve

    ry "Just follow me."

    scene s496a # Riley looking at you worried and confused
    with dissolve

    u "I'll see you later, Riley."

    scene s496b # Riley same as 496a but mouth open
    with dissolve

    ri "Okay, see you."

    scene s497 # you following Ryan to a room
    with fade

    pause 0.5

    scene s498 #FIRST PERSON:  Ryan opens a door, perspective so you can't look inside much
    with dissolve

    play sound "sounds/dooropen.mp3"

    ry "In here."

    scene s499 #FIRST PERSON: Graysons inside the small, dark room ,sitting on a chair,
    with dissolve

    play sound "sounds/doorclose.mp3"

    u "What the fuck is this?!"

    scene s500 # Close Up: Ryan standing behind you next to the now closed door mouth closed
    with dissolve

    u "Ryan?!"

    scene s501 #Close up: Grayson seriou
    with dissolve

    gr "Listen, [name]... I think we started off on the wrong foot."

    scene s501a
    with dissolve

    u "The wrong foot?! Are you kidding me?!"

    scene s501
    with dissolve

    gr "Look, I hit you, it was an accident. I was drunk... these things happen, you know?"

    scene s501a
    with dissolve

    u "No, I don't know."

    scene s500a # Ryan a bit worried, urging
    with dissolve

    ry "Just hear him out."

    scene s501b # Grayson caring serious
    with dissolve

    gr "Believe me, I'm truly sorry about how everything turned out."

    scene s501c
    with dissolve

    u "You did it 'cause I got too close to Chloe, right?"

    scene s501b
    with dissolve

    gr "You know what I think it was? I think I saw a younger me in you and I got scared."

    scene s501d # Grayson convincing, maybe stands up a bit to lean on table
    with dissolve

    gr "You see, me and you, we're a lot alike. We're charismatic, we're confident, we take what we want."

    gr "Natural born leaders."

    menu:
        "What do you want?":
            $ add_point(KCT.BRO)

            scene s501e
            with dissolve

            u "What do you want, Grayson?"

            scene s501d
            with dissolve

            gr "Join the Apes."

        "I guess we are":
            $ add_point(KCT.TROUBLEMAKER)

            scene s501e
            with dissolve

            u "I guess we are somewhat alike..."

            scene s501d
            with dissolve

            gr "So forget the Wolves, join the Apes."

    label ft_ad: #for compatibility only
    gr "You got what it takes, the personality, the pull... and I'll teach you fighting myself."

    scene s501e
    with dissolve

    u "Look, this is all really flattering, but... I don't think-"

    scene s500a
    with dissolve

    ry "Bro, Grayson doesn't train anyone himself. You don't understand how good of an opportunity this is!"

    scene s502 # Grayson walking past you, looking at you
    with dissolve

    gr "Have a think about it and then meet me at midnight on the front stairs."

    scene s503  # Grayson and Ryan exiting room, Ryan looks back at you
    with dissolve

    ry "Don't waste this chance, man."

    stop music fadeout 3
    scene s503a # Grayson and Ryan gone.
    with dissolve

    u "(What the fuck just happened?)"

    scene s504 # Mc walking through school corridors (economics classroom is close, door is open)
    with fade

    pause 0.5
    play music "music/mindie1.mp3"

    queue music [ "music/mindie2.mp3", "music/mindie3.mp3" ]

    scene s504a # Mc walking past open classroom door
    with dissolve

    ro "*Sniffs* Damnit!"

    scene s504b # Mc turns head towards classroom
    with dissolve

    u "(Is that Ms. Rose crying?)"

    menu:
        "Check it out":
            $ add_point(KCT.BOYFRIEND)
            $ checkonrose = True

            scene s505 # First Person: Enter classrom, only Ms Rose at her laptop crying
            with dissolve

            u "Ms. Rose?"

            scene s506 # CLOSE UP: Ms Rose looking away, wiping her tears off
            with dissolve

            ro "Y- *sniffles* Yes?"

            scene s506c # Rose closed mouth sad, unsure, mouth closed
            with dissolve

            u "Are you okay? What happened?"

            scene s506b # same as 506c but mouth open
            with dissolve

            ro "I don't want to talk about it."

            scene s506c
            with dissolve

            u "Are you sure? Maybe I can help."

            scene s506d # ms rose angry
            with dissolve

            ro "I'm sure! You can't help me! No one can!"

            scene s506f #ms rose breaks down. maybe looks down, leans on the desk or something
            with dissolve

            u "I'm sorry-"

            scene s506g #  # ms rose looks up
            with dissolve

            ro "Just leave me alone! Go!"

            scene s507 # mc about to walk away looking at rose
            with dissolve

            u "Okay. Okay. Apologies. I'll leave you alone."

            scene s507a # Mc walking away, rose looks at his back sad
            with dissolve

            ro "Wait."

            scene s508 #CLose up: Rose apologenic
            with dissolve

            ro "I'm sorry. I didn't mean to snap at you. I just have a lot going on right now."

            scene s508a
            with dissolve

            u "It's okay. I get it. I don't wanna pry."

            scene s508b # rose sad smile
            with dissolve

            ro "Thanks, really. I appreciate it."

            scene s508c
            with dissolve

            u "I'm here if you need me."

            pause 1.0

            scene s509 # Mc walking out of classroom you cant see ms rose from this angle, mc is perplexed
            with dissolve

            pause 0.5

            scene s510 # Mc arrives at his dorm, down at his door there's a flyer (Matt's design)
            with fade

        "Don't disturb":
            $ add_point(KCT.TROUBLEMAKER)

            scene s510 # Mc arrives at his dorm, down at his door there's a flyer (Matt's design)
            with fade

            $ grant_achievement("not_my_business")

    label nr_bb: #for compatibility only
    u "(Huh, what's this?)"

    show flyer

    if lauren.relationship >= Relationship.GIRLFRIEND:
        u "(Homecoming. Hm. Lauren would probably be pissed if I didn't ask her...)"

    else:
        u "(Homecoming. Hm. I should really think about who I want to go with...)"

    scene s511 # Mc throwing flyer on his desk
    with dissolve

    pause 0.5

    if imre.relationship <= Relationship.MAD and not imreforgives:
        scene s512 # mc lays back on bed
        with dissolve

        u "(I wanna text Imre, but he's probably still mad...)"

        scene s514 # Looking at Imre's empty bed
        with dissolve

        u "(Why did he move out?)"

        scene s515 # Mc sits up on the side of his , desperate
        with dissolve

        u "(I just don't get it.)"

        u "(And what the fuck am I gonna do about Grayson?)"

    else:
        scene s515
        with dissolve

        u "(What the fuck am I gonna do about Grayson?)"

    scene s515a # mc looks at windowdetermined
    with dissolve

    label continuebe: #for compatibility only
    u "(Fuck this, maybe going for a run will help me clear my mind)"

    scene s516 # Mc running in ruunning chlothes not at park
    with fade

    pause 1.0

    scene s517 # Running somewhere else not park
    with Dissolve (1)

    pause 1.0

    scene s518 # Seeing Nora running: she has in ear headphones not at park
    with Dissolve (1)

    u "(Hey, that's Nora.)"

    menu:
        "Run after her":
            scene s519 # you running after nora
            with dissolve

            u "*Heavy breathing* Nora!"

            scene s519a # you closer to Nora, she turns around
            with dissolve

            u "*Out of breath* Hey, Nora!"

            scene s520 #CLOSE UP: Nora, turned around  pulled out on of her ear buds, confused and slightly annoyed
            with dissolve

            no "Uhm, hey."

            scene s520a
            with dissolve

            u "I just saw you from the distance so I thought I might as well say hi."

            scene s520
            with dissolve

            no "Right."

            scene s520a
            with dissolve

            u "So uhm... do you run a lot?"

            scene s520b # nora thinking, suspicious
            with dissolve

            no "Yeah, almost everyday."

            scene s520c
            with dissolve

            u "Oh, cool."

            scene s520e # nora slight smile nod and confused mouth closed
            with dissolve

            " "

            u "I wanna start running more too, it really helps me clear my thoughts."

            scene s520g # smiling a bit
            with dissolve

            no "I don't even remember an age where I didn't run. It's just such a good stress relief."

            scene s520h
            with dissolve

            u "Haha, it really is."

            u "So, are you going to the Wolves' rush party tomorrow?"

            scene s520g
            with dissolve

            no "Yeah, I think Chris would kill me if I didn't."

            no "What about you?"

            scene s520h
            with dissolve

            u "Uhm, yeah. I think so."

            scene s520e
            with dissolve

            " "

            scene s520b
            with dissolve

            no "So... was that all you needed?"

            scene s520c
            with dissolve

            u "Uhh, yeah."

            scene s520b
            with dissolve

            no "Alright, I'll probably see you tomorrow then."

            scene s520c
            with dissolve

            u "Yeah, cool. I'll see you then."

            scene s521  # First person: Looking at Nora's ass running away
            with dissolve

            u "(Damn...)"

        "Stay on your route":
            pass

    scene s522 # you running into the park
    with fade

    pause 1.0

    label fu_b: #for compatibility only
    scene s523 # you stretching in the park
    with dissolve

    if evelynnumber:
        u "(I should call Evelyn about doing the date tonight. After all, she did say she'd give me a chance.)"

        scene s524 # you on the phone
        with dissolve
        play sound "sounds/calling.mp3"

        pause 0.5
        stop sound

        ev "Hello?"

        scene s524a # mc thoughtful
        with dissolve

        u "Hey Evelyn, it's me, [name]."

        scene s524b # mc confused that she isn't saying anything
        with dissolve

        pause 0.5

        scene s524a
        with dissolve

        u "Uhh.. you know, the really cute guy you wanted to go on a date with."

        scene s524
        with dissolve

        ev "I know who you are."

        scene s524a
        with dissolve

        u "So uhm, how about we do the date tonight?"

        scene s524
        with dissolve

        ev "Look, you gave a fair fight and I think it's great that you're as direct as you were with me."

        ev "But you're really not my type.  Plus I'm meeting friends tonight."

        scene s524e # Mc thinking on his feet
        with dissolve

        u "I know you like playing hard to get, but I think you'd make a big mistake by missing out on this date."

        scene s524d # same as e but mouth closed
        with dissolve

        ev "How so?"

        menu:
            "It'll be an adventure":
                $ add_point(KCT.BRO)

                scene s524e
                with dissolve

                u "'Cause we'll go on an adventure."

                scene s524d
                with dissolve

                ev "An adventure?"

                scene s524e
                with dissolve

                u "Yeah, it will be fun."

                scene s524d
                with dissolve

                ev "To where?"

                scene s524e
                with dissolve

                u "It will be a surprise."

                scene s524d
                with dissolve

                ev "That sounds uhm... a bit childish. Sorry I gotta go."

                ev "I'm sure you'll find someone else, good bye."

                play sound "sounds/rejectcall.mp3"

                "*Evelyn hangs up*"

                scene s524f # mc puts the phone down dissapointed
                with dissolve

                u "Damnit."

            "It'll be a nice dinner":
                $ add_point(KCT.BOYFRIEND)
                $ evelyn.relationship = Relationship.DATE

                scene s524e
                with dissolve

                u "Because we'll go out to a nice dinner. It'll be much more enjoyable than a girls' night and the best part: it's on me."

                scene s524d
                with dissolve

                ev "Hmmm... that does sound enticing. Where would we be going?"

                scene s524e
                with dissolve

                u "That's a surprise."

                scene s524d
                with dissolve

                ev "Okay, I can do with surprises. Pick me up at eight?"

                scene s524h # McEmbarrased
                with dissolve

                u "Yeah... there's one more issue, I don't really have a car-"

                scene s524g # same as h but mouth closed
                with dissolve

                ev "Of course you don't."

                scene s524h
                with dissolve

                u "How about I tell you the address, but you're not allowed to look up which restaurant it is and we'll meet there?"

                scene s524g
                with dissolve

                ev "*Sighs* Fine."

                scene s524h
                with dissolve

                u "376 Gardner Avenue. I'll see you at eight."

                scene s524g
                with dissolve

                ev "Yes..."

                play sound "sounds/rejectcall.mp3"

                "*Evelyn hangs up*"

                scene s524f2 # mc puts the phone down happy, celebrating
                with dissolve

                u "Hell yeah."

    else:
        pause 0.5

    label lookdog: #for compatibility only
    if trolleyb:
        scene s525 # Looking at guy petting his dog
        with dissolve

        pause 1.0

        play sound "sounds/swoosh.mp3"

        show screen fantasyOverlay

        scene s387a # even closer, dog on the left side
        with flash

        pause 0.5
        play sound "sounds/swoosh.mp3"
        scene s388e #you press lever
        with flash
        play sound "sounds/lever.mp3"

        pause 0.5

        play sound "sounds/splat.mp3"

        scene s390a # your face full of blood
        with vpunch

        pause 1.0

        hide screen fantasyOverlay
        play sound "sounds/swoosh.mp3"
        scene s525
        with flash

        u "*Breathing heavily*"

    label runback: #for compatibility only
    play music "music/mindie5.mp3"

    scene s526 # you running back to your dorm
    with fade

    pause 1.0

    scene s527 # you entering your dorm in running clothes
    with fade

    pause 0.5

    scene s528 # you in running clothes sititng on your bed looking at the window
    with dissolve

    pause 0.5

    if volleyball:
        scene s529 # showing blue volleyball on your desk
        with dissolve

        if chloe.relationship <= Relationship.MAD:
            u "(I really need to patch things up with Chloe. It was going so great until-)"

            u "(Until I messed things up.)"

            u "(I should've just trusted her.)"

            scene s529
            with dissolve

            pause 0.5

        else:
            u "(Wow, I still haven't given that to Chloe. Next time I'm definitely taking it with me.)"

            scene s529
            with dissolve

            pause 0.5

    label continuebf: #for compatibility only
    label fw_a: #for compatibility only
    stop music fadeout 3

    play sound "sounds/call.mp3"

    u "(Huh?)"

    scene s530  # FIrst person: Looking at phone: Emily callingL
    with dissolve

    play music "music/m16punk.mp3"

    menu:
        "Accept call":
            stop sound
            play sound "sounds/answercall.mp3"
            $ add_point(KCT.BOYFRIEND)

            # aceept call sound
            if not forgiveemily:
                scene s531 # mc holding his phone to his ear, mouth open, annoyed, slightly mad
                with dissolve

                u "What's wrong now?"

                scene s531a
                with dissolve

                em "(Sobbing) Really? That's how you're going to treat me?"

                scene s531
                with dissolve

                u "Alright fine. What's wrong, Emily?"

                scene s531a
                with dissolve

                em "(Sobbing) Can you please come over? I need you."

                scene s531
                with dissolve

                u "For what? We already went over this..."

                scene s531a
                with dissolve

                em "*Sniff* I just really need someone to talk to."

                scene s531
                with dissolve

                u "Right... like that time you told me you needed me and then opened the door in your underwear trying to get me back???"

                scene s531a
                with dissolve

                em "[name], this is different. I promise. Please can you just come over? I'm in Dorm 17, Block A."

                menu:
                    "Fine, I'll come":
                        $ add_point(KCT.BOYFRIEND)

                        scene s531b # mc empathy
                        with dissolve

                        u "Fine, I'll come."

                        scene s531c
                        with dissolve

                        em "Thank you!"

                        scene s531d # mc looks at phone, away from ear
                        with dissolve

                        play sound "sounds/rejectcall.mp3"

                        "*You hang up*"

                        u "*Sighs*"

                        scene s532 # in front of Emily's dorm knocking
                        with fade

                        "*Knock knock knock*"

                        u "Emily?"

                        scene s532a # no longer knocking
                        with dissolve

                        em "*Sniff* Door's open..."

                        scene s533 # First person: Emily sad on her bed with her phone in her hand looking down
                        with dissolve

                        u "So?"

                        em "*Sniff*"

                        u "Are you going to tell me what's wrong or not?!"

                        scene s534 # Close up: Emily looking at you sad
                        with dissolve

                        em "It's Hazel.."

                        scene s534a
                        with dissolve

                        u "As in your best friend from high school Hazel?"

                        scene s534
                        with dissolve

                        em "Yes."

                        scene s534a
                        with dissolve

                        u "What'd she do?"

                        scene s534b # Emily holds her phone up with a picture of Hazel with another girl and Emily's arm around her but Emily is cropped out)
                        with dissolve

                        u "She posted a picture?"

                        scene s534c # Emily points at where she was cropped out
                        with dissolve

                        em "Look!"

                        scene s535 # zoomed in look of the picture
                        with dissolve

                        em "She cut me out!"

                        menu:
                            "Be understanding":
                                $ add_point(KCT.BOYFRIEND)

                                jump fz_a

                            "Be baffled":
                                $ add_point(KCT.TROUBLEMAKER)

                                jump fz_b

                    "No. (Hang up)":
                        $ add_point(KCT.TROUBLEMAKER)

                        scene s531
                        with dissolve

                        u "No."

                        scene s531d # mc looks at phone, away from ear
                        with dissolve

                        play sound "sounds/rejectcall.mp3"

                        "*You hang up*"

                        u "*Sighs*"

                        jump fy_bd

            else:
                scene s531b
                with dissolve

                u "Hey Emily, what's up?"

                scene s531c
                with dissolve

                em "(Sobbing) Can you please come over? I need you."

                scene s531b
                with dissolve

                u "Uhm, yeah of course, what's wrong?"

                scene s531c
                with dissolve

                em "*Sniff* I just really need someone to talk to. I'm in Dorm 17, Block A."

                scene s531b
                with dissolve

                u "Okay, I'm on my way."

                scene s531d # mc looks at phone, away from ear
                with dissolve

                play sound "sounds/rejectcall.mp3"

                "*You hang up*"

                scene s532
                with fade

                play sound "sounds/knock.mp3"

                "*Knock knock knock*"

                u "Emily?"

                scene s532a
                with dissolve

                em "*Sniff* Door's open..."

                scene s533 # First person: Emily sad on her bed with her phone in her hand looking down
                with dissolve

                u "Hey, what's wrong?"

                scene s534 # Close up: Emily looking at you sad
                with dissolve

                em "*Sniff* It's Hazel.."

                scene s534a
                with dissolve

                u "As in your best friend from college Hazel?"

                scene s534
                with dissolve

                em "Yes."

                scene s534a
                with dissolve

                u "What'd she do?"

                scene s534b # Emily holds her phone up with a picture of Hazel with another girl and Emily's arm around her but Emily is cropped out)
                with dissolve

                u "She posted a picture?"

                scene s534c # Emily points at where she was cropped out
                with dissolve

                em "Look!"

                scene s535 # zoomed in look of the picture
                with dissolve

                em "She cut me out!"

                menu:
                    "Be understanding":
                        $ forgiveemily = True
                        $ add_point(KCT.BOYFRIEND)

                        jump fz_a

                    "Be baffled":
                        $ forgiveemily = False
                        $ add_point(KCT.TROUBLEMAKER)

                        jump fz_b


        "Reject call":
            stop sound
            play sound "sounds/rejectcall.mp3"
            $ add_point(KCT.TROUBLEMAKER)

            scene s531d
            with dissolve

            play sound "sounds/rejectcall.mp3"

            pause 0.5

            jump fy_bd

label fz_a:
    scene s536 # Mc sits down next to Emily and puts his hand on her thigh
    with dissolve

    u "Hey, it's okay."

    scene s537 # CLose up Emily upset:
    with dissolve

    em "No it's not! I just don't understand why she would do that! She didn't even ask me..."

    scene s537a
    with dissolve

    u "Have you asked her?"

    scene s537
    with dissolve

    em "No, of course not. I don't wanna talk to her after what she did."

    scene s537a
    with dissolve

    u "You ever think maybe it wasn't a very good picture of you? So she wouldn't want to post it, if you didn't look good in it."

    scene s537b  # em sad smile, joking, cheer up
    with dissolve

    em "What, you're saying I'm ugly?"

    scene s537c
    with dissolve

    u "*Chuckles* I guess I walked right into that one."

    u "Even though you're cute crying, I still prefer when you're smiling."

    scene s537b
    with dissolve

    em "*Chuckles* Me too."

    scene s537d # Emily comes a bit closer, reminiscing, cute
    with dissolve

    em "Remember when we snuck into the movies 'cause you forgot your ID?"

    scene s537e
    with dissolve

    u "Yeah and we got caught 'cause you couldn't keep your cool."

    scene s537d
    with dissolve

    em "*Laughs* That's still my favorite date to this day."

    scene s537e
    with dissolve

    u "Yeah... it was uhm... good."

    scene em4
    with dissolve

    pause 0.5

    scene em4a
    with dissolve

    menu:
        "Kiss her back":
            $ emily.relationship = Relationship.FWB
            $ forgiveemily = True

            jump emsex_a

        "Push her away":
            $ forgiveemily = False

            scene em4b
            with dissolve

            u "Emily! What are you doing?!"

            scene s537
            with dissolve

            em "I'm sorry, it's just..."

            em "When I see you, I- I just wanna kiss you."

            scene s537a
            with dissolve

            u "Maybe we shouldn't see each other then."

            scene s537
            with dissolve

            em "[name], please..."

            scene s537a
            with dissolve

            u "I gotta go. I'll see you around."

            u "Or... not."

            jump afteremily

label fz_b:
    scene s534
    with dissolve

    u "Are you fucking kidding me?! This is why you're calling me??? Over something stupid like this?"

    scene s538s # Emily stands up angry
    with dissolve

    em "God, you have no empathy at all, do you?!"

    scene s538s # Emily stands up angry
    with dissolve

    em "You never fucking cared! All my problems are ridiculous to you, like my feelings don't matter!"

    scene s538a
    with dissolve

    u "No fucking wonder, you get upset over stupid shit like this!"

    u "You make every little thing about yourself, 'cause that's all you care about! Grow the fuck up. No one gives a shit."

    scene s538b #Emily Sad Angry really upset
    with dissolve

    em "How can you even say that? After everything I did for you?!"
    em "Every day I was there for you. I listened. I was the one who found your therapist. I did everything for you."
    em "So don't you dare tell me I only care about myself!"

    scene s538c
    with dissolve

    u "You cheated on me!"

    scene s538b
    with dissolve

    em "I slipped up, okay?!"

    em "And I'm really sorry. But you have to admit it wasn't going well."

    scene s538d # Emily coming closer, sad curious
    with dissolve

    em "I mean, did you even love me anymore?"

    scene s538e
    with dissolve

    u "Of course I did."

    scene s538f # Emily looking at you with big expectations and cute and head tilted
    with dissolve

    u "I..."

    scene em1
    with dissolve

    pause 0.5

    scene em1a
    with dissolve

    menu:
        "Kiss her back":
            $ emily.relationship = Relationship.FWB
            $ forgiveemily = True

            jump emsex_c

        "Push her away":
            $ forgiveemily = False

            scene em1b
            with dissolve

            u "Emily! What are you doing?!"

            scene s538d
            with dissolve

            em "I'm sorry, it's just..."

            em "When I see you, I- I just wanna kiss you."

            scene s538e
            with dissolve

            u "Maybe we shouldn't see each other then."

            scene s538d
            with dissolve

            em "[name], please..."

            scene s538e
            with dissolve

            u "I gotta go. I'll see you around."

            u "Or... not."

            jump afteremily

    #### SEX SCENE EMILY
label emsex_c:
    play music "music/msexy.mp3"

    scene emvid1
    with dissolve

    $ grant_achievement("reignition")

    " "

    scene em2
    with dissolve

    u "Wow..."

    scene em3
    with dissolve

    em "Come here."

    scene em3a
    with dissolve

    em "*Chuckles*"

    scene em3b
    with dissolve

    pause 0.5

label emsex_a:
    $ sceneList.add("v6_emily")

    scene emvid2
    with dissolve

    play music "music/msexy.mp3"

    $ grant_achievement("reignition")
    
    " "

    scene em5
    with dissolve

    pause 0.5

    if config_censored:
        call screen censoredPopup("v6_nsfwSkipLabel1")

    scene em6
    with dissolve

    em "Fuck... get down there."

    scene em7
    with dissolve

    em "I haven't been eaten out in so long..."

    scene em7a
    with dissolve

    em "*Quiet moan* Mhhh..."

    show screen emilysexoverlay

label emhead:
    scene emvid3
    with dissolve

    em "*Moans* Ahhh..."

    em "*Moans louder* Oh baby..."

    em "*Moans even louder* Fuuuuck."

    " "

    em "Oh my god, I'm gonna cum."

    em "You're so fucking good at this..."

    scene em8
    with dissolve

    u "Nah, first it's my turn."

    scene em9
    with dissolve

    em "Mhhh..."

    scene em9a
    with dissolve

    em "You look so good."

    scene em10
    with dissolve

    u "Take your shirt off."

    scene em10a
    with dissolve

    pause 0.5

    scene em11
    with dissolve

    u "You're gonna suck some dick now."

    scene em12
    with dissolve

    em "Yesss... treat me like your dirty little slut."

    label emfacefuck:

    scene emvid4
    with dissolve

    u "Take this fucking dick."

    em "*Gag sounds*"

    u "Fuck..."

    em "*Gag sounds*"

    " "

    scene em13
    with dissolve

    em "*Breathing heavily* Just fuck me, please!"

    scene em14
    with dissolve

    u "You wanna be fucked you little slut?"

    scene em14a
    with dissolve

    em "I'm so fucking wet."

    em "Fuck me, [name]!"

    scene em15
    with dissolve

    pause 0.5

    scene em15a
    with vpunch

    em "*Moans* Ahhh..."

    label embehind:

    scene emvid6
    with dissolve

    em "*Moans* Oh my god!"

    em "*Moans louder* Yes! Fuck me!"

    em "*Moans* Yes! [name]!"

    em "*Moans* Ahhh! Don't stop!"

    " "

    scene em16
    with dissolve

    u "Fucking turn around."

    scene em16a
    with dissolve

    em "*Breathing heavily* Mhhh..."

    label embutterfly:

    scene emvid7
    with dissolve

    em "*Moans* Baby... yes!"

    em "*Moans louder* Ahhh!"

    " "
    scene emvid8
    with dissolve

    em "*Moans even louder* Oh my god! I'm gonna cum!"

    " "

    u "Fuuuck!"

    em "Cum inside me! Please! Fill me up!"

    label emclimax:

    scene emvid9
    with dissolve

    stop music fadeout 3

    em "*Really loud moan* Ahhhhh!"

    hide screen emilysexoverlay
    $ renpy.end_replay()

    play music "music/m7punk.mp3"

    scene em17
    with fade

    u "That was so good."

    scene em18
    with dissolve

    em "Just like the old times."

    scene em18a
    with dissolve

    u "You are on the pill right?"

    scene em18
    with dissolve

    em "*Laughs* Yeah, don't worry."

    scene em18a
    with dissolve

    u "Phew..."

    u "I still need to finish some of my assignments, so I kinda gotta go now."

label v6_nsfwSkipLabel1:
    scene em18b
    with dissolve

    em "Already?"

    scene em18c
    with dissolve

    u "Sorry, Emily. I don't wanna fall behind this early into the semester."

    scene em18b
    with dissolve

    em "Are you at least gonna be at the party later?"

    scene em18c
    with dissolve

    u "You're going to the Wolves' rush party too?"

    scene em18b
    with dissolve

    em "Yeah, Nora invited me."

    scene em18c
    with dissolve

    u "Oh, awesome. I'll see you tonight then."

    scene em18b
    with dissolve

    em "Still would've rather you stayed now..."

    scene em18c
    with dissolve

    u "Emily, you know I can't. I'll see you later."

    scene em18b
    with dissolve

    em "Okay..."

    jump afteremily

    ##################

label afteremily: #After emily
    scene s539 # You walking back to your dorm
    with fade

    u "(What just happened...?)"

label fy_bd: # not gone to Emily's
    stop music fadeout 3
    scene s540 # you working on your desk
    with Fade (1,0,1)

    play music "music/mfunk.mp3"

    if imreforgives:
        $ imre.relationship = Relationship.FRIEND

    pause 1.0

    if imre.relationship <= Relationship.MAD:
        scene s540a # your head moves to look at your door
        with dissolve

        pause 0.5

        play sound "sounds/swoosh.mp3"

        scene s205a # old render, no need to do
        with flash

        pause 0.5
        play sound "sounds/swoosh.mp3"
        scene s541 # looking at door closed
        with flash

        pause 0.5

        scene s540a
        with dissolve

        pause 0.5

        scene s540
        with dissolve

        u "(I really hope Imre comes back at some point.)"

    else:
        play sound "sounds/dooropen.mp3"

        scene s540a
        with dissolve

        pause 0.5

        scene s541a # Imre coming inside
        with dissolve

        u "Hey, what's up?"

        scene s542 # Imre walking towards his desk, where his jacket is hanging, looking at you
        with dissolve

        imre "Not much, just back from class. What are you up to?"

        scene s542a # Imre walks fruther, mouth closed
        with dissolve

        u "Some boring-ass Econ assignment."

        scene s543 # Imre about to put the jacket on
        with dissolve

        imre "*Laughs* Yeah, assignments are the worst."

        scene s543a # Imre with jacket on about to walk back
        with dissolve

        imre "You up for another training session tomorrow morning?"

        scene s543b # Imre throwing air punches, whilst being in pain
        with dissolve

        imre "*Winces in pain*"

        scene s543c # Imre throwing air punches part 2
        with dissolve

        u "You're not allowed to train yet."

        scene s543d # Imre looking at you no longer throwing punches, excited
        with dissolve

        imre "Come on I'll just do some light stuff, it'll do me good. Plus I can teach you some new moves."

        imre "Pledging period is starting soon, so you wanna at least know the basics."

        scene s543e
        with dissolve

        u "Alright fine, let's go to the gym tomorrow then."

        scene s543d
        with dissolve

        imre "And then tomorrow night it's the Wolves' rush party, I can't fucking wait."

        scene s543e
        with dissolve

        u "Yeah, it's exciting."

        scene s544 # Imre walking to the door, turning around looking at you
        with dissolve

        imre "Alright, I'm gonna head out. Gotta buy more Ibuprofen for my ribs."

        scene s544a
        with dissolve

        u "Jesus... Enjoy."

    label continuebg: #for compatibility only
    scene s545 # you napping on your desk on top of your assignment, phone on the desk next to you
    with Fade (1,0,1)

    pause 1.0

    scene s545a # your head goes up slightly and you open your eyes a bit
    with dissolve

    u "(Hmmm...?)"

    scene s545b # you grab your phone (but it's still turned around on the table
    with dissolve

    pause 0.5

    if evelyn.relationship >= Relationship.DATE:
        play music "music/mlove1.mp3"

        queue music ["music/mlove2.mp3"]

        scene s546a # phone close up, it's 7:30
        with dissolve

        u "(Shit, it's almost eight. I gotta get ready for my date.)"

        scene s547 # you in front of restaurant
        with Fade (1,0,1)

        pause 0.5

        scene s548 # First person: you closer to restaurant spotting evelyn
        with dissolve

        u "(There she is.)"

        u "Evelyn, hey!"

        scene s549 # closer and Evelyn turns around
        with dissolve

        ev "Hello, [name]."

        scene s550a # Evelyn close up smiling but suspicious mouth closed
        with dissolve

        u "Wow, you look-"

        scene s550 # same as s550a but mouth open
        with dissolve

        ev "Let me guess, beautiful?"

        menu:
            "Hot":
                $ add_point(KCT.BRO)

                scene s550a
                with dissolve

                u "Actually, I was gonna say hot."

                scene s550b # evelyn annoyed laugh smile smirk
                with dissolve

                ev "*Smirks* Of course you were."

            "Stunning":
                $ add_point(KCT.BOYFRIEND)

                scene s550a
                with dissolve

                u "Actually, I was gonna say stunning."

                scene s550b # evelyn genuine smile, flattered
                with dissolve

                ev "Oh, well thank you."

        label gc_ad: #for compatibility only
        scene s550a
        with dissolve

        ev "Shall we go inside?"

        scene s550
        with dissolve

        u "After you, m'lady."

        scene s551 #Opening: Showing you and Evlyn sitting at a table inside the restaurant and a waiter standing there talking to you
        with fade

        waiter "Can I start you two off with something to drink?"

        scene s552a # Close up: Waiter mouth closed, polite
        with dissolve

        u "Uh, yeah, can I just get a beer?"

        scene s553a #Close up Evelyn: gives MC a look of disdain. mouth closed, you should not be able to see that wine glass on the table
        with dissolve

        pause 0.5

        scene s553 #same as 553a but mouth open
        with dissolve

        ev "A beer?"

        scene s553a
        with dissolve

        u "Yeah, why not?"

        scene s553b #Evelyn turns to the waiter.
        with dissolve

        ev "Could we get a bottle of red wine instead?"

        scene s553c
        with dissolve

        u "Oh yeah, red wine. That works."

        scene s552b # waiter looking at evelyn polite
        with dissolve

        waiter "Yes ma'am, a bottle of red wine. Excellent choice."

        scene s552d #The waiter walks away.
        with dissolve

        pause 0.5

        scene s553
        with dissolve

        ev "You know if you're going to wine and dine a lady, I suggest you really WINE and dine her."

        scene s553a
        with dissolve

        u "Sorry, I didn't know you liked wine."

        scene s553d # Evelyn rolls her eys
        with dissolve

        pause 0.5

        scene s553a
        with dissolve

        u "Soo... anything else new lately?"

        scene s553f # evelyn bored
        with dissolve

        ev "Not really."

        scene s553g
        with dissolve

        u "Been partying a lot?"

        scene s553f
        with dissolve

        ev "No, I'm actually quite busy with doing normal adult things."

        scene s553g
        with dissolve

        u "Oh, right."

        scene s554 # waiter is back with a bottle of wine
        with dissolve

        waiter "There you go, a bottle of La Grupa Malbec Syrah from the 2018 harvest. It's from Tupungato in Mendoza. Delicate spices, ripe plums and cherries are balanced by refreshing acidity."

        scene s555 # waiter pours wine into evelyns Glass
        with dissolve

        ev "Thank you."

        scene s555a # Waiter pours wine into your glass while Evelyn starts smelling hers
        with dissolve

        u "Thanks."

        scene s552
        with dissolve

        waiter "Are you both ready to order?"

        scene s552a
        with dissolve

        u "Yeah, I'll get the New York steak, medium rare."

        scene s553b
        with dissolve

        ev "And I'll have the eggplant parmesan."

        scene s552b
        with dissolve

        waiter "Very well."

        scene s552d #The waiter walks away.
        with dissolve

        pause 0.5

        scene s553j # eve slightly hopeful smile mouth closed and intruiged
        with dissolve

        menu:
            "Make a joke":
                $ add_point(KCT.BRO)

                u "So uhm, is this the only eggplant you're looking to eat tonight?"

                scene s553a
                with dissolve

                pause 0.5

                u "Wow, tough crowd.."

                scene s553k # Evelyn awkwardly pressing her lips together
                with dissolve

                pause 0.5

            "Say something smart":
                $ add_point(KCT.BOYFRIEND)

                u "So did you hear about the new discoveries they made on Mars recently?"

                scene s553h # sam as 553j but mouth oopen
                with dissolve

                ev "No, I haven't. What was it they discovered?"

                scene s553j
                with dissolve

                u "Oh.. uh.. I'm not sure."

                scene s553a
                with dissolve

                u "Water maybe? Just thought it would be a cool topic to discuss."

                scene s553
                with dissolve

                ev "Right."

        label gd_ad: #for compatibility only
        scene s553m # evelyn about to stand up
        with dissolve

        ev "Will you excuse me for a second?"

        scene s553n
        with dissolve

        u "Yeah, of course."

        scene s553o # evelyn gone
        with dissolve

        u "(Shit this isn't going well. It's super awkward and we're not clicking at all.)"

        u "(I gotta connect with her, but how?)"

        scene s556 # Waiter back with food leaning towards evelyns side
        with dissolve

        waiter "Eggplant parmesan for the lady."

        scene s556a # leaning towards your side
        with dissolve

        waiter "And the New York steak, medium rare, for the gentleman."

        scene s556c # waiter stands normally looking at you
        with dissolve

        u "Thank you."

        scene s556b
        with dissolve

        waiter "You're most welcome."

        scene s557 # Evelyn coming back from the bathroom
        with dissolve

        pause 0.5

        scene s558 # CLOSEUP Evelyn sat down looking down at her food
        with dissolve

        ev "This certainly looks delicious."

        scene s558b # evelyn looks up at you smiling
        with dissolve

        ev "Bon appetit."

        scene s558c
        with dissolve

        u "Uhm, yeah same."

        scene s558d # Evelyn fork in her mouth looking at you
        with dissolve

        u "(Time to turn this date around. I just gotta find a way to connect with her.)"

        scene s558e # Evelyn looking down at her plate trying to get food
        with dissolve

        menu:
            "Ask about her job":
                $ add_point(KCT.BRO)

                scene s558d
                with dissolve

                u "So, how's life as a store clerk?"

                scene s558f # Evelyn looking at you normal looking, slightly thoughtful
                with dissolve

                ev "You know that I'm more than a store clerk, right?"

                scene s558g
                with dissolve

                u "Uhm..."

                scene s558f
                with dissolve

                ev "I'm also assistant regional manager of the branch."

                ev "Well, assistant to the regional manager, but it's basically the same thing."

                scene s558g
                with dissolve

                u "Yeah, sounds uhm... important."

                scene s558d
                with dissolve

                u "(This date really isn't getting better.)"

            "Ask about her dreams":
                $ add_point(KCT.BOYFRIEND)
                $ evelyn.relationship = Relationship.LIKES

                scene s558d
                with dissolve

                u "So, what's your dream job? Say you could do anything."

                scene s558f
                with dissolve

                ev "Dream job? That's not how life works, [name]."

                ev "Working at the store pays well and it will offer great career opportunities in the future."

                scene s558d
                with dissolve

                u "Yeah but... forget about the money for second. You gotta do what you're passionate about, right?"

                scene s558g
                with dissolve

                u "So what are you passionate about? What do you really wanna do?"

                scene s558f
                with dissolve

                ev "Uhm..."

                scene s558h # Evelyn looking up left with an innocent smile like she's imagining
                with dissolve

                ev "I really wanna go into pediatrics."

                scene s558d
                with dissolve

                u "Oh cool, that's like some science stuff, right?"

                scene s558k # Evelyn smiling at you
                with dissolve

                ev "Actually, it's medical. But close."

                scene s558l
                with dissolve

                u "Even cooler. So what exactly would you be doing?"

                scene s558k
                with dissolve

                ev "Help children get and stay healthy."

                scene s558l
                with dissolve

                u "In, like, your own practice?"

                scene s558k
                with dissolve

                ev "I mean that would be the dream."

                scene s558l
                with dissolve

                u "Don't forget to chase it then."

                scene s558k
                with dissolve

                ev "You're pretty wise for someone so stupid, you know that?"

                scene s558l
                with dissolve

                u "It's a gift and a curse."

                ev "*Chuckles*"

        label ge_ad: #for compatibility only
        scene s559 # Showing you and Evelyn outside of the restaurant at night, on something in the back it says "after date inc. It's after your date and you know it, even if it feels like time passed by quickly all of the sudden
        with fade

        u "That place was good."

        scene s560 # Close up evelyn smiling
        with dissolve

        ev "Yeah, it was really good. I've never been here before. Thanks, for paying."

        scene s560a
        with dissolve

        u "My pleasure."

        u "So, how are you getting home?"

        scene s560
        with dissolve

        ev "I've already called an Uber."

        if evelyn.relationship >= Relationship.LIKES:
            ev "Are you just gonna walk back? We can share the Uber if you want."

            scene s560a
            with dissolve

            u "Thanks, but it's okay. It's not that far."

        else:
            scene s560a
            with dissolve

            u "Oh, cool."

        scene s561 # Uber arrives
        with dissolve

        ev "There it is."

        if evelyn.relationship >= Relationship.LIKES:
            scene s562 # Close up evelyn smiling at you, standing in front of you, about to enter the uber
            with dissolve

            ev "Thank you for this date, I didn't think I was gonna enjoy it as much as I did."

            scene s562a
            with dissolve

            u "I hope we can do this again sometime."

            scene s562
            with dissolve

            ev "I hope so too."

            scene s562a
            with dissolve

            menu:
                "Kiss her":
                    $ evelyn.relationship = Relationship.KISS
                    if lauren.relationship >= Relationship.GIRLFRIEND:
                        $ add_point(KCT.TROUBLEMAKER)
                    else:
                        $ add_point(KCT.BOYFRIEND)

                    scene s563 # showing you and evelyn standing close to each other, smiling at each other
                    with dissolve

                    pause 0.75

                    scene s563a # Showing you and Evelyn kissing
                    with dissolve
                    play sound "sounds/kiss.mp3"

                    pause 1.5

                    scene s563
                    with dissolve

                    pause 0.75

                "Don't kiss her":
                    if lauren.relationship >= Relationship.GIRLFRIEND:
                        $ add_point(KCT.BOYFRIEND)
                    else:
                        $ add_point(KCT.BRO)

        label gf_b: #for compatibility only
        scene s562
        with dissolve

        ev "Good bye, [name]."

        scene s562b # Evelyn gets into car
        with dissolve

        u "Good bye, Evelyn."

        scene s564 # you walking back to your dorm at night
        with fade

        if evelyn.relationship >= Relationship.LIKES:
            u "(That went way better than expected. Once she started talking about her dreams, it's like she turned into this completely different person.)"

        else:
            u "(We never really clicked. That probably means I missed my shot with her...)"

        play sound "sounds/vibrate.mp3"
        $ aubrey.messenger.newMessage(_("Hey, I know it's late... but wanna come over?"), force_send=True)
        $ aubrey.messenger.addReply(_("Yeah, sure."), v6_reply7)
        $ aubrey.messenger.addReply(_("Sorry, I can't tonight."), v6_reply8)

        label phoneag:
            stop music fadeout 3
            if aubrey.messenger.replies:
                call screen phone
            if aubrey.messenger.replies:
                u "(I should check my messages.)"
                jump phoneag

        if meetaubrey:
            u "(I'll just go get changed and then it's straight to Aubrey's.)"

        else:
            u "(Damn, I'm in demand today.)"

            jump afteraubrey

    else:
        play sound "sounds/vibrate.mp3"
        scene s546 # phone close up, it's 10:30 pm, message from Aubrey
        with dissolve

        $ aubrey.messenger.newMessage(_("Hey, I know it's late... but wanna come over?"), force_send=True)
        $ aubrey.messenger.addReply(_("Yeah, sure."), v6_reply7)
        $ aubrey.messenger.addReply(_("Sorry, I can't tonight."), v6_reply8)

        u "(Shit, it's already 10:30? Wonder what Aubrey's messaging about.)"

        label v6_phoneah:
            scene s565 # mc sitting at his desk
            with dissolve

            if aubrey.messenger.replies:
                call screen phone
            if aubrey.messenger.replies:
                u "(I should probably reply to Aubrey.)"
                jump v6_phoneah

        if meetaubrey:
            u "(I guess I'm going to Aubrey's)"

        else:
            u "(Damn, I'm in demand today.)"

            jump afteraubrey

    play music "music/mindie1.mp3"

    queue music [ "music/mindie2.mp3", "music/mindie3.mp3" ]

    scene s566 # you knock on aubrey's door
    with Fade(1,0,1)

    play sound "sounds/knock.mp3"

    "*Knock knock knock*"

    scene s567 # Close Up: Aubrey opens the door
    with dissolve
    play sound "sounds/dooropen.mp3"

    au "Heyy."

    scene s567a
    with dissolve

    u "You look good."

    scene s567b # Aubrey flirty
    with dissolve

    au "Oh do I?"

    scene s567c
    with dissolve

    u "Hey, how come you wanted me to sneak in last time, but not this time?"

    scene s567b
    with dissolve

    au "None of the girls are home. We got the whole place to ourselves."

    au "So are you gonna come in or what?"

    scene s568 # Mc sits alone on the edge Aubreys bed waiting for aubrey, aubrey not visible
    with fade

    pause 0.5

    scene s569 # Close up Aubrey standing in front of you (coming from the door) with 2 beers in her hand
    with dissolve

    au "You want a beer?"

    scene s569a
    with dissolve

    u "Sure, thanks."

    scene s570 # CLose up aubrey sitting next to you with a beer, lifting up her beer to toast

    au "Cheers?"

    scene s570a # you toast
    with dissolve
    play sound "sounds/toast.mp3"

    u "Cheers."

    scene s570b # Aubrey drinks beer
    with dissolve

    pause 0.5

    scene s570c # Aubrey puts beer away
    with dissolve

    u "I like your outfit."

    scene s570d # irony smile
    with dissolve

    au "*Chuckles* Good thing I didn't just put the first thing I found on."

    scene s570e
    with dissolve

    u "If you did, it was a lucky find, haha."

    scene s570f # Aubrye curious smile
    with dissolve

    if chloe.relationship <= Relationship.MAD:
        au "So, who have you been seducing lately? Certainly not Chloe. *laughs*"

        scene s570g
        with dissolve

        u "Wow, thanks for that."

    else:
        au "So, how are things with Chloe?"

        scene s570g
        with dissolve

        u "Oh come on, don't act like you don't know more about that than me. You guys are best friends."

        scene s570f
        with dissolve

        au "Okay, how are things with other girls then? Who have you been seducing lately?"

        scene s570g
        with dissolve

    menu:
        "A few different girls":
            $ add_point(KCT.BRO)
            $ add_point(KCT.TROUBLEMAKER)

            u "You know, a few different girls."

            if aubrey.relationship >= Relationship.FWB:
                u "It's kinda crazy how you're so cool with it."

                scene s571a
                with dissolve

                pause 0.5

                scene s571 #Showing you and Aubrey, Aubrey swung herself on your lap facing you
                with vpunch

                au "It's actually kinda hot."

            else:
                scene s570h # aubrey flirting
                with dissolve

                au "Am I one of them?"

                scene s570j
                with dissolve

                menu:
                    "I think you know":
                        $ add_point(KCT.BRO)
                        $ add_point(KCT.TROUBLEMAKER)

                        u "I think you know."

                        scene s571a
                        with dissolve

                        pause 0.5

                        scene s571
                        with vpunch

                        au "I think I do."

                    "We're just friends":
                        $ add_point(KCT.BOYFRIEND)
                        $ add_point(KCT.TROUBLEMAKER)

                        u "Uhm, Aubrey I think we should just stay friends."

                        scene s570k # Aubrey confused and surprised and embarrased
                        with dissolve

                        au "Oh..."

                        au "Uhm, yeah of course."

                        scene s570l
                        with dissolve

                        pause 0.5

                        jump aubreytalk

        "No one, really":
            $ add_point(KCT.BOYFRIEND)

            u "No one, really."

            if aubrey.relationship >= Relationship.FWB:
                scene s571a
                with dissolve

                pause 0.5

                scene s571 #Showing you and Aubrey, Aubrey swung herself on your lap facing you
                with vpunch

                au "Good thing you have me."

            elif kct == "popular":
                call screen kct_popup

                scene s570h # aubrey flirting
                with dissolve

                au "I don't believe that for one second."

                au "I bet you've been seducing them just like you've been trying to seduce me."

                scene s570j
                with dissolve

                menu:
                    "You got me":
                        $ add_point(KCT.BRO)
                        $ add_point(KCT.TROUBLEMAKER)

                        u "You got me."

                        scene s571a
                        with dissolve

                        pause 0.5

                        scene s571
                        with vpunch

                        au "That's what I thought."

                    "I'm not seducing you":
                        $ add_point(KCT.BOYFRIEND)
                        $ add_point(KCT.TROUBLEMAKER)

                        u "Uhm, Aubrey I'm not trying to seduce you."

                        scene s570k # Aubrey confused and surprised and embarrased
                        with dissolve

                        au "Uhm okay... sure."

                        scene s570l
                        with dissolve

                        pause 0.5

                        jump aubreytalk

            else:
                scene s570f
                with dissolve

                au "Huh, I guess that's one way to go through college."

                scene s570g
                with dissolve

                u "Oh come on, it's only my second week."

                scene s570f
                with dissolve

                au "I guess that's true."

                scene s570g
                with dissolve

                jump aubreytalk


label aubreysexb: # aubreysex scene
    $ aubrey.relationship = Relationship.FWB
    $ sceneList.add("v6_aubrey")

    stop music fadeout 3
    play music "music/msexy.mp3"

    scene naubvid0
    with dissolve

    pause 1.0

    scene naubvid1

    " "

    scene naub1
    with Dissolve(1)

    au "*Quiet moan*"

    if config_censored:
        call screen censoredPopup("wayhome")

    scene naub1a
    with dissolve

    au "*Giggles* Oh god, that tickles."

    scene naubvid2
    with dissolve

    au "*Breathing heavily* Mhhh..."

    scene naub2
    with dissolve

    pause 1.0

    scene naub3
    with dissolve

    " "

    scene naub3a
    with dissolve

    au "Fuck... [name]..."

    scene naub4
    with dissolve

    " "

    scene naub5
    with dissolve

    pause 1.0

    scene naub5a
    with vpunch

    " "

    scene naubvid3
    with dissolve

    au "Mhhh..."

    au "This feels so fucking good."

    " "

    scene naub6
    with dissolve

    au "I can't fucking wait, let's get you undressed."

    scene naub7
    with dissolve

    pause 1.0

    scene naub7a
    with dissolve

    pause 1.0

    scene naub7b
    with dissolve

    au "You ready for the best blowjob you've ever had?"

    scene naub7c
    with dissolve

    u "I so am."

    scene naub8
    with dissolve

    pause 0.5

    scene naub8a
    with dissolve

    au "Hello, buddy."

    scene naub9
    with dissolve

    au "Mhhh..."

label naubblowjob:
    show screen aubreysexoverlay

    scene naubvid4
    with dissolve

    u "Fuck..."

    " "

    scene naubvid5
    with dissolve

    u "Oh my god, Aubrey..."

    " "

    u "Move your ass over here."

    scene naub10
    with dissolve

    au "You wanna have some fun too, huh?"

    scene naub11
    with dissolve

    pause 0.5

    scene naub11a
    with dissolve

    pause 1.0

label naub69:
    scene naubvid6
    with dissolve

    au "*Moans* Mhhh..."

    au "*Moans louder* Ah..."

    au "*Moans even louder* Fuck..."

    " "

    scene naubvid7
    with dissolve

    au "Ahhhhh! Yes, [name]!"

    au "Oh my god!"

    scene naub12
    with dissolve

    pause 0.5

    scene naub12a
    with Dissolve (1)

    au "How the fuck did you make me cum so fucking fast?"

    scene naub12b
    with dissolve

    u "*Chuckles* Sorry it's a trade secret."

    scene naub12a
    with dissolve

    au "Well I got a surprise for you to return the favor."

    scene naub12b
    with dissolve

    u "Oh really? What's that?"

    scene naub12a
    with dissolve

    au "Wait here."

    scene naub12c
    with dissolve

    pause 1.0

    scene naub12d
    with dissolve

    pause 1.0

    scene naub13
    with dissolve

    u "*Chuckles* What are you looking for?"

    scene naub14
    with dissolve

    au "This."

    scene naub14a
    with dissolve

    u "Are those real handcuffs?"

    u "Don't you usually use like plush ones for sex?"

    scene naub14
    with dissolve

    au "Where's the fun in that?"

    scene naub15
    with fade

    " "

    scene naub16
    with dissolve

    au "*Quiet moan*"

    scene naub16a
    with dissolve

    au "*Moans* Mhhh..."

    scene naub16b
    with dissolve

    au "*Moans louder* Ahh..."

    scene naub16c
    with dissolve

    au "*Breathing heavily*"

    scene naub17
    with dissolve

    pause 1.0

    scene naub17a
    with dissolve

    u "You have such a gorgeous body..."

    scene naub17b
    with dissolve

    u "*Wets fingers*"

    scene naub17c
    with vpunch

    au "*Loud moan* Ahhh..."

label naubfingering:
    scene naubvid8
    with dissolve

    au "Oh my god..."

    au "*Moans*"

    au "Yes..."

    au "[name] please... *Moans*"

    au "Fuck me! I need your dick inside of me!"

    " "

    scene naub18
    with dissolve

    pause 0.5

label naubmissionary:
    scene naub9start
    with vpunch

    au "*Loud moan* Ohhh..."

    scene naubvid9
    with dissolve

    au "Yes!"

    au "*Moans* Fuck me!"

    " "

    scene naubvid10
    with dissolve

    au "[name]! *Moans louder*"

    au "Ahhhh, oh my god!!!"

    " "

    scene naub18
    with dissolve

    pause 0.5

    scene naub19
    with dissolve

    u "Let's turn you around."

    scene naub19a
    with dissolve

    au "Yes! Fuck me from behind!"

label naubbehind:
    scene naubvid11
    with dissolve

    au "*Moans* Ahhhhh!"

    au "*Moans louder* Yes, [name]! Don't stop!"

    " "

    scene naubvid12
    with dissolve

    au "*Moans* Ohhhhh!"

    au "Oh my god! I'm gonna cum!"

    u "Fuuuuck, me too!"

label naubclimax:
    scene naubvid13
    with dissolve

    au "*Moans really loud* Ahhhh!"

    au "Holy shit..."

    hide screen aubreysexoverlay
    $ renpy.end_replay()

    scene naub20
    with fade
    stop music fadeout 3

    u "That was amazing."

    play music "music/m16punk.mp3"
    scene naub21
    with dissolve

    au "Honestly, I think that was the best sex I ever had."

    scene naub21a
    with dissolve

    u "Yeah, me too."

    scene naub21b
    with dissolve

    au "I know it sucks, but I think the girls are coming back soon..."

    scene naub21c
    with dissolve

    u "I gotta go soon anyway, it's quite late."

    u "I'll see you soon, okay? Can't wait to do this again. *Chuckles*"

    scene naub21
    with dissolve

    au "Sounds good, me neither."

    jump wayhome

label aubreytalk:
    $ aubrey.relationship = Relationship.FRIEND

    u "So uhm... how's third year treating you?"

    scene s570m # aubrey no smile, just awkward convo
    with dissolve

    au "Hmm, it's hard. I don't really understand half of the stuff they're teaching us."

    scene s570n
    with dissolve

    u "Yeah, I get that. My economics teacher just keeps giving us assignment after assignment."

    scene s570m
    with dissolve

    au "If you think first year is a lot of assignments, you're definitely not gonna enjoy third year."

    au "Uhm, I think the girls are coming back soon..."

    scene s570n
    with dissolve

    u "Yeah, I should probably head home anyway. It's already pretty late."

    u "I'll see you later."

label wayhome:
    scene s572 # mc walking home
    with fade

    pause 0.5

label afteraubrey:
    scene s573 # mc in his dorm in bed exhausted with his hand on his pocket
    with fade

    if aubrey.relationship >= Relationship.FWB:
        play sound "sounds/vibrate.mp3"

        if config_censored:
            $ aubrey.messenger.newImgMessage("gui/censoredPopup/censoredBackground.webp", force_send=True)
        else:
            $ aubrey.messenger.newImgMessage("images/v6/text3.webp", force_send=True)

        if meetaubrey:
            $ aubrey.messenger.newMessage(_("Still shaking from earlier"), force_send=True)
            $ aubrey.messenger.addReply(_("Hahaha, we should definitely do this more ;)"))

        else:
            $ aubrey.messenger.newMessage(_("You missed out today"), force_send=True)
            $ aubrey.messenger.addReply(_("Daaaamn, I'll be there next time"))

        " "

    else:
        pause 0.5
    
    scene s573a # mc looks at his phone (you can only see the bakc of the phone)
    with dissolve

    u "(Oh shit, it's almost midnight.)"

    u "(Grayson said I should meet him, but how can I trust him after everything that happened?)"

    scene s574 # First person: Looking at the door
    with dissolve

    menu:
        "Meet Grayson":
            $ meetgrayson = True
            $ add_point(KCT.TROUBLEMAKER)

            label meetgrayson: #for compatibility only
            u "(I wanna hear what he has to say.)"

            scene s575 # mc sits alone at midnight on the front stairs of the college waiting.
            with fade

            play music "music/m3punk.mp3"

            queue music [ "music/m4punk.mp3", "music/m12punk.mp3", "music/m13punk.mp3" ]

            pause 1.0

            scene s575a # Mc looks around
            with dissolve

            u "(Great, he's not even here.)"

            scene s576 # Grayson in car pulls up
            with dissolve

            pause 0.5

            scene s576a # he leans over and opens the passenger door
            with dissolve

            gr "Get in."

            scene s577a # Grayson close up mouth closed arrogant smile
            with dissolve

            u "Where are we-"

            scene s577 # same as 577a but mouth open
            with dissolve

            gr "Just get in. Come on."

            scene s577a
            with dissolve

            u "*Sighs* Alright."

            scene s578 # mc gets into the car
            with dissolve

            pause 0.5

            #### Car scene

            play music "sounds/driving1.mp3"

            show carbacknight

            show s579a # Grayson close up driving mouth closed arrogant / devious smile mouth closed
            with fade

            u "So, really, where are we going?"

            hide s579a
            show s579 # same as 579a but mouth open
            with dissolve

            gr "*Laughs*"

            hide s579
            show s579b # Grayson looking at you with the "are you serious slightly annoyed look"
            with dissolve

            gr "Anyone ever tell you to relax a little."

            hide s579b
            show s579
            with dissolve

            gr "Trust the process!"

            hide s579
            show s579a
            with dissolve

            u "Great... if I knew you were gonna kidnap me I wouldn't have shown up."

            hide s579a
            show s579b
            with dissolve

            gr "Just chill, okay? I'm not kidnapping you, Jesus."

            hide s579b
            show s579a
            with dissolve

            pause 0.5

            hide s579a
            show s579d # grayson looking at the road apologetic
            with dissolve

            gr "Like I said before, sorry about that night at the party. I have a tendency to drink too much sometimes."
            gr "Guess we all have shit that we need to deal with."

            hide s579d
            show s579e
            with dissolve

            u "Right..."

            hide s579e
            show s579d
            with dissolve

            gr "You know, growing up. Things weren't always easy."

            hide s579d
            show s579e
            with dissolve

            u "Yeah, I can relate to that."

            hide s579e
            show s579d
            with dissolve

            gr "Sometimes I just snap. I guess it all comes back to how we grew up."

            hide s579d
            show s579e
            with dissolve

            u "If you don't mind me asking, how did you grow up?"

            hide s579e
            show s579d
            with dissolve

            gr "When I was very young, my mom passed away, so for most of my life it was just me and my dad."

            hide s579d
            show s579e
            with dissolve

            u "I'm sorry."

            hide s579e
            show s579d
            with dissolve

            gr "It wasn't that bad for a while. Sure I was sad, but I had a great life before. My dad was caring and we had a lot of money so that was never an issue."

            hide s579d
            show s579e
            with dissolve

            u "So what happened?"

            hide s579e
            show s579d
            with dissolve

            gr "Well not too long after, my dad remarried. And at first it was fine, like at least my dad was happy."
            gr "I didn't really get along with my two new stepbrothers, but they weren't terrible people."
            gr "It wasn't until my dad became sick... I mean, it all happened so quickly and all of the sudden... he was gone."

            hide s579d
            show s579c # grayson looking at you disturbed
            with dissolve

            gr "After that step mom just went crazy."

            hide s579c
            show s579d
            with dissolve

            gr "It's like she waited for this to push me out of the family. She'd force me to sleep in the attic and I had to do all the chores. I was treated like a maid."
            gr "And my step brothers taunted and bullied me. The once amazing house I lived in had fallen apart because my evil stepmother began spending all of my dad's money."
            gr "It was really terrible. I was never allowed to make friends or have fun. I lived just to serve them."

            hide s579d
            show s579e
            with dissolve

            menu:
                "Empathize":
                    $ add_point(KCT.BOYFRIEND)

                    u "Man, I'm sorry. That's really terrible. I didn't know you had it so rough."

                    hide s579e
                    show s579d
                    with dissolve

                    gr "Yeah, sometimes stuff like that just leads to anger management issues."

                    hide s579d
                    show s579e
                    with dissolve

                    u "I get it. We're cool."

                    hide s579e
                    show s579d
                    with dissolve

                    gr "Good. We're here by the way."

                "Question":
                    $ add_point(KCT.TROUBLEMAKER)

                    u "That story sure sounds an awful lot like Cinderella."

                    hide s579e
                    show s579f # Grayson looking at you with I pranked you laugh
                    with dissolve

                    gr "*Laughs* You got me."

                    hide s579f
                    show s579a
                    with dissolve

                    u "What?"

                    hide s579a
                    show s579
                    with dissolve

                    gr "It was a test."

                    hide s579
                    show s579a
                    with dissolve

                    u "A test?"

                    hide s579a
                    show s579
                    with dissolve

                    gr "Yeah, just to see how naive you were. To be an Ape you gotta be sharp. We need top guys."
                    gr "Not a lot of people would've caught that."

                    hide s579
                    show s579a
                    with dissolve

                    u "Right..."

                    hide s579a
                    show s579
                    with dissolve

                    gr "We're here."

            label wehere: #for compatibility only
            stop music fadeout 3

            scene s580 # Showing you and Grayson At night on a ledge, overlooking the city??? Or something else cool, Grayson looking into the distance
            with fade

            gr "What does it mean to be a winner?"

            scene s580a # Grayson turns around to look at you
            with dissolve

            pause 0.5

            scene s581 # Grayson close up: energetic speech
            with dissolve

            gr "A winner is relentless. Some would even say ruthless. A tough guy. A guy who will stick it out until the end to make sure, that he's the one coming out on top."
            gr "A winner doesn't let anyone surpass him. He won't tolerate anyone who gets in his way. He does whatever it takes to win."

            scene s581b # Grayson uses a hand gesture for emphasis
            with dissolve

            gr "So in other words, a winner is an Ape. An Ape doesn't let any fucker step on him. An Ape isn't a pussy."

            scene s581
            with dissolve

            gr "He stands up for himself and his guys and fights it out. We're some of the strongest and smartest guys around."

            scene s581d # Grayson steps a bit closer
            with dissolve

            gr "[name], I look at you and I see the potential."
            gr "The potential to become the next great Ape. To become a winner. To become a leader."
            gr "Join the Apes. Join me. Together, we'll destroy the Wolves. We'll destroy anyone who gets in our way."

            scene s581f # Grayson devious smile
            with dissolve

            gr "And the best part, all the girls come flocking. I know you have your eye on Chloe. She won't be able to resist you."

            scene s581g
            with dissolve

            pause 0.5

            u "How do you see potential, when you don't even know me?"

            if not fighttom and not fightadam:
                u "I haven't even fought anyone!"

                scene s581d
                with dissolve

                gr "You can teach someone how to fight, but you can't teach them how to think."

            elif not fighttom or not fightadam:
                    u "I fought like one guy in my entire life!"

                    scene s581d
                    with dissolve

                    gr "You can teach someone how to fight, but you can't teach them how to think."

            else:
                u "I fought like two people in my entire life!"

                scene s581d
                with dissolve

                gr "You can teach someone how to fight, you can't teach them how to think."

            gr "You may not be a big fighter yet, but we can change that in no time with our facilities."
            gr "What I see in front of me is much more than a fighter, I see a leader."
            gr "People are drawn to you. Don't let that go to waste with a frat that doesn't see your true potential."
            gr "Join the Apes and I promise you, everyone at San Vallejo will know who you are within weeks."

            scene s581f
            with dissolve

            gr "So what do you say?"

            scene s581g
            with dissolve

            u "Uhm..."

            play sound "sounds/swoosh.mp3"
            scene s63d
            with flash
            show screen fantasyOverlay

            imre "Exactly, which is also why I'm joining the Wolves."

            scene s63e
            with dissolve

            u "The Wolves? I thought the Apes were the best frat to get girls?"

            scene s64
            with dissolve

            imre "Who told you that?! That's bullshit."
            imre "The Apes are disloyal pieces of shit. The Wolves are real brothers and they get mad pussy."

            scene s64a
            with dissolve

            u "Didn't you say it's your first day? How do you know the frats so well?"

            scene s63
            with dissolve

            imre "It is, but my brother used to be a Wolf and he told me about all the shady shit that the Apes would do."

            hide screen fantasyOverlay
            play sound "sounds/swoosh.mp3"
            scene s581g
            with flash

            menu:
                "I'm in":
                    $ add_point(KCT.TROUBLEMAKER)
                    $ joinapes = True

                    u "Okay, I'm in."

                    scene s582 # Interaction: Grayson and you do a bro hand shake
                    with dissolve
                    # handshake clap sound

                    $ grant_achievement("monkey_business")

                    gr "That's what I'm talking about!"

                    scene s582a # Grayson pulls you in for bro hanshake hug
                    with dissolve

                    pause 0.5

                    scene s581f
                    with dissolve

                    gr "You made the right call."

                    scene s581g
                    with dissolve

                    u "Yeah, I sure hope so."

                    scene s581f
                    with dissolve

                    gr "Trust me."
                    gr "Just remember, once an Ape, always an Ape. Otherwise we're gonna have to kill you."

                    scene s581g
                    with dissolve

                    u "What???"

                    scene s581f
                    with dissolve

                    gr "*Laughs* I'm just messing with you. Come on, let's go."

                    # back in the car, already rendered
                    # car sound and background
                    play music "sounds/driving1.mp3"
                    scene carbacknight

                    show s579a
                    with fade

                    u "I told people I was gonna go to the Wolves' rush party, but I probably shouldn't go now, right?"

                    hide s579a
                    show s579b
                    with dissolve

                    gr "Nah, you should go."

                    hide s579b
                    show s579
                    with dissolve

                    gr "Sometimes I like to hang out with less talented people too... just to see how the other side lives."

                    hide s579
                    show s579a
                    with dissolve

                    u "*Chuckles* Alright, I'll go."

                    hide s579a
                    show s579
                    with dissolve

                    gr "The official pledging period starts on Wednesday, so I expect you at the Ape's house at 6 pm that day."

                    hide s579
                    show s579a
                    with dissolve

                    u "I'll be there."

                    hide s579a
                    show s579
                    with dissolve

                    gr "Good. Trust me, this will change everything."
                    stop music fadeout 3

                "I'm not in":
                    $ add_point(KCT.BRO)
                    $ joinapes = False

                    u "Sorry, Grayson. But I don't wanna be an Ape."

                    scene s581h # Grayson angry
                    with dissolve

                    gr "What? What do you mean you don't wanna be an Ape?!"

                    scene s581j
                    with dissolve

                    u "I'm not like you, I care about my friends."
                    u "I'm not gonna betray Imre and I'm not gonna join you after everything that's happened."

                    scene s581h
                    with dissolve

                    gr "You're a nobody without the Apes. You're making the biggest mistake of your life."

                    scene s581j
                    with dissolve

                    u "That may be the case, but at least I'm not being a disloyal piece of shit."

                    scene s581h
                    with dissolve

                    gr "I guess you don't have what it takes to be a winner. What a shame."

                    scene s583 # Grayson walks towards his car
                    with dissolve

                    pause 0.5

                    scene s584 #Grayson gets into his car.
                    with dissolve
                    # car entering sounds

                    u "Hey! Where are you going?"

                    scene s585 # Grayson drives off
                    with dissolve
                    # skirt of sounds

                    u "Grayson, what the fuck?! You're my ride!"

                    scene s585a # Grayson gone
                    with dissolve

                    u "Fuck!"
                    u "(Guess I'm calling an Uber.)"

                    scene s298
                    with fade

                    pause 0.5

        "Stay home":
            $ add_point(KCT.BRO)
            
            $ grant_achievement("seems_fishy")

            u "(Fuck Grayson, I'm not meeting him.)"

    label aftergrayson: #for compatibility only
    stop music fadeout 3

    scene s586 # you lying in bed at night staring at the ceiling
    with fade

    u "(This day was wild. I don't even know what to think anymore...)"

    u "(Time to get some rest.)"

    scene s586a # you sleeping
    with fade

    pause 0.5
    #### Nightmare
    play music "music/mhorror.mp3"
    play sound "sounds/swoosh.mp3"
    scene s587 # Showing you, lauren and Riley running through the forest terrified like someone's after them
    with flash

    ri "He's coming!"

    scene s588  # Lauren running as fast she can scared
    with dissolve

    la "I can't run any faster!"

    scene s589 # showing  only mc in front of a cliff looking down
    with dissolve

    u "Fuck guys! We can't go any further, there's a cliff!"

    scene s590 # zooms out showing mc look around, Riley and Lauren are gone
    with dissolve

    u "Guys?"

    scene s590a # mc turns around shocked
    with dissolve

    pause 0.5

    scene s591 #A really big scary guy has a gun in each hand one to laurens head on his right and one to Rileys head his lefty
    with dissolve

    unknown "I guess it's time for you two to die."
    unknown "3..."
    unknown "2..."

    menu (fail_label="timera"):
        "Save Lauren":
            $ add_point(KCT.BOYFRIEND)
            $ save = 1

            scene s592 # Mc tackles Lauren out of the guns aim
            with dissolve

            unknown "1..."
            play sound "sounds/fall.mp3"

            scene s593 # Mc and Lauren on the ground terrified
            with vpunch

            play sound "sounds/gun.mp3"
            pause 0.5

            scene s593a # mc looks back and screams
            with dissolve

            u "Nooo!"

            jump wakeupa

        "Save Riley":
            $ add_point(KCT.BRO)
            $ save = 2

            scene s594 # Mc tackles Riley out of the guns aim
            with dissolve

            unknown "1..."
            play sound "sounds/fall.mp3"

            scene s595 # Mc and Riley on the ground terrified
            with vpunch

            play sound "sounds/gun.mp3"
            pause 0.5

            scene s595a # mc looks back and screams
            with dissolve

            u "Nooo!"

            jump wakeupa

label timera:
    $ save = 0

    scene s596 # close up of your face terried
    with dissolve

    unknown "1..."
    play sound "sounds/gun.mp3"

    scene s596a # Mc screaming terrified
    with vpunch

    u "Nooo!"

label wakeupa:
    stop sound
    hide screen fantasyOverlay
    play sound "sounds/swoosh.mp3"
    scene s586b # you wake up in disstress
    with flash

    u "*Breathing heavily* (Holy shit... thank god that was just a dream.)"
    play music "music/m15punk.mp3"

    queue music ["music/mfunk.mp3"]

    if imre.relationship <= Relationship.MAD:
        scene s604 # Mc wakes up in bed,
        with Fade (2,0,2)

        u "(I should go to the gym today, even if Imre's no longer gonna train me."

        scene s605 # mc walks to the gym, same clothes as in the scenes with Imre
        with fade

        pause 0.5

        scene s606 # Mc benching, bar in hands, arms extended
        with fade

        pause 0.5

        scene s606a # amrs not extended
        with dissolve

        pause 0.5

        scene s606
        with dissolve

        pause 0.5

        scene s606a
        with dissolve

        pause 0.5

        scene s607 #MC is running on the treadmills.
        with dissolve

        pause 0.5

        scene s607a # other leg forward
        with dissolve

        scene s607
        with dissolve

        pause 0.5

        scene s607a
        with dissolve

        pause 0.5

        scene s608 #*MC is curling dumbbells, arms extended
        with dissolve

        pause 0.5

        scene s608a # arms in curl position
        with dissolve

        pause 0.5

        scene s608
        with dissolve

        pause 0.5

        scene s608a
        with dissolve

        pause 0.5

        scene s601 # you sweaty and you have a pump! (Make MC's base model a bit bulkier) not showing Imre
        with fade

        u "*Breathing heavily* (Fuck, that was so exhausting)."

        scene s602 #MC stands in front of the mirror sweaty and flexes his muscles., not showing Imre, make sure you can't tlel that hte gym is empty
        with dissolve

        u "(At least I'm starting to gain some muscles.)"

        u "(Well. Time to go home.)"

    else:
        scene s597 # First person, Imre standing over Mc in Gym clothes! it's essential that they wear the same clothes as last time! CHeck s234 picture, mc no longer has a black eye as well
        with Fade (2,0,2)

        imre "Wake up, man."
        imre "Time to go to the gym!"

        scene s597a
        with dissolve

        u "Mhmm alright. Give me ten minutes."

        scene s234 # already rendered
        with Fade (1,0,1)

        u "But you gotta promise to keep it light today."

        scene s235 # already rendered
        with dissolve

        imre "Sure, bud. I'm gonna teach you a slick move today."

        scene s235a
        with dissolve

        u "I feel like at some point all these moves become too much to focus on, haha."

        scene s235
        with dissolve

        imre "I used to feel that way too, but my brother taught me a good technique to deal with that."
        imre "Before every fight I like to think about what moves might be best against each opponent and then I just focus on these."

        scene s235a
        with dissolve

        u "Huh, so what's the point of learning new moves if you only use a few at a time anyways?"

        scene s235
        with dissolve

        imre "Different sized opponents require different techniques. Also, what about impressing the ladies that watch you fight? The cooler the moves, the hotter the girls."

        scene s235a
        with dissolve

        u "*Laughs* You really know your priorities."

        scene s598 # you and Imre in front of the boxing bag
        with fade

        imre "Alright, I'm gonna show you how to throw an uppercut."

        scene s599 # First person: Imre in front of boxing bag looking at hte boxing bag ready to throw an uppercut
        with dissolve

        pause 0.5
        play sound "sounds/bs.mp3"
        scene s599a # Imre throws uppercut, bag barely moves
        with vpunch

        imre "*Winces in pain* Ahh fuck."

        scene s599
        with dissolve

        u "Shit. Imre, be careful."

        scene s599b # Imre looking at you slightly in pain
        with dissolve

        imre "Okay, turns out I can't really show you the full power of it right now."

        imre "Just go like this."

        scene s599
        with dissolve

        pause 0.5

        scene s599a
        with dissolve

        pause 0.5

        scene s599
        with dissolve

        pause 0.5

        scene s599a
        with dissolve

        pause 0.5

        scene s599b
        with dissolve

        imre "Just remember, you want your fist to be a vertical line to your opponent's chin when you hit it."

        scene s600 # mc in front of boxing bag # not showing Imre
        with fade

        pause 0.5
        play sound "sounds/bs.mp3"
        scene s600a # mc throws an uppercut successfully
        with vpunch

        pause 0.5

        scene s600
        with dissolve

        imre "Nice! Try again."

        play sound "sounds/bs.mp3"
        scene s600a
        with vpunch

        pause 0.5

        scene s600
        with dissolve

        pause 0.5
        play sound "sounds/bs.mp3"
        scene s600a
        with vpunch

        $ moveuppercut = True

        call screen fightPopup("Uppercut")

        scene s600
        with dissolve

        imre "Great job! Now let's move on to some strength and conditioning training."

        # gym montage not showing Imre

        scene s606 # Mc benching, bar in hands, arms extended
        with fade

        pause 0.5

        scene s606a # amrs not extended
        with dissolve

        pause 0.5

        scene s606
        with dissolve

        pause 0.5

        scene s606a
        with dissolve

        pause 0.5

        scene s607 #MC is running on the treadmills.
        with dissolve

        pause 0.5

        scene s607a # other leg forward
        with dissolve

        scene s607
        with dissolve

        pause 0.5

        scene s607a
        with dissolve

        pause 0.5

        scene s608 #*MC is curling dumbbells, arms extended
        with dissolve

        pause 0.5

        scene s608a # arms in curl position
        with dissolve

        pause 0.5

        scene s608
        with dissolve

        pause 0.5

        scene s608a
        with dissolve

        pause 0.5

        scene s601 # you sweaty and you have a pump! (Make MC's base model a bit bulkier) not showing Imre
        with fade

        u "*Breathing heavily* (Fuck, that was so much harder than last time.)"

        scene s602 #MC stands in front of the mirror sweaty and flexes his muscles., not showing Imre, make sure you can't tlel that hte gym is empty
        with dissolve

        u "(At least I'm starting to gain some muscles.)"

        scene s603 # Imre close up, standing behind you, proud of you
        with dissolve

        imre "Great job today man, you're really learning fast. The Wolves are gonna love you."
        imre "I gotta go meet up with some friends now. I'm just gonna shower here then head out."
        imre "I'll see you later."

    scene s609 # mc walking home by himself after the gym
    with fade
    
    $ amber.messenger.newMessage(_("Heyy, what are you up to? xx"), force_send=True)
    $ amber.messenger.addReply(_("Just walking back from the gym wbu?"))
    $ amber.messenger.newMessage(_("Going to my next lecture x_x"))
    $ amber.messenger.newMessage(_("Which gym do you go to? Maybe we can go together at some point"))
    $ amber.messenger.addReply(_("Sports X and you?"))
    $ amber.messenger.newMessage(_("Awww I'm SV Fitness :("))
    $ amber.messenger.addReply(_("Maybe we should do a home workout together sometime ;)"), v6_reply9)
    $ amber.messenger.addReply(_("Yeah, that's too bad :/"), v6_reply10)

    if bowling:
        $ penelope.messenger.addReply(_("Hey, you wanna go bowling today? I'm free this afternoon"))
        $ penelope.messenger.newMessage(_("Yeah, sounds good :)"))
        $ penelope.messenger.newMessage(_("I have a lecture at 2:30 but I can go straight to the bowling alley afterwards"))
        $ penelope.messenger.newMessage(_("Meet there at 4?"))
        $ penelope.messenger.addReply(_("Yesss, see you there"))

        u "(I should ask Penelope whether she wants to do bowling this afternoon.)"

        call screen phone
        label phoneak:
            if penelope.messenger.replies:
                call screen phone
            if penelope.messenger.replies:
                u "(I should really text Penelope.)"
                jump phoneak

        pause 0.5

    else:
        " "

        pause 0.5
    
    stop music fadeout 3

    scene s610 # you back in your dorm doing work at your desk in your regular clothes, "a few hours later transition"
    with Fade (1,0,1)

    pause 1.0

    play sound "sounds/call.mp3"

    "*Phone rings*"

    stop sound

    play sound "sounds/answercall.mp3"

    play music "music/mindie1.mp3"

    queue music [ "music/mindie2.mp3", "music/mindie3.mp3" ]

    scene s611 # close up mc on phone mouth open
    with dissolve

    u "Hello?"

    scene s611a # mouth closed
    with dissolve

    ri "Hey, I know this is really last minute, but I was wondering if you wanted to go to a poetry slam with me right now?"
    ri "I know it's short notice, but one of my friends bailed on me and now I have an extra ticket."

    scene s611
    with dissolve

    u "Uhh sure, I'll go with you."

    scene s611a
    with dissolve

    ri "Really? Great! Meet me at the theater room in 10 minutes."

    scene s611
    with dissolve

    u "Cool, will do."

    scene s612 #Opening showing everyone, MC shows up to the poetry slam. He sees Riley already seated
    with fade

    pause 0.5

    scene s612a # She sees MC and waves him down.
    with dissolve

    u "Hey."

    scene s612b #MC goes over and takes the empty seat next to her. Riley talks to him
    with dissolve

    ri "Hi, thanks for coming. I know it's last minute, but I think it's gonna be really cool."

    scene s613 #The host walks out onto the stage.
    with dissolve

    scene s614 # RIley close up excited talking to you but looking at the stage
    with dissolve

    ri "Oh, it's starting!"

    scene s615 # host close up, presenting
    with dissolve

    host "Welcome everyone, familiar faces and new faces."
    host "Thank you for joining us for the annual poetry slam. Today we are here to make noise, make our voices heard, make our opinions known and make a difference!"

    scene s615a
    with dissolve

    "*Crowd applauds*"

    scene s615
    with dissolve

    host "Today, we will hear from many talented and amazing people. So without further ado, let's bring out our first poet, Lisa."

    scene s616 # poet 1 walks onto stage
    with dissolve

    "*Crowd applauds*"

    scene s617 # poet 1 close up, performing
    with dissolve

    poet1 "It's been one year since I've recovered from my eating disorder,"
    poet1 "One year of not counting the calories, crying as the food slithered down my throat."
    poet1 "One year without the fainting spells and wasted meals down the toilet."
    poet1 "One year without being afraid of dinner invitations and hiding in cold sweats under sheets."

    scene s617a # poet 1 close up, performing pose 2
    with dissolve

    poet1 "It's the first year I don't find peace in the stomach pains."
    poet1 "It's the first year where I don't wake up to step on the scale."
    poet1 "It's the first year I don't find happiness in the emptiness."
    poet1 "It's the first year I can eat a meal knowing it's not going to come back up."

    scene s617b # poet 1 close up, performing pose 3
    with dissolve

    poet1 "It's really hard to not feel like this eating disorder isn't who I've become when it feels like my only accomplishment."
    poet1 "When I dropped 30 pounds in a month my friends told me I looked incredible."
    poet1 "My father said: Honey, I'm so proud of you."
    poet1 "My mother said: I've never been so happy for you."

    scene s617c # poet 1 close up, performing pose 4
    with dissolve

    poet1 "It's kind of hard to feel that this eating disorder isn't me when people only praised me for my illness."
    poet1 "And it's those same people who blindly support me in this journey to find myself, but ignored all the times I spent too long in the bathroom."
    poet1 "The infinite times I brushed my teeth, the sobs over the toilet seat."
    poet1 "It's kind of hard not to fall back into this black hole of starvation when it feels like it's the only thing that made me feel important."
    poet1 "But hey, at least I can step in front of the mirror and look at myself and say: Well, at least I'm not dying."

    scene s618 #The girl walks off in tears
    with dissolve

    "*Crowd applauds*"

    scene s614a # same aas 614 buth riley mouth closed
    with dissolve

    menu:
        "Praise her":
            $ add_point(KCT.BOYFRIEND)

            u "That was incredible."

            scene s614b # Riley looking at you happy
            with dissolve

            ri "I know it's so amazing what stories people have to tell."

            scene s614c
            with dissolve

            u "Yeah, absolutely."

            scene s614b
            with dissolve

            ri "Honestly, she's so brave. My heart goes out to her."

        "Mock her":
            $ add_point(KCT.BRO)
            $ add_point(KCT.TROUBLEMAKER)

            scene s614a
            with dissolve

            u "God can she talk about something else than puking, she's not the first person to struggle with a diet."

            scene s614d # riley looking at you upset
            with dissolve

            ri "What the hell, [name]???"

            ri "She's so brave for putting herself out there. I can't believe you'd say something like that."

            scene s614e
            with dissolve

            u "Right..."

    label gn_ad: #for compatibility only
    scene s615
    with dissolve

    host "Thank you so much for that wonderful performance, Lisa."

    host "Now comes our next poet, Martin!"

    scene s619 # poet 2 walks onto stage
    with dissolve

    "*Crowd applauds*"

    scene s620 # close up poet 2 performing pose 1
    with dissolve

    poet2 "Rain... It falls from the sky."

    pause 0.5

    scene s620a # close up poet 2 performing pose 2
    with dissolve

    poet2 "Pitter patter. Pitter patter... Rain falling down the windows."

    poet2 "It drips... Pitter patter... Pitter patter..."

    scene s614f # Rley looking at you whispering, laughing/confused
    with dissolve

    ri "*Whispers* What is happening?"

    scene s620
    with dissolve

    poet2 "-... Rain. It falls. Pitter patter. Pitter patter."

    scene s621 # poet2 walks of stage
    with dissolve

    "*One person applauds*"

    scene s614c # Riley looking at you with a look like that guy was ridiculous mouth closed
    with dissolve

    menu:
        "Praise him":
            $ add_point(KCT.BOYFRIEND)

            u "Honestly, that was kinda profound."

            scene s614b # same as 614j but mouth open
            with dissolve

            ri "*Chuckles* Oh shut up, it was not profound."

            scene s614c
            with dissolve

            u "No seriously, I thought that was really good."

            scene s614b
            with dissolve

            ri "Pff, you're ridiculous."

        "Mock him":
            $ add_point(KCT.BRO)
            $ add_point(KCT.TROUBLEMAKER)

            u "Okay, that was bad. He might as well perform whale sounds."

            scene s614b
            with dissolve

            ri "*Chuckles* Oh god, that's so mean."

            scene s614c
            with dissolve
            u "You can say about art what you want, but this was like objectively bad. *Laughs*"

    label go_ad: #for compatibility only
    scene s615
    with dissolve

    host "Wow Martin, thank you for... something."

    host "Next up is our last scheduled poet before the free for all, please welcome Samantha!"

    scene s622 # hot poet3 walks onto stage
    with dissolve

    "*Crowd applauds extra loud, some guys whistle*"

    scene s623 # close up Samantha mouth closed

    u "Oh yeah, she looks like she'll be good."

    ri "Shh."

    scene s623a # performance pose 1
    with dissolve

    sa "When I was a little girl,"

    sa "All I wanted to be was a super star."

    sa "In my room I'd twirl,"

    sa "Dreaming of the day I could go far."

    scene s623b # performance pose 1
    with dissolve

    sa "Now that I am older,"

    sa "I know that I'm a star."

    sa "I am the beholder,"

    sa "You'll never be at par."

    scene s623c # performance pose 1
    with dissolve

    sa "I know you all want to be me,"

    sa "But no one will ever compare."

    sa "So why not take a knee,"

    sa "And maybe I'll let you breathe my air."

    scene s624 # poet 3 leaves the stage
    with dissolve

    "*Crowd applauds slowly*"

    scene s625 #zoom on her ass
    with dissolve

    menu:
        "Praise her":
            $ add_point(KCT.BRO)
            $ add_point(KCT.TROUBLEMAKER)

            u "She was good."

            scene s614k # riley annoyed
            with dissolve

            ri "Are you serious?"

            scene s614l
            with dissolve

            u "Uhm... you don't think so?"

            scene s614k
            with dissolve

            ri "You can't say she was good just 'cause you find her hot, you know."

            scene s614l
            with dissolve

            u "That's not-, I mean she had... talent."

            scene s614k
            with dissolve

            ri "Yeah, right."

        "Mock her":
            $ add_point(KCT.BOYFRIEND)

            u "Man, that girl was into herself. You think she runs her own fan club?"

            scene s614b
            with dissolve
            ri "*Laughs* Probably."

    label gp_ad: #for compatibility only
    scene s615
    with dissolve

    host "Thank you Samantha, that was really ho-"

    scene s615b # host a bit embarrased cuase he almost said hot to a contestant
    with dissolve

    host "Hospitalizingly well written."

    scene s615
    with dissolve

    host "Anyway, it's time for the final part of the poetry slam, our audience free for all."

    host "Anyone who just felt inspired, may raise their hand now and gets to perform themselves."

    host "Be it what you've scribbled on your notebook or what you've collected on your phone's notes app."

    host "There is no judgment here. Is anyone brave enough to share?"

    scene s614b
    with dissolve

    ri "I dare you to go up."

    scene s614c
    with dissolve

    u "*Laughs* What? Are you crazy?"

    u "I don't have anything to perform."

    scene s614b
    with dissolve

    ri "You know how dares work, you gotta do it."

    scene s614c
    with dissolve

    menu:
        "Okay, I'll do it":
            $ add_point(KCT.BRO)
            $ perform = 1

            u "Okay, I'll do it."

            scene s614b
            with dissolve

            ri "Yayyy!"

            scene s615
            with dissolve

            host "Great! We have a volunteer."

            scene s626 # Mc walks onto stage
            with dissolve

            "*Crowd applauds*"

            "*Riley applauds extra loud*"

            scene s627 # Mc nervous close up in front of Mic
            with dissolve

            "*Clears throat*"

            scene s627a # Mc mouth closed
            with dissolve

            menu:
                "Act out a lullaby":
                    $ add_point(KCT.BRO)

                    if kct == "confident":
                        call screen kct_popup
                        $ perform = 2

                        scene s627b # Mc confident performance pose 1
                        with dissolve

                        u "Twinkle, twinkle little star..."

                        u "How I wonder what you are."

                        scene s627c # Mc confident performance pose 2
                        with dissolve

                        u "Up above the world so high..."

                        u "Like a diamond in the sky."

                        scene s627d # Mc confident performance pose 3
                        with dissolve

                        u "Twinkle, twinkle little star..."

                        u "How I wonder what you are."

                        scene s627e # Mc smiles mouth open
                        with dissolve

                        u "Thank you."

                        scene s627f # Mc smiles mouth closed
                        with dissolve

                        "*Crowd applauds loudly*"

                    else:
                        scene s627g # Mc nervous performance pose 1
                        with dissolve

                        u "Twinkle, twinkle little star..."

                        u "How I uh, wonder what you are."

                        scene s627h # Mc nervous performance pose 2
                        with dissolve

                        u "Up above the world so uhm- so high..."

                        u "Like a- Like a diamond in the sky."

                        scene s627j # Mc nervous performance pose 3
                        with dissolve

                        u "Twinkle, twinkle little star..."

                        u "How I wonder what uhm... you are."

                        scene s627
                        with dissolve

                        u "Thank you."

                        scene s627a
                        with dissolve

                        "*Crowd applauds"

                "Make something up":
                    $ add_point(KCT.TROUBLEMAKER)

                    scene s627g
                    with dissolve

                    u "The stars are on uhh... fire."

                    u "And you are on..."

                    scene s627h
                    with dissolve

                    u "fire."

                    u "I just hope you don't burn out because..."

                    scene s627j
                    with dissolve

                    u "That would uhm..."

                    u "Hurt. Thank you."

                    scene s627a
                    with dissolve

                    "*Crowd applauds"

        "No way I'm doing that":
            $ add_point(KCT.BOYFRIEND)
            $ perform = 0

            u "No. No way. I'm not going up there."

            scene s614b
            with dissolve

            ri "C'mon don't be like that. Go up!"

            scene s614c
            with dissolve

            u "You're crazy. I can't do poetry."

            scene s614k
            with dissolve

            ri "Ugh, fine..."

            scene s615
            with dissolve

            host "Well, since no one's volunteering, I guess we'll call it a night."

            host "Thank you for coming everyone! And have a good night!"

            scene s615a
            with dissolve

            "*Crowd applauds*"

    label afterps: #for compatibility only
    scene s628 # Showing Riley and you outside of the theatre room
    with fade

    pause 0.5

    if perform == 2:
        scene s629 #Close up Riley flirty smile
        with dissolve

        ri "How did you pull that off? You just performed a lullaby and everyone was clapping at the end."

        scene s629a
        with dissolve

        u "You just gotta be confident, haha."

        scene s629
        with dissolve

        ri "Incredible..."

        scene s629d # Riley curious
        with dissolve

        ri "So what did you think of the poetry slam as a whole?"

    elif perform == 1:
        scene s629c # Riley smiling, emphatic mouth close
        with dissolve

        u "Oh god, I was awful."

        scene s629b # mouth open
        with dissolve

        ri "At least you went up there, I think it was brave."

        scene s629d
        with dissolve

        ri "So what did you think of the poetry slam as a whole?"

    else:
        scene s629d
        with dissolve

        ri "So what did you think?"

    scene s629e
    with dissolve
    u "Definitely enjoyed it a lot more than I thought I would."

    scene s629b
    with dissolve

    ri "Told you. Pretty incredible what people can come up with."

    if perform == 0:
        scene s629c
        with dissolve

        u "True. We can definitely do this again at some point."

        scene s629b
        with dissolve

        ri "Yeah."

    else:
        scene s629c
        with dissolve

        u "Yeah, but next time you're the one going up on stage, haha."

        scene s629b
        with dissolve

        ri "*Chuckles* Maybe."

    scene s629c
    with dissolve

    u "Alright, I gotta get back."

    label afterpsb: #for compatibility only
    if bowling:

        u "I'm going bowling with Penelope in a bit."

        scene s629
        with dissolve

        ri "Uhh, who's Penelope?"

        if laurenpublic:
            ri "Does Lauren know?"

            u "We're just friends, it's not a big deal."

            scene s629
            with dissolve

            ri "Alright, whatever you say."

            scene s629a
            with dissolve

            u "I'll see you later."

            scene s629
            with dissolve

            ri "Haha, yeah. Enjoy your date."

            scene s629a
            with dissolve

            u "Ugh, it's not a date..."

            scene s629
            with dissolve

            ri "*Chuckles* Okay, [name]. Byyye."

            scene s629a
            with dissolve

            u "Bye, Riley."

        else:
            scene s629a
            with dissolve

            u "She's in my history class."

            scene s629b
            with dissolve

            ri "Well enjoy your date."

            scene s629c
            with dissolve

            u "I'm not even sure it's a date, but thanks. See ya."

    else:
        u "I still haven't completed our economics assignment."

        scene s629b
        with dissolve

        ri "Oof, well good luck then. I'll see you later."

        scene s629c
        with dissolve

        u "Thanks, see ya."

    stop music fadeout 3

    if bowling: # Penelope bowling scene
        play music "music/m16punk.mp3"

        queue music [ "music/mchill1.mp3", "music/m7punk.mp3" ]
        scene s630 # you walking towards bowling
        with Fade (1,0,1)

        pause 1.0

        scene s631 # First person: Penelope sitting in front of Bowling alley
        with dissolve

        u "Hey, Penelope! How are you doing?"

        scene s632 # Closer, Penelope standing up
        with dissolve

        pe "Hey! I'm good, how are you?"

        scene s632a # Penelope close up mouth closed smiling
        with dissolve

        u "Excited to destroy you in bowling."

        scene s632
        with dissolve

        pe "I used to go bowling all the time with my dad, so you better watch out."

        scene s633 # First person penelope at the bowling panel
        with fade

        pe "What do you want your name to be?"

        $ bname = renpy.input("Choose your bowling name:", default=name) or name

        scene s634a # Penelope turns around and looks at you mouth closed smile
        with dissolve

        u "Make it [bname]."

        scene s634b # penelope sarcastic / annoyed smile mouth open
        with dissolve

        if bname == name:
            pe "Wow, how creative..."

        else:
            pe "What a name..."

        scene s634c
        with dissolve

        u "What's your name gonna be?"

        scene s634d # penelope thinking eyes up, saying hmmm
        with dissolve

        pe "Hmmm..."

        scene s634e # penelope # turns around to type
        with dissolve

        pe "Pim Kossible."

        scene s635 # Penelope walking towards bowling ball holder
        with dissolve

        u "Pim Kossible? Like from the TV show?"

        scene s635a # Penelope looking at you hopeful, talking while picking up a bowling ball
        with dissolve

        pe "She was my hero when I was younger, I always wanted to be like her."

        scene s635b # Penelope picked up a bowling ball
        with dissolve

        pe "Saving the world, all these incredible technical gadgets and she was always so cool about it."

        scene s635c
        with dissolve

        u "Wasn't she the one with the naked mole-rat?"

        scene s635b
        with dissolve

        pe "You mean Furrus? He was so cute."

        pe "And surprisingly helpful in most of their missions."

        scene s635c
        with dissolve

        u "Have you ever seen a naked mole-rat in real life? I don't think you'd think they're cute anymore."

        scene s635c
        with dissolve

        pe "Yeah, but that doesn't mean they can't be cute in the show."

        scene s636 # penelope walking to throw
        with dissolve

        pause 0.5

        scene s637 # Penelope thorws horribly
        with dissolve

        pause 0.5

        # bowling ball soundssss all scene

        scene s638 # ball goes into side thing
        with vpunch

        u "*Laughs* Oh god, I thought you used to go bowling all the time?"

        scene s639 # Penelope turns around a bit embarrassed
        with dissolve

        pe "I'm just a bit rusty."

        scene s639a
        with dissolve

        u "Let me show you how it's done."

        scene s640 # Mc throws bowling ball
        with dissolve

        pause 0.5
        play sound "sounds/strike.mp3"
        scene s641 # hits 7 or so pins
        with vpunch

        u "That was just a warm up throw."

        # Montage of different penelope throws, all horrible

        scene s642
        with Dissolve(2)

        pause 0.5

        scene s643
        with Dissolve(2)

        pause 0.5

        scene s637
        with Dissolve(2)

        pause 0.5

        # montage of the ball hitting the alley

        scene s644
        with vpunch

        pause 0.5

        scene s645
        with vpunch

        pause 0.5

        scene s638
        with vpunch

        pause 0.5

        scene s646 # Opening you and Penelope sitting down in the couch area
        with Dissolve(2)

        pause 0.5

        scene s647 # close up Penelope sitting across from you drinking from straw
        with dissolve

        u "Okay, something doesn't add up."

        scene s647a # Penelope puts drink down and looks at you curious
        with dissolve

        u "You said you used to go bowling all the time with your dad..."

        u "But I just don't think it's possible to unlearn something this much."

        u "You have barely hit any pins the entire game."

        scene s647b # penelope confession, slightly embarrassed
        with dissolve

        pe "When I was in 8th grade, I met this boy, James."

        pe "He was super nice and he wouldn't pick on me like some of the others."

        scene s647d # slightly differnet expression a bit more tense
        with dissolve

        pe "At some point he invited me to play foosball with him at his house."

        pe "So I went with him and we played, game after game."

        pe "Turns out, I was a natural at foosball and I beat him. Everytime."

        scene s647e
        with dissolve

        u "*Laughs* So what happened?"

        scene s647d
        with dissolve

        pe "At some point he started accusing me of cheating and he kicked me out."

        pe "He never wanted anything to do with me after that."

        pe "So now, I make sure that when I'm on a date, the guy wins every game."

        scene s647e
        with dissolve

        u "Okay, that's a nice story, but I don't buy it."

        u "You're telling me if you tried to win you'd just beat me easily? No way."

        scene s635 # penelope stands up and walks towards the bowling balls
        with dissolve

        pause 0.5

        scene s635a # she grabs a bowling ball
        with dissolve

        pe "Are you sure?"

        scene s636
        with dissolve

        pause 0.5

        scene s650 # she throws perfectly
        with dissolve

        pause 0.5

        play sound "sounds/strike.mp3"

        scene s651 # all pins knocked down
        with vpunch

        pause 0.5

        scene s652 # She walks back smiling
        with dissolve

        u "Holy shit."

        scene s653 # Penelope closer, standing in front of you, blushing
        with dissolve

        pe "Heehee. I guess I was telling the truth."

        scene s654 # Opening: you and penelope sitting at th bowling bar, mc looking at penelope, while she's looking at her drink
        with fade

        u "You're full of surprises, you know?"

        scene s655 # close up penelope smiling while drinking, glancing at you
        with dissolve

        pause 0.5

        u "Talking about surprises, are you ever gonna tell me what you got kicked out of your old college for?"

        scene s655c # penelope turns her head towards you in a bit sad and annoyed, mouth closed
        with dissolve

        pause 0.5

        scene s655b # mouth open
        with dissolve

        pe "Okay. But you can't tell anyone."

        scene s655c
        with dissolve

        u "Of course."

        scene s655b
        with dissolve

        pe "Uhm.. okay so I... I hacked into the school's system and changed some of the grades."

        scene s655c
        with dissolve

        u "Wait you hacked into your school to improve your grades? Come on that's hilarious."

        scene s655b
        with dissolve

        pe "Not my grades. My best friend Jenny's."

        pe "She was going through a rough time, dealing with some substance abuse, and therefore, didn't hand in some of her assignments on time..."

        pe "Her teacher was gonna fail her."

        pe "So she begged me to help her and I... I changed her grade so she'd pass."

        scene s655c
        with dissolve

        u "Why didn't you just tell me? That's honestly so awesome that you did that for your friend."

        scene s655d #penelope anxious
        with dissolve

        pe "Because that's not what I got kicked out for."

        pe "When they found out what happened, Jenny came forward and said she did it all by herself."
        pe "She told me I shouldn't pay the price for her mistakes."

        scene s655f # penelope upset
        with dissolve

        pe "But then, after she got kicked out, the principal started making her the face of the college's anti substance abuse campaign."

        pe "Without even asking her... how could they do that?"

        pe "So... I decided the hack into the college's website and photoshopped the principal's face onto all of the substance abuse pictures they used."

        scene s655h # Penelope looks away for a second taking a deep breath
        with dissolve

        pe "*Takes a deep breath*"

        scene s655f
        with dissolve

        pe "Turns out the principal had nothing to do with Jenny's pictures being used... it was her parents' idea."

        pe "They didn't want what happened to her to happen to anyone else."

        pe "So I came forward and got expelled."

        scene s655g
        with dissolve

        u "Oh god, Penelope... I had no idea..."

        scene s655b
        with dissolve

        pe "Can we please just stop talking about it?"

        scene s655c
        with dissolve

        u "Uhm yeah, of course."

        scene s656 # OpeningL Mc and Penelope walking back in the evening
        with fade

        pause 0.5

        scene s657 # you and Penelope in front of her dorm
        with dissolve

        u "I had a great time today. We should do this again sometime."

        scene s658 # Close up penelope smiling
        with dissolve

        pe "Yeah, but next time you're the one sharing all of your past."

        scene s658a
        with dissolve

        u "*Chuckles* If you insist."

        menu:
            "Kiss her":
                if lauren.relationship >= Relationship.GIRLFRIEND:
                    $ add_point(KCT.TROUBLEMAKER)
                    $ add_point(KCT.BRO)
                else:
                    $ add_point(KCT.BOYFRIEND)

                scene s658k
                with dissolve

                pause 0.5

                play sound "sounds/kiss.mp3"

                scene s658l
                with dissolve

                pause 1.0

                scene s658k
                with dissolve

                pause 0.5

                scene s658a # penelope blushing and smiling mouth closed
                with dissolve

                $ grant_achievement("strike")
                    
                pe "*Giggles*"

                u "That was nice..."

                scene s658
                with dissolve

                pe "Yes it was..."

                scene s658a
                with dissolve

            "Say Goodbye":
                if lauren.relationship >= Relationship.GIRLFRIEND:
                    $ add_point(KCT.BOYFRIEND)

        u "I gotta go now and get ready for the Wolves' party, but I'll see you soon, okay?"

        scene s658
        with dissolve

        pe "Yeah, no worries. See you soon."

    else: # transition to evening
        scene s659 # mc working on his desk transtion
        with Fade (1,0,1)

        pause 1.0

    label readywolf: #for compatibility only
    stop music fadeout 3
    play music "music/m6punk.mp3"

    if imre.relationship <= Relationship.MAD:
        scene s660 # Mc getting ready for the party by himself
        with Fade (1,0,1)

        u "(Alright, I'm ready for the party.)"
        u "(Wonder how it's gonna be seeing Imre there...)"

        scene s661 # Mc walking to party by himself
        with fade

        pause 0.5

        if joinapes:
            play sound "sounds/swoosh.mp3"
            scene s581g
            with flash

            gr "Join the Apes and I promise you, everyone at San Vallejo will know who you are within weeks."

            scene s581f
            with dissolve

            gr "So what do you say?"

            scene s581g
            with dissolve

            u "Okay, I'm in."

            scene s582 # Interaction: Grayson and you do a bro hand shake
            with dissolve
            # handshake clap sound

            gr "That's what I'm talking about!"

        elif meetgrayson:
            play sound "sounds/swoosh.mp3"
            scene s581g
            with flash

            gr "Join the Apes and I promise you, everyone at San Vallejo will know who you are within weeks."

            scene s581f
            with dissolve

            gr "So what do you say?"

            scene s581g
            with dissolve

            u "Sorry, Grayson. But I don't wanna be an Ape."

            scene s581h # Grayson angry
            with dissolve

            gr "What? What do you mean you don't wanna be an Ape?!"

        else:
            jump wolvesfr

        play sound "sounds/swoosh.mp3"
        scene s661 # Mc walking to party by himself
        with flash

        u "(Hopefully that was the right decision...)"

    else:
        scene s662 #MC and Imre are getting ready in the dorm. Imre looks excited.
        with Fade (1,0,1)

        pause 0.5

        scene s663 # close up Imre excited
        with dissolve

        imre "This is gonna be the best night of the year, I'm telling you."

        scene s663a
        with dissolve

        u "You sure about that?"

        scene s663
        with dissolve

        imre "Yeah, this is the frat you wanna be a part of. This party is gonna be insane."

        scene s663a
        with dissolve

        u "I bet."

        scene s663
        with dissolve

        imre "Not only are we gonna meet all the Wolves, but there are gonna be some feisty mamacitas."

        scene s663a
        with dissolve

        u "*Laughs* Feisty mamacitas? Seriously?"

        scene s663
        with dissolve

        imre "Excuse me for being a man of culture."

        imre "You ready to go?"

        scene s663a
        with dissolve

        u "Yeah, let's go."

        scene s664 # Walking with imre to the party
        with fade

        pause 0.5

        if meetgrayson and joinapes:
            play sound "sounds/swoosh.mp3"
            scene s581g
            with flash

            gr "Join the Apes and I promise you, everyone at San Vallejo will know who you are within weeks."

            scene s581f
            with dissolve

            gr "So what do you say?"

            scene s581g
            with dissolve

            u "Okay, I'm in."

            scene s582 # Interaction: Grayson and you do a bro hand shake
            with dissolve
            # handshake clap sound

            gr "That's what I'm talking about!"

        elif meetgrayson:
            play sound "sounds/swoosh.mp3"
            scene s581g
            with flash

            gr "Join the Apes and I promise you, everyone at San Vallejo will know who you are within weeks."

            scene s581f
            with dissolve

            gr "So what do you say?"

            scene s581g
            with dissolve

            u "Sorry, Grayson. But I don't wanna be an Ape."

            scene s581h # Grayson angry
            with dissolve

            gr "What? What do you mean you don't wanna be an Ape?!"

        else:
            play sound "sounds/swoosh.mp3"
            scene s501d
            with flash

            gr "So forget the Wolves, join the Apes."

            scene s502 # Grayson walking past you, looking at you
            with dissolve

            gr "Have a think about it and then meet me at midnight on the front stairs."

            scene s573a # mc looks at his phone (you can only see the bakc of the phone)
            with flash

            u "(Grayson said I should meet him, but how can I trust him after everything that happened?)"

            scene s574 # First person: Looking at the door
            with dissolve
            u "(Fuck Grayson, I'm not meeting him.)"

        play sound "sounds/swoosh.mp3"
        scene s664
        with flash

        u "(Hopefully that was the right decision...)"

        scene s664a
        with dissolve

        u "Imre, do you know the President of the Apes?"

        scene s665 # Closeup imre looking at you curious
        with dissolve

        imre "Who? Grayson?"

        scene s665a
        with dissolve

        u "Yeah, I think that's his name."

        scene s665
        with dissolve

        imre "You mean the guy that punched you in the face? He's an asshole. Why?"

        imre "You thinking about joining the Apes?"

        scene s665a
        with dissolve

        u "What? No!"

        scene s665b # Imre joking smile
        with dissolve

        imre "*Laughs* Calm down, I'm just kidding man."

        imre "I know you'd never join the Apes."

        scene s665d # Imre determined

        imre "You know why? Cause you're not a fucking asshole."

        imre "You have honor and loyalty and you're a good friend."

        imre "Apes don't have any of that shit."

        scene s665e
        with dissolve

        if joinapes:
            u "Right..."

        else:
            u "Thanks man."

        u "I was just uhm... wondering."

        scene s666 # From behind: Imre and mc arrive the Frat house, you can see Aaron talking to two girls
        with fade

        u "Holy shit..."

        imre "This is where dreams come true."

        scene s667 # First personL Aaron turns around and notices Imre and waves
        with dissolve

        pause 0.5

        scene s667a #Aaron walks towards Imre
        with dissolve

        aa "Hey bro, what's up?"

        scene s668 # Imre close up from the side smiling
        with dissolve

        imre "Sup man? You already working something?"

        scene s669 # aaron close up smiling looking at imre
        with dissolve

        aa "*Chuckles* Trying to."

        scene s668
        with dissolve

        imre "I see there's two... big plans or are you saving one for me?"

        scene s669
        with dissolve

        aa "Dude, I got you. You even get to choose."

        scene s668b # Imre looking at you pointing at Aaron
        with dissolve

        imre "Hahaha, this man knows how to be a bro!"

        scene s669b # Aaron looking at you
        with dissolve

        aa "Oh sorry, didn't introduce myself. I'm Aaron. Vice President of the Wolves. Nice to meet you."

        scene s669c
        with dissolve

        u "I'm [name], Imre's roommate. Nice to meet you too."

        u "You guys know each other long?"

        scene s668d # Imre looking at you smiling
        with dissolve

        imre "Funny story actually. You remember that girls' volleyball game where I kinda hid in the girls' lockerroom afterwards?"

        imre "Aaron was seated next to me at the game."

        scene s669a
        with dissolve

        u "Oh, so you like volleyball, Aaron?"

        scene s669d # aaron looking at you confused
        with dissolve

        aa "What? Hell no. I was there for the tushies."

        scene s669e
        with dissolve

        u "Wow, you guys really are a match made in heaven then."

        scene s669
        with dissolve

        aa "So Imre, you want me to introduce you to my two new friends?"

        scene s668
        with dissolve

        imre "Hell yeah."

        scene s668d
        with dissolve

        imre "[name], you don't mind if I go, do you?"

        scene s668e
        with dissolve

        u "No, not at all. Enjoy."

        scene s668
        with dissolve

        imre "Alriiight! Lead the way, Aaron."

        scene s668f # Imre gone
        with dissolve

        u "(Okay, I guess I'm on my own.)"

        jump wolvesfr2

label wolvesfr:
    scene fr3gardenopening
    with dissolve

    u "(Time to check out this party.)"

### WOLVES RUSH PARTY FREE ROAM freeroam3 freeroam 3 free roam 3
label wolvesfr2:
    play music "music/mparty2.mp3"

    queue music [ "music/mparty3.mp3", "music/mparty4.mp3"]

    #### room labels Navigation:
    call screen v6_fr3garden


# Ground floor~
# location 1- In front of wolves frat house:
# *Clicking on Josh & Kim*
label v6_fr3josh1:
    $ freeroam3.add("josh")

    scene sfr3jo1 # opening: josh and kim sitting on porch super high, with some filled and some empty shots on the ground

    jo "I could go for another right now."

    scene sfr3jo2 #closeup kim talking to josh
    with dissolve

    ki "I don't mind another."

    scene sfr3jo2a
    with dissolve

    u "Hey what's up guys?"

    scene sfr3jo2c # kim looking at you mouth closed
    with dissolve

    pause 0.5

    u "Damn, you guys are pretty high huh?"

    scene sfr3jo3 #close up josh talkign to you chill
    with dissolve

    jo "Maybe."

    scene sfr3jo2b
    with dissolve

    ki "Wanna hit?"

    scene sfr3jo2c
    with dissolve

    u "Nah, I'm good."

    scene sfr3jo3
    with dissolve

    jo "Then at least have a shot with us."

    scene sfr3jo3a
    with dissolve

    menu:
        "Take the shot":
            $ add_point(KCT.BRO)
            $ takeshot = True

            u "Fuck it. Why not."

            scene sfr3jo4
            with dissolve

            pause 0.5

            scene sfr3jo2b
            with dissolve

            ki "Attaboy."

            scene sfr3jo3b # josh laughs
            with dissolve

            jo "Yes, G!"

            scene sfr3jo3c
            with dissolve

        "Decline":
            $ add_point(KCT.BOYFRIEND)

            u "Nah, I'm good."

            scene sfr3jo3d
            with dissolve

            pause 0.5

            scene sfr3jo3f # josh dissapointed
            with dissolve

            jo "You're weak."

            scene sfr3jo3g
            with dissolve

            u "Sorry, gonna start off easy with a beer or something."

            scene sfr3jo3f
            with dissolve

            jo "Alright."

            scene sfr3jo3g
            with dissolve

    u "So, what are you guys doing here?"

    scene sfr3jo3
    with dissolve

    jo "Checking out the Wolves. Just wanna see what the fuzz is all about, you know."

    jo "Maybe join if they're cool."

    scene sfr3jo3a
    with dissolve

    u "Right."

    scene sfr3jo2d # kim annoyed
    with dissolve

    ki "I'm only here 'cuz Amber convinced me."

    scene sfr3jo2e
    with dissolve

    u "Amber's here too? How'd she convince you?"

    scene sfr3jo2d
    with dissolve

    ki "She said there'd be a lot of hot guys here, but right now all I see is you."

    scene sfr3jo3b
    with dissolve

    jo "*Laughs*"

    scene sfr3jo3c
    with dissolve

    u "*Deep breath* Okay, ouch. That felt a little unnecessary, not gonna lie."

    scene sfr3jo3
    with dissolve

    jo "Aww, don't get offended, bro. You know she means well."

    scene sfr3jo3a
    with dissolve

    u "How could that possibly be meant well?"

    u "Anyway, you guys know where Amber is?"

    scene sfr3jo2b
    with dissolve

    ki "Off somewhere inside."

    scene sfr3jo2c
    with dissolve

    u "Alright, I'll probably go inside too. See you guys later."

    scene sfr3jo3
    with dissolve

    jo "Bye G."

    call screen v6_fr3garden


label v6_fr3josh2:
    scene fr3garden

    u "(I already talked to them, not sure I'm down for more Kim right now.)"

    call screen v6_fr3garden


#Location 2: living room
#*Clicking on Guy & Guy*
#Two guys sit on a couch arguing.
label v6_fr3guy1:
    $ freeroam3.add("peter")

    scene sfr3guy1 #showing guy 1 and guy 2 on the couch having a discusison

    guya "Kourtney is way more beautiful than Kylie."

    scene sfr3guy2 # guy 2 closeup
    with dissolve

    guyb "How could you say that? Kylie is definitely the hottest of them all."

    scene sfr3guy3 # guy 1 closeup
    with dissolve

    guya "You're crazy."

    scene sfr3guy2b # guy 2 turns towards you
    with dissolve

    guyb "Ask this guy. He'll know."

    scene sfr3guy2c
    with dissolve

    u "What?"

    scene sfr3guy3b # guy 1 looking at you
    with dissolve

    guya "Who's hotter, Kourtney or Kylie?"

    scene sfr3guy3c
    with dissolve

    u "Like the Kardashians?"

    scene sfr3guy3b
    with dissolve

    guya "Yeah, duh."

    scene sfr3guy2
    with dissolve

    guyb "Definitely Kylie."

    scene sfr3guy2c
    with dissolve

    menu:
        "Kylie":
            $ add_point(KCT.BRO)

            u "Yeah I agree, Kylie's way hotter."

            scene sfr3guy2d # guyb excited
            with dissolve

            guyb "Exactly!"

            scene sfr3guy3d  # guya mad
            with dissolve

            guya "What? Why?"

            scene sfr3guy3e
            with dissolve

            u "Kylie has a body. And her face is way better."

            scene sfr3guy2d
            with dissolve

            guya "Yeah, because all the work done."

            scene sfr3guy2e
            with dissolve

            u "Work done or not, she's hotter."

            scene sfr3guy2d
            with dissolve

            guyb "That's what I've been saying!"

            scene sfr3guy3
            with dissolve

            guya "Man, you guys are crazy. Kourtney's the only natural one."

            scene sfr3guy2
            with dissolve

            guyb "Keeping up with the Kardashians, season 18, episode 3."

            guyb "Tell me Kourtney looks anywhere near as hot as Kylie there."

            scene sfr3guy2a
            with dissolve

            u "Alright, I'ma leave you guys to it."

        "Kourtney":
            $ add_point(KCT.BOYFRIEND)

            u "Definitely Kourtney."

            scene sfr3guy3f # guy a rubbing it in
            with dissolve

            guya "See! Told you!"

            scene sfr3guy2f # guyb pissed looking at you
            with dissolve

            guyb "Hell nah."

            scene sfr3guy2g
            with dissolve

            u "Kourtney's the natural one. I prefer natural beauty all day."

            scene sfr3guy3h # guya looking happy at you
            with dissolve

            guya "My point exactly."

            scene sfr3guy2f
            with dissolve

            guyb "Man, who cares about natural beauty when that body is banging. Don't matter in bed."

            scene sfr3guy2g
            with dissolve

            u "Haha, I feel like natural also looks better naked."

            scene sfr3guy3h
            with dissolve

            guya "Yeah bud, just accept that Kourtney's hotter."

            scene sfr3guy2
            with dissolve

            guyb "Keeping up with the Kardashians, season two, episode 3."

            guyb "Tell me Kourtney looks anywhere near as hot as Kylie there."

            scene sfr3guy2a
            with dissolve

            u "Alright, I'ma leave you guys to it."

    call screen v6_fr3livingroom


label v6_fr3guy2:
    scene fr3livingroom

    u "(No way I'm getting dragged back into that argument.)"

    call screen v6_fr3livingroom


label v6_fr3aubrey1:
    #*If you click on Aubrey & Emily*
    $ freeroam3.add("aubrey")

    scene sfr3au1 # Opening : EMily and aubrey standing with beer bottle, Aubrey mouth open curious smile

    if not forgiveemily and aubrey.relationship < Relationship.FWB: #If you didn't forgive Emily and didn't have sex with Aubrey:
        au "Really?"

        scene sfr3au2 # Emily close up smiling
        with dissolve

        em "Yeah."

        scene sfr3au2a
        with dissolve

        u "Hey."

        scene sfr3au2c # Emily turns to you awkardly
        with dissolve

        pause 0.5

        scene sfr3au2b
        with dissolve

        em "Uhm... hey."

        scene sfr3au2c
        with dissolve

        u "So uhm..."

        pause 0.5

        scene sfr3au3 # close up aubrey looking at you emphatic
        with dissolve

        au "Well, this feels awkward. I can leave if you guys wanna talk."

        scene sfr3au3a
        with dissolve

        u "No, stay. I was just stopping by to say hi."

        scene sfr3au3
        with dissolve

        au "Oh, okay."

        scene sfr3au3a
        with dissolve

        u "Alright, I'ma go talk to some of the other people here. Bye..."

        scene sfr3au3
        with dissolve

        au "Okay, bye."

    elif not forgiveemily: #If you didn't forgive Emily and had sex with Aubrey:
        au "Really?"

        scene sfr3au2 # Emily close up smiling
        with dissolve

        em "Yeah."

        scene sfr3au3b # aubrey smiling at you
        with dissolve

        au "Oh hey."

        scene sfr3au3c
        with dissolve

        u "Hey Aubrey. Uhm... hey Emily."

        scene sfr3au2d # emily turns to you annoyed
        with dissolve

        em "Did you need something?"

        scene sfr3au2e
        with dissolve

        u "Just wanted to say hi to Aubrey."

        scene sfr3au2d
        with dissolve

        em "We were kind of in the middle of talking."

        scene sfr3au2e
        with dissolve

        u "Uhm... okay?"

        scene sfr3au3
        with dissolve

        au "Do you guys need to talk alone for a minute orrr-?"

        scene sfr3au3a
        with dissolve

        u "Nah, it's cool. Just saying hi, I'll go talk to some of the other people here."

    elif aubrey.relationship < Relationship.FWB: #If you slept with Emily and didn't sleep with Aubrey:
        au "Really?"

        scene sfr3au2
        with dissolve

        em "Yeah."

        scene sfr3au2a
        with dissolve

        u "Hey."

        scene sfr3au2f
        with dissolve

        em "Hi."

        scene sfr3au2g
        with dissolve

        u "You look good."

        scene sfr3au2h# emily flirting
        with dissolve

        em "Could say the same about you."

        scene sfr3au3f # aubrey  a bit weirded out smiling
        with dissolve

        au "Uhh, hi?"

        scene sfr3au3g
        with dissolve

        u "Oh, hey Aubrey."

        scene sfr3au3d
        with dissolve

        au "Sooo, Emily was just telling me you guys used to date."

        scene sfr3au3e
        with dissolve

        u "Yup. High school sweethearts."

        scene sfr3au2f
        with dissolve

        em "I was just telling Aubrey the story of how you asked me to senior prom."

        scene sfr3au2g
        with dissolve

        u "*Chuckles* Oh no, not that story."

        scene sfr3au2f
        with dissolve

        em "Why don't you like that story? It was so sweet."

        scene sfr3au3b
        with dissolve

        au "Yeah, I really didn't take you as the romantic type. But a whole banner in the entrance of the school?"
        au "I don't think anyone has ever given me such a grand gesture."

        scene sfr3au2c
        with dissolve

        u "What can I say? I was a hopeless romantic. *Laughs*"

        scene sfr3au2
        with dissolve

        em "When I saw it, I just started crying. It was the most amazing thing anyone's ever done for me."

        scene sfr3au3d
        with dissolve

        au "I mean it's definitely a lot, haha."

        scene sfr3au3e
        with dissolve

        menu:
            "Anything for a girl like that":
                $ add_point(KCT.BOYFRIEND)
                $ simp = True

                u "Anything for a girl like that..."

                scene sfr3au2g
                with dissolve

                em "You're too sweet."

                scene sfr3au3d
                with dissolve

                au "Oh god, think I'm gonna puke."

                scene sfr3au3e
                with dissolve

                u "*Laughs* Couldn't help myself. I was young and in love."

                scene sfr3au3d
                with dissolve

                au "Sure sounds like it."

                scene sfr3au3e
                with dissolve

                u "Anyways, I'ma check out the rest of this party."

                scene sfr3au2h
                with dissolve

                em "I hope we get to catch up some more later."

                scene sfr3au2j
                with dissolve

                u "*Chuckles* I'm sure we will."

            "What people do for pussy...":
                $ add_point(KCT.TROUBLEMAKER)
                $ add_point(KCT.BRO)
                $ simp = False

                u "What people do for pussy, am I right?"

                scene sfr3au2d
                with dissolve

                em "What?!"

                scene sfr3au3
                with dissolve

                au "*Laughs* It seems to have worked."

                scene sfr3au2k # emily looking pissed at aubrey
                with dissolve

                em "Aubrey!"

                scene sfr3au2l
                with dissolve

                u "I was just kidding, calm down Emily."

                scene sfr3au2d
                with dissolve

                em "You better have been."

                scene sfr3au2e
                with dissolve

                pause 0.5

                u "Uhm... anyway, I'ma check out the rest of this party. See you guys later."

    else: #If you slept with Emily and Aubrey:

        au "Really?"

        scene sfr3au2
        with dissolve

        em "Yeah."

        scene sfr3au3b
        with dissolve

        au "Oh hey."
        with dissolve

        u "Hey. Looking good, girls."

        scene sfr3au3d
        with dissolve

        au "Thank you."

        scene sfr3au2h
        with dissolve

        em "You too."

        scene sfr3au3d
        with dissolve

        au "Emily was just telling me some stories about you two from high school."

        scene sfr3au3e
        with dissolve

        u "Oh god. Which ones?"

        scene sfr3au3b
        with dissolve

        au "The one where you asked her to senior prom."

        scene sfr3au3c
        with dissolve

        u "*Chuckles* Oh no."

        scene sfr3au3b
        with dissolve

        au "A whole banner in the entrance of the school? What a grand gesture."

        scene sfr3au3c
        with dissolve

        u "It was nothing really."

        scene sfr3au2
        with dissolve

        em "When I saw it, I just started crying. It was the most amazing thing anyone's ever done for me."

        scene sfr3au3d
        with dissolve

        au "I mean it's definitely a lot, haha."

        scene sfr3au3e
        with dissolve

        menu:
            "I was in love":
                $ add_point(KCT.BOYFRIEND)
                $ simp = True

                u "What can I say? I was young and in love."

                scene sfr3au2f
                with dissolve

                em "*Chuckles* We both were."

                scene sfr3au3g
                with dissolve

                au "Mhm."

                scene sfr3au2f
                with dissolve

                em "Those were good times."

                scene sfr3au2g
                with dissolve

                u "Uh, yeah, yeah they were."

                scene sfr3au2f
                with dissolve

                em "So you here to check out the Wolves?"

                scene sfr3au2g
                with dissolve

                u "Yeah, just seeing what they're like. Plus a lot of my friends are here."

                u "Anyways, I'ma check out the rest of this party."

                scene sfr3au2f
                with dissolve

                em "I hope we get to catch up some more later."

                scene sfr3au2g
                with dissolve

                u "I'm sure we will."

                scene sfr3au3f
                with dissolve

                au "Byeee."

            "It was nothing":
                $ add_point(KCT.TROUBLEMAKER)
                $ add_point(KCT.BRO)
                $ simp = False

                u "Really, it was nothing. Was so long ago."

                scene sfr3au2f
                with dissolve

                em "Was still really sweet."

                scene sfr3au2g
                with dissolve

                u "Yeah, yeah. I know."

                scene sfr3au3d
                with dissolve

                au "Sooo, you here to check out the Wolves or the ladies tonight?"

                scene sfr3au3e
                with dissolve

                u "*Laughs* Maybe a bit of both."

                scene sfr3au2b
                with dissolve

                em "Wow."

                scene sfr3au2c
                with dissolve

                u "I'm kidding. Just tryin' to see what's up."

                scene sfr3au3d
                with dissolve

                au "Sure."

                scene sfr3au3e
                with dissolve

                u "Anyways, I'ma check out the rest of this party."

                scene sfr3au3d
                with dissolve

                au "I'm sure we'll get to catch up some more later."

                scene sfr3au3e
                with dissolve

                u "*Chuckles* I'd hope so."

    call screen v6_fr3livingroom


label v6_fr3aubrey2:
    scene fr3livingroom

    u "(I should check out other parts of the party as well.)"

    call screen v6_fr3livingroom


label v6_fr3dsbathroom:
    #locked door sound
    scene fr3bathroomdoor

    u "(Hmm... locked)"

    call screen v6_fr3middleroom


#LOcation 3: kitchen/ dining room
label v6_fr3matt1:
    $ freeroam3.add("matt")

    scene sfr3ma1 # close up matt looking at fridge

    u "Excuse me?"

    scene sfr3ma1b # looking at you
    with dissolve

    matt "Hehehe."

    scene sfr3ma1c
    with dissolve

    u "Uhm, what?"

    scene sfr3ma1b # looking at you
    with dissolve

    matt "Hehehe."

    scene sfr3ma1c
    with dissolve

    u "You know what? Nevermind."

    call screen v6_fr3kitchen


label v6_fr3matt2:
    scene fr3kitchen

    u "(I'm not going over there again.)"

    call screen v6_fr3kitchen


label v6_fr3chris1:
    $ freeroam3.add("chris")

    if fightadam: #If you fought Adam:
        scene sfr3ch1 # chris and guyc talking, chris back turned to you

        guyc "You serious man? I should've been there."

        scene sfr3ch1a
        with dissolve

        ch "Yeah bro! I'm telling you, it was crazy. Really crazy."

        u "Chris?"

        scene sfr3ch1c # chris turns around  guyc looks at you
        with dissolve

        guyc "Looks like you got a fan waiting for you. I'll catch up with you later."

        scene sfr3ch1d # guyc walking away, chris looking afteer him
        with dissolve

        ch "Yeah for sure."

        scene sfr3ch2 # chris close up smiling
        with dissolve

        ch "Hey, man. What's up?"

        scene sfr3ch2a
        with dissolve

        u "I don't know if you remember, but you told me to come see you at this party. You know, after I fought with Adam."

        scene sfr3ch2
        with dissolve

        ch "Of course I remember. I'm glad you could make it, I really think you'd make a great Wolf."

        if not winadam:
            scene sfr3ch2a
            with dissolve

            u "You do remember that he beat me up, right?"

            scene sfr3ch2b # chris determined
            with dissolve

            ch "What I remember is you standing up for your friend."

            scene sfr3ch2c
            with dissolve

            u "Thanks."

            scene sfr3ch2b
            with dissolve

        else:
            scene sfr3ch2a
            with dissolve

            u "Thanks."

            scene sfr3ch2b
            with dissolve

            ch "Beating up Adam like that, it's mad."

            scene sfr3ch2c
            with dissolve

            u "Yeah, but it was really a one time thing. I don't really know much about fighting."

            scene sfr3ch2b
            with dissolve

            ch "That just proves even more how much talent you have."

        ch "Look, I'm sure you got the same speech by Grayson."

        ch "Truth is, we're both looking for freshmen that show potential."

        scene sfr3ch2c
        with dissolve

        u "Yeah, I get that."

        scene sfr3ch2
        with dissolve

        ch "And if I was in your shoes, I'd think to myself that both the Wolves and the Apes seem to have a lot of similarities."

        scene sfr3ch2a
        with dissolve

        u "I guess."

        scene sfr3ch2b
        with dissolve

        ch "The one key difference is loyalty. The Apes will do anything to win, even if that means stepping on each other."

        ch "They don't have any honor. They don't have a code."

        ch "In the Wolves, loyalty and the brotherhood always comes first."

        ch "It's up to you which one you'd rather be a part of."

        if joinapes:
            scene sfr3ch2c
            with dissolve

            u "I don't know Chris... I'm not sure the Wolves are for me."

        else:
            scene sfr3ch2c
            with dissolve

            u "Loyalty and brotherhood definitely sounds better to me."

        scene sfr3ch2d # chris points at a guy
        with dissolve

        ch "You see that guy right there?"

        scene sfr3ch3 # showing Finn
        with dissolve

        u "Yeah?"

        ch "That's Finn. Used to be super shy, wouldn't talk to anyone. Hell, he never even had a girlfriend."

        ch "Look at him now, he chats up girls with ease. Knowing your brothers have your back no matter what really does wonders to your confidence."

        scene sfr3ch2d # chris points at another guy
        with dissolve

        ch "And you see that guy there? That's Peter."

        scene sfr3ch4 # showing Peter
        with dissolve

        ch "Peter was a whole 300 pounds when he joined. He's 180 now and one of the best fighters we got!"

        scene sfr3ch2b
        with dissolve

        ch "There's a whole lot of us. Harry, he got jumped, was traumatized from it. We got his back. Sebastian, Aaron, Marcus. The list goes on."

        if joinapes:
            scene sfr3ch2c
            with dissolve

            u "Uhm... okay."

        else:
            scene sfr3ch2c
            with dissolve

            u "That's really cool."

        scene sfr3ch2b
        with dissolve

        ch "My point is, that every single of these guys has a much better life since joining the Wolves."

        scene sfr3ch2c
        with dissolve

        u "Yeah, it does seem like it."

        scene sfr3ch2b
        with dissolve

        ch "I've got something else I wanna show you, once you've met everyone."

        ch "So have a look around and come talk to me once you're ready."

        scene sfr3ch2c
        with dissolve

        u "Okay, will do."

    else: #If you didn't fight Adam:

        scene sfr3ch1 # chris and guyc talking, chris back turned to you

        guyc "You serious man? I should've been there."

        scene sfr3ch1a
        with dissolve

        ch "Yeah bro! I'm telling you, it was crazy. Really crazy."

        u "Excuse me?"

        scene sfr3ch1c # chris turns around  guyc looks at you
        with dissolve

        guyc "Looks like a fresher needs your attention. I'll catch up with you later."

        scene sfr3ch1d # guyc walking away, chris looking afteer him
        with dissolve

        ch "Yeah for sure."

        scene sfr3ch2 # chris close up smiling
        with dissolve

        ch "Hey, what's up, man?"

        scene sfr3ch2a
        with dissolve

        u "Hey, I'm [name]. You're Chris, right? The Wolves' President?"

        scene sfr3ch2
        with dissolve

        ch "Yeah, that's me. You thinking of joining us?"

        if joinapes:
            scene sfr3ch2a
            with dissolve

            u "Uhm... I don't know."

        else:
            scene sfr3ch2a
            with dissolve

            u "Maybe, I'm thinking about it."

        scene sfr3ch2
        with dissolve

        ch "I assume you're still unsure about whether you're a better fit for the Wolves or the Apes, I get that."

        ch "At first glance, both the Wolves and the Apes seem to have a lot of similarities."

        scene sfr3ch2a
        with dissolve

        u "I guess."

        scene sfr3ch2b
        with dissolve

        ch "The one key difference is loyalty. The Apes will do anything to win, even if that means stepping on each other."

        ch "They don't have any honor. They don't have a code."

        ch "In the Wolves, loyalty and the brotherhood always comes first."

        ch "It's up to you which one you'd rather be a part of."

        if joinapes:
            scene sfr3ch2c
            with dissolve

            u "Uhm..."

        else:
            scene sfr3ch2c
            with dissolve

            u "Loyalty and brotherhood definitely sounds better to me."

        scene sfr3ch2d # chris points at a guy
        with dissolve

        ch "You see that guy right there?"

        scene sfr3ch3 # showing Finn
        with dissolve

        u "Yeah?"

        ch "That's Finn. Used to be super shy, wouldn't talk to anyone. Hell, he never even had a girlfriend."

        ch "Look at him now, he chats up girls with ease. Knowing your brothers have your back no matter what really does wonders to your confidence."

        scene sfr3ch2d # chris points at another guy
        with dissolve

        ch "And you see that guy there? That's Peter."

        scene sfr3ch4 # showing Peter
        with dissolve

        ch "Peter was a whole 300 pounds when he joined. He's 180 now and one of the best fights we got!"

        scene sfr3ch2b
        with dissolve

        ch "There's a whole lot of us. Harry, he got jumped, was traumatized from it. We got his back. Sebastian, Aaron, Marcus. The list goes on."

        if joinapes:
            scene sfr3ch2c
            with dissolve

            u "Uhm... okay."

        else:
            scene sfr3ch2c
            with dissolve

            u "That's really cool."

        scene sfr3ch2b
        with dissolve

        ch "My point is, that every single of these guys has a much better life since joining the Wolves."

        scene sfr3ch2c
        with dissolve

        u "Yeah, it does seem like it."

        scene sfr3ch2b
        with dissolve

        ch "Just ask them yourself. And once you've had a look around, let me know."

        ch "There's something else I wanna show you."

    call screen v6_fr3kitchen


label v6_fr3riley1: #If you click on Riley and finn*
    $ freeroam3.add("riley")

    scene sfr3ri1 #Riley and finn are sitting at the table talking.

    ri "Yeah, I agree. It seems like a reoccurring issue."

    scene sfr3ri1a
    with dissolve

    finn "Yeah, that's what it feels like-"

    u "Hey guys."

    scene sfr3ri2 # riley close up smiling
    with dissolve

    ri "Oh, hey [name]. How's your night?"

    if save == 0:
        play sound "sounds/swoosh.mp3"
        scene s596a # Mc tackles Lauren out of the guns aim
        with flash
        pause 0.5

    elif save == 1:
        play sound "sounds/swoosh.mp3"
        scene s592
        with flash
        pause 0.5

    elif save == 2:
        play sound "sounds/swoosh.mp3"
        scene s594
        with flash
        pause 0.5

    play sound "sounds/swoosh.mp3"
    scene sfr3ri2 # riley close up smiling
    with flash

    ri "[name]?"

    scene sfr3ri2a
    with dissolve

    u "Uh yeah, sorry. My night was good. What about yours?"

    scene sfr3ri2
    with dissolve

    ri "It's great so far."

    scene sfr3ri2b # riley loookig at finn
    with dissolve

    ri "This is my new friend Finn. Finn, this is [name]."

    scene sfr3ri3 # finn awkward and uncomfortable looking at you
    with dissolve

    finn "Hey."

    scene sfr3ri2
    with dissolve

    ri "So, how do you like the party?"

    scene sfr3ri2a
    with dissolve

    u "It's cool. I mean, it's no poetry slam."

    scene sfr3ri2
    with dissolve

    ri "*Laughs* Trueee!"

    scene sfr3ri2b
    with dissolve

    ri "Have you ever been to a poetry slam?"

    scene sfr3ri2c # finn looking at riley uncomfortable
    with dissolve

    finn "Uh.. No, I don't think so. I'm not really into that kinda stuff."

    scene sfr3ri2b
    with dissolve

    ri "I think you'd really enjoy it. [name] also wasn't sure about it beforehand."

    if perform == 0:
        scene sfr3ri2c
        with dissolve

        u "Yeah, it was really cool."

    else:
        scene sfr3ri2c
        with dissolve

        u "I mean, you did force me to go up on stage and perform myself..."

        scene sfr3ri2d # riley flirting at you
        with dissolve

        ri "And tell me that wasn't exciting?"

        scene sfr3ri2e
        with dissolve

        u "*Chuckles* It certainly was something new."

    menu:
        "Ask Riley something":
            $ add_point(KCT.BOYFRIEND)

            scene sfr3ri2a
            with dissolve
            #If you Ask Riley a Question:

            u "So, what are you doing here tonight? Didn't think you'd wanna fight with the boys?"

            scene sfr3ri2
            with dissolve

            ri "*Laughs* Not quite, but I love a good party and there's so many cool people you can meet here."

            ri "Have you meet Aaron? He was so friendly. He even offered me to walk me home at night."

            scene sfr3ri2a
            with dissolve

            u "Yeah... I feel like he might have ulterior motives."

            scene sfr3ri2d
            with dissolve

            ri "Not everyone's a walking sex robot, you know?"

            scene sfr3ri2c
            with dissolve

            finn "No, he definitely is."

            scene sfr3ri2b
            with dissolve

            ri "Alright guys, I'll just walk home all by myself and get kidnapped then."

            scene sfr3ri2c
            with dissolve

            u "*Chuckles* I'll walk you home."

            scene sfr3ri2d
            with dissolve

            ri "Oh, so you're saying you don't have ulterior motives?"

            scene sfr3ri2e
            with dissolve

            u "*Grins* I don't know what would make you think that."

            scene sfr3ri2
            with dissolve

            ri "*Laughs* Right, my bad."

            ri "You wanna sit down and have a beer with us?"

            scene sfr3ri2a
            with dissolve

            u "Maybe later, I still got some exploring to do."

            scene sfr3ri2a
            with dissolve

            ri "Okay, see you later then."

        "Ask Finn something":
            $ add_point(KCT.BRO)
            $ askfinn = True

            scene sfr3ri3a
            with dissolve

            u "So Finn, are you a Wolf?"

            scene sfr3ri3
            with dissolve

            finn "Oh.. uh.. yeah. Are you looking to join?"

            scene sfr3ri3a
            with dissolve

            u "Not sure yet."

            scene sfr3ri3d # finn comfortable
            with dissolve

            finn "Tough getting in, but once you're in, it's the best place to be."

            scene sfr3ri3c
            with dissolve

            u "Yeah, seems like what everyone is saying around here. You know Imre?"

            scene sfr3ri3d
            with dissolve

            finn "Imre... Oh, he's Bence's younger brother, right?"

            scene sfr3ri3c
            with dissolve

            u "Uhh... yeah, if Bence is the name of his older brother."

            u "He used to be a Wolf, right?"

            scene sfr3ri3d
            with dissolve

            finn "Yeah, I mean he's kind of a legend around here."

            finn "He was fight king two years in a row. It's crazy."

            scene sfr3ri3c
            with dissolve

            u "Wow... Imre's got big shoes to fill."

            scene sfr3ri3d
            with dissolve

            finn "We all do."

            scene sfr3ri2
            with dissolve

            ri "You wanna sit down and have a beer with us?"

            scene sfr3ri2a
            with dissolve

            u "Maybe later, I still got some exploring to do."

            scene sfr3ri2a
            with dissolve

            ri "Okay, see you later then."

    call screen v6_fr3kitchen


label v6_fr3riley2:
    scene fr3kitchen

    u "(I should look around more first.)"
    
    call screen v6_fr3kitchen


#location 4: Garage Gym
#*If you click on Guy #5 and Sebastian*
#Sebastian is guiding Guy #5 through some punches., they're both not wearing a shirt
label v6_fr3sebastian1:
    $ freeroam3.add("sebastian")

    scene sfr3se1 # sebestian teaching guyd how to fight

    se "You can't move your leg like that, you always need to keep your core stable."

    scene sfr3se1a
    with dissolve

    guyd "Ohhh... yeah, I always just wanna step forwards."

    scene sfr3se1b #Guy #5 swings a punch, but it's sloppy and looks weak.
    with vpunch

    se "You really got to put some power behind it."

    u "Hey guys."

    scene sfr3se2 # Close up sebastian
    with dissolve

    se "What's up? You wanna learn some moves too?"

    scene sfr3se2a
    with dissolve

    u "Haha, maybe later. Just checking out the garage. You got a real nice gym in here."

    scene sfr3se2
    with dissolve

    se "Yeah it's dope. And there's always someone training in here. It's so motivating."

    scene sfr3se2a
    with dissolve

    u "I'd imagine."

    scene sfr3se2
    with dissolve

    se "I'm Sebastian by the way. Second year Wolf."

    scene sfr3se2
    with dissolve

    u "I'm [name], nice to meet you."

    scene sfr3se3 # close up guyd exhausted
    with dissolve

    u "Are you a Wolf too?"

    scene sfr3se3a
    with dissolve

    guyd "No, not yet. But I'm definitely looking to pledge."

    scene sfr3se2b
    with dissolve

    se "He's here working on his technique instead of partying, I can already tell he's gonna be a good fit."

    scene sfr3se2c
    with dissolve

    u "It is impressive. Maybe I'll join you guys later."

    scene sfr3se2
    with dissolve

    se "Sounds good man, just let me know."

    scene sfr3se2a
    with dissolve

    u "Cool, will do."

    call screen v6_fr3garage


label v6_fr3sebastian2:
    scene fr3garage

    u "(Maybe I'll join them a bit later.)"

    call screen v6_fr3garage

label v6_fr3amber1:
    $ freeroam3.add("amber")

    scene sfr3am1 #Amber is sitting watching the guys workout and drinking a beer

    u "I see you enjoying the view."

    scene sfr3am2
    with dissolve

    am "Muscular guys working out without shirts is not the worst thing to look at."

    scene sfr3am2a
    with dissolve

    u "*Laughs* I guess it's not."

    scene sfr3am2b # amber flirting
    with dissolve

    am "So you gonna be one of them soon?"

    scene sfr3am2c
    with dissolve

    if joinapes:
        u "Okay, don't tell anyone, but I'm probably gonna join the Apes. I'm just here cause most of my friends are."

        scene sfr3am2b
        with dissolve

        am "Oh damn, so you're kinda infiltrating the enemy right now, huh?"

        scene sfr3am2c
        with dissolve

        u "Uhm... something like that."

    else:
        u "Yeah, maybe."

    scene sfr3am2b
    with dissolve

    am "I definitely wouldn't mind watching you work out without a shirt."

    scene sfr3am2c
    with dissolve

    menu:
        "You're such a tease":
            $ add_point(KCT.BRO)

            u "Wow. You're such a tease."

            scene sfr3am2b
            with dissolve

            am "Really? I think I'm pretty blunt."

            scene sfr3am2c
            with dissolve

        "Not gonna happen":
            $ add_point(KCT.BOYFRIEND)

            u "Mhhh... I don't think that's gonna happen."

            scene sfr3am2d # amber dissapointed
            with dissolve

            am "That's too bad."

            scene sfr3am2a
            with dissolve

    u "So uhm... why you not out there with Josh and Kim?"

    scene sfr3am2
    with dissolve

    am "Eh... they're just sitting outside smoking and it's annoying cause Josh is trying so hard to get into her pants."

    scene sfr3am2a
    with dissolve

    u "Really? I didn't even notice."

    scene sfr3am2
    with dissolve

    am "Yeah, he's always trying to get her attention and he just follows her everywhere."

    am "But to be honest, it might pay off at some point. Kim broke up with her boyfriend like 4 months ago and still hasn't fucked anyone since."

    am "At some point she's bound to get horny and then I guess it's about who's there first, haha."

    scene sfr3am2a
    with dissolve

    u "Huh. I guess it's not gonna be you, considering you're sitting here."

    scene sfr3am2
    with dissolve

    am "*Laughs* As much as I love Kim, I'd rather be doing something more interesting."

    scene sfr3am2a
    with dissolve

    u "Like what?"

    scene sfr3am2
    with dissolve

    am "Like watching a couple shirtless guys work out."

    scene sfr3am2a
    with dissolve

    u "*Laughs* Alright, I'll leave you to it then. See you later."

    scene sfr3am2
    with dissolve

    am "Bye bye."

    call screen v6_fr3garage


label v6_fr3amber2:
    scene fr3garage

    u "(I think I've heard enough about shirtless guys for now.)"

    call screen v6_fr3garage


#LOcation 5: lowered roof
#*If you click on Nora*
#Nora is sitting on the rooftop smoking. MC comes and sits down next to her.
label v6_fr3nora1:
    $ freeroam3.add("nora")

    scene sfr3no1 #Nora is sitting on the rooftop smoking. MC comes and sits down next to her.

    u "Why you up here all alone?"

    scene sfr3no1b # nora turns around not happy
    with dissolve
    pause 0.5

    scene sfr3no1a # nora turns around not happy
    with dissolve

    no "Uhm, guess I just wanted some air."

    scene sfr3no1b
    with dissolve

    u "Mind if I sit down?"

    scene sfr3no1a
    with dissolve

    no "Go ahead."

    scene sfr3no2 # close up nora looking towards the sky smoking
    with dissolve

    pause 0.5

    u "You okay?"

    scene sfr3no2a # nora blowing out smoke
    with dissolve

    pause 0.5

    scene sfr3no2b # nora looking forwards, mouth open no cigarette
    with dissolve

    no "Yeah... people just start to annoy me after a while."

    scene sfr3no2c # nora looking forwards, mouth closed no cigarette (no smoke)
    with dissolve

    u "Yeah, I get that. Parties can feel like a bit much sometimes."

    scene sfr3no2b
    with dissolve

    no "Exactly."

    scene sfr3no2c
    with dissolve

    pause 0.5

    u "So uhm... where's Chris?"

    scene sfr3no2d # nora looking at you  with no particular emotion maybe a little unhappy or annoyed
    with dissolve

    no "Downstairs talking to every person at this party I presume."

    scene sfr3no2e
    with dissolve

    u "You don't sound too happy about that."

    scene sfr3no2d
    with dissolve

    no "No, it's fine. It's just..."

    scene sfr3no2 # close up nora looking towards the sky smoking
    with dissolve

    pause 0.5

    scene sfr3no2a # nora blowing out smoke
    with dissolve

    pause 0.5

    scene sfr3no2d
    with dissolve

    no "Chris is always right in the middle of these parties. He has to talk to everyone, has to find new recruits, et cetera."

    scene sfr3no2b
    with dissolve
    no "So sometimes it can be a bit much."

    scene sfr3no2c
    with dissolve

    u "So it's like he's not giving you enough attention?"

    scene sfr3no2b
    with dissolve

    no "No, it's not that. I just want him to take a break once in a while and, you know, hang out with my boyfriend."

    scene sfr3no2f # nora a bit sad
    with dissolve

    no "But it's hard, because he's Wolves' President. And he's so dedicated and he cares so much and I love that about him."

    no "But... when you do as much for your frat as he does, there's very little time left for other things."

    scene sfr3no2g
    with dissolve

    u "Yeah, he's super passionate from what I've seen. I can see how that can make things hard."

    scene sfr3no2f
    with dissolve

    no "And I don't want him to be less passionate or anything... I just need a little bit of break once in a while."

    scene sfr3no2 # close up nora looking towards the sky smoking
    with dissolve

    pause 0.5

    scene sfr3no2a # nora blowing out smoke
    with dissolve

    pause 0.5

    scene sfr3no2b
    with dissolve

    no "That's why I come up here."

    scene sfr3no2c
    with dissolve

    u "It's nice... up here."

    scene sfr3no2b
    with dissolve

    no "Yeah... it is."

    scene sfr3no2 # close up nora looking towards the sky smoking
    with dissolve

    pause 0.5

    scene sfr3no2a # nora blowing out smoke
    with dissolve

    u "So uhm... anything else been on your mind?"

    scene sfr3no2h # nora cheeky smile at you
    with dissolve

    no "What are you? My therapist?"

    scene sfr3no2j
    with dissolve

    u "No, I don't think you could afford my hourly rate."

    u "But I'm here if you wanna talk."

    scene sfr3no2b
    with dissolve

    no "I don't think you'd want to hear me rant about your crush."

    scene sfr3no2c
    with dissolve

    u "My crush?"

    scene sfr3no2d
    with dissolve

    no "Chloe."

    scene sfr3no2e
    with dissolve

    u "Right..."

    u "You can tell me, I'm not gonna tell her."

    scene sfr3no2d
    with dissolve

    no "I'm not worried about you telling her, I just don't wanna deal with a white knight."

    scene sfr3no2e
    with dissolve

    u "A white knight?"

    scene sfr3no2d
    with dissolve

    no "Someone who's just gonna defend her every action cause she's pretty."

    scene sfr3no2e
    with dissolve

    u "I'm not a white knight, don't worry."

    scene sfr3no2 # close up nora looking towards the sky smoking
    with dissolve

    pause 0.5

    scene sfr3no2a # nora blowing out smoke
    with dissolve

    u "So are you gonna tell me what happened or not?"

    scene sfr3no2d
    with dissolve

    no "I told Chloe that I don't think she's been a good President for the Chicks and she started some drama."

    scene sfr3no2e
    with dissolve

    u "What'd she do for you to think she's not a good President?"

    scene sfr3no2d
    with dissolve

    no "It's not one particular thing. She's just... manipulative."

    no "She plays cute and innocent, but she knows exactly what she's doing."

    no "And she's using the Chicks to play her childish games with other people's feelings."

    no "It's not okay."

    scene sfr3no2 # close up nora looking towards the sky smoking
    with dissolve

    pause 0.5

    scene sfr3no2a # nora blowing out smoke
    with dissolve

    menu:
        "Defend Chloe":
            $ nora.relationship = Relationship.MAD
            $ add_point(KCT.BOYFRIEND)

            u "Chloe's not manipulative. She's just being bad mouthed because people like you see her as a threat."

            u "I mean, what kinda friend are you to feed into all the shit people say about her just because you're jealous that she's the President and you're not."

            scene sfr3no2k # nora pissed at you
            with dissolve

            no "Jealous??? You've got to be kidding me."

            no "I knew you'd turn into a white knight."

            no "If you don't think she's manipulative, then you're one of the people she's manipulated."

            scene sfr3no2b
            with dissolve

            no "Now go back inside and let me smoke in peace."

            scene sfr3no2
            with dissolve

            u "Fine. But you're wrong about Chloe."

        "Don't defend Chloe":
            $ add_point(KCT.BRO)

            u "Yeah, it sounds kinda messed up."

            u "I don't really know her like that."

            scene sfr3no2h
            with dissolve

            no "Well you're gonna find out soon, if you're trying to become her next boy toy."

            scene sfr3no2j
            with dissolve

            u "It's just... when I'm around her, you know..."

            u "She's different. She's honest and funny and just... amazing."

            scene sfr3no2 # close up nora looking towards the sky smoking
            with dissolve

            pause 0.5

            scene sfr3no2a # nora blowing out smoke
            with dissolve

            pause 0.5

            scene sfr3no2b
            with dissolve

            no "Yep, that's how she gets you."

            scene sfr3no2h
            with dissolve

            no "But hey, smarter guys than you have fallen for her."

            scene sfr3no2j
            with dissolve

            u "*Chuckles* Are you trying to say I'm stupid?"

            scene sfr3no2h
            with dissolve

            no "I'm trying to say you're not the only one."

            no "You can keep chasing her if you want, but..."

            scene sfr3no2b
            with dissolve

            no "Just know that... she's not always as honest and funny and amazing as she may seem."

            scene sfr3no2c
            with dissolve

            u "Thanks, Nora..."

            u "For looking out for me."

            scene sfr3no2 # close up nora looking towards the sky smoking
            with dissolve

            pause 0.5

            scene sfr3no2a # nora blowing out smoke
            with dissolve

            u "I'm gonna let you finish your cigarette in peace."

            scene sfr3no2h
            with dissolve

            no "Okay."

            scene sfr3no3 # first person looking at window back inside to the room
            with dissolve

            no "[name]."

            scene sfr3no1e # first person turning around looking at nora sitting
            with dissolve

            u "Yeah?"

            scene sfr3no1d # first person turning around looking at nora sitting
            with dissolve

            no "Thanks for listening."

            scene sfr3no1e
            with dissolve

            u "Anytime."

    call screen v6_fr3roofroom

label v6_fr3nora2:
    scene fr3roofroom

    u "(I should let Nora smoke in peace.)"

    call screen v6_fr3roofroom

#Location 6: bathroom
label v6_fr3chloe1:
    $ freeroam3.add("chloe")

    scene sfr3cl1 #in front of closed bathroom door

    "*Crying noises*"

    "*Sniff*"

    scene sfr3cl2 # you knock on door
    with dissolve

    # knock sounds

    "*Knock knock knock*"

    u "Hello? Are you okay?"

    scene sfr3cl1 #in front of closed bathroom door
    with dissolve

    cl "*Sniff* Who is it?"

    u "Chloe? It's me, [name]."

    if chloe.relationship <= Relationship.MAD:
        cl "*Sniff* Leave me alone."

        u "No, you're crying. I'm not just going to walk away. What happened?"

        cl "I said leave me alone. I don't want to talk to you."

        u "Chloe, just let me in. You can talk to me."

        cl "*Sniff* I don't want to talk to you."

        u "C'mon Chloe. You can trust me."

        cl "But you don't trust me."

        u "Chloe. Stop. Just let me help."

        if kct == "popular":
            call screen kct_popup

            cl "*Sniff* Okay..."

            $ chloe.relationship = Relationship.FRIEND

        else:
            cl "Please, just leave me alone, [name]."

            u "Fine..."

            call screen v6_fr3upstairs

    else:
        cl "Not right now, please."

        u "Chloe, I hear you crying. Just let me in."

        cl "*Sniff* I'm fine. Please. I need a minute."

        u "Chloe, I can hear that you're not fine. Just let me in. We can talk about whatever's bothering you."

        cl "Really, I'm okay!"

        u "Chloe. Please."

        cl "*Sniff* Okay..."

        $ chloe.relationship = Relationship.FRIEND

    # unlock sound

    "*Door unlocks*"

    # door open sound

    scene sfr3cl1a # chloe opens door sad, makeup after crying
    with dissolve

    cl "Hey..."

    scene sfr3cl3a # first person chloe sitting in bathroom in front of you
    with dissolve

    u "So what happened?"

    scene sfr3cl3
    with dissolve

    cl "Nothing, it's stupid."

    scene sfr3cl3a
    with dissolve

    u "Come on, please. Talk to me. I hate seeing you like this."

    scene sfr3cl3
    with dissolve

    cl "It's just... It's just... All the Chicks met today to discuss some stuff, like new recruits and budget, et cetera."

    cl "*Sniff* Then all of the sudden, Nora stands up and says that I'm not doing my job well and she wants me to step down as President."

    cl "I mean, I knew Nora didn't like me, but... she could have just told me in private, you know?"

    scene sfr3cl3b # chloe puts her hands in front of her face looking down
    with dissolve

    cl "*Crying* Oh god, I'm trying so hard to make everyone happy and people just keep attacking me."

    cl "*Crying* First Grayson, now Nora..."

    menu:
        "Maybe you should step down":
            $ add_point(KCT.BOYFRIEND)
            $ chloe.relationship = Relationship.MAD

            u "You ever think, maybe you should step down?"

            scene sfr3cl3d # chloe  aggressive
            with dissolve

            cl "What???"

            scene sfr3cl3e
            with dissolve

            u "You know maybe it's just a bit too stressful and you could always let someone else give it a shot."

            u "It'll definitely put less of a target on your back."

            scene sfr3cl3d # chloe
            with dissolve

            cl "Are you kidding me?"

            cl "That's your solution? Me losing everything I've worked for over the past 3 years?!"

            scene sfr3cl3e
            with dissolve

            u "I'm just trying to help and the pressure's obviously getting to you."

            scene sfr3cl3d
            with dissolve

            cl "The pressure's not getting to me. All the people trying to drag me down are."

            cl "And apparently you're one of those people."

            scene sfr3cl3e
            with dissolve

            u "Chloe, I-"

            scene sfr3cl3d
            with dissolve

            cl "Just get out."

            scene sfr3cl3e
            with dissolve

            u "I'm just trying to help."

            scene sfr3cl3e
            with dissolve

            cl "I said get out! Leave me alone."

            scene sfr3cl3d
            with dissolve

            u "Fine..."

        "Nora's being stupid":
            $ add_point(KCT.BRO)
            $ add_point(KCT.TROUBLEMAKER)

            u "Nora's being stupid. You're a great President. You're smart, you're driven and you care so much..."

            u "She's probably just jealous."

            scene sfr3cl3f # hopeful smile
            with dissolve

            cl "You think so?"

            scene sfr3cl3g
            with dissolve

            u "I know so. And just because one girl doesn't like you, doesn't mean you have to give it all up for her."

            u "I mean what does she know?"

            scene sfr3cl3
            with dissolve

            cl "But what about the other girls? What if she starts getting them to agree with her?"

            scene sfr3cl3a
            with dissolve

            u "They won't agree with her. Chloe you're an amazing person and leader. And all of the girls can see that."

            scene sfr3cl3h # chloe sad smile
            with dissolve

            cl "Thank you. I needed to hear that."

            scene sfr3cl4 # showing chloe and you from the side
            with dissolve

            pause 0.5

            play sound "sounds/kiss.mp3"

            scene sfr3cl4a # chloe gives you a quick kiss
            with dissolve

            pause 1.0

            scene sfr3cl4
            with dissolve

            pause 0.5

            scene sfr3cl3j
            with dissolve

            u "*Grins* What was that for?"

            scene sfr3cl3h
            with dissolve

            cl "Just a little token of my gratitude."

            scene sfr3cl3j
            with dissolve

            u "*Chuckles*"

            scene sfr3cl3h
            with dissolve

            cl "I'm gonna clean up before I go back out."

            scene sfr3cl3j
            with dissolve

            u "Of course. I'll give you some space. Let me know if you need some more words of encouragement later."

            scene sfr3cl3h
            with dissolve

            cl "Thank you."

            scene sfr3cl3j
            with dissolve

            u "Of course."

    #door closing sound
    call screen v6_fr3upstairs


label v6_fr3chloe2:
    scene fr3upstairs

    u "(I should give her some space.)"

    call screen v6_fr3upstairs


#Location 7: office
#MC walks into an empty office.
label v6_fr3office:
    scene fr3office

    if not "office" in freeroam3:
        u "(This must be Chris' office.)"

        u "(It's filled with all of these historic Wolves' relics.)"

    $ freeroam3.add("office")
    
    if relics == 4:
        jump fr3relics
    else:
        call screen v6_fr3office


label v6_fr3picture:
    $ relics += 1

    #*If you click on a photo on the wall*
    #MC sees an old picture of the wolves.
    scene sfr3picture # close up photo with Imre's older brother

    u "An old picture of the Wolves..."

    u "That must be Imre's older brother. They do look alike."

    if relics == 4:
        jump fr3relics
    else:
        call screen v6_fr3office


label v6_fr3trophies:
    $ relics += 1

    scene sfr3trophies # close up of 7 trophies

    u "(Seven summer showdown trophies...)"

    u "(Imre said they only won five out of the last ten so this competition must have been going on for over ten years.)"

    u "(That's crazy...)"

    if relics == 4:
        jump fr3relics
    else:
        call screen v6_fr3office


#*If you click on the certificate on the wall*
#MC looks at the certificate on the wall. It reads: Wolves Fraternity 1976.
label v6_fr3certificate:
    $ relics += 1

    scene sfr3certificate # close up of ceritifcate

    u "Wow. This frat has been around for decades."

    if relics == 4:
        jump fr3relics
    else:
        call screen v6_fr3office

#*If you click on the book shelf*
#MC walks to the book shelf and looks at the row of books.
label v6_fr3books:
    $ relics += 1

    scene sfr3books # close up of bookshelf

    u "I doubt any of these guys actually read any of these. Haha."

    if relics == 4:
        jump fr3relics
    else:
        call screen v6_fr3office


label fr3relics:
    $ relics += 1
    scene fr3office

    u "(Empty room... All alone. This'd be the perfect place for some alone time with a girl... I should ask someone. Haha.)"

    u "(Who to ask though?)"

    if "chloe" in freeroam3 and "nora" in freeroam3:
        u "(Definitely not Chloe or Nora, they both seem too caught up in their fight.)"

    elif "chloe" in freeroam3:
        u "(Definitely not Chloe, she seems too caught up in her fight with Nora.)"

    elif "nora" in freeroam3:
        u "(Definitely not Nora, she seems too caught up in her fight with Chloe.)"

    call screen v6_fr3office

#looking for a girl
#*If you click on Aubrey*
#If you didn't have sex:
#MC walks up to Aubrey.
label v6_fr3aubrey3:
    scene sfr3au1

    menu:
        "Ask Aubrey":
            if not "aubrey" in freeroam3asked:
                $ freeroam3asked.add("aubrey")

                u "Hey, Aubrey, can I talk to you for a second?"

                scene sfr3au3b
                with dissolve

                au "Oh, hey you. Sure, what's up?"

                scene sfr3au3c
                with dissolve

                u "You wanna go upstairs and check out the Wolves' office?"

                if aubrey.relationship >= Relationship.FWB:
                    $ upstairs = "aubrey"

                    scene sfr3au3d
                    with dissolve

                    au "Right now?"

                    scene sfr3au3e
                    with dissolve

                    u "Yeah, if you want."

                    scene sfr3au3d
                    with dissolve

                    au "Okay, sure let's go."

                    jump upstairsaubrey

                elif simp:
                    scene sfr3au3f
                    with dissolve

                    au "Right now?"

                    scene sfr3au3g
                    with dissolve

                    u "Yeah, if you want."

                    scene sfr3au3f
                    with dissolve

                    au "I don't know, maybe later. I'm really enjoying the party down here."

                    scene sfr3au3g
                    with dissolve

                    u "Oh okay."

                else:
                    $ upstairs = "aubrey"

                    scene sfr3au3b
                    with dissolve

                    au "Right now?"

                    scene sfr3au3c
                    with dissolve

                    u "Yeah, if you want."

                    scene sfr3au3b
                    with dissolve

                    au "Okay, sure let's go."

                    jump upstairsaubrey

            else:
                u "(I've already asked Aubrey.)"

        "Ask Emily":
            $ freeroam3asked.add("emily")

            if forgiveemily:
                $ upstairs = "emily"

                u "Hey Emily, can I talk to you for a second?"

                scene sfr3au2f
                with dissolve

                em "Of course. What's up?"

                scene sfr3au2g
                with dissolve

                u "You wanna go upstairs? There's an empty room."

                u "We could have some alone time..."

                scene sfr3au2h
                with dissolve

                em "Oooh, that does sound good. Lead the way."

                jump upstairsemily

            else:
                u "(No way I'm asking Emily.)"

    call screen v6_fr3livingroom


#*If you click on Amber*
#MC walks up and sits next to Amber.
label v6_fr3amber3:
    $ freeroam3asked.add("amber")

    scene sfr3am1

    u "Hey."

    scene sfr3am2
    with dissolve

    am "Yes?"

    scene sfr3am2a
    with dissolve

    u "Bored from watching these guys yet?"

    scene sfr3am2b
    with dissolve

    am "Not in the slightest. Why?"

    scene sfr3am2c
    with dissolve

    u "Just thought maybe you wanna go upstairs. You know, talk somewhere quiet."

    if kct == "popular":
        call screen kct_popup
        $ upstairs = "amber"

        scene sfr3am2b
        with dissolve

        am "Hm, go somewhere alone with you that's quiet?"

        scene sfr3am2c
        with dissolve

        u "Exactly."

        scene sfr3am2b
        with dissolve

        am "Will there be entertainment?"

        scene sfr3am2c
        with dissolve

        u "I guess you'll just have to find out."

        scene sfr3am2b
        with dissolve

        am "Alright then, let's go."

        jump upstairsamber

    else:
        scene sfr3am2
        with dissolve

        am "Uhm... maybe later. I'm not done watching, haha."

        scene sfr3am2a
        with dissolve

        u "Cool co- co- co- co- co- cool."

        u "No doubt, no doubt, no doubt."

        u "I'll see you later then."

        scene sfr3am2
        with dissolve

        am "Okay."
        
    call screen v6_fr3garage

#*If you click on Kim*
#MC walks up to Kim.
label v6_fr3josh3:
    $ freeroam3asked.add("kim")
    
    scene sfr3jo1

    u "Hey guys."

    if takeshot:
        scene sfr3jo2b
        with dissolve

        ki "Hey hey hey."

        scene sfr3jo2c
        with dissolve

        u "Kim, I found this really cool office upstairs and I was wondering if you wanna go check it out?"

        scene sfr3jo2b
        with dissolve

        ki "Oooh, but I'm already on the moon."

        scene sfr3jo2c
        with dissolve

        u "What? You know, on second thought maybe it's better if you stay here."

    else:
        scene sfr3jo2d
        with dissolve

        ki "It's pussyman!"

        scene sfr3jo2c
        with dissolve

        u "Uhm hey, Kim. I found this really cool office upstairs and I was wondering if you wanna go check it out?"

        scene sfr3jo2b
        with dissolve

        ki "Shut up pussyman!"

        scene sfr3jo2c
        with dissolve

        u "Great conversation. On second thought, I might ask someone else."

    call screen v6_fr3garden

#*If you click on Riley*
#MC walks up to Riley.
label v6_fr3riley3:
    $ freeroam3asked.add("riley")
    $ upstairs = "riley"

    scene sfr3ri1

    u "Heyyy."

    scene sfr3ri2
    with dissolve

    ri "Oh hiii!"

    scene sfr3ri2a
    with dissolve

    u "What are you up to?"

    scene sfr3ri2
    with dissolve

    ri "Not much, really. Just hanging out. What about you?"

    scene sfr3ri2a
    with dissolve

    u "Well I was thinking, you wanna catch a bit of a break and go somewhere quiet for a bit?"

    scene sfr3ri2
    with dissolve

    ri "Yeah, sure. Where were you thinking?"

    scene sfr3ri2a
    with dissolve

    u "There's an office upstairs and it's pretty cool."

    scene sfr3ri2a
    with dissolve

    ri "Sounds good, lead the way."

    jump upstairsriley

    ## OFFICE SCENES

label upstairsaubrey:
    if aubrey.relationship < Relationship.FWB:
        scene sufr3au1 # opening aubrey and you sitting on a couch in the office
        with fade

        au "So tell me, why'd you bring me in here?"

        scene sufr3au2a # aubrey close up smiling mouth closed
        with dissolve

        u "I told you, just wanted to go somewhere quiet."

        scene sufr3au2b # aubrey flirting
        with dissolve

        au "To talk?"

        scene sufr3au2c
        with dissolve

        u "Yeah, why not? You ask a lot of questions, you know? *Chuckles*"

        scene sufr3au2
        with dissolve

        au "I'm a curious girl."

        scene sufr3au2a
        with dissolve

        u "So you and Emily?"

        scene sufr3au2
        with dissolve

        au "What about me and Emily?"

        scene sufr3au2a
        with dissolve

        u "I didn't know you guys were friends."

        scene sufr3au2
        with dissolve

        au "I met her for the first time tonight, actually."

        au "We just got along very well, she's pretty cool."

        scene sufr3au2a
        with dissolve

        u "Yeah, I saw that."

        scene sufr3au2d # aubrey calm, curious
        with dissolve

        au "You worried I'm getting too close to your ex?"

        scene sufr3au2e
        with dissolve

        u "No it's not that-"

        scene sufr3au2d
        with dissolve

        au "We're not hooking up if that's what you're asking."

        scene sufr3au2e
        with dissolve

        u "Oh I didn't even know you run that way too."

        scene sufr3au2d
        with dissolve

        au "I like to have fun. I guess I'm attracted to anyone I like."

        scene sufr3au2e
        with dissolve

        u "Nothing wrong with that."

        scene sufr3au2d
        with dissolve

        au "So you just wanted to know about Emily or?"

        scene sufr3au2e
        with dissolve

        u "Or what?"

        scene sufr3au2b
        with dissolve

        au "I mean you're the one that got me alone into a room when I'm tipsy."

        scene sufr3au2c
        with dissolve

        u "Haha. I just wanted to talk to my friend."

        scene sufr3au2b
        with dissolve

        au "Sureee..."

        scene sufr3au2
        with dissolve

        au "Sadly, even though I know you're undressing me in your head right now and I could see us hooking up right now..."

        au "I should get back before your ex comes looking for us and finds us in a compromising position."

        scene sufr3au2a
        with dissolve

        u "*Chuckles* Yeah, probably a good call."

        menu:
            "We could lock the door":
                $ add_point(KCT.BRO)
                $ add_point(KCT.TROUBLEMAKER)

                u "But we could also lock the door and be quiet..."

                scene sufr3au2b
                with dissolve

                au "So you were thinking about it."

                au "Maybe next time. I'll see you back downstairs."

                scene sufr3au3 # aubrey gone
                with dissolve

                u "(Damn...)"

                u "(I should probably talk to Chris soon.)"

            "It was nice talking":
                $ add_point(KCT.BOYFRIEND)

                u "It was nice talking though."

                scene sufr3au2
                with dissolve

                au "Yeah, it was. I'll see you back downstairs."

                scene sufr3au3 # aubrey gone
                with dissolve

                u "(I should probably talk to Chris soon.)"

    else:
        scene sufr3au1
        with fade

        au "So why'd you really bring me in here?"

        scene sufr3au2c
        with dissolve

        u "I told you, just wanted to go somewhere quiet."

        scene sufr3au2b
        with dissolve

        au "Okaaay. You sure? Because I don't think I've ever had sex in an office."

        scene sufr3au2c
        with dissolve

        u "Haha, I don't think I have either."

        scene sufr3au2b
        with dissolve

        au "Here's a question, where is the craziest place you had sex?"

        scene sufr3au2c
        with dissolve

        u "I don't know, a car?"

        scene sufr3au2
        with dissolve

        au "*Laughs* A car? That's it?"

        scene sufr3au2a
        with dissolve

        u "Well, it's something. What about you then? I bet it's not that crazy either."

        scene sufr3au2b
        with dissolve

        au "The center of my high school football field."

        scene sufr3au2c
        with dissolve

        u "Okay I take it back, that is pretty crazy."

        scene sufr3au2
        with dissolve

        au "*Laughs* Don't judge me."

        scene sufr3au2a
        with dissolve

        u "I'm not. It's kinda cool. I like adventurous girls."

        scene sufr3au2b
        with dissolve

        au "Good. Cause that's what you're getting with me."

        scene sufr3au2b
        with dissolve

        u "So who did you do that with? Someone on the football team?"

        scene sufr3au2b
        with dissolve

        au "Haha. Actually no. My ex. He was a baseball player."

        scene sufr3au2c
        with dissolve

        u "So what happened to him?"

        scene sufr3au2
        with dissolve

        au "*Laughs* What do you mean what happened to him?"

        scene sufr3au2a
        with dissolve

        u "Like, why did you guys stop dating?"

        scene sufr3au2
        with dissolve

        au "He was boring. I don't think he could handle how wild I was all the time."

        au "I mean he tried to keep up, but I think I was just too much for him."

        scene sufr3au2a
        with dissolve

        u "*Laughs* What do you mean?"

        scene sufr3au2b
        with dissolve

        au "There was this one time for his birthday, where I had blindfolded him and tied him to the bed for his present."

        au "When I removed the blindfold, my best friend, was right in front of him, completely naked. And she was fucking hot."

        au "I wanted to give him a dream threesome and he just got mad and called it inappropriate and that he didn't wanna share me with another girl."

        menu:
            "He turned down a threesome?!":
                $ add_point(KCT.BRO)

                scene sufr3au2c
                with dissolve

                u "He turned down a threesome?! That's mad."
                u "Two girls... man that's the dream."

                scene sufr3au2
                with dissolve

                au "*Chuckles* I know! That's why I tried to give it to him."

                scene sufr3au2
                with dissolve

                u "So, if you don't mind me asking... are you, like, bisexual?"

                scene sufr3au2a
                with dissolve

                au "Uhm, I guess. I like to have fun. I'm just attracted to anyone I like, be it boy or girl."

                scene sufr3au2
                with dissolve

                u "See, I'm really attracted to one specific girl right now."

                scene sufr3au2b
                with dissolve

                au "And who might that be?"

                scene sufr3au4 # showing mc and aubrey close
                with dissolve

                pause 0.5

                play sound "sounds/kiss.mp3"
                scene sufr3au4a ## kiss
                with dissolve

                pause 1.0

                scene sufr3au4b # aubrey pulls away annoyed, mouth open
                with dissolve

                au "We can't do this right now."

                scene sufr3au2e
                with dissolve

                u "What? Why?"

                scene sufr3au2d
                with dissolve

                au "I've just ditched Emily and she might come looking for us. I'd rather avoid the drama of her seeing me with her ex."

                scene sufr3au2e
                with dissolve

                u "Damn... that's actually a good reason."

                menu:
                    "We could lock the door":
                        $ add_point(KCT.BRO)
                        $ add_point(KCT.TROUBLEMAKER)

                        u "But we could also lock the door and be quiet..."

                        scene sufr3au2b
                        with dissolve

                        au "Maybe next time. I'll see you back downstairs."

                        scene sufr3au3 # aubrey gone
                        with dissolve

                        u "(Damn...)"

                        u "(I should probably talk to Chris soon.)"

                    "At least we got to talk":
                        $ add_point(KCT.BOYFRIEND)

                        u "At least we got to talk a bit, haha."

                        scene sufr3au2
                        with dissolve

                        au "Yeah, it was nice. I'll see you back downstairs."

                        scene sufr3au3 # aubrey gone
                        with dissolve

                        u "(I should probably talk to Chris soon.)"

            "I kinda get what he means":
                $ add_point(KCT.BOYFRIEND)
                $ simp = True
                $ aubrey.relationship = Relationship.FRIEND

                scene sufr3au2c
                with dissolve

                u "I mean, I kinda get what he means... I wouldn't wanna share my girlfriend with anyone else."

                scene sufr3au2e
                with dissolve

                u "Even if it's a girl."

                scene sufr3au2d
                with dissolve

                au "Really? I thought you'd be a little more open to this kinda stuff..."

                scene sufr3au2e
                with dissolve

                u "I don't know. I'm just saying I see where he's coming from."

                scene sufr3au2d
                with dissolve

                au "Right..."

                au "Anyways, I should probably go downstairs again. Emily's probably missing me."

                scene sufr3au2e
                with dissolve

                u "Oh, already?"

                scene sufr3au2d
                with dissolve

                au "Yeah... I'll see you later."

                scene sufr3au3 # aubrey gone
                with dissolve

                u "(I feel like I said something wrong there...)"

                u "(I should probably talk to Chris soon anyway.)"

    call screen v6_fr3office


label upstairsemily:
    scene sufr3em1 # opening emily leaning on the desk playfully grabbing mcs shirt, emily flirting
    with fade

    em "So why'd you choose this office?"

    scene sufr3em2a # emily flirting
    with dissolve

    u "*Chuckles* What do you mean?"

    scene sufr3em2
    with dissolve

    em "It's not the most comfortable place to-"

    scene sufr3em2a
    with dissolve

    u "*Laughs* Woah, slow down. I just wanted to hang out with you a bit."

    scene sufr3em2b # emily cute
    with dissolve

    em "Just missed you is all?"

    em "Soo, actually I was thinking the next we..."

    em "You know..."

    scene sufr3em2
    with dissolve

    em "I wanna try anal."

    scene sufr3em2a
    with dissolve

    u "*Laughs* What? Anal? Seriously?"

    u "I swear you told me you never ever wanted to do it in your entire life back when we were dating."

    scene sufr3em2b # emily cute
    with dissolve

    em "Well that's what I thought at the time..."

    em "But when we broke up, I got lonely... and horny."

    em "So I started looking up porn, you know, just once or twice..."

    em "And anal kinda really turned me on."

    scene sufr3em2c
    with dissolve

    u "I mean yeah, let's do it. Hahaha."

    u "I'm not gonna say no to that."

    scene sufr3em2b
    with dissolve

    em "Good. But we have to start slow. Maybe just a finger or two at first. And a lot of lube."

    scene sufr3em2c
    with dissolve

    u "Yeah, of course. We'll make sure you're comfortable and it doesn't hurt at all."

    scene sufr3em2b
    with dissolve

    em "Thank you."

    em "I should probably go back downstairs now."

    scene sufr3em2c
    with dissolve

    u "*Chuckles* Really? You're gonna put this image in my head and then just leave me like this."

    scene sufr3em2b
    with dissolve

    em "Sorry, but Aubrey is probably waiting for me and I'm not looking to take penalty shots for leaving her... I'm tipsy enough as it is."

    scene sufr3em2c
    with dissolve

    u "Alright, I get it. I should probably talk to Chris anyways."

    scene sufr3em1 # showing both you and emily close , emily mouth open
    with dissolve

    em "Good luck with that."

    scene sufr3em1a # kiss
    with dissolve

    play sound "sounds/kiss.mp3"

    pause 1.0

    scene sufr3em1
    with dissolve

    em "I'll see you later."

    call screen v6_fr3office

label upstairsamber: # upstairs with amber
    
    scene sufr3am1 # amber looking at the bookshelves
    with fade

    am "So you pull me away from all shirtless guys working out to bring me in here?"

    scene sufr3am1a # amber walking to stand in front of you
    with dissolve

    u "Yup. Welcome to the most interesting part of the party, the office."

    scene sufr3am2 # amber close up ironic
    with dissolve

    am "I can barely hold my excitement in."

    scene sufr3am2a
    with dissolve

    u "*Chuckles* And yet you manage."

    u "Just thought it would be nice to be somewhere a bit more quiet for a bit."

    scene sufr3am2
    with dissolve

    am "Uhm... sure."

    scene sufr3am2a
    with dissolve

    u "Did you ever hook up with Josh?"

    scene sufr3am2b # amber smiling
    with dissolve

    am "*Laughs* Wow, that's out of the blue. No, I have not. I mean he used to hit on me quite a bit, but he's not my type. And now he's moved on to Kim."

    scene sufr3am2c
    with dissolve

    u "Sorry, I was just curious."

    scene sufr3am2b
    with dissolve

    am "Here's a tip, if you're trying to get into someone's pants, don't talk to her about whether she's hooking up with other guys."

    scene sufr3am2c
    with dissolve

    u "Who say's I'm trying to get into your pants?"

    scene sufr3am2d
    with dissolve

    am "Isn't it obvious? Dark, lonely office. Just me and you."

    am "There's even a couch here."

    scene sufr3am2e
    with dissolve

    u "Haha. Maybe. But maybe I just wanted to talk to you."

    scene sufr3am2d
    with dissolve

    am "And what's there to talk about?"

    scene sufr3am2e
    with dissolve

    u "For example, why weren't you hanging out with Josh and Kim tonight? Why stay alone all night?"

    scene sufr3am2b
    with dissolve

    am "I found something more interesting, haha. I'm not that deep. They were just getting high all night and I wasn't feeling the vibe."

    scene sufr3am2c
    with dissolve

    u "Are you feeling this vibe?"

    scene sufr3am2d
    with dissolve

    am "Maybe."

    scene sufr3am2e
    with dissolve

    play sound "sounds/call.mp3"

    "*Amber's phone rings*"

    scene sufr3am2f # amber reaching for her phone
    with dissolve

    am "Hold up."

    play sound "sounds/answercall.mp3"

    scene sufr3am2h # amber on phone mouth open serious
    with dissolve

    am "Hello?"

    scene sufr3am2j
    with dissolve

    pause 0.5

    scene sufr3am2k # amber upset
    with dissolve

    am "Oh no, really? Okay I'll come down."

    scene sufr3am2 # amber upset without phone
    with dissolve

    am "Sorry, Kim's throwing up, I gotta go hold her hair."

    scene sufr3am2a
    with dissolve

    u "Oh shit. Uhm... I'll see you later then."

    scene sufr3am2
    with dissolve

    am "Okay, yeah. See you."

    call screen v6_fr3office

    #*You bring Riley into the office*
    #Riley and MC walk into the office. Riley immediately sits down on the desk.
label upstairsriley:
    scene sufr3ri1 # riley and you sitting on a couch
    with dissolve

    ri "This was a good idea."

    scene sufr3ri2a # riley close up smiling
    with dissolve

    u "Coming up here?"

    scene sufr3ri2
    with dissolve

    ri "Yeah, it's nice to be somewhere a bit more quiet after being right next to really loud speakers the entire night."

    scene sufr3ri2a
    with dissolve

    u "Yeah, I guess my ideas are pretty brilliant, aren't they?"

    scene sufr3ri2b # riley flirting
    with dissolve

    ri "*Chuckles* Don't get ahead of yourself, buddy."

    scene sufr3ri2c
    with dissolve

    u "It's hard when you're this dazzling."

    scene sufr3ri2a
    with dissolve

    ri "*Laughs* So have you decided if you're going to join the Wolves or not?"

    scene sufr3ri2
    with dissolve

    if joinapes:
        u "Actually, I'm probably gonna join the Apes."

        scene sufr3ri2d # riley upset
        with dissolve

        ri "The Apes?! Didn't Grayson punch you?"

        scene sufr3ri2e
        with dissolve

        u "Yeah, but he apologized and he really sees my potential, you know."

        scene sufr3ri2d # riley upset
        with dissolve

        ri "Your potential?"

        scene sufr3ri2e
        with dissolve

        u "Yeah, he says I could be one of the greats, leading the Apes."

        scene sufr3ri2d # riley upset
        with dissolve

        ri "[name], are you sure about this? Didn't you say you don't like fighting?"

        ri "Also, I don't wanna be mean, but... you're not really a proven quality, don't you find it weird that he puts so much faith in you."

        scene sufr3ri2e
        with dissolve

        u "What are you trying to say?"

        scene sufr3ri2d # riley upset
        with dissolve

        ri "I don't know... maybe he's manipulating you."

        scene sufr3ri2e
        with dissolve

        u "He's not, okay? You weren't there. He sees in me what no one else seems to see."

        scene sufr3ri2f # riley loving
        with dissolve

        ri "I see stuff in you. [name], you're not like anyone I've ever met."

        ri "But that doesn't mean that Grayson isn't taking advantage of you."

        scene sufr3ri2g
        with dissolve

        u "I don't really wanna talk about it anymore."

        scene sufr3ri2f # riley loving
        with dissolve

        ri "Okay... I'll go back downstairs then. I'll see you later."

        scene sufr3ri2g
        with dissolve

        u "Alright."

    else:
        u "I'm not sure yet, but I'm leaning towards joining them."

        scene sufr3ri2f
        with dissolve

        ri "I think you'd make a great Wolf."

        scene sufr3ri2g
        with dissolve

        u "Thanks."

        u "You talk to Ryan lately?"

        scene sufr3ri2h #riley hessitant
        with dissolve

        ri "Ryan? Honestly, he kind of annoys me sometimes. I know he has no ill intentions, but he can be bit of a horn dog."

        scene sufr3ri2j
        with dissolve

        u "*Laughs* What'd he do?"

        scene sufr3ri2h
        with dissolve

        ri "Nothing really."

        ri "Actually you can't tell anyone but last night, Ryan booty called me. He seemed very drunk... I don't know why."

        scene sufr3ri2j
        with dissolve

        u "*Laughs* So what'd you do?"

        scene sufr3ri2
        with dissolve

        ri "*Chuckles* What do you mean what'd I do? I told him no and that he should drink water and get some rest."

        scene sufr3ri2a
        with dissolve

        u "Ouch."

        scene sufr3ri2
        with dissolve

        ri "I feel kinda bad for him, maybe he was just lonely."

        scene sufr3ri2a
        with dissolve

        u "I think he'll be fine. He was just a horny guy thinking you're an easy lay."

        scene sufr3ri2
        with dissolve

        ri "Well I'm not."

        scene sufr3ri2a
        with dissolve

        u "*Chuckles* Apparently."

        scene sufr3ri2h
        with dissolve

        ri "I should probably go back downstairs before Finn also booty calls me."

        scene sufr3ri2j
        with dissolve

        u "*Laughs* Oh god. I should probably talk to Chris soon anyway."

        scene sufr3ri2
        with dissolve

        ri "Good luck. I'll see you later."
        
    call screen v6_fr3office


label v6_fr3chris3: ### ENDING
    scene sfr3ch2

    ch "You ready?"

    scene sfr3ch2a
    with dissolve

    u "Yeah. So what did you wanna show me?"

    scene sfr3ch2
    with dissolve

    ch "Follow me."

    scene s670 # FIrst person: behind chris walking upstairs
    with dissolve

    pause 0.5

    scene s671 # chris unlocking a door looking at you
    with dissolve

    ch "I don't usually show this to outsiders, but I have a good feeling about you."

    # unlock sounds

    scene s671a # chris about to open the door
    with dissolve

    pause 0.5

    # door open sound

    scene s672 # close up of your face shocked
    with dissolve

    u "Holy shit."
    stop music fadeout 3

    jump v7start
