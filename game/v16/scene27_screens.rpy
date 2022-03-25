screen v16s27_baby_schedule():
    tag free_roam
    modal True
    style_prefix "baby_schedule"

    default image_path = "images/v16/temp/Scene 27/baby-schedule/"
    default schedule_grid = [
        ["Wednesday Night", "Thursday Night", "Friday Night"],
        ["Date with Aubrey\n(optional)", "Polly's San Vallejo Acoustic Concert", "Ms. Rose opera\n(optional)"],
        [
            "I can definitely go to the date regardless of who has the baby, but if I want anything to happen afterwards, I better not be on baby duty for the night.",
            "I can go to the concert regardless of who has the baby, but I may have to go home early and miss whatever happens afterwards if i'm on baby duty.",
            "I can definitely go to the opera regardless of who has the baby, but if I want anything to happen afterwards, I better not be on baby duty for the night."
        ],
        ["Choose Baby Duty", "Choose Baby Duty", "Choose Baby Duty"]
    ]

    frame:
        background image_path + "background.png"
        xysize (1684, 868)
        align (0.5, 0.5)

        grid 3 4:
            pos (285, 10)
            xspacing -10
            yspacing -28

            for row in schedule_grid:
                for item in row:
                    if item == "Choose Baby Duty":
                        button:
                            idle_background image_path + "schedule-idle.png"
                            hover_background image_path + "schedule-hover.png"
                            action NullAction()
                            xysize (485, 208)

                            text item align (0.5, 0.5)

                    else:
                        frame:
                            background image_path + "schedule-idle.png"
                            xysize (485, 208)
                            padding (40, 40)

                            # add "#00ff0080"

                            text item align (0.5, 0.5)

style baby_schedule_text is text:
    font "fonts/Effra-Regular.ttf"
    size 23
    text_align 0.5