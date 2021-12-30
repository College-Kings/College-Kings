screen v15s18a_bathroom():
    tag free_roam

    default image_path = "images/v15/Scene 18a/Free Roam Screens/bathroom/"

    imagemap:
        if True:
            idle "images/v15/Scene 18a/Free Roam Screens/v15s18a_bathroom_1.webp"
        elif False:
            idle "images/v15/Scene 18a/Free Roam Screens/v15s18a_bathroom_2.webp"
        else:
            idle "images/v15/Scene 18a/Free Roam Screens/v15s18a_bathroom_3.webp"
        hover "images/v15/Scene 18a/Free Roam Screens/v15s18a_bathroom_hover.webp"

        hotspot (1274, 0, 333, 1080) action NullAction() # Back Button

        if True:
            hotspot (1042, 0, 232, 740) action NullAction() # Riley
        if True:
            hotspot (612, 540, 564, 540) action NullAction() # Character Name



screen v15s18a_dining_table():
    tag free_roam

    default image_path = "images/v15/Scene 18a/Free Roam Screens/dining_table/"

    add image_path + "v15s18a_bar_1.webp"
    add image_path + "v15s18a_bar_2.webp"
    add image_path + "v15s18a_bar_3.webp"

    imagebutton:
        idle Transform("#0000", size=(779, 961))
        hover image_path + "v15s18a_bar_hover_aubrey.webp"
        action NullAction()
        pos (290, 119)

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
