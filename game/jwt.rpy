# Forced Walkthrough mod by Jany



#shenanigans to make the greyed out choices work

init -1 python: 
    if getattr(renpy.display.get_info(), 'oldmenu', None) is None:
        renpy.display.get_info().oldmenu = renpy.exports.menu

    def menu_override(items, set_expr, args, kwargs, item_arguments):
        items = [ (renpy.exports.substitute(label) + (" (disabled)" if not renpy.python.py_eval(condition) else ""), "True", value)
                  for label, condition, value in items ]
        
        return renpy.display.get_info().oldmenu(items, set_expr)
    renpy.exports.menu = menu_override

screen choice(items, time=3):
    image "gui/curves.png"

    style_prefix "choice"



    timer 0.001 action SetVariable("ischoice", True)

    hbox xpos 209 ypos 907 spacing -3:

        for i in items:
            if i == items[0]:
                if " (disabled)" in i.caption:
                    textbutton i.caption.replace(" (disabled)", "") action NullAction():
                        hover_background "gui/leftwhite.png"
                        idle_background "gui/leftwhite.png"
                        xpadding 50
                        ypadding 21
                        xsize 800
                        text_size 40
                else:
                    textbutton i.caption action [ i.action, SetVariable("ischoice", False) ]:
                        hover_background "gui/leftwhite.png"
                        idle_background "gui/leftblue.png"
                        xpadding 50
                        ypadding 21
                        xsize 800
                        text_size 40
            else:
                if " (disabled)" in i.caption:
                    textbutton i.caption.replace(" (disabled)", "") action NullAction():
                        hover_background "gui/rightwhite.png"
                        idle_background "gui/rightblue.png"
                        xpadding 90
                        ypadding 21
                        xsize 800
                        text_size 40
                else:
                    textbutton i.caption action [ i.action, SetVariable("ischoice", False) ]:
                        hover_background "gui/rightwhite.png"
                        idle_background "gui/rightblue.png"
                        xpadding 90
                        ypadding 21
                        xsize 800
                        text_size 40

    if realkcttut == 1:

        image "images/tutback.png":
            ypos 100 #+300
            xpos 1240 #+260

        imagebutton:
            idle "images/whitearrowleft.png"
            hover "images/whitearrowleft.png"
            ypos 720
            xpos 1260
            if kctpage > 1:
                action SetVariable("kctpage", kctpage -1)
            else:
                action SetVariable("kctpage", 5)

        imagebutton:
            idle "images/whitearrowright.png"
            hover "images/whitearrowright.png"
            ypos 720
            xpos 1740
            if kctpage < 5:
                action SetVariable("kctpage", kctpage +1)
            else:
                action SetVariable("kctpage", 1)

        text "Tutorial" style "choicetextnum" ypos 530 xpos 1490

        if kctpage == 1:
            text "Your decisions strongly influence the way the story progresses and how other characters perceive you." style "choicetuttext"
            text "1 of 5" style "choicetextnum"
        if kctpage == 2:
            text "With each choice you’ll either gain Bro, Boyfriend or Troublemaker points." style "choicetuttext"
            text "2 of 5" style "choicetextnum"
        if kctpage == 3:
            text "Bros put the squad first, boyfriends show strong affinity towards a few selected individuals and troublemakers seek thrills and take risks." style "choicetuttext"
            text "3 of 5" style "choicetextnum"
        if kctpage == 4:
            text "These points are then used to identify your Key Character Trait (KCT).  Each KCT will unlock different possibilities and choices, but you can only have one active at a time." style "choicetuttext"
            text "4 of 5" style "choicetextnum"
        if kctpage == 5:
            text "You can read more about each individual KCT in the Stats app on your phone." style "choicetuttext"
            text "5 of 5" style "choicetextnum"

    if influencetut == True:

        image "images/tutback.png":
            ypos 100 #+300
            xpos 1240 #+260

        imagebutton:
            idle "images/whitearrowleft.png"
            hover "images/whitearrowleft.png"
            ypos 720
            xpos 1260
            if itpage > 1:
                action SetVariable("itpage", itpage -1)
            else:
                action SetVariable("itpage", 4)

        imagebutton:
            idle "images/whitearrowright.png"
            hover "images/whitearrowright.png"
            ypos 720
            xpos 1740
            if itpage < 4:
                action SetVariable("itpage", itpage +1)
            else:
                action SetVariable("itpage", 1)

        text "Tutorial" style "choicetextnum" ypos 530 xpos 1490

        if itpage == 1:
            text "When people make important decisions on how they feel about you, they consider what kind of a person you are." style "choicetuttext"
            text "1 of 4" style "choicetextnum"
        if itpage == 2:
            text "Your Key Character Trait (Loyal, Popular or Confident) has a strong influence on how other characters react to your behavior." style "choicetuttext"
            text "2 of 4" style "choicetextnum"
        if itpage == 3:
            text "Some people value a popular leader, some care more about loyalty than status and some are drawn to confidence." style "choicetuttext"
            text "3 of 4" style "choicetextnum"
        if itpage == 4:
            text "Your decisions matter and have long time effects, as you can only have one KCT at a time. So think about what kind of person you want to be." style "choicetuttext"
            text "4 of 4" style "choicetextnum"

    if showkct == True:
        image "gui/kct.png"
        text "[kct]":
            ypos 18
            #xalign 0.975
            xpos 1700
            text_align 0.5
            font "fonts/Freshman.ttf"
            size 40
            if kct == "popular":
                color "#53d769"
            if kct == "loyal":
                color "#fecb2e"
            if kct == "confident":
                color "#fc3d39"

    if timed == True:

        timer time repeat False action [ Hide('countdown'), Jump("choicetimer") ]
        bar value AnimatedValue(0, time, time, time) at alpha_dissolve # assuming you're using the alpha_dissolve transform from the wiki



#variables

default jwt = False #Walkthrough enabled?
define config.menu_include_disabled = True #makes choices unavailable



#screens
screen jwt(): # the screen to select if the walkthrough is enabled
    image "images/jwt.jpg"

    imagebutton:
        ypos 683
        xpos 417
        idle "images/rlmt.png"
        hover "images/enable.jpg"
        action Jump ("jwt")

    imagebutton:
        ypos 683
        xpos 1016
        idle "images/rlmt.png"
        hover "images/disable.jpg"
        action Jump ("jwtd")



#labels
label jwt: #If the walkthrough is enabled
    $ jwt = True
    $ realmode = False
    $ config.rollback_enabled = True
    $ showkct = True
    
    "Jany" "Welcome to the walkthrough."
    "Jany" "With this walkthrough you will see all the dates and lewd scenes."
    "Jany" "You can just play the game as you would play it normally, but some choices are disabled, so that you won't miss anything."
    "Jany" "Have fun!"
    jump starta
