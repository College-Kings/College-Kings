python early:
    old_files = {
        "bugTesting/bugTesting_Overwrite.rpy",
        "bugTesting/bugTesting_typoNotes.rpy",
        "bugTesting/bugTesting_cheats.rpy",
        "phone/phonescript.rpy",
        "phone/phoneStyle.rpy",
        "sceneGallery/sceneGallery.rpy",
        "v14/chicks_presidency_race/planning_board.rpy"
        "customCharacters.rpy",
        "functions.rpy",
        "path_builder.rpy",
        "scriptv06.rpy",
        "scriptv07.rpy",
        "screen.rpy",
    }

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

    # Helper function
    def write_console(data):
        with open("console.txt", "w") as f:
            f.write(str(data))

init 100 python:
    class CheatItem:
        pass

    class CustomCharacter(NonPlayableCharacter):
        pass

    class MainCharacter(PlayableCharacter):
        pass

    class Teacher(NonPlayableCharacter):
        pass


label after_load:
    python:
        # SAVE FIXES
        ## Force developer mode off on load
        config.developer = False

        # Disable skip transitions
        preferences.transitions = 2

        ### renpy.music.stop(channel=u'music')
        ### If using dummy files, don't need to stop music anymore

        ## PLAYABLE CHARACTERS
        if isinstance(mc, FightCharacter) or isinstance(mc, MainCharacter):
            mc = PlayableCharacter()

        # mc.__after_load__()

        try: mc.profile_picture
        except AttributeError: mc.profile_picture = profile_pictures[0]

        try: mc.username
        except AttributeError: mc.username = name

        try: mc.relationships
        except AttributeError: mc.relationships = set()

        try: mc.girlfriends
        except AttributeError: mc.girlfriends = set()


        # NonPlayable Character
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

        for character in NonPlayableCharacter.characters.values():
            character.__after_load__()

        ## Relationship types
        try:
            if kissamber: amber.relationship = Relationship.KISS
            del kissamber
        except NameError: pass
        try:
            if amberrs: amber.relationship = Relationship.FWB
            del amberrs
        except NameError: pass
        try:
            if aryssars: aryssa.relationship = Relationship.LIKES
            del aryssars
        except NameError: pass
        try:
            if aubreyrs: aubrey.relationship = Relationship.FWB
            del aubreyrs
        except NameError: pass
        try:
            if cameronBro: cameron.relationship = Relationship.BRO
            del cameronBro
        except NameError: pass
        try:
            if chloemad: chloe.relationship = Relationship.MAD
            del chloemad
        except NameError: pass
        try:
            if chloers: chloe.relationship = Relationship.FWB
            del chloers
        except NameError: pass
        try:
            if chloegf: chloe.relationship = Relationship.GIRLFRIEND
            del chloegf
        except NameError: pass
        try:
            if chrismad: chris.relationship = Relationship.MAD
            del chrismad
        except NameError: pass
        try:
            if emmyrs: emmy.relationship = Relationship.LIKES
            del emmyrs
        except NameError: pass
        try:
            if "v13_emmy" in sceneList: emmy.relationship = Relationship.FWB
        except NameError: pass
        try:
            if evelyndate: evelyn.relationship = Relationship.DATE
            del evelyndate
        except NameError: pass
        try:
            if evelynrs: evelyn.relationship = Relationship.LIKES
            del evelynrs
        except NameError: pass
        try:
            if imremad: imre.relationship = Relationship.MAD
            del imremad
        except NameError: pass
        try:
            if jennyawkward: jenny.relationship = Relationship.AWKWARD
            del jennyawkward
        except NameError: pass
        try:
            if jennyrs: jenny.relationship = Relationship.FWB
            del jennyrs
        except NameError: pass
        try:
            if joshmad or joshmadfr: josh.relationship = Relationship.MAD
            del joshmad
            del joshmadfr
        except NameError: pass
        try:
            if kourtneyrs: kourtney.relationship = Relationship.LIKES
            del kourtneyrs
        except NameError: pass
        try:
            if laurenmad: lauren.relationship = Relationship.MAD
            del laurenmad
        except NameError: pass
        try:
            if laurenrs: lauren.relationship = Relationship.GIRLFRIEND
            del laurenrs
        except NameError: pass
        try:
            if laurenrs_v11aubrey and (v11_aubrey_sex or "v11_aubrey" in sceneList): v11_lauren_caught_aubrey = True
            del laurenrs_v11aubrey
        except NameError: pass
        try:
            if lindseyfirstkiss: lindsey.relationship = Relationship.KISS
            del lindseyfirstkiss
        except NameError: pass
        try:
            if lindseyrs: lindsey.relationship = Relationship.FWB
            del lindseyrs
        except NameError: pass
        try:
            if v10_ms_r_kiss: ms_rose.relationship = Relationship.KISS
            del v10_ms_r_kiss
        except NameError: pass
        try:
            if msrosers: ms_rose.relationship = Relationship.FWB
            del msrosers
        except NameError: pass
        try:
            if noralikes: nora.relationship = Relationship.LIKES
            del noralikes
        except NameError: pass
        try:
            if norars: nora.relationship = Relationship.FWB
            del norars
        except NameError: pass
        try:
            if penelopers: penelope.relationship = Relationship.LIKES
            del penelopers
        except NameError: pass
        try:
            if penelopeloyal: penelope.relationship = Relationship.LOYAL
            del penelopeloyal
        except NameError: pass
        try:
            if rileykiss: riley.relationship = Relationship.MOVE
            del rileykiss
        except NameError: pass
        try:
            if rileyrs: riley.relationship = Relationship.FWB
            del rileyrs
        except NameError: pass
        try:
            if v11_samantha_spa: sceneList.add("v11_samantha")
        except NameError: pass
        try:
            if v11_samantha_spa: samantha.relationship = Relationship.MOVE
            del v11_samantha_spa
        except NameError: pass
        try:
            if "v14_samantha" in sceneList: samantha.relationship = Relationship.FWB
        except NameError: pass


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
        adam.username = "A.D.A.M."
        mason.username = "Mason_Mas"
        elijah.username = "Elijah_Woods"
        kim.username = "KimPlausible"
        caleb.username = "Aleb"
        kai.username = "KaiCriesWith2Ply"
        aaron.username = "DoubleARon"
        naomi.username = "NaomiXMarie"
        samantha.username = "SamFromSpaceJam"

        if chloe.relationship == 4:
            chloe.relationship = Relationship.MAD

        ## PHONE
        ### APPLICATIONS
        try:
            messenger.contacts = contacts
            del contacts
        except NameError: pass

        # Transfer statsApp to stats_app
        try:
            stats_app.locked = statsApp.locked
            del statsApp
        except NameError: pass

        # Transfer kiwiiApp to kiwii
        try:
            kiwii = kiwiiApp
            kiwii.image = "images/phone/kiwii/appAssets/kiwiiIcon.webp"
            kiwii.home_screen = "kiwiiApp"
            kiwii.locked = kiwiiApp.locked
            kiwii.contacts = []
            del kiwiiApp
        except NameError:
            kiwii = Application("Kiwii", "kiwii/appAssets/kiwiiIcon.webp", "kiwiiApp", locked=False)

        # Unlock simplr_app
        simplr_app.unlock()

        for app in phone.applications.copy():
            try: app.locked
            except AttributeError: phone.applications.remove(app)

        ### MESSENGER
        #### MESSENGER CONTRACTS
        for contact in messenger.contacts:
            try: contact.sent_messages = contact.sentMessages
            except AttributeError: contact.sent_messages = []

            try: contact.pending_messages = contact.pendingMessages
            except AttributeError: contact.pending_messages = []


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

        # Correct image paths
        message = josh.messenger.find_message("images/text1.webp")
        try:
            message.image = "images/v4/text1.webp"
        except AttributeError: pass

        message = amber.messenger.find_message("images/text2.webp")
        try:
            message.image = "images/v6/text2.webp"
        except AttributeError: pass

        message = aubrey.messenger.find_message("images/text3.webp")
        try:
            message.image = "images/v6/text3.webp"
        except AttributeError: pass
        del message


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

        for kiwii_post in kiwiiPosts:
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

            try: kiwii_post.pendingComments
            except AttributeError: kiwii_post.pendingComments = []

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
            for comment in kiwii_post.sentComments:
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

                ###### KIWII COMMENT REPLIES
                for reply in comment.replies:
                    reply.disabled = False

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

            ##### KIWII PENDING COMMENTS
            for comment in kiwii_post.pendingComments:
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
                if comment.user == "Imre": comment.user = imre
                if comment.user == "Josh": comment.user = josh
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

                ###### KIWII COMMENT REPLIES
                for reply in comment.replies:
                    reply.disabled = False

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

        for contact in (simplr_contacts + simplr_pendingContacts):
            for (dirpath, dirname, filenames) in os.walk(os.path.join(contacts_file_path, contact.name.lower(), "large_profile_pictures")):
                contact.large_profile_pictures = ["images/nonplayable_characters/{}/large_profile_pictures/{}".format(contact.name.lower(), filename) for filename in filenames]

            try: contact.pending_messages
            except AttributeError:
                contact.pending_messages = contact.pendingMessages
                del contact.pendingMessages

            try: contact.sent_messages
            except AttributeError:
                contact.sent_messages = contact.sentMessages
                del contact.sentMessages

        
        # Items
        honey.insensitive_image = "images/v13/Scene 35/sex_shop/honey_insensitive.webp"
        butt_plug.insensitive_image = "images/v13/Scene 35/sex_shop/butt_plug_insensitive.webp"
        spankers.insensitive_image = "images/v13/Scene 35/sex_shop/spankers_insensitive.webp"
        cuffs.insensitive_image = "images/v13/Scene 35/sex_shop/cuffs_insensitive.webp"
        feather.insensitive_image = "images/v13/Scene 35/sex_shop/feather_insensitive.webp"

        # Variables
        try:
            if chlorers: chloers = True
        except NameError: pass
        try: kiwiiPost1
        except NameError: kiwii_firstTime = False

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
        try: candyLike
        except NameError: candyLike = 0
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
        try: v13s20_bleach_suitcase
        except NameError: v13s20_bleach_suitcase = False
        try: v13_aubrey_vote
        except NameError: v13_aubrey_vote = "na"
        try: v14_ryan_satin
        except NameError: v14_ryan_satin = False

        # v1502 fixes:
        
        if chloe.relationship == Relationship.MAD.value:
            chloe.relationship = Relationship.MAD

        if renpy.loadable("v15/scene1.rpy") and not v1502fix:
       
            if ms_rose.relationship == Relationship.FRIEND:
                if v15_threaten_ms_rose:
                    ms_rose.relationship = Relationship.THREATEN
                
                elif any(scene in sceneList for scene in ("v11_rose", "v12_rose", "v15_rose")):
                    ms_rose.relationship = Relationship.FWB
            
            if chloe.relationship == Relationship.FRIEND:
                if chloeSus > 1 + v15s7_chloe_empathize:
                    chloe.relationship = Relationship.GIRLFRIEND
                
                elif meetchloe and hcGirl == "chloe" and ending == "chloe":
                    chloe.relationship = Relationship.GIRLFRIEND # don't have another way of checking if the question was asked, so we'll give this status for free
                
                elif any(scene in sceneList for scene in ("v8_chloe", "v10_chloe", "v11_chloe", "v13_chloe", "v14_chloe")):
                    chloe.relationship = Relationship.FWB
                
                elif chloeSus == 1 + v15s7_chloe_empathize:
                    chloe.relationship = Relationship.FWB
            
            if emily.relationship == Relationship.FRIEND:
                if any(scene in sceneList for scene in ("v6_emily", "v9_emily", "v13_emily")):
                    emily.relationship = Relationship.FWB
                
            if riley.relationship == Relationship.LOYAL:
                riley.relationship = Relationship.FRIEND
                RileyLoyal = True
            
            if riley.relationship == Relationship.FRIEND:
                if any(scene in sceneList for scene in ("v7_riley", "v8_riley", "v9_riley", "v10_riley", "v11_riley", "v13_riley")):
                    riley.relationship = Relationship.FWB
                
                elif "riley" in hcAsked:
                    riley.relationship = Relationship.LIKES # technically it should be MOVE, but we're feeling generous
            
            if aubrey.relationship == Relationship.FRIEND:
                if "v15_naomi" in sceneList:
                    aubrey.relationship = Relationship.MAD
                
                elif RileyLoyal:
                    if any(scene in sceneList for scene in ("v3_aubrey", "v6_aubrey")):
                        aubrey.relationship = Relationship.FWB
                
                elif v13s48_canoeing_as_date and v15s9_wedding_date:
                    aubrey.relationship = Relationship.TAMED
                
                elif "v3_aubrey" in sceneList or "v6_aubrey" in sceneList:
                    aubrey.relationship = Relationship.FWB
            
            if lauren.relationship == Relationship.FRIEND:
                if any(scene in sceneList for scene in ("v10_lauren", "v12_lauren")):
                    lauren.relationship = Relationship.GIRLFRIEND
                
                # elif lauren.points >= 4 or (lauren.points == 2 and v11_hp_points < 3) or (lauren.points == 0 and v11_hp_points < 2) or (lauren.points == -2 and v11_hp_points == 0): lauren.relationship = Relationship.GIRLFRIEND
                elif lauren.points >= v11_hp_points * 2 - 2 and not "v11_aubrey" in sceneList and not (len(freeroam7) == 0) and not (lauren.points == 0 and v11_hp_points == 0):
                    lauren.relationship = Relationship.GIRLFRIEND
                                
                elif "v15_lauren" in sceneList:
                    lauren.relationship = Relationship.FWB

            if lauren.relationship == Relationship.GIRLFRIEND:
                if autumn.relationship == Relationship.FWB:
                    autumn.relationship = Relationship.LOYAL
                    
            if autumn.relationship == Relationship.FRIEND:
                if AutumnTrust:
                    autumn.relationship = Relationship.LOYAL
            
            if amber.relationship == Relationship.FRIEND:
                if any(scene in sceneList for scene in ("v8_amber", "v8_amber2", "v10_amber", "v14_amber")):
                    amber.relationship = Relationship.FWB
                
            if jenny.relationship == Relationship.FRIEND:
                if "v14_jenny" in sceneList:
                    jenny.relationship = Relationship.FWB
                
            if lindsey.relationship == Relationship.FRIEND:
                if "v12_lindsey" in sceneList:
                    lindsey.relationship = Relationship.FWB

                elif "v9_lindsey" in sceneList:
                    lindsey.relationship = Relationship.KISS
            
            if samantha.relationship == Relationship.FRIEND:
                if "v14_samantha" in sceneList: samantha.relationship = Relationship.FWB

                elif "v11_samantha" in sceneList: samanatha.relationship = Relationship.MOVE
            
            if candy.relationship == Relationship.FRIEND:
                if "v11_candy" in sceneList:
                    candy.relationship = Relationship.FWB

            if penelope.relationship == Relationship.FRIEND:
                if v14_penelope_date and not (v15s18a_showlist_penelope_autumn and lauren.relationship == Relationship.GIRLFRIEND):
                    penelope.relationship = Relationship.LOYAL

                elif v14_penelope_date:
                    penelope.relationship = Relationship.LIKES

            v1502fix = True

        setup()

    hide screen reply
    hide screen simplr_reply

    if config.developer:
        show screen bugTesting_Overlay
    else:
        hide screen bugTesting_Overlay

    return