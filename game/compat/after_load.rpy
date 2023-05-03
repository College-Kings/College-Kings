python early:
    old_files = (
        "bugTesting/bugTesting_Overwrite.rpy",
        "bugTesting/bugTesting_typoNotes.rpy",
        "bugTesting/bugTesting_cheats.rpy",
        "bugTesting/styles.rpy",
        "fights/fight_labels.rpy",
        "main_menu/path_builder/path_builder_setup.rpy",
        "phone/applications.rpy",
        "phone/phonescript.rpy",
        "phone/phone_msg.rpy",
        "phone/phone_script.rpy",
        "phone/phoneStyle.rpy",
        "sceneGallery/sceneGallery.rpy",
        "v14/chicks_presidency_race/planning_board.rpy",
        "before_main_menu.rpy",
        "customCharacters.rpy",
        "customLabels.rpy",
        "customATL.rpy",
        "customScreens.rpy",
        "functions.rpy",
        "path_builder.rpy",
        "scriptv06.rpy",
        "scriptv07.rpy",
        "screen.rpy",
        "sex_overlay.rpy",
        "after_load.rpy",
        "items.rpy",
        "kct.rpy",
        "setup.rpy",
    )

    restart_game = False # NEVER CHANGE

    for rpy_file in old_files:
        rpyc_file = rpy_file + "c"

        rpy_file_path = os.path.join(config.basedir, "game", *rpy_file.split("/"))
        rpyc_file_path = os.path.join(config.basedir, "game", *rpyc_file.split("/"))

        if renpy.loadable(rpy_file):
            restart_game = True
            os.remove(rpy_file_path)
        if renpy.loadable(rpyc_file):
            restart_game = True
            os.remove(rpyc_file_path)

    if restart_game:
        try:
            import subprocess
            subprocess.call([os.path.join(config.basedir, "CollegeKings.exe")])
            renpy.quit()
        except OSError:
            raise Exception("Deleting old files please RESTART GAME.")
            

label after_load:
    python:
        # Disable skip transitions
        preferences.transitions = 2

        ## PLAYABLE CHARACTERS
        if isinstance(mc, FightCharacter) or isinstance(mc, MainCharacter):
            mc = PlayableCharacter()

        try: mc.username
        except AttributeError: mc.username = name

        try: mc.relationships
        except AttributeError: mc.relationships = {}


#region NonPlayable Character
        try: chloe
        except NameError: chloe = NonPlayableCharacter("Chloe", "Chloe101")
        try: amber
        except NameError: amber = NonPlayableCharacter("Amber", "Amber_xx")
        try: penelope
        except NameError: penelope = NonPlayableCharacter("Penelope", "Penelopeeps")
        try: riley
        except NameError: riley = NonPlayableCharacter("Riley", "RileyReads")
        try: lindsey
        except NameError: lindsey = NonPlayableCharacter("Lindsey", "LindsLou")
        try: lauren
        except NameError: lauren = NonPlayableCharacter("Lauren", "LoLoLauren")
        try: emily
        except NameError: emily = NonPlayableCharacter("Emily", "emilyyyy")
        try: ms_rose
        except NameError: ms_rose = NonPlayableCharacter("Ms Rose")
        try: nora
        except NameError: nora = NonPlayableCharacter("Nora", "Nora_12")
        try: aubrey
        except NameError: aubrey = NonPlayableCharacter("Aubrey", "Aubs123")
        try: ryan
        except NameError: ryan = NonPlayableCharacter("Ryan", "Ryanator")
        try: imre
        except NameError: imre = NonPlayableCharacter("Imre", "BadBoyImre")
        try: chris
        except NameError: chris = NonPlayableCharacter("Chris", "Chriscuit")
        try: charli
        except NameError: charli = NonPlayableCharacter("Charli", "CharliAndTheCockFactory")
        try: cameron
        except NameError: cameron = NonPlayableCharacter("Cameron", "Cameroon")
        try: josh
        except NameError: josh = NonPlayableCharacter("Josh", "Josh80085")
        try: julia
        except NameError: julia = NonPlayableCharacter("Julia")
        try: evelyn
        except NameError: evelyn = NonPlayableCharacter("Evelyn")
        try: autumn
        except NameError: autumn = NonPlayableCharacter("Autumn", "Its_Fall")
        try: sebastian
        except NameError: sebastian = NonPlayableCharacter("Sebastian", "Big Seb")
        try: grayson
        except NameError: grayson = NonPlayableCharacter("Grayson", "G-rayson")
        try: jenny
        except NameError: jenny = NonPlayableCharacter("Jenny")
        try: samantha
        except NameError: samantha = NonPlayableCharacter("Samantha", "SamFromSpaceJam")

        if isinstance(chloe, CustomCharacter):
            chloe = NonPlayableCharacter("Chloe", "Chloe101")
        if isinstance(amber, CustomCharacter):
            amber = NonPlayableCharacter("Amber", "Amber_xx")
        if isinstance(penelope, CustomCharacter):
            penelope = NonPlayableCharacter("Penelope", "Penelopeeps")
        if isinstance(riley, CustomCharacter):
            riley = NonPlayableCharacter("Riley", "RileyReads")
        if isinstance(lindsey, CustomCharacter):
            lindsey = NonPlayableCharacter("Lindsey", "LindsLou")
        if isinstance(lauren, CustomCharacter):
            lauren = NonPlayableCharacter("Lauren", "LoLoLauren")
        if isinstance(emily, CustomCharacter):
            emily = NonPlayableCharacter("Emily", "emilyyyy")
        if isinstance(ms_rose, CustomCharacter):
            ms_rose = NonPlayableCharacter("Ms Rose")
        if isinstance(nora, CustomCharacter):
            nora = NonPlayableCharacter("Nora", "Nora_12")
        if isinstance(aubrey, CustomCharacter):
            aubrey = NonPlayableCharacter("Aubrey", "Aubs123")
        if isinstance(ryan, CustomCharacter):
            ryan = NonPlayableCharacter("Ryan", "Ryanator")
        if isinstance(imre, CustomCharacter):
            imre = NonPlayableCharacter("Imre", "BadBoyImre")
        if isinstance(chris, CustomCharacter):
            chris = NonPlayableCharacter("Chris", "Chriscuit")
        if isinstance(charli, CustomCharacter):
            charli = NonPlayableCharacter("Charli", "CharliAndTheCockFactory")
        if isinstance(cameron, CustomCharacter):
            cameron = NonPlayableCharacter("Cameron", "Cameroon")
        if isinstance(josh, CustomCharacter):
            josh = NonPlayableCharacter("Josh", "Josh80085")

        ms_rose.name = "Ms Rose"
        chloe.username = "Chloe101"
        amber.username = "Amber_xx"
        penelope.username = "Penelopeeps"
        riley.username = "RileyReads"
        lindsey.username = "LindsLou"
        lauren.username = "LoLoLauren"
        emily.username = "emilyyyy"
        nora.username = "Nora_12"
        aubrey.username = "Aubs123"
        ryan.username = "Ryanator"
        imre.username = "BadBoyImre"
        chris.username = "Chriscuit"
        charli.username = "CharliAndTheCockFactory"
        cameron.username = "Cameroon"
        josh.username = "Josh80085"
        autumn.username = "Its_Fall"
        sebastian.username = "Big Seb"
        grayson.username = "G-rayson"
        mason.username = "Mason_Mas"
        elijah.username = "Elijah_Woods"
        caleb.username = "Aleb"
        aaron.username = "DoubleARon"
        naomi.username = "NaomiXMarie"
        samantha.username = "SamFromSpaceJam"

        try:
            if elijah.relationship == Relationship.MAKEFUN:
                CharacterService.set_mood(elijah, Moods.HURT)
        except AttributeError: pass

        try:
            if evelyn.relationship == Relationship.MOVE:
                v2_made_a_move_on_evelyn = True
        except AttributeError: pass

        for character in (josh, lauren, chris, autumn, chloe, imre, nora):
            try:
                if character.relationship == Relationship.MAD:
                    CharacterService.set_mood(character, Moods.MAD)
            except AttributeError: pass

        try:
            if evelyn.relationship == Relationship.LIKES:
                v6_evelyn_successful_date = True
        except AttributeError: pass

#endregion NonPlayableCharacters
        try:
            bro = reputation.components[Reputations.BRO]
            boyfriend = reputation.components[Reputations.BOYFRIEND]
            troublemaker = reputation.components[Reputations.TROUBLEMAKER]
        except KeyError: pass

        ## KCT
        try:
            reputation.components = {
                RepComponent.BRO: bro,
                RepComponent.BOYFRIEND: boyfriend,
                RepComponent.TROUBLEMAKER: troublemaker,
            }
        except NameError: pass

        try:
            locked_reputation = locked_kct
        except NameError: pass

        ### APPLICATIONS
        messenger.name = "Messenger"

        try:
            messenger.contacts = contacts.copy()
            del contacts
        except NameError: pass

        # Transfer kiwiiApp to kiwii
        try:
            kiwii = kiwiiApp
            kiwii.home_screen = "kiwiiApp"
            kiwii.locked = kiwiiApp.locked
            kiwii.contacts = []
            del kiwiiApp
        except NameError: pass
            
        if not isinstance(kiwii, Application):
            kiwii = Application("kiwii")

        for app in phone.applications:
            app.home_screen = "{}_home".format(app.name.lower())

        messenger.home_screen = "{}_home".format(messenger.name.lower())
        achievement_app.home_screen = "{}_home".format(achievement_app.name.lower())
        kiwii.home_screen = "{}_home".format(kiwii.name.lower())
        simplr_app.home_screen = "{}_home".format(simplr_app.name.lower())
        relationship_app.home_screen = "{}_home".format(relationship_app.name.lower())

        for contact in messenger.contacts:
            try: contact.sent_messages
            except AttributeError: contact.sent_messages = []

            try: contact.sent_messages = contact.sentMessages
            except AttributeError: pass

            try: contact.pending_messages
            except AttributeError: contact.pending_messages = []

            try: contact.pending_messages = contact.pendingMessages
            except AttributeError: pass

            try: contact._notification
            except AttributeError: contact._notification = False

            try: contact.user
            except AttributeError:
                contact.user = getattr(store, contact.name.lower().replace(' ', '_'))

        ### KIWII
        #### KIWII POSTS
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

        try:
            kiwii_posts = kiwiiPosts
            del kiwiiPosts
        except NameError: pass

        for kiwii_post in kiwii_posts:
            if kiwii_post.user == "Aaron": kiwii_post.user = aaron
            if kiwii_post.user == "Amber": kiwii_post.user = amber
            if kiwii_post.user == "Aubrey": kiwii_post.user = aubrey
            if kiwii_post.user == "Autumn": kiwii_post.user = autumn
            if kiwii_post.user == "Caleb": kiwii_post.user = caleb
            if kiwii_post.user == "Cameron": kiwii_post.user = cameron
            if kiwii_post.user == "Charli": kiwii_post.user = charli
            if kiwii_post.user == "Chloe": kiwii_post.user = chloe
            if kiwii_post.user == "Chris": kiwii_post.user = chris
            if kiwii_post.user == "Elijah": kiwii_post.user = elijah
            if kiwii_post.user == "Emily": kiwii_post.user = emily
            if kiwii_post.user == "Grayson": kiwii_post.user = grayson
            if kiwii_post.user == "Imre": kiwii_post.user = imre
            if kiwii_post.user == "Josh": kiwii_post.user = josh
            if kiwii_post.user == "Lauren": kiwii_post.user = lauren
            if kiwii_post.user == "LewsOfficial": kiwii_post.user = lews_official
            if kiwii_post.user == "Lindsey": kiwii_post.user = lindsey
            if kiwii_post.user == "Mason": kiwii_post.user = mason
            if kiwii_post.user == "MC": kiwii_post.user = mc
            if kiwii_post.user == "Naomi": kiwii_post.user = naomi
            if kiwii_post.user == "Nora": kiwii_post.user = nora
            if kiwii_post.user == "Parker": kiwii_post.user = parker
            if kiwii_post.user == "Penelope": kiwii_post.user = penelope
            if kiwii_post.user == "Riley": kiwii_post.user = riley
            if kiwii_post.user == "Ryan": kiwii_post.user = ryan
            if kiwii_post.user == "Samantha": kiwii_post.user = samantha
            if kiwii_post.user == "Sebastian": kiwii_post.user = sebastian

            for mention in kiwii_post.mentions:
                temp_mentions = []
                if mention == "Aaron": temp_mentions.append(aaron)
                if mention == "Amber": temp_mentions.append(amber)
                if mention == "Aubrey": temp_mentions.append(aubrey)
                if mention == "Autumn": temp_mentions.append(autumn)
                if mention == "Caleb": temp_mentions.append(caleb)
                if mention == "Cameron": temp_mentions.append(cameron)
                if mention == "Charli": temp_mentions.append(charli)
                if mention == "Chloe": temp_mentions.append(chloe)
                if mention == "Chris": temp_mentions.append(chris)
                if mention == "Elijah": temp_mentions.append(elijah)
                if mention == "Emily": temp_mentions.append(emily)
                if mention == "Grayson": temp_mentions.append(grayson)
                if mention == "Imre": temp_mentions.append(imre)
                if mention == "Josh": temp_mentions.append(josh)
                if mention == "Lauren": temp_mentions.append(lauren)
                if mention == "LewsOfficial": temp_mentions.append(lews_official)
                if mention == "Lindsey": temp_mentions.append(lindsey)
                if mention == "Mason": temp_mentions.append(mason)
                if mention == "MC": temp_mentions.append(mc)
                if mention == "Naomi": temp_mentions.append(naomi)
                if mention == "Nora": temp_mentions.append(nora)
                if mention == "Parker": temp_mentions.append(parker)
                if mention == "Penelope": temp_mentions.append(penelope)
                if mention == "Riley": temp_mentions.append(riley)
                if mention == "Ryan": temp_mentions.append(ryan)
                if mention == "Samantha": temp_mentions.append(samantha)
                if mention == "Sebastian": temp_mentions.append(sebastian)
                kiwii_post.mentions = temp_mentions

            try: kiwii_post.number_likes
            except AttributeError: kiwii_post.number_likes = kiwii_post.numberLikes

            try:
                kiwii_post.image = kiwii_post.img
                del kiwii_post.img
            except AttributeError: pass

            try:
                kiwii_post.message = kiwii_post.caption
                del kiwii_post.caption
            except AttributeError: pass

            try: del kiwii_post.profilePicture
            except AttributeError: pass

            try:
                kiwii_post.sentComments = kiwii_post.comments
                del kiwii_post.comments
            except AttributeError: pass

            try:
                kiwii_post.sent_comments = kiwii_post.sentComments
                del kiwii_post.sentComments
            except AttributeError: pass

            try: kiwii_post.pendingComments
            except AttributeError: kiwii_post.pendingComments = []

            try: kiwii_post.pending_comments
            except AttributeError: kiwii_post.pending_comments = kiwii_post.pendingComments

            if kiwii_post.image == "images/aupost1.png":
                kiwii_post.image = "images/phone/kiwii/Posts/v7/aupost1.webp"
            if kiwii_post.image == "images/chpost1.png":
                kiwii_post.image = "images/phone/kiwii/Posts/v7/chpost1.webp"
            if kiwii_post.image == "images/clpost1.png":
                kiwii_post.image = "images/phone/kiwii/Posts/v7/clpost1.webp"
            if kiwii_post.image == "images/empost1.png":
                kiwii_post.image = "images/phone/kiwii/Posts/v7/empost1.webp"
            if kiwii_post.image == "images/lapost1.png":
                kiwii_post.image = "images/phone/kiwii/Posts/v7/lapost1.webp"

            ##### KIWII SENT COMMENTS
            for comment in kiwii_post.sent_comments + kiwii_post.pending_comments:
                if comment.user == "Aaron": comment.user = aaron
                if comment.user == "Amber": comment.user = amber
                if comment.user == "Aubrey": comment.user = aubrey
                if comment.user == "Autumn": comment.user = autumn
                if comment.user == "Caleb": comment.user = caleb
                if comment.user == "Cameron": comment.user = cameron
                if comment.user == "Charli": comment.user = charli
                if comment.user == "Chloe": comment.user = chloe
                if comment.user == "Chris": comment.user = chris
                if comment.user == "Elijah": comment.user = elijah
                if comment.user == "Emily": comment.user = emily
                if comment.user == "Grayson": comment.user = grayson
                if comment.user == "Josh": comment.user = josh
                if comment.user == "Imre": comment.user = imre
                if comment.user == "Lauren": comment.user = lauren
                if comment.user == "LewsOfficial": comment.user = lews_official
                if comment.user == "Lindsey": comment.user = lindsey
                if comment.user == "Mason": comment.user = mason
                if comment.user == "MC": comment.user = mc
                if comment.user == "Naomi": comment.user = naomi
                if comment.user == "Nora": comment.user = nora
                if comment.user == "Parker": comment.user = parker
                if comment.user == "Penelope": comment.user = penelope
                if comment.user == "Riley": comment.user = riley
                if comment.user == "Ryan": comment.user = ryan
                if comment.user == "Samantha": comment.user = samantha
                if comment.user == "Sebastian": comment.user = sebastian

                if comment.mentions is None:
                    comment.mentions = []

                for mention in comment.mentions:
                    temp_mentions = []
                    if mention == "Aaron": temp_mentions.append(aaron)
                    if mention == "Amber": temp_mentions.append(amber)
                    if mention == "Aubrey": temp_mentions.append(aubrey)
                    if mention == "Autumn": temp_mentions.append(autumn)
                    if mention == "Caleb": temp_mentions.append(caleb)
                    if mention == "Cameron": temp_mentions.append(cameron)
                    if mention == "Charli": temp_mentions.append(charli)
                    if mention == "Chloe": temp_mentions.append(chloe)
                    if mention == "Chris": temp_mentions.append(chris)
                    if mention == "Elijah": temp_mentions.append(elijah)
                    if mention == "Emily": temp_mentions.append(emily)
                    if mention == "Grayson": temp_mentions.append(grayson)
                    if mention == "Imre": temp_mentions.append(imre)
                    if mention == "Josh": temp_mentions.append(josh)
                    if mention == "Lauren": temp_mentions.append(lauren)
                    if mention == "LewsOfficial": temp_mentions.append(lews_official)
                    if mention == "Lindsey": temp_mentions.append(lindsey)
                    if mention == "Mason": temp_mentions.append(mason)
                    if mention == "MC": temp_mentions.append(mc)
                    if mention == "Naomi": temp_mentions.append(naomi)
                    if mention == "Nora": temp_mentions.append(nora)
                    if mention == "Parker": temp_mentions.append(parker)
                    if mention == "Penelope": temp_mentions.append(penelope)
                    if mention == "Riley": temp_mentions.append(riley)
                    if mention == "Ryan": temp_mentions.append(ryan)
                    if mention == "Samantha": temp_mentions.append(samantha)
                    if mention == "Sebastian": temp_mentions.append(sebastian)
                    comment.mentions = temp_mentions

                try: comment.number_likes
                except AttributeError: comment.number_likes = comment.numberLikes

                ###### KIWII COMMENT REPLIES
                for reply in comment.replies:
                    reply.disabled = False

                    if reply.mentions is None:
                        reply.mentions = []

                    for mention in reply.mentions:
                        temp_mentions = []
                        if mention == "Aaron": temp_mentions.append(aaron)
                        if mention == "Amber": temp_mentions.append(amber)
                        if mention == "Aubrey": temp_mentions.append(aubrey)
                        if mention == "Autumn": temp_mentions.append(autumn)
                        if mention == "Caleb": temp_mentions.append(caleb)
                        if mention == "Cameron": temp_mentions.append(cameron)
                        if mention == "Charli": temp_mentions.append(charli)
                        if mention == "Chloe": temp_mentions.append(chloe)
                        if mention == "Chris": temp_mentions.append(chris)
                        if mention == "Elijah": temp_mentions.append(elijah)
                        if mention == "Emily": temp_mentions.append(emily)
                        if mention == "Grayson": temp_mentions.append(grayson)
                        if mention == "Imre": temp_mentions.append(imre)
                        if mention == "Josh": temp_mentions.append(josh)
                        if mention == "Lauren": temp_mentions.append(lauren)
                        if mention == "LewsOfficial": temp_mentions.append(lews_official)
                        if mention == "Lindsey": temp_mentions.append(lindsey)
                        if mention == "Mason": temp_mentions.append(mason)
                        if mention == "MC": temp_mentions.append(mc)
                        if mention == "Naomi": temp_mentions.append(naomi)
                        if mention == "Nora": temp_mentions.append(nora)
                        if mention == "Parker": temp_mentions.append(parker)
                        if mention == "Penelope": temp_mentions.append(penelope)
                        if mention == "Riley": temp_mentions.append(riley)
                        if mention == "Ryan": temp_mentions.append(ryan)
                        if mention == "Samantha": temp_mentions.append(samantha)
                        if mention == "Sebastian": temp_mentions.append(sebastian)
                        reply.mentions = temp_mentions

                    try: reply.number_likes
                    except AttributeError: reply.number_likes = reply.numberLikes

        kiwii_posts = [kiwii_post for kiwii_post in kiwii_posts if hasattr(kiwii_post.user, "name")]

        # Simplr Contacts
        try:
            simplr_app.contacts = simplr_contacts
            del simpler_contacts
        except NameError: pass

        try:
            simplr_app.pending_contacts = simplr_pendingContacts
            del simplr_pendingContacts
        except NameError: pass

        try: simplr_app.contacts
        except AttributeError: simplr_app.contacts = []

        try: simplr_app.pending_contacts
        except AttributeError: simplr_app.pending_contacts = []

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

        try:
            for contact in (simplr_app.contacts + simplr_app.pending_contacts):

                try: contact.pending_messages
                except AttributeError:
                    contact.pending_messages = contact.pendingMessages
                    del contact.pendingMessages

                try: contact.sent_messages
                except AttributeError:
                    contact.sent_messages = contact.sentMessages
                    del contact.sentMessages

                try: contact._notification
                except AttributeError: contact._notification = False

                try: contact.user
                except AttributeError:
                    contact.user = getattr(store, contact.name.lower().replace(' ', '_'))
        except NameError:
            pass

        ## RELATIONSHIP APP
        relationship_girls = [relationship_girl for relationship_girl in relationship_girls if hasattr(relationship_girl, "name")]

        # Items
        honey.insensitive_image = "images/v13/Scene 35/sex_shop/honey_insensitive.webp"
        butt_plug.insensitive_image = "images/v13/Scene 35/sex_shop/butt_plug_insensitive.webp"
        spankers.insensitive_image = "images/v13/Scene 35/sex_shop/spankers_insensitive.webp"
        cuffs.insensitive_image = "images/v13/Scene 35/sex_shop/cuffs_insensitive.webp"
        feather.insensitive_image = "images/v13/Scene 35/sex_shop/feather_insensitive.webp"

        # Variables
        try: 
            real_life_mode = realmode
            del realmode
        except NameError:
            pass

        try:
            if chlorers: chloers = True
        except NameError: pass
        
        try: kiwiiPost1
        except NameError: kiwii_first_time = False

        try:
            kiwii_first_time = kiwii_firstTime
            del kiwii_firstTime
        except NameError: pass

        try:
            if v13s40fromgame: sceneList.add("v13_chloe")
        except NameError: pass
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
        
        try:
            if rileysex: sceneList.add("v7_riley")
        except NameError: pass
        try:
            if v8_riley_lewd_ending: sceneList.add("v8_riley")
        except NameError: pass
        try:
            if v11_aubrey_sex: sceneList.add("v11_aubrey")
        except NameError: pass
        try:
            if v11_fucked_candy: sceneList.add("v11_candy")
        except NameError: pass
        try:
            if v11_msrose_scene: sceneList.add("v11_rose")
        except NameError: pass
        try:
            if v12_lauren_sex: sceneList.add("v12_lauren")
        except NameError: pass
        try:
            if v12_lindsey_sex: sceneList.add("v12_lindsey")
        except NameError: pass
        try:
            if v12_nora_sex: sceneList.add("v12_nora")
        except NameError: pass
        try:
            if v12_msrose_sex: sceneList.add("v12_rose")
        except NameError: pass
        try:
            if v13_emilysex: sceneList.add("v13_emily")
        except NameError: pass
        try:
            if v13_emmysex: sceneList.add("v13_emmy")
        except NameError: pass
        try:
            if v13_FirstThreesome: sceneList.add("v14_threesome")
        except NameError: pass
        try:
            if v14_amber_sex: sceneList.add("v14_amber")
        except NameError: pass
        try:
            if v14_jenny_sex: sceneList.add("v14_jenny")
        except NameError: pass
        try:
            if v14_samantha_sex: sceneList.add("v14_samantha")
        except NameError: pass
        try:
            if v7_seencrowning: freeroam4.add("crowning")
        except NameError: pass
        try:
            if v13s37_frnora: freeroam11.add("nora")
        except NameError: pass
        try:
            if v9_sex_with_riley: sceneList.add("v9_riley")
        except NameError: pass
        try:
            if v15_emily_sext: sceneList.add("v15_emily")
            del v15_emily_sext
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

        try: v7_emily_bowling
        except NameError: v7_emily_bowling = False
        try: v8_dodged_pipe
        except NameError: v8_dodged_pipe = False
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
        try: v12_lauren_points
        except NameError: v12_lauren_points = 0
        try: v12s32_Aubrey_Boost
        except NameError: v12s32_Aubrey_Boost = False
        try: v12_murder_count
        except NameError: v12_murder_count = 0
        try: v12s7_victims
        except NameError: v12s7_victims = 12
        try: v12s23a_sam
        except NameError: v12s23a_sam = False
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
        try: v11_tease_amber
        except NameError: v11_tease_amber = 0
        try: v11_manhunt_winner
        except NameError: v11_manhunt_winner = "Ryan"
        try: v11_riley_roomate
        except NameError: v11_riley_roomate = False
        try: v11s25_beer
        except NameError: v11s25_beer = True
        try: v11_solo_question
        except NameError: v11_solo_question = False
        try: v11_kiss_nora
        except NameError: v11_kiss_nora = False
        try: v11_told_aubrey
        except NameError: v11_told_aubrey = False
        try: v11_lindsey_slogan
        except NameError: v11_lindsey_slogan = 0 
        try: v11_linds_inv_imre
        except NameError: v11_linds_inv_imre = False 
        try: v11_overtake_points
        except NameError: v11_overtake_points = 0
        try: v11_hp_points
        except NameError: v11_hp_points = 0
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
        try: v13s20_bleach_suitcase
        except NameError: v13s20_bleach_suitcase = False
        try: v13_aubrey_vote
        except NameError: v13_aubrey_vote = "na"
        try: v14_ryan_satin
        except NameError: v14_ryan_satin = False

    hide screen reply
    hide screen simplr_reply

    if config.developer:
        show screen bug_testing_overlay
    else:
        hide screen bug_testing_overlay

    return