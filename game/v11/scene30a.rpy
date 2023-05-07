# SCENE 30a: MC Lauren's room apology
# Location: Hotel Room, Outside Hotel Room, Park, Sidewalk, Hotel Lobby
# Characters: MC (Outfit 9), Lauren (Outfit 1), Lindsey (Outfit 1)
# Time: Morning

label v11_lauren_apology:
    scene v11laa1 # TPP. MC is walking through the hotel corridor, mouth closed, slightly sad
    with fade
    play music "music/v10/Track Scene 40_3.mp3" fadein 2
    u "(*Sighs* I should try and talk to Lauren.)"

    scene v11laa1a # TPP. Same camera as v11laa1, but MC is now further down the corridor
    with dissolve

    pause 0.75

    scene v11laa2 # TPP. MC is standing in front of Lauren's room door, he is slightly nervous, mouth closed
    with dissolve

    pause 0.75

    play sound sound.knock

    scene v11laa3 # FPP. MC is looking at the door, he is knocking on the door
    with dissolve

    u "Lauren... can we please talk?"

    scene v11laa4 # TPP. Lauren is lying on her bed, tears in her eyes, mouth open, sad
    with dissolve

    la "[name], go away."

    scene v11laa3a # FPP. Same as v11laa3, but MC is not knocking on the door
    with dissolve

    u "Lauren, please... let's just talk."

    la "..."

    u "Lauren?"

    scene v11laa3b # FPP. Same cam as v11laa3, MC is looking at Lauren opening the door (make sure not fully open yet), Lauren tears in her eye, mouth closed, very sad
    with dissolve

    pause 1.25

    scene v11laa3c # FPP. Same cam as v11laa3, The door is fully open, she has her back turned to MC, she is heading towards the bed
    with dissolve

    pause 1.25

    scene v11laa5 # FPP. MC is now in the room, Lauren is sitting on the bed, looking down, tears in her eyes, mouth closed, very sad
    with dissolve

    pause 1.25

    scene v11laa6 # FPP. MC is now sitting on the bed, he is next to Lauren, Lauren looking down, tears in eyes, mouth closed, very sad
    with dissolve

    u "Look Lauren, I know I fucked up. I don't want to make excuses or anything like that, I just want to apologize. It was a moment that I wish I could take back."

    scene v11laa6a # FPP. Same cam as v11laa6, Lauren now looking at MC, she is very sad, crying, mouth open
    with dissolve

    la "You know everything I've been through and yet you still betrayed me, [name]."

    scene v11laa7 # FPP. MC is now looking down, he is sitting on the bed
    with dissolve

    u "..."

    scene v11laa6a
    with dissolve

    la "You don't have anything to say? The girl that gave her everything to you is sitting right here in front of you and you just say nothing?"

    scene v11laa6b # FPP. Same as v11laa6a, Lauren very sad, looking at MC, crying, mouth closed
    with dissolve

    u "I care about you so much Lauren, more than you know. I just made a mistake."

    scene v11laa6a
    with dissolve

    la "I don't know how to deal with you, with all of this. \"I made a mistake\"? You say it like it was just a small thing."

    la "You fucked Aubrey on the plane knowing damn well I was just a few feet away."

    scene v11laa6b
    with dissolve

    menu:
        "Leave":
            scene v11laa6b
            with dissolve

            u "I know Lauren, I know. I hope it's possible for you to forgive me."

            scene v11laa6a
            with dissolve

            la "I don't know if I can, [name]."

            scene v11laa6b
            with dissolve

            u "*Sighs* I'll leave you be. Call me if you need anything."

        "Make a move":
            scene v11laa6c # FPP. Same as v11laa6b, MC is grabbing Lauren's cheek, she's crying, mouth closed
            with dissolve

            u "Lauren, you know how much I care for you. I promise, I'll never do anything like this ever again."

            scene v11laa8 # TPP. Show MC and Lauren kissing, she has tears on her face
            with dissolve

            play sound "sounds/kiss.mp3"

            pause 1

            scene v11laa6d # FPP. Same as v11laa6a, Lauren pissed and sad, mouth open, crying
            with dissolve

            la "No, no [name]! This isn't right. You can't just try and kiss your way into me forgiving you."

            scene v11laa6b
            with dissolve

            u "I'm... I'm sorry."

            scene v11laa6a
            with dissolve

            la "*Sighs* Just leave."

            scene v11laa6b
            with dissolve

            u "*Sighs* Call me if you need anything."
    
    scene v11laa9 # TPP. Show MC walking out of Lauren's room, he is sad, mouth closed, show Lauren in the background crying intensely, mouth closed
    with dissolve

    pause 0.75

    scene v11laa1
    with dissolve

    pause 0.75

    scene v11laa11 # TPP. Show MC walking through the lobby, sad, mouth closed
    with dissolve

    u "(Fuck man, I've gotta clear my fucking head.)"

    scene v11laa12 # TPP. Show MC leaving the hotel, sad, mouth closed
    with dissolve

    pause 0.75

    scene v11laa13 # TPP. Show MC walking on the sidewalk near the park, he is sad, mouth closed
    with fade

    pause 0.75

    scene v11laa14 # FPP. MC can see Lindsey sitting in a park bench, she is slightly sad, mouth closed
    with dissolve

    u "(Maybe she can make my day a little better.)"
    stop music fadeout 3
    jump v11_lindsey_park