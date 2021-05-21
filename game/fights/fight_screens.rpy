screen fight_tutorialPopup():
    tag tag_fight

    add "images/endfr.webp"
    text "Would you like to play the fighting tutorial?" style "endfree"

    textbutton "Yes" style "endfr":
        align (0.43, 0.58)
        action [SetVariable("fight_tutorial", True), Call("fight_tutorialLabel")]
        text_align 0.5

    textbutton "No" style "endfr":
        align (0.57, 0.58)
        action [SetVariable("fight_tutorial", False), Return()]
        text_align 0.5


screen fight_tutorial(highlight=None, stance="attack"):
    tag tag_fightTutorial

    add "images/fight_background.webp"

    text "[w]":
        align (0.122, 0.3)
        style "fight_tutorialText"
        if highlight == 'w':
            color "#d10000"
        else:
            color "#FFD166"

    text "[e]":
        align (0.235, 0.5)
        style "fight_tutorialText"
        if highlight == 'e':
            color "#d10000"
        else:
            color "#FFD166"

    text "[q]":
        align (0.02, 0.5)
        style "fight_tutorialText"
        if highlight == 'q':
            color "#d10000"
        else:
            color "#FFD166"

    text "[r]":
        align (0.122, 0.7)
        style "fight_tutorialText"
        if highlight == 'r':
            color "#d10000"
        else:
            color "#FFD166"

    if stance == "attack":
        add "images/hook.webp" align (0.115, 0.4)
        add "images/kick.webp" align (0.115, 0.61)
        add "images/jab.webp" align (0.06, 0.5)
    else:
        add "images/jabblock.webp" align (0.115, 0.4)
        add "images/kickblock.webp" align (0.115, 0.61)
        add "images/hookblock.webp" align (0.06, 0.5)


screen fight_typeMenu():
    tag tag_fight

    add "images/fightchoice.webp"

    text "Fighting":
        align (0.5, 0.25)
        font "fonts/Freshman.ttf"
        color "#ffffff"
        size 90
        xsize 500
        text_align 0.5

    text "Fighting is big part of College Kings, however you can simulate all fights if you'd like to.":
        align (0.5, 0.42)
        font "fonts/OpenSans-Bold.ttf"
        color "#ffffff"
        xsize 500
        text_align 0.5

    textbutton "Play Fight":
        text_size 40
        align (0.5, 0.6)
        sensitive True
        action [SetVariable("fight_type", "normal"), Return()]

    textbutton "Simulate: realistic":
        text_size 40
        align (0.5, 0.7)
        sensitive True
        action [SetVariable("fight_type", "simReal"), Return()]

    textbutton "Simulate: auto-win":
        text_size 40
        align (0.5, 0.8)
        sensitive True
        action [SetVariable("fight_type", "simWin"), Return()]


screen fight_selectDifficulty():
    tag tag_fight

    add "images/fightchoice.webp"

    text "Difficulty":
        align (0.5, 0.25)
        font "fonts/Freshman.ttf"
        color "#ffffff"
        size 90
        xsize 500
        text_align 0.5

    text "Higher difficulties require quicker reactions. You can change this at any time in the settings.":
        align (0.5, 0.42)
        font "fonts/OpenSans-Bold.ttf"
        color "#ffffff"
        xsize 500
        text_align 0.5

    vbox:
        align(0.45, 0.75)
        spacing 30

        textbutton "Easy":
            text_size 40
            action [Function(selectDifficulty, "easy"), Return()]

        textbutton "Moderate":
            text_size 40
            action [Function(selectDifficulty, "normal"), Return()]

        textbutton "Hard":
            text_size 40
            action [Function(selectDifficulty, "hard"), Return()]


screen fight_keybindOptions():
    tag tag_fight

    add "images/fightchoice.webp"

    text "Keybinding":
        align (0.5, 0.25)
        font "fonts/Freshman.ttf"
        color "#ffffff"
        size 90
        xsize 500
        text_align 0.5

    if bodyHook:
        $ keybindText = "\n[q] = Jab / Block Head\n[w] = Hook / Block Face\n[r] = Kick / Block Leg\n[e] = Body Hook / Low Guard"
    else:
        $ keybindText = "\n[q] = Jab / Block Head\n[w] = Hook / Block Face\n[r] = Kick / Block Leg"

    text "The current keybindings are:[keybindText]":
        align (0.5, 0.42)
        font "fonts/OpenSans-Bold.ttf"
        color "#ffffff"
        xsize 500
        text_align 0.5

    vbox:
        align (0.45, 0.75)
        spacing 30

        textbutton "Change Keys":
            text_size 40
            action Call("fight_changeKeybinds")

        textbutton "Start Fight":
            text_size 40
            action Return()


screen fight_overlay(stance=None):
    add "images/fight_background.webp"

    text "[w]":
        align (0.122, 0.3)
        style "fight_overlayText"

    text "[e]":
        align (0.235, 0.5)
        style "fight_overlayText"

    text "[q]":
        align (0.02, 0.5)
        style "fight_overlayText"

    text "[r]":
        align (0.122, 0.7)
        style "fight_overlayText"

    if stance == "attack":
        add "images/hook.webp" align (0.115, 0.4)
        add "images/body.webp" align (0.172, 0.5)
        add "images/kick.webp" align (0.115, 0.61)
        add "images/jab.webp" align (0.06, 0.5)
    elif stance == "defend":
        add "images/jabblock.webp" align (0.115, 0.4)
        add "images/bodyblock.webp" align (0.172, 0.5)
        add "images/kickblock.webp" align (0.115, 0.61)
        add "images/hookblock.webp" align (0.06, 0.5)

# Tom Fight
screen tomtut1():
    tag fightScreen

    add "images/tomstancekick.webp"

    key w:
        action Jump ("tomtut1hook")
    key q:
        action Jump ("tomtut1jab")
    key r:
        action Jump ("tomtut1kick")

    imagebutton:
        idle "images/jab.webp"
        hover "images/jab.webp"
        action Jump ("tomtut1jab")
        align (0.06, 0.5)

    imagebutton:
        idle "images/hook.webp"
        hover "images/hook.webp"
        action Jump ("tomtut1hook")
        align (0.115, 0.4)

    imagebutton:
        idle "images/kick.webp"
        hover "images/kick.webp"
        action Jump ("tomtut1kick")
        align (0.115, 0.61)

    use fight_overlay

screen fight_defendTutorial():

    add "images/tomhook.webp"

    key q:
        action Jump ("tuthookblock")
    key w:
        action Jump ("tuthookhit")
    key r:
        action Jump ("tuthookhit")

    imagebutton:
        idle "images/hookblock.webp"
        hover "images/hookblock.webp"
        xalign 0.06
        yalign 0.5
        action Jump ("tuthookblock")

    imagebutton:
        idle "images/jabblock.webp"
        hover "images/jabblock.webp"
        xalign 0.115
        yalign 0.4
        action Jump ("tuthookhit")

    imagebutton:
        idle "images/kickblock.webp"
        hover "images/kickblock.webp"
        xalign 0.115
        yalign 0.6
        action Jump ("tuthookhit")

    use fight_overlay


screen youattack():

    if tomstance == 1:


        image "images/tomstancekick.webp"

        key r:
            action Jump ("tomkick1")
        key w:
            action Jump ("tomkick2")
        key q:
            action Jump ("tomkick3")

        imagebutton:
            idle "images/jab.webp"
            hover "images/jab.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("tomkick3")

        imagebutton:
            idle "images/hook.webp"
            hover "images/hook.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("tomkick2")


        imagebutton:
            idle "images/kick.webp"
            hover "images/kick.webp"
            xalign 0.115
            yalign 0.61
            action Jump ("tomkick1")

        timer reactiona action Jump("timer1")



    if tomstance == 2:
        image "images/tomstancehook.webp"

        key w:
            action Jump ("tomhook1")
        key q:
            action Jump ("tomhook2")
        key r:
            action Jump ("tomhook3")

        imagebutton:
            idle "images/jab.webp"
            hover "images/jab.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("tomhook2")

        imagebutton:
            idle "images/hook.webp"
            hover "images/hook.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("tomhook1")


        imagebutton:
            idle "images/kick.webp"
            hover "images/kick.webp"
            xalign 0.115
            yalign 0.61
            action Jump ("tomhook3")

        timer reactiona action Jump("timer2")



    if tomstance == 3:
        image "images/tomstancejab.webp"

        key q:
            action Jump ("tomjab1")
        key w:
            action Jump ("tomjab2")
        key r:
            action Jump ("tomjab3")

        imagebutton:
            idle "images/jab.webp"
            hover "images/jab.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("tomjab1")

        imagebutton:
            idle "images/hook.webp"
            hover "images/hook.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("tomjab2")


        imagebutton:
            idle "images/kick.webp"
            hover "images/kick.webp"
            xalign 0.115
            yalign 0.61
            action Jump ("tomjab3")


        timer reactiona action Jump("timer3")

    use fight_overlay


screen tomattack():

    if tomattack == 1:
        image "images/tomhook.webp"

        key r:
            action Jump ("tomhookhit")
        key q:
            action Jump ("tomhookblocked")
        key w:
            action Jump ("tomhookhit2")

        imagebutton:
            idle "images/hookblock.webp"
            hover "images/hookblock.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("tomhookblocked")

        imagebutton:
            idle "images/jabblock.webp"
            hover "images/jabblock.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("tomhookhit")

        imagebutton:
            idle "images/kickblock.webp"
            hover "images/kickblock.webp"
            xalign 0.115
            yalign 0.6
            action Jump ("tomhookhit2")

        timer reaction action Jump("timer4")


    if tomattack == 2:
        image "images/tomjab.webp"

        key q:
            action Jump ("tomjabhit")
        key w:
            action Jump ("tomjabblocked")
        key r:
            action Jump ("tomjabhit2")

        imagebutton:
            idle "images/hookblock.webp"
            hover "images/hookblock.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("tomjabhit")

        imagebutton:
            idle "images/jabblock.webp"
            hover "images/jabblock.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("tomjabblocked")

        imagebutton:
            idle "images/kickblock.webp"
            hover "images/kickblock.webp"
            xalign 0.115
            yalign 0.6
            action Jump ("tomjabhit2")

        timer reaction action Jump("timer5")

    if tomattack == 3:
        image "images/tomkick.webp"

        key w:
            action Jump ("tomkickhit")
        key q:
            action Jump ("tomkickhit2")
        key r:
            action Jump ("tomkickblocked")


        imagebutton:
            idle "images/hookblock.webp"
            hover "images/hookblock.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("tomkickhit")

        imagebutton:
            idle "images/jabblock.webp"
            hover "images/jabblock.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("tomkickhit2")

        imagebutton:
            idle "images/kickblock.webp"
            hover "images/kickblock.webp"
            xalign 0.115
            yalign 0.6
            action Jump ("tomkickblocked")

        timer reaction action Jump("timer6")

    use fight_overlay