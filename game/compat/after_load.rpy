label after_load:
    stop music

    python:
        if isinstance(_version, str):
            _verison = _version.split(' ')[0]
            _verison = _verison.split(".")
            if _verison[-1].endswith("s"):
                _verison[-1] = _verison[-1][:-1]
            _version = tuple(int(i) for i in _verison)

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
            "images/phone/kiwii/Posts/v7/lapost1.webp": "ck1_v7_lauren_post",
            "images/phone/kiwii/Posts/v7/aupost1.webp": "ck1_v7_aubrey_post",
            "images/phone/kiwii/Posts/v7/empost1.webp": "ck1_v7_emily_post",
            "images/phone/kiwii/Posts/v7/chpost1.webp": "ck1_v7_chris_post",
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
            "Charli": Charlie,
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
        
        if _version < (1, 4, 0):
            if isinstance(kiwii, Application):
                kiwii = Kiwii()

            for post in kiwii.posts:
                if post.image in kiwii_post_map:
                    post.image = kiwii_post_map[post.image]

            old_mc_vars = mc.__dict__.copy()
            mc = MainCharacter()
            mc.relationships = old_mc_vars["relationships"]
            mc.money = old_mc_vars["money"]

            old_inventory = old_mc_vars["inventory"]
            if isinstance(old_inventory, Inventory):
                mc.inventory = list(set(old_inventory.items))
            else:
                mc.inventory = list(set(old_inventory))

            mc.frat = old_mc_vars["frat"]

            for npc_name in npc_map:
                old_npc = getattr(store, npc_name.lower().replace(' ', '_'))
                old_npc_vars = old_npc.__dict__.copy()
                npc = npc_map[npc_name]()
                setattr(store, npc_name.lower().replace(' ', '_'), npc)

                try:
                    npc.relationships = old_npc_vars["relationships"]
                except KeyError:
                    npc.relationships[mc] = old_npc_vars.get("_relationship", Relationship.FRIEND) 

                npc.mood = old_npc.mood
                npc.pending_text_messages = old_npc_vars.get("pending_text_messages", [])
                npc.text_messages = old_npc_vars.get("text_messages", [])
                npc.pending_simplr_messages = old_npc_vars.get("pending_simplr_messages", [])
                npc.simplr_messages = old_npc_vars.get("simplr_messages", [])
                npc.points = old_npc_vars.get("points", 0)
                
                if npc.text_messages:
                    messenger.contacts.append(npc)

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