init python:
    class Phone:
        def __init__(self, image):
            self.base_image = "images/phone/{}".format(image)

            self.applications = []

        @property
        def notification(self):
            return any(app.notification for app in self.applications)

        @property
        def image(self):
            if not self.notification:
                return self.base_image

            file_name, extention = os.path.splitext(self.base_image) 
            return file_name + "-notification" + extention


    phone = Phone("phone-icon.webp")


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
                action [Hide("tutorial"), Hide("phone"), Hide("message_reply")]
            else:
                action [Hide("tutorial"), Hide("message_reply"), Return()]

        textbutton "Exit Phone":
            style "phonebutton"
            if renpy.get_screen("free_roam"):
                action [Hide("tutorial"), Hide("phone"), Hide("message_reply")]
            else:
                action [Hide("tutorial"), Hide("message_reply"), Return()]

    frame:
        background "images/phone/phone_screen.webp"
        align (0.5, 0.5)
        xysize (433, 918)
        modal True

        transclude

        if not renpy.get_screen("phone"):
            fixed:
                ysize 69
                ypos 843

                imagebutton:
                    if renpy.get_screen("kiwiiPost") or renpy.get_screen("kiwiiApp") or renpy.get_screen("kiwiiPreferences"):
                        idle "images/phone/home_button_kiwii_idle.webp"
                        hover "images/phone/home_button_kiwii_hover.webp"
                    else:
                        idle "images/phone/home_button_idle.webp"
                        hover "images/phone/home_button_hover.webp"
                    action [Hide("message_reply"), Show("phone")]
                    align (0.5, 0.5)
                

screen base_phone_rotated():
    modal True

    add "darker_80"

    if renpy.get_screen("phone"):
        # Click background to close phone
        button:
            if renpy.get_screen("free_roam"):
                action [Hide("tutorial"), Hide("phone"), Hide("message_reply")]
            else:
                action [Hide("tutorial"), Hide("message_reply"), Return()]

        textbutton "Exit Phone":
            style "phonebutton"
            if renpy.get_screen("free_roam"):
                action [Hide("tutorial"), Hide("phone"), Hide("message_reply")]
            else:
                action [Hide("tutorial"), Hide("message_reply"), Return()]

    frame:
        align (0.5, 0.5)
        xysize (918, 433)
        modal True

        transclude

        fixed:
            xsize 69
            xpos 844

            imagebutton:
                if renpy.get_screen("kiwiiPost") or renpy.get_screen("kiwiiApp") or renpy.get_screen("kiwiiPreferences"):
                    idle "images/phone/home_button_kiwii_idle.webp"
                    hover "images/phone/home_button_kiwii_hover.webp"
                else:
                    idle "images/phone/home_button_idle.webp"
                    hover "images/phone/home_button_hover.webp"
                action [Hide("message_reply"), Show("phone")]
                align (0.5, 0.5)

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
                vbox:
                    spacing 2
                    
                    imagebutton:
                        idle app.image
                        action [Function(renpy.retain_after_load), Show(app.home_screen)]
                            
                    text app.name style "application_name" xalign 0.5

    if config_debug:
        for app in phone.applications:
            if app.notification:
                timer 0.1 action [Function(renpy.retain_after_load), Show(app.home_screen)]

        if not any(app.notification for app in phone.applications):
            timer 0.1:
                if renpy.get_screen("free_roam"):
                    action [Hide("tutorial"), Hide("phone"), Hide("message_reply")]
                else:
                    action [Hide("tutorial"), Hide("message_reply"), Return()]
