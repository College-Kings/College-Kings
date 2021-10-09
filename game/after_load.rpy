python early:
    import os

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
        contact_Lindsey.profile_picture = "images/phone/messages/profile_pictures/lindseyprofilepic.webp"
        contact_Emily.profile_picture = "images/phone/messages/profile_pictures/emilyprofilepic.webp"
        contact_Lauren.profile_picture = "images/phone/messages/profile_pictures/laurenprofilepic.webp"
        contact_Julia.profile_picture = "images/phone/messages/profile_pictures/juliaprofilepic.webp"
        contact_Ryan.profile_picture = "images/phone/messages/profile_pictures/ryanprofilepic.webp"
        contact_Josh.profile_picture = "images/phone/messages/profile_pictures/joshprofilepic.webp"
        contact_Aubrey.profile_picture = "images/phone/messages/profile_pictures/aubreyprofilepic.webp"
        contact_Chloe.profile_picture = "images/phone/messages/profile_pictures/chloeprofilepic.webp"
        contact_Evelyn.profile_picture = "images/phone/messages/profile_pictures/evelynprofilepic.webp"
        contact_Amber.profile_picture = "images/phone/messages/profile_pictures/amberprofilepic.webp"
        contact_Penelope.profile_picture = "images/phone/messages/profile_pictures/penelopeprofilepic.webp"
        contact_Riley.profile_picture = "images/phone/messages/profile_pictures/rileyprofilepic.webp"
        contact_Autumn.profile_picture = "images/phone/messages/profile_pictures/autumnprofilepic.webp"
        contact_Imre.profile_picture = "images/phone/messages/profile_pictures/imreprofilepic.webp"
        contact_Sebastian.profile_picture = "images/phone/messages/profile_pictures/sebastianprofilepicture.webp"
        contact_Grayson.profile_picture = "images/phone/messages/profile_pictures/graysonprofilepicture.webp"
        contact_Lindsey.profile_picture = "images/phone/messages/profile_pictures/lindseyprofilepic.webp"
        contact_Jenny.profile_picture = "images/phone/messages/profile_pictures/jennyprofilepicture.webp"
        contact_Nora.profile_picture = "images/phone/messages/profile_pictures/noraprofilepicture.webp"

        if contact_Grayson not in contacts:
            contacts.append(contact_Grayson)
        if contact_Lindsey not in contacts:
            contacts.append(contact_Lindsey)

        for contact in contacts:
            try: contact.pendingMessages
            except AttributeError: contact.pendingMessages = []

            try: contact.sentMessages
            except AttributeError: contact.sentMessages = []

            try: contact.profile_picture
            except AttributeError: contact.profile_picture = "images/phone/messages/profile_pictures/chloeprofilepic.webp"

            try: contact.profilePicture = "images/phone/messages/profile_pictures/chloeprofilepic.webp"
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

        # Simplr Contacts
        simplr_Beth.profile_picture = "images/phone/simplr/contacts/bethProfilePicture.webp"
        simplr_Iris.profile_picture = "images/phone/simplr/contacts/irisProfilePicture.webp"
        simplr_Samantha.profile_picture = "images/phone/simplr/contacts/samanthaProfilePicture.webp"
        simplr_Emmy.profile_picture = "images/phone/simplr/contacts/emmyProfilePicture.webp"

        simplr_Beth.profile_picture_large = "images/phone/simplr/contacts/bethProfilePictureLarge.webp"
        simplr_Iris.profile_picture_large = "images/phone/simplr/contacts/irisProfilePictureLarge.webp"
        simplr_Samantha.profile_picture_large = "images/phone/simplr/contacts/samanthaProfilePictureLarge.webp"
        simplr_Emmy.profile_picture_large = "images/phone/simplr/contacts/emmyProfilePictureLarge.webp"

        for contact in simplr_pendingContacts + simplr_contacts:
            try: contact.condition
            except AttributeError: contact.condition = True

            try: contact.profile_picture
            except AttributeError: contact.profile_picture = "images/phone/simplr/contacts/bethProfilePicture.webp"

        
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

        # v12 Renpy Fixes:
        try: chloe
        except NameError: chloe = CustomCharacter("Chloe")
        try: amber
        except NameError: amber = CustomCharacter("Amber")
        try: penelope
        except NameError: penelope = CustomCharacter("Penelope")
        try: riley
        except NameError: riley = CustomCharacter("Riley")
        try: lindsey
        except NameError: lindsey = CustomCharacter("Lindsey")
        try: lauren
        except NameError: lauren = CustomCharacter("Lauren")
        try: samantha
        except NameError: samantha = CustomCharacter("Samantha")
        try: emily
        except NameError: emily = CustomCharacter("Emily")
        try: ms_rose
        except NameError: ms_rose = CustomCharacter("Ms Rose")
        try: nora
        except NameError: nora = CustomCharacter("Nora")
        try: aubrey
        except NameError: aubrey = CustomCharacter("Aubrey")
        try: ryan
        except NameError: ryan = CustomCharacter("Ryan")
        try: imre
        except NameError: imre = CustomCharacter("Imre")
        try: chris
        except NameError: chris = CustomCharacter("Chris")
        try: charli
        except NameError: charli = CustomCharacter("Charli")
        try: cameron
        except NameError: cameron = CustomCharacter("Cameron")
        try: josh
        except NameError: josh = CustomCharacter("Josh")

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

        try: v7_seencrowning
        except NameError: v7_seencrowning = False
        try: v7_emily_bowling
        except NameError: v7_emily_bowling = False
        try: v11_samantha_spa
        except NameError: v11_samantha_spa = False
        try: v11_lauren_ily
        except NameError: v11_lauren_ily = False
        try: v11_underground_rose
        except NameError: v11_underground_rose = False
        try: v12_told_chloe
        except NameError: v12_told_chloe = False
        try: v12_kiss_riley
        except NameError: v12_kiss_riley = False
        try: v12_amber_tell_riley
        except NameError: v12_amber_tell_riley = False
        try: v12_fight_win
        except NameError: v12_fight_win = False
        try: v12_chase_robber
        except NameError: v12_chase_robber = False
        try: v12s7_seenList
        except NameError: v12s7_seenList = []
        try: v12s7_killList
        except NameError: v12s7_killList = set()
        try: v12_msrose_sex
        except NameError: v12_msrose_sex = False
        try: v11_lindsey_run
        except NameError: v11_lindsey_run = False
        try: v12_help_chris
        except NameError: v12_help_chris = 0

        try: v12s7_lauren
        except NameError: v12s7_lauren = False
        try: v12s7_emily
        except NameError: v12s7_emily = False
        try: v12s7_emily2
        except NameError: v12s7_emily2 = False
        try: v12s7_samantha
        except NameError: v12s7_samantha = False
        try: v12s7_samantha2
        except NameError: v12s7_samantha2 = False
        try: v12s7_msrose
        except NameError: v12s7_msrose = False
        try: v12s7_penelope
        except NameError: v12s7_penelope = False
        try: v12s7_chris
        except NameError: v12s7_chris = False
        try: v12s7_imre
        except NameError: v12s7_imre = False
        try: v12s7_imre2
        except NameError: v12s7_imre2 = False
        try: v12s7_lindsey
        except NameError: v12s7_lindsey = False
        try: v12s7_lindsey2
        except NameError: v12s7_lindsey2 = False
        try: v12s7_josh
        except NameError: v12s7_josh = False
        try: v12s7_josh2
        except NameError: v12s7_josh2 = False
        try: v12s7_chloe
        except NameError: v12s7_chloe = False
        try: v12s7_riley
        except NameError: v12s7_riley = False
        try: v12s7_riley_moved
        except NameError: v12s7_riley_moved = False
        try: v12s7_riley2
        except NameError: v12s7_riley2 = False
        try: v12s7_riley3
        except NameError: v12s7_riley3 = False
        try: v12s7_mrlee
        except NameError: v12s7_mrlee = False
        try: v12s7_cameron
        except NameError: v12s7_cameron = False
        try: v12s7_ryan
        except NameError: v12s7_ryan = False
        try: v12s7_amber
        except NameError: v12s7_amber = False
        try: v12s7_aubrey
        except NameError: v12s7_aubrey = False
        try: v12s7_aubrey2
        except NameError: v12s7_aubrey2 = False
        try: v12s7_nora
        except NameError: v12s7_nora = False
        try: v12s7_charli
        except NameError: v12s7_charli = False

        try: v12s7_lindsey_moved
        except NameError: v12s7_lindsey_moved = False
        try: v12s7_aubrey_moved
        except NameError: v12s7_aubrey_moved = False
        try: v12_lindsey_sex
        except NameError: v12_lindsey_sex = False
        try: v12s18_bottlespin_played
        except NameError: v12s18_bottlespin_played = False
        try: v12s18_fmk_played
        except NameError: v12s18_fmk_played = False
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
        try: v12s23a_poolsex
        except NameError: v12s23a_poolsex = False
        try: v12s23a_beatcameron
        except NameError: v12s23a_beatcameron = False
        try: v12_nora_sex
        except NameError: v12_nora_sex = False
        try: v12_nora_points
        except NameError: v12_nora_points = 0
        try: supported_nora
        except NameError: supported_nora = False
        try: v12_call_cameron
        except NameError: v12_call_cameron = False
        try: v12s33_door1
        except NameError: v12s33_door1 = False
        try: v12_call_cameron
        except NameError: v12_call_cameron = False
        try: v12s33_door2
        except NameError: v12s33_door2 = False
        try: v12s33_door3
        except NameError: v12s33_door3 = False
        try: v12s24_emmymatch
        except NameError: v12s24_emmymatch = False


        #v11 variables
        try: laurenLike
        except NameError: laurenLike = 0
        try: v11_pen_goes_europe
        except NameError: v11_pen_goes_europe = False
        try: v11s1_riley1
        except NameError: v11s1_riley1 = False
        try: v11s1_mrrose1
        except NameError: v11s1_mrrose1 = False
        try: v11s1_jenny1
        except NameError: v11s1_jenny1 = False
        try: v11s1_delib1
        except NameError: v11s1_delib1 = False
        try: v11s1_courtpoints
        except NameError: v11s1_courtpoints = 0
        try: sammad
        except NameError: sammad = False
        try: v11_invite_sam_europe
        except NameError: v11_invite_sam_europe = False
        try: v11_talk_with_emily
        except NameError: v11_talk_with_emily = False
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
        try: v11_pranked_seb
        except NameError: v11_pranked_seb = False
        try: v11_aubrey_sex
        except NameError: v11_aubrey_sex = False
        try: v11_want_date_aubrey
        except NameError: v11_want_date_aubrey = False
        try: v11_riley_roomate
        except NameError: v11_riley_roomate = False
        try: v11_msrose_kiss
        except NameError: v11_msrose_kiss = False
        try: v11s23_chris1
        except NameError: v11s23_chris1 = False
        try: v11s23_riley1
        except NameError: v11s23_riley1 = False
        try: v11s23_mrlee1
        except NameError: v11s23_mrlee1 = False
        try: v11s23_penelope1
        except NameError: v11s23_penelope1 = False
        try: v11s25_beer
        except NameError: v11s25_beer = True
        try: v11_bartender_have_gf
        except NameError: v11_bartender_have_gf = False
        try: msrosers
        except NameError: msrosers = False
        try: v11_madison_ex
        except NameError: v11_madison_ex = False
        try: v11_ex_drugs
        except NameError: v11_ex_drugs = False
        try: v11_ex_father
        except NameError: v11_ex_father = False 
        try: v11_solo_question
        except NameError: v11_solo_question = False
        try: v11_apology_kiss
        except NameError: v11_apology_kiss = False
        try: v11_kiss_nora
        except NameError: v11_kiss_nora = False
        try: v11_nora_bra_white
        except NameError: v11_nora_bra_white = False
        try: v11_told_aubrey
        except NameError: v11_told_aubrey = False
        try: v11_chloe_sex
        except NameError: v11_chloe_sex = False
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
        try: v11_rileysex
        except NameError: v11_rileysex = False
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
        try: v13_lauren_hospital
        except NameError: v13_lauren_hospital = False
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
        try: v13_help_lindsey
        except NameError: v13_help_lindsey = False
        try: emmyrs
        except NameError: emmyrs = False
        try: kourtneyrs
        except NameError: kourtneyrs = False
        try: aryssars
        except NameError: aryssars = False
        try: v13_told_emmy_no_kids_for_me
        except NameError: v13_told_emmy_no_kids_for_me = False
        try: v13_told_emmy_city
        except NameError: v13_told_emmy_city = False
        try: v13_imre_disloyal
        except NameError: v13_imre_disloyal = False
        try: v13s40_chloe_turned_on
        except NameError: v13s40_chloe_turned_on = 0
        try: v13_perfume
        except NameError: v13_perfume = False
        try: v13_hugged_aubrey
        except NameError: v13_hugged_aubrey = False
        try: v13s9_go_to_concert
        except NameError: v13s9_go_to_concert = False
        try: v13s41_lindsey_points
        except NameError: v13s41_lindsey_points = 0
        try: v13_rileysex
        except NameError: v13_rileysex = False
        try: v13_emmysex
        except NameError: v13_emmysex = False
        try: v13_chloesex
        except NameError: v13_chloesex = False
        try: v13_emilysex
        except NameError: v13_emilysex = False
        try: v13s20_bleach_suitcase
        except NameError: v13s20_bleach_suitcase = False
        try: v13s20_frbleach
        except NameError: v13s20_frbleach = False
        try: v13s20_frcloset
        except NameError: v13s20_frcloset = False
        try: v13s20_frbrush
        except NameError: v13s20_frbrush = False
        try: v13s37_frnora
        except NameError: v13s37_frnora = False
        try: v13s37_frchris
        except NameError: v13s37_frchris = False
        try: v13s40_neckpoint
        except NameError: v13s40_neckpoint = False
        try: v13s40_chestpoint
        except NameError: v13s40_chestpoint = False
        try: v13s40_backpoint
        except NameError: v13s40_backpoint = False
        try: v13s40_shoulderpoint
        except NameError: v13s40_shoulderpoint = False
        try: laurenrs_v11aubrey
        except NameError: laurenrs_v11aubrey = False
        try: v13s40fromgame
        except NameError: v13s40fromgame = False
        try: v13_aubrey_vote
        except NameError: v13_aubrey_vote = "na"


    show no_hard_feelings at achievementShow
    $ achievementAtList = renpy.get_at_list("no_hard_feelings")
    hide no_hard_feelings

    show screen phoneIcon
    hide screen getaccess

    if config.developer:
        show screen bugTesting_Overlay

    return