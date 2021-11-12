screen v14s51_room():
    tag free_roam

    imagemap:
        idle "images/v14/Scene 51/v14s51_2.webp"
        hover "images/v14/Scene 51/v14s51_2_screen_hover.webp"

        if v14s50_listen_to_aubrey_lindsey_2:
            if v14s51_interaction <= 1:
                if not v14s51_bedside:
                    hotspot (1020, 383, 148, 103) action Jump("v14s51_bedside_table")
                if not v14s51_desk:
                    hotspot (1758, 557, 161, 139) action Jump("v14s51_desk_drawer")
                if not v14s51_closet:
                    hotspot (297, 51, 241, 483) action Jump("v14s51_closet")
                if not v14s51_purse:
                    hotspot (7, 417, 292, 316) action Jump("v14s51_purse")
                if not v14s51_pillow:
                    hotspot (1198, 442, 165, 77) action Jump("v14s51_pillow")
            else:
                pass
                ## Continue button 

        elif v14s50_listen_to_aubrey_lindsey:
            if v14s51_interaction <= 2:
                if not v14s51_bedside:
                    hotspot (1020, 383, 148, 103) action Jump("v14s51_bedside_table")
                if not v14s51_desk:
                    hotspot (1758, 557, 161, 139) action Jump("v14s51_desk_drawer")
                if not v14s51_closet:
                    hotspot (297, 51, 241, 483) action Jump("v14s51_closet")
                if not v14s51_purse:
                    hotspot (7, 417, 292, 316) action Jump("v14s51_purse")
                if not v14s51_pillow:
                    hotspot (1198, 442, 165, 77) action Jump("v14s51_pillow")
            else:
                pass
                ## Continue utton

        else:
            if v14s51_interaction <= 3:
                if not v14s51_bedside:
                    hotspot (1020, 383, 148, 103) action Jump("v14s51_bedside_table")
                if not v14s51_desk:
                    hotspot (1758, 557, 161, 139) action Jump("v14s51_desk_drawer")
                if not v14s51_closet:
                    hotspot (297, 51, 241, 483) action Jump("v14s51_closet")
                if not v14s51_purse:
                    hotspot (7, 417, 292, 316) action Jump("v14s51_purse")
                if not v14s51_pillow:
                    hotspot (1198, 442, 165, 77) action Jump("v14s51_pillow")
            else:
                pass
                
    button:
        align (0.5, 0.95)
        action Jump ("v14s51_continue")
        maximum (707, 104)
        add "gui/center.webp"
        text "Leave Chloe's Room" align (0.5, 0.5)


        #-if MC chose to keep listening to Lindsey and Aubrey's conversation more than one time, MC can only choose 2 areas.
        #-if MC chose to keep listening to Lindsey and Aubrey's conversation once, MC can only choose 3 areas.
        #-if MC chose to go to Chloe's room and did not choose to keep listening, MC can choose 4 areas.