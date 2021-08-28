screen v12_girls():
    add "images/v12/Scene 25/juliabackground.webp"

    grid 3 3:
        spacing 50
        xalign 0.5
        ypos 250

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
            if not (laurenrs and v11_aubrey_sex):
                idle "images/v7/HCLauren.webp"
                hover "images/v7/HCLauren2.webp"
                action Jump("v12_jc_lauren")
            else:
                idle "images/v7/HCLauren3.webp"
                hover "images/v7/HCLauren23.webp"

        imagebutton:
            if True:
                idle "images/head shots/Lindsey1.webp"
                hover "images/head shots/Lindsey2.webp"
                action Jump("v12_jc_lindsey")
            else:
                idle "images/head shots/Lindsey1.webp"
                hover "images/head shots/Lindsey2.webp"

        imagebutton:
            if True:
                idle "images/head shots/Nora1.webp"
                hover "images/head shots/Nora2.webp"
                action Jump("v12_jc_nora")
            else:
                idle "images/head shots/Nora1.webp"
                hover "images/head shots/Nora2.webp"

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
                idle "images/head shots/Samantha1.webp"
                hover "images/head shots/Samantha2.webp"
                action Jump("v12_jc_samantha")
            else:
                idle "images/head shots/Samantha3.webp"
                hover "images/head shots/Samantha3.webp"