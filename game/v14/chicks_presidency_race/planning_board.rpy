init python:
    class PlanningBoardApproach:
        def __init__(self, id, name, opinion):
            self.id = id
            self.name = name
            self.opinion = opinion

            self.tasks = []
            self.completed = False


    class PlanningBoardTask:
        def __init__(self, name, opinion, people, cost):
            self.name = name
            self.opinion = opinion
            self.cost = cost

            if people is None: self.people = []
            else: self.people = people

            self.completed = False


    class PlanningBoard:
        def __init__(self, background, background_color, money=0):
            self.background = background
            self.background_color = background_color
            self.money = money

            self.approaches = {}
            self.approach = None
            self.selected_task = None

        def add_approach(self, id, name, opinion=""):
            approach = PlanningBoardApproach(id, name, opinion)
            self.approaches[id] = approach
            return approach

        def add_task(self, approach_id, name, opinion="", people=None, cost=0):
            approach = self.approaches[approach_id]
            task = PlanningBoardTask(name, opinion, people, cost)
            approach.tasks.append(task)
            return task

        def add_subtask(self, approach_id, name, opinion="", people=None, cost=0):
            approach = self.approaches[approach_id]
            subtask = PlanningBoardTask(name, opinion, people, cost)
            if approach.tasks and (isinstance(approach.tasks[-1], list)):
                approach.tasks[-1].append(subtask)
            else:
                approach.tasks.append([subtask])
            return subtask

        def get_total_cost(self):
            for task in self.approach.tasks:
                total_cost = 0
                try: total_cost += task.cost
                except AttributeError: total_cost = self.selected_task.cost

            return total_cost


screen planning_board(planning_board):
    tag planning_board
    zorder 100
    modal True
    
    add planning_board.background

    # Left Side
    $ approach = planning_board.approaches.values()[0]

    imagebutton:
        pos (435, 502)
        idle "images/v14/chicks_presidency_race/planning_boards/select_approach_left.webp"
        selected_idle "images/v14/chicks_presidency_race/planning_boards/selected_approach_left.webp"
        selected_hover "images/v14/chicks_presidency_race/planning_boards/selected_approach_left.webp"
        selected planning_board.approach == approach
        hovered Show("planning_board_approach_desc", None, approach)
        unhovered Hide("planning_board_approach_desc")
        action [SetField(planning_board, "approach", approach, None), Show("planning_board_confirm_approach", None, "Please select optional tasks", background=planning_board.background_color, xypos=(963, 46))]

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
                                    action [SetField(planning_board, "selected_task", subtask), Show("planning_board_confirm_tasks", None, planning_board)]

                else:
                    textbutton task.name:
                        sensitive planning_board.approach is not None
                        selected planning_board.approach == approach
                        hovered Show("planning_board_task_desc", None, task)
                        unhovered Hide("planning_board_task_desc")
                        action NullAction()

    # Right Side
    $ approach = planning_board.approaches.values()[1]

    imagebutton:
        pos (1324, 485)
        idle "images/v14/chicks_presidency_race/planning_boards/select_approach_right.webp"
        selected_idle "images/v14/chicks_presidency_race/planning_boards/selected_approach_right.webp"
        selected_hover "images/v14/chicks_presidency_race/planning_boards/selected_approach_right.webp"
        selected planning_board.approach == approach
        hovered Show("planning_board_approach_desc", None, approach)
        unhovered Hide("planning_board_approach_desc")
        action [SetField(planning_board, "approach", approach, None), Show("planning_board_confirm_approach", None, "Please select optional tasks", background=planning_board.background_color, xypos=(43, 46))]

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
                                    if subtask.cost <= planning_board.money:
                                        action [SetField(planning_board, "selected_task", subtask), Show("planning_board_confirm_tasks", None, planning_board)]
                                    else:
                                        action NullAction()

                else:
                    textbutton task.name:
                        sensitive planning_board.approach is not None
                        selected planning_board.approach == approach
                        hovered Show("planning_board_task_desc", None, task)
                        unhovered Hide("planning_board_task_desc")
                        action NullAction()

    if not renpy.get_screen("planning_board_bottom"):
        use planning_board_help("Please select an approach")


screen planning_board_blank(background_color, xypos):
    zorder 100

    fixed:
        pos xypos
        xysize (914, 990)

        imagebutton:
            idle background_color + "aa"
            action NullAction()


screen planning_board_approach_desc(approach):
    zorder 100

    fixed:
        xysize (804, 337)
        align (0.5, 0.5)

        add "images/v14/chicks_presidency_race/planning_boards/task_background.webp"

        vbox:
            spacing 20
            pos (50, 30)
            xsize 704

            text approach.name:
                color "#777777"
                size 30

            text approach.opinion:
                color "#777777"
                size 22


screen planning_board_task_desc(task):
    zorder 100

    fixed:
        xysize (804, 337)
        align (0.5, 0.5)

        add "images/v14/chicks_presidency_race/planning_boards/task_background.webp"

        vbox:
            spacing 20
            pos (50, 30)
            xsize 704

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
                        add Transform(person.profile_picture, size=(55, 55))

                else:
                    for i in range(3):
                        add Transform(task.people[i].profile_picture, size=(55, 55))
                    
                    null width 35
                    text "+{}".format(len(task.people) - 3):
                        color "#777777"
                        yalign 0.5

        text "${}".format(task.cost):
            align (1.0, 1.0)
            offset (-50, -50)
            color "#777777"


screen planning_board_help(message=""):
    tag planning_board_bottom
    zorder 200

    text message:
        italic True
        xalign 0.5
        ypos 933


# Confirm Screens
screen planning_board_confirm_approach(message, background, xypos):
    tag planning_board_bottom
    zorder 100

    hbox:
        xalign 0.5
        ypos 933
        spacing 40

        imagebutton:
            idle "images/v14/chicks_presidency_race/planning_boards/confirm.webp"
            action [Show("planning_board_blank", None, background, xypos), Show("planning_board_help", None, message), Hide("planning_board_confirm_approach")]

        imagebutton:
            idle "images/v14/chicks_presidency_race/planning_boards/cancel.webp"
            action Hide("planning_board_confirm_approach")


screen planning_board_confirm_tasks(planning_board):
    tag planning_board_bottom
    zorder 100

    hbox:
        xalign 0.5
        ypos 933
        spacing 40

        imagebutton:
            idle "images/v14/chicks_presidency_race/planning_boards/confirm.webp"
            sensitive planning_board.get_total_cost() <= self.money
            action [Hide("planning_board_confirm_tasks"), Hide("planning_board_task_desc"), Hide("planning_board_blank"), Return()]

        imagebutton:
            idle "images/v14/chicks_presidency_race/planning_boards/cancel.webp"
            action [SetField(planning_board, "selected_task", None), Show("planning_board_help", message="Please select optional tasks"), Hide("planning_board_confirm_tasks"), Hide("planning_board_task_desc")]


style task_text is text:
    size 23 


style task_button_text is text:
    size 23
    font "fonts/OpenSans-Bold.ttf"
    outlines [(0, "#000", 0, 0)]
    idle_color "#aaa"
    insensitive_color "#aaa"
    hover_color "#FFD166"
    selected_color "#fff"