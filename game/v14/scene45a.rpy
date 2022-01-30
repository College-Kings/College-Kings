# SCENE 45a: Afternoon event
# Locations: Under a big tree in the park, Lindsey's room.
# Characters: MC (Outfit: 1), AMBER (Outfit: 3), LINDSEY (Outfit: 1)
# Time: Afternoon

label v14s45a:
    scene v14s45a_1 # FPP. MC looking at Amber, Amber looking away from MC, Amber neutral face, mouth closed.
    with dissolve

    u "Hey there. So, what's the news?"

    play music "music/v13/Track Scene 60_1.mp3" fadein 2

    if not v14_amber_clean:
        scene v14s45a_1a # FPP. Same as v14s45a_1, MC looking at Amber, Amber now looking at MC, Amber tired and high, Amber neutral expression, mouth open.
        with dissolve

        am "I just uh... I quit my job at Lew's."

        if v11_amber_sauna_convo:
            am "Guess you can't tease me about it anymore, haha."

        scene v14s45a_1b # FPP. Same as v14s45a_1a, Amber tired and high, neutral expression, mouth closed.
        with dissolve

        u "Just jumped right out and did it, huh? Why'd you quit?"

        scene v14s45a_1a
        with dissolve

        am "Just tired of it, honestly... It's not fun."

        am "I know it sounds kinda... Whatever, I think I'm gonna try to be a private dancer or something."

        scene v14s45a_1b
        with dissolve

        u "(Like a stripper?)"

        scene v14s45a_1a
        with dissolve

        am "I looked into a nightclub that's not too far from here. I could make really good money on the weekends."

        menu:
            "Not a bad idea":
                $ add_point(KCT.TROUBLEMAKER)
                scene v14s45a_1b
                with dissolve
               
                u "Doesn't sound like too bad of an idea, actually."

                scene v14s45a_1a
                with dissolve

                am "Really? You're cool with it? I mean, I know how it sounds at first but-"

                scene v14s45a_1b
                with dissolve

                u "Sure. I am cool with it as long as you're comfortable with it and it makes you happy. You know?"

                scene v14s45a_1a
                with dissolve

                am "Wow, haha. Thank you."

                am "That kinda changes how I feel. Like, I feel pretty good about things now."

                scene v14s45a_1b
                with dissolve

                u "Ha, good. I'm glad I could help."

            "Why a stripper?":
                $ add_point(KCT.BOYFRIEND)
                scene v14s45a_1b
                with dissolve
                
                u "Why the fuck are you becoming a stripper, Amber?"

                scene v14s45a_1a
                with dissolve

                am "Ugh... I knew you'd say that. It's not a stripper it's-"

                scene v14s45a_1b
                with dissolve

                u "A private dancer? Same thing. Now answer the question."

                scene v14s45a_1a
                with dissolve

                am "Well regardless of what you call it, I'm doing it 'cause I want to. I didn't think I needed anyone's permission to do that."

                scene v14s45a_1b
                with dissolve

                u "You don't, but... You had a good, solid job and you're throwing it away for this?"

                scene v14s45a_1a
                with dissolve

                am "I wasn't happy at Lew's and this dancing job... It seems like something I'll enjoy."

                scene v14s45a_1b
                with dissolve

                u "*Sighs* Alright. Let's hope so."

                scene v14s45a_1a
                with dissolve

                am "*Sighs* You're an ass, do you know that?"

                scene v14s45a_1b
                with dissolve

                u "I know. *Chuckles*"

                scene v14s45a_1a
                with dissolve

                am "*Sighs* Haha..."

    else:
        scene v14s45a_1c # FPP. Same as v14s45a_1, Amber looking at MC, Mc looking at Amber, Amber has on a nice pretty red lipstick, Amber slight smile, mouth open.
        with dissolve

        am "I got a promotion at Lew's..."

        scene v14s45a_1d # FPP. Same as v14s45a_1c, Amber slight smile, mouth closed.
        with dissolve

        u "Promotion?! Amber! That's..."

        u "Promotion to what?"

        scene v14s45a_1c
        with dissolve

        am "I'm now the \"Assistant to the Manager\"."

        scene v14s45a_1d
        with dissolve

        u "Wait... The same manager that was being a dick to you that one day?"

        scene v14s45a_1c
        with dissolve

        am "Haha, yeah that's the one."

        am "Turns out that he was just seeing how much bullshit I could take. He thinks I could stay with the company long-term. If I wanted to of course."

        scene v14s45a_1d
        with dissolve

        u "Wow..."

        menu:
            "Make a joke":
                $ add_point(KCT.TROUBLEMAKER)

                scene v14s45a_1d
                with dissolve

                u "So, let me get this straight..."

                u "First, you just work at the rich kid shop, start wearing the rich kid clothes, and now you're moving up in the ranks?"

                u "Should I call you Ma'am now, when I stop by?"

                scene v14s45a_1c
                with dissolve

                am "You're an ass, you know that?"

                scene v14s45a_1d
                with dissolve

                u "Haha, I learned from the best though."

                scene v14s45a_1c
                with dissolve

                am "Haha, okay dickhead..."

                am "When I become CEO and you need a job, I'll show you what an ass I can be."

                scene v14s45a_1d
                with dissolve

                u "Oh wow. I'm scared."

            "Be supportive":
                $ add_point(KCT.BOYFRIEND)

                scene v14s45a_1d
                with dissolve
        
                u "I'm so proud of you, Amber."

                scene v14s45a_2 # TPP. Show MC holding Amber's hand, both slight smile mouth closed.
                with dissolve

                pause 0.5

                scene v14s45a_1e # FPP. Same as v14s45a_1c, Amber's arm moved slightly forward to show that she is holding MC's hand, Slight smile, mouth closed.
                with dissolve

                u "You're really on the right track, I think. At this rate, I'll be asking you for a job at Lew's one day. *Chuckles*"

                scene v14s45a_1f # FPP. Same as v14s45a_1e, Amber slight smile, mouth open.
                with dissolve

                am "*Laughs*"

    scene v14s45a_3 # TPP. Camera view from the park infront of them. MC and Amber looking at the Camera. Amber laying her head on MC's shoulder.
    with dissolve

    stop music fadeout 3
    
    play music "music/v14/Track Scene 45a_slow.mp3" fadein 2

# -Note for music; This is where the slow version of "Blanket" by Van Stee comes into play, see Mozzart for questions-
# -Waiting on song to be ready. Song should start playing here.-

    pause 0.75

    scene v14s45a_3a # TPP. Same as v14s45a_3, Amber slight smile, mouth open, MC slight smile, mouth closed.
    with dissolve

    am "Can I be honest with you?"

    scene v14s45a_3b # TPP. Same as v14s45a_3a, Amber slight smile, mouth closed, MC slight smile, mouth open.
    with dissolve

    u "Of course."

    scene v14s45a_3a
    with dissolve

    am "I appreciate you, a lot."

    am "You're like, a blanket."

    scene v14s45a_3b
    with dissolve

    u "Ha, thank you?"

    scene v14s45a_3a
    with dissolve

    am "I mean, like... You're nice, and warm, like a blanket that wraps me up tight and makes me feel safe."

    scene v14s45a_3
    with dissolve

    u "(Holy shit, that's the cutest thing I've ever heard.)"

    scene v14s45a_3a
    with dissolve

    am "A security blanket of some sorts... *Chuckles* Fucking it all up or doing it all perfectly, at the end of the day you've still got me feeling safe and warm."

    if amber.relationship >= Relationship.FWB:
        scene v14s45a_4 # TPP. Upclose of MC looking into Amber's eyes and Amber looking into MC's eyes, MC's finger lifting up Amber's chin, both slight smile, mouth closed.
        with dissolve

        pause 0.75

        play sound "sounds/kiss.mp3"

        scene v14s45a_4a # TPP. Same as v14s45a_4, Amber and MC kissing.
        with dissolve

        pause 

    scene v14s45a_3c # FPP. Same as v14s45a_3b, MC and Amber looking at each other, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v14s45a_1e
    with dissolve

    u "Do you really feel like that?"

    scene v14s45a_1g # FPP. Same as v14s45a_1f, Amber now with a fake playful angry face, mouth open
    with dissolve

    am "I do, and... It takes a lot for me to say that, so don't take it lightly."

    scene v14s45a_1h # FPP. Same as v14s45a_1g, Amber now with a fake playful angry face, mouth closed
    with dissolve

    u "Haha, I won't. I promise. Thank you for saying that."

    scene v14s45a_1f
    with dissolve

    pause 0.75

    scene v14s45a_5 # TPP. Amber reaching behind the tree they are sitting under where we can't see, MC confused face, mouth closed, Amber slight smile, mouth closed.
    with dissolve

    pause 

    scene v14s45a_1i # FPP. Same as v14s45a_1f, Amber holding a bottle of champagne, slight smile, mouth open.
    with dissolve
    
    am "Here's a little surprise for us."

    scene v14s45a_1j # FPP. Same as v14s45a_1i, Amber slight smile, mouth closed.
    with dissolve

    u "Oh, wow!"

    scene v14s45a_1i
    with dissolve

    am "I have to run soon, but I wanna mark the occasion with a celebratory sip."

    scene v14s45a_1j
    with dissolve

    u "Sounds perfect, haha."

    scene v14s45a_1i
    with dissolve

    am "Okay, cheers!"

    scene v14s45a_1j
    with dissolve

    u "Cheers to you!"

    scene v14s45a_3d # FPP. Same as v14s45a_3c, Amber and MC high fiving as they look at each other, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v14s45a_3e # FPP. Same as v14s45a_3d, Amber taking a sip from the Champagne bottle, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v14s45a_3f # FPP. Same as v14s45a_3e, Amber handing the bottle to MC, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v14s45a_3g # FPP. Same as v14s45a_3f, MC taking a sip from the Champagne bottle, both slight smile, mouth closed.
    with dissolve

    pause

    scene v14s45a_1d
    with dissolve

    u "Mmm, not bad."

    scene v14s45a_1c
    with dissolve

    am "Hell yeah, haha. I'm out of here on a high note."

    am "We'll catch up soon, okay?"

    scene v14s45a_1d
    with dissolve

    u "Sounds like a plan, yeah."

    scene v14s45a_1c
    with dissolve

    am "Bye!"

    scene v14s45a_1k # FPP. Same as v14s45a_1j, Amber starting to get up, slight smile, mouth closed.
    with dissolve
    
    pause 0.75

    scene v14s45a_1l # FPP. Same as v14s45a_1k, Amber walking off, slight smile, mouth closed.
    with dissolve

    pause 0.75

    stop music fadeout 3
    play music "music/v13/Track Scene 59_1.mp3" fadein 2

    scene v14s45a_6 # FPP. MC looking out at the park
    with dissolve

    if (v14_help_lindsey and not v14_lindsey_sell) and not v14_date_distraction: #choosing the concert to distract Chloe
        play sound "sounds/vibrate.mp3"

        u "(Let's check it out.)"

        scene v14s45a_7 # TPP. MC looking at his phone, slight smile, mouth closed.
        with dissolve

        $ lindsey.messenger.newMessage("Hey! Chloe is getting ready to leave for the concert, now's the perfect time to make a dent in her pockets.")
        $ lindsey.messenger.addReply("Roger that, OMW")

        label v14s45a_PhoneContinue:
        if lindsey.messenger.replies:
            call screen phone
        if lindsey.messenger.replies:
            u "(I should reply to Lindsey.)"
            jump v14s45a_PhoneContinue

        scene v14s45a_7a # TPP. Same as v14s45a_7, MC putting his phone away, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v14s45a_8 # TPP. MC starting to stand up, slight smile, mouth closed
        with dissolve

        pause 0.75

        scene v14s45a_9 # TPP. MC walking down the sidewalk near the park, slight smile, mouth closed
        with fade

    elif v14_date_distraction: #choosing to ditch the date you set up with Chloe to steal money
        play sound "sounds/call.mp3"

        pause 0.75

        scene v14s45a_7
        with dissolve

        u "Perfect timing..."

        scene v14s45a_7b # TPP. Same as v14s45a_7, MC holding the phone to his ear, slight smile, mouth open.
        with dissolve

        u "Hello?"

        scene v14s45a_10 # TPP. Show Lindsey in her room with the phone to her ear, Slight smile, mouth open.
        with dissolve

        li "Hey, now's the perfect time."

        scene v14s45a_10a # TPP. Same as v14s45a_10, Lindsey Slight smile, mouth closed.
        with dissolve

        u "For?"

        scene v14s45a_10
        with dissolve

        li "The Chloe, distraction? C'mon now..."

        scene v14s45a_10a
        with dissolve

        u "Yeah, yeah... I was just testing you. *Chuckles*"

        u "Call me in 5, I am going to start heading over..."

        scene v14s45a_10
        with dissolve

        li "Perfect! See you soon..."

        scene v14s45a_10a
        with dissolve

        u "Cya!"

        play sound "sounds/rejectcall.mp3"

        scene v14s45a_7a
        with dissolve

        pause 0.75

        scene v14s45a_8
        with dissolve

        pause 0.75

        scene v14s45a_9
        with dissolve
    
    elif v14_lindsey_sell: #helping Lindsey sell her car.
        play sound "sounds/call.mp3"

        pause 0.75

        scene v14s45a_7
        with dissolve

        u "Perfect timing..."

        scene v14s45a_7b
        with dissolve

        u "Hello?"

        scene v14s45a_10
        with dissolve

        li "Hey, we need to go ahead and take pictures of my car if we're planning on selling it. Think you can come meet me and take some now?"

        scene v14s45a_10a
        with dissolve

        u "Yeah, I can. Where are you?"

        scene v14s45a_10
        with dissolve

        li "In the parking lot off Wayside?"

        scene v14s45a_10a
        with dissolve

        u "I was just there, haha."

        scene v14s45a_10
        with dissolve

        li "Oh damn, sorry."

        if lindsey.relationship >= Relationship.FWB:
            scene v14s45a_10a
            with dissolve

            u "Don't apologize. I'll be right there."

            scene v14s45a_10
            with dissolve

            li "Thank you, handsome..."

            scene v14s45a_10a
            with dissolve

            u "Yeah, yeah..."

        else:
            scene v14s45a_10a
            with dissolve

            u "*Sighs* I'm on my way back."

            scene v14s45a_10
            with dissolve

            li "Thank you!"

            scene v14s45a_10a
            with dissolve

            u "Uh, huh..."

        scene v14s45a_10
        with dissolve

        li "Haha, see you soon."

        play sound "sounds/rejectcall.mp3"

        scene v14s45a_7a
        with dissolve

        pause 0.75

        scene v14s45a_8
        with dissolve

        pause 0.75

        scene v14s45a_9
        with dissolve

        pause 0.75

    else: #not helping Lindsey
        pause 0.75
    
        scene v14s45a_8
        with dissolve

        pause 0.75

        scene v14s45a_9
        with dissolve

        pause 0.75

    stop music fadeout 3

    jump v14s46