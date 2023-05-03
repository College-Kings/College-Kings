# SCENE 34: TUESDAY AFTERNOON IN ROOM
# Locations: MC's room in Wolves house, MC's room in Apes house
# Characters: MC (outfit 2)
# Time: Tuesday afternoon
# Note: There's two versions for MC's renders in this scene. They're both the same essentially except one of them is in Wolves house (starting with "v8room20") and the other is in Apes house (starting with "v8room21")

label v8_tues_noon:
    python:
        v8s34_reply8 = MessageBuilder(chloe)
        v8s34_reply8.new_message(_("There's a new Japanese place right down the road"))
        v8s34_reply8.add_reply(_("Sounds delicious. Meet you there!"))

        v8s34_reply6 = MessageBuilder(chloe)
        v8s34_reply6.set_variable("chloeSteakHouse", True)
        v8s34_reply6.add_function(reputation.add_point, RepComponent.BOYFRIEND)
        v8s34_reply6.new_message(_("..."))
        v8s34_reply6.add_reply(_("As friends"))
        v8s34_reply6.new_message(_("Ok, yeah. I'm actually starving!"))
        v8s34_reply6.add_reply(_("What are you in the mood for? Lady's choice"), v8s34_reply8)

        v8s34_reply7 = MessageBuilder(chloe)
        v8s34_reply7.new_message(_("It was nice talking to you"))
        v8s34_reply7.add_reply(_("You too"))

        v8s34_reply4 = MessageBuilder(chloe)
        v8s34_reply4.new_message(_("Can't say it's all done, but I sure am!"))

        if ending == "chloe":
            v8s34_reply4.add_reply(_("So when can I see you again?"), v8s34_reply5)
            v8s34_reply4.set_variable("chloeSteakHouse", True)
            v8s34_reply4.add_function(reputation.add_point, RepComponent.BOYFRIEND)
            v8s34_reply4.new_message(_("Um... how's now? ;)"))
            v8s34_reply4.add_reply(_("Now's perfect! Should I cum to your place or you wanna cum here? ;)"))
            v8s34_reply4.new_message(_("I was thinking more along the lines of food. I'm hungry!"))
            v8s34_reply4.add_reply(_("Well I got something to fill your mouth up"))
            v8s34_reply4.new_message(_("Maybe after real food :P"))
            v8s34_reply4.add_reply(_("What are you in the mood for? Lady's choice"), v8s34_reply8)

        else:
            v8s34_reply4.add_replies(
                Reply(_("I'm actually getting hungry. Wanna go grab a bite?"), v8s34_reply6),
                Reply(_("I better get back to it. I have so much work to get done. Just wanted to check on you and see how you're doing."), v8s34_reply7)
            )

        v8s34_reply1 = MessageBuilder(chloe)
        v8s34_reply1.add_function(reputation.add_point, RepComponent.BOYFRIEND)
        v8s34_reply1.new_message(_("I bet you were"))
        v8s34_reply1.add_reply(_("I miss them"))
        v8s34_reply1.new_message(_("I know... we should def try again"))
        v8s34_reply1.add_reply(_("I'm on my way!"))
        v8s34_reply1.new_message(_("Hahaha"))
        v8s34_reply1.add_reply(_("Did you finish studying?"), v8s34_reply4)

        v8s34_reply2 = MessageBuilder(chloe)
        v8s34_reply2.new_message(_("Nothing. Bored."))
        v8s34_reply2.add_reply(_("Did you finish studying?"), v8s34_reply4)

    if CharacterService.is_mad(chloe):
        if joinwolves:
            scene v8room20 # TPP. MC laying on bed in his room in Wolves house, looking at his phone, smiling a little, mouth closed
            with Fade(0.75, 0.25, 0.75)
            pause 0.5
            u "(I should check in with Julia.)"
        else:
            scene v8room21 # TPP. MC laying on bed in his room in Apes house, looking at his phone, smiling a little, mouth closed
            with Fade(0.75, 0.25, 0.75)
            pause 0.5
            u "(I should check in with Julia.)"
        jump v8_julia_call

    if joinwolves:
        scene v8room20
        with Fade(0.75, 0.25, 0.75)
        pause 0.5
        u "(I wonder how Chloe's doing. I should text her.)"
    else:
        scene v8room21
        with Fade(0.75, 0.25, 0.75)
        pause 0.5
        u "(I wonder how Chloe's doing. I should text her.)"

    if ending == "chloe":
        $ MessengerService.add_reply(chloe, _("Hey, sexy :* Haven't seen you in a while"))
        $ MessengerService.new_message(chloe, _("OMG! I was just thinking about you!"))
        $ MessengerService.add_reply(chloe, _("I was thinking about you too"))
        $ MessengerService.new_message(chloe, _("Awww!"))
        $ MessengerService.add_replies(chloe,
            Reply(_("I was thinking about your lips :*"), v8s34_reply1),
            Reply(_("Whatcha been up to?"), v8s34_reply2)
        )
    else:
        $ MessengerService.add_reply(chloe, _("Hey, how you been?"))
        $ MessengerService.new_message(chloe, _("Good. Bored. You?"))
        $ MessengerService.add_replies(chloe,
            Reply(_("Same!")),
            Reply(_("Did you finish studying?"), v8s34_reply4)
        )

    while MessengerService.has_replies(chloe):
        call screen phone
        if MessengerService.has_replies(chloe):
            u "(I should talk to Chloe.)"

    if chloeSteakHouse:
        stop music fadeout 3
        u "(Guess I'm meeting Chloe.)"
        jump steak_w_chloe

    else:
        u "(I should check in with Julia.)"
        
    jump v8_julia_call