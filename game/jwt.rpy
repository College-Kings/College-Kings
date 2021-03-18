# Forced Walkthrough mod by Jany


# variables
default jwt = False #Walkthrough enabled?
define config.menu_include_disabled = True #makes choices unavailable
define jany = Character("Jany", who_color="#2293ff", who_outlines=[ (2, "#000000") ], what_outlines=[ (2, "#000000") ])


# screens
screen jwt(): # the screen to select if the walkthrough is enabled
    image "images/jwt.jpg"

    imagebutton:
        ypos 169
        xpos 143
        idle "images/jwte.jpg"
        hover "images/jwteh.jpg"
        action Jump ("jwt")

    imagebutton:
        ypos 168
        xpos 1270
        idle "images/jwtd.jpg"
        hover "images/jwtdh.jpg"
        action Jump ("jwtd")

screen walkthroughOff():
  textbutton "Disable Walkthrough":
    action Hide("walkthroughOff"), SetVariable("jwt", False)



# labels
label jwt: #If the walkthrough is enabled
    $ jwt = True
    $ realmode = False
    $ config.rollback_enabled = True
    $ showkct = False
    
    jany "Welcome to the walkthrough."
    jany "With this walkthrough you will see all the dates and lewd scenes."
    jany "You can just play the game as you would play it normally, but some choices are disabled, so that you won't miss anything."
    jany "Also a few paths do something else than when playing withouzt the walkthrough (since you would miss some scenes while playing normally)"
    show screen walkthroughOff
    jany "If you at any point want to continue playing normally, just click the button in the top right corner."
    
    jany "Have fun!"
    
    $ laurenMessage8a.disableReply("Sorry, I can't", "larep8b")
    $ laurenMessage8b.disableReply("Sorry, I can't", "larep8b")
    $ joshMessage14.disableReply("I can't, sorry.", "jorep14b")
    $ joshMessage8.disableReply("Uhh, sure.", "jorep8a")
    $ aubreyMessage16.disableReply("Sorry, I can't tonight.", "aubrep16b")
    $ rileyMessage8.disableReply("Sorry I'm really exhausted. Another time", "rirep8b")
    $ laurenMessage25.disableReply("Sorry, I can't I'm really busy today", "larep25b")

    
    jump starta


label jwt_bg_b: #riley dream to do both blow- and footjob
    
    scene sda3b
    with dissolve

    u "I want you to suck my dick."

    scene sda3a
    with dissolve

    ri "I was hoping you'd say that."
    image sdabj = Movie (play="images/sdabj.webm", loop = True, image = "images/s1")
    image sdabjf = Movie (play="images/sdabjf.webm", loop = True, image = "images/sda4e")

    show sdabj
    with fade
    u "You look so pretty with my cock in your mouth."

    ri "*Gasp* You taste so good."
    ri "Just make sure you don't come yet."

    u "I won't, I won't. You can go faster."

    show sdabjf
    with dissolve
    ri "*Gasp* Like this?"

    u "Fuuuuck. Yes, exactly like that."
    u "I can't hold it much longer."
    ri "Then let's switch it up."
    
    jump bg_c

label jwt_fradam1:
    
    scene s59
    $ showphone = False
    
    u "I can hear something coming from the dorm behind me."
    
    scene adamaubrey36
    stop music fadeout 2.0

    image adam1 = Movie(play="images/adamau.webm")
    play music "music/msexy.mp3"
    show adam1
    au "Ohhh shit, that feels good!"
    u "(Oh my god... she's so fucking hot.)"
    au "YESSSSS, FASTER!"
    u "(I should probably stop peeking, before I get caught.)"
    $ fr1adam = 1
    stop music fadeout 2.0
    jump jwt_efra

label jwt_eq_b:

    scene jomon16 # kim in bra ready for shot of her body
    with fade

    jo "*Drunk* Alright [name], lick the salt off her collarbone, drink the shot out of her belly button and bite the lime out of her mouth."

    scene jomon16a
    with dissolve

    pause 0.5

    scene jomon16b
    with dissolve

    pause 0.5

    scene jomon16c
    with dissolve

    pause 0.5

    scene jomon17 # close up of you with lemon in mouth right above ambers face
    with dissolve


    menu:

        "Kiss her":

            $ addPoint("tm", 1)
            $ kisskim = True
            jump jwt_es_a


        "Don't kiss her":

            $ addPoint("tm", 1)
            $ kisskim = False
            jump jwt_es_b




label jwt_es_a:

    play sound "sounds/spit.mp3"

    scene jomon17a # spits out lemon
    with dissolve

    u "*Spit sound*"

    scene jomon17b # kiss but she pulls aways
    with dissolve

    ki "Mhhh... no."
    
    jump eq_a

label jwt_es_b:

    play sound "sounds/spit.mp3"

    scene jomon17a # spits out lemon
    with dissolve

    u "*Spits*"
    
    jump eq_a
    
label jwt_awfra:
    
    scene s684 # showing Nora and Chris arguing
    with dissolve

    no "Can you just not for once? You do this every single fucking time. I just don't get it!"

    scene s684a #Nora storms off to the garden
    with dissolve

    pause 0.5

    scene s685 # Chris upset close up looking after her
    with dissolve

    ch "Nora! C'mon! Don't do that!"

    scene s685a #Chris turns to one of his friends and begins talking to him.
    with dissolve

    ch "I swear she finds new reasons to get upset every day."
    
    scene s686 # First person looking at backyard door that nora just walked out of
    with dissolve

    u "(Wow, Nora seemed really upset...)"
    
    menu:

            "Go after Nora":
                u "(I should go after her and make sure she's okay.)"
                $ addPoint("bf", 1)
                $ follownora = True
                jump hd_bd

            "Leave her alone" if not jwt:
                jany "Wait how?"
    
label jwt_hd_bd:
    scene s683
    ri "Are you walking me home?"

    menu:

        "Walk Riley home":
            $ follownora = False
            $ addPoint("bro", 1)
            jump hd_a

        "Leave her alone" if not jwt:
            jany "Wait how?"
            
            
label jwt_wp:
    #after talkjing to chris
                

                
label jwt_hc: #homecoming select screen
    scene jwt_hocochoice
    jany "BUILD ENDS HERE"
    jany "This is where the real walkthrough starts. Up until now you had quite a lot of choices, but not a lot of them split the path."
    jany "Now the path is all over the place, so you'll be guided through a lot of the scenes automatically and have fewer choices."
    jany "For example the homecoming invite screen is missing, which you might've noticed if you already played the game."
    jany "Instead of that you can enjoy this custom render only available in the walkthrough!"
    jany "You will also invite all the girls to the homecoming now."
    jany "To manage this we will have quite a few different timelines."
    jany "The timeline changes if you see this image."
    jany "The character that comes up next will be highlited. In this case, this is Amber"
    jany "Have fun!" 

label jwt_afteramber:
    scene jwt_hocochoice
    jany "Nothing here yet"
    jany "BUILD ENDS HERE"

    
    
