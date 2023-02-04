screen path_builder_alert():
    modal True
    style_prefix "path_builder_alert"

    default image_path = "main_menu/path_builder/images/"

    add "darker_80"

    add image_path + "alert_background.webp" align (0.5, 0.5)

    fixed:
        xysize (742, 356)
        pos (587, 364)

        text "THE PATH BUILDER CONTAINS SPOILERS FOR THE STORY\nOF THE GAME. ARE YOU SURE YOU WANT TO CONTINUE?":
            xsize 572
            xalign 0.5
            ypos 66
            text_align 0.5


        hbox:
            pos (217, 258)
            spacing 5

            fixed:
                xysize (132, 61)

                imagebutton:
                    idle "path_builder_button_idle"
                    hover "path_builder_button_hover"
                    action [Hide("path_builder_alert"), Function(setup), Show("path_builder", from_main_menu=True)]
                text "YES" align (0.5, 0.5)

            fixed:
                xysize (132, 61)

                imagebutton:
                    idle "path_builder_button_idle"
                    hover "path_builder_button_hover"
                    action Hide("path_builder_alert")
                text "NO" align (0.5, 0.5)


style path_builder_alert_text is bebas_neue_30

screen path_builder(from_main_menu):
    tag menu

    modal True
    style_prefix "path_builder"

    default image_path = "main_menu/path_builder/images/"
    default grid_size = { # item_count : (rows, cols)
        0: (0, 0),
        1: (1, 1),
        2: (2, 1),
        3: (3, 1),
        4: (4, 1),
        6: (4, 2),
        11: (4, 3),
        12: (4, 3),
        14: (4, 4),
    }
    
    default category_step = 1
    default start_label = ""

    $ category = PathBuilderCategory.categories[category_step - 1]
    $ items = [item for item in PathBuilderItem.items if item.category == category]

    $ cols, rows = grid_size[len(items)]

    add image_path + "path_builder_background.webp"
    add image_path + "path_builder_box_background.webp" align (0.5, 0.5)

    vbox:
        align (0.95,0.05)

        imagebutton:
            idle image_path + "button_idle.webp"
            hover image_path + "button_hover.webp"
            selected_idle image_path + "button_hover.webp"
            action Show("path_builder_advanced_settings")

        text "Advanced":
            align (0.5, 0.5)
            yoffset -50
            color "#FFF"

    imagebutton:
        idle "gui/common/return_idle.webp"
        hover "gui/common/return_hover.webp"
        action [Hide("path_builder"), ShowMenu("main_menu")]
        align (0.015, 0.015)
    
    vbox:
        align (0.5, 0.215)

        add category.background_image

    vbox:
        spacing 20
        align (0.5, 0.5)

        text category.title xalign 0.5

        vpgrid:
            cols cols
            rows rows
            xspacing 10
            xalign 0.5
            yoffset 40
            allow_underfull True

            for item in items:
                if category == PBC_GIRL or category == PBC_HOMECOMING_DATE:
                    button:
                        idle_background image_path + "girls/{}_idle.webp".format(item.name)
                        hover_background image_path + "girls/{}.webp".format(item.name)
                        selected_idle_background image_path + "girls/{}.webp".format(item.name)
                        insensitive_background Transform(image_path + "girls/{}_idle.webp".format(item.name), matrixcolor=SaturationMatrix(0))
                        xysize (307, 112)
                        if category == PBC_GIRL and item.girl.relationship == item.relationships[-1]:
                            action SetField(item.girl, "relationship", item.relationships[0])
                        elif category == PBC_GIRL:
                            action SetField(item.girl, "relationship", item.relationships[item.relationships.index(item.girl.relationship) + 1])
                        else:
                            action item.actions
                        vbox:
                            xpos 120
                            yalign 0.5
                            spacing -2

                            text item.name:
                                size 30
                                color "#FFF"

                            if category == PBC_GIRL:
                                text item.girl.relationship.name:
                                    size 24
                                    color "#FFD166"

                                if pb_reputation_shown:
                                    text item.reputation: # This could show the reputation for each girl
                                        size 15
                                        color "#FFD166"


                        
                elif category == PBC_START_LOCATION:
                    vbox:
                        xalign 0.5

                        default start_image_path = image_path + "starts/"

                        imagebutton:
                            idle Transform(start_image_path + item.name +".webp", zoom=.8)
                            selected all([a.get_selected() for a in item.actions])
                            action [a for a in item.actions]
                            xalign 0.5

                        imagebutton:
                            idle image_path + "button_idle_dark.webp"
                            hover image_path + "button_hover.webp"
                            selected_idle image_path + "button_hover.webp"
                            selected all([a.get_selected() for a in item.actions])
                            action [a for a in item.actions]
                            xalign 0.5
                            yoffset -35

                        text item.name:
                            align (0.5, 0.5)
                            yoffset -87
                            size 30
                            color "#FFF"

                else:
                    vbox:
                        xalign 0.5

                        imagebutton:
                            idle image_path + "button_idle.webp"
                            hover image_path + "button_hover.webp"
                            selected_idle image_path + "button_hover.webp"
                            selected all([a.get_selected() for a in item.actions])
                            action [a for a in item.actions]

                        text item.name:
                            align (0.5, 0.5)
                            yoffset -50
                            color "#FFF"

        # Option to lock reputation
        if category == PBC_REPUTATION:
            hbox:
                spacing 20
                yoffset 40
                
                imagebutton:
                    idle image_path + "pb_tick.webp"
                    hover image_path + "pb_ticked.webp"
                    selected_idle image_path + "pb_ticked.webp"
                    action ToggleVariable("locked_reputation")

                text "Lock Reputation (Prevent it from changing)":
                    yoffset -7

    if category == PBC_START_LOCATION:
        frame:
            xalign 0.5
            ypos 750

            if start_label == "v1_start":
                text "ACHIEVEMENTS ARE EARNABLE"
            elif start_label:
                text "ACHIEVEMENTS ARE NOT EARNABLE FROM THIS START"

    hbox: 
        spacing 50
        align (0.5, 0.9)

        default button_img_path = "main_menu/path_builder/images/"

        if category_step > 1:

            imagebutton:
                idle button_img_path + "back.webp"
                action SetScreenVariable("category_step", category_step - 1)
        else:
            imagebutton:
                idle button_img_path + "back_blocked.webp"
                action ShowMenu("main_menu")


        imagebutton:
            idle button_img_path + "continue.webp"
            insensitive Transform(button_img_path + "continue.webp", matrixcolor=SaturationMatrix(0))
            sensitive (any(all([a.get_selected() for a in item.actions]) for item in items) or (category_step > 3))

            if category_step >= len(PathBuilderCategory.categories):
                if from_main_menu:
                    action [Show("phone_icon"), Function(setup), Start(start_label)]
                else:
                    action [Show("phone_icon"), Function(setup), Hide("path_builder"), Jump(start_label)]
            else:
                action SetScreenVariable("category_step", category_step + 1)


style path_builder_text is bebas_neue_30


screen path_builder_advanced_settings():
    zorder 100
    modal True

    default image_path = "main_menu/path_builder/images/"

    add image_path + "path_builder_background.webp"

    text "Advanced Settings" align (0.5, 0.15)

    imagebutton:
        idle "gui/common/return_idle.webp"
        hover "gui/common/return_hover.webp"
        action Hide("path_builder_advanced_settings")
        align (0.015, 0.015)
        

    hbox: 
        align (0.5, 0.5)
        spacing 100
        vbox:
            spacing 20

            text "Extras" color "#FFD166" size 50

            hbox:
                spacing 20
                
                imagebutton:
                    idle image_path + "pb_tick.webp"
                    hover image_path + "pb_ticked.webp"
                    selected_idle image_path + "pb_ticked.webp"
                    action ToggleVariable("emily_europe")

                text _("Invite Emily to Europe"):
                    yoffset -7

            hbox:
                spacing 20
                
                imagebutton:
                    idle image_path + "pb_tick.webp"
                    hover image_path + "pb_ticked.webp"
                    selected_idle image_path + "pb_ticked.webp"
                    action ToggleField(lauren, "relationship", Relationship.KISS, Relationship.FRIEND)

                text _("Kissed Lauren"):
                    yoffset -7

        vbox:
            spacing 20

            text _("Gameplay Changes") color "#FFD166" size 50

            hbox:
                spacing 20
                
                imagebutton:
                    idle image_path + "pb_tick.webp"
                    hover image_path + "pb_ticked.webp"
                    selected_idle image_path + "pb_ticked.webp"
                    action ToggleVariable("pb_reputation_shown")

                text _("Show preferred KCT for each girl"):
                    yoffset -7

            hbox:
                spacing 20
                
                imagebutton:
                    idle image_path + "pb_tick.webp"
                    hover image_path + "pb_ticked.webp"
                    selected_idle image_path + "pb_ticked.webp"
                    action ToggleVariable("pb_reputation_notification")

                text _("Show a notification whenever you gain KCT points"):
                    yoffset -7
    

style path_builder_advanced_settings_text is bebas_neue_30
