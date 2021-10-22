screen v13s24_girl():

    if not emmyrs and not kourtneyrs and not aryssars:
        add im.Blur("images/v13/scene24/v13s24_20a.webp", 5)
    elif emmyrs and kourtneyrs and aryssars:
        add im.Blur("images/v13/scene24/v13s24_20b.webp", 5)
    elif emmyrs and kourtneyrs:
        add im.Blur("images/v13/scene24/v13s24_20c.webp", 5)
    elif emmyrs and aryssars:
        add im.Blur("images/v13/scene24/v13s24_20d.webp", 5)
    elif kourtneyrs and aryssars:
        add im.Blur("images/v13/scene24/v13s24_20e.webp", 5)
    elif emmyrs:
        add im.Blur("images/v13/scene24/v13s24_20f.webp", 5)
    elif kourtneyrs:
        add im.Blur("images/v13/scene24/v13s24_20g.webp", 5)
    elif aryssars:
        add im.Blur("images/v13/scene24/v13s24_20h.webp", 5)

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