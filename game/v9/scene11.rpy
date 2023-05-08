# SCENE 11: Viking Time
# Locations: History class/Viking Scene
# Characters: MC (Outfit 1 holding same Sword from Scene 10 (Arming Sword Damascended)), Penelope (Outfit 4), Cameron (Outfit 4)
# Time: Thursday Morning
    
label v9_hc_demo:
    scene v9demo1 # FPP. Show shot of Cameron and Penelope stood on the docks. Cameron looks annoyed (Penelope with beard, Cameron with wig)
    with fade

    play music music.ck1.v9.Track_Scene_11 fadein 2
   
    pause 1

    scene v9demo2 # TPP. Show Cameron and Penelope, walking towards a bald burly guard who is stood outside of a hut. Camera from behind cameron and Penelope.
    with dissolve

    pause 0.75

    scene v9demo3 # TPP. Show Penelope and Cameron now stood infront of the guard, camera from behind Penelope and Cameron.
    with dissolve

    pause 0.75

    scene v9demo4 # TPP. Show Penelope and Cameron, looking at camera (Camera from guard's perspective as if they're both looking at guard). Cameron slightly agitated, Penelope mouth open.
    with dissolve

    pe "*Deep voice* Hark, good sir, it is I, your King. This is my bride, your Queen."

    scene v9demo4a # TPP. Same camera as v9demo4, Cameron and Penelope look at eachother, Cameron annoyed, mouth open, Penelope mouth closed.
    with dissolve

    ca "That's not right."

    scene v9demo4b # TPP. Same camera as v9demo4, both still looking at eachother, both annoyed, Penelope mouth open, Cameron mouth closed.
    with dissolve

    pe "What?"
    
    scene v9demo4a
    with dissolve

    ca "That's not what vikings sounded like."

    scene v9demo4b
    with dissolve

    pe "How would you know?"

    scene v9demo4a
    with dissolve
    
    ca "I'd know better than you. Vikings were men. Powerful, strong..."

    scene v9demo4c # TPP. Same camera as v9demo4, both still looking at eachother, Penelope smile, Cameron annoyed, Penelope mouth open, Cameron mouth closed.
    with dissolve
    
    pe "Sure."

    scene v9demo4d # TPP. Same camera as v9demo4, both still looking at eachother, Penelope smile, Cameron annoyed, Cameron mouth open, Penelope mouth closed.
    with dissolve

    ca "I know they wouldn't say \"hark!\""

    scene v9demo4c
    with dissolve

    pe "There's no way to know."

    scene v9demo4d
    with dissolve

    ca "Of course there is!"

    scene v9demo5 # TPP. Show Penelope and Cameron stood next to eachother, Cameron grabbing his phone out of his pocket to check it.
    with dissolve

    pause 1

    stop music fadeout 3

    scene v9demo6 # TPP. Back in Mr. Lee's classroom, show Cameron looking at his phone, Mr. Lee, MC and Penelope looking it at sternly.
    with fade

    pause 1

    scene v9demo6a # TPP. Same camera as v9demo6, show Cameron placing his phone back into his pocket.
    with dissolve

    pause 1

    scene v9demo7 # TPP. Show MC approaching Cameron, Penelope and the guard from the side, all are looking at MC, neutral expressions, camera from behind MC.
    with fade

    play music music.ck1.v9.Track_Scene_11 fadein 2
    
    pause 1

    scene v9demo8 # FPP. Close up Penelope and Cameron (as if MC is now stood infront of them), both looking at camera, cameron bored expression, Penelope neutral, mouths closed.
    with dissolve

    menu:
        "Recognize the King":
            $ the_king = True
            u "Well met, Your Majesty. And this must be your lovely new bride."

            scene v9demo8a # FPP. Same camera as v9demo8, Penelope mouth open, Cameron mouth closed.
            with dissolve

            pe "Why yes, Sir [name], it is. Did well with my last pillage, did I not?"

            scene v9demo8
            with dissolve

            u "Yes, much better than the last one."

        "Don't recognize the King":
            $ reputation.add_point(RepComponent.TROUBLEMAKER)
            u "Hark, who goes there?"

            scene v9demo8b # FPP. Same camera as v9demo8, Penelope whispering in Cameron's ear, Cameron looks uninterested. Penelope mouth open.
            with dissolve

            pe "*Whispers to Cameron* See told ya."

            scene v9demo8a
            with dissolve

            pe "Well met, Sir [name], it is I, your King and my new bride."

            scene v9demo8
            with dissolve

            u "My apologies sir. You were not expected until tomorrow."

            scene v9demo8a
            with dissolve

            pe "My dear bride is not one for the sea. Sick the whole time. What a mess."

            scene v9demo8
            with dissolve

            u "Ahhh."

            u "Pity. Your last bride was made of stronger stock, I suppose."

    scene v9demo8a
    with dissolve

    pe "What has transpired since my departure?"

    scene v9demo8
    with dissolve

    menu:
        "Discuss War":
            $ reputation.add_point(RepComponent.BRO)

            u "We have conquered the enemies to the East and South. Much is left to pillage to the West. It's good you've returned to us now. We will need your expert guidance."

            scene v9demo8a
            with dissolve

            pe "Great news. We spent months cooped up in our cabin, it will be good to get my sword wet again."

            scene v9demo8
            with dissolve

            u "The new bride not to your liking, my King?"

            scene v9demo8c # FPP. Same camera as v9demo8, Penelope smile, Cameron slightly angry, Penelope mouth open, Cameron mouth closed.
            with dissolve

            pe "Oh, you know me too well, Sir [name]."

        "Discuss Riches":
            u "Gold and jewel cache is overflowing. We'll need to expand, and soon."

            scene v9demo8a
            with dissolve

            pe "Just what I like to hear, Sir [name]."

            pe "I promised my new bride riches beyond her wildest dreams and I must deliver, even if it means escalating the war to the West."

            scene v9demo8
            with dissolve

            u "Already making demands of my King's good nature, I see."

    scene v9demo9 # TPP. Show Penelope, Cameron and MC walking to one of the boats at the docks.
    with dissolve

    pause 1

    scene v9demo10 # FPP. Show Penelope and Cameron, who are now stood next to a boat, Cameron bored, Penelope neutral, mouths closed.
    with dissolve

    u "Almost ready to set sail once more, Your Majesty."

    scene v9demo10a # FPP. Same camera as v9demo10, Penelope mouth open.
    with dissolve

    pe "Where to?"

    scene v9demo10
    with dissolve

    menu:
        "North":
            if the_king:
                $ grant_achievement("king_of_the_north")

            u "North, Your Majesty."

            scene v9demo10a
            with dissolve

            pe "Ah, good practice. We must be well prepared before heading West once more."

            scene v9demo10
            with dissolve

            u "Yes, and with your new bride to join you, I'm sure you'd prefer an easy journey."

            scene v9demo10b
            with dissolve

            pe "Yes, dear thing can't be away from me for long, can she?"

        "West":
            u "West, Your Majesty."

            scene v9demo10a
            with dissolve

            pe "Are we ready for such a battle?"

            scene v9demo10
            with dissolve

            u "We are now that you're here. Will your bride take up arms?"

            scene v9demo10b # FPP. Same camera as v9demo10, Penelope laugh looking at Cameron, Cameron looks slightly angry, Penelope mouth open.1
            with dissolve

            pe "No, she's not got the stomach for battle, poor thing."

    scene v9demo11 # FPP. Show the line of huts as if MC is looking at them from the dock.
    with dissolve

    u "We have set up the royal lair for you and your new bride."

    scene v9demo10c # FPP. Same camera as v9demo10, Penelope looking at Cameron, Cameron looking at Penelope. Cameron bored, Penelope mouth open.
    with dissolve

    pe "Lovely, I'm whipped after a long sail. Ready to retire with your King, dear bride?"

    scene v9demo10d # FPP. Same camera as v9demo10, both looking at eachother, Cameron bored expression, Cameron mouth open, Penelope mouth closed.
    with dissolve

    ca "Yes, Your Majesty."

    stop music fadeout 3

    jump v9_hc_return