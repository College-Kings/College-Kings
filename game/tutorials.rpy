screen phoneTutorial():
    zorder 200
    tag tutorial

    default phoneTutorials = [
        "This is the phone screen. You can access your phone whenever the phone icon in the top right corner appears.",
        "Blue dots show notifications. New notifications are usually accommpanied by a buzz sound. Currently you have a new message waiting for you.",
        "How you reply to messages matters just as much as any other decision.",
        "Over the course of the game you will also unlock all kinds of new apps, such as statistics or social media platforms.",
        "Lastly, if you ever need to get to the homescreen, just click the bottom border of the phone, or the phone icon.",
    ]

    add "images/tutback.webp":
        yalign 0.5
        xpos 1200

    text "Tutorial" style "choicetextnum" pos (1450, 360)

    fixed:
        xysize(650, 85)
        pos(1200, 550)

        hbox:
            align(0.5, 0.5)
            spacing 150

            imagebutton:
                idle "images/whitearrowleft.webp"
                if phoneTutorialPage > 1:
                    action SetVariable("phoneTutorialPage", phoneTutorialPage -1)
                else:
                    action SetVariable("phoneTutorialPage", len(phoneTutorials))

            text "{} of {}".format(phoneTutorialPage, len(phoneTutorials)) style "tutorialtextnum" yalign(0.5)

            imagebutton:
                idle "images/whitearrowright.webp"
                if phoneTutorialPage < len(phoneTutorials):
                    action SetVariable("phoneTutorialPage", phoneTutorialPage +1)
                else:
                    action SetVariable("phoneTutorialPage", 1)

    text phoneTutorials[phoneTutorialPage -1] style "tutorialtext"


screen kctTutorial():
    zorder 200
    tag tutorial

    default kctTutorials = [
        "Your decisions strongly influence the way the story progresses and how other characters perceive you.",
        "With each choice you'll either gain Bro, Boyfriend or Troublemaker points.",
        "Bros put the squad first, boyfriends show strong affinity towards a few selected individuals and troublemakers seek thrills and take risks.",
        "These points are then used to identify your Key Character Trait (KCT).  Each KCT will unlock different possibilities and choices, but you can only have one active at a time.",
        "You can read more about each individual KCT in the Stats app on your phone.",
    ]

    add "images/tutback.webp":
        pos (1240, 100)

    text "Tutorial" style "choicetextnum" pos (1490, 530)

    text kctTutorials[kctTutorialPage -1] style "choicetuttext"

    fixed:
        xysize(650, 85)
        pos(1240, 720)

        hbox:
            align(0.5, 0.5)
            spacing 150

            imagebutton:
                idle "images/whitearrowleft.webp"
                if kctTutorialPage > 1:
                    action SetVariable("kctTutorialPage", kctTutorialPage -1)
                else:
                    action SetVariable("kctTutorialPage", len(kctTutorials))

            text "{} of {}".format(kctTutorialPage, len(kctTutorials)) style "choicetextnum" yalign 0.5

            imagebutton:
                idle "images/whitearrowright.webp"
                if kctTutorialPage < len(kctTutorials):
                    action SetVariable("kctTutorialPage", kctTutorialPage +1)
                else:
                    action SetVariable("kctTutorialPage", 1)


screen freeRoamTutorial():
    zorder 200
    tag tutorial

    default freeRoamTutorials = [
        "At certain parts of the game, you'll unlock free roam.",
        "During free roam, you choose where you go and who you want to talk to next.",
        "You will also be able to use your phone and you might just find some hidden content."
    ]

    add "images/tutback.webp":
        pos (1240, 100)

    text "Tutorial" style "choicetextnum" pos (1490, 530)

    text freeRoamTutorials[freeRoamTutorialPage -1] style "choicetuttext"

    fixed:
        xysize(650, 85)
        pos(1240, 720)

        hbox:
            align(0.5, 0.5)
            spacing 150

            imagebutton:
                idle "images/whitearrowleft.webp"
                if freeRoamTutorialPage > 1:
                    action SetVariable("freeRoamTutorialPage", freeRoamTutorialPage - 1)
                else:
                    action SetVariable("freeRoamTutorialPage", len(freeRoamTutorials))

            text "{} of {}".format(freeRoamTutorialPage, len(freeRoamTutorials)) style "choicetextnum" yalign 0.5

            imagebutton:
                idle "images/whitearrowright.webp"
                if freeRoamTutorialPage < len(freeRoamTutorials):
                    action SetVariable("freeRoamTutorialPage", freeRoamTutorialPage + 1)
                else:
                    action SetVariable("freeRoamTutorialPage", 1)

screen influenceTutorial():
    zorder 200
    tag tutorial

    default influenceTutorials = [
        "When people make important decisions on how they feel about you, they consider what kind of a person you are.",
        "Your Key Character Trait (Loyal, Popular or Confident) has a strong influence on how other characters react to your behavior.",
        "Some people value a popular leader, some care more about loyalty than status and some are drawn to confidence.",
        "Your decisions matter and have long time effects, as you can only have one KCT at a time. So think about what kind of person you want to be."
    ]

    add "images/tutback.webp":
        pos (1240, 100)

    text "Tutorial" style "choicetextnum" pos (1490, 530)

    text influenceTutorials[influenceTutorialPage -1] style "choicetuttext"

    fixed:
        xysize(650, 85)
        pos(1240, 720)

        hbox:
            align(0.5, 0.5)
            spacing 150

            imagebutton:
                idle "images/whitearrowleft.webp"
                if influenceTutorialPage > 1:
                    action SetVariable("influenceTutorialPage", influenceTutorialPage - 1)
                else:
                    action SetVariable("influenceTutorialPage", len(influenceTutorials))

            text "{} of {}".format(influenceTutorialPage, len(influenceTutorials)) style "choicetextnum" yalign 0.5

            imagebutton:
                idle "images/whitearrowright.webp"
                if influenceTutorialPage < len(influenceTutorials):
                    action SetVariable("influenceTutorialPage", influenceTutorialPage + 1)
                else:
                    action SetVariable("influenceTutorialPage", 1)

style choicetuttext is text:
    font "fonts/OpenSans.ttf"
    size 25
    color "#ffffff"
    text_align 0
    xpos 1310
    ypos 570
    xmaximum 500

style choicetextnum is text:
    font "fonts/Freshman.ttf"
    size 25
    color "#FFD166"
    text_align 0.5

style tutorialtext is text:
    font "fonts/OpenSans.ttf"
    size 25
    color "#ffffff"
    text_align 0
    xpos 1270
    ypos 400
    xmaximum 500

style tutorialtextnum is text:
    font "fonts/Freshman.ttf"
    size 25
    color "#FFD166"