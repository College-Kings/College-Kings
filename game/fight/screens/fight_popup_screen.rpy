screen fightPopup(fightMove):
    modal True
    
    use alert_template(_("Congratulations! You have learned a new fighting move: {{b}}{}{{/b}}.".format(fightMove))):

        textbutton _("OK"):
            action Return()

    if config_debug:
        timer 0.1 action Return()


screen fightDamage():
    if youDamage == 3:
        add "images/3 hits.webp"
    elif youDamage == 4:
        add "images/4 hits.webp"
    elif youDamage >= 5:
        add "images/5 hits.webp"