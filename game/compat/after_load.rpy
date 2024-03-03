init python:
    def get_version(version: Union[str, list[str]]) -> tuple[int, int, int]:
        if isinstance(version, str):
            version = version.split(' ')[0]
            version = version.split(".")
            if version[-1].endswith("s"):
                version[-1] = version[-1][:-1]
        version = tuple(int(i) for i in version)
        return version

label after_load:
    stop music

    python:
        kiwii_post_map = {
            "images/phone/kiwii/Posts/v11/v11_autumn_kiwii.webp": "ck1_v11_autumn_post",
            "images/phone/kiwii/Posts/v11/sebnaked.webp": "ck1_v11_sebastian_naked",
            "images/phone/kiwii/Posts/v11/v11_chloemcselfie.webp": "ck1_v11_chloe_mc_selfie",
            "images/phone/kiwii/Posts/v11/v11_caleb.webp": "ck1_v11_caleb_post",
            "images/phone/kiwii/Posts/v11/v11_imrebunny.webp": "ck1_v11_imre_bunny",
            "images/phone/kiwii/Posts/v11/v11s38_amber_kiwii.webp": "ck1_v11_amber_post",
            "images/phone/kiwii/Posts/v12/impost1.webp": "ck1_v12_imre_post",
            "images/phone/kiwii/Posts/v12/lindsey_aubrey_pjs.webp": "ck1_v12_lindsey_aubrey_pjs",
            "images/phone/kiwii/Posts/v12/imre_raccoon.webp": "ck1_v12_imre_raccoon",
            "images/phone/kiwii/Posts/v12/roastedape.webp": "ck1_v12_roasted_ape",
            "images/phone/kiwii/Posts/v12/v12s32_15g.webp": "ck1_v12_lews_post_1",
            "images/phone/kiwii/Posts/v12/v12s32_24.webp": "ck1_v12_lews_post_2",
            "images/phone/kiwii/Posts/v12/v12s32_33.webp": "ck1_v12_lews_post_3",
            "images/phone/kiwii/Posts/v13/aubrey_beach.webp": "ck1_v13_aubrey_beach",
            "images/phone/kiwii/Posts/v7/clpost1.webp": "ck1_v7_chloe_post",
            "images/phone/kiwii/posts/v7/clpost1.webp": "ck1_v7_chloe_post",
            "images/phone/kiwii/Posts/v7/lapost1.webp": "ck1_v7_lauren_post",
            "images/phone/kiwii/posts/v7/lapost1.webp": "ck1_v7_lauren_post",
            "images/phone/kiwii/Posts/v7/aupost1.webp": "ck1_v7_aubrey_post",
            "images/phone/kiwii/posts/v7/aupost1.webp": "ck1_v7_aubrey_post",
            "images/phone/kiwii/Posts/v7/empost1.webp": "ck1_v7_emily_post",
            "images/phone/kiwii/Posts/v7/chpost1.webp": "ck1_v7_chris_post",
            "images/phone/kiwii/posts/v7/chpost1.webp": "ck1_v7_chris_post",
            "images/phone/kiwii/Posts/v8/grpost1.webp": "ck1_v8_grayson_post",
            "images/phone/kiwii/Posts/v8/chlaubpost1.webp": "ck1_v8_chloe_aubrey_post",
            "images/phone/kiwii/Posts/v8/laurosepost1.webp": "ck1_v8_lauren_rose_post",
            "images/phone/kiwii/Posts/v8/riclothpost1.webp": "ck1_v8_riley_post",
            "images/phone/kiwii/Posts/v8/mcpost1w.webp": "ck1_v8_mc_wolves_post",
            "images/phone/kiwii/Posts/v8/mcpost1a.webp": "ck1_v8_mc_apes_post",
            "images/phone/kiwii/Posts/v8/red_square.webp": "ck1_v8_red_square",
        }

        npc_map = {
            "Aaron": Aaron,
            "Adam": Adam,
            "Amber": Amber,
            "Anon": Anon,
            "Aryssa": Aryssa,
            "Aubrey": Aubrey,
            "Autumn": Autumn,
            "Beth": Beth,
            "Buyer": Buyer,
            "Caleb": Caleb,
            "Cameron": Cameron,
            "Candy": Candy,            
            "Charli": Charli,
            "Chloe": Chloe,
            "Chris": Chris,
            "Dean": Dean,
            "Elijah": Elijah,
            "Emily": Emily,
            "Emmy": Emmy,
            "Evelyn": Evelyn,
            "Grayson": Grayson,
            "Imre": Imre,
            "Iris": Iris,
            "Jenny": Jenny,
            "Josh": Josh,
            "Julia": Julia,
            "Kai": Kai,
            "Kim": Kim,
            "Kourtney": Kourtney,
            "Lauren": Lauren,
            "Lews Official": LewsOfficial,
            "Lindsey": Lindsey,
            "Mason": Mason,
            "Mr Lee": MrLee,
            "Ms Rose": MsRose,
            "Naomi": Naomi,
            "Nora": Nora,
            "Parker": Parker,
            "Penelope": Penelope,
            "Polly": Polly,
            "Riley": Riley,
            "Ryan": Ryan,
            "Samantha": Samantha,
            "Satin": Satin,
            "Sebastian": Sebastian,
            "SVC Housing Officer": SVCHousingOfficer,
            "Tom": Tom,
            "Trainer": Trainer,
            "Wolf": Wolf,
        }
        
        version = get_version(store.__dict__["_version"])
        if version > (2, 0, 0):
            version = (0, 0, 0)

        if version < (1, 4, 0):
            if isinstance(kiwii, Application):
                old_kiwii_vars = kiwii.__dict__.copy()
                kiwii = Kiwii()

            if isinstance(kiwii, bool):
                old_kiwii_vars = kiwiiApp.__dict__.copy()
                kiwii = Kiwii()

            if kiwii.posts:
                for post in kiwii.posts:
                    if post.image in kiwii_post_map:
                        post.image = kiwii_post_map[post.image]

            if isinstance(messenger, Application):
                old_messenger_vars = messenger.__dict__.copy()
                messenger = Messenger()

            old_mc_vars = mc.__dict__.copy()
            mc = MainCharacter()
            mc.relationships = old_mc_vars.get("relationships", {})
            mc.money = old_mc_vars["money"]

            try:
                old_inventory = old_mc_vars["inventory"]
                if isinstance(old_inventory, Inventory):
                    mc.inventory = list(set(old_inventory.items))
                else:
                    mc.inventory = list(set(old_inventory))
            except KeyError: pass

            try:
                if joinwolves:
                    mc.frat = Frat.WOLVES
                else:
                    mc.frat = Frat.APES
            except NameError:
                mc.frat = old_mc_vars["frat"]

            for npc_name in npc_map:
                old_npc = CharacterService.get_user(npc_name)
                old_npc_vars = old_npc.__dict__.copy()
                npc = npc_map[npc_name]()
                setattr(store, npc_name.lower().replace(' ', '_'), npc)

                try:
                    npc.relationships = old_npc_vars["relationships"]
                except KeyError:
                    npc.relationships[mc] = old_npc_vars.get("_relationship", Relationship.FRIEND)

                if npc.relationships.setdefault(mc, Relationship.FRIEND) == Relationship.FRIEND:
                    try:
                        if getattr(store, f"{npc_name.lower().replace(' ', '')}rs"):
                            npc.relationships[mc] = Relationship.FWB
                    except AttributeError: pass
                
                mc.relationships[npc] = npc.relationships[mc]

                npc.mood = old_npc.mood
                npc.pending_text_messages = old_npc_vars.get("pending_text_messages", [])
                npc.text_messages = old_npc_vars.get("text_messages", [])
                npc.pending_simplr_messages = old_npc_vars.get("pending_simplr_messages", [])
                npc.simplr_messages = old_npc_vars.get("simplr_messages", [])
                npc.points = old_npc_vars.get("points", 0)

                messenger.contacts = []
                if npc.text_messages:
                    messenger.contacts.append(npc)

            for contact in old_messenger_vars.get("contacts", []):
                npc = CharacterService.get_user(contact.name)
                if hasattr(contact, "messages"):
                    npc.text_messages = contact.messages
                if hasattr(contact, "sentMessages"):
                    npc.text_messages = contact.sentMessages
                if hasattr(contact, "pending_messages"):
                    npc.pending_text_messages = contact.pending_messages
                if hasattr(contact, "pending_text_messages"):
                    npc.pending_text_messages = contact.pending_text_messages

                messenger.contacts.append(npc)

            for npc in messenger.contacts:
                npc_text_messages = npc.text_messages.copy()
                npc.text_messages = []
                seen = set()
                for message in npc_text_messages:
                    old_message_vars = message.__dict__.copy()
                    content = old_message_vars.get("msg") or old_message_vars.get("message") or old_message_vars.get("image")
                    if content in seen or content is None:
                        continue
                    seen.add(content)

                    if isinstance(message, Reply):
                        npc.text_messages.append(Reply(old_message_vars.get("content") or old_message_vars.get("message")))
                    elif isinstance(message, ImgReply):
                        npc.text_messages.append(Reply(old_message_vars["image"]))
                    else:
                        contact = old_message_vars.get("contact") or old_message_vars.get("npc")
                        npc.text_messages.append(Message(CharacterService.get_user(contact.name), content))
                        if old_message_vars.get("reply"):
                            npc.text_messages.append(Reply(old_message_vars["reply"]))

            if hasattr(store, "kiwiiPosts"):
                for post in kiwiiPosts:
                    post_image = post.__dict__.get("image") or post.__dict__.get("img")
                    kiwii.posts.append(KiwiiPost(CharacterService.get_user(post.user), kiwii_post_map[post_image], post.message, [CharacterService.get_user(mention) for mention in post.mentions], post.numberLikes))
                del kiwiiPosts

        if version < (1, 4, 4):
            old_vars = charli.__dict__.copy()
            charli = Charli()
            charli.relationships = old_vars.get("relationships", {})
            charli.pending_text_messages = old_vars.get("pending_text_messages", [])
            charli.text_messages = old_vars.get("text_messages", [])

        if version < (1, 4, 5):
            mc_relationships = tuple(mc.relationships.items())
            mc.relationships = {CharacterService.get_user(npc): rel for npc, rel in mc_relationships}

            for npc, rel in mc.relationships.items():
                npc.relationships = {mc: rel}

        if version < (1, 4, 9):
            achievements_app = Achievements()
            calendar = Calendar()
            relationship_app = Relationships()
            reputation_app = ReputationApp()
            tracker = Tracker()

            phone.applications = [messenger, achievements_app, relationship_app, kiwii, reputation_app, simplr_app, tracker, calendar]

    show screen phone_icon
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