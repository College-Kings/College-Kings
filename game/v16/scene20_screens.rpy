# Call("free_roam_spoken_too", "image", "label", dialog="(I've already seen this...)")

screen v16s20_amber_living_room():
    tag free_roam
    modal True

    default image_path = "images/v16/Scene 20/"

    if v14_amber_clean:
        if v16s20_take_twazzlers:
            add image_path + "v16s20_1c.webp"
        else:
            add image_path + "v16s20_1.webp"
    else:
        if v16s20_take_twazzlers:
            add image_path + "v16s20_1b.webp"
        else:
            add image_path + "v16s20_1a.webp"

    if not "bills" in freeroam16:
        imagebutton:
            idle Transform("#0000", xysize=(150, 46))
            hover image_path + "Screens/Bills.webp"
            action Jump("v16s20_amber_living_room_unpaid_bills")
            pos (817, 794)

    if not "twazzlers" in freeroam16:
        imagebutton:
            idle Transform("#0000", xysize=(82, 112))
            hover image_path + "Screens/Candies.webp"
            action Jump("v16s20_amber_living_room_twazzlers")
            pos (1082, 669)

    if not "laptop" in freeroam16:
        imagebutton:
            idle Transform("#0000", xysize=(139, 99))
            hover image_path + "Screens/Laptop.webp"
            action Jump("v16s20_amber_living_room_laptop")
            pos (1211, 550)

    if not "photos" in freeroam16:
        imagebutton:
            idle Transform("#0000", xysize=(172, 139))
            hover image_path + "Screens/Photos.webp"
            action Jump("v16s20_amber_living_room_photos")
            pos (1472, 231)

    imagebutton:
        idle Transform("#0000", xysize=(68, 38))
        hover image_path + "Screens/Charger.webp"
        action Show("confirm", message="Are you sure you want to end the free roam?", yes_action=[Hide("confirm"), Jump("v16s20_amber_living_room_phone_charger")])
        pos (474, 708)