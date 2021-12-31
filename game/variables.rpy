init python:
    import os


## Init
define flash = Fade(.25, 0, .75, color="#fff")
define config.default_music_volume = 1
define config.default_sfx_volume = 1
default menu_set = set()
default achievementAtList = None

    ## Phone
define contacts_file_path = os.path.join(config.basedir, "game", "images", "nonplayable_characters")

    ## Kiwii Vars
default kiwiiUsers = kiwii_users()
default kiwii_firstTime = False

    ## Fight Vars
default fight_tutorial = False
default fight_type = "normal" # normal / simReal / simWin
default reaction = 1.0
default reactiona = 1.0
default bodyHook = False
default enemyhealth = 0

    ## Free Roam
default previous_location = ""

    ## Checklist
default checklist = Checklist()

    ## Path Builder
default path_builder = False
default pb_name_set = False

# voiceacting
default voice_acted = True

# KCT
default locked_kct = False
default kct = "confident"
default sortedKCT = ["confident", "loyal", "popular"]

default bro = 1
default boyfriend = 2
default troublemaker = 1

#Scenes
default sceneList = set()

# 1.0 - 6.0
default adamattack = 1
default adamdmg = 0
default adamfight = 5
default adamstance = 1
default adamtut = False
default apologize = False
default askfinn = False
default aubreyrs = False
default autumnmad = False
default bowling = False
default v2_caughtpeeking = False
default v2_caughtpeekingcounter = False
default checkonrose = False
default chloecaught = False
default chloemad = True
default chooseimre = True
default costume = 1
default costumetried = set()
default costumeaubrey = False
default difficulty = None
default e = "e"
default emilyandben = False
default emilyrs = False
default evelyndate = False
default evelynmove = False
default evelynnumber = False
default evelynrs = False
default fightadam = False
default fighttom = False
default firstfight = True
default forgiveemily = False
default freeroam1 = set()
default freeroam2 = set()
default freeroam3 = set()
default freeroam3asked = set()
default funofelijah = False
default girl = ""
default imreforgives = False
default imremad = False
default joinapes = False
default kissamber = False
default laawk = True
default laurenkissb = False
default laurenmad = False
default laurenpublic = False
default laurenrs = False
default laurentest = set()
default laurentoofar = False
default meetaubrey = False
default meetchloe = False
default meetgrayson = False
default meetjulia = False
default meetlauren = False
default moveuppercut = False
default muffin = False
default name = "Alex"
default noramad = False
default notcool = False
default penelopekiss = False
default perform = 0
default q = "q"
default r = "r"
default realmode = False
default relics = 0
default rileykiss = False
default save = 0
default showkct = True
default simadam = 1
default simadamfight = True
default simp = False
default simtom = 1
default simtomfight = False
default simyou = 1
default stance = 0
default statsPage = 0
default takeshot = False
default tellschool = False
default toldlauren = False
default tomattack = 1
default tomdmg = 0
default tomstance = 1
default trolleyb = False
default upstairs = "nobody"
default v1_aubreywannafight = False
default v1_hitOnNora = False
default v1_kissLauren = False
default v1_laurenKiss = False
default v1_laurenPoints = 0
default v2_outfits = 0
default volleyball = False
default w = "w"
default winadam = False
default youDamage = 0
default youHealth = 5

# 7.0
default amberrs = False
default apesVids = 0
default beachfirstkiss = False
default chloers = False
default chloesad = False
default cop = False
default emilyText = False
default ending = "riley"
default freeroam4 = set()
default hcAsked = [] # hcAsked.append("girl_name") to add
default hcGirl = "alone"
default joinwolves = False
default kiwii = False
default nobeach = False
default penelopers = False
default politics = False
default preventgrayson = False
default protest = False
default rileyrs = False
default rileysex = False
default seenlauren = False
default signs = False
default v7_emily_bowling = False
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
default noralikes = False
default s28_fightWinner = "MC"
default sideWithCameron = False
default simLarsFight = False
default v8_dodged_pipe = False
default v8_riley_lewd_ending = False

# 9.0
default dreamFightChoice = "na"
default freeroam5 = set()
default hangOutWithLindsey = False
default hl_punch = False
default lindseyfirstkiss = False
default playCoolWLins = False
default the_king = False
default v9_brawl_hesitant = False
default v9_sex_w_em = False
default v9_sex_with_riley = False

# 10.0
default drinkWsam = False
default emily_europe = False
default freeroam6 = set()
default josh_europe = False
default joshmad = False
default makeSamCock = False
default sadlind_reaction = False
default skater = False
default v10_amber_awkward = False
default v10_amber_condoms = False
default v10_cheerfornora = False
default v10_chloe_rematch = False
default v10_help_nora_freeroam = False
default v10_imre_fight = False
default v10_imre_win = False
default v10_inv_pen_cafe = False
default v10_josh_alley_yes = False
default v10_ms_r_interfere = False
default v10_ms_r_kiss = False
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
default chloegf = False
default freeroam7 = set() #Penelope Court
default freeroam8 = set() #London Museum
default msrosers = False
default political_strategist = False
default v11_amber_sauna_convo = False
default v11_aubrey_blue_outfit = False
default v11_aubrey_sex = False
default v11_check_on_nora = False
default v11_fucked_candy = False
default v11_hp_points = 0
default v11_invite_sam_europe = False
default v11_josh_nightclub = False
default v11_kiss_nora = False
default v11_linds_inv_imre = False # If true Lindsey will invite Imre, if false, Lindsey will invite Ryan
default v11_lindsey_slogan = 0 # 1 is Lindsey, Returning The Promise // 2 is Lindsey, Say Bye To The Bullshit
default v11_manhunt_winner = "Ryan"
default v11_msrose_scene = False
default v11_overtake_points = 0
default v11_pen_goes_europe = False
default v11_riley_roomate = False
default v11_samantha_spa = False
default v11_sit_with_lauren = True
default v11_smoke_amber_amsterdam = False
default v11_solo_question = False
default v11_tease_amber = 0
default v11_told_aubrey = False
default v11_underground_rose = False
default v11s1_courtpoints = 0
default v11s23_penelope_date = True # late addition, defaulting to True to enhance act 4 playability
default v11s25_beer = True
default v11_ride_with_mrlee = False # late addition, needed for scene V15 S21

# 12.0
default chrismad = False
default freeroam9 = set() #Ferry
default joshmadfr = False
default lindseyrs = False
default norars = False
default s12v32_get_aubrey_flowers = False
default v11_lindsey_run = False
default v12_chase_robber = False
default v12_fight_win = False 
default v12_girl = "na"
default v12_help_chris = 0
default v12_lauren_points = 0
default v12_lauren_sex = False
default v12_lindsey_sex = False
default v12_msrose_sex = False
default v12_murder_count = 0
default v12_nora_points = 0
default v12_nora_sex = False
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

# 13.0
default aryssars = False
default cameronBro = False
default chloeSus = 0
default chloeturnedon = set() #Chloe Amsterdam
default emmyrs = False
default freeroam10 = set() #Charli room
default freeroam11 = set() #Amsterdam garden
default kourtneyrs = False
default laurenrs_v11aubrey = False
default v13_after_party = False
default v13_aubrey_concert = False
default v13_charli_exposed = False
default v13_cuddle_lauren = False
default v13_cuddle_lauren_text = False
default v13_emilysex = False
default v13_emmysex = False
default v13_help_chloe = False
default v13_hugged_aubrey = False
default v13_imre_disloyal = False
default v13_invite_samantha = False
default v13_lauren_smoke = False
default v13_penelope_concert = False
default v13_perfume = False
default v13_bonsai = False # late addition, needed for scene V15 S21
default v13_smoke_weed = False
default v13_emmy_points = 0
default v13s16_lauren_points = 0
default v13s20_bleach_suitcase = False
default v13s40fromgame = False
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

default AmberLoyal = False
default AutumnTrust = False
default chrissus = 0
default ElijahFriend = False
default irisStrikes = 0
default jennyawkward = False
default jennyfriend = False
default jennyrs = False
default penelopeloyal = False
default v13_FirstThreesome = False # Variable used to call for Riley and Aubrey threesome happening.
default v13_threesomeending = False
default v14_amber_clean = False
default v14_amber_sex = False
default v14_ApesPostChloePics = True #They always post unless MC is an Ape and stops them.
default v14_badsinging_Sam = False
default v14_chrissupport = 0 #3 = Full, 2 = Medium, 1 = Low
default v14_emily_ily = False
default v14_help_chloe = False
default v14_help_lindsey = False
default v14_jenny_sex = False
default v14_jennypoints = 0
default v14_lauren_helps_lindsey = False
default v14_lauren_sabotage = False
default v14_lindsey_popularity = 45 # Use `set_presidency_percent(amount)`.
default v14_noraWhere = False
default v14_noraWorry = False
default v14_penelope_date = False
default v14_PenelopePartner = False
default v14_PenRomScene = False
default v14_ryan_satin = False
default v14_samantha_cum = False
default v14_samantha_sex = False
default v14_SamanthaDrugs = False
default v14_talk_to_chris = False
default v14s03a_take_wallet = False
default v14s23_agree = False
default v14s23_disagree = False
default v14s24a_gummyfish = False
default v14s25_letherstay = False
default v14s30b_image = 0
default v14s30b_its_perfect = False  # Telling Chloe that the caption is perfect
default v14s31b_smoke_weed_with_aubrey = False # s31b smoking weed with Aubrey at Ape's House
default v14s31bTrustChloe = False # MC trust Chloe alone with Grayson
default v14s37_focus_on_us = False # Tell Penelope to focus on them during the date.
default v14s39_id_wait = False # Tell Penelope you'd wait till they got home
default v14s4_tell_imre = False
default v14s41a_standup = False #stand up for Chloe during the Apes meeting
default v14s46a_love_lauren_more = False # MC love Lauren more because of her sex experimenting on MC.
default v14s47_car_pics = []
default v14s47_linds_driver = False
default v14s47_linds_hips = False
default v14s47_linds_hood = False
default v14s47_linds_knees = False
default v14s47_linds_passenger = False
default v14s47_linds_trunk = False
default v14s47_passenger = False
default v14s47_solo_bird = False
default v14s47_solo_driver = False
default v14s47_solo_hood = False
default v14s47_solo_no_bird = False
default v14s47_solo_passenger = False
default v14s47_solo_trunk = False
default v14s48_car_description = CarDescription.LIE
default v14s48_car_price = 100
default v14s50_listen_to_aubrey_lindsey = 0 # MC choses to listen to Lindsey and Aubrey's conversation. 
default freeroam12 = set() #chloe heist
default freeroam12stolen = set()
default v14s5a_riley_should_join_chicks = False
default v14_Samantha_clean = False # Placeholder?

# 15.0 
# Chloe Planning Board (v15s8)
default v15s8_chloe_pb_DamageLindseyRep = False  # checked in v15s12

# Lindsey Planning Board (v15s12)
default v15s12_lindsey_pb_gameNight = False         # True, GameNight; False, VIPNight
default v15s12_lindsey_pb_fakeId = False            # True, FakeIDl False, Limo/VIP rental
default v15s12_lindsey_pb_wouldYouRather = False    # True, Play Would You Rather; False, Play Who's Most Likely To
default v15_s12_lindsey_pb_inviteSebastian = False  # True, Invite Sebastian; False, Invite Grayson

default aubrey_friend = False 
default aubrey_fwb = False 
default aubrey_tamed = False 
default autumn_free_mug = False # not used (28/08/2021)
default autumn_lunch_break = False # not used (28/08/2021)
default dog_name = "Blue"
default v15_lauren_gift = None
default lindsey_friend = False # Placeholder?
default mr_lee_meeting = False # Placeholder?
default ms_rose_meeting = False # (redundancy check) # not used (28/08/2021)
default smoked_with_autumn = False
default v15_blame_chris = False 
default v15_blame_nora = False 
default v15_less_chick_tuition = False # not used (28/08/2021)
default V15_ms_rose_sex = False # Placeholder?
default v15_stuck_up_for_nora = False # not used (28/08/2021)
default v15_took_notes = False # not used (28/08/2021)
default v15s14_lets_go = False
default v15s5_mc_angry_with_rose = False # Placeholder?
default v15s7_chloe_empathize = False # not used (28/08/2021)
default v15s9_mad_at_ms_rose = False # checked in v15s12 # not used (28/08/2021)
default v15s18a_fraubrey = False
default v15s18a_frryan = False
default v15s18a_frautumnpenelope = False
default v15s18a_frimrelauren = False
default v15s18a_frchrisamber = False
default v15s18a_frdeer = False
default v15s18a_frphoto = False 
default v15s18a_frpumpkin = False
default v15s18_partytask = 0
default v15s18a_aub_kiwii_smile = False
default v15s18a_gag = False
default v15s18a_showlist_penelope_autumn = False # Show the party list to Penelope and Autumn.
<<<<<<< Updated upstream
default v15s18a_lie = False
default v15s18c_frpenelope = False
default v15s19_local_mc_ends_in_livingroom = False;  
default v15_told_Emily_I_Love_You = False # Placeholder?
default v15s18e_cum_in_lauren # Noted to be remembered 
default v15s24_nancy_dick = False
default v15_alcohol = False
default v15_ph_riley_upset = False  # placeholder ?? (set in s26?? ; read in v15s27)
default autumnloyal = False 
default autumnrs = False
default v15s33_flirt = False
default v15s33_cheese = False
default aubrey_mad = False
default v15s36_not_good_idea = False 
default v15s42_flirt = False
default v15s42_grab_breakfast = False
default detective = "None" # Archetypes: professional, psychologist, loose cannon
default clue_parents_house = False # Unlock the clue for Nora possibly being at Mr Rose or Ms Rose's house.
default clue_alone = False # Unlock the clue for Nora wanting to be alone.
default clue_camping = False # Unlock the clue for Nora camping.
default clue_mr_rose_cabin = False # Unlock the clue for Mr. Rose's cabin.
default clue_nora_hates_her_dad = False # Unlock the clue that Nora hates Mr. Rose.
default v15threaten_ms_rose = False # Requested Variables for v15s21
default v15seduce_ms_rose = False # Requested Variables for v15s21
default v15s48_interrupt = False
default v15s48_follow_your_heart = False
default v15s48_variable_check = 0