from renpy import store, config

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


config.after_default_callbacks.append(add_applications_to_phone)
