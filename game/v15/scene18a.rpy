# SCENE 18a: Lauren Halloween Party Free Roam Part 1
# Locations: Deer's House/Rooms
# Characters: MC (Outfit: Stripper Costume), AUBREY (Outfit: Clown Costume), RYAN (Outfit: Elvis Costume), AUTUMN (Outfit: Mummy), PENELOPE (Outfit: Sexy Witch), LAUREN (Outfit: Spider necklace costume), IMRE (Outfit: Cowboy Costume), RILEY (Outfit: Schoolgirl Costume), CHRIS (Outfit: Boxer Costume), AMBER (Outfit: Black bloody nurse costume)
# Time: Night

label v15s18a:
    if False: #making sure it shows in Lint
        scene v15s18_kiwii_lauren1
        scene v15s18_kiwii_autumn2
        scene v15s18_kiwii_aubrey3
        scene v15s18_kiwii_aubrey4

    # -Refer to images on Miro for exact placement, but Downstairs: Aubrey at the bar, Imre & Lauren on the couch, Riley in the kitchen, Chris & Amber on bar stools at kitchen counter; Upstairs: Ryan in the bathroom, Autumn & Penelope in Autumn's bedroom
    # -Clickable Objects (placement is irrelevant to plot, available to click on during both free roams): A bronze deer statue, A photo of Autumn and Lauren, A carved Halloween pumpkin, A Deer scarf wall hanging-
    # -Characters are greyed out after they are spoken too besides Lauren. She needs to stay highlighted as she is the way to end the free roam-

    $ v15s18a_kiwiiPost1 = KiwiiPost(lauren, "Steamy and spooky photo of her costume before the party begins", _("Feeling one year older ;)"), numberLikes=854)
    $ v15s18a_kiwiiPost1.newComment(lindsey, _("Holy fuck, babe! You look spectacular, I hope you have the most amazing birthday <3"), numberLikes=renpy.random.randint(15, 35), queue=False)
    $ v15s18a_kiwiiPost1.newComment(autumn, _("Can't wait to celebrate! Happy Birthday, Renny <33"), numberLikes=renpy.random.randint(15, 35), queue=False)
    $ v15s18a_kiwiiPost1.newComment(chloe, _("Sorry I couldn't be there! I'm just so busy... Enjoy yourself and have the night of your life! Happy birthday :)"), numberLikes=renpy.random.randint(15, 35), queue=False)
    $ v15s18a_kiwiiPost1.newComment(amber, _("YES!! That costume is everything! Happy b-day hottie, see you in a bit <3"), numberLikes=renpy.random.randint(15, 35), queue=False)
    $ v15s18a_kiwiiPost1.newComment(lauren, _("Thank you ladies!!"), numberLikes=renpy.random.randint(15, 35), queue=False)

    $ v15s18a_kiwiiPost2 = KiwiiPost(autumn, "Photo of halloween decorations for the party whether it's inside or outside the house", _("Spooky sister season :)"), numberLikes=743)
    $ v15s18a_kiwiiPost2.newComment(penelope, _("I'll never understand your decorating skills... I'm so excited for tonight!"), numberLikes=renpy.random.randint(15, 35), queue=False)
    $ v15s18a_kiwiiPost2.newComment(lauren, _("The house looks absolutely perfect, I couldn't have asked for more! Love u <3"), numberLikes=renpy.random.randint(15, 35), queue=False)
    $ v15s18a_kiwiiPost2.newComment(riley, _("So fucking cool! You're planning my wedding one day, Autumn..."), numberLikes=renpy.random.randint(15, 35), queue=False)
    $ v15s18a_kiwiiPost2.newComment(autumn, _("Haha, sounds great!"), numberLikes=renpy.random.randint(15, 35), queue=False)

    pause 0.75
    
    call screen v15s18a_room

# -Free roam: Everyone can now be holding a drink. There's a punch bowl and food set up in the kitchen. MC can navigate around the house.

# Ground floor
# Location 1- At the bar in the deer's house
# *Clicking on Aubrey*
label v15s18a_Aubrey:
    $ freeroam13.add("aubrey")

    scene v15s18aaub_1 # TPP. Show MC starting to sit on the stool next to Aubrey, slight smile, mouth closed. Just show Aubrey's backside.
    #with dissolve

    pause 0.75

    scene v15s18aaub_2 # FPP. MC sitting on the stool next to Aubrey, Aubrey looking at MC, MC looking at Aubrey, Aubrey slight smile, mouth closed
    with dissolve

    u "Hey, Aubrey. I didn't know you were into clowns, haha."

    scene v15s18aaub_2a # FPP. MC sitting on the stool next to Aubrey, Aubrey looking at MC, MC looking at Aubrey, Aubrey slight smile, mouth open
    with dissolve

    au "I'm not, they're terrifying. *Laughs* I can't even look in the mirror right now..."

    scene v15s18aaub_2
    with dissolve

    u "Haha, what? Why would you dress up as one if you have a fear of them?"

    scene v15s18aaub_2a
    with dissolve

    au "It's Halloween! You have to be something scary, right? Plus, what better way to face a fear... Right? Ha... *Sighs*"

    scene v15s18aaub_2
    with dissolve

    u "*Chuckles* You sound like you might be struggling a bit, but you look fantastic."

    scene v15s18aaub_2a
    with dissolve

    au "Haha, thank you. But enough about me..."

    au "The strip club is in the center of town. You took a wrong turn somewhere!"

    scene v15s18aaub_2b # FPP. MC sitting on the stool next to Aubrey, Aubrey looking down at the lower half of MC, Aubrey laughing.
    with dissolve

    pause 0.75

    scene v15s18aaub_2c # FPP. MC sitting on the stool next to Aubrey, Aubrey looking back at MC's face, Aubrey laughing.
    with dissolve

    pause 0.75

    scene v15s18aaub_2
    with dissolve

    u "Haha... Good one. Let's just say I didn't have much of a choice."

    scene v15s18aaub_2a
    with dissolve

    au "Hey, I'm not complaining. I'm sure all the girls are enjoying the view."

    if aubrey.relationship.value >= Relationship.FWB.value:
        scene v15s18aaub_2d # FPP. MC sitting on the stool next to Aubrey, Aubrey looking at MC's face, flirty, mouth open
        with dissolve

        au "You should wear it more often..."

        scene v15s18aaub_2e # FPP. MC sitting on the stool next to Aubrey, Aubrey looking at MC's face, flirty, mouth closed, Biting her lip.
        with dissolve

        u "Ha, okay. Maybe I will."

        scene v15s18aaub_2d
        with dissolve

        au "Hmm, I do like the idea of having my own personal stripper."

        scene v15s18aaub_2f # FPP. MC sitting on the stool next to Aubrey, Aubrey looking at MC's face, flirty, mouth closed, not biting her lip
        with dissolve

        u "Oh, really? *Laughs*"

    scene v15s18aaub_2a
    with dissolve

    au "Maybe you can perform at my parent's wedding ceremony?"

    scene v15s18aaub_2
    with dissolve

    u "Haha! That's a wonderful idea, I'm sure your parents would love that."

    u "But I'm thinking of something more traditional for that, like a suit."

    scene v15s18aaub_2a
    with dissolve

    au "Aw, come on... That's so old fashioned. You should totally just wear that. *Laughs*"

    scene v15s18aaub_2
    with dissolve

    u "Haha, okay. We'll see who's laughing when I actually do show up in this thing."

    scene v15s18aaub_2a
    with dissolve

    au "Still me... *Chuckles*"

    scene v15s18aaub_2
    with dissolve

    u "Ha, that's exactly why I intend to burn this thing as soon as I get home."

    scene v15s18aaub_2a
    with dissolve

    au "*Sighs* What a waste."

    scene v15s18aaub_2
    with dissolve

    u "Speaking of, are you looking forward to the wedding?"

    scene v15s18aaub_2a
    with dissolve

    au "Yeah... I mean, it should be a lot of fun."

    au "Naomi will be there, so I can catch up with her a bit..."

    scene v15s18aaub_2g # FPP. MC sitting on the stool next to Aubrey, Aubrey looking at MC, MC looking at Aubrey, Aubrey slightly serious, mouth open
    with dissolve

    au "You'll get to witness the favoritism, ha."

    au "They don't even try to hide it, so... I'm just preparing myself for that, you know."

    scene v15s18aaub_2i # FPP. MC sitting on the stool next to Aubrey, Aubrey looking at MC, MC looking at Aubrey, Aubrey slight smile, mouth closed
    with dissolve

    menu:
        "We'll have fun":
            $ add_point(KCT.BRO)
            scene v15s18aaub_2
            with dissolve

            u "I get it, yeah... But we'll have a great time. I'll make sure of it."

            scene v15s18aaub_2a
            with dissolve

            au "Ha, yeah. You're right, we'll have fun."

        "I'll be there":
            $ add_point(KCT.BOYFRIEND)
            scene v15s18aaub_2
            with dissolve

            u "I know, but this time I'll be there."

            u "So, you're not alone. In fact, you're stuck with me."

            scene v15s18aaub_2a
            with dissolve

            au "*Laughs* I can't wait."

    au "Honestly, though..."

    au "I don't think I can forget the sight of you in this costume... *Chuckles*"

    scene v15s18aaub_2
    with dissolve

    u "Haha, that's a good thing, right?"

    if aubrey.relationship.value >= Relationship.FWB.value:
        scene v15s18aaub_2a
        with dissolve

        au "Yeah, a very good thing. Except, I want to make sure I never forget it, so..."

    scene v15s18aaub_3 # FPP. Aubrey with her back turned to MC, on the stool putting her camera up for a selfie with MC.
    with dissolve

    au "Say cheese! *Laughs*"

    scene v15s18aaub_4 # TPP. Show MC behind Aubrey as she leans back towards him, her hand holding her phone in the air for a selfie photo, Aubrey slight smile, mouth closed, MC serious face, mouth closed.
    with dissolve

    menu:
        "Smile":
            $ v15s18a_aub_kiwii_smile = True
            $ add_point(KCT.TROUBLEMAKER)
            scene v15s18aaub_4a # TPP. Show MC behind Aubrey as she leans back towards him, her hand holding her phone in the air for a selfie photo, Aubrey slight smile, mouth closed, MC slight smile, mouth closed.
            with flash

            pause 0.75

            scene v15s18aaub_2a
            with dissolve
            
            u "*Sighs* Thanks for the heads up..."

        "Don't smile":
            $ add_point(KCT.BOYFRIEND)
            scene v15s18aaub_4b # TPP. # TPP. Show MC behind Aubrey as she leans back towards him, her hand holding her phone in the air for a selfie photo, Aubrey slight smile, mouth closed, MC frown, mouth closed.
            with flash

            pause 0.75

            scene v15s18aaub_2
            with dissolve
            
            u "*Sighs* Thanks for the heads up..."

            
    scene v15s18aaub_2a
    with dissolve

    au "Haha, no problem! I can't wait for everyone to see your amazing costume."

    scene v15s18aaub_2j # FPP. MC sitting on the stool next to Aubrey, Aubrey looking at her phone we can't see the screen of, MC looking at Aubrey, Aubrey slight smile, mouth closed
    with dissolve

    u "(Great... Her tens of thousands of followers are going to love that.)"

    u "(Now might be a good time to bring up the list... Do I want Aubrey's help with it?)"

    menu:
        "Mention the list":
            $ v15s18_mention_list_aubrey = True
            $ add_point(KCT.TROUBLEMAKER)
            scene v15s18aaub_2
            with dissolve

            u "Haha, well... I have this list of challenges for the party tonight."

            scene v15s18aaub_2a
            with dissolve

            au "Oh, yeah? Let me see!"

            scene v15s18aaub_5 # FPP. Same camera as v15s18a_aub2, MC looking down slightly at his hand giving Aubrey the challenge paper, Aubrey grabbing the Challenge paper.
            with dissolve

            pause 0.75

            scene v15s18aaub_2k # FPP. MC sitting on the stool next to Aubrey, Aubrey looking at the list, MC looking at Aubrey, Aubrey shocked, mouth closed.
            with dissolve

            pause 0.75

            scene v15s18aaub_2l # FPP. MC sitting on the stool next to Aubrey, Aubrey looking at the list, MC looking at Aubrey, Aubrey smirking, mouth closed.
            with dissolve

            au "That's quite the list! Who gave you this?"

            scene v15s18aaub_2m # FPP. MC sitting on the stool next to Aubrey, Aubrey holding the paper, looking at MC, MC looking at Aubrey, Aubrey smiling, mouth closed.
            with dissolve

            u "Imre."

            scene v15s18aaub_2n # FPP. MC sitting on the stool next to Aubrey, Aubrey holding the paper, looking at MC, MC looking at Aubrey, Aubrey smiling, mouth open.
            with dissolve

            au "I knew it."

            scene v15s18aaub_2l
            with dissolve

            pause 0.75

            scene v15s18aaub_5a # FPP. Same camera as v15s18a_aub2, MC looking down slightly at his hand, Aubrey handing back the challenge paper, MC grabbing the challenge paper.
            with dissolve

            pause 0.75

            scene v15s18aaub_2a
            with dissolve

            au "So, I assume you're wanting me to help you out?"

            scene v15s18aaub_2
            with dissolve

            u "Well, if you wouldn't mind..."

            scene v15s18aaub_2a
            with dissolve

            au "Haha, so polite of you."

            scene v15s18aaub_2
            with dissolve

            u "I am trying to be, for what it's worth."

            scene v15s18aaub_2a
            with dissolve

            au "*Chuckles* Come find me a little later and I'll see what I can do to help."

            scene v15s18aaub_2
            with dissolve

            u "Okay, ha, that sounds perfect."

        "Don't mention the list":
            $ add_point(KCT.BOYFRIEND)
            scene v15s18aaub_2
            with dissolve

            u "(Maybe later. It's still early, so I have plenty of time.)"

            u "I'm gonna go say hi to the others, see you later."

            scene v15s18aaub_2a
            with dissolve

            au "Mhmm! Enjoy the party."

    if v15s18a_aub_kiwii_smile:
        $ v15s18a_kiwiiPost3 = KiwiiPost(aubrey, "Selfie with MC smiling at halloween party", _("Spooky season? More like stripper season ;)"), numberLikes=2492)
        $ v15s18a_kiwiiPost3.newComment(chloe, _("O. M. G."), numberLikes=renpy.random.randint(15, 35), queue=False)
        $ v15s18a_kiwiiPost3.newComment(naomi, _("Hahahaha! I have to come to one of these parties soon..."), numberLikes=renpy.random.randint(15, 35), queue=False)
        if joinwolves:
            $ v15s18a_kiwiiPost3.newComment(sebastian, _("Hell yeah! Can I borrow that outfit when you're done, [name]? :D"), numberLikes=renpy.random.randint(15, 35), queue=False)
        else:
            $ v15s18a_kiwiiPost3.newComment(grayson, _("What the fuck...?"), numberLikes=renpy.random.randint(15, 35), queue=False)
        $ v15s18a_kiwiiPost3.addReply(_("Lol, I love this. Happy birthday Lauren!"), numberLikes=renpy.random.randint(15, 35), mentions=[lauren])
        $ v15s18a_kiwiiPost3.newComment(lauren, _("Hehe, thank you!! You guys are the best <3"), numberLikes=renpy.random.randint(15, 35), queue=False)
        $ v15s18a_kiwiiPost3.addReply(_("Now taking appointments... ;)"), numberLikes=renpy.random.randint(15, 35))
        $ v15s18a_kiwiiPost3.newComment(naomi, _("Can I book you for my birthday party, too? ;D"), numberLikes=renpy.random.randint(15, 35), queue=False)

    else:
        $ v15s18a_kiwiiPost4 = KiwiiPost(aubrey, "Selfie with non-smiling MC at halloween party", _("I think something's wrong with our stripper... Is he supposed to be this sad? </3"), numberLikes=2415)
        $ v15s18a_kiwiiPost4.newComment(chloe, _("O. M. G."), numberLikes=renpy.random.randint(15, 35), queue=False)
        $ v15s18a_kiwiiPost4.newComment(naomi, _("Aww! You need to cheer him up, little sis! Or I will... ;)"), numberLikes=renpy.random.randint(15, 35), queue=False)
        if joinwolves:
            $ v15s18a_kiwiiPost4.newComment(sebastian, _("Lmao, show them how it's done, [name]! #SadboyStriptease"), numberLikes=renpy.random.randint(15, 35), queue=False)
        else:
            $ v15s18a_kiwiiPost4.newComment(grayson, _("What the fuck is this"), numberLikes=renpy.random.randint(15, 35), queue=False)
        $ v15s18a_kiwiiPost4.addReply(_("Sigh... Happy birthday Lauren! Lol"), numberLikes=renpy.random.randint(15, 35), mentions=[lauren])
        $ v15s18a_kiwiiPost4.newComment(lauren, _("Hahaha! Thank you guys <3"), numberLikes=renpy.random.randint(15, 35), queue=False)
        $ v15s18a_kiwiiPost4.addReply(_("Now taking appointments... ;)"), numberLikes=renpy.random.randint(15, 35))
        $ v15s18a_kiwiiPost4.newComment(naomi, _("Can I book you for my birthday party, too? ;D"), numberLikes=renpy.random.randint(15, 35), queue=False)

    pause 0.75
    
    call screen v15s18a_bar

# Upstairs
# Location 2- Bathroom on Upstairs of deer's house:
# *Clicking on Bathroom*
label v15s18a_Ryan:
    $ freeroam13.add("ryan")

    scene v15s18a_ryan_1 # TPP. Show MC standing outside the bathroom, slight smile, mouth closed
    #with dissolve

    u "(I think this is the bathroom...?)"

    play sound "sounds/dooropen.mp3"

    scene v15s18a_ryan_2 # TPP. Show MC entering into the bathroom, as he enters we see Ryan sitting on the floor with his head above the toilet since he is puking, his face obscured by the toilet and we don't ever see inside it.
    with dissolve

    pause 1.25

    scene v15s18a_ryan_3 # FPP. MC looking at Ryan, Ryan's face still obscured by toilet, Ryan disgusted face, mouth closed.
    with dissolve

    u "Oh- Uh, Ryan?"

    scene v15s18a_ryan_3a # FPP. MC looking at Ryan, Ryan's face still obscured by toilet, Ryan disgusted face, mouth open.
    with dissolve

    ry "*Groans*"

    scene v15s18a_ryan_3
    with dissolve

    u "Jeez, you're drunk already? *Chuckles*"

    scene v15s18a_ryan_3a
    with dissolve

    ry "No... Ugh..."

    ry "Too much candy..."

    ry "Every year...I never learn. Why do I never- *Pukes*"

    scene v15s18a_ryan_3a
    with dissolve
    
    menu:
        "Gag":
            $ v15s18a_gag = True

            scene v15s18a_ryan_3
            with dissolve

            u "No- *Gags* You gotta stop, dude. I can't stay here if you're gonna be doing all that..."

            scene v15s18a_ryan_4 # TPP. Shot of just MC with a disgusted face covering his mouth with his hand.
            with dissolve
            
            pause 0.75

        "Hold it back":
            $ add_point(KCT.BRO)

            scene v15s18a_ryan_3
            with dissolve

            u "Ugh- Fuck, man... That sounds painful."

    scene v15s18a_ryan_3a
    with dissolve

    ry "Try being the one who's actually getting sick... *Groans*"

    scene v15s18a_ryan_3
    with dissolve

    u "No thanks, I'll pass."

    scene v15s18a_ryan_3a
    with dissolve

    ry "Ugh, fuck... I'm never eating a gummy worm again..."

    scene v15s18a_ryan_3
    with dissolve

    u "Hey, at least your costume looks good."

    scene v15s18a_ryan_3a
    with dissolve

    ry "Oh... Yeah. I just borrowed it from Cameron."

    scene v15s18a_ryan_3
    with dissolve

    ry "I didn't have much time to plan a costume this year... *Groans*"

    scene v15s18a_ryan_3a
    with dissolve

    u "Trust me, I know the feeling... Ha."

    scene v15s18a_ryan_3b # FPP. MC looking at Ryan, Ryan now looking at MC,Ryan looks miserable, disgusted face, mouth open.
    with dissolve

    ry "..."

    ry "What the fuck are you wear-"

    scene v15s18a_ryan_3
    with dissolve

    ry "*Pukes*"

    if v15s18a_gag:
        scene v15s18a_ryan_3a
        with dissolve

        u "*Gags* I- I'm out... I'm out!"

        scene v15s18a_ryan_5 # TPP. Show MC running out of the bathroom
        with dissolve

        pause 0.75

        scene v15s18a_ryan_2a # TPP. Show MC exiting the bathroom, as he leaves we see Ryan sitting on the floor with his head above the toilet since he is puking, his face obscured by the toilet and we don't ever see inside it.
        with dissolve
        
        pause 0.75

    else:
        scene v15s18a_ryan_3a
        with dissolve

        u "Ha, feel better soon, Ryan. Drink lots of water when you're able to."

        scene v15s18a_ryan_2a
        with dissolve

        pause 0.75

    play sound "sounds/doorclose.mp3"

    scene v15s18a_ryan_6 # TPP. MC standing outside of the bathroom door, neutral face, mouth closed
    with dissolve

    ry "*Pukes*"

    u "(Happy Halloween, Ryan...)"

    pause 0.75

    call screen v15s18a_upstairsroom

# Upstairs
# Location 3- Autumn's room
# *Clicking on Autumn's door
label v15s18a_AutumPenelope:
    $ freeroam13.add("autumn_penelope")

    scene v15s18apen_1 # TPP. Show MC putting his ear to Autumn's room door, slight smile, mouth closed.
    #with dissolve

    u "(I think there's people in here...?)"

    scene v15s18apen_2 # FPP. Show MC opening the door slightly in and peeking through the crack to see Penelope and Autumn, Penelope is sitting on Autumn's computer chair with her legs crossed, Autumn standing by her, both slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s18apen_2a # FPP. Show MC opening the door slightly in and peeking through the crack to see Penelope and Autumn, Penelope is sitting on Autumn's computer chair with her legs crossed, Autumn standing by her, Both slight smile, Autumn mouth open, Penelope mouth closed.
    with dissolve

    aut "Yeah, definitely! You could find an amazing career with your computer skills. Cyber security is a huge deal!"

    scene v15s18apen_2b # FPP. Show MC opening the door slightly in and peeking through the crack to see Penelope and Autumn, Penelope is sitting on Autumn's computer chair with her legs crossed, Autumn standing by her, Both slight smile, Autumn mouth closed, Penelope mouth open.
    with dissolve

    pe "Yeah? I hadn't thought of that, really. Working for the CIA or something? *Laughs*"

    scene v15s18apen_2a
    with dissolve

    aut "Yeah! Haha, exactly."

    scene v15s18apen_2b
    with dissolve

    pe "That would be amazing, not gonna lie."

    scene v15s18apen_3 # FPP. MC opening the door and walking into the room, Autumn and Penelope not noticing MC yet, both slight smile, mouth closed.
    with dissolve

    u "Evening, ladies."

    scene v15s18apen_4 # FPP. MC standing closer to Autumn and Penelope, Both shocked face as they look at MC, mouth open.
    with dissolve

    pause 0.75

    scene v15s18apen_4a # FPP. Penelope covering her mouth with her hand as she laughs, Autumn smiling, mouth open.
    with dissolve

    aut "Hey- [name]... *Chuckles*"

    scene v15s18apen_4b # FPP. Penelope not covering her mouth anymore, Penelope slight smile, mouth open, Autumn slight smile, mouth closed.
    with dissolve

    pe "Wow, looks like the stripper's finally arrived. *Giggles*"

    scene v15s18apen_4c # FPP. Penelope not covering her mouth, both slight smile, mouth closed.
    with dissolve

    u "Ha-ha, very funny..."

    scene v15s18apen_5 # FPP. MC looking at Autumn, Autum looking at MC, Autumn slight smile, mouth open.
    with dissolve

    aut "That... is a very brave costume."

    scene v15s18apen_5a # FPP. MC looking at Autumn, Autumn looking at MC, Autumn slight smile, closed.
    with dissolve

    u "Well, thanks... Although, I didn't really have a choice, haha."

    scene v15s18apen_6 # FPP. MC looking at Penelope, Penelope looking at MC, Penelope slight smile, mouth open.
    with dissolve

    pe "*Laughs* You're practically naked!"

    scene v15s18apen_6a # FPP. MC looking at Penelope, Penelope looking at MC, Penelope slight smile, mouth closed.
    with dissolve

    u "Oh, trust me, I know. Luckily, it's nice and warm in here. Thanks, Autumn."

    if signs:
        scene v15s18apen_7 # FPP. MC looking at Autumn as she is starting to sit comfortably on her bed, slight smile, mouth closed.
        with dissolve

        pause 0.75

        scene v15s18apen_7a # FPP. Autumn sitting on her bed comfortably, MC looking at Autumn, Autumn looking at MC, slight smile, mouth open.
        with dissolve

        aut "Haha, it's been a while since you were here, right? We've redecorated a lot since we made those signs for the protest. Do you like it?"

        scene v15s18apen_7b # FPP. Autumn sitting on her bed comfortably, MC looking at Autumn, Autumn looking at MC, slight smile, mouth closed.
        with dissolve

        u "For sure, yeah. The entire house is looking great."

    scene v15s18apen_6b # FPP. MC looking at Penelope, Penelope looking at Autumn(Off-camera on the bed), Penelope slight smile, mouth open.
    with dissolve

    pe "Yeah, the Deer's house is probably my favorite."

    scene v15s18apen_7c # FPP. MC looking at Autumn, Autumn looking at Penelope(Off-camera sitting in the computer chair), Autumn slight smile, mouth open.
    with dissolve

    aut "Well, it took ages to get where we are, so thank you. Tons of hard work and late nights, but..."

    aut "The hardest part was getting everyone to agree on the colors. I had to get so many samples! *Laughs*"

    scene v15s18apen_7b
    with dissolve

    u "Haha. Decorating, volunteering, learning... Do you ever sleep?"

    scene v15s18apen_7a
    with dissolve

    aut "Nope!"

    scene v15s18apen_6c # FPP. MC looking at Penelope, Penelope looking at MC, Penelope putting a finger to her lips to shush them.
    with dissolve

    pause 0.75

    scene v15s18apen_6d # FPP. MC looking at Penelope, Penelope looking at MC, Penelope's finger not at her lips anymore, Penelope winking at MC, slight smile, mouth open.
    with dissolve

    pe "*Whispers* We're actually vampires... Shhh!"

    scene v15s18apen_6a
    with dissolve

    u "Oh shit, okay... Your secret is safe with me. *Chuckles*"

    scene v15s18apen_7a
    with dissolve

    aut "So, did you end up finding Lauren a good gift?"

    if not v15_autumn_lunchbreak:
        scene v15s18apen_7b
        with dissolve

        u "Uh, I found a gift... Yes. *Laughs*"

        scene v15s18apen_6
        with dissolve

        pe "Haha, that sounded confident."

    else:
        scene v15s18apen_7b
        with dissolve

        u "Oh yeah! Thanks for your advice. I think she's gonna like it."

        scene v15s18apen_6
        with dissolve

        pe "Lauren will like anything from anyone, haha. She's too sweet."

        scene v15s18apen_7a
        with dissolve

        aut "She'll be opening them soon, probably."

        scene v15s18apen_7b
        with dissolve

        u "Awesome, I can't wait to see her reactions."

    scene v15s18apen_7c
    with dissolve

    aut "Oh, yeah! Penelope, do you like dogs?"

    scene v15s18apen_6b
    with dissolve

    pe "Yes! Of course! *Giggles* I love any fur baby, honestly."

    scene v15s18apen_7c
    with dissolve

    aut "Ha, same! You'll have to come visit the dog shelter where I work. I can introduce you to all the rescues."

    scene v15s18apen_6b
    with dissolve

    pe "I'd love that!"

    scene v15s18apen_7c
    with dissolve

    aut "Maybe you can even name one of them."

    scene v15s18apen_6a
    with dissolve

    u "Yeah, Autumn let me name one that came in the other day."

    if dog_name.lower() == "blue":
        scene v15s18apen_7a
        with dissolve

        aut "But we decided to stick with Blue..."

        scene v15s18apen_7b
        with dissolve

        u "Yup."

    else:
        scene v15s18apen_7a
        with dissolve

        aut "Yeah! From Blue to [dog_name]."

    scene v15s18apen_6b
    with dissolve

    pe "Aww! That's so cute, I'm definitely coming."

    scene v15s18apen_6a
    with dissolve

    u "He's such a good boy."

    scene v15s18apen_7c
    with dissolve

    aut "Yeah, and a very hungry one. We've been feeding him three times a day and he still begs for more... *Laughs*"

    scene v15s18apen_6b
    with dissolve

    pe "Typical boy..."

    scene v15s18apen_6a
    with dissolve

    u "Hey, what's that supposed to mean?"

    scene v15s18apen_8 # TPP. Shot of Autumn laughing as she sits on the bed
    with dissolve

    pause 0.75

    scene v15s18apen_6e # FPP. MC looking at Penelope, Penelope looking at MC but more near his waistband, confused, mouth closed.
    with dissolve

    pe "What's that piece of paper tucked into your costume?"

    menu:
        "Show the list":
            $ add_point(KCT.TROUBLEMAKER)
            $ v15s18a_showlist_penelope_autumn = True

            scene v15s18apen_6a
            with dissolve

            u "Oh, here..."

            scene v15s18apen_6f # FPP. MC handing Penelope the challenge paper, Penelope grabbing the paper, Penelope slight smile, mouth closed.
            with dissolve

            u "It's a list of sexual challenges that Imre gave to me. *Laughs*"

            scene v15s18apen_7c
            with dissolve

            aut "Oh, wow... It's the sexless checklist! Haha!"

            scene v15s18apen_7b
            with dissolve

            u "The what?"

            scene v15s18apen_7a
            with dissolve

            aut "*Chuckles* Umm, I can't believe it still exists but... Yeah. This tradition has been around for years."

            scene v15s18apen_7b
            with dissolve

            u "Wait, really?!"

            scene v15s18apen_7a
            with dissolve

            aut "Really. Except it's called the \"sexless checklist\" for a reason, ha."

            scene v15s18apen_6b
            with dissolve

            pe "Sexless? Like, a virgin? A checklist for virgins?"

            scene v15s18apen_7c
            with dissolve

            aut "Exactly. A checklist for the sexless."

            scene v15s18apen_7d # FPP. MC looking at Autumn, Autumn looking at Penelope(Off-camera sitting in the computer chair), Autumn slight smile, mouth closed.
            with dissolve

            u "(Oh... My... God... Imre is such a fucking idiot, haha!)"

            scene v15s18apen_7c
            with dissolve

            aut "It's supposed to turn a virgin into a natural."

            aut "The frat Presidents would each choose one Freshman on Halloween, a virgin obviously, and they were given the list to complete by midnight."

            scene v15s18apen_6b
            with dissolve

            pe "You're supposed to get all of these things done with different girls?"

            scene v15s18apen_7c
            with dissolve

            aut "Yes... Multiple women, multiple sexual acts, one night only."

            scene v15s18apen_6b
            with dissolve

            pe "Huh..."

            scene v15s18apen_6g # FPP. MC looking at Penelope, Penelope looking at the list, Penelope biting her lip.
            with dissolve

            pause 0.75

            scene v15s18apen_7c
            with dissolve

            aut "And if you succeed, congrats. You're not a virgin anymore! But if you fail..."

            scene v15s18apen_7d
            with dissolve

            u "(Like Imre did...)"

            scene v15s18apen_7c
            with dissolve

            aut "Then everyone at SVC knows you're a virgin, and also that you asked at least six different women to help you with the list and got denied."

            scene v15s18apen_7b
            with dissolve

            u "A failed virgin."

            scene v15s18apen_7a
            with dissolve

            aut "That's what they used to call them, yeah. Ha..."

            scene v15s18apen_6b
            with dissolve

            pe "That's kind of crazy..."

            scene v15s18apen_7b
            with dissolve

            u "Yeah, well I don't have a virginity to lose, haha."

            u "Now I'm starting to wonder who gave the list to Imre thinking that he needed to lose his... *Laughs*"

            scene v15s18apen_7a
            with dissolve

            aut "Well, you never know. Whether it's for educational purposes or not, it was something exciting to do during each Halloween party."

            scene v15s18apen_6b
            with dissolve

            pe "Were you ever asked to help with the list?"

            scene v15s18apen_7c
            with dissolve

            aut "Oh yeah, of course. I've helped before."

            scene v15s18apen_7d
            with dissolve

            u "(Oh?)"

            scene v15s18apen_6b
            with dissolve

            pe "Ooooh!"

            scene v15s18apen_7c
            with dissolve

            aut "*Chuckles* I have limits, but I also like to have a good time. This is college after all."

            scene v15s18apen_7b
            with dissolve

            u "So, you're saying if I decided to work on completing this checklist tonight, it would make the party more interesting?"

            scene v15s18apen_6h # FPP. Penelope handing MC back the challenge paper, MC grabbing tha paper, Penelope slight smile, mouth closed.
            with dissolve

            pause 0.75

            scene v15s18apen_6
            with dissolve

            pe "Umm, yeah! Especially while you're wearing that stripper costume... *Giggles*"

            if lauren.relationship.value >= Relationship.GIRLFRIEND.value:
                scene v15s18apen_7a
                with dissolve

                aut "It'd be fun if you weren't dating my sister, haha. I don't think she'd be too happy to come across this list. Just a heads up."

                scene v15s18apen_7b
                with dissolve

                u "Of course, yeah."

                scene v15s18apen_6i # FPP. MC looking at Penelope, Penelope looking at MC, Penelope confused, mouth open.
                with dissolve

                pe "You and Lauren are dating?"

                scene v15s18apen_6j # FPP. MC looking at Penelope, Penelope looking at MC, Penelope confused, mouth closed.
                with dissolve

                u "Yeah, we're together."

                if penelope.relationship.value >= Relationship.LOYAL.value:
                    $ penelope.relationship.value >= Relationship.LIKES.value

                    scene v15s18apen_6k # FPP. MC looking at Penelope, Penelope looking at MC, Penelope slight sad face, mouth open.
                    with dissolve

                    pe "Oh, that's... Great news."

                    scene v15s18apen_6l # FPP. MC looking at Penelope, Penelope looking at MC, Penelople slight sad face, mouth closed.
                    with dissolve

                    u "Pen-"

                elif penelope.relationship.value >= Relationship.LIKES.value:
                    scene v15s18apen_6k
                    with dissolve

                    pe "That's so great to hear..."

                    scene v15s18apen_6l
                    with dissolve

                    u "(I don't think she really means that...)"

                else:
                    scene v15s18apen_6
                    with dissolve

                    pe "That's so cute!"

                scene v15s18apen_6
                with dissolve

                pe "I would definitely avoid the list in that case. *Laughs*"

                scene v15s18apen_6a
                with dissolve

                u "Right, ha."

            else:
                scene v15s18apen_6a
                with dissolve

                u "Let's see how the night goes then I guess, ha."

        "Don't show the list":
            scene v15s18apen_6a
            with dissolve

            u "Oh, it's just the receipt for this damn costume, haha."

            scene v15s18apen_7a
            with dissolve

            aut "Jeez, you really weren't lying about not having enough time to get ready."

            scene v15s18apen_7b
            with dissolve

            u "*Sighs* No, I wasn't lying."

    scene v15s18apen_6a
    with dissolve

    u "Anyway, time for me to catch up with the others."

    scene v15s18apen_6
    with dissolve

    pe "Catch you later!"

    scene v15s18apen_7a
    with dissolve

    aut "Have fun."

    scene v15s18apen_9 # TPP. MC waving as he starts leaving the room, Penelope and Autumn back to looking at the computer in the background
    with dissolve

    u "You too, ladies!"

    play sound "sounds/doorclose.mp3"

    if v15s18a_showlist_penelope_autumn:
        scene v15s18apen_10 # TPP. MC standing outside Autumn's room, slight smile, mouth closed.
        with dissolve

        u "(The sexless checklist, huh? It's worth the practice, I think. *Chuckles*)"

        u "(Maybe I should keep the real name of the game to myself, wouldn't wanna harm Imre's ego now, would we? Hehe...)"

    else:
        scene v15s18apen_10
        with dissolve

        u "(Maybe we can bring up the list later with Autumn or Penelope.)"

    pause 0.75

    call screen v15s18a_upstairsroom

# Ground floor
# Location 4- Couch in the living room
# *Clicking on Imre and Lauren*
label v15s18a_ImreLauren:
    $ freeroam13.add("imre_lauren")
    
    scene v15s18aimre_1 # TPP. MC walking over to Lauren and Imre, Imre looking at Lauren, Lauren looking at Imre, both slight smile, mouth closed.
    #with dissolve

    pause 0.75

    scene v15s18aimre_2 # FPP. MC looking at Lauren, Lauren looking at Imre, Lauren slight smile, mouth open.
    with dissolve

    la "Yeah, it's... cute!"

    scene v15s18aimre_3 # FPP. MC looking at Imre, Imre looking at Lauren, Imre slight smile, mouth open.
    with dissolve

    imre "Cute? I'm supposed to be a badass gunslinger, Lauren. I can shoot the head off a chicken in a hundredth of a second."

    scene v15s18aimre_2
    with dissolve

    la "Eww! Why would you shoot the head off a chicken?!"

    scene v15s18aimre_3
    with dissolve

    imre "I don't know, I saw it in a movie once."

    scene v15s18aimre_2
    with dissolve

    la "*Sighs* What movie?"

    scene v15s18aimre_3
    with dissolve

    imre "I don't remember... Why? You wanna watch it?"

    scene v15s18aimre_2
    with dissolve

    la "No! I want to make sure I never watch it!"

    scene v15s18aimre_4 # FPP. MC sitting down next to Lauren, MC looking at Lauren, Lauren looking at MC, Imre looking at MC, both slight smile, mouth closed.
    with dissolve

    u "*Chuckles* Howdy, partner. Hello, Miss spider lady."

    scene v15s18aimre_4a # FPP. MC sitting down next to Lauren, MC looking at Lauren, Lauren looking at MC, Imre looking at Lauren, both slight smile, Lauren mouth open, Imre mouth closed.
    with dissolve

    la "Hey there, half-naked man!"

    if lauren.relationship.value >= Relationship.GIRLFRIEND.value:
        scene v15s18aimre_4
        with dissolve

        u "I could be a fully naked man."

        scene v15s18aimre_4a
        with dissolve

        la "Haha... *Whispers* Save it for the bedroom."

        scene v15s18aimre_4b # FPP. MC sitting down next to Lauren, Lauren kissing MC, Imre in the background, Imre slight smile, mouth closed.
        with dissolve
        
        pause 0.75

        if v13_imre_disloyal:
            scene v15s18aimre_5 # TPP. Show MC and Lauren kissing on the couch, Imre unamused face, mouth open.
            with dissolve

            imre "*Scoffs*"

        else:
            scene v15s18aimre_5a # TPP. Show MC and Lauren kissing on the couch, Imre slight smile, mouth open. 
            with dissolve

            imre "Get a room..."

            scene v15s18aimre_4c # FPP. MC looking at Lauren, Lauren looking at Imre, Lauren slight smile, mouth open, Imre slight smile, mouth closed.
            with dissolve

            la "Haha, we will."

    scene v15s18aimre_6 # FPP. MC looking at Imre, Imre looking at MC, Lauren looking at Imre, Imre slight smile, mouth open, Lauren slight smile, mouth closed.
    with dissolve

    imre "So, tell me, [name]... Would you ever shoot the head off a chicken?"

    menu:
        "With reason":
            $ add_point(KCT.BRO)
            scene v15s18aimre_6a # FPP. MC looking at Imre, Imre looking at Mc, Lauren looking at MC, Imre slight smile, mouth closed, Lauren slight smile, mouth closed.
            with dissolve

            u "If there was a good reason to, sure."

            scene v15s18aimre_4d # FPP. MC looking at Lauren, Imre looking at Lauren, Lauren looking at Mc, Imre slight smile, mouth closed, Lauren slight smile, mouth open.
            with dissolve

            la "A good reason for shooting an animal? Like what?"

            scene v15s18aimre_6b # FPP. MC looking at Imre, Imre looking at Lauren, Lauren looking at Imre, Imre slight smile, mouth open, Lauren slight smile, mouth closed.
            with dissolve

            imre "Yeah, like, for food."

        "No, I wouldn't":
            $ add_point(KCT.BOYFRIEND)
            scene v15s18aimre_6a
            with dissolve

            u "No, Imre. I wouldn't shoot the head off of a chicken... Why do you ask? *Laughs*"

            scene v15s18aimre_6c # FPP. MC looking at Imre, Imre looking at MC, Lauren looking at Imre, Lauren slight smile, mouth closed, Imre slight smile, mouth open.
            with dissolve

            imre "Damn... It just looked really cool in this movie, I guess."

    scene v15s18aimre_4c
    with dissolve

    la "I genuinely think we should try to protect all animals."

    scene v15s18aimre_6b
    with dissolve

    imre "Even if you're trying to show off your spectacular shooting skills?"

    scene v15s18aimre_4c
    with dissolve

    la "There's no excuse for killing, Imre! I hope those were CGI chickens."

    scene v15s18aimre_6b
    with dissolve

    imre "I don't know... It was an old movie."

    scene v15s18aimre_6a
    with dissolve

    u "Sounds like you're going through a cowboy phase, haha."

    scene v15s18aimre_6c
    with dissolve

    imre "Maybe I am! I might even start wearing this outfit every day."

    scene v15s18aimre_6a
    with dissolve

    u "*Chuckles* Really?"

    scene v15s18aimre_6c
    with dissolve

    imre "Well, it depends if the girls like it. Otherwise, it's going in the trash, haha."

    scene v15s18aimre_4c
    with dissolve

    la "Ha, you're ridiculous, Imre."

    scene v15s18aimre_6c
    with dissolve

    imre "That's what you keep telling me..."

    imre "Oh hey, any luck with the list so far?"

    scene v15s18aimre_7 # TPP. Show MC trying to play it cool, Imre and Lauren both looking at MC, Imre slight smile, mouth closed, Lauren confused, mouth closed.
    with dissolve

    pause 0.75

    if lauren.relationship.value >= Relationship.GIRLFRIEND.value:
        scene v15s18aimre_6a
        with dissolve

        u "(What the fuck, Imre?!)"

    scene v15s18aimre_4e # FPP. MC looking at Lauren, Imre looking at Lauren, Lauren looking at MC, Lauren confused, mouth open, Imre slight smile, mouth closed.
    with dissolve

    la "What list?"

    menu:
        "Be honest":
            $ add_point(KCT.BOYFRIEND)
            scene v15s18aimre_4f # FPP. MC looking at Lauren, Imre looking at Lauren, Lauren looking at MC, Lauren 
            with dissolve

            u "Oh, it's dumb. It's a list that Imre gave me, full of challenges for the party tonight."

            scene v15s18aimre_4e
            with dissolve

            la "Challenges? Like what?"

            if lauren.relationship.value >= Relationship.GIRLFRIEND.value:
                scene v15s18aimre_6d # FPP. Imre looking at MC, MC looking at Imre, Lauren looking at MC, Lauren confused, mouth closed, Imre guilty, mouth open.
                with dissolve

                imre "*Whispers* Oh..."

            scene v15s18aimre_4f
            with dissolve

            u "It's like... steal a pair of panties, find a condom, things like that."

            scene v15s18aimre_4e
            with dissolve

            la "It does sound a bit stupid... But I'll know who to blame if any of my panties go missing, haha."

        "Lie": 
            $ add_point(KCT.TROUBLEMAKER)
            $ v15s18a_lie = True
            scene v15s18aimre_6a
            with dissolve

            u "Oh, it's just my grocery list. Why are you asking me about groceries, Imre? *Nervous laugh*"

            scene v15s18aimre_6c
            with dissolve

            imre "Oh, I- I don't know, ha. Sorry, bro."

    scene v15s18aimre_4
    with dissolve

    u "Haha, alright, I should go check in with the others. See you two in a bit!"

    scene v15s18aimre_4a
    with dissolve

    la "Okay! Gifts soon!"

    scene v15s18aimre_4
    with dissolve

    u "Perfect."

    scene v15s18aimre_8 # TPP. Show MC getting up off of the couch, slight smile, mouth closed.
    with dissolve

    pause 0.75

    call screen v15s18a_livingroom

# Ground floor
# Location 5- Kitchen in Deer's house
# *Clicking on Riley*
label v15s18a_Riley:
    $ freeroam13.add("riley")

# -Riley is shifting around food and plates on the counter, she's wearing a schoolgirl outfit-
    scene v15s18ariley_1 # FPP. MC looking at the Kitchen area, Food and plates out, Riley carrying plates to the part of the counter by the fridge, Riley looks stressed, mouth closed.
    #with dissolve

    pause 0.75

    scene v15s18ariley_1a # FPP. MC looking at the Kitchen area, Riley putting down the plates on the counter.
    with dissolve

    pause 0.75

    scene v15s18ariley_2 # FPP. MC looking at Riley, Riley looking at MC, Riley nervous, mouth closed.
    with dissolve

    u "Hey, Riley."

    scene v15s18ariley_2a # FPP. MC looking at Riley, Riley looking at MC, Riley nervous, mouth open.
    with dissolve

    ri "...Does the arrangement of this food look okay to you?"

    scene v15s18ariley_2
    with dissolve

    u "Umm..."

    scene v15s18ariley_3 # FPP. MC looking at the arrangement of the food.
    with dissolve

    pause 0.75

    scene v15s18ariley_2
    with dissolve

    u "Y-Yeah, it's fine."

    scene v15s18ariley_2a
    with dissolve

    ri "Are you sure?"

    scene v15s18ariley_2
    with dissolve

    u "Riley, why are you worried about the food?"

    scene v15s18ariley_2a
    with dissolve

    ri "Haha, what do you mean? I'm not worried I just-"

    scene v15s18ariley_2
    with dissolve

    u "Riley."

    scene v15s18ariley_2b # FPP. MC looking at Riley, Riley looking at MC, Riley closing her eyes, Riley neutral face, mouth open.
    with dissolve

    ri "*Sighs*"

    scene v15s18ariley_2c # FPP. MC looking at Riley, Riley looking at MC, Riley's eyes back open, Riley neutral face, mouth open.
    with dissolve

    ri "Sorry... I'm a bit stressed."

    scene v15s18ariley_2d # FPP. MC looking at Riley, Riley looking at MC, Riley neutral face, mouth closed.
    with dissolve

    u "No kidding, haha. Why?"

    scene v15s18ariley_2c
    with dissolve

    ri "I don't know... It's just-"

    ri "Maybe I'm overreacting, but-"

    scene v15s18ariley_2d
    with dissolve

    u "That's a good start to a sentence... *Chuckles*"

    if "v14_threesome" in sceneList:
        scene v15s18ariley_2c
        with dissolve

        ri "Ha... Aubrey hasn't spoken to me much since the three of us hooked up..."

        scene v15s18ariley_2d
        with dissolve

        u "Oh, really?"

        scene v15s18ariley_2c
        with dissolve

        ri "Well, you'd think we'd spend more time together now, right?"

        scene v15s18ariley_2d
        with dissolve

        u "Because we hooked up?"
    else:
        scene v15s18ariley_2c
        with dissolve

        ri "Aubrey and I don't hangout that much anymore."

        scene v15s18ariley_2d
        with dissolve

        u "What do you mean? Why not?"

        scene v15s18ariley_2c
        with dissolve

        ri "Well, I don't know. It started when we got back from Europe... She hasn't had any time for me."

        scene v15s18ariley_2d
        with dissolve

        u "Are you sure she isn't just busy with school? And Chloe? And the second wedding that her parents are having? *Laughs*"

    scene v15s18ariley_2c
    with dissolve

    ri "See, maybe I'm just looking too deep into it... Haha."

    scene v15s18ariley_2d
    with dissolve

    u "Maybe. Just maybe."

    scene v15s18ariley_2e # FPP. MC looking at Riley, Riley looking at MC, Riley slight smile, mouth open.
    with dissolve

    ri "Haha... Thanks."

    scene v15s18ariley_2f # FPP. MC looking at Riley, Riley looking at MC, Riley slight smile, mouth closed.
    with dissolve

    u "Always."

    scene v15s18ariley_2e
    with dissolve

    ri "So, I see you managed to pick up a costume in time... Well, half of a costume. *Laughs*"

    scene v15s18ariley_2f
    with dissolve

    u "Yeah, I'm trying to play it off like I planned it but everyone's got jokes. Even you, apparently. *Chuckles*"

    scene v15s18ariley_2e
    with dissolve

    ri "Haha, you look good. I definitely don't mind it, none of the girls here do..."

    ri "Wait a sec..."

    scene v15s18ariley_2g # FPP. MC looking at Riley, Riley looking down at her chest and pulling out a dollar bill from her boob area, nip slip, Riley slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s18ariley_2h # FPP. MC looking at Riley, Riley tucking the dollar in MC's waist band, Riley slight smile ,mouth closed.
    with dissolve

    pause 0.75

    scene v15s18ariley_2e
    with dissolve

    ri "There we go! Hehe..."

    scene v15s18ariley_2f
    with dissolve

    u "Thanks... Do I have to dance for you now?"

    scene v15s18ariley_2e
    with dissolve

    ri "Only if you want to... That was a big tip."

    #scene v15s18ariley_2i # FPP. MC looking at Riley, Riley looking at MC, Riley smirking, mouth closed.
    scene v15s18ariley_2f
    with dissolve

    u "Yeah, ha. Thanks, that dollar will definitely help me get through college."

    scene v15s18ariley_2e
    with dissolve

    ri "Haha, no problem."

    menu:
        "Dance":
            $ add_point(KCT.TROUBLEMAKER)
            scene v15s18ariley_2f
            with dissolve

            u "Alright, here you go."

            scene v15s18ariley_4 # TPP. MC with his hand in the air, swaying his hips to the left, Riley looking at MC, Riley slight smile, mouth closed, MC slight smile, mouth closed.
            with dissolve

            pause 0.75

            scene v15s18ariley_4a # TPP. MC with his hand in the air, swaying his hips to the right, Riley looking at MC, Riley slight smile, mouth closed, MC slight smile, mouth closed.
            with dissolve

            pause 0.75

            scene v15s18ariley_2e
            with dissolve

            ri "*Laughs* Wow..."

            ri "You've got some sexy moves there, [name]."


        "Don't dance":
            scene v15s18ariley_2i
            with dissolve

            u "I would dance for you, but I actually pulled a muscle in my groin, so."

            scene v15s18ariley_2e
            with dissolve

            ri "Oh. Doing what?"

            scene v15s18ariley_2i
            with dissolve

            u "Well, putting on this costume was like playing a game of twister."

            scene v15s18ariley_2e
            with dissolve

            ri "*Laughs*"

    scene v15s18ariley_5 # TPP. Show the Challenge list mid fall out of MC's costume and Riley looking at it, Riley slightly confused, mouth closed, MC slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s18ariley_5a # TPP. The Challenge list landing on the floor and Riley bending over to pick it up, Riley slightly confused, mouth closed, MC slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s18ariley_2j # FPP. MC looking at Riley, Riley looking at the Challenge list in her hand, Riley slightly confused, mouth open.
    with dissolve

    ri "What's this?"

    scene v15s18ariley_2k # FPP. MC looking at Riley, Riley looking at the Challenge list in her hand, Riley smirking, mouth closed.
    with dissolve

    u "A list of challenges that Imre gave to me. The usual college shenanigans... *Chuckles*"

    scene v15s18ariley_2l # FPP. MC looking at Riley, Riley looking at the Challenge list in her hand, Riley smirking, mouth open.
    with dissolve

    ri "Wow..."

    scene v15s18ariley_2k
    with dissolve

    u "I'm not even really doing-"

    scene v15s18ariley_6 # FPP. Riley handing the challenge list to MC, MC grabbing the list, Riley slight smile, mouth closed.
    with dissolve

    pause 0.75

    scene v15s18ariley_2e
    with dissolve

    ri "Do you need any help with it?"

    menu:
        "No, it's fine":
            scene v15s18ariley_2i
            with dissolve

            u "No, it's okay. I mean thanks, but I'm not really interested in playing Imre's games, haha."

            scene v15s18ariley_2e
            with dissolve

            ri "Oh, yeah. That's probably a wise decision."

            scene v15s18ariley_2i
            with dissolve

            u "I guess if you want to play though, Imre would definitely be up for it."

            scene v15s18ariley_2e
            with dissolve

            ri "Eww! I'm not riding that cowboy tonight! *Laughs*"

            scene v15s18ariley_2i
            with dissolve

            u "Haha, another wise decision."

            u "Alrighty, I'm gonna continue working around the room. See you later?"

            scene v15s18ariley_2e
            with dissolve

            ri "Okay, sure thing."

        "Yeah, I do":
            $ v15_imre_checklist[3].complete = True
            
            scene v15s18ariley_2i
            with dissolve

            u "I- Yeah. I do need help, haha. Are you interested?"

            scene v15s18ariley_2e
            with dissolve

            ri "Well, yeah."

            if "v14_threesome" in sceneList:
                ri "I've been craving you since Amsterdam..."

                scene v15s18ariley_2i
                with dissolve

                u "Hmm... Alright, then."

            scene v15s18ariley_2e
            with dissolve

            ri "I'll just close my eyes and pick one at random, yeah?"

            scene v15s18ariley_2m # FPP. Show Riley smiling and covering her eyes with one hand.
            with dissolve

            pause 0.75

            scene v15s18ariley_7 # TPP. Close up of Riley's finger pointing at the handjob challenge on the paper.
            with dissolve

            pause 0.75

            scene v15s18ariley_2i
            with dissolve
        
            u "Haha, what is it?"

            scene v15s18ariley_2n # FPP. Riley looking down at the paper that we can't see, Riley slight smile, mouth open.
            with dissolve

            ri "Looks like I'm giving you a hand job."

            scene v15s18ariley_2i
            with dissolve

            u "Are you sure you're okay with doing this?"

            scene v15s18ariley_2e
            with dissolve

            ri "Hmm..."

            scene v15s18ariley_2o # FPP. Riley leaning in super close to MC, Riley smirking, mouth closed.
            with dissolve

            ri "*Whispers* Let's go somewhere more private so you can see how okay I am with it."

            scene v15s18ariley_8 # FPP. MC following Riley up the stairs.
            with dissolve

            pause 0.75

            scene v15s18ariley_9 # TPP. Upskirt of Riley's outfit from behind.
            with dissolve

            pause 0.75

            play sound "sounds/dooropen.mp3"

            scene v15s18ariley_10 # TPP. Show Riley entering the Guest room and MC right behind her, both slight smile, mouth closed.
            with dissolve

            pause 0.75

            play sound "sounds/doorclose.mp3"

            scene v15s18ariley_11 # FPP. Riley up close to MC, Flirty, mouth open.
            with dissolve

            ri "Just lie down and relax... I'll take care of this."

            scene v15s18ariley_12 # TPP. Show MC pulling the bottom part of his costume down
            with dissolve

            pause 0.75

            play sound "sounds/kiss.mp3"

            scene v15s18ariley_13 # FPP. MC laying in the bed, Riley laying next to him and kissing him.
            with dissolve

            pause 0.75

            scene v15s18ariley_14 # TPP. MC laying on the bed and Riley laying next to him them kissing.
            with dissolve
            
            pause 0.75

            image v15rileyhj = Movie(play="images/v15/Scene 18a/v15rileyhj.webm", loop=True, image="images/v15/Scene 18a/v15rileyhjStart.webp", start_image="images/v15/Scene 18a/v15rileyhjStart.webp")
            image v15rileyhjf = Movie(play="images/v15/Scene 18a/v15rileyhjf.webm", loop=True, image="images/v15/Scene 18a/v15rileyhjStart.webp", start_image="images/v15/Scene 18a/v15rileyhjStart.webp")
            image v15rileyhj2 = Movie(play="images/v15/Scene 18a/v15rileyhj2.webm", loop=True, image="images/v15/Scene 18a/v15rileyhj2Start.webp", start_image="images/v15/Scene 18a/v15rileyhj2Start.webp")
            image v15rileyhj2f = Movie(play="images/v15/Scene 18a/v15rileyhj2f.webm", loop=True, image="images/v15/Scene 18a/v15rileyhj2Start.webp", start_image="images/v15/Scene 18a/v15rileyhj2Start.webp") 

            scene v15rileyhj # Ignore as animation
            with dissolve

            pause 0.75

            u "*Moans*"

            ri "Ha, do you like it?"

            scene v15rileyhjf # Ignore as animation
            with dissolve

            pause 0.75

            u "Yeah... Of course, I do."

            ri "Do you like it hard and fast...?"

            scene v15rileyhj # Ignore as animation
            with dissolve

            pause 0.75

            ri "Or slower and gentler?"

            u "I like a good mi- *Moans*"

            scene v15rileyhjf # Ignore as animation
            with dissolve

            pause 0.75

            ri "*Giggles* What was that?"

            u "Mmm, mix... I like a good mix..."

            scene v15s18ariley_13a # FPP. Riley laying close to MC her hand on his dick, Riley looking at MC, MC looking at Riley, Riley smirking, mouth open.
            with dissolve

            ri "Ah..."

            scene v15s18ariley_13b # FPP. Riley laying close to MC her hand on his dick, Riley looking at MC, MC looking at Riley, Riley biting her lip, mouth closed.
            with dissolve

            u "Fuck, Riley... That feels so good... *Moans*"

            scene v15s18ariley_13a
            with dissolve

            ri "I'm sure my sexy schoolgirl costume is helping quite a bit."

            scene v15s18ariley_15 # TPP. Shot of Riley's costume as she lays on the bed next to MC her hand on his dick.
            with dissolve

            pause 0.75

            scene v15s18ariley_13b
            with dissolve

            u "It is. You're a naughty-"

            scene v15s18ariley_16 # TPP. Close up of Riley kissing MC's neck
            with dissolve

            u "Fuck...*Moans*"

            scene v15rileyhj2 # Ignore as animation
            with dissolve

            pause 0.75

            u "Keep going... Just like that..."

            ri "Like this?"

            scene v15s18ariley_13b
            with dissolve

            u "Y-Yeah, you've... *Moans* Fuck Riley!"

            u "I'm..."

            u "I'm gonna cum."

            scene v15rileyhj2f # Ignore as animation
            with dissolve

            pause 0.75

            ri "Yeah?"

            ri "You're gonna cum for me?"

            scene v15s18ariley_13c # FPP. Riley laying close to MC her hand on his dick, Riley's other hand on MC's cheek, Riley looking at MC, MC looking at Riley, Riley biting her lip, mouth closed.
            with dissolve

            u "Yes..."

            u "Fuuuckkk... *Groans*"

            scene v15rileyhj2f # Ignore as animation
            with dissolve

            pause 0.75

            scene v15s18ariley_17 # TPP. MC cumming onto Riley's hand
            with dissolve

            pause 0.75

            scene v15s18ariley_13a
            with dissolve

            ri "*Gasps* Hehe, looks like you can mark that one off the list now."

            scene v15s18ariley_13b
            with dissolve

            u "Haha, damn... Thanks, Riley. That was amazing as always."

            scene v15s18ariley_13a
            with dissolve

            ri "You're welcome."

            play sound "sounds/kiss.mp3"

            scene v15s18ariley_13d # FPP. Riley kissing MC on the cheek
            with dissolve

            pause 0.75

            scene v15s18ariley_13a
            with dissolve

            ri "I better get cleaned up. Meet you out there?"

            scene v15s18ariley_13b
            with dissolve

            u "Yeah, sounds good."

            scene v15s18ariley_13e # FPP. Show Riley getting off the bed, slight smile, mouth closed.
            with dissolve

            pause 0.75

            play sound "sounds/dooropen.mp3"

            scene v15s18ariley_18 # FPP. Riley opening the door and exiting, slight smile, mouth closed.
            with dissolve

            pause 0.75

            play sound "sounds/doorclose.mp3"

            scene v15s18ariley_18a # FPP. The door closed and Riley gone
            with dissolve

            u "(Well... That wasn't so hard. *Laughs* Where to next?)"

            scene v15s18ariley_12a # TPP. MC putting his costume back on, slight smile, mouth closed.
            with dissolve

    pause 0.75

    call screen v15s18a_upstairsroom

# Ground Floor
# location 6- Kitchen counter stools
# *Clicking on Chris and Amber*
label v15s18a_ChrisAmber:
    $ freeroam13.add("chris_amber")

    scene v15s18aamber_1 # TPP. MC walking towards the Kitchen stools Amber is sitting on, Chris talking to Amber, Chris slight smile, mouth open, Amber slight smile, mouth closed.
    #with dissolve

    pause 0.75

    scene v15s18aamber_2 # FPP. MC keeping a little bit of distance and watching the Convo, Chris looking at Amber, Amber looking at Chris, Chris slight smile, mouth open, Amber slight smile, mouth closed.
    with dissolve

    ch "You're looking like a real knockout tonight, Amber."

    scene v15s18aamber_2a # FPP. MC keeping a little bit of distance and watching the Convo, Chris looking at Amber, Amber looking at Chris, Chris slight smile, mouth closed, Amber confused, mouth open.
    with dissolve

    am "Huh?"

    scene v15s18aamber_2b # FPP. MC keeping a little bit of distance and watching the Convo, Chris looking at Amber, Amber looking at Chris, Chris awkward smile, mouth open, Amber confused, mouth closed.
    with dissolve

    ch "You know, a knockout? Like, you're looking so good that you could knock someone out... *Awkward laugh*"

    scene v15s18aamber_2c # FPP. MC keeping a little bit of distance and watching the Convo, Chris looking at Amber, Amber looking at Chris, Chris awkward smile, mouth closed, Amber annoyed, mouth open.
    with dissolve

    am "I don't need to look good in order to knock somebody out..."

    scene v15s18aamber_2d # FPP. MC keeping a little bit of distance and watching the Convo, Chris looking at Amber, Amber looking at Chris, Chris awkward smile, mouth open, Amber annoyed, mouth closed.
    with dissolve

    ch "No, I didn't mean-"

    scene v15s18aamber_2e # FPP. MC keeping a little bit of distance and watching the Convo, Chris looking at Amber, Amber looking at Chris, Amber stands up with her fist clenched looking at Chris, Chris worried, mouth closed, Amber annoyed, mouth open.
    with dissolve

    am "I just need one good reason."

    scene v15s18aamber_2f # FPP. MC keeping a little bit of distance and watching the Convo, Chris looking at Amber, Amber looking at Chris, Amber stands up with her fist clenched looking at Chris, Chris worried, mouth open, Amber annoyed, mouth closed.
    with dissolve

    ch "Ah, sorry... I- It just came out wrong."

    scene v15s18aamber_2g # FPP. MC keeping a little bit of distance and watching the Convo, Chris walking away, Amber starting to sit back down on the stool.
    with dissolve

    pause 0.75

    scene v15s18aamber_3 # FPP. MC sitting on the stool next to Amber, MC looking at Amber, Amber looking at MC, Amber slight smile, mouth closed.
    with dissolve

    u "What the hell did I just witness? *Laughs*"

    scene v15s18aamber_3a # FPP. MC sitting on the stool next to Amber, MC looking at Amber, Amber looking at MC, Amber slight smile, mouth open.
    with dissolve

    am "Haha! I was thinking the same thing! He's definitely rusty with those pick-up lines."

    scene v15s18aamber_3
    with dissolve

    u "Poor guy. I think you destroyed his ego."

    scene v15s18aamber_3a
    with dissolve

    am "He was flirting with me. That was never going to end well."

    scene v15s18aamber_3
    with dissolve

    u "Yeah, I get that. He's just really sensitive right now, haha."

    scene v15s18aamber_3a
    with dissolve

    am "Well, maybe I'll apologize later."

    scene v15s18aamber_4 # TPP. MC and Amber looking at each other, both serious face, mouth closed.
    with dissolve

    pause 0.75

    scene v15s18aamber_4a # TPP. MC and Amber looking at each other, both laughing.
    with dissolve

    pause 0.75

    scene v15s18aamber_3
    with dissolve
    
    am "Probably not though. *Laughs*"

    am "His game needs to improve and that's the only way some people learn."

    scene v15s18aamber_3a
    with dissolve

    u "That's so charitable of you, Amber."

    scene v15s18aamber_3
    with dissolve

    am "I do my best."

    scene v15s18aamber_3b # FPP. MC sitting on the stool next to Amber, MC looking at Amber, Amber looking down at MC's lower half checking out his costume, Amber smirking, mouth closed.
    with dissolve

    pause 0.75

    scene v15s18aamber_3c # FPP. MC sitting on the stool next to Amber, MC looking at Amber, Amber back to looking at MC's face, Amber smirking, mouth open.
    with dissolve

    am "Now, holy fuck... What on earth is this outfit you're wearing?!"

    scene v15s18aamber_3
    with dissolve

    u "Haha, you like it?"

    scene v15s18aamber_3a
    with dissolve

    am "Strip for me and I'll let you know... *Chuckles*"

    scene v15s18aamber_3
    with dissolve

    u "Haha, okay, sure. A hundred bucks, please!"

    scene v15s18aamber_3a
    with dissolve

    am "Seriously? I was just about to ask where I should insert my quarters. *Laughs*"

    scene v15s18aamber_3
    with dissolve

    u "Haha, ouch! No, thanks, keep your damn change."

    if not v14_amber_clean:
        scene v15s18aamber_3a
        with dissolve

        am "I wouldn't want to compete with you down at the club... You wouldn't make any money."

        scene v15s18aamber_3
        with dissolve

        u "Haha, whatever! We both know I'd make more than you any day of the week."

    else:
        scene v15s18aamber_3
        with dissolve

        u "Is that all they pay the big shots at Lew's these days? Haha, how's that going?"

        scene v15s18aamber_3a
        with dissolve

        am "Really good, thanks!"

        am "I'm honestly doing better than ever and everyone around me seems to be noticing it too."

        am "I even made some suggestions about changing a few things within the company and they agreed to it all."

        scene v15s18aamber_3
        with dissolve

        u "That's amazing, Amber! I'm really happy for you."

        scene v15s18aamber_3a
        with dissolve

        am "Thanks, [name]."

        scene v15s18aamber_3
        with dissolve

        u "Of course."

        menu:
            "Don't mention the list":
                $ add_point(KCT.BOYFRIEND)

                u "(Not feeling like this is the best moment, maybe later.)"

                u "I think I'm going to see who else I can catch up with before it's time for presents."

                scene v15s18aamber_3a
                with dissolve

                am "Okay, good luck. I'll find you later."

            "Mention the list":
                $ add_point(KCT.TROUBLEMAKER)
                scene v15s18aamber_3d # FPP. MC sitting on the stool next to Amber, MC looking at Amber, Amber back to looking at MC's face, Amber smirking, mouth closed.
                with dissolve
            
                u "So, I guess this might be a good time to mention my list of party challenges for this evening..."

                scene v15s18aamber_3c
                with dissolve

                am "*Gasps* You have a secret list of challenges?! Let me see it!"

                scene v15s18aamber_5 # FPP. Just Amber and MC's hands, MC handing Amber the challenge paper, Amber grabbing the paper.
                with dissolve

                pause 0.75

                scene v15s18aamber_3e # FPP. # FPP. MC sitting on the stool next to Amber, MC looking at Amber, Amber looking at the Challenge list, Amber slight smile, mouth open.
                with dissolve

                am "Holy..."

                am "This is my kind of party list, haha! Imagine if everyone had this list..."

                scene v15s18aamber_5a # FPP. Just Amber and MC's hands, Amber handing MC the challenge paper, MC grabbing the paper.
                with dissolve

                u "It would be an orgy party. *Laughs*"

                scene v15s18aamber_3a
                with dissolve

                am "Ha, yes!"

                if not kct == "popular" and amber.relationship.value < Relationship.FWB.value:
                    am "Well, I'm sure you'll find some girls who will gladly help you mark a few things off of here tonight."

                    scene v15s18aamber_3
                    with dissolve

                    u "Thanks, haha. I'm gonna go continue my search and catch up with everyone."

                    scene v15s18aamber_3a
                    with dissolve

                    am "Good luck!"

                else:
                    $ v15_imre_checklist[2].complete = True
                    
                    scene v15s18aamber_3c
                    with dissolve

                    am "Well, between this list and that costume you have on..."

                    am "I think I can help you with one of these."

                    scene v15s18aamber_3d
                    with dissolve

                    u "Yeah? Which one is that?"

                    scene v15s18aamber_3c
                    with dissolve

                    am "You'll find out. Come on."

                    scene v15s18aamber_6 # TPP. MC following Amber up the stairs of the Deer's house
                    with dissolve

                    pause 0.75

                    scene v15s18aamber_7 # FPP. MC focusing in on Amber's ass as they go up the stairs
                    with dissolve

                    pause 0.75

                    scene v15s18aamber_8 # FPP. MC and Amber on the Balcony, MC looking at Amber, Amber looking at MC, Amber smirking, mouth closed.
                    with fade

                    pause 0.75

                    scene v15s18aamber_8a # FPP. MC and Amber on the Balcony, MC looking at Amber, Amber looking at MC, Amber smirking, mouth open.
                    with dissolve

                    am "*Chuckles* Ready?"

                    scene v15s18aamber_8
                    with dissolve

                    u "Can't you tell?"

                    scene v15s18aamber_8a
                    with dissolve

                    am "Yeah, I can see you're definitely ready for something..."

                    scene v15s18aamber_9 # FPP. MC looking down as Amber is on her knees infront of him.
                    with dissolve

                    pause 0.75

                    scene v15s18aamber_9a # FPP. MC looking down as Amber is on her knees infront of him, Amber pulling down the bottom part of his costume.
                    with dissolve

                    pause 0.75
                    
                    scene v15s18aamber_9b # FPP. MC looking down as Amber is on her knees infront of him, MC's bottom part of his costume around his ankles and his dick is out infront of Amber's face.
                    with dissolve

                    pause 0.75

                    image v15amberbj = Movie(play="images/v15/Scene 18a/v15amberbj.webm", loop=True, image="images/v15/Scene 18a/v15amberbjStart.webp", start_image="images/v15/Scene 18a/v15amberbjStart.webp")
                    image v15amberbjf = Movie(play="images/v15/Scene 18a/v15amberbjf.webm", loop=True, image="images/v15/Scene 18a/v15amberbjStart.webp", start_image="images/v15/Scene 18a/v15amberbjStart.webp")
                    image v15amberbj2 = Movie(play="images/v15/Scene 18a/v15amberbj2.webm", loop=True, image="images/v15/Scene 18a/v15amberbj2Start.webp", start_image="images/v15/Scene 18a/v15amberbj2Start.webp")
                    image v15amberbj2f = Movie(play="images/v15/Scene 18a/v15amberbj2f.webm", loop=True, image="images/v15/Scene 18a/v15amberbj2Start.webp", start_image="images/v15/Scene 18a/v15amberbj2Start.webp")

                    scene v15amberbj # Ignore as animation
                    with dissolve

                    pause 0.75

                    am "Mmmm..."

                    u "Oh, yes..."

                    u "Ssssshit, Amber..."

                    scene v15s18aamber_9d # FPP. MC looking down at Amber on her knees, Amber has all of MC's dick in her mouth, MC's hand holding the back of her head
                    with dissolve

                    u "Your mouth feels amazing..."

                    scene v15s18aamber_9e # FPP. MC looking down at Amber on her knees, Amber has all of MC's dick in her mouth, MC's hand holding the back of her head, Amber wrapping her arms around MC's legs and pulling him towards her.
                    with dissolve

                    am "*Gagging*"

                    scene v15amberbjf # Ignore as animation.
                    with dissolve

                    pause 0.75

                    u "*Moans* Take all of me."

                    am "Mmm..."

                    scene v15s18aamber_9f # FPP. MC looking down at Amber, Amber not sucking his dick at the moment, Amber looking up at MC, Amber smirking, mouth open.
                    with dissolve

                    am "Stripper dick tastes kinda good, haha."

                    scene v15s18aamber_9g # FPP. MC looking down at Amber, Amber not sucking his dick at the moment, Amber looking up at MC, Amber biting her lip.
                    with dissolve

                    u "Ha, you can have it whenever you want."

                    scene v15amberbj2 # Ignore as animation
                    with dissolve

                    pause 0.75

                    u "*Moans* Fuck!"

                    am "*Gagging*"

                    u "You like that?"

                    am "Mhmm!"

                    scene v15s18aamber_9h # FPP. MC looking down at Amber, Amber's lips on MC's dick, MC's hand on the top of her head.
                    with dissolve

                    u "Fuuuck..."

                    scene v15s18aamber_9i # FPP. MC looking down at Amber, Amber's lips on MC's dick, Amber reaching up with her hands and scratching at MC's chest.
                    with dissolve

                    am "*Gags*"

                    scene v15amberbj2f # Ignore as animation
                    with dissolve

                    pause 0.75

                    u "I'm going to cum... Amber..."

                    u "Oh... Fuck me..."

                    am "Mmm!"

                    u "Yes, Amber... Yes... *Moans*"

                    scene v15s18aamber_9e
                    with vpunch

                    u "*Groans* Oh, fuckkkkkkk..."

                    scene v15s18aamber_9j # FPP. MC looking down at Amber, Amber looking up at MC with a mouth full of cum winking at MC.
                    with dissolve

                    pause 0.75

                    scene v15s18aamber_10 # TPP. Just Amber spitting the cum over the side of the balcony.
                    with dissolve

                    pause 0.75

                    scene v15s18aamber_11 # TPP. Just Amber wiping her mouth, slight smile, mouth closed.
                    with dissolve

                    am "I hope nobody was standing under there, haha."

                    scene v15s18aamber_8
                    with dissolve

                    u "Amber. That was..."

                    scene v15s18aamber_8a
                    with dissolve

                    am "You have a great dick, [name]."

                    scene v15s18aamber_8
                    with dissolve

                    u "You have a great... mouth, and body, and-"

                    scene v15s18aamber_8a
                    with dissolve

                    am "Haha, okay, got it. You're welcome."

                    am "Now get back to the party and work on crossing more off that list."

                    scene v15s18aamber_8
                    with dissolve

                    u "Haha, I can do that."

                    scene v15s18aamber_12 # FPP. MC watching Amber walking back in the house.
                    with dissolve

                    u "(Blow job, check!)"

                    scene v15s18aamber_13 # TPP. MC pulling the bottom part of his costume back up, slight smile, mouth closed.
                    with dissolve

                    pause 0.75

                    scene v15s18aamber_14 # TPP. Show Mc walking back inside the house, slight smile, mouth closed.
                    with dissolve

        pause 0.75

        call screen v15s18a_upstairsroom

# Upstairs
# Location 7- Upstairs hallway
# *Clicking on the bronze deer statue*
label v15s18a_BronzeDeer:
    $ freeroam13.add("deer")

    scene v15s18adeer_1 # FPP. MC looking at the bronze deer statue in the hallway upstairs
    #with dissolve

    u "(That's an impressive deer... Looks expensive too. I wonder if it's been here since the beginning of the sorority?)"

    pause 0.75

    call screen v15s18a_upstairsroom

# Ground Floor
# Location 8- Magnet on Fridge downstairs
# *Clicking on the magnet photo on the Fridge*
label v15s18a_AutumnLaurenPhoto:
    $ freeroam13.add("photo")

# -if MC clicks on a photo of Autumn and Lauren (Magnet on the fridge), it says "best friends forever". Also note that the player should have a good view of the other magnets on the fridge-
    scene v15s18aphoto_1 # FPP. MC looking at all the magnets on the fridge
    #with dissolve

    pause 0.75

    scene v15s18aphoto_2 # FPP. Close in view of the magnet on the fridge that is a picture of Autumn and Lauren, The magnet says "Best Friends Forever <3".
    with dissolve

    u "(Aww, haha. \"Best friends forever\". They're super close, aren't they...)"

    pause 0.75

    call screen v15s18a_kitchen

# Ground Floor
# Location 9- Pumpkin on table next to the living room couch
# *Clicking on pumpkin*
label v15s18a_Pumpkin:
    $ freeroam13.add("pumpkin")

    scene v15s18apumpkin_1 # FPP. MC looking on a pumpkin on the table near the living room couch, The pumpkin has a cat-face carved into it.
    #with dissolve

    u "(Haha, it looks too cute for a Halloween pumpkin. I'm guessing Lauren made this one.)"

    pause 0.75

    call screen v15s18a_livingroom

# Ground Floor
# Location 10- Couch with Imre
# *Clicking on Lauren*
label v15s18a_end:

    # End freeroam screen
    jump v15s18b