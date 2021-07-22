label before_main_menu:
    python:
        msgApp.img = "images/phone/messages/appAssets/messagesIcon.webp"
        statsApp.img = "images/phone/stats/appAssets/statsIcon.webp"
        achApp.img = "images/phone/achievements/appAssets/achievementsIcon.webp"
        kiwiiApp.img = "images/phone/kiwii/appAssets/kiwiiIcon.webp"

        # Set up murder mystery stats
        Chloe.stats["Competitive"] = True
        Chloe.stats["Vindictive"] = Nora

        Amber.stats["Competitive"] = Amber.stats["Talkative"] = True
        Amber.stats["Vindictive"] = Riley

        Riley.stats["Competitive"] = Riley.stats["Talkative"] = True

        Lindsey.stats["Competitive"] = Lindsey.stats["Talkative"] = True
        Lindsey.stats["Vindictive"] = Chloe

        Samantha.stats["Vindictive"] = Cameron

        Emily.stats["Talkative"] = False

        Nora.stats["Talkative"] = True
        Nora.stats["Vindictive"] = [ Chris, Chloe ]

        Aubrey.stats["Competitive"] = True

        Ryan.stats["Vindictive"] = Imre

        Imre.stats["Competitive"] = False
        Imre.stats["Vindictive"] = Ryan

        Chris.stats["Competitive"] = Chris.stats["Talkative"] = False

        Charli.stats["Competitive"] = True
        Charli.stats["Talkative"] = False

        Cameron.stats["Vindictive"] = Samantha

        Josh.stats["Competitive"] = True

    return


label freeRoamSpokenToo(backgroundImg, returnScreen):
    scene expression backgroundImg
    u "I should probably talk to someone else"
    $ renpy.call_screen(returnScreen)