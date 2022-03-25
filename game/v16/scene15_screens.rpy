screen v16s15_pier_entrance():
    tag free_roam
    modal True

    default image_path = "images/v16/Scene 15/Free Roam Screens/"

    add image_path + "v16s15pier_entrance.webp"

    imagebutton:
        idle Transform("#0000", xysize=(613, 566))
        hover image_path + "Highlights/v16s15pier_entrance_hotdog.webp"
        action Show("v16s15_pier_middle_carousel")
        pos (559, 478)

    imagebutton:
        idle Transform("#0000", xysize=(237, 550))
        hover image_path + "Highlights/v16s15pier_entrance_left.webp"
        action Jump("v16s15pier_date_wheel")
        pos (354, 396)

    imagebutton:
        idle Transform("#0000", xysize=(237, 550))
        hover image_path + "Highlights/v16s15pier_entrance_right.webp"
        action Show("v16s15_pier_middle_carousel")
        pos (1320, 396)


screen v16s15_pier_middle_carousel():
    tag free_roam
    modal True

    default image_path = "images/v16/Scene 15/Free Roam Screens/"

    if v16s15_carousel_strong_spin:
        add image_path + "v16s15pier_middle_carousel_2.webp"
    else:
        add image_path + "v16s15pier_middle_carousel.webp"
        
    imagebutton:
        idle Transform("#0000", xysize=(383, 668))
        hover image_path + "Highlights/v16s15pier_middle_carousel_carousel.webp"
        action Jump("v16s15pier_date_carousel")
        pos (1537, 330)

    if v16s15_carousel_strong_spin:
        imagebutton:
            idle Transform("#0000", xysize=(601, 762))
            hover image_path + "Highlights/v16s15pier_middle_carousel_2_wheel.webp"
            action NullAction()
            pos (204, 318)

    else:
        imagebutton:
            idle Transform("#0000", xysize=(514, 762))
            hover image_path + "Highlights/v16s15pier_middle_carousel_wheel.webp"
            action Jump("v16s15pier_date_wheel")
            ypos 318
      
    imagebutton:
        idle Transform("#0000", xysize=(1330, 180))
        hover "images/common/free-roam-highlights/bottom.webp"
        action Show("v16s15_pier_middle_range")
        align (0.5, 1.0)


screen v16s15_pier_middle_range():
    tag free_roam
    modal True

    default image_path = "images/v16/Scene 15/Free Roam Screens/"

    add image_path + "v16s15pier_middle_range.webp"

    imagebutton:
        idle Transform("#0000", xysize=(272, 770))
        hover image_path + "Highlights/v16s15pier_middle_range_left.webp"
        action Jump("")
        pos (125, 293)

    imagebutton:
        idle Transform("#0000", xysize=(272, 770))
        hover image_path + "Highlights/v16s15pier_middle_range_right.webp"
        action Jump("")
        pos (1509, 293)

    imagebutton:
        idle Transform("#0000", xysize=(850, 465))
        hover image_path + "Highlights/v16s15pier_middle_range_shoot.webp"
        action Show("confirm", message="Are you sure you want to end the free roam?", yes_action=[Hide("confirm"), Jump("v16s15pier_date_wheel_2")])
        pos (528, 348)
