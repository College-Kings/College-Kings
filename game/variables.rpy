#region Init
#region Constants
define is_CK2 = False
define SERVER_URL = "http://82.9.123.190:8080"
define flash = Fade(.25, 0, .75, color="#fff")
define config.default_music_volume = 1
define config.default_sfx_volume = 1

#region Path Builder
define pb_starting_locations = (("Act 1 Start", "start"), ("Act 2 Start", "v7_homecoming"), ("Act 3 Start", "v11_start"))
#endregion Path Builder

#region Scene Gallery
define scene_gallery_items = (
    SceneGallery(
        _("Dreaming of Riley"), "images/v1/sda1.webp", "sexdream1"
    ),  # v1, Riley, day 1
    SceneGallery(
        _("Fight with Tom"), "images/v2/tomhook.webp", "v1_tomShoutBack"
    ),  # v2, Tom
    SceneGallery(
        _("First time with Aubrey"), "images/v3/aub1start.webp", "continuem"
    ),  # v3, Aubrey, day 4
    SceneGallery(_("Fight with Adam"), "images/v5/af5start.webp", "fkcon"),  # v5, Adam
    SceneGallery(
        _("Taking back Emily"), "images/v6/em5.webp", "emsex_a"
    ),  # Emily, day 7
    SceneGallery(
        _("Fun with Aubrey"), "images/v6/naub4.webp", "aubreysexb"
    ),  # Aubrey, day 7
    SceneGallery(
        _("First time with Riley"),
        "images/v7/risex1vid20.webp",
        "rileysexscene",
    ),  # Riley, day 10
    SceneGallery(
        _("Sneaking to the stall"), "images/v7/sfr4ri42.webp", "brbj"
    ),  # Aubrey, day 11
    SceneGallery(
        _("Homecoming Amber"),
        "images/v8/scene 5/v8samb1.webp",
        "hoco_amb_night",
    ),  # 5, Amber, day 11
    SceneGallery(
        _("Homecoming Chloe"), "images/v8/scene 2/v8s16.webp", "v8_cl_start"
    ),  # 2, Chloe, day 11
    SceneGallery(
        _("Homecoming Riley"), "images/v8/scene 3/v8s33_2.webp", "v8_ri_start"
    ),  # 3, Riley, day 11
    SceneGallery(
        _("Fight with Lars"),
        "images/v8/scene 28/mcbodyhookstart.webp",
        "int_deal_w_josh",
    ),  # 28, Lars Joe
    SceneGallery(
        _("With Amber at Josh's"),
        "images/v8/scene 30/v8amber14a.webp",
        "amber_sex_at_joshs",
    ),  # 30, Amber, day 14
    SceneGallery(
        _("Lake w/ Aubrey"),
        "images/v9/scene 7/v9slake18vidend.webp",
        "v9_aubrey_scene_lake",
    ),  # 7, Aubrey, day 16
    SceneGallery(
        _("Emily sex scene"), "images/v9/scene 16/v9emi33.webp", "v9_emily_dorm"
    ),  # 16, Emily, day 17
    SceneGallery(
        _("Riley sex scene"), "images/v9/scene 34/v9ris7a.webp", "v9_ri_sex"
    ),  # 34, Riley, day 19, v9_sex_with_riley
    SceneGallery(
        _("Make out with Lindsey"),
        "images/v9/scene 39/v9linksStart.webp",
        "v9_make_out_w_lin",
    ),  # 39, Lindsey, day 19
    SceneGallery(
        _("Ryan Fight"),
        "images/v10/scene 6/v10mvr6.webp",
        "v10_mc_vs_ryan_fight",
    ),  # 6, Ryan
    SceneGallery(
        _("Imre Fight"),
        "images/v10/scene 7/v10mvi3.webp",
        "v10_mc_vs_imre_fight",
    ),  # 7, Imre
    SceneGallery(
        _("More with Aubrey"),
        "images/v10/scene 17/v10aubfaStart.webp",
        "v10s17_galleryScene",
    ),  # 17, Aubrey, day 20
    SceneGallery(
        _("Make out with Lauren"),
        "images/v10/scene 24/v10lar7d.webp",
        "v10_lauren_room_sg",
    ),  # 24, Lauren, day 21 (scope is Lauren GIRLFRIEND)
    SceneGallery(
        _("Amber Skatepark Sex"),
        "images/v10/scene 26/v10sasp11a.webp",
        "v10_amber_skatepark_sg",
    ),  # 26, Amber, day 21
    SceneGallery(
        _("Changing with Chloe"),
        "images/v10/scene 30/v10chg10f.webp",
        "v10s30_galleryScene",
    ),  # 30, Chloe, day 22
    SceneGallery(
        _("More with Riley"),
        "images/v10/scene 40/v10srds6a.webp",
        "v10s40_galleryScene",
    ),  # 40, Riley, day 23 (scope is Riley FWB)
    SceneGallery(
        _("First time with Candy"),
        "images/v11/scene 5/v11swc25.webp",
        "v11s5_galleryScene",
    ),  # 5, Candy, day 24
    SceneGallery(
        _("Airplane with Aubrey"),
        "images/v11/scene 13/v11aub18a.webp",
        "v11_aubrey_plane_sex_sg",
    ),  # 13, Aubrey, day 26
    SceneGallery(
        _("First time w/ Ms. Rose"),
        "images/v11/scene 28/v11ros3.webp",
        "v11_ms_rose_sex_sg",
    ),  # 28, Rose, day 27
    SceneGallery(
        _("Spa with Samantha"),
        "images/v11/scene 28a/v11sas16a.webp",
        "v11s28a_galleryScene",
    ),  # 28a, Samantha, day 27
    SceneGallery(
        _("In London with Riley"),
        "images/v11/scene 35/v11ris18a.webp",
        "v11_riley_sex_sg",
    ),  # 35, Riley, day 28
    SceneGallery(
        _("In London with Chloe"),
        "images/v11/scene 41b/v11chtf2Start.webp",
        "v11_chloe_sex_scene",
    ),  # 41b, Chloe, day 29
    SceneGallery(
        _("Locked up with Lindsey"),
        "images/v12/scene 17/v12esr33.webp",
        "v12_lindsey_sex",
    ),  # 17, Lindsey, day 32
    SceneGallery(
        _("In Paris with Ms. Rose"),
        "images/v12/scene 23/v12msr19.webp",
        "v12_ms_rose_sex_sg",
    ),  # 23, Rose, day 33
    SceneGallery(
        _("First time with Lauren"),
        "images/v12/scene 29/v12las58.webp",
        "v12_lauren_sex_sg",
    ),  # 29, Lauren, day 34
    SceneGallery(
        _("First time with Nora"),
        "images/v12/scene 35a/v12nos27.webp",
        "v12_nora_sex",
    ),  # 35a, Nora, day 35
    SceneGallery(
        _("Late night with Riley"),
        "images/v13/scene 16a/v13s16a_7.webp",
        "v13s16a",
    ),  # 16a, Riley, day 37
    SceneGallery(
        _("Fun with Emmy"), "images/v13/scene 26/v13s26_5.webp", "v13s25_emmysg"
    ),  # 26, Emmy, day 38
    SceneGallery(
        _("Wild with Chloe"),
        "images/v13/scene 40/v13s40end_1.webp",
        "v13s40_sg",
    ),  # 40, Chloe, day 39
    SceneGallery(
        _("Angry at Emily"), "images/v13/scene 50a/v13s50a_5.webp", "v13s50a"
    ),  # 50a, Emily, day 40
    SceneGallery(
        _("Why not both?"), "images/v14/scene 1/v14s01_4.webp", "v14s01"
    ),  # 1, Riley Aubrey, xx
    SceneGallery(
        _("Satin-ly pleased"),
        "images/v14/scene 3d/v14s03d_5.webp",
        "v14s03c_sg",
    ),  # 3d, Satin, xx
)
#endregion Scene Gallery

#endregion Constants
default menu_set = set()

default is_censored = False
default label_history = []
default real_life_mode = False

    ## Fight Vars
default fight_tutorial = False
default fight_type = "normal" # normal / simReal / simWin
default reaction = 1.0
default reactiona = 1.0
default bodyHook = False
default enemyhealth = 0

    ## Free Roam
default previous_location = ""

    # Voice Acting
default voice_acted = True

# Scenes
default sceneList = set()
default viewed_scenes = set()

# Screens
default screen_options = []

# Sex Overlay
default sex_overlay_options = []

# Splashscreen
default persistent.confirm_18 = False
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
default v6_relics = {
    V6_Relics.PICTURE: False,
    V6_Relics.TROPHIES: False,
    V6_Relics.CERTIFICATE: False,
    V6_Relics.RELICS: False
}
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

#region v8.0
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
default v8_nora_likes_mc = False
#endregion v8.0

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
default v13_help_chloe = False
default v13_hugged_aubrey = False
default v13_imre_disloyal = False
default v13_invite_samantha = False
default v13_lauren_smoke = False
default v13_penelope_concert = False
default v13_concert_backstage = False
default v13_perfume = False
default v13_smoke_weed = False
default v13s16_lauren_points = 0
default v13s20_bleach_suitcase = False
default v13s41_lindsey_points = 0
default v13s48_canoeing_as_date = False
default v13s48_get_aubrey_chocolate = False
default v13s48_ryan_double_date = False
default v13s9_go_to_concert = False
default v13_cameron_and_mc_friends = False

# 14.0
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
