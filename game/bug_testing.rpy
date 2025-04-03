init python:
    def debug_output():
        if not config.developer:
            print("Debug functions are only enabled in the development enviroment")
            return

        print(reputation.components)
        print()

        print(f"Frat : {mc.frat}")
        print()
        
        for npc in (emily, aubrey, lauren, riley, nora, ms_rose, chloe, penelope, amber, samantha, lindsey):
            print(f"{npc.name} : {npc._relationship[mc]}")


screen debug_overlay():
    zorder 1000

    if config.developer:
        python:
            sorted_components = [k for k, v in sorted(reputation.components.items(), key=helper_sorted_by_value, reverse=True)]
            
            points_to_popular = {
                RepComponent.BRO: reputation.components[RepComponent.BOYFRIEND] - reputation.components[RepComponent.BRO],
                RepComponent.TROUBLEMAKER: reputation.components[RepComponent.BOYFRIEND] - reputation.components[RepComponent.TROUBLEMAKER],
            }
            points_to_loyal = {
                RepComponent.BRO: reputation.components[RepComponent.TROUBLEMAKER] - reputation.components[RepComponent.BRO],
                RepComponent.BOYFRIEND: reputation.components[RepComponent.TROUBLEMAKER] - reputation.components[RepComponent.BOYFRIEND],
            }
            points_to_confident = {
                RepComponent.BOYFRIEND: reputation.components[RepComponent.BRO] - reputation.components[RepComponent.BOYFRIEND],
                RepComponent.TROUBLEMAKER: reputation.components[RepComponent.BRO] - reputation.components[RepComponent.TROUBLEMAKER],
            }

        vbox:
            pos (5, 20)

            text str(renpy.get_filename_line()) color "#0f0"
            text "Stack Depth: {}".format(renpy.call_stack_depth())
            # text str(renpy.scene_lists().get_all_displayables()) substitute False
            # text str(renpy.get_screen("phone"))

        vbox:
            xalign 1.0
            xoffset -20
            ypos 250

            if reputation() != Reputations.POPULAR:
                text "Points to Popular: BRO: {}, TM: {}".format(
                    points_to_popular[RepComponent.BRO] if points_to_popular[RepComponent.BRO] > 0 else 0,
                    points_to_popular[RepComponent.TROUBLEMAKER] if points_to_popular[RepComponent.TROUBLEMAKER] > 0 else 0
                ):
                    outlines [ (2, "#000000") ]
            if reputation() != Reputations.LOYAL:
                text "Points to Loyal: BRO: {}, BF: {}".format(
                    points_to_loyal[RepComponent.BRO] if points_to_loyal[RepComponent.BRO] > 0 else 0,
                    points_to_loyal[RepComponent.BOYFRIEND] if points_to_loyal[RepComponent.BOYFRIEND] > 0 else 0
                ):
                    outlines [ (2, "#000000") ]
            if reputation() != Reputations.CONFIDENT:
                text "Points to Confident: BF: {}, TM: {}".format(
                    points_to_confident[RepComponent.BOYFRIEND] if points_to_loyal[RepComponent.BOYFRIEND] > 0 else 0,
                    points_to_confident[RepComponent.TROUBLEMAKER] if points_to_confident[RepComponent.TROUBLEMAKER] > 0 else 0
                ):
                    outlines [ (2, "#000000") ]


screen bug_testing_overlay():
    use debug_overlay