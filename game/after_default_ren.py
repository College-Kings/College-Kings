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

    store.pb_girls = {
        store.amber: {
            "frat_requirement": None,
            "preferred_reputation": Reputations.POPULAR,
            "possible_relationships": (
                Relationship.FRIEND,
                Relationship.KISSED,
                Relationship.FWB,
            ),
        },
        store.aubrey: {
            "frat_requirement": None,
            "preferred_reputation": Reputations.POPULAR,
            "possible_relationships": (Relationship.FRIEND, Relationship.FWB),
        },
        store.chloe: {
            "frat_requirement": None,
            "preferred_reputation": Reputations.POPULAR,
            "possible_relationships": (
                Relationship.FRIEND,
                Relationship.FWB,
                Relationship.GIRLFRIEND,
            ),
        },
        store.emily: {
            "frat_requirement": None,
            "preferred_reputation": Reputations.LOYAL,
            "possible_relationships": (Relationship.FRIEND, Relationship.FWB),
        },
        store.lauren: {
            "frat_requirement": None,
            "preferred_reputation": Reputations.LOYAL,
            "possible_relationships": (
                Relationship.FRIEND,
                Relationship.KISSED,
                Relationship.GIRLFRIEND,
            ),
        },
        store.lindsey: {
            "frat_requirement": None,
            "preferred_reputation": Reputations.POPULAR,
            "possible_relationships": (
                Relationship.FRIEND,
                Relationship.KISSED,
                Relationship.FWB,
            ),
        },
        store.ms_rose: {
            "frat_requirement": Frat.WOLVES,
            "preferred_reputation": Reputations.CONFIDENT,
            "possible_relationships": (
                Relationship.FRIEND,
                Relationship.KISSED,
                Relationship.FWB,
            ),
        },
        store.nora: {
            "frat_requirement": None,
            "preferred_reputation": Reputations.CONFIDENT,
            "possible_relationships": (
                Relationship.FRIEND,
                Relationship.FWB,
            ),
        },
        store.penelope: {
            "frat_requirement": None,
            "preferred_reputation": Reputations.CONFIDENT,
            "possible_relationships": (
                Relationship.FRIEND,
                Relationship.DATING,
            ),
        },
        store.riley: {
            "frat_requirement": None,
            "preferred_reputation": Reputations.CONFIDENT,
            "possible_relationships": (
                Relationship.FRIEND,
                Relationship.KISSED,
                Relationship.FWB,
            ),
        },
        store.samantha: {
            "frat_requirement": Frat.APES,
            "preferred_reputation": Reputations.LOYAL,
            "possible_relationships": (
                Relationship.FRIEND,
                Relationship.KISSED,
                Relationship.FWB,
            ),
        },
    }


store.pb_girls = {}
store.pb_extra_options = ()
store.pb_advanced_options = ()

config.after_default_callbacks.append(add_applications_to_phone)
config.after_default_callbacks.append(create_pb_variables)
