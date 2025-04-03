# SCENE 42: Ms Rose hotel lobby
# Location: Hotel room, hotel lobby, hotel corridor, street, bank exterior, bank interior
# Characters: MC (Outfit 3), Ms Rose (Outfit 1), Mr Lee (Outfit 1), Chloe (Outfit 2), Riley (Outfit 2), Imre (Outfit 1), Nora (Outfit 2)
# Time: Morning

label v11_hotel_lobby_rose:
    play music music.ck1.v11.Track_Scene_7_2 fadein 2
    if "v11_chloe" in sceneList:
        scene black
        with vpunch

        cl "Hey, hey! We need to get up."

        scene v11rol1 # FPP. MC and Chloe lying in MC's bed together, Chloe looking at MC, she's concerned, mouth closed (they're naked)
        with dissolve

        u "Huh, why? What time is it?"

        scene v11rol1a # FPP. Same as v11rol1, Chloe concerned, mouth open
        with dissolve

        cl "I'm not sure, actually... but Ms. Rose just texted me and said we have a group event."

        scene v11rol1b # FPP. Same as v11rol1, Chloe slight smile, mouth closed
        with dissolve

        u "Damn, so... I can't just lay here with you all day?"

        scene v11rol1c # FPP. Same as v11rol1b, Chloe slight smile, mouth open
        with dissolve

        cl "Haha. Sadly, no. We can't today, at least."

        scene v11rol1b
        with dissolve

        u "Ugh, fine."

        scene v11rol2 # TPP. Show MC and Chloe getting out of bed, both slightly smiling, mouths closed
        with dissolve

        pause 0.75

        scene v11rol3 # TPP. Show Chloe putting on her top (boobs still showing, pants already on and MC putting on his shirt (pants already on)
        with fade

        pause 0.75

        scene v11rol4 # FPP. MC and Chloe standing in the room, looking at each other, Chloe slight smile, mouth closed (fully clothed now)
        with dissolve

        u "Let's go."

    elif not v11_riley_roomate and not "v11_chloe" in sceneList:
        scene black
        with vpunch

        cl "Hey, [name]. We need to get up."

        scene v11rol5 # FPP. MC lying in his bed, Chloe standing next to his bed, looking at MC, her mouth is closed, slight smile
        with dissolve

        u "Huh? What? Why, what's up?"

        scene v11rol5a # FPP. Same as v11rol5, Chloe mouth open, slight smile
        with dissolve

        cl "*Chuckles* I'm not sure, but Ms. Rose just texted me and said we have a group event."

        scene v11rol5
        with dissolve

        u "Damn, so... I can't just lay here all day?"

        scene v11rol5a
        with dissolve

        cl "Haha. No you can't. Not today, at least."

        scene v11rol5
        with dissolve

        u "Ugh, fine."

        scene v11rol6 # TPP. Show MC getting out of his bed (MC in his boxers), neutral expression, mouth closed
        with dissolve

        pause 0.75

        scene v11rol7 # TPP. Show MC putting on his shirt (pants already on)
        with dissolve

        pause 0.75
        
        scene v11rol4
        with dissolve

        u "Let's go."

    elif v11_riley_roomate:
        scene black
        with vpunch

        ri "Hey [name], wake up! Sorry to do this again, but you need to get up."

        scene v11rol8 # FPP. MC lying in his bed, Riley standing next to his bed, looking at him, Riley mouth closed, slight smile
        with dissolve

        u "*Sighs* What is it this time?"

        scene v11rol8a # FPP. Same as v11rol8, Riley mouth open, slight smile
        with dissolve

        ri "At breakfast earlier Ms. Rose said we have a group event, and she sent me up here to wake you."

        scene v11rol8
        with dissolve

        u "Oh... What time is it?"

        scene v11rol8a
        with dissolve

        ri "I don't know? Time to get up, loser. We're on vacation! *Chuckles*"

        scene v11rol8
        with dissolve

        u "Alright, alright."

        scene v11rol6
        with dissolve

        pause 0.75

        scene v11rol7
        with dissolve

        pause 0.75

    scene v11rol9 # TPP. Show MC leaving the room, neutral expression, mouth closed
    with dissolve

    pause 0.75

    scene v11rol10 # TPP. Show MC walking in the lobby, mouth closed, neutral expression
    with fade

    pause 0.75
    stop music fadeout 3
    play music music.ck1.v10.Track_Scene_27 fadein 2
    scene v11rol11 # TPP. Show Ms Rose mouth open, slight smile, standing next to Mr Lee, mouth closed, slight smile, show Imre, Riley and Nora standing next to each other (make sure Imre is on the edge, with some space in between him and the girl in the middle, MC will be standing in between the girl and Imre in v11rol12) (Ryan, Amber and some other people are out of shot and won't be used, but they're there, play with angles and hide the place where they're supposed to be)
    with dissolve

    pause 1

    scene v11rol12 # FPP. Same positioning as v11rol11, MC in between the girl and Imre, MC standing close to and looking at Ms Rose, Ms Rose looking at MC, Ms Rose slight smile, mouth open
    with dissolve

    ro "Alright students, please listen up! For today's group event we'll be attending a tour of a bank. Now, this bank is being generous enough to even allow us to do this."

    scene v11rol12a # FPP. Same as v11rol12, Ms Rose now looking towards Imre who is standing next to MC (Imre out of shot), Ms Rose mouth open, slight smile
    with dissolve
    
    ro "I know this is not common field trip in the States and it isn't here either, but in the spirit of education... Here we are. Any questions?"

    scene v11rol13 # FPP. Same positioning as v11rol12, MC looking at Imre, Imre looking at Ms Rose, Imre mouth open, slight smirk
    with dissolve

    imre "Do we have to go?"

    scene v11rol12a
    with dissolve

    ro "Like all of the group events, you don't have to attend, but we strongly recommend it."

    scene v11rol13
    with dissolve

    imre "Alright... In that case, sorry Miss Econ, but I'm headed back to bed."

    scene v11rol14 # FPP. Same positioning as v11rol12, MC looking at Mr Lee, Mr Lee looking at Imre, Mr Lee slightly annoyed, mouth open
    with dissolve

    lee "You will be attending today, Imre."

    scene v11rol13a # FPP. Same as v11rol13, Imre looking down, slightly disappointed, mouth closed
    with dissolve

    imre "*Sighs*"

    scene v11rol14a # FPP. Same as v11rol14, Mr Lee slight smile, mouth open
    with dissolve

    lee "The few of you will be coming with me, the rest will be going with Ms. Rose."

    scene v11rol12
    with dissolve

    ro "Okay, let's get going!"

    scene v11rol15 # TPP. Show MC and Nora leaving the hotel lobby, both slightly smiling, mouths closed
    with dissolve

    pause 0.75

    scene v11rol16 # TPP. Show MC and Riley getting on the shuttle, both slightly smiling, mouths closed
    with dissolve

    pause 0.75

    scene v11rol17 # TPP. Show the shuttle on the road
    with fade

    pause 0.75

    scene v11rol18 # TPP. Show the shuttle stopping at the bank
    with fade

    pause 0.75

    scene v11rol19 # TPP. Show MC and Imre getting off the shuttle, MC slight smile, mouth closed, Imre slightly annoyed, mouth closed
    with dissolve

    pause 0.75

    scene v11rol20 # TPP. Show MC and Ms Rose walking inside the bank, both slightly smiling, mouths closed
    with dissolve

    pause 0.75
    stop music fadeout 3
    jump v11_at_the_bank