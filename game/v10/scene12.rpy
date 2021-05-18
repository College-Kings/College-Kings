label v10_mc_clock_trans:
    if joinwolves:
        scene wOldClock10
        with dissolve

        pause 0.5

        scene wOldClock11
        with dissolve

        pause 0.5

        scene wOldClock12
        with dissolve

        pause 0.5

        scene wOldClock1
        with dissolve

        pause 0.5

        jump v10_wolves_redec
    
    else:
        scene aClock10
        with dissolve

        pause 0.5

        scene aClock11
        with dissolve

        pause 0.5

        scene aClock12
        with dissolve

        pause 0.5
        
        scene aClock1
        with dissolve

        pause 0.5

        jump v10_apes_samantha