screen letter1():
    add "darker_80"
    add Transform("images/v7/emilyletter.webp", size=(764, 1080))

    button:
        action Hide("letter1")

screen hc_select():
    modal True

    default image_path = "images/v7/HC_Date_Select_screen/"
    default girl_path = "gui/julia_call/"

    $ girl_labels = {
        _("Amber"): {
            "label": "hc_asking_amber",
            "condition": ("amber" not in hcAsked) and not CharacterService.is_girlfriend(lauren),
            "tooltip": _("I'm not that close with Amber but she does seem quite flirty around me")
        },
        _("Aubrey"): {
            "label": "hc_asking_aubrey",
            "condition": ("aubrey" not in hcAsked) and not CharacterService.is_girlfriend(lauren),
            "tooltip": (_("Aubrey and I get along well, she might be down to go with me.")
                if aubrey.relationship < Relationship.FWB else
                _("I'm pretty sure that Aubrey would go with me and that would probably lead to a pretty hot night afterwards..."))
        },
        _("Autumn"): {
            "label": "hc_asking_autumn",
            "condition": ("autumn" not in hcAsked) and (not CharacterService.is_mad(autumn)) and not CharacterService.is_girlfriend(lauren),
            "tooltip": (_("Autumn and I aren't really close, but I'll never know if she'd say yes if I don't try.")
                if not CharacterService.is_mad(autumn) else
                _("I think Autumn might be mad at me, so I probably shouldn't ask her."))
        },
        _("Chloe"): {
            "label": "hc_asking_chloe",
            "condition": ("chloe" not in hcAsked) and not CharacterService.is_mad(chloe) and not CharacterService.is_girlfriend(lauren),
            "tooltip": (_("Chloe and I have been getting closer recently. Who knows, I might have a shot.")
                if not CharacterService.is_mad(chloe) else
                _("I think Chloe is mad at me, so I probably shouldn't ask her."))
        },
        _("Emily"): {
            "label": "hc_asking_emily",
            "condition": ("emily" not in hcAsked) and (forgiveemily) and not CharacterService.is_girlfriend(lauren),
            "tooltip": (_("I could take Emily. She definitely still has a thing for me.")
                if forgiveemily else
                _("I don't think asking Emily is the right call."))
        },
        _("Lauren"): {
            "label": "hc_asking_lauren",
            "condition": ("lauren" not in hcAsked) and not CharacterService.is_mad(lauren),
            "tooltip": (_("I'm not sure Lauren sees me as more than a friend, but we have been getting closer.")
                if not CharacterService.is_mad(lauren) else
                _("It's kinda weird between Lauren and me, I probably should ask someone else."))
        },
        _("Penelope"): {
            "label": "hc_asking_penelope",
            "condition": ("penelope" not in hcAsked) and (not v7_emily_bowling) and not CharacterService.is_girlfriend(lauren),
            "tooltip": (_("Penelope didn't seem too eager to talk to me today, I better ask someone else.")
                if v7_emily_bowling else
                _("Penelope and I got along really well when we went bowling together, I think she could say yes.")
                if bowling else
                _("I haven't done that much with Penelope so far, but maybe she'll yes."))
        },
        _("Riley"): {
            "label": "hc_asking_riley",
            "condition": ("riley" not in hcAsked) and not CharacterService.is_girlfriend(lauren),
            "tooltip": (_("Riley and I are good friends. She might say yes if I ask her.")
                if riley.relationship < Relationship.LIKES else
                _("Riley and I are good friends. She might say yes if I ask her."))
        }
    }

    add image_path + "hoco_date_select_background.webp"        

    imagebutton:
        idle image_path + "go_alone_idle.webp"
        action Jump("hc_no_girl")
        pos (1460, 105)

    vpgrid:
        rows 2
        cols 4
        spacing 30
        xalign 0.5
        ypos 400

        for character, i in girl_labels.items():
            button:
                idle_background girl_path + "{}_idle.webp".format(character)
                hover_background girl_path + "{}.webp".format(character)
                insensitive_background girl_path + "{}_grey.webp".format(character)
                sensitive i["condition"]
                tooltip i["tooltip"]
                action Jump(i["label"])
                xysize (307, 112)

                text character:
                    xpos 120
                    yalign 0.5
                    size 30

    $ tooltip = GetTooltip()
    
    if CharacterService.is_girlfriend(lauren, Relationship.GIRLFRIEND):
        $ message = _("Lauren would kill me if I asked someone other than her.")
    elif tooltip:
        $ message = tooltip
    else:
        $ message = _("I could always go alone...")
    
    text message:
        color "#FFF"
        size 35
        xalign 0.5
        ypos 920

    if config_debug:
        timer 0.1 action Jump(renpy.random.choice([i["label"] for i in girl_labels.values()]))


# GYM
screen fr4dancefloor():
    if hcGirl == "chloe":
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            add "images/v7/fr4dancefloorchloedatenonora.webp"
        else:
            add "images/v7/fr4dancefloorchloedate.webp"

    elif hcGirl == "emily":
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            add "images/v7/fr4danceflooremilydatenonora.webp"
        else:
            add "images/v7/fr4danceflooremilydate.webp"

    elif hcGirl == "lauren":
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            add "images/v7/fr4dancefloorlaurendatenonora.webp"
        else:
            add "images/v7/fr4dancefloorlaurendate.webp"

    elif hcGirl == "penelope":
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            add "images/v7/fr4dancefloorpenelopedatenonora.webp"
        else:
            add "images/v7/fr4dancefloorpenelopedate.webp"

    elif hcGirl == "riley":
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            add "images/v7/fr4dancefloorrileydatenonora.webp"
        else:
            add "images/v7/fr4dancefloorrileydate.webp"

    else:
        if "nora" in freeroam4 and not "nora2" in freeroam4:
            add "images/v7/fr4dancefloornodatenonora.webp"
        else:
            add "images/v7/fr4dancefloornodate.webp"

    if not "nora" in freeroam4 or "nora2" in freeroam4:
        imagebutton:
            idle "images/v7/fr4dancefloornora.webp"
            hover "images/v7/fr4dancefloornorahover.webp"
            if "nora2" in freeroam4:
                action Jump("fr4nora3")
            else:
                action Jump("fr4nora1")
    else:
        imagebutton:
            xpos 150
            idle "images/v7/fr4dancefloorchris.webp"
            hover "images/v7/fr4dancefloorchrishover.webp"
            action Jump("fr4chris1")

    imagebutton:
        pos (1100, 50)
        idle "images/v7/fr4dancefloorelijah.webp"
        hover "images/v7/fr4dancefloorelijahhover.webp"
        if not "elijah" in freeroam4:
            action Jump("fr4elijah1")
        else:
            action Jump("fr4elijah2")

    imagebutton:
        pos (905, 85)
        idle "images/v7/fr4dancefloormason.webp"
        hover "images/v7/fr4dancefloormasonhover.webp"
        if not "mason" in freeroam4:
            action Jump("fr4mason1")
        else:
            action Jump("fr4mason2")

    if hcGirl == "chloe":
        imagebutton:
            pos (645, 30)
            idle "images/v7/fr4dancefloorchloe.webp"
            hover "images/v7/fr4dancefloorchloehover.webp"
            action Show("confirm", message=_("Are you sure you want to end the free roam with Chloe?"), yes_action=[Hide("confirm"), Jump("fr4chloedate")])

    elif hcGirl == "emily":
        imagebutton:
            xpos 615
            idle "images/v7/fr4danceflooremily.webp"
            hover "images/v7/fr4danceflooremilyhover.webp"
            action Show("confirm", message=_("Are you sure you want to end the free roam with Emily?"), yes_action=[Hide("confirm"), Jump("fr4emilydate")])

    elif hcGirl == "lauren":
        imagebutton:
            xpos 617
            idle "images/v7/fr4dancefloorlauren.webp"
            hover "images/v7/fr4dancefloorlaurenhover.webp"
            action Show("confirm", message=_("Are you sure you want to end the free roam with Lauren?"), yes_action=[Hide("confirm"), Jump("fr4laurendate")])

    elif hcGirl == "penelope":
        imagebutton:
            xpos 655
            idle "images/v7/fr4dancefloorpenelope.webp"
            hover "images/v7/fr4dancefloorpenelopehover.webp"
            action Show("confirm", message=_("Are you sure you want to end the free roam with Penelope?"), yes_action=[Hide("confirm"), Jump("fr4penelopedate")])

    elif hcGirl == "riley":
        imagebutton:
            pos (675, 25)
            idle "images/v7/fr4dancefloorriley.webp"
            hover "images/v7/fr4dancefloorrileyhover.webp"
            action Show("confirm", message=_("Are you sure you want to end the free roam with Riley?"), yes_action=[Hide("confirm"), Jump("fr4rileydate")])

    imagebutton:
        align (0.5, 1.0)
        idle "images/v7/fr4bottom.webp"
        hover "images/v7/fr4bottomhover.webp"
        action Jump("labelfr4gymentrance")

    imagebutton:
        yalign 0.5
        idle "images/v7/fr4left.webp"
        hover "images/v7/fr4lefthover.webp"
        action Jump("labelfr4gymleft")

    imagebutton:
        align (1.0, 0.5)
        idle "images/v7/fr4right.webp"
        hover "images/v7/fr4righthover.webp"
        action Jump("labelfr4gymright")

    if config_debug:
        python:
            actions = []

            if not "nora" in freeroam4 or "nora2" in freeroam4:
                if "nora2" in freeroam4:
                    actions.append(Jump("fr4nora3"))
            else:
                actions.append(Jump("fr4chris1"))

            if not "elijah" in freeroam4:
                actions.append(Jump("fr4elijah1"))

            if not "mason" in freeroam4:
                actions.append(Jump("fr4mason1"))

            if hcGirl == "chloe":
                actions.append(Show("confirm", message="Are you sure you want to end the free roam with Chloe?", yes_action=[Hide("confirm"), Jump("fr4chloedate")]))

            elif hcGirl == "emily":
                actions.append(Show("confirm", message="Are you sure you want to end the free roam with Emily?", yes_action=[Hide("confirm"), Jump("fr4emilydate")]))

            elif hcGirl == "lauren":
                actions.append(Show("confirm", message="Are you sure you want to end the free roam with Lauren?", yes_action=[Hide("confirm"), Jump("fr4laurendate")]))

            elif hcGirl == "penelope":
                actions.append(Show("confirm", message="Are you sure you want to end the free roam with Penelope?", yes_action=[Hide("confirm"), Jump("fr4penelopedate")]))

            elif hcGirl == "riley":
                actions.append(Show("confirm", message="Are you sure you want to end the free roam with Riley?", yes_action=[Hide("confirm"), Jump("fr4rileydate")]))

            actions.append(Jump("labelfr4gymentrance"))

            actions.append(Jump("labelfr4gymleft"))

            actions.append(Jump("labelfr4gymright"))

        timer 0.1 action renpy.random.choice(actions)


screen fr4gymleft():

    if hcGirl == "chloe":
        if "riley" in freeroam4:
            add "images/v7/fr4gymleftnochloenoriley.webp"
        else:
            add "images/v7/fr4gymleftnochloe.webp"

    elif hcGirl == "riley":
        if "chloe" in freeroam4:
            add "images/v7/fr4gymleftnochloenoriley.webp"
        else:
            add "images/v7/fr4gymleftnoriley.webp"

    else:
        if "riley" in freeroam4 and "chloe" in freeroam4:
            add "images/v7/fr4gymleftnochloenoriley.webp"
        elif "riley" in freeroam4:
            add "images/v7/fr4gymleftnoriley.webp"
        elif "chloe" in freeroam4:
            add "images/v7/fr4gymleftnochloe.webp"
        else:
            add "images/v7/fr4gymleft.webp"

    if not hcGirl == "chloe":
        if not "chloe" in freeroam4:
            imagebutton:
                pos (375, 190)
                idle "images/v7/fr4gymleftchloe.webp"
                hover "images/v7/fr4gymleftchloehover.webp"
                action Jump("fr4chloe1")
        else:
            imagebutton:
                pos (63, 195)
                idle "images/v7/fr4gymleftryan.webp"
                hover "images/v7/fr4gymleftryanhover.webp"
                action Jump("fr4ryan3")

    else:
        imagebutton:
            pos (63, 195)
            idle "images/v7/fr4gymleftryan.webp"
            hover "images/v7/fr4gymleftryanhover.webp"
            action Jump("fr4ryan1")

    if not hcGirl == "riley" and not "riley" in freeroam4:
        imagebutton:
            pos (1485, 215)
            idle "images/v7/fr4gymleftriley.webp"
            hover "images/v7/fr4gymleftrileyhover.webp"
            action Jump("fr4riley1")

    else:
        imagebutton:
            pos (1520, 225)
            idle "images/v7/fr4gymleftaubrey.webp"
            hover "images/v7/fr4gymleftaubreyhover.webp"
            if not "aubrey" in freeroam4:
                action Jump("fr4aubrey1")
            else:
                action Jump("fr4aubrey2")

    imagebutton:
        align (0.5, 1.0)
        idle "images/v7/fr4bottom.webp"
        hover "images/v7/fr4bottomhover.webp"
        action Jump("labelfr4dancefloor")

    if config_debug:
        python:
            actions = []

            if not hcGirl == "chloe":
                if not "chloe" in freeroam4:
                    actions.append(Jump("fr4chloe1"))

            else:
                actions.append(Jump("fr4ryan1"))

            if not hcGirl == "riley" and not "riley" in freeroam4:
                actions.append(Jump("fr4riley1"))

            else:
                if not "aubrey" in freeroam4:
                    actions.append(Jump("fr4aubrey1"))

            actions.append(Jump("labelfr4dancefloor"))

        timer 0.1 action renpy.random.choice(actions)


screen fr4gymright():

    if hcGirl == "lauren":
        add "images/v7/fr4gymrightnolauren.webp"
    else:
        add "images/v7/fr4gymright.webp"

    if not hcGirl == "lauren":
        imagebutton:
            pos (1492, 355)
            idle "images/v7/fr4gymrightlauren.webp"
            hover "images/v7/fr4gymrightlaurenhover.webp"
            if not "lauren" in freeroam4:
                action Jump("fr4lauren1")
            else:
                action Jump("fr4lauren2")
    else:
        imagebutton:
            pos (1775, 335)
            idle "images/v7/fr4gymrightmsrose.webp"
            hover "images/v7/fr4gymrightmsrosehover.webp"
            if not "rose" in freeroam4:
                action Jump("fr4msrose1")
            else:
                action Jump("fr4msrose2")

    imagebutton:
        ypos 360
        idle "images/v7/fr4gymrightcameron.webp"
        hover "images/v7/fr4gymrightcameronhover.webp"
        if not "cameron" in freeroam4:
            action Jump("fr4cameron1")
        else:
            action Jump("fr4cameron2")

    imagebutton:
        align (0.5, 1.0)
        idle "images/v7/fr4bottom.webp"
        hover "images/v7/fr4bottomhover.webp"
        action Jump("labelfr4dancefloor")

    if config_debug:
        python:
            actions = []

            if not hcGirl == "lauren":
                if not "lauren" in freeroam4:
                    actions.append(Jump("fr4lauren1"))

            else:
                if not "rose" in freeroam4:
                    actions.append(Jump("fr4msrose1"))

            if not "cameron" in freeroam4:
                actions.append(Jump("fr4cameron1"))

            actions.append(Jump("labelfr4dancefloor"))

        timer 0.1 action renpy.random.choice(actions)


screen fr4gymentrance():

    if "riley" in freeroam4 and not "riley2" in freeroam4 and "nora" in freeroam4 and not "nora2" in freeroam4:
        add "images/v7/fr4gymentrancerileynora.webp"
    elif "riley" in freeroam4 and not "riley2" in freeroam4:
        add "images/v7/fr4gymentranceriley.webp"
    elif "nora" in freeroam4 and not "nora2" in freeroam4:
        add "images/v7/fr4gymentrancenora.webp"
    else:
        add "images/v7/fr4gymentrance.webp"

    if "riley" in freeroam4 and not "riley2" in freeroam4:
        imagebutton:
            pos (365, 318)
            idle "images/v7/fr4gymentrancerileyidle.webp"
            hover "images/v7/fr4gymentrancerileyhover.webp"
            action Show("confirm", message=_("Are you sure you want to end the free roam with Riley?"), yes_action=[Hide("confirm"), Jump("fr4riley2")])

    if "nora" in freeroam4 and not "nora2" in freeroam4:
        imagebutton:
            ypos 315
            idle "images/v7/fr4gymentrancenoraidle.webp"
            hover "images/v7/fr4gymentrancenorahover.webp"
            action Jump("fr4nora2")

    imagebutton:
        pos (1235, 440)
        idle "images/v7/fr4gymentranceaaron.webp"
        hover "images/v7/fr4gymentranceaaronhover.webp"
        if not "aaron" in freeroam4:
            action Jump("fr4aaron1")
        else:
            action Jump("fr4aaron2")

    imagebutton:
        align (0.5, 1.0)
        idle "images/v7/fr4bottom.webp"
        hover "images/v7/fr4bottomhover.webp"
        action Jump("labelfr4dancefloor")

    imagebutton:
        pos (710, 285)
        idle "images/v7/fr4gymentrancedoor.webp"
        hover "images/v7/fr4gymentrancedoorhover.webp"
        action Jump("labelfr4hallwaygymexit")

    if config_debug:
        python:
            actions = []

            if "riley" in freeroam4 and not "riley2" in freeroam4:
                actions.append(Show("confirm", message="Are you sure you want to end the free roam with Riley?", yes_action=[Hide("confirm"), Jump("fr4riley2")]))

            if "nora" in freeroam4 and not "nora2" in freeroam4:
                actions.append(Jump("fr4nora2"))

            if not "aaron" in freeroam4:
                actions.append(Jump("fr4aaron1"))

            actions.append(Jump("labelfr4dancefloor"))
            
            actions.append(Jump("labelfr4hallwaygymexit"))

        timer 0.1 action renpy.random.choice(actions)


### Hallway ###
screen fr4hallwaygymexit():

    add "images/v7/fr4hallwaygymexit.webp"

    imagebutton:
        align (0.5, 1.0)
        idle "images/v7/fr4bottom.webp"
        hover "images/v7/fr4bottomhover.webp"
        action Jump("labelfr4gymentrance")

    imagebutton:
        align (1.0, 0.5)
        idle "images/v7/fr4right.webp"
        hover "images/v7/fr4righthover.webp"
        action Jump("labelfr4hallwaybathroom")

    imagebutton:
        yalign 0.5
        idle "images/v7/fr4left.webp"
        hover "images/v7/fr4lefthover.webp"
        action Jump("labelfr4hallway")

    if config_debug:
        timer 0.1 action Jump(renpy.random.choice(("labelfr4gymentrance", "labelfr4hallwaybathroom", "labelfr4hallway")))


screen fr4hallwaybathroom():

    add "images/v7/fr4hallwaybathroom.webp"

    imagebutton:
        align (0.5, 1.0)
        idle "images/v7/fr4bottom.webp"
        hover "images/v7/fr4bottomhover.webp"
        action Jump("labelfr4hallwaygymexit")

    imagebutton:
        pos (737, 130)
        idle "images/v7/fr4hallwaybathroomdoor.webp"
        hover "images/v7/fr4hallwaybathroomdoorhover.webp"
        if not "imre" in freeroam4:
            action Jump("fr4imre1")
        else:
            action Jump("fr4imre2")

    if config_debug:
        python:
            labels = ["labelfr4hallwaygymexit"]

            if not "imre" in freeroam4:
                labels.append("fr4imre1")

        timer 0.1 action Jump(renpy.random.choice(labels))


screen fr4hallway():

    if not hcGirl == "penelope":
        if "chloe" in freeroam4 and preventgrayson:
            add "images/v7/fr4hallwaychloe.webp"
        else:
            add "images/v7/fr4hallway.webp"
    else:
        if "chloe" in freeroam4 and preventgrayson:
            add "images/v7/fr4hallwaynopenelopechloe.webp"
        else:
            add "images/v7/fr4hallwaynopenelope.webp"

    if "chloe" in freeroam4 and preventgrayson:
        imagebutton:
            pos (1035, 175)
            idle "images/v7/fr4hallwaychloeidle.webp"
            hover "images/v7/fr4hallwaychloehover.webp"
            if not "chloe2" in freeroam4:
                action Show("confirm", message=_("Are you sure you want to end the free roam with Chloe?"), yes_action=[Hide("confirm"), Jump("fr4chloe2")])
            else:
                action Jump("fr4chloe3")

    if not hcGirl == "penelope":
        imagebutton:
            pos (535, 105)
            idle "images/v7/fr4hallwaypenelope.webp"
            hover "images/v7/fr4hallwaypenelopehover.webp"
            if not "penelope" in freeroam4:
                action Jump("fr4penelope1")
            else:
                action Jump("fr4penelope2")

    imagebutton:
        pos (770, 70)
        idle "images/v7/fr4hallwaycornerpath.webp"
        hover "images/v7/fr4hallwaycornerpathhover.webp"
        action Jump("labelfr4hallwaycorner")

    imagebutton:
        pos (835, 160)
        idle "images/v7/fr4hallwaydoor.webp"
        hover "images/v7/fr4hallwaydoorhover.webp"
        action Jump("labelfr4outsidestairs")

    imagebutton:
        align (0.5, 1.0)
        idle "images/v7/fr4bottom.webp"
        hover "images/v7/fr4bottomhover.webp"
        action Jump("labelfr4hallwaygymexit")

    if config_debug:
        python:
            actions = []

            if "chloe" in freeroam4 and preventgrayson:
                if not "chloe2" in freeroam4:
                    actions.append(Show("confirm", message="Are you sure you want to end the free roam with Chloe?", yes_action=[Hide("confirm"), Jump("fr4chloe2")]))

            if not hcGirl == "penelope":
                if not "penelope" in freeroam4:
                    actions.append(Jump("fr4penelope1"))

            actions.append(Jump("labelfr4hallwaycorner"))

            actions.append(Jump("labelfr4outsidestairs"))

            actions.append(Jump("labelfr4hallwaygymexit"))

        timer 0.1 action renpy.random.choice(actions)


screen fr4hallwaycorner():

    if not "grayson" in freeroam4:
        add "images/v7/fr4hallwaycorner.webp"
    elif preventgrayson:
        add "images/v7/fr4hallwaycornernumber.webp"
    else:
        add "images/v7/fr4hallwaycornernograyson.webp"

    imagebutton:
        pos (875, 205)
        idle "images/v7/fr4hallwaycornerdoor.webp"
        hover "images/v7/fr4hallwaycornerdoorhover.webp"
        if "chloe" in freeroam4 and not preventgrayson:
            action Show("confirm", message=_("Are you sure you want to end the free roam with Chloe?"), yes_action=[Hide("confirm"), Jump("fr4lockerroomchloe")])
        else:
            action Jump("fr4lockerroom")

    if not "grayson" in freeroam4:
        imagebutton:
            pos (320, 395)
            idle "images/v7/fr4hallwaycornergrayson.webp"
            hover "images/v7/fr4hallwaycornergraysonhover.webp"
            action Jump("fr4grayson1")

    imagebutton:
        align (0.5, 1.0)
        idle "images/v7/fr4bottom.webp"
        hover "images/v7/fr4bottomhover.webp"
        action Jump("labelfr4hallway")

    if config_debug:
        python:
            actions = []

            if "chloe" in freeroam4 and not preventgrayson:
                actions.append(Show("confirm", message="Are you sure you want to end the free roam with Chloe?", yes_action=[Hide("confirm"), Jump("fr4lockerroomchloe")]))

            if not "grayson" in freeroam4:
                actions.append(Jump("fr4grayson1"))

            actions.append(Jump("labelfr4hallway"))

        timer 0.1 action renpy.random.choice(actions)


### Outside ###
screen fr4outsidestairs():

    if not hcGirl == "emily":
        add "images/v7/fr4outsidestairs.webp"
    else:
        add "images/v7/fr4outsidestairsnoemily.webp"

    if not hcGirl == "emily":
        imagebutton:
            pos (520, 295)
            idle "images/v7/fr4outsidestairsemily.webp"
            hover "images/v7/fr4outsidestairsemilyhover.webp"
            if not "emily" in freeroam4:
                action Jump("fr4emily1")
            else:
                action Jump("fr4emily2")

    imagebutton:
        align (0.5, 1.0)
        idle "images/v7/fr4bottom.webp"
        hover "images/v7/fr4bottomhover.webp"
        action Jump("labelfr4hallway")

    imagebutton:
        align (1.0, 0.5)
        idle "images/v7/fr4right.webp"
        hover "images/v7/fr4righthover.webp"
        action Jump("labelfr4outsidestreet")

    if config_debug:
        python:
            actions = []

            if not hcGirl == "emily":
                if not "emily" in freeroam4:
                    actions.append(Jump("fr4emily1"))

            actions.append(Jump("labelfr4hallway"))

            actions.append(Jump("labelfr4outsidestreet"))

        timer 0.1 action renpy.random.choice(actions)


screen fr4outsidestreet():

    add "images/v7/fr4outsidestreet.webp"

    imagebutton:
        pos (830, 340)
        idle "images/v7/fr4outsidestreetidle.webp"
        hover "images/v7/fr4outsidestreethover.webp"
        if not "samantha" in freeroam4:
            action Jump("fr4samantha1")
        else:
            action Jump("fr4samantha2")

    imagebutton:
        align (0.5, 1.0)
        idle "images/v7/fr4bottom.webp"
        hover "images/v7/fr4bottomhover.webp"
        action Jump("labelfr4outsidestairs")

    if config_debug:
        python:
            actions = []

            if not "samantha" in freeroam4:
                actions.append(Jump("fr4samantha1"))

            actions.append(Jump("labelfr4outsidestairs"))

        timer 0.1 action renpy.random.choice(actions)


screen rileysexoverlay():

    default overlay = True

    if overlay:
        textbutton _("hide overlay"):
            xpos 250
            action SetScreenVariable("overlay", False)
    else:
        textbutton _("show overlay"):
            xpos 10
            action SetScreenVariable("overlay", True)

    if overlay:
        vpgrid:
            cols 1
            pos (10, 10)
            mousewheel True
            draggable True

            imagebutton:
                idle "images/v7/riblowjob.webp"
                hover "images/v7/riblowjob.webp"
                action Jump("riblowjob")

            imagebutton:
                idle "images/v7/rifingering.webp"
                hover "images/v7/rifingering.webp"
                action Jump("rifingering")

            imagebutton:
                idle "images/v7/rimissionary.webp"
                hover "images/v7/rimissionary.webp"
                action Jump("rimissionary")

            imagebutton:
                idle "images/v7/riclimax.webp"
                hover "images/v7/riclimax.webp"
                action Jump("riclimax")
