screen v12_girls():
    add "images/v12/Scene 25/juliabackground.webp"

    grid 3 3:
        spacing 50
        xalign 0.5
        ypos 250

        imagebutton:
            idle "images/v7/HCAmber.webp"
            hover "images/v7/HCAmber2.webp"
            action Jump("v12_jc_amber")

        imagebutton:
            idle "images/v7/HCAubrey.webp"
            hover "images/v7/HCAubrey2.webp"
            action Jump("v12_jc_aubrey")

        imagebutton:
            if chloe.relationship > Relationship.MAD:
                idle "images/v7/HCChloe.webp"
                hover "images/v7/HCChloe2.webp"
                action Jump("v12_jc_chloe")

            else:
                idle "images/v7/HCChloe3.webp"
                hover "images/v7/HCChloe23.webp"
            
        imagebutton:
            if not v11_lauren_caught_aubrey:
                idle "images/v7/HCLauren.webp"
                hover "images/v7/HCLauren2.webp"
                action Jump("v12_jc_lauren")
            else:
                idle "images/v7/HCLauren3.webp"
                hover "images/v7/HCLauren23.webp"

        imagebutton:
            idle "images/head shots/Lindsey1.webp"
            hover "images/head shots/Lindsey2.webp"
            action Jump("v12_jc_lindsey")

        imagebutton:
            idle "images/head shots/Nora1.webp"
            hover "images/head shots/Nora2.webp"
            action Jump("v12_jc_nora")

        imagebutton:
            idle "images/v7/HCPenelope.webp"
            hover "images/v7/HCPenelope2.webp"
            action Jump("v12_jc_penelope")

        imagebutton:
            idle "images/v7/HCRiley.webp"
            hover "images/v7/HCRiley2.webp"
            action Jump("v12_jc_riley")

        imagebutton:
            if v11_invite_sam_europe:
                idle "images/head shots/Samantha1.webp"
                hover "images/head shots/Samantha2.webp"
                action Jump("v12_jc_samantha")
            else:
                idle "images/head shots/Samantha3.webp"
                hover "images/head shots/Samantha3.webp"