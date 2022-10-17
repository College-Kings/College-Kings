# SCENE 31: MC walking home/Josh encounter
# Location: MC walking home/Josh encounter
# Characters: MC (Outfit 3),Josh (outfit 1)
# Time: Tuesday late evening
label v10_late_alley:

    scene v10all1 # TPP. Show MC on the sidewalk, just before the entrance to the alley, mouth closed
    with dissolve
    play music "music/v10/Track Scene 31.mp3" fadein 2
    pause 0.75

    scene v10all2 # FPP. Show Alley, 2 hookers against the wall near the entrance, Josh down the bottom of the alley with unknown guy in hoody,
    with dissolve

    u "Josh!"

    scene v10all2a # FPP. same 2, josh now infront of camera, josh mouth closed.
    with dissolve

    u "Bro, are you dealing again?"

    scene v10all3 # FPP. Show Josh sat on floor, slight frown, mouth open
    with dissolve

    jo "Look man, I haven't been, you know... getting any lately. I'm here for the girls."

    scene v10all4 # FPP. Show the 2 hookers, both mouths closed. Looking at each other
    with dissolve

    u "Really? So the guy that ran was what... their pimp?"

    scene v10all3
    with dissolve

    jo "*Sighs* Okay, yes I'm dealing."

    if v10_josh_alley_yes:

        jo "You remember everything I told you last time about the guy I met?"

        scene v10all3a # FPP. same 3, mouth closed
        with dissolve

        u "Yeah..."

        scene v10all3
        with dissolve

        jo "Well he's really close to getting everything done, and once he does I'm done with all this."
        jo "He's having issues with his wife though and that's causing problems."

        scene v10all3a
        with dissolve

        u "I just don't want to see you get hurt in the meantime, but I understand your situation."

        scene v10all3
        with dissolve

        jo "Thanks man."
    else:

        jo "Trust me, you have nothing to worry about. I'm being smart."

        scene v10all3a
        with dissolve

        u "I'm not judging and you can do whatever you want, but... I gotta ask, do you enjoy doing this?"

        scene v10all3
        with dissolve

        jo "Hell no, I hate this shit."

        scene v10all3a
        with dissolve

        u "Then why are you doing it?"

        scene v10all3
        with dissolve

        jo "I need the money."

        scene v10all3a
        with dissolve

        u "For what? Didn't your dad-"

        scene v10all3
        with dissolve

        jo "My dad cut me off."

        scene v10all3a
        with dissolve

        u "What?! I thought-"

        scene v10all3
        with dissolve

        jo "I didn't go to the military! So he cut me off, said if I didn't spend at least four years in the military I wouldn't see a penny."

        jo "So now I have to figure out how I'm gonna pay for school."

        scene v10all3a
        with dissolve

        u "Damn man, I'm sorry. I wish you would've told me sooner."

        scene v10all3
        with dissolve

        jo "I was just gonna do it until I had enough, but I'm hoping I won't have to do it much longer."
        jo "I met this guy and he might be able to get me a scholarship."

        scene v10all3a
        with dissolve

        u "That'd be awesome. Shit, what's his name, maybe he can get me one too. *Chuckles*"

        scene v10all3
        with dissolve

        jo "Haha, he's some big shot. Can't remember his name honestly, but he's a bit intimidating. Kinda reminds me of my dad, but more flexible."

    menu:
        "Support him":
            $ v10_support_josh = True
            scene v10all3a
            with dissolve
            u "Just be safe, deal in the daylight not in a back alleyway. Anything could happen and we would have no idea."

            scene v10all3
            with dissolve

            jo "Well I don't want to get caught on campus, that'd defeat the whole purpose of doing this in the first place because I'd be suspended."

            scene v10all3a
            with dissolve

            u "Bro, have your \"clients\" stop by your house or get someone else to deliver for you and give them a little cut. Doing it here is dangerous."

            scene v10all3
            with dissolve

            jo "Having someone work for me does sound nice."

            jo "I'm sure the guy I've been selling to would do it if I just let him have some for free. He's been a pretty serious customer."

            scene v10all3a
            with dissolve

            u "Someone I know?"

            scene v10all3
            with dissolve

            jo "Not sure, he does go to SVC though. He was in that nerd frat."

            scene v10all3a
            with dissolve

            u "(Is he talking about the Frogs?)"

            u "Yeah, let him do your dirty work."

            scene v10all3
            with dissolve

            jo "Not a bad idea. I appreciate the talk man."

        "Don't support":
            if reputation() == Reputations.CONFIDENT:
                scene v10all3a
                with dissolve

                u "I get that this isn't supposed to be a permanent thing for you and you have an out plan, but I still don't support what you're doing. There's other ways to get money. You're gonna end up fucking up your life."

                call screen reputation_popup
                scene v10all3
                with dissolve

                jo "I open up to you and that's your response? What else am I supposed to do?"

                scene v10all3a
                with dissolve

                u "I'm not saying I have all the answers, but putting yourself in a dangerous situation to get out of a dangerous situation isn't a good idea."

                scene v10all3b # FPP. same 3,slight worried look,mouth open
                with dissolve

                jo "Fuck, when you say it out loud like that it kinda makes some sense."

                scene v10all3a
                with dissolve

                u "I'm just saying man."

                scene v10all3
                with dissolve

                jo "Trust me, I hear you. I'm gonna get out of here man."

            else:
                $ josh.relationship = Relationship.MAD
                $ josh_europe = False
                scene v10all3a
                with dissolve
                u "I get that this isn't supposed to be a permanent thing for you and you have an out plan, but I still don't support what you're doing. There's other ways to get money. You're gonna end up fucking up your life."

                scene v10all3c # FPP. same 3,angry look,mouth open
                with dissolve

                jo "I open up to you and that's your response? Mind your own business from now on! Fuck you man!"
                
    scene v10all2a
    with dissolve

    pause 0.75

    scene v10all5 # FPP. Show josh walking off down the sidewalk.
    with dissolve
    stop music fadeout 3
    jump v10_tues_room_night
