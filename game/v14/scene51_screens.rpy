screen v14s51_room():
    tag free_roam

    imagemap:
        idle "images/v14/Scene 51/v14s51_2.webp"
        hover "images/v14/Scene 51/v14s51_2_screen_hover.webp"

        if v14s50_listen_to_aubrey_lindsey == 3:
            if len(freeroam12) < 2: #toggle 2 to 1 to enhance extra difficulty if MC stayed to listen for a third time.
                if not "bedside" in freeroam12:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_bedside.webp"
                        hover "images/v14/Scene 51/v14s51_bedside_hover.webp"
                        action Jump("v14s51_bedside_table")
                        pos (970, 330)
                if not "desk" in freeroam12:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_desk.webp"
                        hover "images/v14/Scene 51/v14s51_desk_hover.webp"
                        action Jump("v14s51_desk_drawer")
                        pos (1710, 500)
                if not "closet" in freeroam12:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_closet.webp"
                        hover "images/v14/Scene 51/v14s51_closet_hover.webp"
                        action Jump("v14s51_closet")
                        pos (230, 5)
                if not "purse" in freeroam12:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_purse.webp"
                        hover "images/v14/Scene 51/v14s51_purse_hover.webp"
                        action Jump("v14s51_purse")
                        pos (0, 170)
                if not "pillow" in freeroam12:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_pillow.webp"
                        hover "images/v14/Scene 51/v14s51_pillow_hover.webp"
                        action Jump("v14s51_pillow")
                        pos (1130, 380)
            else:
                timer 0.75 action Jump("v14s51_continue")

        elif v14s50_listen_to_aubrey_lindsey == 2:
            if len(freeroam12) < 3:
                if not "bedside" in freeroam12:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_bedside.webp"
                        hover "images/v14/Scene 51/v14s51_bedside_hover.webp"
                        action Jump("v14s51_bedside_table")
                        pos (970, 330)
                if not "desk" in freeroam12:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_desk.webp"
                        hover "images/v14/Scene 51/v14s51_desk_hover.webp"
                        action Jump("v14s51_desk_drawer")
                        pos (1710, 500)
                if not "closet" in freeroam12:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_closet.webp"
                        hover "images/v14/Scene 51/v14s51_closet_hover.webp"
                        action Jump("v14s51_closet")
                        pos (230, 5)
                if not "purse" in freeroam12:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_purse.webp"
                        hover "images/v14/Scene 51/v14s51_purse_hover.webp"
                        action Jump("v14s51_purse")
                        pos (0, 170)
                if not "pillow" in freeroam12:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_pillow.webp"
                        hover "images/v14/Scene 51/v14s51_pillow_hover.webp"
                        action Jump("v14s51_pillow")
                        pos (1130, 380)
            else:
                timer 0.75 action Jump("v14s51_continue")

        elif v14s50_listen_to_aubrey_lindsey == 1:
            if len(freeroam12) < 4:
                if not "bedside" in freeroam12:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_bedside.webp"
                        hover "images/v14/Scene 51/v14s51_bedside_hover.webp"
                        action Jump("v14s51_bedside_table")
                        pos (970, 330)
                if not "desk" in freeroam12:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_desk.webp"
                        hover "images/v14/Scene 51/v14s51_desk_hover.webp"
                        action Jump("v14s51_desk_drawer")
                        pos (1710, 500)
                if not "closet" in freeroam12:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_closet.webp"
                        hover "images/v14/Scene 51/v14s51_closet_hover.webp"
                        action Jump("v14s51_closet")
                        pos (230, 5)
                if not "purse" in freeroam12:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_purse.webp"
                        hover "images/v14/Scene 51/v14s51_purse_hover.webp"
                        action Jump("v14s51_purse")
                        pos (0, 170)
                if not "pillow" in freeroam12:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_pillow.webp"
                        hover "images/v14/Scene 51/v14s51_pillow_hover.webp"
                        action Jump("v14s51_pillow")
                        pos (1130, 380)
            else:
                timer 0.75 action Jump("v14s51_continue")

        else:
            if len(freeroam12) < 5:
                if not "bedside" in freeroam12:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_bedside.webp"
                        hover "images/v14/Scene 51/v14s51_bedside_hover.webp"
                        action Jump("v14s51_bedside_table")
                        pos (970, 330)
                if not "desk" in freeroam12:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_desk.webp"
                        hover "images/v14/Scene 51/v14s51_desk_hover.webp"
                        action Jump("v14s51_desk_drawer")
                        pos (1710, 500)
                if not "closet" in freeroam12:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_closet.webp"
                        hover "images/v14/Scene 51/v14s51_closet_hover.webp"
                        action Jump("v14s51_closet")
                        pos (230, 5)
                if not "purse" in freeroam12:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_purse.webp"
                        hover "images/v14/Scene 51/v14s51_purse_hover.webp"
                        action Jump("v14s51_purse")
                        pos (0, 170)
                if not "pillow" in freeroam12:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_pillow.webp"
                        hover "images/v14/Scene 51/v14s51_pillow_hover.webp"
                        action Jump("v14s51_pillow")
                        pos (1130, 380)
            else:
                timer 0.75 action Jump("v14s51_continue")
                


        #-if MC chose to keep listening to Lindsey and Aubrey's conversation more than one time, MC can only choose 2 areas.
        #-if MC chose to keep listening to Lindsey and Aubrey's conversation once, MC can only choose 3 areas.
        #-if MC chose to go to Chloe's room and did not choose to keep listening, MC can choose 4 areas.