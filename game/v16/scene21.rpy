# SCENE 21: Transition MC walking to Lew's or Strip Club
# Locations: Street
# Characters: MC (Outfit: 5)
# Time: Night

label v16s21:
    scene v16s21_1 # TPP. MC walking along the street, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v16s21_2 # TPP. MC walking along the street, different place now, slight smile, mouth closed
    with dissolve

    pause 0.75

    if v14_amber_clean:
        jump v16s22

    else:
        jump v16s23