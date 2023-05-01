init python:
    def v7_kiwiiReply1():
        v7_kiwiiPost1.newComment(cameron, _("Lol, pussy"), mentions=[mc], number_likes=renpy.random.randint(1, 10))
        reputation.add_point(RepComponent.BOYFRIEND)

    def v7_kiwiiReply2():
        v7_kiwiiPost1.newComment(imre, _("Slide into her DMs bro!"), mentions=[mc], number_likes=renpy.random.randint(5, 15))
        reputation.add_point(RepComponent.BRO)
        reputation.add_point(RepComponent.TROUBLEMAKER)

    def v7_kiwiiReply3():
        reputation.add_point(RepComponent.BOYFRIEND)

    def v7_kiwiiReply4():
        v7_kiwiiPost2.newComment(autumn, _("Yeah, they really are"), mentions=[mc], number_likes=renpy.random.randint(8, 18))
    
    def v7_kiwiiReply5():
        reputation.add_point(RepComponent.BRO)
        v7_kiwiiPost3.newComment(aubrey, _("Bring it on!"), mentions=[mc], number_likes=renpy.random.randint(15, 35))

    def v7_kiwiiReply6():
        reputation.add_point(RepComponent.TROUBLEMAKER)
        v7_kiwiiPost4.newComment(josh, _("lol"), mentions=[mc], number_likes=renpy.random.randint(3, 7))

    def kiwii_firstTimeMessages():
        if CharacterService.is_fwb(emily):
            MessengerService.add_reply(riley, _("We're not back together"))
            MessengerService.new_message(riley, _("Okay... just looked like it"))
            MessengerService.add_reply(riley, _("Well we're not."))
            MessengerService.new_message(riley, _("k"))

        if bowling and CharacterService.is_fwb(emily):
            v7_msgReply1 = MessageBuilder(penelope)
            v7_msgReply1.add_function(reputation.add_point, RepComponent.BRO)
            v7_msgReply1.new_message(_("Okay..."))

            v7_msgReply2 = MessageBuilder(penelope)
            v7_msgReply2.new_message(_("Okay..."))

            MessengerService.new_message(penelope, _("I didn't know you and Emily were a thing..."))
            MessengerService.add_replies(penelope,
                Reply(_("We're not a thing"), v7_msgReply1),
                Reply(_("It was a one time thing"), v7_msgReply2)
            )

        if CharacterService.is_fwb(emily) and CharacterService.is_girlfriend(lauren):
            MessengerService.new_message(lauren, _("I saw what Emily posted. I really thought you liked me..."))
            MessengerService.new_message(lauren, _("I guess we're done now, so please just delete my number."))
            MessengerService.add_reply(lauren, _("Lauren can we please just talk about it? I can explain"))
            MessengerService.new_message(lauren, _("What is there to talk about? How could you betray me like that?!"))
            MessengerService.add_reply(lauren, _("Please, it's just a big misunderstanding"))
            MessengerService.new_message(lauren, _("Fine. I'm in my dorm, we can talk now."))

label start7: #for compatibility only
label v7start:

######## SCENE 1 Chris in Wolves secret room
    scene s673 # #showing the room (not showing you or chris)with 6v large portraits and one empty frame on the wall
    with dissolve

    u "This is amazing."

    play music "music/muffledparty.mp3"

    scene s674 # close up chris proud
    with dissolve

    ch "These are all the fight kings of the Wolves. There's one for every year we have won."

    scene s674a
    with dissolve

    u "Haven't you guys won seven times though? I only count six portraits."

    scene s674b # chris pointing and looking at a portrait of Imre's brother
    with dissolve

    ch "Yeah, well that's because of this guy."

    scene s675 # showing Imre's brother portrait
    with dissolve

    ch "This is a Wolves legend right here, Bence Varga."

    u "Imre's brother..."

    ch "He won two years in a row. The only Wolf to ever win twice."

    scene s674
    with dissolve

    ch "You should've seen him. He was so determined. Sometimes he'd workout for eight hours in a single day."

    scene s674a
    with dissolve

    u "That's insane."

    scene s674d # chris smiling
    with dissolve

    ch "Yeah, he was something different."

    scene s674e
    with dissolve

    u "Who's the guy next to him?"

    scene s675a # shows chuck's portrait who's thin
    with dissolve

    ch "*Chuckles* Oh that guy. That's Chuck. AKA the fighting cock."

    u "The fighting cock? Like a-?"

    scene s674d
    with dissolve

    ch "Haha, no not like that. Like a chicken. Cock just sounded better."

    ch "He was scrawny as fuck, but that kid could fight like hell."

    scene s674e
    with dissolve

    u "Haha, damn."

    scene s674f #chris looks at Drew's portrait
    with dissolve

    ch "And then next to him is Drew. He was known for his kicks."

    scene s675b # showing drews portrait
    with dissolve

    ch "I don't remember what that guy used to do, I think it was gymnastics or something. I don't know him personally, but we still teach his kicking technique to this day."

    u "I didn't know gymnastics would make you good at fighting."

    scene s674d
    with dissolve

    ch "Haha, me neither. But here at the Wolves, we try not to judge people based on stereotypes."

    scene s674
    with dissolve

    ch "He actually got turned away by the Apes that year. They told him he didn't fit the style."

    ch "But the Wolves saw his potential and welcomed him with open arms. He turned out be one of the best fighters we ever had."

    scene s674a
    with dissolve

    u "Yeah, sounds amazing."

    u "What about the guys on the other side?"

    scene s675c # showing david
    with dissolve

    ch "On the left that's David Park. He was actually a foreign exchange student from Korea quite a while ago."

    ch "He was a black belt in Taekwondo. It took him a little while to adjust to a different style of combat, but his fighting was like an art. He was swift, light on his feet."

    scene s674e
    with dissolve

    u "How do you know so much about each of them? You've only been at San Vallejo for like three years, right? "

    scene s674
    with dissolve

    ch "These guys are legends. There were hundreds of Wolves over the years, only six ever won the Summer Showdown. It's a huge deal, so you hear a lot about them."

    scene s674a
    with dissolve

    u "Yeah, I guess that makes sense."

    scene s675d # showing the wall portrait
    with dissolve

    u "What about him?"

    ch "That's the wall."

    u "The wall?"

    scene s674
    with dissolve

    ch "He was a big guy. He wasn't particularly skilled at fighting from what I've heard. He was hella slow."

    scene s674a
    with dissolve

    u "Then how the hell did he become Fight King?"

    scene s674
    with dissolve

    ch "Because that guy could take hits like it was nothing, hence the wall."

    ch "He'd just let the other guy hit him over and over again until they got tired. Then when the other guy was completely exhausted, the wall would just lay one good hit on him and he'd be down."

    scene s674a
    with dissolve

    u "That's crazy. That guy must have had some mad genetics."

    scene s674d
    with dissolve

    ch "Yeah he was just completely unbreakable."

    scene s675e #MC walks to a portrait of a brunette guy with glasses, a nerdy and scrawny looking guy.
    with dissolve

    u "Okay, what about the last guy? He can't possibly be a Fight King, right?"

    ch "I told you, we don't discriminate based on prejudices. That's Earl Levington. He was a brain, probably the smartest Wolf we ever had."

    ch "He would plan out his moves methodically. He would analyze the way his opponents fought and prepare every possible move."

    scene s674
    with dissolve

    ch "I mean he barely got hit. He dodged almost every punch thrown at him based on his opponents' micro expressions."

    scene s674a
    with dissolve

    u "Now that's actually insane."

    u "So all these guys were Wolves Presidents too?"

    scene s674d
    with dissolve

    ch "Yup. Each and every one of them was at some point in their lives."

    scene s674e
    with dissolve

    menu:
        "Why aren't you on here?":
            $ reputation.add_point(RepComponent.BRO)
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            u "So, I don't know if it's weird asking, but if you're not one of the Fight Kings, how come you're the current President?"

            scene s674
            with dissolve

            ch "Well the year before me, Chuck was President. It was his last year, so I got voted in."

            ch "We need a new President every one or two years so some Presidents aren't Fight Kings."

            ch "Of course my goal is to become one and get on that wall."

            ch "But I also believe that being President whilst someone else wins for the Wolves is just as big of an honor as winning yourself."

            ch "A good leader doesn't need to be the best fighter."

            scene s674a
            with dissolve

            u "Yeah, I can see that. But winning must be surreal too."

        "That's really impressive":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            u "That's really impressive. Winning the entire tournament must be surreal."

    label hg_ad: #for compatibility only
    scene s674
    with dissolve

    ch "Of course. Good thing we're taking the crown back this year, I can feel it."

    scene s675f
    with dissolve

    u "So that's what the empty frame is for, huh?"

    ch "You gotta manifest your beliefs. Only way to make 'em come true."

    scene s674
    with dissolve

    ch "I bought the frame preemptively because I know that this will be our year."

    scene s674a
    with dissolve

    u "Well it's good you're prepared."

    scene s674d
    with dissolve

    ch "Yeah."

    ch "So pledging starts tomorrow at 6pm right here at the Wolves house."

    ch "I gotta get back downstairs now. I hope I'll see you tomorrow."

    scene s674e
    with dissolve

    u "Yeah, alright. Thanks."

    stop music fadeout 3

    scene s674g # chris gone
    with fade

    u "(I should go back down too.)"

######## SCENE 2 End of the Party
    play music "music/mparty2.mp3"

    queue music [ "music/mparty3.mp3", "music/mparty4.mp3"]

    if CharacterService.is_mad(imre):
        scene s680 # showing mc in Wolves house living room where Aaron is talking to Aubrey
        with fade

        u "(I wonder if Imre is here... Maybe this would be a good time to patch things up between us.)"

        u "Aubrey."

        scene s682 # aubrey close up smiling, and one eyebrow down like she's suspicious
        with dissolve

        au "Yeah?"

        scene s682a
        with dissolve

        u "Have you seen Imre?"

        scene s682
        with dissolve

        au "Who's Imre again?"

        scene s681 # close up aaron smiling
        with dissolve

        aa "I've seen him."

        scene s681b # close up aaron thinking about sexy times look
        with dissolve

        aa "He left with this hot blonde like 10 minutes ago."

        scene s681c
        with dissolve

        u "Oh, alright. Thanks."

        scene s687 # mc walking from the living room into the kitchen
        with dissolve

        u "(Dammit.)"

    else:
        scene s680 # showing mc in living room where Aaron is talking to Aubrey
        with fade

        u "(I'll go check on Imre and see if he wants to go home soon.)"

        u "Aaron."

        scene s681 # close up aaron smiling
        with dissolve

        aa "What's up, my bro?"

        scene s681a
        with dissolve

        u "Have you seen Imre?"

        scene s681b # close up aaron thinking about sexy times look
        with dissolve

        aa "Oh yeah, he left with this hot blonde like 10 minutes ago."

        scene s681c
        with dissolve

        u "Oh, alright. Thanks."

        scene s687 # mc walking from the living room into the kitchen
        with dissolve

        u "(I guess I'm going home without him.)"

    if "riley" in freeroam3 and not askfinn and upstairs != "riley" and not joinapes:
        ri "[name]?"

        scene s683a #Closeup riley mouth closed standing in kitchen curious
        with dissolve

        u "Yeah, what's up, Riley?"

        scene s683
        with dissolve

        ri "I'm gonna head out, just wanted to see if you're gonna live up to your promise and walk me home like you said."

        scene s683a
        with dissolve

        u "Uhm-"

    label nonoriri: #for compatibility only
    scene s684 # showing Nora and Chris arguing
    with dissolve

    no "Can you just not for once? You do this every single fucking time. I just don't get it!"

    scene s684a #Nora storms off to the garden
    with dissolve

    pause 0.5

    scene s685 # Chris upset close up looking after her
    with dissolve

    ch "Nora! C'mon! Don't do that!"

    scene s685a #Chris turns to one of his friends and begins talking to him.
    with dissolve

    ch "I swear she finds new reasons to get upset every day."

    if "riley" in freeroam3 and not askfinn:
        scene s683
        with dissolve

        ri "Soo? Are you walking me home?"

        menu:
            "Walk Riley home":
                $ reputation.add_point(RepComponent.BRO)

                scene s683a
                with dissolve

                $ grant_achievement("true_to_self")
                
                u "Uhh, yeah of course."

                scene s683b # Riley smiling
                with dissolve

                ri "Great, let's go."

                jump hd_ad

            "Go after Nora":
                $ reputation.add_point(RepComponent.TROUBLEMAKER)

                scene s683a
                with dissolve

                u "Uhm... I don't mean to do this, but I told a friend I was gonna catch up with him since yesterday and it just slipped my mind."

                scene s683d # Riley a bit sad
                with dissolve

                ri "Really? Okay..."

                scene s683e
                with dissolve

                u "Yeah, I'm really sorry. I just completely spaced it."

                scene s683d
                with dissolve

                ri "Yeah, it's okay. I asked you after. It's cool."

                scene s683e
                with dissolve

                u "Thanks. Get home safe."

    else:
        scene s686 # First person looking at backyard door that nora just walked out of
        with dissolve

        u "(Wow, Nora seemed really upset...)"

        menu:
            "Go after Nora":
                $ reputation.add_point(RepComponent.BOYFRIEND)

                u "(I should go after her and make sure she's okay.)"

            "Leave her alone":
                $ reputation.add_point(RepComponent.BRO)

                u "(I should leave her alone, she probably just wants to be alone right now.)"
                u "(It's late anyway, I better go home.)"

                jump conwalkhome

####### SCENE 3 Outside with Nora
label hd_bd:
    stop music fadeout 1
    play sound "sounds/dooropen.mp3"
    scene s688 # You walk open the backyard door
    with dissolve

    pause 0.5

    scene s698 # showing Nora standing with her back to you in the garden
    with dissolve

    u "Hey."

    play music "music/muffledparty.mp3"

    scene s698a # Nora turns around a bit sad and upset looking at you
    with dissolve

    pause 0.5

    if not "nora" in freeroam3:
        scene s699 # Close up Nora upset, a bit passive aggressive
        with dissolve

        no "Yeah?"

        scene s699a
        with dissolve

        u "You okay? I saw you run out. You look upset."

        scene s699
        with dissolve

        no "Yeah. I'm fine."

        scene s699a
        with dissolve

        u "You wanna talk about it?"

        scene s699
        with dissolve

        no "Not really."

        scene s699a
        with dissolve

        u "I'm here if you ever wanna talk."

        scene s699
        with dissolve

        no "It's not really your issue to deal with."

        scene s699a
        with dissolve

        u "That doesn't mean I can't help."

        scene s699b # a bit less upset / mad
        with dissolve

        no "I get it. I appreciate you trying, but I'd rather just be alone."

        scene s699c
        with dissolve

        u "Alright. I'll leave."

        scene s699b
        with dissolve

        no "Thanks."

        scene s700 # showing mc walking back inside
        with dissolve

        u "(It's really late so I might as well go home now.)"

    elif CharacterService.is_mad(nora):
        scene s699
        with dissolve

        no "What do you want?"

        scene s699a
        with dissolve

        u "Just wanted to make sure you're okay."

        scene s699
        with dissolve

        no "Why? So you can accuse me of being a jealous bitch again?"

        scene s699a
        with dissolve

        u "Okay first of all, that's not what I said. Also I just saw you run out and I was concerned. That's all."

        scene s699
        with dissolve

        no "Can you just leave me alone? I don't need another lecture."

        scene s699a
        with dissolve

        u "Nora, I didn't-"

        scene s699b
        with dissolve

        no "Please."

        scene s699c
        with dissolve

        u "Yeah, alright. Sorry."

        scene s700 # showing mc walking back inside
        with dissolve

        u "(It's really late so I might as well go home now.)"

    else:
        scene s699
        with dissolve

        no "Yes?"

        scene s699a
        with dissolve

        u "I saw you run out, you looked pretty upset."

        scene s699b
        with dissolve

        no "Yeah, just feels like a load of shit tonight. One thing after the other."

        scene s699c
        with dissolve

        u "You wanna talk about it?"

        scene s699b
        with dissolve

        no "It's just Chris... Sometimes he makes me feel like I don't even matter to him.. He's so, so, he just cares about the frat so much more than about me."

        scene s699c
        with dissolve

        u "I'm sure Chris cares about you much more than he shows."

        scene s699b
        with dissolve

        no "Maybe... Like it's fine that he's President and all and that's important, but he's been with everyone all night."

        no "I just wanted to know if he would wanna go to bed soon so we can at least have some private couple time this week."

        scene s699b
        with dissolve

        u "Yeah, I get that. Like you should make time for each other. You make time for him as well when you're busy, right?"

        scene s699d # Nora still a bit sad but also hopeful that you believe her
        with dissolve

        no "Yeah, right. So you don't think I'm overreacting?"

        scene s699e
        with dissolve

        u "Not at all."

        scene s699d
        with dissolve

        no "And he doesn't see it at all. Every time I try to say something to him, he tells me that I'm being selfish and don't care about the Wolves at all."

        no "I'm literally so supportive of him... It's annoying that he doesn't even see that."

        scene s699e
        with dissolve

        u "I can imagine."

        u "You know what I think you need right now?"

        scene s699d
        with dissolve

        no "What?"

        scene s699e
        with dissolve

        u "I think you need someone to cheer you up."

        scene s699b
        with dissolve

        no "And you let me guess, you're that someone."

        scene s699c
        with dissolve

        u "Come on let's do something fun. It'll take your mind of things."

        if reputation() == Reputations.CONFIDENT:
            call screen reputation_popup

            scene s699f # nora curious smile
            with dissolve

            no "Okay, let me hear it."

            scene s699g
            with dissolve

            u "Let's play never have I ever."

            scene s699f
            with dissolve

            no "Really? You can't be serious."

            scene s699g
            with dissolve

            u "It'll be fun. Come on!"

            scene s699f
            with dissolve

            no "We don't even have drinks."

            scene s699g
            with dissolve

            u "Give me one second."

            scene s700 # showing mc walking back inside
            with dissolve

            pause 0.5

            scene s700a # mc grabbing two beers from the fridge
            with dissolve

            pause 0.5

            scene s700b # mc comes back to Nora with 2 beers, handing one to Nora
            with dissolve

            u "Here you go."

            scene s701 # Nora and mc sitting down on the ground
            with dissolve

            no "Alright, fine. You start."

            scene s702a # Close up Nora sitting down looking at you slight smile and eyebrow raised a bit mouth closed
            with dissolve

            u "Alright, let's see... Uh.. Never have I ever... stolen a car."

            scene s702b # Nora drinks
            with dissolve

            u "What!? You serious! That one I thought for sure was just a shot in the dark. Haha."

            scene s702d # Nora laughing/ smiling
            with dissolve

            no "Nothing crazy. Was just my parent's car. I was like 13."

            scene s702e
            with dissolve

            u "Man, you're wild."

            scene s702f # Nora flirty
            with dissolve

            no "Okay, my turn. Hmm... Never have I ever... been hit in the face."

            scene s702g
            with dissolve

            u "Oh come on, that's not even fair."

            scene s703 # showing mc drinking
            with dissolve

            no "*Laughs* I like to win."

            scene s702g
            with dissolve

            u "Alright, you wanna play like that? Never have I ever hooked up with a guy."

            scene s702f # Nora flirty
            with dissolve

            no "Oh wow."

            scene s702b
            with dissolve

            u "You brought this onto yourself."

            scene s702f
            with dissolve

            no "Never have I ever..."

            no "Cheated on someone."

            if (CharacterService.is_girlfriend(lauren) and CharacterService.is_fwb(aubrey)) or (CharacterService.is_girlfriend(lauren) and CharacterService.is_fwb(emily)):
                scene s703 # showing mc drinking
                with dissolve

                no "Oh you pig."

                scene s702g
                with dissolve

                u "It's complicated."

                scene s702f
                with dissolve

                no "Sure."

                scene s702g
                with dissolve

            else:
                scene s702g
                with dissolve

                u "Nope, not me."

            u "Hmm... Never have I ever... hooked up with someone of the same gender."

            scene s702f
            with dissolve

            no "Not yet, but I really want to."

            scene s702g
            with dissolve

            u "Woah, really?"

            scene s702f
            with dissolve

            no "Yeah I just wanna explore another girls body and maybe oil each other up completely naked."

            scene s702g
            with dissolve

            u "Damn..."

            scene s702f
            with dissolve

            no "And then... maybe we can invite you to join us?"

            scene s702g
            with dissolve

            u "I uh-"

            u "Oh, you're just messing with me."

            scene s702d
            with dissolve

            no "*Laughs* Of course I'm just messing with you. You are aware that my boyfriend is like 20 feet away from us, right?"

            scene s702e
            with dissolve

            u "I was just playing along for the jokes, honestly."

            scene s702d
            with dissolve

            no "Sure you were."

            no "Anyway, I think I should probably call it a night. I'm beat."

            scene s702e
            with dissolve

            u "Yeah, it's super late."

            scene s702d
            with dissolve

            no "But thanks for cheering me up. I needed it."

            scene s702e
            with dissolve

            u "Yeah, of course."

            u "Well, good night and I'll see you soon."

            scene s702d
            with dissolve

            no "Yeah, good night."

            scene s703
            with dissolve

            u "(Time to go home.)"

        else:
            scene s699b
            with dissolve

            no "Honestly, I'm just not in the mood. I kind of just want to be alone right now."

            scene s699c
            with dissolve

            u "Oh, okay. I'll leave you be."

            scene s699b
            with dissolve

            no "Thanks."

            scene s700
            with dissolve

            u "(Time to go home, I guess.)"

####### SCENE 4 Walking Home by yourself
label conwalkhome:
    stop music fadeout 3

    scene s704 # mc walking home by himself at night
    with fade

    pause 1.0

    jump conyourdorm

######## SCENE 5 Walking Riley Home
label hd_ad:
    $ walkedRileyHome = True
    stop music fadeout 3

    scene s705 #Opening: You and Riley walking home at night
    with fade

    u "You had a good night?"

    scene s706 # Close up riley looking at you smiling
    with dissolve
    play music "music/mlove.mp3"

    queue music [ "music/mlove1.mp3" ]

    ri "Yeah, it was really fun getting to meet all of these new people."

    scene s706a
    with dissolve

    menu:
        "Keep it friendly":
            if CharacterService.is_girlfriend(lauren):
                $ reputation.add_point(RepComponent.BOYFRIEND)

            u "I'm glad. A lot of the Wolves seem really cool. How's classes going? Finish the econ assignment yet?"

            scene s706b # riley serious
            with dissolve

            ri "I did, but I might rewrite it. Just feel like I could add a few more references."

            scene s706c
            with dissolve

            u "I do too. We need like ten I think. How many do you have?"

            scene s706d # riley "embarrassed smile"
            with dissolve

            ri "35."

            scene s706c
            with dissolve

            u "35?! Are you kidding me? I have two."

            scene s706d # riley "embarrassed smile"
            with dissolve

            ri "*Chuckles* Well I got carried away a bit. But I still feel like there's more to add."

            scene s706c
            with dissolve

            u "*Laughs* You're aware you're dragging all of our grades down cause they grade the assignments comparatively."

            scene s706
            with dissolve

            ri "*Chuckles* Well maybe you should have added more references yourself then."

            scene s706a
            with dissolve

            u "You're impossible."

            scene s707 # opening  mc and riley in front of Riley's dorm, riley looking at mc, dorm door closed, riley mouth open smiling
            with fade

            ri "Thanks for bringing me home."

            scene s708a # riley smiling mouth closed close up
            with dissolve

            u "No worries, it was a nice walk."

            scene s708 # riley smiling
            with dissolve

            ri "Good night."

            scene s708a
            with dissolve

            u "Yeah, good night. Sleep well."

            stop music fadeout 3

            scene s709 # you walking through the dorm hallways to his dorm
            with fade

            pause 0.5

            jump conyourdorm

        "Start flirting":
            if CharacterService.is_girlfriend(lauren) :
                $ reputation.add_point(RepComponent.TROUBLEMAKER)

            $ reputation.add_point(RepComponent.BRO)

            u "I'd imagine. Plus you saved the best for last."

            scene s706d
            with dissolve

            ri "The best?"

            scene s706e
            with dissolve

            u "Well you're walking home with me, aren't you?"

            scene s706
            with dissolve

            ri "*Chuckles* Oh wow."

            scene s706a
            with dissolve

            u "You know, you look really good tonight."

            scene s706f # riley flirting
            with dissolve

            ri "I know."

            scene s706g
            with dissolve

            u "*Laughs* What? I did so not expect that response."

            scene s706
            with dissolve

            ri "*Laughs* It sounded a lot cooler in my head."

            if reputation() == Reputations.CONFIDENT:
                ri "I just thought. I'd give it a [name]-style response."

                scene s706a
                with dissolve

                u "[name]-style?"

                scene s706
                with dissolve

                ri "Yeah, you know how cocky you are. *Chuckles*"

                u "*Laughs* Unbelievable, I was just giving you a nice compliment and that's how you respond?"

            scene s706f
            with dissolve

            ri "You look good too."

            scene s706g
            with dissolve

            u "*Chuckles* Don't even think you can save this."

            scene s707 # opening  mc and riley in front of Riley's dorm, riley looking at mc, dorm door closed, riley mouth open smiling
            with fade

            ri "Thanks for bringing me home."

            scene s708a # riley smiling mouth closed close up
            with dissolve

            u "No worries, it was a nice walk."

            if reputation() == Reputations.CONFIDENT or CharacterService.is_kissed(riley):
                if CharacterService.is_friend(riley):
                    call screen reputation_popup

            else:
                scene s708 # riley smiling
                with dissolve

                ri "Good night."

                scene s708a
                with dissolve

                u "Yeah, good night. Sleep well."

                stop music fadeout 3

                scene s709 # you walking through the dorm hallways to his dorm
                with fade

                pause 0.75

                jump conyourdorm

    label conrileydorm: #for compatibility only
    scene s708b # riley slightly embarrassed / cute
    with dissolve

    ri "Hey uhm... do you maybe wanna come in?"

    menu:
        "Yeah, I'd like that":
            if CharacterService.is_girlfriend(lauren) or CharacterService.is_fwb(emily):
                $ reputation.add_point(RepComponent.TROUBLEMAKER)

            $ reputation.add_point(RepComponent.BRO)
            $ CharacterService.set_mood(riley, Moods.TEASED)

            u "Yeah, I'd like that."

            scene s708
            with dissolve

            ri "Okay, but we have to be quiet. My roommate is sleeping."

            scene s708a
            with dissolve

            u "Of course."

            play sound "sounds/dooropen.mp3"

            scene s710 # First Person Riley quietly walking in her dorm in front of you # ALL RILEY DORM renders should be regular lighting and I'll make it dark in photoshop
            with dissolve

            pause 0.5

            scene s711 # FIRST PERSON: Riley lies down in her bed under the blanket
            with dissolve

            pause 0.5

            scene s711a # Riley turns towards you, holds up the blanket to let you in and whispers to you
            with dissolve

            ri "*Whispers* Are you gonna come?"

            scene s712a # closeup  First person: Riley looking at you slightly seductive but also slightly smiling mouth closed
            with dissolve

            u "*Whispers* This is like a James Bond movie."

            scene s712
            with dissolve

            ri "*Whispers* Cause of all the sneaking?"

            scene s712a
            with dissolve

            u "*Whispers* No, cause of the pretty girl."

            scene s712
            with dissolve

            ri "*Laughs*"

            scene s712d # riley close up face, worried
            with dissolve

            ri "*Whispers* Shit. That was way too loud."

            scene s712e
            with dissolve

            u "*Whispers* Don't worry I don't think your roommate woke up."

            scene s712d # riley close up face, worried
            with dissolve

            ri "*Whispers* I really don't want her to. Maybe we can do this some other time?"

            scene s712e
            with dissolve

            u "*Whispers* Really?"

            scene s712d
            with dissolve

            ri "*Whispers* It's too risky, I don't think I could control myself."

            scene s712e
            with dissolve

            u "*Whispers* But-"

            scene s712
            with dissolve

            ri "*Whispers* We'll find another night."

            scene s712a
            with dissolve

            u "*Chuckles* *Whispers* Okay, deal."

            u "*Whispers* I'm gonna go home now then. Good night. Sleep well."

            stop music fadeout 4.0

            scene s712b
            with dissolve

            ri "*Whispers* Yeah, sounds good. Good night."

            scene s709 # you walking through the dorm hallways to his dorm
            with fade

            pause 0.5

        "Uhm... I shouldn't":
            if CharacterService.is_girlfriend(lauren) or CharacterService.is_fwb(emily):
                $ reputation.add_point(RepComponent.BOYFRIEND)

            u "Uhm... I probably shouldn't. It's quite late."

            scene s708b
            with dissolve

            ri "Oh yeah, of course. Uhm... good night."

            scene s708c
            with dissolve

            u "Yeah, good night."

            stop music fadeout 3

            scene s709 # you walking through the dorm hallways to his dorm
            with fade

            pause 0.5

########## SCENE 6 MC IN DORM
label conyourdorm:
    scene s713 # mc lying in bed at night sleeping
    with dissolve

    pause 0.5

    scene s713a # mc waking up in the morning
    with Fade(2,0,2)

    play music "music/mindie1.mp3"

    queue music [ "music/m15punk.mp3" ]

    pause 0.5

    $ v7_kiwiiPost1 = KiwiiPost(chloe, "phone/kiwii/Posts/v7/clpost1.webp", _("I'll always follow the sun :)"), number_likes=186)
    $ v7_kiwiiPost1.newComment(grayson, _("Check your DMs"), 14)
    $ v7_kiwiiPost1.newComment(ryan, _("Whore."), 1)
    $ v7_kiwiiPost1.newComment(aubrey, _("What I wouldn't give for your body..."), 32)
    $ v7_kiwiiPost1.newComment(elijah, _("If you ever need a tutor, I'm free on Wednesdays and Fridays."), 2)
    $ v7_kiwiiPost1.newComment(imre, _("SO FUCKING HOT WTFFF"), 10)
    $ v7_kiwiiPost1.newComment(emily, _("Where did you get that bikini?"), 18, mentions=[chloe])
    $ v7_kiwiiPost1.newComment(chloe, _("I can't remember :("), 11, mentions=[emily])
    $ v7_kiwiiPost1.addReply(_("You're so beautiful!"), v7_kiwiiReply1, number_likes=renpy.random.randint(2, 8))
    $ v7_kiwiiPost1.addReply(_("I got some sun in my room..."), v7_kiwiiReply2, number_likes=renpy.random.randint(20, 30))

    $ v7_kiwiiPost2 = KiwiiPost(lauren, "phone/kiwii/Posts/v7/lapost1.webp", _("Wishing I could go back..."), number_likes=39)
    $ v7_kiwiiPost2.newComment(autumn, _("That was such a great vacation!"), 2)
    $ v7_kiwiiPost2.newComment(penelope, _("Omg beautiful!"), 3)
    $ v7_kiwiiPost2.addReply(_("You're a cutie!"), v7_kiwiiReply3, number_likes=renpy.random.randint(3, 10))
    $ v7_kiwiiPost2.addReply(_("Winter vacations are the best"), v7_kiwiiReply4, number_likes=renpy.random.randint(10, 17))

    $ v7_kiwiiPost3 = KiwiiPost(aubrey, "phone/kiwii/Posts/v7/aupost1.webp", _("Finally changed my profile pic!"), number_likes=133)
    $ v7_kiwiiPost3.newComment(cameron, _("You put the hot into thot"), 2)
    $ v7_kiwiiPost3.newComment(josh, _("You still single?"), 3)
    $ v7_kiwiiPost3.newComment(riley, _("Holy hell... gorgeous Aubs!"), 6)
    $ v7_kiwiiPost3.newComment(chloe, _("Most beautiful girl in the world <3"), 6)
    $ v7_kiwiiPost3.addReply(_("I'd destroy you in Air hockey!"), v7_kiwiiReply5, mentions=[aubrey], number_likes=renpy.random.randint(15, 25))

    if CharacterService.is_fwb(emily): # first riley texts, then once you've opened the app you get 2 more messages.
        $ v7_kiwiiPost4 = KiwiiPost(emily, "phone/kiwii/Posts/v7/empost1.webp", _("Finally fate brings us back together. What doesn't kill us only makes us stronger."), number_likes=82)
        $ v7_kiwiiPost4.newComment(riley, _("You guys are so cute"), 5)
        $ v7_kiwiiPost4.newComment(aubrey, _("GORGEOUS"), 8)
        $ v7_kiwiiPost4.newComment(josh, _("Woah, you guys back together??"), 3)
        $ v7_kiwiiPost4.addReply(_("No, we're not."), v7_kiwiiReply6, mentions=[josh], number_likes=renpy.random.randint(5, 15))

        play sound sound.vibrate

        $ MessengerService.new_message(riley, _("Are you and Emily back together?"))
        $ MessengerService.add_reply(riley, _("What are you talking about???"))
        $ MessengerService.new_message(riley, _("Check Kiwii..."))
        $ kiwii_first_time = True

        pause 0.5

        scene s713b # mc looks at his phone
        with dissolve

        u "(What the hell?)"
        
        while MessengerService.has_replies(riley):
            call screen phone
            if MessengerService.has_replies(riley):
                u "(I need to respond to some of these messages.)"

        while kiwii_first_time:
            call screen phone
            if kiwii_first_time:
                u "I should check out what emily posted on kiwii"

        while MessengerService.has_replies(penelope):
            call screen phone
            if MessengerService.has_replies(penelope):
                u "(I should answer Penelope.)"

        while MessengerService.has_replies(lauren):
            call screen phone
            if MessengerService.has_replies(lauren):
                u "(I should respond to Lauren.)"

        if bowling and CharacterService.is_fwb(emily):
            $ v7_emily_bowling = True

        label continueee: #for compatibility only
        scene s714a # mc calm mouth closed
        with dissolve # mc sitting on his bed shirtless with his phone to his head, like he's on the phone

        play sound sound.calling

        u "(Okay... I need to call Emily right now.)"

        u "(What the fuck was she thinking?!)"

        stop sound

        em "Hey, babe."

        menu:
            "Be calm":
                $ reputation.add_point(RepComponent.BOYFRIEND)

                scene s714
                with dissolve
                #If you decide to be calm:

                u "Emily."

                scene s714a
                with dissolve

                em "Yeah?"

                scene s714
                with dissolve

                u "*Takes a deep breath*"

                scene s714a
                with dissolve

                em "Something wrong?"

                scene s714a
                with dissolve

                u "Yeah."

                scene s714a
                with dissolve

                em "What happened?"

                scene s714
                with dissolve

                u "That picture you posted. I need you to take it down."

                scene s714a
                with dissolve

                em "Why?"

                scene s714
                with dissolve

                u "Because I just don't feel comfortable with the photo. A lot of people think we're back together and the photo really does look like we are."

                scene s714a
                with dissolve

                em "And you don't want that?"

                scene s714
                with dissolve

                u "Look, I don't know what the future holds, but right now I don't wanna get back together."

                scene s714a
                with dissolve

                em "It's not like we were kissing or anything on the picture."

                scene s714
                with dissolve

                u "Yeah but... but you knew exactly what message it'd send out to everyone."

                scene s714a
                with dissolve

                em "Sorry... I just-"

                scene s714
                with dissolve

                u "Please just take it down."

                scene s714a
                with dissolve

                em "Okay, I will. I'm sorry."

                scene s714
                with dissolve

                u "I gotta go."

                scene s714a
                with dissolve

                em "Oh, yeah... Okay. Sorry."

                play sound "sounds/rejectcall.mp3"
                scene s714d
                with dissolve
                u "*Sighs*"

                $ v7_kiwiiPost4.remove_post()

                if CharacterService.is_girlfriend(lauren):
                    u "(Time to make things right with Lauren.)"
                    jump thisbelauren

                else:
                    u "(I need to clear my head. Maybe going for a walk will help.)"

                    if CharacterService.is_mad(lauren):
                        u "(But I should probably stop by Lauren's dorm first and see if we can talk things out... She's still mad at me and it really sucks.)"
                        jump apologylauren
                        
                    else:
                        jump thisbewalk

            "Get angry":
                $ reputation.add_point(RepComponent.TROUBLEMAKER)

                scene s714b # mc angry mouth open
                with dissolve

                u "Emily, what the fuck?!"

                scene s714c
                with dissolve

                em "Jeez. What are you getting so worked up about?"

                scene s714b
                with dissolve

                u "Don't play stupid Emily. You know why I'm pissed."

                scene s714c
                with dissolve

                em "Is this about the photo I posted?"

                scene s714b
                with dissolve

                u "Hell yeah, this is about the photo you posted. What else would I be pissed about?!"

                scene s714c
                with dissolve

                em "It's just a photo! I don't understand why you're getting so upset."

                scene s714b
                with dissolve

                u "You purposefully made it look like we're back together and you know we're not. We hooked up, big deal."
                scene s714c
                with dissolve

                em "Okay, okay. Calm down. You don't need to raise your voice at me."

                scene s714b
                with dissolve

                u "You know that we're not getting back together, right???"

                scene s714c
                with dissolve

                em "Yeah, I mean... I was just- I just really enjoyed spending time with you again..."

                scene s714b
                with dissolve

                u "Take the fucking post down. We're done. This is done."

                scene s714d # mc looking dpeesperate holding his phone in front of his face mouth closed
                with dissolve
                play sound "sounds/rejectcall.mp3"

                u "(I forgot how fucking crazy she is...)"

                $ v7_kiwiiPost4.remove_post()

                if CharacterService.is_girlfriend(lauren):
                    u "(Time to make things right with Lauren.)"
                    jump thisbelauren

                else:
                    u "(I need to clear my head. Maybe going for a walk will help.)"
                    jump thisbewalk

    else:
        play sound sound.vibrate

        $ MessengerService.new_message(riley, _("Hey, how come you're not on Kiwii?"))
        $ MessengerService.add_reply(riley, _("What's that?"))
        $ MessengerService.new_message(riley, _("It's a new social media app, you should give it a try"))
        $ MessengerService.add_reply(riley, _("Okay, I'll have a look"))
        $ kiwii_first_time = True

        pause 0.5

        scene s713b # mc looks at his phone
        with dissolve

        u "(Huh? What did Riley text me?)"

        while MessengerService.has_replies(riley):
            call screen phone
            if MessengerService.has_replies(riley):
                u "(I should respond to Riley.)"
            
        scene s713b2 # mc looks up to the window in the same position of 713b
        with dissolve
        u "(It's a nice day for a walk. It'll do me good.)"

        if CharacterService.is_mad(lauren):
            u "(But I should probably stop by Lauren's dorm first and see if we can talk things out... She's still mad at me and it really sucks.)"

        else:
            jump thisbewalk


##### SCENE 7 LAUREN'S DORM
label apologylauren:
    $ seenlauren = True

    stop music fadeout 3
    scene s715 # mc walking through dorm hallways
    with fade

    pause 0.5

    scene s716 #mc knocks on lauren's door
    with dissolve

    play sound sound.knock

    pause 1.5

    play sound "sounds/dooropen.mp3"

    scene s717 #close up Lauren opening door mouth open  a bit upset / put off
    with dissolve

    la "[name]? What are you doing here?"

    play music "music/mindie5.mp3"

    queue music [ "music/mlove2.mp3" ]
    # No but should everything be forgiven? I think so. But you can't make a move on her at the beach I guess in some instances

    scene s717a
    with dissolve

    if not apologize:
        u "Listen, I wanted to apologize, I'm sorry for what I did and I hope you can forgive me. I was gonna apologize a few days ago, but I wanted to give you some more time."

    else:
        u "Listen, I know you said you needed more time, but it's been a few days and I just really want to be friends again... I know I messed up."

    if not CharacterService.is_mad(autumn):
        $ CharacterService.remove_mood(lauren, Moods.MAD)
        
        scene s717
        with dissolve

        la "Yeah... I talked to my sister about it and she helped me understand that you didn't do it with ill intentions."

        la "Look I've missed you as friend to talk to and I'd just like everything to get back to normal."

        scene s717a
        with dissolve

        u "Great, that's what I want too."

        scene s717b # Lauren smiling
        with dissolve

        la "Hey, I was gonna go to the beach today with Autumn, but she's got to work. Do you wanna go?"

        menu:
            "Sounds great!":
                scene s717c
                with dissolve

                u "Yeah, that sounds great! Just let me know."

                scene s717b
                with dissolve

                la "Okay, will do. I'll see you then!"

                scene s717c
                with dissolve

                u "Cool, see you then."

            "I can't today":
                $ nobeach = True

                scene s717c
                with dissolve

                u "Sorry, I'm quite busy today, but I'll see you soon, okay?"

                scene s717
                with dissolve

                la "Oh okay, no problem. See you soon."

        scene s718 # mc walking back to his dorm
        with fade

        u "(I'm glad Lauren's no longer mad at me.)"

        u "(It's also a nice day for a walk... Couldn't hurt to stretch my legs.)"

        jump thisbewalk

    elif reputation() == Reputations.LOYAL:
        $ CharacterService.set_relationship(lauren, Relationship.FRIEND, mc)
        $ CharacterService.remove_mood(lauren, Moods.MAD)
        call screen reputation_popup

        scene s717
        with dissolve

        la "Yeah... I thought a lot about it and I understand that you didn't do it with ill intentions."

        la "Look I've missed you as friend to talk to and I'd just like everything to get back to normal."

        scene s717a
        with dissolve

        u "Great, that's what I want too."

        scene s717b # Lauren smiling
        with dissolve

        la "Hey, I was gonna go to the beach today with Autumn, but she's got to work. Do you wanna go?"

        menu:
            "Sounds great!":
                scene s717c
                with dissolve

                u "Yeah, that sounds great! Just let me know."

                scene s717b
                with dissolve

                la "Okay, will do. I'll see you then!"

                scene s717c
                with dissolve

                u "Cool, see you then."

            "I can't today":
                $ nobeach = True

                scene s717c
                with dissolve

                u "Sorry, I'm quite busy today, but I'll see you soon, okay?"

                scene s717
                with dissolve

                la "Oh okay, no problem. See you soon."

        scene s718 # mc walking back to his dorm
        with fade

        u "(I'm glad Lauren's no longer mad at me.)"

        u "(It's also a nice day for a walk... Couldn't hurt to stretch my legs.)"

        jump thisbewalk

    else:
        $ CharacterService.set_mood(lauren, Moods.MAD)
        
        scene s717
        with dissolve

        la "Yeah... I thought a lot about it and I understand that you didn't do it with ill intentions."

        la "We can be friends again, but it might take some time for everything to go back to normal. I'm still unsure about how I feel."

        scene s717a
        with dissolve

        u "That's totally fine. I'm glad we can be friends again."

        scene s717
        with dissolve

        la "Me too... I guess I'll see you around."

        scene s717a
        with dissolve

        u "Uhm yeah, okay, cool."

        u "See you around."

        scene s718 # mc walking back to his dorm
        with fade

        u "(Not ideal, but at least she's willing to be friends again...)"

        u "(I could really use a walk to clear my head.)"

        jump thisbewalk

label thisbelauren:
    $ seenlauren = True
    scene s715 # mc walking through dorm hallways
    with fade

    pause 0.5

    scene s716 #mc knocks on lauren's door
    with dissolve

    play sound sound.knock

    pause 1.5

    play sound "sounds/dooropen.mp3"

    scene s717
    with dissolve

    la "So?"
    play music "music/mindie5.mp3"

    queue music [ "music/mlove2.mp3" ]

    scene s717a
    with dissolve

    u "Should I maybe come in?"

    scene s717
    with dissolve

    la "No, we can talk about this here."

    scene s717a
    with dissolve

    menu:
        "Come clean about Emily":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            u "I'm just gonna come right out and say it."

            scene s717
            with dissolve

            la "What?"

            scene s717a
            with dissolve

            u "Yes, I did hook up with Emily. And before you say anything, I entirely regret it. I don't know what I was thinking."

            scene s717e # lauren sad mouth closed
            with dissolve

            la "*Takes a deep breath*"

            scene s717d
            with dissolve

            la "Then why'd you do it?"

            scene s717e
            with dissolve

            u "I don't know, Lauren! I wish I had an answer for you, I really do. But I don't know why I did it."

            u "I mean she just kissed me and old feelings came up... and stuff happened."

            scene s717f # Lauren really sad
            with dissolve

            la "*Sniff* It just doesn't make sense, why are we even dating if you're just gonna hook up with any girl you see???"

            scene s717g
            with dissolve

            menu:
                "This won't happen again":
                    $ reputation.add_point(RepComponent.BOYFRIEND)

                    u "Like I said, it was a stupid mistake. After it happened, I realized that's not what I want at all."

                    scene s717f
                    with dissolve

                    la "Then what is it you want?"

                    scene s717g
                    with dissolve

                    u "You. Of course I want you. That's all I want. I promise. It's never gonna happen again."

                    if reputation() == Reputations.LOYAL:
                        call screen reputation_popup

                        $ CharacterService.set_relationship(lauren, Relationship.FRIEND)
                        $ CharacterService.set_mood(autumn, Moods.MAD)

                        scene s717
                        with dissolve

                        la "*Takes a deep breath* I need some time to process this. Could I just be alone for a while?"

                        scene s717a
                        with dissolve

                        u "Of course. Take all the time you need."

                        scene s718 # mc walking back to his dorm
                        with fade

                        u "(Not ideal, but at least we're still talking...)"

                        u "(I could really use a walk to clear my head.)"

                    else:
                        $ CharacterService.set_relationship(lauren, Relationship.FRIEND)
                        $ CharacterService.set_mood(lauren, Moods.MAD)
                        $ CharacterService.set_mood(autumn, Moods.MAD)

                        scene s717d
                        with dissolve

                        la "No, I can't do this [name]."

                        scene s717e
                        with dissolve

                        u "What do you mean?"

                        scene s717d
                        with dissolve

                        la "This, I can't do this. I can't do us."

                        scene s717e
                        with dissolve

                        u "I told you I was sorry, Lauren. It won't ever happen again."

                        scene s717f
                        with dissolve

                        la "I can't trust you. And without trust, there isn't a relationship. If you do it once, it means you'll do it again."

                        scene s717g
                        with dissolve

                        u "Lauren-"

                        scene s717f
                        with dissolve

                        la "I think you should go right now."

                        scene s717g
                        with dissolve

                        u "No, I'm not leaving."

                        scene s717f
                        with dissolve

                        la "Just go. I'm done. You want to go hookup with her again, you can. Because we're not dating anymore."

                        scene s717g
                        with dissolve

                        u "Lauren, stop."

                        scene s717f
                        with dissolve

                        la "I don't want to see you right now. Please just leave."

                        scene s717g
                        with dissolve

                        u "Fine. I'll go."

                        play sound "sounds/doorclose.mp3"
                        scene s717k # door closed
                        with vpunch

                        pause 0.5

                        u "(Fuck...)"

                        u "(I need to go for a walk and clear my head.)"

                "Open relationship?":
                    $ reputation.add_point(RepComponent.BRO)
                    $ reputation.add_point(RepComponent.TROUBLEMAKER)
                    $ CharacterService.set_relationship(lauren, Relationship.FRIEND)
                    $ CharacterService.set_mood(lauren, Moods.MAD)
                    $ CharacterService.set_mood(autumn, Moods.MAD)

                    u "Maybe we just rushed into this."

                    u "I mean, I really like you and I wanna be with you... but this is college."

                    u "Have you ever thought about having an open relationship?"

                    scene s717d
                    with dissolve

                    la "An open relationship? Like you'd be sleeping with other girls whilst we're dating?"

                    scene s717e
                    with dissolve

                    u "I mean yeah... I mean you'd be free to date other people as well. We could even try something with just a second girl-"

                    scene s717h # Lauren slightly angry and in disbelief
                    with dissolve

                    la "Okay, we're done."

                    scene s717j
                    with dissolve

                    u "Lauren, I didn't-"

                    scene s717h
                    with dissolve

                    la "I said we're done!"

                    play sound "sounds/doorclose.mp3"
                    scene s717k # door closed
                    with vpunch

                    pause 0.5

                    u "(Fuck...)"

                    u "(I need to go for a walk and clear my head.)"

        "Deny the cheating":
            $ reputation.add_point(RepComponent.BRO)
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            $ CharacterService.set_relationship(lauren, Relationship.GIRLFRIEND, mc)

            u "I know how this looks."

            u "I didn't cheat on you."

            scene s717d
            with dissolve

            la "And how am I supposed to believe you? That's your ex. You used to hook up with her. What would stop you now?"

            scene s717e
            with dissolve

            u "Emily is crazy. She's still in love with me and she's trying to destroy what we have."

            scene s717d
            with dissolve

            la "You're just saying that."

            scene s717e
            with dissolve

            u "No, she knows I'm with you and she's desperately trying to get me back. That's why she's posted this."

            u "She knows that stuff like this can easily weaken a relationship, but we can't let it weaken ours."

            scene s717
            with dissolve

            la "So you didn't hook up with her?"

            scene s717a
            with dissolve

            u "No! I'm telling you she's just crazy."

            scene s717b
            with dissolve

            la "Okay... I believe you."

            scene s717c
            with dissolve

            u "Thank god."

            scene s717b
            with dissolve

            la "Let's show Emily that she can't tear us apart with stupid accusations."

            scene s717c
            with dissolve

            u "Yes!"

            scene s717b
            with dissolve

            la "I was gonna go to the beach with Autumn later, but she has to work. Why don't we go?"

            scene s717c
            with dissolve

            u "Yeah, I'd love that. Just let me know when."

            scene s717b
            with dissolve

            la "Okay, I'll text you. See you later."

            scene s717c
            with dissolve

            u "Great, see you."

            scene s718 # mc walking back to his dorm
            with fade

            u "(Okay, I know lying to Lauren was wrong, but I just couldn't let her find out...)"

            u "(I should go for a walk and clear my head.)"

######## SCENE 8 Walk / Dog Shelter
label thisbewalk:
    scene s719 #mc on a walk outside in town
    with fade
    stop music fadeout 3

    pause 0.5

    u "(So much has happened in the last few days. I've met so many people and had so many new experiences.)"

    u "(I mean tonight pledging starts.. and after everything that's happened I'd rather join a frat than be without. Even if it means fighting.)"

    u "(At the end of the day, it does seem like the best way to make friends, meet girls and truly experience college.)"

    scene s720 #mc walking a couple feet further forward
    with dissolve

    u "(Shit... just remembered that tomorrow's also my next history lecture. Gotta make sure to remember wearing that stupid costume I bought...)"

    if not CharacterService.is_mad(autumn):
        $ v7_visited_shelter = True
        scene s721 # close up of dogshelter shop window
        with dissolve

        u "Didn't Autumn say she worked here? Maybe she's in."

        scene s722 # opening inside dog shelter, Autumn behind front desk, mc mouth open
        with fade

        u "Hey Autumn."

        play music "music/mfunk.mp3"

        queue music [ "music/mindie5.mp3" ]
        scene s723 # close up autumn curious smile
        with dissolve

        aut "Oh hey, [name]. Are you here to adopt a dog or...?"

        scene s723a
        with dissolve

        u "Just remembered you said you worked here. Thought I'd stop by."

        scene s723
        with dissolve

        aut "I was gonna say, I think there's a pet policy in the dorms. Haha."

        scene s723a
        with dissolve

        u "I mean I also remember you saying you'd let me play with some of the dogs if I came by."

        scene s723
        with dissolve

        aut "Hmm... that's true. Alright follow me."

        scene s724 # First person following Autumn to the back
        with dissolve

        pause 0.5

        scene s725 # first person sititng down with Autumn, she's playing with a french bulldog
        with fade

        aut "This is Oscar. He's probably our least shy one. He won't need to get to know you first in order to be affectionate."

        scene s725a # oscar walks to you
        with dissolve

        aut "Cute, right?"

        scene s727a # close up autumn smiling at you mouth closed
        with dissolve

        menu:
            "Almost as cute as you":
                if CharacterService.is_girlfriend(lauren):
                    $ reputation.add_point(RepComponent.TROUBLEMAKER)
                else:
                    $ reputation.add_point(RepComponent.BOYFRIEND)

                u "Almost as cute as you."

                scene s727b # close up autumn uncomfortable
                with dissolve

                aut "Uhhh..."

            "Yeah, he really is":
                u "Yeah, he really is."

        scene s726 # mc looking down playing with oscar
        with dissolve

        u "Can't believe you get to play with them all day."

        scene s727d # close up autumn no facial expression really
        with dissolve

        aut "Sadly, my job is mostly cleaning, feeding and dealing with administrative stuff."

        aut "Not a lot of playing."

        scene s726a # mc looking down playing with oscar a bit differently
        with dissolve

        u "So I know you're really into politics, right? Feminism and stuff?"

        scene s727
        with dissolve

        aut "Yes, that's right. However I wouldn't necessarily call myself a feminist, I just don't like the idea of classifications."

        aut "But yes I feel very strongly for the feminist movement and do very much care for women's rights."

        scene s726b # mc looking down playing with oscar even more differently
        with dissolve

        u "That's great. Equality is the way."

        scene s727
        with dissolve

        aut "Is there anything you fight for?"

        scene s727a
        with dissolve

        menu:
            "Yes, of course":
                $ reputation.add_point(RepComponent.TROUBLEMAKER)
                $ politics = True

                u "Yes, of course. I guess we all have something. Am I right?"

                scene s727
                with dissolve

                aut "You'd be surprised. Politics tend to scare people."

                scene s727a
                with dissolve

                u "Yeah, but if we're not the ones fighting for change, then who is?"

                scene s727
                with dissolve

                aut "So what is your cause then?"

                scene s727a
                with dissolve

                u "Uhm... my cause is..."

                scene s728 # close up of a poster on the wall that says "Western Animal movement"
                with dissolve

                u "The uhm Western... Animal movement."

                scene s727
                with dissolve

                aut "Oh animal rights, how fascinating. I have to admit, I haven't done much research into the Western Animal Movement... would you care to elaborate on its exact purpose and goals?"

                scene s727a
                with dissolve

                u "You know, uhm... it's like animal rights but more in the west."

                scene s726
                with dissolve

                u "Cause uhm... the eastern animal rights are uhm good. But the west, you know. I mean, that's where we gotta focus our energy."

                scene s727
                with dissolve

                aut "Oh, alright. I'll definitely check it out."

            "No, not really":
                $ reputation.add_point(RepComponent.BRO)

                u "No, not really. I'm not really into politics myself."

                scene s727d
                with dissolve

                aut "Oh, okay."

        scene s726a
        with dissolve

        u "So uhm... do you go to like a lot of protests and stuff like that?"

        scene s727
        with dissolve

        aut "Yeah, whenever I can. This Saturday I'm actually going to a protest for women's rights."

        scene s727a
        with dissolve

        menu:
            "Can I join?":
                $ reputation.add_point(RepComponent.BOYFRIEND)
                $ protest = True

                u "Really? Any chance I can join you?"

                scene s727
                with dissolve

                aut "You sure?"

                scene s727a
                with dissolve

                u "Yeah, I'd love to help."
                if politics:
                    $ signs = True

                    scene s727
                    with dissolve

                    aut "Wow, I'm surprised. But if you really want to then sure. I was gonna make my sign on Friday, if you want to join?"

                    scene s727a
                    with dissolve

                    u "Yeah, definitely. Just let me know when you're making them."

                elif reputation() == Reputations.LOYAL:
                    call screen reputation_popup

                    $ signs = True

                    scene s727
                    with dissolve

                    aut "Wow, I'm surprised. But if you really want to then sure. I was gonna make my sign on Friday, if you want to join?"

                    scene s727a
                    with dissolve

                    u "Yeah, definitely. Just let me know when you're making them."

                    scene s727
                    with dissolve

                    aut "Great, I will."

                else:
                    $ signs = False

                    scene s727
                    with dissolve

                    aut "Uhm, yeah. I'll see you there on Saturday then."

                    scene s727a
                    with dissolve

                    u "Great, sounds good."

                    scene s727
                    with dissolve

            "That's really cool":
                $ reputation.add_point(RepComponent.BRO)
                $ signs = False

                u "That's really cool."

                scene s727
                with dissolve

                aut "Yeah, thanks."

        aut "Anyway, I gotta get back to work soon."

        scene s727a
        with dissolve

        u "Yeah, of course. It was really nice seeing you."

        scene s726b
        with dissolve

        u "And thanks for letting me play with this little fella."

        scene s727
        with dissolve

        stop music fadeout 3

        aut "Yeah, no problem."

        if signs:
            aut "I'll see you on Friday."

            scene s727a
            with dissolve

            u "Yeah, I'll see you."

    scene s729 # mc walking around somewhere else in town
    with fade

    u "(Alright, time to get back to my dorm...)"

    ######## SCENE 9 - PENELOPE IN FRONT OF YOUR DORM
    scene s718
    with fade

    pause 0.5
    play music "music/mhappy.mp3"

    if (not costumeaubrey and v2_caughtpeeking and not v2_caughtpeekingcounter) or penelopekiss:
        scene s731 # First person, Penelope sitting in front of your dorm door
        with dissolve

        u "Penelope? What are you doing here?"

        scene s732 # close up penelope empathetic
        with dissolve

        pe "I feel bad about before. And I hate feeling like there's tension between us. I don't want to be angry at you."

        scene s732a
        with dissolve

        u "Uh, yeah. Thanks I guess."

        scene s732
        with dissolve

        pe "I just don't like the feeling of not getting along with someone, so I forgive you."

        scene s732a
        with dissolve

        u "I'm glad. And I'm sorry for everything. Let's just start over."

        scene s732b # penelope smiles
        with dissolve

        pe "I'd like that."

        pe "Okay, I actually didn't plan on sitting here this long, but I wanted to do this in person and not over text."

        scene s732c
        with dissolve

        u "Sorry, I was on a walk, haha."

        scene s732b # penelope smiles
        with dissolve

        pe "Yeah, no worries. I should probably go now, but I'll see you tomorrow in History 101."

        scene s732c
        with dissolve

        u "Yeah, sounds good."

    ############## SCENE 10 - MC IN HIS DORM WEDNESDAY NOON
    scene s733 # mc in his dorm
    with fade

    pause 0.5

    if not CharacterService.is_mad(lauren) and not nobeach:
        play sound sound.vibrate

        if seenlauren and CharacterService.is_girlfriend(lauren):
            $ MessengerService.new_message(lauren, _("Wanna go now babe?"))
            $ MessengerService.add_reply(lauren, _("Sure, I'll come pick you up"))
            $ MessengerService.new_message(lauren, _("Great :)"))

        elif seenlauren:
            $ MessengerService.new_message(lauren, _("Wanna go now?"))
            $ MessengerService.add_reply(lauren, _("Sure, I'll come pick you up"))
            $ MessengerService.new_message(lauren, _("Great :)"))

        else:
            $ MessengerService.new_message(lauren, _("Hey :)"))

            if CharacterService.is_girlfriend(lauren):
                $ MessengerService.new_message(lauren, _("You wanna go to the beach today?"))
                $ MessengerService.add_reply(lauren, _("Sounds good, when were you thinking?"))
                $ MessengerService.new_message(lauren, _("How about now?"))
                $ MessengerService.add_reply(lauren, _("Sure, I'll come pick you up"))
                $ MessengerService.new_message(lauren, _("Great :)"))

            else:
                $ v7_msgReply3 = MessageBuilder(lauren)
                $ v7_msgReply3.new_message(_("How about now?"))
                $ v7_msgReply3.add_reply(_("Sure, I'll come pick you up"))
                $ v7_msgReply3.new_message(_("Great :)"))

                $ v7_msgReply4 = MessageBuilder(lauren)
                $ v7_msgReply4.set_variable("nobeach", True)
                $ v7_msgReply4.new_message(_("Oh okay, another time then."))

                $ MessengerService.new_message(lauren, _("You wanna go to the beach today?"))
                $ MessengerService.add_replies(lauren,
                    Reply(_("Sounds good, when were you thinking?"), v7_msgReply3),
                    Reply(_("Sorry, I can't I'm really busy today"), v7_msgReply4)
                )

        while MessengerService.has_replies(lauren):
            call screen phone
            if MessengerService.has_replies(lauren):
                u "(I should probably reply.)"

        if nobeach:
            u "(Time to finish my history assignment...)"
            jump nobeach

        else:
            u "(Gotta put on my swim trunks and pick up Lauren.)"
            jump beachlauren

    else:
        u "(Ugh... I still gotta finish my history assignment before tomorrow.)"

        # lauren post on kiwii
        label nobeach:
            scene s733 # mc working at desk
            with fade

            pause 0.5

            if CharacterService.is_fwb(emily):
                scene s733a #mc turns his head to look at the door
                with dissolve

                pause 0.5

                scene s751 #shows a letter that's been slipped under the door.
                with dissolve

                u "(Huh?)"

                scene s752 # mc walks towards letter
                with dissolve

                pause 0.5

                scene s752a # mc picks it up
                with dissolve

                pause 0.5

                show screen letter1

                " "

                #em "Dear MC, I'm really sorry I posted that picture. I should have said something to you about it before. I guess I have to admit that I kind of miss you and I miss us being together. But most of all, I'd really like to make it up to you. Meet me at my dorm tonight at midnight. I'll have a surprise waiting for you xoxo."
                hide screen letter1
                scene s752b # mc walks to his desk with the letter in his hand
                with dissolve

                u "(Emily is just hot and cold... I'll have to see how I feel about it at midnight, but giving her yet another chance doesn't seem like a great idea.)"

                scene s755a # mc walking towards his bed and starts looking at his phone but you can't see the screen in jeans
                with dissolve

            jump afterbeach

########### SCENE 11 Beach trip with Lauren
label beachlauren:
    stop music fadeout 3

    scene s734 # mc walking through dorm hallways
    with fade

    pause 0.5

    scene s735 #mc knocks on lauren's door
    with dissolve

    play sound sound.knock

    pause 1.5

    play sound "sounds/dooropen.mp3"

    if CharacterService.is_girlfriend(lauren):
        play music "music/mlove2.mp3"
        queue music [ "music/mlove.mp3", "music/mlove1.mp3" ]

        scene s736 # showing Mc and Lauren , she's opening the door in a bikini. happy to see mc, mouth open
        with dissolve

        la "Heyyy!"

        scene s736a # lauren passionately kisses mc
        with dissolve

        play sound sound.kiss

        pause 1.0

        scene s736
        with dissolve

        la "How are you?"

        scene s737 #First person: close up lauren mouth closed happy
        with dissolve

        u "I'm good. You really missed me, huh?"

        la "Maybe just a little."

        scene s737b # Lauren turns around and walks inside her dorm

        la "Let me just throw something on and we can go."

        scene s738 # showing you and Lauren inside her dorm she's lookign at her closet, you're behind her grabbing her hand., you're mouth open smiling
        with dissolve

        u "Wait a minute-"

        scene s738a # lauren turns around, her mouth open curious
        with dissolve

        la "What?"

        u "You just look so good right now."

        scene s738avid  # Lauren and mc making out animation
        with dissolve

        pause 1.5

        scene s739a # lauren close up shy smile mouth closed
        with dissolve

        u "When I look at you, I just can't control myself. *Chuckles*"

        scene s739
        with dissolve

        la "Well we better get going because otherwise we won't leave this room before the sun's down."

        scene s739a
        with dissolve

        u "Would that be so bad?"

        scene s739
        with dissolve

        la "*Chuckles* Just give me five minutes."

        scene s740 # lauren and mc in the bus transition (lauren clothed)
        with fade

        pause 1.0

        scene s741 # opening mc and Lauren sitting on the beach (lauren in bikini and mc in swimshorts without shirt, back view camera
        with fade

        u "This is really nice."

        scene s742 # first person close up Lauren looking at you whilst sitting next to you smiling mouth open
        with dissolve

        la "Nice to get away from everything, isn't it?"

        scene s742a
        with dissolve

        u "I mean, it's nice being anywhere with you."

        scene s742
        with dissolve

        la "*Giggles* Awww."

        scene s742a
        with dissolve

        pause 0.5

        scene s742
        with dissolve

        la "So how are things with Imre?"

        scene s742a
        with dissolve

        if CharacterService.is_mad(imre):
            menu:
                "Tell her it's fine":
                    $ reputation.add_point(RepComponent.BRO)
                    $ reputation.add_point(RepComponent.TROUBLEMAKER)

                    u "Good, great. You know how he is. It's just uhm... really good."

                    scene s742
                    with dissolve

                    la "I'm happy for you, seems like you guys really have a strong friendship and that's really important when you live together."

                    scene s742b # lauren slightly annoyed
                    with dissolve

                    la "I wish I would be as close with my roommate as you guys are."

                    scene s742c
                    with dissolve

                    u "Yeah..."

                    u "I mean he's teaching me how to fight and everything..."

                "Tell her he moved out":
                    $ reputation.add_point(RepComponent.BOYFRIEND)

                    u "Uhm... Imre and I had a fight and he moved out..."

                    u "Not like a physical one, just an argument. You know how he is, a bit of a hothead."

                    scene s742d # Lauren empathy
                    with dissolve

                    la "Oh that's too bad. I thought you guys were such good friends, what happened?"

                    scene s742e
                    with dissolve

                    u "I don't really wanna get into the details. But I hope that we can be friends again once he cools down."

                    scene s742d
                    with dissolve

                    la "Aww... I hope so too."

                    scene s742e
                    with dissolve

                    u "It kinda sucks cause he was teaching me how to fight."

        else:
            u "Really good, we're getting along really well and he's teaching me how to fight.."

        scene s742b
        with dissolve

        la "Don't tell me you wanna be a fighter too now?"

        scene s742c
        with dissolve

        u "Look Lauren, I know you're not big on fighting, but being in a frat is so much more. And I just really think I'd miss out on a lot if I didn't join one."

        scene s742b
        with dissolve

        la "Yeah, you'd miss out on all the girls who love fighters..."

        scene s742c
        with dissolve

        u "Lauren, it's not that, come on. It's about the brotherhood and learning from each other and growing as a person."

        scene s742d
        with dissolve

        la "I just don't want you to get hurt."

        scene s742e
        with dissolve

        u "I'll be careful. I promise."

        scene s742f # lauren curious
        with dissolve

        la "So uhm... which frat are you gonna join then?"

        if joinapes:
            scene s742g
            with dissolve

            u "I mean pledging starts tonight, but I'm thinking the Apes."

            scene s742b
            with dissolve

            la "The Apes? Really?"

            scene s742c
            with dissolve

            u "What's wrong with the Apes?"

            scene s742b
            with dissolve

            la "They're obnoxious, arrogant and they don't even have the brotherhood you said you cared about."

            la "My sister told me a bunch about what they're like and I wouldn't want you to be one of them."

            scene s742c
            with dissolve

            u "C'mon I'll still be me. Are you saying you'd break this off if I join the Apes?"

            scene s742d
            with dissolve

            la "No [name]... but if you're already joining a frat, why not at least one that doesn't reek of toxic masculinity?"

            scene s742e
            with dissolve

            u "I'll give it some more thought... but I need you to know that I'm pretty set on it and you might not like my final decision."

            scene s742b
            with dissolve

            la "Okay..."

        else:
            u "I mean pledging starts tonight, but I'm pretty sure I'm gonna join the Wolves."

            scene s742
            with dissolve

            la "Well, at least it's not the Apes."

            scene s742a
            with dissolve

            u "Haha yeah."

            scene s742f
            with dissolve

            la "Are you sure that you've thought this through?"

            scene s742g
            with dissolve

            u "Yeah, pretty sure."

        scene s743 # showing both mc and Lauren from a close angle, lauren leaning closer to him, no one else around, mouth open flirting
        with dissolve

        la "It's just kinda unfortunate, because if you're joining a frat we won't have as much time for stuff like this."

        scene s743a # lauren climbs on top of mc, mc opens mouth surprised smile
        with dissolve

        u "*Chuckles* Woah, Lauren..."

        scene s743b # lauren very close to mcs face, mc has his hands on her hips, mc mouth open flirty
        with dissolve

        la "What? No one else is here. It's just us."

        scene s743c # lauren push mc down so that he's laying with his back on the sand / towel and starts kissing him
        with vpunch

        pause 0.5

        scene s743vid
        with dissolve
        
        pause 1.4

        scene s743apic
        with dissolve

        pause 0.75

        la "*Quiet moan* Mhmmm..."

        scene s745 # lauren mouth open, mc mouth closed
        with dissolve

        la "I'm really glad we're here together."

        scene s745a # close up of Lauren lying on top mc, mc mouth open lauren mouth closed, both smiling
        with dissolve

        u "Yeah, me too."

        scene s746 #OpeningL the lighting should be early evening now, time has passed, Lauren and mc laying on the respective blankets
        with Fade(1,0,1)

        pause 1.0

        scene s747 # Lauren close up laying next to you very slight smile, looking at you, with early evening lighting
        with dissolve

        la "Sun is going to go down soon. We should probably get going."

        scene s747a
        with dissolve

        u "Yeah, we should get back."

        scene s740 # lauren and mc in the bus transition (lauren clothed)
        with fade

        pause 1.0

        scene s748 # back inside Lauren's dorm, both clothed., Lauren and Mc standing quite close looking at each other
        with fade

        pause 0.5

        scene s749 #First person close up Lauren a bit sad mouth open
        with dissolve

        la "I wish you could stay, but I have to get ready for the Deer pledge night."

        scene s749a
        with dissolve

        u "Oh, so you're actually gonna try and join them?"

        scene s749b #Lauren no particular emotion
        with dissolve

        la "Yeah, I mean I know most of them really well and obviously my sister's the President so it's a pretty easy decision."

        scene s749c
        with dissolve

        u "I guess that's true, well good luck anyway."

        scene s749d # Lauren genuine smile
        with dissolve

        la "Thanks. For you too... even though I still don't fully approve."

        scene s748
        with dissolve

        pause 0.5

        scene s748a #lauren and mc kiss
        with dissolve

        play sound sound.kiss
        pause 0.5

        scene s748
        with dissolve

        pause 0.5

        scene s749e # Lauren genuine smile
        with dissolve

        u "I'll see you later."

        stop music fadeout 3

        scene s749d # Lauren genuine smile
        with dissolve

        la "Yeah, goodbye."

    else:
        scene s737
        with dissolve

        la "Oh hey, you're early."

        play music "music/mlove.mp3"
        queue music [ "music/mlove2.mp3", "music/mlove1.mp3" ]

        u "How else am I gonna catch the worm?"

        la "*Chuckles* What?"

        u "*Chuckles* It's a- you know what, never mind."

        scene s737b
        with dissolve

        la "I just gotta throw something on and we can go."

        scene s740 # lauren and mc in the bus transition (lauren clothed)
        with fade

        pause 1.0

        scene s741 # opening mc and Lauren sitting on the beach (lauren in bikini and mc in swimshorts without shirt, back view camera
        with fade

        u "This is really nice."

        scene s742
        with dissolve

        la "Yeah, thanks for coming. I know it was pretty last minute."

        scene s742a
        with dissolve

        u "Nothing better than spontaneous."

        scene s742f
        with dissolve

        la "You weren't busy?"

        scene s742g
        with dissolve

        u "Nah, maybe just some studying but I much rather be here."

        scene s742
        with dissolve

        la "Yeah, it's nice to get away once and a while even if it's not far. College is exhausting."

        scene s742a
        with dissolve

        u "I'm with you on that."

        scene s742
        with dissolve

        la "Anything new with you lately?"

        if CharacterService.is_fwb(emily):
            scene s742a
            with dissolve

            u "My ex has posted some very misleading pictures of us this morning and I didn't really know what to do about it."

            scene s742f
            with dissolve

            la "What do you mean misleading?"

            scene s742g
            with dissolve

            u "She was trying to make it look like we're back together... I don't know. We're definitely not."

            scene s742f
            with dissolve

            la "Have you talked to her?"

            scene s742g
            with dissolve

            u "Yeah but, I don't know..."

            u "Anyways, anything new with you?"

        else:
            scene s742a
            with dissolve

            u "I mean, not really. What about you?"

        scene s742
        with dissolve

        la "I'm pledging for the Deers tonight."

        scene s742a
        with dissolve

        u "Oh, so you're actually gonna try and join them?"

        scene s742
        with dissolve

        la "Yeah, I mean I know most of them really well and obviously my sister's the President so it's a pretty easy decision."

        scene s742a
        with dissolve

        u "I guess that's true, well good luck anyway."

        scene s742
        with dissolve

        la "Thanks."

        la "So how are things with Imre?"

        scene s742a
        with dissolve

        if CharacterService.is_mad(imre):
            menu:
                "Tell her it's fine":
                    $ reputation.add_point(RepComponent.BRO)
                    $ reputation.add_point(RepComponent.TROUBLEMAKER)

                    u "Good, great. You know how he is. It's just uhm... really good."

                    scene s742
                    with dissolve

                    la "I'm happy for you, seems like you guys really have a strong friendship and that's really important when you live together."

                    scene s742b # lauren slightly annoyed
                    with dissolve

                    la "I wish I would be as close with my roommate as you guys are."

                    scene s742c
                    with dissolve

                    u "Yeah..."

                    u "I mean he's teaching me how to fight and everything..."

                "Tell her he moved out":
                    $ reputation.add_point(RepComponent.BOYFRIEND)

                    u "Uhm... Imre and I had a fight and he moved out..."

                    u "Not like a physical one, just an argument. You know how he is, a bit of a hothead."

                    scene s742d # Lauren empathy
                    with dissolve

                    la "Oh that's too bad. I thought you guys were such good friends, what happened?"

                    scene s742e
                    with dissolve

                    u "I don't really wanna get into the details. But I hope that we can be friends again once he cools down."

                    scene s742d
                    with dissolve

                    la "Aww... I hope so too."

                    scene s742e
                    with dissolve

                    u "It kinda sucks cause he was teaching me how to fight."

        else:
            u "Really good, we're getting along really well and he's teaching me how to fight.."

        scene s742b
        with dissolve

        la "So you actually wanna be a fighter now?"

        scene s742c
        with dissolve

        u "Yeah, I really think I'd miss out on a lot if I didn't join a frat."

        scene s742b
        with dissolve

        la "Maybe... but fighting can be really dangerous."

        scene s742c
        with dissolve

        u "It's not street fighting... it's controlled, you know. I think they have a referee and everything."

        scene s742b
        with dissolve

        la "Do what you want, I guess."

        scene s742c
        with dissolve

        u "Yeah... I'll be careful."

        u "I won't get hurt, if that's what you're worried about."

        scene s742d
        with dissolve

        la "I mean... I just don't want you to end up in the hospital."

        menu:
            "You're cute":
                $ reputation.add_point(RepComponent.TROUBLEMAKER)

                scene s742e
                with dissolve

                u "You're cute when you worry about me."

                scene s742
                with dissolve

                la "*Giggles* Oh shut up."

                scene s742a
                with dissolve

                if reputation() == Reputations.LOYAL:
                    call screen reputation_popup

                    menu:
                        "Kiss her":
                            $ beachfirstkiss = True

                            play sound sound.kiss
                            scene s743e # you kiss Lauren
                            with dissolve

                            pause 1.0

                            scene s743 # showing both mc and Lauren from a close angle, lauren leaning closer to him, no one else around, mouth open flirting
                            with dissolve

                            la "Why'd you stop?"

                            scene s743a # lauren climbs on top of mc, mc opens mouth surprised smile
                            with dissolve

                            u "*Chuckles* Huh?"

                            scene s743b # lauren very close to mcs face, mc has his hands on her hips, mc mouth open flirty
                            with dissolve

                            la "I mean it's just us here..."

                            scene s743c # lauren push mc down so that he's laying with his back on the sand / towel and starts kissing him
                            with vpunch

                            pause 0.5

                            scene s743vid
                            with dissolve
                            
                            pause 1.4

                            scene s743apic
                            with dissolve

                            pause 0.75

                            la "*Quiet moan* Mhmmm..."

                            scene s745 # lauren mouth open, mc mouth closed
                            with dissolve

                            la "I'm really glad we're here together."

                            scene s745a # close up of Lauren lying on top mc, mc mouth open lauren mouth closed, both smiling
                            with dissolve

                            u "Yeah, me too."

                        "Don't risk it":
                            $ reputation.add_point(RepComponent.BOYFRIEND)

                            u "*Chuckles*"

                else:
                    u "*Chuckles*"

            "I won't":
                $ reputation.add_point(RepComponent.BOYFRIEND)

                u "I won't... don't worry."

        scene s746 #OpeningL the lighting should be early evening now, time has passed, Lauren and mc laying on the respective blankets
        with Fade(1,0,1)

        pause 1.0

        scene s747 # Lauren close up laying next to you very slight smile, looking at you, with early evening lighting
        with dissolve

        la "Sun is going to go down soon. We should probably get going."

        scene s747a
        with dissolve

        u "Yeah, we should get back."

        scene s740 # lauren and mc in the bus transition (lauren clothed)
        with fade

        pause 1.0

        scene s748 # back inside Lauren's dorm, both clothed., Lauren and Mc standing quite close looking at each other
        with fade

        pause 0.5

        if CharacterService.is_girlfriend(lauren) or beachfirstkiss:
            scene s749b
            with dissolve

            la "I wish you could stay, but I have to get ready for the Deer pledge night."

            scene s749c
            with dissolve

            u "Yeah, of course."

            scene s748
            with dissolve

            pause 0.5

            scene s748a #lauren and mc kiss
            with dissolve

            play sound sound.kiss
            pause 0.5

            scene s748
            with dissolve

            pause 0.5

            scene s749e # Lauren genuine smile
            with dissolve

            u "I'll see you later."

            scene s749d # Lauren genuine smile
            with dissolve

            la "Yeah, goodbye."

        else:
            scene s749b
            with dissolve

            la "Alright, I have to get ready for the Deer pledge night."

            scene s749c
            with dissolve

            u "Yeah, of course."

            scene s749b
            with dissolve

            u "I'll see you later."

            scene s749c
            with dissolve

            la "Yeah, goodbye."

        scene s734 # mc walks back to his dorm through dorm halls
        with fade
        stop music fadeout 3

        pause 0.5

########## SCENE 12: MC BACK AT DORM WEDNESDAY EVENING
    label rightafterbeach: #for compatibility only
    if CharacterService.is_fwb(emily):
        play sound "sounds/dooropen.mp3"
        scene s753 # mc opens his dorm door and looks on the ground, there's a letter
        with dissolve

        u "(Huh?)"

        show screen letter1

        " "
        hide screen letter1
        #em "Dear MC, I'm really sorry I posted that picture. I should have said something to you about it before. I guess I have to admit that I kind of miss you and I miss us being together. But most of all, I'd really like to make it up to you. Meet me at my dorm tonight at midnight. I'll have a surprise waiting for you xoxo."

        scene s754 # mc walking inside in swim trunks with letter in his hand
        with dissolve

        u "(Emily is just hot and cold... I'll have to see how I feel about it at midnight, but giving her yet another chance doesn't seem like a great idea.)"

    scene s755 # mc walking towards his bed and starts looking at his phone but you can't see the screen in swim trunks
    with dissolve

label afterbeach:
    u "(Oh shit, it's almost six already!)"

    if not meetgrayson:
        u "(Wolves pledging starts soon... is it stupid of me to wanna pledge now? I didn't think frat life was for me..."

        $ grant_achievement("wolfpack")
        u "(But after everything that happened I feel like I gotta at least try and get in, otherwise I'll miss out on too much.)"

    elif joinapes:
        u "(Pledging starts soon, I told Grayson I'd join the Apes, but is that really the right call? I mean the Wolves party was sick...)"

        u "(But in the Apes, I can finally be someone. I can be a winner. Grayson may have done some questionable shit in the past, but he also said a lot of stuff that resonated with me...)"

        if CharacterService.is_mad(imre):
            u "(On the other hand, Imre would hate me even more if I pledged the Apes...)"
        else:
            u "(On the other hand, Imre would hate me if I pledged the Apes...)"

        u "(When I came to San Vallejo I didn't even think frat life was for me, but after everything that happened I feel like I gotta at least try and get into one of these. Otherwise I'll miss out on too much.)"

        u "(Time to make a decision.)"

        menu:
            "Pledge to the Apes":
                $ grant_achievement("silverback")
                u "(Fuck it. I'm gonna be winner, no matter what it costs. Time to pledge to the Apes.)"

                jump pledgeapes

            "Pledge to the Wolves":
                $ grant_achievement("wolfpack")
                u "(Grayson might kill me when he finds out, but I can't join the Apes. I gotta pledge to the Wolves.)"

    else:
        u "(Pledging starts soon, I told Grayson I wouldn't join the Apes, but is that really the right call? I mean he did say some things that really resonated with me...)"

        u "(I'm pretty sure their pledging is at the same time as the Wolves, so I might be able to just go to the Apes' house and tell Grayson I changed my mind.)"

        if CharacterService.is_mad(imre):
            u "(But even so, the Wolves party was sick and Imre would hate me even more if I pledged the Apes...)"
        else:
            u "(But even so, the Wolves party was sick and Imre would hate me if I pledged the Apes...)"

        u "(When I came to San Vallejo I didn't even think frat life was for me, but after everything that happened I feel like I gotta at least try and get into one of these. Otherwise I'll miss out on too much.)"

        u "(Time to make a decision.)"

        menu:
            "Pledge to the Apes":
                $ grant_achievement("silverback")
                u "(Fuck it. I'm gonna be winner, no matter what it costs. I'ma go to the Apes' house and tell Grayson I changed my mind.)"

                jump pledgeapes

            "Pledge to the Wolves":
                $ grant_achievement("wolfpack")
                u "(Nah, Grayson's done more than enough questionable shit. The Wolves been nothing but good to me. I'ma pledge to the Wolves.)"


####### SCENE 13 PLEDGING THE WOLVES
label pledgewolves:
    $ reputation.add_point(RepComponent.BRO)
    $ joinwolves = True

    scene s756 # Camera - third person, MC walking through town during evening wearing jeans
    with fade
    u "(Wonder what it'll be like once I'm inside. Or if I even get in.)"

    scene s757 # Camera - first person. Shot showing the Wolves house. Imre waiting outside with a couple of others. They're all talking to each other.
    with fade
    pause 0.7

    if CharacterService.is_mad(imre):
        scene s757a # Imre notices MC, so he is now looking at the camera and waves
        with dissolve

        u "(Wait, is he waving at {i}me{/i}?)"

        play music "music/m11punk.mp3"
        scene s758 # Camera - third person. MC and Imre close up. Imre talking mouth open, MC confused look mouth closed. No others visible in the scene preferably
        with dissolve

        imre "Was wondering where you were."

        scene s758a # Same expressions but MC is now talking
        with dissolve

        u "Really?"

        scene s758b # Imre talking and MC has normal expression now
        with dissolve

        imre "Yeah man, I know we had our differences. But at the end of the day, we're still bros."

        scene s758c # MC happy and talking
        with dissolve

        u "Happy to hear that man. And not just any bros, we're gonna be frat bros!"

        scene s758b
        with dissolve

        imre "Hell yeah!"

        scene s758d # Imre and MC fist bump, but MC applies force
        with vpunch
        pause 0.3

        scene s758e # Imre pulls back his hand and grunts in slight pain, MC mouth open laughing
        with dissolve
        imre "Ouch!"
        u "That's for overreacting a little before *laughs*"

        scene s758f # Imre talking with his right hand behind his head, slightly regretful expression
        with dissolve
        imre "Sorry man. I shouldn't have acted like that."
        imre "Know that I've got your back from here on bro."

        scene s758g # Imre and MC happy and half hugging
        with dissolve
        pause 0.5

        scene s758c
        with dissolve
        u "It's cool man. What matters is we're here now."

        scene s758b
        with dissolve
        imre "And what we'll be in a few hours!!"

    else:
        scene s757a
        with dissolve
        u "(There's Imre. Looks like preparations are still being made.)"

        play music "music/m11punk.mp3"
        scene s758g
        with dissolve
        pause 0.5

        scene s758c
        with dissolve
        u "Sup bro!"

    scene s759 # Camera - first person. Imre and MC close up. Imre very excited, hands on either side of his head, mouth open. The two other people that were present before talking to each other in the background
    with dissolve
    imre "We're about to be Wolves!!!"

    scene s759a # Same as before, but Imre's mouth closed and maybe slightly different positions for people in the background
    with dissolve
    u "This is the shit you've been waiting for!"

    scene s759
    with dissolve
    imre "Our lives will officially change forever!"

    scene s759a
    with dissolve
    u "Haha calm down bro. We're just joining a frat."

    scene s759
    with dissolve
    imre "But we're gonna get mad pussy after this!"

    scene s759a
    with dissolve
    u "Ah shit, here we go again..."

    stop music fadeout 4
    ## Wolves Living Room ##
    scene s760 # Inside the Wolves' living room. A shot of 7 current wolves from the front. Chris and Aaron in the middle (Rest: Harry, Marcus, Sebastian, Finn, Peter)
    with Fade(1, 0.5, 1)
    pause

    scene s761 # Inside the living room, a shot of the 5 pledges (who are standing across the wolves) from the front. MC in the middle and Imre beside him
    with Dissolve(1.5)
    pause

    scene s762 # Chris steps forward, serious face, mouth open. Use a camera angle so as to include a couple of wolves in the background
    with dissolve
    ch "Can any of you tell me what it means to be a Wolf?"

    scene s761
    with dissolve
    pause 0.5

    scene s762
    with dissolve
    ch "To be a Wolf you need to be hardworking, persistent, determined."

    scene s762a # Chris slams a fist in his hand, serious face, talking
    with dissolve
    ch "You need to be deliberate with your actions, confident, dedicated, motivated, and-"

    scene s763 # Chris (serious face) gets in the face of one of the pledges who looks scared (neither MC nor Imre)
    with dissolve
    ch "And fearless!"

    play music "music/mindie1.mp3" fadein 3
    queue music [ "music/m6punk.mp3", "music/m15punk.mp3", "music/m16punk.mp3" ]

    scene s762a
    with dissolve
    ch "Now all of that sounds a bit intense, I know."
    ch "But on top of those qualities we need guys who we can trust, guys who are honest and always look out for each other."

    scene s762
    with dissolve
    ch "{b}Loyalty{/b} is of the essence here. I need guys that I can call at anytime and who will always have my back."
    ch "But most importantly..."

    scene s762a
    with dissolve
    ch "...I need winners. Being a winner doesn't mean you always have to win."
    ch "It means going in there believing that you will win. It's a mindset."

    scene s764 # Camera - first person. Chris looking into the camera, serious face, talking with his fist still in hand. Other wolves can be seen in the background
    with dissolve
    ch "Do you have what it takes to be a winner?"

    scene s764a # Chris hands relaxed, talking, looking slightly away from the camera
    with dissolve
    ch "Every year we only accept three pledges. Training capacities are limited."
    ch "Pledging to the Wolves happens today, and only today. It's one night, filled with challenges. Challenges that test you as a person."

    scene s764
    with dissolve
    ch "You might ask why we don't do hell week. Well this isn't a party frat."
    ch "Training needs to start as soon as possible. So we don't want to waste an entire week. It all happens tonight."
    ch "You will all face four challenges, each representing one of the core Wolves' values."

    scene s764b # Chris one fist closed and infront of his chest, serious face, talking
    with dissolve
    ch "Honor, Determination, Honesty, and Loyalty. These values are what make us, what defines us."
    ch "We need guys that can embody these 100 percent of the time."

    scene s764
    with dissolve
    ch "The challenges will be difficult, but if you wanna be a Wolf, you must prove yourself."
    ch "Now let's get started with the first challenge."

    scene s765 # Slide saying "Determination Challenge"
    with fade
    pause 1.5

    scene s766 # Camera - first person. All the 5 pledges and Chris in a new room (make sure it's big enough to fit around 8 people). Chris, Imre and Xavier visible in the shot. Chris talking looking at the camera. Imre and Xavier looking at Chris with their mouths closed
    with dissolve
    ch "Determination. For this challenge you'll have to prove that you will do whatever it takes to become a Wolf. Each of you will be in a separate room."
    ch "You will be given tasks to test how much you really want to be a Wolf, how far you're willing to go, and what you're willing to give up."
    ch "Other wolves will guide you with the tasks. Let's get started."

    scene s767 # Camera - third person. MC alone in a room, waiting. Make sure door is visible in the shot
    with fade
    u "(I wonder how far they're gonna take us for the tests.)"

    scene s767a # Door open, Marcus walks in. MC looks at him. Nobody talking.
    with dissolve
    pause 0.5

    scene s768 # First person: Marcus close up. Marcus talking
    with dissolve
    guyc "Sup [name]. It's Marcus."

    scene s768a # Marcus mouth closed
    with dissolve
    u "Hey."

    scene s768
    with dissolve
    guyc "So, listen. I'm supposed to run you through a bunch of questions and then hit you with the final one in order to see if you're determined enough."

    guyc "But I'm just gonna tell you straight up, the only way to show determination is if you're willing to eliminate one of the other guys."

    scene s768a
    with dissolve
    u "What do you mean?"

    scene s768
    with dissolve
    guyc "If I tell the guys you're willing to have me eliminate Imre, I can convince them to secure you a spot. You wouldn't have to compete with the others for it."

    scene s768a
    with dissolve
    u "...And if I don't?"

    scene s768
    with dissolve
    guyc "Then you'll still continue on with the challenges to try and secure your place."
    guyc "But remember, we only take in three pledges. And usually at least two people take these deals and get a secure spot. So you might get eliminated if you don't do it."

    scene s768a
    with dissolve
    u "Why Imre?"

    scene s768
    with dissolve
    guyc "You know why."

    scene s768a # Both of their mouths closed. MC thinking pose
    with dissolve
    menu:
        "Eliminate Imre":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            scene s768a
            with dissolve
            u "Fine. I'll do whatever it takes. You can eliminate Imre."

        "Decline":
            $ wolvesTasks.add("task1")
            $ reputation.add_point(RepComponent.BRO)

            scene s768a
            with dissolve
            u "I'm not betraying Imre like that. I'll take my chances."

    scene s768
    with dissolve
    guyc "Noted. Now go meet Chris again."

    scene s768a
    with dissolve
    u "Alright."

    if "task1" in wolvesTasks:
        scene s768
        with dissolve
        guyc "And hey, good luck with the other tasks."

    scene s766
    with fade
    ch "So, how was your first challenge, guys?"

    scene s766c # Chris looking slightly away from camera with mouth closed. Imre and Xavier looking at Chris with their mouths closed
    with dissolve
    xav "*Clears throat*"

    scene s766
    with dissolve
    ch "I've got a confession to make. I know I talked about honesty before, but this challenge was actually meant to test your Loyalty. I lied about the determination part."

    scene s766c # Chris looking slightly away from camera with mouth closed. Imre and Xavier looking at Chris with their mouths closed
    with dissolve

    if not "task1" in wolvesTasks:
        play sound sound.swoosh
        u "(What the fuck!?)"
        
    else:
        u "(Wow, good thing I didn't do it.)"

    scene s766b # Imre and Xavier surprised look. Imre looking at the MC. Chris still talking but looking slightly away from the camera (like s766c)
    with dissolve
    ch "We wanted to see how loyal you were to your fellow pledges and potentially future Wolves."
    ch "Loyalty trumps everything. Never go against a brother's back. For those of you that did, I hope you learned your lesson."

    ch "For now, let's move on to the actual determination challenge."

    scene s769 # Slide saying "Actual Determination Challenge"
    with fade
    pause 1.5

    scene s766
    with dissolve
    ch "Now this is your real determination challenge. You will need to prove that you can stick it out until the very end."
    ch "How bad do you want it? How long can you suffer to get what you want? How determined are you?"

    scene s766a
    with dissolve
    ch "The task is simple. All of you will get into a tub filled with freezing cold ice water. The last one to leave wins."

    scene s770 # Imre and Xavier close up, both looking towards Chris (who is not in the shot). Imre smiling and mouth open. Xavier worried and mouth open
    with dissolve
    imre "I got this."
    xav "Fuck. I hate cold water."

    scene s766
    with dissolve
    ch "Let's get started. Come with me."

    scene s771 # Camera - third person. All the pledges laying in the tubs in shorts/bathing suits, uncomfortable and shivering
    with fade
    pause
    ch "Remember, the last one in is the winner."

    scene s771a # All pledges slightly different pose, still uncomfortable
    with dissolve
    pause 0.5

    scene s771
    with dissolve
    pause 0.5

    scene s772 # Close up of Xavier leaving the tub, disappointed and mouth open
    with dissolve
    xav "I can't do this. I'm out."
    ch "There's our first victim."

    scene s773 # Close up of Jaxon leaving the tub, disappointed and mouth open
    with dissolve
    jax "I'll try my luck in the next one too."
    ch "Another goes down."

    scene s771b # MC, Imre and perry in the tubs. Other two empty.
    with dissolve
    ch "Let's see how long you guys can endure."

    pause

    scene s774 # Close up of Imre leaving the tub, disappointed, shivering and mouth open
    with dissolve
    imre "Shit. I thought this would be easy."

    scene s771c # Only MC and perry in the tubs. Other three empty.
    with dissolve
    ch "That leaves two of you. [name] and Perry. Let's see who chickens out first."

    scene s775 # Camera - third person. Close up of Imre standing alongside Chris. Imre cheering. Chris looking towards the tubs (not visible in shot) with hands folded
    with dissolve
    imre "[name]! You got this bro!"

    scene s771c
    with dissolve
    pause
    u "(Fuck. This is too cold. I'm losing sensation of my body.)"

    play sound sound.ring

    scene s776 # Close up of MC's phone on a desk ringing. Chloe is the caller.
    with vpunch
    pause 1

    scene s777 # Camera - third person. Aaron picks the phone up, laughing and talking. No one else visible in the shot
    with dissolve
    aa "Yo [name]... Why is Chloe calling you? *Laughs*"

    scene s778 # Camera - third person. MC close up in the tub, mouth open, uncomfortable position looking towards Aaron (not visible in the shot)
    with dissolve
    u "Wait, Chloe?"
    u "(This could be important. But if I leave, I'll lose the challenge.)"

    menu:
        "Get the call":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            scene s779 # Close up of MC leaving out of the tub, mouth open
            with dissolve
            u "Shit, I gotta get that."

            ch "And therefore Perry wins! Congrats Perry!"

        "Continue the challenge":
            $ wolvesTasks.add("task2")
            $ reputation.add_point(RepComponent.BRO)

            u "I'll get it later. I'm in this to win."
            ch "That's the spirit!"

            scene s780 # Close up of perry leaving the tub, mouth open
            with dissolve
            guyd "Damn. I tried my best."

            scene s775
            with dissolve
            imre "You did it man!"
            ch "Grats [name]. Good job!"

            jump aftercall

label chloe_call:
    scene sphone1 # mc on the phone mouth open
    with dissolve

    u "Hello? Chloe?"

    scene sphone1a # mc on the phone mouth closed tense
    with dissolve

    if CharacterService.is_mad(chloe):
        cl "Hey [name]... can we talk right now?"

        scene sphone1 # mc on the phone mouth open
        with dissolve

        u "Uhm... right now is bad. How about tomorrow?"

        scene sphone1a # mc on the phone mouth closed
        with dissolve

        cl "Uhm yeah... maybe. I don't know I'm really busy tomorrow."

        cl "You know what... never mind."

        scene sphone1 # mc on the phone mouth open
        with dissolve

        u "What about-"

        play sound "sounds/rejectcall.mp3"

        scene sphone1a # mc on the phone mouth closed
        with dissolve

        "*Chloe hangs up*"

        scene sphone2 # mc looks at his phone, you can't see the screen
        with dissolve

        u "(How weird...)"

    elif "chloe" in freeroam3:
        cl "Hey [name]... just wanted to say thanks for yesterday."

        scene sphone1 # mc on the phone mouth open
        with dissolve

        u "Of course. Is that why you're calling?"

        scene sphone1a # mc on the phone mouth closed
        with dissolve

        cl "Uhm yeah... sorry, I know pledging is going on right now... I just-"

        cl "Oh, shit Aubrey's calling me, I gotta get back. But thanks... for everything. I'll talk to you soon."

        scene sphone1 # mc on the phone mouth open
        with dissolve

        u "Sounds good."

        play sound "sounds/rejectcall.mp3"

        scene sphone1a # mc on the phone mouth closed
        with dissolve

        "*Chloe hangs up*"

        scene sphone2 # mc looks at his phone, you can't see the screen
        with dissolve

        u "(I wonder what she was about to say.)"

    else:
        cl "Hey [name]... can you talk right now?"

        scene sphone1 # mc on the phone mouth open
        with dissolve

        u "Uhm... right now is bad. Is it urgent?"

        scene sphone1a # mc on the phone mouth closed
        with dissolve

        cl "Uhhh no, I just-."

        cl "You know what... never mind."

        scene sphone1 # mc on the phone mouth open
        with dissolve

        u "I mean I can-"

        play sound "sounds/rejectcall.mp3"

        scene sphone1a # mc on the phone mouth closed
        with dissolve

        "*Chloe hangs up*"

        scene sphone2 # mc looks at his phone, you can't see the screen
        with dissolve

        u "(What was that about?)"

label aftercall:
    scene s781 # Slide saying "Honesty Challenge"
    with fade
    pause 1.5

    scene s766
    with dissolve
    ch "Honesty. Honesty is a key pillar to being a Wolf."
    ch "Without honesty, there can be no loyalty or honor. This challenge will test how honest you will really be when the time comes."

    scene s766a
    with dissolve
    ch "The Wolves will come out and say personal statements about each of you. You'll have to say whether the statements are true or false."

    scene s766
    with dissolve
    ch "And I will warn you, these statements are meant to embarrass you, they're meant to be shameful."
    ch "First up, Jaxon."

    scene s782 # Close up of Sebastian and Jaxon. Sebastian speaking. Jaxon neutral expression, mouth closed
    with dissolve
    se "True or False. Your first weekend here at the University, you got so wasted that you shit your own bed."

    scene s782a # Jaxon mouth open and smiling. Sebastian mouth closed
    with dissolve
    jax "False."

    scene s782
    with dissolve
    se "Are you sure?"

    scene s782a # Jaxon mouth open and smiling. Sebastian mouth closed
    with dissolve
    jax "Yeah, I'm not embarrassed. I shit my pants, not my bed."

    scene s782b # Jaxon and Sebastian laughing
    with dissolve
    se "*Laughs*"
    xav "*Laughs* That's so gross."

    scene s786 # Close up of Chris talking, neutral expression. No others visible in the shot.
    with dissolve
    ch "Very good Jaxon. You can step back. Next up, Perry."

    scene s783 # Close up of Aaron and perry. Aaron speaking. perry mouth closed, neutral expression
    with dissolve
    aa "Perry. True or False. In high school you slept with your cousin."

    scene s783a # Aaron mouth open. perry looking down, embarrassed, mouth open
    with dissolve
    guyd "Uhhh..."
    aa "Quick! True or False?"
    guyd "False."
    aa "Sadly we are confident that it's true."

    scene s784 # Close up of Imre and Sebastian, both surprised and mouth open
    with dissolve
    se "What the fuck?"
    imre "Really bro?"

    scene s783b # perry embarrassed and looking into the camera with mouth open. Aaron looking at perry with mouth closed and neutral expression
    with dissolve
    guyd "B-but I have a reason!"

    scene s783c # perry embarrassed and looking into the camera with mouth closed. Aaron looking at perry with mouth closed and neutral expression
    with dissolve
    jax "Man, what reason could you possibly have for that?"

    scene s783b
    with dissolve
    guyd "I didn't know she was my cousin until a lot later."

    scene s783c
    with dissolve
    u "Damn, you must have a big ass family."
    imre "*laughs*"

    scene s783b
    with dissolve
    guyd "Y-yeah."

    scene s786
    with dissolve
    ch "Okay! Enough fuss. Good job Perry. Let's continue. Next up, Xavier."

    scene s785 # Close up of Marcus and Xavier. Marcus speaking. Xavier mouth closed, neutral expression
    with dissolve
    guyc "Xavier. True or False. You slept with your high school Chem teacher to get an A."

    scene s785a # Marcus mouth closed, Xavier smirking with mouth open
    with dissolve
    xav "True."
    guyd "No way!"

    scene s784
    with dissolve
    se "Look at this one banging a teacher like a boss."
    imre "Damn."

    scene s785a # Marcus mouth closed, Xavier smirking with mouth open
    with dissolve
    xav "And she was in really good shape for a 65 year old..."

    scene s784
    with dissolve
    se "65??? What the fuck dude, hahah."
    imre "*Laughs*"

    scene s786
    with dissolve
    ch "Oh god Xavier... anyway, you can step back."

    ch "Imre, you're next."

    scene s787 # Close up of Finn and Imre. Finn is talking, Imre nervous mouth closed
    with dissolve
    finn "Imre. True or False. You've always been jealous of your older brother for being a better fighter than you and at one point even tried to sabotage one of his fights."

    scene s787a # Imre talking slightly embarrassed mouth open. Finn mouth closed.
    with dissolve
    imre "T-true. But those times are behind me. I was a kid then."
    imre "I know that's shitty of me, but I wouldn't do that to any of you ever again."

    scene s786
    with dissolve
    ch "Very well. Thank you for your honesty. You may step back."

    scene s786b # chris looking directly at you mouth open
    with dissolve

    ch "And last but not least, [name]."

    if (CharacterService.is_girlfriend(lauren) and CharacterService.is_fwb(aubrey)) or (CharacterService.is_girlfriend(lauren) and CharacterService.is_fwb(emily)):
        ch "Is it true that you recently cheated on the girl you're currently dating?"

        scene s786c # chris looking directly at you mouth closed
        with dissolve

        u "(How the fuck do they even know about this?)"

        menu:
            "True":
                $ wolvesTasks.add("task3")

                u "It's true, but-"

                scene s786b # chris looking directly at you mouth open
                with dissolve

                ch "No need to explain. We appreciate your honesty."

            "False":
                u "I didn't. False."

                scene s786b # chris looking directly at you mouth open
                with dissolve

                ch "Oh... sure."

    else:
        ch "Is it true that you've never been in a fight before coming to San Vallejo?"

        scene s786c # chris looking directly at you mouth closed
        with dissolve

        u "(Shit, if I say true, I'm gonna look a weakling... but if I say false and they know I'm lying I'll fail the challenge...)"

        menu:
            "True":
                $ wolvesTasks.add("task3")

                u "It's true, but-"

                scene s786b # chris looking directly at you mouth open
                with dissolve

                ch "No need to explain. We appreciate your honesty."

            "False":
                u "I didn't. False."

                scene s786b # chris looking directly at you mouth open
                with dissolve

                ch "Oh... sure."

    scene s786 # chris looking directly at you mouth open
    with dissolve
    ch "Let's move on to the next challenge."

    scene s788 # Slide saying "Honor challenge"
    with fade
    pause 1.5

    scene s766
    with dissolve
    ch "Last but not the least, honor. Reputation is what others know about you, but honor is what you know about yourself."
    ch "Each of you will be placed in a room again, only this time you won't be alone."

    scene s766a
    with dissolve
    ch "In each room you will be placed with someone close to the Wolves. It could be a girlfriend, a sibling, or even a close friend."
    ch "They will each have a hypothetical problem. It is your job to find the most honorable way to solve that problem."

    scene s766
    with dissolve
    ch "You have an hour and don't come out until the hours done."

    scene s766a
    with dissolve
    ch "Wolves, guide the pledges into their respective rooms."

    scene s789 # Camera - first person. Aaron and MC infront of a room with closed door. Aaron looking at the camera pointing towards the door and talking.
    with fade
    aa "That's yours. Good luck."

    scene s790 # Camera - first person. MC just entered the room. Nora in the middle of the room and is looking at the MC, neutral expression and mouth closed.
    with dissolve
    pause 0.5

    if CharacterService.is_mad(nora):
        # mad
        scene s791 # Camera - first person. MC and Nora close up but not very close, maintain abit more than two arms length distance between them. Nora slightly annoyed and talking
        with dissolve
        no "Oh, it's you."

        scene s791a # Nora slightly annoyed, mouth closed
        with dissolve
        u "Nice to see you too."

        scene s791
        with dissolve
        no "Okay well let's just get on with it then."

    elif "nora" in freeroam3:
        # happy
        scene s791b # Nora mouth open and smiling
        with dissolve
        no "Hey, good thing I got you. Maybe I won't be so bored after all."

        scene s791c # Nora mouth closed and smiling
        with dissolve
        u "Haha."

        scene s791b
        with dissolve
        no "Alright, shall we start then?"

        scene s791c
        with dissolve
        u "Don't see any reason to wait haha."

    else:
        # neutral
        scene s791d # Nora looking at camera with no particular expression. Maybe slight smile but that's it. Mouth open
        with dissolve
        no "Hey [name]."

        scene s791e # Nora looking at camera with no particular expression. Maybe slight smile but that's it. Mouth closed
        with dissolve
        u "Nora."

        scene s791b
        with dissolve
        no "Okay well let's just get this over with. Already dying of boredom in here."

        scene s791c
        with dissolve
        u "Haha okay."

    scene s791d
    with dissolve
    no "So, my best friend knows she is going to fail her English final."
    no "She asks me if I can try and seduce her teacher to change her grade. Do I do it or not?"

    scene s791e
    with dissolve
    menu:
        "Do it":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            $ reputation.add_point(RepComponent.BRO)

            u "Why not, you should do it."

            scene s791f # Nora pissed and mouth open
            with dissolve
            no "What? You serious?"

            scene s791g # Nora pissed and mouth closed
            with dissolve
            u "Yeah, she's your best friend."

            scene s791h # Nora facing down and writing something on a slip. What she's writing should not be visible on the camera and she has a neutral expression
            with dissolve
            no "Okaaay, well I'll mark that down."

        "Of course not":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            u "Isn't that obvious? You don't do it."

            scene s791d
            with dissolve
            no "And why not?"

            scene s791e
            with dissolve
            u "Your friend fucked up. She should've studied. That's not on you. And you don't put yourself at risk for her."
            no "Mhm."

            scene s791h
            with dissolve
            no "I'll note that down."

    scene s791d
    with dissolve
    no "Now we wait until the hour's done."

    scene s791e
    with dissolve
    u "Wait, that's it?"

    scene s791d
    with dissolve
    no "Yeah."

    scene s791e
    with dissolve
    u "But the real question is, would you do it?"

    if CharacterService.is_mad(nora):
        scene s791
        with dissolve

    else:
        scene s791b
        with dissolve

    no "Seduce my friend's English teacher? Hell no."
    u "*Laugh*"

    scene s791d
    with dissolve
    no "Even for my best friend, that's a dumb idea."

    scene s791e
    with dissolve
    u "Yeah, yeah."

    # stop musicfadeout 3 #check - music change here to set mood?

    scene s792 # Camera - first person. Nora closer to MC (than s791, slightly more an arm's distance) with a cheeky smile, eyebrows slightly raised and eyes slightly squinted, mouth open
    with dissolve
    no "What would you do? Seduce your friend's teacher?"

    scene s792a # Nora with a cheeky smile, eyebrows slightly raised and eyes slightly squinted, mouth closed
    with dissolve
    u "If she was hot, then maybe!"

    scene s792b # Nora playful smile, mouth open, with a hand on on MC's chest
    with hpunch
    no "Wowwww! You totally would."

    scene s792c # Nora playful smile, mouth closed, with a hand on on MC's chest
    with dissolve
    u "Why not? If she was hot, I'd do it even if my friend didn't ask me."

    scene s792b
    with dissolve
    no "Haha. Unbelievable. And what would you do to seduce this teacher?"

    scene s792c
    with dissolve
    u "Tell her she's beautiful, and that I'd like to do all kinds of things to her in the bedroom."

    scene s793 # Camera - third person (Nora's face should be well visible). Nora very close to the MC and talking with a seductive expression. MC mouth closed
    with dissolve
    no "Then in the bedroom?"

    scene s793a # Nora mouth closed and MC talking now
    with dissolve
    u "I guess she'd have to wait and find out."

    scene s793b # Nora leans in to kiss the MC. Lips slightly touching and one hand on MC's shoulder
    with dissolve
    pause

    menu:
        "Kiss her back":
            if CharacterService.is_girlfriend(lauren):
                $ reputation.add_point(RepComponent.TROUBLEMAKER, 2)
            else:
                $ reputation.add_point(RepComponent.TROUBLEMAKER)
                $ reputation.add_point(RepComponent.BOYFRIEND)

            ### NEW ACHIEVEMENT UNLOCK? ###
            scene s793c # Nora still leaning into the MC. MC tilts forward his head and goes for a kiss
            with dissolve
            pause 0.8

            scene s793d # Nora gets back to normal posture breaking the kiss, and looking into the MC's eyes. Her hand still on MC's shoulder
            with dissolve
            pause 0.5

            scene s793e # Now MC leans in to kiss her, lips touching and MC's hand on Nora's waist
            with dissolve
            pause 1

            scene s792
            with dissolve
            no "Gotcha!"

            scene s792a
            with dissolve
            u "Uhhhh.."

            scene s792
            with dissolve
            no "Sorry, but you didn't pass."

            scene s792a
            with dissolve
            u "What?"

            scene s791b
            with dissolve
            no "That was the real test and you didn't pass."

            scene s792a
            with dissolve
            u "You've gotta be kidding me."

            scene s792
            with dissolve
            no "Well, enjoy the rest of your night."

        "Pull away":
            $ wolvesTasks.add("task4")
            $ reputation.add_point(RepComponent.BRO)
            if CharacterService.is_girlfriend(lauren):
                $ reputation.add_point(RepComponent.BOYFRIEND)

            scene s793f # MC tilts back when Nora is tilting towards him. MC talking, Nora mouth closed
            with dissolve
            u "Nah, we can't do this."

            scene s793f2 # Nora turns to the side, seemingly angry
            with dissolve
            u "Nora, I'm sorr-"

            if CharacterService.is_mad(nora):
                scene s791d
                with dissolve

                no "You passed!"

                scene s791e
                with dissolve
                
                u "What?"

                scene s791d
                with dissolve
                
                no "That was the real test, and you passed it!"

                scene s791e
                with dissolve
                
                u "Wait, really? That's great!"

            else:
                scene s791b
                with dissolve

                no "You passed!"

                scene s791c
                with dissolve

                u "What?"
                
                scene s791b
                with dissolve
                
                no "That was the real test, and you passed it!"

                scene s791c
                with dissolve

                u "Wait, really? That's great!"

    scene s794 # Camera - first person. Nora moves to the door and knocks while talking
    with dissolve

    if "task4" in wolvesTasks:
        no "Aaron, the test is done and he passed."

    else:
        no "Aaron, the test is done and he didn't pass."

    scene s794a # Aaron enters the room and talks while looking at Nora. Nora is is looking at Aaron
    with dissolve
    aa "Thanks Nora, you can go now."

    if not CharacterService.is_mad(nora):
        scene s794b # Nora looks at the MC while slightly smiling. Aaron mouth closed and looking at MC
        with dissolve
        no "Good luck."
        u "Thanks."

    scene s794c # Nora leaving through the door. Aaron looking at MC while talking
    with dissolve
    aa "Let's go back."

    scene s762
    with fade
    ch "This marks the end of pledging."

    ch "We've ranked all five of you based on not only your results, but also how you got them. Doing well in the challenges is one thing, but that's not everything we considered."

    ch "Let's reveal the rankings."

    scene s795 # close up of Aaron reading from some note
    with dissolve

    if len(wolvesTasks) == 4:
        aa "The first place goes to..."

        scene s795a # Aaron looks up at you
        with dissolve

        aa "[name]."

        scene s795
        with dissolve

        aa "The second place goes to..."

        scene s795b # Aaron looks up at Imre
        with dissolve

        aa "Imre."

        scene s795
        with dissolve

        aa "And the third place goes to..."

        scene s795c # Aaron looks up at Perry
        with dissolve

        aa "Perry."

    elif len(wolvesTasks) == 3:
        aa "The first place goes to..."

        scene s795b
        with dissolve

        aa "Imre."

        scene s795
        with dissolve

        aa "The second place goes to..."

        scene s795a
        with dissolve

        aa "[name]."

        scene s795
        with dissolve

        aa "And the third place goes to..."

        scene s795c
        with dissolve

        aa "Perry."

    else:
        aa "The first place goes to..."

        scene s795b
        with dissolve

        aa "Imre."

        scene s795
        with dissolve

        aa "The second place goes to..."

        scene s795c
        with dissolve

        aa "Perry."

        scene s795
        
        with dissolve

        aa "And the third place goes to..."

        scene s795a
        with dissolve

        aa "[name]."

    scene s795b
    with dissolve

    aa "Congratulations guys. You're officially Wolves now. You're moving in tomorrow."

    scene s796 # close up Imre super excited
    with dissolve

    imre "Holy shit!"

    scene s797 # showing your face contemplating and smiling
    with dissolve

    u "(A Wolf... that's who I am now... Crazy to think.)"

    u "(The most exciting phase of my life... just about to begin.)"

    scene s798 # closeup chris talking to you smiling
    with dissolve

    ch "How does it feel?"

    scene s798a
    with dissolve

    u "Unbelievable. I haven't really processed it yet."

    u "I mean I don't even know much about frat life, or fighting, or-"

    scene s798
    with dissolve

    ch "Haha yeah. Don't worry. You're gonna love it."

    scene s798a
    with dissolve

    u "Yeah, I think so too."

    scene s798b # Chris turns to everyone smiling
    with dissolve

    ch "Alright guys, most of us have classes tomorrow and it's already far past midnight, so let's end it here."

    ch "Imre, Perry and [name], I expect you to be here with all of your things tomorrow evening. You're moving in!"

    scene s798c # Chris mouth closed, Wolves applauding
    with dissolve

    "*Applause and cheering*"

    stop music fadeout 3

    jump after_pledges

######## SCENE 14 APES
label pledgeapes:
    $ reputation.add_point(Reputations.TROUBLEMAKER, 3) # I think more TM points for joining the Apes makes sense
    $ joinwolves = False

    scene s756 # Not a new render
    with fade
    
    if joinapes:
        u "(Man, can't believe I'm doing this. Wonder what it's gonna be like if I get in.)"
    else:
        u "(Fuck, this seems like a bad idea. How's he gonna act when he sees me show up on the doorstep after I said no?)"
        u "(Maybe I'm overthinking it and he'll just be cool. Wonder what it's gonna be like if I get in.)"

    scene s825 # Camera - FPP. Shot showing the Apes house. Ryan, Caleb, Cooper, Kai waiting outside the building talking to each other
    with fade
    pause 0.7

    scene s825a # Ryan notices MC, so now is looking at the camera and waving
    with dissolve
    pause 0.5

    play music "music/m11punk.mp3"

    scene s826 # Camera - FPP. MC and Ryan close up. Ryan talking. One or two other guys can be seen in the shot, doesn't really matter as long as it looks continuous with s825a
    with dissolve
    ry "Hey, what's up? You've finally come around to join the Apes or what?"

    scene s826a # Ryan mouth closed
    with dissolve
    if joinapes:
        u "Yup. And I'm guessing that's why you're here too."
    else:
        u "Yeah... I wasn't planning on joining before, but I wanna give it a try now."
        u "Guessin' that's why you're here too."

    scene s826
    with dissolve
    ry "Duh! Of course. Let the best man win."

    scene s827 # Camera - TPP. MC and Ryan happy and shaking hands.
    with dissolve
    pause 0.5

    scene s826a
    with dissolve
    u "Who knows, maybe we both get in."

    scene s826
    with dissolve
    ry "You know it's hard to get into the Apes, right?"

    scene s826a
    with dissolve
    u "Haha, I know. Don't get so crazy about it."

    scene s826
    with dissolve
    ry "I'm not. Just saying that it's a big deal."

    scene s826b # Ryan mouth open, one eyebrow slightly raised and doing the sex gesture (ok symbol in one hand and pointing with the other)
    with dissolve
    ry "Just think of all the girls we'll get."

    scene s826a
    with dissolve
    u "Haha, yeah. That's a perk."

    scene s826
    with dissolve
    ry "I can't wait. I'm giving my 110 percent for sure."

    scene s826a
    with dissolve
    u "Me too. Do we have to wait out here?"

    scene s826
    with dissolve
    ry "Grayson said he'll come for us-"

    if joinapes:
        scene s828 # Camera - FPP. Shot of Grayson just coming out of the building (door should be open) and looking into the camera. Grayson mouth open. Ryan should be visible in the shot looking at Grayson with mouth closed
        with dissolve
        gr "Hey, hey."

        stop music fadeout 3

        scene s828b # Grayson mouth open but looking towards the other pledges with a slightly arrogant smile
        with dissolve
        gr "Get in boys, we're starting."

    else:
        scene s828
        with dissolve
        gr "Hey-{w=0.5}{nw}"

        scene s828a # Grayson surprised with mouth closed
        with dissolve
        pause 0.5

        scene s828b
        with dissolve
        gr "Everybody except [name] get in, we're getting started."

        scene s828c # Ryan turns around to look at the MC with a worried expression, mouth closed. Grayson mouth closed with a slightly arrogant smile looking into the camera.
        with dissolve
        pause 0.7

        scene s829 # Camera - FPP. Grayson stepped down the stairs and now infront of the MC. Grayson mouth closed with the same arrogant smile as s828c. Ryan and other pledges can be seen going inside the door
        with dissolve
        pause 0.5

        scene s829a # Pledges not visible now, everything else same as s829
        with dissolve
        u "I know how this looks, but I changed my mind. I know I was a dick before, but I really think I deserve to be here."
        u "You won't regret it, I-"

        gr "It's cool. Relax. Looks like you finally decided you want to be a winner."
        u "Exactly."

        gr "You made the right call. Come on inside."

        stop music fadeout 3

        scene s829a
        with dissolve
        u "Thanks."

    ## Apes Basement ##

    scene s830: # Inside the Apes basement. A shot of the 6 current Apes from the front. Grayson and Cameron in the middle.
        subpixel True
        truecenter
        zoom 1.0
        ease 15 zoom 1.15
    with Fade(1, 0.5, 1)
    pause

    scene s831: # Inside the Apes basement. A shot of the 5 pledges (who are standing across the Apes) from the front. MC in the middle and Ryan beside him
        subpixel True
        truecenter
        zoom 1.0
        ease 15 zoom 1.15
    with Dissolve(1.5)
    pause

    scene s832 # Camera - FPP. Grayson steps forward and starts speaking with an arrogant smile/smirk while looking away from the camera. Include a couple of Apes in the background
    with dissolve
    gr "Any of you assholes know what it means to be an Ape?"

    scene s831
    with dissolve
    "..."

    scene s832
    with dissolve
    gr "No? Well, then I don't know if any of you guys are even worthy enough to be here."

    scene s831a # Pledges confused and looking at each other
    with dissolve
    pause

    play music "music/m5punk.mp3" fadein 2
    queue music [ "music/m9punk.mp3" ]

    scene s832a # Grayson energetic expression with mouth open and looking into the camera
    with dissolve
    gr "I'm just fuckin' with you. To be an Ape means you gotta be fearless..."

    scene s833 # Sam close up cheering, energetic, mouth open
    with dissolve
    sam "Yeeahh!"

    scene s832
    with dissolve
    gr "You gotta be fierce!"
    wes "Yup!"

    scene s832a
    with dissolve
    gr "You gotta be ruthless!"

    scene s834 # Cameron close up cheering, energetic, mouth open
    with dissolve
    ca "Woooo!"

    scene s832
    with dissolve
    gr "But above all you gotta be willing to fight for what you want, hell even kill for it."
    "*Claps and cheers*"

    scene s832a
    with dissolve
    gr "If I say roll over you roll over. If I say fight you fight. You do things without question here."
    gr "Once you're an Ape, you're always an Ape. So you better prove yourself the whole way through."

    scene s832
    with dissolve
    gr "And lastly, being an Ape means being a winner. I don't need no pussy motherfuckers. You better be ready to fight and claw your way to the top."

    scene s834
    with dissolve
    ca "Yeeahhh!"

    scene s832
    with dissolve
    gr "It won't be easy to get in. You need to prove that you're willing to take things far when needed."

    scene s832a
    with dissolve
    gr "Here's how it's gonna go, each pledge will be set up with an Ape coach. Each coach will be with you for three days."

    scene s832
    with dissolve
    gr "They will record as much video evidence as they can to prove that their pledge is worthy enough to be an Ape. Only three of you will make it."

    scene s835 # Grayson closeup mouth open. No one else should be visible in the shot
    with dissolve
    gr "First off, Caleb. Go ahead and take your pick."

    scene s836 # Caleb close up mouth open
    with dissolve
    cal "Uhm... I'll choose Mason."
    ma "Cheers."

    scene s835
    with dissolve
    gr "Cooper."
    coop "I'll go with Sam."

    scene s837 # Sam and Cooper high five
    with hpunch
    pause 0.7

    scene s835
    with dissolve
    gr "Next, Kai."

    scene s838 # Kai close up mouth open, unsure
    with dissolve
    kai "Uh.. uhm.. Parker."
    par "I gotchu."

    scene s835
    with dissolve
    gr "Ryan."
    ry "Wesley!"

    scene s839 # Ryan and Wesley fist bump
    with hpunch
    pause 0.7

    scene s835
    with dissolve
    gr "And I guess that leaves Cameron and [name]. You guys will be paired together."
    u "(Oh come on!)"

    scene s840 # Cameron close up unimpressed/unhappy mouth open
    # with dissolve
    ca "Dammit."

    scene s835
    with dissolve
    gr "The deadline is 6PM on Saturday. All the videos will be presented then and I'll select the best three."
    gr "There's beers upstairs in the freezers if you want. Now start moving and get shit done!"

    stop music fadeout 3
    scene s841 # Camera - TPP. Shot showing Sam, Ryan, Weasly, Sam cheering. Use different poses for everyone. Cameron is also in the shot but looks disappointed. Make him stand out a little
    with dissolve
    "*Claps and cheers*"

    scene s843 # Camera - FPP. Cameron disappointed and mouth open
    with dissolve
    ca "Now, listen to me here, I've never coached before, but I really don't think you would do anything that an Ape would do."
    play music "music/m3punk.mp3" fadein 2
    ca "But as your coach, I'm not willing to lose. So you're gonna suck it up and do everything I say."

    scene s844 # Camera - TPP (preferably same as). Cameron threatening expression and mouth open. He is leaning towards the MC and is pointing his index finger on MC's chest
    with dissolve
    ca "Otherwise, we're gonna have a problem. You hear me?"

    menu:
        "Stand up to him":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            scene s843a # Cameron threatening and mouth closed
            with dissolve
            u "Fuck that. I'm not your bitch. I'm not gonna fucking take orders from you."

            scene s843b # Cameron pissed and mouth open, with his chest protruding and leaning forward as if about to punch the MC
            with dissolve
            ca "Excuse me?"

            scene s843c # Same as s843b but mouth closed
            with dissolve
            u "You heard me bro, I ain't doin shit you say."

            scene s843b
            with dissolve
            ca "Fight me then, bitch!"

            scene s843c
            with dissolve
            u "What?"

            scene s843d # Same as s843b but now slamming a fist in his hand, mouth open
            with dissolve
            ca "Right here, right now. In the hexagon."

            scene s843e # Same as s843d but mouth closed
            with dissolve
            u "What the fuck?"

            scene s843d
            with dissolve
            ca "What? You a bitch? Too afraid?"

            scene s843e
            with dissolve
            u "I ain't afraid of nothin'"

            scene s843f # Same as s843d but Cameron with a smirk, condescending laugh and mouth open
            with dissolve
            ca "Then get in the ring with me."

        "Hold yourself back":
            $ reputation.add_point(RepComponent.BRO)
            pause 0.5

            scene s844a # MC holding in anger and clenching his fists. Cameron back to normal position and mouth open, with a smirk
            with dissolve
            ca "Hmph. Thought so."
            stop music fadeout 3

            ca "Come with me."

            jump ep7_cam_picture

label ep7_fight_cam:
    scene s845 # Camera - TPP. Cameron inside the MMA ring, MC outside the ring. Cameron gesturing the MC to climb up with one hand and holding a fist with the other.
    with dissolve
    ca "Get in and show me what you got!"

    scene s845a # MC climbing up the ring
    with dissolve
    pause 0.5

    scene s846 # Camera - FPP. Cameron with his fists up, mouth open and angry expression
    with dissolve
    ca "Come on. Put 'em up. We're here to fight."

    scene s846a # Same as before but now MC's fists are up and visible in the shot. Cameron mouth closed
    with dissolve

    menu:
        "Punch him":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            scene s846b # MC throws a punch but Cameron blocks it
            with hpunch
            pause 0.3

            scene s847 # Camera - TPP. Cameron throws MC to the ground and arm locks him. MC winces in pain. (Both of their mouths open)
            with vpunch
            u "OOUUCHH!!"
            ca "Give up for your own sake." with hpunch
            ca "I said give it up!" with vpunch
            u "Okokok *taps out*" with hpunch

            scene s848 # Camera - FPP. Cameron standing in the ring near the MC with a smug face and mouth open while looking into the camera. MC on the ground and looking up at Cameron
            with dissolve
            ca "Come with me. I'm gonna show you something."

            stop music fadeout 3

            scene s848a # Cameron turns back and starts walking away from MC (who is still on the ground)
            with dissolve
            pause 0.7

        "Retreat":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            $ reputation.add_point(RepComponent.BRO)

            scene s846c # Same as s846 but Cameron mouth closed
            with dissolve
            u "Nah, this ain't worth it. I'm not gonna hit you."

            scene s846
            with dissolve
            ca "I knew it. You're a pussy."

            scene s846d # Cameron turns away from the MC and leaving the ring
            with dissolve
            u "Whatever man."
            stop music fadeout 3

            ca "Come with me. I'm gonna show you something."

label ep7_cam_picture:
    play sound "sounds/dooropen.mp3"
    scene s849 # Camera - TPP. MC and Cameron entering a room (Need not show what's inside the room in the shot, they're just entering through the door.)
    with fade
    pause 0.5

    scene s850 # Camera - FPP. MC and Cameron infront of an old black and white picture of the Apes' founder Remington. Cameron neutral expression and talking while looking at the picture
    with dissolve
    ca "Any idea what you're lookin' at?"

    scene s850a # Same as s850 but Cameron mouth closed
    with dissolve
    u "Uh.. No."

    play music "music/m11punk.mp3"
    queue music [ "music/m15punk.mp3", "music/m9punk.mp3" ]

    scene s850
    with dissolve
    ca "This is Remington, founder of the Apes. You wanna know where he started?"

    scene s850a
    with dissolve
    u "Where?"

    scene s850b # Same as s850 but Cameron looking into the camera with mouth open
    with dissolve
    ca "He was in the Wolves and they threw him out. He didn't want to accept it as a defeat and started the Apes."

    scene s850c # Same as s850b but Cameron mouth closed
    with dissolve
    u "Why'd they throw him out?"

    scene s850
    with dissolve
    ca "Because he was willing to do anything it took to win."
    ca "Anything."

    scene s850c
    with dissolve
    u "..."

    scene s850b
    with dissolve
    ca "That's why the Apes only take winners. Nothing less. Got me?"

    scene s850c
    with dissolve
    u "Sure, I guess."

    scene s850b
    with dissolve
    ca "Alright, you can go."

    ## Apes Drinking Scene ##
    scene s851 # Camera - FPP. looking at a few apes on the couch, from seated position
    with Fade(0.75, 0.25, 0.75)
    pause 0.5

    scene s852 # Close up of Wesley talking while laughing a bit. Include the guy sitting beside him in the shot and he's drinking
    with dissolve
    wes "Yeah and one time Sam got so faded, he tried to get in bed with Parker."
    "*Laughs*"

    scene s853 # Close up of Sam and Parker. Parker laughing while Sam talking slightly annoyed expression
    with dissolve
    sam "Hey! That's not fair. I was out of my mind."

    scene s853a # Sam mouth closed with same expression. Parker laughing and talking while looking at Sam
    with dissolve
    par "You called me Katie!"

    scene s853
    with dissolve
    sam "I was fucking her at the time. What else would I say?"


    scene s854 # Close up of Kai talking while laughing
    with dissolve
    kai "How long did it take you to realize?"

    scene s853a
    with dissolve
    par "I don't know! I just woke to Sam kissing my face!"
    ry "Oh man!"

    scene s853b # Same as s853 but Sam talking while laughing. Parker drinking from bottle but has a slightly shocked expression on his face
    with dissolve
    sam "Hey! At least I didn't accidentally fuck one of my girlfriend's sisters."
    coop "What?!"

    scene s853c # Same as s853b but Sam isn't talking. Parker has the same expression but is now talking
    with dissolve
    par "She had a twin!! Identical! If you were drunk you could've made the mistake too. I blame her sister. She should've said no."
    sam "Hahaha."

    scene s855 # Camera - FPP. MC looking at Grayson who is hand gesturing MC to come to the side
    with dissolve
    pause 0.7

    scene s856 # Camera - FPP. MC close up with Grayson a bit away from the previous scene. Grayson slight smile mouth closed.
    with dissolve
    u "What's up?"

    scene s856a
    with dissolve
    gr "So, you're gonna have to do a bit to try and earn some points from Cameron, but once you're in... trust me, I'll make sure you achieve your full potential."

    scene s856
    with dissolve
    u "What do you mean?"

    scene s856a
    with dissolve
    gr "I mean you're really gonna have to push it to get in."

    scene s856b # Grayson handing out a slip to MC, mouth open
    with dissolve
    gr "Here. This is Cameron's little sister's number. She goes to uni here."
    gr "Cameron is very protective of her. So if he ever goes too far, this is how you can get him back."

    menu:
        "Take the slip":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            scene s856
            with dissolve
            u "Thanks man."

            scene s856a
            with dissolve
            gr "No problem. Just looking out."

        "Decline":
            $ reputation.add_point(RepComponent.BRO)

            scene s856
            with dissolve
            u "Nah man, it's cool."

            scene s856a
            with dissolve
            gr "You sure? It could be of help later."

            scene s856
            with dissolve
            u "Yeah, it's fine. I don't need it."

    scene s857 # Camera - TPP. Scene setting same as s851 except that Cameron is also present now. MC is standing near Cameron who is just looking at the other guys talking with a bored expression. Need not show all the others in the shot.
    with fade
    pause 0.5

    scene s857a # MC sits beside Cameron. Cameron eyes the MC with the same bored expression
    with dissolve
    pause 0.7

    scene s854
    with dissolve
    kai "Man, you guys are crazy."

    scene s853b
    with dissolve
    sam "Mostly a crazy mess."

    scene s853c
    with dissolve
    par "That's all you!"

    scene s858 # Camera - TPP. Close up of Cameron leaning over towards MC and talking. MC mouth closed
    with dissolve
    ca "Hey, let's go outside. We're gonna do the first video."

    scene s858a # MC talking now
    with dissolve
    u "Oh.. Okay."

    scene s859 # Camera - TPP (behind MC). MC and Cameron walking nearby a wall outside the Apes building
    with dissolve
    pause 0.5

    scene s860 # Camera - FPP. Cameron leans on the wall and turns towards the MC. Cameron mouth closed with a cunning look
    with dissolve
    u "What are we doing?"

    scene s860a # Cameron mouth open with cunning look
    with dissolve
    ca "You're gonna call Chloe and proudly tell her that you're an Ape."

    scene s860
    with dissolve
    u "Chloe? Why her?"

    scene s860a
    with dissolve
    ca "You know exactly why."

    scene s860
    with dissolve

    menu:
        "Call her":
            $ apesVids += 1
            $ reputation.add_point(RepComponent.BRO)
            $ reputation.add_point(RepComponent.BOYFRIEND)

            u "Okay."

        "Refuse to do it":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            u "Nah, I'm not calling Chloe."

            scene s860b # Cameron slightly disappointed look, mouth open
            with dissolve
            ca "You sure?"
            u "Yep."

            scene s860c # Cameron condescending laugh mouth open
            with dissolve
            ca "Damn! You really are a pussy ass bitch!"
            ca "Haha! Pussy ass dumb little bitch!"

            scene s860d # Cameron condescending laugh mouth closed
            with dissolve
            u "Whatever man."

            u "I think I'ma head home for tonight."

            stop music fadeout 3

            scene s860b # Cameron slightly disappointed look, mouth open
            with dissolve
            ca "We're gonna do some real videos tomorrow. If you like it or not."

            jump after_pledges

    label chloe_call_cameron: #for compatibility only
    scene snew860a # close up mc on the phone mouth closed a bit nervous
    with dissolve

    play sound sound.calling
    pause 2
    stop sound

    if CharacterService.is_mad(chloe):
        play sound "sounds/answercall.mp3"
        cl "What do you want, [name]?"

        scene snew860a # mouth open
        with dissolve

        u "Uhm... I'm an Ape now, so-"

        scene snew860
        with dissolve

        cl "Good for you."

        play sound "sounds/rejectcall.mp3"

        "*Chloe hangs up*"

    else:
        play sound "sounds/answercall.mp3"
        cl "Hello? [name]?"

        scene snew860a # mouth open
        with dissolve

        u "Hey Chloe, just wanted to let you know that I'm an Ape now-"

        scene snew860
        with dissolve

        cl "Really? An Ape? After everything that Grayson did to me? And to you?"

        scene snew860a
        with dissolve

        u "I know a lot of things happened but-"

        scene snew860
        with dissolve

        cl "I mean yeah... it's your decision."

        cl "Look I'm sorry, but I'm really busy right now... we'll talk some other time okay?"

        scene snew860a
        with dissolve

        u "Yeah, uhm... okay."

        scene snew860
        with dissolve

        play sound "sounds/rejectcall.mp3"

        "*Chloe hangs up*"

    scene snew861 #close up Cameron  holding his phone up like he was filming you, cunning smile
    with dissolve
    ca "Well done, man. Show her who's boss."

    scene snew861a # cameron put's phone down, mouth closed
    with dissolve

    u "Right..."

    u "I think I'ma head home for tonight."

    stop music fadeout 3

    scene snew861b # Sam as s861a but cameron's mouth open
    with dissolve
    ca "We'll do more videos tomorrow, tiger."

########## SCENE 15 WALKING HOME AFTER PLEDGING
label after_pledges:

    scene s861 # Camera - TPP. MC walking home at night through the town after Apes pledging
    with fade

    if apesVids == 1 or joinwolves:
        pause 0.5

    else:
        u "(Fucking asshole.)"

    scene s861a # MC walking home at night through the town, different shot
    with dissolve

    if CharacterService.is_fwb(emily): # Please confirm this is the right condition for her to send an apology letter to the MC
        u "(Oh my god, I completely forgot about Emily. Wonder if she's still up.)"

        menu:
            "Text her":
                $ emilyText = True
                $ reputation.add_point(RepComponent.BOYFRIEND)

                $ MessengerService.add_reply(emily, _("Hey, sorry I lost track of time. You up?"))

                while MessengerService.has_replies(emily):
                    call screen phone
                    if MessengerService.has_replies(emily):
                        u "(I should text Emily that I lost track of time.)"

                u "(I guess she's asleep.)"

            "Don't text her":
                $ forgiveemily = False
                $ reputation.add_point(RepComponent.TROUBLEMAKER)

                u "(Nah, I've had enough of her.)"

    else:
        pause 0.5

    scene s483 # Old render - looking at your bed in FPP
    with fade

    u "(Today was so packed... Can't wait to just fall asleep.)"

########## SCENE 16 WAKING UP IN YOUR DORM ON THURSDAY BLACK EYE GONE!!! NEW MC MODEL
    label ep7_before_history: #for compatibility only
    scene s865 # Camera - TPP. MC waking up yawning in bed. No black eye
    with Fade(1,0,1)

    if joinwolves:
        $ v7_kiwiiPost5 = KiwiiPost(chris, "phone/kiwii/Posts/v7/chpost1.webp", _("One of us!"), number_likes=133, mentions=[mc])
        $ v7_kiwiiPost5.newComment(cameron, _("Losers"), 3)
        $ v7_kiwiiPost5.newComment(imre, _("Hell yeah bro!"), 14)
        $ v7_kiwiiPost5.newComment(aubrey, _("Woohoo!"), 35)

    if emilyText:
        play sound sound.vibrate
        
        $ MessengerService.new_message(emily, _("It's okay. You'll get the surprise another time..."))
        $ MessengerService.add_reply(emily, _("Exciting :)"))

    play music "music/mindie2.mp3"
    queue music [ "music/m16punk.mp3", "music/mindie1.mp3" ]
    
    if CharacterService.is_mad(imre):
        scene s866 # Camera - TPP (shot should not include Imre's bed). MC sitting up on his bed, mouth closed.
        with dissolve
        u "(Oh shit, it's history class today, isn't it? Gotta wear that costume.)"

        if costume == 1: # Viking
            scene s867 # MC in Viking costume looking at a mirror and laughing a little
            with fade
            u "(Damn I don't know about this. I look like a cave man.)"
            u "(Well, time to leave to the class.)"

        elif costume == 2: # Knight
            scene s867a # MC in Knight costume looking at a mirror, smiling and mouth closed, his right hand folded near his stomach
            with fade
            u "(That's not bad at all. I'm kind of feeling this one.)"

            scene s867b # Same as s876a but mouth open and MC moves his hand out as if offering a girl to hold it
            with dissolve
            u "Come with me princess. I'm your knight in shining armor. Hahaha."

            scene s867a
            with dissolve
            u "(Time to leave to the class.)"

        else: # Cowboy
            scene s867c # MC looking at a mirror in Cowboy costume with a silly laugh
            with fade
            u "Yeeeehaawww!"
            u "(Hahaha. I look like one of those hired male strippers. Oh god.)"
            u "(Well, time to leave to the class.)"

        scene s867d # MC left and the shot is empty with only the mirror to be seen
        with dissolve
        pause 0.5

    elif joinwolves:
        scene s866
        with dissolve
        imre "Morning."

        scene s868 # Camera - FPP. MC and Imre close up in the middle of their room. Imre mouth closed neutral expression (Imre not in his costume yet)
        with dissolve
        u "Morning. Almost overslept there."

        scene s868a # Imre mouth open neutral expression
        with dissolve
        imre "I would've woken you up."

        scene s868
        with dissolve
        u "Man, can you believe it still? Feels like a dream."

        scene s868b # Imre happy and talking
        with dissolve
        imre "I'm still on cloud nine dude. All our biggest dreams coming true."

        scene s868c # Imre happy, mouth closed
        with dissolve
        u "Haha, yeah. We're Wolves now baby."

        scene s868b
        with dissolve
        imre "We gotta wear those costumes today."

        scene s868c # Imre happy, mouth closed
        with dissolve
        u "Oh yeah, it's history today. Let's hurry up."

        if costume == 1: # Viking
            scene s869 # Camera - TPP. MC and Imre close up in their room wearing their costumes (MC as Viking). Neutral expressions and mouths closed
            with fade
            pause 0.5

            scene s870 # Camera - FPP. MC and Imre close up. Imre slightly laughing and mouth open
            with dissolve
            imre "Haha man, you look dumb."

            scene s870a # Imre slightly laughing and mouth closed
            with dissolve
            u "Me? Look at yourself."

            scene s870b # Imre looking down at his own costume and laughing (tilt the camera a little to show more of his costume)
            with dissolve
            imre "Haha true!"

            scene s870
            with dissolve
            imre "But Viking, it's so... barbaric."

            scene s870a
            with dissolve
            u "The ladies like barbaric."

            scene s870
            with dissolve
            imre "You're probably right about that."

            scene s870a
            with dissolve
            u "Ready to go?"

            scene s870
            with dissolve
            imre "Yeah."

        elif costume == 2:
            scene s871 # Camera - TPP. MC and Imre close up in their room wearing their costumes (MC as Knight). Neutral expressions and mouths closed
            with fade
            pause 0.5

            scene s870
            with dissolve
            imre "Man, that's actually a pretty dope fit."

            scene s870a
            with dissolve
            u "Haha, nah."

            scene s870
            with dissolve
            imre "Yeah, it's pretty badass. It's better than mine, at least."

            scene s870b
            with dissolve
            imre "Yeah, definitely much better than mine."

            scene s870a
            with dissolve
            u "Alright, I'll give you that."

            scene s870
            with dissolve
            imre "Haha. Yeah, it's bad."

            scene s870a
            with dissolve
            u "You ready to go?"
            imre "Mhm."

        else: # cowboy
            scene s872 # Camera - TPP. MC and Imre close up in their room wearing their costumes (MC as Cowboy). Neutral expressions and mouths closed
            with fade
            pause 0.5

            scene s870
            with dissolve
            imre "Man, a cowboy?"

            scene s870a
            with dissolve
            u "And the best one in town!"

            scene s870
            with dissolve
            imre "Haha. Don't come stomping on my rodeo!"

            scene s870a
            with dissolve
            u "Alright, alright. And yours is better?"

            scene s870b
            with dissolve
            imre "Haha, nah."

            scene s870a
            with dissolve
            u "You ready to go?"

            scene s870
            with dissolve
            imre "Yeah, let's go."

    else:
        scene s866
        with dissolve
        pause 0.5

        scene s873 # Camera - FPP. MC sitting in bed and looking at Imre who is getting into his costume
        with dissolve
        u "Morning. You up already?"
        imre "Mhm."
        u "(I should hurry up and get that costume on.)"

        if costume == 1: # Viking
            scene s867
            with fade
            u "(Damn, I don't know about this. I look like a cave man.)"
            u "(Well, let's see if Imre is done.)"

        elif costume == 2: # Knight
            scene s867a
            with fade
            u "(That's not bad at all. I'm kind of feeling this one.)"

            scene s867b
            with dissolve
            u "{size=-5}Come with me princess. I'm your knight in shining armor *laughs*{/size}"

            scene s867a
            with dissolve
            u "(Let's see if Imre is ready to go.)"

        else: # Cowboy
            scene s867c
            with fade
            u "Yeeeehaawww!"
            u "(Hahaha. I look like one of those hired male strippers. Oh god *laughs*)"
            u "(Let's see if Imre is done.)"

        if costume == 1:
            scene s869
            with fade
            pause 0.5

        elif costume == 2:
            scene s871
            with fade
            pause 0.5

        else:
            scene s872
            with fade
            pause 0.5

        scene s870c # Imre slightly questioning look, mouth open
        with dissolve
        imre "So... why weren't you at the Wolves pledge last night?"

        scene s870d # Imre slightly questioing look and mouth closed
        with dissolve
        u "Oh.. uhm... I totally blanked. Got deep in an essay and by the time I saw the clock, it was two hours too late."

        scene s870e # Imre suspicious look and mouth closed
        with dissolve
        u "I didn't wanna show up late. Would've looked bad. So I just went to bed after."

        scene s870f # Imre suspicious look and mouth open
        with dissolve
        imre "Mhm... Sure. Well, you ready?"

        scene s870e
        with dissolve
        u "Yeah, let's go."

########## SCENE 17 HISTORY LECTURE Comments for Finn: Marked with "###"

    ###Copy paste transcribed script into right spot, add defaults and defines at the start of the script

    label history_class: #for compatibility only
    scene s875 # Camera - TPP, Scene - History class, so everyone is in their costumes. Note that MC can be Viking, Knight or Cowboy.(### So MC shouldn't be in this.) Shot showing Penelope sitting in the first row and Lee standing near the board looking towards the students.
    with fade
    pause 1

    ### I deleted s876 cause I felt it was too much work for the renderers and not were Imre sat last time

    if costume == 1:
        scene s877 # Camera - TPP. Close up of MC and Imre. MC about to take the seat beside Imre. Imre notices the MC and looks at him neutral expression. MC in Viking costume
        with dissolve
        pause 0.5

    elif costume == 2:
        scene s877a # Same as s877 but MC in Knight costume
        with dissolve
        pause 0.5

    else:
        scene s877b # Same as s877 but MC in Cowboy costume
        with dissolve
        pause 0.5

    if CharacterService.is_mad(imre) and joinwolves:
        scene s878 # Camera - FPP. MC sitting beside Imre. Imre looking at MC with a bored/uninterested expression. Imre mouth closed
        with dissolve
        u "Hey."

        scene s878a # Imre mouth open
        with dissolve
        imre "Hey man."

        scene s878
        with dissolve
        u "What's up?"

        scene s878a
        with dissolve
        imre "Oh, uh... not much. Just here."

        scene s878b # Imre looking forward as if ignoring the MC, mouth closed
        with dissolve
        u "Mhm."

        scene s878c # Same as s878b but mouth open
        with dissolve
        imre "Nice costume dude."

        scene s878b
        with dissolve
        u "Haha... yeah."

        scene s878
        with dissolve
        u "So, the Wolves. You stoked or what?"

        scene s878d # Imre looking at the camera and smiling a little, mouth open
        with dissolve
        imre "Man, I've been waiting for this day for a while."

        scene s878e # Same as s878d but mouth closed
        with dissolve
        u "Haha, thought so."

        scene s878d
        with dissolve
        imre "Yeah, I'm ready to start fighting already."

        scene s878e
        with dissolve
        u "Oh, so you've been training."

        scene s878d
        with dissolve
        imre "Of course! And I think we should start training together again."
        imre "But this time in the Wolves gym, it's gonna be awesome!"

    elif CharacterService.is_mad(imre):
        scene s878b
        with dissolve
        pause
        u "Hey."

        scene s878c
        with dissolve
        imre "Hey."

    else:
        scene s878f # Imre leaning towards MC (as if whispering) while looking towards Lee and laughing, mouth open.
        with dissolve
        imre "Oh god, look at this clown."

        scene s879 # Camera - TPP. Shot of Lee walking funny."walking like he has a stick up his ass" is what it should look like xD
        with dissolve
        pause 0.5

        scene s878g # Same as s878f but mouth closed
        with dissolve
        u "*Laughs* Walking like he has a stick up his ass."

        scene s878f
        with dissolve
        imre "Probably does hahaha."

        scene s878g
        with dissolve
        u "Yeah who knows where he goes after the class."

        scene s878f
        with dissolve
        imre "I vow to never find out."

    scene s880 # Camera - TPP. Shot of Lee walking and talking in his usual demeanor
    with dissolve
    lee "Well, well... It is so nice to see you all dressed up in your outfits."

    scene s880a # Lee walking and talking shot 2
    with dissolve
    lee "Some of you did very well in choosing, while others... not so much I might say."

    scene s880
    with dissolve
    lee "But nevertheless, doesn't it feel so good to wear something from the past?"

    scene s880b # Lee giddily talking with his two hands stretched out
    with dissolve
    lee "It's like walking through a time machine!"

    scene s881 # Close up of Cameron looking towards Lee (not visible) and talking while laughing
    with dissolve
    ca "Haha. Fuckin' weirdo."

    scene s882 # Close up of Lee offended and talking. Camera should be closer than s880. He is looking towards Cameron (not visible in the shot)
    with dissolve
    lee "Who said that?"

    scene s882a # Same as s882 but Lee is looking towards MC
    with dissolve
    lee "You know, if you guys think you know so much about history, why don't you guys just teach the class instead?"
    class1 "..."

    scene s882
    with dissolve
    lee "I'm listening!"

    if costume == 1:
        class1 "..."

        scene s882a # Same as s882 but Lee is looking towards MC
        with dissolve
        lee "[name]. You come up here then."

        scene s883 # Camera - TPP. Close up of MC in viking costume surprised and talking
        with dissolve
        u "Me?"
        lee "Yeah, come up here."

        scene s882a
        with dissolve
        lee "Why don't you show the class what you picked for your walk through the history?"

        scene s883
        with dissolve
        u "Uh..."

        scene s882a
        with dissolve
        lee "Come on up. Hurry young man!"

        scene s884 # Camera - TPP (far shot). Shot of MC and Lee in front of the class room. Lee talking while looking at the MC. MC slightly confused, mouth closed
        with fade
        lee "And what are you wearing today?"

        scene s884a # Same as s884 but MC is talking now
        with dissolve
        u "Uh... a viking?"

        scene s884
        with dissolve
        lee "Ah, very well."

        scene s884b # Lee talking to the class with his finger pointing up, and his usual creepy smile. MC just looking around
        with dissolve
        lee "Did you guys know that although vikings appear to come off as straggly, they were actually quite known for their cleanliness?"
        lee "They usually bathed once a week!"

        scene s885 # Close up of Penelope in her costume grossed out and talking
        with dissolve
        pe "Eeww! Gross."

        scene s884c # Same as s884b but Lee explanatory with one hand up near his waist level (mouth open)
        with dissolve
        lee "Well, back then you'd be lucky to meet someone who bathed once a month."
        lee "But I must say [name]..."

        scene s884d # Lee poking at the horns on MC's Viking costume and talking. MC is slightly embarrassed
        with dissolve
        lee "...vikings didn't have horns on their helmets."
        lee "Very unfortunate."

        menu:
            "Defend yourself":
                $ reputation.add_point(RepComponent.TROUBLEMAKER)

                scene s886 # Camera - TPP (Similar to s884 but closer). MC confident and talking looking at Lee. Lee mouth closed and looking at the MC
                with dissolve
                u "Mr. Lee, I have a question for you."

                scene s886a # Lee talking now, creepy smile
                with dissolve
                lee "I love questions! What is it?"

                scene s886
                with dissolve
                u "How do you know Vikings don't got horns on their helmets?"

                scene s886a
                with dissolve
                lee "History!"

                scene s884c
                with dissolve
                lee "Historians studied this. They found paintings depicting Vikings and get this..."

                scene s884b
                with dissolve
                lee "...they even uncovered real Viking helmets!"
                lee "Isn't that amazing?"

                scene s886
                with dissolve
                u "Well, you wanna know what I think?"

                scene s886a
                with dissolve
                lee "And what would that be?"

                scene s886
                with dissolve
                u "I think while you're stuck buried in the past, we're out here living in the real world like normal people."

                scene s886b # MC confident look, not talking. Lee embarrassed and looking towards the class, not talking
                with dissolve
                class1 "Oooohhh *laughs*"

                scene s885a # Penelope chuckling
                with dissolve
                pause 0.5

                if not joinwolves:
                    scene s881
                    with dissolve
                    ca "Buurrnnn!"

                scene s887 # Close up of Lee's face. Completely dumbfounded look
                with dissolve
                lee "..."
                u "And I'll excuse myself back to my seat. Thank you very much."

                jump after_history

            "Stay silent":
                $ reputation.add_point(RepComponent.BOYFRIEND)

                scene s886c # MC looking down in embarrassment. Lee looking at MC. Both mouths closed
                with dissolve
                pause 0.5

                scene s881
                with dissolve
                ca "Ha!"

                scene s886d # Lee talking while pointing towards MC's chair. MC still embarrassed
                with dissolve
                lee "Okay, [name]. You can go sit now."

                jump after_history

    scene s882a
    with dissolve
    class1 "..."

    scene s882
    with dissolve
    lee "Cameron, why don't you come up and show the class your costume?"

    scene s881a # Cameron shocked/annoyed and mouth open
    with dissolve
    ca "What?"

    scene s882
    with dissolve
    lee "Maybe you can give us a history lesson and even some insight into what you are representing today."

    scene s888 # Camera - TPP. Shot of Cameron and Lee in front of the class room. Lee talking while looking at Cameron. Cameron looking around uninterested/whatever look, mouth closed
    with fade
    lee "Ha! Class, this is a perfect example of how not to do your history homework right."

    scene s888a # Cameron annoyed, talking while pointing towards his costume. Lee mouth closed
    with dissolve
    ca "You said historical figure... this guy is ancient!"

    scene s885a
    with dissolve
    pause 0.5

    scene s888
    with dissolve
    lee "Mister Cameron, {b}historical{/b}."
    lee "Elvis might have made history with his work, but he is considered a musical legend, not a historical figure."

    scene s889 # Close up of Lee creepy laugh, mouth open
    lee "And he hasn't been gone that long! Hahaha."
    ca "Whatever."

    scene s888b # Cameron annoyed. Lee pointing towards Cameron's seat and talking
    with dissolve
    lee "Well, Cameron you may go sit back down. But next time try Google or even better, your history book!"

label after_history:
    scene clocka
    with fade
    pause 0.5

    play sound "sounds/clock2.mp3"

    scene clockb
    with dissolve
    pause 0.5

    scene clockc
    with dissolve
    pause 0.5

    scene clockd
    with dissolve
    pause 0.5

    stop sound

    scene clocke
    with dissolve


    pause 0.5

### Now you mark the next scene and write down the name like below:

########## SCENE 18 PENELOPE AFTER HISTORY
    # MC and Pen talking in classroom after class ### the next scene only works inside the classroom so this shouldn't be in the hallway
    label pen_after_history: #for compatibility only
    if v7_emily_bowling:
        scene s891 # Camera - FPP (far shot). Penelope in classroom about to walk out (away from the camera) in her costume
        with fade
        u "Hey Penelope!"

        scene s892 # Camera - FPP. MC and Penelope talking, don't get too close. Pen is uncomfortable and forcing a smile, mouth open
        with dissolve
        pe "Oh hey."

        scene s892a # Pen mouth closed
        with dissolve
        u "Love your costume. You look amazing!"

        scene s892
        with dissolve
        pe "Uh.. yeah thanks."

        scene s892b # Pen starts to walk away
        with dissolve
        u "Oh, where are you going?"

        scene s892c # Pen turns her head around to reply hesitantly
        with dissolve
        pe "Sorry, got some stuff."

        scene s892d # Pen walked off
        with dissolve
        u "(That was weird.)"

    elif not costumeaubrey:
        scene s891
        with dissolve
        u "Hey Penelope!"

        scene s893 # Camera - FPP. MC and Penelope close up. Pen smiling wide and talking
        with dissolve
        pe "Hey [name]!"

        scene s893a # Same as s893 but Pen mouth closed
        with dissolve
        u "You look amazing!"

        scene s893
        with dissolve
        pe "Really? Thank you!"

        scene s893a
        with dissolve
        u "Yeah, the costume suits you pretty well."

        scene s894 # Pen kinda blushing and showing off her costume - full shot. MC should not be visible
        with dissolve
        pause 0.8

        scene s893
        with dissolve
        pe "I was so nervous to wear it in front of the entire class!"
        pe "I'm just glad Mr. Lee didn't pull me up. I would've literally been a deer in headlights."

        scene s893a
        with dissolve
        u "Haha."

        if costume == 1:
            scene s893
            with dissolve
            pe "By the way, I told you the horns were not historically accurate."

            scene s893a
            with dissolve
            u "Haha, I know. But you gotta admit, this is a dope costume."

            scene s893b # Pen flirty smile, mouth open
            with dissolve
            pe "Alright, I'll give you that. *laugh*"

        elif costume == 2:
            scene s893
            with dissolve
            pe "I'm glad you ended up with this costume."

            scene s893b
            with dissolve
            pe "It looks good on you and we're totally matching eras! *laugh*"

            scene s895 # Camera - TPP. Shot of Knight MC bowing and talking. Pen is laughing
            with dissolve
            u "Why, thank you, milady!"

            scene s893b
            with dissolve
            pe "Oh stop it, haha."

        else:
            scene s893
            with dissolve
            pe "I hope you're still not considering being a cowboy as your career."

            scene s893a
            with dissolve
            u "Maybe I am. I didn't buy this costume for nothin'. All I need is a horse with a saddle."

            scene s896 # Camera - TPP. Shot of Cowboy MC tipping his hat and talking confidently. Pen is laughing
            with dissolve
            u "Howdy lady! Need a ride?"

            scene s893b
            with dissolve
            pe "Oh stop it, you're stupid! *laugh*"

        scene s893
        with dissolve
        pe "Well, it was good talking to you. Maybe we'll hang out soon."

        scene s893a
        with dissolve
        u "Definitely, bye."

        scene s892d
        with dissolve
        pause 0.5

    else:
        scene s891
        with dissolve
        u "Hey Penelope!"

        scene s893
        with dissolve
        pe "Hey [name]!"

        scene s893a
        with dissolve
        u "Love your costume!"

        scene s894
        with dissolve
        pause 0.8

        scene s893
        with dissolve
        pe "I was nervous, because it's kinda like a maiden costume, but it looks so cute and I really couldn't help myself."

        scene s893a
        with dissolve
        u "Well, it's a good choice. You look amazing!"

        scene s893
        with dissolve
        pe "Thanks!"
        pe "I'm just glad Mr. Lee didn't pull me up in front of the whole class. I would've had no idea what to say."

        scene s893a
        with dissolve
        u "Haha."

        if costume == 1:
            scene s893
            with dissolve
            pe "You know, you could've asked me for some advice on the costumes. I would've told you that one wasn't historically accurate."

            scene s893a
            with dissolve
            u "Well... you win some, you lose some. I still think the costume looks dope. Haha."

            scene s893b
            with dissolve
            pe "Alright, I'll give you that one. *laugh*"

        elif costume == 2:
            scene s893b
            with dissolve
            pe "So, is this Knight gonna come and save me from my tower?"

            scene s895
            with dissolve
            u "Without a doubt, milady!"

            scene s893b
            with dissolve
            pe "Haha. Very cute."

            scene s893
            with dissolve
            pe "Glad you chose this outfit, we're totally matching eras! *laugh*"

            scene s893a
            with dissolve
            u "Haha, yeah."

        else:
            scene s893
            with dissolve
            pe "I must say, I'm surprised by this costume."

            scene s896
            with dissolve
            u "Surprised at what a sexy cowboy I am?"

            scene s893
            with dissolve
            pe "Haha no, I was gonna say it's pretty interesting..."

            scene s893b
            with dissolve
            pe "...but I'm digging the confidence."

            scene s893a
            with dissolve
            u "Haha, thanks."

        scene s893
        with dissolve
        pe "Okay well, I gotta be heading out. Maybe we can catch up soon."

        scene s893a
        with dissolve
        u "Sure, bye."

        scene s892d
        with dissolve
        pause 0.5

    if joinwolves:
        jump after_cam_history

########## SCENE 19 CAMERON AFTER HISTORY
    ### Here I deleted the render since Cameron can just shout at when you're looking in a different direction from before
    label cam_task_2: #for compatibility only
    ca "Hey shitface, come here."

    scene s901 # Camera - FPP. MC and Cameron convo inside the classroom (near the door). Cameron cunning smile, mouth closed
    with dissolve

    menu:
        "Make fun of his costume":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            u "You serious bro? Elvis? Is that how far you could think back? Hahaha."

            scene s901a # Same as s901 but Cameron mouth open
            with dissolve
            ca "At least I don't look as stupid as you do in that."

            scene s901
            with dissolve
            u "Disagree, but what's up?"

        "Just say hello":
            $ reputation.add_point(RepComponent.BRO)

            u "Hey, what's up?"

    if apesVids == 1:
        scene s901a
        with dissolve
        ca "Time for your next video. Let's see if you can handle this one."

        scene s901
        with dissolve
        u "What's it gonna be this time?"

    else:
        scene s901b # Cameron serious talking
        with dissolve
        ca "It's time for your first video. Don't fuckin' pussy out like last time."
        ca "I don't wanna fail as a coach the first time. You understand?"

        scene s901c # Cameron serious mouth closed
        with dissolve
        u "Uhm.. Okay.. What is it?"

    scene s902 # Close up shot of Lee bent over and looking into his bag
    with dissolve
    ca "You're gonna pull down Mr. Lee's pants."

    scene s901
    with dissolve
    u "What!?"

    scene s901a
    with dissolve
    ca "You heard me, you're gonna pull Mr. Lee's pants down."

    scene s901
    with dissolve
    u "Are you kidding me? What's the point of even joining the Apes if I'm just gonna get kicked out of the school?"

    scene s901a
    with dissolve
    ca "Then you better be fast enough to get outta there before he sees you."

    scene s901
    with dissolve
    u "Tell me you're joking. I'm in a fucking costume to be that fast."

    scene s901b
    with dissolve
    ca "Don't drag this. You gotta prove you're a winner."
    ca "You either do it, or pussy out. What's it gonna be?"

    scene s901c
    with dissolve

    menu:
        "Do it":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            u "Fine! If you're that interested in looking at Mr. Lee's naked ass."

            scene s901a
            with dissolve
            ca "Haha, fuck you! Lemme get the cam running."

        "That's stupid and risky":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            u "Nah, that's stupid as fuck. I'm not getting kicked out of school just to join the Apes."

            scene s901d # Cameron pissed and mouth closed
            with dissolve
            u "When you got better ideas, tell me and then we'll talk."

            scene s901e # Cameron pissed and talking
            with dissolve
            if apesVids == 1:
                ca "You're a fuckin' loser."

            else:
                ca "You're the biggest fuckin' loser of all time."

            scene s901f # Cameron walking away from MC
            with dissolve
            u "Whatever dude."

            jump after_cam_history

    label lee_pants_task: #for compatibility only
    scene s903 # Shot of Lee writing something on the board as seen from Cameron's phone (He is standing at the door. Need not render the whole classroom, make it look like he zoomed in and add camera interface.) MC is not visible in the shot
    with fade
    ca "{size=-10}Whenever you're ready shitface.{/size}"

    scene s904 # Camera - FPP. Shot of MC around 5 feet behind Lee who is busy writing something on the board
    with dissolve
    u "(I gotta be quick if I'm gonna get outta this safely.)"

    scene s905 # Same as s904 but MC is now 2 feet behind Lee
    with dissolve

    play sound "sounds/countdown.mp3" #check - is this fine?

    menu (fail_label="lee_pants_fail"): # 3 second timer default
        "Pull it":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            $ apesVids += 1
            stop sound

            if is_censored:
                call screen censored_popup("v7_nsfwSkipLabel2")

            scene s905a # Same as s905 but Lee's pants down showing his naked ass and he is startled. (Lee is still facing the board)
            with vpunch
            pause 0.5

            if costume == 1:
                scene s906 # Camera - TPP. Shot of Lee startled and fixing his pants in hurry while facing the board and MC running towards the door in Vikings costume
                with hpunch
                pause 0.5

            elif costume == 2:
                scene s906a # Same as s906 but Knight costume
                with hpunch
                pause 0.5

            else:
                scene s906b # Same as s906 but Cowboy costume
                with hpunch
                pause 0.5

            label v7_nsfwSkipLabel2:
                scene s907 # Camera - FPP. MC and Cameron running through the door. Cameron is in front of MC with his phone in his hand. MC is almost out of the door
                with vpunch

                $ grant_achievement("lee_way")

                lee "Who was that? {b}WHO WAS THAT?{/b}"
                ca "HAHAHA! FUCKIN' ACES!"

                jump after_cam_history

        "...":
            jump lee_pants_fail

label lee_pants_fail:
    stop sound
    # No point changes here

    scene s908 # Camera - FPP. Same as s905 but Lee turned back and is talking with his usual smile
    with vpunch
    lee "Oh, hi [name]."
    lee "Anything I can help you with? Has history got you all muddled up?"

    scene s908a # Lee mouth closed
    with dissolve
    u "Uhh... no. I just thought I forgot something here."

    scene s908
    with dissolve
    lee "Okay, you can always stop by if you wanna discuss the past, alright?"

    scene s908a
    with dissolve
    u "Uhh... sure, Mr. Lee."

    scene s908b # Lee turns back towards the board and continues whatever he was doing
    with dissolve
    pause 0.5

    scene s901e
    with fade
    ca "What the hell man? Don't waste my time like that again."

    scene s901d
    with dissolve
    u "Dude, at least I tried. You should've been in my shoes."

    scene s901e
    with dissolve
    ca "That ain't gonna cut it if you wanna be a winner!"

    scene s901f
    with dissolve
    ca "You better fuckin' finish the task next time."
    u "(Damn it! At least Mr. Lee didn't get suspicious.)"

########## SCENE 20 BACK AT YOUR DORM
label after_cam_history:
    stop music
    scene s911 # Camera - TPP. MC outside his room opening the door.
    with fade

    u "(Finally back in my normal clothes.)"

    scene s912 # Camera - TPP. MC notices the homecoming flyer on his desk
    with dissolve
    u "(Damn, I totally forgot about it. Homecoming's tomorrow.)"
    u "(I still need to ask a girl as well as rent a suit.)"
    u "(I sure hope this decision doesn't create eight alternate timelines...)"
    play music "music/mlove.mp3" fadein 2
    queue music [ "music/mchill1.mp3", "music/mindie5.mp3" ]
    call screen hc_select

    # If chose to go alone
label hc_no_girl:
    $ hcGirl = "alone"

    u "*sigh* (I think it might be for the best if I go to homecoming all by myself.)"
    jump after_hc_selection

########## SCENE 21 ASKING AMBER

    # Amber promposal
label hc_asking_amber:
    $ hcAsked.append("amber")
    u "(I wonder if Amber will be interested. Let's see what she has to say about it.)"

    scene s918 # Camera - TPP. mc with something romantic under his arm knocking on ambers door
    with fade
    play sound sound.knock

    pause 1.5

    play sound "sounds/dooropen.mp3"
    scene s919 # Camera - FPP. Amber opens the door and talking with a confused look
    with dissolve
    am "Uhmmm... are you about to ask me to go to homecoming with you?"

    scene s919a # Same as s919 but Amber mouth closed
    with dissolve
    u "Uh... yes."

    scene s919
    with dissolve
    am "Uhm.. [name]-"

    scene s919a
    with dissolve
    u "*Chuckles* What?"

    scene s919b # amber serious smile, empathy
    with dissolve
    am "Look, this is nice and all, but I don't do dances."

    scene s919c
    with dissolve
    u "What do you mean?"

    scene s919b
    with dissolve
    am "It means I don't do dances... aaannd I'm not going to homecoming."

    scene s919c
    with dissolve
    u "Come on, it's just a dance."

    scene s919b
    with dissolve
    am "And I'm telling you it's not my thing."
    am "Sorry [name]."

    if reputation() == Reputations.POPULAR:
        call screen reputation_popup

        scene s919d # Amber flirty and talking
        with dissolve
        am "But I might have a better idea. I mean definitely better than some lame-ass homecoming at least."

        scene s919e
        with dissolve
        u "Oh yeah? What's that?"

        scene s919d
        with dissolve
        am "*Whispers* I got some molly."
        am "How about we skip the dance together? I promise it'll be a lot more fun."
        menu:
            "Alright, I'm in":
                $ reputation.add_point(RepComponent.TROUBLEMAKER)
                $ hcGirl = "amber"
                $ CharacterService.set_relationship(amber, Relationship.FWB, mc)

                scene s919e
                with dissolve
                u "Alright, I'm in let's do it."

                scene s919d
                with dissolve
                am "Great, I'll see you tomorrow evening then."

                scene s919e
                with dissolve
                u "Cool."
                u "(Guess I don't need a suit now.)"

                jump after_hc_selection

            "I'd rather go to the dance":
                $ reputation.add_point(RepComponent.BOYFRIEND)

                scene s919e
                with dissolve
                u "Sorry, I'd rather go to the dance."

                scene s919f # Amber surprised in disbelief and talking
                with dissolve
                am "Oookay... You enjoy your dance then, haha."

                scene s919g
                with dissolve
                u "Thanks. I'll see you, I guess."

                scene s919f
                with dissolve
                am "Yeah. See ya."

                scene s919h # amber gone
                with fade
                u "(Well, maybe I can take someone else to the dance?)"

                call screen hc_select

    else:
        scene s919c
        with dissolve

        u "Alright, well thanks for coming. I'll see you, I guess."

        scene s919b
        with dissolve
        am "Yeah. See ya."

        scene s919h # amber gone
        with fade
        u "(Well, maybe I can take someone else to the dance?)"

        call screen hc_select

########## SCENE 22 ASKING AUBREY

    # Aubrey promposal
label hc_asking_aubrey:
    $ hcAsked.append("aubrey")
    u "(I'll text Aubrey to meet me at the beach.)"

    scene s975 # Camera - TPP. MC in a secluded part of the beach, with a rose , aubrey walking towards him in bikini, surprised smile
    with fade

    au "[name]? What is this?"

    scene s976a # close up aubrey mouth closed, awkward smile
    with dissolve

    u "Aubrey, would you go to homecoming with me?"

    scene s976
    with dissolve
    au "I'm pretty sure, I told you I'm not the romance type, haha."

    if CharacterService.is_fwb(aubrey):
        au "And I also like the secrecy of our relationship."

    scene s976a
    with dissolve
    u "Sooo..."

    scene s976
    with dissolve
    au "Sorry, it's not my thing."

    scene s976a
    with dissolve
    u "Oh okay..."

    scene s976
    with dissolve
    au "It's really nice that you asked though."

    if CharacterService.is_fwb(aubrey) and not simp:
        scene s976b # aubrey flirty
        with dissolve

        au "And hey... if you get bored of whomever you go with, then come find me. And maybe we can have some fun..."

        scene s976c
        with dissolve
        u "Haha, that does sound enticing. Anyway, I'll see you then."

        scene s976b
        with dissolve

    else:
        scene s976a
        with dissolve
        u "Right. Uhm... anyway, I'll see you around then."

        scene s976
        with dissolve

    au "Haha, alright. Bye."

    scene s976d #aubrye gone
    with fade
    u "(Maybe I should ask someone else.)"

    call screen hc_select

########## SCENE 23 ASKING AUTUMN
    # Autumn promposal
label hc_asking_autumn:
    $ hcAsked.append("autumn")
    u "(I'll surprise her.)"

    scene s925 # Camera - TPP (far shot). Autumn in library studying on her laptop
    with fade
    pause 1.0

    # play loud trumpet music

    scene s925a # Autumn startled and looks around
    with hpunch

    "*Trumpet starts playing*"

    scene s926 # showing mc walking towards autumn, followed by poet2 playing the trumpet
    with dissolve
    aut "What the hell?"

    # quick fade out trumpet

    scene s927a # fpp close up autumn perplexed mouth closed
    with dissolve
    u "Autumn! Autumn! Will you go to homecoming wi-"

    scene s927b  # Autumn embarrassed and a bit mad
    with dissolve
    aut "Shh! Shhh! *Whispers* What are you doing?!"

    scene s927c
    with dissolve
    u "What does it look like I'm doing? Asking you to homecoming!"

    scene s927b
    with dissolve
    aut "*Whispers* In the library?!"

    scene s927c
    with dissolve
    u "Uhm... I-"

    scene s927d # autumn is sorry, empathy
    with dissolve
    aut "*Whispers* Sorry, I have a thesis to write and I really don't enjoy dances."

    scene s927e
    with dissolve
    u "Aww, come on."

    scene s927d
    with dissolve
    aut "*Whispers* Sorry, but no."

    scene s927e
    with dissolve
    u "*Whispers* Alright, alright. I get it."
    u "*Whispers* I'll uh... see you later then."

    scene s927d
    with dissolve
    aut "*Whispers* Yeah, bye."

    scene s928 #tpp , showing mc about to walk out of the library
    with dissolve

    u "(Damn, did I overdo it?)"
    u "(Anyways, let's see who else I could ask.)"

    call screen hc_select


########## SCENE 24 ASKING CHLOE
    # Chloe promposal
label hc_asking_chloe:
    $ hcAsked.append("chloe")
    u "(I wonder where Chloe even is right now.)"

    scene s935 # Camera - TPP. Chloe running in the park
    with fade

    pause 0.5

    if volleyball:
        scene s936 # Camera - TPP. Chloe runs towards Mc who's kneeling on the path with the blue volleyball that says "Hoco?" on it
        with dissolve

    else:
        scene s936a # Camera - TPP. Chloe runs towards Mc who's kneeling on the path with a rose
        with dissolve

    pause 0.5

    scene s937 # FPP (you're kneeling, so looking up), Close up chloe looking at you smiling surprised
    with dissolve

    cl "[name]?"

    scene s937a
    with dissolve

    u "Chloe, do you wanna go to homecoming with me?"

    scene s937b # chloe hand on her forehead not sure what to do smiling
    with dissolve

    cl "[name], I have so much to do at the dance. I'm in charge of a lot of the planning and organizing, I don't know if I can-"

    scene s937c
    with dissolve

    u "Come on, I know you want to."

    if volleyball or reputation() == Reputations.POPULAR:
        $ hcGirl = "chloe"

        if not volleyball:
            call screen reputation_popup

        scene s937d # chloe smiling eyebrow raised
        with dissolve

        cl "*Chuckles* Alright, fine. I guess I'll have to find a replacement."

        cl "I'll go to homecoming with you."

        u "Ayyy... I'll pick you up at eight."

        cl "You better not forget, haha."

        jump after_hc_selection

    else:
        scene s937f # chloe empathy, sorry
        with dissolve

        cl "I'm sorry [name], but I can't be anyone's date, I'd need to find a replacement and everything."

        cl "I'm really sorry."

        scene s937g
        with dissolve

        u "Okay..."

        u "Uhm... I guess enjoy your run."

        scene s937f # chloe empathy, sorry
        with dissolve

        cl "Thanks... I'll see you there."

        scene s937h  # chloe gone
        with fade

        u "(I guess I'll have to find someone else to ask.)"

        call screen hc_select


########## SCENE 25 ASKING EMILY
label hc_asking_emily:
    $ hcAsked.append("emily")
    $ hcGirl = "emily"

    scene s950 #you kneeling alone in emily's dorm looking at the door with a box of chocolates
    with fade

    pause 0.5

    play sound "sounds/dooropen.mp3"

    scene s950a # emily comes in
    with dissolve

    u "Em... Will you be my date for homecoming?"

    scene s951 # fpp close up Emily ecstatic, in front of open door
    with dissolve
    em "What? How did you?-"

    em "Yes! Definitely!"

    scene s951a
    with dissolve
    u "Great then. I'll pick you up tomorrow."

    scene s951
    with dissolve
    em "Wait! I have so many questions!"

    scene s951a
    with dissolve
    u "Ask them tomorrow, I gotta go rent a suit, haha."

    scene s951
    with dissolve
    em "*Chuckles* Okay! I can't wait."

    jump after_hc_selection

########## SCENE 26 ASKING LAUREN
    # Lauren promposal
label hc_asking_lauren:
    $ hcAsked.append("lauren")

    if CharacterService.is_girlfriend(lauren):
        u "(Of course I'm gonna ask Lauren.)"
    else:
        u "(Wonder if Lauren would wanna go with me...)"

    scene s965 # lauren walking through a hallway, there needs to be like a gallery path to stand on above, so mc can rain rose petals on her
    with fade

    pause 1.0

    scene s966 #tpp  showing mc from above raining rose petals on her
    with dissolve

    pause 0.5

    scene s966a # lauren looking up surprised
    with dissolve

    la "[name]? Was this you?"

    scene s967a #fpp  lauren close up looking up smiling suprrised, looking up at you
    with dissolve

    u "Will you go to Homecoming with me?"

    if CharacterService.is_girlfriend(lauren):
        $ hcGirl = "lauren"

        scene s967b # lauren laughing
        with dissolve
        la "Awww! Of course."

        la "*Laughs* But you really could have spelled out more than just the question mark."

        scene s967c
        with dissolve

        u "I didn't have that many rose petals, haha."

        u "I'll pick you up at eight."

        scene s967b # lauren laughing
        with dissolve
        la "*Chuckles* Alright."

        jump after_hc_selection

    elif reputation() == Reputations.LOYAL or beachfirstkiss:
        $ hcGirl = "lauren"
        
        if not beachfirstkiss:
            call screen reputation_popup

        $ CharacterService.set_relationship(lauren, Relationship.GIRLFRIEND, mc)

        scene s967b # lauren laughing
        with dissolve
        la "*Laughs* You really could have spelled out more than just the question mark."

        la "But okay, I'll go with you."

        scene s967c
        with dissolve

        u "I didn't have that many rose petals, haha."

        u "I'll pick you up at eight."

        scene s967b # lauren laughing
        with dissolve
        la "*Chuckles* Alright."

        jump after_hc_selection

    else:
        scene s967d # lauren sorry, empathy
        with dissolve
        la "[name]..."

        la "Sorry, but no..."

        la "We're really good friends and I don't wanna mess that up. I feel like going to homecoming together is a romantic thing and I'm just not sure I want that right now..."

        scene s967e
        with dissolve
        u "Oh... That's uh- that's okay."

        scene s967d
        with dissolve
        la "I'm really sorry."

        scene s967e
        with dissolve
        u "No it's okay. I get it."
        u "I'll see you later then, I guess."

        scene s967d
        with dissolve
        la "Yeah, sorry. Goodbye."

        scene s967f # lauren gone
        with dissolve
        u "(Damn, that didn't go as I expected.)"

        u "(Now I gotta find someone else...)"

        call screen hc_select

########## SCENE 27 ASKING PENELOPE
    # Penelope promposal
label hc_asking_penelope:
    $ hcAsked.append("penelope")
    $ hcGirl = "penelope"

    scene s955 #tpp  behind penelope who's at her locker in soldiers ceremonial uniform, ideally looking riiculous
    with fade

    pause 0.5

    scene s955a #mc saluting
    with dissolve

    u "Sergeant Penelope?"

    scene s956 #tpp showing both from the side, penelope turns around laughing
    with dissolve

    pe "*Laughs* [name]? Why are you dressed like this?"

    scene s956a # no longer saluting
    with dissolve

    u "I have a query for you."

    scene s956b
    with dissolve

    pe "*Laughs* What is happening?"

    scene s956c
    with dissolve # mc pulls out a rose and bows slightly

    u "Will you go to homecoming with me?"

    if CharacterService.is_fwb(emily) or not bowling:
        scene s957 # fpp close up penelope unsure smili ng
        with dissolve

        pe "*Chuckles* [name], I don't... I don't know, I-"

        scene s957a # fpp close up penelope unsure smili ng
        with dissolve

        u "Come on, I bought this outfit just for you."

        scene s957b # penelope exciting
        with dissolve

        pe "Okay! I'll go with you!"

    else:
        scene s957b # penelope exciting
        with dissolve

        pe "Yes! I'll go with you!"

    scene s957c # penelope exciting
    with dissolve

    u "Yayyy! I'll pick you up at eight."

    scene s957b # penelope exciting
    with dissolve

    pe "Haha okay, but you better wear a proper suit."

    scene s957c
    with dissolve

    u "Haha, we'll see."

    jump after_hc_selection

########## SCENE 28 ASKING RILEY
label hc_asking_riley:
    $ hcAsked.append("riley")

    scene s958 #mc knocks on riley's dorm door, glass slipper in on hand
    with fade

    play sound sound.knock

    pause 1.5

    scene s958a #mc gets on one knee, holds the glass slipper out in front of him
    with dissolve

    pause 0.5

    play sound "sounds/dooropen.mp3"

    scene s959a #fpp close up riley opened the door a bit surprised
    with dissolve

    u "Will you be my Cinderella for homecoming?"

    if Moods.TEASED in riley.mood or reputation() == Reputations.CONFIDENT:
        if Moods.TEASED not in riley.mood:
            call screen reputation_popup

        $ hcGirl = "riley"

        scene s959b # riley excited
        with dissolve

        ri "Yes! Yes I will! How exciting!"

        scene s959c # riley excited
        with dissolve

        u "Awesome!"

        scene s959b # riley excited
        with dissolve

        ri "How did you know that I love Cinderella?"

        scene s959c # riley excited
        with dissolve

        u "A magician never reveals his secrets."

        u "I'll pick you at eight."

        scene s959b # riley excited
        with dissolve

        ri "Haha, okay. Can't wait!"

        jump after_hc_selection

    else:
        scene s959d # riley empathy, sorry
        with dissolve

        ri "Uhm... honestly I was just gonna go with some friends."

        ri "I mean, you could probably go with us if you want?"

        scene s959e
        with dissolve

        u "Oh... uhm no, that's okay. Thanks though."

        scene s959d
        with dissolve

        ri "I'm sorry, it's just-"

        scene s959e
        with dissolve

        u "No worries. I'll see you there then."

        scene s959d
        with dissolve

        ri "Uhm, okay. See you there."

        scene s960 # mc walking through the hallway disappointed with the slipper in his hand.
        with fade

        u "(Guess I'm asking someone else.)"

        call screen hc_select

### SCENE 29: Back to dorm after promposals
label after_hc_selection:
    if hcGirl == "amber":
        jump thurs_night_dorm


### SCENE 30 and 31: Buying a suit
label suit_rental:
    scene s992 # tpp you in a suit store at counter
    with fade
    clerk "Good evening, sir! How may I help you?"

    scene s993a # Same as s993 but Employee mouth closed
    with dissolve
    u "Hey, I need to rent a suit for homecoming."

    scene s993
    with dissolve
    clerk "Of course, sir. Follow me."
    stop music fadeout 3

    scene s994 #you walking out with a shopping bag
    with fade

    u "(Well that didn't take as long as expected.)"

    jump thurs_night_dorm


### SCENE 32: AFTER TUDEXO SHOPPING
label thurs_night_dorm:
    if joinwolves and CharacterService.is_mad(imre):
        scene s1002 # Camera - TPP. MC packing his bag, same as the one he has in scene 34
        with fade

        pause 1.0

        u "(Alright, time for the Wolves ceremony...)"

        u "(Can't believe I'm actually moving into the Wolves house. Kinda crazy.)"

        jump wolves_ceremony

    elif joinwolves:
        scene s1002
        with fade
        pause 0.7

        scene s1003 # Camera - fpp imre with bag next to you, same bag he has in scene 34, excited
        with dissolve

        imre "Ready to go?"

        scene s1003a
        with dissolve

        u "Yeah, let's go. Can't believe we're actually moving into the Wolves' house."

        scene s1003 # Camera - fpp imre with bag next to you, same bag he has in scene 34, excited
        with dissolve

        imre "I knooow. It's gonna be insane, bro."

        jump wolves_ceremony

########## SCENE 33 CHALLENGES W/ CAMERON
    #If you joined the apes:
    #A knock is heard at the door of MC's dorm. MC opens the door and finds Cameron standing in the doorway.

label cameron_thurs_tasks:
    play music "music/mchill1.mp3"
    scene scc1 # TPP. Shot of MC sat in his room on end of his bed.
    with fade

    pause 0.5

    play sound sound.knock
    scene scc1a # TPP. As above but MC turns his head to look at door.
    with dissolve

    pause 1.5
    
    play sound "sounds/dooropen.mp3"
    scene scc2 # FPP. Show MC door, now open, Cameron stood in threshold, neutral expression.
    with dissolve

    pause 0.5

    if apesVids > 0:
        scene scc3 # FPP. Closeup of Cameron, neutral expression, mouth closed.
        with dissolve

        u "Hey Cameron. What's up?"

        scene scc3a # FPP. As above, mouth open.
        with dissolve

        ca "You ready for more video challenges?"

        scene scc3 # FPP. Same as scc3.
        with dissolve

        u "Uh.. sure."

        scene scc4 # TPP. Show MC and Cameron fist bumping, smile on both faces.
        with dissolve

        pause 0.5

        scene scc5 # FPP. Show Cameron mouth open, smile.
        with dissolve

        ca "Hell yeah! That's what I like to hear. Let's go."

        scene scc5a # FPP. As above, mouth closed.
        with dissolve

        u "Alright."

    else:
        scene scc6 # FPP. Same as scc3 but Cameron slight angry expression, mouth closed, arms crossed.
        with dissolve

        u "Oh uh, hey Cameron. What's up?"

        scene scc6a # FPP. As scc6, mouth open.
        with dissolve

        ca "Time for video challenges. But this time don't fuck things up. I'm not gonna be on the losing side."

        scene scc6 # FPP. Same as scc6.
        with dissolve

        u "Uh, yeah. Okay."

        scene scc7 # TPP. Show MC and Cameron looking at eachother awkwardly. Cameron slight angry expression, MC slight confused expression.
        with dissolve

        pause 0.5

        scene scc7a # TPP. As above, but show Cameron walking away and MC following him.
        with dissolve

        pause 0.5

    scene scc8 # TPP. Show MC and Cameron walking down hallway with Adam in view walking towards the pair with knife in hand, Adam looking angry but scared.
    with fade
    pause 0.5

    stop music

    scene scc8a # TPP. As above but Adam now infront of MC and Cameron who are stood next to eachother, Cameron looking angry, MC dumbfounded.
    with dissolve
    ad "Last time you're fucking with me, pissbag."

    scene scc9 # TPP. Close up of cameron now infront of MC, very angry with mouth open, MC stood behind Cameron looking confused.
    with dissolve
    pause 0.5

    ca "What the fuck you gonna do?"

    scene scc10 # FPP. Close up of Adam looking angry/scared, Adam's hand with knife in view.
    with dissolve

    pause 0.5

    play music "music/m13punk.mp3"
    scene scc11 # TPP. Show Cameron grabbing Adam and throwing him to the ground.
    with hpunch

    pause 0.5

    scene scc12 # TPP. Adam now on the ground, Cameron crouched over him, Cameron mouth open very angry expression.
    with dissolve

    ca "You gonna stab me fucker?! Then fucking do it!"
    ca "Stab me you pussy!" with hpunch

    scene scc13 # TPP. Show Cameron grabbing the wrist of Adam's hand that holds the knife.
    with dissolve
    pause 0.5

    scene scc13a # TPP. As above but Cameron now points the knife directly into his own stomach. Cameron mouth open EXTREMELY angry.
    with dissolve

    ca "Fuckin' do it I said. Here's your shot."
    ca "I said DO IT! STAB ME YOU LITTLE BITCH!" with vpunch

    scene scc13b # TPP. As above, Adam looks extremely scared, Cameron mouth closed.
    with dissolve

    pause 0.5

    scene scc13c # TPP. As above but Cameron let's go of Adam, Cameron mouth open, less angry expression.
    with dissolve

    ca "That's what I fucking thought."

    scene scc14 # FPP. Show Adam running away down the hallway.
    with dissolve
    pause 0.5

    scene scc15 # FPP. Close up on Cameron, neutral expression, mouth closed.
    with dissolve

    u "Can't believe you just did that. Thank you."

    scene scc15a # TPP. As above, mouth open.
    with dissolve

    ca "Remember one thing. When someone comes at you like that, you show 'em who's on top."
    ca "Be fearless. That scares the shit outta them. Got it?"

    scene scc15 # FPP. Same as scc15
    with dissolve

    u "Damn, yeah."

    stop music fadeout 3
    scene scc15b # FPP. Same as scc15a but Cameron gesturing MC with his hand to come with him. Mouth open.
    with dissolve

    ca "Good. Let's get on it now. We got videos to make."


    scene scc16 # TPP. Show Cameron and stood looking at eachother in campus, MC mouth open.
    with fade

    u "Alright, what's up first?"

    play music "music/m15punk.mp3"
    queue music [ "music/m11punk.mp3", "music/m6punk.mp3" ]

    scene scc17 # FPP. Close up Cameon, with heavy dute construction glue in hand, grin on face.
    with dissolve

    u "What's that for?"

    scene scc17a # FPP. As above, mouth open.
    with dissolve

    ca "You're going to stick classroom doors shut. It will take them 20 minutes just to open one with this glue."

    scene scc17 # FPP. Same as scc17.
    with dissolve

    u "You serious? This like a high school prank."

    if apesVids > 0:
        scene scc17a # FPP. Same as scc17a.
        with dissolve

        ca "This one is an easy one. Trust me."

    else:
        scene scc17a # FPP. Same as scc17a.
        with dissolve

        ca "C'mon. Stop being a pussy man. This is an easy one."

    menu:
        "Do it":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            $ apesVids += 1

            scene scc19 # TPP. Show MC grabbing the glue from Cameron, Cameron smile, MC mouth open.
            with dissolve

            u "Okay, I'll do it. But how many doors?"

            scene scc20 # FPP. Close up Cameron, hands by side, laugh, mouth open.
            with dissolve

            ca "10. At the least."

            scene scc20a # FPP. As above, mouth closed.
            with dissolve

            u "Okay."

            scene scc21 # TPP. Show MC and Cameron walking down college hallway towards a classrom door, Cameron laughing.
            with fade

            pause 0.5

            scene scc22 # TPP. Show MC infront of classroom door, taking the cap off the glue and looking around to make sure no one is watching. Show Cameron laughing whilst recording MC on his phone.
            with dissolve

            pause 0.5

            scene scc22a # TPP. As above, MC now applying glue to door.
            with dissolve

            pause 0.5

            scene scc23 # TPP. As above, but different door.
            with dissolve

            pause 0.5

            scene scc24 # TPP. As above, but different door.
            with dissolve

            pause 0.5

        "Don't do it":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            scene scc18 # FPP. Show Cameron disappointed expression, mouth closed.
            with dissolve

            u "Nah. This is just dumb. I'm not gonna get arrested for vandalism or something stupid."

            scene scc18a # FPP. As above, shaking head, mouth open.
            with dissolve

            ca "Fine, whatever dude. We'll do something else then."

    label av_chal_2: #for compatibility only
    scene scc25a2 # TPP. Cameron and MC back on campus looking at eachother again, Cameron smile, Cameron mouth open.
    with fade

    ca "This one's gonna be a bit more fun."

    scene scc25 # FPP. Close up Cameron, smile, mouth closed.
    with dissolve

    u "Fun? Enlighten me."

    scene scc25a # FPP. As above, mouth open.
    with dissolve

    ca "Girls, topless."

    scene scc25 # FPP. Same as scc25.
    with dissolve

    u "Okay, you got me. I'm listening."

    scene scc25b # FPP. Same as scc25a but hands in shot as if he's explaining something.
    with dissolve

    ca "Here's how it's gonna go."

    scene scc26 # TPP. Show Cameron reaching into his backpack, for a container of crickets.
    with dissolve

    pause 0.5

    scene scc27 # FPP. Same as scc25 but Cameron now has container of crickets in hand and is laughing, mouth closed.
    with dissolve

    u "Bro, that's nasty."

    scene scc27a # FPP. Same as scc27, mouth open
    with dissolve

    ca "Exactly. You're gonna stand on a patio above. I'm gonna knock on the girls' door and hide. When they come out, you're gonna pour them out on top of them while I record."

    scene scc27 # FPP. Same as scc27.
    with dissolve

    u "Hahaha. And you think this will work?"

    scene scc27a # FPP. Sane as scc27a.
    with dissolve

    ca "No fuckin' idea! But if you wanna prove that you're down with the cause, you gotta do it."

    if apesVids > 0:
        ca "This one is the best of the lot. Just sayin'."

    else:
        ca "If you pussy out on this one, my respect for you is lost."

    scene scc27 # FPP. Same as scc27.
    with dissolve

    menu:
        "Do it":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            scene scc28 # TPP. Show MC and Cameron high fiving, smile on both faces, MC mouth open.
            with dissolve

            u "Fuck it. Let's do it."

            scene scc28a # TPP. As above, no longer high fiving, Cameron pointing at MC, MC mouth closed, Cameron mouth open.
            with dissolve

            ca "That's what I'm talking about!"

            scene scc29 # TPP. Show MC  standing on a patio, Cameron knocking on a door.
            with fade

            pause 0.5

            scene scc29a # TPP. As above but Cameron running away.
            with dissolve

            pause 0.5

            scene scc29b # TPP. As above, Cameron now hiding behind some bushes, two girls come out of door in skimpy pajamas.
            with dissolve

            pause 0.5

            scene scc30 # FPP. Show Cameron hiding behind the bushes gesturing MC to drop the crickets.
            with dissolve

            pause 0.5

            scene scc31 # FPP. Show the girls looking around confused below MC, MC's hands holding crickets in view.
            with dissolve

            # CRICKET DROP TIMER
            menu (fail_label="av_crickets_no_drop"):
                "Drop the crickets":
                    $ reputation.add_point(RepComponent.TROUBLEMAKER)
                    $ apesVids += 1

                    scene scc31a # FPP. As above but, show MC arms turning the container of crickets upside down with them falling out.
                    with dissolve

                    u "Here we go!"

                    if is_censored:
                        call screen censored_popup("v7_nsfwSkipLabel3")

                    scene scc32 # FPP. Show the girls screaming and removing their tops. Cameron laughing whilst filming on his phone in bushes.
                    with dissolve

                    pause 0.5

                    scene scc32a # FPP. Show the girls screaming and removing their tops. Cameron laughing whilst filming on his phone in bushes.
                    with dissolve

                    pause 0.5

                    scene scc33 # FPP. Show the girls with tops off, really angry, walking back inside.
                    with dissolve

                    pause 0.5

                    label v7_nsfwSkipLabel3:
                        scene scc34 # FPP. Show Cameron and MC back at campus, Cameron hugs MC, smile on both faces.
                        with fade

                        pause 0.5

                        scene scc25a # FPP. Same as scc25a.
                        with dissolve

                        ca "That was sick!"

                        scene scc25 # FPP. Same as scc25.
                        with dissolve

                        u "Haha, yeah. They were pretty hot. Good pick."

                        scene scc15a # FPP. Same as scc15a.
                        with dissolve

                        ca "I know where the good ones are. You ready for the next?"

                        scene scc15 # FPP. Same as scc15.
                        with dissolve

                        u "Yeah."

                "...":
                    label av_crickets_no_drop:
                        scene scc35 # FPP. Show the girls looking around confused.
                        with dissolve

                        pause 0.5

                        scene scc36 # FPP. Show Cameron still hiding behind the bushes, angry expression.
                        with dissolve

                        pause 0.5

                        scene scc37 # TPP. Show Cameron and MC back at campus stood together, Cameron angry expression.
                        with fade

                        ca "What the hell man?"

                        u "I missed my shot! I was gonna do it!"

                        ca "Yeah well, next time act faster. I don't have time for this bullshit."

        "Don't do it":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            scene scc27a # TPP. Show Cameron and MC back at campus stood together, Cameron angry expression.
            with dissolve

            ca "Man, you're such a pussy!"

            scene scc27 # TPP. Show Cameron and MC back at campus stood together, Cameron angry expression.
            with dissolve

            u "I'm not doing that, it's just cruel."

            scene scc27a # TPP. Show Cameron and MC back at campus stood together, Cameron angry expression.
            with dissolve

            ca "Whatever, let's move on."

    label cam_phone: #for compatibility only
    scene scc25b # TPP. Show Cameron and MC back at campus stood together, Cameron angry expression.
    with dissolve

    ca "This next one's gonn-"
    play sound sound.ring

    ca "Hold on."

    scene scc54 # FPP. Show Cameron stood still, Cameron answers phone and places it next to ear, Cameron mouth open. Cameron facing  to the side.
    with dissolve


    ca "Yeah... What do you mean? My little sister? Where?"
    ca "Just fuckin' tell me where dude!"
    stop sound fadeout 1
    ca "Fuck. I'm going there right now."

    scene scc54a # FPP. Same as above, Cameron no longer on phone, angry expression.
    with dissolve

    pause 0.5

    scene scc54b # FPP. Cameron now look at Camera looking angry, mouth open.
    with dissolve

    ca "We'll continue this again."

    scene scc56 # TPP. Show Cameron running away, MC chasing after him, MC mouth open.
    with dissolve

    u "Hey, hey! Where you going?"

    scene scc57 # FPP. Cameron turns around, mouth open, angry expression.
    with dissolve

    ca "None of your business."

    scene scc57a # As above, mouth closed.
    with dissolve

    u "C'mon man what happened?"

    scene scc57b # FPP. Cameron mouth open, neutral expression.
    with dissolve

    ca "Just some shit I gotta deal with."

    scene scc57c # FPP. As above, mouth closed.
    with dissolve

    u "You okay?"

    scene scc57d # FPP. Cameron turns back around, angry expression, mouth open.
    with dissolve

    ca "Yeah! I'm fine!"

    scene scc58 # TPP. Show MC grabbing Cameron's arm as he is walking away, MC mouth open.
    with dissolve

    u "Man, just tell me what happened. Maybe I can help you out."

    scene scc57 # FPP. Same as scc57.
    with dissolve

    ca "Wanna know what happened?"
    ca "My little sister has been clean for 3 months off of heroin and my buddy calls me and tells that she's off with some junkie."
    ca "A junkie she had told me she cut ties with."

    scene scc57a # FPP. Same as scc57a.
    with dissolve
    pause 0.5

    scene scc59 # TPP. Show Cameron walking away MC mouth open.
    with dissolve

    u "So, you're gonna go get her now?"

    scene scc59a # TPP. As above, MC mouth closed, Cameron turns head behind him mouth open.
    with dissolve

    ca "Of course I'm gonna go get her."

    scene scc59 # TPP. As above, Cameron mouth closed, turns his head back forward, MC mouth open.
    with dissolve

    u "Well, lemme tag along. I'll back you up."

    scene scc59a # TPP. As above, Cameron continues to walk away mouth open.
    with dissolve

    ca "Alright, fine. Who knows what will go down."
    #Getting cameron's sister:
    #Cameron and MC arrive to a run down house. Cameron begins banging on the front door. No one answers, but music and talking is heard. Cameron bangs on the door again, but again no answers.

    scene scc60 # FPP. Show Cameron banging on the door of a house, angry expression, mouth open.
    with fade

    ca "Open the fucking door! Samantha!"

    scene scc60a # FPP. As above, but Cameron is now kicking the door.
    with vpunch

    pause 0.5
    play music "music/mhorror.mp3"

    if is_censored:
        call screen censored_popup("v7_nsfwSkipLabel4")

    scene scc63 # FPP. Show Cameron's sister sat in a chair tying a belt around her arm while the girl holds a syringe in her hand.
    with Dissolve(1)

    pause 0.5

label v7_nsfwSkipLabel4:
    scene scc64 # FPP. Close up Cameron, now in the house, REALLY ANGRY, MOUTH WIDE OPEN.
    with dissolve

    ca "What the fuck?!"

    scene scc65 # FPP. Show Samantha, startled expression.
    with dissolve

    pause 0.5

    scene scc65a # FPP. As above, Samantha mouth open.
    with dissolve

    sa "Cameron?"

    scene scc64 # FPP. Same as scc64.
    with dissolve

    ca "What the fuck do you think you're doing?"

    scene scc65 # TPP. Samantha stands up and get's in Cameron's face looking really pissed off, Cameron also looking pissed off, MC stood behind Cameron.
    with dissolve
    pause 0.5
    #Samantha is slightly out of it, but still stands to get in Cameron's face.

    scene scc66 # FPP. Close up Samanatha, mouth open, angry, looking out of it.
    with dissolve

    sa "What am I doing? What the hell are you doing here?!"

    scene scc64 # FPP. Same as scc64.
    with dissolve

    ca "It's like I have to fucking babysit you 24-7!"

    scene scc66 # FPP. Same as scc66 but shoutier.
    with dissolve

    sa "I'm an adult! I can take care of myself!"

    scene scc64 # FPP. Same as scc64 but Cameron is a little less angry.
    with dissolve

    ca "You're fucking 18, Sam! You're hardly an adult! And clearly you can't take care of yourself."
    ca "What do you want me to do? Stand around while I watch you kill yourself?!"
    ca "You're my little sister for God's sake!"

    scene scc66b # FPP. Same as scc66 but Samantha turns around facing away from camera.
    with dissolve

    pause 0.5

    scene scc66c # FPP. Same as above but Samantha turns her head around towards camera, shouting.
    with dissolve

    sa "Just fuck off Cameron! Go home!"

    scene scc67 # TPP. Show Cameron grabbing Samantha's arm and she is trying to walk away. Cameron angry, mouth closed.
    with vpunch

    ca "Don't you dare talk to me like that! You're leaving. NOW!"

    scene scc68 # TPP. Show Cameron pulling Samantha towards the front door of the house trying to get her outside.
    with dissolve

    pause 0.5

    scene scc68a # TPP. As above, Cameron looks at Samantha's friends, shouts and points with his free hand, mouth open.
    with dissolve

    ca "Don't you fucking dare drag her into this shit again!"

    scene scc69 # TPP. Show Cameron pulling Samantha but now outside.
    with dissolve

    pause 0.5

    scene scc70 # TPP. Show Cameron pointing at Samantha, angry face, mouth open, Samantha looks upset and still out of it.
    with dissolve

    ca "I cannot fucking believe you Samantha."

    scene scc71 # FPP. Show Cameron walking off with phone to ear. Samantha sat on sidewalk, crying.
    with dissolve

    menu:
        "Console Samantha":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            scene scc72 # TPP. Show MC sat on the sidewalk next to Samantha, MC looking at Samantha mouth open, Samantha head in hands crying.
            with dissolve

            u "Hey, you know he only wants the best for you."

            scene scc73 # FPP. Close up Samantha, crying looking at Camera, mouth open.
            with dissolve

            sa "Yeah, well, he has a shitty way of showing it."

            scene scc73a # FPP. As above, mouth closed.
            with dissolve

            u "Yeah, maybe it's just the only way he knows to show that he cares."
            u "You know, that stuff can really kill you. He doesn't want that for his little sister."

            scene scc73 # FPP. As above, head slightly down, eyes looking at camera, mouth open.
            with dissolve

            sa "I know. I just can't help it."

            scene scc73a # FPP. As above, mouth closed.
            with dissolve

            u "It's hard, I bet. But even though I don't know you, I think you can do it."
            u "You've done it before, haven't you?"

            scene scc73 # FPP. Same as scc73.
            with dissolve

            sa "Yeah."

            scene scc73a # FPP. Same as scc73b.
            with dissolve

            u "Then you can definitely do it again. And in the end it'll all be worth it. Trust me."

            scene scc73d # FPP. Samantha looks at camera and smileS, still upset.
            with dissolve

            pause 0.5

            scene scc74 # TPP. Show Samantha hugging MC.
            with dissolve

            pause 0.5

            scene scc73e # FPP. Same as scc73d, less upset, mouth open.
            with dissolve

            sa "Thank you, really."

        "Leave her be":
            $ reputation.add_point(RepComponent.BRO)

    label av_no_sam: #for compatibility only
    if apesVids > 3:
        scene scc75 # FPP. Same camera as scc73. Show Cameron kneeling infront of Samantha but looking at Camera, slight smile, Samantha too upset but not too bad.
        with dissolve

        pause 0.5

        scene scc75a # FPP. Same as above, Cameron now looking at Samantha, mouth open.
        with dissolve

        ca "Hey, time to go."

        stop music fadeout 3

        scene scc75 # FPP. Same as above, Cameron mouth closed.
        with dissolve

        u "Okay. Bye guys."

        scene scc75a # FPP. Cameron and Samantha get up and start walking away.
        with dissolve
        pause 0.5
        #Cameron and Samantha leave.

        scene scc76 # TPP. Show MC stood up, Cameron and Samantha walking but Cameron turns his head, mouth open.
        with dissolve

        ca "Bye."

    else:
        #If you didn't do most of your tasks:
        #Cameron seems a bit irritated by this. He grabs Samantha by the arm and pulls her up.

        scene scc77 # FPP. Cameron leans down and grabs Samantha's arm and starts pulls her up. Cameron agitated expression, mouth open.
        with dissolve

        ca "Time to go."

        sa "Ugh."

        stop music fadeout 3

        scene scc78 # TPP. Show Samantha and Cameron walking away, MC stood up looking at them, mouth ope.
        with dissolve

        u "Uh, okay bye guys."

        pause 0.5

    label av_mc_dorm: #for compatibility only
    scene scc79 # TPP. Show MC in bed in dorm about to sleep but eyes open lookin at the ceiling
    with Fade(0.75, 0.25, 0.75)

    u "I should probably get some sleep."

    jump rileytext

########## SCENE 34 WOLVES CEREMONY
label wolves_ceremony:
    scene swc0 # FPP. Show Finn & Marcus standing at the entrace to the Wolves house as you are walking towards the house. Finn & Marcus chatting, Wolves house in view.
    with fade
    play music "music/muffledparty.mp3"

    pause 0.75

    if CharacterService.is_mad(imre):
        scene swc4 # FPP. Close up on Marcus, mouth open with smile.
        with dissolve

        guyc "Hey what's up?"

        u "Hey!"

        scene swc6 # TPP. Show Marcus and MC fist bumping with smile, mouth closed. Camera from the side so both in view.
        with dissolve
        #MC gives him a fist bump.

        pause 0.5

        scene swc7 # FPP. Close up on Marcus mouth open gesturing with hand to head on in.
        with dissolve

        guyc "Head on in. They're starting soon."

        scene swc8 # TPP. Show MC walking into the wolves house from behind, wolves house in view. Just like swc3 just without Imre.
        with dissolve
        #MC goes in.

        scene swc8a # TPP. Same as above but MC walking through Wolves door. Just like swc3a just without Imre.
        with dissolve

        pause 0.5

    else:
        scene swc1 # FPP. Close up on Finn, mouth open with smile, welcoming gesture with hand.
        with dissolve

        finn "What up guys? Head on in."

        scene swc2 # FPP. Close up on Imre, mouth open slight smile.
        with dissolve

        imre "For sure."

        scene swc3 # TPP. Show Imre and MC walking into Wolves house from behind, house entrance in view.
        with dissolve
        pause 0.5

        scene swc3a # TPP. Same camera as above but MC and Imre now walking through Wolves door.
        with dissolve

        pause 0.5
        #- CONTINUE at ceremonies -

    #If Imre moved out:
    #MC arrives alone to the Wolves house holding a sports bag of his stuff. A few Wolves , including marcus are outside and welcome him.

    play music "music/mparty3.mp3"
    queue music [ "music/mparty4.mp3", "music/mparty2.mp3" ]

    scene swc9 # TPP. Show as many wolves as possible, make sure Chris is stood in the middle. Upbeat expressions but serious at the same time.
    with dissolve

    pause 0.5

    scene swc10 # TPP. Show Imre, MC and Perry stood opposite the wolves, MC in the middle. SLIGHT excitable expression. Perry with SLIGHT nervous expression.
    with dissolve

    pause 0.5

    scene swc11 # FPP. Close up of Chris with 2 Wolves to his side in the background, Chris mouth open.
    with dissolve

    ch "Welcome and Congratulations to you three who have proven yourselves worthy enough for the Wolves."

    scene swc12 # FPP. Zoom out, show wolves clapping, cheering expressions. Chris is not clapping.
    with dissolve

    pause 0.5

    scene swc13 # FPP. Show Chris with 2 Wolves to his side in background. Chris mouth open slight serious expression.
    with dissolve

    ch "Today is the day you guys officially become Wolves! You guys should be very proud because this was no easy task."

    scene swc14 # TPP. Show Imre, MC and Perry, all smiling.
    with dissolve

    pause 0.5

    scene swc15 # FPP. Show Chris with 2 Wolves to hid side in background. Chris mouth, happy expression, maybe move arm and hand into view to provide some movement in the way you may move your arm when having explaining something to someone.
    with dissolve

    ch "Today you will each be given your official Wolves varsity jacket and a toast from all of us to formally welcome you into the Wolves!!!"

    scene swc16 # FPP. Show included wolves clapping and cheering. Chris not clapping but smiling with mouth closed.
    with dissolve

    pause 0.5

    scene swc13 # FPP. Show Chris with 2 wolves in background, return Chris' arm to neutral position if moved. Slight serious expression mouth open.
    with dissolve

    ch "Before I give you your jacket, I'd just like to remind you of one thing. Here, at the Wolves, we are a brotherhood. And no matter what, we look out for each other. Putting on the jacket is a symbol of your loyalty."

    scene swc18 # FPP. Show everyone in scene clapping, variety of positive expressions.
    with dissolve

    if len(wolvesTasks) == 4: # MC, Imre, Perry
        ch "First up... [name]!"

        scene swc19 # TPP. Show everone clapping/cheering. Show MC walking towards Chris who has Wolves jacket in hand, camera from behind MC looking at Wolves.
        with dissolve

        pause 0.5

        scene swc19a # TPP. As above but MC is now infront of Chris with Wolves jacket on, no longer cheering/clapping.
        with dissolve

        u "Thanks man."

        scene swc19b # TPP. As above but Chris has hand on MC shoulder, Chris smiling.
        with dissolve

        pause 0.5

        scene swc11 # FPP. Close up on Chris with 2 Wolves to his side in the background. Chris mouth open neutral expression.
        with dissolve

        ch "That's all you. Now [name] out of everyone proved he is most qualified to be a Wolf. He proved his loyalty, his determination, but overall, he proved himself over everyone else."
        ch "I think we should be expecting a lot from [name] this year."

        scene swc21 # TPP. Show MC with smile walking back towards line, same camera as swc19, Wolves clapping.
        with dissolve

        pause 0.5

        scene swc15 # FPP. Show Chris with 2 wolves to his side in the background. Chris mouth open, smile.
        with dissolve

        ch "Next up of course is... Imre!"

        scene swc23 # FPP. Show Imre walking towards Chris, Wolves clapping/cheering. Chris has Wolves jacket in hand.
        with dissolve

        pause 0.5

        scene swc23a # FPP. As above but show Imre infront of Chris with Wolves jacket on. Chris mouth open, wolves no longer clapping.
        with dissolve

        ch "Imre came in second in the initiation and proved himself to be Wolves material. Haha which we all know was a given because his brother is a Wolves legend. But anyway, welcome to the Wolves!"

        scene swc23b # FPP. As above but show Imre walking back towards the line with smug expression, everyone clapping/cheering again.
        with dissolve

        pause 0.5

        scene swc11 # FPP. Close up Chris with 2 wolves to his side in background. Chris mouth open.
        with dissolve

        ch "Last but not least of course we've got Perry!"

        scene swc25 # FPP. Show Perry walking with haste towards Chris who has Wolves jacket in hand. Chris smiling all other Wolves clapping/cheering.
        with dissolve

        pause 0.5

        scene swc25a # FPP. As above but Perry now infront of Chris wearing wolves Jacket. Wolves no longer clapping/cheering. Chris mouth open.
        with dissolve

        ch "Perry has been training hard for this next fight season, so we are very glad to have him on board. Good job man."

        scene swc25b # FPP. As above but show Perry walking back to line with big smile and doing a fist pump. everyone clapping/cheering.
        with dissolve

        pause 0.5

        scene swc26 # TPP. Show everyone drinking.
        with dissolve

        pause 0.5

        scene swc27 # TPP. Show everyone clapping, happy expressions.
        with dissolve

    elif len(wolvesTasks) == 3: # Imre, MC, Perry
        scene swc11 # FPP. Close up Chris with 2 wolves to his side in background. Chris mouth open.
        with dissolve

        ch "First up... Imre!"

        scene swc23 # FPP. Show Imre walking towards Chris, Wolves clapping/cheering. Chris has Wolves jacket in hand.
        with dissolve

        pause 0.5

        scene swc23a # FPP. As above but show Imre infront of Chris with Wolves jacket on. Chris mouth open, wolves no longer clapping.
        with dissolve

        pause 0.5

        scene swc15 # FPP. Show Chris with 2 wolves to his side in the background. Chris mouth open, smile.
        with dissolve

        ch "Imre, this was much expected from you, no offense to anyone! But if you didn't already know that Imre's brother is a double time legend here at the Wolves, then it is no surprise that Imre came in first in the challenges."

        scene swc31 # FPP. Same camera as swc22, Chris with hand on Imre's shoulder, Chris smiling mouth open.
        with dissolve

        ch "Welcome to the Wolves man."

        scene swc32 # FPP. Side Camera of Imre & Wolves, Imre mouth open.
        with dissolve

        imre "Thanks!"

        scene swc23b # FPP. Show Imre walking back to line with smile, everyone clapping/cheering.
        with dissolve

        pause 0.5

        scene swc11 # FPP. Close up Chris with 2 wolves to his side in background. Chris mouth open.
        with dissolve

        ch "We expect a lot out of you this year Imre... Next up... [name]!"

        scene swc19 # TPP. Show everone clapping/cheering. Show MC walking towards Chris who has Wolves jacket in hand, camera from behind MC looking at Wolves.
        with dissolve

        pause 0.5

        scene swc19a # TPP. As above but MC is now infront of Chris with Wolves jacket on, no longer cheering/clapping. Chris mouth open.
        with dissolve

        ch "[name] placed second during the initiation challenges. He also has a lot of potential here at the Wolves. We're looking forward to having you."

        scene swc36 # TPP. MC now wearing Wolves jacket fist bumping Chris, smiles on both faces. MC mouth open.
        with dissolve

        u "Thank you."

        scene swc21 # TPP. Show MC with smile walking back towards line, same camera as swc19, Wolves clapping.
        with dissolve

        pause 0.5

        scene swc11 # FPP. Close up Chris with 2 wolves to his side in background. Chris mouth open.
        with dissolve

        ch "And last, but not least... Perry. Come on up here man."

        scene swc25 # FPP. Show Perry walking with haste towards Chris who has Wolves jacket in hand. Chris smiling all other Wolves clapping/cheering.
        with dissolve

        pause 0.5

        scene swc25a # FPP. As above but Perry now infront of Chris wearing wolves Jacket. Wolves no longer clapping/cheering. Chris mouth open.
        with dissolve

        ch "Perry has been training almost everyday to start fighting."

        scene swc40 # FPP. Show Perry & Wolves, Perry mouth open excitable expression.
        with dissolve

        guyd "Fuck yeah I have!"

        scene swc25a # FPP. Same camera as swc25, Chris mouth open.
        with dissolve

        ch "And who knows, maybe Perry will be our Wolves legend this year! But one thing I do know, is you really earned your spot here. Looking forward to watch you in the ring."

        scene swc42 # FPP. Show Perry & Wolves, Perry mouth open smile.
        with dissolve

        guyd "Won't let you guys down!"

        scene swc26 # FPP. Same camera as swc25, show Perry walking back to line with excitable expression. Everyone clapping/cheering.
        with dissolve

        pause 0.5

        scene swc26 # TPP. Show everyone drinking beers.
        with dissolve

        pause 0.5

        scene swc27 # TPP. As above, but no longer drinking, smiling/laughing instead.
        with dissolve

    else: # Imre, Perry, MC
        scene swc15 # FPP. Show Chris with 2 wolves to his side in the background. Chris mouth open, smile.
        with dissolve

        ch "First up... Imre!"

        scene swc23 # FPP. Show Imre walking towards Chris, Wolves clapping/cheering. Chris has Wolves jacket in hand.
        with dissolve

        pause 0.5

        scene swc23a # FPP. As above but show Imre infront of Chris with Wolves jacket on. Chris mouth open, wolves no longer clapping.
        with dissolve

        ch "Now this was no surprise. If you guys already didn't know, Imre's brother here is a two time Wolves champion!"

        scene swc23c # FPP. As above but Wolves cheering.
        with dissolve

        pause 0.5

        scene swc23a # FPP. As above but Wolves no longer cheering, Chris mouth open smile.
        with dissolve

        ch "So we all knew you'd be here Imre. Congratulations. Welcome to the Wolves man."

        scene swc31 # FPP. As above, Chris mouth closed, hand on Imre's shoulder.
        with dissolve

        pause 0.5

        scene swc32 # FPP. Side Camera of Imre & Wolves, Imre mouth open.
        with dissolve

        imre "Thanks man."

        scene swc48 # FPP. Imre walking back towards line, Imre doing fist pump with smile, Wolves cheering/clapping.
        with dissolve

        pause 0.5

        scene swc11 # FPP. Close up Chris with 2 Wolves to his side in background. Chris mouth open.
        with dissolve

        ch "Second... Perry who put up a tough fight in the challenges."

        scene swc25 # FPP. Show Perry running towards Chris who has Wolves jacket in hand, Chris smiling, wolves cheering/clapping.
        with dissolve

        pause 0.5

        scene swc25a  # FPP. As above but Perry now infront of Chris wearing wolves Jacket. Wolves no longer clapping/cheering. Chris mouth open.
        with dissolve

        ch "Perry placed second in the challenges. And we're really glad you made it, but honestly I really knew you had what it took."
        ch "Perry here has already been training everyday to fight this year! We're looking forward to having him in the ring this year."

        scene swc42 # FPP. Show Perry & Wolves, Perry mouth open smile.
        with dissolve

        guyd "Thank you! Thank you!"

        scene swc11 # FPP. Show Chris with 2 wolves to his side in the background. Chris mouth open, smile.
        with dissolve

        ch "And last, but definitely not least, [name]."

        scene swc19 # TPP. Show everone clapping/cheering. Show MC walking towards Chris who has Wolves jacket in hand, camera from behind MC looking at Wolves.
        with dissolve

        pause 0.5

        scene swc19a # As above but MC is now infront of Chris with Wolves jacket on, no longer cheering/clapping. Chris mouth open.
        with dissolve

        ch "[name] may have placed last in the challenges, but it does not make him any less worthy to be here. He has proven his loyalty and dedication to the Wolves and has potential to do great here. Congrats man."

        scene swc36 # TPP. MC now wearing Wolves jacket fist bumping Chris, smiles on both faces. MC mouth open.
        with dissolve

        u "Thanks bro."

        scene swc21 # TPP. Show MC with smile walking back towards line, same camera as swc19, Wolves clapping.
        with dissolve

        pause 0.5

        scene swc26 # TPP. Show everyone with beers in their hands. Cheersing eachother.
        with dissolve

        pause 0.5

        scene swc27 # TPP. As above, but show everyone chugging beers.
        with dissolve

    scene swc58 # FPP. Show Sebastian approaching MC.
    with dissolve

    label wolves_ceremony_2:

    if len(wolvesTasks) == 4:
        scene swc59 # FPP. Close up Sebastian, mouth open smile.
        with dissolve

        se "Hey, it's the big winner of the night. How does it feel?"

        scene swc59a # FPP. As above, mouth closed.
        with dissolve

        u "Ehh, it's cool. We all did good. You know?"

        scene swc59b # FPP. As above, mouth open smile. Head moved.
        with dissolve

        se "Yeah, but still, you came in as top dog."

        scene swc59a # FPP. As above, mouth closed smile.
        with dissolve

        u "Yeah, well, I'm looking forward to this first year."

        scene swc59d # FPP. As above mouth open.
        with dissolve

        se "You ready to fight this year?"

        scene swc59a # FPP. As above, mouth closed.
        with dissolve

        u "Yeah, maybe."

        scene swc59b # FPP. As above, mouth open smile.
        with dissolve

        se "You need any pointers let me know, but I'm sure you won't need it."

        scene swc59a # FPP. As above, mouth closed smile.
        with dissolve

        u "Haha what's that supposed to mean?"

        scene swc59e # FPP. As above mouth open laughing.
        with dissolve

        se "You know.. top dog! Ahaha."

        scene swc59f # FPP. As above mouth closed laughing.
        with dissolve

        u "Haha yeah."

        scene swc59 # FPP. As above, mouth open, welcoming smile.
        with dissolve

        se "But hey, welcome."

        scene swc60 # FPP. Show Sebastian walking away.
        with dissolve

    else:
        scene swc59d # FPP. Close up Sebastian, mouth open.
        with dissolve

        se "Hey, welcome in."

        scene swc59a # FPP. As above, mouth closed.
        with dissolve

        u "Yeah thanks."

        scene swc62 # TPP. Show Sebastian placing hand on MC's shoulder, MC unsure expression, Sebastian caring expression.
        with dissolve

        pause 0.5

        scene swc59d # FPP. Close up Sebastian, mouth open.
        with dissolve

        se "And don't feel so down. Not getting first isn't everything. I didn't get first either."

        scene swc59a # FPP. As above, mouth closed.
        with dissolve

        u "Oh, I wasn't-"

        scene swc59e # FPP. As above, mouth open, laughing.
        with dissolve

        se "Yeah some of the problem solving stuff not my thing, but I'm strong. Haha. Am I right?"

        scene swc59f # FPP. As above, mouth closed, laughing.
        with dissolve

        u "Uh sure."

        scene swc59d # FPP. As above, mouth open, neutral expression.
        with dissolve

        se "So you getting in the ring this year?"

        scene swc59a # FPP. As above mouth closed.
        with dissolve

        u "Yeah, we'll see."

        scene swc59e # FPP. As above, mouth open, slight grin.
        with dissolve

        se "Don't worry my guy. I got you. I'll show you some tricks."

        scene swc59f # FPP. As above, mouth closed, laugh.
        with dissolve

        u "Oh, thanks."

        scene swc59 # FPP. As above, mouth open, neutral expression.
        with dissolve

        se "No worries. Come find me if you need anything."

        scene swc59a # FPP. As above, mouth closed, slight smile.
        with dissolve

        u "Thanks."

        scene swc60 # TPP. Show Sebastian walking away from MC.
        with dissolve

    scene swc65 # TPP. Show MC walking towards Finn.
    with dissolve

    if len(wolvesTasks) >= 3:
        scene swc66 # FPP. Close up Finn, mouth open.
        with dissolve

        finn "Oh uh hey [name]. What's up?"

        scene swc66a # FPP. As above, mouth closed.
        with dissolve

        u "Just wanna say hi. You know, now that I'm in just wanna get acquainted with everyone."

        scene swc66 # FPP. As above, mouth open.
        with dissolve

        finn "Yeah, that's cool."

        scene swc66a # FPP. As above, mouth closed.
        with dissolve

        u "So how were your challenges when you did this thing? Cus man mine were rough haha."

        scene swc66 # FPP. As above, mouth open, smile.
        with dissolve

        finn "Uhh yeah, mine were good. Can't complain. I came in second. Stuck to the books. But you know, Chris had a lot of good to say about me."

        scene swc66e # FPP. As above, mouth closed, proud expression.
        with dissolve

        u "Yeah, yeah. Makes sense. Good job. You close with Chris?"

        scene swc66f # FPP. As above, mouth open, proud expression.
        with dissolve

        finn "Oh, yeah totally. Chris is my bro. He needs something, I'm always his first guy."

        scene swc66a # FPP. As above, mouth closed, smile.
        with dissolve

        u "Oh okay. Well that's good to know."

        scene swc66 # FPP. As above, mouth open.
        with dissolve

        finn "Yeah, well catch you around."

        scene swc66a # FPP. As above, mouth closed.
        with dissolve

        u "Yeah."

        scene swc67 # TPP. Show MC walking away from Finn.
        with dissolve

    else:
        scene swc66 # FPP. Close up Finn, mouth open, smile.
        with dissolve

        finn "Oh, hey. What's up? You're a Wolf now."

        scene swc66a # FPP. As above, mouth closed, smile.
        with dissolve

        u "Yeah just glad to have made it in. Hardly made the cut."

        scene swc66 # FPP. As above, mouth open, welcoming smile.
        with dissolve

        finn "Oh don't worry about that. You're here now! Coming in last isn't so bad anyway."

        scene swc66a # FPP. As above, mouth closed, smile.
        with dissolve

        u "Did you place last in yours?"

        scene swc66 # FPP. As above, mouth open.
        with dissolve

        finn "Me? No I got second. But even though I didn't place first, Chris still had a lot of good to say about me."

        scene swc66a # FPP. As above, mouth closed.
        with dissolve

        u "Yeah that's cool. You guys are tight then?"

        scene swc68f # FPP. As above, mouth open, slight smug expression.
        with dissolve

        finn "Yeah, whenever Chris needs something, I'm always his first guy to call."

        scene swc68g # FPP. As above, mouth closed, slight smug expression.
        with dissolve

        u "That's cool."

        scene swc66 # FPP. As above, mouth open.
        with dissolve

        finn "I'm just dependable you know. That's all. I like to play by the rules."

        scene swc66a # FPP. As above, mouth closed.
        with dissolve

        u "Yeah... I get it. Well, nice talking to you. See you around."

        scene swc66 # FPP. As above, mouth open.
        with dissolve

        finn "Bye."

        scene swc67 # TPP. Show MC walking away from Finn.
        with dissolve

    scene swc70 # FPP. Close up Chris, mouth open, smile.
    with dissolve

    ch "Let me show you to your room."

    scene swc70a # FPP. As above, mouth closed.
    with dissolve

    u "Okay."

    scene swc71 # TPP. Show MC following Chris down a hallway, Chris infront of a bedroom door with hand on handle, about to open it.
    with dissolve

    pause 0.5

    scene swc72 # FPP. Show Chris in room mouth open, smile.
    with dissolve

    ch "Here's your room. You can unpack and get settled."

    scene swc72a # FPP. As above, mouth closed.
    with dissolve

    u "Thanks."

    scene swc72 # FPP. As above, mouth open, smile.
    with dissolve

    ch "No problem. Come get me if you need anything."

    scene swc72a # FPP. As above, mouth closed, smile.
    with dissolve

    u "Will do."

    scene swc73 # FPP. Show Chris leaving MC room.
    with dissolve

    pause 0.5

    scene swc74 # TPP. Show MC in room, looking around, big smile.
    with dissolve

    u "Man, I can't believe it. Joined the Wolves. Moved in here. This is gonna be dope as fuck! I gotta get on my fight training too."

    scene swc75 # FPP. Show Perry into door threshold of MC room.
    with dissolve

    pause 0.5

    scene swc76 # FPP. Show Perry mouth open, out of breath from running.
    with dissolve

    guyd "Oh hey! You're in here."

    scene swc76a # FPP. As above, mouth closed.
    with dissolve

    u "Yeah, what's up?"

    scene swc76b # FPP. As above, mouth open smile.
    with dissolve

    guyd "We're gonna play charades. 3 versus 3. Old Wolves vs New Wolves. We'll need you on the team."

    scene swc76a # FPP. As above, mouth closed, neutral expression.
    with dissolve

    u "Alright, cool."

    scene swc77 # TPP. Show Perry and MC leaving room.
    with dissolve

    pause 0.5

    scene swc79 # TPP. Show everyone sat together in Wolves main room, beers in hands, laughing epxression.
    with fade

    pause 0.5

    scene swc80 # TPP. Show MC leaving Wolves main room to check on Imre who is outside. || Added this to make the transition from inside to outside smoother, remove if needed.
    with dissolve

    u "I'm just gonna go and find Imre."
    play music "music/muffledparty.mp3"

    scene swc81 # FPP. Distant shot of Imre who is looking around outside embracing the fresh air. Camera should show the back of Imre.
    with fade

    u "Hey, what're you doing out here?"

    scene swc82 # FPP. As above but slightly closer shot, Imre now looking in a place different from FPP. If jaw visible in shot, open Imre mouth.
    with dissolve

    imre "Getting some air."

    scene swc83 # FPP. As above, but closer shot, Imre looking elsewhere again, mouth closed.
    with dissolve

    u "You good?"

    scene swc84 # FPP. Close up Imre, Imre now facing camera, smile mouth open.
    with dissolve

    imre "I'm great man. I have a good feeling about this year."

    scene swc84a # FPP. As above, mouth closed, slight smile.
    with dissolve

    u "Yeah it's gonna be amazing. We're Wolves now!"

    scene swc84 # FPP. As above, mouth open, slight smile.
    with dissolve

    imre "Feels like I've been waiting for this moment since my brother was in the Wolves."

    scene swc84a # FPP. As above, mouth closed, slight smile.
    with dissolve

    u "And you made it!"

    scene swc85 # TPP. Show Imre and MC high fiving, Imre mouth open, ecstatic expressions on MC and Imre.
    with dissolve

    imre "Man, we made it! Haha."

    scene swc85a # TPP. Show Imre and MC stood looking at eachother, smiles on both, MC mouth open.
    with dissolve

    u "Haha yeah, but really this year is gonna be dope as fuck."

    scene swc84 # FPP. Close up Imre, mouth open.
    with dissolve

    imre "Remember meeting the first day?"

    scene swc84a # FPP. As above, mouth closed.
    with dissolve

    u "Yeah I mean I knew college was gonna be dope, but I didn't even think about joining a frat."

    scene swc84 # FPP. As above, mouth open, laugh.
    with dissolve

    imre "I didn't see you one joining one either. Haha."

    scene swc84a # FPP. As above, mouth closed, grin.
    with dissolve

    u "Ay what's that supposed to mean?"

    scene swc84b # FPP. As above, mouth open, serious expression.
    with dissolve

    imre "Just that you know, you were a bit of a-"

    scene swc100 # TPP. Close up MC, confused expression.
    with dissolve

    u "A what?"

    scene swc86 # FPP. Close up Imre, mouth open, laughing.
    with dissolve

    imre "I'm fuckin with you! Haha."

    scene swc86a # FPP. As above, mouth closed, laughing.
    with dissolve

    u "You always fuckin with me."

    scene swc87 # TPP. Show MC playfully pushing Imre both laughing.
    with dissolve

    pause 0.5

    scene swc86 # FPP. Close up Imre, mouth open, smile.
    with dissolve

    imre "That's what I'm here for."

    scene swc86a # FPP. As above, mouth closed, slight smile.
    with dissolve

    u "Alright, I'm gonna head in. Try to actually get some sleep."

    scene swc86 # FPP. As above, mouth open, neutral expression.
    with dissolve

    imre "Okay. Goodnight."

    scene swc86a # FPP. As above, mouth closed, neutral expression.
    with dissolve

    u "Night."

    scene swc89 # TPP. Show MC walking away from Imre back into Wolves house.
    with dissolve
    stop music fadeout 1
    pause 0.5

    scene swc90 # TPP. Show MC in bed wolves house about to sleep but eyes open lookin at the ceiling
    with fade

    u "I should probably get some sleep."

############# RILEY TEXT

label rileytext:
    if Moods.TEASED in riley.mood:
        play sound sound.vibrate

        $ v7_msgReply5 = MessageBuilder(riley)
        $ v7_msgReply5.set_variable("rileysex", True)
        $ v7_msgReply5.new_message(_("Yayyy"))

        $ v7_msgReply6 = MessageBuilder(riley)
        $ v7_msgReply6.new_message(_("Oh oki"))

        $ MessengerService.new_message(riley _("Wanna come over? ;)"))
        $ MessengerService.add_replies(riley,
            Reply(_("Sure, on my way :)"), v7_msgReply5),
            Reply(_("Sorry I'm really exhausted. Another time"), v7_msgReply6)
        )

        while MessengerService.has_replies(riley):
            call screen phone
            if MessengerService.has_replies(riley):
                u "(I should check my messages.)"

    if rileysex:
        u "(Guess I'm not going to sleep yet.)"
        jump rileysexscene

    if joinwolves:
        scene swc91 # TPP. Show MC in bed going to sleep
        with dissolve

        jump scene35

    else:
        scene swc96 # TPP. Show MC in bed going to sleep
        with dissolve

        jump scene35a

########## BEFORE SCENE 35: RILEY SEX SCENE
#### RIley Sex Scene, if riley rs = True, you get a message in your dorm from Riley telling you that her roommate isnt home and if you wanna come over. Since you already did stuff, you say yes.
# It's thurday night
label rileysexscene:
    $ CharacterService.set_relationship(riley, Relationship.FWB, mc)
    $ sceneList.add("v7_riley")

    if joinwolves:
        stop music fadeout 3
        scene preri1 # You walking through the night to riley
        with fade

    else:
        stop music fadeout 3
        scene preri2 # You walking through the dorms
        with fade

    pause 0.75

    scene ridrm1 # You knocking on Riley's dorm door (third person)
    with dissolve

    pause 0.75

    scene ridrm2 # Riley opens the door, grin expression (first person)
    with dissolve
    ri "Hey!"

    scene ridrm2a
    with dissolve

    u "Hey Ril-" # MC words cut off by Riley suddenly grabbing hand, not too sure on this tho

    scene ridrm2b
    with vpunch
    play music "music/msexy.mp3"

    pause 0.5

    scene ridrm3 # Riley reaches and grabs your hand pulls you into her dorm, flirty wink (first person)
    with dissolve
    ri "Come on!"

    if is_censored:
        call screen censored_popup("v7_nsfwSkipLabel1")

    scene ridrm4 # Riley close up in her dorm, talking mouth open, single slightly raise brow (first person)
    with dissolve
    ri "I think we have some unfinished business."

    scene ridrm4a
    with dissolve
    u "What do you mean, \"unfinished business\"?"

    scene ridrm4 # Same as above but mouth closed now (first person)#
    with dissolve
    ri "Let me show you what I mean."

    scene ridrm4a # Same as above but mouth closed now (first person)#
    with dissolve
    u "I like that sound of that."

# Riley sex scene
    label risex: #for compatibility only
    show screen rileysexoverlay

    scene risex1a # Riley shirt fully off, flirty grin (first person)
    with fade
    u "Oh wow!"

    scene risex1b # As above but mouth open (first person)
    with dissolve
    ri "What are you waiting for?"

    scene risexvid1 # making out with riley
    with dissolve

    " "

    scene risex2 # MC throwing riley on the bed
    with dissolve

    pause 0.5

    scene risex2a # Riley on the bed laughing  while you take your shirt off
    with dissolve
    ri "*Laughs* Uhhh, I like this side of you."

    scene risex2b # shirt off
    with dissolve

    pause 0.5

    scene risex3 # close to riley
    with dissolve

    pause 0.5

    scene risex4
    with dissolve

    ri "Let's get these off."

    scene risex4a
    with dissolve

    ri "*Giggles*"

    scene risex5
    with dissolve

    pause 0.5
    label riblowjob:

    scene risexvid2s # Riley giving MC a blowjob whilst mc is stood up, MC pleasure expression
    with dissolve
    u "Wow you're so good at this."
    u "Fuck Riley, that feels amazing."
    " "

    scene risexvid2f # Riley giving MC a blowjob whilst mc is stood up, MC pleasure expression
    with dissolve
    u "Mhhh..."
    u "Holy shit..."
    " "

    scene risex6 # MC grabbing Riley standing her up
    with dissolve

    ri "I wanna make you cum."

    scene risex6a # MC grabbing Riley standing her up
    with dissolve

    u "No way, it's my turn."

    scene risex7 # MC grabbing Riley standing her up
    with dissolve

    ri "*Chuckles* What are you doing?"

    scene risex8 # MC grabbing Riley standing her up
    with dissolve

    u "Getting rid of things that shouldn't be there."

    scene risex8a # MC grabbing Riley standing her up
    with dissolve

    pause 0.5

    scene risex8b
    with dissolve

    pause 0.5

label rifingering:
    scene risexvid3s
    with dissolve
    ri "*Moans* Mhmmmm..."
    " "

    scene risexvid3f # Riley cowgirl on MC, Riley pleasure expression
    with dissolve
    ri "Oh my god [name], you're amazing."
    ri "Please! Fuck me!"

    scene risexvid6s # Riley cowgirl on MC, Riley pleasure expression
    with fade
    ri "*Moans* Ahhhh yes!"
    " "

label rimissionary:
    scene risexvid7 # Riley cowgirl on MC, Riley pleasure expression
    with dissolve
    ri "*Moans louder* Holy shit!"
    " "

    scene risexvid6f # Riley cowgirl on MC, Riley pleasure expression
    with dissolve
    ri "*Moans very loud* Oh my god!"

    u "I'm gonna cum!"

    ri "Yesss! Me too!"

label riclimax:
    scene risexvid8 # Riley cowgirl on MC, Riley pleasure expression
    with dissolve

    pause 0.5

    scene rivid8061
    with flash

    u "Fuuuck!"

    hide screen rileysexoverlay
    $ renpy.end_replay()

    scene risex15 # As above but mouth closed
    with fade
    stop music fadeout 3

    ri "This was amazing."
    ri "I wish you could stay, but I think my roommate will be home soon."

    scene risex15a # Riley walking away to get cleaned up MC getting dressed again
    with dissolve
    u "Sure, it's late now anyway and I'm pretty tired, haha."

    scene risex15 # As above but Riley turns to look at MC and laugh and MC is now dressed again
    with dissolve
    ri "I'll see you tomorrow [name]."

label v7_nsfwSkipLabel1:
    scene risex15a # MC leaving Riley's dorm
    with dissolve
    u "Yeah, see you tomorrow."

    if joinwolves:
        scene preri1a # You walking through the night back home
        with fade

        pause 0.5

    else:
        scene preri2a # You walking through the dorms back home
        with fade

        pause 0.5

########## SCENE 35 MC AT DORM / WOLVES ROOM AT NIGHT

    if joinwolves: # IN WOLVES ROOM
        scene swc91 # TPP. Show MC in bed going to sleep
        with fade

        label scene35:
            pause 0.5

            #- CONTINUE at Friday Morning -
            scene swc92 # TPP. Show MC in bed, waking up, camera from corner of room.
            with Fade(2,0,2)
            play music "music/mindie1.mp3"

            queue music [ "music/mindie2.mp3", "music/mindie3.mp3", "music/mindie5.mp3" ]

            pause 0.5

            scene swc93 # TPP. MC waking up, sat on the edge of his bed, looking tired.
            with dissolve

            pause 0.5

            if signs:
                jump signs_with_autumn

            else:
                scene swc95 # TPP. Show MC stood up, yawning, getting ready.
                with dissolve

                u "Not much to do right now, I suppose I can study for a bit."

                scene sas17 # TPP. Show MC working at his desk in wolves room
                with fade

                u "(Shit, I need a book from the library.)"

                pause 0.5

                jump walking_through_hallways

    else: # in DORM
        scene swc96 # TPP. Show MC in bed going to sleep
        with fade

        label scene35a:
            pause 0.5

            #- CONTINUE at Friday Morning -
            scene swc97 # TPP. Show MC in bed, waking up, camera from corner of room.
            with Fade(2,0,2)
            play music "music/mindie1.mp3"

            queue music [ "music/mindie2.mp3", "music/mindie3.mp3", "music/mindie5.mp3"]

            pause 0.5

            scene swc98 # TPP. MC waking up, sat on the edge of his bed, looking tired.
            with dissolve

            pause 0.5

            if signs:
                jump signs_with_autumn

            else:
                scene swc99 # TPP. Show MC stood up, yawning, getting ready.
                with dissolve

                u "Not much to do right now, I suppose I can study for a bit."

                scene swc100 # TPP. Show MC working at his desk
                with fade

                pause 0.5

                scene swc101
                with dissolve

                u "(Shit, I need a book from the library.)"

                pause 0.5

                jump walking_through_hallways

########## SCENE 36 MAKING SIGNS W/ AUTUMN
label signs_with_autumn:
    $ MessengerService.new_message(autumn, _("Hey, it's Autumn."))
    $ MessengerService.new_message(autumn, _("I'm just about to start making signs. Do you still want to join?"))
    $ MessengerService.add_reply(autumn, _("Yes, of course. I'd love to."))
    $ MessengerService.new_message(autumn, _("Great. I'm at the Deer's House. Do you know how to get there?"))
    $ MessengerService.add_reply(autumn, _("Yeah, I think I do. On my way."))
    $ MessengerService.new_message(autumn, _("Alright, see you soon."))

    play sound sound.vibrate

    while MessengerService.has_replies(autumn):
        call screen phone
        if MessengerService.has_replies(autumn):
            u "(I should probably check my messages.)"

    u "(Alright, let's get going to Autumn's.)"
    
    u "(I should probably get going right away.)"
    stop music fadeout 3
    scene sas2 # TPP. Show MC knocking on the door of the Deer's house.
    with fade
    play sound sound.knock

    pause 1.5

    play sound "sounds/dooropen.mp3"

    scene sas3 # FPP. Close up on Autumn who is now stood at the door, smile, mouth open.
    with dissolve

    aut "Hey. Thanks for coming to help. Come on in."

    scene sas4 # TPP. Show MC following Autumn into the deers house.
    with dissolve

    pause 0.5

    scene sas5 # TPP. Show Autumn and MC, Autumn pointing at markers and paint on the floor, mouth open. They are alone.
    with dissolve

    aut "Markers and Paint right here. So pick your fancy."

    scene sas5a # TPP. As above, Autumn mouth closed, with smile.
    with dissolve

    u "Thanks."

    scene sas6 # TPP. Show Autumn and MC on sat on the floor. Markers in hands, Autumn immediately begins writing something on her sign. MC looking at Autumn sign.
    with dissolve

    pause 0.5

    scene sas7 # FPP. Close up Autumn, mouth open, neutral expression.
    with dissolve

    aut "Need help?"

    scene sas7a # FPP. As above, mouth closed.
    with dissolve

    u "Haha yeah, maybe just struggling for some inspo."

    scene sas7b # FPP. As above but Autumn now showing her sign to camera, the sign reads "The Future is Female". Mouth closed.
    with dissolve

    u "Future is Female. That's dope."

    scene sas7c # FPP. As above but mouth closed.
    with dissolve

    aut "I appreciate the witty stuff, but I like to be direct. Feels like it gets right to the point. The more we fight, the more progress we will make."

    scene sas7a2 # FPP. Same sas7a, Autumn no longer holding sign.
    with dissolve

    u "Yeah, I feel you. Think I'm onto something."

    scene sas7d # FPP. As above, smile, mouth open.
    with dissolve

    aut "Let me hear it."

    scene sas7e # FPP. As above, mouth closed.
    with dissolve

    menu:
        "Say something witty":

            u "Girls just want to have FUNdamental rights."

            scene sas8 # TPP. Show MC and Autumn sat down, MC mouth opening gesturing with his hands as if to explain something.
            with dissolve

            u "You know Fun! Fundamental!"

            scene sas9 # FPP. Close up Autumn, mouth open laughing.
            with dissolve

            aut "Ohhhhh hahaha! That's a take on that Cyndi Lauper song."

            scene sas9a # FPP. As above, mouth closed.
            with dissolve

            u "Exactly!"

            scene sas9b # FPP. As above, grin, mouth open.
            with dissolve

            aut "Clever, very clever! Love it."

            scene sas9c # FPP. As above, mouth closed.
            with dissolve

            u "Thanks."

        "Same something direct":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            u "Men against misogyny."

            scene sas7f # FPP. As above but big smile, mouth open.
            with dissolve

            aut "I like that! It's direct and it also has a nice ring to it. It's amazing how misogynistic most guys are in college these days. Refreshing to know you stand with women."

            scene sas7e # FPP. Same as sas73e.
            with dissolve

            u "Yeah. It's an issue for sure."

    scene sas9d # FPP. As above, slight smile, open mouth.
    with dissolve

    aut "Really glad you're doing this. What motivated you?"

    scene sas9e # FPP. As above, mouth closed.
    with dissolve

    u "Like I said, I really think women deserve equal rights. I just really feel for them. It's not fair."

    scene sas9f # FPP. As above, empathetic expression, mouth open.
    with dissolve

    aut "Your empathy is admirable."

    scene sas9e # FPP. Same as sas9e.
    with dissolve

    u "My mom taught me everything I know."

    scene sas9d # FPP. Same as sas9d.
    with dissolve

    aut "Sounds like she is a perspicacious woman."

    scene sas9e # FPP. Same as sas9e.
    with dissolve

    u "She is. Smart and strong for sure."

    scene sas9f # FPP. Same as sas9f.
    with dissolve

    aut "That's kind of you."

    scene sas9e # FPP. Same as sas9e.
    with dissolve

    u "But yeah, that's why I do it. Stand up for those who deserve it."

    scene sas9g # FPP. As above, caring expression, mouth open.
    with dissolve

    aut "You're definitely headstrong. Good to see a guy with that kind of mentality."

    scene sas9e # FPP. Same as sas9e.
    with dissolve

    u "Yeah, I get what you mean."

    scene sas9b # FPP. Same as sas9b.
    with dissolve

    aut "This movement definitely needs more men. Actually, I take that back. Haha. More men just need to realize their given privileges and stop being in denial."

    scene sas9c # FPP. Same as sas9c.
    with dissolve

    u "Yeah, well one step at a time. But we can't blame these guys, they're just uneducated."

    scene sas7 # FPP. Same as sas7.
    with dissolve

    aut "I mean we are in university to learn aren't we?"

    scene sas7a # FPP. Same as sas7a.
    with dissolve

    u "Haha yeah but you know how guys are."

    scene sas9h # FPP. As above, curious expression, mouth open.
    with dissolve

    aut "Educate me."

    scene sas9i # FPP. As above, mouth closed.
    with dissolve

    u "Haha what?"

    scene sas7d # FPP. Same as sas7d.
    with dissolve

    aut "I'm serious! I'd really like to learn more about the male mind."

    scene sas7e # FPP. Same as sas7e.
    with dissolve

    u "Well for one, all guys really think about is girls."

    scene sas7 # FPP. Same as sas7.
    with dissolve

    aut "Haha."

    scene sas7a # FPP. Same as sas7a.
    with dissolve

    u "I mean sex. That is the core to a man's mind."

    scene sas9j # FPP. As above, but slightly agitated, mouth closed.
    with dissolve

    aut "Mm."

    scene sas9k # FPP. As above, but Autumn looking slightly away from camera.
    with dissolve

    u "What about girls? How come you guys aren't so sex hungry all the time?"

    scene sas10 # TPP. Show Autumn and MC sat together, Autumn is grabbing her sign.
    with dissolve

    pause 0.5

    scene sas11 # FPP. Close up Autumn, now holding her completed sign, smile mouth open.
    with dissolve

    aut "How's this?"

    scene sas11a # FPP. As above, mouth closed.
    with dissolve

    u "Looks great!"

    scene sas12 # TPP. Close up MC holding his decorated sign, smiling.
    with dissolve

    pause 0.5

    scene sas12a # TPP. Show MC and Autumn sat together, MC mouth open, Autumn smiling.
    with dissolve

    u "How's mine?"

    scene sas13 # FPP. Close up Autumn, ecstatic, mouth open.
    with dissolve

    aut "Fantastic. Can't wait for the protest tomorrow! It's going to be great."

    scene sas13a # FPP. As above, mouth closed.
    with dissolve

    u "Yeah, can't wait!"

    scene sas13b # FPP. As above, curious expression, mouth open.
    with dissolve

    aut "Meet you there tomorrow?"

    scene sas13c # FPP. As above, mouth closed.
    with dissolve

    u "Yeah."

    scene sas14 # TPP. Show MC and Autumn standing up.
    with dissolve

    pause 0.5

    scene sas14a # TPP. As above, MC and Autumn stood up, Autumn smile, mouth open.
    with dissolve

    aut "Okay well I'll walk you out then. Thanks for coming by."

    scene sas14b # TPP. As above, MC smile, MC mouth open, Autumn mouth closed.
    with dissolve

    u "My pleasure."

    scene sas15 # TPP. Show Autumn walking MC out.
    with dissolve

########## SCENE 37 SETTING UP HOMECOMING W/ MS ROSE
label walking_through_hallways:
    scene shr1 # tpp MC walks through the hallways.
    with fade

    pause 0.5

    scene shr2 #fpp As he walks he passes by Ms. Rose who is setting up Homecoming decorations ideally on some kinda of small latter.
    with dissolve

    scene shr2b # ms rose turns around and looks at you
    with dissolve

    ro "Hey [name], would you mind getting me the tape?"

    scene shr3 #tpp mc walks towards the tape
    with dissolve

    u "Of course, Ms. Rose."

    scene shr3a # mc grabs the tape
    with dissolve

    ro "Thank you."

    scene shr4 # tpp mc hands ms rose the tape
    with dissolve

    u "No worries."

    scene shr5 #fpp ms rose looking at the walk taping something
    with dissolve

    u "*Chuckles* So how did you end up on the homecoming set up crew?"

    scene shr5b # ms rose  no particular emotion, turns around looking at you
    with dissolve

    ro "I'm actually the chaperone in charge of all student events."

    scene shr5c
    with dissolve

    u "That's cool. The head honcho."

    scene shr5d # ms rose starts smiling with an eyeborw raised
    with dissolve

    ro "*Chuckles* I guess you can put it that way."

    if checkonrose:
        scene shr5b
        with dissolve

        ro "This is probably one of the only exciting things I have going on lately."

        scene shr5c
        with dissolve

        u "Really? Why's that?"

        scene shr5b
        with dissolve

        ro "Oh never mind. Not trying to give myself a pity party! Haha."

        scene shr5c
        with dissolve

        u "That's all right. I can listen."

        scene shr5d
        with dissolve

        ro "No, they're my issues, but thanks. I really do enjoy doing these events for the students."

        scene shr5e
        with dissolve

        u "That's good."

    scene shr5d
    with dissolve

    ro "Alright well I better get back to this. Still so much to do!"

    scene shr5e
    with dissolve

    u "Okay. Well you have a good day Ms. Rose."

    scene shr5d
    with dissolve

    ro "You too, [name]."

    scene shr6 # mc walking away
    with dissolve

    pause 0.5

######## SCENE 38 BACK IN YOUR DORM FRIDAY EVENING
    label v7_homecoming:

    if path_builder and not pb_name_set:
        $ name = renpy.input(_("What's your name?"), default=name).strip() or _("Alex")
        $ pb_name_set = True

    if joinwolves:
        stop music fadeout 3

        scene sfr4mc2 # mc in his wolves' room studying
        with fade

        pause 0.5

    else:
        stop music fadeout 3
        scene sfr4mc1 # mc in his dorm studying
        with fade

        pause 0.5

        scene sfr4mc1a # mc looking at his phone
        with dissolve

    play music "music/mdates1.mp3"

    queue music [ "music/mdates2.mp3", "music/mchill1.mp3", "music/mfunk.mp3"]

    if hcGirl == "amber":
        u "(Probably should get going to Amber's soon.)"

        u "(I don't know about doing drugs. Molly? Fuck, I don't know...)"

        u "(I've never done anything like this, but I guess if there's ever a time to do it, it's now.)"

        jump amberhocodate

    else:
        u "(I should probably start getting my suit on and get ready for homecoming.)"

        if joinwolves:
            scene sfr4mc4 # mc adjusting his suit in his Wolves' room
            with fade

        else:
            scene sfr4mc3 # mc adjusting his suit in his drom
            with fade

        if hcGirl == "chloe":
            u "(Time to pick up Chloe. Can't believe she's actually my date...)"

            jump chloehocodate

        elif hcGirl == "emily":
            u "(Time to pick up Emily. Let's hope this goes well...)"

            jump emilyhocodate

        elif hcGirl == "lauren":
            u "(Time to pick up Lauren. I bet she looks stunning in her dress...)"

            jump laurenhocodate

        elif hcGirl == "penelope":
            u "(Time to pick up Penelope. She's gonna make a great date...)"

            jump penelopehocodate

        elif hcGirl == "riley":
            u "(Time to pick up Riley. This is gonna be an amazing night...)"

            jump rileyhocodate

        else:
            u "(I'm sure going without a date has a lot of advantages...)"

            scene sfr4mc5 # mc in a suit going to homecoming by himself
            with fade

            pause 1.0

            play music "music/mhoco1.mp3"

            queue music [ "music/mhoco2.mp3", "music/mhoco3.mp3", "music/mhoco4.mp3"]

            scene sfr4mc6 # mc walking into the gym building
            with fade

            pause 1.0

            jump labelfr4dancefloor


############### SCENE 44 DATE: AMBER

label amberhocodate:
    scene sfr4am1 #mc in white t-shirt walking through the suburbs
    with fade

    pause 0.5

    scene sfr4am2 #MC arrives at Amber's dorm step. He knocks
    with fade
    play sound sound.knock
    
    pause 1.5

    play sound "sounds/dooropen.mp3"
    scene sfr4am3 #CLOSE UP Amber opens the door, excited mouth open
    with dissolve

    am "Hey, you ready to party or what?"

    scene sfr4am3a
    with dissolve

    u "Uhm... yeah."

    scene sfr4am3
    with dissolve

    am "Well come in then."

    scene sfr4am4 # mc follows amber inside
    with dissolve

    pause 0.5

    scene sfr4am5 # they sit down on amber's couch
    with dissolve

    pause 0.5

    if is_censored:
        call screen censored_popup("v7_nsfwSkipLabel5")

    scene sfr4am6 #First person Close up Amber pulls out 2 pills. a bit flirty and happy
    with dissolve

    am "Picked these up yesterday. Heard they're good."

    scene sfr4am6a
    with dissolve

    u "You've never done them?"

    scene sfr4am6
    with dissolve

    am "I mean I've done plenty of pills, just not these particular ones. *Laughs*"

    scene sfr4am6a
    with dissolve

    u "What exactly happens when you take them?"

    scene sfr4am6b # amber curious, surprised
    with dissolve

    am "You've never taken Molly before?"

    scene sfr4am6c
    with dissolve

    u "Uh... no, not really."

    scene sfr4am6
    with dissolve

    am "It's hard to describe. Imagine that all of your negative feelings go away. Also, rubbing your face on the floor feels really good."  ### @goose

    scene sfr4am6a
    with dissolve

    u "Haha, okay. I guess let's just get it over with."

    scene sfr4am6
    with dissolve

    am "Don't worry so much. You're gonna love it."

    scene sfr4am7 # shnowing mc and amber popping a pill into their mouth
    with dissolve
    #Amber shows him the pills and shows him that there is a small heart stamp on each pill. Amber takes one and pops it in her mouth. She Washes it down with a water bottle.
    pause 0.5
    scene sfr4am6d # close up amber, not holding pills, drinking out of a water bottle
    with dissolve

label v7_nsfwSkipLabel5:
    $ grant_achievement("ecstatic")
        
    u "Now what?"

    scene sfr4am6f # amber smiling, with one eyebrow raised a bit at you mouth open
    with dissolve

    am "Now we wait, it takes a few minutes to set in."

    scene sfr4am6g
    with dissolve

    u "Oh alright."

    scene sfr4am6f
    with dissolve

    am "So you glad you missed out on homecoming?"

    scene sfr4am6g
    with dissolve

    u "Yeah I guess. Always got next year if I really wanna go. And this did sound a lot more exciting."

    scene sfr4am6f
    with dissolve

    am "Trust me, this is gonna be so much better. You're about to have the most amazing experience."

    scene sfr4am6g
    with dissolve

    u "I mean we could've done this any day though. How come you don't like dances?"

    scene sfr4am6h # amber more serious / thoughtful
    with dissolve

    am "I mean that kinda stuff was exciting back in high school, but now I'm an adult. Just feels more suitable to do adult stuff, you know."

    scene sfr4am6j
    with dissolve

    u "Like drugs? Haha."

    scene sfr4am6h
    with dissolve

    am "Well yeah. No adults watching over you telling you what you can or can't do. Putting on whatever music you like. Essentially doing whatever you want."

    scene sfr4am6j
    with dissolve

    u "Yeah I get it. Freedom."

    scene sfr4am6h
    with dissolve

    am "Exactly. That reminds me."

    scene sfr4am8 #amber get's up and walks towards speakers
    with dissolve

    pause 0.5

    scene sfr4am8a #amber puts on some music and changes the lights to dark blue lighting
    with dissolve

    play sound "sounds/rejectcall.mp3"

    # music starts

    pause 0.5

    scene sfr4am8b # amber drags the table asside
    with dissolve

    u "Alriiight. I'm starting to get really excited now."

    scene sfr4am8c # table gones just carpet left, amber about to lie down on it
    with dissolve

    am "*Chuckles* The effects should kick in soon."

    scene sfr4am8d # amber lies down on the carpet mouth open
    with dissolve

    am "But yeah. Freedom. Little would you know but I use to be a little angel back in my days. Haha."

    scene sfr4am8e # mouth closed
    with dissolve

    u "What happened?"

    scene sfr4am9 # close up amber looking at you from lying on the floor
    with dissolve

    am "I decided to live! I was tired of trying to fit into my parents' ideas of who I should be. So I just said fuck it."

    scene sfr4am9a
    with dissolve

    u "That's surprisingly wise, haha."

    # pill hit sounds, graphic animation, drug overlay

    scene sfr4am9a
    with vpunch

    pause 1.0
    #Suddenly, the pill hits MC. A smile goes over his face and Amber can see it.

    scene sfr4am10 # showing mc with mouth open on drugs
    with dissolve

    u "Woah..."

    scene sfr4am9b # amber laughingly
    with dissolve

    am "Oooh feeling something aren't you?"

    scene sfr4am9a
    with dissolve

    u "Yeah. Yeah, I think so. I feel kind of-"

    scene sfr4am9b
    with dissolve

    am "Amazing. Am I right?"

    scene sfr4am9a
    with dissolve

    u "Yeah... amazing."

    scene sfr4am9b
    with dissolve

    am "Lie down next to me."

    scene sfr4am11 # mc sitting
    with dissolve

    pause 0.5

    scene sfr4am11a # mc about to lie down next to amber
    with dissolve

    pause 0.5

    scene sfr4am11b # mc lying next to amber
    with dissolve

    pause 0.5

    scene sfr4am12 # First person close up amber looking at you, right next to you. Peacefully
    with dissolve

    am "Just look at the ceiling for a bit."

    scene sfr4am13 # ceiling closeup
    with dissolve

    am "Doesn't it just have the best color ever?"

    u "Yeah... it does."

    u "Honestly the ceiling just fits so perfectly into the room."

    am "I have never seen a better ceiling in my life."

    u "*Chuckles*"

    scene sfr4am12b # Close up amber holding a plush toy towards you
    with dissolve

    am "Hold this."

    scene sfr4am14 # showing mc touch the plush toy
    with dissolve

    u "It's so fluffy."

    scene sfr4am14a # showing mc rubbing the plush toy against his face
    with dissolve

    u "Man, this feels so good."

    scene sfr4am12d # amber smiling
    with dissolve

    am "I know, it's so nice, right?"

    am "Hold my hand."

    u "What?"

    scene sfr4am12d
    with dissolve

    am "Trust me. It feels really good when you're high."

    scene sfr4am15 # close up holding hands
    with dissolve

    u "Woah... my hands are so sensitive."

    u "And your hands are so... soft."

    scene sfr4am12d
    with dissolve

    am "Isn't it just the best?"

    scene sfr4am12e
    with dissolve

    u "Yeah... it's incredible."

    scene sfr4am15a # close up holding hands finger movement
    with dissolve

    pause 0.5

    scene sfr4am15b # close up holding hands finger movement
    with dissolve

    pause 0.5

    scene sfr4am12e
    with dissolve

    pause 0.5

    u "How do you keep your hands so soft?"

    scene sfr4am12d
    with dissolve

    am "Uhm... lotion? *Laughs*"

    scene sfr4am12e
    with dissolve

    u "Woah... that's crazy."

    scene sfr4am12d
    with dissolve

    am "*Chuckles* Is it?"

    scene sfr4am12e
    with dissolve

    u "Yeaaaahhh..."

    scene sfr4am16 # amber puts your hand on her stomach
    with dissolve

    pause 0.5

    u "Man... you're soft everywhere."

    scene sfr4am12d
    with dissolve

    am "*Laughs* Thanks."

    scene sfr4am16a # you put your hand into her belly button
    with dissolve

    am "*Chuckles* Hey! What are you doing?"

    u "Uhm... just exploring."

    scene sfr4am12d
    with dissolve

    am "*Laughs* Exploring my belly button?"

    scene sfr4am12e
    with dissolve

    u "What can I say? it feels good. *Laughs*"

    jump fr4amberending

############### SCENE 39 HOMECOMING DATE: CHLOE
label chloehocodate:
    scene sfr4cl1 #mc in suit walking through the town
    with fade

    pause 0.5

    scene sfr4cl2 #mc knocking on chick's door
    with fade

    play sound sound.knock

    pause 1.5

    play sound "sounds/dooropen.mp3"
    scene sfr4cl3 # close up nora opening the door indifferent in her dress
    with dissolve

    no "Hey."

    scene sfr4cl3b # nora turns around and yells.
    with dissolve

    no "Chloeee! Your date's here."

    scene sfr4cl3f # chloe walks towards you in a dress, smiling
    with fade

    cl "Come in, we're just pregaming."

    u "Okay."

    scene sfr4cl4 #First personBehind Chloe walking into the kitchen where Aubrey, Aaron and Lindsey are already taking shots.
    with dissolve

    if joinwolves:
        cl "This is Lindsey by the way."

    else:
        cl "These are Lindsey and Aaron by the way."

    u "Hey, guys."

    scene sfr4cl9 # close up lindsey smiling
    with dissolve

    li "Heyyy!"

    scene sfr4cl5 # close up aaron smiling at you
    with dissolve

    aa "What's up, player?"

    scene sfr4cl6 # chloe close up looking at aubrey smiling/ laughingly
    with dissolve

    cl "Aubrey, you mind taking a picture before we get too wasted? *Laughs*"

    scene sfr4cl7 # clse up aubrey smiling
    with dissolve

    au "Of course!"

    scene sfr4cl8 # showing aubrey taking a pic of mc with his hand around chloe's waist while she kisses him on the cheek.
    with dissolve

    pause 0.5

    play sound sound.capture
    scene sfr4cl8
    with flash

    pause 0.5

    scene sfr4cl8a #chloe walks towards aubrey mouth open
    with dissolve

    cl "Thanks!"

    scene sfr4cl5b # aaron looking around
    with dissolve

    aa "Shots everyone?"

    scene sfr4cl9a # close up chloe excited, witty
    with dissolve

    cl "Is that even a question?"

    scene sfr4cl10 # aubrey grabs a shot glass from the table
    with dissolve

    pause 0.5

    scene sfr4cl10a # aubrey lifts up the shot glass
    with dissolve

    au "To tonight!"

    scene sfr4cl10b # aubrey takes shot
    with dissolve

    pause 0.5

    scene sfr4cl11 #first person closec up aaron excited, stood up with shot in hand, looking into the room
    with dissolve

    aa "Alriiight! Time for some beer pong!"

    scene sfr4cl11b # aaron excited, stood up with shot in hand, now looking into the camera
    with dissolve

    aa "What you say, bro? Boys versus girls?"

    scene sfr4cl11c
    with dissolve

    u "Sure. Haha."

    # Beer pong montage, sounds

    scene sfr4cl12 # aaron throwing
    with fade

    pause 0.5

    scene sfr4cl12a # chloe throwing
    with Dissolve(1)

    pause 0.5

    scene sfr4cl12b # ball missing
    with Dissolve(1)

    pause 0.5

    scene sfr4cl12c # ball missing other side
    with Dissolve(1)

    pause 0.5

    scene sfr4cl12d # you funny frustrated
    with vpunch

    u "Nooo!"

    scene sfr4cl12e # ball hits
    with vpunch

    pause 0.5

    scene sfr4cl12f # AUbrey celebrating
    with Dissolve(1)

    au "Yesss!"

    scene sfr4cl12g # Aaaron drinking
    with Dissolve(1)

    pause 0.5

    scene sfr4cl12h # Chloe drinking
    with Dissolve(1)

    pause 0.5

    scene sfr4cl12j # ball in cup
    with vpunch

    pause 0.5

    scene sfr4cl12k # ball in cup 2
    with vpunch

    pause 0.5

    scene sfr4cl12l # ball in cup 3
    with vpunch

    pause 0.5

    scene sfr4cl13 # showing you about to throw both teams 1 cup left, aaron behind you motivating you
    with fade

    aa "Come on, man. This is it. You make that and we win."

    scene sfr4cl13a # you throw and it lands
    with vpunch

    pause 0.5

    scene sfr4cl14 # you and aaron euphoric bro hug
    with dissolve

    aa "Hell yeah! That's how you fucking do it!"

    scene sfr4cl15 # close up aubrey complaining with a smile
    with dissolve

    au "His elbow was totally over the line!"

    scene sfr4cl15a
    with dissolve

    u "I don't know what you're talking about. We won fair and square. *Chuckles*"

    scene sfr4cl16 # close up chloe stood up
    with dissolve

    cl "I think we have a bit more time before the limo arrives."

    cl "You guys wanna play would you rather?"

    scene sfr4cl16a
    with dissolve

    u "Sure, but first you better drink the remaining beers. You're not getting away that easy."

    scene sfr4cl16b # close up chloe funny annoyed
    with dissolve

    cl "*Chuckles* Fine."

    scene sfr4cl16d # chloe drinks one of the cups
    with dissolve

    u "Also, did you say limo???"

    scene sfr4cl15b # aubrey funny ashamed smile
    with dissolve

    au "We might have seen that uber does limos while trying to order one... so now we're taking a limo to homecoming."

    scene sfr4cl15c
    with dissolve

    u "Holy shit, that's so cool! I've never been in a limo before."

    scene sfr4cl17 # close up aaron talking to you
    with dissolve

    aa "Hell yeah, bro. You wouldn't believe what it's like."

    scene sfr4cl17a
    with dissolve

    u "Wait, have you actually been in one before?"

    scene sfr4cl17
    with dissolve

    aa "Well... no. But, I did watch a lot of music videos."

    scene sfr4cl17a
    with dissolve

    u "*Laughs* Fair enough."

    scene sfr4cl18 # group sitting on the couch in a circle and Chloe mouth open, everyone's smiling
    with fade

    cl "Okay guys, rules are simple."

    scene sfr4cl19 # cloe up chloe looking into the group
    with dissolve

    cl "You ask someone a \"Would you rather...\"-question and after answering that person gets to ask the next question to someone else."

    cl "I'ma start."

    scene sfr4cl19b # cloe up chloe looking at you flirty
    with dissolve

    cl "[name], if you hadn't taken me to hoco, would you rather take Aubrey or Lindsey?"

    scene sfr4cl19c
    with dissolve

    u "*Laughs* Really? You're gonna start off like that?"

    scene sfr4cl20 # lindsey close up looking at you laughingly
    with dissolve

    li "Choose your answer wisely."

    scene sfr4cl20a
    with dissolve

    menu:
        "Aubrey":
            $ reputation.add_point(RepComponent.BRO)
            scene sfr4cl21a # aubrey looking at you smiling mouth closed
            with dissolve

            u "I'm gonna go with Aubrey. Sorry, Lindsey."

            scene sfr4cl20
            with dissolve

            li "Unbelievable..."

            scene sfr4cl21
            with dissolve

            au "This man's got taste!"

        "Lindsey":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            u "I'm gonna go with Lindsey. Sorry, Aubrey."

            scene sfr4cl21
            with dissolve

            au "You're ridiculous."

            scene sfr4cl20
            with dissolve

            li "Watch out, Aaron."

    scene sfr4cl21a # aubrey looking at you smiling mouth closed
    with dissolve

    u "Okay, uhm... Aubrey."

    scene sfr4cl21
    with dissolve

    au "Yes?"

    scene sfr4cl21a # aubrey looking at you smiling mouth closed
    with dissolve

    menu:
        "Ask something sexual":
            $ reputation.add_point(RepComponent.BRO)
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            u "Would you rather have a threesome with two guys, or a guy and a girl?"

            scene sfr4cl22 # closeup aaron smiling laugh looking at aubrey
            with dissolve

            aa "*Laughs* He's asking the important questions!"

            scene sfr4cl21
            with dissolve

            au "I'd pick a guy and girl. I feel like that'd be the most fun. Two guys just seems like a lot of focus on me and I'd rather give than receive."

            scene sfr4cl22
            with dissolve

            aa "*Laughs* I may have picked the wrong hoco date."

            scene sfr4cl20b # lindsey pissed looking at aaron
            with dissolve

            li "Wow, Aaron..."

            scene sfr4cl20c
            with dissolve

        "Ask something funny":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            u "Would you rather fight 100 hamster sized zebras or one zebra sized hamster?"

            scene sfr4cl21
            with dissolve

            au "*Laughs* Definitely 100 hamster sized zebras!"

            scene sfr4cl22 # closeup aaron smiling laugh looking at aubrey
            with dissolve

            aa "What??? You're crazy, zebras will destroy you. One giant hamster is the way to go!"

            scene sfr4cl22a
            with dissolve

    # honk sound #check - add honk.mp3 sound file
    play sound sound.honk
    "*Honk*"

    scene sfr4cl23 # chloe turned around looking at the door
    with dissolve

    cl "Oh, the limo must be here!"

    scene sfr4cl24 # everyone sitting in the limo, you one side in the middle of aubrey and chloe, aaron enthusiastic
    with fade

    aa "This is the life!"

    scene sfr4cl25 # chloe up chloe looking at you smiling
    with dissolve

    cl "So? What do you think?"

    scene sfr4cl25a
    with dissolve

    u "Sitting in a limo next to the most stunning girl I've ever seen... can't get better than this."

    scene sfr4cl25b # chloe touched by your words
    with dissolve

    cl "Awww!"

    scene sfr4cl25c
    with dissolve

    menu:
        "Joke around":
            $ reputation.add_point(RepComponent.BRO)
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            u "And then on the other side of me, you're sitting. So that's really cool too."

            scene sfr4cl25d # chloe funny pissed laughing
            with dissolve

            cl "*Laughs* Oh wow! You're unbelievable."

        "Keep it romantic":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            u "We'll make this the best night ever."

            scene sfr4cl25b
            with dissolve

            cl "*Smirks* I think we will!"

    play music "music/mhoco1.mp3"

    queue music [ "music/mhoco2.mp3", "music/mhoco3.mp3", "music/mhoco4.mp3"]

    scene sfr4cl26 # you and chloe walking into the gym at homecoming
    with fade

    cl "Can't believe I got out of decorating most of this."

    scene sfr4cl26a
    with dissolve

    u "What do you mean?"

    scene sfr4cl27 # close of up chloe smiling
    with dissolve

    cl "Well I had to find someone to jump in for me since I'm head of the events committee."

    scene sfr4cl27a
    with dissolve

    u "Wait why couldn't you help decorating?"

    scene sfr4cl27 # close of up chloe smiling
    with dissolve

    cl "Cause I wanted to spend the entire night with you, dumbo! *Chuckles*"

    scene sfr4cl27a
    with dissolve

    u "*Laughs* Oh, now I get it. What can I say, I'm a lucky guy."

    scene sfr4cl27 # close of up chloe smiling
    with dissolve

    cl "Yeah, you are. Wanna go take some pictures?"

    scene sfr4cl27a
    with dissolve

    u "100 percent."

    scene sfr4cl28 # chloe and mc getting their pics taken pose 1
    with Dissolve(1)

    pause 0.5

    play sound sound.capture
    scene sfr4cl28 # pose 1
    with flash

    pause 0.5

    scene sfr4cl28a # pose 2
    with dissolve

    pause 0.5

    play sound sound.capture
    scene sfr4cl28a # pose 2
    with flash

    pause 0.5

    scene sfr4cl28b # pose 3
    with dissolve

    pause 0.5

    play sound sound.capture
    scene sfr4cl28b # pose 3
    with flash

    pause 0.5

    scene sfr4cl29 # close up chloe smiling at you
    with dissolve

    cl "Wanna dance?"

    scene sfr4cl29a
    with dissolve

    u "Sure, let's go."

    scene sfr4cl30 # you and chloe dancing
    with Dissolve (1)

    pause 0.5

    scene sfr4cl30a # you and chloe dancing pose 2
    with dissolve

    pause 0.5

    scene sfr4cl30b # you and chloe dancing pose 3
    with dissolve

    pause 0.5

    scene sfr4cl31a # close up chloe mouth closed, dancing happy
    with dissolve

    u "I'm gonna say hi to my friends real quick, if you don't mind."

    scene sfr4cl31 # mouth open
    with dissolve

    cl "Yeah, of course. I'll be here dancing."

    jump labelfr4dancefloor

############### SCENE 40 HOMECOMING DATE: EMILY

label emilyhocodate:
    scene sfr4em1 #mc in a suit walking through dorm hallways
    with fade

    pause 0.5

    scene sfr4em2 #mc knocking on emily's dorm
    with dissolve

    play sound sound.knock

    pause 1.5

    play sound "sounds/dooropen.mp3"
    scene sfr4em3 # close up emily opening the door in her dress smiling
    with dissolve

    em "Heyyy!"

    scene sfr4em3a
    with dissolve

    u "Wow! You look... incredible."

    scene sfr4em3b # em flattered / cute
    with dissolve

    em "Thank you!"

    em "Come in."

    scene sfr4em4 # you and emily sitting on your bed, you looking at her talking
    with dissolve

    u "This reminds me of our prom night."

    scene sfr4em5 #First person close up emily smiling
    with dissolve

    em "*Chuckles* Let's not bring that up."

    scene sfr4em5a
    with dissolve

    u "Just saying, you all dressed up lookin beautiful. Me in a suit."

    scene sfr4em5
    with dissolve

    em "Yeah, only now we're older aaaannnd we can drink with no parents around."

    scene sfr4em5b #Emily lifts up a bottle of alcohol (vodka or somethng?) not beer
    with dissolve

    u "Haha, yeah you're right about that."

    scene sfr4em5c # emily drinks straight from the bottle
    with dissolve

    u "Jesus, you still drink from the bottle? You really haven't changed, haha."

    scene sfr4em5d # emily holds to bottle out to you
    with dissolve

    em "Your turn."

    scene sfr4em6 # showing mc drinking straight from the bottle
    with dissolve

    pause 0.5

    scene sfr4em5a
    with dissolve

    u "*Winces* Oh god."

    scene sfr4em5
    with dissolve

    em "Oh come on, it's not that bad."

    scene sfr4em5a
    with dissolve

    u "I strongly disagree with that statement."

    scene sfr4em5
    with dissolve

    em "You should definitely be used to these things by now."

    scene sfr4em5a
    with dissolve

    u "*Laughs* Yeah... maybe I should be."

    scene sfr4em7 #FIRST PERSON emily stands up
    with dissolve

    em "What do you think of my dress by the way?"

    scene sfr4em7a # emily turnsaround
    with dissolve

    u "It looks amazing on you. I like this dress better than your prom dress."

    scene sfr4em7b # emily back to facing mc smiling, cute
    with dissolve

    em "You think? Or maybe you just miss me."

    scene sfr4em7c
    with dissolve

    u "Maybe a bit of both."

    scene sfr4em8 # showing emily standing close to mc
    with dissolve

    pause 0.5

    scene sfr4em8a # showing emily bending forward to kiss him
    with dissolve
    play sound sound.kiss

    pause 1.0

    scene sfr4em8 # showing emily standing close to mc
    with dissolve

    pause 0.5

    scene sfr4em7b
    with dissolve

    em "Oh yeah, and when we get there, can we take a cute photo in the booth? No prom repeats please."

    scene sfr4em7c
    with dissolve

    u "What was wrong with our prom photos?"

    scene sfr4em7e # emily giving you a "seriously" look mouth closed
    with dissolve

    pause 0.5

    u "What?"

    scene sfr4em7d
    with dissolve

    em "Our prom photos sucked. You were so sweaty in all of them."

    scene sfr4em7e
    with dissolve

    u "*Chuckles* I told you, I ate really hot chili right before they were taken."

    scene sfr4em7f
    with dissolve

    em "*Laughs* Do you still know how to dance?"

    scene sfr4em7g
    with dissolve

    menu:
        "Of course":
            $ reputation.add_point(RepComponent.BRO)

            u "Of course. Dancing is like riding a bicycle. You don't unlearn that."

            u "Especially not if you're as good as I am."

            scene sfr4em7h # emily stretches out her hands towards you to get you to dance with her.
            with dissolve

            em "Show me then."

        "I'm not sure":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            u "I'm not sure... I haven't properly done couple dancing since high school."

            scene sfr4em7h # emily stretches out her hands towards you to get you to dance with her.
            with dissolve

            em "All the more reason to do a trial run."

    scene sfr4em9 # showing you standing up after taking emily's hand
    with dissolve

    pause 0.5

    scene sfr4em9a # showing emily walking to her phone on her desk
    with dissolve

    em "Let me just put on some music."

    # slow dance music starts

    scene sfr4em9b # emily coming back,
    with dissolve

    u "Alright, let's do this."

    scene sfr4em10 # slow dancing pose 1
    with dissolve

    pause 0.5

    scene sfr4em10a # slow dancing pose 2
    with dissolve

    pause 0.5

    scene sfr4em11 #First person close up emily looking cute
    with dissolve

    em "I can work with this."

    scene sfr4em11a
    with dissolve

    u "*Chuckles* Good, cause it's kinda late for you to back out."

    scene sfr4em12 # showing both mc and emily closeup
    with dissolve

    menu:
        "Kiss her lips":
            scene sfr4em12a # mc kisses her on the lips
            with dissolve

            pause 0.5

            scene sfr4em12d # mc and emily faces really close, emily mouth open
            with dissolve

        "Kiss her neck":
            scene sfr4em12b # mc kisses her neck
            with dissolve

            em "Mmm. You know that's my favorite, don't you?"

            scene sfr4em12e # mc and emily faces really close, mc mouth open
            with dissolve

            u "How could I forget?"

            scene sfr4em12d # mc and emily faces really close, emily mouth open
            with dissolve

    em "I miss this."

    scene sfr4em12e
    with dissolve

    u "Yeah... me too."

    scene sfr4em12d
    with dissolve

    em "We should get going before we get carried away."

    scene sfr4em12e
    with dissolve

    u "You're probably right. Might just end up staying."

    scene sfr4em12d
    with dissolve

    em "*Chuckles* Yeah, and we wouldn't want that, would we?"

    scene sfr4em12e
    with dissolve

    u "No we wouldn't."

    play music "music/mhoco1.mp3"

    queue music [ "music/mhoco2.mp3", "music/mhoco3.mp3", "music/mhoco4.mp3"]

    scene sfr4em13 # emily and mc arrive inside the gym
    with fade

    pause 0.5

    scene sfr4em14 #first person close up emily looking at you, little expression.
    with dissolve

    em "I feel like our prom was a lot bigger."

    scene sfr4em14a
    with dissolve

    u "Yeah, maybe."

    scene sfr4em14
    with dissolve

    em "Let's take some pictures."

    scene sfr4em14a
    with dissolve

    u "Sure thing."

    scene sfr4em15 # you and emily posing for pictures pose 1
    with Dissolve(1)

    pause 0.5

    play sound sound.capture
    scene sfr4em15 # you and emily posing for pictures pose 1
    with flash

    pause 0.5

    scene sfr4em15a # you and emily posing for pictures pose 2
    with dissolve

    pause 0.5

    play sound sound.capture
    scene sfr4em15a # you and emily posing for pictures pose 2
    with flash

    pause 0.5

    scene sfr4em15b # you and emily posing for pictures pose 3
    with dissolve

    pause 0.5

    play sound sound.capture
    scene sfr4em15b # you and emily posing for pictures pose 3
    with flash

    pause 0.5

    scene sfr4em16 #showing josh close up, who just walked up to you
    with dissolve

    jo "If it isn't our high school's favorite couple. You guys came together?"

    scene sfr4em16a
    with dissolve

    u "Yeah."

    scene sfr4em16
    with dissolve

    jo "It's great seeing that you guys finally made up."

    scene sfr4em16a
    with dissolve

    em "Thanks."

    u "So what's up, you just wandering around?"

    scene sfr4em16
    with dissolve

    jo "Yeah, maybe gonna go out and smoke a blunt. Too sober for this shit right now. Haha."

    scene sfr4em16a
    with dissolve

    u "Right..."

    scene sfr4em16
    with dissolve

    jo "Well I'll catch you guys around."

    scene sfr4em16a
    with dissolve

    u "Alright."

    scene sfr4em16b # josh walking away
    with dissolve

    pause 0.5

    scene sfr4em17 # first person close up emily curious
    with dissolve

    em "Did he seem off to you?"

    scene sfr4em17a
    with dissolve

    u "Josh? No... I think he was just being nice."

    scene sfr4em17
    with dissolve

    em "Anyway, you wanna go dance?"

    scene sfr4em17a
    with dissolve

    u "Yeah, let's do it."

    scene sfr4em18 # you and emily dancing
    with Dissolve (1)

    pause 0.5

    scene sfr4em18a # you and emily dancing pose 2
    with dissolve

    pause 0.5

    scene sfr4em18b # you and emily dancing pose 3
    with dissolve

    pause 0.5

    scene sfr4em19a # close up emily mouth closed, dancing happy
    with dissolve

    u "I'm gonna say hi to my friends real quick, if you don't mind."

    scene sfr4em19 # mouth open
    with dissolve

    em "Yeah, of course. I'll be here dancing."

    jump labelfr4dancefloor

############### SCENE 41 HOMECOMING DATE: LAUREN

label laurenhocodate:
    scene sfr4em1 #mc in a suit walking through dorm hallways
    with fade

    pause 0.5

    scene sfr4em2
    with dissolve

    play sound sound.knock

    pause 1.5

    play sound "sounds/dooropen.mp3"
    scene sfr4la1 # first personclose up lauren opens the door shy smile
    with dissolve

    la "Heyyy."

    scene sfr4la1a
    with dissolve

    u "Damn!"

    scene sfr4la1
    with dissolve

    la "What?"

    scene sfr4la1a
    with dissolve

    u "Nothin. You just look really good!"

    scene sfr4la1a
    with dissolve

    la "Oh, get in here."

    if CharacterService.is_girlfriend(lauren):
        scene sfr4la2 # showing lauren and mc kissing
        with dissolve

        play sound sound.kiss

        pause 1.0

    scene sfr4la3 # first person lauren standing in front you smiling
    with dissolve

    la "We still have some time left. You want a drink?"

    scene sfr4la3a
    with dissolve

    u "Yeah, definitely. Thanks."

    scene sfr4la3b # lauren walks to her desk
    with dissolve

    pause 0.5

    scene sfr4la4 # lauren grabs wine from her desk
    with dissolve

    pause 0.5

    scene sfr4la4a # lauren comes back with 2 wine glasses fileed with red wine
    with dissolve

    la "My favorite wine. Thought it would be nice."

    scene sfr4la5a # first person close up lauren with a wine glass in her hand smiling mouth closed
    with dissolve

    u "Feeling fancy I see."

    scene sfr4la5
    with dissolve

    la "Just for the occasion."

    scene sfr4la5b # toasting wine glasses
    with dissolve

    play sound "sounds/toast.mp3"

    u "Cheers."

    la "Cheers."

    scene sfr4la5c # lauren smells the wine
    with dissolve

    la "Mhm..."

    u "Ahh yes. I can definitely smell a fine note of oak as well as lime stone which was probably the soil for this particular grape."

    scene sfr4la5d # lauren looks at you laughing about to drink her wine
    with dissolve

    la "*Laughs* Oh don't even pretend like you're some kind of wine expert."

    scene sfr4la5e # lauren drinks her win
    with dissolve

    u "What can I say? I'm a man of many talents."

    scene sfr4la6 # showing lauren and mc with wine glasses
    with dissolve

    pause 0.5

    scene sfr4la6a # showing lauren and mc sitting down on her bed
    with dissolve

    pause 0.5

    scene sfr4la7 # close up lauren sitting next to you smiling with one eyebrow raised
    with dissolve

    la "Oh yeah, I just have to say, I'm not much of a dancer."

    scene sfr4la7a
    with dissolve

    menu:
        "Keep it light":
            $ reputation.add_point(RepComponent.BRO)

            u "I'm not surprised."

            scene sfr4la7
            with dissolve

            la "Oh wow."

        "Reassure her":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            u "I'm sure you're not that bad."

            scene sfr4la7
            with dissolve

            la "*Chuckles* Then you're in for a surprise."

    scene sfr4la7a
    with dissolve

    u "Can you stand up? I really wanna take a picture of you in this dress."

    scene sfr4la8 # showing mc, also showing lauren stands up, unsure, smiling
    with dissolve

    la "Uhm sure, haha. Why?"

    scene sfr4la8a # mc pulls out his phone to take picture
    with dissolve

    u "You just look so amazing."

    scene sfr4la9 # first person close up lauren standing in front of you cute smile
    with dissolve

    la "Awww. Maybe I'll surprise you one day and arrive at your dorm in this dress."

    scene sfr4la9a
    with dissolve

    u "Haha. That might just make my year."

    scene sfr4la9
    with dissolve

    la "Well if I show up to your dorm in this dress then you are definitely showing up to my dorm in this suit. I am kinda liking it on you."

    scene sfr4la9a
    with dissolve

    u "Thanks, haha. I'll make note of that."

    scene sfr4la9
    with dissolve

    la "You almost ready to go?"

    scene sfr4la9a
    with dissolve

    u "Yeah, let's go."

    play music "music/mhoco1.mp3"

    queue music [ "music/mhoco2.mp3", "music/mhoco3.mp3", "music/mhoco4.mp3"]

    scene sfr4la10 # Lauren and Mc walking into the gym
    with fade

    pause 0.5

    scene sfr4la11 # first person close up lauren looking at you smiling
    with dissolve

    la "Wow, they really turned the gym into such a nice location for the dance."

    scene sfr4la11a
    with dissolve

    u "Yeah, I think Ms. Rose did a lot of that, I saw her earlier."

    scene sfr4la11
    with dissolve

    la "You wanna take some pictures?"

    scene sfr4la11a
    with dissolve

    u "Yeah, I'd love to."

    scene sfr4la12 # you and la posing for pictures pose 1
    with Dissolve(1)

    pause 0.5

    play sound sound.capture
    scene sfr4la12 # you and la posing for pictures pose 1
    with flash

    pause 0.5

    scene sfr4la12a # you and la posing for pictures pose 2
    with dissolve

    pause 0.5

    play sound sound.capture
    scene sfr4la12a # you and la posing for pictures pose 2
    with flash

    pause 0.5

    scene sfr4la12b # you and la posing for pictures pose 3
    with dissolve

    pause 0.5

    play sound sound.capture
    scene sfr4la12b # you and la posing for pictures pose 3
    with flash

    pause 0.5

    scene sfr4la13 #first person close up lauren, looking at you cute smiling
    with dissolve

    la "I'm so glad we went here together."

    scene sfr4la13a
    with dissolve

    u "Yeah, me too. Best date I could've asked for."

    scene sfr4la13
    with dissolve

    la "Awww."

    scene sfr4la13b # lauren looking past you, moving her head
    with dissolve

    la "Oh look, Ms. Rose is here. Let's say hi."

    scene sfr4la13c
    with dissolve

    u "Sure."

    scene sfr4la14 # mc and lauren walking towards ms rose sitting at her table
    with dissolve

    pause 0.5

    scene sfr4la15 # first person lauren from the side close up talking to ms rose
    with dissolve

    la "Hey Ms. Rose, I didn't know you were a chaperone."

    scene sfr4la16 # close up ms rose smiling looking at lauren
    with dissolve

    ro "Yup! I always chaperone these things."

    scene sfr4la15
    with dissolve

    la "That's so nice."

    scene sfr4la16a
    with dissolve

    u "Hey Ms. Rose."

    scene sfr4la16b # ms rose looking at you
    with dissolve

    ro "Hi [name]. Look at you two... You guys look great."

    scene sfr4la15
    with dissolve

    la "Thanks!"

    scene sfr4la16b # ms rose looking at you
    with dissolve

    ro "Well you two, enjoy your dance tonight and stay out of trouble."

    scene sfr4la16c
    with dissolve

    u "*Chuckles* Of course."

    scene sfr4la15c # lauren looking at you mouth closed, smiling
    with dissolve

    u "Talking about dance, you ready for some movement, Lauren?"

    scene sfr4la15b # mouth open
    with dissolve

    la "Yeah, alright. Let's do it."

    scene sfr4la15
    with dissolve

    la "Bye, Ms. Rose."

    scene sfr4la16b # ms rose looking at you
    with dissolve

    ro "Goodbye you two. Have fun."

    scene sfr4la17 # you and lauren dancing
    with Dissolve (1)

    pause 0.5

    scene sfr4la17a # you and lauren dancing pose 2
    with dissolve

    pause 0.5

    scene sfr4la17b # you and lauren dancing pose 3
    with dissolve

    pause 0.5

    scene sfr4la18a # close up lauren mouth closed, dancing happy
    with dissolve

    u "I'm gonna say hi to my friends real quick, if you don't mind."

    scene sfr4la18 # mouth open
    with dissolve

    la "Yeah, of course. I'll be here."

    jump labelfr4dancefloor

############### SCENE 42 HOMECOMING DATE: PENELOPE
label penelopehocodate:

    scene sfr4em1 #mc in a suit walking through dorm hallways
    with fade

    pause 0.5

    scene sfr4pe1 #you knocking on penelopes door
    with dissolve
    # loud musics playing

    play sound sound.knock

    pause 1.5

    scene sfr4pe1a # you no longer knocking
    with dissolve

    u "Penelope?"

    menu:
        "Enter her room":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            play sound "sounds/dooropen.mp3"
            scene sfr4pe1b # showing mc entering her room, door still only half open, cant see penelope or much in the room
            with dissolve

            pause 0.5

            scene sfr4pe2 #Penelope dancing and singing in her underwear on her bed.
            with dissolve

            u "Penelope?"

            scene sfr4pe2a #Penelope immediately drops to the bed shocked and trying to cover herself.
            with dissolve

            pe "Ah! Oh my god! Turn around!"

            scene sfr4pe3 # showing mc turned around against the door, not showing penelope
            with dissolve

            u "Sorry, sorry. Didn't mean to scare you."

            pe "Let me just get something on quickly. Oh my god I'm so embarrassed."

            u "It's okay! You looked good doing it. *Laughs*"

            pe "You're early aren't you?"

            u "Nope, I think I'm right on time."

            pe "Sorry, I must have just got carried away."

            pe "You can turn around now."

            scene sfr4pe4a # showing close up penelope in her prom dress, smiling embarrassed mouth closed
            with dissolve

            u "Wow You look... stunning."

        "Knock again":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            scene sfr4pe1 #you knocking on penelopes door
            with dissolve

            play sound sound.knock

            pause 1.5

            scene sfr4pe1a
            with dissolve

            pe "One second!"

            u "Alright."

            pe "Okay, you can come in now!"

            play sound "sounds/dooropen.mp3"
            scene sfr4pe1b # showing mc entering her room, door still only half open, cant see penelope
            with dissolve

            pause 0.5

            scene sfr4pe4
            with dissolve

            pe "Sorry, I just got carried away."

            scene sfr4pe4a
            with dissolve

            u "No worries. You look... stunning."

    scene sfr4pe4b # penelope cute smile awww
    with dissolve

    pe "Awww, thank you."

    pe "Honestly I'm so glad you think that, because it took me forever to pick out this dress!"

    pe "I was almost afraid I wouldn't find anything and that I'd have to cancel, but here I am."

    scene sfr4pe4c # 
    with dissolve

    u "Neurotic as ever. *Laughs*"

    scene sfr4pe4
    with dissolve

    pe "What?"

    scene sfr4pe4a
    with dissolve

    u "*Chuckles* Nothing."

    scene sfr4pe4
    with dissolve

    pe "Uhm... you wanna have a drink before we leave?"

    scene sfr4pe4a
    with dissolve

    u "Yeah, let's do it."

    scene sfr4pe5 # FIRST PERSON: penelope walks to her bed
    with dissolve

    pause 0.5

    scene sfr4pe5a # she bends down and pulls out two beer bottles from below her bed
    with dissolve

    pause 0.5

    scene sfr4pe5b # she seems to open them while on the floor but she's got her back turned to you so you can't see the exacts
    with dissolve

    # beer bottle opening sounds #check - add beeropen.mp3 sound file
    play sound "sounds/beeropen.mp3"

    u "Nice hiding spot."

    scene sfr4pe5c # she walks back to you with two open beer bottles in her hand, smiling
    with dissolve

    pe "Thank you. I used to hide everything that I didn't want my parents to see under my bed."

    scene sfr4pe6 # first person you and penelope toasting with beer bottles, it should be a close up of penelope standing in front of you
    with dissolve

    u "*Chuckles* Really?"

    scene sfr4pe6a # penelope drinking from the bottle
    with dissolve

    u "What kinda things are we talking about?"

    scene sfr4pe6b # penelope shy laugh
    with dissolve

    pe "I don't really wanna say."

    scene sfr4pe6c
    with dissolve

    menu:
        "Ask about sex toys":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            u "Come on, were you hiding your sex toys?"

            scene sfr4pe6d # penelope disgusted funny laughing
            with dissolve

            pe "No, ewww! *Laughs*"

            scene sfr4pe6b
            with dissolve

            pe "Well..."

            pe "It was only one... and I just wanted to try it..."

            scene sfr4pe6a
            with dissolve

            u "Well did you?"

            scene sfr4pe6b
            with dissolve

            pe "Did I what?"

            scene sfr4pe6c
            with dissolve

            u "Did you try the toy?"

            scene sfr4pe6d # penelope disgusted funny laughing
            with dissolve

            pe "No!"

            scene sfr4pe6b
            with dissolve

            pe "Well... yeah."

            pe "It was weird... but good. I don't know."

        "Ask about drugs":
            $ reputation.add_point(RepComponent.BRO)

            u "I bet it was weed."

            scene sfr4pe6b
            with dissolve

            pe "*Chuckles* No, I don't do drugs."

            scene sfr4pe6c
            with dissolve

            u "*Chuckles* Whatever you say."

            scene sfr4pe6b
            with dissolve

    pe "Anyways... you wanna play a drinking game?"

    scene sfr4pe7 # showing mc & showing penelope walking towards her bed, with beer bottle in her hand
    with dissolve

    u "Sure, what did you have in mind?"

    scene sfr4pe7a # showing mc & showing penelope sitting down on her bed looking at you
    with dissolve

    pe "One truth, one lie?"

    scene sfr4pe7b # showing mc following her onto the bed
    with dissolve

    u "Isn't it two truths and a lie?"

    scene sfr4pe8 # close up frist person penelope looking at you slightly confused smile sitting next to you
    with dissolve

    pe "I only know it as one truth, one lie."

    scene sfr4pe8a
    with dissolve

    u "*Smirks* Uhm alright, I guess one truth, one lie it is then."

    scene sfr4pe8d # pen determined smile
    with dissolve

    pe "Okay, I'll start. When I was younger, I had four cats and six lizards."

    scene sfr4pe8e
    with dissolve

    menu:
        "You didn't have four cats":
            u "You definitely did not have four cats."

            scene sfr4pe8d
            with dissolve

            pe "Wrong! I did, I only had four lizards though, not six."

            scene sfr4pe8e
            with dissolve

            u "*Laughs* Four cats? That's way too many."

            scene sfr4pe8
            with dissolve

            pe "What??? You can never have too many cats."

            pe "Your turn."

            scene sfr4pe8a
            with dissolve

        "You didn't have six lizards":
            u "You definitely did not have six lizards."

            scene sfr4pe8f # penelope innocent smille
            with dissolve

            pe "Yeah, you're right. I only had four."

            scene sfr4pe8h # penelope drinks from her beer
            with dissolve

            u "*Laughs* Four? That's still four more than I expected..."

            scene sfr4pe8f
            with dissolve

            pe "Pepé, Ronald, Lucy, and Mike. They were so cute!"

            pe "Your turn."

            scene sfr4pe8g
            with dissolve

    u "Okay...uhm, I have been both scuba diving and cliff jumping."

    scene sfr4pe8d
    with dissolve

    pe "No way, you were never cliff jumping."

    scene sfr4pe8e
    with dissolve

    u "Man you're good."

    scene sfr4pe9 # showing mc drinking from his beer
    with dissolve

    pe "My turn... at 14 I both learned how to drive and lost my virginity."

    scene sfr4pe8e
    with dissolve

    menu:
        "You didn't lose your virginity":
            u "No way you lost your virginity at 14, that's a lie."

            scene sfr4pe8f # penelope innocent smille
            with dissolve

            pe "Yeah, you're right..."

            scene sfr4pe8h
            with dissolve

            pause 0.5

            scene sfr4pe8f
            with dissolve

            pe "It was a year before that."

            scene sfr4pe8g
            with dissolve

            u "What???"

            scene sfr4pe8f # penelope laughing
            with dissolve

            pe "*Laughs* I'm just kidding! You should have seen your face though."

        "You didn't learn to drive":
            u "No way you learned to drive that early. I guess you lost your virginity?"

            scene sfr4pe8d
            with dissolve

            pe "Nope, I learned to drive. My grandma taught me."

            scene sfr4pe8e
            with dissolve

            u "Damn."

            scene sfr4pe9 # showing mc drinking from his beer
            with dissolve

            pause 0.5

    scene sfr4pe8e
    with dissolve

    u "Alright. I once got bitten by a raccoon and I only had As on my final report card in high school."

    scene sfr4pe8d
    with dissolve

    pe "This one's hard... You do seem pretty smart so I'm gonna go with only As."

    scene sfr4pe8e
    with dissolve

    u "Nope, a raccoon bit me when I was five."

    scene sfr4pe8
    with dissolve

    pe "That's so random. *Chuckles*"

    scene sfr4pe8h
    with dissolve

    u "Yeah, it just kinda happened, haha."

    scene sfr4pe8f
    with dissolve

    pe "Should we get going now?"

    scene sfr4pe8g
    with dissolve

    u "Yeah, let's head out."

    play music "music/mhoco1.mp3"

    queue music [ "music/mhoco2.mp3", "music/mhoco3.mp3", "music/mhoco4.mp3"]

    scene sfr4pe10 # showing penelope and mc walking into the gym
    with fade

    pe "Oh, it's so nice!"

    scene sfr4pe11 # close up first person penelope smiling at oyu
    with dissolve

    pe "I love what they did with the balloons!"

    scene sfr4pe11a
    with dissolve

    u "Yeah, it's really cool."

    u "So you ready to dance or what?"

    scene sfr4pe11
    with dissolve

    pe "Haha yes I think so! Let's hope I don't fall, or do something embarrassing."

    scene sfr4pe11a
    with dissolve

    u "Don't worry, if you fall, I'm falling with you."

    scene sfr4pe11
    with dissolve

    pe "*Chuckles* Well that just makes me feel much better."

    scene sfr4pe12 # you and penelope dancing
    with Dissolve (1)

    pause 0.5

    scene sfr4pe12a # you and penelope dancing pose 2
    with dissolve

    pause 0.5

    scene sfr4pe12b # you and penelope dancing pose 3
    with dissolve

    pause 0.5

    scene sfr4pe13a # close up penelope mouth closed, dancing happy
    with dissolve

    u "I'm gonna say hi to my friends real quick, if you don't mind."

    scene sfr4pe13 # mouth open
    with dissolve

    pe "Yeah, of course. I'll be here."

    jump labelfr4dancefloor

############### SCENE 43 HOMECOMING DATE: RILEY
label rileyhocodate:
    scene sfr4em1 #mc in a suit walking through dorm hallways
    with fade

    pause 0.5

    scene sfr4pe1 #you knocking on penelopes door
    with dissolve
    # loud musics playing

    play sound sound.knock

    pause 1.5

    play sound "sounds/dooropen.mp3"

    scene sfr4ri1 # first person close up riley oepning hte door, behind her are lauren and ryan sitting on the floor around a small wooden table filled with bottles of alcohol
    with dissolve

    ry "Heyyy [name]! You ready for a wild night?"

    scene sfr4ri1a
    with dissolve

    u "Yeah, of course!"

    scene sfr4ri2 # showing mc walking into riley's dorm
    with dissolve

    ry "What's up!"

    la "Hey."

    scene sfr4ri3 # first personshowing ryan lauren sitting at hte table smiling at you
    with dissolve

    u "Hey guys, you two going together?"

    scene sfr4ri4 # lauren close up no emotion but hesitant / embarrassed
    with dissolve

    la "What? Oh, no. We're just both predrinking here."

    scene sfr4ri5 # ryan close up looking at lauren flirty
    with dissolve

    ry "You know, we still could go together..."

    scene sfr4ri4b # lauren looking at ryan really not sure how to answer
    with dissolve

    la "Uhm..."

    la "I uhm...-"

    scene sfr4ri6 # close up riley smiling looking at lauren adn ryan
    with dissolve

    ri "Who's ready for some drinks?"

    u "I definitely am."

    scene sfr4ri7 # ryan looking at riley
    with dissolve

    ry "We doing flip pong?"

    scene sfr4ri7a
    with dissolve

    u "What's that?"

    scene sfr4ri7b # ryan looking at you surprised
    with dissolve

    ry "Bro, you don't know flip pong?"

    scene sfr4ri8 # lauren setting up cups while explaining to you
    with dissolve

    la "You just try to flip a cup and once you successfully flipped it your team partner has to do the same thing."

    la "Whichever team flipped both their cups first wins the round and the other team has to take a shot."

    scene sfr4ri8a
    with dissolve

    u "Alright, seems easy enough."

    scene sfr4ri6
    with dissolve

    ri "Girls vs. guys."

    scene sfr4ri7 # ryan looking at riley
    with dissolve

    ry "You're on."

    scene sfr4ri9 # you and riley sitting down while ryan and lauren are pouring beer into the cups
    with dissolve

    pause 0.5

    # cup sounds

    scene sfr4ri10 ## first person ryan looking into the group, ready to flip his cup
    with dissolve

    ry "Ready... and go!"

    scene sfr4ri10a
    with dissolve

    pause 0.5

    scene sfr4ri11 #Ryan begins flipping his cup.
    with dissolve

    pause 0.5

    play sound "sounds/cup.mp3"

    scene sfr4ri11a #Ryan still trying to flip his cup.
    with dissolve

    u "Come on, come on!"

    play sound "sounds/cup.mp3"

    scene sfr4ri11b #Ryan still trying to flip his cup.
    with dissolve

    u "You got this, man!"

    play sound "sounds/cup.mp3"
    scene sfr4ri12 #Lauren successfully flips her cup on the first try.
    with dissolve

    pause 0.5


    scene sfr4ri12a # lauren excited and turns to riley
    with dissolve

    la "Oh my god! I got it. Come on Riley!"

    scene sfr4ri13 #Riley flips her cup before Ryan has even flipped his.
    with dissolve

    pause 0.5

    scene sfr4ri13a # riley celebrating
    with dissolve

    pause 0.5

    play sound "sounds/cup.mp3"

    scene sfr4ri13b # riley celebrating
    with dissolve

    la "Yes!"

    scene sfr4ri13c # riley celebrating
    with dissolve

    ri "Woooh!"

    u "Damnit, Ryan."

    scene sfr4ri142
    with dissolve

    pause 0.5

    scene sfr4ri14 #Ryan and Mc pick up their beers and chug them.
    with dissolve

    ry "Beginner's luck. Let's go again."

    scene sfr4ri15 # you look down at your cup ready to flip it
    with dissolve

    pause 0.5

    scene sfr4ri15a # you trying to flip your cup
    with dissolve

    pause 0.5

    play sound "sounds/cup.mp3"

    scene sfr4ri15b # you trying to flip your cup again
    with dissolve

    la "Yes, Riley!"

    play sound "sounds/cup.mp3"
    scene sfr4ri15c  # you finally get it flipped
    with dissolve

    pause 0.5

    play sound "sounds/cup.mp3"
    scene sfr4ri15d  # you finally get it flipped
    with dissolve

    ry "Nice one, [name]!"

    scene sfr4ri11 #ryan flips it on the first try
    with dissolve

    pause 0.5

    play sound "sounds/cup.mp3"
    scene sfr4ri16 #ryan flips it on the first try
    with dissolve

    u "Hell yeah!"

    scene sfr4ri17 # riley frustrated  looking at ryan's flipped cup
    with dissolve

    ri "Oh come on..."

    scene sfr4ri18 # riley and lauren both drinking
    with dissolve

    pause 0.5

    scene sfr4ri19 # showing lauren filling up cups
    with dissolve

    la "Last one. Loser team has to down four cups."

    u "You're on."

    scene sfr4ri20 # lauren ready to flip # STILL NEEDED
    with dissolve

    la "Go!"

    # scene sfr4ri20a #Lauren flips her cup first try.
    # with dissolve

    scene sfr4ri12
    with dissolve

    pause 0.5

    play sound "sounds/cup.mp3"
    scene sfr4ri16 #ryan flips it on the first try
    with dissolve

    u "Yes!"

    scene sfr4ri13a #riley trying to flip her cup
    with dissolve

    la "Come on, Riley!"

    scene sfr4ri15b # you trying to flip your cup
    with dissolve

    ry "Bro, you got this!"

    play sound "sounds/cup.mp3"
    scene sfr4ri13b #Riley flips her cup
    with dissolve

    pause 0.5

    scene sfr4ri13c # riley celebrating
    with dissolve

    ri "Ahhh yeah!"

    scene sfr4ri23 # close up riley looking at you with a confident smirk
    with dissolve

    ri "Drink up, losers!"

    scene sfr4ri24 # ryan and mc chug beer with one hand while having another cup in the other hand
    with dissolve

    pause 0.5

    scene sfr4ri24a # then they chug from the second cup with the other arm
    with dissolve

    pause 0.5

    scene sfr4ri23 # close up riley looking at you with a confident smirk
    with dissolve

    ri "You guys ready to go?"

    u "Yeah, let's go!"

    play music "music/mhoco1.mp3"

    queue music [ "music/mhoco2.mp3", "music/mhoco3.mp3", "music/mhoco4.mp3"]

    scene sfr4ri25 # ryan, lauren , riley and mc arrive in the gym
    with fade

    ri "How cute!"

    scene sfr4ri252 #first person close up ryan looking at you smiling
    with dissolve

    ry "I'm pretty sure, I signed up to DJ, I'll see you later guys."

    scene sfr4ri252a
    with dissolve

    u "Have fun, man."

    scene sfr4ri26 #first person close up lauren looking at you smiling
    with dissolve

    la "I'm gonna go get settled in and talk to some of my friends."

    scene sfr4ri27 #first person close up riley looking at lauren smiling
    with dissolve

    ri "Alright, see you later."

    scene sfr4ri27b # riley looking at you smiling
    with dissolve

    ri "You ready to dance?"

    scene sfr4ri27c
    with dissolve

    u "Of course."

    scene sfr4ri28 # you and riley dancing
    with Dissolve (1)

    pause 0.5

    scene sfr4ri28a # you and riley dancing pose 2
    with dissolve

    pause 0.5

    scene sfr4ri28b # you and riley dancing pose 3
    with dissolve

    pause 0.5

    scene sfr4ri29a # close up riley mouth closed, dancing happy
    with dissolve

    u "I'm gonna say hi to my friends real quick, if you don't mind."

    scene sfr4ri29 # mouth open
    with dissolve

    ri "Sure, I'll be here dancing."

    jump labelfr4dancefloor

############# SCENE 45 HOMECOMING FREE ROAM

label fr4:
    play music "music/mhoco1.mp3"

    queue music [ "music/mhoco2.mp3", "music/mhoco3.mp3", "music/mhoco4.mp3"]

    jump labelfr4dancefloor

    #anchor
    #### room labels Navigation:

label labelfr4dancefloor:
    if hcGirl == "chloe":
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            scene fr4dancefloorchloedatenonora
        else:
            scene fr4dancefloorchloedate

    elif hcGirl == "emily":
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            scene fr4danceflooremilydatenonora
        else:
            scene fr4danceflooremilydate

    elif hcGirl == "lauren":
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            scene fr4dancefloorlaurendatenonora
        else:
            scene fr4dancefloorlaurendate

    elif hcGirl == "penelope":
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            scene fr4dancefloorpenelopedatenonora
        else:
            scene fr4dancefloorpenelopedate

    elif hcGirl == "riley":
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            scene fr4dancefloorrileydatenonora
        else:
            scene fr4dancefloorrileydate

    else:
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            scene fr4dancefloornodatenonora
        else:
            scene fr4dancefloornodate
    
    call screen fr4dancefloor

label labelfr4gymleft:
    if hcGirl == "chloe":
        if "riley" in freeroam4:
            scene fr4gymleftnochloenoriley
        else:
            scene fr4gymleftnochloe

    elif hcGirl == "riley":
        if "chloe" in freeroam4:
            scene fr4gymleftnoriley
        else:
            scene fr4gymleftnochloenoriley

    else:
        if "riley" in freeroam4 and "chloe" in freeroam4:
            scene fr4gymleftnochloenoriley
        elif "riley" in freeroam4:
            scene fr4gymleftnoriley
        elif "chloe" in freeroam4:
            scene fr4gymleftnochloe
        else:
            scene fr4gymleft
    
    call screen fr4gymleft

label labelfr4gymright:
    if hcGirl == "lauren":
        scene fr4gymrightnolauren
    else:
        scene fr4gymright

    call screen fr4gymright

label labelfr4gymentrance:
    if "riley" in freeroam4 and not "riley2" in freeroam4 and "nora" in freeroam4 and not "nora2" in freeroam4:
        scene fr4gymentrancerileynora
    elif "riley" in freeroam4 and not "riley2" in freeroam4:
        scene fr4gymentranceriley
    elif "nora" in freeroam4 and not "nora2" in freeroam4:
        scene fr4gymentrancenora
    else:
        scene fr4gymentrance
    
    call screen fr4gymentrance

label labelfr4hallwaygymexit:
    scene fr4hallwaygymexit

    call screen fr4hallwaygymexit

label labelfr4hallwaybathroom:
    scene fr4hallwaybathroom

    call screen fr4hallwaybathroom

label labelfr4hallway:
    if not hcGirl == "penelope":
        if "chloe" in freeroam4 and preventgrayson:
            scene fr4hallwaychloe
        else:
            scene fr4hallway
    else:
        if "chloe" in freeroam4 and preventgrayson:
            scene fr4hallwaynopenelopechloe
        else:
            scene fr4hallwaynopenelope

    call screen fr4hallway

label labelfr4hallwaycorner:
    if not "grayson" in freeroam4:
        scene fr4hallwaycorner
    elif preventgrayson:
        scene fr4hallwaycornernumber
    else:
        scene fr4hallwaycornernograyson

    call screen fr4hallwaycorner

label labelfr4outsidestairs:
    if not hcGirl == "emily":
        scene fr4outsidestairs
    else:
        scene fr4outsidestairsnoemily
    
    call screen fr4outsidestairs

label labelfr4outsidestreet:
    scene fr4outsidestreet
    
    call screen fr4outsidestreet

    ##### GYM #####

# LOCATION 1: DANCEFLOOR
label fr4chloedate:
    scene sfr4cl31 # fpp close up chloe smiling on dancefloor

    cl "Hey missed you over here."

    scene sfr4cl31a
    with dissolve

    u "Wanna dance?"

    scene sfr4cl31
    with dissolve

    cl "Yeah, of course. Why do you think I'm still on the dance floor?"

    scene sfr4cl31a
    with dissolve

    u "*Chuckles* True."

    if not "crowning" in freeroam4:
        scene sfr4stage1 # close up ms rose on the stage on the microphone
        with dissolve

        ro "Ahem. Hello... Hello... Hi!"

        scene sfr4stage1a
        with dissolve

        pause 0.5

        scene sfr4stage1
        with dissolve

        ro "So it's time for big announcement as you all know... time to announce the homecoming queen and king!"

        scene sfr4stage1a
        with dissolve

        "*Crowd cheers and applauds*"

        scene sfr4stage1
        with dissolve

        ro "And your homecoming king is..."

        ro "Chris Smith!"

        scene sfr4stage2 # chris walks up on stage
        with dissolve

        "*Crowd cheers and applauds*"

        scene sfr4stage2a # chris on stage looking at the crowd
        with dissolve

        ch "Thank you! Thank you!"

        scene sfr4stage3 # ms rose puts a crown on chris' head
        with dissolve

        ro "Congratulations Chris!"

        scene sfr4stage3a # ms rose turning to the crowd
        with dissolve

        ro "Next up, your homecoming queen is..."

        ro "Chloe Moralez!"

        "*Crowd cheers and applauds*"

        scene sfr4cl31
        with dissolve

        cl "That's my cue."

        scene sfr4cl31a
        with dissolve

        u "Go get 'em!"

        scene sfr4stage4 #Chloe runs up on stage
        with dissolve

        "*Crowd continues to cheer*"

        cl "Thanks guys!"

        scene sfr4stage5 #Ms. Rose puts a tiara on her.
        with dissolve

        ro "Congrats Chloe!"

        scene sfr4stage6 # ms rose turns to the crowd
        with dissolve

        ro "Let's give it up for Chris and Chloe!!"

        scene sfr4stage7 # chris and chloe hand in hand bow
        with dissolve
        "*Crowd cheers and applauds*"

        scene sfr4stage6
        with dissolve

        ro "Now it is a tradition that the king and queen dance with each other."

        scene sfr4stage8 # showing Chloe and Chris walking on to the dance floor together
        with dissolve

        pause 0.5

        scene sfr4stage9 # showing Chloe and Chris slow dancing together
        with dissolve

        pause 0.5

        u "(Well this is great...)"

        scene sfr4cl33 # showing Nora stand arms crossed in the corner
        with dissolve

        u "(Hmm...)"

        menu:
            "Ask Nora to dance":
                scene sfr4cl34 # showing mc walking over to nora
                with dissolve

                pause 0.5

                scene sfr4cl35 # close up nora looking not at you
                with dissolve

                u "Hey... you wanna dance?"

                scene sfr4cl35b # close up nora looking at you hesitant
                with dissolve

                no "Uhm..."

                if not CharacterService.is_mad(nora) and "nora" in freeroam3:
                    #If Nora likes you:
                    no "Yeah, why not."

                    scene sfr4cl35c
                    with dissolve

                    u "Cool."

                    scene sfr4cl36 # TPP nora and mc slow dancing, nora slight smile
                    with Dissolve(1)

                    no "Guess we can't let our dates have all the fun."

                    scene sfr4cl36a
                    with dissolve

                    u "Exactly. You having a good night?"

                    scene sfr4cl36b # new pose
                    with dissolve

                    no "Can't complain, well not too much at least. But you know Chris, Mr. Popular."

                    scene sfr4cl36c
                    with dissolve

                    u "Well I'm glad you're at least having a good time."

                    scene sfr4cl36
                    with dissolve

                    no "Haha at least the best I could in this shitty place."

                    scene sfr4cl36a
                    with dissolve

                    u "Oh come on. It's not that bad."

                    scene sfr4cl36b
                    with dissolve

                    no "Well it's not hell if that's what you mean."

                    scene sfr4cl36c
                    with dissolve

                    u "Haha."

                    scene sfr4cl37 #Chloe and Chris walk up. they both have their tiara / crown in their hand no longer on their head
                    with dissolve

                    ch "You guys having fun?"

                    scene sfr4cl38a # close up chris smiling mouth closed
                    with dissolve

                    u "Haha yeah, congrats!"

                    scene sfr4cl38
                    with dissolve

                    ch "Yeah, yeah. Thanks man."

                    scene sfr4cl39 # showing chris and nora, chris talking to nora
                    with dissolve

                    ch "Wanna get a drink?"

                    scene sfr4cl39a
                    with dissolve

                    no "Sure."

                    scene sfr4cl40 #Chris and Nora walk off.
                    with dissolve

                    pause 0.5

                    scene sfr4cl41 # fpp close up chloe smiling at you
                    with dissolve

                    cl "Now for that dance?"

                    scene sfr4cl41a
                    with dissolve

                    u "Finally, haha."

                    jump chloe_dance

                elif not CharacterService.is_mad(nora):
                    no "I don't really feel like dancing, sorry."

                    scene sfr4cl35c
                    with dissolve

                    u "Oh, okay."

                else:
                    no "I don't."

                    scene sfr4cl35c
                    with dissolve

                    u "Uh, okay..."

            "Leave her be":
                u "(I'll leave her be.)"

        label walk_to_ryan:
        scene sfr4cl42 #MC walks over to Ryan.
        with dissolve

        pause 0.5

        scene sfr4cl43 # close up ryan djing
        with dissolve

        u "Hey, what's up?"

        scene sfr4cl43b # ryan looking up at you smiling
        with dissolve

        ry "Hey."

        scene sfr4cl43c
        with dissolve

        u "How's the DJing?"

        scene sfr4cl43b
        with dissolve

        ry "It's good, just wish there were more girls coming by, that's kinda why I offered to do it."

        scene sfr4cl43c
        with dissolve

        u "Haha, I feel you."

        scene sfr4cl44 # close up chloe embarrassed smile, tiara in her hand not on her hand
        with dissolve

        cl "Hey, sorry about that."

        scene sfr4cl44a
        with dissolve

        u "Congrats!"

        scene sfr4cl44
        with dissolve

        cl "Oh yeah, thanks!"

        cl "Now for that dance?"

        scene sfr4cl44a
        with dissolve

        u "Finally, haha."

label chloe_dance:
    play music "music/mlove2.mp3"

    queue music [ "music/mlove.mp3", "music/mlove1.mp3"]

    scene sfr4cl45 # dancing with chloe she's smiling pose 1
    with Dissolve(1)

    cl "I hope you're a better dancer than Chris."

    scene sfr4cl45a
    with dissolve

    u "*Chuckles* What do you mean?"

    scene sfr4cl45b # still smiling, pose 2
    with dissolve

    cl "I don't know if he's just really uncoordinated, or was just enjoying the spotlight a bit too much, but he didn't really lead well *Laughs*."

    scene sfr4cl45c
    with dissolve

    u "He doesn't strike me as the kinda guy to get blinded by the spotlight, haha."

    scene sfr4cl45d # chloe serious, pose 1 again
    with dissolve

    cl "I've known him for a while now and I'm not sure he's as much of a good guy as you think."

    cl "I don't really get along with Nora, but even I see how poorly he treats her sometimes."

    scene sfr4cl45e
    with dissolve

    u "I mean he's just very busy-"

    scene sfr4cl45f # chloe serious, pose 2
    with dissolve

    cl "Being a fraternity President is exhausting, but it doesn't mean you can treat the people around you like they're unimportant."

    cl "He always acts like this super nice guy, but some of the shit he's done..."

    scene sfr4cl45g
    with dissolve

    u "What has he done?"

    scene sfr4cl45d
    with dissolve

    cl "Look, I don't want our night to revolve around him as well, let's just talk about something else okay?"

    scene sfr4cl45e
    with dissolve

    u "Yeah, of course."

    scene sfr4cl45b
    with dissolve

    cl "I'm so glad, I'm here with you."

    scene sfr4cl45c
    with dissolve

    u "Haha, me too."

    scene sfr4cl45h #chloe flirty pose 2
    with dissolve

    cl "And yet... I feel like I'd rather be somewhere else with you."

    scene sfr4cl45j
    with dissolve

    u "*Chuckles* What do you mean?"

    scene sfr4cl45k # chloe flirty pose 3
    with dissolve

    cl "How about we leave early and go back to mine instead?"

    scene sfr4cl45l
    with dissolve

    u "*Gulp* Hell yeah, that sounds pretty good to me."

    scene sfr4cl45k
    with dissolve

    cl "That's what I thought. Let's go."

    scene sfr4cl46 #showing you and chloe, chloe grabs you by your hand and leads you walking towards the exit
    with dissolve

    pause 0.5

    jump fr4chloeending

label fr4emilydate:
    scene sfr4em20 #fpp close up emily dancing very drunkenly

    u "Woah woah woah. Slow down there."

    scene sfr4em20b # emily turning around smiling at you
    with dissolve

    em "Come on! Don't be lame! Dance with me."

    scene sfr4em20c
    with dissolve

    u "Alright, alright."

    scene sfr4em21 # emily grinding on mc
    with dissolve

    pause 0.5

    scene sfr4em21a # emily grinding on mc pose 2
    with dissolve

    pause 0.5

    scene sfr4em21b # emily grinding on mc pose 2
    with dissolve

    pause 0.5

    scene sfr4em22 # In the middle of dancing, Emily pulls a flask out of her dress
    with dissolve

    pause 0.5

    scene sfr4em22b # Emily turns around with flask in her hand looking at you smirking
    with dissolve

    em "Look what I hid under my dress."

    scene sfr4em22c
    with dissolve

    u "Don't you think you had enough?"

    scene sfr4em22d # emily upset
    with dissolve

    em "Don't be all psycho on me. This isn't high school anymore."

    scene sfr4em22f #she starts to chug it
    with dissolve

    u "Calm down, I just don't want you to throw up."

    scene sfr4em22d
    with dissolve

    em "Jeez, just let me enjoy myself."

    scene sfr4em22e
    with dissolve

    u "Alright, whatever."

    scene sfr4em22f
    with dissolve

    u "Well this is like prom again isn't it? You and me, dancing."

    scene sfr4em22h # thoughtful drunk
    with dissolve

    em "Yeah... we should get more drinks."

    scene sfr4em22j
    with dissolve

    u "Didn't you just-"

    scene sfr4em22k # emily puts her fist in front of her mouth like she's about to throw up
    with dissolve

    em "*Gags*"

    scene sfr4em22l # emily worried
    with dissolve

    em "Shit, I think I'm gonna be sick."

    scene sfr4em23 # fpp Emily runs to the bathroom
    with dissolve

    pause 0.5

    scene sfr4em23a # emily runs around the corner to the bathroom
    with dissolve

    u "Emily?"

    scene sfr4em24 # mc entering the bathroom, door half open
    with dissolve

    em "*Throwing up*"

    scene sfr4em25 # mc knocking on the stall
    with dissolve

    u "You okay?"

    scene sfr4em25b # you looking at stall mouth closed neutral face
    with dissolve

    em "Does it sound like I'm okay? Just leave me alone!"

    scene sfr4em25c
    with dissolve

    menu:
        "Apologize":
            u "Look, I'm sorry. Just let me help you."

            scene sfr4em25b
            with dissolve

            em "Please just leave me alone. I don't want you to see me like this. We'll talk tomorrow."

            scene sfr4em25c
            with dissolve

            u "Tomorrow? I can wait outside till you feel better."

            scene sfr4em25b
            with dissolve

            em "I just wanna be alone... I'm sorry, okay?"

            scene sfr4em25c
            with dissolve

            u "Alright, I guess I'll see you tomorrow."

            scene sfr4em26 # mc walks out of the bathroom, door sitll open
            with dissolve

            em "*Throwing up*"

        "Get upset":
            $ forgiveemily = False
            $ CharacterService.set_relationship(emily, Relationship.FRIEND, mc)

            u "I told you to stop drinking Emily. You never fucking listen!"

            scene sfr4em25b
            with dissolve

            em "Really?! You're gonna start that right now? You're such an asshole."

            scene sfr4em25c
            with dissolve

            u "You know what Emily, fuck this. I'm going."

            scene sfr4em25b
            with dissolve

            em "Go ahead! Leave me the fuck alone!"

            scene sfr4em26 # mc walks out of the bathroom, door sitll open
            with dissolve

            em "*Throwing up*"

    scene sfr4em27 # mc walking towards the exit
    with dissolve

    u "(I guess I'll just go home.)"

    scene sfr4em28 # close up riley curious genuine smile
    with dissolve

    ri "Hey [name]."

    scene sfr4em28a
    with dissolve

    if "riley2" in freeroam4:
        u "Oh, hey Riley, didn't you say you wanted to go home?"

        scene sfr4em28
        with dissolve

        ri "Yeah, but some friends held me here..."

        ri "Where are you going?"

        scene sfr4em28a
        with dissolve

        u "I was just heading out."

        scene sfr4em28
        with dissolve

        ri "So you wanna walk home together and maybe hang out for a bit?"

        scene sfr4em28a
        with dissolve

        u "Sure. Emily said she wants to be alone anyway."

        jump fr4rileyending

    else:
        u "Oh, hey Riley."

        scene sfr4em28
        with dissolve

        ri "Where are you going?"

        scene sfr4em28a
        with dissolve

        u "I was just heading out."

        scene sfr4em28
        with dissolve

        ri "Oh, me too. Where's Emily?"

        scene sfr4em28a
        with dissolve

        u "She's uhm... she just wants to be alone right now."

        scene sfr4em28b # riley no particular emotion
        with dissolve

        ri "Oh okay."

        scene sfr4em28 # riley no particular emotion
        with dissolve

        ri "You wanna walk home together and maybe hang out for a bit?"

        scene sfr4em28a
        with dissolve

        u "Sure."

        jump fr4rileyending

label fr4laurendate:
    scene sfr4la19a # close up lauren smiling mouth closed

    u "There's my beautiful lady."

    scene sfr4la19
    with dissolve

    la "Was wondering where my noble steed went? Off having fun?"

    scene sfr4la19a
    with dissolve

    u "Haha I guess you could say that. Just mingling."

    scene sfr4la19
    with dissolve

    la "Well, I'm glad you're back."

    if not "crowning" in freeroam4:
        scene sfr4stage1 # close up ms rose on the stage on the microphone
        with dissolve

        ro "Ahem. Hello... Hello... Hi!"

        scene sfr4stage1a
        with dissolve

        pause 0.5

        scene sfr4stage1
        with dissolve

        ro "So it's time for big announcement as you all know... time to announce the homecoming queen and king!"

        scene sfr4stage1a
        with dissolve

        "*Crowd cheers and applauds*"

        scene sfr4stage1
        with dissolve

        ro "And your homecoming king is..."

        ro "Chris Smith!"

        scene sfr4stage2 # chris walks up on stage
        with dissolve

        "*Crowd cheers and applauds*"

        scene sfr4stage2a # chris on stage looking at the crowd
        with dissolve

        ch "Thank you! Thank you!"

        scene sfr4stage3 # ms rose puts a crown on chris' head
        with dissolve

        ro "Congratulations Chris!"

        scene sfr4stage3a # ms rose turning to the crowd
        with dissolve

        ro "Next up, your homecoming queen is..."

        ro "Chloe Moralez!"

        "*Crowd cheers and applauds*"

        if not v7_chloesad:
            label fr4laurendatechloe:
                scene sfr4stage4 #Chloe runs up on stage
                with dissolve
                "*Crowd continues to cheer*"

                cl "Thanks guys!"

                scene sfr4stage5 #Ms. Rose puts a tiara on her.
                with dissolve

                ro "Congrats Chloe!"

                scene sfr4stage6 # ms rose turns to the crowd
                with dissolve

                ro "Let's give it up for Chris and Chloe!!"

                scene sfr4stage7 # chris and chloe hand in hand bow
                with dissolve
                "*Crowd cheers and applauds*"

                scene sfr4stage6
                with dissolve

                ro "Now it is a tradition that the king and queen dance with each other."

                scene sfr4stage8 # showing Chloe and Chris walking on to the dance floor together
                with dissolve

                pause 0.5

                scene sfr4stage9 # showing Chloe and Chris slow dancing together
                with dissolve

                pause 0.5

        else:
            pause 0.5

            ro "Chloe?... Chloe?"

            scene sfr4la19b # lauren curious
            with dissolve

            la "That's weird, where is she?"

            scene sfr4la19c
            with dissolve

            u "Who knows."

            scene sfr4stage3a
            with dissolve

            ro "Well, let's just start the dance back up then!"

    play music "music/mlove2.mp3"

    queue music [ "music/mlove.mp3", "music/mlove1.mp3"]

    scene sfr4la20a # showing lauren and mc slow dancing, lauren mouth closed, lauren smiling pose 1
    with Dissolve(1)

    pause 0.5

    scene sfr4la20 # showing lauren and mc dancing, lauren mouth open lauren smiling pose 1
    with dissolve

    la "Surprisingly, you're a good dancer. *Chuckles*"

    scene sfr4la20c # mc mouth open, dancing  pose 2
    with dissolve

    u "Haha, thanks. You're not so bad yourself."

    scene sfr4la20b # lauren mouth open, dancing pose 2
    with dissolve

    la "You know what's weird?"

    scene sfr4la20a
    with dissolve

    u "What?"

    scene sfr4la20
    with dissolve

    la "The entire day I was just super excited for this exact moment, but now that it's here, I'd rather do something else."

    scene sfr4la20e # mc worried pose 1
    with dissolve

    u "Oh, have I done something wrong?"

    scene sfr4la20b
    with dissolve

    la "No, not at all!"

    la "It's just... I read about this thing to do with your partner online and I really wanna try it."

    scene sfr4la20c
    with dissolve

    u "What thing?"

    scene sfr4la20
    with dissolve

    la "How about we go back to my dorm now and you'll see?"

    scene sfr4la20a
    with dissolve

    u "Haha, deal."

    play music "music/m16punk.mp3"

    queue music [ "music/mchill1.mp3", "music/m7punk.mp3" ]

    scene sfr4la21 # mc and lauren walking back holding hands through the park
    with fade

    u "Have fun tonight?"

    scene sfr4la22 # fpp close up lauren cute smile
    with dissolve

    la "Of course! Did you?"

    scene sfr4la22a
    with dissolve

    u "Yeah, even though my date danced like she had two left feet. *Laughs*"

    scene sfr4la22b # fpp close up lauren  laughing anooyed
    with dissolve

    la "*Laughs* Oh wow!"

    scene sfr4la22c
    with dissolve

    u "Honestly though, it was an amazing evening. Plus you look so beautiful in that dress, I could barely keep my eyes off you."

    scene sfr4la22
    with dissolve

    la "Haha awww. It's amazing how quickly you switch between insults and sweet talking."

    scene sfr4la22a
    with dissolve

    u "Sweet and sour talk is my forte."

    scene sfr4la23 #Lauren and Mc arrive at Lauren's dorm.
    with fade
    play sound "sounds/dooropen.mp3"

    pause 0.5

    scene sfr4la24 #fpp lauren in front of you in her dorm, her back turned to you.
    with dissolve

    la "Home sweet home."

    jump fr4laurenending

label fr4penelopedate:
    scene sfr4pe14 # fpp penelope turned around dancing close up

    u "Hey, how's the dancing?"

    scene sfr4pe14b # fpp penelope turned around dancing close up shy/ relieved smile
    with dissolve

    pe "You're back! Thank god! I was beginning to think you left me here and went home or something and..."

    pe "I don't know I guess I just get in my head, but now you're here and-"

    scene sfr4pe14c
    with dissolve

    u "No worries. I'm here now. Sorry I just had a lot of people to talk to."

    scene sfr4pe14d
    with dissolve

    pe "Okay, yay." # Hi Steve!

    if not "crowning" in freeroam4:
        scene sfr4stage1 # close up ms rose on the stage on the microphone
        with dissolve

        ro "Ahem. Hello... Hello... Hi!"

        scene sfr4stage1a
        with dissolve

        pause 0.5

        scene sfr4stage1
        with dissolve

        ro "So it's time for big announcement as you all know... time to announce the homecoming queen and king!"

        scene sfr4stage1a
        with dissolve

        "*Crowd cheers and applauds*"

        scene sfr4stage1
        with dissolve

        ro "And your homecoming king is..."

        ro "Chris Smith!"

        scene sfr4stage2 # chris walks up on stage
        with dissolve

        "*Crowd cheers and applauds*"

        scene sfr4stage2a # chris on stage looking at the crowd
        with dissolve

        ch "Thank you! Thank you!"

        scene sfr4stage3 # ms rose puts a crown on chris' head
        with dissolve

        ro "Congratulations Chris!"

        scene sfr4stage3a # ms rose turning to the crowd
        with dissolve

        ro "Next up, your homecoming queen is..."

        ro "Chloe Moralez!"

        "*Crowd cheers and applauds*"

        if not v7_chloesad:
            scene sfr4pe14d # penelope looking at the stage
            with dissolve

            pe "Aw that's good for her! Of course she would win it!"

            scene sfr4pe14b
            with dissolve

            pe "I could never! I would be so nervous walking up like that."

            scene sfr4pe14c
            with dissolve

            u "I'm sure you could."

            scene sfr4pe14c
            with dissolve

            pe "Maybe in a million lifetimes."

            label fr4penelopedatechloe:
                scene sfr4stage4
                with dissolve

                "*Crowd continues to cheer*"

                cl "Thanks guys!"

                scene sfr4stage5 #Ms. Rose puts a tiara on her.
                with dissolve

                ro "Congrats Chloe!"

                scene sfr4stage6 # ms rose turns to the crowd
                with dissolve

                ro "Let's give it up for Chris and Chloe!!"

                scene sfr4stage7 # chris and chloe hand in hand bow
                with dissolve
                "*Crowd cheers and applauds*"

                scene sfr4stage6
                with dissolve

                ro "Now it is a tradition that the king and queen dance with each other."

                scene sfr4stage8 # showing Chloe and Chris walking on to the dance floor together
                with dissolve

                pause 0.5

                scene sfr4stage9 # showing Chloe and Chris slow dancing together
                with dissolve

                pause 0.5

        else:
            pause 0.5

            ro "Chloe?... Chloe?"

            scene sfr4pe14d
            with dissolve

            pe "That's strange! I hope she's alright!"

            scene sfr4pe14b
            with dissolve

            pe "Maybe she was too nervous to come up. Oh my god, I would be too!"

            scene sfr4pe14c
            with dissolve

            u "Yeah, maybe."

            scene sfr4stage3a
            with dissolve

            ro "Well, let's just start the dance back up then!"

    play music "music/mlove2.mp3"

    queue music [ "music/mlove.mp3", "music/mlove1.mp3"]

    scene sfr4pe15 # penelope and mc slow dancing pose 1, penelope cute smiling
    with Dissolve(1)

    pe "This is so nice. I was so nervous about this!"

    scene sfr4pe15a
    with dissolve

    u "About dancing?"

    scene sfr4pe15b # penelope and mc slow dancing pose 2, penelope cute nervous
    with dissolve

    pe "About everything. About going to homecoming with you. I don't know... I didn't wanna disappoint you!"

    scene sfr4pe15c
    with dissolve

    u "Penelope, come on! You could never disappoint me. I asked you out for a reason."

    scene sfr4pe15
    with dissolve

    pe "I know! And I'm so glad you did!"

    scene sfr4pe15a
    with dissolve

    u "Me too."

    scene sfr4pe16 # MONTAGE  penelope and mc dancing mouths closed
    with Dissolve(1)

    pause 1.0

    scene sfr4pe16a # MONTAGE  pose 2
    with Dissolve(1)

    pause 1.0

    scene sfr4pe16b # MONTAGE  pose 3
    with Dissolve(1)

    pause 1.0

    scene sfr4pe17 # fpp close up penelope on the dance floor in front of you yawning hand before mouth tho she do be polite
    with Dissolve(1)

    pe "*Yawn*"

    scene sfr4pe17c #penelope cute embarrased smile mouth closed
    with dissolve

    u "*Chuckles* You getting tired there?"

    scene sfr4pe17b
    with dissolve

    pe "All this dancing is exhausting. I'm so close to just falling asleep."

    scene sfr4pe17c
    with dissolve

    u "How about I walk you home?"

    scene sfr4pe17b
    with dissolve

    pe "Yeah, that'd be nice."

    scene sfr4pe18 # penelope and mc walking home through the park
    with fade

    pause 0.5

    scene sfr4pe19a # ffp close up penelope genuine smile mouth closed
    with dissolve

    u "Had fun tonight?"

    scene sfr4pe19
    with dissolve

    pe "Yeah I had a blast. Did you?"

    scene sfr4pe19a
    with dissolve

    u "Definitely. I mean, I also had the best date there."

    scene sfr4pe19
    with dissolve

    pe "Really?"

    scene sfr4pe19a
    with dissolve

    u "Yeah of course!"

    scene sfr4pe19
    with dissolve

    pe "Awww!"

    pe "But I couldn't have been the best, cause I'm pretty sure that was you."

    scene sfr4pe19a
    with dissolve

    u "Haha, you're cute."

    scene sfr4pe20 # penelope and mc in front of her dorm
    with fade

    pause 0.5

    scene sfr4pe21 # close up penelope
    with dissolve

    pe "Thank you for the amazing evening! Good night, [name]."

    scene sfr4pe21a #
    with dissolve

    u "Of course, night night Penelope."

    scene sfr4pe21b # penelope turns around about to open her door
    with dissolve

    pause 0.5

    scene sfr4pe21c # penelope's head turns back to you mouth slightly open as if she's about to say something
    with dissolve

    pause 0.5

    scene sfr4pe21b # penelope turns around about to open her door
    with dissolve

    pause 0.5

    scene sfr4pe21c # penelope's head turns back to you mouth slightly open as if she's about to say something
    with dissolve

    pause 0.5

    u "*Chuckles* Everything okay?"

    scene sfr4pe21d # penelope shy
    with dissolve

    pe "I'm just wondering... can we-"

    pe "Can we make out before I go in?"

    scene sfr4pe21e
    with dissolve

    u "*Chuckles* What?"

    scene sfr4pe21d
    with dissolve

    pe "Never mind I-"

    scene sfr4pe21e
    with dissolve

    u "Penelope."

    scene sfr4pe21d
    with dissolve

    pe "Yes?"

    scene sfr4pe21vid # animation with start and end of making out
    with dissolve

    " "

    scene sfr4pe21
    with dissolve

    pe "*Giggles* I liked that."

    scene sfr4pe21a
    with dissolve

    u "Me too."

    scene sfr4pe21
    with dissolve

    pe "We should do this again sometime."

    scene sfr4pe21a
    with dissolve

    u "*Chuckles* Homecoming?"

    scene sfr4pe21
    with dissolve

    pe "*Laughs* No! Going on a date."

    scene sfr4pe21a
    with dissolve

    u "Haha, of course. Good night, Penelope."

    scene sfr4pe21
    with dissolve

    pe "Good night, [name]."

    scene sfr4pe22 # mc walking through dorm hallway
    with Dissolve(1)

    pause 0.5

    scene sfr4pe23 # close up Riley in dorm hallway smiling
    with dissolve

    ri "Oh, heyyy [name]. Where you going?"

    scene sfr4pe23a
    with dissolve

    if "riley2" in freeroam4:
        u "Back to my dorm. Didn't you say you were going home a lot earlier?"

        scene sfr4pe23
        with dissolve

        ri "Yeaaah... some friends held me up. You wanna hang out?"

        scene sfr4pe23a
        with dissolve

        u "Uhm... now?"

        scene sfr4pe23
        with dissolve

        ri "Come on, it'll be fun! I don't want the night to end yet."

        scene sfr4pe23a
        with dissolve

        u "Alright, sure."

        scene sfr4pe23
        with dissolve

        ri "Cool!"

        play music "music/m16punk.mp3"

        queue music [ "music/mchill1.mp3", "music/m7punk.mp3" ]

        jump fr4rileyending2

    else:
        u "Back to my dorm. You?"

        scene sfr4pe23
        with dissolve

        ri "Me too. You wanna hang out?"

        scene sfr4pe23a
        with dissolve

        u "Uhm... now?"

        scene sfr4pe23
        with dissolve

        ri "Come on, it'll be fun! I don't want the night to end yet."

        scene sfr4pe23a
        with dissolve

        u "Alright, sure."

        scene sfr4pe23
        with dissolve

        ri "Cool!"

        play music "music/m16punk.mp3"

        queue music [ "music/mchill1.mp3", "music/m7punk.mp3" ]

        jump fr4rileyending2

label fr4rileydate:
    #Talking to riley & she's your date:
    #MC approaches Riley on the dance floor.

    scene sfr4ri30 # close up riley smiling at yo on dancefloor

    ri "Oh hiii, you're back!"

    scene sfr4ri30a
    with dissolve

    u "Yes, I am!"

    scene sfr4ri30
    with dissolve

    ri "Where have you been?"

    scene sfr4ri30a
    with dissolve

    u "Just talking to everyone here."

    scene sfr4ri30
    with dissolve

    ri "But now you're back to dance with me?"

    scene sfr4ri30a
    with dissolve

    u "You bet!"

    scene sfr4stage1 # close up ms rose on the stage on the microphone
    with dissolve

    ro "Ahem. Hello... Hello... Hi!"

    scene sfr4stage1a
    with dissolve

    pause 0.5

    scene sfr4stage1
    with dissolve

    ro "So it's time for big announcement as you all know... time to announce the homecoming queen and king!"

    scene sfr4stage1a
    with dissolve

    "*Crowd cheers and applauds*"

    scene sfr4stage1
    with dissolve

    ro "And your homecoming king is..."

    ro "Chris Smith!"

    scene sfr4stage2 # chris walks up on stage
    with dissolve

    "*Crowd cheers and applauds*"

    scene sfr4stage2a # chris on stage looking at the crowd
    with dissolve

    ch "Thank you! Thank you!"

    scene sfr4stage3 # ms rose puts a crown on chris' head
    with dissolve

    ro "Congratulations Chris!"

    scene sfr4stage3a # ms rose turning to the crowd
    with dissolve

    ro "Next up, your homecoming queen is..."

    ro "Chloe Moralez!"

    "*Crowd cheers and applauds*"

    if not v7_chloesad:
        label fr4rileydatechloe:
            scene sfr4stage4 #Chloe runs up on stage
            with dissolve

            "*Crowd continues to cheer*"

            cl "Thanks guys!"

            scene sfr4stage5 #Ms. Rose puts a tiara on her.
            with dissolve

            ro "Congrats Chloe!"

            scene sfr4stage6 # ms rose turns to the crowd
            with dissolve

            ro "Let's give it up for Chris and Chloe!!"

            scene sfr4stage7 # chris and chloe hand in hand bow
            with dissolve
            "*Crowd cheers and applauds*"

            scene sfr4stage6
            with dissolve

            ro "Now it is a tradition that the king and queen dance with each other."

            scene sfr4stage8 # showing Chloe and Chris walking on to the dance floor together
            with dissolve

            pause 0.5

            scene sfr4stage9 # showing Chloe and Chris slow dancing together
            with dissolve

            pause 0.5

    else:
        pause 0.5

        ro "Chloe?... Chloe?"

        scene sfr4ri30
        with dissolve

        ri "Damn, she just ditched. *Laughs*"

        scene sfr4ri30a
        with dissolve

        u "Yeah seems like it, haha."

        scene sfr4stage3a
        with dissolve

        ro "Well, let's just start the dance back up then!"

    scene sfr4ri31 # riley grinding on you pose 1
    with Dissolve(1)

    pause 1.0

    scene sfr4ri31a # riley grinding on you pose 2
    with Dissolve(1)

    pause 1.0

    scene sfr4ri31b # riley grinding on you pose 3
    with Dissolve(1)

    pause 1.0

    scene sfr4ri31c # riley turns around
    with dissolve

    pause 0.5

    scene sfr4ri32 #fpp riley flirty looking at you close up
    with dissolve

    ri "I can't wait 'til we get to mine."

    scene sfr4ri32a
    with dissolve

    u "Why wait then?"

    scene sfr4ri32
    with dissolve
    ri "*Chuckles* Uhh I like that, let's go."

    scene sfr4ri33 # showing riley dragging mc out of the gym holding him at his hand
    with dissolve

    pause 0.5

    jump fr4rileyending

label fr4nora1:
    $ freeroam4.add("nora")
    #MC approaches Chris and Nora on the dance floor.

    scene sfr4no1 # showing chris and Nora dancing

    u "Hey you two."

    scene sfr4no2 # close up chris with slight smile no longer dancing
    with dissolve

    ch "Hey what's up?"

    scene sfr4no3 # nora looking at chris not smiling
    with dissolve

    no "I'm gonna go grab a drink."

    scene sfr4no2b # chris looking at nora not smiling more like disappointed
    with dissolve

    ch "Uhm... now? Alright, well I'll be here."

    scene sfr4no3b #Nora gone
    with fade

    pause 0.5

    if joinwolves:
        scene sfr4no2c
        with dissolve

        u "You good?"

        scene sfr4no2d # chris no emotion
        with dissolve

        ch "Yeah, Nora's not much of a dancer, so I think she's just not really feeling it."

        scene sfr4no2e
        with dissolve

        menu:
            "Give Chris advice":
                $ reputation.add_point(RepComponent.BOYFRIEND)

                u "You ever thought of just taking her home?"

                scene sfr4no2
                with dissolve

                ch "Taking her home? It's not even midnight."

                scene sfr4no2a
                with dissolve

                u "I'm just saying, maybe she wants to just go home and be alone with you for once. You are a pretty busy guy."

                scene sfr4no2d
                with dissolve

                ch "Yeah, I get you. But it's also a big night. I can't just leave."

                scene sfr4no2e
                with dissolve

                u "I mean you could..."

                scene sfr4no2
                with dissolve

                ch "Yeah, alright. I'll give it some thought."

                scene sfr4no2a
                with dissolve

                u "Well, I'm gonna go get a drink. You need anything?"

                scene sfr4no2
                with dissolve

                ch "Nah I'm good. I'll see you around."

                scene sfr4no2a
                with dissolve

                u "Cool."

            "Agree":
                $ reputation.add_point(RepComponent.BRO)
                u "Yeah, seems like it. But you're enjoying yourself at least?"

                scene sfr4no2
                with dissolve

                ch "Eh, honestly? I'm trying to talk to all my bros, but she doesn't want me going anywhere."

                scene sfr4no2a
                with dissolve

                u "Women, am I right? Haha."

                scene sfr4no2
                with dissolve

                ch "Yeah. Haha."

                scene sfr4no2a
                with dissolve

                u "Well I'ma go and get a drink. See you back at the house later?"

                scene sfr4no2
                with dissolve

                ch "Yeah, see you."

    else:

        u "I uhm, I'll probably get a drink too."

        scene sfr4no2d
        with dissolve

        ch "Alright."

    jump labelfr4dancefloor

label fr4chris1:
    if hcGirl == "chloe":
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            scene fr4dancefloorchloedatenonora
        else:
            scene fr4dancefloorchloedate

    elif hcGirl == "emily":
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            scene fr4danceflooremilydatenonora
        else:
            scene fr4danceflooremilydate

    elif hcGirl == "lauren":
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            scene fr4dancefloorlaurendatenonora
        else:
            scene fr4dancefloorlaurendate

    elif hcGirl == "penelope":
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            scene fr4dancefloorpenelopedatenonora
        else:
            scene fr4dancefloorpenelopedate

    elif hcGirl == "riley":
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            scene fr4dancefloorrileydatenonora
        else:
            scene fr4dancefloorrileydate

    else:
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            scene fr4dancefloornodatenonora
        else:
            scene fr4dancefloornodate

    u "(I've already talked to Chris.)"

    jump labelfr4dancefloor

label fr4elijah1:
    $ freeroam4.add("elijah")

    scene sfr4el1 #Elijah is dancing really dorky with poet 1

    menu:
        "Say hi to Elijah":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            u "Cool moves, man."

            scene sfr4el2 # close upelijah looking at you smiling, sitll dancing
            with dissolve

            el "Thanks!"

            scene sfr4el2a
            with dissolve

            u "*Chuckles* Keep it up."

        "Make fun of Elijah":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            $ reputation.add_point(RepComponent.BRO)


            u "You dance like a clown, man."

            scene sfr4el2b # close upelijah looking at you no longer dancing, annoyed
            with dissolve

            el "Leave me alone."

            scene sfr4el2c
            with dissolve

            u "Sure thing, Krusty."

            if Moods.HURT in elijah.mood:
                scene sfr4el2d # elijah raging
                with dissolve

                el "FUCK YOU!"

                scene sfr4el2e
                with dissolve

                u "Woah, chill!"

                scene sfr4el2d
                with dissolve

                el "No, I'm sick of this shit! Do you think I'm some kind of joke?!"

                scene sfr4el2e
                with dissolve

                u "Calm the fuck down."

                u "I'll leave you alone... Jesus."

    jump labelfr4dancefloor

label fr4elijah2:
    if hcGirl == "chloe":
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            scene fr4dancefloorchloedatenonora
        else:
            scene fr4dancefloorchloedate

    elif hcGirl == "emily":
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            scene fr4danceflooremilydatenonora
        else:
            scene fr4danceflooremilydate

    elif hcGirl == "lauren":
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            scene fr4dancefloorlaurendatenonora
        else:
            scene fr4dancefloorlaurendate

    elif hcGirl == "penelope":
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            scene fr4dancefloorpenelopedatenonora
        else:
            scene fr4dancefloorpenelopedate

    elif hcGirl == "riley":
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            scene fr4dancefloorrileydatenonora
        else:
            scene fr4dancefloorrileydate

    else:
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            scene fr4dancefloornodatenonora
        else:
            scene fr4dancefloornodate

    u "(I'll let him dance.)"

    jump labelfr4dancefloor

label fr4mason1:
    $ freeroam4.add("mason")

    scene sfr4ma1 #showing mason and rg dancing, Mason is aggressively grabbing her ass. she's really enjoying

    rg1 "Mhmmm..."

    u "(Uhhh... I better leave them to it.)"

    jump labelfr4dancefloor

label fr4mason2:
    if hcGirl == "chloe":
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            scene fr4dancefloorchloedatenonora
        else:
            scene fr4dancefloorchloedate

    elif hcGirl == "emily":
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            scene fr4danceflooremilydatenonora
        else:
            scene fr4danceflooremilydate

    elif hcGirl == "lauren":
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            scene fr4dancefloorlaurendatenonora
        else:
            scene fr4dancefloorlaurendate

    elif hcGirl == "penelope":
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            scene fr4dancefloorpenelopedatenonora
        else:
            scene fr4dancefloorpenelopedate

    elif hcGirl == "riley":
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            scene fr4dancefloorrileydatenonora
        else:
            scene fr4dancefloorrileydate

    else:
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            scene fr4dancefloornodatenonora
        else:
            scene fr4dancefloornodate

    u "(I don't wanna go back to them, that was weird.)"

    jump labelfr4dancefloor

label fr4nora3:
    if hcGirl == "chloe":
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            scene fr4dancefloorchloedatenonora
        else:
            scene fr4dancefloorchloedate

    elif hcGirl == "emily":
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            scene fr4danceflooremilydatenonora
        else:
            scene fr4danceflooremilydate

    elif hcGirl == "lauren":
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            scene fr4dancefloorlaurendatenonora
        else:
            scene fr4dancefloorlaurendate

    elif hcGirl == "penelope":
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            scene fr4dancefloorpenelopedatenonora
        else:
            scene fr4dancefloorpenelopedate

    elif hcGirl == "riley":
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            scene fr4dancefloorrileydatenonora
        else:
            scene fr4dancefloorrileydate

    else:
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            scene fr4dancefloornodatenonora
        else:
            scene fr4dancefloornodate

    u "(I've already talked to both of them.)"

    jump labelfr4dancefloor

    ### LOCATION 2: GYM ENTRANCE
label fr4aaron1:
    $ freeroam4.add("aaron")

    scene sfr4aa1 # showing aaron trying to talk lindsey into something but she's not interested

    aa "Come on. It'll be way better than this. Go to my place and have a couple drinks-"

    scene sfr4aa2 # lindsey close up looking at aaron annoyed
    with dissolve

    li "I already told you no. I want to stay here."

    scene sfr4aa2a
    with dissolve

    menu:
        "Back up Aaron":
            $ reputation.add_point(RepComponent.BRO)

            if joinwolves or hcGirl == "chloe":
                u "Trust me, Aaron's a great guy and any girl would be lucky to go home with him."

                scene sfr4aa3 # close up aaron smiling at you
                with dissolve

                aa "Thank you, [name]."

                scene sfr4aa3b # aaron smiling at lindsey pointing at you with his thumb
                with dissolve

                aa "Even [name] here thinks I'm a great guy, come on."

                scene sfr4aa2 # lindsey close up looking at aaron annoyed
                with dissolve

                li "I'm just trying to enjoy the dance. Can we at least stay for a bit longer?"

                scene sfr4aa3d # aaron looking at lindsey, annoyed with lindsey, giving in
                with dissolve

                aa "Fine, we'll stay for a bit longer."

                scene sfr4aa3
                with dissolve

                aa "*Chuckles* Thanks for trying, bro."

                scene sfr4aa3a
                with dissolve

                u "Yeah no worries, haha."

            else:
                u "Trust me, Aaron's a great guy and any girl would be lucky to go home with him."

                scene sfr4aa3 # close up aaron smiling at you
                with dissolve

                aa "Thank you, random guy."

                scene sfr4aa3b # aaron smiling at lindsey pointing at you with his thumb
                with dissolve

                aa "See Lindsey? Even this rando here thinks I'm a great guy, come on."

                scene sfr4aa2 # lindsey close up looking at aaron annoyed
                with dissolve

                li "I'm just trying to enjoy the dance. Can we at least stay for a bit longer?"

                scene sfr4aa3d # aaron looking at lindsey, annoyed with lindsey, giving in
                with dissolve

                aa "Fine, we'll stay for a bit longer."

                scene sfr4aa3
                with dissolve

                aa "Thanks for trying, rando."

                scene sfr4aa3a
                with dissolve

                u "Actually I was at the Wolves rush party just a few days ago..."

                scene sfr4aa3
                with dissolve

                aa "Nope, never heard of you. Bye bye."

                scene sfr4aa3e
                with dissolve

                u "Uhhh, bye."

        "Side with Lindsey":
            $ reputation.add_point(RepComponent.BOYFRIEND)

            if joinwolves or hcGirl == "chloe":
                u "You guys should stay. It's fun!"

                scene sfr4aa3f # close up aaron looking at you annoyed
                with dissolve

                aa "Get outta here, [name]."

                scene sfr4aa2b # lindsey  looking at you smiling with an eyebrow raised
                with dissolve

                li "I feel like he makes some very good points."

                scene sfr4aa3d # aaron looking at lindsey, annoyed with lindsey, giving in
                with dissolve

                aa "Fine, we'll stay for a bit longer."

                scene sfr4aa3f
                with dissolve

                aa "Thanks, bro..."

                scene sfr4aa2b # lindsey  looking at you smiling with an eyebrow raised
                with dissolve

                li "Yeah, thank you."

                scene sfr4aa2c
                with dissolve

                u "Yeah no worries, haha."

            else:
                u "You guys should stay. It's fun!"

                scene sfr4aa3f # close up aaron looking at you annoyed
                with dissolve

                aa "Get outta here, rando."

                scene sfr4aa2b # lindsey  looking at you smiling with an eyebrow raised
                with dissolve

                li "I feel like he makes some very good points."

                scene sfr4aa3d # aaron looking at lindsey, annoyed with lindsey, giving in
                with dissolve

                aa "Fine, we'll stay for a bit longer."

                scene sfr4aa3f
                with dissolve

                aa "Thanks, man..."

                scene sfr4aa2b # lindsey  looking at you smiling with an eyebrow raised
                with dissolve

                li "Yeah, thank you."

                scene sfr4aa2c
                with dissolve

                u "Yeah no worries, haha."

                scene sfr4aa3g
                with dissolve

                u "Also, I was actually at the Wolves rush party just a few days ago..."

                scene sfr4aa3f
                with dissolve

                aa "Nope, never heard of you. Bye bye."

                scene sfr4aa3g
                with dissolve

                u "Uhhh, bye."

    jump labelfr4gymentrance

label fr4aaron2:
    if "riley" in freeroam4 and not "riley2" in freeroam4 and "nora" in freeroam4 and not "nora2" in freeroam4:
        scene fr4gymentrancerileynora
    elif "riley" in freeroam4 and not "riley2" in freeroam4:
        scene fr4gymentranceriley
    elif "nora" in freeroam4 and not "nora2" in freeroam4:
        scene fr4gymentrancenora
    else:
        scene fr4gymentrance

    u "(Not sure I wanna be dragged back into their discussion.)"

    jump labelfr4gymentrance

label fr4riley2:
    scene sfr4ri50 # showing riley getting a drink

    u "Hey."

    scene sfr4ri51 # close up riley lookign at you smiling
    with dissolve

    ri "Oh hey. We took some great pictures earlier, haha."

    scene sfr4ri51a
    with dissolve

    u "*Chuckles* Yeah, definitely."

    scene sfr4stage1 # close up ms rose on the stage on the microphone
    with dissolve

    ro "Ahem. Hello... Hello... Hi!"

    scene sfr4stage1a
    with dissolve

    pause 0.5

    scene sfr4stage1
    with dissolve

    ro "So it's time for big announcement as you all know... time to announce the homecoming queen and king!"

    scene sfr4stage1a
    with dissolve

    "*Crowd cheers and applauds*"

    scene sfr4stage1
    with dissolve

    ro "And your homecoming king is..."

    ro "Chris Smith!"

    scene sfr4stage2 # chris walks up on stage
    with dissolve

    "*Crowd cheers and applauds*"

    scene sfr4stage2a # chris on stage looking at the crowd
    with dissolve

    ch "Thank you! Thank you!"

    scene sfr4stage3 # ms rose puts a crown on chris' head
    with dissolve

    ro "Congratulations Chris!"

    scene sfr4stage3a # ms rose turning to the crowd
    with dissolve

    ro "Next up, your homecoming queen is..."

    ro "Chloe Moralez!"

    "*Crowd cheers and applauds*"

    if not v7_chloesad:
        label fr4alonechloe:

            if not "crowning" in freeroam4:
                scene sfr4stage4 #Chloe runs up on stage
                with dissolve
                "*Crowd continues to cheer*"

                cl "Thanks guys!"

                scene sfr4stage5 #Ms. Rose puts a tiara on her.
                with dissolve

                ro "Congrats Chloe!"

                scene sfr4stage6 # ms rose turns to the crowd
                with dissolve

                ro "Let's give it up for Chris and Chloe!!"

                scene sfr4stage7 # chris and chloe hand in hand bow
                with dissolve
                "*Crowd cheers and applauds*"

                scene sfr4stage6
                with dissolve

                ro "Now it is a tradition that the king and queen dance with each other."

                scene sfr4stage8 # showing Chloe and Chris walking on to the dance floor together
                with dissolve

                pause 0.5

                scene sfr4stage9 # showing Chloe and Chris slow dancing together
                with dissolve

                pause 0.5

    else:
        pause 0.5

        ro "Chloe?... Chloe?"

        scene sfr4ri51
        with dissolve

        ri "Damn, she just ditched. *Laughs*"

        scene sfr4ri51a
        with dissolve

        u "Yeah seems like it, haha."

        scene sfr4stage3a
        with dissolve

        ro "Well, let's just start the dance back up then!"

    scene sfr4ri51b # riley flirty curious
    with dissolve

    ri "Hey... you wanna go back to mine?"

    scene sfr4ri51b
    with dissolve

    u "*Chuckles* What?"

    scene sfr4ri51
    with dissolve

    ri "Well we've been here for a few hours now and it's getting kinda boring."
    $ freeroam4.add("crowning")

    if (Moods.TEASED in riley.mood or CharacterService.is_fwb(riley)) and hcGirl == "alone":
        scene sfr4ri51b
        with dissolve

        ri "I just feel like we could be doing much more fun things..."

        scene sfr4ri51c
        with dissolve

        u "Haha, I agree. Alright, let's go."

        jump fr4rileyending

    elif (Moods.TEASED in riley.mood or CharacterService.is_fwb(riley)):
        scene sfr4ri51b
        with dissolve

        ri "I just feel like we could be doing much more fun things."

        ri "I'm sure your date would understand if you'd let her know you had to leave early..."

        scene sfr4ri51c
        with dissolve

        menu:
            "Alright, let's go":
                $ reputation.add_point(RepComponent.TROUBLEMAKER)

                u "Alright. Let me tell my date that I gotta leave early and let's go."

                jump fr4rileyending

            "I can't ditch my date":
                $ reputation.add_point(RepComponent.BOYFRIEND)
                $ freeroam4.add("riley2")

                u "Riley, I- I can't ditch my date like that."

                scene sfr4ri51d # riley disappointed
                with dissolve

                ri "Oh, alright... I guess I'm going home by myself then."

                scene sfr4ri51e # riley disappointed
                with dissolve

                u "Sorry about that."

                scene sfr4ri51d # riley disappointed
                with dissolve

                ri "It's okay. Bye bye."

                scene sfr4ri51e # riley disappointed
                with dissolve

                u "Bye Riley."

                jump labelfr4gymentrance

    elif hcGirl == "alone":
        scene sfr4ri51
        with dissolve

        ri "I'd just rather hang out with a friend."

        scene sfr4ri51b
        with dissolve

        u "Yeah, agreed. Alright, let's go."

        jump fr4rileyending

    else:
        scene sfr4ri51
        with dissolve

        ri "I'd just rather hang out with a friend."

        ri "I'm sure your date would understand if you'd let her know you had to leave early..."

        scene sfr4ri51a
        with dissolve

        menu:
            "Alright, let's go":
                $ reputation.add_point(RepComponent.TROUBLEMAKER)

                u "Alright. Let me tell my date that I gotta leave early and let's go."

                jump fr4rileyending

            "I can't ditch my date":
                $ reputation.add_point(RepComponent.BOYFRIEND)
                $ freeroam4.add("riley2")

                u "*Chuckles* I can't ditch my date like that."

                scene sfr4ri51d # riley disappointed
                with dissolve

                ri "Oh, alright... I guess I'm going home by myself then."

                scene sfr4ri51e # riley disappointed
                with dissolve

                u "Sorry about that."

                scene sfr4ri51d # riley disappointed
                with dissolve

                ri "It's okay. Bye bye."

                scene sfr4ri51e # riley disappointed
                with dissolve

                u "Bye Riley."

                jump labelfr4gymentrance

label fr4nora2:
    $ freeroam4.add("nora2")

    scene sfr4no4 # nora grabbing a drink

    u "Hey."

    scene sfr4no4a # nora turns around a bit surprised
    with dissolve

    pause 0.5

    if not CharacterService.is_mad(nora) and "nora" in freeroam3:
        scene sfr4no5 # close up nora smile with a bit of holding back or "this dance is stupid" attitude
        with dissolve

        no "Heyyy. Having fun?"

        scene sfr4no5a
        with dissolve

        u "I am, but you don't seem to. *Chuckles*"

        scene sfr4no5b # nora no emotion
        with dissolve

        no "I've never been big on dances. And Chris seems to just want to go off and hang out with everyone that's not me."

        scene sfr4no5c
        with dissolve

        menu:
            "Agree with Nora":
                $ reputation.add_point(RepComponent.BOYFRIEND)

                u "Sorry, that must suck. He should be spending time with you."

                scene sfr4no5b
                with dissolve

                no "I know, but I know he's his own person so I don't want to be a bitch about it, but tonight is a dance like it should be about the person he's dancing with."

                scene sfr4no5c
                with dissolve

                u "I agree. I wish I could help you out."

                scene sfr4no5b
                with dissolve

                no "It's okay. Thanks for uhm, you know, talking."

                scene sfr4no5c
                with dissolve

                u "That's okay.."

                scene sfr4no5b
                with dissolve

                no "I should probably be getting back. I'll see you later."

                scene sfr4no5c
                with dissolve

                u "Yeah, see ya."

            "Defend Chris":
                $ reputation.add_point(RepComponent.BRO)

                u "I mean I get where he's coming from. He's got his own priorities to deal with too. And he's President of a frat-"

                scene sfr4no5b
                with dissolve

                no "Yup. I get it."

                scene sfr4no5c
                with dissolve

                u "I'm just saying, try to see it out from his perspective. That's all."

                scene sfr4no5b
                with dissolve

                no "I better get back, I'll see you around."

                scene sfr4no5c
                with dissolve

                u "Uh, okay then."

                scene sfr4no5b
                with dissolve

                no "Bye."

    elif not CharacterService.is_mad(nora):
        scene sfr4no5b
        with dissolve

        no "Hey."

        scene sfr4no5c
        with dissolve

        u "You okay?"

        scene sfr4no5b
        with dissolve

        no "Yeah... Is there anything you wanted?"

        scene sfr4no5c
        with dissolve

        u "No, uhm just wanted to check how you're doing."

        scene sfr4no5b
        with dissolve

        no "Oh, well I should probably get back. Bye."

        scene sfr4no5c
        with dissolve

        u "Yeah uhm... bye."

    else:
        scene sfr4no5d # nora annoyed
        with dissolve

        no "Uh, yeah?"

        scene sfr4no5e
        with dissolve

        u "Just wanted to say hi."

        scene sfr4no5d
        with dissolve

        no "I should be getting back to Chris."

        scene sfr4no5e
        with dissolve

        u "Uh... okay."

        scene sfr4no5d
        with dissolve

        no "Bye."

        scene sfr4no5e
        with dissolve

        u "Bye."

    jump labelfr4gymentrance

    ### LOCATION 3: GYM LEFT SIDE
label fr4riley1:
    $ freeroam4.add("riley")

    scene sfr4ri34 #fpp Aubrey and Riley are taking pictures together and posing by kissing each other on the cheek.

    pause 0.5

    scene sfr4ri35 # fpp close up riley looking at mc
    with dissolve

    ri "[name]! Come here. Come take a photo."

    scene sfr4ri35a
    with dissolve

    u "Uhhh..."

    scene sfr4ri36 # fpp aubrey close up smiling at mc
    with dissolve

    au "Come on! You can get in the middle."

    scene sfr4ri36a
    with dissolve

    u "Okay."

    # photo sounds #check - add capture.mp3 sound file
    scene sfr4ri37 # mc in the middle photo pose 1 (friendly)
    with dissolve

    pause 0.5

    play sound sound.capture
    scene sfr4ri37 # mc in the middle photo pose 1 (friendly)
    with flash

    pause 0.5

    scene sfr4ri37a  # mc in the middle photo pose 2 (arms around aubrey and rileys hips they come close)
    with dissolve

    pause 0.5

    play sound sound.capture
    scene sfr4ri37a  # mc in the middle photo pose 2 (arms around aubrey and rileys hips they come close)
    with flash

    pause 0.5

    scene sfr4ri37b  # mc in the middle photo pose 3 (they both kiss him on the cheek)
    with dissolve

    pause 0.5

    play sound sound.capture
    scene sfr4ri37b
    with flash

    pause 0.5

    scene sfr4ri38 # ffp close up riley smiling at you standing next to you
    with dissolve

    ri "I'm gonna go grab a drink, guys."

    scene sfr4ri38a
    with dissolve

    u "Alright, I'm gonna look around some more."

    scene sfr4ri39 #ffp lcose up aubrey looking at you  smiling
    with dissolve

    au "Have fun you guys. I'm gonna take some more pictures."
    jump labelfr4gymleft

label fr4aubrey1:
    $ freeroam4.add("aubrey")

    if "riley" in freeroam4:
        scene sfr4ri39b # aubrey flirty

        au "*Chuckles* Weren't you gonna look around some more?"

        scene sfr4ri39c
        with dissolve

        u "I did... and now I'm back, haha."

    else:
        scene sfr4ri39
        with dissolve

        au "Heyyy!"

        scene sfr4ri39a
        with dissolve

        u "Hey!"

    u "You look good tonight."

    scene sfr4ri39b
    with dissolve

    au "Thanks, you don't look so bad yourself."

    scene sfr4ri39c
    with dissolve

    u "You and Riley seem really close, you know."

    scene sfr4ri39
    with dissolve

    au "Honestly she's so cute. I thought she was super innocent and shy when I first met her but she's almost as wild as me, haha."

    scene sfr4ri39a
    with dissolve

    u "Reaaally? That's a high bar. *Laughs*"

    scene sfr4ri39b
    with dissolve

    au "*Laughs* You wouldn't believe it."

    scene sfr4ri39c
    with dissolve

    u "Well, enjoy taking some more pictures. You better tag me on Kiwii, haha."

    if CharacterService.is_friend(aubrey):
        scene sfr4ri39
        with dissolve

        au "*Chuckles* Of course. I'll see you later."

    else:
        scene sfr4ri39b
        with dissolve

        au "You sure you wanna leave already?"

        scene sfr4ri39c
        with dissolve

        u "Uhhh-"

        scene sfr4ri40 #tpp showing aubrey whispering in your ear
        with dissolve

        au "*Whispers* How about you follow me into the bathroom?"

        scene sfr4ri39c
        with dissolve

        menu:
            "Alright, let's go":
                $ reputation.add_point(RepComponent.BRO)
                $ sceneList.add("v7_aubrey")

                u "Yeah, alright. Let's go."

                if is_censored:
                    call screen censored_popup("labelfr4hallwaybathroom")

                scene sfr4ri41 # tppAubrey and MC walk towards the bathroom.
                with dissolve

                pause 0.5

                label brbj:
                    scene sfr4ri42 # fpp # in the bathroom looking down at your pants where aubrey is on her knees in front of you about to open your pants
                    with fade

                    au "Can I get a taste?"

                    scene sfr4ri42a #aubrey pulls down mcs pants
                    with dissolve

                    pause 0.5

                    scene sfr4ri42b # penis kissing / licking 1
                    with dissolve

                    play sound sound.kiss

                    pause 0.5

                    scene ri42vid # aubrey blowjob slow
                    with dissolve

                    u "Damn. ahh fuck."

                    " "

                    scene ri42vidperspective # aubrey blowjob slow perspective
                    with dissolve

                    u "You're so fucking good at this..."

                    " "

                    scene ri42vidfast # aubrey blowjob fast
                    with dissolve

                    u "Oh my god, keep going."

                    " "

                    scene ri42vidperspectivefast # aubrey blowjob fast perscpective
                    with dissolve

                    u "Fuck, I'm gonna cum!"

                    " "

                    scene sfr4ri43 # cumshot in air
                    with flash

                    u "Ahhh fuck. Mmmmm."

                    scene sfr4ri44 # cum on aubreys face, flirty smiling
                    with flash

                    au "*Grins* Seemed like you enjoyed it."

                    scene sfr4ri44c
                    with dissolve

                    au "*Gulp*"

                    u "That was amazing. I love how wild you are."

                    scene sfr4ri44b
                    with dissolve

                    au "Alright, I better get cleaned up. I guess I'll see you later"

                    scene sfr4ri44c
                    with dissolve

                    u "*Chuckles* You're really something else..."

                    scene sfr4ri44b
                    with dissolve

                    au "Oh, I know."

                    $ renpy.end_replay()

                    jump labelfr4hallwaybathroom

            "I'm not really feeling it":
                $ reputation.add_point(RepComponent.TROUBLEMAKER)

                scene sfr4ri39d # aubrey a bit disappointed
                with dissolve

                au "Oh yeah, of course. Well I'll see you later then."

                scene sfr4ri39e
                with dissolve

                u "Yeah uhm, bye."

    jump labelfr4gymleft

label fr4aubrey2:
    if hcGirl == "chloe":
        if "riley" in freeroam4:
            scene fr4gymleftnochloenoriley
        else:
            scene fr4gymleftnochloe

    elif hcGirl == "riley":
        if "chloe" in freeroam4:
            scene fr4gymleftnochloenoriley
        else:
            scene fr4gymleftnoriley

    else:
        if "riley" in freeroam4 and "chloe" in freeroam4:
            scene fr4gymleftnochloenoriley
        elif "riley" in freeroam4:
            scene fr4gymleftnoriley
        elif "chloe" in freeroam4:
            scene fr4gymleftnochloe
        else:
            scene fr4gymleft

    u "(I should talk to some of the other people here as well.)"

    jump labelfr4gymleft

label fr4chloe1:
    $ freeroam4.add("chloe")
    $ freeroam4.add("grayson")

    if preventgrayson:
        $ v7_chloesad = True

    scene sfr4cl47 #Ryan and Chloe are having a heated argument.

    cl "Are you fucking kidding me, Ryan? You're so full of shit."

    scene sfr4cl48 #close up ryan looking  annoyed at chloe
    with dissolve

    ry "Just calm the fuck down Chloe."

    scene sfr4cl49 #close up chloe angry looking at ryan
    with dissolve

    cl "No. I will not calm down!"

    scene sfr4cl49a
    with dissolve

    u "Hey, what happened?"

    scene sfr4cl49b # chloe looking at you mad
    with dissolve

    cl "This asshole called me a whore on Kiwii."

    scene sfr4cl48
    with dissolve

    ry "You are a whore!"

    scene sfr4cl49
    with dissolve

    cl "Fuck you, Ryan."

    scene sfr4cl49a
    with dissolve

    menu:
        "Defend Chloe":
            $ CharacterService.set_relationship(chloe, Relationship.FRIEND, mc)
            $ CharacterService.remove_mood(chloe, Moods.MAD)
            $ reputation.add_point(RepComponent.BOYFRIEND)
            $ reputation.add_point(RepComponent.TROUBLEMAKER)

            scene sfr4cl48a
            with dissolve

            u "Leave her alone, man."

            scene sfr4cl48d # ryan looking at you annoyed
            with dissolve

            ry "It's true..."

            scene sfr4cl49
            with dissolve

            cl "I'm out of here."

            scene sfr4cl49f # chloe gone
            with fade

            pause 0.5

            scene sfr4cl48b # looking at you with an intense smile
            with dissolve

            ry "Bitches be crazy."

            scene sfr4cl48c
            with dissolve

            u "Shut up, man. Not cool."

        "Say nothing":
            $ reputation.add_point(RepComponent.BRO)

            scene sfr4cl49
            with dissolve

            cl "I'm out of here."

            scene sfr4cl49f # chloe gone
            with fade

            pause 0.5

            scene sfr4cl48b # looking at you with an intense smile
            with dissolve

            ry "Bitches be crazy."

            scene sfr4cl48c
            with dissolve

            u "Right..."

    jump labelfr4gymleft

label fr4ryan1:
    $ freeroam4.add("ryan")

    if hcGirl == "chloe":
        if "riley" in freeroam4:
            scene fr4gymleftnochloenoriley
        else:
            scene fr4gymleftnochloe

    elif hcGirl == "riley":
        if "chloe" in freeroam4:
            scene fr4gymleftnoriley
        else:
            scene fr4gymleftnochloenoriley

    else:
        if "riley" in freeroam4 and "chloe" in freeroam4:
            scene fr4gymleftnochloenoriley
        elif "riley" in freeroam4:
            scene fr4gymleftnoriley
        elif "chloe" in freeroam4:
            scene fr4gymleftnochloe
        else:
            scene fr4gymleft

    u "(Ryan seems busy DJing, I'll talk to him later.)"

    jump labelfr4gymleft

label fr4ryan3:
    if hcGirl == "chloe":
        if "riley" in freeroam4:
            scene fr4gymleftnochloenoriley
        else:
            scene fr4gymleftnochloe

    elif hcGirl == "riley":
        if "chloe" in freeroam4:
            scene fr4gymleftnochloenoriley
        else:
            scene fr4gymleftnoriley

    else:
        if "riley" in freeroam4 and "chloe" in freeroam4:
            scene fr4gymleftnochloenoriley
        elif "riley" in freeroam4:
            scene fr4gymleftnoriley
        elif "chloe" in freeroam4:
            scene fr4gymleftnochloe
        else:
            scene fr4gymleft

    $ freeroam4.add("ryan")

    u "(Not sure I could handle more Ryan right now.)"

    jump labelfr4gymleft

    ### LOCATION 4: GYM RIGHT SIDE
label fr4cameron1:
    $ freeroam4.add("cameron")

    scene sfr4ca1 # Cameron is turned away and the random girl looks annoyed

    rg2 "I don't even know why you asked me if you're not going to even dance with me."

    scene sfr4ca2 # close up cameron looking up annoyed
    with dissolve

    ca "God, all you do is complain."

    if joinwolves:
        scene sfr4ca2b # cameron looking at you pissed
        with dissolve

        ca "What do you want, loser?"

        scene sfr4ca2c
        with dissolve

        u "I just-"

        scene sfr4ca2b
        with dissolve

        ca "Get the fuck out of here, you Wolf nerd."

        scene sfr4ca3 # girl looking at cameron, annoyed
        with dissolve

        rg2 "Cameron, be nice!"

        scene sfr4ca2d # cameron turns around enraged
        with dissolve

        ca "Will you shut the fuck up, bitch?!"

        scene sfr4ca2e
        with dissolve

        u "Jesus..."

    else:
        scene sfr4ca2f # cameron looking at you with intense smile
        with dissolve

        ca "Sup."

        scene sfr4ca2g
        with dissolve

        u "Hey, man. What's up?"

        scene sfr4ca2f
        with dissolve

        ca "Just trying to get a moment of peace and quiet while my date keeps nagging."

        scene sfr4ca3 # girl looking at cameron, annoyed
        with dissolve

        rg2 "Cameron, stop being so rude!"

        scene sfr4ca2d # cameron turns around enraged
        with dissolve

        ca "Will you shut the fuck up, bitch?!"

        scene sfr4ca2e
        with dissolve

        u "Jesus... I gotta go."

    jump labelfr4gymright

label fr4cameron2:
    if hcGirl == "lauren":
        scene fr4gymrightnolauren
    else:
        scene fr4gymright

    u "(Cameron doesn't seem to be in the greatest of moods. I feel like going back there isn't a smart move.)"

    jump labelfr4gymright

label fr4lauren1:
    $ freeroam4.add("lauren")

    if CharacterService.is_mad(lauren):
        scene sfr4la27a
        with dissolve

        u "(Lauren is mad at me, I should leave her alone)"

        jump labelfr4gymright

    else:
        scene sfr4la25 # fpp lauren & ms rose talking

        la "Yeah, I guess I was just having trouble with that one."

        scene sfr4la26 # close up ms rose looking at lauren smiling
        with dissolve

        ro "Well, you know my class is always open if you ever need help with anything."

        scene sfr4la27 # close up lauren looking at ms rose smiling
        with dissolve

        la "Thanks, I appreciate that."

        scene sfr4la27b # lauren smiling looking at you
        with dissolve

        la "Oh, hey [name]. How are you?"

        scene sfr4la27c
        with dissolve

        u "I'm good. How are you two tonight?"

        scene sfr4la27b
        with dissolve

        la "I'm great!"

        scene sfr4la26b # ms rose looking at you smiling eye brow raised
        with dissolve

        ro "Well, about as good as a glorified babysitter could be right now."

        scene sfr4la26c
        with dissolve

        u "Aw come on Ms. Rose, you've put up a pretty amazing event here!"

        scene sfr4la27 # close up lauren looking at ms rose smiling
        with dissolve

        la "Yeah, you've really done a great job!"

        scene sfr4la26
        with dissolve

        ro "Thanks, guys."

        scene sfr4la26a
        with dissolve

        menu:
            "Focus on Lauren":
                scene sfr4la27a
                with dissolve

                u "So uh... Lauren, you look great tonight."

                scene sfr4la27b
                with dissolve

                la "Thanks, you too."

                scene sfr4la26b
                with dissolve

                ro "Am I interrupting something here?"

                scene sfr4la27
                with dissolve

                la "Oh no, haha. Not at all."

                scene sfr4la27b
                with dissolve

                la "Ms. Rose and I were just talking about the last essay."

                scene sfr4la27c
                with dissolve

                u "Fun."

                scene sfr4la26b
                with dissolve

                ro "Do you have any thoughts on it?"

                scene sfr4la27c
                with dissolve

                u "Uhh... I really gotta get back to the dance."

                scene sfr4la26b
                with dissolve

                ro "*Chuckles* Of course you do."

                scene sfr4la27b
                with dissolve

                la "Bye, [name]."

            "Focus on Ms. Rose":

                u "So Ms. Rose, what was homecoming like when you were in college?"

                u "So like 5 years ago."

                scene sfr4la26b
                with dissolve

                ro "Haha, you're too kind. It was very similar, but our chaperone wasn't as amazing."

                scene sfr4la26c
                with dissolve

                u "*Laughs* How could anyone be?"

                scene sfr4la27b
                with dissolve

                la "Ms. Rose and I were just talking about the last essay."

                scene sfr4la27c
                with dissolve

                u "Fun."

                scene sfr4la26b
                with dissolve

                ro "Do you have any thoughts on it?"

                scene sfr4la26c
                with dissolve

                u "Uhh... I really gotta get back to the dance."

                scene sfr4la26b
                with dissolve

                ro "*Chuckles* Of course you do."

                scene sfr4la27b
                with dissolve

                la "Bye, [name]."
        jump labelfr4gymright

label fr4lauren2:
    if hcGirl == "lauren":
        scene fr4gymrightnolauren
    else:
        scene fr4gymright
        
    if CharacterService.is_mad(lauren):
        u "(Lauren is mad at me, I should leave her alone)"
    else:
        u "(I'd rather not talk about the economics essay I forgot to turn in.)"

    jump labelfr4gymright

label fr4msrose1:
    $ freeroam4.add("rose")

    scene sfr4la26b # ms rose looking at you smiling eye brow raised

    ro "Hey [name], how's your night?"

    scene sfr4la26c
    with dissolve

    u "Hey, Ms. Rose. It's really good. How are you?"

    scene sfr4la26b
    with dissolve

    ro "Well, about as good as a glorified babysitter could be right now."

    scene sfr4la26c
    with dissolve

    u "Aw come on Ms. Rose, you've put up a pretty amazing event here!"

    scene sfr4la26b
    with dissolve

    ro "Thanks."

    scene sfr4la26c
    with dissolve

    u "Is this what homecoming was like back when you were in college?"

    u "So like 5 years ago."

    scene sfr4la26b
    with dissolve

    ro "Haha, you're too kind. It was very similar, but our chaperone wasn't as amazing."

    scene sfr4la26c
    with dissolve

    u "*Laughs* How could anyone be?"

    scene sfr4la26b
    with dissolve

    ro "You know, I was talking to another student earlier about the last essay you guys had to write."

    scene sfr4la26c
    with dissolve

    u "Fun."

    scene sfr4la26b
    with dissolve

    ro "Do you have any thoughts on it?"

    scene sfr4la26c
    with dissolve

    u "Uhh... I really gotta get back to the dance."

    scene sfr4la26b
    with dissolve

    ro "*Chuckles* Of course you do."

    jump labelfr4gymright

label fr4msrose2:
    if hcGirl == "lauren":
        scene fr4gymrightnolauren
    else:
        scene fr4gymright

    u "(I'd rather not talk about the economics essay I forgot to turn in.)"

    jump labelfr4gymright

    ##### HALLWAY #####

    ### LOCATION 5: HALLWAYGYMEXIT

    ### LOCATION 6: HALLWAYBATHROOM

label fr4imre1:
    $ freeroam4.add("imre")

    scene sfr4im1 # fpp the bathroom, you can see legs in one of the stalls

    imre "Fuck yeah."

    unknown "*Moans* Fuck Mhmmm, yes!"

    if joinwolves:
        menu:
            "Say something to Imre":
                $ reputation.add_point(RepComponent.BRO)
                $ reputation.add_point(RepComponent.TROUBLEMAKER)

                u "*Laughs* Imre?"

                imre "[name]? That you?"

                u "Haha yeah. You sound pretty busy right now."

                imre "Haha yeah. Making the most out of homecoming. *Laughs*"

                unknown "*Loud moan* Ahhh!"

                u "Alright, I'll leave you two be, haha."

                imre "See you later, bro!"

                jump labelfr4hallwaybathroom

            "Leave them alone":
                $ reputation.add_point(RepComponent.BOYFRIEND)

                u "(I should probably leave these two alone.)"

                jump labelfr4hallwaybathroom

    else:
        u "(Ooops, I should probably leave these two alone.)"

        jump labelfr4hallwaybathroom

label fr4imre2:
    scene fr4hallwaybathroom

    u "(I think I've heard enough of Imre's moaning for now.)"

    jump labelfr4hallway

    ### LOCATION 7: HALLWAY
label fr4penelope1:
    $ freeroam4.add("penelope")

    scene sfr4pe24 #fpp penelope on hte phone turned away from you

    pe "What do you mean you got kicked out again? What happened?!"

    u "Hey."

    pe "That's crazy! I can't even believe that. They have to be insane. Ridiculous really."

    scene sfr4pe24a # penelope turns around and is abit surpsied
    with dissolve

    pe "Let me call you right back."

    scene sfr4pe24b #Penelope hangs up.
    with dissolve

    play sound "sounds/rejectcall.mp3"

    pause 0.5

    scene sfr4pe25 #fpp penelope  close up  cute smiling
    with dissolve

    pe "Heyyy!"

    scene sfr4pe25a
    with dissolve

    u "Hey, you okay? You sounded pretty upset on the phone there."

    scene sfr4pe25b # penelope serious
    with dissolve

    pe "Oh, yeah.. that. My friend she just... she just gets herself into trouble over and over again. I'd rather not get into it."

    scene sfr4pe25c
    with dissolve

    u "Yeah of course. Is she okay though?"

    scene sfr4pe25b
    with dissolve

    pe "Uhm, I guess. It's a bit complicated."

    scene sfr4pe25c
    with dissolve

    u "It's really nice of you to talk to her during homecoming, you know. You're a really good friend."

    scene sfr4pe25
    with dissolve

    pe "Thanks, I just want her to be alright."

    scene sfr4pe25a
    with dissolve

    u "Having a good night other than that?"

    scene sfr4pe25
    with dissolve

    pe "Yeah, yeah. It's been great."

    scene sfr4pe25a
    with dissolve

    menu:
        "I like your dress":
            $ reputation.add_point(RepComponent.BRO)

            u "I really like your dress."

            scene sfr4pe25
            with dissolve

            pe "Thanks! Took me forever to find something that I felt was good enough for the dance."

            scene sfr4pe25a
            with dissolve

            u "Haha, you chose well."

            scene sfr4pe25
            with dissolve

            pe "Yeah... You too."

            scene sfr4pe25a
            with dissolve

        "I'll let you get back":
            $ reputation.add_point(RepComponent.BOYFRIEND)

    u "Alright, well I'll let you get back to your friend. She sounds like she needs you more than I do."

    scene sfr4pe25
    with dissolve

    pe "Okay! Well I hope I see you around tonight."

    scene sfr4pe25a
    with dissolve

    u "Me too."

    jump labelfr4hallway

label fr4penelope2:
    if not hcGirl == "penelope":
        if "chloe" in freeroam4 and preventgrayson:
            scene fr4hallwaychloe
        else:
            scene fr4hallway
    else:
        if "chloe" in freeroam4 and preventgrayson:
            scene fr4hallwaynopenelopechloe
        else:
            scene fr4hallwaynopenelope

    u "(Penelope's on the phone, so I should probably leave her be.)"

    jump labelfr4hallway

label fr4chloe2:
    $ freeroam4.add("chloe2")

    if CharacterService.is_mad(chloe):
        scene sfr4cl53a # fpp close up chloe mad

        u "You okay?"

        scene sfr4cl53
        with dissolve

        cl "I really don't wanna talk right now."

        scene sfr4cl53a
        with dissolve

        u "You sure?"

        scene sfr4cl53
        with dissolve

        cl "Yes."

        scene sfr4cl53a
        with dissolve

        u "Alright..."

        jump labelfr4hallway

    else:
        scene sfr4cl53a # fpp close up chloe mad

        u "You okay?"

        scene sfr4cl53
        with dissolve

        cl "Ryan's just pissing me off. Why do people always have to be such assholes..."

        scene sfr4cl53a
        with dissolve

        u "Yeah... I'm sorry."

        scene sfr4cl53b #chloe no longer mad, emphatic, a bit cute
        with dissolve

        cl "It's not your fault..."

        cl "Thanks for looking after me."

        scene sfr4cl53c
        with dissolve

        u "Yeah of course. I-"

        scene sfr4cl53d # chloe looking at the wall where homecoming is on the other side
        with dissolve

        ro "*Muffled* And your homecoming queen is..."

        ro "*Muffled* Chloe Moralez!"

        scene sfr4cl53f # chloe smile but also a bit flustered and a bit worried
        with dissolve

        cl "Oh god, now I gotta go on stage like this."

        scene sfr4cl53g
        with dissolve

        menu:
            "You got this":
                $ reputation.add_point(RepComponent.BOYFRIEND)

                u "You got this."

                scene sfr4cl53f
                with dissolve

                cl "*Takes a deep breath* Yeah. You're right."

                cl "Thanks [name]. I'll see you later."

                scene sfr4cl53g
                with dissolve

                u "Yeah, no problem."

                scene sfr4cl53h # chloe gone
                with fade

                if hcGirl == "alone":
                    if not "crowning" in freeroam4:
                        u "(I guess I'll watch it with someone.)"
                        
                        scene sfr4stage4 #Chloe runs up on stage
                        with fade

                    else:
                        u "(I guess I'll go back.)"

                    jump fr4alonechloe

                elif hcGirl == "riley":
                    u "(I should probably get back to Riley.)"

                    scene sfr4stage4
                    with fade

                    jump fr4rileydatechloe

                elif hcGirl == "lauren":
                    u "(I should probably get back to Lauren.)"

                    scene sfr4stage4
                    with fade

                    jump fr4laurendatechloe

                elif hcGirl == "penelope":
                    u "(I should probably get back to Penelope.)"

                    scene sfr4stage4
                    with fade

                    jump fr4penelopedatechloe

            "Or we could just leave":
                $ reputation.add_point(RepComponent.TROUBLEMAKER)

                u "Or we could just leave right now and not look back..."

                scene sfr4cl53k # chloe flirty curious smile
                with dissolve

                cl "Are you serious?"

                scene sfr4cl53l
                with dissolve

                u "Yeah, come on."

                u "Who cares about homecoming anyways."

                scene sfr4cl53k
                with dissolve

                cl "Okay, let's go."

                scene sfr4cl53l
                with dissolve

                u "Really?"

                scene sfr4cl53k
                with dissolve

                cl "Yeah."

                jump fr4chloeending

label fr4chloe3:
    if not hcGirl == "penelope":
        if "chloe" in freeroam4 and preventgrayson:
            scene fr4hallwaychloe
        else:
            scene fr4hallway
    else:
        if "chloe" in freeroam4 and preventgrayson:
            scene fr4hallwaynopenelopechloe
        else:
            scene fr4hallwaynopenelope

    u "(Chloe said she doesn't wanna talk right now, I should respect that.)"

    jump labelfr4hallway

    ### LOCATION 8: HALLWAYCORNER

label fr4grayson1:
    $ freeroam4.add("grayson")

    scene sfr4gr1 # grayson about to spray the wall

    if joinwolves:
        u "What are you doing, Grayson?"

        scene sfr4gr1b # grayson looking at you annoyed intense
        with dissolve

        gr "What's up, pussy? You about to police my ass?"

        scene sfr4gr1c
        with dissolve

        u "What were you gonna spray on the wall?"

        scene sfr4gr1d # grayson looking at you angry/ intense smile
        with dissolve

        gr "Chloe's number!"

        scene sfr4gr1e
        with dissolve

        u "What? Why?"

        scene sfr4gr1d
        with dissolve

        gr "She fucks with me, I fuck with her."

        scene sfr4gr1e
        with dissolve

        menu:
            "Don't do that":
                $ reputation.add_point(RepComponent.BOYFRIEND)

                u "Hey man, don't do that. That's a real dick move."

                scene sfr4gr1b
                with dissolve

                gr "She deserves it."

                scene sfr4gr1c
                with dissolve

                u "Whatever she did, I'm sure she doesn't deserve this."

                if reputation() == Reputations.CONFIDENT:
                    $ preventgrayson = True
                    call screen reputation_popup

                    scene sfr4gr1b
                    with dissolve

                    gr "Fine, whatever."

                    scene sfr4gr2 # grayson stands up
                    with dissolve

                    gr "See you, loser."

                    scene sfr4gr2a #grayson gone
                    with fade

                    pause 0.5

                else:
                    scene sfr4gr1b
                    with dissolve

                    gr "I don't give a shit what you think."

                    gr "Now fuck off."

                    scene sfr4gr1c
                    with dissolve

                    u "*Sighs* Fine."

            "Alright, enjoy":
                $ reputation.add_point(RepComponent.TROUBLEMAKER)

                u "Alright, enjoy."

                scene sfr4gr1d
                with dissolve

                gr "Oh, I will."

    else:

        u "What's up, Grayson? What are you up to?"

        scene sfr4gr1d
        with dissolve

        gr "What's up, bro? How you doing?"

        scene sfr4gr1e
        with dissolve

        u "Good, good. What are you gonna spray on the wall?"

        scene sfr4gr1d # grayson looking at you angry/ intense smile
        with dissolve

        gr "Chloe's number!"

        scene sfr4gr1e
        with dissolve

        u "What? Why?"

        scene sfr4gr1d
        with dissolve

        gr "Bro come on, you know the rules. She fucks with me, I fuck with her."

        scene sfr4gr1e
        with dissolve

        menu:
            "Don't do that":
                $ preventgrayson = True
                $ reputation.add_point(RepComponent.BOYFRIEND)

                u "Hey man, don't do that. That's a real dick move."

                scene sfr4gr1b
                with dissolve

                gr "She deserves it."

                scene sfr4gr1c
                with dissolve

                u "Whatever she did, I'm sure she doesn't deserve this."

                scene sfr4gr1b
                with dissolve

                gr "Fine, whatever."

                scene sfr4gr2 # grayson stands up
                with dissolve

                gr "I'm outta here."

                scene sfr4gr2a #grayson gone
                with fade

                pause 0.5

            "Alright, enjoy":
                $ reputation.add_point(RepComponent.TROUBLEMAKER)

                u "Alright, enjoy."

                scene sfr4gr1d
                with dissolve

                gr "Oh, I will."

    jump labelfr4hallway

label fr4lockerroom:
    scene insidelockerroom

    u "(No one in here.)"

    jump labelfr4hallwaycorner

label fr4lockerroomchloe:
    if not "chloe2" in freeroam4:
        $ freeroam4.add("chloe2")

        scene sfr4cl50 # mc knocking on lockerroom

        u "Chloe? You in there?"

        if CharacterService.is_mad(chloe):
            scene sfr4cl51 # fpp close up of the door
            with dissolve

            cl "What do you want, [name]?!"

            u "Can I come in?"

            pause 1.0

            u "Chloe?"

            pause 0.5

            cl "No. Leave me alone!"

            u "Chloe, come on!"

            cl "I said leave me alone!"

            u "Fine..."

            jump labelfr4hallwaycorner

        else:
            scene sfr4cl51 # fpp close up of the door
            with dissolve

            cl "What do you want, [name]?"

            u "Can I come in?"

            pause 1.0

            u "Chloe?"

            pause 0.5

            cl "Okay."

            scene sfr4cl52a # fpp close up chloe sad, miserable
            with dissolve

            u "Ryan really got to you, huh?"

            scene sfr4cl52
            with dissolve

            cl "I don't care about Ryan. Did you see what someone did to the wall?!"

            cl "That's my number! Free blowjobs... everyone thinks I'm a fucking whore!"

            cl "What have I done to fucking deserve this?!"

            scene sfr4cl52a
            with dissolve

            u "I don't think you're a whore..."

            scene sfr4cl52
            with dissolve

            cl "Thanks..."

            scene sfr4cl52a
            with dissolve

            u "I think you're amazing and everyone who thinks something else can fuck off."

            scene sfr4cl52b # chloe sad smile
            with dissolve

            cl "You're cute."

            if not "crowning" in freeroam4:
                scene sfr4cl52d # chloe lookig at the wall where prom is on the other side
                with dissolve

                ro "*Muffled* And your homecoming queen is..."

                ro "*Muffled* Chloe Moralez!"

                u "See? Everyone voted for you. The people love you. So forget about all those guys."

                scene sfr4cl52b
                with dissolve

                cl "I don't know if I can go on stage right now."
                
            else:
                scene sfr4cl52b
                with dissolve
                
                cl "I don't know if I can go back right now."

            scene sfr4cl52c
            with dissolve

            menu:
                "Of course you can":
                    $ reputation.add_point(RepComponent.BOYFRIEND)

                    u "Of course you can."

                    scene sfr4cl52b
                    with dissolve

                    cl "*Takes a deep breath* Yeah. You're right. I got this."

                    cl "Thanks [name]. I'll see you later."

                    scene sfr4cl52c
                    with dissolve

                    u "Yeah, no problem."

                    scene sfr4cl52e # chloe gone
                    with fade

                    if hcGirl == "alone":
                        u "(I guess I'll watch it with someone.)"
                        scene sfr4stage4 #Chloe runs up on stage
                        with fade

                        jump fr4alonechloe

                    elif hcGirl == "riley":
                        u "(I should probably get back to Riley.)"

                        scene sfr4stage4
                        with fade

                        jump fr4rileydatechloe

                    elif hcGirl == "lauren":
                        u "(I should probably get back to Lauren.)"

                        scene sfr4stage4
                        with fade

                        jump fr4laurendatechloe

                    elif hcGirl == "penelope":
                        u "(I should probably get back to Penelope.)"

                        scene sfr4stage4
                        with fade

                        jump fr4penelopedatechloe

                    elif hcGirl == "emily":
                        u "(I should probably get back to Emily.)"

                        scene sfr4em20
                        with fade
                        jump fr4emilydate
                        
                "Let's get out of here":
                    $ reputation.add_point(RepComponent.TROUBLEMAKER)

                    u "You don't have to. Let's just get out of here."

                    if reputation() == Reputations.POPULAR:
                        call screen reputation_popup

                        scene sfr4cl52b
                        with dissolve

                        cl "Really?"

                        scene sfr4cl52c
                        with dissolve

                        u "Yeah, come on."

                        u "Who cares about homecoming anyways."

                        scene sfr4cl52b
                        with dissolve

                        cl "Okay, let's go."

                        scene sfr4cl52c
                        with dissolve

                        u "Really?"

                        scene sfr4cl52b
                        with dissolve

                        cl "Yeah."

                        jump fr4chloeending

                    else:
                        scene sfr4cl52b
                        with dissolve

                        cl "That's cute [name], but I think I have to go up there."

                        scene sfr4cl52c
                        with dissolve

                        u "You sure?"

                        scene sfr4cl52b
                        with dissolve

                        cl "Yeah."

                        scene sfr4cl52e # chloe gone
                        with fade

                        if hcGirl == "alone":
                            u "(I guess I'll go back.)"

                            jump fr4alonechloe

                        elif hcGirl == "riley":
                            u "(I should probably get back to Riley.)"

                            jump fr4rileydatechloe

                        elif hcGirl == "lauren":
                            u "(I should probably get back to Lauren.)"

                            jump fr4laurendatechloe

                        elif hcGirl == "penelope":
                            u "(I should probably get back to Penelope.)"

                            jump fr4penelopedatechloe

                        elif hcGirl == "emily":
                            u "(I should probably get back to Emily.)"

                            scene sfr4em20
                            with fade
                            jump fr4emilydate

                        else:
                            pause 0.75 
                            jump labelfr4hallwaycorner

    else:
        scene sfr4cl51

        if CharacterService.is_mad(chloe):
            u "(I better leave her alone.)"

        else:
            u "(I don't really see the need to go in the right now.)"

        jump labelfr4hallwaycorner

    ##### OUTSIDE #####

    ### LOCATION 9: STAIRS
    
label fr4emily1:
    $ freeroam4.add("emily")
    $ forgiveemily = True

    scene sfr4em29 # showing mc and emily mc stnading behind emily, she doesn't see him

    pause 0.5

    scene sfr4em29a # mc sits down next to her
    with dissolve

    u "Hey, why you out here? You okay?"

    scene sfr4em30 # fpp close up emily looking at you a bit sad
    with dissolve

    em "Yeah, I'm fine. Guess I'm just bored."

    scene sfr4em30a
    with dissolve

    u "You sure?"

    scene sfr4em30
    with dissolve

    em "*Takes a deep breath*"

    em "Honestly, I'm just kind of sad you didn't take me to homecoming."

    scene sfr4em30a
    with dissolve

    u "Really? You're upset about that?"

    scene sfr4em30
    with dissolve

    em "Well, yeah. I don't know. I know we're not dating, but..."

    em "It just hurts."

    em "I'm sorry."

    scene sfr4em30a
    with dissolve

    u "It's okay..."

    u "It's just... sometimes it's really weird between us."

    scene sfr4em30
    with dissolve

    em "Yeah... I know what you mean."

    scene sfr4em30a
    with dissolve

    u "Yeah..."

    scene sfr4em30
    with dissolve

    em "You don't have to sit here with me."

    scene sfr4em30
    with dissolve

    u "I don't-"

    scene sfr4em30a
    with dissolve

    em "I need some alone time anyway... I'll see you around."

    scene sfr4em30
    with dissolve

    u "Oh... yeah, okay."

    jump labelfr4outsidestairs

label fr4emily2:
    scene fr4outsidestairs

    u "(Emily said she needed some alone time, so I better leave her be.)"

    jump labelfr4outsidestairs

    ### LOCATION 10: STREET
    
label fr4samantha1:
    $ freeroam4.add("samantha")

    scene sfr4sa1 #fpp from the side / behind Samantha and Sebastian outside. You can't see their mouthThey are smoking a blunt and laughing.

    se "Haha. This shit hit different today."

    sa "Haha you're telling me."

    se "Maaan."

    scene sfr4sa1a #Samantha points to the trees. Sebastian looks over in a blank stare.
    with dissolve

    sa "Wait, wait, wait, look, right there."

    se "What?... What is it?"

    scene sfr4sa1b # sam looks at sebestian , arm down
    with dissolve

    sa "Doesn't it look like they're alive? Like, like they're moving in the wind, like really moving?"

    scene sfr4sa2 #Samantha stands and slowly starts walking towards the trees. Sebastian still sitting down
    with dissolve

    pause 0.5

    scene sfr4sa2a #Sebastian also stands up and follows, sam stands in front of the trees
    with dissolve

    se "Hahahaha yeaaaah they are! They're like moving like walking hahaha."

    scene sfr4sa3 # a bit closeup they're both standing in front of the trees
    with dissolve

    sa "Yes! Haha you see it! I knew it!"

    u "Uhmmm- hey."

    scene sfr4sa3a # they're turning around  worried that he's an undercover cop
    with dissolve

    pause 0.5

    scene sfr4sa3b # tthey're looking at each other unsure now
    with dissolve

    u "Uhhhh Hello?"

    scene sfr4sa4 # close up sam unsure
    with dissolve

    se "Uhh hey man... are you uhhh... an undercover?"

    scene sfr4sa4a
    with dissolve

    u "An undercover?"

    scene sfr4sa5b # sam unsure
    with dissolve

    if not joinwolves:
        sa "Wait, I know you... or... do I know you?"

        scene sfr4sa4d # sebastian looking at sam
        with dissolve

        se "No Sam! That's why they're called undercover cops, they- they disguise themselves as people you know."

        scene sfr4sa4e
        with dissolve

    else:
        sa "Yeah... like an undercover cop?"

        scene sfr4sa5c
        with dissolve

    menu:
        "Play along":
            $ cop = True
            #If MC chooses to go along with it:

            u "Yep, I'm a cop."

            scene sfr4sa4b # sebastian worried
            with dissolve

            se "Oh shit."

            scene sfr4sa5 # close up samantha worried
            with dissolve

            sa "Are we under arrest? I really don't want to go to jail."

            scene sfr4sa5a
            with dissolve

            u "Look, I know you guys are smoking weed out here, but you're lucky because I'm feeling nice tonight. If you put the blunt out right now, I'll let you off."

            scene sfr4sa4b
            with dissolve

            se "Yes, sir."

            scene sfr4sa5
            with dissolve

            sa "Thanks officer. We promise it will never happen again."

            scene sfr4sa5a
            with dissolve

            u "Good, because I'll be back out here to check."

            scene sfr4sa4
            with dissolve

            se "Yes, sir."

            scene sfr4sa6 #mc walks away smirking
            with dissolve

            u "*Smirks*"

        "Tell them truth":
            u "I'm not a cop, haha."

            scene sfr4sa4
            with dissolve

            se "So you're not like working as a cop undercover?"

            scene sfr4sa4a
            with dissolve

            u "No."

            if not joinwolves:
                scene sfr4sa5c
                with dissolve

                u "And you're Cameron's sister right?"

                scene sfr4sa5d # sam high smile
                with dissolve

                sa "Ohhh, that's where I know you from."

                scene sfr4sa5e
                with dissolve

                u "Yeah..."
            
            scene sfr4sa4h #Sebastian holds out a blunt.
            with dissolve

            se "Soo uhm you want some? Haha."

            scene sfr4sa4j
            with dissolve

            u "Uhm, I'm good right now, but thanks."

            scene sfr4sa4h
            with dissolve

            se "You sure? We have plenty."

            scene sfr4sa4j
            with dissolve

            u "Yeah, I'm good. Just wanted to say hi. I'm gonna head back in."

            scene sfr4sa4h # seb smiling
            with dissolve

            se "Guess more for us then."

            scene sfr4sa4j
            with dissolve

            u "I'll leave you guys be."

            scene sfr4sa5d
            with dissolve

            sa "Byeee."

    jump labelfr4outsidestreet

label fr4samantha2:
    scene fr4outsidestreet

    if cop:
        u "*Chuckles* (I've already messed with them enough.)"

    else:
        u "(I don't really wanna smoke weed right now.)"

    jump labelfr4outsidestreet

##### ENDINGS ###

############### SCENE 46 LAUREN ENDING
label fr4laurenending:
    $ ending = "lauren"

    scene sfr4la28 #fpp lauren walks towards the bed.
    with dissolve

    pause 0.5

    la "Come here."

    scene sfr4la29 # fpp close up Lauren in bed ideally with her head in her hand with one elbow on the bed leaning towards you, smiling cute
    with fade

    la "Wanna know something?"

    scene sfr4la29a
    with dissolve

    u "What's that?"

    scene sfr4la29
    with dissolve

    $ grant_achievement("slow_and_steady")

    la "I read that... if you cuddle in your underwear it increases the serotonin levels in your brain, which in turns means you live a longer, happier life."

    scene sfr4la29a
    with dissolve

    u "Haha and where did you read this?"

    scene sfr4la29
    with dissolve

    la "In some magazine at the doctors' office."

    scene sfr4la29a
    with dissolve

    u "Well I guess if a magazine at the doctor's said it, it must be true. haha."

    scene sfr4la29
    with dissolve

    la "I think we should try it..."

    scene sfr4la29a
    with dissolve

    u "You sure?"

    scene sfr4la29b # lauren starts taking her dress off
    with dissolve

    la "*Chuckles* Yeah."

    scene sfr4la30 # showing mc and Lauren lying close to each other in their underwear
    with fade

    u "Hey.. I think I feel it..."

    scene sfr4la31 # fpp close up lauren smiling curious
    with dissolve

    la "What?"

    scene sfr4la31a
    with dissolve

    u "The serotonin levels in my brain. *Laughs*"

    scene sfr4la31b # lauren cute
    with dissolve

    la "*Laughs* I swear that's a real thing."

    scene sfr4la31c
    with dissolve

    u "It definitely is."

    scene sfr4la30c # lauren and mc kiss
    with dissolve
    play sound sound.kiss

    pause 0.5

    scene sfr4la31b
    with dissolve

    la "I love this."

    scene sfr4la31c
    with dissolve

    u "Me too."

    scene sfr4la30c # lauren and mc kiss
    with dissolve
    play sound sound.kiss

    pause 0.5

    scene sfr4la31
    with fade

    la "It's getting pretty late-"

    scene sfr4la31a
    with dissolve

    u "Oh yeah... I should probably go..."

    scene sfr4la31d # lauren flirting
    with dissolve

    la "Or..."

    la "You could just turn the lights off..."

    jump v8start

############### SCENE 47 RILEY ENDING (LEWD & NON-LEWD)
label fr4rileyending:
    scene sfr4ri52 #MC and Riley are walking back through the dorm hallways.
    with fade

    play music "music/m16punk.mp3"

    queue music [ "music/mchill1.mp3", "music/m7punk.mp3" ]

    if (Moods.TEASED in riley.mood or CharacterService.is_fwb(riley)):
        ri "Sooo homecoming was pretty fun... but I bet the night could get even better."

        scene sfr4ri52a # mc turns his face towards her
        with dissolve

        u "Better how?"

        scene sfr4ri53a # fpp riley close up smile like Maro when he's confused why you're not getting it # mouth closed eye brow raise
        with dissolve

        pause 0.5

        u "*Chuckles* Ohhh..."

        scene sfr4ri53
        with dissolve

        ri "Took you a while there, haha."

    else:
        ri "Can't wait to get back, haha."

        scene sfr4ri52a # mc turns his face towards her
        with dissolve

        u "Yeah... all this dancing was exhausting *Chuckles*."

label fr4rileyending2:
    scene sfr4ri57 # tpp you grabbing something on Rileys desk and Riley sitting on her bed looking at you, you're not looking at her
    with fade

    $ ending = "riley"

    pause 0.5

    scene sfr4ri57a #riley pats the bed,looking at you smiling
    with dissolve

    $ grant_achievement("playing_with_fire")
        
    ri "Sit down with me for a second."

    scene sfr4ri57b #mc walks towards her
    with dissolve

    u "*Chuckles* I was just about to."

    scene sfr4ri54 #tpp  mc sits next to Riley looking at her she smiles at him at bit devious like she's excited to tell him a surprise
    with dissolve

    u "So, what's up?"

    if (Moods.TEASED in riley.mood or CharacterService.is_fwb(riley)):
        scene sfr4ri55  #tpp close up riley whispers into your ear
        with dissolve

        ri "*Whispers* I have a surprise for you."

        jump v8start

    else:
        scene sfr4ri56 # ffp close up riley a bit nervous but also excited to tell you a secret
        with dissolve

        ri "Can I tell you a secret?"

        scene sfr4ri56a
        with dissolve

        u "Of course."

        scene sfr4ri56
        with dissolve

        ri "I-"

        jump v8start

############### SCENE 48 CHLOE ENDING
label fr4chloeending:
    #At the dance MC approaches whoever his date his.

    if hcGirl == "emily" or hcGirl == "lauren" or hcGirl == "riley" or hcGirl == "penelope":
        scene sfr4cl54 # tpp you approaching chloe on the stairs outside
        with fade

        u "Okay, I've told my date that I wasn't feeling so well and had to leave early."

        scene sfr4cl55 # fpp close up chloe devious/ flirty smile
        with dissolve

        cl "Oh, you're bad."

        scene sfr4cl55a
        with dissolve

        u "I'm just comforting a friend."

        scene sfr4cl55
        with dissolve

        cl "Sure you are."

    scene sfr4cl56 #tpp  mc and chloe walking through the park
    with fade

    play music "music/m16punk.mp3"

    queue music [ "music/mchill1.mp3", "music/m7punk.mp3" ]

    $ ending = "chloe"

    u "You know I still haven't actually seen your room."

    scene sfr4cl57 #fpp close up chloe smiling eyebrow raised
    with dissolve

    cl "Well you're about to."

    scene sfr4cl57a
    with dissolve

    u "I bet it's messy."

    scene sfr4cl57b #chloe laughing taking offense
    with dissolve

    cl "*Laughs* Hey!"

    cl "I assure you it's cleaner than your dorm."

    scene sfr4cl57c
    with dissolve

    u "*Laughs* Wow, low blow. Imre made it messy, not me."

    scene sfr4cl57
    with dissolve

    cl "Keep telling yourself that."

    scene sfr4cl58 # tpp from behind: chloe opens the door to her room mc following
    with fade

    $ grant_achievement("homecoming_queen")

    u "So this is your infamous room?"

    cl "In all its glory."

    scene sfr4cl59 #fpp close uochloe smiling at you a bit flirty
    with dissolve

    cl "I'm going to freshen up real quick."

    scene sfr4cl59a
    with dissolve

    u "Sure."

    play sound "sounds/dooropen.mp3"
    scene sfr4cl60 # fpp showing chloe slightly opening a door inside her room  about to walk inside
    with dissolve

    u "You have an en-suite???"

    scene sfr4cl60a # chloe turns her head around cheeky smile
    with dissolve

    cl "*Chuckles* I'll be back in a minute."

    play sound "sounds/doorclose.mp3"

    scene sfr4cl61 # tpp mc walking towards her night stand with a book on it."
    with dissolve

    u "(I wonder what she's reading.)"

    scene sfr4cl61a # mc sits down on the bed about to grab the book from the nightstand
    with dissolve

    pause 0.5

    scene sfr4cl61b # tpp mc looking at the book in his hand while holding the book
    with dissolve

    u "(Hmm... Colony Crisis. Interesting.)"

    play sound "sounds/dooropen.mp3"
    scene sfr4cl61c #showing mc, mc looks up at the door
    with dissolve

    "*Door opening*"

    # towel drop sound #check - add towel.mp3 sound file
    play sound "sounds/towel.mp3"

    if is_censored:
        call screen censored_popup("v8s2_nsfwSkipLabel1")

    scene sfr4cl62 #Chloe steps out of the bathroom. We see her feet and a bathrobe drop to the floor.
    with dissolve

    " "
    jump v8start

############### SCENE 48 AMBER ENDING
label fr4amberending:
    $ ending = "amber"

    scene sfr4am12f # amber flirtatious
    with dissolve

    am "I have another idea of what might feel good..."

    jump v8start
