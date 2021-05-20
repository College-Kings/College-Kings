# Grayson in Room
# Location: MC Apes Room
# Outfits: MC Outfit 2, Grayson Outfit 2
# Time: Tuesday Night

label gray_in_room:
    scene v8sgir1 # TPP. Show MC working at his desk in his Apes room.
    with fade

    u "(What the?!)"

    play music "music/m15punk.mp3"
    queue music ["music/m16punk.mp3", "music/m7punk.mp3"]

    scene v8sgir2 # FPP. Show Grayson barging through MC's door, slight intimidating expression, Grayson mouth open.
    with dissolve

    gr "Come with me."

    scene v8sgir3 # FPP. Show Grayson now stood in MC's room, slight intimidating expression, mouth closed.
    with dissolve

    u "What?"

    scene v8sgir3a # FPP. Same camera as v8sgir3, Grayson mouth open, gesturing MC to come with him.
    with dissolve

    gr "Now."

    scene v8sgir4 # TPP. Show MC getting up from his desk to follow Grayson, Grayson looking at MC with intimidating expression, MC confused expression.
    with dissolve

    u "(So fucking weird, dude.)"

    scene v8sgir5 # TPP. Show Grayson leaving MC's room with MC trailing behind him.
    with dissolve

    jump for_w_gray
