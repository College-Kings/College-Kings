# SCENE 35: Lindsey Game Night
# Locations: Chicks Sorority House
# Characters: LINDSEY (Outfit: 1), MC (Outfit: 2), AUTUMN (Outfit: x), AUBREY (Outfit: 1)
# Time: Evening
# Render Count: Unique Renders 18 Total: 144

init python:
    def v15s35_kiwiireply1():
        v15s35_kiwiiPost1.newComment(imre, "Bro, you have no idea what you're getting yourself into. You're so fucking on!", numberLikes=renpy.random.randint(260, 560))
        
    def v15s35_kiwiireply2():
        v15s35_kiwiiPost1.newComment(lindsey, "Agreed! :) Thanks again for coming, [name].", numberLikes=renpy.random.randint(260, 560))

label v15s35:
    play music "music/v13/Track Scene 18.mp3" fadein 2

    scene v15s35_1 # TPP. MC arrives at the Chicks house, knocks on the front door, slight smile, mouth is closed
    with dissolve

    pause 0.75

    scene v15s35_1a # TPP. same as v15s35_1 Lindsey opens the door slight smile, mouth is open, Mc slight smile, mouth is closed
    with dissolve

    li "Hey, [name], you're right on time. We're about to start!"

    scene v15s35_2 # FPP. Show Lindsey standing in the doorway of the Chicks Sorority house, slight smile, mouth is closed
    with dissolve

    menu:
        "Be polite":
            $ add_point(KCT.BRO)
            $ add_point(KCT.BOYFRIEND)

            scene v15s35_2
            with dissolve

            u "Good, I was worried I would be late. Thanks for inviting me."

            scene v15s35_2a # FPP. same as v15s35_2 Lindsey's mouth is open, still a slight smile
            with dissolve

            li "Of course! It should be a fun night!"

        "Be funny":
            $ add_point(KCT.BRO)
            $ add_point(KCT.TROUBLEMAKER)

            scene v15s35_2
            with dissolve

            u "I hope you're ready to lose!"

            scene v15s35_2a
            with dissolve

            li "No way! I think I have a pretty good chance at winning tonight."

            scene v15s35_2
            with dissolve

            u "You seem confident."

            scene v15s35_2a
            with dissolve

            li "Well, I may have rigged them."

            scene v15s35_2
            with dissolve

            u "Ha! Okay, so cheating is completely fair tonight. Got it."

            scene v15s35_2a
            with dissolve

            li "Haha, we shouldn't need to cheat tonight, but... Whatever happens, happens."
        
    scene v15s35_3 # TPP. MC enters the house, his back is turned to the camera Lindsey closes the door slight smile mouth is closed looking at Mc
    with dissolve

    pause 0.75

    scene v15s35_4 # TPP. MC enters the kitchen with Lindsey both slight smiles mouths are closed, Aubrey and Autumn are standing with their drinks in hand, both of them looking at Mc slight smiles, Aubrey's mouth is closed, Autumn is waving at MC, mouth is open
    with dissolve

    pause 0.75

    scene v15s35_5 # TPP. Show just Lindsey, Aubrey, and Autumn, Aubrey and Autumn have drinks in their hands from render v15s35_4, all of them looking at Mc, slight smiles, mouths are closed, show the sink area in the background as Autumn and Lindsey will be going to that area in future renders
    with dissolve

    u "Hey. What're you drinking?"

    if v15_lindsey_alcohol:
        scene v15s35_5a # TPP. same as v15s35_5 Autumn's mouth is open
        with dissolve

        aut "It's called a liquid marijuana. Lindsey made them, they're not bad!"

        scene v15s35_5b # TPP. same as v15s35_5 Aubrey's mouth is open, Aubrey and Autumn are looking at Lindsey
        with dissolve

        au "They're amazing, Lindsey. I'm already feeling it."

    else:
        scene v15s35_5a
        with dissolve

        aut "They're virgin Sangrias. They taste great. You don't even realize that it's a mocktail, haha."

        scene v15s35_5b
        with dissolve

        au "Yeah, Lindsey, I would never have known if you hadn't told me."

    scene v15s35_5c # TPP. same as v15s35_5 Lindsey's mouth is open, Aubrey and Autumn are looking at Lindsey, Lindsey is looking at Aubrey
    with dissolve

    li "Thanks! I've been studying a lot of recipes lately. I even bought a book."

    scene v15s35_5d # TPP. same as v15s35_5a Autumn is now looking at Lindsey
    with dissolve

    aut "Really? Can I see?"

    scene v15s35_5e # TPP. same as v15s35_5c Lindsey is looking at Autumn
    with dissolve

    li "It's over here. I need to make one for [name] now."

    scene v15s35_5d
    with dissolve

    aut "Oh, I can help you."

    scene v15s35_5f # TPP. same as v15s35_5 Lindsey and Autumn go over towards the sink area where cocktail-making items are laid out, both their backs are turned to MC and Aubrey, Aubrey is looking at Mc slight smile, mouth is closed
    with dissolve

    pause 0.75

    if aubrey.relationship <= Relationship.MAD:
        scene v15s35_5g # TPP. same as v15s35_5f Aubrey has no expression, mouth is open, still looking at Mc, Autumn and Lindsey still have their backs turned to MC and Aubrey
        with dissolve

        au "Can we try to not be awkward tonight? I'm still dealing with what you did with Naomi, but I'll try to act as normal as I can."

        scene v15s35_5h # TPP. same as v15s35_5g Aubrey's mouth is closed
        with dissolve

        u "Okay, yeah. Again, I'm really sorry, I-"

        u "I just want things to go back to the way they used to be."

        scene v15s35_5g
        with dissolve

        au "Yeah, let's hope that's possible."

    else:
        scene v15s35_5f
        with dissolve

        u "Hey, how are you feeling?"

        scene v15s35_5i # TPP. same as v15s35_5f Aubrey's mouth is open, still looking at Mc, Autumn and Lindsey still have their backs turned to MC and Aubrey
        with dissolve

        au "Much better now that I'm home. Thanks for asking."

        scene v15s35_5f
        with dissolve

        au "I'm glad you came to the wedding. I don't think I would have survived if you hadn't been there."

        scene v15s35_5i
        with dissolve

        u "You're welcome. And if they want a third wedding, I'll come to that with you too. *Laughs*"

        scene v15s35_5f
        with dissolve

        au "*Laughs*, If they end up wanting a third wedding, I might die."

        scene v15s35_5i
        with dissolve

        u "Ha, hey. Whatever uncomfortable family gathering you might have in the future; I'll be there for you. I promise."

        scene v15s35_5f
        with dissolve

        au "Aw, thanks, [name]. I may just hold you to that."

    scene v15s35_5j # TPP. same as v15s35_5 Lindsey and Autumn return,Lindsey handing MC his drink, just show Mc's arm and hand reaching for the drink, all slight smiles, all mouths are closed, all looking at MC
    with dissolve

    pause 0.75

    scene v15s35_5k # TPP. same as v15s35_5j Mc's arm and hand are now out of view, Lindsey's mouth is open
    with dissolve

    li "Here's to having an awesome game night!"

    scene v15s35_5l # TPP. same as v15s35_5j Widen the shot to now show Mc, all of them slight smiles, mouths are open, all of them are clinking their glasses together above of the table.
    with fade

    pause 0.75

    scene v15s35_6 # TPP. show everyone sitting at the kitchen table On Mc's Left is Lindsey, in front of Mc is Autumn, on Mc's right is Aubrey, Mc and Lindsey are looking at each other Lindsey's mouth is open, Mc's mouth is closed, Autumn and Aubrey are looking at each other Aubrey's mouth is open, Autumns mouth is closed
    with dissolve

    pause 0.75

    if v15_lindsey_mostlikelyto: #If helping Lindsey and chose Most Likely To
        jump v15most_likely_to

    elif v15_lindsey_gamenight: #If helping Lindsey and chose Would You Rather
        jump v15would_you_rather

    else: # -if MC is not helping lindsey and did not choose a game on the planning board, but just got invited to game night
        scene v15s35_7 # FPP. Mc looks to his left and just see's Lindsey, Lindsey has a slight smile, mouth is open, looking at Mc
        with dissolve

        li "[name], help me out here. I have two games, but I can't decide which one we should play. What do you think?"

        scene v15s35_7a # FPP. same as v15s35_7 Lindsey's mouth is closed, still looking at Mc, still a slight smile
        with dissolve

        u "What are the games?"

        scene v15s35_7
        with dissolve

        li "\"Would you rather\" or \"Most likely to\"."

        scene v15s35_7a
        with dissolve

        u "Hmm..."

        scene v15s35_7a
        with dissolve

        menu:
            "Would you rather":
                scene v15s35_7a
                with dissolve

                u "Let's play \"Would you rather\". It sounds like the most fun option."

                scene v15s35_7
                with dissolve

                li "Okay, perfect."

                jump v15would_you_rather

            "Most likely to":
                scene v15s35_7a
                with dissolve

                u "I vote for \"Most likely to\"."

                scene v15s35_7
                with dissolve

                li "Okay, good choice!"

                jump v15most_likely_to
            
    label v15would_you_rather: # -if Chose would you rather on the planning board and regardless of how they chose the game, continue to the game
        scene v15s35_7b # FPP. same as v15s35_7 Lindsey takes out her phone looks at it and taps on it,  all v15s35_7(letter) renders going forward Lindsey will be holding her phone unless otherwise said, slight smile, mouth is open
        with dissolve

        li "So, I just messaged you all a link to get the game app."

        scene v15s35_6a # TPP. same as v15s35_6 Everyone gets out their phones, looks at them and taps on them, all slight smiles, all mouths closed
        with dissolve

        pause 0.75

        scene v15s35_8 # FPP. Show Autumn holding her phone, all v15s35_8(letter) renders Autumn will be holding her phone unless otherwise said, looking at Lindsey, Slight smile, mouth is open
        with dissolve

        aut "Ready."

        scene v15s35_9 # FPP. Show Aubrey holding her phone,  all v15s35_9(letter) renders Aubrey will be holding her phone unless otherwise said, looking at Lindsey, Slight smile, mouth is open
        with dissolve

        au "Yeah, I'm ready."

        scene v15s35_7c # FPP. same as v15s35_7b Lindsey's mouth is closed, looking at Mc, still Slight smile
        with dissolve

        u "Let's do this!"

        scene v15s35_7b
        with dissolve

        li "So, the first one is..."

        scene v15s35_7d # FPP. same as v15s35_7c Lindsey's mouth is open, still looking at Mc, still Slight smile
        with dissolve

        li "Would you rather be given fifty million dollars to donate to charity, or be given half a million dollars to spend on yourself?"

        scene v15s35_9
        with dissolve

        au "Ooh, good one."

        scene v15s35_8
        with dissolve

        aut "Checking our moral compass, Lindsey?"

        scene v15s35_8a # FPP. same as v15s35_8 Autumn is looking at Mc, mouth is closed, still a slight smile
        with dissolve

        u "(I should choose carefully. I could easily look like the bad guy here.)"

        scene v15s35_7c
        with dissolve

        # -We enter the UI for Would you rather-

        # -After choosing, we see on the UI what everyone has chosen. All three girls chose $50m to charity-

        $ screen_options = [
            {
                "option": "$50 million to charity",
                "votes": [aubrey, autumn, lindsey],
                "label": "v15s35_wyr1_charity"
            },
            {
                "option": "$500k for me",
                "votes": [],
                "label": "v15s35_wyr1_me"
            }
        ]
        call screen would_you_rather("Would you rather?")

    label v15s35_wyr1_charity:
        $ add_point(KCT.BOYFRIEND)
        
        scene v15s35_7d
        with dissolve

        li "And it's unanimous! We're all good people. *Chuckles*"

        scene v15s35_8
        with dissolve

        aut "Of course we are!"

        scene v15s35_9a # FPP. same as v15s35_9 Aubrey is looking at Autumn, mouth is still open, still a slight smile
        with dissolve

        au "But the real question is, what charities would you donate to?"

        scene v15s35_8b # FPP. same as v15s35_8 Autumn is looking at Aubrey, still a slight smile, mouth is still open
        with dissolve

        aut "Homes for Huskies! Or actually..."

        aut "Maybe I could give some to Narwhals in Need and some to Protect the Pandas too."

        scene v15s35_9a
        with dissolve

        au "Hehe, damn. You've got a list ready to go, huh?"

        scene v15s35_8b
        with dissolve

        aut "Ha, I guess yeah. I'm just interested in all of it and helping all of them."

        scene v15s35_8a
        with dissolve

        u "So pure."

        scene v15s35_9b # FPP. same as v15s35_9 Aubrey is looking at Mc, still a slight smile, mouth is still open
        with dissolve

        au "It's almost disgusting... *Giggles*"
        
        jump v15s35_wyr1_end

    label v15s35_wyr1_me:
        $ add_point(KCT.BRO)

        scene v15s35_7d
        with dissolve

        li "Well, it looks like [name] is the only uncharitable one here..."

        scene v15s35_8c # FPP. same as v15s35_8a Autumn is slightly shocked, mouth is open, still looking at Mc
        with dissolve

        aut "[name]!"

        scene v15s35_8a
        with dissolve

        u "What?"

        scene v15s35_8d # FPP. same as v15s35_8a Autumn's mouth is open, still looking at Mc, still Slight smile
        with dissolve

        aut "Fifty million dollars to people in need? And you'd rather have half a million to spend on what? BoobGroup subscriptions?"

        scene v15s35_8a
        with dissolve

        u "*Chuckles* Boob group?"

        scene v15s35_9b
        with dissolve

        au "You could feed the starving world with that kind of money"

        scene v15s35_7d
        with dissolve

        li "But now they'll continue to suffer because of [name]. *Sighs*"

        scene v15s35_7e # FPP. same as v15s35_7c Lindsey has no expression, still looking at Mc, mouth is still closed
        with dissolve

        u "Woah, woah, woah... Hang on. This is a game!"

        scene v15s35_8e # FPP. same as v15s35_8a Autumn has no expression, still looking at Mc, mouth is still closed
        with dissolve

        u "I didn't realize how seriously we were taking this..."

        scene v15s35_9c # FPP. same as v15s35_9b Aubrey is fake crying, still looking at Mc, mouth is still open
        with dissolve

        au "Those poor starving children. *Fake sobbing* You could have saved them!"

        scene v15s35_7f # FPP. same as v15s35_7d Lindsey is fake crying, still looking at Mc, mouth is still open
        with dissolve

        pause 0.75

        scene v15s35_8f # FPP. same as v15s35_8c Autumn is fake crying, still looking at Mc, mouth is still open
        with dissolve

        pause 0.75

        scene v15s35_8a
        with dissolve

        u "Okay, I'm sorry! Jeez..."

        scene v15s35_6b # TPP. same as v15s35_6a Aubrey, Autumn and Lindsey are laughing at Mc, Mc is rolling his eyes, Everyone is still holding their phones
        with dissolve

        pause 0.75

    label v15s35_wyr1_end:
        scene v15s35_7d
        with dissolve

        li "Okay, now that we've established everyone's moral compass, here's the next one..."

        scene v15s35_7b
        with dissolve

        li "Would you rather kill Santa Claus or the Easter bunny?"

        scene v15s35_8
        with dissolve

        aut "What kind of creepy question is that?"

        scene v15s35_9
        with dissolve

        au "Haha, it's an easy one."

        scene v15s35_8b
        with dissolve

        aut "Maybe for psychopaths..."

        scene v15s35_8a
        with dissolve

        u "I guess it depends on what your favorite holiday is."

        scene v15s35_7d
        with dissolve

        li "Yeah, that's what I'm thinking."

        scene v15s35_8
        with dissolve

        aut "Murdering based on favorites... This is getting scary *Giggles*"

        scene v15s35_8a
        with dissolve

        pause 0.75

        # -We enter the UI for Would you rather-

        # -After choosing, we see on the UI what everyone has chosen. Autumn chose Kill Santa. Lindsey and Aubrey chose Kill the Easter bunny-

        $ screen_options = [
            {
                "option": "Kill Santa Claus",
                "votes": [autumn],
                "label": "v15s35_wyr2_santa"
            },
            {
                "option": "Kill the Easter bunny",
                "votes": [aubrey, lindsey],
                "label": "v15s35_wyr2_easter"
            }
        ]
        call screen would_you_rather("Would you rather?")

    label v15s35_wyr2_santa:
        $ add_point(KCT.BRO)
        
        scene v15s35_7g # FPP. same as v15s35_7d Lindsey is slightly shocked, still looking at Mc, mouth is still open
        with dissolve

        $ grant_achievement("christmas_is_dead")
        li "*Gasps* Autumn and [name]! How dare you kill Santa?!"

        scene v15s35_9b
        with dissolve

        au "How?! Santa only brings gifts and joy! Why kill him for that, you psychos?"

        scene v15s35_8b
        with dissolve

        aut "How could you two kill a poor defenseless bunny rabbit?!"

        scene v15s35_9a
        with dissolve

        au "With a shotgun..."

        scene v15s35_6c # TPP. same as v15s35_6b Aubrey and Lindsey look at each other and laugh, Autumn is slightly shocked looking at Aubrey, Mc is rolling his eyes still a slight smile, everyone is still holding their phones
        with dissolve

        pause 0.75

        scene v15s35_9d # FPP. same as v15s35_9b Aubrey's mouth is closed, still looking at Mc, still a slight smile
        with dissolve

        u "Santa has lived plenty of years, alright? A bunny that leaves surprise-filled eggs, is far superior."

        scene v15s35_9b
        with dissolve

        au "I can't believe this."

        scene v15s35_9d
        with dissolve

        u "And we can't believe you shot the Easter bunny. No more Easter baskets for you."

        scene v15s35_9b
        with dissolve

        au "Fine, I don't care. Easter's super lame compared to Christmas; Everyone knows that."

        scene v15s35_7h # FPP. same as v15s35_7d Lindsey is looking at Aubrey, mouth is still open, still a slight smile
        with dissolve

        li "We can still celebrate Easter. Let's just find a new animal."

        scene v15s35_9
        with dissolve

        au "The Easter panda!"

        scene v15s35_7h
        with dissolve

        li "The Easter giraffe. *Laughs*"

        scene v15s35_8g # FPP. same as v15s35_8d Autumn rolls her eyes, mouth is still open, still a slight smile
        with dissolve

        aut "Unbelievable..."

        scene v15s35_8a
        with dissolve

        u "At least with Santa gone, one of the elves has a chance to move up in the company."

        scene v15s35_9e # FPP. same as v15s35_9b Aubrey is slightly shocked, still looking at Mc, mouth is still open
        with dissolve

        au "So, you're saying it's okay to murder Santa if it opens a job for an elf?"

        scene v15s35_9d
        with dissolve

        u "I feel good about my decision, Aubrey. I helped an elf. You murdered a bunny."
        
        jump v15s35_wyr2_end

    label v15s35_wyr2_easter:
        $ add_point(KCT.TROUBLEMAKER)

        scene v15s35_7i # FPP. same as v15s35_7h Lindsey is looking at Autumn, still a slight smile, mouth is still open
        with dissolve

        li "Autumn! You killed Santa?"

        scene v15s35_8
        with dissolve

        aut "Well, I'm not killing an animal! Sorry not sorry."

        scene v15s35_8a
        with dissolve

        u "Tell that to Santa's wife!"

        if aubrey.relationship <= Relationship.MAD:
            scene v15s35_9f # FPP. same as v15s35_9d Aubrey has a disgusted look on her face, still looking at Mc, mouth is still closed
            with dissolve

            pause 0.75

            scene v15s35_9g # FPP. same as v15s35_9a Aubrey has no expression, still looking at Autumn, mouth is still open
            with dissolve

            au "Yeah, and all the elves."

        else:
            scene v15s35_9h # FPP. same as v15s35_9b Aubrey has a full smile and is laughing, still looking at Mc
            with dissolve

            pause 0.75

            scene v15s35_9a
            with dissolve

            au "Yeah, and all the elves."

        scene v15s35_7i
        with dissolve

        li "They're all crying themselves to sleep tonight because of you."

        scene v15s35_8h # FPP. same as v15s35_8a Autumn is smirking, still looking at Mc, mouth is still closed
        with dissolve

        u "Damn, Autumn. Shame on you..."

        scene v15s35_7j # FPP. same as v15s35_7f Lindsey is looking at Autumn, still fake crying, mouth is still open
        with dissolve

        li "Christmas is over... *Fake sobbing*"

        scene v15s35_8
        with dissolve

        aut "What? Haha, come on you guys... They'd have a contingency plan for that, I'm sure."

        scene v15s35_8a
        with dissolve

        u "I guess we'll find out soon enough."

        scene v15s35_8b
        with dissolve

        aut "How can you all be so okay with killing the Easter bunny?"

        scene v15s35_9a
        with dissolve

        au "At least we can eat the Easter bunny. I wouldn't want to chew on Santa. *Laughs*"

        scene v15s35_7h
        with dissolve

        li "Eww, that's so gross, Aubrey..."

        scene v15s35_9
        with dissolve

        au "You're welcome."

        scene v15s35_8a
        with dissolve

        u "Anyone can dress up as a bunny to take its place. Get me a basket and some eggs and our problem is solved."

        if aubrey.relationship <= Relationship.MAD:
            scene v15s35_9f
            with dissolve

            pause 0.75

        elif aubrey.relationship >= Relationship.TAMED:
            scene v15s35_9i # FPP. same as v15s35_9d Aubrey is biting her finger, looking at Mc seductively
            with dissolve

        else:
            scene v15s35_9h
            with dissolve

        scene v15s35_8a
        with dissolve

        u "But finding a new Santa? Sheesh... That's a recruiting nightmare."

        if aubrey.relationship <= Relationship.MAD:
            scene v15s35_9g
            with dissolve

            au "Yeah, Autumn, you really fucked us on this one."

            scene v15s35_9f
            with dissolve

            pause 0.75

        elif aubrey.relationship >= Relationship.TAMED:
            scene v15s35_9j # FPP. same as v15s35_9i Aubrey is winking at Mc, not biting her finger, full smile, mouth is closed
            with dissolve

            pause 0.75

        scene v15s35_8b
        with dissolve

        aut "Alright, alright. Say what you want, but I'm never going to kill that poor bunny."

    label v15s35_wyr2_end:

        scene v15s35_7i
        with dissolve

        li "Now that we know who the murderers are, here's number three..."

        scene v15s35_7b
        with dissolve

        li "Would you rather have the body of a frog and keep your human mind, or keep your human body and have the mind of a frog?"

        scene v15s35_9k # FPP. same as v15s35_9 Aubrey has a concerned expression, still looking at Lindsey, mouth is still open
        with dissolve

        au "..."

        scene v15s35_8i # FPP. same as v15s35_8 Autumn has a concerned expression, still looking at Lindsey, mouth is still open
        with dissolve

        aut "I..."

        scene v15s35_7c
        with dissolve

        u "These are getting really weird, Lindsey. *Laughs*"

        scene v15s35_7d
        with dissolve

        li "They're supposed to make you think!"

        scene v15s35_8
        with dissolve

        aut "Actually, the more I think about it, the easier it is to choose."

        scene v15s35_8a
        with dissolve

        u "Ha, really? Let's see..."

        scene v15s35_9d
        with dissolve

        # -We enter the UI for Would you rather-

        # -After choosing, we see on the UI what everyone has chosen. Lindsey and Autumn chose frog body, human mind. Aubrey chose human body, frog mind-

        $ screen_options = [
            {
                "option": "Human body, frog mind",
                "votes": [aubrey],
                "label": "v15s35_wyr3_humanbody"
            },
            {
                "option": "Frog body, human mind",
                "votes": [autumn, lindsey],
                "label": "v15s35_wyr3_frogbody"
            }
        ]
        call screen would_you_rather("Would you rather?")

    label v15s35_wyr3_frogbody:
        $ add_point(KCT.BRO)
        
        scene v15s35_7h
        with dissolve

        li "Really, Aubrey?"

        scene v15s35_9
        with dissolve

        au "What?"

        scene v15s35_7h
        with dissolve

        u "So, you're happy just jumping around all day, swimming in rivers and eating flies?"

        scene v15s35_9
        with dissolve

        au "Ha! Yeah, actually. It sounds great."

        au "I could still do human things using my human body, but since I have a frog brain... No expectations, no pressure at all."

        scene v15s35_9d
        with dissolve

        u "Huh..."

        scene v15s35_9
        with dissolve

        au "Just enjoying life, sunbathing all day. It would be the life!"

        scene v15s35_8b
        with dissolve

        aut "Wait, that sounds really nice... Can I change my answer?"

        scene v15s35_7i
        with dissolve

        li "Absolutely not! You made your choice. You're now a tiny frog with a human mind."

        scene v15s35_8j # FPP. same as v15s35_8a Autumn has a cute pouting expression, still looking at Mc, mouth is still closed
        with dissolve

        pause 0.75

        scene v15s35_8a
        with dissolve

        u "Yeah, but we're hyper-intelligent frogs. We could build cities, you know."

        scene v15s35_7d
        with dissolve

        li "True. Whatever we wanted."

        scene v15s35_8a
        with dissolve

        u "Maybe one day we could take over the planet."

        scene v15s35_8d
        with dissolve

        aut "Okay, I'm happy with my choice again. *Giggles* Animals taking the planet back!"

        scene v15s35_7i
        with dissolve

        li "Frog power!"

        scene v15s35_8d
        with dissolve

        aut "Frog power!"

        scene v15s35_8a
        with dissolve

        u "Frog power!"

        scene v15s35_9l # FPP. same asv15s35_9j Aubrey is sticking her tongue out, still winking, still full smile, mouth is still open
        with dissolve

        au "Human with frog brain power!"

        scene v15s35_6d # same as v15s35_6c Everyone is looking at each other and laughing
        with dissolve
        
        pause 0.75
        
        jump v15s35_wyr3_end
        
    label v15s35_wyr3_humanbody:
        $ add_point(KCT.BOYFRIEND)

        scene v15s35_7i
        with dissolve

        li "Looks like it's just me and Autumn keeping each other company as frogs."

        scene v15s35_8
        with dissolve

        aut "Haha, I think it would be a lot of fun! Plus, we'd be cute frogs."

        scene v15s35_7i
        with dissolve

        li "Are you kidding? We'd be the hottest frogs!"

        scene v15s35_8a
        with dissolve

        u "What type of adventures do you think you'll have?"

        scene v15s35_8d
        with dissolve

        aut "I just like the simplicity of exploring nature from a frog's perspective."

        scene v15s35_8a
        with dissolve

        u "But you would also have to eat flies for the rest of your life."

        scene v15s35_7k # FPP. same as v15s35_7e Lindsey's mouth is open, still no expression, still looking at Mc
        with dissolve

        li "Ugh, no! No more coffee or Chinese food or... anything?"

        scene v15s35_7e
        with dissolve

        u "Nope. Just flies, all day, every day. *Laughs*"

        scene v15s35_9
        with dissolve

        au "Yeah, I'm happy with my choice. I still get to eat whatever I want."

        scene v15s35_8b
        with dissolve

        aut "But would your frog mind appreciate human food?"

        scene v15s35_7h
        with dissolve

        li "Yeah, it would reject everything, and it wouldn't be long before you're eating flies like us."

        scene v15s35_9
        with dissolve

        au "Fuck, that's true. Okay, I'll eat the damn flies."

        scene v15s35_9d
        with dissolve

        u "Aubrey, let's just go live in a river and eat flies. These two will need our help protecting them from predators anyway."

        if aubrey.relationship <= Relationship.MAD:
            scene v15s35_9m # FPP. same as v15s35_9g Aubrey is looking at Mc, still no expression, mouth is still open
            with dissolve

            au "Ha."

        else:
            scene v15s35_9h
            with dissolve

            au "Haha, okay, sounds like a plan."

        scene v15s35_8a
        with dissolve

        aut "Aww, we have personal human bodyguards!"

        scene v15s35_7d
        with dissolve

        li "I feel so protected... Hehe."

        scene v15s35_9
        with dissolve

        au "What's the next creep question, huh?"
        
    label v15s35_wyr3_end:
        scene v15s35_7b
        with dissolve

        li "Number four..."

        li "Would you rather have no sex for the rest of your life, or only have an orgy with the same twenty people for the rest of your life?"

        scene v15s35_9
        with dissolve

        au "Orgy. For sure. One thousand percent."

        if aubrey.relationship <= Relationship.MAD:
            scene v15s35_9n # FPP. same as v15s35_9f Aubrey rolls her eyes, still a disgusted expression, mouth is still closed, still facing Mc
            with dissolve

            pause 0.75

        scene v15s35_7h
        with dissolve

        li "You sure you don't need a few minutes to think it over? *Giggles*"

        scene v15s35_9
        with dissolve

        au "Nope. I've made my decision."

        scene v15s35_7h
        with dissolve

        li "I mean, it's an orgy, though. Twenty people every time?"

        scene v15s35_7c
        with dissolve

        u "Wait, so there's no option to just have a normal one on one relationship?"

        scene v15s35_7d
        with dissolve

        li "Nope. No sex at all, or sex with all twenty."

        scene v15s35_8k # FPP. same as v15s35_8i Autumn is looking at her phone, still a concerned expression, mouth is still closed
        with dissolve

        pause 0.75

        scene v15s35_8i
        with dissolve

        aut "..."

        scene v15s35_8l # FPP. same as v15s35_8i Autumn is looking at Mc, still a concerned expression, mouth is still closed
        with dissolve

        u "You okay, Autumn?"

        scene v15s35_8m # FPP. same as v15s35_8d Autumn has no expression, still looking at Mc, mouth is still open
        with dissolve

        aut "I'm just thinking about my answer."

        scene v15s35_8k
        with dissolve

        # -We enter the UI for Would you rather-

        # -After choosing, we see on the UI what everyone has chosen. Autumn chose no sex forever. Lindsey and Aubrey chose Orgy with twenty people forever-

        $ screen_options = [
            {
                "option": "No sex forever",
                "votes": [autumn],
                "label": "v15s35_wyr4_nosex"
            },
            {
                "option": "20-person orgy every time",
                "votes": [aubrey, lindsey],
                "label": "v15s35_wyr4_orgy"
            }
        ]
        call screen would_you_rather("Would you rather?")

    label v15s35_wyr4_nosex:
        $ add_point(KCT.BOYFRIEND)
        
        scene v15s35_7g
        with dissolve

        li "Interesting!"

        scene v15s35_9e
        with dissolve

        au "No sex forever? Are you fucking crazy? *Laughs*"

        scene v15s35_9o # FPP. same as v15s35_9m Aubrey's mouth is closed, still no expression, still looking at Mc
        with dissolve

        u "I think an orgy with the same twenty people every time would just get-"

        scene v15s35_8e
        with dissolve

        u "Well... depressing after a while, you know?"

        scene v15s35_8a
        with dissolve

        pause 0.75

        scene v15s35_9m
        with dissolve

        au "Hard to tell. I'll let you know though."

        scene v15s35_9p # FPP. same as v15s35_9d Aubrey is smirking, still looking at Mc, still a slight smile, mouth is still closed
        with dissolve

        pause 0.75

        scene v15s35_9o
        with dissolve

        u "And what if you had serious feelings for one of the people there?"

        u "You would have to watch them get fucked by all those other people, forever?"

        if aubrey.relationship <= Relationship.MAD or "v14_threesome" in sceneList:
            scene v15s35_9q # FPP. same as v15s35_9m Aubrey is slightly sad, still looking at Mc, mouth is still open
            with dissolve

            au "Oh... Yeah, you're right..."

        else:
            scene v15s35_9m
            with dissolve

            au "Oh... Yeah, you're right..."

        scene v15s35_7k
        with dissolve

        li "That sounds awful, actually..."

        scene v15s35_7d
        with dissolve

        li "But I still think I would choose the orgy because I can't imagine life without sex, haha. That would be torture."

        scene v15s35_7c
        with dissolve

        u "I mean, it would totally suck, but still. I'd rather have no sex than be stuck with twenty people."

        scene v15s35_7i
        with dissolve

        li "Is that why you chose it, Autumn?"

        jump v15s35_wyr4_end
        
    label v15s35_wyr4_orgy:

        $ add_point(KCT.BRO)
        $ add_point(KCT.TROUBLEMAKER)
        
        scene v15s35_7d
        with dissolve

        li "*Laughs* Looks like I'll be seeing [name] and Aubrey at the orgy."

        if aubrey.relationship <= Relationship.MAD:
            scene v15s35_9
            with dissolve

            au "About time!"

        else:
            scene v15s35_9h
            with dissolve

            au "About time!"

        scene v15s35_9d
        with dissolve

        u "I wonder who else we would see there."

        scene v15s35_9b
        with dissolve

        au "I hope we get to choose a few of them..."

        scene v15s35_7h
        with dissolve

        li "I don't think we'd get a choice, hate to break it to you."

        scene v15s35_7c
        with dissolve

        u "Well, that's a little weird. Strangers?"

        if aubrey.relationship <= Relationship.MAD:
            scene v15s35_9r # FPP. same as v15s35_9f Aubrey's mouth is open, still a disgusted expression, still looking at Mc
            with dissolve

            au "It doesn't matter who's there. It's not like you have to fuck everyone."

            scene v15s35_9f
            with dissolve

            u "Isn't that the idea?"

            scene v15s35_9r
            with dissolve

            au "No! You just do stuff with whoever you want."

            scene v15s35_9f
            with dissolve

            u "I guess you could just sit and watch then..."

        else:
            scene v15s35_9b
            with dissolve

            au "It doesn't matter who's there. It's not like you have to fuck everyone."

            scene v15s35_9d
            with dissolve

            u "Isn't that the idea?"

            scene v15s35_9b
            with dissolve

            au "No! You just do stuff with whoever you want."

            scene v15s35_9c
            with dissolve

            u "I guess you could just sit and watch then..."

        scene v15s35_6e # TPP. same as v15s35_6d Aubrey, Autumn, and Lindsey are all looking at MC awkwardly, Mc has no expression, all mouths are closed
        with dissolve

        pause 0.75

        scene v15s35_6f # TPP. same as v15s35_6e Mc's mouth is open
        with dissolve

        u "If you wanted to, of course."

        scene v15s35_6e
        with dissolve

        pause 0.75

        scene v15s35_6d
        with dissolve

        pause 0.75

        scene v15s35_7i
        with dissolve

        li "So Autumn, you could really give up sex forever?"

        scene v15s35_9a
        with dissolve

        au "Insanity!"

        label v15s35_wyr4_end:

        scene v15s35_8i
        with dissolve

        aut "Well..."

        scene v15s35_8n # FPP. same as v15s35_8e Autumn has an embarrased expression, still looking at Mc, mouth is still closed
        with dissolve

        pause 0.75

        scene v15s35_8m
        with dissolve

        aut "I guess I can talk to you guys about it, I just haven't said it to anyone yet."

        scene v15s35_8e
        with dissolve

        u "Said what?"

        scene v15s35_8m
        with dissolve

        aut "I'm already used to not having sex, ha. I'm asexual."

        scene v15s35_9s # FPP. same as v15s35_9e Aubrey is looking at Autumn, still a shocked expression, mouth is still open
        with dissolve

        au "No... Fucking... Way!"

        scene v15s35_8e
        with dissolve

        u "Asexual?"

        scene v15s35_8m
        with dissolve

        aut "Yeah, so... It was an easy answer for me, haha."

        scene v15s35_9g
        with dissolve

        au "Not to be insensitive, but how exactly does that work?"
        
        jump v15s35_autumn_reveal

    label v15most_likely_to: # -if Chose Most likely to on the planning board and regardless of how they chose the game, continue to the game
        scene v15s35_7b
        with dissolve

        pause 0.75

        scene v15s35_7d
        with dissolve

        li "Okay, everyone. Phones out. I've messaged you a link to join the game."

        scene v15s35_6a
        with dissolve

        pause 0.75

        scene v15s35_8
        with dissolve

        aut "Okay, I've got it."

        scene v15s35_9
        with dissolve

        au "Me too."

        scene v15s35_7c
        with dissolve

        u "Ready."

        scene v15s35_7b
        with dissolve

        li "So, the first one is..."

        li "Who is most likely to be the first to die and turn into a zombie in a zombie apocalypse?"

        scene v15s35_9
        with dissolve

        au "Oh, that's easy."

        scene v15s35_7h
        with dissolve

        li "Is it?"

        scene v15s35_9b
        with dissolve

        u "This just got serious."

        scene v15s35_8d
        with dissolve

        aut "Ew, I want nothing to do with this."

        scene v15s35_7h
        with dissolve

        li "Okay, let's get started. Just remember you can't vote for yourselves."

        scene v15s35_8k
        with dissolve

    # -We enter the UI for Most likely to-

    # -After MC chooses an Icon, and then votes for a person, we see on the UI who everyone has chosen. Lindsey and Aubrey voted for Autumn. Autumn voted for Lindsey-

        $ screen_options = [
            {
                "character": aubrey,
                "votes": [],
                "label": "v15s35_wml1_aub"
            },
            {
                "character": autumn,
                "votes": [aubrey, lindsey],
                "label": "v15s35_wml1_aub"
            },
            {
                "character": lindsey,
                "votes": [autumn],
                "label": "v15s35_wml1_lin"
            },
            {
                "character": mc,
                "votes": [],
                "label": ""
            }
        ]
        call screen whos_most_likely_to("Most likely to turn into a zombie during an apocalypse?")

    label v15s35_wml1_lin: # -if MC voted for Lindsey, creating a tie
        scene v15s35_7i
        with dissolve

        li "It's a tie between me and Autumn?"

        scene v15s35_8
        with dissolve

        aut "I don't want to be a zombie!"

        scene v15s35_9a
        with dissolve

        au "I voted for you because I think you'd try to be friends with them, haha."

        scene v15s35_8b
        with dissolve

        aut "Really? You think I'd want to be friends with someone who wants to eat me?"

        scene v15s35_7i
        with dissolve

        li "You totally would."

        scene v15s35_8e
        with dissolve

        u "Don't worry, Autumn. I think Lindsey would be right there with you."

        scene v15s35_8a
        with dissolve

        u "*Laughs* Zombie sisters."

        scene v15s35_9a
        with dissolve

        au "You can share brains!"

        scene v15s35_8b
        with dissolve

        aut "Okay, ew, ew , ew! Stop it!"

        scene v15s35_7h
        with dissolve

        li "No thank you. I'll pass."
        
        jump v15s35_wml1_end

    label v15s35_wml1_aub: # -if MC voted for Autumn or Aubrey, Autumn wins the vote
        scene v15s35_7i
        with dissolve

        li "Sorry, Autumn. You're the first one to go."

        scene v15s35_8
        with dissolve

        aut "What? Why?! I don't want to be a zombie."

        scene v15s35_8e
        with dissolve

        u "I think you got the most votes because you're kind natured... *Chuckles*"

        u "It's basically a compliment."

        scene v15s35_8m
        with dissolve

        aut "Well, it's true that I'd probably try to help them... And then I'd get eaten."

        scene v15s35_8d
        with dissolve

        aut "In that case, I'm a proud zombie."

        scene v15s35_9a
        with dissolve

        au "Haha, I knew you would embrace the zombie life."

        scene v15s35_8b
        with dissolve

        aut "Zombies are people too."

        scene v15s35_8a
        with dissolve

        u "Even though you're rampaging killers who eat nothing but brains?"

        scene v15s35_8d
        with dissolve

        aut "*Laughs* You'd be safe, [name]. Don't worry."

        scene v15s35_8a
        with dissolve

        u "Haha, what are you saying? I'm brainless?"

        scene v15s35_8d
        with dissolve

        aut "Of course not! I'm too kind natured to say something like that to someone's face..."

        scene v15s35_8h
        with dissolve

        pause 0.75

        scene v15s35_8a
        with dissolve

        u "Haha, ouch!"

        scene v15s35_8d
        with dissolve

        aut "*Laughs*"

    label v15s35_wml1_end:

        scene v15s35_7b
        with dissolve

        li "Okay, time for the second one..."

        li "Who is most likely to get shit-faced drunk and wake up on the other side of the country?"

        scene v15s35_7c
        with dissolve

        u "Haha, how do you vote for all of us?"

        scene v15s35_9b
        with dissolve

        au "*Laughs* Yeah, it's bound to happen at some point, right?"

        scene v15s35_8b
        with dissolve

        aut "Speak for yourself."

        scene v15s35_8a
        with dissolve

        u "We'll have to get you shit-faced drunk and find out, haha."

        scene v15s35_8h
        with dissolve

        pause 0.75

    # -We enter the UI for Most likely to-

    # -After MC votes for a person, we see on the UI who everyone has chosen. All three girls voted for MC-

        $ screen_options = [
            {
                "character": aubrey,
                "votes": [],
                "label": "v15s35_wml2"
            },
            {
                "character": autumn,
                "votes": [],
                "label": "v15s35_wml2"
            },
            {
                "character": lindsey,
                "votes": [],
                "label": "v15s35_wml2"
            },
            {
                "character": mc,
                "votes": [aubrey, autumn, lindsey],
                "label": ""
            }
        ]
        call screen whos_most_likely_to("Most likely to wake up drunk across the country?")

    label v15s35_wml2:
        scene v15s35_7d
        with dissolve

        li "Haha, was it ever in doubt? [name], let us know where you end up."

        scene v15s35_7c
        with dissolve

        u "Woah now, this is bullying. Why did you all vote for me?"

        scene v15s35_9b
        with dissolve

        au "You're in a frat. You guys get up to all kinds of stupid shit."

        scene v15s35_8d
        with dissolve

        aut "Yeah, it's only a matter of time before you get shit-faced and end up on a random bus ride across country, haha."

        scene v15s35_7d
        with dissolve

        li "Waking up in Alaska or something, wondering why it's so cold, haha."

        scene v15s35_7c
        with dissolve

        u "Haha, to be honest, that does sound like something that would happen to me."

        scene v15s35_9d
        with dissolve

        u "Hopefully, drunk me will choose somewhere nice though, like a tropical island."

        scene v15s35_8d
        with dissolve

        aut "Well, just be sure to send us a postcard when you get there, haha."

        scene v15s35_8a
        with dissolve

        u "I will. Now I'm really looking forward to the next time I get drunk..."

        if aubrey.relationship >= Relationship.TAMED:
            scene v15s35_9b
            with dissolve

            au "If you're going to a tropical island, I'm coming with you."

            scene v15s35_9d
            with dissolve

            u "Okay, but only if you're shit-faced too."

            scene v15s35_9h
            with dissolve

            au "Deal!"

        scene v15s35_7b
        with dissolve

        li "Here's the next one..."

        li "Who is most likely to become a sexy super spy like James Bond?"

        scene v15s35_7c
        with dissolve

        u "Who says I'm not already a sexy super spy like James Bond?"

        if aubrey.relationship <= Relationship.MAD:
            scene v15s35_9r
            with dissolve

            au "Pfft, are you?"

            scene v15s35_9f
            with dissolve

            u "If I told you, I would have to kill you."

            scene v15s35_9n
            with dissolve

            pause 0.75

        elif aubrey.relationship >= Relationship.TAMED:
            scene v15s35_9b
            with dissolve

            au "Pfft, are you?"

            scene v15s35_9d
            with dissolve

            u "If I told you, I would have to kill you."

            scene v15s35_9i
            with dissolve

            pause 0.75

        else:
            scene v15s35_9b
            with dissolve

            au "Pfft, are you?"

            scene v15s35_9d
            with dissolve

            u "If I told you, I would have to kill you."

            scene v15s35_9h
            with dissolve

            pause 0.75

        scene v15s35_8d
        with dissolve

        aut "I'm convinced."

        scene v15s35_8a
        with dissolve

        u "I've already said too much."

        scene v15s35_9
        with dissolve

        au "*Sighs* I want to vote for myself."

        scene v15s35_7h
        with dissolve

        li "Haha, you can't!"

        scene v15s35_9
        with dissolve

        au "Lame!"

        if aubrey.relationship <= Relationship.MAD:
            scene v15s35_9o
            with dissolve

            u "I wouldn't vote for myself because I may already be one."

            scene v15s35_10 # TPP. Show an angle where you can only see Mc and Aubrey sitting at the table Mc winking towards Aubrey, Aubrey has a disgusted expression, looking at Mc
            with dissolve

            pause 0.75

            scene v15s35_10a # TPP. Same as v15s35_10 Aubrey is rolling her eyes, still a disgusted expression, Mc looks slightly sad still looking at Aubrey
            with dissolve

        elif aubrey.relationship >= Relationship.TAMED:
            scene v15s35_9d
            with dissolve

            u "I wouldn't vote for myself because I may already be one."

            scene v15s35_10b # TPP. Same as v15s35_10 Aubrey is looking at Mc seductively, Mc is still winking at Aubrey
            with dissolve

            pause 0.75

        else:
            scene v15s35_9d
            with dissolve

            u "I wouldn't vote for myself because I may already be one."

            scene v15s35_10c # TPP. same as v15s35_10 Aubrey flips her hair back with one hand and extends a "finger pistol" towards Mc she has a slight smile, Mc is still winking at Aubrey
            with dissolve

            pause 0.75

        scene v15s35_7h
        with dissolve

        li "Well, let's all vote before some assassins arrive for a shootout."

    # -We enter the UI for Most likely to-

    # -After MC votes for a person, we see on the UI who everyone has chosen. Lindsey and Autumn voted for Aubrey. Aubrey voted for MC-

        $ screen_options = [
            {
                "character": aubrey,
                "votes": [autumn, lindsey],
                "label": "v15s35_wml3"
            },
            {
                "character": autumn,
                "votes": [],
                "label": "v15s35_wml3"
            },
            {
                "character": lindsey,
                "votes": [],
                "label": "v15s35_wml3"
            },
            {
                "character": mc,
                "votes": [aubrey],
                "label": ""
            }
        ]
        call screen whos_most_likely_to("Most likely to become a super sexy spy?")

    label v15s35_wml3:
        if aubrey.relationship <= Relationship.MAD:
            scene v15s35_9t # FPP. same as v15s35_9o Aubrey is avoiding eye contact with Mc, still no expression, mouth is still closed
            with dissolve

            pause 0.75

        scene v15s35_7h
        with dissolve

        li "Aubrey is the new James Bond!"

        scene v15s35_9u # FPP. same as v15s35_9 Aubrey is striking a sexy/seuctive pose, still facing Lindsey, mouth is open
        with dissolve

        au "Am I? Yes! Now I need to go practice my seduction techniques so I can steal top secret government files..."

        scene v15s35_9d
        with dissolve

        u "How are you with a gun?"

        scene v15s35_9b
        with dissolve

        au "Hmm, I'll have to practice that too."

        scene v15s35_8b
        with dissolve

        aut "You can always get Moneypussy to help."

        scene v15s35_8d
        with dissolve

        u "*Laughs* Moneypussy?"

        scene v15s35_8m
        with dissolve

        aut "Yeah, there's a character called Moneypussy, isn't there?"

        scene v15s35_7i
        with dissolve

        li "*Laughs* Not in any of the movies I've seen."

        scene v15s35_9v # FPP. same as v15s35_9h Aubrey is leaning back in her chair laughing, full smile, facing Autumn
        with dissolve

        pause 0.75

        scene v15s35_9a
        with dissolve

        au "Money... Moneypussy?! *Laughs* You're killing me Autumn... Phew."

        scene v15s35_8b
        with dissolve

        aut "Haha, sorry! I thought that's what his name was..."

        scene v15s35_8n
        with dissolve

        u "I wish that was someone's name."

        scene v15s35_7b
        with dissolve

        li "Now we've got question number four..."

        scene v15s35_7b
        with dissolve

        li "Who is most likely to get caught having sex on an airplane?"

        if "v11_aubrey" in sceneList:
            scene v15s35_9w # FPP. same as v15s35_9h Aubrey is looking at Lindsey, trying to cover her laughter with her mouth, mouth is still open
            with dissolve

            au "*Laughs*"

            scene v15s35_7l # FPP. same as v15s35_7h Lindsey has a full smile, still looking at Aubrey, mouth is still open
            with dissolve

            li "Judging by the laugh, I'm guessing someone already did it."

            scene v15s35_9x # FPP. same as v15s35_9 Aubrey has a finger to her lips seductively, still looking at Lindsey, still a slight smile, mouth is still open
            with dissolve

            au "Maybe..."

            u "(I'm not sure I want everyone knowing about us on the plane, haha.)"

            scene v15s35_8b
            with dissolve

            aut "She's just trying to win all the votes again."

            scene v15s35_8a
            with dissolve

            u "She totally is, don't fall for it."

            if aubrey.relationship > Relationship.MAD:
                scene v15s35_9j
                with dissolve

                u "(Think we dodged that one.)"

        else:
            scene v15s35_9
            with dissolve

            au "Oh, I almost did once. But the guy didn't want to join me..."

            scene v15s35_7h
            with dissolve

            li "What an idiot!"

            if v11s13_rejected_aubrey:
                scene v15s35_9w
                with dissolve

                u "(Is she talking about me?)"

            if aubrey.relationship > Relationship.MAD:
                scene v15s35_9y # FPP. same as v15s35_9d Aubrey is pouting cutely at Mc, still looking at Mc, mouth is still closed
                with dissolve

                pause 0.75

            else:
                scene v15s35_9t
                with dissolve

                pause 0.75

            scene v15s35_9
            with dissolve

            au "There's always next time. *Giggles*"

            scene v15s35_8b
            with dissolve

            aut "You're just saying that to win all the votes again."

            scene v15s35_9a
            with dissolve

            au "Oh, so you think you're the most likely person for this one, then?"

            scene v15s35_8o # FPP. same as v15s35_8m Autumn is looking at Aubrey, mouth is still open, still no expression
            with dissolve

            aut "Um... No."

            scene v15s35_8e
            with dissolve

            u "Very hesitant there, Autumn... *Laughs*"

            scene v15s35_8m
            with dissolve

            aut "Maybe, but not because she's right."

            scene v15s35_7d
            with dissolve

            li "Let's vote and see what everyone thinks."

    # -We enter the UI for Most likely to-

    # -After MC votes for a person, we see on the UI who everyone has chosen. Lindsey voted for Aubrey. Autumn voted for Lindsey. Aubrey voted for MC-

        $ screen_options = [
            {
                "character": aubrey,
                "votes": [lindsey],
                "label": "v15s35_wml4_aub"
            },
            {
                "character": autumn,
                "votes": [],
                "label": "v15s35_wml4_aut"
            },
            {
                "character": lindsey,
                "votes": [autumn],
                "label": "v15s35_wml4_lin"
            },
            {
                "character": mc,
                "votes": [aubrey],
                "label": ""
            }
        ]
        call screen whos_most_likely_to("Most likely to get caught having sex on a plane?")

    label v15s35_wml4_aub:
        scene v15s35_7h
        with dissolve

        li "The votes are in. Aubrey is definitely most likely!"

        scene v15s35_9
        with dissolve

        au "Was it ever in doubt?"

        scene v15s35_8b
        with dissolve

        aut "Just another one of Aubrey's sexual adventures, hehe."

        scene v15s35_9a
        with dissolve

        au "You've gotta spice things up, ladies! Haven't you ever done anything like that?"

        scene v15s35_8b
        with dissolve

        aut "Nope. And I don't think I ever would."
        
        jump v15s35_wml4_end

    label v15s35_wml4_aut:
        scene v15s35_7b
        with dissolve

        li "It's a four-way tie!"

        scene v15s35_7c
        with dissolve

        u "Do you think we could all fit in an airplane bathroom?"

        if aubrey.relationship > Relationship.MAD:
            scene v15s35_9h
            with dissolve

            au "Haha, only one way to find out!"

        scene v15s35_8b
        with dissolve

        aut "Not happening, haha!"
        
        jump v15s35_wml4_end

    label v15s35_wml4_lin:
        scene v15s35_7d
        with dissolve

        li "Me? Haha, no way."

        scene v15s35_9
        with dissolve

        au "You're smiling, so you obviously like the sound of it..."

        scene v15s35_7m # FPP. same as v15s35_7h Lindsey is blushing, still looking at Aubrey, mouth is still open, still a slight smile
        with dissolve

        pause 0.75

        scene v15s35_9
        with dissolve

        au "That's why I voted for you. You protest like you're all innocent, but you totally would!"

        scene v15s35_7m
        with dissolve

        li "Ha, stop it! I mean, I'm not going to lie, it sounds hot... I would just hate to get caught."

        scene v15s35_7c
        with dissolve

        u "Yeah, I think in all the excitement you'd forget to lock the door, haha."

        if v11_aubrey_sex and aubrey.relationship > Relationship.MAD:
            scene v15s35_9
            with dissolve

            au "It happens more often than you think..."

            pause 0.75

            scene v15s35_9j
            with dissolve

        elif v11_aubrey_sex and aubrey.relationship <= Relationship.MAD:
            scene v15s35_9
            with dissolve

            au "It happens more often than you think..."

            pause 0.75

            scene v15s35_9t
            with dissolve

        scene v15s35_8b
        with dissolve

        aut "I'd never put myself in that situation."

    label v15s35_wml4_end:
        scene v15s35_9a
        with dissolve

        au "You never know."

        scene v15s35_8o
        with dissolve

        aut "Yeah, I do..."

        scene v15s35_8m
        with dissolve

        aut "There's something I want to share with you guys, I think."

        scene v15s35_7n # FPP. same as v15s35_7k Lindsey is looking at Autumn, still no expression, mouth is still open
        with dissolve

        li "Of course, Autumn. Anything."

        scene v15s35_8p # FPP. same as v15s35_8o Autumn is looking at Lindsey, still no expression, mouth is still open
        with dissolve

        aut "Well..."

        scene v15s35_8m
        with dissolve

        aut "I'm asexual."

        scene v15s35_9s
        with dissolve

        pause 0.75

        scene v15s35_8o
        with dissolve

        aut "So it's fairly easy for me to say no... Especially to airplane sex where you're guaranteed to get caught, ha."

        scene v15s35_8e
        with dissolve

        u "You're asexual?"

        scene v15s35_8m
        with dissolve

        aut "Yeah."

        scene v15s35_9g
        with dissolve

        au "What exactly does that mean?"

# -Regardless of game choice

    label v15s35_autumn_reveal:
        scene v15s35_8o
        with dissolve

        aut "I just don't desire sex. I don't get the urges that you all have."

        scene v15s35_7n
        with dissolve

        li "So, you've never wanted to try it?"

        scene v15s35_8p
        with dissolve

        aut "No, I've never felt the need to."

        scene v15s35_9g
        with dissolve

        au "Do you think you ever will?"

        scene v15s35_8n
        with dissolve

        pause 0.75

        scene v15s35_8o
        with dissolve

        aut "Maybe?"

        scene v15s35_8m
        with dissolve

        aut "I mean... You never know."

        scene v15s35_8o
        with dissolve

        aut "But... I doubt it."

        scene v15s35_8n
        with dissolve

        u "(That might be enough for right now...)"

        scene v15s35_8n
        with dissolve

        menu:
            "Stop the questions":
                $ add_point(KCT.BRO)
                $ add_point(KCT.BOYFRIEND)
                if protest or v15_autumn_lunchbreak: # -if Stop the questions (and helped Autumn with boxes at dog shelter and/or went to the protest with her in Act1, creates AutumnTrust)
                    $ autumn.relationship = Relationship.TRUST

                scene v15s35_9o
                with dissolve

                u "So, shall we move on? Maybe interrogate Autumn some other time? *Chuckles*"

                scene v15s35_9e
                with dissolve

                pause 0.75

                scene v15s35_9g
                with dissolve

                au "Oh, yeah. Of course! Sorry, Autumn. I didn't mean to-"

                scene v15s35_8o
                with dissolve

                aut "It's okay. I.. I chose to bring it up. But yeah, let's have another drink?"

                scene v15s35_9a
                with dissolve

                au "Yes!"

                scene v15s35_8d
                with dissolve

                aut "Thanks, [name]."

                scene v15s35_8a
                with fade

                u "Sure thing."

            "Ask one more":
                $ add_point(KCT.TROUBLEMAKER)

                scene v15s35_8n
                with dissolve

                u "So, do you know if you would be into guys or girls, or both?"

                scene v15s35_8q # FPP. same as v15s35_8n Autumn is even more embarrased, covering her body with her arms, avoiding eye contact with everyone, mouth is still closed
                with dissolve

                pause 0.75

                scene v15s35_8r # FPP. same as v15s35_8q Autumn's mouth is open everything else is the same
                with dissolve

                aut "..."

                aut "Um..."

                scene v15s35_7k
                with dissolve

                li "I think we may be getting a bit too personal now."

                scene v15s35_7n
                with dissolve

                li "You don't have to keep talking about this, Autumn. Can I get anyone another drink?"

                scene v15s35_8p
                with dissolve

                aut "Thanks, Lindsey. Another drink sounds great."

                scene v15s35_8e
                with dissolve

                u "Oh, sorry about that."

                scene v15s35_8m
                with fade

                aut "No worries. I brought it up, ha."

        scene v15s35_11 # TPP. Show Lindsey pouring a couple of liquids into a cocktail shaker can be different juice colours or the same color, slight smile, mouth closed
        with dissolve

        pause 0.75

        scene v15s35_11a # TPP. same as v15s35_11 Show Lindsey shaking the cocktail shaker, still slight smile, still mouth closed
        with dissolve

        pause 0.75

        scene v15s35_11b # TPP. same as v15s35_11 Show Lindsey pouring drinks into glasses, 4 glasses total, still slight smile, still mouth closed
        with dissolve

        pause 0.75

        scene v15s35_6g # TPP. same as v15s35_6 Lindsey approaches the table with the drinks from render v15s35_11b, Lindsey has a slight smile mouth is open, Autumn, Aubrey and Mc are still sitting in their original seats looking at Lindsey all of them have slight smiles, mouths are closed
        with dissolve

        li "Drinks are served!"

        scene v15s35_6h # TPP. same as v15s35_6h Lindsey is handing a drink to Aubrey, slight smile mouth is closed, Aubrey's mouth is open still a slight smile, Autumn and Mc are looking at Lindsey slight smiles mouths are closed
        with dissolve

        au "These look even better than the last ones!"

        scene v15s35_6i # TPP. Lindsey sits down in her seat, Everyone now has their new drinks in their hands, all slight smiles all mouths closed Autumn Aubrey and Mc looking at Lindsey, Lindsey looking at Aubrey
        with dissolve

        pause 0.75

        scene v15s35_12 # FPP. Use the same positioning and background from renders v15s35_7, Lindsey takes a drink from her glass (if different colors for drinks were used make sure she has the color of the one she gave herself,) all v15s35_12 renders Lindsey will be holding her drink unless otherwise stated
        with dissolve

        pause 0.75

        scene v15s35_12a # FPP. same as v15s35_12 Lindsey's is holding her glass it is 3/4 full (Lindsey will be holding her drink in all all v15s35_12 renders unless otherwise stated), slight smile, mouth is open, looking at Autumn
        with dissolve

        li "So, I just want to talk about something really quick and then we can get back to having fun, okay?"

        scene v15s35_13 # FPP. Use the same positioning and background from renders v15s35_8, Autumn is holding her drink it is full (if different colors for drinks were used make sure she has the color of the one she gave herself,) all v15s35_13 renders Autumn will be holding her drink unless otherwise stated, slight smile, mouth is open, looking at Lindsey
        with dissolve

        aut "Is this the part where we talk about your campaign?"

        scene v15s35_12b # FPP. same as v15s35_12a Lindsey is looking at Mc, mouth is closed, still a slight smile, her glass is still 3/4 full
        with dissolve

        u "The big campaign speech?"

        scene v15s35_12c # FPP. same as v15s35_12b Lindsey's mouth is open, still looking at Mc, still a slight smile, her glass is still 3/4 full
        with dissolve

        li "Haha, yeah. It's about supporting me."

        scene v15s35_14 # FPP. Use the same positioning and background from renders v15s35_9, Autumn is holding her drink it is full (if different colors for drinks were used make sure she has the color of the one she gave herself,) all v15s35_14 renders Aubrey will be holding her drink unless otherwise stated, slight smile, mouth is open, looking at Lindsey
        with dissolve

        au "That's okay. Go ahead."

        scene v15s35_12d # FPP. same as v15s35_12a Lindsey is looking at Aubrey, no expression, mouth is still open, her glass is still 3/4 full
        with dissolve

        li "I just wanted to ask; What has Chloe ever done for you? Like, actually done for you?"

        if v15_chloe_lindseysabotage:
            scene v15s35_15 # TPP. Show only Mc sitting in his seat, reaching into his pant's pocket, looking at his pocket, slight smile, mouth is closed
            with dissolve

            u "(This might get juicy... Maybe I can try and record Lindsey bitching about Chloe?)"

            scene v15s35_15a # TPP. same as v15s35_15 MC takes out his phone to one side, keeping his phone lower than the table height so no-one can see his phone, and taps on it
            with dissolve

            pause 0.75

            scene v15s35_15
            with dissolve

            u "(Okay, it's recording. If I'm careful, maybe I can trick her into saying something bad too.)"

        scene v15s35_13a # FPP. same as v15s35_13 Autumn takes a drink from her glass
        with dissolve

        pause 0.75

        scene v15s35_13b # FPP. same as v15s35_13 Autumn has no expression, still looking at Lindsey, mouth is still open, her glass is 3/4 full now
        with dissolve

        aut "In general, Chloe's been good to me. She's helped me out with a few things in the past, but, well, nothing lately."

        aut "I've invited her to participate in some of the Deer events. She came to one, but all the others, she was a no-show. Not even a text to say sorry."

        scene v15s35_14a # FPP. same as v15s35_14 Aubrey takes a drink from her glass
        with dissolve

        pause 0.75

        scene v15s35_14b # FPP. same as v15s35_14 Aubrey has no expression, looking at Autumn, mouth is still open, her glass is 3/4 full now
        with dissolve

        au "She is the type of person who makes a lot of promises. She likes to tell people what they want to hear."

        scene v15s35_12c
        with dissolve

        li "Yeah, so she can get what she wants. She doesn't seem to follow up on any of her promises, does she?"

        scene v15s35_13a
        with dissolve

        aut "Not lately. But that doesn't mean she's a bad person."

        scene v15s35_12e # FPP. same as v15s35_12c Lindsey is looking at Autumn, still no expression, mouth is still open, her glass is still 3/4 full
        with dissolve

        li "I'm not saying she's a bad person. But is she capable of doing the job she's supposed to be doing?"

        scene v15s35_12c
        with dissolve

        li "This is the whole reason why I'm challenging her. It's nothing personal. I just think she should be doing more as our President."

        scene v15s35_12e
        with dissolve

        li "She should be supporting you at all your events, Autumn. Wouldn't you prefer that?"

        scene v15s35_13a
        with dissolve

        aut "Yeah, I would."

        scene v15s35_12c
        with dissolve

        li "I want to create an environment where we can rely on each other."

        scene v15s35_12e
        with dissolve

        li "To me, supporting other sororities benefits everyone, and that's why we're all here, right?"

        scene v15s35_13a
        with dissolve

        aut "Right."

        scene v15s35_12c
        with dissolve

        li "We all want our experiences to be the best they can be."

        scene v15s35_12e
        with dissolve

        li "We can maintain healthy rivalries or whatever, but we need to be there for each other... And Chloe doesn't seem to get that."

        scene v15s35_13a
        with dissolve

        aut "I totally understand what you're saying. It's a better approach for sure."

        scene v15s35_14a
        with dissolve

        au "I've been trying to stay out of this whole thing as much as possible, but I agree with what you're saying, Lindsey."

        scene v15s35_12f # FPP. same as v15s35_12 Lindsey is looking at Aubrey, still a slight smile, mouth is still open, her glass is still 3/4 full
        with dissolve

        li "Thank you. It means a lot that you both feel the same way."

        scene v15s35_12a
        with dissolve

        if v15_chloe_lindseysabotage:
            if v15_lindsey_alcohol:
                scene v15s35_12a
                with dissolve

                u "(It'll help if Lindsey's more drunk. She'll be easier to trick into bad-mouthing Chloe.)"

                scene v15s35_12a
                with dissolve

                menu:
                    "Stay quiet":
                        $ add_point(KCT.BRO)

                        if chloe.relationship >= Relationship.GIRLFRIEND:
                            $ add_point(KCT.TROUBLEMAKER)

                        if hangOutWithLindsey:
                            $ add_point(KCT.BOYFRIEND)

                        scene v15s35_12a
                        with dissolve

                        u "(Not feeling that this is the best time.)"

                        scene v15s35_14c # FPP. same as v15s35_14b Aubrey's mouth is open, looking at Lindsey, still a slight smile, her glass is still 3/4 full
                        with dissolve

                        au "I think we've talked enough about Chloe now anyway."

                        scene v15s35_13c # FPP. same as v15s35_13 Autumn's glass is 3/4 full, still a slight smile, still looking at Lindsey, mouth is still open
                        with dissolve

                        aut "Yeah, I'm feeling pretty sleepy."

                        scene v15s35_12a
                        with dissolve

                        u "It's been a long day for sure, but I had a great time."

                        scene v15s35_13c
                        with dissolve

                        aut "Yeah, it was a lot of fun Lindsey!"

                        scene v15s35_14c
                        with dissolve

                        au "We should definitely do it again sometime."

                        scene v15s35_12f
                        with dissolve

                        li "Aw, yes, we will!"

                        scene v15s35_14d # FPP. same as scene v15s35_14c Aubrey stands up from her chair, her mouth is closed, still a slight smile, looking at Mc, her glass is still 3/4 full and sitting on the table not in her hand
                        with dissolve

                        pause 0.75

                    "Offer shots":
                        $ add_point(KCT.TROUBLEMAKER)

                        if chloe.relationship >= Relationship.GIRLFRIEND:
                            $ add_point(KCT.BOYFRIEND)

                        if hangOutWithLindsey:
                            $ add_point(KCT.TROUBLEMAKER)

                        scene v15s35_12a 
                        with dissolve

                        u "Let's take shots!"

                        scene v15s35_12g # FPP. same as v15s35_12b Lindsey has no expression, still looking at Mc, mouth is still open, her glass is still 3/4 full
                        with dissolve

                        li "We're in the middle of something here, [name]."

                        scene v15s35_12h # FPP. same as v15s35_12g Lindsey's mouth is closed, still looking at Mc, still no expression, her glass is still 3/4 full
                        with dissolve

                        u "Yeah, but look at the time. It's shots o'clock!"

                        scene v15s35_16 # TPP. show MC in the kitchen, show Mc holding an alcohol bottle pouring it into 3 shot glasses in front of him, and a second different style alcohol bottle same color liquid as the one he is pouring on the counter, he has a slight smile, mouth is closed
                        with dissolve

                        pause 0.75

                        scene v15s35_16a # TPP. same as v15s35_16 MC has put down the first bottle and grabs the second bottle, same colour liquid as the first, and fills a 4th shot glass with it, still a slight smile, mouth is still closed
                        with dissolve

                        u "(I'll put something extra strong in Lindsey's glass.)"

                        scene v15s35_6j # TPP. same as v15s35_6j Show Mc coming back to the table with the 4 filled shot glasses, Autumn Aubrey and Lindsey are sitting in their seats all looking at Mc all slight smiles all mouths are closed, if possible show all of their drinks in their hands 3/4 full (not necessary if not possible)
                        with dissolve

                        pause 0.75

                        scene v15s35_12i # FPP. same as v15s35_12b Lindsey's glass is 3/4 full, still looking at Mc, still a slight smile, mouth is still open
                        with dissolve

                        li "I'm already buzzed, though. I don't think I can handle a shot, ha."

                        scene v15s35_14e # FPP. same as v15s35_14c Aubrey is looking at Mc, still a slight smile, mouth is still open, her glass is still 3/4 full
                        with dissolve

                        au "I want one!"

                        scene v15s35_14c
                        with dissolve

                        u "That's what I like to hear!"

                        scene v15s35_6k # TPP. same as v15s35_6j All of them are standing where they were seated, MC is handing a shot glass to Lindsey slight smile mouth is closed, Lindsey is taking the glass from Mc, no expression mouth is closed, Aubrey and Autumn are looking at Mc holding their shot glasses, both of them slight smiles, mouths are closed
                        with dissolve

                        pause 0.75

                        scene v15s35_6l # TPP. same as v15s35_6k All of them raise their shot glasses together if possible otherwise just show them raising them in the air, Mc's mouth is open, All of them slight smiles, Aubrey Lindsey and Autumn's mouths are closed
                        with dissolve

                        u "3, 2, 1. Shots!"

                        scene v15s35_6m # TPP. same as v15s35_6l They all drink their shots
                        with dissolve

                        pause 0.75

                        scene v15s35_12j # FPP. same as v15s35_12i Lindsey's face is rosey from being drunk, still a slight smile, still looking at Mc, mouth is still open, her glass is still 3/4 full
                        with dissolve

                        li "*Drunk* Okay, now what was I saying?"

                        scene v15s35_12k # FPP. same as v15s35_12j Lindsey's mouth is closed, still looking at Mc, still a slight smile, her glass is still 3/4 full, still a rosey face from being drunk
                        with dissolve

                        u "(This is my chance...)"

                        scene v15s35_12k
                        with dissolve

                        menu (fail_label="v15s35_let_it_happen"):
                            "Let it happen naturally":
                                $ add_point(KCT.BRO)

                                if chloe.relationship >= Relationship.GIRLFRIEND:
                                    $ add_point(KCT.TROUBLEMAKER)

                                jump v15s35_let_it_happen

                            "Bring up Chloe":
                                $ v15s35_bring_up_chloe = True
                                $ add_point(KCT.TROUBLEMAKER)
                                
                                if chloe.relationship >= Relationship.GIRLFRIEND:
                                    $ add_point(KCT.BOYFRIEND)
                                    
                                if hangOutWithLindsey:
                                    $ add_point(KCT.TROUBLEMAKER)
                                    
                                jump v15s35_bring_up_chloe
                            
                        label v15s35_let_it_happen:
                            scene v15s35_12k
                            with dissolve

                            u "(Let's see if she makes a mess on her own.)"

                            scene v15s35_14c
                            with dissolve

                            au "Eh, we get the jist. *Chuckles*"

                            scene v15s35_12l # FPP. same as v15s35_12j Lindsey is looking at Autumn, still a slight smile, mouth is still open, her glass is still 3/4 full, still a rosey face from being drunk
                            with dissolve

                            li "*Drunk* Anyway, I think that's all I had to say..."

                            scene v15s35_12m # FPP. same as v15s35_12l Lindsey is looking at Aubrey, still a slight smile, mouth is still open, her glass is still 3/4 full, still a rosey face from being drunk
                            with dissolve

                            li "Just please think about what I've said and consider supporting me. Please?"

                            scene v15s35_13c
                            with dissolve

                            aut "I totally will."

                            scene v15s35_14c
                            with dissolve

                            au "Yeah, everything you've said makes a lot of sense."

                            scene v15s35_12m
                            with dissolve

                            li "*Drunk* Thanks girlies!"

                            scene v15s35_12l
                            with dissolve

                            li "*Drunk* We should probably end the night here before I pass out on you guys, haha!"

                            scene v15s35_13c
                            with dissolve

                            aut "*Chuckles* I had a great time. I'm so glad I came."

                            scene v15s35_12k
                            with dissolve

                            u "Yeah, it's been fun!"

                            scene v15s35_14c
                            with dissolve

                            au "Let's do it again sometime."

                            scene v15s35_12m
                            with dissolve

                            li "*Drunk* Yes! That sounds perfect."

                        label v15s35_bring_up_chloe:
                            scene v15s35_12k
                            with dissolve

                            u "You were telling us what you don't like about Chloe."

                            scene v15s35_12j
                            with dissolve

                            li "*Drunk* What I don't like about Chloe?"

                            scene v15s35_12k
                            with dissolve

                            u "Yeah, the most annoying things about her?"

                            scene v15s35_14f # FPP. same as v15s35_14e Aubrey has a concerned/worried expression, mouth is closed, still looking at Mc, her glass is still 3/4 full
                            with dissolve

                            pause 0.75

                            scene v15s35_12d
                            with dissolve

                            pause 0.75

                            scene v15s35_12n # FPP. same as v15s35_12j Lindsey's glass is now half full, still a slight smile, still looking at Mc, mouth is still open, still a rosey face from being drunk
                            with dissolve

                            li "*Giggles* do you want a list? I mean, where do I start?"

                            scene v15s35_13b
                            with dissolve

                            aut "Um..."

                            scene v15s35_12n
                            with dissolve

                            $ set_presidency_percent(v14_lindsey_popularity - 3)

                            li "*Drunk* Her plastic boobs?"

                            scene v15s35_14f
                            with dissolve

                            u "(Oof.)"

                            scene v15s35_12n
                            with dissolve

                            $ set_presidency_percent(v14_lindsey_popularity - 3)

                            li "*Drunk* Or her plastic nose?"

                            scene v15s35_14g # FPP. same as v15s35_14f Aubrey is looking at Lindsey, mouth is open, still a worried/concerned expression, her glass is still 3/4 full
                            with dissolve

                            au "I think that's enough, Lindsey."

                            scene v15s35_12d
                            with dissolve

                            pause 0.75

                            scene v15s35_14f
                            with dissolve

                            menu (fail_label="v15s35_stop_lindsey"):
                                "Stop Lindsey":
                                    $ add_point(KCT.BRO)
                                    
                                    if chloe.relationship >= Relationship.GIRLFRIEND:
                                        $ add_point(KCT.TROUBLEMAKER)
                                        
                                    if hangOutWithLindsey:
                                        $ add_point(KCT.BOYFRIEND)
                                        
                                    jump v15s35_stop_lindsey

                                "Say nothing":
                                    $ v15_say_nothing = True
                                    $ add_point(KCT.TROUBLEMAKER)
                                    
                                    if chloe.relationship >= Relationship.GIRLFRIEND:
                                        $ add_point(KCT.BOYFRIEND)
                                        
                                    if hangOutWithLindsey:
                                        $ add_point(KCT.TROUBLEMAKER)
                                        
                                    jump v15s35_say_nothing

                            label v15s35_stop_lindsey:
                                scene v15s35_12o # FPP. same as v15s35_12n Lindsey's glass is now empty, mouth is closed, still a slight smile, still a rosey face from being drunk
                                with dissolve

                                u "Yeah, maybe stop talking now... Ha."

                                scene v15s35_12p # FPP. same as v15s35_12o Lindsey has a worried/concerned expression, mouth is open, still looking at Mc, her glass is still Empty
                                with dissolve

                                $ set_presidency_percent(v14_lindsey_popularity + 3)

                                li "*Drunk* Whoops! I probably just sounded like such a bitch. I'm sorry..."

                                scene v15s35_13c
                                with dissolve

                                aut "It happens. Drinking can turn people's moods just like that."

                                scene v15s35_14c
                                with dissolve

                                au "It's probably a good time to end the night anyway."

                                scene v15s35_12q # FPP. same as v15s35_12p Lindsey is looking at Aubrey, still has a worried/concerned expression, mouth is still open, her glass is still empty
                                with dissolve

                                li "*Drunk* Yeah, okay. It is getting late."

                                scene v15s35_14h # FPP. same as scene v15s35_14d Aubrey has no expression, is still standing up from her chair, her mouth is closed, still looking at Mc, her glass is still 3/4 full and sitting on the table not in her hand
                                with dissolve

                                pause 0.75

                            label v15s35_say_nothing:
                                scene v15s35_12r # FPP. same as v15s35_12o Lindsey's mouth is open, still looking at Mc, still a slight smile, her glass is still empty, still a rosey face from being drunk
                                with dissolve

                                li "*Drunk* That's why she's doing everything she can to not lose her scholarship."

                                li "She'd have to sell a good chunk of her body back to the surgeons in order to pay for school, ha!"

                                scene v15s35_14i # FPP. same as v15s35_14g Aubrey has an angry expression, still looking at Lindsey, mouth is still open, her glass is still 3/4 full
                                with dissolve

                                au "Lindsey, stop. That's way too far."

                                scene v15s35_12q
                                with dissolve

                                li "*Drunk* Oh, shit... You're so right. Oh my-"

                                scene v15s35_12p
                                with dissolve

                                li "I'm so sorry. That was a horrible thing to say."

                                scene v15s35_12s # FPP. same as v15s35_12q Lindsey is looking at Autumn, still a worried/concerned expression, mouth is still open, her glass is still empty
                                with dissolve

                                li "*Drunk* I'm just stressed from all this campaign work... *Sighs* I shouldn't be getting this drunk. I'm really, really sorry."

                                scene v15s35_15
                                with dissolve

                                pause 0.75

                                scene v15s35_15a
                                with dissolve

                                u "(Thank you, Lindsey! That's exactly what I needed!)"

                                scene v15s35_15
                                with dissolve

                                pause 0.75

                                scene v15s35_13d # FPP. same as v15s35_13c Autumn has a slightly angry expression, still looking at Lindsey, mouth is still open, her glass is still 3/4 full
                                with dissolve

                                aut "I can't imagine how stressed you are, but you should go to bed now. Sleep it off and wake up with a new attitude."

                                scene v15s35_12s
                                with dissolve

                                li "*Drunk* Yeah, you're right..."

                                scene v15s35_14j # FPP. same as scene v15s35_14h Aubrey has a slightly angry expression, still standing up from her chair, her mouth is closed, still looking at Mc, her glass is still 3/4 full and sitting on the table not in her hand
                                with dissolve

                                pause 0.75
            
            else:
                scene v15s35_12a
                with dissolve

                u "(This is going to be almost impossible without alcohol. I can try to trick Lindsey, but I doubt she'll take the bait.)"

                scene v15s35_12a
                with dissolve

                menu:
                    "Say nothing":
                        $ add_point(KCT.BRO)
                        
                        if chloe.relationship >= Relationship.GIRLFRIEND:
                            $ add_point(KCT.TROUBLEMAKER)
                            
                        if hangOutWithLindsey:
                            $ add_point(KCT.BOYFRIEND)

                        scene v15s35_12a
                        with dissolve

                        u "(It's not even worth trying...)"

                        scene v15s35_14c
                        with dissolve

                        au "I think we've talked enough about Chloe now anyway."

                        scene v15s35_13c
                        with dissolve

                        aut "Yeah, I'm feeling pretty sleepy."

                        scene v15s35_12a
                        with dissolve

                        u "It's been a long day for sure, but I had a great time."

                        scene v15s35_13c
                        with dissolve

                        aut "Yeah, it was a lot of fun Lindsey!"

                        scene v15s35_14c
                        with dissolve

                        au "We should definitely do it again sometime."

                        scene v15s35_12f
                        with dissolve

                        li "Aw, yes, we will!"

                        scene v15s35_14d
                        with dissolve

                        pause 0.75
                        
                    "Try to trick her":
                        $ add_point(KCT.TROUBLEMAKER)
                        
                        if chloe.relationship >= Relationship.GIRLFRIEND:
                            $ add_point(KCT.BOYFRIEND)
                            
                        if hangOutWithLindsey:
                            $ add_point(KCT.TROUBLEMAKER)

                        scene v15s35_12a
                        with dissolve

                        u "Lindsey, be honest with us for a minute, what do you hate most about Chloe?"

                        scene v15s35_14k # FPP. same as v15s35_14i Aubrey has a slightly angry expression, looking at Mc, mouth is closed, her glass is still 3/4 full
                        with dissolve

                        pause 0.75

                        scene v15s35_12b
                        with dissolve

                        li "Haha, I don't hate her, [name]. She's my sorority sister."

                        li "I care about her. She's my campaign rival, but I don't hate her."

                        scene v15s35_12a
                        with dissolve

                        u "Not even a little bit?"

                        scene v15s35_14k
                        with dissolve

                        pause 0.75

                        if kct == "popular":
                            call screen kct_popup
                            scene v15s35_12b
                            with dissolve

                            $ set_presidency_percent(v14_lindsey_popularity - 3)

                            li "What do you want me to say? That her boobs are obviously fake? Everyone knows that I think."

                            scene v15s35_12a
                            with dissolve

                            u "I don't know, but you kind of just did."

                            scene v15s35_12b
                            with dissolve

                            li "Well, I did, but I didn't mean it in a bad way... I was just joking."

                        else:
                            call screen kct_popup(required_kct="popular")
                        
                            scene v15s35_12b
                            with dissolve

                            li "No. Not at all. Stop trying to cause trouble, [name], haha."

                        scene v15s35_14g
                        with dissolve

                        au "Is it okay if we stop talking about Chloe now?"

                        scene v15s35_13b
                        with dissolve

                        aut "Yeah, I'm ready to go, I think. Getting a little sleepy over here, haha."

                        scene v15s35_12c
                        with dissolve

                        li "Oh, okay. Well, thanks for listening to me anyway. I really appreciate it you guys."

                        scene v15s35_13c
                        with dissolve

                        aut "Of course, I had a great night. Thanks again for the invite."

                        scene v15s35_12a
                        with dissolve

                        u "Yeah, this was fun."

                        scene v15s35_14j
                        with dissolve

                        pause 0.75

        else: # -if helping/not helping Chloe and did not choose Embarrass Lindsey-
            scene v15s35_15b # TPP same as v15s35_15 Mc is stretching and yawning, eyes and mouth are closed
            with dissolve

            pause 0.75

            scene v15s35_12c
            with dissolve

            li "Oh, wow. Are we boring you?"

            scene v15s35_12b
            with dissolve

            u "I'm sorry, it's been a long day, haha."

            scene v15s35_13c
            with dissolve

            aut "Yeah, I need to get going if I plan on getting a good night's rest."

            scene v15s35_12b
            with dissolve

            u "This was fun, though."

            scene v15s35_14c
            with dissolve

            au "Yeah, I loved the game."

            scene v15s35_13c
            with dissolve

            aut "And the drinks!"

            scene v15s35_12a
            with dissolve

            li "Haha, thanks guys. I appreciate you all coming."

            scene v15s35_14d
            with dissolve

            pause 0.75

        scene v15s35_17 # FPP. Aubrey is walking up the stairs looking back and waving to everyone, slight smile, mouth is open
        with fade

        au "Goodnight, losers!"

        scene v15s35_18 # TPP. MC and Autumn walking out the Chicks front door together, waving to Lindsey, slight smiles, mouths are closed, Lindsey waving back at Mc and Autumn slight smile, mouth is open
        with dissolve

        li "Later guys, be safe!"

        scene v15s35_18a # TPP. same as v15s35_18 Lindsey has closed the door and is no longer visible, Autumn and Mc are looking at each other, Autumn's mouth is open slight smile hand extended out like she's explaining something, Mc's mouth is closed slight smile
        with fade

        $ v15s35_kiwiiPost1= KiwiiPost(lindsey, "v15/v15_linpost1.webp", "Always a good time with these good people <3 #GameNight", numberLikes=648)
        $ v15s35_kiwiiPost1.newComment(imre, "The fuck? Where's my invite?", numberLikes=renpy.random.randint(260, 560), force_send=True)
        $ v15s35_kiwiiPost1.newComment(riley, "Omg, I love game nights! Can I come to the next one?", numberLikes=renpy.random.randint(260, 560), force_send=True)
        $ v15s35_kiwiiPost1.newComment(lindsey, "Don't worry, everyone's invited next time. Promise!", numberLikes=renpy.random.randint(260, 560), force_send=True)
        # $ v15s35_kiwiiPost1.newComment(chloe, "I'd never leave you guys out, hope you had fun without the rest of us!", numberLikes=renpy.random.randint(260, 560), force_send=True)
        $ v15s35_kiwiiPost1.addReply("The more the merrier! Except you don't stand a chance when it comes to the games, Imre", v15s35_kiwiireply1, mentions=imre, numberLikes=renpy.random.randint(260, 560))
        $ v15s35_kiwiiPost1.addReply("It was a really good night, gonna have to do it again with the whole gang.", v15s35_kiwiireply2, numberLikes=renpy.random.randint(260, 560))

        stop music fadeout 3

        jump v15s36