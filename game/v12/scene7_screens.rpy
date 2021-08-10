screen murder_button_overlay(character):
    tag freeRoam

    hbox:
        pos (10, 10)
        spacing 15

        if v12s7_seenList:
            add Transform("images/v12/Scene 7/gui/eye_open.webp", size=(75, 75))
            text "This person can currently be seen by someone else" yalign 0.5
        else:
            add Transform("images/v12/Scene 7/gui/eye_closed.webp", size=(75, 75))

    imagebutton:
        align (0.97, 0.928)
        idle Transform("images/v12/Scene 7/gui/gun.webp", size=(100, 100))
        hover Transform("images/v12/Scene 7/gui/gun_hover.webp", size=(100, 100))
        if v12s7_seenList:
            action Jump("v12s7_mc_caught") # Check Label after transcribing review
        else:
            action [ Function(character.kill), Jump("MurderSuccess") ] # Check Label after transcribing review


screen v12s7_minimap(location):
    add Transform("images/v12/Scene 7/minimap/{}.webp".format(location), zoom=0.25)


### Lower Floor
screen v12s7_seating_back():
    tag freeRoam

    # No one
    if (emily in v12s7_killList and lauren in v12s7_killList) or (v12s7_emily and lauren in v12s7_killList) or (lauren in v12s7_killList):
        imagemap:
            idle "images/v12/Scene 7/Screens/Navigation 1c.webp"
            hover "images/v12/Scene 7/Buttons/nav 1.webp"

            hotspot (331, 898, 1227, 181) action Show("v12s7_seating_front")

    # Lauren only
    elif (emily in v12s7_killList) or (emily in v12s7_killList and lauren not in v12s7_killList) or (not emily_europe):
        imagemap:
            idle "images/v12/Scene 7/Screens/Navigation 1a.webp"
            hover "images/v12/Scene 7/Buttons/nav 1.webp"

            hotspot (1318, 182, 421, 605):
                if v12s7_lauren:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferla1", returnScreen="v12s7_seating_back", seenList=[])
                else:
                    action Jump("v12s7_lauren1") # Lauren

            hotspot (331, 898, 1227, 181) action Show("v12s7_seating_front")

    # Lauren and Emily
    elif (emily_europe and not v12s7_emily and not emily in v12s7_killList and lauren not in v12s7_killList):
        imagemap:
            idle "images/v12/Scene 7/Screens/Navigation 1b.webp"
            hover "images/v12/Scene 7/Buttons/nav 1.webp"

            hotspot (1318, 182, 421, 605):
                if v12s7_lauren:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferla1", returnScreen="v12s7_seating_back", seenList=[emily])
                else:
                    action Jump("v12s7_lauren1") # Lauren

            hotspot (180, 182, 380, 605) action Jump("v12s7_emily1") # Emily

            hotspot (331, 898, 1227, 181) action Show("v12s7_seating_front")

    use v12s7_minimap(location="ld_seating")

    on "replaced" action SetVariable("previous_location", "v12s7_seating_back")

screen v12s7_seating_front():
    tag freeRoam

    # No one
    if (v12s7_samantha and ms_rose in v12s7_killList) or (ms_rose in v12s7_killList and not v11_invite_sam_europe):
        imagemap:
            idle "images/v12/Scene 7/Screens/Navigation 2c.webp"
            hover "images/v12/Scene 7/Buttons/nav 2.webp"

            hotspot (367, 0, 1205, 140) action Show("v12s7_seating_back")
            hotspot (327, 917, 1216, 163) action Show("v12s7_walkway")
    
    # Ms Rose
    elif (v12s7_samantha and ms_rose not in v12s7_killList) or (not v11_invite_sam_europe and ms_rose not in v12s7_killList):
        imagemap:
            idle "images/v12/Scene 7/Screens/Navigation 2b.webp"
            hover "images/v12/Scene 7/Buttons/nav 2.webp"

            hotspot (1585, 7, 335, 631):
                if v12s7_msrose:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12fermsr1a", returnScreen="v12s7_seating_front", seenList=[])
                else:
                    action Jump("v12s7_msrose1") # ms rose

            hotspot (367, 0, 1205, 140) action Show("v12s7_seating_back")
            hotspot (327, 917, 1216, 163) action Show("v12s7_walkway")

    # Samantha and Ms Rose
    elif (v11_invite_sam_europe and not v12s7_samantha and ms_rose not in v12s7_killList):
        imagemap:
            idle "images/v12/Scene 7/Screens/Navigation 2a.webp"
            hover "images/v12/Scene 7/Buttons/nav 2.webp"

            hotspot (1585, 7, 335, 631):
                if v12s7_msrose:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12fermsr1a", returnScreen="v12s7_seating_front", seenList=[samantha])
                else:
                    action Jump("v12s7_msrose1") # ms rose

            hotspot (23, 0, 344, 627) action Jump("v12s7_sam_cameron") # sameron

            hotspot (367, 0, 1205, 140) action Show("v12s7_seating_back")
            hotspot (327, 917, 1216, 163) action Show("v12s7_walkway")

    use v12s7_minimap(location="ld_seating")

    on "replaced" action SetVariable("previous_location", "v12s7_seating_front")


screen v12s7_walkway():
    tag freeRoam

    imagemap:
        idle "images/v12/Scene 7/Screens/Navigation 3.webp"
        hover "images/v12/Scene 7/Buttons/nav 3.webp"

        hotspot (0, 30, 126, 1020) action Show("v12s7_left_walkway_middle")
        hotspot (1793, 30, 126, 1020) action Show("v12s7_right_walkway_middle")
        hotspot (242, 950, 1385, 130) action Show(previous_location)

    use v12s7_minimap(location="ld_walkway")

    on "replaced" action SetVariable("previous_location", "v12s7_walkway")


screen v12s7_right_walkway_middle():
    tag freeRoam

    imagemap:
        idle "images/v12/Scene 7/Screens/Navigation 4.webp"
        hover "images/v12/Scene 7/Buttons/nav 4.webp"

        hotspot (84, 26, 186, 944) action Show("v12s7_right_walkway_front")
        hotspot (1516, 12, 186, 955) action Show("v12s7_right_walkway_back")
        hotspot (306, 928, 1231, 152) action Show("v12s7_walkway")

    use v12s7_minimap(location="ld_right_walkway")

    on "replaced" action SetVariable("previous_location", "v12s7_right_walkway_middle")


screen v12s7_left_walkway_middle():
    tag freeRoam

    imagemap:
        idle "images/v12/Scene 7/Screens/Navigation 5.webp"
        hover "images/v12/Scene 7/Buttons/nav 5.webp"

        hotspot (286, 0, 189, 892) action Show("v12s7_left_walkway_front")
        hotspot (1610, 0, 182, 959) action Show("v12s7_left_walkway_back")
        hotspot (306, 928, 1231, 152) action Show("v12s7_walkway")


    use v12s7_minimap(location="ld_left_walkway")
    
    on "replaced" action SetVariable("previous_location", "v12s7_left_walkway_middle")


screen v12s7_left_walkway_back():
    tag freeRoam

    imagemap:
        if ms_rose in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 6c.webp" # No one
        else:
            idle "images/v12/Scene 7/Screens/Navigation 6b.webp" # Ms Rose
        hover "images/v12/Scene 7/Buttons/nav 6.webp"

        hotspot (286, 0, 1348, 191) action Show("v12s7_rear")
        hotspot (286, 889, 1348, 191) action Show("v12s7_left_walkway_middle")

    use v12s7_minimap(location="ld_left_walkway")

    on "replaced" action SetVariable("previous_location", "v12s7_left_walkway_back")


screen v12s7_rear():
    tag freeRoam

    imagemap:
        if v12s7_lindsey_moved and lindsey not in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 7a.webp" # Lindsey
        else:
            idle "images/v12/Scene 7/Screens/Navigation 7b.webp" # No one
        hover "images/v12/Scene 7/Buttons/nav 7.webp"

        if v12s7_lindsey_moved and lindsey not in v12s7_killList:
            hotspot (563, 303, 565, 664):
                if v12s7_lindsey2:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferli3", returnScreen="v12s7_rear", seenList=[])
                else:
                    action Jump("v12s7_lindsey2") # lindsey
  
        hotspot (338, 984, 1200, 96) action Show("v12s7_left_walkway_back")

    use v12s7_minimap(location="ld_rear")

    on "replaced" action SetVariable("previous_location", "v12s7_rear")


screen v12s7_right_walkway_back():
    tag freeRoam

    imagemap:
        if (v12s7_samantha and samantha not in v12s7_killList):
            idle "images/v12/Scene 7/Screens/Navigation 8a.webp"
        else:
            idle "images/v12/Scene 7/Screens/Navigation 8b.webp"
        hover "images/v12/Scene 7/Buttons/nav 8.webp"

        if (v12s7_samantha and samantha not in v12s7_killList):
            hotspot (813, 237, 211, 508):
                if v12s7_samantha2:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12fersam1", returnScreen="v12s7_right_walkway_back", seenList=[])
                else:
                    action Jump("v12s7_sam2") #samantha

        hotspot (338, 970, 1200, 110) action Show("v12s7_right_walkway_middle")

    use v12s7_minimap(location="ld_right_walkway")
    
    on "replaced" action SetVariable("previous_location", "v12s7_right_walkway_back")


screen v12s7_right_walkway_front():
    tag freeRoam

    imagemap:
        idle "images/v12/Scene 7/Screens/Navigation 9.webp"
        hover "images/v12/Scene 7/Buttons/nav 9.webp"

        hotspot (304, 94, 104, 735) action Show("v12s7_rear_gallery")
        hotspot (747, 186, 310, 521) action Show("v12s7_kitchen")
        hotspot (345, 967, 1193, 113) action Show("v12s7_right_walkway_middle")

    use v12s7_minimap(location="ld_right_walkway")

    on "replaced" action SetVariable("previous_location", "v12s7_right_walkway_front")


screen v12s7_kitchen():
    tag freeRoam

    imagemap:
        if v12s7_emily and not emily in v12s7_killList and chris not in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 10a.webp" # Chris and Emily
        elif v12s7_emily and emily not in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 10d.webp" # Emily
        elif chris not in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 10b.webp" # Chris
        else:
            idle "images/v12/Scene 7/Screens/Navigation 10d.webp"
        hover "images/v12/Scene 7/Buttons/nav 10.webp"

        if chris not in v12s7_killList:
            hotspot (1116, 33, 751, 1047):
                if v12s7_chris:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferchr1", returnScreen="v12s7_kitchen", seenList=[])
                else:
                    action Jump("v12s7_chris1") # chris

        hotspot (541, 206, 396, 591) action Show("v12s7_bow")
        hotspot (339, 983, 1198, 97) action Show("v12s7_right_walkway_front")

    use v12s7_minimap(location="ld_kitchen")

    on "replaced" action SetVariable("previous_location", "v12s7_kitchen")


screen v12s7_bow():
    tag freeRoam

    imagemap:
        if v12s7_emily and emily not in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 11a.webp" # Emily
        else:
            idle "images/v12/Scene 7/Screens/Navigation 11b.webp"
        hover "images/v12/Scene 7/Buttons/nav 11.webp"

        if v12s7_emily and emily not in v12s7_killList:
            hotspot (920, 216, 368, 864):
                if v12s7_emily2:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12feremi1", returnScreen="v12s7_bow", seenList=[])
                else:
                    action Jump("v12s7_emily2") # emily

        hotspot (339, 983, 1198, 97) action Show("v12s7_kitchen")

    use v12s7_minimap(location="ld_bow")

    on "replaced" action SetVariable("previous_location", "v12s7_bow")


screen v12s7_left_walkway_front():
    tag freeRoam

    imagemap:
        if v11_pen_goes_europe and penelope not in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 12a.webp" # Penelope
        else:
            idle "images/v12/Scene 7/Screens/Navigation 12b.webp"
        hover "images/v12/Scene 7/Buttons/nav 12.webp"

        if v11_pen_goes_europe and penelope not in v12s7_killList:
            hotspot (223, 326, 752, 656):
                if v12s7_penelope:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferpen1", returnScreen="v12s7_left_walkway_front", seenList=[])
                else:
                    action Jump("v12s7_penelope1") #penelope
        
        hotspot (293, 0, 1385, 130) action Show("v12s7_foyer")
        hotspot (1693, 73, 140, 787) action Show("v12s7_rear_gallery")
        hotspot (353, 984, 1158, 96) action Show("v12s7_left_walkway_middle")

    use v12s7_minimap(location="ld_left_walkway")

    on "replaced" action SetVariable("previous_location", "v12s7_left_walkway_front")


screen v12s7_foyer():
    tag freeRoam

    imagemap:
        if v12s7_imre and imre not in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 13a.webp" # Imre
        else:
            idle "images/v12/Scene 7/Screens/Navigation 13b.webp"
        hover "images/v12/Scene 7/Buttons/nav 13.webp"

        if v12s7_imre and imre not in v12s7_killList:
            hotspot (821, 493, 492, 490):
                if v12s7_imre:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferim1", returnScreen="v12s7_foyer", seenList=[])
                else:
                    action Jump("v12s7_imre2") #imre

        hotspot (339, 983, 1198, 97) action Show("v12s7_left_walkway_front")
        hotspot (1423, 66, 497, 796) action Show("v12s7_bow")

    use v12s7_minimap(location="ld_foyer")

    on "replaced" action SetVariable("previous_location", "v12s7_foyer")


# MIDDLE FLOOR
screen v12s7_left_viewpoint():
    tag freeRoam

    imagemap:
        if not v12s7_riley and riley not in v12s7_killList and chloe not in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 14a.webp" # Chloe and Riley
        elif v12s7_riley2 and chloe in v12s7_killList and riley not in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 14b.webp" # Riley
        elif v12s7_riley and chloe not in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 14c.webp" # Chloe
        else:
            idle "images/v12/Scene 7/Screens/Navigation 14d.webp" # No one

        if not v12s7_riley and riley not in v12s7_killList and chloe not in v12s7_killList:
            hover "images/v12/Scene 7/Buttons/nav 14a.webp" # Chloe and Riley
        elif v12s7_riley2 and chloe in v12s7_killList and riley not in v12s7_killList:
            hover "images/v12/Scene 7/Buttons/nav 14b.webp" # Riley
        else:
            hover "images/v12/Scene 7/Buttons/nav 14c.webp" # Chloe

        if not v12s7_riley and riley not in v12s7_killList and chloe not in v12s7_killList:
            hotspot (685, 117, 540, 786):
                if v12s7_riley3:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferric1", returnScreen="v12s7_left_viewpoint", seenList=[chloe, josh] if josh_europe and not v12s7_josh else [chloe])
                elif v12s7_riley2:
                    action Jump("v12s7_riley3") #Riley & Chloe
                else:
                    action Jump("v12s7_riley1") #Riley & Chloe

        elif v12s7_riley2 and chloe in v12s7_killList and riley not in v12s7_killList:
            hotspot (835, 191, 361, 772):
                if v12s7_riley3:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferril1", returnScreen="v12s7_left_viewpoint", seenList=[josh] if josh_europe and not v12s7_josh else [])
                else:
                    action Jump("v12s7_riley3a") # riley

        elif v12s7_riley2 and chloe in v12s7_killList and riley not in v12s7_killList:
            hotspot (689, 203, 271, 673):
                if v12s7_chloe:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferch1", returnScreen="v12s7_left_viewpoint", seenList=[riley, josh] if josh_europe and not v12s7_josh else [riley])
                else:
                    action Jump("v12s7_chloe1") # chloe

        hotspot (338, 976, 1200, 104) action Show("md_rear_gallery")

    use v12s7_minimap(location="md_left_viewport")

    on "replaced" action SetVariable("previous_location", "v12s7_left_viewpoint")


screen v12s7_right_viewpoint():
    tag freeRoam

    imagemap:
        if not v12s7_josh_moved and josh not in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 15a.webp" # Josh
        else:
            idle "images/v12/Scene 7/Screens/Navigation 15b.webp" # No one
        hover "images/v12/Scene 7/Buttons/nav 15.webp"

        if not v12s7_josh_moved and josh not in v12s7_killList:
            hotspot (729, 375, 451, 545):
                if v12s7_josh:
                    if ((not v12s7_riley or v12s7_riley2) and riley not in v12s7_killList) and (chloe not in v12s7_killList):
                        action Call("v12s7_free_roam_spoken", backgroundImg="v12ferjo1", returnScreen="v12s7_right_viewpoint", seenList=[riley, chloe])
                    elif (not v12s7_riley or v12s7_riley2) and riley not in v12s7_killList:
                        action Call("v12s7_free_roam_spoken", backgroundImg="v12ferjo1", returnScreen="v12s7_right_viewpoint", seenList=[riley])
                    elif chloe not in v12s7_killList:
                        action Call("v12s7_free_roam_spoken", backgroundImg="v12ferjo1", returnScreen="v12s7_right_viewpoint", seenList=[chloe])
                    else:
                        action Call("v12s7_free_roam_spoken", backgroundImg="v12ferjo1", returnScreen="v12s7_right_viewpoint", seenList=[])
                else:
                    action Jump("v12s7_josh1") # josh

        hotspot (382, 972, 1106, 98) action Show(previous_location)

    use v12s7_minimap(location="md_right_viewport")

    on "replaced" action SetVariable("previous_location", "v12s7_right_viewpoint")


screen v12s7_rear_gallery():
    tag freeRoam

    imagemap:
        if v11_invite_sam_europe and v12s7_samantha:
            idle "images/v12/Scene 7/Screens/Navigation 27a.webp" # Mr Lee and Cameron
        else:
            idle "images/v12/Scene 7/Screens/Navigation 27b.webp" # Mr Lee
        hover "images/v12/Scene 7/Buttons/nav 27.webp"

        if v11_invite_sam_europe and v12s7_samantha:
            hotspot (894, 267, 257, 744):
                if v12s7_cameron:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12fercam3", returnScreen="v12s7_rear_gallery", seenList=[])
                else:
                    action Jump("v12s7_cameron2")

        hotspot (172, 320, 239, 653):
            action Jump("v12s7_mrlee")
        
        hotspot (894, 267, 257, 744) action Show(previous_location)

    use v12s7_minimap(location="md_rear_gallery")

    on "replaced" action SetVariable("previous_location", "v12s7_rear_gallery")


screen v12s7_right_gallery_back():
    tag freeRoam

    imagemap:
        if not v12s7_imre:
            idle "images/v12/Scene 7/Screens/Navigation 16a.webp" # Ryan and Imre
        elif ryan in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 16c.webp" # No one
        else:
            idle "images/v12/Scene 7/Screens/Navigation 16b.webp" # Ryan

        if v12s7_imre:
            hover "images/v12/Scene 7/Buttons/nav 16b.webp"
        else:
            hover "images/v12/Scene 7/Buttons/nav 16.webp"

        if v12s7_imre:
            hotspot (932, 265, 240, 716):
                if v12s7_ryan:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferry1", returnScreen="v12s7_right_gallery_back", seenList=[ryan] if (v12s7_riley and not v12s7_riley2) or amber in v12s7_killList else [ryan, amber])
                else:
                    action Jump("v12s7_ryan1") # Ryan

            hotspot (932, 265, 240, 716) action Show(previous_location)

        else:
            hotspot (679, 213, 461, 829):
                action Jump("v12s7_ryan_imre1") # Imre & Ryan

            hotspot (457, 1042, 961, 36) action Show(previous_location)

    use v12s7_minimap(location="md_right_gallery")

    on "replaced" action SetVariable("previous_location", "v12s7_right_gallery_back")


screen v12s7_right_gallery_front():
    tag freeRoam

    imagemap:
        if v12s7_riley and not v12s7_riley2 and amber not in v12s7_killList and riley not in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 17a.webp" # Riley and Amber
            hover "images/v12/Scene 7/Buttons/nav 17a.webp"

            hotspot (757, 270, 316, 649) action NullAction()

        elif v12s7_riley and not v12s7_riley2 and riley not in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 17b.webp" # Riley
            hover "images/v12/Scene 7/Buttons/nav 17b.webp"

            hotspot (758, 279, 223, 640) action NullAction()

        elif (not v12s7_riley and amber not in v12s7_killList) or (v12s7_riley and riley in v12s7_killList):
            idle "images/v12/Scene 7/Screens/Navigation 17c.webp" # Amber
            hover "images/v12/Scene 7/Buttons/nav 17c.webp"

            hotspot (893, 297, 178, 525) action NullAction()

        else:
            idle "images/v12/Scene 7/Screens/Navigation 17d.webp" # No one
            hover "images/v12/Scene 7/Buttons/nav 17d.webp"

        hotspot (376, 991, 1115, 87) action Show(previous_location)

    use v12s7_minimap(location="md_right_gallery")

    on "replaced" action SetVariable("previous_location", "v12s7_right_gallery_front")


screen v12s7_utility():
    tag freeRoam

    imagemap:
        if v12s7_josh_moved and josh not in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 18a.webp" # Josh
        else:
            idle "images/v12/Scene 7/Screens/Navigation 18b.webp" # No one
        hover "images/v12/Scene 7/Buttons/nav 18.webp"

        if v12s7_josh_moved and josh not in v12s7_killList:
            hotspot(413, 183, 452, 895):
                if v12s7_josh:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferjos3", returnScreen="v12s7_utility", seenList=[])
                else:
                    action Jump("v12s7_josh2") # Josh

        hotspot (1847, 113, 72, 865) action Show(previous_location)

    use v12s7_minimap(location="md_utility")

    on "replaced" action SetVariable("previous_location", "v12s7_utility")


screen v12s7_front_gallery():
    tag freeRoam

    imagemap:
        if v12s7_riley and not v12s7_riley2 and amber not in v12s7_killList and riley not in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 19a.webp" # Amber and Riley
            hover "images/v12/Scene 7/Buttons/nav 19a.webp"

            hotspot (411, 59, 640, 1018):
                action Jump("v12s7_riley2_amber") # Riley & Amber

        elif v12s7_riley and not v12s7_riley2 and riley not in v12s7_killList: # Amber
            idle "images/v12/Scene 7/Screens/Navigation 19c.webp"
            hover "images/v12/Scene 7/Buttons/nav 19c.webp"

            hotspot (749, 159, 309, 918):
                if v12s7_riley2:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferrile1", returnScreen="v12s7_front_gallery", seenList=[])
                else:
                    action Jump("v12s7_riley2") # Amber

        elif (not v12s7_riley and amber not in v12s7_killList) or (v12s7_riley and riley in v12s7_killList): # Riley
            idle "images/v12/Scene 7/Screens/Navigation 19b.webp"
            hover "images/v12/Scene 7/Buttons/nav 19b.webp"

            hotspot (407, 60, 481, 1018):
                if v12s7_amber:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12feram1a", returnScreen="v12s7_front_gallery", seenList=[] if v12s7_imre else [imre, ryan])
                else:
                    action Jump("v12s7_amber1") # Riley
                    
        else: 
            idle "images/v12/Scene 7/Screens/Navigation 19d.webp" # No one
            hover "images/v12/Scene 7/Buttons/nav 19c.webp"

        hotspot (383, 0, 1198, 97) action Show("v12s7_balcony_middle")
        hotspot (339, 983, 1198, 97) action Show(previous_location)
    
    use v12s7_minimap(location="md_front_gallery")

    on "replaced" action SetVariable("previous_location", "v12s7_front_gallery")


screen v12s7_balcony_middle():
    tag freeRoam

    imagemap:
        idle "images/v12/Scene 7/Screens/Navigation 20a.webp"
        hover "images/v12/Scene 7/Buttons/nav 20.webp"

        hotspot (242, 950, 1385, 130) action Show(previous_location)
        
    use v12s7_minimap(location="md_balcony")

    on "replaced" action SetVariable("previous_location", "v12s7_balcony_middle")


screen v12s7_balcony_left():
    tag freeRoam

    imagemap:
        if nora in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 21b.webp" # No one
        else:
            idle "images/v12/Scene 7/Screens/Navigation 21a.webp" # Nora
        hover "images/v12/Scene 7/Buttons/nav 21.webp"

        if nora not in v12s7_killList:
            hotspot (507, 152, 282, 926):
                if v12s7_nora:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12fernor1", returnScreen="v12s7_balcony_left", seenList=[] if v12s7_aubrey_moved else [riley])
                else:
                    action Jump("v12s7_nora1") # Nora

        hotspot (493, 137, 307, 943) action Show(previous_location)
    
    use v12s7_minimap(location="md_balcony")

    on "replaced" action SetVariable("previous_location", "v12s7_balcony_left")


screen v12s7_balcony_right():
    tag freeRoam

    imagemap:
        if aubrey in v12s7_killList or v12s7_aubrey_moved:
            idle "images/v12/Scene 7/Screens/Navigation 22b.webp" # No one
        else:
            idle "images/v12/Scene 7/Screens/Navigation 22a.webp" # Aubrey
        hover "images/v12/Scene 7/Buttons/nav 22.webp"

        if not (aubrey in v12s7_killList or v12s7_aubrey_moved):
            hotspot (493, 137, 311, 943):
                if v12s7_aubrey:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferau1a", returnScreen="v12s7_balcony_right", seenList=[nora])
                else:
                    action Jump("v12s7_aubrey1") # Aubrey

        hotspot (806, 967, 1114, 114) action Show(previous_location)

    use v12s7_minimap(location="md_balcony")

    on "replaced" action SetVariable("previous_location", "v12s7_balcony_right")


screen v12s7_left_gallery_back():
    tag freeRoam

    imagemap:
        if aubrey in v12s7_killList or not v12s7_aubrey_moved:
            idle "images/v12/Scene 7/Screens/Navigation 23b.webp" # No one
        else:
            idle "images/v12/Scene 7/Screens/Navigation 23a.webp" # Aubrey
        hover "images/v12/Scene 7/Buttons/nav 23.webp"

        hotspot (899, 210, 321, 517) action Show("v12s7_left_gallery_front")
        hotspot (223, 967, 1422, 114) action Show(previous_location)

    use v12s7_minimap(location="md_left_gallery")

    on "replaced" action SetVariable("previous_location", "v12s7_left_gallery_back")


screen v12s7_left_gallery_front():
    tag freeRoam

    imagemap:
        if aubrey in v12s7_killList or not v12s7_aubrey_moved:
            idle "images/v12/Scene 7/Screens/Navigation 24b.webp" # No one
        else:
            idle "images/v12/Scene 7/Screens/Navigation 24a.webp" # Aubrey
        hover "images/v12/Scene 7/Buttons/nav 24.webp"

        hotspot (0, 0, 105, 1080) action Show(previous_location)
        hotspot (479, 0, 821, 1080) action Show("v12s7_bathroom")
        hotspot (1545, 0, 375, 1080) action Show("v12s7_captains_room")

    use v12s7_minimap(location="md_left_gallery")

    on "replaced" action SetVariable("previous_location", "v12s7_left_gallery_front")


screen v12s7_bathroom():
    tag freeRoam

    imagemap:
        if aubrey in v12s7_killList or not v12s7_aubrey_moved:
            idle "images/v12/Scene 7/Screens/Navigation 25b.webp" # No one
        else:
            idle "images/v12/Scene 7/Screens/Navigation 25a.webp" # Aubrey
        hover "images/v12/Scene 7/Buttons/nav 25.webp"
    
        if not (aubrey in v12s7_killList or not v12s7_aubrey_moved):
            hotspot (657, 196, 483, 878):
                if v12s7_aubrey2:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferauh1a", returnScreen="v12s7_bathroom", seenList=[])
                else:
                    action Jump("v12s7_aubrey2") # Aubrey
                
        hotspot (1836, 79, 82, 959) action Show(previous_location)

    use v12s7_minimap(location="md_bathroom")

    on "replaced" action SetVariable("previous_location", "v12s7_bathroom")


screen v12s7_captains_room():
    tag freeRoam
    
    imagemap:
        if not v12s7_lindsey_moved:
            idle "images/v12/Scene 7/Screens/Navigation 26a.webp" # Lindsey and Charli
            hover "images/v12/Scene 7/Buttons/nav 26a.webp"

            hotspot (506, 117, 1013, 959):
                if v12s7_lindsey:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferlich1", returnScreen="v12s7_captains_room", seenList=[lindsey, charli])
                else:
                    action Jump("v12s7_lindsey_charlie1") # Lindsey & Charli

        elif charli in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 26c.webp" # Charli
            hover "images/v12/Scene 7/Buttons/nav 26b.webp"

            hotspot (1157, 163, 254, 720):
                if v12s7_charli:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12fercha1", returnScreen="v12s7_captains_room", seenList=[])
                else:
                    action Jump("v12s7_charli2") # Charli

        else:
            idle "images/v12/Scene 7/Screens/Navigation 26b.webp" # No one
            hover "images/v12/Scene 7/Buttons/nav 26c.webp"

        hotspot (1824, 79, 95, 957) action Show(previous_location)

    use v12s7_minimap(location="ud_captains_room")

    on "replaced" action SetVariable("previous_location", "v12s7_captains_room")
