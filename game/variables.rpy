#region Init
define is_CK2 = False
define flash = Fade(.25, 0, .75, color="#fff")
define config.default_music_volume = 1
define config.default_sfx_volume = 1
default menu_set = set()

default is_censored = False
default label_history = []
default name = _("Alex")
default real_life_mode = False
default showkct = True
default checklist = Checklist()

# Recap 
default recap_first_run = True # used by the ending scene for each girl narraitive to determine if to return to the recap_girl_summary or to continue to the next girl. Jenny's last scene changes this to false.
default girl_info = {} # Empty
default recap_choose_threesome = False # True = During Aubrey or Riley intereview, player choose to have 3 some/ Falase == Player decided not to have threesome or has yet to decide 

#region Phone
default messenger = Messenger()
default achievement_app = Application(_("Achievements"))
default kiwii = Kiwii()
default simplr_app = Simplr()
default relationship_app = Application(_("Relationships"))
default tracker = Application(_("Tracker"))
default reputation_app = Application(_("Reputation"))
default calendar = Application(_("Calendar"))

#region Kiwii
default kiwii_first_time = False
default kiwii_posts = []
#endregion Kiwii
#endregion Phone

    ## Fight Vars
default fight_tutorial = False
default fight_type = "normal" # normal / simReal / simWin
default reaction = 1.0
default reactiona = 1.0
default bodyHook = False
default enemyhealth = 0

    ## Free Roam
default previous_location = ""

    ## Path Builder
default pb_reputation_notification = False
default path_builder = False
default pb_name_set = False
default pb_reputation_shown = False

    # Voice Acting
default voice_acted = True

# KCT
default reputation = Reputation()
default locked_reputation = False

# Scenes
default sceneList = set()

# Screens
default screen_options = []

# Sex Overlay
default sex_overlay_options = []

# Splashscreen
default persistent.confirm_18 = False

#region NonPlayableCharacters
default aaron = NonPlayableCharacter("Aaron", "DoubleARon")
default amber = NonPlayableCharacter("Amber", "Amber_xx")
default anon = NonPlayableCharacter("Anon", "concerned1")
default aubrey = NonPlayableCharacter("Aubrey", "Aubs123")
default autumn = NonPlayableCharacter("Autumn", "Its_Fall")
default beth = NonPlayableCharacter("Beth")
default buyer = NonPlayableCharacter("Buyer")
default caleb = NonPlayableCharacter("Caleb", "Aleb")
default cameron = NonPlayableCharacter("Cameron", "Cameroon") # Relationship progression: FRIEND, BRO
default charli = NonPlayableCharacter("Charli", "CharliAndTheCockFactory")
default chloe = NonPlayableCharacter("Chloe", "Chloe101")
default chris = NonPlayableCharacter("Chris", "Chriscuit")
default dean = NonPlayableCharacter("Dean")
default elijah = NonPlayableCharacter("Elijah", "Elijah_Woods") # Relationship progression: MAKEFUN, FRIEND
default emily = NonPlayableCharacter("Emily", "emilyyyy")
default emmy = NonPlayableCharacter("Emmy") # Relationship progression: FRIEND, LIKES, FWB (in CK1)
default grayson = NonPlayableCharacter("Grayson", "G-rayson")
default imre = NonPlayableCharacter("Imre", "BadBoyImre")
default iris = NonPlayableCharacter("Iris")
default jenny = NonPlayableCharacter("Jenny")
default josh = NonPlayableCharacter("Josh", "Josh80085")
default lauren = NonPlayableCharacter("Lauren", "LoLoLauren")
default lews_official = NonPlayableCharacter("Lews Official", "LewsOfficial")
default lindsey = NonPlayableCharacter("Lindsey", "LindsLou")
default mason = NonPlayableCharacter("Mason", "Mason_Mas")
default mr_lee = NonPlayableCharacter("Mr Lee")
default ms_rose = NonPlayableCharacter("Ms Rose")
default naomi = NonPlayableCharacter("Naomi", "NaomiXMarie")
default nora = NonPlayableCharacter("Nora", "Nora_12")
default parker = NonPlayableCharacter("Parker")
default perry = NonPlayableCharacter("Perry")
default penelope = NonPlayableCharacter("Penelope", "Penelopeeps")
default polly = NonPlayableCharacter("Polly")
default riley = NonPlayableCharacter("Riley", "RileyReads")
default ryan = NonPlayableCharacter("Ryan", "Ryanator")
default samantha = NonPlayableCharacter("Samantha", "SamFromSpaceJam")
default sebastian = NonPlayableCharacter("Sebastian", "Big Seb")
default tom = NonPlayableCharacter("Tom")
default trainer = NonPlayableCharacter("Trainer")
default wolf = NonPlayableCharacter("Wolf")
#endregion NonPlayableCharacters

#region PlayableCharacters
default mc = PlayableCharacter()
#endregion PlayableCharacters

#endregion Init

# 1.0 - 6.0
# Relationship Screen
default relationship_girls = []

default adamattack = 1
default adamdmg = 0
default adamfight = 5
default adamstance = 1
default adamtut = False
default difficulty = None
default e = _("e")
default fightadam = False
default fighttom = False
default firstfight = True
default moveuppercut = False
default q = _("q")
default r = _("r")
default simadam = 1
default simadamfight = True
default simtom = 1
default simtomfight = False
default simyou = 1
default stance = 0
default tomattack = 1
default tomdmg = 0
default tomstance = 1
default w = _("w")
default winadam = False
default wintom = False
default youDamage = 0
default youHealth = 5

default apologize = False
default askfinn = False
default bowling = False
default v2_caughtpeeking = False
default v2_caughtpeekingcounter = False
default v4_skip_josh_party = False
default checkonrose = False
default chloecaught = False
default chooseimre = True
default costume = 1
default costumetried = set()
default costumeaubrey = False
default emilyandben = False
default evelynnumber = False
default forgiveemily = True
default freeroam1 = set()
default freeroam2 = set()
default freeroam3 = set()
default aubrey_boyfriend_threesome = False
default freeroam3asked = set()
default girl = ""
default imreforgives = False
default joinapes = False
default laurenpublic = False
default laurentest = set()
default laurentoofar = False
default meetaubrey = False
default meetchloe = False
default meetgrayson = False
default meetjulia = False
default meetlauren = False
default muffin = False
default notcool = False
default penelopekiss = False
default perform = 0
default relics = 0
default save = 0
default simp = False
default statsPage = 0
default takeshot = False
default tellschool = False
default toldlauren = False
default trolleyb = False
default upstairs = _("nobody")
default v1_laurenPoints = 0
default v2_outfits = 0
default volleyball = False

#region v2.0
default v2_made_a_move_on_evelyn = False
#endregion v2.0

#region v6.0
default v6_evelyn_successful_date = False
#endregion v6.0

# 7.0
default apesVids = 0
default beachfirstkiss = False
default v7_chloesad = False
default cop = False
default emilyText = False
default ending = _("riley")
default freeroam4 = set()
default hcAsked = [] # hcAsked.append("girl_name") to add
default hcGirl = _("alone")
default joinwolves = False
default nobeach = False
default politics = False
default preventgrayson = False
default protest = False
default rileysex = False
default seenlauren = False
default signs = False
default v7_emily_bowling = False
default v7_visited_shelter = False
default walkedRileyHome = False
default wolvesTasks = set()

# 8.0
default amberSexOfferAtJoshs = False
default chloeSteakHouse = False
default climbwseb = False
default consoledRose = False
default emilyArcade = 0
default helpedNora = False
default helpJosh = False
default hesitantwgrayson = False
default larsdmg = 0
default s28_fightWinner = _("MC")
default sideWithCameron = False
default simLarsFight = False
default v8_dodged_pipe = False
default musicstop = False

# 9.0
default dreamFightChoice = _("na")
default freeroam5 = set()
default hangOutWithLindsey = False
default hl_punch = False
default playCoolWLins = False
default the_king = False
default v9_brawl_hesitant = False
default v9_sex_with_riley = False

# 10.0
default drinkWsam = False
default emily_europe = False
default freeroam6 = set()
default josh_europe = False
default makeSamCock = False
default sadlind_reaction = False
default skater = False
default v10_amber_awkward = False
default v10_amber_condoms = False
default v10_cheerfornora = False
default v10_help_nora_freeroam = False
default v10_imre_fight = False
default v10_imre_win = False
default v10_inv_pen_cafe = False
default v10_josh_alley_yes = False
default v10_ms_r_interfere = False
default v10_nora_bitch_about_chloe = False
default v10_ryan_fight = False
default v10_ryan_win = False
default v10_simplr_known = False
default v10s10_hangWLinds = False
default v10s33_aubreyriley = False
default v10s33_ev_date_now = False
default v10s33_laurenBakeSale = False
default v10s33_ryan_flirt_emily = False
default v10s33_toldChloe = False

# 11.0
default candyLike = 0
default freeroam7 = set() #Penelope Court
default freeroam8 = set() #London Museum
default v11_she_will_miss = False
default v11_amber_sauna_convo = False
default v11_check_on_nora = False
default v11_hp_points = 0
default v11_invite_sam_europe = False
default v11_josh_nightclub = False
default v11_kiss_nora = False
default v11_linds_inv_imre = False # If true Lindsey will invite Imre, if false, Lindsey will invite Ryan
default v11_lindsey_slogan = 1 # 1 is Lindsey, Returning The Promise // 2 is Lindsey, Say Bye To The Bullshit
default v11_manhunt_winner = _("Ryan")
default v11_overtake_points = 0
default v11_pen_goes_europe = False
default v11_riley_roomate = False
default v11_smoke_amber_amsterdam = False
default v11_solo_question = False
default v11_tease_amber = 0
default v11_told_aubrey = False
default v11_underground_rose = False
default v11s1_courtpoints = 0
default v11s23_penelope_date = True # late addition, defaulting to True to enhance act 4 playability
default v11s25_beer = True
default v11_ride_with_mrlee = False
default v11s13_rejected_aubrey = False
default v11_dealership = False

# 12.0
default freeroam9 = set() #Ferry
default s12v32_get_aubrey_flowers = False
default v11_lindsey_run = False
default v12_chase_robber = False
default v12_fight_win = False 
default v12_girl = _("na")
default v12_help_chris = 0
default v12_lauren_points = 0
default v12_murder_count = 0
default v12_nora_points = 0
default v12_sauna_sneak1 = False
default v12_saunadoors = set()
default v12_slumberparty = set()
default v12_told_chloe = False
default v12s23a_sam = 0
default v12s24_emmymatch = False
default v12s32_Aubrey_Boost = False
default v12s7_aubrey_moved = False
default v12s7_endtalkList = []
default v12s7_killList = set()
default v12s7_lindsey_moved = False
default v12s7_riley_moved = False
default v12s7_seenList = []
default v12s7_victims = 12 #Amber, Aubrey, Charli, Chloe, Chris, Imre, Lauren, Lindsey, Nora, Riley, Rose, Ryan + Emily, Josh, Penelope, Samantha. Cameron and Lee don't count.
default v12_followed_nora = False
default v12s16_kissnora = False

# 13.0
default chloeSus = 0
default chloeturnedon = set() #Chloe Amsterdam
default freeroam10 = set() #Charli room
default freeroam11 = set() #Amsterdam garden
default v11_lauren_caught_aubrey = False
default v13_after_party = False
default v13_aubrey_concert = False
default v13_charli_exposed = False
default v13_cuddle_lauren = False
default v13_cuddle_lauren_text = False
default v13_help_chloe = False
default v13_hugged_aubrey = False
default v13_imre_disloyal = False
default v13_invite_samantha = False
default v13_lauren_smoke = False
default v13_penelope_concert = False
default v13_concert_backstage = False
default v13_perfume = False
default v13_smoke_weed = False
default v13_emmy_points = 0
default v13s16_lauren_points = 0
default v13s20_bleach_suitcase = False
default v13s41_lindsey_points = 0
default v13s48_canoeing_as_date = False
default v13s48_get_aubrey_chocolate = False
default v13s48_ryan_double_date = False
default v13s9_go_to_concert = False

# 14.0
## Chloe Planing Board
default chloe_board = PlanningBoard("images/v14/chicks_presidency_race/planning_boards/chloe_background.webp", money=1500)
default v14_chloe_wolves = False ##APPROACH A (v14_chloe_apes = v14_help_chloe and not v14_chloe_wolves)
default v14_realwolf = False ##TASK A2A (v14_plushwolf = v14_chloe_wolves and not v14_realwolf)
default v14_chloe_cameron = False ##TASK B2B (v14_chloe_grayson = (v14_help_chloe and not v14_chloe_wolves) and not v14_chloe_cameron)

## Lindsey Planing Board
default lindsey_board = PlanningBoard("images/v14/chicks_presidency_race/planning_boards/lindsey_background.webp", money=200, style="lindsey_board")
default v14_lindsey_sell = False ##APPROACH A (v14_lindsey_steal = v14_help_lindsey and not v14_lindsey_sell)
default v14_pics_with_linds = False ##TASK A1B (v14_pics_no_linds = v14_lindsey_sell and not v14_pics_with_linds)
default v14_date_distraction = False ###APPROACH B1B (v14_concert_distraction = (v14_help_lindsey and not v14_lindsey_sell) and not v14_date_distraction)

# Animated Bar
default animated_value_percent = 0

default chrissus = 0
default irisStrikes = 0
default v13_threesomeending = False
default v14_amber_clean = False
default v14_ApesPostChloePics = True #They always post unless MC is an Ape and stops them.
default v14_badsinging_Sam = False
default v14_chrissupport = 0 #3 = Full, 2 = Medium, 1 = Low
default v14_emily_ily = False
default v14_help_chloe = False
default v14_help_lindsey = False
default v14_jennypoints = 0
default v14_lauren_helps_lindsey = False
default v14_lauren_sabotage = False
default v14_lindsey_popularity = 45 # Use set_presidency_percent(amount).
default v14_noraWhere = False #????
default v14_noraWorry = False #????
default v14_penelope_date = False
default v14_PenelopePartner = False
default v14_PenRomScene = False
default v14_ryan_satin = False
default v14_samantha_cum = False
default v14_SamanthaDrugs = False
default v14_talk_to_chris = False
default v14s03a_take_wallet = False
default v14s23_agree = False
default v14s23_disagree = False
default v14s24a_gummyfish = False
default v14s25_letherstay = False
default v14s30b_image = 0
default v14s30b_its_perfect = False # Telling Chloe that the caption is perfect
default v14s31b_smoke_weed_with_aubrey = False # s31b smoking weed with Aubrey at Ape's House
default v14s31bTrustChloe = False # MC trust Chloe alone with Grayson
default v14s37_focus_on_us = False # Tell Penelope to focus on them during the date.
default v14s39_id_wait = False # Tell Penelope you'd wait till they got home
default v14s4_tell_imre = False
default v14s41a_standup = False #stand up for Chloe during the Apes meeting
default v14s46a_love_lauren_more = False # MC love Lauren more because of her sex experimenting on MC.
default v14s47_car_pics = []
default v14s48_car_description = None
default v14s48_car_price = 100
default v14s50_listen_to_aubrey_lindsey = 0 # MC choses to listen to Lindsey and Aubrey's conversation. 
default freeroam12 = set() #chloe heist
default freeroam12stolen = set()
default v14s5a_riley_should_join_chicks = False
default AutumnTrust = False
