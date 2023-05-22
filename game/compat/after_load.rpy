label after_load:
    stop music
    stop ambience
    stop sound

    python:
        npcs = (aaron, adam, amber, anon, aryssa, aubrey, autumn, beth, buyer, caleb, cameron, candy, charli, chloe, chris, dean, elijah, emily, emmy, evelyn, grayson, imre, iris, jenny, josh, julia, kai, kim, kourtney, lauren, lews_official, lindsey, mason, mr_lee, ms_rose, naomi, nora, parker, penelope, polly, riley, ryan, samantha, satin, sebastian, tom, trainer, wolf)

        mc.name = name
        if not mc.username:
            mc.username = name
        mc.profile_pictures = CharacterService.get_profile_pictures("mc")

        lews_official.name = "Lews Official"
        ms_rose.name = "Ms Rose"
        mr_lee.name = "Mr Lee"

        for npc in npcs:
            npc.profile_pictures = CharacterService.get_profile_pictures(npc.name.lower())

        if isinstance(_version, str) or _version < (1, 3, 3):
            if isinstance(mc.relationships, set):
                mc.relationships = {}

            #region NonPlayableCharacters
            try:
                if elijah._relationship == Relationship.MAKEFUN:
                    CharacterService.set_mood(elijah, Moods.HURT)
            except AttributeError: pass

            try:
                if evelyn._relationship == Relationship.MOVE:
                    v2_made_a_move_on_evelyn = True
            except AttributeError: pass

            try:
                if evelyn._relationship == Relationship.LIKES:
                    v6_evelyn_successful_date = True
            except AttributeError: pass

            for npc in npcs:
                try: npc.pending_text_messages
                except AttributeError: npc.pending_text_messages = []
                try: npc.text_messages
                except AttributeError: npc.text_messages = []

                try: npc.pending_simplr_messages
                except AttributeError: npc.pending_simplr_messages = []
                try: npc.simplr_messages
                except AttributeError: npc.simplr_messages = []

                try: npc.relationships
                except AttributeError: npc.relationships = {}

                try:
                    if npc._relationship == Relationship.MAD:
                        CharacterService.set_mood(npc, Moods.MAD)
                        CharacterService.set_relationship(npc, Relationship.FRIEND)
                except AttributeError: pass

                try:
                    CharacterService.set_relationship(npc, npc._relationship)
                    del npc._relationship
                except AttributeError: pass
            #endregion NonPlayableCharacters
            
            #region PlayableCharacter
            try:
                if joinwolves:
                    mc.frat = Frat.WOLVES
                else:
                    mc.frat = Frat.APES
            except NameError: mc.frat = None

            try: mc.profile_picture
            except AttributeError: mc.profile_picture = mc.profile_pictures[0]

            if not mc.profile_picture:
                mc.profile_picture = mc.profile_pictures[0]
            #endregion PlayableCharacter

            #region Messenger
            old_messenger_contacts = messenger.contacts.copy()
            messenger.contacts = []
            for contact in old_messenger_contacts:
                npc = CharacterService.get_user(contact.user)
                
                npc.text_messages = []
                for message in contact.sent_messages:
                    if hasattr(message, "message"):
                        message.content = message.message
                    elif hasattr(message, "image"):
                        message.content = message.image
                    
                    if isinstance(message, Reply):
                        npc.text_messages.append(Reply(message.content))
                    else:
                        npc.text_messages.append(Message(npc, message.content))
                messenger.contacts.append(npc)
            #endregion Messenger

            #region Kiwii
            try: kiwii.posts
            except AttributeError: kiwii.posts = []

            for post in kiwii_posts:
                kiwii_post = KiwiiService.new_post(CharacterService.get_user(post.user), post.image, post.message, post.number_likes, post.mentions)
                kiwii_post.liked = post.liked

                for comment in post.sent_comments:
                    KiwiiService.new_comment(kiwii_post, CharacterService.get_user(comment.user), comment.message, comment.number_likes, comment.mentions)
            #endregion Kiwii

        try:
            label_history = list(label_history)
        except NameError:
            label_history = []


        # Disable skip transitions
        preferences.transitions = 2

        ## PLAYABLE CHARACTERS
        if not isinstance(mc, PlayableCharacter):
            mc = PlayableCharacter()

        try: mc.username
        except AttributeError: mc.username = name

        try: mc.relationships
        except AttributeError: mc.relationships = {}

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

        for app in phone.applications:
            app.home_screen = "{}_home".format(app.name.lower())

        messenger.home_screen = "{}_home".format(messenger.name.lower())
        achievement_app.home_screen = "{}_home".format(achievement_app.name.lower())
        kiwii.home_screen = "{}_home".format(kiwii.name.lower())
        simplr_app.home_screen = "{}_home".format(simplr_app.name.lower())
        relationship_app.home_screen = "{}_home".format(relationship_app.name.lower())        

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
        show screen debug_overlay
    else:
        hide screen debug_overlay

    if mc.frat is None:
        call screen compat_frat_is_none

    $ _version = config.version
    $ renpy.block_rollback()
    return