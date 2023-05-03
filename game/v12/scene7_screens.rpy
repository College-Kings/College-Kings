init python:
    def v12s7_kill(char_obj: NonPlayableCharacter):
        # Check Competitive stat
        if char_obj.is_competitive and len(v12s7_killList) < 3:
            char_obj.points -= 1
        elif not char_obj.is_competitive and len(v12s7_killList) < 3:
            char_obj.points += 1

        # Check Vindictive stat
        for character in char_obj.vindictive_characters:
            if character in v12s7_killList:
                char_obj.points += 1
            else:
                char_obj.points -= 1

        # Check Talkative stat
        if char_obj.is_talkative and char_obj in v12s7_endtalkList:
            char_obj.points += 1
        elif char_obj.is_talkative:
            char_obj.points -= 1
        elif not char_obj.is_talkative and char_obj in v12s7_endtalkList:
            char_obj.points -= 1

        # Add character to kill list
        if char_obj != cameron:  # Except Cameron, because he's not playing
            v12s7_killList.add(char_obj)


screen murder_button_overlay(character):
    tag free_roam

    $ char_name = character.name.replace(' ', '_').lower()

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
            action Jump("v12s7_mc_caught")
        else:
            if char_name == "riley" and "riley2" in freeroam9 and not "riley3" in freeroam9:
                action [Function(v12s7_kill, character), Jump("v12s7_{}_kill2".format(char_name)) ]
            else:
                action [Function(v12s7_kill, character), Jump("v12s7_{}_kill".format(char_name)) ]

    if config_debug:
        timer 0.1 repeat True:
            if not v12s7_seenList:
                if char_name == "riley" and "riley2" in freeroam9 and not "riley3" in freeroam9:
                    action [Function(v12s7_kill, character), Jump("v12s7_{}_kill2".format(char_name)) ]
                else:
                    action [Function(v12s7_kill, character), Jump("v12s7_{}_kill".format(char_name)) ]


screen v12s7_minimap(location):
    add Transform("images/v12/Scene 7/minimap/{}.webp".format(location), zoom=0.25)


### Lower Floor
screen v12s7_seating_back():
    tag free_roam

    if (emily_europe and not "emily" in freeroam9 and not emily in v12s7_killList and lauren not in v12s7_killList): #Emily and Lauren
        imagemap:
            idle "images/v12/Scene 7/Screens/Navigation 1b.webp"
            hover "images/v12/Scene 7/Buttons/nav 1.webp"

            hotspot (1318, 182, 421, 605):
                if "lauren" in freeroam9:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferla1", returnScreen="v12s7_seating_back", seenList=[emily], victim=lauren)
                else:
                    action Jump("v12s7_lauren1") # Lauren

            hotspot (180, 182, 380, 605) action Jump("v12s7_emily1") # Emily

            hotspot (331, 898, 1227, 181) action Show("v12s7_seating_front")


    elif (emily_europe and not "emily" in freeroam9 and not emily in v12s7_killList and lauren in v12s7_killList): #Emily only
        imagemap:
            idle "images/v12/Scene 7/Screens/Navigation 1d.webp"
            hover "images/v12/Scene 7/Buttons/nav 1.webp"

            hotspot (180, 182, 380, 605) action Jump("v12s7_emily1") # Emily

            hotspot (331, 898, 1227, 181) action Show("v12s7_seating_front")

    elif lauren not in v12s7_killList: #Lauren only
        imagemap:
            idle "images/v12/Scene 7/Screens/Navigation 1a.webp"
            hover "images/v12/Scene 7/Buttons/nav 1.webp"

            hotspot (1318, 182, 421, 605):
                if "lauren" in freeroam9:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferla1", returnScreen="v12s7_seating_back", seenList=[], victim=lauren)
                else:
                    action Jump("v12s7_lauren1") # Lauren

            hotspot (331, 898, 1227, 181) action Show("v12s7_seating_front")

    else:
        imagemap:
            idle "images/v12/Scene 7/Screens/Navigation 1c.webp"
            hover "images/v12/Scene 7/Buttons/nav 1.webp"

            hotspot (331, 898, 1227, 181) action Show("v12s7_seating_front")

    use v12s7_minimap(location="ld_seating")

    on "replaced" action SetVariable("previous_location", "v12s7_seating_back")

    if config_debug:
        python:
            actions = []

            if (emily_europe and not "emily" in freeroam9 and not emily in v12s7_killList and lauren not in v12s7_killList): #Emily and Lauren
                if "lauren" not in freeroam9:
                    actions.append(Jump("v12s7_lauren1")) # Lauren

                actions.append(Jump("v12s7_emily1")) # Emily

                actions.append(Show("v12s7_seating_front"))


            elif (emily_europe and not "emily" in freeroam9 and not emily in v12s7_killList and lauren in v12s7_killList): #Emily only
                actions.append(Jump("v12s7_emily1")) # Emily

                actions.append(Show("v12s7_seating_front"))

            elif lauren not in v12s7_killList: #Lauren only
                if "lauren" not in freeroam9:
                    actions.append(Jump("v12s7_lauren1")) # Lauren

                actions.append(Show("v12s7_seating_front"))

            else:
                actions.append(Show("v12s7_seating_front"))

        timer 0.1 action renpy.random.choice(actions)


screen v12s7_seating_front():
    tag free_roam

    # No one
    if ("samantha" in freeroam9 and ms_rose in v12s7_killList) or (ms_rose in v12s7_killList and not v11_invite_sam_europe):
        imagemap:
            idle "images/v12/Scene 7/Screens/Navigation 2c.webp"
            hover "images/v12/Scene 7/Buttons/nav 2.webp"

            hotspot (367, 0, 1205, 140) action Show("v12s7_seating_back")
            hotspot (327, 917, 1216, 163) action Show("v12s7_walkway")
    
    # Ms Rose
    elif ("samantha" in freeroam9 and ms_rose not in v12s7_killList) or (not v11_invite_sam_europe and ms_rose not in v12s7_killList):
        imagemap:
            idle "images/v12/Scene 7/Screens/Navigation 2b.webp"
            hover "images/v12/Scene 7/Buttons/nav 2.webp"

            hotspot (1585, 7, 335, 631):
                if "rose" in freeroam9:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12fermsr1a", returnScreen="v12s7_seating_front", seenList=[], victim=ms_rose)
                else:
                    action Jump("v12s7_msrose1") # ms rose

            hotspot (367, 0, 1205, 140) action Show("v12s7_seating_back")
            hotspot (327, 917, 1216, 163) action Show("v12s7_walkway")

    # Samantha and Ms Rose
    elif (v11_invite_sam_europe and not "samantha" in freeroam9 and ms_rose not in v12s7_killList):
        imagemap:
            idle "images/v12/Scene 7/Screens/Navigation 2a.webp"
            hover "images/v12/Scene 7/Buttons/nav 2.webp"

            hotspot (1585, 7, 335, 631):
                if "rose" in freeroam9:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12fermsr1a", returnScreen="v12s7_seating_front", seenList=[samantha], victim=ms_rose)
                else:
                    action Jump("v12s7_msrose1") # ms rose

            hotspot (23, 0, 344, 627) action Jump("v12s7_sam_cameron") # sameron

            hotspot (367, 0, 1205, 140) action Show("v12s7_seating_back")
            hotspot (327, 917, 1216, 163) action Show("v12s7_walkway")

    use v12s7_minimap(location="ld_seating")

    on "replaced" action SetVariable("previous_location", "v12s7_seating_front")

    if config_debug:
        python:
            actions = []

            # No one
            if ("samantha" in freeroam9 and ms_rose in v12s7_killList) or (ms_rose in v12s7_killList and not v11_invite_sam_europe):
                actions.append(Show("v12s7_seating_back"))
                actions.append(Show("v12s7_walkway"))
            
            # Ms Rose
            elif ("samantha" in freeroam9 and ms_rose not in v12s7_killList) or (not v11_invite_sam_europe and ms_rose not in v12s7_killList):
                if "rose" not in freeroam9:
                    actions.append(Jump("v12s7_msrose1")) # ms rose

                actions.append(Show("v12s7_seating_back"))
                actions.append(Show("v12s7_walkway"))

            # Samantha and Ms Rose
            elif (v11_invite_sam_europe and not "samantha" in freeroam9 and ms_rose not in v12s7_killList):
                if "rose" not in freeroam9:
                    actions.append(Jump("v12s7_msrose1")) # ms rose

                actions.append(Jump("v12s7_sam_cameron")) # sameron

                actions.append(Show("v12s7_seating_back"))
                actions.append(Show("v12s7_walkway"))

        timer 0.1 action renpy.random.choice(actions)


screen v12s7_walkway():
    tag free_roam

    imagemap:
        idle "images/v12/Scene 7/Screens/Navigation 3.webp"
        hover "images/v12/Scene 7/Buttons/nav 3.webp"

        hotspot (0, 30, 126, 1020) action Show("v12s7_left_walkway_middle")
        hotspot (1793, 30, 126, 1020) action Show("v12s7_right_walkway_middle")
        hotspot (242, 950, 1385, 130) action Show("v12s7_seating_front")

    use v12s7_minimap(location="ld_walkway")

    on "replaced" action SetVariable("previous_location", "v12s7_walkway")

    if config_debug:
        timer 0.1 action Show(renpy.random.choice(("v12s7_left_walkway_middle", "v12s7_right_walkway_middle", "v12s7_seating_front")))


screen v12s7_right_walkway_middle():
    tag free_roam

    imagemap:
        idle "images/v12/Scene 7/Screens/Navigation 4.webp"
        hover "images/v12/Scene 7/Buttons/nav 4.webp"

        hotspot (84, 26, 186, 944) action Show("v12s7_right_walkway_front")
        hotspot (1516, 12, 186, 955) action Show("v12s7_right_walkway_back")
        hotspot (306, 928, 1231, 152) action Show("v12s7_walkway")

    use v12s7_minimap(location="ld_right_walkway")

    on "replaced" action SetVariable("previous_location", "v12s7_right_walkway_middle")

    if config_debug:
        timer 0.1 action Show(renpy.random.choice(("v12s7_right_walkway_front", "v12s7_right_walkway_back", "v12s7_walkway")))


screen v12s7_left_walkway_middle():
    tag free_roam

    imagemap:
        idle "images/v12/Scene 7/Screens/Navigation 5.webp"
        hover "images/v12/Scene 7/Buttons/nav 5.webp"

        hotspot (286, 0, 189, 892) action Show("v12s7_left_walkway_back")
        hotspot (1610, 0, 182, 959) action Show("v12s7_left_walkway_front")
        hotspot (306, 928, 1231, 152) action Show("v12s7_walkway")


    use v12s7_minimap(location="ld_left_walkway")
    
    on "replaced" action SetVariable("previous_location", "v12s7_left_walkway_middle")

    if config_debug:
        timer 0.1 action Show(renpy.random.choice(("v12s7_left_walkway_back", "v12s7_left_walkway_front", "v12s7_walkway")))


screen v12s7_left_walkway_back():
    tag free_roam

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

    if config_debug:
        timer 0.1 action Show(renpy.random.choice(("v12s7_rear", "v12s7_left_walkway_middle")))


screen v12s7_rear():
    tag free_roam

    imagemap:
        if v12s7_lindsey_moved and lindsey not in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 7a.webp" # Lindsey
        else:
            idle "images/v12/Scene 7/Screens/Navigation 7b.webp" # No one
        hover "images/v12/Scene 7/Buttons/nav 7.webp"

        if v12s7_lindsey_moved and lindsey not in v12s7_killList:
            hotspot (563, 303, 565, 664):
                if "lindsey2" in freeroam9:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferli3", returnScreen="v12s7_rear", seenList=[], victim=lindsey)
                else:
                    action Jump("v12s7_lindsey2") # lindsey
  
        hotspot (338, 984, 1200, 96) action Show("v12s7_right_walkway_back")
        hotspot (293, 0, 1385, 130) action Show("v12s7_left_walkway_back")

    use v12s7_minimap(location="ld_rear")

    on "replaced" action SetVariable("previous_location", "v12s7_rear")

    if config_debug:
        python:
            actions = []

            if "lindsey2" not in freeroam9:
                actions.append(Jump("v12s7_lindsey2"))
            
            actions.append(Show("v12s7_right_walkway_back"))
            actions.append(Show("v12s7_left_walkway_back"))

        timer 0.1 action renpy.random.choice(actions)


screen v12s7_right_walkway_back():
    tag free_roam

    imagemap:
        if ("samantha" in freeroam9 and samantha not in v12s7_killList):
            idle "images/v12/Scene 7/Screens/Navigation 8a.webp"
        else:
            idle "images/v12/Scene 7/Screens/Navigation 8b.webp"
        hover "images/v12/Scene 7/Buttons/nav 8.webp"

        if ("samantha" in freeroam9 and samantha not in v12s7_killList):
            hotspot (813, 237, 211, 508):
                if "samantha2" in freeroam9:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12fersam1", returnScreen="v12s7_right_walkway_back", seenList=[], victim=samantha)
                else:
                    action Jump("v12s7_sam2") #samantha

        hotspot (286, 889, 1348, 191) action Show("v12s7_right_walkway_middle")
        hotspot (286, 0, 1348, 191) action Show("v12s7_rear")

    use v12s7_minimap(location="ld_right_walkway")
    
    on "replaced" action SetVariable("previous_location", "v12s7_right_walkway_back")

    if config_debug:
        python:
            actions = []

            if "samantha2" not in freeroam9:
                actions.append(Jump("v12s7_sam2"))
            
            actions.append(Show("v12s7_right_walkway_middle"))
            actions.append(Show("v12s7_rear"))

        timer 0.1 action renpy.random.choice(actions)


screen v12s7_right_walkway_front():
    tag free_roam

    imagemap:
        idle "images/v12/Scene 7/Screens/Navigation 9.webp"
        hover "images/v12/Scene 7/Buttons/nav 9.webp"

        hotspot (304, 94, 104, 735) action Show("v12s7_rear_gallery")
        hotspot (747, 186, 310, 521) action Show("v12s7_kitchen")
        hotspot (345, 967, 1193, 113) action Show("v12s7_right_walkway_middle")

    use v12s7_minimap(location="ld_right_walkway")

    on "replaced" action SetVariable("previous_location", "v12s7_right_walkway_front")

    if config_debug:
        timer 0.1 action Show(renpy.random.choice(("v12s7_rear_gallery", "v12s7_kitchen", "v12s7_right_walkway_middle")))


screen v12s7_kitchen():
    tag free_roam

    imagemap:
        if "emily" in freeroam9 and not emily in v12s7_killList and not chris in v12s7_killList: # Chris and Emily
            idle "images/v12/Scene 7/Screens/Navigation 10a.webp" 
            hover "images/v12/Scene 7/Buttons/nav 10.webp"
            
        elif "emily" in freeroam9 and not emily in v12s7_killList and chris in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 10d.webp" # Emily
            hover "images/v12/Scene 7/Buttons/nav 10.webp"

        elif chris not in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 10b.webp" # Chris
            hover "images/v12/Scene 7/Buttons/nav 10mock.webp"

        else:
            idle "images/v12/Scene 7/Screens/Navigation 10c.webp"
            hover "images/v12/Scene 7/Buttons/nav 10mock.webp"

        if chris not in v12s7_killList:
            hotspot (1116, 33, 751, 1047):
                if "chris" in freeroam9 and "emily" in freeroam9 and emily not in v12s7_killList:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferchr1", returnScreen="v12s7_kitchen", seenList=[], victim=chris)
                elif "chris" in freeroam9:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferchrnoem1", returnScreen="v12s7_kitchen", seenList=[], victim=chris)
                else:
                    action Jump("v12s7_chris1") # chris

        hotspot (541, 206, 396, 591) action Show("v12s7_bow")
        hotspot (339, 983, 1198, 97) action Show("v12s7_right_walkway_front")

    use v12s7_minimap(location="ld_kitchen")

    on "replaced" action SetVariable("previous_location", "v12s7_kitchen")

    if config_debug:
        python:
            actions = []

            if "chris" not in freeroam9 and "emily" not in freeroam9 and emily in v12s7_killList:
                actions.append(Jump("v12s7_chris1"))
            
            actions.append(Show("v12s7_bow"))
            actions.append(Show("v12s7_right_walkway_front"))

        timer 0.1 action renpy.random.choice(actions)


screen v12s7_bow():
    tag free_roam

    imagemap:
        if "emily" in freeroam9 and emily not in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 11a.webp" # Emily
            hover "images/v12/Scene 7/Buttons/nav 11.webp"
        else:
            idle "images/v12/Scene 7/Screens/Navigation 11b.webp"
            hover "images/v12/Scene 7/Buttons/nav 11b.webp"

        if "emily" in freeroam9 and emily not in v12s7_killList:
            hotspot (920, 216, 368, 864):
                if "emily2" in freeroam9:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12feremi1", returnScreen="v12s7_bow", seenList=[], victim=emily)
                else:
                    action Jump("v12s7_emily2") # emily

        hotspot (339, 983, 1198, 97) action Show("v12s7_kitchen")
        hotspot (0, 30, 126, 1020) action Show("v12s7_foyer")

    use v12s7_minimap(location="ld_bow")

    on "replaced" action SetVariable("previous_location", "v12s7_bow")

    if config_debug:
        python:
            actions = []

            if "emily2" not in freeroam9:
                actions.append(Jump("v12s7_emily2"))
            
            actions.append(Show("v12s7_kitchen"))
            actions.append(Show("v12s7_foyer"))

        timer 0.1 action renpy.random.choice(actions)


screen v12s7_left_walkway_front():
    tag free_roam

    imagemap:
        if v11_pen_goes_europe and penelope not in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 12a.webp" # Penelope
        else:
            idle "images/v12/Scene 7/Screens/Navigation 12b.webp"
        hover "images/v12/Scene 7/Buttons/nav 12.webp"

        if v11_pen_goes_europe and penelope not in v12s7_killList:
            hotspot (223, 326, 752, 656):
                if "penelope" in freeroam9:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferpen1", returnScreen="v12s7_left_walkway_front", seenList=[], victim=penelope)
                else:
                    action Jump("v12s7_penelope1") #penelope
        
        hotspot (1003, 288, 251, 492) action Show("v12s7_foyer")
        hotspot (1693, 73, 140, 787) action Show("v12s7_rear_gallery")
        hotspot (353, 984, 1158, 96) action Show("v12s7_left_walkway_middle")

    use v12s7_minimap(location="ld_left_walkway")

    on "replaced" action SetVariable("previous_location", "v12s7_left_walkway_front")

    if config_debug:
        python:
            actions = []

            if "penelope" not in freeroam9:
                actions.append(Jump("v12s7_penelope1"))
            
            actions.append(Show("v12s7_foyer"))
            actions.append(Show("v12s7_rear_gallery"))
            actions.append(Show("v12s7_left_walkway_middle"))

        timer 0.1 action renpy.random.choice(actions)


screen v12s7_foyer():
    tag free_roam

    imagemap:
        if "imre" in freeroam9 and imre not in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 13a.webp" # Imre
        else:
            idle "images/v12/Scene 7/Screens/Navigation 13b.webp"
        hover "images/v12/Scene 7/Buttons/nav 13.webp"

        if "imre" in freeroam9 and imre not in v12s7_killList:
            hotspot (821, 493, 492, 490):
                if "imre2" in freeroam9:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferim1", returnScreen="v12s7_foyer", seenList=[], victim=imre)
                else:
                    action Jump("v12s7_imre2") #imre

        hotspot (339, 983, 1198, 97) action Show("v12s7_left_walkway_front")
        hotspot (1423, 66, 497, 796) action Show("v12s7_bow")

    use v12s7_minimap(location="ld_foyer")

    on "replaced" action SetVariable("previous_location", "v12s7_foyer")

    if config_debug:
        python:
            actions = []

            if "imre2" not in freeroam9:
                actions.append(Jump("v12s7_imre2"))
            
            actions.append(Show("v12s7_left_walkway_front"))
            actions.append(Show("v12s7_bow"))

        timer 0.1 action renpy.random.choice(actions)


# MIDDLE FLOOR
screen v12s7_left_viewpoint():
    tag free_roam

    imagemap:
        if riley not in v12s7_killList and chloe not in v12s7_killList and ("riley2" in freeroam9 or not v12s7_riley_moved):
            idle "images/v12/Scene 7/Screens/Navigation 14a.webp" # Chloe and Riley
            hover "images/v12/Scene 7/Buttons/nav 14a.webp" # Chloe and Riley
            hotspot (685, 117, 540, 786):
                if "riley3" in freeroam9:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferric1", returnScreen="v12s7_left_viewpoint", seenList=[chloe, josh] if josh_europe and not ("josh" in freeroam9) else [chloe], victim=riley)
                elif "riley2" in freeroam9:
                    action Jump("v12s7_riley3") #Riley & Chloe
                else:
                    action Jump("v12s7_riley1") #Riley & Chloe
    
        elif chloe in v12s7_killList and riley not in v12s7_killList and ("riley2" in freeroam9 or not v12s7_riley_moved):
            idle "images/v12/Scene 7/Screens/Navigation 14b.webp" # Riley
            hover "images/v12/Scene 7/Buttons/nav 14b.webp" # Riley
            hotspot (835, 191, 361, 772):
                if "riley3" in freeroam9:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferril1", returnScreen="v12s7_left_viewpoint", seenList=[josh] if josh_europe and not ("josh" in freeroam9) else [], victim=riley)
                else:
                    action Jump("v12s7_riley3a") # riley

        elif chloe not in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 14c.webp" # Chloe
            hover "images/v12/Scene 7/Buttons/nav 14c.webp" # Chloe
            hotspot (689, 203, 271, 673):
                if "chloe" in freeroam9:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferch1", returnScreen="v12s7_left_viewpoint", seenList=[josh] if josh_europe and not ("josh" in freeroam9) else [], victim=chloe)
                else:
                    action Jump("v12s7_chloe1") # chloe

        else:
            idle "images/v12/Scene 7/Screens/Navigation 14d.webp" # No one
            hover "images/v12/Scene 7/Buttons/nav 14d.webp" # No one

        hotspot (608, 288, 86, 302) action Show("v12s7_right_viewpoint")
        hotspot (338, 976, 1200, 104) action Show("v12s7_rear_gallery")

    use v12s7_minimap(location="md_left_viewpoint")

    on "replaced" action SetVariable("previous_location", "v12s7_left_viewpoint")

    if config_debug:
        python:
            actions = []

            if riley not in v12s7_killList and chloe not in v12s7_killList and ("riley2" in freeroam9 or not v12s7_riley_moved):
                if "riley2" in freeroam9 and not "riley3" in freeroam9:
                    actions.append(Jump("v12s7_riley3")) #Riley & Chloe
                if "riley2" not in freeroam9:
                    actions.append(Jump("v12s7_riley1")) #Riley & Chloe
        
            elif chloe in v12s7_killList and riley not in v12s7_killList and ("riley2" in freeroam9 or not v12s7_riley_moved):
                if "riley3" not in freeroam9:
                    actions.append(Jump("v12s7_riley3a")) # riley

            elif chloe not in v12s7_killList:
                if "chloe" not in freeroam9:
                    actions.append(Jump("v12s7_chloe1")) # chloe
            
            actions.append(Show("v12s7_right_viewpoint"))
            actions.append(Show("v12s7_rear_gallery"))

        timer 0.1 action renpy.random.choice(actions)


screen v12s7_right_viewpoint():
    tag free_roam

    imagemap:
        if josh_europe and not "josh" in freeroam9 and josh not in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 15a.webp" # Josh
        else:
            idle "images/v12/Scene 7/Screens/Navigation 15b.webp" # No one
        hover "images/v12/Scene 7/Buttons/nav 15.webp"

        if josh_europe and not "josh" in freeroam9 and josh not in v12s7_killList:
            hotspot (729, 375, 451, 545):
                if "josh" in freeroam9:
                    if ((not v12s7_riley_moved or "riley2" in freeroam9) and riley not in v12s7_killList) and (chloe not in v12s7_killList):
                        action Call("v12s7_free_roam_spoken", backgroundImg="v12ferjo1", returnScreen="v12s7_right_viewpoint", seenList=[riley, chloe], victim=josh)
                    elif (not v12s7_riley_moved or "riley2" in freeroam9) and riley not in v12s7_killList:
                        action Call("v12s7_free_roam_spoken", backgroundImg="v12ferjo1", returnScreen="v12s7_right_viewpoint", seenList=[riley], victim=josh)
                    elif chloe not in v12s7_killList:
                        action Call("v12s7_free_roam_spoken", backgroundImg="v12ferjo1", returnScreen="v12s7_right_viewpoint", seenList=[chloe], victim=josh)
                    else:
                        action Call("v12s7_free_roam_spoken", backgroundImg="v12ferjo1", returnScreen="v12s7_right_viewpoint", seenList=[], victim=josh)
                else:
                    action Jump("v12s7_josh1") # josh

        hotspot (382, 972, 1106, 108) action Show("v12s7_rear_gallery")
        hotspot (1431, 300, 111, 313) action Show("v12s7_left_viewpoint")

    use v12s7_minimap(location="md_right_viewpoint")

    on "replaced" action SetVariable("previous_location", "v12s7_right_viewpoint")

    if config_debug:
        python:
            actions = []

            if josh_europe and not "josh" in freeroam9 and josh not in v12s7_killList:
                if "josh" not in freeroam9:
                    actions.append(Jump("v12s7_josh1")) # josh
            
            actions.append(Show("v12s7_rear_gallery"))
            actions.append(Show("v12s7_left_viewpoint"))

        timer 0.1 action renpy.random.choice(actions)


screen v12s7_rear_gallery():
    tag free_roam

    imagemap:
        if v11_invite_sam_europe and "samantha" in freeroam9:
            idle "images/v12/Scene 7/Screens/Navigation 27a.webp" # Mr Lee and Cameron
        else:
            idle "images/v12/Scene 7/Screens/Navigation 27b.webp" # Mr Lee
        hover "images/v12/Scene 7/Buttons/nav 27mock.webp"

        if v11_invite_sam_europe and "samantha" in freeroam9:
            hotspot (894, 267, 257, 744):
                if "cameron" in freeroam9:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12fercam3", returnScreen="v12s7_rear_gallery", seenList=[], victim=cameron)
                else:
                    action Jump("v12s7_cameron2")

        hotspot (172, 320, 239, 653):
            if len(v12s7_killList) >= v12s7_victims:
                action Show("confirm", message="Are you sure you want to end the free roam?", yes_action=[Hide("confirm"), Jump("v12_murder_mystery_reveal")])
            else:
                action Jump("v12s7_mrlee")
        
        if previous_location == "v12s7_left_walkway_front" or previous_location == "v12s7_right_walkway_front":
            hotspot (327, 1000, 1216, 80) action Show(previous_location)
        else:
            hotspot (327, 1000, 1216, 80) action Show("v12s7_right_walkway_front")

        hotspot (0, 30, 126, 1020) action Show("v12s7_left_viewpoint")
        hotspot (1793, 30, 126, 1020) action Show("v12s7_right_viewpoint")

        hotspot (391, 345, 251, 492) action Show("v12s7_left_gallery_back")
        hotspot (1224, 345, 251, 492) action Show("v12s7_right_gallery_back")


    use v12s7_minimap(location="md_rear_gallery")

    on "replaced" action SetVariable("previous_location", "v12s7_rear_gallery")

    if config_debug:
        python:
            actions = []

            if v11_invite_sam_europe and "samantha" in freeroam9:
                if "cameron" not in freeroam9:
                    actions.append(Jump("v12s7_cameron2"))

            if len(v12s7_killList) >= v12s7_victims:
                actions.append(Show("confirm", message="Are you sure you want to end the free roam?", yes_action=[Hide("confirm"), Jump("v12_murder_mystery_reveal")]))
            else:
                actions.append(Jump("v12s7_mrlee"))
            
            if previous_location == "v12s7_left_walkway_front" or previous_location == "v12s7_right_walkway_front":
                actions.append(Show(previous_location))
            else:
                actions.append(Show("v12s7_right_walkway_front"))

            actions.append(Show("v12s7_left_viewpoint"))
            actions.append(Show("v12s7_right_viewpoint"))

            actions.append(Show("v12s7_left_gallery_back"))
            actions.append(Show("v12s7_right_gallery_back"))

        timer 0.1 action renpy.random.choice(actions)


screen v12s7_right_gallery_back():
    tag free_roam

    imagemap:
        if not "imre" in freeroam9:
            idle "images/v12/Scene 7/Screens/Navigation 16a.webp" # Ryan and Imre
            hover "images/v12/Scene 7/Buttons/nav 16.webp"

            hotspot (679, 213, 461, 799):
                action Jump("v12s7_ryan_imre1") # Imre & Ryan

        elif ryan in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 16c.webp" # No one
            hover "images/v12/Scene 7/Buttons/nav 16b.webp"
            
        else:
            idle "images/v12/Scene 7/Screens/Navigation 16b.webp" # Ryan
            hover "images/v12/Scene 7/Buttons/nav 16b.webp"
            
            hotspot (932, 265, 240, 716):
                if "ryan" in freeroam9:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferry1", returnScreen="v12s7_right_gallery_back", seenList=[] if (v12s7_riley_moved and not "riley2" in freeroam9) or amber in v12s7_killList else [amber], victim=ryan)
                else:
                    action Jump("v12s7_ryan1") # Ryan

        hotspot (339, 1013, 1198, 67) action Show("v12s7_rear_gallery")
        hotspot (293, 0, 1385, 130) action Show("v12s7_right_gallery_front")
        
    use v12s7_minimap(location="md_right_gallery")

    on "replaced" action SetVariable("previous_location", "v12s7_right_gallery_back")

    if config_debug:
        python:
            actions = []

            if not "imre" in freeroam9:
                actions.append(Jump("v12s7_ryan_imre1")) # Imre & Ryan

            elif ryan not in v12s7_killList:
                if "ryan" not in freeroam9:
                    actions.append(Jump("v12s7_ryan1")) # Ryan
            
            actions.append(Show("v12s7_rear_gallery"))
            actions.append(Show("v12s7_right_gallery_front"))

        timer 0.1 action renpy.random.choice(actions)


screen v12s7_right_gallery_front():
    tag free_roam

    imagemap:
        if v12s7_riley_moved and not "riley2" in freeroam9 and amber not in v12s7_killList and riley not in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 17a.webp" # Riley and Amber
            hover "images/v12/Scene 7/Buttons/nav 17amock.webp"

            hotspot (757, 270, 316, 649) action Show("v12s7_front_gallery")

        elif v12s7_riley_moved and not "riley2" in freeroam9 and amber in v12s7_killList and riley not in v12s7_killList: # Riley
            idle "images/v12/Scene 7/Screens/Navigation 17b.webp" # Riley
            hover "images/v12/Scene 7/Buttons/nav 17bmock.webp"

            hotspot (758, 279, 223, 640) action Show("v12s7_front_gallery")

        elif amber not in v12s7_killList: # Amber
            idle "images/v12/Scene 7/Screens/Navigation 17c.webp" # Amber
            hover "images/v12/Scene 7/Buttons/nav 17cmock.webp"

            hotspot (893, 297, 178, 525) action Show("v12s7_front_gallery")

        else:
            idle "images/v12/Scene 7/Screens/Navigation 17d.webp" # No one
            hover "images/v12/Scene 7/Buttons/nav 17dmock.webp"
            hotspot (293, 0, 1385, 130) action Show("v12s7_front_gallery")

        hotspot (376, 991, 1115, 87) action Show("v12s7_right_gallery_back")
        hotspot (1423, 66, 497, 796) action Show("v12s7_utility")

    use v12s7_minimap(location="md_right_gallery")

    on "replaced" action SetVariable("previous_location", "v12s7_right_gallery_front")

    if config_debug:
        timer 0.1 action Show(renpy.random.choice(("v12s7_front_gallery", "v12s7_right_gallery_back", "v12s7_utility")))


screen v12s7_utility():
    tag free_roam

    imagemap:
        if "josh" in freeroam9 and josh not in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 18a.webp" # Josh
            hover "images/v12/Scene 7/Buttons/nav 18.webp"
        else:
            idle "images/v12/Scene 7/Screens/Navigation 18b.webp" # No one
            hover "images/v12/Scene 7/Buttons/nav 18b.webp"

        if "josh" in freeroam9 and josh not in v12s7_killList:
            hotspot(413, 183, 452, 895):
                if "josh2" in freeroam9 and not v12s7_aubrey_moved:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferjos3", returnScreen="v12s7_utility", seenList=[], victim=josh)
                elif "josh2" in freeroam9:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferjos3noau", returnScreen="v12s7_utility", seenList=[], victim=josh)
                else:
                    action Jump("v12s7_josh2") # Josh
            hotspot (860, 1000, 1060, 80) action Show("v12s7_right_gallery_front")
        else:
            hotspot (339, 983, 1198, 97) action Show("v12s7_right_gallery_front")

    use v12s7_minimap(location="md_utility")

    on "replaced" action SetVariable("previous_location", "v12s7_utility")

    if config_debug:
        python:
            actions = []

            if "josh" in freeroam9 and josh not in v12s7_killList:
                if "josh2" not in freeroam9:
                    actions.append(Jump("v12s7_josh2")) # Josh

            actions.append(Show("v12s7_right_gallery_front"))

        timer 0.1 action renpy.random.choice(actions)


screen v12s7_front_gallery():
    tag free_roam

    imagemap:
        if v12s7_riley_moved and not "riley2" in freeroam9 and amber not in v12s7_killList and riley not in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 19a.webp" # Amber and Riley
            hover "images/v12/Scene 7/Buttons/nav 19a.webp"

            hotspot (411, 59, 640, 1018):
                action Jump("v12s7_riley2_amber") # Riley & Amber

        elif v12s7_riley_moved and not "riley2" in freeroam9 and amber in v12s7_killList and riley not in v12s7_killList: # Riley
            idle "images/v12/Scene 7/Screens/Navigation 19b.webp"
            hover "images/v12/Scene 7/Buttons/nav 19bmock.webp"

            hotspot (432, 84, 350, 990):
                if "riley2" in freeroam9:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferrile1", returnScreen="v12s7_front_gallery", seenList=[], victim=riley)
                else:
                    action Jump("v12s7_riley2") # Riley

        elif amber not in v12s7_killList: # Amber
            idle "images/v12/Scene 7/Screens/Navigation 19c.webp"
            hover "images/v12/Scene 7/Buttons/nav 19c.webp"

            hotspot (782, 177, 280, 834):
                if "amber" in freeroam9:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12feram1a", returnScreen="v12s7_front_gallery", seenList=[] if ("imre" in freeroam9) else [imre, ryan], victim=amber)
                else:
                    action Jump("v12s7_amber1") # Riley

        else: 
            idle "images/v12/Scene 7/Screens/Navigation 19d.webp" # No one
            hover "images/v12/Scene 7/Buttons/nav 19d.webp"

        hotspot (383, 0, 1198, 97) action Show("v12s7_balcony_middle")
        hotspot (339, 983, 1198, 97) action Show("v12s7_right_gallery_front")
    
        hotspot (293, 0, 1385, 130) action Show("v12s7_balcony_middle")

    
    use v12s7_minimap(location="md_front_gallery")

    on "replaced" action SetVariable("previous_location", "v12s7_front_gallery")

    if config_debug:
        python:
            actions = []

            if v12s7_riley_moved and not "riley2" in freeroam9 and amber not in v12s7_killList and riley not in v12s7_killList:
                actions.append(Jump("v12s7_riley2_amber")) # Riley & Amber

            elif v12s7_riley_moved and not "riley2" in freeroam9 and amber in v12s7_killList and riley not in v12s7_killList: # Riley
                if "riley2" not in freeroam9:
                    actions.append(Jump("v12s7_riley2")) # Riley

            elif amber not in v12s7_killList: # Amber
                if "amber" not in freeroam9:
                    actions.append(Jump("v12s7_amber1")) # Riley

            actions.append(Show("v12s7_balcony_middle"))
            actions.append(Show("v12s7_right_gallery_front"))
        
            actions.append(Show("v12s7_balcony_middle"))

        timer 0.1 action renpy.random.choice(actions)


screen v12s7_balcony_middle():
    tag free_roam

    imagemap:
        idle "images/v12/Scene 7/Screens/Navigation 20a.webp"
        hover "images/v12/Scene 7/Buttons/nav 20.webp"

        hotspot (0, 30, 126, 1020) action Show("v12s7_balcony_left")
        hotspot (1793, 30, 126, 1020) action Show("v12s7_balcony_right")
        hotspot (242, 950, 1385, 130) action Show("v12s7_front_gallery")
       
    use v12s7_minimap(location="md_balcony")

    on "replaced" action SetVariable("previous_location", "v12s7_balcony_middle")

    if config_debug:
        timer 0.1 action Show(renpy.random.choice(("v12s7_balcony_left", "v12s7_balcony_right", "v12s7_front_gallery")))



screen v12s7_balcony_left():
    tag free_roam

    imagemap:
        if nora in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 21b.webp" # No one
            hover "images/v12/Scene 7/Buttons/nav 21b.webp"
        else:
            idle "images/v12/Scene 7/Screens/Navigation 21a.webp" # Nora
            hover "images/v12/Scene 7/Buttons/nav 21.webp"

        if nora not in v12s7_killList:
            hotspot (507, 152, 282, 926):
                if "nora" in freeroam9:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12fernor1", returnScreen="v12s7_balcony_left", seenList=[] if v12s7_aubrey_moved else [riley], victim=nora)
                else:
                    action Jump("v12s7_nora1") # Nora
            hotspot (850, 1000, 1070, 80) action Show("v12s7_balcony_middle")
        else:
            hotspot (339, 983, 1198, 97) action Show("v12s7_balcony_middle")
    
    use v12s7_minimap(location="md_balcony")

    on "replaced" action SetVariable("previous_location", "v12s7_balcony_left")

    if config_debug:
        python:
            actions = []

            if nora not in v12s7_killList:
                if "nora" not in freeroam9:
                    actions.append(Jump("v12s7_nora1")) # Nora

            actions.append(Show("v12s7_balcony_middle"))

        timer 0.1 action renpy.random.choice(actions)


screen v12s7_balcony_right():
    tag free_roam

    imagemap:
        if aubrey in v12s7_killList or v12s7_aubrey_moved:
            idle "images/v12/Scene 7/Screens/Navigation 22b.webp" # No one
            hover "images/v12/Scene 7/Buttons/nav 22b.webp"
        else:
            idle "images/v12/Scene 7/Screens/Navigation 22a.webp" # Aubrey
            hover "images/v12/Scene 7/Buttons/nav 22.webp"

        if not (aubrey in v12s7_killList or v12s7_aubrey_moved):
            hotspot (210, 300, 763, 780):
                if "aubrey" in freeroam9:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferau1a", returnScreen="v12s7_balcony_right", seenList=[nora], victim=aubrey)
                else:
                    action Jump("v12s7_aubrey1") # Aubrey
            hotspot (1793, 30, 126, 1020) action Show("v12s7_balcony_middle")
        else:
            hotspot (339, 983, 1198, 97) action Show("v12s7_balcony_middle")

    use v12s7_minimap(location="md_balcony")

    on "replaced" action SetVariable("previous_location", "v12s7_balcony_right")

    if config_debug:
        python:
            actions = []

            if not (aubrey in v12s7_killList or v12s7_aubrey_moved):
                if "aubrey" not in freeroam9:
                    actions.append(Jump("v12s7_aubrey1")) # Aubrey

            actions.append(Show("v12s7_balcony_middle"))

        timer 0.1 action renpy.random.choice(actions)


screen v12s7_left_gallery_back():
    tag free_roam

    imagemap:
        if aubrey in v12s7_killList or not v12s7_aubrey_moved:
            idle "images/v12/Scene 7/Screens/Navigation 23b.webp" # No one
        else:
            idle "images/v12/Scene 7/Screens/Navigation 23a.webp" # Aubrey
        hover "images/v12/Scene 7/Buttons/nav 23.webp"

        hotspot (899, 210, 321, 517) action Show("v12s7_left_gallery_front")
        hotspot (223, 967, 1422, 114) action Show("v12s7_rear_gallery")

    use v12s7_minimap(location="md_left_gallery")

    on "replaced" action SetVariable("previous_location", "v12s7_left_gallery_back")

    if config_debug:
        timer 0.1 action Show(renpy.random.choice(("v12s7_left_gallery_front", "v12s7_rear_gallery")))


screen v12s7_left_gallery_front():
    tag free_roam

    imagemap:
        if aubrey in v12s7_killList or not v12s7_aubrey_moved:
            idle "images/v12/Scene 7/Screens/Navigation 24b.webp" # No one
        else:
            idle "images/v12/Scene 7/Screens/Navigation 24a.webp" # Aubrey
        hover "images/v12/Scene 7/Buttons/nav 24.webp"

        hotspot (0, 0, 105, 1080) action Show("v12s7_left_gallery_back")
        hotspot (479, 0, 821, 1080) action Show("v12s7_bathroom")
        hotspot (1545, 0, 375, 1080) action Show("v12s7_captains_room")

    use v12s7_minimap(location="md_left_gallery")

    on "replaced" action SetVariable("previous_location", "v12s7_left_gallery_front")

    if config_debug:
        timer 0.1 action Show(renpy.random.choice(("v12s7_left_gallery_back", "v12s7_bathroom", "v12s7_captains_room")))


screen v12s7_bathroom():
    tag free_roam

    imagemap:
        if aubrey in v12s7_killList or not v12s7_aubrey_moved:
            idle "images/v12/Scene 7/Screens/Navigation 25b.webp" # No one
            hover "images/v12/Scene 7/Buttons/nav 25b.webp"
        else:
            idle "images/v12/Scene 7/Screens/Navigation 25a.webp" # Aubrey
            hover "images/v12/Scene 7/Buttons/nav 25.webp"
    
        if not (aubrey in v12s7_killList or not v12s7_aubrey_moved):
            hotspot (657, 196, 483, 878):
                if "aubrey2" in freeroam9:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferauh1a", returnScreen="v12s7_bathroom", seenList=[], victim=aubrey)
                else:
                    action Jump("v12s7_aubrey2") # Aubrey
                
            hotspot (1836, 79, 82, 959) action Show("v12s7_left_gallery_front")

        else:
            hotspot (339, 983, 1198, 97) action Show("v12s7_left_gallery_front")


    use v12s7_minimap(location="md_bathroom")

    on "replaced" action SetVariable("previous_location", "v12s7_bathroom")

    if config_debug:
        python:
            actions = []

            if not (aubrey in v12s7_killList or not v12s7_aubrey_moved):
                if "aubrey2" not in freeroam9:
                    actions.append(Jump("v12s7_aubrey2")) # Aubrey
                    
                actions.append(Show("v12s7_left_gallery_front"))

            else:
                actions.append(Show("v12s7_left_gallery_front"))
        
        timer 0.1 action renpy.random.choice(actions)


screen v12s7_captains_room():
    tag free_roam
    
    imagemap:
        if not v12s7_lindsey_moved:
            idle "images/v12/Scene 7/Screens/Navigation 26a.webp" # Lindsey and Charli
            hover "images/v12/Scene 7/Buttons/nav 26a.webp"

            hotspot (506, 117, 1013, 959):
                if "lindsey" in freeroam9:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12ferlich1", returnScreen="v12s7_captains_room", seenList=[lindsey, charli], victim=lindsey)
                else:
                    action Jump("v12s7_lindsey_charlie1") # Lindsey & Charli
            hotspot (1824, 79, 95, 957) action Show("v12s7_left_gallery_front")

        elif charli not in v12s7_killList:
            idle "images/v12/Scene 7/Screens/Navigation 26b.webp" # Charli
            hover "images/v12/Scene 7/Buttons/nav 26b.webp"

            hotspot (1200, 163, 254, 720):
                if "charli" in freeroam9:
                    action Call("v12s7_free_roam_spoken", backgroundImg="v12fercha1", returnScreen="v12s7_captains_room", seenList=[], victim=charli)
                else:
                    action Jump("v12s7_charli2") # Charli
            hotspot (1824, 79, 95, 957) action Show("v12s7_left_gallery_front")

        else:
            idle "images/v12/Scene 7/Screens/Navigation 26c.webp" # No one
            hover "images/v12/Scene 7/Buttons/nav 26c.webp"

            hotspot (1824, 79, 95, 957) action Show("v12s7_left_gallery_front")

        

    use v12s7_minimap(location="ud_captains_room")

    on "replaced" action SetVariable("previous_location", "v12s7_captains_room")

    if config_debug:
        python:
            actions = []

            if not v12s7_lindsey_moved:
                if "lindsey" not in freeroam9:
                    actions.append(Jump("v12s7_lindsey_charlie1")) # Lindsey & Charli

            elif charli not in v12s7_killList:
                if "charli" not in freeroam9:
                    actions.append(Jump("v12s7_charli2")) # Charli

            actions.append(Show("v12s7_left_gallery_front"))

        timer 0.1 action renpy.random.choice(actions)
