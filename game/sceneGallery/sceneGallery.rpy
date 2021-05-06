screen scenegal():
    tag menu

    add "images/sceneGallery/sceneGalleryBackground.webp"

    imagebutton:
        idle "images/backtransp.webp"
        hover "images/back.webp"
        pos (933, 79)
        action Return()

    vpgrid:
        cols 4
        spacing 40
        pos (78, 200)
        xpos 78
        ypos 200
        ysize 700
        scrollbars "vertical"
        draggable True
        mousewheel True

        imagebutton:
            idle "images/gallery1new.webp"
            hover "images/gallery1.webp"
            action Replay ("ga", locked = False)

        imagebutton:
            idle "images/gallery2new.webp"
            hover "images/gallery2.webp"
            action Replay ("gb", locked = False)

        imagebutton:
            idle "images/gallery3new.webp"
            hover "images/gallery3.webp"
            action Replay ("gc", locked = False)

        imagebutton:
            idle "images/gallery4new.webp"
            hover "images/gallery4.webp"
            action Replay ("fkcon", locked = False)

        imagebutton:
            idle "images/gallery6.webp"
            hover "images/gallery6outline.webp"
            action Replay ("ge", locked = False)

        imagebutton:
            idle "images/gallery5.webp"
            hover "images/gallery5outline.webp"
            action Replay ("gf", locked = False)

        imagebutton:
            idle "images/gallery7.webp"
            hover "images/gallery7outline.webp"
            action Replay ("rileysexscene", locked = False)

        imagebutton:
            idle "images/gallery8.webp"
            hover "images/gallery8outline.webp"
            action Replay ("brbj", locked = False)

        imagebutton:
            idle "images/gallery/gallery9.webp"
            hover "images/gallery/gallery9outline.webp"
            action Replay ("v08_cl_start", locked = False)

        imagebutton:
            idle "images/gallery/gallery10.webp"
            hover "images/gallery/gallery10outline.webp"
            action Replay ("v08_ri_start", locked = False)

        imagebutton:
            idle "images/gallery/gallery11.webp"
            hover "images/gallery/gallery11outline.webp"
            action Replay ("hoco_amb_night", locked = False)

        imagebutton:
            idle "images/gallery/gallery12.webp"
            hover "images/gallery/gallery12outline.webp"
            action Replay ("s28_LarsFight", locked = False)

        imagebutton:
            idle "images/gallery/gallery13.webp"
            hover "images/gallery/gallery13outline.webp"
            action Replay ("amber_sex_at_joshs", locked = False)

        imagebutton:
            idle Transform("images/gallery/gallery14.webp", size=(400, 226))
            hover Transform("images/gallery/gallery14_Hover.webp", size=(400, 226))
            action Replay ("v9_aubrey_scene_lake", locked = False)

        imagebutton:
            idle Transform("images/gallery/gallery15.webp", size=(400, 226))
            hover Transform("images/gallery/gallery15_Hover.webp", size=(400, 226))
            action Replay ("v9_emily_dorm", locked = False)

        imagebutton:
            idle Transform("images/gallery/gallery16.webp", size=(400, 226))
            hover Transform("images/gallery/gallery16_Hover.webp", size=(400, 226))
            action Replay ("v9_ri_sex", locked = False)

        imagebutton:
            idle Transform("images/gallery/gallery17.webp", size=(400, 226))
            hover Transform("images/gallery/gallery17_Hover.webp", size=(400, 226))
            action Replay ("v9_make_out_w_lin", locked = False)