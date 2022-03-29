# SCENE 66: Transition Mc walks to College
# Locations: Main Entrance to School Campus
# Characters: MC (Outfit: 2)
# Time: Friday Evening

# can only get here from 61 (if helping Chloe with newspaper), 64 (chicks after spa day, not necessarily helping Chloe) or 65 (helping Chloe with newspaper)

label v16s66:
    if v14_help_chloe and not v16_chloe_newspaper: # -if Transitioning from Scene 64- (spa day
        scene v16s66_1 # TPP. MC (slight smile, mouth is closed, looking at Lindsey) and Lindsey (slight smile, mouth is open, looking at MC) approach the main entrance on campus
        with dissolve

        pause 0.75

    else: # -if Transitioning from Scene 65- (Design cover with Chloe)
        scene v16s66_2 # TPP. MC (slight smile, mouth is closed) is walking alone, approaching the main entrance on campus
        with dissolve

        u "(I hope I haven't missed the start of Polly's performance...)"

    jump v16s67 # -Transition to Scene 67-