# Globals
image darker_80 = Solid("#000c")
image blue_button_idle = Frame("gui/button/blue_idle.webp")
image blue_button_hover = Frame("gui/button/blue_hover.webp")
image blue_filled_button_idle = Frame("gui/button/blue_filled_idle.webp")
image blue_filled_button_hover = Frame("gui/button/blue_filled_hover.webp")
image pink_button_idle = Frame("gui/button/pink_idle.webp")
image pink_button_hover = Frame("gui/button/pink_hover.webp")

# Transitions
image sleep_transition_fast = Movie(play="images/common/sleep-transition-fast.webm", loop=False)

# Splash Screen
image splashscreen_1 = "gui/splashscreen/1.webp"
image splashscreen_2 = "gui/splashscreen/2.webp"
image splashscreen_3 = "gui/splashscreen/3.webp"


# Gui
## Alert
image alert_background = Frame("gui/alert/background.webp")

## Bar
image blue_bar = Frame("gui/bar/blue.webp")
image ruby_bar = Frame("gui/bar/ruby.webp")
image yellow_bar = Frame("gui/bar/yellow.webp")
image transparent_bar = Frame("#0000")

## Choice
image choice_button_idle = Frame("gui/choice/button_idle.webp")
image choice_button_hover = Frame("gui/choice/button_hover.webp")

## End Screen
image patreon_credits = Movie(channel="movie", play="gui/end_screen/patreon_credits.webm")

# Fights
image fight_guard_animation:
    "#000070" with Dissolve(0.5)
    pause 1.0

    "#00f" with Dissolve(0.5)
    pause 1.0

    repeat

image fight_health_animation:
    "#700000" with Dissolve(0.5)
    pause 1.0

    "#f00" with Dissolve(0.5)
    pause 1.0

    repeat

## Path Builder
image path_builder_button_idle = Frame("main_menu/path_builder/images/button_idle.webp", 24, 6)
image path_builder_button_hover = Frame("main_menu/path_builder/images/button_hover.webp", 24, 6)

## Scene Gallery
image scene_gallery_bar_base = Frame("gui/bar/bar_base.webp", 5, 10)

## Settings
image settings_bar_left = Frame("gui/settings/bar_right.webp", 14, 5)
image settings_bar_right = Frame("gui/settings/bar_right.webp", 14, 5)
image settings_bar_thumb = "gui/settings/bar_thumb.webp"

## Tutorial
image tutorial_background = Frame("gui/tutorial/background.webp", 42, 8, 8, 8)
image tutorial_left_button_idle = "gui/tutorial/left_button_idle.webp"
image tutorial_right_button_idle = "gui/tutorial/right_button_idle.webp"

## Warning
image warning_background_blue = Frame("gui/warning/background_blue.webp")

# Phone
## Common
image contact_notification = "images/phone/common/contact-notification.webp"
image back_button = "images/phone/common/back-button.webp"
image message_background = Frame("images/phone/common/message-background.webp", 20, 20)
image reply_background = Frame("images/phone/common/reply-background.webp", 20, 20)
image reply_background_idle = Frame("images/phone/common/reply-background-idle.webp")
image reply_background_hover = Frame("images/phone/common/reply-background-hover.webp")
image reply_button_idle = "images/phone/common/reply-button-idle.webp"

## Achievements
image achievement_locked = Frame("images/phone/achievements/app-assets/achievement-locked.webp", 20, 20)
image achievement_unlocked = Frame("images/phone/achievements/app-assets/achievement-unlocked.webp", 20, 20)

## Relationships
image relationships_frame_background = Frame("images/phone/relationships/app-assets/frame-background.webp")

## v1.0
# image ready_player_three = "images/achievements/v1/ready_player_three.webp" -- CK1 achievement
# image saving_ryans_privates = "images/achievements/v1/saving_ryans_privates.webp" -- CK1 achievement
image beastie_boy = "images/achievements/v1/beastie_boy.webp"
image double_agent = "images/achievements/v1/double_agent.webp"
image agree_to_disagree = "images/achievements/v1/agree_to_disagree.webp"
image how_did_you_know = "images/achievements/v1/how_did_you_know.webp"
image built_on_trust = "images/achievements/v1/built_on_trust.webp"
image wrath_of_pen = "images/achievements/v1/wrath_of_pen.webp"
image your_eyelids_are_heavy = "images/achievements/v1/your_eyelids_are_heavy.webp"
image say_chirp = "images/achievements/v1/say_chirp.webp"
image grand_theft_chloe = "images/achievements/v1/grand_theft_chloe.webp"
image clean_it_up = "images/achievements/v1/clean_it_up.webp"


## v2.0
image blue_cheese_and_sambuca = "images/achievements/v2/blue_cheese_and_sambuca.webp"
image childhood_memories = "images/achievements/v2/childhood_memories.webp"
image christmas_is_dead = "images/achievements/v2/christmas_is_dead.webp"
image counter_intelligence = "images/achievements/v2/counter_intelligence.webp"
image da_ba_dee_da_ba_dai = "images/achievements/v2/da_ba_dee_da_ba_dai.webp"
image emotional_blackmail = "images/achievements/v2/emotional_blackmail.webp"
image honey_bear = "images/achievements/v2/honey_bear.webp"
image horn_dog = "images/achievements/v2/horn_dog.webp"
image just_one_more_thing = "images/achievements/v2/just_one_more_thing.webp"
image karen = "images/achievements/v2/karen.webp"
image mmmm_donut = "images/achievements/v2/mmmm_donut.webp"
image polycurious = "images/achievements/v2/polycurious.webp"
image pumpkin_season = "images/achievements/v2/pumpkin_season.webp"
image taskmaster = "images/achievements/v2/taskmaster.webp"
image too_much_information = "images/achievements/v2/too_much_information.webp"
image what_goes_around = "images/achievements/v2/what_goes_around.webp"

## v3.0
image the_answer_to_everything = "images/achievements/v3/the_answer_to_everything.webp"
image extra_extra = "images/achievements/v3/extra_extra.webp"
image must_resist_temptation = "images/achievements/v3/must_resist_temptation.webp"
image just_curious_about_you = "images/achievements/v3/just_curious_about_you.webp"
image busy_schedule = "images/achievements/v3/busy_schedule.webp"
image perfect_date = "images/achievements/v3/perfect_date.webp"
image fours_a_crowd = "images/achievements/v3/fours_a_crowd.webp"
image defenestrated = "images/achievements/v3/defenestrated.webp"
image caught_red_handed = "images/achievements/v3/caught_red_handed.webp"
image singing_praises = "images/achievements/v3/singing_praises.webp"
image bad_hair_day = "images/achievements/v3/bad_hair_day.webp"