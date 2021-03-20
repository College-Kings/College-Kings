screen skipTutS28():
    tag fightScreen
    add "images/endfr.png"
    text "Would you like to play the fighting tutorial?" style "endfree"
    textbutton "Yes" style "endfr":
        action Jump("s28_fightTut")
        text_align 0.5
        xalign 0.57
        yalign 0.58

    textbutton "No" style "endfr":
        action Jump ("s28_LarsFightCont")
        text_align 0.5
        xalign 0.43
        yalign 0.58

screen s28_LarsFightChoice():
    tag fightScreen
    image "images/fightchoice.png"

    text "Fighting":
        xalign 0.5
        yalign 0.25
        font "fonts/Freshman.ttf"
        color "#ffffff"
        size 90
        xsize 500
        text_align 0.5
    text "Fighting is big part of College Kings, however you can simulate all fights if you'd like to.":
        xalign 0.5
        yalign 0.42
        font "fonts/OpenSans-Bold.ttf"
        color "#ffffff"
        xsize 500
        text_align 0.5


    textbutton "Play Fight":
        text_size 40
        xalign 0.5
        yalign 0.6
        action Jump ("s28_LarsFightDifficulty")

    textbutton "Simulate: realistic":
        text_size 40
        xalign 0.5
        yalign 0.7
        action Jump ("s28_LarsSimulateFight")

    textbutton "Simulate: auto-win":
        text_size 40
        xalign 0.5
        yalign 0.8
        action Jump ("s28_LarsAutoWin")


screen s28_LarsSelectDifficulty():
    tag fightScreen
    image "images/fightchoice.png"

    text "Difficulty":
        xalign 0.5
        yalign 0.25
        font "fonts/Freshman.ttf"
        color "#ffffff"
        size 90
        xsize 500
        text_align 0.5
    text "Higher difficulties require quicker reactions. You can change this at any time in the settings.":
        xalign 0.5
        yalign 0.42
        font "fonts/OpenSans-Bold.ttf"
        color "#ffffff"
        xsize 500
        text_align 0.5

    vbox xalign 0.45 yalign 0.75 spacing 30:
        textbutton "Easy":
            text_size 40
            action Jump ("s28_LarsEasyDifficulty")

        textbutton "Moderate":
            text_size 40
            action Jump ("s28_LarsModerateDifficulty")

        textbutton "Hard":
            text_size 40
            action Jump ("s28_LarsHardDifficulty")

screen s28_LarsKeybindOptions():
     tag fightScreen
   image "images/fightchoice.png"

    text "Keybinding":
        xalign 0.5
        yalign 0.25
        font "fonts/Freshman.ttf"
        color "#ffffff"
        size 90
        xsize 500
        text_align 0.5
    text "The current keybindings are:\n[q] = Jab / Block Head\n[w] = Hook / Block Face\n[r] = Kick / Block Leg":
        xalign 0.5
        yalign 0.42
        font "fonts/OpenSans-Bold.ttf"
        color "#ffffff"
        xsize 500
        text_align 0.5

    vbox xalign 0.45 yalign 0.75 spacing 30:
        textbutton "Change Keys":
            text_size 40
            action Jump ("changekeys")

        textbutton "Start Fight":
            text_size 40
            action Jump ("s28_LarsStartFight")

screen s28_mcLarsAttack():
    tag fightScreen

    if larsStance == 1:
        image "images\v08\Scene 28\fight images\LarsStance - Jab.jpg"

        key q:
            action Jump ("mc_LarsJabsHit")
        key w:
            action Jump ("mc_LarsHooksBlock")
        key e:
            action Jump ("mc_LarsBodyhookBlock")
        key r:
            action Jump ("mc_LarsKickBlock")

        imagebutton:
            idle "images/jab.png"
            hover "images/jab.png"
            xalign 0.06
            yalign 0.5
            action Jump ("mc_LarsJabsHit")

        imagebutton:
            idle "images/hook.png"
            hover "images/hook.png"
            xalign 0.115
            yalign 0.4
            action Jump ("mc_LarsHooksBlock")

        imagebutton:
            idle "images/body.png"
            hover "images/body.png"
            xalign 0.172
            yalign 0.5
            action Jump ("mc_LarsBodyhookBlock")

        imagebutton:
            idle "images/kick.png"
            hover "images/kick.png"
            xalign 0.115
            yalign 0.61
            action Jump ("mc_LarsKickBlock")


        timer reactiona action Jump("lars_McAttack")


    if larsStance == 2:
        image "images\v08\Scene 28\fight images\LarsStance - Bodyhook.jpg"

        key q:
            action Jump ("mc_LarsJabsBlock")
        key w:
            action Jump ("mc_LarsHooksBlock")
        key e:
            action Jump ("mc_LarsBodyhookHit")
        key r:
            action Jump ("mc_LarsKickBlock")

        imagebutton:
            idle "images/jab.png"
            hover "images/jab.png"
            xalign 0.06
            yalign 0.5
            action Jump ("mc_LarsJabsBlock")

        imagebutton:
            idle "images/hook.png"
            hover "images/hook.png"
            xalign 0.115
            yalign 0.4
            action Jump ("mc_LarsHooksBlock")

        imagebutton:
            idle "images/body.png"
            hover "images/body.png"
            xalign 0.172
            yalign 0.5
            action Jump ("mc_LarsBodyhookHit")

        imagebutton:
            idle "images/kick.png"
            hover "images/kick.png"
            xalign 0.115
            yalign 0.61
            action Jump ("mc_LarsKickBlock")



        timer reactiona action Jump("lars_McAttack")


    if larsStance == 3:
        image "images\v08\Scene 28\fight images\LarsStance - Hook.jpg"

        key q:
            action Jump ("mc_LarsJabsBlock")
        key w:
            action Jump ("mc_LarsHooksHit")
        key e:
            action Jump ("mc_LarsBodyhookBlock")
        key r:
            action Jump ("mc_LarsKickBlock")

        imagebutton:
            idle "images/jab.png"
            hover "images/jab.png"
            xalign 0.06
            yalign 0.5
            action Jump ("mc_LarsJabsBlock")

        imagebutton:
            idle "images/hook.png"
            hover "images/hook.png"
            xalign 0.115
            yalign 0.4
            action Jump ("mc_LarsHooksHit")

        imagebutton:
            idle "images/body.png"
            hover "images/body.png"
            xalign 0.172
            yalign 0.5
            action Jump ("mc_LarsBodyhookBlock")

        imagebutton:
            idle "images/kick.png"
            hover "images/kick.png"
            xalign 0.115
            yalign 0.61
            action Jump ("mc_LarsKickBlock")

        timer reactiona action Jump("lars_McAttack")

    if larsStance == 4:


        image "images\v08\Scene 28\fight images\LarsStance - Kick.jpg"

        key q:
            action Jump ("mc_LarsJabsBlock")
        key w:
            action Jump ("mc_LarsHooksBlock")
        key e:
            action Jump ("mc_LarsBodyhookBlock")
        key r:
            action Jump ("mc_LarsKickHit")

        imagebutton:
            idle "images/jab.png"
            hover "images/jab.png"
            xalign 0.06
            yalign 0.5
            action Jump ("mc_LarsJabsBlock")

        imagebutton:
            idle "images/hook.png"
            hover "images/hook.png"
            xalign 0.115
            yalign 0.4
            action Jump ("mc_LarsHooksBlock")

        imagebutton:
            idle "images/body.png"
            hover "images/body.png"
            xalign 0.172
            yalign 0.5
            action Jump ("mc_LarsBodyhookBlock")

        imagebutton:
            idle "images/kick.png"
            hover "images/kick.png"
            xalign 0.115
            yalign 0.61
            action Jump ("mc_LarsKickHit")

        timer reactiona action Jump("lars_McAttack")


screen s28_larsMcAttack():
    tag fightScreen

    if larsAttack == 1: # A
        image "images\v08\Scene 28\fight images\larshookend.jpg"

        key q:
            action Jump ("lars_McHookBlock")
        key w:
            action Jump ("lars_McHookHit")
        key e:
            action Jump ("lars_McHookHit")
        key r:
            action Jump ("lars_McHookHit")

        imagebutton:
            idle "images/hookblock.png"
            hover "images/hookblock.png"
            xalign 0.06
            yalign 0.5
            action Jump ("lars_McHookBlock")

        imagebutton:
            idle "images/jabblock.png"
            hover "images/jabblock.png"
            xalign 0.115
            yalign 0.4
            action Jump ("lars_McHookHit")

        imagebutton:
            idle "images/bodyblock.png"
            hover "images/bodyblock.png"
            xalign 0.172
            yalign 0.5
            action Jump ("lars_McHookHit")

        imagebutton:
            idle "images/kickblock.png"
            hover "images/kickblock.png"
            xalign 0.115
            yalign 0.6
            action Jump ("lars_McHookHit")


        timer reaction action Jump("lars_McHookHit")


    if larsAttack == 2:
        image "images\v08\Scene 28\fight images\larsjabend.jpg"

        key q:
            action Jump ("lars_McJabHit")
        key w:
            action Jump ("lars_McJabBlock")
        key e:
            action Jump ("lars_McJabHit")
        key r:
            action Jump ("lars_McJabHit")

        imagebutton:
            idle "images/hookblock.png"
            hover "images/hookblock.png"
            xalign 0.06
            yalign 0.5
            action Jump ("lars_McJabHit")

        imagebutton:
            idle "images/jabblock.png"
            hover "images/jabblock.png"
            xalign 0.115
            yalign 0.4
            action Jump ("lars_McJabBlock")

        imagebutton:
            idle "images/bodyblock.png"
            hover "images/bodyblock.png"
            xalign 0.172
            yalign 0.5
            action Jump ("lars_McJabHit")

        imagebutton:
            idle "images/kickblock.png"
            hover "images/kickblock.png"
            xalign 0.115
            yalign 0.6
            action Jump ("lars_McJabHit")

        timer reaction action Jump("lars_McJabHit")

    if larsAttack == 3:
        image "images\v08\Scene 28\fight images\larsbodyend.jpg"

        key q:
            action Jump ("lars_McBodyhookHit")
        key w:
            action Jump ("lars_McBodyhookHit")
        key e:
            action Jump ("lars_McBodyhookBlock")
        key r:
            action Jump ("lars_McBodyhookHit")

        imagebutton:
            idle "images/hookblock.png"
            hover "images/hookblock.png"
            xalign 0.06
            yalign 0.5
            action Jump ("lars_McBodyhookHit")

        imagebutton:
            idle "images/jabblock.png"
            hover "images/jabblock.png"
            xalign 0.115
            yalign 0.4
            action Jump ("lars_McBodyhookHit")

        imagebutton:
            idle "images/bodyblock.png"
            hover "images/bodyblock.png"
            xalign 0.172
            yalign 0.5
            action Jump ("lars_McBodyhookBlock")

        imagebutton:
            idle "images/kickblock.png"
            hover "images/kickblock.png"
            xalign 0.115
            yalign 0.6
            action Jump ("lars_McBodyhookHit")

        timer reaction action Jump("lars_McBodyhookHit")

    if larsAttack == 4:
        image "images\v08\Scene 28\fight images\larskickend.jpg"

        key q:
            action Jump ("lars_McKickHit")
        key w:
            action Jump ("lars_McKickHit")
        key e:
            action Jump ("lars_McKickHit")
        key r:
            action Jump ("lars_McKickBlock")

        imagebutton:
            idle "images/hookblock.png"
            hover "images/hookblock.png"
            xalign 0.06
            yalign 0.5
            action Jump ("lars_McKickHit")

        imagebutton:
            idle "images/jabblock.png"
            hover "images/jabblock.png"
            xalign 0.115
            yalign 0.4
            action Jump ("lars_McKickHit")

        imagebutton:
            idle "images/bodyblock.png"
            hover "images/bodyblock.png"
            xalign 0.172
            yalign 0.5
            action Jump ("lars_McKickHit")

        imagebutton:
            idle "images/kickblock.png"
            hover "images/kickblock.png"
            xalign 0.115
            yalign 0.6
            action Jump ("lars_McKickBlock")

        timer reaction action Jump("lars_McKickHit")