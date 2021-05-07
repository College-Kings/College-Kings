screen phoneTutorial():
    zorder 100

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

    default kctTutorials = [
        "Your decisions strongly influence the way the story progresses and how other characters perceive you.",
        "With each choice you’ll either gain Bro, Boyfriend or Troublemaker points.",
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
    zorder 100

    default freeRoamTutorials = [
        "At certain parts of the game, you’ll unlock free roam.",
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