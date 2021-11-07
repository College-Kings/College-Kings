# SCENE 09: Airport Amsterdam (Exposed Charli)
# Locations: Amsterdam Airport
# Characters: MR. LEE (Outfit: 1), MS. ROSE (Outfit: 1), MC (Outfit: 5), CHARLI (Outfit: 1), AUBREY (Outfit: 1), AMBER (Outfit: 1), CHLOE (Outfit: 4), RILEY (Outfit: 2), NORA (Outfit: 2), CHRIS (Outfit: 1), LINDSEY (Outfit: 3), LAUREN (Outfit: 1), RYAN (Outfit: 1), IMRE (Outfit: 1), EMILY (Outfit: 2), JOSH (Outfit: 1), PENELOPE (Outfit: 2)
# Time: Afternoon

label v14s09:
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

    lee "Honestly, I don't think I fully knew what I had signed up for. *Chuckles*"

    scene v14s09_2b # FPP. same as v14s09_2a Ms. Rose mouth open
    with dissolve

    ro "*Laughs* It wasn't all bad. We both had a little bit of fun at least, right?"

    scene v14s09_2a
    with dissolve

    lee "The fun I had was the fun I created."

    scene v14s09_2b
    with dissolve

    ro "Isn't that the type of fun you prefer? *Chuckles*"

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

    if msrosers and v13s20_bleach_suitcase:
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
                scene v14s09_5b
                with dissolve

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
                scene v14s09_5f # FPP. same as v14s09_5b charli has a relieved expression on his face
                with dissolve

                u "(I've done enough)"

    scene v14s09_6a
    with dissolve

    lee "Students, please say \"here\" when we call your name."

    scene v14s09_6a
    with dissolve

    lee "[name]."

    scene v14s09_6
    with dissolve

    u "Here."

    scene v14s09_8 # FPP. show just Ms. Rose holding a clipboard with one hand and a pen in the other, looking to her left, no expression, mouth open
    with dissolve

    ro "Aubrey."

    scene v14s09_8a # FPP. same as v14s09_8 Ms. Rose is now looking down at her clipboard and marking a name off with her pen, mouth closed
    with dissolve

    au "Here!"

    scene v14s09_6b # FPP. same as v14s09_6a Mr. Lee looking to his left
    with dissolve

    lee "Amber."

    scene v14s09_6c # FPP. same as v14s09_6b Mr. Lee is now looking down at his clipboard and marking a name off with his pen, mouth closed
    with dissolve

    am "Here..."

    scene v14s09_8b # FPP. same as v14s09_8 Ms. Rose looking to her right
    with dissolve

    ro "Chloe."

    scene v14s09_8a
    with dissolve

    cl "Yeah, here."

    scene v14s09_6d # FPP. same as v14s09_6b Mr. Lee looking to his right
    with dissolve

    lee "Riley."

    scene v14s09_6c
    with dissolve

    ri "Here! *Chuckles*"

    scene v14s09_8
    with dissolve

    ro "Nora."

    scene v14s09_8a
    with dissolve

    no "Here."

    scene v14s09_6b
    with dissolve

    lee "Chris."

    scene v14s09_6c
    with dissolve

    ch "Right here."

    scene v14s09_8b
    with dissolve

    ro "Lindsey."

    scene v14s09_8a
    with dissolve

    li "Here."

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

        u "(Not for much longer...)"

    scene v14s09_8b
    with dissolve

    ro "Lauren."

    scene v14s09_8a
    with dissolve

    la "Right here!"

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

    scene v14s09_9a # FPP. same as v14s09_9 imre looking at ryan, mouth open, slight smile, ryan looking at imre slight smile mouth closed
    with dissolve

    imre "*Whispers* Nice one, dumbass. Haven't heard that joke since middle school... Did you learn it from your sister? Haha-"

    scene v14s09_8b
    with dissolve

    ro "Imre!"

    scene v14s09_9b # FPP. same as v14s09_9a imre looking at Ms. Rose, hand raised
    with dissolve

    imre "Hey! Oh, here."

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

        scene v14s09_10
        with dissolve

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

    if v11_pen_goes_europe:
        scene v14s09_8b
        with dissolve

        ro "And last but not least..."

        scene v14s09_8b
        with dissolve

        ro "Our adorable assistant, Penelope."

        scene v14s09_11 # FPP. show penelope looking up at Ms. Rose, slight smile, mouth open
        with dissolve

        pe "*Chuckles* Yes... I'm here, Ms. Rose."

        scene v14s09_8b
        with dissolve

        ro "Ah..."

        scene v14s09_11
        with dissolve

        pe "Oh... *Chuckles* Right, sorry!"

        scene v14s09_11
        with dissolve

        pe "Umm, I'm here... Lorraine. *Chuckles*"

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

    jump v14s10