init python:
    class ChecklistItem:
        def __init__(self, name):
            self.name = name

            self.complete = False


    class Checklist:
        def __init__(self):
            self.items = []

        def __getitem__(self, index):
            if _in_replay:
                return ChecklistItem("Replay Template")
            else:
                return self.items[index]

        def __iter__(self):
            return iter(self.items)

        def __len__(self):
            return len(self.items)

        def add_item(self, name):
            self.items.append(ChecklistItem(name))

        def get_completed(self):
            return filter(lambda item: item.complete, self.items)

        def reset(self):
            self.items = []

