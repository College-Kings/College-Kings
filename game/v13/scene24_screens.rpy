screen v13s24_girl():

    if not emmyrs and not kourtney.relationship == Relationship.LIKES and not aryssa.relationship == Relationship.LIKES:
        add Transform("images/v13/scene24/v13s24_20a.webp", blur=15)
    elif emmyrs and kourtney.relationship == Relationship.LIKES and aryssa.relationship == Relationship.LIKES:
        add Transform("images/v13/scene24/v13s24_20b.webp", blur=15)
    elif emmyrs and kourtney.relationship == Relationship.LIKES:
        add Transform("images/v13/scene24/v13s24_20c.webp", blur=15)
    elif emmyrs and aryssa.relationship == Relationship.LIKES:
        add Transform("images/v13/scene24/v13s24_20d.webp", blur=15)
    elif kourtney.relationship == Relationship.LIKES and aryssa.relationship == Relationship.LIKES:
        add Transform("images/v13/scene24/v13s24_20e.webp", blur=15)
    elif emmyrs:
        add Transform("images/v13/scene24/v13s24_20f.webp", blur=15)
    elif kourtney.relationship == Relationship.LIKES:
        add Transform("images/v13/scene24/v13s24_20g.webp", blur=15)
    elif aryssa.relationship == Relationship.LIKES:
        add Transform("images/v13/scene24/v13s24_20h.webp", blur=15)

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
            if kourtney.relationship == Relationship.LIKES:
                action Jump("v13s24_kourtney_date")

            fixed:
                xysize (269, 74)
                if kourtney.relationship == Relationship.LIKES:
                    add "images/button_gray.webp"
                else:
                    add "images/button_light_gray.webp"
                text "Kourtney" align (0.5, 0.5)

        button:
            if aryssa.relationship == Relationship.LIKES:
                action Jump("v13s24_aryssa_date")

            fixed:
                xysize (269, 74)
                if aryssa.relationship == Relationship.LIKES:
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