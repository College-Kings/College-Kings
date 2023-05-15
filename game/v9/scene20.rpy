# SCENE 20: Your Room Fri Afternoon
# Locations: MC Wolves/Apes room
# Characters: MC (Outfit 3)
# Time: Friday Afternoon
# KIWII IMAGES: s20KiwiiWolf = Red Boxing Glove | s20KiwiiApe = Muscular MMA style fighter

label v9_room_fri_aft:
    if mc.frat == Frat.WOLVES:
        scene v9rfa1 # TPP. Show MC sat at his desk in his Wolves room studying.
        with fade

        pause 1

        scene v9rfa1a # TPP. Same camera as v9rfa1, show MC stretching & yawning.
        with dissolve

        u "(This is so boring.)"

        scene v9rfa2 # TPP. Show MC sat at his desk on his phone.
        with dissolve

        $ kiwii_post = KiwiiService.new_post(chris, "v9/Scene 20/s20KiwiiWolf.webp", "Who's ready?!", number_likes=renpy.random.randint(200, 300))
        $ KiwiiService.new_comment(kiwii_post, imre, "Ding! Ding! Ding!", number_likes=renpy.random.randint(200, 250))
        $ KiwiiService.new_comment(kiwii_post, cameron, "Whatever man! You're going down!", number_likes=renpy.random.randint(200, 250))
        $ KiwiiService.add_reply(kiwii_post, _("Fuck yeah!"), number_likes=renpy.random.randint(100, 200))

        pause 0.5

        while KiwiiService.has_replies(kiwii_post):
            call screen phone
            if KiwiiService.has_replies(kiwii_post):
                u "(I should reply to that post on Kiwii.)"

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
       

        $ kiwii_post = KiwiiService.new_post(grayson, "v9/Scene 20/s20KiwiiApe.webp", "Where my APES at?", number_likes=renpy.random.randint(200, 300))
        $ KiwiiService.new_comment(kiwii_post, cameron, "The BEST Ape is right here!", number_likes=renpy.random.randint(200, 250))
        $ KiwiiService.new_comment(kiwii_post, ryan, "I'm SO ready!", number_likes=renpy.random.randint(200, 250))
        $ KiwiiService.add_reply(kiwii_post, _("Let's go!!"), number_likes=renpy.random.randint(100, 200))

        pause 0.5

        while KiwiiService.has_replies(kiwii_post):
            call screen phone
            if KiwiiService.has_replies(kiwii_post):
                u "(I should reply to that post on Kiwii.)"

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