screen message_reply(contact=None):
    vbox:
        xsize 600
        xpos 1200
        yalign 1.0
        yoffset -100
        spacing -75

        for reply in contact.replies:
            button:
                idle_background "reply_background_idle"
                hover_background "reply_background_hover"
                padding (100, 65)
                focus_mask reply_focus_mask
                action [Hide("message_reply"), Function(contact.selected_reply, reply)]

                if isinstance(reply, Reply):
                    text reply.message style "reply_text"

                elif isinstance(reply, ImgReply):
                    add Transform(reply.image, zoom=0.15)


screen phone_image(img=None):
    modal True

    $ bigImage = os.path.splitext(img)[0] + "big" + os.path.splitext(img)[1]

    add "darker_80"
    if renpy.loadable(bigImage):
        add bigImage at truecenter
    else:
        add img at truecenter

    button:
        action Hide("phone_image")