screen message_reply(contact=None):
    vbox:
        xsize 500
        xpos 1200
        yalign 1.0
        yoffset -100
        spacing 10

        for reply in contact.replies:
            button:
                background "reply_background_idle"
                action [Hide("message_reply"), Function(contact.selected_reply, reply)]
                ysize 100
                padding (15, 15)
                size_group "reply_buttons"

                if isinstance(reply, Reply):
                    text reply.message style "reply_text" yalign 0.5

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