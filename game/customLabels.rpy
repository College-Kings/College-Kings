label before_main_menu:
    python:
        msgApp.img = "images/phone/messages/appAssets/messagesIcon.webp"
        statsApp.img = "images/phone/stats/appAssets/statsIcon.webp"
        achApp.img = "images/phone/achievements/appAssets/achievementsIcon.webp"
        kiwiiApp.img = "images/phone/kiwii/appAssets/kiwiiIcon.webp"

        # Set up murder mystery stats
        cl.stats["Competitive"] = True
        cl.stats["Vindictive"] = no

        am.stats["Competitive"] = am.stats["Talkative"] = True
        am.stats["Vindictive"] = ri

        ri.stats["Competitive"] = ri.stats["Talkative"] = True

        li.stats["Competitive"] = li.stats["Talkative"] = True
        li.stats["Vindictive"] = cl

        sa.stats["Vindictive"] = ca

        em.stats["Talkative"] = False

        no.stats["Talkative"] = True
        no.stats["Vindictive"] = [ ch, cl ]

        au.stats["Competitive"] = True

        ry.stats["Vindictive"] = imre

        imre.stats["Competitive"] = False
        imre.stats["Vindictive"] = ry

        ch.stats["Competitive"] = ch.stats["Talkative"] = False

        charli.stats["Competitive"] = True
        charli.stats["Talkative"] = False

        ca.stats["Vindictive"] = sa

        jo.stats["Competitive"] = True

    return


label freeRoamSpokenToo(backgroundImg, returnScreen):
    scene expression backgroundImg
    u "I should probably talk to someone else"
    $ renpy.call_screen(returnScreen)