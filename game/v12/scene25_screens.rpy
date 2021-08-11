screen v12_girls():
    add "images/v7/homecomingchoice.webp"

    grid 3 3:
        spacing 40
        xalign 0.5
        ypos 285

        imagebutton:
            if True:
                idle "images/v7/HCAmber.webp"
                hover "images/v7/HCAmber2.webp"
                action Jump("v12_jc_amber")
            else:
                idle "images/v7/HCAmber3.webp"
                hover "images/v7/HCAmber23.webp"

        imagebutton:
            if True:
                idle "images/v7/HCAubrey.webp"
                hover "images/v7/HCAubrey2.webp"
                action Jump("v12_jc_aubrey")
            else:
                idle "images/v7/HCAubrey3.webp"
                hover "images/v7/HCAubrey23.webp"

        imagebutton:
            if not chloemad:
                idle "images/v7/HCChloe.webp"
                hover "images/v7/HCChloe2.webp"
                action Jump("v12_jc_chloe")

            else:
                idle "images/v7/HCChloe3.webp"
                hover "images/v7/HCChloe23.webp"
            
        imagebutton:
            if not laurenmad:
                idle "images/v7/HCLauren.webp"
                hover "images/v7/HCLauren2.webp"
                action Jump("v12_jc_lauren")
            else:
                idle "images/v7/HCLauren3.webp"
                hover "images/v7/HCLauren23.webp"

        imagebutton:
            if True:
                idle "images/v7/Lindsey.webp"
                hover "images/v7/Lindsey.webp"
                action Jump("v12_jc_lindsey")
            else:
                idle "images/v7/Lindsey.webp"
                hover "images/v7/Lindsey.webp"

        imagebutton:
            if True:
                idle "images/v7/nora.webp"
                hover "images/v7/nora.webp"
                action Jump("v12_jc_nora")
            else:
                idle "images/v7/nora.webp"
                hover "images/v7/nora.webp"

        imagebutton:
            if v11_pen_goes_europe:
                idle "images/v7/HCPenelope.webp"
                hover "images/v7/HCPenelope2.webp"
                action Jump("v12_jc_penelope")
            else:
                idle "images/v7/HCPenelope3.webp"
                hover "images/v7/HCPenelope23.webp"

        imagebutton:
            if True:
                idle "images/v7/HCRiley.webp"
                hover "images/v7/HCRiley2.webp"
                action Jump("v12_jc_riley")
            else:
                idle "images/v7/HCRiley3.webp"
                hover "images/v7/HCRiley23.webp"

        imagebutton:
            if v11_invite_sam_europe:
                idle "images/v7/Samantha.webp"
                hover "images/v7/Samantha.webp"
                action Jump("v12_jc_samantha")
            else:
                idle "images/v7/Samantha.webp"
                hover "images/v7/Samantha.webp"