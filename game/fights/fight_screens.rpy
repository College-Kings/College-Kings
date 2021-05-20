screen fightTutorial():
    tag fightScreen

    add "images/endfr.webp"
    text "Would you like to play the fighting tutorial?" style "endfree"

    textbutton "Yes" style "endfr":
        align (0.43, 0.58)
        action Call("fightTutorialLabel")
        text_align 0.5

    textbutton "No" style "endfr":
        align (0.57, 0.58)
        action Return()
        text_align 0.5


screen fightTutorialKeys(highlight=None):
    tag tag_fightTutorialKeys
    add "images/fight_background.webp"

    text "[w]":
        align (0.122, 0.3)
        style "fightTutorialText"
        if highlight == 'w':
            color "#d10000"
        else:
            color "#FFD166"

    text "[q]":
        align (0.02, 0.5)
        style "fightTutorialText"
        if highlight == 'q':
            color "#d10000"
        else:
            color "#FFD166"

    text "[e]":
        align (0.235, 0.5)
        style "fightTutorialText"
        if highlight == 'e':
            color "#d10000"
        else:
            color "#FFD166"

    text "[r]":
        align (0.122, 0.7)
        style "fightTutorialText"
        if highlight == 'r':
            color "#d10000"
        else:
            color "#FFD166"

    imagebutton:
        align (0.06, 0.5)
        idle "images/jab.webp"
        hover "images/jab.webp"

    imagebutton:
        align (0.115, 0.4)
        idle "images/hook.webp"
        hover "images/hook.webp"

    imagebutton:
        align (0.115, 0.61)
        idle "images/kick.webp"
        hover "images/kick.webp"


screen fight_typeMenu():
    tag fightScreen

    image "images/fightchoice.webp"

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
        xalign 0.5
        yalign 0.6
        action [SetVariable("fight_type", "normal"), Hide("fight_typeMenu"), Jump("fight")]

    textbutton "Simulate: realistic":
        text_size 40
        xalign 0.5
        yalign 0.7
        action [SetVariable("fight_type", "simReal"), Hide("fight_typeMenu"), Jump("fight")]

    textbutton "Simulate: auto-win":
        text_size 40
        xalign 0.5
        yalign 0.8
        action [SetVariable("fight_type", "simWin"), Hide("fight_typeMenu"), Jump("fight")]


screen fight_selectDifficulty():
    tag fightScreen
    image "images/fightchoice.webp"

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
            action [Function(selectDifficulty, "easy"), Show("fight_keybindOptions")]

        textbutton "Moderate":
            text_size 40
            action [Function(selectDifficulty, "normal"), Show("fight_keybindOptions")]

        textbutton "Hard":
            text_size 40
            action [Function(selectDifficulty, "hard"), Show("fight_keybindOptions")]


screen fight_keybindOptions():
    tag fightScreen
    image "images/fightchoice.webp"

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
            action Jump ("startFight")