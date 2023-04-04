init python:
    @dataclass
    class PathBuilderCategory:
        categories: ClassVar[list["PathBuilderCategory"]] = []

        name: str
        title: str
        background_image: str

        def __post_init__(self):
            PathBuilderCategory.categories.append(self)


    class PathBuilderItem:
        items: list["PathBuilderItem"] = []

        def __init__(
            self,
            category: PathBuilderCategory,
            name: str,
            actions: Optional[list[Callable[[], None]]] = None,
            version_requirement: int = 0,
        ):
            self.category = category
            self.name = name
            self.version_requirement = version_requirement

            if actions is None:
                self.actions = []
            elif isinstance(actions, list):
                self.actions = actions
            else:
                self.actions = [actions]

            PathBuilderItem.items.append(self)


    class PathBuilderGirl(PathBuilderItem):
        def __init__(
            self,
            girl: NonPlayableCharacter,
            reputation: str,
            frat_requirement: Optional["Frat"] = None,
            version_requirement: int = 0,
            relationships: Optional[list["Relationship"]] = None,
        ):
            PathBuilderItem.__init__(self, PBC_GIRL, girl.name, None, version_requirement)

            self.girl = girl
            self.reputation = reputation
            self.frat_requirement = frat_requirement

            if relationships is None:
                self.relationships: list[Relationship] = []
            elif isinstance(relationships, list):
                self.relationships = relationships
            else:
                self.relationships = [relationships]


    def path_builder_setup():
        PathBuilderItem.items = []

        PB_WOLVES = PathBuilderItem(
            PBC_FRATERNITY,
            "Wolves",
            actions=[SetVariable("path_builder", True), SetVariable("joinwolves", True)]
        )
        PB_APES = PathBuilderItem(
            PBC_FRATERNITY,
            "Apes",
            actions=[SetVariable("path_builder", True), SetVariable("joinwolves", False)]
        )

        PB_LOYAL = PathBuilderItem(
            PBC_REPUTATION,
            "Loyal",
            actions=SetField(reputation, "components", {RepComponent.BRO: 20, RepComponent.BOYFRIEND: 20, RepComponent.TROUBLEMAKER: 10})
        )
        PB_POPULAR = PathBuilderItem(
            PBC_REPUTATION,
            "Popular",
            actions=SetField(reputation, "components", {RepComponent.BRO: 20, RepComponent.BOYFRIEND: 10, RepComponent.TROUBLEMAKER: 20})
        )
        PB_CONFIDENT = PathBuilderItem(
            PBC_REPUTATION,
            "Confident",
            actions=SetField(reputation, "components", {RepComponent.BRO: 10, RepComponent.BOYFRIEND: 20, RepComponent.TROUBLEMAKER: 20})
        )

        PB_CHLOE = PathBuilderGirl(
            chloe,
            "Popular",
            relationships=[Relationship.FRIEND, Relationship.FWB, Relationship.GIRLFRIEND]
        )
        PB_NORA = PathBuilderGirl(
            nora,
            "Loyal",
            relationships=[Relationship.FRIEND, Relationship.FWB, Relationship.GIRLFRIEND]
        )
        PB_AUBREY = PathBuilderGirl(
            aubrey,
            "Popular",
            relationships=[Relationship.MAD, Relationship.FRIEND, Relationship.FWB, Relationship.GIRLFRIEND]
        )
        PB_RILEY = PathBuilderGirl(
            riley,
            "Confident",
            relationships=[Relationship.FRIEND, Relationship.FWB]
        )
        PB_LAUREN = PathBuilderGirl(
            lauren,
            "Loyal",
            relationships=[Relationship.MAD, Relationship.FRIEND, Relationship.KISS, Relationship.FWB, Relationship.GIRLFRIEND]
        )
        PB_PENELOPE = PathBuilderGirl(
            penelope,
            "Confident",
            relationships=[Relationship.FRIEND, Relationship.LIKES, Relationship.LOYAL]
        )
        PB_AMBER = PathBuilderGirl(
            amber,
            "Popular",
            relationships=[Relationship.FRIEND, Relationship.FWB]
        )
        PB_LINDSEY = PathBuilderGirl(
            lindsey,
            "Popular",
            relationships=[Relationship.FRIEND, Relationship.FWB]
        )
        PB_MS_ROSE = PathBuilderGirl(
            ms_rose,
            "Confident",
            frat_requirement=Frat.WOLVES,
            relationships=[Relationship.THREATEN, Relationship.FRIEND, Relationship.FWB]
        )
        PB_SAMANTHA = PathBuilderGirl(
            samantha,
            "Loyal",
            frat_requirement=Frat.APES,
            relationships=[Relationship.FRIEND, Relationship.MOVE, Relationship.FWB]
        )
        PB_JENNY = PathBuilderGirl(
            jenny,
            "Popular",
            relationships=[Relationship.FRIEND, Relationship.FWB]
        )
        PB_EMILY = PathBuilderGirl(
            emily,
            "Loyal",
            relationships=[Relationship.FRIEND, Relationship.FWB]
        )
        # PB_AUTUMN = PathBuilderGirl(
        #     autumn,
        #     "Loyal",
        #     relationships=[Relationship.FRIEND, Relationship.KISS, Relationship.LOYAL]
        # )
                    
        PB_ACT_1_PART_1 = PathBuilderItem(PBC_START_LOCATION, "Act 1 Start", actions=[SetScreenVariable("start_label", "start"), SetScreenVariable("version_number", 1)])
        PB_ACT_1_PART_2 = PathBuilderItem(PBC_START_LOCATION, "Act 2 Start", actions=[SetScreenVariable("start_label", "v7_homecoming"), SetScreenVariable("version_number", 2)])
        PB_ACT_1_PART_3 = PathBuilderItem(PBC_START_LOCATION, "Act 3 Start", actions=[SetScreenVariable("start_label", "v11_start"), SetScreenVariable("version_number", 3)])

        HC_CHLOE = PathBuilderItem(
            PBC_HOMECOMING_DATE,
            _("Chloe"),
            actions=ToggleVariable("hcGirl", "chloe"), version_requirement=2)
        HC_RILEY = PathBuilderItem(
            PBC_HOMECOMING_DATE,
            _("Riley"),
            actions=ToggleVariable("hcGirl", "riley"), version_requirement=2)
        HC_LAUREN = PathBuilderItem(
            PBC_HOMECOMING_DATE,
            _("Lauren"),
            actions=ToggleVariable("hcGirl", "lauren"), version_requirement=2)
        HC_PENELOPE = PathBuilderItem(
            PBC_HOMECOMING_DATE,
            _("Penelope"),
            actions=ToggleVariable("hcGirl", "penelope"), version_requirement=2)
        HC_EMILY = PathBuilderItem(
            PBC_HOMECOMING_DATE,
            _("Emily"),
            actions=ToggleVariable("hcGirl", "emily"), version_requirement=2)
        HC_AMBER = PathBuilderItem(
            PBC_HOMECOMING_DATE,
            _("Amber"),
            actions=ToggleVariable("hcGirl", "amber"), version_requirement=2)


define PBC_START_LOCATION = PathBuilderCategory("Start Location", "Pick your starting location", "main_menu/path_builder/images/path_builder_step_1.webp") 
define PBC_REPUTATION = PathBuilderCategory("Reputation", "Pick your starting reputation", "main_menu/path_builder/images/path_builder_step_2.webp") 
define PBC_FRATERNITY = PathBuilderCategory("Fraternity", "Pick a fraternity", "main_menu/path_builder/images/path_builder_step_3.webp") 
define PBC_GIRL = PathBuilderCategory("Girls", "Pick which girls you want to be romantically involved with", "main_menu/path_builder/images/path_builder_step_4.webp") 
define PBC_HOMECOMING_DATE = PathBuilderCategory("Homecoming Date", "Pick your homecoming date", "main_menu/path_builder/images/path_builder_step_5.webp")
