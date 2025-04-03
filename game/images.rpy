## Globals
image darker_80 = Solid("#000c")
image blue_button_idle = Frame("gui/button/blue_idle.webp", 24, 6)
image blue_button_hover = Frame("gui/button/blue_hover.webp", 24, 6)

# Splash Screen
image splashscreen_1 = "gui/splashscreen/1.webp"
image splashscreen_2 = "gui/splashscreen/2.webp"
image splashscreen_3 = "gui/splashscreen/3.webp"

#region GUI
## Alert
image alert_background = Frame("gui/alert/background.webp", 8, 8)

## Bar
image blue_bar = Frame("gui/bar/blue.webp", 44, 22, 44, 40)
image ruby_bar = Frame("gui/bar/ruby.webp", 44, 22, 44, 40)
image yellow_bar = Frame("gui/bar/yellow.webp", 44, 22, 44, 40)
image transparent_bar = Frame("#0000")

## Choice
image choice_button_idle = Frame("gui/choice/button_idle.webp", 40, 8)
image choice_button_hover = Frame("gui/choice/button_hover.webp", 40, 8)

#region Main Menu
image main_menu_background = "gui/main_menu/background.webp"
image main_menu_patreon_idle = "gui/main_menu/patreon_idle.webp"
image main_menu_patreon_hover = Transform("gui/main_menu/patreon_hover.webp", pos=(-18, -14))
image main_menu_discord_idle = "gui/main_menu/discord_idle.webp"
image main_menu_discord_hover = "gui/main_menu/discord_hover.webp"
#endregion Main Menu

## Path Builder
image path_builder_button_idle = Frame("main_menu/path_builder/images/button_idle.webp", 24, 6)
image path_builder_button_hover = Frame("main_menu/path_builder/images/button_hover.webp", 24, 6)

## Scene Gallery
image scene_gallery_bar_base = Frame("gui/bar/bar_base.webp")

## Settings
image settings_bar_left = Frame("gui/settings/bar_right.webp", 14, 5)
image settings_bar_right = Frame("gui/settings/bar_right.webp", 14, 5)
image settings_bar_thumb = "gui/settings/bar_thumb.webp"

## Tutorial
image tutorial_background = Frame("gui/tutorial/background.webp", 42, 8, 8, 8)
image tutorial_left_button_idle = "gui/tutorial/left_button_idle.webp"
image tutorial_right_button_idle = "gui/tutorial/right_button_idle.webp"

## Warning
image warning_background_blue = Frame("gui/warning/background_blue.webp", 42, 8, 8, 8)
#endregion GUI

#region Path Builder
image path_builder_act_1_start = "gui/path_builder/act_1_start.webp"
image path_builder_act_2_start = "gui/path_builder/act_2_start.webp"
image path_builder_act_3_start = "gui/path_builder/act_3_start.webp"
#endregion Path Builder

# Transitions
image sleep_transition_fast = Movie(play="images/v15/sleep_transition_fast.webm", loop=False)

## Relationships
image relationships_frame_background = Frame("images/phone/relationships/app-assets/frame-background.webp")

# Fights
image fight_guard_animation:
    "#000070" with Dissolve(0.5)
    pause 1.0

    "#00f" with Dissolve(0.5)
    pause 1.0

    repeat

image fight_health_animation:
    "#700000" with Dissolve(0.5)
    pause 1.0

    "#f00" with Dissolve(0.5)
    pause 1.0

    repeat

#region Common
image girl_button_idle = "images/common/girl_button_idle.webp"
image girl_button_hover = "images/common/girl_button_hover.webp"
image girl_button_insensitive = Transform("girl_button_idle", matrixcolor=SaturationMatrix(0))

#region Free Roam
image free_roam_top = "images/common/free_roam_highlights/top.webp"
image free_roam_right = "images/common/free_roam_highlights/right.webp"
image free_roam_bottom = "images/common/free_roam_highlights/bottom.webp"
image free_roam_left = "images/common/free_roam_highlights/left.webp"
image free_roam_vertical_transparent = Transform("free_roam_top", alpha=0.0)
image free_roam_horizontal_transparent = Transform("free_roam_right", alpha=0.0)
#endregion Free Roam
#endregion Common

# v1.0 - v2.0
image s14 = "images/v1/s14.webp"
image s14a = "images/v1/s14a.webp"
image s14b = "images/v1/s14b.webp"
image s14c = "images/v1/s14c.webp"
image s15 = "images/v1/s15.webp"
image s16 = "images/v1/s16.webp"
image carback = Movie(play="images/v1/carback.webm")
image intro = Movie(play="images/v1/intro.webm", loop=False)
image adam1 = Movie(play="images/v1/adamau.webm")
image sdafj = Movie(play="images/v1/sdafj.webm", image="images/v1/sda4e.webp")
image sdafjf = Movie(play="images/v1/sdafjf.webm", image="images/v1/sda4e.webp")
image sdasex = Movie(play="images/v1/sdasex.webm", image="images/v1/sda7a.webp")
image sdacum2 = Movie(play="images/v1/sdacum2.webm", image="images/v1/aftercum.webp", loop=False)
image tompush = Movie(play="images/v2/tompush.webm", start_image="images/v2/126a.webp", image="images/v2/push12.webp", loop=False)

image abo = "images/abo.webp"
image aboq = "images/q button.webp"
image abow = "images/w button.webp"
image abor = "images/r button.webp"
image abod = "images/abod.webp"
image bboq = "images/block q.webp"
image bbow = "images/block w.webp"
image bbor = "images/block r.webp"
image 3hits = "images/3 hits.webp"
image 4hits = "images/4 hits.webp"
image 5hits = "images/5 hits.webp"
image jab2movie = Movie(play="images/v2/jab2.webm", start_image="images/v2/jab2start.webp", image="images/v2/jab2pic.webp", loop=False)
image tomfinishmovie = Movie(play="images/v2/tomfinish.webm", start_image="images/v2/tomfinishstart.webp", image="images/v2/tomfinish.webp", loop=False)
image youfinishmovie = Movie(play="images/v2/youfinish.webm", start_image="images/v2/youfinishstart.webp", image="images/v2/youfinish.webp", loop=False)
image hook2movie = Movie(play="images/v2/hook2.webm", start_image="images/v2/hook2start.webp", image="images/v2/hook2pic.webp", loop=False)
image kick1movie = Movie(play="images/v2/kick1.webm", start_image="images/v2/kick1start.webp", image="images/v2/kick1pic.webp", loop=False)
image tomjabmovie = Movie(play="images/v2/tomjab.webm", start_image="images/v2/tomjabstart.webp", image="images/v2/tomjab.webp", loop=False)
image tomkickmovie = Movie(play="images/v2/tomkick.webm", start_image="images/v2/tomkickstart.webp", image="images/v2/tomkick.webp", loop=False)
image kick2movie = Movie(play="images/v2/kick2.webm", start_image="images/v2/kick2start.webp", image="images/v2/kick2pic.webp", loop=False)
image tomhookmovie = Movie(play="images/v2/tomhook.webm", start_image="images/v2/tomhookstart.webp", image="images/v2/tomhook.webp", loop=False)
image hook1movie = Movie(play="images/v2/hook1.webm", start_image="images/v2/hook1start.webp", image="images/v2/hook1pic.webp", loop=False)
image jab1movie = Movie(play="images/v2/jab1.webm", start_image="images/v2/jab1start.webp", image="images/v2/jab1pic.webp", loop=False)
image hookcountermovie = Movie(play="images/v2/hookcounter.webm", start_image="images/v2/hookcounterstart.webp", image="images/v2/hookcounter.webp", loop=False)
image jabcountermovie = Movie(play="images/v2/jabcounter.webm", start_image="images/v2/jabcounterstart.webp", image="images/v2/jabcounter.webp", loop=False)

image targets = "images/targets.webp"

image s145far = "images/v2/s145far.webp"
image s145 = "images/v2/s145.webp"
image s145a = "images/v2/s145a.webp"
image s145b = "images/v2/s145b.webp"
image s145c = "images/v2/s145c.webp"
image s145d = "images/v2/s145d.webp"
image s145e = "images/v2/s145e.webp"
image s145bl = "images/v2/s145bl.webp"
image s145f = "images/v2/s145f.webp"

# v3.0
image aub1 = Movie(play="images/v3/aub1.webm", loop=False, image="images/v3/aub1.webp", start_image="images/v3/aub1start.webp")
image aub2 = Movie(play="images/v3/aub2.webm", image="images/v3/aub2.webp", start_image="images/v3/aub1.webp")
image aub3 = Movie(play="images/v3/aub3.webm", loop=False, image="images/v3/aub3.webp", start_image="images/v3/aub3start.webp")
image aub4 = Movie(play="images/v3/aub4.webm", image="images/v3/aub4.webp", start_image="images/v3/aub4start.webp")
image aub5 = Movie(play="images/v3/aub5.webm", loop=False, image="images/v3/aub5.webp", start_image="images/v3/aub5start.webp")
image aub7 = Movie(play="images/v3/aub7.webm", image="images/v3/aub7.webp", start_image="images/v3/aub7start.webp")
image aub8 = Movie(play="images/v3/aub8.webm", loop=False, image="images/v3/aub8.webp", start_image="images/v3/aub8start.webp")
image asexnew1 = Movie(play="images/v3/asexnew1.webm", image="images/v3/asexnew1end.webp", start_image="images/v3/asexnew1start.webp")
image asexnew2 = Movie(play="images/v3/asexnew2.webm", image="images/v3/asexnew2end.webp", start_image="images/v3/asexnew2start.webp")
image asexnew3 = Movie(play="images/v3/asexnew3.webm", image="images/v3/asexnew3end.webp", start_image="images/v3/asexnew3start.webp")
image asexnew4 = Movie(play="images/v3/asexnew4.webm", image="images/v3/asexnew4end.webp", start_image="images/v3/asexnew4start.webp")
image asexnew5 = Movie(play="images/v3/asexnew5.webm", image="images/v3/asexnew5end.webp", start_image="images/v3/asexnew5start.webp")
image asexnew6 = Movie(play="images/v3/asexnew6.webm", image="images/v3/asexnew4end.webp", start_image="images/v3/asexnew4start.webp")
image asexnew7 = Movie(play="images/v3/asexnew7.webm", image="images/v3/asexnew5end.webp", start_image="images/v3/asexnew5start.webp")
image asexnew9 = Movie(play="images/v3/asexnew9.webm", image="images/v3/asexnew8end.webp", start_image="images/v3/asexnew8start.webp")
image asexnew10 = Movie(play="images/v3/asexnew10.webm", image="images/v3/asexnew8end.webp", start_image="images/v3/asexnew8start.webp")
image asexnew11 = Movie(play="images/v3/asexnew11.webm", image="images/v3/asexnew11end.webp", start_image="images/v3/asexnew11start.webp")
image asexnew12 = Movie(play="images/v3/asexnew12.webm", image="images/v3/asexnew11end.webp", start_image="images/v3/asexnew11start.webp")
image asexnew13 = Movie(play="images/v3/asexnew13.webm", loop=False, image="images/v3/asexnew13end.webp", start_image="images/v3/asexnew13start.webp")

image rikiss2 = Movie(play="images/v3/rikiss.webm", loop=False, image="images/v3/rikiss.webp", start_image="images/v3/rikiss.webp")

#region v4.0
image s316 = "images/v4/s316.webp" # Julia looking forward talking smiling
image s316a = "images/v4/s316a.webp" # Julia looking forward talking smiling mouth closed
image s316c = "images/v4/s316c.webp" # Julia looking forward curious
image s316d = "images/v4/s316d.webp" # Julia looking forward curious mouth closed
image s316b = "images/v4/s316b.webp" # Julia looking at you smiling mouth open
#endregion v4.0

# v5.0
image af5 = Movie(play="images/v5/af5.webm", start_image="images/v5/af5start.webp", image="images/v5/af5pic.webp", loop=False)
image af6 = Movie(play="images/v5/af6.webm", start_image="images/v5/af6start.webp", image="images/v5/af6pic.webp", loop=False)
image af7 = Movie(play="images/v5/af7.webm", start_image="images/v5/af7start.webp", image="images/v5/af7pic.webp", loop=False)
image af8 = Movie(play="images/v5/af8.webm", start_image="images/v5/af8start.webp", image="images/v5/af8pic.webp", loop=False)
image af9 = Movie(play="images/v5/af9.webm", start_image="images/v5/af9start.webp", image="images/v5/af9pic.webp", loop=False)
image af10 = Movie(play="images/v5/af10.webm", start_image="images/v5/af10start.webp", image="images/v5/af10pic.webp", loop=False)
image af11 = Movie(play="images/v5/af11.webm", start_image="images/v5/af11start.webp", image="images/v5/af11pic.webp", loop=False)
image af12 = Movie(play="images/v5/af12.webm", start_image="images/v5/af12start.webp", image="images/v5/af12pic.webp", loop=False)
image af13 = Movie(play="images/v5/af13.webm", start_image="images/v5/af13start.webp", image="images/v5/af13pic.webp", loop=False)
image af14 = Movie(play="images/v5/af14.webm", start_image="images/v5/af14start.webp", image="images/v5/af14pic.webp", loop=False)
image af15 = Movie(play="images/v5/af15.webm", start_image="images/v5/af15start.webp", image="images/v5/af15pic.webp", loop=False)
image af16 = Movie(play="images/v5/af16.webm", start_image="images/v5/af16start.webp", image="images/v5/af16pic.webp", loop=False)
image youfinishadam = Movie(play="images/v5/youfinishadam.webm", start_image="images/v5/youfinishadamstart.webp", image="images/v5/youfinishadampic.webp", loop=False)
image adamfinish = Movie(play="images/v5/adamfinish.webm", start_image="images/v5/adamfinishstart.webp", image="images/v5/adamfinishpic.webp", loop=False)

# v6.0
image flyer = "images/v6/flyer.webp"

image emvid1 = Movie(play="images/v6/emvid1.webm", image="images/v6/em1end.webp", start_image="images/v6/em1start.webp")
image emvid2 = Movie(play="images/v6/emvid2.webm", image="images/v6/em2end.webp", start_image="images/v6/em2start.webp")
image emvid3 = Movie(play="images/v6/emvid3.webm", image="images/v6/em3end.webp", start_image="images/v6/em3start.webp")
image emvid4 = Movie(play="images/v6/emvid4.webm", image="images/v6/em4end.webp", start_image="images/v6/em4start.webp")
image emvid6 = Movie(play="images/v6/emvid6.webm", image="images/v6/em6end.webp", start_image="images/v6/em6start.webp")
image emvid7 = Movie(play="images/v6/emvid7.webm", image="images/v6/em7end.webp", start_image="images/v6/em7start.webp")
image emvid8 = Movie(play="images/v6/emvid8.webm", image="images/v6/em8end.webp", start_image="images/v6/em8start.webp")
image emvid9 = Movie(play="images/v6/emvid9.webm", loop=False, image="images/v6/em9end.webp", start_image="images/v6/em9start.webp")

image naubvid0 = Movie(play="images/v6/naubvid0.webm", loop=False, image="images/v6/naub0end.webp", start_image="images/v6/naub0start.webp")
image naubvid1 = Movie(play="images/v6/naubvid1v.webm", image="images/v6/naub1end.webp", start_image="images/v6/naub1start.webp")
image naubvid2 = Movie(play="images/v6/naubvid2.webm", image="images/v6/naub2end.webp", start_image="images/v6/naub2start.webp")
image naubvid3 = Movie(play="images/v6/naubvid3.webm", image="images/v6/naub3end.webp", start_image="images/v6/naub3start.webp")
image naubvid4 = Movie(play="images/v6/naubvid4.webm", image="images/v6/naub4end.webp", start_image="images/v6/naub4start.webp")
image naubvid5 = Movie(play="images/v6/naubvid5v.webm", image="images/v6/naub5end.webp", start_image="images/v6/naub5start.webp")
image naubvid6 = Movie(play="images/v6/naubvid6.webm", image="images/v6/naub6end.webp", start_image="images/v6/naub6start.webp")
image naubvid7 = Movie(play="images/v6/naubvid7.webm", loop=False, image="images/v6/naub7end.webp", start_image="images/v6/naub7start.webp")
image naubvid8 = Movie(play="images/v6/naubvid8.webm", image="images/v6/naub8end.webp", start_image="images/v6/naub8start.webp")
image naubvid9 = Movie(play="images/v6/naubvid9.webm", image="images/v6/naub9end.webp", start_image="images/v6/naub9start.webp")
image naubvid10 = Movie(play="images/v6/naubvid10.webm", image="images/v6/naub10end.webp", start_image="images/v6/naub10start.webp")
image naubvid11 = Movie(play="images/v6/naubvid11.webm", image="images/v6/naub11end.webp", start_image="images/v6/naub11start.webp")
image naubvid12 = Movie(play="images/v6/naubvid12.webm", image="images/v6/naub12end.webp", start_image="images/v6/naub12start.webp")
image naubvid13 = Movie(play="images/v6/naubvid13.webm", loop=False, image="images/v6/naub13end.webp", start_image="images/v6/naub13start.webp")

image carbacknight = Movie(play="images/v6/carbacknight.webm")

# v7.0
image s738avid = Movie(play="images/v7/s738avid.webm", loop=False, image="images/v7/s738avid75.webp", start_image="images/v7/s738avid16.webp")
image s743vid = Movie(play="images/v7/s743vid.webm", loop=False, image="images/v7/s743c.webp", start_image="images/v7/s743c.webp")

image risexvid1 = Movie(play="images/v7/risexvid1.webm", image="images/v7/risex1vid20.webp", start_image="images/v7/risex1vid00.webp")
image risexvid2s = Movie(play="images/v7/risexvid2s.webm", image="images/v7/rivid378.webp", start_image="images/v7/rivid360.webp")
image risexvid2f = Movie(play="images/v7/risexvid2f.webm", image="images/v7/rivid378.webp", start_image="images/v7/rivid360.webp")
image risexvid3s = Movie(play="images/v7/risexvid3s.webm", image="images/v7/rivid498.webp", start_image="images/v7/rivid478.webp")
image risexvid3f = Movie(play="images/v7/risexvid3f.webm", image="images/v7/rivid498.webp", start_image="images/v7/rivid478.webp")
image risexvid6s = Movie(play="images/v7/risexvid6s.webm", image="images/v7/rivid7_068.webp", start_image="images/v7/rivid7_052.webp")
image risexvid6f = Movie(play="images/v7/risexvid6f.webm", image="images/v7/rivid7_068.webp", start_image="images/v7/rivid7_052.webp")
image risexvid7 = Movie(play="images/v7/risexvid7.webm", image="images/v7/rivid8070.webp", start_image="images/v7/rivid8052.webp")
image risexvid8 = Movie(play="images/v7/risexvid8.webm", loop=False, image="images/v7/rivid8070.webp", start_image="images/v7/rivid8052.webp")

image ri42vid = Movie(play="images/v7/ri42vid.webm", image="images/v7/ri42vid20.webp", start_image="images/v7/ri42vid00.webp")
image ri42vidperspective = Movie(play="images/v7/ri42vidperspective.webm", image="images/v7/ri42vidperspective20.webp", start_image="images/v7/ri42vidperspective00.webp")
image ri42vidfast = Movie(play="images/v7/ri42vidfast.webm", image="images/v7/ri42vid20.webp", start_image="images/v7/ri42vid00.webp")
image ri42vidperspectivefast = Movie(play="images/v7/ri42vidperspectivefast.webm", image="images/v7/ri42vidperspective20.webp", start_image="images/v7/ri42vidperspective00.webp")

# v8.0
    # Scene 2
image v8s19dyn:
    "v8s19b" with Dissolve(0.35) # Chloe licking side of MC's shaft (top) while looking into the camera teasingly
    pause 1

    "v8s19c" with Dissolve(0.35) # Same as v8s19b but licking a little lower
    pause 0.5

    "v8s19d" with Dissolve(0.35) # Same as v8s19b but even lower, should not be fully at bottom of the dick though
    pause 1

    "v8s19c" with Dissolve(0.35)
    pause 0.5

    repeat

# Chloe slow blowjob animation. Should be FPP (She's looking into the camera)
image v8clbj1 = Movie(play="images/v8/Scene 2/v8clbj1.webm", loop=True, image="images/v8/Scene 2/clbj1_000.webp", start_image="images/v8/Scene 2/clbj1_000.webp")
# Same animation as bj1 but different angle (maybe a close up or something)
image v8clbj2 = Movie(play="images/v8/Scene 2/v8clbj2.webm", loop=True, image="images/v8/Scene 2/clbj2_000.webp", start_image="images/v8/Scene 2/clbj2_000.webp")
# Fast version of bj1 (need not be re-rendered)
image v8clbj1f = Movie(play="images/v8/Scene 2/v8clbj1f.webm", loop=True, image="images/v8/Scene 2/clbj1_000.webp", start_image="images/v8/Scene 2/clbj1_000.webp")
# Fast version of bj2 (need not be re-rendered)
image v8clbj2f = Movie(play="images/v8/Scene 2/v8clbj2f.webm", loop=True, image="images/v8/Scene 2/clbj2_000.webp", start_image="images/v8/Scene 2/clbj2_000.webp")
# Note the extra images - v8clbj1end, v8clbj1start, v8clbj2end, v8clbj2start

    # Fight Images
image MC_Lars_Kick_hit = Movie(play="images/v8/Scene 28/mckickhit.webm", start_image="images/v8/Scene 28/mckickhitstart.webp", image="images/v8/Scene 28/mckickhitend.webp", loop = False)
image MC_Lars_Kick_block = Movie(play="images/v8/Scene 28/mckickblocked.webm", start_image="images/v8/Scene 28/mckickblockedstart.webp", image="images/v8/Scene 28/mckickblockedend.webp", loop = False)
image MC_Lars_BodyJab_hit = Movie(play="images/v8/Scene 28/mcbodyhit.webm", start_image="images/v8/Scene 28/mcbodyhookstart.webp", image="images/v8/Scene 28/mcbodyhitend.webp", loop = False)
image MC_Lars_BodyJab_block = Movie(play="images/v8/Scene 28/mcbodyblocked.webm", start_image="images/v8/Scene 28/mcbodyblockedstart.webp", image="images/v8/Scene 28/mcbodyblockedend.webp", loop = False)
image MC_Lars_Jab_hit = Movie(play="images/v8/Scene 28/mcjabhit.webm", start_image="images/v8/Scene 28/mcjabhitstart.webp", image="images/v8/Scene 28/mcjabhitend.webp", loop = False)
image MC_Lars_Jab_block = Movie(play="images/v8/Scene 28/mcjabblocked.webm", start_image="images/v8/Scene 28/mcjabblockedstart.webp", image="images/v8/Scene 28/mcjabblockedend.webp", loop = False)
image MC_Lars_Hook_hit = Movie(play="images/v8/Scene 28/mchookhit.webm", start_image="images/v8/Scene 28/mchookhitstart.webp", image="images/v8/Scene 28/mchookhitend.webp", loop = False)
image MC_Lars_Hook_block = Movie(play="images/v8/Scene 28/mchookblocked.webm", start_image="images/v8/Scene 28/mchookblockedstart.webp", image="images/v8/Scene 28/mchookblockedend.webp", loop = False)
image larsjab = Movie(play="images/v8/Scene 28/larsjab.webm", start_image="images/v8/Scene 28/larsjabstart.webp", image="images/v8/Scene 28/larsjabend.webp", loop = False)
image larshook = Movie(play="images/v8/Scene 28/larshook.webm", start_image="images/v8/Scene 28/larshookstart.webp", image="images/v8/Scene 28/larshookend.webp", loop = False)
image larskick = Movie(play="images/v8/Scene 28/larskick.webm", start_image="images/v8/Scene 28/larskickstart.webp", image="images/v8/Scene 28/larskickend.webp", loop = False)
image larsbody = Movie(play="images/v8/Scene 28/larsbody.webm", start_image="images/v8/Scene 28/larsbodystart.webp", image="images/v8/Scene 28/larsbodyend.webp", loop = False)

image Lars_BodyJab_block = "images/v8/Scene 28/Lars_BodyJab_block.webp"
image Lars_BodyJab_hit = "images/v8/Scene 28/Lars_BodyJab_hit.webp"
image Lars_Hook_block = "images/v8/Scene 28/Lars_Hook_block.webp"
image Lars_Hook_hit = "images/v8/Scene 28/Lars_Hook_hit.webp"
image Lars_Jab_block = "images/v8/Scene 28/Lars_Jab_block.webp"
image Lars_Jab_hit = "images/v8/Scene 28/Lars_Jab_hit.webp"
image Lars_Kick_block = "images/v8/Scene 28/Lars_Kick_block.webp"
image Lars_Kick_hit = "images/v8/Scene 28/Lars_Kick_hit.webp"

# v10.0
    # Ryan Fight (Scene 6)
image mc_ryan_BodyJab_hit = Movie(play="images/v10/Scene 6/Animations/MC-BODYHIT/MC-BODYHIT.webm", start_image="images/v10/Scene 6/Animations/MC-BODYHIT/mc-bodyhitstart.webp", image="images/v10/Scene 6/Animations/MC/RYAN-BODYHIT-END.webp", loop = False)
image mc_ryan_BodyJab_block = Movie(play="images/v10/Scene 6/Animations/MC-BODYBLOCKED/MC-BODYBLOCKED.webm", start_image="images/v10/Scene 6/Animations/MC-BODYBLOCKED/mc-bodyblockedstart.webp", image="images/v10/Scene 6/Animations/MC/RYAN-BODYBLOCKED-END.webp", loop = False)
image mc_ryan_Hook_hit = Movie(play="images/v10/Scene 6/Animations/MC-HOOKHIT/MC-HOOKHIT.webm", start_image="images/v10/Scene 6/Animations/MC-HOOKHIT/mc-hookhitstart.webp", image="images/v10/Scene 6/Animations/MC/RYAN-HOOKHIT-END.webp", loop = False)
image mc_ryan_Hook_block = Movie(play="images/v10/Scene 6/Animations/MC-HOOKBLOCKED/MC-HOOKBLOCKED.webm", start_image="images/v10/Scene 6/Animations/MC-HOOKBLOCKED/mc-hookblockedstart.webp", image="images/v10/Scene 6/Animations/MC/RYAN-HOOKBLOCKED-END.webp", loop = False)
image mc_ryan_Jab_hit = Movie(play="images/v10/Scene 6/Animations/MC-JABHIT/MC-JABHIT.webm", start_image="images/v10/Scene 6/Animations/MC-JABHIT/mc-jabhitstart.webp", image="images/v10/Scene 6/Animations/MC/RYAN-JABHIT-END.webp", loop = False)
image mc_ryan_Jab_block = Movie(play="images/v10/Scene 6/Animations/MC-JABBLOCKED/MC-JABBLOCKED.webm", start_image="images/v10/Scene 6/Animations/MC-JABBLOCKED/mc-jabblockedstart.webp", image="images/v10/Scene 6/Animations/MC/RYAN-JABLOCKED-END.webp", loop = False)
image mc_ryan_Kick_hit = Movie(play="images/v10/Scene 6/Animations/MC-KICKHIT/MC-KICKHIT.webm", start_image="images/v10/Scene 6/Animations/MC-KICKHIT/mc-kickhitstart.webp", image="images/v10/Scene 6/Animations/MC/RYAN-KICKHIT-END.webp", loop = False)
image mc_ryan_Kick_block = Movie(play="images/v10/Scene 6/Animations/MC-KICKBLOCKED/MC-KICKBLOCKED.webm", start_image="images/v10/Scene 6/Animations/MC-KICKBLOCKED/mc-kickblockedstart.webp", image="images/v10/Scene 6/Animations/MC/RYAN-KICKBLOCKED-END.webp", loop = False)

image ryanjab = Movie(play="images/v10/Scene 6/Animations/RYANJAB/RYANJAB.webm", start_image="images/v10/Scene 6/Animations/RYANJAB/ryanjabstart.webp", image="images/v10/Scene 6/Animations/RYANJAB/ryanJabEnd.webp", loop = False)
image ryanhook = Movie(play="images/v10/Scene 6/Animations/RYANHOOK/RYANHOOK.webm", start_image="images/v10/Scene 6/Animations/RYANHOOK/ryanhookstart.webp", image="images/v10/Scene 6/Animations/RYANHOOK/ryanHookEnd.webp", loop = False)
image ryanbody = Movie(play="images/v10/Scene 6/Animations/RYANBODYHOOK/RYANBODYHOOK.webm", start_image="images/v10/Scene 6/Animations/RYANBODYHOOK/ryanbodystart.webp", image="images/v10/Scene 6/Animations/RYANBODYHOOK/ryanBodyEnd.webp", loop = False)
image ryankick = Movie(play="images/v10/Scene 6/Animations/RYANKICK/RYANKICK.webm", start_image="images/v10/Scene 6/Animations/RYANKICK/ryankickstart.webp", image="images/v10/Scene 6/Animations/RYANKICK/ryanKickEnd.webp", loop = False)

image Ryan_BodyJab_hit = "images/v10/Scene 6/Animations/END/MCRYAN-BODYHIT-END.webp"
image Ryan_BodyJab_block = "images/v10/Scene 6/Animations/END/MCRYAN-BODYBLOCKED-END.webp"
image Ryan_Hook_hit = "images/v10/Scene 6/Animations/END/MCRYAN-HOOKHIT-END.webp"
image Ryan_Hook_block = "images/v10/Scene 6/Animations/END/MCRYAN-HOOKBLOCKED-END.webp"
image Ryan_Jab_hit = "images/v10/Scene 6/Animations/END/MCRYAN-JABHIT-END.webp"
image Ryan_Jab_block = "images/v10/Scene 6/Animations/END/MCRYAN-JABBLOCKED-END.webp"
image Ryan_Kick_hit = "images/v10/Scene 6/Animations/END/MCRYAN-KICKHIT-END.webp"
image Ryan_Kick_block = "images/v10/Scene 6/Animations/END/MCRYAN-KICKBLOCKED-END.webp"

    # Imre Fight (Scene 7)
image mc_imre_BodyJab_hit = Movie(play="images/v10/Scene 7/Animations/MC-BODYHIT/MC-BODYHIT.webm", start_image="images/v10/scene 7/Animations/MC-BODYHIT/mc-bodyhitstart.webp", image="images/v10/scene 7/Animations/MC-BODYHIT/mc-bodyhitend.webp", loop = False)
image mc_imre_BodyJab_block = Movie(play="images/v10/Scene 7/Animations/MC-BODYBLOCK/MC-BODYBLOCKED.webm", start_image="images/v10/scene 7/Animations/MC-BODYBLOCK/mc-bodyblockstart.webp", image="images/v10/scene 7/Animations/MC-BODYBLOCK/mc-bodyblockedend.webp", loop = False)
image mc_imre_Hook_hit = Movie(play="images/v10/Scene 7/Animations/MC-HOOKHIT/MC-HOOKHIT.webm", start_image="images/v10/scene 7/Animations/MC-HOOKHIT/mc-hookhitstart.webp", image="images/v10/scene 7/Animations/MC-HOOKHIT/mc-hookhitend.webp", loop = False)
image mc_imre_Hook_block = Movie(play="images/v10/Scene 7/Animations/MC-HOOKBLOCKED/MC-HOOKBLOCKED.webm", start_image="images/v10/scene 7/Animations/MC-HOOKBLOCKED/mc-hookblockedstart.webp", image="images/v10/scene 7/Animations/MC-HOOKBLOCKED/mc-hookblockedend.webp", loop = False)
image mc_imre_Jab_hit = Movie(play="images/v10/Scene 7/Animations/MC-JABHIT/MC-JABHIT.webm", start_image="images/v10/scene 7/Animations/MC-JABHIT/mc-jabhitstart.webp", image="images/v10/scene 7/Animations/MC-JABHIT/mc-jabhitend.webp", loop = False)
image mc_imre_Jab_block = Movie(play="images/v10/Scene 7/Animations/MC-JABBLOCKED/MC-JABBLOCKED.webm", start_image="images/v10/scene 7/Animations/MC-JABBLOCKED/mc-jabblockedstart.webp", image="images/v10/scene 7/Animations/MC-JABBLOCKED/mc-jabblockedend.webp", loop = False)
image mc_imre_Kick_hit = Movie(play="images/v10/Scene 7/Animations/MC-KICKHIT/MC-KICKHIT.webm", start_image="images/v10/scene 7/Animations/MC-KICKHIT/mc-kickhitstart.webp", image="images/v10/scene 7/Animations/MC-KICKHIT/mc-kickhitend.webp", loop = False)
image mc_imre_Kick_block = Movie(play="images/v10/Scene 7/Animations/MC-KICKBLOCKED/MC-KICKBLOCKED.webm", start_image="images/v10/scene 7/Animations/MC-KICKBLOCKED/mc-kickblockedstart.webp", image="images/v10/scene 7/Animations/MC-KICKBLOCKED/mc-kickblockedend.webp", loop = False)

image imrejab = Movie(play="images/v10/Scene 7/Animations/IMREJAB/imreJAB.webm", start_image="images/v10/Scene 7/Animations/IMREJAB/imrejabstart.webp", image="images/v10/Scene 7/Animations/IMREJAB/imreJabEnd.webp", loop = False)
image imrehook = Movie(play="images/v10/Scene 7/Animations/IMREHOOK/imreHOOK.webm", start_image="images/v10/Scene 7/Animations/IMREHOOK/imrehookstart.webp", image="images/v10/Scene 7/Animations/IMREHOOK/imrehookend.webp", loop = False)
image imrebody = Movie(play="images/v10/Scene 7/Animations/IMREBODYHOOK/imreBODYHOOK.webm", start_image="images/v10/Scene 7/Animations/IMREBODYHOOK/imrebodyhookstart.webp", image="images/v10/Scene 7/Animations/IMREBODYHOOK/imreBodyEnd.webp", loop = False)
image imrekick = Movie(play="images/v10/Scene 7/Animations/IMREKICK/imreKICK.webm", start_image="images/v10/Scene 7/Animations/IMREKICK/imrekickstart.webp", image="images/v10/Scene 7/Animations/IMREKICK/imreKickEnd.webp", loop = False)

image Imre_BodyJab_hit = "images/v10/Scene 7/Animations/END/MCIMRE-BODYHIT-END.webp"
image Imre_BodyJab_block = "images/v10/Scene 7/Animations/END/MCIMRE-BODYBLOCKED-END.webp"
image Imre_Hook_hit = "images/v10/Scene 7/Animations/END/MCIMRE-HOOKHIT-END.webp"
image Imre_Hook_block = "images/v10/Scene 7/Animations/END/MCIMRE-HOOKBLOCKED-END.webp"
image Imre_Jab_hit = "images/v10/Scene 7/Animations/END/MCIMRE-JABHIT-END.webp"
image Imre_Jab_block = "images/v10/Scene 7/Animations/END/MCIMRE-JABBLOCKED-END.webp"
image Imre_Kick_hit = "images/v10/Scene 7/Animations/END/MCIMRE-KICKHIT-END.webp"
image Imre_Kick_block = "images/v10/Scene 7/Animations/END/MCIMRE-KICKBLOCKED-END.webp"

#region v12.0
#region Left Walkway Front
image v12s7_left_walkway_front_background_a = "images/v12/Scene 7/Screens/Navigation 12a.webp"
image v12s7_left_walkway_front_background_b = "images/v12/Scene 7/Screens/Navigation 12b.webp"

image v12s7_left_walkway_front_door_idle = Transform("v12s7_left_walkway_front_door_hover", alpha=0.0)
image v12s7_left_walkway_front_door_hover = "images/v12/Scene 7/Buttons/v12s7_left_walkway_front_door.webp"

image v12s7_left_walkway_front_penelope_idle = Transform("v12s7_left_walkway_front_penelope_hover", alpha=0.0)
image v12s7_left_walkway_front_penelope_hover = "images/v12/Scene 7/Buttons/v12s7_left_walkway_front_penelope.webp"

image v12s7_left_walkway_front_right_idle = Transform("v12s7_left_walkway_front_right_hover", alpha=0.0)
image v12s7_left_walkway_front_right_hover = "images/v12/Scene 7/Buttons/v12s7_left_walkway_front_right.webp"
#endregion Left Walkway Front

#region Balcony Left
image v12s7_balcony_left_background_a = "images/v12/Scene 7/Screens/Navigation 21a.webp"
image v12s7_balcony_left_background_b = "images/v12/Scene 7/Screens/Navigation 21b.webp"

image v12s7_balcony_left_nora_idle = Transform("v12s7_balcony_left_nora_hover", alpha=0.0)
image v12s7_balcony_left_nora_hover = "images/v12/Scene 7/Buttons/v12s7_balcony_left_nora.webp"
#endregion Balcony Left
#endregion v12.0