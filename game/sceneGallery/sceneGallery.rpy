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

    ## SCENE GALLERY ITEMS HERE
    SceneGallery("sexdream1")
    SceneGallery("v1_tomShoutBack")
    SceneGallery("continuem")
    SceneGallery("fkcon")
    SceneGallery("aubreysexb")
    SceneGallery("emsex_a")
    SceneGallery("rileysexscene")
    SceneGallery("brbj")
    SceneGallery("v8_cl_start")
    SceneGallery("v8_ri_start")
    SceneGallery("hoco_amb_night")
    SceneGallery("int_deal_w_josh")
    SceneGallery("amber_sex_at_joshs")
    SceneGallery("v9_aubrey_scene_lake")
    SceneGallery("v9_emily_dorm")
    SceneGallery("v9_ri_sex")
    SceneGallery("v9_make_out_w_lin")
        # v10.0
    SceneGallery("v10_mc_vs_ryan_fight")
    SceneGallery("v10_mc_vs_imre_fight")
    SceneGallery("v10s17_galleryScene")
    SceneGallery("v10_lauren_room_sg")
    SceneGallery("v10_amber_skatepark_sg")
    SceneGallery("v10s30_galleryScene")
    SceneGallery("v10s40_galleryScene", scope={"rileyrs": True})

screen spoiler():
    modal True

    add "images/darker.webp"

    add "images/endfr.webp"
    text "Warning: The scene gallery contains spoilers for the story of the game. Are you sure you want to continue?" style "endfree"

    textbutton "Yes":
        style "endfr"
        text_align 0.5
        align (0.43, 0.58)
        action [Hide("spoiler"), ui.callsinnewcontext("sceneGalleryNameChange"), Show("sceneGallery")]

    textbutton "No":
        style "endfr"
        text_align 0.5
        align (0.57, 0.58)
        action Hide("spoiler")


screen sceneGallery():
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
                insensitive Transform(im.Blur(sceneGalleryItem.idleImg, 3), size=(400, 226))

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