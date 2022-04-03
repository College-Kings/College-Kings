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
                padding (15, 15)
                size_group "reply_buttons"

                if isinstance(reply, Reply):
                    text reply.message style "reply_text" align (0.5, 0.5)

                elif isinstance(reply, ImgReply):
                    add Transform(reply.image, zoom=0.15)

    if config_debug:
        if contact.replies:
            timer 0.1 action [Hide("message_reply"), Function(contact.selected_reply, renpy.random.choice(contact.replies))]
        else:
            timer 0.1 action Hide("message_reply")


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