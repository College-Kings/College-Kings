init python:
    achievements = []

    class Achievement:
        def __init__(self, achieve, text, condition):
            self.achieve = achieve
            self.text = text
            self.condition = condition

            achievements.append(self)

            # Add achievements to renpy/steam
            achievement.register(achieve.replace(" ", "_"))
            achievement.sync()

        def checkCondition(self):
            return getattr(store, self.condition)

# ACHIEVEMENT ITEMS HERE
    # v1.0
    Achievement("open_wound", "Tell off Emily", "openwound")
    Achievement("no_hard_feelings", "Play nice with Emily", "nohardfeelings")
    Achievement("keep_it_moving", "Hit on Nora", "keepitmoving")
    Achievement("romeo", "Kiss Lauren", "romeo")
    Achievement("big_mouth", "Threaten Cameron", "bigmouth")

    # v2.0
    Achievement("mixed_feelings", "Decline Lauren", "mixedfeelings")
    Achievement("the_notorious", "Win your first fight", "thenotorious")
    Achievement("a_new beginning", "Lauren likes you", "anewbeginning")
    Achievement("over_it", "Let Benjamin make a move", "overit")

    # v3.0
    Achievement("not_now_mom", "Decline Julia's call", "notnowmom")
    Achievement("lips_dont_lie", "Kiss Riley in the Park", "lipsdontlie")
    Achievement("truth_hurts", "Tell Lauren about Aubrey", "truthhurts")

    # v4.0
    Achievement("relight_the_fire", "Tell Julia about Emily", "relightthefire")
    Achievement("rematch", "Buy Chloe the volleyball", "rematch")
    Achievement("keen_eye", "Pick the muffin", "keeneye")
    
    # v5.0
    Achievement("on_the_low", "Deny PDA with Lauren", "onthelow")
    Achievement("peta_public_enemy", "Kill dog as animal lover", "petapublicenemy")
    Achievement("snitch", "Tell the school", "snitch")

    # v6.0
    Achievement("bros_before_hoes", "Help Imre", "brosbeforehoes")
    Achievement("monkey_business", "Join the Apes", "monkeybusiness")
    Achievement("not_my_business", "Don't disturb Ms. Rose", "notmybusiness")
    Achievement("reignition", "Kiss Emily back", "reignition")
    Achievement("credulous", "Trust Chloe", "credulous")
    Achievement("seems_fishy", "Don't meet Grayson", "seemsfishy")
    Achievement("strike", "Kiss Penelope", "strike")

    # v7.0
    Achievement("true_to_self", "Walk home with Riley", "truetoself")
    Achievement("silverback", "Pledge to the Apes", "silverback")
    Achievement("wolfpack", "Pledge to the Wolves", "wolfpack")
    Achievement("lee_way", "Pull down Mr. Lee's pants", "leeway")
    Achievement("ecstatic", "Bunk homecoming with Amber", "ecstatic")
    Achievement("slow_and_steady", "End homecoming with Lauren", "slowandsteady")
    Achievement("playing_with_fire", "End homecoming with Riley", "playingwithfire")
    Achievement("homecoming_queen", "End homecoming with Chloe", "homecomingqueen")
