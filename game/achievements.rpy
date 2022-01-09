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


    def grant_achievement(_achievement):
        if path_builder or _in_replay:
            return
            
        try:
            renpy.show(_achievement, at_list=achievementAtList)
        except TypeError: pass
        achievement.grant(_achievement) 
        achievement.sync()


# ACHIEVEMENT ITEMS HERE
    
    # v1
    if renpy.loadable("v1/v1.rpy"):
        Achievement("open_wound", "Tell off Emily")
        Achievement("no_hard_feelings", "Play nice with Emily")
        Achievement("keep_it_moving", "Hit on Nora")
        Achievement("romeo", "Kiss Lauren")
        Achievement("big_mouth", "Threaten Cameron")

    # v2
    if renpy.loadable("v2/v2.rpy"):
        Achievement("mixed_feelings", "Decline Lauren")
        Achievement("the_notorious", "Win your first fight")
        Achievement("a_new_beginning", "Lauren likes you")
        Achievement("over_it", "Let Benjamin make a move")

    # v3
    if renpy.loadable("v3/v3.rpy"):
        Achievement("not_now_mom", "Decline Julia's call")
        Achievement("lips_dont_lie", "Kiss Riley in the Park")
        Achievement("truth_hurts", "Tell Lauren about Aubrey")

    # v4
    if renpy.loadable("v4/v4.rpy"):
        Achievement("relight_the_fire", "Tell Julia about Emily")
        Achievement("rematch", "Buy Chloe the volleyball")
        Achievement("keen_eye", "Pick the muffin")
    
    # v5
    if renpy.loadable("v5/v5.rpy"):
        Achievement("on_the_low", "Deny PDA with Lauren")
        Achievement("peta_public_enemy", "Kill dog as animal lover")
        Achievement("snitch", "Tell the school")

    # v6
    if renpy.loadable("v6/v6.rpy"):
        Achievement("bros_before_hoes", "Help Imre")
        Achievement("monkey_business", "Join the Apes")
        Achievement("not_my_business", "Don't disturb Ms. Rose")
        Achievement("reignition", "Kiss Emily back")
        Achievement("credulous", "Trust Chloe")
        Achievement("seems_fishy", "Don't meet Grayson")
        Achievement("strike", "Kiss Penelope")

    # v7
    if renpy.loadable("v7/v7.rpy"):
        Achievement("true_to_self", "Walk home with Riley")
        Achievement("silverback", "Pledge to the Apes")
        Achievement("wolfpack", "Pledge to the Wolves")
        Achievement("lee_way", "Pull down Mr. Lee's pants")
        Achievement("ecstatic", "Bunk homecoming with Amber")
        Achievement("slow_and_steady", "End homecoming with Lauren")
        Achievement("playing_with_fire", "End homecoming with Riley")
        Achievement("homecoming_queen", "End homecoming with Chloe")
    
    # v8
    if renpy.loadable("v8/scene1.rpy"):
        Achievement("thick_and_thin", "Help Penelope")
        Achievement("text_with_an_s", "Return to sender")
        Achievement("lucky_7", "Flashing lights at the arcade")
        Achievement("ip_man", "Win the alley fight")
        Achievement("get_a_room", "Stay with Amber at Josh's")
        Achievement("helping_hand", "Help Nora hand out flyers for the trip")
        Achievement("up_for_more", "Flirt with Chloe at the Steakhouse")

    # v9
    if renpy.loadable("v9/scene01.rpy"):
        Achievement("relaxing_day", "Have fun with Aubrey at the lake")
        Achievement("king_of_the_north", "The King is heading North")
        Achievement("back_down", "Punch the guy in the hallway")
        Achievement("second_date", "Get a second date with Evelyn")
        Achievement("cheat_day", "Skip the gym and get with Riley")
        Achievement("the_wrong_time", "Don't kiss Lindsey")

    # v10
    if renpy.loadable("v10/scene1.rpy"):
        Achievement("lights_out", "Beat Ryan on Hard difficulty at the Brawl")
        Achievement("fright_club", "Don't fight Ryan at the Brawl")
        Achievement("golden_boy", "Beat Imre on Hard difficulty at the Brawl")
        Achievement("bros_before_blows", "Don't fight Imre at the Brawl")
        Achievement("rawr_im_a_lion", "Tell Lauren you like Lions")
        Achievement("getting_clean", "Have fun in the bathroom")
        Achievement("forbidden_romance", "Kiss Ms. Rose")
        Achievement("rough_rider", "Have fun at the skatepark")
        Achievement("family_secrets", "Find out Nora and Ms. Rose are family")
        Achievement("on_the_court", "Have a rematch with Chloe")
        Achievement("hard_decisions", "Tell Chloe what Nora said")

    #v11
    if renpy.loadable("v11/scene1.rpy"):
        Achievement("perry_mason", "Successfully defend Penelope")
        Achievement("candy_crusher", "Candy's sex scene")
        Achievement("hold_your_horses", "Balance the horse at the end of the manhunt")
        Achievement("off_your_high_horse", "Don't balance the horse at the end of the manhunt")
        Achievement("cross_your_heart", "Kiss Penelope at the airport")
        Achievement("on_target", "Hit a bullseye at Duncan's")
        Achievement("just_a_theory", "Tell Riley dinosaurs aren't real")
        Achievement("fruity", "Have a cocktail at the bar")
        Achievement("earn_your_owl", "Get all the HP answers right")
        Achievement("political_strategist", "Tell Autumn you're into politics and encourage Lindsey to run")
        Achievement("two_timer", "Date both Lauren and Chloe")
        Achievement("dont_just_stand_there", "Break Imre and Ryan apart")
        Achievement("pretty_in_pink", "Nora buys the pink bra")

    #v12
    if renpy.loadable("v12/scene1.rpy"):
        Achievement("good_vs_evil", "Penelope understands you")
        Achievement("a_person_like_me", "You see yourself as Penelope's husband material")
        Achievement("zero_to_hero", "Tell Riley you are poor")
        Achievement("doctors_orders", "Accept Nurse Aubrey's advances")
        Achievement("mercy_killing", "Kill Imre")
        Achievement("talk_murder_to_me", "Kill Samantha")
        Achievement("best_for_last", "Charli is your final kill")
        Achievement("weapons_down", "Don't kill anyone")
        Achievement("killing_spree", "Kill enough people to win the game")
        Achievement("mass_casualties", "Kill everyone (including optional characters)")
        Achievement("thrown_to_the_lions", "Encourage Lindsey to run but then tell Aubrey and Chloe about it")
        Achievement("you_may_kiss_the_bride", "Kiss Nora at the altar")
        Achievement("a_bet_is_a_bet", "Embarrassing Kiwii picture for losing the race")
        Achievement("brotherhood_of_men", "Defend Chris every time as a Wolf")
        Achievement("best_frenemies", "Defend Chris every time as an Ape")
        Achievement("worth_the_wait", "Consummate an exclusive relationship with Lauren")
        Achievement("inside_job", "Have sex with Nora as a Wolf")
        Achievement("all_is_fair_in_love_and_war", "Have sex with Nora as an Ape")
        Achievement("city_of_love", "Have sex with Lauren, Nora, Ms. Rose and Lindsey")
    
    #v13
    if renpy.loadable("v13/scene1.rpy"):
        Achievement("indecisive", "Help neither Chloe nor Lindsey")
        Achievement("funny_night", "Yes Penelope, you're flying")
        Achievement("gentlemen_prefer_gingers", "Bail on Lauren's cuddles")
        Achievement("flush_flush", "Flush Charli's toothbrush")
        Achievement("he_is_done", "Expose Charli")
        Achievement("urbanizer_womanizer", "Tell Emmy and Lauren you're a city man")
        Achievement("romantic_heart", "Score a date with Kourtney")
        Achievement("bro_moment", "Cameron recognizes your pure intentions")
        Achievement("an_honest_liar", "Own up to Clipps")
        Achievement("we_like_them_wild", "Reveal a new side of Chloe")
        Achievement("voyeur", "What are they doing over there?")
        Achievement("dammit_emily", "Angry bathroom sex")
        Achievement("calm_down_big_fella", "Respect Nora")

    #v14
    if renpy.loadable("v14/scene1.rpy"):
        Achievement("ready_player_three", "Three-way with Riley and Aubrey")
        Achievement("saving_ryans_privates", "Don't let Ryan catch an STD")
        Achievement("beastie_boy", "Sabotage the bake sale")
        Achievement("double_agent", "Help both Chloe and Lindsey's campaigns")
        Achievement("agree_to_disagree", "Chris does not help Chloe")
        Achievement("how_did_you_know", "Buy Amber her favourite candy")
        Achievement("built_on_trust", "Trust your girlfriend Chloe with her ex")
        Achievement("wrath_of_pen", "Penelope makes a scene at the restaurant")
        Achievement("your_eyelids_are_heavy", "Lauren uses her hypnosis powers for good")
        Achievement("say_chirp", "Take a photo with the bird")
        Achievement("grand_theft_chloe", "Steal the diary and all the money")
        Achievement("clean_it_up", "Be a positive influence on Amber and Samantha")
    
    #v15
    if renpy.loadable("v15/scene1.rpy"):
        Achievement("horn_dog", "Peek on Autumn") #s4
        Achievement("da_ba_dee_da_ba_dai", "I'm Blue") #s4
        Achievement("counter_intelligence", "Lindsey was expecting that strategy") #s12
        Achievement("mmmm_donut", "Eat the donut") #s13
        Achievement("honey_bear", "Lick Ms. Rose's pancakes") #s15
        Achievement("pumpkin_season", "You really like that pumpkin, huh?") #s18
        Achievement("childhood_memories", "Surprise the birthday girl") #s18
        Achievement("taskmaster", "Clear the checklist") #s18
        Achievement("too_much_information", "Check your meeting notes often") #s21
        Achievement("emotional_blackmail", "Threaten Ms. Rose") #s21
        Achievement("karen", "Where is your manager?!") #s24
        Achievement("polycurious", "Monogamy is overrated") #s26
        Achievement("what_goes_around", "Aubrey tastes her own medicine at the wedding") #s33
        Achievement("just_one_more_thing", "Find all the clues and crack the case") #s46