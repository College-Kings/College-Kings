screen letter1():
    add "images/darker.webp"
    add Transform("images/emilyletter.webp", size=(764, 1080))

    button:
        action Hide ("letter1")

screen hc_select():
    add "images/v7/homecomingchoice.webp"

    grid 4 2:
        spacing 40
        xalign 0.5
        ypos 285

        imagebutton:
            if "amber" not in hcAsked and not laurenrs:
                idle "images/v7/HCAmber.webp"
                hover "images/v7/HCAmber2.webp"
                tooltip "I'm not that close with Amber but she does seem quite flirty around me."

            else:
                idle "images/v7/HCAmber3.webp"
                hover "images/v7/HCAmber23.webp"
            
            if "amber" not in hcAsked and not laurenrs:
                action Jump("hc_asking_amber")
            else:
                action NullAction()

        imagebutton:
            if "aubrey" not in hcAsked and not laurenrs:
                idle "images/v7/HCAubrey.webp"
                hover "images/v7/HCAubrey2.webp"
            else:
                idle "images/v7/HCAubrey3.webp"
                hover "images/v7/HCAubrey23.webp"

            if aubreyrs:
                tooltip "I'm pretty sure that Aubrey would go with me and that would probably lead to a pretty hot night afterwards..."
            else:
                tooltip "Aubrey and I get along well, she might be down to go with me."
            
            if "aubrey" not in hcAsked and not laurenrs:
                action Jump("hc_asking_aubrey")
            else:
                action NullAction()

        imagebutton:
            if "autumn" not in hcAsked and not autumnmad and not laurenrs:
                idle "images/v7/HCAutumn.webp"
                hover "images/v7/HCAutumn2.webp"
            else:
                idle "images/v7/HCAutumn3.webp"
                hover "images/v7/HCAutumn23.webp"

            if autumnmad:
                tooltip "I think Autumn might be mad at me, so I probably shouldn't ask her."
            else:
                tooltip "Autumn and I aren't really close, but I'll never know if she'd say yes if I don't try."
            
            if "autumn" not in hcAsked and not (laurenrs or autumnmad):
                action Jump("hc_asking_autumn")
            else:
                action NullAction()

        imagebutton:
            if "chloe" not in hcAsked and not chloemad and not laurenrs:
                idle "images/v7/HCChloe.webp"
                hover "images/v7/HCChloe2.webp"
            else:
                idle "images/v7/HCChloe3.webp"
                hover "images/v7/HCChloe23.webp"

            if chloemad:
                tooltip "I think Chloe is mad at me, so I probably shouldn't ask her."
            else:
                tooltip "Chloe and I have been getting closer recently. Who knows, I might have a shot."
            
            if "chloe" not in hcAsked and not (laurenrs or chloemad):
                action Jump("hc_asking_chloe")
            else:
                action NullAction()

        imagebutton:
            if "emily" not in hcAsked and forgiveemily and not laurenrs:
                idle "images/v7/HCEmily.webp"
                hover "images/v7/HCEmily2.webp"
            else:
                idle "images/v7/HCEmily3.webp"
                hover "images/v7/HCEmily23.webp"

            if forgiveemily:
                tooltip "I could take Emily. She definitely still has a thing for me."
            else:
                tooltip "I don't think asking Emily is the right call."
            
            if "emily" not in hcAsked and not laurenrs and forgiveemily :
                action Jump("hc_asking_emily")
            else:
                action NullAction()

        imagebutton:
            if "lauren" not in hcAsked and not laurenmad:
                idle "images/v7/HCLauren.webp"
                hover "images/v7/HCLauren2.webp"
            else:
                idle "images/v7/HCLauren3.webp"
                hover "images/v7/HCLauren23.webp"

            if laurenmad:
                tooltip "It's kinda weird between Lauren and me, I probably should ask someone else."
            else:
                tooltip "I'm not sure Lauren sees me as more than a friend, but we have been getting closer."

            if "lauren" not in hcAsked:
                action Jump("hc_asking_lauren")
            else:
                action NullAction()

        imagebutton:
            if "penelope" not in hcAsked and not (bowling and emilyrs) and not laurenrs:
                idle "images/v7/HCPenelope.webp"
                hover "images/v7/HCPenelope2.webp"
            else:
                idle "images/v7/HCPenelope3.webp"
                hover "images/v7/HCPenelope23.webp"

            if bowling and emilyrs:
                tooltip "Penelope didn't seem too eager to talk to me today, I better ask someone else."
            elif bowling:
                tooltip "Penelope and I got along really well when we went bowling together, I think she could say yes."
            else:
                tooltip "I haven't done that much with Penelope so far, but maybe she'll yes."

            if "penelope" not in hcAsked and not laurenrs and not (bowling and emilyrs):
                action Jump("hc_asking_penelope")
            else:
                action NullAction()

        imagebutton:
            if "riley" not in hcAsked and not laurenrs:
                idle "images/v7/HCRiley.webp"
                hover "images/v7/HCRiley2.webp"
            else:
                idle "images/v7/HCRiley3.webp"
                hover "images/v7/HCRiley23.webp"

            if rileyrs:
                tooltip "Riley seems to really like me so I think she'll say yes."
            else:
                tooltip "Riley and I are good friends. She might say yes if I ask her."

            if "riley" not in hcAsked and not laurenrs:
                action Jump("hc_asking_riley")
            else:
                action NullAction()

    textbutton "Go Alone":
        pos (1500, 100)
        action Jump("hc_no_girl")


    $ tooltip = GetTooltip()

    if laurenrs:
        text "Lauren would kill me if I asked someone other than her.":
            color "#000"
            align (0.5, 0.88)

    elif tooltip:
        text tooltip:
            color "#000"
            xmaximum 700
            align (0.5, 0.88)

    else:
        text "I could always go alone...":
            color "#000"
            xmaximum 700
            align (0.5, 0.88)

# GYM
screen fr4dancefloor():

    if hcGirl == "chloe":
        if fr4nora and not fr4nora2:
            add "images/fr4dancefloorchloedatenonora.webp"
        else:
            add "images/fr4dancefloorchloedate.webp"

    elif hcGirl == "emily":
        if fr4nora and not fr4nora2:
            add "images/fr4danceflooremilydatenonora.webp"
        else:
            add "images/fr4danceflooremilydate.webp"

    elif hcGirl == "lauren":
        if fr4nora and not fr4nora2:
            add "images/fr4dancefloorlaurendatenonora.webp"
        else:
            add "images/fr4dancefloorlaurendate.webp"

    elif hcGirl == "penelope":
        if fr4nora and not fr4nora2:
            add "images/fr4dancefloorpenelopedatenonora.webp"
        else:
            add "images/fr4dancefloorpenelopedate.webp"

    elif hcGirl == "riley":
        if fr4nora and not fr4nora2:
            add "images/fr4dancefloorrileydatenonora.webp"
        else:
            add "images/fr4dancefloorrileydate.webp"

    else:
        if fr4nora and not fr4nora2:
            add "images/fr4dancefloornodatenonora.webp"
        else:
            add "images/fr4dancefloornodate.webp"

    if not fr4nora or fr4nora2:
        imagebutton:
            idle "images/fr4dancefloornora.webp"
            hover "images/fr4dancefloornorahover.webp"
            if fr4nora2:
                action Jump("fr4nora3")
            else:
                action Jump("fr4nora1")
    else:
        imagebutton:
            xpos 150
            idle "images/fr4dancefloorchris.webp"
            hover "images/fr4dancefloorchrishover.webp"
            action Jump("fr4chris1")

    imagebutton:
        pos (1100, 50)
        idle "images/fr4dancefloorelijah.webp"
        hover "images/fr4dancefloorelijahhover.webp"
        if not fr4elijah:
            action Jump("fr4elijah1")
        else:
            action Jump("fr4elijah2")

    imagebutton:
        pos (905, 85)
        idle "images/fr4dancefloormason.webp"
        hover "images/fr4dancefloormasonhover.webp"
        if not fr4mason:
            action Jump("fr4mason1")
        else:
            action Jump("fr4mason2")

    if hcGirl == "chloe":
        imagebutton:
            pos (645, 30)
            idle "images/fr4dancefloorchloe.webp"
            hover "images/fr4dancefloorchloehover.webp"
            action Show("v7_endFreeRoamConfirm", continueLabel="fr4chloedate", girl="Chloe")

    elif hcGirl == "emily":
        imagebutton:
            xpos 615
            idle "images/fr4danceflooremily.webp"
            hover "images/fr4danceflooremilyhover.webp"
            action Show("v7_endFreeRoamConfirm", continueLabel="fr4emilydate", girl="Emily")

    elif hcGirl == "lauren":
        imagebutton:
            xpos 617
            idle "images/fr4dancefloorlauren.webp"
            hover "images/fr4dancefloorlaurenhover.webp"
            action Show("v7_endFreeRoamConfirm", continueLabel="fr4laurendate", girl="Lauren")

    elif hcGirl == "penelope":
        imagebutton:
            xpos 655
            idle "images/fr4dancefloorpenelope.webp"
            hover "images/fr4dancefloorpenelopehover.webp"
            action Show("v7_endFreeRoamConfirm", continueLabel="fr4penelopedate", girl="Penelope")

    elif hcGirl == "riley":
        imagebutton:
            pos (675, 25)
            idle "images/fr4dancefloorriley.webp"
            hover "images/fr4dancefloorrileyhover.webp"
            action Show("v7_endFreeRoamConfirm", continueLabel="fr4rileydate", girl="Riley")

    imagebutton:
        align (0.5, 1.0)
        idle "images/fr4bottom.webp"
        hover "images/fr4bottomhover.webp"
        action Jump("labelfr4gymentrance")

    imagebutton:
        yalign 0.5
        idle "images/fr4left.webp"
        hover "images/fr4lefthover.webp"
        action Jump("labelfr4gymleft")

    imagebutton:
        align (1.0, 0.5)
        idle "images/fr4right.webp"
        hover "images/fr4righthover.webp"
        action Jump("labelfr4gymright")


screen fr4gymleft():

    if hcGirl == "chloe":
        if fr4riley:
            add "images/fr4gymleftnochloenoriley.webp"
        else:
            add "images/fr4gymleftnochloe.webp"

    elif hcGirl == "riley":
        if fr4chloe:
            add "images/fr4gymleftnochloenoriley.webp"
        else:
            add "images/fr4gymleftnoriley.webp"

    else:
        if fr4riley and fr4chloe:
            add "images/fr4gymleftnochloenoriley.webp"
        elif fr4riley:
            add "images/fr4gymleftnoriley.webp"
        elif fr4chloe:
            add "images/fr4gymleftnochloe.webp"
        else:
            add "images/fr4gymleft.webp"

    if not hcGirl == "chloe":
        if not fr4chloe:
            imagebutton:
                pos (375, 190)
                idle "images/fr4gymleftchloe.webp"
                hover "images/fr4gymleftchloehover.webp"
                action Jump("fr4chloe1")
        else:
            imagebutton:
                pos (63, 195)
                idle "images/fr4gymleftryan.webp"
                hover "images/fr4gymleftryanhover.webp"
                action Jump("fr4ryan3")

    else:
        imagebutton:
            pos (63, 195)
            idle "images/fr4gymleftryan.webp"
            hover "images/fr4gymleftryanhover.webp"
            action Jump("fr4ryan1")

    if not hcGirl == "riley" and not fr4riley:
        imagebutton:
            pos (1485, 215)
            idle "images/fr4gymleftriley.webp"
            hover "images/fr4gymleftrileyhover.webp"
            action Jump("fr4riley1")

    else:
        imagebutton:
            pos (1520, 225)
            idle "images/fr4gymleftaubrey.webp"
            hover "images/fr4gymleftaubreyhover.webp"
            if not fr4aubrey:
                action Jump("fr4aubrey1")
            else:
                action Jump("fr4aubrey2")

    imagebutton:
        align (0.5, 1.0)
        idle "images/fr4bottom.webp"
        hover "images/fr4bottomhover.webp"
        action Jump("labelfr4dancefloor")


screen fr4gymright():

    if hcGirl == "lauren":
        add "images/fr4gymrightnolauren.webp"
    else:
        add "images/fr4gymright.webp"

    if not hcGirl == "lauren":
        imagebutton:
            pos (1492, 355)
            idle "images/fr4gymrightlauren.webp"
            hover "images/fr4gymrightlaurenhover.webp"
            if not fr4lauren:
                action Jump("fr4lauren1")
            else:
                action Jump("fr4lauren2")
    else:
        imagebutton:
            pos (1775, 335)
            idle "images/fr4gymrightmsrose.webp"
            hover "images/fr4gymrightmsrosehover.webp"
            if not fr4msrose:
                action Jump("fr4msrose1")
            else:
                action Jump("fr4msrose2")

    imagebutton:
        ypos 360
        idle "images/fr4gymrightcameron.webp"
        hover "images/fr4gymrightcameronhover.webp"
        if not fr4cameron:
            action Jump("fr4cameron1")
        else:
            action Jump("fr4cameron2")

    imagebutton:
        align (0.5, 1.0)
        idle "images/fr4bottom.webp"
        hover "images/fr4bottomhover.webp"
        action Jump("labelfr4dancefloor")


screen fr4gymentrance():

    if fr4riley and not fr4noriley and fr4nora and not fr4nora2:
        add "images/fr4gymentrancerileynora.webp"
    elif fr4riley and not fr4noriley:
        add "images/fr4gymentranceriley.webp"
    elif fr4nora and not fr4nora2:
        add "images/fr4gymentrancenora.webp"
    else:
        add "images/fr4gymentrance.webp"

    if fr4riley and not fr4noriley:
        imagebutton:
            pos (365, 318)
            idle "images/fr4gymentrancerileyidle.webp"
            hover "images/fr4gymentrancerileyhover.webp"
            action Show("v7_endFreeRoamConfirm", continueLabel="fr4riley2", girl="Riley")

    if fr4nora and not fr4nora2:
        imagebutton:
            ypos 315
            idle "images/fr4gymentrancenoraidle.webp"
            hover "images/fr4gymentrancenorahover.webp"
            action Jump("fr4nora2")

    imagebutton:
        pos (1235, 440)
        idle "images/fr4gymentranceaaron.webp"
        hover "images/fr4gymentranceaaronhover.webp"
        if not fr4aaron:
            action Jump("fr4aaron1")
        else:
            action Jump("fr4aaron2")

    imagebutton:
        align (0.5, 1.0)
        idle "images/fr4bottom.webp"
        hover "images/fr4bottomhover.webp"
        action Jump("labelfr4dancefloor")

    imagebutton:
        pos (710, 285)
        idle "images/fr4gymentrancedoor.webp"
        hover "images/fr4gymentrancedoorhover.webp"
        action Jump("labelfr4hallwaygymexit")


### Hallway ###
screen fr4hallwaygymexit():

    add "images/fr4hallwaygymexit.webp"

    imagebutton:
        align (0.5, 1.0)
        idle "images/fr4bottom.webp"
        hover "images/fr4bottomhover.webp"
        action Jump("labelfr4gymentrance")

    imagebutton:
        align (1.0, 0.5)
        idle "images/fr4right.webp"
        hover "images/fr4righthover.webp"
        action Jump("labelfr4hallwaybathroom")

    imagebutton:
        yalign 0.5
        idle "images/fr4left.webp"
        hover "images/fr4lefthover.webp"
        action Jump("labelfr4hallway")


screen fr4hallwaybathroom():

    add "images/fr4hallwaybathroom.webp"

    imagebutton:
        align (0.5, 1.0)
        idle "images/fr4bottom.webp"
        hover "images/fr4bottomhover.webp"
        action Jump("labelfr4hallwaygymexit")

    imagebutton:
        pos (737, 130)
        idle "images/fr4hallwaybathroomdoor.webp"
        hover "images/fr4hallwaybathroomdoorhover.webp"
        if not fr4imre:
            action Jump("fr4imre1")
        else:
            action Jump("fr4imre2")


screen fr4hallway():

    if not hcGirl == "penelope":
        if fr4chloe and preventgrayson:
            add "images/fr4hallwaychloe.webp"
        else:
            add "images/fr4hallway.webp"
    else:
        if fr4chloe and preventgrayson:
            add "images/fr4hallwaynopenelopechloe.webp"
        else:
            add "images/fr4hallwaynopenelope.webp"

    if fr4chloe and preventgrayson:
        imagebutton:
            pos (1035, 175)
            idle "images/fr4hallwaychloeidle.webp"
            hover "images/fr4hallwaychloehover.webp"
            if not fr4chloe2:
                action Show("v7_endFreeRoamConfirm", continueLabel="fr4chloe2", girl="Chloe")
            else:
                action Jump("fr4chloe3")

    if not hcGirl == "penelope":
        imagebutton:
            pos (535, 105)
            idle "images/fr4hallwaypenelope.webp"
            hover "images/fr4hallwaypenelopehover.webp"
            if not fr4penelope:
                action Jump("fr4penelope1")
            else:
                action Jump("fr4penelope2")

    imagebutton:
        pos (770, 70)
        idle "images/fr4hallwaycornerpath.webp"
        hover "images/fr4hallwaycornerpathhover.webp"
        action Jump("labelfr4hallwaycorner")

    imagebutton:
        pos (835, 160)
        idle "images/fr4hallwaydoor.webp"
        hover "images/fr4hallwaydoorhover.webp"
        action Jump("labelfr4outsidestairs")

    imagebutton:
        align (0.5, 1.0)
        idle "images/fr4bottom.webp"
        hover "images/fr4bottomhover.webp"
        action Jump("labelfr4hallwaygymexit")


screen fr4hallwaycorner():

    if not fr4grayson:
        add "images/fr4hallwaycorner.webp"
    elif preventgrayson:
        add "images/fr4hallwaycornernumber.webp"
    else:
        add "images/fr4hallwaycornernograyson.webp"

    imagebutton:
        pos (875, 205)
        idle "images/fr4hallwaycornerdoor.webp"
        hover "images/fr4hallwaycornerdoorhover.webp"
        if fr4chloe and not preventgrayson:
            action Show("v7_endFreeRoamConfirm", continueLabel="fr4lockerroomchloe", girl="Chloe")
        else:
            action Jump("fr4lockerroom")

    if not fr4grayson:
        imagebutton:
            pos (320, 395)
            idle "images/fr4hallwaycornergrayson.webp"
            hover "images/fr4hallwaycornergraysonhover.webp"
            action Jump("fr4grayson1")

    imagebutton:
        align (0.5, 1.0)
        idle "images/fr4bottom.webp"
        hover "images/fr4bottomhover.webp"
        action Jump("labelfr4hallway")


### Outside ###
screen fr4outsidestairs():

    if not hcGirl == "emily":
        add "images/fr4outsidestairs.webp"
    else:
        add "images/fr4outsidestairsnoemily.webp"

    if not hcGirl == "emily":
        imagebutton:
            pos (520, 295)
            idle "images/fr4outsidestairsemily.webp"
            hover "images/fr4outsidestairsemilyhover.webp"
            if not fr4emily:
                action Jump("fr4emily1")
            else:
                action Jump("fr4emily2")

    imagebutton:
        align (0.5, 1.0)
        idle "images/fr4bottom.webp"
        hover "images/fr4bottomhover.webp"
        action Jump("labelfr4hallway")

    imagebutton:
        align (1.0, 0.5)
        idle "images/fr4right.webp"
        hover "images/fr4righthover.webp"
        action Jump("labelfr4outsidestreet")


screen fr4outsidestreet():

    add "images/fr4outsidestreet.webp"

    imagebutton:
        pos (830, 340)
        idle "images/fr4outsidestreetidle.webp"
        hover "images/fr4outsidestreethover.webp"
        if not fr4samantha:
            action Jump("fr4samantha1")
        else:
            action Jump("fr4samantha2")

    imagebutton:
        align (0.5, 1.0)
        idle "images/fr4bottom.webp"
        hover "images/fr4bottomhover.webp"
        action Jump("labelfr4outsidestairs")


screen v7_endFreeRoamConfirm(continueLabel, girl):
    modal True
    
    use endfrTemplate:

        text "Are you sure you want to end the free roam with [girl]?":
            style "endfree"
            xalign 0.5

        hbox:
            align (0.5, 1.0)
            spacing 200

            textbutton "Yes":
                action [Hide("v7_endFreeRoamConfirm"), SetVariable("freeRoam", False), Jump(continueLabel)]
                
            textbutton "No":
                action Hide("v7_endFreeRoamConfirm")


screen rileysexoverlay():

    default overlay = True

    if overlay:
        textbutton "hide overlay":
            xpos 250
            action SetScreenVariable("overlay", False)
    else:
        textbutton "show overlay":
            xpos 10
            action SetScreenVariable("overlay", True)

    if overlay:
        vpgrid:
            cols 1
            pos (10, 10)
            mousewheel True
            draggable True

            imagebutton:
                idle "images/riblowjob.webp"
                hover "images/riblowjob.webp"
                action Jump("riblowjob")

            imagebutton:
                idle "images/rifingering.webp"
                hover "images/rifingering.webp"
                action Jump("rifingering")

            imagebutton:
                idle "images/rimissionary.webp"
                hover "images/rimissionary.webp"
                action Jump("rimissionary")

            imagebutton:
                idle "images/riclimax.webp"
                hover "images/riclimax.webp"
                action Jump("riclimax")