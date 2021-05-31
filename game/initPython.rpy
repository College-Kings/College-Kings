init 999 python:
    try:
        import _renpysteam as steamAPI
    except ImportError:
        config.enable_steam = False