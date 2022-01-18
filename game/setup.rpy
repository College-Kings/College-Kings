label setup:
    call nonplayable_characters_setup from _call_nonplayable_characters_setup

    python:
        # Phone Setup
        phone.applications = []
        phone.applications.append(messenger)
        phone.applications.append(stats_app)
        phone.applications.append(achievement_app)
        phone.applications.append(kiwii)
        phone.applications.append(simplr_app)


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

    # Renpy Script
    # Get Animation/Transform List
    show no_hard_feelings at achievementShow
    $ achievementAtList = renpy.get_at_list("no_hard_feelings")
    hide no_hard_feelings

    jump expression start_location