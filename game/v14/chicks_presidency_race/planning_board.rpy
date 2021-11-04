init python:
    class PlanningBoardApproach:
        def __init__(self):
            # self.opinion = opinion
            # self.people = people
            # self.cost = cost

            self.tasks = []


    class PlanningBoardTask:
        def __init__(self, name, description):
            self.name = name
            self.description = description


    class PlanningBoard:
        def __init__(self, background):
            self.background = background
            self.approaches = []
            self.approach = None
            

    chloe_board = PlanningBoard("images/v14/chicks_presidency_race/planning_boards/example.png")
    
    approach_wolves = PlanningBoardApproach()
    approach_apes = PlanningBoardApproach()
    
    task1 = PlanningBoardTask("Talk to Chris about getting his full support",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse sagittis enim in mauris posuere porta. Ut vel mauris lobortis, viverra arcu non, posuere tortor. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.")

    chloe_board.approaches.append(approach_wolves)
    chloe_board.approaches.append(approach_apes)
    approach_wolves.tasks.append(task1)


screen planning_board(planning_board):
    tag planning_board
    
    add planning_board.background

    imagebutton:
        pos (435, 502)
        idle "images/v14/chicks_presidency_race/planning_boards/select_approach_left.png"
        selected_idle "images/v14/chicks_presidency_race/planning_boards/selected_approach_left.png"
        selected planning_board.approach == planning_board.approaches[0]
        action Show("planning_board_confirm", None, planning_board, planning_board.approaches[0], xypos=(963, 46))

    ## Need Right Selected Button.
    # imagebutton:
    #     pos (1324, 480)
    #     idle "images/v14/chicks_presidency_race/planning_boards/select_approach_right.png"
    #     selected_idle "images/v14/chicks_presidency_race/planning_boards/selected_approach_right.png"
    #     selected planning_board.approach == planning_board.approaches[1]
    #     action Show("planning_board_confirm", None, planning_board, planning_board.approaches[1], xypos=(43, 46))


screen planning_board_blank(xypos):
    modal True

    fixed:
        pos xypos
        xysize (914, 990)

        add "#4E91D7aa"


screen planning_board_confirm(planning_board, approach, xypos):
    modal True

    hbox:
        xalign 0.5
        ypos 933
        spacing 40

        imagebutton:
            idle "images/v14/chicks_presidency_race/planning_boards/confirm.png"
            action [SetField(planning_board, "approach", approach), Show("planning_board_blank", None, xypos), Hide("planning_board_confirm")]

        imagebutton:
            idle "images/v14/chicks_presidency_race/planning_boards/cancel.png"
            action Hide("planning_board_confirm")