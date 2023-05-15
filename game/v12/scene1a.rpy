# SCENE 1a: MC Chases After Robber
# Location: 
# Characters: MC (Outfit X), Nora (Outfit X)
# Time: Nighttime

label v12_chase_robber:
    $ v12_chase_robber = True
    scene v12car1 # TPP Show MC shoving Charli out of the way to take off after robber
    with dissolve

    pause 0.75

    play music music.v12_Track_Scene_1_1 fadein 2

    scene v12car2 # TPP Show MC turning into an alley at a full run
    with dissolve

    pause 0.75

    scene v12car3 # FPP Alley splits in two directions - MC has to choose which way to go
    with dissolve

    u "(What the fuck? He's too fast... Where'd he go?)"

    menu:
        "Left":
            scene v12car4 # FPP MC looking down dark alley to the left
            with dissolve
            
            u "(This way!)"

            scene v12car5 # FPP View of an alley that ends in a dead end
            with dissolve

            u "(Where is he?)"

            scene v12car6 # TPP Show MC getting hit on the back of the head
            with dissolve
            play sound sound.hit

            pause 0.3
            scene v12car7 # TPP Show MC laying on the ground in the alley, face down, trying to catch himself
            with hpunch

            robber "Eat asphalt, bitch!"

            scene v12car8 # FPP MC looking up at robber from a position laying on the ground
            with dissolve

            u "Ahh, shit! You've really fucked up now."

            scene v12car9 # TPP Show MC hopping up from the ground and moving to fight
            with dissolve

            pause 0.75

        "Right":
            scene v12car10 # FPP Show robber in right alley, digging through Nora's bag
            with dissolve

            u "Got your ass now!"

            scene v12car10a # FPP Same angle as v12car10, robber holding Nora's bag, looking at MC, holding his hand out and looking nervous, mouth open
            with dissolve

            robber "Wait! Look man, please. I just needed some money for food. I don't want any trouble."

            scene v12car11 # FPP Show robber, MC has moved closer, robber holding Nora's bag, mouth closed, MCs arm extended to grab bag
            with dissolve

            u "There are plenty of other ways to get help, dude. Hand over the bag."

            scene v12car11a # FPP Same angle as v12car11, robber looking angry and taking a swing at MC
            with dissolve

            menu (fail_label="v12s1a_failed_timer"):
                "Dodge":
                    $ reputation.add_point(RepComponent.TROUBLEMAKER)
                    $ v12_fight_win = True
                    scene v12car12 # TPP Show MC dodging robber's punch
                    with dissolve

                    pause 0.75
                    
                    play sound sound.hit
                    scene v12car0
                    with hpunch
                    
                    pause 0.5
                    
                    play sound sound.hit
                    scene v12car00
                    with vpunch
                    
                    pause 0.5
                    
                    
                "Huh":
                    label v12s1a_failed_timer:
                        scene v12car12a # TPP Same angle as v12car12, show MC getting punched in the mouth by the robber
                        with hpunch

                        play sound sound.hit

                        pause 0.75

    # MANUAL FIGHT

    if not v12_fight_win:
        scene v12car13 # TPP Show MC laying on the ground, writhing in pain
        with vpunch

        robber "Ha, you sure are one sorry ass fighter. Now your girl lost her bag and you got your ass kicked. Bet you won't be getting any tonight. *Laughs*"

        stop music fadeout 3
        play music music.ck1.v12.Track_Scene_1a_2 fadein 2

        scene v12car14 # FPP View of MC laying on the ground, show robber running out of the alley and into the night
        with dissolve

        u "Motherfucker... Ahh, shit."

        scene v12car14a # FPP Same angle as v12car14, show exit of the alley, nobody visible
        with dissolve

        imre "[name]! [name]! Are you out here?"

        u "I'm... I'm over here."

        scene v12car15 # FPP Show Imre standing over MC, Imre looks worried, mouth open
        with dissolve

        imre "Damn, are you alright?"

        scene v12car15a # FPP Same angle as v12car15, Imre looking worried with mouth closed
        with dissolve

        u "Do I look alright?"

        scene v12car15b # FPP Same angle as v12car15, Imre smiling with mouth open
        with dissolve

        imre "You look exactly how you looked when Grayson got done with you, minus the black eye. *Laughs*"

        scene v12car15c # FPP Same angle as v12car15, Imre smiling with mouth closed
        with dissolve

        u "You gonna keep laughing or help me up?"

        scene v12car15b
        with dissolve

        imre "*Chuckles* I got you."

        scene v12car16 # TPP Show Imre helping MC to his feet
        with dissolve

        pause 0.75

        scene v12car17 # TPP Imre throwing MC's arm over his shoulder to support him, Imre with neutral expression, mouth open
        with dissolve

        imre "Could've at least gotten the purse..."

        scene v12car18 # FPP Show Imre, close to MC as he supports him as they walk out of the alley, Imre smiling with mouth closed
        with dissolve

        u "Oh I'm sorry, should I have kindly asked for the bag before or after I got my ass kicked?"

        scene v12car18a # FPP Same angle as v12car18, Imre laughing with mouth open
        with dissolve

        imre "*Laughs*"

        scene v12car19 # FPP Back out on the street, show Charli, neutral expression, mouth open
        with dissolve

        charli "There you are. Where's the mugger?"

        scene v12car19a # FPP Same angle as v12car19, Charli's mouth closed
        with dissolve

        u "Gone."

        scene v12car19
        with dissolve

        charli "You let him get away? Where's Nora's bag?"

        scene v12car19a
        with dissolve

        u "Do you really think I would just \"let him?\""

        scene v12car20 # FPP Imre stops supporting MC, his hand on Charli's shoulder, pointing back toward the alley, mouth open
        with dissolve

        imre "If you wanna try your luck, he's that way."

        scene v12car20a # FPP Same angle as v12car20, Imre smiling with mouth closed, Charli with mouth open
        with dissolve

        charli "I'm sure I'd have a much better chance at beating him than either of you, but he's definitely long gone by now."

        scene v12car20
        with dissolve

        imre "Ha, pussy."

        scene v12car21 # TPP Show MC and Imre walking back along the sidewalk, Charli behind them
        with dissolve

        pause 0.75

        stop music fadeout 3
        play music music.ck1.v12.Track_Scene_1a_3 fadein 2

        scene v12car100
        with fade

        pause 0.75

        scene v12car22 # FPP Show Charli walking away from the hotel lobby down the hallway
        with dissolve

        imre "I can't stand that guy."

        u "And he can't stand us."

        scene v12car23 # FPP Show Imre, standing in hotel lobby, smiling with mouth open
        with dissolve

        imre "Don't worry... I'll catch him off guard one of these days and we'll see how tough he really is."

        scene v12car23a # FPP Same angle as v12car23, Imre smiling with mouth closed
        with dissolve

        u "Shit man, are you selling tickets? I wanna be in the front row for that. *Chuckles*"

        scene v12car23
        with dissolve

        imre "Haha, I'll consider it. Are you good to get up to your room by yourself?"

        scene v12car23a
        with dissolve

        u "Yeah man, I'm feeling a lot better. I think he just knocked the wind out of me. Thanks for coming to find me, though. I guess Ryan and Chris were busy, huh?"

        scene v12car23
        with dissolve

        imre "I didn't even stop to turn and see. I saw you run and just started running too. You guys just got away from me there for a bit."

        scene v12car23a
        with dissolve

        u "Because you're slow. Don't worry, I get it dude. It's the thought that counts. *Chuckles*"

        scene v12car23
        with dissolve

        imre "Maybe. *Chuckles* But it wasn't hard to find you. That big ass forehead is impossible to miss."

        scene v12car23a
        with dissolve

        u "*Laughs* Hey, man... At least I have a full head of hair to cover it up a bit. What's your excuse?"

        scene v12car23
        with dissolve

        imre "*Chuckles* Too far, man. Too fucking far..."

        scene v12car23a
        with dissolve

        u "*Laughs* See ya, dude."

        scene v12car22a # FPP Same angle as v12car22, Imre walking away down the hallway, turning and waving at MC, Imre smiling with mouth open
        with dissolve

        imre "Haha, later."

        scene v12car24 # TPP Show MC walking down the hallway to his room
        with dissolve

        pause 0.75

    else:
        scene v12car13a # FPP Same angle as v12car13, show robber laying on the ground next to Nora's bag, writhing in pain
        with dissolve

        u "Fucking asshole!"

        stop music fadeout 3
        play music music.ck1.v12.Track_Scene_1a_2 fadein 2

        scene v12car16a # TPP Same angle as v12car16, show MC reaching down to robber on the ground and grabbing Nora's bag
        with dissolve

        pause 0.75

        scene v12car13b # FPP Same angle as v12car13, robber laying on the ground in pain, Nora's bag is gone
        with dissolve

        menu:
            "Kick him":
                $ reputation.add_point(RepComponent.TROUBLEMAKER)
                scene v12car16b # TPP Same angle as v12car16, show MC kicking robber
                with dissolve
                play sound sound.hit


                u "Bitch!"

            "Walk off":
                u "(He's had enough.)"

        scene v12car25 # FPP Show Imre, in alley, Imre looks winded, mouth open
        with dissolve

        imre "*Heavy breathing* You got the purse, good."

        scene v12car25a # FPP Same angle as v12car25, Imre smiling with mouth closed
        with dissolve

        u "Did you doubt me? *Chuckles*"

        scene v12car25b # FPP Same angle as v12car25, Imre smiling with mouth open
        with dissolve

        imre "Nah, I knew I had no reason to worry. I was just coming to back you up."

        scene v12car25a
        with dissolve

        u "Haha, I appreciate that. Where's everyone else?"

        scene v12car25b
        with dissolve

        imre "Most of them went back to the hotel. They tried staying with Nora but she told them to go."

        scene v12car25a
        with dissolve

        u "\"Most?\" Who stayed with her?"

        scene v12car25b
        with dissolve

        imre "I'm sure you can guess who. His name rhymes with bitch boy."

        scene v12car25a
        with dissolve

        u "(Rhymes with \"bitch boy?\" Oh...) *Laughs* Charli?"

        scene v12car25c # FPP Same angle as v12car25, Imre laughing with mouth open
        with dissolve

        imre "Bingo! *Laughs*"

        scene v12car26 # TPP Show MC and Imre walking up to Nora and Charli, Charli has his hand on Nora's shoulder
        with dissolve

        pause 0.75

        scene v12car27 # FPP Back out on the street, show Imre, looking over toward Nora and Charli, Imre smiling with mouth open
        with dissolve

        imre "Your hero has arrived!"

        scene v12car28 # FPP Show Nora looking at MC and Imre, smiling with mouth open
        with dissolve

        no "Oh my God, you actually got my bag!"

        scene v12car27
        with dissolve

        imre "He sure did. He also taught that guy a lesson with a little Ali treatment."

        scene v12car28a # FPP Same angle as v12car28, Nora closer to MC and away from Charli, Nora smiling with mouth closed, MC is holding her bag out to her
        with dissolve

        no "*Chuckles*"

        u "Here you go."

        scene v12car28b # FPP Same angle as v12car28, Nora standing close to MC, smiling with mouth open
        with dissolve

        no "Th-Thank you [name]. That was really sweet of you. This means a lot."

        scene v12car28c # FPP Same angle as v12car28, Nora standing close to MC, smiling with mouth closed
        with dissolve

        u "No need to thank me, but you're very welcome. I don't normally see you with a bag so I assumed since you had one you must've been carrying something important with you."

        scene v12car28b
        with dissolve

        no "Well... Your assumption isn't wrong."

        scene v12car27
        with dissolve

        imre "You know, I don't mind taking rainbow unicorn boy back to the hotel if you two wanna hang back and talk about my boy's heroic moment a bit longer. *Laughs*"

        scene v12car29 # FPP Show Charli out on the street, Charli with annoyed expression, mouth open
        with dissolve

        charli "After what just occurred, splitting up doesn't seem like the wisest decision."

        scene v12car28d # FPP Same angle as v12car28, Nora standing close to MC but looking back at Charli, Nora's mouth open
        with dissolve

        no "If we did split up it's obvious [name] can handle himself, but for your sake Charli, we'll all walk back together."

        scene v12car29a # FPP Same angle as v12car29, Charli looks annoyed with mouth closed
        with dissolve

        u "(Damn... roasted!)"

        scene v12car21a # TPP Same angle as v12car21, show MC and Nora walking back toward the hotel, Imre and Charli behind them, Imre grinning and Charli looking annoyed
        with dissolve

        pause 0.75

        scene v12car22b # FPP Same angle as v12car22, Nora and Charli walking away from the hotel lobby down the hallway
        with dissolve

        pause 0.75

        stop music fadeout 3
        play music music.ck1.v12.Track_Scene_1a_3 fadein 2

        scene v12car23
        with dissolve

        imre "I may just have to put you in the top tier fighters on campus after that. He was a pretty big dude."

        scene v12car23a
        with dissolve

        u "Was I not top tier already? *Chuckles*"

        scene v12car23
        with dissolve

        imre "I don't think so, but maybe now. I'll have to speak with the best fighters commission."

        scene v12car23a
        with dissolve

        u "Who's on the commission?"

        scene v12car23
        with dissolve

        imre "Only the best fighters on campus. Imre, Imre and Imre. *Laughs*"

        scene v12car23a
        with dissolve

        u "*Laughs* Goodnight man."

        scene v12car22a
        with dissolve

        imre "Haha, you too."

        scene v12car24
        with dissolve

        pause 0.75

    stop music fadeout 3
    play music music.v11_Track_Scene_6 fadein 2

    scene v12car30 # TPP Show MC sitting on his bed in the hotel room
    with dissolve

    pause 0.75

    scene v12car31 # FPP Show MC's view of the inside of closed hotel room door
    with dissolve

    u "(*Sighs* I wonder where the roomie went.)"

    scene v12car32 # TPP Show MC laying back on hotel room bed
    with dissolve

    pause 0.75

    scene v12car33 # FPP Show MC's view up at the hotel room ceiling from laying on his bed
    with dissolve

    u "(Why would some random dude try and steal a bag from someone who's obviously in a group? That just stupid... Then there's Charli... I swear he can't just be a normal person... Definitely a weird ass dude.)"

    scene v12car34 # TPP Show MC looking at himself in the hotel room mirror
    with dissolve

    pause 0.75

    scene v12car65 # FPP MC looking down at his fists, his knuckles are bruised and bloody from the fight
    with dissolve
    
    u "You chased a robber, my guy! A robber! You could've died! *Chuckles*"
    u "(Haha, little self pep talk.)"

    scene v12car30
    with dissolve

    play sound sound.vibrate
    pause 1.25

    scene v12car30a # TPP Same angle as v12car30, MC sitting on the hotel room bed and checking his phone
    with dissolve

    pause 0.75

    $ kiwii_post = KiwiiService.new_post(imre, "phone/kiwii/Posts/v12/impost1.webp", _("Would your man chase a robber down in the middle of the night? If not, you don't have a real man..."), number_likes=216)
    $ KiwiiService.new_comment(kiwii_post, charli, _("If you want a man Imre I can take you to a few bars... All you had to do was ask."), number_likes=14)
    $ KiwiiService.new_comment(kiwii_post, ryan, _("LMAO"), number_likes=1, mentions=[imre])

    $ MessengerService.new_message(imre, "Check Kiwii... you're welcome. :)")
    $ MessengerService.add_reply(imre, "Haha okay")

    call screen phone

    # MC checks Kiwii and there's a picture of MC running after the robber posted by Imre 
    # caption "Would your man chase a robber down in the middle of the night? If not, you don't have a real man..."
    # There's a comment from Charli that says "If you want a man Imre I can take you to a few bars, all you had to do was ask."
    
    # MC replies back to Imre-
    $ MessengerService.add_reply(imre, "Boosting me huh?")
    $ MessengerService.new_message(imre, "You deserved it")
    $ MessengerService.add_reply(imre, "You see Charli's comment?")
    $ MessengerService.new_message(imre, "No, one sec")
    $ MessengerService.new_message(imre, "I'm gonna beat his ass")
    $ MessengerService.add_reply(imre, "Haha")

    scene v12car30a
    with dissolve
    pause 0.75
    call screen phone
    
    scene v12car30b # TPP Same angle as v12car30, MC sitting on bed, putting his phone away in his pocket
    with dissolve

    pause 0.75

    # -MC hears a knock on his door-

    play sound sound.knock
    pause 0.75

    stop music fadeout 3

    jump v12_nora_checks_mc # jump scene 2