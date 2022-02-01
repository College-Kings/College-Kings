# SCENE 28: Ms Rose Sex Scene in her room
# Location: Ms Rose Hotel Room, MC Hotel Room, Hotel Room Corridor
# Characters: MC (Outfit 1), Ms. Rose (outfit 1)then in a robe in the bedroom, (female)Bartender (Outfit 1)
# Time: Night

label v11_ms_rose_sex:
    $ sceneList.add("v11_rose")
    $ ms_rose.relationship = Relationship.FWB

    scene v11ros1 # TPP. Show MC walking thourgh the corridor, he is slightly nervous, mouth closed
    with fade
    play music "music/v10/Track Scene 41_2.mp3" fadein 2
    pause 0.75

    scene v11ros2 # FPP. MC is standing outside Ms Rose's room, he is looking at the door
    with dissolve

    menu:
        "Open the door":
            $ add_point(KCT.TROUBLEMAKER)

            scene v11ros2a # FPP. Same as v11ros2, MC is grabbing the door handle
            with dissolve
            play sound "sounds/dooropen.mp3"

            pause 0.75

            scene v11ros2b # FPP. The door is open, show Ms Rose sitting on her bed, she is in a bathrobe, looking at the door, seductive look, mouth closed
            with dissolve

            pause 1

            scene v11ros3 # FPP. MC is in the room now, close to Ms Rose, they're looking at each other, Ms Rose seductive look, mouth closed (they're standing next to the bed)
            with dissolve

            pause 1

        "Knock":
            $ add_point(KCT.BOYFRIEND)

            scene v11ros2c # FPP. Same as v11ros2, show MC knocking on the door
            with dissolve

            play sound "sounds/knock.mp3"

            pause 0.75

            scene v11ros2d # FPP. Same cam as v11ros2, Show the door slightly open, Ms Rose poking her head through, slight smile, mouth closed, looking at MC
            with dissolve

            pause 0.75

            scene v11ros2e # FPP. Same cam as v11ros2, Ms Rose has the door open, she is looking in the corridor, towards the right, slightly worried, mouth closed
            with dissolve

            pause 0.75

            scene v11ros2f # FPP. Same as v11ros2e, but Ms Rose looking in the corridor, looking at the left
            with dissolve

            pause 0.75

            scene v11ros2g # FPP. Same as v11ros2, the door fully open, Ms Rose pulling MC by the arm, she has a seductive look, mouth closed
            with dissolve

            pause 1

            scene v11ros3
            with dissolve

            pause 1

label v11_ms_rose_sex_sg:
    stop music fadeout 3
    play music "music/v10/Track Scene 17_2.mp3" fadein 2
    scene v11ros3a # FPP. Same as v11ros3, Rose mouth open, seductive look
    with dissolve

    ro "Take off your clothes."

    scene v11ros3
    with dissolve

    u "..."

    scene v11ros3a
    with dissolve

    ro "I didn't stutter and I don't have all night. Take off your clothes or I'll do it for you."

    scene v11ros3
    with dissolve

    u "I-"

    scene v11ros3a
    with dissolve

    ro "Don't talk, just listen."

    scene v11ros3b # FPP. Same cam as v11ros3, Show Ms Rose getting very close to MC, she has a seductive look, mouth closed
    with dissolve

    pause 1.25

    scene v11ros4 # TPP. Show Ms Rose removing MC's shirt, she is slightly smiling, mouth closed
    with dissolve

    pause 1.25

    if config_censored:
        call screen censored_popup("v11s28_nsfwSkipLabel1")

    scene v11ros5 # TPP. Show Ms Rose removing MC's pants, show her ass appearing from under the bathrobe while she's bending over to remove his pants
    with dissolve

    pause 1.25

    scene v11ros3a
    with dissolve

    ro "This will go my way and my way only. Lie down."

    scene v11ros6 # TPP. Show Ms Rose pushing naked MC on the bed, both slightly smiling, mouths closed
    with dissolve

    pause 0.75

    scene v11ros6a # TPP. Same cam as v11ros6, MC lying in the bed, Ms Rose removing her bathrobe, mouth closed, seductive look
    with dissolve

    pause 1

    scene v11ros7 # FPP. MC is lying down on the bed, Ms Rose is on top of him, seductive look, mouth open
    with dissolve

    ro "What happens tonight doesn't leave this room. Understood?"

    scene v11ros7a # FPP. Same as v11ros7 seductive look, mouth closed
    with dissolve

    u "Yes."

    scene v11ros7b # FPP. MC is looking as Ms Rose slides down, she is kissing his abs
    with dissolve

    pause 1

    scene v11ros8 # FPP. MC lying down in the bed, looking as Ms Rose has her mouth close to his dick, she is looking at MC, seductive look, mouth closed
    with dissolve

    pause 1

    image v11rosbj = Movie(play="images/v11/Scene 28/v11rosbj.webm", loop=True, image="images/v11/Scene 28/v11rosbjStart.webp", start_image="images/v11/Scene 28/v11rosbjStart.webp") # Ms Rose blowjob
    image v11rosbjf = Movie(play="images/v11/Scene 28/v11rosbjf.webm", loop=True, image="images/v11/Scene 28/v11rosbjStart.webp", start_image="images/v11/Scene 28/v11rosbjStart.webp") # Ms Rose blowjob spedup

    scene v11rosbj # Ignore as animation
    with dissolve
    pause

    u "Mmm."

    u "(Fuck, this is my teacher!)"

    scene v11rosbjf # Ignore as animation
    with dissolve
    pause

    u "(This is hot as fuck.)"

    scene v11ros9 # TPP. Show Ms Rose climbing on MC, both smiling, mouths closed
    with dissolve

    pause 1

    image v11roscgc = Movie(play="images/v11/Scene 28/v11roscgc.webm", loop=True, image="images/v11/Scene 28/v11roscgcStart.webp", start_image="images/v11/Scene 28/v11roscgcStart.webp") # Ms Rose cowgirl choking
    image v11roscgcf = Movie(play="images/v11/Scene 28/v11roscgcf.webm", loop=True, image="images/v11/Scene 28/v11roscgcStart.webp", start_image="images/v11/Scene 28/v11roscgcStart.webp") # Ms Rose cowgirl choking spedup

    scene v11roscgc # Ignore as animation
    with dissolve
    pause

    ro "*Moans*"

    u "Damn, Lorraine..."

    scene v11roscgcf # Ignore as animation
    with dissolve
    pause

    ro "Oh... that feels good."

    scene v11ros10 # TPP. Show Ms Rose rolling over and pulling MC on top of her for missionary, both slightly smiling, mouths closed
    with dissolve
    
    pause 1

    image v11rosm = Movie(play="images/v11/Scene 28/v11rosm.webm", loop=True, image="images/v11/Scene 28/v11rosmStart.webp", start_image="images/v11/Scene 28/v11rosmStart.webp") # Ms Rose missionary
    image v11rosmf = Movie(play="images/v11/Scene 28/v11rosmf.webm", loop=True, image="images/v11/Scene 28/v11rosmStart.webp", start_image="images/v11/Scene 28/v11rosmStart.webp") # Ms Rose missionary


    scene v11rosm # Ignore as animation
    with dissolve
    pause

    ro "Harder."

    scene v11rosmf # Ignore as animation
    with dissolve
    pause

    ro "Ahh! That's it."

    ro "*Moans*"

    scene v11ros11 # TPP. Show Ms Rose turning over (she has her ass slightly turned to MC)
    with dissolve

    pause 1

    scene v11ros12 # TPP. Show Ms Rose poking her ass up at MC, ready for doggystyle
    with dissolve

    image v11rosdg = Movie(play="images/v11/Scene 28/v11rosdg.webm", loop=True, image="images/v11/Scene 28/v11rosdgStart.webp", start_image="images/v11/Scene 28/v11rosdgStart.webp") # Ms Rose doggystyle with MC holding her hands behind her back
    image v11rosdgf = Movie(play="images/v11/Scene 28/v11rosdgf.webm", loop=True, image="images/v11/Scene 28/v11rosdgStart.webp", start_image="images/v11/Scene 28/v11rosdgStart.webp") # Ms Rose doggystyle with MC holding her hands behind her back sped up

    scene v11rosdg # Ignore as Animation
    with dissolve
    pause

    ro "Go faster, [name]!"

    scene v11rosdgf # Ignore as animaton
    with dissolve
    pause

    ro "Oh my god..."

    u "I'm gonna cum!"

    ro "Do it."

    scene v11ros13 # TPP. Close up shot of Ms Rose's pussy filled with cum (she's doggystyle position)
    with dissolve

    pause 1

    scene v11ros14 # TPP. Show MC and Ms Rose lying next to each other on the bed, looking up
    with dissolve

    pause 0.75

    scene v11ros15 # FPP. MC and Ms Rose still lying in bed, MC and Ms Rose looking at each other, Ms Rose neutral expression, mouth open
    with dissolve

    ro "Umm, don't get comfortable. You need to leave."

    scene v11ros15a # FPP. Same as v11ros15, Ms Rose mouth closed, neutral expression
    with dissolve

    u "Can we talk about what just happened?"

    scene v11ros15
    with dissolve

    ro "If you want this to happen again, the answer is no."

    scene v11ros15a
    with dissolve

    u "*Chuckles* In that case, I'll see you later."

    scene v11ros16 # TPP. Show MC getting out of bed, slight smile, mouth closed, Ms Rose lying down in the bed, mouth closed, neutral expression
    with dissolve
    stop music fadeout 3
    play music "music/v10/Track Scene 41_2.mp3" fadein 2
    pause 1

    scene v11ros17 # TPP. Show MC putting on his pants, Ms Rose sitting down in the bed behind him, still naked, both mouths closed, slight smiles
    with dissolve

    pause 1

    scene v11ros17a # TPP. Same as v11ros17, but MC is putting on his shirt instead
    with dissolve

    pause 1

    scene v11ros18 # FPP. MC is looking at Ms Rose while she is sitting in the bed, still naked, Ms Rose mouth open, slight smile
    with dissolve

    ro "I'll see you tomorrow."

    scene v11ros18a # FPP. Same as v11ros18, Ms Rose mouth closed, slight smile
    with dissolve

    u "See you tomorrow."

    scene v11ros19 # TPP. Show MC leaving the room, Ms Rose naked in the background putting on her bathrobe
    with dissolve

    pause 1

    label v11s28_nsfwSkipLabel1:

    scene v11ros20 # TPP. Show MC slosing the door behind him
    with dissolve

    play sound "sounds/doorclose.mp3"

    $ renpy.end_replay()

    pause 0.75

    scene v11ros21 # FPP. The bartender is walking past MC, looking at him, grinning, mouth closed
    with dissolve

    u "Hey."

    scene v11ros22 # FPP. The bartender continues walking past, not looking at MC now
    with dissolve

    pause 0.75

    scene v11ros23 # FPP. Bartender even further down the corridor, looking at MC now, mouth open, grinning, hand on her mouth as if she were shouting
    with dissolve

    bartender "Player, player!"

    scene v11ros24 # TPP. Show MC walking through the hotel room door 
    with dissolve

    pause 1

    if v11_riley_roomate:
        scene v11ros25 # FPP. MC is standing in the room, he can see Riley sleeping on her bed
        with dissolve

        pause 1

    else:
        scene v11ros25a # FPP. Same cam as v11ros25, but MC can see Chloe sleeping on her bed instead of Riley
        with dissolve

        pause 1 

    scene v11ros26 # TPP. Show MC lying in his bed, under the covers, he is sleeping, room is dark
    with dissolve

    pause 1
    stop music fadeout 3
    jump v11_hotel_room