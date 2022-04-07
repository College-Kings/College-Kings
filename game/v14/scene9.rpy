# SCENE 09: Airport Amsterdam (Exposed Charli)
# Locations: Amsterdam Airport
# Characters: MR. LEE (Outfit: 1), MS. ROSE (Outfit: 1), MC (Outfit: 5), CHARLI (Outfit: 1), AUBREY (Outfit: 1), AMBER (Outfit: 1), CHLOE (Outfit: 4), RILEY (Outfit: 2), NORA (Outfit: 2), CHRIS (Outfit: 1), LINDSEY (Outfit: 3), LAUREN (Outfit: 1), RYAN (Outfit: 1), IMRE (Outfit: 1), EMILY (Outfit: 2), JOSH (Outfit: 1), PENELOPE (Outfit: 2)
# Time: Afternoon

label v14s09:
    play music "music/v11/Track Scene 10.mp3" fadein 2
    
    scene v14s09_1 # TPP. show mc walking through airport, pulling his luggae, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v14s09_1a # TPP. same as v14s09_1 mc sees and looks at Mr. Lee and Ms. Rose looking over a checklist and hears them from a distance
    with dissolve

    pause 0.75

    scene v14s09_2 # FPP. show Mr. Lee no expression, mouth open standing on the right of the screen, and Ms. Rose slight smile, mouth closed, standing on the left side of the screen, both Mr. Lee and Ms. Rose are holding clipboards
    with dissolve

    lee "It'll be a very long time before I do another one of these trips..."

    scene v14s09_2a # FPP. same as v14s09_2 Mr. Lee slight smile
    with dissolve

    lee "Honestly, I don't think I fully knew what I had signed up for."

    scene v14s09_2b # FPP. same as v14s09_2a Ms. Rose mouth open
    with dissolve

    ro "*Laughs* It wasn't all bad. We both had a little bit of fun at least, right?"

    scene v14s09_2a
    with dissolve

    lee "The fun I had was the fun I created."

    scene v14s09_2b
    with dissolve

    ro "Isn't that the type of fun you prefer?"

    scene v14s09_2c # FPP. same as v14s09_2a Mr. Lee has an eyebrow raised
    with dissolve

    lee "You think you know me, don't you?"

    scene v14s09_2d # FPP. same as v14s09_2b Ms. Rose increases to half smile
    with dissolve

    ro "*Chuckles* I know you very well, generous statue giver."

    scene v14s09_2
    with dissolve

    lee "Okay... There is absolutely- *Whispers* No need to bring that up."

    scene v14s09_2d
    with dissolve

    ro "*Laughs* Are you saying what I think you're saying?"

    scene v14s09_2a
    with dissolve

    lee "*Sighs* I suppose that what happens in Europe, truly does stay in Europe..."

    if ms_rose.relationship >= Relationship.FWB and joinwolves and v13s20_bleach_suitcase: #sanitizing pathbuilder input
        scene v14s09_2e # FPP. same as v14s09_2a show Ms. Rose looking at mc slightly biting a pen slight smile, mouth closed, show Mr. Lee looking at Charli's suitcase with a confused expression, mouth closed
        with dissolve

        pause 0.75

        scene v14s09_2f # FPP. same as v14s09_2e Ms. Rose now looking at Mr. Lee and has placed a hand on his shoulder, slight smile, mouth closed, Mr. Lee looking at Ms. Rose slight smile, mouth closed
        with dissolve

        pause 0.75

    scene v14s09_2g # FPP. same as v14s09_2a Mr. Lee and Ms. Rose both laugh
    with dissolve

    u "(Those two are obviously good friends, and even closer now it seems.)"

    if v13_charli_exposed:
        scene v14s09_3 # TPP. show mc looking around, slight smile, mouth closed
        with dissolve

        u "(I don't see Charli anywhere... Guess Mr. Lee wasn't fucking around.)"

    elif v13s20_bleach_suitcase:
        scene v14s09_4 # FPP. mc see's charli grabbing his bleached suitcase, charli slight sad, mouth closed, charli looks at mc
        with dissolve

        pause 0.75

        scene v14s09_4a # FPP. same as v14s09_4 charli looks away.
        with dissolve

        pause 0.75

    else:
        scene v14s09_4b # FPP. same as v14s09_4 mc see's charli grabbing his suitcase (SUITCASE IS NOT BLEACHED,) charli slight sad, mouth closed, charli looks at mc
        with dissolve

        pause 0.75

        scene v14s09_4c # FPP. same as v14s09_4a charli's SUITCASE IS NOT BLEACHED
        with dissolve

        pause 0.75

    if not v13_charli_exposed:
        scene v14s09_5 # FPP. show just charli, no suitcase is visible, charli looks back at mc, slight sad, mouth closed
        with dissolve

        u "What?"

        scene v14s09_5a # FPP. same as v14s09_5 charli slight scared, mouth open
        with dissolve

        charli "N-nothing, sorry."

        scene v14s09_5
        with dissolve

        u "(Thought so.)"

        scene v14s09_5b # FPP. same as v14s09_5a charli looks at mc slightly scared and concerned mouth closed
        with dissolve

        menu:
            "Scare him":
                $ add_point(KCT.TROUBLEMAKER)
                u "(This should be fun.)"

                scene v14s09_6 # FPP. MC looks at Mr. Lee, show just Mr. Lee looking at mc, holding a clipboard with one hand and a pen in the other, no expression, mouth closed
                with dissolve

                u "Mr. Lee!"

                scene v14s09_6a # FPP. same as v14s09_6 Mr. Lee mouth open
                with dissolve

                lee "Yes?"

                scene v14s09_6
                with dissolve

                u "Charli and I wanted to discuss something with you."

                scene v14s09_6a
                with dissolve

                lee "Can it wait?"

                scene v14s09_5c # FPP. same as v14s09_5b charli looking at Mr. Lee, mouth open
                with dissolve

                charli "*High pitch* It... it can wait, yeah. No rush."

                scene v14s09_5d # FPP. same as v14s09_5a charli slight anger
                with dissolve

                charli "As a matter of fact, I think I've got it handled, [name]."

                scene v14s09_5
                with dissolve

                u "Oh! Are you sure?"

                scene v14s09_5e # FPP. same as v14s09_5 charli mouth open
                with dissolve

                charli "Yeah, positive. I got it."

                scene v14s09_7 # TPP. MC pats Charli on the back extra hard, mc slight smile mouth open, charli slight sad mouth closed
                with dissolve

                pause 0.75

                scene v14s09_7a # TPP. same as v14s09_7 Charli falls forward, slight shock, mouth open
                with hpunch

                pause 0.75

                scene v14s09_5
                with dissolve

                u "Ha... Good to hear, pal."

            "I've done enough":
                $ add_point(KCT.BOYFRIEND)
                scene v14s09_5f # FPP. same as v14s09_5b charli has a relieved expression on his face
                with dissolve

                u "(I've done enough to mess with him.)"

    scene v14s09_6a
    with dissolve

    lee "Students, please say \"here\" when we call your name."

    lee "[name]."

    scene v14s09_6
    with dissolve

    u "Here."

    u "(Can't believe the trip is already over, so much shit happened, I wonder what everyone's favorite part was...)"

    scene v14s09_8 # FPP. show just Ms. Rose holding a clipboard with one hand and a pen in the other, looking to her left, no expression, mouth open
    with dissolve

    ro "Aubrey."

    scene v14s09_8a # FPP. same as v14s09_8 Ms. Rose is now looking down at her clipboard and marking a name off with her pen, mouth closed
    with dissolve

    au "Here!"

    u "(So her favorite part was probably...)"

    menu:
        "Canoeing":
            u "(Probably when we went canoeing, that was interesting to say the least.)"

        "Becoming a model":
            u "(Definitely when she became a model at Naomi's photoshoot.)"

        "Going to the concert" if v13_aubrey_concert:
            u "(When I took her to the concert. She seemed to have a good time.)"
    
    scene v14s09_6b # FPP. same as v14s09_6a Mr. Lee looking to his left
    with dissolve

    lee "Amber."

    scene v14s09_6c # FPP. same as v14s09_6b Mr. Lee is now looking down at his clipboard and marking a name off with his pen, mouth closed
    with dissolve

    am "Here..."

    u "(And Amber's...)"

    menu:
        "Smoking weed at the canals":
            u "(Probably smoking at the canals, I really liked that.)"

        "Playing security":
            u "(She seemed to enjoy playing security during the murder mystery.)"

        "Almost robbing the bank":
            u "(We almost went to prison for robbing a bank, haha. Maybe that was her favorite part.)"

    scene v14s09_8b # FPP. same as v14s09_8 Ms. Rose looking to her right
    with dissolve

    ro "Chloe."

    scene v14s09_8a
    with dissolve

    cl "Yeah, here."

    u "(Chloe's favorite part was most likely...)"

    menu:
        "The Pier":
            u "(The pier. She was super excited about it when she asked me to come.)"

        "Murder Mystery":
            u "(She had a decent time getting into that “poor person” role.)"

        "Being tied to the bed" if "v13_chloe" in sceneList:
            u "(When I had her tied to the bed... That was definitely the best part, haha.)"
    
    scene v14s09_6d # FPP. same as v14s09_6b Mr. Lee looking to his right
    with dissolve

    lee "Riley."

    scene v14s09_6c
    with dissolve

    ri "Here!"

    u "(Oh and Riley's...)"

    menu:
        "Revenge against Charli":
            u "(Charli was the worst, so getting revenge must have felt amazing.)"

        "Mr. Lee's riddles":
            u "(She did seem to have fun while solving Mr. Lee's riddles.)"

        "The threesome" if "v14_threesome" in sceneList:
            u "(That fucking threesome... It has to be her favorite part of the trip, haha.)"

    scene v14s09_8
    with dissolve

    ro "Nora."

    scene v14s09_8a
    with dissolve

    no "Here."

    u "(I wonder about Nora's favorite part...)"

    menu:
        "London Museum":
            u "(The museum was really cool and she certainly loved London.)"

        "Carriage ride Chloe roast":
            u "(She really destroyed Chloe on that carriage ride.)"

        "Having sex with me" if "v12_nora" in sceneList:
            u "(Having sex with Nora certainly was one of my favorite parts... I'd assume it might be hers as well.)"
    
    scene v14s09_6b
    with dissolve

    lee "Chris."

    scene v14s09_6c
    with dissolve

    ch "Right here."

    u "(Hmm, Chris is a difficult one.)"

    menu:
        "Calling Sebastian":
            u "(He sure did call Sebastian a lot, probably was his favorite part, haha.)"

        "Japanese Garden":
            u "(The Japanese garden definitely wasn't the worst part of the trip.)"

        "Punching the wall":
            u "(Okay, so maybe not his favorite part. But it was kinda hilarious for everyone else.)"

    scene v14s09_8b
    with dissolve

    ro "Lindsey."

    scene v14s09_8a
    with dissolve

    li "Here."

    u "(Lindsey's...)"

    menu:
        "Escape Room":
            u "(Her birthday at the escape room was really cool, that was probably her favorite part of the trip.)"

        "Secretly planning her campaign":
            u "(I know she's really been planning to take Chloe down, I wouldn't be surprised if she enjoyed planning that even more than Europe.)"

        "The ferris wheel" if not "v13_chloe" in sceneList:
            u "(The ferris wheel was really nice. Definitely could've been her favorite part.)"
    
    if v13_charli_exposed:
        scene v14s09_6d
        with dissolve

        lee "Charli."

        scene v14s09_6c
        with dissolve

        lee "Is not here... Right."

        scene v14s09_8
        with dissolve

        ro "Not here? Where-"

        scene v14s09_6d
        with dissolve

        lee "*Whispers* I have him handled. He already left, headed back to campus. I'll be attending his meeting with the Dean when we return."

        scene v14s09_8c # FPP. same as v14s09_8 points her pen at Mr. Lee, mouth closed
        with dissolve

        pause 0.75

    else:
        scene v14s09_6b
        with dissolve

        lee "Charli."

        scene v14s09_5g # FPP. same as v14s09_5 charli looking down at the ground, facing Mr. Lee, charli's mouth is open
        with dissolve

        charli "Here."

        scene v14s09_5h # FPP. same as v14s09_5g charli's mouth is closed
        with dissolve

        u "(Right, Charli.)"

        menu:
            "Who fucking cares?":
                u "(Who fucking cares what that douche's favorite part was...)"
    
            "Being a bitch":
                u "(Being a bitch seemed to be his favorite activity, in my opinion.)"

    scene v14s09_8b
    with dissolve

    ro "Lauren."

    scene v14s09_8a
    with dissolve

    la "Right here!"

    u "(Lauren's favorite part was definitely...)"

    menu:
        "Bike Tour":
            u "(The bike tour. Lauren loves nature and we had a couple wild encounters, haha.)"

        "The murder mystery":
            u "(I think that was a pretty memorable event for all of us, and I know she had fun.)"

        "Our first time together" if "v12_lauren" in sceneList:
            u "(We shared an incredible night together. I don't think either of us will ever forget it.)"
    
    scene v14s09_6d
    with dissolve

    lee "Ryan."

    scene v14s09_9 # FPP. show ryan and imre standing next to mc, ryan raising his hand mouth open, half smile, imre facing ryan rolling his eyes, mouth closed
    with dissolve

    ry "Present."

    scene v14s09_6e # FPP. same as v14s09_6c Mr. Lee mouth open, rolling his eyes.
    with dissolve

    lee "*Sighs* There's always one..."

    scene v14s09_6f # FPP. same as v14s09_6e Mr. Lee looking at ryan
    with dissolve

    lee "The appropriate response is \"here\"."

    scene v14s09_9
    with dissolve

    ry "My bad, \"here\". *Laughs*"

    u "(And Ryan's favorite part was...)"

    menu:
        "When Imre got catfished":
            u "(Ryan does really enjoy seeing Imre's misfortune, I don't think he'll ever let him live that one down.)"

        "Being Imre's Husband":
            u "(Okay, maybe I'm just a troll, but they were a really cute couple.)"

        "Sex with a stripper" if v14_ryan_satin:
            u "(Losing his virginity, even if to a stripper, has got to be his highlight.)"
    
    scene v14s09_9a # FPP. same as v14s09_9 imre looking at ryan, mouth open, slight smile, ryan looking at imre slight smile mouth closed
    with dissolve

    imre "*Whispers* Nice one, dumbass. Haven't heard that joke since middle school... Did you learn it from your sister? Haha-"

    scene v14s09_8b
    with dissolve

    ro "Imre!"

    scene v14s09_9b # FPP. same as v14s09_9a imre looking at Ms. Rose, hand raised
    with dissolve

    imre "Hey! Oh, here."

    u "(Imre must have loved...)"

    menu:
        "The Red Light District":
            u "(Boobs and booze, I have never seen him happier than when we first arrived at the RLD.)"

        "Being Ryan's Wife":
            u "(Greatest. Couple. Ever.)"

        "Robbing the hustler" if v14s03a_take_wallet:
            u "(He did seem pretty confident after robbing that hustler. Maybe that was his favorite moment...)"

    scene v14s09_9c # FPP. same as v14s09_9a imre mouth closed, slightly annoyed, ryan looking and pointing at imre laughing
    with dissolve

    pause 0.75

    if emily_europe:
        scene v14s09_6b
        with dissolve

        lee "Emily."

        scene v14s09_6c
        with dissolve

        em "I'm here."

        u "(I don't even know with Emily, I didn't really see her all that much.)"

    if v11_invite_sam_europe:
        scene v14s09_8b
        with dissolve

        ro "Samantha."

        scene v14s09_8d # FPP. same as v14s09_8b Ms. Rose has a concerned expression
        with dissolve

        ro "...Sam? Where's Samantha?"

        scene v14s09_10 # FPP. show amber standing to the left and about 5 meters from Ms. Rose, looking at Ms Rose no expression mouth open, Ms. Rose looking at amber no expression mouth closed
        with dissolve

        am "Oh, she-"

        am "She already left this morning with her brother."

        scene v14s09_8
        with dissolve

        ro "*Sighs* She should've told us."

        scene v14s09_6d
        with dissolve

        lee "They both should have."

        scene v14s09_10
        with dissolve

        am "Sorry... I was supposed to pass on the message. It was a last minute decision I think."

        scene v14s09_8a
        with dissolve

        ro "Right, then... I'll contact her before we take off."

    if josh_europe:
        scene v14s09_6b
        with dissolve

        lee "Josh."

        scene v14s09_6c
        with dissolve

        jo "*Sighs* Here."

        u "(So Josh's favorite Europe moment...)"

        menu:
            "Playing Leopard Lord":
                u "(He was definitely a fan of his role during the murder mystery.)"
    
            "Drinks in London":
                u "(We had a good round of drinks together in London, maybe that was his favorite part.)"
    
            "Fancy dinner":
                u "(That fancy dinner Mr. Lee set up was free and delicious, I'm sure Josh loved that, haha.)"
        
    if v11_pen_goes_europe:
        scene v14s09_8b
        with dissolve

        ro "And last but not least..."

        ro "Our adorable assistant, Penelope."

        scene v14s09_11 # FPP. show penelope looking up at Ms. Rose, slight smile, mouth open
        with dissolve

        pe "Yes... I'm here, Ms. Rose."

        scene v14s09_8b
        with dissolve

        ro "Ah..."

        scene v14s09_11
        with dissolve

        pe "Oh... *Chuckles* Right, sorry!"

        pe "Umm, I'm here... Lorraine."

        u "(And Penelope's favorite...)"

        menu:
            "Cleaning the ship":
                u "(Haha, Mr. Lee really made her do a lot of annoying shit throughout the trip. I think she had a good time though.)"
    
            "The London Museum":
                u "(I think she really enjoyed the museum.)"
    
            "Going to the concert" if v13_penelope_concert:
                u "(She loved the concert, so I can definitely see that being her favorite part of the trip.)"
        
    scene v14s09_8e # FPP. same as v14s09_8 Ms. Rose looks at mc
    with dissolve

    ro "Very good. Now, if everyone will follow me so we can get seated, then we can finally head back home!"

    scene v14s09_12 # TPP. Show Ms. Rose, aubrey, amber in a line entering the gate to board the plane, all slight smiles, mouths closed
    with dissolve

    pause 0.75

    scene v14s09_12a # TPP. same as v14s09_12 Show nora, chris, and mc in a line entering the gate to board the plane, all slight smiles, mouths closed
    with dissolve

    pause 0.75

    scene v14s09_13 # FPP. mc looking to his left and sees riey with her hand up waving at mc slight smile mouth open, 
    with fade

    pause 1.25

    scene v14s09_14 # FPP. Mc sits down next to riley and looks at the screen on the headrest of the seat in front of him.
    with dissolve

    pause 1.25

    stop music fadeout 3
    jump v14s10