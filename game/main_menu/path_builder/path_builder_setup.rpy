label path_builder_setup:
    python:
        pb_items = []


        # Fraternity
        PB_WOLVES = PathBuilderItem(
            PathBuilderCategories.FRATERNITY,
            "WOLVES",
            actions=[
                SetVariable("path_builder", True),
                SetVariable("joinwolves", True)
            ]
        )

        PB_APES = PathBuilderItem(
            PathBuilderCategories.FRATERNITY,
            "APES",
            actions=[
                SetVariable("path_builder", True),
                SetVariable("joinwolves", False)
            ]
        )


        #KCT
        PB_LOYAL = PathBuilderItem(
            PathBuilderCategories.KCT,
            "LOYAL",
            actions=[
                SetVariable("kct", "loyal"),
                SetVariable("bro", 2),
                SetVariable("boyfriend", 2),
                SetVariable("troublemaker", 1)
            ]
        )

        PB_POPULAR = PathBuilderItem(
            PathBuilderCategories.KCT,
            "POPULAR",
            actions=[
                SetVariable("kct", "popular"),
                SetVariable("bro", 2),
                SetVariable("boyfriend", 1),
                SetVariable("troublemaker", 2)
            ]
        )

        PB_CONFIDENT = PathBuilderItem(
            PathBuilderCategories.KCT,
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
            PathBuilderCategories.GIRL,
            "CHLOE",
            actions=[
                ToggleField(chloe, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND),
                ToggleVariable("ending", "chloe", "riley"),
                ToggleVariable("hcGirl", "chloe", "alone")
            ]
        )

        PB_NORA = PathBuilderItem(
            PathBuilderCategories.GIRL,
            "NORA",
            actions=ToggleField(nora, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND)
        )

        PB_AUBREY = PathBuilderItem(
            PathBuilderCategories.GIRL,
            "AUBREY",
            actions=ToggleField(aubrey, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND)
        )

        PB_RILEY = PathBuilderItem(
            PathBuilderCategories.GIRL,
            "RILEY",
            actions=ToggleField(riley, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND)
        )

        PB_LAUREN = PathBuilderItem(
            PathBuilderCategories.GIRL,
            "LAUREN",
            actions=ToggleField(lauren, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND)
        )

        PB_PENELOPE = PathBuilderItem(
            PathBuilderCategories.GIRL,
            "PENELOPE",
            actions=[
                ToggleField(penelope, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND),
                ToggleVariable("v11_pen_goes_europe")
            ]
        )

        PB_AMBER = PathBuilderItem(
            PathBuilderCategories.GIRL,
            "AMBER",
            actions=ToggleField(amber, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND)
        )

        PB_LINDSEY = PathBuilderItem(
            PathBuilderCategories.GIRL,
            "LINDSEY",
            actions=ToggleField(lindsey, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND)
        )

        PB_MS_ROSE = PathBuilderItem(
            PathBuilderCategories.GIRL,
            "MS ROSE",
            actions=ToggleField(ms_rose, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND)
        )

        PB_SAMANTHA = PathBuilderItem(
            PathBuilderCategories.GIRL,
            "SAMANTHA",
            actions=ToggleField(samantha, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND)
        )

        PB_JENNY = PathBuilderItem(
            PathBuilderCategories.GIRL,
            "JENNY",
            actions=ToggleField(jenny, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND)
        )

        PB_EMILY = PathBuilderItem(
            PathBuilderCategories.GIRL,
            "EMILY",
            actions=ToggleField(emily, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND)
        )


        # Start positions
        PB_ACT_1 = PathBuilderItem(
            PathBuilderCategories.START_LOCATION,
            "ACT 1 START",
            actions=SetVariable("pb_start_location", "start")
            )

        PB_HOMECOMING = PathBuilderItem(
            PathBuilderCategories.START_LOCATION,
            "ACT 2 START",
            actions=SetVariable("pb_start_location", "v7_homecoming")
            )

        PB_ACT_3 = PathBuilderItem(
            PathBuilderCategories.START_LOCATION,
            "ACT 3 START",
            actions=SetVariable("pb_start_location", "v11_start")
            )

        PB_ACT_4 = PathBuilderItem(
            PathBuilderCategories.START_LOCATION,
            "ACT 4 START",
            actions=SetVariable("pb_start_location", "v14_start")
            )
        

        #Homecoming dates
        HC_CHLOE = PathBuilderItem(
            PathBuilderCategories.HOMECOMING_DATE,
            "CHLOE", 
            actions=SetVariable("hcGirl", "chloe")
            )

        HC_RILEY = PathBuilderItem(
            PathBuilderCategories.HOMECOMING_DATE,
            "RILEY", 
            actions=SetVariable("hcGirl", "riley")
            )

        HC_LAUREN = PathBuilderItem(
            PathBuilderCategories.HOMECOMING_DATE,
            "LAUREN", 
            actions=SetVariable("hcGirl", "lauren")
            )

        HC_PENELOPE = PathBuilderItem(
            PathBuilderCategories.HOMECOMING_DATE,
            "PENELOPE",
            actions=SetVariable("hcGirl", "penelope")
            )

        HC_AMBER = PathBuilderItem(
            PathBuilderCategories.HOMECOMING_DATE,
            "AMBER",
            actions=SetVariable("hcGirl", "amber")
            )

        HC_EMILY = PathBuilderItem(
            PathBuilderCategories.HOMECOMING_DATE,
            "EMILY",
            actions=SetVariable("hcGirl", "emily")
            )

    return