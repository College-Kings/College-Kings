from dataclasses import dataclass
from typing import Callable, ClassVar

_: Callable[[str], str] = lambda x: x

path_builder: bool
_in_replay: bool

"""renpy
init python:
"""


@dataclass
class Achievement:
    all_achievements: ClassVar[dict[str, "Achievement"]] = {}

    _id: str
    _description: str
    _hidden: bool = False
    _hide_description: bool = False

    @property
    def id(self) -> str:
        return self._id

    @property
    def description(self) -> str:
        return self._description

    @property
    def hidden(self) -> bool:
        return self._hidden

    @hidden.setter
    def hidden(self, value: bool) -> None:
        self._hidden = value

    @property
    def hide_description(self) -> bool:
        return self._hide_description

    @property
    def display_name(self) -> str:
        return self.id.replace("_", " ")

    def register(self) -> "Achievement":
        self.all_achievements[self.id] = self

        # Add achievements to renpy/steam
        achievement.register(self.id)  # type: ignore
        achievement.sync()  # type: ignore
        return self

    def grant(self) -> None:
        if path_builder or _in_replay:
            return

        renpy.show(self.id, [show_achievement])  # type: ignore
        achievement.grant(self.id)  # type: ignore
        achievement.sync()  # type: ignore


def grant_achievement(achievement_: str) -> None:
    if achievement_ in Achievement.all_achievements:
        Achievement.all_achievements[achievement_].grant()


# ACHIEVEMENT ITEMS HERE
Achievement("open_wound", _("Tell off Emily"))
Achievement("no_hard_feelings", _("Play nice with Emily"))
Achievement("keep_it_moving", _("Hit on Nora"))
Achievement("romeo", _("Kiss Lauren"))
Achievement("big_mouth", _("Threaten Cameron"))

# v2
Achievement("mixed_feelings", _("Decline Lauren"))
Achievement("the_notorious", _("Win your first fight"))
Achievement("a_new_beginning", _("Lauren likes you"))
Achievement("over_it", _("Let Benjamin make a move"))

# v3
Achievement("not_now_mom", _("Decline Julia's call"))
Achievement("lips_dont_lie", _("Kiss Riley at the Park"))
Achievement("truth_hurts", _("Tell Lauren about Aubrey"))

# v4
Achievement("relight_the_fire", _("Tell Julia about Emily"))
Achievement("rematch", _("Buy Chloe the volleyball"))
Achievement("keen_eye", _("Pick the muffin"))

# v5
Achievement("on_the_low", _("Deny PDA with Lauren"))
Achievement("peta_public_enemy", _("Kill dog as animal lover"))
Achievement("snitch", _("Tell the school"))

# v6
Achievement("bros_before_hoes", _("Help Imre"))
Achievement("monkey_business", _("Join the Apes"))
Achievement("not_my_business", _("Don't disturb Ms. Rose"))
Achievement("reignition", _("Kiss Emily back"))
Achievement("credulous", _("Trust Chloe"))
Achievement("seems_fishy", _("Don't meet Grayson"))
Achievement("strike", _("Kiss Penelope"))

# v7
Achievement("true_to_self", _("Walk home with Riley"))
Achievement("silverback", _("Pledge to the Apes"))
Achievement("wolfpack", _("Pledge to the Wolves"))
Achievement("lee_way", _("Pull down Mr. Lee's pants"))
Achievement("ecstatic", _("Bunk homecoming with Amber"))
Achievement("slow_and_steady", _("End homecoming with Lauren"))
Achievement("playing_with_fire", _("End homecoming with Riley"))
Achievement("homecoming_queen", _("End homecoming with Chloe"))

# v8
Achievement("thick_and_thin", _("Help Penelope"))
Achievement("text_with_an_s", _("Return to sender"))
Achievement("lucky_7", _("Flashing lights at the arcade"))
Achievement("ip_man", _("Win the alley fight"))
Achievement("get_a_room", _("Stay with Amber at Josh's"))
Achievement("helping_hand", _("Help Nora hand out flyers for the trip"))
Achievement("up_for_more", _("Flirt with Chloe at the Steakhouse"))

# v9
Achievement("relaxing_day", _("Have fun with Aubrey at the lake"))
Achievement("king_of_the_north", _("The King is heading North"))
Achievement("back_down", _("Punch the guy in the hallway"))
Achievement("second_date", _("Get a second date with Evelyn"))
Achievement("cheat_day", _("Skip the gym and get with Riley"))
Achievement("the_wrong_time", _("Don't kiss Lindsey"))

# v10
Achievement("lights_out", _("Beat Ryan on Hard difficulty at the Brawl"))
Achievement("fright_club", _("Don't fight Ryan at the Brawl"))
Achievement("golden_boy", _("Beat Imre on Hard difficulty at the Brawl"))
Achievement("bros_before_blows", _("Don't fight Imre at the Brawl"))
Achievement("rawr_im_a_lion", _("Tell Lauren you like Lions"))
Achievement("getting_clean", _("Have fun in the bathroom"))
Achievement("forbidden_romance", _("Kiss Ms. Rose"))
Achievement("rough_rider", _("Have fun at the skatepark"))
Achievement("family_secrets", _("Find out Nora and Ms. Rose are family"))
Achievement("on_the_court", _("Have a rematch with Chloe"))
Achievement("hard_decisions", _("Tell Chloe what Nora said"))

# v11
Achievement("perry_mason", _("Successfully defend Penelope"))
Achievement("candy_crusher", _("Have fun with Candy"))
Achievement("hold_your_horses", _("Balance the horse at the end of the manhunt"))
Achievement(
    "off_your_high_horse", _("Don't balance the horse at the end of the manhunt")
)
Achievement("cross_your_heart", _("Kiss Penelope at the airport"))
Achievement("on_target", _("Hit a bullseye at Duncan's"))
Achievement("just_a_theory", _("Tell Riley dinosaurs aren't real"))
Achievement("fruity", _("Have a cocktail at the bar"))
Achievement("earn_your_owl", _("Get all the HP answers right"))
Achievement(
    "political_strategist",
    _("Tell Autumn you're into politics and encourage Lindsey to run"),
)
Achievement("two_timer", _("Date both Lauren and Chloe"))
Achievement("dont_just_stand_there", _("Break Imre and Ryan apart"))
Achievement("pretty_in_pink", _("Nora buys the pink bra"))

# v12
Achievement("good_vs_evil", _("Penelope understands you"))
Achievement("a_person_like_me", _("You see yourself as Penelope's husband material"))
Achievement("zero_to_hero", _("Tell Riley you are poor"))
Achievement("doctors_orders", _("Accept Nurse Aubrey's advances"))
Achievement("mercy_killing", _("Kill Imre"))
Achievement("talk_murder_to_me", _("Kill Samantha"))
Achievement("best_for_last", _("Charli is your final kill"))
Achievement("weapons_down", _("Don't kill anyone"))
Achievement("killing_spree", _("Kill enough people to win the game"))
Achievement("mass_casualties", _("Kill everyone (including optional characters)"))
Achievement(
    "thrown_to_the_lions",
    _("Encourage Lindsey to run but then tell Aubrey and Chloe about it"),
)
Achievement("you_may_kiss_the_bride", _("Kiss Nora at the altar"))
Achievement("a_bet_is_a_bet", _("Embarrassing Kiwii picture for losing the race"))
Achievement("brotherhood_of_men", _("Defend Chris every time as a Wolf"))
Achievement("best_frenemies", _("Defend Chris every time as an Ape"))
Achievement("worth_the_wait", _("Consummate an exclusive relationship with Lauren"))
Achievement("inside_job", _("Have sex with Nora as a Wolf"))
Achievement("all_is_fair_in_love_and_war", _("Have sex with Nora as an Ape"))
Achievement("city_of_love", _("Have sex with Lauren, Nora, Ms. Rose and Lindsey"))

# v13
Achievement("indecisive", _("Help neither Chloe nor Lindsey"))
Achievement("funny_night", _("Yes Penelope, you're flying"))
Achievement("gentlemen_prefer_gingers", _("Bail on Lauren's cuddles"))
Achievement("flush_flush", _("Flush Charli's toothbrush"))
Achievement("he_is_done", _("Expose Charli"))
Achievement("urbanizer_womanizer", _("Tell Emmy and Lauren you're a city man"))
Achievement("romantic_heart", _("Score a date with Kourtney"))
Achievement("bro_moment", _("Cameron recognizes your pure intentions"))
Achievement("an_honest_liar", _("Own up to Clipps"))
Achievement("we_like_them_wild", _("Reveal a new side of Chloe"))
Achievement("voyeur", _("What are they doing over there?"))
Achievement("dammit_emily", _("Angry bathroom sex"))
Achievement("calm_down_big_fella", _("Respect Nora"))

# v14
Achievement("ready_player_three", _("Three-way with Riley and Aubrey"))
Achievement("saving_ryans_privates", _("Don't let Ryan catch an STD"))
