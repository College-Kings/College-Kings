# SCENE 21: Museum tour with Mr Lee
# Location: Hotel Lobby, Outside of the Hotel Lobby, Road, Road outside the Museum
# Characters: MC(outfit 1), Riley(outfit 2), Mr. Lee (Outfit 1), Nora (Outfit 1), Chris (Outfit 2)
# Time: Late morning

label v11_going_to_museum:
    scene v11gtm1 # TPP. Show MC, Mr Lee and Riley walking in the hotel lobby
    with dissolve
    play music music.v11_Track_Scene_10 fadein 2
    pause 0.75

    scene v11gtm2 # FPP. (MC, Lee, Riley, Nora and Chris standing outside the shuttle) MC and Mr Lee looking at each other, Mr Lee very slightly annoyed, mouth closed (Only Lee in shot)
    with dissolve

    u "I really would like to lay down for a minute if that's alright."

    scene v11gtm2a # FPP. Same as v11gtm2, Mr Lee mouth open, very slightly annoyed
    with dissolve

    lee "Not possible, the rooms are being cleaned and it's best if you walk off the pain anyway."

    scene v11gtm3 # FPP. Same character positioning as v11gtm2, MC and Nora looking at each other, Nora slightly annoyed, mouth open
    with dissolve

    no "I already tried to get out of going..."

    scene v11gtm2b # FPP. Same as v11gtm2, Mr Lee looking towards Nora's direction, Mr Lee mouth open, slightly annoyed
    with dissolve

    lee "And I said no to you as well, so that means I've been fair and consistent."

    scene v11gtm4 # FPP. Same character positioning as v11gtm2, MC and Riley looking at each other, Riley slightly smiling, mouth open
    with dissolve

    ri "Don't worry [name], Duncan won't be there. *Chuckles*"

    scene v11gtm4a # FPP. Same as v11gtm4, Riley mouth closed, slightly smiling
    with dissolve

    u "He better not be."

    scene v11gtm5 # FPP. Same character positioning as v11gtm2, MC looking at Chris, Chris is talking on the phone, mouth open, smiling
    with dissolve

    ch "Sebastian, you know this guy is a legend, we have to impress him."

    scene v11gtm3a # FPP. Same as v11gtm3, Nora mouth closed, slightly annoyed
    with dissolve

    u "Is Chris coming?"

    scene v11gtm3
    with dissolve

    no "Does it matter? We won't know if he's there or not anyways."

    scene v11gtm3b # FPP. Same as v11gtm3, but Nora is walking away, slightly annoyed, mouth closed
    with dissolve

    pause 0.75

    scene v11gtm2a
    with dissolve

    lee "Let's get moving then."

    scene v11gtm6 # TPP. Show Nora and MC boarding the shuttle, both slightly annoyed, mouths closed
    with dissolve

    pause 0.75

    scene v11gtm8 # TPP. Show the shuttle pulling up at the museum
    with fade

    pause 0.75
    stop music fadeout 3
    jump v11_museum_tour