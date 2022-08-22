init python:
    def path_builder_setup():
        PathBuilderItem.items = []

        PB_WOLVES = PathBuilderItem(
            PathBuilderCatagories.FRATERNITY,
            _("Wolves"),
            actions=[SetVariable("path_builder", True), SetVariable("joinwolves", True)],
        )
        PB_APES = PathBuilderItem(
            PathBuilderCatagories.FRATERNITY,
            _("Apes"),
            actions=[SetVariable("path_builder", True), SetVariable("joinwolves", False)],
        )

        PB_LOYAL = PathBuilderItem(
            PathBuilderCatagories.KCT,
            _("Loyal"),
            actions=[
                SetVariable("kct", "loyal"),
                SetVariable("bro", 2),
                SetVariable("boyfriend", 2),
                SetVariable("troublemaker", 1),
            ],
        )
        PB_POPULAR = PathBuilderItem(
            PathBuilderCatagories.KCT,
            _("Popular"),
            actions=[
                SetVariable("kct", "popular"),
                SetVariable("bro", 2),
                SetVariable("boyfriend", 1),
                SetVariable("troublemaker", 2),
            ],
        )
        PB_CONFIDENT = PathBuilderItem(
            PathBuilderCatagories.KCT,
            _("Confident"),
            actions=[
                SetVariable("kct", "confident"),
                SetVariable("bro", 1),
                SetVariable("boyfriend", 2),
                SetVariable("troublemaker", 2),
            ],
        )

        PB_CHLOE = PathBuilderGirl(
            chloe,
            _("Popular"),
            actions=[
                ToggleField(
                    chloe, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND
                ),
                ToggleVariable("meetchloe"),
                ToggleVariable("ending", "chloe", "riley"),
                ToggleVariable("hcGirl", "chloe", "alone"),
            ],
        )
        PB_NORA = PathBuilderGirl(
            nora,
            _("Loyal/Confident"),
            ToggleField(nora, "relationship", Relationship.FWB, Relationship.FRIEND),
        )
        PB_AUBREY = PathBuilderGirl(
            aubrey,
            _("Popular"),
            actions=ToggleField(aubrey, "relationship", Relationship.FWB, Relationship.FRIEND),
        )
        PB_RILEY = PathBuilderGirl(
            riley,
            _("Confident"),
            actions=ToggleField(riley, "relationship", Relationship.FWB, Relationship.FRIEND),
        )
        PB_LAUREN = PathBuilderGirl(
            lauren,
            _("Loyal"),
            actions=ToggleField(
                lauren, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND
            ),
        )
        PB_PENELOPE = PathBuilderGirl(
            penelope,
            _("Confident"),
            actions=[
                ToggleField(penelope, "relationship", Relationship.LOYAL, Relationship.FRIEND),
                ToggleVariable("v11_pen_goes_europe"),
            ],
        )
        PB_AMBER = PathBuilderGirl(
            amber,
            _("Popular"),
            actions=ToggleField(amber, "relationship", Relationship.FWB, Relationship.FRIEND),
        )
        PB_LINDSEY = PathBuilderGirl(
            lindsey,
            _("Popular"),
            actions=ToggleField(lindsey, "relationship", Relationship.FWB, Relationship.FRIEND),
        )
        PB_MS_ROSE = PathBuilderGirl(
            ms_rose,
            _("Confident"),
            actions=ToggleField(ms_rose, "relationship", Relationship.FWB, Relationship.FRIEND),
            frat_requirement=Frat.WOLVES,
        )
        PB_SAMANTHA = PathBuilderGirl(
            samantha,
            _("Loyal"),
            actions=ToggleField(
                samantha, "relationship", Relationship.FWB, Relationship.FRIEND
            ),
            frat_requirement=Frat.APES,
        )
        PB_JENNY = PathBuilderGirl(
            jenny,
            _("Popular"),
            actions=ToggleField(jenny, "relationship", Relationship.FWB, Relationship.FRIEND),
        )

        PB_EMILY = PathBuilderGirl(
            emily,
            _("Loyal"),
            actions=[
                ToggleField(emily, "relationship", Relationship.FWB, Relationship.FRIEND),
                ToggleVariable("emily_europe"),
                ToggleVariable("v14_emily_ily"),
            ],
        )

        PB_ACT_1 = PathBuilderItem(
            PathBuilderCatagories.START_LOCATION,
            _("Act 1 Start"),
            actions=[
                SetScreenVariable("start_label", "start"),
                SetScreenVariable("act_number", 1),
            ],
        )
        PB_ACT_2 = PathBuilderItem(
            PathBuilderCatagories.START_LOCATION,
            _("Act 2 Start"),
            actions=[
                SetScreenVariable("start_label", "v7_homecoming"),
                SetScreenVariable("act_number", 2),
            ],
        )
        PB_ACT_3 = PathBuilderItem(
            PathBuilderCatagories.START_LOCATION,
            _("Act 3 Start"),
            actions=[
                SetScreenVariable("start_label", "v11_start"),
                SetScreenVariable("act_number", 3),
            ],
        )

        HC_CHLOE = PathBuilderItem(
            PathBuilderCatagories.HOMECOMING_DATE,
            _("Chloe"),
            actions=ToggleVariable("hcGirl", "chloe"),
        )
        HC_RILEY = PathBuilderItem(
            PathBuilderCatagories.HOMECOMING_DATE,
            _("Riley"),
            actions=ToggleVariable("hcGirl", "riley"),
        )
        HC_LAUREN = PathBuilderItem(
            PathBuilderCatagories.HOMECOMING_DATE,
            _("Lauren"),
            actions=ToggleVariable("hcGirl", "lauren"),
        )
        HC_PENELOPE = PathBuilderItem(
            PathBuilderCatagories.HOMECOMING_DATE,
            _("Penelope"),
            actions=ToggleVariable("hcGirl", "penelope"),
        )
        HC_EMILY = PathBuilderItem(
            PathBuilderCatagories.HOMECOMING_DATE,
            _("Emily"),
            actions=ToggleVariable("hcGirl", "emily"),
        )
        HC_AMBER = PathBuilderItem(
            PathBuilderCatagories.HOMECOMING_DATE,
            _("Amber"),
            actions=ToggleVariable("hcGirl", "amber"),
        )
