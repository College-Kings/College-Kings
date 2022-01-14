label path_builder_setup:
    python:
        PB_WOLVES = PathBuilderItem(
            PathBuilderCategories.FRATERNITY,
            "Wolves",
                actions=[
                    SetVariable(
                        "path_builder",
                        True
                    ),
                    SetVariable(
                        "joinwolves",
                        True
                        )
                    ]
            )

        PB_APES = PathBuilderItem(
            PathBuilderCategories.FRATERNITY,
            "Apes",
                actions=[
                    SetVariable(
                        "path_builder",
                        True
                    ),
                    SetVariable(
                        "joinwolves",
                        False
                        )
                    ]
            )

        PB_LOYAL = PathBuilderItem(
            PathBuilderCategories.KCT,
            "Loyal",
                actions=[
                    SetVariable(
                        "kct",
                        "loyal"
                    ),
                    SetVariable(
                        "bro",
                        2
                    ),
                    SetVariable(
                        "boyfriend",
                        2
                    ),
                    SetVariable(
                        "troublemaker",
                        1
                    )
                ]
        )

        PB_POPULAR = PathBuilderItem(
            PathBuilderCategories.KCT,
            "Popular",
                actions=[
                    SetVariable(
                        "kct",
                        "popular"
                    ),
                    SetVariable(
                        "bro",
                        2
                    ),
                    SetVariable(
                        "boyfriend",
                        1
                    ),
                    SetVariable(
                        "troublemaker",
                        2
                    )
                ]
        )

        PB_CONFIDENT = PathBuilderItem(
            PathBuilderCategories.KCT,
            "Confident",
                actions=[
                    SetVariable(
                        "kct",
                        "confident"
                    ),
                    SetVariable(
                        "bro",
                        1
                    ),
                    SetVariable(
                        "boyfriend",
                        2
                    ),
                    SetVariable(
                        "troublemaker",
                        2
                    )
                ]
        )

        PB_CHLOE = PathBuilderItem(
            PathBuilderCategories.GIRL,
            "Chloe",
                actions=[
                    ToggleField(
                        chloe,
                        "relationship",
                        Relationship.GIRLFRIEND,
                        Relationship.FRIEND
                    ),
                    ToggleVariable(
                        "ending",
                        "chloe",
                        "riley"
                    ),
                    ToggleVariable(
                        "hcGirl",
                        "chloe",
                        "alone"
                        )
                ]
        )

        PB_NORA = PathBuilderItem(
            PathBuilderCategories.GIRL,
            "Nora",
                ToggleField(
                    nora,
                    "relationship",
                    Relationship.GIRLFRIEND,
                    Relationship.FRIEND
                )
        )

        PB_AUBREY = PathBuilderItem(
            PathBuilderCategories.GIRL,
            "Aubrey",
                actions=ToggleField(
                    aubrey,
                    "relationship",
                    Relationship.GIRLFRIEND,
                    Relationship.FRIEND
                )
        )

        PB_RILEY = PathBuilderItem(
            PathBuilderCategories.GIRL,
            "Riley",
                actions=ToggleField(
                    riley,
                    "relationship",
                    Relationship.GIRLFRIEND,
                    Relationship.FRIEND
                )
        )
            
        PB_LAUREN = PathBuilderItem(
            PathBuilderCategories.GIRL,
            "Lauren",
                actions=ToggleField(
                    lauren,
                    "relationship",
                    Relationship.GIRLFRIEND,
                    Relationship.FRIEND
                )
        )

        PB_PENELOPE = PathBuilderItem(
            PathBuilderCategories.GIRL,
            "Penelope",
                actions=[
                    ToggleField(
                        penelope,
                        "relationship",
                        Relationship.GIRLFRIEND,
                        Relationship.FRIEND
                    ),
                    ToggleVariable("v11_pen_goes_europe")
                ]
        )
            
        PB_AMBER = PathBuilderItem(
            PathBuilderCategories.GIRL,
            "Amber",
                actions=ToggleField(
                    amber,
                    "relationship",
                    Relationship.GIRLFRIEND,
                    Relationship.FRIEND
                )
        )

        PB_LINDSEY = PathBuilderItem(
            PathBuilderCategories.GIRL,
            "Lindsey",
                actions=ToggleField(
                    lindsey,
                    "relationship",
                    Relationship.GIRLFRIEND,
                    Relationship.FRIEND
                )
        )

        PB_MS_ROSE = PathBuilderItem(
            PathBuilderCategories.GIRL,
            "Ms Rose",
                actions=ToggleField(
                    ms_rose,
                    "relationship",
                    Relationship.GIRLFRIEND,
                    Relationship.FRIEND
                )
        )
            
        PB_SAMANTHA = PathBuilderItem(
            PathBuilderCategories.GIRL,
            "Samantha",
                actions=ToggleField(
                    samantha,
                    "relationship",
                    Relationship.GIRLFRIEND,
                    Relationship.FRIEND
                )
        )

        PB_JENNY = PathBuilderItem(
            PathBuilderCategories.GIRL,
            "Jenny",
                actions=ToggleField(
                    jenny,
                    "relationship",
                    Relationship.GIRLFRIEND,
                    Relationship.FRIEND
                )
        )

        PB_EMILY = PathBuilderItem(
            PathBuilderCategories.GIRL,
            "Emily",
                actions=ToggleField(
                    emily,
                    "relationship",
                    Relationship.GIRLFRIEND,
                    Relationship.FRIEND
                )
        )


        PB_ACT_1 = PathBuilderItem(
            PathBuilderCategories.START_LOCATION,
            "Act 1 Start",
                actions=SetVariable(
                    "pb_start_location",
                    "start"
                )
            )

        if renpy.loadable("v8/scene1.rpy"):
            PB_HOMECOMING = PathBuilderItem(
                PathBuilderCategories.START_LOCATION,
                "Act 2 Start",
                    actions=SetVariable(
                        "pb_start_location",
                        "v7_homecoming"
                    )
            )
                
        if renpy.loadable("v11/scene1.rpy"):
            PB_ACT_3 = PathBuilderItem(
                PathBuilderCategories.START_LOCATION,
                "Act 3 Start",
                    actions=SetVariable(
                        "pb_start_location",
                        "v11_start"
                    )
            )

        if renpy.loadable("v14/scene1.rpy"):
            PB_ACT_4 = PathBuilderItem(
                PathBuilderCategories.START_LOCATION,
                "Act 4 Start",
                    actions=SetVariable(
                        "pb_start_location",
                        "v14_start"
                    )
            )


        HD_CHLOE = PathBuilderItem(
            PathBuilderCategories.HOMECOMING_DATE,
            "Chloe",
                actions=SetVariable(
                    "hcGirl",
                    "chloe"
                )
        )

        HD_RILEY = PathBuilderItem(
            PathBuilderCategories.HOMECOMING_DATE,
            "Riley",
                actions=SetVariable(
                    "hcGirl",
                    "riley"
                )
        )

        HD_LAUREN = PathBuilderItem(
            PathBuilderCategories.HOMECOMING_DATE,
            "Lauren",
                actions=SetVariable(
                    "hcGirl",
                    "lauren"
                )
        )

        HD_PENELOPE = PathBuilderItem(
            PathBuilderCategories.HOMECOMING_DATE,
            "Penelope",
                actions=SetVariable(
                    "hcGirl",
                    "penelope"
                )
        )

        HD_EMILY = PathBuilderItem(
            PathBuilderCategories.HOMECOMING_DATE,
            "Emily",
                actions=SetVariable(
                    "hcGirl",
                    "emily"
                )
        )

        HD_AMBER = PathBuilderItem(
            PathBuilderCategories.HOMECOMING_DATE,
            "Amber",
                actions=SetVariable(
                    "hcGirl",
                    "amber"
                )
        )

    return