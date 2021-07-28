screen murderButtonOverlay(character):
    tag freeRoam

    hbox:
        pos (10, 10)
        spacing 15

        if v12s7_seenList:
            add Transform("images/v12/Scene 7/gui/eye_open.png", size=(75, 75))
            text "This person can currently be seen by someone else" yalign 0.5
        else:
            add Transform("images/v12/Scene 7/gui/eye_closed.png", size=(75, 75))

    imagebutton:
        align (0.97, 0.928)
        idle Transform("images/v12/Scene 7/gui/gun.png", size=(100, 100))
        hover Transform("images/v12/Scene 7/gui/gun_hover.png", size=(100, 100))
        if v12s7_seenList:
            action Jump("MurderFail") # Check Label after transcribing review
        else:
            action [ Function(character.kill), Jump("MurderSuccess") ] # Check Label after transcribing review


screen v12s7_minimap(location):
    add Transform("images/v12/Scene 7/minimap/[location].webp", size=(300, 300)) pos (10, 10)


### Lower Floor
screen v12s7_seating_back():
    tag freeRoam

    # No one
    if (emily in v12s7_killList and lauren in v12s7_killList) or (v12s7_emily and lauren in v12s7_killList) or (lauren in v12s7_killList):
        add "images/v12/Scene 7/Navigation 1c.webp"

    # Lauren only
    elif (emily in v12s7_killList) or (emily in v12s7_killList and lauren not in v12s7_killList) or (not emily_europe):
        imagemap:
            ground "images/v12/Scene 7/Navigation 1a.webp"
            insensitive "images/v12/Scene 7/Navigation 1a.webp"
            hover "images/v12/Scene 7/Navigation 1a_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_lauren:
                    action Call("v12s7_free_roam_spoken", backgroundImg="", returnScreen="v12s7_seating_back", seenList=[])
                else:
                    action Jump("v12s7_lauren1") # Lauren

    # Lauren and Emily
    elif (emily_europe and not v12s7_emily and not emily in v12s7_killList and lauren not in v12s7_killList):
        imagemap:
            ground "images/v12/Scene 7/Navigation 1b.webp"
            insensitive "images/v12/Scene 7/Navigation 1b.webp"
            hover "images/v12/Scene 7/Navigation 1b_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_lauren:
                    action Call("v12s7_free_roam_spoken", backgroundImg="", returnScreen="v12s7_seating_back", seenList=[])
                else:
                    action Jump("v12s7_lauren1") # Lauren

            hotspot (x, y, width, height):
                if v12s7_emily:
                    action Jump("v12s7_emily1") # Emily
                else:
                    action Call("v12s7_free_roam_spoken", backgroundImg="", returnScreen="v12s7_seating_back", seenList=[])

    use v12s7_minimap(location="ld_bow")


screen v12s7_seating_front():
    tag freeRoam

    # No one
    if (v12s7_sam1 and ms_rose in v12s7_killList) or (ms_rose in v12s7_killList and not v11_invite_sam_europe):
        add "images/v12/Scene 7/Navigation 2c.webp"
    
    # Ms Rose
    elif (v12s7_sam1 and ms_rose not in v12s7_killList) or (not v11_invite_sam_europe and ms_rose not in v12s7_killList):
        imagemap:
            ground "images/v12/Scene 7/Navigation 2b.webp"
            insensitive "images/v12/Scene 7/Navigation 2b.webp"
            hover "images/v12/Scene 7/Navigation 2b_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_msrose:
                    action Call("v12s7_free_roam_spoken", backgroundImg="", returnScreen="v12s7_seating_front", seenList=[])
                else:
                    action Jump("v12s7_msrose1") # ms rose


    # Samantha and Ms Rose
    elif (v11_invite_sam_europe and not v12s7_sam1 and ms_rose not in v12s7_killList):
        imagemap:
            ground "images/v12/Scene 7/Navigation 2a.webp"
            insensitive "images/v12/Scene 7/Navigation 2a.webp"
            hover "images/v12/Scene 7/Navigation 2a_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_msrose:
                    action Call("v12s7_free_roam_spoken", backgroundImg="", returnScreen="v12s7_seating_front", seenList=[])
                else:
                    action Jump("v12s7_msrose1") # ms rose

            hotspot (x, y, width, height):
                if v12s7_samantha:
                    action Call("v12s7_free_roam_spoken", backgroundImg="", returnScreen="v12s7_seating_front", seenList=[])
                else:
                    action Jump("v12s7_sam_cameron") # sameron

    use v12s7_minimap(location="ld_seating")


screen v12s7_walkway():
    tag freeRoam

    add "images/v12/Scene 7/Navigation 3.webp"

    use v12s7_minimap(location="ld_walkway")


screen v12s7_right_walkway_middle():
    tag freeRoam

    add "images/v12/Scene 7/Navigation 4.webp"

    use v12s7_minimap(location="ld_right_walkway")


screen v12s7_left_walkway_middle():
    tag freeRoam

    add "images/v12/Scene 7/Navigation 5.webp"

    use v12s7_minimap(location="ld_left_walkway")
    

screen v12s7_left_walkway_back():
    tag freeRoam

    # No one
    if ms_rose in v12s7_killList: # ms rose dead
        add "images/v12/Scene 7/Navigation 6c.webp"
    
    # Ms Rose
    else:
        add "images/v12/Scene 7/Navigation 6b.webp"

    use v12s7_minimap(location="ld_left_walkway")

                    
screen v12s7_rear():
    tag freeRoam

    # Lindsey
    if v12s7_lindsey_moved and lindsey not in v12s7_killList:
        imagemap:
            ground "images/v12/Scene 7/Navigation 7a.webp"
            insensitive "images/v12/Scene 7/Navigation 7a.webp"
            hover "images/v12/Scene 7/Navigation 7a_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_lindsey:
                    action Call("v12s7_free_roam_spoken", backgroundImg="", returnScreen="v12s7_rear", seenList=[])
                else:
                    action Jump("v12s7_lindsey2") # lindsey

    # No one
    else:
        add "images/v12/Scene 7/Navigation 7b.webp"

    use v12s7_minimap(location="ld_rear")


screen v12s7_right_walkway_back():
    tag freeRoam

    # Samantha
    if (v12s7_samantha and samantha not in v12s7_killList):
        imagemap:
            ground "images/v12/Scene 7/Navigation 8a.webp"
            insensitive "images/v12/Scene 7/Navigation 8a.webp"
            hover "images/v12/Scene 7/Navigation 8a_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_samantha2:
                    action Call("v12s7_free_roam_spoken", backgroundImg="", returnScreen="v12s7_right_walkway_back", seenList=[])
                else:
                    action Jump("v12s7_sam2") #samantha

    else:
        add "images/v12/Scene 7/Navigation 8b.webp"

    use v12s7_minimap(location="ld_right_walkway")
    

screen v12s7_right_walkway_front():
    tag freeRoam

    add "images/v12/Scene 7/Navigation 9.webp"

    use v12s7_minimap(location="ld_right_walkway")


screen v12s7_kitchen():
    tag freeRoam

    # Chris and Emily
    if v12s7_emily and not emily in v12s7_killList and chris not in v12s7_killList:
        imagemap:
            ground "images/v12/Scene 7/Navigation 10a.webp"
            insensitive "images/v12/Scene 7/Navigation 10a.webp"
            hover "images/v12/Scene 7/Navigation 10a_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_chris:
                    action Call("v12s7_free_roam_spoken", backgroundImg="", returnScreen="v12s7_kitchen", seenList=[])
                else:
                    action Jump("v12s7_chris1") # chris
                
            
    # Emily
    elif v12s7_emily and emily not in v12s7_killList:
        add "images/v12/Scene 7/Navigation 10d.webp"

    # Chris
    elif chris not in v12s7_killList:
        imagemap:
            ground "images/v12/Scene 7/Navigation 10b.webp"
            insensitive "images/v12/Scene 7/Navigation 10b.webp"
            hover "images/v12/Scene 7/Navigation 10b_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_chris:
                    action Call("v12s7_free_roam_spoken", backgroundImg="", returnScreen="v12s7_kitchen", seenList=[])
                else:
                    action Jump("v12s7_chris1") # chris

    # No one
    else:
        add "images/v12/Scene 7/Navigation 10d.webp"

    use v12s7_minimap(location="ld_kitchen")


screen v12s7_bow():
    tag freeRoam

    # Emily
    if v12s7_emily and emily not in v12s7_killList:
        imagemap:
            ground "images/v12/Scene 7/Navigation 11a.webp"
            insensitive "images/v12/Scene 7/Navigation 11a.webp"
            hover "images/v12/Scene 7/Navigation 11a_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_chris:
                    action Call("v12s7_free_roam_spoken", backgroundImg="", returnScreen="v12s7_bow", seenList=[])
                else:
                    action Jump("v12s7_emily2") # emily
            
    else:
        add "images/v12/Scene 7/Navigation 11b.webp"

    use v12s7_minimap(location="ld_bow")


screen v12s7_left_walkway_front():
    tag freeRoam

    # Penelope
    if v11_pen_goes_europe and penelope not in v12s7_killList:
        imagemap:
            ground "images/v12/Scene 7/Navigation 12a.webp"
            insensitive "images/v12/Scene 7/Navigation 12a.webp"
            hover "images/v12/Scene 7/Navigation 12a_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_penelope:
                    action Call("v12s7_free_roam_spoken", backgroundImg="", returnScreen="v12s7_left_walkway_front", seenList=[])
                else:
                    action Jump("v12s7_penelope1") #penelope
            
    else:
        add "images/v12/Scene 7/Navigation 12b.webp"

    use v12s7_minimap(location="ld_left_walkway")


screen v12s7_foyer():
    tag freeRoam

    # Imre
    if v12s7_imre and imre not in v12s7_killList:
        imagemap:
            ground "images/v12/Scene 7/Navigation 13a.webp"
            insensitive "images/v12/Scene 7/Navigation 13a.webp"
            hover "images/v12/Scene 7/Navigation 13a_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_imre:
                    action Call("v12s7_free_roam_spoken", backgroundImg="", returnScreen="v12s7_foyer", seenList=[])
                else:
                    action Jump("v12s7_imre2") #imre
    else:
        add "images/v12/Scene 7/Navigation 13b.webp"

    use v12s7_minimap(location="ld_foyer")


# MIDDLE FLOOR
screen v12s7_left_viewpoint():
    tag freeRoam

    # Chloe and Riley
    if not v12s7_riley2 and riley not in v12s7_killList and chloe not in v12s7_killList:
        imagemap:
            ground "images/v12/Scene 7/Navigation 14a.webp"
            insensitive "images/v12/Scene 7/Navigation 14a.webp"
            hover "images/v12/Scene 7/Navigation 14a_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_riley:
                    action Call("v12s7_free_roam_spoken", backgroundImg="", returnScreen="v12s7_left_viewpoint", seenList=[])
                elif v12s7_riley2:
                    action Jump("v12s7_riley3") #Riley & Chloe
                else:
                    action Jump("v12s7_riley1") #Riley & Chloe
                    
    
    # Riley
    elif v12s7_riley2 and chloe in v12s7_killList and riley not in v12s7_killList:
        imagemap:
            ground "images/v12/Scene 7/Navigation 14b.webp"
            insensitive "images/v12/Scene 7/Navigation 14b.webp"
            hover "images/v12/Scene 7/Navigation 14b_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_riley:
                    action Call("v12s7_free_roam_spoken", backgroundImg="", returnScreen="v12s7_left_viewpoint", seenList=[])
                else:
                    action Jump("v12s7_riley3a") # riley

    # Chloe
    elif v12s7_riley1 and chloe not in v12s7_killList:
        imagemap:
            ground "images/v12/Scene 7/Navigation 14c.webp"
            insensitive "images/v12/Scene 7/Navigation 14c.webp"
            hover "images/v12/Scene 7/Navigation 14c_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_chloe:
                    action Call("v12s7_free_roam_spoken", backgroundImg="", returnScreen="v12s7_left_viewpoint", seenList=[])
                else:
                    action Jump("v12s7_chloe1") # chloe

    # No one
    else:
        add "images/v12/Scene 7/Navigation 14d.webp"

    use v12s7_minimap(location="md_left_viewport")


screen v12s7_right_viewpoint():
    tag freeRoam

    # Josh
    if not v12s7_josh_moved and josh not in v12s7_killList:
        imagemap:
            ground "images/v12/Scene 7/Navigation 15a.webp"
            insensitive "images/v12/Scene 7/Navigation 15a.webp"
            hover "images/v12/Scene 7/Navigation 15a_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_josh:
                    action Call("v12s7_free_roam_spoken", backgroundImg="", returnScreen="v12s7_right_viewpoint", seenList=[])
                else:
                    action Jump("v12s7_josh1") # josh

    # No one
    else:
        add "images/v12/Scene 7/Navigation 15b.webp"

    use v12s7_minimap(location="md_right_viewport")


screen v12s7_rear_gallery():
    tag freeRoam

    # Mr Lee and Cameron
    if v11_invite_sam_europe and v12s7_samantha:
        imagemap:
            ground "images/v12/Scene 7/Navigation 27a.webp"
            insensitive "images/v12/Scene 7/Navigation 27a.webp"
            hover "images/v12/Scene 7/Navigation 27a_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_cameron:
                    action Call("v12s7_free_roam_spoken", backgroundImg="", returnScreen="v12s7_rear_gallery", seenList=[])
                else:
                    action Jump("v12s7_cameron2")
                    
            hotspot (x, y, width, height):
                if v12s7_mrlee:
                    action Call("v12s7_free_roam_spoken", backgroundImg="", returnScreen="v12s7_rear_gallery", seenList=[])
                else:
                    action Jump("v12s7_mrlee")
    
    # Mr Lee
    else:
        imagemap:
            ground "images/v12/Scene 7/Navigation 27b.webp"
            insensitive "images/v12/Scene 7/Navigation 27b.webp"
            hover "images/v12/Scene 7/Navigation 27b_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_mrlee:
                    action Call("v12s7_free_roam_spoken", backgroundImg="", returnScreen="v12s7_rear_gallery", seenList=[])
                else:
                    action Jump("v12s7_mrlee") # mr lee

    use v12s7_minimap(location="md_rear_gallery")


screen v12s7_right_gallery_back():
    tag freeRoam

    # Ryan and Imre
    if not v12s7_imre:
        imagemap:
            ground "images/v12/Scene 7/Navigation 16a.webp"
            insensitive "images/v12/Scene 7/Navigation 16a.webp"
            hover "images/v12/Scene 7/Navigation 16a_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_imre:
                    action Call("v12s7_free_roam_spoken", backgroundImg="", returnScreen="v12s7_right_gallery_back", seenList=[])
                else:
                    action Jump("v12s7_ryan_imre1") # Imre & Ryan

    # No one
    elif ryan in v12s7_killList:
        add "images/v12/Scene 7/Navigation 16c.webp"

    # Ryan
    else:
        imagemap:
            ground "images/v12/Scene 7/Navigation 16b.webp"
            insensitive "images/v12/Scene 7/Navigation 16b.webp"
            hover "images/v12/Scene 7/Navigation 16b_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_ryan:
                    action Call("v12s7_free_roam_spoken", backgroundImg="", returnScreen="v12s7_right_gallery_back", seenList=[])
                else:
                    action Jump("v12s7_ryan1") # Ryan

    use v12s7_minimap(location="md_right_gallery")


screen v12s7_right_gallery_front():
    tag freeRoam

    # Riley and Amber
    if v12s7_riley1 and not v12s7_riley2 and amber not in v12s7_killList and riley not in v12s7_killList:
        add "images/v12/Scene 7/Navigation 17a.webp"

    # Riley
    elif v12s7_riley1 and not v12s7_riley2 and riley not in v12s7_killList:
        add "images/v12/Scene 7/Navigation 17b.webp"

    # Amber
    elif (not v12s7_riley1 and amber not in v12s7_killList) or (v12s7_riley1 and riley in v12s7_killList):
        add "images/v12/Scene 7/Navigation 17c.webp"

    # No one
    else:
        add "images/v12/Scene 7/Navigation 17d.webp"

    use v12s7_minimap(location="md_right_gallery")


screen v12s7_utility():
    tag freeRoam

    # Josh
    if v12s7_josh_moved and josh not in v12s7_killList:
        imagemap:
            ground "images/v12/Scene 7/Navigation 18a.webp"
            insensitive "images/v12/Scene 7/Navigation 18a.webp"
            hover "images/v12/Scene 7/Navigation 18a_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_josh:
                    action Call("v12s7_free_roam_spoken", backgroundImg="", returnScreen="v12s7_utility", seenList=[])
                else:
                    action Jump("v12s7_josh2") # Josh

    # No one
    else:
        add "images/v12/Scene 7/Navigation 18b.webp"

    use v12s7_minimap(location="md_utility")


screen v12s7_front_gallery():
    tag freeRoam

    # Amber and Riley
    if v12s7_riley1 and not v12s7_riley2 and amber not in v12s7_killList and riley not in v12s7_killList:
        imagemap:
            ground "images/v12/Scene 7/Navigation 19a.webp"
            insensitive "images/v12/Scene 7/Navigation 19a.webp"
            hover "images/v12/Scene 7/Navigation 19a_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_riley2:
                    action Call("v12s7_free_roam_spoken", backgroundImg="", returnScreen="v12s7_front_gallery", seenList=[])
                else:
                    action Jump("v12s7_riley2_amber") # Riley & Amber

    # Amber
    elif v12s7_riley1 and not v12s7_riley2 and riley not in v12s7_killList:
        imagemap:
            ground "images/v12/Scene 7/Navigation 19b.webp"
            insensitive "images/v12/Scene 7/Navigation 19b.webp"
            hover "images/v12/Scene 7/Navigation 19b_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_amber:
                    action Call("v12s7_free_roam_spoken", backgroundImg="", returnScreen="v12s7_front_gallery", seenList=[])
                else:
                    action Jump("v12s7_amber1") # Amber

    # Riley
    elif (not v12s7_riley1 and amber not in v12s7_killList) or (v12s7_riley1 and riley in v12s7_killList):
        imagemap:
            ground "images/v12/Scene 7/Navigation 19c.webp"
            insensitive "images/v12/Scene 7/Navigation 19c.webp"
            hover "images/v12/Scene 7/Navigation 19c_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_riley2:
                    action Call("v12s7_free_roam_spoken", backgroundImg="", returnScreen="v12s7_front_gallery", seenList=[])
                else:
                    action Jump("v12s7_riley2") # Riley

    # No one
    else:
        add "images/v12/Scene 7/Navigation 19d.webp"

    use v12s7_minimap(location="md_front_gallery")


screen v12s7_balcony_middle():
    tag freeRoam

    add "images/v12/Scene 7/Navigation 20a.webp"

    use v12s7_minimap(location="md_balcony")


screen v12s7_balcony_left():
    tag freeRoam

    # No one
    if nora in v12s7_killList:
        add "images/v12/Scene 7/Navigation 21b.webp"

    # Nora
    else:
        imagemap:
            ground "images/v12/Scene 7/Navigation 21a.webp"
            insensitive "images/v12/Scene 7/Navigation 21a.webp"
            hover "images/v12/Scene 7/Navigation 21a_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_nora:
                    action Call("v12s7_free_roam_spoken", backgroundImg="", returnScreen="v12s7_balcony_left", seenList=[])
                else:
                    action Jump("v12s7_nora1") # Nora

    use v12s7_minimap(location="md_balcony")


screen v12s7_balcony_right():
    tag freeRoam

    # No one
    if aubrey in v12s7_killList or v12s7_aubrey_moved:
        add "images/v12/Scene 7/Navigation 22b.webp"

    # Aubrey
    else:
        imagemap:
            ground "images/v12/Scene 7/Navigation 22a.webp"
            insensitive "images/v12/Scene 7/Navigation 22a.webp"
            hover "images/v12/Scene 7/Navigation 22a_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_aubrey:
                    action Call("v12s7_free_roam_spoken", backgroundImg="", returnScreen="v12s7_balcony_right", seenList=[])
                else:
                    action Jump("v12s7_aubrey1") # Aubrey

    use v12s7_minimap(location="md_balcony")


screen v12s7_left_gallery_back():
    tag freeRoam

    # No one
    if aubrey in v12s7_killList or not v12s7_aubrey_moved:
        add "images/v12/Scene 7/Navigation 23b.webp"

    # Aubrey
    else:
        add "images/v12/Scene 7/Navigation 23a.webp"

    use v12s7_minimap(location="md_left_gallery")


screen v12s7_left_gallery_front():
    tag freeRoam

    # No one
    if aubrey in v12s7_killList or not v12s7_aubrey_moved:
        add "images/v12/Scene 7/Navigation 24b.webp"

    # Aubrey
    else:
        imagemap:
            add "images/v12/Scene 7/Navigation 24a.webp"

    use v12s7_minimap(location="md_left_gallery")


screen v12s7_bathroom():
    tag freeRoam

    # No one
    if aubrey in v12s7_killList or not v12s7_aubrey_moved:
        add "images/v12/Scene 7/Navigation 25b.webp"

    # Aubrey
    else:
        imagemap:
            ground "images/v12/Scene 7/Navigation 25a.webp"
            insensitive "images/v12/Scene 7/Navigation 25a.webp"
            hover "images/v12/Scene 7/Navigation 25a_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_aubrey2:
                    action Call("v12s7_free_roam_spoken", backgroundImg="", returnScreen="v12s7_bathroom", seenList=[])
                else:
                    action Jump("v12s7_aubrey2") # Aubrey

    use v12s7_minimap(location="md_bathroom")


screen v12s7_captains_room():
    tag freeRoam
    
    # Lindsey and Charli
    if not v12s7_lindsey_moved:
        imagemap:
            ground "images/v12/Scene 7/Navigation 26a.webp"
            insensitive "images/v12/Scene 7/Navigation 26a.webp"
            hover "images/v12/Scene 7/Navigation 26a_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_lindsey:
                    action Call("v12s7_free_roam_spoken", backgroundImg="", returnScreen="v12s7_captains_room", seenList=[])
                else:
                    action Jump("v12s7_lindsey_charlie1") # Lindsey & Charli

    # Charli
    elif charli in v12s7_killList:
        imagemap:
            ground "images/v12/Scene 7/Navigation 26c.webp"
            insensitive "images/v12/Scene 7/Navigation 26c.webp"
            hover "images/v12/Scene 7/Navigation 26c_hover.webp"

            hotspot (x, y, width, height):
                if v12s7_charli:
                    action Call("v12s7_free_roam_spoken", backgroundImg="", returnScreen="v12s7_captains_room", seenList=[])
                else:
                    action Jump("v12s7_charli2") # Charli
            
    # No one
    else:
        add "images/v12/Scene 7/Navigation 26b.webp"

    use v12s7_minimap(location="ud_captains_room")