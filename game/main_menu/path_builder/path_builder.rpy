init python:
    class PathBuilderCatagories(Enum):
        FRATERNITY = {
            1: "Pick a fraternity",
            "background": "main_menu/path_builder/images/path_builder_step_1.webp"
        }
        KCT = {
            2: "Pick your starting KCT",
            "background": "main_menu/path_builder/images/path_builder_step_2.webp"
        }
        GIRL = {
            3: "Pick which girls you want to be romantically involved with",
            "background": "main_menu/path_builder/images/path_builder_step_3.webp"
        }
        START_LOCATION = {
            4: "Pick your starting location",
            "background": "main_menu/path_builder/images/path_builder_step_4.webp"
        }
        HOMECOMING_DATE = {
            5: "Pick your homecoming date",
            "background": "main_menu/path_builder/images/path_builder_step_5.webp"
        }     

    class PathBuilderItem:
        items = []

        def __init__(self, catagory, name, actions=None):
            self.catagory = catagory
            self.name = name

            if actions is None: self.actions = []
            elif isinstance(actions, list): self.actions = actions
            else: self.actions = [actions]

            PathBuilderItem.items.append(self)


    def get_catagory(step):
        for catagory in PathBuilderCatagories:
            if step in catagory.value:
                return catagory
        return None

    def get_selected(item):
        for a in item.actions:
            try:
                if a.true_value is None:
                    a.true_value = True

                if getattr(a.object, a.field) != a.true_value:
                    return False
            except AttributeError:
                if getattr(a.object, a.field) != a.value:
                    return False

        return True


screen path_builder_alert():
    modal True
    style_prefix "path_builder_alert"

    default image_path = "main_menu/path_builder/images/"

    add "darker_80"

    add image_path + "alert_background.webp" align (0.5, 0.5)

    fixed:
        xysize (742, 356)
        pos (587, 364)

        text "THE PATH BUILDER CONTAINS SPOILERS FOR THE STORY\nOF THE GAME. ARE YOU SURE YOU WANT TO CONTINUE?\nYOU WILL NOT BE ABLE TO EARN ACHIEVEMENTS IN THIS MODE.":
            xsize 572
            xalign 0.5
            ypos 66


        hbox:
            pos (217, 258)
            spacing 5

            fixed:
                xysize (132, 61)

                imagebutton:
                    idle "path_builder_button_idle"
                    hover "path_builder_button_hover"
                    action [Hide("path_builder_alert"), Show("path_builder")]
                text "YES" align (0.5, 0.5)

            fixed:
                xysize (132, 61)

                imagebutton:
                    idle "path_builder_button_idle"
                    hover "path_builder_button_hover"
                    action Hide("path_builder_alert")
                text "NO" align (0.5, 0.5)


style path_builder_alert_text is bebas_neue_30

screen path_builder(catagory_step=1):
    tag menu
    modal True

    default image_path = "main_menu/path_builder/images/"
    default grid_size = { # item_count : (rows, cols)
        2: (2, 1),
        3: (3, 1),
        4: (4, 1),
        6: (4, 2),
        11: (4, 3),
        12: (4, 3),
    }

    default catagory = get_catagory(catagory_step)
    default items = [item for item in PathBuilderItem.items if item.catagory == catagory]
    default heading = catagory.value[catagory_step]
    
    $ cols, rows = grid_size[len(items)]

    add image_path + "path_builder_background.webp"
    add image_path + "path_builder_box_background.webp" align (0.5, 0.5)

    vbox:
        align (0.95,0.05)

        imagebutton:
            idle image_path + "button_idle.webp"
            hover image_path + "button_hover.webp"
            selected_idle image_path + "button_hover.webp"
            action ShowMenu("path_builder_advanced_settings")

        text "Advanced":
            align (0.5, 0.5)
            yoffset -50
            color "#FFF"

    imagebutton:
        idle "gui/common/return_idle.webp"
        hover "gui/common/return_hover.webp"
        action ShowMenu("main_menu")
        align (0.015, 0.015)
    
    vbox:
        align (0.5, 0.215)

        add catagory.value["background"]

    vbox:
        spacing 20
        align (0.5, 0.5)

        text heading xalign 0.5

        vpgrid:
            cols cols
            rows rows
            xspacing 10
            xalign 0.5
            yoffset 40

            for item in items:
                if catagory == PathBuilderCatagories.GIRL or catagory == PathBuilderCatagories.HOMECOMING_DATE:
                    vbox:
                        xalign 0.5

                        default girl_image_path = image_path + "girls/"

                        imagebutton:
                            idle girl_image_path + item.name +"_idle.webp"
                            hover girl_image_path + item.name +".webp"
                            selected_idle girl_image_path + item.name +".webp"
                            selected get_selected(item)
                            action [a for a in item.actions]

                        text item.name:
                            align (0.5, 0.5)
                            yoffset -75
                            xoffset 30
                            size 30
                            color "#FFF"

                        #text "Loyal": # This could show the kct for each girl
                        #    align (0.5, 0.5)
                        #    yoffset -75
                        #    xoffset 30
                        #    size 15
                        #    color "#FFF"

                        
                elif catagory == PathBuilderCatagories.START_LOCATION:
                    vbox:
                        xalign 0.5

                        default start_image_path = image_path + "starts/"

                        imagebutton:
                            idle Transform(start_image_path + item.name +".webp", zoom=.8)
                            selected get_selected(item)
                            action [a for a in item.actions]
                            xalign 0.5

                        imagebutton:
                            idle image_path + "button_idle_dark.webp"
                            hover image_path + "button_hover.webp"
                            selected_idle image_path + "button_hover.webp"
                            selected get_selected(item)
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
                            selected get_selected(item)
                            action [a for a in item.actions]

                        text item.name:
                            align (0.5, 0.5)
                            yoffset -50
                            color "#FFF"

        # Option to lock KCT
        if catagory == PathBuilderCatagories.KCT:
            hbox:
                spacing 20
                yoffset 40
                
                imagebutton:
                    idle image_path + "pb_tick.webp"
                    hover image_path + "pb_ticked.webp"
                    selected_idle image_path + "pb_ticked.webp"
                    action ToggleVariable("locked_kct")

                text "Lock KCT (Prevent it from changing)":
                    yoffset -7

    hbox: 
        spacing 50
        align (0.5, 0.9)

        default button_img_path = "main_menu/path_builder/images/"

        if catagory_step > 1:

            imagebutton:
                idle button_img_path + "back.webp"
                action Show("path_builder", None, catagory_step - 1)
        else:
            imagebutton:
                idle button_img_path + "back_blocked.webp"
                action ShowMenu("main_menu")


        imagebutton:
            idle button_img_path + "continue.webp"

            if catagory_step < len(PathBuilderCatagories):
                sensitive any(get_selected(item) for item in items)
                action Show("path_builder", None, catagory_step + 1)
            else:
                action Start(pb_start_location)


screen path_builder_advanced_settings():
    tag menu
    modal True

    default image_path = "main_menu/path_builder/images/"

    add image_path + "path_builder_background.webp"

    text "Advanced Settings" align (0.5, 0.15)

    imagebutton:
        idle "gui/common/return_idle.webp"
        hover "gui/common/return_hover.webp"
        action ShowMenu("path_builder")
        align (0.015, 0.015)

    vbox:
        align (0.25, 0.5)
        hbox:
            spacing 20
            yoffset 40
            
            imagebutton:
                if lindsey_board.money == 10000:
                    idle image_path + "pb_ticked.webp"
                else: 
                    idle image_path + "pb_tick.webp"
                    hover image_path + "pb_ticked.webp"

                if lindsey_board.money == 10000:
                    action [SetVariable("lindsey_board.money", 200), SetVariable("lindsey_board.money", 1500)]
                else:
                    action [SetVariable("lindsey_board.money", 10000), SetVariable("lindsey_board.money", 10000)]

            text "Unlimited Presidency Campaign Budget":
                yoffset -7
    

style path_builder_advanced_settings_text is bebas_neue_30