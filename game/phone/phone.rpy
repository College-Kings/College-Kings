init python:

    class Application:
        def __init__(self, name, image, screen, notification=False, locked=False):
            self.name = name
            self.image = image
            self.screen = screen
            self.notification = notification
            self.locked = locked
            if notification:
                self.newNotification()

            applications.append(self)

        def newNotification(self):
            self.notification = True
            if not os.path.splitext(self.image)[0][-3:] == "not":
                self.image = os.path.splitext(self.image)[0] + "not" + os.path.splitext(self.image)[1]

            # if achievementsnot == 1: - Achievements Screen Notification Var
            # if statsnot == 1: - Stats Screen Notification Var

        def seenNotification(self):
            self.notification = False
            if os.path.splitext(self.image)[0][-3:] == "not":
                self.image = os.path.splitext(self.image)[0][:-3] + os.path.splitext(self.image)[1]

        def unlock(self):
            self.locked = False

init offset = -1
default applications = []

screen phoneTemplate():

    add "images/phonescreen.png"

    if not noexit:
        textbutton "Exit Phone" action [Hide("reply"), Jump("exitphone")] style "phonebutton"

    if phonetut and not renpy.get_screen("tutorial"):
        use tutorial

    transclude

    if not renpy.get_screen("phone") and not renpy.get_screen("reply"):
        button:
            xysize(407, 61)
            xalign 0.5
            ypos 906
            style "phonehome"
            action Jump ("homescreen")


screen phone():
    tag phoneTag

    use phoneTemplate:

        vpgrid:
            cols 3
            ypos 180
            xpos 787
            spacing 20

            for app in applications:
                if not app.locked:
                    vbox:
                        imagebutton:
                            idle Transform(app.image, size=(100, 100))
                            if app.name == "Kiwii" and kiwii_firstTime:
                                action Jump("kiwii_firstTime")
                            elif app.name == "Messages" or app.name == "Kiwii":
                                action [Function(renpy.retain_after_load), Show(app.screen)]
                            else:
                                action Jump(app.screen)
                        text app.name style "applabels"


screen tutorial():

        default phoneTuts = [
            "This is the phone screen. You can access your phone whenever the phone icon in the top right corner appears.",
            "Blue dots show notifications. New notifications are usually accommpanied by a buzz sound. Currently you have a new message waiting for you.",
            "How you reply to messages matters just as much as any other decision.",
            "Over the course of the game you will also unlock all kinds of new apps, such as statistics or social media platforms.",
            "Lastly, if you ever need to get to the homescreen, just click the bottom border of the phone, or the phone icon.",
        ]

        add "images/tutback.png":
            yalign 0.5
            xpos 1200

        fixed:
            xysize(650, 85)
            pos(1200, 550)

            hbox:
                align(0.5, 0.5)
                spacing 150

                imagebutton:
                    idle "images/whitearrowleft.png"
                    if phonetutpage > 1:
                        action SetVariable("phonetutpage", phonetutpage -1)
                    else:
                        action SetVariable("phonetutpage", 5)

                text "{} of {}".format(phonetutpage, len(phoneTuts)) style "tutorialtextnum" yalign(0.5)

                imagebutton:
                    idle "images/whitearrowright.png"
                    if phonetutpage < 5:
                        action SetVariable("phonetutpage", phonetutpage +1)
                    else:
                        action SetVariable("phonetutpage", 1)

        text phoneTuts[phonetutpage -1] style "tutorialtext"
