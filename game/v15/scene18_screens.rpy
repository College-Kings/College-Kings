screen v15s18a_room():
    tag free_roam

    default image_path = "images/v15/Scene 18a/Free Roam Screens/room/"

    if not "lauren2" in freeroam13:
        if not "chris_amber" in freeroam13:
            add image_path + "v15s18a_room_1.webp"
        else:
            add image_path + "v15s18a_room_2.webp"
    else:
        add image_path + "v15s18a_room_3.webp"

    if not "lauren2" in freeroam13:
        if not "chris_amber" in freeroam13: # Amber and Chris
            # Amber
            imagebutton:
                idle Transform("#0000", size=(389, 689))
                hover image_path + "v15s18a_room_hover_amber.webp"
                action Jump("v15s18a_ChrisAmber")
                pos (755, 42)

            # Chris
            imagebutton:
                idle Transform("#0000", size=(307, 468))
                hover image_path + "v15s18a_room_hover_chris.webp"
                action Jump("v15s18a_ChrisAmber")
                pos (1005, 59)
        
        else: # Amber
            add image_path + "v15s18a_room_2.webp"
            
            imagebutton:
                idle Transform("#0000", size=(436, 679))
                hover image_path + "v15s18a_room_hover_amber2.webp"
                action Call("freeRoamSpokenToo", backgroundImg="v15s18a_room_2", returnScreen="v15s18a_room")
                pos (704, 48)

    else:
        # Aubrey
        imagebutton:
            idle Transform("#0000", size=(403, 673))
            hover image_path + "v15s18a_room_hover_aubrey.webp"
            if not "imre_aubrey" in freeroam14:
                action Jump("v15s18c_imre_aubrey")
            else:
                action Call("freeRoamSpokenToo", backgroundImg="v15s18a_room_3", returnScreen="v15s18a_room")
            pos (742, 57)

        # Imre
        imagebutton:
            idle Transform("#0000", size=(253, 429))
            hover image_path + "v15s18a_room_hover_imre.webp"
            if not "imre_aubrey" in freeroam14:
                action Jump("v15s18c_imre_aubrey")
            else:
                action Call("freeRoamSpokenToo", backgroundImg="v15s18a_room_3", returnScreen="v15s18a_room")
            pos (1039, 52)
    
    imagebutton:
        idle Transform("#0000", size=(140,1080))
        hover image_path + "left.webp"
        action Show("v15s18a_livingroom")
        pos (0, 0)

    imagebutton:
        idle Transform("#0000", size=(140,1080))
        hover image_path + "right.webp"
        action Show("v15s18a_kitchen")
        pos (1780, 0)

    imagebutton:
        idle Transform("#0000", size=(1330, 180))
        hover image_path + "bottom.webp"
        action Show("v15s18a_stairs")
        pos (325, 900)

screen v15s18a_livingroom():
    tag free_roam

    default image_path = "images/v15/Scene 18a/Free Roam Screens/livingroom/"

    if not "lauren2" in freeroam13:
        add image_path + "v15s18a_livingroom_2.webp"
    else:
        add image_path + "v15s18a_livingroom_4.webp"

    if not "lauren2" in freeroam13:
        if not "imre_lauren" in freeroam13:
            # Imre
            imagebutton:
                idle Transform("#0000", size=(634, 740))
                hover image_path + "v15s18a_livingroom_hover_imre.webp"
                action Jump("v15s18a_ImreLauren")
                pos (1002, 272)

            # Lauren
            imagebutton:
                idle Transform("#0000", size=(608, 507))
                hover image_path + "v15s18a_livingroom_hover_lauren.webp"
                action Jump("v15s18a_ImreLauren")
                pos (312, 340)

        else:
            # Lauren
            imagebutton:
                idle Transform("#0000", size=(608, 507))
                hover image_path + "v15s18a_livingroom_hover_lauren.webp"
                action Show("confirm", message="Are you sure you want to end the free roam?", yes_action=[Hide("confirm"), Jump("v15s18b")])
                pos (312, 340)

    else:
            # Ryan
            imagebutton:
                idle Transform("#0000", size=(473, 647))
                hover image_path + "v15s18a_livingroom_hover_ryan.webp"
                if not "ryan" in freeroam14:
                    action Jump("v15s18c_ryan")
                else:
                    action Call("freeRoamSpokenToo", backgroundImg="v15s18a_livingroom_4", returnScreen="v15s18a_livingroom")
                pos (1279, 433) 

    # Pumpkin
    if v15s18_pumpkin < 5:
        imagebutton:
            idle Transform("#0000", size=(156, 143))
            hover image_path + "v15s18a_livingroom_hover_pumpkin.webp"
            action Jump("v15s18a_Pumpkin")
            pos (1013, 317)

    imagebutton:
        idle Transform("#0000", size=(140,1080))
        hover image_path + "right.webp"
        action Show("v15s18a_room")
        pos (1780, 0)

    imagebutton:
        idle Transform("#0000", size=(1330, 180))
        hover image_path + "bottom.webp"
        action Show("v15s18a_bar")
        pos (325, 900)

screen v15s18a_bar():
    tag free_roam

    default image_path = "images/v15/Scene 18a/Free Roam Screens/bar/"

    if not "lauren2" in freeroam13:
        add image_path + "v15s18a_bar_1.webp"
    elif not "autumn_amber" in freeroam14:
        add image_path + "v15s18a_bar_2.webp"
    else:
        add image_path + "v15s18a_bar_3.webp"

    if not "lauren2" in freeroam13:
        # Aubrey
        imagebutton:
            idle Transform("#0000", size=(569, 968))
            hover image_path + "v15s18a_bar_hover_aubrey.webp"
            if not "aubrey" in freeroam13:
                action Jump("v15s18a_Aubrey")
            else:
                action Call("freeRoamSpokenToo", backgroundImg="v15s18a_bar_1", returnScreen="v15s18a_bar")
            pos (510, 110)

    elif not "autumn_amber" in freeroam14:
        # Autumn
        imagebutton:
            idle Transform("#0000", size=(245, 369))
            hover image_path + "v15s18a_bar_hover_autumn.webp"
            if not "autumn_amber" in freeroam14:
                action Jump("v15s18c_autumn_amber")
            else:
                action Call("freeRoamSpokenToo", backgroundImg="v15s18a_bar_2", returnScreen="v15s18a_bar")
            pos (873, 28)

        # Amber
        imagebutton:
            idle Transform("#0000", size=(579, 989))
            hover image_path + "v15s18a_bar_hover_amber.webp"
            if not "autumn_amber" in freeroam14:
                action Jump("v15s18c_autumn_amber")
            else:
                action Call("freeRoamSpokenToo", backgroundImg="v15s18a_bar_2", returnScreen="v15s18a_bar")
            pos (440, 90)

    imagebutton:
        idle Transform("#0000", size=(1330, 180))
        hover image_path + "bottom.webp"
        action Show("v15s18a_livingroom")
        pos (325, 900)

screen v15s18a_kitchen():
    tag free_roam

    default image_path = "images/v15/Scene 18a/Free Roam Screens/kitchen/"

    if not "lauren2" in freeroam13:
        add image_path + "v15s18a_kitchen_1.webp"

        # Riley
        imagebutton:
            idle Transform("#0000", size=(305, 1056))
            hover image_path + "v15s18a_kitchen_hover_riley.webp"
            if not "riley" in freeroam13:
                action Jump("v15s18a_Riley")
            else:
                action Call("freeRoamSpokenToo", backgroundImg="v15s18a_kitchen_1", returnScreen="v15s18a_kitchen")
            pos (554, 12)

    else:
        add image_path + "v15s18a_kitchen_2.webp"
    
    # Fridge
    if not "photo" in freeroam13:
        imagebutton:
            idle Transform("#0000", size=(735, 1080))
            hover image_path + "v15s18a_kitchen_hover_fridge.webp"
            action Jump("v15s18a_AutumnLaurenPhoto")
            pos (1167, 0)

    imagebutton:
        idle Transform("#0000", size=(140,1080))
        hover image_path + "left.webp"
        action Show("v15s18a_room")
        pos (0, 0)

    imagebutton:
        idle Transform("#0000", size=(1330, 180))
        hover image_path + "bottom.webp"
        action Show("v15s18a_stairs")
        pos (325, 900)

screen v15s18a_upstairsroom():
    tag free_roam

    default image_path = "images/v15/Scene 18a/Free Roam Screens/upstairsroom/"

    if ("lauren2" not in freeroam13) or ("chris_penelope" in freeroam14):
        add image_path + "v15s18a_upstairsroom_1.webp"
    else:
        add image_path + "v15s18a_upstairsroom_2.webp"

    # Chris and Penelope
    if ("lauren2" in freeroam13) and not ("chris_penelope" in freeroam14):
        imagebutton:
            idle Transform("#0000", size=(420, 672))
            hover image_path + "v15s18a_upstairsroom_hover_chris.webp"
            if not "chris_penelope" in freeroam14:
                action Jump ("v15s18c_chris_penelope")
            else:
                action Call("freeRoamSpokenToo", backgroundImg="v15s18a_upstairsroom_2", returnScreen="v15s18a_upstairsroom")
            pos (1500, 200)

    # Door 1, Bathroom (Ryan, then Riley)
    imagebutton:
        idle Transform("#0000", size=(391, 1067))
        hover image_path + "v15s18a_upstairsroom_hover_door1.webp"
        
        if not "lauren2" in freeroam13:
            if not "ryan" in freeroam13:
                action Jump("v15s18a_Ryan")
            else:
                action Call("freeRoamSpokenToo", backgroundImg="v15s18a_upstairsroom_1", returnScreen="v15s18a_upstairsroom")
        else:
            if not "riley" in freeroam14:
                action Jump("v15s18c_riley")
            else:
                action Call("freeRoamSpokenToo", backgroundImg="v15s18a_upstairsroom_2", returnScreen="v15s18a_upstairsroom")
        pos (247, 13)

    # Door 2
    imagebutton:
        idle Transform("#0000", size=(283, 600))
        hover image_path + "v15s18a_upstairsroom_hover_door2.webp"
        
        if not "lauren2" in freeroam13:
            if not "autumn_penelope" in freeroam13:
                action Jump("v15s18a_AutumPenelope")
            else:
                action Call("freeRoamSpokenToo", backgroundImg="v15s18a_upstairsroom_1", returnScreen="v15s18a_upstairsroom")
        else:
            if not "lauren" in freeroam14:
                action Jump("v15s18c_lauren")
            else:
                action Show("confirm", message="Are you sure you want to end the free roam?", yes_action=[Hide("confirm"), Jump("v15s18d")])
        pos (1008, 203)

    # Deer Statue
    if not "deer" in freeroam13:
        imagebutton:
            idle Transform("#0000", size=(149, 615))
            hover image_path + "v15s18a_upstairsroom_hover_deer_statue.webp"
            action Jump ("v15s18a_BronzeDeer")
            pos (818, 332)

    imagebutton:
        idle Transform("#0000", size=(1330, 180))
        hover image_path + "bottom.webp"
        action Show("v15s18a_stairs")
        pos (325, 900)

screen v15s18a_stairs():
    tag free_roam

    default image_path = "images/v15/Scene 18a/Free Roam Screens/stairs/"

    add image_path + "v15s18a_stairs.webp"
    
    imagebutton:
        idle Transform("#0000", size=(936, 1080))
        hover image_path + "v15s18a_stairs_hover.webp"
        action Show("v15s18a_upstairsroom")
        pos (984, 0)

    imagebutton:
        idle Transform("#0000", size=(140,1080))
        hover image_path + "left.webp"
        action Show("v15s18a_kitchen")
        pos (0, 0)

    imagebutton:
        idle Transform("#0000", size=(1330, 180))
        hover image_path + "bottom.webp"
        action Show("v15s18a_room")
        pos (325, 900)