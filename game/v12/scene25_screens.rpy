screen v12_girls():

    default girlLabels = [
        ["Amber", "v12_jc_amber"],
        ["Aubrey", "v12_jc_aubrey"],
        ["Chloe", "v12_jc_chole"],
        ["Lauren", "v12_jc_lauren"],
        ["Lindsey", "v12_jc_lindsey"],
        ["Nora", "v12_jc_nora"],
        ["Penelope", "v12_jc_penelope"],
        ["Riley", "v12_jc_riley"],
        ["Samantha", "v12_jc_samantha"],
    ]

    default image_path = "gui/julia_call/"

    add image_path + "jc_background.webp"

    vpgrid:
        cols 4
        rows 3
        spacing 40
        xalign 0.5
        ypos 350

        for i in girlLabels:
            vbox:
                align (0.5, 0.5)

                if i[0] == "Chloe":
                    imagebutton:
                        if chloe.relationship > Relationship.MAD:
                            idle image_path + i[0] + "_idle.webp"
                            hover image_path + i[0] + ".webp"
                            action Jump(i[1])
                        else:
                            idle image_path + i[0] + "_grey.webp"
                            hover image_path + i[0] + "_grey.webp"
                elif not v11_lauren_caught_aubrey:
                    if not v11_lauren_caught_aubrey:
                        imagebutton:
                            idle image_path + i[0] + "_idle.webp"
                            hover image_path + i[0] + ".webp"
                            action Jump(i[1])
                    else:
                        imagebutton:
                            idle image_path + i[0] + "_grey.webp"
                            hover image_path + i[0] + "_grey.webp"

                elif v11_invite_sam_europe:
                    if v11_invite_sam_europe:
                        imagebutton:
                            idle image_path + i[0] + "_idle.webp"
                            hover image_path + i[0] + ".webp"
                            action Jump(i[1])
                    else:
                        imagebutton:
                            idle image_path + i[0] + "_grey.webp"
                            hover image_path + i[0] + "_grey.webp"
                else:
                    imagebutton:
                        idle image_path + i[0] + "_idle.webp"
                        hover image_path + i[0] + ".webp"
                        action Jump(i[1])

                text i[0]:
                    yoffset -80
                    xoffset 30
                    xalign 0.5
                    size 30