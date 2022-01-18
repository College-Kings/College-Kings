label path_builder_setup:
    python:
        PathBuilderItem.items = []

        PB_WOLVES = PathBuilderItem(
            PathBuilderCatagories.FRATERNITY,
            "Wolves",
            actions=[SetVariable("path_builder", True), SetVariable("joinwolves", True)])
        PB_APES = PathBuilderItem(
            PathBuilderCatagories.FRATERNITY,
            "Apes",
            actions=[SetVariable("path_builder", True), SetVariable("joinwolves", False)])

        PB_LOYAL = PathBuilderItem(
            PathBuilderCatagories.KCT,
            "Loyal",
            actions=[SetVariable("kct", "loyal"), SetVariable("bro", 2), SetVariable("boyfriend", 2), SetVariable("troublemaker", 1)])
        PB_POPULAR = PathBuilderItem(
            PathBuilderCatagories.KCT,
            "Popular",
            actions=[SetVariable("kct", "popular"), SetVariable("bro", 2), SetVariable("boyfriend", 1), SetVariable("troublemaker", 2)])

        PB_CONFIDENT = PathBuilderItem(
            PathBuilderCatagories.KCT,
            "Confident",
            actions=[SetVariable("kct", "confident"), SetVariable("bro", 1), SetVariable("boyfriend", 2), SetVariable("troublemaker", 2)])

        PB_CHLOE = PathBuilderGirl(PathBuilderCatagories.GIRL, "Chloe", "Popular",
            actions=[
                ToggleField(chloe, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND),
                ToggleVariable("ending", "chloe", "riley"),
                ToggleVariable("hcGirl", "chloe", "alone")])
        PB_NORA = PathBuilderGirl(PathBuilderCatagories.GIRL, "Nora",
            ToggleField(nora, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
        PB_AUBREY = PathBuilderGirl(PathBuilderCatagories.GIRL, "Aubrey",
            actions=ToggleField(aubrey, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
        PB_RILEY = PathBuilderGirl(PathBuilderCatagories.GIRL, "Riley",
            actions=ToggleField(riley, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
        PB_LAUREN = PathBuilderGirl(PathBuilderCatagories.GIRL, "Lauren",
            actions=ToggleField(lauren, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
        PB_PENELOPE = PathBuilderGirl(PathBuilderCatagories.GIRL, "Penelope",
            actions=[
                ToggleField(penelope, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND),
                ToggleVariable("v11_pen_goes_europe")])
        PB_AMBER = PathBuilderGirl(PathBuilderCatagories.GIRL, "Amber",
            actions=ToggleField(amber, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
        PB_LINDSEY = PathBuilderGirl(PathBuilderCatagories.GIRL, "Lindsey",
            actions=ToggleField(lindsey, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
        PB_MS_ROSE = PathBuilderGirl(PathBuilderCatagories.GIRL, "Ms Rose",
            actions=ToggleField(ms_rose, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
        PB_SAMANTHA = PathBuilderGirl(PathBuilderCatagories.GIRL, "Samantha",
            actions=ToggleField(samantha, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
        PB_JENNY = PathBuilderGirl(PathBuilderCatagories.GIRL, "Jenny",
            actions=ToggleField(jenny, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
        PB_EMILY = PathBuilderGirl(PathBuilderCatagories.GIRL, "Emily",
            actions=[
                ToggleField(emily, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND),
                ToggleVariable("emily_europe"),
                ToggleVariable("v14_emily_ily")])

        PB_ACT_1 = PathBuilderItem(PathBuilderCatagories.START_LOCATION, "Act 1 Start", actions=SetScreenVariable("start_label", "start"))
        if renpy.loadable("v8/scene1.rpy"):
            PB_ACT_2 = PathBuilderItem(PathBuilderCatagories.START_LOCATION, "Act 2 Start", actions=SetScreenVariable("start_label", "v7_homecoming"))
        if renpy.loadable("v11/scene1.rpy"):
            PB_ACT_3 = PathBuilderItem(PathBuilderCatagories.START_LOCATION, "Act 3 Start", actions=SetScreenVariable("start_label", "v11_start"))
        if renpy.loadable("v14/scene1.rpy"):
            PB_ACT_4 = PathBuilderItem(PathBuilderCatagories.START_LOCATION, "Act 4 Start", actions=SetScreenVariable("start_label", "v14_start"))

        HC_CHLOE = PathBuilderItem(PathBuilderCatagories.HOMECOMING_DATE, "Chloe",actions=ToggleVariable("hcGirl", "chloe"))
        HC_RILEY = PathBuilderItem(PathBuilderCatagories.HOMECOMING_DATE, "Riley",actions=ToggleVariable("hcGirl", "riley"))
        HC_LAUREN = PathBuilderItem(PathBuilderCatagories.HOMECOMING_DATE, "Lauren",actions=ToggleVariable("hcGirl", "lauren"))
        HC_PENELOPE = PathBuilderItem(PathBuilderCatagories.HOMECOMING_DATE, "Penelope",actions=ToggleVariable("hcGirl", "penelope"))
        HC_EMILY = PathBuilderItem(PathBuilderCatagories.HOMECOMING_DATE, "Emily",actions=ToggleVariable("hcGirl", "emily"))
        HC_AMBER = PathBuilderItem(PathBuilderCatagories.HOMECOMING_DATE, "Amber",actions=ToggleVariable("hcGirl", "amber"))

    return