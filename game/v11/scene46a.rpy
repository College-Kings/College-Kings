# SCENE 46a) Diner with Aubrey
# Locations: sidewalk restraunt
# Characters: MC (Outfit 3), Penelope (outfit1), Samantha (outfit1), Charli (outfit 1), Cameron (outfit1), Emily (outfit2), Josh(outfit1), Riley(Outfit 2), amber(outfit 2), Mr Lee(outfit 1), imre(outfit 1), ryan(outfit 1), nora(Outfit 2), chloe(outfit 1), chris(outfit 1), ms rose (outfit 1)
# Time: evening
label v11_dinner_with_aubrey:

    scene v11dwa1 # FPP. Show Aubrey slight smile mouth closed
    with dissolve
    u "So, do you like fancy restaurants like this?"
    play music music.ck1.v10.Track_Scene_40_2 fadein 2
    scene v11dwa1a # FPP. # FPP. Show Aubrey slight smile mouth open
    with dissolve

    au "When I'm not the one paying, of course I do. *Laughs* What's not to like? It beats fast food any day and I definitely can't cook myself..."

    scene v11dwa1
    with dissolve

    u "Haha, I know. I can't cook for shit either."

    scene v11dwa1a
    with dissolve

    au "We're gonna have to show some love to our Pimp Daddy Mr. Lee for spoiling all of us little sugar babies."   

    scene v11dwa1
    with dissolve

    u "*Chuckles* Why does Mr. Lee have to be our pimp daddy?"

    scene v11dwa1a
    with dissolve

    au "What else do you call a man that spends a bunch of money on fancy dinners for people he hardly knows, just so they can have a good time getting to know each other?"

    scene v11dwa1
    with dissolve

    u "Okay, I see where you're coming from now. *Chuckles* Not gonna lie though, and I don't know if I'm just now seeing it or if he's always been this way, but Mr. Lee is a really cool guy."

    scene v11dwa1a
    with dissolve

    au "He's changed a lot since I started school at SVC, but he's definitely one of my favorite professors for sure. He's always been really fair."

    scene v11dwa1
    with dissolve

    u "Ryan and Imre got into it again the other day, and all Mr. Lee did was try really hard to get them to work past their issues."
    u "It didn't work, but he still tried his best. I was impressed."

    scene v11dwa1a
    with dissolve

    au "You want me to pass him a note letting him know you like him or something? *Chuckles*"

    scene v11dwa1b # Fpp. same 1, different pose, mouth closed
    with dissolve

    u "What? *Chuckles* I'm just saying, he's actually a good dude."

    scene v11dwa1c # Fpp. same 1, different pose, mouth open
    with dissolve

    au "Haha, I'm teasing. You're right, though. He's not a complete cornball. Anyways, I'm so ready to get out of London."

    scene v11dwa1b
    with dissolve

    u "Really? How come?"

    scene v11dwa1c
    with dissolve

    au "Because Paris is the only reason I came on this trip. *Chuckles* I want to get a really nice outfit from a Lew's in Paris."
    au "They have some really rare pieces and my sister is also doing a shoot there. So, the whole gang will be able to meet her."
    au "I'm really hoping we can go to her shoot because then we could take some professional pictures together."

    scene v11dwa1b
    with dissolve

    u "Holy shit, that definitely sounds like fun."

    scene v11dwa1c
    with dissolve

    au "Oh, it will be. Hopefully we make it in time because I really think you'll like my sister. *Chuckles*"

    scene v11dwa1b
    with dissolve

    u "*Chuckles* How come?"

    scene v11dwa1c
    with dissolve

    au "Imagine me, but prettier, and a bit more blunt."

    scene v11dwa1b
    with dissolve

    u "Wait... More blunt than you? That can't be possible. *Laughs*"

    scene v11dwa1a
    with dissolve

    au "Hard to believe, isn't it? When you're a Kiwii model though, and you are your own boss, no one can really tell you what to do."

    scene v11dwa1
    with dissolve

    u "Hmm... Must be nice."

    scene v11dwa1a
    with dissolve

    au "I may just follow in her steps and become a Kiwii model if the whole acting thing doesn't work out. *Chuckles*"

    scene v11dwa1
    with dissolve

    u "*Laughs* Well, you can do whatever you want. It's your life and you're the only one who has to live it."

    scene v11dwa1a
    with dissolve

    au "Haha, thanks."

    scene v11dwa1
    with dissolve

    if CharacterService.is_friend(aubrey):
        scene v11dwa1e # FPP. Same 1, different pose, neutral look, mouth open
        with dissolve
        au "I'm surprised you're not like all the other guys."

        scene v11dwa1d # FPP. Same 1, different pose, neutral look, mouth closed
        with dissolve

        u "What do you mean?"

        scene v11dwa1e
        with dissolve

        au "Well, you aren't jumping to have sex with every girl you see. *Chuckles* You actually care about who you sleep with."

        scene v11dwa1d
        with dissolve

        u "You're sure your sister is more blunt than you?"

        scene v11dwa1e
        with dissolve

        au "Haha, maybe not. But, I mean it, [name]. It's surprising. I don't know if it makes you a good guy, interesting, or just lame."

        scene v11dwa1d
        with dissolve

        u "Well, two of those weren't insults so I'd rather go with those."

        scene v11dwa1e
        with dissolve

        au "*Chuckles* I'm still deciding. It kinda surprised me to hear what Charli had to say about you."

        scene v11dwa1d
        with dissolve

        u "Yeah? What'd he say?"

        scene v11dwa1e
        with dissolve

        au "He basically just said that you're a man whore."

        scene v11dwa1
        with dissolve

        u "Well, that's definitely worse than being lame I guess. *Chuckles*"

        scene v11dwa1e
        with dissolve

        au "I still don't know why you two can't get along. You could easily be friends. All it takes is for one of you to apologize."

        scene v11dwa1
        with dissolve

        u "Yeah, one of us."

        scene v11dwa1c
        with dissolve

        au "That \"one\" could easily be you."

        scene v11dwa1b
        with dissolve

        u "Yeah. It could be."

        scene v11dwa1c
        with dissolve

        au "Will it be? Can you at least attempt it?"

        menu:
            "Yes":
                scene v11dwa1b
                with dissolve
                
                u "If I get the chance, yeah. I'll try and make peace with him."

                scene v11dwa1c
                with dissolve

                au "I've decided then, you're officially a good guy. *Chuckles* I might have gone with lame if you had said no to me."

                scene v11dwa1b
                with dissolve

                u "*Laughs*"

            "No":
                scene v11dwa1b
                with dissolve

                u "I don't know exactly what you've heard, but I'm most certainly not the one that needs to apologize."

                scene v11dwa1c
                with dissolve

                au "It's not about who needs to, it's about who will."

                scene v11dwa1b
                with dissolve

                u "Well, it won't be me."

                scene v11dwa1c
                with dissolve

                au "Lameeeee."

                scene v11dwa1b
                with dissolve

                u "How am I lame?"

                scene v11dwa1b
                with dissolve

                au "*Chuckles* Because you two are like Chloe and Nora 2.0."

                scene v11dwa1c
                with dissolve

                u "*Laughs* Okay, that was pretty funny."
                
    else:
        scene v11dwa1
        with dissolve

        u "It's been really nice to vibe with you lately, Aubrey."

        scene v11dwa1a
        with dissolve

        au "Well, if you continue to play your cards right, maybe we can vibe some more while we're in Paris. *Chuckles*"

        menu:
            "Be More than friends":
                scene v11dwa1
                with dissolve
                u "That's actually something I've been wanting to talk to you about."

                scene v11dwa1a
                with dissolve

                au "What?"

                scene v11dwa1
                with dissolve

                u "Us?"

                scene v11dwa1a
                with dissolve

                au "What do you mean by \"us\"?"

                scene v11dwa1
                with dissolve

                u "Well, we've been messing around for a while now and I was hoping we could do more than just mess around. Maybe go on a real date or really get to know each other?"

                scene v11dwa1f # FPP. SHow aubrey looking down covering her face
                with dissolve

                au "..."

                u "Aubrey?"

                scene v11dwa1g # FPP. Show aubrey laughing, mouth open
                with dissolve

                au "*Laughs* I'm sorry... I couldn't resist laughing. You're joking right? You know I'm not interested in a relationship."

                scene v11dwa1d
                with dissolve

                u "I know you said that before, but I thought that maybe things felt a little different lately."

                if reputation() == Reputations.CONFIDENT:
                    scene v11dwa1e
                    with dissolve

                    au "Oh shit, you're actually being serious. Well, like I said, I'm not interested in being tied down right now. I enjoy being a free bird, [name]."

                else:
                    scene v11dwa1e
                    with dissolve

                    au "Someone's getting a little confident aren't they?"

                scene v11dwa1d
                with dissolve

                u "Yeah... I got it now. Sorry, haha."

                scene v11dwa1e
                with dissolve

                au "Haha, it's fine. Just don't make things all awkward now."

            "Stay FWB":
                scene v11dwa1d
                with dissolve

                u "Don't I always? *Chuckles*"

                scene v11dwa1e
                with dissolve

                au "*Chuckles* Yeah, you do. But the minute you start acting like you're my \"boyfriend\" or something, I'll have to cut you loose."

                scene v11dwa1d
                with dissolve

                u "Well, I wouldn't want that."

                scene v11dwa1e
                with dissolve

                au "I wouldn't either 'cause then I'd have to go push up on Pimp Daddy Mr. Lee."

                scene v11dwa1
                with dissolve

                u "Okay, I think you can stop with Pimp Daddy stuff now. *Chuckles*"

                scene v11dwa1a
                with dissolve

                au "Haha. As long as you keep me satisfied, [name]."

    scene v11dwa1c
    with dissolve

    au "Oh, look! The food's coming out."

    scene v11dwa1b
    with dissolve

    u "We didn't even order anything..."

    scene v11dwa1c
    with dissolve

    au "Oh yeah, Pimp Daddy-I mean... Mr. Lee, ordered for everybody. *Chuckles*"

    scene v11dwa1b
    with dissolve

    u "Wow, you really can't stop thinking about Mr. Lee as your pimp, can you? *Laughs*"

    scene v11dwa1c
    with dissolve

    au "Haha, stop it."

    scene v11dwa3 # TPP. Show MC and aubrey talking and eating
    with dissolve

    pause 2

    scene v11dwa4 # TPP. Show Riley and Amber talking and eating
    with fade

    pause 2

    scene v11dwa5 # TPP. Show Lindsey and charli talking and eating
    with fade

    pause 2

    scene v11dwa6 # FPP. Show aubrey, laid back slightly hands on stomach mouth open
    with dissolve

    au "Wow, I'm so full... That was amazing, I'm gonna go thank Mr. Lee."

    scene v11dwa7 # FPP. Show aubrey walking off towards Mr. Lee
    with dissolve

    u "Haha, alright. You go do that."

    u "(*Laughs* She's definitely got a little thing for Mr. Lee.)"

    scene v11dwa8 # FPP. Show Mr Lee infront of the students, mouth open
    with dissolve

    lee "Alright students, we're going to enjoy one final walk back to the hotel."

    scene v11dwa8a # FPP. Show Mr Lee infront of the students, mouth closed
    with dissolve

    u "(A nice dinner and a relaxing walk... Not a bad night, Mr. Lee.)"

    scene v11dwa9 # TPP. Show some of the students walking out the restraunt
    with dissolve

    pause 1

    scene v11dwa10 # TPP. Show Nora,chris, Mc, Chloe walking alond the sidewalk (camera from slightly above so you can't tell everyone else isn't with them)
    with dissolve

    pause 1

    stop music fadeout 3
    jump v11_walking_back