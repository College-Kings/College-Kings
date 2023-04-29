from renpy import store, config
from renpy.exports import ToggleVariable

from game.characters.Relationship_ren import Relationship
from game.characters.Frat_ren import Frat
from game.reputation.Reputations_ren import Reputations

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


def create_pb_variables() -> None:
    store.pb_extra_options = (
        ("Took Chloe to the homecoming date", ToggleVariable("hcGirl", "chloe")),
        ("Took Riley to the homecoming date", ToggleVariable("hcGirl", "riley")),
        ("Took Lauren to the homecoming date", ToggleVariable("hcGirl", "lauren")),
        ("Took Penelope to the homecoming date", ToggleVariable("hcGirl", "penelope")),
        ("Took Emily to the homecoming date", ToggleVariable("hcGirl", "emily")),
        ("Took Amber to the homecoming date", ToggleVariable("hcGirl", "amber")),
    )

    store.pb_advanced_options = (
        ("Invite Emily to Europe", ToggleVariable("emily_europe")),
        ("Invite Emily to Europe", ToggleVariable("emily_europe")),
    )

    store.pb_girls = (
        (
            store.amber,
            None,
            Reputations.POPULAR,
            (Relationship.FRIEND, Relationship.KISSED, Relationship.FWB),
        ),
        (
            store.aubrey,
            None,
            Reputations.POPULAR,
            (Relationship.FRIEND, Relationship.FWB),
        ),
        (
            store.chloe,
            None,
            Reputations.POPULAR,
            (
                Relationship.FRIEND,
                Relationship.FWB,
                Relationship.GIRLFRIEND,
            ),
        ),
        (store.emily, None, Reputations.LOYAL, (Relationship.FRIEND, Relationship.FWB)),
        (
            store.lauren,
            None,
            Reputations.LOYAL,
            (
                Relationship.FRIEND,
                Relationship.KISSED,
                Relationship.GIRLFRIEND,
            ),
        ),
        (
            store.lindsey,
            None,
            Reputations.POPULAR,
            (Relationship.FRIEND, Relationship.KISSED, Relationship.FWB),
        ),
        (
            store.ms_rose,
            Frat.WOLVES,
            Reputations.CONFIDENT,
            (Relationship.FRIEND, Relationship.KISSED, Relationship.FWB),
        ),
        (
            store.nora,
            None,
            Reputations.CONFIDENT,
            (
                Relationship.FRIEND,
                Relationship.FWB,
            ),
        ),
        (
            store.penelope,
            None,
            Reputations.CONFIDENT,
            (
                Relationship.FRIEND,
                Relationship.DATING,
            ),
        ),
        (
            store.riley,
            None,
            Reputations.CONFIDENT,
            (Relationship.FRIEND, Relationship.KISSED, Relationship.FWB),
        ),
        (
            store.samantha,
            Frat.APES,
            Reputations.LOYAL,
            (Relationship.FRIEND, Relationship.KISSED, Relationship.FWB),
        ),
    )


store.pb_girls = ()
store.pb_extra_options = ()
store.pb_advanced_options = ()

config.after_default_callbacks.append(add_applications_to_phone)
config.after_default_callbacks.append(create_pb_variables)
