from game.phone.Phone_ren import Phone
from game.phone.simplr.simplr_ren import Simplr
from game.phone.tracker.tracker_ren import tracker
from game.phone.calendar.calendar_ren import calendar_app

from renpy import store, config
from renpy.exports import ToggleVariable

from game.characters.Relationship_ren import Relationship
from game.characters.Frat_ren import Frat
from game.reputation.Reputations_ren import Reputations

phone = Phone()
simplr_app = Simplr()

"""renpy
init python:
"""


def phone_setup() -> None:
    try:
        phone.applications.remove(tracker)
    except ValueError:
        pass
    try:
        phone.applications.remove(calendar_app)
    except ValueError:
        pass

    simplr_app.pending_contacts = [
        store.beth,
        store.iris,
        store.samantha,
        store.emmy,
    ]


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

config.after_default_callbacks.append(phone_setup)
config.after_default_callbacks.append(create_pb_variables)
