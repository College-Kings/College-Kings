label load_failed:
    python:
        renpy.execute_default_statement()

    call after_load from _call_after_load

    python:
        try:
            for i in reversed(list(label_history)):
                if renpy.has_label(i) and i.startswith("v"):
                    renpy.jump(i)
        except NameError: pass

        renpy.jump("v1_start")