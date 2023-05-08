label v10_mc_clock_trans:
    if mc.frat == Frat.WOLVES:
        scene woldclock10
        with dissolve

        pause 0.5

        scene woldclock11
        with dissolve

        pause 0.5

        scene woldclock12
        with dissolve

        pause 0.5

        scene woldclock1
        with dissolve

        pause 0.5

        jump v10_wolves_redec
    
    else:
        scene aclock10
        with dissolve

        pause 0.5

        scene aclock11
        with dissolve

        pause 0.5

        scene aclock12
        with dissolve

        pause 0.5
        
        scene aclock1
        with dissolve

        pause 0.5

        jump v10_apes_samantha