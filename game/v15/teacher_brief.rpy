screen v15_teacher_brief_icon(teacher, description, loves, hates):
    tag teacher_brief

    imagebutton:
        idle "images/v15/Scene 20/teacher_brief/icon.png"
        action Show("v15_teacher_brief", None, teacher, description, loves, hates)


screen v15_teacher_brief(teacher=mr_lee,
    description="Mr Lee can be a great ally, but also a great adversary.",
    loves=["Strong moral code.", "Mutual respect.", "Professionalism.", "Manners.", "Culture.", "Passionate about all these things and of course, history!"],
    hates=["Lies.", "Cheating.", "Dishonor."], insight="", insight_condition=False):
    tag teacher_brief
    modal True

    button:
        action Show("v15_teacher_brief_icon")

    imagebutton:
        idle "images/v15/Scene 20/teacher_brief/background.png"
        action NullAction()
        align (0.5, 0.5)

    add teacher.profile_picture pos(357, 248)

    vbox:
        pos (682, 231)

        text teacher.name.replace('_', ' ').upper() style "teacher_brief_title"
        text "TEACHER" style "teacher_brief_subtitle"
        null height 20
        text description style "teacher_brief_body"

    vbox:
        pos (362, 609)
        xysize (515, 285)

        hbox:
            xalign 0.5
            spacing 15
            
            add "images/v15/Scene 20/teacher_brief/heart.png" yalign 0.5
            text "LOVES" style "teacher_brief_header1" yalign 0.5

        for i in loves:
            hbox:
                spacing 15

                add "images/v15/Scene 20/teacher_brief/check.png" yalign 0.5
                text i style "teacher_brief_body" yalign 0.5

    vbox:
        pos (1052, 609)
        xysize (515, 285)

        hbox:
            xalign 0.5
            spacing 15
            
            add "images/v15/Scene 20/teacher_brief/cross.png" yalign 0.5
            text "HATE" style "teacher_brief_header1" yalign 0.5

        for i in hates:
            hbox:
                spacing 15

                add "images/v15/Scene 20/teacher_brief/check.png" yalign 0.5
                text i style "teacher_brief_body" yalign 0.5

    fixed:
        xalign 0.5
        ypos 933
        xysize (1330, 90)

        if insight_condition:
            text insight align (0.5, 0.5)

        else:
            hbox:
                align (0.5, 0.5)
                spacing 25

                add "images/v15/Scene 20/teacher_brief/lock.png"
                text "LOCKED SECRET INSIGHT" style "teacher_brief_header1"

# default dean = Teacher(
#     "Dean Harrison",
#     description="The Dean is super serious. Respect her authority.",
#     loves="Respect her position. It's not an easy path to becoming a College Dean. Very proud and protective of SVC and its reputation.",
#     hates="Unprofessionalism. Disorganisation."
# )
# default mr_lee = Teacher(
#     "Mr Lee",
#     description="Mr Lee can be a great ally, but also a great adversary.",
#     loves="Strong moral code. Mutual respect. Professionalism. Manners. Culture. Passionate about all these things and of course, history!",
#     hates="Lies. Cheating. Dishonor."
# )
# default ms_rose = Teacher(
#     "Ms Rose",
#     description="Ms Rose is a great teacher, kind and attentive, but she's no pushover.",
#     loves="Supporting good causes, especially helping the sororities. Making sure things are fair and nobody is upset.",
#     hates="Selfishness. Misogyny."
# ) # Relationship progression: THREATEN, FRIEND, KISS, FWB

style teacher_brief_title is text:
    font "fonts/Montserrat-ExtraBold.ttf"
    size 64

style teacher_brief_subtitle is text:
    font "fonts/Montserrat-Bold.ttf"
    size 26
    color "#ffcc2b"

style teacher_brief_header1 is text:
    font "fonts/Montserrat-ExtraBold.ttf"
    size 36

style teacher_brief_body is text:
    font "fonts/Effra-Regular.ttf"
    size 23