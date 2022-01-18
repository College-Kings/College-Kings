init python:
    class CarDescription(Enum):
        LIE = 1
        TRUTH = 2

screen iBuy():
    zorder 100

    default car_images_index = 0

    add "images/v14/iBuy/background.webp"

    add "images/v14/iBuy/price_scale_background.webp":
        pos(301,865)

    hbox:
        xalign 0.78
        yalign 0.9
        spacing 20

        text "Car Price: ${}".format(v14s48_car_price):
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

        add Transform("images/v14/Scene 47/{}".format(v14s47_car_pics[car_images_index]), size=(929, 358))

        imagebutton:
            idle "images/v14/iBuy/arrow_right.webp"
            action SetScreenVariable("car_images_index", car_images_index + 1)
            sensitive car_images_index < len(v14s47_car_pics) - 1
            yalign 0.5

    # Select Car Description
    add "images/v14/iBuy/descriptions_only.webp":
        xalign 0.5
        ypos 583

    if v14s48_car_description == CarDescription.LIE:
        add "images/v14/iBuy/lie_hover.webp" pos (233, 750)

    button:
        area (174, 650, 771, 208)
        action SetVariable("v14s48_car_description", CarDescription.LIE)

    button:
        area (945, 650, 786, 208)
        action SetVariable("v14s48_car_description", CarDescription.TRUTH) 

    if v14s48_car_description == CarDescription.TRUTH:
        add "images/v14/iBuy/truth_hover.webp" pos (1650, 750)

    # Determine Price
    bar:
        value VariableValue("v14s48_car_price", offset=100, range=700)
        pos (765, 870)
        maximum (800, 50)

    add "images/v14/iBuy/price_scale.webp":
        xalign 0.5
        ypos 868

    # Confirm
    imagebutton:
        idle "images/v14/iBuy/confirm.webp"
        action [Hide("iBuy"), Jump ("v14s48_end")]
        xalign 0.5
        ypos 973