init python:
    class BabyDuty(Enum):
        ALONE = "Baby Duty alone"
        WITH_PARTNER = "Baby Duty with Partner"
        PARTNER_ALONE = "Parter has Baby Duty alone"
        NULL = ""


screen v16s27_baby_schedule():
    style_prefix "baby_schedule"

    default image_path = "images/v16/Scene 27/baby-schedule/"
    default schedule_grid = [
        ["Wednesday Night", "Thursday Night", "Friday Night"],
        ["Date with Aubrey\n(optional)", "Polly's San Vallejo Acoustic Concert", "Ms. Rose opera\n(optional)"],
        [
            "I can definitely go to the date regardless of who has the baby, but if I want anything to happen afterwards, I better not be on baby duty for the night.",
            "I can go to the concert regardless of who has the baby, but I may have to go home early and miss whatever happens afterwards if i'm on baby duty.",
            "I can definitely go to the opera regardless of who has the baby, but if I want anything to happen afterwards, I better not be on baby duty for the night."
        ]
    ]

    frame:
        background image_path + "schedule-background.webp"
        xysize (1732, 973)
        align (0.5, 0.5)
        yoffset -25

        vpgrid:
            cols 3
            pos (285, 70)
            xspacing -10
            yspacing -28

            for row in schedule_grid:
                for item in row:
                    frame:
                        background image_path + "frame-background.webp"
                        xysize (485, 208)
                        padding (40, 40)

                        text item align (0.5, 0.5)

            for i in ("wednesday", "thursday", "friday"):
                frame:
                    background image_path + "frame-background.webp"
                    xysize (485, 208)
                    padding (40, 40)

                    text v16s27_mc_baby_schedule[i].value align (0.5, 0.5)     

style baby_schedule_text is text:
    font "fonts/Effra-Regular.ttf"
    size 23
    text_align 0.5


label v16s27_baby_schedule:
    show screen v16s27_baby_schedule

    $ v16s27_mc_baby_schedule["wednesday"] = BabyDuty.NULL
    $ v16s27_mc_baby_schedule["thursday"] = BabyDuty.NULL
    $ v16s27_mc_baby_schedule["friday"] = BabyDuty.NULL

    "Which night do you want to share the baby with your Partner?"

    menu:
        "Wednesday":
            $ v16s27_mc_baby_schedule["wednesday"] = BabyDuty.WITH_PARTNER

        "Thursday":
            $ v16s27_mc_baby_schedule["thursday"] = BabyDuty.WITH_PARTNER

        "Friday":
            $ v16s27_mc_baby_schedule["friday"] = BabyDuty.WITH_PARTNER

    "Which night do you want the baby alone?"

    menu:
        "Wednesday" if v16s27_mc_baby_schedule["wednesday"] != BabyDuty.WITH_PARTNER:
            $ v16s27_mc_baby_schedule["wednesday"] = BabyDuty.ALONE

            if v16s27_mc_baby_schedule["thursday"] == BabyDuty.WITH_PARTNER:
                $ v16s27_mc_baby_schedule["friday"] = BabyDuty.PARTNER_ALONE
            else:
                $ v16s27_mc_baby_schedule["thursday"] = BabyDuty.PARTNER_ALONE

        "Thursday" if v16s27_mc_baby_schedule["thursday"] != BabyDuty.WITH_PARTNER:
            $ v16s27_mc_baby_schedule["thursday"] = BabyDuty.ALONE
            
            if v16s27_mc_baby_schedule["wednesday"] == BabyDuty.WITH_PARTNER:
                $ v16s27_mc_baby_schedule["friday"] = BabyDuty.PARTNER_ALONE
            else:
                $ v16s27_mc_baby_schedule["wednesday"] = BabyDuty.PARTNER_ALONE

        "Friday" if v16s27_mc_baby_schedule["friday"] != BabyDuty.WITH_PARTNER:
            $ v16s27_mc_baby_schedule["friday"] = BabyDuty.ALONE
            
            if v16s27_mc_baby_schedule["thursday"] == BabyDuty.WITH_PARTNER:
                $ v16s27_mc_baby_schedule["wednesday"] = BabyDuty.PARTNER_ALONE
            else:
                $ v16s27_mc_baby_schedule["thursday"] = BabyDuty.PARTNER_ALONE

    pause

    hide screen v16s27_baby_schedule

    return

