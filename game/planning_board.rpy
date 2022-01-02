init python:
    class PlanningBoardApproach:
        def __init__(self, id, name, opinion):
            self.id = id
            self.name = name
            self.opinion = opinion

            self.tasks = []
            self.completed = False

        @property
        def cost(self):
            return sum(task.cost for task in self.get_tasks())

        def get_tasks(self):
            tasks = []
            for task in self.tasks:
                if isinstance(task, PlanningBoardTask):
                    tasks.append(task)
                else:
                    tasks.extend(task)
            return tasks


    class PlanningBoardTask:
        def __init__(self, name, opinion, people, cost):
            self.name = name
            self.opinion = opinion
            self.cost = cost

            if people is None: self.people = []
            else: self.people = people

            self.completed = False


    class PlanningBoard:
        def __init__(self, background, money=0, style=None):
            self.background = background
            self.money = money
            self.style = style

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
            total_cost = 0
            for task in self.approach.tasks:
                try: total_cost += task.cost
                except AttributeError: total_cost += self.selected_task.cost

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
        idle "images/planning_boards/select_approach_left.webp"
        selected_idle "images/planning_boards/selected_approach_left.webp"
        selected_hover "images/planning_boards/selected_approach_left.webp"
        selected planning_board.approach == approach
        hovered Show("planning_board_approach_desc", None, approach)
        unhovered Hide("planning_board_approach_desc")
        action [SetField(planning_board, "approach", approach), Show("planning_board_help", message="Please select optional tasks")]

    vbox:
        pos (130, 600)
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
                                    sensitive planning_board.approach == approach
                                    selected planning_board.selected_task == subtask
                                    if approach.cost <= planning_board.money:
                                        unhovered Hide("planning_board_task_desc")
                                        hovered Show("planning_board_task_desc", None, subtask)
                                        action [SetField(planning_board, "selected_task", subtask), Show("planning_board_confirm_tasks", None, planning_board)]
                                    else:
                                        unhovered [Hide("planning_board_task_desc"), Show("planning_board_help", message="Please select an approach")]
                                        hovered Show("planning_board_help", message="{color=#f00}Not enough money to select task.")
                                        action NullAction()
                                    if planning_board.style is not None:
                                        text_style planning_board.style

                else:
                    textbutton task.name:
                        sensitive planning_board.approach == approach
                        selected planning_board.approach == approach
                        hovered Show("planning_board_task_desc", None, task)
                        unhovered Hide("planning_board_task_desc")
                        action NullAction()
                        if planning_board.style is not None:
                            text_style planning_board.style


    text "Budget: ${}".format(planning_board.money):
        align (0.5, 0.1)
        outlines [(1, "#000", 0, 0)]

    # Right Side
    $ approach = planning_board.approaches.values()[1]

    imagebutton:
        pos (1324, 485)
        idle "images/planning_boards/select_approach_right.webp"
        selected_idle "images/planning_boards/selected_approach_right.webp"
        selected_hover "images/planning_boards/selected_approach_right.webp"
        selected planning_board.approach == approach
        hovered Show("planning_board_approach_desc", None, approach)
        unhovered Hide("planning_board_approach_desc")
        action [SetField(planning_board, "approach", approach, None), Show("planning_board_help", message="Please select optional tasks")]

    vbox:
        pos (1052, 600)
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
                                    sensitive planning_board.approach == approach
                                    selected planning_board.selected_task == subtask
                                    if approach.cost <= planning_board.money:
                                        unhovered Hide("planning_board_task_desc")
                                        hovered Show("planning_board_task_desc", None, subtask)
                                        action [SetField(planning_board, "selected_task", subtask), Show("planning_board_confirm_tasks", None, planning_board)]
                                    else:
                                        unhovered [Hide("planning_board_task_desc"), Show("planning_board_help", message="Please select an approach")]
                                        hovered Show("planning_board_help", message="{color=#f00}Not enough money to select task.")
                                        action NullAction()
                                    if planning_board.style is not None:
                                        text_style planning_board.style

                else:
                    textbutton task.name:
                        sensitive planning_board.approach == approach
                        selected planning_board.approach == approach
                        hovered Show("planning_board_task_desc", None, task)
                        unhovered Hide("planning_board_task_desc")
                        action NullAction()
                        if planning_board.style is not None:
                            text_style planning_board.style

    
    on "show" action Show("planning_board_help", message="Please select an approach")


screen planning_board_approach_desc(approach):
    zorder 100

    fixed:
        xysize (804, 337)
        align (0.5, 0.5)

        add "images/planning_boards/task_background.webp"

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

        add "images/planning_boards/task_background.webp"

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
        outlines [(1, "#000", 0, 0)]


# Confirm Screens
screen planning_board_confirm_tasks(planning_board):
    tag planning_board_bottom
    zorder 100

    hbox:
        xalign 0.5
        ypos 933
        spacing 40

        imagebutton:
            idle "images/planning_boards/confirm.webp"
            sensitive planning_board.get_total_cost() <= planning_board.money
            action [Hide("planning_board_bottom"), Hide("planning_board_task_desc"), Hide("planning_board_blank"), Return()]

        imagebutton:
            idle "images/planning_boards/cancel.webp"
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

style lindsey_board is task_button_text:
    idle_color "#b9b18d"
    insensitive_color "#b9b18d"
    hover_color "#877E54"
    selected_color "#877E54"