init python:
    pb_items = []

    class PathBuilderCategories(Enum):
        FRATERNITY = "Step 1: Pick a fraternity"
        KCT = "Step 2: Pick your starting KCT"
        GIRL = "Step 3: Pick which girls you want to be romantically involved with"
        START_LOCATION = "Step 4: Pick your starting location"
        HOMECOMING_DATE = "Step 5: Pick your homecoming date"
    

    class PathBuilderItem:
        def __init__(self, category, name, actions=None):
            self.category = category
            self.name = name

            if actions is None: self.actions = []
            elif isinstance(actions, list): self.actions = actions
            else: self.actions = [actions]

            pb_items.append(self)


    def get_category(step):
        for category in PathBuilderCategories:
            if category.value.startswith("Step {}".format(step)):
                return category
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


screen path_builder_base(header=""):
    add "images/path builder/path_builder_background.webp"

    text "PATH BUILDER":
        size 50
        align (0.5, 0.1)

    vbox:
        spacing 20
        pos (200, 300)

        text header

        transclude


screen path_builder(category_step=1):
    tag menu
    modal True

    default category = get_category(category_step)
    default items = [item for item in pb_items if item.category == category]

    use path_builder_base(header=category.value):
        vpgrid:
            cols 4
            xspacing 50
            yspacing 20

            for item in items:
                vbox:
                    imagebutton:
                        idle "images/path builder/pb_button.webp"
                        hover "images/path builder/pb_selected.webp"
                        selected_idle "images/path builder/pb_selected.webp"
                        selected get_selected(item)
                        action [a for a in item.actions]

                    text item.name:
                        align (0.5, 0.5)
                        yoffset -70
                        color "#000"

        # Option to lock KCT
        if category == PathBuilderCategories.KCT:
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
                if category_step > 1:
                    action Show("path_builder", None, category_step - 1)
                else:
                    action ShowMenu("main_menu")

            textbutton "CONTINUE":
                xalign 1.0
                selected False
                if category_step < len(PathBuilderCategories):
                    sensitive any(get_selected(item) for item in items)
                    action Show("path_builder", None, category_step + 1)
                else:
                    action Start(pb_start_location)