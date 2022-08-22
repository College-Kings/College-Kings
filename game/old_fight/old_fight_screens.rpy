screen fight_tutorial(highlight=None, stance="attack"):
    tag tag_fightTutorial

    add "images/fight_background.webp"

    text _("[w]"):
        align (0.122, 0.3)
        style "fight_tutorialText"
        if highlight == 'w':
            color "#d10000"
        else:
            color "#FFD166"

    text _("[e]"):
        align (0.235, 0.5)
        style "fight_tutorialText"
        if highlight == 'e':
            color "#d10000"
        else:
            color "#FFD166"

    text _("[q]"):
        align (0.02, 0.5)
        style "fight_tutorialText"
        if highlight == 'q':
            color "#d10000"
        else:
            color "#FFD166"

    text _("[r]"):
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

    text _("Fighting"):
        align (0.5, 0.25)
        font "fonts/Freshman.ttf"
        color "#ffffff"
        size 90
        xsize 500
        text_align 0.5

    text _("Fighting is big part of College Kings, however you can simulate all fights if you'd like to."):
        align (0.5, 0.42)
        font "fonts/OpenSans-Bold.ttf"
        color "#ffffff"
        xsize 500
        text_align 0.5

    textbutton _("Play Fight"):
        text_size 40
        align (0.5, 0.6)
        sensitive True
        action [SetVariable("fight_type", "normal"), Return()]

    textbutton _("Simulate: realistic"):
        text_size 40
        align (0.5, 0.7)
        sensitive True
        action [SetVariable("fight_type", "simReal"), Return()]

    textbutton _("Simulate: auto-win"):
        text_size 40
        align (0.5, 0.8)
        sensitive True
        action [SetVariable("fight_type", "simWin"), Return()]

    if config_debug:
        timer 0.1 action [SetVariable("fight_type", "normal"), Return()]


screen fight_selectDifficulty():
    tag tag_fight

    add "images/fightchoice.webp"

    text _("Difficulty"):
        align (0.5, 0.25)
        font "fonts/Freshman.ttf"
        color "#ffffff"
        size 90
        xsize 500
        text_align 0.5

    text _("Higher difficulties require quicker reactions. You can change this at any time in the settings."):
        align (0.5, 0.42)
        font "fonts/OpenSans-Bold.ttf"
        color "#ffffff"
        xsize 500
        text_align 0.5

    vbox:
        align(0.45, 0.75)
        spacing 30

        textbutton _("Easy"):
            text_size 40
            action [Function(selectDifficulty, "easy"), Return()]

        textbutton _("Moderate"):
            text_size 40
            action [Function(selectDifficulty, "normal"), Return()]

        textbutton _("Hard"):
            text_size 40
            action [Function(selectDifficulty, "hard"), Return()]

    if config_debug:
        timer 0.1 action [Function(selectDifficulty, "easy"), Return()]


screen fight_keybindOptions():
    tag tag_fight

    add "images/fightchoice.webp"
    default keybindText = _("\n[q!u] = Jab / Block Head\n[w!u] = Hook / Block Face\n[e!u] = Kick / Block Leg")

    text _("Keybinding"):
        align (0.5, 0.25)
        font "fonts/Freshman.ttf"
        color "#ffffff"
        size 90
        xsize 500
        text_align 0.5

    if bodyHook:
        $ keybindText += _("\n[r!u] = Body Hook / Low Guard")


    text _("The current keybindings are: [keybindText]"):
        align (0.5, 0.42)
        font "fonts/OpenSans-Bold.ttf"
        color "#ffffff"
        xsize 500
        text_align 0.5

    vbox:
        align (0.45, 0.75)
        spacing 30

        textbutton _("Change Keys"):
            text_size 40
            action Call("fight_changeKeybinds")

        textbutton _("Start Fight"):
            text_size 40
            action Return()

    if config_debug:
        timer 0.1 action Return()


screen fight_overlay(stance=None):
    add "images/fight_background.webp"

    text _("[w]"):
        align (0.122, 0.3)
        style "fight_overlayText"

    text _("[e]"):
        align (0.235, 0.5)
        style "fight_overlayText"

    text _("[q]"):
        align (0.02, 0.5)
        style "fight_overlayText"

    text _("[r]"):
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

    add "images/v2/tomstancekick.webp"

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

    if config_debug:
        timer 0.1 action Jump(renpy.random.choice("tomtut1hook", "tomtut1jab", "tomtut1kick"))


screen fight_defendTutorial():

    add "images/v2/tomhook.webp"

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

    if config_debug:
        timer 0.1 action Jump(renpy.random.choice("tuthookblock", "tuthookhit", "tuthookhit"))

screen youattack():

    if tomstance == 1:


        image "images/v2/tomstancekick.webp"

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
        image "images/v2/tomstancehook.webp"

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
        image "images/v2/tomstancejab.webp"

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

    if config_debug:
        python:
            if tomstance == 1:
                labels = ("tomkick1", "tomkick2", "tomkick3")

            if tomstance == 2:
                labels = ("tomhook1", "tomhook2", "tomhook3")

            if tomstance == 3:
                labels = ("tomjab1", "tomjab2", "tomjab3")

        timer 0.1 action Jump(renpy.random.choice(labels))



screen tomattack():

    if tomattack == 1:
        image "images/v2/tomhook.webp"

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
        image "images/v2/tomjab.webp"

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
        image "images/v2/tomkick.webp"

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

    if config_debug:
        python:
            if tomattack == 1:
                labels = ("tomhookhit", "tomhookblocked", "tomhookhit2")

            if tomattack == 2:
                labels = ("tomjabhit", "tomjabblocked", "tomjabhit2")

            if tomattack == 3:
                labels = ("tomkickhit", "tomkickhit2", "tomkickblocked")

        timer 0.1 action Jump(renpy.random.choice(labels))


screen larsFight_MCDefend(attack=None):
    tag fightScreen

    if attack == "Hook": # A
        add "images/v8/Scene 28/larshookend.webp"

        key q:
            action Jump ("lars_McHookBlock")
        key w:
            action Jump ("lars_McHookHit")
        key e:
            action Jump ("lars_McHookHit")
        key r:
            action Jump ("lars_McHookHit")

        imagebutton:
            idle "images/hookblock.webp"
            hover "images/hookblock.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("lars_McHookBlock")

        imagebutton:
            idle "images/jabblock.webp"
            hover "images/jabblock.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("lars_McHookHit")

        imagebutton:
            idle "images/bodyblock.webp"
            hover "images/bodyblock.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("lars_McHookHit")

        imagebutton:
            idle "images/kickblock.webp"
            hover "images/kickblock.webp"
            xalign 0.115
            yalign 0.6
            action Jump ("lars_McHookHit")

        timer reaction action Jump("lars_McHookHit")


    if attack == "Jab":
        add "images/v8/Scene 28/larsjabend.webp"

        key q:
            action Jump ("lars_McJabHit")
        key w:
            action Jump ("lars_McJabBlock")
        key e:
            action Jump ("lars_McJabHit")
        key r:
            action Jump ("lars_McJabHit")

        imagebutton:
            idle "images/hookblock.webp"
            hover "images/hookblock.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("lars_McJabHit")

        imagebutton:
            idle "images/jabblock.webp"
            hover "images/jabblock.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("lars_McJabBlock")

        imagebutton:
            idle "images/bodyblock.webp"
            hover "images/bodyblock.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("lars_McJabHit")

        imagebutton:
            idle "images/kickblock.webp"
            hover "images/kickblock.webp"
            xalign 0.115
            yalign 0.6
            action Jump ("lars_McJabHit")

        timer reaction action Jump("lars_McJabHit")

    if attack == "BodyHook":
        add "images/v8/Scene 28/larsbodyend.webp"

        key q:
            action Jump ("lars_McBodyhookHit")
        key w:
            action Jump ("lars_McBodyhookHit")
        key e:
            action Jump ("lars_McBodyhookBlock")
        key r:
            action Jump ("lars_McBodyhookHit")

        imagebutton:
            idle "images/hookblock.webp"
            hover "images/hookblock.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("lars_McBodyhookHit")

        imagebutton:
            idle "images/jabblock.webp"
            hover "images/jabblock.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("lars_McBodyhookHit")

        imagebutton:
            idle "images/bodyblock.webp"
            hover "images/bodyblock.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("lars_McBodyhookBlock")

        imagebutton:
            idle "images/kickblock.webp"
            hover "images/kickblock.webp"
            xalign 0.115
            yalign 0.6
            action Jump ("lars_McBodyhookHit")

        timer reaction action Jump("lars_McBodyhookHit")

    if attack == "Kick":
        image "images/v8/Scene 28/larskickend.webp"

        key q:
            action Jump ("lars_McKickHit")
        key w:
            action Jump ("lars_McKickHit")
        key e:
            action Jump ("lars_McKickHit")
        key r:
            action Jump ("lars_McKickBlock")

        imagebutton:
            idle "images/hookblock.webp"
            hover "images/hookblock.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("lars_McKickHit")

        imagebutton:
            idle "images/jabblock.webp"
            hover "images/jabblock.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("lars_McKickHit")

        imagebutton:
            idle "images/bodyblock.webp"
            hover "images/bodyblock.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("lars_McKickHit")

        imagebutton:
            idle "images/kickblock.webp"
            hover "images/kickblock.webp"
            xalign 0.115
            yalign 0.6
            action Jump ("lars_McKickBlock")

        timer reaction action Jump("lars_McKickHit")

    use fight_overlay

screen larsFight_MCAttack():
    tag fightScreen

    if larsStance == 1:
        add "images/v8/Scene 28/LarsStance - Jab.webp"

        key q:
            action Jump ("mc_LarsJabsHit")
        key w:
            action Jump ("mc_LarsHooksBlock")
        key e:
            action Jump ("mc_LarsBodyhookBlock")
        key r:
            action Jump ("mc_LarsKickBlock")

        imagebutton:
            idle "images/jab.webp"
            hover "images/jab.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("mc_LarsJabsHit")

        imagebutton:
            idle "images/hook.webp"
            hover "images/hook.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("mc_LarsHooksBlock")

        imagebutton:
            idle "images/body.webp"
            hover "images/body.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("mc_LarsBodyhookBlock")

        imagebutton:
            idle "images/kick.webp"
            hover "images/kick.webp"
            xalign 0.115
            yalign 0.61
            action Jump ("mc_LarsKickBlock")


        timer reactiona action Jump("lars_McAttack")


    if larsStance == 2:
        add "images/v8/Scene 28/LarsStance - Bodyhook.webp"

        key q:
            action Jump ("mc_LarsJabsBlock")
        key w:
            action Jump ("mc_LarsHooksBlock")
        key e:
            action Jump ("mc_LarsBodyhookHit")
        key r:
            action Jump ("mc_LarsKickBlock")

        imagebutton:
            idle "images/jab.webp"
            hover "images/jab.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("mc_LarsJabsBlock")

        imagebutton:
            idle "images/hook.webp"
            hover "images/hook.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("mc_LarsHooksBlock")

        imagebutton:
            idle "images/body.webp"
            hover "images/body.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("mc_LarsBodyhookHit")

        imagebutton:
            idle "images/kick.webp"
            hover "images/kick.webp"
            xalign 0.115
            yalign 0.61
            action Jump ("mc_LarsKickBlock")



        timer reactiona action Jump("lars_McAttack")


    if larsStance == 3:
        add "images/v8/Scene 28/LarsStance - Hook.webp"

        key q:
            action Jump ("mc_LarsJabsBlock")
        key w:
            action Jump ("mc_LarsHooksHit")
        key e:
            action Jump ("mc_LarsBodyhookBlock")
        key r:
            action Jump ("mc_LarsKickBlock")

        imagebutton:
            idle "images/jab.webp"
            hover "images/jab.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("mc_LarsJabsBlock")

        imagebutton:
            idle "images/hook.webp"
            hover "images/hook.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("mc_LarsHooksHit")

        imagebutton:
            idle "images/body.webp"
            hover "images/body.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("mc_LarsBodyhookBlock")

        imagebutton:
            idle "images/kick.webp"
            hover "images/kick.webp"
            xalign 0.115
            yalign 0.61
            action Jump ("mc_LarsKickBlock")

        timer reactiona action Jump("lars_McAttack")

    if larsStance == 4:
        add "images/v8/Scene 28/LarsStance - Kick.webp"

        key q:
            action Jump ("mc_LarsJabsBlock")
        key w:
            action Jump ("mc_LarsHooksBlock")
        key e:
            action Jump ("mc_LarsBodyhookBlock")
        key r:
            action Jump ("mc_LarsKickHit")

        imagebutton:
            idle "images/jab.webp"
            hover "images/jab.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("mc_LarsJabsBlock")

        imagebutton:
            idle "images/hook.webp"
            hover "images/hook.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("mc_LarsHooksBlock")

        imagebutton:
            idle "images/body.webp"
            hover "images/body.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("mc_LarsBodyhookBlock")

        imagebutton:
            idle "images/kick.webp"
            hover "images/kick.webp"
            xalign 0.115
            yalign 0.61
            action Jump ("mc_LarsKickHit")

        timer reactiona action Jump("lars_McAttack")

    use fight_overlay


screen ryanFight_MCDefend(attack=None):
    tag fightScreen

    if attack == "Hook": # A
        add "images/v10/Scene 6/Animations/RYANHOOK/ryanHookEnd.webp"

        key q:
            action Jump ("ryan_McHookBlock")
        key w:
            action Jump ("ryan_McHookHit")
        key e:
            action Jump ("ryan_McHookHit")
        key r:
            action Jump ("ryan_McHookHit")

        imagebutton:
            idle "images/hookblock.webp"
            hover "images/hookblock.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("ryan_McHookBlock")

        imagebutton:
            idle "images/jabblock.webp"
            hover "images/jabblock.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("ryan_McHookHit")

        imagebutton:
            idle "images/bodyblock.webp"
            hover "images/bodyblock.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("ryan_McHookHit")

        imagebutton:
            idle "images/kickblock.webp"
            hover "images/kickblock.webp"
            xalign 0.115
            yalign 0.6
            action Jump ("ryan_McHookHit")

        timer reaction action Jump("ryan_McHookHit")


    if attack == "Jab":
        add "images/v10/Scene 6/Animations/RYANJAB/ryanJabEnd.webp"

        key q:
            action Jump ("ryan_McJabHit")
        key w:
            action Jump ("ryan_McJabBlock")
        key e:
            action Jump ("ryan_McJabHit")
        key r:
            action Jump ("ryan_McJabHit")

        imagebutton:
            idle "images/hookblock.webp"
            hover "images/hookblock.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("ryan_McJabHit")

        imagebutton:
            idle "images/jabblock.webp"
            hover "images/jabblock.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("ryan_McJabBlock")

        imagebutton:
            idle "images/bodyblock.webp"
            hover "images/bodyblock.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("ryan_McJabHit")

        imagebutton:
            idle "images/kickblock.webp"
            hover "images/kickblock.webp"
            xalign 0.115
            yalign 0.6
            action Jump ("ryan_McJabHit")

        timer reaction action Jump("ryan_McJabHit")

    if attack == "BodyHook":
        add "images/v10/Scene 6/Animations/RYANBODYHOOK/ryanBodyEnd.webp"

        key q:
            action Jump ("ryan_McBodyhookHit")
        key w:
            action Jump ("ryan_McBodyhookHit")
        key e:
            action Jump ("ryan_McBodyhookBlock")
        key r:
            action Jump ("ryan_McBodyhookHit")

        imagebutton:
            idle "images/hookblock.webp"
            hover "images/hookblock.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("ryan_McBodyhookHit")

        imagebutton:
            idle "images/jabblock.webp"
            hover "images/jabblock.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("ryan_McBodyhookHit")

        imagebutton:
            idle "images/bodyblock.webp"
            hover "images/bodyblock.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("ryan_McBodyhookBlock")

        imagebutton:
            idle "images/kickblock.webp"
            hover "images/kickblock.webp"
            xalign 0.115
            yalign 0.6
            action Jump ("ryan_McBodyhookHit")

        timer reaction action Jump("ryan_McBodyhookHit")

    if attack == "Kick":
        image "images/v10/Scene 6/Animations/RYANKICK/ryanKickEnd.webp"

        key q:
            action Jump ("ryan_McKickHit")
        key w:
            action Jump ("ryan_McKickHit")
        key e:
            action Jump ("ryan_McKickHit")
        key r:
            action Jump ("ryan_McKickBlock")

        imagebutton:
            idle "images/hookblock.webp"
            hover "images/hookblock.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("ryan_McKickHit")

        imagebutton:
            idle "images/jabblock.webp"
            hover "images/jabblock.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("ryan_McKickHit")

        imagebutton:
            idle "images/bodyblock.webp"
            hover "images/bodyblock.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("ryan_McKickHit")

        imagebutton:
            idle "images/kickblock.webp"
            hover "images/kickblock.webp"
            xalign 0.115
            yalign 0.6
            action Jump ("ryan_McKickBlock")

        timer reaction action Jump("ryan_McKickHit")

    use fight_overlay

screen ryanFight_MCAttack():
    tag fightScreen

    if ryanStance == 1:
        add "images/v10/Scene 6/Animations/END/ryanStance - Jab.webp"

        key q:
            action Jump ("mc_ryanJabsHit")
        key w:
            action Jump ("mc_ryanHooksBlock")
        key e:
            action Jump ("mc_ryanBodyhookBlock")
        key r:
            action Jump ("mc_ryanKickBlock")

        imagebutton:
            idle "images/jab.webp"
            hover "images/jab.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("mc_ryanJabsHit")

        imagebutton:
            idle "images/hook.webp"
            hover "images/hook.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("mc_ryanHooksBlock")

        imagebutton:
            idle "images/body.webp"
            hover "images/body.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("mc_ryanBodyhookBlock")

        imagebutton:
            idle "images/kick.webp"
            hover "images/kick.webp"
            xalign 0.115
            yalign 0.61
            action Jump ("mc_ryanKickBlock")


        timer reactiona action Jump("ryan_McAttack")


    if ryanStance == 2:
        add "images/v10/Scene 6/Animations/END/ryanStance - Bodyhook.webp"

        key q:
            action Jump ("mc_ryanJabsBlock")
        key w:
            action Jump ("mc_ryanHooksBlock")
        key e:
            action Jump ("mc_ryanBodyhookHit")
        key r:
            action Jump ("mc_ryanKickBlock")

        imagebutton:
            idle "images/jab.webp"
            hover "images/jab.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("mc_ryanJabsBlock")

        imagebutton:
            idle "images/hook.webp"
            hover "images/hook.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("mc_ryanHooksBlock")

        imagebutton:
            idle "images/body.webp"
            hover "images/body.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("mc_ryanBodyhookHit")

        imagebutton:
            idle "images/kick.webp"
            hover "images/kick.webp"
            xalign 0.115
            yalign 0.61
            action Jump ("mc_ryanKickBlock")



        timer reactiona action Jump("ryan_McAttack")


    if ryanStance == 3:
        add "images/v10/Scene 6/Animations/END/ryanStance - Hook.webp"

        key q:
            action Jump ("mc_ryanJabsBlock")
        key w:
            action Jump ("mc_ryanHooksHit")
        key e:
            action Jump ("mc_ryanBodyhookBlock")
        key r:
            action Jump ("mc_ryanKickBlock")

        imagebutton:
            idle "images/jab.webp"
            hover "images/jab.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("mc_ryanJabsBlock")

        imagebutton:
            idle "images/hook.webp"
            hover "images/hook.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("mc_ryanHooksHit")

        imagebutton:
            idle "images/body.webp"
            hover "images/body.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("mc_ryanBodyhookBlock")

        imagebutton:
            idle "images/kick.webp"
            hover "images/kick.webp"
            xalign 0.115
            yalign 0.61
            action Jump ("mc_ryanKickBlock")

        timer reactiona action Jump("ryan_McAttack")

    if ryanStance == 4:
        add "images/v10/Scene 6/Animations/END/ryanStance - Kick.webp"

        key q:
            action Jump ("mc_ryanJabsBlock")
        key w:
            action Jump ("mc_ryanHooksBlock")
        key e:
            action Jump ("mc_ryanBodyhookBlock")
        key r:
            action Jump ("mc_ryanKickHit")

        imagebutton:
            idle "images/jab.webp"
            hover "images/jab.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("mc_ryanJabsBlock")

        imagebutton:
            idle "images/hook.webp"
            hover "images/hook.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("mc_ryanHooksBlock")

        imagebutton:
            idle "images/body.webp"
            hover "images/body.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("mc_ryanBodyhookBlock")

        imagebutton:
            idle "images/kick.webp"
            hover "images/kick.webp"
            xalign 0.115
            yalign 0.61
            action Jump ("mc_ryanKickHit")

        timer reactiona action Jump("ryan_McAttack")

    use fight_overlay


screen imreFight_MCDefend(attack=None):
    tag fightScreen

    if attack == "Hook": # A
        add "images/v10/Scene 7/Animations/IMREHOOK/imreHookEnd.webp"

        key q:
            action Jump ("imre_McHookBlock")
        key w:
            action Jump ("imre_McHookHit")
        key e:
            action Jump ("imre_McHookHit")
        key r:
            action Jump ("imre_McHookHit")

        imagebutton:
            idle "images/hookblock.webp"
            hover "images/hookblock.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("imre_McHookBlock")

        imagebutton:
            idle "images/jabblock.webp"
            hover "images/jabblock.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("imre_McHookHit")

        imagebutton:
            idle "images/bodyblock.webp"
            hover "images/bodyblock.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("imre_McHookHit")

        imagebutton:
            idle "images/kickblock.webp"
            hover "images/kickblock.webp"
            xalign 0.115
            yalign 0.6
            action Jump ("imre_McHookHit")

        timer reaction action Jump("imre_McHookHit")


    if attack == "Jab":
        add "images/v10/Scene 7/Animations/IMREJAB/imreJabEnd.webp"

        key q:
            action Jump ("imre_McJabHit")
        key w:
            action Jump ("imre_McJabBlock")
        key e:
            action Jump ("imre_McJabHit")
        key r:
            action Jump ("imre_McJabHit")

        imagebutton:
            idle "images/hookblock.webp"
            hover "images/hookblock.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("imre_McJabHit")

        imagebutton:
            idle "images/jabblock.webp"
            hover "images/jabblock.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("imre_McJabBlock")

        imagebutton:
            idle "images/bodyblock.webp"
            hover "images/bodyblock.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("imre_McJabHit")

        imagebutton:
            idle "images/kickblock.webp"
            hover "images/kickblock.webp"
            xalign 0.115
            yalign 0.6
            action Jump ("imre_McJabHit")

        timer reaction action Jump("imre_McJabHit")

    if attack == "BodyHook":
        add "images/v10/Scene 7/Animations/IMREBODYHOOK/imreBodyEnd.webp"

        key q:
            action Jump ("imre_McBodyhookHit")
        key w:
            action Jump ("imre_McBodyhookHit")
        key e:
            action Jump ("imre_McBodyhookBlock")
        key r:
            action Jump ("imre_McBodyhookHit")

        imagebutton:
            idle "images/hookblock.webp"
            hover "images/hookblock.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("imre_McBodyhookHit")

        imagebutton:
            idle "images/jabblock.webp"
            hover "images/jabblock.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("imre_McBodyhookHit")

        imagebutton:
            idle "images/bodyblock.webp"
            hover "images/bodyblock.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("imre_McBodyhookBlock")

        imagebutton:
            idle "images/kickblock.webp"
            hover "images/kickblock.webp"
            xalign 0.115
            yalign 0.6
            action Jump ("imre_McBodyhookHit")

        timer reaction action Jump("imre_McBodyhookHit")

    if attack == "Kick":
        image "images/v10/Scene 7/Animations/IMREKICK/imreKickEnd.webp"

        key q:
            action Jump ("imre_McKickHit")
        key w:
            action Jump ("imre_McKickHit")
        key e:
            action Jump ("imre_McKickHit")
        key r:
            action Jump ("imre_McKickBlock")

        imagebutton:
            idle "images/hookblock.webp"
            hover "images/hookblock.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("imre_McKickHit")

        imagebutton:
            idle "images/jabblock.webp"
            hover "images/jabblock.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("imre_McKickHit")

        imagebutton:
            idle "images/bodyblock.webp"
            hover "images/bodyblock.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("imre_McKickHit")

        imagebutton:
            idle "images/kickblock.webp"
            hover "images/kickblock.webp"
            xalign 0.115
            yalign 0.6
            action Jump ("imre_McKickBlock")

        timer reaction action Jump("imre_McKickHit")

    use fight_overlay

screen imreFight_MCAttack():
    tag fightScreen

    if imreStance == 1:
        add "images/v10/Scene 7/Animations/END/imreStance - Jab.webp"

        key q:
            action Jump ("mc_imreJabsHit")
        key w:
            action Jump ("mc_imreHooksBlock")
        key e:
            action Jump ("mc_imreBodyhookBlock")
        key r:
            action Jump ("mc_imreKickBlock")

        imagebutton:
            idle "images/jab.webp"
            hover "images/jab.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("mc_imreJabsHit")

        imagebutton:
            idle "images/hook.webp"
            hover "images/hook.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("mc_imreHooksBlock")

        imagebutton:
            idle "images/body.webp"
            hover "images/body.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("mc_imreBodyhookBlock")

        imagebutton:
            idle "images/kick.webp"
            hover "images/kick.webp"
            xalign 0.115
            yalign 0.61
            action Jump ("mc_imreKickBlock")


        timer reactiona action Jump("imre_McAttack")


    if imreStance == 2:
        add "images/v10/Scene 7/Animations/END/imreStance - Bodyhook.webp"

        key q:
            action Jump ("mc_imreJabsBlock")
        key w:
            action Jump ("mc_imreHooksBlock")
        key e:
            action Jump ("mc_imreBodyhookHit")
        key r:
            action Jump ("mc_imreKickBlock")

        imagebutton:
            idle "images/jab.webp"
            hover "images/jab.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("mc_imreJabsBlock")

        imagebutton:
            idle "images/hook.webp"
            hover "images/hook.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("mc_imreHooksBlock")

        imagebutton:
            idle "images/body.webp"
            hover "images/body.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("mc_imreBodyhookHit")

        imagebutton:
            idle "images/kick.webp"
            hover "images/kick.webp"
            xalign 0.115
            yalign 0.61
            action Jump ("mc_imreKickBlock")



        timer reactiona action Jump("imre_McAttack")


    if imreStance == 3:
        add "images/v10/Scene 7/Animations/END/imreStance - Hook.webp"

        key q:
            action Jump ("mc_imreJabsBlock")
        key w:
            action Jump ("mc_imreHooksHit")
        key e:
            action Jump ("mc_imreBodyhookBlock")
        key r:
            action Jump ("mc_imreKickBlock")

        imagebutton:
            idle "images/jab.webp"
            hover "images/jab.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("mc_imreJabsBlock")

        imagebutton:
            idle "images/hook.webp"
            hover "images/hook.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("mc_imreHooksHit")

        imagebutton:
            idle "images/body.webp"
            hover "images/body.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("mc_imreBodyhookBlock")

        imagebutton:
            idle "images/kick.webp"
            hover "images/kick.webp"
            xalign 0.115
            yalign 0.61
            action Jump ("mc_imreKickBlock")

        timer reactiona action Jump("imre_McAttack")

    if imreStance == 4:
        add "images/v10/Scene 7/Animations/END/imreStance - Kick.webp"

        key q:
            action Jump ("mc_imreJabsBlock")
        key w:
            action Jump ("mc_imreHooksBlock")
        key e:
            action Jump ("mc_imreBodyhookBlock")
        key r:
            action Jump ("mc_imreKickHit")

        imagebutton:
            idle "images/jab.webp"
            hover "images/jab.webp"
            xalign 0.06
            yalign 0.5
            action Jump ("mc_imreJabsBlock")

        imagebutton:
            idle "images/hook.webp"
            hover "images/hook.webp"
            xalign 0.115
            yalign 0.4
            action Jump ("mc_imreHooksBlock")

        imagebutton:
            idle "images/body.webp"
            hover "images/body.webp"
            xalign 0.172
            yalign 0.5
            action Jump ("mc_imreBodyhookBlock")

        imagebutton:
            idle "images/kick.webp"
            hover "images/kick.webp"
            xalign 0.115
            yalign 0.61
            action Jump ("mc_imreKickHit")

        timer reactiona action Jump("imre_McAttack")

    use fight_overlay