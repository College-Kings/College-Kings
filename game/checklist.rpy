init python:
    class ChecklistItem:
        def __init__(self, name: str):
            self.name = name

            self.complete = False


    class Checklist:
        def __init__(self):
            self.items: list[ChecklistItem] = []

        def __getitem__(self, index: int):
            if _in_replay:
                return ChecklistItem("Replay Template")
            else:
                return self.items[index]

        def __iter__(self):
            return iter(self.items)

        def __len__(self):
            return len(self.items)

        def add_item(self, name: str):
            self.items.append(ChecklistItem(name))

        def get_completed(self):
            return list(filter(lambda item: item.complete, self.items))

        def reset(self):
            self.items = []
