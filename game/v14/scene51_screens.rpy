screen v14s51_room():
    tag free_roam

    imagemap:
        idle "images/v14/Scene 51/v14s51_2.webp"
        hover "images/v14/Scene 51/v14s51_2_screen_hover.webp"

        if v14s50_listen_to_aubrey_lindsey_3:
            if v14s51_interaction < 2: #toggle 2 to 1 to enhance extra difficulty if MC stayed to listen for a third time.
                if not v14s51_bedside:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_bedside.png"
                        hover "images/v14/Scene 51/v14s51_bedside_hover.png"
                        action Jump("v14s51_bedside_table")
                        pos (970, 330)
                if not v14s51_desk:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_desk.png"
                        hover "images/v14/Scene 51/v14s51_desk_hover.png"
                        action Jump("v14s51_desk_drawer")
                        pos (1710, 500)
                if not v14s51_closet:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_closet.png"
                        hover "images/v14/Scene 51/v14s51_closet_hover.png"
                        action Jump("v14s51_closet")
                        pos (230, 5)
                if not v14s51_purse:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_purse.png"
                        hover "images/v14/Scene 51/v14s51_purse_hover.png"
                        action Jump("v14s51_purse")
                        pos (0, 170)
                if not v14s51_pillow:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_pillow.png"
                        hover "images/v14/Scene 51/v14s51_pillow_hover.png"
                        action Jump("v14s51_pillow")
                        pos (1130, 380)
            else:
                timer 0.75 action Jump("v14s51_continue")

        elif v14s50_listen_to_aubrey_lindsey_2:
            if v14s51_interaction < 2:
                if not v14s51_bedside:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_bedside.png"
                        hover "images/v14/Scene 51/v14s51_bedside_hover.png"
                        action Jump("v14s51_bedside_table")
                        pos (970, 330)
                if not v14s51_desk:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_desk.png"
                        hover "images/v14/Scene 51/v14s51_desk_hover.png"
                        action Jump("v14s51_desk_drawer")
                        pos (1710, 500)
                if not v14s51_closet:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_closet.png"
                        hover "images/v14/Scene 51/v14s51_closet_hover.png"
                        action Jump("v14s51_closet")
                        pos (230, 5)
                if not v14s51_purse:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_purse.png"
                        hover "images/v14/Scene 51/v14s51_purse_hover.png"
                        action Jump("v14s51_purse")
                        pos (0, 170)
                if not v14s51_pillow:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_pillow.png"
                        hover "images/v14/Scene 51/v14s51_pillow_hover.png"
                        action Jump("v14s51_pillow")
                        pos (1130, 380)
            else:
                timer 0.75 action Jump("v14s51_continue")

        elif v14s50_listen_to_aubrey_lindsey:
            if v14s51_interaction < 3:
                if not v14s51_bedside:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_bedside.png"
                        hover "images/v14/Scene 51/v14s51_bedside_hover.png"
                        action Jump("v14s51_bedside_table")
                        pos (970, 330)
                if not v14s51_desk:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_desk.png"
                        hover "images/v14/Scene 51/v14s51_desk_hover.png"
                        action Jump("v14s51_desk_drawer")
                        pos (1710, 500)
                if not v14s51_closet:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_closet.png"
                        hover "images/v14/Scene 51/v14s51_closet_hover.png"
                        action Jump("v14s51_closet")
                        pos (230, 5)
                if not v14s51_purse:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_purse.png"
                        hover "images/v14/Scene 51/v14s51_purse_hover.png"
                        action Jump("v14s51_purse")
                        pos (0, 170)
                if not v14s51_pillow:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_pillow.png"
                        hover "images/v14/Scene 51/v14s51_pillow_hover.png"
                        action Jump("v14s51_pillow")
                        pos (1130, 380)
            else:
                timer 0.75 action Jump("v14s51_continue")

        else:
            if v14s51_interaction < 4:
                if not v14s51_bedside:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_bedside.png"
                        hover "images/v14/Scene 51/v14s51_bedside_hover.png"
                        action Jump("v14s51_bedside_table")
                        pos (970, 330)
                if not v14s51_desk:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_desk.png"
                        hover "images/v14/Scene 51/v14s51_desk_hover.png"
                        action Jump("v14s51_desk_drawer")
                        pos (1710, 500)
                if not v14s51_closet:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_closet.png"
                        hover "images/v14/Scene 51/v14s51_closet_hover.png"
                        action Jump("v14s51_closet")
                        pos (230, 5)
                if not v14s51_purse:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_purse.png"
                        hover "images/v14/Scene 51/v14s51_purse_hover.png"
                        action Jump("v14s51_purse")
                        pos (0, 170)
                if not v14s51_pillow:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_pillow.png"
                        hover "images/v14/Scene 51/v14s51_pillow_hover.png"
                        action Jump("v14s51_pillow")
                        pos (1130, 380)
            else:
                timer 0.75 action Jump("v14s51_continue")
                


        #-if MC chose to keep listening to Lindsey and Aubrey's conversation more than one time, MC can only choose 2 areas.
        #-if MC chose to keep listening to Lindsey and Aubrey's conversation once, MC can only choose 3 areas.
        #-if MC chose to go to Chloe's room and did not choose to keep listening, MC can choose 4 areas.