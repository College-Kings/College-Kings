python early:
    import os

    if renpy.loadable("customCharacters.rpy"):
        os.remove(os.path.join(config.basedir, "game", "customCharacters.rpy"))
    if renpy.loadable("customCharacters.rpyc"):
        os.remove(os.path.join(config.basedir, "game", "customCharacters.rpyc"))

    if renpy.loadable("bugTesting/bugTesting_Overwrite.rpy"):
        os.remove(os.path.join(config.basedir, "game", "bugTesting", "bugTesting_Overwrite.rpy"))
    if renpy.loadable("bugTesting/bugTesting_Overwrite.rpyc"):
        os.remove(os.path.join(config.basedir, "game", "bugTesting", "bugTesting_Overwrite.rpyc"))

    if renpy.loadable("bugTesting/bugTesting_typoNotes.rpy"):
        os.remove(os.path.join(config.basedir, "game", "bugTesting", "bugTesting_typoNotes.rpy"))
    if renpy.loadable("bugTesting/bugTesting_typoNotes.rpyc"):
        os.remove(os.path.join(config.basedir, "game", "bugTesting", "bugTesting_typoNotes.rpyc"))

    if renpy.loadable("phone/phonescript.rpy"):
        os.remove(os.path.join(config.basedir, "game", "phone", "phonescript.rpy"))
    if renpy.loadable("phone/phonescript.rpyc"):
        os.remove(os.path.join(config.basedir, "game", "phone", "phonescript.rpyc"))
    
    if renpy.loadable("phone/phoneStyle.rpy"):
        os.remove(os.path.join(config.basedir, "game", "phone", "phoneStyle.rpy"))
    if renpy.loadable("phone/phoneStyle.rpyc"):
        os.remove(os.path.join(config.basedir, "game", "phone", "phoneStyle.rpyc"))
    
    if renpy.loadable("functions.rpy"):
        os.remove(os.path.join(config.basedir, "game", "functions.rpy"))
    if renpy.loadable("functions.rpyc"):
        os.remove(os.path.join(config.basedir, "game", "functions.rpyc"))

    if renpy.loadable("scriptv06.rpy"):
        os.remove(os.path.join(config.basedir, "game", "scriptv06.rpy"))
    if renpy.loadable("scriptv06.rpyc"):
        os.remove(os.path.join(config.basedir, "game", "scriptv06.rpyc"))

    if renpy.loadable("scriptv07.rpy"):
        os.remove(os.path.join(config.basedir, "game", "scriptv07.rpy"))
    if renpy.loadable("scriptv07.rpyc"):
        os.remove(os.path.join(config.basedir, "game", "scriptv07.rpyc"))

    if renpy.loadable("screen.rpy"):
        os.remove(os.path.join(config.basedir, "game", "screen.rpy"))
    if renpy.loadable("screen.rpyc"):
        os.remove(os.path.join(config.basedir, "game", "screen.rpyc"))

    if os.path.exists(os.path.join(config.basedir, "game", "v8")):
        try:
            for file in os.listdir(os.path.join(config.basedir, "game", "v0.8")):
                os.remove(file)
            os.rmdir(MYPATH)
        except Exception: pass

    if os.path.exists(os.path.join(config.basedir, "game", "v9")):
        try:
            for file in os.listdir(os.path.join(config.basedir, "game", "v0.9")):
                os.remove(file)
            os.rmdir(MYPATH)
        except Exception: pass

    try: v7_msgReply8
    except NameError:
        def v7_msgReply8():
            pass

    try: v7_msgReply9
    except NameError:
        def v7_msgReply9():
            pass

    try: v7_msgReply10
    except NameError:
        def v7_msgReply10():
            pass

    class CheatItem:
        pass


init 100 python:
    class CustomCharacter(NonPlayableCharacter):
        pass

    class MainCharacter(PlayableCharacter):
        pass


label after_load:
    python:
        # Disable skip transitions
        preferences.transitions = 2

        # Applications
        for app in applications:
            try: app.img = app.image
            except AttributeError: pass

            try: app.homeScreen = app.screen
            except AttributeError: pass

        msgApp.img = "images/phone/messages/appAssets/messagesIcon.webp"
        statsApp.img = "images/phone/stats/appAssets/statsIcon.webp"
        achApp.img = "images/phone/achievements/appAssets/achievementsIcon.webp"
        kiwiiApp.img = "images/phone/kiwii/appAssets/kiwiiIcon.webp"

        renpy.music.stop(channel=u'music') ### temporary emergency break

        # Playable Character
        mc.profile_picture = profile_pictures[0]


        # NonPlayable Character
        try: chloe
        except NameError: chloe = NonPlayableCharacter("Chloe", "chloe.webp")
        try: amber
        except NameError: amber = NonPlayableCharacter("Amber", "amber.webp")
        try: penelope
        except NameError: penelope = NonPlayableCharacter("Penelope", "penelope.webp")
        try: riley
        except NameError: riley = NonPlayableCharacter("Riley", "riley.webp")
        try: lindsey
        except NameError: lindsey = NonPlayableCharacter("Lindsey", "lindsey.webp")
        try: lauren
        except NameError: lauren = NonPlayableCharacter("Lauren", "lauren.webp")
        try: emily
        except NameError: emily = NonPlayableCharacter("Emily", "emily.webp")
        try: ms_rose
        except NameError: ms_rose = NonPlayableCharacter("Ms Rose", "ms_rose.webp")
        try: nora
        except NameError: nora = NonPlayableCharacter("Nora", "nora.webp")
        try: aubrey
        except NameError: aubrey = NonPlayableCharacter("Aubrey", "aubrey.webp")
        try: ryan
        except NameError: ryan = NonPlayableCharacter("Ryan", "ryan.webp")
        try: imre
        except NameError: imre = NonPlayableCharacter("Imre", "imre.webp")
        try: chris
        except NameError: chris = NonPlayableCharacter("Chris", "chris.webp")
        try: charli
        except NameError: charli = NonPlayableCharacter("Charli", "charli.webp")
        try: cameron
        except NameError: cameron = NonPlayableCharacter("Cameron", "cameron.webp")
        try: josh
        except NameError: josh = NonPlayableCharacter("Josh", "josh.webp")
        try: julia
        except NameError: julia = NonPlayableCharacter("Julia", "julia.webp")
        try: evelyn
        except NameError: evelyn = NonPlayableCharacter("Evelyn", "evelyn.webp")
        try: autumn
        except NameError: autumn = NonPlayableCharacter("Autumn", "autumn.webp")
        try: sebastian
        except NameError: sebastian = NonPlayableCharacter("Sebastian", "sebastian.webp")
        try: grayson
        except NameError: grayson = NonPlayableCharacter("Grayson", "grayson.webp")
        try: jenny
        except NameError: jenny = NonPlayableCharacter("Jenny", "jenny.webp")
        try: samantha
        except NameError: samantha = NonPlayableCharacter("Samantha", "samantha.webp")

        if isinstance(chloe, CustomCharacter):
            char_points = chloe.points
            char_stats = chloe.stats
            chloe = NonPlayableCharacter("Chloe", "chloe.webp")
            chloe.points = char_points
            chloe.stats = char_stats
        if isinstance(amber, CustomCharacter):
            char_points = amber.points
            char_stats = amber.stats
            amber = NonPlayableCharacter("Amber", "amber.webp")
            amber.points = char_points
            amber.stats = char_stats
        if isinstance(penelope, CustomCharacter):
            char_points = penelope.points
            char_stats = penelope.stats
            penelope = NonPlayableCharacter("Penelope", "penelope.webp")
            penelope.points = char_points
            penelope.stats = char_stats
        if isinstance(riley, CustomCharacter):
            char_points = riley.points
            char_stats = riley.stats
            riley = NonPlayableCharacter("Riley", "riley.webp")
            riley.points = char_points
            riley.stats = char_stats
        if isinstance(lindsey, CustomCharacter):
            char_points = lindsey.points
            char_stats = lindsey.stats
            lindsey = NonPlayableCharacter("Lindsey", "lindsey.webp")
            lindsey.points = char_points
            lindsey.stats = char_stats
        if isinstance(lauren, CustomCharacter):
            char_points = lauren.points
            char_stats = lauren.stats
            lauren = NonPlayableCharacter("Lauren", "lauren.webp")
            lauren.points = char_points
            lauren.stats = char_stats
        if isinstance(emily, CustomCharacter):
            char_points = emily.points
            char_stats = emily.stats
            emily = NonPlayableCharacter("Emily", "emily.webp")
            emily.points = char_points
            emily.stats = char_stats
        if isinstance(ms_rose, CustomCharacter):
            char_points = ms_rose.points
            char_stats = ms_rose.stats
            ms_rose = NonPlayableCharacter("Ms Rose", "ms_rose.webp")
            ms_rose.points = char_points
            ms_rose.stats = char_stats
        if isinstance(nora, CustomCharacter):
            char_points = nora.points
            char_stats = nora.stats
            nora = NonPlayableCharacter("Ms Rose", "ms_rose.webp")
            nora.points = char_points
            nora.stats = char_stats
        if isinstance(aubrey, CustomCharacter):
            char_points = aubrey.points
            char_stats = aubrey.stats
            aubrey = NonPlayableCharacter("Aubrey", "aubrey.webp")
            aubrey.points = char_points
            aubrey.stats = char_stats
        if isinstance(ryan, CustomCharacter):
            char_points = ryan.points
            char_stats = ryan.stats
            ryan = NonPlayableCharacter("Ryan", "ryan.webp")
            ryan.points = char_points
            ryan.stats = char_stats
        if isinstance(imre, CustomCharacter):
            char_points = imre.points
            char_stats = imre.stats
            imre = NonPlayableCharacter("Imre", "imre.webp")
            imre.points = char_points
            imre.stats = char_stats
        if isinstance(chris, CustomCharacter):
            char_points = chris.points
            char_stats = chris.stats
            chris = NonPlayableCharacter("Chris", "chris.webp")
            chris.points = char_points
            chris.stats = char_stats
        if isinstance(charli, CustomCharacter):
            char_points = charli.points
            char_stats = charli.stats
            charli = NonPlayableCharacter("Charli", "charlie.webp")
            charli.points = char_points
            charli.stats = char_stats
        if isinstance(cameron, CustomCharacter):
            char_points = cameron.points
            char_stats = cameron.stats
            cameron = NonPlayableCharacter("Cameron", "cameron.webp")
            cameron.points = char_points
            cameron.stats = char_stats
        if isinstance(josh, CustomCharacter):
            char_points = josh.points
            char_stats = josh.stats
            josh = NonPlayableCharacter("Josh", "josh.webp")
            josh.points = char_points
            josh.stats = char_stats
        if isinstance(julia, CustomCharacter):
            char_points = julia.points
            char_stats = julia.stats
            julia = NonPlayableCharacter("Julia", "julia.webp")
            julia.points = char_points
            julia.stats = char_stats
        if isinstance(evelyn, CustomCharacter):
            char_points = evelyn.points
            char_stats = evelyn.stats
            evelyn = NonPlayableCharacter("Evelyn", "evelyn.webp")
            evelyn.points = char_points
            evelyn.stats = char_stats
        if isinstance(autumn, CustomCharacter):
            char_points = autumn.points
            char_stats = autumn.stats
            autumn = NonPlayableCharacter("Autumn", "autumn.webp")
            autumn.points = char_points
            autumn.stats = char_stats
        if isinstance(sebastian, CustomCharacter):
            char_points = sebastian.points
            char_stats = sebastian.stats
            sebastian = NonPlayableCharacter("Sebastian", "sebastian.webp")
            sebastian.points = char_points
            sebastian.stats = char_stats
        if isinstance(grayson, CustomCharacter):
            char_points = grayson.points
            char_stats = grayson.stats
            grayson = NonPlayableCharacter("Grayson", "grayson.webp")
            grayson.points = char_points
            grayson.stats = char_stats
        if isinstance(jenny, CustomCharacter):
            char_points = jenny.points
            char_stats = jenny.stats
            jenny = NonPlayableCharacter("Jenny", "jenny.webp")
            jenny.points = char_points
            jenny.stats = char_stats


        # Kiwii Users
        kiwiiUsers = kiwii_users()

        # Kiwii Posts
        try: v11s1_kiwiiPost.img = "images/phone/kiwii/posts/v11/v11_autumn_kiwii.webp"
        except NameError: pass
        try: v11s19_kiwiiPost1.img = "images/phone/kiwii/posts/v11/v11_chloemcselfie.webp"
        except NameError: pass
        try: v11s19_kiwiiPost2.img = "images/phone/kiwii/posts/v11/v11_chloemcselfie.webp"
        except NameError: pass
        try: v11s19_kiwiiPost3.img = "images/phone/kiwii/posts/v11/v11_rileymcselfie.webp"
        except NameError: pass
        try: v11s24_kiwiiPost1.img = "images/phone/kiwii/posts/v11/v11_caleb.webp"
        except NameError: pass
        try: v11s24_kiwiiPost2.img = "images/phone/kiwii/posts/v11/v11_imrebunny.webp"
        except NameError: pass
        try: v11s38_kiwiiPost1.img = "images/phone/kiwii/posts/v11/v11s38_amber_kiwii.webp"
        except NameError: pass
        try: v11s9a_kiwiiPost1.img = "images/phone/kiwii/posts/v11/sebnaked.webp"
        except NameError: pass
        try: v11s9a_kiwiiPost2.img = "images/phone/kiwii/posts/v11/sebnaked.webp"
        except NameError: pass
        try: v13s49_kiwiiPost1.img = "images/phone/kiwii/posts/v13/aubrey_beach.webp"
        except NameError: pass

        for kiwiiPost in kiwiiPosts:
            try: kiwiiPost.img = kiwiiPost.image
            except AttributeError: pass

            kiwiiPost.img = os.path.splitext(kiwiiPost.img)[0] + ".webp"

            for i in range(7, 10):
                if renpy.loadable("images/phone/kiwii/posts/v{}/{}".format(i, kiwiiPost.img.split("/")[-1])):
                    kiwiiPost.img = "images/phone/kiwii/posts/v{}/{}".format(i, kiwiiPost.img.split("/")[-1])
                    break
                    
            try: kiwiiPost.message = kiwiiPost.caption
            except AttributeError: pass

            try:
                if kiwiiPost.message[0] == "[" and kiwiiPost.message[1] != "[":
                    kiwiiPost.message = "[" + kiwiiPost.message
            except IndexError:
                pass

            try: kiwiiPost.sentComments = kiwiiPost.comments
            except AttributeError: pass

            try: kiwiiPost.profile_picture = kiwiiPost.profilePicture
            except AttributeError: pass

            # Kiwii Comments
            for comment in kiwiiPost.sentComments:
                try: comment.message = comment.text
                except AttributeError: pass

                try: comment.profile_picture = comment.profilePicture
                except AttributeError: pass
                
            # Old Kiwii Replies
            try:
                for reply in kiwiiPost.replies:
                    kiwiiPost.replies.remove(reply)
                    kiwiiPost.addReply(reply.reply, numberLikes=reply.numberLikes, mentions=reply.mentions)
            except AttributeError: pass

            # New Kiwii Replies
            try:
                for reply in kiwiiPost.sentComments[-1].replies:
                    reply.disabled = False
            except Exception: pass

            try:
                for pendingComment in kiwiiPost.pendingComments:
                    for reply in pendingComment.replies:
                        reply.disabled = False
            except AttributeError: pass


        # Contacts
        for contact in contacts:
            try: contact.pendingMessages
            except AttributeError: contact.pendingMessages = []

            try: contact.sentMessages
            except AttributeError: contact.sentMessages = []

            contact.profile_picture = "images/nonplayable_characters/profile_pictures/{}.webp".format(contact.name.lower())

            try: contact.profilePicture = "images/nonplayable_characters/profile_pictures/chloe.webp"
            except: pass

            # Messages
            try:
                for message in contact.messages:
                    try: message.image = os.path.splitext(message.image)[0] + ".webp"
                    except AttributeError: pass

                    try: message.image = message.image.replace("v08", "v8")
                    except AttributeError: pass
                    try: message.image = message.image.replace("v09", "v9")
                    except AttributeError: pass

                    try: message.message = message.msg
                    except AttributeError: pass

                    try: message.replies
                    except AttributeError: message.replies = []

                    contact.sentMessages.append(message)

                    # Replies
                    for reply in message.replies:
                        try: reply.func
                        except AttributeError: reply.func = None

                        try: reply.disabled
                        except AttributeError: reply.disabled = False
            except AttributeError: pass



        # Transfer Contact object to NonPlayableCharacter class
        try:
            emily.messenger = contact_Emily
            del contact_Emily
        except NameError: pass
        try:
            lauren.messenger = contact_Lauren
            del contact_Lauren
        except NameError: pass
        try:
            julia.messenger = contact_Julia
            del contact_Julia
        except NameError: pass
        try:
            ryan.messenger = contact_Ryan
            del contact_Ryan
        except NameError: pass
        try:
            josh.messenger = contact_Josh
            del contact_Josh
        except NameError: pass
        try:
            aubrey.messenger = contact_Aubrey
            del contact_Aubrey
        except NameError: pass
        try:
            chloe.messenger = contact_Chloe
            del contact_Chloe
        except NameError: pass
        try:
            amber.messenger = contact_Amber
            del contact_Amber
        except NameError: pass
        try:
            penelope.messenger = contact_Penelope
            del contact_Penelope
        except NameError: pass
        try:
            riley.messenger = contact_Riley
            del contact_Riley
        except NameError: pass
        try:
            autumn.messenger = contact_Autumn
            del contact_Autumn
        except NameError: pass
        try:
            imre.messenger = contact_Imre
            del contact_Imre
        except NameError: pass
        try:
            sebastian.messenger = contact_Sebastian
            del contact_Sebastian
        except NameError: pass
        try:
            grayson.messenger = contact_Grayson
            del contact_Grayson
        except NameError: pass
        try:
            lindsey.messenger = contact_Lindsey
            del contact_Lindsey
        except NameError: pass
        try:
            jenny.messenger = contact_Jenny
            del contact_Jenny
        except NameError: pass
        try:
            nora.messenger = contact_Nora
            del contact_Nora
        except NameError: pass


        # Simplr Contacts
        try:
            beth.simplr = simplr_Beth
            del simplr_Beth
        except NameError: pass
        try:
            iris.simplr = simplr_Iris
            del simplr_Iris
        except NameError: pass
        try:
            samantha.simplr = simplr_Samantha
            del simplr_Samantha
        except NameError: pass
        try:
            emmy.simplr = simplr_Emmy
            del simplr_Emmy
        except NameError: pass

        for contact in simplr_contacts + simplr_pendingContacts:
            contact.profile_picture = "images/nonplayable_characters/{0}/{0}_profile_picture.webp".format(contact.name.lower())
            
            contact.large_profile_pictures = ["images/nonplayable_characters/{}/large_profile_pictures/1.webp".format(contact.name.lower())]
            for (dirpath, dirname, filenames) in os.walk(os.path.join(contacts_file_path, contact.name.lower(), "large_profile_pictures")):
                contact.large_profile_pictures = ["images/nonplayable_characters/{}/large_profile_pictures/{}".format(contact.name.lower(), filename) for filename in filenames]

        
        # Items
        honey.insensitive_image = "images/v13/Scene35/sex_shop/honey_insensitive.webp"
        butt_plug.insensitive_image = "images/v13/Scene35/sex_shop/butt_plug_insensitive.webp"
        spankers.insensitive_image = "images/v13/Scene35/sex_shop/spankers_insensitive.webp"
        cuffs.insensitive_image = "images/v13/Scene35/sex_shop/cuffs_insensitive.webp"
        feather.insensitive_image = "images/v13/Scene35/sex_shop/feather_insensitive.webp"

        # Variables
        try:
            if chlorers: chloers = True
        except NameError: pass
        try: kiwiiPost1
        except NameError: kiwii_firstTime = False

        try:
            if v14s51_closet: freeroam12.add("closet")
        except NameError: pass
        try:
            if v14s51_purse: freeroam12.add("purse")
        except NameError: pass
        try:
            if v14s51_take_cash_large: freeroam12stolen.add("cash_large")
        except NameError: pass
        try:
            if v14s51_take_cash_small: freeroam12stolen.add("cash_small")
        except NameError: pass
        try:
            if v14s51_take_diary: freeroam12stolen.add("diary")
        except NameError: pass

        # v12 Renpy Fixes:
        chloe.name = "Chloe"
        amber.name = "Amber"
        penelope.name = "Penelope"
        riley.name = "Riley"
        lindsey.name = "Lindsey"
        lauren.name = "Lauren"
        samantha.name = "Samantha"
        emily.name = "Emily"
        ms_rose.name = "Ms_Rose"
        nora.name = "Nora"
        aubrey.name = "Aubrey"
        ryan.name = "Ryan"
        imre.name = "Imre"
        chris.name = "Chris"
        charli.name = "Charli"
        cameron.name = "Cameron"
        josh.name = "Josh"

        chloe.profile_picture = "images/nonplayable_characters/profile_pictures/chloe.webp"
        amber.profile_picture = "images/nonplayable_characters/profile_pictures/amber.webp"
        penelope.profile_picture = "images/nonplayable_characters/profile_pictures/penelope.webp"
        riley.profile_picture = "images/nonplayable_characters/profile_pictures/riley.webp"
        lindsey.profile_picture = "images/nonplayable_characters/profile_pictures/lindsey.webp"
        lauren.profile_picture = "images/nonplayable_characters/profile_pictures/lauren.webp"
        samantha.profile_picture = "images/nonplayable_characters/profile_pictures/samantha.webp"
        emily.profile_picture = "images/nonplayable_characters/profile_pictures/emily.webp"
        ms_rose.profile_picture = "images/nonplayable_characters/profile_pictures/ms_rose.webp"
        nora.profile_picture = "images/nonplayable_characters/profile_pictures/nora.webp"
        aubrey.profile_picture = "images/nonplayable_characters/profile_pictures/aubrey.webp"
        ryan.profile_picture = "images/nonplayable_characters/profile_pictures/ryan.webp"
        imre.profile_picture = "images/nonplayable_characters/profile_pictures/imre.webp"
        chris.profile_picture = "images/nonplayable_characters/profile_pictures/chris.webp"
        charli.profile_picture = "images/nonplayable_characters/profile_pictures/charli.webp"
        cameron.profile_picture = "images/nonplayable_characters/profile_pictures/cameron.webp"
        josh.profile_picture = "images/nonplayable_characters/profile_pictures/josh.webp"

        try: v7_emily_bowling
        except NameError: v7_emily_bowling = False
        try: v8_dodged_pipe
        except NameError: v8_dodged_pipe = False
        try: v11_samantha_spa
        except NameError: v11_samantha_spa = False
        try: v11_underground_rose
        except NameError: v11_underground_rose = False
        try: v12_told_chloe
        except NameError: v12_told_chloe = False
        try: v12_fight_win
        except NameError: v12_fight_win = False
        try: v12_chase_robber
        except NameError: v12_chase_robber = False
        try: v12s7_seenList
        except NameError: v12s7_seenList = []
        try: v12s7_endtalkList
        except NameError: v12s7_endtalkList = []
        try: v12s7_killList
        except NameError: v12s7_killList = set()
        try: v12_msrose_sex
        except NameError: v12_msrose_sex = False
        try: v11_lindsey_run
        except NameError: v11_lindsey_run = False
        try: v12_help_chris
        except NameError: v12_help_chris = 0
        try: v12s7_riley_moved
        except NameError: v12s7_riley_moved = False
        try: v12s7_lindsey_moved
        except NameError: v12s7_lindsey_moved = False
        try: v12s7_aubrey_moved
        except NameError: v12s7_aubrey_moved = False
        try: v12_lindsey_sex
        except NameError: v12_lindsey_sex = False
        try: v12_lauren_sex
        except NameError: v12_lauren_sex = False
        try: v12_lauren_points
        except NameError: v12_lauren_points = 0
        try: v12s32_Aubrey_Boost
        except NameError: v12s32_Aubrey_Boost = False
        try: v12_murder_count
        except NameError: v12_murder_count = 0
        try: joshmadfr
        except NameError: joshmadfr = False
        try: v12s7_victims
        except NameError: v12s7_victims = 12
        try: v12s23a_sam
        except NameError: v12s23a_sam = False
        try: v12_nora_sex
        except NameError: v12_nora_sex = False
        try: v12_nora_points
        except NameError: v12_nora_points = 0
        try: v12s24_emmymatch
        except NameError: v12s24_emmymatch = False
        try: v12_sauna_sneak1
        except NameError: v12_sauna_sneak1 = False
        try: v12_girl
        except NameError: v12_girl = "na"

        #v11 variables
        try: v11_pen_goes_europe
        except NameError: v11_pen_goes_europe = False
        try: v11s1_courtpoints
        except NameError: v11s1_courtpoints = 0
        try: v11_invite_sam_europe
        except NameError: v11_invite_sam_europe = False
        try: v11_josh_nightclub
        except NameError: v11_josh_nightclub = False
        try: candyLike
        except NameError: candyLike = 0
        try: v11_fucked_candy
        except NameError: v11_fucked_candy = False
        try: v11_aubrey_blue_outfit
        except NameError: v11_aubrey_blue_outfit = False
        try: v11_tease_amber
        except NameError: v11_tease_amber = 0
        try: v11_manhunt_winner
        except NameError: v11_manhunt_winner = "Ryan"
        try: v11_aubrey_sex
        except NameError: v11_aubrey_sex = False
        try: v11_riley_roomate
        except NameError: v11_riley_roomate = False
        try: v11s25_beer
        except NameError: v11s25_beer = True
        try: msrosers
        except NameError: msrosers = False
        try: v11_solo_question
        except NameError: v11_solo_question = False
        try: v11_kiss_nora
        except NameError: v11_kiss_nora = False
        try: v11_told_aubrey
        except NameError: v11_told_aubrey = False
        try: chloegf
        except NameError: chloegf = False
        try: v11_lindsey_slogan
        except NameError: v11_lindsey_slogan = 0 
        try: v11_linds_inv_imre
        except NameError: v11_linds_inv_imre = False 
        try: v11_sit_with_lauren
        except NameError: v11_sit_with_lauren = True
        try: v11_msrose_scene
        except NameError: v11_msrose_scene = False
        try: v11_overtake_points
        except NameError: v11_overtake_points = 0
        try: v11_hp_points
        except NameError: v11_hp_points = 0
        try: political_strategist
        except NameError: political_strategist = False
        try: emily_europe
        except NameError: emily_europe = False
        try: v11_check_on_nora
        except NameError: v11_check_on_nora = False

        # v13 Errors
        try: v13_penelope_concert
        except NameError: v13_penelope_concert = False
        try: v13_aubrey_concert
        except NameError: v13_aubrey_concert = False
        try: chloeSus
        except NameError: chloeSus = 0
        try: v13_cuddle_lauren
        except NameError: v13_cuddle_lauren = False
        try: v13_cuddle_lauren_text
        except NameError: v13_cuddle_lauren_text = False
        try: v13s16_lauren_points
        except NameError: v13s16_lauren_points = 0
        try: v13_smoke_weed
        except NameError: v13_smoke_weed = False
        try: v13_lauren_smoke
        except NameError: v13_lauren_smoke = False
        try: cameronBro
        except NameError: cameronBro = False
        try: v13_charli_exposed
        except NameError: v13_charli_exposed = False
        try: v13_invite_samantha
        except NameError: v13_invite_samantha = False
        try: v13_after_party
        except NameError: v13_after_party = False
        try: v13s48_get_aubrey_chocolate
        except NameError: v13s48_get_aubrey_chocolate = False
        try: v13s48_ryan_double_date
        except NameError: v13s48_ryan_double_date = False
        try: v13s48_canoeing_as_date
        except NameError: v13s48_canoeing_as_date = False
        try: v13_help_chloe
        except NameError: v13_help_chloe = False
        try: emmyrs
        except NameError: emmyrs = False
        try: kourtneyrs
        except NameError: kourtneyrs = False
        try: aryssars
        except NameError: aryssars = False
        try: v13_emmy_points
        except NameError: v13_emmy_points = 0
        try: v13_imre_disloyal
        except NameError: v13_imre_disloyal = False
        try: v13_perfume
        except NameError: v13_perfume = False
        try: v13_hugged_aubrey
        except NameError: v13_hugged_aubrey = False
        try: v13s9_go_to_concert
        except NameError: v13s9_go_to_concert = False
        try: v13s41_lindsey_points
        except NameError: v13s41_lindsey_points = 0
        try: v13_emmysex
        except NameError: v13_emmysex = False
        try: v13_emilysex
        except NameError: v13_emilysex = False
        try: v13s20_bleach_suitcase
        except NameError: v13s20_bleach_suitcase = False
        try: laurenrs_v11aubrey
        except NameError: laurenrs_v11aubrey = False
        try: v13s40fromgame
        except NameError: v13s40fromgame = False
        try: v13_aubrey_vote
        except NameError: v13_aubrey_vote = "na"
        try: v14_ryan_satin
        except NameError: v14_ryan_satin = False


    show no_hard_feelings at achievementShow
    $ achievementAtList = renpy.get_at_list("no_hard_feelings")
    hide no_hard_feelings

    show screen phoneIcon
    hide screen getaccess

    if config.developer:
        show screen bugTesting_Overlay

    return