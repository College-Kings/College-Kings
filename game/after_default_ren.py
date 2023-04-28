from renpy import store, config
from renpy.exports import ToggleVariable, If, Function

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


def create_pb_option_variables() -> None:
    store.pb_extra_options = (
        ("Took Chloe to the homecoming date", ToggleVariable("hcGirl", "chloe")),
        ("Took Riley to the homecoming date", ToggleVariable("hcGirl", "riley")),
        ("Took Lauren to the homecoming date", ToggleVariable("hcGirl", "lauren")),
        ("Took Penelope to the homecoming date", ToggleVariable("hcGirl", "penelope")),
        ("Took Emily to the homecoming date", ToggleVariable("hcGirl", "emily")),
        ("Took Amber to the homecoming date", ToggleVariable("hcGirl", "amber")),
    )

    store.pb_advanced_options = (
        ("Invite Emily to Europe",
        ToggleVariable("emily_europe"))
    )


store.pb_extra_options = ()
store.pb_advanced_options = ()

config.after_default_callbacks.append(add_applications_to_phone)
config.after_default_callbacks.append(create_pb_option_variables)
