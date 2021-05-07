# SCENE 34: TUESDAY AFTERNOON IN ROOM
# Locations: MC's room in Wolves house, MC's room in Apes house
# Characters: MC (outfit 2)
# Time: Tuesday afternoon
# Note: There's two versions for MC's renders in this scene. They're both the same essentially except one of them is in Wolves house (starting with "v8room20") and the other is in Apes house (starting with "v8room21")

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
    $ contact_Chloe.addReply("Hey, sexy :* Haven't seen you in a while", "phn_chloe12_a1")
else:
    $ contact_Chloe.addReply("Hey, how you been?", "phn_chloe12_b1")
    

pause
call screen messager(contact_Chloe)

label phn_chloe13:
if contact_Chloe.messages[-1].replies:
    u "(I should talk Chloe.)"
    jump phn_chloe13

else:
    
    jump phn_chloe13_done

label phn_chloe12_a1:
    $ contact_Chloe.newMessage("OMG! I was just thinking about you!")
    $ contact_Chloe.addReply("I was thinking about you too", "phn_chloe12_a2")
    call screen messager(contact_Chloe)

label phn_chloe12_a2:
    $ contact_Chloe.newMessage("Awww!")
    $ contact_Chloe.addReply("I was thinking about your lips :*", "phn_chloe12_axa1")
    $ contact_Chloe.addReply("Whatcha been up to?", "phn_chloe12_axb1")

    call screen messager(contact_Chloe)

label phn_chloe12_axa1:
    $ addPoint("bf", 1)
    $ contact_Chloe.newMessage("I bet you were")
    $ contact_Chloe.addReply("I miss them", "phn_chloe12_axa2")
    call screen messager(contact_Chloe)

label phn_chloe12_axa2:
    $ contact_Chloe.newMessage("I know... we should def try again")
    $ contact_Chloe.addReply("I'm on my way!", "phn_chloe12_axa3")
    call screen messager(contact_Chloe)

label phn_chloe12_axa3:
    $ contact_Chloe.newMessage("Hahaha")
    $ contact_Chloe.addReply("Did you finish studying?", "phn_chloe13_a2")
    call screen messager(contact_Chloe)

label phn_chloe12_axb1:
    $ contact_Chloe.newMessage("Nothing. Bored.")
    $ contact_Chloe.addReply("Did you finish studying?", "phn_chloe13_a2")
    call screen messager(contact_Chloe)

label phn_chloe12_b1:
    $ contact_Chloe.newMessage("Good. Bored. You?")
    $ contact_Chloe.addReply("Same!", "phn_chloe13_a1")
    call screen messager(contact_Chloe)

label phn_chloe13_a1:
    $ contact_Chloe.addReply("Did you finish studying?", "phn_chloe13_a2")
    call screen messager(contact_Chloe)

label phn_chloe13_a2:
    $ contact_Chloe.newMessage("Can't say it's all done, but I sure am!")
    if ending == "chloe":
        $ contact_Chloe.addReply("So when can I see you again?", "phn_chloe13_axa1")
    else:
        $ contact_Chloe.addReply("I'm actually getting hungry. Wanna go grab a bite?", "phn_chloe13_axb1")
        $ contact_Chloe.addReply("I better get back to it. I have so much work to get done. Just wanted to check on you and see how you're doing.", "phn_chloe13_axc1")

    call screen messager(contact_Chloe)

label phn_chloe13_axa1:
    $ chloeSteakHouse = True
    $ addPoint("bf", 1)
    $ contact_Chloe.newMessage("Um... how's now? ;)")
    $ contact_Chloe.addReply("Now's perfect! Should I cum to your place or you wanna cum here? ;)", "phn_chloe13_axa2")
    call screen messager(contact_Chloe)

label phn_chloe13_axa2:
    $ contact_Chloe.newMessage("I was thinking more along the lines of food. I'm hungry!")
    $ contact_Chloe.addReply("Well I got something to fill your mouth up", "phn_chloe13_axa3")
    call screen messager(contact_Chloe)

label phn_chloe13_axa3:
$ contact_Chloe.newMessage("Maybe after real food :P")
$ contact_Chloe.addReply("What are you in the mood for? Lady's choice", "phn_chloe13_axxxa1")
call screen messager(contact_Chloe)

label phn_chloe13_axb1:
    $ chloeSteakHouse = True
    $ addPoint("bf", 1)
    $ contact_Chloe.newMessage("...")
    $ contact_Chloe.addReply("As friends", "phn_chloe13_axb2")
    call screen messager(contact_Chloe)

label phn_chloe13_axb2:
    $ contact_Chloe.newMessage("Ok, yeah. I'm actually starving!")
    $ contact_Chloe.addReply("What are you in the mood for? Lady's choice", "phn_chloe13_axxxa1")
    call screen messager(contact_Chloe)

label phn_chloe13_axc1:
    $ chloeSteakHouse = False
    $ contact_Chloe.newMessage("It was nice talking to you")
    $ contact_Chloe.addReply("You too", "phn_chloe13_none")
    call screen messager(contact_Chloe)

label phn_chloe13_axxxa1:
    $ contact_Chloe.newMessage("There's a new Japanese place right down the road")
    $ contact_Chloe.addReply("Sounds delicious. Meet you there!", "phn_chloe13_none")
    call screen messager(contact_Chloe)

label phn_chloe13_none:
    call screen messager(contact_Chloe)

label phn_chloe13_done:
    if chloeSteakHouse:
        stop music fadeout 2
        u "(Guess I'm meeting Chloe.)"
        jump steak_w_chloe
    else:
        u "(I should check in with Julia.)"
    jump v8_julia_call
