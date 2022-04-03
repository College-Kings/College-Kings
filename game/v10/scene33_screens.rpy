screen v10s33_entrance():
    tag free_roam

    # Background
    if not v10s33_toldChloe and "riley" in freeroam6 and not "ryan" in freeroam6:
        add "images/v10/scene 33/Ent1.webp"
    if v10s33_toldChloe and "riley" in freeroam6 and not "ryan" in freeroam6:
        add "images/v10/scene 33/Ent2.webp"
    if v10s33_toldChloe and not "riley" in freeroam6 and not "ryan" in freeroam6:
        add "images/v10/scene 33/Ent3.webp"
    if not v10s33_toldChloe and "riley" in freeroam6 and "ryan" in freeroam6:
        add "images/v10/scene 33/Ent4.webp"
    if not v10s33_toldChloe and not "riley" in freeroam6 and "ryan" in freeroam6:
        add "images/v10/scene 33/Ent5.webp"
    if v10s33_toldChloe and not "riley" in freeroam6 and "ryan" in freeroam6:
        add "images/v10/scene 33/Ent6.webp"
    if not v10s33_toldChloe and not "riley" in freeroam6 and not "ryan" in freeroam6:
        add "images/v10/scene 33/Ent7.webp"
    if v10s33_toldChloe and "riley" in freeroam6 and "ryan" in freeroam6:
        add "images/v10/scene 33/Ent8.webp"

    # Cake statue - Right
    imagebutton:
        align (1.0, 0.5)
        idle "images/v10/scene 33/freeroamidle_hori.webp"
        hover "images/v10/scene 33/fr4righthover.webp"
        action Show("v10s33_cakestatue")

    # Toilet - Left
    imagebutton:
        align (0, 0.5)
        idle "images/v10/scene 33/freeroamidle_hori.webp"
        hover "images/v10/scene 33/fr4lefthover.webp"
        action Show("v10s33_toilet")

    # Centre aisle - Top
    imagebutton:
        align (0.5, 0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4tophover.webp"
        action Show("v10s33_centeraisle")

    if config_debug:
        timer 0.1 action Show(renpy.random.choice(("v10s33_cakestatue", "v10s33_toilet", "v10s33_centeraisle")))


screen v10s33_cakestatue():
    tag free_roam

    # Background
    if v10s33_laurenBakeSale:
        add "images/v10/scene 33/fr6cake.webp"
    else:
        add "images/v10/scene 33/fr6statue.webp"

    # Lauren - Bake sale
    if v10s33_laurenBakeSale:
        imagebutton:
            pos (1579, 324)
            idle "images/v10/scene 33/fr6laurenbake.webp"
            hover "images/v10/scene 33/fr6laurenbakehover.webp"
            if "lauren" not in freeroam6:
                action Jump("v10s33_laurenbake1")
            else:
                action Call("free_roam_spoken_too", "v10cfrla1a", "v10s33_cakestatue")

    # Lauren - Statue
    else:
        imagebutton:
            pos (1182, 139)
            idle "images/v10/scene 33/fr6laurenstatue.webp"
            hover "images/v10/scene 33/fr6laurenstatuehover.webp"
            if "lauren" not in freeroam6:
                action Jump("v10s33_laurenstatue1")
            else:
                action Call("free_roam_spoken_too", "v10cfrla3", "v10s33_cakestatue")

    # Bench - Left
    imagebutton:
        yalign 0.5
        idle "images/v10/scene 33/freeroamidle_hori.webp"
        hover "images/v10/scene 33/fr4lefthover.webp"
        action Show("v10s33_bench")

    # Entrance - Bottom
    imagebutton:
        align (0.5, 1.0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4bottomhover.webp"
        action Show("v10s33_entrance")

    if config_debug:
        python:
            actions = []

            if v10s33_laurenBakeSale:
                if "lauren" not in freeroam6:
                    actions.append(Jump("v10s33_laurenbake1"))

            else:
                if "lauren" not in freeroam6:
                    actions.append(Jump("v10s33_laurenstatue1"))

            actions.append(Show("v10s33_bench"))

            actions.append(Show("v10s33_entrance"))

        timer 0.1 action renpy.random.choice(actions)


screen v10s33_bench():
    tag free_roam

    # Background
    if v10s33_toldChloe:
        add "images/v10/scene 33/fr6benchchloenoraatmudwrestling.webp"
    else:
        add "images/v10/scene 33/fr6bench.webp"

    # Emily
    imagebutton: 
        pos (942, 420)
        idle "images/v10/scene 33/fr6emily.webp"
        hover "images/v10/scene 33/fr6emilyhover.webp"
        if not "emily" in freeroam6:
            action Jump("v10s33_emily1")
        else:
            action Call("free_roam_spoken_too", "v10cfrem1a", "v10s33_bench")
  
    # Centre aisle - Left
    imagebutton:
        yalign 0.5
        idle "images/v10/scene 33/freeroamidle_hori.webp"
        hover "images/v10/scene 33/fr4lefthover.webp"
        action Show("v10s33_centeraisle")

    # Cake statue - Bottom
    imagebutton:
        align (0.5, 1.0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4bottomhover.webp"
        action Show("v10s33_cakestatue")

    if config_debug:
        python:
            actions = []

            if not "emily" in freeroam6:
                actions.append(Jump("v10s33_emily1"))

            actions.append(Show("v10s33_centeraisle"))

            actions.append(Show("v10s33_cakestatue"))

        timer 0.1 action renpy.random.choice(actions)

 
screen v10s33_toilet(): # NO
    tag free_roam

    # Background
    if "ryan" in freeroam6:
        add "images/v10/scene 33/fr6toiletwithryan.webp"
    else:
        add "images/v10/scene 33/fr6toilet.webp"

    # Evelyn
    imagebutton:
        pos (613, 207)
        idle "images/v10/scene 33/fr6evelyn.webp"
        hover "images/v10/scene 33/fr6evelynhover.webp"
        if not "evelyn" in freeroam6:
            action Jump("v10s33_evelyn1")
        else:
            action Call("free_roam_spoken_too", "v10cfrev1a", "v10s33_toilet")

    # Toilet Ryan
    if "ryan" in freeroam6:            
        imagebutton: 
            pos (812, 253)
            idle "images/v10/scene 33/fr6toiletryan.webp"
            hover "images/v10/scene 33/fr6toiletryanhover.webp"
            if not "ryan2" in freeroam6:
                action Jump("v10s33_toiletryan1")
            else:
                action Call("free_roam_spoken_too", "v10cfrry5", "v10s33_toilet")

    # Body paint - Right
    imagebutton:
        align (1.0, 0.5)
        idle "images/v10/scene 33/freeroamidle_hori.webp"
        hover "images/v10/scene 33/fr4righthover.webp"
        action Show("v10s33_bodypaint")

    # Entrance - Bottom
    imagebutton:
        align (0.5, 1.0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4bottomhover.webp"
        action Show("v10s33_entrance")

    if config_debug:
        python:
            actions = []

            if not "evelyn" in freeroam6:
                actions.append(Jump("v10s33_evelyn1"))

            # Toilet Ryan
            if "ryan" in freeroam6:            
                if not "ryan2" in freeroam6:
                    actions.append(Jump("v10s33_toiletryan1"))

            actions.append(Show("v10s33_bodypaint"))

            actions.append(Show("v10s33_entrance"))

        timer 0.1 action renpy.random.choice(actions)


screen v10s33_bodypaint():
    tag free_roam

    # Background
    if "riley" in freeroam6:
        add "images/v10/scene 33/fr6bodypaintnoriley.webp"
    else:
        add "images/v10/scene 33/fr6bodypaint.webp"

    # Ms Rose
    imagebutton: 
        pos (473, 315)
        idle "images/v10/scene 33/fr6msrose.webp"
        hover "images/v10/scene 33/fr6msrosehover.webp"
        if not "rose" in freeroam6:
            action Jump("v10s33_msrose1")
        else:
            action Call("free_roam_spoken_too", "v10cfrcfrro1", "v10s33_bodypaint")

    # Lindsey
    imagebutton: 
        pos (783, 346)
        idle "images/v10/scene 33/fr6lindsey.webp"
        hover "images/v10/scene 33/fr6lindseyhover.webp"
        if not "lindsey" in freeroam6:
            action Jump("v10s33_lindsey1")
        else:
            action Call("free_roam_spoken_too", "v10cfrfrli1", "v10s33_bodypaint")

    # Thrift - Top
    imagebutton:
        xalign 0.5
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4tophover.webp"
        action Show("v10s33_thrift")

    # Toilet - Bottom
    imagebutton:
        align (0.5, 1.0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4bottomhover.webp"
        action Show("v10s33_toilet")

    if config_debug:
        python:
            actions = []

            if not "rose" in freeroam6:
                actions.append(Jump("v10s33_msrose1"))

            if not "lindsey" in freeroam6:
                actions.append(Jump("v10s33_lindsey1"))

            actions.append(Show("v10s33_thrift"))

            actions.append(Show("v10s33_toilet"))

        timer 0.1 action renpy.random.choice(actions)


screen v10s33_thrift():
    tag free_roam

    # Background
    if "riley" in freeroam6:
        add "images/v10/scene 33/fr6thriftnoriley.webp"
    else:
        add "images/v10/scene 33/fr6thrift.webp"

    # Deer Girl 4
    imagebutton: 
        pos (629, 433)
        idle "images/v10/scene 33/fr6deergirl4.webp"
        hover "images/v10/scene 33/fr6deergirl4hover.webp"
        action Jump("v10s33_deergirl41")

    # Riley
    if not "riley" in freeroam6:                
        imagebutton: 
            pos (391, 388)
            idle "images/v10/scene 33/fr6riley.webp"
            hover "images/v10/scene 33/fr6rileyhover.webp"
            action Jump("v10s33_riley1")

    # Stage from left - Top
    imagebutton:
        xalign 0.5
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4tophover.webp"
        action Show("v10s33_stagefromleft")

    # Body paint - Bottom
    imagebutton:
        align (0.5, 1.0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4bottomhover.webp"
        action Show("v10s33_bodypaint")

    if config_debug:
        python:
            actions = []

            actions.append(Jump("v10s33_deergirl41"))

            if not "riley" in freeroam6:                
                actions.append(Jump("v10s33_riley1"))

            actions.append(Show("v10s33_stagefromleft"))

            actions.append(Show("v10s33_bodypaint"))

        timer 0.1 action renpy.random.choice(actions)


screen v10s33_stagefromleft():
    tag free_roam

    # Background 
    if "riley" in freeroam6 and v10s33_toldChloe:
        add "images/v10/scene 33/fr6stagefromleftchloeandnoraatmudwrestlingwithrileyatstage.webp"
    if "riley" in freeroam6 and not v10s33_toldChloe:
        add "images/v10/scene 33/fr6stagewithrileyatstage.webp"
    if not "riley" in freeroam6 and v10s33_toldChloe:
        add "images/v10/scene 33/fr6stagefromleftchloeandnoraatmudwrestling.webp"
    if not "riley" in freeroam6 and not v10s33_toldChloe:
        add "images/v10/scene 33/fr6stageleft.webp"

    # Thrift - Bottom
    imagebutton:
        xalign 0.5
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4tophover.webp"
        action Show("v10s33_stage")

    # Stage - Top
    imagebutton:
        align (0.5, 1.0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4bottomhover.webp"
        action Show("v10s33_thrift")

    if config_debug:
        timer 0.1 action Show(renpy.random.choice(("v10s33_stage", "v10s33_thrift")))


screen v10s33_stage():
    tag free_roam

    # Background
    if "riley" in freeroam6:
        add "images/v10/scene 33/fr6stagewithriley.webp"
    else:
        add "images/v10/scene 33/fr6stage.webp"

    # Aubrey
    if not "riley" in freeroam6:   
        imagebutton: 
            pos (1282, 322)
            idle "images/v10/scene 33/fr6aubrey.webp"
            hover "images/v10/scene 33/fr6aubreyhover.webp"
            if not "aubrey" in freeroam6:
                action Jump("v10s33_aubrey1")
            else:
                action Call("free_roam_spoken_too", "v10cfrau1", "v10s33_stage")

    # Aubrey & Riley
    else:   
        imagebutton: 
            pos (1062, 168)
            idle "images/v10/scene 33/fr6aubreyriley.webp"
            hover "images/v10/scene 33/fr6aubreyrileyhover.webp"
            if not v10s33_aubreyriley:
                action Jump("v10s33_riley2")
            else:
                action Call("free_roam_spoken_too", "v10cfrriau1", "v10s33_stage")

    # Deer girl 1
    imagebutton: 
        pos (650, 195)
        idle "images/v10/scene 33/fr6deergirl1.webp"
        hover "images/v10/scene 33/fr6deergirl1hover.webp"
        if not "rachel" in freeroam6:
            action Jump("v10s33_deergirl11")
        else:
            action Call("free_roam_spoken_too", "v10cfrdg11", "v10s33_stage")

    # Stage from left - Left
    imagebutton:
        yalign 0.5
        idle "images/v10/scene 33/freeroamidle_hori.webp"
        hover "images/v10/scene 33/fr4lefthover.webp"
        action Show("v10s33_stagefromleft")

    # Bag toss - Right
    imagebutton:
        align (1.0, 0.5)
        idle "images/v10/scene 33/freeroamidle_hori.webp"
        hover "images/v10/scene 33/fr4righthover.webp"
        action Show("v10s33_bagtoss")

    # Centre aisle - Bottom
    imagebutton:
        align (0.5, 1.0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4bottomhover.webp"
        action Show("v10s33_centeraisle")

    if config_debug:
        python:
            actions = []

            if not "aubrey" in freeroam6:
                actions.append(Jump("v10s33_aubrey1"))

            if not v10s33_aubreyriley:
                actions.append(Jump("v10s33_riley2"))

            if not "rachel" in freeroam6:
                actions.append(Jump("v10s33_deergirl11"))

            actions.append(Show("v10s33_stagefromleft"))

            actions.append(Show("v10s33_bagtoss"))

            actions.append(Show("v10s33_centeraisle"))

        timer 0.1 action renpy.random.choice(actions)


screen v10s33_bagtoss():
    tag free_roam

    # Background
    if v10s33_toldChloe:
        add "images/v10/scene 33/fr6bagtossnonora.webp"
    else:
        add "images/v10/scene 33/fr6bagtoss.webp"

    # Deer Girl 2
    imagebutton:
        pos (89, 274)
        idle "images/v10/scene 33/fr6deergirl2.webp"
        hover "images/v10/scene 33/fr6deergirl2hover.webp"
        if not "eleanor" in freeroam6:
            action Jump("v10s33_deergirl21")
        else:
            action Call("free_roam_spoken_too", "v10cfrdg21", "v10s33_bagtoss")

    # Chris
    imagebutton:
        pos (1032, 255)
        idle "images/v10/scene 33/fr6chris.webp"
        hover "images/v10/scene 33/fr6chrishover.webp"
        if not "chris" in freeroam6:
            action Jump("v10s33_chris1")
        else:
            action Call("free_roam_spoken_too", "v10cfrch1", "v10s33_bagtoss")

    # Nora
    if not v10s33_toldChloe:
        imagebutton:
            pos (754, 293)
            idle "images/v10/scene 33/fr6nora.webp"
            hover "images/v10/scene 33/fr6norahover.webp"
            if not "nora" in freeroam6:
                action Jump("v10s33_nora1")
            else:
                action Call("free_roam_spoken_too", "v10cfrno1", "v10s33_bagtoss")

    # Stage - Bottom
    imagebutton:
        align (0.5, 1.0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4bottomhover.webp"
        action Show("v10s33_stage")

    if config_debug:
        python:
            actions = []

            if not "eleanor" in freeroam6:
                actions.append(Jump("v10s33_deergirl21"))

            if not "chris" in freeroam6:
                actions.append(Jump("v10s33_chris1"))

            # Nora
            if not v10s33_toldChloe:
                if not "nora" in freeroam6:
                    actions.append(Jump("v10s33_nora1"))

            actions.append(Show("v10s33_stage"))

        timer 0.1 action renpy.random.choice(actions)


screen v10s33_centeraisle():
    tag free_roam

    # Background
    if v10s33_toldChloe and "riley" in freeroam6 and "ryan" in freeroam6:
        add "images/v10/scene 33/Mid8.webp"
    if v10s33_toldChloe and "riley" in freeroam6 and not "ryan" in freeroam6:
        add "images/v10/scene 33/Mid2.webp"
    if v10s33_toldChloe and not "riley" in freeroam6 and "ryan" in freeroam6:
        add "images/v10/scene 33/Mid6.webp"
    if v10s33_toldChloe and not "riley" in freeroam6 and not "ryan" in freeroam6:
        add "images/v10/scene 33/Mid3.webp"
    if not v10s33_toldChloe and "riley" in freeroam6 and "ryan" in freeroam6:
        add "images/v10/scene 33/Mid4.webp"
    if not v10s33_toldChloe and "riley" in freeroam6 and not "ryan" in freeroam6:
        add "images/v10/scene 33/Mid1.webp"
    if not v10s33_toldChloe and not "riley" in freeroam6 and "ryan" in freeroam6:
        add "images/v10/scene 33/Mid5.webp"
    if not v10s33_toldChloe and not "riley" in freeroam6 and not "ryan" in freeroam6:
        add "images/v10/scene 33/Mid7.webp"

    # Chloe
    if not v10s33_toldChloe:
        imagebutton:
            pos (534, 331)
            idle "images/v10/scene 33/fr6chloe.webp"
            hover "images/v10/scene 33/fr6chloehover.webp"
            if not "chloe" in freeroam6:
                action Jump("v10s33_chloe1")
            else:
                action Call("free_roam_spoken_too", "v10cfrcl1", "v10s33_centeraisle")

    # Deer Girl 3
    imagebutton:
        pos (180, 338)
        idle "images/v10/scene 33/fr6deergirl3.webp"
        hover "images/v10/scene 33/fr6deergirl3hover.webp"
        if not "karen" in freeroam6:
            action Jump("v10s33_deergirl31")
        else:
            action Call("free_roam_spoken_too", "v10cfrdg31a", "v10s33_centeraisle")
    
    # Ryan
    if not "ryan" in freeroam6:
        imagebutton:
            pos (1290, 251)
            idle "images/v10/scene 33/fr6ryan.webp"
            hover "images/v10/scene 33/fr6ryanhover.webp"
            if not "ryan" in freeroam6:
                action Jump("v10s33_ryan1")
            else:
                action Call("free_roam_spoken_too", "v10cfrry1", "v10s33_centeraisle")

    # Stage - Top
    imagebutton:
        xalign 0.5
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4tophover.webp"
        action Show("v10s33_stage")

    # Mud Wrestling - Right
    imagebutton:
        align (1.0, 0.5)
        idle "images/v10/scene 33/freeroamidle_hori.webp"
        hover "images/v10/scene 33/fr4righthover.webp"
        action Show("v10s33_mudwrestling")

    # Entrance - Bottom
    imagebutton:
        align (0.5, 1.0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4bottomhover.webp"
        action Show("v10s33_entrance")

    if config_debug:
        python:
            actions = []

            if not v10s33_toldChloe:
                if not "chloe" in freeroam6:
                    actions.append(Jump("v10s33_chloe1"))

            if not "karen" in freeroam6:
                actions.append(Jump("v10s33_deergirl31"))
            
            if not "ryan" in freeroam6:
                if not "ryan" in freeroam6:
                    actions.append(Jump("v10s33_ryan1"))

            actions.append(Show("v10s33_stage"))

            actions.append(Show("v10s33_mudwrestling"))

            actions.append(Show("v10s33_entrance"))

        timer 0.1 action renpy.random.choice(actions)


screen v10s33_mudwrestling():
    tag free_roam

    # Background
    if v10s33_toldChloe:
        add "images/v10/scene 33/fr6mudwrestlingwithnoraandchloe.webp"
    else:
        add "images/v10/scene 33/fr6mudwrestling.webp"

    # Amber
    imagebutton: 
        pos (1607, 320)
        idle "images/v10/scene 33/fr6amber.webp"
        hover "images/v10/scene 33/fr6amberhover.webp"
        if not "amber" in freeroam6:
            action Jump("v10s33_amber1")
        else:
            action Call("free_roam_spoken_too", "v10cfram1", "v10s33_mudwrestling")
    
    # Autumn
    imagebutton: 
        pos (1207, 299)
        idle "images/v10/scene 33/fr6autumn.webp"
        hover "images/v10/scene 33/fr6autumnhover.webp"
        if not "autumn" in freeroam6:
            action Jump("v10s33_autumn1")
        else:
            action Show("confirm", message="Are you sure you want to end the free roam?", yes_action=[Hide("confirm"), Jump("v10_autumn_announcement")])

    # Centre Aisle - Bottom
    imagebutton:
        align (0.5, 1.0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4bottomhover.webp"
        action Show("v10s33_centeraisle")

    if config_debug:
        python:
            actions = []

            if not "amber" in freeroam6:
                actions.append(Jump("v10s33_amber1"))
        
            if not "autumn" in freeroam6:
                actions.append(Jump("v10s33_autumn1"))
            else:
                actions.append(Show("confirm", message="Are you sure you want to end the free roam?", yes_action=[Hide("confirm"), Jump("v10_autumn_announcement")]))

            actions.append(Show("v10s33_centeraisle"))

        timer 0.1 action renpy.random.choice(actions)
