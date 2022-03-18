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

    config.overlay_screens.append("phone_icon")

default phone = Phone("phone_icon.webp")


screen phone_icon():
    zorder 100
    
    if not renpy.get_screen("choice") and not renpy.get_screen("censored_popup"):
        imagebutton:
            idle Transform(phone.image, zoom=0.55)
            
            if renpy.get_screen("free_roam"):
                action Show("phone")
            else:
                action Call("call_screen_phone")

            align (0.999, 0.05)
            yoffset -118
            xoffset 73

label call_screen_phone:
    call screen phone
    return


screen base_phone():
    modal True

    add "darker_80"
    add Transform("images/phone/phone_screen.webp", zoom=0.25)

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

        if renpy.get_screen("kiwiiPost") or renpy.get_screen("kiwiiApp") or renpy.get_screen("kiwiiPreferences"):
            imagebutton:
                idle Transform("images/phone/home_button_kiwii_idle.webp", size=(40,40))
                hover Transform("images/phone/home_button_kiwii_hover.webp", size=(40,40))
                action [Hide("messenger_reply"), Show("phone")]
                xalign 0.5
                yalign 0.88
        else:
            imagebutton:
                idle Transform("images/phone/home_button_idle.webp", size=(55,55))
                hover Transform("images/phone/home_button_hover.webp", size=(55,55))
                action [Hide("messenger_reply"), Show("phone")]
                xalign 0.5
                yalign 0.88

screen base_phone_rotated():
    modal True

    add "darker_80"
    add Transform("images/phone/phone_screen.webp", zoom=0.40) at rotation

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
        imagebutton:
            idle Transform("images/phone/home_button_idle.webp", size=(80,80))
            hover Transform("images/phone/home_button_hover.webp", size=(80,80))
            action [Hide("messenger_reply"), Show("phone")]
            xalign 0.16
            yalign 0.5  

transform rotation:
    around (.5, .5) alignaround (.5, .5) xalign .5 yalign .5
    linear 0.0 rotate 90 



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
        