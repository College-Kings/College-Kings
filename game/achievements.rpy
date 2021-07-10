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
    
    # v8.0
    Achievement("thick_and_thin", "Help Penelope", "thick_and_thin")
    Achievement("text_with_an_s", "Return to sender", "text_with_an_s")
    Achievement("lucky_7", "Flashing lights at the arcade", "lucky_7")
    Achievement("ip_man", "Win The Alley Fight", "ip_man")
    Achievement("get_a_room", "Stay With Amber at Josh's", "get_a_room")
    Achievement("helping_hand", "Help Nora hand out flyers for the trip", "helping_hand")
    Achievement("up_for_more", "Flirt With Chloe", "up_for_more")

    # v9.0
    Achievement("relaxing_day", "Have fun with Aubrey at the lake", "lake_hj")
    Achievement("king_of_the_north", "The King is heading North", "king_of_the_north")
    Achievement("back_down", "Punch the guy in the hallway", "down_for_the_count")
    Achievement("second_date", "Get a second date with Evelyn", "second_date")
    Achievement("cheat_day", "Skip the gym and get with Riley", "cheat_day")
    Achievement("the_wrong_time", "Don't kiss Lindsey", "the_wrong_time")

    # v10.0
    Achievement("lights_out", "Beat Ryan on Hard difficulty at the Brawl", "lights_out")
    Achievement("fright_club", "Don't fight Ryan at the Brawl", "fright_club")
    Achievement("golden_boy", "Beat Imre on Hard difficulty at the Brawl", "golden_boy")
    Achievement("bros_before_blows", "Don't fight Imre at the Brawl", "bros_before_blows")
    Achievement("rawr_im_a_lion!", "Tell Lauren you like Lions", "im_a_lion")
    Achievement("getting_clean", "Have fun in the bathroom", "bathroom_sex")
    Achievement("forbidden_romance", "Kiss Ms. Rose", "kiss_teacher")
    Achievement("rough_rider", "Have fun at the skatepark", "rough_rider")
    Achievement("family_secrets", "Find out Nora and Ms. Rose are family", "family_secrets")
    Achievement("on_the_court", "Have a rematch with Chloe", "on_the_court")
    Achievement("hard_decisions", "Tell Chloe what Nora said", "chloe_over_nora")

    #v11.0
    Achievement("perry_mason", "Successfully defend Penelope", "perry_mason")
    Achievement("candy_crusher", "Candy's sex scene", "candy_crusher")
    Achievement("hold_your_horses", "Balance the horse at the end of the manhunt", "hold_your_horses")
    Achievement("off_your_high_horse", "Don't balance the horse at the end of the manhunt", "off_your_high_horse")
    Achievement("cross_your_heart", "Kiss Penelope at the airport", "cross_your_heart")
    Achievement("on_target", "Hit a bullseye at Duncan's", "on_target")
    Achievement("just_a_theory", "Tell Riley dinosaurs aren't real", "just_a_theory")
    Achievement("fruity", "Have a cocktail at the bar", "fruity")
    Achievement("earn_your_owl", "Get all the HP answers right", "earn_your_owl")
    Achievement("political_strategist", "Tell Autumn you're into politics and encourage Lindsey to run", "political_strategist")
    Achievement("two_timer", "Date both Lauren and Chloe", "two_timer")
    Achievement("dont_just_stand_there", "Break Imre and Ryan apart", "dont_just_stand_there")
    Achievement("pretty_in_pink", "Nora buys the pink bra", "pretty_in_pink")

