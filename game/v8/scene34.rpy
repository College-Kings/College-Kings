# SCENE 34: TUESDAY AFTERNOON IN ROOM
# Locations: MC's room in Wolves house, MC's room in Apes house
# Characters: MC (outfit 2)
# Time: Tuesday afternoon
# Note: There's two versions for MC's renders in this scene. They're both the same essentially except one of them is in Wolves house (starting with "v8room20") and the other is in Apes house (starting with "v8room21")

init python:
    def v8s34_reply1():
        reputation.add_point(RepComponent.BOYFRIEND)
        chloe.messenger.newMessage(_("I bet you were"))
        chloe.messenger.addReply(_("I miss them"))
        chloe.messenger.newMessage(_("I know... we should def try again"))
        chloe.messenger.addReply(_("I'm on my way!"))
        chloe.messenger.newMessage(_("Hahaha"))
        chloe.messenger.addReply(_("Did you finish studying?"), v8s34_reply4)

    def v8s34_reply2():
        chloe.messenger.newMessage(_("Nothing. Bored."))
        chloe.messenger.addReply(_("Did you finish studying?"), v8s34_reply4)

    def v8s34_reply3():
        chloe.messenger.newMessage(_("Good. Bored. You?"))
        chloe.messenger.addReply(_("Same!"))
        chloe.messenger.addReply(_("Did you finish studying?"), v8s34_reply4)

    def v8s34_reply4():
        chloe.messenger.newMessage(_("Can't say it's all done, but I sure am!"))
        if ending == "chloe":
            chloe.messenger.addReply(_("So when can I see you again?"), v8s34_reply5)

        else:
            chloe.messenger.addReply(_("I'm actually getting hungry. Wanna go grab a bite?"), v8s34_reply6)
            chloe.messenger.addReply(_("I better get back to it. I have so much work to get done. Just wanted to check on you and see how you're doing."), v8s34_reply7)

    def v8s34_reply5():
        setattr(store, "chloeSteakHouse", True)
        reputation.add_point(RepComponent.BOYFRIEND)
        chloe.messenger.newMessage(_("Um... how's now? ;)"))
        chloe.messenger.addReply(_("Now's perfect! Should I cum to your place or you wanna cum here? ;)"))
        chloe.messenger.newMessage(_("I was thinking more along the lines of food. I'm hungry!"))
        chloe.messenger.addReply(_("Well I got something to fill your mouth up"))
        chloe.messenger.newMessage(_("Maybe after real food :P"))
        chloe.messenger.addReply(_("What are you in the mood for? Lady's choice"), v8s34_reply8)

    def v8s34_reply6():
        setattr(store, "chloeSteakHouse", True)
        reputation.add_point(RepComponent.BOYFRIEND)
        chloe.messenger.newMessage(_("..."))
        chloe.messenger.addReply(_("As friends"))
        chloe.messenger.newMessage(_("Ok, yeah. I'm actually starving!"))
        chloe.messenger.addReply(_("What are you in the mood for? Lady's choice"), v8s34_reply8)

    def v8s34_reply7():
        chloe.messenger.newMessage(_("It was nice talking to you"))
        chloe.messenger.addReply(_("You too"))

    def v8s34_reply8():
        chloe.messenger.newMessage(_("There's a new Japanese place right down the road"))
        chloe.messenger.addReply(_("Sounds delicious. Meet you there!"))

label v8_tues_noon:
    if chloe.relationship <= Relationship.MAD:
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
        $ chloe.messenger.addReply(_("Hey, sexy :* Haven't seen you in a while"))
        $ chloe.messenger.newMessage(_("OMG! I was just thinking about you!"))
        $ chloe.messenger.addReply(_("I was thinking about you too"))
        $ chloe.messenger.newMessage(_("Awww!"))
        $ chloe.messenger.addReply(_("I was thinking about your lips :*"), v8s34_reply1)
        $ chloe.messenger.addReply(_("Whatcha been up to?"), v8s34_reply2)
    else:
        $ chloe.messenger.addReply(_("Hey, how you been?"), v8s34_reply3)

label phn_chloe13:
    if chloe.messenger.replies:
        call screen phone
    if chloe.messenger.replies:
        u "(I should talk to Chloe.)"
        jump phn_chloe13

    if chloeSteakHouse:
        stop music fadeout 3
        u "(Guess I'm meeting Chloe.)"
        jump steak_w_chloe

    else:
        u "(I should check in with Julia.)"
        
    jump v8_julia_call