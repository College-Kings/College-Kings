screen messenger_contacts(contact=None):
    tag phone_tag
    modal True

    default image_path = "images/phone/messenger/app-assets/"

    use base_phone:
        frame:
            background image_path + "conversation-background.webp"
            xysize (433, 918)

            hbox:
                pos (41, 62)
                ysize 93
                spacing 15

                imagebutton:
                    idle "back_button"
                    action [Hide("message_reply"), Show("messenger_home")]
                    yalign 0.5

                if contact is not None:
                    add Transform(contact.profile_picture, xysize=(65, 65)) yalign 0.5

                    text contact.name style "nametext" yalign 0.5

            viewport:
                yadjustment inf_adj
                mousewheel True
                pos (11, 157)
                xysize (416, 686)

                vbox:
                    spacing -25

                    null height 25

                    if contact is not None:
                        for message in contact.sent_messages:
                            frame:
                                padding (50, 50)

                                if isinstance(message, Message) and message.message.strip():
                                    background "message_background"

                                    text message.message  style "message_text"

                                elif isinstance(message, ImageMessage):
                                    background "message_background"

                                    imagebutton:
                                        idle Transform(message.image, zoom=0.15)
                                        action Show("phone_image", img=message.image)

                                elif isinstance(message, Reply):
                                    background "reply_background"
                                    xalign 1.0

                                    text message.message  style "reply_text"

                                elif isinstance(message, ImgReply):
                                    background "reply_background"
                                    xalign 1.0

                                    imagebutton:
                                        idle Transform(message.image, zoom=0.15)
                                        action Show("phone_image", img=message.image)
                    else:
                        text "Exception: Contact is None. Please make a support ticket at https://discord.gg/H98n8ubrGA if this error persists."

                    null height 75

            if contact is not None and contact.replies:
                fixed:
                    xysize (416, 63)
                    ypos 780

                    imagebutton:
                        idle "reply_button_idle"
                        hover image_path + "reply-button-hover.webp"
                        selected_idle image_path + "reply-button-hover.webp"
                        action Show("message_reply", contact=contact)
                        align (0.5, 0.5)

    if kiwii_firstTime:
        timer 0.01 action Show("kiwiiPopup")

    if config_debug:
        if contact.replies:
            timer 0.1 repeat True action Show("message_reply", contact=contact)
        else:
            timer 0.1 repeat True action [Hide("message_reply"), Show("phone")]