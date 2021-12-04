screen bugTesting_Overlay():
    $ fileLine = renpy.get_filename_line()
    text "[fileLine!q]" xpos 10 color "#0f0"

define bugTesting_Scenes = [
    ["start", "Start of Game"],
    ["v1start", "Start of v1"],
    ["v2start", "Start of v2"],
    ["v3start", "Start of v3"],
    ["v4start", "Start of v4"],
    ["v5start", "Start of v5"],
    ["v6start", "Start of v6"],
    ["v7start", "Start of v7"],
    ["conyourdorm", "Wednesday Morning"],
    ["rightafterbeach", "Wednesday Evening"],
    ["ep7_before_history", "Thursday Morning"],
    ["after_cam_history", "Asking girls to hoco"],
    ["fr4", "Homecoming Free Roam"],
    ["drug_deal_w_josh", "Scene 28 (Fight)"]
]

screen bugTesting_SceneSelect():
    modal True
    zorder 300
    
    add "#23272a"

    imagebutton:
        action Hide("bugTesting_SceneSelect"), SetVariable("quick_menu", True)
        idle "/bugTesting/images/cheatMenuBackButton.webp"
        hover Transform("/bugTesting/images/cheatMenuBackButton.webp", matrixcolor=BrightnessMatrix(0.2))
        pos (1666, 50)

    text "Bug Testing Scene Select" style "modTextHeader" align (0.5, 0.1)

    vpgrid:
        cols 4
        spacing 50
        align (0.5, 0.5)

        for gameScene in bugTesting_Scenes:
            textbutton gameScene[1]:
                action Jump(gameScene[0])
                text_style "modTextButtonHeader"