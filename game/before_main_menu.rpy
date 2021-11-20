label before_main_menu:
    python:
        msgApp.img = "images/phone/messages/appAssets/messagesIcon.webp"
        statsApp.img = "images/phone/stats/appAssets/statsIcon.webp"
        achApp.img = "images/phone/achievements/appAssets/achievementsIcon.webp"
        kiwiiApp.img = "images/phone/kiwii/appAssets/kiwiiIcon.webp"


        # Create messenger contacts
        try: emily.messenger
        except AttributeError: emily.create_contact(locked=False)
        try: lauren.messenger
        except AttributeError: lauren.create_contact()
        try: julia.messenger
        except AttributeError: julia.create_contact()
        try: ryan.messenger
        except AttributeError: ryan.create_contact()
        try: josh.messenger
        except AttributeError: josh.create_contact()
        try: aubrey.messenger
        except AttributeError: aubrey.create_contact()
        try: chloe.messenger
        except AttributeError: chloe.create_contact()
        try: amber.messenger
        except AttributeError: amber.create_contact()
        try: penelope.messenger
        except AttributeError: penelope.create_contact()
        try: riley.messenger
        except AttributeError: riley.create_contact()
        try: autumn.messenger
        except AttributeError: autumn.create_contact()
        try: imre.messenger
        except AttributeError: imre.create_contact()
        try: sebastian.messenger
        except AttributeError: sebastian.create_contact()
        try: grayson.messenger
        except AttributeError: grayson.create_contact()
        try: lindsey.messenger
        except AttributeError: lindsey.create_contact()
        try: jenny.messenger
        except AttributeError: jenny.create_contact()
        try: nora.messenger
        except AttributeError: nora.create_contact()


        # Create simplr contacts
        try: beth.simplr
        except AttributeError: beth.create_simplr()
        try: iris.simplr
        except AttributeError: iris.create_simplr()
        try: samantha.simplr
        except AttributeError: samantha.create_simplr()
        try: emmy.simplr
        except AttributeError: emmy.create_simplr()


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

        josh.stats["Competitive"] = True

    return