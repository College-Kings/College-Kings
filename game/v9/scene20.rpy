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

        $ s20KiwiiPost = KiwiiPost("Chris", "v9/s20KiwiiWolf.webp", "Who's ready?!", numberLikes=renpy.random.randint(200, 300))
        $ s20KiwiiPost.addComment("Imre", "Ding! Ding! Ding!", numberLikes=renpy.random.randint(200, 250), queue=False)
        $ s20KiwiiPost.addComment("Cameron", "Whatever man! You're going down!", numberLikes=renpy.random.randint(200, 250), queue=False)
        $ s20KiwiiPost.addReply("Fuck yeah!", numberLikes=renpy.random.randint(100, 200))

        pause 0.5

    else:
        scene v9rfa3 # TPP. Show MC sat at his desk in his Apes room studying.
        with fade

        pause 1

        scene v9rfa3a # TPP. Same camera as v9rfa3, show MC stretching & yawning.
        with dissolve

        u "(This is so boring.)"

        scene v9rfa4 # TPP. Show MC sat at his desk on his phone.
        with dissolve
       

        $ s20KiwiiPost = KiwiiPost("Grayson", "v9/s20KiwiiApe.webp", "Where my APES at?", numberLikes=renpy.random.randint(200, 300))
        $ s20KiwiiPost.addComment("Cameron", "The BEST Ape is right here!", numberLikes=renpy.random.randint(200, 250), queue=False)
        $ s20KiwiiPost.addComment("Ryan", "I'm SO ready!", numberLikes=renpy.random.randint(200, 250), queue=False)
        $ s20KiwiiPost.addReply("Let's go!!", numberLikes=renpy.random.randint(100, 200))

        pause 0.5

    call screen phone
    label s20_phoneExitW:
        if s20KiwiiPost.getReplies():
            "(I should check Kiwii)"
            jump s20_phoneExitW
        jump v9_room_fri_aft_contW

label v9_room_fri_aft_contW:
    scene v9rfa2a # TPP. Same camera as v9rfa2, show MC placing his phone on his desk.
    with dissolve

    u "(They're really hyping this thing up. I need to get some workouts in before it's too late)"

    jump v9_room_w_chris

label v9_room_fri_aft_contA:
    scene v9rfa4a # TPP. Same camera as v9rfa4, show MC placing his phone on his desk.
    with dissolve

    u "(They're really hyping this thing up. I need to get some workouts in before it's too late)"

    jump v9_room_w_sam