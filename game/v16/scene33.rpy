# SCENE 33: Transition Mc showers
# Locations: Bathroom
# Characters: MC (Outfit: Naked/Towel)
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

    $ lauren.messenger.newMessage("Hey. Autumn's too busy to walk the dogs tonight so I'm helping, and the dog is way bigger than I thought! Lol. I'm gonna need your help! Please come?")

    if v16s25a_date_with_aubrey: # TODO: Variable  # PLACEHOLDER VARIABLE NAME # -if MC going on Aubrey date
        
        $ lauren.messenger.addReply("I'm sorry but I already have plans and am about to head out. Good luck! :)")
        $ lauren.messenger.newMessage("Aw, okay. Thanks anyway!")

        label v16s33_phone_continue1:
            if lauren.messenger.replies:
                call screen phone
            if lauren.messenger.replies:
                u "I should reply to Lauren."
                jump v16s33_phone_continue1
    
    
    else: # -if MC not going on Aubrey date
        
        if lauren.relationship == Relationship.FRIEND: # -if LaurenFriend
            $ lauren.messenger.addReply("Sure, I'll come. But how big is this dog?")
            $ lauren.messenger.newMessage("Massive!")
            $ lauren.messenger.addReply("How massive?")
            $ lauren.messenger.newMessage("Just come, please!")
            $ lauren.messenger.addReply("Alright, alright, I'm coming.")
            $ lauren.messenger.newMessage("Yay! I'll meet you at the park :)")

        elif lauren.relationship == Relationship.GIRLFRIEND: # -if LaurenGF/RS
            $ lauren.messenger.addReply("Better be worth it... ;)")
            $ lauren.messenger.newMessage("A kiss is worth a thousand words...?")
            $ lauren.messenger.addReply("Sold! I'm in.")
            $ lauren.messenger.newMessage("Hehe, meet me at the park :)")

        label v16s33_phone_continue2:
            if lauren.messenger.replies:
                call screen phone
            if lauren.messenger.replies:
                u "I should reply to Lauren."
                jump v16s33_phone_continue2

        scene v16s33_6a # TPP Same angle as 6, MC smiling and lowering his phone
        with dissolve

        u "(It'll probably turn out to be a Chihuahua, haha.)"

    # -Regardless of Aubrey date or not-

    scene v16s33_7 # TPP Show MC exiting the bathroom
    with dissolve

    pause 0.75

    if v16s25a_date_with_aubrey: #TODO: Variable # PLACEHOLDER VARIALBE # -if MC going on Aubrey date, transition to Scene 36-
        jump v16s36

    else: # -if MC not going on Aubrey date, transition to Scene 43-
        jump v16s43