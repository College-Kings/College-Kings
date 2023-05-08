# SCENE 13: Your Room Thurs Afternoon
# Locations: MC's room in Wolves house, MC's room in Apes house
# Characters: MC (Outfit 1)
# Time: Wednesday Afternoon

label thurs_aft_room:
    if mc.frat == Frat.WOLVES:
        scene v9tar1 # TPP. Show MC sitting at his desk in his Wolves room trying to study.
        with fade

        u "(What a day. Hot babes and assholes roaming the hallways, catching me off guard after class.)"

        scene v9tar1a # TPP. Same camera as v9tar1, MC turns the page of his book.
        with dissolve

        if hl_punch:
            u "(Well, that guy got what he deserved, either way. And seems like I did put up quite a show for the hotness across the hallway.)"

        else:
            u "(Shouldn't have taken my eyes off that fucker. Catching me off guard like that. But at least I got Lindsey's number, so it wasn't all bad.)"

        scene v9tar2 # TPP. Show MC leaning back in his chair, looking bored.
        with dissolve

        u "(I guess I should concentrate more on studying.)"

        scene v9tar1b # TPP. Same camera as v9tar1, MC turns another page in his book.
        with dissolve

        u "(Yet it seems like it's getting harder and harder, with less and less time to do it.)"

        scene v9tar3 # TPP. Show MC closing the book on his desk and leaning back into his chair
        with dissolve

        u "(I know. I'll just relax for a bit. I need a breather from all that is going on.)"

        scene v9tar3a # TPP. Same camera as v9tar3, MC mouth closed.
        with dissolve

        u "(I guess I got too used to the company around here. Things aren't really fun when alone.)"

        scene v9tar4 # TPP. Show MC leaning further back in his chair, playing legs on desk.
        with dissolve

        u "(Well, fuck.)"

        jump v9_thur_room_w_seb

    else:
        scene v9tar5 # TPP. Show MC sitting at his desk in his Apes room trying to study.
        with fade

        u "(What a day. Hot babes and assholes roaming the hallways, catching me off guard after class.)"

        scene v9tar5a # TPP. Same camera as v9tar1, MC turns the page of his book.
        with dissolve

        if hl_punch:
            u "(Well, that guy got what he deserved, either way. And seems like I did put up quite a show for the hotness across the hallway.)"

        else:
            u "(Shouldn't have taken my eyes off that fucker. Catching me off guard like that. But at least I got Lindsey's number, so it wasn't all bad.)"

        scene v9tar6 # TPP. Show MC leaning back in his chair, looking bored.
        with dissolve

        u "(I guess I should concentrate more on studying.)"

        scene v9tar5b # TPP. Same camera as v9tar1, MC turns another page in his book.
        with dissolve

        u "(Yet it seems like it's getting harder and harder, with less and less time to do it.)"

        scene v9tar7 # TPP. Show MC closing the book on his desk and leaning back into his chair
        with dissolve

        u "(I'll just relax for a bit. I do need a breather from all that is going on.)"

        scene v9tar7a # TPP. Same camera as v9tar3, MC mouth closed.
        with dissolve

        u "(I guess I got too used to the company around here. Things aren't really fun when alone.)"

        scene v9tar8 # TPP. Show MC leaning further back in his chair, playing legs on desk.
        with dissolve

        u "(Well, fuck.)"

        jump v9_thur_room_w_cam
