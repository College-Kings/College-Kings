label path_builder_setup:
    python:
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

        PB_CHLOE = PathBuilderItem(PathBuilderCatagories.GIRL, "Chloe",
            actions=[
                ToggleField(chloe, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND),
                ToggleVariable("ending", "chloe", "riley"),
                ToggleVariable("hcGirl", "chloe", "alone")])
        PB_NORA = PathBuilderItem(PathBuilderCatagories.GIRL, "Nora",
            ToggleField(nora, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
        PB_AUBREY = PathBuilderItem(PathBuilderCatagories.GIRL, "Aubrey",
            actions=ToggleField(aubrey, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
        PB_RILEY = PathBuilderItem(PathBuilderCatagories.GIRL, "Riley",
            actions=ToggleField(riley, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
        PB_LAUREN = PathBuilderItem(PathBuilderCatagories.GIRL, "Lauren",
            actions=ToggleField(lauren, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
        PB_PENELOPE = PathBuilderItem(PathBuilderCatagories.GIRL, "Penelope",
            actions=[
                ToggleField(penelope, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND),
                ToggleVariable("v11_pen_goes_europe")])
        PB_AMBER = PathBuilderItem(PathBuilderCatagories.GIRL, "Amber",
            actions=ToggleField(amber, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
        PB_LINDSEY = PathBuilderItem(PathBuilderCatagories.GIRL, "Lindsey",
            actions=ToggleField(lindsey, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
        PB_MS_ROSE = PathBuilderItem(PathBuilderCatagories.GIRL, "Ms Rose",
            actions=ToggleField(ms_rose, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
        PB_SAMANTHA = PathBuilderItem(PathBuilderCatagories.GIRL, "Samantha",
            actions=ToggleField(samantha, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
        PB_JENNY = PathBuilderItem(PathBuilderCatagories.GIRL, "Jenny",
            actions=ToggleField(jenny, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
        PB_EMILY = PathBuilderItem(PathBuilderCatagories.GIRL, "Emily",
            actions=ToggleField(emily, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))

        PB_ACT_1 = PathBuilderItem(PathBuilderCatagories.START_LOCATION, "Act 1 Start", actions=SetVariable("pb_start_location", "start"))
        if renpy.loadable("v8/scene1.rpy"):
            PB_HOMECOMING = PathBuilderItem(PathBuilderCatagories.START_LOCATION, "Act 2 Start", actions=SetVariable("pb_start_location", "v7_homecoming"))
        if renpy.loadable("v11/scene1.rpy"):
            PB_ACT_3 = PathBuilderItem(PathBuilderCatagories.START_LOCATION, "Act 3 Start", actions=SetVariable("pb_start_location", "v11_start"))
        if renpy.loadable("v14/scene1.rpy"):
            PB_ACT_4 = PathBuilderItem(PathBuilderCatagories.START_LOCATION, "Act 4 Start", actions=SetVariable("pb_start_location", "v14_start"))

    return