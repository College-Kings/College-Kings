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

    phone = Phone("phone_icon.webp")



screen phone_icon():
    zorder 100
    
    if not renpy.get_screen("choice") and not renpy.get_screen("censored_popup"):
        imagebutton:
            idle phone.image
            
            if renpy.get_screen("free_roam"):
                action Show("phone")
            else:
                action Call("call_screen_phone")

            xalign 1.0
            offset (25, -25)

label call_screen_phone:
    call screen phone
    return


screen base_phone():
    modal True

    add "darker_80"

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

    window:
        background "images/phone/phone_screen.webp"
        align (0.5, 0.5)
        xysize (433, 918)
        modal True

        transclude

        if not renpy.get_screen("phone"):
            imagebutton:
                if renpy.get_screen("kiwiiPost") or renpy.get_screen("kiwiiApp") or renpy.get_screen("kiwiiPreferences"):
                    idle Transform("images/phone/home_button_kiwii_idle.webp", size=(40,40))
                    hover Transform("images/phone/home_button_kiwii_hover.webp", size=(40,40))
                else:
                    idle Transform("images/phone/home_button_idle.webp", size=(55,55))
                    hover Transform("images/phone/home_button_hover.webp", size=(55,55))
                action [Hide("messenger_reply"), Show("phone")]
                align (0.5, 1.0)
                yoffset -10
                

screen base_phone_rotated():
    modal True

    add "darker_80"

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

    window:
        background "images/phone/phone_screen.webp"
        align (0.5, 0.5)
        xysize (433, 918)
        modal True
        at center_rotation(-90)

        transclude

        if not renpy.get_screen("phone"):
            imagebutton:
                if renpy.get_screen("kiwiiPost") or renpy.get_screen("kiwiiApp") or renpy.get_screen("kiwiiPreferences"):
                    idle Transform("images/phone/home_button_kiwii_idle.webp", size=(40,40))
                    hover Transform("images/phone/home_button_kiwii_hover.webp", size=(40,40))
                else:
                    idle Transform("images/phone/home_button_idle.webp", size=(55,55))
                    hover Transform("images/phone/home_button_hover.webp", size=(55,55))
                action [Hide("messenger_reply"), Show("phone")]
                align (0.5, 1.0)
                yoffset -10

screen phone():
    tag phone_tag
    modal True

    use base_phone:
        vpgrid:
            cols 3
            spacing 35
            xalign 0.5
            ypos 100
            

            for app in phone.applications:
                if not app.locked:
                    vbox:
                        imagebutton:
                            idle Transform(app.image, size=(100, 100))
                            action [Function(renpy.retain_after_load), Show(app.home_screen)]
                                
                        text app.name style "applabels"
        

transform center_rotation(amount):
    around (0.5, 0.5)
    alignaround (0.5, 0.5)
    align (0.5, 0.5)
    rotate amount