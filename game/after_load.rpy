python early:
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
        # SAVE FIXES:

        # Disable skip transitions
        preferences.transitions = 2

        renpy.music.stop(channel=u'music') ### temporary emergency break

        ## PLAYABLE CHARACTERS
        try: mc.profile_picture
        except AttributeError: mc.profile_picture = profile_pictures[0]

        try: mc.username
        except AttributeError: mc.username = name


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

        ##Relationship types
        try:
            if evelyndate: evelyn.relationship = Relationship.DATE
        except NameError: pass
        try:
            if evelynrs: evelyn.relationship = Relationship.LIKES
        except NameError: pass
        try:
            if aryssars: aryssa.relationship = Relationship.LIKES
        except NameError: pass
        try:
            if kourtneyrs: kourtney.relationship = Relationship.LIKES
        except NameError: pass


        for character in (
            chloe,
            amber,
            penelope,
            riley,
            lindsey,
            lauren,
            emily,
            ms_rose,
            nora,
            aubrey,
            ryan,
            imre,
            chris,
            charli,
            cameron,
            josh,
            julia,
            evelyn,
            autumn,
            sebastian,
            grayson,
            jenny,
        ):
            character.__after_load__()

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
            if kiwii is False:
                kiwii = Application("Kiwii", "kiwii/appAssets/kiwiiIcon.webp", "kiwiiApp", locked=True)

        # Transfer simplrApp to simplr_app
        try:
            simplr_app.locked = simplrApp.locked
        except NameError:
            pass

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
            if kiwii_post.user == "Chloe": kiwii_post.user = chloe
            if kiwii_post.user == "Lauren": kiwii_post.user = lauren
            if kiwii_post.user == "Aubrey": kiwii_post.user = aubrey
            if kiwii_post.user == "Grayson": kiwii_post.user = grayson
            if kiwii_post.user == "Riley": kiwii_post.user = riley
            if kiwii_post.user == "MC": kiwii_post.user = mc
            if kiwii_post.user == "Chris": kiwii_post.user = chris
            if kiwii_post.user == "Aaron": kiwii_post.user = aaron
            if kiwii_post.user == "Cameron": kiwii_post.user = cameron
            if kiwii_post.user == "Samantha": kiwii_post.user = samantha
            if kiwii_post.user == "Autumn": kiwii_post.user = autumn
            if kiwii_post.user == "Sebastian": kiwii_post.user = sebastian
            if kiwii_post.user == "Imre": kiwii_post.user = imre
            if kiwii_post.user == "Lindsey": kiwii_post.user = lindsey
            if kiwii_post.user == "Amber": kiwii_post.user = amber
            if kiwii_post.user == "LewsOfficial": kiwii_post.user = lews_official
            if kiwii_post.user == "Naomi": kiwii_post.user = naomi

            try:
                kiwii_post.image = kiwii_post.img
                del kiwii_post.img
            except AttributeError: pass

            ##### KIWII SENT COMMENTS
            for comment in kiwii_post.sentComments:
                if comment.user == "Chloe": comment.user = chloe
                if comment.user == "Lauren": comment.user = lauren
                if comment.user == "Aubrey": comment.user = aubrey
                if comment.user == "Grayson": comment.user = grayson
                if comment.user == "Riley": comment.user = riley
                if comment.user == "MC": comment.user = mc
                if comment.user == "Chris": comment.user = chris
                if comment.user == "Aaron": comment.user = aaron
                if comment.user == "Cameron": comment.user = cameron
                if comment.user == "Samantha": comment.user = samantha
                if comment.user == "Autumn": comment.user = autumn
                if comment.user == "Sebastian": comment.user = sebastian
                if comment.user == "Imre": comment.user = imre
                if comment.user == "Lindsey": comment.user = lindsey
                if comment.user == "Amber": comment.user = amber
                if comment.user == "LewsOfficial": comment.user = lews_official
                if comment.user == "Naomi": comment.user = naomi

                ###### KIWII COMMENT REPLIES
                for reply in comment.replies:
                    reply.disabled = False

            ##### KIWII PENDING COMMENTS
            for comment in kiwii_post.pendingComments:
                if comment.user == "Chloe": comment.user = chloe
                if comment.user == "Lauren": comment.user = lauren
                if comment.user == "Aubrey": comment.user = aubrey
                if comment.user == "Grayson": comment.user = grayson
                if comment.user == "Riley": comment.user = riley
                if comment.user == "MC": comment.user = mc
                if comment.user == "Chris": comment.user = chris
                if comment.user == "Aaron": comment.user = aaron
                if comment.user == "Cameron": comment.user = cameron
                if comment.user == "Samantha": comment.user = samantha
                if comment.user == "Autumn": comment.user = autumn
                if comment.user == "Sebastian": comment.user = sebastian
                if comment.user == "Imre": comment.user = imre
                if comment.user == "Lindsey": comment.user = lindsey
                if comment.user == "Amber": comment.user = amber
                if comment.user == "LewsOfficial": comment.user = lews_official
                if comment.user == "Naomi": comment.user = naomi

                ###### KIWII COMMENT REPLIES
                for reply in pendingComment.replies:
                    reply.disabled = False


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
        
        try:
            if v13_emilysex: sceneList.add("v13_emily")
        except NameError: pass
        try:
            if v11_fucked_candy: sceneList.add("v11_candy")
        except NameError: pass
        try:
            if v11_msrose_scene: sceneList.add("v11_rose")
        except NameError: pass
        try:
            if v13_emmysex: sceneList.add("v13_emmy")
        except NameError: pass
        try:
            if v12_msrose_sex: sceneList.add("v12_rose")
        except NameError: pass
        try:
            if v12_lauren_sex: sceneList.add("v12_lauren")
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
        try: laurenrs_v11aubrey
        except NameError: laurenrs_v11aubrey = False
        try: v13s40fromgame
        except NameError: v13s40fromgame = False
        try: v13_aubrey_vote
        except NameError: v13_aubrey_vote = "na"
        try: v14_ryan_satin
        except NameError: v14_ryan_satin = False


        # Before main menu redundancy
            ## Phone setup
        phone.applications = []
        phone.applications.append(messenger)
        phone.applications.append(stats_app)
        phone.applications.append(achievement_app)
        phone.applications.append(kiwii)
        phone.applications.append(simplr_app)

            ## Set up murder mystery stats
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


    show no_hard_feelings at achievementShow
    $ achievementAtList = renpy.get_at_list("no_hard_feelings")
    hide no_hard_feelings

    show screen phone_icon
    hide screen getaccess
    hide screen phone

    if config.developer:
        show screen bugTesting_Overlay

    return