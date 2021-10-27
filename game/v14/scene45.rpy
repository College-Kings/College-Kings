# SCENE 45: MC walks home
# Locations: Park, Sidewalk
# Characters: MC (Outfit: 1)
# Time: Afternoon

label v14s45:
    scene v14s45_1 # TPP. Show MC walking through the city, slight smile, mouth closed
    with dissolve

    pause 0.75

    play sound "sounds/vibrate.mp3"

    scene v14s45_2 # TPP. MC walking on the sidewalk (different position to v14s45_1), grabbing his phone, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v14s45_2a # TPP. Same as v14s45_2, MC looking down at his phone, slight smile, mouth closed
    with dissolve

    $ contact_Amber.newMessage("Hey, let's meet up...", queue=False)
    $ contact_Amber.newMessage("I have some news to share.", queue=False)
    $ contact_Amber.addReply("Ooh, okay.")
    $ contact_Amber.newMessage("I'm close to the park, meet me there?")
    $ contact_Amber.addReply("Kk")

    label v14s43_PhoneContinueAmber:
        if contact_Amber.getReplies():
            call screen phone
        if contact_Amber.getReplies():
            u "(I should check my phone.)"
            jump v14s43_PhoneContinueAmber
    
    scene v14s45_2b # TPP. Show MC putting his phone away, slightly confused, mouth closed
    with dissolve

    u "(News to share… Hmm.)"

    scene v14s45_3 # TPP. Show MC walking on the sidewalk, going towards the park, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v14s45_4 # TPP. Show MC arriving at the park, looking for Amber, slight smile, mouth closed
    with dissolve

    pause 0.75

    scene v1s45_5 # FPP. MC in the park, looks at Amber sitting on the bench under the tree, he is far from her, she is tired and sad
    with dissolve

    pause 0.75

    scene v14s45_6 # TPP. Show MC sitting next to Amber, both looking at each other, MC slightly worried, Amber tired and sad
    with dissolve

    pause 0.75

    jump v14s45a