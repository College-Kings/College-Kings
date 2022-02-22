# SCENE 33: Transition Mc showers
# Locations: Bathroom
# Characters: MC (Outfit: 9)
# Time: Wednesday


label v16s33: # 33) MC showers

    scene v16s33_1 # TPP Show MC washing himself in the shower, lips pursed, whistling
    with dissolve

    u "*Whistling badly*"


    scene v16s33_2 # TPP Show MC now out of the shower with a towel around his waist, looking at the foggy mirror
    with fade


    menu:
        "Draw a cat":
            scene v16s33_3 # FPP MC drawing a cat on the foggy mirror with his finger
            with dissolve

            pause 0.75


            scene v16s33_3a # FPP Same angle as 3, MC smiling and admiring the cat that he drew on the mirror
            with dissolve

            u "*Laughs* (Maybe I should take up a minor in art.)"


        "Draw a dick":
            scene v16s33_3b # FPP Same angle as 3, MC drawing a penis on the foggy mirror with his finger
            with dissolve

            pause 0.75


            scene v16s33_3c # FPP Same angle as 3, MC smiling and admiring the penis that he drew on the mirror
            with dissolve

            u "*Laughs* (Maybe I should take up a minor in art.)"


    # -Regardless-
    scene v16s33_4 # TPP Show MC sniffing his under arm
    with dissolve

    u "(Ah... Nice and fresh.)"


    scene v16s33_5 # FPP Show phone set on the edge of the sink
    with dissolve

    play sound "sounds/vibrate.mp3"

    pause 0.75


    scene v16s33_6 # TPP Show MC looking at his phone
    with dissolve

    pause 0.75


    $ contact_lauren.newMessage("Hey. Autumn's too busy to walk the dogs tonight so I'm helping, and the dog is way bigger than I thought! Lol. I'm gonna need your help! Please come?")


    if v16_Aubrey_date: # PLACEHOLDER VARIABLE NAME # -if MC going on Aubrey date
        $ contact_lauren.addReply("I'm sorry but I already have plans and am about to head out. Good luck! :)")
        $ contact_lauren.newMessage("Aw, okay. Thanks anyway!")


    else: # -if MC not going on Aubrey date
        if lauren.relationship == Relationship.FRIEND: # -if LaurenFriend
            $ contact_lauren.addReply("Sure, I'll come. But how big is this dog?")
            $ contact_lauren.newMessage("Massive!")
            $ contact_lauren.addReply("How massive?")
            $ contact_lauren.newMessage("Just come, please!")
            $ contact_lauren.addReply("Alright, alright, I'm coming.")
            $ contact_lauren.newMessage("Yay! I'll meet you at the park :)")

        else lauren.relationship == Relationship.GIRLFRIEND: # -if LaurenGF/RS
            $ contact_lauren.addReply("Better be worth it... ;)")
            $ contact_lauren.newMessage("A kiss is worth a thousand words...?")
            $ contact_lauren.addReply("Sold! I'm in.")
            $ contact_lauren.newMessage("Hehe, meet me at the park :)")


        scene v16s33_6a # TPP Same angle as 6, MC smiling and lowering his phone
        with dissolve

        u "(It'll probably turn out to be a Chihuahua, haha.)"


    # -Regardless of Aubrey date or not-
    scene v16s33_7 # TPP Show MC exiting the bathroom
    with dissolve

    pause 0.75


    if v16_Aubrey_date: # PLACEHOLDER VARIALBE # -if MC going on Aubrey date, transition to Scene 36-
        jump v16s36

    else: # -if MC not going on Aubrey date, transition to Scene 43-
        jump v16s43