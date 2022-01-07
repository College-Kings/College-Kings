# SCENE 11: Airport San Vallejo
# Locations: Airport San Vallejo Gate
# Characters: MC (Outfit: 5), MR. LEE (Outfit: 1), MS. ROSE (Outfit: 1), RILEY (Outfit: 2), CHARLI (Outfit: 1)
# Time: Afternoon

label v14s11:
    play music "music/v11/Track Scene 14.mp3" fadein 2

    scene v14s11_1 # TPP. MC walks into the airport and closes his eyes as he takes a deep breath, slight smile
    with dissolve

    u "*Deep breath*"

    scene v14s11_1a # TPP. same as v14s11_1 mc walks further away from the gate
    with dissolve

    u "(It feels so good to be back on home turf.)"

    if v13_charli_exposed:
        scene v14s11_2 # FPP. MC looks over sees and overhears Mr. Lee talking to Ms. Rose, Mr. Lee. extends one hand out slightly palm up, no expression mouth open, Ms. Rose. no expression, mouth closed
        with dissolve

        lee "Right, well... I need to be on my way! It's insisted that I attend Charli's meeting with the dean."

        scene v14s11_2a # FPP. same as v14s11_2 Mr. Lee no hand gesture mouth closed, Ms Rose. mouth open
        with dissolve

        ro "Bruce, it is very late and you are very tired. Do you really feel that now is the best time?"

        scene v14s11_2
        with dissolve

        lee "Whether it is the right time or not, that student will not be on this campus another night. Not if I have anything to do with it."

        scene v14s11_2a
        with dissolve

        ro "*Sighs* Very well..."

        scene v14s11_2
        with dissolve

        lee "Make sure the students all get home safe, will you?"

        scene v14s11_2a
        with dissolve

        ro "Of course, take care of yourself."

        scene v14s11_2
        with dissolve

        lee "I will."

        scene v14s11_2c # FPP. same as v14s11_2a Mr. Lee is walking away from Ms. Rose with his back turned, Ms Rose is looking at Mr. Lee, Ms. Rose mouth open, one hand pointing at Mr. Lee
        with dissolve

        ro "I'm serious Bruce!"

        scene v14s11_2d # FPP. same as v14s11_2c Mr. Lee raises an arm and hand above his head as he walks further away, Ms. Rose. mouth closed, no hand gesture.
        with dissolve

        lee "I am too!"

    else:
        if v13s20_bleach_suitcase:
            scene v14s11_3 #FPP. MC sees Charli with his bag leaving the airport, without speaking to anyone, Charli's back is turned
            with dissolve

        else:
            scene v14s11_3a #FPP. MC sees Charli with his bag leaving the airport, without speaking to anyone, Charli's back is turned
            with dissolve

        u "(He came into our lives with a bang, trying to show his ass off, and look at him now...)"
        u "(A sad dude, walking away all alone, just as he was when he first arrived.)"

        u "(Definitely didn't like the guy, but I do get this weird feeling seeing him go.)"

    scene v14s11_4 # FPP. Mc turns around and see's Riley approaching him, Riley looking at mc, Riley no expression, mouth closed
    with dissolve

    pause 0.75

    scene v14s11_4a # FPP. same as v14s11_4 Riley is now standing in front of mc, looking at mc, no expression, mouth open
    with dissolve

    ri "Are you thinking about him too?"

    scene v14s11_4b # FPP. same as v14s11_4 Riley mouth closed
    with dissolve

    u "Who?"

    scene v14s11_4a
    with dissolve

    ri "Charli?"

    scene v14s11_4b
    with dissolve

    u "A little bit..."

    scene v14s11_4c # FPP. same as v14s11_4a Riley slight smile, mouth open, hand gesture
    with dissolve

    ri "He definitely isn't the best human out there in my opinion. Even when I was giving him a chance, I knew that deep down."

    scene v14s11_4b
    with dissolve

    u "I knew that too, and that's exactly why-"

    scene v14s11_4a
    with dissolve

    ri "But..."

    scene v14s11_4c
    with dissolve

    ri "He did teach us a lot."

    scene v14s11_4b
    with dissolve

    u "*Scoffs* What did he possibly teach us?"

    scene v14s11_4d # FPP. same as v14s11_4c Riley eyebrow raised, different hand gesture
    with dissolve

    ri "You're telling me that Charli never said anything to you that made you think about the choices you've made or ponder about who you are as a person?"

    menu:
        "He did":
            $ add_point(KCT.BRO)

            scene v14s11_4b
            with dissolve

            u "I admit, he helped me do some self reflecting, but... I'm not giving him any more than that."

            scene v14s11_4c
            with dissolve

            ri "I wouldn't expect you to. He was worse to you than most of us."

        "He didn't":
            $ add_point(KCT.TROUBLEMAKER)

            scene v14s11_4b
            with dissolve

            u "Not at all. I'm completely content with all the choices I've made."

            scene v14s11_4a
            with dissolve

            ri "Well, maybe it was just me. *Chuckles*"

    scene v14s11_4e # FPP. same as v14s11_4b Riley places her hand on her head and closes her eyes for a second, mouth closed
    with dissolve

    u "You okay?"

    scene v14s11_4f # FPP. same as v14s11_4e Riley opens her eyes, mouth open
    with dissolve

    ri "Uhh, y-yeah. Just got dizzy for a second there..."

    scene v14s11_4e
    with dissolve

    u "Make sure you're taking care of yourself, red."

    scene v14s11_4g # FPP. same as v14s11_4c Riley no hand gesture
    with dissolve

    ri "I am, I just need to head back home."

    scene v14s11_4h # FPP. same as v14s11_4g Riley has a concerned expression
    with dissolve

    ri "Aubrey invited me to stay over at the Chicks house, but I don't know if I wanna be involved in any of the drama."

    scene v14s11_4b
    with dissolve

    u "Then don't be a part of the drama and just enjoy Aubrey's company. Sounds like that's what she's inviting you over for."

    scene v14s11_4c
    with dissolve

    ri "Haha, you're right..."

    scene v14s11_4g
    with dissolve

    ri "Knowing Aubrey she probably doesn't wanna talk about that stuff right now either."
    ri "Being around her is probably the safest way to stay out of any Chicks drama. *Chuckles*"

    if riley.relationship.value >= Relationship.FWB.value:
        scene v14s11_4a
        with dissolve

        ri "I admit though, there's more than just one reason why I'm unsure about hanging with Aubrey."

        scene v14s11_4b
        with dissolve

        u "What's the other reason?"

        scene v14s11_4a
        with dissolve

        ri "I guess I just feel..."

        scene v14s11_4h
        with dissolve

        ri "I feel a little conflicted."

        scene v14s11_4b
        with dissolve

        u "About?"

        scene v14s11_4a
        with dissolve

        ri "*Sighs* I'm just gonna come right out and say it! I..."

        scene v14s11_4b
        with dissolve

        u "I'm listening..."

        scene v14s11_4i # FPP. same as v14s11_4a Riley is blushing, shy expression, slightly looking away from mc, mouth open
        with dissolve

        ri "I have feelings for her... Also you."

        scene v14s11_4a
        with dissolve

        ri "I'm not exactly sure what those feelings are just yet, but I know they exist. And they're the same feelings that I have for Aubrey too."

        scene v14s11_4b
        with dissolve

        u "I get it. You want to know what I want, right?"

        scene v14s11_4i
        with dissolve

        ri "I think it might help... Yeah."

        scene v14s11_4b
        with dissolve

        menu:
            "Like us both":
                $ add_point(KCT.BRO)

                scene v14s11_4b
                with dissolve

                u "Well, for starters... It means a lot to me to know that the feeling is mutual."

                scene v14s11_4c
                with dissolve

                ri "*Chuckles* Right..."

                scene v14s11_4j # FPP. same as v14s11_4c Riley increases to a half smile
                with dissolve

                u "Plus, I'm sure Aubrey would be more than happy to hear that you have feelings for her too."

                scene v14s11_4i
                with dissolve

                ri "Yeah... So..."

                scene v14s11_4b
                with dissolve

                u "I don't see how you having feelings for both of us is a problem. Is that supposed to be a problem?"

                scene v14s11_4k # FPP. same as v14s11_4c Riley has a slightly shocked expression, mouth open
                with dissolve

                ri "Wait... You're okay with that?!"

                scene v14s11_4j
                with dissolve

                u "Haha, why wouldn't I be? That's what life is all about right? Spending time with the people you like most?"

                scene v14s11_4l # FPP. same as v14s11_4k Riley mouth closed, increases to a full smile, no hand gesture
                with dissolve

                u "And if that means the three of us get to spend the most of our time together, I'm not complaining. *Chuckles* You're my two favorite ladies."

                scene v14s11_4m # FPP. same as v14s11_4l Riley mouth open, full smile, no hand gesture
                with dissolve

                ri "Wow..."

                scene v14s11_4l
                with dissolve

                u "Is that a good wow? *Laughs*"

                scene v14s11_4m
                with dissolve

                ri "I don't know, I mean- Yes! That was definitely a good wow..."

                ri "I guess I just didn't think you'd be open to something like that. It's kind of my fantasy..."

                scene v14s11_4l
                with dissolve

                u "Well, looks like your wet dreams are finally coming true. *Laughs*"

                scene v14s11_4n # FPP. same as v14s11_4m Riley non-aggressively shoves mc's shoulder
                with dissolve

                ri "Stop it, loser! I'm actually really relieved."

                scene v14s11_4l
                with dissolve

                u "Glad I could do that for you."

                scene v14s11_4m
                with dissolve

                ri "Haha, thanks. I'm going to go meet with Aubrey now."

                scene v14s11_5 # TPP. Riley kisses Mc's cheek
                with dissolve

                pause 0.75

                scene v14s11_4m
                with dissolve

                ri "I'll see you soon, handsome. Very soon..."

                scene v14s11_4l
                with dissolve

                u "Ha... Catch you later."
            
                scene v14s11_4o # FPP. same as v14s11_4 Riley's back is turned walking away from the mc, her face is not visible
                with dissolve

            "Pick one of us":
                $ add_point(KCT.TROUBLEMAKER)
                $ add_point(KCT.BOYFRIEND)

                scene v14s11_4b
                with dissolve

                u "I'll be honest, I like you a lot Riley. The feelings are definitely mutual and I'm really happy you told me, but relationship-wise..."

                u "I'm just not the sharing type, I guess."

                scene v14s11_4p # FPP. same as v14s11_4h Riley mouths is closed
                with dissolve

                u "I don't really know if I'd feel comfortable with the whole situation."

                scene v14s11_4h
                with dissolve

                ri "I... I completely understand. It definitely makes sense why you wouldn't want that. I just wanted to be honest with you."

                scene v14s11_4p
                with dissolve

                u "Of course, and thank you for that."

                scene v14s11_4q # FPP. same as v14s11_4a Riley slightly sad, mouth open
                with dissolve

                ri "Yeah, well... I'm gonna go and track down Aubrey then."

                scene v14s11_4r # FPP. same as v14s11_4q Rileys mouth is closed
                with dissolve

                u "Oh... Okay. See you later?"

                scene v14s11_4q
                with dissolve

                ri "Uh, yeah. Bye."

                scene v14s11_4r
                with dissolve

                u "See ya."

                scene v14s11_4o
                with dissolve

                u "(I don't think she liked hearing that answer.)"
        
    else:
        scene v14s11_4j
        with dissolve

        u "Exactly. So go do exactly that and enjoy yourself while you figure out what you wanna do."

        scene v14s11_4m
        with dissolve

        ri "Haha, okay. I'm gonna go do just that. I'll catch up with you soon?"

        scene v14s11_4l
        with dissolve

        u "Yeah, see you soon."

        scene v14s11_4o
        with dissolve

    u "(Guess I need to get home myself. I can barely think with all this jetlag.)"

    scene v14s11_6 # TPP. show mc walking through the airport, no expression, mouth closed
    with dissolve

    pause 0.75

    scene v14s11_6a # TPP. same as v14s11_6 Mc exiting the airport
    with dissolve

    pause

    stop music

    image act4intro = Movie(play="images/v14/Scene 11/Act_4_Intro.webm", loop=False)
    scene act4intro
    with fade
    
    pause 42.5
    
    stop music fadeout 3
    jump v14s12