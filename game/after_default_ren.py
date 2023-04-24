from renpy import store, config, persistent

"""renpy
init python:
"""


def add_applications_to_phone() -> None:
    store.phone.applications = (
        store.messenger,
        store.achievement_app,
        store.relationship_app,
        store.kiwii,
        store.reputation_app,
    )


def check_hidden_tutorials() -> None:
    if isinstance(persistent.hidden_tutorials, set):
        persistent.hidden_tutorials = {
            "fight_preparation_tutorial": False,
            "fight_tutorial": False,
            "free_roam_tutorial": False,
            "phone_tutorial": False,
            "reputation_tutorial": False,
        }


config.after_default_callbacks.append(add_applications_to_phone)
config.after_default_callbacks.append(check_hidden_tutorials)
