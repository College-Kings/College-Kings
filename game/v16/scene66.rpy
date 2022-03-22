# SCENE 66: Transition Mc walks to College
# Locations: Main Entrance to School Campus
# Characters: MC (Outfit: 2)
# Time: Evening


label v16s66:

    if v14_help_chloe and chloe_spa_evening: # -if Transitioning from Scene 64-

        scene v16s66_1 # TPP. MC (slight smile, mouth is closed, looking at Lindsey) and Lindsey (slight smile, mouth is open, looking at MC) approach the main entrance on campus
        with dissolve

    else: # -if Transitioning from Scene 65-

        scene v16s66_2 # TPP. MC (slight smile, mouth is closed) is walking alone, approaching the main entrance on campus
        with dissolve

        u "(I hope I haven't missed the start of Polly's performance...)"

    jump v16s67 # -Transition to Scene 67-