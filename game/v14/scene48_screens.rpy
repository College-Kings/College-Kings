screen iBuy():
    zorder 100

    default car_images = ["car1.png"]
    default car_images_index = 0

    add "images/v14/iBuy/background.png"

    hbox:
        xalign 0.5
        ypos 186
        spacing 150

        imagebutton:
            idle "images/v14/iBuy/arrow_left.png"
            action SetScreenVariable("car_images_index", car_images_index - 1)
            sensitive car_images_index > 0
            yalign 0.5

        add Transform("images/v14/iBuy/{}".format(car_images[car_images_index]), size=(929, 358))

        imagebutton:
            idle "images/v14/iBuy/arrow_right.png"
            action SetScreenVariable("car_images_index", car_images_index + 1)
            sensitive car_images_index < len(car_images) - 1
            yalign 0.5

    imagemap:
        idle "images/v14/iBuy/descriptions_only.png"
        xalign 0.5
        ypos 583

        hotspot (174, 629, 771, 208) action NullAction()

        hotspot (945, 629, 786, 208) action NullAction()

    add "images/v14/iBuy/price_scale.png":
        xalign 0.5
        ypos 868

    text str(v14s48_campaign_money)

    # bar:
    #     value VariableValue("v14s48_campaign_money", 1000)
    #     xalign 0.5
    #     ypos 844
        

    imagebutton:
        idle "images/v14/iBuy/confirm.png"
        action NullAction()
        xalign 0.5
        ypos 973