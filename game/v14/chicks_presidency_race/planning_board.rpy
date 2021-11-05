init python:
    class PlanningBoardApproach:
        def __init__(self):
            self.tasks = []


    class PlanningBoardTask:
        def __init__(self, name, opinion, people, cost):
            self.name = name
            self.opinion = opinion
            self.people = people
            self.cost = cost

            self.completed = False


    class PlanningBoard:
        def __init__(self, background):
            self.background = background

            self.approaches = []
            self.approach = None
            self.selected_task = None

        def add_approach(self):
            self.approaches.append(PlanningBoardApproach())

        def add_task(self, approach_index, name, opinion, people, cost):
            approach = self.approaches[approach_index]
            approach.tasks.append(PlanningBoardTask(name, opinion, people, cost))

        def add_subtask(self, approach_index, name, opinion, people, cost):
            approach = self.approaches[approach_index]
            if isinstance(approach.tasks[-1], list):
                approach.tasks[-1].append(PlanningBoardTask(name, opinion, people, cost))
            else:
                approach.tasks.append([PlanningBoardTask(name, opinion, people, cost)])


screen planning_board(planning_board):
    tag planning_board
    zorder 100
    modal True
    
    add planning_board.background

    # Left Side
    $ approach = planning_board.approaches[0]
    imagebutton:
        pos (435, 502)
        idle "images/v14/chicks_presidency_race/planning_boards/select_approach_left.png"
        selected_idle "images/v14/chicks_presidency_race/planning_boards/selected_approach_left.png"
        selected planning_board.approach == planning_board.approaches[0]
        action Show("planning_board_confirm_approach", None, planning_board, planning_board.approaches[0], xypos=(963, 46))

    vbox:
        pos (130, 661)
        spacing 30
        style_prefix "task"
        xmaximum 770

        for number, task in enumerate(approach.tasks, start=1):
            hbox:
                spacing 20
                text "{}.".format(number) yalign 0.5

                if isinstance(task, list):
                    vbox:
                        spacing 10

                        for alphabet, subtask in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", task):
                            hbox:
                                spacing 15

                                text "{})".format(alphabet) yalign 0.5
                                textbutton subtask.name:
                                    sensitive planning_board.approach is not None
                                    selected planning_board.selected_task == subtask
                                    hovered Show("planning_board_task_desc", None, subtask)
                                    unhovered Hide("planning_board_task_desc")
                                    action Show("planning_board_confirm_task", None, planning_board, subtask)

                else:
                    textbutton task.name:
                        sensitive planning_board.approach is not None
                        selected planning_board.selected_task == task
                        hovered Show("planning_board_task_desc", None, task)
                        unhovered Hide("planning_board_task_desc")
                        action Show("planning_board_confirm_task", None, planning_board, task)



    # Right Side
    $ approach = planning_board.approaches[1]
    ## Need Right Selected Button.
    imagebutton:
        pos (1324, 485)
        idle "images/v14/chicks_presidency_race/planning_boards/select_approach_right.png"
        # selected_idle "images/v14/chicks_presidency_race/planning_boards/selected_approach_right.png"
        selected planning_board.approach == planning_board.approaches[1]
        action Show("planning_board_confirm_approach", None, planning_board, planning_board.approaches[1], xypos=(43, 46))

    vbox:
        pos (1052, 660)
        spacing 30
        style_prefix "task"
        xmaximum 770

        for number, task in enumerate(approach.tasks, start=1):
            hbox:
                spacing 20
                text "{}.".format(number) yalign 0.5

                if isinstance(task, list):
                    vbox:
                        spacing 10

                        for alphabet, subtask in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", task):
                            hbox:
                                spacing 15

                                text "{})".format(alphabet) yalign 0.5
                                textbutton subtask.name:
                                    sensitive planning_board.approach is not None
                                    selected planning_board.selected_task == subtask
                                    hovered Show("planning_board_task_desc", None, subtask)
                                    unhovered Hide("planning_board_task_desc")
                                    action Show("planning_board_confirm_task", None, planning_board, subtask)

                else:
                    textbutton task.name:
                        sensitive planning_board.approach is not None
                        selected planning_board.selected_task == task
                        hovered Show("planning_board_task_desc", None, task)
                        unhovered Hide("planning_board_task_desc")
                        action Show("planning_board_confirm_task", None, planning_board, task)


screen planning_board_blank(xypos):
    zorder 100

    fixed:
        pos xypos
        xysize (914, 990)

        imagebutton:
            idle "#4E91D7aa"
            action NullAction()


screen planning_board_task_desc(task):
    zorder 100

    fixed:
        xysize (804, 337)
        align (0.5, 0.5)

        add "images/v14/chicks_presidency_race/planning_boards/task_background.png"

        vbox:
            spacing 20
            xalign 0.5
            ypos 50

            text task.name:
                color "#777777"
                size 30

            text task.opinion:
                color "#777777"
                size 22

            hbox:
                spacing -10

                if len(task.people) < 4:
                    for person in task.people:
                        add person.profile_picture

                else:
                    for i in range(3):
                        add task.people[i].profile_picture
                    
                    null width 35
                    text "+{}".format(len(task.people) - 3):
                        color "#777777"
                        yalign 0.5

        text "${}".format(task.cost):
            align (1.0, 1.0)
            offset (-50, -50)
            color "#777777"


# Confirm Screens
screen planning_board_confirm_approach(planning_board, approach, xypos):
    zorder 100
    modal True

    hbox:
        xalign 0.5
        ypos 933
        spacing 40

        imagebutton:
            idle "images/v14/chicks_presidency_race/planning_boards/confirm.png"
            action [SetField(planning_board, "approach", approach), Show("planning_board_blank", None, xypos), Hide("planning_board_confirm_approach")]

        imagebutton:
            idle "images/v14/chicks_presidency_race/planning_boards/cancel.png"
            action Hide("planning_board_confirm_approach")


screen planning_board_confirm_task(planning_board, task):
    zorder 100
    modal True

    hbox:
        xalign 0.5
        ypos 933
        spacing 40

        imagebutton:
            idle "images/v14/chicks_presidency_race/planning_boards/confirm.png"
            action [SetField(planning_board, "selected_task", task), Hide("planning_board_confirm_task"), Hide("planning_board_task_desc"), Hide("planning_board_blank"), Return()]

        imagebutton:
            idle "images/v14/chicks_presidency_race/planning_boards/cancel.png"
            action [Hide("planning_board_confirm_task"), Hide("planning_board_task_desc")]


style task_text is text:
    size 23 


style task_button_text is text:
    size 23
    font "fonts/OpenSans-Bold.ttf"
    outlines [(0, "#000", 0, 0)]
    idle_color "#fff"
    hover_color "#FFD166"
    selected_color "#FFD166"