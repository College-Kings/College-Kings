screen v15_teacher_brief_icon(key):
    tag teacher_brief

    default opened_count = 0

    imagebutton:
        idle "images/v15/Scene 20/teacher_brief/icon.webp"
        action [SetScreenVariable("opened_count", opened_count + 1), Show("v15_teacher_brief", None, key)]


screen v15_teacher_brief(key):
    tag teacher_brief
    zorder 100
    modal True

    default teachers = {
        "dean": {
            "name": "Dean Harrison",
            "profile_picture": dean.profile_picture,
            "description": "The Dean is super serious. Respect her authority.",
            "loves": ["Respect her position.", "It's not an easy path to becoming a College Dean.", "Very proud and protective of SVC and its reputation."],
            "hates": ["Unprofessionalism.", "Disorganization."],
            "insight_info": "Just don't joke around!",
            "insight_condition": v11s1_courtpoints >= 4
        },
        "mr_lee": {
            "name": mr_lee.name.replace('_', ' '),
            "profile_picture": mr_lee.profile_picture,
            "description":"Mr. Lee can be a great ally, but also a great adversary.",
            "loves": ["Strong moral code.", "Mutual respect.", "Professionalism.", "Manners.", "Culture.", "Passionate about all these things and of course, history!"],
            "hates": ["Lies.", "Cheating.", "Dishonor."],
            "insight_info": "Always yield to his knowledge and experience.", 
            "insight_condition": v11_ride_with_mrlee
        },
        "ms_rose": {
            "name": ms_rose.name.replace('_', ' '),
            "profile_picture": ms_rose.profile_picture,
            "description": "Ms. rose is a great teacher, kind and attentive, but she's no pushover.",
            "loves": ["Supporting good causes, especially helping the sororities.", "Making sure things are fair and nobody is upset."],
            "hates": ["Selfishness.", "Misogyny."],
            "insight_info": "If needed, seduction might work best.",
            "insight_condition": ms_rose.relationship >= Relationship.FWB
        }
    }
    default teacher = teachers[key]

    button:
        action Show("v15_teacher_brief_icon", None, key)

    imagebutton:
        idle "images/v15/Scene 20/teacher_brief/background.webp"
        action NullAction()
        align (0.5, 0.5)

    add teacher["profile_picture"] pos(357, 248)

    vbox:
        pos (682, 231)

        text teacher["name"].upper() style "teacher_brief_title"
        text "TEACHER" style "teacher_brief_subtitle"
        null height 20
        text teacher["description"] style "teacher_brief_body"

    vbox:
        pos (362, 609)
        xysize (515, 285)

        hbox:
            xalign 0.5
            spacing 15
            
            add "images/v15/Scene 20/teacher_brief/heart.webp" yalign 0.5
            text "LOVES" style "teacher_brief_header1" yalign 0.5

        for i in teacher["loves"]:
            hbox:
                spacing 15

                add "images/v15/Scene 20/teacher_brief/check.webp" yalign 0.5
                text i style "teacher_brief_body" yalign 0.5

    vbox:
        pos (1052, 609)
        xysize (515, 285)

        hbox:
            xalign 0.5
            spacing 15
            
            add "images/v15/Scene 20/teacher_brief/cross.webp" yalign 0.5
            text "HATES" style "teacher_brief_header1" yalign 0.5

        for i in teacher["hates"]:
            hbox:
                spacing 15

                add "images/v15/Scene 20/teacher_brief/check.webp" yalign 0.5
                text i style "teacher_brief_body" yalign 0.5

    fixed:
        xalign 0.5
        ypos 933
        xysize (1330, 90)

        if teacher["insight_condition"]:
            text teacher["insight_info"] align (0.5, 0.5) style "teacher_brief_header1"

        else:
            hbox:
                align (0.5, 0.5)
                spacing 25

                add "images/v15/Scene 20/teacher_brief/lock.webp"
                text "LOCKED SECRET INSIGHT" style "teacher_brief_header1"


style teacher_brief_title is montserrat_extra_bold_64

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