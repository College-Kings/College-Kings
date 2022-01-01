label before_main_menu:
    python:
        # Path Builder Setup
        PB_WOLVES = PathBuilderItem(
            PathBuilderCatagories.FRATERNITY,
            "Wolves",
            [SetVariable("path_builder", True), SetVariable("joinwolves", True)])
        PB_APES = PathBuilderItem(
            PathBuilderCatagories.FRATERNITY,
            "Apes",
            [SetVariable("path_builder", True), SetVariable("joinwolves", False)])

        PB_LOYAL = PathBuilderItem(
            PathBuilderCatagories.KCT,
            "Loyal",
            [SetVariable("kct", "loyal"), SetVariable("bro", 2), SetVariable("boyfriend", 2), SetVariable("troublemaker", 1)])
        PB_POPULAR = PathBuilderItem(
            PathBuilderCatagories.KCT,
            "Popular",
            [SetVariable("kct", "popular"), SetVariable("bro", 2), SetVariable("boyfriend", 1), SetVariable("troublemaker", 2)])

        PB_CONFIDENT = PathBuilderItem(
            PathBuilderCatagories.KCT,
            "Confident",
            [SetVariable("kct", "confident"), SetVariable("bro", 1), SetVariable("boyfriend", 2), SetVariable("troublemaker", 2)])

        PB_CHLOE = PathBuilderItem(PathBuilderCatagories.GIRL, "Chloe",
            [ToggleField(chloe, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND),
            ToggleVariable("ending", "chloe", "riley"),
            ToggleVariable("hcGirl", "chloe", "alone")])
        PB_NORA = PathBuilderItem(PathBuilderCatagories.GIRL, "Nora",
            ToggleField(nora, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
        PB_AUBREY = PathBuilderItem(PathBuilderCatagories.GIRL, "Aubrey",
            ToggleField(aubrey, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
        PB_RILEY = PathBuilderItem(PathBuilderCatagories.GIRL, "Riley",
            ToggleField(riley, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
        PB_LAUREN = PathBuilderItem(PathBuilderCatagories.GIRL, "Lauren",
            ToggleField(lauren, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
        PB_PENELOPE = PathBuilderItem(PathBuilderCatagories.GIRL, "Penelope",
            [ToggleField(penelope, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND),
            ToggleVariable("v11_pen_goes_europe")])
        PB_AMBER = PathBuilderItem(PathBuilderCatagories.GIRL, "Amber",
            ToggleField(amber, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
        PB_LINDSEY = PathBuilderItem(PathBuilderCatagories.GIRL, "Lindsey",
            ToggleField(lindsey, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
        PB_MS_ROSE = PathBuilderItem(PathBuilderCatagories.GIRL, "Ms Rose",
            ToggleField(ms_rose, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
        PB_SAMANTHA = PathBuilderItem(PathBuilderCatagories.GIRL, "Samantha",
            ToggleField(samantha, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
        PB_JENNY = PathBuilderItem(PathBuilderCatagories.GIRL, "Jenny",
            ToggleField(jenny, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))
        PB_EMILY = PathBuilderItem(PathBuilderCatagories.GIRL, "Emily",
            ToggleField(emily, "relationship", Relationship.GIRLFRIEND, Relationship.FRIEND))

        PB_ACT_1 = PathBuilderItem(PathBuilderCatagories.START_LOCATION, "Act 1 Start", SetVariable("pb_start_location", "start"))
        PB_HOMECOMING = PathBuilderItem(PathBuilderCatagories.START_LOCATION, "Act 2 Start", SetVariable("pb_start_location", "v7_homecoming"))
        PB_ACT_3 = PathBuilderItem(PathBuilderCatagories.START_LOCATION, "Act 3 Start", SetVariable("pb_start_location", "v11_start"))
        PB_ACT_4 = PathBuilderItem(PathBuilderCatagories.START_LOCATION, "Act 4 Start", SetVariable("pb_start_location", "v14_start"))


        # Phone Setup
        phone.applications.append(messenger)
        phone.applications.append(stats_app)
        phone.applications.append(achievement_app)
        phone.applications.append(kiwii)
        phone.applications.append(simplr_app)


        # Set up murder mystery stats
        chloe.stats["Competitive"] = True
        chloe.stats["Vindictive"] = [nora]

        amber.stats["Competitive"] = amber.stats["Talkative"] = True
        amber.stats["Vindictive"] = [riley]

        riley.stats["Competitive"] = riley.stats["Talkative"] = True

        lindsey.stats["Competitive"] = lindsey.stats["Talkative"] = True
        lindsey.stats["Vindictive"] = [chloe]

        emily.stats["Talkative"] = False

        nora.stats["Talkative"] = True
        nora.stats["Vindictive"] = [chris, chloe]

        aubrey.stats["Competitive"] = True

        ryan.stats["Vindictive"] = [imre]

        imre.stats["Competitive"] = False
        imre.stats["Vindictive"] = [ryan]

        chris.stats["Competitive"] = chris.stats["Talkative"] = False

        charli.stats["Competitive"] = True
        charli.stats["Talkative"] = False

        josh.stats["Competitive"] = True

    return