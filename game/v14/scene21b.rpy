# SCENE 21b: Show the sky changing from midday to evening
# Locations: Window
# Characters: None
# Time: Midday

label v14s21b:
    scene v14s21b_1 # TPP. Show the sky, it's midday
    with dissolve

    pause 1

    scene v14s21b_1a # TPP. Show the sky, it's now evening
    with Fade(1,1,1)

    pause 1

    if v14_help_lindsey and not v14_talk_to_chris:
        jump v14s22

    elif v14_talk_to_chris:
        jump v14s23

    else:
        jump v14s24