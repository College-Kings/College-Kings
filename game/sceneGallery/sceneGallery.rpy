default persistent.name = ""
default scopeDict = {}

init python:
    sceneGalleryItems = []

    class SceneGallery:
        def __init__(self, label, scope=None):
            self.label = label
            self.idleImg = "sceneGallery/images/gallery{}.webp".format(len(sceneGalleryItems) + 1)
            self.hoverImg = "sceneGallery/images/gallery{}_hover.webp".format(len(sceneGalleryItems) + 1)

            if scope is None: self.scope = {}
            else: self.scope = scope

            sceneGalleryItems.append(self)

    def updateScope(newScope):
        rv = scopeDict.copy()
        rv.update(newScope)
        return rv

    # SCENE GALLERY ITEMS HERE
        # v1
    if renpy.loadable("v1/v1.rpy"):
        SceneGallery("sexdream1") #Riley, day 1
        # v2
    if renpy.loadable("v2/v2.rpy"):
        SceneGallery("v1_tomShoutBack") #Tom
        # v3
    if renpy.loadable("v3/v3.rpy"):
        SceneGallery("continuem") #Aubrey, day 4
        # v5
    if renpy.loadable("v5/v5.rpy"):
        SceneGallery("fkcon") #Adam
        # v6
    if renpy.loadable("v6/v6.rpy"):
        SceneGallery("emsex_a") #Emily, day 7
        SceneGallery("aubreysexb") #Aubrey, day 7
        # v7
    if renpy.loadable("v7/v7.rpy"):
        SceneGallery("rileysexscene") #Riley, day 10
        SceneGallery("brbj") #Aubrey, day 11
        # v8
    if renpy.loadable("v8/scene1.rpy"):
        SceneGallery("v8_cl_start") #2, Chloe, day 11
        SceneGallery("v8_ri_start") #3, Riley, day 11
        SceneGallery("hoco_amb_night") #5, Amber, day 11
        SceneGallery("int_deal_w_josh") #28, Lars Joe
        SceneGallery("amber_sex_at_joshs") #30, Amber, day 14
        # v9
    if renpy.loadable("v9/scene01.rpy"):
        SceneGallery("v9_aubrey_scene_lake") #7, Aubrey, day 16
        SceneGallery("v9_emily_dorm") #16, Emily, day 17
        SceneGallery("v9_ri_sex") #34, Riley, day 19, v9_sex_with_riley
        SceneGallery("v9_make_out_w_lin") #39, Lindsey, day 19
        # v10
    if renpy.loadable("v10/scene1.rpy"):
        SceneGallery("v10_mc_vs_ryan_fight") #6, Ryan
        SceneGallery("v10_mc_vs_imre_fight") #7, Imre
        SceneGallery("v10s17_galleryScene") #17, Aubrey, day 20
        SceneGallery("v10_lauren_room_sg") #24, Lauren, day 21 (scope is Lauren GIRLFRIEND)
        SceneGallery("v10_amber_skatepark_sg") #26, Amber, day 21
        SceneGallery("v10s30_galleryScene") #30, Chloe, day 22
        SceneGallery("v10s40_galleryScene") #40, Riley, day 23 (scope is Riley FWB)
        # v11
    if renpy.loadable("v11/scene1.rpy"):
        SceneGallery("v11s5_galleryScene") #5, Candy, day 24
        SceneGallery("v11_aubrey_plane_sex_sg") #13, Aubrey, day 26
        SceneGallery("v11_ms_rose_sex_sg") #28, Rose, day 27
        SceneGallery("v11s28a_galleryScene") #28a, Samantha, day 27
        SceneGallery("v11_riley_sex_sg") #35, Riley, day 28
        SceneGallery("v11_chloe_sex_scene") #41b, Chloe, day 29
        #v12
    if renpy.loadable("v12/scene1.rpy"):
        SceneGallery("v12_lindsey_sex") #17, Lindsey, day 32
        SceneGallery("v12_ms_rose_sex_sg") #23, Rose, day 33
        SceneGallery("v12_lauren_sex_sg") #29, Lauren, day 34
        SceneGallery("v12_nora_sex") #35a, Nora, day 35
        #v13
    if renpy.loadable("v13/scene1.rpy"):
        SceneGallery("v13s16a") #16a, Riley, day 37
        SceneGallery("v13s25_emmysg") #26, Emmy, day 38
        SceneGallery("v13s40_sg") #40, Chloe, day 39
        SceneGallery("v13s50a") #50a, Emily, day 40
        #v14
    if renpy.loadable("v14/scene1.rpy"):
        SceneGallery("v14s01") #1, Riley Aubrey, xx
        SceneGallery("v14s03c_sg") #3d, Satin, xx
        SceneGallery("v14s21a") #21a, Chloe, xx
        SceneGallery("v14s25a") #25a, Amber, xx
        SceneGallery("v14s36_sg") #36, Jenny, xx
        SceneGallery("v14s46a_sga") #46a, Lauren good (scope is Lauren GIRLFRIEND)
        SceneGallery("v14s46a_sgb") #46a, Lauren bad
        SceneGallery("v14s53_sg") #53a, Samantha, xx

    ## v15
    if renpy.loadable("v15/scene1.rpy"):
        SceneGallery("15") #15, Ms. Rose - 47
        SceneGallery("18a") #18a, Riley - 48
        SceneGallery("18a") #18a, Amber - 49
        SceneGallery("18c") #18c, Aubrey - 50
        SceneGallery("18c") #18c, Autumn - 51
        SceneGallery("18c") #18c, Penelope - 52
        SceneGallery("18e"), #18e, Lauren - 53
        SceneGallery("33"), #33, Naomi - 54
        SceneGallery("48"), #48, Nora - 55


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
                action [Hide("spoiler"), ui.callsinnewcontext("sceneGalleryNameChange"), ShowMenu("scene_gallery")]

            textbutton "No":
                action Hide("spoiler")


screen scene_gallery():
    tag menu
    modal True

    add "sceneGallery/images/sceneGalleryBackground.webp"

    vpgrid:
        cols 4
        spacing 40
        pos (78, 200)
        ysize 700
        scrollbars "vertical"
        draggable True
        mousewheel True

        for sceneGalleryItem in sceneGalleryItems:
            imagebutton:
                action Replay(sceneGalleryItem.label, scope=updateScope(sceneGalleryItem.scope))
                idle Transform(sceneGalleryItem.idleImg, size=(400, 226))
                hover Transform(sceneGalleryItem.hoverImg, size=(400, 226))
                insensitive Transform(sceneGalleryItem.idleImg, blur=20, size=(400, 226))

    imagebutton:
        idle "images/backtransp.webp"
        hover "images/back.webp"
        pos (79, 933)
        action Show("main_menu")


label sceneGalleryNameChange:
    
    scene black
    if not persistent.name.strip():
        $ persistent.name = renpy.input(_("What's your name?"), default=_("Alex")).strip() or _("Alex")

    $ scopeDict = {"name":persistent.name}

    return