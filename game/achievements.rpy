init python:
    achievements = []

    class Achievement:
        """
        Achievement data class for storing and managing the creation, syncing and managing of in-game achievements

        Args:
            _achievement (str): Programic name for the achievement
            text (str): Short description of achievement
        """

        def __init__(self, _achievement, text):
            self.achievement = _achievement
            self.text = text

            self.display_name = _achievement.replace("_", " ")

            achievements.append(self)

            # Add achievements to renpy/steam
            achievement.register(_achievement)
            achievement.sync()

        def checkCondition(self):
            return getattr(store, self.condition)

# ACHIEVEMENT ITEMS HERE
    # v1.0
    Achievement("open_wound", "Tell off Emily")
    Achievement("no_hard_feelings", "Play nice with Emily")
    Achievement("keep_it_moving", "Hit on Nora")
    Achievement("romeo", "Kiss Lauren")
    Achievement("big_mouth", "Threaten Cameron")

    # v2.0
    Achievement("mixed_feelings", "Decline Lauren")
    Achievement("the_notorious", "Win your first fight")
    Achievement("a_new beginning", "Lauren likes you")
    Achievement("over_it", "Let Benjamin make a move")

    # v3.0
    Achievement("not_now_mom", "Decline Julia's call")
    Achievement("lips_dont_lie", "Kiss Riley in the Park")
    Achievement("truth_hurts", "Tell Lauren about Aubrey")

    # v4.0
    Achievement("relight_the_fire", "Tell Julia about Emily")
    Achievement("rematch", "Buy Chloe the volleyball")
    Achievement("keen_eye", "Pick the muffin")
    
    # v5.0
    Achievement("on_the_low", "Deny PDA with Lauren")
    Achievement("peta_public_enemy", "Kill dog as animal lover")
    Achievement("snitch", "Tell the school")

    # v6.0
    Achievement("bros_before_hoes", "Help Imre")
    Achievement("monkey_business", "Join the Apes")
    Achievement("not_my_business", "Don't disturb Ms. Rose")
    Achievement("reignition", "Kiss Emily back")
    Achievement("credulous", "Trust Chloe")
    Achievement("seems_fishy", "Don't meet Grayson")
    Achievement("strike", "Kiss Penelope")

    # v7.0
    Achievement("true_to_self", "Walk home with Riley")
    Achievement("silverback", "Pledge to the Apes")
    Achievement("wolfpack", "Pledge to the Wolves")
    Achievement("lee_way", "Pull down Mr. Lee's pants")
    Achievement("ecstatic", "Bunk homecoming with Amber")
    Achievement("slow_and_steady", "End homecoming with Lauren")
    Achievement("playing_with_fire", "End homecoming with Riley")
    Achievement("homecoming_queen", "End homecoming with Chloe")
