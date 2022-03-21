# SCENE 21b: Show the sky changing from midday to evening
# Locations: Window
# Characters: None
# Time: Midday

init python:
    def v14_beth_simplr():
        beth.simplr.newMessage("The best kind. Bye wiener boy!")
        simplr_app.contacts.remove(beth.simplr)

label v14s21b:
    play music "music/v13/Track Scene 45.mp3" fadein 2

    scene v14s21b_1 # TPP. Show the sky, it's midday
    with dissolve

    pause 1

    if beth.simplr in simplr_app.contacts:
        $ beth.simplr.newMessage("Oh, my bad... I thought you were a really cute chick XD", force_send=True)
        $ beth.simplr.addReply(_("You thought I was a girl? Lmao, what kind of girls have you been talking to?"), v14_beth_simplr)
    elif beth.simplr in simplr_app.pending_contacts:
        $ beth.simplr.removeContact()

    scene v14s21b_1a # TPP. Show the sky, it's now evening
    with Fade(1,1,1)

    pause 1

    stop music fadeout 3
    if v14_help_lindsey:
        jump v14s22

    elif v14_talk_to_chris:
        jump v14s23

    else:
        jump v14s24