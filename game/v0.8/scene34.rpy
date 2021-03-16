# SCENE 34: TUESDAY AFTERNOON IN ROOM
# Locations: MC's room in Wolves house, MC's room in Apes house
# Characters: MC (outfit 2)
# Time: Tuesday afternoon
# Note: There's two versions for MC's renders in this scene. They're both the same essentially except one of them is in Wolves house (starting with "v8room20") and the other is in Apes house (starting with "v8room21")

# Variables and definitions
default chloeSteakHouse = False

default chloeMessage12 = (contact_Chloe, "")
default chloeMessage12_a1 = (contact_Chloe, "OMG! I was just thinking about you!")
default chloeMessage12_a2 = (contact_Chloe, "Awww!")
default chloeMessage12_axa1 = (contact_Chloe, "I bet you were")
default chloeMessage12_axa2 = (contact_Chloe, "I know... we should def try again")
default chloeMessage12_axa3 = (contact_Chloe, "Hahaha")
default chloeMessage12_axb1 = (contact_Chloe, "Nothing. Bored.")
default chloeMessage12_b1 = (contact_Chloe, "Good. Bored. You?")
# Same convo but divided into two parts to avoid insanity
default chloeMessage13_a1 = (contact_Chloe, "")
default chloeMessage13_a2 = (contact_Chloe, "Can't say it's all done, but I sure am!")
default chloeMessage13_axa1 = (contact_Chloe, "Um... how's now? ;)")
default chloeMessage13_axa2 = (contact_Chloe, "I was thinking more along the lines of food. I'm hungry!")
default chloeMessage13_axa3 = (contact_Chloe, "Maybe after real food :P")
default chloeMessage13_axb1 = (contact_Chloe, "...")
default chloeMessage13_axb2 = (contact_Chloe, "Ok, yeah. I'm actually starving!")
default chloeMessage13_axxxa1 = (contact_Chloe, "There's a new Japanese place right down the road")
default chloeMessage13_axc1 = (contact_Chloe, "It was nice talking to you")

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

if ending == "chloe":
    $ chloeMessage12.addReply("Hey, sexy :* Haven't seen you in a while", "phn_chloe12_a1")
else:
    $ chloeMessage12.addReply("Hey, how you been?", "phn_chloe12_b1")

$ chloeMessage12_a1.addReply("I was thinking about you too", "phn_chloe12_a2")
$ chloeMessage12_a2.addReply("I was thinking about your lips :*", "phn_chloe12_axa1")
$ chloeMessage12_axa1.addReply("I miss them", "phn_chloe12_axa2")
$ chloeMessage12_axa2.addReply("I'm on my way!", "phn_chloe12_axa3")

$ chloeMessage12_a2.addReply("Whatcha been up to?", "phn_chloe12_axb1")
$ chloeMessage12_b1.addReply("Same!", "phn_chloe13_a1")

$ chloeMessage13_a1.addReply("Did you finish studying?", "phn_chloe13_a2")
if ending == "chloe":
    $ chloeMessage13_a2.addReply("So when can I see you again?", "phn_chloe13_axa1")
else:
    $ chloeMessage13_a2.addReply("I'm actually getting hungry. Wanna go grab a bite?", "phn_chloe13_axb1")
$ chloeMessage13_a2.addReply("I better get back to it. I have so much work to get done. Just wanted to check on you and see how you're doing.", "phn_chloe13_axc1")

$ chloeMessage13_axa1.addReply("Now's perfect! Should I cum to your place or you wanna cum here? ;)", "phn_chloe13_axa2")
$ chloeMessage13_axa2.addReply("Well I got something to fill your mouth up", "phn_chloe13_axa3")
$ chloeMessage13_axb1.addReply("As friends", "phn_chloe13_axb2")
$ chloeMessage13_axa3.addReply("What are you in the mood for? Lady's choice", "phn_chloe13_axxxa1")
$ chloeMessage13_axb2.addReply("What are you in the mood for? Lady's choice", "phn_chloe13_axxxa1")
$ chloeMessage13_axxxa1.addReply("Sounds delicious. Meet you there!", "phn_chloe13_none")
$ chloeMessage13_axc1.addReply("You too", "phn_chloe13_none")

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

$ contact_Chloe.newMessage(chloeMessage12)
$ phoneexit = "phn_chloe13"
$ showphone = True
pause
call screen messager(contact_Chloe)

label phn_chloe13:
if not chloeMessage12.reply:
    u "(I should text Chloe.)"
    jump phn_chloe13

elif not chloeMessage13_axc1.reply or not chloeMessage13_axxxa1.reply:
    u "(I should reply to Chloe.)"
    jump phn_chloe13

else:
    $ showphone = False
    jump phn_chloe13_done

label phn_chloe12_a1:
$ contact_Chloe.newMessage(chloeMessage12_a1)
call screen messager(contact_Chloe)

label phn_chloe12_a2:
$ contact_Chloe.newMessage(chloeMessage12_a2)
call screen messager(contact_Chloe)

label phn_chloe12_axa1:
$ addPoint("bf", 1)
$ contact_Chloe.newMessage(chloeMessage12_axa1)
call screen messager(contact_Chloe)

label phn_chloe12_axa2:
$ contact_Chloe.newMessage(chloeMessage12_axa2)
call screen messager(contact_Chloe)

label phn_chloe12_axa3:
$ contact_Chloe.newMessage(chloeMessage12_axa3)
$ contact_Chloe.newMessage(chloeMessage13_a1)
call screen messager(contact_Chloe)

label phn_chloe12_axb1:
$ contact_Chloe.newMessage(chloeMessage12_axb1)
$ contact_Chloe.newMessage(chloeMessage13_a1)
call screen messager(contact_Chloe)

label phn_chloe12_b1:
$ contact_Chloe.newMessage(chloeMessage12_b1)
call screen messager(contact_Chloe)

label phn_chloe13_a1:
$ contact_Chloe.newMessage(chloeMessage13_a1)
call screen messager(contact_Chloe)

label phn_chloe13_a2:
$ contact_Chloe.newMessage(chloeMessage13_a2)
call screen messager(contact_Chloe)

label phn_chloe13_axa1:
$ chloeSteakHouse = True
$ addPoint("bf", 1)
$ contact_Chloe.newMessage(chloeMessage13_axa1)
call screen messager(contact_Chloe)

label phn_chloe13_axa2:
$ contact_Chloe.newMessage(chloeMessage13_axa2)
call screen messager(contact_Chloe)

label phn_chloe13_axa3:
$ contact_Chloe.newMessage(chloeMessage13_axa3)
call screen messager(contact_Chloe)

label phn_chloe13_axb1:
$ chloeSteakHouse = True
$ addPoint("bf", 1)
$ contact_Chloe.newMessage(chloeMessage13_axb1)
call screen messager(contact_Chloe)

label phn_chloe13_axb2:
$ contact_Chloe.newMessage(chloeMessage13_axb2)
call screen messager(contact_Chloe)

label phn_chloe13_axc1:
$ chloeSteakHouse = False
$ contact_Chloe.newMessage(chloeMessage13_axc1)
call screen messager(contact_Chloe)

label phn_chloe13_axxxa1:
$ contact_Chloe.newMessage(chloeMessage13_axxxa1)
call screen messager(contact_Chloe)

label phn_chloe13_none:
call screen messager(contact_Chloe)

label phn_chloe13_done:
if chloeSteakHouse:
    u "(Guess I'm meeting Chloe.)"
else:
    u "(I should check in with Julia.)"
    jump v8_julia_call
