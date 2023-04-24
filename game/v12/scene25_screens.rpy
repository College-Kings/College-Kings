screen v12_girls():

    # character: label
    default girl_labels = {
        "Amber": {
            "label": "v12_jc_amber",
            "condition": True
        },
        "Aubrey": {
            "label": "v12_jc_aubrey",
            "condition": True
        },
        "Chloe": {
            "label": "v12_jc_chloe",
            "condition": not CharacterService.is_mad(chloe)
        },
        "Lauren": {
            "label": "v12_jc_lauren",
            "condition": not v11_lauren_caught_aubrey
        },
        "Lindsey": {
            "label": "v12_jc_lindsey",
            "condition": True
        },
        "Nora": {
            "label": "v12_jc_nora",
            "condition": True
        },
        "Penelope": {
            "label": "v12_jc_penelope",
            "condition": True
        },
        "Riley": {
            "label": "v12_jc_riley",
            "condition": True
        },
        "Samantha": {
            "label": "v12_jc_samantha",
            "condition": v11_invite_sam_europe
        }
    }

    default image_path = "gui/julia_call/"

    add image_path + "jc_background.webp"

    vpgrid:
        cols 4
        rows 3
        spacing 40
        xalign 0.5
        ypos 350
        allow_underfull True

        for character, i in girl_labels.items():
            vbox:
                align (0.5, 0.5)

                imagebutton:
                    idle image_path  + "{}_idle.webp".format(character)
                    hover image_path + "{}.webp".format(character)
                    insensitive image_path + "{}_grey.webp".format(character)
                    sensitive i["condition"]
                    action Jump(i["label"])

                text character:
                    yoffset -80
                    xoffset 30
                    xalign 0.5
                    size 30

    if config_debug:
        timer 0.1 action Jump(renpy.random.choice([i["label"] for i in girl_labels.values()]))
