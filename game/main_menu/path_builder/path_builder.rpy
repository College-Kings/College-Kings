init python:
    class PathBuilderCatagories(Enum):
        FRATERNITY          =   "Step 1: Pick a fraternity"
        KCT                 =   "Step 2: Pick your starting KCT"
        GIRL                =   "Step 3: Pick which girls you want to be romantically involved with"
        START_LOCATION      =   "Step 4: Pick your starting location"
        HOMECOMING_DATE     =   "Step 5: Pick your homecoming date"
    

    class PathBuilderItem:
        def __init__(self, catagory, name, actions=None):
            self.catagory = catagory
            self.name = name

            if actions is None: self.actions = []
            elif isinstance(actions, list): self.actions = actions
            else: self.actions = [actions]

            pb_items.append(self)


    def get_catagory(step):
        for catagory in PathBuilderCatagories:
            if catagory.value.startswith("Step {}".format(step)):
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
    default image_path_2 = "images/path builder/"

    default catagory = get_catagory(catagory_step)
    default items = [item for item in pb_items if item.catagory == catagory]

    default header = catagory.value

    $ heading = 0

    if header == "Step 1: Pick a fraternity":
        $ heading = "Pick a fraternity"
    elif header == "Step 2: Pick your starting KCT":
        $ heading = "Pick your starting KCT"
    elif header == "Step 3: Pick which girls you want to be romantically involved with":
        $ heading = "Pick which girls you want to be romantically involved with"
    elif header == "Step 4: Pick your starting location":
        $ heading = "Pick your starting location"
    elif header == "Step 5: Pick your homecoming date":
        $ heading = "Pick your homecoming date"
    

    add image_path_2 + "path_builder_background.webp"
    add image_path_2 + "path_builder_box_background.webp" align (0.5, 0.5)

    imagebutton:
        idle "gui/common/return_idle.webp"
        hover "gui/common/return_hover.webp"
        action ShowMenu("main_menu")
        align (0.015, 0.015)
    
    vbox:
        align (0.5, 0.215)

        if catagory == PathBuilderCatagories.FRATERNITY:
            add image_path_2 + "path_builder_step_1.webp" xalign 0.5
        elif catagory == PathBuilderCatagories.KCT:
            add image_path_2 + "path_builder_step_2.webp" xalign 0.5
        elif catagory == PathBuilderCatagories.GIRL:
            add image_path_2 + "path_builder_step_3.webp" xalign 0.5
        elif catagory == PathBuilderCatagories.START_LOCATION:
            add image_path_2 + "path_builder_step_4.webp" xalign 0.5
        elif catagory == PathBuilderCatagories.HOMECOMING_DATE:
            add image_path_2 + "path_builder_step_5.webp" xalign 0.5

    vbox:
        spacing 20
        align (0.5, 0.5)

        text heading xalign 0.5

        $ count = 0
        $ col   = 0
        $ row   = 0

        for item in items:
            $ count += 1


        if count == 1:
            $ col = 1
            $ row = 1
        elif count == 2:
            $ col = 2
            $ row = 1
        elif count == 3:
            $ col = 3
            $ row = 1
        elif count == 4:
            $ col = 4
            $ row = 1
        elif count >= 5 and count <= 8:
            $ col = 4
            $ row = 2
        elif count >= 9 and count <= 12:
            $ col = 4
            $ row = 3
        elif count >= 13 and count <= 15:
            $ col = 4
            $ row = 4
            

        vpgrid:
            cols col
            rows row
            xspacing 10
            xalign 0.5
            yoffset 40

            for item in items:
                if catagory == PathBuilderCatagories.GIRL or catagory == PathBuilderCatagories.HOMECOMING_DATE:
                    vbox:
                        xalign 0.5

                        default girl_image_path = image_path_2 + "girls/"

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
                elif catagory == PathBuilderCatagories.START_LOCATION:
                    vbox:
                        xalign 0.5

                        default start_image_path = image_path_2 + "starts/"

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
                    idle "images/path builder/pb_tick.webp"
                    hover "images/path builder/pb_ticked.webp"
                    selected_idle "images/path builder/pb_ticked.webp"
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