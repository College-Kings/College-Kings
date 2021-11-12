screen v14s51_room():
    tag free_roam

    imagemap:
        idle "images/v14/Scene 51/v14s51_2.webp"
        hover "images/v14/Scene 51/v14s51_2_screen_hover.webp"

        if v14s50_listen_to_aubrey_lindsey_2:
            if v14s51_interaction <= 1:
                # if not v14s51_bedside:
                #     imagebutton:
                #         idle "images/v14/Scene 51/v14s51_bedside.png"
                #         hover "images/v14/Scene 51/v14s51_bedside_hover.png"
                #         action Jump("v14s51_bedside_table")
                #         pos (0, 0)
                #     #hotspot (1008, 367, 191, 136) action Jump("v14s51_bedside_table")
                # if not v14s51_desk:
                #     imagebutton:
                #         idle "images/v14/Scene 51/v14s51_desk.png"
                #         hover "images/v14/Scene 51/v14s51_desk_hover.png"
                #         action Jump("v14s51_desk_drawer")
                #         pos (0, 0)
                #     #hotspot (1728, 535, 191, 202) action Jump("v14s51_desk_drawer")
                if not v14s51_closet:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_closet.png"
                        hover "images/v14/Scene 51/v14s51_closet_hover.png"
                        action Jump("v14s51_closet")
                        pos (230, 5)
                    #hotspot (280, 39, 269, 494) action Jump("v14s51_closet")
                # if not v14s51_purse:
                #     imagebutton:
                #         idle "images/v14/Scene 51/v14s51_purse.png"
                #         hover "images/v14/Scene 51/v14s51_purse_hover.png"
                #         action Jump("v14s51_purse")
                #         pos (0, 0)
                #     #hotspot (0, 265, 301, 527) action Jump("v14s51_purse")
                # if not v14s51_pillow:
                #     imagebutton:
                #         idle "images/v14/Scene 51/v14s51_pillow.png"
                #         hover "images/v14/Scene 51/v14s51_pillow.png"
                #         action Jump("v14s51_pillow")
                #         pos (0, 0)
                #     #hotspot (1146, 424, 263, 96) action Jump("v14s51_pillow")
            else:
                pass
                ## Continue button 

        elif v14s50_listen_to_aubrey_lindsey:
            if v14s51_interaction <= 2:
                if not v14s51_bedside:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_bedside.png"
                        hover "images/v14/Scene 51/v14s51_bedside_hover.png"
                        action Jump("v14s51_bedside_table")
                        pos (0, 0)
                    #hotspot (1008, 367, 191, 136) action Jump("v14s51_bedside_table")
                if not v14s51_desk:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_desk.png"
                        hover "images/v14/Scene 51/v14s51_desk_hover.png"
                        action Jump("v14s51_desk_drawer")
                        pos (0, 0)
                    #hotspot (1728, 535, 191, 202) action Jump("v14s51_desk_drawer")
                if not v14s51_closet:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_closet.png"
                        hover "images/v14/Scene 51/v14s51_closet_hover.png"
                        action Jump("v14s51_closet")
                        pos (0, 0)
                    #hotspot (280, 39, 269, 494) action Jump("v14s51_closet")
                if not v14s51_purse:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_purse.png"
                        hover "images/v14/Scene 51/v14s51_purse_hover.png"
                        action Jump("v14s51_purse")
                        pos (0, 0)
                    #hotspot (0, 265, 301, 527) action Jump("v14s51_purse")
                if not v14s51_pillow:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_pillow.png"
                        hover "images/v14/Scene 51/v14s51_pillow.png"
                        action Jump("v14s51_pillow")
                        pos (0, 0)
            else:
                pass
                ## Continue utton

        else:
            if v14s51_interaction <= 3:
                if not v14s51_bedside:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_bedside.png"
                        hover "images/v14/Scene 51/v14s51_bedside_hover.png"
                        action Jump("v14s51_bedside_table")
                        pos (0, 0)
                    #hotspot (1008, 367, 191, 136) action Jump("v14s51_bedside_table")
                if not v14s51_desk:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_desk.png"
                        hover "images/v14/Scene 51/v14s51_desk_hover.png"
                        action Jump("v14s51_desk_drawer")
                        pos (0, 0)
                    #hotspot (1728, 535, 191, 202) action Jump("v14s51_desk_drawer")
                if not v14s51_closet:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_closet.png"
                        hover "images/v14/Scene 51/v14s51_closet_hover.png"
                        action Jump("v14s51_closet")
                        pos (0, 0)
                    #hotspot (280, 39, 269, 494) action Jump("v14s51_closet")
                if not v14s51_purse:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_purse.png"
                        hover "images/v14/Scene 51/v14s51_purse_hover.png"
                        action Jump("v14s51_purse")
                        pos (0, 0)
                    #hotspot (0, 265, 301, 527) action Jump("v14s51_purse")
                if not v14s51_pillow:
                    imagebutton:
                        idle "images/v14/Scene 51/v14s51_pillow.png"
                        hover "images/v14/Scene 51/v14s51_pillow.png"
                        action Jump("v14s51_pillow")
                        pos (0, 0)
            else:
                pass
                


        #-if MC chose to keep listening to Lindsey and Aubrey's conversation more than one time, MC can only choose 2 areas.
        #-if MC chose to keep listening to Lindsey and Aubrey's conversation once, MC can only choose 3 areas.
        #-if MC chose to go to Chloe's room and did not choose to keep listening, MC can choose 4 areas.