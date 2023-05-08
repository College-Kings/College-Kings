# SCENE 17: Arrive at hotel
# Location: Hotel Lobby
# Characters: MC(outfit1)/Ms Rose(outfit 1)/Lindsey(Outfit 1)
# Time: Late night

label v11_arrive_hotel:
    scene v11arrh1 # FPP. MC is looking at Ms Rose, Ms Rose is looking at the students in the lobby, tired, mouth open
    with dissolve
    play music music.ck1.v11.Track_Scene_17 fadein 2
    ro "Listen up, please! I'm not going to sugar coat anything, I'm very tired so let's please get through this quickly."

    ro "Based on your submitted preferences we've assigned your rooms and roommates. You can find them on this list."

    scene v11arrh2 # TPP. Ms Rose is handing out an item to Lindsey, both tired, mouths closed
    with dissolve

    pause 0.75

    scene v11arrh3 # FPP. Ms Rose is walking towards MC, she has a slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v11arrh3a # FPP. Same cam as v11arrh3, Ms Rose is now in talking distance to MC, Ms Rose mouth open, slight smile
    with dissolve

    ro "[name], you never submitted any preferences and there's two students without a roommate because their preferences were just too uhm... yeah..."

    ro "You can either room with Chloe or Riley."

    scene v11arrh3b # FPP. Same as v11arrh3a, Ms Rose mouth closed
    with dissolve

    menu:
        "Chloe":
            scene v11arrh3b
            with dissolve

            u "I'll room with Chloe."

        "Riley":
            $ v11_riley_roomate = True

            scene v11arrh3b
            with dissolve

            u "I'll room with Riley."
        
    scene v11arrh3a
    with dissolve

    ro "Very good."

    scene v11arrh3c # FPP. Show Ms Rose walking away (going to the same position as v11arrh1)
    with dissolve

    pause 0.75

    scene v11arrh1
    with dissolve

    ro "Everyone please wait and talk amongst yourselves while we wait on the keys."
    stop music fadeout 3
    if joinwolves:
        scene v11arrh3
        with dissolve

        pause 0.75

        scene v11arrh3a
        with dissolve

        ro "*Whisper* [name], may I speak to you in private?"

        scene v11arrh3b
        with dissolve

        u "Sure."

        scene v11arrh4 # TPP. Show MC and Ms Rose walking off towards a secluded area, both slightly smiling, mouths closed
        with dissolve

        pause 0.75

        jump v11_msrose_convo

    else:
        jump v11_roommate