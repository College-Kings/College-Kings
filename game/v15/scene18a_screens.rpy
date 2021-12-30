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


screen v15s18a_dining_table():
    tag free_roam

    default image_path = "images/v15/Scene 18a/Free Roam Screens/dining_table/"

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


screen v15s18a_living_room():
    tag free_roam


screen v15s18a_room():
    tag free_roam


screen v15s18a_upstairs():
    tag free_roam
