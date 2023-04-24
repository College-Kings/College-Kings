screen v13s24_girl():

    if emmy.points != 3 and not kourtney.relationship >= Relationship.LIKES and not aryssa.relationship >= Relationship.LIKES:
        add Transform("images/v13/Scene 24/v13s24_20a.webp", blur=15)
    elif emmy.points == 3 and kourtney.relationship >= Relationship.LIKES and aryssa.relationship >= Relationship.LIKES:
        add Transform("images/v13/Scene 24/v13s24_20b.webp", blur=15)
    elif emmy.points == 3 and kourtney.relationship >= Relationship.LIKES:
        add Transform("images/v13/Scene 24/v13s24_20c.webp", blur=15)
    elif emmy.points == 3 and aryssa.relationship >= Relationship.LIKES:
        add Transform("images/v13/Scene 24/v13s24_20d.webp", blur=15)
    elif kourtney.relationship >= Relationship.LIKES and aryssa.relationship >= Relationship.LIKES:
        add Transform("images/v13/Scene 24/v13s24_20e.webp", blur=15)
    elif emmy.points == 3:
        add Transform("images/v13/Scene 24/v13s24_20f.webp", blur=15)
    elif kourtney.relationship >= Relationship.LIKES:
        add Transform("images/v13/Scene 24/v13s24_20g.webp", blur=15)
    elif aryssa.relationship >= Relationship.LIKES:
        add Transform("images/v13/Scene 24/v13s24_20h.webp", blur=15)

    hbox:
        align (0.5, 0.5)
        spacing 20

        button:
            if emmy.points == 3:
                action Jump("v13s24_emmy_date")

            fixed:
                xysize (269, 74)
                if emmy.points == 3:
                    add "gui/common/button_gray.webp"
                else:
                    add "gui/common/button_light_gray.webp"
                text "Emmy" align (0.5, 0.5)

        button:
            if kourtney.relationship >= Relationship.LIKES:
                action Jump("v13s24_kourtney_date")

            fixed:
                xysize (269, 74)
                if kourtney.relationship >= Relationship.LIKES:
                    add "gui/common/button_gray.webp"
                else:
                    add "gui/common/button_light_gray.webp"
                text "Kourtney" align (0.5, 0.5)

        button:
            if aryssa.relationship >= Relationship.LIKES:
                action Jump("v13s24_aryssa_date")

            fixed:
                xysize (269, 74)
                if aryssa.relationship >= Relationship.LIKES:
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

    if config_debug:
        python:
            actions = []

            if emmy.points == 3:
                actions.append(Jump("v13s24_emmy_date"))

            if kourtney.relationship >= Relationship.LIKES:
                actions.append(Jump("v13s24_kourtney_date"))

            if aryssa.relationship >= Relationship.LIKES:
                actions.append(Jump("v13s24_aryssa_date"))

            actions.append(Jump("v13s24_no_simplr_date"))

        timer 0.1 action renpy.random.choice(actions)
