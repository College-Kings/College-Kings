screen v12_girls:
    add "images/v7/homecomingchoice.webp"

    grid 4 2:
        spacing 40
        xalign 0.5
        ypos 285

        imagebutton:
            if "chloe" not in hcAsked and not chloemad:
                idle "images/v7/HCChloe.webp"
                hover "images/v7/HCChloe2.webp"
            else:
                idle "images/v7/HCChloe3.webp"
                hover "images/v7/HCChloe23.webp"
            
            if "chloe" in hcAsked and not (laurenrs or chloemad):
                action Jump("hc_asking_chloe")

        imagebutton:
            if "lauren" not in hcAsked:
                idle "images/v7/HCLauren.webp"
                hover "images/v7/HCLauren2.webp"
            else:
                idle "images/v7/HCLauren3.webp"
                hover "images/v7/HCLauren23.webp"

            if "lauren" not in hcAsked and laurenrs:
                action Jump("hc_asking_lauren")

        imagebutton:
            if "nora" not in hcAsked:
                idle "images/v7/nora.webp"
                hover "images/v7/nora.webp"
            else:
                idle "images/v7/nora.webp"
                hover "images/v7/nora.webp"

            if "nora" not in hcAsked and laurenrs:
                action Jump("hc_asking_nora")

        imagebutton:
            if "penelope" not in hcAsked:
                idle "images/v7/HCPenelope3.webp"
                hover "images/v7/HCPenelope23.webp"
            else:
                idle "images/v7/HCPenelope.webp"
                hover "images/v7/HCPenelope2.webp"

            if "penelope" not in hcAsked and not laurenrs:
                action Jump("hc_asking_penelope")

        imagebutton:
            if "Samantha" not in hcAsked:
                idle "images/v7/Samantha.webp"
                hover "images/v7/Samantha.webp"
            else:
                idle "images/v7/Samantha.webp"
                hover "images/v7/Samantha.webp"

            if "Samantha" not in hcAsked and laurenrs:
                action Jump("hc_asking_Samantha")

        imagebutton:
            if "Lindsey" not in hcAsked:
                idle "images/v7/Lindsey.webp"
                hover "images/v7/Lindsey.webp"
            else:
                idle "images/v7/Lindsey.webp"
                hover "images/v7/Lindsey.webp"

            if "Lindsey" not in hcAsked and laurenrs:
                action Jump("hc_asking_Lindsey")

        imagebutton:
            if "riley" not in hcAsked:
                idle "images/v7/HCRiley3.webp"
                hover "images/v7/HCRiley23.webp"
            else:
                idle "images/v7/HCRiley.webp"
                hover "images/v7/HCRiley2.webp"

            if "riley" not in hcAsked and not laurenrs:
                action Jump("hc_asking_riley")

        imagebutton:
            if "aubrey" not in hcAsked:
                idle "images/v7/HCAubrey.webp"
                hover "images/v7/HCAubrey2.webp"
            else:
                idle "images/v7/HCAubrey3.webp"
                hover "images/v7/HCAubrey23.webp"
            
            if "aubrey" not in hcAsked and not laurenrs:
                action Jump("hc_asking_aubrey")