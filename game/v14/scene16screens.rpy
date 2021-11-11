screen loyalty_tutorial():
    add "images/darker.webp"

    add "gui/frame.webp":
        align (0.5,0.5)
        ysize 450

    

    vbox:
        xsize 800
        align (0.5, 0.5)
        spacing 20
        text "The Chicks' Presidency":
            #color "#FFD166"
            size 40

        text "With Chloe and Lindsey competing against each other for one of the most influential positions at San Vallejo, it's up to you to pick sides. Campaign planning unlocks a large amount of opportunities that you don't want to miss out on!\n\nWill you help Chloe, or Lindsey? Or will you even dare to secretly campaign for both at the same time? The potential gratitude of both girls may be huge, but you better not get caught.":
            font "fonts/OpenSans.ttf"
            size 20

        textbutton "Next":
            text_size 40
            action Show("loyalty_tutorial2")
            xalign 0.5

screen loyalty_tutorial2():
    

    add "gui/frame.webp":
        align (0.5,0.5)
        ysize 450

    vbox:
        xsize 800
        align (0.5, 0.5)
        spacing 20
        text "Campaign Planning":
            #color "#FFD166"
            size 40

        text "When planning a campaign, you get to make the big decisions. Both campaigns are divided into different phases and for each phase you will have multiple approaches with a variety of options on how to execute those approaches.\n\nWill you play dirty or stay clean? Will you try to make deals with the Wolves, or the Apes? Will you persuade people with expensive limos and alcohol, or by ruining the other candidate's reputation? The choice is yours. ":
            font "fonts/OpenSans.ttf"
            size 20

        textbutton "Next":
            text_size 40
            action Show("loyalty_tutorial3")
            xalign 0.5

screen loyalty_tutorial3():

    add "gui/frame.webp":
        align (0.5,0.5)
        ysize 450

    vbox:
        xsize 800
        align (0.5, 0.5)
        spacing 20
        text "Popularity":
            #color "#FFD166"
            size 40

        text "Every presidency related action, from executing your big campaign plan, to making a bad joke about one of the candidates, impacts the candidates' popularity, which plays a big role in who's going to be elected.\n\nBut beware, just because you intended to help one candidate, doesn't mean that you'll succeed. Playing too dirty may cause backlash and even the best plans can fail. The stakes have never been higher.":
            font "fonts/OpenSans.ttf"
            size 20

        textbutton "Continue":
            text_size 40
            action [Hide ("loyalty_tutorial"),Hide ("loyalty_tutorial2"),Hide ("loyalty_tutorial3"), Jump ("after_loyalty_tutorial")]
            xalign 0.5