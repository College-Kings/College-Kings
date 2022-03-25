screen v16s15_pier_entrance():
    tag free_roam
    modal True

    default image_path = "images/v16/Scene 15/Free Roam Screens/"

    add image_path + "v16s15pier_entrance.webp"

    imagebutton:
        idle Transform("#0000", xysize=(613, 566))
        hover image_path + "Highlights/v16s15pier_entrance_hotdog.webp"
        if not "hotdog" in freeroam15:
            action Jump("v16s15pier_hotdog")
        else:
            action Call("free_roam_spoken_too", "v16s15pier_entrance", "v16s15_pier_entrance")
        pos (559, 478)

    imagebutton:
        idle Transform("#0000", xysize=(237, 550))
        hover image_path + "Highlights/v16s15pier_entrance_left.webp"
        action Show("v16s15_pier_middle_carousel")
        pos (354, 396)

    imagebutton:
        idle Transform("#0000", xysize=(237, 550))
        hover image_path + "Highlights/v16s15pier_entrance_right.webp"
        action Show("v16s15_pier_middle_range")
        pos (1320, 396)


screen v16s15_pier_middle_carousel():
    tag free_roam
    modal True

    default image_path = "images/v16/Scene 15/Free Roam Screens/"

    if "wheel_strong" in freeroam15:
        add image_path + "v16s15pier_middle_carousel_2.webp"
    else:
        add image_path + "v16s15pier_middle_carousel.webp"
        
    imagebutton:
        idle Transform("#0000", xysize=(383, 668))
        hover image_path + "Highlights/v16s15pier_middle_carousel_carousel.webp"
        action Jump("v16s15pier_date_carousel")
        pos (1537, 330)

    if "wheel_strong" in freeroam15:
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
        action Show("v16s15_pier_entrance")
        align (0.5, 1.0)


screen v16s15_pier_middle_range():
    tag free_roam
    modal True

    default image_path = "images/v16/Scene 15/Free Roam Screens/"

    add image_path + "v16s15pier_middle_range.webp"

    imagebutton:
        idle Transform("#0000", xysize=(1330, 180))
        hover "images/common/free-roam-highlights/bottom.webp"
        action Show("v16s15_pier_entrance")
        align (0.5, 1.0)

    imagebutton:
        idle Transform("#0000", xysize=(850, 465))
        hover image_path + "Highlights/v16s15pier_middle_range_shoot.webp"
        action Show("confirm", message="Are you sure you want to end the free roam?", yes_action=[Hide("confirm"), Jump("v16s15pier_date_wheel_2")])
        pos (528, 348)