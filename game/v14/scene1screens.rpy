screen VoiceActing_Toggle(jumplabel):
    

    add "gui/frame.webp":
        align (0.5,0.5)
        ysize 350

    vbox:
        xsize 700
        align (0.5, 0.5)
        spacing 20
        text "Voice Acted Sex Scenes":
            #color "#FFD166"
            size 40
            text_align 0.5
            xalign 0.5

        text "This act has voice acted sex scenes. Each girl has a unique voice and moans accordingly. Please select if you'd like to enable voice acting in the sex scenes.":
            font "fonts/OpenSans.ttf"
            size 25
            text_align 0.5
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100
            textbutton "Enable":
                text_size 40
                action [SetVariable("voice_acted", True),Hide("VoiceActing_Toggle"), Jump (jumplabel)]
            textbutton "Disable":
                text_size 40
                action [SetVariable("voice_acted", False),Hide("VoiceActing_Toggle"), Jump (jumplabel)]
            