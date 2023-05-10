# SCENE 62a: Fever Dream Cliffhanger
# Locations: Hotel Room, Hotel Room Bathroom
# Characters: LINDSEY (Outfit: 1), MC (Outfit: 3)
# Time: Night

label v13s62a:
    play sound sound.door_open

    scene v13s62a_1 # FPP. Lindsey walking into the hotel room, sexy expression, mouth closed
    with dissolve

    pause 1.25

    play music music.ck1.v13.Track_Scene_62a fadein 2

    scene v13s62a_2 # FPP. Lindsey standing next to MC, grabbing his hand, sexy expression, mouth open
    with dissolve

    li "Come with me. Now."

    scene v13s62a_3 # TPP. Show Lindsey pulling MC by the hand through the room towards the bathroom, MC surprised, Lindsey sexy, mouths closed
    with dissolve

    pause 0.75
 
    scene v13s62a_4 # TPP. Show Lindsey and MC walking into the bathroom, MC surprised, Lindsey sexy, mouths closed
    with dissolve

    pause 0.75

    scene v13s62a_5 # FPP. MC and Lindsey in bathroom, Lindsey sexy expression, mouth closed
    with dissolve

    u "What's going on?!"

    scene v13s62a_5a # FPP. Same as v13s62a_5, Lindsey mouth slightly open
    with dissolve

    li "Shhh!"

    scene v13s62a_6 # TPP. Show Lindsey taking off her top, sexy expression, mouth closed
    with dissolve

    if is_censored:
        call screen censored_popup("v14s01a_nsfwSkipLabel1")

    pause

    scene v13s62a_7 # TPP. Show LIndsey taking off her pants (she has panties on, no bra), sexy expression, mouth closed
    with dissolve

    pause

    scene v13s62a_8 # TPP. Show Lindsey handcuffing herself to something near the sink, sexy expression, mouth closed
    with dissolve

    pause

    scene v13s62a_9 # FPP. MC looking at Lindsey sitting on the sink, legs closed, sexy expression, mouth open
    with fade

    li "I know you have all the other girls, but I want you for myself and want you... Right... Fucking... Now."

    li "*Chuckles* Now, please... You can do anything you want..."

    scene v13s62a_9a # FPP. Same as v13s62a_9, Lindsey's legs spread open
    with vpunch

    li "ANYTHING!"

    scene v13s62a_9b # FPP. Same as v13s62a_9a, Lindsey mouth closed
    with dissolve

    u "(What the fuck is going on?)"

    scene v13s62a_9c # FPP. Same as v13s62a_9b, MC stretching his hand out as if he wanted to touch her (not touching Lindsey)
    with dissolve

    pause

    scene v13s62a_10 # TPP. Show MC approaching Lindsey, not touching her, MC surprised, mouth closed, Lindsey sexy, mouth closed
    with dissolve

    pause

    #scene v13s62a_10a # TPP. Same v13s62a_10, MC even closer, still not touching her, MC surprised, mouth closed, Lindsey sexy, mouth closed
    #with dissolve

    #pause

    stop music fadeout 3

    jump v14_start
    