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


    def get_catagory(step):
        for catagory in PathBuilderCatagories:
            if catagory.value.startswith("Step {}".format(step)):
                return catagory
        return None


define PB_WOLVES = PathBuilderItem(
    PathBuilderCatagories.FRATERNITY,
    "Wolves",
    [
        (set_variable, "path_builder", True),
        (set_variable, "joinwolves", True),
        (set_variable, "forgiveemily", True)
    ])
define PB_APES = PathBuilderItem(
    PathBuilderCatagories.FRATERNITY,
    "Apes",
    [
        (set_variable, "path_builder", True),
        (set_variable, "joinwolves", False),
        (set_variable, "forgiveemily", True)
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
        (set_variable, "chloe.relationship", Relationship.GIRLFRIEND),
        (set_variable, "ending", "chloe"),
        (set_variable, "hcGirl", "chloe")
    ])
define PB_NORA = PathBuilderItem(PathBuilderCatagories.GIRL, "Nora", [(toggle_variable, "nora.relationship", Relationship.FRIEND, Relationship.GIRLFRIEND)])
define PB_AUBREY = PathBuilderItem(PathBuilderCatagories.GIRL, "Aubrey", [(toggle_variable, "aubrey.relationship", Relationship.FRIEND, Relationship.GIRLFRIEND)])
define PB_RILEY = PathBuilderItem(PathBuilderCatagories.GIRL, "Riley", [(toggle_variable, "riley.relationship", Relationship.FRIEND, Relationship.GIRLFRIEND)])
define PB_LAUREN = PathBuilderItem(PathBuilderCatagories.GIRL, "Lauren", [(toggle_variable, "lauren.relationship", Relationship.FRIEND, Relationship.GIRLFRIEND)])
define PB_PENELOPE = PathBuilderItem(PathBuilderCatagories.GIRL, "Penelope", [
        (toggle_variable, "penelope.relationship", Relationship.FRIEND, Relationship.GIRLFRIEND)
        (toggle_variable, "v11_pen_goes_europe")
    ])
define PB_AMBER = PathBuilderItem(PathBuilderCatagories.GIRL, "Amber", [(toggle_variable, "amber.relationship", Relationship.FRIEND, Relationship.GIRLFRIEND)])
define PB_LINDSEY = PathBuilderItem(PathBuilderCatagories.GIRL, "Lindsey", [(toggle_variable, "lindsey.relationship", Relationship.FRIEND, Relationship.GIRLFRIEND)])
define PB_MS_ROSE = PathBuilderItem(PathBuilderCatagories.GIRL, "Ms Rose", [(toggle_variable, "ms_rose.relationship", Relationship.FRIEND, Relationship.GIRLFRIEND)])
define PB_SAMANTHA = PathBuilderItem(PathBuilderCatagories.GIRL, "Samantha", [(toggle_variable, "samantha.relationship", Relationship.FRIEND, Relationship.GIRLFRIEND)])
define PB_JENNY = PathBuilderItem(PathBuilderCatagories.GIRL, "Jenny", [(toggle_variable, "jenny.relationship", Relationship.FRIEND, Relationship.GIRLFRIEND)])
define PB_EMILY = PathBuilderItem(PathBuilderCatagories.GIRL, "Emily", [(toggle_variable, "emily.relationship", Relationship.FRIEND, Relationship.GIRLFRIEND)])

define PB_ACT_1 = PathBuilderItem(PathBuilderCatagories.START_LOCATION, "Act 1 Start", [(set_variable, "start_location", "start")])
define PB_HOMECOMING = PathBuilderItem(PathBuilderCatagories.START_LOCATION, "Act 2 Start", [(set_variable, "start_location", "v7_homecoming")])
define PB_ACT_3 = PathBuilderItem(PathBuilderCatagories.START_LOCATION, "Act 3 Start", [(set_variable, "start_location", "v11_start")])
define PB_ACT_4 = PathBuilderItem(PathBuilderCatagories.START_LOCATION, "Act 4 Start", [(set_variable, "start_location", "v14_start")])

screen spoiler_path_builder():
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
                        selected all(getattr(store, variable) == value for func variable, value in item.funcs) or all(value in variable for func variable, value in item.funcs)
                        action [Function(func, variable, value) for func, variable, value in item.funcs]

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
                    sensitive any(all(getattr(store, variable) == value for variable, value in zip(item.variables, item.values)) for item in items)
                    action Show("path_builder", None, catagory_step + 1)
                elif start_location == "v7_homecoming":
                    action Show("pb_select_homecoming_date")
                else:
                    action Start(start_location)


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