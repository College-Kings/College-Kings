init python:
    from enum import Enum

    class CarDescription(Enum):
        LIE = 1
        TRUTH = 2


screen iBuy(car_images=["car1.webp"]):
    zorder 100

    default car_images_index = 0

    add "images/v14/iBuy/background.webp"

    vbox:
        xalign 0.5

        text "Car Description: {}".format(v14s48_car_description.name):
            xalign 0.5
        text "Car Price: {}".format(v14s48_campaign_money):
            xalign 0.5

    hbox:
        xalign 0.5
        ypos 186
        spacing 150

        imagebutton:
            idle "images/v14/iBuy/arrow_left.webp"
            action SetScreenVariable("car_images_index", car_images_index - 1)
            sensitive car_images_index > 0
            yalign 0.5

        add Transform("images/v14/iBuy/{}".format(car_images[car_images_index]), size=(929, 358))

        imagebutton:
            idle "images/v14/iBuy/arrow_right.webp"
            action SetScreenVariable("car_images_index", car_images_index + 1)
            sensitive car_images_index < len(car_images) - 1
            yalign 0.5


    # Select Car Description
    add "images/v14/iBuy/descriptions_only.webp":
        xalign 0.5
        ypos 583

    button:
        area (174, 650, 771, 208)
        action SetVariable("v14s48_car_description", CarDescription.LIE)

    button:
        area (945, 650, 786, 208)
        action SetVariable("v14s48_car_description", CarDescription.TRUTH) 


    # Determine Price
    bar:
        value VariableValue("v14s48_campaign_money", 800)
        pos (703, 868)
        maximum (897, 50)

    add "images/v14/iBuy/price_scale.webp":
        xalign 0.5
        ypos 868

    # Confirm
    imagebutton:
        idle "images/v14/iBuy/confirm.webp"
        action Hide("iBuy")
        xalign 0.5
        ypos 973