init python:
    class Phone:
        def __init__(self, image):
            self._image = "images/phone/{}".format(image)

            self.applications = []

        @property
        def image(self):
            file_name, extention = os.path.splitext(self._image)

            if any(app.notification for app in self.applications):
                return file_name + "_notification" + extention
            else:
                return self._image


default phone = Phone("phone_icon.webp")


screen phone_icon():
    zorder 100
    
    if not renpy.get_screen("choice") and not renpy.get_screen("censoredPopup"):
        imagebutton:
            idle phone.image
            
            if renpy.get_screen("free_roam"):
                action Show("phone")
            else:
                action Call("call_screen_phone")

            align (0.999, 0.05)

label call_screen_phone:
    call screen phone
    return


screen base_phone():
    modal True

    add "images/phone/phone_screen.webp"

    if renpy.get_screen("phone"):
        # Click background to close phone
        button:
            if renpy.get_screen("free_roam"):
                action [Hide("tutorial"), Hide("phone"), Hide("messenger_reply")]
            else:
                action [Hide("tutorial"), Hide("messenger_reply"), Return()]

        textbutton "Exit Phone":
            style "phonebutton"
            if renpy.get_screen("free_roam"):
                action [Hide("tutorial"), Hide("phone"), Hide("messenger_reply")]
            else:
                action [Hide("tutorial"), Hide("messenger_reply"), Return()]

    # Button to prevent phone closing on phone ui
    button:
        align (0.5, 0.5)
        xysize (400, 800)
        action NullAction()

    transclude

    if not renpy.get_screen("phone"):
        button:
            xysize(407, 61)
            xalign 0.5
            ypos 906
            style "phonehome"
            action [Hide("messenger_reply"), Show("phone")]

            text "Home":
                align (0.5, 0.5)


screen phone():
    tag phone_tag
    modal True

    use base_phone:
        vpgrid:
            cols 3
            pos (787, 180)
            spacing 20

            for app in phone.applications:
                if not app.locked:
                    vbox:
                        imagebutton:
                            idle Transform(app.image, size=(100, 100))
                            action [Function(renpy.retain_after_load), Show(app.home_screen)]
                                
                        text app.name style "applabels"
        