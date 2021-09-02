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
    
    # v8.0
    Achievement("thick_and_thin", "Help Penelope")
    Achievement("text_with_an_s", "Return to sender")
    Achievement("lucky_7", "Flashing lights at the arcade")
    Achievement("ip_man", "Win The Alley Fight")
    Achievement("get_a_room", "Stay With Amber at Josh's")
    Achievement("helping_hand", "Help Nora hand out flyers for the trip")
    Achievement("up_for_more", "Flirt With Chloe")

    # v9.0
    Achievement("relaxing_day", "Have fun with Aubrey at the lake")
    Achievement("king_of_the_north", "The King is heading North")
    Achievement("back_down", "Punch the guy in the hallway")
    Achievement("second_date", "Get a second date with Evelyn")
    Achievement("cheat_day", "Skip the gym and get with Riley")
    Achievement("the_wrong_time", "Don't kiss Lindsey")

    # v10.0
    Achievement("lights_out", "Beat Ryan on Hard difficulty at the Brawl")
    Achievement("fright_club", "Don't fight Ryan at the Brawl")
    Achievement("golden_boy", "Beat Imre on Hard difficulty at the Brawl")
    Achievement("bros_before_blows", "Don't fight Imre at the Brawl")
    Achievement("rawr_im_a_lion!", "Tell Lauren you like Lions")
    Achievement("getting_clean", "Have fun in the bathroom")
    Achievement("forbidden_romance", "Kiss Ms. Rose")
    Achievement("rough_rider", "Have fun at the skatepark")
    Achievement("family_secrets", "Find out Nora and Ms. Rose are family")
    Achievement("on_the_court", "Have a rematch with Chloe")
    Achievement("hard_decisions", "Tell Chloe what Nora said")

    #v11.0
    Achievement("perry_mason", "Successfully defend Penelope")
    Achievement("candy_crusher", "Candy's sex scene")
    Achievement("hold_your_horses", "Balance the horse at the end of the manhunt")
    Achievement("off_your_high_horse", "Don't balance the horse at the end of the manhunt")
    Achievement("cross_your_heart", "Kiss Penelope at the airport")
    Achievement("on_target", "Hit a bullseye at Duncan's")
    Achievement("just_a_theory", "Tell Riley dinosaurs aren't real")
    Achievement("fruity", "Have a cocktail at the bar")
    Achievement("earn_your_owl", "Get all the HP answers right",)
    Achievement("political_strategist", "Tell Autumn you're into politics and encourage Lindsey to run")
    Achievement("two_timer", "Date both Lauren and Chloe")
    Achievement("dont_just_stand_there", "Break Imre and Ryan apart")
    Achievement("pretty_in_pink", "Nora buys the pink bra")

    #v12.0
    Achievement("good_vs_evil", "Penelope understands you")
    Achievement("a_person_like_me", "You see yourself as Penelope’s husband material")
        # Murder Mystery Achievements
    Achievement("zero_to_hero", "Tell Riley you are poor")
    Achievement("doctors_orders", "Accept Nurse Aubrey's advances")
    Achievement("mercy_killing", "Kill Imre")
    Achievement("talk_murder_to_me", "Kill Samantha")
    Achievement("best_for_last", "Charli is your final kill")
    Achievement("weapons_down", "Don't kill anyone")
    Achievement("killing_spree", "Kill enough people to win the game")
    Achievement("mass_casualties", "Kill everyone (including optional characters)")
        #Back to v12
    Achievement("throw_her_to_the_lions", "Encourage Lindsey to run but then tell Aubrey and Chloe about it")
    Achievement("you_may_kiss_the_bride", "Kiss Nora at the altar")
    Achievement("a_bet_is_a_bet", "Embarrassing Kiwii picture for losing the race")
    Achievement("brotherhood_of_men", "Defend Chris every time as a Wolf")
    Achievement("best_frenemies", "Defend Chris every time as an Ape")
    Achievement("worth_the_wait", "Consummate an exclusive relationship with Lauren")
    Achievement("inside_job", "Have sex with Nora as a Wolf")
    Achievement("all_is_fair_in_love_and_war", "Have sex with Nora as an Ape")
    Achievement("city_of_love", "Have sex with Lauren, Nora, Ms. Rose and Lindsey")