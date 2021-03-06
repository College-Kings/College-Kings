define bugTesting_Scenes = [
    ["start", "Start of Game"],
    ["gf_b", "After Evelyn Date"],
    ["v07", "Start of v07"],
    ["conyourdorm", "Wednesday Morning"],
    ["rightafterbeach", "Wednesday Evening"],
    ["ep7_before_history", "Thursday Morning"],
    ["after_cam_history", "Asking girls to hoco"],
    ["risex", "RileySex"],
    ["fr4", "Homecoming Free Roam"],

]

screen bugTesting_SceneSelect():
    modal True
    zorder 200

    add "#23272a"

    imagebutton:
        action Hide("bugTesting_SceneSelect"), SetVariable("quick_menu", True)
        idle "/bugTesting/images/cheatMenuBackButton.png"
        hover im.MatrixColor("/bugTesting/images/cheatMenuBackButton.png", im.matrix.brightness(0.2))
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
