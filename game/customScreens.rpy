screen alert_template(message):
    zorder 200
    modal True
    style_prefix "alert"

    python:
        message = message.upper()
        message = message.replace("{B}", "{b}")
        message = message.replace("{/B}", "{/b}")

    frame:
        align (0.5, 0.5)
        minimum (758, 363)
        background "alert_background"

        vbox:
            align (0.5, 0.5)
            spacing 45

            text _(message) xalign 0.5 xsize 650

            hbox:
                xalign 0.5
                spacing 20

                transclude

style alert_text is bebas_neue_30


screen warning_template(message, style="blue"):
    zorder 200
    modal True
    style_prefix "warning"

    frame:
        align (0.5, 0.5)
        yoffset -42
        minimum (758, 363)
        background "warning_background_{}".format(style)

        vbox:
            align (0.5, 0.5)
            spacing 45

            null height 50

            text _(message.upper()) xalign 0.5 xsize 650

            hbox:
                xalign 0.5
                spacing 20
                
                transclude

            null height 50

style warning_text is bebas_neue_30


screen popup(message):
    frame:
        background "alert_background"
        padding (30, 10)
        pos (10, 10)
        at achievementShow

        text _(message)

    timer 4 action Hide("popup")


screen real_life_mode():
    modal True

    add "images/start/real_life_mode_background.webp"

    use warning_template("THIS MODE PROHIBITS you from saving during important choices, meaning all choices are final. this can't be disabled without starting a new game."):

        button:
            idle_background "blue_button_idle"
            hover_background "blue_button_hover"
            action [SetVariable("realmode", True), SetVariable("config.rollback_enabled", False), SetVariable("showkct", False), Show("phone_icon"), Jump("v1start")]
            xysize (215, 55)

            text "ENABLE" align (0.5, 0.5)

        button:
            idle_background "blue_button_idle"
            hover_background "blue_button_hover"
            action [SetVariable("realmode", False), SetVariable("config.rollback_enabled", True), SetVariable("showkct", True), Show("phone_icon"), Jump("v1start")]
            xysize (215, 55)

            text "DISABLE" align (0.5, 0.5)


screen fantasyOverlay():
    add "images/fantasyoverlay.webp"


screen censored_popup(continueLabel):
    modal True

    add "gui/censoredPopup/censoredBackground.webp"

    text "THE NEXT SCENE HAS NSFW CONTENT":
        size 70
        color "#FFFFFF"
        style "nsfw_text"
        xalign 0.5
        ypos 125

    text "* CONTENT NOT SUITABLE FOR TWITCH OR YOUTUBE":
        size 40
        color "#FFFFFF"
        style "nsfw_italic_text"
        xalign 0.5
        ypos 255

    vbox:
        ypos 450
        xalign 0.5
        xsize 1050

        if config_censored:
            text "TO VIEW THIS SCENE YOU MUST HAVE NSFW ENABLED":
                size 35
                color "#FFFFFF"
                style "nsfw_text"
                xalign 0.5

            text "IN THE SETTINGS MENU":
                size 35
                color "#FFFFFF"
                style "nsfw_text"
                xalign 0.5

        else:
            text "YOU HAVE NSFW CONTENT ENABLED SO YOU MAY":
                size 35
                color "#FFFFFF"
                style "nsfw_text"
                xalign 0.5

            text "CONTINUE TO VIEW THE FOLLOWING SCENE":
                size 35
                color "#FFFFFF"
                style "nsfw_text"
                xalign 0.5

    text "OR YOU MAY CHOOSE TO SKIP THIS SCENE":
        size 35
        color "#FFFFFF"
        style "nsfw_text"
        xalign 0.5
        ypos 730
        xsize 1050    

    if config_censored:
        imagebutton:
            idle Transform("gui/censoredPopup/censoredSettings.webp", zoom=0.65)
            hover Transform("gui/censoredPopup/censoredSettingsHover.webp", zoom=0.65)
            action ShowMenu("preferences")
            xalign 0.5
            ypos 555
    else:
        imagebutton:
            idle Transform("gui/censoredPopup/censoredContinue.webp", zoom=0.65)
            hover Transform("gui/censoredPopup/censoredContinueHover.webp", zoom=0.65)
            action Return()
            xalign 0.5
            ypos 555

    imagebutton:
        idle Transform("gui/censoredPopup/censoredSkipScene.webp", zoom=0.65)
        hover Transform("gui/censoredPopup/censoredSkipSceneHover.webp", zoom=0.65)
        action Jump(continueLabel)
        xalign 0.5
        ypos 790

style nsfw_text is text:
    font "fonts/Montserrat-Bold.ttf"

style nsfw_italic_text is text:
    font "fonts/Montserrat-MediumItalic.ttf"


screen timerBar(seconds=3):
    bar value AnimatedValue(0, seconds, seconds, seconds) at alpha_dissolve


screen animated_value_bar(old_value, new_value, max_value, left_frame=None, right_frame=None, offset=(0, 0), size=(0, 0), delay=2):
    tag animated_value_bar

    bar:
        value AnimatedValue(new_value, max_value, delay, old_value)
        left_bar left_frame
        right_bar right_frame
        align (0.5, 0.5)
        offset offset
        xysize size


# Kiwii Screens
screen kiwiiPopup():
    modal True
    zorder 200

    use alert_template("You've just unlocked the social media app Kiwii! Open it now from the homescreen."):

        textbutton "OK":
            xalign 0.5
            action [Function(kiwii_firstTimeMessages), SetVariable("kiwii_firstTime", False), Hide("kiwiiPopup")]


# Fight Screens
screen fightPopup(fightMove):
    modal True
    
    use alert_template("Congratulations! You have learned a new fighting move: {{b}}{}{{/b}}.".format(fightMove)):

        textbutton "OK":
            action Return()


screen fightDamage():
    if youDamage == 3:
        add "images/3 hits.webp"
    elif youDamage == 4:
        add "images/4 hits.webp"
    elif youDamage >= 5:
        add "images/5 hits.webp"
