screen v13s24_girl():

    if not emmy.relationship.value >= Relationship.LIKES.value and not kourtney.relationship.value >= Relationship.LIKES.value and not aryssa.relationship.value >= Relationship.LIKES.value:
        add Transform("images/v13/Scene 24/v13s24_20a.webp", blur=15)
    elif emmy.relationship.value >= Relationship.LIKES.value and kourtney.relationship.value >= Relationship.LIKES.value and aryssa.relationship.value >= Relationship.LIKES.value:
        add Transform("images/v13/Scene 24/v13s24_20b.webp", blur=15)
    elif emmy.relationship.value >= Relationship.LIKES.value and kourtney.relationship.value >= Relationship.LIKES.value:
        add Transform("images/v13/Scene 24/v13s24_20c.webp", blur=15)
    elif emmy.relationship.value >= Relationship.LIKES.value and aryssa.relationship.value >= Relationship.LIKES.value:
        add Transform("images/v13/Scene 24/v13s24_20d.webp", blur=15)
    elif kourtney.relationship.value >= Relationship.LIKES.value and aryssa.relationship.value >= Relationship.LIKES.value:
        add Transform("images/v13/Scene 24/v13s24_20e.webp", blur=15)
    elif emmy.relationship.value >= Relationship.LIKES.value:
        add Transform("images/v13/Scene 24/v13s24_20f.webp", blur=15)
    elif kourtney.relationship.value >= Relationship.LIKES.value:
        add Transform("images/v13/Scene 24/v13s24_20g.webp", blur=15)
    elif aryssa.relationship.value >= Relationship.LIKES.value:
        add Transform("images/v13/Scene 24/v13s24_20h.webp", blur=15)

    hbox:
        align (0.5, 0.5)
        spacing 20

        button:
            if emmy.relationship.value >= Relationship.LIKES.value:
                action Jump("v13s24_emmy_date")

            fixed:
                xysize (269, 74)
                if emmy.relationship.value >= Relationship.LIKES.value:
                    add "gui/common/button_gray.webp"
                else:
                    add "gui/common/button_light_gray.webp"
                text "Emmy" align (0.5, 0.5)

        button:
            if kourtney.relationship.value >= Relationship.LIKES.value:
                action Jump("v13s24_kourtney_date")

            fixed:
                xysize (269, 74)
                if kourtney.relationship.value >= Relationship.LIKES.value:
                    add "gui/common/button_gray.webp"
                else:
                    add "gui/common/button_light_gray.webp"
                text "Kourtney" align (0.5, 0.5)

        button:
            if aryssa.relationship.value >= Relationship.LIKES.value:
                action Jump("v13s24_aryssa_date")

            fixed:
                xysize (269, 74)
                if aryssa.relationship.value >= Relationship.LIKES.value:
                    add "gui/common/button_gray.webp"
                else:
                    add "gui/common/button_light_gray.webp"
                text "Aryssa" align (0.5, 0.5)

        button:
            action Jump("v13s24_no_simplr_date")

            fixed:
                xysize (269, 74)
                add "gui/common/button_gray.webp"
                text "No Date" align (0.5, 0.5)