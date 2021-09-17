screen v13s24_girl():
    add im.Blur("images/v13/scene24/v13s24_12a.webp", 5)

    hbox:
        align (0.5, 0.5)
        spacing 20

        button:
            if emmyrs:
                action Jump("v13s24_emmy_date")

            fixed:
                xysize (269, 74)
                if emmyrs:
                    add "images/button_gray.webp"
                else:
                    add "images/button_light_gray.webp"
                text "Emmy" align (0.5, 0.5)

        button:
            if kourtneyrs:
                action Jump("v13s24_kourtney_date")

            fixed:
                xysize (269, 74)
                if kourtneyrs:
                    add "images/button_gray.webp"
                else:
                    add "images/button_light_gray.webp"
                text "Kourtney" align (0.5, 0.5)

        button:
            if aryssars:
                action Jump("v13s24_aryssa_date")

            fixed:
                xysize (269, 74)
                if aryssars:
                    add "images/button_gray.webp"
                else:
                    add "images/button_light_gray.webp"
                text "Aryssa" align (0.5, 0.5)

        button:
            action Jump("v13s24_no_simplr_date")

            fixed:
                xysize (269, 74)
                add "images/button_gray.webp"
                text "No Date" align (0.5, 0.5)