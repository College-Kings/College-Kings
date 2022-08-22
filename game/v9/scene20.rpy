# SCENE 20: Your Room Fri Afternoon
# Locations: MC Wolves/Apes room
# Characters: MC (Outfit 3)
# Time: Friday Afternoon
# KIWII IMAGES: s20KiwiiWolf = Red Boxing Glove | s20KiwiiApe = Muscular MMA style fighter

label v9_room_fri_aft:
    if joinwolves:
        scene v9rfa1 # TPP. Show MC sat at his desk in his Wolves room studying.
        with fade

        pause 1

        scene v9rfa1a # TPP. Same camera as v9rfa1, show MC stretching & yawning.
        with dissolve

        u "(This is so boring.)"

        scene v9rfa2 # TPP. Show MC sat at his desk on his phone.
        with dissolve

        $ v9s20KiwiiPost1 = KiwiiPost(chris, "v9/Scene 20/s20KiwiiWolf.webp", "Who's ready?!", numberLikes=renpy.random.randint(200, 300))
        $ v9s20KiwiiPost1.newComment(imre, "Ding! Ding! Ding!", numberLikes=renpy.random.randint(200, 250))
        $ v9s20KiwiiPost1.newComment(cameron, "Whatever man! You're going down!", numberLikes=renpy.random.randint(200, 250))
        $ v9s20KiwiiPost1.addReply("Fuck yeah!", numberLikes=renpy.random.randint(100, 200))

        pause 0.5

        label s20_phoneExit1:
            if v9s20KiwiiPost1.replies:
                call screen phone
            if v9s20KiwiiPost1.replies:
                u "(I should reply to that post on Kiwii.)"
                jump s20_phoneExit1

        jump v9_room_fri_aft_contW

    else:
        scene v9rfa3 # TPP. Show MC sat at his desk in his Apes room studying.
        with fade

        pause 1

        scene v9rfa3a # TPP. Same camera as v9rfa3, show MC stretching & yawning.
        with dissolve

        u "(This is so boring.)"

        scene v9rfa4 # TPP. Show MC sat at his desk on his phone.
        with dissolve
       

        $ v9s20KiwiiPost2 = KiwiiPost(grayson, "v9/Scene 20/s20KiwiiApe.webp", "Where my APES at?", numberLikes=renpy.random.randint(200, 300))
        $ v9s20KiwiiPost2.newComment(cameron, "The BEST Ape is right here!", numberLikes=renpy.random.randint(200, 250))
        $ v9s20KiwiiPost2.newComment(ryan, "I'm SO ready!", numberLikes=renpy.random.randint(200, 250))
        $ v9s20KiwiiPost2.addReply("Let's go!!", numberLikes=renpy.random.randint(100, 200))

        pause 0.5

        label s20_phoneExit2:
            if v9s20KiwiiPost2.replies:
                call screen phone
            if v9s20KiwiiPost2.replies:
                u "(I should reply to that post on Kiwii)"
                jump s20_phoneExit2
        jump v9_room_fri_aft_contA

label v9_room_fri_aft_contW:
    scene v9rfa2a # TPP. Same camera as v9rfa2, show MC placing his phone on his desk.
    with dissolve

    u "(They're really hyping this thing up. I need to get some workouts in before it's too late.)"

    jump v9_room_w_chris

label v9_room_fri_aft_contA:
    scene v9rfa4a # TPP. Same camera as v9rfa4, show MC placing his phone on his desk.
    with dissolve

    u "(They're really hyping this thing up. I need to get some workouts in before it's too late.)"

    jump v9_room_w_sam