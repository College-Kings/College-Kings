label before_main_menu:
    python:
        msgApp.img = "images/phone/messages/appAssets/messagesIcon.webp"
        statsApp.img = "images/phone/stats/appAssets/statsIcon.webp"
        achApp.img = "images/phone/achievements/appAssets/achievementsIcon.webp"
        kiwiiApp.img = "images/phone/kiwii/appAssets/kiwiiIcon.webp"

        # Set up murder mystery stats
        chloe.stats["Competitive"] = True
        chloe.stats["Vindictive"] = [nora]

        amber.stats["Competitive"] = amber.stats["Talkative"] = True
        amber.stats["Vindictive"] = [riley]

        riley.stats["Competitive"] = riley.stats["Talkative"] = True

        lindsey.stats["Competitive"] = lindsey.stats["Talkative"] = True
        lindsey.stats["Vindictive"] = [chloe]

        emily.stats["Talkative"] = False

        nora.stats["Talkative"] = True
        nora.stats["Vindictive"] = [chris, chloe]

        aubrey.stats["Competitive"] = True

        ryan.stats["Vindictive"] = [imre]

        imre.stats["Competitive"] = False
        imre.stats["Vindictive"] = [ryan]

        chris.stats["Competitive"] = chris.stats["Talkative"] = False

        charli.stats["Competitive"] = True
        charli.stats["Talkative"] = False

        cameron.stats["Vindictive"] = [samantha]

        josh.stats["Competitive"] = True

    return


label freeRoamSpokenToo(backgroundImg, returnScreen):
    scene expression backgroundImg
    u "I should probably talk to someone else"
    scene black
    $ renpy.call_screen(returnScreen)