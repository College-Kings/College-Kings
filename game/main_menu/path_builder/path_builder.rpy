init python:
    pb_items = []

    class PathBuilderCategories(Enum):
        FRATERNITY          =   "Step 1: PICK A FRATERNITY"
        KCT                 =   "Step 2: PICK YOUR STARTING KCT"
        GIRL                =   "Step 3: PICK WHICH GIRLS YOU WANT TO BE ROMANTICALLY INVOLVED WITH"
        START_LOCATION      =   "Step 4: PICK YOUR STARTING LOCATION"
        HOMECOMING_DATE     =   "Step 5: PICK YOUR HOMECOMING DATE"
    

    class PathBuilderItem:
        def __init__(self, catagory, name, actions=None):
            self.catagory = catagory
            self.name = name

            if actions is None: self.actions = []
            elif isinstance(actions, list): self.actions = actions
            else: self.actions = [actions]

            pb_items.append(self)


    def get_catagory(step):
        for catagory in PathBuilderCategories:
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

        text "THE PATH BUILDER CONTAINS SPOILERS FOR THE STORY OF THE GAME. ARE YOU SURE YOU WANT TO CONTINUE?":
            xsize 512
            xalign 0.5
            ypos 86


        hbox:
            pos (217, 228)
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


style path_builder_alert_text is olympus_mount_30


screen path_builder_base(header=""):

    default image_path = "main_menu/path_builder/images/"

    add image_path + "pathbuilder_background.webp"

    add image_path + "path_builder_steps_background.webp" align (0.5, 0.5)

    vbox:
        spacing 20
        pos (200, 300)

        text header

        transclude


screen path_builder(catagory_step=1):
    tag menu
    modal True

    default image_path = "main_menu/path_builder/images/"

    default catagory = get_catagory(catagory_step)
    default items = [item for item in pb_items if item.catagory == catagory]

    use path_builder_base(header=catagory.value):
        vpgrid:
            cols 4
            xspacing 50
            yspacing 20

            for item in items:
                vbox:
                    imagebutton:
                        idle  image_path + "path_builder_button_idle.webp"
                        hover image_path + "path_builder_button_selected.webp"
                        selected_idle image_path + "path_builder_button_selected.webp"
                        selected get_selected(item)
                        action [a for a in item.actions]

                    text item.name:
                        align (0.5, 0.5)
                        yoffset -50
                        color "#fff"

        # Option to lock KCT
        if catagory == PathBuilderCategories.KCT:
            hbox:
                spacing 20
                
                imagebutton:
                    idle "images/path builder/pb_tick.webp"
                    hover "images/path builder/pb_ticked.webp"
                    selected_idle "images/path builder/pb_ticked.webp"
                    action ToggleVariable("locked_kct")

                text "Lock KCT (Prevent it from changing)":
                    yoffset -7

        hbox: 
            spacing 200

            textbutton "BACK":
                xalign 0
                selected False
                if catagory_step > 1:
                    action Show("path_builder", None, catagory_step - 1)
                else:
                    action ShowMenu("main_menu")

            textbutton "CONTINUE":
                xalign 1.0
                selected False
                if catagory_step < len(PathBuilderCategories):
                    sensitive any(get_selected(item) for item in items)
                    action Show("path_builder", None, catagory_step + 1)
                elif pb_start_location == "v7_homecoming":
                    action Start("v7_homecoming")
                else:
                    action Start(pb_start_location)