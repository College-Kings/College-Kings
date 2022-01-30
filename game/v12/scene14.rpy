# SCENE 14: At the Cafe with Chloe
# Locations: Cafe
# Characters: CHLOE (Outfit: 5), MC (Outfit: 5), FRENCH WAITRESS (Outfit: 1), RILEY (Outfit: 2)
# Time: Morning
# Phone Images: rileycatacomb.webp - Riley selfie at the catacomb entrance with a street sign behind her with "CATACOMBS" written on it, Riley smiling, mouth closed

label v12_chloe_cafe:
    scene v12chc1 # TPP. Show MC and Chloe going into the cafe, both smiling, mouths closed
    with dissolve

    pause 0.75

    play music "music/v12/Track Scene 14.mp3" fadein 2

    scene v12chc2 # TPP. Show MC and Chloe approaching their table, both smiling, mouths closed
    with dissolve

    pause 0.75

    if chloe.relationship >= Relationship.FWB:
        scene v12chc3 # TPP. Show MC pulling Chloe's chair out so she can sit down, both smiling, mouths closed
        with dissolve

        pause 0.75

        scene v12chc4 # TPP. Show MC midway through sitting down on his chair, Chloe looking at MC, she is sitting down in her chair, both smiling, mouths closed
        with dissolve

        pause 0.75

    else:
        scene v12chc4a # TPP. Show MC and Chloe midway through sitting down, both smiling, mouths closed
        with dissolve

        pause 0.75
    
    scene v12chc5 # FPP. MC and Chloe sitting down in the cafe, both of them looking at each other, Chloe smiling, mouth open
    with dissolve

    cl "This is such a nice place! I feel like I'm underdressed... *Laughs*"

    if chloe.relationship >= Relationship.FWB:
        scene v12chc5a # FPP. Same as v12chc5, Chloe blushing, smiling, mouth closed, avoiding eye contact
        with dissolve

        u "Are you kidding? You look perfect. Like always."

        scene v12chc5b # FPP. Same as v12chc5a, Chloe smiling, mouth open, blushing, avoiding eye contact
        with dissolve

        cl "Thank you, Mr. Charming... *Chuckles*"

        scene v12chc5
        with dissolve

        cl "But really... I mean look at this place."

    scene v12chc5c # FPP. Same as v12chc5, Chloe mouth closed, smiling
    with dissolve

    u "Haha, I know what you mean... It is fancy here. A very \"French movie\" type of place."

    scene v12chc5
    with dissolve

    cl "*Chuckles* What does that even mean?"

    scene v12chc5c
    with dissolve

    u "I have no idea. *Chuckles*"

    scene v12chc5
    with dissolve

    cl "Haha... Hmm, Do you know what you want to eat?"

    scene v12chc5c
    with dissolve

    u "I'm in another country and have no idea what I'm reading half the time. Probably best to just tell them to surprise us. *Laughs*"

    scene v12chc5d # FPP. Same as v12chc5, different pose
    with dissolve

    cl "I'm sure they can speak English, this is a tourist spot, right?"

    scene v12chc5e # FPP. Same as v12chc5d, Chloe smiling, mouth closed
    with dissolve

    u "Guess we'll find out because here comes the waiter."

    scene v12chc6 # TPP. Show the waitress walking over to MC and Chloe's table, everyone smiling, mouths closed
    with dissolve

    pause 0.75

    scene v12chc7 # FPP. MC looking at the waitress, waitress looking at MC, waitress mouth open, slight smile, waitress standing next to their table
    with dissolve

    fwait "Bonjour, comment allez-vous?"

    scene v12chc7a # FPP. Same as v12chc7, waitress mouth closed, slight smile
    with dissolve

    u "Uhhh..."

    scene v12chc5f # FPP. Same as v12chc5, Chloe looking at the waitress' direction, Chloe slight smile, mouth open
    with dissolve

    cl "V-Very good. We um-"

    scene v12chc7b # FPP. Same as v12chc7, waitress lookign at Chloe's direction, waitress slight smile, mouth open
    with dissolve

    fwait "Parles-tu français?"

    scene v12chc5f
    with dissolve

    cl "Un peu."

    scene v12chc7b
    with dissolve

    fwait "Oooo, très bien."

    scene v12chc5e
    with dissolve

    u "The fu- You never told me you spoke French..."

    scene v12chc5d
    with dissolve

    cl "I don't speak French... I just remember a few things from my language class."

    scene v12chc7b
    with dissolve

    fwait "Que puis-je faire pour vous?"

    scene v12chc5f
    with dissolve

    cl "Umm..."

    scene v12chc5e
    with dissolve

    u "And... We found the extent of your French skills. *Laughs*"

    scene v12chc5f
    with dissolve

    cl "I'm sorry, but do you have a waiter that speaks English?"

    scene v12chc7b
    with dissolve

    fwait "I can go try to find one."

    scene v12chc5g # FPP. Same as v12chc5f, Chloe surprised, mouth closed
    with dissolve

    pause 0.75

    scene v12chc5h # FPP. Same as v12chc5f, Chloe slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v12chc7b
    with dissolve

    fwait "*Laughs* Anytime I spot tourists, I like to see just how much I can mess with them."

    scene v12chc5f
    with dissolve

    cl "*Chuckles* Well it was very convincing, I'm so sorry for assuming."

    scene v12chc7b
    with dissolve

    fwait "Haha, no it's fine. I'd assume you only spoke English."

    scene v12chc5f
    with dissolve

    cl "And you'd be right. *Chuckles*"

    scene v12chc7b
    with dissolve

    fwait "So, what can I get for the gorgeous couple?"

    if chloe.relationship >= Relationship.GIRLFRIEND:
        scene v12chc5i # FPP. Same as v12chc5, Show Chloe blushing, slight smile, avoiding eye contact, putting her hair behind her ear, mouth closed
        with dissolve

        u "Haha, why are you smiling?"

        scene v12chc7b
        with dissolve

        fwait "Was it something I said?"

        scene v12chc5j # FPP. Same as v12chc5f, Chloe still blushing, mouth open, slight smile, 
        with dissolve

        cl "It was actually, but not in a bad way. My handsome boyfriend here actually asked me out pretty recently and well... This is our first time out as an official couple. *Chuckles*"

        scene v12chc7b
        with dissolve

        fwait "Oh wow! Congrats... That's exciting stuff."

        scene v12chc5c
        with dissolve

        u "\"Handsome boyfriend\". Hmm... I like the sound of that."

        scene v12chc5
        with dissolve

        cl "*Chuckles*"

        scene v12chc7a
        with dissolve

        u "Alright, now... Since my amazing girlfriend's French is so bad-"

    else:
        scene v12chc5f
        with dissolve

        cl "Haha, he wishes we were a couple."

        scene v12chc5e
        with dissolve

        menu:
            "It'd be nice":
                $ add_point(KCT.BOYFRIEND)
                scene v12chc5c
                with dissolve

                u "Mmm, yeah... It'd be nice. *Chuckles*"

            "Not really":
                $ add_point(KCT.BRO)
                scene v12chc5c
                with dissolve

                u "I'd rather date a fishing pole."

                scene v12chc5
                with dissolve

                cl "A fishing pole? What on earth made you say that? *Chuckles*"

                scene v12chc5c
                with dissolve

                u "It was the first thing that came to mind. *Chuckles*"
        
        scene v12chc7a
        with dissolve

        u "But, since my friend's French is so bad-"

    scene v12chc5d
    with dissolve

    cl "Hey! *Chuckles*"

    scene v12chc7a
    with dissolve

    u "We had planned to just have you surprise us with whatever you thought we'd enjoy. As hungry as I am, I'm not very picky at the moment."

    scene v12chc7
    with dissolve

    fwait "I think I know exactly what to get for you two. If you're sure there's nothing specific you'd like, I can get it going for you guys."

    scene v12chc5f
    with dissolve

    cl "Nope, that'd be great. Thank you."

    scene v12chc6a # TPP. Same as v12chc6, waitress walking away, everyone smiling, mouths closed
    with dissolve

    pause 0.75

    scene v12chc5
    with dissolve

    cl "She was really sweet."

    scene v12chc5c
    with dissolve

    u "Yeah, she was cool."

    scene v12chc5k # FPP. Same as v12chc5, Chloe looking at MC, she is slightly worried, mouth open, different pose
    with dissolve

    cl "*Sighs* One more stop before we get back."

    scene v12chc5l # FPP. Same as v12chc5k, Chloe slightly worried, mouth closed
    with dissolve

    u "What's making you think about going back all of a sudden?"

    scene v12chc5k
    with dissolve

    cl "Well, after the stuff that went down on the carriage rides there's been something on my mind."

    scene v12chc5l
    with dissolve

    u "And what's that?"

    scene v12chc5k
    with dissolve

    cl "I... I think Lindsey's planning something. I'm not sure what, but I know it's something."

    scene v12chc5m # FPP. Same as v12chc5k, different pose
    with dissolve
    
    cl "One of the girls video called me the other day and said that Lindsey had been in contact with nearly everyone about something important, but she wouldn't say what."
    
    scene v12chc5k
    with dissolve
    
    cl "I know it can't be the names thing she brought up because I asked if that's what it was, and she said no."

    scene v12chc5l
    with dissolve

    u "Hmm... Did she give you any clues at all?"

    scene v12chc5m
    with dissolve

    cl "None, but it bothers me because Lindsey hasn't said anything to me about whatever it is that she's planning."

    scene v12chc5k
    with dissolve
    
    cl "Lindsey is a sweet girl, so I don't want to assume it's anything bad, but if it wasn't bad, I don't see why she wouldn't tell me."

    scene v12chc5l
    with dissolve

    u "What bad things could Lindsey do?"

    scene v12chc5k
    with dissolve

    cl "Well, that's what I've been thinking about. The worst thing she could be doing is getting girls to leave the sorority, and the least worst thing she could be doing is setting up some dumb prank."
    
    scene v12chc5m
    with dissolve

    cl "There's a lot of things that she could be doing that range in between those two things."

    scene v12chc5l
    with dissolve

    menu:
        "Tell her about Lindsey":
            $ add_point(KCT.TROUBLEMAKER)
            $ v12_told_chloe = True

            u "(I can't keep this from her.) *Sighs* There's something I need to tell you."

            scene v12chc5m
            with dissolve

            cl "What?"

            scene v12chc5n
            with dissolve

            u "Don't quote me, please. And I don't want you doing anything rash. Can you promise me you won't freak out?"

            scene v12chc5k
            with dissolve

            cl "You're making me nervous, [name]."

            scene v12chc5l
            with dissolve

            u "Just promise me you won't freak out."

            scene v12chc5
            with dissolve

            cl "For fucks sake... *Sighs* Fine, I won't freak out. Happy?"

            scene v12chc5o # FPP. Same as v12chc5, Chloe angry, mouth closed
            with dissolve
            
            if v11_lindsey_run and v11_told_aubrey:
                $ grant_achievement("thrown_to_the_lions")
            
            u "Good. Now, again, don't quote me. I'm not sure of all the details and I'm not even positive if this is truly her plan, but I heard that Lindsey's been considering running for President of the Chicks, against you."
           
            scene v12chc5p # FPP. Same as v12chc5o, Chloe angry, mouth open
            with dissolve

            cl "WHY THE FUCK WOULD SHE DO THAT!?"

            scene v12chc5o
            with dissolve

            u "Calm down, please... You said you wouldn't freak out."

            scene v12chc5p
            with dissolve

            cl "*Deep breath* Why, the fuck, would she do that?"

            scene v12chc5o
            with dissolve

            u "Something about the Chicks needing major changes in order to save the sorority from it's downhill spiral... And again, don't quote me."

            scene v12chc5p
            with dissolve

            cl "Wow... I really can't believe she'd actually do that."
            cl "You know what, I'm not gonna jump to any conclusions. If she really did plan on doing something like that she'd have to be a lunatic."

            scene v12chc5o
            with dissolve

            scene v12chc5p
            with dissolve

            cl "Rather than seeing how she can help she'd rather just take over? No way. This can't be real."

        "Don't tell her about Lindsey":
            u "(No way I'm telling her. She's not hearing that news from me.)"

            scene v12chc5n # FPP. Same as v12chc5m, Chloe slightly worried, mouth closed
            with dissolve

            u "I don't want to start making assumptions about what it could or couldn't be, so just try to think positive. Maybe she is doing some prank, haha..."

            scene v12chc5m
            with dissolve

            cl "Well, if I don't figure it out soon I'm gonna end up going crazy. I'll talk to Aubrey first and see if she's heard anything, and I guess if she hasn't then I'll just go to Lindsey myself."

    scene v12chc5o
    with dissolve

    u "(Okay, this is not going well.)"

    u "Why not just enjoy Europe like we discussed before?"

    scene v12chc5p
    with dissolve

    cl "It's kinda hard to relax with something like this lingering over my head."

    scene v12chc5c
    with dissolve

    u "Yeah I know, but look at what's right in front of you. A handsome man treating you to breakfast... Is that not a good enough distraction? *Chuckles*"

    scene v12chc5q # FPP. Same as v12chc5, Chloe rolling her eyes, mouth closed, slight smile
    with dissolve

    pause 0.75
    
    scene v12chc5
    with dissolve

    cl "For now."

    scene v12chc5c
    with dissolve

    u "If I'm not good enough, the food can be plan B. Here it comes now."

    scene v12chc6b # TPP. Same as v12chc6, waitress with food in her hand
    with dissolve

    pause 0.75

    scene v12chc7c # FPP. Same as v12chc7b, waitress holding food
    with dissolve

    fwait "Alrighty, you two. Here you guys go. I hope you enjoy."

    scene v12chc5f
    with dissolve

    cl "Thank you."

    scene v12chc5r # FPP. MC watches as Chloe is eating
    with dissolve

    pause 1

    scene v12chc8 # TPP. Show MC and Chloe both eating their dishes
    with dissolve

    pause 1

    scene v12chc6
    with dissolve

    pause 1

    scene v12chc9 # TPP. Show the waitress grabbing MC and Chloes' empty dishes, all smiling, mouths closed
    with dissolve

    pause 1

    scene v12chc5e
    with dissolve

    u "Finished stuffing your face? *Chuckles*"

    scene v12chc5d
    with dissolve

    cl "Haha, I am. Are you? Seems like you enjoyed yourself."

    scene v12chc5e
    with dissolve

    u "I could've enjoyed anything considering how hungry I was. *Chuckles*"

    scene v12chc5
    with dissolve

    cl "*Laughs* Alright... Ready to go?"

    scene v12chc5c
    with dissolve

    u "Yeah, let's go."

    scene v12chc5d
    with dissolve

    cl "Okay."

    scene v12chc5e
    with dissolve

    u "And hey, don't let any of that Lindsey stuff get to you."

    scene v12chc5d
    with dissolve

    cl "I know I shouldn't. I promise I won't go back and explode or anything. I'm gonna take some time to figure out what's going on."

    scene v12chc5e
    with dissolve

    u "That's a good idea."

    scene v12chc5c 
    with dissolve

    play sound "sounds/vibrate.mp3"

    u "Sorry, let me check this real quick."

    scene v12chc10 # TPP. Show MC sitting down, looking down at his phone, neutral expression, mouth closed
    with dissolve

    $ riley.messenger.newMessage("TREASURE HUNT TIME!", force_send=True)
    $ riley.messenger.addReply("Really... now?")
    $ riley.messenger.newMessage("Yep, and I'm already at the spot of the next clue... I think.")
    $ riley.messenger.newImgMessage("images/v12/Scene 14/rileycatacomb.webp") # Riley selfie at the catacomb entrance with a street sign behind her with the address of where she is at, Riley smiling, mouth closed
    $ riley.messenger.newMessage("Meet me here :)")
    $ riley.messenger.addReply("Okay, I'll be there soon.")

    label v12s14_PhoneContinueRiley:
        if riley.messenger.replies:
            call screen phone
        if riley.messenger.replies:
            u "(I should check my phone.)"
            jump v12s14_PhoneContinueRiley

    scene v12chc10
    with dissolve

    u "(This isn't that far.)"

    scene v12chc5c
    with dissolve

    u "Well, looks like I'm meeting Riley for our Mr. Lee hunt."

    scene v12chc5
    with dissolve

    cl "A Mr. Lee... hunt? What is that?"

    scene v12chc5e
    with dissolve

    u "Some little treasure hunt he has us doing for him while we're in Europe."

    scene v12chc5d
    with dissolve

    cl "*Laughs*"

    scene v12chc5e
    with dissolve

    u "What?"

    scene v12chc5
    with dissolve

    cl "Nothing, nothing... Enjoy. I'll catch you later."

    scene v12chc5c
    with dissolve

    u "Alright, catch you later."

    scene v12chc11 # TPP. Show Chloe walking away, MC still sitting down, watching as she leaves, both smiling, mouths closed
    with dissolve

    pause 0.75

    scene v12chc12 # TPP. Show MC getting up from his chairm, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v12chc13 # TPP. Show MC leaving the cafe, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v12chc14 # TPP. Show MC walking down the streets, slight smile, mouth closed
    with fade

    pause 0.75

    stop music fadeout 3

    jump v12_riddle_riley #scene 15