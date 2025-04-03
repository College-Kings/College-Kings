screen v12_girls():
    # character: label
    default girl_labels = {
        amber: {
            "label": "v12_jc_amber",
            "condition": True
        },
        aubrey: {
            "label": "v12_jc_aubrey",
            "condition": True
        },
        chloe: {
            "label": "v12_jc_chloe",
            "condition": not CharacterService.is_mad(chloe)
        },
        lauren: {
            "label": "v12_jc_lauren",
            "condition": not v11_lauren_caught_aubrey
        },
        lindsey: {
            "label": "v12_jc_lindsey",
            "condition": True
        },
        nora: {
            "label": "v12_jc_nora",
            "condition": True
        },
        penelope: {
            "label": "v12_jc_penelope",
            "condition": True
        },
        riley: {
            "label": "v12_jc_riley",
            "condition": True
        },
        samantha: {
            "label": "v12_jc_samantha",
            "condition": v11_invite_sam_europe
        }
    }

    add "images/v4/jc_background.webp"

    vpgrid:
        cols 4
        rows 3
        spacing 40
        xalign 0.5
        ypos 350
        allow_underfull True

        for girl_obj, i in girl_labels.items():
            button:
                background "girl_button_idle"
                hover_background "girl_button_hover"
                insensitive_background "girl_button_insensitive"
                sensitive i["condition"]
                xysize (307, 112)
                action Jump(i["label"])

                add Transform(girl_obj.profile_picture, xysize=(100, 100)) xpos 6 yalign 0.5
 
                vbox:
                    xpos 120
                    yalign 0.5
                    spacing -2

                    text girl_obj.name:
                        size 30
                        color "#FFF"

    if config_debug:
        timer 0.1 action Jump(renpy.random.choice([i["label"] for i in girl_labels.values()]))

