screen v10s33_entrance():
    tag tag_freeRoam

    # Background
    if not v10s33_toldChloe and v10s33_riley and not v10s33_ryan:
        $ v10s33_background = "images/v10/scene 33/Ent1.webp"
    if v10s33_toldChloe and v10s33_riley and not v10s33_ryan:
        $ v10s33_background = "images/v10/scene 33/Ent2.webp"
    if v10s33_toldChloe and not v10s33_riley and not v10s33_ryan:
        $ v10s33_background = "images/v10/scene 33/Ent3.webp"
    if not v10s33_toldChloe and v10s33_riley and v10s33_ryan:
        $ v10s33_background = "images/v10/scene 33/Ent4.webp"
    if not v10s33_toldChloe and not v10s33_riley and v10s33_ryan:
        $ v10s33_background = "images/v10/scene 33/Ent5.webp"
    if v10s33_toldChloe and not v10s33_riley and v10s33_ryan:
        $ v10s33_background = "images/v10/scene 33/Ent6.webp"
    if not v10s33_toldChloe and not v10s33_riley and not v10s33_ryan:
        $ v10s33_background = "images/v10/scene 33/Ent7.webp"
    if v10s33_toldChloe and v10s33_riley and v10s33_ryan:
        $ v10s33_background = "images/v10/scene 33/Ent8.webp"

    add v10s33_background

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


screen v10s33_cakestatue():
    tag tag_freeRoam
    
    # Background
    if v10s33_laurenBakeSale:
        $ v10s33_background = "images/v10/scene 33/fr6cake.webp"
    else:
        $ v10s33_background = "images/v10/scene 33/fr6statue.webp"

    add v10s33_background

    # Lauren - Bake sale
    if v10s33_laurenBakeSale:
        imagebutton:
            pos (0, 0)
            idle "images/v10/scene 33/fr6laurenbake.webp"
            hover "images/v10/scene 33/fr6laurenbakehover.webp"
            if not v10s33_lauren:
                action Jump("v10s33_laurenbake1")
            else:
                action Call("freeRoamSpokenToo", backgroundImg=v10s33_background, returnScreen="v10s33_cakestatue")

    # Lauren - Statue
    else:
        imagebutton:
            pos (0, 0)
            idle "images/v10/scene 33/fr6laurenstatue.webp"
            hover "images/v10/scene 33/fr6laurenstatuehover.webp"
            if not v10s33_lauren:
                action Jump("v10s33_laurenstatue1")
            else:
                action Call("freeRoamSpokenToo", backgroundImg=v10s33_background, returnScreen="v10s33_cakestatue")

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


screen v10s33_bench():
    tag tag_freeRoam

    # Background
    if v10s33_toldChloe:
        $ v10s33_background = "images/v10/scene 33/fr6benchchloenoraatmudwrestling.webp"
    else:
        $ v10s33_background = "images/v10/scene 33/fr6bench.webp"

    add v10s33_background

    # Emily
    imagebutton: 
        pos (0, 0)
        idle "images/v10/scene 33/fr6emily.webp"
        hover "images/v10/scene 33/fr6emilyhover.webp"
        if not v10s33_emily:
            action Jump("v10s33_emily1")
        else:
            action Call("freeRoamSpokenToo", backgroundImg=v10s33_background, returnScreen="v10s33_bench")
  
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
        
 
screen v10s33_toilet():
    tag tag_freeRoam

    # Background
    if v10s33_ryan:
        $ v10s33_background = "images/v10/scene 33/fr6toiletwithryan.webp" #IMAGE NEEDS TO BE RENDERED
    else:
        $ v10s33_background = "images/v10/scene 33/fr6toilet.webp" #IMAGE NEEDS TO BE RENDERED

    add v10s33_background

    # Evelyn
    imagebutton:
        pos (0, 0)
        idle "images/v10/scene 33/fr6evelyn.webp"
        hover "images/v10/scene 33/fr6evelynhover.webp"
        if not v10s33_evelyn:
            action Jump("v10s33_evelyn1")
        else:
            action Call("freeRoamSpokenToo", backgroundImg=v10s33_background, returnScreen="v10s33_toilet")

    # Toilet Ryan
    if v10s33_ryan:            
        imagebutton: 
            pos (0, 0)
            idle "images/v10/scene 33/fr6toiletryan.webp"
            hover "images/v10/scene 33/fr6toiletryanhover.webp"
            if not v10s33_ryanb:
                action Jump("v10s33_toiletryan1")
            else:
                action Call("freeRoamSpokenToo", backgroundImg=v10s33_background, returnScreen="v10s33_toilet")

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


screen v10s33_bodypaint():
    tag tag_freeRoam

    # Background
    if v10s33_riley:
        $ v10s33_background = "images/v10/scene 33/fr6bodypaintnoriley.webp" #IMAGE NEEDS TO BE RENDERED
    else:
        $ v10s33_background = "images/v10/scene 33/fr6bodypaint.webp" #IMAGE NEEDS TO BE RENDERED

    add v10s33_background

    # Ms Rose
    imagebutton: 
        pos (0, 0)
        idle "images/v10/scene 33/fr6msrose.webp"
        hover "images/v10/scene 33/fr6msrosehover.webp"
        if not v10s33_msRose:
            action Jump("v10s33_msrose1")
        else:
            action Call("freeRoamSpokenToo", backgroundImg=v10s33_background, returnScreen="v10s33_bodypaint")

    # Lindsey
    imagebutton: 
        pos (0, 0)
        idle "images/v10/scene 33/fr6lindsey.webp"
        hover "images/v10/scene 33/fr6lindseyhover.webp"
        if not v10s33_lindsey:
            action Jump("v10s33_lindsey1")
        else:
            action Call("freeRoamSpokenToo", backgroundImg=v10s33_background, returnScreen="v10s33_bodypaint")

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


screen v10s33_thrift():
    tag tag_freeRoam

    # Background
    if v10s33_riley:
        $ v10s33_background = "images/v10/scene 33/fr6thriftnoriley.webp" #IMAGE NEEDS TO BE RENDERED
    else:
        $ v10s33_background = "images/v10/scene 33/fr6thrift.webp" #IMAGE NEEDS TO BE RENDERED

    add v10s33_background

    # Deer Girl 4
    imagebutton: 
        pos (0, 0)
        idle "images/v10/scene 33/fr6deergirl4.webp"
        hover "images/v10/scene 33/fr6deergirl4hover.webp"
        action Jump("v10s33_deergirl41")

    # Riley
    if not v10s33_riley:                
        imagebutton: 
            pos (0, 0)
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


screen v10s33_stagefromleft():
    tag tag_freeRoam

    # Background 
    if v10s33_riley and v10s33_toldChloe:
        $ v10s33_background = "images/v10/scene 33/fr6stagefromleftchloeandnoraatmudwrestlingwithrileyatstage.webp"
    if v10s33_riley and not v10s33_toldChloe:
        $ v10s33_background = "images/v10/scene 33/fr6stagewithrileyatstage.webp"
    if not v10s33_riley and v10s33_toldChloe:
        $ v10s33_background = "images/v10/scene 33/fr6stagefromleftchloeandnoraatmudwrestling.webp"
    if not v10s33_riley and not v10s33_toldChloe:
        $ v10s33_background = "images/v10/scene 33/fr6stageleft.webp"

    add v10s33_background

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


screen v10s33_stage():
    tag tag_freeRoam

    # Background
    if v10s33_riley:
        $ v10s33_background = "images/v10/scene 33/fr6stagewithriley.webp" #IMAGE NEEDS TO BE RENDERED
    else:
        $ v10s33_background = "images/v10/scene 33/fr6stage.webp" #IMAGE NEEDS TO BE RENDERED

    add v10s33_background

    # Aubrey
    if not v10s33_riley:   
        imagebutton: 
            pos (0, 0)
            idle "images/v10/scene 33/fr6aubrey.webp"
            hover "images/v10/scene 33/fr6aubreyhover.webp"
            if not v10s33_aubrey:
                action Jump("v10s33_aubrey1")
            else:
                action Call("freeRoamSpokenToo", backgroundImg=v10s33_background, returnScreen="v10s33_stage")

    # Aubrey & Riley
    else:   
        imagebutton: 
            pos (0, 0)
            idle "images/v10/scene 33/fr6aubreyriley.webp"
            hover "images/v10/scene 33/fr6aubreyrileyhover.webp"
            if not v10s33_aubreyriley:
                action Jump("v10s33_aubreyriley1")
            else:
                action Call("freeRoamSpokenToo", backgroundImg=v10s33_background, returnScreen="v10s33_stage")

    # Deer girl 1
    imagebutton: 
        pos (0, 0)
        idle "images/v10/scene 33/fr6deergirl1.webp"
        hover "images/v10/scene 33/fr6deergirl1hover.webp"
        if not v10s33_deergirl1:
            action Jump("v10s33_deergirl11")
        else:
            action Call("freeRoamSpokenToo", backgroundImg=v10s33_background, returnScreen="v10s33_stage")

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


screen v10s33_bagtoss():
    tag tag_freeRoam

    # Background
    if v10s33_toldChloe:
        $ v10s33_background = "images/v10/scene 33/fr6bagtossnonora.webp" #IMAGE NEEDS TO BE RENDERED
    else:
        $ v10s33_background = "images/v10/scene 33/fr6bagtoss.webp" #IMAGE NEEDS TO BE RENDERED

    add v10s33_background

    # Deer Girl 2
    imagebutton:
        pos (0, 0)
        idle "images/v10/scene 33/fr6deergirl2.webp"
        hover "images/v10/scene 33/fr6deergirl2.webp"
        if not v10s33_deergirl2:
            action Jump("v10s33_deergirl21")
        else:
            action Call("freeRoamSpokenToo", backgroundImg=v10s33_background, returnScreen="v10s33_bagtoss")

    # Chris
    imagebutton:
        pos (0, 0)
        idle "images/v10/scene 33/fr6chris.webp"
        hover "images/v10/scene 33/fr6chrishover.webp"
        if not v10s33_chris:
            action Jump("v10s33_chris1")
        else:
            action Call("freeRoamSpokenToo", backgroundImg=v10s33_background, returnScreen="v10s33_bagtoss")

    # Nora
    if not v10s33_toldChloe:
        imagebutton:
            pos (0, 0)
            idle "images/v10/scene 33/fr6nora.webp"
            hover "images/v10/scene 33/fr6norahover.webp"
            if not v10s33_nora:
                action Jump("v10s33_nora1")
            else:
                action Call("freeRoamSpokenToo", backgroundImg=v10s33_background, returnScreen="v10s33_bagtoss")

    # Stage - Bottom
    imagebutton:
        align (0.5, 1.0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4bottomhover.webp"
        action Show("v10s33_stage")


screen v10s33_centeraisle():
    tag tag_freeRoam

    # Background
    if v10s33_toldChloe and v10s33_riley and v10s33_ryan:
        $ v10s33_background = "images/v10/scene 33/Mid8.webp"
    if v10s33_toldChloe and v10s33_riley and not v10s33_ryan:
        $ v10s33_background = "images/v10/scene 33/Mid2.webp"
    if v10s33_toldChloe and not v10s33_riley and v10s33_ryan:
        $ v10s33_background = "images/v10/scene 33/Mid6.webp"
    if v10s33_toldChloe and not v10s33_riley and not v10s33_ryan:
        $ v10s33_background = "images/v10/scene 33/Mid3.webp"
    if not v10s33_toldChloe and v10s33_riley and v10s33_ryan:
        $ v10s33_background = "images/v10/scene 33/Mid4.webp"
    if not v10s33_toldChloe and v10s33_riley and not v10s33_ryan:
        $ v10s33_background = "images/v10/scene 33/Mid1.webp"
    if not v10s33_toldChloe and not v10s33_riley and v10s33_ryan:
        $ v10s33_background = "images/v10/scene 33/Mid5.webp"
    if not v10s33_toldChloe and not v10s33_riley and not v10s33_ryan:
        $ v10s33_background = "images/v10/scene 33/Mid7.webp"

    add v10s33_background

    # Chloe
    if not v10s33_toldChloe:
        imagebutton:
            pos (0, 0)
            idle "images/v10/scene 33/fr6chloe.webp"
            hover "images/v10/scene 33/fr6chloehover.webp"
            if not v10s33_chloe:
                action Jump("v10s33_chloe1")
            else:
                action Call("freeRoamSpokenToo", backgroundImg=v10s33_background, returnScreen="v10s33_centeraisle")

    # Deer Girl 3
    imagebutton:
        pos (0, 0)
        idle "images/v10/scene 33/fr6deergirl3.webp"
        hover "images/v10/scene 33/fr6deergirl3hover.webp"
        if not v10s33_deergirl3:
            action Jump("v10s33_deergirl31")
        else:
            action Call("freeRoamSpokenToo", backgroundImg=v10s33_background, returnScreen="v10s33_centeraisle")
    
    # Ryan
    if not v10s33_ryan:
        imagebutton:
            pos (0, 0)
            idle "images/v10/scene 33/fr6ryan.webp"
            hover "images/v10/scene 33/fr6ryanhover.webp"
            if not v10s33_ryan:
                action Jump("v10s33_ryan1")
            else:
                action Call("freeRoamSpokenToo", backgroundImg=v10s33_background, returnScreen="v10s33_centeraisle")

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


screen v10s33_mudwrestling():
    tag tag_freeRoam

    # Background
    if v10s33_toldChloe:
        $ v10s33_background = "images/v10/scene 33/fr6mudwrestlingwithnoraandchloe.webp"
    else:
        $ v10s33_background = "images/v10/scene 33/fr6mudwrestling.webp"

    add v10s33_background

    # Amber
    imagebutton: 
        pos (0, 0)
        idle "images/v10/scene 33/fr6amber.webp"
        hover "images/v10/scene 33/fr6amberhover.webp"
        if not v10s33_amber:
            action Jump("v10s33_amber1")
        else:
            action Call("freeRoamSpokenToo", backgroundImg=v10s33_background, returnScreen="v10s33_mudwrestling")
    
    # Autumn
    imagebutton: 
        pos (0, 0)
        idle "images/v10/scene 33/fr6autumn.webp"
        hover "images/v10/scene 33/fr6autumnhover.webp"
        if not v10s33_autumn:
            action Jump("v10s33_autumn1")
        else:
            action Show("endFreeRoamConfirm", backgroundImg=v10s33_background, continueLabel="v10_autumn_announcement")

    # Centre Aisle - Bottom
    imagebutton:
        align (0.5, 1.0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4bottomhover.webp"
        action Show("v10s33_centeraisle")