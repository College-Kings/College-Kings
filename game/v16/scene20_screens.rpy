# Call("free_roam_spoken_too", "image", "label", dialog="(I've already seen this...)")

screen v16s20_amber_living_room():
    tag free_roam
    modal True

    default image_path = "images/v16/Scene 20/"

    if v14_amber_clean:
        add image_path + "v16s20_1.webp"
    else:
        add image_path + "v16s20_1a.webp"

    imagebutton:
        idle Transform("#0000", xysize=(150, 46))
        hover image_path + "Screens/Bills.webp"
        if v14_amber_clean:
            action Jump("v16s20_amber_living_room_unpaid_bills")
        else:
            action Jump("v16s20_amber_living_room_unpaid_bills2")
        pos (817, 794)

    imagebutton:
        idle Transform("#0000", xysize=(82, 112))
        hover image_path + "Screens/Candies.webp"
        if v14_amber_clean:
            action Jump("v16s20_amber_living_room_twazzlers")
        else:
            action Jump("v16s20_amber_living_room_twazzlers2")
        pos (1082, 669)

    imagebutton:
        idle Transform("#0000", xysize=(68, 38))
        hover image_path + "Screens/Charger.webp"
        if v14_amber_clean:
            action Show("confirm", message="Are you sure you want to end the free roam?", yes_action=[Hide("confirm"), Jump("v16s20_amber_living_room_phone_charger")])
        else:
            action Show("confirm", message="Are you sure you want to end the free roam?", yes_action=[Hide("confirm"), Jump("v16s20_amber_living_room_phone_charger2")])
        pos (474, 708)

    imagebutton:
        idle Transform("#0000", xysize=(139, 99))
        hover image_path + "Screens/Laptop.webp"
        if v14_amber_clean:
            action Jump("v16s20_amber_living_room_laptop")
        else:
            action Jump("v16s20_amber_living_room_laptop2")
        pos (1211, 550)

    imagebutton:
        idle Transform("#0000", xysize=(172, 139))
        hover image_path + "Screens/Photos.webp"
        if v14_amber_clean:
            action Jump("v16s20_amber_living_room_photos")
        else:
            action Jump("v16s20_amber_living_room_photos2")
        pos (1472, 231)
