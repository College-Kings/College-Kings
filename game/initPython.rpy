init python:
    try:
        import _renpysteam as steam
    except ImportError:
        config.enable_steam = False