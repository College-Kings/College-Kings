label before_main_menu:
    python:
        msgApp.img = "images/phone/messages/appAssets/messagesIcon.webp"
        statsApp.img = "images/phone/stats/appAssets/statsIcon.webp"
        achApp.img = "images/phone/achievements/appAssets/achievementsIcon.webp"
        kiwiiApp.img = "images/phone/kiwii/appAssets/kiwiiIcon.webp"


        # Create messenger contacts
        try: emily.messenger
        except AttributeError: emily.create_contact("emilyprofilepic.webp", locked=False)
        try: lauren.messenger
        except AttributeError: lauren.create_contact("laurenprofilepic.webp")
        try: julia.messenger
        except AttributeError: julia.create_contact("juliaprofilepic.webp")
        try: ryan.messenger
        except AttributeError: ryan.create_contact("ryanprofilepic.webp")
        try: josh.messenger
        except AttributeError: josh.create_contact("joshprofilepic.webp")
        try: aubrey.messenger
        except AttributeError: aubrey.create_contact("aubreyprofilepic.webp")
        try: chloe.messenger
        except AttributeError: chloe.create_contact("chloeprofilepic.webp")
        try: amber.messenger
        except AttributeError: amber.create_contact("amberprofilepic.webp")
        try: penelope.messenger
        except AttributeError: penelope.create_contact("penelopeprofilepic.webp")
        try: riley.messenger
        except AttributeError: riley.create_contact("rileyprofilepic.webp")
        try: autumn.messenger
        except AttributeError: autumn.create_contact("autumnprofilepic.webp")
        try: imre.messenger
        except AttributeError: imre.create_contact("imreprofilepic.webp")
        try: sebastian.messenger
        except AttributeError: sebastian.create_contact("sebastianprofilepicture.webp")
        try: grayson.messenger
        except AttributeError: grayson.create_contact("graysonprofilepicture.webp")
        try: lindsey.messenger
        except AttributeError: lindsey.create_contact("lindseyprofilepic.webp")
        try: jenny.messenger
        except AttributeError: jenny.create_contact("jennyprofilepicture.webp")
        try: nora.messenger
        except AttributeError: nora.create_contact("noraprofilepicture.webp")


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