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
        SceneGallery("Fight with Tom", "images/v1/sda1.webp", "v1_tomShoutBack") # Tom
    
    ## v3
    if renpy.loadable("v3/v3.rpy"):
        SceneGallery("Fight time with Aubrey", "images/v1/sda1.webp", "continuem") # Aubrey, day 4

    ## v5
    if renpy.loadable("v5/v5.rpy"):
        SceneGallery("Fight with Adam", "images/v1/sda1.webp", "fkcon") # Adam

    ## v6
    if renpy.loadable("v6/v6.rpy"):
        SceneGallery("Taking back Emily", "images/v1/sda1.webp", "emsex_a") # Emily, day 7
        SceneGallery("Fun with Aubrey", "images/v1/sda1.webp", "aubreysexb") # Aubrey, day 7

    ## v7
    if renpy.loadable("v7/v7.rpy"):
        SceneGallery("First time with Riley", "images/v1/sda1.webp", "rileysexscene") # Riley, day 10
        SceneGallery("Sneaking to the stall", "images/v1/sda1.webp", "brbj") # Aubrey, day 11

    ## v8
    if renpy.loadable("v8/scene1.rpy"):
        SceneGallery("Homecoming Chloe", "images/v1/sda1.webp", "v8_cl_start") # 2, Chloe, day 11
        SceneGallery("Homecoming Riley", "images/v1/sda1.webp", "v8_ri_start") # 3, Riley, day 11
        SceneGallery("Homecoming Amber", "images/v1/sda1.webp", "hoco_amb_night") # 5, Amber, day 11
        SceneGallery("Fight with Lars", "images/v1/sda1.webp", "int_deal_w_josh") # 28, Lars Joe
        SceneGallery("With Amber at Josh's", "images/v1/sda1.webp", "amber_sex_at_joshs") # 30, Amber, day 14

    ## v9
    if renpy.loadable("v9/scene01.rpy"):
        SceneGallery("Lake w/ Aubrey", "images/v1/sda1.webp", "v9_aubrey_scene_lake") # 7, Aubrey, day 16
        SceneGallery("Emily sex scene", "images/v1/sda1.webp", "v9_emily_dorm") # 16, Emily, day 17
        SceneGallery("Riley sex scene", "images/v1/sda1.webp", "v9_ri_sex") # 34, Riley, day 19, v9_sex_with_riley
        SceneGallery("Make out with Lindsey", "images/v1/sda1.webp", "v9_make_out_w_lin") # 39, Lindsey, day 19

    ## v10
    if renpy.loadable("v10/scene1.rpy"):
        SceneGallery("Ryan Fight", "images/v1/sda1.webp", "v10_mc_vs_ryan_fight") # 6, Ryan
        SceneGallery("Imre Fight", "images/v1/sda1.webp", "v10_mc_vs_imre_fight") # 7, Imre
        SceneGallery("More with Aubrey", "images/v1/sda1.webp", "v10s17_galleryScene") # 17, Aubrey, day 20
        SceneGallery("Making out with Lauren", "images/v1/sda1.webp", "v10_lauren_room_sg") # 24, Lauren, day 21 (scope is Lauren GIRLFRIEND)
        SceneGallery("Amber Skatepark Sex", "images/v1/sda1.webp", "v10_amber_skatepark_sg") # 26, Amber, day 21
        SceneGallery("Changing with Chloe", "images/v1/sda1.webp", "v10s30_galleryScene") # 30, Chloe, day 22
        SceneGallery("More with Riley", "images/v1/sda1.webp", "v10s40_galleryScene") # 40, Riley, day 23 (scope is Riley FWB)

    ## v11
    if renpy.loadable("v11/scene1.rpy"):
        SceneGallery("Fight time with Candy", "images/v1/sda1.webp", "v11s5_galleryScene") # 5, Candy, day 24
        SceneGallery("Airplane with Aubrey", "images/v1/sda1.webp", "v11_aubrey_plane_sex_sg") # 13, Aubrey, day 26
        SceneGallery("First time w/ Ms. Rose", "images/v1/sda1.webp", "v11_ms_rose_sex_sg") # 28, Rose, day 27
        SceneGallery("First time w/ Samantha", "images/v1/sda1.webp", "v11s28a_galleryScene") # 28a, Samantha, day 27
        SceneGallery("In London with Riley", "images/v1/sda1.webp", "v11_riley_sex_sg") # 35, Riley, day 28
        SceneGallery("In London with Chloe", "images/v1/sda1.webp", "v11_chloe_sex_scene") # 41b, Chloe, day 29

    ## v12
    if renpy.loadable("v12/scene1.rpy"):
        SceneGallery("Locked up with Lindsey", "images/v1/sda1.webp", "v12_lindsey_sex") # 17, Lindsey, day 32
        SceneGallery("In Paris with Ms. Rose", "images/v1/sda1.webp", "v12_ms_rose_sex_sg") # 23, Rose, day 33
        SceneGallery("First time with Lauren", "images/v1/sda1.webp", "v12_lauren_sex_sg") # 29, Lauren, day 34
        SceneGallery("First time with Nora", "images/v1/sda1.webp", "v12_nora_sex") # 35a, Nora, day 35

    ## v13
    if renpy.loadable("v13/scene1.rpy"):
        SceneGallery("Late night with Riley", "images/v1/sda1.webp", "v13s16a") # 16a, Riley, day 37
        SceneGallery("Fun with Emmy", "images/v1/sda1.webp", "v13s25_emmysg") # 26, Emmy, day 38
        SceneGallery("Wild with Chloe", "images/v1/sda1.webp", "v13s40_sg") # 40, Chloe, day 39
        SceneGallery("Angry at Emily", "images/v1/sda1.webp", "v13s50a") # 50a, Emily, day 40

    ## v14
    if renpy.loadable("v14/scene1.rpy"):
        SceneGallery("Why not both?", "images/v1/sda1.webp", "v14s01") # 1, Riley Aubrey, xx
        SceneGallery("Satin-ly pleased", "images/v1/sda1.webp", "v14s03c_sg") # 3d, Satin, xx
        SceneGallery("Right here, right now", "images/v1/sda1.webp", "v14s21a") # 21a, Chloe, xx
        SceneGallery("Fuck while fucked up", "images/v1/sda1.webp", "v14s25a") # 25a, Amber, xx
        SceneGallery("Lagoon of love", "images/v1/sda1.webp", "v14s36_sg") # 36, Jenny, xx
        SceneGallery("Good Dr. Lauren", "images/v1/sda1.webp", "v14s46a_sga") # 46a, Lauren good (scope is Lauren GIRLFRIEND)
        SceneGallery("Evil Dr. Lauren", "images/v1/sda1.webp", "v14s46a_sgb") # 46a, Lauren bad
        SceneGallery("Messy with Samantha", "images/v1/sda1.webp", "v14s53_sg") # 53a, Samantha, xx

    ## v15
    if renpy.loadable("v15/scene1.rpy"):
        SceneGallery("Angry with Ms. Rose", "images/v1/sda1.webp", "15") # 15, Ms. Rose - 47
        SceneGallery("The List (Riley)", "images/v1/sda1.webp", "18a") # 18a, Riley - 48
        SceneGallery("The List (Amber)", "images/v1/sda1.webp", "18a") # 18a, Amber - 49
        SceneGallery("The List (Aubrey)", "images/v1/sda1.webp", "18c") # 18c, Aubrey - 50
        SceneGallery("The List (Autumn)", "images/v1/sda1.webp", "18c") # 18c, Autumn - 51
        SceneGallery("The List (Penelope)", "images/v1/sda1.webp", "18c") # 18c, Penelope - 52
        SceneGallery("Birthday treat", "images/v1/sda1.webp", "18e"), # 18e, Lauren - 53
        SceneGallery("Fun at the wedding", "images/v1/sda1.webp", "33"), # 33, Naomi - 54
        SceneGallery("Choosing Nora", "images/v1/sda1.webp", "48"), # 48, Nora - 55


screen scene_gallery_spoiler():
    modal True

    add "images/darker.webp"

    use endfrTemplate:
        text "Warning: The scene gallery contains spoilers for the story of the game. Are you sure you want to continue?":
            style "endfree"
            xalign 0.5

        hbox:
            align (0.5, 1.0)
            spacing 200

            textbutton "Yes":
                action [Hide("scene_gallery_spoiler"), ui.callsinnewcontext("scene_gallery_name_change"), ShowMenu("scene_gallery")]

            textbutton "No":
                action Hide("scene_gallery_spoiler")


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

        vpgrid:
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

                        text gallery_item.title.upper() align (0.5, 0.5)

    add image_path + "shadow.png" xalign 0.5 ypos 893


style scene_gallery_text is olympus_mount_30


label scene_gallery_name_change:
    scene black
    if not persistent.name.strip():
        $ persistent.name = renpy.input(_("What's your name?"), default=_("Alex")).strip() or _("Alex")

    $ scopeDict = {"name":persistent.name}

    return