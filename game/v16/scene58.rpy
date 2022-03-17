# SCENE 58: Transition Mc leaves the house
# Locations: Sidewalk
# Characters: MC (Outfit: 2)
# Time: Thursday Afternoon


label v16s58:

    scene v16s58_1 # TPP. Show MC (no expression, mouth is closed) walking along a sidewalk, plain background (something easy to render)
    with dissolve

    u "(I was hoping to fit in a quick nap, but frat drama bullshit strikes again... *Sighs*)"

    u "(Time to meet Lindsey.)"

    if v16s28_lindsey_pb_intereview_polly_choice: # -if helping Lindsey with interview, transition to Scene 60-

        jump v16s60

    else: # -if helping Lindsey with Polly endorsement, transition to Scene 59-

        jump v16s59