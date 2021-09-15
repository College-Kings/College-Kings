screen v13s35_adult_shop():
    modal True

    add "#00f"

    vbox:
        align (0.5, 0.5)
        spacing 50

        hbox:
            spacing 50

            for i in (honey, butt_plug, spankers):
                button:
                    xysize (300, 300)
                    action Function(mc.add_item, i)
                    background "#fff"

                    vbox:
                        text i.name color "#000"
                        text str(i.cost) color "#000"

        hbox:
            xalign 0.5
            spacing 50

            for i in (cuffs, feather):
                button:
                    xysize (300, 300)
                    action Function(mc.add_item, i)
                    background "#fff"

                    vbox:
                        text i.name color "#000"
                        text str(i.cost) color "#000"