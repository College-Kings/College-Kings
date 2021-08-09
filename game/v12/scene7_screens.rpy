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


screen v12s7_walkway():
    tag freeRoam

    imagemap:
        idle "images/v12/Scene 7/Screens/Navigation 3.webp"
        hover "images/v12/Scene 7/Buttons/nav 3.webp"

        hotspot (0, 30, 126, 1020) action Show("v12s7_left_walkway_middle")
        hotspot (1793, 30, 126, 1020) action Show("v12s7_right_walkway_middle")

    use v12s7_minimap(location="ld_walkway")


screen v12s7_right_walkway_middle():
    tag freeRoam

    imagemap:
        idle "images/v12/Scene 7/Screens/Navigation 4.webp"
        hover "images/v12/Scene 7/Buttons/nav 4.webp"

        hotspot (84, 26, 186, 944) action Show("v12s7_right_walkway_front")
        hotspot (1516, 12, 186, 955) action Show("v12s7_right_walkway_back")
        hotspot (306, 928, 1231, 152) action Show("v12s7_walkway")

    use v12s7_minimap(location="ld_right_walkway")


screen v12s7_left_walkway_middle():
    tag freeRoam

    imagemap:
        idle "images/v12/Scene 7/Screens/Navigation 5.webp"
        hover "images/v12/Scene 7/Buttons/nav 5.webp"

        hotspot (286, 0, 189, 892) action Show("v12s7_left_walkway_front")
        hotspot (1610, 0, 182, 959) action Show("v12s7_left_walkway_back")
        hotspot (306, 928, 1231, 152) action Show("v12s7_walkway")


    use v12s7_minimap(location="ld_left_walkway")
    

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
    

screen v12s7_right_walkway_front():
    tag freeRoam

    imagemap:
        idle "images/v12/Scene 7/Screens/Navigation 9.webp"
        hover "images/v12/Scene 7/Buttons/nav 9.webp"

        hotspot (304, 94, 104, 735) action Show("v12s7_rear_gallery")
        hotspot (747, 186, 310, 521) action Show("v12s7_kitchen")
        hotspot (345, 967, 1193, 113) action Show("v12s7_right_walkway_middle")

    use v12s7_minimap(location="ld_right_walkway")


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


# MIDDLE FLOOR
screen v12s7_left_viewpoint():
    tag freeRoam

    # Chloe and Riley
    if not v12s7_riley and riley not in v12s7_killList and chloe not in v12s7_killList:
        imagemap:
            ground "images/v12/Scene 7/Screens/Navigation 14a.webp"
            insensitive "images/v12/Scene 7/Screens/Navigation 14a.webp"
            hover "images/v12/Scene 7/Screens/Navigation 14a_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_riley3:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferric1", returnScreen="v12s7_left_viewpoint", seenList=[chloe, josh] if josh_europe and not v12s7_josh else [chloe])
                elif v12s7_riley2:
                    action Jump("v12s7_riley3") #Riley & Chloe
                else:
                    action Jump("v12s7_riley1") #Riley & Chloe
                    
    
    # Riley
    elif v12s7_riley2 and chloe in v12s7_killList and riley not in v12s7_killList:
        imagemap:
            ground "images/v12/Scene 7/Screens/Navigation 14b.webp"
            insensitive "images/v12/Scene 7/Screens/Navigation 14b.webp"
            hover "images/v12/Scene 7/Screens/Navigation 14b_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_riley3:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferril1", returnScreen="v12s7_left_viewpoint", seenList=[josh] if josh_europe and not v12s7_josh else [])
                else:
                    action Jump("v12s7_riley3a") # riley

    # Chloe
    elif v12s7_riley and chloe not in v12s7_killList:
        imagemap:
            ground "images/v12/Scene 7/Screens/Navigation 14c.webp"
            insensitive "images/v12/Scene 7/Screens/Navigation 14c.webp"
            hover "images/v12/Scene 7/Screens/Navigation 14c_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_chloe:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferch1", returnScreen="v12s7_left_viewpoint", seenList=[riley, josh] if josh_europe and not v12s7_josh else [riley])
                else:
                    action Jump("v12s7_chloe1") # chloe

    # No one
    else:
        add "images/v12/Scene 7/Screens/Navigation 14d.webp"

    use v12s7_minimap(location="md_left_viewport")


screen v12s7_right_viewpoint():
    tag freeRoam

    # Josh
    if not v12s7_josh_moved and josh not in v12s7_killList:
        imagemap:
            ground "images/v12/Scene 7/Screens/Navigation 15a.webp"
            insensitive "images/v12/Scene 7/Screens/Navigation 15a.webp"
            hover "images/v12/Scene 7/Screens/Navigation 15a_hover.webp"

            hotspot (x, y, width, height):
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

    # No one
    else:
        add "images/v12/Scene 7/Screens/Navigation 15b.webp"

    use v12s7_minimap(location="md_right_viewport")


screen v12s7_rear_gallery():
    tag freeRoam

    # Mr Lee and Cameron
    if v11_invite_sam_europe and v12s7_samantha:
        imagemap:
            ground "images/v12/Scene 7/Screens/Navigation 27a.webp"
            insensitive "images/v12/Scene 7/Screens/Navigation 27a.webp"
            hover "images/v12/Scene 7/Screens/Navigation 27a_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_cameron:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12fercam3", returnScreen="v12s7_rear_gallery", seenList=[])
                else:
                    action Jump("v12s7_cameron2")
                    
            hotspot (x, y, width, height):
                    action Jump("v12s7_mrlee")
    
    # Mr Lee
    else:
        imagemap:
            ground "images/v12/Scene 7/Screens/Navigation 27b.webp"
            insensitive "images/v12/Scene 7/Screens/Navigation 27b.webp"
            hover "images/v12/Scene 7/Screens/Navigation 27b_hover.webp"

            hotspot (x, y, width, height):
                    action Jump("v12s7_mrlee") # mr lee

    use v12s7_minimap(location="md_rear_gallery")


screen v12s7_right_gallery_back():
    tag freeRoam

    # Ryan and Imre
    if not v12s7_imre:
        imagemap:
            ground "images/v12/Scene 7/Screens/Navigation 16a.webp"
            insensitive "images/v12/Scene 7/Screens/Navigation 16a.webp"
            hover "images/v12/Scene 7/Screens/Navigation 16a_hover.webp"

            hotspot (x, y, width, height):
                    action Jump("v12s7_ryan_imre1") # Imre & Ryan

    # No one
    elif ryan in v12s7_killList:
        add "images/v12/Scene 7/Screens/Navigation 16c.webp"

    # Ryan
    else:
        imagemap:
            ground "images/v12/Scene 7/Screens/Navigation 16b.webp"
            insensitive "images/v12/Scene 7/Screens/Navigation 16b.webp"
            hover "images/v12/Scene 7/Screens/Navigation 16b_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_ryan:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferry1", returnScreen="v12s7_right_gallery_back", seenList=[ryan] if (v12s7_riley and not v12s7_riley2) or amber in v12s7_killList else [ryan, amber])
                else:
                    action Jump("v12s7_ryan1") # Ryan

    use v12s7_minimap(location="md_right_gallery")


screen v12s7_right_gallery_front():
    tag freeRoam

    # Riley and Amber
    if v12s7_riley and not v12s7_riley2 and amber not in v12s7_killList and riley not in v12s7_killList:
        add "images/v12/Scene 7/Screens/Navigation 17a.webp"

    # Riley
    elif v12s7_riley and not v12s7_riley2 and riley not in v12s7_killList:
        add "images/v12/Scene 7/Screens/Navigation 17b.webp"

    # Amber
    elif (not v12s7_riley and amber not in v12s7_killList) or (v12s7_riley and riley in v12s7_killList):
        add "images/v12/Scene 7/Screens/Navigation 17c.webp"

    # No one
    else:
        add "images/v12/Scene 7/Screens/Navigation 17d.webp"

    use v12s7_minimap(location="md_right_gallery")


screen v12s7_utility():
    tag freeRoam

    # Josh
    if v12s7_josh_moved and josh not in v12s7_killList:
        imagemap:
            ground "images/v12/Scene 7/Screens/Navigation 18a.webp"
            insensitive "images/v12/Scene 7/Screens/Navigation 18a.webp"
            hover "images/v12/Scene 7/Screens/Navigation 18a_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_josh:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferjos3", returnScreen="v12s7_utility", seenList=[])
                else:
                    action Jump("v12s7_josh2") # Josh

    # No one
    else:
        add "images/v12/Scene 7/Screens/Navigation 18b.webp"

    use v12s7_minimap(location="md_utility")


screen v12s7_front_gallery():
    tag freeRoam

    # Amber and Riley
    if v12s7_riley and not v12s7_riley2 and amber not in v12s7_killList and riley not in v12s7_killList:
        imagemap:
            ground "images/v12/Scene 7/Screens/Navigation 19a.webp"
            insensitive "images/v12/Scene 7/Screens/Navigation 19a.webp"
            hover "images/v12/Scene 7/Screens/Navigation 19a_hover.webp"

            hotspot (x, y, width, height):
                    action Jump("v12s7_riley2_amber") # Riley & Amber

    # Amber
    elif v12s7_riley and not v12s7_riley2 and riley not in v12s7_killList:
        imagemap:
            ground "images/v12/Scene 7/Screens/Navigation 19b.webp"
            insensitive "images/v12/Scene 7/Screens/Navigation 19b.webp"
            hover "images/v12/Scene 7/Screens/Navigation 19b_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_amber:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12feram1a", returnScreen="v12s7_front_gallery", seenList=[] if v12s7_imre else [imre, ryan])
                else:
                    action Jump("v12s7_amber1") # Amber

    # Riley
    elif (not v12s7_riley and amber not in v12s7_killList) or (v12s7_riley and riley in v12s7_killList):
        imagemap:
            ground "images/v12/Scene 7/Screens/Navigation 19c.webp"
            insensitive "images/v12/Scene 7/Screens/Navigation 19c.webp"
            hover "images/v12/Scene 7/Screens/Navigation 19c_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_riley2:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferrile1", returnScreen="v12s7_front_gallery", seenList=[])
                else:
                    action Jump("v12s7_riley2") # Riley

    # No one
    else:
        add "images/v12/Scene 7/Screens/Navigation 19d.webp"

    use v12s7_minimap(location="md_front_gallery")


screen v12s7_balcony_middle():
    tag freeRoam

    add "images/v12/Scene 7/Screens/Navigation 20a.webp"

    use v12s7_minimap(location="md_balcony")


screen v12s7_balcony_left():
    tag freeRoam

    # No one
    if nora in v12s7_killList:
        add "images/v12/Scene 7/Screens/Navigation 21b.webp"

    # Nora
    else:
        imagemap:
            ground "images/v12/Scene 7/Screens/Navigation 21a.webp"
            insensitive "images/v12/Scene 7/Screens/Navigation 21a.webp"
            hover "images/v12/Scene 7/Screens/Navigation 21a_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_nora:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12fernor1", returnScreen="v12s7_balcony_left", seenList=[] if v12s7_aubrey_moved else [riley])
                else:
                    action Jump("v12s7_nora1") # Nora

    use v12s7_minimap(location="md_balcony")


screen v12s7_balcony_right():
    tag freeRoam

    # No one
    if aubrey in v12s7_killList or v12s7_aubrey_moved:
        add "images/v12/Scene 7/Screens/Navigation 22b.webp"

    # Aubrey
    else:
        imagemap:
            ground "images/v12/Scene 7/Screens/Navigation 22a.webp"
            insensitive "images/v12/Scene 7/Screens/Navigation 22a.webp"
            hover "images/v12/Scene 7/Screens/Navigation 22a_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_aubrey:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferau1a", returnScreen="v12s7_balcony_right", seenList=[nora])
                else:
                    action Jump("v12s7_aubrey1") # Aubrey

    use v12s7_minimap(location="md_balcony")


screen v12s7_left_gallery_back():
    tag freeRoam

    # No one
    if aubrey in v12s7_killList or not v12s7_aubrey_moved:
        add "images/v12/Scene 7/Screens/Navigation 23b.webp"

    # Aubrey
    else:
        add "images/v12/Scene 7/Screens/Navigation 23a.webp"

    use v12s7_minimap(location="md_left_gallery")


screen v12s7_left_gallery_front():
    tag freeRoam

    # No one
    if aubrey in v12s7_killList or not v12s7_aubrey_moved:
        add "images/v12/Scene 7/Screens/Navigation 24b.webp"

    # Aubrey
    else:
        imagemap:
            add "images/v12/Scene 7/Screens/Navigation 24a.webp"

    use v12s7_minimap(location="md_left_gallery")


screen v12s7_bathroom():
    tag freeRoam

    # No one
    if aubrey in v12s7_killList or not v12s7_aubrey_moved:
        add "images/v12/Scene 7/Screens/Navigation 25b.webp"

    # Aubrey
    else:
        imagemap:
            ground "images/v12/Scene 7/Screens/Navigation 25a.webp"
            insensitive "images/v12/Scene 7/Screens/Navigation 25a.webp"
            hover "images/v12/Scene 7/Screens/Navigation 25a_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_aubrey2:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferauh1a", returnScreen="v12s7_bathroom", seenList=[])
                else:
                    action Jump("v12s7_aubrey2") # Aubrey

    use v12s7_minimap(location="md_bathroom")


screen v12s7_captains_room():
    tag freeRoam
    
    # Lindsey and Charli
    if not v12s7_lindsey_moved:
        imagemap:
            ground "images/v12/Scene 7/Screens/Navigation 26a.webp"
            insensitive "images/v12/Scene 7/Screens/Navigation 26a.webp"
            hover "images/v12/Scene 7/Screens/Navigation 26a_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_lindsey:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferlich1", returnScreen="v12s7_captains_room", seenList=[lindsey, charli])
                else:
                    action Jump("v12s7_lindsey_charlie1") # Lindsey & Charli

    # Charli
    elif charli in v12s7_killList:
        imagemap:
            ground "images/v12/Scene 7/Screens/Navigation 26c.webp"
            insensitive "images/v12/Scene 7/Screens/Navigation 26c.webp"
            hover "images/v12/Scene 7/Screens/Navigation 26c_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_charli:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12fercha1", returnScreen="v12s7_captains_room", seenList=[])
                else:
                    action Jump("v12s7_charli2") # Charli
            
    # No one
    else:
        add "images/v12/Scene 7/Screens/Navigation 26b.webp"

    use v12s7_minimap(location="ud_captains_room")