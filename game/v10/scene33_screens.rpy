screen v10cfr33_entrance():
    tag v10cfr33_freeRoam

    if v10cfr33_toldchloe:
        if v10cfr33_riley:
            if v10cfr33_ryan:
                add "images/v10/scene 33/Ent8.webp"
            else:
                add "images/v10/scene 33/Ent2.webp"
        else:
            if v10cfr33_ryan:
                add "images/v10/scene 33/Ent6.webp"
            else:
                add "images/v10/scene 33/Ent3.webp"
    else:
        if v10cfr33_riley:
            if v10cfr33_ryan:
                add "images/v10/scene 33/Ent4.webp"
            else:
                add "images/v10/scene 33/Ent1.webp"
        else:
            if v10cfr33_ryan:
                add "images/v10/scene 33/Ent5.webp"
            else:
                add "images/v10/scene 33/Ent7.webp"

    #PEOPLE:
        #none

    #LOCATIONS:
        #cakestatue (right)
        #toilet (left)
        # center aisle (top)

    imagebutton:
        align (1.0, 0.5)
        idle "images/v10/scene 33/freeroamidle_hori.webp"
        hover "images/v10/scene 33/fr4righthover.webp"
        action Show("v10cfr33_cakestatue")

    imagebutton:
        align (0, 0.5)
        idle "images/v10/scene 33/freeroamidle_hori.webp"
        hover "images/v10/scene 33/fr4lefthover.webp"
        action Show("v10cfr33_toilet")

    imagebutton:
        align (0.5, 0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4tophover.webp"
        action Show("v10cfr33_centeraisle")

screen v10cfr33_cakestatue():
    tag v10cfr33_freeRoam
    
    if lauren_bake_sale:
        add "images/v10/scene 33/fr6cake.webp" #IMAGE NEEDS TO BE RENDERED
    else:
        add "images/v10/scene 33/fr6statue.webp" #IMAGE NEEDS TO BE RENDERED

    #PEOPLE:
    if lauren_bake_sale:
        imagebutton: # Lauren Bakesale
            pos (0, 0)
            idle "images/v10/scene 33/fr6laurenbake.webp"
            hover "images/v10/scene 33/fr6laurenbakehover.webp"
            if not v10cfr33_lauren:
                action Jump("v10cfr33_laurenbake1")
            else:
                action Call("freeRoamSpokenToo", returnScreen="v10cfr33_cakestatue")
              
                
    else:
        imagebutton: # Lauren Statue
            pos (0, 0)
            idle "images/v10/scene 33/fr6laurenstatue.webp"
            hover "images/v10/scene 33/fr6laurenstatuehover.webp"
            if not v10cfr33_lauren:
                action Jump("v10cfr33_laurenstatue1")
            else:
                action Call("freeRoamSpokenToo", returnScreen="v10cfr33_cakestatue")

    #LOCATIONS:
        #bench (left)
        #entrance (bottom)

    imagebutton:
        yalign 0.5
        idle "images/v10/scene 33/freeroamidle_hori.webp"
        hover "images/v10/scene 33/fr4lefthover.webp"
        action Show("v10cfr33_bench")

    imagebutton:
        align (0.5, 1.0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4bottomhover.webp"
        action Show("v10cfr33_entrance")

screen v10cfr33_bench():
    tag v10cfr33_freeRoam

    if v10cfr33_toldchloe:
        add "images/v10/scene 33/fr6benchchloenoraatmudwrestling.webp" #IMAGE NEEDS TO BE RENDERED
    else:
        add "images/v10/scene 33/fr6bench.webp" #IMAGE NEEDS TO BE RENDERED

    #PEOPLE:
    imagebutton: # Emily
        pos (0, 0)
        idle "images/v10/scene 33/fr6emily.webp"
        hover "images/v10/scene 33/fr6emilyhover.webp"
        if not v10cfr33_emily:
            action Jump("v10cfr33_emily1")
        else:
            action Call("freeRoamSpokenToo", returnScreen="v10cfr33_bench")

    #LOCATIONS:
        #centeraisle (left)
        #cakestatue (bottom)
  
    imagebutton:
        yalign 0.5
        idle "images/v10/scene 33/freeroamidle_hori.webp"
        hover "images/v10/scene 33/fr4lefthover.webp"
        action Show("v10cfr33_centeraisle")

    imagebutton:
        align (0.5, 1.0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4bottomhover.webp"
        action Show("v10cfr33_cakestatue")
        
          
screen v10cfr33_toilet():
    tag v10cfr33_freeRoam

    if v10cfr33_ryan:
        add "images/v10/scene 33/fr6toiletwithryan.webp" #IMAGE NEEDS TO BE RENDERED
    else:
        add "images/v10/scene 33/fr6toilet.webp" #IMAGE NEEDS TO BE RENDERED

    #PEOPLE:
    imagebutton: # Evelyn
        pos (0, 0)
        idle "images/v10/scene 33/fr6evelyn.webp"
        hover "images/v10/scene 33/fr6evelynhover.webp"
        if not v10cfr33_evelyn:
            action Jump("v10cfr33_evelyn1")
        else:
            action Call("freeRoamSpokenToo", returnScreen="v10cfr33_toilet")

    if v10cfr33_ryan:            
        imagebutton: # Toilet Ryan
            pos (0, 0)
            idle "images/v10/scene 33/fr6toiletryan.webp"
            hover "images/v10/scene 33/fr6toiletryanhover.webp"
            if not v10cfr33_ryanb:
                action Jump("v10cfr33_toiletryan1")
            else:
                action Call("freeRoamSpokenToo", returnScreen="v10cfr33_toilet")

    #LOCATIONS:
        #bodypaint (right)
        #entrance (bottom)

    imagebutton:
        align (1.0, 0.5)
        idle "images/v10/scene 33/freeroamidle_hori.webp"
        hover "images/v10/scene 33/fr4righthover.webp"
        action Show("v10cfr33_bodypaint")

    imagebutton:
        align (0.5, 1.0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4bottomhover.webp"
        action Show("v10cfr33_entrance")

screen v10cfr33_bodypaint():
    tag v10cfr33_freeRoam

    if v10cfr33_riley:
        add "images/v10/scene 33/fr6bodypaintnoriley.webp" #IMAGE NEEDS TO BE RENDERED
    else:
        add "images/v10/scene 33/fr6bodypaint.webp" #IMAGE NEEDS TO BE RENDERED

    #PEOPLE:
    imagebutton: # Ms Rose
        pos (0, 0)
        idle "images/v10/scene 33/fr6msrose.webp"
        hover "images/v10/scene 33/fr6msrosehover.webp"
        if not v10cfr33_msrose:
            action Jump("v10cfr33_msrose1")
        else:
            action Call("freeRoamSpokenToo", returnScreen="v10cfr33_bodypaint")
    imagebutton: # Lindsey
        pos (0, 0)
        idle "images/v10/scene 33/fr6lindsey.webp"
        hover "images/v10/scene 33/fr6lindseyhover.webp"
        if not v10cfr33_lindsey:
            action Jump("v10cfr33_lindsey1")
        else:
            action Call("freeRoamSpokenToo", returnScreen="v10cfr33_bodypaint")
    #LOCATIONS:
        #thrift (top)
        #toilet (bottom)

    imagebutton:
        xalign 0.5
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4tophover.webp"
        action Show("v10cfr33_thrift")

    imagebutton:
        align (0.5, 1.0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4bottomhover.webp"
        action Show("v10cfr33_toilet")

screen v10cfr33_thrift():
    tag v10cfr33_freeRoam

    if v10cfr33_riley:
        add "images/v10/scene 33/fr6thriftnoriley.webp" #IMAGE NEEDS TO BE RENDERED
    else:
        add "images/v10/scene 33/fr6thrift.webp" #IMAGE NEEDS TO BE RENDERED

    #PEOPLE:
    imagebutton: # Deer Girl 4
        pos (0, 0)
        idle "images/v10/scene 33/fr6deergirl4.webp"
        hover "images/v10/scene 33/fr6deergirl4hover.webp"
        action Jump("v10cfr33_deergirl41")

    if not v10cfr33_riley:                
        imagebutton: # Riley
            pos (0, 0)
            idle "images/v10/scene 33/fr6riley.webp"
            hover "images/v10/scene 33/fr6rileyhover.webp"
            action Jump("v10cfr33_riley1")

    #LOCATIONS:
        #bodypaint (bottom)
        #stagefromleft (top)

    imagebutton:
        xalign 0.5
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4tophover.webp"
        action Show("v10cfr33_stagefromleft")

    imagebutton:
        align (0.5, 1.0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4bottomhover.webp"
        action Show("v10cfr33_bodypaint")

screen v10cfr33_stagefromleft():
    tag v10cfr33_freeRoam

    if v10cfr33_riley:
        if v10cfr33_toldchloe:
            add "images/v10/scene 33/fr6stagefromleftchloeandnoraatmudwrestlingwithrileyatstage.webp" #IMAGE NEEDS TO BE RENDERED
        else:
            add "images/v10/scene 33/fr6stagewithrileyatstage.webp" #IMAGE NEEDS TO BE RENDERED
    else:
        if v10cfr33_toldchloe:
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
        action Show("v10cfr33_stage")

    imagebutton:
        align (0.5, 1.0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4bottomhover.webp"
        action Show("v10cfr33_thrift")

screen v10cfr33_stage():
    tag v10cfr33_freeRoam

    if v10cfr33_riley:
        add "images/v10/scene 33/fr6stagewithriley.webp" #IMAGE NEEDS TO BE RENDERED
    else:
        add "images/v10/scene 33/fr6stage.webp" #IMAGE NEEDS TO BE RENDERED

    #PEOPLE:
    if not v10cfr33_riley:   
        imagebutton: # Aubrey
            pos (0, 0)
            idle "images/v10/scene 33/fr6aubrey.webp"
            hover "images/v10/scene 33/fr6aubreyhover.webp"
            if not v10cfr33_aubrey:
                action Jump("v10cfr33_aubrey1")
            else:
                action Call("freeRoamSpokenToo", returnScreen="v10cfr33_stage")
    if v10cfr33_riley:   
        imagebutton: # Aubrey & Riley
            pos (0, 0)
            idle "images/v10/scene 33/fr6aubreyriley.webp"
            hover "images/v10/scene 33/fr6aubreyrileyhover.webp"
            if not v10cfr33_aubreyriley:
                action Jump("v10cfr33_aubreyriley1")
            else:
                action Call("freeRoamSpokenToo", returnScreen="v10cfr33_stage")
    imagebutton: # Deer girl 1
        pos (0, 0)
        idle "images/v10/scene 33/fr6deergirl1.webp"
        hover "images/v10/scene 33/fr6deergirl1hover.webp"
        if not v10cfr33_deergirl1:
            action Jump("v10cfr33_deergirl11")
        else:
            action Call("freeRoamSpokenToo", returnScreen="v10cfr33_stage")

    #LOCATIONS:
        #stagefromleft (left)
        #bagtoss (right)
        #centeraisle (bottom)

    imagebutton:
        yalign 0.5
        idle "images/v10/scene 33/freeroamidle_hori.webp"
        hover "images/v10/scene 33/fr4lefthover.webp"
        action Show("v10cfr33_stagefromleft")

    imagebutton:
        align (1.0, 0.5)
        idle "images/v10/scene 33/freeroamidle_hori.webp"
        hover "images/v10/scene 33/fr4righthover.webp"
        action Show("v10cfr33_bagtoss")

    imagebutton:
        align (0.5, 1.0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4bottomhover.webp"
        action Show("v10cfr33_centeraisle")

screen v10cfr33_bagtoss():
    tag v10cfr33_freeRoam

    if v10cfr33_toldchloe:
        add "images/v10/scene 33/fr6bagtossnonora.webp" #IMAGE NEEDS TO BE RENDERED
    else:
        add "images/v10/scene 33/fr6bagtoss.webp" #IMAGE NEEDS TO BE RENDERED

    #PEOPLE:

    imagebutton: # Deer Girl 2
        pos (0, 0)
        idle "images/v10/scene 33/fr6deergirl2.webp"
        hover "images/v10/scene 33/fr6deergirl2.webp"
        if not v10cfr33_deergirl2:
            action Jump("v10cfr33_deergirl21")
        else:
            action Call("freeRoamSpokenToo", returnScreen="v10cfr33_bagtoss")
    imagebutton: # Chris
        pos (0, 0)
        idle "images/v10/scene 33/fr6chris.webp"
        hover "images/v10/scene 33/fr6chrishover.webp"
        if not v10cfr33_chris:
            action Jump("v10cfr33_chris1")
        else:
            action Call("freeRoamSpokenToo", returnScreen="v10cfr33_bagtoss")
    if not v10cfr33_toldchloe:
        imagebutton: # Nora
            pos (0, 0)
            idle "images/v10/scene 33/fr6nora.webp"
            hover "images/v10/scene 33/fr6norahover.webp"
            if not v10cfr33_nora:
                action Jump("v10cfr33_nora1")
            else:
                action Call("freeRoamSpokenToo", returnScreen="v10cfr33_bagtoss")

    #LOCATIONS:
        #stage (bottom)

    imagebutton:
        align (0.5, 1.0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4bottomhover.webp"
        action Show("v10cfr33_stage")

screen v10cfr33_centeraisle():
    tag v10cfr33_freeRoam

    if v10cfr33_toldchloe:
        if v10cfr33_riley:
            if v10cfr33_ryan:
                add "images/v10/scene 33/Mid8.webp" #IMAGE NEEDS TO BE RENDERED
            else:
                add "images/v10/scene 33/Mid2.webp" #IMAGE NEEDS TO BE RENDERED
        else:
            if v10cfr33_ryan:
                add "images/v10/scene 33/Mid6.webp" #IMAGE NEEDS TO BE RENDERED
            else:
                add "images/v10/scene 33/Mid3.webp" #IMAGE NEEDS TO BE RENDERED
    else:
        if v10cfr33_riley:
            if v10cfr33_ryan:
                add "images/v10/scene 33/Mid4.webp" #IMAGE NEEDS TO BE RENDERED
            else:
                add "images/v10/scene 33/Mid1.webp" #IMAGE NEEDS TO BE RENDERED
        else:
            if v10cfr33_ryan:
                add "images/v10/scene 33/Mid5.webp" #IMAGE NEEDS TO BE RENDERED
            else:
                add "images/v10/scene 33/Mid7.webp" #IMAGE NEEDS TO BE RENDERED

    #PEOPLE:
    if not v10cfr33_toldchloe:
        imagebutton: # chloe
            pos (0, 0)
            idle "images/v10/scene 33/fr6chloe.webp"
            hover "images/v10/scene 33/fr6chloehover.webp"
            if not v10cfr33_chloe:
                action Jump("v10cfr33_chloe1")
            else:
                action Call("freeRoamSpokenToo", returnScreen="v10cfr33_centeraisle")

    imagebutton: # Deer Girl 3
        pos (0, 0)
        idle "images/v10/scene 33/fr6deergirl3.webp"
        hover "images/v10/scene 33/fr6deergirl3hover.webp"
        if not v10cfr33_deergirl3:
            action Jump("v10cfr33_deergirl31")
        else:
            action Call("freeRoamSpokenToo", returnScreen="v10cfr33_centeraisle")
    
    if not v10cfr33_ryan:
        imagebutton: # Ryan
            pos (0, 0)
            idle "images/v10/scene 33/fr6ryan.webp"
            hover "images/v10/scene 33/fr6ryanhover.webp"
            if not v10cfr33_ryan:
                action Jump("v10cfr33_ryan1")
            else:
                action Call("freeRoamSpokenToo", returnScreen="v10cfr33_centeraisle")

    #LOCATIONS:
        #stage (top)
        #mud wrestling (right)
        #entrance (bottom)

    imagebutton:
        xalign 0.5
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4tophover.webp"
        action Show("v10cfr33_stage")

    imagebutton:
        align (1.0, 0.5)
        idle "images/v10/scene 33/freeroamidle_hori.webp"
        hover "images/v10/scene 33/fr4righthover.webp"
        action Show("v10cfr33_mudwrestling")

    imagebutton:
        align (0.5, 1.0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4bottomhover.webp"
        action Show("v10cfr33_entrance")

screen v10cfr33_mudwrestling():
    tag v10cfr33_freeRoam

    if v10cfr33_toldchloe:
        add "images/v10/scene 33/fr6mudwrestlingwithnoraandchloe.webp" #IMAGE NEEDS TO BE RENDERED
    else:
        add "images/v10/scene 33/fr6mudwrestling.webp" #IMAGE NEEDS TO BE RENDERED

    #PEOPLE:
    imagebutton: # Amber
        pos (0, 0)
        idle "images/v10/scene 33/fr6amber.webp"
        hover "images/v10/scene 33/fr6amberhover.webp"
        if not v10cfr33_amber:
            action Jump("v10cfr33_amber1")
        else:
            action Call("freeRoamSpokenToo", returnScreen="v10cfr33_mudwrestling")
        
    imagebutton: # Autumn
        pos (0, 0)
        idle "images/v10/scene 33/fr6autumn.webp"
        hover "images/v10/scene 33/fr6autumnhover.webp"
        if not v10cfr33_autumn:
            action Jump("v10cfr33_autumn1")
        else:
            action Show("endFreeRoamConfirm", continueLabel="v10_autumn_announcement")

    #LOCATIONS:
        #center aisle (bottom)

    imagebutton:
        align (0.5, 1.0)
        idle "images/v10/scene 33/freeroamidle_vert.webp"
        hover "images/v10/scene 33/fr4bottomhover.webp"
        action Show("v10cfr33_centeraisle")