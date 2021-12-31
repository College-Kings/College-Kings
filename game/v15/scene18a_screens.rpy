screen v15s18a_bathroom():
    tag free_roam

    default image_path = "images/v15/Scene 18a/Free Roam Screens/bathroom/"

    # Backgrounds
    add image_path + "v15s18a_bathroom_1.webp"
    add image_path + "v15s18a_bathroom_2.webp"
    add image_path + "v15s18a_bathroom_3.webp"

    # Door
    imagebutton:
        idle Transform("#0000", size=(560, 1080))
        hover image_path + "v15s18a_bathroom_hover_door.webp"
        action NullAction()
        pos (1047, 0)

    # Riley
    imagebutton:
        idle Transform("#0000", size=(239, 610))
        hover image_path + "v15s18a_bathroom_hover_riley.webp"
        action NullAction()
        pos (1042, 128)

    # Ryan
    imagebutton:
        idle Transform("#0000", size=(418, 467))
        hover image_path + "v15s18a_bathroom_hover_ryan.webp"
        action NullAction()
        pos (749, 525)


screen v15s18a_bar():
    tag free_roam

    default image_path = "images/v15/Scene 18a/Free Roam Screens/bar/"

    # Backgrounds
    add image_path + "v15s18a_bar_1.webp"
    add image_path + "v15s18a_bar_2.webp"
    add image_path + "v15s18a_bar_3.webp"

    # Aubrey
    imagebutton:
        idle Transform("#0000", size=(779, 961))
        hover image_path + "v15s18a_bar_hover_aubrey.webp"
        action NullAction()
        pos (290, 119)

    # Autumn
    imagebutton:
        idle Transform("#0000", size=(245, 369))
        hover image_path + "v15s18a_bar_hover_autumn.webp"
        action NullAction()
        pos (873, 28)


screen v15s18a_kitchen():
    tag free_roam

    default image_path = "images/v15/Scene 18a/Free Roam Screens/kitchen/"

    # Backgrounds
    add image_path + "v15s18a_kitchen_1.webp"
    add image_path + "v15s18a_kitchen_2.webp"

    # Fridge
    imagebutton:
        idle Transform("#0000", size=(735, 1080))
        hover image_path + "v15s18a_kitchen_hover_fridge.webp"
        action NullAction()
        pos (1167, 0)

    # Riley
    imagebutton:
        idle Transform("#0000", size=(305, 1056))
        hover image_path + "v15s18a_kitchen_hover_riley.webp"
        action NullAction()
        pos (554, 12)


screen v15s18a_living_room():
    tag free_roam

    default image_path = "images/v15/Scene 18a/Free Roam Screens/living_room/"

    # Backgrounds
    add image_path + "v15s18a_livingroom_1.webp"
    add image_path + "v15s18a_livingroom_2.webp"
    add image_path + "v15s18a_livingroom_3.webp"
    add image_path + "v15s18a_livingroom_4.webp"

    # Imre
    imagebutton:
        idle Transform("#0000", size=(634, 740))
        hover image_path + "v15s18a_livingroom_hover_imre.webp"
        action NullAction()
        pos (1002, 272)

    # Lauren
    imagebutton:
        idle Transform("#0000", size=(608, 507))
        hover image_path + "v15s18a_livingroom_hover_lauren.webp"
        action NullAction()
        pos (312, 340)

    # Ryan
    imagebutton:
        idle Transform("#0000", size=(473, 647))
        hover image_path + "v15s18a_livingroom_hover_ryan.webp"
        action NullAction()
        pos (1279, 433)

    # Pumpkin
    imagebutton:
        idle Transform("#0000", size=(156, 143))
        hover image_path + "v15s18a_livingroom_hover_pumpkin.webp"
        action NullAction()
        pos (1013, 317)


screen v15s18a_room():
    tag free_roam

    default image_path = "images/v15/Scene 18a/Free Roam Screens/room/"

    # Backgrounds
    add image_path + "v15s18a_room_1.webp"
    add image_path + "v15s18a_room_2.webp"
    add image_path + "v15s18a_room_3.webp"
    add image_path + "v15s18a_room_4.webp"

    # Amber
    imagebutton:
        idle Transform("#0000", size=(436, 679))
        hover image_path + "v15s18a_room_hover_amber.webp"
        action NullAction()
        pos (704, 48)

    # Amber (with Chris)
    # imagebutton:
    #     idle Transform("#0000", size=(608, 507))
    #     hover image_path + "v15s18a_room_hover_amber2.webp"
    #     action NullAction()
    #     pos (312, 340)

    # Aubrey
    imagebutton:
        idle Transform("#0000", size=(403, 673))
        hover image_path + "v15s18a_room_hover_aubrey.webp"
        action NullAction()
        pos (742, 57)

    # Aubrey (with Imre)
    # imagebutton:
    #     idle Transform("#00ff0080", size=(315, 664))
    #     hover image_path + "v15s18a_room_hover_aubrey2.webp"
    #     action NullAction()
    #     pos (774, 67)

    # Chris
    # imagebutton:
    #     idle Transform("#0000", size=(156, 143))
    #     hover image_path + "v15s18a_room_hover_chris.webp"
    #     action NullAction()
    #     pos (1013, 317)

    # Imre
    # imagebutton:
    #     idle Transform("#00ff0080", size=(253, 429))
    #     hover image_path + "v15s18a_room_hover_imre.webp"
    #     action NullAction()
    #     pos (1043, 42)


screen v15s18a_upstairs():
    tag free_roam

    default image_path = "images/v15/Scene 18a/Free Roam Screens/upstairs/"

    # Backgrounds
    add image_path + "v15s18a_upstairsroom_1.webp"
    add image_path + "v15s18a_upstairsroom_2.webp"

    # Door 1
    imagebutton:
        idle Transform("#0000", size=(391, 1067))
        hover image_path + "v15s18a_upstairsroom_hover_door1.webp"
        action NullAction()
        pos (247, 13)

    # Deer Statue
    imagebutton:
        idle Transform("#0000", size=(149, 615))
        hover image_path + "v15s18a_upstairsroom_hover_deer_statue.webp"
        action NullAction()
        pos (818, 332)

    # Door 2
    imagebutton:
        idle Transform("#0000", size=(283, 600))
        hover image_path + "v15s18a_upstairsroom_hover_door2.webp"
        action NullAction()
        pos (1008, 203)

    # Aubrey (with Imre)
    # imagebutton:
    #     idle Transform("#00ff0080", size=(315, 664))
    #     hover image_path + "v15s18a_upstairsroom_hover_aubrey2.webp"
    #     action NullAction()
    #     pos (774, 67)

    # Chris
    # imagebutton:
    #     idle Transform("#0000", size=(156, 143))
    #     hover image_path + "v15s18a_upstairsroom_hover_chris.webp"
    #     action NullAction()
    #     pos (1013, 317)
