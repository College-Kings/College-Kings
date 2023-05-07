# SCENE 59: Canoeing with Aubrey
# Locations: Canoeing Location
# Characters: AUBREY (Outfit: 2), MC (Outfit: 3)
# Time: Afternoon

label v13s59:
    scene v13s59_1 # TPP. show mc and aubrey walking to the canoe rental shop, slight smiles, mouths closed, rental shop in background
    with dissolve

    pause 0.75

    play music "music/v13/Track Scene 59_1.mp3" fadein 2

    scene v13s59_1a # TPP. same as v13s59_1 show mc and aubrey standing in front of the rental stanb waiting for the shop clerk, shop clerk not visible, looking at each other, mc rings a service bell
    with dissolve

    pause 0.75

    scene v13s59_2 # FPP. show just aubrey standing in front of canoe rental stand, looking at mc, slight smile, mouth open
    with dissolve

    au "Why am I getting nervous? I've got butterflies over here. *Laughs*"

    scene v13s59_2a # FPP. same as v13s59_2 aubrey mouth closed
    with dissolve

    u "You're nervous? *Chuckles* What are you nervous about?"

    scene v13s59_2
    with dissolve

    au "Falling into the water for one..."

    scene v13s59_2a
    with dissolve

    u "That's a reasonable thing to be nervous about, I guess. You can always just swim to my boat if that happens though, haha."

    scene v13s59_2b # FPP. same as v13s59_2 Aubrey looks away and down nervously
    with dissolve

    au "Actually... I can't do that."

    scene v13s59_2c # FPP. same as v13s59_2b aubrey mouth closed
    with dissolve

    u "What do you mean? *Chuckles*"

    scene v13s59_2b
    with dissolve

    au "I can't swim."

    scene v13s59_2c
    with dissolve

    u "Wait, what? You never learned how to swim? *Chuckles*"

    scene v13s59_2
    with dissolve

    au "Yeah, I know... It's kinda funny at first but I was terrified of the water when I was little."

    scene v13s59_2a
    with dissolve

    u "But you swam at the lake, didn't you?"

    scene v13s59_2
    with dissolve

    au "I stayed very, very close to the shoreline. *Laughs* Also though, I'd been to that lake before so I was already comfortable with it, you know?"

    au "Diving into a body of water, especially with unknown creatures inside of it... Is terrifying. *Chuckles*"

    scene v13s59_2a
    with dissolve

    u "Unknown creatures? *Laughs* Really?"

    scene v13s59_2d # FPP. same as v13s59_2 aubrey head slightly tilted with hand on the side of her face
    with dissolve

    au "*Chuckles* Yes, really."

    scene v13s59_2e # FPP. same as v13s59_2d aubrey mouth closed
    with dissolve

    u "Well, I will protect you from any of these \"creatures\", haha. Why haven't you learned yet?"

    scene v13s59_2d
    with dissolve

    au "I was never really interested and also horrified, but right now I'm wishing I had. *Laughs*"

    scene v13s59_2e
    with dissolve

    u "I'm surprised this conversation didn't come up while we were at the beach. *Chuckles* Are you ready?"

    scene v13s59_2
    with dissolve

    au "As I'll ever be..."

    scene v13s59_1b # TPP. same as v13s59_1a Shop clerk appears in the canoe rental stand, mc and aubrey look at shop clerk, slight smiles, aubrey mouth closed, mc mouth open
    with dissolve

    pause 0.75

    scene v13s59_3 # TPP. mc and aubrey, and the shop clerk arrive at a dock, with a canoe on both sides of the dock, canoe rack to the side of the dock, mc aubrey and shop clerk slight smiles mouths closed looking at the canoes
    with dissolve

    pause 1

    scene v13s59_3a # TPP. same as scene v13s59_3 Mc and aubrey get into separate canoes, slight smiles looking at each other, mouths closed
    with dissolve

    pause 0.75

    scene v13s59_3b # TPP. same as v13s59_3a mc and aubrey start rowing away from the dock, shop clerk waving goodbye
    with dissolve

    pause 1

    scene v13s59_4 # FPP. show just aubrey sitting in her canoe, holding a paddle with the left side of the paddle dipped into the water and right side of paddle in the air, slight smile, mouth open, looking at mc
    with dissolve

    au "This is kinda... hard. *Chuckles*"

    scene v13s59_4a # FPP. same as v13s59_4 right side of paddle dipped in the water and left side of the paddle in the air, aubrey mouth closed
    with dissolve

    u "That's what she said... *Laughs*"

    scene v13s59_4
    with dissolve

    au "*Chuckles* I'm serious!"

    scene v13s59_4a
    with dissolve

    menu:
        "Agree":
            $ aubrey.points += 1
            $ reputation.add_point(RepComponent.BOYFRIEND)
            scene v13s59_4a
            with dissolve

            u "It is a little hard... I'm not gonna lie."

        "Disagree":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            scene v13s59_4a
            with dissolve

            u "Nah, you're just weak. *Chuckles*"

            scene v13s59_4
            with dissolve

            au "Uhh, rude! *Chuckles*"

    scene v13s59_4b # FPP. same as v13s59_4 aubrey shakes and almost falls out her canoe, slight fear, mouth open
    with dissolve

    au "Fuck!"

    scene v13s59_4c # FPP. same as v13s59_4a aubrey, slight fear, mouth closed
    with dissolve

    u "Hold on there big fella! *Laughs*"

    scene v13s59_4
    with dissolve

    au "Stop laughing! *Laughs*"

    scene v13s59_4a
    with dissolve

    u "It's not my fault you're lookin' all goofy."

    scene v13s59_4d # FPP. same as v13s59_4 aubrey slightly sad
    with dissolve

    au "I'm not enjoying this as much as I thought..."

    scene v13s59_4e # FPP. same as v13s59_4a aubrey slight sad
    with dissolve

    u "Just give it a chance, haha."

    scene v13s59_4d
    with dissolve

    au "If you say so..."

    scene v13s59_5 # TPP. show mc and aubrey paddling down the stream, looking at each other, slight smiles, aubrey mouth open, mc mouth closed
    with dissolve

    pause 0.75

    scene v13s59_5a # TPP. same as v13s59_5 aubrey almost falls out of her canoe, aubrey slight fear, mc mouth open
    with dissolve

    pause 0.75

    scene v13s59_5
    with dissolve

    pause 0.75

    scene v13s59_5a
    with dissolve

    pause 0.75

    scene v13s59_4d
    with dissolve

    au "I'm sorry, but... I'm done with this."

    scene v13s59_4e
    with dissolve

    u "*Chuckles* Well, you gave it a chance."

    scene v13s59_3c # TPP. same as v13s59_3b mc and aubrey are rowing towards the dock instead of leaving
    with dissolve

    pause 1.25

    scene v13s59_3d # TPP. same as v13s59_3a mc and aubrey getting out of canoes instead of getting in
    with dissolve

    pause 1.25

    scene v13s59_6 # FPP. show aubrey looking at mc, slight concern, mouth open
    with dissolve

    au "I think I'm just not a huge fan of the water. And honestly, I'm not mad about it."

    scene v13s59_6a # FPP. same as v13s59_6 aubrey mouth closed
    with dissolve

    u "Do you feel like you'd enjoy it if you learned how to swim and had more experience in the water?"

    scene v13s59_6
    with dissolve

    au "I don't know... Maybe."

    scene v13s59_6a
    with dissolve

    u "So, do you want to learn?"

    scene v13s59_6
    with dissolve

    au "Well, yeah."

    scene v13s59_6a
    with dissolve

    menu:
        "Teach her":
            $ reputation.add_point(RepComponent.BOYFRIEND)
            scene v13s59_6a
            with dissolve

            u "How about I teach you?"

            scene v13s59_6b # FPP. same as v13s59_6 aubrey slight smile
            with dissolve

            au "Now?"

            scene v13s59_6c # FPP. same as v13s59_6a aubrey slight smile
            with dissolve

            u "Yeah."

            scene v13s59_6b
            with dissolve

            au "*Chuckles* Well..."

            scene v13s59_6b
            with dissolve

            au "Not right now, but I'll definitely let you teach me one day."

            scene v13s59_6d # FPP. same as v13s59_6c aubrey head slightly tilted, staring at mc
            with dissolve

            pause 0.75

            if v13s48_canoeing_as_date:

                scene v13s59_6e # FPP. same as v13s59_6d aubrey puts her hands around MC, mouth open, a cow is in the background
                with dissolve

                au "I appreciate what you're doing for me."

                scene v13s59_6f # FPP. same as v13s59_6e aubrey mouth closed, the cow walks closeer
                with dissolve

                u "Always."

                scene v13s59_7 # TPP. Aubrey and MC romantically kiss
                with dissolve
                play sound sound.kiss

                pause 1.25

                play sound sound.lick
                scene v13s59_7a # TPP. the cow licks aubrey and the mc's faces, aubrey and mc slight shock, they are both looking at the cow
                with dissolve

                pause 1.25

                stop music fadeout 3
                play music "music/v13/Track Scene 59_2.mp3" fadein 2

                scene v13s59_7b # TPP. the cow has walked away, aubrey and mc look at each other
                with dissolve

                pause 1.25

                scene v13s59_6g # FPP. same as v13s59_6c aubrey full smile
                with dissolve

                u "What the fuck?!"

                scene v13s59_6h # FPP. same as v13s59_6g aubrey mouth open
                with dissolve

                au "Oh... My... *Laughs*"

                scene v13s59_6g
                with dissolve

                u "You wouldn't see that kinda shit back at home. *Laughs*"

                scene v13s59_6h
                with dissolve

                au "Definitely not. *Laughs*"

                scene v13s59_6g
                with dissolve

                u "So... What was that little kiss for?"

                scene v13s59_6i # FPP. same as v13s59_6h aubrey flirty look
                with dissolve

                au "Hmm... Many reasons."

        "Let her figure it out":
            $ reputation.add_point(RepComponent.BRO)
            scene v13s59_6a
            with dissolve

            u "(I'll keep it to myself.)"

            scene v13s59_6a
            with dissolve

            u "Maybe one day you'll be in the right place at the right time and you'll learn comfortably."

            scene v13s59_6j # FPP. same as v13s59_6 aubrey slight frown
            with dissolve

            au "Haha, yeah... I hope so."

    scene v13s59_6b
    with dissolve

    au "Ready to go back?"

    scene v13s59_6c
    with dissolve

    u "I am, yeah."

    scene v13s59_6b
    with dissolve

    au "Let's go then."

    scene v13s59_8 # TPP. show MC and aubrey walking away from the canoe rental stand, slight smiles, looking at each other mouths open
    with dissolve

    pause 0.75

    scene v13s59_8a # TPP. same as v13s59_8 different background, looking straight ahead, mouths closed
    with dissolve

    pause 0.75

    scene v13s59_8b # TPP. same as v13s59_8a different background
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v13s60