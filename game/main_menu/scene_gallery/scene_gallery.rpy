default persistent.name = ""
default scopeDict = {}

init python:
    scene_gallery_items = []

    class SceneGallery:
        def __init__(self, title, image, label, scope=None):
            self.title = title
            self.image = image
            self.label = label

            if scope is None: self.scope = {}
            else: self.scope = scope

            scene_gallery_items.append(self)

    def update_scope(newScope):
        rv = scopeDict.copy()
        rv.update(newScope)
        return rv

    # SCENE GALLERY ITEMS HERE
    ## v1
    if renpy.loadable("v1/v1.rpy"):
        SceneGallery("Dreaming of Riley", "images/v1/sda1.webp", "sexdream1") # Riley, day 1

    ## v2
    if renpy.loadable("v2/v2.rpy"):
        SceneGallery("Fight with Tom", "images/v2/tomhook.webp", "v1_tomShoutBack") # Tom
    
    ## v3
    if renpy.loadable("v3/v3.rpy"):
        SceneGallery("First time with Aubrey", "images/v3/aub1start.webp", "continuem") # Aubrey, day 4

    ## v5
    if renpy.loadable("v5/v5.rpy"):
        SceneGallery("Fight with Adam", "images/v5/af5start.webp", "fkcon") # Adam

    ## v6
    if renpy.loadable("v6/v6.rpy"):
        SceneGallery("Taking back Emily", "images/v6/em5.webp", "emsex_a") # Emily, day 7
        SceneGallery("Fun with Aubrey", "images/v6/naub4.webp", "aubreysexb") # Aubrey, day 7

    ## v7
    if renpy.loadable("v7/v7.rpy"):
        SceneGallery("First time with Riley", "images/v7/risex1vid20.webp", "rileysexscene") # Riley, day 10
        SceneGallery("Sneaking to the stall", "images/v7/sfr4ri42.webp", "brbj") # Aubrey, day 11

    ## v8
    if renpy.loadable("v8/scene1.rpy"):
        SceneGallery("Homecoming Amber", "images/v8/scene 5/v8samb1.webp", "hoco_amb_night") # 5, Amber, day 11
        SceneGallery("Homecoming Chloe", "images/v8/scene 2/v8s16.webp", "v8_cl_start") # 2, Chloe, day 11
        SceneGallery("Homecoming Riley", "images/v8/scene 3/v8s33_2.webp", "v8_ri_start") # 3, Riley, day 11
        SceneGallery("Fight with Lars", "images/v8/scene 28/mcbodyhookstart.webp", "int_deal_w_josh") # 28, Lars Joe
        SceneGallery("With Amber at Josh's", "images/v8/scene 30/v8amber14a.webp", "amber_sex_at_joshs") # 30, Amber, day 14

    ## v9
    if renpy.loadable("v9/scene01.rpy"):
        SceneGallery("Lake w/ Aubrey", "images/v9/scene 7/v9slake18vidend.webp", "v9_aubrey_scene_lake") # 7, Aubrey, day 16
        SceneGallery("Emily sex scene", "images/v9/scene 16/v9emi33.webp", "v9_emily_dorm") # 16, Emily, day 17
        SceneGallery("Riley sex scene", "images/v9/scene 34/v9ris7a.webp", "v9_ri_sex") # 34, Riley, day 19, v9_sex_with_riley
        SceneGallery("Make out with Lindsey", "images/v9/scene 39/v9linksStart.webp", "v9_make_out_w_lin") # 39, Lindsey, day 19

    ## v10
    if renpy.loadable("v10/scene1.rpy"):
        SceneGallery("Ryan Fight", "images/v10/scene 6/v10mvr6.webp", "v10_mc_vs_ryan_fight") # 6, Ryan
        SceneGallery("Imre Fight", "images/v10/scene 7/v10mvi3.webp", "v10_mc_vs_imre_fight") # 7, Imre
        SceneGallery("More with Aubrey", "images/v10/scene 17/v10aubfaStart.webp", "v10s17_galleryScene") # 17, Aubrey, day 20
        SceneGallery("Make out with Lauren", "images/v10/scene 24/v10lar7d.webp", "v10_lauren_room_sg") # 24, Lauren, day 21 (scope is Lauren GIRLFRIEND)
        SceneGallery("Amber Skatepark Sex", "images/v10/scene 26/v10sasp11a.webp", "v10_amber_skatepark_sg") # 26, Amber, day 21
        SceneGallery("Changing with Chloe", "images/v10/scene 30/v10chg10f.webp", "v10s30_galleryScene") # 30, Chloe, day 22
        SceneGallery("More with Riley", "images/v10/scene 40/v10srds6a.webp", "v10s40_galleryScene") # 40, Riley, day 23 (scope is Riley FWB)

    ## v11
    if renpy.loadable("v11/scene1.rpy"):
        SceneGallery("First time with Candy", "images/v11/scene 5/v11swc25.webp", "v11s5_galleryScene") # 5, Candy, day 24
        SceneGallery("Airplane with Aubrey", "images/v11/scene 13/v11aub18a.webp", "v11_aubrey_plane_sex_sg") # 13, Aubrey, day 26
        SceneGallery("First time w/ Ms. Rose", "images/v11/scene 28/v11ros3.webp", "v11_ms_rose_sex_sg") # 28, Rose, day 27
        SceneGallery("Spa with Samantha", "images/v11/scene 28a/v11sas16a.webp", "v11s28a_galleryScene") # 28a, Samantha, day 27
        SceneGallery("In London with Riley", "images/v11/scene 35/v11ris18a.webp", "v11_riley_sex_sg") # 35, Riley, day 28
        SceneGallery("In London with Chloe", "images/v11/scene 41b/v11chtf2Start.webp", "v11_chloe_sex_scene") # 41b, Chloe, day 29

    ## v12
    if renpy.loadable("v12/scene1.rpy"):
        SceneGallery("Locked up with Lindsey", "images/v12/scene 17/v12esr33.webp", "v12_lindsey_sex") # 17, Lindsey, day 32
        SceneGallery("In Paris with Ms. Rose", "images/v12/scene 23/v12msr19.webp", "v12_ms_rose_sex_sg") # 23, Rose, day 33
        SceneGallery("First time with Lauren", "images/v12/scene 29/v12las58.webp", "v12_lauren_sex_sg") # 29, Lauren, day 34
        SceneGallery("First time with Nora", "images/v12/scene 35a/v12nos27.webp", "v12_nora_sex") # 35a, Nora, day 35

    ## v13
    if renpy.loadable("v13/scene1.rpy"):
        SceneGallery("Late night with Riley", "images/v13/scene 16a/v13s16a_7.webp", "v13s16a") # 16a, Riley, day 37
        SceneGallery("Fun with Emmy", "images/v13/scene 26/v13s26_5.webp", "v13s25_emmysg") # 26, Emmy, day 38
        SceneGallery("Wild with Chloe", "images/v13/scene 40/v13s40end_1.webp", "v13s40_sg") # 40, Chloe, day 39
        SceneGallery("Angry at Emily", "images/v13/scene 50a/v13s50a_5.webp", "v13s50a") # 50a, Emily, day 40

    ## v14
    if renpy.loadable("v14/scene1.rpy"):
        SceneGallery("Why not both?", "images/v14/scene 1/v14s01_4.webp", "v14s01") # 1, Riley Aubrey, xx
        SceneGallery("Satin-ly pleased", "images/v14/scene 3d/v14s03d_5.webp", "v14s03c_sg") # 3d, Satin, xx
        SceneGallery("Right here, right now", "images/v14/scene 21a/v14chlcgTPP.webp", "v14s21a") # 21a, Chloe, xx
        SceneGallery("Fuck while fucked up", "images/v14/scene 25a/v14s25a_17.webp", "v14s25a") # 25a, Amber, xx
        SceneGallery("Lagoon of love", "images/v14/scene 36/v14jenmo2Start.webp", "v14s36_sg") # 36, Jenny, xx
        SceneGallery("Good Dr. Lauren", "images/v14/scene 46a/v14s46a_12.webp", "v14s46a_sga") # 46a, Lauren good (scope is Lauren GIRLFRIEND)
        SceneGallery("Evil Dr. Lauren", "images/v14/scene 46a/v14s46a_27c.webp", "v14s46a_sgb") # 46a, Lauren bad
        SceneGallery("Messy with Samantha", "images/v14/scene 53a/v14s53a_16.webp", "v14s53_sg") # 53a, Samantha, xx

    ## v15
    if renpy.loadable("v15/scene1.rpy"):
        SceneGallery("Angry with Ms. Rose", "images/v15/scene 15/v15s15_7f.webp", "v15s15sg") # 15, Ms. Rose
        SceneGallery("The List (Amber)", "images/v15/scene 18a/v15s18aamber_9e.webp", "v15s18a_ambersg") # 18a, Amber
        SceneGallery("The List (Aubrey)", "images/3 hits.webp", "18c") # 18c, Aubrey
        SceneGallery("The List (Autumn)", "images/3 hits.webp", "18c") # 18c, Autumn
        SceneGallery("The List (Penelope)", "images/3 hits.webp", "18c") # 18c, Penelope
        SceneGallery("The List (Riley)", "images/v15/scene 18a/v15s18ariley_14.webp", "v15s18a_rileysg") # 18a, Riley
        SceneGallery("Birthday treat", "images/v15/scene 18e/v15s18eend_6.webp", "v15s18e_sg"), # 18e, Lauren
        SceneGallery("Fun at the wedding", "images/3 hits.webp", "33"), # 33, Naomi
        SceneGallery("Choosing Nora", "images/3 hits.webp", "48"), # 48, Nora


screen scene_gallery():
    tag menu
    modal True
    style_prefix "scene_gallery"

    default image_path = "main_menu/scene_gallery/images/"

    add image_path + "background.png"

    imagebutton:
        idle image_path + "return_idle.png"
        action ShowMenu("main_menu")
        pos (129, 82)

    fixed:
        pos (114, 178)
        ypos 178
        xysize (1688, 830)

        vpgrid id "vpg":
            cols 4
            spacing 20
            xalign 0.5
            top_margin 50
            mousewheel True
            
            for gallery_item in scene_gallery_items:
                fixed:
                    xysize (374, 264)

                    button:
                        background Transform(gallery_item.image, size=(362, 230), pos=(6, 6))
                        insensitive_background Transform(gallery_item.image, blur=50, size=(362, 230), pos=(6, 6))
                        idle_foreground image_path + "button_idle.png"
                        hover_foreground image_path + "button_hover.png"
                        insensitive_foreground image_path + "button_idle.png"
                        action Replay(gallery_item.label, scope=update_scope(gallery_item.scope))

                    fixed:
                        xysize (250, 49)
                        xalign 0.5
                        ypos 210

                        # add "#0f0"
                        text gallery_item.title.upper() align (0.5, 0.5)

    add image_path + "shadow.png" xalign 0.5 ypos 893

    add "scene_gallery_bar_base" pos (1743, 226) xysize (27, 734)
    vbar:
        pos (1748, 231)
        xysize (17, 724)
        base_bar "#0000"
        thumb image_path + "bar_thumb.png"
        value YScrollValue("vpg")



style scene_gallery_text is olympus_mount_30:
    size 25


label scene_gallery_name_change:
    scene black
    if not persistent.name.strip():
        $ persistent.name = renpy.input(_("What's your name?"), default=_("Alex")).strip() or _("Alex")

    $ scopeDict = {"name":persistent.name}

    return