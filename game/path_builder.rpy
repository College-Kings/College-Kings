init python:
    pb_item = []
    pb_catagories = []

    class PathBuilderCatagories(Enum):
        FRATERNITY = "Step 1: Pick a fraternity"
        KCT = "Step 2: Pick your starting KCT"
        GIRL = "Step 3: Pick which girls you want to be romantically involved with"
        START_LOCATION = "Step 4: Pick your starting location"
    

    class PathBuilderItem:
        def __init__(self, catagory, name, funcs=None):
            self.catagory = catagory
            self.name = name

            if funcs is None: self.funcs = []
            elif isinstance(funcs, list): self.funcs = funcs
            else: self.funcs = [funcs]

            pb_item.append(self)


    # Action functions
    def set_variable(variable, value):
        setattr(store, variable, value)

    def toggle_variable(variable, true_value=True, false_value=False):
        current_value = getattr(store, variable)

        if current_value == true_value:
            setattr(store, variable, false_value)
        else:
            setattr(store, variable, true_value)

    def add_to_list(variable, value):
        var = getattr(store, variable)

        var.append(value)
        setattr(store, variable, var)

    def add_to_set(variable, value):
        var = getattr(store, variable)
        
        var.add(value)
        setattr(store, variable, var)

    def toggle_field(obj, field, true_value=True, false_value=False):
        obj = getattr(store, obj)
        current_value = getattr(obj, field)

        if current_value == true_value:
            setattr(obj, field, false_value)
        else:
            setattr(obj, field, true_value)

    def get_catagory(step):
        for catagory in PathBuilderCatagories:
            if catagory.value.startswith("Step {}".format(step)):
                return catagory
        return None

    def get_selected(item):
        for i in item.funcs:
            func = i[0]
            obj = getattr(store, i[1]) if func == toggle_field else store
            args = i[2:] if func == toggle_field else i[1:]

            try:
                if getattr(obj, args[0]) != args[1]:
                    return False
            except IndexError:
                if getattr(obj, args[0]) is False:
                    return False

        return True
        


define PB_WOLVES = PathBuilderItem(
    PathBuilderCatagories.FRATERNITY,
    "Wolves",
    [
        (set_variable, "path_builder", True),
        (set_variable, "joinwolves", True)
    ])
define PB_APES = PathBuilderItem(
    PathBuilderCatagories.FRATERNITY,
    "Apes",
    [
        (set_variable, "path_builder", True),
        (set_variable, "joinwolves", False)
    ])

define PB_LOYAL = PathBuilderItem(
    PathBuilderCatagories.KCT,
    "Loyal",
    [
        (set_variable, "kct", "loyal"),
        (set_variable, "bro", 2),
        (set_variable, "boyfriend", 2),
        (set_variable, "troublemaker", 1)
    ])
define PB_POPULAR = PathBuilderItem(
    PathBuilderCatagories.KCT,
    "Popular",
    [
        (set_variable, "kct", "popular"),
        (set_variable, "bro", 2),
        (set_variable, "boyfriend", 1),
        (set_variable, "troublemaker", 2)
    ])
define PB_CONFIDENT = PathBuilderItem(
    PathBuilderCatagories.KCT,
    "Confident",
    [
        (set_variable, "kct", "confident"),
        (set_variable, "bro", 1),
        (set_variable, "boyfriend", 2),
        (set_variable, "troublemaker", 2)
    ])

define PB_CHLOE = PathBuilderItem(PathBuilderCatagories.GIRL, "Chloe",
    [
        (toggle_field, "chloe", "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND),
        (toggle_variable, "ending", "chloe", "riley"),
        (toggle_variable, "hcGirl", "chloe", "alone")
    ])
define PB_NORA = PathBuilderItem(PathBuilderCatagories.GIRL, "Nora", (toggle_field, "nora", "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
define PB_AUBREY = PathBuilderItem(PathBuilderCatagories.GIRL, "Aubrey", (toggle_field, "aubrey", "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
define PB_RILEY = PathBuilderItem(PathBuilderCatagories.GIRL, "Riley", (toggle_field, "riley", "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
define PB_LAUREN = PathBuilderItem(PathBuilderCatagories.GIRL, "Lauren", (toggle_field, "lauren", "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
define PB_PENELOPE = PathBuilderItem(PathBuilderCatagories.GIRL, "Penelope", [
        (toggle_field, "penelope", "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND),
        (toggle_variable, "v11_pen_goes_europe")
    ])
define PB_AMBER = PathBuilderItem(PathBuilderCatagories.GIRL, "Amber", (toggle_field, "amber", "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
define PB_LINDSEY = PathBuilderItem(PathBuilderCatagories.GIRL, "Lindsey", (toggle_field, "lindsey", "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
define PB_MS_ROSE = PathBuilderItem(PathBuilderCatagories.GIRL, "Ms Rose", (toggle_field, "ms_rose", "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
define PB_SAMANTHA = PathBuilderItem(PathBuilderCatagories.GIRL, "Samantha", (toggle_field, "samantha", "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
define PB_JENNY = PathBuilderItem(PathBuilderCatagories.GIRL, "Jenny", (toggle_field, "jenny", "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
define PB_EMILY = PathBuilderItem(PathBuilderCatagories.GIRL, "Emily", (toggle_field, "emily", "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))

define PB_ACT_1 = PathBuilderItem(PathBuilderCatagories.START_LOCATION, "Act 1 Start", (set_variable, "pb_start_location", "start"))
define PB_HOMECOMING = PathBuilderItem(PathBuilderCatagories.START_LOCATION, "Act 2 Start", (set_variable, "pb_start_location", "v7_homecoming"))
define PB_ACT_3 = PathBuilderItem(PathBuilderCatagories.START_LOCATION, "Act 3 Start", (set_variable, "pb_start_location", "v11_start"))
define PB_ACT_4 = PathBuilderItem(PathBuilderCatagories.START_LOCATION, "Act 4 Start", (set_variable, "pb_start_location", "v14_start"))


screen path_builder_spoiler():
    modal True

    add "images/darker.webp"

    use endfrTemplate:
        text "Warning: The path builder contains spoilers for the story of the game. Are you sure you want to continue?":
            style "endfree"
            xalign 0.5

        hbox:
            align (0.5, 1.0)
            spacing 200

            textbutton "Yes":
                action [Hide("spoiler_path_builder"), Show("path_builder")]

            textbutton "No":
                action Hide("spoiler_path_builder")


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


screen path_builder(catagory_step=1):
    tag menu
    modal True

    default catagory = get_catagory(catagory_step)
    default items = [item for item in pb_item if item.catagory == catagory]
    
    use path_builder_base(header=catagory.value):
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
                        action [Function(i[0], *i[1:]) for i in item.funcs]

                    text item.name:
                        align (0.5, 0.5)
                        yoffset -70
                        color "#000"

        # Option to lock KCT
        if catagory == PathBuilderCatagories.KCT:
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
                if catagory_step < len(PathBuilderCatagories):
                    sensitive any(get_selected(item) for item in items)
                    action Show("path_builder", None, catagory_step + 1)
                elif pb_start_location == "v7_homecoming":
                    action Show("pb_select_homecoming_date")
                else:
                    action Start(pb_start_location)


screen pb_select_homecoming_date():
    tag menu
    modal True

    default items = [
        ["Chloe", "hcGirl", "chloe"],
        ["Riley", "hcGirl", "riley"],
        ["Lauren", "hcGirl", "lauren"],
        ["Penelope", "hcGirl", "penelope"],
        ["Emily", "hcGirl", "emily"],
        ["Amber", "hcGirl", "amber"],
    ]

    use path_builder_base(header="Step 5: Pick your homecoming date"):
        vpgrid:
            cols 4
            xspacing 50
            yspacing 20

            for name, variable, value in items:
                vbox:
                    imagebutton:
                        idle "images/path builder/pb_button.webp"
                        hover "images/path builder/pb_selected.webp"
                        selected_idle "images/path builder/pb_selected.webp"
                        action ToggleVariable(variable, value)

                    text name:
                        align (0.5, 0.5)
                        yoffset -70
                        color "#000"

        hbox: 
            spacing 200

            textbutton "BACK":        
                xalign 0
                action Show("path_builder", catagory_step=3)

            textbutton "CONTINUE":          
                xalign 1.0
                action Start("v7_homecoming")