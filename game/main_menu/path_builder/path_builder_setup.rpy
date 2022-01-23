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
        PB_NORA = PathBuilderGirl(PathBuilderCatagories.GIRL, "Nora", "Loyal/Confident",
            ToggleField(nora, "relationship", Relationship.FWB, Relationship.FRIEND))
        PB_AUBREY = PathBuilderGirl(PathBuilderCatagories.GIRL, "Aubrey", "Popular",
            actions=ToggleField(aubrey, "relationship", Relationship.FWB, Relationship.FRIEND))
        PB_RILEY = PathBuilderGirl(PathBuilderCatagories.GIRL, "Riley", "Confident",
            actions=ToggleField(riley, "relationship", Relationship.FWB, Relationship.FRIEND))
        PB_LAUREN = PathBuilderGirl(PathBuilderCatagories.GIRL, "Lauren", "Loyal",
            actions=ToggleField(lauren, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
        PB_PENELOPE = PathBuilderGirl(PathBuilderCatagories.GIRL, "Penelope", "Confident",
            actions=[
                ToggleField(penelope, "relationship", Relationship.LOYAL, Relationship.FRIEND), 
                ToggleVariable("v11_pen_goes_europe")], act_requirement=4)
        PB_AMBER = PathBuilderGirl(PathBuilderCatagories.GIRL, "Amber", "Popular",
            actions=ToggleField(amber, "relationship", Relationship.FWB, Relationship.FRIEND))
        PB_LINDSEY = PathBuilderGirl(PathBuilderCatagories.GIRL, "Lindsey", "Popular",
            actions=ToggleField(lindsey, "relationship", Relationship.FWB, Relationship.FRIEND), act_requirement=3)
        PB_MS_ROSE = PathBuilderGirl(PathBuilderCatagories.GIRL, "Ms Rose", "Confident",
            actions=ToggleField(ms_rose, "relationship", Relationship.FWB, Relationship.FRIEND),
            frat_requirement=Frat.WOLVES, act_requirement=3)
        PB_SAMANTHA = PathBuilderGirl(PathBuilderCatagories.GIRL, "Samantha", "Loyal",
            actions=ToggleField(samantha, "relationship", Relationship.FWB, Relationship.FRIEND),
            frat_requirement=Frat.APES, act_requirement=4)
        PB_JENNY = PathBuilderGirl(PathBuilderCatagories.GIRL, "Jenny", "Popular",
            actions=ToggleField(jenny, "relationship", Relationship.FWB, Relationship.FRIEND))
        if renpy.loadable("v14/scene1.rpy"):
            PB_EMILY = PathBuilderGirl(PathBuilderCatagories.GIRL, "Emily", "Loyal",
                actions=[
                    ToggleField(emily, "relationship", Relationship.FWB, Relationship.FRIEND),
                    ToggleVariable("emily_europe"),
                    ToggleVariable("v14_emily_ily")])
        elif renpy.loadable("v11/scene1.rpy"):
            PB_EMILY = PathBuilderGirl(PathBuilderCatagories.GIRL, "Emily", "Loyal",
                actions=[
                    ToggleField(emily, "relationship", Relationship.FWB, Relationship.FRIEND),
                    ToggleVariable("emily_europe")])
        else:
            PB_EMILY = PathBuilderGirl(PathBuilderCatagories.GIRL, "Emily", "Loyal",
                actions=[
                    ToggleField(emily, "relationship", Relationship.FWB, Relationship.FRIEND)])
                    
        PB_ACT_1 = PathBuilderItem(PathBuilderCatagories.START_LOCATION, "Act 1 Start", actions=[SetScreenVariable("start_label", "start"), SetScreenVariable("act_number", 1)])
        if renpy.loadable("v8/scene1.rpy"):
            PB_ACT_2 = PathBuilderItem(PathBuilderCatagories.START_LOCATION, "Act 2 Start", actions=[SetScreenVariable("start_label", "v7_homecoming"), SetScreenVariable("act_number", 2)])
        if renpy.loadable("v11/scene1.rpy"):
            PB_ACT_3 = PathBuilderItem(PathBuilderCatagories.START_LOCATION, "Act 3 Start", actions=[SetScreenVariable("start_label", "v11_start"), SetScreenVariable("act_number", 3)])
        if renpy.loadable("v14/scene1.rpy"):
            PB_ACT_4 = PathBuilderItem(PathBuilderCatagories.START_LOCATION, "Act 4 Start", actions=[SetScreenVariable("start_label", "v14_start"), SetScreenVariable("act_number", 4)])

        HC_CHLOE = PathBuilderItem(PathBuilderCatagories.HOMECOMING_DATE, "Chloe", actions=ToggleVariable("hcGirl", "chloe"))
        HC_RILEY = PathBuilderItem(PathBuilderCatagories.HOMECOMING_DATE, "Riley", actions=ToggleVariable("hcGirl", "riley"))
        HC_LAUREN = PathBuilderItem(PathBuilderCatagories.HOMECOMING_DATE, "Lauren", actions=ToggleVariable("hcGirl", "lauren"))
        HC_PENELOPE = PathBuilderItem(PathBuilderCatagories.HOMECOMING_DATE, "Penelope", actions=ToggleVariable("hcGirl", "penelope"))
        HC_EMILY = PathBuilderItem(PathBuilderCatagories.HOMECOMING_DATE, "Emily", actions=ToggleVariable("hcGirl", "emily"))
        HC_AMBER = PathBuilderItem(PathBuilderCatagories.HOMECOMING_DATE, "Amber", actions=ToggleVariable("hcGirl", "amber"))

    return