screen youattack2():

    if adamstance == 1:
        image "images/v5/afstancejab.webp"

        key q:
            action Jump ("adamjab1")
        key w:
            action Jump ("adamhook2")
        key e:
            action Jump ("adambody2")
        key r:
            action Jump ("adamkick2")

        imagebutton:
            idle "images/jab.webp"
            hover "images/jab.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("adamjab1")

        imagebutton:
            idle "images/hook.webp"
            hover "images/hook.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("adamhook2")

        imagebutton:
            idle "images/body.webp"
            hover "images/body.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("adambody2")

        imagebutton:
            idle "images/kick.webp"
            hover "images/kick.webp"
            xalign 0.115
            yalign 0.61
            action Jump ("adamkick2")

        timer reactiona action Jump("adamattack")

    if adamstance == 2:
        image "images/v5/afstancehook.webp"

        key q:
            action Jump ("adamjab2")
        key w:
            action Jump ("adamhook1")
        key e:
            action Jump ("adambody2")
        key r:
            action Jump ("adamkick2")

        imagebutton:
            idle "images/jab.webp"
            hover "images/jab.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("adamjab2")

        imagebutton:
            idle "images/hook.webp"
            hover "images/hook.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("adamhook1")

        imagebutton:
            idle "images/body.webp"
            hover "images/body.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("adambody2")

        imagebutton:
            idle "images/kick.webp"
            hover "images/kick.webp"
            xalign 0.115
            yalign 0.61
            action Jump ("adamkick2")

        timer reactiona action Jump("adamattack")

    if adamstance == 3:
        image "images/v5/afstancebody.webp"

        key q:
            action Jump ("adamjab2")
        key w:
            action Jump ("adamhook2")
        key e:
            action Jump ("adambody1")
        key r:
            action Jump ("adamkick2")

        imagebutton:
            idle "images/jab.webp"
            hover "images/jab.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("adamjab2")

        imagebutton:
            idle "images/hook.webp"
            hover "images/hook.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("adamhook2")

        imagebutton:
            idle "images/body.webp"
            hover "images/body.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("adambody1")

        imagebutton:
            idle "images/kick.webp"
            hover "images/kick.webp"
            xalign 0.115
            yalign 0.61
            action Jump ("adamkick2")

        timer reactiona action Jump("adamattack")

    if adamstance == 4:
        image "images/v5/afstancekick.webp"

        key q:
            action Jump ("adamjab2")
        key w:
            action Jump ("adamhook2")
        key e:
            action Jump ("adambody2")
        key r:
            action Jump ("adamkick1")

        imagebutton:
            idle "images/jab.webp"
            hover "images/jab.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("adamjab2")

        imagebutton:
            idle "images/hook.webp"
            hover "images/hook.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("adamhook2")

        imagebutton:
            idle "images/body.webp"
            hover "images/body.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("adambody2")

        imagebutton:
            idle "images/kick.webp"
            hover "images/kick.webp"
            xalign 0.115
            yalign 0.61
            action Jump ("adamkick1")

        timer reactiona action Jump("adamattack")

    if config_debug:
        python:
            labels = []

            if adamstance == 1:
                labels.append("adamjab1")
                labels.append("adamhook2")
                labels.append("adambody2")
                labels.append("adamkick2")

            if adamstance == 2:
                labels.append("adamjab2")
                labels.append("adamhook1")
                labels.append("adambody2")
                labels.append("adamkick2")

            if adamstance == 3:
                labels.append("adamjab2")
                labels.append("adamhook2")
                labels.append("adambody1")
                labels.append("adamkick2")

            if adamstance == 4:
                labels.append("adamjab2")
                labels.append("adamhook2")
                labels.append("adambody2")
                labels.append("adamkick1")

        timer 0.1 action Jump(renpy.random.choice(labels))

    use fight_overlay # TODO: Update fight code


screen adamattack():
    if adamattack == 1:
        image "images/v5/af13pic.webp"

        key q:
            action Jump ("adamhookblocked")
        key w:
            action Jump ("adamhookhit")
        key e:
            action Jump ("adamhookhit")
        key r:
            action Jump ("adamhookhit")

        imagebutton:
            idle "images/hookblock.webp"
            hover "images/hookblock.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("adamhookblocked")

        imagebutton:
            idle "images/jabblock.webp"
            hover "images/jabblock.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("adamhookhit")

        imagebutton:
            idle "images/bodyblock.webp"
            hover "images/bodyblock.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("adamhookhit")

        imagebutton:
            idle "images/kickblock.webp"
            hover "images/kickblock.webp"
            xalign 0.115
            yalign 0.6
            action Jump ("adamhookhit")

        timer reaction action Jump("adamhookhit")

    if adamattack == 2:
        image "images/v5/af14pic.webp"

        key q:
            action Jump ("adamjabhit")
        key w:
            action Jump ("adamjabblocked")
        key e:
            action Jump ("adamjabhit")
        key r:
            action Jump ("adamjabhit")

        imagebutton:
            idle "images/hookblock.webp"
            hover "images/hookblock.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("adamjabhit")

        imagebutton:
            idle "images/jabblock.webp"
            hover "images/jabblock.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("adamjabblocked")

        imagebutton:
            idle "images/bodyblock.webp"
            hover "images/bodyblock.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("adamjabhit")

        imagebutton:
            idle "images/kickblock.webp"
            hover "images/kickblock.webp"
            xalign 0.115
            yalign 0.6
            action Jump ("adamjabhit")

        timer reaction action Jump("adamjabhit")

    if adamattack == 3:
        image "images/v5/af15pic.webp"

        key q:
            action Jump ("adambodyhit")
        key w:
            action Jump ("adambodyhit")
        key e:
            action Jump ("adambodyblocked")
        key r:
            action Jump ("adambodyhit")

        imagebutton:
            idle "images/hookblock.webp"
            hover "images/hookblock.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("adambodyhit")

        imagebutton:
            idle "images/jabblock.webp"
            hover "images/jabblock.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("adambodyhit")

        imagebutton:
            idle "images/bodyblock.webp"
            hover "images/bodyblock.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("adambodyblocked")

        imagebutton:
            idle "images/kickblock.webp"
            hover "images/kickblock.webp"
            xalign 0.115
            yalign 0.6
            action Jump ("adambodyhit")

        timer reaction action Jump("adambodyhit")

    if adamattack == 4:
        image "images/v5/af16pic.webp"

        key q:
            action Jump ("adamkickhit")
        key w:
            action Jump ("adamkickhit")
        key e:
            action Jump ("adamkickhit")
        key r:
            action Jump ("adamkickblocked")

        timer reaction action Jump("adamkickhit")

        imagebutton:
            idle "images/hookblock.webp"
            hover "images/hookblock.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("adamkickhit")

        imagebutton:
            idle "images/jabblock.webp"
            hover "images/jabblock.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("adamkickhit")

        imagebutton:
            idle "images/bodyblock.webp"
            hover "images/bodyblock.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("adamkickhit")

        imagebutton:
            idle "images/kickblock.webp"
            hover "images/kickblock.webp"
            xalign 0.115
            yalign 0.6
            action Jump ("adamkickblocked")

    if config_debug:
        python:
            labels = []

            if adamattack == 1:
                labels.append("adamhookblocked")
                labels.append("adamhookhit")
                labels.append("adamhookhit")
                labels.append("adamhookhit")

            if adamattack == 2:
                labels.append("adamjabhit")
                labels.append("adamjabblocked")
                labels.append("adamjabhit")
                labels.append("adamjabhit")

            if adamattack == 3:
                labels.append("adambodyhit")
                labels.append("adambodyhit")
                labels.append("adambodyblocked")
                labels.append("adambodyhit")

            if adamattack == 4:
                labels.append("adamkickhit")
                labels.append("adamkickhit")
                labels.append("adamkickhit")
                labels.append("adamkickblocked")

        timer 0.1 action Jump(renpy.random.choice(labels))

    use fight_overlay # TODO: Update fight code


screen trolleyProblem(option1, option2):
    add "images/v5/trolleylever.webp"

    imagebutton:
        idle "images/v5/leverno.webp"
        hover "images/v5/lever.webp"
        pos (125, 150)
        action Jump(option2)

    timer 3 action Jump(option1)
    use timer_bar

    if config_debug:
        timer 0.1 action Jump(renpy.random.choice((option1, option2)))