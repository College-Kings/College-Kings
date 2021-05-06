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
    SceneGallery("bj_a")
    SceneGallery("continuem")
    SceneGallery("fkcon")
    SceneGallery("emsex_a")
    SceneGallery("aubreysexb")
    SceneGallery("rileysexscene")
    SceneGallery("brbj")
    SceneGallery("v08_cl_start")
    SceneGallery("v08_ri_start")
    SceneGallery("hoco_amb_night")
    SceneGallery("s28_LarsFight")
    SceneGallery("amber_sex_at_joshs")
    SceneGallery("v9_aubrey_scene_lake")
    SceneGallery("v9_emily_dorm")
    SceneGallery("v9_ri_sex")
    SceneGallery("v9_make_out_w_lin")

screen scenegal():
    tag menu

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

    imagebutton:
        idle "images/backtransp.webp"
        hover "images/back.webp"
        pos (933, 79)
        action Return()