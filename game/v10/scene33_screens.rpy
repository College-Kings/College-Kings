screen v10s33_entrance():
    tag tag_freeRoam

    # Background
    if not v10s33_toldChloe and v10s33_riley and not v10s33_ryan:
        add "images/v10/scene 33/Ent1.webp"
    if v10s33_toldChloe and v10s33_riley and not v10s33_ryan:
        add "images/v10/scene 33/Ent2.webp"
    if v10s33_toldChloe and not v10s33_riley and not v10s33_ryan:
        add "images/v10/scene 33/Ent3.webp"
    if not v10s33_toldChloe and v10s33_riley and v10s33_ryan:
        add "images/v10/scene 33/Ent4.webp"
    if not v10s33_toldChloe and not v10s33_riley and v10s33_ryan:
        add "images/v10/scene 33/Ent5.webp"
    if v10s33_toldChloe not v10s33_riley and v10s33_ryan:
        add "images/v10/scene 33/Ent6.webp"
    if not v10s33_toldChloe and not v10s33_riley and not v10s33_ryan:
        add "images/v10/scene 33/Ent7.webp"
    if v10s33_toldChloe and v10s33_riley and v10s33_ryan:
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

screen v10s33_cakestatue():
    tag tag_freeRoam
    
    # Background
    if v10s33_laurenBakeSale:
        add "images/v10/scene 33/fr6cake.webp"
    else:
        add "images/v10/scene 33/fr6statue.webp"

    # Lauren - Bake sale
    if v10s33_laurenBakeSale:
        imagebutton:
            pos (0, 0)
            idle "images/v10/scene 33/fr6laurenbake.webp"
            hover "images/v10/scene 33/fr6laurenbakehover.webp"
            if not v10s33_lauren:
                action Jump("v10s33_laurenbake1")
            else:
                action Call("freeRoamSpokenToo", returnScreen="v10s33_cakestatue")

    # Lauren - Statue
    else:
        imagebutton:
            pos (0, 0)
            idle "images/v10/scene 33/fr6laurenstatue.webp"
            hover "images/v10/scene 33/fr6laurenstatuehover.webp"
            if not v10s33_lauren:
                action Jump("v10s33_laurenstatue1")
            else:
                action Call("freeRoamSpokenToo", returnScreen="v10s33_cakestatue")

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
        add "images/v10/scene 33/fr6benchchloenoraatmudwrestling.webp"
    else:
        add "images/v10/scene 33/fr6bench.webp"

    # Emily
    imagebutton: 
        pos (0, 0)
        idle "images/v10/scene 33/fr6emily.webp"
        hover "images/v10/scene 33/fr6emilyhover.webp"
        if not v10s33_emily:
            action Jump("v10s33_emily1")
        else:
            action Call("freeRoamSpokenToo", returnScreen="v10s33_bench")

    #LOCATIONS:
        #centeraisle (left)
        #cakestatue (bottom)
  
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

    if v10s33_ryan:
        add "images/v10/scene 33/fr6toiletwithryan.webp" #IMAGE NEEDS TO BE RENDERED
    else:
        add "images/v10/scene 33/fr6toilet.webp" #IMAGE NEEDS TO BE RENDERED

    #PEOPLE:
    imagebutton: # Evelyn
        pos (0, 0)
        idle "images/v10/scene 33/fr6evelyn.webp"
        hover "images/v10/scene 33/fr6evelynhover.webp"
        if not v10s33_evelyn:
            action Jump("v10s33_evelyn1")
        else:
            action Call("freeRoamSpokenToo", returnScreen="v10s33_toilet")

    if v10s33_ryan:            
        imagebutton: # Toilet Ryan
            pos (0, 0)
            idle "images/v10/scene 33/fr6toiletryan.webp"
            hover "images/v10/scene 33/fr6toiletryanhover.webp"
            if not v10s33_ryanb:
                action Jump("v10s33_toiletryan1")
            else:
                action Call("freeRoamSpokenToo", returnScreen="v10s33_toilet")

    #LOCATIONS:
        #bodypaint (right)
        #entrance (bottom)

    imagebutton:
        align (1.0, 0.5)
        idle "images/v10/scene 33/freeroamidle_hori.webp"
        hover "images/v10/scene 33/fr4righthover.webp"
        action Show("v10s33_bodypaint")

    imagebutton:
        align (0.5, 1.0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4bottomhover.webp"
        action Show("v10s33_entrance")

screen v10s33_bodypaint():
    tag tag_freeRoam

    if v10s33_riley:
        add "images/v10/scene 33/fr6bodypaintnoriley.webp" #IMAGE NEEDS TO BE RENDERED
    else:
        add "images/v10/scene 33/fr6bodypaint.webp" #IMAGE NEEDS TO BE RENDERED

    #PEOPLE:
    imagebutton: # Ms Rose
        pos (0, 0)
        idle "images/v10/scene 33/fr6msrose.webp"
        hover "images/v10/scene 33/fr6msrosehover.webp"
        if not v10s33_msRose:
            action Jump("v10s33_msrose1")
        else:
            action Call("freeRoamSpokenToo", returnScreen="v10s33_bodypaint")
    imagebutton: # Lindsey
        pos (0, 0)
        idle "images/v10/scene 33/fr6lindsey.webp"
        hover "images/v10/scene 33/fr6lindseyhover.webp"
        if not v10s33_lindsey:
            action Jump("v10s33_lindsey1")
        else:
            action Call("freeRoamSpokenToo", returnScreen="v10s33_bodypaint")
    #LOCATIONS:
        #thrift (top)
        #toilet (bottom)

    imagebutton:
        xalign 0.5
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4tophover.webp"
        action Show("v10s33_thrift")

    imagebutton:
        align (0.5, 1.0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4bottomhover.webp"
        action Show("v10s33_toilet")

screen v10s33_thrift():
    tag tag_freeRoam

    if v10s33_riley:
        add "images/v10/scene 33/fr6thriftnoriley.webp" #IMAGE NEEDS TO BE RENDERED
    else:
        add "images/v10/scene 33/fr6thrift.webp" #IMAGE NEEDS TO BE RENDERED

    #PEOPLE:
    imagebutton: # Deer Girl 4
        pos (0, 0)
        idle "images/v10/scene 33/fr6deergirl4.webp"
        hover "images/v10/scene 33/fr6deergirl4hover.webp"
        action Jump("v10s33_deergirl41")

    if not v10s33_riley:                
        imagebutton: # Riley
            pos (0, 0)
            idle "images/v10/scene 33/fr6riley.webp"
            hover "images/v10/scene 33/fr6rileyhover.webp"
            action Jump("v10s33_riley1")

    #LOCATIONS:
        #bodypaint (bottom)
        #stagefromleft (top)

    imagebutton:
        xalign 0.5
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4tophover.webp"
        action Show("v10s33_stagefromleft")

    imagebutton:
        align (0.5, 1.0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4bottomhover.webp"
        action Show("v10s33_bodypaint")

screen v10s33_stagefromleft():
    tag tag_freeRoam

    if v10s33_riley:
        if v10s33_toldChloe:
            add "images/v10/scene 33/fr6stagefromleftchloeandnoraatmudwrestlingwithrileyatstage.webp" #IMAGE NEEDS TO BE RENDERED
        else:
            add "images/v10/scene 33/fr6stagewithrileyatstage.webp" #IMAGE NEEDS TO BE RENDERED
    else:
        if v10s33_toldChloe:
            add "images/v10/scene 33/fr6stagefromleftchloeandnoraatmudwrestling.webp" #IMAGE NEEDS TO BE RENDERED
        else:
            add "images/v10/scene 33/fr6stageleft.webp" #IMAGE NEEDS TO BE RENDERED

    #PEOPLE:
        #none

    #LOCATIONS:
        #thirft (bottom)
        #stage (top)

    imagebutton:
        xalign 0.5
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4tophover.webp"
        action Show("v10s33_stage")

    imagebutton:
        align (0.5, 1.0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4bottomhover.webp"
        action Show("v10s33_thrift")

screen v10s33_stage():
    tag tag_freeRoam

    if v10s33_riley:
        add "images/v10/scene 33/fr6stagewithriley.webp" #IMAGE NEEDS TO BE RENDERED
    else:
        add "images/v10/scene 33/fr6stage.webp" #IMAGE NEEDS TO BE RENDERED

    #PEOPLE:
    if not v10s33_riley:   
        imagebutton: # Aubrey
            pos (0, 0)
            idle "images/v10/scene 33/fr6aubrey.webp"
            hover "images/v10/scene 33/fr6aubreyhover.webp"
            if not v10s33_aubrey:
                action Jump("v10s33_aubrey1")
            else:
                action Call("freeRoamSpokenToo", returnScreen="v10s33_stage")

    if v10s33_riley:   
        imagebutton: # Aubrey & Riley
            pos (0, 0)
            idle "images/v10/scene 33/fr6aubreyriley.webp"
            hover "images/v10/scene 33/fr6aubreyrileyhover.webp"
            if not v10s33_aubreyriley:
                action Jump("v10s33_aubreyriley1")
            else:
                action Call("freeRoamSpokenToo", returnScreen="v10s33_stage")
    imagebutton: # Deer girl 1
        pos (0, 0)
        idle "images/v10/scene 33/fr6deergirl1.webp"
        hover "images/v10/scene 33/fr6deergirl1hover.webp"
        if not v10s33_deergirl1:
            action Jump("v10s33_deergirl11")
        else:
            action Call("freeRoamSpokenToo", returnScreen="v10s33_stage")

    #LOCATIONS:
        #stagefromleft (left)
        #bagtoss (right)
        #centeraisle (bottom)

    imagebutton:
        yalign 0.5
        idle "images/v10/scene 33/freeroamidle_hori.webp"
        hover "images/v10/scene 33/fr4lefthover.webp"
        action Show("v10s33_stagefromleft")

    imagebutton:
        align (1.0, 0.5)
        idle "images/v10/scene 33/freeroamidle_hori.webp"
        hover "images/v10/scene 33/fr4righthover.webp"
        action Show("v10s33_bagtoss")

    imagebutton:
        align (0.5, 1.0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4bottomhover.webp"
        action Show("v10s33_centeraisle")

screen v10s33_bagtoss():
    tag tag_freeRoam

    if v10s33_toldChloe:
        add "images/v10/scene 33/fr6bagtossnonora.webp" #IMAGE NEEDS TO BE RENDERED
    else:
        add "images/v10/scene 33/fr6bagtoss.webp" #IMAGE NEEDS TO BE RENDERED

    #PEOPLE:

    imagebutton: # Deer Girl 2
        pos (0, 0)
        idle "images/v10/scene 33/fr6deergirl2.webp"
        hover "images/v10/scene 33/fr6deergirl2.webp"
        if not v10s33_deergirl2:
            action Jump("v10s33_deergirl21")
        else:
            action Call("freeRoamSpokenToo", returnScreen="v10s33_bagtoss")
    imagebutton: # Chris
        pos (0, 0)
        idle "images/v10/scene 33/fr6chris.webp"
        hover "images/v10/scene 33/fr6chrishover.webp"
        if not v10s33_chris:
            action Jump("v10s33_chris1")
        else:
            action Call("freeRoamSpokenToo", returnScreen="v10s33_bagtoss")
    if not v10s33_toldChloe:
        imagebutton: # Nora
            pos (0, 0)
            idle "images/v10/scene 33/fr6nora.webp"
            hover "images/v10/scene 33/fr6norahover.webp"
            if not v10s33_nora:
                action Jump("v10s33_nora1")
            else:
                action Call("freeRoamSpokenToo", returnScreen="v10s33_bagtoss")

    #LOCATIONS:
        #stage (bottom)

    imagebutton:
        align (0.5, 1.0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4bottomhover.webp"
        action Show("v10s33_stage")

screen v10s33_centeraisle():
    tag tag_freeRoam

    if v10s33_toldChloe:
        if v10s33_riley:
            if v10s33_ryan:
                add "images/v10/scene 33/Mid8.webp" #IMAGE NEEDS TO BE RENDERED
            else:
                add "images/v10/scene 33/Mid2.webp" #IMAGE NEEDS TO BE RENDERED
        else:
            if v10s33_ryan:
                add "images/v10/scene 33/Mid6.webp" #IMAGE NEEDS TO BE RENDERED
            else:
                add "images/v10/scene 33/Mid3.webp" #IMAGE NEEDS TO BE RENDERED
    else:
        if v10s33_riley:
            if v10s33_ryan:
                add "images/v10/scene 33/Mid4.webp" #IMAGE NEEDS TO BE RENDERED
            else:
                add "images/v10/scene 33/Mid1.webp" #IMAGE NEEDS TO BE RENDERED
        else:
            if v10s33_ryan:
                add "images/v10/scene 33/Mid5.webp" #IMAGE NEEDS TO BE RENDERED
            else:
                add "images/v10/scene 33/Mid7.webp" #IMAGE NEEDS TO BE RENDERED

    #PEOPLE:
    if not v10s33_toldChloe:
        imagebutton: # chloe
            pos (0, 0)
            idle "images/v10/scene 33/fr6chloe.webp"
            hover "images/v10/scene 33/fr6chloehover.webp"
            if not v10s33_chloe:
                action Jump("v10s33_chloe1")
            else:
                action Call("freeRoamSpokenToo", returnScreen="v10s33_centeraisle")

    imagebutton: # Deer Girl 3
        pos (0, 0)
        idle "images/v10/scene 33/fr6deergirl3.webp"
        hover "images/v10/scene 33/fr6deergirl3hover.webp"
        if not v10s33_deergirl3:
            action Jump("v10s33_deergirl31")
        else:
            action Call("freeRoamSpokenToo", returnScreen="v10s33_centeraisle")
    
    if not v10s33_ryan:
        imagebutton: # Ryan
            pos (0, 0)
            idle "images/v10/scene 33/fr6ryan.webp"
            hover "images/v10/scene 33/fr6ryanhover.webp"
            if not v10s33_ryan:
                action Jump("v10s33_ryan1")
            else:
                action Call("freeRoamSpokenToo", returnScreen="v10s33_centeraisle")

    #LOCATIONS:
        #stage (top)
        #mud wrestling (right)
        #entrance (bottom)

    imagebutton:
        xalign 0.5
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4tophover.webp"
        action Show("v10s33_stage")

    imagebutton:
        align (1.0, 0.5)
        idle "images/v10/scene 33/freeroamidle_hori.webp"
        hover "images/v10/scene 33/fr4righthover.webp"
        action Show("v10s33_mudwrestling")

    imagebutton:
        align (0.5, 1.0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4bottomhover.webp"
        action Show("v10s33_entrance")

screen v10s33_mudwrestling():
    tag tag_freeRoam

    if v10s33_toldChloe:
        add "images/v10/scene 33/fr6mudwrestlingwithnoraandchloe.webp" #IMAGE NEEDS TO BE RENDERED
    else:
        add "images/v10/scene 33/fr6mudwrestling.webp" #IMAGE NEEDS TO BE RENDERED

    #PEOPLE:
    imagebutton: # Amber
        pos (0, 0)
        idle "images/v10/scene 33/fr6amber.webp"
        hover "images/v10/scene 33/fr6amberhover.webp"
        if not v10s33_amber:
            action Jump("v10s33_amber1")
        else:
            action Call("freeRoamSpokenToo", returnScreen="v10s33_mudwrestling")
        
    imagebutton: # Autumn
        pos (0, 0)
        idle "images/v10/scene 33/fr6autumn.webp"
        hover "images/v10/scene 33/fr6autumnhover.webp"
        if not v10s33_autumn:
            action Jump("v10s33_autumn1")
        else:
            action Show("endFreeRoamConfirm", continueLabel="v10_autumn_announcement")

    #LOCATIONS:
        #center aisle (bottom)

    imagebutton:
        align (0.5, 1.0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4bottomhover.webp"
        action Show("v10s33_centeraisle")