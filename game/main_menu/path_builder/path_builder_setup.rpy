    label path_builder_setup:
    python:
        pb_items = []

        # Fraternity
        PB_WOLVES = PathBuilderItem(
            PathBuilderCatagories.FRATERNITY,
            "WOLVES",
            actions=[
                SetVariable("path_builder", True),
                SetVariable("joinwolves", True)
            ]
        )

        PB_APES = PathBuilderItem(
            PathBuilderCatagories.FRATERNITY,
            "APES",
            actions=[
                SetVariable("path_builder", True),
                SetVariable("joinwolves", False)
            ]
        )

        #KCT
        PB_LOYAL = PathBuilderItem(
            PathBuilderCatagories.KCT,
            "LOYAL",
            actions=[
                SetVariable("kct", "loyal"),
                SetVariable("bro", 2),
                SetVariable("boyfriend", 2),
                SetVariable("troublemaker", 1)
            ]
        )

        PB_POPULAR = PathBuilderItem(
            PathBuilderCatagories.KCT,
            "POPULAR",
            actions=[
                SetVariable("kct", "popular"),
                SetVariable("bro", 2),
                SetVariable("boyfriend", 1),
                SetVariable("troublemaker", 2)
            ]
        )

        PB_CONFIDENT = PathBuilderItem(
            PathBuilderCatagories.KCT,
            "CONFIDENT",
            actions=[
                SetVariable("kct", "confident"),
                SetVariable("bro", 1),
                SetVariable("boyfriend", 2),
                SetVariable("troublemaker", 2)
            ]
        )


        # Love interests
        PB_CHLOE = PathBuilderItem(
            PathBuilderCatagories.GIRL,
            "CHLOE",
            actions=[
                ToggleField(chloe, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND),
                ToggleVariable("ending", "chloe", "riley"),
                ToggleVariable("hcGirl", "chloe", "alone")
            ]
        )

        PB_NORA = PathBuilderItem(
            PathBuilderCatagories.GIRL,
            "NORA",
            actions=ToggleField(nora, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND)
        )

        PB_AUBREY = PathBuilderItem(
            PathBuilderCatagories.GIRL,
            "AUBREY",
            actions=ToggleField(aubrey, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND)
        )

        PB_RILEY = PathBuilderItem(
            PathBuilderCatagories.GIRL,
            "RILEY",
            actions=ToggleField(riley, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND)
        )

        PB_LAUREN = PathBuilderItem(
            PathBuilderCatagories.GIRL,
            "LAUREN",
            actions=ToggleField(lauren, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND)
        )

        PB_PENELOPE = PathBuilderItem(
            PathBuilderCatagories.GIRL,
            "PENELOPE",
            actions=[
                ToggleField(penelope, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND),
                ToggleVariable("v11_pen_goes_europe")
            ]
        )

        PB_AMBER = PathBuilderItem(
            PathBuilderCatagories.GIRL,
            "AMBER",
            actions=ToggleField(amber, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND)
        )

        PB_LINDSEY = PathBuilderItem(
            PathBuilderCatagories.GIRL,
            "LINDSEY",
            actions=ToggleField(lindsey, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND)
        )

        PB_MS_ROSE = PathBuilderItem(
            PathBuilderCatagories.GIRL,
            "MS ROSE",
            actions=ToggleField(ms_rose, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND)
        )

        PB_SAMANTHA = PathBuilderItem(
            PathBuilderCatagories.GIRL,
            "SAMANTHA",
            actions=ToggleField(samantha, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND)
        )

        PB_JENNY = PathBuilderItem(
            PathBuilderCatagories.GIRL,
            "JENNY",
            actions=ToggleField(jenny, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND)
        )

        PB_EMILY = PathBuilderItem(
            PathBuilderCatagories.GIRL,
            "EMILY",
            actions=ToggleField(emily, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND)
        )


        # Start positions
        PB_ACT_1 = PathBuilderItem(
            PathBuilderCatagories.START_LOCATION,
            "Act 1 Start",
            actions=SetVariable("pb_start_location", "start")
            )
        if renpy.loadable("v8/scene1.rpy"):
            PB_HOMECOMING = PathBuilderItem(
                PathBuilderCatagories.START_LOCATION,
                "Act 2 Start",
                actions=SetVariable("pb_start_location", "v7_homecoming")
                )
        if renpy.loadable("v11/scene1.rpy"):
            PB_ACT_3 = PathBuilderItem(
                PathBuilderCatagories.START_LOCATION,
                "Act 3 Start",
                actions=SetVariable("pb_start_location", "v11_start")
                )
        if renpy.loadable("v14/scene1.rpy"):
            PB_ACT_4 = PathBuilderItem(
                PathBuilderCatagories.START_LOCATION,
                "Act 4 Start",
                actions=SetVariable("pb_start_location", "v14_start")
                )
        

        #Homecoming dates
        HC_CHLOE = PathBuilderItem(
            PathBuilderCatagories.HOMECOMING_DATE,
            "CHLOE", 
            actions=SetVariable("hcGirl", "chloe")
            )

        HC_RILEY = PathBuilderItem(
            PathBuilderCatagories.HOMECOMING_DATE,
            "RILEY", 
            actions=SetVariable("hcGirl", "riley")
            )

        HC_LAUREN = PathBuilderItem(
            PathBuilderCatagories.HOMECOMING_DATE,
            "LAUREN", 
            actions=SetVariable("hcGirl", "lauren")
            )

        HC_PENELOPE = PathBuilderItem(
            PathBuilderCatagories.HOMECOMING_DATE,
            "PENELOPE",
            actions=SetVariable("hcGirl", "penelope")
            )

        HC_AMBER = PathBuilderItem(
            PathBuilderCatagories.HOMECOMING_DATE,
            "AMBER",
            actions=SetVariable("hcGirl", "amber")
            )

        HC_EMILY = PathBuilderItem(
            PathBuilderCatagories.HOMECOMING_DATE,
            "EMILY",
            actions=SetVariable("hcGirl", "emily")
            )

    return