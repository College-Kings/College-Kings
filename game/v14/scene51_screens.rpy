screen v14s51_room():
    tag free_roam

    imagemap:
        idle "images/v14/Scene 51/v14s51_2.webp"
        hover "images/v14/Scene 51/v14s51_2_screen_hover.webp"

        if v14s50_listen_to_aubrey_lindsey_2:
            if v14s51_interaction <= 2:
                hotspot (1020, 383, 148, 103) action Show("v14s51_bedside_table")
                hotspot (1758, 557, 161, 139) action Show("v14s51_desk_drawer")
                hotspot (297, 51, 241, 483) action Show("v14s51_closet")
                hotspot (7, 417, 292, 316) action Show("v14s51_purse")
                hotspot (1198, 442, 165, 77) action Show("v14s51_pillow")
            else:
                ## Continue button 

        elif v14s50_listen_to_aubrey_lindsey:
            if v14s51_interaction <= 3:
                hotspot (1020, 383, 148, 103) action Show("v14s51_bedside_table")
                hotspot (1758, 557, 161, 139) action Show("v14s51_desk_drawer")
                hotspot (297, 51, 241, 483) action Show("v14s51_closet")
                hotspot (7, 417, 292, 316) action Show("v14s51_purse")
                hotspot (1198, 442, 165, 77) action Show("v14s51_pillow")
            else:
                ## Continue utton

        else:
            if v14s51_interaction <= 4:
                hotspot (1020, 383, 148, 103) action Show("v14s51_bedside_table")
                hotspot (1758, 557, 161, 139) action Show("v14s51_desk_drawer")
                hotspot (297, 51, 241, 483) action Show("v14s51_closet")
                hotspot (7, 417, 292, 316) action Show("v14s51_purse")
                hotspot (1198, 442, 165, 77) action Show("v14s51_pillow")
            else:
                ## Continue button


        #-if MC chose to keep listening to Lindsey and Aubrey's conversation more than one time, MC can only choose 2 areas.
        #-if MC chose to keep listening to Lindsey and Aubrey's conversation once, MC can only choose 3 areas.
        #-if MC chose to go to Chloe's room and did not choose to keep listening, MC can choose 4 areas.