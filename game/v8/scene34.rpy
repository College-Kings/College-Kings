# SCENE 34: TUESDAY AFTERNOON IN ROOM
# Locations: MC's room in Wolves house, MC's room in Apes house
# Characters: MC (outfit 2)
# Time: Tuesday afternoon
# Note: There's two versions for MC's renders in this scene. They're both the same essentially except one of them is in Wolves house (starting with "v8room20") and the other is in Apes house (starting with "v8room21")

init python:
    def v8s34_reply1():
        addPoint("bf")
        contact_Chloe.newMessage("I bet you were")
        contact_Chloe.addReply("I miss them")
        contact_Chloe.newMessage("I know... we should def try again")
        contact_Chloe.addReply("I'm on my way!")
        contact_Chloe.newMessage("Hahaha")
        contact_Chloe.addReply("Did you finish studying?", v8s34_reply4)

    def v8s34_reply2():
        contact_Chloe.newMessage("Nothing. Bored.")
        contact_Chloe.addReply("Did you finish studying?", v8s34_reply4)

    def v8s34_reply3():
        contact_Chloe.newMessage("Good. Bored. You?")
        contact_Chloe.addReply("Same!", "phn_chloe13_a1")
        contact_Chloe.addReply("Did you finish studying?", v8s34_reply4)

    def v8s34_reply4():
        contact_Chloe.newMessage("Can't say it's all done, but I sure am!")
        if ending == "chloe":
            contact_Chloe.addReply("So when can I see you again?", v8s34_reply5)

        else:
            contact_Chloe.addReply("I'm actually getting hungry. Wanna go grab a bite?", v8s34_reply6)
            contact_Chloe.addReply("I better get back to it. I have so much work to get done. Just wanted to check on you and see how you're doing.", v8s34_reply7)

    def v8s34_reply5():
        setattr(store, "chloeSteakHouse", True)
        addPoint("bf")
        contact_Chloe.newMessage("Um... how's now? ;)")
        contact_Chloe.addReply("Now's perfect! Should I cum to your place or you wanna cum here? ;)")
        contact_Chloe.newMessage("I was thinking more along the lines of food. I'm hungry!")
        contact_Chloe.addReply("Well I got something to fill your mouth up")
        contact_Chloe.newMessage("Maybe after real food :P")
        contact_Chloe.addReply("What are you in the mood for? Lady's choice", v8s34_reply8)

    def v8s34_reply6():
        setattr(store, "chloeSteakHouse", True)
        addPoint("bf")
        contact_Chloe.newMessage("...")
        contact_Chloe.addReply("As friends", "phn_chloe13_axb2")
        contact_Chloe.newMessage("Ok, yeah. I'm actually starving!")
        contact_Chloe.addReply("What are you in the mood for? Lady's choice", v8s34_reply8)

    def v8s34_reply7():
        contact_Chloe.newMessage("It was nice talking to you")
        contact_Chloe.addReply("You too")

    def v8s34_reply8():
        contact_Chloe.newMessage("There's a new Japanese place right down the road")
        contact_Chloe.addReply("Sounds delicious. Meet you there!")

label v8_tues_noon:
    if ending != "chloe" and chloemad:
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
        $ contact_Chloe.addReply("Hey, sexy :* Haven't seen you in a while")
        $ contact_Chloe.newMessage("OMG! I was just thinking about you!")
        $ contact_Chloe.addReply("I was thinking about you too")
        $ contact_Chloe.newMessage("Awww!")
        $ contact_Chloe.addReply("I was thinking about your lips :*", v8s34_reply1)
        $ contact_Chloe.addReply("Whatcha been up to?", v8s34_reply2)
    else:
        $ contact_Chloe.addReply("Hey, how you been?", v8s34_reply3)

call screen phone
label phn_chloe13:
    if contact_Chloe.getReplies():
        u "(I should talk to Chloe.)"
        jump phn_chloe13

    if chloeSteakHouse:
        stop music fadeout 2
        u "(Guess I'm meeting Chloe.)"
        jump steak_w_chloe

    else:
        u "(I should check in with Julia.)"
        
    jump v8_julia_call
