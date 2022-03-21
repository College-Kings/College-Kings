# SCENE 72: Student Newspaper Reveal
# Locations: SVC School Classrom
# Characters: MC (Outfit: 5)
# Time: Morning


label v16s72:

    scene v16s72_1 # TPP. MC (slight smile, mouth is closed, looking at the SVC classroom door) walks along the hallway, As he's passing the SVC Times door, he sees a stack of newspapers in the hallway, beside the door
    with dissolve

    u "(What's this? The first edition of the newspaper?)"

    scene v16s72_1a # TPP. MC (slight smile, mouth is closed, looking at the newspapers next to the SVC classroom door)approaches the stack of newspapers. The cover is unseen as a white sheet of paper is on the top of the stack, with the text written out in black marker pen: SVC TIMES 1st Edition. For distribution on Monday. DO NOT TOUCH!-
    with dissolve

    u "(Haha, okay, Elijah. I bet a sneak peek won't hurt...)"

    scene v16s72_1b # TPP. MC (slight smile, mouth is closed, he is holding a newspaper with the text written out in black marker pen: SVC TIMES 1st Edition. For distribution on Monday. DO NOT TOUCH!-
    with dissolve


    menu:

        "Take a peek":

            # -We enter the newspaper UI, where the player will see the front cover and can read the newspaper articles-

            scene v16s72_1a
            with dissolve

            if # -if MC helped Chloe with the cover design, we see the chosen design

                scene v16s72_2 # FPP. (Image should already be rendered, double check with Mozzart) Image is (Photo one: mid-shot of Chloe smiling and waving a "Vote for Chloe flag", wearing a Chicks t-shirt.) With Headline one: Great leadership starts with a beautiful smile!
                with dissolve

            if # -if MC helped Chloe with the cover design, we see the chosen design

                scene v16s72_2a # FPP. (Image should already be rendered, double check with Mozzart) Image is (Photo one: mid-shot of Chloe smiling and waving a "Vote for Chloe flag", wearing a Chicks t-shirt.) Headline two: I'm ready to dive in, I just need your vote!)
                with dissolve

            elif # -if MC helped Chloe with the cover design, we see the chosen design

                scene v16s72_2b # FPP. (Image should already be rendered, double check with Mozzart) Image is (Photo two: Chloe in a white bikini with white toenails, posing by Jenny's lagoon from v14, hand on hip.) With Headline one: Great leadership starts with a beautiful smile!
                with dissolve

            elif # -if MC helped Chloe with the cover design, we see the chosen design

                scene v16s72_2c # FPP. (Image should already be rendered, double check with Mozzart) Image is (Photo two: Chloe in a white bikini with white toenails, posing by Jenny's lagoon from v14, hand on hip.) Headline two: I'm ready to dive in, I just need your vote!)
                with dissolve

            elif # -if MC did not help Chloe with the cover design, the default design shows a Chloe vs Lindsey image with the two girls facing each other and a big VS between them, like a boxing/MMA type thing. And the headline, Battle of the Chicks!-

                scene v16s72_3 # FPP. (Image should already be rendered, double check with Mozzart) The default design shows a Chloe vs Lindsey image with the two girls facing each other and a big VS between them, like a boxing/MMA type thing. And the headline, Battle of the Chicks!-
                with dissolve

            elif v16s28_lindsey_pb_intereview_polly_choice and #Written by Elijah: # -if MC helped Lindsey with Newspaper interview, the player will be able to read the article. Depending on MC's phase three choices and Scene 60, the article will either be written by Elijah or Riley and will be a positive or negative article. Also, if on this path, the player should be forced to see the interview article before being able to exit (to allow for MC dialogue after UI closes) (if possible)-

                scene v16s72_4
                with dissolve

            elif v16s28_lindsey_pb_intereview_polly_choice and #Written by Riley: # -if MC helped Lindsey with Newspaper interview, the player will be able to read the article. Depending on MC's phase three choices and Scene 60, the article will either be written by Elijah or Riley and will be a positive or negative article. Also, if on this path, the player should be forced to see the interview article before being able to exit (to allow for MC dialogue after UI closes) (if possible)-

                scene v16s72_4
                with dissolve

            # -We exit the UI when the player chooses to finish reading the newspaper-

            scene v16s72_5 # FPP. Close up shot of MC (slight smile, mouth is closed, looking at the newspaper in his hand)
            with dissolve

            u "(Well, shit. Not bad... Thanks, Elijah!)"

            scene v16s72_1c # TPP. MC (slight smile, mouth is closed, is putting the newspaper with the text written out in black marker pen: SVC TIMES 1st Edition. For distribution on Monday. DO NOT TOUCH! back onto the stack of other newspapers
            with dissolve

            if # -if MC helped Chloe with the cover design and chose a Chloe image (LindseyPopularity MINUS 2)

                scene v16s72_5a # FPP. Close up shot of MC (full smile, mouth is closed)
                with dissolve

                u "(I chose well, Chloe looks great on the cover!)"

            elif # -if MC helped Chloe with the cover design and chose a Lindsey image (LindseyPopularity MINUS 4)

                scene v16s72_5b # FPP. Close up shot of MC (smirking, mouth is closed)
                with dissolve

                u "(I can't wait to see the drama unfold when everyone sees that awful photo of Lindsey, haha!)"

            elif # -if MC helped Lindsey with interview and it was a positive article (LindseyPopularity PLUS 4)

                scene v16s72_5a
                with dissolve

                u "(Lindsey's interview was so good. She'll get plenty of votes out of that!)"

            elif # -if MC helped Lindsey with interview and it was a negative article (LindseyPopularity MINUS 2)

                scene v16s72_5c # FPP. Close up shot of MC (no expression, mouth is closed)
                with dissolve

                u "*Sighs* (I'd like to blame it on the editor, but to be honest, Lindsey just did a horrible job in the interview...)"

        "Don't look":

            scene v16s72_5
            with dissolve

            u "(Hmm, on second thought, I'll wait until the official release date.)"

    # -Regardless-

    scene v16s72_1d # TPP. MC (slight smile, mouth is closed) continues walking along the school hallway
    with dissolve

    jump v16s73 # -Transition to Scene 73-