screen recap_rep_selection_screen():
    modal True

    default recap_ui_path = "images/recap/ui/"

    add recap_ui_path + "recap_rep_selection_bg.webp"

    # Pink/Left/Loyal
    button:
        idle_background  recap_ui_path + "pink_idle.webp"
        hover_background recap_ui_path + "pink_hover.webp"
        pos (190, 785)
        xysize (392, 114)
        action [SetVariable("kct", "loyal"), SetVariable("bro", 2), SetVariable("boyfriend", 2), SetVariable("troublemaker", 1), Return()]

        text "Pick" style "bebas_neue_30" align(0.5, 0.5)

    # Yellow/Middle/Popular
    button:
        idle_background  recap_ui_path + "yellow_idle.webp"
        hover_background recap_ui_path + "yellow_hover.webp"
        pos (760, 785)
        xysize (396, 115)   
        action [SetVariable("kct", "popular"), SetVariable("bro", 2), SetVariable("boyfriend", 1), SetVariable("troublemaker", 2), Return()]

        text "Pick" style "bebas_neue_30" align(0.5, 0.5)


    # Blue/Right/Confident
    button:
        idle_background recap_ui_path + "blue_idle.webp"
        hover_background recap_ui_path + "blue_hover.webp"
        pos (1320, 745)
        xysize (480, 200)
        action [SetVariable("kct", "confident"), SetVariable("bro", 1), SetVariable("boyfriend", 2), SetVariable("troublemaker", 2), Return()]

        text "Pick" style "bebas_neue_30" align(0.5, 0.5)

    on "show" action Hide("phone_icon")


screen recap_frat_selection_screen():
    modal True

    default recap_ui_path = "images/recap/ui/"

    add recap_ui_path + "recap_frat_selection_bg.webp"

    # Red/Left
    frame:
        xysize (435, 150)
        pos (270, 725)
        background Frame(recap_ui_path + "trans_bg.webp")

        text "Fearless, tough and ruthless, Apes are born warriors and leaders who will do whatever it takes to win. Pledging to the Apes means constantly challenging yourself and fighting your way to the top.":
            style "effra_regular_23"
            text_align 0.5
            align (0.5, 0.5)

    # Red button
    button:
        idle_background  recap_ui_path + "red_idle.webp"
        hover_background recap_ui_path + "red_hover.webp"
        pos (250, 875)
        xysize (460, 182)
        action Return("apes")

        text "Apes" style "bebas_neue_30" align (0.5, 0.5)

    # Blue/Right
    frame:
        xysize (435, 165)
        pos (1215, 727)
        background Frame(recap_ui_path + "trans_bg.webp")

        text "Honor, loyalty and brotherhood, Wolves bring a touch of chivalry to the world and look out for one another. Pledging to the Wolves means having the determination to be your best self and always having your frat brother’s back.":
            style "effra_regular_23"
            text_align 0.5
            align (0.5, 0.5)

    # Blue button
    button: 
        idle_background recap_ui_path + "blue_idle.webp"
        hover_background recap_ui_path + "blue_hover.webp"
        pos (1200, 869)
        xysize (480, 200)
        action Return("wolves")        

        text "Wolves" style "bebas_neue_30" align (0.5, 0.5)

    on "show" action Hide("phone_icon")


screen recap_girl_overview_screen():
    # Path builder light but use the same UI elements
    # Show icons of the girls
    # Click the icon to load the recap_girl_summary for that girls
    # Jump actions for each
    modal True

    default recap_ui_path = "images/recap/ui/"
    default idle_image = ""
    default hover_image = ""

    # Emily
    # Autumn
    # Ms Rose
    # Lauren
    # Riley
    # Nora
    # Aubrey
    # Chloe
    # Penelope
    # Amber
    # Samantha
    # Lindsey
    # Jenny

    default girls = [
        {
            "girl_object": emily,
            "xpos": 275,
            "label": "recap_emily_questions"
        },
        {
            "girl_object": autumn,
            "xpos": 325,
            "label": "recap_autumn_questions"
        },
        {
            "girl_object": ms_rose,
            "xpos": 190,
            "label": "recap_ms_rose_questions"
        },
        {
            "girl_object": lauren,
            "xpos": 350,
            "label": "recap_lauren_questions"
        },
        {
            "girl_object": riley,
            "xpos": 165,
            "label": "recap_riley_questions"
        },
        {
            "girl_object": nora,
            "xpos": 325,
            "label": "recap_nora_questions"
        },
        {
            "girl_object": aubrey,
            "xpos": 225,
            "label": "recap_aubrey_questions"
        },
        {
            "girl_object": chloe,
            "xpos": 250,
            "label": "recap_chloe_questions"
        },
        {
            "girl_object": penelope,
            "xpos": 145,            
            "label": "recap_penelope_questions"
        },
        {
            "girl_object": amber,
            "xpos": 285,
            "label": "recap_amber_questions"
        },
        {
            "girl_object": samantha,
            "xpos": 200,
            "label": "recap_samantha_questions"
        },
        {
            "girl_object": lindsey,
            "xpos": 200,
            "label": "recap_lindsey_questions"
        }
    ]

    add recap_ui_path + "recap_summary_bg.webp"

    frame:
        background recap_ui_path + "recap_summary_banner.webp"
        xysize (1779, 712)
        pos (71, 104)

        text "The Girls of College Kings":
            style "montserrat_extra_bold_64"
            xalign 0.5
            ypos 50

        grid 4 3:
            spacing 30
            align (0.5, 0.5)

            for girl in girls:
                button:
                    idle_background "images/common/girl_button/idle.webp"
                    hover_background "images/common/girl_button/hover.webp"
                    sensitive True
                    action Jump(girl["label"])
                    xysize (307, 112)

                    hbox:
                        xpos 6
                        yalign 0.5
                        spacing 20

                        add Transform(girl["girl_object"].profile_picture, xysize=(100, 100))

                        text girl["girl_object"].name:
                            yalign 0.5
                            size 30

                    if girl["girl_object"].relationship != Relationship.FRIEND:
                        add recap_ui_path + "rs_hearts.webp":
                            align (1.0, 1.0)
                            xoffset -15

        text "Click on a girl to change your decisions about her or click continue to start College Kings.":
            style "effra_regular_26"
            align (0.5, 1.0)
            yoffset -50

    button:
        idle_background recap_ui_path + "blue_idle.webp"
        hover_background recap_ui_path + "blue_hover.webp"
        sensitive True
        action [Hide("recap_girl_overview_screen", transition=dissolve), Jump("recap_end")]
        pos (700, 835)
        xysize (480, 200)        

        text "Continue": 
            style "bebas_neue_30"
            align (0.5, 0.5)

    on "show" action Hide("phone_icon")


screen recap_girl_summary(girl_name):
    modal True
    style_prefix "recap"

    default recap_image_path = "images/recap/girls/"
    default recap_ui_path = "images/recap/ui/" 

    default girl_info = {
        "penelope": {
            "ui_name": "Penelope",
            "xpos": 145,            
            "summary": "Penelope is in the same history class as me, but the first time we actually spoke was when she randomly stopped me in the street. Straight away I was struck by how quirky she was. Definitely an endearing quality, and I like how she was different to the girls I'd already met.",
            "birthday": "January 1",
            "eyes": "Green",
            "hair": "Black",
            "star_sign": "Capricorn",
            "height": "5 feet 10 inches",
            "measurements": "34-25-37",
            "bra_size": "28B",
            "favorite_color": "White",
            "left_btn": "Pursue relationship",
            "right_btn": "Be friends",
        },
        "emily": {
            "ui_name": "Emily",
            "xpos": 275,
            "summary": "Emily, my ex from high school, was starting college too. She wanted to apologize for cheating on me and ruining our relationship.",
            "birthday": "May 30",
            "eyes": "Green",
            "hair": "Red",
            "star_sign": "Gemini",
            "height": "5 feet 10 inches",
            "measurements": "37-28-39",
            "bra_size": "30B",
            "favorite_color": "Yellow",
            "left_btn": "Forgive her",
            "right_btn": "Don't forgive her",
        },
        "autumn": {
            "ui_name": "Autumn",
            "xpos": 325,
            "summary": "Autumn is Lauren's older sister, and I got the impression that she was more of a long-term challenge if anything serious was ever going to develop between us. I had opportunities to spend some time with her though to start putting the work in, and to learn more about what makes her tick.",
            "birthday": "April 15",
            "eyes": "Greenish-brown",
            "hair": "Brown",
            "star_sign": "Aries",
            "height": "5 feet 11 inches",
            "measurements": "34-25-37",
            "bra_size": "28A",
            "favorite_color": "Lime Green",
            "left_btn": "Spend time with her",
            "right_btn": "Don't spend time with her",
        },
        "ms_rose": {
            "ui_name": "Ms. Rose",
            "xpos": 190,
            "summary": "Ms Rose is our economics teacher, and later I found out she's also Nora's stepmom! After fully expecting some crusty old professor type to be teaching us economics, I was pleasantly surprised to see her at the front of the class.",
            "ape_summary": "\n\nThe Wolves frat seemed to have way more contact with her, so if I was interested, joining that frat was the only way I'd have a chance of working my way into her affections, and her panties.",
            "left_stats": "Birthday:  \nEyes:  \nHair:  \nSign: ",
            "right_stats": "Height:  \nMeasurements:  \nBra size:  \nFavorite Color: ",
            "birthday": "October 9",
            "eyes": "Green",
            "hair": "Brown",
            "star_sign": "Libra",
            "height": "5 feet 11 inches",
            "measurements": "38-24-36",
            "bra_size": "30C",
            "favorite_color": "Teal",
            "left_btn": "Pursue a relationship",
            "right_btn": "Be friends",
        },
        "lauren": {
            "ui_name": "Lauren",
            "xpos": 350,
            "summary": "I sat next to Lauren in Economics class on my first day and we hit it off straight away.",
            "birthday": "October 31",
            "eyes": "Brown",
            "hair": "Brown",
            "star_sign": "Scorpio",
            "height": "5 feet 11 inches",
            "measurements": "37-28-39",
            "bra_size": "30C",
            "favorite_color": "Green",
            "left_btn": "Pursue a relationship",
            "right_btn": "Be friends",
        },
        "riley": {
            "ui_name": "Riley",
            "xpos": 165,
            "summary": "Like Lauren, Riley has been in my life since my very first day on campus. She always seemed to be the girl making herself available for a chat, and was clearly someone I could dependent on, as well as fun to be around.",
            "birthday": "June 1",
            "eyes": "Brown",
            "hair": "Red",
            "star_sign": "Gemini",
            "height": "5 feet 10 inches",
            "measurements": "33-25-36",
            "bra_size": "26C",
            "favorite_color": "Red",
            "left_btn": "Pursue a relationship",
            "right_btn": "Be friends",
        },
        "nora": {
            "ui_name": "Nora",
            "xpos": 325,
            "summary": "Nora's been dating Chris, the Wolves president, since before I arrived at college. This didn't stop me being able to flirt with her though. And their relationship didn't seem to be going all that great, so somebody had to give her the attention she was missing.",
            "birthday": "March 17",
            "eyes": "Green",
            "hair": "Brown",
            "star_sign": "Pisces",
            "height": "5 feet 10 inches",
            "measurements": "37-29-41",
            "bra_size": "30B",
            "favorite_color": "Red",
            "left_btn": "Flirt with her",
            "right_btn": "Don't flirt with her",
        },
        "aubrey": {
            "ui_name": "Aubrey",
            "xpos": 225,
            "summary": "Aubrey was one of the most easy-going girls I'd ever met. There was some clear chemistry and she was the first college girl I had the chance to have sex with. She didn't seem the type to want anything serious any time soon, so it was purely going to be a friends-with-benefits deal if I wanted to go that route.",
            "birthday": "February 14",
            "eyes": "Brown",
            "hair": "Brown",
            "star_sign": "Aquarius",
            "height": "5 feet 10 inches",
            "measurements": "36-26-39",
            "bra_size": "30B",
            "favorite_color": "Purple",
            "left_btn": "Have Sex",
            "right_btn": "Be friends",
        },
        "chloe": {
            "ui_name": "Chloe",
            "xpos": 250,
            "summary": "I was at the Apes' frat house party when I first met Chloe. Clearly, she was one of the hottest girls on campus. But they say the hotter they are, the crazier they are. We were doing some obvious flirting, so I felt I had the chance to find out for myself if there was any truth to that saying.",
            "birthday": "August 4",
            "eyes": "Green",
            "hair": "Green",
            "star_sign": "Leo",
            "height": "5 feet 10 inches",
            "measurements": "38-25-37",
            "bra_size": "30D",
            "favorite_color": "Baby Pink",
            "left_btn": "Pursue a relationship",
            "right_btn": "Be friends",
        },
        "amber": {
            "ui_name": "Amber",
            "xpos": 285,
            "summary": "My childhood friend, Josh, introduced me to Amber. Straight away I knew she was a party girl, always looking to have fun and enjoy life to the fullest. She was into drinking and taking drugs, but seemed responsible with it rather than totally out of control.",
            "birthday": "December 21",
            "eyes": "Brown",
            "hair": "Black",
            "star_sign": "Sagittarius",
            "height": "5 feet 10 inches",
            "measurements": "36-28-39",
            "bra_size": "30B",
            "favorite_color": "Black",
            "left_btn": "Pursue a relationship",
            "right_btn": "Be friends",
        },
        "samantha": {
            "ui_name": "Samantha",
            "xpos": 200,
            "ape_summary": "Samantha is Cameron's drug-addicted sister. She already had my sympathy for being related to Cameron, but I needed to decide if I wanted to get closer to her or keep my distance.",
            "wolf_summary": "Samantha is Cameron's drug-addicted sister and someone I barely even see as she's part of that whole Apes clan. If I really wanted to get to know her better, I had to shape shift into an Ape!",
            "birthday": "November 24",
            "eyes": "rownish-green",
            "hair": "Auburn/Red",
            "star_sign": "Sagittarius",
            "height": "5 feet 10 inches",
            "measurements": "37-25-36",
            "bra_size": "30C",
            "favorite_color": "Burgundy",
            "left_btn": "Keep my distance",
            "right_btn": "Get Closer",
        },
        "lindsey": {
            "ui_name": "Lindsey",
            "xpos": 325,
            "summary": "I'd seen Lindsey around a few times but didn't really get to know her until some guy tried to start a fight with me after class one day. She seemed to appreciate the way I dealt with him and starting showing some genuine interest. It was the night of my first big fight tournament and she wanted me to go over to hers right before the main event.",            
            "birthday": "October 16",
            "eyes": "Green",
            "hair": "Blonde",
            "star_sign": "Libra",
            "height": "5 feet 11 inches",
            "measurements": "37-26-40",
            "bra_size": "30C",
            "favorite_color": "Peachy Orange",
            "left_btn": "Go see her",
            "right_btn": "Don't go see her",
        },
        "jenny": {
            "ui_name": "Jenny",
            "xpos": 160,
            "summary": "Penelope tried to enroll Jenny into our college by hacking the system, but she got caught and was in a whole heap of trouble. It was kinda weird how I first met Jenny. She sent me a random text one day asking to meet so we can talk about Penelope. To begin with, I had no idea who this Jenny was, but decided there was nothing to lose by meeting up with her. It's too early to say if there's any potential for romance here.",
            "birthday": "June 11",
            "eyes": "Blue",
            "hair": "Blonde",
            "star_sign": "Gemini",
            "height": "5 feet 8 inches",
            "measurements": "36-26-38",
            "bra_size": "30B",
            "favorite_color": "Lavender",
            "left_btn": None,            
            "right_btn": None,
        }
    }
    
    $ girl = girl_info[girl_name]

    # background image load
    add recap_ui_path + "recap_girl_bg.webp"

    # Large clothed image 
    add Transform(recap_image_path + "ui_hd_{}_stand.webp".format(girl_name), zoom=1.5):
        pos (girl["xpos"], 200)

    # Girl Name Header 
    text girl["ui_name"]:
        style "montserrat_extra_bold_64"
        pos (752, 216)

    # Horitzontal box for narrative 
    frame:
        pos (752, 312)
        xysize (912, 240)

        # Special handling for Ms Rose Narrative
        if girl_name == "ms_rose":
            if joinapes:
                text girl_info[girl_name]["summary"] + girl_info[girl_name]["ape_summary"]
            else:
                text girl_info[girl_name]["summary"]
        
        # special handling for Samantha narraitive
        elif girl_name == "samantha":
            if joinapes:
                text girl_info[girl_name]["ape_summary"]
            else:
                text girl_info[girl_name]["wolf_summary"]

        else:
            # narrative text 
            text girl_info[girl_name]["summary"]

    # stats left 
    vbox:
        pos (752, 632)
        xysize (416, 128)

        for i in ("birthday", "eyes", "hair", "star_sign"):
            text "{}: {}".format(i.replace('_', ' ').capitalize(), girl[i])

    # stats right
    vbox:
        pos (1248, 632)
        xysize (416, 128)

        for i in ("height", "measurements", "bra_size", "favorite_color"):
            text "{}: {}".format(i.replace('_', ' ').capitalize(), girl[i])

    #  Special handling for Ms Rose and Samantha Continue button 
    if (girl_name == "jenny") or (girl_name == "ms_rose" and joinapes) or (girl_name == "samantha" and (joinwolves or not joinapes)):
        # Continue button
        button:
            idle_background recap_ui_path + "blue_idle.webp"
            hover_background recap_ui_path + "blue_hover.webp"
            sensitive True
            action Return("continue") 
            pos (700, 835)
            xysize (480, 200)        

            text "Continue": 
                style "recap_button_text"
                align (0.5, 0.5)

    else:        
        # Left Button 
        button:
            idle_background recap_ui_path + "pink_idle.webp"
            hover_background recap_ui_path + "pink_hover.webp"
            action Return(girl["left_btn"])
            pos (546, 909)            
            xysize (392, 114)

            text girl["left_btn"]:
                style "recap_button_text"
                align (0.5, 0.5)

        # Right Button
        button:
            idle_background recap_ui_path + "blue_idle.webp"
            hover_background recap_ui_path + "blue_hover.webp"
            action Return(girl["right_btn"])
            pos (933, 867)
            xysize (480, 200)

            text girl["right_btn"]:            
                style "recap_button_text"
                align (0.5, 0.5)

    on "show" action Hide("phone_icon")
